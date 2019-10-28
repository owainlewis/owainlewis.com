import os, os.path, time
import re
import subprocess

POST_DIR = '_posts'

OUT_DIR  = 'posts'

class PostData(object):
    """ A utility class for extracting link text information """

    def __init__(self, file_name, file_path):
        self.file_name = file_name
        self.file_path = file_path

    def get_title(self):
        normalised = re.sub('.md', '', self.file_name)
        return ' '.join(normalised.split('-')).title()

    def get_last_modified(self):
        created = time.gmtime(os.path.getctime(self.file_path))
        return time.strftime('%d/%m/%Y', created)

    def get_link_ref(self):
        normalised = re.sub('.md', '.html', self.file_name)
        return '/%s/%s' % (OUT_DIR, normalised)

    def link_text(self):
        return "### %s\n## [%s](%s)" % \
            (self.get_last_modified(), self.get_title(), self.get_link_ref())


def run_cmd(cmd):
    print('Running command %s' % cmd)
    p = subprocess.Popen(cmd, shell=True, \
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print(line)
    return p.wait()


def build_post_index():
    posts = [post for post in os.listdir("_posts") \
             if not post == 'index.md']
    with open("_posts/index.md", "w+") as f:
        for post in posts:
            pd = PostData(post, f.name)
            f.write(pd.link_text() + '\n')


def pandoc_compile_command(post_file_name):
    """ Generates the shell command required by Pandoc """
    output_cmd = '-o %s/%s' % (OUT_DIR, re.sub('.md', '.html', post_file_name))
    post_relative_path = '%s/%s' % (POST_DIR, post_file_name)
    lines = ['pandoc',
             '-H static/html/header.html',
             '-A static/html/footer.html',
             post_relative_path,
             output_cmd]
    return ' '.join(lines)


def pandoc_compile():
    for f in os.listdir(POST_DIR):
        cmd = pandoc_compile_command(f)
        run_cmd(cmd)


def main():
    pandoc_compile()


if __name__ == '__main__':
    print('Building site...')
    main()

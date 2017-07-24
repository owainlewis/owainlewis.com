import os, os.path, time
import re

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
        last_mod = time.gmtime(os.path.getmtime(self.file_path))
        return time.strftime('%d/%m/%Y', last_mod)

    def get_link_ref(self):
        normalised = re.sub('.md', '.html', self.file_name)
        return '/posts/%s' % normalised

    def link_text(self):
        return "*[%s](%s) - %s" % \
            (self.get_title(), self.get_link_ref(), self.get_last_modified())


def build_post_index():
    posts = [post for post in os.listdir("_posts") \
             if not post == 'index.md']
    with open("_posts/index.md", "w+") as f:
        for post in posts:
            pd = PostData(post, f.name)
            f.write(pd.link_text() + '\n')


def pandoc_compile_command(post_file_name):
    """ Generates the shell command required by Pandoc """
    output_cmd = '-o posts/%s' % re.sub('.md', '.html', post_file_name)
    post_relative_path = '_/posts/%s' % post_file_name
    lines = ['pandoc',
             '-H static/html/header.html',
             '-A static/html/footer.html',
             post_relative_path,
             output_cmd]
    return ' '.join(lines)


def pandoc_compile():
    pass


def main():
    print('Building post index.md file')
    build_post_index()
    pandoc_compile()


if __name__ == '__main__':
    main()

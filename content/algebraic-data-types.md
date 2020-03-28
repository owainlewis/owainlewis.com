% Algebraic Data Types
% Owain Lewis
% 28/04/2020

# Algebraic Data Types (ADT)

Algebraic Data Types, are used in functional programming as a way of representing data. An Algebraic Data Type is a type that’s formed by composing other types.

There are two variants; sum types (OR) and product types (AND).

- Sum (A | B, meaning A OR B but not both)
- Product ( A + B, meaning A and B)

## Sum Types

A sum type, also known as a tagged union, is a type that can be one of multiple possible options.

Examples of sum types:

- A boolean value is either True OR False
- A list is either empty ([]) OR an item appended to another list (a : [b])
- A traffic light is either Red OR Amber OR Green

```haskell
data Bool = False | True
```

The most general sum type in Haskell is Either. A value of type Either a b can be either a OR b but not both.

```haskell
data Either a b =
	  Left a
	| Right b
```

## Product Types (Tuples, Records)

Product types are created by combining two or more types with AND. The canonical implementation of a product of two types in a programming language is a pair (a, b).

Examples of product types:

- A Person has a Name (String), Age (Integer) and Email Address (String)

```haskell
data Person =
	Person String Int String

data Person = Person {
	name  :: String,
	age   :: Int,
	email :: String
}
```

In most programming languages, combining types with AND is often the only way to construct new types.

## Further Reading

[https://codewords.recurse.com/issues/three/algebra-and-calculus-of-algebraic-data-types](https://codewords.recurse.com/issues/three/algebra-and-calculus-of-algebraic-data-types)

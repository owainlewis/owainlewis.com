% Bifunctor
% Owain Lewis
% 28/04/2020

# Bifunctor

**Status: WIP**

This article will look at bifunctors, and how they can be used in the real world. This article assumes some knowlege of functors.

A bifunctor is a type class of types which give rise to two independent, covariant functors. Some common uses of bifunctor include mapping over `Either` and `Tuple2` types. While functor provides a map operation that takes a function `A = >B` and applies that function over a context `F[A] => F[B]`, a bifunctor offers us the bimap operation which takes two functions `(A = >B, C => D)` and applies one or both of these functions over a context.

In Haskell, we can define a bifunctor as:

```haskell
class Bifunctor (f:: * -> * -> *) where
  bimap  :: (a -> b) -> (c -> d) -> f a c -> f b d
  first  :: (a -> b) -> f a c -> f b c
  second :: (b -> c) -> f a b -> f a c
  {-# MINIMAL bimap | first, second #-}
```

A Scala implementation of `bimap` for both `Tuple2` and `Either`:

```scala
trait Functor[F[+_]] {
  def map[A,B](a: F[A])(f: A => B): F[B]
}

trait Bifunctor[F[+_, +_]] {
  def bimap[A, B, C, D](fa: F[A, B], f: A => C, g: B => D): F[C, D]
}

object Bifunctor {
  implicit def Tuple2Bifunctor = new Bifunctor[Tuple2] {
	def bimap[A, B, C, D](fa: (A, B), f: A => C, g: B => D) =
	  (f(fa._1), g(fa._2))
  }

  implicit def EitherBifunctor = new Bifunctor[Either] {
	def bimap[A, B, C, D](fa: Either[A, B], f: A => C, g: B => D) =
	  fa match {
		case Left(a) => Left(f(a))
		case Right(b) => Right(g(b))
	  }
  }
}
```

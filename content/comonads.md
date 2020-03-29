% Comonads
% Owain Lewis
% 28/04/2020

# Comonads

A comonad is the categorical dual of a monad. In simple terms, it is a monad with the arrows reversed. It is a typeclass with three operations:

- extract (the dual of return)
- duplicate (the dual of join)
- extend (the dual of bind)

In general, comonads are not as useful or widely used as monads but they can be useful in some cases.

It's helpful to compare comonads with monads for better intuition. A monad provides a way of inserting a value in a container using `return`. Once a value is inside the monad, there is no standard interface for extracting the value from its container. Conversely, a comonad gives you a way of extracting a value from its container using `extract` but does not provide a way to insert a value.

The Comonad typeclass is defined as follows

```haskell
class Functor w => Comonad w where
	extract :: w a -> a
	duplicate :: w a -> w (w a)
	extend :: (w a -> b) -> w a -> w b
```

The Scala definitions below are, IMO, easier to understand. We replace bind (or flatMap) with the join opeerator since it's more intuative.

```scala
trait Monad[M[_]] extends Functor[M] {
  def unit[A](a: A): M[A]
  def join[A](mma: M[M[A]]): M[A]
}
```

A comonad is the same as a monad in reverse

```scala
trait Comonad[W[_]] extends Functor[W] {
  def counit[A](w: W[A]): A
  def duplicate[A](wa: W[A]): W[W[A]]
}
```

## Comonad Laws

- Left Identity
- Right Identity
- Associativity

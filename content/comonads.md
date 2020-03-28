% Comonads
% Owain Lewis
% 28/04/2020

# Comonads

A comonad is the categorical dual of a monad. In simple terms, it is a monad with the arrows reversed. It is a typeclass with three operations:

- extract (the dual of return)
- duplicate (the dual of join)
- extend (the dual of bind)

It's helpful to compare comonads with monads for better intuition. The categorical dual of a Monad is a Comonad which is defined as follows

```haskell
class Functor w => Comonad w where
	extract :: w a -> a
	duplicate :: w a -> w (w a)
	extend :: (w a -> b) -> w a -> w b
```

## Comonad Laws

- Left Identity
- Right Identity
- Associativity

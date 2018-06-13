# Chapter 1
---

## 1. [Logic Formulas](#sec1)

## 2. [Semantics of Formulas](#sec2)

## 3. [Models and Logical Consequence](#sec3)

## 4. [Logical Inference](#sec4)

## 5. [Substitutions](#sec5)

---

## <a name='sec1'>Logic Formulas</a>
The notion of declarative sentence has its roots in linguistics. => A declarative sentence is a complete expression of natural language which is `either true or false`.

Followings are some declarative sentences:

> (a) "Every mother loves her children"
> (b) "Mary is a mother and Tom is Mary's child"

Knoing (i) and (ii) it is possible to conclude that:

> (c) "Mary loves Tome"

The first concept considered is that of `logic formulas` which provide a formalized syntax for writing `sentences` like (a)~(c). Such sentences refer to `individuals` in some  `world` and to `relations` between those individuals.



The starting point is an assumption about the alphabet of the language. It must include:

>* symbols for denoting individuals. Such symbols will be called constants
>* symbols for denoting relations. Such symbols are called `predicate symbols`
>  * every predicate symbol has an associated natural number, called arity
>  * the relation named by an n-ary predicate symbol is a n-tuples of individuals



The formal language should also provide the possibility of expressing sentences like (a) which refers to `all` elements of the described `"world"`. Now the sentences (a)~(c) can be formalized accordingly:

> (1) $\forall$X ($\forall$Y (mother(X) $\land$ child_of(Y, X)) $\supset$ loves(X, Y))
> (2) mother(mary) $\land$ child_of(tom, mary)
> (3) loves(mary, tom)
>
> Where:
> 	X, Y are variables
> 	mother, child_of, loves are predicates



From the syntactic point of view logic formulas are finite sequences of symbols such as variables, functors and predicate symbols. There are infinitely many of them and there fore the symbols are usually represented by finite strings of primitive characters.`Thus, the alphabet of the language of predicate logic consists of the follwing classes of symbols:`

> * `variables`: which will be written as alphanumeric identifiers beginning with capital letters.
> * `constants`: which are numerals or alphanumeric identifiers beginning with lowercase letters.
> * `functors`: which are alphanumeric identifiers beginning with lowercase letters and with an associated arity > 0. To emphasize the arity n of a functor f it is sometimes written in the form `f/n`.
> * `predicate symbols`: which are usually alphanumeric identifiers starting with lowercase letters and with an associated arity $\geq$ 0. The notation `p/n` is used also for predicate symbols
> * `logical connectives`: which are $\land$ (conjunction), $\neg$ (negation), $\iff$ (logical equivalence), $\supset$ (implication) and $\lor$ (disjunction)
> * `quantifiers`: $\forall$ (universal) ans $\exist$ (existential)
> * `auxiliary`: symbols like parentheses and commas

[`What is the difference between functors and predicate symbols?`](https://stackoverflow.com/questions/29093366/in-prolog-functors-vs-predicates-and-goals)
e.g.

What is `father(X,Y)` in the following cases (independent from the missing context...)?

```
?- isA(father(X,Y)).
```

`father` is a functor that constructs a binary term

and

```
?- father(X,Y).
```

`father` is a binary predicate.

## <a name='sec2'>Semantics of Formulas</a>

## <a name='sec3'>Models and Logical Consequence</a>
## <a name='sec4'>Logical Inference</a>
## <a name='sec5'>Substitutions</a>

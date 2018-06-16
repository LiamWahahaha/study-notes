# Chapter 1
---

## 1. [Logic Formulas](#sec1)

> * [Definition Terms](#terms)
> * [Definition Formulas](#formulas)

## 2. [Semantics of Formulas](#sec2)

> * [Definition Interpretation](#interpretation)
> * [Definition Semantics of Terms](#sot)
> * [Definition Semantics of $wff$'s](#sowff)

## 3. [Models and Logical Consequence](#sec3)

> * [Definition Model](#model)
> * [Definition Logical Consequence](#consequence)
> * [Proposition Unsatisfiability](#unsatisfiability)
> * [Definition Logical Equivalence](#equivalence)

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

### <a name='terms'>Def. Terms</a>

The set $T$ of $terms$ over a given alphabet $A$ is the smallest set such that:

> * any constant in $A$ is in $T$;
> * any variable in $A$ is in $T$;
> * if $f$/n is a functor in $A$ and $t_1, ..., t_n \in T$ then $f(t_1, ..., t_n) \in T$.

### <a name='formulas'>Def. Formulas</a>

In natural language only certain combinations of words are meaningful sentences. The counterpart of sentences in predicate logic are specialconstructs built from terms. These are called `formulas` or well-formed formulas($wff$). 

Let $T$ be the set of terms over the alphabet $A$. The set $F_s$ of $wff$ (with respect to $A$) is the smallest set such that:

> * if $p$/n is a predicate symbol in $A$ and $t_1, ...,t_n \in T$ then $p(t_1, ..., t_n) \in F_s$;
> * if $F$ and $G \in F_s$ then so are ($\neg F$), ($F \land G$), ($F \lor G$) , ($F \supset G$) and ($F \iff G$);
> * if $F \in F_s$ and $X$ is a variable in $A$ then ($\forall XF$) and ($\exist XF$) $\in F_s$. 

> * Formulas of the form $p(t_1, ..., t_n)$ are called `atomic formulas`(or simply `atoms`);
> * formulas in the form $(F \supset G) \equiv (G \leftarrow F)$.

To avoid ambiguity the formulas will be assumed that the connectives have a binding-order as follows:

> * $\neg, \forall, \exist$
> * $\lor$
> * $\land$
> * $\supset, \leftarrow$
> * $\iff$

e.g. $(a \leftarrow ((\neg b)\land c)) \equiv a\leftarrow \neg b \land c $

Some terminologies

> * Let $F$ be a formula.
>   *  An occurrence of the variable $X$ in $F$ is said to be `bound`
>     *  either if the occurrence follows directly after a quantifier($\forall, \exist$) ;
>     * or if it appears inside the subformula which follows directly after "$\forall X$" or "$\exist X$". 
>   * Otherwise the occurrence is said to be `free`.
> * A formula with no free occurrences of variables is said to be `closed`.
> * A formula/term which contains no variables is called `ground`.
> * Let $X_1, ..., X_n$ be all variables that occur free in a formula $F$.
>   * The closed formula of the form $\forall X_1(...(\forall X_n F))$ is called the `universal closure` of $F$ and is denoted $\forall F$.
>   * Similary, $\exist F$ is called the `existential closure` of $F$ and denotes the formula $F$ closed under existential quantification.

## <a name='sec2'>Semantics of Formulas</a>

The mathematical abstraction of the 'world', called a structure, is a `nonempty set of individuals` (called the `domain`) with a number of `relations` and `functions` defined on this `domain`.

### <a name='interpretation'>Def. Interpretation</a>

An interpretation $I$ of an alphabet $A$ is a nonempty domain $D$ (sometimes denoted $|I|$) and a mapping that associates:

> * each constant $c \in A$ with an element $c_I \in D$
> * each $n-$ary functor $f \in A$ with a function $f_i:D^n \rightarrow D$
> * each $n-$ary predicate symbol $p \in A$ with a relation $p_I  \subseteq\underbrace{D\times\dots\times D}_{n}$

The interpretation of constants, functors and predicate symbols provides a basis for assigning truth values to formulas of the language.

### <a name='sot'>Def. Semantics of terms</a>

A valuation $\varphi$ is a mapping from variables of the alphabet to the domain of an interpretation. Thus it is a function which assigns objects of an interpretation to variables of the language. <u>*By the notation $\varphi[X\mapsto t]$ we denote the valuation which is identical to $\varphi$ except that $\varphi[X\mapsto t]$ maps X to t.*</u>

Let $I$ be an interpretation, $\varphi$ a valuation and $t$ a term. Then the `meaning` $\varphi_I(t)$ of $t$ is an element in $|I|$ defined as follows:

> * if $t$ is a constant $c$ then $\varphi_I(t) := c_I$;
> * if $t$ is a variable $X$ then $\varphi_I(t):=\varphi(X)$;
> * if $t$ is of the form $f(t_1,...,t_n),$ then $\varphi_I(t):=f_I(\varphi_I(t_1), ..., \varphi_I(t_n))$.

### <a name='sowff'>Def. Semantics of $wff$'s</a>

In the following definition the notation <u>*$I\models_{\varphi}Q$ is used as a shorthand for the statement ''$Q$ is true w.r.t. $I$ and $\varphi$" and $I \not\models_{\varphi} Q$ is to be read "$Q$ is false w.r.t. $I$ and $\varphi$".*</u>

Let $I$ be an interpretation, $\varphi$ a valuation and $Q$ a formula. The meaning of $Q$ w.r.t. $I$ and $\varphi$ is defined as follows:

> * $I\models_{\varphi}p(t_1,...,t_n)$ iff $\langle\varphi_I(t_1),...,\varphi_I(t_n) \rangle \in p_I$;
> * $I\models_{\varphi}(\neg F)$ iff $I\not\models_{\varphi}F$;
> * $I\models_{\varphi}(F\land G)$ iff $I\models_{\varphi}F$ and $I\models_{\varphi}G$;
> * $I\models_{\varphi}(F\lor G)$ iff $I\models_{\varphi}F$ or $I\models_{\varphi}G$ or both;
> * $I\models_{\varphi}(F\supset G)$ iff $I\models_{\varphi}G$ whenever $I\models_{\varphi}F$;
> * $I\models_{\varphi}(F\iff G)$ iff $I\models_{\varphi}(F\supset G)$ and $I\models_{\varphi}(G \supset F)$;
> * $I\models_{\varphi}(\forall XF)$ iff $I\models_{\varphi[X\mapsto t]}F$  for every $t \in |I|$;
> * $I\models_{\varphi}(\exist XF)$ iff $I\models_{\varphi[X\mapsto t]}F$  for some $t \in |I|$.

## <a name='sec3'>Models and Logical Consequence</a>

### <a name='model'>Def. Model</a>

An interpretation $I$ is said to be a `model` of *P* iff every formula of *P* is true in $I$.



### <a name='consequence'>Def. Logical consequence</a>

Let *P* be a set of closed formulas. A closed formula *F* is called a logical consequence of *P* (denoted $P\models F$) iff *F* is true in every model of *P*.



### <a name='unsatisfiability'>Prop. Unsatisfiability</a>

Let *P* be a set of closed formulas and *F* a closed formula. Then $P\models F$ iff $P \cup {\neg F}$ is unsatisfiable.



### <a name='equivalence'>Def. Logical equivalence</a>

Two formulas *F* and *G* are said to be logically equivalent (denoted $F \equiv G$) iff *F* and *G* have the same truth value for all interpretations *I* and valuations $\varphi$.

## <a name='sec4'>Logical Inference</a>
## <a name='sec5'>Substitutions</a>

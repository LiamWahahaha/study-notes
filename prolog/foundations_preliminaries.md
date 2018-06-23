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
> * [Definition Logical Equivalences](#equivalence)

## 4. [Logical Inference](#sec4)

> * [Definition Soundness and Completeness](#soundness)

## 5. [Substitutions](#sec5)

> * [Definition Substitutions](#substitutions)
> * [Definition Application](#application)
> * [Definition Composition](#composition)
> * [Definition Idempotent Substitution](#idempotent)
> * [Proposition Properties of Substitutions](#propofsubstitute)

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
> * **A formula with no free occurrences of variables is said to be `closed`.**
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

Given a set of closed formulas *P* and an interpretation *I* is natural to ask whether the formulas of *P* give a proper account of this world. This is the case if all formulas of *P* are true in *I*.

### <a name='model'>Def. Model</a>

An interpretation $I$ is said to be a `model` of *P* iff every formula of *P* is true in $I$.

Clearly *P* has infinitely many interpretations. However, it may happen that none of them is a model of *P*. A trivial example is any *P* that includes the formula ($F \land \neg F$) where *F* is an arbitrary (closed) formula. Such sets of formulas are called *unsatisfiable*.

### <a name='consequence'>Def. Logical consequence</a>

Our intention is to use the description of the world of interest to obtain more information about this world. This new information is to ***represented by new formulas not explicitly included in the original description.***

For a given set *P* of formulas other formulas (say *F*) which are also true in the world described by *P* are searched for. Unfortunately, *P* itself has many models and does not uniquely identify the 'intended model' which was described by *P*. Therefore it must be required that *F* is true in every model of *P* to guarantee that it is also true in the particular world of interest.

Let *P* be a set of closed formulas. A closed formula *F* is called a logical consequence of *P* (denoted $P\models F$) iff *F* is true in every model of *P*.

### **<a name='unsatisfiability'>Prop. Unsatisfiability</a>**

**Let *P* be a set of closed formulas and *F* a closed formula. Then $P\models F$ iff $P \cup {\neg F}$ is unsatisfiable.**

e.g.:

> * $\neg\neg F \equiv F$
>
> * $F \supset G \equiv \neg F \lor G$
>
> * $F \supset G \equiv \neg G \supset \neg F$
>
> * $F \iff G \equiv (F\supset G) \land (G\supset F)$
>
> * $\neg (F \land G) \equiv \neg F \lor \neg G$     DeMorgan's law
>
> * $\neg(F \lor G) \equiv \neg F \land G$        DeMorgan's law
>
> * $\neg\forall XH(X) \equiv \exist X \neg H(X)$ DeMorgan's law
>
> * $\neg \exist XH(X) \equiv \forall X \neg H(X)$ DeMorgan's law
>
>   

### <a name='equivalence'>Def. Logical equivalence</a>

Two formulas *F* and *G* are said to be logically equivalent (denoted $F \equiv G$) iff *F* and *G* have the same truth value for all interpretations *I* and valuations $\varphi$.

e.g.:

> - $\neg\neg F \equiv F$
> - $F\supset G \equiv \neg F \lor G$
> - $F \supset G \equiv \neg G \supset \neg F$
> - $F \iff G \equiv (F \supset G) \land (G \supset F)$
> - $\neg (F \lor G) \equiv \neg F \land \neg G$        DeMorgan's law
> - $\neg(F \land G) \equiv \neg F \lor \neg G$        DeMorgan's law
> - $\neg \forall XH(X) \equiv \exist  X \neg H(X)$   DeMorgan's law
> -  $\neg \exist XH(X) \equiv \forall X \neg H(X)$  DeMorgan's law
> - if there are no free occurrence of *X* in  *F* then:
>   - $\forall X(F \lor H(X)) \equiv F \lor \forall XH(X)$

## <a name='sec4'>Logical Inference</a>

> * Premises
>
>   (1) $\forall$X ($\forall$Y (mother(X) $\land$ child_of(Y, X)) $\supset$ loves(X, Y)) 
>
>   (2) mother(mary) $\land$ child_of(tom, mary)
>
> * Conclusion
>
>   (3) loves(mary, tom)

With this formalization, reasoning can be seen as a process of manipulation of formulas, which from a given set of formulas, like (1) and (2), called the *premises*, produces a new formula called the *conclusion*, for instance (3).

An inference rule satisfying the following requirement is said to be `sound`: whenever the premises are true in any world under consideration, any conclusion obtained by application of an inference rule should also be true in this world.

Among well-known inference rules of predicate logic the following are frequently used:

* **Modus ponens or elimination rule for implication**

  This rule says that whenever formulas of the form *F* and ($F\supset G$) belong to or are concluded from a set of premises, *G* can be inferred. This rule is often presented as follows:

  ##                            $\frac{F F\supset G}{G} (\supset E)$

* **Elimination rule for universal quantifier**

  This rule says that whenever a formula of the form ($\forall XF$) belongs to or is concluded from the premises a new formula can be concluded by replacing all free occurrences of *X* in *F* by some term *t* which is *free* for *X* (that is, all variables in *t* remain free when *X* is replaced by *t*). This rule is often presented as follows:

  ###                           $\frac{\forall XF(X)}{F(t)} (\forall E)$

* **Introduction rule for conjunction**

  This rule states that if formulas *F* and *G* belong to or are concluded form the premises then the conclusion $F\land G$ can be inferred. This is often stated as follows:

  ##                               $\frac{F G}{F\land G} (\land I)$ 

e.g.

> (a) $\forall$X ($\forall$Y (mother(X) $\land$ child_of(Y, X)) $\supset$ loves(X, Y)) 
>
> (b) mother(mary) $\land$ child_of(tom, mary)
>
> 
>
> => Elimination rule for universal quantifier in (a) yields:
>
> (c) $\forall Y (mother(mary)) \land child\_of(Y, mary) \supset loves(mary, Y)$
>
> 
>
> => Elimination rule of the universal quantifier in (c) yields:
>
> (d) $mother(mary) \land child\_of(tom, mary) \supset loves(mary, tom)$
>
> 
>
> => Modus ponens applied to (b) and (d) yields:
>
> (e) $loves(mary, tom)$

Thus the conclusion (e) has been produced in a formal way by application of the inference rules.

Any formula *F* that can be obtained in that way from a given set *P* of premises is said to be `derivable` from *P*. **This is denoted by $P \vdash F$**.

### <a name='soundness'>Def. Soundness and Completeness</a>

A set of inference rules are said to be `sound` if, for every set of closed formulas *P* and every closed formula *F*, whenever $P \vdash F$ it holds that $P \models F$. The inference rules are `complete` if $P \vdash F$ whenever $P\models F$.

## <a name='sec5'>Substitutions</a>

Formally a substitution is a mapping from variables of a given alphabet to terms in this alphabet.

### <a name='substitutions'>Def. Substitutions</a>

A *substituion* is a finite set of pairs of terms {$X_1/t_1, ..., X_n/t_n$} where each $t_i$ is a term and each $X_i$ a variable such that $X_i \not = t_i$ and $X_i \not = X_j$ if $i \not = j$. The *empty substitution* is denoted $\epsilon$.

###  <a name='application'>Def. Application</a>

Let $\theta$ be a substitution  {$X_1/t_1, ..., X_n/t_n$} and $E$ a term or a formula. The application $E\theta$ of $\theta$ to $E$ is the term/formula obtained by simultaneously replacing $t_i$ for every free occurence of $X_i$ in X ($1\leq i \leq n$). $E\theta$ is called an *instance* of *E*.

The *application* $X\theta$ of a substitution $\theta$ to a variable $X$ is defined as follows:

​		 $X\theta := $

​			if $X/t \in \theta$:

​                                  $X \theta := t $

 			otherwise:

​				 $X \theta := X$

in what follows let $Dom(\{ X_1/t_1, ..., X_n/t_n\})$ denote the set $\{X_1, ..., X_n\}$. Also let $Range(\{X_1/t_1, ..., X_n/t_n\})$ be the set of all variables in $t_1,..., t_n$. Thus, for variables not included in $Dom(\theta)$, $\theta$ behaves as the identity mapping. It is natural to extend the domain of substitutions to include also terms and formulas.

e.g. $p(f(X,Z), f(Y,a))\{X/a, Y/z, W/b\} = p(f(a,Z), f(Z,a))$

e.g. $p(X,Y){X/f(Y), Y/b}=p(f(Y), b)$

### <a name='composition'>Def. Composition</a>

Let $\theta$ and $\sigma$ be two substitutions:

​                                     $\theta := \{ X_1/s_1, ..., X_m/s_m\}$

​                                     $\sigma :=\{Y_1/t_1, ..., Y_n/t_n\}$

The *composition* $\theta\sigma$ of $\theta$ and $\sigma$ is obtained from the set:

​                                    $\{X_1/s1\sigma, ...,X_m/s_m\sigma, Y_1/t_1, ..., Y_n/t_n\}$

by removing all $X_i/s_i\sigma$ for which $X_i=s_i\sigma(1\leq i \leq m)$ and by removing those $Y_j/t_j$ for which $Y_j \in \{X_1, ..., X_m\} (1\leq j \leq n)$.

### <a name='idempotent'>Def. Idenpotent Substitution</a>

A substitution $\theta$ is said to be *idempotent* iff $\theta=\theta\theta$

It can be shown that a substitution $\theta$ is 

​                        $idemptoent\iff Dom(\theta) \cap Range(\theta)=\phi$.

### <a name='propofsubstitute'>Prop. Properties of Substitutions</a>

Let $\theta, \sigma$ and $\gamma$ be substitutions and let *E* be a term or a formula. Then:

* $E(\theta\sigma)=(E\theta)\sigma$
* $(\theta\sigma)\gamma=\theta(\sigma\gamma)$
* $\epsilon\theta=\theta\epsilon=\theta$

<u>**Notice that composition of substitutions is not commutative.**</u>
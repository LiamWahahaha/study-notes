# Chapter 3

------

## 1. [Informal Introduction](#sec1)

## 2. [Unification](#sec2)

> - [Definition Unifier](#unifier)
> - [Definition Generality of Substitutions](#gos)
> - [Definition Most General Unifier](#mgu)
> - [Definition Solved Form](#sf)
> - [Proposition](#prop)
> - [Definition Equivaluence of Sets of Equations](#eosoe)
> - [Theorem](#theo)
> - [Definition Renaming](#renaming)
> - [Proposition](#prop1)
> - [Proposition](#prop2)

## 3. [SLD-Resolution](#sec3)

> - [Definition Herbrand Universe, Herbrand Base](#huhb)
> - [Definition Herbrand Interpretations](#hi)
> - [Definition Herbrand Model](#hm)
> - [Theorem](#theorem1)
> - [Theorem Model Intersection Property](#theorem2)
> - [Theorem](#theorem3)

## 4. [Soundness of SLD-Resolution](#sec4)

> - [Definition Immediate Consequence Operator](#ico)
> - [Theorem]

## 5. [Completeness of SLD-Resolution](#sec5)

## 6. [Proof Trees](#sec6)

**The `SLD-resolution` principle makes it possible to draw correct conclusions from the program, thus providing a foundation for a logically sound `operational semantics` of definite programs.**

## <a name='sec1'>Informal Introduction</a>

The sentences of logic programs have a general structure of logical implication:

​				       $A_0 \leftarrow A_1, ..., A_n (n \geq 0)$

where $A_0, ..., A_n$ are atomic formulas and where $A_0$ may be absent (in which case it is a goal clause).

Consider the following definite program:

> $proud(X)\leftarrow parent(X, Y), newborn(Y)$.
>
> $parent(X, Y)\leftarrow father(X, Y)$.
>
> $parent(X, Y) \leftarrow mother(X, Y)$.
>
> $father(adam,mary)$.
>
> $newborn(mary)$.

that describes a world where:

> "parents of newborn children are proud"
>
> "Adam is the father of Mary"
>
> "Mary is newborn"

Say now that we want to ask the question "Who is proud?". The question concerns the world described by the program $P$, that is, the intended model of $P$.

Since predicate logic does not provide the means for expressing this type of `interrogative` sentences; only `declarative` ones. **Therefore the question may be formalized as the goal clause:**

​						    $\leftarrow proud(Z)$ 							 $(G_0)$

which is an abbreviation for $\forall Z \neg proud(Z)$ which in turn is equivalent to:

  					           $\neg \exist Z proud(Z)$

whose reading is "Nobody is proud". That is a negative answer to the query above. **The aim now is to show that this answer is a false statement in every model of $P$ (and in particular in the intended model).** Then it can be concluded that $P\models \exist Z proud(Z)$. Thus, the objective is rather to find a substitution $\theta$ such that the set $P \cup \{\neg proud(Z)\theta\}$ is unsatisfiable, or equivalently such that $P\models proud(Z)\theta$.

The starting point of reasoning is the assumption - "For any Z, Z is not proud." Inspection of the program reveals a rule describing one condition for someone to be proud:

​	    	              $proud(X)\leftarrow parent(X,Y), newborn(Y)$

Its equivalent logical reading is:

​	 	    $\forall (\neg proud(X)\supset \neg(parent(X,Y)\and newborn(Y)))$

Renaming X into Z, elimination of universal quantification and the use of `modus ponens` w.r.t. $G_0$ yields:

​      $\neg (parent(Z, Y) \and newborn(Y)) \equiv \leftarrow parent(Z, Y), newborn(Y)$       $(G_1)$

...

![refutation](/Users/liam/CodeForever/LiamWahahaha/study-notes/prolog/refutation.png)

In the example discussed, the goal 'Nobody is proud' is unsatisfiable with $P$ since its instance 'Adam is not proud' is unsatisfiable with $P$. In other words - in every model of $P$ of the sentence 'Adam is proud' is true.

## <a name='sec2'>Unification</a>

`Unification` is a process of making two atomic formulas syntactically equivalent. This procedure takes two atomic formulas as input, and either shows how they can be instantiated to identical atoms or, reports a failure.

### <a name='unifier'>Def. Unifier</a>

Let $s$ and $t$ be terms. A substitution $\theta$ such that $s\theta$ and $t\theta$ are identical (denoted $s\theta=t\theta$) is called a `unifier` of s and t.

### <a name='gos'>Def. Generality of substitutions</a>

A substitution $\theta$ is said to be `more general` than a substitution $\sigma$ (denoted $\sigma \preceq \theta$) iff there exists a substitution $\omega$ such that $\sigma = \theta\omega$

### <a name='mgu'>Def. Most General Unifier</a>

A unifier $\theta$ is said to be a most general unifier (mgu) of two terms iff $\theta$ is more general than any other unifier of the terms.

### <a name='sf'>Def. Solved Form</a>

A set of equations $\{X_1\doteq t_1,...X_n\doteq t_n\}$ is said to be in `solved form` iff $X_1,...,X_n$ are distinct variables none of which appear in $t_1,...,t_n$.

### <a name='prop'>Prop.</a>

Let $\{X_1\doteq t_1,...,X_n\doteq t_n\}$ be a set of equations in solved form. Then $\{X1/t_1,...,X_n/t_n\}$ is an (idempotent) mgu of the solved form.

> *Proof*:
>
> ​	First define:
>
> ​				    $\varepsilon := \{X_1\doteq t_1,...X_n\doteq t_n\}$
>
> ​				    $\theta := \{X_1/t_1, ..., X_n/t_n\}$
>
> ​	Clearly $\theta$ is an idempotent unifier of $\varepsilon$. 
>
> ​	Now, assume that $\sigma$ is a unifier of $\varepsilon$. Then $X_i\sigma = t_i \sigma$ for $1\leq i\leq n$. It
> 	must follow that $X_i/t_i\sigma \in \sigma$ for $1\leq i \leq n$. In addition $\sigma$ may 
>         contain some additional pairs $Y_1/s_1,...,Y_m/s_m$ such that 
>         $\{X_1,...,X_n\}\cap \{Y_1,...,Y_m\} = \phi$. Thus, $\sigma$ is of the form:
>
> ​			    $\{X_1/t_1\sigma, ..., X_n/t_n\sigma, Y_1/s_1, ..., Y_m/s_m\}$
> 	Now, $\theta \sigma = \sigma$. Thus, there exists a substitution $\omega$ (viz. $\sigma$) such that 
>         $\sigma = \theta\omega$. Therefore, $\theta$ is an idempotent mgu.

### <a name='eosoe'>Def. Equivalence of Sets of Equations</a>

Two sets of equations $\varepsilon_1$ and $\varepsilon_2$ are said to be `equivalent` if they have the same set of unifiers.

[TODO]

### <a name='theo'>Theo.</a>

The solved form algorithm terminates and returns an equivalent solved form or **failure** if no such solved form exists.

### <a name='renaming'>Def. Renaming</a>

A substitution$\{X_1/Y_1,...,X_n/Y_n\} $ is called a `renaming substitution` iff $Y_1,...,Y_n$ is a  permutation of $X_1,...,X_n$.

### <a name='prop1'>Prop.</a>

Let $\theta$ be an mgu of $s$ and $t$ and assume that $\omega$ is a renaming. Then $\theta\omega$ is an mgu of $s$ and $t$.

### <a name='prop2'>Prop.</a>

Let $\theta$ and $\sigma$ be substitutions. If $\theta\preceq\sigma$ and $\sigma\preceq\theta$ then there exists a renaming substitution $\omega$ such that $\sigma=\theta\omega$ (and $\theta=\sigma\omega^{-1}$).
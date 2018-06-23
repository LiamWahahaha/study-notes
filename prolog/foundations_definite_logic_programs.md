# Chapter 2

------

## 1. [Definite Clauses](#sec1)

## 2. [Definite Programs and Goals](#sec2)

> - [Definition Clause](#clause)
> - [Definition Definite Programs](#definiteprog)

## 3. [The Least Herbrand Model](#sec3)

> - [Definition Herbrand Universe, Herbrand Base](#huhb)
> - [Definition Herbrand Interpretations](#hi)
> - [Definition Herbrand Model](#hm)
> - [Theorem](#theorem1)
> - [Theorem Mpdel Intersection Property](#theorem2)
> - [Theorem](#theorem3)

## 4. [Construction of Least Herbrand Models](#sec4)

> - [Theorem](#theorem4)

---

## <a name='sec1'>Definite Clauses</a>

There is a special type of *declarative* sentences of natural language that describe positive *facts* and *rules*. A sentence of this type either states that ***a relation holds between individuals*** *<u>(in case of a fact)</u>*, or that a relation holds between individuals ***provided*** that some other relations hold (in case of a rule). For example, consider the sentences:

> (a) Tom is John's child
>
> (b) Ann is Tom's child
>
> (c) John is Mark's child
>
> (d) Alice is John's child
>
> (e) The grandchild of a person is a child of a child of this person

These sentences may be formalized in two steps.

* First atomic formulas describing fact are introduced:

  * (1) child(tom, john)
  * (2) child(ann, tom)
  * (3) child(john, mark)
  * (4) child(alice, john)

  Applying this notation to the final sentence yields:

  * (5) For all X and Y, grandchild(X, Y) if there exists a Z such that child(X, Z) and child (Z, Y)

  This can be further formalized using quantifiers and the logical connectives '$\supset$' and '$\land$', but to preserve the natural order of expression the implication is reversed and written '$\leftarrow$':

  * (6) $\forall X \forall Y (grandchild(X, Y)\leftarrow \exist (child(X,Z) \land child(Z, Y))) $

  This formula can be transformed into the following equivalent forms:

  >$\forall X\forall Y (grandchild(X, Y) \lor \neg \exist Z(child(X,Z)\land child(Z, Y)))$
  >
  >$\forall X\forall Y (grandchild(X, Y) \lor\forall Z\neg(child(X,Z)\land child(Z, Y)))$
  >
  >$\forall X\forall Y\forall Z(grandchild(X,Y)\lor\neg(child(X,Z)\land child(Z,Y)))$
  >
  >$\forall X\forall Y\forall Z (grandchild(X,Y)\leftarrow (child(X,Z)\land child(Z, Y)))$

* It consists of formulas of the form:

  * $A_0\leftarrow A_1\and ... \and A_n$ (where $n\geq 0$) 
  * or equivalently, $A_0 \or \neg A_1 \or ... \or \neg A_n$

  where $A_0, ..., A_n$ are atomic formulas and all variables occurring in a formula are (implicitly) universally quantified over the whole formula. The formulas of the form are called ***definite clauses*.**

  > * Facts, sometimes be called unit-clauses, are definite clauses where $n=0$.
  > * $A_0$ is called the *head* of the clause
  > * $A_1\and ...\and A_n$ is called the *body*

## <a name='sec2'>Definite Programs and Goals</a>

### <a name='clause'>Def. Clause</a>

A *clause* is a formula $\forall(L_1\or ...\or L_n)$ where each $L_i$ is ***an atomic formula*** (a positive literal) or ***the negation of an atomic formula*** (a negative literal).

> A *definite clause* is a clause that contains exactly one positive literal. That is, a formula of the form:
>
> ​				          $\forall (A_0 \or \neg A_1 \or ... \or \neg A_n)$
>
> The notational convention is to write such a definite clause thus:
>
> ​					   $A_0 \leftarrow A_1,...A_n (n\geq 0)$
>
> If the *body* is empty the implication arrow is usually omitted.

### <a name='definiteprog'>Def. Definite Programs</a>

A *definite program* is a finite set of definite clauses.

> What is logic programming?
>
> * The programmer attempts to describe the ***intended model*** by means of declarative sentences
>   * These sentences are definite clauses: facts and rules.
> * The program is a set of logic formulas and ***it may have many models, including the intended model***
>   * The ***concept of intended model*** makes it possible to discuss correctness of logic programs: a program *P* is incorrect iff the intended model is not a model of *P*
> * 
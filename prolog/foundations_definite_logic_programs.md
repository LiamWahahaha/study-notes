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
> - [Theorem Model Intersection Property](#theorem2)
> - [Theorem](#theorem3)

## 4. [Construction of Least Herbrand Models](#sec4)

> - [Definition Immediate Consequence Operator](#ico)
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
> * The program is ***a set of logic formulas*** and ***it may have many models, including the intended model***
>   * The ***concept of intended model*** makes it possible to discuss correctness of logic programs: a program *P* is incorrect iff the intended model is not a model of *P*

e.g.

| QUERY                        | GOAL                            | RESULT   |
| :--------------------------- | ------------------------------- | -------- |
| Is Ann a child of Tome?      | $\leftarrow child (ann, tom)$   | yes      |
| Who is a grandchild of Ann?  | $\leftarrow grandchild(X, ann)$ | no one   |
| Whose grandchild is Tome?    | $\leftarrow grandchild(tom, X)$ | X = mark |
| Who is a grandchild of whom? | $grandchild (X,Y)$              | Table 2  |

Table 2



* |   X   |  Y   |
  | :---: | :--: |
  |  tom  | mark |
  | alice | mark |
  |  ann  | john |

  It is also possible to ask more complicated queries, for example 'is there a person whose grandchildren are Tom and Alice?', expressed formally as:

  $\leftarrow grandchild(tom, X), grandchild(alice, X)$

  Whose (expected) answer is X = *mark.*

##  <a name='sec3'>The Least Herbrand Model</a>

Every definite program has a well defined *least* model. Intuitively ***this model reflects all information expressed by the program and nothing more.***

### <a name='huhb'>Def. Herbrand Univers, Herbrand Base</a>

Let *A* be an alphabet containing at least one constant symbol. The set $U_A$ of all ground terms constructed from functors and constants in *A* is called the `Herbrand universe` of *A*. The set $B_A$ of all ground, atomic formulas over *A* is called the `Herbrand base` of *A*.

The Herbrand universe and Herbrand base are often defined for a given `program`. In this case it is assumed that:

* The alphabet of the program consists of exactly those symbols which appear in the program
* The program contains at least one constant

e.g. Consider the following definite program *P*:

> $odd(s(0))$.
>
> $odd(s(s(X)))\leftarrow odd(X)$.

The program contains one constant (0) and one unary functor (s). Consequently the corresponding Herbrand universe and Herbrand base look as follows:

> $U_P = \{0, s(0), s(s(0)), s(s(s(0))),...\}$
>
> $B_P = \{odd(0), odd(s(0)), odd(s(s(0))),...\}$

e.g. Consider the following definite program *P*:

> $owns(owner(corvette), corvette)$.
>
> $happy(X)\leftarrow owns(X, corvette)$.

In this case the Herbrand universe and Herbrand base look as follows:

> $U_P=\{corvette, owner(corvette), owner(owner(corvette)),...\}$
>
> $B_P=\{owns(s,t) | s,t \in U_P\}\cup \{happy(s)|s\in U_P\}$

### <a name='hi'>Def. Herbrand Interpretations</a>

A Herbrand interpretation of *P* is an interpretation *I* such that:

* the domain of *I* is $U_P$

* for every constant $c$, $c_I$ is defined to be $c$ itself

* for every $n$-ary functor $f$ the function $f_I$ is defined as follows

  $f_I(x_1, ..., x_n) := f(x_1, ..., x_n)$

  That is, the function $f_I$ applied to $n$ ground terms composes them into the ground term with the principal functor $f$

* for every $n$-ary predicate symbol $p$ the relation $p_I$ is a subset of $U_P^n$ (the set of all $n$-tuples of ground terms)

  For an $n$-ary predicate symbol $p$ and a Herbrand interpretation $I$ the meaning $p_I$ of $p$ consists of the following set of $n$-tuples:$\{ <t_1, ..., t_n>\in U_P^n|I\models p(t_1,..., t_n)\}$

e.g. Consider the fp;;pwomg definite program $P$:

> $odd(s(0))$.
>
> $odd(s(s(X)))\leftarrow odd(X)$.

One possible interpretation of the program $P$ is $odd_I=\{<s(0)>, <s(s(s(0)))>\}$.

A Herbrand interpretation can be specified by giving a family of such relations (one for every predicate symbol).

Here are some alternative Herbrand interpretations for the program $P$:

> $I_1 := \phi$
>
> $I_2:= \{odd(s(0))\}$
>
> $I_3:=\{odd(s(0)), odd(s(s(0)))\}$
>
> $I_4:= {odd(s^n(0))|n\in \{1,3,5,7,...\}}=\{odd(s(0)), odd(s(s(s(0))))\}$
>
> $I_5:=B_P$

### <a name='hm'>Def. Herbrand Model</a>

A Herbrand model of a set of (closed) formulas is a Herbrand interpretation which is a model of every formula in the set.

Further discussion:

> * $I_1$ is cannot be a model of $P$ as it is not a Herbrand model of $odd(s(0))$.
> * $I_2, I_3, I_4, I_5$ are all models of $odd(s(0))$ since $odd(s(0))\in I_i (2\leq i\leq 5)$.
> * $I_2$ is not a model of $odd(s(s(X)))\leftarrow odd(X)$ since there is a ground instance of the rule - namely $odd(s(s(s(0))))\leftarrow odd(s(0))$ -  such that all premises are true: $odd(s(0)) \in I_2$, but $odd(s(s(s(0))))\not\in I_2$.
> * $I_3$ is not a model of the rule for the similar reason.
> * $I_4$ and $I_5$ are a model of the rule.

### <a name='theorem1'>Theorem</a>

Let $P$ be a definite program and $G$ a definite goal. If $I'$ is a model of $P\cup \{G\}$ then $I:= \{A\in B_P | I'\models A\}$ is a Herbrand model of $P\cup \{G\}$.

*Proof:*

$I$ is a Herbrand interpretation. Now assume that $I'$ is a model and that $I$ is not a model of $P \cup \{G\}$. In other words, there exists a ground instance of a clause or a goal in $P \cup \{G\}$: $A_0\leftarrow A_1, ..., A_m (m\geq 0)$ which is not true in $I$.

Since this clause is false in $I$ then $A_1, ...,A_m$ are all true and $A_0$ is false in $I$. Hence, by the definition of $I$ we conclude that $A_1, ..., A_m$ are true and $A_0$ is false in $I'$. This contradicts the assumption that $I'$ is a model. Hence $I$ is a model of $P \cup \{G\}$.

**In the general case, nonexistence of a Hergrand model of a set of formulas $P$ does not mean that $P$ is unsatisfiable. That is, there are sets of formulas $P$ which do not have a Herbrand model but which have other models.**

e.g. Consider the formulas $\{\neg p(a), \exist Xp(X)\}$ where $U_P:=\{a\}$ and $B_P:= \{p(a)\}$.

> Sol:
>
> There are only two Herbrand interpretations - 
>
> * The empty set
>
>   This is not a not a model of the second formula
>
> * $B_P$
>
>   This is a model of the second formula but not of the first
>
> However, if we do the following:
>
> * let the domain be the natural numbers
> * assign 0 to the constant $a$
> * assign the relation $\{<1>, <3>,<5>,...\}$ to the predicate symbol $p$.
>
> Clearly, this is a model since '0 is not odd' and 'there exists a natural number which is odd'

### <a name='theorem2'>Theorem Model Intersection Property</a>

Let $M$ be a non-empty family of Herbrand models of a definite program $P$. Then the intersection $I:=\cap M$ is a Herbrand model of $P$.

*Proof:*

Assume that $I$ is not a model of $P$. 

Then there exists a ground instance of a clause of $P$: 

> $A_0\leftarrow A_1, ..., A_m(m\geq 0)$ which is not true in $I$. 
>
> This implies that $I$ contains $A_1, ..., A_m$ but not $A_0$.

Then $A_1, ..., A_m$ are elements of every interpretation of the family $M$.

Moreover, there must be at least one model $I_i \in M$ such that $A_0 \not\in I_i$.

Thus $A_0\leftarrow A_1, ...,A_m$ is not true in this $I_i$.

Hence $I_i$ is not a model of the program, which contradicts the assumption.

This concludes the proof that the intersection of any set of Herbrand models of a program is also a Herbrand model.

### <a name='theorem3'>Theorem</a>

The least Herbrand model $M_P$ of a definite program $P$ is the set of all ground atomic logical consequences of the program. That is, $M_P= \{A \in B_P | P\models A\}$

*Proof:*

Show first $M_P \supseteq \{A\in B_P | P\models A\}$: 

> Every ground atom $A$ which is a logical consequence of $P$ is an element of $M_P$. On the other hand, the definition of Herbrand interpretation states that $A$ is true in $M_P$ iff $A$ is an element of $M_P$.

Then show that $M_P \subseteq \{A\in B_P | P\models A\}$:

> Assume that $A$ is in $M_P$. Hence it is true in every Herbrand model of $P$.
>
> Assume that $A$ is not true in some non-Herbrand model $I'$ of $P$. 
>
> But we know that the set $I$ of all ground atomic formulas which are true in $I'$ is a Herbrand model of $P$.
>
> Hence $A$ cannot be an element of $I$. This contradicts the assumption that there exists a model of $P$ where $A$ is false.
>
> Hence $A$ is true in every model of $P$, that is $P\models A$, which concludes the proof.

### <a name='sec4'>Construction of Least Herbrand Models</a>

<a name='ico'>Def. Immediate Consequence Operator</a

Let $ground(P)$ be the set of all ground instances of claused in $P$. $T_P$ is a function on Herbrand interpretations of $P$ defined as follows:

| $T_P(I):=\{A_0|A_0\leftarrow A_1,...A_m \in ground(P)\land \{A_1, ..., A_,\}\subseteq I\}$ |
| :----------------------------------------------------------: |

For definite programs it can be shown that there exists a least interpretation $I$ such that $T_P(I) = I$ and that $I$ is identical with the least Herbrand model $M_P$. Moreover, $M_P$ is the limit of the increasing, possibly infinite sequence of iterations:

| $\phi, T_P(\phi), T_P(T_P(\phi)),T_P(T_P(T_P(\phi))),...$ |
| :-------------------------------------------------------: |

There is a standard notation used to denote elements of the sequence of interpretations constructed for $P$. Namely:

|               $T_P \uparrow 0 := \phi$               |
| :--------------------------------------------------: |
|      $T_P \uparrow (i+1) := T_P(T_P\uparrow i)$      |
| $T_P\uparrow \omega:=\cup_{i=0}^{\inf}T_P\uparrow i$ |

### <a name='theorem4'>Theorem</a>

Let $P$ be a definite program and $M_P$ its least Herbrand model. Then:

* $M_P$ is the least Herbrand interpretation such that $T_P(M_P)=M_P$
* $M_P=T_P\uparrow \omega$






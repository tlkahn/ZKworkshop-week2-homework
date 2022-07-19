- [Week2 Assignments](#week2-assignments)
  - [Assignment Selection](#assignment-selection)
  - [Assignment 1. Polynomial Solving and Proving](#assignment-1-polynomial-solving-and-proving)
    - [Q1](#q1)
    - [Q2](#q2)
    - [Q3](#q3)
    - [Q4](#q4)
  - [Assignment 2. Classical Protocol Analysis](#assignment-2-classical-protocol-analysis)
    - [Q1](#q1-1)
    - [Q2](#q2-1)
  - [Assignment 3. Classical Protocol Engineering Practice](#assignment-3-classical-protocol-engineering-practice)
  - [Deadline](#deadline)
  - [Assignment Workflow](#assignment-workflow)
  - [Assignment Requirements](#assignment-requirements)
    - [File format](#file-format)
    - [Assignment content](#assignment-content)
  - [Scoring Rules](#scoring-rules)

# Week2 Assignments

## Assignment Selection

We offer 3 assignments, so you can choose one or more depending on your situation.

| Assignment                              | Description                                                  | Category             |
| --------------------------------------- | ------------------------------------------------------------ | -------------------- |
| Polynomial Solving and Proving          | Solving polynomials and proving polynomials in Groth16 and Plonk forms, respectively | Theory               |
| Classical Protocol Analysis             | Any one of Groth16, Plonk or Stark protocols to analyze the use of common reference strings for computation and implementation of zero-knowledge features, etc. | Theory               |
| Classical Protocol Engineering Practice | Implement a simple verifiable computation with any of the Groth16, Plonk or Stark protocols | Engineering Practice |

> Bonus points for completing multiple assignments !!!

Define the following function with 3 variables a, b, c.

```python
def f(a, b, c):
  if a == 1:
    return b*c
  return 2b - c
}
```

## Assignment 1. Polynomial Solving and Proving

Polynomial solving and polynomial proving are very important parts of zkSNARKs, while Groth16 and Plonk representations of circuit constraints differently, completing the following polynomial-related problem solving and deduction.

> Tips: Refer to  [Why and How zk-SNARK Works: Definitive Explanation](https://arxiv.org/pdf/1906.07221) for help.

### Q1

To convert the function to circuit of R1CS form (flatten), use polynomial interpolation with values(1,2,3,...) to solve variable polynominals for each variables (including intermediate variables).


### Q2
Continuing with Q1, solve for the left operand polynomial L(X), the right operand polynomial R(X), the output operand polynomial O(X), and the target polynomial T(X) = (x-1)(x-2)(x-3)... (interpolation of Q1 solution process), after assigning values to the variables (x=1, y=2, z=5)... , verify if L(X)*R(X) - O(X) is divisible by T(X) and why?

> Note: The polynomial solution problems involved in Q1, Q2 are the very core of Groth16, Pinocchio


### Q3
Convert the function into a system of circuit constrained equations (addition, multiplication, input, output, etc.), then convert these circuit constraints into a system of circuit constrained equations of the form defined by Plonk as "(qL) - a + (qR) - b + (qO) - c + (qM) - (a * b) + (qC) = 0", and finally perform a polynomial interpolation (1,2,3,...) Solve for: qL(x), qR(x), ... , qM(x)

### Q4
Continuing with Q3, assign the variables (x=1, y=2, z=5) and then interpolate (1,2,3,...) Solve for: a(x), b(x), c(x), then verify if qL(x) - a(x) + qR(x) - b(x) + qO(x) - c(x) + qM(x) - (a(x) * b(x)) + qC(x) can be obtained by the target polynomial T(x) = (x-1)(x-2)(x-3)...

> Note: The polynomial solution problems involved in Q3, Q4 are fundamentals of Plonk.

## Assignment 2. Classical Protocol Analysis

Choose any one protocol from Groth16, Plonk, Stark and complete the following questions.

### Q1

1. Please describe the main features and workflow of the protocol
2. If the protocol produces public parameters in if there is a trust-setup step, point out which circuit-independent public parameters they provide and which circuit-related parameters? How are these public parameters produced, briefly describe the implementation idea, and are there security issues in the application process?
3. If the protocol does not have a trust-setup step, please explain the basic principles of proof and verification for implementing no public parameters, and further analyze the protocol


### Q2

How does the protocol achieve zero-knowledge in the computation process (proof, verification)? Please analyze the implementation idea and construction method to achieve zero-knowledge, and analyze whether it satisfies perfect zero-knowledge.



## Assignment 3. Classical Protocol Engineering Practice

The following function is known, with 3 variables x, y, z.
```python
def f(x, y, z):
  if x == 1:
    return y*z
  return 2y - z
}
```

prover owns private variables x, y, z with values (x = 1, y = 2, z = 5), please choose one open source libraries or toolkits of Groth16, Plonk, Stark protocol, and use one of the protocols to complete the verifiable computation of function `f(x,y,z)` as above.

Engineering Assignment Requirements:
1. please briefly describe the use of the protocol code base or framework
2. please explain the implementation idea in steps
3. if there is an output of the calculation step, please give a screenshot of the result
4. please provide the project practice repository, specify the commit hash


## Deadline

2022.07.21

----
## Assignment Workflow

The assignment workflow is as follows:
1. Follow the assignment requirements to complete the assignment and output the assignment PDF
2. Send the assignment to the course administrator via Discord private message (before the assignment submission deadline)
3. Get the assignment approval result via email or Discord (before the next class starts)

----
## Assignment Requirements

### File format

The output format of the assignment is PDF, the file naming format is: {user registration name}-{assignment name}-yymmdd.pdf, for example: Alice-zkGame-20220714.pdf

### Assignment content

- Basic Information

| Item | Description | Example |
| --------------- | ---------------------------------------- | ------------------------------------------------------ |
| Name | registered name of the course | Name: `Alice` |
| Discord Account | registered Discord account of the course | DiscordAccount: `Alice#1234` |
| Study Group | which study group you joined | StudyGroup: `team1` |
| Assignment | the assignment name | Assignment: `assignment of week2` |
| GitHub Rep | repository of your GitHub account | Repository: `https://github.com/GitHubOfAlice/example` |


- Answers to Assignment Questions


> Please do not copy the assignment (it will result in a zero score), and if you use open source code or resources, please cite them.




-----
## Scoring Rules

Comprehensive evaluation according to the scoring points to encourage innovation and optimization.

Scoring points:

- Correctness

  The calculation process is rigorous and the results are correct

- Completeness
  Documented instructions for use, complete operationalization

- Completeness
  Excellent documentation, beautiful interface, user-friendly

- Interface friendly
  Simple and easy to use interface

- Practicality
  Good practicality, can be applied to related fields

- Innovation
  Originality, novelty, security or performance improvement

- Theoretical depth
  Comprehensive and integrated analysis, in-depth exploration
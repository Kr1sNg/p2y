# 1. Introduction

## What is an algorithm?

An *algorithm* is a method for solving some computational problem. An algorithm implemented in some programming language can be executed on a computer.

The *input* of an algorithm is the initial data provided to the algorithm. The *output* of an algorithm is the answer produced by the algorithm by the end of its execution. In Python an algorithm can be implemented as a function, and then typically the input is given as the function parameters and the output is the return value.


## What is a data structure?

A *data structure* is a way of storing data within a program. The choice of data structures is an important part of designing an algorithm, because the data structures have a big effect on the efficiency of the algorithm.


## Implementing an algorithm

Any algorithm can be implemented with a few basic programming constructs. In Python, these basic constructs are:

- variables
- operators (+, = etc.)
- conditionals (if)
- loops (for, while)
- lists
- functions
- classes

In addition to these, programming languages have many other features that can help shorten the code, but do not affect the fundamental operating logic of the code. They can be used in implementing algorithms but are not necessary.


### Efficiency of algorithms

The same task can be solved by different algorithms, and there can be big differences in their efficiencies. Often the goal is to find an efficient algorithm that solves the task quickly.

### Measuring efficiency

The efficiency of an algorithm can be studied with a test program that runs the algorithm for a given input and measures the execution time. It is often a good idea to write the test program so that it generates a random input of a given size. Then it is easy to test the algorithm with inputs of different sizes.


## Analysis of algorithms

The efficiency of an algorithm can be estimated by counting how many steps the algorithm executes for an input of a given size. Often we can think of a step as corresponding to a line of code.

### Time complexity

Often we do not need to determine the exact number of steps, but it is enough to know the time complexity, which gives the magnitude of the number of steps on a given input size.

A time complexity is usually shown in the form `O(⋯)`, where the three dots are replaced by an arithmetic expression representing an upper bound on the number of steps. The expression involves a variable `n` that represents the size of the input.

Common time complexities include:
| **Time complexity** | **Name of complexity class** |
| ----------- | ----------- |
| *O*(1) | Constant |
| *O*(log *n*) |	Logarithmic |
| *O*(*n*) | Linear |
| *O*(*n* log *n*) | – |
| *O*(*n*^2^) |	Quadratic |
| *O*(*n*^3^) | Cubic |
|


### Time complexity of loops
In practice, the time complexity is often determined by the loops in the code.

#### *Constant time*

If an algorithm has no loops and it executes the same steps independent of the input, its time complexity is *O*(1).

#### *Single loop*

If the algorithm contains a single loop that goes through all elements of the input, its time complexity is *O*(*n*).

#### *Nested loops*

If an algorithm contains a loop inside a loop, each of which goes through all elements of the input, its time complexity is *O*(*n*^2^).

#### *Sequential code segments*

If the algorithm consists of multiple code segments in sequence, the whole time complexity is the maximum of the segment time complexities.



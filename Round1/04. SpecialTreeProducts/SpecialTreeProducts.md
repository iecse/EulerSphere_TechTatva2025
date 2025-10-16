# Spectral Tree Products

Problem 127

### Description:

A **spectral tree** is a labeled tree where each vertex v is assigned a weight equal to its degree (number of edges connected to it). For any spectral tree T, we define its **spectral product** S(T) as the product of all vertex weights.

For example, consider this spectral tree on 4 vertices:

```
  1---2---3---4
```

The degrees are: vertex 1 has degree 1, vertex 2 has degree 2, vertex 3 has degree 2, vertex 4 has degree 1.
So S(T) = 1 × 2 × 2 × 1 = 4.

Consider the spectral tree on 5 vertices:

```
    2
    |
1---3---4
    |
    5
```

The degrees are: 1→1, 2→1, 3→3, 4→1, 5→1.
So S(T) = 1 × 1 × 3 × 1 × 1 = 3.

For all possible labeled trees on exactly 6 vertices, there are 6^(6-2) = 1296 such trees by Cayley's formula. Among these, exactly 52 trees have spectral products that are perfect squares.

Find the sum of spectral products S(T) for all labeled trees T on exactly **9** vertices where S(T) is both a **perfect square** and **divisible by 7**.

### Answer:

```
0
```

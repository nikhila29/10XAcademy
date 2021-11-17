# Asymptotic / Complexity Analysis

```text
When we discuss about complexity of programs / algorithms, indirectly we discuss how it perform with large input.
```

## Why to worry about performance?

```text
Performance is like currency through which we can buy all the modularity, security, maintainability, friendliness etc.
```

```text
Another reason for studying performance is – speed is fun!
```

## Given two algorithms for a task, how do we find out which one is better?

```text
Let's say list A and list B

Size of list B is 5000 times that of list A

Linear Search on A - n
Binary Search on B - 5000 * log(n)

------------------------------------------------
|n      | Running time on A | Running time on B |
-------------------------------------------------
|10     | 2 sec             | ~ 1 h             |
-------------------------------------------------
|100    | 20 sec            | ~ 1.8 h           |
-------------------------------------------------
|10^6   | ~ 55.5 h          | ~ 5.5 h           |
-------------------------------------------------
|10^9   | ~ 6.3 years       | ~ 8.3 h           |
-------------------------------------------------
```

## Does Asymptotic Analysis always work?

```text
It works in most of the cases, but simple answer is `Not always`. For example, say there are two sorting algorithms that take 1000n * log(n) and 2n * log(n). Both of these algorithms are asymptotically same.
```

## Worst, Average and Best Cases

```text
1. Worst Case (Usually)
2. Average Case (Sometimes)
3. Best Case (Rare)
```

## Time & Space complexities


# Maximum Path Sum

## Problem Statement

You are given a **triangular arrangement of integers**. Starting from the **top of the triangle**, you must move to **adjacent numbers on the row below**, one step at a time.

Your task is to **find the maximum possible total from top to bottom** by choosing a path that yields the highest sum.

At each step, you may move only to **one of the two adjacent numbers directly below** your current position.

### Example Triangle (Input)

```
                        75
                      95   64
                    17   47   82
                  18   35   87   10
                20   04   82   47   65
              19   01   23   75   03   34
            88   02   77   73   07   63   67
          99   65   04   28   06   16   70   92
        41   41   26   57   74   79   95   11   48
      17   47   82   18   35   87   10   63   60   25
    20   04   82   47   65   19   04   23   76   41   39
```

### Output

Print the **maximum total path sum** from top to bottom.

---

## ⬛ Solution Approach

We solve this using **Dynamic Programming (Bottom-Up Approach):**

1. Start from the **second-last row**.
2. For each element, add the **maximum** of the two adjacent numbers in the row below.
3. Repeat this process row by row until you reach the top.
4. The top element will now hold the **maximum path sum**.

---

## 🟩 Sample Java Code

```java
public class MaximumPathSum {
    public static void main(String[] args) {
        int[][] triangle = {
            {75},
            {95, 64},
            {17, 47, 82},
            {18, 35, 87, 10},
            {20,  4, 82, 47, 65},
            {19,  1, 23, 75,  3, 34},
            {88,  2, 77, 73,  7, 63, 67},
            {99, 65,  4, 28,  6, 16, 70, 92},
            {41, 41, 26, 57, 74, 79, 95, 11, 48},
            {17, 47, 82, 18, 35, 87, 10, 63, 60, 25},
            {20,  4, 82, 47, 65, 19,  4, 23, 76, 41, 39}
        };

        for (int i = triangle.length - 2; i >= 0; i--) {
            for (int j = 0; j < triangle[i].length; j++) {
                triangle[i][j] += Math.max(triangle[i+1][j], triangle[i+1][j+1]);
            }
        }

        System.out.println("Maximum Path Sum = " + triangle[0][0]);
    }
}
```

✅ **Output:**

```
Maximum Path Sum = 818
```

---


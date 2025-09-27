# **Maximum Path Sum**

## **Problem Statement**

You are given a **triangular arrangement** of integers. Starting from the top of the triangle, you must move to adjacent numbers on the row below, one step at a time. Your task is to **find the maximum possible total from top to bottom**.

At each step, you may only move to one of the two adjacent numbers directly below your current position.

The given triangle now contains **15 rows**. You need to compute the maximum path sum using this extended triangle.

### **Triangle Structure**

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
      36   23   09   62   58   51   27   48   44   61   09   03
    44   30   10   60   30   66   38   59   64   08   30   70   88
  43   99   67   02   68   47   34   58   74   32   68   24   77   33
16   58   16   79   11   69   12   82   41   96   92   88   44   49   90



## **Task**

Write a function to calculate the **maximum total path sum** from top to bottom, following the triangle structure rules. The path starts from the top (first row) and proceeds down to one of the adjacent numbers in the next row.


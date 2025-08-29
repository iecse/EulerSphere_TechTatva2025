A Pythagorean triple is a set of integers (a,b,c) such that 
          a^2+ b^2 = c^2
Such a triple represents the sides of a right triangle.

Now imagine trying to tile a c × c square using 4 copies of such a triangle.
For this tiling to perfectly fill the square without gaps, the following condition must hold:
         c%(c-b)=0
That is, the difference between the hypotenuse c and the longer leg b must exactly divide c.
Given an integer N, find the total number of valid Pythagorean triples (a,b,c) such that :
1. a < b < c < =  N
2.  a^2+ b^2 = c^2
3.Print the total count for N = 50

                   

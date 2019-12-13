#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  a = 0
    while (a < n * n * n):
      a = a + n * n
o(1)
o(n^3)
o(n^2)

n^3 but runs n^2 everytime.the rate of growth would be just o(n)
linear time




b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
o(1)- constant
o(n)- linear
o(1)- constant
o(n)- linear
o(log n)- logarithmic
o(1)- constant
there are nested loops so o(n log n)


c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
o(1) base case
o(n)

loops one bunny at a time until 0:  o(n)
a crazy long list of bunnies will call to bunnyEars to run bunnies-1 every time until list reaches 0

## Exercise II
---binary search would be useful here(runtime of o(log n) as steps are reduced as more floors are added)
-building has already sorted floors so cool
-Cut this problem into above, below, and middle.

  ## STEPS
  Go to middle as starting point
  if egg breaks, count out floors above
  else if doesnt break, count out all floors below
  keep iterating through until highest floor, f,  where the egg would not break
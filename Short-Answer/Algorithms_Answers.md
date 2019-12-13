#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  a = 0
    while (a < n * n * n):
      a = a + n * n
o(1)
o(n^3)
o(n^2)

-only 1 loop of iterations
-n^3 but gets n^2 update everytime.
-the rate of growth would be just: o(n) linear time




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

-function is called recursively n times before base case is reached:  o(n) Linear time
-a crazy long list of bunnies will call to bunnyEars to run bunnies-1 every time until list reaches 0

## Exercise II

---binary search would be useful here(runtime of o(log n) as steps are reduced as more floors are added)
--assuming we have all the eggs from walmart.
-building has already sorted floors so cool
-Cut this problem into above, below, and middle.

  ## IDEAS TO START ON
  def eggs(n):
  n for floors starting at 1
  above = len(n) -1
  below= 0
  middle = (above + below) //2
  if n <= 0:
    return None
  egg_broken = False

  ## STEPS
  Go to middle as starting point
  if egg breaks, count out floors above
  else if doesnt break, count out all floors below
  keep iterating through until highest floor, f,  where the egg would not break
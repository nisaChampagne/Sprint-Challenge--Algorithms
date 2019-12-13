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
there are nested loops so multiply o(n) with o(log(n)) === o(n log n)

dmv
 4 dif places in dmv to go to
 have to go to each
 however for some reason they sped up
 cost factor is based on money
  normally 100 bucks
  but due to tax
  take 100, square root it
  still have to pay 100 at each stall


c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
o(1) base case
o(n)

-function is called recursively n times before base case is reached:  o(n) Linear time
-a crazy long list of bunnies will call to bunnyEars to run bunnies-1 every time until list reaches 0

## Exercise II

## Breakdown
-n-story building and plenty of eggs
-Suppose also that an egg gets broken if it is thrown off floor f or higher
-doesn't get broken if dropped off a floor less than floor f
-determine the value of f such that the number of dropped + broken eggs is minimized.

## Questions?
  How many eggs do we have at our disposal? Plenty is pretty out there
  Are we dropping eggs of each floor, each time?
  How many floors in the building?

## Notes
---binary search would be useful here(runtime of o(log n) as steps are reduced as more floors are added)
--assuming we have all the eggs.
-building has already sorted floors so cool
-Cut this problem into above, below, and middle.

## input
n = list of floors in order

## variables needed
f = highest floor w/ no egg breaking
above = len(n)-1
below = 0
mid = (below + above) // 2

## STEPS
-Store highest floor,f, where the egg would not break
-below = 0
-above = len(n) -1
-Go to middle as starting point (below + above) // 2
-If egg breaks:
 rule out floors above because those are going to be scrambled eggs
-Else if doesnt break:
 rule out all floors below (Could keep going up if indeed have plenty of eggs )
-Keep iterating through until highest floor, f,  where the egg would not break
-store floor num in variable f
-Return highest floor, f


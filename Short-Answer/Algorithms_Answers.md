#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
  O(N)
  I say that this is O(N) because for how many numbers that n increases the amount of steps increase by the same amount. Also the math breaks down to N^3/N^2 which is the same as N/1 or N if you divide the numerator and denominator by N^2. So it is just running a single loop through a range of N.

b)
  O(Nlog(N))
  I say that this is O(Nlog(N)) because there is a loop for each number in the range N so we have an O(N). Then we have a nested loop inside of that loop that is incrementing by an amount that is doubling with each loop and is moving towards N. Since it is doubling with each increment we know that it is a O(log(N)).
  This leaves us with O(N) * O(log(N)) = O(Nlog(N))
c)
  O(N)
  I say O(N) because it is taking N a number of bunnies and it is counting 2 for each one of them. It does this recursively by decrementing N by 1 and return 2 + total for each bunny and ending when num of bunnies is 0.

## Exercise II

I would do a binary search for this.

while there is a difference between the first and last floor

  add first floor to the last floor and divide by 2 and round down to get the middle floor
  keep track of the highest floor if the egg doesnt break
  go to the mid floor and drop and egg
  if the egg breaks then go to the mid of the floor you are on and the first floor
  and change last floor to the one under you
  else egg does not break then go to the mid of floor you are on and the last floor,
  change first floor to one you are on, and change highest floor the one you are on

when the first and last floor are equal then you know that the highest floor variable is the highest you can drop from

The runtime for this should be O(log(N))

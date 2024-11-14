## Homework INI4 2024_11_15
~~~ Python
# Problem
#Given: Two positive integers a and b  (a<b<10000).
# Return: The sum of all odd integers from a  through b, inclusively.
# Sample 100 200
# Output 7500
x_new=0
for x in range(4240, 8925):
  if x % 2 == 1:
    x_new = x_new + x
    print(x_new)
#Solution: 15415044
~~~
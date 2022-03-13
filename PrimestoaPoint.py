#Gives all the prime numbers until a certain point?
n = int(input("Please enter a number to get all the prime numbers until that number: "))
primelist = []
for number in list(range(1, n+1)):
  hit = 0
  for divider in list(range(1, number+1)):
    if number % divider == 0:
      hit += 1
  if hit == 2:
    primelist.append(number)
print(f"The prime numbers until {n} are: \n {primelist}")

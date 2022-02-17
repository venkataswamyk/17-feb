n=int(input('enter a number:'))
esum=0
0sum=0
for num in range(1,n+1):
  if num%2==0:
    esum=esum+num
  else:
    osum=osum+num
print('sum of even numbers upto',n,'is equal to',esum)
print('sum of odd numbers upto',n,'is equal to',osum)

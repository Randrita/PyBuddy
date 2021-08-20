for _ in range(int(input())):
      sum = 0
  n =int(input())
  for x in range(1, n):
    if n % x == 0:
      sum += x
        
  if sum== n:
    print('true')
  else:
    print('false')
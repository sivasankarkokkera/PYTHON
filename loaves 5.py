def price_cal(t,r):
  price = 185.00
  discount = price*60/100
  new_loaves = round(price*t,2)
  old_loaves = round(discount*r,2)
  print(f"Regular Price: {price}")
  print(f"Amount of new loaves: {new_loaves}")
  print(f"Amount of day old loaves: {old_loaves}")
  print(f"Total amount: {new_loaves+old_loaves}")

n = int(input("Enter the no of fresh loaves: "))
i = int(input("Enter the no of day old loaves: "))

if n<0 or i<0:
  print("input cant be negative")
else:
  price_cal(n,i)

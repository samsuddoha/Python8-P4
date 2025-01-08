def yourfunction():
  a = 5
  b = 6
  # nested function
  def myfunction():
     nonlocal a
     nonlocal b
     a = 10
     b = 20
     print("Inside- a:", a)
     print("Inside- b:", b)
     return a+b

  print (myfunction())
  print("Outside- a:", a)
  print("Outside- b:", b)

yourfunction()

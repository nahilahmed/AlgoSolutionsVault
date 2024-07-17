def my_function(param1,param2):
 print("This is a test function")
 if param1 > param2:
  print("Param1 is greater than Param2")
  print("Halleloooya")
  return param1
 else:
  print("Param2 is greater than or equal to Param1")
  return param2

def another_function():
  x=  10
  y= 5
  z=   my_function(x,y)
  print("The result is: ",z)

another_function()
 
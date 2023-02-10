# Outer function
global function1
def function1():
  global var1
  var1 = 1
  var2 = 2
  # Inner function
  def function2():
    nonlocal var2
    global var3
    var2 += 1
    var3 = 3
    print(globals())
    print(locals())
  
  # Call inner function
  function2()

# Call outer function
function1()
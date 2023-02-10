color = 'green'
def change_color(new_color):
  global color
  # Checkpoint #2
  to_update = new_color
  
  def disp_color():
    print('The original color was: ' + color)

  disp_color()
  # Checkpoint #3
  color = to_update
  print('The new color is: ' + color)
change_color('blue')
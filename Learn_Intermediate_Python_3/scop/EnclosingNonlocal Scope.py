def calc_paint_amount(width, height):
  square_feet = width * height
  # Checpoint #2
  def calc_gallons():
      return square_feet / 400
  # Checkpoint #3
  return calc_gallons()
print('Number of paint gallons needed: ')
print(str(calc_paint_amount(30,20)))
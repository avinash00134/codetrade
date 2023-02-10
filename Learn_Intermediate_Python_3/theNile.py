from nile import get_distance, format_price, SHIPPING_PRICES
from test import test_function

# Define calculate_shipping_cost() here:
def calculate_shipping_cost(from_coords,to_coords,shipping_type="Overnight"):
  from_lat,from_long = from_coords
  to_lat,to_long = to_coords

  distance = get_distance(from_lat,from_long,to_lat,to_long)

  shipping_rate = SHIPPING_PRICES[shipping_type]
  price = distance * shipping_rate
  return format_price(price)


# Test the function by calling 
test_function(calculate_shipping_cost)

# Define calculate_driver_cost() here
def calculate_driver_cost(distance,*drivers):
  cheapest_driver=None
  cheapest_driver_price = None

  for driver in drivers:
    print(driver.speed)
    driver_time = distance / driver.speed
    print(driver_time)
    print(driver.salary)
    price_for_driver = driver.salary * driver_time
    if cheapest_driver is None:
      cheapest_driver = driver
      cheapest_driver_price = price_for_driver
    elif price_for_driver < cheapest_driver_price:
      cheapest_driver = driver
      cheapest_driver_price = price_for_driver
  return cheapest_driver_price,cheapest_driver  
  
  
  
  
  #Sam's Surf Shop PROJECT
  import surfshop
import unittest
import datetime
class Tests(unittest.TestCase):
  def setUp(self):
    self.cart = surfshop.ShoppingCart()

  def test_add_surfboard(self):
        message = self.cart.add_surfboards(quantity=1)
        self.assertEqual(message, f'Successfully added 1 surfboard to cart!')

  def test_add_surfboards(self):
        for i in range(2, 5):
            with self.subTest(i=i):
                message = self.cart.add_surfboards(i)
                self.assertEqual(message, f'Successfully added {i} surfboards to cart!')
                self.cart = surfshop.ShoppingCart()

  @unittest.skip
  def test_add_surfboards(self, num):
    for n in [2, 3, 4]:
      with unittest.subTest(num):
        self.assertRaises(surfshop.TooManyBoardsError, surfshop.ShoppingCart().add_surfboards(num))

  #@unittest.expectedFailure
  def test_apply_locals_discount(self):
        self.cart.apply_locals_discount()
        self.assertTrue(self.cart.locals_discount)

  def test_add_invalid_checkout_date(self):
        date = datetime.datetime.now()
        self.assertRaises(surfshop.CheckoutDateError, self.cart.set_checkout_date, date)

unittest.main()

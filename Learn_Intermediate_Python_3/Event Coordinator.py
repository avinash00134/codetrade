guests = {}
def read_guestlist(file_name):
  text_file = open(file_name,'r')
  while True:
    line_data = text_file.readline().strip().split(",")
    if len(line_data) < 2:
    # If no more lines, close file
      text_file.close()
      break
    name = line_data[0]
    age = int(line_data[1])
    guests[name] = age
    yield name, age


guest_generator = read_guestlist('guest_list.txt')


i=0
for guest in guest_generator:
  if i < 10:
    print(guest)
    i += 1
  else:
    break

drinks_generator = (name for name, age in guests.items() if age >= 21 )

def Table_1():
  food = 'Chicken'
  table = 1
  for i in range(1,6):
    seat = i
    yield food, table, seat

def Table_2():
  food = 'Beef'
  table = 2
  for i in range(1,6):
    seat = i
    yield food, table, seat


def Table_3():
  food = 'Fish'
  table = 3
  for i in range(1,6):
    seat = i
    yield food, table, seat

def all_tables():
  yield from Table_1()
  yield from Table_2()
  yield from Table_3()

tab = all_tables()

assign = ((guest, table) for guest, table in zip(guests, tab))

for i in range(15):
  try:
    print(next(assign))
  except StopIteration:
    print("Generator exhausted.")
    break
# Output:
# ('Tim', 22)
# ('Tonya', 45)
# ('Mary', 12)
# ('Ann', 32)
# ('Beth', 20)
# ('Sam', 5)
# ('Manny', 76)
# ('Kenton', 15)
# ('Kenny', 27)
# ('Dixie', 46)
# ('Tim', ('Chicken', 1, 1))
# ('Tonya', ('Chicken', 1, 2))
# ('Mary', ('Chicken', 1, 3))
# ('Ann', ('Chicken', 1, 4))
# ('Beth', ('Chicken', 1, 5))
# ('Sam', ('Beef', 2, 1))
# ('Manny', ('Beef', 2, 2))
# ('Kenton', ('Beef', 2, 3))
# ('Kenny', ('Beef', 2, 4))
# ('Dixie', ('Beef', 2, 5))
# Generator exhausted.
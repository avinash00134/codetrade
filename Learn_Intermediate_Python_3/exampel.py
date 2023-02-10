
def update_order(new_item, current_order=[]):
  current_order.append(new_item)
  return current_order
order1 = update_order({'item': 'burger', 'cost': '3.50'})
order2 = update_order({'item': 'soda', 'cost': '1.50'})
print(order2)
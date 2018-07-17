def ground_shipping(weight):
  cost = 0
  if (weight <= 2):
    cost = weight * 1.50 + 20.0
    return cost 
  elif (weight >2) and (weight<=6):
    cost = weight * 3.0 + 20.0
    return cost
  elif (weight>6) and (weight<=10):
    cost = weight * 4.0 + 20.0
    return cost
  else:
    cost = weight * 4.75 + 20.0
    return cost
""""print(ground_shipping(8.4))"""
PREMIUM_GROUND_COST = 125

def drone_shipping(weight):
  cost = 0
  if (weight <= 2):
    cost = weight * 4.50 + 0.0
    return cost
  elif (weight >2) and (weight<=6):
    cost = weight * 9.0 + 0.0
    return cost
  elif (weight>6) and (weight<=10):
    cost = weight * 12.0 + 0.0
    return cost
  else:
    cost = weight * 14.25 + 0.0
    return cost
"""print (drone_shipping(1.5))"""
def cheapest_shipping(weight):
  if (ground_shipping(weight) < drone_shipping(weight)) and (ground_shipping(weight) < PREMIUM_GROUND_COST):
    return "ground shipping method is cheapest "+ str(ground_shipping(weight))
  elif (ground_shipping(weight) > drone_shipping(weight)) and (drone_shipping(weight) < PREMIUM_GROUND_COST):
    return "drone shipping method is cheapest: "+ str(drone_shipping(weight))
  else:
    return "premium shipping method is cheapest "+ str(PREMIUM_GROUND_COST)
  try:
    cheapest_shipping(weight)
  except TypeError:
    print("Erreur dans la fonction")
print(cheapest_shipping(4.8))
print(cheapest_shipping(41.5))

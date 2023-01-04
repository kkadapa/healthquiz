def calculate_score(email, exercise, fruits_veggies, sugary_drinks, sleep, tobacco):
  score = 0
  if exercise == 'a':
    score += 0
  elif exercise == 'b':
    score += 1
  elif exercise == 'c':
    score += 2
  elif exercise == 'd':
    score += 3
  else:
    return 'Invalid input'

  if fruits_veggies == 'a':
    score += 0
  elif fruits_veggies == 'b':
    score += 1
  elif fruits_veggies == 'c':
    score += 2
  elif fruits_veggies == 'd':
    score += 3
  else:
    return 'Invalid input'

  if sugary_drinks == 'a':
    score += 0
  elif sugary_drinks == 'b':
    score += 1
  elif sugary_drinks == 'c':
    score += 2
  elif sugary_drinks == 'd':
    score += 3
  else:
    return 'Invalid input'

  if sleep == 'a':
    score += 0
  elif sleep == 'b':
    score += 1
  elif sleep == 'c':
    score += 2
  elif sleep == 'd':
    score += 3
  else:
    return 'Invalid input'

  if tobacco == 'a':
    score += 0
  elif tobacco == 'b':
    score += 3
  else:
    return 'Invalid input'

  return score / 6.0

email = input('Enter your email address: ')
exercise = input('How many days per week do you exercise for at least 30 minutes? (a) 0 days (b) 1-2 days (c) 3-4 days (d) 5 or more days: ')
fruits_veggies = input('How many servings of fruits and vegetables do you eat per day? (a) 0-1 servings (b) 2-3 servings (c) 4-5 servings (d) 6 or more servings: ')
sugary_drinks = input('How many servings of sugary drinks (such as soda, sports drinks, or fruit juice) do you consume per day? (a) 0 servings (b) 1-2 servings (c) 3-4 servings (d) 5 or more servings: ')
sleep = input('How often do you get at least 7 hours of sleep per night? (a) Never (b) Rarely (c) Occasionally (d) Always: ')
tobacco = input('Do you currently smoke cigarettes or use tobacco products? (a) Yes (b) No: ')

score = calculate_score(email, exercise, fruits_veggies, sugary_drinks, sleep, tobacco)
print(f'Your score is {score}')

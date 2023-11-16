import random

w = 'Welcome to the snake-water-gun game\n'
print(w)
Rules = "Rules:-\n\nSnake drinks the water - Snake won\nGun swims in the water - Water won\nGun shoots the snake - Gun won"
print(Rules)

while True:
  print("""\nSelect your choice    
    1-snake
    2-water
    3-Gun
    """)
  lst = [1, 2, 3]
  a = int(input("Enter your choice: "))
  b = int(random.choice(lst))
  print("Computer's Choice:", b)

  try:
    if (a == 1 and b == 1):
      print("draw")
    elif (a == 1 and b == 2):
      print("You Won")

    elif (a == 2 and b == 1):
      print("Computer Won")

    elif (a == 1 and b == 3):
      print("Computer Won")

    elif (a == 3 and b == 1):
      print("You Won")

    elif (a == 2 and b == 2):
      print("draw")

    elif (a == 2 and b == 3):
      print("You Won")

    elif (a == 3 and b == 2):
      print("Computer Won")

    elif (a == 3 and b == 3):
      print("draw")

    else:
      print("Enter a valid Input")

  except:
    print("Enter a valid number")

  finally:
    choice = input("Press Enter to play again or type 'no' to stop: ")
    if choice.lower() == 'no':
      break

print("Thanks for playing")

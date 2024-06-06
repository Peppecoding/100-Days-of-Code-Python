print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
price = 0
if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age <= 12:
    print("Please pay $5.")
    price = 5
  elif age <= 18:
    print("Please pay $7.")
    price = 7
  elif age >=45 and age <+55:
     print("All good the right is on us")
  else:
    print("Please pay $12.")
    price = 12
else:
  print("Sorry, you have to grow taller before you can ride.")
    


#  Photo path

while True:
        photo_answer = input("\nDo you want a photo for $3? Yes/No\n")
        if photo_answer.lower() == "yes":
            photo_price = 3
            print(f"The total bill is ${price + photo_price}")
            break
        elif photo_answer.lower() == "no":
            print(f"Thank you, your total bill is ${price}")
            break
        else:
            print("Please answer 'Yes' or 'No'")




# This program is to ask the user for name, age, major and favorite hobby, 
# then f string a formatted summary 
# ---------------------------------------------------------------------------

#pseudocode: start program / greeting 
print("Hello, This program is designed to create an template for introductions!")
name = str(input("What is your name: ")) #pseudocode: Ask user for name

print(f"Hello, {name}! It's nice to meet you")
age = int(input("How old are you? "))

print(f"Your age is {age}, okay lets move on to the next question.")
major = str(input("What are you majoring in? "))

print(f"Ah! {major} thats a intresting concept to major in")
print("Finally, The last question!")

hobby = str(input("What is one hobby you can say is your favorite? "))
print(f"You favorite hobby is {hobby}, okay I should have eveything I need\n..........pleae hold")

#pseudocode: print to summary 
print(f"Hello! my name is {name}, I'm {age} and I'm currently in College\n majoring in {major} and ")
print(f"My favorite hobby is {hobby}! It's nice to meet you.")
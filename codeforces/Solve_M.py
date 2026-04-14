# M : Capital or Small or Digit

input_character = input()
if input_character.isalpha():
    print("ALPHA")
    if input_character.isupper():
        print("IS CAPITAL")
    else:
        print("IS SMALL")
if input_character.isdigit():
    print("IS DIGIT")

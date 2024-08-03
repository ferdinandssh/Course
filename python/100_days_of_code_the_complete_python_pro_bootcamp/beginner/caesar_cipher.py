alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

import random

valid_direction = False
valid_shift = False

while not valid_direction:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  if direction.lower() != 'encode' and direction.lower() != 'decode':
    print("Invalid input.Please try again.")
  else:
    valid_direction = True

text = input("Type your message:\n").lower()

while not valid_shift:
  shift = input("Type the shift number:\n")
  if shift.isnumeric() == False:
    print("Invalid input.Please try again.")
  else:
    valid_shift = True
    shift = int(shift)
    if shift > 25:
      shift = shift % 26


def caesar(start_text,shift_amount, direction_action):
  end_text = ""

  if direction_action == 'encode':
    shift_amount = shift_amount * 1
  elif direction_action == 'decode':
    shift_amount = shift_amount * -1

  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      if new_position > 25:
        new_position = new_position - 26
      elif new_position < 0:
        new_position = new_position + 26
      end_text += alphabet[new_position]
    else:
      end_text += char

  print(f"here is the {direction_action}d result: {end_text}")



caesar(start_text = text,shift_amount = shift, direction_action = direction)

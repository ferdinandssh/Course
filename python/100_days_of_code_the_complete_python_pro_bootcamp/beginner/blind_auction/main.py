from art import logo

print(logo)
print("Welcome to the secret auction program.\n")


def find_highest_bidder(bidder_dict):
  highest_bid = 0
  highest_bidder = ""
  for n in bidder_dict:
    if bidder_dict[n] > highest_bid:
      highest_bid = bidder_dict[n]
      highest_bidder = n
  print(f"The winner is {n} with a bid of ${highest_bid}")


#INPUT
bidder = {}
ask_other_bidder = "yes"
while ask_other_bidder == "yes":
  #BIDDER INPUT
  name = input(f"What is your name?: ")

  valid_bid = False
  while not valid_bid:
    ask_bid = input(f"What's your bid?: $")
    if ask_bid.isnumeric():
      ask_bid = int(ask_bid)
      valid_bid = True
    else:
      print("Invalid input. Please input valid number.")

  bidder[name] = ask_bid

  valid_ask_other_bidder = False
  while not valid_ask_other_bidder:
    ask_other_bidder = input(
        "Are there any other bidders? Type 'yes' or 'no'.")
    if ask_other_bidder.lower() != "yes" and ask_other_bidder.lower() != "no":
      print("Invalid input. Please type 'yes' or 'no'.")
    else:
      valid_ask_other_bidder = True

find_highest_bidder(bidder)

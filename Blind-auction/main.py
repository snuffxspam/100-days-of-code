logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
name = input("What's your name?\n")
bid = int(input("How much are you bid?\n$"))
score = {name:bid}
bool = True
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")
while bool:
  answer = input("Are there any other bidders? Type 'yes or 'no'.\n".lower())
  if answer == "yes":
    name = input("What's your name?\n")
    bid = int(input("How much are you bid?\n$"))
    score = {name:bid}
  else:
    find_highest_bidder(score)
    bool = False
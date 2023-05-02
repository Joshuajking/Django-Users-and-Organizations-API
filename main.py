# Create a list of dictionaries that contain the information for each credit card, such as the current balance, interest rate, and minimum payment.
cards = [
    {"balance": 2447.71, "interest_rate": 29.99, "min_payment": 74},
    {"balance": 285.95, "interest_rate": 29.99, "min_payment": 40},
    {"balance": 482.64, "interest_rate": 29.99, "min_payment": 40},
    {"balance": 686.57, "interest_rate": 29.99, "min_payment": 40},
]

# Calculate the total minimum payment for all credit cards.
total_min_payment = sum(card["min_payment"] for card in cards)
print(total_min_payment)
# Determine the extra amount of money available to pay off credit cards each month. This can be the difference between the total amount you can afford to pay each month and the total minimum payment.
extra_payment = 0 - total_min_payment
print(extra_payment)
# assuming a total budget of 500 per month
# Calculate the interest charged on each credit card per month.
for card in cards:
    card["interest_charged"] = card["balance"] * card["interest_rate"] / 12
print(card)
# Sort the credit cards by their interest charged in ascending order.
sorted_cards = sorted(cards, key=lambda x: x["interest_charged"])

# Apply the extra payment amount to the credit card with the highest interest rate until it is paid off. Then, move on to the next highest interest rate card and continue until all cards are paid off.
while extra_payment > 0:
    for card in sorted_cards:
        if card["balance"] > card["min_payment"]:
            payment = min(card["balance"] - card["min_payment"], extra_payment)
            card["balance"] -= payment
            extra_payment -= payment
        if extra_payment == 0:
            break

# Print out the total amount paid, the amount of interest saved, and the number of months it took to pay off all credit cards.
total_paid = sum(card["balance"] for card in cards)
interest_charged = sum(card["interest_charged"] for card in cards)
for card in sorted_cards:
    interest_charged -= card["interest_charged"]
interest_saved = interest_charged
months = int(total_paid / (500 - interest_saved))
print(f"Total amount paid: ${total_paid:.2f}")
print(f"Interest saved: ${interest_saved:.2f}")
print(f"Number of months: {months}")


# This algorithm assumes that you want to pay off all credit cards as quickly as possible while minimizing the amount of interest paid. It does not take into account any rewards or other benefits that may be associated with each credit card.


# if __name__ == "__main__":
#   main()

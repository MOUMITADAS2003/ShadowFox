# 1. Create a list of your friends' names. The list should have at least 5 names.
#  Create a list of tuples. Each tuple should contain a friend's name and the length
#  of the name. 
# For example, if someone’s name is Aditya, the tuple would be: ('Aditya', 6)



# Ask user to enter 5 friends' names
friends = []

for i in range(5):
    name = input(f"Enter name of friend {i+1}: ")
    friends.append(name)

# Create list of tuples (name, length of name)
name_length = [(name, len(name)) for name in friends]

print("\nFriends and their name lengths:")
print(name_length)




# 2.You and your partner are planning a trip, and you want to track expenses.
#  Create two dictionaries, one for your expenses and one for your partner's
#  expenses. Each dictionary should contain at least 5 expense categories and their
#  corresponding amounts



# Create dictionaries for expenses
your_expenses = {}
partner_expenses = {}

# Define categories
categories = ["Hotel", "Food", "Transportation", "Attractions", "Miscellaneous"]

print("Enter your expenses:")
for category in categories:
    amount = int(input(f"How much did you spend on {category}? "))
    your_expenses[category] = amount

print("\nEnter your partner's expenses:")
for category in categories:
    amount = int(input(f"How much did your partner spend on {category}? "))
    partner_expenses[category] = amount

# Calculate totals
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print("\n--- Trip Expenses Summary ---")
print("Your total expenses:", your_total)
print("Partner's total expenses:", partner_total)

# Who spent more
if your_total > partner_total:
    print("You spent more money overall.")
elif partner_total > your_total:
    print("Your partner spent more money overall.")
else:
    print("Both spent the same amount.")

# Find category with biggest difference
max_diff = 0
diff_category = ""

for category in categories:
    diff = abs(your_expenses[category] - partner_expenses[category])
    if diff > max_diff:
        max_diff = diff
        diff_category = category

print(f"The biggest difference is in '{diff_category}' with a difference of {max_diff}.")


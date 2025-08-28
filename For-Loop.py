# 1. Using a for loop, simulate rolling a sixsided die multiple times (at least 20
#  times). 
# Count and print the following statistics: 
# How many times you rolled a 6 
# How many times you rolled a 1 
# How many times you rolled two 6s in a row


import random

rolls = 20   # number of times to roll
count_6 = 0
count_1 = 0
two_6s_in_a_row = 0

previous_roll = 0

for i in range(rolls):
    roll = random.randint(1, 6)   # simulate die roll
    print(f"Roll {i+1}: {roll}")
    
    if roll == 6:
        count_6 += 1
        if previous_roll == 6:
            two_6s_in_a_row += 1
    if roll == 1:
        count_1 += 1
    
    previous_roll = roll

print("\nStatistics:")
print("Total 6s rolled:", count_6)
print("Total 1s rolled:", count_1)
print("Two consecutive 6s rolled:", two_6s_in_a_row)




# 2. Imagine you are doing a workout routine, and you have to complete 100
#  jumping jacks. 
# Write a program that: 
# Asks you to perform 10 jumping jacks at a time. 
# After each set, it asks, "Are you tired?" 
# If you reply "yes" or "y," it should ask if you want to skip the remaining sets. 
# If you reply "yes" or "y," it should break and print, "You completed a total of
#  jumping jacks." 



total_jacks = 100
done = 0

for i in range(10):  # 10 sets of 10
    done += 10
    print(f"You completed {done} jumping jacks.")
    
    if done == total_jacks:
        print("🎉 Congratulations! You completed the workout.")
        break
    
    tired = input("Are you tired? (yes/no): ").lower()
    
    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/no): ").lower()
        if skip in ["yes", "y"]:
            print(f"You completed a total of {done} jumping jacks.")
            break
    else:
        print(f"{total_jacks - done} jumping jacks remaining.\n")

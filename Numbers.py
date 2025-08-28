# 1. Write a function that takes two arguments, 145 and 'o', and
#  uses the `format` function to return a formatted string. Print the
#  result. Try to identify the representation used.


def format_number(num, fmt):
    result = format(num, fmt)
    print(result)
    return result

format_number(145, 'o')



# 2. In a village, there is a circular pond with a radius of 84 meters.
#  Calculate the area of the pond using the formula: Circle Area = π
#  r^2. (Use the value 3.14 for π) Bonus Question: If there is exactly
#  1.4 liters of water in a square meter, what is the total amount of
#  water in the pond? Print the answer without any decimal point in
#  it. Hint: Circle Area = π r^2 Water in the pond = Pond Area
#  Water per Square Meter


r = 84
pi = 3.14
area = pi * r * r   # Circle area
water_per_sqm = 1.4  # liters per sq.m
water = area * water_per_sqm

print("Pond Area:", int(area))
print("Water in Pond (liters):", int(water))



# 3. If you cross a 490meterlong street in 7 minutes, calculate your
#  speed in meters per second. Print the answer without any decimal
#  point in it. Hint: Speed = Distance / Time


distance = 490
time = 7 * 60  # seconds
speed = distance / time

print("Speed (m/s):", int(speed))

# 1. if / else / elif (Conditional Statements)

score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# For loop
# Iterating over a string
for char in "Python":
    print(char)

# Iterating using range
for i in range(5):  # 0, 1, 2, 3, 4
    print(f"Count: {i}")

for i in range(1, 6): # 1, 2, 3, 4, 5
    print(f"Number: {i}")

# while loop
count = 0
while count < 5:
    print(f"Count is: {count}")
    count += 1 # Same as count = count + 1
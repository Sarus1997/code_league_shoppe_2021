'''
Hands-on#4
'''

numbers = []

while True:
    user_input = input("Enter a number: ").strip()
    if user_input == "":
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if numbers:
    average = sum(numbers) / len(numbers)
    print(f"\nAverage of {len(numbers)} input numbers: {average:.2f}")
else:
    print("\nNo numbers were entered.")

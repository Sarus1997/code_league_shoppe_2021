'''
Hands-on#2
'''

# อ่านจำนวนเงินจากผู้ใช้งาน

def calculate_change(amount):
    denominations = {
        "$10": 10.00,
        "$5": 5.00,
        "$2": 2.00,
        "$1": 1.00,
        "50c": 0.50,
        "20c": 0.20,
        "10c": 0.10
    }

    print(f"Change ($): {amount:.2f}")
    
    for name, value in denominations.items():
        count = int(amount // value)
        amount -= count * value
        amount = round(amount, 2)  # หลีกเลี่ยงตัวเลขทศนิยม
        print(f"{name} x {count}")

amount = float(input("Enter the amount of change in dollars: "))
calculate_change(amount)

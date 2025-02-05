'''
Hands-on#3
'''

def calculate_bill(talk_time, sms_count, data_gb):
    BASE_CHARGE = 50.00
    INCLUDED_TALK_TIME = 120
    INCLUDED_SMS = 50
    INCLUDED_DATA = 5
    TALK_TIME_RATE = 0.25
    SMS_RATE = 0.15
    DATA_RATE = 10.70
    DATA_CAP = 188.00
    TAX_RATE = 0.07

    # Calculate additional usage
    extra_talk_time = max(0, talk_time - INCLUDED_TALK_TIME)
    extra_sms = max(0, sms_count - INCLUDED_SMS)
    extra_data = max(0, data_gb - INCLUDED_DATA)

    # Calculate additional charges
    talk_time_charge = extra_talk_time * TALK_TIME_RATE
    sms_charge = extra_sms * SMS_RATE
    data_charge = min(extra_data * DATA_RATE, DATA_CAP)

    # Calculate subtotal
    sub_total = BASE_CHARGE + talk_time_charge + sms_charge + data_charge

    # Calculate tax
    tax = sub_total * TAX_RATE

    # Calculate total
    total = sub_total + tax

    # Print the bill
    print("")
    print(" " * 15 + "BILL")
    print("==================================")
    print(f"Base charge            : $ {BASE_CHARGE:.2f}")
    print("Additional charges:")
    print(f"  Talk time            : $ {talk_time_charge:.2f}")
    print(f"  SMS                  : $ {sms_charge:.2f}")
    print(f"  Data                 : $ {data_charge:.2f}")
    print("----------------------------------")
    print(f"Sub-total              : $ {sub_total:.2f}")
    print(f"GST (7%)               : $ {tax:.2f}")
    print(f"TOTAL                  : $ {total:.2f}")
    print("-----------------------------------")

talk_time = int(input("Talk time (mins) : "))
sms_count = int(input("SMS              : "))
data_gb = int(input("Data (GB)        : "))

calculate_bill(talk_time, sms_count, data_gb)

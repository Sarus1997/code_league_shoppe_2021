'''
Hands-on#6
'''

def bill(kwh, cubicm):
    # คำนวณค่าน้ำ
    if cubicm < 40:
        water_cost = cubicm * 1.21
    else:
        water_cost = cubicm * 1.52

    # คำนวณค่าไฟ
    electricity_cost = kwh * 20.76 # แปลงจากเซนต์เป็นดอลลาร์

    # รวมค่าใช้จ่ายก่อนภาษี
    total_cost = water_cost + electricity_cost

    # คำนวณภาษี 7%
    total_with_tax = total_cost * 1.07

    return round(total_with_tax, 2)  # ปัดเศษทศนิยม 2 ตำแหน่ง

# ตัวอย่างการใช้งาน
print(bill(100, 50))  # ทดสอบค่าไฟ 100 kWh และค่าน้ำ 50 m³

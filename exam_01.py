'''
Hands-on#1
'''

# อ่านข้อมูลเงินฝากเริ่มต้นและอัตราดอกเบี้ยจากผู้ใช้งาน
principal = float(input("Principal (S$): "))
interest_rate = float(input("Interest (%): "))

# แปลงอัตราดอกเบี้ยจากเปอร์เซ็นต์เป็นทศนิยม
interest_rate /= 100

# คำนวณและแสดงยอดคงเหลือในแต่ละปี
for year in range(1, 4):
    principal += principal * interest_rate
    print(f"Balance after year {year}: S${principal:.2f}")

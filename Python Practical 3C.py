#Name : Atharva Ashish Jadhav.
#Roll NO.: F084.

#To Create A Bill.
print("~~~~~~~Billing~~~~~~~~~")
mrp=int(input("Enter Mrp: "))
quantity=int(input("Enter Quantity: "))
basicBill=mrp * quantity
if basicBill >= 15000:
    disPer = 0.1
else:
    disPer = 0

disAmt= basicBill * disPer
totBill = basicBill - disAmt
gstAmt = totBill * 0.18
billPay = totBill + gstAmt
print()
print()
print("--------INVOICE-------")
print("MRP Rs.",mrp)
print("Quantity",quantity)
print("BAsic Bill Rs.",basicBill)
print("Discount Rs.",disAmt)
print("GST @18% Rs.",gstAmt)
print("Amount Payable Rs.",billPay)
print("----------------------")


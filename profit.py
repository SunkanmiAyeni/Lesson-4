saleamount=float(input("please enter your sales amount"))
actualamount=float(input("please enter your actual amount"))
if saleamount>actualamount:
    profit=saleamount-actualamount
    print("profit is",profit)
else:
    print("there is no profit")
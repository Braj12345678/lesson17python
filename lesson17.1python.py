def total_calc(bill_amount, tip_perc):
    total = bill_amount*(1 + 0.01*tip_perc)
    total = round(total, 2)
    print(f"Total amount to be paid: ${total}")

total_calc(150,20)
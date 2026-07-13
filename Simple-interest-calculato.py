print("===" * 45 )
print("SIMPLE INTEREST CALCULATOR ")
print("==="* 45)
name = input("Enter your name ")
principle_amount = (float(input("Enter the principal amount ")))
if principle_amount < 0 :
    print("invalid information ")
    exit()
rate_interest = (float(input("Enter annual rate of interest (%) ")))
if rate_interest < 0 :
    print("invalid information ")
    exit()
time = (float(input("Enter the time (in years ) ")))
if time < 0 :
    print("invalid information ")
    exit()
simple_interest =( principle_amount * rate_interest * time)/100
total = principle_amount + simple_interest
print(f"Hello  {name}")
print(f"PRINCIPAL AMOUNT : {principle_amount:.2f}")
print(f"RATE OF INTEREST : {rate_interest:.2f} ")
print(f"TIME : {time:.2f} years ")
print(f"SIMPLE INTEREST : {simple_interest:.2f}")
print(f"TOTAL AMOUNT : {total:.2f}")

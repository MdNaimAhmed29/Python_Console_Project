principal_amount = input("Enter the principal amount: ")
principal_amount = float(principal_amount)

rate = input("Enter the rate of interest: ")
time = input("Enter the time (in years): ")

rate = float(rate)
time = float(time)

interest = (principal_amount * rate * time)/100 #interest calculation formula I = P × R × T, where P = Principal, R = Rate of Interest, and T = Time

print("The interest is: ", interest)
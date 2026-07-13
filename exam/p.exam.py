
print("----------------------------------")
print("\Welcome To The Bill Spliter App!")
print("----------------------------------")

total_bill = float(input("Enter total bill amount: ₹"))
people = int(input("Enter number of people: "))

tip_choice = input("Do you want to add tip? (yes/no): ").lower()

tip_amount = 0

if tip_choice == "yes":
    tip_percent = float(input("Enter tip percentage: "))
    tip_amount = (total_bill * tip_percent) / 100

final_bill = total_bill + tip_amount
per_person = final_bill / people

print("\------ Bill Summary ------")
print(f"Original Bill : ₹{total_bill:.2f}")
print(f"Tip Amount    : ₹{tip_amount:.2f}")
print(f"Final Bill    : ₹{final_bill:.2f}")
print(f"Each Person Pays : ₹{per_person:.2f}")

again=input("\n Do another calculations? (yes/no): ").lower()

if again!="yes":

  print("---thankyou for useing to the our bill spliter app---") 


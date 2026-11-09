student_name=input("Enter student name:")
daily_transport_cost=float(input("Enter daily transport cost:"))
daily_feeding_cost=float(input("Enter daily feeding cost:"))
days_on_campus=int(input("Enter number of days on campus:"))
other_expenses=float(input("Enter other expenses for the week:"))
transport_total=daily_transport_cost*days_on_campus
feeding_total=daily_feeding_cost*days_on_campus
weekly_total=transport_total+feeding_total+other_expenses
print("WEEKLY EXPENSE SUMMARY")
print()
print(f"Student:", student_name)
print(f"Transport total:NGN{transport_total:,.2f}")
print(f"Feeding total:NGN{feeding_total:,.2f}")
print(f"Weekly total:NGN{weekly_total:,.2f}")

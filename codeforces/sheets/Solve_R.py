# R : Age in Days

age_days = int(input())
years = age_days // 365
months = age_days % 365 // 30
days = age_days % 365 % 30

print(f"{years} years", f"{months} months", f"{days} days",sep = '\n')

s=input("enter a string")
upper_case=0
lower_case=0

for ch in s:
    if ch.isupper():
        upper_count+=1
    elif ch.islower():
        lower_count+=1

print("number of uppercase letter:",upper_count)
print("number of lowercase letter:",lower_count)
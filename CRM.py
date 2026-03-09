
# CRM System: 1.Add 2.Log 3.Sale 4.Report


cust = {} # {name: [email, stage, notes]}

def add():
    name = input("name: ")
    cust[name] = [input("email: "), "Lead", ""]
    print("added!")

def log():
    name = input("name: ")
    if name in cust:
        note = input("note: ")
        cust[name][2] += note + ", "
        print("saved!")
    else: print("not found!")

def sale():
    name = input("name: ")
    if name in cust:
        cust[name][1] = input("stage (Lead/Deal/Won): ")
        print("updated!")
    else: print("not found!")

def view():
    for name, d in cust.items():
        print(f"{name} | {d[0]} | Stage: {d[1]} | Notes: {d[2]}")

while True:
    print("\n1.Add 2.Log 3.Sale 4.View 5.Exit")
    c = input("choice: ")
    if c == '1': add()
    elif c == '2': log()
    elif c == '3': sale()
    elif c == '4': view()
    elif c == '5': break
    else: print("invalid!")
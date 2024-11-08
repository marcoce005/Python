def aid(salary, kids):
    if salary < 20000:
        return 2000 * kids
    elif salary < 30000 and kids >= 2:
        return 1500 * kids
    elif salary < 40000 and kids >= 3:
        return 1000 * kids
    return "Non possono usufruire di alcun sussidio."

salary = int(input("Inserire il reddito [intero]:\t"))
while salary != -1:
    kids = int(input("Inserire il numero di figli [intero]:\t"))
    print(f"Sussidio:\t{aid(salary, kids)}\n\n")
    
    salary = int(input("Inserire il reddito [intero]:\t"))
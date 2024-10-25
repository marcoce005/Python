married = input("Inserire lo stato civile [non coniugato / coniugato]:\t")
salary = float(input("Inserire il salario:\t"))

if married in ["non coniugato", "coniugato"] and salary >= 0:
    print("Tasse:\t", end="")
    if married == "non coniugato":
        if salary <= 8000:
            print(salary * 0.1)
        elif salary <= 32000:
            print(((salary - 8000) * 0.15) + 800)
        else:
            print(((salary - 32000) * 0.25) + 4400)
    else:
        if salary <= 16000:
            print(salary * 0.1)
        elif salary <= 64000:
            print(((salary - 16000) * 0.15) + 1600)
        else:
            print(((salary - 64000) * 0.25) + 8800)
else:
    print("Dati errati, riprovare")

def name_of_best_customer(sales, customers):
    return customers[sales.index(max(sales))]


sale = int(input("Inserire il prezzo pagato:\t"))
customer = input("Inserire il nomer del cliente:\t")

customers = []
sales = []

while sale != 0:
    customers.append(customer)
    sales.append(sale)
    
    sale = int(input("\n\nInserire il prezzo pagato:\t"))
    customer = input("Inserire il nomer del cliente:\t")


print(f"\n\nIl miglior acquirente è:\t{name_of_best_customer(sales, customers)}")
from csv import reader

file = open("./prova.csv", "r")

csv_read = reader(file)     # deafult delimiter is ','

file.close()

print(*csv_read)

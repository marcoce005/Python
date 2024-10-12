row = 0b01010

# print normal row '01010' if line is even else it print the xor with 0b11111 of the row
[print(str(bin(row).split('b')[1].zfill(5))) if i % 2 == 0 else print(str(bin(row ^ 0b11111)).split('b')[1].zfill(5)) for i in range(0, 5)]

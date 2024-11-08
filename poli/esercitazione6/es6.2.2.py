def digit_roman_2_dec(c):
    romans_digit = "IVXLCDM"

    index = romans_digit.index(c)
    return 10 ** (index // 2) * (1 if index % 2 == 0 else 5)


def roman_2_dec(s):
    i = tot = 0
    while i < len(s):
        actual_c = digit_roman_2_dec(s[i])
        next_c = digit_roman_2_dec(s[i + 1]) if i + 1 < len(s) else 0

        tot, i = (
            (tot + (next_c - actual_c), i + 2)
            if next_c > actual_c
            else (tot + actual_c, i + 1)
        )
    return tot


print(f"MCMLXXVIII = {roman_2_dec("MCMLXXVIII")}")

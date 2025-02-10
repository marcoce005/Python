def print_numbers(m, d):
    output = ""
    for i in range(5):          # iterate layer by layer
        for c in n:
            output += d[int(c)].split("\n")[1: 6][i] + " "
        output += "\n"
    return output


digits = [
    """
    ###
    # #
    # #
    # #
    ###
    """,
    """
    #  
    #  
    #  
    #  
    #  
    """,
    """
    ###
      #
    ###
    #  
    ###
    """,
    """
    ###
      #
    ###
      #
    ###
    """,
    """
    # #
    # #
    ###
      #
      #
    """,
    """
    ###
    #  
    ###
      #
    ###
    """,
    """
    ###
    #  
    ###
    # #
    ###
    """,
    """
    ###
      #
      #
      #
      #
    """,
    """
    ###
    # #
    ###
    # #
    ###
    """,
    """
    ###
    # #
    ###
      #
    ###
    """
]

n = input("Choose an integer number non-negative:\t")

if int(n) < 0:
    print("\nIncorrect input.")
    exit(0)

print(print_numbers(n, digits))
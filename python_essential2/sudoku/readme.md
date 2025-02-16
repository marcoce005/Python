# Sudoku
As you probably know, Sudoku is a number-placing puzzle played on a 9x9 board. The player has to fill the board in a very specific way:
 - each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
 - each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
 - each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table must contain all digits from 0 to 9.

If you need more details, you can find them [here](https://en.wikipedia.org/wiki/Sudoku).

Your task is to write a program which:
 - reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
 - outputs Yes if the Sudoku is valid, and No otherwise.

Test your code using the data we've provided.

## Test Data

Sample input:
```
295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672
```
Sample output:
```
Yes
```

<hr>

Sample input:
```
195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671
```
Sample output:
```
No
```
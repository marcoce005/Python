# Sorted character frequency histogram
The previous code needs to be improved. It's okay, but it has to be better.

Your task is to make some amendments, which generate the following results:
 - the output histogram will be sorted based on the characters' frequency (the bigger counter should be presented first)
 - the histogram should be sent to a file with the same name as the input one, but with the suffix '.hist' (it should be concatenated to the original name)

Assuming that the input file contains just one line filled with:

#### input.txt
```
cBabAa
```

## Expected output
```
a -> 3
b -> 2
c -> 1
```

**Tip**: Use a lambda to change the sort order.
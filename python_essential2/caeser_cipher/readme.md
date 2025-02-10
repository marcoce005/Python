# The Caesar Cipher

## Encrypting a message
We're going to show you four simple programs in order to present some aspects of string processing in Python. They are purposefully simple, but the lab problems will be significantly more complicated.

The first problem we want to show you is called the Caesar cipher – more details here: https://en.wikipedia.org/wiki/Caesar_cipher.

This cipher was (probably) invented and used by Gaius Julius Caesar and his troops during the Gallic Wars. The idea is rather simple – every letter of the message is replaced by its nearest consequent (A becomes B, B becomes C, and so on). The only exception is Z, which becomes A.

The program in the editor is a very simple (but working) implementation of the algorithm.

```python
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)
```

We've written it using the following assumptions:

it accepts Latin letters only (note: the Romans didn't use whitespaces or digits)
all letters of the message are in upper case (note: the Romans knew only capitals)

Let's trace the code:
 - line 02: ask the user to enter the open (unencrypted), one-line message;
 - line 03: prepare a string for an encrypted message (empty for now)
 - line 04: start the iteration through the message;
 - line 05: if the current character is not alphabetic...
 - line 06: ...ignore it;
 - line 07: convert the letter to upper-case (it's preferable to do it blindly, rather than check whether it's needed or not)
 - line 08: get the code of the letter and increment it by one;
 - line 09: if the resulting code has "left" the Latin alphabet (if it's greater than the Z code)...
 - line 10: ...change it to the A code;
 - line 11: append the received character to the end of the encrypted message;
 - line 13: print the cipher.


The code, fed with this message:

```
AVE CAESAR
```

outputs:

```
BWFDBFTBS
```

<hr>

## Decrypting a message
The reverse transformation should now be clear to you – let's just present you with the code as-is, without any explanations.

Look at the code in the editor. Check carefully if it works. Use the cryptogram from the previous program.

```python
cipher = input('Enter your cryptogram: ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)
```
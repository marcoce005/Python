# The Timer class
We need a class able to count seconds. Easy? Not as easy as you may think, as we're going to have some specific requirements.

Read them carefully as the class you're about write will be used to launch rockets carrying international missions to Mars. It's a great responsibility. We're counting on you!

Your class will be called ```Timer```. Its constructor accepts three arguments representing hours (a value from the range [0..23] – we will be using military time), minutes (from the range [0..59]) and seconds (from the range [0..59]).

Zero is the default value for all of the above parameters. There is no need to perform any validation checks.

The class itself should provide the following facilities:
 - objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the following form: "hh:mm:ss", with leading zeros added when any of the values is less than 10;
 - the class should be equipped with parameterless methods called ```next_second()``` and ```previous_second()```, incrementing the time stored inside the objects by +1/-1 second respectively.

Use the following hints:
 - all object properties should be private;
 - consider writing a separate function (not method!) to format the time string.

Complete the template we've provided in the editor. Run your code and check whether the output looks the same as ours.

## Expected output

```
23:59:59
00:00:00
23:59:59
```

Start from this code

```python
class Timer:
    def __init__( ??? ):
        #
        # Write code here
        #

    def __str__(self):
        #
        # Write code here
        #

    def next_second(self):
        #
        # Write code here
        #

    def prev_second(self):
        #
        # Write code here
        #


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
```
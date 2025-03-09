# The datetime and time modules
During this course, you learned about the ```strftime``` method, which requires knowledge of directives to create a format. It's now time to put these directives into practice.

By the way, you'll have the opportunity to practice working with documentation, because you'll have to find directives that you don't yet know.

**Here's your task:**
Write a program that creates a ```datetime``` object for ```November 4, 2020 , 14:53:00```. The object created should call the ```strftime``` method with the appropriate format to display the following result:

```
2020/11/04 14:53:00
20/November/04 14:53:00 PM
Wed, 2020 Nov 04
Wednesday, 2020 November 04
Weekday: 3
Day of the year: 309
Week number of the year: 44
```

**Note**: Each result line should be created by calling the strftime method with at least one directive in the format argument.
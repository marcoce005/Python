# Evaluating students' results
Prof. Jekyll conducts classes with students and regularly makes notes in a text file. Each line of the file contains three elements: the student's first name, the student's last name, and the number of points the student received during certain classes.

The elements are separated with white spaces. Each student may appear more than once inside Prof. Jekyll's file.

The file may look as follows:

#### input.txt
```
John     Smith    5
Anna     Boleyn   4.5
John     Smith    2
Anna     Boleyn   11
Andrew   Cox      1.5
```

Your task is to write a program which:
 - asks the user for Prof. Jekyll's file name;
 - reads the file contents and counts the sum of the received points for each student;
 - prints a simple (but sorted) report, just like this one:

```
Andrew   Cox      1.5
Anna     Boleyn   15.5
John     Smith    7.0
```

Notes:
 - your program must be fully protected against all possible failures: the file's non-existence, the file's emptiness, or any input data failures; encountering any data error should cause immediate program termination, and the error should be presented to the user;
 - implement and use your own exceptions hierarchy – we've presented it in the editor; the second exception should be raised when a wrong line is detected, and the third when the source file exists but is empty.

**Tip**: Use a dictionary to store the students' data.


Start from this code.

```python
class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    # Write your code here.


class FileEmpty(StudentsDataException):
    # Write your code here.
```
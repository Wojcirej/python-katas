# Guess my number

### Description
Your Goal is to create a function that takes two strings, a guess and a phone number.

Based on the guess, the function should display a portion of the phone number.

Order of the guess string should not matter, and should not have duplicates of the ten digitis 0-9. Guess will never be an empty string or contains any other charachters. The phone number will always bea ten digit number in the format ###-###-####.

The default number of 123-451-2345 should be included, but can be overwriten by a different number if supplied at the time of execution.

### Examples
```python
guess_my_number('052', '123-451-2345') #=> '#2#-#5#-2##5'
guess_my_number('142', '123-451-2345') #=> '12#-4#1-2#4#'
```

### Link to kata on codewars.com
https://www.codewars.com/kata/5654d2428be803670a000030/

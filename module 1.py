#Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
def even_or_odd(number):
    if (number % 2) == 0:
        return "Even"
    else:
        return"Odd"
    
#Convert a Number to a String
def number_to_string(num):
    return str(num)

#Return the number (count) of vowels in the given string. 
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.
def get_count(sentence):
    num_vowels = 0
    vowels = 'aeiou'
    for x in sentence:
        if x in vowels:
            num_vowels += 1
    return num_vowels
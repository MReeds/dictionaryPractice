"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

word_definitions["Door"] = "A hinged, sliding, or revolving barrier"
word_definitions["Rug"] = "A floor covering of thick woven material"
word_definitions["Kitchen"] = "A room or area where food is prepared and cooked"
word_definitions["Bed"] = "A piece of furniture for sleep or rest"

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions["House"] = "A building for human habitation"
word_definitions["Light Bulb"] = "A glass bulb inserted into a lamp or a socket in a ceiling"
word_definitions["Couch"] = "A long upholstered piece of furniture"

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
# x = word_definitions["House"]
# y = word_definitions["Kitchen"]
# print(x, y)
"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""
for (key, value) in word_definitions.items():
    print(f"The definition of {key} is {value}")
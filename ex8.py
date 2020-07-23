# Define formatter variable with four inputs
formatter = "{} {} {} {}"

# print formatter with 1, 2, 3, 4 as inputs
print(formatter.format(1,2,3,4))
# print formatter with one, two, three, four as inputs
print(formatter.format("one", "two", "three", "four"))
# print formatter with true, false, false, true as inputs
print(formatter.format(True, False, False, True))
# print formatter with formatter, formatter, formatter, formatter as inputs
print(formatter.format(formatter, formatter, formatter, formatter))
# print formatter with following text on as inputs
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

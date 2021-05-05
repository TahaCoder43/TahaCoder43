# A string is an immutable, ordered, and it is represented by text
# A string can be written in all these different ways and all have their own advantages
# like the single  quote  one is easy
# double quote help if you want to throw in a single quote
# triple quote are used for multiple lines
#
var1 = 'Hello World'
var2 = ",I got pies from the mar's planet"
var3 = """
"Isn't cool" titan moons habitants said
"""
print(var1 + " " + var2 + "" + var3)

# if you don't want multiple lines oyu can also do this
var4 = """\
This \
is
"""
print(var4)
# index fetching works the same as lists but you can't change it
# This is a nice way to reverse
reverse_mode = "This is sparta"
print(reverse_mode[::-1])
# important:This function may not be used but is important it removes white space
extra_dude = "         lol          "
print(extra_dude.strip())
extra_dude_2 = "_____________lol__________"
print(extra_dude_2.strip("_"))
# different chars can be used
#startswith function: It proves the starting value with boolean expression

time_do_you_get_the_joke_scientist = "Hello time"
print(time_do_you_get_the_joke_scientist.startswith("H"))
# this function also have its opposite called endswith
# and there is  this split and join method,must know

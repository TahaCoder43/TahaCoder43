is_male= True
is_tall= True
is_adult = False
if is_male and is_tall and is_adult:
    print("your a tall men")
elif is_male and not(is_tall) and not(is_adult):
    print("your a short boy")
elif is_male and is_tall and not(is_adult):
    print("your a tall boy")
elif is_male and not(is_tall) and is_adult:
    print("your a short men")
elif not(is_male) and is_tall and is_adult:
    print("your a tall lady")
elif not(is_male) and not(is_tall) and is_adult:
    print("your a short lady")
elif not(is_male) and is_tall and not(is_adult):
    print("your a tall girl")
else:
    print("your a short girl")

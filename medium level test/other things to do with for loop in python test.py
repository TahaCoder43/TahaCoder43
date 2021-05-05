for numbers in range(21):
    if int(numbers)!=2 or 4 or 6 or 8 or 10 or 12 or 14 or 16 or 18 or 20:
        print(str(numbers) + " This is an even number")
    else:
        print(str(numbers) + " This is an odd number")
print("down below is another test" + "\n" * 10)

sentence=["I","used","the","stones","to","destroy","the","stones"]
for index in range(len(sentence)):
    print(sentence[index])
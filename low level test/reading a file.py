paragraph_3 = open("test_subject", "w")
paragraph_3.write("This is sparta")
paragraph_3.close()


paragraph=open("test_subject", "r")
print(paragraph.readline())
paragraph.close()


paragraph_2=open("test_subject", "r")
print(paragraph_2.readlines()[2])
paragraph_2.close()



text = open("test_subject", "w")

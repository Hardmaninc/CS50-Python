question = (input("What is the Answer to the Great of Life, the Universe, and Everything?" )).lower().strip(" ")

if question == "42":
    print("Yes")
elif question == "forty two":
    print("Yes")
elif question== "42.0":
    print("Yes")
elif question == "forty-two":
    print("Yes")
else:
    print("No")
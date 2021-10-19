import magic
for i in range(1,999999):
    if "WRONG!!!!" not in magic.check_box(i) :
        print(i)
        print(magic.check_box(i))
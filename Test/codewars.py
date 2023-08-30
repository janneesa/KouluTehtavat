def same_case(a, b):
    if a.isalpha() == False or b.isalpha() == False:
        return -1
    elif (a.isupper() and b.isupper()) or (a.islower() and b.islower()):
        return 1
    elif a.isalpha() and b.isalpha():
        return 0
    pass
# lambda expression practicee
def even(a):
    if a%2 ==0:
        return True
    else:
        return False
# or
def is_even(a):
    return a%2==0 
print(is_even(4))


iseven= lambda a: a%2==0
print(iseven(4))


def last_char(s):
    return s[-1]
print(last_char('isha'))


last_char1= lambda s: s[-1]
print(last_char1('verma'))


# if else
def func(s):
    if len(s)>5:
        return True
    return False
print(func("ish"))

funct=lambda s: True if len(s)>5 else False
print(funct("ishaverma"))


# without if else
def func(s):
    return len(s)>5
print(func("ish"))

a=lambda s: len(s)>5
print(a("ishaverma"))
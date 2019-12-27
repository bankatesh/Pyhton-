in_val=input("Enter the value to find it's factorial")
val = int(in_val)
print(type(val))
def func(val):
    if val == 1:
        return 1
    else:
        return (val*func(val-1))

result = func(val)
print(result)

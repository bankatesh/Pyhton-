in_val=input("Enter the number of elements you want in fibonacci series ")
val = int(in_val)
def func(val):
    if val == 0:
        return 0
    elif val == 1:
        return 1
    else:
        return func(val-2)+func(val-1)
res = func(val)
print('The '+ in_val +' digit of series is '+str(res) )

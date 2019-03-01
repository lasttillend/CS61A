def invert(x):
    y = 1 / x
    print("Never printed if x is 0")
    return y

# invert(0)

def invert_safe(x):
    try:
        return invert(x)
    except ZeroDivisionError as e:
        print("handled", e)
        return 0

# invert_safe(2)
invert_safe(0)


# invert_safe(1/0)





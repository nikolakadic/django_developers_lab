try:
    a = 0/0
    print(55)
except ZeroDivisionError as zero_division_error:
    a = 0
    print(zero_division_error)
finally:
    print('Ishendlovao sam ovo',a )
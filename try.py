try:
    x = 10/0

except ZeroDivisionError as e:
    print("Error:",e)
finally:
    print("cleanup executed")

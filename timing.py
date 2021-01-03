from timeit import timeit


code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""


print("Time: ", timeit(code1, number=1000000))  # 0.4 seconds

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age


xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
 """

print("Time: ", timeit(code2, number=1000000))  # 0.4 seconds

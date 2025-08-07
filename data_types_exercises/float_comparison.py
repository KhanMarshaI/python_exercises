# Implement def almost_equal(a, b, rel_tol=1e-9, abs_tol=0.0) reproducing math.isclose without using the module.

def almost_equal(a, b, rel_tol=1e-09, abs_tol=0.0):
    result = abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)
    return result

float1 = float(input("Enter first float: "))
float2 = float(input("Enter second float: "))

try: 
    relative_tolerance = float(input("Enter max allowed tolerance(upto ? decimal digits): "))
except ValueError:
    relative_tolerance = 1e-09

while(relative_tolerance < 0 or relative_tolerance >= 1.0):
    print("Relative tolerance may not be negative or greater than 1.0.")
    relative_tolerance = float(input("Enter relative tolerance: "))

try:
    absolute_tolerance = float(input("Enter absolute tolerance: "))
except:
    absolute_tolerance = 0.0

while(absolute_tolerance < 0.0):
    print("Absolute tolerance may only be positive.")
    absolute_tolerance = float(input("Enter absolute tolerance: "))

print("Almost Equal?", almost_equal(float1,float2, relative_tolerance, absolute_tolerance))

# Positional-only Division
# Define def div(a, b, /, precision=2) that forbids keyword use of a and b but allows precision=4.

from decimal import Decimal, localcontext

def div(a,b, /, precision=2):
    with localcontext() as ctx:
        ctx.prec = precision
        result = Decimal(a) / Decimal(b)
        return result


print(div(22,7, precision=15))
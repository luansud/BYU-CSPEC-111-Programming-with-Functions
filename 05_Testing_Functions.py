import math
# Example 4

    # The variables e and f can be any floating-
    # point numbers from any calculation.
e = 7.135
f = 7.128
if abs(e - f) < 0.01:
    print(f"{e} and {f} are close enough so")
    print("we'll consider them to be equal.")
else:
    print(f"{e} and {f} are not close and")
    print("therefor not equal.")
    
    
def test_sqrt():
    assert math.sqrt(5) == approx(2.24, rel=0.01)
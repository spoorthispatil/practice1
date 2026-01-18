import sys
import math
def hcf_lcm(a,b):
    hcf=math.gcd(a,b)
    lcm=a*b//hcf
    return hcf,lcm
if __name__=="__main__":
    if len(sys.argv)==3:
        script_name=sys.argv[0]
        a=int(sys.argv[1])
        b=int(sys.argv[2])
    else:
        a,b=2,5
    print(f"The HCF and LCM of {a} and {b} are: {hcf_lcm(a,b)}")


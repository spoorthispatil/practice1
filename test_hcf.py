from hcf import hcf_lcm
def test1():
    assert hcf_lcm(5,10)==(5,10)
def test2():
    assert hcf_lcm(3,11)==(1,33)
def test3():
    assert hcf_lcm(6,9)==(3,18)
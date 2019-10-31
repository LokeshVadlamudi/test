#test file
import pytest
from RiceBowl import RiceBowl


#can create instance of riceBowl class:
# def test_canCreateInstance():
#     rB = RiceBowl()

@pytest.fixture()
def riceBowl():
    riceBowl = RiceBowl()
    return riceBowl

#failing test case
@pytest.mark.skip
def test_chooseRiceType(riceBowl):
    riceBowl.addRiceType("w")
    assert riceBowl.riceType == "brown"

#pass test case
@pytest.mark.skip
def test_chooseRiceType(riceBowl):
    riceBowl.addRiceType("b")
    assert riceBowl.riceType == "brown"

def test_addMixVeg(riceBowl):
    riceBowl.addMixVeg("y")
    assert riceBowl.mixVeg == "yes"

def test_addMixVeg(riceBowl):
    riceBowl.addMixVeg("n")
    assert riceBowl.mixVeg == "skip"

def test_addMeatType(riceBowl):
    riceBowl.addMeatType("c")
    assert riceBowl.mixVeg == "chicken"

def test_addMeatType(riceBowl):
    riceBowl.addMeatType("b")
    assert riceBowl.mixVeg == "beef"











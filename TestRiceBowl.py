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

#failing test case - passing white rice type and expecting brown rice type
@pytest.mark.skip
def test_chooseRiceType(riceBowl):
    riceBowl.addRiceType("w")
    assert riceBowl.riceType == "brown"

#pass test case - passing brown rice type and expecting white rice type
@pytest.mark.skip
def test_chooseRiceType(riceBowl):
    riceBowl.addRiceType("b")
    assert riceBowl.riceType == "brown"

#pass test case - passing yes to add mix veg and expecting the output as yes
def test_addMixVeg(riceBowl):
    riceBowl.addMixVeg("y")
    assert riceBowl.mixVeg == "yes"

#pass test case - passing no to add mix veg and expecting the output as skip
def test_addMixVeg(riceBowl):
    riceBowl.addMixVeg("n")
    assert riceBowl.mixVeg == "skip"

#pass test case - passing c to add chicken and expecting the output as chicken
def test_addMeatType(riceBowl):
    riceBowl.addMeatType("c")
    assert riceBowl.mixVeg == "chicken"

#pass test case - passing b to add beef and expecting the output as beef
def test_addMeatType(riceBowl):
    riceBowl.addMeatType("b")
    assert riceBowl.mixVeg == "beef"











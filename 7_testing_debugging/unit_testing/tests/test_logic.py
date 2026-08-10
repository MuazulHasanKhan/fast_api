import pytest

from app.logic import is_available_for_loan

def test_is_available_for_loan():
    assert is_available_for_loan(60000, 25, "employed") == True


def test_underage_user():
    assert is_available_for_loan(60000, 20, "employed") == False

def test_low_income_user():
    assert is_available_for_loan(40000, 25, "employed") == False

def test_unemployed_user():
    assert is_available_for_loan(60000, 25, "unemployed") == False

def test_boundary_conditions():
    assert is_available_for_loan(50000, 21, "employed") == True
    
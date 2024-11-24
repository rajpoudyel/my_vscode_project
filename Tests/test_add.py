import os
from os import listdir
import sys

#sys.path.insert(0,'../../My First VC Code Project/src/calculator/') 
#sys.path.insert(0,'../../My First VC Code Project/src/')
from my_vscode_project.src.calculator.add import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
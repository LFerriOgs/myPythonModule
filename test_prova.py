# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 10:16:30 2024

@author: lferri
"""
from dfModifier import quadrato

def test_quadrato():
    """Test our ``square()`` function."""
    assert quadrato(2) == 4
    assert quadrato(0) == 0
    assert quadrato(-1) == -1
    
    
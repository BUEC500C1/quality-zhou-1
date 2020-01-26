# test for roman 2 Intgeer converter

import pytest
import Arabic2Roman

def testConverter():
  arabic = [1, 10, 101, 1999]
  roman = ["I", "X", "CI", "MCMXCIX"]
  
  for a,r in zip(arabic,roman):
	  assert Arabic2Roman.2Roman(a) == r

    
# if __name__ == "__main__":
# 	testConverter() 

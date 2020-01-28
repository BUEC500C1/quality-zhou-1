# test for roman 2 Intgeer converter

import pytest
import ArabicToRoman

def test_Converter():
  arabic = [1, 10, 101, 1999, -10, 2865, 901, -1]
  roman = ["I", "X", "CI", "MCMXCIX", "-1", "MMDCCCLXV", "CMI", "-1"]
  
  for a,r in zip(arabic,roman):
	  assert ArabicToRoman.toRoman(a) == r

    
# if __name__ == "__main__":
# 	test_Converter() 

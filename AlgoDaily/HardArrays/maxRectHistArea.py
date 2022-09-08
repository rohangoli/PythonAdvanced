## Max Rectangle in a Histogram

def maxRectInHist(histArr):
    # fill in
    maxArea = 0
    i=0
    while i<len(histArr)-1:
      j=i+1
      while j<len(histArr):
        maxArea = max(maxArea,min(histArr[i],histArr[j])*(j-1))
        j+=1
      i+=1
    return maxArea


import unittest


class Test(unittest.TestCase):
    def test_1(self):
        assert maxRectInHist([3, 1, 4, 2, 2, 1]) == 6
        print("PASSED: assert maxRectInHist([3, 1, 4, 2, 2, 1]) == 6")

    def test_2(self):
        assert maxRectInHist([]) == 0
        print("PASSED: assert maxRectInHist([]) == 0")

    def test_3(self):
        assert maxRectInHist([1, 2, 3, 4]) == 6
        print("PASSED: assert maxRectInHist([1, 2, 3, 4]) == 6")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 3/3 tests passed!")



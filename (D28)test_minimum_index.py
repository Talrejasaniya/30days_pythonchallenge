# NOTE:
# This file only includes the test data classes used for testing the `minimum_index()` function.
# The actual function and test logic were already provided by HackerRank.
# I acted as a tester to ensure the function behaves correctly under different input scenarios.
def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx
class TestDataEmptyArray():
    @staticmethod
    def get_array():
        return []
        

class TestDataUniqueValues():
    @staticmethod
    def get_array():
        return [5,3,8,10]
    
    @staticmethod    
    def get_expected_result():
        return 1
      
class TestDataExactlyTwoDifferentMinimums():
    @staticmethod
    def get_array():
        return [4,5,2,7,2,5]
    
    @staticmethod
    def get_expected_result():
        return 2

def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False


def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print("OK")


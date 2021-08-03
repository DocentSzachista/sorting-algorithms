from src.main import Sorts
import pytest
#worth noting after using parametrize in test function it cant be reused in another 
# After creating class and putting test methods in there parametrize works fine 
# happy path - sorted asc 
@pytest.mark.parametrize("test_input,expected", [
    ([1,4,2,3],[1,2,3,4]),
    ([4,3,5,1],[1,3,4,5]),
    ([], []),
    (None, None)
    ])
# items sorted asc
class TestAsc:
    def test_bubble_sort(self, test_input, expected):
        Sorts.bubble_sort(test_input)
        assert test_input == expected

    def test_insert_sort(self, test_input, expected):
        Sorts.insert_sort(test_input)
        assert test_input == expected
    
    def test_quick_sort(self, test_input, expected):
        try:
            Sorts.quick_sort(test_input, 0, len(test_input)-1)
            assert test_input == expected
        except TypeError:
            print("Your input array can't be a null value")
    #def test_merge_sort(self, test_input, expected):
    #    assert True
    
    def test_counting_sort(self, test_input, expected):
        Sorts.counting_sort(test_input)
        assert test_input == expected
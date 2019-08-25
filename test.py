import list_reporter

def test_one():
    tc = [['g', 'gh', 'ghj', 'g'], ['j', 'ju', 'gh', 'gk', 'gn']]
    assert list_reporter.analyse_list(tc) == '''Strings appearing in multiple lists: 'gh'
Number of unique strings: 7
Total number of strings processed: 9'''

def test_two():
    tc = [['g', 'bh'], ['j', 'g', 'bh']]
    assert list_reporter.analyse_list(tc) == '''Strings appearing in multiple lists: 'g', 'bh'
Number of unique strings: 3
Total number of strings processed: 5'''

def test_three():
    tc = [['abc', 'def', 'zyx', 'bh'], ['abc', 'abc', 'bh', 'bh', 'the'], ['the', 'abc']]
    assert list_reporter.analyse_list(tc) == '''Strings appearing in multiple lists: 'abc', 'bh', 'the'
Number of unique strings: 5
Total number of strings processed: 11'''

def test_four():
    tc = [['abc', 'def', 'zyx', 'bh']]
    assert list_reporter.analyse_list(tc) == '''Strings appearing in multiple lists: 
Number of unique strings: 4
Total number of strings processed: 4'''

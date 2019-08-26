import list_reporter

def test_one_list():
    tc = [['abc', 'def', 'zyx', 'bh']]
    assert list_reporter.analyse_list(tc) == '''Strings appearing in multiple lists: 
Number of unique strings: 4
Total number of strings processed: 4'''

def test_two_lists_one_match():
    tc = [['g', 'gh', 'ghj', 'g'], ['j', 'ju', 'gh', 'gk', 'gn']]
    assert list_reporter.analyse_list(tc) == '''Strings appearing in multiple lists: 'gh'
Number of unique strings: 7
Total number of strings processed: 9'''

def test_three_lists_multiple_matches():
    tc = [['abc', 'def', 'zyx', 'bh'], ['abc', 'abc', 'bh', 'bh', 'the'], ['the', 'abc']]
    assert list_reporter.analyse_list(tc) == '''Strings appearing in multiple lists: 'abc', 'bh', 'the'
Number of unique strings: 5
Total number of strings processed: 11'''

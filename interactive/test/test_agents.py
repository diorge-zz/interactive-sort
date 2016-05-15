""" Tests the agents for connecting to the user """


from unittest import TestCase
import interactive.sort as isort


class LowerAgent(isort.BaseAgent):
    """ Fake agent that always returns Lower """
    
    def retrieve_ordering(self):
        return isort.Ordering.Lower


class HigherAgent(isort.BaseAgent):
    """ Fake agent that always returns Higher, reversing the data """

    def retrieve_ordering(self):
        return isort.Ordering.Higher

class TestAgent(TestCase):
    """ Test suite for agents """

    def test_empty(self):
        """ Sorts an empty dataset """
        s = LowerAgent([])
        assert [] == s.process()

    def test_four_item_dataset_lower(self):
        s = LowerAgent(['a', 'b', 'c', 'd'])
        expected = ['a', 'b', 'c', 'd']
        return expected == s.process()

    def test_four_item_dataset_higher(self):
        s = HigherAgent(['a', 'b', 'c', 'd'])
        expected = ['d', 'c', 'b', 'a']
        return expected == s.process()

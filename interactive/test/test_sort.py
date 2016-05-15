""" Tests for the Sort class """

from unittest import TestCase
import interactive.sort as isort


class TestSort(TestCase):
    """ Test suite for the Sort class """

    dataset = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    def test_complete_info(self):
        """ Basic API test for sort operation """
        s = isort.Sort(self.dataset)
        expected = ['a', 'b', 'd', 'c', 'h', 'g', 'e', 'f']
        s.table.order('a', 'b', isort.Ordering.Lower)
        s.table.order('c', 'd', isort.Ordering.Higher)
        s.table.order('e', 'f', isort.Ordering.Lower)
        s.table.order('h', 'g', isort.Ordering.Lower)
        s.table.order('b', 'd', isort.Ordering.Lower)
        s.table.order('c', 'h', isort.Ordering.Lower)
        s.table.order('g', 'e', isort.Ordering.Lower)
        s.table.order('c', 'h', isort.Ordering.Lower)
        s.sort()
        assert s.done
        assert expected == s.result

    def test_empty_sort(self):
        """ Sorts an empty dataset """
        s = isort.Sort([])
        s.sort()
        assert s.done
        assert [] == s.result

    def test_not_complete_info(self):
        """ Tries to sort without enough information """
        s = isort.Sort(self.dataset)
        s.sort()
        assert not s.done
        assert s.question == ('a', 'b')

    def test_sort_null_dataset(self):
        """ Tries to sort a null dataset """
        with self.assertRaises(TypeError) as ctx:
            s = isort.Sort(None)

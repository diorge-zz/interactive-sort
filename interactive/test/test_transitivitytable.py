""" Tests for the Transitivity Table class """


from unittest import TestCase
import interactive.sort as isort


class TestTransitivityTable(TestCase):
    """ Test suite for the TransitivityTable class """

    dataset = ['a', 'b', 'c', 'd']

    def test_construction_dimension(self):
        """ Tests basic construction and dimension """
        table = isort.TransitivityTable(self.dataset)
        assert len(self.dataset) == table.dimension

    def test_empty_state(self):
        """ Tests check for ordering when table is empty """
        table = isort.TransitivityTable(self.dataset)
        assert not table.isHigher('a', 'b')
        assert not table.isHigher('b', 'a')
        assert isort.Ordering.Unknown == table.status('a', 'b')

    def test_set_and_test(self):
        """ Tests for setting an ordering and immediately checking it """
        table = isort.TransitivityTable(self.dataset)
        table.order('a', 'b', isort.Ordering.Higher)
        assert table.isHigher('a', 'b')

    def test_set_and_reflectivity(self):
        """ Tests for setting an ordering and checking its reflection """
        table = isort.TransitivityTable(self.dataset)
        table.order('a', 'b', isort.Ordering.Lower)
        assert table.isHigher('b', 'a')

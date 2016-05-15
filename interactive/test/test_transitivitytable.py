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
        assert not table.ishigher('a', 'b')
        assert not table.ishigher('b', 'a')
        assert isort.Ordering.Unknown == table.orderof('a', 'b')

    def test_set_and_test(self):
        """ Tests for setting an ordering and immediately checking it """
        table = isort.TransitivityTable(self.dataset)
        table.order('a', 'b', isort.Ordering.Higher)
        assert table.ishigher('a', 'b')

    def test_set_and_reflectivity(self):
        """ Tests for setting an ordering and checking its reflection """
        table = isort.TransitivityTable(self.dataset)
        table.order('a', 'b', isort.Ordering.Lower)
        assert table.ishigher('b', 'a')

    def test_transitivity(self):
        """ Tests the transitivity check """
        table = isort.TransitivityTable(self.dataset)
        table.order('a', 'b', isort.Ordering.Lower)
        table.order('b', 'c', isort.Ordering.Lower)
        assert table.ishigher('c', 'a')

    def test_construction_invalid_iterator(self):
        """ Tests the construction when passing an invalid iterator """
        with self.assertRaises(TypeError) as e:
            table = isort.TransitivityTable(10)

    def test_construction_empty_iterator(self):
        """ Tests the construction when passing an empty iterator """
        table = isort.TransitivityTable([])
        assert 0 == table.dimension

    def test_orderof_not_existant_origin(self):
        """ Tests the orderof method when origin is not in the set """
        table = isort.TransitivityTable(self.dataset)
        with self.assertRaises(KeyError) as e:
            s = table.orderof('z', 'a')

    def test_orderof_not_existant_target(self):
        """ Tests the orderof method when target is not in the set """
        table = isort.TransitivityTable(self.dataset)
        with self.assertRaises(KeyError) as e:
            s = table.orderof('a', 'z')

    def test_order_not_existant_origin(self):
        """ Tests the order method when giving an invalid origin """
        table = isort.TransitivityTable(self.dataset)
        with self.assertRaises(ValueError) as e:
            table.order('z', 'a', isort.Ordering.Higher)

    def test_order_not_existant_target(self):
        """ Tests the order method when giving an invalid target """
        table = isort.TransitivityTable(self.dataset)
        with self.assertRaises(ValueError) as e:
            table.order('a', 5, isort.Ordering.Unknown)

    def test_order_invalid_value(self):
        """ Tests the order method when value is not an Ordering """
        table = isort.TransitivityTable(self.dataset)
        with self.assertRaises(TypeError) as e:
            table.order('a', 'b', 5)

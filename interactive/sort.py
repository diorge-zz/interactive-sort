"""
Interactive Sort
================
Sorts a collection of objects without native ordering, by asking someone
the order of some elements and applying transitivity to find out the total
ordering for the set.
"""


from enum import Enum


class Ordering(Enum):
    Unknown = 0
    Lower = 1
    Higher = 2

    def opposite(self):
        """ Returns the opposite ordering. >.op(<), <.op(>), ?.op(?) """
        return {Ordering.Unknown: Ordering.Unknown,
                Ordering.Lower: Ordering.Higher,
                Ordering.Higher: Ordering.Lower}[self]


class TransitivityTable(object):
    """
    Transitivity table stores the order between every member of a set.
    It can be operated to fill vacant slots according to the transivity rule.
    """

    def __init__(self, data):
        """ Creates a new empty transitivity table using elements from
        a supplied dataset """
        self.data = {(x, y): Ordering.Unknown
                     for x in data for y in data
                     if x != y}
        self._datadim = len(data)
        self._dataset = tuple(data)
        self._elements = frozenset(data)

    def orderof(self, origin, target):
        """ Return the ordering between origin and target """
        return self.data[(origin, target)]

    def ishigher(self, origin, target):
        """ Returns if origin is higher than target """
        return self.orderof(origin, target) == Ordering.Higher

    def islower(self, origin, target):
        """ Returns if origin is lower than target """
        return self.orderof(origin, target) == Ordering.Lower

    def order(self, origin, target, value):
        """ The ordering between origin and target becomes value """
        if not isinstance(value, Ordering):
            raise TypeError('Only Ordering is supported')
        if origin not in self._elements:
            raise ValueError('origin is not in the dataset')
        self.data[(origin, target)] = value
        self.data[(target, origin)] = value.opposite()
        self.transitivity_set(origin)
        self.transitivity_set(target)

    def transitivity_set(self, pivot):
        """ Uses the pivot to provide transitivity rules """
        lowers = [x for x in self._dataset if x != pivot and self.islower(x, pivot)]
        highers = [x for x in self._dataset if x != pivot and self.ishigher(x, pivot)]
        for l in lowers:
            for h in highers:
                self.order(l, h, Ordering.Lower)

    dimension = property(fget=lambda self: self._datadim)

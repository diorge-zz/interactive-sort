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

    def status(self, origin, target):
        """ Return the ordering between origin and target """
        return self.data[(origin, target)]

    def isHigher(self, origin, target):
        """ Returns if origin is higher than target """
        return self.status(origin, target) == Ordering.Higher

    def order(self, origin, target, value):
        """ The ordering between origin and target becomes value """
        self.data[(origin, target)] = value
        self.data[(target, origin)] = value.opposite()

    dimension = property(fget=lambda self: self._datadim)

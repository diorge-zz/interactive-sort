# interactive-sort
Interactive merge sort with transitivity relations

### Sorting naturally unorderable data sets
Produce a fully-ordered list in a naturally unorderable domain.
Using MergeSort with a table containing the relationships
and applying the transitivity (a > b and b > c => a > c)
and reflexive (a > b => b < a) rules, the algorithm tries
to minimize the amount of questions asked to the agent (user).

This allows to (fully) sort a collection using personal preference,
by comparing only some elements in a "do your prefer X or Y?" manner.

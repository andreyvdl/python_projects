from push_swap import PushSwap

'''
1. Group the elements of X into _n/2_ pairs of elements, arbitrarily,
leaving one element unpaired if there is an odd number of elements.
2. Perform [n/2] comparisons, one per pair, to determine the larger of the
two elements in each pair.
3. Recursively sort the _n/2_ larger elements from each pair, creating a
sorted sequence S of _n/2_ of the input elements, in ascending order.
4. Insert at the start of S the element that was paired with the first and
smallest element of S.
5. Insert the remaining ^n/2^-1 elements of X\\S into one at a time, with a
specially chosen insertion ordering described below. Use binary search in
subsequences of S to determine the position at which each element should
be inserted.
'''


def merge_insertion_sort(ps: PushSwap):
    pairs = mount_pairs(ps)
    pairs = compare_pairs(pairs)


def mount_pairs(ps: PushSwap):
    pairs = list()
    if len(ps.stack_a) & 1 == 0:
        for a, b in ps.stack_a:
            pairs.append( [a, b] )

    else:
        for i in range(0, len(ps.stack_a) - 1, 2):
            pairs.append( [ ps.stack_a[i], ps.stack_a[i + 1] ] )

        pairs.append( [ps.stack_a[-1], ] )

    return pairs

def compare_pairs(pairs: list):
    for i in range( len(pairs) ):
        pairs[i] = sorted(pairs[i])

    return pairs

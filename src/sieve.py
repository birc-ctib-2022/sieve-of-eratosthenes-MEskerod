"""Computing primes."""


from os import remove


def sieve(n: int) -> list[int]:
    """
    Compute all the primes up to (and possibly including) `n`.

    `n` must be positive.

    >>> sieve(15)
    [2, 3, 5, 7, 11, 13]

    """
    assert n > 0
    candidates = list(range(2, n + 1))
    primes = []

    # FIXME: fill out this bit
    while len(candidates)>0:
        prime  =candidates[0]
        del candidates[0]
        not_deleted = []
        for i in candidates: 
            if  i % prime != 0: 
                not_deleted.append(i)
        primes.append(prime)
        candidates = not_deleted
    return primes

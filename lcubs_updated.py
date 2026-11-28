import argparse
from functools import lru_cache


def commonBlock(A, B, C):
    """Return one longest common subsequence of A, B, and C.

        Input: 
            A, B, C: strings of length n, m, and p
        Output:
            A string of length k, where k is the length of the longest common subsequence of A, B, and C.
            If there are multiple longest common subsequences, return any one of them.
            If there is no common subsequence, return the empty string.
    """

    @lru_cache(maxsize=None)
    def length(i, j, k):
        """Return the LCS length of the prefixes A[:i], B[:j], C[:k]."""
        if min(i, j, k) == 0:
            return 0

        if A[i - 1] == B[j - 1] == C[k - 1]:
            return 1 + length(i - 1, j - 1, k - 1)

        return max(
            length(i - 1, j, k),
            length(i, j - 1, k),
            length(i, j, k - 1),
        )

    # Trace back from the full prefixes to recover the block's characters.
    i, j, k = len(A), len(B), len(C)
    block = []

    while min(i, j, k) > 0:
        if A[i - 1] == B[j - 1] == C[k - 1]:
            block.append(A[i - 1])
            i, j, k = i - 1, j - 1, k - 1
        elif length(i - 1, j, k) == length(i, j, k):
            i -= 1
        elif length(i, j - 1, k) == length(i, j, k):
            j -= 1
        else:
            k -= 1

    length.cache_clear()
    return "".join(reversed(block))


def longestCubicSubsequence(sequence):
    """Return a longest subsequence of the form X + X + X.

        Input:
            sequence: a string
        Output:
            Returns X + X + X, where X is a longest repeated block. The returned string has length 3 * len(X).
    """
    best = ""

    for a in range(1, len(sequence) - 1):
        for b in range(a + 1, len(sequence)):
            block = commonBlock(sequence[:a], sequence[a:b], sequence[b:])
            if len(block) > len(best):
                best = block

    return best * 3


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("sequence", help="The input string")
    args = parser.parse_args()
    print(longestCubicSubsequence(args.sequence))
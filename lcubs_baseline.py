import argparse
from itertools import combinations


def longestCubicSubsequence(S):
    """
    Return a longest subsequence of the form X + X + X in S using exhaustive search.

    Input:
        S: a string of length n

    Output:
        A string of length 3 * m, where m is the length of the longest subsequence X such that X + X + X is a subsequence of S.
        If there are multiple longest subsequences, return any one of them.
        If there is no such subsequence, return the empty string.
    """
    n = len(S)
   
    # Three copies of X must fit in n characters.
    for blockLength in range(n // 3, 0, -1):
        candidateLength = 3 * blockLength

        # Choose positions in increasing order to preserve subsequence order.
        for positions in combinations(range(n), candidateLength):
            candidate = "".join(S[i] for i in positions)

            firstBlock = candidate[:blockLength]
            secondBlock = candidate[blockLength:2 * blockLength]
            thirdBlock = candidate[2 * blockLength:]

            if firstBlock == secondBlock == thirdBlock:
                return candidate

    return ""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Find a longest cubic subsequence using exhaustive search."
    )
    parser.add_argument("sequence", help="The input string S")
    args = parser.parse_args()

    print(longestCubicSubsequence(args.sequence))
import argparse
from itertools import combinations


def longest_cubic_subsequence(S):
    """Return a longest subsequence of S of the form X + X + X."""
    n = len(S)

    # Three copies of X must fit in n characters.
    for block_length in range(n // 3, 0, -1):
        candidate_length = 3 * block_length

        # Choose positions in increasing order to preserve subsequence order.
        for positions in combinations(range(n), candidate_length):
            candidate = "".join(S[i] for i in positions)

            first = candidate[:block_length]
            second = candidate[block_length:2 * block_length]
            third = candidate[2 * block_length:]

            if first == second == third:
                return candidate

    return ""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Find a longest cubic subsequence using exhaustive search."
    )
    parser.add_argument("sequence", help="The input string S")
    args = parser.parse_args()

    print(longest_cubic_subsequence(args.sequence))
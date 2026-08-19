class Solution:

    def encode(self, strs: List[str]) -> str:
        # Create an empty string
        encoded = ""

        # Take every string one by one
        for s in strs:

            # Add: length + # + actual string
            encoded += str(len(s)) + "#" + s

        # Return the encoded string
        return encoded

    def decode(self, s: str) -> List[str]:
        # Empty list to store decoded strings
        res = []

        # Starting position
        i = 0

        # Continue until we reach the end
        while i < len(s):

            # j starts where i starts
            j = i

            # Move j until we find #
            while s[j] != "#":
                j += 1

            # Get the number before #
            length = int(s[i:j])

            # Take exactly 'length' characters after #
            word = s[j + 1 : j + 1 + length]

            # Add word to result
            res.append(word)

            # Move i to the next encoded string
            i = j + 1 + length

        # Return the decoded list
        return res
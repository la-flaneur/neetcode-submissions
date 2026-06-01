class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for w in strs:
            encoded = encoded + w + ";p"
        print("Encoded: ", encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = s.split(";p")
        decoded.pop()
        return decoded
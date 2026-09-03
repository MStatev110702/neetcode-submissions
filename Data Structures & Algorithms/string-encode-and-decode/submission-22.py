class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += f"{len(s)}#{s}"

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        length = ""
        i = 0
        while i < len(s):
            print(i)
            if s[i] == "#":
                start = i + 1
                end = start + int(length)
                result.append(s[start:end])
                length = ""
                i = end
            elif s[i].isnumeric():
                length += s[i]
                i += 1
        return result
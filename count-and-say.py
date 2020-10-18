class Solution:
    def countAndSay(self, n: int) -> str:
        x = "1"
        for _ in range(n - 1):
            x = self._nextSequence(x)
        return x

    def _nextSequence(self, string: str) -> str:
        result = []
        curr = string[0]
        count = 0
        for char in string:
            if char == curr:
                count += 1
            else:
                result.append(str(count) + curr)
                curr = char
                count = 1
        result.append(str(count) + curr)
        return "".join(result)

class Solution:
    def removeDuplicates(self, s: str) -> str:
        char = []
        for item in s:
            dup = False
            while char and char[-1]==item:
                dup = True
                char.pop()
            if not dup:
                char.append(item)


        return "".join(char)
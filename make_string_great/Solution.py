class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for c in s:
            poped = ""
            if stack and abs(ord(stack[-1]) - ord(c)) == 32: #
                poped = stack.pop()

            if not poped:
                stack.append(c)


        return "".join(stack)


def main():
       n = Solution()
       sl = n.makeGood( "abBAcC")
       print(sl)

if __name__ == "__main__":
        main()        
          




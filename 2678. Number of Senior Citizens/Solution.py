class Solution:
    def countSeniors(self, details: List[str]) -> int:
        counter=0
        for age in details:
            if int(age[-4:-2]) > 60:
                counter+=1
        return counter
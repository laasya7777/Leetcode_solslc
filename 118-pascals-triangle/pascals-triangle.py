class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        i=0
        res=[]
        for i in range(numRows):
            rows=[1]*(i+1)
            for j in range(1,i):
                rows[j]=res[i-1][j-1]+res[i-1][j]
            res.append(rows)
        return res




        
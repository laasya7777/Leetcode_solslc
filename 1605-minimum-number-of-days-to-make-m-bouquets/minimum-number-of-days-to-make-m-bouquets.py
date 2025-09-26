class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def can_i_make_bouqets(bloomDay,day,m,k):
            flowers=0
            bouqets=0
            for bloomed_flower in bloomDay:
                if(bloomed_flower<=day):
                    flowers+=1
                    if(flowers==k):
                        bouqets+=1
                        flowers=0
                else:
                    flowers=0
            if(bouqets>=m):
                return True
            return False
        if(m*k>len(bloomDay)):
            return -1
        low=min(bloomDay)
        high=max(bloomDay)
        while(low<=high):
            day=(low+high)//2
            if(can_i_make_bouqets(bloomDay,day,m,k)):
                high=day-1
            else:
                low=day+1
        return low
        
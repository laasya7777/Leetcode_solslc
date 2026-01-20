class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[]
        nge={}
        for num in reversed(nums2):
            while st and st[-1]<=num:
                st.pop()
            if st:
                nge[num]=st[-1]
            else:
                nge[num]=-1
            st.append(num)
        res=[]
        for num in nums1:
            res.append(nge[num])
        return res
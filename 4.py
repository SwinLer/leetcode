#
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n=len(nums1),len(nums2)
        if m>n:
            nums1,nums2,m,n=nums2,nums1,n,m
        if n==0:
            raise ValueError

        #在nums1部分折半查找
        #由i取值确定j取值保证i+j取得数字总数一半
        imin=0
        imax=m
        half=(m+n+1)//2

        while imin<=imax:
            i=(imin+imax)//2
            j=half-i
            if i<m and nums2[j-1]>nums1[i]:
                imin=i+1
            elif i>0 and nums1[i-1]>nums2[j]:
                imax=i-1
            else:
                #i为中值
                if i==0:
                    max_left=nums2[j-1]
                elif j==0:
                    max_left=nums1[i-1]
                else:
                    max_left=max(nums1[i-1],nums2[j-1])

                if(m+n)%2==1:
                    return max_left
                
                if i==m:
                    min_right=nums2[j]
                elif j==n:
                    min_right=nums1[i]
                else:
                    min_right=min(nums1[i],nums2[j])

                    return (max_left+min_right)/2.0

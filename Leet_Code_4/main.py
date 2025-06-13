nums1=list(map(int,input("Enter the first sorted array: ").split()))
nums2=list(map(int,input("Enter the second sorted array: ").split()))
def median(nums1,nums2):
    nums=nums1+nums2
    nums.sort()
    n=len(nums)
    if n%2==0:
        return (nums[n//2]+nums[n//2-1])/2
    else:
        return nums[n//2]
print("Median of the two sorted arrays is: ",median(nums1,nums2))
#this method takes more time
def twoSum():
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return([i,j])


nums=[1,2,3,4,5]
target=9
result=twoSum()
print(result)

def _two_sum():
    seen={}
    for i,num in enumerate(nums1):
        if tar-num in seen:
            return(seen[tar-num],i)
        elif num not in seen:
            seen[num]=i


nums1=[1,4,6,7,9,5]
tar=16
res=_two_sum()
print(res)


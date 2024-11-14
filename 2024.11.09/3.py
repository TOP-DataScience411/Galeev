nums1 = map(int, input().split())
nums2 = map(int, input().split())
nums1 = list(nums1)
nums2 = list(nums2)

found = False
  
for i in range(len(nums1)):
    if nums1[i: i + len(nums2)] == nums2:
        found = True
        break

if found:        
    print('да')
else:
    print('нет')        



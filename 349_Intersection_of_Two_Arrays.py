from array import array

# 1. given nums 1,2,3,needs to get the numbers randomly
nums1 = [1,2,2,2,2,2,1,5,5,4,7]
nums2 = [2,2,2,2,2,2,1,3,4,5,5]
nums3 = []
#nums1_length = len(nums1))
#print(len(nums1))

# 2. compare two nums.
# (stick into leetcode box)
while len(nums1) > 0:
	nums_needs_to_be_compared = nums1.pop(0)
	count_flag = nums2.count(nums_needs_to_be_compared)
	if count_flag > 0:
		nums2.remove(nums_needs_to_be_compared)
		nums3.append(nums_needs_to_be_compared)
		# delete repeated numbers in nums3
#print(len(nums3))

#count_flag_2 = 0
index = 0
while len(nums3) > index :
	if nums3.count(nums3[index]) > 1:
		#print(nums3.count(nums3[index])
		nums3.remove(nums3[index])
		#print(nums3)
	else:
		index = index + 1
print(nums3)

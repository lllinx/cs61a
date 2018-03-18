"""1. Two Sum"""
# given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
def twoSum(nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: List[int]
	"""
	for i in range(0,len(nums)):
		for j in range(i+1,len(nums)):
			if nums[i] + nums[j] == target:
				return [i,j]
			j += 1
		i += 1

"""2. Add Two Number"""
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

"""3. Longest Substring Without Repeating Characters"""
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
def lengthOfLongestSubstring(s):
	"""
	:type s: str
	:rtype: int
	"""
	length=len(s)
	substring=[]
	i=0
	while i<length:
		string=s[i]
		j=i+1
		repeat=False
		while j<length and repeat==False:
			if s[j] not in string:
				string += s[j]
				j += 1
			else:
				repeat=True
				substring.append(string) 
		i += 1
	max_sub_len=max([len(i) for i in substring])
	return [x for x in substring if len(x)==max_sub_len]

"""4. Median of Two Sorted Arrays"""
def findMedianSortedArrays(nums1, nums2):
	"""
	:type nums1: List[int]
	:type nums2: List[int]
	:rtype: float
	"""
	def median(x):
		length=len(x)
		if length%2==0:
			return (x[length//2-1]+x[length//2])/2
		else:
			return x[(length-1)//2]
	if max(nums1)<min(nums2):
		new_list=nums1+nums2
	elif min(nums1)>max(nums2):
		new_list=nums2+nums1
	else:
		new_list=[]
		for el1 in list(nums1):
			for el2 in list(nums2):
				if el1<el2:
					new_list.append(el1)
					nums1.remove(el1)
				elif el1>el2:
					new_list.append(el2)
					nums2.remove(el2)
				elif el1==el2:
					new_list.extend([el1,el2])
					nums1.remove(el1)
					nums2.remove(el2)
	return median(new_list)

"""7. Reverse Integer"""
def reverse(x):
		"""
		:type x: int
		:rtype: int
		"""
		s=[]
		if x>=0:
			while x!=0:
				s.append(x%10)
				x=x//10
			new_x=sum([s[i]*pow(10,len(s)-i-1) for i in range(len(s))])
			return new_x
		else:
			return -1*reverse(-x)
reverse(123)
reverse(-123)
reverse(120)

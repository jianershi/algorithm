"""
845. Greatest Common Divisor
https://www.lintcode.com/problem/greatest-common-divisor/description
"""

class Solution:
	"""
	@param a: the given number
	@param b: another number
	@return: the greatest common divisor of two numbers
	"""
	def gcd(self, a, b):
		# write your code here
		if a > b:
			return self.greatest_common_divisor(a, b)
		else:
			return self.greatest_common_divisor(b, a)

	def greatest_common_divisor(self, big, small):
		if small == 0:
			return big
		return self.greatest_common_divisor(small, big % small)

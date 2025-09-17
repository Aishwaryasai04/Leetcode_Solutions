class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask=0xFFFFFFFF
        MAX_INT=0x7FFFFFFF

        while b!=0:
            carry=(a&b)&mask
            a=(a^b)&mask
            b=(carry <<1)&mask

        return a if a<=MAX_INT else ~(a^mask)

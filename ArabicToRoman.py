# print("Arabic to Roman program starts. \n")

def toRoman(num):
    strs = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]        
    ret = ""  
    
    if num < 0:
        return "-1"
    for i, j in enumerate(nums):
        while num >= j:
            ret += strs[i]
            num -= j
        if num == 0:
            return ret
    
#if __name__ == '__main__':
#    x = 1000
#    print(toRoman(x))

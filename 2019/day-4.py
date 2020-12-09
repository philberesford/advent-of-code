MIN = 235741
MAX = 706948

def isCandidate(num):
    numAsString = str(num)
    numAsList = list(numAsString) 
    nums = map(int, numAsList)

    i = 0
    hasConsecutive = False

    while i < len(nums)-1:
        current = nums[i]
        next = nums[i+1]
            
        if (current > next):
            return False

        if current == next:
            hasConsecutive = True

#        print(nums[i])
#        print(hasConsecutive)
        if hasConsecutive and i < len(nums)-2:
            hasConsecutive = current != nums[i+2]        
            if not hasConsecutive:
                return False


        i = i + 1    

    return hasConsecutive 

candidates = []

print(isCandidate(334334))
#for num in range(235741, 706949):
#    if (isCandidate(num)):
#        candidates.append(num)

#print(len(candidates))
#print(candidates)
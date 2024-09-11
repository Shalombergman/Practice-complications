

#1
# T(n) = 2n 
# O(n)
def CalculateOddSum(array):
    odd_sum = 0
    for num in array:
        if num % 2 != 0:
            odd_sum += num
    return odd_sum

#2
#T(n) = 2n -2
#O(n)
def FindMaximumTwo(array):
    maxTwoNum = array[0] + array[1]
    for i  in range(len(array) - 1):
        current = array[i] + array[i + 1]
        if current > maxTwoNum:
            maxTwoNum = current
    return maxTwoNum
#3
#T(n) = n
#O(n)
def ContainsNumber(array, n):
    for num in array:
        if num == n:
            return True
    return False
#4
#T(n) = 4n -2
#O(n)
def SumOfAllTriplets(array):
    if len(array) < 3:
        return 0
    maxTriplet = array[0] + array[1] + array[2]
    for i in range(len(array)-2):
        current = array[i] + array[i + 1] + array[i + 2]
        if current > maxTriplet:
            maxTriplet = current
    return maxTriplet
#5
#T(n) = 2n -2
#O(n)
def FindLastPairWithProduct(array, product):
    for i in range(len(array) - 1, 0, -1):
        if array[i] * array[i - 1] == product:
            return array[i - 1], array[i]
    return None
#6
#T(n) = 2n
#O(n)
def CountEvenNumbers(array):
    count = 0
    for num in array:
        if num % 2 == 0:
            count += 1
    return count
#7

#8
#O(n**2)
def FindPairsWithSum(array, sum):
    newArry = []
    for i in range(len(array)):
        j = i+1
        for j in range(j, len(array)):
            if array[i] + array[j] == sum:
                newArry.append((array[i], array[j]))
    return newArry
#9

#10

#11
#T(n)= 2n
#O(n)
def FindFirstRepeating(array):
    newArry = []
    for num in array:
        if num in newArry:
            return num
        newArry.append(num)
    return -1

def main():
    print(CalculateOddSum([3,5,6,7,8,9,2]))
    print(FindMaximumTwo([5,6,3,2,4,7,89]))
    print(ContainsNumber([4,5,6,7,8,3,4],6))
    print(SumOfAllTriplets([8,4,3,2,5,6,7,8]))
    print(FindLastPairWithProduct([6,5,4,3,6,7,8,6,7],5))
    print(CountEvenNumbers([5,6,8,9,2,3,]))
    print(FindFirstRepeating([2,3,4,5,4]))
if __name__ == "__main__":
    main()

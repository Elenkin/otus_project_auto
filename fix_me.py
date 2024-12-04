def calculate_average(nums):
    total = sum(nums)
    count = len(nums)
    average = total / count
    return average


nums = [10, 15, 20]
average = calculate_average(nums)
print("The average is:", average)

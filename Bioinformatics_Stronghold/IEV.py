### Calculating expected offspring ###

nums = open("C:/Users/anqja/Downloads/rosalind_iev.txt").readline().split(' ')
probs = [2, 2, 2, 1.5, 1, 0]
exp = 0
for i in range(len(nums)):
    exp += int(nums[i]) * probs[i]
print(exp)
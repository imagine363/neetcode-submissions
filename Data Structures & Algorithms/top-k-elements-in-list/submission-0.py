class Solution:
    def topKFrequent(self, nums, k):
        dic = {}
        for i in nums:
            key = i
            if key not in dic:
                dic[key] = 0
            dic[key] += 1
        sorteditems = sorted(dic.items(),key = lambda x : x[1], reverse= True)
        return [item[0] for item in sorteditems[:k]]
sol = Solution()
nums = [7,7] 
k = 1
print(sorted(sol.topKFrequent(nums,k)))

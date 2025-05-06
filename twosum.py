class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #usando dictionary hash map para resolver 
        index = {}
        #nums = [2,7,11,15], target = 9
        #usando enumaerate para conseguir acessar tanto o indice quanto o que esta dentro da posição do indice 
        for i, num in enumerate(nums):
            if target - num in index:
                return [i, index[target-num]]
            #apos iterar armazenamos caso a condição n ser cumprida e vamos para o proximo .
            index[num] = i

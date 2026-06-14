class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        n = len(nums)

        for i in range(n):
            product=1
            for j in range(n):
                if j ==i:
                    continue
                else:
                    product *= nums[j]

            products.append(product)

        return products    


        
## Minimum Index Sum of Two Lists

# Example 1:
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".

# Example 2:
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict1={}
        for idx,val in enumerate(list1):
            dict1[val]=idx
            
        dict2={}
        minIdxSum=len(list1)+len(list2)
        for idx,val in enumerate(list2):
            if val in dict1:
                dict2[val]=dict1[val]+idx
                if dict2[val]<minIdxSum:
                    minIdxSum=dict2[val]
        
        print(dict2)
        
        result=[]
        for k in dict2:
            if dict2[k]==minIdxSum:
                result.append(k)
        return result
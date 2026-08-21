from collections import deque
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        window = deque(arr[:k])
        print(window)

        for i in range(k,len(arr)):
            b = window[0]
            a = arr[i]
            print(f"from window b:{b}, from arr {a}")

            if (abs(a-x) < abs(b-x)) or (abs(a-x) == abs(b-x) and a<=b):
                window.append(a)
                window.popleft()

                
            
            else:
                break
                
        
        return list(window)

        
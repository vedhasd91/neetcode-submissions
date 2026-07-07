class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Input:
            target = 10, 
        
            p = [1,4], 
            s = [3,2]

            d = [9, 6]

        Output: 1
        """
        cars = [(p,s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)

        stack = []

        for p, s in cars:
            t = (target - p) / s
            if not stack:
                stack.append(t)
            if not t<=stack[-1]: 
                stack.append(t)

        return len(stack)
        
class Solution:
    def separateSquares(self, squares):
        def area_above(Y):
            total = 0.0
            for x, y, l in squares:
                top = y + l
                if Y <= y:
                    total += l * l
                elif Y < top:
                    total += (top - Y) * l
            return total

        def area_below(Y):
            total = 0.0
            for x, y, l in squares:
                top = y + l
                if Y >= top:
                    total += l * l
                elif Y > y:
                    total += (Y - y) * l
            return total

        low = min(y for _, y, _ in squares)
        high = max(y + l for _, y, l in squares)

        for _ in range(60):  
            mid = (low + high) / 2
            if area_above(mid) > area_below(mid):
                low = mid
            else:
                high = mid

        return (low + high) / 2

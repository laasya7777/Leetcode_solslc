class Solution:
    def separateSquares(self, squares):
        def diff(Y):
            d = 0.0
            for _, y, l in squares:
                top = y + l
                area = l * l
                if Y <= y:
                    d += area
                elif Y >= top:
                    d -= area
                else:
                    d += (top - Y) * l
                    d -= (Y - y) * l
            return d

        low = min(y for _, y, _ in squares)
        high = max(y + l for _, y, l in squares)

        for _ in range(50):   
            mid = (low + high) / 2
            if diff(mid) > 0:
                low = mid
            else:
                high = mid

        return (low + high) / 2

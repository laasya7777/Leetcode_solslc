class Solution:
    def separateSquares(self, squares):
        events = []
        xs = set()

        for x, y, l in squares:
            events.append((y, 1, x, x + l))   
            events.append((y + l, -1, x, x + l)) 
            xs.add(x)
            xs.add(x + l)

        events.sort()
        xs = sorted(xs)
        x_index = {x: i for i, x in enumerate(xs)}

        seg = [0] * (4 * len(xs))
        count = [0] * (4 * len(xs))

        def update(node, l, r, ql, qr, val):
            if ql <= l and r <= qr:
                count[node] += val
            else:
                mid = (l + r) // 2
                if ql <= mid:
                    update(node * 2, l, mid, ql, qr, val)
                if qr > mid:
                    update(node * 2 + 1, mid + 1, r, ql, qr, val)

            if count[node] > 0:
                seg[node] = xs[r + 1] - xs[l]
            else:
                seg[node] = seg[node * 2] + seg[node * 2 + 1] if l != r else 0

       
        prev_y = events[0][0]
        total_area = 0

        for y, typ, x1, x2 in events:
            dy = y - prev_y
            total_area += seg[1] * dy
            update(1, 0, len(xs) - 2, x_index[x1], x_index[x2] - 1, typ)
            prev_y = y
        seg = [0] * (4 * len(xs))
        count = [0] * (4 * len(xs))
        area = 0
        prev_y = events[0][0]

        for y, typ, x1, x2 in events:
            dy = y - prev_y
            curr_width = seg[1]
            if curr_width > 0:
                if area + curr_width * dy >= total_area / 2:
                    return prev_y + (total_area / 2 - area) / curr_width
                area += curr_width * dy

            update(1, 0, len(xs) - 2, x_index[x1], x_index[x2] - 1, typ)
            prev_y = y

        return prev_y

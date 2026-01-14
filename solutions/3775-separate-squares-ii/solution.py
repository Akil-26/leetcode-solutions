from typing import List
from collections import Counter

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        xs = set()

        # Build y-events and collect x-coordinates
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
            xs.add(x)
            xs.add(x + l)

        events.sort()
        xs = sorted(xs)

        # Coordinate compression for x
        x_id = {x: i for i, x in enumerate(xs)}

        # Segment tree to maintain covered x-length
        n = len(xs) - 1
        cover = [0] * (4 * n)
        length = [0] * (4 * n)

        def push_up(node, l, r):
            if cover[node] > 0:
                length[node] = xs[r + 1] - xs[l]
            elif l == r:
                length[node] = 0
            else:
                length[node] = length[node * 2] + length[node * 2 + 1]

        def update(node, l, r, ql, qr, val):
            if ql <= l and r <= qr:
                cover[node] += val
                push_up(node, l, r)
                return
            mid = (l + r) // 2
            if ql <= mid:
                update(node * 2, l, mid, ql, qr, val)
            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr, val)
            push_up(node, l, r)

        # -------- First sweep: compute total area --------
        prev_y = events[0][0]
        total_area = 0

        for y, typ, x1, x2 in events:
            dy = y - prev_y
            if dy > 0:
                total_area += length[1] * dy

            l = x_id[x1]
            r = x_id[x2] - 1
            update(1, 0, n - 1, l, r, typ)
            prev_y = y

        half = total_area / 2

        # -------- Second sweep: find exact y --------
        cover = [0] * (4 * n)
        length = [0] * (4 * n)

        prev_y = events[0][0]
        acc = 0

        for y, typ, x1, x2 in events:
            dy = y - prev_y
            if dy > 0 and length[1] > 0:
                area = length[1] * dy
                if acc + area >= half:
                    return prev_y + (half - acc) / length[1]
                acc += area

            l = x_id[x1]
            r = x_id[x2] - 1
            update(1, 0, n - 1, l, r, typ)
            prev_y = y

        return 0.0

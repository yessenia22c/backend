def queensAttack(n, k, rq, cq, obstacles):
    obstacles_set = {(r, c) for r, c in obstacles}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    attackable_squares = 0

    for dr, dc in directions:
        r, c = rq, cq
        while 1 <= r + dr <= n and 1 <= c + dc <= n:
            r += dr
            c += dc
            if (r, c) in obstacles_set:
                break
            attackable_squares += 1

    return attackable_squares

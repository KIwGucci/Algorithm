import heapq as hpq
"""ヒープ構造の実装はせずライブラリheapqを利用することにした"""

def heapsort(iterlist):
    h = []
    #ヒープ構造を生成
    for value in iterlist:
        hpq.heappush(h, value)
    # ヒープから順に値を取り出すリスト内包
    return [hpq.heappop(h) for i in range(len(h))]


before = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
after = heapsort(before)
print('before : {}'.format(before))
print('after : {}'.format(after))

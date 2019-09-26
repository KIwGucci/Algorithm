# coding:utf-8


class Binatree():
    """二分木構造クラス"""
    # dataに其の木の値を束縛
    # left,rightは其の左右の子には初期はNoneを代入。その子に値が割り当てられる際に
    # Binatreeとして子Binatreeクラスを代入
    # parentbranchに親Binatreeクラスを割り当てる
    def __init__(self, parentbranch=None):
        self.data = None
        self.left = None
        self.right = None
        self.parentbranch = parentbranch


class Heap():
    def __init__(self):
        # 親に二分木構造を割り当て
        self.parent = Binatree(None)
        # lastbranchesに二分木構造の最末端のデータを格納
        self.lastbranches = [self.parent]

    def downheap(self):
        # 子にデータがない場合は再構築はしない
        for i in self.lastbranches:
            if i.data is None:
                return None
        else:
            # 最末端のデータが全て値を持っている時、其々の左右木にヒープ構造を割り当て
            # データ処理対象を1段下がる
            branches = []
            for i in self.lastbranches:
                i.left = Binatree(i)
                i.right = Binatree(i)
                branches.append(i.left)
                branches.append(i.right)
            self.lastbranches = branches

    def upheap(self):
        # 最末端段のデータの全てが値を持たないときデータ処理対象を1段あげる
        for i in self.lastbranches:
            # 最上位ではNoneを返す
            if i.parentbranch is None:
                return None
            elif i.data is not None:
                # 最末端の段にデータが残っている場合 はFalseを返す
                return False
            else:
                pass
        else:
            # 上記for文条件確認を通過したら子ヒープ構造をNoneにし
            # データ処理対象を1段上がる
            parents = []
            predata = None
            for i in self.lastbranches:
                if i.parentbranch is predata:
                    # 左右で同じ親が出現するので重複を避ける
                    pass
                else:
                    parents.append(i.parentbranch)
                    predata = i.parentbranch
                i = None
            self.lastbranches = parents

    def insert(self, num):
        """二分木ピープ構造にnumを加える"""
        # lastbranchesは二分木構造クラスのlist
        self.downheap()
        cur = None
        for i in self.lastbranches:
            if i.data is None:
                i.data = num
                cur = i
                break

        while True:
            if cur.parentbranch is None:
                # 最上位でループから抜ける
                break
            parent = cur.parentbranch
            if cur.data < parent.data:
                cur.data, parent.data = parent.data, cur.data
                cur = parent
            else:
                break

    def popdata(self):
        """ヒープ構造からtopにある数字を取り出す"""
        popnum = self.parent.data
        try:
            lastd = [i for i in self.lastbranches if i.data is not None][-1]
        except IndexError:
            return None
        self.parent.data = lastd.data
        lastd.data = None
        self.upheap()
        cur = self.parent
        while True:
            if cur is None:
                break
            elif cur.data is None or (cur.left is None and cur.right is None):
                break
            if cur.left.data is None and cur.right.data is None:
                break
            elif cur.left.data is None:
                children = cur.right
            elif cur.right.data is None:
                children = cur.left
            elif cur.left.data <= cur.right.data:
                children = cur.left
            else:
                children = cur.right

            if cur.data > children.data:
                cur.data, children.data = children.data, cur.data
                cur = children
            else:
                break

        return popnum

    def addnums(self, nums):
        """insert some numbers"""
        for i in nums:
            self.insert(i)


def heapsort(numbers):
    """リストをヒープソートでソート処理して返す"""
    heapstr = Heap()
    heapstr.addnums(numbers)
    sortedlist = []
    while True:
        output = heapstr.popdata()
        if output:
            sortedlist.append(output)
        else:
            break
    return sortedlist


example = [5, 20, 2, 1, 100, 46, 3, 2, 500, 15, 30, 5]
print(f'before {example}')
print(f'after {heapsort(example)}')

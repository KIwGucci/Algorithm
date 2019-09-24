# coding:utf-8


class Binatree():
    def __init__(self, parentbranch=None):
        self.data = None
        self.left = None
        self.right = None
        self.parentbranch = parentbranch


class Heap():
    def __init__(self):
        # 親に二本木構造を割り当て
        self.parent = Binatree(None)
        self.lastbranches = [self.parent]

    def downheap(self):
        # 子にデータがない場合は再構築はしない
        for i in self.lastbranches:
            if i.data is None:
                return None
        else:
            # 上記for文条件確認を通過したら孫にヒープ構造を割り当て
            # データ処理対象を1段下がる
            branches = []
            for i in self.lastbranches:
                i.left = Binatree(i)
                i.right = Binatree(i)
                branches.append(i.left)
                branches.append(i.right)
            self.lastbranches = branches

    def upheap(self):
        # 其の段にデータがない場合は一段上がる
        for i in self.lastbranches:
            # 最上位ではNoneを返す
            if i.parentbranch is None:
                return None
            elif i.data is not None:
                # 其の段にデータが残っている場合 はFalseを返す
                return False
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
            elif cur.parentbranch.data > cur.data:
                cur.parentbranch.data, cur.data = cur.data, cur.parentbranch.data
                cur = cur.parentbranch
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
            jdleft = False
            jdright = False
            if cur.data is None:
                break
            if cur.left is not None and cur.left.data is not None:
                if cur.data > cur.left.data:
                    cur.data, cur.left.data = cur.left.data, cur.data
                    jdleft = True
            if cur.right is not None and cur.right.data is not None:
                if cur.data > cur.right.data:
                    cur.data, cur.right.data = cur.right.data, cur.data
                    jdright = True

            if jdright:
                cur = cur.right
            elif jdleft and jdright is False:
                cur = cur.left
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
    sortedlist=[]
    while True:
        output = heapstr.popdata()
        if output:
            sortedlist.append(output)
        else:
            break
    return sortedlist

example = [5,20,2,1,100,46,3,2]
print(f'before {example}')
print(f'after {heapsort(example)}')
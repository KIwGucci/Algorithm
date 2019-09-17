# coding:utf-8


class Binatree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.alterna = True


class Heap():
    def __init__(self, nums):
        self.parent = None
        for num in nums:
            self.insert(num)

    def insert(self, num):
        """二分木ピープ構造にnumを加える"""
        n = self.parent  # nに親ノードを束縛
        if n is None:
            # 親に二分木を割り当て
            self.parent = Binatree(num)
            return True
        else:
            # 親に数値が入っている場合
            while True:
                if n.data > num:
                    #挿入する値numが親より小さい時、numと親を入れ替え
                    n.data, num = num, n.data
                if n.left is None:
                    # 左に二分木を割り当て
                    n.left = Binatree(num)
                    break
                elif n.right is None:
                    # 右に二分木を割り当て
                    n.right = Binatree(num)
                    break
                elif n.alterna is True:
                    # 親の左右が埋まっている時、左を親にして子二分木構造生成
                    # alternaで左右交互に切り替え
                    n.alterna = False
                    n = n.left
                else:
                    # 親の左右が埋まっている時、右を親にして子二分木構造生成
                    n.alterna = True
                    n = n.right

a= Heap([5,2,10,1,3])
o = a.parent
print(o.data,o.left.data,o.right.data)
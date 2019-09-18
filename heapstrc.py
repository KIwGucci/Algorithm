# coding:utf-8


class Binatree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.alterna = True


class Heap():
    def __init__(self, nums):
        self.numbers = nums
        self.parent = None
        self.lastbranch = None
        for num in self.numbers:
            self.insert(num)

    def insert(self, num):
        """二分木ピープ構造にnumを加える"""
        n = self.parent  # nに親を束縛 後から左右のブランチに入れ替えることで降っていく
        if n is None:
            # 親に二分木を割り当て
            self.parent = Binatree(num)
            n = self.parent
        if n.data is None:
            n.data = num
        # 親に数値が入っている場合
        while True:
            if n.data > num:
                # 挿入する値numが親より小さい時、numと親を入れ替え
                n.data, num = num, n.data
            # 最端末にnumを追加する。木をたどって小左右木の値とnumを比較入れ替えし小さい方を上位にする
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
                n = n.left  # 左ブランチを親としてnに束縛
            else:
                # 親の左右が埋まっている時、右を親にして子二分木構造生成
                n.alterna = True
                n = n.right  # 右ブランチを親としてnに束縛
       
        self.lastbranch = n

    def popdata(self):
        # 以下検証中
        popnum = self.parent.data
        self.parent.data = None
        num = self.lastbranch.data
        self.lastbranch.data = None
        self.insert(num)
        # return popnum

 
a = Heap([5, 2, 10, 1, 3])

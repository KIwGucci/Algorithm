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
            # 最末端のデータが全て値を持っていない時、現在処理対象となっている二分木をNoneにし
            # データ処理対象を1段上がる
            # 現在の処理対象となっている二分木の親をparentsリストに格納する
            parents = []
            # predata:前のデータを記憶しておくための仮変数
            predata = None
            for i in self.lastbranches:
                if i.parentbranch is predata:
                    # 左右で同じ親が出現するので重複を避ける
                    pass
                else:
                    parents.append(i.parentbranch)
                    predata = i.parentbranch
                # 親の格納が終わった二分木データ構造をNoneとする
                i = None
            # 処理対象データを現在の二分木の親に変更し処理対象を一段あげる。
            self.lastbranches = parents

    def insert(self, num):
        """二分木ピープ構造にnumを加える"""
        # lastbranchesは二分木構造クラスのlist
        # ヒープ構造を再構築
        self.downheap()
        cur = None
        for i in self.lastbranches:
            # ヒープ最末端のデータ群のdataの値がNoneのものが
            # 見つかった時点でnumの値を代入する
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
                # 追加したデータの値と其の親のdataの値を比較して親よりも値が小さい時は
                # 値を入れ替える。
                cur.data, parent.data = parent.data, cur.data
                # さらに其の親と比較するためにcur(カーソル)に親を代入する
                cur = parent
            else:
                break

    def popdata(self):
        """ヒープ構造からtopにある数字を取り出す"""
        # ヒープ最上位の値をpopnumとして取り出す
        popnum = self.parent.data
        try:
            lastd = [i for i in self.lastbranches if i.data is not None][-1]
        except IndexError:
            return None
        # ヒープ最末端の値を最上位のdataの値に代入する
        self.parent.data = lastd.data
        lastd.data = None
        # ヒープ構造を再構築
        self.upheap()
        # 作業カーソルを最上位に
        cur = self.parent
        while True:
            # 現在の二分木にデータがある場合とない場合で比較対象となるchildrenを変更する
            # leftとright両方にデータがある場合は値の小さい方を比較対象とする
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
            # 現在の二分木構造のdataの値と上記で選択した子木のdataの値を比較して子の方が
            # dataの値が小さい時はdataの値を入れ替え
            if cur.data > children.data:
                cur.data, children.data = children.data, cur.data
                # さらに下の層dataの値と比較するため作業カーソルにchildrenを代入
                cur = children
            else:
                break

        return popnum

    def addnums(self, nums):
        """insert some numbers"""
        # 前述のinsert関数をリストで連続処理する
        for i in nums:
            self.insert(i)


def heapsort(numbers):
    """リストをヒープソートでソート処理して返す"""
    heapstr = Heap()
    # ヒープクラスのaddnumsを使って値をヒープ構造に格納する
    heapstr.addnums(numbers)
    sortedlist = []
    while True:
        # ヒープ構造から一つずつ値を取り出しsortedlistに加えていく
        output = heapstr.popdata()
        if output:
            sortedlist.append(output)
        else:
            break
    return sortedlist


example = [5, 20, 2, 1, 100, 46, 3, 2, 500, 15, 30, 5]
print(f'before {example}')
print(f'after {heapsort(example)}')

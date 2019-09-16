# coding:utf-8


def selectsort(numlist):
    """sort numlist with select sort"""
    n = len(numlist)
    if n == 1:
        return numlist
    else:
        # 選択ソート
        # リストの中で最小値を選択し左端に持っていく。
        # 本来は線形探索で最小値を見つけるがここでは組み込み関数minを用いる
        minimum = min(numlist)
        minindex = numlist.index(minimum)
        headnum = numlist.pop(minindex)
        # 上記を行った後左端をソート済みとして残り要素を順に処理
        # ここでは再帰関数を用いているÏ
        return [headnum]+selectsort(numlist)


def main():
    before = [6, 3, 2, 5, 4, 1]
    print('before : {}'.format(before))
    print('after : {}'.format(selectsort(before)))


if __name__ == "__main__":
    main()

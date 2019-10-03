# coding:utf-8


def bubblesort(numlist):
    """sort numlist by using bubblesort"""
    n = len(numlist)
    if n == 1:
        return numlist
    else:
        # バブルソート
        # 右から順に隣り合った数を比較して小さい方を左になるように入れ替える
        for i in reversed(range(1, n)):
            if numlist[i] < numlist[i-1]:
                numlist[i], numlist[i-1] = numlist[i-1], numlist[i]
        # 比較が終わったら左端をソート済みとして再度残ったリスト要素で上記を行う
        # ここでは再帰を用いて処理
        return [numlist[0]] + bubblesort(numlist[1:])


def main():
    before = [2, 13, 6, 4, 3, 1, 5, 7, 9, 8, 10, 2, 3, 800, 30, 40, 50]
    print('before : {}'.format(before))
    print('after : {}'.format(bubblesort(before)))


if __name__ == "__main__":
    main()

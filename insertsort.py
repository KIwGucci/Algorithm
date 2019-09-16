# coding:utf-8


def insertsort(numlist):
    """sort numlist by using insertsorting"""
    n = len(numlist)
    if n == 1:
        return numlist
    else:
        # 挿入ソート：左端を処理済みとしてと次の要素を左と比較
        # 自分が左より小さかったら入れ替え。さらに左と比較して入れ替えが発生しなくなるまで続ける
        # 上記が終わると処理済みとして処理の要素を右に1つずらして最後まで繰り返して処理
        for i in range(n):
            while True:
                if i == 0:
                    break
                elif numlist[i] < numlist[i-1]:
                    numlist[i], numlist[i-1] = numlist[i-1], numlist[i]
                    i -= 1
                else:
                    break
    return numlist


def main():
    before = [6, 10, 5, 20, 2, 4, 3, 1]
    print('before : {}'.format(before))
    print('after : {}'.format(insertsort(before)))


if __name__ == "__main__":
    main()

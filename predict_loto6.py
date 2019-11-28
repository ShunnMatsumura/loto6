# coding: UTF-8
import numpy as np

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]

def predict_combination():
    deleteContent("./datas/predict.txt")
    # 131-135の組み合わせを取得
    # 有力候補の組み合わせが存在しているか確認
    result = []
    with open("./datas/result6culumn.txt", "r") as all_conbinations:
        for line in all_conbinations:
            for l in greate_sets():
                target = ",".join(map(str, l))
                if(target in line):
                    result.append(line.strip())

    # 既存の当選番号は省く
    predict_combinations = []
    for l in result:
        with open("./datas/real_result.txt", "r") as real_result:
            for line in real_result:
                if(l == line.strip()):
                    predict_combinations.append(l)
    
    for l in result:
        if(l in predict_combinations):
            result.remove(l)
    
    # 予測のファイルへ出力
    with open("./datas/predict.txt", "w") as predict:
        for r in result:
            predict.write(r+"\n")
        
    # 任意の組み合わせを返却
    for x in range(0, 5):
        desteny = np.random.randint(len(result))
        print result[desteny]

    return "これが当たるよ"

def deleteContent(fName):
    with open(fName, "w"):
        pass

# targetが合計になる整数の組み合わせを配列で返す
def a(lst, target, with_replacement=False):
    def _a(idx, l, r, t, w):
        if t == sum(l): r.append(l)
        elif t < sum(l): return
        for u in range(idx, len(lst)):
            _a(u if w else (u + 1), l + [lst[u]], r, t, w)
        return r
    return _a(0, [], [], target, with_replacement)

# 組み合わせの中から、6この要素をもつ配列だけ抽出し、ファイルへ書き出し
def c(data):
    outputfile = open("./datas/result6culumn.txt", "w")
    for d in data:
        if(len(d) == 6):
            str_list = map(str, d)
            write_data = ",".join(str_list)+"\n"
            outputfile.write(write_data)
    outputfile.close()

# 実際の当選番号一覧
def get_real_result():
    real_result_file = open("./datas/real_result.txt")
    real_result_list = []
    for line in real_result_file:
        real_result_list.append(line)

# 合計値が密集している130-135のレンジで生成される自然数の組み合わせをファイルにappendする
# for target in range(131, 135):
#     c(a(list, target))

# 実際の当選番号は一度も重複していないので、候補から外す
def reduce_real_result_nums(all_data):
    pass

# 統計的に有力な数字が特定の部分に入っている組み合わせだけ抽出
def get_main_sets(parameter_list):
    pass

# 有力な数字の組み合わせをセット
def greate_sets():
    greate_sets = [
        [1, 10, 21, 28, 35, 43],
        [1, 10, 21, 28, 35],
        [1, 10, 21, 28],
        [1, 10, 21],
        [1, 10],
        [10, 21, 28, 35, 43],
        [10, 21, 28, 35],
        [10, 21, 28],
        [10, 21],
        [21, 28, 35, 43],
        [21, 28, 35],
        [21, 28],
        [21, 28, 35],
        [21, 28],
        [28, 35],
    ]
    return greate_sets

print predict_combination()

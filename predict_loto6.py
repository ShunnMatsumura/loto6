def a(lst, target, with_replacement=False):
    def _a(idx, l, r, t, w):
        if t == sum(l): r.append(l)
        elif t < sum(l): return
        for u in range(idx, len(lst)):
            _a(u if w else (u + 1), l + [lst[u]], r, t, w)
        return r
    return _a(0, [], [], target, with_replacement)

def c(data):
    outputfile = open("./datas/result6culumn.txt", "w")
    for d in data:
        if(len(d) == 6):
            str_list = map(str, d)
            write_data = ",".join(str_list)+"\n"
            outputfile.write(write_data)
    outputfile.close()

def get_real_result():
    real_result_file = open("./datas/real_result.txt")
    real_result_list = []
    for line in real_result_file:
        real_result_list.append(line)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]

for target in range(101, 151):
    c(a(list, target))
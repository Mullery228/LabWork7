import os


def get_size_in_list(path: str) -> list:
    list_of_sizes = list()
    for entry in os.scandir(path):
        if entry.is_file():
            list_of_sizes.append(entry.stat(follow_symlinks=False).st_size)
        elif entry.is_dir():
            list_of_sizes += (get_size_in_list(entry))
    return list_of_sizes


def get_dict():
    pat = 'W:\LabWork7.4\project'
    need_list = get_size_in_list(pat)
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(len(need_list)):
        if type(need_list[i]) == int:
            if need_list[i] <= 100:
                a += 1
            elif need_list[i] > 100 and need_list[i] <= 1000:
                b += 1
            elif need_list[i] > 1000 and need_list[i] <= 10000:
                c += 1
            elif need_list[i] > 10000 and need_list[i] <= 100000:
                d += 1
    dickt = {'100': a, '1000': b, '10000': c, '100000': d}
    return dickt


print(get_dict())

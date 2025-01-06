import os

def union_fs(f_paths = ["1.txt", "2.txt", "3.txt"], f_out ="union_fs.txt"):
    f_info = []
    for f_path in f_paths:
        with open(f_path,'r', encoding='utf-8') as f:
            lines = f.readlines()
            line_count = len(lines)
            f_info.append((f_path, line_count, lines))
    
    f_info.sort(key=lambda tup: tup[1])

    with open(f_out, 'w', encoding='utf-8') as out_f:
        for f_path, line_count, lines in f_info:
            out_f.write(f"{f_path} \n")
            out_f.write(f"{line_count} \n")
            for line in lines:
                 out_f.write(line)
            out_f.write("\n")

f_paths = ["1.txt", "2.txt", "3.txt"]
f_out ="union_fs.txt"

union_fs(f_paths, f_out)
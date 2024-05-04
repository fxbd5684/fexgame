import os

def count_code_lines(path):
    """ 统计指定目录下的代码行数 """
    counts = {}
    all_code_lines = 0
    for root, dirs, files in os.walk(path):
        # 排除.venv目录
        if '.venv' in root:
            continue
        for file in files:
            # 统计.py文件中的代码行数
            if file.endswith('.py'):
                file_path = os.path.relpath(os.path.join(root, file), path)  # 使用相对路径
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    line_count = len(lines)
                    counts[file_path] = line_count
                    all_code_lines += line_count
    
    # 按照代码行数多少排序
    sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
    return all_code_lines, sorted_counts


if __name__ == '__main__':
    # 统计当前目录下的代码行数
    current_dir = os.getcwd()
    code_lines, sorted_counts = count_code_lines(current_dir)

    print('当前目录下的代码行数：', code_lines)
    print('\n文件路径\t\t\t代码行数')
    for file_path, line_count in sorted_counts.items():
        print(f'{file_path.ljust(30)}|\t{line_count}')
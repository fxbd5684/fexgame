def return_border(content, width, wight=6):
    """
    打印带有特定边框样式的内容

    参数:
    content (str): 要打印的内容
    width (int): 边框宽度
    """
    # 构建上下边框
    top_bottom = "+" + "-" * (width + wight * 2) + "+"

    # 构建内容行
    content_lines = content.splitlines()
    wrapped_lines = [line.center(width) for line in content_lines]
    content_rows = ""
    for i in range(len(content_lines)):
        content = content_lines[i]
        is_the_last_line = i == len(wrapped_lines) - 1
        content_rows = (
            content_rows
            + "|"
            + " " * wight
            + content
            + " " * wight
            + "|"
            + ("\n" if not is_the_last_line else "")
        )

    con = ""
    con += top_bottom + "\n"
    con += content_rows + "\n"
    con += top_bottom

    return con


def return_menu(menu_items, width=None, wight=6):
    """
    打印带边框的菜单

    参数:
    menu_items (list): 菜单项列表
    width (int): 菜单边框宽度,如果不提供则根据最长菜单项长度自动计算
    """
    # 计算所需边框宽度
    if width is None:
        max_length = max(len(item) for item in menu_items)
        width = max_length + 4

    # 构建菜单项字符串
    menu_str = "\n".join(item.center(width - 2) for item in menu_items)

    # 打印边框
    return return_border(menu_str, width, wight=wight)


if __name__ == "__main__":
    menu_items = ["选项1", "选项2", "选项3", "选项4"]
    print(return_menu(menu_items))

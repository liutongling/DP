'''
    思路：如果发现不能按照第一个循环寻找最大前后缀长度（也就是patt[prefix_len]!=patt[i]）,
    此时的思路就是退而求其次，选择剩下较小的前后缀长度，然后比较较小前后缀长度的下一个字符是不是与当前要匹配patt[i]相同，如果相同则此时next[i+1]等于当前的较小的前后缀长度加1.
    否则继续上述的循环。
'''
def build_next(patt):
    # 计算Next数组
    next = [0]
    prefix_len = 0
    i = 1
    while i < len(patt):
        if patt[prefix_len] == patt[i]:
            prefix_len += 1
            next.append(prefix_len)
            i += 1
        else:
            if prefix_len == 0:
                next.append(0)
                i += 1
            else:
                prefix_len = next[prefix_len - 1]
    return next


def compute_next_array(pattern):
    """
    计算KMP算法中的next数组

    参数:
    pattern -- 要计算next数组的模式字符串

    返回:
    next数组
    """
    n = len(pattern)
    next_arr = [0] * n
    next_arr[0] = -1  # 初始值设为-1

    i, j = 0, -1  # i是主指针，j是前缀指针

    while i < n - 1:
        # j == -1 表示需要从头开始匹配
        # pattern[i] == pattern[j] 表示当前字符匹配成功
        if j == -1 or pattern[i] == pattern[j]:
            i += 1
            j += 1
            next_arr[i] = j
        else:
            # 字符不匹配时，j回退到next[j]的位置
            j = next_arr[j]

    return next_arr


def kmp_search(text, pattern):
    """
    使用KMP算法在文本中搜索模式串

    参数:
    text -- 待搜索的文本
    pattern -- 要搜索的模式串

    返回:
    匹配成功的起始位置列表
    """
    n, m = len(text), len(pattern)
    next_arr = compute_next_array(pattern)
    result = []

    i, j = 0, 0  # i是文本指针，j是模式指针

    while i < n:
        # j == -1 表示需要从头开始匹配
        if j == -1 or text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            # 不匹配时，根据next数组跳转
            j = next_arr[j]

        # 找到完整匹配
        if j == m:
            result.append(i - j)
            j = next_arr[j - 1] if j > 0 else -1

    return result


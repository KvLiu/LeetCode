#coding=utf-8

# 读文件到缓冲区
def process_file(dst):
    try:     # 打开文件
        f = open(dst, 'r')  # dst为文本的目录路径
    except IOError as s:
        print(s)
        return None
    try:     # 读文件到缓冲区
        bvffer = f.read()
        print type(bvffer)
    except:
        print("Read File Error!")
        return None
    f.close()
    return bvffer


# 处理缓冲区，返回存放每个单词频率的字典word_freq
def process_buffer(bvffer):
    if bvffer:
        # 下面添加处理缓冲区bvffer代码，统计每个单词的频率，存放在字典word_freq
        word_freq = {}
        # 将文本内容都改为小写且去除文本中的中英文标点符号
        for ch in '“‘!;,.?”':
             bvffer = bvffer.lower().replace(ch, " ")
        # strip()删除空白符（包括'/n', '/r','/t'）；split()以空格分割字符串
        words = bvffer.strip().split()
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
        return word_freq


# 出现频率排在前*的单词
def output_result(word_freq):
        if word_freq:
            sorted_word_freq = sorted(word_freq.items(), key=lambda v: v[1], reverse=True)
            for item in sorted_word_freq[:100]:  # 输出 Top 139 的单词

                print("单词:%s 频数:%d " % (item[0], item[1]))


def main():
    # 文件的路径和名字
    # dst = "C:\\Users\\1\\Desktop\\review2.txt"
    dst = "F:\\LeetCode\\DataProcess\\review1.txt"
    bvffer = process_file(dst)
    word_freq = process_buffer(bvffer)
    output_result(word_freq)


if __name__ == "__main__":
    main()
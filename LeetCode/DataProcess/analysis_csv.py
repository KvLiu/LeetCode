# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
import os

result_data = {}


def process_file(file_path):
    # read raw scv file
    try:
        df = pd.read_csv(file_path, error_bad_lines=False)

    except IOError as err:
        print(err)
        return None

    room_id_list = []
    for index in range(len(df["id"])):
        room_id_list.append(df["id"][index])
    # print "room_id_list=", room_id_list
    len_comment = len(room_id_list)
    print "comment_nums=", len_comment

    current_index = df.ix[0][0]
    print (type(current_index))
    room_comments = ""
    for i in range(len(df["id"])):
        if df.ix[i][0] == current_index:
            #print "current_index=", current_index
            #print "current_comment=", str(df.ix[i][1])
            if not isinstance(df.ix[i][1], float):
                temp = df.ix[i][1].encode(encoding='UTF-8', errors='ignore')
            else:
                temp = str(df.ix[i][1])
            room_comments += temp + " "
            continue
        else:  # analysis comment，write room id and comment to result.csv
            # print "room_comments=", room_comments
            # print "process_buffer", current_index, "starting..."
            word_freq = process_buffer(room_comments)
            # print "process_buffer", current_index, "done..."
            output_result(current_index, word_freq)
            room_comments = ""
            current_index = df.ix[i][0]


# 处理缓冲区，返回存放每个单词频率的字典word_freq
def process_buffer(bvffer):
    if bvffer:
        # 下面添加处理缓冲区bvffer代码，统计每个单词的频率，存放在字典word_freq
        word_freq_dic = {}
        # 将文本内容都改为小写且去除文本中的中英文标点符号
        for ch in '“‘!;,.?”':
             bvffer = bvffer.lower().replace(ch, " ")
        # strip()删除空白符（包括'/n', '/r','/t'）；split()以空格分割字符串
        words = bvffer.strip().split()
        for word in words:
            word_freq_dic[word] = word_freq_dic.get(word, 0) + 1
        # print "word_freq =", sorted(word_freq_dic.items(), key=lambda v: v[1], reverse=True)
        return word_freq_dic


# 出现频率排在前*的单词
def output_result(room_id, word_freq):
    if word_freq:
        sorted_word_freq = sorted(word_freq.items(), key=lambda v: v[1], reverse=True)
        str_current = ""
        for item in sorted_word_freq[:20]:  # 输出 Top 20 的单词
            str_current += "单词:" + str(item[0]) + "频数:" + str(item[1]) + ";"
        # temp_list = [str(room_id), str_current]
        # print "temp_list=", temp_list
        result_data[str(room_id)] = str_current #.encode(encoding='UTF-8')



def main():
    src = r'F:/LeetCode/DataProcess/s1.csv'
    rst = r'F:/LeetCode/DataProcess/result.csv'
    title = ["room_id", "keywords"]
    # with open(rst, "w") as result:
    #     result.write(','.join(title) + '\n')
    process_file(src)
    print "result_data=", result_data
    # df = pd.DataFrame.from_dict(result_data, orient='index', columns=["room_id", "keywords"])
    # print "df=", df
    # df.to_csv(rst, encoding='utf-8')

    # save to result.svc
    title = ["room_id", "keywords"]
    my_path = "F:/LeetCode/DataProcess"
    if not os.path.exists(my_path):
        os.makedirs(my_path, 0755)
        print"Path is created"
    fname = my_path + "/" + "t1.csv"
    with open(fname, "w",) as result:
        result.write(','.join(title) + '\n')
        for key, val in result_data.iteritems():
            row_content = key + "," + val + '\n'
            result.write(row_content)


if __name__ == "__main__":
    main()
def reverseWords(input):
     
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")
 
    # 翻转字符串
    inputWords=inputWords[::-1]
 
    # 重新组合字符串
    output = ' '.join(inputWords)

    return output
 
if __name__ == "__main__":
    input = 'I like runoob'
    rw = reverseWords(input)
    print(rw)


print(reverseWords('you love i'))


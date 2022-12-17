import pwgenerator as pw

Characters = ["Char", "gngnaga", "agnajgagja", "aabbcc"]


for chars in Characters:
    total_char = pw.CountChar(chars)

    print(total_char)
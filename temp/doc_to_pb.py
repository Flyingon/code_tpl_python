
doc = """
BossCommand	请求命令字	Int	
BossTranTime	交易时间	String	
BossUserNumType	业务号码类型	Int	
BossUserNum	业务号码	String	
BossProductID	物品id	String	
"""

if __name__ == '__main__':
    d_list = doc.split("\n")
    num = 1
    for d in d_list:
        l = d.split("	")
        # print(l)
        if len(l) < 2:
            continue
        name = l[0]
        desc = l[1]
        t = l[2]
        # print(name, t)
        if t == "String":
            print("string %s = %s; // %s" % (name, num, desc))
        elif t == "Int":
            print("int32 %s = %s; // %s" % (name, num, desc))
        num += 1

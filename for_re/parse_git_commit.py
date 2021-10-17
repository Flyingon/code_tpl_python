import re

pattern = re.compile("--(story|task|issue|bug)=([0-9]+|#[0-9]+)")


def parse_commit(msg):
    line_list = msg.split("\n")
    for l in line_list:
        d_list = pattern.findall(l)
        print(d_list)


parse_commit("阿斯顿撒大的\n--story=868528101\n--story=868528101")

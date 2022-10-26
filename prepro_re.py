import re
import os

# a = 'uav_ ubv_ ;ucv_]uw 放大镜=看是；否打开 v_uz,v;_,uc 美好风景的房间 yt''v_uov[&123-456-789'
# text = re.sub('[^\u4e00-\u9fa5A-Za-z0-9 ]', '', a)#\u4e00-\u9fa5表示中文，A-Za-z0-9分别表示...
# print(text)

f1 = open('subj.subjective1', 'w', encoding='utf-8')

with open('subj.objective', 'r', encoding='utf-8') as f:
    for ii, line in enumerate(f):
        line = line.strip()
        text = re.sub('[^\u4e00-\u9fa5 A-Za-z0-9]', '', line)
        T = text+'\n'
        f1.write(T)
f1.close()
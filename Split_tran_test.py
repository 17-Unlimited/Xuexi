# 此代码是针对数据形式为“195:rated argo imdb”的.txt文件
#只需修改dataset和open（）打开的路径即可
from sklearn.model_selection import train_test_split
import os

dataset = "tweeter"

# if os.path.exists(r'dataset\%s' % (dataset))
os.mkdir(r'dataset/%s' % (dataset))
default_path = "dataset/"+dataset+"/"
train_path = default_path+dataset+"_train.txt"
dev_path = default_path+dataset+"_dev.txt"
test_path = default_path+dataset+"_test.txt"


feature_data = []
label_data = []
#读取特征和标签
with open('C:/Users/Administrator/Desktop/user/dataset/dataset/tweeter.tsv', 'r', encoding='utf-8') as f:
    for ii, line in enumerate(f):

        str = line.strip().split('\t')
        label = str[-1]
        text = str[0]
        feature_data.append(text)
        label_data.append(label)
#将数据进行划分
x_train, x_test, y_train, y_test = train_test_split(feature_data, label_data,test_size=0.20)
x_train, x_dev, y_train, y_dev = train_test_split(x_train, y_train,test_size=0.20)
#将训练集写入train.txt
f_w = open('%s' % train_path, 'w', encoding='utf-8')
i=0
for x_t in x_train:
    f_w.write(y_train[i] + ':' + x_t + '\n')
    i = i+1
f_w.close()
#将训练集写入dev.txt
f_w = open('%s' % dev_path, 'w', encoding='utf-8')
i=0
for x_t in x_dev:
    f_w.write(y_dev[i] + ':' + x_t + '\n')
    i = i+1
f_w.close()
#将测试集写入test.txt
f_w = open('%s' % test_path, 'w', encoding='utf-8')
i=0
for x_t in x_test:
    f_w.write(y_test[i] + ':' + x_t + '\n')
    i = i+1
f_w.close()

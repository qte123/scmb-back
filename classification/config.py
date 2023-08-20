# coding=utf-8
"""
配置文件，统一将所有可配值参数放在此配置文件中
参数主要包括：
数据集参数：batch_size、文件存放路径
训练参数：学习率、epoch
模型参数等
"""
import warnings
import torch as t
from common.config import common_trains

class DefaultConfig(object):
    env = "default"  # visdom环境
    vis_port = 8097  # visdom端口
    img_num = 1
    model = "ResNet34"  # 使用的模型

    train_data = './data/train/'
    trains = common_trains
    train_data_root = [train_data + trains[0] + '/',
                       train_data + trains[1] + '/',
                       train_data + trains[2] + '/',
                       train_data + trains[3] + '/',
                       train_data + trains[4] + '/',
                       train_data + trains[5] + '/']  # 训练集的各个路径

    test_data_root = "./data/test/"  # 测试集存放路径

    load_model = './checkpoints/'

    dir_path = 'classification/data/'

    load_model_path = [load_model + trains[0] + '/',
                       load_model + trains[1] + '/',
                       load_model + trains[2] + '/',
                       load_model + trains[3] + '/',
                       load_model + trains[4] + '/',
                       load_model + trains[5] + '/']  # 加载预训练的模型的路径，为None代表不加载

    model_name = ['dog_model_0304_17_53_33.pth', 'cat_model_0304_17_58_15.pth', 'horse_model_0304_18_02_58.pth',
                  'elephant_model_0304_18_07_40.pth', 'chicken_model_0304_18_12_23.pth',
                  'butterfly_model_0304_18_17_05.pth']

    # load_model_path = './checkpoints/model0303_18_41_55.pth'  # 加载预训练模型的路径，None表示不加载

    batch_size = 8  # batch_size
    use_gpu = True
    num_workers = 4
    print_freq = 50

    debug_file = ""
    result = './csv/'
    result_file = [result + 'result1.csv',
                   result + 'result2.csv',
                   result + 'result3.csv',
                   result + 'result4.csv',
                   result + 'result5.csv',
                   result + 'result6.csv']  # 测试文件

    # result_file = "./submission.csv"

    max_epoch = 120
    lr = 0.001
    lr_decay = 0.95
    weight_decay = 1e-4  # 损失函数

    """根据字典更新config参数，便于命令行更改参数"""

    def parse(self, kwargs):

        """更新配置参数"""
        for k, v in kwargs.items():
            if not hasattr(self, k):
                warnings.warn("Warning:opt has not attribut %s" % k)
            setattr(self, k, v)

        """打印配置信息"""
        print("user config:")
        for k, v in self.__class__.__dict__.items():
            if not k.startswith('__'):
                print(k, getattr(self, k))


opt = DefaultConfig()
"""
new_config = {'lr':0.1,'use_gpu':False}
opt.parse(new_config)
print "*************",opt.lr,opt.use_gpu
"""

# coding=utf-8
#模型测试

from classification.config import opt
import os
# import models
import torch as t
from classification.data.dataset import Test
from torch.utils.data import DataLoader
from torchnet import meter
from classification.utils.visualize import Visualizer
from torch.autograd import Variable
from torchvision import models
from torch import nn
import time
import csv
import shutil  # 导入移动模块

from images.images import add_img
from img_oss.oss_control import file_up
from img_oss.read_json import read_json


# 图片测试
def check(load_model_path, model_name, result_file, train_data, **kwargs):
    # opt.parse(kwargs)

    # data
    test_data = Test(opt.test_data_root, test=True)
    test_dataloader = DataLoader(test_data, batch_size=opt.batch_size, shuffle=False, num_workers=opt.num_workers)
    results = []

    # model
    model = models.resnet34(pretrained=True)
    model.fc = nn.Linear(512, 2)
    model.load_state_dict(t.load('classification/' + load_model_path + model_name))
    if opt.use_gpu:
        model.cuda()
    model.eval()

    for ii, (data, path) in enumerate(test_dataloader):
        input = Variable(data, volatile=True)
        if opt.use_gpu:
            input = input.cuda()
        score = model(input)
        path = path.numpy().tolist()
        # print path
        # print score.data,"+++++"
        _, predicted = t.max(score.data, 1)
        # print "***************"
        # print predicted
        predicted = predicted.data.cpu().numpy().tolist()
        res = ""
        for (i, j) in zip(path, predicted):
            if j == 1:
                res = train_data
            else:
                res = "none"
            results.append([i, "".join(res)])
    # print results

    write_csv(results, result_file)
    return results


""""""


def write_csv(results, file_name):
    with open('classification/' + file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'label'])
        writer.writerows(results)



def check_(train_data):
    trains = opt.trains
    load_model_path = opt.load_model_path
    model_name = opt.model_name
    result_file = opt.result_file
    for j in range(0, len(trains)):
        if train_data == trains[j]:
            return check(load_model_path[j], model_name[j], result_file[j], train_data)


# 开始测试
def start_test(username):
    res = []
    trains = opt.trains
    print('正在测试，请稍等')
    # import fire
    init_image_name(opt.dir_path + 'test')
    for i in range(0, len(trains)):
        for j in range(0, opt.img_num):
            if check_(trains[i])[j][1] != 'none':
                res.append(check_(trains[i])[j])
                if len(res) != 1:
                    newres = []
                    newres.append([res[0][0], 'none'])
                    res = newres
    classify(res, username)
    print(res)


# 图片分类
def classify(res, username):
    trains = opt.trains
    for i in range(0, len(trains)):
        if os.path.exists(opt.dir_path + 'img/' + trains[i] + '/'):
            shutil.rmtree(opt.dir_path + 'img/' + trains[i] + '/')  # 能删除该文件夹和文件夹下所有文件
            os.mkdir(opt.dir_path + 'img/' + trains[i] + '/')
        else:
            os.mkdir(opt.dir_path + 'img/' + trains[i] + '/')
    if os.path.exists(opt.dir_path + 'img/none/'):
        shutil.rmtree(opt.dir_path + 'img/none/')  # 能删除该文件夹和文件夹下所有文件
        os.mkdir(opt.dir_path + 'img/none/')
    else:
        os.mkdir(opt.dir_path + 'img/none/')
    for i in range(0, len(res)):
        move_img(res[i][1])
    for i in range(0, len(trains)):
        change_img_name(opt.dir_path + 'img/' + trains[i], trains[i], username)
    change_img_name(opt.dir_path + 'img/none', 'none', username)
    if os.path.exists(opt.dir_path + 'test/1.jpg'):
        os.remove(opt.dir_path + 'test/1.jpg')
    else:
        print("The file does not exist")


# 移动图片
def move_img(trains):
    # 移动目标文件的根目录
    # 移动操作
    shutil.copy(opt.dir_path + 'test/' + "1.jpg", opt.dir_path + 'img/' + trains + '/' + "1.jpg")


# 初始化test图片名称
def init_image_name(filepath):
    file_list = os.listdir(filepath)
    for i, fi in enumerate(file_list):
        old_dir = os.path.join(filepath, fi)
        filename = '1.' + str(fi.split(".")[-1])
        new_dir = os.path.join(filepath, filename)
        try:
            os.rename(old_dir, new_dir)
        except Exception as e:
            print(e)
            print("Failed!")
        else:
            print("Success!")


# 改变图片名称
def change_img_name(path, name, username):
    web=''
    file_list = os.listdir(path)
    for i, fi in enumerate(file_list):
        date = time.strftime('%Y_%m_%d_%H%M%S')
        old_dir = os.path.join(path, fi)
        filename = name + "_" + date + "." + str(fi.split(".")[-1])
        new_dir = os.path.join(path, filename)
        try:
            os.rename(old_dir, new_dir)
            file_up(path + '/', filename)
            osslist = read_json('img_oss/oss_setting.json')
            webpath = osslist['webpath']
            oss_user = osslist['oss_user']
            web = webpath + '/' + oss_user + '/' + filename
            type1 = 0
            classify1 = ''
            if path == 'classification/data/img/' + name:
                classify1 = name
            elif path == 'user/img_head':
                type1 = 1
            add_img(filename, web, type1, classify1, username)
        except Exception as e:
            print(e)
            print("Failed!")
        else:
            print("Success!")
    return web

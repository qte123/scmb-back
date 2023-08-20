# coding=utf-8
#模型训练

from classification.config import opt
import os
# import models
import torch as t
from classification.data.dataset import Train
from torch.utils.data import DataLoader
from torchnet import meter
from classification.utils.visualize import Visualizer
from torch.autograd import Variable
from torchvision import models
from torch import nn
import time

# 模型训练
def train(train_data_root, load_model_path, trains, **kwargs):
    """根据命令行参数更新配置"""
    # opt.parse(kwargs)
    print('正在训练' + trains)
    vis = Visualizer(opt.env)

    """(1)step1：加载网络，若有预训练模型也加载"""
    # model = getattr(models,opt.model)()
    model = models.resnet34(pretrained=True)
    model.fc = nn.Linear(512, 2)
    # if opt.load_model_path:
    #	model.load(opt.load_model_path)
    if opt.use_gpu:  # GPU
        model.cuda()
    """(2)step2：处理数据"""
    train_data = Train(train_data_root, train=True)  # 训练集
    val_data = Train(train_data_root, train=False)  # 验证集

    train_dataloader = DataLoader(train_data, opt.batch_size, shuffle=True, num_workers=opt.num_workers)
    val_dataloader = DataLoader(val_data, opt.batch_size, shuffle=False, num_workers=opt.num_workers)

    """(3)step3：定义损失函数和优化器"""
    criterion = t.nn.CrossEntropyLoss()  # 交叉熵损失
    lr = opt.lr  # 学习率
    optimizer = t.optim.SGD(model.parameters(), lr=opt.lr, weight_decay=opt.weight_decay)

    """(4)step4：统计指标，平滑处理之后的损失，还有混淆矩阵"""
    loss_meter = meter.AverageValueMeter()
    confusion_matrix = meter.ConfusionMeter(2)
    previous_loss = 1e10

    """(5)开始训练"""
    for epoch in range(opt.max_epoch):

        loss_meter.reset()
        confusion_matrix.reset()

        for ii, (data, label) in enumerate(train_dataloader):

            print("ii:", ii)
            # 训练模型参数
            input = Variable(data)
            target = Variable(label)

            if opt.use_gpu:
                input = input.cuda()
                target = target.cuda()

            # 梯度清零
            optimizer.zero_grad()
            score = model(input)

            loss = criterion(score, target)
            loss.backward()  # 反向传播

            # 更新参数
            optimizer.step()

            # 更新统计指标及可视化
            loss_meter.add(loss.item())
            # print score.shape,target.shape
            confusion_matrix.add(score.detach(), target.detach())

            if ii % opt.print_freq == opt.print_freq - 1:
                vis.plot('loss', loss_meter.value()[0])

                if os.path.exists(opt.debug_file):
                    import ipdb;
                    ipdb.set_trace()
        # model.save()
        name = time.strftime(trains + '_model_' + '%m%d_%H_%M_%S.pth')
        t.save(model.state_dict(), load_model_path + name)

        """计算验证集上的指标及可视化"""
        val_cm, val_accuracy = val(model, val_dataloader)
        vis.plot('val_accuracy', val_accuracy)
        vis.log("epoch:{epoch},lr:{lr},loss:{loss},train_cm:{train_cm},val_cm:{val_cm}".
                format(epoch=epoch, loss=loss_meter.value()[0], val_cm=str(val_cm.value()),
                       train_cm=str(confusion_matrix.value()), lr=lr))

        print("epoch:", epoch, "loss:", loss_meter.value()[0], "accuracy:", val_accuracy)

        """如果损失不再下降，则降低学习率"""
        if loss_meter.value()[0] > previous_loss:
            lr = lr * opt.lr_decay
            for param_group in optimizer.param_groups:
                param_group["lr"] = lr

        previous_loss = loss_meter.value()[0]


"""计算模型在验证集上的准确率等信息"""


@t.no_grad()
def val(model, dataloader):
    model.eval()  # 将模型设置为验证模式

    confusion_matrix = meter.ConfusionMeter(2)
    for ii, data in enumerate(dataloader):
        input, label = data
        val_input = Variable(input, volatile=True)
        val_label = Variable(label.long(), volatile=True)
        if opt.use_gpu:
            val_input = val_input.cuda()
            val_label = val_label.cuda()

        score = model(val_input)
        confusion_matrix.add(score.detach().squeeze(), label.long())

    model.train()  # 模型恢复为训练模式
    cm_value = confusion_matrix.value()
    accuracy = 100. * (cm_value[0][0] + cm_value[1][1]) / (cm_value.sum())

    return confusion_matrix, accuracy

def train_(train_data):
    train_data_root = opt.train_data_root
    trains = opt.trains
    load_model_path = opt.load_model_path
    for i in range(0, len(trains)):
        if train_data == trains[i]:
            train(train_data_root[i], load_model_path[i], trains[i])
            break


# 开始训练
def start_train():
    trains = opt.trains
    print('正在训练，请稍等')
    for i in range(0, len(trains)):
        train_(trains[i])

if __name__ == '__main__':#这个地方可以解决多线程的问题
    start_train()

from common.utils.jsonUtils import get_json, load_json


def dispatcherBase(request, action2HandlerTable):

    # # GET 请求 参数 在request 对象的GET属性中
    # if request.method == 'GET':
    #     request.params = request.GET
    # elif request.method in ['POST', 'PUT', 'DELETE']:
    #     # 根据接口，POST/PUT/DELETE 请求的消息体都是json格式
    #     request.params = load_json(request)

    # 根据不同的action分派给不同的函数进行处理
    print(request)
    action = request.POST.get('action')
    print(action)
    if action in action2HandlerTable:
        handlerFunc = action2HandlerTable[action]
        return handlerFunc(request)

    else:
        return get_json({'ret': 1, 'msg': 'action参数错误'})


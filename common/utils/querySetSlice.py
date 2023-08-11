from common.utils.common import TABLE_MAX_SIZE


# 分割查找集
def query_slice(queryset, index):
    if index != '':
        first = 0 + index * TABLE_MAX_SIZE
        final = (index + 1) * TABLE_MAX_SIZE
        return queryset[first:final]
    else:
        return queryset

#!/usr/bin/python
# _*_coding:utf-8 _*_
import json
import sys

reload(sys)
sys.setdefaultencoding('utf8')
title = {
    "系统名称": "systemName",
    "系统代码": "systemCode",
    "需求名称": "reqName",
    "需求代码": "reqCode",
    "提交人": "submitterName",
    "需求类型": "reqType",
    "需求状态": "reqStatus",
    "创建时间": "createDate",
    "计划上线时间": "planRealeaseTime",
    "订单状态存储": "orderStatusStore",
    "订单状态": "orderStatus",
    "订单代码": "orderCode",
    "不知道什么意思": "actId",
    "当前处理人": "dealMan"
}


def fileread(filepath):
    titletmp = []
    results = []
    for line in open(filepath):
        if len(titletmp) == 0:
            titletmp = line.replace('"', '').replace('\n', '').replace('\r', '').replace('\t', '').split(',')
        else:
            result = {}
            lines = line.replace('"', '').replace('\n', '').replace('\r', '').replace('\t', '').split(',')
            num = len(lines)
            i = 0
            for key in titletmp:
                if i <= num:
                    if title.has_key(key):
                        result[title[key]] = lines[i]
                        i = i + 1
                    else:
                        result[key] = lines[i]
                        i = i + 1
            results.append(result)
    with open(filepath + '.json', 'w') as fo1:
        fo1.write(json.dumps(results, ensure_ascii=False, sort_keys=True, indent=4))


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        i = 0
        for name in sys.argv:
            if i != 0:
                print sys.argv[i]
                fileread(sys.argv[i])
            i = i + 1

    print ("finish")

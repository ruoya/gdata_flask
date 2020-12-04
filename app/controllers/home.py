#encoding:utf-8
__author__ = 'yanghuihui'

from . import main


@main.route('/', methods=['GET', 'POST'])
def login():
    res = {"errno": 0, "message": "hello world"}
    return res


@main.route('/get_table_data', methods=['GET'])
def get_table_data():
    res = {'status':0, 'message':''}
    data = [{
        'date': '2016-05-02',
        'name': '王小虎111',
        'address': '上海市普陀区金沙江路 1518 弄'
      }, {
        'date': '2016-05-04',
        'name': '王小虎222',
        'address': '上海市普陀区金沙江路 1517 弄'
      }, {
        'date': '2016-05-01',
        'name': '王小虎333',
        'address': '上海市普陀区金沙江路 1519 弄'
      }, {
        'date': '2016-05-03',
        'name': '王小虎444',
        'address': '上海市普陀区金沙江路 1516 弄'
      }]
    res['data'] = data
    return res
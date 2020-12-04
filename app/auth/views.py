#encoding:utf-8
__author__ = 'yanghuihui'

from . import auth


@auth.route('/login', methods=['GET', 'POST'])
def login():
    print('login')
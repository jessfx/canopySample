import pymysql
import random
import math


def get_data():
    con = pymysql.connect(host='127.0.0.1', port=3306,
                          user='root', passwd='', db='network')
    cursor = con.cursor()
    sql = 'select * from table'
    cursor.execute(sql)
    dataSet = cursor.fetchall()
    return dataSet


def rand_cen(size):
    num = random.randint(0, size)
    return num


def canopy(dateSet=(), t):
    dateSet = list(dateSet)
    items = []
    while len(dateSet) != 0:
        num = rand_cen(len(dateSet))
        item = []
        cent = dateSet[num]
        item.append(cent)
        dateSet.remove(cent)
        for date in dateSet:
            length = 0
            for col in range(2, len(date)):
                length = length + (cent[col] - date[col]) * \
                    (cent[col] - date[col])
            length = math.sqrt(length)
            if length <= t:
                item.append(date)
                dateSet.remove(date)
        items.append(item)
    return items

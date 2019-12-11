from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery_project import app

@app.task
def add(x, y):
    return x + y

@app.task
def mul(x, y):
    return x * y

@app.task
def xsum(numbers):
    return sum(numbers)

@app.task
def test(idx) :
    import time
    time.sleep(4)

    print("finish" + str(idx))

    return "finish" + str(idx)

@app.task
def test2(idx) :
    for i in range(10000) :
        for j in range(10000) :
            continue

    for i in range(10000) :
        for j in range(10000) :
            continue

    for i in range(10000) :
        for j in range(10000) :
            continue

    return "22finish" + str(idx)
from __future__ import absolute_import, unicode_literals
from celery import shared_task

@shared_task
def add(x, y):
    return x + y

@shared_task
def mul(x, y):
    return x * y

@shared_task
def xsum(numbers):
    return sum(numbers)

@shared_task
def test() :
    for i in range(10000) :
        for j in range(10000) :
            continue

    for i in range(10000) :
        for j in range(10000) :
            continue

    for i in range(10000) :
        for j in range(10000) :
            continue

    return "finish"
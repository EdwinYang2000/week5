# -*- coding: utf-8 -*-

import sys
from pymongo import MongoClient
from bson import SON
import sys


def get_rank(user_id):
    client = MongoClient()
    db = client.shiyanlou
    contests = db.contests
    pipeline = [{"$group":{"_id":"$user_id", "score":{"$sum":"$score"},"submit_time":{"$sum":"$submit_time"}}},{"$sort": SON([("score",-1),("submit_time",1)])}]
    res = list(contests.aggregate(pipeline))
    n = 0
    for contest in res:
        n = n + 1
        if contest['_id'] == int(user_id):
            rank = n, score = contest['score'], submit_time = contest['submit_time']
            break

    return rank, score, submit_time

if __name__ == '__main__':

    #TODO
    if len(sys.argv) == 3:
        userdata = get_rank(user_id)
        print(userdata)
    else:
        print("Parameter Error")


    

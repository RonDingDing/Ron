#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from pprint import pprint

users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]
print('users: {}'.format(users))

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
# 比如说，元组 (0, 1) 表示 id 为 0 的数据科学家 Hero 和 id 为 1 的数据科学家 Dunn 是朋友。
print('friendships: {}'.format(friendships))

for user in users:
    user["friends"] = []

for i, j in friendships:
    users[i]["friends"].append(users[j])  # 把i加为j的朋友
    users[j]["friends"].append(users[i])  # 把j加为i的朋友


def number_of_friends(user):
    """how many friends does _user_have?"""
    return len(user["friends"])  # 列表friend_ids的长度


total_connections = sum(number_of_friends(user) for user in users)
print('total_connections: {}'.format(total_connections))

num_users = len(users)  # 列表users的长度
avg_connections = total_connections / num_users  # 2.4

num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
sorted(num_friends_by_id, key=lambda (user_id, num_friends): num_friends, reverse=True)
# 把它按照num_friends从最大到最小排序

# [(1, 3), (2, 3), (3, 3), (5, 3), (8, 3), (0, 2), (4, 2), (6, 2), (7, 2), (9, 1)]
print('num_friends_by_id: {}'.format(num_friends_by_id))


def friends_of_friend_ids_bad(user):
    # foaf朋友的朋友
    return [foaf["id"]
            for friend in user["friends"]  # 对每一位用户的朋友
            for foaf in friend["friends"]]  # 得到他们的朋友


print ([friend["id"] for friend in users[0]["friends"]])  # [1, 2]

print ([friend["id"] for friend in users[1]["friends"]])  # [0, 2, 3]

print [friend["id"] for friend in users[2]["friends"]]  # [0, 1, 3]

from collections import Counter


def not_the_same(user, other_user):
    """two users are not the same if they have different ids"""
    return user["id"] != other_user["id"]


def not_friends(user, other_user):
    """other_user is not a friend if he's not in user["friends"];
    that is, if he's not_the_same as all the people in user["friends"]"""
    return all(not_the_same(friend, other_user)
               for friend in user["friends"])


def friends_of_friend_ids(user):
    return Counter(foaf["id"]
                   for friend in user["friends"]  # 对我的每一位朋友
                   for foaf in friend["friends"]  # 计数他们的朋友
                   if not_the_same(user, foaf)  # 既不是我
                   and not_friends(user, foaf))  # 也不是我的朋友


print friends_of_friend_ids(users[3])  # Counter({0: 2, 5: 1})
Counter({0: 2, 5: 1})

# 按照兴趣找朋友
interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]  # 每个元素都是成对数据 (user_id, interest)


def data_scientists_who_like(target_interest):
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]


from collections import defaultdict

# 键是interest， 值是带有这个interest的user_id的列表
user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

print('user_ids_by_interest: {}'.format(user_ids_by_interest))
# defaultdict(<type 'list'>, {'Java': [0, 5, 9], 'neural networks': [7, 8], 'NoSQL': [1], 'Hadoop': [0, 9], 'Mahout': [7], 'Storm': [0], 'regression': [3, 4], 'statistics': [3, 6], 'probability': [3, 6], 'programming languages': [5], 'Python': [2, 3, 5], 'deep learning': [8], 'Haskell': [5], 'mathematics': [6], 'Spark': [0], 'numpy': [2], 'pandas': [2], 'artificial intelligence': [8], 'theory': [6], 'libsvm': [4], 'C++': [5], 'R': [3, 5], 'HBase': [0, 1], 'Postgres': [1], 'decision trees': [4], 'Big Data': [0, 8, 9], 'MongoDB': [1], 'scikit-learn': [2, 7], 'MapReduce': [9], 'machine learning': [4, 7], 'scipy': [2], 'statsmodels': [2], 'Cassandra': [0, 1]})


# 键是user_id， 值是对那些user_id的interest的列表
interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

print('interests_by_user_id: {}'.format(interests_by_user_id))


# 迭代这个用户的兴趣；针对这个用户的每一种兴趣，寻找这种兴趣的其他用户，并迭代；记录每一个用户在循环中出现的次数。
def most_common_interests_with(user):
    return Counter(interested_user_id
                   for interest in interests_by_user_id[user["id"]]
                   for interested_user_id in user_ids_by_interest[interest]
                   if interested_user_id != user["id"])


###########################################
# 每位用户的工资（ salary ）和作为数据科学家的工作年限 （ tenure ）

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

# 键是tenure， 值是对每一个tenure的salary的列表
salary_by_tenure = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

print('salary_by_tenure: {}'.format(salary_by_tenure))
# defaultdict(<type 'list'>, {6.5: [69000], 7.5: [76000], 6: [76000], 10: [83000], 8.1: [88000], 4.2: [63000], 0.7: [48000], 8.7: [83000], 1.9: [48000], 2.5: [60000]})

average_salary_by_tenure = {tenure: sum(salaries) / len(salaries)
                            for tenure, salaries in salary_by_tenure.items()}
print('average_salary_by_tenure: {}'.format(average_salary_by_tenure))


def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"


# 键是tenure bucket， 值是相应bucket的salary的列表
salary_by_tenure_bucket = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

print('salary_by_tenure_bucket: {}'.format(salary_by_tenure_bucket))
# defaultdict( < type'list' >, {'more than five': [83000, 88000, 76000, 69000, 76000, 83000], 'between two and five': [60000, 63000],'less than two': [48000, 48000]})

average_salary_by_bucket = {tenure_bucket: sum(salaries) / len(salaries) for tenure_bucket, salaries in
                            salary_by_tenure_bucket.iteritems()}
print('average_salary_by_bucket: {}'.format(average_salary_by_bucket))

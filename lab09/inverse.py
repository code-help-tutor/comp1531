WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
def inverse(d):
    '''
    Given a dictionary d, invert its structure such that values in d map to lists of keys in d. For example:
    >>> inverse({1: 'A', 2: 'B', 3: 'A'})
    {'A': [1, 3], 'B': [2]}
    '''
    new = {}
    for i in d.values():
        if i not in new:
            new[i] = []

    for i in d.items():
        new[i[1]].append(i[0])

    return new
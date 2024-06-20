def solution(want, number, discount):
    from collections import Counter

    want_dict = dict(zip(want, number)) #딕셔너리로
    want_length = len(discount)

    def matches(want_dict, current_window):
        for item in want_dict:
            if want_dict[item] != current_window.get(item, 0):
                return False
        return True

    current_window = Counter(discount[:10])
    valid_days = 0

    if matches(want_dict, current_window):
        valid_days += 1

    for i in range(10, want_length):
        current_window[discount[i - 10]] -= 1
        if current_window[discount[i - 10]] == 0:
            del current_window[discount[i - 10]]
        current_window[discount[i]] += 1
        if matches(want_dict, current_window):
            valid_days += 1

    return valid_days

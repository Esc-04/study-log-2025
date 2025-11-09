segments = [(1, 4), (2, 5), (6, 8), (7, 9)]

events = []

for s, e in segments:
    events.append((s, 1))   # 시작: +1
    events.append((e, -1))  # 끝: -1

events.sort()

active = 0
overlap_count = 0
in_overlap = False

for time, delta in events:
    active+=delta
    if active>=1:
        in_overlap=True
    else:
        in_overlap=False
    if in_overlap:
        overlap_count+=delta if delta>0 else 0


print(overlap_count)  # 겹친 "구간"의 개수만 출력!

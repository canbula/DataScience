prev_id_ = 0
for i in range(1000):
    id_ = id(i)
    diff = id_ - prev_id_
    s = "\n" if i % 5 == 0 else " "
    print(f"{i} >> {id_}:{diff}", end=s)
    if diff != 32 and i > 0:
        break
    prev_id_ = id_

def _back_off(slot_time, slot_max=None):
    collisions = 0
    while True:
        print((random.randint(0, 2 ** collisions - 1)) * slot_time)
        if not slot_max or collisions < slot_max:
                collisions += 1
        else:
            break

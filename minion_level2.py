def total_lambs(total_lambs):
    indx = 0
    gen_arr = [1]
    sti_arr = [1, 1]

# for generous offering
    for x in gen_arr:
        if sum(gen_arr) <= total_lambs:
            gen_arr.append(x * 2)
            if sum(gen_arr) > total_lambs:
                gen_arr.pop()


# for stingy offering
# constraint 2: indx + 1 != > indx*2
#    if (sti_arr[indx] + 1) < sti_arr[indx]:
# constraint 3: indx - 1 and indx - 2 != > indx
#    if (sti_arr[indx] - 1) + (sti_arr[indx] - 2) <= sti_arr[indx]:

# constraint 4: if there are enough lambs left over so another senior henchman
    # can be added while adhering to above constraints, it must be added
#    if tot >= sti_arr[-1:]:
#        senior = (sti_arr[-1:] * 2)
#        sti_arr.append(senior)
#        tot -= senior

#    sti_arr += [y for y in sti_arr if sti_arr[indx] + sti_arr[indx - 1] >= sti_arr[indx]]
#    for y in sti_arr:
#        if sum(sti_arr) <= total_lambs:
#            sti_arr.append(y + sti_arr[indx - 1])
#            lump = sti_arr[indx] + sti_arr[indx - 1]
#            sti_arr.append(lump)
#            indx += 1
    while sum(sti_arr) <= total_lambs:
        y = sti_arr[-1] + sti_arr[-2]
        sti_arr.append(y)
    if sum(sti_arr) > total_lambs:
        sti_arr.pop()
    return len(sti_arr) - len(gen_arr)

print(total_lambs(10))

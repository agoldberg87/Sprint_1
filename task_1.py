time = '1h 45m,360s,25m,30m 120s,2h 60s'

time_lst = time.split(',')
time_min_total = 0

for t in time_lst:
    time_lst_split = t.split() if ' ' in t else [t]
    time_min = 0

    for i in time_lst_split:
        if 'h' in i:
            i = int(i.replace('h','')) * 60
            time_min += i            
        elif 'm' in i:
            i = int(i.replace('m',''))
            time_min += i
        elif 's' in i:
            i = int(i.replace('s','')) / 60
            time_min += i
    time_min_total += time_min

print(time_min_total)
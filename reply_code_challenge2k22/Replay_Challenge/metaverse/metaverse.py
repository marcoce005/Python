def cal_num_of_concurrent_days(calendar, n, m):
    total_day = 0
    for c in range(0,m):
        single_day = 0
        for r in range(0,n):
            single_day += calendar[r][c]
        if single_day == n:
            total_day += 1
    return total_day

def generate_empty_calendar(n, m):
    calendar = []
    for i in range(0, n):
        player = [0 for element in range(m)]
        calendar.append(player)
    return calendar

def fill_calendar(n, m, play_freq, calendar):
    for idx,player in enumerate(play_freq):
        for day in range(1, m + 1, player):
            calendar[idx][day - 1] = 1
    return calendar

def process_input_file(fname):
    with open(fname, "r", encoding='utf8') as f:
        raw_lines = f.readlines()
        lines = [line.strip() for line in raw_lines]
        T = int(lines[0])
        with open("input-metaverse-c1b4_output.txt", "w", encoding='utf8') as outf:
            for i in range(T):
                N = int(lines[(i * 2) + 1].split()[0])
                M = int(lines[(i * 2) + 1].split()[1])
                raw_players = lines[(i * 2) + 2].split()
                players = [int(player) for player in raw_players]
                calendar = generate_empty_calendar(N, M)
                fill_calendar(N, M, players, calendar)
                concurr = cal_num_of_concurrent_days(calendar, N, M)
                outf.write("Case #{}: {}".format(i + 1, concurr))
                outf.write('\n')
            
process_input_file("input-metaverse-c1b4.txt")
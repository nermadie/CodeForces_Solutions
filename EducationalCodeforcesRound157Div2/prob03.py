# Torn Lucky Ticket
def get_require_num(ticket, shift):
    sum = 0
    sum_shift = 0
    n = len(ticket)
    for i in range(n):
        if i < n - shift:
            sum += int(ticket[i])
        else:
            sum_shift += int(ticket[i])
    if n // 2 >= shift:
        return sum - sum_shift if sum >= sum_shift else -1
    else:
        return sum_shift - sum if sum_shift >= sum else -1


def count_lucky_ticket_pairs(tickets):
    g1 = []
    g2 = []
    g3 = []
    g4 = []
    g5 = []
    group_1 = {}
    group_2 = {}
    group_3 = {}
    group_4 = {}
    group_5 = {}
    lucky_tickets = 0
    key = None
    for ticket in tickets:
        n = len(ticket)
        if n == 1:
            g1.append(ticket)
        elif n == 2:
            g2.append(ticket)
        elif n == 3:
            g3.append(ticket)
        elif n == 4:
            g4.append(ticket)
        else:
            g5.append(ticket)

    for ticket in g1:
        key = int(ticket)
        if key in group_1:
            group_1[key] += 1
        else:
            group_1[key] = 1
    for ticket in g2:
        key = get_require_num(ticket, 0)
        if key in group_2:
            group_2[key] += 1
        else:
            group_2[key] = 1
    for ticket in g3:
        key = get_require_num(ticket, 0)
        if key in group_3:
            group_3[key] += 1
        else:
            group_3[key] = 1

        key = get_require_num(ticket, 1)
        if key in group_1:
            lucky_tickets += group_1[key]
        key = get_require_num(ticket, 2)
        if key in group_1:
            lucky_tickets += group_1[key]
    for ticket in g4:
        key = get_require_num(ticket, 0)
        if key in group_4:
            group_4[key] += 1
        else:
            group_4[key] = 1

        key = get_require_num(ticket, 1)
        if key in group_2:
            lucky_tickets += group_2[key]
        key = get_require_num(ticket, 3)
        if key in group_2:
            lucky_tickets += group_2[key]
    for ticket in g5:
        key = get_require_num(ticket, 0)
        if key in group_5:
            group_5[key] += 1
        else:
            group_5[key] = 1

        key = get_require_num(ticket, 1)
        if key in group_3:
            lucky_tickets += group_3[key]
        key = get_require_num(ticket, 2)
        if key in group_1:
            lucky_tickets += group_1[key]
        key = get_require_num(ticket, 3)
        if key in group_1:
            lucky_tickets += group_1[key]
        key = get_require_num(ticket, 4)
        if key in group_3:
            lucky_tickets += group_3[key]

    for value in group_1.values():
        lucky_tickets += value * value
    for value in group_2.values():
        lucky_tickets += value * value
    for value in group_3.values():
        lucky_tickets += value * value
    for value in group_4.values():
        lucky_tickets += value * value
    for value in group_5.values():
        lucky_tickets += value * value
    return lucky_tickets


n = int(input())
tickets = input().split()

result = count_lucky_ticket_pairs(tickets)

print(result)

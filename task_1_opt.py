types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}


def remove_duplicates(tickets_dict):
    seen = set()
    for priority in tickets_dict.keys():
        new_list = [ticket for ticket in tickets_dict[priority] if ticket not in seen]
        tickets_dict[priority] = new_list
        seen.update(new_list)

def rename_keys(tickets_dict, types_dict):
    return {types_dict[key]: value for key, value in tickets_dict.items()}
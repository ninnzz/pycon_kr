data = [
    {
        'name': 'Naruto',
        'team': 7,
        'skill': 'bunshin'
    },
    {
        'name': 'Ino',
        'team': 4,
        'skill': 'mind transfer'
    },
    {
        'name': 'Sakura',
        'team': 7,
        'skill': 'strenght'
    },    
    {
        'name': 'hinata',
        'team': 2,
        'skill': 'byakugan'
    },    
    {
        'name': 'Neji',
        'team': 3,
        'skill': 'byakugan'
    },    
    {
        'name': 'Kiba',
        'team': 2,
        'skill': 'dogggo'
    },    
    {
        'name': 'Choji',
        'team': 4,
        'skill': 'expansion'
    },    
    {
        'name': 'Sasuke',
        'team': 7,
        'skill': 'sharingan'
    },
    {
        'name': 'Rock Lee',
        'team': 3,
        'skill': 'taijutsu'
    }
]


teams = []
temp_dict = {}

for row in data:
    if row['team'] not in temp_dict:
        temp_dict[row['team']] = {
            'members': [],
            'member_count': 0
        }

    temp_dict[row['team']]['members'].append(row)
    temp_dict[row['team']]['member_count'] += 1

for team in temp_dict.values():
    print(team)
    teams.append(team)

print(teams)
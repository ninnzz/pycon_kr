ninjas = [
    {
        'name': 'Naruto', 'team': 7, 'skill': 'bunshin'
    },
    {
        'name': 'Ino', 'team': 4, 'skill': 'mind transfer'
    },
    {
        'name': 'Sakura', 'team': 7, 'skill': 'strenght'
    },    
    {
        'name': 'hinata', 'team': 2, 'skill': 'byakugan'
    },    
    {
        'name': 'Neji', 'team': 3, 'skill': 'byakugan'
    },    
    {
        'name': 'Kiba', 'team': 2, 'skill': 'dogggo'
    },    
    {
        'name': 'Choji', 'team': 4, 'skill': 'expansion'
    },    
    {
        'name': 'Sasuke', 'team': 7, 'skill': 'sharingan'
    },
    {
        'name': 'Rock Lee', 'team': 3, 'skill': 'taijutsu'
    }
]

"""
# Transform data to this
[{
    'members': [
        { 'name': 'Naruto', 'team': 7, 'skill': 'bunshin' }, 
        { 'name': 'Sakura', 'team': 7, 'skill': 'strenght' }, 
        { 'name': 'Sasuke', 'team': 7, 'skill': 'sharingan' }
    ],
    'member_count': 3
}, {
    'members': [
        { 'name': 'Ino', 'team': 4, 'skill': 'mind transfer' }, 
        { 'name': 'Choji', 'team': 4, 'skill': 'expansion' }
    ],
    'member_count': 2
}, {
    'members': [
        { 'name': 'hinata', 'team': 2, 'skill': 'byakugan' }, 
        { 'name': 'Kiba', 'team': 2, 'skill': 'dogggo' }
    ],
    'member_count': 2
}, {
    'members': [
        { 'name': 'Neji', 'team': 3, 'skill': 'byakugan' }, 
        { 'name': 'Rock Lee', 'team': 3, 'skill': 'taijutsu' }
    ],
    'member_count': 2
}]
"""


teams = []

# Simulates order by in mysql
ninjas = sorted(ninjas, key=lambda x: x['team'])

current_team = None

for row in ninjas:
    if current_team != row['team']:
        current_team = row['team']
        teams.append({
            'members': [],
            'member_count': 0
        })

    index = len(teams) - 1
    teams[index]['members'].append(row)
    teams[index]['member_count'] += 1

print(teams)
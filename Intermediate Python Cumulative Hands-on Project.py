rarebirds = {
    'Gold-crested Toucan': {
        'Height (m)': 1.1,
        'Weight (kg)': 35,
        'Color': 'Gold',
        'Endangered': True,
        'Aggressive': True}
,
'Pearlescent Kingfisher': {
        'Height (m)': 0.25,
        'Weight (kg)': 0.5,
        'Color': 'White',
        'Endangered': False,
        'Aggressive': False}
,
'Four-metre Hummingbird': {
        'Height (m)': 0.6,
        'Weight (kg)': 0.5,
        'Color': 'Blue',
        'Endangered': True,
        'Aggressive': False}
,
'Giant Eagle': {
        'Height (m)': 1.5,
        'Weight (kg)': 52,
        'Color': 'Black and White',
        'Endangered': True,
        'Aggressive': True}
,
'Ancient Vulture': {
        'Height (m)': 2.1,
        'Weight (kg)': 70,
        'Color': 'Brown',
        'Endangered': False,
        'Aggressive': False}
}
birdlocation = [
    'In the canopy directly above our heads.',
    'Between my 6 and 9 o’clock above.',
    'Between my 9 and 12 o’clock above.',
    'Between my 12 and 3 o’clock above.',
    'Between my 3 and 6 o’clock above.',
    'In a nest on the ground.',
    'Right behind you.'
]
codes = {'HHH': 'In the canopy directly above our heads.',
    'HHT': 'Between my 6 and 9 o’clock above.',
    'HTH': 'Between my 9 and 12 o’clock above.',
    'THH': 'Between my 12 and 3 o’clock above.',
    'HTT': 'Between my 3 and 6 o’clock above.',
    'THT': 'In a nest on the ground.',
    'TTH': 'Right behind you.'}
actions = ['Back Away', 'Cover our Heads','Take a Photograph']
#print(rarebirds['Giant Eagle']['Aggressive'])
for k in rarebirds.keys():
    print('The name of the bird is: ' + k)
for k, v in codes.items():
    print(k +' - ' + v)
for k, v in rarebirds.items():
    v['Seen'] = False
    print(v)
rarebirdsList = list(rarebirds.keys())
print(rarebirdsList)
Encounter = True
while Encounter == True:
    Sighting = input('What do you see? ')
    if Sighting in rarebirdsList:
        print("This is one of the birds we're looking for.")
        break       
    else:
        print("That's not one of the birds we're looking for.")        
    continue
code = input("Where do you see it? ").upper()
location = codes[code]
print("So you've seen a", Sighting, location,'My goodness.')
for k, v in rarebirds.items():
    if k == Sighting:
        if v['Aggressive'] == True:
            print("It's aggressive. We need to", actions[0], "and", actions[1], ".")
            print(actions[2], "of the", Sighting , location)
        elif v['Endangered'] == True:
            print("It's endangered. We need to", actions[0], ".")
            print(actions[2], "of the", Sighting, location)
        else:
            print(actions[2], "of the ultra rare", Sighting, location)



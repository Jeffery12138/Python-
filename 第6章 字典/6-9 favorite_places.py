favorite_places = {
    'Lucy': ['Shanghai', 'Tokyo'],
    'Tom': ['Tokyo'],
    'Sarah': ['Paris', 'New York', 'London'],
    'Edward': ['Beijing'],
}
for name, places in favorite_places.items():
    if len(places) > 1:
        print("\n" + name.title() + "'s favorite places are:")
        for place in places:
            print("\t" + place)
    else:
        print("\n" + name.title() + "'s favorite place is:")
        print("\t" + places[0])
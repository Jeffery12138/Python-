def make_album(singer_name, album_name, songs_number=''):
    """返回一个字典，包含专辑信息"""
    album = {'singer_name': singer_name, 'album_name': album_name}
    if songs_number:
        album['songs_number'] = songs_number

    return album


while True:
    print("\nPlease tell me the info about your album:")
    print("(Enter 'q' at any time to quit)")
    singer_name = input("Singer name:")
    if singer_name == 'q':
        break
    album_name = input("Album name:")
    if album_name == 'q':
        break
    album = make_album(singer_name, album_name)
    print(album)
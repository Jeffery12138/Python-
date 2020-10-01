def make_album(singer_name, album_name, songs_number=''):
    """返回一个字典，包含专辑信息"""
    album = {'singer_name': singer_name, 'album_name': album_name}
    if songs_number:
        album['songs_number'] = songs_number

    return album


print(make_album('Jay', 'Sunday', 12))
print(make_album('Lily', 'COOL'))
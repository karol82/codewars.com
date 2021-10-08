def song_decoder(str):
    song_decoded = str.replace('WUB', ' ')
    song_decoded = song_decoded.strip()
    song_decoded = song_decoded.replace('   ', ' ')
    song_decoded = song_decoded.replace('  ', ' ')
    return song_decoded


song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
  # =>  WE ARE THE CHAMPIONS MY FRIEND
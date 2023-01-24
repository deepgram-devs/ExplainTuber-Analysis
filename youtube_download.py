import youtube_dl
'''
This comment contains the lists of videos that we will be parsing. Feel free to create your own lists!

#Vsauce
vsauce_vids = ['https://youtu.be/fXW-QjBsruE', 'https://youtu.be/_ArVh3Cj9rw', 'https://youtu.be/zHL9GP_B30E',
'https://youtu.be/U6VBV4QUMu0', 'https://youtu.be/egEraZP9yXQ', 'https://youtu.be/_WHRWLnVm_M', 'https://youtu.be/Xc4xYacTu-E', 'https://youtu.be/J51ncHP_BrY']

#CGP Grey
cgp_vids = ['https://youtu.be/jfOUVYQnuhw', 'https://youtu.be/qD6bPNZRRbQ', 'https://youtu.be/8Fn_30AD7Pk',
'https://youtu.be/qEV9qoup2mQ', 'https://youtu.be/9LMr5XTgeyI', 'https://youtu.be/_8xhdL8BPvU', 'https://youtu.be/-FBwZtuJtMw', 'https://youtu.be/pUF5esTscZI', 'https://youtu.be/qC5h9zcHmPA', 'https://youtu.be/thOifuHs6eY']

#veritasium
veritasium_vids = ['https://youtu.be/TILjzuBGkRc',
        'https://youtu.be/J_n1FZaKzF8',
        'https://youtu.be/pXoZQsZP2PY',
        'https://youtu.be/pir_muTzYM8',
        'https://youtu.be/esQyYGezS7c',
        'https://youtu.be/evUfG3lrk5U',
        'https://youtu.be/nmgFG7PUHfo',
        'https://youtu.be/16Ci_2bN_zc',
        'https://youtu.be/daaDuC1kbds',
        'https://youtu.be/5eW6Eagr9XA']

#Tom Scott
tom_vids = ['https://youtu.be/PSrO55KS6VY', 'https://youtu.be/2nQ-rijlX3o', 'https://youtu.be/FhHM9MT41IE',
          'https://youtu.be/t19wSDqf6qo', 'https://youtu.be/Wif1EAgEQKI', 'https://youtu.be/vIfC4Aj05Ps',
          'https://youtu.be/eMTZvA8iFgI', 'https://youtu.be/nCrTsWtPVIY', 'https://youtu.be/I99Qgb4mE5I', 'https://youtu.be/wbVIBmoUdUs']

#3blue
3blue_vids = ['https://youtu.be/KuXjwB4LzSA', 'https://youtu.be/851U557j6HE', 'https://youtu.be/cDofhN-RJqg',
          'https://youtu.be/VYQVlVoWoPY', 'https://youtu.be/bOXCLR3Wric', 'https://youtu.be/fRed0Xmc2Wg', 
          'https://youtu.be/v68zYyaEmEA', 'https://youtu.be/ltLUadnCyi0', 'https://youtu.be/LqbZpur38nw', 'https://youtu.be/-RdOwhmqP5s']

#nerdwriter
nerdwriter_vids = ['https://youtu.be/AAwbvGywdOc', 'https://youtu.be/MN-1jdFSDs8', 'https://youtu.be/S0C62-HzbwY', 'https://youtu.be/ww_lmtMpfqE',
         'https://youtu.be/jceCjCJlbi0',  'https://youtu.be/PoV9JyiUcTs', 'https://youtu.be/r20njl0plVU',
          'https://youtu.be/pUs9A10WbEI', 'https://youtu.be/ZRLcZTr6Z0Q', 'https://youtu.be/-H1c7C-hyAk']
'''

wendover_vids = ['https://youtu.be/qQTjLWIHN74', 'https://youtu.be/c3dDagZMALQ', 'https://youtu.be/Pm5bTZRhncY', 'https://youtu.be/AIqxfBhlwx0',
      'https://youtu.be/oL0umpPPe-8', 'https://youtu.be/GBp_NgrrtPM', 'https://youtu.be/YBNcYxHJPLE',
      'https://youtu.be/iIpPuJ_r8Xg', 'https://youtu.be/MY8AB1wYOtg', 'https://youtu.be/8xzINLykprA']


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    # change this to change the path you want your downloads to be located
    'outtmpl': './wendover/audio/%(title)s.mp3',
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(wendover_vids)
    print()
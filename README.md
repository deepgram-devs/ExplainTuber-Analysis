# ExplainTuber-Analysis

This repository contains four files to run in the following order:

1) youtube_download.py
2) deepgram_transcribe.py
3) create_pretty_transcripts.py
4) calculate_wpm.py

More specifically, `youtube_download.py` will take a Python list of YouTube links 
that you specified, and will download those links locally. Then, the `deepgram_transcribe.py`
file will output a json dump of the audio transcriptions of each of the videos. Then, 
`create_pretty_transcripts.py` will turn the json dumps into human-readable scripts. You will also get
to label the speakers by name when running this file. Finally, calculate_wpm.py will output the 
word counts of the hosts of each of the videos.

Check out this video for a full tutorial and demo of this code!

<img width="552" alt="Screen Shot 2023-06-06 at 7 48 44 AM" src="https://github.com/deepgram-devs/ExplainTuber-Analysis/assets/57232352/e711c12f-13c2-4192-aa37-b5c65f01c884">

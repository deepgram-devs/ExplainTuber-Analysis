import json
import os

# create transcripts
def create_transcripts():
    print('running create_transcripts')
    for filename in os.listdir("wendover/transcripts"):
        with open(f"wendover/transcripts/{filename}", "r") as file:
            transcript = json.load(file)
        paragraphs = transcript["results"]["channels"][0]["alternatives"][0]["paragraphs"]
        print(paragraphs['transcript'])
        with open(f"wendover/pretty_scripts/{filename[:-5]}.txt", "w") as f:
            for line in paragraphs['transcript']:
                f.write(line)

create_transcripts()

'''
This function gives you the ability to label your speakers by name.
When diarizing, the Deepgram API will label the speakers as 
Speaker 0, Speaker 1, Speaker 2, etc.

When this function is run, you'll one line from the transcript
for each individual speaker that the API identified during diarization.

You will then label the speaker of that line with the name that you desire.
'''
def assign_speakers():
    for filename in os.listdir("wendover/pretty_scripts"):
        print(f"Current File: {filename}")
        print()
        with open(f"wendover/pretty_scripts/{filename}", "r") as f:
            lines = f.readlines()
        spoken = []
        names = []
        for line in lines:
            if line.startswith("Speaker "):
                if line[0:9] in spoken:
                    continue
                print(line)
                print()
                name = input("Who is the Speaker? ")
                if len(name) <= 1:
                    continue
                spoken.append(line[:9])
                names.append(name)
                print()
        # print(spoken)
        # print(names)
        filedata = "\n".join(lines)
        print(filedata)
        for speaker, name in zip(spoken, names):
            filedata = filedata.replace(speaker, name)
        with open(f"wendover/pretty_scripts/{filename}", "w") as f:
            f.write(filedata)

assign_speakers()
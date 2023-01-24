from deepgram import Deepgram as DG
import asyncio, json, os

dg_key = 'Your key here'
dg = DG(dg_key)

options = {
    "diarize": True,
    "punctuate": True,
    "paragraphs": True,
    "numerals": True,
    "model": 'general',
    "tier": 'enhanced'
}

async def main():
    #Change this path as you need
    podcasts = os.listdir("./wendover/audio") 
    for podcast in podcasts:
        print("Currently processing:", podcast)
        #Change this path as you need
        with open(f"wendover/audio/{podcast}", "rb") as audio: 
            source = {"buffer": audio, "mimetype":'audio/mp3'}
            res = await dg.transcription.prerecorded(source, options)

            #Change this path as you need
            with open(f"wendover/transcripts/{podcast[:-4]}.json", "w") as transcript:
                json.dump(res, transcript)
    return

asyncio.run(main())
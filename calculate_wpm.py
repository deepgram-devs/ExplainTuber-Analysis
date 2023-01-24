import json
import os

youtuber = 'wendover'
main_char = 'wendover:'
others = ['1:', '2:', '3:', '4:', '5:', '6:', '7:', '8:', '9:', '0:']
words_per_minute = {}

#Calculate the word spoken only by the speaker we're currently analyzing. No guests.
def calculate_wpms():
    print('calculating wpms')

    #Change these paths as you need.
    for filename in os.listdir("wendover/pretty_scripts"):
        with open(f"wendover/pretty_scripts/{filename}", "r") as file:
            word_count = 0
            should_count = False # We only count the words of the host of the ExplainTube video.
            for line in file:
                words = line.split()
                if len(words) > 0:
                    if words[0] in others:
                        should_count = False
                    elif words[0] == main_char:
                        should_count = True
                        word_count += len(words) - 1
                    else:
                        if should_count:
                            word_count += len(words)
            print('word count: ', word_count)
            words_per_minute[filename] = word_count

    #Change this filename and path as you need.
    with open(f"wendover/words_per_minute.txt", 'w') as results:
        for title, word_count in words_per_minute.items():
                result = title[:-4] + '@' + str(word_count)
                results.write(result)
                results.write('\n')

calculate_wpms()
print(words_per_minute)
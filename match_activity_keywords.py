# import modules
import csv
import string
from nltk.tokenize import word_tokenize

# import list of categorical response keywords and create dictionary
file = open('activity_keywords.csv', 'r', encoding='utf-8-sig')
activities = list(csv.reader(file, delimiter=","))
file.close()
activities = [row[0] for row in activities]

# import 2022 sample data and count the categorical keywords present in every open response
with open('activities_sample2.csv', 'r', encoding='utf-8-sig') as fr, \
        open('activities_sample2_open_keyword_output.csv', 'w', encoding='utf-8-sig', newline='') as fw:
    reader = csv.reader(fr)
    writer = csv.writer(fw)

    next(fr)
    header = ['sample', 'PPID', 'quest', 'start', 'stop', 'MC', 'open', 'length', 'total']
    header.extend(activities)
    writer.writerow(header)

    for row in reader:
        sample = row[6]
        PPID = row[0]
        quest = row[1]
        start = row[2]
        stop = row[3]
        mc = row[4]
        text = row[5]
        text = text.translate(str.maketrans('', '', string.punctuation))
        tokens = [token for token in word_tokenize(text)]
        length = len(tokens)
        activities_dictionary = dict.fromkeys(activities, 0)
        for token in tokens:
            if token.lower() in activities_dictionary:
                activities_dictionary[token.lower()] += 1
        activity_counts = list(activities_dictionary.values())
        total = sum(activity_counts)

        to_write = [sample, PPID, quest, start, stop, mc, text, length, total]
        to_write.extend(activity_counts)
        writer.writerow(to_write)

# import 2022 sample data and count the categorical keywords present in every categorical response
with open('activities_sample2.csv', 'r', encoding='utf-8-sig') as fr, \
        open('activities_sample2_mc_keyword_output.csv', 'w', encoding='utf-8-sig', newline='') as fw:
    reader = csv.reader(fr)
    writer = csv.writer(fw)

    next(fr)
    header = ['sample', 'PPID', 'quest', 'start', 'stop', 'MC', 'open', 'length', 'total']
    header.extend(activities)
    writer.writerow(header)

    for row in reader:
        sample = row[6]
        PPID = row[0]
        quest = row[1]
        start = row[2]
        stop = row[3]
        mc = row[4]
        text = row[5]
        mc = mc.replace(",", ", ") # add space after commas so responses do not run together
        mc = mc.translate(str.maketrans('', '', string.punctuation))
        tokens = [token for token in word_tokenize(mc)]
        length = len(tokens)
        activities_dictionary = dict.fromkeys(activities, 0)
        for token in tokens:
            if token.lower() in activities_dictionary:
                activities_dictionary[token.lower()] += 1
        activity_counts = list(activities_dictionary.values())
        total = sum(activity_counts)

        to_write = [sample, PPID, quest, start, stop, mc, text, length, total]
        to_write.extend(activity_counts)
        writer.writerow(to_write)
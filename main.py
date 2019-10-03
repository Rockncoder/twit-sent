import collections
import multiprocessing as mp
import re
SAMPLE_TEXT = 'war-of-the-worlds.txt'

# Reading a simple natural language file into memory

# def process(line):
#     print(line)

# with open(SAMPLE_TEXT) as f:
#     data = f.readlines()  # everything in memory!
#     for line in data:
#         process(line)

# with open(SAMPLE_TEXT) as f:
#     # to handle large text files, we use the file as an iterator
#     for line in f:
#         # each line is garbage collected after the iteration
#         # unless it is referenced elsewhere.
#         process(line)

# pool = mp.Pool(2)  # no. of pools = no. of CPU cores
# jobs = []
#
# with open(SAMPLE_TEXT) as f:
#     for line in f:
#         jobs.append(
#             pool.apply_async(process, (line)))
#
# for job in jobs:
#     job.get()  # wait for all jobs to finish

# pool.close()

corpus = ("Andy is a data scientist. Andy's boss, Megan, was looking for him, "
          "but Andy was out to lunch. Megan texted Andy, 'How's the deadline"
          " coming along?'")

# Simply splitting the sentence with spaces
# print(corpus.split())

# Taking out punctuation
punctuation = ".',?"  # what is the universe of punctuation? How do we handle 's?
for p in punctuation:
    corpus = corpus.replace(p, '')

# print(corpus.split())

# Regex
word_regex = r'\W+'  # a raw str: one or more (+) non-word characters (\W)
split_corpus = re.split(word_regex, corpus)
# print(split_corpus)

# a better regex
# word character + zero or more word characters or 's + word character
# OR
# just a word character
word_regex_improved = r"(\w[\w']*\w|\w)"
word_matcher = re.compile(word_regex_improved)
# print(word_matcher.findall(corpus))


def split_into_words(line):
    word_regex_improved = r"(\w[\w']*\w|\w)"
    word_matcher = re.compile(word_regex_improved)
    return word_matcher.findall(line)

processed_corpus = []

with open("natural-language-data.txt") as f:
    # to handle large text files, we use the file as an iterator
    for line in f:
        processed_corpus.extend(split_into_words(line))

processed_corpus = [w.lower() for w in processed_corpus]

print(processed_corpus)


# Before stop word removal
word_counts = collections.Counter(processed_corpus)
print(word_counts)

# Define some stop words
stop_words = {
    'ourselves', 'hers', 'between', 'yourself', 'but', 'again',
    'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they',
    'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into',
    'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as',
    'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we',
    'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more',
    'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above',
    'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any',
    'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does',
    'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can',
    'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where',
    'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't',
    'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how',
    'further', 'was', 'here', 'than'}

# find least common elements
uncommon_words = word_counts.most_common()[:-10:-1]

processed_corpus = [w for w in processed_corpus if w not in stop_words]
processed_corpus = [w for w in processed_corpus if w not in uncommon_words]
print(processed_corpus)
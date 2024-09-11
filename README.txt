The following files are used to conduct analyses in Part I:

Impact of the categorical item on open-ended responses (2022 sample only):
- match_activity_keywords.py (Python script that counts the number of words in each open-ended response that match keywords from the categorical items)
- activity_keywords.csv (list of input keywords from categorical items used in above script; manually generated)

Describing vocabularies across samples:
- count_unique_activity_words.py (Python script that counts the number of unique activity words used in each sample/response format; NOTE that these counts must be separately summed across all rows in the output spreadsheets to generate total counts per sample/format)
- unique_activity_words.csv (list of unique words used across both open and categorical responses; generated using the freely-available software Basic Unit-Transposable Text Experimentation Resource [BUTTER version 0.9.4.1; Boyd, 2020])

Comparing response formats within the 2022 sample:
- compare_word_embeddings.ipynb (Jupyter notebook [Python] that gets word embeddings for open and categorical responses, calculates cosine distance for each pair)


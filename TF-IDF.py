import pandas as pd
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer
import csv

df = pd.read_csv('preprocess.csv')
text_data_column_name = df.columns[-1]
text_data = df[text_data_column_name]
df[text_data_column_name] = df[text_data_column_name].fillna('')
content = {}
categories_column_name = df.columns[0]
text_cate = df[categories_column_name].unique()


def split_into_sentences(contents):
    return sent_tokenize(contents)


output_file_path = 'TF-IDF.csv'
with open(output_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Category', 'Text', 'TF-IDF', 'Vocabulary'])

    for category in text_cate:
        filtered_content = df.loc[df[categories_column_name] == category, text_data_column_name].tolist()
        content[category] = filtered_content
        category_vocabulary = []

        # Khởi tạo vectorizer và tfidf_transformer ở đầu vòng lặp
        vectorizer = TfidfVectorizer()
        tfidf_transformer = TfidfTransformer()

        # Tạo danh sách tất cả các nội dung của category
        all_content_text = [content_text for content_text in content[category] if content_text]

        # Áp dụng TF-IDF cho toàn bộ nội dung của category
        X = vectorizer.fit_transform(all_content_text)
        X_tfidf = tfidf_transformer.fit_transform(X)
        vocabulary = vectorizer.get_feature_names_out()
        category_vocabulary.extend(vocabulary)
        print("TF-IDF:", X_tfidf)
        print("Vocabulary:", vocabulary)
        for sentence, tfidf_value in zip(all_content_text, X_tfidf):
            csv_writer.writerow([category, sentence, tfidf_value])
        # csv_writer.writerow([category, '', '', ', '.join(vocabulary)])

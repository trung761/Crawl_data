import pandas as pd
from nltk.tokenize import word_tokenize
import nltk
import unidecode
nltk.download('punkt')
nltk.download('stopword')
input_file = 'final.csv'
output_file = 'preprocess.csv'
stopwords_file = 'vietnamese-stopwords.txt'


with open(stopwords_file, 'r', encoding='utf-8') as file:
    stop_words_content = file.read()

# Tạo danh sách stopword từ nội dung đọc được
stop_words = set(word.strip() for word in stop_words_content.split('\n') if word.strip())


df = pd.read_csv(input_file)

def xoa_ky_tu_dac_biet(chuoi):
    chuoi_moi = ""
    for ky_tu in chuoi:
        if ky_tu.isalnum() or ky_tu.isspace():
            chuoi_moi += ky_tu
    return chuoi_moi

def preprocess_text(text):
    if pd.notna(text):
        text = xoa_ky_tu_dac_biet(text)
        text = text.lower()
        tokens = word_tokenize(text)
        tokens = [token for token in tokens if token not in stop_words]
        if not tokens:
            return ''

        processed_text = ' '.join(tokens)
        processed_text = unidecode.unidecode(processed_text)
        return processed_text
    else:
        return ''


def preprocess_text1(text):
    if pd.notna(text):
        text = text.lower()
        text = unidecode.unidecode(text)
        text = xoa_ky_tu_dac_biet(text)
        tokens = word_tokenize(text)
        processed_text = ' '.join(tokens)
        return processed_text
    else:
        return ''


last_column_name = df.columns[-1]
first_col_name = df.columns[0]
df[first_col_name] = df[first_col_name].apply(preprocess_text1)
df[last_column_name] = df[last_column_name].apply(preprocess_text)

df.to_csv(output_file, index=False, encoding='utf-8')

print('\n')
q = df[first_col_name].unique()
print(q)
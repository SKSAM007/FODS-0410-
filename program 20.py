import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import string
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    stop_words = set(stopwords.words('english'))
    tokens = text.split()
    text = ' '.join([word for word in tokens if word not in stop_words])
    return text

def plot_frequency_distribution(freq_dist, top_n):
    words, frequencies = zip(*freq_dist.most_common(top_n))
    plt.figure(figsize=(10, 6))
    plt.bar(words, frequencies, color='skyblue')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Top {} Most Frequent Words'.format(top_n))
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def main():
    df = pd.read_csv('data.csv')
    df['preprocessed_feedback'] = df['feedback'].apply(preprocess_text)
    all_words = ' '.join(df['preprocessed_feedback']).split()
    word_freq = Counter(all_words)
    while True:
        try:
            top_n = int(input("Enter the number of top frequent words you want to see: "))
            break
        except ValueError:
            print("Please enter a valid integer.")
    print("\nTop {} Most Frequent Words:".format(top_n))
    print("-" * 30)
    for word, freq in word_freq.most_common(top_n):
        print("{:<15} : {}".format(word, freq))
    plot_frequency_distribution(word_freq, top_n)

if __name__ == "__main__":
    main()

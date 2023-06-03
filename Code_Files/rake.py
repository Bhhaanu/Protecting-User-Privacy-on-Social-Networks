import nltk
from commonregex import CommonRegex
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

stop_words = set(stopwords.words('english'))
threshold = 3

def Rake(text):
    count = 0
    common_regex = CommonRegex(text)
    dates = common_regex.dates
    if len(dates) > 0: 
        count += 1
    if len(common_regex.times) > 0:
        count += 1
    if len(common_regex.phones) > 0:
        count += 1
    if len(common_regex.links) > 0:
        count += 1
    if len(common_regex.emails) > 0:
        count += 1
    if len(common_regex.credit_cards) > 0:
        count += 1
    if len(common_regex.street_addresses) > 0:
        count += 1
    if len(common_regex.zip_codes) > 0:
        count += 1
    tokens = word_tokenize(text)
    clean_tokens = [token for token in tokens if token.lower() not in stop_words]
    tagged = nltk.pos_tag(clean_tokens)
    nouns = [word for word, pos in tagged if pos.startswith('N')]
    if len(nouns) >= threshold:
        print(nouns)
        count += 1
    if count >= 1:
        return True
    else:
        return False

if __name__ == '__main__':
    Rake("My contact number is 9807275623")

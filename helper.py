import bs4 as bs
import re
import urllib.request
import nltk
import heapq
nltk.download('stopwords')
nltk.download('punkt')
def get_output(url):
	source = urllib.request.urlopen(url).read()
	soup = bs.BeautifulSoup(source,'lxml')
	text = ""
	for paragraph in soup.find_all('p'):
    		text += paragraph.text
	text = re.sub(r'\[[0-9]*\]',' ',text)
	text = re.sub(r'\s+',' ',text)
	clean_text = text.lower()
	clean_text = re.sub(r'\W',' ',clean_text)
	clean_text = re.sub(r'\d',' ',clean_text)
	clean_text = re.sub(r'\s+',' ',clean_text)
	sentences = nltk.sent_tokenize(text)
	stop_words = nltk.corpus.stopwords.words('english')
	word2count = {}
	for word in nltk.word_tokenize(clean_text):
    		if word not in stop_words:
        		if word not in word2count.keys():
            			word2count[word] = 1
        		else:
            			word2count[word] += 1
	max_count = max(word2count.values())
	for key in word2count.keys():
    		word2count[key] = word2count[key]/max_count
	sent2score = {}
	for sentence in sentences:
    		for word in nltk.word_tokenize(sentence.lower()):
        		if word in word2count.keys():
            			if len(sentence.split(' ')) < 25:
                			if sentence not in sent2score.keys():
                    				sent2score[sentence] = word2count[word]
                			else:
                    				sent2score[sentence] += word2count[word]
	best_sentences = heapq.nlargest(5, sent2score, key=sent2score.get)
	return best_sentences
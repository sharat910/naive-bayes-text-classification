from helper import tokenize,count_words
import operator
from nltk.corpus import stopwords

class Classifier(object):
    def __init__(self, categories):
        self.vocab = {}
        self.categories = categories
        self.word_counts = {}
        self.prior_counts = {}
        self.prior_probs = {}        
        
        for category in categories:
            self.word_counts[category] = {}
            self.prior_counts[category] = 0.
            self.prior_probs[category] = 0.

    def train(self, data,category):        
        self.prior_counts[category] += 1        
        words = tokenize(data)
        count_dict = count_words(words)
        for word, count in count_dict.items():
            if word not in self.vocab:
                self.vocab[word] = 0.0 # use 0.0 here so Python does "correct" math
            if word not in self.word_counts[category]:
                self.word_counts[category][word] = 0.0
            self.vocab[word] += count
            self.word_counts[category][word] += count
        self.update_prior_prob()

    def update_prior_prob(self):
        for key in self.prior_probs.keys():
            self.prior_probs[key] = self.prior_counts[key]/sum(self.prior_counts.values())

    def test(self, data):
        words = tokenize(data)
        count_dict = count_words(words)
        p_abstract_given = self.init_p_abstract_given_category()
        
        for w, cnt in count_dict.items():
            #if w in stopwords:
             #   continue            
            p_w_given = self.calc_p_w_given_category(w)
            for category in self.categories:
                p_abstract_given[category] *= p_w_given[category]**cnt
        
        posterior_prob = self.calc_posterior_prob(p_abstract_given)
	print posterior_prob
        predicted_category = max(posterior_prob.iteritems(), key=operator.itemgetter(1))[0]
        return predicted_category

    def calc_p_w_given_category(self, w):
        p_w_given = {}
        for category in self.categories:
            p_w_given[category] =  (self.word_counts[category].get(w, 0.0) + 1) / (sum(self.word_counts[category].values()) + sum(self.vocab.values()) + 1)
        return p_w_given

    def init_p_abstract_given_category(self):
        p_abstract_given = {}
        for category in self.categories:
            p_abstract_given[category] = 1
        return p_abstract_given

    def calc_posterior_prob(self, p_abstract_given):
        posterior_prob = {}
        for category in self.categories:
            posterior_prob[category] = p_abstract_given[category]*self.prior_probs[category]
        return posterior_prob

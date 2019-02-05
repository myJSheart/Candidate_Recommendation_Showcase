""" Recommend candidates for a project
"""
# all imports go here
import spacy
from gensim.summarization.bm25 import BM25
from .utils import text2tokens


class RecommendCandidate:
    def __init__(self, candidates):
        self.candidates = candidates
        self.load_nlp()
        self.load_bm25()


    def load_nlp(self):
        self.nlp = spacy.load('en_core_web_lg')


    def load_bm25(self):
        """ Convert the description of candidates into corpus and load the corpus into a bm25 object, which is used for keyword ranking.
        """
        self.corpus = []
        for candidate in self.candidates:
            self.corpus.append(text2tokens(candidate['description']))
        self.bm25 = BM25(self.corpus)
        self.average_idf = sum(float(val) for val in self.bm25.idf.values()) / len(self.bm25.idf)


    def keyword_ranking(self, title):
        """ Search required title (e.g., web developer) in candidates description

        Args:
            title (str): the job that required by project
        """
        scores = self.bm25.get_scores(title, self.average_idf)
        return scores


    def semantic_similarity(self, requirement):
        """ Calculate the semantic similarity between two documents

        Args:
            requirement (str): the requirement of project
        """
        scores = []
        doc1 = self.nlp(requirement)
        for candidate in self.candidates:
            doc2 = self.nlp(candidate['description'])
            scores.append(doc1.similarity(doc2))
        return scores


    def find_candidates(self, project):
        """ calculate scores for every candidate for the given project

        Args:
            project (dict): a dict of project
        """
        # calculate the scores based on the job title
        title_scores = []
        if project['title']:
            title_scores = self.keyword_ranking(project['title'])

        # calculate the description and requirement similarity score
        description_scores = []
        if project['requirement']:
            description_scores = self.semantic_similarity(project['requirement'])

        if title_scores and description_scores:
            return [x + y for (x, y) in list(zip(title_scores, description_scores))]
        elif title_scores:
            return title_scores
        elif description_scores:
            return description_scores
        else:
            return 

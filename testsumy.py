from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from JanomeToken import corpus
from JanomeToken import sentences

parser = PlaintextParser.from_string("".join(corpus), Tokenizer("japanese"))

summarizer = LexRankSummarizer()
summarizer.stop_words = [" "]

summary = summarizer(document=parser.document, sentences_count=2)

for sentence in summary:
    print(sentences[corpus.index(sentence.__str__())])
    
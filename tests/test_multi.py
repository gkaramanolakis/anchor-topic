MAX_VOCAB = 50
MAX_DF = 10
K = 5
THRESHOLD = 0.1
SEED = 1 
TOP = 5

def test_init(toy_multimodel):
    assert toy_multimodel.n_topics == K
    assert toy_multimodel.seed == SEED
    assert toy_multimodel.model1.anchors is None
    assert toy_multimodel.model2.anchors is None
    assert toy_multimodel.model1.word_topic is None
    assert toy_multimodel.model2.word_topic is None
    assert toy_multimodel.model1.doc_threshold == 1
    assert toy_multimodel.model2.doc_threshold == 0

def test_find_anchors(toy_multimodel):
    toy_multimodel.find_anchors()
    assert len(toy_multimodel.model1.anchors) == toy_multimodel.n_topics
    assert len(toy_multimodel.model2.anchors) == toy_multimodel.n_topics
    toy_multimodel.get_anchors(word=True, show=True)

def test_update_topics(toy_multimodel):
    toy_multimodel.update_topics()
    assert toy_multimodel.model1.word_topic.shape == (MAX_VOCAB, K)
    assert toy_multimodel.model2.word_topic.shape == (MAX_VOCAB, K)
    toy_multimodel.get_top_topic_words(TOP, word=True, show=True)


def test_tandem_update(toy_multimodel):
    anchors = [[1,3,4],[15,6,2],[11],[13,14],[29,45]]
    toy_multimodel.update_topics(anchors, anchors)
    toy_multimodel.get_anchors(word=True, show=True)
    assert toy_multimodel.model1.word_topic.shape == (MAX_VOCAB, K)
    assert toy_multimodel.model2.word_topic.shape == (MAX_VOCAB, K)
    toy_multimodel.get_top_topic_words(TOP, word=True, show=True)


from  main import DirectedGraphProcessor

setup_graph = DirectedGraphProcessor()
setup_graph.create_directed_graph('2.txt')

def test_query_bridge_words_not_in_graph():
    assert setup_graph.query_bridge_words("dog", "cat") == 'NOT_IN'

def test_query_bridge_words_in_cache():
    setup_graph.query_bridge_words("apple", "banana")
    assert setup_graph.query_bridge_words("apple", "banana") == ["orange","pear"]

def test_query_bridge_words_with_bridge():
    setup_graph.bridge_word = {}
    assert setup_graph.query_bridge_words("apple", "banana") == ["orange","pear"]

def test_query_bridge_words_no_bridge():
    setup_graph.bridge_word = {}
    assert setup_graph.query_bridge_words("orange", "pear") == []
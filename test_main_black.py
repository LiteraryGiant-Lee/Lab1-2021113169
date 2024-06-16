from  main import DirectedGraphProcessor

processor = DirectedGraphProcessor()
processor.create_directed_graph('2.txt')

def test_existing_one_bridge_word():
    assert  processor.query_bridge_words( "orange","apple") == ["banana"]

def test_existing_more_bridge_word():
    assert processor.query_bridge_words("apple", "banana") == ["orange","pear"]

def test_no_bridge_word():
    assert processor.query_bridge_words("orange", "pear") == []

def test_word_not_in_graph():
    assert processor.query_bridge_words("dog", "cat") == 'NOT_IN'

def test_same_word():
    assert processor.query_bridge_words("apple", "apple") == []
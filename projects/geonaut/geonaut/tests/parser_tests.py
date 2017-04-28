from nose.tools import *
from geonaut.parser import *
from geonaut.lexicon import *
from copy import deepcopy
from pprint import pprint


# construct a test set that consists of a list of named tuples
input_list = [ scan('south'), scan('door'), scan('go'), scan('to'),
                      scan('234'), scan('error123'), scan('the east door'), scan('go to east'),
                      scan('bear go to the door'), scan('the princess kill 10 bears') 
                    ]

def test_peek():
    #peek returns item [0] from a list. Pass a single item list.
    for i in range(len(input_list)):
        test_list = input_list[i]
        assert_equal(peek(test_list), test_list[0][0])


def test_match():
    #deepcopy, to allow list.pop, and preserve master_input_list
    correct_types = ('direction', 'noun', 'verb', 'stop', 'number', 'error',
               'stop', 'verb', 'noun', 'stop', None)
    word_list = deepcopy(input_list)
    right_list = deepcopy(input_list)
    for i in range(len(input_list)):
        assert_equal(match(word_list[i], correct_types[i]), right_list[i][0])

def test_skip():
    ''' test skip function '''
    word_type = 'verb'
    word_list = [['verb','go'],['verb','feel'],['noun','dog'],['verb','do'],['verb','be'],['noun','cat'],['verb','buy']]
    skipped_list = [['noun', 'dog'], ['verb', 'do'], ['verb', 'be'], ['noun', 'cat'], ['verb', 'buy']]
    skip(word_list,word_type)
    assert_equal(word_list,skipped_list)

def test_parse_verb():
    ''' test parse_verb function '''
    parser = Parser()
    # test good situations
    word_list =  [['stop', 'from'], ['stop', 'to'], ['verb', 'go']]
    expected_list = ['verb', 'go']
    assert_equal(parser.parse_verb(word_list),expected_list)
    
    # test bad situations
    bad_word_list =  [['stop', 'from'], ['stop', 'to'], ['direction', 'south']]
    assert_raises(ParserError, parser.parse_verb,bad_word_list)

def test_parse_object():
    ''' test parse_verb function '''
    parser = Parser()
    # passing test = list only contains stops, nouns & directions
    word_list =  [['stop', 'from'], ['stop', 'to'], ['noun', 'dog']]
    expected_list = ['noun', 'dog']
    assert_equal(parser.parse_object(word_list),expected_list)
    
    # failing test = list contains verb (i.e. not noun or direction)
    bad_word_list =  [['stop', 'from'], ['stop', 'to'], ['verb', 'go']]
    assert_raises(ParserError, parser.parse_object,bad_word_list)

def test_parse_subject():
    ''' test parse_subject function '''
    parser = Parser()
    
    word_list =  [['stop', 'from'], ['stop', 'to'], ['verb', 'go'],['stop', 'from'], ['stop', 'to'], ['noun', 'dog']]
        
    subj = 'bear'
    expected_verb = ['verb', 'go']
    expected_noun = ['noun', 'dog']
    expected_sentence = Sentence(subj,expected_verb,expected_noun)

    sentence = parser.parse_subject(word_list,subj)
    assert_equal(sentence.verb, "go")


def test_parse_sentence():
    ''' test parse_sentence function '''
    parser = Parser()

    word_list =  [['noun', 'dog'], ['verb', 'eat'],['stop', 'to'], ['noun', 'dog'],['stop', 'from'], ['stop', 'to'], ['noun', 'dog']]
    sentence = parser.parse_sentence(word_list)
    assert_equal(sentence.object, "dog")

    word_list =  [['verb', 'go'], ['noun', 'dog'],['stop', 'to'], ['noun', 'dog'],['stop', 'from'], ['stop', 'to'], ['noun', 'dog']]
    sentence = parser.parse_sentence(word_list)
    assert_equal(sentence.subject, "player")

    word_list =  [['number', '123'],]
    assert_raises(ParserError, parser.parse_sentence,word_list)

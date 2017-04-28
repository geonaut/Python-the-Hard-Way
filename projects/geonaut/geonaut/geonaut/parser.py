class ParserError(Exception):
    pass

class Sentence(object):

    def __init__(self, subject, verb, object):
        # remember we take ('noun','princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = object[1]


def peek(word_list):
    """A function to return the first item in a nested list or tuple.

    Args:
        word_list (tuple/list): Tuple or list containing lists eg (['verb', 'go'], ['noun', 'dog'])

    Returns:
        word (str): The first value in the nested list or tuple eg (('returned','xxx'),('xxx','xxx'))

    """
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None


def match(word_list, expecting):
    """A function to remove an item from a list, match it against a value, and return if matched

    Args:
        word_list (list): List containing lists eg (['verb', 'go'], ['noun', 'dog'])
        expecting (str): The word type, as a string eg 'verb'

    Returns:
        word (list): Returns the containing list eg ['verb', 'go']

    """
    if word_list:
        # notice the pop function here
        word = word_list.pop(0)
        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None


def skip(word_list, word_type):
    """ A function to remove words of a specified type from a tuple containing lists. Uses while, so will iterate until it reaches a word of a different type
    
    Args:
        word_list (list): List containing lists eg (['verb', 'go'], ['noun', 'dog'])
        word_type (str): Word type eg 'verb'

    """
    while peek(word_list) == word_type:
        # remove words that belongs to word_type from word_list
        match(word_list, word_type)


class Parser(object):

    def parse_verb(self, word_list):
        print word_list
        skip(word_list, 'stop')
 
        if peek(word_list) == 'verb':
            return match(word_list, 'verb')
        else:
            raise ParserError("Expected a verb next")


    def parse_object(self, word_list):
        skip(word_list, 'stop')
        next = peek(word_list)

        if next == 'noun':
            return match(word_list, 'noun')
        if next == 'direction':
            return match(word_list, 'direction')
        else:
            raise ParserError("Expected a noun or direction next.")


    def parse_subject(self, word_list, subj):
        verb = self.parse_verb(word_list)
        obj = self.parse_object(word_list)
        print subj
        return Sentence(subj, verb, obj)


    def parse_sentence(self, word_list):
        skip(word_list, 'stop')

        start = peek(word_list)

        if start == 'noun':
            print "NOUN"
            subj = match(word_list, 'noun')
            # print word_list
            print subj
            return self.parse_subject(word_list, subj)
        elif start == 'verb':
            print "VERB"
            # assume the subject is the player then
            return self.parse_subject(word_list, ('noun', 'player'))
        else:
            raise ParserError("Must start with subject, object, or verb not: %s" % start)

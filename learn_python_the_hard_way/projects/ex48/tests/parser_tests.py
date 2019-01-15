from nose.tools import *
from ex48 import parser

def test_peek():
  result = parser.peek([('verb', 'run')])
  assert_equal(result, 'verb')

def test_peek_with_none():
  result = parser.peek(None)
  assert_equal(result, None)

def test_match():
  wordlist = [('verb', 'run')]
  result = parser.match(wordlist, 'verb')
  assert_equal(result, ('verb', 'run'))
  assert_equal(wordlist, [])

def test_match_with_none():
  result = parser.match(None, 'verb')
  assert_equal(result, None)

def test_match_with_no_matches():
  wordlist = [('noun', 'bear')]
  result = parser.match(wordlist, 'verb')
  assert_equal(result, None)
  assert_equal(wordlist, [])

def test_skip():
  wordlist = [('stop', 'the'), ('noun', 'bear')]
  result = parser.skip(wordlist, 'stop')
  assert_equal(result, None)
  assert_equal(wordlist, [('noun', 'bear')])

def test_skip_with_no_matches():
  wordlist = [('stop', 'the')]
  result = parser.skip(wordlist, 'noun')
  assert_equal(result, None)
  assert_equal(wordlist, [('stop', 'the')])

def test_parse_verb():
  wordlist = [('stop', 'the'), ('verb', 'run')]
  result = parser.parse_verb(wordlist)
  assert_equal(result, ('verb', 'run'))
  assert_equal(wordlist, [])

def test_parse_verb_with_exception():
  wordlist = [('stop', 'the'), ('noun', 'bear')]
  assert_raises(parser.ParserError, parser.parse_verb, wordlist)

def test_parse_subject():
  wordlist = [('stop', 'the'), ('noun', 'bear')]
  result = parser.parse_subject(wordlist)
  assert_equal(result, ('noun', 'bear'))
  assert_equal(wordlist, [])

  wordlist = [('stop', 'the'), ('verb', 'run')]
  result = parser.parse_subject(wordlist)
  assert_equal(result, ('noun', 'player'))
  assert_equal(wordlist, [('verb', 'run')])

def test_parse_subject_with_exception():
  wordlist = [('stop', 'the'), ('direction', 'north')]
  assert_raises(parser.ParserError, parser.parse_subject, wordlist)

def test_parse_object():
  wordlist = [('stop', 'the'), ('noun', 'bear'), ('direction', 'north')]
  result = parser.parse_object(wordlist)
  assert_equal(result, ('noun', 'bear'))
  assert_equal(wordlist, [('direction', 'north')])
  result = parser.parse_object(wordlist)
  assert_equal(result, ('direction', 'north'))
  assert_equal(wordlist, [])

def test_parse_object_raises_exception():
  wordlist = [('stop', 'the'), ('verb', 'run')]
  assert_raises(parser.ParserError, parser.parse_object, wordlist)

def test_parse_sentence():
  wordlist = [('verb', 'run'), ('direction', 'north')]
  result = parser.parse_sentence(wordlist)
  assert_equal(result.__class__, parser.Sentence)
  assert_equal(result.subject, 'player')
  assert_equal(result.verb, 'run')
  assert_equal(result.object, 'north')

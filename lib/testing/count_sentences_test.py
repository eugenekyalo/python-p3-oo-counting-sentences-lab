import io
import sys
from count_sentences import MyString

def test_value_string():
    '''prints "The value must be a string." if not string.'''
    captured_out = io.StringIO()
    sys.stdout = captured_out
    string = MyString(123)  # Initialize MyString with an integer value
    sys.stdout = sys.__stdout__
    assert captured_out.getvalue() == "The value must be a string.\n"

def test_is_sentence():
    '''returns True if value ends with a period and False otherwise.'''
    assert MyString("Hello World.").is_sentence() == True

def test_is_question():
    '''returns True if value ends with a question mark and False otherwise.'''
    assert MyString("Is anybody there?").is_question() == True

def test_is_exclamation():
    '''returns True if value ends with an exclamation mark and False otherwise.'''
    assert MyString("It's me!").is_exclamation() == True

def test_count_sentences():
    '''returns the number of sentences in the value.'''
    simple_string = MyString("one. two. three?")
    assert simple_string.count_sentences() == 3

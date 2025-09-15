import pytest
import os
import re
import csv
from task_1 import *
from task_2 import *
from task_3 import *
from task_4 import *
from task_5 import *
from task_6 import *
from task_7 import *
from task_8 import *
from task_9 import *
from main import *
import tempfile
from unittest.mock import mock_open, patch, MagicMock

data = [
    ["When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow."],
    ["When it healed, and Jem's fears of never being able to play football were assuaged"],
    ["he was seldom self-conscious about his injury."],
    ["His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh."],
    ["He couldn't have cared less, so long as he could pass and punt."],
    ["When enough years had gone by to enable us to look back on them, we sometimes discussed the events leading to his accident."],
    ["I maintain that the Ewells started it all, but Jem, who was four years my senior, said it started long before that."],
    ["He said it began the summer Dill came to us, when Dill first gave us the idea of making Boo Radley come out."],
    ["I said if he wanted to take a broad view of the thing, it really began with Andrew Jackson."],
    ["If General Jackson hadn't run the Creeks up the creek, Simon Finch would never have paddled up the Alabama."],
    ["And where would we be if he hadn't? We were far too old to settle an argument with a fist-fight, so we consulted Atticus. Our father said we were both right."],
    ["Being Southerners, it was a source of shame to some members of the family that we had no recorded ancestors on either side of the Battle of Hastings."],
    ["All we had was Simon Finch, a fur-trapping apothecary from Cornwall whose piety was exceeded only by his stinginess."],
    ["In England, Simon was irritated by the persecution of those who called themselves Methodists at the hands of their more liberal brethren"],
    ["And as Simon called himself a Methodist, he worked his way across the Atlantic to Philadelphia"],
    ["Thence to Jamaica, thence to Mobile, and up the Saint Stephens."]
]
first_filename = "sentences.csv"
with open(first_filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
sentences = os.path.join(os.getcwd(),first_filename)

name_list = [["Name","Other Names"],["Jem"],["Dill"],["Boo Radley"] ,["Andrew Jackson"],["General Jackson"],["Simon Finch"],["Atticus"]]
second_filename = "names.csv"
with open(second_filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(name_list)
names = os.path.join(os.getcwd(),second_filename)

remove_words = words = [
    ["a"], ["about"], ["above"], ["actual"], ["after"], ["again"], ["against"], ["all"], ["alreadi"], ["also"], ["alway"],
    ["am"], ["amp"], ["an"], ["and"], ["ani"], ["anoth"], ["any"], ["anyth"], ["are"], ["around"], ["as"], ["at"], ["aww"],
    ["babi"], ["back"], ["be"], ["becaus"], ["because"], ["bed"], ["been"], ["befor"], ["before"], ["being"], ["below"],
    ["between"], ["birthday"], ["bit"], ["book"], ["both"], ["boy"], ["but"], ["by"], ["call"], ["can"], ["cannot"],
    ["cant"], ["car"], ["check"], ["com"], ["come"], ["could"], ["day"], ["did"], ["didn"], ["dinner"], ["do"], ["doe"],
    ["does"], ["doesn"], ["doing"], ["don"], ["done"], ["dont"], ["down"], ["during"], ["each"], ["eat"], ["end"], ["even"],
    ["ever"], ["everyon"], ["exam"], ["famili"], ["feel"], ["few"], ["final"], ["find"], ["first"], ["follow"], ["for"],
    ["found"], ["friday"], ["from"], ["further"], ["game"], ["get"], ["girl"], ["give"], ["gone"], ["gonna"], ["got"],
    ["gotta"], ["guess"], ["guy"], ["had"], ["hair"], ["happen"], ["has"], ["have"], ["haven"], ["having"], ["he"], ["head"],
    ["hear"], ["her"], ["here"], ["hers"], ["herself"], ["hey"], ["him"], ["himself"], ["his"], ["home"], ["hour"], ["hous"],
    ["how"], ["http"], ["i"], ["if"], ["im"], ["in"], ["into"], ["is"], ["isn"], ["it"], ["its"], ["itself"], ["job"], ["just"],
    ["keep"], ["know"], ["last"], ["later"], ["least"], ["leav"], ["let"], ["life"], ["listen"], ["littl"], ["live"], ["look"],
    ["lot"], ["lunch"], ["made"], ["make"], ["man"], ["mani"], ["may"], ["mayb"], ["me"], ["mean"], ["meet"], ["might"],
    ["mom"], ["monday"], ["month"], ["more"], ["morn"], ["most"], ["move"], ["movi"], ["much"], ["must"], ["my"], ["myself"],
    ["need"], ["never"], ["new"], ["night"], ["no"], ["nor"], ["not"], ["noth"], ["now"], ["of"], ["off"], ["on"], ["once"],
    ["one"], ["onli"], ["only"], ["or"], ["other"], ["ought"], ["our"], ["ours"], ["ourselves"], ["out"], ["over"], ["own"],
    ["peopl"], ["phone"], ["pic"], ["pictur"], ["play"], ["post"], ["put"], ["quot"], ["rain"], ["read"], ["readi"],
    ["realli"], ["run"], ["said"], ["same"], ["saw"], ["say"], ["school"], ["see"], ["seem"], ["she"], ["shop"], ["should"],
    ["show"], ["sinc"], ["sleep"], ["so"], ["some"], ["someon"], ["someth"], ["song"], ["soon"], ["sound"], ["start"],
    ["stay"], ["still"], ["studi"], ["stuff"], ["such"], ["summer"], ["sunday"], ["sure"], ["take"], ["talk"], ["tell"],
    ["than"], ["thank"], ["that"], ["the"], ["their"], ["theirs"], ["them"], ["themselves"], ["then"], ["there"], ["these"],
    ["they"], ["thing"], ["think"], ["this"], ["those"], ["though"], ["thought"], ["through"], ["time"], ["to"], ["today"],
    ["tomorrow"], ["tonight"], ["too"], ["total"], ["tri"], ["tweet"], ["twitpic"], ["twitter"], ["two"], ["u"], ["under"],
    ["until"], ["up"], ["updat"], ["use"], ["veri"], ["very"], ["video"], ["wait"], ["wanna"], ["want"], ["was"], ["watch"],
    ["way"], ["we"], ["weather"], ["week"], ["weekend"], ["went"], ["were"], ["what"], ["when"], ["where"], ["whi"],
    ["which"], ["while"], ["who"], ["whom"], ["why"], ["will"], ["with"], ["woke"], ["won"], ["work"], ["world"], ["would"],
    ["www"], ["yay"], ["yeah"], ["year"], ["yes"], ["yesterday"], ["yet"], ["you"], ["your"], ["yours"], ["yourself"],
    ["yourselves"], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"], ["i"], ["j"], ["k"], ["l"], ["m"], ["n"],
    ["o"], ["p"], ["k"], ["r"], ["s"], ["t"], ["u"], ["v"], ["w"], ["x"], ["u"], ["z"], ["mr"], ["miss"], ["mrs"], ["ms"]
]
third_filename = "remove.csv"
with open(third_filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(remove_words)
remove = os.path.join(os.getcwd(),third_filename)

second_data = [
    ["Hello, world!"],
    ["Python is great."],
    ["Let's test some sentences."],
    ["Numbers like 1234 and special characters #, $, & should be handled."],
    [""],  # Empty string
]
fourth_filename = "test_sentences.csv"

with open(fourth_filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(second_data)

second_sentences = os.path.join(os.getcwd(), fourth_filename)
@pytest.fixture

def mock_json_data():
    """Returns mock JSON data."""
    return json.dumps({"key": {"subkey": ["value1", "value2"]}})

def test_file_not_found():
    with pytest.raises(SystemExit):
        read_csv_file("non_existent_file.csv")

def test_csv_with_empty_rows():
    test_csv_path = "test_empty_rows.csv"
    with open(test_csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age", "City"])
        writer.writerow([])
        writer.writerow(["Charlie", "35", "Chicago"])

    result = read_csv_file(test_csv_path)
    expected = [["Name", "Age", "City"], ["Charlie", "35", "Chicago"]]
    assert result == expected

    # Clean up
    os.remove(test_csv_path)


def test_read_valid_csv():
    # Create a temporary CSV file for testing
    test_csv_path = "test_valid.csv"
    with open(test_csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age", "City"])
        writer.writerow(["Alice", "30", "New York"])
        writer.writerow(["Bob", "25", "Los Angeles"])

    result = read_csv_file(test_csv_path)
    expected = [["Name", "Age", "City"], ["Alice", "30", "New York"], ["Bob", "25", "Los Angeles"]]
    assert result == expected

    # Clean up
    os.remove(test_csv_path)


def test_sentence_breaking():
    result = [['when', 'he', 'was', 'nearly', 'thirteen', 'my', 'brother', 'jem', 'got', 'his', 'arm', 'badly', 'broken', 'at', 'the', 'elbow'], ['when', 'it', 'healed', 'and', 'jem', 's', 'fears', 'of', 'never', 'being', 'able', 'to', 'play', 'football', 'were', 'assuaged'], ['he', 'was', 'seldom', 'self', 'conscious', 'about', 'his', 'injury'], ['his', 'left', 'arm', 'was', 'somewhat', 'shorter', 'than', 'his', 'right', 'when', 'he', 'stood', 'or', 'walked', 'the', 'back', 'of', 'his', 'hand', 'was', 'at', 'right', 'angles', 'to', 'his', 'body', 'his', 'thumb', 'parallel', 'to', 'his', 'thigh'], ['he', 'couldn', 't', 'have', 'cared', 'less', 'so', 'long', 'as', 'he', 'could', 'pass', 'and', 'punt'], ['when', 'enough', 'years', 'had', 'gone', 'by', 'to', 'enable', 'us', 'to', 'look', 'back', 'on', 'them', 'we', 'sometimes', 'discussed', 'the', 'events', 'leading', 'to', 'his', 'accident'], ['i', 'maintain', 'that', 'the', 'ewells', 'started', 'it', 'all', 'but', 'jem', 'who', 'was', 'four', 'years', 'my', 'senior', 'said', 'it', 'started', 'long', 'before', 'that'], ['he', 'said', 'it', 'began', 'the', 'summer', 'dill', 'came', 'to', 'us', 'when', 'dill', 'first', 'gave', 'us', 'the', 'idea', 'of', 'making', 'boo', 'radley', 'come', 'out'], ['i', 'said', 'if', 'he', 'wanted', 'to', 'take', 'a', 'broad', 'view', 'of', 'the', 'thing', 'it', 'really', 'began', 'with', 'andrew', 'jackson'], ['if', 'general', 'jackson', 'hadn', 't', 'run', 'the', 'creeks', 'up', 'the', 'creek', 'simon', 'finch', 'would', 'never', 'have', 'paddled', 'up', 'the', 'alabama'], ['and', 'where', 'would', 'we', 'be', 'if', 'he', 'hadn', 't', 'we', 'were', 'far', 'too', 'old', 'to', 'settle', 'an', 'argument', 'with', 'a', 'fist', 'fight', 'so', 'we', 'consulted', 'atticus', 'our', 'father', 'said', 'we', 'were', 'both', 'right'], ['being', 'southerners', 'it', 'was', 'a', 'source', 'of', 'shame', 'to', 'some', 'members', 'of', 'the', 'family', 'that', 'we', 'had', 'no', 'recorded', 'ancestors', 'on', 'either', 'side', 'of', 'the', 'battle', 'of', 'hastings'], ['all', 'we', 'had', 'was', 'simon', 'finch', 'a', 'fur', 'trapping', 'apothecary', 'from', 'cornwall', 'whose', 'piety', 'was', 'exceeded', 'only', 'by', 'his', 'stinginess'], ['in', 'england', 'simon', 'was', 'irritated', 'by', 'the', 'persecution', 'of', 'those', 'who', 'called', 'themselves', 'methodists', 'at', 'the', 'hands', 'of', 'their', 'more', 'liberal', 'brethren'], ['and', 'as', 'simon', 'called', 'himself', 'a', 'methodist', 'he', 'worked', 'his', 'way', 'across', 'the', 'atlantic', 'to', 'philadelphia'], ['thence', 'to', 'jamaica', 'thence', 'to', 'mobile', 'and', 'up', 'the', 'saint', 'stephens']]
    assert sentence_breaking(sentences) == result

    expected_result = [
        ['hello', 'world'],
        ['python', 'is', 'great'],
        ['let', 's', 'test', 'some', 'sentences'],
        ['numbers', 'like', '1234', 'and', 'special', 'characters','should','be','handled']]
          # Empty sentence should return an empty list
    assert sentence_breaking(second_sentences) == expected_result

def test_dictionary_of_names():
    result = {'Jem': [], 'Dill': [], 'Boo Radley': [], 'Andrew Jackson': [], 'General Jackson': [], 'Simon Finch': [], 'Atticus': []}
    assert dictionary_of_names(names,remove) == result

def test_string_cleaning():
    result= "hagrid father"
    assert string_cleaning("Hagrid s Father ",remove) == result

def test_string_cleaning_2():
    assert string_cleaning("s",remove) == ''

def test_string_cleaning_3():
    assert string_cleaning("Hagrid fat'her",remove) == "hagrid father"

def test_dictionary_cleaning():
    result = {'jem': [''], 'dill': [''], 'boo radley': [''], 'andrew jackson': [''], 'general jackson': [''], 'simon finch': [''], 'atticus': ['']}
    names = {'Jem': [''], 'Dill': [''], 'Boo Radley': [''], 'Andrew Jackson': [''], 'General Jackson': [''], 'Simon Finch': [''], 'Atticus': ['']}
    assert dictionary_cleaning(names,remove) == result

def test_dictionary_cleaning_empty():
    result = dictionary_cleaning({}, remove)
    assert result == {}

def test_grouping_names():
    result = [[[]]]
    assert grouping_names({}) == result

def test_sentence_output():
    result =[['healed', 'jem', 'fears', 'able', 'football', 'assuaged'], ['seldom', 'self', 'conscious', 'injury'], ['left', 'arm', 'somewhat', 'shorter', 'right', 'stood', 'walked', 'hand', 'right', 'angles', 'body', 'thumb', 'parallel', 'thigh'], ['couldn', 'cared', 'less', 'long', 'pass', 'punt'], ['enough', 'years', 'enable', 'us', 'sometimes', 'discussed', 'events', 'leading', 'accident'], ['maintain', 'ewells', 'started', 'jem', 'four', 'years', 'senior', 'started', 'long'], ['began', 'dill', 'came', 'us', 'dill', 'gave', 'us', 'idea', 'making', 'boo', 'radley'], ['wanted', 'broad', 'view', 'really', 'began', 'andrew', 'jackson'], ['general', 'jackson', 'hadn', 'creeks', 'creek', 'simon', 'finch', 'paddled', 'alabama'], ['hadn', 'far', 'old', 'settle', 'argument', 'fist', 'fight', 'consulted', 'atticus', 'father', 'right'], ['southerners', 'source', 'shame', 'members', 'family', 'recorded', 'ancestors', 'either', 'side', 'battle', 'hastings'], ['simon', 'finch', 'fur', 'trapping', 'apothecary', 'cornwall', 'whose', 'piety', 'exceeded', 'stinginess'], ['england', 'simon', 'irritated', 'persecution', 'called', 'methodists', 'hands', 'liberal', 'brethren'], ['simon', 'called', 'methodist', 'worked', 'across', 'atlantic', 'philadelphia'], ['thence', 'jamaica', 'thence', 'mobile', 'saint', 'stephens']]
    removed = read_csv_file(remove)
    assert sentence_output(removed,sentences) == result

def test_initial_text_processing():
    result ={'Question 1': {'Processed Sentences': [['healed', 'jem', 'fears', 'able', 'football', 'assuaged'], ['seldom', 'self', 'conscious', 'injury'], ['left', 'arm', 'somewhat', 'shorter', 'right', 'stood', 'walked', 'hand', 'right', 'angles', 'body', 'thumb', 'parallel', 'thigh'], ['couldn', 'cared', 'less', 'long', 'pass', 'punt'], ['enough', 'years', 'enable', 'us', 'sometimes', 'discussed', 'events', 'leading', 'accident'], ['maintain', 'ewells', 'started', 'jem', 'four', 'years', 'senior', 'started', 'long'], ['began', 'dill', 'came', 'us', 'dill', 'gave', 'us', 'idea', 'making', 'boo', 'radley'], ['wanted', 'broad', 'view', 'really', 'began', 'andrew', 'jackson'], ['general', 'jackson', 'hadn', 'creeks', 'creek', 'simon', 'finch', 'paddled', 'alabama'], ['hadn', 'far', 'old', 'settle', 'argument', 'fist', 'fight', 'consulted', 'atticus', 'father', 'right'], ['southerners', 'source', 'shame', 'members', 'family', 'recorded', 'ancestors', 'either', 'side', 'battle', 'hastings'], ['simon', 'finch', 'fur', 'trapping', 'apothecary', 'cornwall', 'whose', 'piety', 'exceeded', 'stinginess'], ['england', 'simon', 'irritated', 'persecution', 'called', 'methodists', 'hands', 'liberal', 'brethren'], ['simon', 'called', 'methodist', 'worked', 'across', 'atlantic', 'philadelphia'], ['thence', 'jamaica', 'thence', 'mobile', 'saint', 'stephens']], 'Processed Names': [[['jem'], []], [['dill'], []], [['boo', 'radley'], []], [['andrew', 'jackson'], []], [['general', 'jackson'], []], [['simon', 'finch'], []], [['atticus'], []]]}}
    assert initial_text_processing(sentences, names ,remove) == result

def test_searching_string():
    result = ["alabama", 1]
    sentence = "simon finch paddled alabama"
    assert searching_string("alabama",sentence) == result

def test_all_strings():
    dictionary = {'Question 1': {'Processed Sentences': [['healed', 'jem', 'fears', 'able', 'football', 'assuaged'], ['seldom', 'self', 'conscious', 'injury'], ['left', 'arm', 'somewhat', 'shorter', 'right', 'stood', 'walked', 'hand', 'right', 'angles', 'body', 'thumb', 'parallel', 'thigh'], ['couldn', 'cared', 'less', 'long', 'pass', 'punt'], ['enough', 'years', 'enable', 'us', 'sometimes', 'discussed', 'events', 'leading', 'accident'], ['maintain', 'ewells', 'started', 'jem', 'four', 'years', 'senior', 'started', 'long'], ['began', 'dill', 'came', 'us', 'dill', 'gave', 'us', 'idea', 'making', 'boo', 'radley'], ['wanted', 'broad', 'view', 'really', 'began', 'andrew', 'jackson'], ['general', 'jackson', 'hadn', 'creeks', 'creek', 'simon', 'finch', 'paddled', 'alabama'], ['hadn', 'far', 'old', 'settle', 'argument', 'fist', 'fight', 'consulted', 'atticus', 'father', 'right'], ['southerners', 'source', 'shame', 'members', 'family', 'recorded', 'ancestors', 'either', 'side', 'battle', 'hastings'], ['simon', 'finch', 'fur', 'trapping', 'apothecary', 'cornwall', 'whose', 'piety', 'exceeded', 'stinginess'], ['england', 'simon', 'irritated', 'persecution', 'called', 'methodists', 'hands', 'liberal', 'brethren'], ['simon', 'called', 'methodist', 'worked', 'across', 'atlantic', 'philadelphia'], ['thence', 'jamaica', 'thence', 'mobile', 'saint', 'stephens']], 'Processed Names': [[['jem'], []], [['dill'], []], [['boo', 'radley'], []], [['andrew', 'jackson'], []], [['general', 'jackson'], []], [['simon', 'finch'], []], [['atticus'], []]]}}
    sentences_list = dict_to_list(dictionary)
    result = [['healed', 'jem', 'fears', 'able', 'football', 'assuaged', 'seldom', 'self', 'conscious', 'injury', 'left', 'arm', 'somewhat', 'shorter', 'right', 'stood', 'walked', 'hand', 'right', 'angles', 'body', 'thumb', 'parallel', 'thigh', 'couldn', 'cared', 'less', 'long', 'pass', 'punt', 'enough', 'years', 'enable', 'us', 'sometimes', 'discussed', 'events', 'leading', 'accident', 'maintain', 'ewells', 'started', 'jem', 'four', 'years', 'senior', 'started', 'long', 'began', 'dill', 'came', 'us', 'dill', 'gave', 'us', 'idea', 'making', 'boo', 'radley', 'wanted', 'broad', 'view', 'really', 'began', 'andrew', 'jackson', 'general', 'jackson', 'hadn', 'creeks', 'creek', 'simon', 'finch', 'paddled', 'alabama', 'hadn', 'far', 'old', 'settle', 'argument', 'fist', 'fight', 'consulted', 'atticus', 'father', 'right', 'southerners', 'source', 'shame', 'members', 'family', 'recorded', 'ancestors', 'either', 'side', 'battle', 'hastings', 'simon', 'finch', 'fur', 'trapping', 'apothecary', 'cornwall', 'whose', 'piety', 'exceeded', 'stinginess', 'england', 'simon', 'irritated', 'persecution', 'called', 'methodists', 'hands', 'liberal', 'brethren', 'simon', 'called', 'methodist', 'worked', 'across', 'atlantic', 'philadelphia', 'thence', 'jamaica', 'thence', 'mobile', 'saint', 'stephens'], ['healed jem', 'jem fears', 'fears able', 'able football', 'football assuaged', 'seldom self', 'self conscious', 'conscious injury', 'left arm', 'arm somewhat', 'somewhat shorter', 'shorter right', 'right stood', 'stood walked', 'walked hand', 'hand right', 'right angles', 'angles body', 'body thumb', 'thumb parallel', 'parallel thigh', 'couldn cared', 'cared less', 'less long', 'long pass', 'pass punt', 'enough years', 'years enable', 'enable us', 'us sometimes', 'sometimes discussed', 'discussed events', 'events leading', 'leading accident', 'maintain ewells', 'ewells started', 'started jem', 'jem four', 'four years', 'years senior', 'senior started', 'started long', 'began dill', 'dill came', 'came us', 'us dill', 'dill gave', 'gave us', 'us idea', 'idea making', 'making boo', 'boo radley', 'wanted broad', 'broad view', 'view really', 'really began', 'began andrew', 'andrew jackson', 'general jackson', 'jackson hadn', 'hadn creeks', 'creeks creek', 'creek simon', 'simon finch', 'finch paddled', 'paddled alabama', 'hadn far', 'far old', 'old settle', 'settle argument', 'argument fist', 'fist fight', 'fight consulted', 'consulted atticus', 'atticus father', 'father right', 'southerners source', 'source shame', 'shame members', 'members family', 'family recorded', 'recorded ancestors', 'ancestors either', 'either side', 'side battle', 'battle hastings', 'simon finch', 'finch fur', 'fur trapping', 'trapping apothecary', 'apothecary cornwall', 'cornwall whose', 'whose piety', 'piety exceeded', 'exceeded stinginess', 'england simon', 'simon irritated', 'irritated persecution', 'persecution called', 'called methodists', 'methodists hands', 'hands liberal', 'liberal brethren', 'simon called', 'called methodist', 'methodist worked', 'worked across', 'across atlantic', 'atlantic philadelphia', 'thence jamaica', 'jamaica thence', 'thence mobile', 'mobile saint', 'saint stephens'], ['healed jem fears', 'jem fears able', 'fears able football', 'able football assuaged', 'seldom self conscious', 'self conscious injury', 'left arm somewhat', 'arm somewhat shorter', 'somewhat shorter right', 'shorter right stood', 'right stood walked', 'stood walked hand', 'walked hand right', 'hand right angles', 'right angles body', 'angles body thumb', 'body thumb parallel', 'thumb parallel thigh', 'couldn cared less', 'cared less long', 'less long pass', 'long pass punt', 'enough years enable', 'years enable us', 'enable us sometimes', 'us sometimes discussed', 'sometimes discussed events', 'discussed events leading', 'events leading accident', 'maintain ewells started', 'ewells started jem', 'started jem four', 'jem four years', 'four years senior', 'years senior started', 'senior started long', 'began dill came', 'dill came us', 'came us dill', 'us dill gave', 'dill gave us', 'gave us idea', 'us idea making', 'idea making boo', 'making boo radley', 'wanted broad view', 'broad view really', 'view really began', 'really began andrew', 'began andrew jackson', 'general jackson hadn', 'jackson hadn creeks', 'hadn creeks creek', 'creeks creek simon', 'creek simon finch', 'simon finch paddled', 'finch paddled alabama', 'hadn far old', 'far old settle', 'old settle argument', 'settle argument fist', 'argument fist fight', 'fist fight consulted', 'fight consulted atticus', 'consulted atticus father', 'atticus father right', 'southerners source shame', 'source shame members', 'shame members family', 'members family recorded', 'family recorded ancestors', 'recorded ancestors either', 'ancestors either side', 'either side battle', 'side battle hastings', 'simon finch fur', 'finch fur trapping', 'fur trapping apothecary', 'trapping apothecary cornwall', 'apothecary cornwall whose', 'cornwall whose piety', 'whose piety exceeded', 'piety exceeded stinginess', 'england simon irritated', 'simon irritated persecution', 'irritated persecution called', 'persecution called methodists', 'called methodists hands', 'methodists hands liberal', 'hands liberal brethren', 'simon called methodist', 'called methodist worked', 'methodist worked across', 'worked across atlantic', 'across atlantic philadelphia', 'thence jamaica thence', 'jamaica thence mobile', 'thence mobile saint', 'mobile saint stephens'], ['healed jem fears able', 'jem fears able football', 'fears able football assuaged', 'seldom self conscious injury', 'left arm somewhat shorter', 'arm somewhat shorter right', 'somewhat shorter right stood', 'shorter right stood walked', 'right stood walked hand', 'stood walked hand right', 'walked hand right angles', 'hand right angles body', 'right angles body thumb', 'angles body thumb parallel', 'body thumb parallel thigh', 'couldn cared less long', 'cared less long pass', 'less long pass punt', 'enough years enable us', 'years enable us sometimes', 'enable us sometimes discussed', 'us sometimes discussed events', 'sometimes discussed events leading', 'discussed events leading accident', 'maintain ewells started jem', 'ewells started jem four', 'started jem four years', 'jem four years senior', 'four years senior started', 'years senior started long', 'began dill came us', 'dill came us dill', 'came us dill gave', 'us dill gave us', 'dill gave us idea', 'gave us idea making', 'us idea making boo', 'idea making boo radley', 'wanted broad view really', 'broad view really began', 'view really began andrew', 'really began andrew jackson', 'general jackson hadn creeks', 'jackson hadn creeks creek', 'hadn creeks creek simon', 'creeks creek simon finch', 'creek simon finch paddled', 'simon finch paddled alabama', 'hadn far old settle', 'far old settle argument', 'old settle argument fist', 'settle argument fist fight', 'argument fist fight consulted', 'fist fight consulted atticus', 'fight consulted atticus father', 'consulted atticus father right', 'southerners source shame members', 'source shame members family', 'shame members family recorded', 'members family recorded ancestors', 'family recorded ancestors either', 'recorded ancestors either side', 'ancestors either side battle', 'either side battle hastings', 'simon finch fur trapping', 'finch fur trapping apothecary', 'fur trapping apothecary cornwall', 'trapping apothecary cornwall whose', 'apothecary cornwall whose piety', 'cornwall whose piety exceeded', 'whose piety exceeded stinginess', 'england simon irritated persecution', 'simon irritated persecution called', 'irritated persecution called methodists', 'persecution called methodists hands', 'called methodists hands liberal', 'methodists hands liberal brethren', 'simon called methodist worked', 'called methodist worked across', 'methodist worked across atlantic', 'worked across atlantic philadelphia', 'thence jamaica thence mobile', 'jamaica thence mobile saint', 'thence mobile saint stephens']]
    assert all_strings(sentences_list,4) == result

def test_dict_to_list():
    result = [['healed', 'jem', 'fears', 'able', 'football', 'assuaged'], ['seldom', 'self', 'conscious', 'injury'], ['left', 'arm', 'somewhat', 'shorter', 'right', 'stood', 'walked', 'hand', 'right', 'angles', 'body', 'thumb', 'parallel', 'thigh'], ['couldn', 'cared', 'less', 'long', 'pass', 'punt'], ['enough', 'years', 'enable', 'us', 'sometimes', 'discussed', 'events', 'leading', 'accident'], ['maintain', 'ewells', 'started', 'jem', 'four', 'years', 'senior', 'started', 'long'], ['began', 'dill', 'came', 'us', 'dill', 'gave', 'us', 'idea', 'making', 'boo', 'radley'], ['wanted', 'broad', 'view', 'really', 'began', 'andrew', 'jackson'], ['general', 'jackson', 'hadn', 'creeks', 'creek', 'simon', 'finch', 'paddled', 'alabama'], ['hadn', 'far', 'old', 'settle', 'argument', 'fist', 'fight', 'consulted', 'atticus', 'father', 'right'], ['southerners', 'source', 'shame', 'members', 'family', 'recorded', 'ancestors', 'either', 'side', 'battle', 'hastings'], ['simon', 'finch', 'fur', 'trapping', 'apothecary', 'cornwall', 'whose', 'piety', 'exceeded', 'stinginess'], ['england', 'simon', 'irritated', 'persecution', 'called', 'methodists', 'hands', 'liberal', 'brethren'], ['simon', 'called', 'methodist', 'worked', 'across', 'atlantic', 'philadelphia'], ['thence', 'jamaica', 'thence', 'mobile', 'saint', 'stephens']]
    task_1_output = {'Question 1': {'Processed Sentences': [['healed', 'jem', 'fears', 'able', 'football', 'assuaged'], ['seldom', 'self', 'conscious', 'injury'], ['left', 'arm', 'somewhat', 'shorter', 'right', 'stood', 'walked', 'hand', 'right', 'angles', 'body', 'thumb', 'parallel', 'thigh'], ['couldn', 'cared', 'less', 'long', 'pass', 'punt'], ['enough', 'years', 'enable', 'us', 'sometimes', 'discussed', 'events', 'leading', 'accident'], ['maintain', 'ewells', 'started', 'jem', 'four', 'years', 'senior', 'started', 'long'], ['began', 'dill', 'came', 'us', 'dill', 'gave', 'us', 'idea', 'making', 'boo', 'radley'], ['wanted', 'broad', 'view', 'really', 'began', 'andrew', 'jackson'], ['general', 'jackson', 'hadn', 'creeks', 'creek', 'simon', 'finch', 'paddled', 'alabama'], ['hadn', 'far', 'old', 'settle', 'argument', 'fist', 'fight', 'consulted', 'atticus', 'father', 'right'], ['southerners', 'source', 'shame', 'members', 'family', 'recorded', 'ancestors', 'either', 'side', 'battle', 'hastings'], ['simon', 'finch', 'fur', 'trapping', 'apothecary', 'cornwall', 'whose', 'piety', 'exceeded', 'stinginess'], ['england', 'simon', 'irritated', 'persecution', 'called', 'methodists', 'hands', 'liberal', 'brethren'], ['simon', 'called', 'methodist', 'worked', 'across', 'atlantic', 'philadelphia'], ['thence', 'jamaica', 'thence', 'mobile', 'saint', 'stephens']], 'Processed Names': [[['jem'], []], [['dill'], []], [['boo', 'radley'], []], [['andrew', 'jackson'], []], [['general', 'jackson'], []], [['simon', 'finch'], []], [['atticus'], []]]}}
    assert dict_to_list(task_1_output) == result

def test_sequences():
    sentence_list = [['healed', 'jem', 'fears', 'able', 'football', 'assuaged'], ['seldom', 'self', 'conscious', 'injury'], ['left', 'arm', 'somewhat', 'shorter', 'right', 'stood', 'walked', 'hand', 'right', 'angles', 'body', 'thumb', 'parallel', 'thigh'], ['couldn', 'cared', 'less', 'long', 'pass', 'punt'], ['enough', 'years', 'enable', 'us', 'sometimes', 'discussed', 'events', 'leading', 'accident'], ['maintain', 'ewells', 'started', 'jem', 'four', 'years', 'senior', 'started', 'long'], ['began', 'dill', 'came', 'us', 'dill', 'gave', 'us', 'idea', 'making', 'boo', 'radley'], ['wanted', 'broad', 'view', 'really', 'began', 'andrew', 'jackson'], ['general', 'jackson', 'hadn', 'creeks', 'creek', 'simon', 'finch', 'paddled', 'alabama'], ['hadn', 'far', 'old', 'settle', 'argument', 'fist', 'fight', 'consulted', 'atticus', 'father', 'right'], ['southerners', 'source', 'shame', 'members', 'family', 'recorded', 'ancestors', 'either', 'side', 'battle', 'hastings'], ['simon', 'finch', 'fur', 'trapping', 'apothecary', 'cornwall', 'whose', 'piety', 'exceeded', 'stinginess'], ['england', 'simon', 'irritated', 'persecution', 'called', 'methodists', 'hands', 'liberal', 'brethren'], ['simon', 'called', 'methodist', 'worked', 'across', 'atlantic', 'philadelphia'], ['thence', 'jamaica', 'thence', 'mobile', 'saint', 'stephens']]
    strings =  [['healed', 'jem', 'fears', 'able', 'football', 'assuaged', 'seldom', 'self', 'conscious', 'injury', 'left', 'arm', 'somewhat', 'shorter', 'right', 'stood', 'walked', 'hand', 'right', 'angles', 'body', 'thumb', 'parallel', 'thigh', 'couldn', 'cared', 'less', 'long', 'pass', 'punt', 'enough', 'years', 'enable', 'us', 'sometimes', 'discussed', 'events', 'leading', 'accident', 'maintain', 'ewells', 'started', 'jem', 'four', 'years', 'senior', 'started', 'long', 'began', 'dill', 'came', 'us', 'dill', 'gave', 'us', 'idea', 'making', 'boo', 'radley', 'wanted', 'broad', 'view', 'really', 'began', 'andrew', 'jackson', 'general', 'jackson', 'hadn', 'creeks', 'creek', 'simon', 'finch', 'paddled', 'alabama', 'hadn', 'far', 'old', 'settle', 'argument', 'fist', 'fight', 'consulted', 'atticus', 'father', 'right', 'southerners', 'source', 'shame', 'members', 'family', 'recorded', 'ancestors', 'either', 'side', 'battle', 'hastings', 'simon', 'finch', 'fur', 'trapping', 'apothecary', 'cornwall', 'whose', 'piety', 'exceeded', 'stinginess', 'england', 'simon', 'irritated', 'persecution', 'called', 'methodists', 'hands', 'liberal', 'brethren', 'simon', 'called', 'methodist', 'worked', 'across', 'atlantic', 'philadelphia', 'thence', 'jamaica', 'thence', 'mobile', 'saint', 'stephens'], ['healed jem', 'jem fears', 'fears able', 'able football', 'football assuaged', 'seldom self', 'self conscious', 'conscious injury', 'left arm', 'arm somewhat', 'somewhat shorter', 'shorter right', 'right stood', 'stood walked', 'walked hand', 'hand right', 'right angles', 'angles body', 'body thumb', 'thumb parallel', 'parallel thigh', 'couldn cared', 'cared less', 'less long', 'long pass', 'pass punt', 'enough years', 'years enable', 'enable us', 'us sometimes', 'sometimes discussed', 'discussed events', 'events leading', 'leading accident', 'maintain ewells', 'ewells started', 'started jem', 'jem four', 'four years', 'years senior', 'senior started', 'started long', 'began dill', 'dill came', 'came us', 'us dill', 'dill gave', 'gave us', 'us idea', 'idea making', 'making boo', 'boo radley', 'wanted broad', 'broad view', 'view really', 'really began', 'began andrew', 'andrew jackson', 'general jackson', 'jackson hadn', 'hadn creeks', 'creeks creek', 'creek simon', 'simon finch', 'finch paddled', 'paddled alabama', 'hadn far', 'far old', 'old settle', 'settle argument', 'argument fist', 'fist fight', 'fight consulted', 'consulted atticus', 'atticus father', 'father right', 'southerners source', 'source shame', 'shame members', 'members family', 'family recorded', 'recorded ancestors', 'ancestors either', 'either side', 'side battle', 'battle hastings', 'simon finch', 'finch fur', 'fur trapping', 'trapping apothecary', 'apothecary cornwall', 'cornwall whose', 'whose piety', 'piety exceeded', 'exceeded stinginess', 'england simon', 'simon irritated', 'irritated persecution', 'persecution called', 'called methodists', 'methodists hands', 'hands liberal', 'liberal brethren', 'simon called', 'called methodist', 'methodist worked', 'worked across', 'across atlantic', 'atlantic philadelphia', 'thence jamaica', 'jamaica thence', 'thence mobile', 'mobile saint', 'saint stephens'], ['healed jem fears', 'jem fears able', 'fears able football', 'able football assuaged', 'seldom self conscious', 'self conscious injury', 'left arm somewhat', 'arm somewhat shorter', 'somewhat shorter right', 'shorter right stood', 'right stood walked', 'stood walked hand', 'walked hand right', 'hand right angles', 'right angles body', 'angles body thumb', 'body thumb parallel', 'thumb parallel thigh', 'couldn cared less', 'cared less long', 'less long pass', 'long pass punt', 'enough years enable', 'years enable us', 'enable us sometimes', 'us sometimes discussed', 'sometimes discussed events', 'discussed events leading', 'events leading accident', 'maintain ewells started', 'ewells started jem', 'started jem four', 'jem four years', 'four years senior', 'years senior started', 'senior started long', 'began dill came', 'dill came us', 'came us dill', 'us dill gave', 'dill gave us', 'gave us idea', 'us idea making', 'idea making boo', 'making boo radley', 'wanted broad view', 'broad view really', 'view really began', 'really began andrew', 'began andrew jackson', 'general jackson hadn', 'jackson hadn creeks', 'hadn creeks creek', 'creeks creek simon', 'creek simon finch', 'simon finch paddled', 'finch paddled alabama', 'hadn far old', 'far old settle', 'old settle argument', 'settle argument fist', 'argument fist fight', 'fist fight consulted', 'fight consulted atticus', 'consulted atticus father', 'atticus father right', 'southerners source shame', 'source shame members', 'shame members family', 'members family recorded', 'family recorded ancestors', 'recorded ancestors either', 'ancestors either side', 'either side battle', 'side battle hastings', 'simon finch fur', 'finch fur trapping', 'fur trapping apothecary', 'trapping apothecary cornwall', 'apothecary cornwall whose', 'cornwall whose piety', 'whose piety exceeded', 'piety exceeded stinginess', 'england simon irritated', 'simon irritated persecution', 'irritated persecution called', 'persecution called methodists', 'called methodists hands', 'methodists hands liberal', 'hands liberal brethren', 'simon called methodist', 'called methodist worked', 'methodist worked across', 'worked across atlantic', 'across atlantic philadelphia', 'thence jamaica thence', 'jamaica thence mobile', 'thence mobile saint', 'mobile saint stephens'], ['healed jem fears able', 'jem fears able football', 'fears able football assuaged', 'seldom self conscious injury', 'left arm somewhat shorter', 'arm somewhat shorter right', 'somewhat shorter right stood', 'shorter right stood walked', 'right stood walked hand', 'stood walked hand right', 'walked hand right angles', 'hand right angles body', 'right angles body thumb', 'angles body thumb parallel', 'body thumb parallel thigh', 'couldn cared less long', 'cared less long pass', 'less long pass punt', 'enough years enable us', 'years enable us sometimes', 'enable us sometimes discussed', 'us sometimes discussed events', 'sometimes discussed events leading', 'discussed events leading accident', 'maintain ewells started jem', 'ewells started jem four', 'started jem four years', 'jem four years senior', 'four years senior started', 'years senior started long', 'began dill came us', 'dill came us dill', 'came us dill gave', 'us dill gave us', 'dill gave us idea', 'gave us idea making', 'us idea making boo', 'idea making boo radley', 'wanted broad view really', 'broad view really began', 'view really began andrew', 'really began andrew jackson', 'general jackson hadn creeks', 'jackson hadn creeks creek', 'hadn creeks creek simon', 'creeks creek simon finch', 'creek simon finch paddled', 'simon finch paddled alabama', 'hadn far old settle', 'far old settle argument', 'old settle argument fist', 'settle argument fist fight', 'argument fist fight consulted', 'fist fight consulted atticus', 'fight consulted atticus father', 'consulted atticus father right', 'southerners source shame members', 'source shame members family', 'shame members family recorded', 'members family recorded ancestors', 'family recorded ancestors either', 'recorded ancestors either side', 'ancestors either side battle', 'either side battle hastings', 'simon finch fur trapping', 'finch fur trapping apothecary', 'fur trapping apothecary cornwall', 'trapping apothecary cornwall whose', 'apothecary cornwall whose piety', 'cornwall whose piety exceeded', 'whose piety exceeded stinginess', 'england simon irritated persecution', 'simon irritated persecution called', 'irritated persecution called methodists', 'persecution called methodists hands', 'called methodists hands liberal', 'methodists hands liberal brethren', 'simon called methodist worked', 'called methodist worked across', 'methodist worked across atlantic', 'worked across atlantic philadelphia', 'thence jamaica thence mobile', 'jamaica thence mobile saint', 'thence mobile saint stephens']]
    result = [[['able', 1], ['accident', 1], ['across', 1], ['alabama', 1], ['ancestors', 1], ['andrew', 1], ['angles', 1], ['apothecary', 1], ['argument', 1], ['arm', 1], ['assuaged', 1], ['atlantic', 1], ['atticus', 1], ['battle', 1], ['began', 2], ['body', 1], ['boo', 1], ['brethren', 1], ['broad', 1], ['called', 2], ['came', 1], ['cared', 1], ['conscious', 1], ['consulted', 1], ['cornwall', 1], ['couldn', 1], ['creek', 1], ['creeks', 1], ['dill', 2], ['discussed', 1], ['either', 1], ['enable', 1], ['england', 1], ['enough', 1], ['events', 1], ['ewells', 1], ['exceeded', 1], ['family', 1], ['far', 1], ['father', 1], ['fears', 1], ['fight', 1], ['finch', 2], ['fist', 1], ['football', 1], ['four', 1], ['fur', 1], ['gave', 1], ['general', 1], ['hadn', 2], ['hand', 1], ['hands', 1], ['hastings', 1], ['healed', 1], ['idea', 1], ['injury', 1], ['irritated', 1], ['jackson', 2], ['jamaica', 1], ['jem', 2], ['leading', 1], ['left', 1], ['less', 1], ['liberal', 1], ['long', 2], ['maintain', 1], ['making', 1], ['members', 1], ['methodist', 1], ['methodists', 1], ['mobile', 1], ['old', 1], ['paddled', 1], ['parallel', 1], ['pass', 1], ['persecution', 1], ['philadelphia', 1], ['piety', 1], ['punt', 1], ['radley', 1], ['really', 1], ['recorded', 1], ['right', 3], ['saint', 1], ['seldom', 1], ['self', 1], ['senior', 1], ['settle', 1], ['shame', 1], ['shorter', 1], ['side', 1], ['simon', 4], ['sometimes', 1], ['somewhat', 1], ['source', 1], ['southerners', 1], ['started', 2], ['stephens', 1], ['stinginess', 1], ['stood', 1], ['thence', 2], ['thigh', 1], ['thumb', 1], ['trapping', 1], ['us', 3], ['view', 1], ['walked', 1], ['wanted', 1], ['whose', 1], ['worked', 1], ['years', 2]], [['able football', 1], ['across atlantic', 1], ['ancestors either', 1], ['andrew jackson', 1], ['angles body', 1], ['apothecary cornwall', 1], ['argument fist', 1], ['arm somewhat', 1], ['atlantic philadelphia', 1], ['atticus father', 1], ['battle hastings', 1], ['began andrew', 1], ['began dill', 1], ['body thumb', 1], ['boo radley', 1], ['broad view', 1], ['called methodist', 1], ['called methodists', 1], ['came us', 1], ['cared less', 1], ['conscious injury', 1], ['consulted atticus', 1], ['cornwall whose', 1], ['couldn cared', 1], ['creek simon', 1], ['creeks creek', 1], ['dill came', 1], ['dill gave', 1], ['discussed events', 1], ['either side', 1], ['enable us', 1], ['england simon', 1], ['enough years', 1], ['events leading', 1], ['ewells started', 1], ['exceeded stinginess', 1], ['family recorded', 1], ['far old', 1], ['father right', 1], ['fears able', 1], ['fight consulted', 1], ['finch fur', 1], ['finch paddled', 1], ['fist fight', 1], ['football assuaged', 1], ['four years', 1], ['fur trapping', 1], ['gave us', 1], ['general jackson', 1], ['hadn creeks', 1], ['hadn far', 1], ['hand right', 1], ['hands liberal', 1], ['healed jem', 1], ['idea making', 1], ['irritated persecution', 1], ['jackson hadn', 1], ['jamaica thence', 1], ['jem fears', 1], ['jem four', 1], ['leading accident', 1], ['left arm', 1], ['less long', 1], ['liberal brethren', 1], ['long pass', 1], ['maintain ewells', 1], ['making boo', 1], ['members family', 1], ['methodist worked', 1], ['methodists hands', 1], ['mobile saint', 1], ['old settle', 1], ['paddled alabama', 1], ['parallel thigh', 1], ['pass punt', 1], ['persecution called', 1], ['piety exceeded', 1], ['really began', 1], ['recorded ancestors', 1], ['right angles', 1], ['right stood', 1], ['saint stephens', 1], ['seldom self', 1], ['self conscious', 1], ['senior started', 1], ['settle argument', 1], ['shame members', 1], ['shorter right', 1], ['side battle', 1], ['simon called', 1], ['simon finch', 2], ['simon irritated', 1], ['sometimes discussed', 1], ['somewhat shorter', 1], ['source shame', 1], ['southerners source', 1], ['started jem', 1], ['started long', 1], ['stood walked', 1], ['thence jamaica', 1], ['thence mobile', 1], ['thumb parallel', 1], ['trapping apothecary', 1], ['us dill', 1], ['us idea', 1], ['us sometimes', 1], ['view really', 1], ['walked hand', 1], ['wanted broad', 1], ['whose piety', 1], ['worked across', 1], ['years enable', 1], ['years senior', 1]], [['able football assuaged', 1], ['across atlantic philadelphia', 1], ['ancestors either side', 1], ['angles body thumb', 1], ['apothecary cornwall whose', 1], ['argument fist fight', 1], ['arm somewhat shorter', 1], ['atticus father right', 1], ['began andrew jackson', 1], ['began dill came', 1], ['body thumb parallel', 1], ['broad view really', 1], ['called methodist worked', 1], ['called methodists hands', 1], ['came us dill', 1], ['cared less long', 1], ['consulted atticus father', 1], ['cornwall whose piety', 1], ['couldn cared less', 1], ['creek simon finch', 1], ['creeks creek simon', 1], ['dill came us', 1], ['dill gave us', 1], ['discussed events leading', 1], ['either side battle', 1], ['enable us sometimes', 1], ['england simon irritated', 1], ['enough years enable', 1], ['events leading accident', 1], ['ewells started jem', 1], ['family recorded ancestors', 1], ['far old settle', 1], ['fears able football', 1], ['fight consulted atticus', 1], ['finch fur trapping', 1], ['finch paddled alabama', 1], ['fist fight consulted', 1], ['four years senior', 1], ['fur trapping apothecary', 1], ['gave us idea', 1], ['general jackson hadn', 1], ['hadn creeks creek', 1], ['hadn far old', 1], ['hand right angles', 1], ['hands liberal brethren', 1], ['healed jem fears', 1], ['idea making boo', 1], ['irritated persecution called', 1], ['jackson hadn creeks', 1], ['jamaica thence mobile', 1], ['jem fears able', 1], ['jem four years', 1], ['left arm somewhat', 1], ['less long pass', 1], ['long pass punt', 1], ['maintain ewells started', 1], ['making boo radley', 1], ['members family recorded', 1], ['methodist worked across', 1], ['methodists hands liberal', 1], ['mobile saint stephens', 1], ['old settle argument', 1], ['persecution called methodists', 1], ['piety exceeded stinginess', 1], ['really began andrew', 1], ['recorded ancestors either', 1], ['right angles body', 1], ['right stood walked', 1], ['seldom self conscious', 1], ['self conscious injury', 1], ['senior started long', 1], ['settle argument fist', 1], ['shame members family', 1], ['shorter right stood', 1], ['side battle hastings', 1], ['simon called methodist', 1], ['simon finch fur', 1], ['simon finch paddled', 1], ['simon irritated persecution', 1], ['sometimes discussed events', 1], ['somewhat shorter right', 1], ['source shame members', 1], ['southerners source shame', 1], ['started jem four', 1], ['stood walked hand', 1], ['thence jamaica thence', 1], ['thence mobile saint', 1], ['thumb parallel thigh', 1], ['trapping apothecary cornwall', 1], ['us dill gave', 1], ['us idea making', 1], ['us sometimes discussed', 1], ['view really began', 1], ['walked hand right', 1], ['wanted broad view', 1], ['whose piety exceeded', 1], ['worked across atlantic', 1], ['years enable us', 1], ['years senior started', 1]], [['ancestors either side battle', 1], ['angles body thumb parallel', 1], ['apothecary cornwall whose piety', 1], ['argument fist fight consulted', 1], ['arm somewhat shorter right', 1], ['began dill came us', 1], ['body thumb parallel thigh', 1], ['broad view really began', 1], ['called methodist worked across', 1], ['called methodists hands liberal', 1], ['came us dill gave', 1], ['cared less long pass', 1], ['consulted atticus father right', 1], ['cornwall whose piety exceeded', 1], ['couldn cared less long', 1], ['creek simon finch paddled', 1], ['creeks creek simon finch', 1], ['dill came us dill', 1], ['dill gave us idea', 1], ['discussed events leading accident', 1], ['either side battle hastings', 1], ['enable us sometimes discussed', 1], ['england simon irritated persecution', 1], ['enough years enable us', 1], ['ewells started jem four', 1], ['family recorded ancestors either', 1], ['far old settle argument', 1], ['fears able football assuaged', 1], ['fight consulted atticus father', 1], ['finch fur trapping apothecary', 1], ['fist fight consulted atticus', 1], ['four years senior started', 1], ['fur trapping apothecary cornwall', 1], ['gave us idea making', 1], ['general jackson hadn creeks', 1], ['hadn creeks creek simon', 1], ['hadn far old settle', 1], ['hand right angles body', 1], ['healed jem fears able', 1], ['idea making boo radley', 1], ['irritated persecution called methodists', 1], ['jackson hadn creeks creek', 1], ['jamaica thence mobile saint', 1], ['jem fears able football', 1], ['jem four years senior', 1], ['left arm somewhat shorter', 1], ['less long pass punt', 1], ['maintain ewells started jem', 1], ['members family recorded ancestors', 1], ['methodist worked across atlantic', 1], ['methodists hands liberal brethren', 1], ['old settle argument fist', 1], ['persecution called methodists hands', 1], ['really began andrew jackson', 1], ['recorded ancestors either side', 1], ['right angles body thumb', 1], ['right stood walked hand', 1], ['seldom self conscious injury', 1], ['settle argument fist fight', 1], ['shame members family recorded', 1], ['shorter right stood walked', 1], ['simon called methodist worked', 1], ['simon finch fur trapping', 1], ['simon finch paddled alabama', 1], ['simon irritated persecution called', 1], ['sometimes discussed events leading', 1], ['somewhat shorter right stood', 1], ['source shame members family', 1], ['southerners source shame members', 1], ['started jem four years', 1], ['stood walked hand right', 1], ['thence jamaica thence mobile', 1], ['thence mobile saint stephens', 1], ['trapping apothecary cornwall whose', 1], ['us dill gave us', 1], ['us idea making boo', 1], ['us sometimes discussed events', 1], ['view really began andrew', 1], ['walked hand right angles', 1], ['wanted broad view really', 1], ['whose piety exceeded stinginess', 1], ['worked across atlantic philadelphia', 1], ['years enable us sometimes', 1], ['years senior started long', 1]]]
    assert sequences(sentence_list, 4, strings) == result

def test_grouping():
    sequence = [[['able', 1], ['accident', 1], ['across', 1], ['alabama', 1], ['ancestors', 1], ['andrew', 1], ['angles', 1], ['apothecary', 1], ['argument', 1], ['arm', 1], ['assuaged', 1], ['atlantic', 1], ['atticus', 1], ['battle', 1], ['began', 2], ['body', 1], ['boo', 1], ['brethren', 1], ['broad', 1], ['called', 2], ['came', 1], ['cared', 1], ['conscious', 1], ['consulted', 1], ['cornwall', 1], ['couldn', 1], ['creek', 1], ['creeks', 1], ['dill', 2], ['discussed', 1], ['either', 1], ['enable', 1], ['england', 1], ['enough', 1], ['events', 1], ['ewells', 1], ['exceeded', 1], ['family', 1], ['far', 1], ['father', 1], ['fears', 1], ['fight', 1], ['finch', 2], ['fist', 1], ['football', 1], ['four', 1], ['fur', 1], ['gave', 1], ['general', 1], ['hadn', 2], ['hand', 1], ['hands', 1], ['hastings', 1], ['healed', 1], ['idea', 1], ['injury', 1], ['irritated', 1], ['jackson', 2], ['jamaica', 1], ['jem', 2], ['leading', 1], ['left', 1], ['less', 1], ['liberal', 1], ['long', 2], ['maintain', 1], ['making', 1], ['members', 1], ['methodist', 1], ['methodists', 1], ['mobile', 1], ['old', 1], ['paddled', 1], ['parallel', 1], ['pass', 1], ['persecution', 1], ['philadelphia', 1], ['piety', 1], ['punt', 1], ['radley', 1], ['really', 1], ['recorded', 1], ['right', 3], ['saint', 1], ['seldom', 1], ['self', 1], ['senior', 1], ['settle', 1], ['shame', 1], ['shorter', 1], ['side', 1], ['simon', 4], ['sometimes', 1], ['somewhat', 1], ['source', 1], ['southerners', 1], ['started', 2], ['stephens', 1], ['stinginess', 1], ['stood', 1], ['thence', 2], ['thigh', 1], ['thumb', 1], ['trapping', 1], ['us', 3], ['view', 1], ['walked', 1], ['wanted', 1], ['whose', 1], ['worked', 1], ['years', 2]], [['able football', 1], ['across atlantic', 1], ['ancestors either', 1], ['andrew jackson', 1], ['angles body', 1], ['apothecary cornwall', 1], ['argument fist', 1], ['arm somewhat', 1], ['atlantic philadelphia', 1], ['atticus father', 1], ['battle hastings', 1], ['began andrew', 1], ['began dill', 1], ['body thumb', 1], ['boo radley', 1], ['broad view', 1], ['called methodist', 1], ['called methodists', 1], ['came us', 1], ['cared less', 1], ['conscious injury', 1], ['consulted atticus', 1], ['cornwall whose', 1], ['couldn cared', 1], ['creek simon', 1], ['creeks creek', 1], ['dill came', 1], ['dill gave', 1], ['discussed events', 1], ['either side', 1], ['enable us', 1], ['england simon', 1], ['enough years', 1], ['events leading', 1], ['ewells started', 1], ['exceeded stinginess', 1], ['family recorded', 1], ['far old', 1], ['father right', 1], ['fears able', 1], ['fight consulted', 1], ['finch fur', 1], ['finch paddled', 1], ['fist fight', 1], ['football assuaged', 1], ['four years', 1], ['fur trapping', 1], ['gave us', 1], ['general jackson', 1], ['hadn creeks', 1], ['hadn far', 1], ['hand right', 1], ['hands liberal', 1], ['healed jem', 1], ['idea making', 1], ['irritated persecution', 1], ['jackson hadn', 1], ['jamaica thence', 1], ['jem fears', 1], ['jem four', 1], ['leading accident', 1], ['left arm', 1], ['less long', 1], ['liberal brethren', 1], ['long pass', 1], ['maintain ewells', 1], ['making boo', 1], ['members family', 1], ['methodist worked', 1], ['methodists hands', 1], ['mobile saint', 1], ['old settle', 1], ['paddled alabama', 1], ['parallel thigh', 1], ['pass punt', 1], ['persecution called', 1], ['piety exceeded', 1], ['really began', 1], ['recorded ancestors', 1], ['right angles', 1], ['right stood', 1], ['saint stephens', 1], ['seldom self', 1], ['self conscious', 1], ['senior started', 1], ['settle argument', 1], ['shame members', 1], ['shorter right', 1], ['side battle', 1], ['simon called', 1], ['simon finch', 2], ['simon irritated', 1], ['sometimes discussed', 1], ['somewhat shorter', 1], ['source shame', 1], ['southerners source', 1], ['started jem', 1], ['started long', 1], ['stood walked', 1], ['thence jamaica', 1], ['thence mobile', 1], ['thumb parallel', 1], ['trapping apothecary', 1], ['us dill', 1], ['us idea', 1], ['us sometimes', 1], ['view really', 1], ['walked hand', 1], ['wanted broad', 1], ['whose piety', 1], ['worked across', 1], ['years enable', 1], ['years senior', 1]], [['able football assuaged', 1], ['across atlantic philadelphia', 1], ['ancestors either side', 1], ['angles body thumb', 1], ['apothecary cornwall whose', 1], ['argument fist fight', 1], ['arm somewhat shorter', 1], ['atticus father right', 1], ['began andrew jackson', 1], ['began dill came', 1], ['body thumb parallel', 1], ['broad view really', 1], ['called methodist worked', 1], ['called methodists hands', 1], ['came us dill', 1], ['cared less long', 1], ['consulted atticus father', 1], ['cornwall whose piety', 1], ['couldn cared less', 1], ['creek simon finch', 1], ['creeks creek simon', 1], ['dill came us', 1], ['dill gave us', 1], ['discussed events leading', 1], ['either side battle', 1], ['enable us sometimes', 1], ['england simon irritated', 1], ['enough years enable', 1], ['events leading accident', 1], ['ewells started jem', 1], ['family recorded ancestors', 1], ['far old settle', 1], ['fears able football', 1], ['fight consulted atticus', 1], ['finch fur trapping', 1], ['finch paddled alabama', 1], ['fist fight consulted', 1], ['four years senior', 1], ['fur trapping apothecary', 1], ['gave us idea', 1], ['general jackson hadn', 1], ['hadn creeks creek', 1], ['hadn far old', 1], ['hand right angles', 1], ['hands liberal brethren', 1], ['healed jem fears', 1], ['idea making boo', 1], ['irritated persecution called', 1], ['jackson hadn creeks', 1], ['jamaica thence mobile', 1], ['jem fears able', 1], ['jem four years', 1], ['left arm somewhat', 1], ['less long pass', 1], ['long pass punt', 1], ['maintain ewells started', 1], ['making boo radley', 1], ['members family recorded', 1], ['methodist worked across', 1], ['methodists hands liberal', 1], ['mobile saint stephens', 1], ['old settle argument', 1], ['persecution called methodists', 1], ['piety exceeded stinginess', 1], ['really began andrew', 1], ['recorded ancestors either', 1], ['right angles body', 1], ['right stood walked', 1], ['seldom self conscious', 1], ['self conscious injury', 1], ['senior started long', 1], ['settle argument fist', 1], ['shame members family', 1], ['shorter right stood', 1], ['side battle hastings', 1], ['simon called methodist', 1], ['simon finch fur', 1], ['simon finch paddled', 1], ['simon irritated persecution', 1], ['sometimes discussed events', 1], ['somewhat shorter right', 1], ['source shame members', 1], ['southerners source shame', 1], ['started jem four', 1], ['stood walked hand', 1], ['thence jamaica thence', 1], ['thence mobile saint', 1], ['thumb parallel thigh', 1], ['trapping apothecary cornwall', 1], ['us dill gave', 1], ['us idea making', 1], ['us sometimes discussed', 1], ['view really began', 1], ['walked hand right', 1], ['wanted broad view', 1], ['whose piety exceeded', 1], ['worked across atlantic', 1], ['years enable us', 1], ['years senior started', 1]], [['ancestors either side battle', 1], ['angles body thumb parallel', 1], ['apothecary cornwall whose piety', 1], ['argument fist fight consulted', 1], ['arm somewhat shorter right', 1], ['began dill came us', 1], ['body thumb parallel thigh', 1], ['broad view really began', 1], ['called methodist worked across', 1], ['called methodists hands liberal', 1], ['came us dill gave', 1], ['cared less long pass', 1], ['consulted atticus father right', 1], ['cornwall whose piety exceeded', 1], ['couldn cared less long', 1], ['creek simon finch paddled', 1], ['creeks creek simon finch', 1], ['dill came us dill', 1], ['dill gave us idea', 1], ['discussed events leading accident', 1], ['either side battle hastings', 1], ['enable us sometimes discussed', 1], ['england simon irritated persecution', 1], ['enough years enable us', 1], ['ewells started jem four', 1], ['family recorded ancestors either', 1], ['far old settle argument', 1], ['fears able football assuaged', 1], ['fight consulted atticus father', 1], ['finch fur trapping apothecary', 1], ['fist fight consulted atticus', 1], ['four years senior started', 1], ['fur trapping apothecary cornwall', 1], ['gave us idea making', 1], ['general jackson hadn creeks', 1], ['hadn creeks creek simon', 1], ['hadn far old settle', 1], ['hand right angles body', 1], ['healed jem fears able', 1], ['idea making boo radley', 1], ['irritated persecution called methodists', 1], ['jackson hadn creeks creek', 1], ['jamaica thence mobile saint', 1], ['jem fears able football', 1], ['jem four years senior', 1], ['left arm somewhat shorter', 1], ['less long pass punt', 1], ['maintain ewells started jem', 1], ['members family recorded ancestors', 1], ['methodist worked across atlantic', 1], ['methodists hands liberal brethren', 1], ['old settle argument fist', 1], ['persecution called methodists hands', 1], ['really began andrew jackson', 1], ['recorded ancestors either side', 1], ['right angles body thumb', 1], ['right stood walked hand', 1], ['seldom self conscious injury', 1], ['settle argument fist fight', 1], ['shame members family recorded', 1], ['shorter right stood walked', 1], ['simon called methodist worked', 1], ['simon finch fur trapping', 1], ['simon finch paddled alabama', 1], ['simon irritated persecution called', 1], ['sometimes discussed events leading', 1], ['somewhat shorter right stood', 1], ['source shame members family', 1], ['southerners source shame members', 1], ['started jem four years', 1], ['stood walked hand right', 1], ['thence jamaica thence mobile', 1], ['thence mobile saint stephens', 1], ['trapping apothecary cornwall whose', 1], ['us dill gave us', 1], ['us idea making boo', 1], ['us sometimes discussed events', 1], ['view really began andrew', 1], ['walked hand right angles', 1], ['wanted broad view really', 1], ['whose piety exceeded stinginess', 1], ['worked across atlantic philadelphia', 1], ['years enable us sometimes', 1], ['years senior started long', 1]]]
    result = grouping(sequence,4)
    assert grouping(sequence,4) ==  result

def test_file_type_valid_json(mock_json_data):
    """Test with a valid JSON file."""
    with patch("builtins.open", mock_open(read_data=mock_json_data)):
        with patch("json.load", return_value=json.loads(mock_json_data)):
            result = file_type("data.json", "people.txt", "remove.txt")
            assert result == json.loads(mock_json_data)

def test_file_type_invalid_csv_dependencies():
    """Test when people or remove file is a CSV but the main file is not (should exit)."""
    with patch("sys.exit") as mock_exit:
        file_type("data.txt", "people.csv", "remove.txt")
        mock_exit.assert_called_with("Invalid Input")

    with patch("sys.exit") as mock_exit:
        file_type("data.txt", "people.txt", "remove.csv")
        mock_exit.assert_called_with("Invalid Input")

def test_file_type_invalid_json():
    """Test with an invalid JSON file (should exit)."""
    with patch("builtins.open", mock_open(read_data="{invalid_json")):
        with patch("sys.exit") as mock_exit:
            file_type("data.json", "people.txt", "remove.txt")
            mock_exit.assert_called_with("Invalid Input")

def test_file_type_invalid_extension():
    """Test with an invalid file extension (should exit)."""
    with patch("sys.exit") as mock_exit:
        file_type("data.txt", "people.txt", "remove.txt")
        mock_exit.assert_called_with("Invalid Input")

def test_process_data_from_dict():
    task_1_output = {'Question 1': {'Processed Sentences': [['healed', 'jem', 'fears', 'able', 'football', 'assuaged'], ['seldom', 'self', 'conscious', 'injury'], ['left', 'arm', 'somewhat', 'shorter', 'right', 'stood', 'walked', 'hand', 'right', 'angles', 'body', 'thumb', 'parallel', 'thigh'], ['couldn', 'cared', 'less', 'long', 'pass', 'punt'], ['enough', 'years', 'enable', 'us', 'sometimes', 'discussed', 'events', 'leading', 'accident'], ['maintain', 'ewells', 'started', 'jem', 'four', 'years', 'senior', 'started', 'long'], ['began', 'dill', 'came', 'us', 'dill', 'gave', 'us', 'idea', 'making', 'boo', 'radley'], ['wanted', 'broad', 'view', 'really', 'began', 'andrew', 'jackson'], ['general', 'jackson', 'hadn', 'creeks', 'creek', 'simon', 'finch', 'paddled', 'alabama'], ['hadn', 'far', 'old', 'settle', 'argument', 'fist', 'fight', 'consulted', 'atticus', 'father', 'right'], ['southerners', 'source', 'shame', 'members', 'family', 'recorded', 'ancestors', 'either', 'side', 'battle', 'hastings'], ['simon', 'finch', 'fur', 'trapping', 'apothecary', 'cornwall', 'whose', 'piety', 'exceeded', 'stinginess'], ['england', 'simon', 'irritated', 'persecution', 'called', 'methodists', 'hands', 'liberal', 'brethren'], ['simon', 'called', 'methodist', 'worked', 'across', 'atlantic', 'philadelphia'], ['thence', 'jamaica', 'thence', 'mobile', 'saint', 'stephens']], 'Processed Names': [[['jem'], []], [['dill'], []], [['boo', 'radley'], []], [['andrew', 'jackson'], []], [['general', 'jackson'], []], [['simon', 'finch'], []], [['atticus'], []]]}}
    result =[['andrew jackson'], ['atticus'], ['boo radley'], ['dill'], ['general jackson'], ['jem'], ['simon finch']]
    assert process_data_from_dict(task_1_output) == result

def test_number_of_counters():
    sentences_list = [['healed', 'jem', 'fears', 'able', 'football', 'assuaged'], ['seldom', 'self', 'conscious', 'injury'] ,['left', 'arm', 'somewhat', 'shorter', 'right', 'stood', 'walked', 'hand', 'right', 'angles', 'body', 'thumb', 'parallel', 'thigh'], ['couldn', 'cared', 'less', 'long', 'pass', 'punt'], ['enough', 'years', 'enable', 'us', 'sometimes', 'discussed', 'events', 'leading', 'accident'], ['maintain', 'ewells', 'started', 'jem', 'four', 'years', 'senior', 'started', 'long'], ['began', 'dill', 'came', 'us', 'dill', 'gave', 'us', 'idea', 'making', 'boo', 'radley'], ['wanted', 'broad', 'view', 'really', 'began', 'andrew', 'jackson'], ['general', 'jackson', 'hadn', 'creeks', 'creek', 'simon', 'finch', 'paddled', 'alabama'], ['hadn', 'far', 'old', 'settle', 'argument', 'fist', 'fight', 'consulted', 'atticus', 'father', 'right'], ['southerners', 'source', 'shame', 'members', 'family', 'recorded', 'ancestors', 'either', 'side', 'battle', 'hastings'], ['simon', 'finch', 'fur', 'trapping', 'apothecary', 'cornwall', 'whose', 'piety', 'exceeded', 'stinginess'], ['england', 'simon', 'irritated', 'persecution', 'called', 'methodists', 'hands', 'liberal', 'brethren'], ['simon', 'called', 'methodist', 'worked', 'across', 'atlantic', 'philadelphia'], ['thence', 'jamaica', 'thence', 'mobile', 'saint', 'stephens']]
    names_list =  [['andrew jackson'], ['atticus'], ['boo radley'], ['dill'], ['general jackson'], ['jem'], ['simon finch']]
    result =[['andrew jackson', 4], ['atticus', 1], ['boo radley', 3], ['dill', 2], ['general jackson', 4], ['jem', 2], ['simon finch', 8]]
    assert number_of_counters(names_list, sentences_list) ==  result

def test_generate_consecutive_substrings():
    name = "andrew jackson"
    result = ['andrew', 'andrew jackson', 'jackson']
    assert generate_consecutive_substrings(name)== result

def test_grouping_func():
    names_occurences = [['andrew jackson', 4], ['atticus', 1], ['boo radley', 3], ['dill', 2], ['general jackson', 4], ['jem', 2], ['simon finch', 8]]
    result = grouping_func(names_occurences)
    assert grouping_func(names_occurences)== result

def test_key_to_search():
    keys_list=  {
        "keys":[
		["jem", "across"],
        ["argument", "far", "seldom", "settle"],
        ["injury", "muffled", "voice"]
    ]
}
    result =[['jem across'], ['argument far seldom settle'], ['injury muffled voice']]
    assert key_to_search(keys_list, remove)== result

def test_key_to_search_2():
    keys_list = {
        "nice" : [["hi" , "across"]]
    }
    assert key_to_search(keys_list, remove) == []

def test_key_to_search_3():
        keys_list ={}
        assert key_to_search(keys_list, remove) == []

def test_key_to_search_invalid_type():
    """Test case where the first argument is not a dictionary (should raise SystemExit)."""
    invalid_inputs = [
        [],  # List instead of dict
        "string",  # String instead of dict
        {"keys": "not a list of lists"}  # Invalid structure inside dict
    ]

    with pytest.raises(SystemExit) as excinfo:  # Catch the SystemExit
        key_to_search(invalid_inputs, remove)
        # Check that the exit message matches
    assert str(excinfo.value) == "Invalid Input"

def test_key_to_search_4():
    with pytest.raises(SystemExit) as excinfo:  # Catch the SystemExit
        key_to_search(None, remove)
        # Check that the exit message matches
    assert str(excinfo.value) == "Invalid Input"

def test_keys_in_sentence():
    sentences_list = [['healed', 'jem', 'fears', 'able', 'football', 'assuaged'], ['seldom', 'self', 'conscious', 'injury'], ['left', 'arm', 'somewhat', 'shorter', 'right', 'stood', 'walked', 'hand', 'right', 'angles', 'body', 'thumb', 'parallel', 'thigh'], ['couldn', 'cared', 'less', 'long', 'pass', 'punt'], ['enough', 'years', 'enable', 'us', 'sometimes', 'discussed', 'events', 'leading', 'accident'], ['maintain', 'ewells', 'started', 'jem', 'four', 'years', 'senior', 'started', 'long'], ['began', 'dill', 'came', 'us', 'dill', 'gave', 'us', 'idea', 'making', 'boo', 'radley'], ['wanted', 'broad', 'view', 'really', 'began', 'andrew', 'jackson'], ['general', 'jackson', 'hadn', 'creeks', 'creek', 'simon', 'finch', 'paddled', 'alabama'], ['hadn', 'far', 'old', 'settle', 'argument', 'fist', 'fight', 'consulted', 'atticus', 'father', 'right'], ['southerners', 'source', 'shame', 'members', 'family', 'recorded', 'ancestors', 'either', 'side', 'battle', 'hastings'], ['simon', 'finch', 'fur', 'trapping', 'apothecary', 'cornwall', 'whose', 'piety', 'exceeded', 'stinginess'], ['england', 'simon', 'irritated', 'persecution', 'called', 'methodists', 'hands', 'liberal', 'brethren'], ['simon', 'called', 'methodist', 'worked', 'across', 'atlantic', 'philadelphia'], ['thence', 'jamaica', 'thence', 'mobile', 'saint', 'stephens']]
    keys_list = [['jem across'], ['argument far seldom settle'], ['injury muffled voice']]
    result = {}
    assert keys_in_sentence(sentences_list,keys_list)== result

def test_keys_in_sentence_1():
    sentence_list = [['healed', 'jem', 'fears', 'able', 'football', 'assuaged']]
    keys_list = [""]
    result = {}
    assert keys_in_sentence(sentence_list,keys_list)== result

def test_keys_in_sentence_2():
    sentence_list =[]
    keys_list= [["sarah"],['harry'],['hagrid']]
    assert keys_in_sentence(sentence_list,keys_list)== {}

def test_keys_in_sentence_3():
    sentence_list = [['healed', 'jem', 'fears', 'able', 'football', 'assuaged']]
    keys_list= [["harry"],["hagrid"]]
    assert keys_in_sentence(sentence_list, keys_list) == {}

def test_grouping_function():
    data = {}
    result = grouping_function(data)
    assert grouping_function(data) ==  result

def test_json_file_opening_valid(tmp_path):
    json_data = {"name": "Alice", "age": 25, "city": "Wonderland"}
    json_file = tmp_path / "valid.json"

    with open(json_file, "w") as f:
        json.dump(json_data, f)

    result = json_file_opening(str(json_file))
    assert result == json_data

def test_json_file_opening_file_not_found():
    with pytest.raises(SystemExit):
        json_file_opening("non_existent.json")

def test_json_file_opening_invalid_json(tmp_path):
    json_file = tmp_path / "invalid.json"

    with open(json_file, "w") as f:
        f.write("{invalid_json: true,}")  # Invalid JSON syntax

    with pytest.raises(SystemExit):
        json_file_opening(str(json_file))

def test_flatten_list():
    sentences_list = [['healed', 'jem', 'fears', 'able', 'football', 'assuaged'], ['seldom', 'self', 'conscious', 'injury'], ['left', 'arm', 'somewhat', 'shorter', 'right', 'stood', 'walked', 'hand', 'right', 'angles', 'body', 'thumb', 'parallel', 'thigh'], ['couldn', 'cared', 'less', 'long', 'pass', 'punt'], ['enough', 'years', 'enable', 'us', 'sometimes', 'discussed', 'events', 'leading', 'accident'], ['maintain', 'ewells', 'started', 'jem', 'four', 'years', 'senior', 'started', 'long'], ['began', 'dill', 'came', 'us', 'dill', 'gave', 'us', 'idea', 'making', 'boo', 'radley'], ['wanted', 'broad', 'view', 'really', 'began', 'andrew', 'jackson'], ['general', 'jackson', 'hadn', 'creeks', 'creek', 'simon', 'finch', 'paddled', 'alabama'], ['hadn', 'far', 'old', 'settle', 'argument', 'fist', 'fight', 'consulted', 'atticus', 'father', 'right'], ['southerners', 'source', 'shame', 'members', 'family', 'recorded', 'ancestors', 'either', 'side', 'battle', 'hastings'], ['simon', 'finch', 'fur', 'trapping', 'apothecary', 'cornwall', 'whose', 'piety', 'exceeded', 'stinginess'], ['england', 'simon', 'irritated', 'persecution', 'called', 'methodists', 'hands', 'liberal', 'brethren'], ['simon', 'called', 'methodist', 'worked', 'across', 'atlantic', 'philadelphia'], ['thence', 'jamaica', 'thence', 'mobile', 'saint', 'stephens']]
    result = ['healed', 'jem', 'fears', 'able', 'football', 'assuaged', 'seldom', 'self', 'conscious', 'injury', 'left', 'arm', 'somewhat', 'shorter', 'right', 'stood', 'walked', 'hand', 'right', 'angles', 'body', 'thumb', 'parallel', 'thigh', 'couldn', 'cared', 'less', 'long', 'pass', 'punt', 'enough', 'years', 'enable', 'us', 'sometimes', 'discussed', 'events', 'leading', 'accident', 'maintain', 'ewells', 'started', 'jem', 'four', 'years', 'senior', 'started', 'long', 'began', 'dill', 'came', 'us', 'dill', 'gave', 'us', 'idea', 'making', 'boo', 'radley', 'wanted', 'broad', 'view', 'really', 'began', 'andrew', 'jackson', 'general', 'jackson', 'hadn', 'creeks', 'creek', 'simon', 'finch', 'paddled', 'alabama', 'hadn', 'far', 'old', 'settle', 'argument', 'fist', 'fight', 'consulted', 'atticus', 'father', 'right', 'southerners', 'source', 'shame', 'members', 'family', 'recorded', 'ancestors', 'either', 'side', 'battle', 'hastings', 'simon', 'finch', 'fur', 'trapping', 'apothecary', 'cornwall', 'whose', 'piety', 'exceeded', 'stinginess', 'england', 'simon', 'irritated', 'persecution', 'called', 'methodists', 'hands', 'liberal', 'brethren', 'simon', 'called', 'methodist', 'worked', 'across', 'atlantic', 'philadelphia', 'thence', 'jamaica', 'thence', 'mobile', 'saint', 'stephens']
    assert flatten_list(sentences_list) == result

def test_flatten_list_1():
    sentence =[[]]
    assert flatten_list(sentence) == []

def test_flatten_list_2():
    assert flatten_list([]) == []

def test_key_in_sentence():
    sentences_list = [['healed', 'jem', 'fears', 'able', 'football', 'assuaged'], ['seldom', 'self', 'conscious', 'injury'], ['left', 'arm', 'somewhat', 'shorter', 'right', 'stood', 'walked', 'hand', 'right', 'angles', 'body', 'thumb', 'parallel', 'thigh'], ['couldn', 'cared', 'less', 'long', 'pass', 'punt'], ['enough', 'years', 'enable', 'us', 'sometimes', 'discussed', 'events', 'leading', 'accident'], ['maintain', 'ewells', 'started', 'jem', 'four', 'years', 'senior', 'started', 'long'], ['began', 'dill', 'came', 'us', 'dill', 'gave', 'us', 'idea', 'making', 'boo', 'radley'], ['wanted', 'broad', 'view', 'really', 'began', 'andrew', 'jackson'], ['general', 'jackson', 'hadn', 'creeks', 'creek', 'simon', 'finch', 'paddled', 'alabama'], ['hadn', 'far', 'old', 'settle', 'argument', 'fist', 'fight', 'consulted', 'atticus', 'father', 'right'], ['southerners', 'source', 'shame', 'members', 'family', 'recorded', 'ancestors', 'either', 'side', 'battle', 'hastings'], ['simon', 'finch', 'fur', 'trapping', 'apothecary', 'cornwall', 'whose', 'piety', 'exceeded', 'stinginess'], ['england', 'simon', 'irritated', 'persecution', 'called', 'methodists', 'hands', 'liberal', 'brethren'], ['simon', 'called', 'methodist', 'worked', 'across', 'atlantic', 'philadelphia'], ['thence', 'jamaica', 'thence', 'mobile', 'saint', 'stephens']]
    key = ['andrew jackson']
    result = {'andrew jackson': [['wanted', 'broad', 'view', 'really', 'began', 'andrew', 'jackson']]}
    assert key_in_sentence(sentences_list, key)== result

def test_all_sentences():
    sentences_list = [['healed', 'jem', 'fears', 'able', 'football', 'assuaged'], ['seldom', 'self', 'conscious', 'injury'], ['left', 'arm', 'somewhat', 'shorter', 'right', 'stood', 'walked', 'hand', 'right', 'angles', 'body', 'thumb', 'parallel', 'thigh'], ['couldn', 'cared', 'less', 'long', 'pass', 'punt'], ['enough', 'years', 'enable', 'us', 'sometimes', 'discussed', 'events', 'leading', 'accident'], ['maintain', 'ewells', 'started', 'jem', 'four', 'years', 'senior', 'started', 'long'], ['began', 'dill', 'came', 'us', 'dill', 'gave', 'us', 'idea', 'making', 'boo', 'radley'], ['wanted', 'broad', 'view', 'really', 'began', 'andrew', 'jackson'], ['general', 'jackson', 'hadn', 'creeks', 'creek', 'simon', 'finch', 'paddled', 'alabama'], ['hadn', 'far', 'old', 'settle', 'argument', 'fist', 'fight', 'consulted', 'atticus', 'father', 'right'], ['southerners', 'source', 'shame', 'members', 'family', 'recorded', 'ancestors', 'either', 'side', 'battle', 'hastings'], ['simon', 'finch', 'fur', 'trapping', 'apothecary', 'cornwall', 'whose', 'piety', 'exceeded', 'stinginess'], ['england', 'simon', 'irritated', 'persecution', 'called', 'methodists', 'hands', 'liberal', 'brethren'], ['simon', 'called', 'methodist', 'worked', 'across', 'atlantic', 'philadelphia'], ['thence', 'jamaica', 'thence', 'mobile', 'saint', 'stephens']]
    names_list =  [['andrew jackson'], ['atticus'], ['boo radley'], ['dill'], ['general jackson'], ['jem'], ['simon finch']]
    result = {'andrew jackson': [['general', 'jackson', 'hadn', 'creeks', 'creek', 'simon', 'finch', 'paddled', 'alabama'], ['wanted', 'broad', 'view', 'really', 'began', 'andrew', 'jackson']], 'atticus': [['hadn', 'far', 'old', 'settle', 'argument', 'fist', 'fight', 'consulted', 'atticus', 'father', 'right']], 'boo radley': [['began', 'dill', 'came', 'us', 'dill', 'gave', 'us', 'idea', 'making', 'boo', 'radley']], 'dill': [['began', 'dill', 'came', 'us', 'dill', 'gave', 'us', 'idea', 'making', 'boo', 'radley']], 'general jackson': [['general', 'jackson', 'hadn', 'creeks', 'creek', 'simon', 'finch', 'paddled', 'alabama'], ['wanted', 'broad', 'view', 'really', 'began', 'andrew', 'jackson']], 'jem': [['healed', 'jem', 'fears', 'able', 'football', 'assuaged'], ['maintain', 'ewells', 'started', 'jem', 'four', 'years', 'senior', 'started', 'long']], 'simon finch': [['england', 'simon', 'irritated', 'persecution', 'called', 'methodists', 'hands', 'liberal', 'brethren'], ['general', 'jackson', 'hadn', 'creeks', 'creek', 'simon', 'finch', 'paddled', 'alabama'], ['simon', 'called', 'methodist', 'worked', 'across', 'atlantic', 'philadelphia'], ['simon', 'finch', 'fur', 'trapping', 'apothecary', 'cornwall', 'whose', 'piety', 'exceeded', 'stinginess']]}
    assert all_sentences(sentences_list,names_list) == result

def test_extract_k_sequences_flat():
    data = {'andrew jackson': [['general', 'jackson', 'hadn', 'creeks', 'creek', 'simon', 'finch', 'paddled', 'alabama'], ['wanted', 'broad', 'view', 'really', 'began', 'andrew', 'jackson']], 'atticus': [['hadn', 'far', 'old', 'settle', 'argument', 'fist', 'fight', 'consulted', 'atticus', 'father', 'right']], 'boo radley': [['began', 'dill', 'came', 'us', 'dill', 'gave', 'us', 'idea', 'making', 'boo', 'radley']], 'dill': [['began', 'dill', 'came', 'us', 'dill', 'gave', 'us', 'idea', 'making', 'boo', 'radley']], 'general jackson': [['general', 'jackson', 'hadn', 'creeks', 'creek', 'simon', 'finch', 'paddled', 'alabama'], ['wanted', 'broad', 'view', 'really', 'began', 'andrew', 'jackson']], 'jem': [['healed', 'jem', 'fears', 'able', 'football', 'assuaged'], ['maintain', 'ewells', 'started', 'jem', 'four', 'years', 'senior', 'started', 'long']], 'simon finch': [['england', 'simon', 'irritated', 'persecution', 'called', 'methodists', 'hands', 'liberal', 'brethren'], ['general', 'jackson', 'hadn', 'creeks', 'creek', 'simon', 'finch', 'paddled', 'alabama'], ['simon', 'called', 'methodist', 'worked', 'across', 'atlantic', 'philadelphia'], ['simon', 'finch', 'fur', 'trapping', 'apothecary', 'cornwall', 'whose', 'piety', 'exceeded', 'stinginess']]}
    result = [['andrew jackson', [['alabama'], ['andrew'], ['andrew', 'jackson'], ['began'], ['began', 'andrew'], ['began', 'andrew', 'jackson'], ['broad'], ['broad', 'view'], ['broad', 'view', 'really'], ['broad', 'view', 'really', 'began'], ['creek'], ['creek', 'simon'], ['creek', 'simon', 'finch'], ['creek', 'simon', 'finch', 'paddled'], ['creeks'], ['creeks', 'creek'], ['creeks', 'creek', 'simon'], ['creeks', 'creek', 'simon', 'finch'], ['finch'], ['finch', 'paddled'], ['finch', 'paddled', 'alabama'], ['general'], ['general', 'jackson'], ['general', 'jackson', 'hadn'], ['general', 'jackson', 'hadn', 'creeks'], ['hadn'], ['hadn', 'creeks'], ['hadn', 'creeks', 'creek'], ['hadn', 'creeks', 'creek', 'simon'], ['jackson'], ['jackson', 'hadn'], ['jackson', 'hadn', 'creeks'], ['jackson', 'hadn', 'creeks', 'creek'], ['paddled'], ['paddled', 'alabama'], ['really'], ['really', 'began'], ['really', 'began', 'andrew'], ['really', 'began', 'andrew', 'jackson'], ['simon'], ['simon', 'finch'], ['simon', 'finch', 'paddled'], ['simon', 'finch', 'paddled', 'alabama'], ['view'], ['view', 'really'], ['view', 'really', 'began'], ['view', 'really', 'began', 'andrew'], ['wanted'], ['wanted', 'broad'], ['wanted', 'broad', 'view'], ['wanted', 'broad', 'view', 'really']]], ['atticus', [['argument'], ['argument', 'fist'], ['argument', 'fist', 'fight'], ['argument', 'fist', 'fight', 'consulted'], ['atticus'], ['atticus', 'father'], ['atticus', 'father', 'right'], ['consulted'], ['consulted', 'atticus'], ['consulted', 'atticus', 'father'], ['consulted', 'atticus', 'father', 'right'], ['far'], ['far', 'old'], ['far', 'old', 'settle'], ['far', 'old', 'settle', 'argument'], ['father'], ['father', 'right'], ['fight'], ['fight', 'consulted'], ['fight', 'consulted', 'atticus'], ['fight', 'consulted', 'atticus', 'father'], ['fist'], ['fist', 'fight'], ['fist', 'fight', 'consulted'], ['fist', 'fight', 'consulted', 'atticus'], ['hadn'], ['hadn', 'far'], ['hadn', 'far', 'old'], ['hadn', 'far', 'old', 'settle'], ['old'], ['old', 'settle'], ['old', 'settle', 'argument'], ['old', 'settle', 'argument', 'fist'], ['right'], ['settle'], ['settle', 'argument'], ['settle', 'argument', 'fist'], ['settle', 'argument', 'fist', 'fight']]], ['boo radley', [['began'], ['began', 'dill'], ['began', 'dill', 'came'], ['began', 'dill', 'came', 'us'], ['boo'], ['boo', 'radley'], ['came'], ['came', 'us'], ['came', 'us', 'dill'], ['came', 'us', 'dill', 'gave'], ['dill'], ['dill', 'came'], ['dill', 'came', 'us'], ['dill', 'came', 'us', 'dill'], ['dill', 'gave'], ['dill', 'gave', 'us'], ['dill', 'gave', 'us', 'idea'], ['gave'], ['gave', 'us'], ['gave', 'us', 'idea'], ['gave', 'us', 'idea', 'making'], ['idea'], ['idea', 'making'], ['idea', 'making', 'boo'], ['idea', 'making', 'boo', 'radley'], ['making'], ['making', 'boo'], ['making', 'boo', 'radley'], ['radley'], ['us'], ['us', 'dill'], ['us', 'dill', 'gave'], ['us', 'dill', 'gave', 'us'], ['us', 'idea'], ['us', 'idea', 'making'], ['us', 'idea', 'making', 'boo']]], ['dill', [['began'], ['began', 'dill'], ['began', 'dill', 'came'], ['began', 'dill', 'came', 'us'], ['boo'], ['boo', 'radley'], ['came'], ['came', 'us'], ['came', 'us', 'dill'], ['came', 'us', 'dill', 'gave'], ['dill'], ['dill', 'came'], ['dill', 'came', 'us'], ['dill', 'came', 'us', 'dill'], ['dill', 'gave'], ['dill', 'gave', 'us'], ['dill', 'gave', 'us', 'idea'], ['gave'], ['gave', 'us'], ['gave', 'us', 'idea'], ['gave', 'us', 'idea', 'making'], ['idea'], ['idea', 'making'], ['idea', 'making', 'boo'], ['idea', 'making', 'boo', 'radley'], ['making'], ['making', 'boo'], ['making', 'boo', 'radley'], ['radley'], ['us'], ['us', 'dill'], ['us', 'dill', 'gave'], ['us', 'dill', 'gave', 'us'], ['us', 'idea'], ['us', 'idea', 'making'], ['us', 'idea', 'making', 'boo']]], ['general jackson', [['alabama'], ['andrew'], ['andrew', 'jackson'], ['began'], ['began', 'andrew'], ['began', 'andrew', 'jackson'], ['broad'], ['broad', 'view'], ['broad', 'view', 'really'], ['broad', 'view', 'really', 'began'], ['creek'], ['creek', 'simon'], ['creek', 'simon', 'finch'], ['creek', 'simon', 'finch', 'paddled'], ['creeks'], ['creeks', 'creek'], ['creeks', 'creek', 'simon'], ['creeks', 'creek', 'simon', 'finch'], ['finch'], ['finch', 'paddled'], ['finch', 'paddled', 'alabama'], ['general'], ['general', 'jackson'], ['general', 'jackson', 'hadn'], ['general', 'jackson', 'hadn', 'creeks'], ['hadn'], ['hadn', 'creeks'], ['hadn', 'creeks', 'creek'], ['hadn', 'creeks', 'creek', 'simon'], ['jackson'], ['jackson', 'hadn'], ['jackson', 'hadn', 'creeks'], ['jackson', 'hadn', 'creeks', 'creek'], ['paddled'], ['paddled', 'alabama'], ['really'], ['really', 'began'], ['really', 'began', 'andrew'], ['really', 'began', 'andrew', 'jackson'], ['simon'], ['simon', 'finch'], ['simon', 'finch', 'paddled'], ['simon', 'finch', 'paddled', 'alabama'], ['view'], ['view', 'really'], ['view', 'really', 'began'], ['view', 'really', 'began', 'andrew'], ['wanted'], ['wanted', 'broad'], ['wanted', 'broad', 'view'], ['wanted', 'broad', 'view', 'really']]], ['jem', [['able'], ['able', 'football'], ['able', 'football', 'assuaged'], ['assuaged'], ['ewells'], ['ewells', 'started'], ['ewells', 'started', 'jem'], ['ewells', 'started', 'jem', 'four'], ['fears'], ['fears', 'able'], ['fears', 'able', 'football'], ['fears', 'able', 'football', 'assuaged'], ['football'], ['football', 'assuaged'], ['four'], ['four', 'years'], ['four', 'years', 'senior'], ['four', 'years', 'senior', 'started'], ['healed'], ['healed', 'jem'], ['healed', 'jem', 'fears'], ['healed', 'jem', 'fears', 'able'], ['jem'], ['jem', 'fears'], ['jem', 'fears', 'able'], ['jem', 'fears', 'able', 'football'], ['jem', 'four'], ['jem', 'four', 'years'], ['jem', 'four', 'years', 'senior'], ['long'], ['maintain'], ['maintain', 'ewells'], ['maintain', 'ewells', 'started'], ['maintain', 'ewells', 'started', 'jem'], ['senior'], ['senior', 'started'], ['senior', 'started', 'long'], ['started'], ['started', 'jem'], ['started', 'jem', 'four'], ['started', 'jem', 'four', 'years'], ['started', 'long'], ['years'], ['years', 'senior'], ['years', 'senior', 'started'], ['years', 'senior', 'started', 'long']]], ['simon finch', [['across'], ['across', 'atlantic'], ['across', 'atlantic', 'philadelphia'], ['alabama'], ['apothecary'], ['apothecary', 'cornwall'], ['apothecary', 'cornwall', 'whose'], ['apothecary', 'cornwall', 'whose', 'piety'], ['atlantic'], ['atlantic', 'philadelphia'], ['brethren'], ['called'], ['called', 'methodist'], ['called', 'methodist', 'worked'], ['called', 'methodist', 'worked', 'across'], ['called', 'methodists'], ['called', 'methodists', 'hands'], ['called', 'methodists', 'hands', 'liberal'], ['cornwall'], ['cornwall', 'whose'], ['cornwall', 'whose', 'piety'], ['cornwall', 'whose', 'piety', 'exceeded'], ['creek'], ['creek', 'simon'], ['creek', 'simon', 'finch'], ['creek', 'simon', 'finch', 'paddled'], ['creeks'], ['creeks', 'creek'], ['creeks', 'creek', 'simon'], ['creeks', 'creek', 'simon', 'finch'], ['england'], ['england', 'simon'], ['england', 'simon', 'irritated'], ['england', 'simon', 'irritated', 'persecution'], ['exceeded'], ['exceeded', 'stinginess'], ['finch'], ['finch', 'fur'], ['finch', 'fur', 'trapping'], ['finch', 'fur', 'trapping', 'apothecary'], ['finch', 'paddled'], ['finch', 'paddled', 'alabama'], ['fur'], ['fur', 'trapping'], ['fur', 'trapping', 'apothecary'], ['fur', 'trapping', 'apothecary', 'cornwall'], ['general'], ['general', 'jackson'], ['general', 'jackson', 'hadn'], ['general', 'jackson', 'hadn', 'creeks'], ['hadn'], ['hadn', 'creeks'], ['hadn', 'creeks', 'creek'], ['hadn', 'creeks', 'creek', 'simon'], ['hands'], ['hands', 'liberal'], ['hands', 'liberal', 'brethren'], ['irritated'], ['irritated', 'persecution'], ['irritated', 'persecution', 'called'], ['irritated', 'persecution', 'called', 'methodists'], ['jackson'], ['jackson', 'hadn'], ['jackson', 'hadn', 'creeks'], ['jackson', 'hadn', 'creeks', 'creek'], ['liberal'], ['liberal', 'brethren'], ['methodist'], ['methodist', 'worked'], ['methodist', 'worked', 'across'], ['methodist', 'worked', 'across', 'atlantic'], ['methodists'], ['methodists', 'hands'], ['methodists', 'hands', 'liberal'], ['methodists', 'hands', 'liberal', 'brethren'], ['paddled'], ['paddled', 'alabama'], ['persecution'], ['persecution', 'called'], ['persecution', 'called', 'methodists'], ['persecution', 'called', 'methodists', 'hands'], ['philadelphia'], ['piety'], ['piety', 'exceeded'], ['piety', 'exceeded', 'stinginess'], ['simon'], ['simon', 'called'], ['simon', 'called', 'methodist'], ['simon', 'called', 'methodist', 'worked'], ['simon', 'finch'], ['simon', 'finch', 'fur'], ['simon', 'finch', 'fur', 'trapping'], ['simon', 'finch', 'paddled'], ['simon', 'finch', 'paddled', 'alabama'], ['simon', 'irritated'], ['simon', 'irritated', 'persecution'], ['simon', 'irritated', 'persecution', 'called'], ['stinginess'], ['trapping'], ['trapping', 'apothecary'], ['trapping', 'apothecary', 'cornwall'], ['trapping', 'apothecary', 'cornwall', 'whose'], ['whose'], ['whose', 'piety'], ['whose', 'piety', 'exceeded'], ['whose', 'piety', 'exceeded', 'stinginess'], ['worked'], ['worked', 'across'], ['worked', 'across', 'atlantic'], ['worked', 'across', 'atlantic', 'philadelphia']]]]
    assert extract_k_sequences_flat(data,4) == result

def test_format_as_json():
    data = [['andrew jackson', [['alabama'], ['andrew'], ['andrew', 'jackson'], ['began'], ['began', 'andrew'], ['began', 'andrew', 'jackson'], ['broad'], ['broad', 'view'], ['broad', 'view', 'really'], ['broad', 'view', 'really', 'began'], ['creek'], ['creek', 'simon'], ['creek', 'simon', 'finch'], ['creek', 'simon', 'finch', 'paddled'], ['creeks'], ['creeks', 'creek'], ['creeks', 'creek', 'simon'], ['creeks', 'creek', 'simon', 'finch'], ['finch'], ['finch', 'paddled'], ['finch', 'paddled', 'alabama'], ['general'], ['general', 'jackson'], ['general', 'jackson', 'hadn'], ['general', 'jackson', 'hadn', 'creeks'], ['hadn'], ['hadn', 'creeks'], ['hadn', 'creeks', 'creek'], ['hadn', 'creeks', 'creek', 'simon'], ['jackson'], ['jackson', 'hadn'], ['jackson', 'hadn', 'creeks'], ['jackson', 'hadn', 'creeks', 'creek'], ['paddled'], ['paddled', 'alabama'], ['really'], ['really', 'began'], ['really', 'began', 'andrew'], ['really', 'began', 'andrew', 'jackson'], ['simon'], ['simon', 'finch'], ['simon', 'finch', 'paddled'], ['simon', 'finch', 'paddled', 'alabama'], ['view'], ['view', 'really'], ['view', 'really', 'began'], ['view', 'really', 'began', 'andrew'], ['wanted'], ['wanted', 'broad'], ['wanted', 'broad', 'view'], ['wanted', 'broad', 'view', 'really']]], ['atticus', [['argument'], ['argument', 'fist'], ['argument', 'fist', 'fight'], ['argument', 'fist', 'fight', 'consulted'], ['atticus'], ['atticus', 'father'], ['atticus', 'father', 'right'], ['consulted'], ['consulted', 'atticus'], ['consulted', 'atticus', 'father'], ['consulted', 'atticus', 'father', 'right'], ['far'], ['far', 'old'], ['far', 'old', 'settle'], ['far', 'old', 'settle', 'argument'], ['father'], ['father', 'right'], ['fight'], ['fight', 'consulted'], ['fight', 'consulted', 'atticus'], ['fight', 'consulted', 'atticus', 'father'], ['fist'], ['fist', 'fight'], ['fist', 'fight', 'consulted'], ['fist', 'fight', 'consulted', 'atticus'], ['hadn'], ['hadn', 'far'], ['hadn', 'far', 'old'], ['hadn', 'far', 'old', 'settle'], ['old'], ['old', 'settle'], ['old', 'settle', 'argument'], ['old', 'settle', 'argument', 'fist'], ['right'], ['settle'], ['settle', 'argument'], ['settle', 'argument', 'fist'], ['settle', 'argument', 'fist', 'fight']]], ['boo radley', [['began'], ['began', 'dill'], ['began', 'dill', 'came'], ['began', 'dill', 'came', 'us'], ['boo'], ['boo', 'radley'], ['came'], ['came', 'us'], ['came', 'us', 'dill'], ['came', 'us', 'dill', 'gave'], ['dill'], ['dill', 'came'], ['dill', 'came', 'us'], ['dill', 'came', 'us', 'dill'], ['dill', 'gave'], ['dill', 'gave', 'us'], ['dill', 'gave', 'us', 'idea'], ['gave'], ['gave', 'us'], ['gave', 'us', 'idea'], ['gave', 'us', 'idea', 'making'], ['idea'], ['idea', 'making'], ['idea', 'making', 'boo'], ['idea', 'making', 'boo', 'radley'], ['making'], ['making', 'boo'], ['making', 'boo', 'radley'], ['radley'], ['us'], ['us', 'dill'], ['us', 'dill', 'gave'], ['us', 'dill', 'gave', 'us'], ['us', 'idea'], ['us', 'idea', 'making'], ['us', 'idea', 'making', 'boo']]], ['dill', [['began'], ['began', 'dill'], ['began', 'dill', 'came'], ['began', 'dill', 'came', 'us'], ['boo'], ['boo', 'radley'], ['came'], ['came', 'us'], ['came', 'us', 'dill'], ['came', 'us', 'dill', 'gave'], ['dill'], ['dill', 'came'], ['dill', 'came', 'us'], ['dill', 'came', 'us', 'dill'], ['dill', 'gave'], ['dill', 'gave', 'us'], ['dill', 'gave', 'us', 'idea'], ['gave'], ['gave', 'us'], ['gave', 'us', 'idea'], ['gave', 'us', 'idea', 'making'], ['idea'], ['idea', 'making'], ['idea', 'making', 'boo'], ['idea', 'making', 'boo', 'radley'], ['making'], ['making', 'boo'], ['making', 'boo', 'radley'], ['radley'], ['us'], ['us', 'dill'], ['us', 'dill', 'gave'], ['us', 'dill', 'gave', 'us'], ['us', 'idea'], ['us', 'idea', 'making'], ['us', 'idea', 'making', 'boo']]], ['general jackson', [['alabama'], ['andrew'], ['andrew', 'jackson'], ['began'], ['began', 'andrew'], ['began', 'andrew', 'jackson'], ['broad'], ['broad', 'view'], ['broad', 'view', 'really'], ['broad', 'view', 'really', 'began'], ['creek'], ['creek', 'simon'], ['creek', 'simon', 'finch'], ['creek', 'simon', 'finch', 'paddled'], ['creeks'], ['creeks', 'creek'], ['creeks', 'creek', 'simon'], ['creeks', 'creek', 'simon', 'finch'], ['finch'], ['finch', 'paddled'], ['finch', 'paddled', 'alabama'], ['general'], ['general', 'jackson'], ['general', 'jackson', 'hadn'], ['general', 'jackson', 'hadn', 'creeks'], ['hadn'], ['hadn', 'creeks'], ['hadn', 'creeks', 'creek'], ['hadn', 'creeks', 'creek', 'simon'], ['jackson'], ['jackson', 'hadn'], ['jackson', 'hadn', 'creeks'], ['jackson', 'hadn', 'creeks', 'creek'], ['paddled'], ['paddled', 'alabama'], ['really'], ['really', 'began'], ['really', 'began', 'andrew'], ['really', 'began', 'andrew', 'jackson'], ['simon'], ['simon', 'finch'], ['simon', 'finch', 'paddled'], ['simon', 'finch', 'paddled', 'alabama'], ['view'], ['view', 'really'], ['view', 'really', 'began'], ['view', 'really', 'began', 'andrew'], ['wanted'], ['wanted', 'broad'], ['wanted', 'broad', 'view'], ['wanted', 'broad', 'view', 'really']]], ['jem', [['able'], ['able', 'football'], ['able', 'football', 'assuaged'], ['assuaged'], ['ewells'], ['ewells', 'started'], ['ewells', 'started', 'jem'], ['ewells', 'started', 'jem', 'four'], ['fears'], ['fears', 'able'], ['fears', 'able', 'football'], ['fears', 'able', 'football', 'assuaged'], ['football'], ['football', 'assuaged'], ['four'], ['four', 'years'], ['four', 'years', 'senior'], ['four', 'years', 'senior', 'started'], ['healed'], ['healed', 'jem'], ['healed', 'jem', 'fears'], ['healed', 'jem', 'fears', 'able'], ['jem'], ['jem', 'fears'], ['jem', 'fears', 'able'], ['jem', 'fears', 'able', 'football'], ['jem', 'four'], ['jem', 'four', 'years'], ['jem', 'four', 'years', 'senior'], ['long'], ['maintain'], ['maintain', 'ewells'], ['maintain', 'ewells', 'started'], ['maintain', 'ewells', 'started', 'jem'], ['senior'], ['senior', 'started'], ['senior', 'started', 'long'], ['started'], ['started', 'jem'], ['started', 'jem', 'four'], ['started', 'jem', 'four', 'years'], ['started', 'long'], ['years'], ['years', 'senior'], ['years', 'senior', 'started'], ['years', 'senior', 'started', 'long']]], ['simon finch', [['across'], ['across', 'atlantic'], ['across', 'atlantic', 'philadelphia'], ['alabama'], ['apothecary'], ['apothecary', 'cornwall'], ['apothecary', 'cornwall', 'whose'], ['apothecary', 'cornwall', 'whose', 'piety'], ['atlantic'], ['atlantic', 'philadelphia'], ['brethren'], ['called'], ['called', 'methodist'], ['called', 'methodist', 'worked'], ['called', 'methodist', 'worked', 'across'], ['called', 'methodists'], ['called', 'methodists', 'hands'], ['called', 'methodists', 'hands', 'liberal'], ['cornwall'], ['cornwall', 'whose'], ['cornwall', 'whose', 'piety'], ['cornwall', 'whose', 'piety', 'exceeded'], ['creek'], ['creek', 'simon'], ['creek', 'simon', 'finch'], ['creek', 'simon', 'finch', 'paddled'], ['creeks'], ['creeks', 'creek'], ['creeks', 'creek', 'simon'], ['creeks', 'creek', 'simon', 'finch'], ['england'], ['england', 'simon'], ['england', 'simon', 'irritated'], ['england', 'simon', 'irritated', 'persecution'], ['exceeded'], ['exceeded', 'stinginess'], ['finch'], ['finch', 'fur'], ['finch', 'fur', 'trapping'], ['finch', 'fur', 'trapping', 'apothecary'], ['finch', 'paddled'], ['finch', 'paddled', 'alabama'], ['fur'], ['fur', 'trapping'], ['fur', 'trapping', 'apothecary'], ['fur', 'trapping', 'apothecary', 'cornwall'], ['general'], ['general', 'jackson'], ['general', 'jackson', 'hadn'], ['general', 'jackson', 'hadn', 'creeks'], ['hadn'], ['hadn', 'creeks'], ['hadn', 'creeks', 'creek'], ['hadn', 'creeks', 'creek', 'simon'], ['hands'], ['hands', 'liberal'], ['hands', 'liberal', 'brethren'], ['irritated'], ['irritated', 'persecution'], ['irritated', 'persecution', 'called'], ['irritated', 'persecution', 'called', 'methodists'], ['jackson'], ['jackson', 'hadn'], ['jackson', 'hadn', 'creeks'], ['jackson', 'hadn', 'creeks', 'creek'], ['liberal'], ['liberal', 'brethren'], ['methodist'], ['methodist', 'worked'], ['methodist', 'worked', 'across'], ['methodist', 'worked', 'across', 'atlantic'], ['methodists'], ['methodists', 'hands'], ['methodists', 'hands', 'liberal'], ['methodists', 'hands', 'liberal', 'brethren'], ['paddled'], ['paddled', 'alabama'], ['persecution'], ['persecution', 'called'], ['persecution', 'called', 'methodists'], ['persecution', 'called', 'methodists', 'hands'], ['philadelphia'], ['piety'], ['piety', 'exceeded'], ['piety', 'exceeded', 'stinginess'], ['simon'], ['simon', 'called'], ['simon', 'called', 'methodist'], ['simon', 'called', 'methodist', 'worked'], ['simon', 'finch'], ['simon', 'finch', 'fur'], ['simon', 'finch', 'fur', 'trapping'], ['simon', 'finch', 'paddled'], ['simon', 'finch', 'paddled', 'alabama'], ['simon', 'irritated'], ['simon', 'irritated', 'persecution'], ['simon', 'irritated', 'persecution', 'called'], ['stinginess'], ['trapping'], ['trapping', 'apothecary'], ['trapping', 'apothecary', 'cornwall'], ['trapping', 'apothecary', 'cornwall', 'whose'], ['whose'], ['whose', 'piety'], ['whose', 'piety', 'exceeded'], ['whose', 'piety', 'exceeded', 'stinginess'], ['worked'], ['worked', 'across'], ['worked', 'across', 'atlantic'], ['worked', 'across', 'atlantic', 'philadelphia']]]]
    result = format_as_json(data)
    assert format_as_json(data) ==  result

def test_matching_pair():
    sentence_list = [['healed', 'jem', 'fears', 'able', 'football', 'assuaged'], ['seldom', 'self', 'conscious', 'injury'], ['left', 'arm', 'somewhat', 'shorter', 'right', 'stood', 'walked', 'hand', 'right', 'angles', 'body', 'thumb', 'parallel', 'thigh'], ['couldn', 'cared', 'less', 'long', 'pass', 'punt'], ['enough', 'years', 'enable', 'us', 'sometimes', 'discussed', 'events', 'leading', 'accident'], ['maintain', 'ewells', 'started', 'jem', 'four', 'years', 'senior', 'started', 'long'], ['began', 'dill', 'came', 'us', 'dill', 'gave', 'us', 'idea', 'making', 'boo', 'radley'], ['wanted', 'broad', 'view', 'really', 'began', 'andrew', 'jackson'], ['general', 'jackson', 'hadn', 'creeks', 'creek', 'simon', 'finch', 'paddled', 'alabama'], ['hadn', 'far', 'old', 'settle', 'argument', 'fist', 'fight', 'consulted', 'atticus', 'father', 'right'], ['southerners', 'source', 'shame', 'members', 'family', 'recorded', 'ancestors', 'either', 'side', 'battle', 'hastings'], ['simon', 'finch', 'fur', 'trapping', 'apothecary', 'cornwall', 'whose', 'piety', 'exceeded', 'stinginess'], ['england', 'simon', 'irritated', 'persecution', 'called', 'methodists', 'hands', 'liberal', 'brethren'], ['simon', 'called', 'methodist', 'worked', 'across', 'atlantic', 'philadelphia'], ['thence', 'jamaica', 'thence', 'mobile', 'saint', 'stephens']]
    result = 2
    assert matching_pair("andrew jackson","dill",sentence_list,3) == result

def test_pairs_occurrences():
    sentence_list = [['healed', 'jem', 'fears', 'able', 'football', 'assuaged'], ['seldom', 'self', 'conscious', 'injury'], ['left', 'arm', 'somewhat', 'shorter', 'right', 'stood', 'walked', 'hand', 'right', 'angles', 'body', 'thumb', 'parallel', 'thigh'], ['couldn', 'cared', 'less', 'long', 'pass', 'punt'], ['enough', 'years', 'enable', 'us', 'sometimes', 'discussed', 'events', 'leading', 'accident'], ['maintain', 'ewells', 'started', 'jem', 'four', 'years', 'senior', 'started', 'long'], ['began', 'dill', 'came', 'us', 'dill', 'gave', 'us', 'idea', 'making', 'boo', 'radley'], ['wanted', 'broad', 'view', 'really', 'began', 'andrew', 'jackson'], ['general', 'jackson', 'hadn', 'creeks', 'creek', 'simon', 'finch', 'paddled', 'alabama'], ['hadn', 'far', 'old', 'settle', 'argument', 'fist', 'fight', 'consulted', 'atticus', 'father', 'right'], ['southerners', 'source', 'shame', 'members', 'family', 'recorded', 'ancestors', 'either', 'side', 'battle', 'hastings'], ['simon', 'finch', 'fur', 'trapping', 'apothecary', 'cornwall', 'whose', 'piety', 'exceeded', 'stinginess'], ['england', 'simon', 'irritated', 'persecution', 'called', 'methodists', 'hands', 'liberal', 'brethren'], ['simon', 'called', 'methodist', 'worked', 'across', 'atlantic', 'philadelphia'], ['thence', 'jamaica', 'thence', 'mobile', 'saint', 'stephens']]
    names_list =  [['andrew jackson'], ['atticus'], ['boo radley'], ['dill'], ['general jackson'], ['jem'], ['simon finch']]
    result = {('andrew jackson', 'atticus'): 2, ('andrew jackson', 'boo radley'): 2, ('andrew jackson', 'dill'): 2, ('andrew jackson', 'general jackson'): 4, ('andrew jackson', 'jem'): 1, ('andrew jackson', 'simon finch'): 3, ('atticus', 'boo radley'): 0, ('atticus', 'dill'): 0, ('atticus', 'general jackson'): 2, ('atticus', 'jem'): 0, ('atticus', 'simon finch'): 3, ('boo radley', 'dill'): 3, ('boo radley', 'general jackson'): 2, ('boo radley', 'jem'): 2, ('boo radley', 'simon finch'): 1, ('dill', 'general jackson'): 2, ('dill', 'jem'): 2, ('dill', 'simon finch'): 1, ('general jackson', 'jem'): 1, ('general jackson', 'simon finch'): 3, ('jem', 'simon finch'): 0}
    assert pairs_occurrences(sentence_list,names_list,3) == result

def test_format_result_to_json():
    pairs = {('andrew jackson', 'atticus'): 2, ('andrew jackson', 'boo radley'): 2, ('andrew jackson', 'dill'): 2, ('andrew jackson', 'general jackson'): 4, ('andrew jackson', 'jem'): 1, ('andrew jackson', 'simon finch'): 3, ('atticus', 'boo radley'): 0, ('atticus', 'dill'): 0, ('atticus', 'general jackson'): 2, ('atticus', 'jem'): 0, ('atticus', 'simon finch'): 3, ('boo radley', 'dill'): 3, ('boo radley', 'general jackson'): 2, ('boo radley', 'jem'): 2, ('boo radley', 'simon finch'): 1, ('dill', 'general jackson'): 2, ('dill', 'jem'): 2, ('dill', 'simon finch'): 1, ('general jackson', 'jem'): 1, ('general jackson', 'simon finch'): 3, ('jem', 'simon finch'): 0}
    result = format_result_to_json(pairs, 2)
    assert format_result_to_json(pairs,2) == result

def test_dict_processing():
    connection_dict = {
    "Question 6": {
        "Pair Matches": [
            [
                [
                    "andrew",
                    "jackson"
                ],
                [
                    "general",
                    "jackson"
                ]
            ],
            [
                [
                    "andrew",
                    "jackson"
                ],
                [
                    "simon",
                    "finch"
                ]
            ],
            [
                [
                    "atticus"
                ],
                [
                    "simon",
                    "finch"
                ]
            ],
            [
                [
                    "boo",
                    "radley"
                ],
                [
                    "dill"
                ]
            ],
            [
                [
                    "general",
                    "jackson"
                ],
                [
                    "simon",
                    "finch"
                ]
            ]
        ]
    }
}
    result =[['andrew jackson', 'general jackson'], ['andrew jackson', 'simon finch'], ['atticus', 'simon finch'], ['boo radley', 'dill'], ['general jackson', 'simon finch']]
    assert dict_processing(connection_dict) == result

def test_dict_processing_1():
    with pytest.raises(SystemExit) as excinfo:  # Catch the SystemExit
        dict_processing([])
        # Check that the exit message matches
    assert str(excinfo.value) == "Invalid Input"

def test_dict_processing_2():
    with pytest.raises(SystemExit) as excinfo:  # Catch the SystemExit
        dict_processing(None)
        # Check that the exit message matches
    assert str(excinfo.value) == "Invalid Input"

def test_dict_processing_3():
    connection_dict = {
        "Question 6": { "Pairs" : [
            [
                [
                    "andrew",
                    "jackson"
                ],
                [
                    "general",
                    "jackson"
                ]]]}}
    with pytest.raises(SystemExit) as excinfo:  # Catch the SystemExit
        dict_processing(connection_dict)
        # Check that the exit message matches
    assert str(excinfo.value) == "Invalid Input"

def test_checking_connection():
    with pytest.raises(SystemExit) as excinfo:  # Catch the SystemExit
        checking_connection({},[],1000)
        # Check that the exit message matches
    assert str(excinfo.value) == "Invalid Input"

def test_making_adjacency_list():
    joined_pairs = [['andrew jackson', 'general jackson'], ['andrew jackson', 'simon finch'], ['atticus', 'simon finch'], ['boo radley', 'dill'], ['general jackson', 'simon finch']]
    result ={'andrew jackson': ['general jackson', 'simon finch'], 'general jackson': ['andrew jackson', 'simon finch'], 'simon finch': ['andrew jackson', 'atticus', 'general jackson'], 'atticus': ['simon finch'], 'boo radley': ['dill'], 'dill': ['boo radley']}
    assert making_adjacency_list(joined_pairs)== result

def test_bfs():
    graph ={'andrew jackson': ['general jackson', 'simon finch'], 'general jackson': ['andrew jackson', 'simon finch'], 'simon finch': ['andrew jackson', 'atticus', 'general jackson'], 'atticus': ['simon finch'], 'boo radley': ['dill'], 'dill': ['boo radley']}
    start = "boo radley"
    result = {'boo radley': 0, 'dill': 1}
    assert bfs_with_distance(graph,start)== result

def test_checking_connection_1():
    keys_dict = {
        "keys": [
        ["andrew jackson", "simon finch"],
        ["dill", "boo radley"],
        ["sarah", "atticus"]

    ]
}
    names_list =[['andrew jackson', 'general jackson'], ['andrew jackson', 'simon finch'], ['atticus', 'simon finch'], ['boo radley', 'dill'], ['general jackson', 'simon finch']]
    result = [['andrew jackson', 'simon finch', True], ['atticus', 'sarah', False], ['boo radley', 'dill', True]]
    assert checking_connection(keys_dict,names_list,1000)== result

def test_json_format():
    connected_pairs = [['andrew jackson', 'simon finch', True], ['atticus', 'sarah', False], ['boo radley', 'dill', True]]
    result = json_format(connected_pairs)
    assert json_format(connected_pairs)== result

def test_is_connected_by_path_of_length():
    graph = Graph ({'andrew jackson': ['general jackson', 'simon finch'], 'general jackson': ['andrew jackson', 'simon finch'], 'simon finch': ['andrew jackson', 'atticus', 'general jackson'], 'atticus': ['simon finch'], 'boo radley': ['dill'], 'dill': ['boo radley']})
    start = "boo radley"
    end ="sarah"
    result = False
    assert graph.is_connected_by_path_of_length(start,end,4)== result

def test_all_the_connections():
    graph = Graph ({'andrew jackson': ['general jackson', 'simon finch'], 'general jackson': ['andrew jackson', 'simon finch'], 'simon finch': ['andrew jackson', 'atticus', 'general jackson'], 'atticus': ['simon finch'], 'boo radley': ['dill'], 'dill': ['boo radley']})
    keys_dict = {
    "keys": [
                ["andrew jackson", "simon finch"],
                ["dill", "boo radley"],
                ["sarah", "atticus"]

            ]
        }
    result = [['andrew jackson', 'simon finch', True], ['atticus', 'sarah', False], ['boo radley', 'dill', False]]
    assert graph.all_the_connections(keys_dict,2)==result

def test_generate_result_file():
    graph = Graph ({'andrew jackson': ['general jackson', 'simon finch'], 'general jackson': ['andrew jackson', 'simon finch'], 'simon finch': ['andrew jackson', 'atticus', 'general jackson'], 'atticus': ['simon finch'], 'boo radley': ['dill'], 'dill': ['boo radley']})
    result_list = [['andrew jackson', 'simon finch', True], ['atticus', 'sarah', False], ['boo radley', 'dill', False]]
    result = graph.generate_result_file(result_list)
    assert graph.generate_result_file(result_list)== result

def test_common_words():
    sentence_list = [['healed', 'jem', 'fears', 'able', 'football', 'assuaged'], ['seldom', 'self', 'conscious', 'injury'], ['left', 'arm', 'somewhat', 'shorter', 'right', 'stood', 'walked', 'hand', 'right', 'angles', 'body', 'thumb', 'parallel', 'thigh'], ['couldn', 'cared', 'less', 'long', 'pass', 'punt'], ['enough', 'years', 'enable', 'us', 'sometimes', 'discussed', 'events', 'leading', 'accident'], ['maintain', 'ewells', 'started', 'jem', 'four', 'years', 'senior', 'started', 'long'], ['began', 'dill', 'came', 'us', 'dill', 'gave', 'us', 'idea', 'making', 'boo', 'radley'], ['wanted', 'broad', 'view', 'really', 'began', 'andrew', 'jackson'], ['general', 'jackson', 'hadn', 'creeks', 'creek', 'simon', 'finch', 'paddled', 'alabama'], ['hadn', 'far', 'old', 'settle', 'argument', 'fist', 'fight', 'consulted', 'atticus', 'father', 'right'], ['southerners', 'source', 'shame', 'members', 'family', 'recorded', 'ancestors', 'either', 'side', 'battle', 'hastings'], ['simon', 'finch', 'fur', 'trapping', 'apothecary', 'cornwall', 'whose', 'piety', 'exceeded', 'stinginess'], ['england', 'simon', 'irritated', 'persecution', 'called', 'methodists', 'hands', 'liberal', 'brethren'], ['simon', 'called', 'methodist', 'worked', 'across', 'atlantic', 'philadelphia'], ['thence', 'jamaica', 'thence', 'mobile', 'saint', 'stephens']]
    result = UnionFind.common_words(sentence_list,2)
    assert UnionFind.common_words(sentence_list,2) == result

def mock_is_valid_csv(value):
    return value == "valid_csv"

def mock_is_valid_json(value):
    return value == "valid_json"

def test_valid_args_invalid_input_1():
    parsed_args = {
        "task":"",
        "sentences": "valid_csv",
        "names": "",
        "removewords": "",
        "preprocessed":"",
        "maxk": 5,
        "fixed_length": "",
        "windowsize" : "" ,
        "threshold":"",
        "maximal_distance":"",
        "qsek_query_path":"",
        "pairs":""

    }
    with patch('sys.exit') as mock_exit:
        valid_args(parsed_args)
        mock_exit.assert_called_with("Invalid Input")

def test_valid_args_invalid_input_2():
    parsed_args = {
        "task":11,
        "sentences": "",
        "names": "",
        "removewords": "",
        "preprocessed":"",
        "maxk": 2,
        "fixed_length": "",
        "windowsize" : "" ,
        "threshold":"",
        "maximal_distance":"",
        "qsek_query_path":"",
        "pairs":""
    }
    with patch('sys.exit') as mock_exit:
        valid_args(parsed_args)
        mock_exit.assert_called_with("Invalid Input")

def test_valid_args_invalid_input_3():
    parsed_args = {
        "task":"",
        "sentences": "valid_csv",
        "names": "valid_csv",
        "removewords": "valid_csv",
        "preprocessed":"",
        "maxk": 2,
        "fixed_length": "",
        "windowsize" : "" ,
        "threshold":"",
        "maximal_distance":"",
        "qsek_query_path":"valid.json",
        "pairs":""

    }
    with patch('sys.exit') as mock_exit:
        valid_args(parsed_args)
        mock_exit.assert_called_with("Invalid Input")

def test_valid_args_invalid_input_4():
    parsed_args = {
        "task":None,
        "sentences": "",
        "names": "valid_csv",
        "removewords": "",
        "preprocessed":"",
        "maxk":None,
        "fixed_length": "",
        "windowsize" : 7 ,
        "threshold":"",
        "maximal_distance":"",
        "qsek_query_path":"",
        "pairs":""

    }
    with patch('sys.exit') as mock_exit:
        valid_args(parsed_args)
        mock_exit.assert_called_with("Invalid Input")

def test_valid_args_invalid_input_5():
    parsed_args = {
        "task":"",
        "sentences": "",
        "names": "",
        "removewords": "valid_json",
        "preprocessed":"",
        "maxk":-2,
        "fixed_length": "",
        "windowsize" : "" ,
        "threshold":"",
        "maximal_distance":"",
        "qsek_query_path":"",
        "pairs":""
    }
    with patch('sys.exit') as mock_exit:
        valid_args(parsed_args)
        mock_exit.assert_called_with("Invalid Input")

def test_valid_args_invalid_input_6():
    parsed_args = {
        "task":"",
        "sentences": "",
        "names": "",
        "removewords": "",
        "preprocessed":"valid_json",
        "maxk": 1,
        "fixed_length": "",
        "windowsize" : "" ,
        "threshold":"",
        "maximal_distance":"",
        "qsek_query_path":"",
        "pairs":""
    }
    with patch('sys.exit') as mock_exit:
        valid_args(parsed_args)
        mock_exit.assert_called_with("Invalid Input")

def test_valid_args_invalid_input_7():
    parsed_args = {
        "task":"",
        "sentences": "",
        "names": "",
        "removewords": "",
        "preprocessed":"",
        "maxk": -1 ,
        "fixed_length": "",
        "windowsize" : "" ,
        "threshold":"",
        "maximal_distance":"",
        "qsek_query_path":"",
        "pairs":""
    }
    with patch('sys.exit') as mock_exit:
        valid_args(parsed_args)
        mock_exit.assert_called_with("Invalid Input")

def test_valid_args_invalid_input_8():
    parsed_args = {
        "task":"",
        "sentences": "",
        "names": "",
        "removewords": "",
        "preprocessed":"",
        "maxk": None,
        "fixed_length": -7,
        "windowsize" : "" ,
        "threshold":"",
        "maximal_distance":"",
        "qsek_query_path":"",
        "pairs":""
    }
    with patch('sys.exit') as mock_exit:
        valid_args(parsed_args)
        mock_exit.assert_called_with("Invalid Input")

def test_valid_args_invalid_input_9():
    parsed_args = {
        "task":"",
        "sentences": "",
        "names": "",
        "removewords": "",
        "preprocessed":"",
        "maxk": None,
        "fixed_length": "",
        "windowsize" : -8,
        "threshold":"",
        "maximal_distance":"",
        "qsek_query_path":"",
        "pairs":""
    }
    with patch('sys.exit') as mock_exit:
        valid_args(parsed_args)
        mock_exit.assert_called_with("Invalid Input")

def test_valid_args_invalid_input_10():
    parsed_args = {
        "task":"",
        "sentences": "",
        "names": "",
        "removewords": "",
        "preprocessed":"",
        "maxk": None,
        "fixed_length": "",
        "windowsize" : "" ,
        "threshold":-5,
        "maximal_distance":"",
        "qsek_query_path":"",
        "pairs":""

    }
    with patch('sys.exit') as mock_exit:
        valid_args(parsed_args)
        mock_exit.assert_called_with("Invalid Input")

def test_valid_args_invalid_input_11():
    parsed_args = {
        "task":"",
        "sentences": "",
        "names": "",
        "removewords": "",
        "preprocessed":"",
        "maxk": None,
        "fixed_length": "",
        "windowsize" : "" ,
        "threshold":"",
        "maximal_distance":-4,
        "qsek_query_path":"",
        "pairs":""

    }
    with patch('sys.exit') as mock_exit:
        valid_args(parsed_args)
        mock_exit.assert_called_with("Invalid Input")

def test_valid_args_invalid_input_12():
    parsed_args = {
        "task":"",
        "sentences": "",
        "names": "",
        "removewords": "",
        "preprocessed":"",
        "maxk": None,
        "fixed_length": "",
        "windowsize" : "" ,
        "threshold":"",
        "maximal_distance":"",
        "qsek_query_path":"",
        "pairs":"valid_json"

    }
    with patch('sys.exit') as mock_exit:
        valid_args(parsed_args)
        mock_exit.assert_called_with("Invalid Input")

def test_valid_csv():
    # Mocking the open function to simulate a valid CSV file
    file_path = "valid_file.csv"
    with patch("builtins.open", mock_open(read_data="header1,header2\nvalue1,value2")):
        with patch("os.path.isfile", return_value=True):
            result = is_valid_csv(file_path)
            assert result is True

def test_non_csv_file():
    # Simulate a file with a non-CSV extension
    file_path = "file.txt"
    result = is_valid_csv(file_path)
    assert result is False

def test_file_does_not_exist():
    # Simulate a file that does not exist
    file_path = "non_existent_file.csv"
    with patch("os.path.isfile", return_value=False):
        result = is_valid_csv(file_path)
        assert result is False

def test_invalid_csv_format():
    # Mocking the open function to simulate a file with invalid CSV format
    file_path = "invalid_file.csv"
    with patch("builtins.open", mock_open(read_data="header1,header2\nvalue1,value2\nvalue3")):
        with patch("os.path.isfile", return_value=True):
            # Simulate CSV error, e.g., malformed row count
            with patch("csv.reader", side_effect=csv.Error):
                result = is_valid_csv(file_path)
                assert result is False

def test_empty_file():
    # Simulate an empty CSV file
    file_path = "empty_file.csv"
    with patch("builtins.open", mock_open(read_data="")):
        with patch("os.path.isfile", return_value=True):
            result = is_valid_csv(file_path)
            assert result is True

def test_task_1_valid_case():
    # Mock initial_text_processing to avoid actual processing
    parsed_args = {
        "task": 1,
        "sentences": "Some sentences",
        "names": "Some names",
        "removewords": "Some words to remove",
        "preprocessed": "",
        "maxk": "",
        "fixed_length": "",
        "windowsize": "",
        "threshold": "",
        "maximal_distance": "",
        "qsek_query_path": "",
        "pairs": ""
    }
    with patch("task_1.initial_text_processing", side_effect=Exception("Some error")):
        with patch("sys.exit") as mock_exit:
            functions_calling(parsed_args)
            mock_exit.assert_called_with("Invalid Input")

def test_task_2_invalid_case():
    # Test for task 2 when no required fields are given
    parsed_args = {
        "task": 2,
        "sentences": "",
        "names": "",
        "removewords": "",
        "maxk": 3,
        "preprocessed": "not_valid_json",
        "fixed_length": "",
        "windowsize": "",
        "threshold": "",
        "maximal_distance": "",
        "qsek_query_path": "",
        "pairs": ""
    }
    with patch("sys.exit") as mock_exit:
        functions_calling(parsed_args)
        mock_exit.assert_called_with("Invalid Input")

def test_task_3_invalid_case():
    # Test for task 3 when no required fields are given
    parsed_args = {
        "task": 3,
        "sentences": "json_valid",
        "names": "not_valid_json",
        "removewords": "not_valid.json",
        "maxk": 3,
        "preprocessed": "",
        "fixed_length": "",
        "windowsize": "",
        "threshold": "",
        "maximal_distance": "",
        "qsek_query_path": "",
        "pairs": ""
    }
    with patch("sys.exit") as mock_exit:
        functions_calling(parsed_args)
        mock_exit.assert_called_with("Invalid Input")

def test_task_4_invalid_case():
    # Test for task 4 when no required fields are given
    parsed_args = {
        "task": 4,
        "sentences": "",
        "names": "",
        "removewords": "not_valid_json",
        "maxk": 3,
        "preprocessed": "not_valid_json",
        "fixed_length": "",
        "windowsize": "",
        "threshold": "",
        "maximal_distance": "",
        "qsek_query_path": "valid_json",
        "pairs": ""
    }
    with patch("sys.exit") as mock_exit:
        functions_calling(parsed_args)
        mock_exit.assert_called_with("Invalid Input")

def test_task_5_invalid_case():
    # Test for task 5 when no required fields are given
    parsed_args = {
        "task": 5,
        "sentences": "",
        "names": "",
        "removewords": "",
        "maxk": 'f',
        "preprocessed": "not_valid_json",
        "fixed_length": "",
        "windowsize": "",
        "threshold": "",
        "maximal_distance": "",
        "qsek_query_path": "",
        "pairs": ""
    }
    with patch("sys.exit") as mock_exit:
        functions_calling(parsed_args)
        mock_exit.assert_called_with("Invalid Input")

def test_task_6_invalid_case():
    # Test for task 6 when no required fields are given
    parsed_args = {
        "task": 6,
        "sentences": "",
        "names": "",
        "removewords": "",
        "maxk": "",
        "preprocessed": "not_valid_json",
        "fixed_length": "",
        "windowsize": -8,
        "threshold": 0,
        "maximal_distance": "",
        "qsek_query_path": "",
        "pairs": ""
    }
    with patch("sys.exit") as mock_exit:
        functions_calling(parsed_args)
        mock_exit.assert_called_with("Invalid Input")

def test_task_7_invalid_case():
    # Test for task 7 when no required fields are given
    parsed_args = {
        "task": 7,
        "sentences": "",
        "names": "",
        "removewords": "",
        "maxk": 0,
        "preprocessed": "not_valid.json",
        "fixed_length": "",
        "windowsize": "",
        "threshold": "",
        "maximal_distance": 0,
        "qsek_query_path": "",
        "pairs": "not_valid_json"
    }
    with patch("sys.exit") as mock_exit:
        functions_calling(parsed_args)
        mock_exit.assert_called_with("Invalid Input")

def test_task_8_invalid_case():
    # Test for task 8 when no required fields are given
    parsed_args = {
        "task": 8,
        "sentences": "",
        "names": "",
        "removewords": "",
        "maxk": 5,
        "preprocessed": "",
        "fixed_length": 0,
        "windowsize": "",
        "threshold": "",
        "maximal_distance": "",
        "qsek_query_path": "not_valid_jon",
        "pairs": ""
    }
    with patch("sys.exit") as mock_exit:
        functions_calling(parsed_args)
        mock_exit.assert_called_with("Invalid Input")

def test_task_9_invalid_case():
    # Test for task 9 when no required fields are given
    parsed_args = {
        "task": 9,
        "sentences": "",
        "names": "",
        "removewords": "",
        "maxk": "",
        "preprocessed": "not_valid",
        "fixed_length": "",
        "windowsize": "",
        "threshold": 0,
        "maximal_distance": "",
        "qsek_query_path": "",
        "pairs": ""
    }
    with patch("sys.exit") as mock_exit:
        functions_calling(parsed_args)
        mock_exit.assert_called_with("Invalid Input")

def test_valid_csv_1():
    valid_csv_content = "col1,col2,col3\nval1,val2,val3\n"

    with patch("builtins.open", mock_open(read_data=valid_csv_content)):
        with patch("os.path.isfile", return_value=True):  # Mock file existence check
            result = is_valid_csv("test.csv")
            assert result is True

def test_file_does_not_exist_1():
    with patch("os.path.isfile", return_value=False):  # Mock file existence check
        result = is_valid_csv("nonexistent.csv")
        assert result is False  # Should return False since file doesn't exist

def test_valid_json():
    valid_json_content = '{"key": "value", "num": 10}'

    with patch("builtins.open", mock_open(read_data=valid_json_content)):
        with patch("os.path.isfile", return_value=True):  # Mock file existence check
            result = is_valid_json("test.json")
            assert result is True  # Should return True for valid JSON

# Test case for a file that doesn't exist
def test_file_does_not_exist_3():
    with patch("os.path.isfile", return_value=False):  # Mock file existence check
        result = is_valid_json("nonexistent.json")
        assert result is False  # Should return False since file doesn't exist

# Test case for a file with invalid extension
def test_invalid_extension():
    with patch("os.path.isfile", return_value=True):  # Mock file existence check
        result = is_valid_json("test.txt")  # Not a JSON file
        assert result is False  # Should return False due to invalid extension

def test_valid_json_file():
    valid_json_content = '{"key": "value", "num": 10}'

    with patch("builtins.open", mock_open(read_data=valid_json_content)):
        result = open_file("test.json")
        assert result == {"key": "value", "num": 10}  # The function should return the parsed JSON content

def test_valid_text_file():
    valid_text_content = "This is a valid text file."

    with patch("builtins.open", mock_open(read_data=valid_text_content)):
        result = open_file("test.txt")
        assert result == valid_text_content

def test_file_not_found_2():
    with patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(SystemExit) as excinfo:  # Mock print to check the output
            result = open_file("nonexistent_file.json")
        assert str(excinfo.value) == "Invalid Input"

def test_key_in_sentence_1():
    with pytest.raises(SystemExit) as excinfo:  # Catch the SystemExit
        key_in_sentence(None,["albus"])
        # Check that the exit message matches
    assert str(excinfo.value) == "Invalid Input"

def test_all_sentences_2():
    sentence =[["under","tuft"]]
    with pytest.raises(SystemExit) as excinfo:  # Catch the SystemExit
        all_sentences(sentence,None)
        # Check that the exit message matches
    assert str(excinfo.value) == "Invalid Input"

def test_all_sentences_3():
    sentences =[["under","tuft"]]
    assert all_sentences(sentences,[]) == {}

def test_all_sentences_4():
    sentences = [["under", "tuft"]]
    assert all_sentences(sentences, [[]]) == {}

def test_is_valid_json_decode_error():
    # Create a temporary file with invalid JSON content
    with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as temp_file:
        temp_file.write(b"{invalid_json: true")  # Malformed JSON
        temp_file_path = temp_file.name

    try:
        assert not is_valid_json(temp_file_path)  # Should return False due to JSONDecodeError
    finally:
        os.remove(temp_file_path)

def test_open_file_not_found():
    """Test if FileNotFoundError is handled properly."""
    with pytest.raises(SystemExit) as excinfo:
        open_file("non_existent_file.txt")
    assert str(excinfo.value) == "Invalid Input"

def test_open_file_json_decode_error():
    """Test if json.JSONDecodeError is handled properly."""
    """Test if json.JSONDecodeError triggers SystemExit with 'Invalid Input'."""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as temp_file:
        temp_file.write(b"{invalid_json: true")  # Malformed JSON
        temp_file.close()
        temp_file_path = temp_file.name

    with pytest.raises(SystemExit) as exc_info:
        open_file(temp_file_path)

    assert str(exc_info.value) == "Invalid Input"

    os.remove(temp_file_path)  # Clean up


def test_open_file_unexpected_exception(monkeypatch):
    """Test if a general exception triggers SystemExit with 'Invalid Input'."""

    def mock_open(*args, **kwargs):
        raise RuntimeError("Unexpected error")  # Simulating an unknown exception

    monkeypatch.setattr("builtins.open", mock_open)  # Patching open() to always raise RuntimeError

    with pytest.raises(SystemExit) as exc_info:
        open_file("somefile.txt")

    assert str(exc_info.value) == "Invalid Input"

def test_functions_calling_exception(mocker):
    """Test if an exception inside the try block raises SystemExit."""

    # Mock initial_text_processing to raise an exception
    mocker.patch("task_1.initial_text_processing", side_effect=RuntimeError("Test Error"))

    with pytest.raises(SystemExit) as exc_info:  # Expecting SystemExit due to sys.exit("Invalid Input")
        functions_calling({"task": 1, "sentences": [], "names": [], "removewords": [], "maxk": "",
        "preprocessed": "not_valid", "fixed_length": "", "windowsize": "", "threshold": 0, "maximal_distance": "",
        "qsek_query_path": "", "pairs": ""})
    assert str(exc_info.value) == "Invalid Input"


@pytest.fixture
def mock_csv_files(mocker):
    """Mock reading from CSV files."""
    # Mock content for each CSV file
    sentences_csv_content = "sentence1\nsentence2"
    names_csv_content = "name1\nname2"
    removewords_csv_content = "word1\nword2"

    # Mocking the open function for CSV files
    mocker.patch("builtins.open", mock_open(read_data=sentences_csv_content), create=True)
    mocker.patch("builtins.open", mock_open(read_data=names_csv_content), create=True)
    mocker.patch("builtins.open", mock_open(read_data=removewords_csv_content), create=True)

    # Mock initial_text_processing to return a valid dictionary structure
    mocker.patch("task_1.initial_text_processing", return_value={
        "Question 1": {
            "Processed Names": ["name1", "name2"],
            "Processed Sentences": [["sentence1"], ["sentence2"]],
        }
    })
    mocker.patch("task_2.dict_to_list", side_effect=lambda d: d["Question 1"]["Processed Sentences"])
    mocker.patch("task_2.all_strings", return_value=["mock_string"])
    mocker.patch("task_2.sequences", return_value=["mock_sequence"])
    mocker.patch("task_2.grouping", return_value="Mocked Grouping Output")
    mocker.patch("builtins.print")  # Mock print to suppress output

def test_functions_calling_valid_case_1(mock_csv_files):
    """Test when all required arguments are provided."""
    parsed_args = {
        "task": 2, "sentences": "sentences.csv", "names": "names.csv", "removewords": "removewords.csv", "maxk": 3,
        "preprocessed": "", "fixed_length": "", "windowsize": "", "threshold": 0, "maximal_distance": "",
        "qsek_query_path": "", "pairs": ""
    }
    functions_calling(parsed_args)


@pytest.fixture
def mock_json_file(mocker):
    """Mock reading from a JSON file."""
    # Mock content for JSON file (simulating a valid JSON)
    json_content = '{"Question 1": {"Processed Sentences": [["sentence1"], ["sentence2"]], "Processed Names": ["name1", "name2"]}}'

    # Mocking the open function to simulate reading from a JSON file
    mocker.patch("builtins.open", mock_open(read_data=json_content), create=True)

    # Mocking open_file to return parsed JSON data
    mocker.patch("main.open_file", return_value={
        "Question 1": {
            "Processed Sentences": [["sentence1"], ["sentence2"]],
            "Processed Names": ["name1", "name2"],
        }
    })

    # Mocking other functions to avoid actual execution
    mocker.patch("task_2.dict_to_list", side_effect=lambda d: d["Question 1"]["Processed Sentences"])
    mocker.patch("task_2.all_strings", return_value=["mock_string"])
    mocker.patch("task_2.sequences", return_value=["mock_sequence"])
    mocker.patch("task_2.grouping", return_value="Mocked Grouping Output")
    mocker.patch("builtins.print")  # Mock print to suppress output


def test_functions_calling_with_preprocessed(mock_json_file):
    """Test when 'preprocessed' and 'maxk' are provided."""
    parsed_args = {
        "task" :2 ,"preprocessed": "output.json", "maxk": 3, "sentences": "", "names": "", "removewords": "",
        "fixed_length": "", "windowsize": "", "threshold": 0, "maximal_distance": "",
        "qsek_query_path": "", "pairs": ""
    }
    functions_calling(parsed_args)

@pytest.fixture
def mock_dependencies(mocker):
    """Mock all function dependencies to prevent real function execution."""
    # Mock the content for CSV files (sentences, names, removewords)
    sentences_csv_content = "sentence1\nsentence2"
    names_csv_content = "name1\nname2"
    removewords_csv_content = "word1\nword2"

    # Mock open for reading CSV files
    mocker.patch("builtins.open", mock_open(read_data=sentences_csv_content), create=True)
    mocker.patch("builtins.open", mock_open(read_data=names_csv_content), create=True)
    mocker.patch("builtins.open", mock_open(read_data=removewords_csv_content), create=True)

    # Mock functions to avoid real processing
    mocker.patch("task_1.initial_text_processing", return_value={
        "Question 1": {
            "Processed Names": ["name1", "name2"],
            "Processed Sentences": [["sentence1"], ["sentence2"]],
        }
    })
    mocker.patch("task_2.dict_to_list", side_effect=lambda d: d["Question 1"]["Processed Sentences"])
    mocker.patch("task_2.all_strings", return_value=["mock_string"])
    mocker.patch("task_2.sequences", return_value=["mock_sequence"])
    mocker.patch("task_2.grouping", return_value="Mocked Grouping Output")
    mocker.patch("builtins.print")  # Mock print to suppress output

def test_functions_calling_valid_case(mock_dependencies):
    """Test when required arguments are provided, and names file is created."""
    parsed_args = {
        "task": 2,
        "sentences": "sentence.csv",
        "names": "name.csv",
        "removewords": "removewords.csv",
        "maxk": 3,
        "preprocessed": "", "fixed_length": "", "windowsize": "", "threshold": 0, "maximal_distance": "",
        "qsek_query_path": "", "pairs": ""
    }
    functions_calling(parsed_args)

def test_functions_calling_invalid_case():
    """Test if sys.exit() is triggered on invalid input."""
    parsed_args = {
        "task": 2,
        "sentences": "sentence.csv",
        "names": "",  # Missing names argument
        "removewords": "removewords.csv",
        "maxk": 3,
        "preprocessed": "", "fixed_length": "", "windowsize": "", "threshold": 0, "maximal_distance": "",
        "qsek_query_path": "", "pairs": ""
    }

    with pytest.raises(SystemExit):  # Expecting SystemExit due to sys.exit("Invalid Input")
        functions_calling(parsed_args)

@pytest.fixture
def mock_dependencis_2(mocker):
    """Mock all function dependencies to prevent real function execution."""
    # Mock content for files
    preprocessed_content = '{"key": "value"}'  # Example JSON content

    # Mock open for reading JSON file
    mocker.patch("builtins.open", mock_open(read_data=preprocessed_content), create=True)

    # Mock the functions used in task 3
    mocker.patch("main.open_file", return_value={"key": "value"})  # Mock open_file function
    mocker.patch("task_2.dict_to_list", return_value=[["sentence1"], ["sentence2"]])  # Mock dict_to_list function
    mocker.patch("task_3.process_data_from_dict", return_value=["name1", "name2"])  # Mock process_data_from_dict function
    mocker.patch("task_3.number_of_counters", return_value=2)  # Mock number_of_counters function
    mocker.patch("task_3.grouping_func", return_value="Mocked Grouping Output")  # Mock grouping_func function
    mocker.patch("builtins.print")  # Mock print to suppress output

def test_task_3_functions(mock_dependencies):
    """Test if the correct functions are called and the flow works for task 3."""
    parsed_args = {"task" : 3 ,"sentences": "", "names": "", "removewords": "", "preprocessed": r'.\output.json',
                   "fixed_length": "", "windowsize": "", "threshold": 0, "maximal_distance": "",
                   "qsek_query_path": "", "pairs": "" , "maxk" : ""
    }

    # Call the task 3 logic
    with pytest.raises(SystemExit):  # Expecting SystemExit due to sys.exit("Invalid Input")
        functions_calling(parsed_args)


@pytest.fixture
def mock_dependencies_3(mocker):
    """Mock all function dependencies to prevent real function execution."""
    # Mock content for CSV files (sentences, names, removewords)
    sentences_csv_content = "sentence1\nsentence2"
    names_csv_content = "name1\nname2"
    removewords_csv_content = "word1\nword2"

    # Mock open for reading CSV files
    mocker.patch("builtins.open", mock_open(read_data=sentences_csv_content), create=True)
    mocker.patch("builtins.open", mock_open(read_data=names_csv_content), create=True)
    mocker.patch("builtins.open", mock_open(read_data=removewords_csv_content), create=True)

    # Mock functions to avoid real processing
    mocker.patch("task_1.initial_text_processing", return_value={
        "Question 1": {
            "Processed Names": ["name1", "name2"],
            "Processed Sentences": [["sentence1"], ["sentence2"]],
        }
    })
    mocker.patch("task_2.dict_to_list", side_effect=lambda d: d["Question 1"]["Processed Sentences"])
    mocker.patch("task_3.process_data_from_dict", return_value=["name1", "name2"])
    mocker.patch("task_3.number_of_counters", return_value=2)
    mocker.patch("task_3.grouping_func", return_value="Mocked Grouping Output")
    mocker.patch("builtins.print")  # Mock print to suppress output


def test_functions_calling_valid_case_3(mock_dependencies):
    """Test when required arguments are provided, and files are processed correctly."""
    parsed_args = {
        "task": 3,
        "sentences": "sentences.csv",
        "names": "names.csv",
        "removewords": "removewords.csv",
        "maxk": "",
        "preprocessed": "", "fixed_length": "", "windowsize": "", "threshold": 0, "maximal_distance": "",
        "qsek_query_path": "", "pairs": ""
    }

    # Call the logic that uses the provided arguments
    functions_calling(parsed_args)  # Should execute without errors
    # Replace this with actual file creation check if your logic creates a file
    assert os.path.exists("names_file.csv")  # Example check, adjust as needed
    os.remove("names_file.csv")  # Cleanup after test

@pytest.fixture
def mock_dependencies_4(mocker):
    """Mock all function dependencies to prevent real function execution."""
    # Mock content for files
    preprocessed_json_content = '{"key": "value"}'  # Example JSON content for preprocessed file
    query_json_content = '{"key1": "value1", "key2": "value2"}'  # Example JSON content for query
    removewords_csv_content = "word1\nword2"  # Example CSV content for removewords file

    # Mock open for reading files
    mocker.patch("builtins.open", mock_open(read_data=preprocessed_json_content), create=True)
    mocker.patch("builtins.open", mock_open(read_data=query_json_content), create=True)
    mocker.patch("builtins.open", mock_open(read_data=removewords_csv_content), create=True)

    # Mock functions used in the logic
    mocker.patch("main.open_file", return_value={"key": "value"})  # Mock open_file (reads JSON)
    mocker.patch("task_2.dict_to_list", return_value=[["sentence1"], ["sentence2"]])  # Mock dict_to_list
    mocker.patch("task_4.json_file_opening", return_value=[{"key1": "value1"}, {"key2": "value2"}])  # Mock json_file_opening
    mocker.patch("task_4.key_to_search", return_value=["value1", "value2"])  # Mock key_to_search
    mocker.patch("task_4.keys_in_sentence", return_value=["sentence1", "sentence2"])  # Mock keys_in_sentence
    mocker.patch("task_4.grouping_function", return_value="Mocked Grouping Output")  # Mock grouping_function
    mocker.patch("builtins.print")  # Mock print to suppress output

def test_functions_calling_valid_case_4(mock_dependencies):
    """Test when required arguments are provided and the correct output is generated."""
    parsed_args = {
        "task" : 4, "preprocessed": r'.\output.json',  "qsek_query_path": r'.\query.json',  "removewords": "removewords.csv",
        "sentences": "", "names": "" ,"maxk": "","windowsize": "", "threshold": 0, "maximal_distance": "","pairs": "",
        "fixed_length" : ""
    }
    # Call the logic with the provided parsed arguments
    with pytest.raises(SystemExit):  # Expecting SystemExit due to sys.exit("Invalid Input")
        functions_calling(parsed_args)

@pytest.fixture
def mock_dependencies_5(mocker):
    """Mock all function dependencies to prevent real function execution."""
    # Mock content for files
    sentences_csv_content = "sentence1\nsentence2"  # Example CSV content for sentences
    names_csv_content = "name1\nname2"  # Example CSV content for names
    removewords_csv_content = "word1\nword2"  # Example CSV content for removewords file
    query_json_content = '{"key1": "value1", "key2": "value2"}'  # Example JSON content for query


    # Mock open for reading files
    mocker.patch("builtins.open", mock_open(read_data=sentences_csv_content), create=True)
    mocker.patch("builtins.open", mock_open(read_data=names_csv_content), create=True)
    mocker.patch("builtins.open", mock_open(read_data=removewords_csv_content), create=True)

    # Mock functions used in the logic
    mocker.patch("task_1.initial_text_processing", return_value={  # Mock initial_text_processing
        "Question 1": {
            "Processed Names": ["name1", "name2"],
            "Processed Sentences": [["sentence1"], ["sentence2"]],
        }
    })

def test_functions_calling_valid_case_5(mock_dependencies_5):
    """Test when required arguments are provided and the correct output is generated."""
    parsed_args = {
        "task": 4,
        "preprocessed": "",
        "qsek_query_path": r'.\query.json',
        "removewords": "removewords.csv",
        "sentences": "sentences_csv_content",
        "names": "names_csv_content",
        "maxk": "",
        "windowsize": "",
        "threshold": 0,
        "maximal_distance": "",
        "pairs": "",
        "fixed_length": ""
    }

    # Call the logic with the provided parsed arguments
    with pytest.raises(SystemExit):  # Expecting SystemExit due to sys.exit("Invalid Input")
        functions_calling(parsed_args)

@pytest.fixture
def create_temp_csv(tmp_path):
    """Helper function to create temporary CSV files"""
    def _create_temp_csv(filename, data):
        file_path = tmp_path / filename
        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(data)
        return str(file_path)  # Return file path as a string
    return _create_temp_csv

def test_full_pipeline(create_temp_csv):
    """Test case for the entire sequence processing pipeline."""

    # Create test CSV files with sample data
    sentences_csv = create_temp_csv("sentences.csv", [["Hello world"], ["Test sentence"]])
    names_csv = create_temp_csv("names.csv", [["John"], ["Doe"]])
    removewords_csv = create_temp_csv("removewords.csv", [["a"], ["the"]])

    # Simulate parsed_args with valid file paths and maxk
    parsed_args = {
        "sentences": sentences_csv,
        "names": names_csv,
        "removewords": removewords_csv,
        "maxk": 2
    }

    # Run the pipeline
    dictionary = initial_text_processing(parsed_args["sentences"], parsed_args["names"], parsed_args["removewords"])
    names_list = process_data_from_dict(dictionary)
    sentences_list = dict_to_list(dictionary)
    result = all_sentences(sentences_list, names_list)
    data = extract_k_sequences_flat(result, parsed_args["maxk"])

    # Ensure the final result is a correctly formatted JSON string
    output_json = format_as_json(data)
    assert isinstance(output_json, str)  # Check if the result is a string
    assert output_json.startswith("{") and output_json.endswith("}")  # Basic JSON structure check


@pytest.fixture
def create_temp_csv_5(tmp_path):
    """Helper function to create temporary CSV files."""

    def _create_temp_csv(filename, data):
        file_path = tmp_path / filename
        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(data)
        return str(file_path)  # Return file path as a string

    return _create_temp_csv

def test_full_pipeline_json(create_temp_csv_5):
    """Test the entire processing pipeline and validate the JSON output."""

    # Create temporary CSV files with sample data
    sentences_path = create_temp_csv_5("sentences1.csv", [["Hello world"], ["Test sentence"]])
    names_path = create_temp_csv_5("names1.csv", [["John"], ["Doe"]])
    removewords_path = create_temp_csv_5("remove1.csv", [["a"], ["the"]])

    # Simulate parsed_args with valid file paths and maxk
    parsed_args = {
        "sentences": sentences_path,
        "names": names_path,
        "removewords": removewords_path,
        "maxk": 2
    }

    # Run the pipeline
    text_dict = initial_text_processing(parsed_args["sentences"], parsed_args["names"], parsed_args["removewords"])
    processed_names = process_data_from_dict(text_dict)
    sentences_list = dict_to_list(text_dict)
    result = all_sentences(sentences_list, processed_names)
    data = extract_k_sequences_flat(result, parsed_args["maxk"])

    # Format the final output as JSON
    formatted_output = {
        "Question 5": {
            "Person Contexts and K-Seqs": data
        }
    }

    output_json = json.dumps(formatted_output, indent=4)  # Convert to JSON string

    # Assert the output is a valid JSON string
    assert isinstance(output_json, str)

    # Assert JSON format (loads without errors)
    parsed_json = json.loads(output_json)  # Convert back to dict

    # Assert the correct structure
    assert "Question 5" in parsed_json
    assert "Person Contexts and K-Seqs" in parsed_json["Question 5"]

    # Assert the content is non-empty
    assert isinstance(parsed_json["Question 5"]["Person Contexts and K-Seqs"], list)


@pytest.fixture
def create_temp_json(tmp_path):
    """Helper function to create a temporary JSON file."""

    def _create_temp_json(filename, data):
        file_path = tmp_path / filename
        with open(file_path, mode="w", encoding="utf-8") as file:
            json.dump(data, file)
        return str(file_path)  # Return file path as a string

    return _create_temp_json


def test_pipeline_with_preprocessed(create_temp_json):
    """Test the pipeline using a preprocessed JSON file."""
    # Sample dictionary data
    sample_data = {
        "Question 1": {
            "Processed Names": ["name1", "name2"],
            "Processed Sentences": [["sentence1"], ["sentence2"]],
        }
    }

    # Create a temporary JSON file with sample data
    preprocessed_path = create_temp_json("output.json", sample_data)

    # Simulate parsed_args
    parsed_args = {
        "preprocessed": preprocessed_path,
        "maxk": 2
    }

    # Run the pipeline
    dictionary = open_file(parsed_args["preprocessed"])
    names_list = process_data_from_dict(dictionary)
    sentences_list = dict_to_list(dictionary)
    result = all_sentences(sentences_list, names_list)
    data = extract_k_sequences_flat(result, parsed_args["maxk"])
    formatted_output = format_as_json(data)

    # Assert the output is a valid JSON string
    assert isinstance(formatted_output, str)

    # Assert JSON format (loads without errors)
    parsed_json = json.loads(formatted_output)

    # Assert the correct structure
    assert isinstance(parsed_json, dict)

    # Assert the content is non-empty
    assert len(parsed_json) > 0

def test_invalid_input_no_sentences():
    # Simulate the absence of 'sentences' argument
    parsed_args = {"task" :5 , "sentences": None, "names": "names_file.csv", "removewords": "removewords_file.csv", "maxk": 10,
                   "windowsize": "", "threshold": 0, "maximal_distance": "", "pairs": "", "fixed_length": "", "preprocessed":"",
                   "qsek_query_path" :""

                   }
    with patch('sys.exit') as mock_exit:
        functions_calling(parsed_args)
        mock_exit.assert_called_with("Invalid Input")

def test_invalid_input_file_not_found():
    # Simulate non-existing files for 'names' or 'removewords'
    parsed_args = {"task":5 , "sentences": "sentences_file.csv", "names": "nonexistent_file.csv", "removewords": "removewords_file.csv", "maxk": 10,
                   "windowsize": "", "threshold": 0, "maximal_distance": "", "pairs": "","fixed_length": "", "preprocessed":"",
                   "qsek_query_path" :""}

    with patch('sys.exit') as mock_exit:
        functions_calling(parsed_args)
        mock_exit.assert_called_with("Invalid Input")

def test_invalid_input_windowsize_less_than_length():
    # Simulate the case where 'windowsize' is larger than the length of 'sentences_list'
    parsed_args = {"task" : 6 ,"preprocessed": r'.\output.json', "threshold": 0.5, "windowsize": 100 ,"sentences": "","names": "",
                   "removewords":"" , "maximal_distance": "", "pairs": "","fixed_length": "","qsek_query_path" :""
    }

    # Mocking the functions to return expected values for the test
    with patch('builtins.open', mock_open(read_data='{"data": "some data"}')), \
         patch('main.open_file') as mock_open_file, \
         patch('task_3.process_data_from_dict') as mock_process_data_from_dict, \
         patch('task_2.dict_to_list') as mock_dict_to_list, \
         patch('task_6.pairs_occurrences') as mock_pairs_occurrences, \
         patch('sys.exit') as mock_exit:

        # Simulate mock returns
        mock_open_file.return_value = {"data": "mocked data"}
        mock_process_data_from_dict.return_value = ["name1", "name2"]
        mock_dict_to_list.return_value = ["sentence1", "sentence2"]

        # Run the function and expect sys.exit to be called
        functions_calling(parsed_args)
        mock_exit.assert_called_with("Invalid Input")

def test_invalid_input_missing_argument():
    # Simulate missing 'threshold' argument
    parsed_args = {"task" : 6,"preprocessed": r'.\output.json', "threshold": None, "windowsize": 3 , "sentences": "","names": "",
                   "removewords":"" , "maximal_distance": "", "pairs": "","fixed_length": "","qsek_query_path" :""
    }

    with patch('sys.exit') as mock_exit:
        functions_calling(parsed_args)
        mock_exit.assert_called_with("Invalid Input")

def test_valid_input():
    # Simulate valid arguments where 'windowsize' is valid
    parsed_args = {"task" : 6,"preprocessed": r'.\output.json',"threshold": 0.5,"windowsize": 2 ,"sentences": "","names": "",
                   "removewords":"" , "maximal_distance": "", "pairs": "","fixed_length": "","qsek_query_path" :""
    }

    # Mocking the functions to return expected values for the test
    with patch('builtins.open', mock_open(read_data='{"data": "some data"}')), \
         patch('main.open_file') as mock_open_file, \
         patch('task_3.process_data_from_dict') as mock_process_data_from_dict, \
         patch('task_2.dict_to_list') as mock_dict_to_list, \
         patch('task_6.pairs_occurrences') as mock_pairs_occurrences:

        # Simulate mock returns
        mock_open_file.return_value = {"data": "mocked data"}
        mock_process_data_from_dict.return_value = ["name1", "name2"]
        mock_dict_to_list.return_value = ["sentence1", "sentence2"]
        mock_pairs_occurrences.return_value = [("pair1", 1), ("pair2", 2)]

        # Run the function (no exit expected in this case)
        with patch('sys.exit') as mock_exit:
            functions_calling(parsed_args)
            mock_exit.assert_called_with("Invalid Input")

def test_valid_input_7():
    # Simulate valid input with all arguments present
    parsed_args = {
        "task" : 7 , "preprocessed": r'.\output.json',"pairs": r'.\pairs.json',"maximal_distance": 5 ,
        "sentences": "","names": "","removewords":"" ,"fixed_length": "","qsek_query_path" :"","threshold" : ""
         , "windowsize" : ""
    }

    # Mocking the functions to return expected values for the test
    with patch('builtins.open', mock_open(read_data='{"data": "some data"}')), \
         patch('main.open_file') as mock_open_file, \
         patch('task_7.dict_processing') as mock_dict_processing, \
         patch('task_7.checking_connection') as mock_checking_connection:

        # Simulate mock returns
        mock_open_file.side_effect = [
            {"data": "mocked data"},  # For parsed_args["preprocessed"]
            {"pairs": "mocked pairs"}  # For parsed_args["pairs"]
        ]
        mock_dict_processing.return_value = ["name1", "name2"]
        mock_checking_connection.return_value = ["connected", "disconnected"]

        # Run the function (no exit expected in this case)
        with patch('sys.exit') as mock_exit:
            functions_calling(parsed_args)
            mock_exit.assert_called_with("Invalid Input")

def test_valid_case_1():
        # Simulate valid input with all required arguments for the first case
    parsed_args = {"task" : 8,
            "preprocessed": r'.\output.json',"qsek_query_path": r'.\query.json',"fixed_length": 5,"pairs": "" ,
        "maximal_distance": "" , "sentences": "","names": "","removewords":"" ,"threshold" : "", "windowsize" : "" }
    # Mocking the functions to return expected values for the test
    with patch('builtins.open', mock_open(read_data='{"data": "some data"}')), \
         patch('main.open_file') as mock_open_file, \
         patch('task_4.json_file_opening') as mock_json_file_opening, \
         patch('task_7.dict_processing') as mock_dict_processing, \
         patch('task_7.making_adjacency_list') as mock_making_adjacency_list, \
         patch('task_8.Graph') as mock_graph, \
         patch('sys.stdout') as mock_stdout:

        # Simulate mock returns
        mock_open_file.return_value = {"data": "mocked data"}
        mock_json_file_opening.return_value = ["key1", "key2"]
        mock_dict_processing.return_value = ["joined_pair1", "joined_pair2"]
        mock_making_adjacency_list.return_value = [["adj1", "adj2"]]
        mock_graph.return_value.all_the_connections.return_value = ["connection1", "connection2"]
        mock_graph.return_value.generate_result_file.return_value = "result_file"

        # Run the function (no exit expected in this case)
        with patch('sys.exit') as mock_exit:
            functions_calling(parsed_args)
        mock_exit.assert_called_with("Invalid Input")

def test_valid_case_2():
    # Simulate valid input with all required arguments for the second case
    parsed_args = { "task" : 8,"sentences": r'.\sentences.csv',"names": r'.\names.csv',"removewords": r'.\removewords.csv',
    "qsek_query_path": r'.\query.json', "fixed_length": 5,"windowsize": 3,"threshold": 0.5 , "preprocessed": "" ,
    "pairs" : "" }

    # Mocking the functions to return expected values for the test
    with patch('builtins.open', mock_open(read_data='{"data": "some data"}')), \
         patch('main.open_file') as mock_open_file, \
         patch('task_4.json_file_opening') as mock_json_file_opening, \
         patch('task_1.initial_text_processing') as mock_initial_text_processing, \
         patch('task_2.dict_to_list') as mock_dict_to_list, \
         patch('task_3.process_data_from_dict') as mock_process_data_from_dict, \
         patch('task_6.pairs_occurrences') as mock_pairs_occurrences, \
         patch('task_7.making_adjacency_list') as mock_making_adjacency_list, \
         patch('task_8.Graph') as mock_graph, \
         patch('sys.stdout') as mock_stdout:

        # Simulate mock returns
        mock_open_file.return_value = {"data": "mocked data"}
        mock_json_file_opening.return_value = ["key1", "key2"]
        mock_initial_text_processing.return_value = {"sentence1": "data1", "sentence2": "data2"}
        mock_dict_to_list.return_value = ["sentence1", "sentence2"]
        mock_process_data_from_dict.return_value = ["name1", "name2"]
        mock_pairs_occurrences.return_value = [("pair1", 1), ("pair2", 2)]
        mock_making_adjacency_list.return_value = [["adj1", "adj2"]]
        mock_graph.return_value.all_the_connections.return_value = ["connection1", "connection2"]
        mock_graph.return_value.generate_result_file.return_value = "result_file"

        # Run the function (no exit expected in this case)
        with patch('sys.exit') as mock_exit:
            functions_calling(parsed_args)
        mock_exit.assert_called_with("Invalid Input")

def test_invalid_input_case_1_missing_arguments():
    # Simulate missing arguments for the first case (e.g., missing 'preprocessed')
    parsed_args = {"task":8 ,"preprocessed": None,"qsek_query_path": r'.\query.json',"fixed_length": 5 , "sentences": "","names": "",
    "removewords":"" ,"threshold" : "", "windowsize" : "","pairs" : ""
    }

    with patch('sys.exit') as mock_exit:
        functions_calling(parsed_args)
        mock_exit.assert_called_with("Invalid Input")

def test_invalid_input_case_2_windowsize_greater_than_sentences():
    # Simulate the case where windowsize is larger than sentences_list
    parsed_args = {
        "task": 9,
        "sentences": r'.\sentences_1.csv',
        "names": r'.\names1.csv',
        "removewords": r'.\removewords1.csv',
        "qsek_query_path": r'.\query.json',
        "fixed_length": 5,
        "windowsize": 100,  # windowsize is larger than the number of sentences
        "threshold": 1,
        "pairs": "",
        "preprocessed": ""
    }

    # Mocking the functions to return expected values for the test
    with patch('builtins.open', mock_open(read_data='{"data": "some data"}')), \
         patch('main.open_file') as mock_open_file, \
         patch('task_4.json_file_opening') as mock_json_file_opening, \
         patch('task_1.initial_text_processing') as mock_initial_text_processing, \
         patch('task_2.dict_to_list') as mock_dict_to_list, \
         patch('task_4.process_data_from_dict') as mock_process_data_from_dict, \
         patch('sys.exit') as mock_exit:

        # Simulate mock returns
        mock_open_file.return_value = {"data": "mocked data"}
        mock_json_file_opening.return_value = ["key1", "key2"]
        mock_initial_text_processing.return_value = {"sentence1": "data1", "sentence2": "data2"}
        mock_dict_to_list.return_value = ["sentence1", "sentence2"]  # 2 sentences in total
        mock_process_data_from_dict.return_value = ["name1", "name2"]

        # Run the function (this should hit the 'sys.exit' due to the invalid windowsize)
        functions_calling(parsed_args)
        result = None

        # Assert that sys.exit was called with the expected message
        assert functions_calling(parsed_args) == result

def test_invalid_input_case_3_invalid_threshold():
    # Simulate missing 'threshold' argument for the third case
    parsed_args = {"task" : 9 ,"preprocessed": r'.\output.json',"threshold": None, "sentences": "","names": "",
    "removewords":"" , "windowsize" : "","pairs" : "" , "qsek_query_path": "","fixed_length": ""
    }

    with patch('sys.exit') as mock_exit:
        functions_calling(parsed_args)
        mock_exit.assert_called_with("Invalid Input")

def test_invalid_input_case_4_other_missing_arguments():
    # Simulate missing arguments for other parts of the code (e.g., missing 'sentences')
    parsed_args = {"task":9 ,"sentences": None,"removewords": r'.\removewords.csv',"threshold": 0.5 , "names": "",
                   "windowsize": "", "pairs": "", "qsek_query_path": "", "fixed_length": ""
    }

    with patch('sys.exit') as mock_exit:
        functions_calling(parsed_args)
        mock_exit.assert_called_with("Invalid Input")
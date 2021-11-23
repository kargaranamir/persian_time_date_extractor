import re
from pattern_to_regex import res_pattern_list as pattern_list
from utilities.Utilities import normalize_cumulative as normalize

def time_marker_extractor(input_sentence):
    """
    function should output list of strings, each item in list is a time marker present in the input sentence.
    :param input_sentence:
    :return:
    """
    input_sentence = normalize(input_sentence)
    output = []
    for i in range(len(pattern_list)):
        out = re.findall(fr'\b(?:{pattern_list[i]})', input_sentence)
        output.append(out)

    res = max(output, key=len)

    return [res]
import inspect
import sys
from collections import Counter
"""
Raise a "not defined" exception as a reminder
"""


def _raise_not_defined():
    print("Method not implemented: %s" % inspect.stack()[1][3])
    sys.exit(1)


"""
Extract 'basic' features, i.e., whether a pixel is background or
forground (part of the digit)
"""


def extract_basic_features(digit_data, width, height):
    features = []
    for i in range(width):
        for j in range(height):

            if digit_data[i][j] == 1 or digit_data[i][j]==2:
                features.append(True)
            else:
                features.append(False)
    # Your code starts here
    # You should remove _raise_not_defined() after you complete your code
    # Your code ends here
    return features


"""
Extract advanced features that you will come up with
"""


def extract_advanced_features(digit_data, width, height):
    features = []
    # Your code starts here
    # You should remove _raise_not_defined() after you complete your code
    # Your code ends here
    _raise_not_defined()
    return features


"""
Extract the final features that you would like to use
"""


def extract_final_features(digit_data, width, height):
    features = []
    # Your code starts here
    # You should remove _raise_not_defined() after you complete your code
    # Your code ends here
    _raise_not_defined()
    return features


"""
Compupte the parameters including the prior and and all the P(x_i|y). Note
that the features to be used must be computed using the passed in method
feature_extractor, which takes in a single digit data along with the width
and height of the image. For example, the method extract_basic_features
defined above is a function than be passed in as a feature_extractor
implementation.

The percentage parameter controls what percentage of the example data
should be used for training.
"""
computedStatistics = dict()

def compute_statistics(data, label, width, height, feature_extractor, percentage=100.0):
    '''predicted = []
    rng = len(data) * percentage / 100
    rng = int(rng)
    countThisPlace = dict()
    global computedStatistics
    dict_label = Counter(label[:len(label)*int(percentage/100)])
    for l in dict_label:
        dict_label[l] /= len(label)*int(percentage/100)
    for i in range(rng):
        #curFeature = feature_extractor(data[i],width,height)
        #curLabel = label[i]
        countTrue =0
        for j in  range(width):
            for k in range(height):
                if data[i][j][k] == True:
                    countTrue += 1



            continue

        computedStatistics[curLabel] = curFeature'''

    #print(computedStatistics)
    #print(label)
    prob_label = []
    k=10
    dict_label = Counter(label[:len(label)*int(percentage/100)])
    for l in dict_label:
        dict_label[l] /= len(label)*int(percentage/100)
    dictLabel = dict()
    for i in range(len(label)):
        curLabel = label[i]
        curImg = data[i]
        curFeature = feature_extractor(curImg,width,height)
        if curLabel in  dictLabel:
            dictLabel[curLabel].append(curFeature)
            continue
        dictLabel[curLabel] = [curFeature]
    countTrue = 0
    trueAtThisPos = dict()
    labeList = dict()
    for i in range(len(dictLabel[1])):
        trueAtThisPos[i] = 0
    for i in dictLabel:
        l = dictLabel[i]
        for j in l:
            for index,k in enumerate(j):
                if k == True:
                    if index in trueAtThisPos:
                        trueAtThisPos[index] += 1
                        continue
            for m in trueAtThisPos:
                li = list()
                for n in range(len(dictLabel[1])):
                    li.append(trueAtThisPos[n])
                labeList[i] = li
                # for o in range(len(dictLabel[1])):
                #     trueAtThisPos[o] = 0
    print(labeList)

    #print(trueAtThisPos)
    # global computedStatistics
    # predicted = []
    # for i in range(len(data)):
    #     features = feature_extractor(i,width,height)

    # Your code starts here
    # You should remove _raise_not_defined() after you complete your code
    # Your code ends here
    _raise_not_defined()


"""
For the given features for a single digit image, compute the class
"""


def compute_class(features):
    predicted = -1

    # Your code starts here
    # You should remove _raise_not_defined() after you complete your code
    # Your code ends here
    _raise_not_defined()

    return predicted


"""
Compute joint probaility for all the classes and make predictions for a list
of data
"""

computedStatistics = []
def classify(data, width, height, feature_extractor):



    # Your code starts here
    # You should remove _raise_not_defined() after you complete your code
    # Your code ends here
    _raise_not_defined()

    return predicted

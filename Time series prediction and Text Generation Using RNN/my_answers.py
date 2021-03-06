import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Activation
import keras


# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series,window_size):
    p=0
    X=[]  
    y=[]  
    while(p+window_size < len(series)):
       X.append(series[p:p+window_size])
       p=p+1
    y=series[window_size:]
    return np.asarray(X),np.reshape(y,(len(y),1))
'''
def window_transform_series(series, window_size):
    # containers for input/output pairs
    X = []
    y = []

    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)

    return X,y
'''

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(window_size):
    model = Sequential()
    model.add(LSTM(5, input_shape=(window_size,1)))
    model.add(Dense(1))
    #model.compile(loss='mean_squared_error', optimizer='adam')
    #model.fit(trainX, trainY, epochs=100, batch_size=1, verbose=2)
    return model
    pass

def is_ascii_alpha(word):
    try:
        return word.encode('ascii').isalpha()
    except:
        return False

### TODO: return the text input with only ascii lowercase and the punctuation given below included.
def cleaned_text(text):
    punctuation = ['!', ',', '.', ':', ';', '?']
    text=text.lower()
    uniqchars = set(text)
    #print (uniqchars)
    for char in uniqchars:
        #if ((len(char)>0) and (not is_ascii_alpha(char)) and (not char.isnumeric()) and (char not in punctuation)):
        if ((len(char)>0) and (not is_ascii_alpha(char))  and (char not in punctuation)):
            #print (char)
            text=text.replace(char,' ')
    return text

### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text, window_size, step_size):
    # containers for input/output pairs
    inputs = []
    outputs = []
    p=0
    while(p+window_size < len(text)):
       inputs.append(text[p:p+window_size])
       outputs.append(text[p+window_size])
       p=p+step_size  

    return inputs,outputs

# TODO build the required RNN model: 
# a single LSTM hidden layer with softmax activation, categorical_crossentropy loss 
def build_part2_RNN(window_size, num_chars):
    model = Sequential()
    model.add(LSTM(200, input_shape=(window_size,num_chars)))
    model.add(Dense(num_chars))
    model.add(Activation('softmax'))
    return model

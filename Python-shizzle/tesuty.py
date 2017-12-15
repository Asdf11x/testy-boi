#!/usr/bin/env python

"""tesuty.py: try something."""

from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D
from keras.models import Sequential

__author__      = "Asdf"
__copyright__   = "Copyright 2017, Planet Earth"


class Tesuu:

    def foobar(self, input_shape, num_classes):
        model = Sequential()
        model.add(Conv2D(32, kernel_size=(5, 5), strides=(1, 1),
                         activation='relu',
                         input_shape=input_shape))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
        model.add(Conv2D(64, (5, 5), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Flatten())
        model.add(Dense(1000, activation='relu'))
        model.add(Dense(num_classes, activation='softmax'))
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
from tensorflow.keras import regularizers

def build_model(input_dim, output_dim, optimizer, use_dropout=False, use_bn=False, l2_reg=None):
    model = Sequential()
    if l2_reg:
        reg = regularizers.l2(l2_reg)
    else:
        reg = None
    model.add(Dense(512, activation='relu', input_dim=input_dim, kernel_regularizer=reg))
    if use_bn:
        model.add(BatchNormalization())
    if use_dropout:
        model.add(Dropout(0.3))
    model.add(Dense(256, activation='relu', kernel_regularizer=reg))
    if use_bn:
        model.add(BatchNormalization())
    if use_dropout:
        model.add(Dropout(0.3))
    model.add(Dense(output_dim, activation='softmax'))
    model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
    return model
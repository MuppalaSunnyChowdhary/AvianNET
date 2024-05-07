from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, GRU, Conv2D, MaxPooling2D
from tensorflow.keras.layers import Dropout, Flatten, BatchNormalization, TimeDistributed
from tensorflow.keras.optimizers import Adam

# Assuming mfccs has shape (num_samples, timesteps, features) e.g., (1000, 44, 13)
# where 1000 is the number of samples, 44 is the number of timesteps, and 13 is the number of MFCC features.

input_shape = (44, 13)  # This needs to match the shape of your MFCC input

# Create the model
model = Sequential()

# First, add a Convolutional layer that will learn frequency patterns
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=input_shape + (1,)))
model.add(MaxPooling2D((2, 2)))
model.add(BatchNormalization())

# Add more Convolutional layers
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(BatchNormalization())

model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(BatchNormalization())

# Flatten the output of the conv layers to feed into the RNN
model.add(TimeDistributed(Flatten()))

# Add one or more GRU layers
model.add(GRU(128, return_sequences=True))
model.add(GRU(128, return_sequences=False))

# Add a Dropout layer for regularization
model.add(Dropout(0.5))

# Add a Dense layer with a softmax activation for classification
model.add(Dense(91, activation='softmax'))  # Change the number of neurons to match the number of classes you have

# Compile the model
model.compile(optimizer=Adam(lr=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

# Model summary
model.summary()

# Train the model - you will need to add your actual data here
# model.fit(train_data, train_labels, epochs=100, batch_size=32, validation_split=0.2)

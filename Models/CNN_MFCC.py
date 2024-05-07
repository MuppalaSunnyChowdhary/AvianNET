import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Flatten, Dense, Dropout, BatchNormalization

# Define the input shape (number of MFCC coefficients, number of frames, 1 channel for mono audio)
input_shape = (num_mfcc_coeffs, num_frames, 1)  # Replace with actual shape

# Create the model
model = Sequential()

# First layer with input shape and batch normalization
model.add(Conv2D(32, kernel_size=(3, 3), activation='tanh', input_shape=input_shape))
model.add(BatchNormalization())

# Add more Convolutional layers with pooling and dropout to prevent overfitting
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

# Flatten the output of the convolutional layers
model.add(Flatten())

# Add dense layers for further processing
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))

# Output layer with 'softmax' activation for multi-class classification
model.add(Dense(num_classes, activation='softmax'))  # num_classes is the number of bird species

# Compile the model with appropriate loss function and optimizer
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# Summary of the CNN model architecture
model.summary()

# Assuming you have training_data and training_labels prepared
# Fit the model on the training data
model.fit(training_data, training_labels, epochs=50, validation_split=0.2, verbose=1)

# Save the model
model.save('bird_species_cnn_model.h5')

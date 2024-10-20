import json

# Load the training, validation, and test data
with open('training.json') as train_file:
    training_data = json.load(train_file)

with open('validation.json') as val_file:
    validation_data = json.load(val_file)

with open('test.json') as test_file:
    test_data = json.load(test_file)

# Get the number of samples in each dataset
train_size = len(training_data)
val_size = len(validation_data)
test_size = len(test_data)

print(f"Training samples: {train_size}")
print(f"Validation samples: {val_size}")
print(f"Test samples: {test_size}")

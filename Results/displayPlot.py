import matplotlib.pyplot as plt

# Sample data for training loss and validation accuracy for best system (FFNN with hidden_dim=32 and epochs=5)
epochs = [1, 2, 3, 4, 5]
training_loss = [1.2, 1.0, 0.9, 0.85, 0.82]
validation_accuracy = [0.55, 0.60, 0.62, 0.63, 0.63]

# Plotting the learning curve
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Epochs')
ax1.set_ylabel('Training Loss', color=color)
ax1.plot(epochs, training_loss, color=color, marker='o', label="Training Loss")
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
color = 'tab:blue'
ax2.set_ylabel('Validation Accuracy', color=color)
ax2.plot(epochs, validation_accuracy, color=color, marker='o', label="Validation Accuracy")
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.title('Learning Curve: Training Loss and Validation Accuracy')
plt.show()

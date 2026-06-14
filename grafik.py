import matplotlib.pyplot as plt
import os


os.makedirs("hasil", exist_ok=True)


epoch = range(1, 11)


accuracy = [
    0.3859,
    0.5896,
    0.6674,
    0.7161,
    0.7301,
    0.7635,
    0.7690,
    0.7820,
    0.7966,
    0.8045
]


val_accuracy = [
    0.6180,
    0.7680,
    0.7740,
    0.8360,
    0.8735,
    0.8185,
    0.8885,
    0.8935,
    0.9010,
    0.8960
]


loss = [
    1.4518,
    1.0536,
    0.8449,
    0.7252,
    0.6744,
    0.6140,
    0.5856,
    0.5581,
    0.5293,
    0.5197
]


val_loss = [
    1.1736,
    0.8357,
    0.6878,
    0.5767,
    0.5114,
    0.4598,
    0.4281,
    0.3816,
    0.3639,
    0.3667
]


# Grafik Accuracy
plt.figure(figsize=(8,5))

plt.plot(epoch, accuracy, label="Training Accuracy")
plt.plot(epoch, val_accuracy, label="Validation Accuracy")

plt.title("Accuracy Training dan Validation")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.grid()

plt.savefig("hasil/accuracy_graph.png")

plt.close()


# Grafik Loss
plt.figure(figsize=(8,5))

plt.plot(epoch, loss, label="Training Loss")
plt.plot(epoch, val_loss, label="Validation Loss")

plt.title("Loss Training dan Validation")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.grid()

plt.savefig("hasil/loss_graph.png")

plt.close()


print("Grafik berhasil dibuat!")
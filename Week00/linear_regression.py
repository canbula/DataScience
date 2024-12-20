import numpy as np
import matplotlib.pyplot as plt


ORIGINAL_SLOPE = 5
ORIGINAL_INTERCEPT = 3
NOISE = 6
NUMBER_OF_DATA_POINTS = 100
START = 0
STOP = 10
SEED = 0


def mse(y_true_, y_pred_):
    return np.mean((y_true_ - y_pred_) ** 2)


def mse_derivative(x_, y_, a_, b_):
    y_pred_ = a_ * x_ + b_
    da_ = 2 * np.mean((y_pred_ - y_) * x_)
    db_ = 2 * np.mean(y_pred_ - y_)
    return da_, db_


def gradient_descent(x_, y_, learning_rate_, epochs_):
    a_ = ORIGINAL_SLOPE
    b_ = ORIGINAL_INTERCEPT
    mse_values = np.zeros(epochs_)
    a_values = np.zeros(epochs_)
    b_values = np.zeros(epochs_)
    for i in range(epochs_):
        y_pred_ = a_ * x_ + b_
        da_, db_ = mse_derivative(x_, y_, a_, b_)
        a_ -= learning_rate_ * da_
        b_ -= learning_rate_ * db_
        mse_values[i] = mse(y_, y_pred_)
        a_values[i] = a_
        b_values[i] = b_
        if i % 100 == 0:
            print(
                f"Epoch {i}: MSE = {mse(y_, y_pred_):.2f} (a = {a_:.2f}, b = {b_:.2f})"
            )
    return a_, b_, {"mse": mse_values, "a": a_values, "b": b_values}


a = np.int64(ORIGINAL_SLOPE)
b = np.int64(ORIGINAL_INTERCEPT)
np.random.seed(SEED)
x = np.linspace(START, STOP, NUMBER_OF_DATA_POINTS)
y_original = a * x + b
y_true = a * x + b + np.random.normal(0, NOISE, NUMBER_OF_DATA_POINTS)
# a_, b_ = np.polyfit(x, y_true, 1)
# y = a_ * x + b_
a_, b_, fit_info = gradient_descent(x, y_true, 1e-2, 1001)
y = a_ * x + b_

plt.plot(x, y_original, color="gray", label=f"Original Line: y = {a} * x + {b}")
plt.scatter(x, y_true, color="blue", label="Distorted Data Points")
plt.plot(
    x,
    y,
    color="red",
    label=f"Best Fit: y = {a_:.2f} * x + {b_:.2f} (MSE: {mse(y_true, y):.2f})",
)
plt.xlim(START, STOP)
plt.ylim(-10, 80)
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="upper left")
plt.show()

a_values = np.linspace(0, 10, 100)
b_values = np.linspace(0, 10, 100)
mse_for_a = np.zeros(100)
mse_for_b = np.zeros(100)
for i, a_ in enumerate(a_values):
    mse_for_a[i] = mse(y_true, a_ * x + b)
for i, b_ in enumerate(b_values):
    mse_for_b[i] = mse(y_true, a * x + b_)
fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].plot(a_values, mse_for_a)
ax[0].set_xlabel("Slope (a)")
ax[0].set_ylabel("MSE")
ax[0].set_title("MSE vs. Slope")
ax[1].plot(b_values, mse_for_b)
ax[1].set_xlabel("Intercept (b)")
ax[1].set_ylabel("MSE")
ax[1].set_title("MSE vs. Intercept")
plt.show()


mse_values = np.zeros((100, 100))
for i, a_ in enumerate(a_values):
    for j, b_ in enumerate(b_values):
        mse_values[i, j] = mse(y_true, a_ * x + b_)
a_index, b_index = np.unravel_index(np.argmin(mse_values), mse_values.shape)
a_best = a_values[a_index]
b_best = b_values[b_index]
plt.contourf(a_values, b_values, mse_values, levels=20)
plt.colorbar()
plt.scatter(a, b, color="gray", label="Original Line")
# plt.scatter(a_, b_, color="blue", label="Best Fit")
plt.scatter(a_best, b_best, color="red", label="Best Fit")
# add fit info
plt.plot(fit_info["a"], fit_info["b"], color="green", label="Gradient Descent")
plt.xlabel("Slope (a)")
plt.ylabel("Intercept (b)")
plt.legend(loc="upper left")
plt.show()

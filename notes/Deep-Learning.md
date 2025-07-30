# Deep Learning 

[PDF Notes](../pdf/3_Deep_Learning_Overview.pdf)

## Quick Facts
## Core Concepts
The loss function in deep learning quantifies the difference between the model prediction and the target value.

The cross-entropy loss function is particularly suitable for classification problems, as it measures the difference between predicted and actual probability distributions.

A convex set is one in which the line segment between any two points in the set also lies entirely within the set.

A classification hyperplane is defined by the weights of a perceptron and divides the input space into distinct classes.

Deep learning allows models to automatically extract features from data without manual feature engineering.

Increasing the number of hidden layers in a neural network can help the model learn more abstract features.

A fully connected (dense) layer treats all input units equally and is typically used for decision-making after feature extraction.


## Activation Functions and Problems
The Softmax function outputs a probability distribution over multiple classes, where the sum of outputs is 1.

The sigmoid activation function can cause vanishing gradient problems in deep neural networks.

The softsign activation function is a smoother alternative to tanh and can help avoid saturation issues.

ReLU (Rectified Linear Unit) is an activation function that outputs zero for negative inputs and passes positive values unchanged.

ReLU does not allow the backpropagation of gradients for negative input values.

The ReLU activation function introduces non-linearity and is widely used in modern neural networks.

The vanishing gradient problem arises when gradients become very small, preventing weights from updating effectively in deep networks.

The vanishing gradient problem can be alleviated by using ReLU activation or LSTM architectures.

The exploding gradient problem occurs when gradients grow excessively during backpropagation, often in deep or recurrent networks.


## Training and Regularization Methods
Backpropagation algorithm minimizes the error by propagating the loss from output to input using chain rule.

Backpropagation uses the chain rule of calculus to compute gradients layer by layer.

Dropout works by randomly disabling some neurons during training to prevent overfitting.

Dropout acts as a regularization method by randomly disabling neurons during training, thus reducing model dependence on specific nodes.

L1 regularization encourages sparsity by driving some weights exactly to zero.

Noise injection during training can improve model robustness by making it less sensitive to small variations in input.

Early stopping monitors validation performance and halts training when the model begins to overfit.


## Optimization
The Adam optimizer combines the benefits of both momentum and adaptive learning rates.

The Adam optimizer adapts the learning rate for each parameter using the first and second moments of gradients.

The momentum optimizer adds an inertial term to the gradient update, helping to accelerate convergence and escape local minima.


## Network Types
CNNs are especially effective in processing visual data due to local receptive fields and parameter sharing.

Parameter sharing in CNNs drastically reduces the number of learnable weights compared to fully connected networks.

RNNs are designed to handle sequential data by maintaining context through hidden states.

A Recurrent Neural Network (RNN) maintains internal memory to process sequences of data, making it suitable for tasks like language modeling.

GRU (Gated Recurrent Unit) is a type of RNN that uses gates to control the flow of information and solve vanishing gradient problems.

BPTT (Backpropagation Through Time) is used in training RNNs by unrolling the network across time steps.

In a GAN, the generator learns to produce fake data to fool the discriminator, which learns to distinguish fake from real.

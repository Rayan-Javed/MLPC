### 1. Classification as Regression

- Classification can be seen as predicting a **probability** (a number between 0 and 1).
    
- Example: output = probability of “salmon”; if > 0.5 → salmon, else bass.
    
- So the task becomes **regression** – learning a function f(x)f(x) that maps features to a numeric output.
    

---
![[Pasted image 20260614052404.png]]

---

### 3. Why We Need Non‑Linearity

- Real data often has **curves, bumps, and wiggles** (e.g., fuel consumption flattening at large engine size).
    
- A straight line cannot fit such shapes.
    
- We need a **non‑linear function** – built by combining many simple “bumps”.
    

---

### 4. Multi‑Layer Feed‑Forward Network (MLP)

- **Structure**:
    
    - Input layer – one neuron per feature (no computation).
        
    - One or more **hidden layers** – each neuron computes weighted sum of inputs, adds a bias, then applies an **activation function**.
        
    - Output layer – produces final prediction (often a probability).
        
- **Feed‑forward**: information flows only forward (input → hidden → output), no loops.
    

---

### 5. Activation Functions – The “Magic”

- Without activation functions, stacking layers would still be linear.
    
- **Non‑linear** activation functions (tanh, sigmoid, ReLU) allow the network to learn curves and complex patterns.
    
- tanh squashes input to [−1,1]; sigmoid squashes to [0,1] (useful for probabilities); ReLU outputs input if positive else 0 (fast and popular).
    

---

### 6. Universal Approximation Theorem

- A neural network with **one hidden layer** (and enough neurons) can approximate **any continuous function** to any desired accuracy.
    
- However, “enough neurons” might be astronomically many. **Deep networks** (many hidden layers) can represent the same function with far fewer total neurons by building hierarchical features.
    

---

### 7. Training Neural Networks – Gradient Descent & Backpropagation

- **Training** = adjusting weights and biases to minimise the error (loss) function.
    
- **Gradient Descent**:
    
    - Compute the gradient (direction of steepest increase of error).
        
    - Step in the opposite direction (downhill).
        
    - Step size = **learning rate** (η). Too high → overshoot; too low → slow.
        
- **Backpropagation**:
    
    - Problem: hidden layers have no “target” values.
        
    - Solution: propagate error **backward** from output to input, computing how much each weight contributed to the error.
        
    - This gives the gradient for every weight, allowing gradient descent.
        

---

### 8. Bias‑Variance Trade‑off in Neural Networks

- **High bias** (underfitting): model too simple → systematic errors.
    
- **High variance** (overfitting): model too complex → fits noise, fails on new data.
    
- Small network → high bias; large network → high variance.
    
- Monitor validation error: when it starts rising while training error keeps falling, stop (early stopping).
    
- Other anti‑overfitting methods: regularisation (penalise large weights), dropout (randomly turn off neurons), more data.
    

---

### 9. Deep Networks (Many Hidden Layers)

- **Deep learning** = stacking many hidden layers.
    
- Advantages:
    
    - Learn **hierarchical features** (edges → shapes → objects).
        
    - More efficient than a single wide hidden layer for complex functions.
        
- Challenges: vanishing gradients (early layers learn very slowly), need large data & computing power (GPUs).
    

---

### 10. Practical Comparison with Other Classifiers

|Classifier|Strengths|Weaknesses|
|---|---|---|
|Decision Tree|Interpretable, fast|Axis‑aligned, overfits|
|k‑NN|Simple, no training|Slow prediction, curse of dimensionality|
|SVM|Robust, works in high dimensions|Hard to interpret, slow to train|
|Neural Network|Very flexible, state‑of‑the‑art for complex tasks|Black box, needs lots of data & tuning, slow training|

---

### 11. Key Takeaways (for the exam)

- Non‑linear activation functions are **essential**.
    
- Backpropagation enables learning in hidden layers.
    
- Overfitting is a major risk – use validation, early stopping, regularisation.
    
- Deep networks (multiple hidden layers) are powerful but not always needed.
    
- Understand the **flow**: forward pass to compute output, backward pass to compute gradients, gradient descent to update weights.


Here are the **answers** to the 20 knowledge check questions from Chapter 7.

---

### Basic Concepts

1. **Why is classification considered a regression task?**  
   Classification can be seen as predicting the **probability** that an example belongs to a class (e.g., 0 for bass, 1 for salmon). That probability is a numeric value, so the task becomes a regression problem (predicting a number). You then convert the number to a class label (e.g., >0.5 → salmon).

2. **Name three types of layers in a feed‑forward neural network.**  
   - Input layer (holds features)  
   - Hidden layer(s) (process information)  
   - Output layer (produces final prediction)

3. **What is the purpose of an activation function?**  
   It introduces **non‑linearity**. Without it, stacking layers would still be linear, and the network could only learn straight lines / flat planes. Activation functions allow the network to learn curves, bumps, and complex patterns.

4. **Give two examples of activation functions and their output ranges.**  
   - **tanh** → output range \([-1, 1]\)  
   - **sigmoid** → output range \([0, 1]\)  
   - **ReLU** → output range \([0, \infty)\) (non‑negative)

---

### Architecture & Computation

5. **A network has 5 input features, one hidden layer with 8 neurons, and an output layer with 2 neurons. How many weights?**  
   - Input → hidden: \(5 \times 8 = 40\)  
   - Hidden → output: \(8 \times 2 = 16\)  
   - Total weights = \(40 + 16 = 56\)  
   - (Biases: 8 + 2 = 10 extra parameters if asked.)

6. **What does “feed‑forward” mean? How is it different from recurrent networks?**  
   Feed‑forward means information moves **only forward** from input to output, with no loops or feedback. Recurrent networks have loops that allow information to persist (like memory), which is useful for sequences (text, time series).

7. **What is the Universal Approximation Theorem? Does it mean one hidden layer is always enough in practice?**  
   The theorem says a network with **one hidden layer** (and enough neurons) can approximate any continuous function to any desired accuracy.  
   However, in practice, “enough neurons” may be astronomically large, making training impossible. Deep networks (many layers) can represent the same function with far fewer neurons, so they are often preferred.

---

### Training & Learning

8. **Describe gradient descent in your own words. What is the learning rate?**  
   Gradient descent is an optimisation method: start with random weights, compute the slope (gradient) of the error function, then take a small step downhill (opposite direction). Repeat until you reach a low error.  
   The **learning rate** (\(\eta\)) controls the step size. Too large → you might overshoot; too small → learning is very slow.

9. **Why can’t we directly compute the error for hidden units?**  
   Because hidden units have no “target” values from the data. We only know the correct output for the whole network, not what each hidden unit should produce.

10. **What does backpropagation do? Explain the intuition of “blame assignment”.**  
    Backpropagation computes how much each weight (especially in hidden layers) contributed to the final error. It sends error signals **backward** through the network, from output to input, using the chain rule.  
    *Intuition:* It’s like a team of workers: if the final product is wrong, you send a message backward to each worker telling them how much they are to blame, so they can adjust.

11. **What happens to the error if the learning rate is set too high? Too low?**  
    - Too high → the weights bounce around and may never settle; error may oscillate or diverge.  
    - Too low → learning is extremely slow; you need many training epochs to reach a good minimum.

---

### Overfitting & Bias‑Variance

12. **How can you tell if a neural network is overfitting?**  
    Training error keeps decreasing, but **validation error** stops improving or starts increasing. The model memorises noise in training data and fails on new data.

13. **Name three techniques to reduce overfitting in neural networks.**  
    - Early stopping (stop when validation error rises)  
    - Regularisation (add penalty for large weights, e.g., L2)  
    - Dropout (randomly turn off neurons during training)  
    - Use more training data  
    - Reduce network size (fewer layers / neurons)

14. **Explain the bias‑variance trade‑off in the context of neural networks. When would you prefer a small network? A large one?**  
    - **High bias** (small network): model too simple → underfits (systematic errors).  
    - **High variance** (large network): model too complex → overfits (fits noise).  
    - **Prefer small network** when you have limited data or the true function is simple.  
    - **Prefer large network** when you have lots of data and the problem is complex (e.g., image recognition).

---

### Deep Networks

15. **What is the main advantage of having many hidden layers (deep network) over a single hidden layer?**  
    Deep networks can learn **hierarchical features**: earlier layers learn simple patterns (edges, tones), later layers combine them into complex structures (objects, faces). They can represent the same function with far fewer total neurons than a shallow network.

16. **Why might training a deep network be more difficult than a shallow one?**  
    - **Vanishing gradients**: gradients become very small in early layers, so they learn very slowly.  
    - Need more data and computing power (GPUs).  
    - More hyperparameters (learning rates, layer sizes, etc.) to tune.  
    - Higher risk of overfitting.

---

### Comparison & Application

17. **When would you choose a neural network over a decision tree? Over a k‑NN?**  
    - Over a decision tree: when you need high accuracy on complex, high‑dimensional data (images, audio, text) and don’t need interpretability.  
    - Over k‑NN: when you have a large dataset (k‑NN is slow at prediction) and the decision boundary is very non‑linear.

18. **A dataset has only 100 examples. Is it a good candidate for a large neural network? Why or why not?**  
    No. A large neural network would likely overfit because it has many more parameters than training examples. A simpler model (e.g., logistic regression, small decision tree) would generalise better.

19. **In the music detection example, why would a 0.4‑second “music” segment likely be an error? How does smoothing help?**  
    Real music segments are typically longer (e.g., several seconds). A very short isolated “music” prediction is likely noise or a transient sound.  
    **Smoothing** looks at neighbouring frames; if a short segment disagrees with its neighbours, it is corrected to the majority label, removing false positives.

---

### Exam‑Style Scenario

20. **Suppose you train a neural network and obtain very low training error but poor test error. What is the most likely problem? What steps would you take to fix it?**  
    **Problem:** Overfitting. The model memorised the training data, including noise.  
    **Fixes:**  
    - Increase training data (if possible).  
    - Use early stopping (monitor validation error).  
    - Add regularisation (L2 weight penalty).  
    - Add dropout.  
    - Reduce network size (fewer layers / neurons).  
    - Simplify the model or use cross‑validation.

---

Now you have both the questions and the answers. Good luck with your exam preparation!


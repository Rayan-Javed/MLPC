# Chapter 1: Introduction to Pattern Classification 

Welcome! This is the first chapter of your Machine Learning & Pattern Classification (MLPC) course. I’ll explain every slide, every word, every picture, and every formula. We’ll go **slowly** and use **very simple examples**. By the end, you will understand what this class is about, what “classification” means, and how a machine can learn to make decisions – like telling a sea bass from a salmon.

I have split this chapter into **6 small parts**. Each part covers a few related topics. Read them in order. After each part, you’ll have a clear piece of the puzzle.

---

## Part 1: What is this class all about? (Slides 1–9)

### Topic 1.1: The goal of this class
This class teaches you **supervised machine learning** for **classification tasks**.  
- **Supervised** = you show the computer examples with correct answers.  
- **Machine learning** = the computer learns a rule (a “classifier”) from those examples.  
- **Classification** = putting things into groups (classes), e.g., “sea bass” or “salmon”.  

The class focuses on **real-world problems** – not just theory. You will do a big practical project where you go through all the steps: collecting data, cleaning it, building a classifier, testing it, etc.

### Topic 1.2: What this class is NOT
- It is **not** a deep‑learning‑only class (though you will learn some neural networks at the end).  
- It is **not** an advanced statistics class.  
- It is a **basic introduction** – perfect for a complete beginner like you.

### Topic 1.3: How the class is organised (just so you know)
- **Lectures** (2 hours every week) – you get slides and videos.  
- **Exercise class (UE)** – you work in groups of 2 on a real project.  
- **Exam** – multiple‑choice, written, closed book. You need to register early because seats are limited.  
- **Grading**: from 100% down to 50% for a pass, with grades like “Sehr Gut” (very good) down to “Nicht Genügend” (fail).

> **Real‑life connection** – Think of this class like learning to cook. The lecture gives you recipes (theory). The UE is actually cooking a meal (practice). The exam checks if you know why the recipes work.

---

## Part 2: Why “fish”? – The sorting machine problem (Slides 10–14)

### Topic 2.1: The problem we want to solve
A fish factory has a conveyor belt with two kinds of fish: **sea bass** and **salmon**. They want an **automatic sorting machine** that uses a camera to look at each fish and decide: “This is a sea bass” or “This is a salmon”.

**Why is this hard?**  
Fish can look similar. They may be different sizes, or rotated, or poorly lit. A human can do it easily, but we want a machine to do it fast and without getting tired.

### Topic 2.2: How to build a classifier using machine learning (slide 13)
We don’t write “if‑then” rules by hand. Instead, we **teach** the computer:

1. **Collect training examples** – catch many sea bass and many salmon, take pictures.  
2. **Label them** – ask fish experts to mark each picture as “bass” or “salmon”.  
3. **Extract features** – instead of giving the whole picture, we measure simple numbers like **length**, **lightness** (how dark or light the fish is), **width**, etc.  
4. **Train a classifier** – the computer looks at the features and the labels, and learns a decision rule.  
5. **Test** – try the rule on new fish (not used during training) to see how accurate it is.  
6. **Deploy** – if good enough, put it on the conveyor belt.

> **Simple analogy** – Teaching a child to recognise apples vs oranges:  
> Show them many apples and oranges, point to colour and shape (“features”), then let them guess on new fruit.

### Topic 2.3: The three main steps (slide 14)
1. **Preprocessing** – clean the image, separate each fish from the background and from other fish.  
2. **Feature extraction** – measure numbers: length = 23 cm, lightness = 0.7 (0 = black, 1 = white), etc.  
3. **Classification** – use those numbers to decide the fish type.

Machine learning lives in step 3, but step 2 (choosing good features) is also very important.

---

## Part 3: Trying to classify with only one feature (Slides 15–18)

### Topic 3.1: Using “length” as the only clue (slide 15)
Imagine we only measure the **length** of each fish. We plot two histograms (bar charts):
- One histogram shows how many sea bass have a certain length.
- Another shows how many salmon have a certain length.

On the slide, you see that both histograms **overlap** – some sea bass are short, some salmon are long. No single length value can perfectly separate them.

### Topic 3.2: The best single threshold (slide 16)
We can still try to find one length value – call it **l*** – and say:  
- If length < l* → classify as sea bass.  
- If length > l* → classify as salmon.

The picture shows that even at the best possible l*, some fish are on the wrong side (errors).  
> **Real‑life example** – Trying to separate men and women by height alone. Many men are short, many women are tall. You will always have errors.

### Topic 3.3: Trying a different feature – “lightness” (slide 18)
Now measure how **light** the fish is (darker vs brighter). The histograms for lightness show **less overlap**. That means lightness is a better feature for this problem – but still not perfect.

**Lesson:** Choosing the right features is critical. A bad feature (like length) gives poor separation. A good feature (like lightness) gives better separation.

---

## Part 4: Decision boundaries and misclassification costs (Slides 19–20)

### Topic 4.1: What is a decision boundary?
When you have one feature (like lightness), your decision rule is a single number (a **threshold**). On a number line, that threshold is a point – we call it a **decision boundary**.  
When you have two features, the boundary becomes a line (or a curve) in a 2D plane.

### Topic 4.2: Not all errors cost the same (slide 19–20)
In the fish factory, suppose:
- Mistaking a sea bass for a salmon is **very expensive** – maybe the factory will lose a big customer because salmon is more valuable.
- Mistaking a salmon for a sea bass is cheaper – you just put a cheap fish in an expensive box.

If the cost is different, you should move the decision boundary. For example, to avoid costly mistakes (bass → salmon), you shift the boundary **left** (towards the “bass” side). Then you will classify more fish as salmon, even if some are actually bass, because the expensive error is reduced.

> **Simple analogy** – Airport security: They would rather mistakenly stop an innocent person (cheap error) than let a dangerous person through (expensive error). So they set the decision boundary very strict.

This is part of **Decision Theory** – a topic you will learn in Lecture 2.

---

## Part 5: Using two features – vectors and feature space (Slides 21–23)

### Topic 5.1: Representing a fish as a vector (slide 21)
Instead of just one number, we can use **two features** – for example:
- \(x_1\) = lightness  
- \(x_2\) = width

We write the fish as a **vector** (a list of numbers in a column):

\[
x = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix}
\]

Example: a fish with lightness 0.6 and width 5.2 cm is written as \(x = \begin{pmatrix} 0.6 \\ 5.2 \end{pmatrix}\).

### Topic 5.2: Feature space – a 2D playground (slide 21)
Imagine a graph:
- Horizontal axis = lightness (\(x_1\))
- Vertical axis = width (\(x_2\))

Every fish becomes a **point** in this 2D space. That space is called the **feature space**. In general, if you have \(d\) features, it’s a \(d\)-dimensional space (hard to draw, but the idea is the same).

### Topic 5.3: Decision boundaries in 2D (slides 22–23)
**Slide 22** shows a **straight line** (linear boundary) that tries to separate bass points from salmon points. Some points are on the wrong side – those are the errors.

**Slide 23** shows a **complex, wiggly boundary** that separates all training points perfectly – zero errors on the training data.

**But is that good?** Not necessarily. Let’s see why.

---

## Part 6: Overfitting, generalisation, and the design cycle (Slides 24–28)

### Topic 6.1: The real goal – generalisation (slide 24)
The purpose of learning is **not** to memorise the training examples. It is to classify **new, unseen fish** correctly. This ability is called **generalisation**.

If you draw a very wiggly boundary that perfectly separates every training fish, you might have “learned” random noise, outliers, or measurement errors. Then when a new fish comes that is slightly different, your boundary will fail.

> **Real‑life example** – A student memorises all the answers to the homework problems. Then on the exam (new problems), the student does poorly. Memorisation ≠ learning.

### Topic 6.2: Overfitting and model selection (slide 25)
**Overfitting** = making your model too complex, so it fits the training data perfectly but generalises badly.  
**Underfitting** = making your model too simple, so it cannot capture the real pattern.

The slide shows three models (simple, medium, complex). Which one do we trust most? Usually the **medium** one – not too simple, not too complex. But how do we know? There is no mathematical formula. You must use **experimental evaluation** (testing on separate data). That is a big part of this class.

### Topic 6.3: Different ways to build a classifier (slide 26)
- **Rule‑based systems** – a human writes “if length > 30 cm then salmon”. Works only for very simple problems.  
- **Classical machine learning** – human designs features (lightness, width), then a computer learns the classifier from examples.  
- **Representation learning** – the computer also learns which features are useful (often without labels first).  
- **Deep learning** – a stack of layers that learn everything from raw input (e.g., pixels) – features and classifier together (“end‑to‑end”).

You will learn more about deep learning in Lectures 8–10.

### Topic 6.4: The complete design cycle (slide 27)
Here is the loop you will follow in your project:

1. **Data acquisition** – collect examples, label them correctly.  
2. **Feature extraction** – turn raw data (images) into numbers.  
3. **Model training** – run a learning algorithm to get a classifier.  
4. **Evaluation** – test on new data, measure accuracy, find errors.  
5. **Go back** – improve features, try another model, clean the data, etc.

Each step matters. Many beginners think only step 3 is important – that is wrong.

### Topic 6.5: A classifier is just a function (slide 28)
A classifier takes a fish’s features (e.g., lightness = 0.6, width = 5.2) and returns a class label (“bass” or “salmon”). In math terms, it is a **function** that maps input to output. Even huge systems like GPT (which generates text) can be seen as a very big classifier – they predict the next word.

### Topic 6.6: What’s next? (slides 29–30)
The remaining lectures will teach you:
- Bayesian Decision Theory
- Density estimation (parametric & non‑parametric)
- Overfitting, evaluation, model selection
- Specific algorithms (k‑NN, neural networks, etc.)
- Unsupervised learning (clustering)

You do not need to buy the books, but the list on slide 30 (Duda, Bishop, Hastie, Murphy, Russell & Norvig) are excellent references if you want to go deeper.

---

## Final check – can you answer these simple questions?

1. What is the difference between **supervised** and **unsupervised** learning? (Hint: supervised uses labels.)  
2. Give an example of a **feature** for the fish problem. Why is it called a “feature”?  
3. What is **overfitting**? Draw a picture in your mind of a very wiggly decision boundary.  
4. If misclassifying a salmon as a sea bass is 10 times more costly than the opposite, how would you move the decision boundary?  
5. What are the three main steps in a classification pipeline (slide 14)?

If you can answer these, you have mastered Chapter 1! Move to Chapter 2 when you are ready.
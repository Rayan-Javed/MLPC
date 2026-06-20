# Part 1
## 1. Bernoulli distribution

**What is it?**  
A Bernoulli distribution is a way to describe something that has only **two possible outcomes**:

- Success (1) – e.g., heads, spam, salmon
    
- Failure (0) – e.g., tails, not spam, bass
    

Each outcome has a probability:

- P(success)=θ (theta, a number between 0 and 1)
    
- P(failure)=1−θ
    

**Example:** Tossing a coin.  
If the coin is fair, θ=0.5  
If the coin is biased towards heads, θ=0.7

**Real life:**

- Fish: medium = success, large = failure (if we define medium as “success”).
    
- Email: spam = success, ham = failure.
    

---

## 2. i.i.d. (Independent and Identically Distributed)

**What does it mean?**

- **Independent:** The outcome of one toss does not affect the next.
    
- **Identically distributed:** Every toss uses the **same** probability θ.
    

**Example:** You toss the same coin 10 times. Each toss is independent (no memory), and each toss has the same θ. That’s i.i.d.

**Real life:**

- Catching fish from a large lake: each fish’s size is independent of the previous one, and all come from the same population (same priors, same likelihoods).
    
- But if you catch fish without replacing, they are not independent (because removing one changes the lake). So i.i.d. is an assumption we often make to simplify math.
    

---

## 3. Likelihood (reminder) and MLE

**Likelihood** L(θ) = probability of seeing the **observed data** given a particular θ.

**MLE** = **Maximum Likelihood Estimation**  
It answers: _What value of θ makes the observed data most probable?_

**Example:** You toss a coin 5 times and get: H, H, T, H, T.  
What θ (probability of heads) makes this exact sequence most likely?  
MLE finds that θ.

---

## 4. Log likelihood

![[Pasted image 20260521070915.png]]

---

## 5. How to find MLE – step by step

![[Pasted image 20260521070837.png]]

So MLE says: the best estimate of heads probability is **0.6** (3 heads out of 5).

**That matches your intuition:** MLE = number of successes / total trials.

---

## 6. Connection to your fish example

Suppose you want to estimate P(medium∣salmon)P(medium∣salmon) from data.  
You catch 100 salmon, count how many are medium.  
Each salmon is a Bernoulli trial (medium=1, large=0).  
MLE = (# medium salmon) / (total salmon).  
That’s exactly the likelihood you used earlier (0.67).

So **MLE** is how you learn the likelihoods from data, instead of being given them.

---


## 7. Summary for a child

- **Bernoulli** = a yes/no experiment (like coin toss).
    
- **i.i.d.** = each toss is separate and uses same coin.
    
- **Likelihood** = chance of seeing your data for a given coin bias, how probable is my data if the rule is this?
    
- **Log likelihood** = turning product into sum (easier math).
    
- **MLE** = finding the bias that makes your data most likely, the best guess for the unknown rule of your magic bag.
    
- **Formula** for MLE in Bernoulli = (# successes) / (# trials).
    

Now you know how to learn probabilities from data!

---
---
# Part 2
![[Pasted image 20260521154940.png]]![[Pasted image 20260521154945.png]]
## What is a normal distribution (Gaussian)?

A **normal distribution** is a **bell-shaped curve**.  
It describes many things in nature:

- Heights of people
    
- Lengths of fish
    
- Test scores in a big class
    

Most values are near the middle, and fewer values are far away.

The curve has two important numbers:

- **Mean (μ)** = the center (where the hump is)
    
- **Standard deviation (σ)** = how spread out the curve is (small σ = skinny curve, large σ = wide curve)
    

**Real life:**  
Heights of 10-year-old boys: mean = 138 cm, standard deviation = 7 cm.  
Most boys are between 131 cm and 145 cm (mean ± 1σ).

---

## The problem: We don’t know the true mean and standard deviation

You have **measured the lengths of 50 salmon**.  
You believe length follows a normal distribution, but you **don’t know** the true mean and true standard deviation.  
You want to **estimate** them from your 50 measurements.

---

## Intuition (common sense)

- What would you guess for the **mean**?  
    → The **average** of the 50 lengths. Add them up, divide by 50.
    
- What would you guess for the **variance** (how spread out)?  
    → The **average squared distance** from the mean.  
    For each fish, compute (length − mean)², add them up, divide by 50.
    

**That’s exactly what Maximum Likelihood gives you.**

![[Pasted image 20260521155151.png]]

## Real life example (not fish)

You measure the **heights of 10 adult women** in a small town.  
You get: 160, 162, 165, 158, 170, 163, 167, 161, 164, 166 cm.

- Mean = add all ÷ 10 = (sum = 1636) ÷ 10 = **163.6 cm**
    
- Variance = average squared distance from mean:  
    Compute (160-163.6)² = 12.96, (162-163.6)² = 2.56, ... add them all, divide by 10.  
    Suppose the sum of squares = 100.4, then variance = 10.04, standard deviation ≈ 3.17 cm.
    

So you estimate: women’s height ~ normal with mean 163.6 cm, std dev 3.17 cm.

## Why is this useful?

Now you can answer questions like:  
“What’s the probability a random woman is taller than 170 cm?”  
You just plug the estimated mean and std dev into the normal formula.

And this is how machine learning learns the **likelihood** for a feature (like length) for each class (bass, salmon). You collect training data, compute mean and variance for each class separately, and you have your Gaussian class‑conditional probability.

---

## Summary (for a child)

- **Normal distribution** = bell curve (heights, fish lengths).
    
- **Mean** = average = sum ÷ number of fish.
    
- **Standard deviation** = how spread out = square root of (average squared distance from mean).
    
- **Maximum Likelihood** just gives you those simple formulas.
    
- **Real life**: measure 50 salmon, get average length and spread, now you can predict the chance of a new salmon being any size.

Let me explain **multivariate normal** (multiple features together) in super easy words, with real life examples.

---

## What is “multivariate”?

**Univariate** = one feature (e.g., only length of fish).  
**Multivariate** = two or more features together (e.g., length **and** weight **and** colour).

We still assume the features follow a **normal (bell‑shaped) distribution**, but now it’s a **joint** distribution – like a 2D bell curve (looks like a mountain).

---

## The two features in our example

For salmon, we measure:  
- **Lightness** (\(x_1\)) – how pale or dark the fish is.  
- **Width** (\(x_2\)) – how wide the fish is.

We believe these two numbers together follow a **multivariate normal** distribution for salmon.

---

## What we need to estimate from training data (50 salmon)

We need two things:

### 1. Mean vector \(μ\)
This is just **the average of each feature** for salmon.

- Average lightness of the 50 salmon = e.g., 0.7 (on a scale from 0 to 1).  
- Average width of the 50 salmon = e.g., 5.2 cm.

So the mean vector is:

μ=[0.7,5.2]

**Intuition:** It’s the “center” of the salmon cloud in the two‑dimensional space.

---

### 2. Covariance matrix (\(Σ\))

This is a small table (2×2) that tells us three things:

|                  | Lightness | Width |
|------------------|-----------|-------|
| **Lightness**    | variance of lightness | how lightness and width move together |
| **Width**        | same number (symmetric) | variance of width |

- **Variance of lightness:** how spread out are the lightness values among salmon? If all salmon are nearly the same colour, variance is small. If some are very pale and some very dark, variance is large.

- **Variance of width:** how spread out are the widths? If all salmon are similar width, small variance; if some are skinny and some fat, large variance.

- **Covariance (off‑diagonal):** tells us **how lightness and width change together**.  
  - Positive covariance: lighter salmon tend to be wider (as lightness goes up, width goes up).  
  - Negative covariance: lighter salmon tend to be narrower.  
  - Zero covariance: no relationship.

**Real life:** For salmon, you might find a **positive covariance** – the pale (light) salmon are often the wider ones.

---

## How do we estimate these from data? (Very simple)

### Mean vector:
For each feature (lightness, width), compute the **average** of your 50 salmon.  
That’s the mean vector.

### Covariance matrix:
For each salmon, compute how much it **deviates** from the mean in both features. Then multiply those deviations together (like (deviation in lightness) × (deviation in width)), average over all 50 salmon.  
Do this for:
- Lightness × Lightness → variance of lightness  
- Width × Width → variance of width  
- Lightness × Width → covariance

That’s it. **The formula just does exactly what your intuition says:** average the product of deviations.

---

## Real life example (not fish)

Imagine you measure **height** and **weight** of 10 adult men.

Height (cm): 170, 172, 175, 168, 180, 176, 169, 174, 178, 173  
Weight (kg): 65, 68, 72, 63, 78, 74, 66, 70, 76, 69

- **Mean vector** = (average height, average weight).  
  Average height = 173.5 cm, average weight = 70.1 kg.

- **Covariance matrix** tells you:  
  - Variance of height (how spread out heights are)  
  - Variance of weight (how spread out weights are)  
  - Covariance: taller men tend to weigh more (positive covariance) – that’s expected.

If covariance is **positive**, it means the two features move in the same direction (taller = heavier).  
If it were negative, taller would mean lighter (unusual).  
If zero, no relationship.

---

## Why is this useful?

Once you estimate the mean vector and covariance matrix for salmon (and separately for bass), you can:

- Compute the **likelihood** of a new fish (with lightness and width) being a salmon vs. bass.  
- Draw **decision boundaries** – in two dimensions, they can be straight lines or curves (ellipses).  
- Build a **classifier** that looks at both features together, not just one.

This is much more powerful than using only length.

---

## Summary (for a child)

- **Multivariate normal** = bell shape in 2D (or more dimensions).  
- **Mean vector** = average of each feature (like average height and average weight).  
- **Covariance matrix** = tells how spread out each feature is, and how they move together (e.g., taller = heavier).  
- **Estimation** = just average the numbers from your training data.  
- **Real life:** Height and weight are positively correlated. That “positive correlation” is captured by the covariance.

Now you know how to learn a **multivariate** model from data, not just a single feature!

Let me teach you **Topic 4** in super easy words, like you’re a child, with real‑life examples.

---

## What is a Single‑Gaussian Bayes Classifier?

It’s a **simple way to teach a computer how to classify things** (like fish, fruits, or emails) using **bell‑shaped curves** (Gaussians) for each class.

We call it our “first real learning algorithm” because:
- It actually **learns** from training data (it doesn’t just guess).
- It uses **probability** to make decisions.
- It’s the foundation for many fancier methods.

---

## Step 1: What we learn from training data (the “learning” part)

You give the computer a **training set** – many examples of fish where you already know if it’s bass or salmon.  
For each fish you record features (e.g., lightness and width).

The computer calculates **three things** for each class (bass and salmon):

### 1. Prior \( \hat{P}(\omega_i) \)
That’s just **how common each fish is** in the training set.  
*Example:* If 400 out of 1000 fish are bass, then \( \hat{P}(\text{bass}) = 0.4 \).  
Simple: count and divide.

### 2. Mean vector \( \hat{\mu}_i \)
For each class, take **average lightness** and **average width** of those fish.  
*Example:* For salmon, average lightness = 0.7, average width = 5.2 cm.  
That gives a “center point” for the salmon cloud.

### 3. Covariance matrix \( \hat{\Sigma}_i \)
This tells **how spread out** the fish are and **how features move together** (e.g., lighter salmon tend to be wider).  
We estimate it by averaging the products of deviations (as you saw in Topic 3).

So after training, the computer has a **bell‑shaped description** for each class: “Salmon look like this on average, with this much spread and correlation.”

---

## Step 2: How to classify a new fish (the “prediction” part)

A new fish comes with features \( x = (\text{lightness}=0.65, \text{width}=5.0) \).  
The computer does this:

### For each class (bass and salmon):
- It plugs \( x \) into the **Gaussian formula** using that class’s estimated mean and covariance.  
  This gives \( p(x \mid \text{class}) \) – the likelihood of seeing that fish if it were that class.
- It multiplies by the **prior** \( P(\text{class}) \) to get the **numerator** of the posterior.
- It divides by the **evidence** (the sum of both numerators) to get the **posterior probability**  
  \( P(\text{class} \mid x) \).

### Then it picks the class with the **largest posterior** (if using zero‑one loss, i.e., all mistakes equal).

That’s it. That’s the classifier.

---

## A real‑life example (fruit instead of fish)

Imagine you have two fruit classes: **apple** and **orange**.  
Features: sweetness (1‑10) and colour (1=green, 10=orange).

Training data gives:
- Apples: mean sweetness = 6, mean colour = 3 (greenish); small spread.
- Oranges: mean sweetness = 7, mean colour = 9 (orange); larger spread.

New fruit: sweetness = 6.5, colour = 8.  
The Gaussian for oranges might give a higher likelihood (because colour 8 is very orange). Multiply by prior (say 50‑50), compute posterior.  
If posterior(orange) > posterior(apple), classify as orange.

---

## Advantages (why this is cool)

- **Simple:** Just compute averages and spreads from data.
- **Fast to train:** Even with thousands of fish, it’s just a few maths operations.
- **Interpretable:** You can look at the mean and covariance and understand the “typical” fish of each class.
- **Gives probabilities:** Not just a yes/no answer, but “70% chance salmon, 30% chance bass”.

---

## Disadvantages (when it fails)

- **Real data is rarely one perfect bell curve.**  
  Example: Salmon might come in two distinct sizes – small young salmon and large adult salmon. That’s **two peaks**, not one. A single Gaussian would fail.
- **Many parameters:** If you have 100 features (e.g., 100 pixel values), the covariance matrix has about 5,050 numbers. You need a **lot** of training data to estimate those reliably.
- **Assumes Gaussian shape.** If the true shape is different (e.g., very skewed), the classifier may do poorly.

---

## A picture to remember

Imagine two ellipses (fuzzy clouds) in 2D – one for bass, one for salmon.  
The **decision boundary** is the line (or curve) where the two ellipses are equally likely.  
The Single‑Gaussian Bayes classifier draws that boundary based on the estimated means and covariances.  
If the ellipses are circular and same size, the boundary is a straight line. If one is long and skinny, the boundary becomes a curve.

---

## Summary for a child

- **Training** = learn the average, spread, and shape of each class (like drawing a fuzzy cloud around all bass, and another around all salmon).
- **Prediction** = put the new fish on the map, see which cloud it’s more likely to belong to, and pick that class.
- **Good because** it’s simple, fast, and gives probabilities.
- **Bad because** real data isn’t always a single bell‑shaped cloud, and too many features need too much data.

Now you have your **first real machine learning algorithm**!

# Part 3

## Topic 1: The problem with a single Gaussian – “Multimodal” data

### The shape of a Gaussian (bell curve)

A Gaussian has **one peak** (one “mode”). It rises smoothly, then falls.  
Example: people’s **height** in a single gender – one peak around the average. That’s **unimodal**.

### But what if your data has two peaks?

Imagine you collect **salmon** from two different rivers:

- River A salmon are small and dark (average length 40 cm, lightness 0.3)
    
- River B salmon are large and light (average length 70 cm, lightness 0.8)
    

If you mix them, the overall distribution of salmon length is **bimodal** – two peaks.  
If you force a single Gaussian to fit this data, the best fit will put its peak **between** the two groups, and it will be very wide. That bell curve will not represent either group well. It will give **low density** at the actual peaks and **high density** in the gap – completely wrong.

### Why this matters for classification

If you model salmon as one Gaussian, a new salmon from River A (small and dark) might be closer to the bass distribution (which might be dark) and get misclassified.  
Your classifier fails because your **model is too simple**.

> **Real‑life analogy:** Trying to describe the heights of **all humans (men + women)** with one bell curve. The curve would peak somewhere between the two genders, but it would poorly represent both men and women. You need **two** bells – one for men, one for women.

### Also: too many parameters

For high‑dimensional data (many features), the covariance matrix has d(d+1)/2d(d+1)/2 parameters.  
If d=100d=100, that’s about 5,050 numbers per class. With 5 classes, that’s 25,250 parameters. You need huge training data to estimate them reliably.  
This is called the **curse of dimensionality** (we’ll see it again later).

![[Pasted image 20260521163826.png]]
### Example (picture in your mind)

Salmon data has two clouds: one small and dark (River A), one large and light (River B).  
A GMM with two components can fit both clouds perfectly.

### But… how do we learn the parameters?

We cannot use the simple ML formulas we derived before, because we don’t know **which sub‑group each training example belongs to**.  
If we knew, we could just average per sub‑group. But we don’t.  
This is a classic **hidden variable** problem. The solution is an algorithm called **EM (Expectation‑Maximisation)** – you will learn it later in the unsupervised learning part of this course (clustering). For now, just know that GMMs exist and can fit complex data.

> EM alternates between guessing which sub‑group each fish belongs to, then re‑estimating the Gaussians, then re‑guessing, until it finds the best fit.

It’s like: “I think this fish might be from River A… now let me recompute the average for River A… oh, now that fish looks more like River B…” – repeating until stable.

## Summary (for a child)

- **GMM** = a mixture of several bell curves for one class.
    
- It can fit **two‑peaked** (bimodal) or even more complex data.
    
- Each bell curve has its own mean, covariance, and a weight.
    
- **Learning** a GMM is harder because we don’t know which fish belongs to which sub‑group.
    
- The **EM algorithm** solves that by guessing and improving iteratively.
    
- GMMs are powerful but we will study them later in unsupervised learning.

Let me teach you **Topic 3: Naïve Bayes** in super easy words, like you’re a child, with real‑life examples.

---

## 1. What’s the problem we’re trying to solve?

We saw that a **full Gaussian** (with covariance) needs a huge number of parameters – especially when we have many features.  
For 100 features, we need about 5,050 numbers **per class**. That’s too many. We need simpler solution.

---

## 2. The “naïve” assumption

**Naïve Bayes** makes a very strong (and often wrong) assumption:  
> “Given the class, all features are independent of each other.”

That means: if you know a fish is salmon, then knowing its lightness tells you **nothing** about its width. No correlation.

![[Pasted image 20260521165014.png]]

**In simple words:**  
To know the chance of a salmon having a certain lightness **and** width, just multiply the chance of that lightness (alone) by the chance of that width (alone).

---

## 3. Why is this “naïve”?

Because in real life, features **are** often correlated.  
- Longer salmon tend to be wider.  
- Heavier people tend to be taller.  

Naïve Bayes ignores that. It acts as if features know nothing about each other.  
That’s why we call it **naïve** – it’s a bit too simple, even childishly simple.

---

## 4. But why does it work so well anyway?

Even though the assumption is often wrong, Naïve Bayes can still make **correct classifications** surprisingly often. Why?

- **The decision is about which class has the highest posterior** – not about getting the exact probability.  
  Even if the product is wrong, the **largest** product might still point to the right class.

- **It needs very few parameters:**  
  For each class and each feature, you only need to estimate **one distribution** (e.g., mean and variance for a Gaussian, or a small table for discrete features).  
  With 100 features and 5 classes, that’s about 500 numbers – far smaller than 25,000.

- **It resists overfitting:** Because it ignores correlations, it doesn’t learn random noise patterns that appear in the training data. It’s a simple, robust model.

---

## 5. Real‑life example (spam filter)

Suppose you classify emails as spam or ham (good).  
Features: presence of words “free”, “winner”, “money”.

Naïve Bayes assumes these words are **independent** given the class (spam or ham).  
That’s not true – “free” and “winner” often appear together in spam. But even so, Naïve Bayes spam filters work very well in practice.

---

![[Pasted image 20260521165043.png]]
---

## 7. A child’s analogy

Imagine you have two baskets: “cat” and “dog”.  
Features: “has long tail” and “barks”.

Naïve Bayes says: given it’s a dog, having a long tail and barking are **independent** (knowing about the tail doesn’t change the chance of barking). That’s silly because dogs that bark can have any tail length. But for classification, it might still work: if an animal barks and has a long tail, it’s probably a dog.

---

## 8. Summary (for a child)

- **Naïve Bayes** = assume all features are independent within each class.  
- **Why naïve?** Because real features often are not independent.  
- **Why good?** Needs few numbers from data, resists overfitting, often works well.  
- **How classify?** Multiply (or add logs of) feature probabilities for each class, pick largest.  
- **Real life:** Spam filters, text classification, medical diagnosis with few features.

Now you know a simple, powerful classifier that even a child can understand!

Let me teach you **Topic 4: Document classification with Naïve Bayes** in super easy words, like you’re a child, with real‑life examples.

---

## 1. The problem we want to solve

You have a pile of **news articles**. Each article is already labelled with a category, for example:

- Politics (e.g., elections, laws)  
- Sports (e.g., football, basketball)  
- Entertainment (e.g., movies, music)

You get a **new article** (no label) and you want the computer to guess which category it belongs to.  
This is called **document classification**.

**Real life:** Spam filters, news website recommenders, email sorting.

---

## 2. How do we turn an article into numbers for the computer?

Computers don’t understand words directly. We need to make a **feature vector** (a list of numbers) from the article.

**Common way:** Make a big dictionary of the most common words in the language – say the top 50,000 words like “the”, “and”, “party”, “game”, “movie”, “score”, “government”.

Then for each article, we create a **binary vector** (a list of 0s and 1s) of length 50,000:

- \(x_j = 1\) if the **j‑th word** in the dictionary appears in the article.
- \(x_j = 0\) if it does not appear.

**Example:**  
If the dictionary starts with: “the”, “a”, “game”, “party”, “election”, …  
And the article says: “The game was exciting.”  
Then the vector might be: [1 (the), 0 (a), 1 (game), 0 (party), 0 (election), …] – mostly zeros.

This is called a **bag‑of‑words** model – we ignore the order of words, just whether they appear.

---

## 3. Why can’t we use a full Gaussian (with covariance) for this?

A full Gaussian would need a **covariance matrix** for each category.  
For 50,000 features (words), the covariance matrix would be **50,000 × 50,000** – that’s **2.5 billion numbers** per category!  
That’s impossible – you would need more training articles than there are atoms in the universe.  
Also, most words never appear together in the same article, so estimating correlations is hopeless.

**So full Gaussian fails completely.**

---

## 4. Why Naïve Bayes works for documents

Naïve Bayes makes the **naïve assumption** that, given the category (e.g., Sports), the presence of each word is **independent** of the others.

This is **false** in real life – in a Sports article, the words “football” and “goal” often appear together.  
But it works anyway because:

- **Many weak pieces of evidence add up** – a single word might be weak, but hundreds of words together point strongly to a category.
- **The assumption simplifies the math** – we don’t need covariances. We only need to estimate, for each category and each word, the probability that the word appears in an article of that category.
- **Even if the probabilities are not perfectly accurate, the **ranking** of categories (which one is most likely) is often still correct.**

**Real‑life example:** A spam email with words “free”, “prize”, “click”, “winner” – even if those words are not truly independent, the product of their probabilities will be much higher for spam than for ham.

---

![[Pasted image 20260522000248.png]]


---

![[Pasted image 20260522000214.png]]

---

## 7. Real‑life application: Spam filter

Spam filters use exactly this idea:

- Two classes: **Spam** and **Ham** (good email).
- Features = words in the email (e.g., “free”, “prize”, “click”, “money”).
- Training: collect many spam and ham emails, count word frequencies.
- Classification: for a new email, compute log probability for spam and for ham; if spam score > ham score, put it in spam folder.

Naïve Bayes spam filters work surprisingly well even though words like “free” and “winner” are not independent.

---

## 8. Summary (for a child)

- **Document classification** = sorting news articles into categories like Sports, Politics.
- **Feature vector** = a long list of 0/1 telling which words appear in the article.
- **Full Gaussian** fails because it would need billions of numbers.
- **Naïve Bayes** assumes all words are independent given the category – a silly assumption but it works well in practice.
- **Training** = count for each category how often each word appears, and the prior (how common each category is).
- **Classification** = multiply (or add logs of) the word probabilities, pick the category with the highest score.
- **Real life** = spam filters, news recommendations, email sorting.

Now you know how a simple probability model can read and classify text!

## Topic 5: Advantages and disadvantages of Naïve Bayes (summary)

|**Advantages**|**Disadvantages**|
|---|---|
|Very fast to train and classify|Assumes feature independence – rarely true in reality|
|Needs very few parameters|Can give poor probability estimates (but classification may still be good)|
|Works well with high‑dimensional data (e.g., text)|Decision boundaries are simple (linear in many cases) – cannot model complex interactions|
|Resists overfitting|If a feature is strongly correlated with another, the product overcounts evidence|
# Part 4


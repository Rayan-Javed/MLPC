# Fish Example
## Step 1: What are we trying to do?

We catch a fish. We only see its **length** (medium or large).  
We want to guess if it’s **bass** or **salmon**.

Real life example:  
You’re fishing. You pull up a fish. It looks medium-sized. Is it a bass or a salmon? You can’t see clearly, so you use math to help you guess.

---

## Step 2: What is “prior probability”?

**Prior** means: before you see the fish’s size, how likely is each type?

In our example:

- Half the fish in the lake are bass, half are salmon.  
    So P(bass)=0.5P(bass)=0.5, P(salmon)=0.5P(salmon)=0.5.
    

Real life:  
Imagine a lake with 100 fish: 50 bass, 50 salmon. If you close your eyes and grab one, chance of bass = 50 out of 100 = 0.5.

---

## Step 3: What is “likelihood”?

**Likelihood** answers: If I know it’s a certain fish, how often is it medium or large?

We have these numbers (from counting many fish):

- For salmon:  
    P(medium∣salmon)=0.67 (67 out of 100 salmon are medium)  
    P(large∣salmon)=0.33
    
- For bass:  
    P(medium∣bass)=0.33 (33 out of 100 bass are medium)  
    P(large∣bass)=0.67
    

Real life:  
You go to a fish farm. You look at 100 salmon: 67 are medium, 33 are large. You look at 100 bass: 33 are medium, 67 are large.

---

## Step 4: We catch a medium fish. What is the “evidence”?

**Evidence** = total chance of catching a medium fish, no matter what type.

We calculate it like this:

> Chance of medium =  
> (chance it’s bass) × (chance bass is medium) +  
> (chance it’s salmon) × (chance salmon is medium)

Put numbers:  
(0.5×0.33)+(0.5×0.67)=0.165+0.335=0.5

So P(medium)=0.5
That means half the fish in the lake are medium.

Real life:  
Out of 100 fish (50 bass + 50 salmon):

- Medium bass = 50 × 0.33 = 16.5
    
- Medium salmon = 50 × 0.67 = 33.5  
    Total medium = 16.5 + 33.5 = 50 out of 100 = 0.5.
    

---

## Step 5: What is “posterior probability”?

**Posterior** = after seeing the fish is medium, what’s the chance it’s bass? What’s the chance it’s salmon?

We use Bayes’ rule:

P(bass∣medium)=P(medium∣bass)×P(bass)P(medium)

Put numbers:  
=0.33×0.50.5=0.1650.5=0.33=0.5

For salmon:  
P(salmon∣medium)=0.67×0.50.5=0.67

So:

- After seeing “medium”, chance it’s bass = 0.33 (33%)
    
- Chance it’s salmon = 0.67 (67%)
    

Real life:  
You caught a medium fish. It is more likely to be salmon (67%) than bass (33%) because salmon are more often medium.

---

## Step 6: Making a decision with “MAP” (simple way)

**MAP** = choose the type with the **largest posterior** probability.

Here, salmon has 0.67, bass has 0.33. So MAP says: **guess salmon**.

This is like: “If you want to be right most often, always guess salmon when you see a medium fish.”

Real life:  
You catch 100 medium fish. If you always guess “salmon”, you’ll be right about 67 times, wrong 33 times. That’s the best you can do if all mistakes are equal.

---

## Step 7: What if mistakes have different costs? (General loss)

Now imagine:

- If you guess bass but it’s salmon → customer allergic to salmon → very bad. Cost = 100.
    
- If you guess salmon but it’s bass → no allergy, just different fish → small problem. Cost = 1.
    

We don’t just care about being right most often. We care about **avoiding very costly mistakes**.

We calculate **expected cost** for each guess.

---

### Expected cost if you guess “bass”:

Cost =  
(prob it’s bass × cost if correct) + (prob it’s salmon × cost if wrong)

Correct guess (bass) cost = 0.  
Wrong guess (salmon) cost = 100.

So: (0.33×0)+(0.67×100)=0+67=67

---

### Expected cost if you guess “salmon”:

Wrong guess (bass) cost = 1.  
Correct guess (salmon) cost = 0.

So: (0.33×1)+(0.67×0)=0.33+0=0.33

---

### Choose the guess with smaller expected cost

Guess bass → cost 67  
Guess salmon → cost 0.33

0.33 is smaller, so we still guess salmon. That’s the same as MAP here.

---

## Step 8: Example where general loss changes the decision

Let’s change costs:

- Mistake: guess bass, true salmon → cost = 10 (mild allergy)
    
- Mistake: guess salmon, true bass → cost = 50 (wasting expensive bass)
    

Same posteriors: bass 0.33, salmon 0.67.

Expected cost for “guess bass”:  
(0.33×0)+(0.67×10)=6.7

Expected cost for “guess salmon”:  
(0.33×50)+(0.67×0)=16.5

Now guess bass (6.7) is better than guess salmon (16.5).  
So even though salmon is more likely, we choose **bass** because the cost of being wrong about bass is huge (50).

Real life:  
If wasting a bass ruins your expensive recipe, you’d rather risk a small allergy problem (cost 10) than lose a bass (cost 50). So you guess bass even though it’s less likely.

---

## Summary in very simple words

1. **Prior** = guess before seeing size (half bass, half salmon).
    
2. **Likelihood** = how often each fish is medium or large (from counting).
    
3. **Evidence** = total chance of medium fish (calculated from prior + likelihood).
    
4. **Posterior** = chance of each fish after seeing medium (bass 33%, salmon 67%).
    
5. **MAP** = pick the fish with highest posterior (salmon) – best for being right most often.
    
6. **General loss** = different mistakes have different costs – pick the fish that gives smallest expected cost, which may not be the most likely one.
    

You now know how to go from simple probability to smart decision making!

------
---
---
# Unknown Terms

![[Two‑class case with general loss.png]]
![[Pasted image 20260521060539.png|697]]
![[Pasted image 20260521060603.png]]
![[Pasted image 20260521060725.png]]
## 7. Real-life interpretation (child-friendly)

Imagine you have a scale:

- Left pan = how many times salmon are more likely to be this size.
    
- Right pan = a number you set based on:
    
    - How common bass are vs. salmon (priors)
        
    - How bad it is to mistake bass for salmon vs. salmon for bass (costs)
        

If the left pan is lighter (smaller number) → guess bass.  
If heavier → guess salmon.

So the **likelihood ratio** is like the “evidence from the fish size”.  
The threshold is your **personal caution level** depending on how much you want to avoid one mistake over another.

![[Pasted image 20260521060819.png]]
## Summary (for a child)

- **Likelihood ratio** = how many times more likely one fish type is to have that size than the other.
    
- **Threshold** = a number that depends on how common each fish is and how bad each mistake is.
    
- Decision: if likelihood ratio is below threshold → guess bass; else guess salmon.
    
- This is just another way of doing the same “minimize risk” rule, but it helps you see the importance of the evidence from the data.

-----
---
---
# Basic Concepts
## 1. Decision / classification as a probabilistic inference task

**What does it mean?**  
When you have to decide between two or more classes (e.g., bass vs. salmon, healthy vs. sick, spam vs. not spam), you rarely have perfect information. You observe some **features** (length, weight, pixel values, words in an email).  
Because the world is noisy, you cannot be 100% sure. So you treat the problem as **probabilistic inference**: you compute how likely each class is **given the data**, then choose the best one.

**Real life example**

- Doctor: sees your symptoms (cough, fever). Not 100% sure if it’s flu or cold. Uses probability to make a decision.
    
- Email filter: sees words “free”, “winner”. Computes probability it’s spam.
    
**Key idea:** Classification = using data to update your beliefs about which class is true.

![[Pasted image 20260521061155.png]]
![[Pasted image 20260521061220.png]]
![[Pasted image 20260521061310.png]]
![[Pasted image 20260521061342.png]]
![[Pasted image 20260521061407.png]]
## 8. Connecting everything together

Let me tie all the concepts into one coherent picture:

1. **Probabilistic inference** is the foundation: we treat classification as updating probabilities using data.
    
2. **Bayes’ rule** gives us the posterior probabilities from prior and likelihoods.
    
3. **Loss and risk** allow us to incorporate different costs for different mistakes.
    
4. **The optimal Bayes decision rule** minimises expected loss (risk).
    
5. **Minimum error classification** is a special case with zero‑one loss → MAP.
    
6. **Likelihood ratio** simplifies the decision rule to comparing evidence to a threshold.
    
7. **Decision regions and boundaries** are the set of data points leading to each decision; the boundary is where LR equals threshold.
    
8. For **Gaussian class‑conditional densities**, the decision boundary can be computed in closed form (linear or quadratic), which is why many real‑world classifiers assume normality.
    

**Final real‑life story (spam filter):**

- Prior: 80% ham, 20% spam (from historical data).
    
- Likelihood: for each word, how often it appears in spam vs. ham (learned from emails).
    
- Loss: marking ham as spam costs 10, marking spam as ham costs 1.
    
- Compute likelihood ratio for the entire email (product of word probabilities).
    
- Compare to a threshold derived from prior and losses.
    
- If LR < threshold → classify as ham; else spam.
    
- The decision boundary in word‑space is complex, but if we assume Gaussian distributions for word counts, the boundary becomes simple (e.g., linear in the log‑odds).
    
- In practice, we use machine learning to estimate these distributions from thousands of emails.


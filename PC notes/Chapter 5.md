# Part 2

## Entropy

![[Pasted image 20260525173419.png]]

 Why do we care about entropy?

Because in **decision trees** (like ID3 algorithm), entropy is used to decide **which feature to split on first**.

You look at each feature (e.g., Outlook = Sunny, Overcast, Rainy).  
You compute how much **entropy decreases** after splitting on that feature.  
The feature that gives the biggest drop in entropy (most “information gain”) is chosen for the split.

**In simple words:**

> Entropy tells you how messy your data is. You want to make it less messy (lower entropy) as you build the tree.

- **Entropy** = a number that measures how mixed up your data is.
    
- Low entropy (0) = all the same class.
    
- High entropy (1) = two classes are half‑and‑half.
    
- Used in decision trees to choose the best question to ask.
    
- You don’t need to memorise the formula – just remember the idea of “mixed‑up‑ness”.


## Information Gain

Low entropy = clean / pure. High entropy = messy / mixed.
Information Gain = how much the mix‑up (entropy) goes down after you ask a question.
You want to **pick the question that gives the highest Information Gain** – the one that cleans up the mix‑up the most.
You always ask the question that gives the biggest drop in mix‑up (entropy) first.
You split the data into groups based on the answer.
### What if a group is not pure?

Then you **repeat** the same process on that group only:

- Compute entropy for that group.
    
- Among remaining features (not used yet in that branch), pick the one with highest gain.
    
- Split again.
    
- Keep going until all groups are pure or no features left.
    

That’s the **ID3 algorithm**:

> 1. Start with all data.
>     
> 2. If pure → stop (leaf).
>     
> 3. Else, choose feature with highest Information Gain.
>     
> 4. Split on that feature.
>     
> 5. For each branch, go back to step 2.
## Full Example

Perfect. Let’s build the **full tennis tree** together, **very slowly**, one tiny step at a time. We’ll use the actual 14‑day data, but I’ll explain everything in simple words without heavy math.

---

### First, here is the data (14 days)

Each day has weather and whether you played tennis.

| Day | Outlook    | Temperature | Humidity | Wind   | Play? |
|-----|------------|-------------|----------|--------|-------|
| 1   | Sunny      | Hot         | High     | Weak   | No    |
| 2   | Sunny      | Hot         | High     | Strong | No    |
| 3   | Overcast   | Hot         | High     | Weak   | Yes   |
| 4   | Rainy      | Mild        | High     | Weak   | Yes   |
| 5   | Rainy      | Cool        | Normal   | Weak   | Yes   |
| 6   | Rainy      | Cool        | Normal   | Strong | No    |
| 7   | Overcast   | Cool        | Normal   | Strong | Yes   |
| 8   | Sunny      | Mild        | High     | Weak   | No    |
| 9   | Sunny      | Cool        | Normal   | Weak   | Yes   |
| 10  | Rainy      | Mild        | Normal   | Weak   | Yes   |
| 11  | Sunny      | Mild        | Normal   | Strong | Yes   |
| 12  | Overcast   | Mild        | High     | Strong | Yes   |
| 13  | Overcast   | Hot         | Normal   | Weak   | Yes   |
| 14  | Rainy      | Mild        | High     | Strong | No    |

---

### Step 1: How mixed up is the whole set?

Count how many Play = Yes and Play = No.

- Yes: days 3,4,5,7,9,10,11,12,13 → **9 Yes**
- No: days 1,2,6,8,14 → **5 No**

It’s **not pure** (not all Yes). It’s **not 50/50** (9 vs 5).  
Entropy is medium‑high: about **0.94** (you don’t need to calculate, just know it’s mixed).

---

### Step 2: Which question (feature) should we ask first?

We have 4 features: Outlook, Temperature, Humidity, Wind.  
We compute **Information Gain** for each. That means:  
> If we split on this feature, how much does the mix‑up (entropy) go down?

I’ll give you the gains (you don’t need to calculate them yourself):

- **Outlook** gain = **0.25** (highest)
- Humidity gain = 0.15
- Wind gain = 0.05
- Temperature gain = 0.03

**Highest is Outlook (0.25)**. So the **root question** is: “What is the Outlook?”

---

### Step 3: Split the data by Outlook

Outlook has three values: Sunny, Overcast, Rainy.

### Branch: Outlook = Overcast
Days with Overcast: 3, 7, 12, 13 → all **Yes** (4 Yes, 0 No).  
**Pure** → leaf = **Yes**. No more questions.

### Branch: Outlook = Sunny
Days: 1,2,8,9,11 → Yes? Let’s see:  
- Day1: No  
- Day2: No  
- Day8: No  
- Day9: Yes  
- Day11: Yes  

So: **2 Yes, 3 No**. Still mixed. We need to ask another question **for this branch only**.

### Branch: Outlook = Rainy
Days: 4,5,6,10,14 → Yes?  
- Day4: Yes  
- Day5: Yes  
- Day6: No  
- Day10: Yes  
- Day14: No  

So: **3 Yes, 2 No**. Also mixed. Need another question **for this branch only**.

---

### Step 4: For the Sunny branch (2 Yes, 3 No)

We now look only at these 5 days (1,2,8,9,11).  
Remaining features: Temperature, Humidity, Wind (Outlook is already used).

We compute gains on this subset (again, I give you the numbers):

- **Humidity** gain = very high (nearly 0.97) because:
  - Humidity = High → days 1,2,8 → all No (pure)
  - Humidity = Normal → days 9,11 → all Yes (pure)
- Wind gain = smaller
- Temperature gain = smaller

So best is **Humidity**. Ask: “Humidity?”

- Humidity = High → **No**
- Humidity = Normal → **Yes**

Sunny branch is done.

---

### Step 5: For the Rainy branch (3 Yes, 2 No)

Look at days 4,5,6,10,14.  
Remaining features: Temperature, Humidity, Wind.

Compute gains:

- **Wind** gain = very high (0.97) because:
  - Wind = Weak → days 4,5,10 → all Yes (pure)
  - Wind = Strong → days 6,14 → all No (pure)
- Others give less gain.

So best is **Wind**. Ask: “Wind?”

- Wind = Weak → **Yes**
- Wind = Strong → **No**

Rainy branch is done.

---

### Step 6: The final tree

```
Outlook?
├── Overcast → Yes
├── Sunny → Humidity?
│   ├── High → No
│   └── Normal → Yes
└── Rainy → Wind?
    ├── Weak → Yes
    └── Strong → No
```

That’s it. No more questions because all leaves are pure.

---

### Now you understand the whole ID3 algorithm:

1. Start with all data.  
2. If all same class → leaf.  
3. Else, pick feature with **highest Information Gain** (biggest drop in entropy).  
4. Split on that feature.  
5. For each branch, repeat steps 2‑4.

---

### Your turn – quick check

If you have a new day: Outlook = Sunny, Humidity = High, what does the tree predict?

Answer when ready. Then we can talk about numeric features (like temperature in degrees) – but only when you want.

## Topic 6: Numeric features – what if temperature is a number? (slides 20–21)

In the tennis example, Temperature was discrete (Hot, Mild, Cool). But real data often has **numbers** like 85°, 80°, 83°.

We cannot split on every possible number – that would create too many branches. Instead, we create a **binary test**: `Temperature ≤ t` or `Temperature > t`.

**How to find the best threshold t?**

1. Sort the examples by temperature.
    
2. Look at mid‑points between consecutive values (e.g., between 65 and 68, mid = 66.5).
    
3. For each mid‑point, pretend to split the data into two groups (≤ t and > t). Compute Information Gain.
    
4. Pick the t that gives the highest gain.
    

Example: Temperature values in the data: 64,65,68,69,70,71,72,75,80,81,83,85.  
Try t = 66.5 → left group: {64,65}, right group: {68,…85}. Compute gain. Try others. Choose best.

This makes a **binary split** (only two branches), which works fine.
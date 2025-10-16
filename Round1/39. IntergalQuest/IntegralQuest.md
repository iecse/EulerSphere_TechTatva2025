---
title: "The Hidden Angle Integral"
difficulty: "Easy"
tags: ["calculus", "integration", "substitution", "integration by parts"]
id: 11
---

# The Hidden Angle Integral (Difficulty: Easy)

### Problem  
Evaluate:

$$
I = \int_{0}^{1/2} \frac{x \sin^{-1} x}{\sqrt{1 - x^2}} \, dx
$$

$$
Take \pi = 3.14 and \sqrt{3} = 1.732
$$

Keep the answer in 3 decimal places
---

### Solution  

Let  

$$
I = \int_{0}^{1/2} \frac{x \sin^{-1} x}{\sqrt{1 - x^2}} \, dx
$$  

Substitute:  

$$
x = \sin \theta, \quad dx = \cos \theta \, d\theta
$$  

$$
When ( x = 0 \Rightarrow \theta = 0),  
and when (x = \frac{1}{2} \Rightarrow \theta = \tfrac{\pi}{6}).  
$$

Thus:  

$$
I = \int_{0}^{\pi/6} \theta \sin \theta \, d\theta
$$

---

### Integration by Parts  

Using integration by parts:  

$$
I = \Big[ \theta(-\cos \theta) \Big]_{0}^{\pi/6} + \int_{0}^{\pi/6} \cos \theta \, d\theta
$$

$$
I = \Big[-\theta \cos \theta + \sin \theta \Big]_{0}^{\pi/6}
$$

---

### Final Answer  

$$
I = -\frac{\pi}{6} \cdot \frac{\sqrt{3}}{2} + \frac{1}{2}
= \frac{6 - \pi \sqrt{3}}{12}
$$

Answer = 0.047

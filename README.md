# VBA of Wall Street

## Overview of Project

### Purpose
The purpose of this project was to analyze two years worth of stock market data to find the best and most reliable eco-friendly stocks for Steve's parents to purchase. This included taking existing code and refactoring it for optimal efficiency.
## Analysis and Challenges

### Analysis of 2017
2017 was a great year for eco-friendly stocks, with 11 of the 12 researched reporting a positive return; 4 of which had a return over 100%. Because of the many economic factors at play in a given year, it's important to review the 2018 data as well, before making any purchases.

The refactored code (as seen here) featuring the tickerIndex variable, ran faster than the original code:
![VBA Code Time 2017](https://github.com/krockway/stock-analysis/blob/main/Resources/VBA_Challenge_2017.png)

### Analysis of 2018
2018 was a less reliable year for eco-friendly stocks, only 2 of the 12 researched had a positive return. In combination with the 2017 results, Steve should recommend ENPH and RUN to his parents, as these two stocks performed reliably in both 2017 and 2018.

The refactored code (as seen here) featuring the tickerIndex variable, ran faster than the original code:
![VBA Code Time 2018](https://github.com/krockway/stock-analysis/blob/main/Resources/VBA_Challenge_2018.png)

## Results

**- What are the advantages or disadvantages of refactoring code?**

The main advantage of refactoring is that it helps improve code - it can make it faster, easier to understand and simpler to maintain.

One of the main disadvantages of refactoring code is that you didn't write it the first time around. The first step is to understand what the code is trying to do, then you can look for ways to enhance it. 

Depending on the size or complexity of the code, it can also be risky or hazardous to refactor code. You might be making unintended changes.

**- How do these pros and cons apply to refactoring the original VBA script?**

One of the main pros was that the code ran faster - .496 seconds for the original file 2018 analysis vs .472 seconds in the refactored file 2018 analysis. Although this is a small amount of time savings, for a larger file this could be much more significant. 

The refactored code also increases the flexibility because of the tickerIndex variable. If I wanted to change the number of stocks that I was researching, I would have to update fewer pieces of information - only the array size and the initial for loop. 

The con to using someone else's code at the start, is that it took me much longer to understand the layout, than if I had written it myself. In some cases, the provided outline used language that I did not find intuitive. For example, this part of the outline took me a while to understand:
```
        '3d Increase the tickerIndex.
        Next j
    
    Next i
```    
Had I written this myself from scratch, I would have known that I needed to move to the next part of the loop via the "Next j" and "Next i" commands.
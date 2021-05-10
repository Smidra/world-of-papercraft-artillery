# World of papercraft artillery
*Wanna play some tanks?*

## What is this?
World of papercraft artillery is a simple boardgame implementation of the [artillery game](https://en.wikipedia.org/wiki/Artillery_game).
It is Python script which generates artillery tables for a symetrical 2D game area.
The terrain (mountains) is described by a mathematical function hardcoded (SHAME!) in the script.

## Why is this?
It is a pet project of me and my roomate. It all started with the idea if it would be possible to play the artillery game offline on a squared paper.

## How to use it?
Simple, just download and print out one of the four generated levels. In the 

**1) Draw the game area**
Take a squared piece of paper and mark fifty squares horizontaly and fifteen sqraues verticaly.
On the botom of level there is a surface height mark for every 2 squares.
Draw the whole line as the level.

**2) Place your tank on the drawn surface**
Pick a place where your and your oponent's tanks are starting.

**3) Pick a direction & angle**
Direction of your howitzer can be to the left or to the right. Angle must be between 0° and 90˚.
Pick without looking at the table.

**4a) Fire right**
When shooting to the right side. On the "↷" Y axis find the square number (place) from which you fired.
On the horizontal X axis (top) find the angle in wich you fired.

At the intersection of the column and row you shall find the result in a format **IMPACT SQUARE: IMPACT ANGLE**

**4b) Fire left**
When shooting to the left side. On the "↶" Y axis find the square number (place) from which you fired.
On the horizontal X axis (top) find the angle in wich you fired.

At the intersection of the column and row you shall find the result in a format **IMPACT SQUARE: IMPACT ANGLE**

**Substract the IMPACT SQUARE from fifty to get the final place**

## Is it any good?
[Yes](https://news.ycombinator.com/item?id=3067434)

## Credits
Created in cooperation with Pavel Mares

## 1. Opening (target 12 s, ~25 words)
Hello, I'm Arnav Maheshwari. In this video we'll explore the derivative, and see how a secant line becomes a tangent line to give us an instantaneous rate of change.

## 2. Hook (target 40 s, ~85 words)
Imagine a car driving for three hours, where the distance travelled after t hours is d of t equals t squared kilometres. Over the whole trip it covers nine kilometres in three hours, so its average speed is three kilometres per hour. But an average hides details. The car starts slowly and speeds up. So a better question is: how fast is it going at exactly one hour? To answer that, we first need to understand average rate of change.

## 3. Average rate of change (target 50 s, ~105 words)
Here is the graph of f of x equals x squared. Take two points: A at x equals 1, where y is 1, and B at x equals 3, where y is 9. A straight line through two points on a curve is called a secant line. The horizontal change, delta x, is 3 minus 1, which is 2. The vertical change, delta y, is 9 minus 1, which is 8. The average rate of change is delta y divided by delta x, which is 8 divided by 2, equal to 4. This is exactly the slope of the secant line.

## 4. Secant to tangent (target 50 s, ~105 words)
Now let's keep point A fixed at x equals a, which is 1, and move the second point closer. We call the horizontal gap h. The secant slope is f of a plus h, minus f of a, all divided by h. Watch what happens as h shrinks. The red line rotates, and its slope drops from 4 toward 2. When h becomes extremely small, the secant line settles onto the green line that just touches the curve at one point. That line is the tangent line, and its slope is the instantaneous rate of change.

## 5. Numerical table (target 40 s, ~85 words)
Let's check this with numbers. For h equals 1, the slope is 3. For h equals 0.5, the slope is 2.5. For h equals 0.1, it is 2.1, and for h equals 0.01, it is 2.01. The pattern is clear: as h gets closer to zero, the slope gets closer to 2. But a pattern is not a proof, so next we will show why, using algebra.

## 6. Algebra and definition (target 65 s, ~135 words)
We start from the secant slope formula with f of x equals x squared. Substituting, we get a plus h squared, minus a squared, all over h. Expanding a plus h squared gives a squared plus 2ah plus h squared. The a squared terms cancel, leaving 2ah plus h squared, over h. Now factor h out of the top: h times 2a plus h, over h. Since h is not zero, we can cancel h, and the slope simplifies to 2a plus h. Now let h approach zero. The slope approaches 2a. At a equals 1, that gives 2, matching our table. This idea is the definition of the derivative: f prime of a equals the limit, as h approaches zero, of f of a plus h minus f of a, over h. It is the slope of the tangent line at x equals a.

## 7. Worked example (target 50 s, ~105 words)
Let's use this to find the tangent line to x squared at x equals 1. The point is f of 1, which equals 1, so the point is (1, 1). The slope is f prime of 1, which is 2. Using point-slope form, y minus 1 equals 2 times x minus 1, which simplifies to y equals 2x minus 1. Let's check by substitution. At x equals 1, y equals 2 minus 1, which is 1, so the line passes through our point. Setting x squared equal to 2x minus 1 gives x minus 1, squared, equals zero, which has only one solution, x equals 1. So the line touches the curve at exactly one point, as a tangent should.

## 8. Closing (target 30 s, ~65 words)
To summarise: the average rate of change is the slope of a secant line. As h shrinks, the secant becomes the tangent, and its slope is the derivative. For x squared, the derivative at a is 2a. Thanks for watching. This video was animated with Manim, and used AI assistance for planning and code help. All the mathematics was verified by me.
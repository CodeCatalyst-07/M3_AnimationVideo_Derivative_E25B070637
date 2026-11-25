# The Derivative: from Secant to Tangent

M3 Internal Assessment (10%) - Animation Video
Student: Arnav Maheshwari  | ID: E25B070637

## Learning objective
By the end of the video, the viewer will be able to explain the derivative of f(x) = x^2 at a point as the limit of secant slopes, and interpret f'(1) = 2 as the slope of the tangent line at x = 1.

## Contents
- E25B070637_Video.mp4 - final 1080p video (about 5 min 57 s)
- E25B070637_Storyboard.pdf - 6-scene storyboard
- E25B070637_Code/ - all source code
  - scenes.py - Manim scenes (Opening, Hook, AverageRate, SecantToTangent, NumericalTable, Algebra, WorkedExample, Closing)
  - narration_script.md - narration script
  - audio/ - my recorded narration, one file per part
  - build.sh - matches each animation clip to its narration with FFmpeg
  - make_storyboard.py - generates the storyboard PDF
  - requirements.txt - Python packages

## How to run
Requires Python 3, FFmpeg and a LaTeX installation (needed by Manim for math text).

    cd E25B070637_Code
    pip install -r requirements.txt
    manim -qh scenes.py Opening
    (repeat for the other 7 scenes, or use a loop)
    bash build.sh

## Credits and AI disclosure
- Animation: Manim Community (Python)
- Narration: recorded by me
- Music: no background music used
- AI disclosure: AI assistance was used for planning, script drafting and code help. All mathematics was independently recalculated and verified by me.

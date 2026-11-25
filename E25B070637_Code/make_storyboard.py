"""
Generates the storyboard PDF for the M3 animation video.

1. Edit STUDENT_NAME, STUDENT_ID and MUSIC_CREDIT below.
2. pip install reportlab
3. python make_storyboard.py
"""
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (PageBreak, Paragraph, SimpleDocTemplate,
                                Spacer, Table, TableStyle)

# ---------- EDIT THESE ----------
STUDENT_NAME = "Arnav Maheshwari"
STUDENT_ID = "E25B070637"
MUSIC_CREDIT = "no background music used"
OUTPUT = f"{STUDENT_ID}_Storyboard.pdf"
# --------------------------------

NAVY = colors.HexColor("#16294a")
LIGHT = colors.HexColor("#f4f6fa")
GRID = colors.HexColor("#c5cddd")

ss = getSampleStyleSheet()
H1 = ParagraphStyle("H1", parent=ss["Title"], fontSize=20, textColor=NAVY,
                    alignment=0, spaceAfter=4)
H2 = ParagraphStyle("H2", parent=ss["Heading2"], fontSize=13, textColor=NAVY,
                    spaceBefore=10, spaceAfter=4)
BODY = ParagraphStyle("BODY", parent=ss["Normal"], fontSize=9.5, leading=13)
CELL = ParagraphStyle("CELL", parent=ss["Normal"], fontSize=8.3, leading=10.8)
CELLB = ParagraphStyle("CELLB", parent=CELL, fontName="Helvetica-Bold")
HEAD = ParagraphStyle("HEAD", parent=CELL, fontName="Helvetica-Bold",
                      textColor=colors.white)


def p(text, style=CELL):
    return Paragraph(text, style)


def make_table(data, widths, header=True):
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0)
    style = [
        ("GRID", (0, 0), (-1, -1), 0.5, GRID),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]
    if header:
        style.append(("BACKGROUND", (0, 0), (-1, 0), NAVY))
    for r in range(1, len(data)):
        if r % 2 == 0:
            style.append(("BACKGROUND", (0, r), (-1, r), LIGHT))
    t.setStyle(TableStyle(style))
    return t


story = []

# ---------------- Page 1: overview ----------------
story.append(p("M3 Internal Assessment - Animation Video Storyboard", H1))
story.append(p(
    f"<b>Concept:</b> The Derivative as the limit of secant slopes "
    f"(rate of change, secant to tangent) &nbsp;|&nbsp; "
    f"<b>Student:</b> {STUDENT_NAME} &nbsp;|&nbsp; <b>ID:</b> {STUDENT_ID}", BODY))
story.append(Spacer(1, 6))

story.append(p("Learning objective", H2))
story.append(p(
    "<i>By the end of this video, the viewer will be able to explain the "
    "derivative of f(x) = x<super>2</super> at a point as the limit of secant "
    "slopes, and interpret f'(1) = 2 as the slope of the tangent line at "
    "x = 1.</i>", BODY))

story.append(p("Video details", H2))
details = [
    [p("Length", CELLB), p("About 5 min 57 s (minimum required: 5 min; maximum: 7 min)")],
    [p("Format", CELLB), p("1920 x 1080 (1080p), 16:9, MP4, 60 fps")],
    [p("Tool", CELLB), p("Manim Community (Python). One scene class per clip, all in scenes.py")],
    [p("Narration", CELLB), p("Recorded by the student, one audio file per part, "
                              "combined with the animation using FFmpeg (build.sh)")],
    [p("Example used", CELLB), p("f(x) = x<super>2</super> at a = 1: "
                                 "points A(1,1) and B(3,9), secant slope 4, "
                                 "tangent slope 2, tangent line y = 2x - 1")],
]
story.append(make_table(details, [90, 680], header=False))

story.append(p("Colour coding (kept the same in every scene)", H2))
colours = [
    [p("Colour", HEAD), p("Used for", HEAD)],
    [p("Blue", CELLB), p("The graph of f(x) = x<super>2</super>, titles")],
    [p("Yellow", CELLB), p("Fixed point A / a = 1, key results and definitions")],
    [p("Red", CELLB), p("Secant line, second point B, secant slope")],
    [p("Green", CELLB), p("Tangent line, horizontal step (delta x), final slope")],
    [p("Orange", CELLB), p("Vertical step (delta y)")],
]
story.append(make_table(colours, [90, 680]))

# ---------------- Storyboard table ----------------
story.append(PageBreak())
story.append(p("6-scene storyboard", H2))
story.append(p(
    "Each scene lists the animation clip(s) in scenes.py that implement it. "
    "One step is animated at a time, and all notation is defined before use.",
    BODY))
story.append(Spacer(1, 4))

rows = [[p("Scene / Purpose", HEAD), p("Time", HEAD),
         p("Visual plan", HEAD), p("Narration plan", HEAD),
         p("Math plan", HEAD)]]


def scene_row(title, purpose, time, clips, visual, narration, math):
    return [
        p(f"<b>{title}</b><br/><i>{purpose}</i><br/><font size=7>Code: {clips}</font>"),
        p(time),
        p(visual), p(narration), p(math),
    ]


rows.append(scene_row(
    "1. Hook / Context", "Spark curiosity and motivate the topic.",
    "0:00 - 0:55", "Opening, Hook",
    "Title frame with concept, name and ID. Then a distance-time graph "
    "d(t) = t<super>2</super> with a moving dot (a car). Red line over the "
    "whole trip shows the average speed. The question 'how fast at exactly "
    "t = 1?' appears on screen.",
    "A car drives for 3 hours. Average speed is easy to find, but an average "
    "hides details. The real question: how fast is it going at one exact "
    "moment?",
    "d(3) = 9 km in 3 h, so average speed = (9 - 0)/(3 - 0) = 3 km/h."))

rows.append(scene_row(
    "2. Concept Introduction", "Define the concept and learning goal.",
    "0:55 - 1:43", "AverageRate",
    "Graph of f(x) = x<super>2</super> with points A(1,1) and B(3,9). "
    "Red secant line. Green dashed horizontal step (delta x) and orange "
    "dashed vertical step (delta y), each labelled as it appears.",
    "Defines secant line, delta x and delta y. Average rate of change = "
    "delta y / delta x = slope of the secant line. States what we will "
    "find: the rate of change at a single point.",
    "delta x = 3 - 1 = 2<br/>delta y = f(3) - f(1) = 9 - 1 = 8<br/>"
    "average rate = 8/2 = 4"))

rows.append(scene_row(
    "3. Visual Intuition", "Build geometric understanding first.",
    "1:43 - 3:06", "SecantToTangent, NumericalTable",
    "Point A stays fixed. Point B slides toward A as h shrinks from 2 to "
    "0.01 while the secant rotates and its slope is shown live. The green "
    "tangent line then appears. A table lists the slope for h = 1, 0.5, "
    "0.1, 0.01 and the slope column is boxed.",
    "Keep A fixed and move B closer, with horizontal gap h. The secant "
    "settles onto the tangent line. Check with numbers: slopes 3, 2.5, 2.1, "
    "2.01 head toward 2. A pattern is not a proof, so algebra comes next.",
    "m_sec = (f(1+h) - f(1))/h<br/>h = 1: 3 &nbsp; h = 0.5: 2.5<br/>"
    "h = 0.1: 2.1 &nbsp; h = 0.01: 2.01<br/>As h -> 0, slope -> 2"))

rows.append(scene_row(
    "4. Worked Example", "Demonstrate why and how the math works.",
    "3:06 - 4:24", "Algebra",
    "Each algebra line appears one at a time with a short yellow note "
    "(expand, cancel, factor, cancel h). The final line 2a + h is boxed in "
    "green. The scene ends with the boxed definition of the derivative.",
    "Substitute f(x) = x<super>2</super> into the secant slope, expand, "
    "cancel, factor out h and simplify. Let h approach 0. This is exactly "
    "the definition of the derivative.",
    "((a+h)<super>2</super> - a<super>2</super>)/h = (2ah + h<super>2</super>)/h "
    "= 2a + h<br/>h -> 0 gives f'(a) = 2a, so f'(1) = 2<br/>"
    "f'(a) = lim (h->0) (f(a+h) - f(a))/h"))

rows.append(scene_row(
    "5. Interpretation", "Connect algebra back to visual meaning.",
    "4:24 - 5:22", "WorkedExample",
    "Graph with the point (1,1). The tangent line y = 2x - 1 is drawn in "
    "green while the steps appear on the right. Verification by "
    "substitution is shown below.",
    "f'(1) = 2 is the slope of the tangent at (1,1). Build the line with "
    "point-slope form. Check: the line passes through (1,1) and meets the "
    "curve at only one point, as a tangent should.",
    "f(1) = 1, f'(1) = 2<br/>y - 1 = 2(x - 1), so y = 2x - 1<br/>"
    "Check: x = 1 gives y = 1<br/>x<super>2</super> = 2x - 1 gives "
    "(x - 1)<super>2</super> = 0, only x = 1"))

rows.append(scene_row(
    "6. Summary and Credits", "Reinforce takeaways and cite sources.",
    "5:22 - 5:57", "Closing",
    "Four summary points appear one at a time, then a credits screen: "
    "creator, tools, narration, music and AI disclosure.",
    "Average rate of change is the slope of a secant. Shrinking h turns the "
    "secant into the tangent, and its slope is the derivative. For "
    "x<super>2</super>, f'(a) = 2a. Credits and AI disclosure.",
    "Recap: 1) average rate = secant slope; 2) h -> 0 gives the tangent; "
    "3) f'(a) = lim (f(a+h) - f(a))/h; 4) f'(a) = 2a, f'(1) = 2."))

story.append(make_table(rows, [105, 50, 205, 205, 205]))

# ---------------- Verification + credits ----------------
story.append(PageBreak())
story.append(p("Mathematical verification (done by hand on paper)", H2))
ver = [
    [p("Check", HEAD), p("Working", HEAD), p("Result", HEAD)],
    [p("Average rate on [1, 3]"), p("(9 - 1)/(3 - 1)"), p("4")],
    [p("Secant slope, h = 0.5"), p("(1.5<super>2</super> - 1)/0.5 = 1.25/0.5"), p("2.5")],
    [p("Secant slope, h = 0.1"), p("(1.1<super>2</super> - 1)/0.1 = 0.21/0.1"), p("2.1")],
    [p("Secant slope, h = 0.01"), p("(1.01<super>2</super> - 1)/0.01 = 0.0201/0.01"), p("2.01")],
    [p("Algebra"), p("(a+h)<super>2</super> - a<super>2</super> = 2ah + h<super>2</super>; "
                     "divide by h"), p("2a + h")],
    [p("Tangent line at x = 1"), p("y - 1 = 2(x - 1)"), p("y = 2x - 1")],
    [p("Tangent touches only once"), p("x<super>2</super> - 2x + 1 = (x - 1)<super>2</super> = 0"),
     p("Only x = 1")],
]
story.append(make_table(ver, [170, 440, 160]))

story.append(p("Tools, credits and AI disclosure", H2))
story.append(p(
    f"<b>Animation:</b> Manim Community (Python). "
    f"<b>Narration:</b> recorded by {STUDENT_NAME}. "
    f"<b>Music:</b> {MUSIC_CREDIT}. "
    f"<b>Video assembly:</b> FFmpeg. "
    f"<b>AI disclosure:</b> AI assistance was used for planning, script "
    f"drafting and code help. All mathematics was independently recalculated "
    f"and verified by the student.", BODY))


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.grey)
    canvas.drawString(15 * mm, 8 * mm,
                      f"M3 Internal Assessment - Storyboard - {STUDENT_NAME} ({STUDENT_ID})")
    canvas.drawRightString(landscape(A4)[0] - 15 * mm, 8 * mm, f"Page {doc.page}")
    canvas.restoreState()


doc = SimpleDocTemplate(OUTPUT, pagesize=landscape(A4),
                        leftMargin=36, rightMargin=36,
                        topMargin=30, bottomMargin=30,
                        title="M3 Animation Video Storyboard",
                        author=STUDENT_NAME)
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print("Created", OUTPUT)

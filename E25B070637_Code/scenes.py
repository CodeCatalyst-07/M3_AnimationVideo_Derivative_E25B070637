from manim import *

class SecantToTangent(Scene):
    def construct(self):
        a = 1
        axes = Axes(
            x_range=[0, 4, 1], y_range=[0, 10, 2],
            x_length=7, y_length=5,
            axis_config={"include_numbers": True},
        ).to_edge(LEFT)
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        graph = axes.plot(lambda x: x**2, x_range=[0, 3.2], color=BLUE)
        glabel = axes.get_graph_label(graph, "f(x)=x^2", x_val=2.8, direction=UL)

        h = ValueTracker(2)

        dot_a = Dot(axes.c2p(a, a**2), color=YELLOW)
        dot_b = always_redraw(lambda: Dot(
            axes.c2p(a + h.get_value(), (a + h.get_value())**2), color=RED))
        secant = always_redraw(lambda: axes.plot(
            lambda x: (2*a + h.get_value()) * (x - a) + a**2,
            x_range=[0.3, 3.2], color=RED))
        slope_text = always_redraw(lambda: MathTex(
            r"m_{\text{sec}} = \frac{f(a+h)-f(a)}{h} = ",
            f"{2*a + h.get_value():.3f}").scale(0.8).to_corner(UR))
        h_text = always_redraw(lambda: MathTex(
            "h = ", f"{h.get_value():.3f}").scale(0.8).next_to(slope_text, DOWN))

        self.play(Create(axes), Write(labels))
        self.play(Create(graph), Write(glabel))
        self.play(FadeIn(dot_a), FadeIn(dot_b), Create(secant))
        self.play(Write(slope_text), Write(h_text))
        self.wait(2)
        self.play(h.animate.set_value(0.01), run_time=8, rate_func=smooth)
        self.wait(1)

        tangent = axes.plot(lambda x: 2*a*(x - a) + a**2,
                            x_range=[0.3, 3.2], color=GREEN)
        self.play(Create(tangent))
        self.wait(2)

class Opening(Scene):
    def construct(self):
        title = Text("The Derivative", font_size=64, color=BLUE)
        sub = Text("Rate of Change: from Secant to Tangent", font_size=32)
        sub.next_to(title, DOWN)
        info = VGroup(
            Text("Name: Arnav Maheshwari", font_size=28),
            Text("Student ID: E25B070637", font_size=28),
            Text("M3 Internal Assessment - Animation Video", font_size=24),
        ).arrange(DOWN, buff=0.3).to_edge(DOWN)

        self.play(Write(title))
        self.play(FadeIn(sub, shift=UP))
        self.play(FadeIn(info))
        self.wait(3)


class Hook(Scene):
    def construct(self):
        intro = Text("A car drives for 3 hours.", font_size=36)
        self.play(Write(intro))
        self.wait(1)
        self.play(intro.animate.to_edge(UP))

        axes = Axes(
            x_range=[0, 3.5, 1], y_range=[0, 10, 2],
            x_length=7, y_length=4.5,
            axis_config={"include_numbers": True},
        ).shift(DOWN * 0.2)
        labels = axes.get_axis_labels(MathTex("t"), MathTex("d"))
        graph = axes.plot(lambda t: t**2, x_range=[0, 3], color=BLUE)
        graph_label = MathTex(r"d(t)=t^2", color=BLUE).move_to(axes.c2p(1.0, 8))

        t = ValueTracker(0)
        dot = always_redraw(lambda: Dot(
            axes.c2p(t.get_value(), t.get_value()**2), color=YELLOW))

        self.play(Create(axes), Write(labels))
        self.play(Create(graph), Write(graph_label))
        self.add(dot)
        self.play(t.animate.set_value(3), run_time=5, rate_func=linear)
        self.wait(1)

        line = Line(axes.c2p(0, 0), axes.c2p(3, 9), color=RED)
        avg = MathTex(
            r"\text{average speed}=\frac{9-0}{3-0}=3\ \text{km/h}",
            color=RED).scale(0.8).to_edge(DOWN)
        self.play(Create(line))
        self.play(Write(avg))
        self.wait(2)

        question = Text("But how fast is it going at exactly t = 1 hour?",
                        font_size=30, color=YELLOW).to_edge(DOWN)
        self.play(FadeOut(avg), FadeOut(line))
        self.play(t.animate.set_value(1), run_time=2)
        self.play(Write(question), Indicate(dot))
        self.wait(3)


class AverageRate(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 4, 1], y_range=[0, 10, 2],
            x_length=6.5, y_length=5,
            axis_config={"include_numbers": True},
        ).to_edge(LEFT)
        labels = axes.get_axis_labels(MathTex("x"), MathTex("f(x)"))
        graph = axes.plot(lambda x: x**2, x_range=[0, 3.2], color=BLUE)
        glabel = MathTex("f(x)=x^2", color=BLUE).move_to(axes.c2p(1.2, 8))

        A = axes.c2p(1, 1)
        B = axes.c2p(3, 9)
        C = axes.c2p(3, 1)
        dotA = Dot(A, color=YELLOW)
        dotB = Dot(B, color=RED)
        labA = MathTex("A(1,1)", color=YELLOW).scale(0.7).next_to(dotA, DR, buff=0.1)
        labB = MathTex("B(3,9)", color=RED).scale(0.7).next_to(dotB, LEFT)

        secant = axes.plot(lambda x: 4 * (x - 1) + 1,
                           x_range=[0.8, 3.2], color=RED)
        horiz = DashedLine(A, C, color=GREEN)
        vert = DashedLine(C, B, color=ORANGE)
        dx_lab = MathTex(r"\Delta x", color=GREEN).scale(0.8).next_to(horiz, DOWN, buff=0.1)
        dy_lab = MathTex(r"\Delta y", color=ORANGE).scale(0.8).next_to(vert, RIGHT, buff=0.1)

        eq1 = MathTex(r"\Delta x = x_2 - x_1 = 3 - 1 = 2", color=GREEN)
        eq2 = MathTex(r"\Delta y = f(x_2) - f(x_1) = 9 - 1 = 8", color=ORANGE)
        eq3 = MathTex(r"\text{average rate}=\frac{\Delta y}{\Delta x}=\frac{8}{2}=4", color=RED)
        panel = VGroup(eq1, eq2, eq3).scale(0.8).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        panel.to_edge(RIGHT).shift(UP * 0.5)

        note = Text("A line through two points on a curve is called a secant line.",
                    font_size=22).to_edge(DOWN)
        final = Text("Average rate of change = slope of the secant line",
                     font_size=26, color=YELLOW).to_edge(DOWN)

        self.play(Create(axes), Write(labels))
        self.play(Create(graph), Write(glabel))
        self.play(FadeIn(dotA), Write(labA))
        self.play(FadeIn(dotB), Write(labB))
        self.play(Create(secant), FadeIn(note))
        self.wait(2)
        self.play(Create(horiz), Write(dx_lab))
        self.play(Write(eq1))
        self.wait(1)
        self.play(Create(vert), Write(dy_lab))
        self.play(Write(eq2))
        self.wait(1)
        self.play(Write(eq3))
        self.wait(2)
        self.play(FadeOut(note))
        self.play(Write(final))
        self.wait(3)

class NumericalTable(Scene):
    def construct(self):
        title = Text("What happens as h gets smaller?", font_size=34).to_edge(UP)
        setup = MathTex(
            r"f(x)=x^2,\quad a=1,\quad "
            r"m_{\text{sec}}=\frac{f(1+h)-f(1)}{h}"
        ).scale(0.8).next_to(title, DOWN)

        table = Table(
            [["1", "4", "3", "3"],
             ["0.5", "2.25", "1.25", "2.5"],
             ["0.1", "1.21", "0.21", "2.1"],
             ["0.01", "1.0201", "0.0201", "2.01"]],
            col_labels=[
                MathTex("h"),
                MathTex("f(1+h)"),
                MathTex("f(1+h)-f(1)"),
                MathTex(r"m_{\text{sec}}"),
            ],
            include_outer_lines=True,
        ).scale(0.6).shift(DOWN * 0.8)

        self.play(Write(title))
        self.play(Write(setup))
        self.wait(1)
        self.play(Create(table), run_time=4)
        self.wait(2)

        box = SurroundingRectangle(table.get_columns()[3], color=YELLOW)
        self.play(Create(box))
        result = MathTex(
            r"\text{As } h \to 0,\ m_{\text{sec}} \to 2",
            color=YELLOW,
        ).scale(0.9).to_edge(DOWN)
        self.play(Write(result))
        self.wait(3)

class Algebra(Scene):
    def construct(self):
        title = Text("Why does the slope approach 2?", font_size=34).to_edge(UP)
        self.play(Write(title))

        steps = VGroup(
            MathTex(r"m_{\text{sec}}=\frac{f(a+h)-f(a)}{h}"),
            MathTex(r"=\frac{(a+h)^2-a^2}{h}"),
            MathTex(r"=\frac{a^2+2ah+h^2-a^2}{h}"),
            MathTex(r"=\frac{2ah+h^2}{h}"),
            MathTex(r"=\frac{h\,(2a+h)}{h}"),
            MathTex(r"=2a+h"),
        ).scale(0.85).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        steps.next_to(title, DOWN, buff=0.4).to_edge(LEFT, buff=1.2)

        notes = [
            "Start with f(x) = x^2",
            "Expand (a+h)^2",
            "a^2 terms cancel",
            "Factor out h",
            "Cancel h (allowed because h is not 0)",
            "",
        ]
        note_text = Text("", font_size=24)

        self.play(Write(steps[0]))
        self.wait(1)
        for i in range(1, 6):
            new_note = Text(notes[i], font_size=24, color=YELLOW)
            new_note.next_to(steps[i], RIGHT, buff=0.6)
            self.play(Write(steps[i]), FadeIn(new_note))
            self.wait(1.5)
            self.play(FadeOut(new_note))

        box = SurroundingRectangle(steps[5], color=GREEN)
        self.play(Create(box))
        self.wait(1)

        limit = MathTex(
            r"\text{As } h\to 0:\quad 2a+h \;\to\; 2a", color=GREEN
        ).scale(0.9).next_to(steps, RIGHT, buff=1.0).shift(UP * 0.5)
        at1 = MathTex(r"\text{At } a=1:\ f'(1)=2", color=YELLOW).scale(0.9)
        at1.next_to(limit, DOWN, buff=0.5)
        self.play(Write(limit))
        self.wait(1)
        self.play(Write(at1))
        self.wait(3)

        # Definition of the derivative
        self.play(*[FadeOut(m) for m in self.mobjects])
        defn_title = Text("Definition of the derivative", font_size=36).to_edge(UP)
        defn = MathTex(
            r"f'(a)=\lim_{h\to 0}\frac{f(a+h)-f(a)}{h}", color=YELLOW
        ).scale(1.2)
        defn_box = SurroundingRectangle(defn, color=BLUE, buff=0.4)
        meaning = Text(
            "f'(a) is the slope of the tangent line at x = a,\n"
            "the instantaneous rate of change.",
            font_size=26,
        ).next_to(defn_box, DOWN, buff=0.6)
        self.play(Write(defn_title))
        self.play(Write(defn), Create(defn_box))
        self.play(FadeIn(meaning))
        self.wait(4)

class WorkedExample(Scene):
    def construct(self):
        title = Text("Worked example: tangent line at x = 1", font_size=32).to_edge(UP)
        self.play(Write(title))

        axes = Axes(
            x_range=[0, 4, 1], y_range=[0, 10, 2],
            x_length=6, y_length=4.5,
            axis_config={"include_numbers": True},
        ).to_edge(LEFT).shift(DOWN * 0.4)
        labels = axes.get_axis_labels(MathTex("x"), MathTex("f(x)"))
        graph = axes.plot(lambda x: x**2, x_range=[0, 3.2], color=BLUE)
        glabel = MathTex("f(x)=x^2", color=BLUE).scale(0.8).move_to(axes.c2p(1.0, 8))
        point = Dot(axes.c2p(1, 1), color=YELLOW)
        plabel = MathTex("(1,1)", color=YELLOW).scale(0.7).next_to(point, DR, buff=0.1)
        tangent = axes.plot(lambda x: 2 * x - 1, x_range=[0.2, 3], color=GREEN)

        s1 = MathTex(r"\text{Point: } f(1)=1^2=1 \Rightarrow (1,1)")
        s2 = MathTex(r"\text{Slope: } f'(1)=2")
        s3 = MathTex(r"y-1=2(x-1)")
        s4 = MathTex(r"y=2x-1", color=GREEN)
        steps = VGroup(s1, s2, s3, s4).scale(0.75).arrange(
            DOWN, aligned_edge=LEFT, buff=0.45)
        steps.to_edge(RIGHT, buff=0.5).shift(UP * 0.8)

        self.play(Create(axes), Write(labels))
        self.play(Create(graph), Write(glabel))
        self.play(FadeIn(point), Write(plabel))
        self.play(Write(s1))
        self.wait(1)
        self.play(Write(s2))
        self.wait(1)
        self.play(Write(s3))
        self.wait(1)
        self.play(Write(s4), Create(tangent))
        self.wait(2)

        # Verification by substitution
        check_title = Text("Check:", font_size=26, color=YELLOW)
        c1 = MathTex(r"x=1:\ y=2(1)-1=1\ \checkmark")
        c2 = MathTex(r"x^2=2x-1 \Rightarrow (x-1)^2=0", color=YELLOW)
        c3 = Text("Only one solution, x = 1, so the line touches\nthe curve at exactly one point.",
                  font_size=20)
        checks = VGroup(check_title, c1, c2, c3).arrange(
            DOWN, aligned_edge=LEFT, buff=0.3)
        checks.scale(0.8).next_to(steps, DOWN, buff=0.5).align_to(steps, LEFT)

        self.play(FadeIn(check_title))
        self.play(Write(c1))
        self.wait(1)
        self.play(Write(c2))
        self.wait(1)
        self.play(FadeIn(c3))
        self.wait(4)

class Closing(Scene):
    def construct(self):
        title = Text("Summary", font_size=44, color=BLUE).to_edge(UP)

        points = VGroup(
            Text("1. Average rate of change = slope of the secant line", font_size=26),
            Text("2. Shrinking h turns the secant into the tangent", font_size=26),
            Text("3. f'(a) = lim (f(a+h) - f(a)) / h", font_size=26),
            Text("4. For f(x) = x^2: f'(a) = 2a, so f'(1) = 2", font_size=26),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).next_to(title, DOWN, buff=0.6)

        self.play(Write(title))
        for p in points:
            self.play(FadeIn(p, shift=RIGHT * 0.3))
            self.wait(1.5)
        self.wait(2)

        self.play(FadeOut(points), FadeOut(title))

        credits_title = Text("Credits", font_size=44, color=BLUE).to_edge(UP)
        credits = VGroup(
            Text("Created by: Arnav Maheshwari (ID: E25B070637)", font_size=26),
            Text("Animation: Manim Community (Python)", font_size=26),
            Text("Narration: recorded by me", font_size=26),
            Text("AI disclosure: AI assistance was used for planning and\n"
                 "code help. All mathematics was independently verified by me.",
                 font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).next_to(credits_title, DOWN, buff=0.6)

        self.play(Write(credits_title))
        self.play(FadeIn(credits))
        self.wait(5)
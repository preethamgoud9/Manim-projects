from manim import *
import numpy as np
import scipy.stats as stats

class ProbabilityDistributions(Scene):
    def construct(self):
        # Title
        self.title = Text("Probability Distributions", font="Arial").scale(1.2)
        self.title.to_edge(UP)
        self.play(Write(self.title))
        
        # Axes setup
        self.axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 1, 0.1],
            axis_config={"color": WHITE},
            tips=False
        ).scale(1.2)
        self.axes.center()
        self.axes.to_edge(DOWN, buff=0.5)
        self.play(Create(self.axes))
        
        # Add labels
        x_label = Text("x", font="Arial").scale(0.6)
        y_label = Text("P(x)", font="Arial").scale(0.6)
        x_label.next_to(self.axes.x_axis, RIGHT)
        y_label.next_to(self.axes.y_axis, UP)
        self.play(Write(x_label), Write(y_label))
        
        # Explain different distributions
        self.explain_uniform_distribution()
        self.wait(2)
        self.clear_scene()
        self.explain_binomial_distribution()
        self.wait(2)
        self.clear_scene()
        self.explain_normal_distribution()
        self.wait(2)
    
    def clear_scene(self):
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
    def create_properties_list(self, items):
        properties = VGroup()
        for i, item in enumerate(items):
            bullet = Text("•", font="Arial").scale(0.4)
            text = Text(item, font="Arial").scale(0.4)
            line = VGroup(bullet, text).arrange(RIGHT, buff=0.2)
            if i > 0:
                line.next_to(properties[-1], DOWN, aligned_edge=LEFT)
            properties.add(line)
        return properties
    
    def explain_uniform_distribution(self):
        # Update title
        uniform_title = Text("Uniform Distribution", font="Arial").scale(1.2)
        uniform_title.to_edge(UP)
        self.play(Transform(self.title, uniform_title))
        
        # Properties
        properties = self.create_properties_list([
            "Equal probability across range",
            "Defined by min (a) and max (b) values",
            "Constant probability density",
            "Examples: Dice rolls, random number generators"
        ])
        properties.next_to(self.title, DOWN, buff=0.5)
        self.play(Write(properties))
        
        # Plot uniform PDF
        uniform_graph = VGroup()
        points = [
            self.axes.c2p(-2, 0),
            self.axes.c2p(-2, 0.5),
            self.axes.c2p(2, 0.5),
            self.axes.c2p(2, 0)
        ]
        uniform_graph.add(Line(points[0], points[1], color=BLUE))
        uniform_graph.add(Line(points[1], points[2], color=BLUE))
        uniform_graph.add(Line(points[2], points[3], color=BLUE))
        self.play(Create(uniform_graph))
    
    def explain_binomial_distribution(self):
        binomial_title = Text("Binomial Distribution", font="Arial").scale(1.2)
        binomial_title.to_edge(UP)
        self.play(Transform(self.title, binomial_title))
        
        # Properties
        properties = self.create_properties_list([
            "Discrete distribution",
            "Parameters: n (trials), p (success probability)",
            "Models coin flips, pass/fail tests"
        ])
        properties.next_to(self.title, DOWN, buff=0.5)
        self.play(Write(properties))
        
        # Plot binomial PMF
        n, p = 10, 0.5
        x_values = np.arange(0, n+1)
        y_values = stats.binom.pmf(x_values, n, p)
        dots = VGroup()
        lines = VGroup()
        
        for i in range(len(x_values)):
            point = self.axes.c2p(x_values[i], y_values[i])
            dot = Dot(point, color=RED)
            dots.add(dot)
            if i > 0:
                line = Line(
                    self.axes.c2p(x_values[i-1], y_values[i-1]),
                    point,
                    color=RED_A
                )
                lines.add(line)
        
        self.play(Create(lines), Create(dots))
    
    def explain_normal_distribution(self):
        normal_title = Text("Normal Distribution", font="Arial").scale(1.2)
        normal_title.to_edge(UP)
        self.play(Transform(self.title, normal_title))
        
        # Properties
        properties = self.create_properties_list([
            "Continuous, bell-shaped curve",
            "Defined by mean (μ) and standard deviation (σ)",
            "Common in natural phenomena (height, IQ, etc.)"
        ])
        properties.next_to(self.title, DOWN, buff=0.5)
        self.play(Write(properties))
        
        # Plot normal PDF
        x_range = np.linspace(-4, 4, 100)
        y_values = stats.norm.pdf(x_range, 0, 1)
        points = [self.axes.c2p(x, y) for x, y in zip(x_range, y_values)]
        normal_curve = VMobject()
        normal_curve.set_points_smoothly(points)
        normal_curve.set_color(GREEN)
        self.play(Create(normal_curve))
        
        # Highlight area within one standard deviation
        x_fill = np.linspace(-1, 1, 50)
        y_fill = stats.norm.pdf(x_fill, 0, 1)
        fill_points = [self.axes.c2p(x, y) for x, y in zip(x_fill, y_fill)]
        fill_points = [self.axes.c2p(1, 0)] + fill_points + [self.axes.c2p(-1, 0)]
        area = VMobject()
        area.set_points_smoothly(fill_points)
        area.set_fill(BLUE, opacity=0.3)
        area.set_stroke(width=0)
        self.play(FadeIn(area))
from manim import *
import numpy as np

class NeuralNetworkAnimation(Scene):
    def construct(self):
        self.camera.background_color = "#202020"
        
        # Introduction
        self.show_introduction()
        
        # Build Network Architecture
        layers = self.build_network()
        
        # Show Weights and Inputs
        self.explain_weights_and_inputs(layers)
        
        # Forward Pass
        self.demonstrate_forward_pass(layers)
        
        # Backpropagation
        self.demonstrate_backpropagation(layers)
        
        self.wait(2)
    
    def show_introduction(self):
        title = Text("Neural Networks", font="Arial", color=BLUE).scale(1.5)
        subtitle = Text("Step by Step Visualization", font="Arial", color=BLUE_B).scale(0.8)
        subtitle.next_to(title, DOWN)
        
        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))
    
    def create_neuron(self, color=WHITE):
        neuron = Circle(radius=0.15, color=color, fill_opacity=0.3)
        return neuron
    
    def build_network(self):
        # Network architecture: 3-4-2-1
        layer_sizes = [3, 4, 2, 1]
        layers = VGroup()
        
        # Title for this section
        section_title = Text("Building the Network", font="Arial", color=BLUE).scale(1.2)
        section_title.to_edge(UP)
        self.play(Write(section_title))
        
        # Create layers
        x_spacing = 2.5
        for i, size in enumerate(layer_sizes):
            layer = VGroup()
            y_spacing = 0.5
            for j in range(size):
                neuron = self.create_neuron()
                neuron.move_to([i * x_spacing - 3, (size-1)*y_spacing/2 - j*y_spacing, 0])
                layer.add(neuron)
            layers.add(layer)
            
            # Add layer label
            if i == 0:
                label = Text("Input Layer", font="Arial", color=BLUE_B).scale(0.4)
            elif i == len(layer_sizes)-1:
                label = Text("Output Layer", font="Arial", color=BLUE_B).scale(0.4)
            else:
                label = Text(f"Hidden Layer {i}", font="Arial", color=BLUE_B).scale(0.4)
            label.next_to(layer, DOWN, buff=0.5)
            layers.add(label)
            
            # Animate each neuron appearing
            for neuron in layer:
                self.play(Create(neuron), run_time=0.3)
            self.play(Write(label))
        
        # Create connections between layers
        connections = VGroup()
        for i in range(len(layer_sizes)-1):
            layer_connections = VGroup()
            for neuron1 in layers[i]:
                for neuron2 in layers[i+1]:
                    if isinstance(neuron1, Circle) and isinstance(neuron2, Circle):
                        connection = Line(
                            neuron1.get_center(),
                            neuron2.get_center(),
                            stroke_opacity=0.3
                        )
                        layer_connections.add(connection)
            connections.add(layer_connections)
            self.play(Create(layer_connections), run_time=1)
        
        self.wait(1)
        self.play(FadeOut(section_title))
        return layers
    
    def explain_weights_and_inputs(self, layers):
        # Title for this section
        section_title = Text("Weights and Inputs", font="Arial", color=BLUE).scale(1.2)
        section_title.to_edge(UP)
        self.play(Write(section_title))
        
        # Show sample input values
        input_values = [0.5, 0.8, 0.2]
        input_labels = VGroup()
        for i, value in enumerate(input_values):
            neuron = layers[0][i]
            label = Text(f"{value}", font="Arial", color=YELLOW).scale(0.4)
            label.next_to(neuron, LEFT)
            input_labels.add(label)
            self.play(Write(label))
        
        # Show sample weights on some connections
        weight_labels = VGroup()
        for i in range(2):  # Show weights for first two connections
            connection = layers[i]
            weight = Text(f"w={np.random.rand():.2f}", font="Arial", color=GREEN).scale(0.3)
            weight.move_to(connection.get_center())
            weight_labels.add(weight)
            self.play(Write(weight))
        
        self.wait(2)
        self.play(
            FadeOut(section_title),
            FadeOut(input_labels),
            FadeOut(weight_labels)
        )
    
    def demonstrate_forward_pass(self, layers):
        # Title for this section
        section_title = Text("Forward Pass", font="Arial", color=BLUE).scale(1.2)
        section_title.to_edge(UP)
        self.play(Write(section_title))
        
        # Animate data flowing through the network
        for i in range(len(layers)-1):
            if isinstance(layers[i], VGroup):
                for neuron in layers[i]:
                    if isinstance(neuron, Circle):
                        # Create animation of value passing through
                        pulse = Circle(radius=0.15, color=YELLOW, fill_opacity=1)
                        pulse.move_to(neuron.get_center())
                        self.play(
                            pulse.animate.scale(0.1).set_opacity(0),
                            run_time=0.5
                        )
        
        self.wait(1)
        self.play(FadeOut(section_title))
    
    def demonstrate_backpropagation(self, layers):
        # Title for this section
        section_title = Text("Backpropagation", font="Arial", color=RED).scale(1.2)
        section_title.to_edge(UP)
        self.play(Write(section_title))
        
        # Show error at output
        error = Text("Error", font="Arial", color=RED).scale(0.4)
        error.next_to(layers[-1], RIGHT)
        self.play(Write(error))
        
        # Animate error propagating backwards
        for i in range(len(layers)-1, 0, -1):
            if isinstance(layers[i], VGroup):
                for neuron in layers[i]:
                    if isinstance(neuron, Circle):
                        # Create animation of error propagating backwards
                        pulse = Circle(radius=0.15, color=RED, fill_opacity=1)
                        pulse.move_to(neuron.get_center())
                        self.play(
                            pulse.animate.scale(0.1).set_opacity(0),
                            run_time=0.5
                        )
        
        # Show weight updates
        weight_update = Text("Updating Weights", font="Arial", color=GREEN).scale(0.6)
        weight_update.to_edge(RIGHT)
        self.play(Write(weight_update))
        
        self.wait(1)
        self.play(
            FadeOut(section_title),
            FadeOut(error),
            FadeOut(weight_update)
        )
from typing import Tuple, Dict

import matplotlib.pyplot as plt
import numpy as np
from logic import BayesLogic, Shannon_entropy

 
# Clase para representar una onda sinusoidal 
class TimeSeries:
    def __init__(self, amplitud: float, frecuencia: float, fase: float):
        self.amplitud = amplitud
        self.frecuencia = frecuencia
        self.fase = fase

    def evaluate(self, x: np.ndarray) -> np.ndarray:
        return self.amplitud * np.sin(2 * np.pi * self.frecuencia * x + self.fase)

    # Definir un valor ambiental (puedes ajustar este valor según tus necesidades)
    env_value = 0.8

    # Calcular los cosenos directores
    cos_x, cos_y, cos_z = calculate_cosines(entropy, env_value)

    # Usar los cosenos directores para calcular una medida adicional (por ejemplo, ángulo)
    angle = np.arctan2(cos_y, cos_x) * (180 / np.pi)  # Convertir a grados

    # Determinar la coherencia basada en los cosenos directores (esto es un ejemplo)
    coherence = (cos_x + cos_y + cos_z) / 3

    # Usar BayesLogic para determinar la acción a tomar
    probabilities = bayes_logic.calculate_probabilities_and_select_action(
        entropy=entropy,
        coherence=coherence,
        prn_influence=prn_influence,
        action=previous_action
    )

    action_to_take = probabilities["action_to_take"]

    # Simular el estado colapsado basado en la acción
    if action_to_take == 1:
    # Colapso hacia una fase específica (por ejemplo, 180 grados)
        estado_colapsado = np.pi  # 180 grados en radianes
    else:
    # Colapso hacia otra fase (por ejemplo, 0 grados)
        estado_colapsado = 0.5
    return estado_colapsado, action_to_take

    # Definir una simple wave function
def wave_function(x, t, amplitude=1.0, frequency=1.0, phase=0.5):
    """Defines a simple sinusoidal wave function."""
    return amplitude * np.sin(2 * np.pi * frequency * x - phase * t)


def visualize_wave_and_network(network, iteration, t):  # Added time parameter
    """Visualizes both the network state and the wave function."""

    # 1. Wave Function Plot
    x_wave = np.linspace(0, 10, 500)  # Adjust x range as needed
    y_wave = wave_function(x_wave, t)  # Evaluate wave function

    plt.figure(figsize=(12, 6))  # Larger figure for both plots
    plt.subplot(1, 2, 1)  # Subplot for the wave

    plt.plot(x_wave, y_wave, color='blue', label=f"Wave at t={t:.2f}")  # label added
    plt.xlabel("x")
    plt.ylabel("ψ(x)")
    plt.title("Wave Function")
    plt.grid()
    plt.legend()  # show label

    # 2. Network State Plot
    plt.subplot(1, 2, 2)  # Subplot for the network
    for layer_index, layer in enumerate(network):
        for node_index, node in enumerate(layer):
           if is_active(node):
             plt.scatter(layer_index, node_index)

    plt.title(f"Network State at Iteration {iteration}")
    plt.xlabel("Layer Index")
    plt.ylabel("Node Index")
    plt.xlim(-1, len(network))
    plt.ylim(-1, max(len(layer) for layer in network))
    plt.grid()

    plt.tight_layout()  # Adjust subplot params for a tight layout
    plt.show()


def visualize_network(network, iteration):
    """
    Visualizes the network state using matplotlib.
    Args:
        network: The network to visualize.
    """
    plt.figure(figsize=(8, 6))
    for layer_index, layer in enumerate(network):
        for node_index, node in enumerate(layer):
            if is_active(node):
                plt.scatter(layer_index, node_index, color='red', marker='o')

    plt.title(f"Network State at Iteration {iteration}")
    plt.xlabel("Layer Index")
    plt.ylabel("Node Index")
    plt.xlim(-1, len(network))
    plt.ylim(-1, max(len(layer) for layer in network))
    plt.grid()
    plt.show()
    visualize_wave_and_network(network, iteration, t)  # added time t.


# Run simulation
network = [[initialize_node() for _ in range(n)] for n in [2, 3, 2, 2]]
average = np.array([1.0, 0.1]) #Example average for Mahalanobis
covariance = np.cov(np.random.rand(10,2)) #Example covariance matrix
for iteration in range(10):
    t = iteration + 0.1
    visualize_network(network, iteration)
    visualize_wave_and_network(network, iteration, t)

for layer in network:
    for node in layer:
        print("Node Norm:", np.linalg.norm(node))

print(network) #Uncomment for debugging
print(qc.measure_active()) #Uncomment for debugging
if __name__ == "__main__":
    # Parámetros de las ondas
    amplitud = 0.5
    frecuencia = 1.5
    fase = -np.pi / 21

    # Crear las ondas
    onda_incidente = TimeSeries(amplitud, frecuencia, fase)
    onda_reflejada = TimeSeries(amplitud, frecuencia, fase + np.pi)  # Fase invertida para onda reflejada

    # Generar los valores de x
    x = np.linspace(0, 10, 500)

    # Evaluar las ondas en los puntos x
    y_incidente = onda_incidente.evaluate(x)
    y_reflejada = onda_reflejada.evaluate(x)

    # Superposición de las ondas
    y_superpuesta = y_incidente + y_reflejada

    # Instanciar BayesLogic y PRN
    bayes_logic = BayesLogic()
    prn = PRN(influence=0.5)

    # Acción previa (puede ser 0 o 1)
    previous_action = 1

    # Simular el colapso de onda
    estado_colapsado, selected_action = colapso_onda(y_superpuesta, bayes_logic, prn_influence=prn.influence,
                                                     previous_action=previous_action)

# Mostrar la información calculada 
    entropy = shannon_entropy(y_superpuesta)
    cos_x, cos_y, cos_z = calculate_cosines(entropy, 0.8)
    angle = np.arctan2(cos_y, cos_x) * (180 / np.pi)
    coherence = (cos_x + cos_y + cos_z) / 3

    print(f"Entropía de Shannon: {entropy:.4f}")
    print(f"Cosenos Directores: cos_x = {cos_x:.4f}, cos_y = {cos_y:.4f}, cos_z = {cos_z:.4f}")
    print(f"Ángulo calculado: {angle:.2f} grados")
    print(f"Coherencia: {coherence:.4f}")
    print(f"Acción seleccionada: {'Mover Derecha' if selected_action == 1 else 'Mover Izquierda'}")
    print(f"Estado colapsado: {'180 grados' if estado_colapsado == np.pi else '0 grados'}")

    # Graficar las ondas
    plt.figure(figsize=(12, 6))
    plt.plot(x, y_incidente, label="Onda Incidente", color="blue")
    plt.plot(x, y_reflejada, label="Onda Reflejada", color="red")
    plt.plot(x, y_superpuesta, label="Onda Superpuesta", color="green")

    # Graficar el estado colapsado como una línea vertical
    if estado_colapsado == np.pi:
        plt.axvline(x=5, color='purple', linestyle='--', label="Estado Colapsado: 180°")
    else:
        plt.axvline(x=5, color='orange', linestyle='--', label="Estado Colapsado: 0°")

    plt.xlabel("x")
    plt.ylabel("ψ(x)")
    plt.title("Superposición y Colapso de Ondas")
    plt.grid(True)
    plt.legend()
    plt.show()

    # Graficar las ondas sin el estado colapsado
    plt.figure(figsize=(12, 6))
    plt.plot(x, y_incidente, label="Onda Incidente", color="blue")
    plt.plot(x, y_reflejada, label="Onda Reflejada", color="red")
    plt.plot(x, y_superpuesta, label="Onda Superpuesta", color="green")
    plt.xlabel("x")
    plt.ylabel("ψ(x)")
    plt.title("Superposición de Ondas")
    plt.grid(True)
    plt.legend()
    plt.show()
    
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

n = 13
alpha_deg = 10 * (n + 1)
alpha_rad = np.deg2rad(alpha_deg)
center_of_rotation = np.array([480, 480])

def get_rotation_matrix(alpha, center):
    cos_a = np.cos(alpha)
    sin_a = np.sin(alpha)
    rotation_matrix = np.array([
        [cos_a, -sin_a],
        [sin_a, cos_a]
    ])
    translation_matrix = np.array([
        center - center @ rotation_matrix
    ]).T
    return rotation_matrix, translation_matrix

def load_dataset(file_path):
    dataset = np.loadtxt(file_path, dtype=int)
    return dataset

def apply_affine_transformation(dataset, rotation_matrix, translation_matrix):
    transformed_data = (dataset @ rotation_matrix.T) + translation_matrix.T
    return transformed_data

def plot_data(original_data, transformed_data):
    plt.figure(figsize=(9.6, 9.6))
    plt.scatter(original_data[:, 0], original_data[:, 1], color='blue', label='Original')
    plt.scatter(transformed_data[:, 0], transformed_data[:, 1], color='red', label='Transformed')
    plt.legend()
    plt.title(f'Affine Transformation (Rotation by {alpha_deg}°)')
    plt.show()

def main():
    current_dir = Path(__file__).parent
    dataset_path = current_dir / 'DS3.txt'
    dataset = load_dataset(dataset_path)
    rotation_matrix, translation_matrix = get_rotation_matrix(alpha_rad, center_of_rotation)
    transformed_dataset = apply_affine_transformation(dataset, rotation_matrix, translation_matrix)
    output_path = current_dir / "transformed_data.txt"
    np.savetxt(output_path, transformed_dataset, fmt="%d")
    plot_data(dataset, transformed_dataset)

if __name__ == "__main__":
    main()

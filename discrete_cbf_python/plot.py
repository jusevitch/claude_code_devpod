#!/usr/bin/env python3
"""
Plot the trajectory from the single-integrator simulation.
Usage: python plot.py [trajectory_file.npz] [--output-base output_name]
"""

import numpy as np
import matplotlib.pyplot as plt
import argparse
from pathlib import Path

def plot_trajectory(filename="trajectory.npz", output_base=None):
    """Load and plot the trajectory from the simulation."""
    
    # Load the data
    try:
        data = np.load(filename)
        trajectory = data['trajectory']
        x = data['x']
        y = data['y']
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return
    except KeyError as e:
        print(f"Error: Expected data not found in file. Missing: {e}")
        return
    
    # Determine output file names
    if output_base is None:
        # Use input filename without extension as base
        output_base = Path(filename).stem
    
    # Extract start from trajectory
    start = trajectory[0]
    
    # Create figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), dpi=100)
    
    # Plot 1: 2D trajectory in state space
    ax1.plot(x, y, 'b-', linewidth=2, label='Trajectory', alpha=0.7)
    ax1.plot(x, y, 'b.', markersize=3, alpha=0.3)  # Show discrete points
    ax1.plot(start[0], start[1], 'go', markersize=12, label='Start', markeredgecolor='darkgreen', markeredgewidth=2)
    ax1.plot(x[-1], y[-1], 'ro', markersize=12, label='Final', markeredgecolor='darkred', markeredgewidth=2)
    
    # Add arrow to show direction
    n_arrows = min(10, len(x) // 5)
    indices = np.linspace(0, len(x)-2, n_arrows, dtype=int)
    for i in indices:
        dx = x[i+1] - x[i]
        dy = y[i+1] - y[i]
        ax1.arrow(x[i], y[i], dx*0.5, dy*0.5, head_width=0.05, 
                 head_length=0.05, fc='blue', ec='blue', alpha=0.5)
    
    ax1.set_xlabel('$x_1$', fontsize=12)
    ax1.set_ylabel('$x_2$', fontsize=12)
    ax1.set_title('2D Trajectory in State Space', fontsize=14)
    ax1.grid(True, alpha=0.3)
    ax1.legend(loc='best')
    ax1.axis('equal')
    
    # Plot 2: Time evolution of states
    time_steps = np.arange(len(x))
    
    ax2.plot(time_steps, x, 'b-', linewidth=2, label='$x_1(k)$')
    ax2.plot(time_steps, y, 'r-', linewidth=2, label='$x_2(k)$')
    ax2.axhline(y=x[-1], color='b', linestyle='--', alpha=0.3, label=f'Final $x_1$ = {x[-1]:.3f}')
    ax2.axhline(y=y[-1], color='r', linestyle='--', alpha=0.3, label=f'Final $x_2$ = {y[-1]:.3f}')
    
    ax2.set_xlabel('Time Step $k$', fontsize=12)
    ax2.set_ylabel('State Value', fontsize=12)
    ax2.set_title('State Evolution Over Time', fontsize=14)
    ax2.grid(True, alpha=0.3)
    ax2.legend(loc='best')
    
    # Add statistics text box
    stats_text = "Simulation Statistics:\n"
    stats_text += f"Steps: {len(x)}\n"
    stats_text += f"Start: [{start[0]:.3f}, {start[1]:.3f}]\n"
    stats_text += f"Final: [{x[-1]:.3f}, {y[-1]:.3f}]\n"
    distance_traveled = np.sum(np.sqrt(np.diff(x)**2 + np.diff(y)**2))
    stats_text += f"Path length: {distance_traveled:.3f}"
    
    fig.text(0.5, 0.02, stats_text, ha='center', fontsize=10, 
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.suptitle('Single-Integrator System with Proportional Control', fontsize=16, y=1.02)
    plt.tight_layout()
    
    # Save figures in high quality
    png_filename = f"{output_base}.png"
    svg_filename = f"{output_base}.svg"
    pdf_filename = f"{output_base}.pdf"
    
    # Save as PNG with high DPI (300)
    print(f"Saving high-quality PNG to '{png_filename}'...")
    fig.savefig(png_filename, dpi=300, bbox_inches='tight', pad_inches=0.1)
    
    # Save as SVG (vector format)
    print(f"Saving vector format SVG to '{svg_filename}'...")
    fig.savefig(svg_filename, format='svg', bbox_inches='tight', pad_inches=0.1)
    
    # Save as PDF (vector format)
    print(f"Saving vector format PDF to '{pdf_filename}'...")
    fig.savefig(pdf_filename, format='pdf', bbox_inches='tight', pad_inches=0.1)
    
    plt.show()
    
    # Print some statistics
    print("\n=== Trajectory Statistics ===")
    print(f"Number of steps: {len(x)}")
    print(f"Start position: [{start[0]:.3f}, {start[1]:.3f}]")
    print(f"Final position: [{x[-1]:.3f}, {y[-1]:.3f}]")
    print(f"Total path length: {distance_traveled:.3f}")
    
    # Check convergence
    final_velocities = np.sqrt(np.diff(x[-10:])**2 + np.diff(y[-10:])**2)
    avg_final_velocity = np.mean(final_velocities)
    print(f"Average velocity (last 10 steps): {avg_final_velocity:.6f}")
    
    if avg_final_velocity < 0.01:
        print("System appears to have converged to the goal.")
    else:
        print("System is still moving significantly.")
    
    print("\n=== Files Saved ===")
    print(f"PNG: {png_filename} (300 DPI)")
    print(f"SVG: {svg_filename} (vector format)")
    print(f"PDF: {pdf_filename} (vector format)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot trajectory from single-integrator simulation")
    parser.add_argument("trajectory_file", nargs="?", default="trajectory.npz",
                        help="Input trajectory file (default: trajectory.npz)")
    parser.add_argument("--output-base", "-o", default=None,
                        help="Base name for output files (default: use input filename)")
    
    args = parser.parse_args()
    plot_trajectory(args.trajectory_file, args.output_base)
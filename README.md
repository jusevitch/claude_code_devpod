# 2D Single-Integrator System Simulator

A Rust implementation of a discrete-time 2D single-integrator system with proportional control.

## System Description

The system implements the following discrete-time dynamics:
- **State update**: `x[k+1] = x[k] + dt * u[k]`
- **Control law**: `u[k] = 2(g - x[k])`

Where:
- `x[k]` is the 2D state vector at time step k
- `u[k]` is the control input
- `g` is the goal location
- `dt` is the time step size

The proportional controller drives the system toward the goal location with a gain of 2.

## Building the Project

1. Ensure you have Rust installed (https://rustup.rs/)
2. Clone/create the project with the provided files
3. Build the project:
```bash
cargo build --release
```

## Running the Simulator

The simulator accepts the following command-line arguments:

```bash
cargo run --release -- \
    --num-steps 100 \
    --dt 0.1 \
    --goal-x 5.0 \
    --goal-y 5.0 \
    --start-x 0.0 \
    --start-y 0.0 \
    --output trajectory.npz
```

### Arguments

- `-n, --num-steps`: Number of simulation steps
- `-d, --dt`: Step size (time increment between steps)
- `--goal-x`: Goal location x-coordinate
- `--goal-y`: Goal location y-coordinate
- `--start-x`: Start location x-coordinate
- `--start-y`: Start location y-coordinate
- `-o, --output`: Output file path (default: "trajectory.npz")

### Example Commands

**Basic simulation:**
```bash
cargo run --release -- -n 100 -d 0.1 --goal-x 10.0 --goal-y 10.0 --start-x 0.0 --start-y 0.0
```

**Fast convergence with small time steps:**
```bash
cargo run --release -- -n 500 -d 0.01 --goal-x 5.0 --goal-y 3.0 --start-x -2.0 --start-y -1.0
```

**Slow motion with large time steps:**
```bash
cargo run --release -- -n 50 -d 0.5 --goal-x 8.0 --goal-y 6.0 --start-x 1.0 --start-y 1.0
```

## Output Format

The simulator saves the trajectory in NumPy's `.npz` format with three arrays:
- `trajectory`: (N+1) × 2 array containing the complete state history
- `x`: 1D array of x-coordinates
- `y`: 1D array of y-coordinates

## Visualizing Results

Use the provided Python script to visualize the trajectory:

```bash
python plot_trajectory.py trajectory.npz
```

Requirements for the Python script:
```bash
pip install numpy matplotlib
```

## Control Theory Background

The proportional controller `u[k] = 2(g - x[k])` implements a simple feedback law where:
- The control input is proportional to the error (distance from goal)
- The gain of 2 determines the convergence rate
- For a single integrator, this controller is globally asymptotically stable

The closed-loop dynamics become:
```
x[k+1] = x[k] + dt * 2(g - x[k])
       = x[k] + 2*dt*g - 2*dt*x[k]
       = (1 - 2*dt)*x[k] + 2*dt*g
```

For stability, we need `|1 - 2*dt| < 1`, which gives us `0 < dt < 1`. 

With `dt` in this range, the system converges exponentially to the goal.

## Performance Characteristics

- **Convergence rate**: Exponential with time constant τ = 1/2
- **Settling time**: Approximately 3τ = 1.5 seconds (to reach ~95% of goal)
- **No overshoot**: The system approaches the goal monotonically
- **Steady-state error**: Zero (system converges exactly to the goal)

## Tips for Usage

1. **Choosing dt**: 
   - Smaller dt → more accurate simulation but more steps needed
   - Larger dt → faster simulation but less accuracy
   - Must satisfy dt < 1 for stability

2. **Number of steps**:
   - Total simulation time = num_steps × dt
   - For full convergence, use simulation time > 2 seconds

3. **Initial conditions**:
   - System works for any initial position
   - Farther starts require more time to converge
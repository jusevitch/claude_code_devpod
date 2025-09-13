use clap::Parser;
use ndarray::{Array1, Array2};
use ndarray_npy::NpzWriter;
use std::fs::File;
use std::io::BufWriter;

/// CLI for 2D single-integrator system simulation
#[derive(Parser, Debug)]
#[command(author, version, about, long_about = None)]
struct Args {
    /// Number of simulation steps
    #[arg(short = 'n', long, default_value = "100")]
    num_steps: usize,

    /// Step size (dt)
    #[arg(short = 'd', long, default_value = "0.1")]
    dt: f64,

    /// Goal location x-coordinate
    #[arg(long = "goal-x", default_value = "0.0")]
    goal_x: f64,

    /// Goal location y-coordinate
    #[arg(long = "goal-y", default_value = "0.0")]
    goal_y: f64,

    /// Start location x-coordinate
    #[arg(long = "start-x", default_value = "5.0")]
    start_x: f64,

    /// Start location y-coordinate
    #[arg(long = "start-y", default_value = "5.0")]
    start_y: f64,

    /// Output file path (defaults to "trajectory.npz")
    #[arg(short = 'o', long, default_value = "trajectory.npz")]
    output: String,
}

/// Compute the control input u[k] = 2(g - x[k])
fn compute_control(goal: &Array1<f64>, state: &Array1<f64>) -> Array1<f64> {
    2.0 * (goal - state)
}

/// Update the state using discrete-time dynamics: x[k+1] = x[k] + dt*u[k]
fn update_state(state: &Array1<f64>, control: &Array1<f64>, dt: f64) -> Array1<f64> {
    state + dt * control
}

/// Run the simulation for the specified number of steps
fn simulate(
    start: Array1<f64>,
    goal: Array1<f64>,
    dt: f64,
    num_steps: usize,
) -> Array2<f64> {
    // Initialize state history matrix (num_steps + 1) x 2
    // +1 to include the initial state
    let mut history = Array2::<f64>::zeros((num_steps + 1, 2));
    
    // Set initial state
    let mut state = start.clone();
    history.row_mut(0).assign(&state);
    
    // Simulation loop
    for k in 0..num_steps {
        // Compute control input
        let control = compute_control(&goal, &state);
        
        // Update state
        state = update_state(&state, &control, dt);
        
        // Store in history
        history.row_mut(k + 1).assign(&state);
    }
    
    history
}

/// Save trajectory to NumPy-readable file
fn save_trajectory(history: &Array2<f64>, filename: &str) -> Result<(), Box<dyn std::error::Error>> {
    let file = File::create(filename)?;
    let writer = BufWriter::new(file);
    let mut npz = NpzWriter::new(writer);
    
    // Save the trajectory with name "trajectory"
    npz.add_array("trajectory", history)?;
    
    // Also save individual x and y coordinates for convenience
    let x_coords = history.column(0).to_owned();
    let y_coords = history.column(1).to_owned();
    npz.add_array("x", &x_coords)?;
    npz.add_array("y", &y_coords)?;
    
    npz.finish()?;
    Ok(())
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Parse command line arguments
    let args = Args::parse();
    
    // Create start and goal vectors
    let start = Array1::from_vec(vec![args.start_x, args.start_y]);
    let goal = Array1::from_vec(vec![args.goal_x, args.goal_y]);
    
    // Print simulation parameters
    println!("=== 2D Single-Integrator System Simulation ===");
    println!("Start location: [{:.3}, {:.3}]", args.start_x, args.start_y);
    println!("Goal location: [{:.3}, {:.3}]", args.goal_x, args.goal_y);
    println!("Number of steps: {}", args.num_steps);
    println!("Step size (dt): {:.3}", args.dt);
    println!("Total simulation time: {:.3} seconds", args.num_steps as f64 * args.dt);
    println!();
    
    // Run simulation
    println!("Running simulation...");
    let history = simulate(start, goal.clone(), args.dt, args.num_steps);
    
    // Get final state for reporting
    let final_state = history.row(args.num_steps);
    let final_error = (goal[0] - final_state[0]).hypot(goal[1] - final_state[1]);
    
    println!("Simulation complete!");
    println!("Final state: [{:.3}, {:.3}]", final_state[0], final_state[1]);
    println!("Final error (distance to goal): {:.6}", final_error);
    
    // Save to file
    println!("Saving trajectory to '{}'...", args.output);
    save_trajectory(&history, &args.output)?;
    println!("Saved successfully!");
    
    Ok(())
}
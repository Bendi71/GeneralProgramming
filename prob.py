import NonogramSolver as ns

# Create a Nonogram instance
nonogram = ns.Nonogram((15,15))

# Generate a random nonogram
nonogram.generate_random_nonogram()

# Solve the nonogram
nonogram.solve()

# Print the difference
nonogram.print_difference()

# File paths
input_file = 'hub.csv'
output_file = 'sample-steps.txt'

def timestamp_to_milliseconds(timestamp):
    """
    Converts a timestamp in the format MM:SS.MMM or M:SS.MMM into total milliseconds.
    
    Args:
        timestamp (str): The timestamp string (e.g., "10:29.824").
    
    Returns:
        int: Total milliseconds.
    """
    try:
        # Split the timestamp into minutes, seconds, and milliseconds
        minutes, rest = timestamp.split(":")
        seconds, milliseconds = rest.split(".")
        
        # Convert each component to integers
        minutes = int(minutes)
        seconds = int(seconds)
        milliseconds = int(milliseconds)
        
        # Calculate total milliseconds
        total_milliseconds = (minutes * 60 * 1000) + (seconds * 1000) + milliseconds
        return total_milliseconds
    except ValueError:
        # Return None if the timestamp is invalid
        return None

RESET_SEEK = "reset-seek"

# Open and read the input file as a string
with open(input_file, 'r') as f:
    data = f.read()

# Split the string into rows
lines = data.splitlines()
output_lines = []

# Parse the lines into a list of steps and values
rows = []
for line in lines:
    # Split the line into columns using ,s
    columns = line.split(',')
    
    # Ensure the row has enough columns and try converting to integers
    try:
        step = int(columns[1].strip())
        value = timestamp_to_milliseconds(columns[2].strip())
        rest = columns[4].strip()
        if(rest != ""):
            rest = RESET_SEEK
        rows.append((step, value, rest))
    except (IndexError, ValueError):
        # Skip rows that don't have enough data or have invalid integers
        continue

# Generate the output based on the "next value" logic
base = 0
prevNextValue = 0
for i in range(len(rows) - 1):  # Stop one before the last row
    resetInfo = ""
    if(rows[i][2] == RESET_SEEK and i >0):
        base = rows[i][1]
        resetInfo = str(prevNextValue) + " "+RESET_SEEK+" "
    current_step, _, _ = rows[i]
    _, next_value, _ = rows[i + 1]
    differenceToDisplay = int(next_value)-base
    output_lines.append(f"{current_step}, {resetInfo}{differenceToDisplay};")
    prevNextValue = differenceToDisplay

# Write the output file
with open(output_file, 'w') as f:
    f.write("\n".join(output_lines))

print(f"Output written to {output_file}")

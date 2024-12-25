#!/usr/bin/env python

def evaluate_gate(gate_type, input1, input2):
    """Evaluates the output of a single logic gate."""
    if gate_type == "AND":
        return input1 & input2
    elif gate_type == "OR":
        return input1 | input2
    elif gate_type == "XOR":
        return input1 ^ input2
    else:
        raise ValueError(f"Unknown gate type: {gate_type}")

def parse_input(lines):
    """Parses input lines into initial values and gates."""
    initial_values = {}
    gates = []

    for line in lines:
        if ":" in line:  # Initial value
            wire, value = line.split(": ")
            initial_values[wire.strip()] = int(value)
        elif "->" in line:  # Gate definition
            gates.append(line.strip())

    return initial_values, gates

def simulate_system(initial_values, gates):
    """Simulates the gates and computes the decimal output."""
    wires = initial_values.copy()  # Start with initial wire values
    remaining_gates = gates.copy()  # Gates that still need processing

    # Tracking status of wires
    wire_status = {}  # {wire: status_message}

    while remaining_gates:
        progress = False  # Track if any gate was processed in this iteration

        for gate in remaining_gates[:]:  # Process a copy of the list
            parts = gate.split(" ")
            if "AND" in parts:
                wire1, _, wire2, _, output = parts
                if wire1 in wires and wire2 in wires:
                    wires[output] = evaluate_gate("AND", wires[wire1], wires[wire2])
                    wire_status[output] = f"Assigned {wires[output]}"
                    remaining_gates.remove(gate)
                    progress = True
                else:
                    wire_status[output] = "Rejected (missing inputs)"
            elif "OR" in parts:
                wire1, _, wire2, _, output = parts
                if wire1 in wires and wire2 in wires:
                    wires[output] = evaluate_gate("OR", wires[wire1], wires[wire2])
                    wire_status[output] = f"Assigned {wires[output]}"
                    remaining_gates.remove(gate)
                    progress = True
                else:
                    wire_status[output] = "Rejected (missing inputs)"
            elif "XOR" in parts:
                wire1, _, wire2, _, output = parts
                if wire1 in wires and wire2 in wires:
                    wires[output] = evaluate_gate("XOR", wires[wire1], wires[wire2])
                    wire_status[output] = f"Assigned {wires[output]}"
                    remaining_gates.remove(gate)
                    progress = True
                else:
                    wire_status[output] = "Rejected (missing inputs)"

        if not progress:
            break  # Exit if no progress is made in this iteration

    # Extract binary number from wires starting with 'z', sorted by numerical index
    binary_number = ""
    z_keys = sorted((k for k in wires if k.startswith("z")), key=lambda x: int(x[1:]))
    for key in z_keys:
        binary_number = str(wires[key]) + binary_number  # Add least significant bit first

    # Print the binary number
    print(f"\nBinary number: {binary_number}")

    # Append status to all wires
    print("\nWire Status:")
    for wire, status in wire_status.items():
        print(f"{wire}: {status}")

    # Convert binary to decimal
    return int(binary_number, 2)

if __name__ == "__main__":
    # Replace this with your input file path
    from util import read_input
    lines = read_input("../aoc_data/day24_data.txt")

    # Parse the input into initial values and gates
    initial_values, gates = parse_input(lines)

    # Debugging initial parsed data
    print(f"Initial values: {initial_values}")
    print(f"Initial gates: {gates}")

    # Simulate the system
    decimal_output = simulate_system(initial_values, gates)

    # Print the final result
    print(f"Decimal output: {decimal_output}")
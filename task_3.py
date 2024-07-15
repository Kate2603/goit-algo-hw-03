def hanoi(n, from_pole, to_pole, aux_pole, poles):
    if n == 1:
        print(f"Move disk 1 from {from_pole} to {to_pole}")
        poles[to_pole].append(poles[from_pole].pop())
        print_state(poles)
        return
    hanoi(n-1, from_pole, aux_pole, to_pole, poles)
    print(f"Move disk {n} from {from_pole} to {to_pole}")
    poles[to_pole].append(poles[from_pole].pop())
    print_state(poles)
    hanoi(n-1, aux_pole, to_pole, from_pole, poles)

def print_state(poles):
    print("State:", {k: v[:] for k, v in poles.items()})

def main(n):
    poles = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
    print_state(poles)
    hanoi(n, 'A', 'C', 'B', poles)
    print_state(poles)

if __name__ == "__main__":
    n = int(input("Enter the number of disks: "))
    main(n)
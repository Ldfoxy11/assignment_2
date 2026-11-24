A = [1, 2, 3, 4, 5]
N = 5

def input_matrix():
    print("Enter 5x5 matrix (row by row, 0 or 1 separated by space):")
    m = []
    for i in range(N):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        m.append(row)
    return m

def print_matrix(m):
    for row in m:
        print(" ".join(map(str, row)))

def is_reflexive(m):
    for i in range(N):
        if m[i][i] != 1:
            return False
    return True

def is_symmetric(m):
    for i in range(N):
        for j in range(N):
            if m[i][j] != m[j][i]:
                return False
    return True

def is_transitive(m):
    for i in range(N):
        for j in range(N):
            if m[i][j] == 1:
                for k in range(N):
                    if m[j][k] == 1 and m[i][k] != 1:
                        return False
    return True

def check_equivalence(m):
    r = is_reflexive(m)
    s = is_symmetric(m)
    t = is_transitive(m)
    print(f"Reflexive: {r}, Symmetric: {s}, Transitive: {t}")
    if r and s and t:
        print("-> This is an equivalence relation.")
        return True
    else:
        print("-> This is NOT an equivalence relation.")
        return False

def get_eq_class(m, x):
    idx = x - 1
    res = []
    for j in range(N):
        if m[idx][j] == 1:
            res.append(A[j])
    return res

def print_eq_classes(m):
    print("Equivalence classes:")
    for x in A:
        print(f"[{x}] = {get_eq_class(m, x)}")

def reflexive_closure(m):
    res = [row[:] for row in m]
    for i in range(N):
        res[i][i] = 1
    return res

def symmetric_closure(m):
    res = [row[:] for row in m]
    for i in range(N):
        for j in range(N):
            if res[i][j] == 1:
                res[j][i] = 1
    return res

def transitive_closure(m):
    res = [row[:] for row in m]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if res[i][k] == 1 and res[k][j] == 1:
                    res[i][j] = 1
    return res

def print_partition(m):
    parts = []
    for x in A:
        c = get_eq_class(m, x)
        if c not in parts:
            parts.append(c)
    print("Partition:", parts)

def main():
    m = input_matrix()
    print("\nInput Matrix:")
    print_matrix(m)
    print()

    if check_equivalence(m):
        print_eq_classes(m)
        print_partition(m)
    else:
        if not is_reflexive(m):
            print("\n--- Reflexive Closure ---")
            print("Before:")
            print_matrix(m)
            rm = reflexive_closure(m)
            print("After:")
            print_matrix(rm)
            if check_equivalence(rm):
                print_eq_classes(rm)

        if not is_symmetric(m):
            print("\n--- Symmetric Closure ---")
            print("Before:")
            print_matrix(m)
            sm = symmetric_closure(m)
            print("After:")
            print_matrix(sm)
            if check_equivalence(sm):
                print_eq_classes(sm)

        if not is_transitive(m):
            print("\n--- Transitive Closure ---")
            print("Before:")
            print_matrix(m)
            tm = transitive_closure(m)
            print("After:")
            print_matrix(tm)
            if check_equivalence(tm):
                print_eq_classes(tm)

        print("\n--- Equivalence Closure (Extra Feature) ---")
        eq_m = transitive_closure(symmetric_closure(reflexive_closure(m)))
        print_matrix(eq_m)
        if check_equivalence(eq_m):
            print_eq_classes(eq_m)
            print_partition(eq_m)

if __name__ == "__main__":
    main()

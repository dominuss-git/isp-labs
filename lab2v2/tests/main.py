import numpy as np


def find_max(a: np.array, n: int):
    maximum = abs(a[0][1])
    i_max = 0
    j_max = 1

    for i in range(n - 1):
        for j in range(i + 1, n):
            if maximum < abs(a[i][j]):
                maximum = a[i][j]
                i_max, j_max = i, j

    return maximum, i_max, j_max


def jacobi(a: np.array, n: int, eps: float):
    converge = False
    iteration = 0
    v_res = np.zeros((n, n))
    while not converge:

        maximum, i_max, j_max = find_max(a, n)

        v = np.eye(n)
        if a[i_max][i_max] != a[j_max][j_max]:
            pk = (2.0 * maximum) / (a[i_max][i_max] - a[j_max][j_max])
            fi = 0.5 * np.arctan(pk)
        else:
            fi = np.pi / 4

        v[i_max][i_max] = v[j_max][j_max] = np.cos(fi)
        v[i_max][j_max] = - np.sin(fi)
        v[j_max][i_max] = np.sin(fi)

        if iteration > 0:
            v_res = np.dot(v_res, v)
        else:
            v_res = v

        a = np.dot(np.transpose(v), a)
        a = np.dot(a, v)

        iteration += 1
        converge = abs(find_max(a, n)[0]) < eps

    return a, v_res


def print_self(a: np.array, values, vectors, n):
    print("Исходная матрица:\n")
    for item in a:
        print(item)
    print("\nСобственные значения: \n" + str(np.diag(values)))
    print("\nСобственные весторы:")
    for i in range(n):
        print(f"x[{i + 1}] = {vectors[:, i]}")


def main():
    C = np.array(
        [
            (0.2, 0, 0.2, 0, 0),
            (0, 0.2, 0, 0.2, 0),
            (0.2, 0, 0.2, 0, 0.2),
            (0, 0.2, 0, 0.2, 0),
            (0, 0, 0.2, 0, 0.2)
        ]
    )

    D = np.array(
        [
            (2.33, 0.81, 0.67, 0.92, -0.53),
            (0.81, 2.33, 0.81, 0.67, 0.92),
            (0.67, 0.81, 2.33, 0.81, 0.92),
            (0.92, 0.67, 0.81, 2.33, -0.53),
            (-0.53, 0.92, 0.92, -0.53, 2.33)
        ]
    )

    a = np.array(C) * int(input("Enter the variant:")) + np.array(D)
    n = len(a)

    values, vectors = jacobi(a, n, 0.0001)
    print_self(a, values, vectors, n)


if __name__ == '__main__':
    main()

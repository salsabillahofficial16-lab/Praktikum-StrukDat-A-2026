# def floyd_warshall(matrix_awal, n):
#     M = math.inf

#     q = [row[:] for row in matrix_awal]
#     r = [[0]*n for _ in range(n+1)]

#     for k in range(1, n +1):
#         for i in range(1, n +1):
#             for j in range(1, n+1):
#                 via_k = q[i][k] + q[k][j]
#                 if via_k < q[i][j]: 
#                     q[i][j] = via_k
#                     r[i][j] = k if r[k][j] == 0 else r[k][j]

# def baca_rute_fw(r, start, end):
#     stack = []
#     j = end

#     while r[start][j] != 0:
#         stack.append(j)
#         j = r[start][j]
    
#     rute = [strat]
#     while stack:
#         rute.append(stack.pop())
#     rute.append(end)
#     return rute

 
import math
import heapq

def dijkstra_matrix(matrix, n, start, end):
    """
    Algoritma Dijkstra menggunakan Adjacency Matrix.
    matrix : list 2D berbobot, math.inf = tidak ada edge
    n      : jumlah node
    start  : node asal
    end    : node tujuan
    """
    M = math.inf

    Q = [M] * (n + 1)     # Q[i] = jarak terpendek dari start ke i
    R = [0] * (n + 1)     # R[i] = node sebelumnya (untuk rekonstruksi jalur)
    Q[start] = 0

    pq   = [(0, start)]   # priority queue: (jarak, node)
    done = [False] * (n + 1)

    print("=" * 55)
    print(f"ALGORITMA DIJKSTRA: Node {start} ke Node {end}")
    print("=" * 55)

    while pq:
        jarak_min, CN = heapq.heappop(pq)   # CN = Current Node

        if done[CN]:
            continue
        done[CN] = True
        print(f"\nProses Node {CN} | beban min dari asal = {jarak_min}")

        if CN == end:
            print("  → Node tujuan ditemukan, selesai!")
            break

        # Baca baris CN di adjacency matrix untuk temukan tetangga
        for i in range(1, n + 1):
            if matrix[CN][i] != M and not done[i]:
                jarak_baru = Q[CN] + matrix[CN][i]
                if jarak_baru < Q[i]:
                    Q[i] = jarak_baru
                    R[i] = CN                          # catat node sebelumnya
                    heapq.heappush(pq, (jarak_baru, i))
                    print(f"  Update Node {i}: beban min = {jarak_baru}, sebelumnya = {CN}")

    # Rekonstruksi jalur dari matriks R (backtrack dari end ke start)
    jalur = []
    node  = end
    while node != 0:
        jalur.append(node)
        node = R[node]
    jalur.reverse()

    print(f"\n{'=' * 55}")
    if Q[end] == M:
        print(f"Tidak ada jalur dari {start} ke {end}!")
    else:
        print(f"Rute terpendek : {' -> '.join(map(str, jalur))}")
        print(f"Beban minimal  : {int(Q[end])}")

    return Q, R, jalur

# ── Adjacency matrix berbobot — contoh dari slide ──────────────
M = math.inf
n = 5
matrix_dijkstra = [
    [M, M, M, M, M, M],   # baris 0 tidak dipakai
    [M, M, 1, 3, M, M],   # node 1 -> 2 (bobot 1), 1 -> 3 (bobot 3)
    [M, M, M, 1, M, 5],   # node 2 -> 3 (bobot 1), 2 -> 5 (bobot 5)
    [M, 3, M, M, 2, M],   # node 3 -> 1 (bobot 3), 3 -> 4 (bobot 2)
    [M, M, M, M, M, 1],   # node 4 -> 5 (bobot 1)
    [M, M, M, M, M, M],   # node 5 -> (tidak ada)
]

Q, R, jalur = dijkstra_matrix(matrix_dijkstra, n, 1, 5)


import math

def floyd_warshall(matrix_awal, n):
    """
    Algoritma Floyd-Warshall.
    Input : adjacency matrix berbobot (M = math.inf jika tidak ada edge)
    Output: matriks jarak terpendek Q dan matriks rute R
    """
    M = math.inf

    # Salin matrix input agar tidak mengubah data asli
    Q = [row[:] for row in matrix_awal]
    R = [[0] * (n + 1) for _ in range(n + 1)]  # 0 = tidak ada perantara

    print("=" * 55)
    print("ALGORITMA FLOYD-WARSHALL")
    print("=" * 55)

    # Iterasi untuk setiap titik perantara k
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                via_k = Q[i][k] + Q[k][j]
                if via_k < Q[i][j]:
                    Q[i][j] = via_k
                    # Catat titik perantara untuk matriks rute
                    R[i][j] = k if R[k][j] == 0 else R[k][j]

    return Q, R

def tampilkan_matrix_fw(matrix, n, label=""):
    if label:
        print(f"\n{label}:")
    header = "    " + "  ".join([f" {j} " for j in range(1, n + 1)])
    print(header)
    print("    " + "-" * (n * 5))
    for i in range(1, n + 1):
        baris = []
        for j in range(1, n + 1):
            val = matrix[i][j]
            if val == math.inf:
                baris.append(" M ")
            else:
                baris.append(f" {int(val)} ")
        print(f" {i}  | {'  '.join(baris)}")

def baca_rute_fw(R, start, end):
    """
    Baca rute dari matriks R menggunakan teknik push-pop (stack).
    Nilai R[i][j] = titik perantara dari i menuju j.
    Nilai 0 = tidak ada perantara (jalur langsung).
    """
    stack = []
    j = end

    # Telusuri ke belakang, kumpulkan semua perantara ke stack
    while R[start][j] != 0:
        stack.append(R[start][j])
        j = R[start][j]

    # Pop stack untuk mendapatkan urutan yang benar
    rute = [start]
    while stack:
        rute.append(stack.pop())
    rute.append(end)
    return rute

# ── Contoh dari slide — graph 5 node berbobot ──────────────────
M = math.inf
n = 5
matrix_fw = [
    [M, M, M, M, M, M],   # baris 0 tidak dipakai
    [M, M, 1, 3, M, M],   # node 1 -> 2 (bobot 1), 1 -> 3 (bobot 3)
    [M, M, M, 1, M, 5],   # node 2 -> 3 (bobot 1), 2 -> 5 (bobot 5)
    [M, 3, M, M, 2, M],   # node 3 -> 1 (bobot 3), 3 -> 4 (bobot 2)
    [M, M, M, M, M, 1],   # node 4 -> 5 (bobot 1)
    [M, M, M, M, M, M],   # node 5 -> (tidak ada)
]

Q, R = floyd_warshall(matrix_fw, n)
tampilkan_matrix_fw(Q, n, "Matriks Beban Terpendek (Q)")
tampilkan_matrix_fw(R, n, "Matriks Rute (R)")

print(f"\nRute 1 ke 5   : {baca_rute_fw(R, 1, 5)}")
print(f"Jarak min 1→5 : {int(Q[1][5])}")
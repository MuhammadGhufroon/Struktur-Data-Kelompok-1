"""
PRAKTIKUM DOUBLY LINKED LIST -- TIPE A   (Soal 01 s.d. 11)
=====================================================================
Data awal tipe ini : ['A', 'B', 'C']
Catatan tipe       : Target berada di tengah list (3 node).

CARA KERJA
- Setiap nomor soal dikerjakan oleh SATU mahasiswa. Isi NIM & NAMA pada blok
  identitas milik nomor soal Anda, lalu tulis kode pada fungsi soal Anda
  (ganti baris `pass`). Jangan mengubah nama fungsi/parameter dan helper.py.
- Jalankan  python3 soal_tipe_A.py  untuk melihat hasil pengujian otomatis.

STRUKTUR OBJEK (ada di helper.py, tinggal dipakai)
    class Node:
        self.info  -> data node (mis. "A") [atau self.isi]
        self.prev  -> pointer ke node sebelumnya (None jika di ujung kiri)
        self.next  -> pointer ke node sesudahnya  (None jika di ujung kanan)

    class DoublyLinkedList:
        self.first -> pointer ke node paling depan (None jika list kosong) [atau self.head]
        self.last  -> pointer ke node paling belakang (None jika list kosong) [atau self.tail]

- Membuat node baru : P = Node("X")
- Pointer next dan prev HARUS konsisten (diperiksa otomatis dua arah).
"""

from helper import Node, DoublyLinkedList, jalankan_pengujian


# ======================================================================
# SOAL 01 -- Insert Empty Node
# ======================================================================
NIM_01 = "108102530006"
NAMA_01 = "BAIQ JIHAN KUSUMA"

def soal_01_insert_empty(dll, data):
    """
    Sisipkan node berisi "D" ke list yang masih KOSONG.
    Kondisi awal : KOSONG
    Hasil        : D

    PSEUDOCODE:
    P = Node(data)
    dll.first = P
    dll.last = P
    """
  P = Node(data)
    P.prev = None
    P.next = None
    dll.first = P
    dll.last = P

# ======================================================================
# SOAL 02 -- Insert First Node
# ======================================================================
NIM_02 = "ISI_NIM"
NAMA_02 = "ISI_NAMA"

def soal_02_insert_first(dll, data):
    """
    Sisipkan node "E" di posisi PALING DEPAN list.
    Kondisi awal : A <-> B <-> C
    Hasil        : E <-> A <-> B <-> C

    PSEUDOCODE:
    P = Node(data)
    P.next = dll.first
    dll.first.prev = P
    dll.first = P
    """
    pass  # <-- tulis kode Anda di sini


# ======================================================================
# SOAL 03 -- Insert Last Node
# ======================================================================
NIM_03 = "108102500031"
NAMA_03 = "NAUFALIA NAFISA"

def soal_03_insert_last(dll, data):
    """
    Sisipkan node "F" di posisi PALING BELAKANG list.
    Kondisi awal : A <-> B <-> C
    Hasil        : A <-> B <-> C <-> F

    PSEUDOCODE:
    P = Node(data)
    P.prev = dll.last
    dll.last.next = P
    dll.last = P
    """
    #Inisiasi node#

    n1 = Node("A")
    n2 = Node("B")
    n3 = Node("C")

    n1.next = n2
    n2.next = n3
    n2.prev = n1
    n3.prev = n2

    dll.first = n1
    dll.last = n3
    P = Node("F")
    P.prev = dll.last
    dll.last.next = P
    dll.last = P


# ======================================================================
# SOAL 04 -- Insert After Target Node
# ======================================================================
NIM_04 = "ISI_NIM"
NAMA_04 = "ISI_NAMA"

def soal_04_insert_after(dll, node_target, data):
    """
    Sisipkan node "G" tepat SETELAH node_target (node "B").
    Kondisi awal : A <-> B <-> C
    Hasil        : A <-> B <-> G <-> C

    PSEUDOCODE:
    P = Node(data)
    Q = node_target.next
    P.prev = node_target
    P.next = Q
    node_target.next = P
    Q.prev = P
    """
    pass  # <-- tulis kode Anda di sini

# ======================================================================
# SOAL 05 -- Insert Before Target Node
# ======================================================================
NIM_05 = "108102500034"
NAMA_05 = "Rayana Bintang Rahmanda"

def soal_05_insert_before(dll, node_target, data):
    """
    Sisipkan node "H" tepat SEBELUM node_target (node "B").
    Kondisi awal : A <-> B <-> C
    Hasil        : A <-> H <-> B <-> C

    PSEUDOCODE:
    P = Node(data)
    Q = node_target.prev
    P.next = node_target
    P.prev = Q
    node_target.prev = P
    Q.next = P
    """
    P = Node(data)
    Q = node_target.prev

    P.next = node_target
    P.prev = Q
    node_target.prev = P

    if Q is not None:
        Q.next = P
    else:
        dll.head = P
    return P# <-- tulis kode Anda di sini

# ======================================================================
# SOAL 06 -- Traverse Maju
# ======================================================================
NIM_06 = "ISI_NIM"
NAMA_06 = "ISI_NAMA"

def soal_06_traverse_maju(dll):
    """
    Telusuri list dari first ke last, kembalikan string info node dipisah " <-> ".
    Kondisi awal : A <-> B <-> C
    Hasil        : "A <-> B <-> C"

    PSEUDOCODE:
    hasil = ""
    P = dll.first
    WHILE P is not None:
        hasil = GABUNG_STRING(hasil, P.info)
        P = P.next
    RETURN hasil
    """
    pass # <-- tulis kode Anda di sini

# ======================================================================
# SOAL 07 -- Traverse Mundur
# ======================================================================
NIM_07 = "108102530010"
NAMA_07 = "SELFI NUR ASYIKIN"

def soal_07_traverse_mundur(dll):
    """
    Telusuri list dari last ke first, kembalikan string info node dipisah " <-> ".
    Kondisi awal : A <-> B <-> C
    Hasil        : "C <-> B <-> A"

    PSEUDOCODE:
    hasil = ""
    P = dll.last
    WHILE P is not None:
        hasil = GABUNG_STRING(hasil, P.info)
        P = P.prev
    RETURN hasil
    """
    hasil = ""
    P = dll.last

    while P is not None:
        if hasil == "":
            hasil = P.info
        else:
            hasil = hasil + " <-> " + P.info
        P = P.prev

    return hasil # <-- tulis kode Anda di sini

# ======================================================================
# SOAL 08 -- Search Target
# ======================================================================
NIM_08 = "ISI_NIM"
NAMA_08 = "ISI_NAMA"

def soal_08_search(dll, target):
    """
    Cari node berisi "B" dan kembalikan NODE-nya (bukan string). List tidak berubah.
    Kondisi awal : A <-> B <-> C
    Hasil        : node "B"

    PSEUDOCODE:
    P = dll.first
    WHILE P is not None:
        IF P.info == target:
            RETURN P
        P = P.next
    RETURN None
    """
    P = dll.first
    while P is not None:
        if P.info == target:
            return P
        P = P.next
    return None

# ======================================================================
# SOAL 09 -- Delete First Node
# ======================================================================
NIM_09 = "10810253007"
NAMA_09 = "LUQMAN SYARIF RAHMADANI"

def soal_09_delete_first(dll):
    """
    Hapus node PALING DEPAN dari list.
    Kondisi awal : A <-> B <-> C
    Hasil        : B <-> C

    PSEUDOCODE:
    dll.first = dll.first.next
    dll.first.prev = None
    """
    
    dll.first = dll.first.next
    dll.first.prev = None

# ======================================================================
# SOAL 10 -- Delete Last Node
# ======================================================================
NIM_10 = "ISI_NIM"
NAMA_10 = "ISI_NAMA"

def soal_10_delete_last(dll):
    """
    Hapus node PALING BELAKANG dari list.
    Kondisi awal : A <-> B <-> C
    Hasil        : A <-> B

    PSEUDOCODE:
    dll.last = dll.last.prev
    dll.last.next = None
    """
    pass  # <-- tulis kode Anda di sini

# ======================================================================
# SOAL 11 -- Delete Target Node
# ======================================================================
NIM_11 = "108102500052"
NAMA_11 = "TESSAGYANI DIVANTY TODE"

def soal_11_delete_node(dll, node_target):
    """
    Hapus node_target (node "B") dari list.
    Kondisi awal : A <-> B <-> C
    Hasil        : A <-> C

    PSEUDOCODE:
    P = node_target.prev
    Q = node_target.next
    P.next = Q
    Q.prev = P
    """
    P = node_target.prev
    Q = node_target.next
    P.next = Q
    Q.prev = P


if __name__ == "__main__":
    jalankan_pengujian(1, "Insert Empty Node", NAMA_01, NIM_01, soal_01_insert_empty,
                       [], ('D',), "D", "ubah")
    jalankan_pengujian(2, "Insert First Node", NAMA_02, NIM_02, soal_02_insert_first,
                       ['A', 'B', 'C'], ('E',), "E <-> A <-> B <-> C", "ubah")
    jalankan_pengujian(3, "Insert Last Node", NAMA_03, NIM_03, soal_03_insert_last,
                       ['A', 'B', 'C'], ('F',), "A <-> B <-> C <-> F", "ubah")
    jalankan_pengujian(4, "Insert After Target Node", NAMA_04, NIM_04, soal_04_insert_after,
                       ['A', 'B', 'C'], ('B', 'G'), "A <-> B <-> G <-> C", "ubah")
    jalankan_pengujian(5, "Insert Before Target Node", NAMA_05, NIM_05, soal_05_insert_before,
                       ['A', 'B', 'C'], ('B', 'H'), "A <-> H <-> B <-> C", "ubah")
    jalankan_pengujian(6, "Traverse Maju", NAMA_06, NIM_06, soal_06_traverse_maju,
                       ['A', 'B', 'C'], (), "A <-> B <-> C", "string")
    jalankan_pengujian(7, "Traverse Mundur", NAMA_07, NIM_07, soal_07_traverse_mundur,
                       ['A', 'B', 'C'], (), "C <-> B <-> A", "string")
    jalankan_pengujian(8, "Search Target", NAMA_08, NIM_08, soal_08_search,
                       ['A', 'B', 'C'], ('B',), "B", "node")
    jalankan_pengujian(9, "Delete First Node", NAMA_09, NIM_09, soal_09_delete_first,
                       ['A', 'B', 'C'], (), "B <-> C", "ubah")
    jalankan_pengujian(10, "Delete Last Node", NAMA_10, NIM_10, soal_10_delete_last,
                       ['A', 'B', 'C'], (), "A <-> B", "ubah")
    jalankan_pengujian(11, "Delete Target Node", NAMA_11, NIM_11, soal_11_delete_node,
                       ['A', 'B', 'C'], ('B',), "A <-> C", "ubah")

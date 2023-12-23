#include <stdio.h>
#include <stdlib.h>

// Mendefinisikan struktur baru 'PohonPembagian' yang berfungsi seperti Segment Tree
typedef struct {
    int ukuran;     // Menyimpan ukuran array yang akan digunakan di pohon
    int *dataPohon; // Pointer untuk menyimpan data pohon (array dinamis)
} PohonPembagian;

// Fungsi untuk menginisialisasi pohon baru
PohonPembagian *siapinPohon(int ukuran) {
    // Mengalokasikan memori untuk struktur PohonPembagian
    PohonPembagian *pohonBaru = (PohonPembagian *)malloc(sizeof(PohonPembagian));
    pohonBaru->ukuran = ukuran; // Menyimpan ukuran array yang diberikan

    // Mengalokasikan memori untuk data pohon (ukuran pohon adalah 2 kali ukuran array asli)
    pohonBaru->dataPohon = (int *)malloc(sizeof(int) * (2 * ukuran));

    // Menginisialisasi semua nilai di pohon dengan 0
    for (int i = 0; i < 2 * ukuran; i++) {
        pohonBaru->dataPohon[i] = 0;
    }

    return pohonBaru; // Mengembalikan pointer ke pohon yang baru dibuat
}

// Fungsi untuk mengubah nilai pada pohon
void setNilai(PohonPembagian *pohon, int posisi, int nilai) {
    posisi += pohon->ukuran; // Menyesuaikan posisi dengan indeks pada pohon

    // Menyimpan nilai baru pada posisi yang disesuaikan
    pohon->dataPohon[posisi] = nilai;

    // Melakukan update pada nilai-nilai parent sampai ke root
    for (; posisi > 1; posisi /= 2) {
        pohon->dataPohon[posisi / 2] = (pohon->dataPohon[posisi] > pohon->dataPohon[posisi ^ 1]) ? pohon->dataPohon[posisi] : pohon->dataPohon[posisi ^ 1];
    }
}

// Fungsi untuk menghitung nilai maksimal dalam range tertentu pada pohon
int hitungMaks(PohonPembagian *pohon, int awal, int akhir) {
    // Menyesuaikan indeks awal dan akhir ke posisi yang sesuai pada pohon
    awal += pohon->ukuran;
    akhir += pohon->ukuran;

    int maksimal = 0; // Variabel untuk menyimpan nilai maksimal

    // Loop sampai range awal dan akhir bertemu
    while (awal < akhir) {
        // Jika awal adalah node kanan, perbarui nilai maksimal dan maju
        if (awal & 1) maksimal = (maksimal > pohon->dataPohon[awal]) ? maksimal : pohon->dataPohon[awal++];
        
        // Jika akhir adalah node kanan, perbarui nilai maksimal dan mundur
        if (akhir & 1) maksimal = (maksimal > pohon->dataPohon[--akhir]) ? maksimal : pohon->dataPohon[akhir];
        
        // Bergerak ke parent node selanjutnya
        awal >>= 1;
        akhir >>= 1;
    }

    return maksimal; // Mengembalikan nilai maksimal
}

// Fungsi untuk mencari Longest Increasing Subsequence (LIS) dalam array
int cariLIS(int angka[], int n) {
    // Membuat array untuk menyimpan elemen-elemen yang disortir
    int *angkaUrut = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++) {
        angkaUrut[i] = angka[i];
    }

    // Melakukan sorting pada array
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            // Jika elemen i lebih besar dari elemen j, tukar
            if (angkaUrut[i] > angkaUrut[j]) {
                int tukar = angkaUrut[i];
                angkaUrut[i] = angkaUrut[j];
                angkaUrut[j] = tukar;
            }
        }
    }

    // Membuat pohon dari array yang telah disortir
    PohonPembagian *pohon = siapinPohon(n);

    // Variabel untuk menyimpan panjang LIS sementara
    int panjangLIS = 0;

    // Mengiterasi setiap elemen dalam array
    for (int i = 0; i < n; i++) {
        int posisi = 0;
        // Mencari posisi elemen dalam array yang disortir
        for (int j = 0; j < n; j++) {
            if (angkaUrut[j] == angka[i]) {
                posisi = j;
                break;
            }
        }

        // Menghitung panjang subsequence saat ini dan memperbarui pohon
        int panjangSekarang = hitungMaks(pohon, 0, posisi) + 1;
        setNilai(pohon, posisi, panjangSekarang);

        // Memperbarui panjang LIS jika ditemukan subsequence yang lebih panjang
        if (panjangLIS < panjangSekarang) panjangLIS = panjangSekarang;
    }

    return panjangLIS; // Mengembalikan panjang LIS terbesar
}

int main() {
    // Array yang akan dicari LIS-nya
    int angka[] = {3, 1, 5, 2, 6};
    // Menghitung ukuran array
    int ukuran = sizeof(angka) / sizeof(angka[0]);

    // Memanggil fungsi cariLIS dan mencetak hasilnya
    int hasilLIS = cariLIS(angka, ukuran);
    printf("LIS paling panjang nya: %d\n", hasilLIS);

    return 0;
}

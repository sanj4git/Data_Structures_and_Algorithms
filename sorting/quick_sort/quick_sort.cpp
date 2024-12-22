#include <iostream>
#include <cstdlib>

using namespace std;

int partition(int A[], int p, int r) {
    int randomIndex = p + rand() % (r - p + 1);  
    swap(A[randomIndex], A[r]);  
    int pivot = A[r];  
    int i = p - 1;
    
    for (int j = p; j < r; ++j) {  
        if (A[j] < pivot) {
            ++i;
            swap(A[i], A[j]);
        }
    }
    swap(A[i + 1], A[r]);  
    return i + 1;
}

void quickSort(int A[], int p, int r) { 
    if (p < r) {
        int q = partition(A, p, r);
        quickSort(A, p, q - 1); 
        quickSort(A, q + 1, r); 
    }
}

int main() {
    int A[10];
    for (int &x : A) x = rand() % 101;  
    for (int x : A) cout << x << " ";  
    cout << endl;

    quickSort(A, 0, 9);

    for (int x : A) cout << x << " ";  
    cout << endl;
    
    return 0;
}

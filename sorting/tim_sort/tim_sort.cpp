/*
    Cpp program to perform Tim Sort

    Algorithm

    Step 1 - Divide the array into the number of blocks known as run.
    Step 2 - Consider the size of run, either 32 or 64.
    Step 3 - Sort the individual elements of every run one by one using insertion sort.
    Step 4 - Merge the sorted runs one by one using the merge function of merge sort.
    Step 5 - Double the size of merged sub-arrays after every iteration.

    Time Complexity Analaysis 

    Best    Case O(n)
    Average Case O(n*log(n))
    Worst   Case O(n*log(n))

    Space O(n)

*/
#include <iostream>
using namespace std;

const int RUN_SIZE = 32; // for larger data sets we can use 64 as the run size

int getMin(int x, int y)
{
    return (x < y) ? x : y;
}

// insertion sort
void perfInsSort(int arr[], int start, int stop)
{
    for (int idx = start + 1; idx <= stop; ++idx)
    {
        int current = arr[idx];
        int prev = idx - 1;
        while (prev >= 0 && arr[prev] > current)
        {
            arr[prev + 1] = arr[prev];
            prev--;
        }
        arr[prev + 1] = current;
    }
}

// merge sort.
void mergeSegments(int arr[], int left, int middle, int right)
{
    int len1 = middle - left + 1;
    int len2 = right - middle;

    int leftPart[len1], rightPart[len2];

    for (int i = 0; i < len1; ++i)
    {
        leftPart[i] = arr[left + i];
    }
    for (int j = 0; j < len2; ++j)
    {
        rightPart[j] = arr[middle + 1 + j];
    }

    int i = 0, j = 0, k = left;

    while (i < len1 && j < len2)
    {
        if (leftPart[i] <= rightPart[j])
        {
            arr[k] = leftPart[i];
            ++i;
        }
        else
        {
            arr[k] = rightPart[j];
            ++j;
        }
        ++k;
    }

    while (i < len1)
    {
        arr[k] = leftPart[i];
        ++i;
        ++k;
    }

    while (j < len2)
    {
        arr[k] = rightPart[j];
        ++j;
        ++k;
    }
}

void executeTimSort(int arr[], int size)
{
    // Sort chunks of size RUN_SIZE using insertion sort
    for (int i = 0; i < size; i += RUN_SIZE)
        perfInsSort(arr, i, getMin(i + RUN_SIZE - 1, size - 1));

    // Merge sorted chunks, doubling the merge size in each iteration
    for (int run = RUN_SIZE; run < size; run *= 2)
    {
        for (int start = 0; start < size; start += 2 * run)
        {
            int mid = start + run - 1;
            int end = getMin(start + 2 * run - 1, size - 1);
            if (mid < end) mergeSegments(arr, start, mid, end);
        }
    }
}
void displayArray(const int arr[], int size)
{
    for (int i = 0; i < size; ++i)
        cout << arr[i] << " ";
    cout << endl;
}

int main()
{
    int arr[] = {-2, 7, 16, -17, 10, 15, 0, 9, -7, -4, -13, 5, 8, -14, 12};
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "Array before sorting:" << endl;
    displayArray(arr, n);

    executeTimSort(arr, n);

    cout << "Array after sorting:" << endl;
    displayArray(arr, n);

    return 0;
}


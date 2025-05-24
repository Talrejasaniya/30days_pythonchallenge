#include <iostream>
#include <vector>
#include <string>

using namespace std;

/**
 * Template function to print elements of any vector type.
 * Each element is printed on a new line.
 * @param arr - vector of any datatype T
 */
template <typename T>
void printArray(vector<T> arr) {
    for (T element : arr) {
        cout << element << endl;
    }
}

int main() {
    int n;

    // Read the number of integers
    cin >> n;
    vector<int> int_vector(n);

    // Read 'n' integers into int_vector
    for (int i = 0; i < n; i++) {
        int value;
        cin >> value;
        int_vector[i] = value;
    }

    // Read the number of strings
    cin >> n;
    vector<string> string_vector(n);

    // Read 'n' strings into string_vector
    for (int i = 0; i < n; i++) {
        string value;
        cin >> value;
        string_vector[i] = value;
    }

    // Print all integers
    printArray<int>(int_vector);

    // Print all strings
    printArray<string>(string_vector);

    return 0;
}

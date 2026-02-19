#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <chrono>

using namespace std;
using namespace chrono;

int main(int argc, char* argv[]) {

    ios::sync_with_stdio(false);
    cin.tie(NULL);

    if (argc < 2) {
        cerr << "No input file provided.\n";
        return 1;
    }

    string filename = argv[1];
    ifstream file(filename);

    vector<double> data;
    data.reserve(1000000);

    double x;
    while (file >> x)
        data.push_back(x);

    auto start = high_resolution_clock::now();
    sort(data.begin(), data.end());
    auto stop = high_resolution_clock::now();

    auto duration =
        duration_cast<microseconds>(stop - start);

    cout << duration.count() << endl;

    return 0;
}

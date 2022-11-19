#include <iostream>
using namespace std;

int main() {
    int ages[5];

    for (int i = 0; i < 5; ++i) {
        cin >> ages[i];
    }
    //your code goes here
    int youngest = ages[0];
    int p = 1;
    
    while (p < 5) {
        if (ages[p] < youngest) {
            youngest = ages[p];
        }
        p += 1;
    }

    int percent = 100 - youngest;
    float f_price = 50 * (percent/100);

    cout << f_price;

    return 0;
}
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    while (n--){
        string word;
        cin >> word;
        int l=word.length();
        if (l > 10) {
            cout << word[0] << l-2 << word[l-1] << endl;
        } else {
            cout << word << endl;
        }
    }
}

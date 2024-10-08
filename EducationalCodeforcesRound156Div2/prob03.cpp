#include <bits/stdc++.h>
using namespace std;

void solve() {
    string s;
    cin >> s;

    int n = s.size();
    long long pos;
    cin >> pos;
    pos--;
    int x, y;
    for (int i = 0; i < n; i++) {
        int len = n - i;
        if (pos < len) {
            x = i;
            y = pos;
            break;
        }
        pos -= len;
    }

    string t;
    for (auto c : s) {
        while (x > 0 && !t.empty() && c < t.back()) {
            t.pop_back();
            x--;
        }
        t += c;
    }
    cout << t[y];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout << fixed << setprecision(10);
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    cout << "\n";
    return 0;
}

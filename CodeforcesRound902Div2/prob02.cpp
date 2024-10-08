#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

long long min_announcement_cost(int n, long long p, vector<int>& a, vector<int>& b) {
    if (n == 1) {
        return p;
    }

    vector<pair<int, pair<int, int>>> residents;
    for (int i = 0; i < n; ++i) {
        residents.push_back({a[i], {b[i], i}});
    }

    sort(residents.begin(), residents.end(), [](auto& left, auto& right) {
        return left.second.first < right.second.first;
    });

    long long total_cost = 0;
    vector<bool> announced(n, false);

    for (int i = 0; i < n; ++i) {
        int max_announce = residents[i].first;
        int cost = residents[i].second.first;
        int resident_idx = residents[i].second.second;

        if (!announced[resident_idx]) {
            announced[resident_idx] = true;
            total_cost += p;
        }

        if (i == n - 1) {
            return total_cost;
        }

        if (cost >= p) {
            for (int j = i + 1; j < n; ++j) {
                int next_resident_idx = residents[j].second.second;
                if (!announced[next_resident_idx]) {
                    total_cost += p;
                }
            }
            return total_cost;
        } else {
            int count = 0;
            for (int j = 0; j < max_announce; ++j) {
                while (true) {
                    int next_resident_idx = residents[i + j + count + 1].second.second;
                    if (!announced[next_resident_idx]) {
                        announced[next_resident_idx] = true;
                        total_cost += cost;
                        if (i + j + count + 1 == n - 1)
                            return total_cost;
                        break;
                    } else {
                        count += 1;
                    }
                }
            }
        }
    }

    return 0;
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        long long p;
        cin >> n >> p;
        vector<int> a(n);
        vector<int> b(n);

        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }

        for (int i = 0; i < n; ++i) {
            cin >> b[i];
        }

        long long cost = min_announcement_cost(n, p, a, b);
        cout << cost << endl;
    }

    return 0;
}
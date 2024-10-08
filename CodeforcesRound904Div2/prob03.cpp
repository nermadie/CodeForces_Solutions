#include <algorithm>
#include <bitset>
#include <cassert>
#include <chrono>
#include <cmath>
#include <deque>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <random>
#include <set>
#include <string>
#include <vector>
typedef long long ll;
typedef long double ld;
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--)
    {
        int n, m;
        cin >> n >> m;
        vector<int> l(n), r(n);
        for (int i = 0; i < n; i++)
            cin >> l[i] >> r[i];
        map<int, vector<int>> u;
        for (int i = 0; i < n; i++)
        {
            u[l[i]].push_back(r[i]);
            u[r[i] + 1].push_back(l[i]);
        }
        int ans = 0;
        int cnt = 0, zac = 0, kon = 0;
        for (pair<int, vector<int>> p : u)
        {
            int x = p.first;
            if (x > m)
                break;
            for (int y : p.second)
            {
                if (x <= y) // zaciatok
                {
                    if (x == 1)
                        zac++;
                    if (y == m)
                        kon++;
                    cnt++;
                }
                else
                {
                    if (y == 1)
                        zac--;
                    cnt--;
                }
            }
            ans = max(ans, cnt - min(zac, kon));
        }
        cout << ans << "\n";
    }
    return 0;
}
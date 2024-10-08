#include <bits/stdc++.h>
using namespace std;
#define int long long
int32_t main()
{
    int q;
    cin >> q;
    while (q--)
    {
        int n;
        cin >> n;
        vector<int> result;
        int temp;
        cin >> temp;
        result.push_back(temp);
        for (int i = 1; i < n; i++)
        {
            int x;
            cin >> x;
            if (x < result.back())
            {
                result.push_back(1);
            }
            result.push_back(x);
        }
        cout << result.size() << endl;
        for (int i : result)
        {
            cout << i << " ";
        }
        cout << endl;
    }
    return 0;
}
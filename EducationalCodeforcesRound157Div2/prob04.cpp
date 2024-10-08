#include <bits/stdc++.h>
using namespace std;
int a[200000];
int b[200000];
int construct_array(int n)
{
    for (int i = 0; i < n; ++i)
    {
        b[0] = i;
        bool check = true;
        for (int j = 1; j < n; ++j)
        {
            b[j] = a[j - 1] ^ b[j - 1];
            if (b[j] >= n)
            {
                check = false;
                break;
            }
        }
        if (check)
        {
            return 0;
        }
    }
    return 0;
}

int main()
{
    int n;
    cin >> n;

    for (int i = 0; i < n - 1; ++i)
    {
        cin >> a[i];
    }

    construct_array(n);

    for (int i = 0; i < n; ++i)
    {
        cout << b[i] << " ";
    }

    return 0;
}

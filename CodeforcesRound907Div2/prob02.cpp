#include <bits/stdc++.h>

std::vector<int> apply_modifications(int n, std::vector<int> &arr, std::vector<int> &queries)
{
    std::vector<int> divisor_arr(n, 0);

    for (int i = 0; i < n; i++)
    {
        int count = 1;
        int pow_res = 2;
        while (arr[i] % pow_res == 0)
        {
            count++;
            pow_res *= 2;
        }
        divisor_arr[i] = count - 1;
    }

    int cur = 30;

    for (int i = 0; i < queries.size(); i++)
    {
        if (queries[i] > cur)
        {
            continue;
        }

        for (int j = 0; j < n; j++)
        {
            if (divisor_arr[j] >= queries[i])
            {
                arr[j] += std::pow(2, queries[i] - 1);
                divisor_arr[j] = queries[i] - 1;
                cur = queries[i] - 1;
            }
        }
    }

    return arr;
}

int main()
{
    int t;
    std::cin >> t;

    while (t--)
    {
        int n, q;
        std::cin >> n >> q;
        std::vector<int> arr(n);
        std::vector<int> queries(q);

        for (int i = 0; i < n; i++)
        {
            std::cin >> arr[i];
        }

        for (int i = 0; i < q; i++)
        {
            std::cin >> queries[i];
        }

        std::vector<int> result = apply_modifications(n, arr, queries);

        for (int i = 0; i < n; i++)
        {
            std::cout << result[i] << ' ';
        }
        std::cout << std::endl;
    }

    return 0;
}

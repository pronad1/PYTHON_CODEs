#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        vector<int> a(n);
        for (auto &x : a)
            cin >> x;
        set<int> st;
        for (int x : a)
            st.insert(x);
        if (st.size() == 1)
        {
            cout << 1 << endl;
            continue;
        }
        int c = 0;
        bool upward = false, downward = false;
        if (a[1] >= a[0])
            upward = true;
        else
        {
            downward = true;
            c++;
        }
        int mx = 0;
        int mn = INT_MAX;
        if (a[0] > a[n - 1])
        {
            for (int i = 0; i < n - 1; i++)
            {
                if (upward == true)
                {
                    if (a[i + 1] > a[i])
                        mx = a[i + 1];
                    else
                    {
                        downward = true;
                        upward = false;
                        mx = 0;
                        c++;
                    }
                    // cout << a[i] << "u" << endl;
                }

                else if (downward == true)
                {
                    if (a[i + 1] < a[i])
                        mn = a[i + 1];
                    else
                    {
                        downward = false;
                        upward = true;
                        mn = INT_MAX;
                    }
                    // cout << a[i] << "d" << endl;
                }
            }
            // cout << upward << " " << downward;
            if (a[n - 1] > a[n - 2])
                c++;
            if (upward == true && c == 0)
                c = 1;
            cout << c << endl;
        }
        else
        {
            reverse(a.begin(), a.end());
            for (int i = 0; i < n - 1; i++)
            {
                if (upward == true)
                {
                    if (a[i + 1] > a[i])
                        mx = a[i + 1];
                    else
                    {
                        downward = true;
                        upward = false;
                        mx = 0;
                        c++;
                    }
                    // cout << a[i] << "u" << endl;
                }

                else if (downward == true)
                {
                    if (a[i + 1] < a[i])
                        mn = a[i + 1];
                    else
                    {
                        downward = false;
                        upward = true;
                        mn = INT_MAX;
                    }
                    // cout << a[i] << "d" << endl;
                }
            }
            // cout << upward << " " << downward;
            if (a[n - 1] > a[n - 2])
                c++;
            if (upward == true && c == 0)
                c = 1;
            cout << c << endl;
        }
    }
    return 0;
}
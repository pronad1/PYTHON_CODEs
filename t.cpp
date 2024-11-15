
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    while (t--)
    {
       int s;
       cin>>s;
       int o=0;
       for (int i = 0; i <2*s; i++)
       {
         int a;
         cin>>a;
         if (a==1)
         {
            o++;
         }
       }
       int mi=max(0,o-s);
       int ma=min(o,o-s);
       cout<<mi<<" "<<ma<<'\n';
    }
    
    return 0;
}
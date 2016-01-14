#include <iostream>
#include <string>
#include <algorithm>
#include <cstdio>
#include <stack>

using namespace std;

class Solution {

public:
    bool isNumber(string s) 
    {
        int i = 0, n = s.length();
        bool isNumeric = false;

        while (i < n && s[i] == ' ') i++;

        if (i < n && (s[i] == '+' || s[i] == '-')) i++;

        while (i < n && s[i] >= '0'&& s[i] <= '9')
        {
            i++;
            isNumeric = true;
        }

        if (i < n && s[i] == '.')
        {
            i++;
            while (i < n && s[i] >= '0' && s[i] <= '9')
            {
                i++;
                isNumeric = true;
            }
        }

        if (isNumeric && i < n && s[i] == 'e')
        {
            i++;
            isNumeric = false;
            if (s[i] == '+' || s[i] == '-') i++;
            while(i < n && s[i] >= '0' && s[i] <= '9')
            {
                i++;
                isNumeric = true;
            }
        }

        if (i < n && s[i] == ' ')
        {
            i++;
            while (i < n && s[i] == ' ') i++;
        }
        cout<<isNumeric<<" "<<i<<" "<<n<<endl;
        return i == n && isNumeric;
    }
};

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    string str;
    while(cin>>str)
    {
        Solution *s = new Solution();
        cout<<s->isNumber(str)<<endl;
    }
    return 0;
}
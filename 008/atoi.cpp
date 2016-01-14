#include <iostream>
#include <string>
#include <algorithm>
#include <cstdio>
#include <stack>

using namespace std;

class Solution {

public:
    int myAtoi(string str) 
    {
#define INT_MAX 0x7fffffff
#define INT_MIN 0x80000000

        int i = 0, flag = 1, res = 0, n = str.length();
        while (i <= n && str[i] == ' ') i++;

        if (str[i] == '+') i++;
        else if (str[i] == '-') flag = -1, i++;

        while ((i<str.length()) && (str[i]>='0') && (str[i]<='9'))
        {
            if (res > INT_MAX/10 || (res == INT_MAX/10 && (str[i]-'0') >= 8))
            {
                if (flag == 1)
                    res = INT_MAX;
                else
                    res = INT_MIN;
                break;
            }
            res = res * 10 + str[i] - '0';
            i++;
        }
        return res*flag;
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
        cout<<s->myAtoi(str)<<endl;
    }
    return 0;
}
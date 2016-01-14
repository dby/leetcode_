#include <iostream>
#include <string>
#include <algorithm>
#include <cstdio>
#include <stack>

using namespace std;

class Solution {

public:
    void reverseWords(string &s)
    {
        reverse(s, 0, s.length());

        for (int i = 0, j = 0; j <= s.length(); j++)
        {
            if (j == s.length() || s[j] == ' ')
            {
                reverse(s, i, j);
                i = j + 1;
            }
        }
    }

private:
    void reverse(string &s, int begin, int end)
    {
        for (int i = 0; i < (end - begin)/2; i++)
        {
            char temp = s[begin + i];
            s[begin + i] = s[end - i - 1];
            s[end - i - 1] = temp;
        }
    }
};

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    string ss = "the sky is blue";
    //ss = getline(cin, "\n");
//    while(1)
    {
        Solution *s = new Solution();
        s->reverseWords(ss);
        cout <<ss<<endl;
    }
    return 0;
}
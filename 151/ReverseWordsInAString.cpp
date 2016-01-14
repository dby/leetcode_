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
        int i = 0;
        stack<int> word;
        stack<int> sentence;
        
        while(i <= s.size())
        {
            if (i == s.size() || s[i] == ' ')
            {
                if (!word.empty())
                {
                    if (!sentence.empty())
                    {
                        sentence.push(' ');
                    }
                    while(!word.empty())
                    {
                        sentence.push(word.top());
                        word.pop();
                    }
                }
            }
            else
            {
                word.push(s[i]);
            }
            i++;
        }

        s.clear();
        while(!sentence.empty())
        {
            s.push_back(sentence.top());
            sentence.pop();
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
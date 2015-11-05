#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

bool isPalindrome(char *s)
{
    int i = 0;
    int j = strlen(s) - 1;
    
    int tmp = 'a' - 'A';
    if (j == -1) return true;

    while (i < j)
    {
        while (i < j && !((s[i] >= '0'&&s[i] <= '9') || (s[i] >= 'a'&&s[i] <= 'z') || (s[i] >= 'A'&&s[i] <= 'Z'))) i++;
        while (i < j && !((s[j] >= '0'&&s[j] <= '9') || (s[j] >= 'a'&&s[j] <= 'z') || (s[j] >= 'A'&&s[j] <= 'Z'))) j--;
//         if ( !((s[i] >= '0'&&s[i] <= '9') || (s[i] >= 'a'&&s[i] <= 'z') || (s[i] >= 'A'&&s[i] <= 'Z')) )
//         {
//             i++;
//             continue;
//         }
//         if ( !((s[j] >= '0'&&s[j] <= '9') || (s[j] >= 'a'&&s[j] <= 'z') || (s[j] >= 'A'&&s[j] <= 'Z')) )
//         {
//             j--;
//             continue;
//         }
        if (s[i] == s[j] || abs(s[i] - s[j]) == tmp)
        {
            i++;
            j--;
        }
        else
        {
            return false;
        }
    }
    return true;
}

int main()
{

    printf("%d\n", isPalindrome(""));

    system("pause");
    return 0;
}
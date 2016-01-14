#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int strStr(char* haystack, char* needle) 
{
    if (strlen(needle) == 0)
        return 0;
    if (strlen(haystack) < strlen(needle))
        return -1;
    for (int i = 0; i <= strlen(haystack) - strlen(needle); i++)
    {
        if (strncmp(haystack + i, needle, strlen(needle)) == 0)
            return i;
    }
    return -1;
}

int main()
{

    printf("%d\n", strStr("a", ""));
    system("pause");
    return 0;
}

/*
 * strlen() 返回值为unsigned int格式，注意相减的结果
 * ""是任何字符串的字串
 *
 */
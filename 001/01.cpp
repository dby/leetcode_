#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int cmp(const void *a, const void *b)
{
    return *(int *)a > *(int *)b ? 1 : -1;
}

int* twoSum(int* nums, int numsSize, int target) 
{
    int i = 0;
    int j = numsSize - 1;
    int *res = (int *)malloc(sizeof(int) * 2);
    int *nums_c = (int *)malloc(sizeof(int) * numsSize);
    for (int k = 0; k < numsSize; k ++)
        nums_c[k] = nums[k];

    qsort(nums, numsSize, sizeof(int), cmp);
    while (i < j)
    {
        if (nums[i] + nums[j] == target)
        {
            for (int k = 0; k < numsSize; k++)
                if (nums_c[k] == nums[i])
                {
                    res[0] = k + 1;
                    break;
                }
            for (int k = 0; k < numsSize; k++)
                if (nums_c[k] == nums[j])
                {
                    if (k == res[0]) continue;
                    res[1] = k + 1;
                    break;

                }
            qsort(res, 2, sizeof(int), cmp);
            free(nums_c);
            return res;
        }
        else if (nums[i] + nums[j] < target)
            i++;
        else
            j--;
    }
    res[0] = 0;
    res[1] = 0;
    return res;
}

int main()
{

    int a[] = {5,75,25};
    int *re = twoSum(a, 3, 100);
    printf("%d, %d\n", *re, *(re + 1));

    system("pause");
    return 0;
}
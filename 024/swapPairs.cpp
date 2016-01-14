#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* swapPairs(struct ListNode* head)
{
    struct ListNode *temp = head;
    struct ListNode *ln = NULL;

    if (temp->next)
        head = temp->next;

    while(temp && temp->next)
    {
        ln = temp->next;
        temp->next = temp->next->next;
        ln->next = temp;
        temp = temp->next;
        temp = temp->next;
    }

    return head;
}

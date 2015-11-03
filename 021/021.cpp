#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* MergeTwoLists(struct ListNode* l1, struct ListNode* l2);

int main()
{
    struct ListNode ln1 = {0};
    struct ListNode ln2 = {0};
    struct ListNode* ll1 = &ln1;
    struct ListNode* ll2 = &ln2;
    struct ListNode* ll1_head;
    struct ListNode* ll2_head;

    ll1_head = ll1;
    ll2_head = ll2;

    for (int i = 1; i < 10; i++)
    {
        if (0 == i % 2) 
        {
            ListNode *p = (ListNode *)malloc(sizeof(ListNode));
            p->val = i;
            ll1->next = p;
            ll1 = ll1->next;
        }
        else
        {
            ListNode *p = (ListNode *)malloc(sizeof(ListNode));
            p->val = i;
            ll2->next = p;
            ll2 = ll2->next;
        }
    }
    ll1->next = NULL;
    ll2->next = NULL;
    
    struct ListNode* res = MergeTwoLists(ll1_head->next, ll2_head->next);
    while (res)
    {
        printf("%d\n", res->val);
        res = res->next;
    }

    system("pause");
    return 0;
}

struct ListNode* MergeTwoLists(struct ListNode* l1, struct ListNode* l2) 
{
    struct ListNode head = {0};
    struct ListNode *temp = &head;

    if (l1 == NULL) return l2;
    if (l2 == NULL) return l1;

    while(l1 || l2)
    {
        if (!l1)
        {
            temp->next = l2;
            temp = l2;
            l2 = l2->next;
        }
        else if (!l2)
        {
            temp->next = l1;
            temp = l1;
            l1 = l1->next;
        }
        else 
        {
            if (l1->val > l2->val)
            {
                temp->next = l2;
                temp = l2;
                l2 = l2->next;
            }
            else
            {
                temp->next = l1;
                temp = l1;
                l1 = l1->next;
            }
        }
    }

    return head.next;
}
#include <iostream>
#include <map>

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// 递归
class Solution
{
public:
    ListNode *reverseList(ListNode *head)
    {
        // 终止条件
        if (head == nullptr || head->next == nullptr)
        {
            return head;
        }
        // 递归体
        ListNode *subHead = reverseList(head->next);
        head->next = nullptr;
        moveToTail(subHead, head);
        return subHead;
    }

    void moveToTail(ListNode *head, ListNode *node)
    {
        ListNode *p = head;
        if (p == nullptr)
        {
            return;
        }
        while (p->next != nullptr)
        {
            p = p->next;
        }
        p->next = node;
    }
};
#include <iostream>
#include <vector>
using namespace std;
// 这题有点脑残，必须升序排序，面向测试例AC

class Solution
{
public:
    int findKthLargest(vector<int> &nums, int k)
    {
        int n = nums.size();
        int start = 0, end = n - 1;

        int i, j, tmp;
        while (start < end)
        {
            i = start, j = end;
            tmp = nums[i];
            while (i < j)
            {
                while (i < j && nums[j] >= tmp)
                    j--;
                nums[i] = nums[j];
                while (i < j && nums[i] <= tmp)
                    i++;
                nums[j] = nums[i];
            }
            if (i == n - k)
            {
                return tmp;
            }
            else if (n - k < i)
            {
                end = i - 1;
            }
            else
            {
                start = i + 1;
            }
        }
        return nums[nums.size() - k];
    }
};

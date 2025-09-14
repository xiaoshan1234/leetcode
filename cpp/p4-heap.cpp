#include <iostream>
#include <vector>
using namespace std;
// 这题有点脑残，必须升序排序，面向测试例AC

class Solution
{
public:
    int findKthLargest(vector<int> &nums, int k)
    {
        buidlHeap(nums, 0, nums.size() - 1);
        int tmp;
        for (int i = 0; i < k; i++)
        {
            tmp = nums[0];
            nums[0] = nums[nums.size() - 1 - i];
            nums[nums.size() - 1 - i] = tmp;
            adjustHeap(nums, 0, nums.size() - 2 - i);
        }
        return nums[nums.size() - k];
    }

    int adjustHeap(vector<int> &nums, int lf, int rt)
    {
        int tmp = nums[lf];
        int k = lf;
        int i = 2 * k + 1; // 1打头时是2k ，0打头时是2k+1
        while (i <= rt)
        {
            if (i + 1 <= rt && nums[i + 1] > nums[i])
            {
                i++;
            }
            if (nums[i] > tmp)
            {
                nums[k] = nums[i];
                k = i;
                i = i * 2 + 1;
            }
            else
            {
                break;
            }
        }
        nums[k] = tmp;
        return 0;
    }

    int buidlHeap(vector<int> &nums, int lf, int rt)
    {
        for (int i = (rt - 1) / 2; i >= lf; i--)
        {
            adjustHeap(nums, i, rt);
        }
        return 0;
    }
};

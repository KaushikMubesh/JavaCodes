#include <stdio.h>

void searchRange(int* nums, int numsSize, int target, int* result) {
    int start = 0, end = numsSize - 1, a = -1, k = -1;
    int mini = -1, maxi = -1;

    if (numsSize == 1 && nums[0] == target) {
        result[0] = 0;
        result[1] = 0;
        return;
    }
    while (start <= end) {
        a = (start + end) / 2;
        if (nums[a] > target) {
            end = a - 1;
        } else if (nums[a] < target) {
            start = a + 1;
        } else {
            k = a;
            break;
        }
    }
    if (k != -1) {
        int j = a;
        if (j == 0) {
            mini = j;
        } else if (j - 1 >= 0) {
            while (j - 1 >= 0 && nums[j - 1] == target) {
                j--;
            }
            mini = j;
        }
        if (a + 1 < numsSize) {
            while (a + 1 < numsSize && nums[a + 1] == target) {
                a++;
            }
            maxi = a;
        } else {
            maxi = a;
        }
        result[0] = mini;
        result[1] = maxi;
    } else {
        result[0] = -1;
        result[1] = -1;
    }
}

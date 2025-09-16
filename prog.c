#include <stdio.h>
#define MAX_FRUITS 100000
int totalFruit(int* fruits, int fruitsSize) {
    int start = 0, end = 0;
    int count[100001] = {0};  // Assuming fruit types are in range 0 to 100000
    int total = 0;
    int types = 0;
    int maxLen = 0;
    while (end < fruitsSize) {
        int currFruit = fruits[end];
        if (count[currFruit] == 0) {
            types++;
        }
        count[currFruit]++;
        total++;
        end++;

        while (types > 2) {
            int remFruit = fruits[start];
            count[remFruit]--;
            total--;
            if (count[remFruit] == 0) {
                types--;
            }
            start++;
        }

        if (total > maxLen) {
            maxLen = total;
        }
    }

    return maxLen;
}

int main() {
    int fruits[] = {1, 2, 1, 3, 4, 4, 5, 4, 5, 4, 1};
    int size = sizeof(fruits) / sizeof(fruits[0]);
    int result = totalFruit(fruits, size);
    printf("Max fruits collected: %d\n", result);
    return 0;
}

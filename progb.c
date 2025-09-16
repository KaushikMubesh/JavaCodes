#include <stdio.h>
#include <stdlib.h>
int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}
int numRescueBoats(int* people, int peopleSize, int limit) {
    qsort(people, peopleSize, sizeof(int), compare);

    int start = 0;
    int end = peopleSize - 1;
    int m = peopleSize;
    int n = 0;
    int t = 0;
    int* l = (int*)malloc(sizeof(int) * peopleSize);

    while (n != m) {
        if (start == end) {
            t++;
            break;
        }
        if (people[start] + people[end] <= limit) {
            l[n++] = people[start];
            l[n++] = people[end];
            start++;
            end--;
        } else {
            l[n++] = people[end];
            end--;
        }
        t++;
    }
    free(l);
    return t;
}

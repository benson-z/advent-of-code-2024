#include <_stdio.h>
#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int main() {
    FILE *f = fopen("input.txt", "r");
    if (f == NULL) {
        perror("Error opening file");
        return 1;
    }

    int numLines = 0;
    char tempBuffer[256];
    while (fgets(tempBuffer, sizeof(tempBuffer), f)) {
        numLines++;
    }

    rewind(f);

    int *a_list = malloc(numLines * sizeof(int));
    int *b_list = malloc(numLines * sizeof(int));

    for (int i=0; i<numLines; i++) {
        int a;
        int b;
        fscanf(f, "%d   %d", &a, &b);
        a_list[i] = a;
        b_list[i] = b;
    }
    qsort(a_list, numLines, sizeof(int), compare);
    qsort(b_list, numLines, sizeof(int), compare);

    int total = 0;
    for (int j=0; j<numLines; j++) {
        total += abs(a_list[j] - b_list[j]);
    }

    printf("%d", total);

    free(a_list);
    free(b_list);

    fclose(f);

    return 0;
}

#include <stdio.h>

int main() {
    int n, m, i, j, k, flag = 0;
    printf("Enter number of processes: ");
    scanf("%d", &n);
    printf("Enter number of resources: ");
    scanf("%d", &m);

    int need[n][m], max[n][m], allocation[n][m], available[m], work[m];
    printf("Enter allocation matrix\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) {
            scanf("%d", &allocation[i][j]);
        }
    }
    printf("Enter max matrix\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) {
            scanf("%d", &max[i][j]);
        }
    }
    printf("Enter available matrix\n");
    for (j = 0; j < m; j++) {
        scanf("%d", &available[j]);
    }

    // Initializing need matrix
    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) {
            need[i][j] = max[i][j] - allocation[i][j];
        }
    }

    // Initializing work array
    for (j = 0; j < m; j++) {
        work[j] = available[j];
    }

    // Check for safe state
    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) {
            if (need[i][j] > work[j]) {
                flag = 1;
                break;
            }
        }
    }
    if (flag == 1) {
        printf("Unsafe State\n");
        return 0;
    }

    int finish[n];
    for (i = 0; i < n; i++) {
        finish[i] = 0;
    }

    int count = 0;
    int safeSeq[n];
    while (count < n) {
        flag = 0;
        for (i = 0; i < n; i++) {
            if (finish[i] == 0) {
                for (j = 0; j < m; j++) {
                    if (need[i][j] > work[j]) {
                        flag = 1;
                        break;
                    }
                }
                if (flag == 0) {
                    for (k = 0; k < m; k++) {
                        work[k] = work[k] + allocation[i][k];
                    }
                    safeSeq[count] = i;
                    finish[i] = 1;
                    count++;
                }
            }
        }
    }

    printf("Safe sequence: ");
    for (i = 0; i < n; i++) {
        printf("%d ", safeSeq[i]);
    }
    printf("\n");
    return 0;
}

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    char msg[200];

    printf("Enter message: ");
    fgets(msg, sizeof(msg), stdin);

    // remove newline from fgets
    msg[strcspn(msg, "\n")] = 0;

    char command[300];

    // build command
    sprintf(command, "python predict.py \"%s\"", msg);

    // run python script
    system(command);

    return 0;
}

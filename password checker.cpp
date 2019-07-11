#include <stdio.h>
#include <string.h>

int main(int argc, char **argv) {
	char password[] = "temp";
	char input[11];
	
	int accepted = 0;
	strcpy(input, argv[1]);
	if(strcmp(input, password) == 0) {
		accepted = 1;
	}
	if(accepted) {
		printf("Login Success\n");
	}
}

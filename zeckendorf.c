#include <stdio.h>
#include <stdlib.h>

int fib_val;
int fib_prev;
int prev_val;
int rmn;

void fib(int c, int p){
	if (rmn == c+p){
		fib_val = rmn;
	}
	else if (rmn > p+c){	
		fib_prev = p;
		fib(p+c, c);
	}
	else if (rmn < p+c){	
		if (c != prev_val){
		prev_val = p;
		fib_val = c;
		}
		else{
			fib_val = fib_prev;
		}
	}
	else if (rmn == 1){
		fib_val = 1;
	}
}

int main(int argc, char *argv[])
{
	int target;
	fib_prev = 1;
	prev_val = 1;

	if(argc > 1){
		target = atoi(argv[1]);
	}
	else{
		//printf("Enter a positive integer to see it's zeckendorf's representation: ");
		//scanf("%d", &target);
		target = rand() % 717 + 1;
	}

	if (target >= 1){
		FILE *file = fopen("zeckendorf.txt", "w");
	rmn = target;
	//printf("The zeckendorf representation of %d is ", target);
	
	while (rmn != 0){
	fib(1, 1);
	rmn = rmn - fib_val;
	fprintf(file, "%d ", fib_val);
	}
	fclose(file);
	}
	else
	{
		FILE *file = fopen("zeckendorf.txt", "w");
		fprintf(file, "%d", target);
		fclose(file);
		//printf("Your input is not valid. Input must have a value of 1 or greater.");
	}
	system("python hellocomplicatedworld.py 2> /dev/null");
	//printf("\n");
	return 0;
}



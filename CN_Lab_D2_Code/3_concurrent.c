/* concurrent.c - A conventional C program that sum integers from 1 to 5 */
#include<stdio.h>
#include<unistd.h>

int sum;  					/* sum is a global variable */
int main(){
	int i;      				/* i is a local variable */
	sum=0;
	fork();					/* used to create a new proces*/
	for(i=1;i<=100;i++) {			/* iterate i from 1 to 5 */	
	    printf("The value of i id %d\n",i);
	    sum+= i;
	}
	printf("The sum is %d\n",sum);
	
}

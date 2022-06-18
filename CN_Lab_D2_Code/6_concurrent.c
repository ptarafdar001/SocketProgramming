/* concurrent.c - A conventional C program that sum integers from 1 to 5 */
/* line 12 & 13 prints in parent process. Line 17 prints in newly created process*/
/* open terminal and write ps -p 7879 -o comm= or top or htop */
#include<stdio.h>
#include<unistd.h>

int sum;  					/* sum is a global variable */
int main(){
	int pid;      				/* i is a local variable */
	sum=0;
	printf("Process ID: %d\n", getpid() );
  	printf("Parent Process ID: %d\n", getppid() );
	pid=fork();
	if(pid!=0) {   				/* Original Process */
	  printf("Original Process prints this. \n"); 	  
	  int a=20, b=3;
          int c;
          c=a+b;
          printf("Sum of a+b is:%d\n",c);
	  
	} 
	else {
	  printf("The new process prints this. \n");
	  int a=20, b=3;
          int c;
          c=a*b;
          printf("Multiplication of a*b is:%d\n",c);
	  
	}
	
}

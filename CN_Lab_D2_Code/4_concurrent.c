/* concurrent.c - A conventional C program that sum integers from 1 to 5 */
/* line 12 & 13 prints in parent process. Line 17 prints in newly created process*/
#include<stdio.h>
#include<unistd.h>

int sum;  					/* sum is a global variable */
int main(){
	int pid;      				/* i is a local variable */
	sum=0;
	pid=fork();
	if(pid!=0) {   				/* Original Process */
	  printf("Original Process prints this. \n"); 	  
	  printf("The process id of child process is:%d\n",pid);
	  
	} 
	else {
	  printf("The new process prints this. \n");
	  
	}
	
}

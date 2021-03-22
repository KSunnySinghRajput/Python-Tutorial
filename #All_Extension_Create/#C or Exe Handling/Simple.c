// C program to illustrate 
// command line arguments 
#include<stdio.h> 

/*int main(int argc,char* argv[]) 
{ 
	int counter; 
	printf("Program Name Is: %s",argv[0]); 
	if(argc==1) 
		printf("\nNo Extra Command Line Argument Passed Other Than Program Name"); 
	if(argc>=2) 
	{ 
		printf("\nNumber Of Arguments Passed: %d",argc); 
		printf("\n----Following Are The Command Line Arguments Passed----"); 
		for(counter=0;counter<argc;counter++) 
			printf("\nargv[%d]: %s",counter,argv[counter]); 
	} 
	return 0; 
} 
*/

// argc argumment count
int main(int argc,char* argv[]) 
 {
    int counter; 
	printf("Program Name Is: %s",argv[0]); 
    int a;
    sscanf(argv[1], "%d", &a);
    int b;
    sscanf(argv[2], "%d", &b);
    int c= a+b;
    printf("\nProgram output Is: %d\n",c);
    return c;
 }
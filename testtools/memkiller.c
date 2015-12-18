#include <stdio.h>
#include <stdlib.h>

#define SIZE 1024L

int main ( int argc, char** argv )
{
  char* ptr = NULL;
  long size = 0;

  while ( 1 )
  {
     printf("allocating %ld bytes\n",SIZE);
     size += SIZE;
     ptr = (char*) malloc(SIZE);
     printf("%ld allocated thus far\n",size);
  }

  return 0;
}



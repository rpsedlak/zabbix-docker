#include <stdio.h>
#include <stdlib.h>

#define SIZE 1024L

int main ( int argc, char** argv )
{
  char* ptr = NULL;
  long size = 0;

  while ( 1 )
  {
#ifdef DEBUG
     printf("allocating %ld bytes\n",SIZE);
     size += SIZE;
#endif

     ptr = (char*) malloc(SIZE);

#ifdef DEBUG
     printf("%ld allocated thus far\n",size);
#endif
  }

  return 0;
}



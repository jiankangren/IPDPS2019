#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double average(double s[], int sz){
	double t = 0;
	for(int i=0; i< sz; i++){
		t+= s[i];
	}
	return t/sz;
}

int main(int argc, char *argv[]){
	if(argc<4)
	{
		printf("Usage: temporl-decompress file1 file2 size times\n");
		return 1;
	}
	char* file1 = argv[1]; 
	char* file2 = argv[2]; 
	int sz = atoi(argv[3]);
        int times = atoi(argv[4]); 
	//    int sz=66*66*130;
	printf("%s, %s, %d, %d\n", file1, file2,  sz,times);
	//    printf("size of double: %ld\n", sizeof(double));
	double * ptr1 = (double *)malloc(sz * sizeof(double)) ;
	double * ptr2 = (double *)malloc(sz * sizeof(double)) ;
	double * ptr3=(double *)malloc(sz * sizeof(double));
	double * diff = (double *)malloc(sz * sizeof(double)) ;

	FILE* stream1 = fopen(file1, "rb");
	FILE* stream2 = fopen(file2, "rb");
	FILE* stream3 = fopen("base.recover", "wb");
	//fread(ptr, sizeof(float), 6, stream);



	for(int i=0;i<sz;i++){
		fscanf(stream1,"%lf",&ptr1[i]);		
	}


        for(int j=0;j<times;j++)
	for(int i=0;i<sz;i++){
		fscanf(stream2,"%lf",&ptr2[i]);
		diff[i]=ptr2[i] + ptr1[i];
	}
	fwrite(diff, sizeof(double),sz,stream3);
	fclose(stream1);
	fclose(stream2);
	fclose(stream3);
}

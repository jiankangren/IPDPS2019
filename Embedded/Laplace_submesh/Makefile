GFORTRAN    = gfortran -Wall
CC          = gcc -Wall
MPI_FORTRAN = mpif90 -Wall
MPI_CC      = cc 
LD = -lm

.SUFFIXES : .o .c

all:  laplace_full laplace_reduced base_laplace


base_laplace : base_laplace.o explUtilPar.o updateBound.o readParam.o
	$(MPI_CC)  -o $@ base_laplace.o explUtilPar.o updateBound.o readParam.o $(LD)

		
laplace_full : explicitPar.o explUtilPar.o updateBound.o readParam.o
	$(MPI_CC)  -o $@ explicitPar.o explUtilPar.o updateBound.o readParam.o $(LD)
laplace_reduced : explicitPar_reduced.o explUtilPar.o updateBound.o readParam.o
	$(MPI_CC)  -o $@ explicitPar_reduced.o explUtilPar.o updateBound.o readParam.o $(LD)

.c.o :
	$(MPI_CC) -c $(*F).c

clean : 
	/bin/rm -f *.o  laplace laplace_reduced

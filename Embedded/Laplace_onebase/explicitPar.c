#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "mpi.h"
#include "explicitPar.h"
#include <unistd.h>
#define min(a,b) a <= b ? a : b

int main(int argc, char *argv[])
{
	/* Arrays */
	double **x0;
	double **x;
	double *xfinal;
	double *xfinal_delta;
	double *xtemp;
	double *xtemp_delta;

	int nproc_reduced = atoi(argv[1]);
	/* Sizes of the discretization */
	double dt, dt1, dt2, hx, hy, epsilon;
	double resLoc, result, t, tstart, tend, elapsed_time;

	/* Index variables */
	int i, j, k, l;

	/* Convergence */
	int convergence = 0;

	int step, maxStep;
	int size_x, size_y, me, x_domains,y_domains;
	int size_x_reduced, size_y_reduced,  x_domains_reduced, y_domains_reduced;

	int iconf[5];

	int size_x_glo, size_y_glo;
	double conf[2];
	int iconf_reduced[5];
	double conf_reduced[2];

	/* MPI variables */
	int nproc, ndims;

	MPI_Comm comm, comm2d;
	int dims[2];
	int periods[2];
	int reorganisation = 0;
	MPI_Datatype column_type;
	int S = 0, E = 1, N = 2, W = 3;
	int NeighBor[4];
	int xcell, ycell, size_tot_x, size_tot_y;
	int *xs, *ys, *xe, *ye;
	double temp1_init, temp2_init, k0;
	FILE* file;
	FILE* file_delta;
	temp1_init = 10.0;

	/* temp2_init: temperature init inside */
	temp2_init = -10.0;

	/* Diffusivity coefficient */
	k0 = 1;

	MPI_Init(&argc, &argv);


	comm=MPI_COMM_WORLD;
	MPI_Comm_size(comm,&nproc);
	//printf("Full: size is %d, world id is %d \n", nproc, world_rank);
	MPI_Comm_rank(comm,&me);



	/* Getting input parameters */
	if(me==0){
		readParam(iconf,conf);
		readParam_reduced(iconf_reduced,conf_reduced,nproc_reduced);
	}
	MPI_Bcast(iconf,5,MPI_INT,0,comm);
	MPI_Bcast(conf,2,MPI_DOUBLE,0,comm);
	MPI_Bcast(iconf_reduced,5,MPI_INT,0,comm);
	size_x    = iconf[0];
	size_y    = iconf[1];
	x_domains = iconf[2];
	y_domains = iconf[3];
	maxStep   = iconf_reduced[4];
	dt1       = conf[0];
	epsilon   = conf[1];

	size_x_reduced    = iconf_reduced[0];
	size_y_reduced    = iconf_reduced[1];
	x_domains_reduced = iconf_reduced[2];
	y_domains_reduced = iconf_reduced[3];

	//        printf("Full: %d,%d,%d,%d\n",size_x_reduced,x_domains_reduced,y_domains,y_domains_reduced);
	if((me==0) && (nproc!=(x_domains*y_domains)))
		printf("Number of processes not equal to Number of subdomains\n");

	size_x_glo = size_x + 2;
	size_y_glo = size_y + 2;
	hx = 1.0/(double)(size_x_glo);
	hy = 1.0/(double)(size_y_glo);
	dt2 = 0.25*((min(hx,hy))*(min(hx,hy)))/k0;

	/* Taking a good step for convergence */
	if(dt1>=dt2)
	{
		if(me==0)
		{
			printf("\n");
			printf("  Time step too large in 'param' file - Taking convergence criterion\n");
		}
		dt=dt2;
	}
	else dt=dt1;

	size_tot_x = size_x + 2*x_domains + 2;
	size_tot_y = size_y + 2*y_domains + 2;

	/* Allocation of Contiguous 2D arrays */
	xfinal = malloc(size_x*size_y*sizeof(*xfinal));

	xfinal_delta = malloc(size_x*size_y*sizeof(*xfinal_delta));
	x0 = malloc(size_tot_y*sizeof(*x0));
	x0[0] = malloc(size_tot_x*size_tot_y*sizeof(**x0));
	x = malloc(size_tot_y*sizeof(*x));
	x[0] = malloc(size_tot_x*size_tot_y*sizeof(**x));

	for(j=1;j<=size_tot_y-1;j++)
	{
		x0[j] = x0[0] + j*size_tot_x;
		x[j] = x[0] + j*size_tot_x;
	}

	xs = malloc(nproc*sizeof(int));
	xe = malloc(nproc*sizeof(int));
	ys = malloc(nproc*sizeof(int));
	ye = malloc(nproc*sizeof(int));
	int *x_index,*y_index;
	x_index= malloc(nproc*sizeof(int));
	y_index= malloc(nproc*sizeof(int));

	/* Create 2D cartesian grid */
	periods[0] = 0;
	periods[1] = 0;

	ndims = 2;
	dims[0] = x_domains;
	dims[1] = y_domains;

	MPI_Cart_create(comm, ndims, dims, periods, reorganisation, &comm2d);

	/* Identify neighbors */
	NeighBor[0] = MPI_PROC_NULL;
	NeighBor[1] = MPI_PROC_NULL;
	NeighBor[2] = MPI_PROC_NULL;
	NeighBor[3] = MPI_PROC_NULL;

	/* Left/West and right/Est neigbors */
	MPI_Cart_shift(comm2d, 0, 1, &NeighBor[W], &NeighBor[E]);

	/* Bottom/South and Upper/North neigbors */
	MPI_Cart_shift(comm2d, 1, 1, &NeighBor[S], &NeighBor[N]);

	/* Size of each cell */
	xcell = (size_x/x_domains);
	ycell = (size_y/y_domains);

	xtemp = malloc(xcell*ycell*sizeof(*xtemp));
	xtemp_delta = malloc(xcell*ycell*sizeof(*xtemp_delta));
	/* Calculate Map for xs and ys from "me" process  */
	processToMap(xs, xe, ys, ye, xcell, ycell, x_domains, y_domains,x_index,y_index);






	/* Create column data type to communicate with East and West neighbors */
	MPI_Type_vector( ycell, 1, size_tot_x, MPI_DOUBLE, &column_type);
	MPI_Type_commit(&column_type);

	int xyz_index[3];
	xyz_index[0]=x_index[me];
	xyz_index[1]=y_index[me];
	xyz_index[2]=me;
	int index=0;
	int proc_map[128][4];

	int proc_base=-1;
	for(i=0;i<nproc;i++){
                if(i==me)
                    continue;
		MPI_Send(xyz_index,3,MPI_INT,i,1,MPI_COMM_WORLD);
   }
	int xyz_index_recv[3];

	if(xyz_index[1]==y_domains/2){
		for(i=0;i<nproc;i++){
                     if(i==me)
                         continue;
			MPI_Recv(xyz_index_recv,3,MPI_INT,i,1,MPI_COMM_WORLD,MPI_STATUS_IGNORE);
			if(xyz_index[0]==xyz_index_recv[0])
			{ 
				proc_map[index][2]=xyz_index_recv[2];
				proc_map[index][0]=xyz_index_recv[0];
				proc_map[index][1]=xyz_index_recv[1];
				//printf("Full process# %d is mapped to %d\n",me,proc_map[index][2]);
				index++;
			}
		}
	} 
	else{
		for(i=0;i<nproc;i++){
                       if(i==me)
                           continue;
                        MPI_Recv(xyz_index_recv,3,MPI_INT,i,1,MPI_COMM_WORLD,MPI_STATUS_IGNORE);
			if(xyz_index[0]==xyz_index_recv[0]&&xyz_index_recv[1]==y_domains/2)
				proc_base=xyz_index_recv[2];
		}
	}
	double *buffer_reduced= malloc((size_x_reduced/x_domains)*sizeof(double));
	/* Initialization */
	initValues(x0, size_tot_x, size_tot_y, temp1_init, temp2_init);

	/* Update the boundaries */
	updateBound(x0, NeighBor, comm2d, column_type, me, xs, ys, xe, ye, xcell);

	step = 0;
	t = 0.0;

	tstart = MPI_Wtime();

	/* Main loop */
	while(!convergence)
	{
		step = step + 1;
		t = t + dt ;

		/* Perform one step of the explicit scheme */
		Explicit(x0, x, dt, &resLoc, hx, hy, me, xs, ys, xe, ye, k0);

		/* Update the partial solution along the interface */
		updateBound(x0, NeighBor, comm2d, column_type, me, xs, ys, xe, ye, xcell);

		/* Reduce all cartesian subgrids for convergence */
		MPI_Allreduce(&resLoc, &result, 1, MPI_DOUBLE, MPI_SUM, comm);

		result= sqrt(result);
		if ((result<epsilon) || (step>maxStep)) break;
	}

	int i1;
	if(xyz_index[1]==y_domains/2){

		for(i=0;i<index;i++){

			for(i1=0;i1<(size_x/x_domains);i1++)
			{
				buffer_reduced[i1]=x0[ys[me]][xs[me]+i1];

			}

			//printf("send to %d\n",proc_map[i][2]-nproc_reduced);
			MPI_Send(buffer_reduced,(size_x/x_domains),MPI_DOUBLE,proc_map[i][2],2,MPI_COMM_WORLD);

		}
	}
       else
	MPI_Recv(buffer_reduced,(size_x/x_domains),MPI_DOUBLE,proc_base,2,MPI_COMM_WORLD,MPI_STATUS_IGNORE);
	regen_linear(x,buffer_reduced, size_x/size_x_reduced, size_y/size_y_reduced,me, xs, xe, ys, ye, xcell, ycell);


	j=1;
	for(i=ys[me];i<=ye[me];i++)
	{
		for(k=0;k<=xcell-1;k++){ 
			xtemp[(j-1)*xcell+k] = x0[i][xs[me]+k];
			xtemp_delta[(j-1)*xcell+k] = x[i][xs[me]+k];

		}
		j=j+1;
	}

	MPI_Gather(xtemp, xcell*ycell, MPI_DOUBLE, xfinal, xcell*ycell, MPI_DOUBLE, 0, comm);
	MPI_Gather(xtemp_delta, xcell*ycell, MPI_DOUBLE, xfinal_delta, xcell*ycell, MPI_DOUBLE, 0, comm);


	tend = MPI_Wtime();
	elapsed_time = tend - tstart;

	/* Output results */
	if(me == 0)
	{
		printf("\n");
		printf("Full:  Time step = %3.18f\n", dt);
		printf("\n");
		printf("  Convergence = %11.9f after %d steps\n", epsilon, step);
		printf("\n");
		printf("  Problem size = %d\n", size_x*size_y);
		printf("\n");
		printf("  Wall Clock = %15.6f\n", elapsed_time);

		/* Print the solution at each point of the grid */
		printf("\n");
		printf("Full:  Computed solution in outputPar.dat\n");
		printf("\n");

		file=fopen("outputPar.dat", "w");
		file_delta=fopen("outputPar_delta.dat","w");


		for(i=1;i<=y_domains;i++)
		{
			for(j=1;j<=ycell;j++)
			{
				for(k=0;k<=x_domains-1;k++)
					for(l=0;l<=xcell-1;l++){
						fprintf(file,"%15.11f ", xfinal[(j-1)*xcell+l+((y_domains-i)+k*y_domains)*xcell*ycell]);
						fprintf(file_delta,"%15.11f ", xfinal_delta[(j-1)*xcell+l+((y_domains-i)+k*y_domains)*xcell*ycell]);
					}
				fprintf(file,"\n");
				fprintf(file_delta,"\n");
			}
		}


		fclose(file);
		fclose(file_delta);
	}

	/* Free all arrays */
	free(x);
	free(x0);
	free(xfinal);
	free(xfinal_delta);
	free(xtemp_delta);
	free(xs);
	free(xe);
	free(ys);
	free(ye); 

	MPI_Type_free(&column_type);

	MPI_Finalize();

	return 0;
}

/**************************************************************************/
/*                                                                        */
/* This subroutin computes next values in subdomain of current process me */
/* within the domain                                                      */
/*                                                                        */
/**************************************************************************/

void Explicit(double** x0, double** x, double dt, double* r, double hx, double hy, int me, int* xs, int* ys, int* xe, int* ye, double k0)
{
   /* Index variables */
   int i, j;

   /* Factors for the stencil */
   double diagx, diagy, weightx, weighty, rk;

   /* 
      The stencil of the explicit operator for the heat equation
      on a regular rectangular grid using a five point finite difference
      scheme in space is :

      |                                    weightx * x[i-1][j]                                   |
      |                                                                                          |
      | weighty * x[i][j-1]   (diagx * weightx + diagy * weighty) * x[i][j]  weightx * x[i][j+1] |
      |                                                                                          |
      |                                    weighty * x[i+1][j]                                   |
   */

   diagx = -2.0 + hx*hx/(2*k0*dt);
   diagy = -2.0 + hy*hy/(2*k0*dt);
   weightx = k0*dt/(hx*hx);
   weighty = k0*dt/(hy*hy);

   /* Perform an explicit update on the points within the domain */
   for(i=ys[me];i<=ye[me];i++)
     for(j=xs[me];j<=xe[me];j++)
       x[i][j] = weighty*(x0[i-1][j] + x0[i+1][j] + x0[i][j]*diagy)
               + weightx*(x0[i][j-1] + x0[i][j+1] + x0[i][j]*diagx);

   /* Copy back the computed value : x  <-- x^(n+1)             */
   /*                                x0 <-- x^n                 */
   /* and compute at the same time the 2_norm of the 'residual' */
   *r = 0.0;
   for(i=ys[me];i<=ye[me];i++)
     for(j=xs[me];j<=xe[me];j++)
     {
      rk = x0[i][j] - x[i][j];
      *r  = *r + rk*rk;
      x0[i][j] = x[i][j];
     }
}

void Explicit1(double** x0, double** x, double dt, double* r, double hx, double hy, int me, int* xs, int* ys, int* xe, int* ye, double k0)
{
   /* Index variables */
   int i, j;

   /* Factors for the stencil */
   double diagx, diagy, weightx, weighty, rk;

   /* 
      The stencil of the explicit operator for the heat equation
      on a regular rectangular grid using a five point finite difference
      scheme in space is :

      |                                    weightx * x[i-1][j]                                   |
      |                                                                                          |
      | weighty * x[i][j-1]   (diagx * weightx + diagy * weighty) * x[i][j]  weightx * x[i][j+1] |
      |                                                                                          |
      |                                    weighty * x[i+1][j]                                   |
   */

   diagx = -2.0 + hx*hx/(k0*dt);
   weightx = k0*dt/(hx*hx);

   /* Perform an explicit update on the points within the domain */
   for(i=ys[me];i<=ye[me];i++)
     for(j=xs[me];j<=xe[me];j++)
       x[i][j] = weightx*(x0[i][j-1] + x0[i][j+1] + x0[i][j]*diagx);

   /* Copy back the computed value : x  <-- x^(n+1)             */
   /*                                x0 <-- x^n                 */
   /* and compute at the same time the 2_norm of the 'residual' */
   *r = 0.0;
   for(i=ys[me];i<=ye[me];i++)
     for(j=xs[me];j<=xe[me];j++)
     {
      rk = x0[i][j] - x[i][j];
      *r  = *r + rk*rk;
      x0[i][j] = x[i][j];
     }
}

/**************************************************************************/
/*                                                                        */
/* This subroutine setups the initial guess, i.e. the initial temperature */
/* within the domain                                                      */
/*                                                                        */
/**************************************************************************/

void initValues(double** x0, int size_tot_x, int size_tot_y, double temp1_init, double temp2_init)
{
   /* Index variables */
   int i, j;


   /* Setup temp1_init on edges */
   for(j=0;j<=size_tot_x-1;j++)
   {
    x0[0][j] = 0;
    x0[size_tot_y-1][j] = temp1_init;
   }

   for(j=0;j<=size_tot_y-1;j++)
   {
    x0[j][0] = temp1_init;
    x0[j][size_tot_x-1] = 0;
   }

   for(j=1;j<=size_tot_x-2;j++)
   {
    x0[1][j] = 0;
    x0[size_tot_y-2][j] = 0;
   }

   for(j=0;j<=size_tot_y-2;j++)
   {
    x0[j][1] = 0;
    x0[j][size_tot_x-2] = temp1_init;
   }

   /* Setup temp2_init inside */
   for(j=2;j<=size_tot_y-3;j++)
     for(i=2;i<=size_tot_x-3;i++)
       x0[j][i] = temp2_init;

/* FILE* file;	
 file=fopen("luo.dat","r");
double temp;
 for(i=0;i<=size_tot_x+1;i++)
	fscanf(file,"%lf",&temp);

	for(i=0;i<=size_tot_y+1;i++){
		fscanf(file,"%lf",&temp);
		for(j=1;j<=size_tot_x;i++)
		if()
			fscanf(file,"%lf",&x0[i][j])


}

fclose(file);
*/

}

/**************************************************************************/
/*                                                                        */
/* This subroutine computes the bounds of cell for the current process me */
/*                                                                        */
/**************************************************************************/

void processToMap (int *xs, int *xe, int *ys, int *ye, int xcell, int ycell, int x_domains, int y_domains,int *x_index,int *y_index)
{
   /* Index variables */
   int i, j;

   /* xs,xe coordinates */
   for(i=0;i<=y_domains-1;i++){
     xs[i] = 2;
      x_index[i]=0;
}
   for(i=0;i<=y_domains-1;i++)
     xe[i] = xs[i]+xcell - 1;

   for(i=1;i<=(x_domains-1);i++)
     for(j=0;j<=(y_domains-1);j++)
     {
      xs[i*y_domains+j] = xs[(i-1)*y_domains+j] + xcell + 2;
      xe[i*y_domains+j] = xs[i*y_domains+j] + xcell - 1;
      x_index[i*y_domains+j]=i;
     }

   /* ys,ye coordinates */
   for(i=1;i<=x_domains;i++)
   {
    ys[i*y_domains-1] = 2;
    ye[i*y_domains-1] = 2 + ycell- 1;
    y_index[i*y_domains-1]=0;
   }

   for(i=1;i<=x_domains;i++)
     for(j=0;j<=y_domains-2;j++)
     {
      ys[i*y_domains-2-j] = ys[i*y_domains-2-j+1] + ycell + 2;
      ye[i*y_domains-2-j] = ys[i*y_domains-2-j] + ycell - 1;
      y_index[i*y_domains-2-j]=j+1;
     }
}
void processToMap1 (int *xs, int *xe, int *ys, int *ye, int xcell, int ycell, int x_domains, int y_domains)
{
   /* Index variables */
   int i, j;

   /* xs,xe coordinates */
   for(i=0;i<=y_domains-1;i++){
     xs[i] = 2;
}
   for(i=0;i<=y_domains-1;i++)
     xe[i] = xs[i]+xcell - 1;

   for(i=1;i<=(x_domains-1);i++)
     for(j=0;j<=(y_domains-1);j++)
     {
      xs[i*y_domains+j] = xs[(i-1)*y_domains+j] + xcell + 2;
      xe[i*y_domains+j] = xs[i*y_domains+j] + xcell - 1;
     }

   /* ys,ye coordinates */
   for(i=1;i<=x_domains;i++)
   {
    ys[i*y_domains-1] = 2;
    ye[i*y_domains-1] = 2 + ycell- 1;
   }

   for(i=1;i<=x_domains;i++)
     for(j=0;j<=y_domains-2;j++)
     {
      ys[i*y_domains-2-j] = ys[i*y_domains-2-j+1] + ycell + 2;
      ye[i*y_domains-2-j] = ys[i*y_domains-2-j] + ycell - 1;
     }
}

void regen_linear(double** x, double** x0, int ratio_x, int ratio_y,  int me, int* xs, int* xe, int* ys, int* ye,  int xcell, int ycell )
{
   /* Index variables */
   int i, j;

     for(j=ys[me];j<=ye[me];j++)
        for(i=xs[me];i<=xe[me];i++){

/*
        int x_low=(i-xs[me])/ratio_x*ratio_x+xs[me];
        int y_low=(j-ys[me])/ratio_y*ratio_y+ys[me];
        int x_high=x_low+ratio_x;
        if(x_high>xe[me])
            x_high=xe[me];
        int y_high=y_low+ratio_y;
        if(y_high>ye[me])
            y_high=ye[me];

        double ii=i-x_low;
        double jj=j-y_low;


        double t4=x0[y_low][x_high];
        double t3=x0[y_high][x_high];
        double t2=x0[y_high][x_low];
        double t1=x0[y_low][x_low];
  */
     x[j][i]=x0[ys[me]+ycell/2][i]-x[j][i];

        }



}




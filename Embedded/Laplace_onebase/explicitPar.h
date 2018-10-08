void readParam(int* iconf, double* conf);

<<<<<<< HEAD:Embedded/Laplace_onebase/explicitPar.h

void processToMap(int* xs, int *xe, int *ys, int *ye, int xcell, int ycell, int x_domains, int y_domains,int *x_index, int* y_index);
void processToMap1(int* xs, int *xe, int *ys, int *ye, int xcell, int ycell, int x_domains, int y_domains);

=======
void processToMap(int* xs, int *xe, int *ys, int *ye, int xcell, int ycell, int x_domains, int y_domains,int *x_index, int* y_index);
>>>>>>> c7c9e0ee8edba03204298fe0ab7e55a72e63d718:Heat2D/explicitPar.h

void initValues( double** tab, int a, int b, double temp1, double temp2);

void updateBound( double** x, int* NeighBor, MPI_Comm comm, MPI_Datatype datatype, int current, int* x1, int* y1, int* x2, int* y2, int sizex);

void Explicit( double** x0, double** x, double dt, double* res, double hx, double hy, int me, int* x1, int* y1, int* x2, int* y2, double k);
<<<<<<< HEAD:Embedded/Laplace_onebase/explicitPar.h
void Explicit1( double** x0, double** x, double dt, double* res, double hx, double hy, int me, int* x1, int* y1, int* x2, int* y2, double k);

void initValues2(int nb_layers, double*** x0, int x_dim, int y_dim, int z_dim, double temp1_init, double temp2_init, int nproc, int *xs, int *xe, int *ys, int *ye, int *zs, int *ze, int xcell, 
                  int ycell, int zcell, int x_domains, int y_domains, int z_domains);
void initValues3(int nb_layers, double*** x0, int x_dim, int y_dim, int z_dim, double temp1_init, double temp2_init, int nproc, int *xs, int *xe, int *ys, int *ye, int *zs, int *ze, int xcell, 
                  int ycell, int zcell, int x_domains, int y_domains, int z_domains);

void readParam_reduced(int* iconf, double* conf,int nproc_reduced);

void regen_linear(double** x0, double* reduced_buffer, int ratio_x, int ratio_y, int me, int* xs, int* xe, int* ys,
                 int* ye, int xcell, int ycell);

=======
>>>>>>> c7c9e0ee8edba03204298fe0ab7e55a72e63d718:Heat2D/explicitPar.h

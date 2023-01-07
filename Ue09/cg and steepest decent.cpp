#include <iostream>
#include <cmath>
//Eigen/Dense not found?
//https://stackoverflow.com/questions/23284473/fatal-error-eigen-dense-no-such-file-or-directory
#include <eigen3/Eigen/Dense>
#include <chrono>
#include <random>
// #include "gnuplot-iostream.h"
using namespace Eigen;
using namespace std;
#include <fstream> //include the filestreamobject as the header files
#include <string.h>

//Inspired by https://sophiamyang.github.io/DS/optimization/descentmethod2/descentmethod2.html#:~:text=Descent%20method%20%E2%80%94%20Steepest%20descent%20and%20conjugate%20gradient%20in%20Python,-Python%20implementation&text=The%20solution%20x%20the%20minimize,the%20minimum%20of%20the%20function
VectorXd steepestDescent(MatrixXd A, VectorXd b, VectorXd x, int maxTolerance)
{
    double tolerance = 1e-6;
    for(int i=0; i<maxTolerance; i++)
    {
        VectorXd r = b - A * x;
        double r_norm = r.norm();

        if (r_norm < tolerance)
        {
            
            break;
        }
        VectorXd d = r;
        double alpha = r.dot(r) / (d.transpose() * (A * d));
        x = x + alpha * d;
    }
    return x;
}

/*
Write a two codes which performs the CG 
https://en.wikipedia.org/wiki/Conjugate_gradient_method#The_resulting_algorithm
*/
void conjugateGradient(MatrixXd A, VectorXd b, VectorXd &x, int maxIterations){
    double tolerance = 1e-6;
    // r0 = b-A*x0
    VectorXd r0 = b - A * x;
    //if r0 is sufficiently small, then return x0 as the result
    //Wiki doesnt say how small :(
    // if (r0<tolerance)
    // {
    //     x = r0;
    // }
    //rk = r0 in the first iteration
    VectorXd rk = r0;
    //p0 = r0
    VectorXd p0 = r0;
    //pk = p0 in the first iteration
    VectorXd pk = p0;
    //Not 100% sure why, but I cant do 1/ (pk * A * pk), so I will use this variable Ap to work around
    VectorXd Ap(b.size());
    //So they dont get initializes every iteration
    double alphak, betak, scalar;

    // repeat for k=0,1,2,....
    for (int i = 0; i < maxIterations; i++) {
        //a_k = r_k^T * r_k / ((p_k)^T * A * p_k) 
        scalar = rk.dot(rk); // with scalar = r_k^T * r_k
        Ap = A*pk;
        alphak = scalar / pk.dot(Ap);
        //x_k+1 := x_k + a_k * p_k
        x = x + alphak * pk;
        //r_k+1 = r_k - a_k * A*p
        rk = rk - alphak * Ap;
        //if r_k^T * r_k is too small, stop
        if (sqrt(scalar) < tolerance) {
            break;}
        //beta_k = rk+1^T * rk+1 / (rk^T*rk)
        betak = rk.dot(rk) / scalar;
        //p_k+1 = r_k+1  + beta_k * p_k
        pk = rk + betak*pk;
    }
}
//Generates random n,n matrix
//https://stackoverflow.com/questions/35827926/eigen-matrix-library-filling-a-matrix-with-random-float-values-in-a-given-range
MatrixXd generateRandomMatrixForDimension(int n)
{
  double HI = 10; // set HI and LO according to your problem.
  double LO = 1;
  double range= HI-LO;
  MatrixXd m = MatrixXd::Random(n,n); // 3x3 Matrix filled with random numbers between (-1,1)
  m = (m + MatrixXd::Constant(n,n,1.))*range/2.; // add 1 to the matrix to have values between 0 and 2; multiply with range/2
  m = (m + MatrixXd::Constant(n,n,LO)); //set LO as the lower bound (offset)
  return m;
}
//Generates random Vector of size n
// https://en.cppreference.com/w/cpp/numeric/random/uniform_real_distribution
VectorXd generateRandomVectorForDimension(int n)
{
    VectorXd v(n);
    random_device rd;
    mt19937 gen(rd());
    uniform_real_distribution<> dis(0, 1);
    for (int i = 0; i < n; i++)
        v(i) = dis(gen);
    return v;
}
int main()
{
    // Apply your method to the following test system
    MatrixXd A(4, 4);
    A << 7.0, 3.0, -1, 2, 
        3,8,1,-4
        ,-1,1,4,-1
        ,2,-4,-1,6;
    VectorXd b(4);
    b << 1, 2,3,4;
    VectorXd x(4);
    x << 0,0,0,0;
    conjugateGradient(A, b, x, 1000);
    // Print the result
    cout << "Solution vector for conjugate Gradient: \n" << x << "\n";
    //Proof
    cout << "A*solution should be 1,2,3,4: \n" << A*x << "\n";
    A << 7.0, 3.0, -1, 2, 
        3,8,1,-4
        ,-1,1,4,-1
        ,2,-4,-1,6;

    b << 1, 2,3,4;
    x << 0,0,0,0;
    x = steepestDescent(A,b,x, 1000);
    cout << "Solution vector for steepest Descent:  \n " << x << "\n";
    cout << "A*solution should be 1,2,3,4: \n" << A*x << "\n";
    //Perform benchmarks for matrices of different size (use e.g. the matrices of the 2D Laplacian
    // of the last exercise). 
    //sizes
    int arr[6] = {4,10,20,30, 50, 70};
    double averageTimeNeededConjugate[6];
    double averageTimeNeededSteepest[6];
    //For each of the sizes, solve 10 random systems with both
    //Then calculate the average
    for (int i = 0; i < 6; i++)
    {
        double LocalTimeNeededConjugate[10];
        double LocalTimeNeededSteepest[10];
        for (int j = 0; j < 10; j++)
        {
            //Random A, random B
            MatrixXd randMatrix = generateRandomMatrixForDimension(arr[i]);
            VectorXd randVector = generateRandomVectorForDimension(arr[i]);
            //creates vector 0 for n dimension
            VectorXd v = VectorXd::Zero(arr[i]);
            auto start = chrono::high_resolution_clock::now();
            
            conjugateGradient(randMatrix, randVector, v, 10000);
            auto stop = chrono::high_resolution_clock::now();

            auto difference = stop - start;
            LocalTimeNeededConjugate[j] = std::chrono::duration<double>(difference).count();
            start = chrono::high_resolution_clock::now();
            
            VectorXd solution = steepestDescent(randMatrix, randVector, v, 10000);
            stop = chrono::high_resolution_clock::now();
            difference = stop - start;
            LocalTimeNeededSteepest[j] = std::chrono::duration<double>(difference).count();

        }
       //Calculate and add the average
       double sum = 0;
       for(int k=0; k<10; k++)
       {
        sum += LocalTimeNeededConjugate[k];
       }
       averageTimeNeededConjugate[i] = sum / 10;
       sum = 0;
       for(int k=0; k<10; k++)
       {
        sum += LocalTimeNeededSteepest[k];
       }
       averageTimeNeededSteepest[i] = sum / 10;
        
    }
    //my gnuplot is not working right now >:(
    //So I will just write it into a file and do the print stuff with python
    ofstream o; 
    o.open("conjugate.csv"); 
    for (int i = 0; i < 6; i++)
    {
    string line = to_string(averageTimeNeededConjugate[i]) + "," + to_string(arr[i]) + "\n";
    o << line; // << operator which is used to print the file informations in the screen
    }
    o.close();
    o.open("steepest.csv");
    for (int i = 0; i < 6; i++)
    {
    string line = to_string(averageTimeNeededSteepest[i]) + "," + to_string(arr[i]) + "\n";
    o << line; 
    
    }
    o.close();
    
    return 0;
}

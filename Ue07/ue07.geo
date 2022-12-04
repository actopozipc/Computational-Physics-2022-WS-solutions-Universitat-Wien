

Mesh.MshFileVersion = 2.0;
cl1 = 10.0;

Point(1) = {-150, -150, -150, cl1};
Point(2) = { 150, -150, -150, cl1};
Point(3) = {-150,  150, -150, cl1};
Point(4) = { 150,  150, -150, cl1};

Line(1) = {1, 2};
Line(2) = {3, 4};
Line(3) = {1, 3};
Line(4) = {2, 4};

Line Loop(1) = {1, 4, -2, -3};
Plane Surface(1) = {1};

// COILR
cl2 = 5.0;

Point(5) = {35, 35, -50, cl2};
Point(6) = {-35, 35, -50, cl2};
Point(7) = {-35,  -35,  -50, cl2};
Point(8) = {35, -35,  -50, cl2};

Point(9) = {45, 45, -50, cl2};
Point(10) = {-45, 45, -50, cl2};
Point(11) = {-45, -45,  -50, cl2};
Point(12) = {45, -45,  -50, cl2};

Point(13) = {45, 20, -50, cl2};
Point(14) = {45, -20, -50, cl2};
Point(15) = {35, 20,  -50, cl2};
Point(16) = {35, -20,  -50, cl2};

Line(5)  = {5,6};
Line(6)  = {6,7};
Line(7)  = {7,8};
Line(8)  = {8,16};
Line(9)  = {16,14};
Line(10)  = {14,12};
Line(11)  = {12,11};
Line(12)  = {11,10};
Line(13)  = {10,9};
Line(14)  = {9,13};
Line(15)  = {13,15};
Line(16)  = {15,5};

Line Loop(2) = {5,6,7,8,9,10,11,12,13,14,15,16};
Plane Surface(2) = {2};

// EXTRUDE
cube[] = Extrude{0, 0,  300} {Surface{1};};
Delete{Volume{cube[1]};}
coil[] = Extrude{0, 0, 100} {Surface{2};};
Delete{Volume{coil[1]};}
Surface Loop(1) = {1, cube[0], cube[2], cube[3], cube[4], cube[5]};
Surface Loop(2) = {2, coil[0], coil[2], coil[3], coil[4], coil[5], coil[6], coil[7], coil[8], coil[9], coil[10], coil[11], coil[12], coil[13]};

// DEFINE PHYSICAL VOLUMES
Volume(100) = {2};
Volume(200) = {1,2};



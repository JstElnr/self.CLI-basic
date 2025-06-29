#include<iostream>
#include<cmath>
using namespace std;
const double PI= 3.1415;
    double dr(double deg){
        return deg*PI/180.0;
    }
    double rd(double rad){
        return rad*180.0/PI;
    }
    int main(){
        int choose;
        do{
            cout<<"\n=======Angle Calculator=======\n";
            cout<<"1.Degree to Radian\n";
            cout<<"2.Radian to Degree\n";
            cout<<"3.Exit\n";
            cout<<"Choose: ";
            cin>>choose;
            double a,b;
            switch(choose){
                case 1:
                cout<<"Print Degrees: ";
                cin>>a;
                cout<<"Radians: "<<dr(a)<<endl;
                break;
                case 2:
                cout<<"Print Radians: ";
                cin>>a;
                cout<<"Degrees: "<<rd(a)<<endl;
                break;
                case 3:
                cout<<"Quitting...\n";
                break;
                default:
                cout<<"Invalid\n";
            }
        }
        while(choose!=0);
        return 0;
    }
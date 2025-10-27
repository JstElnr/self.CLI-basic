#include<iostream>
#include<cmath>
using namespace std;
int main(){
    //ios::sync_with_stdio(0);
    //cin.tie(0);
    int choose;
    double x,y;
    do{
        cout<<"\n====== CLI Calculator =======\n";
        cout<<"1. +\n";
        cout<<"2. -\n";
        cout<<"3. *\n";
        cout<<"4. /\n";
        cout<<"5. x^y\n";
        cout<<"6. sqrt(x)\n";
        cout<<"7. 1/x\n";
        cout<<"0. Quit\n";
        cout<<"Choose an operation: ";
        cin>>choose;
        switch(choose){
            case 1:
            cout<<"Print numbers: ";
            cin>>x>>y;
            cout<<"Out: "<<x+y<<'\n';
            break;

            case 2:
            cout<<"Print numbers: ";
            cin>>x>>y;
            cout<<"Out: "<<x-y<<'\n';
            break;

            case 3:
            cout<<"Print numbers: ";
            cin>>x>>y;
            cout<<"Out: "<<x*y<<'\n';
            break;

            case 4:
            cout<<"Print numbers: ";
            cin>>x>>y;
            cout<<"Out: "<<x/y<<'\n';
            break;

            case 5:
            cout<<"Print numbers: ";
            cin>>x>>y;
            cout<<"Out: "<<pow(x,y)<<'\n';
            break;

            case 6:
            cout<<"Print number: ";
            cin>>x;
            if(x>=0){
            cout<<"Out: "<<sqrt(x)<<'\n';
            }
                else{
                cout<<"Invalid";
                }
                break;
            case 7:
            cout<<"Print number: ";
            cin>>x;
            if(x!=0){
            cout<<"Out: "<<1/x<<'\n';
        }else{
            cout<<"Invalid\n";
        }
        break;
        case 0:
        cout<<"----------Quitting calculator----------";
        break;
        default:
        cout<<"Invalid\n";
        }
    }while(choose!=0);
    return 0;
}

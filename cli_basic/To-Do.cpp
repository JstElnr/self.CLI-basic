#include<iostream>
#include<string>
#include<vector>
#include<fstream>
#include<sstream>
using namespace std;
const string FILENAME="ToDo.txt";
vector<string> load(){
    vector<string> tasks;
    ifstream file(FILENAME);
    string line;
    while(getline(file,line)){
        tasks.push_back(line);
    }
    return tasks;
}
void save(const vector<string>&tasks){
    ofstream file(FILENAME);
    for(const auto&task:tasks){
        file<<task<<endl;
        }
    }
void list(const vector<string>&tasks){
    if(tasks.empty()){
        cout<<"Empty\n";
    }else{
        cout<<"Tasks: \n";
        for(size_t i=0;i<tasks.size();i++){
            cout<<i+1<<". "<<tasks[i]<<endl;
                }
            }
        }
void add(vector<string>&tasks){
    cout<<"Print :";
    string task;
    cin.ignore();
    getline(cin,task);
    tasks.push_back("[ ] "+task);
    cout<<"Task is added\n";
        }
    void del(vector<string>&tasks){
    list(tasks);
    cout<<"Number of task to delete: ";
    int num;
    cin>>num;
    if(num>0&&num<=tasks.size()){
    tasks.erase(tasks.begin()+num-1);
    cout<<"Task is deleted\n";
    }else{
    cout<<"Wrong number\n";
            }
        }
    void complete(vector<string>&tasks){
    list(tasks);
    cout<<"Number of completed task: ";
    int num;
    cin>>num;
    if(num>0&&num<=tasks.size()){
    if(tasks[num-1].rfind("[ ]",0)==0){
    tasks[num-1].replace(0,3,"[x]");
    cout<<"Task is marked as completed\n";
    }else{
    cout<<"Task is done\n";
        }
    }else{
    cout<<"Wrong number\n";
             }
        }
    int main(){
    vector<string> tasks=load();
    while(true){
    cout<<"\n========To-Do CLI=======\n";
    cout<<"1.Show\n";
    cout<<"2.Add\n";
    cout<<"3.Delete\n";
    cout<<"4.Mark\n";
    cout<<"5.Quit\n";
    cout<<"Choose: ";
    int choose;
    cin>>choose;
    switch(choose){
    case 1:list(tasks); break;
    case 2:add(tasks); break;
    case 3:del(tasks); break;
    case 4:complete(tasks); break;
    case 5:save(tasks); return 0;
    default: cout<<"Wrong choice\n";
            }
        }
    }

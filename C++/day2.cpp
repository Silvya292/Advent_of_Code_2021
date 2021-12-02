#include <fstream>
#include <iostream>
#include <string>

using namespace std;

//forward 416
//down 378
//up 206

int main(){
    ifstream file("inputDay2.txt");

    int contX=0;
    int contY=0;
    int contZ=0;
    string cadena;
    getline(file,cadena,' ');

    while(!file.eof()){
        if(cadena == "forward"){
            contX++;
        }
        else if(cadena == "down"){
            contY++;
        }
        else if(cadena == "up"){
            contZ++;
        }
        getline(file,cadena,' ');
    }

    cout << contX << endl;
    cout << contY << endl;
    cout << contZ << endl;
    cout << contX*contY << endl;
    file.close();
}
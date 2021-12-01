#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int main(){
    ifstream file("inputDay1.txt");

    int cont=1;
    string cadena,cadenaAux;
    getline(file,cadena,'\n');

    while(!file.eof()){
        getline(file,cadenaAux,'\n');
        if(cadena != "" && cadenaAux != ""){
            if(cadenaAux>cadena){
                cont++;
            }
        }
        cadena=cadenaAux;
    }

    cout << cont << endl;
    file.close();
}
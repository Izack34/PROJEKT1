#include <iostream>
#include <cstddef>

using namespace std ;

class Point {
    // tutaj przepisz klase Point z poprzednich zajec
    private:
        int x;
        int y;
    public:
    Point() {x = 0; y = 0;}
    Point(int x, int y) { this->x = x; this->y = y; }
    const int getX(){ return x; }
    const int getY(){ return y; }
    void setX(int x){ this->x=x; }
    void setY(int y){ this->y=y; }
    void print(){ cout << x  << '\t' << y << endl; } 
};

class PointArray {
  int size ;
  Point *points ;
  
  public:
  PointArray () {
    size = 0;
    points = new Point [0];
  }



  PointArray (const Point ptsToCopy [] , const int toCopySize) {
    /*Zaimplementuj konstruktor, ktory przyjmuje wektor punktow i liczbe typu integer. 
  Konstruktor powinien inicjalizowac tablice points o podanym rozmiarze i skopiowac
  liczby z ptsToCopy do wektora points.*/
      size = toCopySize;
      points = new Point[size];
      for(int i=0; i < size; i++){
          points[i] = ptsToCopy[i];
      }

  }

  PointArray ( const PointArray & other ) {
  //Zaimplementuj konstruktor kopiujacy.
      size = other.size;
      points = new Point[size];
      for (int i=0; i < size; i++){
          points[i] = other.points[i];
      }
  }


  ~PointArray () {
  //destruktor
    delete [] points ;
  }
 
  void print(){
    if(getSize() == 0) cout << "Pusta tablica" << endl;
    for(int i = 0; i < getSize(); i++){
        cout << "[" << i << "] " << ": " << points[i].getX() << "\t" << points[i].getY() << endl;
    }
  }

  int getSize () const { 
  //Zaimplementuj metode, ktora zwracaja aktualny rozmiar obiektu PointArray
    return size; 
  }
};


/////////////////////////////PROSZE DOPISAC BRAKUJACE ELEMENTY KODU///////////////
////////////////////////////PROSZE NIC Z PLIKU NIE KASOWAC///////////////////////
///////////////////////////uruchamianie: ./a.out < input.txt //////////////////
int main(){
  int T = 0, x = 0, y = 0;
  cin >> T;
  Point *pa = new Point[T];
  for(int i = 0; i < T; ++i){
    cin >> x >> y;
    Point p(x, y);
    pa[i] = p;
  }
  PointArray pArr1 = PointArray(pa, T);
  PointArray pArr2 = PointArray(pArr1);
  pArr1.print();
  pArr2.print();
    

}


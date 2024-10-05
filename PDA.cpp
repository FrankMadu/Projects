#include <iostream>
using namespace std;

class PDA {
private:
  enum State {retT, retF};

public:
  State currentState = retT;
  int n = 100;
  char* stack = new char[n];
  int top = -1;
  char alphabet[26] ={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
  char symbol[4] = {'(',')','[',']'};

  void push (char c) {
    if (top < n-1) {
      top++;
      stack[top] = c;
      cout << "Element " << c << " was pushed into the stack." << endl;
    }
  }

  void pop () {
    if (top > -1) {
      cout << "Element " << stack[top] << " was popped from the stack." << endl;
      top--;
    }
  }

  void displayStack() {
    if (top > -1) {
      for (int i = 0; i <= top; i++) {
        cout << stack[i] << " ";
      }
      cout << endl;
    }
  }
  
  bool checkCharacter (char c) {
    switch (currentState) {
      case retT: {   
        bool isAlpha = false;
        bool isSymbol = false;
        for (int i = 0; i < 26; i++) {
          if (alphabet[i] == c) {
            isAlpha = true;
            break;
          }
        }
        for (int i = 0; i < 4; i++) {
          if (symbol[i] == c) {
            isSymbol = true;
            break;
          }
        }
        if (isAlpha) {
          cout << "Current character is the letter " << c << ". No push or pop required." << endl;
        } else if (c == ' ') {
          cout << "Current character is a blank space (␢). No push or pop required." << endl;
        } else if (isSymbol) {
          if (c == '(' || c == '[') {
            push(c);
          } else if (c == ')') {
            if (stack[top] == '(') {pop();} else {currentState = retF;}
          } else if (c == ']') {
            if (stack[top] == '[') {pop();} else {currentState = retF;}
          }
        } else {
          cout << "Invalid character detected. The string processing will end." << endl;
          currentState = retF;
        }
        break;
      }
      default:
        break;
    }
    return (currentState == retT);
  }
};



int main() {
  PDA pda;
  string input;

  cout << "Enter a string (alphabet {a-z,␢,(,),[,]}): ";
  getline(cin, input);

  bool finalStatement = true;
  pda.push('$');
  
  for (char c: input) {
    if (!(pda.checkCharacter(c))) {
      finalStatement = false;
      break;
    }
  }

  cout << pda.stack << endl;
  cout << pda.stack[pda.top] << endl;

  bool stackCheck;

  if (pda.stack[pda.top] == '$') {
    stackCheck = true;
  } else {
    stackCheck = false;
  }


  if (finalStatement && stackCheck) {
    pda.pop();
    cout << "\nString is accepted (PDA conditions met)" << endl;
  } else {
    cout << "\nString is not accepted (PDA conditions not met or there are invalid characters present)" << endl;
  }
  
}





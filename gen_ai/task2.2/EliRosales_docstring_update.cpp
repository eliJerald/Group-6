#include <iostream> // Include the standard input-output stream library
using namespace std;

int main() {
    // Prompt the user to enter a number
    cout << "Please enter a number:\n";

    int userInput = 0; // Variable to store user input
    cin >> userInput;  // Read user input

    // Loop to ensure valid input: only numbers <= 100 are accepted
    while (cin.fail() || userInput > 100) {
        // If the input is not a number (cin fails)
        if (cin.fail()) {
            cout << "Invalid input! Please enter a valid number:\n";
            cin.clear();              // Clear the error state
            cin.ignore(100, '\n');    // Ignore invalid input in buffer
        }
        // If the input is a number but greater than 100
        else if (userInput > 100) {
            cout << "Number too large! Please enter a number <= 100:\n";
            cin.clear();              // Clear any potential errors
            cin.ignore(100, '\n');    // Ignore extra input in buffer
        }
        
        // Prompt the user again for input
        cout << "Please enter a number:\n";
        cin >> userInput;
    }

    // Confirm the valid input
    cout << "Your input was: " << userInput << endl;

    return 0; // Indicate successful program termination
}

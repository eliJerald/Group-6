#include <iostream>
#include <vector>
#include <limits>

int secondLargest(const std::vector<int>& nums) {
    int max = std::numeric_limits<int>::min(), second = max;
    for (int n : nums) {
        if (n > max) {
            second = max;
            max = n;
        } else if (n > second && n < max) {
            second = n;
        }
    }
    return second;
}

int main() {
    std::vector<int> arr = {12, 45, 23, 51, 19, 8};
    std::cout << "Second largest: " << secondLargest(arr) << std::endl;
}

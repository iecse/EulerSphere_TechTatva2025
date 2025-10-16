#include <stdio.h>

int main() {
    double height = 120.0;     // Initial height
    double rebound_ratio = 4.0 / 5.0; // Rebound fraction
    double total_distance = 0.0;
    double rebound_height = height;

    // First fall
    total_distance += height;

    // Keep rebounding until the height becomes negligible
    while (rebound_height > 0.0001) {
        rebound_height *= rebound_ratio;   // rebound height
        total_distance += 2 * rebound_height; // going up and coming down
    }

    printf("Total distance travelled by the ball = %.2f metres\n", total_distance);
    return 0;
}

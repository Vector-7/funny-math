#include <iostream>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int N;
    double matrix[6][7];
    double ans[6];

    cin >> N;
    
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N+1; j++)
            cin >> matrix[i][j];
    }
    
    
    for(int k = 0; k < N-1; k++) {
        for(int i = k+1; i < N; i++) {
            double p = matrix[k][k] / matrix[i][k];
            for(int j = k; j < N+1; j++) {
                matrix[i][j] = matrix[k][j] - (matrix[i][j] * p);
            }
        }
    }

    for(int i = N-1; i >= 0; i--) {
        for(int j = N-1; j > i; j--)
            matrix[i][N] -= (matrix[i][j] * ans[j]);
        ans[i] = matrix[i][N] / matrix[i][i];
    }

    for(int i = 0; i < N; i++) cout << ans[i] << ' ';
    cout << '\n';
    return 0;
}
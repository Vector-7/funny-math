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
    
    // 차례대로 계수 0으로 만들기
    for(int k = 0; k < N-1; k++) {
        for(int i = k+1; i < N; i++) {
            double p = matrix[i][k] / matrix[k][k];
            for(int j = k; j < N+1; j++) {
                matrix[i][j] = matrix[i][j] - (matrix[k][j] * p);
            }
        }
    }

    // 맨 밑부터 시작해서 해 구하기
    
    for(int i = N-1; i >= 0; i--) {
        for(int j = N-1; j > i; j--)
            matrix[i][N] -= (matrix[i][j] * ans[j]);
        ans[i] = matrix[i][N] / matrix[i][i];
    }
    

    for(int i = 0; i < N; i++) cout << ans[i] << ' ';
    cout << '\n';
    return 0;
}
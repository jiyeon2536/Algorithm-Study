// 정수 삼각형
function solution(triangle) {
  var answer = 0;

  // DP 테이블을 만든다
  // let dp = [];
  // let cnt = 1

  // for (let i = 0; i < len; i++) {
  //     let tmp = [];
  //     for (let j = 0; j < cnt; j++) {
  //         tmp.push(0)
  //     }
  //     cnt += 1
  //     dp.push(tmp)
  // }
  // console.log(dp) 여기까지 내 코드

  // 여기부터 고친 코드
  const len = triangle.length;

  let dp = new Array(len).fill(0).map(() => []);

  // 초기값 설정한다.
  dp[0][0] = triangle[0][0];
  //     dp[1][0] = dp[0][0] + triangle[1][0]
  //     dp[1][1] = dp[0][0] + triangle[1][1]

  // 점화식 작성한다.
  for (let n = 1; n < len; n++) {
    const nthLen = triangle[n].length;
    for (let m = 0; m < nthLen; m++) {
      if (m === 0) {
        dp[n][m] = dp[n - 1][m] + triangle[n][m];
      } else if (m === nthLen - 1) {
        dp[n][m] = dp[n - 1][m - 1] + triangle[n][m];
      } else {
        dp[n][m] = Math.max(
          dp[n - 1][m - 1] + triangle[n][m],
          dp[n - 1][m] + triangle[n][m]
        );
      }
    }
  }

  answer = Math.max(...dp[len - 1]);

  return answer;
}

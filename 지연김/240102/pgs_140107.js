// 점 찍기
function solution(k, d) {
  var answer = 0;

  const lim = d ** 2;

  for (let x = 0; x < d + 1; x += k) {
    const y = Math.sqrt(lim - x ** 2);
    const cnt = Math.floor(y / k) + 1;
    answer += cnt;
  }

  return answer;
}

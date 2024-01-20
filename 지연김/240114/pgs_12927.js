// 야근지수

function solution(n, works) {
  var answer = 0;

  // 두번째 큰 수보다 1 작은 만큼 깎아내면 되긴함..

  // 가장 큰 수부터 깎아내서 남은 애들에 제곱헤서 돌려주면됨
  while (n > 0) {
    const maxTime = Math.max(...works);
    const maxIndex = works.indexOf(maxTime);

    if (works[maxIndex] === 0) {
      break;
    } else {
      works[maxIndex] -= 1;
      n -= 1;
    }
  }

  works.map((work) => {
    answer += work ** 2;
  });

  return answer;
}

// 는 시간초과 코드

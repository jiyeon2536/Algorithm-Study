// 기능개발
function solution(progresses, speeds) {
  var answer = [];
  let stack = [];
  const arrLen = progresses.length;

  progresses.map((progress, idx) => {
    const days = Math.ceil((100 - progress) / speeds[idx]);
    stack.push(days);
  });
  // 맨 마지막의 날짜
  let last = stack.shift();
  let cnt = 1; // 기본 하나

  while (stack.length > 0) {
    const now = stack.shift();
    // 만약 지금꺼가 그전에날짜보다 일찍 끝나고 기다리고 있었다면
    if (last >= now) {
      cnt++;
    } else {
      last = now;
      answer.push(cnt);
      cnt = 1;
    }
  }

  answer.push(cnt);

  return answer;
}

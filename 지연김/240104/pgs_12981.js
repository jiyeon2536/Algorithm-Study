// 영어 끝말잇기
function solution(n, words) {
  var answer = [0, 0];
  let spoken = new Object();
  let lastChar = "";
  let nthTurn = [];

  for (let j = 0; j < n; j++) {
    nthTurn.push(1);
  }
  const arrLen = words.length;

  for (let i = 0; i < arrLen; i++) {
    const word = words[i];
    const nthPerson = i % n;
    nthTurn[nthPerson] += 1;

    if (spoken.hasOwnProperty(word) || (i !== 0 && word[0] !== lastChar)) {
      answer[0] = nthPerson + 1;
      answer[1] = nthTurn[nthPerson] - 1;
      break;
    }

    lastChar = word[word.length - 1];
    spoken[word] = 1;
  }

  return answer;
}

// 행렬 테두리 회전하기

function solution(rows, columns, queries) {
  var answer = [];
  let prevMatrix = [];
  let count = 0;

  // 첫 행렬 만들기

  for (let i = 0; i < rows; i++) {
    let tempArray = [];
    for (let j = 0; j < columns; j++) {
      count++;
      tempArray.push(count);
    }
    prevMatrix.push(tempArray);
  }

  //

  queries.map((query) => {
    const x1 = query[0] - 1;
    const y1 = query[1] - 1;
    const x2 = query[2] - 1;
    const y2 = query[3] - 1;

    let copiedMatrix = JSON.parse(JSON.stringify(prevMatrix));
    let changed = []; // 바뀐 숫자들만 저장

    for (let x = x1; x < x2; x++) {
      copiedMatrix[x][y1] = prevMatrix[x + 1][y1];
      changed.push(prevMatrix[x][y1]);
    }
    for (let y = y1; y < y2; y++) {
      copiedMatrix[x2][y] = prevMatrix[x2][y + 1];
      changed.push(prevMatrix[x2][y]);
    }
    for (let x = x2; x > x1; x--) {
      copiedMatrix[x][y2] = prevMatrix[x - 1][y2];
      changed.push(prevMatrix[x][y2]);
    }
    for (let y = y2; y > y1; y--) {
      copiedMatrix[x1][y] = prevMatrix[x1][y - 1];
      changed.push(prevMatrix[x1][y]);
    }

    // 1. 다 돌았으면 바뀐 값들 중에서 가장 작은 수 찾기
    let minValue = Math.min(...changed);
    answer.push(minValue);

    // 2. copiedMatrix 를 prevMatrix로 바꾸기
    prevMatrix = JSON.parse(JSON.stringify(copiedMatrix));
  });

  return answer;
}

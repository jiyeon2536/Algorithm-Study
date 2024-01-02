// 무인도 여행
function solution(maps) {
  var answer = [];

  // 가로 세로 길이
  const m = maps.length;
  const n = maps[0].length;

  let newArray = [];
  let visited = [];

  // 숫자, 배열로 변환
  maps.map((row) => {
    let newRow = []; // 새로운 배열 값
    let tmpRow = []; // visited 배열 값

    const listRow = [...row];

    listRow.map((col) => {
      if (col !== "X") {
        newRow.push(Number(col));
        tmpRow.push(false);
      } else {
        newRow.push(col);
        tmpRow.push(false);
      }
    });

    newArray.push(newRow);
    visited.push(tmpRow);
  });

  // 델타 탐색, bfs 함수 정의
  const di = [0, 0, 1, -1];
  const dj = [1, -1, 0, 0];

  function bfs(i, j) {
    let total = newArray[i][j];
    visited[i][j] = true;
    let needVisit = [[i, j]];

    while (needVisit.length > 0) {
      const tmp = needVisit.shift();
      const r = tmp[0];
      const c = tmp[1];
      for (let k = 0; k < 4; k++) {
        const nr = r + di[k];
        const nc = c + dj[k];
        if (
          0 <= nr &&
          nr < m &&
          0 <= nc &&
          nc < n &&
          !visited[nr][nc] &&
          newArray[nr][nc] != "X"
        ) {
          visited[nr][nc] = true;
          total += newArray[nr][nc];
          needVisit.push([nr, nc]);
        }
      }
    }

    return total;
  }

  // 순회하면서 bfs 수행하기
  for (let a = 0; a < m; a++) {
    for (let b = 0; b < n; b++) {
      if (newArray[a][b] !== "X" && !visited[a][b]) {
        const total = bfs(a, b);
        answer.push(total);
      }
    }
  }

  answer.sort((a, b) => a - b);

  if (answer.length === 0) {
    answer = [-1];
  }

  return answer;
}

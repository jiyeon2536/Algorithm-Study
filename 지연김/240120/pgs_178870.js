// 연속된 부분 수열의 합
function solution(sequence, k) {
  var answer = [];
  let startId = 0;
  let endId = 0;
  let total = sequence[0]; // 초깃값

  const lastId = sequence.length;

  let mnLength = lastId;

  while (startId < lastId && endId < lastId) {
    if (total === k) {
      if (endId - startId < mnLength) {
        mnLength = endId - startId;
        answer = [startId, endId];
      }

      total -= sequence[startId];
      startId += 1;
      endId += 1;
      total += sequence[endId];
    } else if (total < k) {
      endId += 1;
      total += sequence[endId];
    } else if (total > k) {
      total -= sequence[startId];
      startId += 1;
    }
  }

  return answer;
}

// 최고의 집합
function solution(n, s) {
    var answer = [];
    // 일단 안되는 경우는 n이 s보다 큰 경우
    if (n > s) {
        return [-1]
    }
    // 같은 경우는 전부 1로 채워서 나가면 됨
    else if (n === s) {
        for (let i = 0; i < s; i++) {
            answer.push[1]
        }
        return answer
    }
    // 가장 중간에 있는 값들을 모으면 되는데,
    // 몫으로 하고 나머지만큼은 +1 해서 
    // 다 곱하면 최대값인듯
    else {
        const average = Math.floor(s / n)
        const remainder = (s - (average * n))
        const tmp = n - remainder
        
        for (let j = 0; j < tmp; j++) {
            answer.push(average)
        }
        for (let k = 0; k < remainder; k++) {
            answer.push(average + 1)
        }
    }
    
    return answer;
}
// 단어 변환

function solution(begin, target, words) {
	let answer = 0
	let n = words.length + 1
	let m = begin.length

	const tarIdx = words.indexOf(target)
	if (tarIdx === -1) return 0

	words.unshift(begin)

	// 인접 그래프 initialize
	let graph = {}
	let visited = {}

	words.forEach((word) => {
		graph[word] = []
		visited[word] = 0
	})
	console.log(graph)

	// 인접 그래프를 만든다
	for (let i = 0; i < n; i++) {
		const me = words[i]
		for (let j = 0; j < n; j++) {
			if (i === j) continue
			const you = words[j]
			let diff = 0
			for (let k = 0; k < m; k++) {
				if (me[k] !== you[k]) {
					diff++
					if (diff > 1) {
						break
					}
				}
			}
			if (diff === 1) {
				graph[me].push(you)
			}
		}
	}

	// bfs 를 돌고 타겟의 visited를 출력한다

	function bfs(begin) {
		let queue = [begin]
		visited[begin] = 1
		while (queue.length > 0) {
			const now = queue.shift()
			// 연결된 아이들 리스트
			console.log(now, graph[now])
			graph[now].forEach((next) => {
				if (visited[next] === 0) {
					visited[next] = visited[now] + 1
					queue.push(next)
				}
			})
		}
	}

	bfs(begin)

	if (visited[target] === 0) return 0
	answer = visited[target] - 1

	return answer
}

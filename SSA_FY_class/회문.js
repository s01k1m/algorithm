words = ['level', 'noon', 'mom', 'happy', 'ssafy', 'life']

function palindrome(word) {
    n = word.length
    let answer = true
    // 처음부터 중간까지 for 문으로 탐색하며 글자가 일치하는지 판단
    for (const i = 0; i < n / 2; i++){
        if (word[i] === word[n-i-1]){
            continue
        } else {
            answer = false // 회문이 아니면 false 반환하며 탈출
            break
        }
    }
    return answer
  }
  
for (const word of words) {
  console.log(palindrome(word))
}

// 출력 예시
// true
// true
// true
// false
// false
// false

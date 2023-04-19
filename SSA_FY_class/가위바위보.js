const p1 = ['rock', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'paper', 'paper', 'rock', 'scissors']
const p2 = ['paper', 'paper', 'rock', 'scissors', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'rock']
// opqrstu scissors>rock>paper
// 

const playGame = (p1_choice, p2_choice) => {
	for (let i=0; i<p1.length; i++){
		if (p1[i] === 'rock') {
            if (p2[i] === 'paper') {
                console.log(2)
            } else if (p2[i] === 'scissors') {
                console.log(1)
            } else {
                console.log(0)
            }
        } else if (p1[i] === 'paper') {
            if (p2[i] === 'paper') {
                console.log(0)
            } else if (p2[i] === 'scissors') {
                console.log(2)
            } else {
                console.log(1)
            }
        } else if (p1[i] === 'scissors') {
            if (p2[i] === 'paper') {
                console.log(1)
            } else if (p2[i] === 'scissors') {
                console.log(0)
            } else {
                console.log(2)
            }  
	    }
    }
}

playGame(p1, p2)
// 2
// 0
// 2
// 0
// 2
// 1
// 2
// 1
// 0
// 2

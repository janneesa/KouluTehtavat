const candidates_number = parseInt(prompt('How many candidates?'))

let candidate = []

function create_candidates(number){
  for (let i = 0; i < number; i++){

    let candidate_name = prompt(`Name for candidate ${i+1} .`)

    let new_candidate = {
      name: candidate_name,
      votes: 0
    };

    candidate.push(new_candidate)
    console.log(new_candidate)
  }
}


function voting_machine(candidates) {
  const voters_number = parseInt(prompt('How many voters?'))

  let display = 'Vote by typing candidate name:\n';

  for (let i = 0; i < candidates.length; i++) {
    display += `${candidates[i].name}\n`;
  }

  for (let i = 0; i < voters_number; i++){
    let voted_candidate = prompt(display)
    for (let i = 0; i < candidates.length; i++){
      if (voted_candidate.toUpperCase() === candidates[i].name.toUpperCase()){
        candidates[i].votes++
        break
      }
    }
  }
  console.log(candidate)
}


function winner_finder(candidates) {
  let max_votes = 0;
  let winner = null;

  for (let i = 0; i < candidates.length; i++) {
    if (candidates[i].votes > max_votes) {
      max_votes = candidates[i].votes;
      winner = candidates[i];
    }
    else if (candidates[i].votes === max_votes) {
      winner = false
    }
  }
  return winner;
}


function displayResults(candidates) {

  let winner = winner_finder(candidates);

  if (winner) {
    console.log(`The winner is ${winner.name} with ${winner.votes} votes.`);
  } else {
    console.log("There was a tie");
  }

  console.log("Results:");
  candidates.forEach(candidate => {
    console.log(`${candidate.name}: ${candidate.votes} votes`);
  });
}


create_candidates(candidates_number)

voting_machine(candidate)

displayResults(candidate);

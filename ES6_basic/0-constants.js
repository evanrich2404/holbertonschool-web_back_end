// modifying the code to use const and let

// const is used when the value of the variable is not going to change
export function taskFirst() {
  const task = 'I prefer const when I can. but';
  return task;
}

export function getLast() {
  return ' is okay';
}

// let is used when the value of the variable is going to change
export function taskNext() {
  let combination = 'But sometimes let';
  combination += getLast();

  return combination;
}

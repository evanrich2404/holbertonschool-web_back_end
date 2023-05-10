export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  const [newTask, newTask2] = (() => {
    let t = task;
    let t2 = task2;

    if (trueOrFalse) {
      t = true;
      t2 = false;
    }

    return [t, t2];
  })();
  return [newTask, newTask2];
}

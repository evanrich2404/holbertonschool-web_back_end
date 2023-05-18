export default function cleanSet(set, array) {
  array.forEach((value) => set.delete(value));
  return set;
}

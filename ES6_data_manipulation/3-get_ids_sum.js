export default function getStudentIdsSum(array) {
  if (!Array.isArray(array)) {
    return [];
  }
  return array.reduce((accumulator, item) => accumulator + item.id, 0);
}

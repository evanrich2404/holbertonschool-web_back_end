import signUpUser from "./4-user-promise";
import uploadPhoto from "./5-photo-reject";

export default async function handleProfileSignup(firstName, lastName, filename) {
  const user = await signUpUser(firstName, lastName);
  let photo;
  try {
    photo = await uploadPhoto(filename);
  } catch (err) {
    photo = null;
  }
  return {
    user,
    photo,
  };
}

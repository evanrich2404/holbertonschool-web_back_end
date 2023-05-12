import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, filename) {
  const user = await signUpUser(firstName, lastName).then((data) => {
    console.log(data);
    return ({
      status: 'fulfilled',
      value: data,
    });
  });

  const photo = await uploadPhoto(filename).catch((err) => {
    console.log(err.message);
    return ({
      status: 'rejected',
      value: `Error: ${err.message}`,
    });
  });

  return ([user, photo]);
}

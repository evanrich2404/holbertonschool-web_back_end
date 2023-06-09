export default function loadBalancer(chinaDownload, USDownload) {
  return new Promise((resolve, reject) => {
    chinaDownload.then((data) => {
      resolve(data);
    }).catch((err) => {
      reject(err);
    });
    USDownload.then((data) => {
      resolve(data);
    }).catch((err) => {
      reject(err);
    });
  });
}

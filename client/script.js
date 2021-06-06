async function getServerData(serverUrl = "http://localhost:8888") {
  try {
    const res = await fetch(serverUrl);
    const data = await res.json();
    const serverData = `<h1>Tornado Web Server</h1>
      <p> OS: ${data.platform} </p>
      <p> Architecture: ${data.architecture} </p>
      <p> Hostname: ${data.hostname} </p>
      <p> IP adress: ${data.ip_adress} </p>
      <p> Available RAM: ${data.ram} </p>
      <p> Server time: ${data.time} </p>
      `;
    return serverData;
  } catch (err) {
    console.error(err);
  }
}

document.addEventListener("DOMContentLoaded", async () => {
  const text = await getServerData();
  const appRoot = document.getElementById("app");
  appRoot.innerHTML = text;
});

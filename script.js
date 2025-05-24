
const endpoints = {
  "meta-1": "/metadata",
  "meta-2": "/metadata"
};

Object.entries(endpoints).forEach(([elementId, path]) => {
  fetch(path)
    .then(res => res.json())
    .then(data => {
      const html = `
        <p><strong>Instance ID:</strong> ${data["instance-id"]}</p>
        <p><strong>Private IP:</strong> ${data["local-ipv4"]}</p>
        <p><strong>AZ:</strong> ${data["placement-availability-zone"]}</p>
        <p><strong>Type:</strong> ${data["instance-type"]}</p>
      `;
      document.getElementById(elementId).innerHTML = html;
    })
    .catch(() => {
      document.getElementById(elementId).innerText = "Unable to fetch metadata.";
    });
});

fetch("/alb-metadata.json")
  .then(res => res.json())
  .then(data => {
    const albElement = document.querySelector(".alb .label");
    albElement.innerHTML += `
      <p style="font-size: 0.85em;"><strong>DNS:</strong> ${data["dns_name"]}</p>
      <p style="font-size: 0.85em;"><strong>Listener:</strong> ${data["listener_port"]} (${data["listener_protocol"]})</p>
      <p style="font-size: 0.85em;"><strong>Target Group:</strong> ${data["target_group"]}</p>
    `;
  })
  .catch(() => {
    const albElement = document.querySelector(".alb .label");
    albElement.innerHTML += `<p style="font-size: 0.85em;">Unable to fetch ALB metadata.</p>`;
  });

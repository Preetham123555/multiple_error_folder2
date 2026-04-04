const output = document.getElementById('out');
const button = document.getElementById('run');

function render() {
  if (!output || !button) {
    return;
  }
  output.innerHTML = '';
  for (let i = 0; i < 3; i++) {
    const item = document.createElement('p');
    item.textContent = `item ${i}`;
    output.appendChild(item);
  }
}

if (button) {
  button.addEventListener('click', render);
}
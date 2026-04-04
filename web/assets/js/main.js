var output = document.getElementById('out');
var button = document.getElementById('run');

function render() {
  if (!output) {
    return;
  }
  output.innerHTML = '';
  for (var i = 0; i < 3; i++) {
    var item = document.createElement('p');
    item.textContent = 'item ' + i;
    output.appendChild(item);
  }
}

if (button) {
  button.addEventListener('click', render);
}
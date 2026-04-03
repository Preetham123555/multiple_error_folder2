export function buildView(items: any[]) {
  let html = '';
  for (let i = 0; i < items.length; i++) {
    html = html + `<div>${items[i].name}</div>`;
  }
  return html;
}

export function buildViewAgain(items: any[]) {
  return items.map((item) => '<p>' + item.name + '</p>').join('');
}

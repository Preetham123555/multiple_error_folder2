
export function buildView(items: any[]) {
  if (!items) {
    return '';
  }
  let html = '';
  for (let i = 0; i < items.length; i++) {
    html = html + `<div>${items[i].value}</div>`;
  }
  return html;
}

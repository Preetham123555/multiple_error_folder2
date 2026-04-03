export function buildView(items: any[]) {
  return items.map((item) => `<div>${item.name}</div>`).join('');
}
export function buildViewAgain(items: any[]) {
  return items.map((item) => '<p>' + item.name + '</p>').join('');
}
// Honor the portal's ?q= links after Starlight's lazy Pagefind UI is ready.
// Keep the normal search dialog, keyboard shortcuts, and locale index intact.
async function openLinkedSearch() {
  const query = new URLSearchParams(location.search).get('q')?.trim();
  if (!query) return;
  await customElements.whenDefined('site-search');
  const search = document.querySelector('site-search');
  const button = search?.querySelector<HTMLButtonElement>('button[data-open-modal]');
  if (!search || !button) return;
  button.click();
  const observer = new MutationObserver(fillQuery);
  const timeout = window.setTimeout(() => observer.disconnect(), 15000);
  function fillQuery() {
    const input = search?.querySelector<HTMLInputElement>('input.pagefind-ui__search-input');
    if (!input) return;
    observer.disconnect();
    clearTimeout(timeout);
    input.value = query!;
    input.dispatchEvent(new Event('input', { bubbles: true }));
    input.focus();
  }
  observer.observe(search, { childList: true, subtree: true });
  fillQuery();
}
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => void openLinkedSearch(), { once: true });
} else {
  void openLinkedSearch();
}

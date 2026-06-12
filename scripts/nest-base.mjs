// Astro `base: '/wiki'` prefixes every emitted URL with /wiki, but does NOT move
// the built files under dist/wiki/. This postbuild step nests the whole output
// under dist/wiki/ so the on-disk paths match the /wiki-prefixed URLs when the
// site is served (directly, or proxied at www.uotavern.com/wiki/*).
import { readdirSync, mkdirSync, renameSync, existsSync, copyFileSync } from 'node:fs';
import { join } from 'node:path';

const dist = './dist';
const sub = join(dist, 'wiki');
const keepAtRoot = new Set(['wiki']); // never move the target into itself

const entries = readdirSync(dist).filter((n) => !keepAtRoot.has(n));
mkdirSync(sub, { recursive: true });
for (const name of entries) {
  renameSync(join(dist, name), join(sub, name));
}
// Keep a root 404 so direct hits outside /wiki still render something.
const nested404 = join(sub, '404.html');
if (existsSync(nested404)) copyFileSync(nested404, join(dist, '404.html'));

console.log(`nested ${entries.length} entries under dist/wiki/`);

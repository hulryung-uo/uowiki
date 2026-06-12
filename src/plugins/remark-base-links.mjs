// @ts-check
// Prefix the site base ('/wiki') onto every ROOT-ABSOLUTE reference that
// originates from authored markdown/MDX content.
//
// Why this exists: with Astro `base: '/wiki'`, Starlight auto-prefixes its OWN
// component-emitted links (nav, sidebar, pagination) via `base`. But the ~11.5k
// absolute markdown links (`[x](/skills/mining/)`), ~26k raw-HTML asset `src`s
// (`<img src="/img/...">`, `<audio src="/audio/...">`) and ko/ja locale links
// (`/ko/...`) that live INSIDE content are never touched by `base` — they pass
// through verbatim. This plugin rewrites them at build time.
//
// Runs at the REMARK (mdast) stage, not rehype: Astro keeps raw HTML in `.md`
// as `html`-type mdast nodes and re-inserts them verbatim into the output
// WITHOUT routing them through the rehype/HAST pass — so a rehype plugin can't
// see those `<img>`/`<audio>` tags. mdast is the only stage where both the
// parsed `link`/`image` nodes AND the raw `html` strings are visible.
//
// Mental model after base:'/wiki' — the entire emitted site lives under /wiki/,
// so every absolute reference an author wrote must gain the /wiki prefix.

const BASE = '/wiki';

/**
 * Should this URL value be prefixed with the base?
 * Rewrite only root-absolute, same-origin paths that aren't already based.
 * Excludes: external (`http`, `//`), in-page (`#`), `mailto:`/other schemes
 * (those don't start with `/`), and anything already under `/wiki`.
 * @param {unknown} value
 * @returns {boolean}
 */
export function shouldPrefix(value) {
	if (typeof value !== 'string' || value.length === 0) return false;
	if (value[0] !== '/') return false; // must be root-absolute
	if (value[1] === '/') return false; // protocol-relative ("//cdn…") → external
	if (value === BASE) return false; // already exactly the base
	if (
		value.startsWith(BASE + '/') ||
		value.startsWith(BASE + '#') ||
		value.startsWith(BASE + '?')
	) {
		return false; // already under the base — don't double-prefix
	}
	return true;
}

// href/src on raw HTML strings (e.g. `<img src="/img/…">`, `<audio src="/…">`,
// `<a href="/…">`, `<source src="/…">`). Captures the quoted value; the negative
// lookahead `(?!/)` rejects protocol-relative `//…`. We re-test with
// shouldPrefix() so `#`, `?`, and already-based values are skipped.
const RAW_ATTR_RE = /\b(href|src)(\s*=\s*)("|')(\/[^"']*)\3/g;

/**
 * Rewrite root-absolute href/src values inside a raw HTML string.
 * @param {string} html
 * @returns {string}
 */
function rewriteRawHtml(html) {
	return html.replace(RAW_ATTR_RE, (match, attr, eq, quote, value) => {
		if (!shouldPrefix(value)) return match;
		return `${attr}${eq}${quote}${BASE}${value}${quote}`;
	});
}

/**
 * Remark plugin: walk the mdast and base-prefix in-content URLs.
 * @returns {(tree: any) => void}
 */
export default function remarkBaseLinks() {
	return (tree) => {
		visit(tree, (node) => {
			if (!node) return;
			// Markdown links `[x](/…)` and reference defs.
			if (node.type === 'link' || node.type === 'definition') {
				if (shouldPrefix(node.url)) node.url = BASE + node.url;
				return;
			}
			// Markdown images `![alt](/…)`.
			if (node.type === 'image') {
				if (shouldPrefix(node.url)) node.url = BASE + node.url;
				return;
			}
			// Raw HTML blocks/inline (`<img src="/…">`, `<audio>`, raw `<a>`).
			if (node.type === 'html' && typeof node.value === 'string') {
				node.value = rewriteRawHtml(node.value);
			}
		});
	};
}

/**
 * Minimal mdast walker (avoids a unist-util-visit dependency).
 * @param {any} node
 * @param {(n: any) => void} fn
 */
function visit(node, fn) {
	fn(node);
	const children = node && node.children;
	if (children) {
		for (const child of children) visit(child, fn);
	}
}

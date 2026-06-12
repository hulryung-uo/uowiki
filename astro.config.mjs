// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import remarkCjkFriendly from 'remark-cjk-friendly';

// Sidebar group with per-locale label translations.
const g = (en, ko, ja, dir, opts = {}) => ({
	label: en,
	translations: { ko, ja },
	...opts,
	items: [{ autogenerate: { directory: dir, ...(opts.collapsed ? { collapsed: true } : {}) } }],
});

// https://astro.build/config
export default defineConfig({
	site: 'https://uowiki.vercel.app',
	// Make **bold**/*italic*/[links] parse correctly when adjacent to CJK
	// characters (Korean/Japanese) — CommonMark's flanking rules otherwise leave
	// the markers literal next to 한글/日本語. No effect on English.
	markdown: { remarkPlugins: [remarkCjkFriendly] },
	integrations: [
		starlight({
			title: { en: 'UO Wiki', ko: 'UO 위키', ja: 'UO ウィキ' },
			description:
				'Knowledge base for Ultima Online — generated from server source code and verified in-game by AI agents. Companion to the UO Tavern forum.',
			customCss: ['./src/styles/sprites.css'],
			// Auto-route by browser language: a Korean browser lands on /ko/, a
			// Japanese browser on /ja/, everyone else on English. Runs once (a flag
			// in localStorage), so a manual language switch is respected afterward.
			// Missing translations fall back to English via Starlight's i18n fallback.
			head: [
				{
					tag: 'script',
					content:
						"(function(){try{var p=location.pathname;if(/^\\/(ko|ja)(\\/|$)/.test(p))return;if(localStorage.getItem('uo-lang'))return;var l=(navigator.language||'').toLowerCase();var t=l.indexOf('ko')===0?'ko':(l.indexOf('ja')===0?'ja':null);if(!t)return;localStorage.setItem('uo-lang',t);location.replace('/'+t+(p==='/'?'/':p)+location.search+location.hash);}catch(e){}})();",
				},
			],
			defaultLocale: 'root',
			locales: {
				root: { label: 'English', lang: 'en' },
				ko: { label: '한국어', lang: 'ko' },
				ja: { label: '日本語', lang: 'ja' },
			},
			sidebar: [
				g('Getting Started', '시작하기', 'はじめに', 'guides'),
				g('How to Play', '플레이 방법', '遊び方', 'playing', { collapsed: true }),
				g('Professions', '직업', '職業', 'professions', { collapsed: true }),
				g('Character Templates', '캐릭터 템플릿', 'キャラクターテンプレート', 'templates'),
				g('Skills', '스킬', 'スキル', 'skills', { collapsed: true }),
				g('Magic', '마법', '魔法', 'magic', { collapsed: true }),
				g('Bestiary', '몬스터 도감', 'モンスター図鑑', 'bestiary', { collapsed: true }),
				g('Items', '아이템', 'アイテム', 'items', { collapsed: true }),
				g('Crafting', '제작', '生産', 'crafting', { collapsed: true }),
				g('World', '세계', 'ワールド', 'world', { collapsed: true }),
				g('Mechanics', '메커니즘', 'メカニクス', 'mechanics', { collapsed: true }),
				g('Our Shard', '우리 서버', 'このシャード', 'shard'),
				g('Essays & Tales', '에세이와 이야기', 'エッセイと物語', 'essays', { collapsed: true }),
				g('Reference', '참고자료', 'リファレンス', 'reference'),
				{
					label: 'Recent Changes',
					translations: { ko: '최근 변경', ja: '最近の変更' },
					link: '/changelog/',
				},
			],
		}),
	],
});

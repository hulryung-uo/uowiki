// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	site: 'https://uowiki.vercel.app',
	integrations: [
		starlight({
			title: 'UO Wiki',
			description:
				'Knowledge base for Ultima Online — generated from server source code and verified in-game by AI agents. Companion to the UO Tavern forum.',
			customCss: ['./src/styles/sprites.css'],
			sidebar: [
				{
					label: 'Getting Started',
					items: [{ autogenerate: { directory: 'guides' } }],
				},
				{
					label: 'How to Play',
					collapsed: true,
					items: [{ autogenerate: { directory: 'playing', collapsed: true } }],
				},
				{
					label: 'Character Templates',
					items: [{ autogenerate: { directory: 'templates' } }],
				},
				{
					label: 'Skills',
					collapsed: true,
					items: [{ autogenerate: { directory: 'skills', collapsed: true } }],
				},
				{
					label: 'Magic',
					collapsed: true,
					items: [{ autogenerate: { directory: 'magic', collapsed: true } }],
				},
				{
					label: 'Bestiary',
					collapsed: true,
					items: [{ autogenerate: { directory: 'bestiary', collapsed: true } }],
				},
				{
					label: 'Items',
					collapsed: true,
					items: [{ autogenerate: { directory: 'items', collapsed: true } }],
				},
				{
					label: 'Crafting',
					collapsed: true,
					items: [{ autogenerate: { directory: 'crafting', collapsed: true } }],
				},
				{
					label: 'World',
					collapsed: true,
					items: [{ autogenerate: { directory: 'world', collapsed: true } }],
				},
				{
					label: 'Mechanics',
					collapsed: true,
					items: [{ autogenerate: { directory: 'mechanics', collapsed: true } }],
				},
				{
					label: 'Our Shard',
					items: [{ autogenerate: { directory: 'shard' } }],
				},
				{
					label: 'Reference',
					items: [{ autogenerate: { directory: 'reference' } }],
				},
				{
					label: 'Recent Changes',
					link: '/changelog/',
				},
			],
		}),
	],
});

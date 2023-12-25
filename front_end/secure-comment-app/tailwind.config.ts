import { join } from 'path'
import type { Config } from 'tailwindcss'
import { skeleton } from '@skeletonlabs/tw-plugin'

export default {
	darkMode: 'class',
	content: ['./src/**/*.{html,js,svelte,ts}', join(require.resolve('@skeletonlabs/skeleton'), '../**/*.{html,js,svelte,ts}')],
	theme: {
		extend: {},
	},
	plugins: [
        require('@tailwindcss/forms'),
		skeleton({
			themes: {
				preset: [
					{
						name: 'modern',
						enhancements: true,
					},
					{
						name: 'seafoam',
						enhancements: true,
					},
					{
						name: 'wintry',
						enhancements: true,
					},
                    {
                        name: 'hamlindigo',
                        enhancements: true,
                    },
				],
			},
		}),
	],
} satisfies Config;

// module.exports = {
//   title: 'Physical AI & Humanoid Robotics',
//   tagline: 'AI Systems in the Physical World',
//   url: 'https://physical-ai-book-jeyfjswje-zartash-imrans-projects.vercel.app',
//   baseUrl: '/',
//   onBrokenLinks: 'throw',
//   onBrokenMarkdownLinks: 'warn',
//   favicon: 'img/favicon.ico',

//   organizationName: 'zartasha-khan123',
//   projectName: 'physical-ai-humanoid-robotics-book',

//   presets: [
//     [
//       '@docusaurus/preset-classic',
//       {
//         docs: {
//           path: 'docs',
//           routeBasePath: '/', 
//           sidebarPath: require.resolve('./sidebars.js'),
//           include: ['**/*.md', '**/*.mdx'],

//           editUrl: ({ docPath }) => {
//             return `https://github.com/zartasha-khan123/physical-ai-humanoid-robotics-book/edit/main/docusaurus-book/docs/${docPath}`;
//           },
//         },

//         blog: false,

//         theme: {
//           customCss: require.resolve('./src/css/custom.css'),
//         },
//       },
//     ],
//   ],
// };


module.exports = {
  title: 'Physical AI & Humanoid Robotics',
  tagline: 'AI Systems in the Physical World',

  url: 'https://physical-ai-book-jeyfjswje-zartash-imrans-projects.vercel.app',
  baseUrl: '/',

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',

  organizationName: 'zartasha-khan123',
  projectName: 'physical-ai-humanoid-robotics-book',

  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          path: 'docs',
          routeBasePath: '/',
          sidebarPath: require.resolve('./sidebars.js'),
          include: ['**/*.md', '**/*.mdx'],
          editUrl:
            'https://github.com/zartasha-khan123/physical-ai-humanoid-robotics-book/edit/main/docusaurus-book/docs/',
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],

  themeConfig: {
    sitemap: {
      changefreq: 'weekly',
      priority: 0.5,
      filename: 'sitemap.xml',
    },
  },
};

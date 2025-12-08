



// module.exports = {
//   title: 'Physical AI & Humanoid Robotics',
//   tagline: 'AI Systems in the Physical World',
//   url: 'https://zartasha-khan123.github.io', 
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

//           // 🔥 FIXED EDIT URL
//           // It will correctly open file editor for every page
//           editUrl:
//             'https://github.com/zartasha-khan123/physical-ai-humanoid-robotics-book/edit/main/docs',

//           include: ['**/*.md','**/*.mdx'],
//         },

//         blog: false,

//         theme: {
//           // 🔥 ONLY ONE CSS FILE — clean build
//           customCss: require.resolve('./src/css/custom.css'),
//         },
//       },
//     ],
//   ],
// };



module.exports = {
  title: 'Physical AI & Humanoid Robotics',
  tagline: 'AI Systems in the Physical World',
  url: 'https://zartasha-khan123.github.io',
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

          // FIX: dynamic edit URL
          editUrl: ({ docPath }) =>
            docPath === 'index.mdx'
              ? 'https://github.com/zartasha-khan123/physical-ai-humanoid-robotics-book/edit/main/docs/index.mdx'
              : `https://github.com/zartasha-khan123/physical-ai-humanoid-robotics-book/edit/main/docs/${docPath}`,
        },

        blog: false,

        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};

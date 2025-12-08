


// module.exports = {
//   title: 'Physical AI & Humanoid Robotics',
//   tagline: 'AI Systems in the Physical World',
//   url: 'https://zartasha-khan123.github.io', // for GitHub Pages deployment
//   baseUrl: '/', // if you deploy to subfolder change accordingly
//   onBrokenLinks: 'throw',
//   onBrokenMarkdownLinks: 'warn',
//   favicon: 'img/favicon.ico',
//   organizationName: 'zartasha-khan123', // your GitHub username
//   projectName: 'physical-ai-humanoid-robotics-book', // your GitHub repo name
//   presets: [
//     [
//       '@docusaurus/preset-classic',
//       {
//         docs: {
//           path: 'docs',
//           routeBasePath: '/', // serve docs at root
//           sidebarPath: require.resolve('./sidebars.js'),
//           editUrl: 'https://github.com/zartasha-khan123/physical-ai-humanoid-robotics-book/edit/main/',
//           include: ['**/*.md'], // include all markdown files
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

          // 🔥 FIXED EDIT URL
          // It will correctly open file editor for every page
          editUrl:
            'https://github.com/zartasha-khan123/physical-ai-humanoid-robotics-book/edit/main/',

          include: ['**/*.md','**/*.mdx'],
        },

        blog: false,

        theme: {
          // 🔥 ONLY ONE CSS FILE — clean build
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};

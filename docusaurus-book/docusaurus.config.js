// // docusaurus.config.js
// module.exports = {
//   title: 'Physical AI & Humanoid Robotics',
//   tagline: 'AI Systems in the Physical World',
//   url: 'http://localhost:3000', // your website URL (for deployment, update later)
//   baseUrl: '/',
//   onBrokenLinks: 'throw',
//   onBrokenMarkdownLinks: 'warn',
//   favicon: 'img/favicon.ico',
//   organizationName: 'YourOrg', // Usually GitHub org/user
//   projectName: 'physical-ai-book', // Usually repo name
//   presets: [
//     [
//       '@docusaurus/preset-classic',
//       {
//         docs: {
//           path: 'docs',
//           routeBasePath: '/', // serve docs at root
//           sidebarPath: require.resolve('./sidebars.js'),
//           editUrl: 'https://github.com/YourOrg/physical-ai-book/edit/main/',
//         },
//         blog: false, // disable blog
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
  url: 'https://zartasha-khan123.github.io', // for GitHub Pages deployment
  baseUrl: '/', // if you deploy to subfolder change accordingly
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'zartasha-khan123', // your GitHub username
  projectName: 'physical-ai-humanoid-robotics-book', // your GitHub repo name
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          path: 'docs',
          routeBasePath: '/', // serve docs at root
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/zartasha-khan123/physical-ai-humanoid-robotics-book/edit/main/docs/',
          include: ['**/*.md'], // include all markdown files
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};

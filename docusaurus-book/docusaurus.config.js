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


// docusaurus.config.js
module.exports = {
  title: 'Physical AI & Humanoid Robotics',
  tagline: 'AI Systems in the Physical World',
  url: 'http://localhost:3000', // website URL
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'YourOrg', // GitHub org/user
  projectName: 'physical-ai-book', // repo name
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          path: 'docs',
          routeBasePath: '/', // serve docs at root
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/zartasha-khan123/physical-ai-humanoid-robotics-book/edit/main/docs/',
           include: ['**/*.md'], // ensure all md files are included
          includeCurrentVersion: true,
        },
        blog: false, // disable blog
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};

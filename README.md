# Personal Website

Welcome to my personal page!  
Powered by [Jekyll](https://jekyllrb.com/) and the [al-folio](https://github.com/alshedivat/al-folio) theme.

## Features

- Responsive design for desktop and mobile
- Publication and project showcase
- Integrated blog and news sections
- Social media links and icons
- Easy customization via YAML and Markdown

## Getting Started

1. **Install dependencies**  
   Make sure you have Ruby and Bundler installed.  
   Then run:
   ```sh
   bundle install
   ```

2. **Serve locally**  
   Start the development server:
   ```sh
   bundle exec jekyll serve
   ```
   Visit `http://localhost:4000` in your browser.

3. **Customize your content**  
   - Edit `_config.yml` for site settings
   - Add your info to `_pages/about.md`
   - Update projects in `_projects/`
   - Add publications in `_bibliography/papers.bib`
   - Configure social links in `_data/coauthors.yml` and `_includes/social.html`

## Deployment

Deploy to GitHub Pages using the provided script:
```sh
bin/deploy
```
Or push to your `gh-pages` branch.

## Contributing

Contributions are welcome!  
See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the [MIT License](LICENSE).
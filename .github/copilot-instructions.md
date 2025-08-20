# Roberts Lab Resources Repository

The Roberts Lab Resources repository is a documentation and handbook site for the Roberts Lab at the University of Washington. It contains lab protocols, equipment manuals, computing guides, and general lab resources built with MkDocs and deployed to GitHub Pages.

Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.

## Working Effectively

### Environment Setup and Dependencies
- Install Python 3.7+ (Python 3.12+ recommended)
- Install dependencies: `pip install -r docs/requirements.txt`
  - This installs mkdocs-material and all required dependencies
  - Installation takes approximately 30-60 seconds under normal conditions
  - **May fail due to network timeouts or firewall limitations** - document any installation issues
  - Alternative: `pip install mkdocs-material` (single package installs all dependencies)

### Building and Testing the Documentation
- **CRITICAL TIMING**: Build the documentation: `mkdocs build`
  - Takes approximately 4 seconds to complete. NEVER CANCEL.
  - Set timeout to 30+ seconds for safety
  - Produces warnings about missing links and unrecognized files - this is NORMAL
  - Output directory: `site/`
- Test the development server: `mkdocs serve --dev-addr=0.0.0.0:8000`
  - Serves on http://localhost:8000
  - Hot-reloads on file changes
  - NEVER CANCEL - keeps running until stopped with Ctrl+C
  - Set timeout to appropriate duration for testing needs

### Validation Requirements
- **MANDATORY**: After making documentation changes, ALWAYS run `mkdocs build` to validate syntax
- **MANDATORY**: Start development server and manually test navigation to changed pages
- **SCENARIO VALIDATION**: For content changes, navigate to at least 3 different sections:
  1. Main index page (docs/index.md)
  2. A computing guide (e.g., klone_quick-start.md)
  3. A protocol (e.g., protocols/resazurin-assay.md)
- Verify all internal links work and pages render correctly
- Check that new content appears in navigation if added to mkdocs.yml

## Repository Structure and Navigation

### Key Directories
- `docs/` - Main documentation source files (Markdown)
  - `index.md` - Homepage content
  - Computing guides (klone_*, mox_*, raven_*)
  - Lab procedures and protocols
  - Safety and organizational documentation
- `protocols/` - Lab protocol files and commercial kit documentation
- `equipment_manuals/` - Equipment manuals and guides
- `.github/workflows/` - GitHub Actions for auto-deployment and validation
- `mkdocs.yml` - MkDocs configuration and site navigation

### Configuration Files
- `mkdocs.yml` - Site configuration, theme settings, and navigation structure
- `docs/requirements.txt` - Python dependencies (mkdocs-material)
- `.readthedocs.yml` - ReadtheDocs configuration (alternative deployment)

## Common Development Tasks

### Adding New Documentation
1. Create new `.md` file in appropriate `docs/` subdirectory
2. Add entry to `nav:` section in `mkdocs.yml` if you want it in navigation
3. Use proper Markdown syntax with front matter if needed
4. ALWAYS test with `mkdocs build` and `mkdocs serve` before committing

### Editing Existing Content
1. Edit the `.md` file directly in `docs/` directory
2. Follow existing formatting and style conventions
3. ALWAYS validate with build and development server
4. Test that links and references still work

### Protocol Management
- Lab protocols are stored in both `docs/protocols/` and root-level `protocols/`
- Commercial protocols and kit manuals go in `protocols/Commercial_Protocols/`
- Equipment manuals go in `equipment_manuals/`
- Always follow existing naming conventions

## Continuous Integration and Deployment

### GitHub Actions Workflows
- **Auto-deployment**: `.github/workflows/mkdocs-material-theme.yml`
  - Triggers on push to master/main branches
  - Builds and deploys to GitHub Pages automatically
  - Takes approximately 2-3 minutes. NEVER CANCEL.
  - Deploys to https://robertslab.github.io/resources/
- **URL Checking**: `.github/workflows/urlchecker-md-files.yml`
  - Validates all links in markdown files
  - Runs on every push, takes 1-2 minutes
  - Set to force_pass: true (warnings don't fail build)
- **Greetings**: `.github/workflows/greetings.yml`
  - Welcomes new contributors automatically

### Manual Deployment Commands
- `mkdocs gh-deploy --force` - Deploy to GitHub Pages manually
  - Use only when needed to override automatic deployment
  - Takes 30-60 seconds. Set timeout to 120+ seconds.

## Validation and Quality Assurance

### Pre-commit Validation
- ALWAYS run `mkdocs build` before committing changes
- Check for new warnings or errors in build output
- Start development server and manually test changed pages
- Verify navigation structure if mkdocs.yml was modified

### Content Quality Guidelines
- Follow existing Markdown formatting conventions
- Use proper heading hierarchy (# ## ### ####)
- Include code blocks with language specification when applicable
- Test all internal and external links when possible
- Maintain consistent terminology across lab documentation

### Common Build Warnings (EXPECTED)
The following warnings are normal and expected during builds:
- "Excluding 'README.md' from the site because it conflicts with 'index.md'"
- "The following pages exist in the docs directory, but are not included in the 'nav' configuration:" (lists unused .md files)
- Unrecognized relative links to files outside docs/ directory (e.g., '../lab_safety_docs/')
- Missing target files for cross-references (e.g., './r_packages_installs.R', 'cfx_plate_template.csv')
- Anchor link warnings for chemical SOP references (e.g., '#rnazol_rt', '#isopropanol')
- Links to external repositories or broken external URLs in Pubathon.md
- Missing navigation entries for certain protocol files (ATPase.md, etc.)

### Build Success Indicators
A successful build will:
- Complete in ~1 second 
- Show "Documentation built in X.XX seconds" message
- Generate `site/` directory with HTML files
- Not show any ERROR messages (warnings are acceptable)

## Technical Details

### Dependencies and Requirements
- Python 3.7+ (tested with 3.12)
- mkdocs-material package (installs mkdocs and all dependencies)
- No additional build tools or compilers required
- No database or external services needed for local development

### Performance Expectations
- **NEVER CANCEL** any build or deployment commands
- Build time: ~1 second (set timeout to 30+ seconds for safety)
- Development server startup: ~1-2 seconds
- Full site deployment via GitHub Actions: 2-3 minutes (set timeout to 300+ seconds)
- URL checking workflow: 1-2 minutes (set timeout to 180+ seconds)
- Dependency installation: 15-60 seconds (set timeout to 120+ seconds)

### Troubleshooting
- **Network Installation Issues**: `pip install mkdocs-material` may fail due to network timeouts or firewall limitations
  - If installation fails, document the specific error message
  - Workaround: Use basic mkdocs with readthedocs theme for validation: temporarily change `theme: name: material` to `theme: name: readthedocs` in mkdocs.yml
- If build fails, check for Markdown syntax errors in recently changed files
- Missing files referenced in navigation will cause warnings but not failures
- Development server issues usually resolve with restart
- Network timeouts during deployment are temporary - retry after brief wait

## Working with Specific Content Types

### Computing Guides
- Klone, Mox, and Raven computing cluster documentation
- Include exact commands, file paths, and expected outputs
- Test commands when possible or note when testing isn't feasible
- Update container references and software versions as needed

### Lab Protocols
- Step-by-step procedures with timing and safety information
- Include equipment requirements and safety considerations
- Reference related protocols and cross-link appropriately
- Maintain version history for significant protocol changes

### Equipment Documentation
- Manuals and guides stored in `equipment_manuals/`
- Include model numbers, purchase dates, and maintenance schedules
- Link to manufacturer resources when available
- Document troubleshooting steps and common issues

This repository serves as the central knowledge base for Roberts Lab operations. Always prioritize accuracy, completeness, and usability when making changes to ensure lab members can efficiently find and use the information they need.
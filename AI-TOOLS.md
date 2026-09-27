# Using this repository with AI tools

This repository works with any AI tool that can read GitHub. Every tool reads the same rules:
`AGENTS.md` is the master file. The small files below exist only because some tools look for
their own filename; each one points back to `AGENTS.md` and repeats the rules most often missed.

| Tool | File it reads automatically | What to do |
|---|---|---|
| OpenAI Codex, Cursor, GitHub Copilot agent, Jules, Aider, Windsurf, Zed, Amp, Factory, opencode | `AGENTS.md` | Open the repository. Codex setup script: `bash scripts/setup.sh` |
| Claude Code, Claude projects | `CLAUDE.md` | Open the repository, or add `CLAUDE.md` and `AGENTS.md` as project knowledge |
| Gemini CLI, Gemini Code Assist | `GEMINI.md` | Open the repository |
| GitHub Copilot chat | `.github/copilot-instructions.md` | Nothing; Copilot loads it in this repository |
| Cursor (rules) | `.cursor/rules/ocean-brand.mdc` | Nothing; always applied |
| ChatGPT projects | `brand/CHATGPT-PROJECT-INSTRUCTIONS.md` | Paste it into the project instructions and upload the files it lists |
| Base44, Lovable, Bolt, v0, Replit and other app builders | `brand/AI-APP-BUILDER-INSTRUCTIONS.md` and `web-kit/` | See below |
| Tools that load Agent Skills (Base44 agents, Claude, Perplexity Computer and others) | `skills/ocean-brand/SKILL.md` | Add the skill folder; Base44 agent skills follow the open Agent Skills format ([Base44 docs](https://docs.base44.com/developers/backend/overview/skills)) |
| Perplexity Computer and any tool that reads a repository index | `llms.txt` | Point the tool at the repository |

## What each kind of tool can do

- **Tools that run code** (Codex, Claude Code, Cursor, Copilot agent, Gemini CLI, Perplexity
  Computer): build decks, proposals, reports and contracts with the pipelines, which enforce the
  rules in code. Run `npm test`, `npm run starter` and `npm run documents` before and after a
  change.
- **Chat tools that cannot run code** (ChatGPT chat, Claude chat, Gemini chat): write content
  and review work. Decks they draw by hand are not rule-checked; build them with a code-running
  tool, or check them against `brand/DECK-CHECKLIST.md` and `scripts/qa.py`.
- **App and site builders** (Base44, Lovable, Bolt, v0, Replit): build web apps and sites
  with `web-kit/` and the app-builder instructions. They do not build decks or documents.

## Base44 and other app builders

Base44 connects to a repository that contains a web or full-stack app it can build and run,
which this brand repository is not ([Base44 docs](https://docs.base44.com/Getting-Started/importing-from-github)).
So the app lives in its own repository and takes the brand from here:

1. Create or open the app in Base44 (or connect the app's own repository).
2. Copy `web-kit/` from this repository into the app, for example `src/brand/ocean/`, and
   import `ocean.css` at the app root. With Tailwind, add `tailwind.preset.js` to `presets`.
3. Paste `brand/AI-APP-BUILDER-INSTRUCTIONS.md` into the app's instructions or knowledge.
   It stays under 10,000 characters because Base44 sends only the first 10,000 characters of
   an app's custom instructions to its agent ([Base44 docs](https://docs.base44.com/developers/white-label/custom-instructions)).
4. When the brand changes, rerun `python3 scripts/build_web_kit.py` here and copy `web-kit/` again.

`web-kit/example.html` shows the kit working: header, hero, emphasis, cards, pairings and a
notice footer.

## Keeping every tool in sync

- Change rules in `AGENTS.md`, `brand/decisions.md` and `brand/BRAND-SYSTEM.md` first, then
  update the pointer files if a most-missed rule changes.
- `npm test` fails if a pointer file stops referencing `AGENTS.md`, if the app-builder
  instructions go over 10,000 characters, if `web-kit/` is out of date with the tokens, or if any
  instruction file names a file that does not exist.

# Worked config example: Grey Matter Knowledge

This is the real brand configuration the toolkit author uses, shown so you can
see a complete filled-in brand before you write your own. It documents the
values that go into the CONFIG block of `template/brand.sty`, the filename
prefix used by the skill and the logo filenames. It contains no logo image
files. Logos are brand assets and are not distributed with the toolkit.

## Accent colour

Grey Matter uses a single orange accent.

- HTML hex: `DE7404`
- RGB triple: `222, 116, 4`

In `brand.sty` this becomes:

```latex
\definecolor{brandAccent}{HTML}{DE7404}
% or, equivalently:
% \definecolor{brandAccent}{RGB}{222,116,4}
```

## Organisation identity

```latex
\newcommand{\brandOrgName}{Grey Matter Knowledge}
\newcommand{\brandStrapline}{AI-Augmented Engineering}
\newcommand{\brandWebsite}{www.greymatterknowledge.com}
\newcommand{\brandIPNotice}{This document is the intellectual property of Grey Matter Knowledge.}
```

## Logo filenames

Grey Matter keeps its two logo files under these names. The light-page logo and
the inverted logo for dark covers both live in `template/assets/`.

```latex
\newcommand{\brandLogo}{Grey_Matter_logo.png}
\newcommand{\brandLogoInverted}{Grey_Matter_logo_inverted.png}
```

The default toolkit names are `logo.png` and `logo-inverted.png`. Grey Matter
overrides them to the names above. Either approach works. Match the filenames
in `brand.sty` to the files you actually drop into `template/assets/`.

## Closing lines

The closing page carries two lines. Grey Matter uses an engagement question
followed by the website.

- Close line 1: `How can we help you build a knowledge-driven engineering team?`
- Close line 2: `www.greymatterknowledge.com`

These two values fill `__CLOSE_LINE_1__` and `__CLOSE_LINE_2__` when the skill
assembles a document.

## Filename prefix

Grey Matter prefixes every generated document with `GM-`. A document titled
"Pilot Study" is written as `GM-Pilot-Study.qmd` and renders to
`GM-Pilot-Study.pdf`. The toolkit default prefix is `Doc-`. Set your own prefix
in the skill configuration described in `SKILL.md`.

## Summary table

| Config item | Grey Matter value |
|-------------|-------------------|
| Accent colour (hex) | `DE7404` |
| Accent colour (RGB) | `222, 116, 4` |
| Organisation name | Grey Matter Knowledge |
| Strapline | AI-Augmented Engineering |
| Website | www.greymatterknowledge.com |
| Close line 1 | How can we help you build a knowledge-driven engineering team? |
| Close line 2 | www.greymatterknowledge.com |
| Filename prefix | `GM-` |
| Light logo file | `Grey_Matter_logo.png` |
| Inverted logo file | `Grey_Matter_logo_inverted.png` |

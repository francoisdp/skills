# Brand assets

Place two image files in this folder:

- `logo.png` for a logo that reads well on a light page header. Used in the top margin of every content page.
- `logo-inverted.png` for a logo that reads well on a dark background. Used on the cover page and the closing page, both of which have a dark background.

The filenames must match the `\brandLogo` and `\brandLogoInverted` macros in `../brand.sty`. If you change the filenames there, change them here to match.

Until both files exist, the template still compiles. The cover and closing pages fall back to a text wordmark built from your organisation name, while the page header omits the logo. Drop the two files in and the images appear automatically on the next render.

A logo width of roughly 1200 pixels and a transparent background give the cleanest result. PDF and JPG also work, in which case change the extension in the macro names in `brand.sty`.

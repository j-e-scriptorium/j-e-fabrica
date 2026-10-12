"""Provenance tiers and judgment flags for the review package.

Tier is about how the text reached this project, not about the source's own quality.
  A1  Handbook of North American Indians vol. 13 (2001), read in the PDF supplied by the user; page-cited.
  A2  Original or standard printed text read in a full-text copy online (Internet Archive, Project Gutenberg,
      UNL Lewis & Clark edition, digitised Indian Office reports, BAE series).
  B   Reference article read online (Wikipedia, Historical Marker Database, Handbook of Texas, Encyclopedia of
      the Great Plains, Encyclopedia of Saskatchewan, Dictionary of Canadian Biography, NPS pages).
  C   Second-hand or recalled: the work itself was not read in this project (quoted through another page,
      a reader's highlight, or recalled from general knowledge). Treat as a lead to verify.
"""
import re

C_MARKERS = ('recalled', 'not checked', 'as quoted in', 'reader’s highlight', "reader's highlight",
             'as summarized in Wikipedia', 'Brooks, Captives', 'Thornton, American Indian',
             'Fenn, Pox', 'Calloway', 'Burnet to the Indian Office', 'Hämäläinen', 'Gaignard',
             'Ray, Indians in the Fur Trade', 'Moodie', 'Ewers', 'West, The Contested', 'Isenberg',
             'Frazer, Forts', 'Hannings', 'Milloy', 'Binnema', 'Kavanagh, Comanche Political')
B_MARKERS = ('Wikipedia', 'Historical Marker Database', 'hmdb', 'Handbook of Texas', 'Encyclopedia of the Great Plains',
             'Encyclopedia of Saskatchewan', 'DCB', 'Dictionary of Canadian Biography', 'nps.gov', 'National Park Service',
             'North American Forts', 'Kansapedia', 'northamericanforts', 'State Historical Society', 'history.nd.gov')
A2_MARKERS = ('Swanton', 'Mooney', 'Clark', 'Lewis & Clark', 'Annual Report of the Commissioner', 'Commissioner of Indian',
              'ARCIA', 'Indian Office', 'Hayden', 'Grinnell', 'Warren', 'Morse', 'Denig', 'Henry the younger', 'Fletcher',
              'Frémont', 'Thompson', 'Maximilian', 'Pike', 'Catlin', 'Raynolds', 'Russell, Journal', 'James, Account',
              'Gregg', 'Garrard', 'Tixier', 'Larpenteur', 'Mallery', 'Kappler', 'Stevens', 'Bradbury', 'Brackenridge',
              'Hodge', 'Irving', 'Parkman', 'Larocque', 'Mackenzie', 'Long expedition', 'Doty', 'Dorsey', 'Hornaday',
              'Steiner', 'Umfreville', 'Tabeau', 'Truteau', 'Keating')


def tier(src: str) -> str:
    """Weakest component wins when a record cites several works."""
    s = src or ''
    hb = 'Handbook of North American Indians, vol. 13' in s
    if any(k in s for k in ('recalled', 'not checked', 'as quoted in', 'highlight', 'as summarized in')):
        return 'C'
    if any(k in s for k in C_MARKERS) and not hb:
        return 'C'
    if any(k in s for k in B_MARKERS):
        return 'B'
    if hb:
        return 'A1'
    if any(k in s for k in A2_MARKERS):
        return 'A2'
    return 'C'


FLAG_RULES = [
    ('place_centre_ours', r'centre ours|center ours|centre of the range|\(a range'),
    ('date_ours', r'date ours|dated? (?:only )?by|date from|about \d{4}\)'),
    ('identification_judged', r'identif|probabl[ey]|thought by some|usually read as'),
    ('kept_off_track', r'kept off'),
    ('partial_group', r'\(part|a band\b|part of the|delegation|war party|visit'),
    ('assumed_quantity', r'assumed|\(ours\)|ours\)|camp size ours'),
    ('recalled', r'recalled|not checked'),
]


def flags(raw: str, basis: str = '', loc: str = '', whole=True) -> list:
    t = f'{raw} {basis}'
    out = [name for name, rx in FLAG_RULES if re.search(rx, t, re.I)]
    if loc == 'inferred':
        out.append('place_placed_by_us')
    if basis and re.search(r'×', basis):
        out.append('multiplier_' + ('stated_by_source' if re.search(r'stated|Thompson|Lehmer|Opler|Levy', basis) else 'ours'))
    if whole is False and 'kept_off_track' not in out:
        out.append('kept_off_track')
    return sorted(set(out))

"""Provenance tiers and judgment flags for the review package.

Tier is about how the text reached this project, not about the source's own quality.
  A1  A work read in a PDF supplied by the project's owner, page-cited: Handbook of North American Indians vols. 10, 11
      and 13; the 1890 census Report on Indians Taxed and Indians Not Taxed (1894), its tables read from the page
      images; Hämäläinen, The Comanche Empire (2008); Kavanagh, Comanche Political History (1996);
      Fenn, Pox Americana (2001, an EPUB without print pages, cited by chapter); West, The Contested Plains (1998,
      likewise cited by chapter); Winfrey and Day, eds., The Indian Papers of Texas and the Southwest, vols. 1–5 (1966; repr. 1995);
      Bolton's De Mézières papers (1914); Henday, Cocking and La Vérendrye in Burpee's editions; Ewers (1955); Denig (BAE 46);
      Jenness (1938); Bray, "Teton Sioux Population History" (1994); Morton, A History of the Canadian West (1939);
      Binnema, Common and Contested Ground (2001);
      the Canadian Department of Indian Affairs reports of 1884–1900.
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
             'Calloway', 'Burnet to the Indian Office',
             'Ray, Indians in the Fur Trade', 'Moodie', 'Ewers', 'West, The Contested', 'Isenberg',
             'Frazer, Forts', 'Hannings', 'Milloy', 'Binnema')
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
    hb = any(k in s for k in ('Handbook of North American Indians, vol. 1', 'Report on Indians Taxed', 'Comanche Empire (2008), p', 'Comanche Political History: An Ethnohistorical Perspective, 1706–1875 (1996), p', 'Pox Americana (2001), ch', 'Rush to Colorado (1998), ch', 'The Indian Papers of Texas and the Southwest, 1825–1916, vol.', 'Louisiana–Texas Frontier, 1768–1780 (1914), vol', '“York Factory to the Blackfeet Country” (1907), p', '“An Adventurer from Hudson Bay” (1908), p', 'Vérendrye and His Sons (1927), p', 'Blackfoot Indian Culture (BAE Bulletin 159, 1955), p', '(BAE 46th Annual Report, 1930), p', 'Sarcee Indians of Alberta (1938), p', 'read from the page images of the', 'Nebraska History 75 (1994)', 'Canadian West to 1870–71 (1939), p', 'Northwestern Plains (2001), p', 'Department of Indian Affairs, Annual Report for the year ended', 'Department of Indian Affairs, Annual Report for the year ended 30 June', 'The Contested Plains (1998), p', 'The Contested Plains (1998), c. p', 'Handbook of North American Indians 13 (2001), p'))
    if 'Hämäläinen' in s and 'Comanche Empire (2008), p' not in s: return 'C'
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

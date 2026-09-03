import re
from pathlib import Path


# ============================================================
# 1. CÁC RULE HEADER
# ============================================================

RULES = [
    # --------------------------------------------------------
    # Case: #### (XXI) (Ek II, 4) (It. 7)
    #       -> {#21}
    # --------------------------------------------------------
    {
        "regex": re.compile(
            r"^(####)\s+\(([IVXLCDM]+)\)\s+(.+?)[ \t]*$",
            re.MULTILINE
        ),
        "anchor": lambda m: str(roman_to_int(m.group(2))),
    },

    # --------------------------------------------------------
    # Case:
    # ## 2. Giới đức (Sīla)
    # ### 2.1. Giới đức nhỏ (Cūḷasīla)
    #
    # -> {#2}
    # -> {#2.1}
    # --------------------------------------------------------
    {
        "regex": re.compile(
            r"^(#{2,})\s+(\d+(?:\.\d+)*\.)\s+(.+?)[ \t]*$",
            re.MULTILINE
        ),
        "anchor": lambda m: m.group(2).rstrip("."),
    },
    # --------------------------------------------------------
    # Case:
    # ### AN 10.189 Con Đường Thiện Lành Ariyamaggasutta
    # ### AN 1.11--20 Nīvaraṇappahānavagga
    #
    # -> {#189}
    # -> {#11-20}
    # --------------------------------------------------------
    {
        "regex": re.compile(
            r"^(#{2,})\s+AN\s+\d+\.(\d+(?:\s*(?:--|–|-)\s*\d+)?)\s+(.+?)[ \t]*$",
            re.MULTILINE
        ),
        "anchor": lambda m: re.sub(
            r"\s*(?:--|–|-)\s*",
            "-",
            m.group(2)
        ),
    },
]


# ============================================================
# 2. ROMAN -> INTEGER
# ============================================================

def roman_to_int(s):
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    total = 0
    prev = 0

    for char in reversed(s.upper()):
        value = values[char]

        if value < prev:
            total -= value
        else:
            total += value

        prev = value

    return total


# ============================================================
# 3. XỬ LÝ FILE
# ============================================================

def process_file(filename):
    path = Path(filename)
    content = path.read_text(encoding="utf-8")

    original_content = content

    for rule in RULES:

        def replace(match):
            header = match.group(0).rstrip()

            # Không thêm anchor nếu đã có
            if re.search(r"\{#[^}]+\}\s*$", header):
                return header

            anchor = rule["anchor"](match)

            return f"{header}{{#{anchor}}}"

        content = rule["regex"].sub(replace, content)

    if content != original_content:
        path.write_text(content, encoding="utf-8")
        print(f"Updated: {filename}")
    else:
        print(f"No change: {filename}")


# ============================================================
# 4. INPUT = LIST FILES
# ============================================================

files = [
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-01-001-the-chapter-on-what-occupies-the-mind.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-01-002-the-chapter-on-giving-up-the-hindrances.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-01-003-the-chapter-on-the-useless-mind.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-01-004-the-chapter-on-the-wild-mind.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-01-005-the-chapter-on-a-spike.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-01-006-the-chapter-on-a-finger-snap.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-01-007-the-chapter-on-arousing-energy.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-01-008-the-chapter-on-good-friends.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-01-009-the-chapter-on-negligence.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-01-010-the-chapter-on-negligence-2nd.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-01-011-the-chapter-on-not-the-teaching.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-01-012-the-chapter-on-non-offense.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-01-013-the-chapter-on-one-person.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-01-014-seven-chapters-on-the-foremost-persons.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-01-015-three-chapters-on-the-impossible.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-01-016-four-chapters-on-one-thing-1.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-01-017-four-chapters-on-one-thing-2.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-01-018-four-chapters-on-one-thing-3.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-01-019-four-chapters-on-one-thing-4.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-01-020-the-chapter-on-inspiring-qualities.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-01-021-another-chapter-on-a-finger-snap.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-01-022-the-chapter-on-mindfulness-of-the-body.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-01-023-the-chapter-on-freedom-from-death.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-02-000-chapter-2.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-02-001-the-chapter-on-punishments.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-02-002-the-chapter-on-disciplinary-issues.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-02-003-the-chapter-on-fools.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-02-004-the-chapter-on-the-peaceful-mind.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-02-005-the-chapter-on-assemblies.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-02-006-the-chapter-on-persons.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-02-007-the-chapter-on-happiness.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-02-008-the-chapter-with-a-foundation.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-02-009-the-chapter-on-two-things.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-02-010-the-chapter-on-fools.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-02-011-the-chapter-on-hopes-that-are-hard-to-give-up.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-02-012-the-chapter-on-aspiration.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-02-013-the-chapter-on-giving.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-02-014-the-chapter-on-welcome.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-02-015-the-chapter-on-attainment.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-02-016-the-chapter-of-abbreviated-texts-beginning-with-anger.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-02-017-the-chapter-of-abbreviated-texts-on-monastic-law.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-03-000-chapter-3.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-03-001-the-chapter-on-fools.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-03-002-the-chapter-on-the-chariot-maker.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-03-003-the-chapter-on-persons.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-03-004-the-chapter-on-messengers-of-the-gods.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-03-005-a-short-chapter.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-03-006-the-chapter-on-brahmins.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-03-007-the-great-chapter.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-03-008-the-chapter-with-ananda.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-03-009-the-chapter-on-ascetics.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-03-010-the-chapter-on-a-lump-of-salt.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-03-011-the-chapter-on-awakening.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-03-012-the-chapter-on-bound-for-loss.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-03-013-the-chapter-at-kusinara.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-03-014-the-chapter-on-a-warrior.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-03-015-the-chapter-on-good-fortune.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-03-016-the-chapter-on-practices.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-04-000-chapter-4.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-04-001-the-chapter-at-wares-village.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-04-002-the-chapter-on-walking.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-04-003-the-chapter-at-uruvela.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-04-004-the-chapter-on-situations.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-04-005-the-chapter-with-rohitassa.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-04-006-the-chapter-on-overflowing-merit.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-04-007-the-chapter-on-deeds-of-substance.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-04-008-the-chapter-on-guaranteed.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-04-009-the-chapter-on-confirmed.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-04-010-the-chapter-on-demons.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-04-011-the-chapter-on-gods-of-the-clouds.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-04-012-the-chapter-with-kesi.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-04-013-the-chapter-on-perils.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-04-014-the-chapter-on-persons.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-04-015-the-chapter-on-brightness.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-04-016-the-chapter-on-faculties.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-04-017-the-chapter-on-practice.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-04-018-the-chapter-on-intention.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-04-019-the-chapter-on-brahmins.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-04-020-the-great-chapter.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-04-021-the-chapter-on-a-good-person.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-04-022-the-chapter-on-assemblies.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-04-023-the-chapter-on-bad-conduct.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-04-024-the-chapter-on-deeds.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-04-025-the-chapter-on-perils-of-offenses.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-04-026-the-chapter-on-direct-knowledges.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-04-027-the-chapter-on-ways-of-performing-deeds.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-04-028-abbreviated-texts-beginning-with-greed.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-05-000-chapter-5.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-05-001-the-chapter-on-powers-of-a-trainee.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-05-002-the-chapter-on-powers.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-05-003-the-chapter-on-five-factors.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-05-004-the-chapter-with-sumana.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-05-005-the-chapter-with-king-munda.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-05-006-the-chapter-on-hindrances.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-05-007-the-chapter-on-perceptions.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-05-008-the-chapter-on-a-warrior.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-05-009-the-chapter-on-senior-mendicants.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-05-010-the-chapter-with-kakudha.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-05-011-the-chapter-on-living-comfortably.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-05-012-the-chapter-at-andhakavinda.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-05-013-the-chapter-on-sick.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-05-014-the-chapter-on-kings.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-05-015-the-chapter-at-tikandaki.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-05-016-the-chapter-on-the-true-teaching.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-05-017-the-chapter-on-resentment.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-05-018-the-chapter-on-a-lay-follower.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-05-019-the-chapter-on-wilderness-dwellers.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-05-020-the-chapter-on-brahmins.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-05-021-the-chapter-with-kimbila.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-05-022-the-chapter-on-abuse.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-05-023-the-chapter-on-long-wandering.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-05-024-the-chapter-on-a-resident-mendicant.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-05-025-the-chapter-on-bad-conduct.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-05-026-the-chapter-on-ordination.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-06-000-chapter-6.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-06-001-the-chapter-on-worthy-of-offerings.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-06-002-the-chapter-on-warm-hearted.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-06-003-the-chapter-on-unsurpassable.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-06-004-the-chapter-on-deities.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-06-005-the-chapter-with-dhammika.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-06-006-the-great-chapter.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-06-007-the-chapter-on-deities.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-06-008-the-chapter-on-perfection.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-06-009-the-chapter-on-coolness.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-06-010-the-chapter-on-benefit.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-06-011-the-chapter-on-triads.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-06-012-the-chapter-on-the-ascetic-life.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-07-000-chapter-7.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-07-001-the-chapter-on-wealth.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-07-002-the-chapter-on-tendencies.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-07-003-the-chapter-on-the-vajji-seven.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-07-004-the-chapter-on-deities.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-07-005-the-chapter-on-a-great-sacrifice.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-07-006-the-chapter-on-the-undeclared-points.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-07-007-the-great-chapter.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-07-008-the-chapter-on-the-monastic-law.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-07-009-the-chapter-on-ascetics.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-08-000-chapter-8.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-08-001-the-chapter-on-love.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-08-002-the-great-chapter.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-08-003-the-chapter-on-householders.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-08-004-the-chapter-on-giving.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-08-005-the-chapter-on-sabbath.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-08-006-the-chapter-on-gotami.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-08-007-the-chapter-on-earthquakes.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-08-008-the-chapter-on-pairs.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-08-009-the-chapter-on-mindfulness.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-08-010-the-chapter-on-similarity.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-09-000-chapter-9.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-09-001-the-chapter-on-awakening.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-09-002-the-chapter-on-the-lion-s-roar.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-09-003-the-chapter-on-abodes-of-sentient-beings.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-09-004-the-great-chapter.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-09-005-the-chapter-on-similarity.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-09-006-the-chapter-on-a-safe-place.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-09-007-the-chapter-on-mindfulness-meditation.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-09-008-the-chapter-on-right-efforts.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-09-009-the-chapter-on-bases-of-psychic-power.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-09-010-the-chapter-on-bases-of-psychic-power2.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-10-000-chapter-10.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-10-001-the-chapter-on-benefits.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-10-002-the-chapter-on-a-protector.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-10-003-the-great-chapter.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-10-004-the-chapter-with-upali.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-10-005-the-chapter-on-abuse.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-10-006-the-chapter-on-your-own-mind.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-10-007-the-chapter-on-pairs.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-10-008-the-chapter-on-if-you-want.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-10-009-the-chapter-on-senior-mendicants.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-10-010-the-chapter-with-upali.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-10-011-the-chapter-on-perceptions-for-ascetics.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-10-012-the-chapter-on-the-ceremony-of-descent.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-10-013-the-chapter-on-purified.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-10-014-the-chapter-on-good.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-10-015-the-chapter-on-the-noble-path.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-10-016-the-chapter-on-persons.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-10-017-the-chapter-with-janussoni.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-10-018-the-chapter-on-good.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-10-019-the-chapter-on-the-noble-path.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-10-020-another-chapter-on-persons.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-10-021-the-chapter-on-the-body-born-of-deeds.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-10-022-the-chapter-on-similarity.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-11-000-chapter-11.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-11-001-the-chapter-on-dependence.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-11-002-the-chapter-on-recollection.md",
"/Users/ng/projects/nikaya2/docs/kinhtangchi/sujato-vi/an-11-003-the-chapter-on-similarity.md",
]

for file in files:
    process_file(file)
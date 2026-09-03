from pathlib import Path
import re
import json
import sys


def get_range(file_path: str):
    text = Path(file_path).read_text(encoding="utf-8")

    min_num = None
    max_num = None

    for line in text.splitlines():
        line = line.strip()

        if not line.startswith("### "):
            continue

        # Hỗ trợ:
        # 1.1
        # 1.1-10
        # 1.1--10
        # 1.1–10
        # 1.1—10
        match = re.search(
            r"\d+\.(\d+)(?:\s*[-–—]+\s*(\d+))?",
            line
        )

        if not match:
            continue

        start = int(match.group(1))
        end = int(match.group(2)) if match.group(2) else start

        min_num = start if min_num is None else min(min_num, start)
        max_num = end if max_num is None else max(max_num, end)

    return min_num, max_num


def main():

    filex = [
"../../docs/kinhtangchi/sujato-vi/an-01-001-the-chapter-on-what-occupies-the-mind.md",
"../../docs/kinhtangchi/sujato-vi/an-01-002-the-chapter-on-giving-up-the-hindrances.md",
"../../docs/kinhtangchi/sujato-vi/an-01-003-the-chapter-on-the-useless-mind.md",
"../../docs/kinhtangchi/sujato-vi/an-01-004-the-chapter-on-the-wild-mind.md",
"../../docs/kinhtangchi/sujato-vi/an-01-005-the-chapter-on-a-spike.md",
"../../docs/kinhtangchi/sujato-vi/an-01-006-the-chapter-on-a-finger-snap.md",
"../../docs/kinhtangchi/sujato-vi/an-01-007-the-chapter-on-arousing-energy.md",
"../../docs/kinhtangchi/sujato-vi/an-01-008-the-chapter-on-good-friends.md",
"../../docs/kinhtangchi/sujato-vi/an-01-009-the-chapter-on-negligence.md",
"../../docs/kinhtangchi/sujato-vi/an-01-010-the-chapter-on-negligence-2nd.md",
"../../docs/kinhtangchi/sujato-vi/an-01-011-the-chapter-on-not-the-teaching.md",
"../../docs/kinhtangchi/sujato-vi/an-01-012-the-chapter-on-non-offense.md",
"../../docs/kinhtangchi/sujato-vi/an-01-013-the-chapter-on-one-person.md",
"../../docs/kinhtangchi/sujato-vi/an-01-014-seven-chapters-on-the-foremost-persons.md",
"../../docs/kinhtangchi/sujato-vi/an-01-015-three-chapters-on-the-impossible.md",
"../../docs/kinhtangchi/sujato-vi/an-01-016-four-chapters-on-one-thing-1.md",
"../../docs/kinhtangchi/sujato-vi/an-01-017-four-chapters-on-one-thing-2.md",
"../../docs/kinhtangchi/sujato-vi/an-01-018-four-chapters-on-one-thing-3.md",
"../../docs/kinhtangchi/sujato-vi/an-01-019-four-chapters-on-one-thing-4.md",
"../../docs/kinhtangchi/sujato-vi/an-01-020-the-chapter-on-inspiring-qualities.md",
"../../docs/kinhtangchi/sujato-vi/an-01-021-another-chapter-on-a-finger-snap.md",
"../../docs/kinhtangchi/sujato-vi/an-01-022-the-chapter-on-mindfulness-of-the-body.md",
"../../docs/kinhtangchi/sujato-vi/an-01-023-the-chapter-on-freedom-from-death.md",
"../../docs/kinhtangchi/sujato-vi/an-02-000-chapter-2.md",
"../../docs/kinhtangchi/sujato-vi/an-02-001-the-chapter-on-punishments.md",
"../../docs/kinhtangchi/sujato-vi/an-02-002-the-chapter-on-disciplinary-issues.md",
"../../docs/kinhtangchi/sujato-vi/an-02-003-the-chapter-on-fools.md",
"../../docs/kinhtangchi/sujato-vi/an-02-004-the-chapter-on-the-peaceful-mind.md",
"../../docs/kinhtangchi/sujato-vi/an-02-005-the-chapter-on-assemblies.md",
"../../docs/kinhtangchi/sujato-vi/an-02-006-the-chapter-on-persons.md",
"../../docs/kinhtangchi/sujato-vi/an-02-007-the-chapter-on-happiness.md",
"../../docs/kinhtangchi/sujato-vi/an-02-008-the-chapter-with-a-foundation.md",
"../../docs/kinhtangchi/sujato-vi/an-02-009-the-chapter-on-two-things.md",
"../../docs/kinhtangchi/sujato-vi/an-02-010-the-chapter-on-fools.md",
"../../docs/kinhtangchi/sujato-vi/an-02-011-the-chapter-on-hopes-that-are-hard-to-give-up.md",
"../../docs/kinhtangchi/sujato-vi/an-02-012-the-chapter-on-aspiration.md",
"../../docs/kinhtangchi/sujato-vi/an-02-013-the-chapter-on-giving.md",
"../../docs/kinhtangchi/sujato-vi/an-02-014-the-chapter-on-welcome.md",
"../../docs/kinhtangchi/sujato-vi/an-02-015-the-chapter-on-attainment.md",
"../../docs/kinhtangchi/sujato-vi/an-02-016-the-chapter-of-abbreviated-texts-beginning-with-anger.md",
"../../docs/kinhtangchi/sujato-vi/an-02-017-the-chapter-of-abbreviated-texts-on-monastic-law.md",
"../../docs/kinhtangchi/sujato-vi/an-03-000-chapter-3.md",
"../../docs/kinhtangchi/sujato-vi/an-03-001-the-chapter-on-fools.md",
"../../docs/kinhtangchi/sujato-vi/an-03-002-the-chapter-on-the-chariot-maker.md",
"../../docs/kinhtangchi/sujato-vi/an-03-003-the-chapter-on-persons.md",
"../../docs/kinhtangchi/sujato-vi/an-03-004-the-chapter-on-messengers-of-the-gods.md",
"../../docs/kinhtangchi/sujato-vi/an-03-005-a-short-chapter.md",
"../../docs/kinhtangchi/sujato-vi/an-03-006-the-chapter-on-brahmins.md",
"../../docs/kinhtangchi/sujato-vi/an-03-007-the-great-chapter.md",
"../../docs/kinhtangchi/sujato-vi/an-03-008-the-chapter-with-ananda.md",
"../../docs/kinhtangchi/sujato-vi/an-03-009-the-chapter-on-ascetics.md",
"../../docs/kinhtangchi/sujato-vi/an-03-010-the-chapter-on-a-lump-of-salt.md",
"../../docs/kinhtangchi/sujato-vi/an-03-011-the-chapter-on-awakening.md",
"../../docs/kinhtangchi/sujato-vi/an-03-012-the-chapter-on-bound-for-loss.md",
"../../docs/kinhtangchi/sujato-vi/an-03-013-the-chapter-at-kusinara.md",
"../../docs/kinhtangchi/sujato-vi/an-03-014-the-chapter-on-a-warrior.md",
"../../docs/kinhtangchi/sujato-vi/an-03-015-the-chapter-on-good-fortune.md",
"../../docs/kinhtangchi/sujato-vi/an-03-016-the-chapter-on-practices.md",
"../../docs/kinhtangchi/sujato-vi/an-04-000-chapter-4.md",
"../../docs/kinhtangchi/sujato-vi/an-04-001-the-chapter-at-wares-village.md",
"../../docs/kinhtangchi/sujato-vi/an-04-002-the-chapter-on-walking.md",
"../../docs/kinhtangchi/sujato-vi/an-04-003-the-chapter-at-uruvela.md",
"../../docs/kinhtangchi/sujato-vi/an-04-004-the-chapter-on-situations.md",
"../../docs/kinhtangchi/sujato-vi/an-04-005-the-chapter-with-rohitassa.md",
"../../docs/kinhtangchi/sujato-vi/an-04-006-the-chapter-on-overflowing-merit.md",
"../../docs/kinhtangchi/sujato-vi/an-04-007-the-chapter-on-deeds-of-substance.md",
"../../docs/kinhtangchi/sujato-vi/an-04-008-the-chapter-on-guaranteed.md",
"../../docs/kinhtangchi/sujato-vi/an-04-009-the-chapter-on-confirmed.md",
"../../docs/kinhtangchi/sujato-vi/an-04-010-the-chapter-on-demons.md",
"../../docs/kinhtangchi/sujato-vi/an-04-011-the-chapter-on-gods-of-the-clouds.md",
"../../docs/kinhtangchi/sujato-vi/an-04-012-the-chapter-with-kesi.md",
"../../docs/kinhtangchi/sujato-vi/an-04-013-the-chapter-on-perils.md",
"../../docs/kinhtangchi/sujato-vi/an-04-014-the-chapter-on-persons.md",
"../../docs/kinhtangchi/sujato-vi/an-04-015-the-chapter-on-brightness.md",
"../../docs/kinhtangchi/sujato-vi/an-04-016-the-chapter-on-faculties.md",
"../../docs/kinhtangchi/sujato-vi/an-04-017-the-chapter-on-practice.md",
"../../docs/kinhtangchi/sujato-vi/an-04-018-the-chapter-on-intention.md",
"../../docs/kinhtangchi/sujato-vi/an-04-019-the-chapter-on-brahmins.md",
"../../docs/kinhtangchi/sujato-vi/an-04-020-the-great-chapter.md",
"../../docs/kinhtangchi/sujato-vi/an-04-021-the-chapter-on-a-good-person.md",
"../../docs/kinhtangchi/sujato-vi/an-04-022-the-chapter-on-assemblies.md",
"../../docs/kinhtangchi/sujato-vi/an-04-023-the-chapter-on-bad-conduct.md",
"../../docs/kinhtangchi/sujato-vi/an-04-024-the-chapter-on-deeds.md",
"../../docs/kinhtangchi/sujato-vi/an-04-025-the-chapter-on-perils-of-offenses.md",
"../../docs/kinhtangchi/sujato-vi/an-04-026-the-chapter-on-direct-knowledges.md",
"../../docs/kinhtangchi/sujato-vi/an-04-027-the-chapter-on-ways-of-performing-deeds.md",
"../../docs/kinhtangchi/sujato-vi/an-04-028-abbreviated-texts-beginning-with-greed.md",
"../../docs/kinhtangchi/sujato-vi/an-05-000-chapter-5.md",
"../../docs/kinhtangchi/sujato-vi/an-05-001-the-chapter-on-powers-of-a-trainee.md",
"../../docs/kinhtangchi/sujato-vi/an-05-002-the-chapter-on-powers.md",
"../../docs/kinhtangchi/sujato-vi/an-05-003-the-chapter-on-five-factors.md",
"../../docs/kinhtangchi/sujato-vi/an-05-004-the-chapter-with-sumana.md",
"../../docs/kinhtangchi/sujato-vi/an-05-005-the-chapter-with-king-munda.md",
"../../docs/kinhtangchi/sujato-vi/an-05-006-the-chapter-on-hindrances.md",
"../../docs/kinhtangchi/sujato-vi/an-05-007-the-chapter-on-perceptions.md",
"../../docs/kinhtangchi/sujato-vi/an-05-008-the-chapter-on-a-warrior.md",
"../../docs/kinhtangchi/sujato-vi/an-05-009-the-chapter-on-senior-mendicants.md",
"../../docs/kinhtangchi/sujato-vi/an-05-010-the-chapter-with-kakudha.md",
"../../docs/kinhtangchi/sujato-vi/an-05-011-the-chapter-on-living-comfortably.md",
"../../docs/kinhtangchi/sujato-vi/an-05-012-the-chapter-at-andhakavinda.md",
"../../docs/kinhtangchi/sujato-vi/an-05-013-the-chapter-on-sick.md",
"../../docs/kinhtangchi/sujato-vi/an-05-014-the-chapter-on-kings.md",
"../../docs/kinhtangchi/sujato-vi/an-05-015-the-chapter-at-tikandaki.md",
"../../docs/kinhtangchi/sujato-vi/an-05-016-the-chapter-on-the-true-teaching.md",
"../../docs/kinhtangchi/sujato-vi/an-05-017-the-chapter-on-resentment.md",
"../../docs/kinhtangchi/sujato-vi/an-05-018-the-chapter-on-a-lay-follower.md",
"../../docs/kinhtangchi/sujato-vi/an-05-019-the-chapter-on-wilderness-dwellers.md",
"../../docs/kinhtangchi/sujato-vi/an-05-020-the-chapter-on-brahmins.md",
"../../docs/kinhtangchi/sujato-vi/an-05-021-the-chapter-with-kimbila.md",
"../../docs/kinhtangchi/sujato-vi/an-05-022-the-chapter-on-abuse.md",
"../../docs/kinhtangchi/sujato-vi/an-05-023-the-chapter-on-long-wandering.md",
"../../docs/kinhtangchi/sujato-vi/an-05-024-the-chapter-on-a-resident-mendicant.md",
"../../docs/kinhtangchi/sujato-vi/an-05-025-the-chapter-on-bad-conduct.md",
"../../docs/kinhtangchi/sujato-vi/an-05-026-the-chapter-on-ordination.md",
"../../docs/kinhtangchi/sujato-vi/an-06-000-chapter-6.md",
"../../docs/kinhtangchi/sujato-vi/an-06-001-the-chapter-on-worthy-of-offerings.md",
"../../docs/kinhtangchi/sujato-vi/an-06-002-the-chapter-on-warm-hearted.md",
"../../docs/kinhtangchi/sujato-vi/an-06-003-the-chapter-on-unsurpassable.md",
"../../docs/kinhtangchi/sujato-vi/an-06-004-the-chapter-on-deities.md",
"../../docs/kinhtangchi/sujato-vi/an-06-005-the-chapter-with-dhammika.md",
"../../docs/kinhtangchi/sujato-vi/an-06-006-the-great-chapter.md",
"../../docs/kinhtangchi/sujato-vi/an-06-007-the-chapter-on-deities.md",
"../../docs/kinhtangchi/sujato-vi/an-06-008-the-chapter-on-perfection.md",
"../../docs/kinhtangchi/sujato-vi/an-06-009-the-chapter-on-coolness.md",
"../../docs/kinhtangchi/sujato-vi/an-06-010-the-chapter-on-benefit.md",
"../../docs/kinhtangchi/sujato-vi/an-06-011-the-chapter-on-triads.md",
"../../docs/kinhtangchi/sujato-vi/an-06-012-the-chapter-on-the-ascetic-life.md",
"../../docs/kinhtangchi/sujato-vi/an-07-000-chapter-7.md",
"../../docs/kinhtangchi/sujato-vi/an-07-001-the-chapter-on-wealth.md",
"../../docs/kinhtangchi/sujato-vi/an-07-002-the-chapter-on-tendencies.md",
"../../docs/kinhtangchi/sujato-vi/an-07-003-the-chapter-on-the-vajji-seven.md",
"../../docs/kinhtangchi/sujato-vi/an-07-004-the-chapter-on-deities.md",
"../../docs/kinhtangchi/sujato-vi/an-07-005-the-chapter-on-a-great-sacrifice.md",
"../../docs/kinhtangchi/sujato-vi/an-07-006-the-chapter-on-the-undeclared-points.md",
"../../docs/kinhtangchi/sujato-vi/an-07-007-the-great-chapter.md",
"../../docs/kinhtangchi/sujato-vi/an-07-008-the-chapter-on-the-monastic-law.md",
"../../docs/kinhtangchi/sujato-vi/an-07-009-the-chapter-on-ascetics.md",
"../../docs/kinhtangchi/sujato-vi/an-08-000-chapter-8.md",
"../../docs/kinhtangchi/sujato-vi/an-08-001-the-chapter-on-love.md",
"../../docs/kinhtangchi/sujato-vi/an-08-002-the-great-chapter.md",
"../../docs/kinhtangchi/sujato-vi/an-08-003-the-chapter-on-householders.md",
"../../docs/kinhtangchi/sujato-vi/an-08-004-the-chapter-on-giving.md",
"../../docs/kinhtangchi/sujato-vi/an-08-005-the-chapter-on-sabbath.md",
"../../docs/kinhtangchi/sujato-vi/an-08-006-the-chapter-on-gotami.md",
"../../docs/kinhtangchi/sujato-vi/an-08-007-the-chapter-on-earthquakes.md",
"../../docs/kinhtangchi/sujato-vi/an-08-008-the-chapter-on-pairs.md",
"../../docs/kinhtangchi/sujato-vi/an-08-009-the-chapter-on-mindfulness.md",
"../../docs/kinhtangchi/sujato-vi/an-08-010-the-chapter-on-similarity.md",
"../../docs/kinhtangchi/sujato-vi/an-09-000-chapter-9.md",
"../../docs/kinhtangchi/sujato-vi/an-09-001-the-chapter-on-awakening.md",
"../../docs/kinhtangchi/sujato-vi/an-09-002-the-chapter-on-the-lion-s-roar.md",
"../../docs/kinhtangchi/sujato-vi/an-09-003-the-chapter-on-abodes-of-sentient-beings.md",
"../../docs/kinhtangchi/sujato-vi/an-09-004-the-great-chapter.md",
"../../docs/kinhtangchi/sujato-vi/an-09-005-the-chapter-on-similarity.md",
"../../docs/kinhtangchi/sujato-vi/an-09-006-the-chapter-on-a-safe-place.md",
"../../docs/kinhtangchi/sujato-vi/an-09-007-the-chapter-on-mindfulness-meditation.md",
"../../docs/kinhtangchi/sujato-vi/an-09-008-the-chapter-on-right-efforts.md",
"../../docs/kinhtangchi/sujato-vi/an-09-009-the-chapter-on-bases-of-psychic-power.md",
"../../docs/kinhtangchi/sujato-vi/an-09-010-the-chapter-on-bases-of-psychic-power2.md",
"../../docs/kinhtangchi/sujato-vi/an-10-000-chapter-10.md",
"../../docs/kinhtangchi/sujato-vi/an-10-001-the-chapter-on-benefits.md",
"../../docs/kinhtangchi/sujato-vi/an-10-002-the-chapter-on-a-protector.md",
"../../docs/kinhtangchi/sujato-vi/an-10-003-the-great-chapter.md",
"../../docs/kinhtangchi/sujato-vi/an-10-004-the-chapter-with-upali.md",
"../../docs/kinhtangchi/sujato-vi/an-10-005-the-chapter-on-abuse.md",
"../../docs/kinhtangchi/sujato-vi/an-10-006-the-chapter-on-your-own-mind.md",
"../../docs/kinhtangchi/sujato-vi/an-10-007-the-chapter-on-pairs.md",
"../../docs/kinhtangchi/sujato-vi/an-10-008-the-chapter-on-if-you-want.md",
"../../docs/kinhtangchi/sujato-vi/an-10-009-the-chapter-on-senior-mendicants.md",
"../../docs/kinhtangchi/sujato-vi/an-10-010-the-chapter-with-upali.md",
"../../docs/kinhtangchi/sujato-vi/an-10-011-the-chapter-on-perceptions-for-ascetics.md",
"../../docs/kinhtangchi/sujato-vi/an-10-012-the-chapter-on-the-ceremony-of-descent.md",
"../../docs/kinhtangchi/sujato-vi/an-10-013-the-chapter-on-purified.md",
"../../docs/kinhtangchi/sujato-vi/an-10-014-the-chapter-on-good.md",
"../../docs/kinhtangchi/sujato-vi/an-10-015-the-chapter-on-the-noble-path.md",
"../../docs/kinhtangchi/sujato-vi/an-10-016-the-chapter-on-persons.md",
"../../docs/kinhtangchi/sujato-vi/an-10-017-the-chapter-with-janussoni.md",
"../../docs/kinhtangchi/sujato-vi/an-10-018-the-chapter-on-good.md",
"../../docs/kinhtangchi/sujato-vi/an-10-019-the-chapter-on-the-noble-path.md",
"../../docs/kinhtangchi/sujato-vi/an-10-020-another-chapter-on-persons.md",
"../../docs/kinhtangchi/sujato-vi/an-10-021-the-chapter-on-the-body-born-of-deeds.md",
"../../docs/kinhtangchi/sujato-vi/an-10-022-the-chapter-on-similarity.md",
"../../docs/kinhtangchi/sujato-vi/an-11-000-chapter-11.md",
"../../docs/kinhtangchi/sujato-vi/an-11-001-the-chapter-on-dependence.md",
"../../docs/kinhtangchi/sujato-vi/an-11-002-the-chapter-on-recollection.md",
"../../docs/kinhtangchi/sujato-vi/an-11-003-the-chapter-on-similarity.md",
]

    files = filex

    output = []

    for file_path in files:
        min_num, max_num = get_range(file_path)

        if min_num is None:
            print(f"Không tìm thấy range: {file_path}")
            continue

        filename = Path(file_path).name

        output.append(
            f'{{"filename": "{filename}", "range": ({min_num}, {max_num})}},'
        )

    output_file = "range.txt"

    Path(output_file).write_text(
        "\n".join(output),
        encoding="utf-8"
    )

    # output_file = "range.txt"

    # Path(output_file).write_text(
    #     json.dumps(result, ensure_ascii=False, indent=2),
    #     encoding="utf-8"
    # )

    print(f"Đã tạo: {output_file}")


if __name__ == "__main__":
    main()
import svgwrite
from svgwrite import cm, mm
from datetime import datetime


def dayOfTheYear(std_date):
    formatted_dt = datetime.strptime(std_date, "%Y-%m-%d")
    doy = formatted_dt.strftime("%j")
    return int(doy)


def date_reformat(std_date):
    ddmm = datetime.strptime(std_date, "%Y-%m-%d").strftime("%d-%b")
    return ddmm


ORIGIN = 3
LENGTH_OF_LINE = ORIGIN + (365 / 20)
COLOR_CODE = {
    "background": "rgb(255, 241, 229)",  #
    "lines": "rgb(173, 216, 230)",
    "bubble_stroke": "rgb(255, 255, 0)",
    "year": "rgb(85, 136, 238)",
}


years = [2023, 2022, 2021, 2020, 2019, 2018, 2017]

posted_date = {
    2023: [
        "2023-01-01",
        "2023-01-08",
        "2023-01-15",
        "2023-01-22",
        "2023-01-29",
        "2023-02-05",
        "2023-02-12",
    ],
    2022: ["2022-05-09", "2022-05-17", "2022-08-22", "2022-10-13"],
    2021: ["2021-04-16", "2021-09-30", "2021-08-20", "2021-07-12", "2021-05-29"],
    2020: [
        "2020-11-10",
        "2020-11-03",
        "2020-09-29",
        "2020-09-22",
        "2020-09-13",
        "2020-09-08",
        "2020-09-06",
        "2020-08-30",
        "2020-08-03",
        "2020-07-11",
        "2020-06-26",
        "2020-06-14",
        "2020-06-07",
        "2020-04-12",
        "2020-04-08",
        "2020-04-06",
        "2020-04-03",
        "2020-04-01",
        "2020-04-04",
        "2020-02-23",
        "2020-01-05",
        "2020-01-10",
    ],
    2019: [
        "2019-12-25",
        "2019-10-13",
        "2019-08-29",
        "2019-08-27",
        "2019-08-25",
        "2019-07-22",
        "2019-07-07",
        "2019-06-23",
        "2019-06-17",
        "2019-05-29",
        "2019-05-04",
        "2019-04-26",
        "2019-04-25",
    ],
    2018: ["2018-02-25", "2018-06-03"],
    2017: ["2017-05-06"],
}

post_url_on = {
    "2023-01-01": "https://dheepakg.github.io/post/2023/01/project-update-1/",
    "2023-01-08": "https://dheepakg.github.io/post/2023/01/are-you-envious-of-younger-generation/",
    "2023-01-15": "https://dheepakg.github.io/post/2023/01/personal-help/maid-affordability-a-social-indicator/",
    "2023-01-22": "https://dheepakg.github.io/post/2023/01/project-update-2/",
    "2023-01-29": "https://dheepakg.github.io/post/2023/01/project-update-3/",
    "2023-02-05": "https://dheepakg.github.io/post/2023/02/osmosis-irl/",
    "2023-02-12": "https://dheepakg.github.io/post/2023/02/api-configurations-database-operation/",
    "2022-05-09": "https://dheepakg.github.io/post/2022/05/cross-compatibility-is-key/",
    "2022-05-17": "https://dheepakg.github.io/post/2022/05/hugo-site-deployment-using-github-actions/",
    "2022-08-22": "https://dheepakg.github.io/post/2022/08/what-if-google-suspends-your-account/",
    "2022-10-13": "https://dheepakg.github.io/post/2022/10/migrated-to-blogdown/",
    "2021-04-16": "https://dheepakg.github.io/post/2021/04/aws-certified-solution-architect-for-whom-why-and-how/",
    "2021-09-30": "https://dheepakg.github.io/post/2021/11/yet-another-tech-ceo-of-indian-origin/",
    "2021-08-20": "https://dheepakg.github.io/post/2021/08/a-backend-devs-journey-into-js-world-part-i/",
    "2021-07-12": "https://dheepakg.github.io/post/2021/07/power-of-open-data/",
    "2021-05-29": "https://dheepakg.github.io/post/2021/05/longreads-with-kindle/",
    "2020-11-10": "https://dheepakg.github.io/post/2020/11/weekly-update-7-nov-10-2020/",
    "2020-11-03": "https://dheepakg.github.io/post/2020/11/weekly-update-6-nov-3-2020/",
    "2020-09-29": "https://dheepakg.github.io/post/2020/09/weekly-update-5-sep-29-2020/",
    "2020-09-22": "https://dheepakg.github.io/post/2020/09/weekly-update-4-sep-22-2020/",
    "2020-09-13": "https://dheepakg.github.io/post/2020/09/weekly-update-3-sep-13-2020/",
    "2020-09-08": "https://dheepakg.github.io/post/2020/09/unexpected-outcome/",
    "2020-09-06": "https://dheepakg.github.io/post/2020/09/weekly-update-sep-6-2020/",
    "2020-08-30": "https://dheepakg.github.io/post/2020/08/weekly-update-aug-30-2020/",
    "2020-08-03": "https://dheepakg.github.io/post/2020/08/if-youre-approaching-20s-or-in-early-20s/",
    "2020-07-11": "https://dheepakg.github.io/post/2020/07/one-neednt-be-proud/",
    "2020-06-26": "https://dheepakg.github.io/post/2020/06/the-return-of-newsletters/",
    "2020-06-14": "https://dheepakg.github.io/post/2020/06/essentially-theyre-non-essentials/",
    "2020-06-07": "https://dheepakg.github.io/post/2020/06/a-curious-question-on-reading/",
    "2020-04-12": "https://dheepakg.github.io/post/2020/04/a-lost-relationship/",
    "2020-04-08": "https://dheepakg.github.io/post/2020/04/covid-19-political-change-on-the-cards/",
    "2020-04-06": "https://dheepakg.github.io/post/2020/04/couple-of-things-that-went-unnoticed/",
    "2020-04-03": "https://dheepakg.github.io/post/2020/04/shouldnt-there-be-some-regulation-road-side-shops/",
    "2020-04-01": "https://dheepakg.github.io/post/2020/04/striving-with-contextual-speakers/",
    "2020-04-04": "https://dheepakg.github.io/post/2020/04/working-with-raspberry-pi-files/",
    "2020-02-23": "https://dheepakg.github.io/post/2020/02/comparison-of-various-hdfs-file-formats/",
    "2020-01-05": "https://dheepakg.github.io/post/2020/01/the-2010s-part-1/",
    "2020-01-10": "https://dheepakg.github.io/post/2020/01/the-2010s-part-2/",
    "2019-12-25": "https://dheepakg.github.io/post/2019/12/the-guinea-pig-generation/",
    "2019-10-13": "https://dheepakg.github.io/post/2019/10/pyconindia-2019/",
    "2019-08-29": "https://dheepakg.github.io/post/2019/08/oxidation-2-variables-shadowing/",
    "2019-08-27": "https://dheepakg.github.io/post/2019/08/oxidation-1-cargo-rustdoc/",
    "2019-08-25": "https://dheepakg.github.io/post/2019/08/what-makes-rust-interesting/",
    "2019-07-22": "https://dheepakg.github.io/post/2019/07/yes-humanity-exists/",
    "2019-07-07": "https://dheepakg.github.io/post/2019/07/podcast-listening-101/",
    "2019-06-23": "https://dheepakg.github.io/post/2019/06/fight-against-climate-change-is-not-getting-traction-why/",
    "2019-06-17": "https://dheepakg.github.io/post/2019/06/no-more-ad-breaks-thanks-pi-hole/",
    "2019-05-29": "https://dheepakg.github.io/post/2019/05/first-serious-project-that-has-some-rational-application/",
    "2019-05-04": "https://dheepakg.github.io/post/2019/05/starting-with-jekyll/",
    "2019-04-26": "https://dheepakg.github.io/post/2019/04/evms-should-be-avoided-for-indian-elections-why/",
    "2019-04-25": "https://dheepakg.github.io/post/2019/04/welcome-to-the-site/",
    "2018-02-25": "https://dheepakg.github.io/post/2018/02/what-is-farming-biz-or-charity/",
    "2018-06-03": "https://dheepakg.github.io/post/2018/06/final-frontier-for-ai-could-be-decoding-sarcasm/",
    "2017-05-06": "https://dheepakg.github.io/post/2017/05/democracy-a-silver-bullet/",
}


post_url__title_on = {
    "2023-01-01": {
        "title": "Project Update - 1",
        "url": "https://dheepakg.github.io/post/2023/01/project-update-1/",
    },
    "2023-01-08": {
        "title": "Are you envious of younger generation?",
        "url": "https://dheepakg.github.io/post/2023/01/are-you-envious-of-younger-generation/",
    },
    "2023-01-15": {
        "title": "Personal help/maid affordability - a social indicator?",
        "url": "https://dheepakg.github.io/post/2023/01/personal-help/maid-affordability-a-social-indicator/",
    },
    "2023-01-22": {
        "title": "Project Update - 2",
        "url": "https://dheepakg.github.io/post/2023/01/project-update-2/",
    },
    "2023-01-29": {
        "title": "Project Update - 3",
        "url": "https://dheepakg.github.io/post/2023/01/project-update-3/",
    },
    "2023-02-05": {
        "title": "Osmosis IRL",
        "url": "https://dheepakg.github.io/post/2023/02/osmosis-irl/",
    },
    "2023-02-12": {
        "title": "API, Configurations & Database operation",
        "url": "https://dheepakg.github.io/post/2023/02/api-configurations-database-operation/",
    },
    "2022-05-09": {
        "title": "Cross compatibility is key",
        "url": "https://dheepakg.github.io/post/2022/05/cross-compatibility-is-key/",
    },
    "2022-05-17": {
        "title": "Hugo Site Deployment Using Github Actions",
        "url": "https://dheepakg.github.io/post/2022/05/hugo-site-deployment-using-github-actions/",
    },
    "2022-08-22": {
        "title": "What if: Google suspends your account?",
        "url": "https://dheepakg.github.io/post/2022/08/what-if-google-suspends-your-account/",
    },
    "2022-10-13": {
        "title": "Migrated to blogdown",
        "url": "https://dheepakg.github.io/post/2022/10/migrated-to-blogdown/",
    },
    "2021-11-30": {
        "title": "Yet another tech CEO of Indian origin",
        "url": "https://dheepakg.github.io/post/2021/11/yet-another-tech-ceo-of-indian-origin/",
    },
    "2021-08-20": {
        "title": "A backend dev's journey into JS world - Part I",
        "url": "https://dheepakg.github.io/post/2021/08/a-backend-devs-journey-into-js-world-part-i/",
    },
    "2021-07-12": {
        "title": "Power of Open Data",
        "url": "https://dheepakg.github.io/post/2021/07/power-of-open-data/",
    },
    "2021-05-29": {
        "title": "Longreads with Kindle",
        "url": "https://dheepakg.github.io/post/2021/05/longreads-with-kindle/",
    },
    "2021-04-16": {
        "title": "AWS Certified Solution Architect - for whom, why and how",
        "url": "https://dheepakg.github.io/post/2021/04/aws-certified-solution-architect-for-whom-why-and-how/",
    },
    "2020-11-10": {
        "title": "Weekly Update 7 - Nov 10, 2020",
        "url": "https://dheepakg.github.io/post/2020/11/weekly-update-7-nov-10-2020/",
    },
    "2020-11-03": {
        "title": "Weekly Update 6 - Nov 3, 2020",
        "url": "https://dheepakg.github.io/post/2020/11/weekly-update-6-nov-3-2020/",
    },
    "2020-09-29": {
        "title": "Weekly Update 5 - Sep 29, 2020",
        "url": "https://dheepakg.github.io/post/2020/09/weekly-update-5-sep-29-2020/",
    },
    "2020-09-22": {
        "title": "Weekly Update 4 - Sep 22, 2020",
        "url": "https://dheepakg.github.io/post/2020/09/weekly-update-4-sep-22-2020/",
    },
    "2020-09-13": {
        "title": "Weekly Update 3 - Sep 13, 2020",
        "url": "https://dheepakg.github.io/post/2020/09/weekly-update-3-sep-13-2020/",
    },
    "2020-09-08": {
        "title": "Unexpected outcome",
        "url": "https://dheepakg.github.io/post/2020/09/unexpected-outcome/",
    },
    "2020-09-06": {
        "title": "Weekly Update - Sep 6, 2020",
        "url": "https://dheepakg.github.io/post/2020/09/weekly-update-sep-6-2020/",
    },
    "2020-08-30": {
        "title": "Weekly Update - Aug 30, 2020",
        "url": "https://dheepakg.github.io/post/2020/08/weekly-update-aug-30-2020/",
    },
    "2020-08-03": {
        "title": "If you're approaching 20's or in early 20's",
        "url": "https://dheepakg.github.io/post/2020/08/if-youre-approaching-20s-or-in-early-20s/",
    },
    "2020-07-11": {
        "title": "One needn't be proud",
        "url": "https://dheepakg.github.io/post/2020/07/one-neednt-be-proud/",
    },
    "2020-06-26": {
        "title": "The return of Newsletters",
        "url": "https://dheepakg.github.io/post/2020/06/the-return-of-newsletters/",
    },
    "2020-06-14": {
        "title": "Essentially, they're non-essentials",
        "url": "https://dheepakg.github.io/post/2020/06/essentially-theyre-non-essentials/",
    },
    "2020-06-07": {
        "title": "A curious question on reading?",
        "url": "https://dheepakg.github.io/post/2020/06/a-curious-question-on-reading/",
    },
    "2020-04-12": {
        "title": "A lost relationship",
        "url": "https://dheepakg.github.io/post/2020/04/a-lost-relationship/",
    },
    "2020-04-08": {
        "title": "COVID-19: Political change on the cards?",
        "url": "https://dheepakg.github.io/post/2020/04/covid-19-political-change-on-the-cards/",
    },
    "2020-04-06": {
        "title": "Couple of things that went unnoticed",
        "url": "https://dheepakg.github.io/post/2020/04/couple-of-things-that-went-unnoticed/",
    },
    "2020-04-03": {
        "title": "Shouldn’t there be some regulation – road side shops",
        "url": "https://dheepakg.github.io/post/2020/04/shouldnt-there-be-some-regulation-road-side-shops/",
    },
    "2020-04-01": {
        "title": "Striving with Contextual speakers",
        "url": "https://dheepakg.github.io/post/2020/04/striving-with-contextual-speakers/",
    },
    "2020-04-04": {
        "title": "Working with Raspberry Pi files",
        "url": "https://dheepakg.github.io/post/2020/04/working-with-raspberry-pi-files/",
    },
    "2020-02-23": {
        "title": "Comparison of various HDFS file formats",
        "url": "https://dheepakg.github.io/post/2020/02/comparison-of-various-hdfs-file-formats/",
    },
    "2020-01-05": {
        "title": "https://dheepakg.github.io/post/2020/01/the-2010s-part-2/",
        "url": "https://dheepakg.github.io/post/2020/01/the-2010s-part-1/",
    },
    "2020-01-10": {
        "title": "The 2010s - Part 1",
        "url": "https://dheepakg.github.io/post/2020/01/the-2010s-part-2/",
    },
    "2019-12-25": {
        "title": "The Guinea Pig Generation",
        "url": "https://dheepakg.github.io/post/2019/12/the-guinea-pig-generation/",
    },
    "2019-10-13": {
        "title": "PyConIndia 2019",
        "url": "https://dheepakg.github.io/post/2019/10/pyconindia-2019/",
    },
    "2019-08-29": {
        "title": "Oxidation 2 - Variables, Shadowing",
        "url": "https://dheepakg.github.io/post/2019/08/oxidation-2-variables-shadowing/",
    },
    "2019-08-27": {
        "title": "Oxidation 1 - Cargo, Rustdoc",
        "url": "https://dheepakg.github.io/post/2019/08/oxidation-1-cargo-rustdoc/",
    },
    "2019-08-25": {
        "title": "What makes Rust interesting?",
        "url": "https://dheepakg.github.io/post/2019/08/what-makes-rust-interesting/",
    },
    "2019-07-22": {
        "title": "Yes, humanity exists",
        "url": "https://dheepakg.github.io/post/2019/07/yes-humanity-exists/",
    },
    "2019-07-07": {
        "title": "Podcast listening 101",
        "url": "https://dheepakg.github.io/post/2019/07/podcast-listening-101/",
    },
    "2019-06-23": {
        "title": "Fight against Climate Change is not getting traction - Why?",
        "url": "https://dheepakg.github.io/post/2019/06/fight-against-climate-change-is-not-getting-traction-why/",
    },
    "2019-06-17": {
        "title": "No more Ad breaks - thanks Pi-hole",
        "url": "https://dheepakg.github.io/post/2019/06/no-more-ad-breaks-thanks-pi-hole/",
    },
    "2019-05-29": {
        "title": "First serious project that has some rational application",
        "url": "https://dheepakg.github.io/post/2019/05/first-serious-project-that-has-some-rational-application/",
    },
    "2019-05-04": {
        "title": "Starting with Jekyll",
        "url": "https://dheepakg.github.io/post/2019/05/starting-with-jekyll/",
    },
    "2019-04-26": {
        "title": "EVMs should be avoided for Indian elections - Why?",
        "url": "https://dheepakg.github.io/post/2019/04/evms-should-be-avoided-for-indian-elections-why/",
    },
    "2019-04-25": {
        "title": "Welcome to the site!",
        "url": "https://dheepakg.github.io/post/2019/04/welcome-to-the-site/",
    },
    "2018-02-25": {
        "title": "What is farming — Biz or Charity?",
        "url": "https://dheepakg.github.io/post/2018/02/what-is-farming-biz-or-charity/",
    },
    "2018-06-03": {
        "title": "Final frontier for AI could be decoding Sarcasm",
        "url": "https://dheepakg.github.io/post/2018/06/final-frontier-for-ai-could-be-decoding-sarcasm/",
    },
    "2017-05-06": {
        "title": "Democracy, a silver bullet?",
        "url": "https://dheepakg.github.io/post/2017/05/democracy-a-silver-bullet/",
    },
}


def build_svg(name):
    dwg = svgwrite.Drawing(filename=name, size=(1000, 400))

    dwg.add(
        dwg.rect(
            insert=(0, 0),
            size=("100%", "100%"),
            rx=None,
            ry=None,
            fill=COLOR_CODE["background"],
            stroke="black",
            stroke_width=3,
        )
    )

    paragraph = dwg.add(
        dwg.g(style="font-size:20px; font-weight:Bold; fill:COLOR_CODE['year']")
    )

    hlines = dwg.add(dwg.g(id="hlines", stroke=COLOR_CODE["lines"], stroke_width=10))

    for y in range(len(years)):
        paragraph.add(dwg.text(years[y], (1 * cm, (2.1 + y) * cm)))
        hlines.add(
            dwg.line(
                start=(ORIGIN * cm, (2 + y) * cm),
                end=((int(ORIGIN) + LENGTH_OF_LINE) * cm, (2 + y) * cm),
            )
        )

        print("year is ", years[y])
        tool_tip = dwg.add(
            dwg.g(style="font-size:20px; font-weight:Bold; fill:COLOR_CODE['year']")
        )

        if years[y] in posted_date.keys():
            print("posts available", years[y], posted_date[years[y]])
            for d in posted_date[years[y]]:
                print(d, " is ", dayOfTheYear(d))
                print(
                    "position is ",
                    (dayOfTheYear(d) * (0.058)),
                    "circle posit is ",
                    (ORIGIN + (dayOfTheYear(d) * (0.058))) * cm,
                )
                if d in post_url__title_on.keys():
                    print("URL present")
                    link = dwg.add(dwg.a(post_url__title_on[d]["url"], target="_blank"))
                    link.set_desc(
                        date_reformat(d) + ": " + post_url__title_on[d]["title"]
                    )
                else:
                    print("URL not present")
                    link = dwg.add(dwg.a("http://www.w3.org", target="_blank"))
                circle = dwg.circle(
                    center=((ORIGIN + (dayOfTheYear(d) * 0.058)) * cm, (2 + y) * cm),
                    r="4",
                    stroke=COLOR_CODE["bubble_stroke"],
                    stroke_width=1,
                )
                # tool_tip.add(dwg.text("Something", (1.5 * cm, (2.5 + y) * cm)))
                # tool_tip.add(circle)
                # link.set_desc("yy")
                link.add(circle)

    dwg.save()


build_svg("post-over-the-years.svg")

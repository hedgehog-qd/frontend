from quart import render_template


def lbfe(result,mode,sort):
    if (len(result) < 24):
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
        result.append({'name': 'No Player', 'country': '-', 'tscore': '-', 'pp': '-', 'plays': '-', 'acc': '-'})
    modeout = ""
    if (mode == "0"):
        modeout = "osu! mode"
    if (mode == "1"):
        modeout = "osu!taiko mode"
    if (mode == "2"):
        modeout = "osu!catch mode"
    if (mode == "3"):
        modeout = "osu!mania mode"
    if (mode != "0" and mode != "1" and mode != "2" and mode != "3"):
        modeout = "WTF mode it is !!??"
    return render_template('leaderboard.html', p1=modeout, p2=result, p3="Order by: " + sort)
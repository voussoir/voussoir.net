const eternalseptember = {};

eternalseptember.EPOCH = new Date("1993-09-01T00:00:00");

eternalseptember.AM_PM = ["AM", "PM"];
eternalseptember.WEEKDAY_NAMES = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
]
eternalseptember.WEEKDAY_ABBREVS = [
    "Sun",
    "Mon",
    "Tue",
    "Wed",
    "Thu",
    "Fri",
    "Sat",
]
eternalseptember.MONTH_NAMES = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

eternalseptember.twelvehour =
function twelvehour(hour)
{
    hour = parseInt(hour % 12);
    if (hour === 0)
    {
        return 12;
    }
    return hour;
}

eternalseptember.strftime =
function strftime(date, format)
{
    const diff = date - eternalseptember.EPOCH;
    const diff_days = parseInt(diff / (1000*60*60*24));

    const day_of_month = diff_days + 1
    const day_of_year = diff_days + 244

    let result = format;
    result = result.replace(/(?<!%)%b/, 'Sep');
    result = result.replace(/(?<!%)%B/, 'September');
    result = result.replace(/(?<!%)%d/, day_of_month);
    result = result.replace(/(?<!%)%-d/, day_of_month);
    result = result.replace(/(?<!%)%j/, day_of_year);
    result = result.replace(/(?<!%)%-j/, day_of_year);
    result = result.replace(/(?<!%)%m/, '09');
    result = result.replace(/(?<!%)%-m/, '9');
    result = result.replace(/(?<!%)%Y/, '1993');
    result = result.replace(/(?<!%)%y/, '93');

    result = result.replace(/(?<!%)%A/, eternalseptember.WEEKDAY_NAMES[date.getDay()]);
    result = result.replace(/(?<!%)%a/, eternalseptember.WEEKDAY_ABBREVS[date.getDay()]);

    result = result.replace(/(?<!%)%w/, date.getDay());
    result = result.replace(/(?<!%)%H/, String(date.getHours()).padStart(2, "0"));
    result = result.replace(/(?<!%)%-H/, date.getHours());
    result = result.replace(/(?<!%)%I/, String(eternalseptember.twelvehour(date.getHours())).padStart(2, "0"));
    result = result.replace(/(?<!%)%-I/, eternalseptember.twelvehour(date.getHours()));
    result = result.replace(/(?<!%)%M/, String(date.getMinutes()).padStart(2, "0"));
    result = result.replace(/(?<!%)%-M/, date.getMinutes());
    result = result.replace(/(?<!%)%S/, String(date.getSeconds()).padStart(2, "0"));
    result = result.replace(/(?<!%)%-S/, date.getSeconds());

    result = result.replace(/(?<!%)%p/, eternalseptember.AM_PM[+(date.getHours() > 12)]);
    return result;
}

eternalseptember.init_clock =
function init_clock(clock)
{
    const format = clock.dataset.eternalseptemberStrftime;
    if (clock.dataset.eternalseptemberTickrate === undefined)
    {
        clock.innerText = eternalseptember.strftime(new Date(), format);
        return;
    }

    const tickrate = parseInt(clock.dataset.eternalseptemberTickrate);
    const ticktock = function ticktock()
    {
        clock.innerText = eternalseptember.strftime(new Date(), format);
        setTimeout(ticktock, tickrate);
    }
    ticktock();
}

eternalseptember.init_clocks =
function init_clocks()
{
    const clocks = Array.from(document.getElementsByClassName("eternalseptember_clock"));
    for (const clock of clocks)
    { 
        eternalseptember.init_clock(clock);
    }
}

eternalseptember.on_pageload =
function on_pageload()
{
    eternalseptember.init_clocks();
}
document.addEventListener("DOMContentLoaded", eternalseptember.on_pageload);

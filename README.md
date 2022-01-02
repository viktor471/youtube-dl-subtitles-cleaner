# youtube-dl-subtitles-cleaner
Clean autogenerated subtitles downloaded with the help youtube-dl

This is just my attempt to delete extra service data from autogenerate subtitles. I wrote this just for my own use. But I will be glad if someone finds this code useful. I will be glad to see any criticism and suggestions.

## Why it is needed

When we download autogenerated subtitles with the help youtube-dl with flag --write-auto-sub we get file with content like:
```
00:00:01.840 --> 00:00:04.210 align:start position:0%
 
welcome<00:00:02.840><c> to</c><00:00:02.929><c> this</c><00:00:03.020><c> video</c><00:00:03.199><c> what's</c><00:00:04.069><c> the</c>

00:00:04.210 --> 00:00:04.220 align:start position:0%
welcome to this video what's the
 

00:00:04.220 --> 00:00:06.280 align:start position:0%
welcome to this video what's the
difference<00:00:04.609><c> between</c><00:00:04.819><c> static</c><00:00:05.420><c> websites</c><00:00:06.050><c> and</c>

00:00:06.280 --> 00:00:06.290 align:start position:0%
difference between static websites and
```

I don't know why file has data like `<00:00:04.609>` or `<c>` and `</c>` tag like parts, alignment label. I couldn't find hot to simply get rid of this unnecessary and unuseful data, so I also added a function to remove this data to my code (`delete_service_data.py`). Besides, you can see that text contains duplicate lines. Although in the upper text this is not so obvious due to the service data like extra timecodes and some other things, but there are duplicates. Therefore, I added script "`delete_duplicate_string.py`" that cleans duplicates. main.py does the both actions.

## How to use it

In current moment you need just pass file with subtitles as first argument and optionally name of output file as second argument. 

```
$ ./main.py input_file output_file
```

A little later I make more user-friendly interface, and some other fixes.  

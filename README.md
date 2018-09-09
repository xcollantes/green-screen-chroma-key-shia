# Green Screen Processor for Shia LaBeouf
## What It Does
Take this image of Shia LaBeouf with a green screen behind him from the famous meme where Shia stands in front of a green screen giving a strangely effective motovational speech.    
If you haven't seen it, [check it out](shia).  You'll be glad you did.  
<img alt='Shia LaBeouf' width='50%' height='50%' align='center' src='lib/09-Sep-18_00-52-96.png'>



Superimpose Shia on the below image of me and friends.  
<img alt='For Good' width='50%' height='50%' align='center' src='lib/transpose_horizontal.png'>




## How It Works


## Next Steps
Notice the green outline of our hero, Shia LaBeouf, in the final image.  
Fine tuning the chroma key algorithm to detect a greater range of greens could result in a cleaner image.  

## Libraries Used
`os` for writing our RGB values to find threshold in foreground image.  
`pillow` or _Python Image Library_ to manipulate images on a pixel level.  


[shia]:https://www.youtube.com/watch?v=ZXsQAXx_ao0
[rgb]:https://www.w3schools.com/colors/colors_rgb.asp
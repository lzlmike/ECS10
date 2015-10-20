def main():
   HTML_string=str(input("Please enter a HTML string: "))
   #Str_length=len(HTML_string)
   #Transfer_Set={"&ldquo;":"``","&rdquo;":"\"","&apos;":"'","&amp;":"&","&lt;":"<",
    #         "&gt;":">","{":"\{","}":"\}","%":"\%"}
   HTML_string=HTML_string.replace("&ldquo;","``")
   HTML_string=HTML_string.replace("&rdquo;","\"")
   HTML_string=HTML_string.replace("&apos;","'")
   HTML_string=HTML_string.replace("&amp;","&")
   HTML_string=HTML_string.replace("&lt;","<")
   HTML_string=HTML_string.replace("&gt;",">")
   HTML_string=HTML_string.replace("{","\{")
   HTML_string=HTML_string.replace("}","\}")
   HTML_string=HTML_string.replace("%","\%")

   print(HTML_string)
main()

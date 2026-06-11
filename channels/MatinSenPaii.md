<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn1.telesco.pe/file/rTQJib_KDlOvLsXn-hgKDqFzTmmXTH7g7kNUMsAwV3Z4wTXBE1vs9bSC6-NQViZgxLyZB3UmZedKnmc4nMSKJBdh6sqxe7PUwOp-EbIndT4Y_KWSkRzmLP_R2xjbS4RnGllgZcmkoxnAa4nG0ZWyv8Di97vAdxgXK6zdYzrja1jIkwhJvu9KTuRAmnf-rtua8MDLWMuKqdM5A_57IBAA-covIKvhkA5cNGm6gmIXZ55NR8d0JvBdAovAR6RQ_-DUtTJEg0Ndn6N_tX5M65K_2UAwKxLm83p8l2f4dpcGdZGSCnNnHctXXrm5pqYnZ481-B5LkbncWox4DllPyKsZig.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 163K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 06:16:46</div>
<hr>

<div class="tg-post" id="msg-3784">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">امیدوارم
WhiteDNS
ستاپ کرده باشید. برای اتصال توی شرایط جنگ
دیگه حوصله‌ی اصرار نیست</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/MatinSenPaii/3784" target="_blank">📅 01:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3782">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اگر خواستید مفهوم فیلترینگ منطقه‌ای رو بفهمید، سوار اتوبوس بشید و از تهران برید خوزستان. به هر شهری می‌رسید آیپی تمیزهاتون از کار میفتن و باید دوباره اسکن کنید. به استان خوزستان که می‌رسید، گوشی تبدیل به یه پاره آجر بی‌مصرف میشه و فقط می‌تونید باهاش زنگ بزنید
😂</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/3782" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3781">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jMas--XUaKifIP-MGmxYteGG5lGJ_LTNbOJRAimYfZxpr6T9sHiizEjhhoc3epoh0ONYvgv5EQIwhw6mk6-viDouRGE2WKBHf0tENNR5afeuF5t6g6qlkCRW2C6xLxGvgRNkjHUitnKnVstI5BHE9zqbt8bQpFLv6tQB5B88-mMKP2L7cijZzlBl0loIKf5YVtOHDUdqpjNw6_2N5BZo62KT0tdaE86a4TOsmTHxfzrcS0zTj36p-Lrk3uKL7QXxGKSS3xDT94IBzyAjWho611Ivyb0A-yursshn30ZTg0OhzkRprYzYCSTe7pVZ79mwP9QMLEQVrns_CuHdcmmjgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏وقتشه یه سری حقایق راجب بورسیه MEXT ژاپن بگم.
حالم از این پوسترا مخصوصا راجب بورسیه‌ی ژاپن به هم می‌خوره.
واقعیت:
۱- از چندین هزار متقاضی، سالانه زیر ۵۰ نفر(متغیر) مجموعا از تمام مقاطع برگزیده میشن که اونم کاملا شانسیه.
۲- انتخاب شدن شما تماما به نیاز ژاپن بستگی داره و اصلا هم اعلام نمی‌کنن که ما به فلان رشته نیاز داریم. ممکنه شما تمام شرایط عالی رو داشته باشی با بالاترین نمره، اما «امسال ژاپن به رشته شما نیاز نداشته باشه»(مقطع ارشد و دکتری) و این رو به صورت مبهم فقط بهتون میگن که شما رد شدید! یعنی هیچ دلیلی برای رد شدنتون بهتون نمیدن توی هیچ مقطعی. شخص A با دانش نزدیک به صفر بدون بلد بودن انگلیسی یا ژاپنی قبول میشه چون ژاپن این رشته رو نیاز داره، شخص B بدون توضیح رد میشه با اینکه دانش و علم خیلی بالایی داره یا حتی مدرک زبان ژاپنی داره، چون به رشته‌اش نیاز ندارن. و فقط میگن رد شدی بدون توضیح.
۳- روند غربالگری به شدت غیراستاندارد، و رد شدن توی هر مرحله بدون توضیح هست(سه مرحله داره شامل ارسال مدارک و آزمون کتبی و مصاحبه که هرجا رد شدید، علتی نمیگن)
۴- ثبت نام برخلاف به روز بودن خود کشور ژاپن، به صورت کاملا سنتی و با پست کردن مدرک کاغذی برای سفارت توی یه فرآیند بسیار زمان‌بر و استرس‌زا(نکنه فلان چیز رو یادم رفته باشه) و هزارتا دنگ و فنگ انجام میشه. همه چیز کاغذی. همه‌چیز. یعنی حتی زحمت نمی‌دن به خودشون کد ملی شما رو وارد کنن اطلاعاتتون رو بگیرن. و توی همه‌ی ۱۵-۲۰ تا مدرکی هم که می‌خوان، یه نقطه اگر اشتباه باشه رد می‌شید توی مرحله‌ی اول. که باز هم توضیحی نمی‌دن بهتون که چرا رد شدید. صرفا میگن نقص مدارک
۵- شما ممکنه تمام تلاشتون رو بکنید، همه‌ی مراحل رو قبول بشید، اما در نهایت ژاپن توی اون سال Mext رو برای ایران کنسل کنه!! بله درست شنیدید. پارسال به خاطر جنگ ۱۲ روزه، ژاپن بورسیه‌اش رو برای ایران لغو کرد(
🤣
🤣
🤣
) صرفا چون تایم آزمونش جنگ شد. به تعویق هم ننداخت. لغو کرد. امسال هم همین شد دقیقا و به دلیل وضعیت کشور، لغو کرد. و تمام کسایی که پارسال و امسال هدفشون رو گذاشته بودن Mext، گند خورد به زندگیشون.
خلاصه‌ی کلام اینکه برای بورسیه تمرکزتون رو روی ژاپن به تنهایی نذارید و چندین تا کشور زیر نظرتون باشه</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/3781" target="_blank">📅 00:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3780">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lr7zahDIfEmsrakwWXUtt8JWpae0LzYg0FVJWqdSy1Q9zk9nM7lER9rENEFjcUwgMmln5-GsWZGTDj8E_HtNQ70iwYgds1N-KeoIbR7w8cPG0rcWwuEu-JPDS4pEytCyM9gVe0kbNTSq4TwucFPTZkkM69ikKztMdp24VJCK7lOvsMj7CXzCksS5v8lPDg9vriESx2e63D4snAr5V4KZwBk-AwaizNXdin1d9NgpSxj-1aT7zK5yPw2VVW4lRpZIujYvLtBbW9KzhCIZZvpE-gkhnU9FGtVRYRGJgFNPfTrsUrmRHRDaIr_cks17nvUjhHsG2qu5aO7wvEa98AQghg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
پروژه‌ی FreeLLMAPI — یه پروکسی OpenAI-compatible فوق‌العاده‌ست که ۱۶ تا از بهترین ارائه‌دهنده‌های LLM(مدل‌های زبانی بزرگ. همون هوش مصنوعی خودمون) رایگان رو روی هم جمع کرده!
تقریباً ۱٫۷ میلیارد توکن توی هر ماه ظرفیت inference (از Google Gemini، Groq، Mistral، Cerebras، OpenRouter، GitHub Models، Cloudflare، NVIDIA، HuggingFace و ... + هر endpoint سفارشی مثل Ollama، vLLM، LM Studio و غیره) می‌ده.
ویژگی‌های اصلی:
🔤
یه endpoint واحد (/v1/chat/completions) برای همه‌چی
🔤
روتینگ هوشمند + failover خودکار (اگر یه کلید به rate limit خورد، سریع میره سراغ بعدی)
🔤
مدیریت دقیق quota هر api key تا زیر حد استفاده‌ی رایگان بمونیم
🔤
کلیدها به صورت رمزنگاری‌شده ذخیره میشن
🔤
داشبورد باحال برای مدیریت api key
🔤
نصب خیلی راحت با Docker
در واقع همه free tierهای پراکنده رو تبدیل کرده به یه LLM قدرتمند و همیشه در دسترس، بدون اینکه مجبور بشی با کلی SDK و rate limit جداگانه کلنجار بری.
بهترین‌ها برای کدنویسی (بر اساس این پروژه و لیست هوش مصنوعی‌ها) عمدتاً DeepSeek V4 Pro، Qwen3-Coder سری (مخصوصاً Qwen3-Coder Next و 480B) و Codestral/Devstral هستن.
⚡️
لینک پروژه:
https://github.com/tashfeenahmed/freellmapi
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/3780" target="_blank">📅 23:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3779">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">من خودم با Hiddify راحتترم برای ساب، از اون استفاده میکنم کلا(با نت H+ الان دارم این پست رو می‌ذارم با همین ساب) اگر پینگ نداد، توی تنظیمات Tls Fragment رو روشن کنید</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/3779" target="_blank">📅 22:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3777">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QXlbZMN74g_9orVLj9iry8Xm6ZqBj3JMevm_qePsvrEWYcBT-C6oCNH0nQnVnwRSodIXR5nNGyckNqWGGSN3j3xu4OTEj7nQvxSDTXqJMCCD1gg4gTV8WrvqbfbHfu_RRFS8SYwuZg6esyA4s4ZteJQcaZOmLzeqxHLGu9oLInE3nJ049aFKAf7HL25af8pgiHcHpiWSRhQkaJE1P0O9wmasgnMgyavTlA-KfWHDpRxJCw9YDRfJVezfsAbDYs6ynFkvrszyG5lxJzBUJ6rB0W0g0joVyCBQnVimoKiRdpI9LKuJgJsRBx8oR_R8ycQ9yqvxX24Ute-cyvhha3q3lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KqaCPDott3FSHga8Z9GMBkYx2CehgU2Clen_S2AYQPZu1EDJoOwTkhRdF0pEL463dD4rd15UxiR2Z6HaB3a_RvXER-4E3CjuL07Tk4O1e53Mc22oGRMPWjiDtkp61xuno0r5eDNLULqaPH1MCX5qIEvSlUqBDEmAndBiG9P5sDGfn5bdK-d_3bs4rEfHLQ5MZ7sGq57cYZiheZMR6BCj_8iaLCmCDlj9JGG5ch_JAwQqacVW6q2DB6MGl-WNaIYBGi362CPeXISMu2q0Uqu9bJe3Zi5EVJQzaB0cJsKIES8jiIU3GbCNC6bMdt80ZLpVrWy_avRYxkxlvlFsvlfy-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بچه‌های WhiteDNS دارن رو یه چیزی کار می‌کنن که شاهکاره ایده‌اش
(عاشق UI اولیه‌ی اپلیکیشنم
😂
)</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/3777" target="_blank">📅 21:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3776">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cao7PBJHNvSTn0rvIO-QtpPFWSkZM6_8O9Kv3EFE8Xjiqlw04N5KrhJ1rSR_xeIDdEkbK1E_KnCrDpdgRIQz7AnqwnwPj-nPzkCJFWIyxFig63-ntKd3f0rEiNbeUbXZk6cmj8eDVuWQFYFRoFgVHd7TpNaM-MRS5NDPvN9RlXd81P1pKIwqSknVjaeF9xPc7T4IpB1vfT4i8SXp-ynczWRQKJt3-zswppCyl1F1VvpZ6DOp-KQAwKQS1s2FNi3ZCivx0IGT-JcfJLhtAuj5EwL1LCOGzLa80mobxf2_h6p_5a6rN1mhc3FmUshLsg5RbuPFkc4gZJ82otT92ptfCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتروپیک هنوز جوهر Opus 4.8 خشک نشده بود، مدل جدید Fable 5 رو به عنوان قوی‌ترین مدل عمومی Claude معرفی کرد!  این مدل توی برنامه‌نویسی، تحقیق و همینطور تحلیل تصویر عالی‌ترینه؛ هرچقدر کارمون پیچیده‌تر بشه، برتریش نسبت به مدل‌های دیگه بیشتر و بیشتر مشخص می‌شه.…</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/3776" target="_blank">📅 19:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3775">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79adfc024d.mp4?token=TSnwT7VyRFe8RLO4t6Ci8Fac-Ai4QUaoM4p_TYvsdafpXDaYLqT4SH7yy1fDdBSP_cH4n4UWm6Q6Jtgwt9Gc9ZemlvGZYOnbwd5JB1QQfR8dKPPCB83OKQwwsFGmZwAq65_7oSLhen2mY_Ggz_Hb_h_43yTQ40eEjV0-hDggzXGiUef_XDfFPtR0Tl6vnMf5hjrohzLDbDRwmnadkp9vISTECR7rg-aII7htF2pmF5ktYQ5rvj6QPajMWcJB1Dt9s8OjyIXwbkNiWbWB-p3_kHti_70jtU7KOxAv4ooNCnTPERyDFViIWCEwaLOuym2SPCkoOcqOzr1VMVKG19uR-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79adfc024d.mp4?token=TSnwT7VyRFe8RLO4t6Ci8Fac-Ai4QUaoM4p_TYvsdafpXDaYLqT4SH7yy1fDdBSP_cH4n4UWm6Q6Jtgwt9Gc9ZemlvGZYOnbwd5JB1QQfR8dKPPCB83OKQwwsFGmZwAq65_7oSLhen2mY_Ggz_Hb_h_43yTQ40eEjV0-hDggzXGiUef_XDfFPtR0Tl6vnMf5hjrohzLDbDRwmnadkp9vISTECR7rg-aII7htF2pmF5ktYQ5rvj6QPajMWcJB1Dt9s8OjyIXwbkNiWbWB-p3_kHti_70jtU7KOxAv4ooNCnTPERyDFViIWCEwaLOuym2SPCkoOcqOzr1VMVKG19uR-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آنتروپیک هنوز جوهر Opus 4.8 خشک نشده بود، مدل جدید Fable 5 رو به عنوان قوی‌ترین مدل عمومی Claude معرفی کرد!
این مدل توی برنامه‌نویسی، تحقیق و همینطور تحلیل تصویر عالی‌ترینه؛ هرچقدر کارمون پیچیده‌تر بشه، برتریش نسبت به مدل‌های دیگه بیشتر و بیشتر مشخص می‌شه.
همینطور به دلیل توانایی‌های بالاش، برای موضوعات حساس مثل امنیت سایبری(هک و امنیت)، زیست‌شناسی(شاید تولید سلاح‌های زیستی)، شیمی(شاید تولید مواد مخدر
😂
) و مطالب مشابه، از مدل ضعیف‌تر Opus 4.8 استفاده می‌شه.
همینطور همزمان مدل Mythos 5 هم معرفی شده که یه نسخه از Fable 5 با محدودیت‌های امنیتی کمتره.
فعلاً Mythos 5 فقط در اختیار تیم‌های امنیت سایبری خود آمریکا و زیرساخت‌های حیاتیش هست و ممکنه بعداً برای پژوهش‌های پزشکی و امنیتی به افراد مورد اعتماد بیشتری داده بشه. طبق جدول منتشر شده، Mythos 5 و Fable 5 در بنچمارک‌ها امتیاز بالاتری نسبت به GPT 5.5 و Gemini 3.1 Pro و خود Claude Opus 4.8 کسب کردن</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/MatinSenPaii/3775" target="_blank">📅 18:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3774">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hc45NxrtT2ld_4HIU53rU7HQ9tSvIHmH6bbQrUE0gnbjf18EwSaYBmkeZJv1Ti_ZRqqO1XNZ8n45m6tixbJ-PUqq5Tj6ITPq_3Se85HqBhpHScgh7Mbjiqw1eYI4jNHamvgLWjiVL93qYtH4KpyKb5X0eUUD2RGXWzp2M9GtL0fq0zPr-OcBnkfY6rvBdciVZCzATYcMmywwuB6ymJ2-2FvxGe6cau65YNSfTqLJmuySqR7dDg2QsqOTCNp82CL_yoQd6ccg1DlsvH3pLZf4APO3J8hpv9yYuxnYarHkd-pBB61VQhFBQRIkSflYjmCUEPoHz71sZW6Mqd8WPbI3lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من خودم با Hiddify راحتترم برای ساب، از اون استفاده میکنم کلا(با نت H+ الان دارم این پست رو می‌ذارم با همین ساب) اگر پینگ نداد، توی تنظیمات Tls Fragment رو روشن کنید</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/3774" target="_blank">📅 16:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3773">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j2YNrs7Ws1RLoWkXjikgl9mwl5oc4_g-tmSTmiXtcfzTax0zAW5hT7vwyo_OA3G6on87ul1unGDsw5k-Y8aC5CnZoVrZja2hNaY4BY52gb9oOUVmFtaHF9K2Pmtl2RkU4QbrInKPe7lvW20eH8NY7acR1VYVzPsZDlQhiNT_u4jmP-ptC9vL_rQnlUZj8sV8MuaquXQrpOYW1X74Br3Ig6eknfZ8UOYhMPrQlf45mpH_sHUAxSCTRT1iOv7oPEBWkuyWwNdeJAstO6PnPqk_UGH85mrGdMOPLlC3ATf6F77qWqltMnSGAlEWr96DQUML10kvXALdr_XKkoqF5nexGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ساب‌ها رو می‌تونید توی هر کلاینت V2rayای که دارید وارد کنید و استفاده کنید ازشون</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/MatinSenPaii/3773" target="_blank">📅 14:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3772">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ساب لینک مخصوص تمامی اپراتور ها نامحدود
❤️
✔️
اپدیت کنین ساب رو اگه نتونستین اضافه کنین ساب رو کافیه لینکو توی مرورگر بزنید بالا میاد و کانفیگا رو کپی کنید
⚡️
لینک ساب دائمی کانفیگ ها: https://raw.githubusercontent.com/masir-sefid/Sub/main/@Masir_Sefid.txt…</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/MatinSenPaii/3772" target="_blank">📅 13:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3771">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمسیر سفید🕊</strong></div>
<div class="tg-text">ساب لینک
مخصوص تمامی اپراتور ها نامحدود
❤️
✔️
اپدیت کنین ساب رو اگه نتونستین اضافه کنین ساب رو کافیه لینکو توی مرورگر بزنید بالا میاد و کانفیگا رو کپی کنید
⚡️
لینک ساب دائمی کانفیگ ها
:
https://raw.githubusercontent.com/masir-sefid/Sub/main/@Masir_Sefid.txt
⚡️
توی تمامی کلاینت ها به جز npv میتونین استفاده کنین پینگ نگیرین وصله
🟢
نحوه ی اضافه کردن ساب لینک با اپدیت خودکار
⭐️
پروکسی 1
⭐️
دونیت برای کمک به ادامه دادن این مسیر
❤️
🪐
Channel |
@Masir_Sefid
| کانال
🪐</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/3771" target="_blank">📅 13:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3770">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">⏯️
ویدیو آموزش استفاده از WhiteDNS Wizard و نصب و راه‌اندازی کامل و اتوماتیک پنل ثنایی
https://youtu.be/rxxlNXLcaqU</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/3770" target="_blank">📅 11:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3769">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🛡️𝔽𝕣𝕖𝕖 𝕋𝕣𝕚𝕒𝕝 𝕂𝕖𝕪𝕤🗝️(ÐΛɌ₭ᑎΞ𐒡𐒡)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c2b536338.mp4?token=n5jgPTn1YzOtSAZwcAP4btnlRkuWY9fwX4RX-ptfozbrtVqC10mwfU3LH7o1PBDrSEBC0s9I_2r0jxNDhze7n8mSjosOdC7EMAfROjdymTHiE7hC-zNdsJ5wlhz9nC-7rIzSyYeNl3EcRx_C1LRVHMrpLsFB6T6ixH684X2VVwApkyMZIEk3J5u9DpXfBBpqkDULiAI6vuwnjc1bB1wmBebpDaB_V-mu5o9yOyv4tyxDQ0367b3AElCPLonLmaeRwYadPoBq5_2_GKezESjfIhQzY2adRHMWC4vEUQE5HNGM2-t4stD0Wy6KfZkBRuf88brYmkN8WgNxpagkeP8A2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c2b536338.mp4?token=n5jgPTn1YzOtSAZwcAP4btnlRkuWY9fwX4RX-ptfozbrtVqC10mwfU3LH7o1PBDrSEBC0s9I_2r0jxNDhze7n8mSjosOdC7EMAfROjdymTHiE7hC-zNdsJ5wlhz9nC-7rIzSyYeNl3EcRx_C1LRVHMrpLsFB6T6ixH684X2VVwApkyMZIEk3J5u9DpXfBBpqkDULiAI6vuwnjc1bB1wmBebpDaB_V-mu5o9yOyv4tyxDQ0367b3AElCPLonLmaeRwYadPoBq5_2_GKezESjfIhQzY2adRHMWC4vEUQE5HNGM2-t4stD0Wy6KfZkBRuf88brYmkN8WgNxpagkeP8A2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روش وارد کردن کلید avast secureline
هر کلید برای صد کاربر هستش
اگه به لوکیشن گیر داد داخل نرفت یبار کلیر کش کنید دوباره کلید رو وارد کنید یا به نت دیگه و vpn دیگه</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/MatinSenPaii/3769" target="_blank">📅 01:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3768">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🛡️𝔽𝕣𝕖𝕖 𝕋𝕣𝕚𝕒𝕝 𝕂𝕖𝕪𝕤🗝️(ÐΛɌ₭ᑎΞ𐒡𐒡)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b056aeeb9d.mp4?token=cx5VEwP3j__3sdBXeZ3vpgWomcI7bDco9msHuUerz39DQAxCFutPWooCsmU3-DXmR9cH01enEOnPTKAlk4Eo0z8jjG8z9dP7bSUdwgV4WyVl1l09J-NImeaodSiKSRV_onFtSXDvaAMBMKEuQzoLhiYOLfr0qViMeIrK25t90WcEcoESZr-KqWPH7PSaRMZ9rr0KFdfZSyIix_0qgQeUeXz8dRt0_gcqqRH2UIbisxNSzUZtJZzfacva7oIOSb8O1M2URT0cX1R-8rRJ04IoZHySF3exeSAu4H3_17NB5ETiKf8h_4oyrbPAb0-5f3Sl20FMJUSBQ3LkOnDvgnap6XvhpE0gHUOrz5DP0S5CJx9a-OCnTWM1MoRCfLsiIYZRxpemyB8eeDGFQeLp-_HiBc-Jt2FB5zybYM1_n7DJGrIhtC4dx29EeVJZzELVT0-_Na3-Hg_XGtcmzXQoqHEkCiy7X603NcXQeevhnXYyDWRlnhHF-cMiuBwI9NItPPdRmceKKJJI-OzC5PjkrqaTiDqN07RjlI1eO3FrukyqCV1n1JAU_45WL3Gjo7eUEvbd7o04yX569kRooIysLCfmEE31VdYn2ZRgWAanvXkImXhAT8_Ez1sNbTObHcci5UF-dPJfLe0CLyyaY12V1E7ySfTg1DCFclg-jF-gY-B6E0o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b056aeeb9d.mp4?token=cx5VEwP3j__3sdBXeZ3vpgWomcI7bDco9msHuUerz39DQAxCFutPWooCsmU3-DXmR9cH01enEOnPTKAlk4Eo0z8jjG8z9dP7bSUdwgV4WyVl1l09J-NImeaodSiKSRV_onFtSXDvaAMBMKEuQzoLhiYOLfr0qViMeIrK25t90WcEcoESZr-KqWPH7PSaRMZ9rr0KFdfZSyIix_0qgQeUeXz8dRt0_gcqqRH2UIbisxNSzUZtJZzfacva7oIOSb8O1M2URT0cX1R-8rRJ04IoZHySF3exeSAu4H3_17NB5ETiKf8h_4oyrbPAb0-5f3Sl20FMJUSBQ3LkOnDvgnap6XvhpE0gHUOrz5DP0S5CJx9a-OCnTWM1MoRCfLsiIYZRxpemyB8eeDGFQeLp-_HiBc-Jt2FB5zybYM1_n7DJGrIhtC4dx29EeVJZzELVT0-_Na3-Hg_XGtcmzXQoqHEkCiy7X603NcXQeevhnXYyDWRlnhHF-cMiuBwI9NItPPdRmceKKJJI-OzC5PjkrqaTiDqN07RjlI1eO3FrukyqCV1n1JAU_45WL3Gjo7eUEvbd7o04yX569kRooIysLCfmEE31VdYn2ZRgWAanvXkImXhAT8_Ez1sNbTObHcci5UF-dPJfLe0CLyyaY12V1E7ySfTg1DCFclg-jF-gY-B6E0o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Avast
Secureline
آموزش دریافت لایسنس‌کی یکماهه
لینک سایت
https://businesshub.avast.com/dashboard
فیک میل
https://temp-mail.org/en/
https://internxt.com/temporary-email
https://mail.tm/en/
https://temp-mail.io/en
لینک دانلود
•
Android
•
iOS
برای کانکت شدن از ی vpn کمکی حتما استفاده کنید
از پروتکل mimic و openvpn استفاده کنید
ÐΛɌ₭ᑎΞ𐒡𐒡</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/MatinSenPaii/3768" target="_blank">📅 01:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3767">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZJgeyp3RgsaBc8sbH1u4t0QrMRiIm0GDLTc9MTvMOzGQmdvQrRlS5M3J3l1QZW4k9bsBywGanU1_X6d55FAp6GjYpRzXUiF6Ibd-bGLrTZ3VUDcCnsIoEyfvM58RKFAYswEFfLjowJDD-twrlOLgO-FgOIObFoqb_RmtwGGqN3ZVNZPST0K5l0AUF6mWKGog_dHAjyNf2u38_SAdkIU6afasforVPQCDY9K2kPuZpGrV7k9UzwIVUNTE-eO3rigrrncuc7Jj19KSOcZW1z1B8z4RCrdkUjJ1APAI474tqMoZWVi5Whf--kyuUu6h6TU4Ip0O_59xkltAs8zO70kZMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وایب کد وایب کده. اسم دیگه روش گذاشتن قرار نیست ماهیتش رو عوض کنه
و نه خوبه نه بد. بحثش به شدت مفصله</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/MatinSenPaii/3767" target="_blank">📅 22:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3766">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">برای WhiteDNS از
http://Netlen.com.tr
هم میتونید سرور بگیرید. فقط قبلا یه تایمی درگاه ترونش خراب بود نمیدونم درست شده یا نه
اینجا میتونید با شماره ایرانتون هم رجیستر کنید</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/MatinSenPaii/3766" target="_blank">📅 17:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3765">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q8xn-gw8YPiTwSvXxyh5ANBQAxX7Ej0KpyiXoJ_tzk0juUxnwwGKp4CNp1t1UNyicVcX0-Asws9vsD7CM7mdI7KXfMwv4zZzh7IUieAHLu8JSkPbfqleXY1p28FQedYdafifV_s1eHt9O8MfJ8q05EuteCAPm7O1upWOPxcsfeAeMBRaecnjWG6-75R87kqLECTpkIo_9aTiSwqSo-alaK7QrRCgCZmDhKjFqRb3_c7AYsSYkWfnL_hlRK7buJKF_-RfIAC2Rru9VnN6CQ8wN3hUWw_B7zK_VfHHb5hcD3EM0EZOWOp_DHPPkBjcsO60CUvcwIZ3ggmokMOqi-1nUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام بچه‌ها:
متین جان لطفا تو کانال اعلام کن که از namecheap دامنه نگیرن. من گرفتم و بعد دو روز به علت تحریمات اکانتمو بست.</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/MatinSenPaii/3765" target="_blank">📅 13:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3764">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اگر توی ساخت پنل bpb یا edge یا nova یا نهان ارور 1101 گرفتید، کلا از اون اکانت Log out کنید و با یه اکانت جدید شروع کنید</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/MatinSenPaii/3764" target="_blank">📅 10:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3763">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اگر توی ساخت پنل bpb یا edge یا nova یا نهان ارور 1101 گرفتید، کلا از اون اکانت Log out کنید و با یه اکانت جدید شروع کنید</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/MatinSenPaii/3763" target="_blank">📅 09:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3762">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دوستان اگر خواستید از سایت yotta سرور و دامنه بگیرید، می‌تونید آدرس فیک از
fakexy.com
بگیرید و استفاده کنید</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/MatinSenPaii/3762" target="_blank">📅 23:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3761">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">Valid-08-June-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/MatinSenPaii/3761" target="_blank">📅 16:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3760">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/67cf13d855.webm?token=BV4FvIGDMWqCEHU0kr6T_U_bjRYOEoOil7u47es4zjdutEUDuFvTpbu-Es7e9705K8-Ik5QY5hm7MFM4rDfeCciohmFnGj5_ufMGn7A58_i2BNYgPq9SVzcAEFHPwGtkL6PAKbFTbGq7lWACa9XM41RfNX-iJP2aStad1glkInRz_b2839UYz-YfkssaP0zJYsGp8B2IRJ2Qo-SRp6hT_9AfNnHLyEl2OyadaBbum6FK6LOW4LCMVObFfM_WKbNvs2YIlje870H4dU-bE9RHgOf61hTZdwOASuzlsrMV326Vp_VLYmFC7_9v8qdHF6pUK7leRTr_3dEKBEhBivrXZg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/67cf13d855.webm?token=BV4FvIGDMWqCEHU0kr6T_U_bjRYOEoOil7u47es4zjdutEUDuFvTpbu-Es7e9705K8-Ik5QY5hm7MFM4rDfeCciohmFnGj5_ufMGn7A58_i2BNYgPq9SVzcAEFHPwGtkL6PAKbFTbGq7lWACa9XM41RfNX-iJP2aStad1glkInRz_b2839UYz-YfkssaP0zJYsGp8B2IRJ2Qo-SRp6hT_9AfNnHLyEl2OyadaBbum6FK6LOW4LCMVObFfM_WKbNvs2YIlje870H4dU-bE9RHgOf61hTZdwOASuzlsrMV326Vp_VLYmFC7_9v8qdHF6pUK7leRTr_3dEKBEhBivrXZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/MatinSenPaii/3760" target="_blank">📅 15:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3759">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Valid-08-June-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">9.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3759" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اینها 688 تا ریزالوری هستن که Valid بودن توی دوره‌ی قطعی برای من، از اون 5800 تا ریزالور ویدئوی WhiteDNS</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/MatinSenPaii/3759" target="_blank">📅 15:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3758">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-poll">
<h4>📊 دوستانی که سرور دارید، دیتاسنترای ایرانتون...</h4>
<ul>
<li>✓ اصلا وصل نشده بود هنوز اینترنتش</li>
<li>✓ وصل شده بود، الان قطع شد</li>
<li>✓ وصل شده بود و هنوز وصله</li>
<li>✓ سرور ندارم، دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/MatinSenPaii/3758" target="_blank">📅 13:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3757">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترجیحا هیچ VPNای نخرید دوستان. هیچ تضمینی نیست که اگر اینترنت قطع بشه هم اونا وصل بمونن یا نه. مثل اوایل جنگ که خیلیا اسکم شدن
همون هزینه رو بذارید whitedns راه بندازید</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/MatinSenPaii/3757" target="_blank">📅 12:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3756">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">هر پنج دقیقه میرم یه پینگ میگیرم ببینم وضعیت چیه
روانیمون کردن</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/MatinSenPaii/3756" target="_blank">📅 12:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3755">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اینکه هنوز اینترنت قطع نشده جای تعجب داره به خدا</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/MatinSenPaii/3755" target="_blank">📅 12:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3754">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مجددا تأکید می‌کنم که سرورهای عمومی سرعت به شدت پایینی دارن مخصوصا توی محدودیت‌های شدید و بسته شدن ریزالورها. تمام تلاش رو بذارید روی راه‌اندازی
سرور+دامنه شخصی</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/MatinSenPaii/3754" target="_blank">📅 11:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3753">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سرورهای عمومی MasterDns(با کلاینت WhiteDNS):
1-
https://t.me/Masir_Sefid/612</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/MatinSenPaii/3753" target="_blank">📅 09:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3752">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FpiHyNWFWGIfei1YWJLpJQgY6hnuzXgKgzlbdr_vno9VPJ9xmW8PTiVeKcllpNXiubbeu-NuhAA5ffefO8kYoiQUvLd_l7JSO_KJaydF8RTaHv-93c45Nav-EupLF7Vg6M0eosN4TN3ZH763XnM3uEpS7vVMwrTsW9To-aytqOvEznoFg5yjNtDxCu4aEBMv-0cutA61Io4HZc4LlPddcLqLTr4iAEIkGKKHHxS93CGKRbjUdRiyTckUbBxdLErTUJ8iYaxa99aGoI0t1PjrcWLeVTcZbruzlYkRitkZZFD6YbxIWVftMW22I60IBE7jpP5T2r9h-ank83uH-n2hWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب همونی شد که فکر می‌کردیم. جنگی در کار نیست انگار تا بعد از جام جهانی. فعلا اینترنت داریم</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/MatinSenPaii/3752" target="_blank">📅 08:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3751">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خب همونی شد که فکر می‌کردیم. جنگی در کار نیست انگار تا بعد از جام جهانی. فعلا اینترنت داریم</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/MatinSenPaii/3751" target="_blank">📅 08:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3750">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دوستان دامین سالم این شکلیه. نه اینکه از ۵۸۰۰ تا بهتون ۴ تا valid بده</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/MatinSenPaii/3750" target="_blank">📅 00:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3749">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kS3jaOwsjklRy21iaYrxenJEcsuSeGfb43Mq_iC6w83pOjRZoZ9JzvKOLLSkAwTRhqM6lq96aml3jfEDh9zFSsA8xLRltO676GdYUhOTkiPH9nUZOLNcWQwtN7FlWywAHMtLBDV93QIYmiKD9Zhj4-YWyFkTPOMvpsVJvsywL1gSqPlgjBLLCCIaxkSwMmLvNjbwpW7jChicgf-Pe940a0iMzXS1AQQKi4HNOBlwegKqXFM0eg-JN1BNwf6lVZJEshpfJTe_8aLkSo6jtV0fHbnPMtRwO2YBwAHcAbty11MV0707F8JcTw9CWxKvmLoHwOqYoWlK4VaR1WIIDypIiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان دامین سالم این شکلیه. نه اینکه از ۵۸۰۰ تا بهتون ۴ تا valid بده</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/MatinSenPaii/3749" target="_blank">📅 00:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3748">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-poll">
<h4>📊 سرعت اینترنتتون؟</h4>
<ul>
<li>✓ تفاوتی نکرده</li>
<li>✓ یه کم کندی حس میکنم</li>
<li>✓ تمام کانفیگا از کار افتاده و نمیتونم به هیچی وصل بشم</li>
</ul>
</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/MatinSenPaii/3748" target="_blank">📅 23:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3746">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">Matin SenPai
pinned «
دوستان با این اوصاف حمله‌ی پیش‌دستانه WhiteDNS+Master راه بندازید که هر لحظه ممکنه اینترنت رو قطع کنن متأسفانه. توی ویدئو آموزش خرید سرور و دامنه و راه‌اندازی و تانل کردن کل سیستم و راه‌اندازی روی گوشی و سیستم هست کامل: https://youtu.be/6Pm7kNQb3mo سر هر تحرک…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3746" target="_blank">📅 23:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3745">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/MatinSenPaii/3745" target="_blank">📅 23:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3744">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تا حالا حمله‌ی پیش‌دستانه تجربه نکردیم. اگر منطقی باشه، اینترنت به جای قطع شدن باید قوی‌تر بشه</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/MatinSenPaii/3744" target="_blank">📅 23:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3743">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دوستان با این اوصاف حمله‌ی پیش‌دستانه WhiteDNS+Master راه بندازید که هر لحظه ممکنه اینترنت رو قطع کنن متأسفانه.
توی ویدئو آموزش خرید سرور و دامنه و راه‌اندازی و تانل کردن کل سیستم و راه‌اندازی روی گوشی و سیستم هست کامل:
https://youtu.be/6Pm7kNQb3mo
سر هر تحرک نظامی و موشک مجبورم این حرفو بزنم چون احتمالش هست واقعا هر لحظه</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/MatinSenPaii/3743" target="_blank">📅 23:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3742">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">تغییرات WhiteDNS Wizard v1.1.0
- خطای ACME و DNS بهتر تشخیص داده می‌شود.
- قبل از ساخت SSL، برنامه چک می‌کند دامنه واقعا روی Cloudflare فعال و درست تنظیم شده باشد.
- پیام‌های خطا واضح‌تر شده‌اند و کاربر بهتر می‌فهمد مشکل از توکن، دامنه یا DNS است.
- آموزش دسترسی‌های Cloudflare در README کامل‌تر شده.
- Reality XHTTP با Reality TCP Vision جایگزین شد.
- Reality حالا از
xtls-rprx-vision
استفاده می‌کند.
- انتخاب SNI برای Reality امن‌تر و پایدارتر شده.
- مسیر نصب روی سرور از
/opt
به
/var/lib/whitedns
منتقل شد تا روی VPSهای بیشتری بدون مشکل کار کند.
- مشکل ساخت فایل Docker Compose روی بعضی سرورها رفع شد.
- نصب Docker Compose Plugin روی سیستم‌عامل‌های مختلف بهتر شده.
- بیلدهای GitHub Release سریع‌تر شده‌اند و به صورت موازی ساخته می‌شوند.
- چند مشکل مربوط به مسیر فایل‌ها، ریستور، تست‌ها و آپلود فایل‌ها رفع شد.
https://github.com/iampedii/WhiteDNS-Wizard/releases/tag/v1.1.0</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/MatinSenPaii/3742" target="_blank">📅 21:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3741">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">یه جمله‌ی مشترک که از افرادی که پایتون اولین زبان برنامه‌نویسیشون بوده و بعد از اون رفتن سراغ یه زبان دیگه(علی‌الحصوص
زبان‌های کامپایلری
) زیاد شنیدم، این بوده که تازه با یاد گرفتن یه زبان جدید فهمیدن برنامه‌نویسی چیه. و درک و قدرت حل مسئله‌شون اونجا بوده که رشد کرده. علتش برام جالبه</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/MatinSenPaii/3741" target="_blank">📅 20:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3740">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">این پنل هم دیدم بچه‌ها زیاد باهاش ساخته بودن vpn روی کلودفلر. یه تست بکنید https://github.com/IRNova/Nova-Proxy</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/MatinSenPaii/3740" target="_blank">📅 17:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3739">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">این پنل هم دیدم بچه‌ها زیاد باهاش ساخته بودن vpn روی کلودفلر. یه تست بکنید
https://github.com/IRNova/Nova-Proxy</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/MatinSenPaii/3739" target="_blank">📅 15:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3738">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمسیر سفید🕊</strong></div>
<div class="tg-text">ساب لینک
مخصوص تمامی اپراتور ها نامحدود
❤️
✔️
اپدیت کنین ساب رو اگه نتونستین اضافه کنین ساب رو کافیه لینکو توی مرورگر بزنید بالا میاد و کانفیگا رو کپی کنید
⚡️
لینک ساب دائمی کانفیگ ها
:
https://raw.githubusercontent.com/masir-sefid/Sub/main/@Masir_Sefid.txt
⚡️
توی تمامی کلاینت ها به جز npv میتونین استفاده کنین پینگ نگیرین وصله
🟢
نحوه ی اضافه کردن ساب لینک با اپدیت خودکار
⭐️
پروکسی 1
|
پروکسی 2
|
پروکسی 3
⭐️
دونیت برای کمک به ادامه دادن این مسیر
❤️
🪐
Channel |
@Masir_Sefid
| کانال
🪐</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/MatinSenPaii/3738" target="_blank">📅 11:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3737">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromیـ بـ خـ(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dH6hSldB4Rd2qLrn5e23tLsKBDtLXpq73y3Lzz-rLJjeIP-8PwMNwMoREA4fPhqS_Ak7YBnuDuIo3sgUdTi5HeaO_Vm5GyL4GQ5QVrjraN8F_nX1gnb7jIpDC_pMmJ49gJVlHtmHHnU0CQk1hpW21I39bKTpWQ1CDWWhBjVGEuhbFVhCe7ak7c0cfF9xIWe-4s2Gt-MyVgNkCBsS66Hph435qXsg70EHoHNunpZQ7r94IW5yKs591TxQIcr0g7IPbCdnBo8sYwkcNgaNcEm72IR_6eH9udeQnjf8G0T09lo8v_s60Z5Sqh3FLiGjtmI4zlhiGUJv8TnDt5aPt9kICw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه نهان
🍷
پنلی بر بستر
#کلودفلر
با کلی قابلیت به صورت رایگان و تنها با دادن ip واسه خودتون یا خانواده فیلترشکن بسازید...
ویژگی های این پنل:
✅
⭐
محدودیت حجم گذاشت
🗓
تاریخ انقضا تعیین کرد
🚫
دسترسی رو قطع کرد
✅
دوباره فعالش کرد
❗️
مصرفش رو دید
و همه اینا بدون دست زدن به مستقیم به Worker یا KV.
‏یه سری امکانات مدیریتی هم داره که بعد از مدتی استفاده واقعاً به درد می‌خورن:
⚡️
داشبورد مصرف
☁️
Cloudflare Analytics
🔔
نوتیف با بات تلگرام
💾
Backup / Restore
و چندتا ابزار دیگه که کم‌کم بیشتر میشن.
لینک خود پروژه:
https://github.com/itsyebekhe/nahan
@yebekhe
👑</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/MatinSenPaii/3737" target="_blank">📅 08:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3736">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🍷
یه سری نکات رو بگم در مورد bpb:  کانفیگ ممکنه پینگ نده واستون ولی کار کنه الویت رو پینگ نزارید  داخل تنظیمات اگر مشکلی بود به جای chrome از firefox استفاده کنید  اگر اینترنت شما 8.8.8.8 کار نمیکنه یا اختلال داره سعی کنید از dns زیر استفاده کنید:(کمترین اختلال…</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/MatinSenPaii/3736" target="_blank">📅 01:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3735">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">☠️
آموزش ساده آپدیت پنل BPB به آخرین نسخه  نکته: همونطور که توی ویدئو گفتم این صرفا آموزش آپدیته و هنوز نسخه‌ی استیبل نیومده اما می‌تونید استفاده کنید از ورژن‌های Pre-release
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی  BPB برای دانلود فایل…</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/MatinSenPaii/3735" target="_blank">📅 01:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3734">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏نسخه‌ 4.2.2 پنل BPB منتشر شد
🕶️
طبق گفته‌ی
برنامه‌نویس پروژه
، این نسخه مشکلاتی که از سمت کلادفلر بودن رو برطرف کرده
🔁
اگر دارید پنل جدید باهاش می‌سازید هیچ کار اضافه‌تری نیاز نیست، ولی اگر آپدیت می‌کنید باید همه‌ی ساب‌ها رو آپدیت کنید و اگر دستی توی داشبورد مقدار compatibility date رو تغییر داده بودید، بذارید روی جدیدترین تاریخ
طبق ویدئویی که برای آپدیت دادم
📆
تغییرات این نسخه:
1- بخش جدید External Raw configs:
میتونید ساب و کانفیگای شخصیتون رو اضافه کنید که همه‌شون به ساب Raw اضافه می‌شن
💪
2- بخش UpStream اضافه شده که می‌تونید به طور مثال
127.0.0.1:40443
رو به عنوان آیپی و پورت دیفالت بذارید(برای اسپوف) که به ساب Normal و Raw اضافه میشه و دیگه نیازی نیست دستی ویرایش کنید
💪
3- تغییرات جدید هسته‌ی Xray اعمال شده که حتما باید کلاینتاتون(V2rayNG یا هر کلاینتی استفاده می‌کنید) آخرین نسخه رو داشته باشه
😎
جزئیات کامل تغییرات رو اینجا بخونید:
https://github.com/bia-pain-bache/BPB-Worker-Panel/releases/tag/v4.2.2
آموزش ویدئویی آپدیت از نسخه قدیمی به جدید:
https://t.me/MatinSenPaii/3732
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/MatinSenPaii/3734" target="_blank">📅 00:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3733">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FqMYtOBAGrVDGcgDvZsPm_ZhL_qSO6gh-N_Wu7l2db7UBuCBvqD2lrZPJynx8QPP4Lc-xD3lJyhoDredsr_YfDgASXuqAk7d6q_TmgqTMtR7HbaTXYS_761pWzfNonQlOX8DmZcmYrDgqvW1h4EIbDudj7RC3fIG7CsfFvd8_W137WV0Nkz-3XoBAFHe7H0Rr9e37EPHrObiOnlyj8NfPGFuQBHpMUE0tSGXkVqmpJbBJq3X12L4CN1xZB-q22jymTqw03zfbiw4hJ3d9i7TPzObyd9np-I5Q1sTxX0u3Xi-EbpnUylkSSHzCEL3HsChJIPBfW2QFDg0YvNG36rxpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگار دیسلایک اضافه کردن به توییتر</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/MatinSenPaii/3733" target="_blank">📅 20:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3732">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">☠️
آموزش ساده آپدیت پنل BPB به آخرین نسخه
نکته: همونطور که توی ویدئو گفتم این صرفا آموزش آپدیته و هنوز نسخه‌ی استیبل نیومده اما می‌تونید استفاده کنید از ورژن‌های Pre-release
⚡️
لینک سایت کلودفلر:
https://dash.cloudflare.com/
لینک پروژه‌ی  BPB برای دانلود فایل ورکر:
https://github.com/bia-pain-bache/BPB-Worker-Panel/releases
⭐️
توی این ویدئو بهتون یاد میدم که چه شکلی می‌تونید پنل BPB رو آپدیت کنید
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
قبلش باید این شکلی یکی ساخته باشین:
https://youtu.be/_aXy8wwyRG8
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/MatinSenPaii/3732" target="_blank">📅 16:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3731">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔥
1500 کانفیگ جدید به ساب WhiteDNS اضافه شد
.
همون ساب های قبلی رو رفرش کنید.
⬅️
آموزش استفاده از FlClash
⬅️
آموزش استفاده از Clash Party
ممنون از همراهی شما
🤍</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/MatinSenPaii/3731" target="_blank">📅 15:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3730">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⚠️
Confirmed: Metrics show a major disruption to internet connectivity in Pakistan-administered Azad Jammu and Kashmir.</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/MatinSenPaii/3730" target="_blank">📅 13:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3729">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHaoodi Senpai</strong></div>
<div class="tg-text">یک سری بحث و احتمال هست که یوتیوب فیلترش برداشته بشه، همون‌طور که گویا برای یک سری شده الان هم (البته مشخص نیست اختلاله یا واقعا داره رفع فیلتر میشه).
اینکه حقی که ازمون گرفتن رو بدن هنر نیست، ولی خب واقعا خوب میشه اگه این اتفاق بیفته و مردم همه بتونن دسترسی داشته باشن
♥️
همون‌طور که
قبلاً هم بارها گفتم
، ما یوتیوبر بی خانمان هم بشیم مهم نیست، مهم دسترسی درست هست و آزاد برای همه هستش.
اون یوتوبر بی‌شرفی که ناراحت میشه از آزاد شدن دسترسی هم بنظرم هرچه سریعتر آرک تمرینی نفس نکشیدن رو شروع بکنه
🫵🏻</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/MatinSenPaii/3729" target="_blank">📅 12:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3728">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مراقب باشید سرور ۱۲۸ مگابایت رم و بدون ipv4 و اینا نخرید دوستان
😂
اونا رو هیچ کاریشون نمی‌تونید بکنید</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/MatinSenPaii/3728" target="_blank">📅 12:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3727">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یکی از دوستان توییتر(ixAbolfazl)، دیشب یه سایت معرفی کردش برای پیدا کردن ارزون‌ترین سرورهای مجازی یه سریاش قیمت سالیانه‌شون کلا 2-3 دلاره. در این حد و کریپتو هم قبول میکنن مجدد یه سریا  آدرس: serverhunter.com</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/MatinSenPaii/3727" target="_blank">📅 11:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3726">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uM_ipgvqITMzb5ZbwLPIG5yVGE_JGLRktEMvNIPndqhT7AenDrX335npgqg1eJMxmb-u0TIsBq_eTa3PQiRoNE7lvQo6qsh7yzKchAHrsbBh1bqvu9b9L4zlKffSXzKmlKkfZXAkNzUjwDthh0bHtGraUfRrJ9yMtLEMlhEMh7Hjmzn4Pdq_dwpdng5VOMu3moBzVWPlnfUM5k7W_b_dVaKoAGWh-SWWcdF_eRzfTHg2Ukyn8rYlynL80I3MiMXGerhIAb6xaTOOo8_jGSjdDfRvt7iyAGodqvpjb2Qov6YtcbvOEthJQ5vVYN_-5CXN2QA_lQsEoC-aTcNGrPQPpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از دوستان توییتر(
ixAbolfazl
)، دیشب یه سایت معرفی کردش برای پیدا کردن ارزون‌ترین سرورهای مجازی
یه سریاش قیمت سالیانه‌شون کلا 2-3 دلاره. در این حد
و کریپتو هم قبول میکنن مجدد یه سریا
آدرس:
serverhunter.com</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/MatinSenPaii/3726" target="_blank">📅 08:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3724">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pjntDSpmkkIg0iTBXmpkCuj85rtSP6amjmjnCUJu7RSWnAwj0L3s49TNRSTXqNuFfN8NIQk2TQpkDp-6Lqjsmtqg9hqTiGtR36JdR3TGRnK-S2XE3_zzkMOUTazpi7ZTRMwXg3HYjGP8h4Tkd270KCeLHVR0rKQNhl45jJfyBcJw7f6N7VL9jb3FaqEyT5bqGvBk7c-MlAOha9zUErPghDn3pswf16q9t_paytulqACzyGCkZOjnZI-tDBQMvUr3kVtZEPffSdn_ypBQnLMdV6FepbHPvKy5gIsH926AALLohYHZC6hUZqksIriXmVTsj14VR2oXQCsVQE6ZhZH0tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KgXrqLCNJlsGECLAUw_L6CNCZyflsYqO-6HMvu4i1W8gQmpblq6nxu5_t2eAkA42BAMgg5z9p-qCQSUI7WHJ-ayPLDyOqQFqvgT9IDgrs0brUNqGhAMhh_OHUywXOv3_h839medxwBwoD-vP6Y4SLCgEGbwtBgzMbhscr5VcFv9tFIxyVS5d9jY7Ea66GFZWgrU9DOMDEoEt9UGFW8GTlZDpRKMqWtpwBK6Xr3Gvjoh6YTAktHFPI5xUlLBQyoZm3XUUFFFIKCuAItmx5676bgzI_qQfrFdhZ4IgvbkN_9cL5WtA7CojxL2e4qCbp5WznrnyEyRbRoLjQBG0vxMyjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">والا برای من هیچکدوم روی ایرانسل و همراه اول نمیان
یه سری شایعه شده بود که میخوان یوتوب رو رفع فیلتر کنن
اما خب بازیشونه دیگه. سرگرم کردن ملت</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/MatinSenPaii/3724" target="_blank">📅 02:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3723">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cq3yNDiA-Us7rTh70z_U0I5tY9KEpZyAhSzS-mfRZu5KmKk8YO-1v-L_AGxa_gm0_UA8nf2jwV0YIEzcV86wRS7max7R2ogRqN2fWuGCwXeohZgiD1m0MMhUzeCvTBxUWLMPZ5hoITp9Oawa7xHwiJC6IoEWbsPyZLONWnJaQzMqpwuwE0vsQ4Dxhokg9txsa7vZgpKebXuElVgTwXUsrdFm7CpAvzAY9-jaGPqLlBVTPwo_gCxjwwemA3ntrnFy5K71UFZrxx-_U6EkEFO7CuTUM_tzYVf3YPGqDGeJLVNoCIJ9Ihavm9aikhTVMQ0qWlxgThyxh-0wmB6nMSBSjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای شما هم این شکلی شده بچه‌ها؟ با لایک و دیسلایک بگید
شنیدم این رو چند بار از سر شب</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/MatinSenPaii/3723" target="_blank">📅 02:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3716">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">31.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3716" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بفرمایید تست کنید. ورژن 0.6.0</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/MatinSenPaii/3716" target="_blank">📅 02:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3715">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kj0-9kIJLDgV8_03cihxx_ub5jYYZXiInOLDbPpZ_20BZjq5OisgsSxrHfDHVBNBHq8bJZsP5CWAE3SuwI-p8H5VSesXiqsysU_qYez5B9k6hqYhkmyRZjqW9ohvSHxjNrMDwYcRdJIfP68HLuEbqb_Akkn6VwM1I0fG9iKjGCU4s4fRbg6KPluYbEK2DVMUA5h1wlkIv6A13baQkU4_IOP0PbMKolMg1GCWtYY9GrIhiuedC1tXWwBavFDOzmz07Cf3QlQpGdO8-19uDdjAw5CTgt5JbKgcGnL1dQg6z7nTbHSAn0mhewwZwGfeYAV3NjgA5LY_0CZxaj1wmZvuwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشکل بزرگ اسکن روی اینترنت سیمکارت هم حل شد</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/MatinSenPaii/3715" target="_blank">📅 01:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3714">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مشکل بزرگ اسکن روی اینترنت سیمکارت هم حل شد</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/MatinSenPaii/3714" target="_blank">📅 00:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3713">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hieuf1-A7AEBJvUI3TvT7ZaLoIebMW2yvMPqQi0E20spavEstLYbqCtVs4POR0bcAb_Pu4P8jufcqrEpQ-2U39qzAhkoL8BRvi9n_3cfpnmcs5WP_xtYeMNkVqauTetuJQqd4UIws0bJ9jN_RmgPAJRitZ8U6gorG5Xrb2ZKcqAWSTJwmpIHujWrc3g9drHakAlLIeznBe15NKsl6qAv4UG8LtExJ1pejPEQH2oLHbBx4TYhFGptasMB8YdfPZSTvehNc51uZdTHp41y2vDmvnBlB5cKVpfoPH66TcS2jMM9mmkBMIPKU_ZIxLGU3E7gDRCW2ayP9d2dq9hSolTO3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان این رو بگم توی ورژن جدید هسته‌ی ایکس ری، حتما باید Allow Insecure رو False بذارید توی کانفیگ وگرنه ارور میده</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/MatinSenPaii/3713" target="_blank">📅 00:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3712">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">یه کار جالبی یکی از بچه‌ها سر SenPaiScanner در آورده که واستون قرار میدم به زودی. PR های بقیه‌ی دوستان هم بررسی کردم و همه عالی بود و تأیید شد و رفت روی کد اصلی</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/MatinSenPaii/3712" target="_blank">📅 00:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3711">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">یه کار جالبی یکی از بچه‌ها سر SenPaiScanner در آورده که واستون قرار میدم به زودی. PR های بقیه‌ی دوستان هم بررسی کردم و همه عالی بود و تأیید شد و رفت روی کد اصلی</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/MatinSenPaii/3711" target="_blank">📅 00:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3710">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Uoouhm_etz-s_UTyFYjv3CoA9PITAoETg7yFnk_umhvQxjnqHPfHifYaujKO_T0grkvZoO9v0HKUdYt-I1eC2KieoCAuRuBWHJD9Ylp8SumaKO52fvQmYo8ga1SFJSQtMixtt8WU0k4ToanVPXLdRG0txFe1ddd7djVUQ0KjwsheoveWtNFTnQ7z9viXobGsqsYpBoP8Fg9Foz-kZKeOfMmLrZ593bnsSgn8lUcwMLI2MWsZ54S_9F9Wi1c0Yu-p8s_PZuKx2t652J5XZQRf5KBtT4jfsfFJ-NsRKkuqx6FGG23k_8hswNw_tnCoiI-zf-5R1YlkYlNBQ8w-FC6V0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرویس WhiteDNS-Wizard برای کسایی طراحی شده که سرور و دامنه خریدن، و حالا نمی‌دونن که با اینا چیکار بکنن
👍
این نرم‌افزار مولتی‌کراس پلتفرم تحت CLI اوپن سورس، از شما اطلاعات سرور و دامنه میگیره، به علاوه API-TOKEN کلودفلر، و برای شما صفر تا صد کار نصب پنل، گرفتن سرتیفیکیت و ssl و ... رو انجام میده. و این خروجی‌ها رو میده:
1- کانفیگ VLESS WS شخصی
2- کانفیگ REALITY-XHTTP شخصی
3- کانفیگ Hysteria2 شخصی
4- کانفیگ Shadowsocks شخصی
5- کانفیگ Tor vless ws
6- کانفیگ Tor Hysteria2
7- کانفیگ Tor direct
8- به زودی مستر و ... هم اضافه میشه
آموزشش رو هم داریم با آپدیت بعدی
گیتهاب:
https://github.com/iampedii/WhiteDNS-Wizard
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/MatinSenPaii/3710" target="_blank">📅 22:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3709">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVMNJkiERh828jvgvO53SfDZU9qje56B5Mdg_nNQHRMQUX7p1rl3ynHHz6SzfJNukbicB-FA2QOi3ImMHErP75BB-niM--Y0PerEA7sj0MG5HPro9W3NFQrABFCFZqCU6uA6GsqUrU9m4pD8uhcvQiVXV3ExDHwqH6-lqajAtLb2S1hrBiod8_l3NQ7ffwuTa0jmns_UjzE3zxpvPKrw9zsAYZ6FszS96Z3p3FUfp8lHz_7rOwYSb51gKLCwUV5eZieTap9TvsAaVGnCwssj_4co_YYq_98MlNssmPOOt-JBpbUP5hJzXH--OW09earUvMbQfq5AQ6VOwtVZ_QEl-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">AzadiTunnel نسخه آیفون شیر و خورشید
👑
یک اپ iOS برای اتصال امن و پایدارتر، با تمرکز روی تجربه ساده، CDN Fronting، DNS هوشمند و تست اتصال.
📱
لینک مستقیم اپ استور:
https://apps.apple.com/ca/app/azaditunnel/id6776486891
منبع توییتر
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/MatinSenPaii/3709" target="_blank">📅 20:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3708">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ورژن جدید 4.2.0 BPB رو تست کنید بچه‌ها. سازنده‌ی عزیز روی مشکل Undefined کار کرد و درستش کرد. همینطور بخش Compatibility date رو نیازی نیست دست بزنید دیگه https://github.com/bia-pain-bache/BPB-Worker-Panel/releases/tag/v4.2.0</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/MatinSenPaii/3708" target="_blank">📅 18:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3707">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WWSnYx-NKRYlljwlJHbxvce5OJR6aB_jbTO_rQEk2d_ezdBCbLxqlOxVFC9FT24N70s546fELoX1dymwv-Xnzyu_BtGCCzWapzdlX7JfxSTk5QvcKmRbN-xnuFcvzIDcjzpDYpXwKGMUY3R-ahcZKGChzyIMesy8J5ddWs-4bkZaPWIncK4XcTY1NLfshYpGmYSvqkm77IDewLUuHUJrxEeoZA07MwhAnrMH6shzXMsU17o6w_8X4x81VtYfuCJNjN-RPWIjkRZWBv1uL-0cs51NvGWCplZnxY86vdye_n6jhwbBR_G-YGsQOBiE1b7-x2x2X5qTMuFMZlKmGd7Teg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏شرکت OpenAI ویژگی Dreaming رو برای حافظه ChatGPT معرفی کرد!
بالاخره بعد از مدت‌ها انتظار، OpenAI ویژگی خیلی مهمی به اسم Dreaming رو برای ChatGPT معرفی کرد. این آپدیت حافظه رو از حالت «یادآوری ساده» به یه سیستم هوشمند و پویا تبدیل کرده.
قبلاً چی بود؟
قبلاً ChatGPT چند تا نکته رو یادش می‌موند، ولی بعد از مدتی قدیمی و بی‌ربط می‌شد. مثلاً اگه بهش گفته بودی رژیم غذایی خاصی داری یا پروژه‌ای داری، بعد از چند هفته دیگه درست به یادش نمی‌اومد.
حالا با Dreaming چی شده؟
با این قابلیت ChatGPT تو پس‌زمینه (حتی وقتی باهاش حرف نمی‌زنی) همه چت‌هات رو بررسی می‌کنه، خلاصه می‌کنه، الگوها رو پیدا می‌کنه و حافظه‌ش رو همیشه تازه و به‌روز نگه می‌داره. انگار داره «رویا می‌بینه» و اطلاعات رو مرتب و هوشمندانه سازماندهی می‌کنه.
فایده‌های واقعی‌ش چیه؟
شخصی‌سازی خیلی بهتر: ترجیحاتت، علایقت، محدودیت‌هات و جزئیات زندگی‌ت رو خیلی دقیق‌تر به خاطر می‌سپاره. مثلاً اگه قبلاً گفتی عاشق عکاسی طبیعت هستی، دیگه پیشنهادهای generic نمی‌ده؛ مستقیم بهت ایده‌های مرتبط با سبک مورد علاقه‌ت می‌ده.
پروژه‌های طولانی: اگه روی یه پروژه چند ماهه کار می‌کنی (مثل نوشتن کتاب، راه‌اندازی بیزینس یا یادگیری زبان)، لازم نیست هر بار از اول توضیح بدی. ChatGPT زمینه کامل رو حفظ می‌کنه.
آپدیت خودکار: مثلاً اگه گفتی قراره به سفر بری، بعد از سفر خودش متوجه می‌شه و اطلاعات قدیمی رو پاک یا آپدیت می‌کنه.
کنترل کامل داری: می‌تونی حافظه رو ببینی، ویرایش کنی، بگی چی رو فراموش کنه یا چی رو حتماً یادش بمونه.
در کل، ChatGPT دیگه مثل یه دوست معمولی عمل می‌کنه که فقط حرفاتو گوش می‌ده (حتی این هم با ما دوست معمولیه!) حالا مثل یه دستیار واقعاً باهوش شده که تو جزئیات زندگی و کارتو درگیره و همیشه به‌روزه.
این ویژگی از امروز برای کاربران Plus و Pro در آمریکا فعال شده و به زودی برای بقیه کشورها و حتی کاربران معمولی هم می‌رسه.
لینک کامل توضیحات OpenAI:
https://openai.com/index/chatgpt-memory-dreaming/
✍️
Diego JR</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/MatinSenPaii/3707" target="_blank">📅 15:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3706">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ورژن جدید 4.2.0 BPB رو تست کنید بچه‌ها. سازنده‌ی عزیز روی مشکل Undefined کار کرد و درستش کرد. همینطور بخش Compatibility date رو نیازی نیست دست بزنید دیگه
https://github.com/bia-pain-bache/BPB-Worker-Panel/releases/tag/v4.2.0</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/MatinSenPaii/3706" target="_blank">📅 14:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3705">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fhlidh5RMOZxJlKZG-PV5ww58bRGnFiVBaUUpddkdzwJ7IXlUlw85G3L7_9xZZTRCayfJutRNxmWHQ_Yqtv8lQ0MYlTeexZVd7pXR54ZpcY-KwrUzhFYjPLX4SktB-b9wbG6UKZmDPJ9AChXXcXmvLRKgKB4C8N-zJXXvcUtcN7LI8oOQhwgmQkra99Hv0s_OM9BJndnA3DE74CbNUsl4gx1Htk8lgD7h3sRh1bku9xzrxNhwcQdBSsHtkIfmihBk9uSaaVmcgZ0xiFjLS05vZ88mKEiEA6ET1avTF9U77UKllaEvdrEbof83Du1kLZ7W6k4fYCCMBuS7spL9RVVcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اگر کانفیگ worker پینگ می‌ده اما درست وصل نمیشه تنظیمات مثل عکس قرار بدید fingerprint روی Firefox و Alpn روی http/1.1
یا اگر توی mahsang هستید Psiphon انتهای اتصال قرار بدید
✍️
🏴
Amin
🏴</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/MatinSenPaii/3705" target="_blank">📅 11:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3704">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دوستان این رو بگم توی ورژن جدید هسته‌ی ایکس ری، حتما باید Allow Insecure رو False بذارید توی کانفیگ وگرنه ارور میده</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/MatinSenPaii/3704" target="_blank">📅 06:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3703">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/feK58v4d4bJcbB-OZ5DvvXZc61PqjtNT7NlRtwrFN5zd4_b7Izul06Ht1Yv7RKJ4FfZD0FKnq1aZus7QvfO_qptMEnf8YhYovK-5mXcjeGxCcg4NS9jvLJih5SV7DySAVvP-02zA2plI2q5xJA5Rfn5nx5cSGTD_IXbWEsCJjvJQMmXTeNXBFpR5tIhZibTuYFBAhgeK5Y80NIPNB-jma-z251w3KFckGDp1IV0xD7dHy36PmyEPR_nMkAz7l7apNlFboBk7N8d_sx_HjjflqodTAcRFLTRt58-FsGB1103dJPLZ3Kcvgo2p3wCXN2oVaH6uFQeGSPexpIouKDqRDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به چند سرویس تحریمی مثل اسپاتیفای، گراک، کلاد و ... ربطی به آتش‌بس، توافق و رفع تحریم‌ها نداره و مربوط میشه به دستکاری شبکه توسط فیلترچی و عبور ترافیک از شبکه آذربایجان!</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/MatinSenPaii/3703" target="_blank">📅 23:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3702">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qwmlUEB2YwCjkt-ODo5yOHheMF9f2wYnQN_EGuO-3GVD6q9y0QfF7Dsj8SlE_YZp2FRZSuBNYsWzghRIkh9JpzpAM_YFRNSYDrx0UgZwe2cw5UbOKrNkLB0ZFjfi2n_EfW5pO2wp1knFZxYvBHkYafGrVSuaHa61dIGex7iip1xxH30ALomlG8WIjK56dJ_qlGtMSpwzXOUhpJjm0H8dWfBEgEtkc5-XY1sQVuGeBxj5XfJsbnPOKWhYmW9dkq5zmNYaDTfvFAPUTr737jvUQxEa7BXlJnMD249qOB_ILchByMSYzs3h5PEo_47Pcl3ZcBQBkDYHJe0cFsNpDvicYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محدودیت کلودفلر(روزانه تقریبا ۶ گیگ) روی اکانت کلودفلر شماست. نه خود Worker
پس اگر می‌خواید این محدودیت بشه 12 گیگ، یه اتمیک میل جدید می‌سازید، یه اکانت کلودفلر جدید می‌سازید، و یه بار دیگه مراحل ساخت رو پیش میرید روی اکانت جدید</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/MatinSenPaii/3702" target="_blank">📅 23:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3701">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">📌
چند نکته کاربردی برای بهتر وصل شدن با FlClash در اندروید
یکی از کاربران WhiteDNS تجربه‌ی شخصی خودش را از کار با FlClash فرستاده که برای اتصال بهتر مؤثر بوده.
اگر با FlClash مشکل اتصال، آپدیت نشدن ساب، پینگ‌های عجیب یا ناپایداری دارید، این موارد را امتحان کنید.
━━━━━━━━━━━━━━
1️⃣
بعد از نصب، قبل از اضافه کردن ساب، Resourceها را آپدیت کنید
بعد از نصب FlClash، قبل از اینکه لینک سابسکریپشن را اضافه کنید، وارد این بخش شوید:
Tools → Resource
و تمام Resourceها را آپدیت کنید.
⚠️
نکته مهم:
طبق تجربه‌ی بعضی کاربران، اگر اول لینک ساب را اضافه کنید، ممکن است بعداً Resourceها درست آپدیت نشوند یا اپ رفتار عجیب نشان بدهد.
━━━━━━━━━━━━━━
2️⃣
تنظیمات Network
از بخش Network این موارد را بررسی کنید:
✅
گزینه‌ی DNS Hijack را فعال کنید.
❌
گزینه‌ی
Allow applications to bypass VPN
را غیرفعال کنید.
این کار کمک می‌کند برنامه‌ها ترافیک یا DNS را از بیرون VPN رد نکنند.
━━━━━━━━━━━━━━
3️⃣
تنظیمات دسترسی و اجرای پس‌زمینه
بعد از نصب وارد این مسیر شوید:
Tools → Advanced Configuration → On Demand
در این بخش، گزینه‌های مربوط به دسترسی‌ها را روی Authorized قرار دهید.
همچنین در تنظیمات باتری گوشی، برای FlClash حالت Battery Optimization را غیرفعال کنید تا اندروید برنامه را در پس‌زمینه نبندد.
━━━━━━━━━━━━━━
4️⃣
گوشی روی Power Saving نباشد
اگر گوشی روی حالت
Power Saving / Battery
Saver باشد، ممکن است اتصال ناپایدار شود یا برنامه در پس‌زمینه قطع شود.
برای استفاده بهتر از FlClash، هنگام اتصال، حالت Power Saving را خاموش کنید.
━━━━━━━━━━━━━━
5️⃣
تنظیمات DNS
از بخش DNS:
✅
گزینه‌ی Override DNS را فعال کنید.
🌍
گزینه‌ی GeoIP Code را روی IR قرار دهید.
بعد از این تغییرات، لینک ساب را اضافه کنید و تست پینگ بگیرید.
━━━━━━━━━━━━━━
6️⃣
اگر ساب آپدیت نمی‌شود، حذف و دوباره اضافه کنید
طبق تجربه‌ی بعضی کاربران، FlClash گاهی نشان می‌دهد که ساب آپدیت شده، اما در عمل لیست کانفیگ‌ها تغییر نکرده است.
اگر حس کردید ساب درست آپدیت نشده:
1. لینک ساب را حذف کنید.
2. دوباره همان لینک را اضافه کنید.
3. مجدد پینگ بگیرید و تست اتصال انجام دهید.
━━━━━━━━━━━━━━
7️⃣
در تب Auto کمی صبر کنید
طبق تجربه‌ی کاربر، بعد از حذف و اضافه کردن دوباره‌ی ساب و گرفتن پینگ در تب Auto، ممکن است اول فقط چند سرور پینگ بدهند و بقیه Timeout شوند.
اما بعد از اولین اتصال، FlClash ممکن است خودش شروع کند سرورها را دوباره بررسی کند و از بالای لیست Auto دونه‌دونه سرورها را تست کند تا به گزینه‌ی بهتر برسد.
یعنی ممکن است اول یک سرور اصلاً پینگ ندهد یا در لیست بالا نباشد، اما بعد از اولین اتصال، همان سرور یا سرورهای دیگر دوباره تست شوند و وصل شوند.
⏳
گاهی این روند کمی زمان می‌برد، پس اگر همان لحظه همه‌چیز Timeout بود، چند دقیقه صبر کنید و دوباره وضعیت را بررسی کنید.
━━━━━━━━━━━━━━
8️⃣
مرتب‌سازی سرورها بر اساس پینگ
برای اینکه سرورهایی که پینگ گرفته‌اند بالای لیست بیایند، روی سه‌نقطه بزنید و وارد این مسیر شوید:
⋮ → Settings → Sort → Delay
با این کار، سرورهایی که پینگ بهتری دارند بالاتر نمایش داده می‌شوند و انتخاب سرور راحت‌تر می‌شود.
━━━━━━━━━━━━━━
✅
ترتیب پیشنهادی بعد از نصب FlClash
1. نصب FlClash
2. آپدیت Resourceها از بخش Tools → Resource
3. فعال کردن DNS Hijack
4. غیرفعال کردن Allow applications to bypass VPN
5. فعال کردن Override DNS
6. تنظیم GeoIP Code روی IR
7. غیرفعال کردن Battery Optimization برای FlClash
8. خاموش بودن Power Saving گوشی
9. اضافه کردن لینک ساب
10. رفتن به تب Auto و گرفتن پینگ
11. تنظیم Sort روی Delay
12. اتصال و چند دقیقه صبر برای تست خودکار سرورها
━━━━━━━━━━━━━━
⚠️
این تنظیمات تضمینی نیست، چون شرایط اینترنت، اپراتور و گوشی‌ها متفاوت است؛ اما برای بعضی کاربران باعث اتصال بهتر و پایدارتر شده است.
🔗
لینک ساب WhiteDNS برای FlClash:
https://sub.whitedns.one/sub/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://sub.whitedns.one/sub/base64.txt
📱
یا دسترسی ساب از گیتهاب
لینک ساب برای  Clash Party & Mi Clash & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/MatinSenPaii/3701" target="_blank">📅 20:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3700">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">😊
آموزش استفاده از Clash Party نسخه ویندوز در کانال یوتیوب WhiteDNS
🔥
کانال مارو Subscribe داشته باشید.
https://youtu.be/gMFH88yRghg</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/MatinSenPaii/3700" target="_blank">📅 20:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3699">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">این هم آموزش‌های مربوطه. از لینک ساب گیتهاب استفاده کنید</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/MatinSenPaii/3699" target="_blank">📅 20:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3698">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-poll">
<h4>📊 چرا نتونستید وصل بشید؟</h4>
<ul>
<li>✓ بلد نشدم وارد کنم</li>
<li>✓ لینک ساب رو زدم آپدیت نشد</li>
<li>✓ لینک ساب رو ژدم آپدیت هم شد، وصل نشد</li>
<li>✓ الکی دیسلایک زدم اصلا وارد نکردم</li>
</ul>
</div>
<div class="tg-text">تونستید به ساب جدید WhiteDNS وصل بشید؟</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/MatinSenPaii/3698" target="_blank">📅 20:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3696">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔥
لینک ساب جدید
https://sub.iampedi2.live/sub/mihomo.yaml
📱
یا دسترسی ساب از گیتهاب
لینک ساب برای  Clash Party & Mi Clash & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/MatinSenPaii/3696" target="_blank">📅 19:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3695">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">به یاد محمد جواد حضوری.npvt</div>
  <div class="tg-doc-extra">3.4 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3695" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">💔
این کانفیگ رو به یاد محمدجواد حضوری عزیز که هم محلی من بود و دیگه پیش ما نیست میزارم تا یادش تا ابد در ذهن من و شما خواهد ماند...
به یادتیم پسر
💔
💔
💔
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/MatinSenPaii/3695" target="_blank">📅 13:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3694">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">😭
الان که همه‌چی فیلتر و بسته‌ست و فیلترنت داریم، یه مشکل کلاسیک ویندوز همه‌مونو کلافه کرده!</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/MatinSenPaii/3694" target="_blank">📅 12:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3693">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ob8RbwXyFpLBwDY2vWh_KUIEYDp_7PUXnwm5OFlYMbS2adWHYWhybhV0d55IoB58Z7oHr6pfybu8EZtoYRzIVhy5s8yBiOX_YJB2WrtLMPXC86Gm-EWvf3Dy-xdobhajMVHurNCfm9DqObpRPJWyjcI_iIH-SLzBHMNYjwu6Uoi8cNqvwKa093-6nHFsfEg9iqFEVm2gDO7MXvMYwU9WBuDOzYsHoUoii1vPIE8RC9_rTd08le3yAp3_YpEguST3opkRWSbk3O7AcNNylbSc6MZ29sipk0UtZOSuaW4JK7TxFKzqeJylNNnh-hSJ58Mp0_Z3d152JRU8E1C8xAue7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیدونم چی باعث میشه یه سری دوستان ادب و نزاکت یادشون بره، ولی خب برای بقیه میگم. فکر کنم دو سه باری هم گفتم قبلا که برای مشکل سرعت آپلود متدهای پشت سی دی ان چه شخصی چه BPB و Edge:
1- فعالسازی Fragment (اون F بالای صفحه توی اپ MahsaNG با تنظیمات auto)
2- بردن کانفیگ پشت SNI-SPOOF</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/MatinSenPaii/3693" target="_blank">📅 09:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3692">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2725e3a8.mp4?token=WVZZ8R3rnyb_N_F3XO0ymVmMaMv_k5310UxSk2Uben5gPuyMujYILopMd_U99sxl9SmXAHj1GKDIA7v244fCZiHbHMGKh81VgdoL8m10VdkFcLrYeJId30ahYd9yOqsuJtk8YDU9-phhMu2P4yhb4ceLYXB6JAHQrOu4fbSJoLl97HImPybS_l9KAK-j0bbG5rtuu8sap-QRAqjTjiB7npVl_DGZlH5_8oMQn7KUrcneT8jyoDfDqwLdtjZx3Z0CkmnU96Qwkxrrj5WdoZRvXEv2085Jv2Y5je4Oi18IO2lNA6FS6dC0FezjrjOt4_BTE7JQC_4kqpSIzOuSfQzWKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2725e3a8.mp4?token=WVZZ8R3rnyb_N_F3XO0ymVmMaMv_k5310UxSk2Uben5gPuyMujYILopMd_U99sxl9SmXAHj1GKDIA7v244fCZiHbHMGKh81VgdoL8m10VdkFcLrYeJId30ahYd9yOqsuJtk8YDU9-phhMu2P4yhb4ceLYXB6JAHQrOu4fbSJoLl97HImPybS_l9KAK-j0bbG5rtuu8sap-QRAqjTjiB7npVl_DGZlH5_8oMQn7KUrcneT8jyoDfDqwLdtjZx3Z0CkmnU96Qwkxrrj5WdoZRvXEv2085Jv2Y5je4Oi18IO2lNA6FS6dC0FezjrjOt4_BTE7JQC_4kqpSIzOuSfQzWKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کمتر از یکساعت پیش مدل جدید تصویر ساز Reve 2.0 معرفی شد , این مدل با پیشی گرفتن از نانو بنانای دو، رتبه دوم رو در جدول مدل های تصویر ساز بعد از GPT بدست آورده
از سایت
Reve.com
‎ می‌تونید به صورت محدود و رایگان تستش کنید.
یادداشت تیم: «ما روشی نوین برای تولید و ویرایش هر نوع تصویر با استفاده از چیدمان‌های دقیق ابداع کرده‌ایم. برای نخستین بار، خلق تصاویری که گویی می‌توان آن‌ها را لمس کرد، امکان‌پذیر شده است.»
✍️
سگارو</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/MatinSenPaii/3692" target="_blank">📅 05:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3691">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">واقعا متوجه نمیشدم چرا مردم پول vpn میدن</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/MatinSenPaii/3691" target="_blank">📅 05:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3690">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">توی 12 دقیقه، با گوشی یا کامپیوترت بدون هیچ دانش فنی‌ای برای خودت سرور VLESS اختصاصی بساز!
🔥
توی این ویدئو، بهتون یاد دادم که چطوری از طریق وبسایت کلودفلر، پروژه BPB و پروژه BPB-ReCoder محدودیت‌های قبلی کلودفلر رو به راحتی دور بزنین و برای خودتون سابسکریپشن…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/MatinSenPaii/3690" target="_blank">📅 05:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3689">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">از کامپیوتر فقط دکمه خاموش روشن کردنش رو بلدی؟ نگران نباش! من بهتون یاد میدم که چطور با دانش فنی بسیار پایین، بتونید برای خودتون و خانوادتون، بدون یک ریال هزینه، VPN بسازید!
🔥
هم برای IOS، هم برای اندروید، و هم برای دسکتاپ و مک  ربع ساعت وقت بذارید این ویدئو…</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/MatinSenPaii/3689" target="_blank">📅 05:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3688">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">یکی از دوستان این روش رو رفته بود برای مشکل اسکنر و برطرف شده بود این اشکال واسش:
متین جان برای مشکل
https://t.me/MatinSenPaii/3652
از این کد استفاده کنن دوستان
pkg install wget -y && pkg install unzip -y && wget https://uploadkon.ir/uploads/c86602_26senpaiscanner.zip && unzip c86602_26senpaiscanner.zip && cp senpaiscanner /data/data/com.termux/files/usr/bin/ && chmod +x /data/data/com.termux/files/usr/bin/senpaiscanner
بعد از اتمام کار
کافیه برای اجرا
senpaiscanner
رو بنویسن و اینتر بزنن
(توی نسخه ۵ اسکنرت)</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/MatinSenPaii/3688" target="_blank">📅 23:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3687">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">به مناسبت ۲۰ هزارتایی شدن، یوتوب هم ۱۲۰۰ دلار از کل درآمد این چند ماهم(که موفق نشده بودم بگیرمش سر مشکل ادسنس) رو خورد و با ادسنس چینج، کلا پروند همه‌اش رو
😂
عاشق این آمریکاییام</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/MatinSenPaii/3687" target="_blank">📅 22:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3686">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">به مناسبت ۲۰ هزارتایی شدن، یوتوب هم ۱۲۰۰ دلار از کل درآمد این چند ماهم(که موفق نشده بودم بگیرمش سر مشکل ادسنس) رو خورد و با ادسنس چینج، کلا پروند همه‌اش رو
😂
عاشق این آمریکاییام</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/MatinSenPaii/3686" target="_blank">📅 22:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3685">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bsp-Kxv1EueOHe2RTsLmRz2OKmidfWgsK7amSgNYnTxi8OOHzGNWkZmrsnZqvNCeOc9GsLFsHlFa9fnht_yqL-K5QAGLDFS2SD8a0chP_tk4O8-UWlu9Prg2xki4usFiH35hd6sjMF8MyK67aeZ-jbpZYGkdHj0p8RfAlrleLx2H0GJVXpjGE9hWw8nyNf1zYgLGmQXAbFBxsyAjbOSPXlBVOGb1D9eB2sDjwmPu0lbBg0Qj1BBYDc6FDRZKgoV_RkbMmiQAIfd1Lv4CVFYD2E3d7xhrAi9_vg9pPz0sYG_SXR2ZLhlyjU0aQDXgGBRzvcZlv89-m3xzYp-qCZGrPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عدده هیچوقت مهم نبوده و نیست. اما مناسبتیه که به خودم یادآوری کنم اهدافم رو. از 2021 که با یه گوشی و ذوق مسیرم رو عوض کردم و اومدم سراغ یوتوب، هدف والا و بلندمدت من، گذاشتن یه تأثیر مثبت روی جوونا و نوجوونای خوب وطنم بوده. کسایی که ارزشش رو دارن، عقاید و شخصیت درستی دارن، انسانیت سرمشق‌ـشونه و شرافتمندانه زندگی می‌کنن.
شاید یه جرقه‌ی امید توی این تاریکی.
شاید جلوگیری از خودکشی چندتا از برادرا و خواهرام.
شاید ایجاد شغل و ایده دادن و کمک بهشون.
توی این خراب شده، ما فقط همدیگه رو داریم.
ممنونم از تینا، پارتنر عزیزم. کسی بود که من رو از تاریکی بیرون کشید، و بهم امید زندگی داد.
پنج سال گذشت، و از مسیری که رفتم پشیمون نیستم.</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/MatinSenPaii/3685" target="_blank">📅 22:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3684">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">شما یه اپلیکیشن می‌بینید، یه لینک ساب می‌بینید، من ساعت‌ها و روزها زحمت و هزاران دلار هزینه از جیب شخصی بدون چشم‌داشت و تلاش شبانه‌روزی می‌بینم. هم از بچه‌های وایت‌دی‌ان‌اس، هم از بقیه‌ی دوستامون که برای اینترنت آزاد تلاش می‌کنن
✌️</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/MatinSenPaii/3684" target="_blank">📅 21:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3683">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">لینک ساب ها درست شدند
😃
🔗
لینک ساب WhiteDNS برای FlClash:
https://sub.whitedns.one/sub/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://sub.whitedns.one/sub/base64.txt
📱
یا دسترسی ساب از گیتهاب
لینک ساب برای  Clash Party & Mi Clash & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/MatinSenPaii/3683" target="_blank">📅 20:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3682">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3682" target="_blank">📅 19:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3681">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">الان که بهش نگاه می‌کنم، از دی‌ماه تا الان نزدیک ده سال گذشت...</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/MatinSenPaii/3681" target="_blank">📅 15:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3680">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d94HQAGom9kvI2pxELcRvzklAUHyXLpfOfP_SN_AlqRn8pn0At54W4mr_mh4aQtmhwjS-TTwvPUl57ME8f5CKJcuyB0gSuRt04mr54uJ9KqThVZ-WAlLfL488_7Zky-YMyBoxVrGcnyChNqe16MUGgXvUyXI9e2JGjJw_mZIVh8rgTppCODVnTA0kvZVWMOrApb-A3P9WqWxAlEBc5u2rxCj1MYs70rwDv1fN6L-qdt0QrmWUtO-zv3lFeEi67m1qcN7QlkGr9amB6_wFwEEsBhPzJK3-XmJ2iimHGXpR2SxhTm9Jlw1NPj6VAkXVuCTDYs_4wmBu_vJ1AcB5oKFdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمام آموزش‌های مبنی بر اینترنت آزاد که من توی کانال یوتوبم منتشر کردم به علاوه‌ی توضیحات و اینکه توی چه شرایطی به چه دردی می‌خورن. از بالا به پایین، برای شرایط سخت‌تر معرفی می‌شن تا شرایط خاموشی کامل:
1- متد Paqet، ویژه‌ی شرایط الآن(کلودفلر و اینترنت بین‌الملل باز شده) واسه‌ی هر نتی(تبدیل سرعت اینترنت داغون به سرعت خدا)
مزایا: سرعت بالا و راه‌اندازی یک باره(هم مستقیم هم تانل)
معایب: نیاز به سرور داره، روش مستقیمش فقط روی سیستم میتونه ران بشه یا گوشی Root شده و تانلش مصرف داده‌اش ۴-۵ برابره
ویدئوی اول آموزش Paqet مستقیم:
https://youtu.be/q4BbgdhPm-w
ویدئوی دوم آموزش Paqet تانل:
https://youtu.be/nwpLOANv7VY
ویدئوی سوم آموزش Paqet با نصب آسان(اسکریپت سم):
https://youtu.be/QkGI8WoOtPc
2- متدهای بر پایه کلودفلر Workers، ویژه‌ی شرایط الآن(کلودفلر و اینترنت بین‌الملل باز شده) واسه‌ی اکثر اینترنتا به علاوه‌ی آیپی تمیز
مزایا: سرعت بالا و راه‌اندازی یک باره، نامحدود بودن(هر اکانت روزانه 6 گیگابایت حدودا(هر شب ریست میشه) و می‌تونید اکانت‌های زیادی بسازید. من خودم نزدیک به ۱۰۰ تا ساختم)
معایب: فقط وب سوکت میشه ساخت و ممکنه برای گیم و... مناسب نباشه اما برای اینستاگرام و یوتوب و اینها خارق‌العادست.
سری اول کلودفلر، پنل BPB:
آموزش اول: ساخت فیلترشکن بر پایه پروژه BPB و اسکن آیپی تمیز با سیستم:
https://youtu.be/_aXy8wwyRG8
آموزش دوم: تنظیمات پنل BPB از سیر تا پیاز:
https://youtu.be/7G9Fjhe_NxM
سری دوم کلودفلر، آموزش پنل Edge:
آموزش اول، ساخت پنل Edge با سیستم به علاوه تمام تنظیماتش و ثابت کردن لوکیشن:
https://youtu.be/svYBcv4bSzo
آموزش دوم، ساخت پنل Edge فقط با یک گوشی موبایل و نصب ترموکس و اسکنر برای پیدا کردن آیپی تمیز:
https://youtu.be/2otJfXgNWCM
3- آموزش کامل خرید سرور و دامنه و نصب کاندوئیت بر روی سرور ویژه ایرانی‌های خارج از کشور که می‌خوان کمک کنن به اتصال از طریق سایفون:
https://youtu.be/DtZyWXWV4BA
4- متد SNI-SPOOFING که در صورتی که یه روزنه‌ی کوچیک باز بمونه، می‌تونید باهاش با نهایت سرعت حتی توی بدترین قطعی‌ها هم وصل بمونید.
مزایا: بدون محدودیت سرعت، می‌تونید کاملا رایگان وصل بشید(با کانفیگ‌های کلودفلر متد شماره 2)
معایب: نیاز به باز بودن اون روزنه داره، و فقط روی سیستم قابل اجراست مثل Paqet. اما قابل اشتراک‌گذاری به دیگر دستگاه‌هاست.
آموزش اول: راه‌اندازی SNI-SPOOFING و استفاده ازش روی ویندوز:
https://youtu.be/dujMBt4sCpw
آموزش دوم: رفع مشکلات و ترکیب لوکیشن متد هر کانفیگی از SNI-SPOOFING روی آمریکا:
https://youtu.be/PuYwXH4D4tU
5- متدهای بر پایه‌ی گوگل. این متدها مادامی که گوگل وصل باشن، کار می‌کنن و طیف وسیعی از متدها رو هم در بر می‌گیرن:
الف- متد MHR و زیرمجموعه‌هاش: این متد محدودیت ۲۰ هزار ریکوئست روزانه روی هر جیمیل داره و سرعت آنچنان بالایی نداره اما با تعداد ایمیل‌های بالا، میشه بهترش کرد.
آموزش اول، متد MHR خام(توصیه میشه بعدیا رو راه بندازید نه این. چون با آیپی خودتون باید برید و هوش مصنوعیا رو نمیاره واستون):
https://youtu.be/jzaqdKl40Ww
آموزش MHR-CFW(ترکیب همین، با کلودفلر برای داشتن آیپی خارج):
https://youtu.be/L3lJZrAqqUQ
آموزش راه‌اندازی MHRv-RUST با گوشی موبایل:
https://youtu.be/7YdJIJloIxY
ب- متد MITM برای دسترسی به سرویس‌های بسته شده‌ی گوگل(چون از روش یک حمله‌ی سایبری استفاده میشه روی تلگرام آپلود شده فقط):
آموزش اول دسترسی به سرویس‌های گوگل و گیتهاب:
https://t.me/MatinSenPaii/3151
آموزش دوم دانلود نامحدود از یوتوب با نت ملی بر پایه‌ی آموزش اول:
https://t.me/MatinSenPaii/3230
ج- متد Skirk بر پایه‌ی گوگل درایو که مزایاش، سرعت دانلود بالا و معایبش، Latency بالا هست؛ از کانال عزیزی:
https://youtu.be/vCr4E6Y1k4c
6- متدهای بر پایه‌ی DNS، که از روز اول جنگ وصل بودن تا آخر قطعی. اما ما اواخر قطعی بود که به بهترین ترکیبش رسیدیم. پروژه‌ی MasterDNS و کلاینت WhiteDNS. مزایا: وصل توی هر شرایطی، قابلیت اجرا روی هر پلتفرم و سیستم عاملی، حتی روی سرور، و اضطراری‌ترین راه چاره‌ی ما
معایب: مصرف حدود دو برابری اینترنت(که به نظر خودم می‌ارزه توی اون شرایط) به علت کوئری‌های DNS فراوان. همینطور نیاز به سرور داره اما از سرورهای رایگان هم می‌تونید استفاده کنید(طبیعتا سرعت خیلی پایینتر)
آموزش کامل راه‌اندازی روی گوشی و سیستم:
https://youtu.be/6Pm7kNQb3mo</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/MatinSenPaii/3680" target="_blank">📅 14:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3679">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">امروز واستون دسته بندی می‌کنم یه کم راهکارهایی که تا الان دادمو</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/MatinSenPaii/3679" target="_blank">📅 08:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3677">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UQs_OpoXwTc9vxV8A3FrFL4j3AHFf1sP078blHZJximacqmhuSFTNgEZPlFDz7wfqqlq8S2uBlYeN3Z3KltdKqs1eezKr107i0EwYAUh4-Ek_Wh5crXl8lAEbTsyUBQdnxecpfUgVz5kpPLh_91c6gKXe8wJoBZEqxCK9gmjuN3dY_UspsjcGBXix06hycShPxt79kZ1j_FP8NYQxfOtXjiWFtAn3o3pELlkGggOiMkFEUaaGTkg-xCzwwrr-L-OZ8zJH4Y1U8Jc1ykHFXJqXrpDZ-o6hmwZ5DAFFuYxNkIVLDFwxzgjOGvL-f1lfx2JTVM5HkmtU1bQA8CEHlbl5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/215e27ea42.mp4?token=slSuEHY5bQIXBhZKJUJ1fImyHc_fpe7LOJhdI6DhYVFipE9LaPTNf76JaqKESMHaiJAGOCPKWdLFuTbUP_wNU1kTQpNCyKIc_Xcvjg-UDkJGvmru_fhQ76jz-hcRTBW2FrWDcL25rhAcQfhk034ayz1WbqtV_-GqiaZdR6lkZzpYV7_p5ltvr7q3Oz9WN3YKQL2EL5srvWlf4UIzBV1YKqvDq7fKqKdShfaNF9J-A2GzannRcDbYMjK3Z0g5BmKidgk56nc748OH4KI8WZbohXApEWSc34qct165CsaPF5GwnMKFXB4uc_ZhOLEj-dVkA6tVtU-SR8rFbQxMJjUiCw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/215e27ea42.mp4?token=slSuEHY5bQIXBhZKJUJ1fImyHc_fpe7LOJhdI6DhYVFipE9LaPTNf76JaqKESMHaiJAGOCPKWdLFuTbUP_wNU1kTQpNCyKIc_Xcvjg-UDkJGvmru_fhQ76jz-hcRTBW2FrWDcL25rhAcQfhk034ayz1WbqtV_-GqiaZdR6lkZzpYV7_p5ltvr7q3Oz9WN3YKQL2EL5srvWlf4UIzBV1YKqvDq7fKqKdShfaNF9J-A2GzannRcDbYMjK3Z0g5BmKidgk56nc748OH4KI8WZbohXApEWSc34qct165CsaPF5GwnMKFXB4uc_ZhOLEj-dVkA6tVtU-SR8rFbQxMJjUiCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Operator: Asiatech/Datacenter Time: 2026-06-02 22:22:04  The status of this service has changed to:
❌
DNS google.com via 8.8.8.8 : timeout</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/MatinSenPaii/3677" target="_blank">📅 04:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3676">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">هیچی.
موشک زده شد؛
اونا هم گفتن دفع کردیم.
ما مردم بدبخت هم چیزای عادی‌تر دیگه‌ای از سبد خریدمون حذف میشه فردا و پس‌فردا و روز بعدش</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/MatinSenPaii/3676" target="_blank">📅 03:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3675">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=UI0y9hS07T7Y9xZ3ZACAcRVKgtPMz4b98Z7LWPLzgaPwma8FNlw65H8aKqPjvaUxTXQj2XYpjJ3uT4124o4MgOQkJVSIa2zaPQThs5BxIX8cVBvIC-ia3aSwvaLwhd0oEVwE8OpLusTX9GenXZl9b2MnSE_DG9COfp1JixNFBPJ5Uuo11VEWvTHXkX26Pb9yzGEGT2kzoLUhymTghDjKYuVEsypSrw_oBSDgKJ9362h07qWsevvD6VebJk7Jg1nUNeVjK2uTYfJPS0yDf-IjTcZhx7D3kriiRkZeHAEIXNiHRRZ_H6LuBgH0ICJYuV3OUDlOXrFaIFDpzzqbxqPWaKPISpxbsFmnlKsoZzgXfkB8zxZhXgWyxJLgxDApaSzn0EijcSwRvC113pj9zQ6FrcP-nsPmQvO7Ed4fwItOpgK7wdftFAAS6RKFP6NqIhxPzXKfKAbP-TsLvux0yldfMvFJgtAOzfg3EF_HLYwj0Klb6ExRzbyWJdia5HHA11zo9vEwNf1mghXaQSMNoGg7aW7kh1XbKEcHGi-bt50OKV5tEw3Oaa1va3rT9sNovoWQeCRYq3yAlFcUBO8rsnofbbhZg4KozpoABJOSo5rMWSv8vAX7FMZHJaxnVnlBwh0yM_dIGhievKsuUSYgmOIRWYc3lyoRAVYLMJtq_wtVy-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=UI0y9hS07T7Y9xZ3ZACAcRVKgtPMz4b98Z7LWPLzgaPwma8FNlw65H8aKqPjvaUxTXQj2XYpjJ3uT4124o4MgOQkJVSIa2zaPQThs5BxIX8cVBvIC-ia3aSwvaLwhd0oEVwE8OpLusTX9GenXZl9b2MnSE_DG9COfp1JixNFBPJ5Uuo11VEWvTHXkX26Pb9yzGEGT2kzoLUhymTghDjKYuVEsypSrw_oBSDgKJ9362h07qWsevvD6VebJk7Jg1nUNeVjK2uTYfJPS0yDf-IjTcZhx7D3kriiRkZeHAEIXNiHRRZ_H6LuBgH0ICJYuV3OUDlOXrFaIFDpzzqbxqPWaKPISpxbsFmnlKsoZzgXfkB8zxZhXgWyxJLgxDApaSzn0EijcSwRvC113pj9zQ6FrcP-nsPmQvO7Ed4fwItOpgK7wdftFAAS6RKFP6NqIhxPzXKfKAbP-TsLvux0yldfMvFJgtAOzfg3EF_HLYwj0Klb6ExRzbyWJdia5HHA11zo9vEwNf1mghXaQSMNoGg7aW7kh1XbKEcHGi-bt50OKV5tEw3Oaa1va3rT9sNovoWQeCRYq3yAlFcUBO8rsnofbbhZg4KozpoABJOSo5rMWSv8vAX7FMZHJaxnVnlBwh0yM_dIGhievKsuUSYgmOIRWYc3lyoRAVYLMJtq_wtVy-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
آموزش کامل TheFeed از صفر تا صد
اگر تازه با TheFeed آشنا شدید و نمی‌دانید از کجا باید شروع کنید، این ویدیو دقیقاً برای شماست.
👇
در این آموزش یاد می‌گیرید:
✅
اضافه کردن کانفیگ
✅
آشنایی با ریزالورها (DNS)
✅
پیدا کردن ریزالورهای سالم
✅
مشاهده کانال‌ها و دریافت محتوا
✅
آشنایی با بخش TeleMirror
✅
رفع مشکلات رایج کاربران
✅
نکات مهم برای استفاده بهتر از برنامه
دفید یک سیستم مبتنی بر DNS است که امکان دسترسی به محتوای کانال‌های تلگرام را حتی در شرایط محدودیت اینترنت فراهم می‌کند.
📢
کانال اصلی پروژه:
@networkti
📦
فایل‌های نصب:
@thefeedfile
⚙️
کانفیگ‌های عمومی:
@thefeedconfig
توضیحات متنی
👇
سلام. توی این ویدیو می‌خوام خیلی ساده و سریع نحوه کار با برنامه The Feed رو توضیح بدم.
بعد از نصب و باز کردن برنامه، اولین کاری که باید انجام بدید اضافه کردن یک کانفیگه. برای این کار از بالا روی علامت جمع بزنید و کانفیگ مورد نظرتون رو وارد کنید. کانفیگ‌های عمومی داخل کانال
@thefeedconfig
منتشر میشن و می‌تونید از اونجا دریافتشون کنید.
هر کانفیگ دارای تعدادی ریزالور پیش فرض هست که توسط سازنده کانفیگ داخل کانفیگ قرار میگیرن. بعد از اینکه کانفیگ رو اضافه کردید، برنامه شروع می‌کنه به بررسی ریزالورها. ریزالورها همون DNS هایی هستن که The Feed از طریق اون‌ها اطلاعات رو دریافت می‌کنه. این مرحله ممکنه چند دقیقه طول بکشه، پس اگر بلافاصله کانال‌ها نمایش داده نشدن نگران نباشید. بعد از پیدا شدن ریزالورهای سالم، لیست کانال‌ها دریافت میشه و می‌تونید وارد هر کانال بشید، پست‌ها رو ببینید و در صورت وجود، عکس‌ها، فایل‌ها، ویس‌ها و ویدیوها رو دانلود کنید.
اگر یه زمانی دیدید برنامه کند شده یا اطلاعات جدید دریافت نمی‌کنه، معمولاً مشکل از ریزالورهاست. برای همین داخل برنامه بخشی به اسم «پیدا کردن ریزالور» وجود داره. وارد این قسمت بشید و روی «بارگذاری لیست پیش‌فرض» بزنید. با این کار حدود ۵۸ هزار ریزالور برای اسکن آماده میشن.
اگه خودتون ریزالور خاصی دارید، می‌تونید به صورت دستی هم واردش کنید. علاوه بر این، ربات
@dns_resolvers_bot
هم می‌تونه برای پیدا کردن ریزالورهای جدید بهتون کمک کنه.
بعد دکمه «شروع اسکن» رو بزنید تا برنامه ریزالورهای سالمی که روی اینترنت شما کار می‌کنن رو پیدا کنه. وقتی چند تا ریزالور پیدا شد، می‌تونید اون‌ها رو به لیست فعال اضافه کنید. فقط یادتون باشه موقع اسکن بهتره VPN خاموش باشه تا نتیجه دقیق‌تری بگیرید.
داخل برنامه یه بخش دیگه هم به اسم Tele Mirror وجود داره. این قسمت با سیستم اصلی TheFeed فرق داره و برای نمایش کانال‌های عمومی تلگرام از سرویس‌های گوگل استفاده می‌کنه. با TeleMirror می‌تونید خیلی از کانال‌های عمومی دلخواهتون رو دنبال کنید، ولی محدودیت‌هایی هم داره؛ مثلاً امکان دانلود فایل یا پخش ویدیو توی این بخش وجود نداره. همچنین اگر سرویس‌های گوگل در دسترس نباشن، ممکنه Tele Mirror کار نکنه. البته این موضوع روی بخش اصلی TheFeed تأثیری نداره و سیستم اصلی برنامه همچنان از طریق DNS به کار خودش ادامه میده.
در نهایت اگر جایی به مشکل خوردید، اولین چیزی که باید بررسی کنید ریزالورها هستن. در اکثر مواقع با پیدا کردن چند ریزالور سالم، مشکل برنامه برطرف میشه. برای دریافت آخرین اخبار پروژه هم می‌تونید کانال
@networkti
رو دنبال کنید، فایل‌های نصب رو از
@thefeedfile
بگیرید و کانفیگ‌های عمومی رو از
@thefeedconfig
دریافت کنید.
ممنون که این ویدیو رو دیدید و امیدوارم از The Feed لذت ببرید.</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/MatinSenPaii/3675" target="_blank">📅 02:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3674">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">من الان خودم با WhiteDNS آنلاینم(داشتم تست میکردم دامین اینها نپریده باشه)
خواهش میکنم ستاپ کنید هر چه سریعتر. هرچی نیاز دارید توی ویدیو هست
https://youtu.be/6Pm7kNQb3mo?is=Hh_zNDNmPQGHgzLb</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/MatinSenPaii/3674" target="_blank">📅 01:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3673">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=njKdAjcmi3-p2v261Ftly-zQ5TRUHrGOykTWwlisy6O-DHWXZtQXfVzNYXBdZUzL_jfHcctW0_dLM6dXXgC4DPmU967PE6IEPejbG6pHsgAWqZkAZm0ffNM6Y6NZphOEniOvewKF76Gm_RjfdX0y2yEq4V-ydzACeUt3L90KlGVYkCSyq7Vh80d79tdcLBtGW4Uyme8-hndwSR2TZsS9oB29k1h6u-zOiIUZSiGCwrlRpKPy1U82PpxBScusuk0OCECDfz7cqVb8L3ePDJqkLRvChnVJpAU8SAhu7PyKYkrYrIPt3NQAc_NtY11S6erqVOFz9EpCx1HHPgaqwk8EBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=njKdAjcmi3-p2v261Ftly-zQ5TRUHrGOykTWwlisy6O-DHWXZtQXfVzNYXBdZUzL_jfHcctW0_dLM6dXXgC4DPmU967PE6IEPejbG6pHsgAWqZkAZm0ffNM6Y6NZphOEniOvewKF76Gm_RjfdX0y2yEq4V-ydzACeUt3L90KlGVYkCSyq7Vh80d79tdcLBtGW4Uyme8-hndwSR2TZsS9oB29k1h6u-zOiIUZSiGCwrlRpKPy1U82PpxBScusuk0OCECDfz7cqVb8L3ePDJqkLRvChnVJpAU8SAhu7PyKYkrYrIPt3NQAc_NtY11S6erqVOFz9EpCx1HHPgaqwk8EBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/MatinSenPaii/3673" target="_blank">📅 01:34 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

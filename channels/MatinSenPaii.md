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
<img src="https://cdn1.telesco.pe/file/rzfVGsAXhW-vH51YcHLtw_FbRtFtfBh8vSfJFDbALTprWCYmQm3GILAQT5gmeWFn5kazpGqt-zokuuqwriykMi4qZHBxScwPOO-N-xCIuHIBnIXvY9jQVqQgFOd-87dYyLljbHc3TWYf5T9K80Sjmrk-XhJ7EqlvuoLx5g9dc41dazxVKASsjiA287aKYUM210VqU3kzk2A3Wqqzdr8T1sDqkB2wtlvIOXAv3IZHcvsp12VW-NKLYnVhjXT5JIXDfzvl9cGmwcNKVlWsi-9zfUr-2CIjfDe-anB7chzY254Yb99HVo3eU9osAWbq4O9T7O_2dnjIYO8nXgdm0IOApg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 158K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPaiایمیل کاری: matinsp.job@gmail.com</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 23:31:29</div>
<hr>

<div class="tg-post" id="msg-4521">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">شاید هم عاقل شدن
چه میدونم والا</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/MatinSenPaii/4521" target="_blank">📅 22:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4520">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فکر کنم تا اسرائیل حمله نکرده نت رو قطع نمی‌کنن</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/MatinSenPaii/4520" target="_blank">📅 22:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4519">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مرز "یادگیری" و "تنبلی" با LLM ها واقعا یه خط موی باریکه</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/MatinSenPaii/4519" target="_blank">📅 20:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4518">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">خالق لینوکس: هوش مصنوعی یه ابزاره، هرکی دوست نداره جمع کنه بره!
🐧
یه بحث جنجالی توی لیست پستی توسعه‌دهندگان لینوکس بالا گرفته بود سر اینکه آیا باید از هوش مصنوعی (LLMها) برای بررسی کدها و کمک به Maintainerهای لینوکس استفاده بشه یا نه. بعضی‌ها خیلی سفت‌وسخت مخالف بودن و می‌گفتن کلاً نباید پای AI به هسته لینوکس باز بشه.
اما
لینوس توروالدز
(خالق لینوکس) همونطور که از شخصیت رک و بی‌اعصابش انتظار می‌رفت، وارد بحث شده و یه جواب به شدت قاطع داده.
خلاصه‌ی حرف‌های لینوس ایناست:
1-
لینوکس پروژه ضد هوش مصنوعی نیست:
لینوس صراحتاً گفته: "می‌دونم بعضی‌ها از هوش مصنوعی متنفرن، اما لینوکس قرار نیست یکی از اون پروژه‌های ضد AI باشه. اگه کسی با این قضیه مشکل داره، می‌تونه طبق قانونِ اوپن‌سورس پروژه‌مون رو Fork کنه یا کلاً از اینجا بره!"
2-
کسی که میگه AI به درد نمی‌خوره، اصلاً باهاش کار نکرده:
به گفته‌ی لینوس: "AI مثل بقیه ابزارهایی که داریم، صرفاً یه ابزاره. شاید تا یه سال پیش کاربردش واضح نبود، اما الان دیگه شکی توش نیست که مفیده. هرکسی که به مفید بودنش شک داره، کاملاً مشخصه که تا حالا ازش استفاده نکرده."
3-
به جای غر زدن، درستش کنیم:
لینوس قبول داره که هوش مصنوعی گاهی اوقات به خاطر پیدا کردن باگ‌های خجالت‌آور یا تولید کارهای اضافه، می‌تونه برای مدیران پروژه‌ها دردسرساز باشه. اما می‌گه راه‌حلش این نیست که "سرمون رو بکنیم تو برف و بگیم من چیزی نمی‌شنوم". راه‌حل اینه که یاد بگیریم چطور از این ابزارها برای «کمک» به تیم استفاده کنیم، نه اینکه کلاً حذفشون کنیم.
4-
انسان‌ها هم بی‌نقص نیستن:
لینوس یه تیکه‌ی سنگین هم انداخته: "بله، AI بی‌نقص نیست. ولی محض رضای خدا، هرکسی که به مشکلات AI اشاره می‌کنه، بهتره تو آینه به خودش هم نگاه کنه! چون هوش طبیعیِ انسان‌ها هم همیشه اونقدرها عالی و بی‌نقص نیست."
حرف آخر:
در نهایت لینوس آب پاکی رو ریخته رو دست همه و گفته لینوکس یه پروژه‌ی تکنولوژی‌محوره، نه یه کمپین مذهبی یا اجتماعی. ما اوپن‌سورس کار می‌کنیم چون نتیجه‌ش می‌شه تکنولوژی بهتر، و تصمیماتمون رو هم بر اساس ارزش‌های فنی می‌گیریم، نه از روی «ترس از ابزارهای جدید». به قول معروف: پیشرفت منتظر کسی نمی‌مونه!
لینک ایمیل اصلی لینوس توی لور:
https://lore.kernel.org/linux-media/CAHk-=wi4zC+Ze8e+p3tMv8TtG_80KzsZ1syL9anBtmEh5Z40vg@mail.gmail.com/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/MatinSenPaii/4518" target="_blank">📅 18:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4517">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">قبلا چندتا مقاله خونده بودم، اما تا با چشم خودم ندیدم قبولش نکردم.
واقعا AI ها، زبان TypeScript رو خیلی خیلی بهتر از مابقی زبان‌ها می‌فهمن</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/MatinSenPaii/4517" target="_blank">📅 17:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4516">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ماجرای اوپن سورس شدن xAI Grok-Build  داستان یه مقدار خنده‌دار (و یه مقدار دارک) هستش. همونطور که می‌دونید Grok-Build همون ایجنت کدنویسی تحت ترمینال شرکت xAI (مال ایلان ماسک) هست که به‌تازگی توی گیت‌هاب اوپن‌سورس شده؛ اما پشت این اوپن‌سورس شدن یه رسوایی بزرگ…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/4516" target="_blank">📅 16:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4515">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">آیا هوش مصنوعی داره قدرت تفکر رو از ما می‌گیره؟
🏃‍♂
یه مقاله‌ی جالب توی وبلاگ ArtFish منتشر شد، درباره‌ی اینکه چطور داریم کم‌کم «فکر کردن» رو به هوش مصنوعی واگذار می‌کنیم. نویسنده‌ی مقاله خودش توی بخش توسعه‌ی Gemini کار می‌کنه، ولی یه سری دغدغه‌های به‌شدت درست و روانی مطرح کرده که خوندنش خالی از لطف نیست.
خلاصه‌ی بحث و چند تا نکته‌ی جذابی که گفته:
1-
از موتور جستجو تا ماشین فکر:
قبل از چت‌جی‌پی‌تی و جمنای و...، ما برای پیدا کردن جواب می‌رفتیم گوگل می‌کردیم، ولی همون سرچ کردن هم نیاز به «فکر» داشت. باید سوال رو می‌شکستیم، منابع رو می‌خوندیم و خودمون ترکیبشون می‌کردیم تا به جواب برسیم. اما الان هوش مصنوعی تمام این مراحلِ میانی رو حذف کرده و یه جواب شسته‌رفته و آماده می‌ذاره کف دستمون. این کار زمان رو ذخیره می‌کنه، اما «فکر کردن» رو هم حذف می‌کنه
🤔
2-
داستان ترسناک مرد میکروفون‌دار!
نویسنده تعریف می‌کنه که دوستش تو یه رویداد استارتاپی تو سانفرانسیسکو یه نفر رو دیده که یه میکروفون کوچیک به لباسش وصل کرده بوده و کل مکالمات روزمره‌ش رو ضبط می‌کرده. آخر شب هم می‌داده به هوش مصنوعی تا تحلیلش کنه! اون آدم با افتخار می‌گفته: "کلاد از من باهوش‌تره و تفکر انتقادی (Critical Thinking) بهتری داره، پس من کلاً فکر کردنم رو سپردم به اون!"
🎤
3-
مرز بین دستیار و از دست دادن استقلال:
ما همیشه بین «جواب‌های سریع» و «تفکر عمیق» یه معامله می‌کنیم. وقتی برای هر سوال کوچیک و بزرگی (از اینکه "شام چی بخورم؟" تا سوالات فلسفی و تاریخی) سریع گوشی رو درمیاریم و از AI می‌پرسیم، کم‌کم قدرت استدلال، حدس زدن و بحث کردن رو از دست می‌دیم
🗃️
4-
داستان سفر پرتغال:
یه جای قشنگ مقاله می‌گه با خواهرش تو پرتغال بودن و براشون یه سوال تاریخی/فرهنگی پیش میاد. خواهرش سریع می‌گه "بذار از ChatGPT بپرسم". اما نویسنده می‌گه "نه، بیا اول خودمون فکر کنیم." شروع می‌کنن به حدس زدن، تئوری بافتن، مخالفت با هم و استفاده از اطلاعات دبیرستانشون. بعد از کلی بحث، می‌رن از AI می‌پرسن و می‌بینن خیلی از حدس‌هاشون درست بوده. لذتِ اون «مسیر فکری» دقیقاً چیزیه که داریم با هوش مصنوعی از دستش می‌دیم
🗺
5-
اگه من کارای روتین رو بدم به AI، زندگیم بهتر نمی‌شه؟
اینم یه زاویه‌ست. خیلیا می‌گن اگه تسک‌های خسته‌کننده (مثل ترجمه داکیومنت یا خلاصه‌سازی) رو بدیم به AI، وقتمون برای تفکر مهم‌تر و جذاب‌تر آزاد می‌شه. اما مشکل اینجاست که مرز بین «اتوماتیک کردن کار» و «تنبل شدن ذهن» خیلی باریکه. مثل دانش‌آموزایی که حل مسئله‌ی فیزیک رو می‌دن به AI؛ درسته که نمره می‌گیرن، اما در نهایت یاد نمی‌گیرن «چطور» به اون جواب برسن
👍
حرف آخر:
سوال اصلی اینه که ما دقیقاً داریم چیو اتوماتیک می‌کنیم؟ «کارهای انسانی» رو یا «عاملیت (Agency) و تفکر انسانی» رو؟ استفاده از AI عالیه، ولی یادمون نره که بعضی وقتا حدس زدن، اشتباه کردن و با ذهن خودمون به جواب رسیدن، همون چیزیه که ما رو انسان نگه می‌داره
🛡
لینک مقاله‌ی اصلی:
https://www.artfish.ai/p/offloading-thinking-to-ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/4515" target="_blank">📅 14:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4514">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZjgHlEm0K0ddiMvUeV_lchzOCOblhPtCYAWoVQt5B3nvLBApWvXBSkYuoLUAv6s65i-I25aG5TID4H5emKdqexVRHRVvqrw7xTMrxYmHeDfz1l_RfTF6X-f_548U16y124qDJ-kKcQX4NWsQ5FiIny4QUxxuIotghRl0DKexgDjun_7T8bpD-T50MTMfyLyq8Yj-twQTh9qRvqbX_BSeCnRr8c0SBozwIFdkP9vn7NC6RZxPQpOCUMiWSiiMbvqRIlA9WDBCIL19B7Cwolr1ojbQygEv1DaAMN24OX_ad9ZtIRwjG2CmM4TGI0U0VjkokLSV6ZIxywhyYrEKM1C3PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای اوپن سورس شدن xAI Grok-Build
داستان یه مقدار خنده‌دار (و یه مقدار دارک) هستش. همونطور که می‌دونید Grok-Build همون ایجنت کدنویسی تحت ترمینال شرکت xAI (مال ایلان ماسک) هست که به‌تازگی توی گیت‌هاب اوپن‌سورس شده؛ اما پشت این اوپن‌سورس شدن یه رسوایی بزرگ خوابیده بود.
داستان از این قراره:
1- رسوایی سرقت کد (Spyware شدن ابزار): چند وقت پیش، یه سری از محقق‌های امنیتی و دولوپرها نشستن ریکوئست‌های شبکه‌ی Grok-Build رو مانیتور کردن. دیدن این ابزار وقتی روی سیستم کاربر اجرا می‌شه، فقط فایل‌هایی که بهش می‌گی رو نمی‌خونه؛ بلکه داره تو بک‌گراند کل هیستوری گیت، کل فایل‌های پروژه (حتی اونایی که بهش ربطی نداره)، کلیدهای SSH، پسوردها و Credentials رو زیپ می‌کنه و می‌فرسته روی سرورهای xAI!
😂
2- مچ‌گیری و آبروریزی توی توییتر: وقتی این قضیه لو رفت، توییتر منفجر شد. همه شروع کردن به گفتن اینکه xAI داره دیتای خصوصیِ دولوپرها رو واسه Train کردن مدل‌هاش می‌دزده و اسم ابزار رو گذاشتن «جاسوس‌افزار (Spyware)».
3- ماله‌کشیِ سریع xAI: شرکت xAI وقتی دید مچش رو بدجور گرفتن، سریعا یه بیانیه داد و آپلود اتوماتیک دیتا رو قطع کرد. گفتن تمام دیتای قبلی رو پاک می‌کنیم و یه دستور /privacy هم اضافه کردن که کاربر بتونه کنترل کنه چه دیتایی بره به سرورا.
4- تیر آخر (اوپن‌سورس کردن اجباری): برای اینکه اعتماد از دست‌رفته رو برگردونن و بگن «ببینید ما هیچ کدی رو قایم نکردیم و چیزی نمی‌دزدیم»، مجبور شدن کُل پروژه‌ی ۸۰۰ هزار(
😭
😭
😭
) خطی Grok-Build رو (که به زبان Rust نوشته شده) اوپن‌سورس کنن! الان سورس کدش به صورت کامل روی اکانت xai-org تو گیت‌هاب منتشر شده:
https://github.com/xai-org/grok-build
خلاصه:
دلیل خنده‌ی ملت اینه که xAI از قصد نمی‌خواست این ابزار خفن رو اوپن‌سورس کنه، ولی چون دولوپرها مچشون رو سر «دزدی بی‌سروصدای کدها» گرفتن، واسه فرار از رسوایی و اعتمادسازی مجدد، مجبور شدن کل سورسش رو بریزن بیرون!
ولی خب، از هر زاویه‌ای نگاه کنیم، این رسوایی در نهایت به نفع ما دولوپرها تموم شد و الان یه ایجنت کدنویسی لوکال، قدرتمند و اوپن‌سورس داریم که می‌تونیم مستقیما رو سیستم خودمون (بدون فرستادن دیتا به سرورهای اونا) اجراش کنیم.
هرچند فعلا باید خودمون بیلد بگیریم با Rust
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4514" target="_blank">📅 08:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4513">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ماجرا داره این اوپن سورس شدن
که خب به نفع ما مردمه به هر حال
و خنده دار</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/MatinSenPaii/4513" target="_blank">📅 07:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4512">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">انقدر خندیدم که دل درد گرفتم</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/MatinSenPaii/4512" target="_blank">📅 07:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4511">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">https://github.com/xai-org/grok-build</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/MatinSenPaii/4511" target="_blank">📅 07:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4510">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">برگام
گویا Grok-Build به طور کامل اوپن سورس شده
😂</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/MatinSenPaii/4510" target="_blank">📅 07:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4509">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">هک Suno فاش کرد این هوش مصنوعی با دزدیدن میلیون‌ها آهنگ از یوتیوب و دیزر، یاد گرفته موسیقی بسازد.  در یک رسوایی دوگانه، گزارش 404 Media فاش کرد که Suno، سازنده موسیقی با AI، هدف یک «حمله زنجیره تأمین» (نفوذ از طریق تامین‌کنندگان نرم‌افزاری) قرار گرفته است.…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/MatinSenPaii/4509" target="_blank">📅 07:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4508">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bjnwW6yOOgGMF-grKfQ8ThQKTNT9JGUgqFXb-Fk-Tg1kj5dua2_7sIS-Zi9VI2obP5M-KXaJEXt8QCjr4P9sUvHLKYXA5AKvz8PCv2N9VUw_cKaIwy4cmK8Id8QW0X03jAgxnaewctdVZYezp2auUpChFG0KWHFcW_UEUIRVjN3FdpZ0n8AMCj13GYz96qzfDCLzsOYuMG6qEN457rK8zd1Giv155ScACD4kNk8bE-Q6khgtdZ8a9JeDhmLIcoPyTs93dQAtYQaJLjl5ZLSFMmw5XlkD-kb5K1juGM4HtYiOQBwKAwcuAwHjrUw6B1FpxVsyc8_wqa4adVQlPNVCeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هک Suno فاش کرد این هوش مصنوعی با دزدیدن میلیون‌ها آهنگ از یوتیوب و دیزر، یاد گرفته موسیقی بسازد.
در یک رسوایی دوگانه، گزارش 404 Media فاش کرد که Suno، سازنده موسیقی با AI، هدف یک «حمله زنجیره تأمین» (نفوذ از طریق تامین‌کنندگان نرم‌افزاری) قرار گرفته است. هکر با دسترسی به اعتبارنامه‌های یک کارمند، به کد منبع دست یافت که ثابت می‌کند Suno برای آموزش مدل‌های خود، دهه‌ها محتوای صوتی را از یوتیوب موزیک، دیزر و پادکست‌ها «اسکرپ» (استخراج انبوه و غیرقانونی) کرده است.
شرکت Suno پیش‌تر ادعا می‌کرد بر اساس «دکترین استفاده منصفانه» (قانون اجازه استفاده محدود از اثرات دارای کپی‌رایت برای اهداف تحلیلی یا آموزشی) عمل می‌کند، اما شرکت‌های ضبط موسیقی معتقدند دور زدن پروتکل‌های حفاظتی یوتیوب، نقض صریح DMCA (قانون کپی‌رایت دیجیتال) است. این وضعیت مانند آن است که کسی برای یادگیری نقاشی، موزه‌ها را شبانه تخلیه کند و ادعا کند چون آثار «در معرض دید» بوده‌اند، کپی‌برداری از آن‌ها مجاز است. علاوه بر این، داده‌های حساس کاربران از جمله شماره تلفن و بخشی از اطلاعات کارت‌های بانکی در Stripe لو رفته است؛ حادثه‌ای که Suno در نوامبر 2025 رخ داد اما آن را به عنوان یک «حادثه امنیتی محدود» پنهان کرد و کاربران را مطلع نساخت.
منبع:
https://techcrunch.com/2026/07/15/hack-suggests-ai-music-generator-suno-scraped-youtube-for-training-data/
✍️
هوش مصنوعی گراتومیک</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/MatinSenPaii/4508" target="_blank">📅 07:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4507">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">نسخه‌ی اندروید هم دوستم زحمتشو کشید نوشت:
https://github.com/ZethRise/Aethery
البته هنوز باید کاملترش کنه
😀</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/4507" target="_blank">📅 00:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4506">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GpQm6_fjLasMNHt9XVCaGzlNXQLN7CuIV9cc0yLSlBc8YjlfeZxGf9Pz0FB4CK6yGD4ZoOAvPqyHPljKrCIq70v6CIk16NQiQNdgt-E1dRC4PynmrztPmfJ2X5Xv-gw-crT2UB6eYnWnv708Lfapo0WUlDxRM7UL3XtOZdUCs1RIk-WwQIsPynGHNYAcTCDvyp-YBLMtgLU2medayKSGakfE_Z_2ST2urDw7STAdRpXrHVKZ1wraZSECKbDBQ_8zTQB8iP8xKoZaDRomvAKoUGuJz5BUdct6xO6i20R_wUWhzEneOzksRx0s8YxULV-35wGiBF5uPH94jwRB4KVmlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن Aether-GUI آپدیت شد به ورژن 0.3.0
تغییراتی که توی این ورژن دادم:
الف) آپدیت به هسته‌ی 1.1.1 خود Aether که سه تا قابلیت داره:
1- دیگه وقتی می‌نویسه Connected، یعنی واقعا Connected! تونل الان به‌ صورت سرتاسری اعتبارسنجی می‌شه تا مشکلی که توی اون برنامه متصل نشون داده می‌شد اما هیچ ترافیکی جریان نداشت، برطرف بشه.
2- خودترمیمی MASQUE — در صورت قطع شدن تونل یا شکست توی اعتبارسنجی، Aether به‌طور خودکار مجددا اتصال رو برقرار می‌کنه.
3- اتصال مجدد سریع — آخرین تنظیماتی که باهاش تونستید وصل بشید به حافظه سپرده میشه تا سری بعدی خیلی سریعتر وصل بشید.
ب) مشکل ارور setup prompts برطرف شد کامل
ج) مشکل بافر نامحدودی که باعث افزایش تدریجی و مداوم مصرف پردازنده توی حین مسیر اتصال و توی تمام سیستم‌ها می‌شد، برطرف شد. الان مصرف CPU نزدیک به 0 هست.
د) تمامی کتابخونه‌های غیرضروری و سنگین، حذف شدن
از اینجا دانلود کنید:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.3.0</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/4506" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4505">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
آموزش ساخت کانفیگ bepass uoosef
1. از یکی از لینک های زیر پلاگین bepass رو دانلود کنید
✅
•
https://github.com/bepass-org/nekobepass/releases
2. پلاگین رو داخل برنامه نکوباکس فعال کنید.
3. وارد لینک زیر بشید و فایل worker رو دانلود کنید
•
https://github.com/bepass-org/bepass-worker
4. به کلودفلر برید و یک ورکر بسازید وفایل رو داخلش اپلود کنید
5. ورکر خودتون رو در فرمت زیر قرار دهید
https://name.workers.dev/dns-query
• /dns-query
6. فایل خامی که باید در اخر ادرس worker خودتونو داخلش قرار بدید  داخل لینک زیر هستش
https://rentry.co/bepass
💡
خلاصه و نکته:اگر حوصله ساخت این کانفیگ رو ندارید میتونید از کانفیگ اماده زیر استفاده کنید و از نسخه ۱.۳.۴ برنامه رو بریزید:
#کانفیگ
های آماده بدون نیاز به ساخت:
👇
https://rentry.co/bepass
(این کانفیگ هیچ ربطی به پنل هایی مثل نهان یا bpb نداره و کاملا متفاوت و نتیجه دیگه ای داره به خاطر وجود پلاگین یوسف د نکوباکس)
#یوسف_قبادی
@xsfilterrnet
👑
@Paradise_Of_Freedom
⚡️</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/MatinSenPaii/4505" target="_blank">📅 23:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4504">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">همراه اول Masque + Balanced ترکیب خیلی خوبیه</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/4504" target="_blank">📅 22:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4503">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBloom.(Tin.)</strong></div>
<div class="tg-text">این‌روزا تماما بغضم. از دیدن این وضع زندگی و اینهمه فشاری که به مردمم میاد
از اینکه حتی نمیتونن یه زندگی معمولی داشته باشن
از اینکه نه نونی هست برای خوردن، نه آینده ای برای امیدوار بودن..
هر روز میبینم که قطعی برق چه ضرر‌هایی داره به مردم جنوب میزنه..یکی رو خودش بنزین خالی میکنه، یکی از شدت فشار جلوی دوربین گریه میکنه..یکی گوسفند مرده رو میذاره رو کولش که ببره برای زن و بچه‌ای که دوساله گوشت نخوردن..
چی میتونم بگم، فقط اینکه پا به پاشون من هم غمگینم..</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/4503" target="_blank">📅 21:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4502">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">همراه اول Masque + Balanced ترکیب خیلی خوبیه</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4502" target="_blank">📅 19:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4501">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">☠️
اتصال رایگان و پرسرعت با پروژه Aether + پروتکل ویژه گیم Wireguard
⚡️
لینک پروژه‌ی اصلی: https://github.com/CluvexStudio/Aether لینک پروژه GUI من: https://github.com/MatinSenPai/Aether-GUI دستور نصب از ترموکس:  curl -fsSL https://raw.githubusercontent.co…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4501" target="_blank">📅 18:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4500">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خیلیا سر ویدئوها از من می‌پرسید که کدوم روش برای نت ملی جوابه؟ و آیا «اینم زمان نت ملی قطع میشه»؟
جوابش اینجاست که کامل توضیح دادم:
https://t.me/MatinSenPaii/3680
اما خلاصه بخوام بهتون بگم نه این متد ویدئوی آخری نه پنل‌های کلودفلر هیچکدوم وصل نمی‌مونن طبیعتا. اگه اینا وصل می‌موند که دنیا گلستان می‌شد. قطعی اینترنت معنایی نداشت دیگه.
با بسته شدن
cloudflare.com
و آیپی‌هاش، اکثرا از کار میفتن(sni کمی سختتر)</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4500" target="_blank">📅 18:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4499">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">مشکل گیر کردن روی answering setup prompts رو هم برق برگشت سعی می‌کنم برطرف کنم
🎨</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4499" target="_blank">📅 11:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4498">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">و رفقا در مورد ویدئوی قبل و اسکنر، من مشغول کار کردن روش هستم که اسکنر رو خیلی خیلی قوی‌تر و پایدار تر بکنم روی اینترنت‌های محدودتر مخصوصا نت همراه، و به زودی ورژن جدید SenPai Scanner همراه با نسخه‌ی اندرویدش قرار داده میشه روی گیتهاب
تا اون موقع با تعداد ورکر پایین(50 یا زیر 50) و با کانفیگ‌های BPB یا Edge یا پنل Nahan تست بگیرید. با خود Cfnew تست نگیرید</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4498" target="_blank">📅 11:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4497">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">تمام تلاشم این بود تا قبل از ساعت 12 که برق بره ویدئو رو بذارم
🦆</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4497" target="_blank">📅 11:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4496">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XEym4_JibZ2iOyaPIiZAlqdBNG-k1en8asds2l0lEwU9hreQJrk3QMxQhG53pQzz1TV2ExxvlkDZbpjVHZ-FY115IX0NNW8R9CySLdqHOXMMqHQmzbOvcXQKZb1TjkmXTX1r7WWERJ_UcB7l5EC7eGMSbSAv8NAVb4CEIXi3ZaZxB5-LASRSwLRNhwJ4nLk9B6fXRhHEatFo_dN-rLyKmc7wX8BC7jF1hPlwdegyUm6RAHYh8-10tlDEO-h7Uf2DI0ZkIEeqmF4n42QQ4oNTiArBmGSWzxhZmzP6cx-T5Cn-Whix5YcBB_89-703XdQwR1mXzfCkg8s79lziNbpV6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
اتصال رایگان و پرسرعت با پروژه Aether + پروتکل ویژه گیم Wireguard
⚡️
لینک پروژه‌ی اصلی:
https://github.com/CluvexStudio/Aether
لینک پروژه GUI من:
https://github.com/MatinSenPai/Aether-GUI
دستور نصب از ترموکس:
curl -fsSL https://raw.githubusercontent.com/CluvexStudio/aether/main/aether.sh -o aether.sh && chmod +x aether.sh && ./aether.sh install
دستور غیرفعال کردن محدودیت مصرف CPU و باتری:
termux-wake-lock
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش‌نیاز فنی و نیاز به خرید سرور و... نداره. حتی نیاز به اکانت کلودفلر هم نداره
😂
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/MatinSenPaii/4496" target="_blank">📅 11:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4495">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نفر اول:
دوست ممد
🥳</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/4495" target="_blank">📅 10:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4494">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">آموزش رو ضبط کردم. قرار میدم واستون کمی دیگه</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/4494" target="_blank">📅 10:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4493">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">متشکرم از همه‌ی دوستان بابت فیدبک
روی ایرانسل و مبین نت اختلال بیشتره، مخابرات و آسیاتک و همراه اول جواب بهتری گرفته بودن همه
برای گیم هم Wireguard بزنید. نه warp on warp</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4493" target="_blank">📅 08:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4492">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4492" target="_blank">📅 08:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4491">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اگر سؤالی دارید، توی کانال سازنده‌ی اصلی هسته‌ی پروژه بپرسید:
https://t.me/CluvexStudio</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4491" target="_blank">📅 08:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4490">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bP8WV4id65nnhCJN5_JjluYsoUn8FFpJOrPPOo3xNlKqMoIPpyiE1mi3OPMlke37cIaCs5Qu5VDz0B_NLfjzqf9H9-aB4h-_SOq1B3LGCrKUmRDQU6SR88OrD8OlBqS6LqXefAQ0paDeNJm2mdA4ZYhO8fQbQfeISSThfBE9_upg0lqicQOqCdmzO0D9z5hcyDdB_0y59kMtSbbBYR_Q-4XtJU5jxEyQZICu7xMZnWNlYFODOrOx64ovapI1jP5K66gxSgyFktPkTQxkRXrxyJxKBUF4EZtixF7lN_xKQnj_50z-YZD0Cd-Y16APyLb91Xw5O2NEcBV0RzoWXEeofQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقت کنید که Wireguard آیپی ایران نشون میده(نه آیپی خودتونو)  ولی Warp on Warp آلمانه اصولا بعد از کانکت شدن هم خیلی راحت روی V2rayN بزنید و وصل بشید: socks://Og@127.0.0.1:1819#Aether-GUI</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/4490" target="_blank">📅 08:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4489">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">هنوز کسی سر گیم فیدبک نداده
👀</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/4489" target="_blank">📅 08:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4488">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/skEVOIFSZhcmSkot4bPlqxfwNphi5E3MgcfIy8yVOqllQYW4J5HgDrlza4FruzRU0OKTKbcNxBMqfEWG4mZ0uDEH3gA6r5Hnso-bJ6R2NSkvNn2qNMNW230sOPWO2MVR77xi7aFiL-BR2WYF1vCaqXSKIlVosRz2yQa_hrlpaA6Zc71YvRO3zO1q-xXmh-B6so7I5wMs9jOpKhQ7L5MlhzxIcpD8l6hbShQHP79aZYmocclZIHuGTZ_i2z_kCAL0sXWlW5TDW3LERUlfXob_FdNGynCzE13xNWXQeJ87nz590VZeJdGVZOFnm2xocvLDZID7mqolIDQAC0ix-_kMnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر این ارور رو مثل دوستمون می‌گیرید، پروتکل‌های wireguard و warp on warp رو امتحان کنید و همچنین scan mode رو هرچی از چپ به راست ببرید، سختگیرانه‌تر جستجو می‌کنه</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/4488" target="_blank">📅 08:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4487">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">موقتا نیاز دارم بچه‌های گیمر سر این متد Aether بهم فیدبک بدن، ببینم تا چه حد پاسخگو بوده براشون هر پروتکل(یا اصلا نبوده)
https://t.me/MatinSenPaii?direct</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/MatinSenPaii/4487" target="_blank">📅 08:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4486">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4486" target="_blank">📅 08:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4485">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">به همین راحتی</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/4485" target="_blank">📅 08:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4484">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">خوبیش نسبت به Worker کلودفلر اینه که محدودیتی در کار نیست و همچنین دردسر اضافی هم نداره.
سازنده هم لطف کرد اسکریپت راحتتر واسه ترموکس نوشت:
https://t.me/CluvexStudio/254</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/4484" target="_blank">📅 07:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4483">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">بفرمایید دانلود کنید. قبلش با سازنده‌ی پروژه مشورت کوتاهی داشتم و اجازه گرفتم که روی یه پروژه‌ی مجزا GUI رو بنویسم دنبال راهی هستم که همچنان اتصال راحتتر بشه. فایل Setup رو دانلود و نصب کنید https://github.com/MatinSenPai/Aether-GUI</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/4483" target="_blank">📅 07:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4482">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یه ‌GUI راحتتر واسش نوشتم روی ویندوز</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/4482" target="_blank">📅 07:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4481">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">روی گوشی درست نمایش داده نمیشه</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/4481" target="_blank">📅 07:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4480">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">خیلی خلاصه بگم:
فیلترینگ به‌طور معمول دو راه داره برای شناسایی:
(الف) دیدن امضای مشخص پروتکل در هندشیک،
(ب) بلاک‌کردن آدرس‌های شناخته‌شده یا کل ترافیک UDP.
حالا  Aether راه (الف) رو با تقلید از HTTPS معمولی + نویز خنثی می‌کنه، و راه (ب) رو با اسکن دائمی آدرس‌ها + قابلیت سوییچ به TCP (h2) دور می‌زنه.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/4480" target="_blank">📅 23:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4479">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CcB0LC5vEW_s9DcFsZ0rOqllszdUVTaBfuLvduKGGQocDMqTZHiH3AzIzDHhSNiZ8SlJN1C7gTVwAR4h3rxAL09zOVfbp3bYD4oRHqEV3Y8C1i3t3anYdlgI8uKiWlWGEr1Pwx5WcRRVjzFD2ifFcAuFWMgA5x4U3urPJM063TVpqSk1go6yr3zDArsS6l_iaOLoBdB4dkayi1KwzlMIKs1tEkRgrf0f3p46uIBcp4hgr2kX_xkO1VoadnXhk4MeoOFhpJ55J0zwvrQnQcRm5tNW1BjRfP173BGz_LojgaDw3VvkKjN17UwLKnSIvzQa9HjOiwu0v9qt-ZgbWpu3qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4479" target="_blank">📅 23:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4478">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/4478" target="_blank">📅 23:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4477">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">به زودی آموزشش رو می‌ذارم. هم دسکتاپ هم اندروید</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/4477" target="_blank">📅 23:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4476">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
خلاصه از متن و ساده کردن برای دوستان مبتدی:
شما فیلترشکن oblivion یا وارپ(
1.1.1.1
) قطعا میشناسید.
این فیلترشکن ها تا قبل از دی ماه خونین متصل بود و شما با تنها وارد کردن یه مقداری مثل ip شیر و خورشید متصل میشدید ولی بعد از اون ماجرا ها از کار افتاد و هسته عملا بروز نشده بود تا الان.
حالا یعنی چی یعنی واسه
#اندروید
و
#ios
قراره هسته اپلیکیشن هایی که مربوط به این روش بودن بروز شن و شما بتونید با اپلیکیشن هایی مثل:
Oblivion
(اندروید)
Defyx
(ios,اندروید)
💡
نکته:فیلترشکن defyx رو میتونید بریزید و از یوتوب بدون تبلیغ و سرور های معمولی به صورت نامحدود استفاده کنید.
متصل بشید خلاصه بود از این پروژه وارپ این وارپ.
متین به زودی آموزشش رو میگیره
❗️
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/4476" target="_blank">📅 23:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4475">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qkQCv0rg9dLPVghqdgSFqb_uM_GxHIpa6klSBpj0salsjf0HH4R0f2eJealV3j0wiyzUCku3dF2Z0Ez4DL-QWSsdvJ8OqG-pUYrBazXyqiMNMpNy5rRHp1c1m8ggdbUmoEsFIPra-2iT5aepccCZEEg71CiFobGc_h7Q2P9oGSlNpdg5DgaI_t8d4YM9QCBHa4VWXaKURYeD-m9IiZDU0vI0zJ20_P9nKoy9IBAcWGurm2fOKQbBeZYALpPZTUerU_e235K1RxMvCIgR-PuoxufHQYbsRZ35oHZfHHU1tpszACt5RMhUWI8ij-bG7Do5O0BqAsFBJoKkq6EDHh_6Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوق‌العاده.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/MatinSenPaii/4475" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4474">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">الان خودم ران کردم و حقیقتا جالبه</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/MatinSenPaii/4474" target="_blank">📅 22:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4473">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اگر ارور Port already in use روی ترموکس می‌گیرید، باید لوکال پورت V2rayNG رو از ۱۰۸۰۸ تغییر بدید</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/MatinSenPaii/4473" target="_blank">📅 22:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4472">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">Aether یه پروژه‌ی شبکه سریع و مقاوم - برای اینترنت آزاد Aether  با ترکیب Cloudflare  پروتکل MASQUE (روی QUIC/HTTP3) و WireGuard به‌همراه چندتا لایه مبهم‌سازی ترافیک خیلی کمک میکنه از DPI و فیلترینگ شبکه رد بشی  برنامه خودش به‌ صورت خودکار بهترین Endpoint موجود…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/4472" target="_blank">📅 22:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4471">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">Aether
یه پروژه‌ی شبکه سریع و مقاوم - برای اینترنت آزاد
Aether
با ترکیب Cloudflare
پروتکل MASQUE
(روی QUIC/HTTP3) و WireGuard به‌همراه چندتا لایه مبهم‌سازی ترافیک خیلی کمک میکنه از DPI و فیلترینگ شبکه رد بشی
برنامه خودش به‌ صورت خودکار بهترین Endpoint موجود رو اسکن و انتخاب میکنه پس نیازی نیست دستی چیزی تنظیم کنیم یا دنبال سرور از پیش‌ آماده بگردی...
روی شبکه‌هایی که فیلترینگ سنگین و پیچیده دارن هم عملکرد خوبی/عالی داره چون از پروتکل‌ هایی استفاده می‌کنه که خودشون رو کاملاً شبیه ترافیک وب معمولی نشون میدن. :))
پروتکل‌ها:
MASQUE + WireGuard + WARP-in-WARP
برای MASQUE هم به‌ صورت پیش‌فرض از HTTP/3 استفاده میکنه ولی اگه تو شبکه‌ای هستی که HTTP/3 یا QUIC محدود شده
میتونی بری روی HTTP/2 که سازگاری بیشتری با شبکه‌های محدودتر داره.
یه اسکنر داخلی هم داره که خودش endpoint های سالم رو پیدا میکنه و انتخابشون میکنه :))
مناسب هم برای شبکه‌های به‌شدت محدود هم شبکه‌های عادی.
پشتیبانی از:
Linux، macOS، Windows، Android/Termux
دانلود:
https://github.com/CluvexStudio/Aether/releases/tag/v1.0.0
اینترنت آزاد برای همه! :))
بزودی توی Defyx و Oblivion هم اضافه‌اش میکنیم!
داکیومنت فارسی/اینگلیسی هم کامل نوشته شده توی گیت‌هابم حتما بخونید:
https://github.com/CluvexStudio/Aether</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/MatinSenPaii/4471" target="_blank">📅 22:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4469">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XOnet4_SC0cPkMaB8dmk6avF7PZD42CojvmEEMwBcpY-Z04k1WCmN-uk4Frjdz2Wc6CBqKKauVcsZMCB1noyf-pS9xl5mzsmqxDElQdQgNizKaptFUmiBYvaiLCtX0wcM8nB3iFHLJo1pW6pbzj2u5FUDO9Laqir9T6p_A-JudaUWCD1DnTXxlPrZIILY331A_a-xY-iSh7hUWb_FgoTN49DCQTh8oACPVIUuo8jeNYcamEKstHuBw_cnlfJXRCxs4AJO9e7Pppusx5-DkN3ra4m7aULN79-pu_rBbw-zI-YWeaJYc_nYvdSYdDlVk8qnPj_QtLXiXxQxgCDQf_gAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rU1TkI_Ymi43o0iIvCzZgIdotCWCbEJITR4DJTLgFEN5epJgFlGVBkBf9Qn9q0Z5E7ujYmmCKToblsasBazvS4ZNlBVus1hU-qlDlTJf6EgdQQivUJ21EvmdHssvXDx-oObMmDTCGNWG1DFbPa1m_Q1SUV5KGUc1CVikwAh_HYmct5G7fBGdQA0vJMqf2OPHPVB5WSk8gTV8X7uSF8dGsn93Cwdfz7KURNU5fbqzVJAMlbONiKN7sN_59vt0HkJc-v5wEN0DHbF3BgZ49hoEAVbifbRQ07VFgDKIsTT07HuEQGiwp2u4RnBIxPsVoRSH4-ewLNGEcymFMHQOLSLvOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از کلاد خواستم که
https://github.com/Graphify-Labs/graphify
رو نصب کنه روی پروژه‌ام(کارش اینه که کل کدبیس رو تبدیل به یه گراف دانشی عظیم می‌کنه تا Agentها به‌جای باز کردن مداوم فایل‌ها و دنبال کردن importها، ساختار پروژه و ارتباطات بین بخش‌های مختلفش رو مستقیما درک کنن) و کلاد ازم پرسید داداش مطمئنی میخوای اینو نصب کنی؟
زدم Proceed که آره مطمئنم
دوباره رفت یه کم دیگه گشت
گفت ببین این پروژه تازه سه ماه هست اومده، 86 کا استار گرفته روی گیتهاب. خیلی مشکوک میزنه. نصب نکن چون امکان نداره یه پروژه یهویی انقدر پیشرفت کنه
😂
😂</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/4469" target="_blank">📅 21:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4468">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LrBlFFRg3i-I265trP-aYPEG_R0HK8PMB8spKNDkD0Tr7t5jg8KCTqiOUot82Llm9DJ2x_5xcQstX6vVEWQXB91wMK8CHFbVSE2TLIWhxP8P1Fm0ccwrK17XupeDpfG1kQucmjWYILjvaCgSTIdG-1hrKi9nExyx90F_v7uCiiVVtjUFLpQahtIoucaDt6BFLKbPGGrPICZXQaWH8Lspouf8VzOyc7FXQcFJXvzoG9bgLtPuuIWoSoe-sNbba_Aprj2NLB1zZKgqd0Ip631uaa1GbvmtgM3mpC62J2HhsmhckSrU9nEUl_Txs1_NRn6yPy3vouM7ANIDv-hc_5Rd0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب رفقا گویا دامنه‌ی
t.me
مجددا در دسترس قرار گرفت بعد از توییت پاول</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4468" target="_blank">📅 19:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4467">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ببخشید.
خودتون میدونید دیگه بانو
❤️</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/4467" target="_blank">📅 19:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4466">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/a54ac3d5b4.mp4?token=F_4UKW3jVHChwbmc_c9jXizUkIFKSKzUGInCYU04-QBXx4PWnxPIPynZ7EhC9ge5KGof1lYFjGoJX7E3v1DLbDuRw34JoqqI2lrsDGRzsSfmUxS5RZ3RzbBbJ9c3sRkhoz8VKBZ0oHSGnG5StUvdch4lf0M0e6mWq8BZAFh5-AQXMwUd0vG7XHaMDNk5XdKfsAjHDkfr9u-6g4H9-WP7iXcPQdT9N2QX-S5rLX17x5f4BMjBS4GO8FFlVxRckiIh8nfafa1G6Y0Yc-tcW8P57IHR2Z9yN6e5957U-v0U4rkKJbI5P_j4cIS4_MW3WlCwfTMdsdsRBGDVpqEPR81_Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/a54ac3d5b4.mp4?token=F_4UKW3jVHChwbmc_c9jXizUkIFKSKzUGInCYU04-QBXx4PWnxPIPynZ7EhC9ge5KGof1lYFjGoJX7E3v1DLbDuRw34JoqqI2lrsDGRzsSfmUxS5RZ3RzbBbJ9c3sRkhoz8VKBZ0oHSGnG5StUvdch4lf0M0e6mWq8BZAFh5-AQXMwUd0vG7XHaMDNk5XdKfsAjHDkfr9u-6g4H9-WP7iXcPQdT9N2QX-S5rLX17x5f4BMjBS4GO8FFlVxRckiIh8nfafa1G6Y0Yc-tcW8P57IHR2Z9yN6e5957U-v0U4rkKJbI5P_j4cIS4_MW3WlCwfTMdsdsRBGDVpqEPR81_Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای خودم نگهش میداشتم
👍</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4466" target="_blank">📅 16:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4465">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">Lira’s first challenge
🌟
به اولین چالش لیرا خوش اومدید!
🤍
این چالش برای همه‌ست؛ فرقی نمی‌کنه تا حالا از لیرا خرید کرده باشید یا نه. فقط کافیه توی این سؤال با ما همراه بشید، چون باور داریم گاهی یک جواب ساده، می‌تونه پشت خودش یک داستان قشنگ داشته باشه.  اگر…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/4465" target="_blank">📅 16:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4464">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLira.</strong></div>
<div class="tg-text">Lira’s first challenge
🌟
به اولین چالش لیرا خوش اومدید!
🤍
این چالش برای همه‌ست؛ فرقی نمی‌کنه تا حالا از لیرا خرید کرده باشید یا نه. فقط کافیه توی این سؤال با ما همراه بشید، چون باور داریم گاهی یک جواب ساده، می‌تونه پشت خودش یک داستان قشنگ داشته باشه.
اگر برنده‌ی این شمع می‌شدید، برای خودتون نگهش می‌داشتید یا به کسی هدیه‌اش می‌دادید؟ اگر هدیه‌اش می‌دادید، اولین کسی که به ذهنتون می‌رسه کیه و چرا؟
برای شرکت توی چالش:
⬇️
در کانال لیرا عضو باشید.
⬇️
این پیام رو توی کانال‌تون که پابلیک هست فوروارد کنید.
⬇️
به سوال بالا پاسخ بدید.
🎁
جوایز:
🥇
نفر اول: یک شمع کروم صدف لیرا
🥈
نفر دوم: 15% بن تخفیف
🥉
نفر سوم: 10% بن تخفیف
مهلت این چالش تا ساعت 12 امشب هست و نتایج چالش فردا ساعت 10 صبح در کانال لیرا قرار داده میشه
🩵</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4464" target="_blank">📅 16:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4463">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مثل اینه که یکی با Toyota دزدی کرده باشه
برق کارخونه تویوتا رو قطع کنن تا دیگه نتونه ماشین بفروشه به دزدا</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/4463" target="_blank">📅 15:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4462">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromوب آموز(m J)</strong></div>
<div class="tg-text">دامنه t[.]me تلگرام به دلیل تحریم OFAC آمریکا از دسترس خارج شد.
در ۱۳ جولای ۲۰۲۶، دامنه کوتاه t[.]me تلگرام (که برای لینک کانال‌ها، گروه‌ها و پروفایل‌ها استفاده می‌شود) در سطح جهانی از DNS حذف شد و مرورگرها دیگر نمی‌توانند آن را باز کنند.دلیل:
ثبت‌کننده دامنه .me (Identity Digital) وضعیت serverHold را اعمال کرد. این اقدام مستقیماً به دلیل تحریم‌های OFAC (دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا) بود. OFAC شرکت First VPN Service (1VPNS) را به لیست تحریم‌ها اضافه کرد — سرویسی که به حداقل ۲۵ گروه باج‌افزار (از جمله Avaddon) کمک می‌کرد تا حملات خود را پنهان کنند. یکی از شناسه‌های این شرکت، کانال تلگرام t[.]me/FirstVPNService بود.
چون نمی‌توان فقط یک لینک داخل دامنه را بلاک کرد، ثبت‌کننده کل دامنه t[.]me را از DNS جهانی حذف کرد.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4462" target="_blank">📅 15:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4461">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">جوری نوسان برق رو اعصابه که هیچ کاریمو نتونستم برسم کل روز. نه سه راهی روشن میشه که لپ تاپو بزنم شارژ، نه نت فیبر نوری کار میکنه کلا قطع شده از صبح، نه آنتن درست حسابی مونده و همش قطعی داره، نه کولر کار میکنه که بشینم لااقل یه کتاب بخونم🫩</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4461" target="_blank">📅 14:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4460">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">جالبه که هیچ توضیحی بابتش داده نشده
هیچ واکنشی هم از سمت تلگرام هنوز ندیدیم</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4460" target="_blank">📅 10:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4459">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگیفت بازار | Gift news(𐌼𝛜)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiwtKkDqc0dhSeAneybtECS8YH_4xYIETzQEQJ_uxJT3KS1HLQGnIa1JDeFYLJJldXRw45AQMrIV3TEhhFkRZsOMljm7I90JIptleZO7zlSYz0V7nVXocM-1M8K6dMAOPt1_AHOJcAwIQZbgny0dMwPdB2ETiXEcEIBj-CZq1v1HuARlLQt5aXAEzcIKyszIQL8bLnMNZmFD3yBUY-OwFWIQFyXPxYW4wMwBQrmIObdwJBWyDN_BpcuDaDrduCtzEep1rNitcsEuSWLxVnrFz0_1c5Dh-2rMiziLYN83UaME8UdvkT9WbhuOYBxTRuGcXWyBbADk7r0lzt8aG7bF_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💸
اختلال در لینک‌های
t.me
از ساعاتی پیش، کاربران زیادی گزارش داده‌اند که لینک‌های
t.me
باز نمی‌شوند.
⚪️
طبق اطلاعات
WHOIS
، دامنه‌ی
t.me
از ناحیه‌ی DNS رجیستری .me حذف شده؛
اما همچنان تلگرام واکنشی نسبت به این موضوع نداشته.
ℹ️
اگر امروز موقع باز کردن کانال‌ها، دیدن تصاویر گیفت‌ها یا ورود به بعضی لینک‌های تلگرام به مشکل خوردید، دلیلش همین اختلال است.
📰
تا برطرف شدن مشکل، ممکنه بعضی از لینک‌ها و سرویس‌های وابسته به
t.me
به‌درستی کار نکنند.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4459" target="_blank">📅 10:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4458">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">الان برای یه سری کار داخل فتوشاپ، چندتا اسکریپت با Claude (پلن رایگانش. توی صفحه چت) نوشتم که کارم رو 20 برابر سریعتر کرد.
بهش فکر کردم، و به این نتیجه رسیدم که اگه فتوشاپ بلد نبودم طبیعتا نمیدونستم میتونم همچین کاری کنم.
از طرفی اگر از قابلیت‌های AI باخبر نبودم که میشه اصلا کارها رو باهاش Automate کرد یا لااقل، پرسید که "آیا فلان کار رو میشه Automate کرد یا نه؟" هم مجددا همچین چیزی به ذهنم نمی‌رسید.
اینه که شما به صرف بلد بودن کار با AI شاید نتونید از 100 درصد پتانسیل یه ابزار استفاده کنید،
از اون طرف به صرفِ "خوب" بلد بودن یه ابزار هم اگر از AI استفاده نکنید و سنتی کار کنید، به راحتی عقب میفتید.
هر دو با هم عالیه!
<تجربه‌ی شخصی. نه Fact></div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4458" target="_blank">📅 09:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4457">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚀
انتشار نسخه نهایی و پایدار MTProxyMax v1.4.0-LTS</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4457" target="_blank">📅 09:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4456">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">📱
دامنه t.me تلگرام تعلیق شد؛ قطعی ناگهانی لینک‌ها در سراسر جهان</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4456" target="_blank">📅 09:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4455">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">توی علم روانشناسی به «جوک ساختن با قضیه‌ی جنگ یا قطعی اینترنت» می‌گن طنز سیاه (Dark Humor) یا طنز گالوز (Gallows Humor). این یه مکانیسم دفاعی برای بقای روانیه، نه نشونه‌ی بی‌خیالی. مخصوصا سر قضیه‌ی جنگ
1- جنگ یعنی استرس، ترس و درموندگیِ مطلق. اگه این حجم از فشار رو سرکوب کنیم، عملا از لحاظ روانی مریض می‌شیم (و همچنین در بلندمدت می‌تونه ریسک PTSD رو افزایش بده.). جوک ساختن مثل یه سوپاپ اطمینان عمل می‌کنه و بهمون اجازه می‌ده این فشار رو به یه شکل غیرمستقیم تخلیه کنیم. (در عین پذیرش واقعیت، تحملش کنیم)
2- خندیدن روی بدن جواب می‌ده. سطح کورتیزول (هورمون استرس) رو می‌کشه پایین و اندورفین (هورمون شادی) ترشح می‌کنه. تو شرایطی که ضربان قلب رو هزاره، مغز با یه میم خنده‌دار، ترمز دستیِ استرس رو می‌کشه.
3- جورج ویلانت طنز رو جزو یکی از «بالغانه‌ترین» مکانیسم‌های دفاعی طبقه‌بندی می‌کنه. توی این حالت، ما واقعیت تلخ رو انکار نمی‌کنیم، می‌بینیمش؛ ولی با طنز یه فاصله‌ی ذهنی باهاش می‌گیریم تا بتونیم تحملش کنیم.
4- وقتی دوتا کشور می‌جنگن و موشک میره و میاد، شما هیچ کنترلی روی اوضاع نداری. اما وقتی باهاش شوخی می‌کنی، مغزت حس می‌کنه حداقل روی «روایت داستان» کنترل داره. با خودت می‌گی: "من نمی‌تونم جنگ رو متوقف کنم، ولی می‌تونم بهش بخندم!" این بهمون حس Agency و قدرت ذهنی برای مقابله‌ی نسبی با این قضیه توی ذهنمون می‌ده.
5- توی شرایط ترسناک، آدم‌ها به شدت احساس تنهایی می‌کنن. وقتی یه جوک مشترک می‌سازیم و با هم بهش می‌خندیم، یه حس همدلی‌ای این وسط شکل می‌گیره که تاب‌آوری جامعه رو مقابل این قضیه بالا می‌بره.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4455" target="_blank">📅 05:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4454">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gFc88T2V3MBOFRtYA7tiJN18c4fRmQEVDvhijWF_kufSJzNGhLBDhcAuyu8h7gkdSZhOV-cYk4Oc5N2cp-0kr-N8SHWdSZYr9k1Edx0TLLMvferZZuiIvnIw7YRq_buI_G0LlmUshm9PES138iXa-6Jn7CGsgnLgRkWHlrT37MDEduiOsFoUrZ3dsceATLHLw4aD9Vu27nQihsL010W0sFTHJkgEir_e99LJ_Uhqyxj4PvEJZbsX9fYrtYvc1NgpCVivqjpc9DpvwVg4a2GBCyGPIvmD4YUT2nlO8j_4K6SsXAXBmQKggtxRz0cIfU0SymTbPTtBYOQzCLr-8-LDHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتباطات زیرساخت در حال لحظه شماری برای دستور قطع</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4454" target="_blank">📅 01:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4452">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cSa2-3XxPqOpSTfH9QxtFMGJEzJ7j_uYar7LVnRAYPYREPB_9xplLeDr7104xVQIs-7-BSj-v-s-ICobPy5mu59JWrDSLSVj_boSu0TTUcuWeNdlL0tNMNMmdc7Ka1TjtbsHPtd-nzDDmX6IgAiFUYb1uJtJFBtoW2utNfe-eXy8xiFS4tWe3yRE0vBD5k_mlc5DzGu4v1_-Wkbz_SaSXniOQD7OwxEFEgCvcQcqBItuD6Qrx4jLwf0YY5hDBDW09w-g0txXMo3vdYky7EMuthYRSV-Szj6rQAnaM0l6q1GYdg54mAfm4sNnaNRsftb9iuYmnkinfUKun-48yr0f2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T6NBKCurzTZoFOWz8f_v_t-7Yr9DfC2AUo3cxn_GnRmqFd26QkS-XPwp7WUNACVB724BvUH8WgJ6waeHXM8jbzKaIFMG7pMoxeznzERJcCYU9joPCeWpvIgc-TfXZIzyaMexAVg0xQWpCYujIN6WhP2nHxqzBwU0tlk-FEKnm1LAGgNL9yAoAv6sF0dC99yynuawBmRGFQJVl1myiG9nLxdU6R66MNErYuS1lNl31SxE_Hyx7_rIRhohVjxPNVXQTNa71d4BaYpXgqBrRW7gK65d1QDZX3KmGPncRh7W-_8M4AKJQL-eOfZ5ukYJqu6XMueSpSARL3OJRfM2MSCxgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فکر کنم من یادآور خاطرات بدی هستم متاسفانه
😂</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4452" target="_blank">📅 01:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4451">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge  https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4451" target="_blank">📅 01:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4450">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">Android</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4450" target="_blank">📅 01:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4449">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">Desktop(mac-win-linux)</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4449" target="_blank">📅 01:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4448">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">Master-White-DNS-@MatinSenPaii.zip</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4448" target="_blank">📅 01:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4447">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">امکان دانلود کل ریزالور ها به ربات @dns_resolvers_bot اضافه شد   @WhiteDNS</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4447" target="_blank">📅 01:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4446">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohammad👑</strong></div>
<div class="tg-text">اگه دیدین جایی نوشت
تهران رو زدن
ثانیه بعد نت قطعه</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4446" target="_blank">📅 01:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4445">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hj7XWFUs6UjpkXfy7cJKC9bx0jOTgZxQ8KKtWOPiOi2se4ndDojqOxEvC63qfWwQYv5qQv_o3mkD0usDag150u8DN0trVM53o8FLt4IwGY9LxuDmTG2jzJiwxADjG0cwzbWarPdAZUvdEKKT9tCDvJ6uwibFq4O8kvKQf_6fuDFUxWw20ZZTw5vYboBfR9IgniuM9lzB3_fM30blqCjIk5AkhVwxZv9jMnjdpNflJHGAS5clGxerhrgn-jyYLT4Ega_W506pysQJT_CcWkOaQZVp7drUNUZj5Rb1geza1oYM_FXbyR2peCqRM_EHhA_JzoOLMP9kFtexfL1-ewc2zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق معمول، پیشنهاد میکنم WhiteDNS رو راه‌اندازی کنید برای خودتون و دوستانتون
آموزش:
https://youtu.be/6Pm7kNQb3mo</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/4445" target="_blank">📅 00:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4444">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHaoodi Senpai</strong></div>
<div class="tg-text">صابرین نیوز داره لینک چنل سروش و روبیکاشو میده.
این یعنی به زودی نت بای بای
😭</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/4444" target="_blank">📅 00:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4443">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBloom.(Tin.)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pO9ZL-lHBeuz2o1LFTAvUebohSg46a9YQeW1fKp2xmiSY_C4NqGVDDGJXdJQZes_gBjGEpaTdB6NH65EQX3aX6JczGU1EWCNeOhtxsrT_qtQDxbWCkd7AYFz8RbWII7kM21o0b4B9A6K6p_cHh8yQzA_bYPRlM2CwVHK3DUwkxpqNsdOy0VeMfoUxUSCO539NFzgt3WQtAruayVbDIq3_cXCsPTjq-63QDjkvx9ovfo-sef9oLS6COyRfFiz4IiCOs9L3gZDP3cISfHQVHRviZJzycwvH_4pzOOMaNYNpHohY09DL4hpLZ-7o9DTFfPJMrTM54ZCFnSLgOagmOZ1PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Solomon’s paradox
“انسان‌ها معمولاً می‌توانند برای دیگران توصیه‌های منطقی و عاقلانه ارائه دهند، اما وقتی پای زندگی خودشان وسط باشد، اغلب نمی‌توانند همان توصیه‌ها را به کار بگیرند”
روان‌شناسان معتقدند آنچه ما را از تصمیم درست دور می‌کند، کمبود منطق نیست؛ بلکه نزدیکی بیش از حد به مسئله است. هرچه یک اتفاق بیشتر با هویت، احساسات و آینده‌ی ما گره خورده باشد، و درگیری احساسی در ما ایجاد شود، احتمال سوگیری ذهنی بیشتر می‌شود و تصمیم‌گیری، سخت تر.
البته که احساسات، بخش مهم و تاثیرگذاری در تصمیم‌های هر انسان است؛ اما زمانی که فرد با موجی از احساسات مواجه میشود، ایجاد تعادل به مراتب دشوارتر میشود..</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/4443" target="_blank">📅 00:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4441">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">معرفی  Rowboat | یه همکار هوش مصنوعی که همه‌چی یادشه!   یه ابزار جالب اوپن‌سورس توی گیت‌هاب پیدا کردم به اسم Rowboat. این ابزار در واقع یه «همکار هوش مصنوعی دسکتاپی» هست که روی سیستم‌عامل‌های ویندوز، مک و لینوکس نصب می‌شه. توی اولین نگاه هم شبیه هرمس به نظر…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/4441" target="_blank">📅 23:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4440">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4440" target="_blank">📅 22:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4439">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cL_UvYckaInzw-4baPC3XySpam0vA0wKArik619-StT3Fgq4YV8RzbTfpYfurVrAdnUeEjr-n37ySO0lOKD3hERvS8aSnlCF11csLuUisPrz95fMRBY8qVT_2OTHbC9M1ykiIoHgaDai_wLLQ4tE_eiHHlbopObqdAoVPw7eUT_rlz7-IHoFyj5AMDELPbsEvBc9uxTT7lCzC5ov0AhPqNe4dXhS7lII094zdbAVsiQp0XV7wc0hDdAgkLeltwHoZPTaIWoYZjnOnSxoaQ-LKInV-kgpnmw2a_xkBIX_ExWIR-UGhjG190mLVXO2-I8bwASROzR2INEWGnDkCr3R3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">8- بخش پایانی Integrations:
از قابلیت اتصالِ One-click به اکثر محصولات و ابزارهای پرکاربرد پشتیبانی می‌کنه.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/4439" target="_blank">📅 22:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4438">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UNu6V0O4EKXnj7wntTW8KoODDBA5UgLckBfRn27E-TF6-zoKMRkBmca_HLY3YuZ_Q50F-sF4kNFcFFdtXP5x2RglqAInLaOq3Oheiv46rMFbL-WG1Fx6HlfgvUY5EMzviZdxCkcRzlH6Z2aTtUjVMC12AD2Bkw0WK3tVa6paAcaY2aGW-fB001CkE6tQxEwD-XSbwMXtJm0dNLmrBScnxI1WA_hp3y2-A1KQ4foxflurDxMqh8fUPgqUT5VOsR7bvF1VB7NsNKZTqifeW48JJwmz9T_LZfOAd3xQa0mSUNOMN_P9P_n1q9v14vlUxH39WUMuKPopy1LrV_4Y1-56RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">7- بخش Apps:
می‌تونید فضاهای کاری اختصاصیِ خودتون رو داخل Rowboat بسازید؛ این اپ‌ها به تمام ابزارها و اتصالات دسترسی دارن و حتی می‌تونید اون‌ها رو با بقیه به اشتراک بذارید.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/4438" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4437">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/czcdaEGVwmKzmYt5zgaf-_LQwSB1P5aN-KSmqpSeWm6W93YTKgI4-GlhdqM4KAmNz_MDTWPI9NjWypAYSsKxVFPLTkR3vt1TTNUqEy0xoj7yH6UkMBkvIa37_oQVoB6Glpeeata9Nm56zxqGTFTBMEpB3QEIEHksfNQbb0KxWgs9cm3qXrSrekvS2FOFViHK_xtqkPOVSdKqp6RWzTuPwQfISlG1YCX-8i3EK-vjGR-prlEJ0NrN72gDv2GCGnwWuUWTkVJS3EJX5ISM6lOfUXIiq40kYeXQ6BwAG58E373iRawIAosO--EyncqlJrlyqIDKmirSpT1LxTW7Ob2U5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6- بخش Code Mode:
این بخش بهتون اجازه می‌ده همزمان چند تا ایجنت کدنویس (مثل Claude Code یا Codex) بالا بیارید تا Rowboat با استفاده از کانتکست پروژه‌هاتون، اون‌ها رو هدایت کنه و کارها رو پیش ببرن.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/4437" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4436">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L1OKu7dAqDXXnlvx8Okip41L-g8P9C8s7SA7rkmlps-m5OPgps25fvfjmWlkwzRERoCcZBF-kj5A5WGXfVlUMWDO0GmuCgGjKCK39ipj9HDu8AYdoEeXhcAcHY1T5_2rjitfl2eNnVUu0pE_usdPLC1pWbWonDSW9gWEEHV642KBRerlUM-mH3gQ7BdJRz2bqlLRUs6yoIOTA4CXJrwajeqRFzkQrElYevZZODUilPuk1ByBDrULQldC2geTHsjjhTa-L5IZnREJcF_doE8QAY_dxFD3q86bUiHmtFInOLTlQZj7QOAVAmfHkByPsIskcNneiMZw9wWvjO1lp_hlpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5- بخش Meeting Notes:
یه دستیار محلی داره که مستقیماً به میکروفون و اسپیکر سیستم وصل می‌شه، همون‌موقع صحبت‌ها رو تایپ (ترنسکریپت) می‌کنه، در نهایت خلاصه‌ی جلسه رو تو یه فایل Markdown بهتون می‌ده و گراف دانشِ سیستم رو هم آپدیت می‌کنه.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/MatinSenPaii/4436" target="_blank">📅 22:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4435">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VHBA9zvN22XGRroNZ5uAKtflbnAy_Zr0re9HXQ0d1YwZdi25ZcDKTVJAedjJfOXP4qFmfFBQ-swMeWlIQ5VG3fayhSy6udan5HfOj2oCtEPQ0ns2sPCP_1iBFQrxva9Ec-lunLJPs9e-K3tfJSuTwv_C4iseAkaFlQvbld7x3PfR_O0OyiPnvWkCy7OIZwEJtNMId_7-5cHBsiA7ExERoo5NUeT8Jv1oSNTAY_ST8tT_ef99zcCeJAu0dJzQW8Ba4ebZX2UlaHGJEegSfubSSk9OfcjDMVjs6owADCk1NZwZe0vl_0XnXWROTZkhVsMZ9WYdVT5Z1A99URdf-DScmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4- بخش مرورگر اختصاصی:
یه مرورگر  Built-in داره که اجازه می‌ده شما و دستیار هوش مصنوعی روی تسک‌های وب با هم کار کنید. چون این مرورگر از مرورگر اصلیِ خودتون ایزوله‌ست، می‌تونید فقط تو اکانت‌هایی لاگین کنید که دوست دارید هوش مصنوعی بهشون دسترسی داشته باشه.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/MatinSenPaii/4435" target="_blank">📅 22:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4434">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U9LffR7WcY9LqGazSjBXKcMjdbMCcZ6LYt9pVwvwx8xhQ2w1SW2YJNKb4Mc1yUe1Sl0ViSXvBWkFmgGimf4D7qf8PCI8QWOuzzKR66crsgHglr0-h0RG8GKEl2BhO1WSV7k0sKO9OYXOfCeEzpYhF8et_UzkMwCmWGMgy2v8aC4qkbqZP_uoteuACpGSKVaW6-xpnwZ8U031_5EEXH4oR6Reo6vQrGGNCqI5AykkCPO3i3Be3lLYuCXEKpmw-yi2J-4Agqib3xGd2U_MIkk8Ni98cdsRHdMEg-BvoIYkKr2C95VHjO7U0mwmk7Z0QdsQ9GhiVxN864RQJrchrGuQRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3- بخش Background agents:
می‌تونید ایجنت‌هایی بسازید که بر اساس یه اتفاق (مثلاً دریافت ایمیل جدید) یا بر اساس زمان‌بندی (مثلاً هر روز ساعت ۸ صبح) اجرا بشن. این ایجنت‌ها می‌تونن به ابزارها وصل بشن، تو وب سرچ کنن، از مرورگر استفاده کنن و حتی با Claude Code یا Codex براتون کد بنویسن.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/MatinSenPaii/4434" target="_blank">📅 22:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4433">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mY-CbkTwzCtgqahp4BZY8A_gc25GVHTp_L6A6PZFG-z2V_B5dTnsScOUSAr0PkrtW_aevA7mG9ePoEhD140cLEItFvWzzuxKkqzhhq21337-KygT3Dqg3TIuHOfUlZ93yBYKglU3jEmlmtbO-3nQsE7meVpXaO9zrT_1qmylAThjF4UFiSwQLslDACClUh1iEd1o4aJf1VAHWcBzA1_Y_PcHg46jYV3muGXtg2reQy6bzloHgsX6qGSaJkk0Tp3pJvyHh01EOzYGLk9jcDWDv8O84_yjkrQ4AKnxkup8tDwKM-od6SNxZ5_chP_TlXxZze6rjm7XyWy5_pbfMLiC_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2- بخش Email:
یه بخش ایمیل داخلی که ایمیل‌های مهم رو از بقیه جدا می‌کنه. بعدش با استفاده از تمام اطلاعات و دیتایی که از کارهای شما داره، به‌صورت خودکار برای ایمیل‌های مهم پیش‌نویسِ جواب می‌نویسه.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/MatinSenPaii/4433" target="_blank">📅 22:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4432">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ziofiv4reQ3q966-PeEUt-EsQtYbSbztG6cQ6T-7HoK5Fro9XlgG0YKmJWZZNmOrgmIQ-uVqoYFs6XLAsRPBebyG1iFpVbDf3de-khTgO-iUZ31z7w2IBka7Lz3QBv3uj59OgZgsbqA46NDBZu9FdsRa4JQk9sBGm19RRwA7Kq_AgfFrlFYFNRgzFMb5TAE9vjCrsanug-gn_QKHD82nte-oNNj9wUItA3a0Srt_cWxqL-gwAGWVAo4lnBnIDnLRP9AGn6duPxCtuiQ39vgl_8VZfYga9cVb_xKZlEOlD04elgt4xSgX0i4xERft-_1WtnDIKDP7O82Ldirs8uT2jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1- بخش Brain(مغز)
کل ایمیل‌ها، جلسات، پیام‌های اسلک و چت‌هایی که با دستیار داشتید رو به یه گراف دانشِ به‌هم‌پیوسته (دقیقاً شبیه استایل نرم‌افزار Obsidian) تبدیل می‌کنه.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/MatinSenPaii/4432" target="_blank">📅 22:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4431">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">بذارید تک تک نشونتون بدم
👀</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/MatinSenPaii/4431" target="_blank">📅 22:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4430">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K9lNwAUW8btU9fcWY88Zs-4O3i6zTpOd7Ne5uHgO0ejcArhAqLPkBcyXmdEAI0DPRzt_SdEGKJ3gHRuxeY0zWEj0ittZzsgSEjzud7AMN9FbBZTLbnLUHpENCUa3zTLYIx3ZkE8D5rW5TR2_fT7vxQ4CKtaklz-iRkkOmHk48acxAR2M7Lht4sDy5N3ehiHmXyIk7sqqFOCODZGtQLkYA0LIUUzjpTeQVSL30F_8JL6uZMIqYDgvEeijStugZkj-ydmgGqKHy1DAEzVzJRmF7uI7AX6VQ47WrjnnZaNdECc-8igW6S81NSfn4epqiE5CKqpMVdVku7v0xxiTEqkA6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی  Rowboat | یه همکار هوش مصنوعی که همه‌چی یادشه!   یه ابزار جالب اوپن‌سورس توی گیت‌هاب پیدا کردم به اسم Rowboat. این ابزار در واقع یه «همکار هوش مصنوعی دسکتاپی» هست که روی سیستم‌عامل‌های ویندوز، مک و لینوکس نصب می‌شه. توی اولین نگاه هم شبیه هرمس به نظر…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/MatinSenPaii/4430" target="_blank">📅 22:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4429">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RQFAzdmV3_FpERQOGl9pd7PAiTLFLDZXiYDvKKU5NvI-gzHRXuM_XBpqPjNB2ujTWP61g0nbATavRZIeQtI-qzkvo3Z5dlnOrYRnOLJtKTct7q_ZXfCPJH_SGX0dBkym-nIjIe-y0O1cW5GDFVd9NVtIIayTRYxhuzsVEkKFbIb36RtPOqwSu4itmnej7vxvtLJGRnafX3yVyXRUexKgdoh9ofgk6o1bBSknZFaaFqZdXguXqkXUf8DLXVYiGkkkpqY_jm35jtmKtLQazVgYTWcEmmRPRbA-WBCtJNMPHaUwA3ZP7QlT7nxOToMppS9BI2yBy25pJoveVXPycnAd4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی  Rowboat | یه همکار هوش مصنوعی که همه‌چی یادشه!
یه ابزار جالب اوپن‌سورس توی گیت‌هاب پیدا کردم به اسم
Rowboat
. این ابزار در واقع یه «همکار هوش مصنوعی دسکتاپی» هست که روی سیستم‌عامل‌های ویندوز، مک و لینوکس نصب می‌شه. توی اولین نگاه هم شبیه هرمس به نظر اومد، اما بعد تفاوتش رو متوجه شدم.
کار اصلیش چیه؟ اینکه یه گراف دانش (Knowledge Graph) زنده از کل کارها، ایمیل‌ها، جلسات و چت‌هایی که باهاش دارید می‌سازه و با استفاده از همون اطلاعات، کارهای شما رو روی سیستمتون انجام می‌ده.
چه مزیت‌هایی نسبت به بقیه داره؟
بیشتر ابزارهای هوش مصنوعی فعلی وقتی ازشون یه سوال می‌پرسید، می‌رن همون لحظه تو فایل‌ها یا داکیومنت‌ها سرچ می‌کنن تا یادشون بیاد جریان چیه (RAG). اما فرق اساسی Rowboat اینه که
حافظه‌ی بلندمدت
داره:
- اطلاعات و کانتکست کارهای شما در گذر زمان روی هم انباشته می‌شه (مثل حافظه‌ی انسان).
- ارتباط بین داده‌ها و فایل‌های مختلف رو به صورت گرافیکی (شبیه گراف‌های Obsidian) بهتون نشون می‌ده.
- نوت‌ها و یادداشت‌ها تو دلِ هوش مصنوعی مخفی نیستن، بلکه فایل‌های ساده‌ی Markdown هستن که خودتون هم می‌تونید ویرایششون کنید.
-
همه چیز روی سیستم خودتون ذخیره می‌شه
(Local-first) و دیتاتون تو سرورهای ابری هیچ شرکتی رد و بدل نمیشه.
امکانات و بخش‌های اصلیش چیه؟
-
🧠
مغز (Brain):
کل ایمیل‌ها، جلسات، اسلک و چت‌ها رو به یه گراف دانشِ به‌هم‌پیوسته تبدیل می‌کنه.
-
📬
ایمیل کلاینت بومی:
ایمیل‌هاتون رو دسته‌بندی می‌کنه و برای ایمیل‌های مهم، بر اساس دیتای کارهاتون به صورت خودکار جواب می‌نویسه.
-
🤖
ایجنت‌های پس‌زمینه (Background Agents):
می‌تونید ایجنت‌هایی بسازید که مثلاً هر روز ساعت ۸ صبح یا هروقت ایمیل جدیدی اومد، برن وب رو بگردن یا کد بنویسن.
-
🌐
مرورگر اختصاصی:
یه مرورگر ایزوله داره که به ایجنت‌ها اجازه می‌ده فقط به اکانت‌هایی که شما بهشون دسترسی دادید وصل بشن.
-
🎤
نوت‌بردار جلسات:
به میکروفون و اسپیکر وصل می‌شه، صدای جلسه رو ترنسکریپت می‌کنه، خلاصه‌ش رو تو یه فایل مارک‌داون می‌نویسه و گراف دانش رو آپدیت می‌کنه!
-
💻
حالت کدنویسی (Code Mode):
می‌تونه همزمان چند تا ایجنت کدنویسی (مثل Claude Code) بالا بیاره تا بر اساس کانتکست پروژه‌هاتون براتون کد بزنن.
-
🔌
پشتیبانی از MCP:
می‌تونید راحت به هر ابزار خارجی مثل اسلک، جیرا، گیت‌هاب و توییتر وصلش کنید.
آزادی عمل توی انتخاب مدل
یکی دیگه از ویژگی‌های جذابش اینه که می‌تونید مدل زبانی رو خودتون انتخاب کنید. می‌تونید کلید API خودتون رو بدید (مدل‌های ابری) یا اصلاً از مدل‌های لوکال (مثل Ollama یا LM Studio) استفاده کنید تا حتی پردازش‌ها هم کاملاً آفلاین باشه.
پاسخ خود هرمس به تفاوت این دو ابزار:
۱. هرمس (من): یک دولوپر و ماشینِ اجرای تسک
من برای
انجام دادن (Execution)
ساخته شدم. رابط گرافیکی سنگینی ندارم و دقیقاً مثل یه دولوپر سینیور تو ترمینال یا چت تلگرام نشسته‌م. تو از من می‌خوای یه اسکریپت پایتون بنویسم، داکر ایمیج بسازم، یه ویدیو رو با FFmpeg فشرده کنم، یا یه کرون‌جاب تنظیم کنم که هر ۶ ساعت اخبار رو اسکرپ کنه؛ و من مستقیماً با هسته‌ی سیستم‌عاملت (لینوکس/مک) درگیر می‌شم و انجامش می‌دم. حافظه‌ی من از جنس «مهارت» (Skills) و دستورالعمل‌هاست.
۲. روبوت (Rowboat): یک دستیار اجرایی و ناظر
روبوت بیشتر شبیه یه
منشی فوق‌هوشمند
با یه رابط کاربری دسکتاپه. کار اصلیش «نظارت خاموش» (Passive Observer) روی کاراته. تو پس‌زمینه ایمیل‌هات رو می‌خونه، تو جلسات آنلاینت صدای میکروفون و اسپیکر رو شنود می‌کنه تا خلاصه برداره، اسلک رو چک می‌کنه و در نهایت همه‌ی این‌ها رو مثل نرم‌افزار Obsidian به یه گراف دانش (Knowledge Graph) متصل می‌کنه.
لینک سورس گیت‌هاب:
🔗
https://github.com/rowboatlabs/rowboat
لینک دانلود نرم‌افزارش:
🔗
https://www.rowboatlabs.com/downloads
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/4429" target="_blank">📅 22:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4427">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rl0T0ETt5Uuur6R-IOXDUPF9wPdW13ewH6joLSJPJTT1G3JsYRUans4qrjc5FEPMElku7IwoZq_5bCZzk2g5wFddmyJnD7WCsRpE-jkKa5THAWVSwkFdh02Yg2HPOliVE-V6K-YVo7MSQ24GU82aGq3v8ELIvUKChXn4dGUE21mxwOL8qT91B1HLwJOCeVbARREkzI5Z5KM13ZMQuhN0HMfElg_3IyTBkSAOAaTXuphhZDcQFNT1oQqVdqsR4Yanq66Veuhct-yWppaPKmulv_fNDuBvlIjBtCTGbNbPDYawDfsmzaXc_bV08SPApiY5wCm2Its_BpzQzs5MNA4L4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/18c4e8f180.mp4?token=hUrz4j8Hp6Jq7EyAZREg9u-_BLnk3s-gPYvCtiT3k5VNxAj63wHjGvdHU1XzVgLrC0HlBTT7e_uRkkUzn4i5DggTpy8NtO22fUFe9Ce2Gt_J-BKQc5uPv6LVp-3xS0LayUSoEYw1qdN0_ClDc3RxTVjid6IQE64bFeofePa4rdKRkWmo_Fb4V0OTATyYoRl8RhKSgl6gkhhIfYs_4DAPSVCbf2OwJDTYC4G4RKz0jaPFtJF62NLXKVqtRqjJDtH7x2QQOUh5U7SycxD4DvYJcmQBDU4FsTkbvBW3r8KRWipDcSdBNC-TQ7htkrLPjo_3zGJK3DWfYSvxcKhKT8_oWg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/18c4e8f180.mp4?token=hUrz4j8Hp6Jq7EyAZREg9u-_BLnk3s-gPYvCtiT3k5VNxAj63wHjGvdHU1XzVgLrC0HlBTT7e_uRkkUzn4i5DggTpy8NtO22fUFe9Ce2Gt_J-BKQc5uPv6LVp-3xS0LayUSoEYw1qdN0_ClDc3RxTVjid6IQE64bFeofePa4rdKRkWmo_Fb4V0OTATyYoRl8RhKSgl6gkhhIfYs_4DAPSVCbf2OwJDTYC4G4RKz0jaPFtJF62NLXKVqtRqjJDtH7x2QQOUh5U7SycxD4DvYJcmQBDU4FsTkbvBW3r8KRWipDcSdBNC-TQ7htkrLPjo_3zGJK3DWfYSvxcKhKT8_oWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چیزی که برام ساخت خوب بود. میتونم بگم در حد OPUS 4.8 + Claude Design هست. برای وان شات خوب بود واقعا
اون پایین هم زده هرمس باگشه. مدلی که استفاده شده grok 4.5 هست</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/MatinSenPaii/4427" target="_blank">📅 22:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4426">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iMPGsvBLib6cIlWCUi2P30VXbrbpNimzfProfZAoucaU7_nwUktRbneW0Q1F72KFHoHoXjopLeXxBJ4dAOtPJE5GSUKJqMx5sB3PXw9RIbey1AdfdVvaTmBsxI-tQMxzIU4AFBIepXNesKbxpwLQLv8GPOAM7TfsV2ma_YIJIkur6EzpecBAY7qEqzPef9Xxc-WvOkLWKgT-06joVUafFleRv_2FtLnbpi8w4e4EzbrkoTvg2qxiUvYMWh5KEcdqau7dq_AbUBsq_4LV9gCEKgR-pkvVfNMWeEnc4RB5Mr7F_-BVnhxKqRHeDHltAAim3mt3ggJaGo1eGvfh5LsIRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با atomic mail یه اکانت ساختم بهش وصل کردم مجددا
😁
روی سرور</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/4426" target="_blank">📅 21:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4425">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/my4cwgiXVl6VI6fvHCNwyuV-U5eHrVYD7sEPtAVyPxnQy9EGFHLx0rGyDW0OWPkPCdg0eeQl3jrBRijuHeWiO2NKW05K-TC1gAWdMOTBI8S8vuvw4mVNfDj460jwYQih6s4eiLXWGpNjOyUnsEcrihjMihkM7NfVfOuppSaeRkQFqUzjQOAzWbgtQjktzWBwaUXn8TYWOzlZJkUzRqB6f3ubeoxBJHRL6J13B_cdRl57yA8Kb-bKKzdZWguadyI73CakrtNpS0nFHeOtU-aSFHy0KKdqrm0JF6n4-26lqqEFtcgXH7xIIJzY8-U9pVMgcQC1TpPntbkWAikV_NSpGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با atomic mail یه اکانت ساختم بهش وصل کردم مجددا
😁
روی سرور</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/MatinSenPaii/4425" target="_blank">📅 21:31 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4424">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دقت کنید روی ویندوز حتما باید proxifier روشن باشه که روی ترمینال هم تانل بشه وی پی انتون</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/4424" target="_blank">📅 21:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4423">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گویا روی grok cli می‌تونید با Context 500 هزارتایی به مدت محدود ولی به صورت رایگان از Grok-4.5 استفاده کنید(قدرتش هم سطح Opus-4.8 بوده توی بنچمارک‌ها) نصب روی powershell ویندوز:  irm https://x.ai/cli/install.ps1 | iex نصب روی سرور:  curl -fsSL https://x.a…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/4423" target="_blank">📅 21:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4422">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eGDSj0QKpDFpbYMmSJwhiddLx-QO0XK1KZ6NKtJePfSjvIPHJ3f_jaS8YtkDSc9ZZGNg-Dr6EQReTxb_25RT369Mk1akiL4kJrw_aLAXs8T_nDT8AsuNMc9GEbOW7JJLSM_fdhElSP4mb2NlANedbeEOIQFFJq24xGaTBU9wsXPl8DNNSBVZRXpCmBl3ztTHuiFkAhBusCfi6qtYq2hpqhS-2SdKlxo5Y-yb9CARmDByN64la52raEeCN9Dy4EiyQEXNkdVQvwwL2ziT0c2Adlc1dzVHH0SKupES3IZ-B2G5a5Jq8tcrOKcEEtQHNFzFwmgcVSfz64V5kMgEKSWEYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا روی grok cli می‌تونید با Context 500 هزارتایی به مدت محدود ولی به صورت رایگان از Grok-4.5 استفاده کنید(قدرتش هم سطح Opus-4.8 بوده توی بنچمارک‌ها)
نصب روی powershell ویندوز:
irm https://x.ai/cli/install.ps1 | iex
نصب روی سرور:
curl -fsSL https://x.ai/cli/install.sh | bash</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4422" target="_blank">📅 21:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4420">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/D6fc_qic7-ZjrvUePI87cR4EfKzHdBESDTMm7328OBCXXWD8c_XWygJmVOwhd60x5bjXBfSdK2T7dkfnbwDmv1jxBDevLYBTrcbsiqWEX5qKkF8XaJYgHV_ll4yN3RkfczeggLOaodWKFjbNhWb969W-rP_rBtimt3YkDneVue-Leb2SadRJ6TKCapG5aqxvZ5-2ZU1tOYEiUR_LE22bXlG_X0z1eQyQUQr6ilK5d57kN9YZGrhCAEaXvdu3mvm_eVS9HhqyUlpKLqGpCEdwL99_h-F3eLqmjx0iKRNCW8JlDi2A_XET7IoYpYkwBCpuSpfx4CO3sGdFbgTkwQx1Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qqxwCj-4uFlljKaZLWQrvU2cuNjJZMw0iUi8qX_kKN3arRrNKy0hNTgWEmw5nFQbGseZJtOBrkdDGb35kzIzZ19ALgKYKakjVas1HB47Zo1tQ1r_tDJcxDsMVSx-gt5RyiVH63Pm2NqJEhQpO6SiYPbdzHA43_UhnFpSKjEIiMBOSPLLI45mE3MV1PRRVwP0Hcdtp1zldWQsh_mTv-nyh4UfGBaGI4rcoNpYOjB8V-s7t-2Gt23KRZCXWVylOWtXFzxRbXzGvjDimZLKCmHJjfdZ2YhqTHGVQj5g86Q-g8Ldbx4D7QPrBeRgyUjv6zw4M07U6A7iu_44nR75akAcWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فکر کنم راه استفاده از Meta AI بدون خطای ریجن رو کشف کردم!
با کلی IP مختلف (حتی آمریکا)، اکانت با شماره آمریکا و جیمیل تست کردم ولی بازم ریجن می‌داد.
اما با سرور آمریکا Mullvad خیلی راحت باز شد (حتی اکانتی که با جیمیل ساختم) و کار می‌کنه..
البته اگه مشکلی پیش نیاد :)
++ با فیدبکی که بچه ها بهم دادن ، با windscribe و Surfshark هم نتیجه داده
✍️
AmirHossein JPL</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/4420" target="_blank">📅 21:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4418">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Otr9cikmRCYDFLzq7JOFhCYh_sgRBxxGKwcXPboaXGvM-ZhoTZ38ekmYf_F83hJ0DRsBfTLCqee-yPEspC-JJVkLzVTOhUwF4Ifi9GCiYjuz8rtgECm-YiJD-CfIufg60QNqBuHgb0qaw9jsW33MfcsiFBA2TLsHvCNlv3XUSSUqmWe0t2F-Exg9P8nUAlUEwCJcRffCncnbJyS8nfkk58TZEQf4K8KwR2N3lGwcl3O5X1uaEiPedGUFgKj8PxACouHiYTSHndmAti9cgpYVhZ4ujmmFtcUwNhNw8LeSJRbhQPSM6n2dfB8dhnghgNoQcPGGbZbnzP8jcBBqrcHUHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UM8-rCyOtF-ZTyCPktuPAHcOYpi-m2mVcaaATO9G-GG3wUY37zmnVOSFwClF-UDonTx8VQ4Es92IQzmxquaueSpAwdlUCK3R5o7EBPUWrBBfFuFilzEqgg9vLQgQTp5lvyjwSCHMmLU4sUWtdYujJDdf0HetbnfNHmoeyizFxHgf6d7mRnjGaSg6nwBeelulOgdcS8lVLaPX2pjVZrayoORBFNwstTutQUCLJIp0AHH6Fc-vfhf42sLxrRlZ6rEhKIqGyUwMQXAGXgAYOzknFv_u7TOQiOoWIQwgXK6E9HhEw0opxOn6bMTOOIWWanrBidxCmD08FKwoL4P15CEcCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مأموریت شکست خورد بچه‌ها
فقط اون جمله‌ای که آخر گفت</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4418" target="_blank">📅 12:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4417">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/goeKYV068GRhAgNywIXM27GUIQwDR93PDeaKNsYL0gWINQYSxVf0lKahjvYCrO4kQuc4V-RztWdb6hKIDKINMKfBSer3sC-EWFLgKeYgiIj8zncfQARJaWcnssdTe5Oo64WuxVddK-PU3NteIgIpiE2p-AIETBzOyGaPC-V0ZWZRiXZncKHBV47Ye4awne0A8SMZLkfF0KYJ_-qog04HLQGFdk_aqxc0UEplgFJGnkH_MKOJTg6J_AqdqbfAow3SBcVqQNuSRpPDcR4AxymFtfMxRvE7Kur1QT7uGxs_ryRw5mbuRh2X8xliz4SrU28BBa_ljDWDHPxxlYnLI_EK6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4417" target="_blank">📅 11:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4416">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گویا برق قسمت‌هایی از اهواز رفت.
دلیلش هم حمله به زیرساخت برق بیان شده.</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4416" target="_blank">📅 03:15 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

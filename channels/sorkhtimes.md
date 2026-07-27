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
<img src="https://cdn4.telesco.pe/file/vP-6_qDtNeRC8pQMHUYdqrWO0NT6C0u-IY6vAmDbFOmJ8HmnDTj69JQdg1rQ0HThugrjzWKcWwlusRxb9DBu9AL1fF78alIAEDgcw5PrPB3p2MrGWJ3SFjVM2mZZYscKOTBeWZo8H5K0J9fzpGQdyN4BkfggooAGyQpSxkWdRuw97Oqhb90HNUOiA35hl_X9jWYdpeP-WLoSM0gjq52_q3v7QPcE4IvUKRT2ntcjtUzmxdq0zbgOuFB239qI9e7bDmu2Az97nBAUUJu013d50wCxYWqfC3QXUJvm0DbkC3MjSl_h4JQXAtAUWWsndU4apSCWSgSgcUDvZgLJBHPs2w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 22:22:38</div>
<hr>

<div class="tg-post" id="msg-136853">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🤩
#تایمز_توئیت
❌
هر روز برای من مطالبی تحت عنوان افشاگری از مدیران باشگاه میفرستن که بیشتر شبیه فیلمنامه هاست
⁉️
وقتی هر روز یه روایت جدید از نقل‌وانتقالات میاد، آدم نمی‌دونه مدیرعامل کیه، سرمربی کیه، دلال کیه، خبرنگار کیه، منبع آگاه کیه!
❌
یه عده میگن فلانی توافق کرده، یه عده میگن نه، یکی میگه پول نیست، اون یکی میگه پول هست ولی نمی‌دن، یکی میگه لج کرده، یکی میگه اصلاً از اول قرار نبوده!
❌
باشگاه رو انگار گروهی دارن با ریموت کنترل می‌کنن؛ هر دکمه دست یکیه، فقط دکمه «اعلام خبر قطعی» خراب شده!
❌
خلاصه تا وقتی هیچ سند و خبر رسمی‌ای منتشر نشده، این مدل روایت‌ها بیشتر شبیه فیلمنامه‌ست تا خبر. ولی خب برای جذب فالور و دعوا راه انداختن، ظاهراً از هر نقل‌وانتقالی جذاب‌تره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 642 · <a href="https://t.me/SorkhTimes/136853" target="_blank">📅 22:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136851">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">➕
بعد پنج سال به این نتیجه رسیدم حداقل نصف هوادار هامون متعصب،ناآگاه،هیجانی،و تو دنیای موازی هستن و اغلب دنبال کری خوندن و دلقک بازی
➕
هیچ فهم و درکی از فوتبال حرفه ای ندارن و چشم گوششون به دهن چهارتا از خدا بی خبر بچه ساله که گوشی گرفتن دستشون میگن لنگش کنید، هوادار واقعی پرسپولیس رو سکوعه که لب دهن نیستن اونی که تو گرما و سرما از تیمش حمایت میکنه و بالا پایین این تیمو دیده و به مسائل اشراف کامل داره، یه عده فقط لب دهن مجازی هستن و ساخته شدن تو زمین رقبا بازی کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/SorkhTimes/136851" target="_blank">📅 22:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136850">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🫦
کونده رفته به ایجنت ایری و طاهری گفته به بازیکن هاتون بگید استوری بزارن… شما که پول نداشتید گوه خوردید این دوتا رو خریدید به امید اینکه این وسط یه پولی گیرتون بیاد ولی فعلا کیر خر دستتون داده بانک شهر… به قران خود بازیکن ها هم ذی نفع بودن وگرنه هیچ کصخولی…</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/SorkhTimes/136850" target="_blank">📅 21:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136848">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🗣
خیلی اینکاره این
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SorkhTimes/136848" target="_blank">📅 21:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136847">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🗣
خیلی اینکاره این
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SorkhTimes/136847" target="_blank">📅 21:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136846">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⚡️
شهاب‌زندی‌مدیرعامل‌باشگاه نساجی مازندران:
◻️
تا فردا شب تکلیف دانیال ایری و کسری طاهری مشخص خواهد شد. باشگاه نساجی حسن نیت خود را برای انتقال‌این‌دو بازیکن به پرسپولیس نشان داده وحالامدیران این‌باشگاه باید تصمیم بگیرند که واقعا دانیال ایری و کسری‌طاهری…</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SorkhTimes/136846" target="_blank">📅 21:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136845">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6K23ShxVd7fafdbLz_8VlOak-zqCHk_VR_G2cBtdg0QjRw2a5Lbbt5Pdg2E2LQnUsfR4LY3yJvGB8qbwv4EiF0CuTLVANZUbjDgGrOrX6po2xVZz_qUNX7oj8fFlyZwEgC1jp_C-Fn7PfGWaL1TmGw3M2dWg25WwxSMlMIv_0bexbgTyvgNFNTHHzXpGh4d8ASNUezzQbJPkC8FPCWM2a761Ovo8PXKhRkrguJ-L_5exEsw_oYveIZzDo9ryANLW1p1BH11MgpIL8xlRr3fdG6F5LqbPUl1f5vWhlNN2tcm1JfneH80SzrCRHKgYU6Yp-fQp-MDfA-TKSN5pDb7eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
شهاب‌زندی‌مدیرعامل‌باشگاه نساجی مازندران:
◻️
تا فردا شب تکلیف دانیال ایری و کسری طاهری مشخص خواهد شد. باشگاه نساجی حسن نیت خود را برای انتقال‌این‌دو بازیکن به پرسپولیس نشان داده وحالامدیران این‌باشگاه باید تصمیم بگیرند که واقعا دانیال ایری و کسری‌طاهری رومیخواهند یاکه خیر!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SorkhTimes/136845" target="_blank">📅 21:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136844">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
✖️
✖️
آنا: یاسر آسانی به سرنوشت دیدیه اندونگ دچار شد و تحت هیچ شرایطی نمیتونه تا نیم فصل برای استقلال بازی کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/136844" target="_blank">📅 21:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136843">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6Q6gzOSHp7oyM1EqOUh-jNtsIEZPsdMZO89mQmjz8wJOEhR3gPZcdyEe7zRlk2fXZWm_TVkeues72mLkl0MP4VxZ1eq4sLkG592TahDBfwuzdaUop6Rpr0DipAwrXrgp26r_wq7Qf9yg6MS-bHymUekdSZkxHfO2NDT_VykUtTJTSsFnpr-JijEB2jjxeqZw5Z_vDZBgRYSpuAOl43PW0zxUkQz5TcQihPLsVFsihCrFZxTcFZ5BBfgEiUED10iK93f7-c384m9ckbsb6gpAuxu05dIRNQk_JQdHR7ooJRXuzL0lncSxOx5w9QB7PrMJGsy086QbcO7cYWBXb8k2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
👋
گل رو پیدا کن و جایزه ببر!
🧐
وقتش رسیده تا دقت و شانس خودت رو به چالش بکشی!
⚡️
همین حالا وارد سایت شو و حدس بزن گل زیر کدام لیوان هست و شانس خودت را امتحان کن!
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/136843" target="_blank">📅 20:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136842">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‼️
پرسپولیس میخواد رفیعی رو برای بازگشت راضی کنه؛ کاری که خیلی سخته چون امیررضا میخواد جایی باشه که بهش بازی برسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/136842" target="_blank">📅 20:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136841">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
❌
☹️
ادعای ترامپ درباره ایران:ما در حال گفتگو هستیم و به نظر می‌رسد که اتفاقات خوبی ممکن است رخ دهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/136841" target="_blank">📅 20:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136840">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
❌
#فوری | ترامپ:
🔻
برای دیدار با مقامات ایران به توافق رسیدیم
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/136840" target="_blank">📅 20:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136839">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔹
🔹
🔹
فوری/کانال ۱۴ اسرائیل:
🔹
ترامپ دستور توقف تمام حملات به ایران را تا اطلاع ثانوی صادر کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/136839" target="_blank">📅 20:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136838">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">#شفاف_سازی
🔖
🏅
نساجی دانیال ایری رو پارسال ۷۰ میلیارد از ذوب آهن خریده الان زندی گفت ۱ میلیون دلار بدید…پول زور
❌
کسری طاهری ۷۰۰ هزار دلار خریدن گفتن ۸۰۰ هزار دلار… باشگاه میگه با همون ۷۰۰ هزار دلار رو میدیم
❌
باشگاه اگر ۸۰۰ هزار دلار بده هم تا نیم فصل نمیتونه…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/136838" target="_blank">📅 19:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136837">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔄
🔄
گوهری گزینه ی گلری پرسپولیس نیست/قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/136837" target="_blank">📅 19:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136836">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
🔴
پرسپولیس برای جذب فرهان جعفری از نظام وظیفه استعلام گرفته و اگه مشکلی نداشته باشه میاد پیش خودمون/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/136836" target="_blank">📅 19:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136835">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🎶
🎶
🎶
صادق محرمی طی روز های آینده از تراکتور تبریز به صورت رسمی جدا خواهد شد و احتمالا به پرسپولیس بازخواهد گشت/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/136835" target="_blank">📅 19:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136834">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🔱 Hero 🔱</strong></div>
<div class="tg-text">همه چی رو کنار هم میزاری میبینی کسری طاهری و دانیال ایری و مدیرعامل نساجی و دلال این بازیکنا در کنار بنگاه دلالی ورزش سه دستشون تو یه کاسه هس و دارن آخرین زورشون رو میزنن برای تیغ زدن باشگاه صب ورزش سه خبر میده کنسل شدن الان بازیکنا خیلی یهویی با دستور دلال هایشان استوری مشترک میزارن هوادار هم که خدارو شکر سوار موج میشه</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/136834" target="_blank">📅 18:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136833">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">#شفاف_سازی
🔖
🏅
نساجی دانیال ایری رو پارسال ۷۰ میلیارد از ذوب آهن خریده الان زندی گفت ۱ میلیون دلار بدید…پول زور
❌
کسری طاهری ۷۰۰ هزار دلار خریدن گفتن ۸۰۰ هزار دلار… باشگاه میگه با همون ۷۰۰ هزار دلار رو میدیم
❌
باشگاه اگر ۸۰۰ هزار دلار بده هم تا نیم فصل نمیتونه…</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/136833" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136832">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⭕
هرکسی از ننش قهر کرده گوشی دست گرفته کانال هواداری زده هر کصشری میخان میزنن، اون حروم زاده ها اگر میخاستم بیان پرسپولیس چرا رفتن نساجی؟! صدرصد هم خود بازیکن هم ایجنتشون با زندی بستن
‼️
یکم عقل تون به کار بندازید خداوکلی چرا هرکس هر کصشری میگه طوطی وار تکرار…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/136832" target="_blank">📅 18:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136831">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‼️
🥇
آقای مدیرعامل بزار چند صباحی از پرونده عظیم فساد تون داخل باشگاه مس رفسنجان بگذره… بعد ادای آدم های سالم و مظلوم رو در بیارید
❌
هر موقع پای میز مذاکره زورشون نمیرسه پول مفت بگیرن که از روش بخورن به هوادار دنده میدن، هوادار هم که ماشالله مسائل رو تجزیه تحلیل…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/136831" target="_blank">📅 18:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136830">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‼️
🥇
آقای مدیرعامل بزار چند صباحی از پرونده عظیم فساد تون داخل باشگاه مس رفسنجان بگذره… بعد ادای آدم های سالم و مظلوم رو در بیارید
❌
هر موقع پای میز مذاکره زورشون نمیرسه پول مفت بگیرن که از روش بخورن به هوادار دنده میدن، هوادار هم که ماشالله مسائل رو تجزیه تحلیل نمیکنه شروع میکنه کوبیدن باشگاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/136830" target="_blank">📅 18:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136829">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOw7oDt4C62TP4G_47jhqpl_jRnKTSguisABiV0mcuv_qJMNbs4NQIA3RzPRckKIw36Y9iCyjGZnbHOxg-GH2lvtxl-XuO6gWGnMfj3szG4OOtecekyRl7_FrLk9WANBugrlTYrIeFWSQ3wrSCMVJ89CwiDwoXLHY3GMDQDGJt-ElUfJHrtWATrtUrbzt0x9mH8WVwT_gO9Z73MbcMyzDylADX02YVNTPk7hYZw1wTu5VDsXikftAosp59azb35MKWSVEbCi_XT0tKU_RUfEYUmupHmquGfhe-TkJFRMrmxZno8SgpRSeBiudBLN6vPDkN0G83T0gGhxBKw7-E3Szg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیرانوند اصلا دانشجوی دکتری نیست
🔺️
رئیس مرکز ورزش و تربیت بدنی دانشگاه آزاد گفت آخرین مدرک بیرانوند، کارشناسی ارشد است و او حتی دانشجوی دکتری هم نیست.
🔺️
پیش از این بیرانوند در تاریخ ۵ خرداد ١۴٠۴ و در برنامه فوتبال برتر ادعا کرده بود که دانشجوی دکتری است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/136829" target="_blank">📅 18:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136828">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">⬅️
⬅️
⬅️
حسین پنبه‌کار:
🌀
شهاب زندی از صبح در دفتر باشگاه استقلال حضور دارد و مراحل نهایی جذب دو بازیکن جدید در حال انجام است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/136828" target="_blank">📅 18:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136827">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔄
🔄
ماهم مانند شما بلاتکلیفیم و خبر قطعی و رسمی نداریم و این شرایط برای خودمان نیز آسان نیست؛
🔴
🔴
ما نیز میخواهیم هرچه زودتر تکلیفمان مشخص شود تا به فوتبال و آینده خود برسیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/136827" target="_blank">📅 18:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136826">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emOnL3qgPadRcFr7u2yo0Ythf3dkBFJMNLOBu5dvM6Y4PHUe-PwDsQAOhKbcHnFbFdlWivN4r1-G970qmkYEfenBhLjacVXhzdK7OcPmGoZ5cehWbZjH2htPUnbuO4nnMnuiExWjHVKYYCT2kpJ6nubf691jF5jW4EIGuqjqW7qSUXFSR1KrKA2EfPLgNjpdXRr_q8j4gUfXcTSoXNchMuQaTfpZLM_SIkI8jou7yfFAOBE70K04QcqSYB--Czitexh9MNGdl_FenHeP4KsnobOlEqoz6k6NkeIoEfm3kydLj1iiIbodc5F69fk9klvQA64psdK3-mnUxvRP7aIh8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
📸
آغاز یک روز پرفشار و همراه با انگیزه سرخپوشان در اردوی ترکیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/136826" target="_blank">📅 18:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136825">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔄
🔄
استوری مشترک کسری طاهری و دانیال ایری برای هواداران؛ ماهم مانند شما بلاتکلیفیم و خبر قطعی و رسمی نداریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/136825" target="_blank">📅 18:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136824">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔄
🔄
گوهری گزینه ی گلری پرسپولیس نیست/قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/136824" target="_blank">📅 18:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136823">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
🔴
🔴
انتقال دانیال ایری به پرسپولیس نهایی شده است.
❌
اما جذب کسری طاهری هنوز قطعی نیست و نهایی شدن این انتقال به حل مشکلات حقوقی بستگی دارد. //خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/136823" target="_blank">📅 18:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136822">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
❌
❌
امیر عابدزاده که به تازگی بازیکن آزاد شده و احمد گوهری از گزینه‌های باشگاه برای گلر دوم می باشند ناگفته نماند وضعیت اخباری همچنان مبهم است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/136822" target="_blank">📅 17:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136821">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">⚪️
⚪️
⚪️
انتقال کسری طاهری به پرسپولیس فعلاً نه قطعیه، نه منتفی. سرخ‌ها علاوه بر دردسرهای قانونی مربوط به قانون «پل»، بابت مصدومیت رباط صلیبی قبلی این بازیکن هم نگرانن. پرسپولیس تأکید کرده بیشتر از ۷۵۰ هزار دلار برای طاهری هزینه نمی‌کنه و تا وقتی از نظر حقوقی…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/136821" target="_blank">📅 17:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136820">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
باشگاه استقلال پیشنهاد 5 میلیون دلاری آسانی رو قبول کرد و این بازیکن شنبه به ایران برمیگرده !!!
😕
😕
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/136820" target="_blank">📅 17:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136819">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
پرسپولیس و تراکتورسازی پشت پرده توافق کردن که پرسپولیس بیخیال قربانی بشه و تراکتور هم بیخیال محبی تا باشگاه های اماراتی بازار گرمی نکنن و مبلغ رضایت نامه رو نبرن بالا
😐
/ فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/136819" target="_blank">📅 17:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136818">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
🔴
🔴
انتقال دانیال ایری به پرسپولیس نهایی شده است.
❌
اما جذب کسری طاهری هنوز قطعی نیست و نهایی شدن این انتقال به حل مشکلات حقوقی بستگی دارد. //خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/136818" target="_blank">📅 17:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136817">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
❌
محمد قربانی: پرسپولیس و تراکتور مرا میخواهند/ مبلغ رضایتنامه‌ ام ۲۰۰ تا ۳۰۰ میلیارد است
🔴
🔴
بهتر بود نام تیم نیاورم، اما حالا که سئوال میکنید، میگویم. هم پرسپولیس و هم تراکتور با من و باشگاه الوحده مذاکره کرده‌ اند و در نهایت باید ببینیم ظرف روزهای آینده…</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/136817" target="_blank">📅 17:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136816">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">😳
😳
😳
😳
😳
😳</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/136816" target="_blank">📅 17:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136815">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">😳
😳
😳
😳
😳
😳</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/136815" target="_blank">📅 17:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136814">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
🚨
قدوسی اعلام کرده یک مقام از باشگاه منتفی شدن دانیال ایری و کسری طاهری رو رد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/136814" target="_blank">📅 15:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136813">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
⚪️
🔴
#فوووووری
⚪️
⚪️
منتفی شدن انتقال کسری طاهری و دانیال ایری به پرسپولیس
🔴
🔴
طبق پیگیری‌های ایسنا از مسئولان نساجی، مدیران پرسپولیس حاضر به پرداخت مبلغ درخواستی از سوی مدیران نساجی برای انتقال این دو بازیکن نشدند تا انتقال آن‌ها به پرسپولیس منتفی شود.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/136813" target="_blank">📅 15:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136812">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">📎
📎
📎
یه سوال پیش میاد اگه واقعا حس میکنید هنوز تو دفاع راست مشکل دارین پس عیدی چرا جذب شد؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/136812" target="_blank">📅 15:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136811">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
⚪️
🔴
#فوووووری
⚪️
⚪️
منتفی شدن انتقال کسری طاهری و دانیال ایری به پرسپولیس
🔴
🔴
طبق پیگیری‌های ایسنا از مسئولان نساجی، مدیران پرسپولیس حاضر به پرداخت مبلغ درخواستی از سوی مدیران نساجی برای انتقال این دو بازیکن نشدند تا انتقال آن‌ها به پرسپولیس منتفی شود.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/136811" target="_blank">📅 15:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136810">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVDTGeIl_FAO1wDluT5llLVFKGGOHOl6aW4f12LKSXu6E6Bt7jQ2Ukk7MXmjNiA50aXUNQ7_YGdXm-9JK9EooaddxmrT8ikpSkXjmzQAZ9ESu2dmMZ9QL8yT_nQ8LjiAtX_DT9VKCecaMJoBiJYF_itSxMvcmMCzXVZ9gswoYrWShbSoDT2aNtWbab4DN-3ELiVw-uWskeOamoFws3h6E5KOAollqTs7DlOtVRTwm2-8U6aH4toh6COoWahApwmit8w2wieL_5XNn8qtSkOx7B8KY3DBUgHI3vjVCEE4j-TTb5WQYXsdKfejytzn236_YBeVcmft68cEuMxEe3w94Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کاظمیان به گل‌گهر پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/136810" target="_blank">📅 15:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136809">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">⬅️
⬅️
⬅️
حسین پنبه‌کار:
🌀
شهاب زندی از صبح در دفتر باشگاه استقلال حضور دارد و مراحل نهایی جذب دو بازیکن جدید در حال انجام است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/136809" target="_blank">📅 15:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136808">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⬅️
⬅️
⬅️
حسین پنبه‌کار:
🌀
شهاب زندی از صبح در دفتر باشگاه استقلال حضور دارد و مراحل نهایی جذب دو بازیکن جدید در حال انجام است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/136808" target="_blank">📅 15:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136807">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
⚪️
🔴
#فوووووری
⚪️
⚪️
منتفی شدن انتقال کسری طاهری و دانیال ایری به پرسپولیس
🔴
🔴
طبق پیگیری‌های ایسنا از مسئولان نساجی، مدیران پرسپولیس حاضر به پرداخت مبلغ درخواستی از سوی مدیران نساجی برای انتقال این دو بازیکن نشدند تا انتقال آن‌ها به پرسپولیس منتفی شود.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/136807" target="_blank">📅 15:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136806">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGZ6z13Ec937pOUvdqplKvVCZV1teffAgBemlaEPICSYM4Xlq7hmQHE5u2SGaBLpJeiOZFSDZR1saCtC1R5h13T1gy8ZfSbZuGtEFLGnqdWE9NwUJuzm2FRWoWeYY0bho0cBhN7dmEHeHU5zS-iXyDx9xQ4Acqp0lwx16Gng7n0588PTEq5EeJ65IAcIpDb4RgcpUUQz26ChhpBhBlPy-O9ZJDlfS66YjB1XcxFOENjLRHwOoQyW5DDsFYbbwA8udrZRboafTG35hlmyYXdM4yMfM8UiHvO3hpcYHBWDxCg2Q9DD9z_9YM4Fg8gCsIE1190mwSYAggjO57RQKSV5og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
وقتشه پوکرو حرفه‌ای بازی کنی!
🎰
اگر به دنبال تجربه‌ای متفاوت و پر از هیجان هستید، بخش کازینوی وینکوبت بهترین انتخاب برای شماست. از بازی‌های کلاسیک مانند بلک‌جک، رولت و باکارات گرفته تا صدها اسلات جذاب با جوایز بزرگ، همه چیز برای یک سرگرمی حرفه‌ای فراهم شده است.
🕹
همین حالا وارد دنیای کازینوی وینکوبت شوید و هیجان واقعی را تجربه کنید. شاید برنده بزرگ بعدی شما باشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/136806" target="_blank">📅 14:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136805">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
❌
باشگاه نساجی گفته از اقدام پیمان حدادی به شدت ناراحت شده و میخواهد دانیال ایری و کسری طاهری را به باشگاه های دیگری بفروشد
😀
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/136805" target="_blank">📅 14:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136804">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‼️
پرسپولیس میخواد رفیعی رو برای بازگشت راضی کنه؛ کاری که خیلی سخته چون امیررضا میخواد جایی باشه که بهش بازی برسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/136804" target="_blank">📅 14:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136803">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
شنیده‌ها: با توجه به عدم جذب اخباری احتمالا یا رفیعی برگرده یا گوهری که بازیکن آزاد جذب بشه
🚨
پ.ن: برای گلر دوم رفیعی یا گوهری هم جوابه بعید برن سراغ گلری که قرارداد داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/136803" target="_blank">📅 13:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136802">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
🚨
باشگاه تراکتور پاسخ هایجک محبی رو به پرسپولیس داد و محمد قربانی تا ۷۲ ساعت دیگر تراکتوری میشه/ ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/136802" target="_blank">📅 13:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136801">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
به دلیل تعلل مدیران باشگاه پرسپولیس در جذب کسری طاهری و دانیال ایری حضور این دو بازیکن در پرسپولیس از سوی شهاب زندی مدیرعامل باشگاه نساجی منتفی شد /ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/136801" target="_blank">📅 13:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136800">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✅
🔴
پوریا لطیفی فر ستاره 22 ساله تیم‌گل‌گهر با عقد قرار دادی چهار ساله رسما به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/136800" target="_blank">📅 13:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136799">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
به دلیل تعلل مدیران باشگاه پرسپولیس در جذب کسری طاهری و دانیال ایری حضور این دو بازیکن در پرسپولیس از سوی شهاب زندی مدیرعامل باشگاه نساجی منتفی شد /ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/136799" target="_blank">📅 13:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136798">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/136798" target="_blank">📅 13:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136797">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/136797" target="_blank">📅 13:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136796">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
عجیب اما واقعی؛ پرسپولیس و سپاهان داداشی شدن و پیمان حدادی کمپ شهید کاظمی رو در اختیار سپاهان گذاشته تا اونجا تمرین کنن…!
☹️
☹️
🫥
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/136796" target="_blank">📅 13:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136795">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vzcv7iUKsSJkNJiQbienR-e7-X9gI8YHGsJFaeeXJP2ODNeL26eSsO9sZ1DV6a7SjH-a4IbVB1vfao9kmJMh8JnOK6dX6KRuikvLwh_6FyshXCQoBapdtE7qDrbomhn3ylJO9vZkcVXjANPDkWMxOSB8FGOZWcaIK_IMVqrHeTdnPomI3EwZTZZLG0A6mqh9lphwvDVqiibKqriO2xMAM3AmZpjKhJx2Xk-flsKoen7GSUPhdJn4nzOTplhXSFFbYAcPtpNY_c8PGiMY79pDgnXtsqo8o-gWA3JegnPHdhQ0BCFoiQWBG32EXK5AAEX9YU0tpDyjmm_OvU4KtHi0PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
باشگاه سیرجانی با انتشار تصویری از محمدرضا اخباری به صورت رسمی اعلام کرد این دروازه بان با قراردادی دوساله به گل گهر پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/136795" target="_blank">📅 13:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136794">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
❌
#ورزش‌سه : ممکن است به زودی یک قرارداد معاوضه به اضافه پول نقد بین دو باشگاه پرسپولیس و سپاهان شکل گرفته و احتمال دارد نام‌هایی مانند محمدامین کاظمیان، حسین ابرقویی و آریا یوسفی در این معامله جای پیدا کنند. حتی احتمال رخ دادن این اتفاق برای محمد عمری نیز…</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/136794" target="_blank">📅 13:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136793">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgF-ORp9V4ZScewcrI8MStYnKo1mR9s1Ey7-zYovSDhRq1V4paIzMcvNArazAgxApXgwmkXaS3q1WGFG6lZiLFyxNVlNSbw412COwcUGT9BhfEeY25WScJcROXpCHfNkJdqPT2FMAiAXhlc_03F8blUGN6mjnVZPZA0VNkGi4uujnI_6obqeQByaVrzzdVwxXDM54NX_JU43OwdxtkldtOKDFcZIBxjpqBQpLcsdWytM3qLpee_bzZkP2fQST19TIM8MIsT5oEB683RegzfrbgYBDeB77O2uoohTMEbA8gfAJ62xJNZ1e5a9wV1fRrolMelyfbd2OfkNGtcQLbovCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووووری :
محمد قربانی به تراکتور پیوست!
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/136793" target="_blank">📅 13:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136792">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">➡️
➡️
➡️
➡️
⬅
تارتار به دنبال پاکسازی پرسپولیس!
⏳
💬
مهدی تارتار پس از بازگشت از ترکیه قصد دارد چند نفر از اطرافیان باشگاه را به دلیل لو رفتن ترکیب تیم کنار بگذارد.
⬇️
سرمربی پرسپولیس به چند نفر مشکوک شده و پیگیر این موضوع است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/136792" target="_blank">📅 10:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136791">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
🔴
ورزش سه: هیچ کدوم از هافبک های پرسپولیس بازیساز نیستن و دو خرید جدید پرسپولیس در این پست (لطیفی فر و پورعلی) بیشتر وظایف دفاعی دارن. پرسپولیس اگه پست 8 بازیکن نخره تو شروع فصل به مشکل میخوره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/136791" target="_blank">📅 10:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136790">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
❌
❌
امیر عابدزاده که به تازگی بازیکن آزاد شده و احمد گوهری از گزینه‌های باشگاه برای گلر دوم می باشند ناگفته نماند وضعیت اخباری همچنان مبهم است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/136790" target="_blank">📅 10:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136789">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🌀
🌀
🌀
پرسپولیس خواستار جذب مدافع تراکتور شد
🌀
باشگاه پرسپولیس با ارسال نامه به باشگاه تراکتور خواستار جذب صادق محرمی مدافع تیم فوتبال تراکتور شده است.
🌀
محرمی پیش از این سابقه بازی در پرسپولیس را داشت و از همین تیم راهی دیناموزاگرب کرواسی شد.
🌀
باشگاه تراکتور…</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/136789" target="_blank">📅 10:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136788">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
صادق محرمی درخواست خروج از باشگاه تراکتور را داده و قصد ندارد فصل آینده در این تیم باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/136788" target="_blank">📅 10:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136787">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✅
گل پرسپولیس به تیم مصری توسط بیفوما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/136787" target="_blank">📅 09:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136786">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
فرشید حقیری: یاسین سلمانی دیروز پشت دروازه تمرین کرده و احتمال زیاد می‌ره مازاد تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/136786" target="_blank">📅 09:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136785">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❗️
❗️
لیست تیم ملی امید اعلام شد.
❌
در این لیست 4 بازیکن از پرسپولیس به تیم ملی امید دعوت شدند.
🔴
امیرحسین محمودی
🔴
علیرضا همایی فرد
🔴
سهیل صحرایی
🔴
فرزین معامله گری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/136785" target="_blank">📅 09:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136784">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
❌
خبرنگار پرسپولیس:
🔴
امروز محمدمهدی زارع و پویا پورعلی در تمرینات عالی ظاهر شدن .تیکدری هم مثل همیشه خوب بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/136784" target="_blank">📅 09:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136783">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
🔴
گزینه بعدی پرسپولیس برا گلر دوم گوهریه آماده س ولی برخلاف اخباری سهمیه لیگ برتری  حساب میشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/136783" target="_blank">📅 09:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136782">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxFEMFAH9Qr6QkghIB9OuYfBmwUxjTpJwGgR4kzkAnrpRaI27yA6t1NGR_hNxK2MrWG9tgEURiyM-nn_RVQFgPbE2KN8gOB9r9dUD2lFTc2k-63yR_wqYph7zyqiWQlRWRQxYlGjhQw6ftlGxkU_Qe2NbsWDxaC3zYOYY-7mL9634ujpR9Gpefz6Rw-zU6AxBKuER3HxSiqOuuFfi-47eowfJ0Rfmd_hhmyo56RIqP5yypfdDpvrsedKUwfc0xKC68MU38DQzE5W3tt6-g2dvmVN2Xvu4vv9BlXao3GGVjnmmifHt5ptkhicJCkOHInOdaBAvAaKYZ0I2M2B8w_3BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کریم باقری : پرسپولیس فصل گذشته مشکلات زیادی داشت و من خودم شخصاً جزو کسانی بودم که از عملکرد و نتایج تیم راضی نبودم اما نسبت به فصل آینده امیدوارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/136782" target="_blank">📅 09:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136781">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYjiFlCKB6luPVrow9pc-_ooPrwuoiZti4NU-M7v-i1kwkkKlZaVfIoenVz6qoXc6X0NPDH1GhuSdn1LhacoaaK8lLiX3G1a9HVprmvivpZgv1vsiJtW8HzBiBUqzoVo6QZvHnETlt6Im46Pf4rKpLi8vYfYakD_D8g0-mTCfZulsjL96esjt-iBAehB6fAt_LMNZBPLI39nWDQrNCBCaDvwNkb-pfEH9UjOdA5PDhOdp2-nzSo1ZVf8Ar7eTw2DuRGmlEEyvgndlwTSHlXmCNSYOmCNb9qrCAIFvQ7mx57c-6s4M3TTLylQoViMT_O0wSrI0AH-U0ynU2lUg8JOKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبح 5/5/5 تون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/136781" target="_blank">📅 08:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136780">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSb4DlJoBape-NCihCfJ3qne9VtbylsdSrN4nC9atlqdiK7iFbnuKiIkhq4zs4gh75GxQd52NaDrbwdlSnoe4-Gv2V8tqXt_V6sLiVlxqrywfk7qe9Qc3P7g8lv77bYNYb6gpZ25EGQknROi34hWMXa0THPzVHW1bL8Kcjr7VM8ZVqv0Hg_x2x0le3wznZK2JG6CVED4rGsBSB-xuVd-RCZoQB6KyFM2EG0kKXulQkunNo8uxfuuTmz2v7REF2YeO2eW5aKweWEjoUTYdfAY7gjszaI8e9ixtAEDO7mtwZV2S76l8Is_DS40JKaKdkpRCsiNfFvTI10uItyo1DiUDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
ربات وینکوبت در دسترس تمامی کاربران
🟢
بدون اینکه از تلگرام خارج بشید میتونید مستقیم وارد سایت و بخش بازی‌ها و کازینو بشید، پیش‌بینی ثبت کنید و براحتی واریز و برداشت انجام بدید.
📌
حالت Mini App داخل تلگرامه و خیلی سبک‌تر و سریع‌تر براتون باز میشه:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/136780" target="_blank">📅 01:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136779">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✅
✅
✅
نظر شخصی :یا به گندمی اعتماد کنید که  الان تو اردوی تیم هست .یا رفیعی و برگردانید ...یا به امثال آرشا شکوری و آرمین عباسی اعتماد کنید و جذبشون کنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/136779" target="_blank">📅 00:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136778">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">➡️
➡️
➡️
➡️
⬅
تارتار به دنبال پاکسازی پرسپولیس!
⏳
💬
مهدی تارتار پس از بازگشت از ترکیه قصد دارد چند نفر از اطرافیان باشگاه را به دلیل لو رفتن ترکیب تیم کنار بگذارد.
⬇️
سرمربی پرسپولیس به چند نفر مشکوک شده و پیگیر این موضوع است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/136778" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136777">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
❌
تارتار اسم یه مهاجم خارجی رو به باشگاه داده و درصورت جدایی بیفوما و گرا مدیریت برای جذبش اقدام میکنه/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/136777" target="_blank">📅 00:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136776">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/136776" target="_blank">📅 00:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136775">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/136775" target="_blank">📅 00:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136774">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✅
مهدی طارمی: این جام‌جهانی فاجعه بار است، فاجعه‌ بارترین. فیفا باید هر مشکلی را که وجود دارد، حل کند. اما متاسفانه از همان ابتدا نتوانستند چیزی را حل کنند. اکنون دوباره برای رفتن به تیخوانا سفر خواهیم کرد، بدون ریکاوری. این منصفانه نیست. اگر این از نظر فیفا…</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/136774" target="_blank">📅 00:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136773">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
❌
وکلای باشگاه پرسپولیس گفتن جذب کسری طاهری خیلی پر ریسکه! باشگاه پرسپولیس مجدد از یه وکیل خارجی داره مشورت میگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/136773" target="_blank">📅 00:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136772">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
در حرکت رونالدینهویی هایجک خوردیم و اخباری رفت به گل گهر و شاگرد رحمتی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/136772" target="_blank">📅 23:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136771">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔘
🔘
امیر عابدزاده هم تنها گلر بزرگسالی هست که سهمیه لیگ برتری محسوب نمیشه چون لژیونر بوده   جذب گلر بزرگسال اشتباه بزرگیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/136771" target="_blank">📅 23:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136770">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔘
🔘
امیر عابدزاده هم تنها گلر بزرگسالی هست که سهمیه لیگ برتری محسوب نمیشه چون لژیونر بوده   جذب گلر بزرگسال اشتباه بزرگیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/136770" target="_blank">📅 23:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136769">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
شنیده‌ها: با توجه به عدم جذب اخباری احتمالا یا رفیعی برگرده یا گوهری که بازیکن آزاد جذب بشه
🚨
پ.ن: برای گلر دوم رفیعی یا گوهری هم جوابه بعید برن سراغ گلری که قرارداد داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/136769" target="_blank">📅 23:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136768">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
در حرکت رونالدینهویی هایجک خوردیم و اخباری رفت به گل گهر و شاگرد رحمتی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/136768" target="_blank">📅 23:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136767">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">⚠️
⚠️
اخباری قرار بود امشب رسمی بشه ولی انگاری تماس مهدی رحمتی باعث شده به فکر رفتن به گل‌گهر بیفته ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/136767" target="_blank">📅 23:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136766">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🫥
🫥
حالا باید بگردیم دنبال دروازبان مطمین برای ذخیره پیام ...حالا چرا این وسط چرا رفیعی رفت دلیلش معلوم نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/136766" target="_blank">📅 23:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136765">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
در حرکت رونالدینهویی هایجک خوردیم و اخباری رفت به گل گهر و شاگرد رحمتی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/136765" target="_blank">📅 23:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136764">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_TYNYd8wbkWO6gi1PfeVy-8W3lx1fRje6i6Ndsv3TjLr0ZMXf4x0UpS_-z-3of9dcf1DPQuOIdMe-dduTZcdNpX0ivK0EsuHf_Irlati37pPNBrRD7eOCqawTEy8eRoChRSjZ01-sHdJ8RrHCV3D2wDZAQfLUFIOPLCxTIOpBeYL2gvotHPWWpnxcbfCiUHEhrhMDinGEPhi5IwXikkdCEzhA9h7t7lpV9PrYBCySAxMaow8cGjSFkHLjCqSUZvmC9hAKWWVGpwO5LLx4yKX8ILFXEs0oQtk6-I52UVrVxsxBP1dd1fwpJGu4qeQSRkxwqf2nkrHgjbsGutV4ZqaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
📸
از بازی دوستانه امروز با نماینده فوتبال مصر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/136764" target="_blank">📅 23:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136763">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
در حرکت رونالدینهویی هایجک خوردیم و اخباری رفت به گل گهر و شاگرد رحمتی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/136763" target="_blank">📅 23:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136762">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
در حرکت رونالدینهویی هایجک خوردیم و اخباری رفت به گل گهر و شاگرد رحمتی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/136762" target="_blank">📅 23:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136761">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
🚨
محمدرضا اخباری تا دو ساعت دیگه قرارداد شو امضا می‌کنه / قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/136761" target="_blank">📅 23:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136760">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔻
⚽
ویدویی از حال و هوای پرسپولیسی‌ها در اردوی ترکیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/136760" target="_blank">📅 23:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136759">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🕹
هیجان واقعی کازینو؛ جایی که شانس و مهارت به هم می‌رسند
!
🎰
اگر به دنبال تجربه‌ای متفاوت و پر از هیجان هستید، بخش کازینوی وینکوبت بهترین انتخاب برای شماست. از بازی‌های کلاسیک مانند بلک‌جک، رولت و باکارات گرفته تا صدها اسلات جذاب با جوایز بزرگ، همه چیز برای یک سرگرمی حرفه‌ای فراهم شده است.
🎰
چرا کازینوی وینکوبت؟
• تنوع بالای بازی‌های کازینویی
• میزهای زنده با دیلرهای حرفه‌ای
• گرافیک و کیفیت فوق‌العاده
• بونوس‌ها و پیشنهادهای ویژه
• محیطی امن، سریع و کاربرپسند
🕹
همین حالا وارد دنیای کازینوی وینکوبت شوید و هیجان واقعی را تجربه کنید. شاید برنده بزرگ بعدی شما باشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/136759" target="_blank">📅 22:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136758">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🟠
🟠
🟠
مهدی عبدی در لیست مازاد مازیار زارع قرار گرفت.
✅
✅
چه بلایی سر خودت آوردی پسر..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/136758" target="_blank">📅 22:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136757">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
فووووووووووری و رسمی؛ رای نهایی دادگاه پژمان جمشیدی صادر شد و نتیجه آزمایش تجاوز منفی اعلام شد و پرونده بازیکن سابق پرسپولیس و فوق ستاره فعلی سینما مختومه اعلام شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/136757" target="_blank">📅 22:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136756">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
ویسی:
❌
اومدیم که امتیاز بگیریم و میگیریم
🎗
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚩
⭐️
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/136756" target="_blank">📅 22:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136755">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❗️
رامین رضاییان نام استقلال رو از بیو پیجش پاک کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/136755" target="_blank">📅 22:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136752">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4nJb379ACft7kIFwwh9H0UOqif4HlxyhhbK0OCpm28m1bY8aGZTXkEQ4IRicMoum6mwINbxNRArj1JSqZ0nRw36aKSn_jmbgTqfT7H_3_Bjjgk6r8_38v0_v8dFUF1UVVKyK3FHBoGEsszWpLNAR_6dCw-6Lp0uVmP9D1xEdQ9P3vWNNbrbHrYbKO8cNKHvs2cv0RQXrycj1UE9BsKSIJeJkQuXKeN7FSUMfWtRiYZgzhxgjsyT7TYzoiyxIFDHEeVz53brZrbNPX8sCEl4L4PgnP1Q0uEpPT0nk2j7J1ZNxe4kRmu57Ol57lk6mStmYB73ff3JGeMAD0I3p68Q8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فووووووووووری و رسمی؛ رای نهایی دادگاه پژمان جمشیدی صادر شد و نتیجه آزمایش تجاوز منفی اعلام شد و پرونده بازیکن سابق پرسپولیس و فوق ستاره فعلی سینما مختومه اعلام شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/136752" target="_blank">📅 20:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136751">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726dada166.mp4?token=mpTgbw8sPG7el_bYz6a7du8-EOEBX3Yx_itTfyz5yWb8FEUGd7bXLUYXuWswx-n3V_0yvKAbQeI5eysniCB2tIXIFCsyhDPC_wecZJxoLu9s7Uzk507Gy3Whz4Kf_0lToMSaCPlIGT8H1V3s1ifWJHT4808mGhfWz_Z527RtIY_ufZQvd4GKvGKpO360iwR_tGx4xay9L2bQDttAV6dpo5Gj7P4TjMlg_aq-Ie_iI_S7BiGrVRYeAjHg3ftrIFMKHVmQYN0Hysog5Oj_XrSxV0R3ksAT9U5NPX-o9Ng0GCkQhBVwL2cJ6Ul9FRcXq1H4GYCEiYmXyxErhAtxyrPqgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726dada166.mp4?token=mpTgbw8sPG7el_bYz6a7du8-EOEBX3Yx_itTfyz5yWb8FEUGd7bXLUYXuWswx-n3V_0yvKAbQeI5eysniCB2tIXIFCsyhDPC_wecZJxoLu9s7Uzk507Gy3Whz4Kf_0lToMSaCPlIGT8H1V3s1ifWJHT4808mGhfWz_Z527RtIY_ufZQvd4GKvGKpO360iwR_tGx4xay9L2bQDttAV6dpo5Gj7P4TjMlg_aq-Ie_iI_S7BiGrVRYeAjHg3ftrIFMKHVmQYN0Hysog5Oj_XrSxV0R3ksAT9U5NPX-o9Ng0GCkQhBVwL2cJ6Ul9FRcXq1H4GYCEiYmXyxErhAtxyrPqgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
گل پرسپولیس به تیم مصری توسط بیفوما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/136751" target="_blank">📅 20:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136750">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">⚡️
⚡️
🚨
🚨
🚨
🚨
فووووووووووووری
✅
محمدمهدی محبی نهایتا امشب یا فردا قرارداد شو امضا می‌کنه
🔽
تمام توافقات با کلبا نهایی شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/136750" target="_blank">📅 20:49 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

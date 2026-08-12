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
<img src="https://cdn4.telesco.pe/file/JnD4FpKP6RkHAVy2jSvlN67E1sV3MadOIrwXHe85QaKX7q7bSXUjy15wVVIiSGBUb7LuI4sy60XT9pOzx80W4bBLmexS36nshkVsyHHIQsjrevv2vXlZHnURuvInzAiup4AW1Y-K-rJk9Xwf4ckNr2yI7PlQWoCe3vyXM4y2yeyCfIKEd3e2PDTAsBlH5hXQDZY4fpSY6aXK_cW_cltUtm0vreX0nqd6sR2X0ByoHkkrzVhAl2dFHTI_89WOgN5tUfNendZNp29xg4bEZrlPwrUonJy7M5nAmruvmJLAtjPrtfSQFPl-cjwwmDmvArXW3jHy3B5iAyEYs00mt-fcTg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 966K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 21:44:00</div>
<hr>

<div class="tg-post" id="msg-141368">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
یک فاجعه در راهه  گرونی بنزین فقط به معنی گرون شدن بنزین نیست،یک دومینو از اتفاقات فاجعه بار اقتصادیه…  امشب یک تحلیل مهم راجب بنزین و تاثیرش  روی تورم و سرمایتون داریم</div>
<div class="tg-footer">👁️ 3 · <a href="https://t.me/alonews/141368" target="_blank">📅 21:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141367">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
منبع ارشد ایرانی به المیادین: تنگه هرمز باز نشده است/ اخبار فیک ترامپ برای کنترل قیمت بازار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/alonews/141367" target="_blank">📅 21:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141366">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
رویترز: دولت لبنان ممکن است از نیروهای خارجی برای نظارت بر روند خلع سلاح حزب‌الله دعوت کند.
🔴
لبنان و اسرائیل بر سر معرفی بریتانیا، ایتالیا، سوئیس و اندونزی به‌عنوان کشورهای احتمالی مشارکت‌کننده در سازوکار پیشنهادی برای راستی‌آزمایی خلع سلاح حزب‌الله توافق کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/141366" target="_blank">📅 21:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141365">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAloMedia | پخش زنده ماهواره و مسابقات ورزشی | اَلومِدیا</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/BpU52udGS0PyhqBIbK6x60hFWdNtds9KqIEdy3clrJ-xxHUlOyKjKOrbltwbLKjUyNvcydoGlTpfNfq0gADE_LfcOA31HbQTDIJ1Tj4AWASASQiO32z1RJukwwgYZQUOVU_L5V0S9mjaOdzPgwnkt1W44hlbc3eBOE9r1Ogp-d5UCJSoqOA17wtwPfg1MDDJSLyOjp1MrmqJh86KiW3UrOlEtknrtJoAyUxnasXdeDVGW81IM8XtYvpiIrd-Fh1au-awJXRWYE4wFVE2BOC1vlChEb-BKKRERaru_mrJjW-DjvQbJBdecPrAywhLnSL6uBqkIesFFmrk_pPIXAfPUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پخش زنده بازی‌های امشب
▶️
رایگان ، بدون سانسور ، کیفیت FHD
🟢
شروع پخش زنده
🎁
😍
۵۰۰،۰۰۰ تومن شـارژ رایـگـان، هــدیـه‌ به کـاربـران جـدیـد
⛓
همین حالا ثبت‌نام کن</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/141365" target="_blank">📅 21:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141364">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه پاکستان:
اسلام‌آباد به دنبال بازگرداندن تهران و واشنگتن به میز مذاکره است
🔴
طاهر اندرابی، سخنگوی وزارت امور خارجه پاکستان تأکید کرد که کشورش به تلاش‌های خود برای بازگرداندن تهران و واشنگتن به میز مذاکره ادامه می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/141364" target="_blank">📅 21:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141362">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUvF1DnvmAuVG32-BeJTBn-Pz2WERfwq8uefWulnXe8Q-irXzTmTk_VW_Q-6LmCeR7lfqXmsPyTYLGpKLmoqrbdEkxWe9CDPL4TLgn8GjarRK2IvCz2MJmXp610Ijol2rM0dRyzh9jNF7MzhEmNSwWNdttUv3MzdHDlZbMWazRFP-w5ekhfEuglT_iHdd9BX1ESbJXMANoZJwi2ytnylL7BZVeM5AiiSpa2ed6vwRjb88t2QbPZpnwRT_0M19IdojZ-UJzGf5BrlNAP7B9EyNCAOYsihdcyPa5O_nh7Lf7S0J3hSpFRyA9dhA57hqMguHCJ7NsDvCeYr2xzhC5MlDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
نرخ چهارم بنزین از راه رسید
‼️
🔴
نرخ اول: ۶۰ لیتر بنزین با نرخ ۱۵۰۰ تومان
🔴
نرخ دوم: ۵۰ لیتر با نرخ ۳۰۰۰ تومان
🔴
نرخ سوم: ۴۰ لیتر با نرخ ۵۰۰۰ تومان
🔴
نرخ چهارم: ۸۷,۲۰۰ تومان
🔴
گفتنی است این طرح هنوز به طور رسمی در کشور اجرا نشده و فعلا محدود به ۲۰۴ جایگاه سوخت در استان کرمان است.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/141362" target="_blank">📅 21:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141361">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
اتحادیه اروپا و ۲۶ کشور دیگر با صدور بیانیه‌ای از ایران خواستند اقدامات معناداری برای تضمین رعایت حقوق بشر انجام دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/141361" target="_blank">📅 21:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141359">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
سفیر پاکستان در مسکو:  سفیر پاکستان در مسکو تاکید کرد اسلام‌آباد هیچ مخالفتی با پیوستن ایران و مصر به توافقنامه دفاعی مشترک با آنکارا و ریاض تحت عنوان توافق مکه ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/141359" target="_blank">📅 21:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141358">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6shTVWDaQV5wOY8s8snZ-8d6fDa-_aFZjkcFVJ4EQEnheHYh9D0MXUVQ2BWUwUFtrgeHH4WYrjk2OPHOEpscotU_w-GcWbWyb2FnW-QFZh5741bAr8xuJ1RdKuva072ndUHsPXZBGmZwdnYjxgFwPi1wI5b3hoDLQmuY2MUlNhfV7aRPob90M3H3wdNVncSPkCMtnntOYEEmqs9gH1nKlYUBKBgBklJQOaaQwk-SKBnEw3nRPIH3QqGnhoyY4b_e5K_VVsVga61JMy9NyVHEjtwohRrQZg5BMgzSJAIHZ86vtTjAXebYND0xnX1-q_73qK-gEyPm2rLHUo9I00aaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز: 2 تا 3 نفر از خدمه ناو هواپیمابر آبراهام لینکن در اثر فشار روانی طولانی شدن مدت اعزام این ناوگروه به بیش از 8 ماه، اقدام به خودکشی با پرتاب خود به سمت دریا کرده اند که همگی آن ها توسط دیگر خدمه یا نجات یافته اند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/141358" target="_blank">📅 20:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141357">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
به دلیل درگیری و نا امنی در تنگه هرمز ، میزان درآمد کانال پاناما سه برابر شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/141357" target="_blank">📅 20:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141356">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iykp7bUXz9tvryYw5yNJuj_SSFPdqYvps76oJVCkEDWfJdH06YTIiwje6c6Bz3DVelObDmzhsZwGBi5JJSX2ttYFLvNPZuCYM_9P1dbCDkcix45keITNXTD6lAn_x6kMhJ23fA4qh5SKmxQuL-OeY-gK2VMqqodNJ6SPzfoiaTAkoApuQTg43okfUjBUjEJIOqdi2uR6iDYA1tPez2mAolZAedqokfl46S8FcPXvBHSYg9mo1-gpygYr-Bv2K36_UWT90K8e0hVbarArtIYmImcaca12kByulmu7uwqjaKa2E6E8Um5CPxgGf0_C-65lBQ3SMcdPNg5FA_gEN4ILQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اولین واکنش احسان خواجه امیری به درگذشت پدرش
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/141356" target="_blank">📅 20:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141355">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fadc935aa1.mp4?token=s2aUueezw8aeeS_J4Q5xIH0PWClyDDP-YhcA96yL3BMSgGOwrgRa-w4_YJqZ7r7nNXUZkKl_p67vuq8pXk3UGdimCmtM6kE-C5Wu_LXZfZBtyVFrDvr3CWkg7DDGjl3xgQSIsiFU5fqQkTnRNv2EQuBfZVc8GLZArTUZADVmUimhjoRK5ouBZ3o79zkLXPwgvgSvG--l-EdkCymCoodzkeEgo9qJUWO5fCWvvwuf8_Hg5o8EZOHL_I97K0-eOWKOi2gIHGf5P4Hyid8hfI6ZKyWdkmKR0PaCUOgvAuI79rS3aBCS9y2PdOUtJF1mCn3j4xxqGmI2Moi0yBWM-F_MfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fadc935aa1.mp4?token=s2aUueezw8aeeS_J4Q5xIH0PWClyDDP-YhcA96yL3BMSgGOwrgRa-w4_YJqZ7r7nNXUZkKl_p67vuq8pXk3UGdimCmtM6kE-C5Wu_LXZfZBtyVFrDvr3CWkg7DDGjl3xgQSIsiFU5fqQkTnRNv2EQuBfZVc8GLZArTUZADVmUimhjoRK5ouBZ3o79zkLXPwgvgSvG--l-EdkCymCoodzkeEgo9qJUWO5fCWvvwuf8_Hg5o8EZOHL_I97K0-eOWKOi2gIHGf5P4Hyid8hfI6ZKyWdkmKR0PaCUOgvAuI79rS3aBCS9y2PdOUtJF1mCn3j4xxqGmI2Moi0yBWM-F_MfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سفیر ایالات متحده در اسرائیل، مایک هاکبی، در مورد  ایران: ترامپ نه تنها ثابت کرده که مایل به بمباران آن‌ها بوده، بلکه همچنین مایل به ورشکست کردن آن‌ها است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/141355" target="_blank">📅 20:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141354">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
بلومبرگ گزارش داده ایران با بازسازماندهی ساختار نظامی و امنیتی خود، به‌دنبال ایجاد نیرویی تهاجمی‌تر و آماده‌تر برای درگیری‌های طولانی‌مدت است. این تغییرات می‌تواند نشانه‌ای از آمادگی تهران برای مواجهه‌های نظامی آینده باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/141354" target="_blank">📅 20:17 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141353">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b1765ff5a.mp4?token=H32y7gf5cJdcYmJEX0V5R1jZhxvYUjkzUUyQj5EpXadeaJjxHsYDTk9BWrOq_MJDjyb233bXQRU-UUBd5lr9D9E9VnhNruzq41kC2fZqP9Z8yVcriIfOqM-yTkMO0Px6I1qoLGWiPJmJjmNpLq8qEQS1fUn2jN4VRxYhvlNkdNvrz9CjAnd2WQYSFx6XcUL5ZFm7r9sxMkyrZCZEJLBwCQwGwJfjH247znOPLi-gqVYZ09LabL6u0nHzxrBOgpIb15apQEiDsDl2XDj_JuC7rRJQ_MWRMh5e6zYC2AgtPSCTwa1OyJ9T-1SagqEpOPnVDFzzJS6Aawu0RE_9fZh-GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b1765ff5a.mp4?token=H32y7gf5cJdcYmJEX0V5R1jZhxvYUjkzUUyQj5EpXadeaJjxHsYDTk9BWrOq_MJDjyb233bXQRU-UUBd5lr9D9E9VnhNruzq41kC2fZqP9Z8yVcriIfOqM-yTkMO0Px6I1qoLGWiPJmJjmNpLq8qEQS1fUn2jN4VRxYhvlNkdNvrz9CjAnd2WQYSFx6XcUL5ZFm7r9sxMkyrZCZEJLBwCQwGwJfjH247znOPLi-gqVYZ09LabL6u0nHzxrBOgpIb15apQEiDsDl2XDj_JuC7rRJQ_MWRMh5e6zYC2AgtPSCTwa1OyJ9T-1SagqEpOPnVDFzzJS6Aawu0RE_9fZh-GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بوریس جانسون ادعاهای مبنی بر اینکه سفر او به کی‌یف در آوریل ۲۰۲۲ مذاکرات صلح اوکراین و روسیه را خراب کرده است را «کاملاً و بی‌شک دروغ محض» خواند.
🔴
او می‌گوید هیچ رهبر غربی نمی‌توانست مانع از جنگیدن اوکراینی‌ها شود.
🔴
و پیام او به زلنسکی ساده بود: اگر می‌خواهید بجنگید، ما همراه شما خواهیم بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/141353" target="_blank">📅 20:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141352">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
وال‌استریت ژورنال به نقل از شرکت کپلر: نیمی از کشتی‌هایی که در ماه اوت از تنگه هرمز عبور کردند، مسیری را که ایران اداره می‌کند، انتخاب کردند.
🔴
از میان ۱۶۶ عملیات عبور، تنها دو کشتی مسیر تحت حمایت ایالات متحده را انتخاب کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/141352" target="_blank">📅 20:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141351">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
فارس: کنوانسیون خزر سهم ایران را از ۲۰% به ۱۱% و حتی کمتر کاهش می‌دهد!
🔴
همچنین امکان بهره‌برداری از میدان‌های نفتی مشترک مهمی را از بین می‌برد و دسترسی ایران به بازارهای شمالی را با مشکل مواجه می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/141351" target="_blank">📅 20:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141350">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/141350" target="_blank">📅 20:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141349">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvNxpApsoITvFiiuuDdpS8Rd0CWAncdWDXSMEDIv3MayvcPl1_FOS3zEVra6q0rbliiYQI9npTmhe-vnxKCqJGZRvZEC0PREHLoC6VvCHiVL9ecg4DB8_WJ4SaHGVucjAqK0C4k_5X3r8lV9hJYi6HM7fAsoR-GPA6Quk1bLYYPJkFbQdN6pjgwUNb5gPDGHIB_6uzx04PN8cZXcJhL2bJha58CmLFyXMTZchl_ihdThjO3PN2dzX19ReKuqRKUutUsEi5U4FF7tuzOAVuK-oSd6u3X5c8C_Uv7h3KZsdeZna83aXpkBW4mKRrBVY4YTIrNEcvYA0m7z7SQmwCoUug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚘
✨
رضائی موتورز
✨
🚘
خرید و فروش خودرو | ترخیص سریع و مطمئن
🔹
خودرو: ملی | گذر موقت | مناطق آزاد
🛳
ژنراتور: ارسال و ترخیص
🌍
صادرات و واردات قطعات و تجهیزات
⛴
ترخیص کالا از ایران و امارات
📌
بهترین قیمت، سریع‌ترین خدمات
📲
موجودی و قیمت روز وارد کانال شوید
👇
👇
https://t.me/rezaei_motors
https://t.me/rezaei_motors
https://t.me/rezaei_motors</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/141349" target="_blank">📅 19:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141348">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZM1Lh2Q6s7svYJdR4_w1IK8sF63rvbnYe6jffOV8CqLsnZjSF0sW3SUPOkPHa1HgGe4CbjcDmNvF6OIly0_dlW4OKzU-FKrjUrNpvTV3spXpPdDCyOllFmxci03goFZE0GzLndUQ0_MKkiotCajtUF9bZHPpPWE1SUqA3UaA_Kl89agCUhuy4a4plvb2OJ56xjXogl5BSrwj92SIBHRo4mBppw2Z26j9iRC0Ajdumg8iP8EoPxmPtgSxeChQzqj7olJ0G14VO5wol3eI16hYmNlf2MpXUsF2mbX3SvlP3dh8nScgEjF5aSK4O8GwRyqGXY2xI-tqSleWQf7RrXEhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی فالح الزیدی» نخست‌وزیر عراق و «براد کوپر» فرمانده سنتکام در دیداری رسمی، بر سر توافق کامل و نهایی جهت پایان دادن به مأموریت نظامی ائتلاف بین‌المللی در خاک عراق توافق کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/141348" target="_blank">📅 19:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141347">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
سازمان محیط‌زیست عمان اعلام کرد لکه نفتی ناشی از نشت یک نفتکش به گل‌نشسته، به سواحل جنوب‌شرقی این کشور رسیده است.
🔴
این نهاد رسمی هشدار داد آلودگی نفتی پس از سرریز از نفتکش آسیب‌ دیده، به نوار ساحلی جنوب‌شرق عمان گسترش یافته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/141347" target="_blank">📅 19:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141346">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
مشاور ارشد قالیباف: آمریکا و اسرائیل برای یک حمله نظامی پیش از انتخابات سراسری در اسرائیل و انتخابات کنگره آمریکا در آبان ماه، آماده می‌شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/141346" target="_blank">📅 19:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141345">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
العربیه: میانجی پاکستانی برای تمدید ۶۰ روزه آتش‌بس ایران و آمریکا در تلاش است و نسبت به آن ابراز خوشبینی کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/141345" target="_blank">📅 19:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141344">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
شرکت آلمانی TKMS: در پی جنگ علیه ایران، شاهد افزایش تقاضا از سوی کشور‌های خاورمیانه برای ساخت شناو‌رهای نظامی بوده‌ایم
🔴
یکی از حوزه‌هایی که این افزایش در آن به طور مشخص دیده می‌شود، فناوری‌های مقابله با مین‌های دریایی است
🔴
همه توافق داریم که روایت و برداشت امنیتی در منطقه تا حدی تغییر کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/141344" target="_blank">📅 18:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141343">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
فارن پالسی: پیمان مکه، نظم منطقه‌ای بدون ایران می‌سازد
🔴
نظم منطقه‌ای مورد نظر ایران، بدون حضور خودش در حال شکل‌گیری است‌‌. تهران مدت‌ها خواهان همکاری بیشتر میان کشورهای مسلمان بوده است. اما پیمان مکه چیزی نیست که مدنظرش بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/141343" target="_blank">📅 18:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141342">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ee4191cae.mp4?token=hYi1Nd3s0F7_lbAMUz_r8sbv6Pj7h4FgCeqyYIojVjI6uORDXyMIs91fj9p5z4yS3pWM0qDQZnfOCvf8tKehI0V4Q13ispS-KwIRwrr32fm7F7zGWhk3NTuhSSsrjA6AjWlkpptQ3wr7TbNKnNaL03eu9muLPiFFy2pJ_Am4HNyh63Ae9vuxQySTrDFz2-xIBZoXijgKheVWaXenycRLyl0em4mLZ9sxtvcbTL2FdvvD5X5fHYeR-KZRgtFQf6gEhVQZhAEm3HMaDy7GJ2YMTv0Dk3Zu0K6iOveHyL5MQHvxZY_s7E_ulhAtDDMIbcNbtHrMYfTwh1gZ2OyFcfz5dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ee4191cae.mp4?token=hYi1Nd3s0F7_lbAMUz_r8sbv6Pj7h4FgCeqyYIojVjI6uORDXyMIs91fj9p5z4yS3pWM0qDQZnfOCvf8tKehI0V4Q13ispS-KwIRwrr32fm7F7zGWhk3NTuhSSsrjA6AjWlkpptQ3wr7TbNKnNaL03eu9muLPiFFy2pJ_Am4HNyh63Ae9vuxQySTrDFz2-xIBZoXijgKheVWaXenycRLyl0em4mLZ9sxtvcbTL2FdvvD5X5fHYeR-KZRgtFQf6gEhVQZhAEm3HMaDy7GJ2YMTv0Dk3Zu0K6iOveHyL5MQHvxZY_s7E_ulhAtDDMIbcNbtHrMYfTwh1gZ2OyFcfz5dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فوران آب پس از شکستگی خط‌ انتقال آب به بجنورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/141342" target="_blank">📅 18:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141341">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
نخست وزیر عراق: تصمیم برای پایان ماموریت ائتلاف بین‌المللی در عراق در تاریخ ۳۰ سپتامبر، تاریخی قطعی و غیرقابل بازگشت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/141341" target="_blank">📅 18:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141340">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqqHhHUEvrZRgq6HLxMwDGpBUpCEUAXmIeZGWU8vSQ2gwd5ZFTGwKqIG_KYijFTMi8Q5D6a7mkMpUT2zxBUpkQPogyZsXMFvjHAWO6BcoVoGV_Kb4wywSEQEN1w_GfPgsgVfxUcv9yerRDc_zEXjUTbnM4VzXUPs8FuAJiChA7P9ULI8DWVU1QT_X_k8EVFK92PXY-H3wdw41EN_MB9XNoeaehUGvD3MNyEb03F0zr-vtLCQAGFojvKVelougM5xCZ7pYWsLPVO3z9uQNXV171AHvh9YSw3ND5sMokYeUR-YaifuAytMghXK_LF3oogVfCNLCVQ-Lqp--QPscnNYrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز ۳ اتفاق نجومی قرار است همزمان در آسمان رخ دهد: خورشیدگرفتگی، هم‌نشینی ۶ سیاره و اوج بارش شهابی
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/141340" target="_blank">📅 18:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141339">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
سی‌ان‌ان: وزارت خارجه آمریکا سفارت‌های منطقه را برای شرایط جنگی آماده می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/141339" target="_blank">📅 18:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141338">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLhahD6r2u32csu_jv97cQ3ofltwjSYOsrhuDw0Bc1mhWLrQHB2EGG1HiMiH5OM4P83L8WkjTEM-_jd-pEPfDYvGIFf_M1bJ0EXSRzXiQkz4rzg8jpR0OS_lhu_De5kADaSLWpHT_RiCsT0Tb5G5CJHsaLviJck7IZwy_BI3DvzPoy3sM8p2mg-d5BJQaVFmmh7aXeG6Xv7XhMSEeS3AbA9M3lu5Bl9gc0KuIurql90DHmobzk7hFLWF1RxUz8KwuR-seQu3OozyneUMXJb05tn9hDfacvFWHCN7dCmh7rZVcQKErOiCbB5tmJMQdXgAJd55PlnqfKYgd2CgOis_YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابراز همدردی کریستیانو رونالدو با کامنت زیر پست لیونل مسی
🔴
لئو، در این دوران سخت، آرزوی سلامتی و آرامش برای تو و عزیزانت را دارم. امیدوارم قدرت و صبر داشته باشید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/141338" target="_blank">📅 18:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141337">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBCGEaZqnVWj-n18eofz3rO1X_p_9-SubDSRAewWqREF8IOx2Zdy8Bn1f_goxQuppb_ASHQO_Z2c_P9MNM6k8kPSn8r3l8Xtna8v1lm4HhcKM22OmGCSjvNW6cyTbuRVCe-lAA_CzNpeCullAF5KeEbxDkqrxyDyOsmWlPcQf3Lcd6q86S5PuWNRer25R3CR5dR01jIGLyfF4LrT_USqHP9iY61H7MQxB8O_TW-e2Xrp_FkfD9rUEKR-EP8I_hjhKTfCsmjJorgHPfTe-ErU2NhuTpWKHykDSrUw1TLA3aOo4m9yNyGIJJBqC9zBIXge0291sS6CALSn310qmLoi9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
آمریکا کنترل کامل هرمز رو در اختیار داره
- فکر می‌کنم همین کنترل رو حفظ کنیم! محاصره دریایی ما رو همه «دیوار فولادی» صدا می‌زنن و ایران هیچ کاری از دستش برنمیاد
- ایران دیگه نیروی دریایی و نیروی هوایی نداره، نیروهاش حقوق نمی‌گیرن
- سپاه هم نابود شده و در حال فراره رهبرانش هم در بهترین حالت، وضعیت نامشخصی دارند
- ایران پولی نداره و کشورش از هم پاشیده؛ فقط اخبار جعلی و تورم ۳۰۰ درصدی براش مونده که روزبه‌روز هم بدتر میشه!
- ایران فقط حرف می‌زنه و دیگه قلدر خاورمیانه نیست.الحمدلله!
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/141337" target="_blank">📅 18:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141336">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل: ارتش برای دفاع از کل اسرائیل در منطقه امنیتی در لبنان، سوریه و غزه باقی خواهد ماند.
🔴
به ارتش دستور دادم تمام اقدامات لازم را برای آمادگی جهت حضور طولانی‌تر در منطقه امنیتی لبنان انجام دهد.
🔴
ما زیرساخت های حزب الله و تمام خانه های منطقه امنیتی را نابود می کنیم و اجازه نمی دهیم شهروندان ما مورد تهدید قرار گیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/141336" target="_blank">📅 17:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141335">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwaadsZRdyMrDFm5cRb-PI0L57G6OhknpXOZqO_fBWyhapN-cbinpO5j2yCjZp1l02xsVC2SkLio84ZKVYdlCJx1ENjbqaY5HFcHVgXOFyKQLkjLLJM-EpIKz16bn7vMgUwu9FfO93MkKlQ1lySC7kION1XyWzM95ebdaR0oSxSDxrCl1WEvxFYcbTqRRBtaLN0Z39vxYgzbQ2CqQ0pPUMcCjEXJPgLqT_Jizwnyo8A4okeMINOeDhbuJFlW71xpHmeEpj15W7Mq78Jh8Bo4y7luCs1nXqIkj7whDKe8q2r-CM5MCFCdY4yHV-9HL4jFatoPpMx1GWSrg3WV0KboKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ساعتی پیش این هواپیما دولتی کشور به مقصدی نامعلوم از کشور تیک آف کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/141335" target="_blank">📅 17:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141334">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
گزارش CNN: وزارت امور خارجه آمریکا به دلیل تنش های احتمالی به سفارت‌های این کشور در خاورمیانه دستور داده است تا برنامه‌هایی را آماده کنند که به آن‌ها اجازه دهد با تعداد محدودی از کارکنان به فعالیت خود ادامه دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/141334" target="_blank">📅 17:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141333">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKvV06Xg0b2-KwIvwW-Tm3hXvEx6oMPsuv05ljlgU9nYb3l5KzKPQuQFVtK8DqudV5eqjSmXRiEc9UHrH0EU7bX3kEspn_pF0q1T3ekrZY0LmuU0GXaq5pnpUrhbd2jEFKD0hi9TaMWJ5w-8h6oAyhrzXdYxo5rkkveiNAt3kVcfv7djCdHOptebdm1AQWvzkD1KSohoNa5mOlZpflnGE4qKjgCV4o5XKyV7dAgKhWzwbYgda3NB-PbK40jgW36awRqaWI8yE4kxvzmvDQ3d_fl7R5EPWl2D_EUPBx2Wfs8qKsfyTlwB2hsXexWWIx7YvRlekjGP3pnCU-mMUdIiKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین وضعیت قیمت نفت
🔴
نفت آمریکا (WTI): ۸۲.۹۳ دلار
🔴
نفت برنت (معیار قیمت جهانی): ۸۸.۵۴ دلار
🔴
نفت امارات: ۸۹.۴۹ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/141333" target="_blank">📅 17:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141332">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
سیدمحسن نقوی، وزیر کشور پاکستان با استقبال علی‌اکبر پورجمشیدیان قائم‌مقام وزیر کشور به مشهد سفر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/141332" target="_blank">📅 17:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141331">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
سوال
:
چرا مجتبی خامنه‌ای توی طول این جنگ هیچ‌وقت جلوی مردم دیده نشده؟
🔴
نقدی : استراتژی دست اونه. دشمن ما جنایتکاره و به هیچ قانونی هم پایبند نیست
🔴
پرسش : یعنی به خاطر مسائل امنیتیه؟
🔴
نقدی : معلومه که به خاطر مسائل امنیتیه. قطعاً دلیل دیگه‌ای وجود نداره
🔴
پرسش : خودتون ایشون رو دیدید؟
🔴
نقدی : بیایید این موضوع رو دیگه ادامه ندیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/141331" target="_blank">📅 17:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141330">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
یک هیئت عراقی فردا برای شرکت در مذاکرات مربوط به مسائل امنیتی مشترک به عربستان سعودی سفر خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/141330" target="_blank">📅 17:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141329">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
حمزه صفوی:
ممکن است بمب اتم داشته باشی اما مردم انقلاب کنند
🔴
اگر بمب اتم هم داشته باشی، باید مسئله تحریم و اجماع جهانی را حل کنی
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141329" target="_blank">📅 17:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141328">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-wceEVpS6FmKF7H78Fb4Ww0xfoDco6IOxJYHtMEsQ_P5aAkFeJW_wa74fbxzSDexd6Z6XoblV6cTb8Thw3oZstNcmF4S2_YbdK7NuZvrz5mD_5_vrYxKVV0CP0wN6KhCCLEoEUSVAxIeWgfhxB6w8xBWF2BNrWnIazA6oXSmQBR6QSG_sD2B2XBa3T8mGkazbcLis1O05iOHaUSZ_mJnML5Q_kG3Bj0gF4MMGrIho7JchTcmlDYPHhkUeQQHHhZ7nwwdevClyWeDWo7xTjFf5atIbFV7fHSSa24ajKJv28wkdJV-cbbBXrS3yqXaAtWOO_d-_MZhbTs_NruZsWeAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قوی‌ترین پاسپورت‌های جهان
🔴
سنگاپور، کره‌جنوبی و ژاپن و امارات دارای قوی‌ترین پاسپورت‌ها
🔴
ایران هم جزو داغون ترین پاسپورت‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/141328" target="_blank">📅 17:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141327">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKcnfDJK6zXHMVJueOcMV6g650CwKK2utMPYANbY2b39tMj0e0w0pBMT3fA8k7KGcRjipPw6-1tc_TnpxiMQE3d8FEBAfHbpS-0BOfSyYa5cden1PGsXFsKoq93ywmF8hYqkv3J4pMnkppaqK_WIFg-v3aKP2qLQttG_R2kkmAL8KialBJDCLkVc3hSnPIL_QmYV0na3aMH7oyU10r49ia4JGezSyr5DqbFCBTSNbmAUrvHZOTq892GjRDmGv4th51zeBQ0Zw-8cqKo6mVcIBsfcTlG6I9i9NQLZCddqmLe2712KMdkgpiESsUZKQy_tU7m5brVKky91t8DrbXniKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ
دموکرات ها (ترکیب احمق/Dumb و دموکرات)
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141327" target="_blank">📅 16:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141326">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2FSrm1ODaOs8WdXop1Fto37b_BeI06YRW-9PnlVXdDlthRk4fjGx87bdnOzbbLOLl4JENKykpIO2EpEw15jmFDGnJu2Nz_LOPsZMUNDoxbyHkbPbYaM1ziyifQ0Ki146Q2KDLVzalF81Uqy7Kpc17HcaHdfgTTfDPltNku3eCBKCdeo3doUKtwiTeADIzvBLXXF835gWmZNcgKIKMUbNB-ZI49Ks-4UQYN9h1VLcojttyDQP4Kjq_3qp_CkE5FJ1RfzPBm__N6RmaKPZE3YeIVIWwdlqq_52mbwPUlwQ1mj9BkRZfk3YTHNN9Z9bggipUzqfI1wCKUm325QLBR_WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرمانده نیروی قدس سپاه پاسداران، قانی، در جریان بازدید اخیر خود از عراق، طبق گزارش شبکه العربیه، از دولت عراق درخواست کرد فرآیند خلع سلاح گروه‌های مسلح موافق جمهوری اسلامی توسط دولت را به تعویق بیندازد.
به گزارش منابع، قانی اظهار داشت که اعمال انحصار دولت بر سلاح‌ها در حال حاضر به عنوان «ضربه از پشت» به ایران تلقی خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/141326" target="_blank">📅 16:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141325">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ee3cab0d0.mp4?token=Lle9GmdEdqzWZwG8CbzD8L1EN37H64bsRB83hi-A75DIQbtA6ke089ZL9jIAeiUagGEFH776dcpTqSY6nHUsDE8MvzEbZlOtJymz0OmhljFYp-kaP_pgoDgv6Q98dGbmugGkqiQhBsVvS72yylt6k4oA5H3YSNBAjz0bC6z3PkGxT5s2USGiP6pCdZv9ILWQrNTSQ7URN13BirHQFwnEzQR6vimO6PSm6uIy7s_dpwBJ1Mpcg0Y1I5OsgkphPv1TWjpugJoej-VG-NKCbhdxJa560cIY2TrbeUNAGlMdjWsXgA40P3110egSyigksiWnQh7FYu3gT48lPuZMQRNYZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ee3cab0d0.mp4?token=Lle9GmdEdqzWZwG8CbzD8L1EN37H64bsRB83hi-A75DIQbtA6ke089ZL9jIAeiUagGEFH776dcpTqSY6nHUsDE8MvzEbZlOtJymz0OmhljFYp-kaP_pgoDgv6Q98dGbmugGkqiQhBsVvS72yylt6k4oA5H3YSNBAjz0bC6z3PkGxT5s2USGiP6pCdZv9ILWQrNTSQ7URN13BirHQFwnEzQR6vimO6PSm6uIy7s_dpwBJ1Mpcg0Y1I5OsgkphPv1TWjpugJoej-VG-NKCbhdxJa560cIY2TrbeUNAGlMdjWsXgA40P3110egSyigksiWnQh7FYu3gT48lPuZMQRNYZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یدونه جنگنده F16 ارتش ترکیه‌ حین پرواز آموزشی سقوط کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/141325" target="_blank">📅 16:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141324">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGPZDaG-iujgFQphI7we_fS6zupIXyWpGTLR9Xc8lEjwbqXQFyn3R-AWyUUvxJ4IAXkN9AZlm1B-lZdBBYE7DMUrc3mUYq4tosfQjHWsZqa1f4vCrEe5yDnUB1P82SC212mpfKtxw5qbcZvJfJ7ppByKYJmD5McRKf8s913x28YH2HABIHEka08Dam_OVpsYKhsitzCeeuY-bUaSZ_fNDeuj-TKmaS1y3qvunh1P8LsZuPOyzLqiX1Rt4q87vCW5oYLaqYZLz0t8rLndRRv5p8ciK9YhNXkGMTVSk9hLQkuAgwL6ANZmgfbXjArKV4CXcSIXoqYiE8Q0cZy6akQHww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار فیلد مارشال محسن رضایی با لباس نظامی با وزیر کشور پاکستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/141324" target="_blank">📅 16:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141323">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnSjKPlRA-zaq-niN497XyyKMGkD1Puv7kodQ0SQ-FhWqFqtIVtQioh07IB4iFOgMoCi46hctJWQWa0XR322AUYSMoM1iBjc_vYs7q6AsIfc6CoPk_Y5mOJWL1-knOcj6KW1PUbT4nniKMWwrSuZj1ybSW9hBWPNV7AysQuyuBBCKmII1xI9X4nlN85PLDmn2-wJ2gXBi1g5RBRMkxn13-g4zUvLHF1n676GTwPVtvmkgJYMqn994_6ZM9fcEpC5ZPn_9QhiSAVcrokwCQFgDrCtZDJitMUHEI6oLPX-PVLOF2REfI0zAoNOK4QM9_-b1SbQwwAWAZ9WGodh2vFudA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
متاسفانه ایرج خواجه امیری خواننده با سابقه و قدیمی در ۹۴سالگی درگذشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141323" target="_blank">📅 16:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141322">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_2BIb7ZAUQuV5Lxbd7rm8mb-4darYTDplD67fvlJPJg5Mrvo7NSNGFsae44vQlToEhdIgVX3lXWxgzpY6eDkWrBYBX1FUBbw_SXmXMwU5dhrN27J13RExIatcsiG_dn70gv9pT7aYBVwiM265KZHx3VN-ZDmCDT87c7YuDzPGN_BAuxuQuyNnvQHhtEdhlj2k_gGQSYXnzF3rX7z0ZAZTPk06WO0Qxof2T6g2v-vsewj01rItgOTzcAaXu4GAXzfkVMQCIQ-FcMIezhnRDfleGivcgODaWe_bEGbsP3L1_gLJso5sAp4K2J1BvQFCfl_AjRWKxBwAgaS1O0aEsGAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی دولت:
گرانی ناشی از فشار اقتصادی هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/141322" target="_blank">📅 16:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141321">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-kyCKxTwQba5ZB9v_crCF7_W5srxmtOEKA-Q1sWRjkVBQfJGWkM8J3D9UGs4OR_NNyF4_e9DKi13v-b6WAyaVFyq0Fl_K5QClcTnyWe8LvRd7r-EzUFgCpU6qmAJbwl4zbc1rbojgUbhiVE6m5SWVLtQg8vARj10yxvUtxZQI7i-fy3GIs8rCUYjLCl9vWlfuCOsZGZlGnnVJpwEg0Rq0iAMhwQvBRjHarSN_kZWi-wOG3-gr6UfDgfb6Ux9hXjh12VgswuYkG-qpZUCY9lq5wNjVvZ3szbjJbHMm9ej-yj2IsAgKiPR9yp2JXrCsqtDogghVo7nQfVPidL6UPEZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
تهدید‌های جانی زیادی علیه من وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/141321" target="_blank">📅 15:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141320">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNHYM_GbKlYFFjJj--jIsW_CRLOBfLu3bhG0dfYdpqkA1PKwWbutULk__cKehbNsFMs-uuaRXzF677bpZMZm11LqvrrLHlvZoHiT-0qONcyO2_uQAi31ka9w6TBVXAgoK3y-_CJynY8Hoyfdm5gUysf9rAwrxPs8LvbmP-4ywJdX4HZzUeFQZXMPzz_dE41sXMmQRkl8gm_Q5B1vfiwx_7BxSpcV-Wg_M0XUhu814ZrMj1FxQ4hN55cwH3C5AiBHMc3QpXqU3QTQfoH9J1qlwVHLRN1uO6AVsjZFCDCW22yziaW1ZESieazPuPbxhQJ8xiQ6pIY-RC7PwOJZoaCjKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل تخریب ۲۶ ساختمان فلسطینی در نزدیکی جنین را آغاز کرده است.
🔴
هدف از این اقدام، فراهم کردن زمینه برای احداث یک شهرک اسرائیلی عنوان شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/141320" target="_blank">📅 15:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141319">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49eca3a5ff.mp4?token=pMyqjG3StwNXp3yvKUPIQ5ECnexZf_qTFLhXqTBUkxOre9IX3fXh2HJ_lf4L0CSyctborN9Vuskj6JvgHJJwvWmMbH6qx09ivvsy7GoIUWx7qcR6x0QJHci79fBnPmxdezjTnGpT3l7qC9RZDccJ6xwZg6XALOBh7cHXP0tIwA-hVUhV-DpZcUzKy3OdQa5vazuCV950kYgKdEqhaFtQTGV6rdrKUqojXj0nGpIlGiwzt0f6N2A-DrzYbEnzbt6RX3xathsPohxCm4ScIFL07hjO8jeYDsT9pkQ_YyKWoeTQle984JgQ45lgkZQSADmIdJurg5-nT1lht9NMBbv7ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49eca3a5ff.mp4?token=pMyqjG3StwNXp3yvKUPIQ5ECnexZf_qTFLhXqTBUkxOre9IX3fXh2HJ_lf4L0CSyctborN9Vuskj6JvgHJJwvWmMbH6qx09ivvsy7GoIUWx7qcR6x0QJHci79fBnPmxdezjTnGpT3l7qC9RZDccJ6xwZg6XALOBh7cHXP0tIwA-hVUhV-DpZcUzKy3OdQa5vazuCV950kYgKdEqhaFtQTGV6rdrKUqojXj0nGpIlGiwzt0f6N2A-DrzYbEnzbt6RX3xathsPohxCm4ScIFL07hjO8jeYDsT9pkQ_YyKWoeTQle984JgQ45lgkZQSADmIdJurg5-nT1lht9NMBbv7ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شروری که با قمه‌کشی، ضرب‌وشتم شهروندان و عربده‌کشی در خیابان‌های تهران اقدام به ایجاد رعب و وحشت می‌کرد و تصاویر اقداماتش را در فضای مجازی منتشر می‌کرد، دستگیر شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/141319" target="_blank">📅 15:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141318">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
پی‌بی‌اس به نقل از کاخ سفید: عاقلانه است که ایران با توافق موافقت کند، در غیر این صورت می‌داند چه اتفاقی خواهد افتاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/141318" target="_blank">📅 15:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141317">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b51dddb4a.mp4?token=Y5XU4IC-_oyiT2THKNaXhYaohNrMPId2ijO2iIqJXfdPNfbsLZTkMIdNUQIXpFtxBjgLWDUAwh7H8tMJNsVHOluQ5Lke3nl6O7zDXuP55AWPtmncPGy1L2mvbRyXPjt5-r_IrfXKX64-8khQt2P9_xRDD7mXZJ_wot3yz0WYPWhe-odTs14CaF2ozZ-MwSB2Ihujsv2vRb8Ofn8NKGJFi7Lj3epgdsChKsMZ2MGZ6ImMiY-0wDXbPU5jvs78XrcSYTO-64cMwKyIY-H8Kq_MPmnKcAohU_dAl_mNpebwbl7lT17czquG57k_SpXdzgNo3xCEFI4z9lSLQNyJZ9HsIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b51dddb4a.mp4?token=Y5XU4IC-_oyiT2THKNaXhYaohNrMPId2ijO2iIqJXfdPNfbsLZTkMIdNUQIXpFtxBjgLWDUAwh7H8tMJNsVHOluQ5Lke3nl6O7zDXuP55AWPtmncPGy1L2mvbRyXPjt5-r_IrfXKX64-8khQt2P9_xRDD7mXZJ_wot3yz0WYPWhe-odTs14CaF2ozZ-MwSB2Ihujsv2vRb8Ofn8NKGJFi7Lj3epgdsChKsMZ2MGZ6ImMiY-0wDXbPU5jvs78XrcSYTO-64cMwKyIY-H8Kq_MPmnKcAohU_dAl_mNpebwbl7lT17czquG57k_SpXdzgNo3xCEFI4z9lSLQNyJZ9HsIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت عجیب سواحل جنوب که کاملا نفتی شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/141317" target="_blank">📅 15:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141316">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
آتلانتیک: جنگ با ایران ذخایر موشکی آمریکا را فرسوده و دست ترامپ را بسته است؛ کاهش مهمات دوربرد و کمبود رهگیرهای پاتریوت و تاد، گزینه‌های نظامی واشنگتن را محدود کرده و دیپلماسی را به گزینه‌ای کم‌هزینه‌تر تبدیل کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/141316" target="_blank">📅 15:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141315">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجار در جاسک بر اثر عملیات خنثی‌سازی مهمات
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/141315" target="_blank">📅 15:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141314">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
پوتین: توقیف کشتی‌های روسیه توسط برخی کشور‌های اروپایی، چیزی بیشتر از «دزدی دریایی» نیست
‏
🔴
اگر اروپا این اقدام را انجام دهد، پاسخ مشابهی خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/141314" target="_blank">📅 15:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141313">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
فارس: نرخ خودکشی تو ارتش آمریکا بالا رفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141313" target="_blank">📅 15:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141312">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
فارس به نقل از منبع ایرانی: هیچ مذاکره‌ای درباره تمدید آتش‌بس با آمریکا در جریان نیست
🔴
از دیدگاه ایران، آتش‌بس تاریخ شروعی نداشته که چیزی برای تمدید وجود داشته باشد.
🔴
آمریکا ۴۸ ساعت پس از توافق موقت آن را نقض کرد و چند روز بعد از آن خارج شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/141312" target="_blank">📅 15:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141311">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
فوری / خبرگزاری آناتولی به نقل از منابع پاکستانی مدعی شد ایران و آمریکا با تمدید مهلت ۶۰ روزه مندرج در تفاهم‌نامه اسلام‌آباد موافقت کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/141311" target="_blank">📅 14:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141310">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
بلومبرگ: روسیه طی یک سال بیش از ۱.۱ میلیارد دلار مواد معدنی راهبردی با کاربردهای مرتبط با صنایع نظامی وارد کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141310" target="_blank">📅 14:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141309">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی: بسته ماندن تنگه هرمز و بالا بودن قیمت‌ها، بر مصرف نفت فشار وارد کرده
🔴
انتظار می‌رود که تقاضای جهانی نفت امسال روزانه ۱.۶ میلیون بشکه کاهش یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/141309" target="_blank">📅 14:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141308">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه پاکستان:
فرایند صلح گسترده‌تر بین آمریکا و ایران با مشکلاتی روبرو شده است و ما امیدواریم که دو طرف به گفت‌وگو بازگردند. ما می‌توانیم توافق‌نامه همکاری را قبل از پایان مدت اعتبار آن تمدید کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141308" target="_blank">📅 14:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141307">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
۴ ساحل قشم آلوده به نفت شدند
🔴
سواحل سوزا، شیب‌دراز، نقاشه و بخش‌هایی از جزیره هنگام دچار آلودگی نفتی شدند و مدیرکل آلودگی دریایی سازمان محیط‌زیست می‌گوید که علت این آلودگی هنوز مشخص نشده است.
🔴
هماهنگی‌های لازم برای پاکسازی کامل این محدوده انجام شده و پیش‌بینی می‌شود عملیات پاکسازی ساحل تا پایان امروز به‌طور کامل انجام شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/141307" target="_blank">📅 14:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141306">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8847ad310.mp4?token=Rw1-tyksDsu5uF9Xg7quAaH4NtL2HRajlgq7z_N1WS605lTw9-rAiI7oymwLS3v0Q5TaB2RGT8gn285oQ3B8PZXA-AHxSAfhfYP1Nadi363B4XKOyzgO_OotiBND_v5SQS9anT0vCtprxWZOSCx1_gMEBnxzpYi50sLcnUffylLuoXjAMp58l8Dl9GWO2vc5egOZXJQn-GYmYxt-yJ9AzqoEvnwu3nFXICIIHfFu55Gn1hiTxCbEW-oKlN3iIjr2u-G1P0ir01NSWL7fmxs1hpJrS3k5Va0yhMb7ejiuoqMCudtuBAG47iSgDcA9y6CpnTlafX97yiK5ni2ltyXjtDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8847ad310.mp4?token=Rw1-tyksDsu5uF9Xg7quAaH4NtL2HRajlgq7z_N1WS605lTw9-rAiI7oymwLS3v0Q5TaB2RGT8gn285oQ3B8PZXA-AHxSAfhfYP1Nadi363B4XKOyzgO_OotiBND_v5SQS9anT0vCtprxWZOSCx1_gMEBnxzpYi50sLcnUffylLuoXjAMp58l8Dl9GWO2vc5egOZXJQn-GYmYxt-yJ9AzqoEvnwu3nFXICIIHfFu55Gn1hiTxCbEW-oKlN3iIjr2u-G1P0ir01NSWL7fmxs1hpJrS3k5Va0yhMb7ejiuoqMCudtuBAG47iSgDcA9y6CpnTlafX97yiK5ni2ltyXjtDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خروج نیروهای آمریکایی از اربیل به سمت ترکیه
🔴
بر اساس ویدئوی منتشرشده، نیروهای آمریکایی بامداد امروز اربیل را ترک کرده و به سمت ترکیه حرکت کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/141306" target="_blank">📅 14:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141305">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
بلومبرگ: امارات در صادرات نفت از طریق تنگه هرمز به عراق کمک می‌کند
🔴
نفت خام عراق با بهره‌گیری از زیرساخت‌های انرژی در امارات، برای صادرات به نقاط دیگر جهان ارسال می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/141305" target="_blank">📅 14:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141304">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
یک منبع ارشد ایرانی به رویترز گفت:
هیچ بحثی برای تمدید آتش‌بس بین آمریکا و ایران وجود ندارد
🔴
در عوض، مذاکرات بر بازگشت احتمالی آمریکا به توافق‌نامه تفاهم (MOU) و یک جدول زمانی برای اجرای تعهدات متمرکز است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141304" target="_blank">📅 14:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141303">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcGf-pkTXkICT-Oi605JhwfCton9sfspIu3T9ZB3CBAtsgdtLZrGPKbuONfKg7YiHHCvusPquo8m33-rZyp3gqEcx4OGXYwmg-gYmv2pE_o5Mrkj8WbrDUWoxE5a1Qp-PvyiCVThkART-Usayv_UzSY_YaW5VAAF9-OKSAdosFrVBiUnIiMvbkj17aeBcP_iGKySlzc_fxU9VbRO3TpSWwlbXd2ztyYoWsNQwAUMdw_lSEPqRC2DQzpgmJLYb_Ie1C38PzsqHcz-EoE_pOjRfZLqo8hm_y5W7Wl1iEr1Yjyaw-j6YySnSVwWHn9XDn8yaVGaiG-qQn-hpnJtIXZQhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت چندسال قبل حمید رسایی که پس از انتصاب روز گذشته حجت الاسلام طائب توسط مجتبی خامنه‌ای، مجدداً در فضای مجازی درحال انتشار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/141303" target="_blank">📅 14:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141301">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
پاکستان: روند صلح گسترده‌تر متوقف شده است؛ امیدواریم به زودی از سر گرفته شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/141301" target="_blank">📅 14:17 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141300">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
مدیر برق عسلویه حین جمع‌آوری ماینرهای غیرمجاز، از سوی یکی از استخراج‌کنندگان مورد ضرب‌وشتم قرار گرفت و به‌دلیل آسیب جدی به بیمارستان منتقل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/141300" target="_blank">📅 14:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141299">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0GbnbqnRjn0mVcTFQ4J-3-bt14tV5dwPwV3vKNDmjIc0S0-K8TMB2yeysMO4mwIE1PBrnifGyFORps1WvyLMm14ETth6KYJDXr1uhJGe6lrCeOPKy6XifZiORNAklG3ZLyP7l-a581GTbzfcDd3quC7j4AUquCXKRhx7hQr2ctYkLSwqz9oGaI2DScs5Ie8XHq4VRKolKqLTkOg1z05EA8C8e8aw0ghLFSVGyF9Fa_vQmurL4jNxEUAIukAcr0APFNpGgbVTquldpxdaWqKg1dFDAevdyJAXAAYZyasMbfV3sfevgKH42jje0S7rRY_aTBrDcZabJ5ioFd0b2Tn0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر جدید نشان  می دهد که چین یک سامانه ناشناس را روی ناو آزمایشی رادارگریز خود نصب کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141299" target="_blank">📅 13:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141298">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLfmUND3nsazuho2FNHyRkKeaTLEQvCv5YK4BXGHh9cVXmnM27_FdWxU0FqlCL5Pnpcra5_1vVwaYRcW8_H9XPB3sOOGU4bUl_LSz5JZTso6S9aNEvQiI9w-sLbcMQBo0DksEWM_fN1xMZWrHhnTWaEYubrLQAmTocqcsWqWH1L6SxYz8l7j4jyabR31kLZKRlxhsatHwPxg4OaPom1hQmYgW28FI5veuBTBu94DQfUQSQGB12Hx9mEWyO6vN1hqAH7g1lH74qUV7GCX7gl9HgnIXYDVESfyslBQpzeyi6-uvNfiAV2moZGnUewtPIx5pXpFVDnFLiKY9n18KQt3AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وندی شرمن، معاون پیشین وزیر امور خارجه آمریکا: در آینده قابل پیش‌بینی و شاید برای همیشه، ایران کنترل تنگه هرمز را در دست خواهد داشت
🔴
بعید است اعمال فشار اقتصادی بیشتر از سوی ترامپ، باعث شود رهبران ایران تسلیم شوند یا از مواضع خود عقب‌نشینی کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141298" target="_blank">📅 13:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141297">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
گروه‌های حقوق بشری آمریکا علیه دولت ترامپ به دلیل تحریم‌های دیوان کیفری بین‌المللی شکایت کردند
🔴
چهار سازمان حقوق بشری آمریکا به دلیل تحریم‌های اعمال شده علیه دیوان کیفری بین‌الملل، علیه دولت ترامپ شکایت کرده‌اند و استدلال می‌کنند که این اقدامات نقض حقوق اساسی بوده و به صورت غیرقانونی فعالیت‌های حمایتی را محدود می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/141297" target="_blank">📅 13:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141296">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
کپلر: تردد کشتی‌ها در تنگه هرمز به پایین‌ترین حد یک هفته اخیر رسید؛ تنها ۸ کشتی روز سه‌شنبه از این آبراه عبور کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141296" target="_blank">📅 13:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141295">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
همتی در اجلاس بریکس: بریکس باید از گفت‌وگو به اقدام عملی برسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141295" target="_blank">📅 13:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141294">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHiO_gOidujbutcdDrvvdweo5FiH8fMyoBaUIE003jxMMLO2ksQqLiglMPQmOw7R2wcGVZcXKTIYNtuZPhRTJZBuiFlRAJeeNqKn3K4BCoh6fuSqgNr5PsHAyjQOUblAzV5bDTmZBD2wgAej-lCEXeknGd2uCYfD5iMvyMA9DAB6ksc8wxNVmY9iENIC0RkFYF9HMUKNvpzuW5GFOm49eMe0GGxs4Ygz0bbyMQFvr5jtvPwrvdbdUz5bD0LN4hNCZiwFGN-gSLenrQds7QYhmZkMQB3GeE9tv4mg2mpxkxXqNRaN4WRYvH524o5Oxy-w4RRaC4rycpATDCjGJYPrjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز: تهدید ایران که منجر به جابه‌جایی مخفیانه ترامپ در آنکارا شد، در آخرین روز نشست ناتو در ۸ جولای آشکار شد.
🔴
اطلاعات آمریکا چندین جریان اطلاعاتی دریافت کرد که نشان‌دهنده تهدید موشکی خاص علیه ایرفورس وان بود، صرف‌نظر از اینکه کدام هواپیما حامل رئیس‌جمهور باشد. یک فرد مسلح به موشک دوش‌پرتاب در نزدیکی محل نشست ناتو مشاهده شد و نیروهای ایرانی دقیقاً می‌دانستند ترامپ در کدام طبقه از ساختمان محل اقامتش در آنکارا مستقر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/141294" target="_blank">📅 13:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141293">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
اداره‌ فرودگاه‌های هرمزگان: فعالیت پروازی فرودگاه بین‌المللی بندرعباس از ۲۴ مرداد آغاز خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/141293" target="_blank">📅 13:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141292">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uA1CCKwYEYrbkJw6z9kAejFj9tTCiP-zOWDBlIq-2lYyKepVwd1j4T5pQtoGhUZbTYlTUFqNmbzCT6ywPsd5VHtAtWH1h3f4bGchvq1spS51xjfu-lSziOecyB1-ovgorKDyLSd0EWpHWRRsNqQBUB_GvPEbQ-ndLjTXtpgHE593jemNe4ISfsOPnVLyWlfgS-LaXTOV0oLV3RJujCQDzjhpkTi8bSDmPX49YQ1Ek7CJKDDqnVqmeDUc0-5xHx3LkX1JhNXRpV5TKs0HRqUYUoOGHzb4UNnJQelMjvgyd3r60jvjMa3cHpULndhAFQ1Tk2t-P5_9zVI9lZZ3_C2NCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس مجله اکونومیست، محبوبیت ترامپ به پایین ترین حالت خود رسیده. حتی از کم ترین محبوبیت دوره اول خودش و حتی بایدن، کم تر شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141292" target="_blank">📅 13:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141291">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f65a8eb14e.mp4?token=qmcO84cuDasUAK0rvYX93fefwxbUbdz286YPCA8ZZxwXAHyTd-LF2oULeLhCo0HuRtklrsX13IrnMIEEhYVidJBRR45aX4Z7LQyN2Lyg8e17ee4GsnVKKAo9T0qSt208u22vyyVEZNk_XDqTTen82auTkaQJOsKrDC_qh0qL86ATZUBc4_ytd8SPcVJ-zr_M07jDwqgmcrno-fg1Uu-LJY-FfRziL5ims-JENjwskM0fLzp3nTLnZThxDPftReTllTuTsYhLs_JzB7Snn9GvTCWVuFgQPDqoIZ7_jWnSWPRX9pla1ISqq5y9E-W_tP8UUyOwfTgKHIuC0JdLtnheKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f65a8eb14e.mp4?token=qmcO84cuDasUAK0rvYX93fefwxbUbdz286YPCA8ZZxwXAHyTd-LF2oULeLhCo0HuRtklrsX13IrnMIEEhYVidJBRR45aX4Z7LQyN2Lyg8e17ee4GsnVKKAo9T0qSt208u22vyyVEZNk_XDqTTen82auTkaQJOsKrDC_qh0qL86ATZUBc4_ytd8SPcVJ-zr_M07jDwqgmcrno-fg1Uu-LJY-FfRziL5ims-JENjwskM0fLzp3nTLnZThxDPftReTllTuTsYhLs_JzB7Snn9GvTCWVuFgQPDqoIZ7_jWnSWPRX9pla1ISqq5y9E-W_tP8UUyOwfTgKHIuC0JdLtnheKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک کشتی مسافربری در سواحل بالی آتش گرفت
🔴
۱۳۱ نفر در این کشتی بودند که بیشتر آنها توسط کشتی‌های عبوری و امدادگران نجات یافته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/141291" target="_blank">📅 13:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141290">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
فارس: هزینه اجاره نفتکش‌های غول‌پیکر در مسیر خاورمیانه به چین به‌دلیل افزایش ریسک عبور از تنگه هرمز، از ۲۵ تا ۳۰ هزار دلار به حدود ۵۰۰ هزار دلار در روز رسیده؛ یعنی ۲۰ برابر
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/141290" target="_blank">📅 13:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141289">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd9e409144.mp4?token=ZWpR7XIHaN3Xoyp2jvS3OVrz1yLCMucLo9a9MdigeS6hipsqF4qhFREPW0JNBV9-43qBzM2ukShshDNuSzNE3PQWWr0mDENUzTw0RfuEJtnCvShjk5YUQAY_2ApK4TDsI6_1P9W2_qAkeIGwTvhdL4G7-_7uBIXs6GRACJlk7RttqooJdqM6oxkosv-quFIiTXjTi5MEgZDf52AmDOB3M00I1AWTn7EUfuaFSzDgm5GecvDyXfmk7Hd8bQkEIU-hUbz0rL2UsAoKHhDw6UB9fh6TPEUohJG4R0nUugjTOOkmbreI2g4ZUJFv4WFoTVBkGA94g3kPnFI3gachF3s-u4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd9e409144.mp4?token=ZWpR7XIHaN3Xoyp2jvS3OVrz1yLCMucLo9a9MdigeS6hipsqF4qhFREPW0JNBV9-43qBzM2ukShshDNuSzNE3PQWWr0mDENUzTw0RfuEJtnCvShjk5YUQAY_2ApK4TDsI6_1P9W2_qAkeIGwTvhdL4G7-_7uBIXs6GRACJlk7RttqooJdqM6oxkosv-quFIiTXjTi5MEgZDf52AmDOB3M00I1AWTn7EUfuaFSzDgm5GecvDyXfmk7Hd8bQkEIU-hUbz0rL2UsAoKHhDw6UB9fh6TPEUohJG4R0nUugjTOOkmbreI2g4ZUJFv4WFoTVBkGA94g3kPnFI3gachF3s-u4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مسعود نیلی: وقتی تفاهم‌نامه منتشر شد گفتم احسنت بر کسانی که توانستند این را از آمریکا بگیرند.
🔴
یک ساعت جنگ بیشتر به ضرر کشور است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141289" target="_blank">📅 12:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141288">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
سازمان بین‌المللی دریانوردی:
نشت نفت از نفتکشی که در شمال شرق جزیره قبلیه عمان به گل نشسته است.
🔴
انتظار می‌رود نشت نفت از نفتکش کارولین بیزینجی به عمان برسد.
🔴
بادها دسترسی به نفتکش به گل نشسته در نزدیکی عمان را محدود کرده و عملیات نجات را به تأخیر می‌اندازند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141288" target="_blank">📅 12:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141287">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
زاکانی: زمان حمله آمریکا، آقا مجتبی تو منزل کنار همسرشون بودن و همسرشون شهید شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/141287" target="_blank">📅 12:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141286">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424fedac1b.mp4?token=tFfY7NZOU00zlwUJmZ5qBWZ_feLhPVkERINBftC7yPhJ5ZqRcoOG_V633vhrp_IjALgW70bD_9nmYohJKUkRWX9Tp_chzroVu_DwolXOEHf1t10yWD_1hVWOtPpxkq2CTzyitYgfwVTqFPerc8YX39Q_ePjLvor_HWnZwQJjBkNDdktscjasVrb5HTRm42f5Yc5jr2V_-S7gqT753wTWv70uC7ZttQE8iW3i5TVcsggsi0QB9KHiT19YsvCocxl1PQ9Px5zacqdz53iqL3zSchJ8_VksirzoaF4L-ujFyZWXTW8rRCp4fvo8qDQmrcV6bfuvPWj2RIs5fs-y5U5KAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424fedac1b.mp4?token=tFfY7NZOU00zlwUJmZ5qBWZ_feLhPVkERINBftC7yPhJ5ZqRcoOG_V633vhrp_IjALgW70bD_9nmYohJKUkRWX9Tp_chzroVu_DwolXOEHf1t10yWD_1hVWOtPpxkq2CTzyitYgfwVTqFPerc8YX39Q_ePjLvor_HWnZwQJjBkNDdktscjasVrb5HTRm42f5Yc5jr2V_-S7gqT753wTWv70uC7ZttQE8iW3i5TVcsggsi0QB9KHiT19YsvCocxl1PQ9Px5zacqdz53iqL3zSchJ8_VksirzoaF4L-ujFyZWXTW8rRCp4fvo8qDQmrcV6bfuvPWj2RIs5fs-y5U5KAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تفاوت خرید گوشت طی سال‌های اخیر را ببینیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/141286" target="_blank">📅 12:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141284">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bK3VkU-j3Gf2WhRvesf_Fep0pptywOAS0P0is8rB9p8yRjTO4rqeuB3a2c-QlyeY1uB8OMuSH9qXejbXmtWtNuEUBzxfyhQvwTm5JwSQV_BJ2vbnRbtcbdp4DzX0wbIa5CGm9BtoPQwJLZCwslNTChGlkywo-cW_DNh5i7_Ct7GtWvy_kupTtgv69_t0ytGzVkjpWrTwDqcBs8jBl_69SoEu1JmFoRfZynFHIVdjjrMoo3nEQrpGa0lckq12-Gu03Dvc236ePcA5ni9JIiDRPBBsB3pf-QeJzYgXreOTcx530VST8ka2ibE3JR-MEnuiUEfaJtuQ6s1yY6FZKtwaDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf690f4728.mp4?token=MUsCUDQfKdWOgFiOdd3rHwuo2wQUmD38qKHitLTBwXUXeBPgLNUpWjYG3j9EBjSD59j2LTbK1xT_SH2nQVsDgZRVCXdZPrpwWeAEqiyVn1ig9Eb2YCLUpEBw9m1jVAZwLPxjn9lifW0aiI3ri-PyYiZDIWSRwxVFaGO5F5bGDJ-csY9JyevswTU9oJJdZdvxnWGrainTNS0xjMHMCOxXFgmihQuaTV4g30eU6fD7nlYFQe-yrzDs9VmbDtSHvX9yEqnONyYRf9m782_FJyDr3uMrxoW_zKgMuTo-mID5KE8ChRO7mJAOYrPIpICINWhx-ZSwywbENeIshceEg4PEng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf690f4728.mp4?token=MUsCUDQfKdWOgFiOdd3rHwuo2wQUmD38qKHitLTBwXUXeBPgLNUpWjYG3j9EBjSD59j2LTbK1xT_SH2nQVsDgZRVCXdZPrpwWeAEqiyVn1ig9Eb2YCLUpEBw9m1jVAZwLPxjn9lifW0aiI3ri-PyYiZDIWSRwxVFaGO5F5bGDJ-csY9JyevswTU9oJJdZdvxnWGrainTNS0xjMHMCOxXFgmihQuaTV4g30eU6fD7nlYFQe-yrzDs9VmbDtSHvX9yEqnONyYRf9m782_FJyDr3uMrxoW_zKgMuTo-mID5KE8ChRO7mJAOYrPIpICINWhx-ZSwywbENeIshceEg4PEng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شاید باور نکنید ولی۲۰ سال قبل «پارسا پیروزفر» به دلیل خوشگل بودن زیادی برای همیشه از تلویزیون ممنوع التصویر شد و رفت سینما.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/141284" target="_blank">📅 12:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141283">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
وزارت خارجه پاکستان: وزیر کشورمان پیام مهمی را از سوی نخست‌وزیر و فرمانده ارتش به رهبری ایران منتقل کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/141283" target="_blank">📅 12:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141282">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
روند صعودی بازار طلا شروع شد   امروز ساعت ۳ یک تحلیل بسیار مهم از طلا و تورم داریم و ساعت ۲۱ قسمت ششم دوره رایگان  «سواد مالی»   حواسا جمعه؟؟
❤️‍🔥</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/141282" target="_blank">📅 12:12 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141281">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9cNoG2R89ROAILefAyMAu_4BVUJ73CiqxIyhrzMWlL9mLCccOv8ipAiKqi7dW6kCdR7T4HTTBcBysgLgZvusoHahSKpFJnsOKisGeqX-Xn8XTHzo2fyYtsQwk_JaoOtmyky9aZqKYJPthNQO5FWPfv_YZ5zHf8bPKHa42zawnbuDv96XfYvYIWlX5azoEztpC8ojrSMuMii2POw9MBfj_XI0wVgFtziVI1kzfnftbLEhRP0DCFq_PjKtJwcnuWzUBK7PCML4qvEpcAku0ljy7QXWHtR640ELbGAV2YzFWeOHK8sdn3j2f5k89H3RIGJBMC_abyLmPDeA2wsnXJ2ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حجم نفت رها شده در نزدیکی جزیره قشم که بسیار خطرناک است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/141281" target="_blank">📅 11:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141280">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
وزارت امور خارجه پاکستان: پرونده میانجیگری بین واشنگتن و تهران را نبسته‌ایم و مدت ۶۰ روز مندرج در یادداشت تفاهم قابل تمدید است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/141280" target="_blank">📅 11:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141279">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cedbc59d6.mp4?token=SGAG_8t_ueKntPONwZeO_L538WS7mxRjVN7WBSoYgvvFYWrePWY66D_JGI6B-p5kxmx3mEjpP8y7kHKYkpPeiPhCCyFqbVo4Kd94GWZJF5UME_cx0RhU44NEI1BKy-N7v2on4yykFxqFN6TsDIPlwvPhMYl45eZg-WcKg4B4CGhcQcr2m0Uo-9o7dFFErgKkp-gWSMq2RH2v1waT8HDY-TPueaKfF8ujw16D4YSw38rNZKUQFYzwG7PVnbYEYGhXedVuhMbgez31hzJVsqB2j9jXNv9ip7BhetChzNXHgxwm9qCUY2z3C9BHrl5dVp6fFH4z4Vzc-QIV1DC5JllLPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cedbc59d6.mp4?token=SGAG_8t_ueKntPONwZeO_L538WS7mxRjVN7WBSoYgvvFYWrePWY66D_JGI6B-p5kxmx3mEjpP8y7kHKYkpPeiPhCCyFqbVo4Kd94GWZJF5UME_cx0RhU44NEI1BKy-N7v2on4yykFxqFN6TsDIPlwvPhMYl45eZg-WcKg4B4CGhcQcr2m0Uo-9o7dFFErgKkp-gWSMq2RH2v1waT8HDY-TPueaKfF8ujw16D4YSw38rNZKUQFYzwG7PVnbYEYGhXedVuhMbgez31hzJVsqB2j9jXNv9ip7BhetChzNXHgxwm9qCUY2z3C9BHrl5dVp6fFH4z4Vzc-QIV1DC5JllLPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحبت‌های چندسال قبل احمدی نژاد درباره طائب: تعادل روانی نداره و پرونده سازی میکنه برای همه و دو به هم زنی میکنه فقط
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/141279" target="_blank">📅 11:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141278">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QG2SsPddmJ2O15UPPxPIk0SVLxqnMi252m37Ef0mJhwz6TJEnhBt-x-OgPsl9punUJAOktiYDnzCM8owRSajdLUHacm-3R2JZDpq8R9fKd5RvBndJWrxRjZl2Wl25hriTHagvv53ZKQRAchL3Dwd-0dcjt05Lzx_4jX3q5o68u0ovwEjOsONXgYnM55lISqLGT5hMW93FZoq7o503BEys-KnzAVkOdSh3yd4-n7Fck0mdQ04xXIkTkd6qUzJ_bdxik-fG4S6S9BU4X-eHDQvSYOEaTQU421HMCkYvJITD63j43FRbhFMMWUIIV1HmoN0u1NQjVidLitEfSnU4zc6WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جنوب ایران نابود شد
‼️
🔴
لکه‌های نفتی به جنگل‌های حرا در قشم رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/141278" target="_blank">📅 11:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141277">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6895ee6189.mp4?token=K1iNO-hWbEiL14W_YeV5_iKzFwrJIdtJqpdiAJFIEVb9gXdOQnee4lp7fdUjgviFhhlrCAv5_CZU7URezGy2y-A94gOUNLeSivDoA2gCR-Gn6ktUcq_vtOB-De4s2wKGENskRfOBVcUBcWXt1OqQ4SiS9a2_N-R5KGzbGnTIdGKBP4iJlDvDJFqYz3rTSIiAa2SBEockuKk9oVKvMeLH2jAwAIzFJAaDol9AtGJm_5YnFz1nkCd_PzZwJRUBwVjGIsKeD9SLuRt2ORRs952_81UR_xMYRJrF5yCfoyoWbcTDZ5abigT-dDsrV8e4x149_w7BS0HCwdwPWubmVRB_Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6895ee6189.mp4?token=K1iNO-hWbEiL14W_YeV5_iKzFwrJIdtJqpdiAJFIEVb9gXdOQnee4lp7fdUjgviFhhlrCAv5_CZU7URezGy2y-A94gOUNLeSivDoA2gCR-Gn6ktUcq_vtOB-De4s2wKGENskRfOBVcUBcWXt1OqQ4SiS9a2_N-R5KGzbGnTIdGKBP4iJlDvDJFqYz3rTSIiAa2SBEockuKk9oVKvMeLH2jAwAIzFJAaDol9AtGJm_5YnFz1nkCd_PzZwJRUBwVjGIsKeD9SLuRt2ORRs952_81UR_xMYRJrF5yCfoyoWbcTDZ5abigT-dDsrV8e4x149_w7BS0HCwdwPWubmVRB_Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیه‌ی هردو سینه‌ یه خانم برابر با دیه کامل یه خانم هست ، و دیه کامل یه خانم کمتر از دیه‌ی بیضه سمت چپ یه آقا هست !
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/141277" target="_blank">📅 11:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141276">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
ارتش آمریکا در دو جنگ اخیر با ایران بیش از ۱٬۴۰۰ موشک و پهپاد را رهگیری کرده است
🔴
به گفته ژنرال جان رافرتی، فرمانده پدافند هوایی و موشکی ارتش آمریکا، نیروهای ارتش آمریکا در جریان جنگ ۱۲روزه ایران و اسرائیل ۱۲۵ موشک بالستیک و در عملیات «خشم حماسی» بیش از ۱٬۲۰۰ تهدید شامل موشک‌های بالستیک، کروز و پهپاد را منهدم یا رهگیری کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/141276" target="_blank">📅 11:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141274">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
یک پهپاد ناشناس با پرواز حدود دو ساعته در حریم ممنوعه فرودگاه هانوفر آلمان، دست‌کم ۶ پرواز مسافری را با تأخیر مواجه کرد و یک هواپیمای باری را نیز مجبور به تغییر مسیر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/141274" target="_blank">📅 10:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141273">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
خبرگزاری رویترز گزارش داد کره شمالی در آستانه برگزاری رزمایش مشترک «سپر آزادی اولچی» میان آمریکا و کره جنوبی، یک موشک بالستیک شلیک کرده است
🔴
بر اساس این گزارش، موشک شلیک‌شده حدود ۷۰۰ کیلومتر پرواز کرده و سپس در دریا فرود آمده است. رزمایش مشترک آمریکا و کره جنوبی قرار است از ۱۷ تا ۲۷ اوت برگزار شود.
🔴
این پرتاب، یازدهمین آزمایش مشکوک موشک بالستیک کره شمالی در سال ۲۰۲۶ محسوب می‌شود. تحلیلگران کره جنوبی احتمال داده‌اند موشک شلیک‌شده از نوع مافوق‌صوت بوده باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/141273" target="_blank">📅 10:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141272">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
سی‌ان‌ان‌: یک روز پس از اینکه ترامپ ادعا کرد تنگه هرمز باز است، مقامات دولت او درباره افزایش قیمت نفت و بنزین هشدار دادند، زیرا «محدودیت‌هایی» جریان انرژی از طریق این آبراه را مسدود کرده
🔴
اداره اطلاعات انرژی ایالات متحده پیش‌بینی خود را در مورد میزان توقف تولید نفت در خاورمیانه در ماه‌های آینده را بالا برده؛ این کاملاً در تضاد با اظهارات خود ترامپ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/141272" target="_blank">📅 10:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141271">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
رئیس‌کل بانک مرکزی: ایران به‌زودی عضو بانک توسعه نوین بریکس می‌شود؛ معتقدیم کشورهای عضو بریکس می‌توانند با پول‌های ملی با یکدیگر تبادلات تجاری داشته باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/141271" target="_blank">📅 10:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141270">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7-D5s7jqHIRY-uMVxcwV2m-RmWaVDaQkXpi9heblAajwq9doWcj-TqDIz1wq9wCBOycj9h0ItJTu64KzALtQ7XpfCP2mP5lLYzMS8dLQ8MgEzbuVBKBunzkx3mYbrWDQX3OiHPWvaYeDNQq5Pr0sAwjT99skvwkkQLKPbV4Dcrw2-kwDV_XI7LShvXPH5z5dYK-O_Tx7U77dOhQIn33MEv7lLiTg85trefyTGz0xhOWb0k_bn-noH37pip69sleC4IFCJop-8kcoxLxv_dM9ulSrIH1jiiqLPNBgJnwGCilFAdmy3UTewwoDn1SR-a5qOUXYHgyqcHkzQHOZ29MlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اپک‌تایمز: آمریکا ۲۰۰۰ گیمر را به‌دلیل تصمیم‌گیری سریع و عملکرد خوب در شرایط پراسترس، به‌عنوان کنترلر هوایی برج مراقبت فرودگاه‌ها استخدام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/141270" target="_blank">📅 10:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141269">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
الجزیره: روبیو و بسنت از جمله کسانی بودند که در ایرفورس‌وان که به عنوان طعمه استفاده می‌شد، باقی ماندند
🔴
به گفته یک مقام آمریکایی در عملیات انتقال مخفیانه ترامپ، مارکو روبیو (وزیر خارجه) و اسکات بسنت (وزیر خزانه‌داری) به همراه کارکنان کاخ سفید و خبرنگاران، در هواپیمای اصلی (بوئینگ ۷۴۷) ماندند تا به‌عنوان نوعی «طعمه» عمل کنند، در حالی که او با یک جت کوچک‌تر به‌صورت پنهانی به یک پایگاه نظامی در بریتانیا منتقل شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/141269" target="_blank">📅 10:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141268">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه، امریکا درباره کوبا: من مطمئنم که تا پایان این دوره ریاست جمهوری آمریکا، کوبا در مسیری غیرقابل بازگشت به سوی آینده‌ای بسیار متفاوت قرار خواهد گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/141268" target="_blank">📅 10:17 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141267">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcc2FK9wxAI5pLiUvDhf_-jzR5_wLP2KcgC2mX1uPWXfmbg4fwTEZ-f5zjrHhRel3vt-CxKTybiS4h9ZWIpMFIW5pwhK4koHxjnR9ueji8wx047xGLDXRtnCeR5lxpwUcawcbAlwNGO-mUfWAixoFI5ZYh8YH4piEpEx4ARMG0hczA5L0PuyAq-Zt233YnsEtXnbEm92DyWGwnb0mK4jjaZ14lQjMQctHVGG7KtHy9Vm9cnlqXaA3YHhka8-fGn9xmSaMLmWL5NJE3sKGM-NCnBbKgH7NWSobgn8LAndUQOCEQCHxkRqV3A29GpNq8CwNr1Yt6xANY5FjDdJ_Pl45A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: ایران فعلا تنگه را باز نمی‌کند؛ جلوی امضای توافق با عمان _با جزییاتِ مدنظر آمریکا_ نیز گرفته شد
🔴
مُدل پیشنهادی ایران برای عبور از تنگه (شمالِ تنگه، مسیر ایران و جنوبِ تنگه، مسیر عمان) قرار بود برای ۳۰ روز تست شود و در صورت انعطافِ آمریکا در حوزه «تحریم ها» و «آزادسازی منابعِ ایران»، دائمی گردد که با لجاجت آمریکا فعلا همه چیز متوقف شده است
🔴
دو هفته‌ی آینده، بسیار حساس است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/141267" target="_blank">📅 10:12 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141266">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
وزیر خارجه پاکستان: کشته شدن ۳ نفر از شهروندان ما در حمله روز گذشته به یک کشتی در دریای سرخ
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/141266" target="_blank">📅 10:12 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141265">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
شبکه الجزیره در خبری فوری از اصابت ۴ فروند پهپاد به استان اربیل عراق خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/141265" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141264">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
الجزیره: قطعاً بین ترامپ و نتانیاهو شکاف ایجاد شده و ممکن است برای یکدیگر به «بار انتخاباتی» تبدیل شده باشند
🔴
هیچ واکنش مستقیمی از سوی دونالد ترامپ، رئیس‌جمهور، یا کاخ سفید [به رد طرح پیشنهادی صلح ترامپ در غزه از سوی اسرائیل] وجود نداشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/141264" target="_blank">📅 09:37 · 21 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

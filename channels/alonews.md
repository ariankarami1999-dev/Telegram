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
<img src="https://cdn4.telesco.pe/file/Ba70mH17qF5gSeJsIf0rVjuOb9zuzSqTcJ9ZWYCNaJSEbL28_wf6dADtwE6JSe5jaapxqEpYKe_npGHzgc-6CSmhK9OWZIqZKWCj58UMZzQke5sDJf3tQDF6mN97ZBLKPRbig7MYAicGsmOG7uLr93t1zbU0bq8hDXXZpFOSur4tMMmqpePiRq2wybgWFL-ooGizF2FeteTn1rG1zRmwaxnAG6krq2dY12p3yMbPK90KCPqXQi1Mqd9j30sHdz4trlqGdAZGJSh0EQNOCHLWxZiSL01yNnBdPX8KNa3v31AdBYrEvYZ9FvBQ1Oooh-xkSYQw_VbM3XtT4XQkqWZ_ng.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.02M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 02:32:07</div>
<hr>

<div class="tg-post" id="msg-149617">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPAYONET | VPN |</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZ59hp4dbvkBOwS4NT_mriuISRaLX55CyqaWzY846CJmoQZ_PkolPMD6W5iHLrR9rHCJtrIT_zzxLj55TuL6vNiR5FzH6NhT-tDAK_7Cn4I5M5KhvfJ3cTA9llMJ2lyTYnEA1M5-EZv0Mb4wreJ38N1_eDmUEs3yzdXFVjLO6miXVCZrgDPp49C3Ev9WPX7P6NDe8VYU2ILQVZs1oHfB5xi1W__sxXXMzOUGASUH01-cseWi-KFhf2VYCybwsstQqY-QlFOPpokfo89ni3XUxdIggQjrJORtMvnXXeF2PDIQ1NKcS525D_ApsUN5ZHK04E9nHTWiNZw8MAgdwJsOfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
کانفیگ v2ray نامحدود | چند کاربره
🦋
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
📍
نامحدود _ PLUS
⚡
:
🇩🇪
🇫🇷
🇮🇹
🇸🇪
🇦🇹
🇦🇿
🇵🇱
🇹🇷
🇺🇦
🇦🇱
🇦🇩
🇫🇮
🇳🇱
🇺🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇲
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
برای اولین بار در ایران
👑
کانفیگ ها بدون تبلیغات هستن
🚫
تمامی لوکیشن ها قابل استفاده در جمنای
✅
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
☄️
مناسب شرایط جنگی و اختلالات
💬
پشتیبانی تا آخرین لحظه اشتراک
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
👾
نامحدود تک کاربره  | 79 تومان
💵
👾
نامحدود دو کاربره  | 99 تومان
💵
👾
نامحدود سه کاربره  | 119 تومان
💵
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
خرید و تست رایگان از ربات
⬇️
BOT
🤖
@Payonetvpn_bot
ID
✅
@payonet_supp
❤️
CHANNEL
🫡
@payonetvpn
🔺</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/alonews/149617" target="_blank">📅 01:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149616">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
خبرنگار اسرائیلی:
حملات امشب سپاه پاسداران به کشتی‌ها در تنگه هرمز گسترده و کم‌سابقه بوده است.
🔴
گزارش‌های دریایی از افزایش حملات و کاهش شدید تردد کشتی‌های تجاری در تنگه هرمز خبر می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/149616" target="_blank">📅 01:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149615">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHrAcdI3UL53YL8ddcCtt04nXdz_x37D6Ed0sUlYttD2-2o5CrCkB8Coo-qwpKqCFpEGEXFNoQE4Tm6DET-BPXF2nnI8C2C017WhRlE8j6Tg3exlma1Rq5uxuePmTGQHqs-bgV0WIwgQoBsqTwfaH2J1thS_5iirKuQIy-H2wTM-6ZgW-crXzLTAMWR0nfyHF1CXzAaeYBLMUJ1mtv8Ds3AZ2bYFtSflicECV1D2lkw0iL1-FhQ7Lf3Ekn_xZlb-uUQ9l8mjzb5jjR-J8jP_LoAEUD4wsCk5yf85jZHS25s3Ev_ZAHRK0aAi472L9KKNvD50alKFyueVDAH-fepyqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توهین عجیب به پزشکیان در ایتا
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/149615" target="_blank">📅 01:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149614">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
نیروی دریایی سپاه: در جنگ جدید، شناورهای دشمن در اقیانوس هند هم امنیت نخواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/alonews/149614" target="_blank">📅 01:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149613">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vixZ0CqyOjkK_ePtIosjNgncDr-PyzbhtICLXzNxtMrzkLsjYjlOKUagn_FI8y_T32ZrUAYaoEfICn3Ao0TLYWkwcOMFE8h9Ega2jh_yxQPzq4qIKxJouznPowoPwA2pcXLDafiPhjeBSvz6yve_9QdJwoTqeRLu-FPpu9YhHQF-cKKsWYPdlJIKj-GDDJhtX1ZNMot_d67zcrTGGj568Ev6tQHwsCFdLpPtl-bBX-4aBaGSwKplqPwk1aDNX4sReWBzOOhwE89y2knedbf1A6552pP0lx8W-vH_rd3lm-fYgXqR2Jk-YQ--hp-JGcdLn_TWokIgeW0xlRUhVAraoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی:
از شروط خود کوتاه نمی‌آییم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/alonews/149613" target="_blank">📅 00:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149612">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b0c9e9f6d.mp4?token=BXgitTZjZTCwQJ5UXerVTipn38p1Ho1kPpP6U8z9fw--iRXFbKwiQiZGoZFLfvTo9a0pKMGJ5SJvETRDxhFHN4tkmAYifoQxEs0hY287uZi3hfs9Gt0lXkHwl0IoY8sJuB9kc8jJjOHnurXh8rjDTOB55SjPW1hVNDGA0fnWQjBaUexz_xrGs2kMoS-eIFUHB1gg9wsAcPPpuhIXrU_Qt21wWklJhu9aQfR9bwg00wUEcX4C0b8q6yfG7OwMlmlEOzHoCrwUE1dG9R4_IFhne38kGjZC-9fTB_m0uekeT0kjZAs_fXtnYmjnrecfViTYq0ZDKdmQEo4l0rm2-qZsKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b0c9e9f6d.mp4?token=BXgitTZjZTCwQJ5UXerVTipn38p1Ho1kPpP6U8z9fw--iRXFbKwiQiZGoZFLfvTo9a0pKMGJ5SJvETRDxhFHN4tkmAYifoQxEs0hY287uZi3hfs9Gt0lXkHwl0IoY8sJuB9kc8jJjOHnurXh8rjDTOB55SjPW1hVNDGA0fnWQjBaUexz_xrGs2kMoS-eIFUHB1gg9wsAcPPpuhIXrU_Qt21wWklJhu9aQfR9bwg00wUEcX4C0b8q6yfG7OwMlmlEOzHoCrwUE1dG9R4_IFhne38kGjZC-9fTB_m0uekeT0kjZAs_fXtnYmjnrecfViTYq0ZDKdmQEo4l0rm2-qZsKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیوی معناداری که ترامپ ری پست کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/alonews/149612" target="_blank">📅 00:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149610">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/L0PLNCRBLdMF4AjCeucqNchEcTYAQ2meiaNK32z5BoIA4_Lfxzxn8QAx5NLR3S0Euh3sQOlrggPXpd4TxUpe4Nr_ttNdn-kSfNq2jDK1bRQJjLq_u2pJfhKkrI6j_09QU9kNeYj0JJINx2HSMcQNOj2GskESIio5feXqFhYk_qkCXTsaHuyad5UzJUQol1yRp-uNCcl_99mE8bSR7iVjbOm4ISBxaEJbNj71MI6foA-2DDLHVc6BnHSjOMr5d3q8ZynfkGV4NVsOnpjl1GZqiIaME7RxnboSSK82WMxCP993NZbR9bE2zMdC8bLVdK0NYPL_9gEBIUyUwKj5ahbLqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Pgza64zSthiH29lGw_Iu7fDcHxTK0OxUe951v8SV5wsCiDUFOwsCT-p8wCpT7-ucKUWOiLYu9WE1qdpNQMFiHYD2Lr2TzboefTcM2MiuITVyJoqXUovgEAkuZqLAhN1Ufoa77JhXWk3au9g-PTiKXUgYMe4G_-_0EPNN_N9JBjXEQu4bgPu6bT1YgzbacX1Rekpfpvi9ZxlTJz0Rd2RlevIp5EXbuiRt9XkAmiiPVHuGoYhYXya02d8DWfcvYy3VI0Q37_x_GgmU1iAyjdSSpC9_vuj753fcK5oYpHlChLyxYIo1BfverUjvV2WyvzIV0DB4i0y9BKrzi2FPlpdVXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
فوری/گوگل رسما ایرانیا رو تحریم کرد و از این به بعد مردم ایران دیگه نمیتونن حساب جدید جمیل بسازن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/149610" target="_blank">📅 00:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149609">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
گزارش انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/alonews/149609" target="_blank">📅 00:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149608">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
سخنگوی ارشد نیروهای مسلح: قدرتمندترین ارتش جهان مقابل نیروهای مسلح ایران زانو زد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/149608" target="_blank">📅 23:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149607">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
البوسعیدی وزیر خارجه عمان : امنیت کشتیرانی در تنگه هرمز نیازمند همکاری همه طرف‌هاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/alonews/149607" target="_blank">📅 23:54 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149606">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
کارشناس صداوسیما: ایران اصلا به نفت‌کش‌های امارات شلیک نمی‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/149606" target="_blank">📅 23:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149605">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
اردوغان: جای نتانیاهو پشت تریبون سازمان ملل نیست، بلکه در دادگاهه
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/149605" target="_blank">📅 23:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149604">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
پزشکیان: ما می‌میریم ولی سر خم نمی‌کنیم. آمریکا و اسرائیل فکر می‌کنند با این فشارها می‌توانند ما را ساقط کنند اما ما با قدرت بر همه مشکلات غلبه می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/149604" target="_blank">📅 23:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149603">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
بیل گیتس مالک مایکروسافت: بزودی ممکنه هوش مصنوعی اونقدر قوی و خطرناک بشه که حتی باعث کشته شدن ۱ میلیارد آدم بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149603" target="_blank">📅 23:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149602">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MD37q8aJrJxvJVT6R3fvMDKvTI6vCUr-dj2muPUI53R2LaOXWn2CrNmBcGdkArLd-NaPFnyMVpufKxMbtTc-bYG_b1XO7s2iv77JDp7lSrYXBmrMuGRD76EC-z-NL5MJ4m7_dkjo4Rdp8EG8Hra2N3_SlyFL0Cyz5E4Dav5Hn6eeZIbhOGacOf6sIzQp6wi6Dx_G5qFP6pUQxvo4ptNLFx6a7jVveXSQE5920ftqBK0qIkYLV7oD5zehEanlztT51BM9oB8fbb2rKODtU4IpSuwHF93vLMFTv_t6s5u_nD3kolbNkxQw6C8oYwNGC6uOJbWCo-hEUMKwyS8ipsDTMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: امروز روز بزرگی برای کارگران صنعت خودروسازی آمریکا و خریداران خودرو است! من به تازگی استانداردهای جدید بهره‌وری سوخت را تصویب کرده‌ام که دستورالعمل احمقانه مربوط به خودروهای برقی که توسط جو بایدن و پیټ بوتجج مطرح شده بود، را لغو می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/149602" target="_blank">📅 23:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149601">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHsK_aQwcs3IaaCTPFllUXksGUlBm_mvtDKQBINIx1W1AdXcUYQsGjZGU3SyM4m8Gd0dAKldMqnxlLaR5AlLVGNr3Xt---AAEXJQ3NgbmP47ExhriQWmzn1Daq6zpj8RstaanfHqL0YSLVN97bViThawPd-p2tKzGK3nmuTBe-Wd7Zrz2h_treh9b2LJVmO0DYZ_yrXFpfP4VBOkjn3UkDLT9aGJNmZF-XbLYR7OF4oIBnM-eGMJFBhTL0Aw2Op4dh67sKLxqsLJR0JPa1Smu-LOvyY6xIdBPZHh2F9aKLIehTS54bfighHFoALpH1ewqHZZ-NBjlIMiEDA1yhTcjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت اینترنت کشور
🔴
در حال حاضر اینترنت کشور به‌طور کامل قطع نیست، اما اختلال و افت کیفیت در برخی مسیرهای داخلی و بین‌المللی مشاهده می‌شود.
🔴
وضعیت: ناپایدار / همراه با اختلال
🔴
اینترنت بین‌الملل: دارای اختلال در برخی مسیرها
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/149601" target="_blank">📅 23:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149600">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
پزشکیان: ما و یمن در حمله به خط‌لولۀ عربستان دخالت نداشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/149600" target="_blank">📅 22:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149599">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
پزشکیان: بی‌هیچ واهمه‌ای آنچه را که اعتقاد داشتم در سازمان ملل مطرح کردم، شاید اگر رئیس جمهور آمریکا آن حرف‌ها را نمی‌زد ما هم این حرف‌ها را نمی‌زدیم
🔴
برای این در تریبون‌های بین‌المللی صحبت می‌کنیم که دنیا فکر نکند که از گفتگو می‌ترسیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/149599" target="_blank">📅 22:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149598">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
پزشکیان: زمانی که به نیویورک رسیدیم سخنرانی ترامپ را به ما گزارش دادند، که حرف‌هایی زده بود که شایسته خودشان بود و در نتیجه نوع فکر و پاسخ ما را تاحدودی تغییر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/149598" target="_blank">📅 22:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149597">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
پزشکیان در گفت‌وگو با شبکه الجزیره: از توافق عربستان، ترکیه و پاکستان استقبال می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/149597" target="_blank">📅 22:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149596">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
پزشکیان: نتانیاهو نتوانسته غزه را وادار به تسلیم کند، حالا می‌خواهد حکومت ایران را تغییر دهد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/149596" target="_blank">📅 22:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149595">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a56a2e5a7.mp4?token=N6EIEqsopKN8sM3ps_ZehSITrbvkZGzIMhfgC5IHhxdQaQKansQr0MqEE3uXxnRfGND7X0oy-ielzjYz7IZIdjvflYEUUj4khSg_6JtDeeDj9lfjhwu7tJ4BMb0u4vq90gRa5LGnUBgnmnIXyz2sFAkq3Yy_Yj-JZKlJ_H69Fqd-UjVxiwBiJMKv2M36PSu8C8gyyZCL8ge40kNyCzq3cx0gEopvfFKpdTmx0onKuR9VQmkFQH3Lf1IVRA6Qrcg540QGhJCcovhAHRAbW7RwTl4JTkCD1HMt-GSHVT5F8H_ITyFo53biOwqBD9Y6wGSWhVq5L8HjAeAUGkQkduJHOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a56a2e5a7.mp4?token=N6EIEqsopKN8sM3ps_ZehSITrbvkZGzIMhfgC5IHhxdQaQKansQr0MqEE3uXxnRfGND7X0oy-ielzjYz7IZIdjvflYEUUj4khSg_6JtDeeDj9lfjhwu7tJ4BMb0u4vq90gRa5LGnUBgnmnIXyz2sFAkq3Yy_Yj-JZKlJ_H69Fqd-UjVxiwBiJMKv2M36PSu8C8gyyZCL8ge40kNyCzq3cx0gEopvfFKpdTmx0onKuR9VQmkFQH3Lf1IVRA6Qrcg540QGhJCcovhAHRAbW7RwTl4JTkCD1HMt-GSHVT5F8H_ITyFo53biOwqBD9Y6wGSWhVq5L8HjAeAUGkQkduJHOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حرکت پربازدید از ترامپ
🔴
ترامپ پس‌ از دست دادن با زلنسکی حرکتی انجام می‌دهد که برخی رسانه‌های خارجی نوشتند اسمش «دست شاخدار» است.
🔴
می‌گویند افراد خرافاتی معتقدند وقتی با آدم نحس دست میدهی باید فورا این حرکت را بزنی تا نحسی طرف به تو منتقل نشود!
🔴
برخی دیگر نیز حرکت دست ترامپ را عادی و اتفاقی می‌دانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/149595" target="_blank">📅 22:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149594">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OR8wR11Vs3zFTy1Q8ixMk9ei_47-y4vnCNbSIcKrUoEW1apwBg8I00E3BZTAWz4aqapwNOD5gpKoR43Rh10o6cPUyMdFmeQmr4nJYggcE3d_21uGyZDyZsHjDO1aM-Ot1JO3I7woxHu1ag3UuwRIpEu-Y_PYsvN8hD-6OELaY_sS7xczCKPsHM448ndMw4Qfzxm4hfTgics-znitK4fifqhGzT376N4YekKYjTfaJmhOTQ0CC5wGwPbOx2P7hHYUm_JOWvpsjhKSRRBt4hzpbnNXNTb58YXPfhJ5PVhoIsBvtraHSG62Fp1Dk0TezJp6E5wU9QHR1PH-8LT3vj5yVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شش فروند هواپیمای تانکر آمریکایی در نزدیکی تنگه هرمز در حال پرواز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/149594" target="_blank">📅 22:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149593">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
پزشکیان: می‌خواهند ما با ذلت با آنان مذاکره کنیم؛ ما می‌میریم اما زیربار ذلت نمی‌رویم؛ ما اعتمادی به مذاکره با آمریکا نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/149593" target="_blank">📅 22:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149592">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
پزشکیان به تهران رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/149592" target="_blank">📅 22:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149591">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/get-_44SOqB1g5tc0XidqpyFvyWW_jpAFK6yANarQ4VEBh8m6KicERHIUdWlBajjmIOx9l-qFrkyPh3B8B5sW2XhRM-K00w-xgtqgpwMevcFbg-TxT2N7hkm8HIWppNbzIpdLHckqFqjbzmu9mCkMrxMo45F8d-_jEcOCcGu8ukDyVPWTQRK9XdG0gczewIcjLCRK5FLTRCnZ3Ap8vCcFrT-5hwHd0Ve3RRfPRRBgvUVP11EsTPkMyGJgcKn1gnmp-UepB3m2gDTW3UbdOMwNgO3SWydt71ZYstg0Wkfc66vd8-LwSMjNbcUWiNK60p6cxgwubOFtGMBecY5CyeYvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسام الدین آشنا: تجمع غیرقانونی در برابر خانه‌ها و فرودگاه‌ها نه مشکل « ناترازی»ها را حل می‌کند و نه رسوایی «ناتراستی»ها  را پوشش می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/149591" target="_blank">📅 21:54 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149590">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی مجلس:
به زودی ایالات متحده بر هدر دادن فرصت پاسخگویی به شرایط ایران برای بازگشایی تنگه هرمز و انجام ندادن توافق پشیمان خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/149590" target="_blank">📅 21:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149589">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
هواپیمای حامل رئیس‌جمهور تا دقایقی دیگر در فرودگاه مهرآباد به زمین خواهد نشست
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/149589" target="_blank">📅 21:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149588">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ترامپ: ایران دیگر پولی برایش نمانده؛ برای همین دنبال توافق است
🔴
اگر تهران به توافق نیاز نداشت، دلیلی نداشت که پیشنهاد مذاکره ارائه کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/149588" target="_blank">📅 21:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149587">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
فوری /فاکس نیوز:؛عملیات نظامی علیه ایران اجتناب ناپذیر است.
🔴
ژنرال ارشد آمریکایی به فاکس نیوز: با شکست مذاکرات جاری میان ایران و آمریکا، مسیری که در پیش داریم شامل ادامه محاصره دریایی و هوایی و عملیات های نظامی گسترده از سوی اسرائیل و آمریکا علیه ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/alonews/149587" target="_blank">📅 21:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149586">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
سخنگوی حوثی ها: با ضربات موشکی و پهپادی به تجاوزات سعودی پاسخ داده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/149586" target="_blank">📅 21:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149585">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZ0ZNqkVltmAXfNdfQe_vhc7InWPRKcTbn4thjfT00d3C7ydqKJJroM-UIdnn_5Mp0zo7oqtHWyhYt8hkQL0T4EtuZHFc7UfFRza_9KJwT_cqI_BI2dMLS9SqJRH-4YsMIvmJhkpZtrkztFXa8xidRK_PSOhTgTmSIKHZbUeExjpmQT-kL_cfaOzE3c54kgcwVo4eNplLinAXsBcBs_VyrFRRk73wkm3gozWPEZ1p2P_KiPeOXLHqxBgwj9_yKrp_nAanjJUiZtIgBHGJViy8w9z5QZ71wODeXi0iF6DA9JfhNS9Gs4zzt0nitCbDUC_sFs_d_FwZW46yNy1U7CM4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد میرشکرایی درگذشت
🔴
محمد میرشکرایی، پژوهشگر، مردم‌شناس و چهره ماندگار میراث‌ فرهنگی امروز  درگذشت.
🔴
ثبت جهانی نوروز یکی از اقدامات درخشان او بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/149585" target="_blank">📅 21:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149584">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TX8M7PLzwaRy6CWF8_78yjqEycTvqzOvjxXCSsy6ZY8_I-zvwcmdjIpR6PZid-NhGNyMAWQ8uJ-USjK9IuUS4Z7OgFsU_foU1hT7nwdkkVT8kGscmcoeh-YDRDzLfGuVOZgmv0gFI4Lq13p2z2XVn-4n8bqpmZYMfm9VDZmZAfUxfLJXVyURSb_A4yrEfLghbbK5KUGRR0BG_TzYleu_QcQfwXfcxqFVpBD3eFhLEmfPRbxEd6rVleqGY0VbFZuu-ukEXEFiC81ROqJJCq0G1we7vCPnewO4-vua1h4waXTPuVJRCrS97Hj4GPIPyBAFPdp0eSnlmCPP2rL_vz8qpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت پروازهای ایران در مقایسه با سایر کشورهای منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/149584" target="_blank">📅 21:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149583">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
محمد جعفر قائم‌پناه: حضور آمریکا در منطقه سازنده نیست و سرنوشت این منطقه باید به دست کشورهای منطقه ساخته و بالنده شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/149583" target="_blank">📅 20:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149582">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
العربیه: ترامپ به تیم مذاکره‌کننده خود اعلام کرده است که تیم مذاکره‌کننده ایران تصمیم گیرنده نیستند و با آنها نمیتوان به توافقی رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/149582" target="_blank">📅 20:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149581">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
وزیر خارجه عربستان سعودی: تنگه هرمز باید به شرایط پیش از جنگ بازگردد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/alonews/149581" target="_blank">📅 20:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149580">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtdx53AunjU1_NSCu0gvGSsI-3_lPVyvPb1bKH7r8_uU_7zoUtimffL4ojxDvnAUfyhydagGrYyVZzMR58qeQqIf78RfY18Hfshjd_80nwR5-7DYpL3k8IYJ1m1eLlQ2p-5pWdJ0oW9oCdmpy12b232cowoOetPut8ovSWIBVe8OCBT-sSbeEGu8SnrBItOUY9bJ6xTwzxSqQxeCWfGmQnQINt00ZAn1zCjXTXfmVXVghgCmzsI6omBTUWgnGPdadGSYtUDe6_n4oTUc4TK7PJNqyHTlrJ9J1-Ttz7Cp8oaQCq-EkGtvzDFqGJR86BM7SulOvIIaPWWOYOPhxLZwDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واردات برند های لوازم خانگی از مبدأ کره جنوبی آزاد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/alonews/149580" target="_blank">📅 20:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149579">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
لاوروف: روسیه معتقد است زمان آن رسیده که به دولت فلسطین رسمیت داده شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/149579" target="_blank">📅 20:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149578">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
لاوروف: حمله به تأسیسات هسته‌ای ایران، اعتبار آژانس را خدشه‌دار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/149578" target="_blank">📅 20:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149577">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
روسیه: ابتکاری را برای برقراری صلح در منطقه خلیج‌فارس و حل‌وفصل بحران تنگه هرمز آغاز کرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/149577" target="_blank">📅 20:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149576">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
هیأت آمریکایی همزمان با آغاز سخنرانی «برونو رودریگز پاریا»، وزیر امور خارجه کوبا، صحن مجمع عمومی سازمان ملل را ترک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/149576" target="_blank">📅 19:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149575">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
وزیر امور خارجه عمان: در نیویورک با همتای ایرانی خود درباره تلاش‌های کاهش تنش و تضمین امنیت کشتیرانی در تنگه هرمز گفت‌وگو کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/149575" target="_blank">📅 19:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149574">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60465d9694.mp4?token=q4_NJ19w_hHQwnV2Zl8DLp0JGO--wgvU9lYf_JBzlWCh1h9RqKiWE6RIsqH4h8ZHRt0p9JkXrC-N4Hn6wkKHTZZoA0C3fkZiqKR5jM2apZGj1GOLU8x6ivjOeLjubuin1_ZaCVMXu7zF7dV0wZ-T9OkH1d6jzmornWjY0eTUB5BCIgkdrWIxkgej1xtlR7Yr_Ure7qBCHHo3UfTKWGJlOcl8XnSFJS2C4IeGoIPrQ5ijLo5tRVloHwpih5y1hUOXZ3mA-YPr8T-i9a0lJNPGftvhLM-RbmUjtjkviCMqb8og9idB7mNZlOG-fnQsA6tPV49s7iALIxmETVdW7MsnLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60465d9694.mp4?token=q4_NJ19w_hHQwnV2Zl8DLp0JGO--wgvU9lYf_JBzlWCh1h9RqKiWE6RIsqH4h8ZHRt0p9JkXrC-N4Hn6wkKHTZZoA0C3fkZiqKR5jM2apZGj1GOLU8x6ivjOeLjubuin1_ZaCVMXu7zF7dV0wZ-T9OkH1d6jzmornWjY0eTUB5BCIgkdrWIxkgej1xtlR7Yr_Ure7qBCHHo3UfTKWGJlOcl8XnSFJS2C4IeGoIPrQ5ijLo5tRVloHwpih5y1hUOXZ3mA-YPr8T-i9a0lJNPGftvhLM-RbmUjtjkviCMqb8og9idB7mNZlOG-fnQsA6tPV49s7iALIxmETVdW7MsnLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: من از الزیدی حمایت کرده‌ام او فوق‌العاده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/149574" target="_blank">📅 19:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149572">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
چین: از بازگشت آمریکا و ایران به توافق اسلام آباد استقبال می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/149572" target="_blank">📅 19:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149571">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/819769b9dc.mp4?token=u1hzYhkybgEV-r2G0LJPdSV9UgchDTUSf6Kmcj2gMmGNcEfvwAowNsh4ukQeB6ZyNYPsmQTIXTvWIXM8zLTpoDKdFvZzRQl287ADVmsw9vJ6LoQfZNfcfYER-dZjUH2Ie3RGJnHM0Z7tRdVYIEBwAej-6-uUL6_CBGmQV7vvfm5rNOAcaIA-Z8lPurs7vU3yOfUfKX_k6jYB2frgiyi9EArGV1qriheL8dFBAgUU5JDK6pFWYGm6lpQp6hH4NEc5SXTDGrFgdd8Bw7IntOHKlYj0pal0Y1hRXSYiDSZJBiWHZKCKggWKHV8uPHdO1vv9KTkIgNvH1wRTw6bO3AemOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/819769b9dc.mp4?token=u1hzYhkybgEV-r2G0LJPdSV9UgchDTUSf6Kmcj2gMmGNcEfvwAowNsh4ukQeB6ZyNYPsmQTIXTvWIXM8zLTpoDKdFvZzRQl287ADVmsw9vJ6LoQfZNfcfYER-dZjUH2Ie3RGJnHM0Z7tRdVYIEBwAej-6-uUL6_CBGmQV7vvfm5rNOAcaIA-Z8lPurs7vU3yOfUfKX_k6jYB2frgiyi9EArGV1qriheL8dFBAgUU5JDK6pFWYGm6lpQp6hH4NEc5SXTDGrFgdd8Bw7IntOHKlYj0pal0Y1hRXSYiDSZJBiWHZKCKggWKHV8uPHdO1vv9KTkIgNvH1wRTw6bO3AemOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خارجه روسیه، لاوروف:
ما بر آزادی فوری مادورو و همسرش تأکید داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/149571" target="_blank">📅 19:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149570">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29448d7b81.mp4?token=NwQzfNVGz3T-AwvKMTmZF5eO8oGLH8PtFjcxovdwu2qwzLnJP4xwIXsoItXmGlLc4z9RE7dob2Nkg8vS_zwFFN8aVYzzX_kxp6NvHpsAm7GrVxCC41V63J1p8PFpDEy8AuApDK8gVLnPgHzqej0VVD4wB2VXcR0nH6NJacgyRVIGdwyngAdBiDB3dKiv-1VemVgUL_LdC9sWOHBSGOxEOR0_f-CNx7IlGABMUxxaDnahEVJ7hFeiLoIMQaZlA6YV3UsKSKXYrpmJ5CEngXn9S864mqv3oY8q99E_vJo6282uOm8iV7On00tvG6Npz2NFnAmssp-I1ROUkSMJSl0qaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29448d7b81.mp4?token=NwQzfNVGz3T-AwvKMTmZF5eO8oGLH8PtFjcxovdwu2qwzLnJP4xwIXsoItXmGlLc4z9RE7dob2Nkg8vS_zwFFN8aVYzzX_kxp6NvHpsAm7GrVxCC41V63J1p8PFpDEy8AuApDK8gVLnPgHzqej0VVD4wB2VXcR0nH6NJacgyRVIGdwyngAdBiDB3dKiv-1VemVgUL_LdC9sWOHBSGOxEOR0_f-CNx7IlGABMUxxaDnahEVJ7hFeiLoIMQaZlA6YV3UsKSKXYrpmJ5CEngXn9S864mqv3oY8q99E_vJo6282uOm8iV7On00tvG6Npz2NFnAmssp-I1ROUkSMJSl0qaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عملیات‌ نظامی گسترده‌ای علیه ایران در راه است
؟
جک کین، ژنرال بازنشسته ارتش آمریکا:
"عملیات نظامی اجتناب‌ناپذیر است ... حماس در حال بازسازی خود است. هزاران نیروی جدید جذب کرده‌اند و در مواضعشان ذره‌ای تغییر ایجاد نشده است ... حزب‌الله نیز با وجود ضربات سنگینی که متحمل شده، همچنان به اهداف خود پایبند است. ایران در اینجا مرکز ثقل ماجراست. اگر این مرکز ثقل را از میان برداریم، نیروهای نیابتی نیز در پی آن به تدریج تضعیف خواهند شد.
عملیات نظامی اجتناب‌ناپذیر است. این روند شامل
محاصره، فشار اقتصادی و همچنین عملیات نظامی گسترده
اسرائیل و آمریکا برای پایان دادن به این وضعیت خواهد بود؛ عملیاتی که قرار است زمینه لازم را برای فروپاشی رژیم فراهم کند.
عملیات‌های مخفیانه موساد و سیا
نیز برای تشدید شکاف‌های درون رژیم و همچنین تقویت مردم ایران برای مقاومت و، بله، دست بردن به سلاح علیه این رژیم انجام خواهد شد. فکر می‌کنم مسیر احتمالی ما همین است."
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/149570" target="_blank">📅 19:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149569">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBhf8AOnXDrqYp0gzYWllbzpbf52aE8nKgW9mragY3YQTdLechoV0fhLR_IM4-m8T-rAVWn5kO-P7f2WiVzCD4p8s2WMnutbBMxyflsiWizJ-couR2pp3t5Yggz6PL6NSuk3lfgYj5t5o_7gy27dVAo7tQ-vR2-Lx_3oNMHyPWxx2jC5TTispcrhZ1hfbUFlDb0s1PhYnCVqSIwpYMaOr5LnjsFIAyPPNQtKbv382jINuKmRtXsmFNHz5NKWsh-zgVu9oKFzjmUhKNqtFwxNPXiboLjetmxwl0G0hI8Siw4ylwwBYWsn-3u0TdMZ2SCoaF-N_6pgbQfdnO5hwNZCBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکوتراست، دنبال بهترین کارشناس‌های فروش ایرانه
🚀
✅
اگه
ساکن تهرانی
،
پورسانت بدون سقف
برات مهمه و
شرایط زیر رو داری
:
فن بیان و مهارت ارتباطی قوی
🗣️
توانایی مذاکره و متقاعدسازی
🤝
پیگیری بالا و نتیجه‌گرایی
📈
توانایی برقراری تعداد تماس‌های روزانه در محیط Call Center
☎️
روحیه کار تیمی و مسئولیت‌پذیری
👥
علاقه‌مندی به حوزه فروش و ارتباط با مشتری
❤️
💫
همین الان رزومه‌ت رو به این آیدی بفرست:
@EcoTrustHR
@EcoTrustHR
@EcoTrustHR
@EcoTrustHR</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/149569" target="_blank">📅 19:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149568">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gs_7MNiCg9cjdXKPWauF_Ii4HC8tIfkbPcmm5QUvpArmlycJVvI3xAcZDbbHG8NUxuk1mFK-s9ivAIgEOv_HlRKj-MqSEOCRkdmYU4xrqQf9N-_taXaazLAFUD1OqN7_WCrQAgFiBdF3lC9pkjZI8irymVgSu1IS6E1BTo425xg_zyGP39Eq67kGh1C195hE7AM-Em9C4IzorjLXlieRPBj9-4UnwbV5LM2OZsCz4gsfgP5MQbOS2j5flV3tBuUJt07Xn5mpW3dNCjIFtIdV6Ax_ZXPk2RL7P1bVgDcjbyeU85d4IOoV9cbaQ94kZFo4uON6byzwXyJLGEA5te1QTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فووووووووووووووووری</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/149568" target="_blank">📅 19:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149567">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
فووووووووووووووووری</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/149567" target="_blank">📅 19:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149566">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
محمد مهاجری: کمتر کسی از میزان علاقه من به سرلشکر محسن رضایی و لطف متقابل او خبر دارد.
🔴
با این حال خدمت این عزیز عرض می‌کنم حتما از مشاوران رسانه‌ای و سیاسی فهیم و دوراندیش کمک بگیرد.
🔴
نه فقط برای آنکه حرفهایش در خارج درست بازتاب داده شود بلکه برای اینکه مردم خودمان هم بفهمند منظورش چیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/149566" target="_blank">📅 19:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149565">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7a35fd24d.mp4?token=erxj2omRzXFLj9BQIkQdSKL5slis1I120kdbLooCKp0NaHTH2oaoVKMbVfA2akQXLxKQT33N_P-MGelFZ_b6DBDsbO3rVdK1y2ef1YkQWp2YM4M9yc5KZXUfZBVJpPLWoBRMMvf_BgXEYaUI5b8yRQRn--e2FL8iCKgR4GfDEr16vtkHSWvKXoJ86DiKNwmJzCZ-QwIrxH0Bq8AZTz_1mQtDLTAQgGNqZe5U7l4jjY8rGHe-oXeEJ_Ex4LDs29-uxuS_N5xPhsEaUyesos1HxfiB0M4EEdFVvfWNMIFS9552R2A0tlricNyEatkxP6OIYvjmwc9A4jv91nZZNU7IdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7a35fd24d.mp4?token=erxj2omRzXFLj9BQIkQdSKL5slis1I120kdbLooCKp0NaHTH2oaoVKMbVfA2akQXLxKQT33N_P-MGelFZ_b6DBDsbO3rVdK1y2ef1YkQWp2YM4M9yc5KZXUfZBVJpPLWoBRMMvf_BgXEYaUI5b8yRQRn--e2FL8iCKgR4GfDEr16vtkHSWvKXoJ86DiKNwmJzCZ-QwIrxH0Bq8AZTz_1mQtDLTAQgGNqZe5U7l4jjY8rGHe-oXeEJ_Ex4LDs29-uxuS_N5xPhsEaUyesos1HxfiB0M4EEdFVvfWNMIFS9552R2A0tlricNyEatkxP6OIYvjmwc9A4jv91nZZNU7IdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الونیوز خطاب به کانال‌ دارهای مخبر
😂
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/149565" target="_blank">📅 19:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149564">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6naUug4JrJvClAfVffDqsglbN3fVc8765d--6KHPj6fTGySYNYToQFm8yalWWaHSPQavSDwEyWA43DDUfa71IxjJBgevPPebJgJGf-PECiENFJHuWiyRajJ5BprEqNvcoj0n_RLBuEVLGuaBkLZbw0RK3S2Bwuw78jLu3m5ogiHKatuOuIqeJg3PCjeKUekw3icO5Tqgl39hbQAZA-Seovfzn2OhEFAXA_yWI78PVm30P4QHzQSQ6HHml0JXkPpBJv1aWLYooMw7Qns-O4OfyMLpvqP1gJSIUL7emn-YUt0h-iOk60U1BylORI9AmA1Npzu5T_avzp_CGIMzOfIXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی:
به نظر می‌رسد ترامپ تحت فشارنتانیاهو و متحدانش برای تشدید تنش، پیشنهاد ایران را که مبتنی بر تفاهم‌نامه اسلام‌آبادبود، رد کرده است.
🔴
اگر نتانیاهو تصور کند که درانتخابات شکست خواهد خورد، ممکن است برای به تعویق انداختن رأی‌گیری یا ایجاد فضای«همبستگی ملی در شرایط بحرانی» (پدیده «حمایت از پرچم» یعنی همون کاری که خودمون میکنیم)، به دنبال جنگ باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/149564" target="_blank">📅 19:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149563">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad8b3ef10.mp4?token=l9YK6VEUsoQhv_RrGiho8rdjhEH8ka_OCYJbObl0rbYvLfCEyVe4qcEcC6Fvbk2HeGfZ2OwZiymixM-yMW3Hlra4Pie_vbZ8o2iP9H4I5faRnFmrhGRMN60YLtCmFUfc1Y91yu-0uA4ZIAQz4ac3p9Sn1vAz1rurqAiqFpim7tm382E0lnE30Ndot2hu1QFWc_lRf35aWgTeJYKFC9E2GIXfctEZupm1zCBUYAYI7_ZcxRR3aRQtDaAL9vtnSGR1b5S3ftpA73x98EUoJreXqOnKSN22LYE8taKVWBQ5br93PT4HJNMn1DOYw5xplsSWYaKn9ES3y0xMmfg14uE21w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad8b3ef10.mp4?token=l9YK6VEUsoQhv_RrGiho8rdjhEH8ka_OCYJbObl0rbYvLfCEyVe4qcEcC6Fvbk2HeGfZ2OwZiymixM-yMW3Hlra4Pie_vbZ8o2iP9H4I5faRnFmrhGRMN60YLtCmFUfc1Y91yu-0uA4ZIAQz4ac3p9Sn1vAz1rurqAiqFpim7tm382E0lnE30Ndot2hu1QFWc_lRf35aWgTeJYKFC9E2GIXfctEZupm1zCBUYAYI7_ZcxRR3aRQtDaAL9vtnSGR1b5S3ftpA73x98EUoJreXqOnKSN22LYE8taKVWBQ5br93PT4HJNMn1DOYw5xplsSWYaKn9ES3y0xMmfg14uE21w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پست
اکانت ریاست‌جمهوری ایالات متحده آمریکا در فضاهای مجازی که فیلم‌هایی از انهدام تجهیزات نظامی سپاه و منهدم کردن بیت رهبری گذاشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/149563" target="_blank">📅 19:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149562">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maNOe2AfT2jyZv-fMkvhhM7Md8DtfMeCEnzvIaxMApBEOu2dwpjvWwyaRrT-A5PV9NI7UGixlaCg8auBNeqpE43cJgHR1SpLZ6mowtBbuixnXicAOs1dvikIN6KOfEXtYqbnROxTEPZg9Oh46Ld8TWZUrPhJ0zJFm1p42XeogWFivQftYGkskYGcwlFwpkSL0SPut9a1pf14TZpcri2AGwKoxcwFBFLG6CtS87kYDljVf38s8WIrEIQd2JhkNQAEgP4tWP8hs4gWxwzKDtjUspdPim1xRZjcEx8e8WtuBywphUYShEMR7HZfYJViLvvSPicrHel7CYFkHfNwhhNoJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
واردات سامسونگ و ال‌جی آزاد شد اما محاصره‌ایم
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/149562" target="_blank">📅 18:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149561">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfuuHESYjx8eR05BPB5K6sLLhR5WMUYC4Ue0_teDufSHb17uYgIj_DAUjE12lXEnoZ09DVUxLtUa5ImPv7_gU88PWDkvNAHl2AbcoTvnXA3eBJSCX-aODZ8R8Szf5BTMm7Tvnxz69NtsqiHg0-r0PyA_ttKG4n1VXtNiDFzDfMq0U7Pm2JdoWJwvLBGkMs9zJRlWA9fr5fphbpWeHF6Gm2FHvN7Kk2Z4PjXZHOYrlJLMh901HYixE_ZtEljNfSeVC1RpEdUY1dN97I2EMAm6nOZEtuVjAhmG845ik83CMymqnNQowqld6s6RVIAV2giKWSMEBTk0Owg8baLjBCMQRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: من یه پزشکم خب؟ آقا مجتبی تونست ۷ساعت رو زمین بشینه و بامن حرف بزنه پس سالمه
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/149561" target="_blank">📅 18:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149560">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رسانه‌های آمریکایی ادعا کردن، نتانیاهو داره آماده یک حمله تنهایی به ایران می‌شه و اگه حس کنه وضعیت انتخاباتی خوبی نداره، جنگ رو شروع می‌کنه   @shahab_gold_trading</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/149560" target="_blank">📅 18:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149559">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41e294531f.mp4?token=qvND9kDVJw02Vj8RNShhicn_nOEnoV4l5yfAXA6rtNlridEJVDyDBskSETrVSYGTnI3OSBZpccq90ylXOFMX6gOoQ2xHCv1CI1Se1kRrAC19djLr3jMK_olDVq4YW1F5F_vBSqSHRlDCfeOzNIm_wiloRCRoWFxWtUOLLgNUkc6dmAU6AopcgW7yBkNkpm3ypsEv-Qus2KjJzM3w2kpmZOL3RNkeEE1o_Lr5KqMMQ0Gbffd_NqsHS0bV7Ew4PN5QMMXRl6GzPd5hW2KMMIe9hjABF9vMurEAyqDOZxOi2dT_jKWxto11u93lywh66uBKleaftKpJ1CVPeNt8MzqQ-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41e294531f.mp4?token=qvND9kDVJw02Vj8RNShhicn_nOEnoV4l5yfAXA6rtNlridEJVDyDBskSETrVSYGTnI3OSBZpccq90ylXOFMX6gOoQ2xHCv1CI1Se1kRrAC19djLr3jMK_olDVq4YW1F5F_vBSqSHRlDCfeOzNIm_wiloRCRoWFxWtUOLLgNUkc6dmAU6AopcgW7yBkNkpm3ypsEv-Qus2KjJzM3w2kpmZOL3RNkeEE1o_Lr5KqMMQ0Gbffd_NqsHS0bV7Ew4PN5QMMXRl6GzPd5hW2KMMIe9hjABF9vMurEAyqDOZxOi2dT_jKWxto11u93lywh66uBKleaftKpJ1CVPeNt8MzqQ-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تجمع بیکارها و الاف‌ها در فرودگاه مهرآباد و شعار علیه پزشکیان و عراقچی
🔴
این‌ جماعت معلوم نیست درآمدشون از کجا هست که هر روز ول هستن از اینور به اونور
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/149559" target="_blank">📅 18:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149558">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) : در پی شناسایی تسلیحات که نیروهای ما را تهدید می‌کردند: ارتش اسرائیل یک انبار تسلیحات متعلق به سازمان تروریستی حزب‌الله را در منطقه سجد در جنوب لبنان هدف قرار داد
🔴
ارتش اسرائیل امروز (شنبه) یک انبار تسلیحات متعلق به سازمان تروریستی حزب‌الله را در منطقه سجد در جنوب لبنان هدف قرار داد.
🔴
این حمله با هدف رفع تهدید انجام شد. در این انبار تسلیحاتی نگهداری می‌شد که برای آسیب‌رساندن به نیروهای ما که در منطقه امنیتی فعالیت می‌کنند و مختل کردن فعالیت‌های آنها مورد استفاده قرار می‌گرفت.
🔴
ارتش اسرائیل به اقدامات خود برای رفع تهدیدهای فوری ادامه خواهد داد.
هرگونه استفاده از خاک لبنان با هدف آسیب‌رساندن به شهروندان اسرائیل یا نیروهای ارتش اسرائیل، با قدرت پاسخ داده خواهد شد.
🔴
ارتش اسرائیل همچنان به توافق میان اسرائیل و لبنان متعهد است.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/149558" target="_blank">📅 18:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149557">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">الان عراقچی میاد میگه شروع خوبی بود</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/149557" target="_blank">📅 18:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149556">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
آکسیوس: مذاکرات همچنان سازنده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/149556" target="_blank">📅 18:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149555">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
اکسیوس:
در حالی که ایران می‌خواهد هرگونه مذاکرات را بر موضوع تنگه هرمز و محاصره دریایی آمریکا متمرکز کند، دولت ترامپ خواستار آن است که ایرانی‌ها با امتیازدهی در موضوع هسته‌ای موافقت کنند.
🔴
مذاکره‌کنندگان آمریکایی در جریان مذاکرات روز سه‌شنبه به ایرانی‌ها اعلام کردند که ایران کنترل تنگه هرمز را در اختیار ندارد و بنابراین نمی‌تواند درباره آن مطالبه‌ای مطرح کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/149555" target="_blank">📅 18:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149554">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d83c735408.mp4?token=fy21mQoK-WsejSd09pimvidWPHY3pd2h76JKKFWz-CpXTn5s-rAa_tigBqq_aEgbILKWKEg2z-YOzknntcOag6YMoH0azvq4U2_lQKuyUfgBtdjUO972EA-kyFe9TY-Ed498aNXa8DB8f4dGpAQvjpKN9Z6YS6qG32IzXmt3tlZ3SzAzdlxqR8KrcQKHjQCVp1jBeO-pATFt4nH378K-mt9OwniUikvHqPzqbkYdlioOIz2oO9maxx6NRokVrPmbcyk_TiaFJu47S19jUvjmkKIBLcq3ufLrPsYG7IiBJdzPaw46pbakaQMKiaUd8pX_-pE6sKGL5Zqn_FMZXKJ8PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d83c735408.mp4?token=fy21mQoK-WsejSd09pimvidWPHY3pd2h76JKKFWz-CpXTn5s-rAa_tigBqq_aEgbILKWKEg2z-YOzknntcOag6YMoH0azvq4U2_lQKuyUfgBtdjUO972EA-kyFe9TY-Ed498aNXa8DB8f4dGpAQvjpKN9Z6YS6qG32IzXmt3tlZ3SzAzdlxqR8KrcQKHjQCVp1jBeO-pATFt4nH378K-mt9OwniUikvHqPzqbkYdlioOIz2oO9maxx6NRokVrPmbcyk_TiaFJu47S19jUvjmkKIBLcq3ufLrPsYG7IiBJdzPaw46pbakaQMKiaUd8pX_-pE6sKGL5Zqn_FMZXKJ8PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: باراک اوباما اخیراً گفته است: «اگر برای دو سال زنان را مسئول همه دولت‌ها قرار دهید، اوضاع بهتر خواهد شد.»
🔴
دونالد ترامپ، رئیس‌جمهور آمریکا:
«من زنان را دوست دارم و فکر می‌کنم فوق‌العاده هستند. اما این واقعاً چه حرف مضحکی است، درست است؟»
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/149554" target="_blank">📅 18:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149553">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ایرنا: عراقچی فعلاً در نیویورک می‌ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/149553" target="_blank">📅 18:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149551">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
تیرخلاص ترامپ به تفاهم‌نامه با ایران
🔴
العربیه: ترامپ اعلام کرده که امکان بازگشت به تفاهم‌نامه با ایران وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/149551" target="_blank">📅 17:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149550">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=PFKb3FQkHNmpMxO_EX931lCklEvIrgmCK1ZTn9P4-RQP1N4_bkXYzomYtNce5ejsXp8iLnnTStzqkY7KJLaPC4V_SroWHBb2Sv3lAn_HdynnVDunEiOd_tWeI7Uu9dT1s_nuFe5Bnz2y74eK8b27phOD_9i6xYfHSGDfzqGfzU_lNVot9eO5iX_965oIo7Bo7IANiywWGXsPHUkNz1VZaLrtCUMoTbg2vOvDADa5eOJdZURdcNu1JanHZQy7vpSQlys_IT5rp8xWSSpm_rXUEptaOHVpUOBV0GLdUpH2Pk3A5n1MbNX0iB_DVR0jMgr_HxoGMZxLwtk9lY2YY4FIpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=PFKb3FQkHNmpMxO_EX931lCklEvIrgmCK1ZTn9P4-RQP1N4_bkXYzomYtNce5ejsXp8iLnnTStzqkY7KJLaPC4V_SroWHBb2Sv3lAn_HdynnVDunEiOd_tWeI7Uu9dT1s_nuFe5Bnz2y74eK8b27phOD_9i6xYfHSGDfzqGfzU_lNVot9eO5iX_965oIo7Bo7IANiywWGXsPHUkNz1VZaLrtCUMoTbg2vOvDADa5eOJdZURdcNu1JanHZQy7vpSQlys_IT5rp8xWSSpm_rXUEptaOHVpUOBV0GLdUpH2Pk3A5n1MbNX0iB_DVR0jMgr_HxoGMZxLwtk9lY2YY4FIpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صدا و سیما:
اول ما پیشنهاد آمریکا رو رد کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/149550" target="_blank">📅 17:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149549">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3Oi2mSa2zmXqBEUU1jKeXjNSN5aar1Ul3zwBxxqQJXJZSPfWTsMGD2NkIp7c_jpYOzqTxttxVgmyTuFtsyxMwQpQmVj5Gk6SOIGm2V9SSvglcHFvdgEb_VZI79opjew5iPN8W4tqL2ZBKpSf8BN828wOXOL6Swf7ZPZlShgwgBQRDcv9T24NXH9KAzZG0xoQzIbINUOmV2GDfd_A-BF-4b1HGgDpJibD8dBHTT1YNDI0N7phuQalH7iLmeqrJnXVe4MP0P3nABGooRqiNQitZJBJJBxs0o1XLel6FMqpSMxY9RjfyV7vZs22NtF20OepRgvs9IBNrWNiAu4oJ-1gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۴۰میلیون بشکه نفت طی روزهای اخیر از تنگه هرمز رد شده و عملا تنگه برای همه گشاده جز ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/149549" target="_blank">📅 17:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149548">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/753abf70cb.mp4?token=e-eWjW0xdxZeuLtnEm5apG0Nx9WBzX0dNrYH4KTjxWCa6dgTQkWu3qJ7nTzVO-AFQ2dPYoEX5W9SIxotIXjCTwrfdyyPvcuU99Rl1WBukkEg2tVEvzeBAFh7ybgs3gUhxrwLfbW9kFhkuoOqpCpANVRCK09pO4WhXafLwNAsorbrje5wtbcC0KkIBl9ZtUlUKPZf43QbGWlYvPe15aVpqo4pfdntnSIN6TO0lKEvc-awvSF2uurqeh6-Kejx6q7P6wb68RPtY3Ia6rTZPYhnEWUp6OxYalxk_AfPedN71UmzUGa6kfxLHp-YFyPdZSHbHW4LmLBGKif_RwOORvZOwaD5hYgt-MxsouhHcAscqTS6F-_yrJRCsSE43Uc0z2UwIptQdRRVldsUwDPyejEuVu8XskX5oNIBpepmvfuuvTpYW0dAeVcKmQMFx-QHC1LQNElYXHhol-8ghFQP3IZZGQAhcOciHF-GfBe6VZ_GjHvHAaSFLntd7mIjxn_8Y9y1xMuprc3iMc6jULEC0kr63dkbiYw2ltM9LUzy01Arw2LWEuPQFwHc2Cs1edApNoQZwiAttkqwTQ45WRq0sk09dhKfYMsy01Z92QQxZOsD17L7xyBulzfSToHtbLilP5TznLwqNiVpTCHrM66YI_5eaLsG-Are-_t00CjR3LFua2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/753abf70cb.mp4?token=e-eWjW0xdxZeuLtnEm5apG0Nx9WBzX0dNrYH4KTjxWCa6dgTQkWu3qJ7nTzVO-AFQ2dPYoEX5W9SIxotIXjCTwrfdyyPvcuU99Rl1WBukkEg2tVEvzeBAFh7ybgs3gUhxrwLfbW9kFhkuoOqpCpANVRCK09pO4WhXafLwNAsorbrje5wtbcC0KkIBl9ZtUlUKPZf43QbGWlYvPe15aVpqo4pfdntnSIN6TO0lKEvc-awvSF2uurqeh6-Kejx6q7P6wb68RPtY3Ia6rTZPYhnEWUp6OxYalxk_AfPedN71UmzUGa6kfxLHp-YFyPdZSHbHW4LmLBGKif_RwOORvZOwaD5hYgt-MxsouhHcAscqTS6F-_yrJRCsSE43Uc0z2UwIptQdRRVldsUwDPyejEuVu8XskX5oNIBpepmvfuuvTpYW0dAeVcKmQMFx-QHC1LQNElYXHhol-8ghFQP3IZZGQAhcOciHF-GfBe6VZ_GjHvHAaSFLntd7mIjxn_8Y9y1xMuprc3iMc6jULEC0kr63dkbiYw2ltM9LUzy01Arw2LWEuPQFwHc2Cs1edApNoQZwiAttkqwTQ45WRq0sk09dhKfYMsy01Z92QQxZOsD17L7xyBulzfSToHtbLilP5TznLwqNiVpTCHrM66YI_5eaLsG-Are-_t00CjR3LFua2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا:
«من اخبار واقعی می‌خواهم و عاشق رسانه‌های آزاد و مطبوعات آزاد مثل الونیوز هستم.
🔴
چیزی که دوست ندارم، رسانه‌های جعلی هستند؛ مثل شبکه‌هایی مانند CNN که بینندگان کمی دارند، یا MSDNC که فکر می‌کنم حالا نامش را به MS NOW تغییر داده‌اند. می‌دانید چرا تغییرش دادند؟ چون میزان بینندگانشان بسیار پایین بود.
🔴
چیزی که من دوست ندارم، اخبار جعلی است و آنها ۱۰۰ درصد اخبار جعلی هستند. در دو سال گذشته، بعید می‌دانم حتی یک گزارش خوب درباره من منتشر کرده باشند؛ در حالی که من در انتخابات با اختلاف زیادی پیروز شدم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/149548" target="_blank">📅 17:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149547">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
ترامپ: آنچه آنها می‌خواهند انجام دهند، این است که تنگه هرمز را فوراً باز کنند. می‌دانید چرا؟ چون دارند از پا درمی‌آیند.
🔴
آنها پولشان را از تنگه هرمز به دست می‌آورند. بنابراین، خودشان خودشان را گول زدند.
🔴
آنها گفتند: «بیایید تنگه را ببندیم و برای جهان مشکل ایجاد کنیم.» بعد من وارد ماجرا شدم و ما بزرگ‌ترین محاصره تاریخ نظامی را ایجاد کردیم. این یک دیوار فولادی است.
🔴
حدس بزنید چه اتفاقی افتاد؟ آنها حالا دیگر پولی ندارند، چون می‌خواستند تنگه را ببندند.
🔴
و من گفتم: «بسیار خب، ما هم آن را برای خود شما می‌بندیم. اما بقیه می‌توانند از آن استفاده کنند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/149547" target="_blank">📅 17:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149546">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ترامپ: ایران خواهان توافق است و من هم از توافق خوشم می‌آید، اما این پیشنهاد غیرقابل قبول است.
🔴
ایران با بستن تنگه هرمز خود را در مخمصه انداخت و ما بزرگترین محاصره تاریخ نظامی را بر آن اعمال کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/149546" target="_blank">📅 17:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149545">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏
🔴
فوری/ترامپ: پیشنهاد ۷ شرطی ایران را رد کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149545" target="_blank">📅 17:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149544">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏
🔴
فوری/ترامپ: پیشنهاد ۷ شرطی ایران را رد کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/149544" target="_blank">📅 17:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149543">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
العربیه به نقل از یک منبع آمریکایی:
ترامپ به تیم مذاکره‌کننده ابلاغ کرده است که بدون اقدام اولیه از سوی ایران، هیچ توافقی در کار نخواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/149543" target="_blank">📅 17:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149542">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec46292c4c.mp4?token=G1j5b_KT2H36X_NljiagX0voAK4C_URTxUyf_CM9C6w6hbBidInNMZhjMYnvQYYaZQ9_ag6DnptZORrlhxztEu2VPCIYjXOsXy0XL8e_3scJ9-2OMEsd057efoK7DTuITklrQRLy-XcBgN__Lkmbnxh4KCwdYOY6-CNhpMjOR3cL2QbDQ52h9TUZvtgpSpYiR-NO0xslBcd6KyARk9XVC48rM2pG_f7qQY69I5CGuH_n5Ir67BI_nmwWfqkehiXLHonk1koae6p-9ofWwnEL0t0Dt21Q1X403cbyMiJaxa0ij5VXJHk39Kgt2OAG0yz0-BBJ1_e2yqVehkbYTEH7Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec46292c4c.mp4?token=G1j5b_KT2H36X_NljiagX0voAK4C_URTxUyf_CM9C6w6hbBidInNMZhjMYnvQYYaZQ9_ag6DnptZORrlhxztEu2VPCIYjXOsXy0XL8e_3scJ9-2OMEsd057efoK7DTuITklrQRLy-XcBgN__Lkmbnxh4KCwdYOY6-CNhpMjOR3cL2QbDQ52h9TUZvtgpSpYiR-NO0xslBcd6KyARk9XVC48rM2pG_f7qQY69I5CGuH_n5Ir67BI_nmwWfqkehiXLHonk1koae6p-9ofWwnEL0t0Dt21Q1X403cbyMiJaxa0ij5VXJHk39Kgt2OAG0yz0-BBJ1_e2yqVehkbYTEH7Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استاد مطهرنیا: جمهوری اسلامی بیشتر از پهلوی، منافع آمریکا رو تامین کرده
🔴
جمهوری اسلامی اصلا تو وزن آمریکا نیست که بخواد جنگ کنه، مثل این میمونه از ارتفاع ۱۰۰متری تو ۲۵سانت آب بخوای شیرجه بزنی(مترادف گنده گدزی)
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/149542" target="_blank">📅 17:12 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149541">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMlf0viM1EwiWx_8RPy0Kivi0n5f2uk0pat9O1ui8HulCO6--Dh9OrUBoGzNUHN2FzuT24paYEJKxiCM3ytSDvbZc4Hq6CbaG7jQVVQ2joNRdH0uhkhOBHXJCxvijUq8C_2JFd7lWOaUKf7xZJcEJ8KdpSxKp2z3TnIPrdCDGOHYcj8VtpT4cFhqOTot4hFE7bcuOSOagh7dagP-A2lBMtZzs8Dmry58FyduoVdq3EjsSV68pPG3UJ_QEhjn7eAldgFJIpymVGseIWlcTCLAsfujXjB3EOCx0LBPP2waNCvRoxnHmRvOjOZc-P2UE7y2U0IpTVDorSJhaq5feZDzXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
احمد جانجان فعال بازار سرمايه : سردار دهقان به ثابتی پس گردنی زد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149541" target="_blank">📅 16:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149540">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
دو انفجار در تنگه هرمز در حال حاضر رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/149540" target="_blank">📅 16:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149539">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8Bq3wjyL-VQ0HKMzgQJmRp-b_i40UnKvjBHxxRkhlC3ITp0RzEe9qbaIRPU8ft3sGWC1zt4lZd2ZbuRy9GU2-eb_z6kZ7sJNabSPEp5QFjSqvATrfuXrPCzGQK8eJxYQV8xUmrw5ryvm5SlN_1J0ZzIp4nL5hKg8rW9n-pfFfH6-MIXDWghu96t2TRBIV92Pb9oVONAnFkE1ZOd6yBDLsrw0PwL0Edi1Ql902oc8LNEXnujeRqpvFwogVHtEoOAItZKwPe-FwihOPZ0wadjRl4jU3oKN4p3rlbLrq9eoG6RJ7ODfJf9dgwy9CMWtI2s9yZqWVw67bqCZq9VmcAD3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/149539" target="_blank">📅 16:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149538">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دلار منفجر میشه
‼️
این پسره یه تحلیل عجیب گفته
😐
👇
https://t.me/shahab_gold_trading
https://t.me/shahab_gold_trading</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/149538" target="_blank">📅 16:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149537">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4beefbece2.mp4?token=vWJbynYwWqeNnWupfhkS6e0wgNTr2OAyS5O7AN5PRCHr7o2T4rGFdtcJNoinLxWj0PiuJOdJMeY_foo97IB1RhxYm7OZkkehds5e9ZZkpi9mLWW_Rr6RJfQvPe0ZlOjQpbVLzBt9HTgqZ1o8vV3rjUkVsszoyrCrdqvyrcts-Y-waK5g9DhNu_gJqAJhN_gW38Skf1xIz-vVX20IVQ0GIteedpWL3ODO4HsY69wBE1DLr2zMQIfut6xvukmvNRHUDakyWm0ZEEGbobj4lU-9umirwBt-NGKCjYW_sxzCByHBZ5hVYHQT7EUF-0GRdf-mTCIesXUhTntfjx5bxLlS9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4beefbece2.mp4?token=vWJbynYwWqeNnWupfhkS6e0wgNTr2OAyS5O7AN5PRCHr7o2T4rGFdtcJNoinLxWj0PiuJOdJMeY_foo97IB1RhxYm7OZkkehds5e9ZZkpi9mLWW_Rr6RJfQvPe0ZlOjQpbVLzBt9HTgqZ1o8vV3rjUkVsszoyrCrdqvyrcts-Y-waK5g9DhNu_gJqAJhN_gW38Skf1xIz-vVX20IVQ0GIteedpWL3ODO4HsY69wBE1DLr2zMQIfut6xvukmvNRHUDakyWm0ZEEGbobj4lU-9umirwBt-NGKCjYW_sxzCByHBZ5hVYHQT7EUF-0GRdf-mTCIesXUhTntfjx5bxLlS9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اعتراض گسترده‌ای در مادرید در واکنش به آنچه برگزارکنندگان آن «هجوم ده‌ها هزار مهاجر غیرقانونی به سئوتا» می‌خوانند، در حال برگزاری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/149537" target="_blank">📅 16:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149536">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
خبرگزاری معتبر تسنیم: هیچ هیئت فنی از ایران به نیویورک جهت انجام مذاکره با آمریکا سفر نکرده است و این مطالب صرفا خبرسازی رسانه‌ای است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/149536" target="_blank">📅 16:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149535">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
شورای عالی امنیت ملی: اینکه ایران در مقابل محدودیت‌های هوایی اخیر دست به مقابله به‌مثل نظامی می‌زند، تکذیب می‌شود
🔴
مذاکرات میان ایران با کشور‌های مربوطه برای رفع برخی محدودیت‌های هواییِ غیرقانونی ایجاد شده، با جدیت در حال انجام و پیگیری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/149535" target="_blank">📅 16:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149534">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
کوثری، نماینده مجلس: ما به زودی اقداماتی را برای شکستن محاصره هوایی انجام خواهیم داد و ضربه‌ای به آن‌ها خواهیم زد که باعث پشیمانی آن‌ها از این تحریم‌ها شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/149534" target="_blank">📅 16:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149533">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
کوثری، نماینده مجلس: ما به زودی اقداماتی را برای شکستن محاصره هوایی انجام خواهیم داد و ضربه‌ای به آن‌ها خواهیم زد که باعث پشیمانی آن‌ها از این تحریم‌ها شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/149533" target="_blank">📅 16:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149532">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzS5XTLU1Jgv0q50bYHhxKOYWsrcWx-4XHAY3mI5h6GxACYdCZBZxKn6K83TgAiGs_XHwHpNw6yn4TTCwTY7rnzkk59-6MWYAl3LtqMHLK7k_Tls4vbnmcKHr_PYQvAbjniwBuQNC0Nvs4IIn5YSEguXiU-iq1OhV_aQjy_kF9nz_ZkcM5ToO1096I01fa52BOcgEBAbbMV4lMuNj2H5bax17C9GTyHajOLQDl7UHSHEu9ZQ97k8xAN5kAgqpxF3RjKS9yt2VLsOYqAbFt8ZXCEw1fsP0QUMZSK8BWIG43jHT1wARsMEoQVqqO4yJiZ8qQNjU3XLNAS1MOeHem68xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : اخبار دروغ نباید در کاخ سفید اجازه انتشار داشته باشند!!!
🔴
این وضعیت مدت زیادی است که ادامه دارد و هزینه‌های بسیار سنگینی را به کشور ما تحمیل کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149532" target="_blank">📅 16:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149531">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
سعید آجرلو، عضو کمیته رسانه‌ای تیم مذاکره‌کننده:  آمریکایی‌ها در ابتدا پیشنهادی برای توافق ۳ روزه روی میز گذاشتند که محتوای آن عمدتا از جنس اسلام‌آباد بود
🔴
اکنون ما آن پیشنهاد را اصلاح کردیم و شروط خود را به آن اضافه کردیم این جمع‌بندی در کمیته مذاکرات در شعام انجام شده
🔴
در پیشنهاد ایران، از موضوع لبنان تا پایان جنگ، معافیت نفتی و لغو تحریم های جدید و محاصره وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/149531" target="_blank">📅 16:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149530">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ترامپ :ایران نباید به سلاح هسته‌ای دست پیدا کند!!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149530" target="_blank">📅 16:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149529">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c277f60d17.mp4?token=Gefy6DEnqRZoKmNpZcNm6Oab5Ln8apDU1Vj6LqlNGjIsej0_cqb_fE18bbdXbMFm9yjRi61H2tesSFi-fE_0w20j0m6eQdyMknSAHBHUY4suxwwJcV4fDl9-i06ZVlrjV6ZvidStfvscoLRGHSvDtGYaVW7USUJC8x30Pr0Gy1U3kQ8HwHfFsTfYrwNtoEX2KOaVgQoGgjybjsc0njh0gyCmxSnrvUhODOGTa6zYBMWUxHtUw9Xr44c9it7e4v9_-sVXdR9nFaq0vmVeQH40NIbj5acdglTOM1YQGGVCZIkO-btwCO_9ezcohhe6HUTJ-7-u1fEwNL8CKd8j-JqeWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c277f60d17.mp4?token=Gefy6DEnqRZoKmNpZcNm6Oab5Ln8apDU1Vj6LqlNGjIsej0_cqb_fE18bbdXbMFm9yjRi61H2tesSFi-fE_0w20j0m6eQdyMknSAHBHUY4suxwwJcV4fDl9-i06ZVlrjV6ZvidStfvscoLRGHSvDtGYaVW7USUJC8x30Pr0Gy1U3kQ8HwHfFsTfYrwNtoEX2KOaVgQoGgjybjsc0njh0gyCmxSnrvUhODOGTa6zYBMWUxHtUw9Xr44c9it7e4v9_-sVXdR9nFaq0vmVeQH40NIbj5acdglTOM1YQGGVCZIkO-btwCO_9ezcohhe6HUTJ-7-u1fEwNL8CKd8j-JqeWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: آقای سفیر، پیام دولت آمریکا به مردم ایران چیه؟
🔴
سفیر آمریکا در سازمان ملل: این رژیم تروریستی باید بره راهی دیگه نیست
✅
@AloNews
|</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/149529" target="_blank">📅 15:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149528">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDT1KI4nkoYY0HF5c9orAnHGGki0DdIHkePu877LsPhbxnKA2tk-tU2Zap1jevhnO94TCUH5IkfVqIz9wbzLV6FQukj805LdrFsxSdtPbdpgekJucXlzIm0L066S28iNMZBsgOhNi4EHJUXwKSnU_yUhrihRGykYmzj7ysV_OGSR7YEJ624D-8HZsSaHNNtHv-iCv-yESyxcwdR6JYVpW_j-H5eXvadCtr-cGVvh-x-UeAxtN3fwbkOD5qeQn6rCd0stQJ7rDuwd32vAIsbVnwgO7_X2BCRfynBLNlIIIUyFZV9XEKN8juSkeFTtQcitmYeDVGhsJO4OHNHg_N8rjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فروند هواپیمای نظامی باری مدل C-130H متعلق به ایالات متحده آمریکا به سمت خاورمیانه در حرکت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149528" target="_blank">📅 15:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149527">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RyV8hoDOcYtk9tY4fZ-E1ijLOdLw5em5Fwy8X03Akc1zEeyUlv0ciFceIbyj5kzY-piZOGcDmiJxmr6zmiUZEPIW1qjuDLoE2Fx1-F812KMTBE2FtimReey7G5tySMxMrtzRUHGw9wg5T2Fmdax_yqqSpZzU1AnthoRn7aytO_5Q9YUVTcsSpmR4kML9d7434fjogWbWG1yekHYkI90gBGODCMI3dFg3ZfBqhWwfJui6RzxSJiE7q3MsnIf2kMqrGNcXM5GsQZWJy-FPe8QVAbCwNuGaJkalECpjhQMqtwFv5_jFaPi-fdL4Wh0KAOw7WJuLBfvtuKuLhztYU3HEdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز ۴مهر روز سرباز هست، یادی کنیم از سربازان بی گناه پادگان بمپور
🖤
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/149527" target="_blank">📅 15:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149526">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
پزشکیان در پاسخ به سوال خبرنگار الجزیره: چرا و برای چه باید با ترامپ دیدار کنم؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/149526" target="_blank">📅 15:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149525">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وال استریت ژورنال: مقام‌های آمریکایی گفتند، دونالد ترامپ، رئیس‌جمهور آمریکا، پیشنهاد ایران برای برقراری آتش‌بس هفت‌روزه را رد کرده و به دستیارانش گفته است که انتظار دارد پس از انتخابات میان‌دوره‌ای ماه نوامبر، بمباران ایران را از سر بگیرد.  @shahab_gold_trading</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/149525" target="_blank">📅 15:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149524">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
فوری / وال‌استریت ژورنال: آمریکا با بیش از 50 کشور تماس گرفته تا اجرای تحریم‌ها علیه ایران را تشدید کند و به آنها پیام داده است: در موضوع ایران یا با ما هستید یا علیه ما
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/149524" target="_blank">📅 15:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149523">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
صدای انفجاری در جزیره خارک ایران شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149523" target="_blank">📅 15:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149522">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
مدیرعامل شرکت شهر فرودگاهی امام : پروازها به ترکیه، مالزی، چین، پاکستان و مالزی برقرار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/149522" target="_blank">📅 15:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149520">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R3v_etDHcdznT_WCgO9jie30FAqwvDVDorA2K9PjcqWFB0G2YIOfLTzbLR1MDjC9EAY9Ht4sbzv08U_F3othKRt4WhAEGATWxaOyi9jWmMvh1RPbqEywwosGinnYC66OSGRfRMDUrNN3dEDuFEU12KtlizWLovP5YbE0mKGfbZA-wMNrHrFpHRDcEWz1No3YPhdTq34MJjUlhNOg6r-kGPnW0jOKsf3SS1nZYS8AsRT0t1cFrgm7tY_b5HYrMEn7w679qIHKithpt9aZja7xUfv3Ez9ZoI6BjRb214lru8dmrQv2oIaF_OE0Y0WMq7TUtyj1aBiQoSgnfSxxxczKRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FbEmP-23LJ6_MCUGmxUm9QwM4sBlfUQFtPrzHiak_IqvIbJXEhLlSUy2yQ9e2YXF1GuUA-XU9QSUwn6Fcxu0PoavwKxxVB570GkR-__zX305SJMd5AImrppgrWZPZEhQNFTtPZm3tAqp3pZwv-Tci7zyrBqMVgYpNOJzM1eCrncmDKdcuTkf3U6YD741dpx8qw01unSPW4097ZD1LOeGMlmSnD27QVUBoZwXGGpisXvMNzxOeobKxhcTab9HwnmDSIFJRsC_iMsjmVwxeHVM2TT689rOrDcB5T2hAZy_8wArtD37h1ewIpO0kirZjNXFelWR5fJz5lFylidhvSStlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک پهپاد "گران" روسی که بر فراز اوکراین سرنگون شده اکنون به عنوان یک تزئین در یک سوپرمارکت محلی در ترنوپیل، در غرب اوکراین، به نمایش گذاشته شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/149520" target="_blank">📅 15:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149519">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
۱۱ کشته و ۳۰ زخمی در انفجاری در شمال غربی پاکستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/149519" target="_blank">📅 15:09 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149518">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
واستریت ژورنال: آمریکا از بریتانیا خواست مجوز فعالیت بانک «ملی» در لندن را تمدید نکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149518" target="_blank">📅 14:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149517">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
وزیر علوم: دانشجوهای عراقی به‌زودی به محل تحصیل خود در دانشگاه‌های ایران بازمی‌گردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/149517" target="_blank">📅 14:48 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149516">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WizKl4D8ZgHYcIJYkfpbIWUHhc1ZfRuK0MZVMPFPFO1MpW-EwAu0ns2i0APXDRujCk_hybSiC1mUeq-sQB78H7b96_6Jt7YgNzDjit2fv98yBbZJi4xZlBnI7Sq0v1IG__zCivXhBYK-r5kEp3qf98S_0smC2gGnM3trPrhHLFabJsG8QrCfmQ1N1x1H7t8ywCjgRzELoanwkFv-51_i_6WZhGjSYAeRBZyD9pj2EcOieArD7JjcMvHZ5F77ZYBYtNfVyLFP6agcEMZouR76SWCCZfFT1HVsynL7ycHzOjGOW0LpcRK7Qt9IFUqYQ09BBUkRWvKXouYm1EeEpPQrmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا:
«چرا باید منتشرکنندگان اخبار جعلی، مانند CNN و MSNBC، اجازه دسترسی به کاخ سفید را داشته باشند؟
🔴
با وجود پیروزی بزرگ من در انتخابات، تقریباً ۱۰۰ درصد پوشش خبری درباره «ترامپ» منفی است و سال‌هاست که همین‌طور بوده است!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/149516" target="_blank">📅 14:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149515">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
نیروی هوایی عربستان سعودی، پروژه‌ی تصفیه آب منطقه‌ی الأکبوش و شبکه ارتباطات در شهرستان حیفا در استان تعز را هدف قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149515" target="_blank">📅 14:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149514">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
مکرون از ریاست جمهوری کناره‌گیری خواهد کرد!
🔴
امانوئل مکرون، رئیس‌جمهور فرانسه، اعلام کرد که در سال ۲۰۲۷ به دلیل محدودیت‌های قانونیِ دوره تصدی، از سمت خود کناره‌گیری خواهد کرد، اما احتمال بازگشت دوباره به ریاست‌جمهوری در آینده را رد نکرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/149514" target="_blank">📅 14:32 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

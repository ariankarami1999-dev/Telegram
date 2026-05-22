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
<img src="https://cdn4.telesco.pe/file/Ou27ZDYrK-gZeGjJhgJtLZlXyUmTtA9ny3OQUcbs9mRofDIXXcIzm0NGOI-z8buIs8ORTwwzn50imVYasWrFMEr07wWqMZhGl3Xr4Z6yvH6JNjl-7FrXGdSyPdD0rSf3a09n0Wlh7hiUX-eMAergkYuY5mb33MY8nJPZlKnjp5-wCVRvsHEcc4KEGy1xeRNsiI-mc-bInqkiblqoFQ9T-d4BalEhIpVL8V9OVlKopZ2C6LrtvhwAQjMXF5hCqTvdKvXTY_RcU-v2wtpdtLiD4UQ8eBcIWmGkRYtuZdzJzLHrzRWrPiDZgGEHITpQI2n_EnSDgf-RWfGfCtX5wCnAPQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 168K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 22:54:31</div>
<hr>

<div class="tg-post" id="msg-75585">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔮
اینترنت آزاد با «ملوان زبل»
📦
تخفیف 24 ساعته
📦
70,00 تومان تخفیف فقط بنرو برامون ارسال کنید
💣
مثلا 1 گیگ میشه 120,000 تومان
😐
🔥
پلن ویژه:
✨
1G = 190,000
❌
120,000 تومان
✨
2G = 380,000
❌
310,000تومان
✨
3G = 540,000
❌
470,000تومان
✨
5G = 850,000
❌
780,000تومان
✨
10G…</div>
<div class="tg-footer">👁️ 905 · <a href="https://t.me/funhiphop/75585" target="_blank">📅 22:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75584">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3Mn9pzOFZ52VgHkqxRdx_WzL-M3UBSXAnbHFlF2Pp9rhwySMqsF3_Q7-0TrlGi9W3OY9NuWL_jh7RMlDfFP3BJ4oyjnK0EAAvgo7390NPh17ICjqLfJJ4oLiRplUdIWoGqARZC-bjWTqCHSb4EUJOzGaM88SFeXubOaGjq1cqT4XiKaynZU2ONY_lw3YUuuRRloAMtyJDqGoCor4sLDHf7uEUrk3fwaiNlD2Zu7ZFcAs0UmWdZL3_AU3OAZjKKTHIDdjhEwpZlpvkZAmW8gbFNIbgwwFtbIX9uGk649_lcmL_uVCt2KsH66TrRTQsJlJy9u_qNs5Ck1WLrCQMtb0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔮
اینترنت آزاد با «ملوان زبل»
📦
تخفیف 24 ساعته
📦
70,00 تومان تخفیف فقط بنرو برامون ارسال کنید
💣
مثلا 1 گیگ میشه 120,000 تومان
😐
🔥
پلن ویژه:
✨
1G = 190,000
❌
120,000 تومان
✨
2G = 380,000
❌
310,000تومان
✨
3G = 540,000
❌
470,000تومان
✨
5G = 850,000
❌
780,000تومان
✨
10G = 1,600,000
❌
1,530,00تومان
☄️
تمام سرویس ها با ساب تقدیمتون میشه
☄️
⭐️
‌تا 100G هم موجوده
⭐️
کاربر و زمان نامحدود است
🌕
✅
تحویل سریع
✅
پشتیبانی
✅
مناسب آیفون و اندروید
⭐️
. فروش همکاری هم داریم
⭐️
🔴
برای دریافت این تخفیف حتما این بنر رو برای ما ارسال کنید تا از تخفیف بهره مند شوید
🔴
✍️
برای خرید پیام بده
🚀
«ملوان زبل»؛
@MalavanZ_SUPPORT
چنل
🦠
@MalavanVpn</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/funhiphop/75584" target="_blank">📅 22:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75583">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اکسیوس:  یه مقام آمریکایی، مذاکرات رو به‌شدت «طاقت‌فرسا» توصیف کرد.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/funhiphop/75583" target="_blank">📅 22:16 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75582">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اکسیوس:
یه مقام آمریکایی، مذاکرات رو به‌شدت «طاقت‌فرسا» توصیف کرد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/funhiphop/75582" target="_blank">📅 22:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75581">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjpJdCh-P-QEn1M1En32E4aLI_P_9DLexMMYLl0VKZ2yeHV453uLvS885L_oikpipI7qzugy2nzKDESaeZtfp5Ke0K4Zb_MqVCqqEGgOb4o8BjmFaGvjLVglYPybAzI8anq3V3GeaP4LVBnwfQ0revh9qcFiUqESUCleA7MhupjYS2Rlt6o4UYNyNA2Xu5y0s-x6CPL_gdMTwAYuUdjHvJuAMOXEzrn4MG8JD1AX_WMcmxKsCmNfrRB8u2URAz_jE5Vbz_LM5wc9Yc1g8dOOYULDUr_MQyRCX8ytNbn-xm59av6meTvRCIKfDVlIx_24qbcPWyPYyEMehnNipJeH5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست خدا عیان شد حضرت آقا تو یه کشور دیگ رویت شد.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/funhiphop/75581" target="_blank">📅 21:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75580">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ:
مهریه عروس خیلی زیاد بود‌ برای همین به نشانه اعتراض در مراسم شرکت نمیکنم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/funhiphop/75580" target="_blank">📅 21:41 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75578">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ بازدید برنامه‌ریزی‌شده خود از باشگاه گلف ملی ترامپ نیوجرسی را لغو کرده و طبق برنامه به‌روزشده‌اش، در اقدامی غیر معمول در تمام مدت تعطیلات آخر هفته در کاخ سفید خواهد ماند.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/funhiphop/75578" target="_blank">📅 21:30 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75577">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">امشب یا صبح میزنن  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/funhiphop/75577" target="_blank">📅 21:30 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75576">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ بازدید برنامه‌ریزی‌شده خود از باشگاه گلف ملی ترامپ نیوجرسی را لغو کرده و طبق برنامه به‌روزشده‌اش، در اقدامی غیر معمول در تمام مدت تعطیلات آخر هفته در کاخ سفید خواهد ماند.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/funhiphop/75576" target="_blank">📅 21:29 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75575">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ بازدید برنامه‌ریزی‌شده خود از باشگاه گلف ملی ترامپ نیوجرسی را لغو کرده و طبق برنامه به‌روزشده‌اش، در اقدامی غیر معمول در تمام مدت تعطیلات آخر هفته در کاخ سفید خواهد ماند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/funhiphop/75575" target="_blank">📅 21:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75574">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دکتر بگقایی در ادامه: اختلاف‌نظرها بین ایران و آمریکا آن‌قدر عمیق و زیاد است که نمی‌شود گفت با چندبار رفت‌وآمد یا مذاکرات ظرف چند هفته ما باید حتماً به نتیجه برسیم. تمرکز این مذاکرات بر خاتمهٔ جنگ است و در این مرحله قرار نیست راجع‌‌ به مباحث مرتبط با موضوعات…</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/funhiphop/75574" target="_blank">📅 21:16 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75573">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ تو تروث سوشال: من تو عروسی پسرم شرکت نخواهم کرد.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/funhiphop/75573" target="_blank">📅 21:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75572">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">رهبری جمهوری‌خواهان مجلس نمایندگان آمریکا رای‌گیری درباره محدود کردن اختیارات جنگی پرزیدنت ترامپ در قبال رژیم ایران را لغو کرد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/funhiphop/75572" target="_blank">📅 21:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75571">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اورشلیم پست:
تهران در فکر یک حمله غافلگیرانه به اسراییل و کشورهای حاشیه خلیج فارس است.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/funhiphop/75571" target="_blank">📅 21:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75570">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دکتر اسماعیل بقایی، سخنگوی وزارت خارجه: نمی‌توانیم بگوییم ضرورتا به جایی رسیده‌ایم که توافق نزدیک است. تمرکز مذاکرات بر خاتمه جنگ است. یک هیئتی از قطر درحال مذاکره با وزیر خارجه کشورمان هستند اما میانجی مذاکرات همچنان طرف پاکستانی است. سفر عاصم منیر به تهران…</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/funhiphop/75570" target="_blank">📅 20:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75569">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دکتر اسماعیل بقایی، سخنگوی وزارت خارجه:
نمی‌توانیم بگوییم ضرورتا به جایی رسیده‌ایم که توافق نزدیک است.
تمرکز مذاکرات بر خاتمه جنگ است.
یک هیئتی از قطر درحال مذاکره با وزیر خارجه کشورمان هستند اما میانجی مذاکرات همچنان طرف پاکستانی است.
سفر عاصم منیر به تهران و این رفت و امدها علی رغم اینکه پرترافیک تر شده، تداوم همان روند دیپلماتیک سابق است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/funhiphop/75569" target="_blank">📅 20:56 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75568">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ تو تروث سوشال: من تو عروسی پسرم شرکت نخواهم کرد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/funhiphop/75568" target="_blank">📅 20:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75567">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">تو ترکیه اردوغان یه رقیب داره، ۱۵ بار نامزد شده و هر ۱۵ بار شکست خورده جلوش، الان این دوره باز اومده نامزد شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/funhiphop/75567" target="_blank">📅 20:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75566">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZr6ePPWGrupPW9tV5k5ZqT0QHZeQ3fydCyH6VfkxCd-Y7Ntj-uBvZvegU9kiWMo6zWjpZkCF25Q1LuxC49FOUdoBdlRPHc5GVLJ0XPZujC76UydjnA3vHTZ5f7e9YHnzcn-424Fm3PwvPF1CS532TaOuT-do6MkDXMNnB5fyD8kVagvdg4gIcP_W73atEV5n4HhZanDuydVDcUm6-MropxNrBbDckczIvFFhXVESiEFR6CF6T3x4W6GdP3-WJzvmKyc_S1rm4R3fgDOdc-XinlPpldieFwXdov9esbz0-JT-JZzd6NViUd3YHYC7H4bSR1E7wwUSQ8HT3V5NV2ZUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر سفر عاصم منیر به ایران تکذیب شد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/funhiphop/75566" target="_blank">📅 20:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75565">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بچه ها اگه نیاز به کانفیگ دارید میتونید از ترنادو وی پی ات تهیه کنید با بهترین کیفیت و قیمت، تا حالا بالای ده بار تبلیغشو گذاشتم هیچ شاکی ای نداشته و همه راضی بودن:
@TornadoAdmin
| خرید
@Tornado_Ping
| فروشگاه</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/funhiphop/75565" target="_blank">📅 20:02 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75564">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ: ایران مشتاق است که به توافق برسد.
ما به شدت به آنها ضربه زدیم. چاره‌ای نداشتیم چون ایران نمی‌تواند سلاح هسته‌ای داشته باشد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/funhiphop/75564" target="_blank">📅 19:37 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75562">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6Wjvl6HWXoQNBVA78ITpuJmHmEeNvJelIoCVor69DJf-2KWTvez3p3FrC9ovUaKKC8g5DUlvN3zJs070pGCOj9Cu5fIzHJDJytzWmyU-b0Xdt3_FyOSKucc6ThvbhXAnQbx8SoL_2XaOogxae63XLbJmqZS-UCURI4XobmVeaF_UaXdmcMm1hoeXkAUz1vf3TaWzB12A36Oc30lJ3u-vkYg6L2dlVOziqp40TqkKnhSNn9K0ZAK-3lmQqWNrubqI4wpPZQrB_RCEFT8K9oS2F9QTbK_gIrIOzZ6sGPBJCj3-XO3pA2Sns-0OkYHrKIyFOInzefagjizP0ii3__5lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/funhiphop/75562" target="_blank">📅 18:41 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75561">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">خبر سفر عاصم منیر به ایران تکذیب شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/funhiphop/75561" target="_blank">📅 18:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75560">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">برنا رو ادمین کنم؟</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/funhiphop/75560" target="_blank">📅 17:58 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75559">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7e5cb903d7.mp4?token=aM2odFuJZD-2OYG7yrVnR8bkywoeZiAbpxEwX5-m6okNjl8CiTi3ar-YNjK-8zL5RZp8QbVjKGtX8K8a5M27ebzNmQLDHcmbN7_exY4fZKzY_qz4Z6U8QohG72J-Qzb5qQWEf_ALeiRyQjcV94qKTCQDoZxHiM0cIw3VnBrDX-GGIVyeKISFWSFV3AVs8I2k5x0D0aAGfz7p5qZRyaZLUVVxR_B1nWg9WJAgAWG018mX3NpDtRekTKkgMEF-Ekv0IM0XrmJIYCbAuDe7ivNgogEqCCyeyUX8xVKdZjXEtbjdsL7HIeBLqlSzr6PycU6NehsDb-OLHFdVJbhhMGdjLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7e5cb903d7.mp4?token=aM2odFuJZD-2OYG7yrVnR8bkywoeZiAbpxEwX5-m6okNjl8CiTi3ar-YNjK-8zL5RZp8QbVjKGtX8K8a5M27ebzNmQLDHcmbN7_exY4fZKzY_qz4Z6U8QohG72J-Qzb5qQWEf_ALeiRyQjcV94qKTCQDoZxHiM0cIw3VnBrDX-GGIVyeKISFWSFV3AVs8I2k5x0D0aAGfz7p5qZRyaZLUVVxR_B1nWg9WJAgAWG018mX3NpDtRekTKkgMEF-Ekv0IM0XrmJIYCbAuDe7ivNgogEqCCyeyUX8xVKdZjXEtbjdsL7HIeBLqlSzr6PycU6NehsDb-OLHFdVJbhhMGdjLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/funhiphop/75559" target="_blank">📅 17:56 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75558">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ادعای منبع نزدیک به العربی الجدید:
سفر فرمانده ارتش پاکستان، عاصم منیر، به تهران به این معنا نیست که توافق در دسترس است
گزارش‌ها درباره وجود پیش‌نویس احتمالی توافق صحت ندارد و اینها صرفاً گمانه‌زنی‌های رسانه‌ای است
وزیر کشور پاکستان پیام جدیدی از آمریکا به ایران منتقل نکرده است
سفر مقامات پاکستانی به تهران در راستای تقویت میانجی‌گری اسلام‌آباد و نقش آن و تمایلش برای جلوگیری از تنش‌زایی است
تهران همچنان خواسته‌های آمریکا را افراطی و غیرمنطقی می‌داند و معتقد است مشکل در واشنگتن است، نه تهران
@Funhiphop
| ALI</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/funhiphop/75558" target="_blank">📅 17:01 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75556">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4snagvh20O5XUdzO8kwfM4N4kVJV4SrM7evvcsId6VRGXaHxtVgG50L8beJym-jNbOKdg5yoEAvW-YxA346wDHEhNWkyuJ3OcbDJYmGfP44870R81lcv7e1hERKRadAXF78LkK2jujGQxyJ7GJVjDhRC8hU5Xb5fzbR05hfmNDenqOj7-1qrNC9HlIbiFAXCtDoaKMCC5vn3SYMKlMYeriFx34M5eEdhZxg5yBuE_jp8L9mR-owg-SQ8p5lMM1izCtyd15JDTuBhVuQeVmOgXHcOX5jdrzdksYjasoU_v4igHYUxlBGVtJB-OvFMiJOytojJGht-7J_bE_c95nWGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیموتی کصکش زیدت کایلی جنره بعد هر شب میری بسکتبال میبینی؟
کونی تو اصلا نباید از خونه بیرون بری
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/funhiphop/75556" target="_blank">📅 16:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75555">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlVB8BmDPrVIO01kp6cgiYRVrsjNP7uBsvAUpqPRAIuNxgUyaJzcRKPYeKJPppHCUlIHtP8E2LERRJHhm3sWZN-ZW3_4uOzFHcmu9PPC3CH_qaGGWCOPzN26qZsSa4hV-Oa_nJYtLi-fwBkxU6lnHWhQTtotvfaHimGaSiqm7lo2T4o-YyBnzt6EzPt37SclYnqUJQ3lfO0NzK2lp1BmxxGA9ipw8xTbCCWkTUcPEbbo3tVBFNWPwCpmngqT6NG_pEmXa7OsdWvF4fXraf-NoppO_tCCralQ18bgsoLZucFIZ59lDIg_xXqbehGJWehyAapkwrWEPuEJHFuYEw60hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاصم منیر که امروز نیومد تهران (العربیه گفت سفرش رو یهویی لغو کرده) نکنه تو این مدتی که نبودم توافق شده من هنوز داغم نمی‌فهمم؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/funhiphop/75555" target="_blank">📅 16:00 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75554">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGa4WW7NB0g3uwu7OvH0wk135kLB6e_GZt5n2HFCzJ1JwnQQZU9F-tbpdCOWB4J9qCF_wCedpwbVYr4Vq-jQ0fV4bztoh5i0x274yU0wbvPLjzuh_ATywLrEta9jue6kYtRED5FwuIPq0Q2TXcWFVmVV5Ths9K07b-JfYi3Og3_EtAPeUOvEXSILKaIN7CW-iCW4NCpHNnUHvegovaO9xeUb14rMz2dEB1D6XCPi3vL3iLxfrJsXkxZo0-u2ehTG6wQ7g7qhXr4n8gIJv2RArVi9JavkZQ5AKlU96h40Dkd4swaHTCZLP7yo5-NVvr6kNq2fcgBoFxCwy-MPQizWoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصکشا یا کلا برید یا برنامه کیریتونو درست ادامه بدید، ماهی یبار خداحافظی میکنید، ابی هم انقدر خداحافظی نکرد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/funhiphop/75554" target="_blank">📅 15:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75553">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">والا من هرچی لیست تیم ملی انگلیسو نگا میکنم تیم خوبیو جمع کرده، این بازیکنایی که دعوت نکرده فقط اسم داشتن وگرنه بازیکنایی که جاشون دعوت شدن سال بهتری داشتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/funhiphop/75553" target="_blank">📅 15:29 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75552">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j85f2X8HRs26U_eDec--3mmSnHb7jTy2CNZu0MKD__uqGqNZDM0Q169Y_nPhn6WiLqya1lR8KUqMluoOafm3FO_a4vW2-tSzXQDkEyzEDZGkWKl0ZRwspu4HcWMKYMkIqqnWp61_MDuZ5aytod1wm-OmMJnIUpJLdc_yxAE2Of6Qy0966jDKSme86JZX-PxClt8OUVZ99cD2AYBt9C5kkIxIee8jwbjLG_-y69GCE23Q9fwKSzh13AdaHCB7HVb_mhyPzoGmOkLn0n-CvtAx1I05jRLmEK6yHaxarkVvliu2EXcyuwIBtZeMprDK0FfG4lOzceD9D6ktGPQsxJHQ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیمای ملی:
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/funhiphop/75552" target="_blank">📅 15:12 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75551">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">آمریکا دید استقلال داره قهرمان لیگ میشه برا همین حمله کرد که باز حق به حقدار نرسه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/funhiphop/75551" target="_blank">📅 15:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75550">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">میدونم بکیرتونه ولی با اعلام سازمان لیگ، لیگ برتر ایران نیمه تموم و بدون قهرمان به پایان رسید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/funhiphop/75550" target="_blank">📅 14:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75549">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">آتش بس ۴۵ روزه امروز رسماً تموم میشه  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/funhiphop/75549" target="_blank">📅 14:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75548">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آتش بس ۴۵ روزه امروز رسماً تموم میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/funhiphop/75548" target="_blank">📅 14:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75547">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">العربیه: پاکستان روی میانجی گری چین حساب باز کرده که دیل آمریکا ایران و با کمکش ببنده شاید این چند روزی شهباز شریف بره چین یه صحبتایی با همتای چینی خودش داشته باشه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/funhiphop/75547" target="_blank">📅 13:44 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75546">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">من نمی‌دونم ولی فان هیپ هاپو پین کنید تو تلگرامتون
بگیرنتون به کار میاد
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/funhiphop/75546" target="_blank">📅 13:37 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75545">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">الشرق : ایران تقاضای هزاران تن پرکلرات آمونیوم، اکسید کننده ای برای سوخت جامد موشک و برای بازسازی توان موشکی خودش از چین داشته و با این محموله میشه 800 تا موشک ساخت.  یه شرکت ایرانی برای واردات این مواد به یه شرکت مستقر تو هنگ کنگ درخواست داده.  @FunHipHop…</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/funhiphop/75545" target="_blank">📅 13:17 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75543">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">الشرق : ایران تقاضای هزاران تن پرکلرات آمونیوم، اکسید کننده ای برای سوخت جامد موشک و برای بازسازی توان موشکی خودش از چین داشته و با این محموله میشه 800 تا موشک ساخت.
یه شرکت ایرانی برای واردات این مواد به یه شرکت مستقر تو هنگ کنگ درخواست داده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/funhiphop/75543" target="_blank">📅 12:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75542">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">هروقتم خواستید اعتراضی کنید
یادتون باشه مردم سال ۵۷ اینترنت 4G و 5G هم نداشتن
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/funhiphop/75542" target="_blank">📅 11:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75541">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بعد کصخلا
اینترنت تو ایران هیچوقت باز نبوده
صرفا قیمت وپن پایین بوده، همین</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/funhiphop/75541" target="_blank">📅 11:17 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75540">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">چی شد اصن یهو انقد قیمت کانفیگ اومد پایین؟</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/funhiphop/75540" target="_blank">📅 11:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75538">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1rl4c_qht4fTamQua4wlPikoa_fbB23mDeShXsvc5lT0V-ZJ9fRNs4oo0QfLJRSuhuv9jKvFQPkBoR9HWydBWiacK8CeDmlyr8UCyFtCvFpNVODXfCwoejzQW7BOdi-HTqXbKCHbW56RSIoAhglsynbd2xT8GOAtcXCz_-cPUKlI67LT2v5PDHXhnpARuD_Anpzflv8l-mM4na7ExFMrYwhPYhInqcAoKhqXZ18Z6a4d4w3YzD15aLnnTfuUrALVQWfO_2CCggVncrTvUZhQHkWe9Kgp5_qLv1s5d5Hiq2asllJQbgMHaHM2SIqHGx8ELyRzIHlfq-7pgw_iAfpPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتبلاکس : اینترنت تو 84امین روز خاموشی خودش به سر میبره و 1992 ساعت از قطعی اینترنت در ایران میگذره.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/funhiphop/75538" target="_blank">📅 11:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75537">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">رویترز : نگرانی هایی از بابت اتمام صبر دونالد ترامپ وجود دارد. اما میانجی گری پاکستان سعی دارد سرعت انتقال پیام را بین دو طرف افزایش دهد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/funhiphop/75537" target="_blank">📅 11:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75536">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">جروزالم پست:
مقامات اطلاعاتی اسرائیل هشدار دادند که ایران ممکن است در حال برنامه‌ریزی برای حمله موشکی و پهپادی غافلگیرکننده علیه اسرائیل و کشورهای خلیج فارس باشد
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/funhiphop/75536" target="_blank">📅 10:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75535">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">این عرزشیاهم دنیایی دارنا
مثلاً علی تو چنل رپی که مال یکی دیگه‌ست داره تیکه میندازه به کسی که نرخ اوتباند تأیین می‌کنه تو تلگرام
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/funhiphop/75535" target="_blank">📅 10:37 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75534">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">حرف از شرافت شد
کونتون بدجور از بازار داره میسوزه که خب منم میدونم چرا
یارویی که با ضریب 5X و 10X سرویس ارائه بده مطمئنا هم قیمتش اینه پس دلت رو بهش خوش نکن که فردا تو هم به عنوان اسکمر میری بغل اون چون زیادی داری واسش میمالی
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/funhiphop/75534" target="_blank">📅 10:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75533">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">از رضا پیشرو قشنگ تر خوند</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/funhiphop/75533" target="_blank">📅 04:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75532">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBorna</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a1232073f2.mp4?token=szmuo94zlosOh6J98fQcJumeZURaTiNj4mD72y2tWz4wETjhT_8OOhDhUj7QP2h5LyguYsyP60A6mhRMotC9GHXkc_6B8RpWQx6Gw7JHzPVoSkp3kmT0WPmrAMgCAnRp8ktQUJ3xD3ifvWILr6IHS_RLlRS9aQ1g0eypAgTYnFb7NPwRjHbCgxSErSUviFPLDalQKwesBEnSpXWc4iabrD1GNtkxISKftfzxtIO622FXL5QqiDmqz1k5XGn6Mz7qSFb4ZlbuOWkEP4eXWwjqtOk571sylUxFnXD1QlN1a9tFDwSbQ_fMnownmhnIaVN9Z9IVckZd24MJF3B_oSwZHg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a1232073f2.mp4?token=szmuo94zlosOh6J98fQcJumeZURaTiNj4mD72y2tWz4wETjhT_8OOhDhUj7QP2h5LyguYsyP60A6mhRMotC9GHXkc_6B8RpWQx6Gw7JHzPVoSkp3kmT0WPmrAMgCAnRp8ktQUJ3xD3ifvWILr6IHS_RLlRS9aQ1g0eypAgTYnFb7NPwRjHbCgxSErSUviFPLDalQKwesBEnSpXWc4iabrD1GNtkxISKftfzxtIO622FXL5QqiDmqz1k5XGn6Mz7qSFb4ZlbuOWkEP4eXWwjqtOk571sylUxFnXD1QlN1a9tFDwSbQ_fMnownmhnIaVN9Z9IVckZd24MJF3B_oSwZHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/funhiphop/75532" target="_blank">📅 04:42 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75531">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🤐
نادرشاه تو قرن ۱۸ یکی از ترسناک‌ترین فرمانده‌های نظامی دنیا حساب می‌شد
تا حدی که بعضی تاریخ‌نگارهای اروپایی بهش لقب:
ناپلئونِ شرق دادن.
🤨
چند دلیلش :
امپراتوری عثمانی ازش شکست خورد.
روس‌ها عقب‌نشینی کردن.
هند رو فتح کرد و دهلی رو گرفت.
ارتشش سرعت و خشونت عجیبی داشت.
تقریباً بیشتر جنگ‌هاشو برد.
بعد از فتح دهلی، اسم نادرشاه تو کل آسیا و اروپا پیچید چون تونست ثروتمندترین شهر اون زمان رو ظرف مدت کوتاهی تسخیر کنه.
😮
حتی بعضی کشورها فقط با شنیدن نزدیک شدن سپاهش، دنبال مذاکره می‌رفتن نه جنگ.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/funhiphop/75531" target="_blank">📅 03:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75530">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">😵‍💫
رسوایی جنسی در بانک جی پی مورگان آمریکا
این ماجرا از اونجا شروع میشه که یه کارمند سابق
مرد از یک کارمند زن به دلیل سو استفاده و فشار کاری
شکایت کرده.
😂
😂
🤡
مرده اومده گفته این خانم منو میبرد پارتی بعد پارتی بهم مواد میداد و بعد مواد هم میگفت باید با هم سکس کنیم
و زنه یارو رو خفت کرده بوده و هرکاری میخواسته باهاش میکرده.
بانک هم گفته برا اینکه نه سیخ بسوزه نه کباب ما میایم
یک میلیون دلار
میدیم بهت آقایی که مورد تعرض قرار گرفتی برو خونتون
دیگه شکایت نکن
.
🔥
😡
وکیل شاکی انگاری گفته وارد نیست ما میخوایم
به شکایتمون ادامه بدیم
و وارد جزییات بشیم و این موضوع تو
آمریکا
قابل پذیرش
نیست
.
یه آبرو ریزی درست حسابی که میتونه امنیت سرمایه انسانی بزرگترین بانک آمریکارو مورد تراز و سنچش قرار بده.
👍
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/funhiphop/75530" target="_blank">📅 02:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75529">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">الجزیره
یک حمله هوایی اسرائیل مرکز آمبولانس در حنویه، جنوب لبنان را هدف قرار داد و چهار نفر را کشت، گزارش الجزیره.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/funhiphop/75529" target="_blank">📅 02:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75527">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_WdqfxJpqnIJERvPchDDZm0FFxBhD3zOQQCDU6iuN0ZU2Ys1ICACIfajTE2kKTD2YpdEOBQkCvlAxgrE9ajquY-QN2OsogpjLTA0dMmk2y3UtQ96R7LnBzAfgkwVEvzMkPYFW9VPswPHib4ounFPcaGR6Ry-yeli-45UZ4fImU0MDCCqNTf2HyovKteuZ4oAnmMDrulCGNKxRKfDQf1HPVFp85v44juN0blow72s48KemlA-3uxaAHq9egpWn3Cmj58eXUaX75c5dXGXHq9F6Pf41w6wFadMA6NKE30gUrzruKRt72Lqps96Wsvjeg-jRY7d3Dk_eq-8uR_bXz3GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادرقحبه دوسال شد، ولی تو هنوز نیومدی توضیح بدی
بیا پول مردمو بده کصکش</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/funhiphop/75527" target="_blank">📅 02:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75526">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">۲ گیگ حجم مصرف می‌کنید اگه فدایی آلبوم بده؟  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/funhiphop/75526" target="_blank">📅 02:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75525">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">۲ گیگ حجم مصرف می‌کنید اگه فدایی آلبوم بده؟
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/funhiphop/75525" target="_blank">📅 01:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75521">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ریدم رضا پیشرو ترک داده</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/funhiphop/75521" target="_blank">📅 01:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75520">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghPgP5-A-d8wYjmPx_pXyuHVnqGf1WtqDspAaM1mXi4Tj1YJXvV-jJOf5dGdsJviT3Pg4OxMxozkTwMgWqD_CTZ_xKSUtwAXWB1QGzxCZ4UYH5a-qP2WKHZHCT1cYEUZ87K7bpcQeBd-miZUei95plBqYk8Cl0aq2uVwdITGFHQ05Hz5ayHBWM7BetIiGNA3MJqIpbTaHQKE5F8CAYxgcna6krCen7AAnRjlRPp-dr4oREVxz7UeJK4plFUK7oO7_Ld-4IEBzieyTxEEui2yl5kGKzZD8a1da8FkYXpj2e13Rr7dDFSIGYNXd-t_KyQ9eU6XJOPij5ro938ev40TKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرینلندی‌ها در نوک با پلاکاردهایی که روی آن نوشته شده بود «بله به ناتو، نه به پدوفیلیا» دیده شدند.
👿
یکی از این پلاکاردها توسط یک معترض در بیرون کنسولگری جدید آمریکا رها شده بود
. (عکسی که مشاهده میکنید)
-
لینک
مجله اکونومیست و جنجال های 2026
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/funhiphop/75520" target="_blank">📅 00:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75519">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">امروز سالگرد درگذشت اسطوره بی بدیل فوتبال ایران، ناصر حجازی هست
شخصی که نبودش بیشتر از هر زمان دیگه ای حس میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/funhiphop/75519" target="_blank">📅 00:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75518">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">باز خداروشکر ایران اینترنشنال هست، دو دقیقه میبینم قیمت کل محصولات بهداشتی و غذایی میاد دستم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/funhiphop/75518" target="_blank">📅 00:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75517">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">عاصم منیر که امروز نیومد تهران (العربیه گفت سفرش رو یهویی لغو کرده) نکنه تو این مدتی که نبودم توافق شده من هنوز داغم نمی‌فهمم؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/funhiphop/75517" target="_blank">📅 23:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75515">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">النصر قهرمان لیگ عربستان شد.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/funhiphop/75515" target="_blank">📅 23:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75514">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">العریبه به نقل از منابع به‌شدت معتبر:
عاصم منیر، فرمانده ارتش پاکستان احتمالا فردا به ایران سفر خواهد کرد.
اگر عاصم منیر به ایران سفر نکند به این معنی خواهد بود که متن نهایی توافق ظرف چند ساعت دیگر اعلام خواهد شد.</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/funhiphop/75514" target="_blank">📅 23:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75512">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">البته بیشتر شبیه گل عالیشاه به استقلال بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/funhiphop/75512" target="_blank">📅 23:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75511">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">این گل رونالدو منو یاد گل کروس به سوئد انداخت
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/funhiphop/75511" target="_blank">📅 22:59 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75510">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رونالدوی مادرقهبه برو دیگه</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/funhiphop/75510" target="_blank">📅 22:56 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75509">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">جان جدتون یه کانفیگی یه راهی یه کصشری چیزی برای دوتا۲ استیم پیدا کنید هرچی میزنم پینگش بالاس
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/funhiphop/75509" target="_blank">📅 22:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75508">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">از فصل بعد تو لالیگا به هوش مصنوعی قراره نقش تو داوری بازیا بدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/funhiphop/75508" target="_blank">📅 22:41 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75505">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzTe_wpfW8Jkpa5LeqG3TENfq1uoQs1i7V445aT6nyCo8Xw4g_sYtwl-igesoOIaFD_mMeW2CrlbWl-7jb5NVX37sNGLrSQIf4hEZOWQZO9FGw__Afg8D5RS537haQ46QX1aE8IyznSF-aaLOm1qyDdqkNeBYnVfdziL4qHabU0pL5NooZABPA8Ksvc-qXZijfYoyOCGPScLekBhfekeJb1wH4bE-jejnHIJFuV29fQFrgq8rcP8UDl20YPmH3Yk61R3hac0RG-mVhdsUpkW9hP3r9niSX2TwXcfgDTLQuVkT7u6nWu1-qG8geKC5IWiP4t2C0d0RV3rdLbRzPB9qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایی دیگه کیر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/funhiphop/75505" target="_blank">📅 22:05 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75501">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دبی با 49 ثانیه قطعی برق در طول یک سال،کمترین میزان قطعی برق در سطح جهان رو ثبت کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/funhiphop/75501" target="_blank">📅 21:35 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75500">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">آقایون وسط باز یکم جو خوابید باز شروع کردن به گله از گرونی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/funhiphop/75500" target="_blank">📅 21:05 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75498">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb792999a1.mp4?token=LWUKyNTKo0SsYbectG8ofajCXrj3K9pmtvMiBfrRLI8d4PFgQcKR8JUOpFudcAfdOdb86II4Q-zDuNwcrGTlaZuKmjwu1ZRz93ZaICbQ5_mpzafD4h7zSHzJfmh4mPBempFXJ7g482mXJg-2zXftGGWOnRoCA9iC0CZMDVebuMM24Qtu3j1WObPJsIx96k1l4yOD2uHq-lm2yJMhtalV6CQRWB53wGdduBWnZq0inktZ1kAU5I6etC0qs71DG-7x8Kaa96i8M0emurva2MTHVjOnokjwXLnb7v3sX_KrDwESIAP5feChbRrbcX5ogdyDBGWea46Y8YjVLWk6GeMUPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb792999a1.mp4?token=LWUKyNTKo0SsYbectG8ofajCXrj3K9pmtvMiBfrRLI8d4PFgQcKR8JUOpFudcAfdOdb86II4Q-zDuNwcrGTlaZuKmjwu1ZRz93ZaICbQ5_mpzafD4h7zSHzJfmh4mPBempFXJ7g482mXJg-2zXftGGWOnRoCA9iC0CZMDVebuMM24Qtu3j1WObPJsIx96k1l4yOD2uHq-lm2yJMhtalV6CQRWB53wGdduBWnZq0inktZ1kAU5I6etC0qs71DG-7x8Kaa96i8M0emurva2MTHVjOnokjwXLnb7v3sX_KrDwESIAP5feChbRrbcX5ogdyDBGWea46Y8YjVLWk6GeMUPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/funhiphop/75498" target="_blank">📅 20:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75497">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ای کیروم به ننت ترامپ خستم کردی</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/funhiphop/75497" target="_blank">📅 20:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75495">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">😠
کله زرد بنگاهی
ما نمیخوایم تنگه هرمز عوارضی بشه
کنترل تنگه هرمز (محاصره) کامل در اختیار داریم
نود و هشت درصد توان موشکی ایران و از بین بردیم
ایران نمیتونه اورانیوم غنای بالا رو نگه داره و اگه بهش دست پیدا کنیم احتمالا همشو نابود میکنیم و ما این اورانیومارو نمیخوایم
درگیری با ایران به زوری به پایان خواهد رسید
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/funhiphop/75495" target="_blank">📅 20:05 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75494">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McZf2J2kltfzIxkZawZwNL6o60Cl27VBLiwss5O70jiN6GCD9rOOG6Nr-YiMJzstHO-X8eEmpQlhjImiWEcfERzv_p_gaT-ZOANnX0qH5gb9KLc9EmGNDSJYBhyunVwpdLV5-sFtzHaEIjeOY0yV4xnm1Fs29KZJ2Mm7u-9Abcq_8dNZD6gAAS3pJvIrLBW6Q-hzjtXpyH85ROlHpbbYmE4iyDed1RDscYHqv3mpgeGr28DTgjkhKURtFOwWcXTlbsYN7a-NLRmSq5Xt6jwSJkK2BAAy1y51M9XdZ-B-UJSAyWT57PYxhqh62ELulHasCdbENcU8nPBvXVhDphy1iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔜
فایننشال جوس
مارکو روبیو، وزیر خارجه آمریکا، گفته اگر در تنگه هرمز سیستم دریافت عوارض برای عبور کشتی‌ها اجرا شود، رسیدن به توافق دیپلماتیک
تقریباً
غیرممکن خواهد شد.
😶‍🌫️
این حرف بعد از خبری مطرح شد که گفته بود
ایران و عمان
درباره
دائمی
شدن
عوارض
عبور از
تنگه
هرمز
در حال
مذاکره
هستند.
👻
یعنی آمریکا این اقدام را
تنش‌زا
می‌داند و معتقد است می‌تواند مذاکرات سیاسی و توافقات منطقه‌ای را سخت‌تر کند.
👍
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/funhiphop/75494" target="_blank">📅 19:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75493">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">امشب النصر قهرمان میشه؟
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/funhiphop/75493" target="_blank">📅 18:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75492">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دلم میسوزه برات ناموسا، کاش میشد یکم عقل تو کلت کاشت.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/funhiphop/75492" target="_blank">📅 18:10 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75491">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pl8qSxOCJGPCA9vgSaQckooRQwycG5vk-Eg6eU0E_PvgxnUT6IaED19W8ODxl_8voPlnFr6xQlc20MBpMV5u-otS5Im50ptaR1qAIdS7PEpONADnuA9NEmEJQs2Sg2k3sAwN7NxdTytON3JgoaYV7nP0r0ByHtptF4_yvS56JlfOnE-gNiKm_OdSAlat-3KOOTfvnTqkSvVgXh-_ensby_qsDg4SB9I33d-Gf56DChlVuwqHILZ0DYKy1gjGmISa6H1GzXnuKxDNEp5D9KkevwhjBdC1WQp4U120KKCIQbQTWeVoHRyFuFdLdL5kVUeLgMY_i8R1pdkXe2Jt6OtVvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلم میسوزه برات ناموسا، کاش میشد یکم عقل تو کلت کاشت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/funhiphop/75491" target="_blank">📅 18:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75488">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">فاکس نیوز
طبق نظر سنجی 60 درصد آمریکایی ها با اقدام نظامی علیه تهران مخالف هستند.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/funhiphop/75488" target="_blank">📅 17:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75486">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oH7GBT7a9yj87FH1vcK3jaXxvmGXZJIBNMiddJBEqP7_Yan9hZEmRfF_JQ9iEVESElQDZqfidkgYd6kShYg-P2D7pDkdhTnEATQP0ZfCPPjGQoPOSRPeuE6rUcDO2EikZTSEYtxLBgquJADQomUYP6Svej7-Fc0HX4ogzFVv4Xj2l0ZaVzrjNzCL5OYvEOuPC5OqFY3XUZgVB2n2P5QFk2xa2VuO-YlFTT0GV7M7JG6sMn2qgwUh5kJPQZ6m1fbIGMn8KR3n74SELBgl4dBAcnxjui5em17Aw9lURADgee_TbO4l1oYMrFTLD1pgNzoilpWRAf9LnjSsxEEv4lmI6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MZhYwFuvuayK3JFB4SENuR0OAQOnBXsyLVz6ozzDGU48nGXbyuqz_NQqjC3hezXGhvT6-5iauft2E8sTwpEMm6Ms6DXjpunTmL8j6J9O63zAf318aBHGG0U-UHgkYHOMrVUHhUFzqOZksvaLv3HU96xRIiHMGA3oM9_QyuXevz2uItM81e-h7Uhhj3UKgyzbKGSJPzP7re_0SZ5vt4zyELi8NHZvVUob2vnd4ItihLP0inbuNRivd7iM7PgC-8L6XImCgXVXbN-RvE3sUbaB5frwjdHvtYN3ZrlvekVz4vK-pjofs2uFKbbnPUdJs0piHv10kwC4cYcq5lXzvVsiKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همون همیشگی دوستان اشتباه شد دارن میزنن هنوز  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/funhiphop/75486" target="_blank">📅 16:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75485">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">هیچوقت نفهمیدم چرا رپرا وقتی تو ایران میمونن کم کم بنجل و گنده گوز میشن
وقتی از ایران میرن کم کم دچار زوال عقل و بحران هویت میشن
چرا بالانسو رعایت نمیکنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/funhiphop/75485" target="_blank">📅 16:21 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75484">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ:
ما داریم با آدمای خوبی در ایران مذاکره میکنیم/مذاکرات داره خوب پیش میره/اونا با عقل شدن
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/funhiphop/75484" target="_blank">📅 15:08 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75483">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">حالا ترامپ کصکش باز میاد میگه مذاکرات مثبت بوده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/funhiphop/75483" target="_blank">📅 14:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75482">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">رویترز:
مجتبی خامنه ای دستور داده که اورانیوم غنی شده در ایران بماند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/funhiphop/75482" target="_blank">📅 14:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75481">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">به پیر به پیغمبر من خشخاش نکاشتم، دست از سرم بردارید
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/funhiphop/75481" target="_blank">📅 12:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75480">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_-7ReAWjbgVJ0zV54xGnFmws1rRrzM4ExbaizSxJ07Jj4IHyr8qanzZu9YXRy2QQBYL6L4WPGv3NPLq8btLEi_hO0gsv0TZjmy8wLzvVrLdhJO8zvtsze5ZY-ro3Cn7jAjftlgC89NIfmvWIgDpeBvZHB4GQ32DbXAONYKl4bpeyrSviNc9vvMG_91D64YIeQDS0WZDRNCDjru8BbeD48VlxldlHfzSePjq41Gbp4afY1pSJkKlw8y1cDFMJ7wM4KYmUiqmBprpDkIhqyQz_XizOP269-6ZEyTlmQXCkBEiBHftFkguA6PppMxznJjFoJkY0mQCSyo6FmWUZ1gxng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید سردار آزمون
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/funhiphop/75480" target="_blank">📅 12:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75479">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ویناک رپر سیاسی شد رفت
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/funhiphop/75479" target="_blank">📅 12:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75478">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">حواستون به قحطی نون هست که خیلی چراغ خاموش داره میره تو کونمون؟</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/funhiphop/75478" target="_blank">📅 11:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75477">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">واقعا چطوری ملت میتونن طرفدار پهلوی باشن من  الان داشتم با بابا بزرگم حرف میزدم میگفت اونزمان ملت حتی نمیتونستن یه جومونگ ساده ببینن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/funhiphop/75477" target="_blank">📅 10:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75476">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec7c8d7ea8.mp4?token=UO40aS9X1w8LxqYe83e5f9iv_vDBZyKC4KD-duy65cvfTQsGY9Ur8xuD63Fo6YYkJHdExxkERIbOE2oZl-znTrFTjbOT6VEqmGwPrbhKvW2LOtRypoSMJNSh3y8t3PJoFeDN9kJjIlP872WO9N6eZUKXXkoIaPiM0StBedqSlOGwOvvaWqMNwwvzOhCbIh5a37GH3W4BUYPwc79rk7gxzXacWndzwrOlraeqyttWp4g7f2hB990Sjm73lrF8mbHNVGjd28oDcwHyR-gLyQ8kbjcy_Bteolb4mzPIEt9GxgkL8EQ953tUavliT5AP0XnpogpuzKrFIwELlLD8q-Iz0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec7c8d7ea8.mp4?token=UO40aS9X1w8LxqYe83e5f9iv_vDBZyKC4KD-duy65cvfTQsGY9Ur8xuD63Fo6YYkJHdExxkERIbOE2oZl-znTrFTjbOT6VEqmGwPrbhKvW2LOtRypoSMJNSh3y8t3PJoFeDN9kJjIlP872WO9N6eZUKXXkoIaPiM0StBedqSlOGwOvvaWqMNwwvzOhCbIh5a37GH3W4BUYPwc79rk7gxzXacWndzwrOlraeqyttWp4g7f2hB990Sjm73lrF8mbHNVGjd28oDcwHyR-gLyQ8kbjcy_Bteolb4mzPIEt9GxgkL8EQ953tUavliT5AP0XnpogpuzKrFIwELlLD8q-Iz0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحاتی مختصر درباره برنامه هایی که رو گوشیتون نصب میکنید
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/75476" target="_blank">📅 09:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75475">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">از اتفاقا دی حدود ۱۳۰ روز گذشته و تو این مدت بیشتر از ۹۰ روزش رو انتظار کشیدیم
ایوب هم بود روانی میشد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/funhiphop/75475" target="_blank">📅 09:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75473">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">😑
رویترز
کشتی‌های متحدان ایران مانند
روسیه
و
چین
اولویت عبور از تنگه هرمز را دارند.
😅
برخی کشتی‌ها برای عبور امن بالای ۱۵۰ هزار دلار
هزینه امنیتی
می‌پردازند.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/75473" target="_blank">📅 00:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75470">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">معاون فرمانده نیروی دریایی سپاه پاسداران انقلاب اسلامی:
دست ما روی ماشه است و
اگر ترامپ فکر می‌کند می‌تواند تنگه هرمز را با زور و کشتی‌ها باز کند، باید بداند همان نیروی دریایی که ادعا کردید نابود شده، شما را در کف دریا غرق خواهد کرد.
دشمنان ما باید بدانند که کاملاً اشتباه می‌کنند اگر فکر کنند این ملت با تخریب زیرساخت‌هایش عقب‌نشینی خواهد کرد، این ملت در طول ۴۷ سال ثابت کرده است که ممکن است تخریب شود اما تسلیم نمی‌شود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/75470" target="_blank">📅 23:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75468">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">با اینکه نداریم سیم‌کارت سفید میشناسنمون تو ایست بازرسی</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/funhiphop/75468" target="_blank">📅 23:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75467">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">خبرنگار :
پیامت به خانواده‌های آمریکایی که از هوش مصنوعی می‌ترسن چیه اونا نگرانن بچه‌هاشون تو آینده کار نداشته باشن
ترامپ :
هوش مصنوعی فوق‌العاده‌ست ایران نباید سلاح هسته‌ای داشته باشه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/funhiphop/75467" target="_blank">📅 23:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75466">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مایکل بی، کارگردان آمریکایی، درحال ساخت فیلمی بر اساس مأموریت نجات دو خلبان آمریکایی پس از سقوط جنگنده‌ی ارتش آمریکا درجریان جنگ با ایرانه؛ تمرکز این فیلم برروی عملیات گسترده‌ای که تو پشت خطوط دشمن در کوه‌های زاگرس در غرب ایران صورت گرفت، خواهد بود و بر اساس کتابی آینده از میچل زاکوف ساخته می‌شه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/funhiphop/75466" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75465">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2221a06fe7.mp4?token=pPzE0WjOqPlygj8yWXHqjoFbGPldF8FK-peK9rmCjs-ctXCfii45jySz-xcjkD1UUIPyCK0V9BJ6HUeYYd7uZfovkSVbQSsiLVttA0L7Q20cmUxBpa83L3ETzMCXpgduWMXwILoWhlDkmE93eNjoiMcaqIxq-vm2gnYhxUaNRkrC-K6qIDeZXR1BV-qDDTb-Ls-PiXe7Jxkp8tTLvl0-v6mMjQsxqDlAA65Bu750ujHiAPydK8CoT3QxOE0hrvpXz4IfF1dC6N_Ecm4ap3G7RDw4tGhWl7cC_f5cimf0GwLw7v7_ykzLWyR-qIxmvqzAXv-jLV77t2VY_ttEkU4OTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2221a06fe7.mp4?token=pPzE0WjOqPlygj8yWXHqjoFbGPldF8FK-peK9rmCjs-ctXCfii45jySz-xcjkD1UUIPyCK0V9BJ6HUeYYd7uZfovkSVbQSsiLVttA0L7Q20cmUxBpa83L3ETzMCXpgduWMXwILoWhlDkmE93eNjoiMcaqIxq-vm2gnYhxUaNRkrC-K6qIDeZXR1BV-qDDTb-Ls-PiXe7Jxkp8tTLvl0-v6mMjQsxqDlAA65Bu750ujHiAPydK8CoT3QxOE0hrvpXz4IfF1dC6N_Ecm4ap3G7RDw4tGhWl7cC_f5cimf0GwLw7v7_ykzLWyR-qIxmvqzAXv-jLV77t2VY_ttEkU4OTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
اگر پاسخ‌های درست را دریافت نکنیم، اوضاع خیلی سریع پیش می‌رود. همه ما آماده‌ایم. باید پاسخ‌های درست را بگیریم.
باید پاسخ‌های ایران کاملاً ۱۰۰٪ درست باشند، و اگر اینطور شود، زمان، انرژی و جان‌های زیادی را نجات می‌دهیم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/funhiphop/75465" target="_blank">📅 22:36 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75464">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace87a5520.mp4?token=Cwm9hQMMNRRuvUwGk71y9_IaRHBASfLwbE0sAsz-VnqSB_BmtkJ6v46YxEKy8lcg4QIvH2KgttBp5XpN_Ge1qhjjxxpg8lzaSMhytPcZKO6WyPbaggArUmcYZzp9dGfgoMrbHY7NHMNCXy7a2s9BIYGAmo-LnbMPgyjCXuI-PekvgFANVGT8uH5A1RLl3EwDaXj7XmF39MkWLmNhrmPFdqvny8RkgMp0TUrHMnmzV4877nM-VxSJDwA62DT3rS4473h5zyEWFPm8PivQpg7FZ1FtKoerYOIY91mrvOdL2T2G5_z4xPigVO8WAKi7J1Ey1NncB_8DdmWXjd2wRnknQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace87a5520.mp4?token=Cwm9hQMMNRRuvUwGk71y9_IaRHBASfLwbE0sAsz-VnqSB_BmtkJ6v46YxEKy8lcg4QIvH2KgttBp5XpN_Ge1qhjjxxpg8lzaSMhytPcZKO6WyPbaggArUmcYZzp9dGfgoMrbHY7NHMNCXy7a2s9BIYGAmo-LnbMPgyjCXuI-PekvgFANVGT8uH5A1RLl3EwDaXj7XmF39MkWLmNhrmPFdqvny8RkgMp0TUrHMnmzV4877nM-VxSJDwA62DT3rS4473h5zyEWFPm8PivQpg7FZ1FtKoerYOIY91mrvOdL2T2G5_z4xPigVO8WAKi7J1Ey1NncB_8DdmWXjd2wRnknQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
آیا آمریکا در جریان مذاکرات صلح، لغو تحریم‌های نفتی علیه ایران را پیشنهاد داده است، همانطور که رسانه‌های دولتی ایران گزارش داده‌اند؟
ترامپ:
نه، من چنین چیزی نشنیده‌ام. تا زمانی که آنها توافقنامه‌ای امضا نکنند، هیچ لغو تحریمی انجام نمی‌دهم.
وقتی آنها توافقنامه را امضا کنند، می‌توانیم آنجا را دوباره بسازیم و چیزی داشته باشیم که واقعاً برای مردم آن کشور خوب باشد.
اما نه، ما هیچ پیشنهادی نداده‌ایم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/funhiphop/75464" target="_blank">📅 22:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75463">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ درباره ایران: ما در واقع با برخی افراد بسیار خوبی درحال معامله هستیم. ما با افرادی با استعداد و با هوش خوب معامله می‌کنیم. ما از هوش آنها کاملاً تحت تأثیر قرار گرفته‌ایم.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/funhiphop/75463" target="_blank">📅 22:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75462">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb46c8698f.mp4?token=Lpynp9aN7S34q0aimpn8O4gTjG9i2feEess-vdyeNs7HJNvGAGnXwAwx-1zCLferDOrfBrvEyWtP6kf5IW_99vkTV3LkUiaiN8OQzMJPjIeYF2eHhvZJ4ED2B_Izk-9cNOIBZUBejh1ySAoQOsknH9laBejKyrfWfMRw2C0nFixRsSzI0BvPRxaBdFoFugqw1e1aZwYhYRWrWenrAFrlsBymVclcU8L0NX6Cw3Zn79UqGY27wbRq2NfjmJgZsYer6Uv7qOxhCUfNcbgVA13YPaLk-M0J9oc93CWt84gkwfeVc-Jp0iheycXaERmXsN1_Qkth_6tSfaW1WKQ4DBeoyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb46c8698f.mp4?token=Lpynp9aN7S34q0aimpn8O4gTjG9i2feEess-vdyeNs7HJNvGAGnXwAwx-1zCLferDOrfBrvEyWtP6kf5IW_99vkTV3LkUiaiN8OQzMJPjIeYF2eHhvZJ4ED2B_Izk-9cNOIBZUBejh1ySAoQOsknH9laBejKyrfWfMRw2C0nFixRsSzI0BvPRxaBdFoFugqw1e1aZwYhYRWrWenrAFrlsBymVclcU8L0NX6Cw3Zn79UqGY27wbRq2NfjmJgZsYer6Uv7qOxhCUfNcbgVA13YPaLk-M0J9oc93CWt84gkwfeVc-Jp0iheycXaERmXsN1_Qkth_6tSfaW1WKQ4DBeoyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
ما در واقع با برخی افراد بسیار خوبی درحال معامله هستیم.
ما با افرادی با استعداد و با هوش خوب معامله می‌کنیم.
ما از هوش آنها کاملاً تحت تأثیر قرار گرفته‌ایم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/funhiphop/75462" target="_blank">📅 22:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75461">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3kf88qrjSX7KiYoib4Wkg9lyx3J5SX68DI51kOTJ1CS7DpMyJBietY-18Bkl8Mf3UBkwZiRsMQHveGg-Hq03KaX3NDoLEEbJrX-JehtrcKwaf3ChGCJqewmR_nBSO19vuNYA07YkKqKB3OTpSdVTpFjVn-9f6QXSzGRUMnEZx9hsX9iOtqXYtLOSfo7CczzJLjPlHgq00o16pQOEYGWoGjgjvdEHZaFuJPCh5yEMJWYdkl_5SsUcI0al75ShaEGqoOv79l_98qpLx9qpwjzAaQ8Zfp924N7K4bOO0j8mLQfZRtY4b8WA6VZ4Lr1KH2GlZpCc_S0CzYVjJ3__5Uazw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من الان که فهمیدم که لارنس نورمن در واکنش به حضور مقامات پاکستانی در ایران برای پیشبرد مذاکرات گفته این جالب و قابل توجه عه و اتفاقات جالبی درحال رخ دادنه تا ته ماجرا رو رفتم جدی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/funhiphop/75461" target="_blank">📅 22:12 · 30 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

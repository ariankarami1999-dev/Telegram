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
<img src="https://cdn4.telesco.pe/file/UByV2a-t6w3YeXu1ZRlVUdIWFFjva2Thc-sFF3MjeiyhdqTe-CMg0k2OnAA0d0f7w7JF6L_f_447-LfZ7MwCkM7aL049ON4OKCnw_VtvvaaeipqCTW8HLJ6a7YFphPiNwD63wg7KOLwXrsargPEqsJ0rhkGRDM215YvYDacShNSqHnTOYl6ljTtLnhr0H4e7GAsHY7ZuBEO6O6tigv0ScqiZ3rXnoHeQqEtdCCY6rfj-tzT3a2hq5l9gMASwJpNzq8wIbPnrUU704gw3vGyPdhMgil5IHfQwEdwOVUw_4nuPJ88agp7s46tDf-ZZxvWDyOTIH0hy2WhtCYlLRsydPQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 14:44:54</div>
<hr>

<div class="tg-post" id="msg-139149">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8tNH1Wbyr5nA2C0b9sUcC37jn5rXzCkHguArlcdOWkgB8SPkRaAH1UOJEXKi82tYY5mtE05Gwl4waEaYpB3O40OfEClcpW1-a_lan6Er9oghmzyC2ILjN5i-zomieATDSHyuLHNymDSqQhyZCy-57QuWV3TFZM1-FvYYybgmYYsAdf40I8D4GLfskfMNtZMLW69Bg5lykl4ucnFsLb1_idMPoVTWWtJVPHp-Vwdg1G4aZnkzuws_-YG-qxIe_wecP4gsL1KprxBVJ3cxJsznid3biVUzCnLIOBGy9kySBGo_13NMtYNRPjBdiftPXGl4Ow8wrYffYQtmk1fc4_yMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پایتخت آماده یک شب داغ!
🔥
پرسپولیس دنبال شکار ملوان؛ قویِ انزلی برای غافلگیری به‌میدان میاد!
امشب نوبت کدوم تیمه که حرف آخر رو بزنه؟
[
پرسپولیس
⚽
🆚
⚽
ملوان
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 977 · <a href="https://t.me/SorkhTimes/139149" target="_blank">📅 14:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139148">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dJkmMg07xqm-DfotVNW7w_Q098-fUd6_zvTYLFpuoIKlsIFn6tQscNpOZjAN7AUc5IqMMrMA5NIs1XDiIwWC9g7w131mZZNOsnS11lr56TWPWseEdnenX9dUVy3zWRMqhlxQykhSNcrDtokSwqi0VrXc7EIB5ho8wBIWlO-noxQPso2Yon2o_gTjSWpZzvVXPBzfIfoNGhJOZ3MmbMVZN-S1TWG8Fw2XytXuBOmMFutMZbUnZrZS4KcXt3yfqaeib4fH7oVvLJaL1MxxXg80h-2OrbLeWRyoLtfqZxcpvR1ZHNnfoK9QFs3IeKrmVZ-bmIlfKqNRv9B23F6BzjKLAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
🔻
رضاییان در توجیه رفتنش به استقلال میگفت هواداران استقلال جنتلمن و با فرهنگ هستند اما دیروز هرچی فحش توهین بود بارش کردند وسط بازی هم کلی بطری سنگ و ... سمتش پرتاپ شد !
🔻
🔻
بله آقای رضاییان اینا همون هواداران جنتلمن و بزرگ استقلال هستند که به مادربزرگ مرحوم جلالی هم رحم نکردن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SorkhTimes/139148" target="_blank">📅 13:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139147">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✔️
✔️
✔️
حجت کریمی مدیرعامل تراکتورسازی: چون دلار شده ۲۰۰ هزار تومان کسی نباید در مورد بیرانوند صحبت کنه. مردم به فکر مشکلات اقتصادی باشند نه بیرانوند
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/SorkhTimes/139147" target="_blank">📅 13:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139146">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✔️
✔️
✔️
دنیل گرا مصدومیتش برطرف شده اما تارتار بهش اجازه شرکت در تمرینات رو نمی‌ده و باشگاه هم گرا رو نمی‌خواد ولی تا پایان قراردادش در پرسپولیس میمونه/ فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SorkhTimes/139146" target="_blank">📅 13:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139145">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ghypa6cncYggC53U_K07RqRFUmZd62aUnhcubYNOXkOB4IAoWN-XLYHY9Rwl5MexmsNQ3DIoyx_CXzil3MJTD9Ab_zkWk4CV8Ey1bWNxySELJPXl3K_yv6UvzdANts-M-XAsqcZ-bPnOtB7BtW_mJzjJshN_3KrZI1Pq_UpPV4EJfIzNs3Lfa02EEojlof6EUHcVSltCPtD_bzj_X1LYmUy242jsuJ43pA-aNaLFHNB2HRpcZdZR9_pzsBPb8PELW66f5ju-AMFU1FV5TpKjakYMg8sRWQpJoS-emuaQv-PR79w_WegLHGqTg13Y7jaPbD1-Rs3BAd9wRcPNnikpmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
اتفاق عجیب در لیگ عربستان؛ از هوش رفتن ۵۰ تماشاگر!
🔻
در دیدار الهلال و الخلیج بیش از ۵۰ تماشاگر به دلیل گرما و رطوبت شدید هوا بیهوش شدند.‌ بسیاری از هواداران نیز پیش از پایان نیمه اول ورزشگاه را ترک کردند. الهلال این دیدار را با نتیجه ۵-۱ به سود خود به پایان رساند.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SorkhTimes/139145" target="_blank">📅 13:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139144">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✔️
✔️
گفته میشه مدیران باشگاه گل گهر برای شکایت از باشگاه سپاهان بخاطر بازی دادن به کسری طاهری از تیم حقوقی پرسپولیس قبل از شروع مسابقه مشورت گرفتن!   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/139144" target="_blank">📅 11:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139143">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
فووووووووووری
❌
❌
یک سری شایعات پخش شده امسال بخاطر فشردگی تقویم لیگ خبری از جام حذفی نیست و قراره سهیمه آسیایی جام حذفی به چادرملو داده بشه
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/139143" target="_blank">📅 09:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139142">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🌬
پایان بازی  نساجی
0⃣
-
2⃣
شمس آذر
🔴
👔
اولین حیا کن، رها کن فصل در قائمشهر؛ روزهای سخت در انتظار مجتبی حسینی!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/139142" target="_blank">📅 09:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139141">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✔️
✔️
✔️
حجت کریمی مدیرعامل تراکتورسازی: چون دلار شده ۲۰۰ هزار تومان کسی نباید در مورد بیرانوند صحبت کنه. مردم به فکر مشکلات اقتصادی باشند نه بیرانوند
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/139141" target="_blank">📅 08:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139140">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
صبحی که ی بازی سخت و حساسی  داریم بخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/139140" target="_blank">📅 08:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139139">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZ_b3DFBnQ3lRPnAhZmwf9vjVdbOL2hvrrlgqit0R56F43nfjBsxKPNR931qwjuNsGagAtZCB8zZudKlDUZXiIuzdbkN9JnY2Cm0m4jxaJPrFYaWNKLxgEuN7p3euKIoaGOIm-CyN3fGz5Mh-79KRntA8SWJFzRb4bPrCEya2bUdUrE9TwdRTT9Jk-HnkmLr1D7PObMA4tuha80CBOEfGha7qKCXm-pAK2NUKRc86dHeLzIF7FLUklR6cWuMdWtKJ04TXlhzKycXNeP9KNDHtP6jjVsazdB8zYKamyqIYxsJt1EeqSwl2oQV1XALr9tmm9c2tt_lAGsEgdBs0cvR3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ورود به اسپورت‌نود؛ ساده‌تر از همیشه!
🔗
دنبال یه راه سریع و بدون دردسر برای ورود به اسپورت‌نود هستی؟
🔵
با مینی‌اپ ربات رسمی اسپورت‌نود، مسیر دسترسی ساده و یکپارچه شده؛ بدون لینک‌های متعدد و مراحل اضافی، مستقیماً وارد محیط کاربری شو و از امکانات سایت استفاده کن.
🔗
ربات رسمی اسپورت‌نود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت‌نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/139139" target="_blank">📅 02:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139138">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/241731bcb2.mp4?token=qmPsaYKMYhZ8jDHIkHfP-AWQYqM4vBBCZnnveEWOwmjfa0XSvSqK1OGy8p4ntxZOPJ9BFG9-ZzMi3zs4bGdUwvuMv2tj7tBaaombnivPJYZ01aaJYeAoBv8zkLwq4N-2VX2FdH3bjSOvgsl6alTe6mYRtmxtDuc3PZgWhOSZaba_Bo8DGutRhqydSRydGdYyrMvpwRktC25Z16cKJxPWwKIC-ZHmvhBKrEvrWVX4OJ3wXRLO3c4qckAt-zjpPmJHLLm3E4oZwjuEse16EEplwfk3gluq-XbbO4sNzbaRKfZnb0Rl7HvsTV23xWmNFjv7pPIfeuXNM7b-YW7LAAHnQDTCkwnvS4IcAEArTRliVZCiH3z5nWjIchwLr5hmaJW6W_WyA4AXlZ3IsMEKG80hrYoleJFCgNOVzrA5tvh28ggj5tor4UrKSLEgiPqUwMZRSLwnf1vLoRucFjWY1zA3LjxkIoimjY95qGlwsP30e5QjTd-84DDsjO-L2TBa2bj98JUX8vlSlBfws6e3nvc5W3gbzmFxHcIz-i341QyI84idSqky29vqYHWGTRQ37e58KsxxvWXRwxlKHQiiH0IlvkhMUKoZ18Ust-UorHpe2zVcvor4gTqWs3DwGFQqKEWaXp6btzLUGS6jKcmS_hjehDHAWqJCfPKDKSDHevu8Mpk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/241731bcb2.mp4?token=qmPsaYKMYhZ8jDHIkHfP-AWQYqM4vBBCZnnveEWOwmjfa0XSvSqK1OGy8p4ntxZOPJ9BFG9-ZzMi3zs4bGdUwvuMv2tj7tBaaombnivPJYZ01aaJYeAoBv8zkLwq4N-2VX2FdH3bjSOvgsl6alTe6mYRtmxtDuc3PZgWhOSZaba_Bo8DGutRhqydSRydGdYyrMvpwRktC25Z16cKJxPWwKIC-ZHmvhBKrEvrWVX4OJ3wXRLO3c4qckAt-zjpPmJHLLm3E4oZwjuEse16EEplwfk3gluq-XbbO4sNzbaRKfZnb0Rl7HvsTV23xWmNFjv7pPIfeuXNM7b-YW7LAAHnQDTCkwnvS4IcAEArTRliVZCiH3z5nWjIchwLr5hmaJW6W_WyA4AXlZ3IsMEKG80hrYoleJFCgNOVzrA5tvh28ggj5tor4UrKSLEgiPqUwMZRSLwnf1vLoRucFjWY1zA3LjxkIoimjY95qGlwsP30e5QjTd-84DDsjO-L2TBa2bj98JUX8vlSlBfws6e3nvc5W3gbzmFxHcIz-i341QyI84idSqky29vqYHWGTRQ37e58KsxxvWXRwxlKHQiiH0IlvkhMUKoZ18Ust-UorHpe2zVcvor4gTqWs3DwGFQqKEWaXp6btzLUGS6jKcmS_hjehDHAWqJCfPKDKSDHevu8Mpk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#منهای_پرسپولیس
👤
فراز فاطمی سرپرست چادرملو:
❌
آقای حیدری فکر کرده ما خریم. قشنگ بگید میخواید یه تیم ببازه دیگه اینجور قضاوت کردن بخاطر چیه. امیرحسین حسین‌زاده با تکلی که زد دوبار باید اخراج میشد ولی حتی صحنه به وار
هم نرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/139138" target="_blank">📅 01:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139137">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✔️
✔️
براساس‌صحبت‌های‌مهدی‌تارتار؛ سرگیف از بازی فردا مقابل ملوان به ترکیب سرخ‌ها برمیگرده و تارتار میخواد زوج علیپور - سرگیف استفاده کنه اما اوستون اورونوف همچنان نیمکت نشین خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/139137" target="_blank">📅 00:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139136">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
❌
استقلال فولاد مساوی تموم شد.کیسه خیلی خسته و کوفته شد و واسه دربی قانونا خسته میاد تیمش امیدوارم استفاده کنیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/139136" target="_blank">📅 00:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139135">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
کشاله‌درد دوباره شجاع خلیل‌زاده در بازی امشب مقابل هواداران یزدی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139135" target="_blank">📅 00:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139134">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
کشاله‌درد دوباره شجاع خلیل‌زاده در بازی امشب مقابل هواداران یزدی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139134" target="_blank">📅 00:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139133">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32fe7cb793.mp4?token=nX66md2mEsmMa0jgqaT4Hnvrv8fsOUNr8fP8Q6-4HDVJmCrG22bVdT-DvFpuZcLmkuFTgAUF-VKLACIBTGjRu9VIqsp69yby5PankxYxTH6fghEWGdQqmEUn99RoBXdQXJeuMOFG2bu51AvjvrJq2KpTmJszmQCkDQcZ0EMF9qyixFZSE5VUEddEcPZqSlSAKXxzzDcB6tlQmUQYFgEL4yb_tDgUrdlSzJBdf48T3GRv7Ggi8NMTKlQA4VtySNjULSTHwmY2qYB8usmwlu5vYozrMMEe5j6zvvixN98OzxGHBhcg3WrNtRcPkn-QFS6nsnV0XgS4PSvCxzMIyueWPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32fe7cb793.mp4?token=nX66md2mEsmMa0jgqaT4Hnvrv8fsOUNr8fP8Q6-4HDVJmCrG22bVdT-DvFpuZcLmkuFTgAUF-VKLACIBTGjRu9VIqsp69yby5PankxYxTH6fghEWGdQqmEUn99RoBXdQXJeuMOFG2bu51AvjvrJq2KpTmJszmQCkDQcZ0EMF9qyixFZSE5VUEddEcPZqSlSAKXxzzDcB6tlQmUQYFgEL4yb_tDgUrdlSzJBdf48T3GRv7Ggi8NMTKlQA4VtySNjULSTHwmY2qYB8usmwlu5vYozrMMEe5j6zvvixN98OzxGHBhcg3WrNtRcPkn-QFS6nsnV0XgS4PSvCxzMIyueWPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
کشاله‌درد دوباره شجاع خلیل‌زاده در بازی امشب مقابل هواداران
یزدی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139133" target="_blank">📅 00:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139132">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/867c2d8104.mp4?token=YT2W3kdDVbTARlzJdUMoEv0H27F7Tdz2vpPtmLiz_uIXzHsnuhMLD4HWvOeSldWIi7oWAd9eihYvyJ8fmoaqEwEYh73jT45dvDWmG23Exd65jlKMCEPJRPwB_xiYdpu_iN4CGkv3iOrFySM7ZwqMkyu6-r6w8GI9wj5IQEAAjDzuI-nmcSP88Cx9xGOxLK1lxQOUb4My1DCqYWkmzbty1rF177I0wBx2QRKQwT31t0J6OKeitH7ihScLrnggeuYNP0tWhg3rnSeTi0h7gNfYdL8Da5yhMKK2Jlacb7-paxs4w5z_ig_C9vwxCxFqzyXB3cUlM2FdCURfceq94BttIUiNeiiN-6zl4Hy77fcVv5tud0L4YVXHKm6aVFAsFbsYmUTlu30_ZgJh-kZ5zD87ouLGg4mXO6QItjGvBrURn5kDRiL7K28vX7uS-A4b2bahnqJ6bqqHoQGaV9oODXyKEjOVSGxvSOIlLsCmLk8FwSsI9BemIgvTdlk4L9wLgrGeYLGJOCauvToN_a5iEB3uXKiPWA5547eD6H8H8NbEqas0zGf1WCqF9YMgjjJOejA5mayXyYugruor9W1b7P43yG0JMKkmy-NFdYhF_qdxp6VWTh4ax0W8jv_e31LPCq3m_235r4FQrIcDBsvQnIAOqRyHyM6EgE59Ex27zTXDht8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/867c2d8104.mp4?token=YT2W3kdDVbTARlzJdUMoEv0H27F7Tdz2vpPtmLiz_uIXzHsnuhMLD4HWvOeSldWIi7oWAd9eihYvyJ8fmoaqEwEYh73jT45dvDWmG23Exd65jlKMCEPJRPwB_xiYdpu_iN4CGkv3iOrFySM7ZwqMkyu6-r6w8GI9wj5IQEAAjDzuI-nmcSP88Cx9xGOxLK1lxQOUb4My1DCqYWkmzbty1rF177I0wBx2QRKQwT31t0J6OKeitH7ihScLrnggeuYNP0tWhg3rnSeTi0h7gNfYdL8Da5yhMKK2Jlacb7-paxs4w5z_ig_C9vwxCxFqzyXB3cUlM2FdCURfceq94BttIUiNeiiN-6zl4Hy77fcVv5tud0L4YVXHKm6aVFAsFbsYmUTlu30_ZgJh-kZ5zD87ouLGg4mXO6QItjGvBrURn5kDRiL7K28vX7uS-A4b2bahnqJ6bqqHoQGaV9oODXyKEjOVSGxvSOIlLsCmLk8FwSsI9BemIgvTdlk4L9wLgrGeYLGJOCauvToN_a5iEB3uXKiPWA5547eD6H8H8NbEqas0zGf1WCqF9YMgjjJOejA5mayXyYugruor9W1b7P43yG0JMKkmy-NFdYhF_qdxp6VWTh4ax0W8jv_e31LPCq3m_235r4FQrIcDBsvQnIAOqRyHyM6EgE59Ex27zTXDht8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎤
بخش دوم صحبت های تند خداداد عزیزی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/139132" target="_blank">📅 23:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139131">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🎙
درگیری شدید خداداد با خبرنگاران یزدی
!
پ.ن باز شروع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/139131" target="_blank">📅 23:58 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139130">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✔️
✔️
✔️
منهای ورزش :همراه اول تو جدیدترین شاهکارش، سقف مصرف بسته اینترنت ۷ روزه «نامحدود» شبانه رو از ۱۰۰ گیگ رسونده به ۲۰ گیگ!
✔️
اینترنت نامحدود تو ایران = ۲۰ گیگابایت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/139130" target="_blank">📅 23:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139129">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
سپاهان از استقلال شکایت می‌کند
❌
❌
باشگاه سپاهان به دلیل استفاده از یاسر آسانی در دیدار مقابل استقلال از آبی‌های تهران شکایت خواهد کرد.
❌
❌
این در حالی است که چند روز قبل سخنگوی سازمان لیگ استفاده استقلال از یاسر آسانی را قانونی دانسته بود.
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139129" target="_blank">📅 23:39 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139128">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✔️
✔️
گل‌گهر از سپاهان به خاطر کسری شکایت کرد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139128" target="_blank">📅 23:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139127">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">📷
جدول لیگ برتر پس از پایان روز اول از هفته چهارم  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/139127" target="_blank">📅 23:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139126">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyJ1Sk0Z9TbBc9Myh-5YE1jtcrD9m_hT-7NRU8XHvtXg_DB9c8KWL44ExolbADWQG3-xg1Wr9845TviD8KvdtnSOTLQNPIz9Qn47UMmclSjxAWu0gAuvnMyfX98g6ERDiVU9jwaRTYGUNteBJv9YSV8wWHB2D3s3bNjR0F2yCSa0kyf5rkubzlb1TtGUTh9R7K9b6U83_qYioj5YRGZJXuOIbiT48AhiTZ9mKAcdRGCwiD8Rr88szpxd6-ipxExCzbYnj3OvaTgYmVA86AaW-D3_qDGHOwwVDYstwTfKD0UvH1PFyIYHkRWTkR3g5kReWnjzW3J5quE9Nnf1FxXsjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
جدول لیگ برتر پس از پایان روز اول از هفته چهارم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/139126" target="_blank">📅 23:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139125">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfGjkzPwE4jrZgz-3QllHFv-T-Y3cChQn1V1t88EiMdsY2DXbZ08ru3bwe7MzH1-FJOsnmhsnZLJmeOvz7fOdAamL6SJmX8nHLYAV_neh6kxiCCepK7Af5unGxLNOf59WeqUYrQJi-zsl9Wme752VbWSkxu8GGkzWpxJWzlCe9ZPHzPdXp5duUzv8A7JJ7-PKCXIcXAzhHok3BPo4-7TP7nWLca_Sk29y7a7a0RZoeEPBB_Y9GBGiImQzo987-zPCM_Xb8MTvLLRpYNiEXOeCZO00B6wNmQYsMEoaOxZC161RzowWK3Coq0CEY-unMW0oisVuMa_F4hXr_jke83bfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شرکت یوسف جامه اسپانسر جدید پرسپولیس شد و قراره ۵۵۰ میلیارد تومان در سه مرحله به حساب باشگاه واریز کنه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139125" target="_blank">📅 23:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139123">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✅
✅
سپاهان هم با دو گل کسری طاهری .گل گهر و دو هیچ برد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/139123" target="_blank">📅 23:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139122">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
❌
❌
آغاسی اخراج شد ولی قبلش آفساید بود و شانس آورد که دربی و از دست نداد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/139122" target="_blank">📅 23:24 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139120">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
آخرین تمرین تیم قبل از بازی ملوان؛ با حضور محمدحسین صادقی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/139120" target="_blank">📅 22:24 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139119">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✔️
✔️
بند 500 هزار دلاری در انتقال بازیکن پرسپولیس به نساجی
❌
❌
در بندی از تفاهم نامه انتقال قرضی براجعه از پرسپولیس به نساجی عنوان شده است در صورتی که باشگاه مازندرانی خواستار دائمی کردن قرارداد براجعه باشد، می تواند با پرداخت 500 هزار دلار به پرسپولیس، قرارداد…</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139119" target="_blank">📅 22:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139118">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🌬
پایان بازی
نساجی
0⃣
-
2⃣
شمس آذر
🔴
👔
اولین حیا کن، رها کن فصل در قائمشهر؛ روزهای سخت در انتظار مجتبی حسینی!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/139118" target="_blank">📅 22:20 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139117">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
🟡
احتمالا طارمی و سردار امشب برای اولین بار مقابل همدیگه قرار میگیرن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/139117" target="_blank">📅 22:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139113">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/acs7Pb2x38e26YtDTxO8edN98JirjBI8n5Lf4tRNoDowr9eS4b586kqwr1Tkqwc0c_E0LNTGTjE9gP0tN3uEKZzxO3hTYspPboOHnOulHDzX2NaErlOeXlP02spDZub9HUJ8N_189DXICguGTc42q-3g8VKaYOGiBPbPTRMnwfZU3r0tGagrythnGjVt-hCpcELiDkWPx1Ba7knUM47QeD53Kqpb4qxY9vM2SgcjAZUGZYp38q34a-lOm-iOfMmqAxCN7kqL4lwetSjFkzGq3e0uQ7IbNPySJ1s2ZSBeB1PFFwhUI01iDYsv_c3JOIJiNPfkN36JZqrJ7hQQoUW38A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VXPBWuAjU7FBDlJE7RC-pf05UkrnwSKzx19DeyeNhE74jonNd9VBZovshfdDWYbLGMJaalLbVgs74iKZRUTuEbvc8RJB1cE4_nDFy6dexWf0b2KErTHDlpkwj5H7DRiw3gRg8yaXc5l_dGb1gVHEEtC_xs07vMF1CGNLndb_qbTHjClyxYHYGfF9nrMCr6GoRLqV68TTymZc46v6YA00ATnN0MokIuUhZp8qpowUnfY9Hr5_3alHkkaz5z5rb43ke7PzWL0VJX0kHBFHTHWKkFBy_hmQcsfawCQP8h2HubRNqULn9c12B7BiVWJixCIcGWkVoHTYhro61374TjDkkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MyJgblZjkqiKWs2-5sSOTrIirrhDO0Qa5vesdE6AQpz4DcmU-zaY4KJnK8CYVD2jgVkHAJyk9WW4bx_Gcgi3OIesxyLdvKh-TREUxYfNLl8FiZGG56za8JtUtwqKAyuIBErtUoSllMeLBoR28GLrQmcuBEdQqdtuLcPlxEKhtIgVXhEdkeNR8RcLSQvw811C4rng_ZnJLXHUm7V-zavlk-qD9ChAYUMEkK3v3hPBftFjg5deYg45bJBV8VoM8kZwgwI9-P9ELCb79lD5z7WW_ksVJeRWuENsaJQztOt-7EDDOFEMuVaCVVMEaB57fohLyVVplhjN2EEE7I2Qj-s6PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F5F2q3B5ye_aWIFQKJcjB_evtfagDZe-_BD_B1IQjwpv5jUBUDcH4BNWZNMpuZz75MbyoucYylBz_5OYZTkU85ZJBW585dgHXPntRSYQtpirbc-DqnJldxV8UVh9YTNBe92t2BSjrMX8n5O2SJSI9sJw-wEjIb76ey1SVljwRLz1RIAU6J-HKXSXwGslaFRN8ZhcEq6bmpljTH4ryw0mpaKmjoDK0r7O88_mavNSQJnmZR8sZopFYrHknml16JY5Wv_VZyxK42_DKEHi8FTC7bONjFkaIICJqhA52E3JplkRdGv7fEWH_Cl3941qWBw-eNniwCBrYeaficQ7_J28Yg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽
🤩
پیمان حدادی، مدیرعامل باشگاه پرسپولیس، به همراه ناصر محمدخانی، بهروز سلطانی و مرتضی فنونی‌زاد رفتن سر تمرین امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/139113" target="_blank">📅 22:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139112">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
خبرگزاری فارس: تارتار دلش می‌خواست سرکیف رو جلوی تراکتور بفرسته داخل ولی تو ذهنش یه تصمیم تاکتیکی گرفت و فکر می‌کرد شهرآبادی می‌تونه بازی رو دربیاره
🚨
تارتار همچنین علاقه‌مند به سبک بازی سرگیف هست اما تعدد بازیکن تو تیم‌ باعث شده به همه بازی نرسه
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/139112" target="_blank">📅 22:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139111">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✔️
فرصت‌سوزی باورنکردنی فرشاد احمدزاده مقابل کیسه
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139111" target="_blank">📅 21:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139110">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTU-Wh8mk0z69ixzXZoxVD5pmpD0YuPim1wOPAUW_tVyw9o9YQv7uikwc0EHMXWU4xNWC2MusOfOSKU2JGeRRq_JqdkYgZ_jnuAcZ-EuarRR-gK_LRLTeQZSTC5yqGT0QgSs530MrHftmKJpndL_USJJA6qe3XLI8MOQgsWXIzbXnKsnylCcXPlHuTkuK-7W8UVWx0A_KDnFGwYDGG624Qx1AvCZVqCJs0RTZRkP2WNKNmNr0SCR2HU84KcsjSnoSJLQxwzbn7V4UCdhrLIO7xdcYAk5xyxnrVwM4EVtHSCyRWUHlqsowf-Wbd3klP_sohh9Z9UNU_ebkrOyQ6cexQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
حسین کنعانی ، دانیال ایری ، مجید عیدی ، پویا پورعلی و محمد عمری پنج بازیکن تیم پرسپولیس که سابقه پوشیدن پیراهن تیم ملوان دارن
✔️
فرزین معامله‌گری هم که برای سربازی منتقل شده به ملوان تنها بازیکنی که سابقه پوشیدن لباس پرسپولیس داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/139110" target="_blank">📅 21:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139109">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
✅
تراکتور دو بر هیچ برد و چهارمین برد تراکتور رقم خورد ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/139109" target="_blank">📅 21:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139108">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPzJDhj5E43vsALnEvUfyi3ktH5i4RpvkNOSKcGqzHDxw32DLrmW-GpdhBkJcbu6AuJHpTKL5CNEwnrZmwXTKxZNbU4QnL7asJckQBNaagsWsCN3LsfI78eswt0qvLTJPZ9fywhObIqGjoMI1T0CSnlGClnBDdQ-NQj9SvU54XvRM0W1n9cyxx-Lho6c-vdYNeOr7FFDypZqypLrmWZrrhOhgmHMFPivoEefBlBxyQGvxBG6KFCsqQ2b3EqqVHH7wb8QltgLAS2eP7bmpz6z33LeIVDPxHo4YI34Q6wFf6w3crXBua2rdEYXoRz1AOEa9UQjfcLmnW3b2UaWHPt8iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
تراکتور دو بر هیچ برد و چهارمین برد تراکتور رقم خورد ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139108" target="_blank">📅 21:19 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139107">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cbe495b77.mp4?token=UZM11F3Rhg8JxEfZuUKaem6xyssHpE9NZXz9cSlPdAEqJNmIVTbDZtYGAfMx8F2a_C5fRDlzeedAzyxXTgoQFUYFQ6CU3aBj88lxHrXyBZkfAkc57JQo71n0xEDlZiNVpHEkOA3k1JDCzEMeXMNR2KE5LffcOduEKpggNuYJTD9eP9Wf4YkPetMmPbu89PB4pG__VaVHYwrn0bxqGErIC7p-4rXkm0npv56cfW6RMlspDW2vzXhHNndS56cHkDsghQxA-lXubNi9wBdzk2uQ0Fvhr0QSZVg-_sdJwHQ8UZHB494PJjvEHMC1SUGZ70tj4yRIuvm4SPBNYQyG4wZoOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cbe495b77.mp4?token=UZM11F3Rhg8JxEfZuUKaem6xyssHpE9NZXz9cSlPdAEqJNmIVTbDZtYGAfMx8F2a_C5fRDlzeedAzyxXTgoQFUYFQ6CU3aBj88lxHrXyBZkfAkc57JQo71n0xEDlZiNVpHEkOA3k1JDCzEMeXMNR2KE5LffcOduEKpggNuYJTD9eP9Wf4YkPetMmPbu89PB4pG__VaVHYwrn0bxqGErIC7p-4rXkm0npv56cfW6RMlspDW2vzXhHNndS56cHkDsghQxA-lXubNi9wBdzk2uQ0Fvhr0QSZVg-_sdJwHQ8UZHB494PJjvEHMC1SUGZ70tj4yRIuvm4SPBNYQyG4wZoOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
فرصت‌سوزی باورنکردنی فرشاد احمدزاده مقابل کیسه
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/139107" target="_blank">📅 21:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139106">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
❌
ترتر گل اول و زد و الکی الکی سبک مجیدی یک هیچ یک هیچ داره می‌بره همه رو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/139106" target="_blank">📅 21:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139105">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmPzF6mo-BVvVb4ue1ybqFQVanvTII2mgAQCwm1jCnXKMRTCNl88mOhN8SAa8ntgriEzDy5WL-Q-T0qLJeC_67clNvvRukIu1n8zGFM2jxMp16NtMqk4PgDRPh6bdjCP6ipm-tsWS5-Nrcppn6uipI7leNbOTEJcSKwlMPZdHNnnw4JIL5ANXvdMk7UgM3MJLyBPQFaFbl3P-3I2Vnq0Pf1_4FxlyIyACI3L5d7wvDFW_p2aAkIMtQW4plsTR6Eyph1bIvFM079BxANR5eqOAUyVHue5LOT5_m2wgAZ-oCqVopkdUUQrMDs73d0YSfQaKdg4fNbqPuvNhNWFAJK4MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آخرین تمرین تیم قبل از بازی ملوان؛ با حضور محمدحسین صادقی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/139105" target="_blank">📅 21:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139097">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✅
حالا که حوصلمون سر رفته تو عصر جمعه میتونیم بشینیم پای بازی ترتر و چادرملو رو ببینیم که انشالله مساوی یا باخت ترتر و شاهد باشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/139097" target="_blank">📅 20:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139096">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvDSRCp79LAsNVN4g3HyjID8Qe5qAhDWsos50t6c6LawGS8SIzIaJkRJgeo--zK24ZHRBAga4V3G5N8VoabNz8NXc61fzac7Cegng3BqARVwLIg0wUWrkjX-7ZSqDYcg5AKQrf88HjNRDDm6-gH5Z795343vY2V6iv-iTmYDL-lkziH6FPwpjwnlvRfsOyFgQvT7tv0mb-Ap_M6cNdpEnEUXA7Prbh0ljn2Uh7CqetE8eT5TsWYepY4DUjO2pwmlorlTZWPMwnAbk9_SH0aNP4V-ytfaOe2hsLuaICKCK9KrM_Lpkh_d1xQQvZJWRIbPdrB6a0Je2P2ttTJ1EAklbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
دو مدعی، یک زمین، ۹۰ دقیقه نفسگیر
جنگ امشب در اهواز کفه‌ی ترازو رو به نفع کدوم تیم سنگین میکند؟ همین حالا میتونید این دیدار حساس رو در اسپورت‌نود پیش‌بینی کنید.
[
فولاد
🇮🇷
🆚
⚽
استقلال
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139096" target="_blank">📅 20:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139095">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✅
حالا که حوصلمون سر رفته تو عصر جمعه میتونیم بشینیم پای بازی ترتر و چادرملو رو ببینیم که انشالله مساوی یا باخت ترتر و شاهد باشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/139095" target="_blank">📅 18:58 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139094">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✅
حالا که حوصلمون سر رفته تو عصر جمعه میتونیم بشینیم پای بازی ترتر و چادرملو رو ببینیم که انشالله مساوی یا باخت ترتر و شاهد باشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/139094" target="_blank">📅 18:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139093">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
بازی تیم های مدعی در هفته چهارم
❌
چادرملو - تراکتورسازی امروز ساعت ۱۹:۰۰
❌
سپاهان - گل گهر امروز ساعت ۱۹:۳۰
❌
فولاد - کیسه امروز ساعت ۲۱:۰۰
✔️
پرسپولیس - ملوان فردا ساعت ۱۹:۱۵
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/139093" target="_blank">📅 18:54 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139092">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⭕️
⭕️
فوری/ آکسیوس : طبق گفته مقامات آمریکایی فشار اقتصادی به ایران تا بعد از انتخابات کنگره و سنا آمریکا (۱۲ آبان ماه) ادامه خواهد داشت و بعد از اون دوباره میرن سراغ بمباران و حمله نظامی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/139092" target="_blank">📅 18:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139091">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
فوری/ با اعلام مهدی تارتار باشگاه تا 22 شهریور بازیکنی به تیم ملی امید نخواهد داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/139091" target="_blank">📅 17:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139090">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
فووووری/ با اعلام فدراسیون فوتبال بازیکنان دعوت شده به اردو تیم ملی باید تا پایان روز شنبه هفتم شهریور خودشون رو به اردو تیم ملی امید معرفی کنن
😐
❌
❌
اگه پرسپولیس بازیکن بده عملا ایری، شهرآبادی و لطیفی فر رو برای دربی نداریم
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/139090" target="_blank">📅 17:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139089">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa7be285b4.mp4?token=igSxu8AMagboEO_HCCxqDB8ZhglDTeuNV25crYfKe86yZe8OXG5LjGW0H-W0V7mXY5QXqSSmGXTNf4tNJ2dBcxXIA4fAGKcSKBVi5BmmJft8pOD2jhPbuh3xESALIbraMBXMVcDBRgzlwQQZvWqNRE_kVngWDzFtc3_4bqyiyWb-20BL_1rmy2e6D31IY9VnoiXk0MMNFIyWuKNoSKIiG6iJ1_n23bm4r75buQ5ITLZ85XEINrjSanBiGCkS61g6KNzEKEzjy6QkD3VtHA28DXmrAZLFqSBbvf0w2q_1yroYN96IJzpHP7JtTK-_gm3qqWpRFLBpLxCRECvwfIn5Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa7be285b4.mp4?token=igSxu8AMagboEO_HCCxqDB8ZhglDTeuNV25crYfKe86yZe8OXG5LjGW0H-W0V7mXY5QXqSSmGXTNf4tNJ2dBcxXIA4fAGKcSKBVi5BmmJft8pOD2jhPbuh3xESALIbraMBXMVcDBRgzlwQQZvWqNRE_kVngWDzFtc3_4bqyiyWb-20BL_1rmy2e6D31IY9VnoiXk0MMNFIyWuKNoSKIiG6iJ1_n23bm4r75buQ5ITLZ85XEINrjSanBiGCkS61g6KNzEKEzjy6QkD3VtHA28DXmrAZLFqSBbvf0w2q_1yroYN96IJzpHP7JtTK-_gm3qqWpRFLBpLxCRECvwfIn5Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
مهدی تارتار: واقعا یک تیم نمی تواند 90 دقیقه تهاجمی بازی کند. ما باید طوری برنامه ریزی کنیم که بتوانیم به شکل خوبی 90 دقیقه را به پایان برسانیم
. زمین چمن یادگار امام تبریز واقعا استاندارد نبود و کار را سخت کرده بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139089" target="_blank">📅 17:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139088">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f04141bbb0.mp4?token=LfYo7kagczhzfHhEPBa1IDIBGRFhbfy9lr4bVha-u19BavuC4H_KBgjKs8sLKM65DeZpNnKI1CtC50p56TpwRGX6skAK5DoijoUhJm0-XezLGuIqjurQL8x4v2oSv53q-gcx6ibr9Bpi94jBo-ta4_EuTMYvQFs94zb7mkLMkn7Yky5hBn2p4CmA2PY3mIif1-ithsCBH_JABO5JyAOx5J-tsmz3mL7mtLu2FXOIh9gVIdb6_snPfEgFxYx1md3E_uPQ4P1mfXvYnfkzuiu3aE9ZnrKL5pSlbV0iPuhcU_xfe0WuJ3cVL3AxmVNC6andwu49uTSRme-r194OqXqXPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f04141bbb0.mp4?token=LfYo7kagczhzfHhEPBa1IDIBGRFhbfy9lr4bVha-u19BavuC4H_KBgjKs8sLKM65DeZpNnKI1CtC50p56TpwRGX6skAK5DoijoUhJm0-XezLGuIqjurQL8x4v2oSv53q-gcx6ibr9Bpi94jBo-ta4_EuTMYvQFs94zb7mkLMkn7Yky5hBn2p4CmA2PY3mIif1-ithsCBH_JABO5JyAOx5J-tsmz3mL7mtLu2FXOIh9gVIdb6_snPfEgFxYx1md3E_uPQ4P1mfXvYnfkzuiu3aE9ZnrKL5pSlbV0iPuhcU_xfe0WuJ3cVL3AxmVNC6andwu49uTSRme-r194OqXqXPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
مهدی تارتار:واقعا از شکست پرسپولیس مقابل تراکتور ناراحت هستم اما این هجمه علیه ما طبیعی نیست. ما اینقدر در ۲ بازی اول خوب کار کردیم که رقبا ترسیده‌اند. احساس خطر کرده‌اند از بازی‌های خوب پرسپولیس!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/139088" target="_blank">📅 17:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139087">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ef45c0a06.mp4?token=ajyiL3iOUYeKXW_L-n0aR3Z9TEIOIh3-YpfuSpLm-klkeXLKEDAaJSLtryrTu4sLOGtIRPwfwVx0hzIOHN4ZWj56Z8363PH472p4dSqHQfv_RdZhAPV3mOAhLXSHCBpFDasAoiSKkvPw-oGSwzD1DWSjjPcsAXUgnXKQM3FP1uur4BDBkGCKssS_mV-SBAaDrVXKTdWwmqCDku-Ramy3stUNfOmmGVYwVSa0p-V1zgclmULOT_YFMM58bhv1mKk4peTeeO3f_BOWwB6Hrng4yLV8_uNx6vqJAflvr7yBmedNjbXH3oRR4RRZ_e32yKzlozCCkBqLVaPUslTybMl7vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ef45c0a06.mp4?token=ajyiL3iOUYeKXW_L-n0aR3Z9TEIOIh3-YpfuSpLm-klkeXLKEDAaJSLtryrTu4sLOGtIRPwfwVx0hzIOHN4ZWj56Z8363PH472p4dSqHQfv_RdZhAPV3mOAhLXSHCBpFDasAoiSKkvPw-oGSwzD1DWSjjPcsAXUgnXKQM3FP1uur4BDBkGCKssS_mV-SBAaDrVXKTdWwmqCDku-Ramy3stUNfOmmGVYwVSa0p-V1zgclmULOT_YFMM58bhv1mKk4peTeeO3f_BOWwB6Hrng4yLV8_uNx6vqJAflvr7yBmedNjbXH3oRR4RRZ_e32yKzlozCCkBqLVaPUslTybMl7vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تارتار سرمربی پرسپولیس:
🔹
ارونوف یکی از بازیکنان خوب تیم ماست اما دیر به تمرینات اضافه شده است. بحث مصدومیت ارونوف جدی
نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/139087" target="_blank">📅 16:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139086">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7eb7a5402.mp4?token=dCvSZbVWrLVgbBrtrPxzOH2OsM5R4mjNIdt1MigBtFktBzo9HKpr7XICwvkPtkSX8V7G8AJUTOyKE9_uPDQhyehg-tELgQXehlOz8WoY70ZRWiBHZbS77qjFJKw-ka_YZJv4yOkRSgtOwQg6dg6Wv0bvFD4jKGV7z76tCLpSx-Pqrm_-D6r_89LioR5FlT3Ho2dUwLhLVc0h5302wmgjYgJOEfdAdTVIPcIyOSXypaBXUXyLMO4wfgFDe9f5jTpVdmeV3sbKgrW2Lv314Rb3738J0W6vhHGnRHmhijJHjFG3AJPVtsR1eMgyX4bVa4OcjEXkMwuKvK58s_tZVpRYqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7eb7a5402.mp4?token=dCvSZbVWrLVgbBrtrPxzOH2OsM5R4mjNIdt1MigBtFktBzo9HKpr7XICwvkPtkSX8V7G8AJUTOyKE9_uPDQhyehg-tELgQXehlOz8WoY70ZRWiBHZbS77qjFJKw-ka_YZJv4yOkRSgtOwQg6dg6Wv0bvFD4jKGV7z76tCLpSx-Pqrm_-D6r_89LioR5FlT3Ho2dUwLhLVc0h5302wmgjYgJOEfdAdTVIPcIyOSXypaBXUXyLMO4wfgFDe9f5jTpVdmeV3sbKgrW2Lv314Rb3738J0W6vhHGnRHmhijJHjFG3AJPVtsR1eMgyX4bVa4OcjEXkMwuKvK58s_tZVpRYqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تارتار
:
❌
• وضعیت ابوالفضل جلالی بهتر شده است/ بازی فردا مقابل ملوان را فدای دربی نخواهیم کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/139086" target="_blank">📅 16:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139085">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/587e6b7701.mp4?token=jG8B9UDXXmN827lqvgLNtWZmrqy-V6PR5ujfEvvA5M7F4VRIECBvs8PS5Y_p0EKzAfUuh-ZHtsSdj0EBWG0TTUdX3x-g9lPxhy4CtM-vWGqdLxrj-VqDWizcVnkwMqyGk0EjDPgD4L-rcIiehNgLjSM1J2uVDnuczidrtu34vuXTzWnUp2t0vxEB7WEfL8RgVWULCfZTCGn3to31ws6s1NkDCmptrvO4xtta_9I5sjgFVhQCiEA5P23mY9LVtH5SaqPa99qHlncCiw1gZxmNlVVdJtso6wPJiX86032qRjJzxdknqyvMss0mWxYmRxmpIwU11RhlIDVRaJjTEiMSaXQFYu5qY-p55tunhgIExlSBPEYznbxGjoh5shJc7MqIfWQdFhNzfEVJWYWjDs3sGZt6MtCb9Po8gNBV7ER0zsbnvuAkNxkrFWOXQay4aYsXqbatkUxBQb8lJM-uEtdYkHkLg6p1QRF06RmJZUGbxFWDDi6Fb3zvuFzPYp0qMrcTlJW3ybk05c8zovd2gM9pm2s5SoBkb8pxlEixz3CvkrBZG3xMqdEoTUXetl2B5wcUCxeihoDf1qpwh4PkJHcKdNQbmpipQI67k6pmsrxbdSaJ-Cg5Zst7EvEIpEy5nz1nd5UxToBzJAbrqD2YYTXozdVj3KQAqsSGbiPgU3pzwiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/587e6b7701.mp4?token=jG8B9UDXXmN827lqvgLNtWZmrqy-V6PR5ujfEvvA5M7F4VRIECBvs8PS5Y_p0EKzAfUuh-ZHtsSdj0EBWG0TTUdX3x-g9lPxhy4CtM-vWGqdLxrj-VqDWizcVnkwMqyGk0EjDPgD4L-rcIiehNgLjSM1J2uVDnuczidrtu34vuXTzWnUp2t0vxEB7WEfL8RgVWULCfZTCGn3to31ws6s1NkDCmptrvO4xtta_9I5sjgFVhQCiEA5P23mY9LVtH5SaqPa99qHlncCiw1gZxmNlVVdJtso6wPJiX86032qRjJzxdknqyvMss0mWxYmRxmpIwU11RhlIDVRaJjTEiMSaXQFYu5qY-p55tunhgIExlSBPEYznbxGjoh5shJc7MqIfWQdFhNzfEVJWYWjDs3sGZt6MtCb9Po8gNBV7ER0zsbnvuAkNxkrFWOXQay4aYsXqbatkUxBQb8lJM-uEtdYkHkLg6p1QRF06RmJZUGbxFWDDi6Fb3zvuFzPYp0qMrcTlJW3ybk05c8zovd2gM9pm2s5SoBkb8pxlEixz3CvkrBZG3xMqdEoTUXetl2B5wcUCxeihoDf1qpwh4PkJHcKdNQbmpipQI67k6pmsrxbdSaJ-Cg5Zst7EvEIpEy5nz1nd5UxToBzJAbrqD2YYTXozdVj3KQAqsSGbiPgU3pzwiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مازیار زارع سرمربی ملوان:
🚨
پرسپولیس پرمهره ترین تیم ایران است و کادرفنی خوبی دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/139085" target="_blank">📅 16:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139084">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
بازی تیم های مدعی در هفته چهارم
❌
چادرملو - تراکتورسازی امروز ساعت ۱۹:۰۰
❌
سپاهان - گل گهر امروز ساعت ۱۹:۳۰
❌
فولاد - کیسه امروز ساعت ۲۱:۰۰
✔️
پرسپولیس - ملوان فردا ساعت ۱۹:۱۵
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/139084" target="_blank">📅 16:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139083">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
بازی تیم های مدعی در هفته چهارم
❌
چادرملو - تراکتورسازی امروز ساعت ۱۹:۰۰
❌
سپاهان - گل گهر امروز ساعت ۱۹:۳۰
❌
فولاد - کیسه امروز ساعت ۲۱:۰۰
✔️
پرسپولیس - ملوان فردا ساعت ۱۹:۱۵
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/139083" target="_blank">📅 15:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139082">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6LlLOvr6ffyGca_fMVXg_rzjLsUWG1hlJvtDRwKDPLIKLRAgCss9ZNbQnB8yW9PjO1eFl7YTr5AnvhVWwWRlY5RuLzYDhsO4bUFKXeySr64SMxaoswPp-VS4cbw1zVuCcWiP7pWenRDlyRxr-NhVTmiTtkPjyyORFu5xJrAhNDT5iuFPodxrEfaXz-r5KwuQCzJ4uZSPnkVUqRfep2W5yfFdt4-OOT8RcCTDgu_rxi9FnLgybe2iun_vHBPMrgqFSsYYXFlbCIK7Z8Bhn81d17-0c0vPa1IXjzk-cmAAWptsxTVpu7WlVd0lFUh0ZyNIp7O-0aXPfxvo4YPXd8qjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خبرگزاری فارس: تارتار دلش می‌خواست سرکیف رو جلوی تراکتور بفرسته داخل ولی تو ذهنش یه تصمیم تاکتیکی گرفت و فکر می‌کرد شهرآبادی می‌تونه بازی رو دربیاره
🚨
تارتار همچنین علاقه‌مند به سبک بازی سرگیف هست اما تعدد بازیکن تو تیم‌ باعث شده به همه بازی نرسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/139082" target="_blank">📅 15:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139081">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etTHqKXkB3WaYSoLdjbDYtO6iDG5Esx0nV8tfh1a7VX5J4qBNJdp3XHcZ7HnXshVMbyT9O09M4cytX5kga1GKIde71G5h_n-PLlWPGi9BeTdhrkHL-5ZwJ7BBqViCk2jfKjEjNxkDSvQQGJouiIYoppVEkDKprlFA9Le1EneyMXueB3fJsKJPoXI4OREHPDGWV7AHnjtF9nRPyDy88ZQnNVCUnE12vXoFKecS6FV2uz_kZRMGkj98eHFphEk4z2sg0dzuh0muyCas2bRZhKWnVOqw6XlXA9PquAHrxLPD07S07oJn7GajXfFtF1Y0Ek_4FTEL4JtV1-6XCx1nB0M9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
احتمالا طارمی و سردار امشب برای اولین بار مقابل همدیگه قرار میگیرن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/139081" target="_blank">📅 15:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139080">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MK47A0bvI8Eh_Pl-CGrThO-OJZlYrSvZlTFJh8Y3N7TdjAflZMSExzAymGGafjV3YqZxzwap5TuCwP8UtbNhJxVEa-rtQWxKFXpQV3sBIrvwW7nhvOhoAOjfr9qnIGvcruhCTJQ1Om45y9QxmBtTbNjOorJxsSczYL4n3FN2k74HwmEuqUQfXDd5JS3AH0Q0WoWfohyplItjE1oujfjsL2a7IcC5MESOe5EpsxO5nBauLEqT_0NHdt7KgXpY-xmOMyIExoz4aB-Y9ZiruDZdARkrnhZ5gaYNtvYAXtmYIYBEkytjBdftu-xBIGiPAYnMSJmgHH0B5fybV4hT7Z8Keg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
💵
مهمترین بازیکنان آزاد ایران و ارزش آنها در ترانسفرمارکت تا این لحظه:
🔻
محمد محبی
- 2.5 میلیون یورو
😀
مجید حسینی
- 700 هزار یورو
🔻
رضا اسدی
-  500 هزار یورو
🔻
فراز امامعلی
- 450 هزار یورو
🔻
علی کریمی
- 350 هزار یورو
🔻
مهدی مهدی‌پور
- 350 هزار یورو
🔻
ایمان سلیمی
- 250 هزار یورو
🔻
امیر عابدزاده
- 200 هزار یورو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/139080" target="_blank">📅 15:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139079">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivXJ9-njVb_H8hLz7y7lgjDErhAjqvsPeWnJTfKEP1ylZg532MIWPB9ph326zx7FFVYXKi_CpdsqrdJJOShGbJHqGdnY9kL2qRby7LtFenTJES3t_stgnT2F_7pt2cMQLu4g4j1vr2IvdhkRwtyfSmiJgz-jGRH3pHUEqxOgRZTpuYe7oi9dBxpQ1iD3i09P34pQYHr0p0cjsqd9W_xT_-DdTy6m_HLpw359_Bnlj1nMeka-1ULyNY7RJSzS8LteyqFoy-x1O-TVTeClSoKllwGTD73qch7aJOCVRea57rPCiPvpCYUa4cGPlE4-9AtUKDVVpcZ6j0-C3FSm-udWnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
چادرملو برای فرار از روزهای سخت، امروز باید مقابل تراکتورِ آماده دست به کار بزرگی بزند؛ تراکتور با شروع قدرتمندش، برای حفظ روند خوب و اضافه کردن یک برد دیگر به کارنامه‌اش به میدان می‌آید.
[
چادرملو
🇮🇷
🆚
⚽
تراکتور
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/139079" target="_blank">📅 15:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139078">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❤️
فووووووووووووری
🔴
گفته میشه محمدحسین صادقی دیروز تو تمرین پرسپولیس با یک بازیکن درگیری لفظی داشته و توسط مهدی تارتار از تمرین پرسپولیس اخراج شده / هفت صبح
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139078" target="_blank">📅 15:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139076">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
❌
تصاویری از تمرین امروز عصر سرخ ها پس از یک روز استراحت؛ارونوف بدون مشکل در تمرین گروهی/گرا و جلالی مصدومان پرسپولیس
❌
کنفرانس مطبوعاتی تارتار و مازیار زارع فردا ساعت 16:00 در هتل المپیک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139076" target="_blank">📅 14:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139075">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✔️
✔️
✔️
بی انصافیه اگه از عملکرد خوب مهدی تیکدری نگیم!
✔️
برای اولین بار تو عمرش اومد پست غیر تخصصی دفاع چپ بازی کرد و هم در دفاع و هم در حمله موثر و خوب بود
✔️
✔️
پر تلاش و انگیزه از دقیقه اول تا آخرین دقیقه ظاهر شد و امیدوار مون کرد
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/139075" target="_blank">📅 11:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139074">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
امید عالیشاه به علت مصدومیت چهار هفته از میادین دور خواهد بود
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/139074" target="_blank">📅 11:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139073">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🔵
🔴
کشوری فرد دبیر سازمان لیگ فوتبال ایران:
🔴
سهمیه هواداران در دربی استقلال و پرسپولیس ۵۰-۵۰ است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/139073" target="_blank">📅 11:39 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139072">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
❌
ادعای هفت ورزشی: محمدحسین صادقی به علت درگیری با دو بازیکن پرسپولیس از حضور در تمرینات منع شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/139072" target="_blank">📅 11:38 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139071">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
مهدی تارتار سرمربی پرسپولیس، محمد حسین صادقی وینگر جوان خود را به صورت کامل از تیم کنار گذاشته است و هیچ قصدی برای استفاده از وی ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/139071" target="_blank">📅 10:26 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139070">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
❌
هادی چوپان مستر المپیا را از دست داد
✔️
✔️
هادی چوپان، پس از غیرفعال شدن ویزای طلایی امارات و از دست دادن مصاحبه سفارت آمریکا، از حضور در مستر المپیا ۲۰۲۶ انصراف داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/139070" target="_blank">📅 09:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139069">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❤️
صبح آدینه تون بخیر و شادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/139069" target="_blank">📅 09:10 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139068">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔵
ورود به اسپورت‌نود، فقط با یه کلیک!
📌
هنوز برای ورود، دنبال لینک و مسیرهای مختلف می‌گردی؟
📌
وقتشه راه ساده‌تر رو انتخاب کنی!
🔗
با مینی‌اپ رسمی اسپورت‌نود، همه‌چیز یکجا و آماده‌ست؛ ربات رو باز کن، وارد شو و مستقیم به امکانات اسپورت‌نود دسترسی داشته باش.
1⃣
-  بدون لینک‌های سرگردان
2⃣
-  بدون مراحل اضافه
3⃣
-  سریع، ساده و یکپارچه
🔗
مسیر ورودت رو کوتاه کن؛ اسپورت‌نود همینجاست:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
📌
کانال رسمی اسپورت‌نود:
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/139068" target="_blank">📅 01:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139067">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❌
❌
تارتار با حضور بازیکنا در تیم ملی امید خارج از فیفادی مخالفت کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/139067" target="_blank">📅 00:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139066">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⚠️
یایا امپرور بعداز نتایج درخشانش تو عراق میخاد برگرده ایران…سپاهان هم یه نیم نگاهی بهش داره؛فورا باید اسپند دود کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/139066" target="_blank">📅 00:39 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139065">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
فووووووووووری
❌
❌
یک سری شایعات پخش شده امسال بخاطر فشردگی تقویم لیگ خبری از جام حذفی نیست و قراره سهیمه آسیایی جام حذفی به چادرملو داده بشه
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/139065" target="_blank">📅 00:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139064">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✖️
✖️
بهمنی رییس سازمان لیگ: فکر نمی‌کنم بتوانیم به خاطر فشردگی بازی ها امسال جام حذفی برگزار کنیم
🙁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/139064" target="_blank">📅 00:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139063">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشــًٍـٍؓـٍ۪ـ۪ؔـٍ℘ًًیــًٍـٍؓـٍ۪ـ۪ؔـٍ℘ًًد۪ؔاٍؓ℘ًً</strong></div>
<div class="tg-text">تا میتونی اورنوف تشویق کنید و سرگیف اینا ستاره تیمند ارزو هرتیمی ک این بازیکن داشته باشند و ایری هم تشویق کنید روحیه اش برگرد</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/139063" target="_blank">📅 00:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139062">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🅼🅴🅷🅳🅸</strong></div>
<div class="tg-text">پاس هایی ک باکیچ میندازه رو هیچ بازیکنی نمیتونه تو پرسپولیس بندازه بعد کلا یارو رو نیمکته</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/139062" target="_blank">📅 00:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139061">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0zbwwgJSPEdFWVhHUmj41eT-QWnwif-DHck1Z_97e_LT4fl8BHgGXwmIgniafIRQATavNO-WYWdN4Bc1PLVSPG1ztapnX1qqMeTbt2-771hUiGNSzA4ydDRN99hFHUrZ85J-4Bm4o2sOPx7DxGrEBW--XOH3sImS1qu1grOIcFXgOKZR7-iutVCsLoi_fJEBKf5i47cwxD4ZxPb0nMfwH28kJpA6G-_bAGCJhlPHC9g0I2wIJmzOugN36zhGTvXo_z18drexwUUWNsMdI0IFvf5xuq-bynA41loqTKEb4xu84Ow26aWWTg__HS6-H7c4d5IUHujhL_KBgcrCbQ9Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فارس:
⌛
مدیریت پرسپولیس تصمیمی برای تغییر در کادر فنی ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/139061" target="_blank">📅 00:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139060">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d099f34763.mp4?token=jqSGcxUaxhM7ThofZ2_TlMFJ4WpCmtDd_a4q09RKs_m0vlP2ucfFgYZbGGuZWy7PjdCOuK4W9C86psa3IUAv1ZmZL0W0LzY3rxpnLahbfkx4-_00VZc-OcnIJPlPWnYOUCPILui6aFj1IMafimH074l4CmsVNhy6QDCME47Umxib3-3xZ9F5fdb_4-aRqQG2a7gPIITsCt1fy-DNKdhsam3aBT1CgLYTiyIzf0fBg_clu8uaxcoyYuBsX2-6GFTxnAVZcLJZHV1JXVfNNxiv8hF213hyabojNRqjZwuy9bJgN1MS6wryg546LqOMSQqGp0-ObplCPnm7cziSKvBJcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d099f34763.mp4?token=jqSGcxUaxhM7ThofZ2_TlMFJ4WpCmtDd_a4q09RKs_m0vlP2ucfFgYZbGGuZWy7PjdCOuK4W9C86psa3IUAv1ZmZL0W0LzY3rxpnLahbfkx4-_00VZc-OcnIJPlPWnYOUCPILui6aFj1IMafimH074l4CmsVNhy6QDCME47Umxib3-3xZ9F5fdb_4-aRqQG2a7gPIITsCt1fy-DNKdhsam3aBT1CgLYTiyIzf0fBg_clu8uaxcoyYuBsX2-6GFTxnAVZcLJZHV1JXVfNNxiv8hF213hyabojNRqjZwuy9bJgN1MS6wryg546LqOMSQqGp0-ObplCPnm7cziSKvBJcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتشار تیزر رسمی سریال کمدی «مرد سه‌ هزار چهره»؛
آغاز پخش از جمعه ۱۳ شهریور از شبکه سه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/139060" target="_blank">📅 00:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139059">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‼️
👤
آقا مهدی فرمودن دستیار خارجی نمیخان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/139059" target="_blank">📅 00:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139058">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‼️
👤
آقا مهدی فرمودن دستیار خارجی نمیخان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139058" target="_blank">📅 23:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139057">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✔️
✔️
⚡️
⚡️
⚡️
علیرضا همایی‌فر، یعقوب براجعه و محمدحسین صادقی از جمله بازیکنانی هستند که احتمال دارد در ساعات پایانی نقل‌وانتقالات از پرسپولیس جدا شوند و به صورت قرضی راهی تیم‌های دیگر شوند
✍️
🗞
خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/139057" target="_blank">📅 23:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139056">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
❌
قدوسی: اورونوف تو بازی با ملوان هم روی نیمکته!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/139056" target="_blank">📅 23:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139055">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✔️
✔️
✔️
✔️
ارونوف از امروز در تمرین پرسپولیس
🔴
اورونوف که در بازی تدارکاتی پرسپولیس مقابل امیدهای این باشگاه بار دیگر احساس ناراحتی کرده بود، با پیگیری کادر پزشکی و انجام بررسی‌های لازم، ظاهراً شرایط مطلوبی پیدا کرده است.
🔴
این بازیکن از امروز در تمرینات گروهی…</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/139055" target="_blank">📅 22:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139054">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔄
❌
اسماعیل کارتال با فنرباغچه در مجموع 3-2 تیم لیون رو تو فرانسه شکست داد و به لیگ قهرمانان اروپا صعود کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139054" target="_blank">📅 22:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139053">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dkl04kOldeOegg0oKn277loWzZPatbPOtd15ayTwRVbOpMrBogJxt8Y6cJhOaWKfv4YN15nK9RFDO9Y1Ea8eS-TN4oo2D9L1O38JxSTS7FNrZ6jaoJSr-FnSCQ8IFvYFi738UsLURwpvBjeRcwGMYnTLCrHVMpBF6KuQid71dasAKDllylszQ0Dne5EMfhlnRVtZ3Gn_kjzRQCpFs_Y7fgmpodrLw800P4zK6YOMBPElcNDtAjFBG5xGrVfQkPKBczEfl70wumO6f917IY0wVuNvrr6k7kHyI8P0HzNJvI-rcZARNXdEDxRX62f4a4LGfwM_9eCwFignPUo_mxgHhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
آبی‌ها آماده‌ی شکار؛ لوتون سد راه چلسی!
نبردی که می‌تونه از همون سوت اول بازی غافلگیرکننده باشه.
[
چلسی
🔹
🆚
🔹
لوتون
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139053" target="_blank">📅 22:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139052">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✔️
✔️
✔️
✔️
ارونوف از امروز در تمرین پرسپولیس
🔴
اورونوف که در بازی تدارکاتی پرسپولیس مقابل امیدهای این باشگاه بار دیگر احساس ناراحتی کرده بود، با پیگیری کادر پزشکی و انجام بررسی‌های لازم، ظاهراً شرایط مطلوبی پیدا کرده است.
🔴
این بازیکن از امروز در تمرینات گروهی…</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/139052" target="_blank">📅 22:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139051">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔹
🔹
فووووری
🔹
فراز امامعلی : به عنوان دفاع چپ با پرسپولیس به توافق رسیدم و منتظر جلسه نهایی عقد قرارداد هستم. دفاع چپ و وینگر چپ میتوانم بازی کنم. آقای تارتار و باشگاه پرسپولیس به من لطف داشتند و برای پست دفاع چپ من را انتخاب کردند.
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/139051" target="_blank">📅 22:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139050">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvTryYOz3p33iszOs7gyqrXAP8vN8-nzvWcSIH6h-WDHrKlOPDLQ2jpSVAa5kr55hhJKNsgnGmqmaGMBN8e108XXHLoSrMZwDEIcBOjGAGoYUcW2_CP013ot_LE3v5OItlnvsBgLrNd3Rr4S_oEoy_7Bx9QKktXIthVJ18SDiW_sQG77fXtisLYtpZYePb6OWccpXxoqgT39mCtj_I4R97aDS31I8kKpx7tpYvziDmtLD1dH97X4XdW_JWoB64DpjCx1LneQmYrmbZwzREP_peebZTPHsi2FG__qFMHEb74f6Q_uDna6cc8CmwXUFXmghb11ckOA9MW5Z277JbYGZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
تصاویری از تمرین امروز عصر سرخ ها پس از یک روز استراحت؛ارونوف بدون مشکل در تمرین گروهی/گرا و جلالی مصدومان پرسپولیس
❌
کنفرانس مطبوعاتی تارتار و مازیار زارع فردا ساعت 16:00 در هتل المپیک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139050" target="_blank">📅 22:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139049">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✔️
✔️
مدیر پرسپولیس: فراز امامعلی مدنظر ما نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/139049" target="_blank">📅 22:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139048">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
فراز امامعلی: پرسپولیس یکی از تیم‌هایی است که با من مذاکره کرد. اتفاقا به توافق نهایی هم رسیدیم و منتظرم ببینم جلسه عقد قرارداد برگزار خواهد شد یا نه
❌
❌
راجب پست‌هایی که توانایی بازی داره گفته: هم دفاع چپ بازی میکنم، هم وینگر چپ و هم مهاجم نوک
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139048" target="_blank">📅 21:08 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139047">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cp5sQW5i6KptH1DlnDXKWnKfMNkrS0-900T1q2Pezggh7kBvdhxI2fMPSnjVJpuvVCic4p0fcXPVfFmQrlUJ3jtX-hl4Avc02E_nPa5NoKKPg0jH66ZQmmWeuIs28udCWGlG4BFzL4rZMHXnusWUVVCzGiNVdTfp6qJnVQWgw3yVV1H9IvlaUoN4EEyn7iKXgfFk93ZSYeNO2iy1xIgpruH0FPJF7Z3ZeiOTW_sXeduTdGovp_QuW3kHboWiEMP7Hin3Fo3pG6mt4PqoXFp1wM0KXDq9IAJCOF1M-KtcbryudZ4XfyaDpLc5JEOsKskg9OjQZQLBqCK-o8Xp20Q5Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
اسکواد پرسپولیس با ۲۶ بازیکن برای فصل پیش رو بسته شد
🟪
۳ گلر
🟪
۵ مدافع وسط
🟪
۲ دفاع راست
🟪
۲ دفاع چپ
🟪
۵ هافبک وسط
🟪
۳ وینگر چپ
🟪
۳ وینگر راست
🟪
۳ مهاجم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
﻿</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/139047" target="_blank">📅 20:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139046">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔹
🔹
فووووری
🔹
فراز امامعلی : به عنوان دفاع چپ با پرسپولیس به توافق رسیدم و منتظر جلسه نهایی عقد قرارداد هستم. دفاع چپ و وینگر چپ میتوانم بازی کنم. آقای تارتار و باشگاه پرسپولیس به من لطف داشتند و برای پست دفاع چپ من را انتخاب کردند.
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/139046" target="_blank">📅 18:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139045">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🔹
🔹
🔹
🔹
🔹
🔹</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/139045" target="_blank">📅 18:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139044">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🔹
🔹
🔹
🔹
🔹
🔹</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/139044" target="_blank">📅 18:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139043">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✅
✅
عادل فردوسی‌پور: فدراسیون لحظات آخر تصمیم گرفت سردار آزمون رو برگردونه و به جام‌جهانی ببرنش ولی یادشون افتاد اسمش تو لیست اولیه و ۵۵ نفره نبوده برا همین نمیتونن ببرنش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/139043" target="_blank">📅 17:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139042">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✔️
✔️
✔️
اورونوف و سرگیف هیچ مشکلی با تارتار ندارن/برنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/139042" target="_blank">📅 17:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139041">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❤️
📊
نقل و انتقالات کامل پرسپولیس در فصل جدید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/139041" target="_blank">📅 15:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139040">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✔️
✔️
✔️
آقا کریم باقری به عنوان بزرگتر تیم این روزها خیلی حواسش به دانیال ایری هست و کلی با این بازیکن صحبت کرده تا روحیه اش رو برگردونه و داره کمکش میکنه تا اون اشتباه مقابل تراکتور رو فراموش کنه و بجنگه برای جبران اون اتفاق
🎙
امثال آقا کریم برای پرسپولیس نعمت…</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/139040" target="_blank">📅 15:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139039">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
❌
❌
مصدومیت اوستن اورونوف جدی نیست و جای نگرانی وجود نداره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/139039" target="_blank">📅 15:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139038">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjQCCV_zWY27w_uawKk-8rbhbPlaqLCLBebkevxt0_PEz-iyC0FQFC4h4TvRI6m3IWC_M3j2hf50gar5qL0Jqc4leu60QOB5JN2RPMqXm4-iAU3q2MHS-RKGImM1wMqrrrloSiEQX3DXQmWaduxbS1kP6ofe0o4uVHWEMxsW_eNYZc5q5pjHPX3kP7GHkdV6Q2yZIXgbcwJnyunI15y0At9b9QuB_B8--PYaLHHZ18lAkwgcg7lwqspDc79sMTPAWUyLRNVXCxxcHVNtQLOFGo9ENj64zEA3wGpwWOk5L9wFGVWQjs6CxW9Orm74RTPHp2m8pCKLZEJ-LfajqAOlEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
با ‌درخواست تیم ملی علیرضا بیرانوند تا نیم فصل اجازه بازی خواهد داشت تا در جام ملت ها آمادگی داشته باشد سپس به سربازی میرود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/139038" target="_blank">📅 15:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139037">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyLs8OJnWl92IT5wC66u1EINBiD-4mjxaolDtjOhTVYKFbRcs98A5h-rE85dlNB9RETKfV43mJbItAXdFs1DDZ0h6cG_4GVEkt-orx9u7iTIzI2NL6746C0CXDqE3FVNLzulNuftT5zNOEF-nIelw-dBnzskNRU0FB3xqW7JjIhK6RV2Cabe2wM6K6HIUZIIg94Pss9Ey7Vf-awOSxoidF1lYe5Vsi3VCnEbqBI5MBsXdV2gcaV_ZgLfJskveuEyb0xZJQwwFRml6TdT4q0InV2ZX4Yzy5DJO6il9rRm-YYmflxgk_d0ZVzqqdFxAoRpWmTBMFAFNHuEQ7pe2QmEmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
دو گزینه اصلی قضاوت در دربی 107
💢
کوپال ناظمی و موعود بنیادی‌فر، دو گزینه نهایی کمیته داوران برای قضاوت در دربی تهران هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/139037" target="_blank">📅 15:00 · 05 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/urFNX22FrJggyHxBjMD_j3Q5_l4L9NJN-jTYlsscJc-qppcgHVp1kf3V9evIbNGSonmr3J-lHWW7WWWJPuv4vu6zJqLDu7n1lIKqf-vbsYcUeeCrW0ij3gZOsWV_g2fyFuWfQrOtSHC7haPFQxeAc7-XfP2425_R3UDDia49UkIU45rnOZVgE3YO4mH8hsk8lhssIfPHktJY0CPN_AMNdoK9PeyJK1sAZyKaNtQMIDSugDIP8Fra94gsXNZZt3UYqo1_EW_8IQWbq5jKyaG0g0sn4CKZeRO6gWOeWtNZDUdc4QCVPIj_v0afBfT8_jM35yDv8dFJTZH3eUzfnS_ETA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 905K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 19:30:02</div>
<hr>

<div class="tg-post" id="msg-123995">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
منبع آمریکایی به سی بی اس :
فعلاً برای رسیدن به توافق با ایران هیچ ضرب‌الاجل و زمان مشخصی تعیین نشده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/alonews/123995" target="_blank">📅 19:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123994">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SU8qk_t8xBptDOZcXjCRecDU4K3KmCYNvlR8K2BmQFvJjh-ZEipKQh-yXrY37x6CGqai2U7EEXLdJgdu4nJ7-4Las2kKaFas0KN1-sh_NrrgBhNty5U0HNtvCwctP0QXKQZAgsafwB7kiyAiMBFZmXYs1MAHsud1ISJ7OTH2Xg1FAQhSXrec9yfBwsPruA6yaTjmyaJFIEu_dXMJSbANLk-3fCvtnUaUwX_GwqEzRD_c5L3txa87PB5PL55fe3n05ho-CGUY9xDUfML5ex8Bvhi8bAFibMGoxkmNahuLCkVB-nr_o4OCTK2gII5NNh3GBviiFx1MyP1ANX8VIimCzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این تصویر که میبینید اولین جلسه مجلس شورای اسلامیه که فقط با حضور ۱۴ نماینده برگزار شده.
۱۸۷ نماینده به صورت آنلاین شرکت کردن و ۹۳ نماینده دیگه حتی به صورت آنلاین هم حاضر نشدن.
🔴
طرف نماینده شهرشه ولی حتی حوصله نداشته آنلاین شه بعد انتظار دارن دانش آموزا و دانشجوها هر روز به صورت مجازی تو کلاسا شرکت کنن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/alonews/123994" target="_blank">📅 19:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123993">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 9T!
🚀
❌
آفر فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!  @Netaazaadbot @NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15 سرور اختصاصی پرسرعت
✅
اتصال پایدار و بدون قطعی
✅
سرعت بالا…</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/alonews/123993" target="_blank">📅 19:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123992">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W6zgeMLaZGLvS5deinV3Ybyw7HzCbdJ3oxWxHiy5LwpdeGddvKO94zwAxtqeEQC5vIRzp0hLK0x387l45yadG1Q-8em-fhTq7vTZzOb4he6FspCjNXtpWBUS4FxNef2JVsyOvGF2Yes2ysJsQHnH9-ULfFmYazhmAPkZhW6jt2MvVXo0cSsmOBn-Mr5PYzA8w-uK2vGfJSzilOj-EEiKDYVUsGNH46MocS0hAC6X3yI_IcVCqc093BVYAi492q3v5BcwnwPM51Gc6D6T73xkKbA3AdCH0bQMwbYnH5Dx_ICGP-9D9K0QKcyDRivjLe5h5wtoCYUkOvMDmaG_5R9TRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 9T!
🚀
❌
آفر فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!
@Netaazaadbot
@NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15 سرور اختصاصی پرسرعت
✅
اتصال پایدار و بدون قطعی
✅
سرعت بالا حتی در ساعات شلوغ
@Netaazaadbot
@NetAazaadBot
💎
کیفیتی که بعد از استفاده متوجه تفاوتش میشی!
📩
برای خرید و دریافت سرویس استارت رو بزن
✅</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/alonews/123992" target="_blank">📅 19:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123991">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
کانال 12 اسرائیل: حزب الله از صبح امروز بیش از 20 راکت به سمت شمال اسرائیل شلیک کرده است‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/alonews/123991" target="_blank">📅 19:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123990">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
انفجار مهیب در میانمار، دستکم ۵۵ کشته
🔴
در انفجار مهیب در انبار مواد منفجره در نامکام در میانمار، دستکم ۵۵ نفر کشته و بیش از ۶۰ نفر زخمی شدند.
🔴
از سرنوشت چندی نفر دیگر خبری در دست نیست .
🔴
در جریان این انفجار ۱۰۰ خانه آسیب دیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/123990" target="_blank">📅 19:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123989">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
فوری/سی ان ان:
ترامپ با آزادسازی هرگونه دارایی ایران در توافق احتمالی مخالفت کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/123989" target="_blank">📅 18:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123988">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70850c8c7e.mp4?token=HVi0TucKzfUMTqn3Vur4CpXPvopzsSed0z-lNGf95w2lMEzaZU4_RiJM93pd55o_x5K38S9WABwct7En5FxHxkX3OO_F8U4Kg8hAWUEdNvfZtalylfSqChGgsEsyiFGgzpIOGwQyFmM-MQ73pdtOCZfosN6s3s2EV4-uwKODLxw0x4-wCHGs-rjNTUS5lgFRSh-pe4SYOuiL3uM7QyziU8EJigb_WmVJ9JxRN7KfIIpe8dbadbG6aK3VL1olfHksB2Q-JN9T2yg9PYB6KuOrUw30vpGbe0cSUpwTMsfA5a4XY387t9Go8WcAUt4sh-GATLESldLnrs4aE_zcxgFujw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70850c8c7e.mp4?token=HVi0TucKzfUMTqn3Vur4CpXPvopzsSed0z-lNGf95w2lMEzaZU4_RiJM93pd55o_x5K38S9WABwct7En5FxHxkX3OO_F8U4Kg8hAWUEdNvfZtalylfSqChGgsEsyiFGgzpIOGwQyFmM-MQ73pdtOCZfosN6s3s2EV4-uwKODLxw0x4-wCHGs-rjNTUS5lgFRSh-pe4SYOuiL3uM7QyziU8EJigb_WmVJ9JxRN7KfIIpe8dbadbG6aK3VL1olfHksB2Q-JN9T2yg9PYB6KuOrUw30vpGbe0cSUpwTMsfA5a4XY387t9Go8WcAUt4sh-GATLESldLnrs4aE_zcxgFujw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه اصابت یک پهپاد حزب الله در داخل پایگاه نظامی ارتش اسرائیل در نزدیکی بیت هیل چندی پیش‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/123988" target="_blank">📅 18:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123987">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
حمله مجدد اوکراین به نیروگاه هسته‌ای زاپروژیا در روسیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/123987" target="_blank">📅 18:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123986">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91e2d4b641.mp4?token=Px6Rtvmt2rxGeme07N4yB3yNoyBsnGNo84ftIxh2Xbuquc8GkYvB4po8LOCoXGhkxY2oHbxaE5gu28H6sngdko780eZk9VrlCPf-B--yCdg9n5sbXvucfFsa2L3cSBCKJg8M85qUZJ_JiulF_CbuNszr90UY8b6KknNgnBQaKtUVR6jstoKi6QBkdmTi6hYZv_lT_HMugKULT2Az8U4_yRwqAqzgShaEuTgYchOIlgC75zSp90gm_qhwRTjMzjU56_Le1H27Xk2js72BB2lQm5u28Fak7qE00B6-9xMJ_SN00LhcYhXI104cuU35oz1cV-dl9q3mIPAal9sUbgeXdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91e2d4b641.mp4?token=Px6Rtvmt2rxGeme07N4yB3yNoyBsnGNo84ftIxh2Xbuquc8GkYvB4po8LOCoXGhkxY2oHbxaE5gu28H6sngdko780eZk9VrlCPf-B--yCdg9n5sbXvucfFsa2L3cSBCKJg8M85qUZJ_JiulF_CbuNszr90UY8b6KknNgnBQaKtUVR6jstoKi6QBkdmTi6hYZv_lT_HMugKULT2Az8U4_yRwqAqzgShaEuTgYchOIlgC75zSp90gm_qhwRTjMzjU56_Le1H27Xk2js72BB2lQm5u28Fak7qE00B6-9xMJ_SN00LhcYhXI104cuU35oz1cV-dl9q3mIPAal9sUbgeXdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فواد ایزدی: از من به یادگار داشته باشید که در ژانویه، مجلس نمایندگان به دلیل جنگ ایران، ترامپ را استیضاح خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/123986" target="_blank">📅 18:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123985">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d8b0f815b.mp4?token=h-68XiZGBuD79ApdVsKrseF7VJUFd95wyD5dRa9RoiyaoKxWR9pASJ2pCHlh81BjPJUSNgE7X41CtqZg_qIGPIgJ3_TfzGoLiDvnb3GW2uTSJOtmJ-MBO0W_L_iCmhx07aN948kNDB_v3jYQboJI2gzSkOXqQEy4WiE2k4EdCcFGurn6cI3gCjhF-BV_HNofy9gNhhmIz4DW-iB00pI4TSWAn3awu_zHsCG8EDO43ocKtROSon_Quj7NxBZGIoaL8Nb8UYEd6CzOIFor1GZOEmO-G2siS8fYmC-t0sYRuapEFkSfIbFzLJo6j20TlMakSltxuFsEWcmmzmtGxY1E5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d8b0f815b.mp4?token=h-68XiZGBuD79ApdVsKrseF7VJUFd95wyD5dRa9RoiyaoKxWR9pASJ2pCHlh81BjPJUSNgE7X41CtqZg_qIGPIgJ3_TfzGoLiDvnb3GW2uTSJOtmJ-MBO0W_L_iCmhx07aN948kNDB_v3jYQboJI2gzSkOXqQEy4WiE2k4EdCcFGurn6cI3gCjhF-BV_HNofy9gNhhmIz4DW-iB00pI4TSWAn3awu_zHsCG8EDO43ocKtROSon_Quj7NxBZGIoaL8Nb8UYEd6CzOIFor1GZOEmO-G2siS8fYmC-t0sYRuapEFkSfIbFzLJo6j20TlMakSltxuFsEWcmmzmtGxY1E5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
جاویدنام زهره خاکسار ، دخترش که بر مزار مادرش میرقصد
🤔
برای ما مردم دیگر فقط مسئلهٔ اقتصاد و سیاست نیست؛ یک حساب تسویه نشدهٔ عمیق با حرام زاده های عرزشی است که تا ابد در ذهنمان مانده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/123985" target="_blank">📅 18:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123984">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
خبرگزاری CBS: تغییراتی که ترامپ در متن تفاهم نامه داده جزئی نیست و قابل توجه است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/123984" target="_blank">📅 18:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123983">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
خبرنگار الجزیره: دو حمله هوایی اسرائیل به شهرهای کفرسیر و شوکین در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/123983" target="_blank">📅 18:43 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123982">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
گروسی: حملات به تأسیسات هسته‌ای غیرقابل قبول است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/123982" target="_blank">📅 18:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123981">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
سی ان ان: ایران ۷۰ درصد سایت‌های موشکی خود که بمباران شده بود را باز کرد
🔴
ترامپ نگرانی خود را از میزان سود مالی که ممکن است ایران در چارچوب توافق به دست آورد، ابراز کرد
🔴
ترامپ بر عبارت‌های سختگیرانه‌تری در مورد تعهدات هسته‌ای ایران و وعده‌هایش برای بازگشایی تنگه هرمز اصرار دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/123981" target="_blank">📅 18:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123980">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qB6R4pvqxEtwQNEp8yh5TjFd22debPqug1vidrkNAJ7SK2kf9u6Ma0oudLw54fFidiRJAefPOKN6OLKZNClfgGzrPks0qGvkKkr_M6qhQcoIy53za89THDfoYdFXkVCHQpIt2ko5EHnSNXvpsx0C4RnCKvM0dR9RTsYP6jZl8ZnulSqRPXK25CX5SwF-gwsSwPLcl4ijlJlh_Vv32dpkb_4KqExOlfEtyI4ilxB4eJ3rdg9y8xDg1yUdEPCdQ8op3j653SI-mIQs4cbusDo1aSfWrdmJyDDyhb0HqWrP3JS1Fdit85qQkJrnXknuWJ5Ddl8uuSt-6ZqkSbiZmAc4Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جدیدترین کمپین در خبرگزاری فارس با عنوان قطع داوطلبانه نت بین الملل!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/123980" target="_blank">📅 18:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123979">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
سی‌بی‌اس نیوز به نقل از یک منبع:
در حال حاضر هیچ ضرب‌الاجل یا چارچوب زمانی مشخصی برای دستیابی به توافق در مورد ایران وجود ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/123979" target="_blank">📅 18:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123978">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
پزشکیان: خدمات‌رسانی دولت در هر شرایطی ادامه خواهد داشت
🔴
دولت با تمام توان و ظرفیت خود مسیر خدمت به مردم را ادامه خواهد داد و ادارۀ امور کشور با قدرت و صلابت دنبال خواهد شد.
🔴
بخشی از مشکلات اقتصادی کشور ناشی از محدودیت‌های بیرونی و بخشی نیز ناشی از فشارهایی است که در نتیجه شرایط خاص کشور ایجاد شده است.
🔴
دولت و تمامی دستگاه‌های اجرایی با تمام توان در تلاش هستند تا کشور با کمترین هزینه و آسیب از این شرایط عبور کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/alonews/123978" target="_blank">📅 18:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123977">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fb7188e1b.mp4?token=ZI6l2QV9p5sO9IwHUGoeonXAe6t1pGa2hTupPEk1W1q5_ST10m4U_S3nhehAAoxvnM6KoCIc2cNUOSgtdNY706Pu38iUifyRo7g3dYogb_Ii6p1skjQKBvNyOEBiJBRSIi57NMlHNPy1G_ugyuugGpgHia0LEEjKIRWI-X0qy6_z_gysk21A-nccN7RVTPKMoN-dFv9bUR6E1DV9xQ49dpQ30leP_ml6M30QFd1Okzdm0NMqxsYk2ezVFLMDkbKCIclaqcrvvM57zxgs2G67-AvjEl8rZjbuK5ynBjafcjJB8gyoiMCGclp1RKMP5enun_H4UJjSD5H6tOyeMAsHxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fb7188e1b.mp4?token=ZI6l2QV9p5sO9IwHUGoeonXAe6t1pGa2hTupPEk1W1q5_ST10m4U_S3nhehAAoxvnM6KoCIc2cNUOSgtdNY706Pu38iUifyRo7g3dYogb_Ii6p1skjQKBvNyOEBiJBRSIi57NMlHNPy1G_ugyuugGpgHia0LEEjKIRWI-X0qy6_z_gysk21A-nccN7RVTPKMoN-dFv9bUR6E1DV9xQ49dpQ30leP_ml6M30QFd1Okzdm0NMqxsYk2ezVFLMDkbKCIclaqcrvvM57zxgs2G67-AvjEl8rZjbuK5ynBjafcjJB8gyoiMCGclp1RKMP5enun_H4UJjSD5H6tOyeMAsHxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خزانه‌داری ایالات متحده اسکات بسنت درباره ایران
:
اطمینان از باز بودن تنگه هرمز، دریافت اورانیوم بسیار غنی‌شده، و اینکه ایران سلاح هسته‌ای نداشته باشد — این پایان دادن به کار است.
🔴
این اولین بار است که ایرانی‌ها در ۴۷ سال گذشته حاضر به بحث درباره نداشتن سلاح هسته‌ای شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/123977" target="_blank">📅 18:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123976">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfAr7SamgXRogVOiVLpTFFofYY0LUNvRlDma-ENPHtZTzi5mtgfxTzi0aHqjt8jx70BvLgui81-IJRBXgR4Cop0phyhqUE7VOxUUY1Qg0sMYBh6VHoTytnEylzin190LahUUp4bRdEuXpov8oP-PhLxsvkKMoxO4tpA5Ha4nKfLlRLSdlwo_sZ-gXZ2Yczk50onNX3TRVgqchhEkj3FQjDvvRL7udNVm_y9KR6ouF70azFMvoxG6LFOqUMpvpfHFcyWbNzhooh0x62yplHf7JuV_Te7Md-EKa7lnPR-hAntCb235mEgpG94jbOk55ZWpx4q156Bw-pNAX542S4G8Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/123976" target="_blank">📅 18:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123975">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
منابع خبری مدعی حمله موشکی به حزب ضد «پاک» در کردستان عراق شدند.
🔴
یک مقام حزب آزادی کردستان به روداو گفت که روز یکشنبه  پایگاه مهم وابسته به این گروه مخالف ایران نزدیک اربیل هدف حمله موشکی قرار گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/123975" target="_blank">📅 18:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123974">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
شبکه LBCI لبنان: روبیو دو روز دیگر آتش‌بس فراگیر در لبنان را اعلام می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/alonews/123974" target="_blank">📅 17:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123973">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKn-btqaWKdqEikU3thr0HW6v6Pme1o_WLqfIP5TGiHba2W8sNLrsQmLyDxKwZMb9-jKLNuzOxvJP1Gqyj0JXSolXGdaD-qwQM9tbN0HHAzjYcGOOBNk6yNk6BGgxdgJDuXmdkV3EEfLRWve5QIykP79pKCxkPEJszRPtdF4wL7GLWhOuEplLpXv1uxLCMa1n04HBDWRNUv3lzWiNTby4T4FSxLU9bAFcQSMNbSzJA2nGSpbKaipJB7zzhHxOwlX0OvIVBZJRO2ftkIITrrXACusTJHjCvgS6sojnaIv9HJTh6SbM6K7agPgkZ1VNx8Ixf1N72ZQ5vHtDxJnm5VbIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: با کمال خرسندی اعلام می‌کنم که تام باراک، سفیر ایالات متحده در ترکیه، که عملکرد فوق‌العاده‌ای داشته است، به عنوان فرستاده ویژه ریاست جمهوری در سوریه و عراق منصوب خواهد شد، و ما همکاری استراتژیک خود را با هر دو دولت پیش خواهیم برد.
🔴
تام با حمایت کامل وزارت امور خارجه، سفیر ایالات متحده در ترکیه باقی خواهد ماند.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/alonews/123973" target="_blank">📅 17:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123972">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
حزب‌الله با پهپاد FPV مستقیم به کابین یه خودروی امدادی اسرائیلی حمله کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/123972" target="_blank">📅 17:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123971">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
سی‌بی‌اس: میانجی‌ها به مذاکرات توافق تهران-واشنگتن ادامه می‌دهند؛ ترامپ متن توافق را جمعه بازبینی کرد و آن را برای تأیید به ایران فرستاد، پاسخ هنوز در انتظار است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/123971" target="_blank">📅 17:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123970">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
رویترز: جمع‌آوری سلاح توسط اهالی گرینلند از ترس حمله احتمالی آمریکا
🔴
برخی از اهالی گرینلند به رویترز گفته‌اند که برای مقابله با حمله احتمالی ایالات متحده، اقدام به جمع‌آوری اسلحه و مهمات کرده‌اند. یکی از مدیران معدن با یادآوری اینکه پسرش گفته بود برای آمادگی در برابر تهاجم قصد خرید مهمات دارد، به گریه افتاد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/123970" target="_blank">📅 17:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123969">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
وزارت جنگ آمریکا قصد دارد در ماه ژوئن، برنامه‌های مشخصی برای خروج بخشی از نیروهای خود از اروپا را در بروکسل، مقر ناتو ارائه دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/123969" target="_blank">📅 17:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123967">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QP44qMdNLu4h6_EmfopM-fcJ5jR8xnY4dOQxzTMwaKeHKFua6HYeJgS6c-niO1Ay4yiORo7O4WDch3aQwBr9008sFaWKgWU3uEamlYG_sxjkvMTE_zxs901v4m0NImPRBvd0DDKgcqsgiz3g-VgP9yasxWpP19OwE90WkKPouM2ZORUb3NJTGU28xD6A6snC4VVSbBeK4miN_Cd9uNEYhC_vBOCX4FwrL6EX6B8Gm2agwnyS8GUT6IE5pO5ZWu5DfBeFLrexjGr2unJumz4RNWHu89uHwAD8dBnOIDn6PoFKS03b6-s3D2nhqYI2tY_viqmoMm6uh-aBh9VFS5O8Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HEdz2kOhwN9ROEVYGv7ePrbwJsSoXBq-BM_ITQea9x7YvqZvkRg3xKaA7Cnd0JvL9A-toQkcWIZmWuEpC5m5GFvSW-N-Fvrjr9zikKuQAqQXTk3zLJa7Fcvnml2bsiZ4bi7WVmZD3p460Kwa1ik4paziJEE2K98MQE3f57WmOiO08SCFl0SstN0QOzOtim5fRDOiCT-cBCqhRREBe-uygKEs8BqiqqHhy5aykUhOtYSYUi95IjC40OgqOFSZJ_bopJB1l44ors5a2KWldFvV98EF_8LSac97FYEXjPLlHXvWgNKZ2QQFNAQhIo7uguT_t4cmnt8ImnwiNraLLgSkmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک راکت حزب‌الله بین منازل مسکونی در روستای مسیحی نشین رمیچ جنوب لبنان سقوط کرد. که تلفات جانی نداشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/123967" target="_blank">📅 17:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123966">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
مدیر عامل پارس جنوبی: بازگشت سه سکوی فراساحلی میدان مشترک پارس جنوبی به مدار تولید
🔴
مدیرعامل شرکت نفت و گاز پارس از بازگشت سه سکوی فراساحلی میدان مشترک پارس جنوبی به مدار تولید پس از جنگ‌ تحمیلی سوم خبر داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/123966" target="_blank">📅 17:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123965">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0fze-9JaTTMZFaQLvP7n2mnKfTiDf9qIrlXqrwtfBsoao0t-IyzVOj6Y9O_UnGOPiJvBSdj-J0r8908gA6_0YAu5VSZoCUSsYzjPkHSOIp5FpL2cx83xycfc_NDJmc0ipYYguDsy04G78IDDTiiCkVU9h8WAhP9pHu9f165aqpo_jUDUxc37YvHioKQr_F1J3AXJWS0HHeDl71TAmRRZLH8TD0WR22UWjK-jlfJWE4euSUklArJthugTPc8Hsk_9untX-MQW3rpMSIXhQ4opLcv3GZJEyrDmvon1YOTSsBSHdqPZ5RsR_O3MIO29Dqk3GBUIC8ut-LERCD_TDlEyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جروزالم پست: درخواست فرانسه برای نشست اضطراری شورای امنیت درباره لبنان
🔴
ژان نوئل بارو، وزیر امور خارجه فرانسه، اعلام کرد که در واکنش به عملیات نظامی جاری اسرائیل در لبنان، خواستار تشکیل جلسه اضطراری شورای امنیت سازمان ملل متحد شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/123965" target="_blank">📅 16:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123964">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
قائم مقام معاونت راهبردی رئیس جمهور: تراکنش مالی وابسته به تنگه هرمز حدود ۲۰۰۰ میلیارد دلار در سال است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/123964" target="_blank">📅 16:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123958">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bab239b5e.mp4?token=bCsCjUxRXf1rTGMqXiUIVA0x8e3tcVJIZtrXB8SmJCjVymTdV0PiV3c2xysDuXzG64G_q7eeM9nQ992yTnRb3QjPw-0sQnForjQhJvJLGht5nMqymhAa-Hqp-EML3_DBtAaUhVFru6BIbz86zAHi-Xli3WMfX7XkIQJppi7JZFTVPY1RfyQBrVCqs3BW1d1voIwITp6IOnOxkI52QJ4jtxPB0cZZxix-zUy8jrfV9UFcCtHi3CB0ZNwzkMnPqZCyavTGUKXz8GBKZxRH4dzBeJbGW5bX5sc9nro4NTZ6IvgbtEGqF69-5pwowjj0ncFXkSC7LVJv3OnmIAahQsviaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bab239b5e.mp4?token=bCsCjUxRXf1rTGMqXiUIVA0x8e3tcVJIZtrXB8SmJCjVymTdV0PiV3c2xysDuXzG64G_q7eeM9nQ992yTnRb3QjPw-0sQnForjQhJvJLGht5nMqymhAa-Hqp-EML3_DBtAaUhVFru6BIbz86zAHi-Xli3WMfX7XkIQJppi7JZFTVPY1RfyQBrVCqs3BW1d1voIwITp6IOnOxkI52QJ4jtxPB0cZZxix-zUy8jrfV9UFcCtHi3CB0ZNwzkMnPqZCyavTGUKXz8GBKZxRH4dzBeJbGW5bX5sc9nro4NTZ6IvgbtEGqF69-5pwowjj0ncFXkSC7LVJv3OnmIAahQsviaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی امروز به طور مداوم حملات هوایی شدیدی را بر شهر صور در جنوب لبنان انجام داده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/123958" target="_blank">📅 16:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123957">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
وال استریت ژورنال: سازمان ملل در حال ورشکستگی است، زیرا ایالات متحده و چین میلیاردها دلار را از این نهاد بین‌المللی خارج می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/123957" target="_blank">📅 16:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123956">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
عضو هیئت‌مدیره انجمن داروسازان :
کمبود کدئین به خاطر تحریم نیست، به خاطر محدود شدن تأمین تریاکه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/123956" target="_blank">📅 16:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123955">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
الجزیره: پرونده لبنان در صدر تعاملات مربوط به توافق بین تهران و واشنگتن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/alonews/123955" target="_blank">📅 16:28 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123954">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
سی‌ان‌ان: اگر خصومت‌ها از سر گرفته شوند، ایران در موقعیتی است که می‌تواند تا زمانی که پرتابگرها و خدمه داشته باشد، حتی اگر تولید متوقف شده باشد، به پرتاب موشک ادامه دهد
🔴
هیچ چیز مانع از مسلح شدن پرتابگرها به ذخایر فراوان موشکی که ایرانی‌ها هنوز در اختیار دارند، نمی‌شود
🔴
برای آسیب به تاسیسات موشکی ایران از سلاح‌های بسیار پیچیده و بسیار گران‌قیمت استفاده می‌شود، اما عملیات بازیابی با فناوری بسیار ساده‌ای انجام می‌شود: بولدوزر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/123954" target="_blank">📅 16:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123950">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K6fr-g-MJ6j_jH5IaSv3i_Q6ygxXME0Jy9CD-UfZ_Hjh56ROQ91glbTOqnhMgdUFjjMwIvsht6PvkiloMS_0_aUK80r86yEz9KvbY5ZHmJhlRJwrhBiiu1eVzqO2b0OTr4Tb0VBb00EaXB520bYLToU9inLP9clkbmRqxIFqqEqy8MukhoK14MHz5nv1_pXcEHQTnQPjsl2Vmm9UwX10TT0OSCJ80FiSx7PdxP2zeJLNz_spG-lfmN7rJndgwrrwR9KEQJuXLyxA7Wo5phYDMyAin9mwZftn9eYYssXZpu_vqvFvhDuSXUu9RNW-ZVRuurFYDLzsqlSeC8ZmstHixw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DK4IFBufc5BWsXubAYJo30eMnEtfneLPYtk6qhNbBPFVmQIbHCPQhxqmQLOSFzPGfwh57EJQsqTGFxwv3Q4OJ8dHyqaCKYsxZmK_2sZY3SinixC1S9waYWIKe1CoqDIQwvQ77LGoUH0-vKSNZyPoSoOdzGidQkWcblBgaAWxGLN4MhoAHw6v_Ld3rUbYdNguOkmMeS2wfg80Oq7MS1JYoqvz2bJA-TRv7HZ5Bm66v2UQCUjwToLyT_09iND8Bdp_naOMUdCsKuBFd9x6W7Qm_dSEZyUy8Z1CL8Z1m1Agrtzt3GbPpeA7VES2kEEpfI8veKzjSY2_Z6EVHHAFtW6unA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=bmRsOpV45ZfLJEfgbKtgJtFqooqbwOCOejb7lpmOQtI2AKlSs2rrTzF0iiDvOXjzMOBd8ejT2aD8iU7Rr2RxQLFGRJS1Y5bJrQ7BOhMPnvPsCNbCVnx1g9hbPQZdMhNgOvMLqp708vQHBjvMTjzebSA61ky6Ijk3gQrVhVn660Bc7F_9OJt0-YyZ82StwqNkUG4dg7vyAXzv7512rl1ko65sBVNxMoO8Y7OIrLd-dStb-JxHFbVL_3pZQPRA-K_pyazp0gNYX8X0t3ezKpO6uCJoFzgoe0nV2t_A_2Pkx_kmJwfEOnHc-VMlmaqfp7FmgkPWbrimz975GKPaKFhHJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=bmRsOpV45ZfLJEfgbKtgJtFqooqbwOCOejb7lpmOQtI2AKlSs2rrTzF0iiDvOXjzMOBd8ejT2aD8iU7Rr2RxQLFGRJS1Y5bJrQ7BOhMPnvPsCNbCVnx1g9hbPQZdMhNgOvMLqp708vQHBjvMTjzebSA61ky6Ijk3gQrVhVn660Bc7F_9OJt0-YyZ82StwqNkUG4dg7vyAXzv7512rl1ko65sBVNxMoO8Y7OIrLd-dStb-JxHFbVL_3pZQPRA-K_pyazp0gNYX8X0t3ezKpO6uCJoFzgoe0nV2t_A_2Pkx_kmJwfEOnHc-VMlmaqfp7FmgkPWbrimz975GKPaKFhHJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویرانیِ.های گسترده؛ جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/123950" target="_blank">📅 16:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123949">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
روزنامه کیهان: به دلیل نقض آتش‌بس در لبنان، میتونیم جنگ علیه اسرائیل رو آغاز کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/123949" target="_blank">📅 16:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123948">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
صادرات تخم‌مرغ آزاد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123948" target="_blank">📅 16:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123947">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMl_9AaFryN_Crg6psE8uATV2jVxha9kCXEAGVsk-Dk03STfGek6X7gdnC5eMWQF_ZGtfWoyABrqAd80fKVlcxRHIxhoetDu1sxuEJeNJC4pyesJ3mPr37d3o3nB140O2m1qUMMOGxrgDgZsf98BmrMPQaKH9rtMee3G2DcdeIY9Cu6_ZwLEVHSOJWgaa_lrrTS9qpGTi-UfNyJwxwytg6jI87gQkM90jIcigmpdqDOCpx14WeoKtwjvwxXcnr9Use9NG3EWM66rqiu0IINxd7g64wYR2yZpMfVEMfHUIszchE9Wt77W3x4ScSIsTaPkrYYIn70a_6Q8PFEseYi_fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دقایقی پیش سامانه پدافند هوایی در کریات یام بدون به صدا درآمدن آژیر فعال شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123947" target="_blank">📅 16:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123946">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
سی‌ن‌ان: ایران ۵۰ ورودی از ۶۹ ورودی تونل‌های تاسیسات هدف قرارگرفته موشکی را باز کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/123946" target="_blank">📅 16:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123945">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvLC5NHGV792QR3ZV5wJ_8n2fdvAMkODd4RiXxSct43M6e85gX7K2MhJlaGT92s4_JRLPfbJW1dw-hqC-4llFkSMnyCbsDZmvZvoTAW0QJ8h3A_lu1hicx9rrwv0qPjOi1ZzkbZ60zyt8rn23CneHaF-CvtSzVzh9rbPwse_4etxyULFZZOHDqNlAdWIRp2YyocCI4aMb0Qy3RrdMwMlWI8bltSseufk6E3ZVS0RXEwaqwt5P3P0zW--JgLDFn3gldZKqrQhZyTZRARkCJcJqd1H7cUs3ogGp537KNf_jAsEyQg1x234i4lQObxVuWEPkX9CaCm04yj4DhyqefNtQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش به گزارش امنیتی دانمارک؛ سفارت ایران خواستار ارائه شواهد درباره اتهامات شد
🔴
سفارت جمهوری اسلامی ایران در کپنهاگ به ارزیابی اخیر «سازمان اطلاعات و امنیت دانمارک» (PET) که در آن از افزایش نقش ایران در تهدیدات «تروریستی» در داخل خاک دانمارک سخن گفته شده بود، واکنش نشان داد و این اتهامات را فاقد شواهد «مستند و غیرقابل‌انکار» خواند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/123945" target="_blank">📅 16:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123944">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
سد کرج پس از بارش‌های اخیر جان گرفت و مخزن آن به ۷۰ درصد ظرفیت رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/123944" target="_blank">📅 15:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123943">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t74sZa2CaPjod89B1bE2-ykKXOLriVN8FUGwAkZGJPzbmx5k2WmvrvBXBhuvl8za_p7jLHwIxyRBfToIXLxuV9QJ3ufixfzB2UX5PsibmENJBZnY5hnz1RLIguHrE_xw2GvKjj3TjnZDPF_tLxwDupVpwMWoJ9dXdLU1BODQytrrgqXzFEbmmiW5DrwIH_Nnbn0yHoZ1VP8DeboNUIjMR-DRAfziCS6y1z1LK9AFSO9nf4zRLG4U-XHhG9FHOliCaiFwqf-j083_xeNgMa5JBmcxK4VfR_p09WWAdvbYPiyJ33ZnfaLNtsWL7e-WePSYPriJR5agMhrUllTl09etRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پخش برنامه «به من چه» که از روبیکا منتشر و اجرای آن را مجید واشقانی برعهده داشت، به دستور سازمان تنظیم مقررات رسانه‌های صوت و تصویر فراگیر در فضای مجازی متوقف شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/123943" target="_blank">📅 15:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123942">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
وزارت بهداشت لبنان اعلام کرد از دوم مارس تاکنون در جریان درگیری‌های جاری بین اسرائیل و حزب‌الله، ۳۳۷۱ کشته و ۱۰۱۲۹ زخمی گزارش شده اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/123942" target="_blank">📅 15:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123941">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
نیویورک‌تایمز: ترامپ شرایط سخت‌تری را برای چارچوب صلح به ایران ارسال کرده است
🔴
نیویورک تایمز به نقل از سه مقام آگاه:
رئیس‌جمهور آمریکا عناصری از پیش‌نویس توافق را اصلاح کرده و آن را برای بررسی به تهران بازگردانده است.
🔴
این گزارش به تغییرات دقیق اعمال شده در متن اشاره‌ای نکرده است.
🔴
ترامپ نگران بخش‌هایی از توافق احتمالی است که شامل آزادسازی دارایی‌های مسدود شده برای ایرانیان می‌شود.
🔴
ترامپ از مدت زمانی که طول کشیده تا ایران به پیشنهادات واشنگتن پاسخ دهد، ناامید شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/alonews/123941" target="_blank">📅 15:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123940">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac3936dc2b.mp4?token=ZzOHs8a5CIZqKFiar6-t5HTaLwK6CBc6E4DpqV3EV8i-ioTCOqpJb8Jq-JjDZ92M5ksL9zJxy76buIci0MVLbALqD7QW89S7-s3mjKY8-ackiP7hNoRrqy7ogt5RM0hUzFYetAjCqnw45WqX6DrqKkS-Iho9NlvAhfelFxBlb0kGQVcPcF2BP7rUqE0I-bDARkr6qgN3Cx0WE95c6IuVWE2v7mAOJJv7d4_jlWf2pD4t3FpUytZYCOLRJGQe9NUISgyO6XM6K2elX5378LSkfI7fh5gBiGjvxmgp1OqtUVUpXc3XRlgk8aX8BDakHzQ_-gfY2n7nzIsC_WdrWhLgcXOSUxRujuFDNBSg3nebfn41QA1HSzC-Z11X8Hbjnx7ZZp_605OHssjRjJy3dKyxudRVWDy62pYsC55SR2CG3Rgm4_ukW5OjCNaGbgH-8_XUhuDT-PmPB43-J0YGqORyBV70Woudr8avYbIGatcswY2PJKMtchpfaIc6WJRGHoM6dL0qXXx8a_XD7vPjqbNcUVL0FpXtrxs2r4FIPDyidB9ujGw7SVLXs-V0xNYaKH_fDyrWL8WkP7I4p-nrtk7cARpES8IfKqvRVvOXh0svIrFeJQWUWmKCaVOV8UxoGVxf2Zh1UHiePdKm_Y2-steSdXnanVWbgIlg4YO5ED2yIFo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac3936dc2b.mp4?token=ZzOHs8a5CIZqKFiar6-t5HTaLwK6CBc6E4DpqV3EV8i-ioTCOqpJb8Jq-JjDZ92M5ksL9zJxy76buIci0MVLbALqD7QW89S7-s3mjKY8-ackiP7hNoRrqy7ogt5RM0hUzFYetAjCqnw45WqX6DrqKkS-Iho9NlvAhfelFxBlb0kGQVcPcF2BP7rUqE0I-bDARkr6qgN3Cx0WE95c6IuVWE2v7mAOJJv7d4_jlWf2pD4t3FpUytZYCOLRJGQe9NUISgyO6XM6K2elX5378LSkfI7fh5gBiGjvxmgp1OqtUVUpXc3XRlgk8aX8BDakHzQ_-gfY2n7nzIsC_WdrWhLgcXOSUxRujuFDNBSg3nebfn41QA1HSzC-Z11X8Hbjnx7ZZp_605OHssjRjJy3dKyxudRVWDy62pYsC55SR2CG3Rgm4_ukW5OjCNaGbgH-8_XUhuDT-PmPB43-J0YGqORyBV70Woudr8avYbIGatcswY2PJKMtchpfaIc6WJRGHoM6dL0qXXx8a_XD7vPjqbNcUVL0FpXtrxs2r4FIPDyidB9ujGw7SVLXs-V0xNYaKH_fDyrWL8WkP7I4p-nrtk7cARpES8IfKqvRVvOXh0svIrFeJQWUWmKCaVOV8UxoGVxf2Zh1UHiePdKm_Y2-steSdXnanVWbgIlg4YO5ED2yIFo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرار سخنگوی دولت از پاسخ به سوالی درباره ستاد غیرقانونی فضای مجازی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/123940" target="_blank">📅 15:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123939">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7e984d08a.mp4?token=LW-BmO9kBVgrrWQhEWU2xNLrTs-fR1eUqVDxWmh6Z852UvRV3NPaSPSLcRMRtNk_b71NoOjKS0H2OcaxA0x9aUMH5tAr7JoTBcsKRxPmX2LIbJLOV6e_7RjO2O_cbPOqiCQ3crzUYSLH2U81TH3UOOwKi1qJBVUdzTkX_sTiO1imUQcNi2VauRNR6glnfpqsOC-Of91vodbovbv2PAoUz0pP_k2uOEQuDf9N0LQVnjUUWyOAa81lItyKLCZKA8LaRsQvnM71SQq77ujjUo3VfdZTu-FnRhqhTxvqN3a8tpivXI_GDoHWGDXhqguZZu5M5fqixbpZeJwO7D5zcyrxbIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7e984d08a.mp4?token=LW-BmO9kBVgrrWQhEWU2xNLrTs-fR1eUqVDxWmh6Z852UvRV3NPaSPSLcRMRtNk_b71NoOjKS0H2OcaxA0x9aUMH5tAr7JoTBcsKRxPmX2LIbJLOV6e_7RjO2O_cbPOqiCQ3crzUYSLH2U81TH3UOOwKi1qJBVUdzTkX_sTiO1imUQcNi2VauRNR6glnfpqsOC-Of91vodbovbv2PAoUz0pP_k2uOEQuDf9N0LQVnjUUWyOAa81lItyKLCZKA8LaRsQvnM71SQq77ujjUo3VfdZTu-FnRhqhTxvqN3a8tpivXI_GDoHWGDXhqguZZu5M5fqixbpZeJwO7D5zcyrxbIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
جاویدنام مهرداد مشتاقی «چه جوان خوشتیپی، چه رقصی، من که دیدمش یاد آلن دلون افتادم» یاد و نامت جاوید قهرمان.
🤔
عرزشی حرام زاده ، مهرداد مشتاقی تروریست بود؟ دینی که پرستش میکنین دروغگو بودن از واجبات شماست؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/123939" target="_blank">📅 15:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123938">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ناتو: ممکن است در موضوع بازگشایی تنگه هرمز مداخله کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/123938" target="_blank">📅 15:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123937">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
سی‌ان‌ان: ایران ۵۰ ورودی از ۶۹ ورودی تونل‌های تاسیسات هدف قرارگرفته موشکی را باز کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/alonews/123937" target="_blank">📅 15:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123936">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5g1lfR0Fd9NxlM6NjonioTeqsKb8IU0mIayPsP7uNfm6CwT93M_a1r2M1czdczmMioiH8gS0Wn-h7G9cUAegFFsk8RzmSlJJIjqOSjgpB5vG_IwH0dEHF9LJftLs2Q-4pEQDeqDBTxmhy3hJZPcwCh1ZrWiPljeYwRtgMMiRICoI5vwy5Ozp5wOn2Ndx_2eUHZv9eI0nSXiQHwXKgaaBaM4EM8RAUpTjei4yxwBtmjDnKlXBpZcsUdIXuk0J4rxIGTVLTiBN-ZgCDn2elrpB8ozxBQ7V9-4G0ZgGDBFKg9v9msKKBYaKxMNXnlclIMSJAlpP6QN7nkXrHQhWzrroQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فارن افرز: نقطه بی‌بازگشت ژاپن؛ بحث در توکیو بر سر سرعت تقویت امنیت ملی است
🔴
دایسوکه کاوایی در مقاله‌ای اشاره می‌کند که در میان اکثر سیاستمداران توکیو، دیگر بحث بر سر اینکه آیا ژاپن باید امنیت خود را تقویت کند یا خیر وجود ندارد؛ بلکه مسئله اصلی اکنون تمرکز بر روی این است که این اقدام با چه سرعتی باید عملی شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123936" target="_blank">📅 15:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123935">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odVkNHWvQBGOEfVcGghpveTCqqZ2kHb33gQtizeAKozkch7RiaFheobZt1k7hZrIKT_6qD4sLEBSb4vhOLMhD3ixuuTfdVsFCon1KcePZS_L_Gl-XtbmG1rZL9zroM_gKI69aJsVK0MlzGwK1VGs5NPdOiLRdFujyeykHQ7R2n5-MjCqeRY7jTX0u9Fo6W5joucu0m0X38s16YSPqvoI6r-Spzy3oUAqb1Ufa605m53_ToSSEAuJIv7GZGfN2HWuL3_85FJgjDSoCMyr_NuWjmW1W1BAsUESuOGfj3-I5Y2K7uyCXnGey87tjj_iTn7hLf_HrPlyh7i3rQyXZ9o-ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال: مشکل این است که آنها با انجام اجتناب‌ناپذیر - طفره رفتن و کم‌اهمیت جلوه دادن تعهدات هسته‌ای - به پیشرفت در تفاهم‌نامه رسیده‌اند.
🔴
بنابراین اگر رئیس جمهور آمریکا تعهدات هسته‌ای قوی‌تری می‌خواهد، ممکن است خود را بدون توافق تفاهم‌نامه بیابد.تبصره ۲۲
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/123935" target="_blank">📅 15:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123934">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
فاکس‌نیوز درباره آخرین وضعیت مذاکرات ایران و آمریکا
🔴
فاکس‌نیوز مدعی شد بنابر گزارشات جدید، ترامپ شرایط توافق با ایران راخ سخت‌تر کرده و شروط جدیدی در موضوعات هسته‌ای و تنگه هرمز اضافه کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/123934" target="_blank">📅 15:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123933">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
قتل پدر توسط پسر نوجوان به خاطر بیکاری...
🔴
مشاجره خانوادگی در محله مجیدیه به جنایت انجامید. پسر نوجوان پس از درگیری لفظی بر سر بیکاری و عدم توانایی در پیدا کردن شغل، با چند ضربه چاقو پدر سالخورده خود را به قتل رساند.
🔴
متهم دستگیر شده و به جرم خود اعتراف کرده است. پرونده برای بررسی جزئیات بیشتر در دست تحقیق است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123933" target="_blank">📅 15:28 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123932">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZNe2UrGTdQU7vL_tONntxOkJr9BXvD5Mx27xUQiktQd4MaDmINvrSyFGRBAAfVfOTLQjJ4H-7gM1KOdGGxaT7e1ELtSz_kl8fI20-PlYVAnuNfrwBs8sgOwNpW8_IBbpxBPXmr-QrRazS_ldeuTeX4hJwKVwfYMfjK79Z8WfJbNGvyUEUhtkqhIrU_trRBv-w89-q9LPhqv6ZCA5tGh7xszzq4gQMLxV9FJR_DR_7eIvQ9f4Fxm1JOdnvZeF_X0RKa3C3yvhXxFxWvhNmNZD12W56pQqcN0pFpjWGAJU_nW7z75IPdY-K8z3af_FXkxu4cZnMsx4oM9Cqt1cO63lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ خواستار حسابرسی فیزیکی از ذخایر طلای فورت ناکس شد.
🔴
ایالات متحده گزارش می‌دهد که ۱۴۷.۳ میلیون اونس تروی طلا در فورت ناکس نگهداری می‌کند که ارزش آن بیش از ۵۰۰ میلیارد دلار است.
🔴
با این حال، فورت ناکس بیش از ۷۰ سال است که حسابرسی فیزیکی مستقل نداشته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123932" target="_blank">📅 15:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123931">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجار کنترل شده در یزد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/123931" target="_blank">📅 15:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123930">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
اسرائیل هیوم: ترامپ به دلیل ترس از شکست در انتخابات میان دوره ای جنگ را متوقف کرد و بعد از انتخابات جنگ را ادامه خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/123930" target="_blank">📅 15:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123929">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 9T!
🚀
❌
آفر فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!  @Netaazaadbot @NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15 سرور اختصاصی پرسرعت
✅
اتصال پایدار و بدون قطعی
✅
سرعت بالا…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/alonews/123929" target="_blank">📅 15:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123928">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CBtjfUc9jnUb7-byoLm3EzQbqKU_H-jZzMMt9By49sWIUIH7P4Bnz24Z0VSnFadwvhFDfGUzhcA0Vn9_fQBz6iBlFUJtj5bnydYexs9lWZBL8YeEApO76ahkgmPxy7c66HQd0FQwuGpwrIYgfF7tVbDKYAuMrfkl3put7GF6CDvpYcRpJRUxoUdEE_H_YkrWgNjbHfUqK7XEVN1VB9GzPSCneW2K79a5RhfrQQNQEhJy9sNnkUJjs1efGO1_2Eq81vJbEVTynZSud91QF2MqugnEQZSA0Pvp7GUjEP8kmXpHJBeyw9UUAjA8Ev3cEOgMIztipfmVA5vZEv995rUDfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 9T!
🚀
❌
آفر فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!
@Netaazaadbot
@NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15 سرور اختصاصی پرسرعت
✅
اتصال پایدار و بدون قطعی
✅
سرعت بالا حتی در ساعات شلوغ
@Netaazaadbot
@NetAazaadBot
💎
کیفیتی که بعد از استفاده متوجه تفاوتش میشی!
📩
برای خرید و دریافت سرویس استارت رو بزن
✅</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/alonews/123928" target="_blank">📅 15:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123927">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
ایال زیسر، معاون رئیس دانشگاه تل‌آویو:
اسرائیل در حال ارتکاب «هر اشتباه ممکنی» در لبنان است و به طرز احمقانه‌ای درگیر یک جنگ فرسایشی در جنوب لبنان شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/123927" target="_blank">📅 15:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123924">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec19bfa89f.mp4?token=rWGeQgzw_uJY_L41ctNR-rjD9RCbAsNH24yncLjirrKWz49AsQvIGeho0gj5PjR63Pz-S5Epy_bQ16ak13usDLblx0MZp_rwG9d3IuzwO0nxqeT_GkoqDl4oFtx5NT_80q_gsjUVuUUJmeOTjxv1RL2bcBOXXlYvb4ISWabmI9LmMONsVp4KYTm1wylCTZ0y9tIYMD_hCxCyEQzRC6Pf94ASmJvx-Mr1DESePiYP5cF5wF0lSMF9RJ0JJkuRyqmGcruNQb7J6WXd0D0O_pcavNp5cXPTvjFXNTyrdQjvmqNjZxjPwDlJVyrZNjqWSpwDJpdiol4vFQV_tTf9Nys6Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec19bfa89f.mp4?token=rWGeQgzw_uJY_L41ctNR-rjD9RCbAsNH24yncLjirrKWz49AsQvIGeho0gj5PjR63Pz-S5Epy_bQ16ak13usDLblx0MZp_rwG9d3IuzwO0nxqeT_GkoqDl4oFtx5NT_80q_gsjUVuUUJmeOTjxv1RL2bcBOXXlYvb4ISWabmI9LmMONsVp4KYTm1wylCTZ0y9tIYMD_hCxCyEQzRC6Pf94ASmJvx-Mr1DESePiYP5cF5wF0lSMF9RJ0JJkuRyqmGcruNQb7J6WXd0D0O_pcavNp5cXPTvjFXNTyrdQjvmqNjZxjPwDlJVyrZNjqWSpwDJpdiol4vFQV_tTf9Nys6Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لبنان، صور
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/123924" target="_blank">📅 15:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123923">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
هاآرتص: اسرائیل به جای اذعان به محدودیت‌های قدرت نظامی خود در نوار غزه و لبنان، همچنان به گسترش میدان‌های نبرد در هر دو کشور ادامه می‌دهد و به دنبال دستیابی به اهدافی است که تقریباً دو سال است در رسیدن به آنها شکست خورده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/123923" target="_blank">📅 15:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123922">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
گزارش ها از حملات هوایی  در سراسر جنوب لبنان، بمباران بی وقفه در شهرهای بزرگ جنوب لبنان ادامه دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123922" target="_blank">📅 15:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123921">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ul_qzBvg8eKVPtr7cQvGozrJHoCeBi7F3t9dCrDtWlaAN1Vzr86_ZN7-EbU9HP3gL6_CmgBN9mpUX2w4dSUtdhqEdtCYzA5QYKTWCAUQA4KIDHkmlNRytCaiE29f4n1aphqsW4IOBPm07EyqfrrYkRCTGseFgPzktx4nwII30JHjoZBYduMGjQfUfMrjL0c2Jo4rcDGPBe7nrEWJx35PBpdtRNvsefnJrGNzH5uWhAYqezu1NuLWW3QzxxQcLSqa1d847UkFEj6EBxovznXsxCbJOUfYJboPFtupyCLzGn0eJt1dOXB_ywiE7s4BPPTtQMsCg3_8U7UPw83QmC_rtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دسترسی دیتاسنتر همراه اول به اینترنت برقرار شد
🔴
اولین نشانه بازگشت اینترنت به دیتاسنتر ها  باید منتظر باشیم و وضعیت بقیه دیتاسنتر ها رو هم ببینیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/123921" target="_blank">📅 14:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123920">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
منابع عبری: عملیات در جنوب لبنان بیش از یک سال پیش برنامه‌ریزی شده بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/123920" target="_blank">📅 14:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123919">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
تسنیم: تبادل پیام‌ها میان ایران و آمریکا درباره متن تفاهم‌نامه احتمالی همچنان ادامه دارد و دو طرف به صورت متناوب اصلاحیه‌هایی را مطرح می‌کنند.
🔴
تا این لحظه هیچ تفاهمی نهایی نشده و احتمال منتفی شدن هرگونه تفاهم نیز قاعدتاً وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/123919" target="_blank">📅 14:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123918">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
وزیر خارجه فرانسه: باز کردن تنگه هرمز یک اولویت اصلی است زیرا ما قصد نداریم همچنان بهای جنگی را بپردازیم که جنگ ما نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/123918" target="_blank">📅 14:43 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123917">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jozFS1NSKJ92iO7LEVuBrGHHPMXWWLuxHSi_A3cQOC9qQyUhefOfark6Nkp993xnetLaQL7Yr3-nJA3loLyuGYAQaMIcLAZfqYTaqfe-oV4dvsopA1XwodY0Apl1FjKhdA-2OH69z6Vcx79XYJhQf2SPKsnHSpYG4KdopJJP4hau2bbmIoIkYVGHIpCKItEQAarS7kKg8E1X3CQ1Up0-ZZT7pVGfXNePFj5J7nGPEEI-m0tyjQwgbgG8JY6ppgFy3cLv1_Kw_Ydtbq9EWxSVe8b2O78RC-M8af54U465R50k-3UtCL2Ix9apcxEBEK_1M6erfe275WEBqb94LHRNzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سرباز ارتش دفاعی اسرائیل، گروهبان مایکل تایویکین، ۲۱ ساله، از واحد شناسایی تیپ گیواتی، در حمله پهپاد انفجاری حزب‌الله در جنوب لبنان کشته شد و چهار نفر دیگر به طور سطحی زخمی شدند.
🔴
تایویکین، فرزند تنها، در سال ۲۰۲۰ همراه با مادرش از اوکراین به اسرائیل مهاجرت کرده بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/123917" target="_blank">📅 14:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123916">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m13QyZOMgzD732b7PlS1uH192KPUaD_NOP98fCTxXBUN5Zfm283oUQHbIZhe_dSYaFi_wy71IrEqkyAPDwgEV6yX-Vklpzdyo3imdzTjNwwUFzMNye5PLkkDjjkRaMMsHVW62R5WYygGN_atAwwpDXuTropQ24KkiT1f2Cq-QTshJuaYNkt74wpaZSmh4t1o0Q90sDoIcIc2-B3gxTPrkCEWJkz0wxuuLSvkwzs55hTikakOQJ0GFO6kzLzDCAhnpgALy-31uxVdn6Sc5g9TcqK1RoPZr7kTH75-CL8vnmFAAgWV7VXUPzLcRNj0NxVTPlqnTfNsovi37eLG3r_cnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آرتی: حمله اوکراین به تأسیسات جانبی نیروگاه زاپوروژیه و افزایش ریسک ایمنی
🔴
شبکه آرتی (RT) از حمله جدید اوکراین به محوطه نیروگاه اتمی زاپوروژیه خبر داد که در آن، گاراژ و خودروهای خدماتی این مجموعه هدف قرار گرفتند.
🔴
این حمله تلفات جانی نداشت اما به انهدام ۸ خودرو (۶ اتوبوس و ۲ ون) منجر شد و به گفته این رسانه، خطرات برای عملکرد ایمن و باثبات بزرگترین نیروگاه هسته‌ای اروپا را افزایش داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/123916" target="_blank">📅 14:34 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123915">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">📱
لطفا توییتر الونیوز رو دنبال کنین
🔴
پست های انگلیسی در رابطه با جنایت های حکومت به انگلیسی نوشته شده و افراد مهم منشن و هشتگ های مهم قرار داده شده.
🔴
ریپست کنین. مهمترین کمک این روزها جلوگیری از پروپاگاندا حکومت علیه این قتل عام مردم هستش. خونشون نباید پایمال…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/123915" target="_blank">📅 14:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123914">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
صدای یک انفجار در محدوده شهرستان قشم از سوی چندین منبع محلی گزارش شده است. ساکنان مناطق مرکزی و جنوبی جزیره، وقوع این صوت ناگهانی را تأیید کرده‌اند.
🔴
بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/123914" target="_blank">📅 14:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123913">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
صدای یک انفجار در محدوده شهرستان قشم از سوی چندین منبع محلی گزارش شده است. ساکنان مناطق مرکزی و جنوبی جزیره، وقوع این صوت ناگهانی را تأیید کرده‌اند.
🔴
بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/123913" target="_blank">📅 14:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123912">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
نتانیاهو: به ارتش اسرائیل دستور داده‌ام دامنه عملیات نظامی در لبنان را گسترش دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/123912" target="_blank">📅 14:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123911">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
آکسیوس مدعی شد: یک مقام ارشد در دولت ترامپ اعلام کرد که احتمال دارد تا پایان هفته آینده وضعیت توافق احتمالی میان آمریکا و ایران روشن شود و واشنگتن برای دریافت پاسخ تهران آماده صبر کردن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/123911" target="_blank">📅 14:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123910">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
رادیوی ارتش اسرائیل: حزب‌الله حدود ۱۰ موشک به سمت کریات شمونه، مطله و چندین شهرک در جلیل علیا پرتاب کرد.
🔴
آژیرهای هشدار در طول یک ساعت گذشته به طور مداوم در جلیل علیا به صدا درآمده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/123910" target="_blank">📅 14:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123909">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
حزب‌الله: مناطق زیربنایی ارتش اسرائیل را در منطقه کریوت در شمال شهر حیفا را با موشک بمباران کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/123909" target="_blank">📅 14:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123908">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
قالیباف: سربازان دیپلماسی هیچ اعتمادی به وعده‌های دشمن ندارند؛ ملاک برای ما دستاورد‌های عینی است
🔴
تا اطمینان پیدا نکنیم که حقوق ملت ایران را گرفته‌ایم، هیچ توافقی را تأیید نخواهیم کرد؛ تضمین این راهبرد جان ما است که کف دست گرفته‌ایم
🔴
خود و همکارانم را به پرهیز از اختلافات پوچ سیاسی توصیه می‌کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/123908" target="_blank">📅 14:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123907">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
جبهه داخلی اسرائیل: به صدا درآمدن آژیرهای هشدار در کریات شمونه و حومه آن در جلیل علیا به دنبال پرتاب موشک از لبنان.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/123907" target="_blank">📅 14:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123906">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iP-SY2NNK9c4ojjeUS3FUejB2JUqiG-1RFfgwcuC5N6dWMfqlB12xcq9zZiRisil0gtKqT-nhfnNeQgHLy6XvcmuLV65gBg0H8ni5wAR7W-vAai5p2xtHF-lKDTjH2E4MuN97ZrwkPbCwVf6wlMDTzo_hL2oZgM5Lxeul_ueGXU9ZOibBbcGUY58PvAjmuGAdPMlKxdC2tHwq1KdRR9jA5gYMKMYDUDYxrWuIUTaeEt5JE9Gxhl8i1CbP255CztDmG6GI6IbAxnKRGacBLVrq9xPYp0YRouDOzsS4kPWwlgqYJ33d0NmRaSAjY8dSzFX6bRUmEPSWibZb95nAaWuuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت طلا و سکه امروز‌ ۱۰ خردادماه ۱۴۰۵
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/123906" target="_blank">📅 14:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123905">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-AfNkUX7NuAmG3w4O746DiPhkcOHTm3BkDGgHAbarGgJFCQbvBaLW5sDno1rO4G5ZRgs6RVBUClkuCM9RBZYefgSUMulluARqLvg8Ll2mxmtmsuIPX7Uw1-TM7-Q3EytAfYm_qFK5IOxYI9aSKyPdKBn09BjsKqD0pPQMNnSgc6LY6aI9CcMPNerubO4gIj6PETPIob0-apZW5djKPV0GgkZL1ijYlU3suKof40bU-_eYS91NXcMYjuIDgeEWmGfWkPrFJVYFkYHpp4PSa6hlSQO798riItG5NTzFE2KbNLsHiq604oRprEokChgXIWk1vKhSKUH-CiebeUqMR4VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آشوب و درگیری شبانه در پاریس پس از قهرمانی پاری ‌سن‌ژرمن؛ پلیس ۴۰۰ نفر را بازداشت کرد
🔴
پلیس فرانسه بیش از ۴۰۰ نفر را که در درگیری‌های خشونت‌آمیز پاریس و دیگر شهرهای فرانسه دست داشتند، بازداشت کرد؛ ناآرامی‌هایی که شامگاه شنبه پس از قهرمانی تیم پاری سن‌ژرمن در لیگ قهرمانان اروپا آغاز شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/123905" target="_blank">📅 14:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123904">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21c0898080.mp4?token=NcqQgVlM6u1lUDK0eC93UNPfmJo4B_CRXbjZVXwIXxOBFOQfr6s9EXIC6lppMA4A36maZNAt8kpdISs5M1Wx4ab2oshk2g6PcL6GhEY9EBsnSWl-KBGjqFFePF3GkrxEPe8whTPw4pM18t7WU_MewyYxaF3PO8BYJGBfDgPZZk_KoADsfD1RiLgpAFq3X7-C1RCR7rdStFdXNuxuRZZeAGr0MjlWtPRkhaUEW82mvKKbeYGi4mwxgrSsSDUkOhJBaWj7rifsEA7ikzR7pTO6i-bQOsPQ9oTrrKm0amwZbWWuqMPPnpkmPrzm_4yBfoidkSC6N9y6Z41HP7SfF_bJzJHpQfFmuB4XxbIgQfKVfg1HAGm8hxxfTDnjC44WONeZqL7MyfBPt2orUP8wAKL_2qqZDGHuYQ6ipfMaTzja8XfskThnM-qdpsBfsvpltrd8jMqADUOVEpcgObw4PmR-a0lQTV-aI7IvEPfZGJOek2lJzgX9rhk9aQCKN-PS1jrkWknV4Zh2hZa0wl5OHYZBe7I06VKwstDODz4qCTOQ7Ncin09gKZm0RgF3Zq4np9mWUNMJBhap-QNhuLb6irrvYAWx3W3h231hQ-OaCXH3sCZa5cSEOJhVPHLzyEUGSQmE-s1HuUAcpTuojHgVttMSdKXNAV0jLplRfQszMJnRVWM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21c0898080.mp4?token=NcqQgVlM6u1lUDK0eC93UNPfmJo4B_CRXbjZVXwIXxOBFOQfr6s9EXIC6lppMA4A36maZNAt8kpdISs5M1Wx4ab2oshk2g6PcL6GhEY9EBsnSWl-KBGjqFFePF3GkrxEPe8whTPw4pM18t7WU_MewyYxaF3PO8BYJGBfDgPZZk_KoADsfD1RiLgpAFq3X7-C1RCR7rdStFdXNuxuRZZeAGr0MjlWtPRkhaUEW82mvKKbeYGi4mwxgrSsSDUkOhJBaWj7rifsEA7ikzR7pTO6i-bQOsPQ9oTrrKm0amwZbWWuqMPPnpkmPrzm_4yBfoidkSC6N9y6Z41HP7SfF_bJzJHpQfFmuB4XxbIgQfKVfg1HAGm8hxxfTDnjC44WONeZqL7MyfBPt2orUP8wAKL_2qqZDGHuYQ6ipfMaTzja8XfskThnM-qdpsBfsvpltrd8jMqADUOVEpcgObw4PmR-a0lQTV-aI7IvEPfZGJOek2lJzgX9rhk9aQCKN-PS1jrkWknV4Zh2hZa0wl5OHYZBe7I06VKwstDODz4qCTOQ7Ncin09gKZm0RgF3Zq4np9mWUNMJBhap-QNhuLb6irrvYAWx3W3h231hQ-OaCXH3sCZa5cSEOJhVPHLzyEUGSQmE-s1HuUAcpTuojHgVttMSdKXNAV0jLplRfQszMJnRVWM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بحث چالشی مجری صداوسیما و سخنگوی دولت درباره تشکیل ستاد فضای مجازی و موضوع اینترنت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/123904" target="_blank">📅 14:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123902">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oAiPeIteED0f0_tWeOXYViSz2v60t5TG5kUNOBXLFWYdd42janceK2H4behEr8kNpzZKCr0y1FAe74E88QLemiE9lOjJnT6Cs5DWpCz20kD3OtdxpzRVKnIAnEApxV6JtZpGK66KbMwJGcVlcUbK6_US-U8tgakn-SWz7tyOdBftaVLQk8uRtTbytg4sXzq_5H0mmf-5GITtPugpMZwTC2S5vDc8l4dS5AO8eMUctDAK-uxFeDjgRaAMEnaz4KB1X6gNVlKiG4nUh8G1HsbGQJboR-AMPVcfcZaKyRTwaf8So_YtgL2S1h4qUckABfdAqTxeHHwyzKNj2F4iRyfI5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cm-Vd3STKpKY-hU78IBbF96_BbHhaFmL9BgDDtMtVMtLDcGueP-cMJuoZ-AKkFKTEHmS4zLq54VGqEoECahFFa6qsSgVzryzxgv6Kqvmmu7_nJPyynK6l4-5mscOMLtMOhSbjbQPBdjQCyXpBnnFcPGwaerPi02cw-enGNfICtT2LAEgdAwWt3MvLYsfMqiU5Y9gQf9L_IMM1otKN-2FJiDNVXfAaazNLKyEIpBEe-INoDMbid0pL_5d9tno8BnjL5MQ9mUwncefkykTKH4cwu2h38WgoGEYm68s6mVuGOfQbYAc5wSfauxb2oDLyb8sa3xXz3MzK-_n9ncQauFKIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
تأیید هویت یک دانشجوی کشته‌شده دی‌ماه؛ جاویدنام شهاب خورشید، دانشجوی معماری
🔴
«شهاب خورشید» ۲۲ ساله و دانشجوی رشته معماری، شامگاه ۱۹ دی‌ماه حوالی ساعت ۲۲ در جریان اعتراضات میدان کاج سعادت‌آباد تهران هدف شلیک گلوله نیروهای امنیتی قرار گرفت و در همان محل جان باخت.
🔴
طبق گزارش ها گلوله از ناحیه پشت کتف به او اصابت کرده و همچنین دو گلوله جنگی قلب و ریه‌های او را هدف قرار داده است. بنا بر اطلاعات دریافتی، پیکر شهاب روز بعد در کهریزک به خانواده تحویل داده شد.
🔴
بر اساس روایت‌های منتشرشده، شهاب پیش از پیوستن به تجمعات گفته بود: «یا همه‌چیز عوض می‌شه یا من می‌میرم». او ساکن فاز یک شهرک غرب تهران و اصالتاً اهل اهواز معرفی شده و بنا بر گفته نزدیکان، از بدو تولد با دیابت درگیر بوده و انسولین مصرف می‌کرده است.
🔴
همچنین گزارش‌ها حاکی است پس از کشته‌شدن او، فشارها و محدودیت‌هایی بر خانواده اعمال شده و خانواده اجازه نیافته‌اند برای او مزار جداگانه‌ای در نظر بگیرند. بنا بر همین گزارش‌ها، پیکر شهاب در بهشت زهرا، قطعه ۲۱۱، ردیف ۲۳، شماره ۱۱ به خاک سپرده شده و گفته می‌شود در قبر خانوادگی سه‌طبقه دفن شده است.
🤔
عرزشی های حرام زاده این تروریست بود که بهش شلیک کردین؟ داعش ما ایرانی ها شمایین
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123902" target="_blank">📅 14:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123901">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
نشریه آر‌تی: لوکاشنکو تهدیدات زلنسکی را «حرف‌های بیهوده» خواند؛ توصیف ارتش اوکراین به «گوشت دم توپ»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/123901" target="_blank">📅 13:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123900">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/redJyeRHNMVK2fTirfTLWmfkG7W2_4CF5kqwV8zNbOf2RtsHv-f_V79dGwRkfNBB6OPu3ZRhjLFAM0fV6rS7ocDP1dDLYgZNIlJH6jVhkcca9GJKKS0Dychx1KmFDHBnXtEmp4TZ5uk3XWIsnde8JhNJXk-vPQxPd-LiYfGeCMnfnadMPPQSxbv_jpjLkVTtHXoVnblBsUUGoY9nUEoAVYfvREoZAyS7GVDPLcHLcWemV_5vPj9QwSqlZ_EmJnRTo-YaIj2PVv4rieG1RfBw0J1o9TWK48fKmxa7xnOy00vi4MzV8iOj0H-x04gmam402gKw8k2JOZiycKHEtlEQ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بررسی ۱۸۳۵ اکانت بازنشرکننده توییت‌های قالیباف نشان می‌دهد بزرگ‌ترین گروه این اکانت‌ها در ایالات متحده امریکا قرار دارند؛ پدیده‌ای بسیار قابل‌تأمل، به‌ویژه در شرایطی که برخی جریان‌های سیاسی در غرب تلاش می‌کنند از او چهره‌ای «میانه‌رو» و قابل‌قبول برای مذاکره ارائه دهند.
🔴
نکته مهم دیگر این است که پست‌های قالیباف که تا پیش از ژانویه معمولاً کمتر از ۵۰۰ لایک دریافت می‌کردند، همزمان با قطع اینترنت ایران در ماه‌های مارس تا می، ناگهان با ده‌ها هزار لایک و بازنشر حمایت شدند؛ آماری که با میزان دسترسی و ارتباط کاربران داخل ایران همخوانی ندارد و مجدد احتمال وجود شبکه‌ای سازمان‌یافته برای تقویت مصنوعی این محتوا را مطرح می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/123900" target="_blank">📅 13:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123899">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سخنگوی دولت: فعلا خبری از افزایش مبلغ کالابرگ نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123899" target="_blank">📅 13:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123898">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ویدیویی از برافرایشته شدن پرچم ارتش اسرائیل در قلعه تاریخی و استراتژیک بوفور، لبنان
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/123898" target="_blank">📅 13:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123897">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7db1c2c33c.mp4?token=Qp1y7ekZueiWIyJesOywgvLxnFUF0dGpDDO-OBSxFZWn18S7vOzupqCBLd1uDEW_gwzn1epfmq8z9seOOeM2bzwKwCAVsUIw91UKJ76A1_VfB0S947kjCxq5KcmNQJVOSlVB6UZvkFhZA6LzqWUl-rdTBmtNZ392hrhvWO6yUaKn3unR0WyCYNnaRNpK-oyJjl1jmAbslpo61Fj7-evNXk-wAPjVDMM_1aRgUY4LU6Jeue5rf1s1UWR7fr2dJZTgiJD1oxG_fC7gHvWQm0zZGhgIBUTEc312MxRn6jNtQMM06vTggehztFPUdoRRjHKLs440bDL-YsYfQ4I-MoTiUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7db1c2c33c.mp4?token=Qp1y7ekZueiWIyJesOywgvLxnFUF0dGpDDO-OBSxFZWn18S7vOzupqCBLd1uDEW_gwzn1epfmq8z9seOOeM2bzwKwCAVsUIw91UKJ76A1_VfB0S947kjCxq5KcmNQJVOSlVB6UZvkFhZA6LzqWUl-rdTBmtNZ392hrhvWO6yUaKn3unR0WyCYNnaRNpK-oyJjl1jmAbslpo61Fj7-evNXk-wAPjVDMM_1aRgUY4LU6Jeue5rf1s1UWR7fr2dJZTgiJD1oxG_fC7gHvWQm0zZGhgIBUTEc312MxRn6jNtQMM06vTggehztFPUdoRRjHKLs440bDL-YsYfQ4I-MoTiUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف : دشمن بعد از شکست نظامی، با فشار اقتصادی و جنگ رسانه‌ای دنبال ایجاد تفرقه و وادار کردن ایران به تسلیم شدنه
🔴
اما مردم با اتحاد و ایستادگی نقشه‌هاش رو خنثی کردن
🔴
رمز پیروزی حفظ همین وحدت و انسجامه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/123897" target="_blank">📅 13:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123896">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vF-5GSfwyspdOnvYM9Edpqvjd4sstNv-jEqV5SfXvLUSuOPZcBCBuc1-5S_4JgTa-7W8hI_8g--GU6aAKbhBSnCXYWnhcNO6tsELTM9Qa1RhsuPQFSohSGtk3bcRygltdqhGVgnS-frcY0OUZ_1z6qf8gnbkolWRb-Ij0Nf-aLrX6Swb0qMakEdp6usB4aVph6yyWPrk12cuQNuPpjGn5vn1n6jcKwz7lpwdunra2w_SM2bxv-GPCKejeT9XiEPdoWUxXGqhxACJL-sTi5XREMvUCvLAy6Iu0I-mRjFbyEIJzrbVYv72JurXPpRmvwq4AlbNnTMTtQ_eoDVafC6kvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس با رشد ۸۳ هزار واحدی در پایان معاملات امروز به ۴ میلیون و ۲۳۶ هزار واحد رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/123896" target="_blank">📅 13:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123895">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7328c91388.mp4?token=cE7o_LKWKVyP1SSEpbsN4d_Cmsfx6p8xabZrx6DG9l8VZO0vhYO3y7iV9bBMgm4xltjxDBaGtZTFQ4kjdeXSSadf19MrKOtjuKRdDfSEXCa47PU3yuwsmUpjoke0NNO04d67gpSouMHsHuJE7CiJOJh3r9eKx6c_IG0rIpQVL1kmoyNT6o0I7WChRrPXbXJd3-aV7npD2zrCv7m1OJAWWUJnLj_GIV6rvxptmz2GpEi2I5uV6ZlYkRnPMw6vft1S9zV2LTXvSxTDvMQjHoIee41H-Fdm152sMrA5UW9pSimM8265kzvhaIt3BRtAMtP9vfKUggJbK-1gkjFjbSdzGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7328c91388.mp4?token=cE7o_LKWKVyP1SSEpbsN4d_Cmsfx6p8xabZrx6DG9l8VZO0vhYO3y7iV9bBMgm4xltjxDBaGtZTFQ4kjdeXSSadf19MrKOtjuKRdDfSEXCa47PU3yuwsmUpjoke0NNO04d67gpSouMHsHuJE7CiJOJh3r9eKx6c_IG0rIpQVL1kmoyNT6o0I7WChRrPXbXJd3-aV7npD2zrCv7m1OJAWWUJnLj_GIV6rvxptmz2GpEi2I5uV6ZlYkRnPMw6vft1S9zV2LTXvSxTDvMQjHoIee41H-Fdm152sMrA5UW9pSimM8265kzvhaIt3BRtAMtP9vfKUggJbK-1gkjFjbSdzGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیوِ وایرال شده از ذوق کردن یه پسر بچه، بعد از وصل شدنِ اینترنت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/123895" target="_blank">📅 13:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123894">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
قالیباف: چک سفید امضا به کسی نمی‌دهیم
🔴
رئیس‌مجلس: ما فراموش نمی کنیم که در شرایط کنونی کشور، دولت در میانه‌ میدان مدیریت مسائل و مشکلات ایستاده و نیاز به کمک همه از جمله مجلس دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/123894" target="_blank">📅 13:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123893">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 9T!
🚀
❌
آفر فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!  @Netaazaadbot @NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15 سرور اختصاصی پرسرعت
✅
اتصال پایدار و بدون قطعی
✅
سرعت بالا…</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/alonews/123893" target="_blank">📅 13:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123892">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cQlQMrMP2aQuAIO69A7EnsBDQVG8BGNqzVGdZgCyUCffB6XMKmmgbD7Z-oP0PhE7-I0b0ruDnw5LKwA_nfoJJ4VLjilEWxE6z-LzDR37azpkdWEpc0EyncNchyWJ1GaIGKUq7hdmeQwwCc-AnPSPnYd0HY-JarQ2VfyRfDv7Do0bZyRfA2S04MVcDUaQ7nh5GaWgYA-heEjecnAcinDdX1WQOQOnDxr8QOTS9WA7H6gBMsOjgvNpJKFRCeUVbF942r29P4hAPMqaxKsQsQjDNdrIDjlv-rvz5TnI9MDiaOTVqGbi1IbfzZ8lurjip4fk8cN_iAJVMhm3yLNy0VyHOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 9T!
🚀
❌
آفر فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!
@Netaazaadbot
@NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15 سرور اختصاصی پرسرعت
✅
اتصال پایدار و بدون قطعی
✅
سرعت بالا حتی در ساعات شلوغ
@Netaazaadbot
@NetAazaadBot
💎
کیفیتی که بعد از استفاده متوجه تفاوتش میشی!
📩
برای خرید و دریافت سرویس استارت رو بزن
✅</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/alonews/123892" target="_blank">📅 13:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123891">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnqDdOa5DBKP42BL5TIu2mEczowbPMsCL3XLn1Aup53OUJSovEmWOUPqDCBJZ4q--Lgi1yt257w5K35EdklfCBEduhuMXlfzWlB76V6ac9exzRYIUGVKnY-kRDOIOqd2MDwWfj-q4s8F33sc97ZDfUJ7wPA73vlBL4cA0vTi2ONv0z5ub26aXNF3OuElzIVl7jZy-X8gY-kkM6DGyev_911CEzROawBV5SfTOZAAsqVHCK4w3MGzEPSxykdbCP23SAUZP7tnknb8rZqSq-Be6_KgQH7eQAsYvKTRtqPVK5tMvEqQEuJOy-otygF4dKw_BS9FCP36th8sCaAi8ILoWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امسال ۷۷درصد بیشتر از پارسال بارندگی داشتیم و سدهای کشور ۲۹درصد بیشتر از پارسال آب دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/123891" target="_blank">📅 13:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123890">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
الجزیره: [جنگ آمریکا و اسراییل علیه ایران]، فضایی را ایجاد کرده است که در آن هر دو طرف احساس پیروزی می‌کنند و بنابراین تمایل دارند در مذاکرات احتمالی برای امتیازات بیشتر تلاش کنند و این امر تلاش‌ها برای کاهش تنش را پیچیده می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/123890" target="_blank">📅 12:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123889">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
الجزیره: از آغاز جنگ، فقدان شفافیت داخلی در آمریکا در مورد اهداف مورد نظر، منجر به عدم قطعیت جهانی شده و به متحدان و دشمنان کمک کرده است تا جایگاه و رهبری آمریکا در نظام بین‌الملل را زیر سوال ببرند.
🔴
تمایل ایالات متحده برای آغاز درگیری با ایران، ارزش درک شده سلاح‌های هسته‌ای را به عنوان یک عامل بازدارنده در برابر متجاوزان تقویت کرد.
🔴
این جنگ انگیزه معکوسی ایجاد کرده است که کشورها را به سمت دستیابی به برنامه‌های خود و توسعه سلاح‌های هسته‌ای خود به عنوان عامل بازدارنده نهایی سوق می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/123889" target="_blank">📅 12:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123888">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
الجزیره: کوتاهی ایالات متحده در مشورت با متحدان و شرکای سنتی خود یا جلب نظر کشورهای خلیج فارس که مستقیماً تحت تأثیر تصمیم به جنگ قرار می‌گیرند، پیامدهای بلندمدتی برای کیفیت و ماهیت برخی از قوی‌ترین روابط و اتحادهای آمریکا از زمان جنگ جهانی دوم خواهد داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/123888" target="_blank">📅 12:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123886">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
هاآرتص: غنی‌سازی ایران دیگر موضوع اصلی طرح‌های توافق نیست
🔴
یک رسانه اسراییلی نوشت غنی سازی ایران دیگر موضوع اصلی طرح‌های توافق نیست و بازگشایی تنگه هرمز و ارائه غرامت به تهران موضوع اصلی آنها هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/123886" target="_blank">📅 12:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123885">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5afb45638.mp4?token=a_YnIjnHzEJHXYtBGCWjYz-AIPgMC6KSm8GPItkf4k1KSJ812b-XPml4k4SojCCpH6Y2DWL1uPrkZCRrYB5oN40mJVqMBGKyRXlvyxX1fwY4pSDMGmtQhLbD_a_Ujd7Quc9KaxIRVDH4AneNZGbcKahtadw8fwP7MFmZWcRuQa655-jhJOkQKRB4z5e-naNb7oX3d6mmVAbHuWvjBUCjcHaXLcYyalYapSOnlc9wnyY_rfudJvOsf13tl1zXCBLJ99Cv72G5450buSGCvIk_Q4oWe8uDcRBTlAsQR_SEoEGY7YshhHt-w0eb2KLL-dGHFdyHa240JK5WtF0QSo20Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5afb45638.mp4?token=a_YnIjnHzEJHXYtBGCWjYz-AIPgMC6KSm8GPItkf4k1KSJ812b-XPml4k4SojCCpH6Y2DWL1uPrkZCRrYB5oN40mJVqMBGKyRXlvyxX1fwY4pSDMGmtQhLbD_a_Ujd7Quc9KaxIRVDH4AneNZGbcKahtadw8fwP7MFmZWcRuQa655-jhJOkQKRB4z5e-naNb7oX3d6mmVAbHuWvjBUCjcHaXLcYyalYapSOnlc9wnyY_rfudJvOsf13tl1zXCBLJ99Cv72G5450buSGCvIk_Q4oWe8uDcRBTlAsQR_SEoEGY7YshhHt-w0eb2KLL-dGHFdyHa240JK5WtF0QSo20Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ :  ما ارتش ایران رو تقریباً دست‌نخورده گذاشتیم؛ خیلی‌ها از شنیدن این موضوع تعجب می‌کنن!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/123885" target="_blank">📅 12:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123884">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b253c1d60.mp4?token=lkfGXnGAVB-hL9ZTWgsoVYDast_j9BiW-qriir_FRuMtgS5jKi3ElGXMdQF3CKOpbuj-iCMj3YwptJOmVe2xy4z37ig9LPQNz0WdufsbRSnt3pCut88lNI728wG-zxiLUcyzawewkphH3kMERIMBimlQEgErlPZYKXwi04YHL3NGoOD-lLi31d6G0rP0gnVoUfbR8OoV0WqJ3ty4mP_7th8rTBbEKPRfoIe1fkDzeh9-z6VgqOl1ELl8SGz_ES184QvDrPDo3VwHbC2FSYGBmct66yTkXfgX4VY40CWuHF9Y_GWMhBkAYac0afdjz1AjdTXT5z6p-EkYCbt1UZt7vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b253c1d60.mp4?token=lkfGXnGAVB-hL9ZTWgsoVYDast_j9BiW-qriir_FRuMtgS5jKi3ElGXMdQF3CKOpbuj-iCMj3YwptJOmVe2xy4z37ig9LPQNz0WdufsbRSnt3pCut88lNI728wG-zxiLUcyzawewkphH3kMERIMBimlQEgErlPZYKXwi04YHL3NGoOD-lLi31d6G0rP0gnVoUfbR8OoV0WqJ3ty4mP_7th8rTBbEKPRfoIe1fkDzeh9-z6VgqOl1ELl8SGz_ES184QvDrPDo3VwHbC2FSYGBmct66yTkXfgX4VY40CWuHF9Y_GWMhBkAYac0afdjz1AjdTXT5z6p-EkYCbt1UZt7vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ :  ما اصلاً نباید درگیر ایران می‌شدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/123884" target="_blank">📅 12:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123883">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
سخنگوی شهرداری تهران: مترو و بی‌آرتی تا زمان تعیین‌تکلیف توسط شورای شهر، رایگان می‌ماند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/123883" target="_blank">📅 12:37 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

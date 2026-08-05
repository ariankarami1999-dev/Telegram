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
<img src="https://cdn4.telesco.pe/file/NRcG1nHmLvSRZ06H0EvY-TIVHVVxUU0Pozw3pu5oYSiQsfevKNE2OBVNSUyMy2mi2A870O77_Z8_tWL6QlzRlxdmvZe4YqPR0OLQdKW3GyzwF9wbYTpgYtCcFQIrlXycgscYqRvu9KiJx0kp9R_sUoDr9MDNRiNTx13-veqMito807GYQUAxc4TfaOXpb1tkEgP5ungTV5g34jnJp6DjHaSc_JvMAsuruHUcrWY9V9-6i8wE8-KoLSGdiUx9CUJMzeHW-njyWbnjjIZa-0SbN7fS8L-_tQNRvlhQdBXW6ZPaokZblfYsSptyJwPyG2ibPUpNiuIsapyuGvrYxHWuFA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 984K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 15:51:59</div>
<hr>

<div class="tg-post" id="msg-140016">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
خبرنگار المیادین در تهران: چشم‌انداز نسبتاً مثبت و خوش‌بینانه‌ای در ایران درباره پرونده تنگه هرمز وجود دارد.
🔴
اگر مداخلات آمریکایی متوقف شود، عمان و ایران می‌توانند در مورد تنگه هرمز به توافق برسند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/alonews/140016" target="_blank">📅 15:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140015">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBa4UbGa2HZXNn8_boM9RDRRJSeGbbZxemxz8ywY8EpQCvK6EO6WpHsF8ac9AwwAd5dxeNVqEsyIptF-_5n9I5xEMPgfWY-x9KDHQnVNnA5ccyfWS_mHqVMkAPSxUbmf1fnNRzX3TDGfmMVgDIotYguwKvyxgsKyXwx5Ka1OazKzsmR8fM38y1F-F8ivqFTjOkhBXdRA1pnrESdJCIVCGeY3mUAA4Zu4PtgHg4n3srj24CQVgIx94Prpoygf0vruYvj9RyfvxNEioHdqaUZz8T51i_uACZkidEQ6Z05PIefsZyVQFbf141NX_xMTQJJosAsl8dkVRicGWzlHD4Qsag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پشت پرده حذف تلگرام از «اپ‌استور»
🔴
پاول دورف در کانال تلگرامش نوشت:
یک مهاجم با استفاده از ترفندهای فنی توانسته بود محتوای غیرقانونی تولیدشده با هوش مصنوعی را در یک پیام قدیمی ویرایش کند تا از دید اعضای گروه و گزارش‌های مردمی پنهان بماند.
🔴
این اقدام با هدف باج‌گیری از مدیران گروه‌های بزرگ انجام شد تا در صورت پرداخت‌نکردن پول، گزارش تخلف آن‌ها مستقیم به اپل ارسال شود.
🔴
باج‌گیران، راهی برای سوءاستفاده از واکنش‌های شتاب‌زده‌ی اپل پیدا کرده‌اند. اپل پیش از تماس با ما، تلگرام را از اپ‌ استور حذف کرد.
🔴
این رویکرد یک ریسک ساختاری برای تمام برنامه‌های میزبان محتوای کاربر ایجاد می‌کند؛ زیرا اگر اپلیکیشنی با بیش از یک میلیارد کاربر بدون هشدار قبلی حذف شود، این اتفاق برای هر برنامه‌ی دیگری نیز رخ خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/alonews/140015" target="_blank">📅 15:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140014">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S89yHzulntef7ynMCxkVKkGfYed5g0MpqoUvhBADRjhOvKkQiZTel38zobU10xFCOBkG0LNRtymAdfwq-LCQUB0XTsAGZbkkCoepiYAKPn-Gqnczpjqd0Xb13n_2ON6QiDIFytvLHWeokY0nN7flB5F0_4iwXHLzAfR8JgeJC2PabyGE58Y8z7hfnMigGNNRapxCVhytHFKSJrBHfbYflneTUv8d1bgZNmKrlMOr0MnewhxIFOJOOaTJgdXh_Q29yjGtdqQVtmwbKt5q6FnkkMNf3o8219Qxd6N0kjaLHE88oP3OuF_wjzo9GRFyCUyChTAOrAxU1aVChle8nk6vtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون_این کشتی مورد حمله یک شناور بدون سرنشین قرار گرفت که منجر به آتش‌سوزی در داخل آن شد. مقامات محلی خدمه کشتی را نجات دادند و آن‌ها در سلامت هستند. گزارش شده است که کشتی غرق شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/alonews/140014" target="_blank">📅 15:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140013">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
برخی منابع خبری از وقوع یک حادثه امنیتی جدید در دریای سرخ خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/140013" target="_blank">📅 15:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140012">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d55a3ac7ee.mp4?token=tbEk_DbLbc5tEouqGN1kwLX9nvbUlnpNrBkAV1-EvNpx3dUcGCs7u3i-FYUtmSL-DLLoUecKqpGky2VQX69g0_i2Gxx2Lki7wgw0JjAvD3VsZPMGte4OGYVur3HlyIXgy-Kt1VF66FmqurgOKCSsTxg7uiRpOcmmlXJV2rYrVbgf9JVD6Qe1UWgdP1za4sBcSktkuvGjY15ciJwPSiO7zygEwFQAk46k9Ov-IEHI-nOlJ_GIMSN13SpR_FQW9ZZqkJvKOcQYAdUWwI2RX9PaFGqWUegi5kU4D0YVCRKOUqlHjrNqdbKovL2vi76cDX6_D5wWB45ZRQivcO3QsvbSdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d55a3ac7ee.mp4?token=tbEk_DbLbc5tEouqGN1kwLX9nvbUlnpNrBkAV1-EvNpx3dUcGCs7u3i-FYUtmSL-DLLoUecKqpGky2VQX69g0_i2Gxx2Lki7wgw0JjAvD3VsZPMGte4OGYVur3HlyIXgy-Kt1VF66FmqurgOKCSsTxg7uiRpOcmmlXJV2rYrVbgf9JVD6Qe1UWgdP1za4sBcSktkuvGjY15ciJwPSiO7zygEwFQAk46k9Ov-IEHI-nOlJ_GIMSN13SpR_FQW9ZZqkJvKOcQYAdUWwI2RX9PaFGqWUegi5kU4D0YVCRKOUqlHjrNqdbKovL2vi76cDX6_D5wWB45ZRQivcO3QsvbSdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور روسیه، پوتین
:
روسیه یک یگان نظامی جدید برای جنگ پهپادی تشکیل داده
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/140012" target="_blank">📅 15:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140011">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
برخی منابع خبری از وقوع یک حادثه امنیتی جدید در دریای سرخ خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/140011" target="_blank">📅 15:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140010">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ded1face75.mp4?token=UB0Nt6nvuShFHKy54Gaca96neuhboJfGnNte0yM6xMHtVDLUG0IsssMzJmyZFQeeCXBzoxg9cRLxUD1hAo2WAmsq0Pq5UCJxOLgO_Uv4sTCZteQ59X0B9-j8jxSdlZI4TDWGxPBf9fuy0GgT1VM3PAY2p1mAsK3RHasste9NN_PfbrKTZy4OOhqWUaj4nKTDQbZM1Fl5lqXVqohbaHxeHd6Y7VwlM3sU2duCAnT-aZM6OG4N_4_s4NDm9Y6cTh8R_Rrwsc7m_WDWmBCLrcLZyn-HejC0Ts-qTAd5l1eHvFxeSaxM-AnnZOuwRQHQPA4pOdQgyDsFuA2TZUJarq0prg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ded1face75.mp4?token=UB0Nt6nvuShFHKy54Gaca96neuhboJfGnNte0yM6xMHtVDLUG0IsssMzJmyZFQeeCXBzoxg9cRLxUD1hAo2WAmsq0Pq5UCJxOLgO_Uv4sTCZteQ59X0B9-j8jxSdlZI4TDWGxPBf9fuy0GgT1VM3PAY2p1mAsK3RHasste9NN_PfbrKTZy4OOhqWUaj4nKTDQbZM1Fl5lqXVqohbaHxeHd6Y7VwlM3sU2duCAnT-aZM6OG4N_4_s4NDm9Y6cTh8R_Rrwsc7m_WDWmBCLrcLZyn-HejC0Ts-qTAd5l1eHvFxeSaxM-AnnZOuwRQHQPA4pOdQgyDsFuA2TZUJarq0prg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه اصابت هواپیمای هندی به زمین
سقوط این پرواز چندین مصدوم بر جای گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/140010" target="_blank">📅 15:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140009">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
معاون برق و انرژی وزارت نیرو: هیچ جهش قیمتی در قبوض برق انجام نشده و هر کی قبضش جهش داشته، بخاطر این هست که زیاد برق مصرف کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/140009" target="_blank">📅 15:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140008">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
یک منبع بلندپایه پاکستانی در گفتگو با ریانووستی: انتظار می‌رود عباس عراقچی وزیر امور خارجه ایران هفتم اوت (روز جمعه) به پاکستان سفر کند.
🔴
وی قرار است با عاصم منیر، فرمانده ارتش پاکستان، شهباز شریف، نخست‌وزیر و اسحاق دار، معاون وزیر امور خارجه دیدار داشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/140008" target="_blank">📅 15:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140007">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f81b077e40.mp4?token=b8MLTn-q2cuUePKSkWPRu9QpeLMqIKZhzLQutx7iYFRFinNNqWVgZ8PJCsI7O909XNYA8Ptmp-VYtEAdMYEq4aTx3YvBHOmuMvPDoPNrUMUjjtNut9Co-Ht8QfDnrWS8EeC-Des5qLoTWBHnHJIEnhPhjRxZIie0eX0npYBL8BgHxrrN3boc6typQBpByYcWq_9Omq-rqo43-IOiP5carbELwYeq3NSuizrs6wFcstVR_2S9g58DXoKNIpen40DFG9O0VQ2VAPIEy-1zTL3PsC_hP5WBZ_9S9l8R3i2aMDLbKK979vvUsbttUwbJo2vqNiqk6Qgv_iLAFAiw6cRrkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f81b077e40.mp4?token=b8MLTn-q2cuUePKSkWPRu9QpeLMqIKZhzLQutx7iYFRFinNNqWVgZ8PJCsI7O909XNYA8Ptmp-VYtEAdMYEq4aTx3YvBHOmuMvPDoPNrUMUjjtNut9Co-Ht8QfDnrWS8EeC-Des5qLoTWBHnHJIEnhPhjRxZIie0eX0npYBL8BgHxrrN3boc6typQBpByYcWq_9Omq-rqo43-IOiP5carbELwYeq3NSuizrs6wFcstVR_2S9g58DXoKNIpen40DFG9O0VQ2VAPIEy-1zTL3PsC_hP5WBZ_9S9l8R3i2aMDLbKK979vvUsbttUwbJo2vqNiqk6Qgv_iLAFAiw6cRrkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه سرباز روس بعد از فرار از مواضعش، گیر افتاد و کتک خورد
🔴
لباس زنونه تنش کرده بود و داخل یک گودال قایم شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/140007" target="_blank">📅 15:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140006">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
حسن روحانی: یک اقلیتی هستند که می‌گویند «اگر این جنگ تشدید و گسترش بیابد، امام زمان زودتر ظهور می‌کند! برای ظهور امام باید جنگ را تشدید کنیم»
🔴
رهبر پیشین هیچ‌وقت به دنبال جنگ نبودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/140006" target="_blank">📅 15:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140005">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
پرواز جنگنده های اسرائیل بر فراز استان درعا در جنوب سوریه
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/140005" target="_blank">📅 14:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140004">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
حسین پاک، خبرنگار صداوسیما: خلع سلاح مقاومت در کار نیست و نخواهد بود هیچ سلاحی از غزه خارج یا تحویل داده نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/140004" target="_blank">📅 14:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140003">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAVC5MBmpPBoyBb5rIACfJ9MDVi6zQuhT8yXm90xaPLmWpsWznCQ-mpXEH4smqwrQiEUol3m0Aau74Mc0Nqymd9FTLdq8ATYLBmr0QGbJh_oJKuMW6OyrErKfO6jH6j_-IxIJx5XZtarxrrh3JsZqYcc6F3rFRx089c6QUUsb_ZAdrzYo_VDfyhn3bhRqK0q3KcZ7W1MKdWdgdKvwZoE2LZmw1j5kVVRuh2UkpWc0dfejnn5v3cXxVEa1nTjM3D8bEzxDS_aYHzQWHA0HLF-taXcxIT9aaKFQDbbh3snN4gCosHBet4tG28O7nj47zz66crau7NXH9QDAnhJHft69A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اطلاعیه وزارت آموزش و پرورش درباره برگزاری امتحانات نهایی معوق در ۴ استان جنوبی کشور
🔴
ستاد عالی آزمون‌های وزارت آموزش و پرورش:به غایبین موجه امتحانات در دو درس تخصصی پایه دوازدهم هر رشته تحصیلی در مرحله کشوری اجازه داده می شود در امتحاناتی که مطابق برنامه ابلاغی به چهار استان جنوبی کشور در روزهای شنبه ۱۷ و سه‌شنبه ۲۰ مردادماه ۱۴۰۵ برگزار می‌شود، شرکت کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/140003" target="_blank">📅 14:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140002">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
سرویس ترجمه Chat GPT بعد از مدت ها بصورت رسمی فعال شد و زبان فارسی هم ساپورت میکنه
🔗
https://chatgpt.com/translate
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/140002" target="_blank">📅 14:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140001">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca751f3e8.mp4?token=P4tr23iRLkkMJ3PL7VaTNe8woWuO3_UGvGvaB6eav06uPYgQiswBCxxDgfn9zvUKfw7JUzi65O8AJrmbxSfF8aJXFkhfeqVoC6YXS02RnLMNimYgnMV0EQsUHU1IGjeCPZYNiS_xrpH_lQ8TooKv7AJEK22Mheuee0TyFZCflfqnGXUPdNUzL6YZqu9hxam388sK9WBXoqm0X4Slu4ej3ZZwmRWIqp3UUz4OwX9CTKTW_xZtuTjm5yg9TQu7QlnF7izzKJJ7IPUIhhl-PVIeNc0SzlqR-7gNaSIf4OAD_deJkp6x05ussnGOP4Ja6xjAfRlS2qWY6fvbUgfwwtSvVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca751f3e8.mp4?token=P4tr23iRLkkMJ3PL7VaTNe8woWuO3_UGvGvaB6eav06uPYgQiswBCxxDgfn9zvUKfw7JUzi65O8AJrmbxSfF8aJXFkhfeqVoC6YXS02RnLMNimYgnMV0EQsUHU1IGjeCPZYNiS_xrpH_lQ8TooKv7AJEK22Mheuee0TyFZCflfqnGXUPdNUzL6YZqu9hxam388sK9WBXoqm0X4Slu4ej3ZZwmRWIqp3UUz4OwX9CTKTW_xZtuTjm5yg9TQu7QlnF7izzKJJ7IPUIhhl-PVIeNc0SzlqR-7gNaSIf4OAD_deJkp6x05ussnGOP4Ja6xjAfRlS2qWY6fvbUgfwwtSvVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طبق گزارش رسانه‌های اسرائیلی، دو سرباز اسرائیلی در اثر انفجاری که در یک ساختمان مین‌گذاری‌شده در منطقه مجدل زون، در جنوب لبنان، رخ داد، کشته و هفت نفر دیگر زخمی شدند.
🔴
آسیب‌دیدگان به بیمارستان رامبام در حیفا منتقل شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/140001" target="_blank">📅 14:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140000">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
فوری/ انفجار در لاذقیه سوریه
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/140000" target="_blank">📅 14:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139999">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
سخنگوی صنعت برق: افزایش سه تا چهار برابری برخی قبض‌های برق، ناشی از تغییر خودسرانه و ناگهانی تعرفه‌ها نیست
🔴
عبور از الگوی مصرف، موجب افزایش پلکانی هزینه برق می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/139999" target="_blank">📅 14:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139998">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
اتحادیه اروپا ۱.۴ میلیارد یورو از سود دارایی‌های مسدودشده بانک مرکزی روسیه را برای حمایت نظامی و افزایش پایداری اوکراین اختصاص داد.
🔴
این دارایی‌ها پس از آغاز جنگ و در چارچوب تحریم‌های غرب منجمد شده بودند. اورسولا فون‌درلاین تأکید کرده است که استفاده از عواید این منابع، بخشی از تلاش اروپا برای وادارکردن مسکو به پرداخت هزینه ویرانی‌های جنگ است.
🔴
اروپا فعلاً اصل دارایی‌ها را نگه داشته و سود آن را خرج جنگ علیه روسیه می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/139998" target="_blank">📅 14:32 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139997">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
ان‌بی‌سی: آمریکا با تغییر راهبردهای دکترین هسته‌ای خود، شیوه استفاده از بمب‌های اتمی تاکتیکی را در جهت مقابله احتمالی با چین و روسیه تسهیل می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/139997" target="_blank">📅 14:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139996">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
دکتر صدیق،روانپزشک : کسایی که تو گوشیشون بازی ندارن به احتمال زیاد دچار اختلالات روانی هستن و مشکلات روحی دارن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/139996" target="_blank">📅 14:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139995">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
وزارت دفاع روسیه گزارش داد، شهرک "زارنیتسا" در منطقه زاپروژیا و شهرک "ریژوکا" در منطقه سومی توسط نیروهای مسلح روسیه آزاد شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/139995" target="_blank">📅 14:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139994">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c6f01196a.mp4?token=KtyFq1SyvEJNvxvzh58eD0KQW-BUf7LgaqkJfON1xiUbngFpzRY3HRLqr9oAK9hvTLMPaEzJvBDzbCmB1azKOpePSHNIYE1n91tfUfXyIkgisHI9aZF2pMEyGHiYhU5Gif821Qgu9vr5aP-t75KLBwFrAB-JsZIfzu3nPIOJo2U0tUuGA7ArraMR-wq_4IewuSfuCjauW0EJvBWjfk-TdlhAH1pyT_3LCfj2sCdcoRWZFg9Id8McyCDMvXR5v3VqO7MRKeaeE-3FoKgDj-K6JwuuIgosMW9SvnHOHQadFxh0ncsExkmWLKAL-5IOo0ib0KrOdQGURHUSwSgN7aSwOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c6f01196a.mp4?token=KtyFq1SyvEJNvxvzh58eD0KQW-BUf7LgaqkJfON1xiUbngFpzRY3HRLqr9oAK9hvTLMPaEzJvBDzbCmB1azKOpePSHNIYE1n91tfUfXyIkgisHI9aZF2pMEyGHiYhU5Gif821Qgu9vr5aP-t75KLBwFrAB-JsZIfzu3nPIOJo2U0tUuGA7ArraMR-wq_4IewuSfuCjauW0EJvBWjfk-TdlhAH1pyT_3LCfj2sCdcoRWZFg9Id8McyCDMvXR5v3VqO7MRKeaeE-3FoKgDj-K6JwuuIgosMW9SvnHOHQadFxh0ncsExkmWLKAL-5IOo0ib0KrOdQGURHUSwSgN7aSwOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی از زخمی‌شدن چند نظامی اسرائیلی در مجدل زون در جنوب لبنان پس‌از انفجار یک مین خبر دادند و اعلام کردند که نظامیان اسرائیلی با بالگرد به بیمارستان‌ها انتقال یافتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/139994" target="_blank">📅 14:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139993">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5cPEn6aM-mtjPCduTUepG7MSV5P2XBfECXqjxphv8iKwKI0E8xfQwFc4MOVoMAFcTUuPn2sd-JVsIhX2A1Bbr-_vhZvnQw80Cjn6xJtg1lRjOi6BGbyUt3zh1lvK6g_CnfyGd-aQqHa0GGqMQx1Ys3jZ6Z1le_JgAwxCFYr1GbDbEysRCeJXiWrP-LhGrHf5IgvR6eO9mlETMQ0a_0FjulQagT7Z7kS9B5ya60WO_C_kE-TY6aCe3iZEKR0XzilWALgTDs7VfDtQddTc1Id9dWSEForXm9jv4FhV60dAqcEabBSS04akFNTY0mrV1sxD7JN3YtuJn45pHmfMF5CTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امیر حسن، نامزد مورد حمایت ترامپ، در انتخابات مقدماتی جمهوری‌خواهان میشیگان برای حوزه انتخابیه هشتم کنگره، در مقابل توماس جی. اسمیت شکست خورد. اسمیت با وجود تعلیق مبارزات انتخاباتی خود از چند هفته قبل، پیروز شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/139993" target="_blank">📅 14:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139989">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ccaj2g1JJiTAbQ0L6CQmyVWaFEUULX3TzYNEddjyQhYQdbVDG1aBSue8KDk5wx4wmdB5g2vMgF7QkTNSnJaW_-i_ZmArSkYTBAqS320P_pLh53AWu_P8XDcCsKvk-FuKHr9TW6gBCB2k-S-uS2zN0Y72OIX6T9EryMD1SEAIln7A1Ts9Z9rJPjRVUuKQLU_QsB4_Jw4uUlPo0MPKa0ybzjtrjv5Xb_6U7_HuhIFFUuQO8-Edws-IhXyTev7P_kFizcj63eT3ugrCEMfSYfCBOpgzadsXiJ_vLoBH1700_6lwns_i-SDUqA9SNTiqThNfI_ntBUqdrL5eCZDQS2yLVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AiFwgXPqDUDLyXO2OrYDg2hnrypsA5_Z33odzXRwuv7HxnbOvXkSm2sB3jHKT2ziNawOR6kMnZch2jc7wVoMvHlLXdSX2oqznzn8p12So3f9YfFjckEJSYvWAR16vBd4EgocHAXE7tzlf6IMqAuCrwOpsx10ypHKHpSnLrH4wTdw3I5pzXyVNHtrfH2wxvfM-e8cBuKEFZk2U7_SV_s36M0kDXplk-4bRgU3sHVCRKYqQTjr4TtVHsT2l_qt2ahufwehRJm6E7FYqGrguy-7BKOH68M8UnX73ErfI74AVPvCi_yCRS3WB5IW-xVSiPmX_3um0oWMx7dv2vebenWn0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s2B1EQT9NWqKAA5Wlya8qiISvI-FDuFrcnwxM8e9T5Viq3oC4t8PCE0lK331z-MCc511cxQ0XGm0TLYifQN4KGFalNtRFL4GwFPKJWS2IIRSq23rcql4mMLA9FyE5YkOGLzs94WkQNfmFvSv6D7kF805Nkyud1IGuYxO1rMyOfU-nL5J-xQH1ZGnnxJiHq00gX0CyYBZZXb8A6g7KpxGd6VDOAHEzYgLyWwgQzBM2IXVejEmxGRussR7XEpHFt7iF25nzJ6jLTfFE3lBpISqz46lndEt2sr7USf7IiJMMH4ReaFdGmJVdzhkLQ8MQ73ymkuvqoEUXmu8vejBc1Rd_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96951795cb.mp4?token=bCnhMMJ5rpG6FoY6Q8GQuW8y6WnXka1SzqFDacpU62hJC2FZUgjRh-8qdJmcwIQeH5uHdeG4giT-nZuGqOh2fzHwokmEqjMLW9z3-GBUsZmxUGZi8F22lt0qHLnKMZylY_aiDKWVHPjOKxHl7OQahNmfDkjKPlsD4S8-ElZ7bnWgLpIwn3Ij8U2FCM1CQLpvcD2Q4XsZSrYryp0i217tLqljUPuOu52K0XRCMqNXH6HpatkWnW13KJmaXwSpkryyFjYxrCy2d1tW5IBrv1avM3cFzSksUP0Xs7haiPODEfByozUw9kxZ6O8weZC-7ult8d6FTO164WoPNrXlJV2tag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96951795cb.mp4?token=bCnhMMJ5rpG6FoY6Q8GQuW8y6WnXka1SzqFDacpU62hJC2FZUgjRh-8qdJmcwIQeH5uHdeG4giT-nZuGqOh2fzHwokmEqjMLW9z3-GBUsZmxUGZi8F22lt0qHLnKMZylY_aiDKWVHPjOKxHl7OQahNmfDkjKPlsD4S8-ElZ7bnWgLpIwn3Ij8U2FCM1CQLpvcD2Q4XsZSrYryp0i217tLqljUPuOu52K0XRCMqNXH6HpatkWnW13KJmaXwSpkryyFjYxrCy2d1tW5IBrv1avM3cFzSksUP0Xs7haiPODEfByozUw9kxZ6O8weZC-7ult8d6FTO164WoPNrXlJV2tag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر‌ی از حمله‌های ارتش اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/139989" target="_blank">📅 13:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139988">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
حمله هوایی اسرائیل به شهرک المنصوری در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/139988" target="_blank">📅 13:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139987">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNsjjKdHPZvZ14TnAXjPwNHAHoHzyhwIzftugPACfmH6l-GCWyQ98ERyphN6GwSEnXqzGs_aOe7dtpbHEXJft_DR3V6E2wPBicLrNQxa3wiJvM_zfUP-hpv9lIihYtMLAvvXQPQQo2PhKKGtM1vma3JZTwlLI6-OCCjpaoUb5m3U4OpE94B7PvIiNDaVRid_hwh-6q6SE9oj6zdKCl9VXoVE8whmxJ1s8oCSJpmqawN5MQP3VQh3CNfFp8HIDr0cqeCW99EyM7gEB1ZHJk7mNaEQkW0Lwk8dnUnHKarDDYD6orOvs-ZiVfm01U3ROrzBfp-YkM740xeRKq2G1u8HHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
احمدرضا خاتمی به عنوان فرمانده مرزبانی استان کردستان معرفی شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/139987" target="_blank">📅 13:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139986">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
پزشکیان: از هر تصمیم رهبران فلسطینی در روند مذاکرات حمایت می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/139986" target="_blank">📅 13:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139985">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
دور جدید مذاکرات لبنان و اسرائیل در رم عصر سه‌شنبه با تمرکز بر پرونده مرزها، سازوکار راستی‌آزمایی اجرای ترتیبات امنیتی، خروج نیروهای اسرائیلی و موضوع خلع سلاح حزب‌الله پایان یافت و قرار است گفت‌وگوها روز پنج‌شنبه از سر گرفته شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/139985" target="_blank">📅 13:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139984">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a513U-0ticZr5hmUKXXLuwK-sjlzPnKJDGm59eFGSx7x58Zu_bVWVxvqzy4vzN9-214035Gj7fY4-Kz_MHXFyQTWEtabN2O4eOGIEd_I_HSjndOrX_x7mVmnClakC57Pc8lPLXWlaYwQ-UnRCmNR_YquubtrzKtH1cKX1y7TrjEXY29RmWijZVseTR8RjRDVI4XBaQr58CyNXJZyc19oDuEKiinELjjU2GP3tdOLmETOCQI-2z4paOyK9Z_VEA9qgfvw7Le_YDncWVLyiTvWSE7eiaRhSnHDE94TSe9QSrZhOpswGP0atNjUvcLEw-IbvUcb-cvkwJvEifpLwLbG8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کمیسیون امنیت ملی خطاب به آمریکا: به زودی از منطقه اخراج می‌شوید
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/139984" target="_blank">📅 13:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139983">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaQcYxJc0G8kGs-H1S8B830Uwu2qN2MhP1w_CvgMJmRlCj27JliEpIfFbZB1aFin4K6wjtYbI-qWNRNo8O1tv0jtXdLmYa94Lh9-PfSjBFhTHm1iy4ETW1B7CcepHKkpp3qVuR1gGe3ZN-7fQ4x08hcuVc98RK7EHheozT0bK4u7lL8Jon-owkDscptiClvRHUORsem3I0amDf16a0FTkbdpmXpYe_JR5KTU3R8XNVF6H_jZZOMfeLvMc4circJPameofg6pJ4oo3yxR_uEG700jlp0H7mxfwrSOxl7QUPDI5fuaV_CXbWtTrH3n63Ev4IQQZCaWgWeoajHrjwSjqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش NBC News: مسئول سیاست‌گذاری وزارت دفاع آمریکا (پنتاگون) در حال تدوین راهبرد جدید هسته‌ای آمریکا است.
🔴
در این راهبرد، استفاده احتمالی از سلاح‌های هسته‌ای تاکتیکی (برد کوتاه‌تر) در صورت وقوع یک جنگ منطقه‌ای با چین یا روسیه پررنگ‌تر خواهد شد.
🔴
این سند محرمانه است و گزینه‌های هسته‌ای در اختیار رئیس‌جمهور آمریکا را برای شرایط بحرانی مشخص می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/139983" target="_blank">📅 13:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139982">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpbqUmi6m3Y0mEyiaEXJelxbLl-q9j0dltRHGm546rFUz6pMw44j41vxUPGO2RzjJk7b6RgHNLl5ZYNZIz3Y9g06V7OUfJtZB4nYGLscglV7C7R1F4Uja6YjIfInzRqnP15hmVlHZ2ng0nFSNXmqyP61-lJgN34p-Jr2Wy-uC3qq5NPDNzLwUI5A7e6X1CxNo8_9sF0MMvJblYZ4dS4-yaTV4PjoaTh8ArYjep5sLBR-mvui4hIyh3kJJHGBTchvx5ZT0r3WUQISxS8ymHuYd0HTgDekLZfBg55LccN4dCg_BhloyYlUJ5aETDHuK8qYldzf0y45tY16w02Yjq-6RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دسته‌ جدیدی از سوخت رسان ها برای مذاکره وارد خاورمیانه شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/139982" target="_blank">📅 12:57 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139981">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSm_mWS2fYdhz-k0HaReLFTcXNdCT9QGEJI0fQgyhVpPTVKTrWDhXfz2w0cwe328ZbIgthfzKLgyo8dXqr3QnoDPXxx2zr3s4mx1bjbrmKRAzx4DcViLHiHBvmG0g_m--PV93KkLHhrcOKhlTgEBDwpjk0lNt4_qD8QVf2XsHNgI5n_RviyRFLvgx3YHq4ZZsWF_qg6a49R25ES_ncanTomtEvtP_CedSvIEjTz5jA55lNspCr0-Q7SO5WyfdwGr0MTWXmoPdGC_mY0Fl87UMjDfIiaXX69lYIlnhEM_r0zkT1KZY3l41zmmpy9vbz9u2mtvWfo-vNkwvlENohf7ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
قیمت نفت با کاهش های پی در پی به ۷۶ دلار رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/139981" target="_blank">📅 12:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139980">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa0e8f6822.mp4?token=IJJ_1Fxw52eHP31h5tc8-BTvfqoCu0wTCYwdI8270Bmsox90stVF941lTJp-Ze1bHJ4q168B60XqoxiU7Zg5YlBNUO6h-2YVUUX8rJVZOUfyLjHf8NqmBtw7Q1SOOCSrfj5vZT6UMPK9tB0QKUWYPqowhIZwbF2viPypEMnTir1hvOjSF_r6okFksFIvfxf3QBs3jq6cJeFpJ6KKFu7QigaeAtsjKF228fmYERDpPqIWy3pwcjMlZrrxcCI4DQtsdWpA2H3qzohLmvcUwHZkJAU4ZNmhVrp04nzZXgRjY3dU_quwxai-oGDjnmedPk9lpKeBbyxtGU1Ne3goesA2kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa0e8f6822.mp4?token=IJJ_1Fxw52eHP31h5tc8-BTvfqoCu0wTCYwdI8270Bmsox90stVF941lTJp-Ze1bHJ4q168B60XqoxiU7Zg5YlBNUO6h-2YVUUX8rJVZOUfyLjHf8NqmBtw7Q1SOOCSrfj5vZT6UMPK9tB0QKUWYPqowhIZwbF2viPypEMnTir1hvOjSF_r6okFksFIvfxf3QBs3jq6cJeFpJ6KKFu7QigaeAtsjKF228fmYERDpPqIWy3pwcjMlZrrxcCI4DQtsdWpA2H3qzohLmvcUwHZkJAU4ZNmhVrp04nzZXgRjY3dU_quwxai-oGDjnmedPk9lpKeBbyxtGU1Ne3goesA2kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای بدون سرنشین "گرن-4" متعلق به روسیه، دو کشتی باری را در دریای سیاه غربی مورد اصابت قرار دادند.
🔴
وزارت دفاع روسیه مدعی است که این کشتی‌ها تجهیزاتی را برای ارتش اوکراین حمل می‌کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/139980" target="_blank">📅 12:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139978">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f39178e72d.mp4?token=ZqicXuTjDSsjHJw0umB6Fv9pnPxnhpJj93jEShFCIyo5fbzANmr7l0Kl2TDPvN28pRL6N03zjLAMykrC10PYiBz7mqlnoaohJLzLG01KkxGllb43BC_sya2japIZvZRINsPVBYjsvOSnBaGHdgOj03UNaRCQtkwjD0vi8T6s62cbQ8m7UT4L0AJ5L9ay5grgnwldVFXbWlO0Oh09ieEtyLPaQdIz4IngNnDG8blam72seXNG_rkcO7XomoG6OAyJr8Wj9bgwZq3yDm4kgnlYCz6q7vuwg1TZRT3Sg1BNY2fm-Y9FeS2_xt5HzkJnXF1zhBckIlM8UnsZSFeylr5Xnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f39178e72d.mp4?token=ZqicXuTjDSsjHJw0umB6Fv9pnPxnhpJj93jEShFCIyo5fbzANmr7l0Kl2TDPvN28pRL6N03zjLAMykrC10PYiBz7mqlnoaohJLzLG01KkxGllb43BC_sya2japIZvZRINsPVBYjsvOSnBaGHdgOj03UNaRCQtkwjD0vi8T6s62cbQ8m7UT4L0AJ5L9ay5grgnwldVFXbWlO0Oh09ieEtyLPaQdIz4IngNnDG8blam72seXNG_rkcO7XomoG6OAyJr8Wj9bgwZq3yDm4kgnlYCz6q7vuwg1TZRT3Sg1BNY2fm-Y9FeS2_xt5HzkJnXF1zhBckIlM8UnsZSFeylr5Xnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر تکمیلی از موشک‌های بالستیک اسکندر-ام روسیه که مجهز به مهمات خوشه‌ای هستند و شب گذشته به شهر کی‌یف، اوکراین، اصابت کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/139978" target="_blank">📅 12:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139977">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با جهش ۱۳۰ هزار واحدی به ۵ میلیون و ۴۰۸ هزار واحد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/139977" target="_blank">📅 12:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139976">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
روزنامه اسرائیلی جروزالم‌پست:حماس در حال انتقال واحدهای خود به ترکیه است
🔴
حماس در حال انتقال واحدهای سازمانی، فعالیت‌های مخفی و عملیات امنیت سایبری خود به ترکیه است، در حالی که قطر همچنان میزبان رهبری و فعالیت‌های عمومی این سازمان خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/139976" target="_blank">📅 12:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139975">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfKdAUSJheWWp_hQS9WFzFs_Ihjxy8DxPVCqrxaRNQDlslrS4sV4diR8mwadh85QstiI8dBYWhxeF0P9V1aGsQBYXgHoAlYxC2kpAU3NPPd5ODV7Swf3HzBB05HHXDRQk5aDyOnDqlhpWVQC3bdRndqvPE3ZPZ35-ucIHzL0qzcEiSjxHDb1YY_eprlBpzXDvKa-ME6lKyWOrNVh-OEOcexKOtfQ0P4yeu3bo20_MEp1JS3G6F3bqoED3KsLRT_gfXmj-HADxsJsaDSu1D-4Y2TYf9wTCanEQgoNHGfPkqpqpZNdWlHcJ2AOi5XbxLtuYk79wqRv_6Ek_rxHdDRC-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیلد آلمان : یک پهپاد در محوطهٔ پارکینگ هواپیماهای فرودگاه Leipzig/Halle  در آلمان پیدا شده است که به آن یک جسم حجیم با یک مواد منفجره متصل بوده و بازرسان آن را به عنوان یک وسیلهٔ انفجاری احتمالی طبقه‌بندی کرده‌اند.
🔴
گزارش شده که این پهپاد درست در کنار یک هواپیمای باری اوکراینی از نوع آنتونوف قرار داشته است.
🔴
پلیس فدرال تیم‌های خنثی‌سازی بمب و یک ربات را به محل اعزام کرده و انفجار کنترل‌شده‌ای را برنامه‌ریزی کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/139975" target="_blank">📅 12:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139974">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
میدونستین اسلام آباد غرب، قبلا اسمش شاه آباد غرب بوده.
🤔
هر جا رو شاه آباد کرد اینا زدن به نام اسلام
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/139974" target="_blank">📅 12:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139973">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xd3gJcw1XzuHQzFV6RnxL5lTsuNFDaRICtJduov_o7RQNPGj280Rzv8fSFjp2qe-wFAqRAxBayqDgMYgNpwfYTSMEEM6NkHA8AGZShSUJcD3iJ2TKz219GKi8t9c_jDEq3ZjJeMAChc2ufEhT55nu9EewhNtJVRsmKiCFrJPGeTsQa8IeP6mu70Iat8ZV1NvqIMdoIc_qh_9IHQBlxAEuSb8vUAAH4na2q6t_q2IH2-uQlyNBBcsjxYx7NkZFKyL158mfDT0LHPzMDshOGMKarSsYzqxOuBxE8g2OJoJbQUy_yomn5lkAl_7hpFx1B6H8KdqJfTyibGMCs2Eakif0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به عنوان بخشی از افزایش حضور نظامی آمریکا در خاورمیانه، هواپیماهای سوخت‌رسانی بیشتری از آمریکا وارد فرودگاه بن گوریون شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/139973" target="_blank">📅 12:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139972">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
روزنامه فایننشال تایمز: ترامپ در جنگ با ایران در یک تحقیر استراتژیک گرفتار شده و نمی تواند بدون پرداخت هزینه سیاسی در داخل، از این جنگ خارج شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/139972" target="_blank">📅 12:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139971">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac8efc6d7.mp4?token=a259UJrfaNc2ph1Lt9DU0qWvm4w3TbvcEqBZRhNJqkQT08rmKp65XHmWguxy3z-mcVGZSCvO9wCZ5Eve-rI23t8yqaADbrHmLGqDYw55ezRId0wny-0I1n447ltDB2a-cIQ4b1cCBFkV52pHwxctjm2y-8uBIf4MlqHhPwqnt3OR6oQqZay89ImBKDvROJ99Ko-Mu9TnRcw5vTH-uzNiye8TiaS8TBYyiv2-qkNZ6-dM0NnUoOrRuJo-sCXX_LvP3AlKKtc_FL2tWF6WRyfxwTD9czvUtlVCJsewjmd7YfzvOyfDOVonkFcidAvlhA0i2rpO67lq9Am-PBNbnaI4Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac8efc6d7.mp4?token=a259UJrfaNc2ph1Lt9DU0qWvm4w3TbvcEqBZRhNJqkQT08rmKp65XHmWguxy3z-mcVGZSCvO9wCZ5Eve-rI23t8yqaADbrHmLGqDYw55ezRId0wny-0I1n447ltDB2a-cIQ4b1cCBFkV52pHwxctjm2y-8uBIf4MlqHhPwqnt3OR6oQqZay89ImBKDvROJ99Ko-Mu9TnRcw5vTH-uzNiye8TiaS8TBYyiv2-qkNZ6-dM0NnUoOrRuJo-sCXX_LvP3AlKKtc_FL2tWF6WRyfxwTD9czvUtlVCJsewjmd7YfzvOyfDOVonkFcidAvlhA0i2rpO67lq9Am-PBNbnaI4Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی: با حمله سنگین موشکی مواجه شدیم
🔴
ساعاتی پس از انفجارهای مهیب در پایتخت اوکراین، ولودیمیر زلنسکی با انتشار یک فیلم خبر داد که کی‌یف هدف حمله مرگبار موشکی و پهپادی روسیه قرار گرفت.
🔴
رئیس‌جمهور اوکراین گفت: «تاکنون، گزارش شده است که ۴۴ نفر در حمله گسترده روسیه به کی‌یف و منطقه کی‌یف زخمی و ۱۷ نفر دیگر، به طرز غم‌انگیزی کشته شدند. به خانواده‌ها و عزیزان آنها تسلیت می‌گویم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/139971" target="_blank">📅 12:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139970">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ترامپ درباره اقتصاد آمریکا گفت:
آن‌ها می‌گویند محبوبیت من در موضوع اقتصاد ۴۲ درصد است. من نباید ۴۲ درصد باشم. ما شاید بهترین اقتصاد در تاریخ جهان را داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/139970" target="_blank">📅 12:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139969">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
سازمان زمین‌شناسی آمریکا (USGS) ساعاتی پیش از وقوع زمین‌لرزه‌ای به بزرگی ۶.۳ ریشتر در سواحل جنوب فیلیپین خبر داد.
🔴
تاکنون گزارشی از تلفات جانی یا خسارات گسترده منتشر نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/139969" target="_blank">📅 12:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139968">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3c27e3dc6.mp4?token=Zrx59JMlsEheLUdZ2GmReyWgWBaYDRSVz_GcXnTOb56af52m05geWlJBmk0aLaBdmH-nrJkZvMkgQEX8SPiMuASyuybEZT7wNlK7QjML0j0vgyK6iJ47iyqRI0Q1e72rVxKKeX4ZtJ5BJoCH9F_jGIaHhLWuUSi_8P_sGQzciuW2416x-yVW4rKWqpbl6t32i0m9F-qQVNvNwJPHdW6WyNXbhbzLqt7wWJHMXQlIxColDs8abiUpVEQ99tQccl8HFuZhpC9Xfpyw5bW94QGUWm17Kmy2U2Gd0K-mMnRcksOGnoXuaFFSWctglC13WePNEqWUSW6ucxfY5m_Dbpi0FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3c27e3dc6.mp4?token=Zrx59JMlsEheLUdZ2GmReyWgWBaYDRSVz_GcXnTOb56af52m05geWlJBmk0aLaBdmH-nrJkZvMkgQEX8SPiMuASyuybEZT7wNlK7QjML0j0vgyK6iJ47iyqRI0Q1e72rVxKKeX4ZtJ5BJoCH9F_jGIaHhLWuUSi_8P_sGQzciuW2416x-yVW4rKWqpbl6t32i0m9F-qQVNvNwJPHdW6WyNXbhbzLqt7wWJHMXQlIxColDs8abiUpVEQ99tQccl8HFuZhpC9Xfpyw5bW94QGUWm17Kmy2U2Gd0K-mMnRcksOGnoXuaFFSWctglC13WePNEqWUSW6ucxfY5m_Dbpi0FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : حرکت‌هایی در حال انجامه, ممکنه فردا یا پس‌فردا، یعنی چهارشنبه یا پنجشنبه، اتفاقی بیفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/139968" target="_blank">📅 12:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139967">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56e4a309b6.mp4?token=Jo3OHEwGPC8lDk97ex6WYerupYkq14jdKDMYKaRyq5xDWXdBoUn3gCcOvHyFdEjze4IFPwjuOV7F7l2XoSWpsNmF6D2WMEPlI_bFiUv6pYbT21plTgmfVPeiqWicNDsze8GenFizqXkPb9JCuXfX5xOyueKYAapMDhnGGkfAJWsUcJORXKE-GYcm4_R1ei_8oRublSTNnlP9VMN7M47KlWd568pg4S6t7tJ1qETCuaqMxdKR0MM27LM1VvSDVOBNCT9uMIhL5FKUR2VMndnejD4QxAbzIZMU8OFZBTKXDHeDloP8leBuyCSCbnjtfLD8d-0L1huXkVABm45VwhX1zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56e4a309b6.mp4?token=Jo3OHEwGPC8lDk97ex6WYerupYkq14jdKDMYKaRyq5xDWXdBoUn3gCcOvHyFdEjze4IFPwjuOV7F7l2XoSWpsNmF6D2WMEPlI_bFiUv6pYbT21plTgmfVPeiqWicNDsze8GenFizqXkPb9JCuXfX5xOyueKYAapMDhnGGkfAJWsUcJORXKE-GYcm4_R1ei_8oRublSTNnlP9VMN7M47KlWd568pg4S6t7tJ1qETCuaqMxdKR0MM27LM1VvSDVOBNCT9uMIhL5FKUR2VMndnejD4QxAbzIZMU8OFZBTKXDHeDloP8leBuyCSCbnjtfLD8d-0L1huXkVABm45VwhX1zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار : اوضاع چطوره؟
🔴
ترامپ : داریم خیلی خوب پیش می‌ریم، مشخص می‌شه. تا ۴۸ ساعت دیگه می‌فهمیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/139967" target="_blank">📅 12:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139966">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIW2iMKVkJepgu3EMnP3SAZa_DLX_5dih9hs7-hq_jHoIfBoYyPid2eO7ZXAXgOrzgDVA6BoldYwyMfOdHOoBp0dw_LX0xbSz5MdFn5WayVvrRHo9_-0Qzv9wMHg45gQ8_dkW4iUX3-YtBrFpLNIGvJEXkMtm_XlLx0NRs_lzUhzUHa46xyeGxu_YTX74x3CiYRgOaJTyYh4Y9SeIUMZTvfQ7N2HxDTLPY71Z_mSIyYxvaVZUbcbvurzjjQZ-p8TJKFy9dhic91eUEdyMdEhK_VlSibtQfFHwiEZ6yUl2NVyiGI7QSnhjNGkXWqRpvcFom3aZj-en9e4gdcIKF1iHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای شناسایی و نظارتی E-3G ایالات متحده اوایل امروز به پرواز درآمد که احتمالاً مربوط به فعالیت‌هایی در تنگه هرمز یا یمن است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/139966" target="_blank">📅 11:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139965">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
صدا سیما : توافق احتمالی ایران و عمان در باره ترتیبات عبور شناورها از تنگه هرمز هیچ ارتباطی با باز شدن فوری این تنگه ندارد/در صورت ادامه تخلفات آمریکا، تنگه هرمز حتی با توافق بین ایران و عمان باز نخواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/139965" target="_blank">📅 11:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139964">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
سازمان امور مالیاتی کشور: بلاگرها و فعالان فضای مجازی نیز در صورت عبور درآمدشان از سقف‌های تعیین‌شده، باید مالیات پرداخت کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/139964" target="_blank">📅 11:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139963">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
حساب‌ شرکت ملی نفت ایران بسته شد
🔴
کسب اطلاع فارس نشان می‌هد بانک دولتی صنعت‌ومعدن حساب‌های شرکت ملی نفت را به‌خاطر بدهی بست.
🔴
پیش از این وزارت خزانه‌داری آمریکا در قالب تحریم اقدام به محدودیت مالی برای شرکت ملی نفت کرده بود.
🔴
اقدام این بانک در شرایطی انجام می‌شود که طبق قانون بودجه بدهی‌های شرکت ملی نفت تا پایان سال ۱۴۰۵ امهال شده و این شرکت تا آخر اسفند برای بازپرداخت بدهی‌ها مهلت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/139963" target="_blank">📅 11:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139962">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0miyr2UbEL_OZD819cjlOVyHHd0UNyciwD2rFfnWTR7QoKLv2qohSUoDZfN0ZeXn-olSNBwcujQx7-RR7_elwm0ehaje1BfT0LHNobVaoHIRu8Lk_afxcRQuukPiOCgHqtgKPlM7PoNrpOnFUbtfDur4yzXtKMNrkv7qwLU32zxgle4pKtSlGybrzHl4ZjADiTuCRhY5MYNf5L2l31CLINlowj5oNLv-HoyGQAihXZqnGNJLTY2VPyHH5ttclXC1_3_8FGhUJdkizzZLxHcjraIsUvUZiTxUjHrpFOO6GdrPrSxx448FLQqON9c2Ra5QRcnfrtII3UR9yM-Bh4AmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوکراین بار دیگر به پالایشگاه باشنف روسیه در شهر اوفا ، یکی از سه پالایشگاه واقع در این شهر ، حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/139962" target="_blank">📅 11:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139961">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aekuRM2m3baigZAHfiZuplkHUPxkmb533GPoKp1QQBSr-gMpgvpB_V8KajO2OdaJ6cdo6Qk6wO0qjhjaOTlGPZfyKRgfHz1ITX4DJ0uxwEuzN0vXbv5N8cYzDAea9-Ui6a7ww4M_1D-NkeC-DGgSuErG6kqWzF9mZcDK8EJdRkL_nf_uuqly6LbWtYlUtbiQMvrKWzeg9XY9p7mDLRjHnLN2jtya9LcD9mXAt9NO52IonxHlzNrhX74jSr_UJPaPMLXbqHxcnF95s7HTxL3R-uHKuMAqlrZOIS_sY4OYaVi1jW6yVRT4Age2INj1gzDYtu0e_8r8o2vnPjmapdL9Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز : اطلاعات نظامی اوکراین میگه، کره شمالی شروع به استقرار یه واحد موشکی تو غرب روسیه کرده
🔴
قراره تا ۱۲۰ موشک بالستیک و ۶ پرتابگر برای استفاده علیه اوکراین تحویل داده بشه
🔴
اگه این خبر تأیید بشه، نشون‌دهنده گسترش همکاری نظامی روسیه و کره شمالیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/139961" target="_blank">📅 11:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139960">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OL_t8ZQ2hUB-vPavCe2tv7HcvVPkq13SDR_6Rg8yZb5qLsDKNi4b8te6gANgK3qX_j9olHQRfsMakO5OVUHttZsdaaO0Itt4e-QO6gDPJl6byokREVjJDUu8sr6IMJ3MDWQL24ysQ_tik7pMTTIMsD2yqyiUKyJhu84vl5Jx29x7T11WX8ZqrMtKe91jteSW4EG_CYQmHSJMJMpv-MPkvFFpch3lBgiiaj76PhSQ6cBSIY2U43fw1kV6aZrT1YymzfVQNIPV42o2UItZjK_8zTR8cX4JaMD845t6k4grdQo9-gEqRLLnDfRtcvk0TXB6qt4pdU557lKCp2uT9k9JwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کیم یو جونگ، خواهر رهبر کره شمالی، پس از آزمایش موشکی ژاپن هشدار داد پیونگ یانگ «گزینه‌های نظامی بیشتری» در پیش خواهد گرفت و گفت: باید کاری کنیم که پشیمان شود.
🔴
او ارتش ژاپن را به تبدیل شدن به یک قدرت نظامی تهاجمی متهم کرد و آمریکا را پشت این اقدامات دانست.
🔴
خبرگزاری کره شمالی نیز اعلام کرد اقدامات آمریکا، ژاپن و کره جنوبی از نقطه بحرانی عبور کرده است. تحلیلگران می‌گویند پیونگ یانگ به دنبال توجیه توسعه تسلیحات خود با نمایش ژاپن به عنوان تهدید است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/139960" target="_blank">📅 11:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139959">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
رویترز : آمریکا همچنان داره با اوکراین مذاکره می‌کنه
🔴
تا اجازه تولید موشک‌های رهگیر پاتریوت یا قطعاتش رو بگیره
🔴
یکی از طرح‌ها اینه که قطعات تو اوکراین ساخته و مونتاژ نهایی تو آلمان انجام بشه
🔴
اما تحویل اولین موشک‌ها حداقل یک سال زمان می‌بره
🔴
و اوکراین تا اون موقع همچنان به کمک‌های تسلیحاتی متحدانش وابسته خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/139959" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139958">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ترامپ: تنگه هرمز ممکن است امروز یا فردا، باز شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/139958" target="_blank">📅 11:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139957">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFheslg0Nu3Bjh_LDgCj6U4Wv-9OsnYjPjtKOxi76o05LyOLcjqfw0BwzigESpXz9B2QeOJw-k43zjrf7qBfTHSAUkFuQWG3vb2f-5mlB1WCEa74ZnL3r_02WWcTlqSXSh-wNzZdxxc2B7KMmBFzE8IzDQwSfzDUGZ5SPJR4vfjZHpVPuCNhSOMGibEfxXy5Wh0-rvf0kngnHBDtO0Zvai6-LYkTEtRJ2EjIHx-GcqLj3vg0bzbeiGlbmN1rp1tPVYKeMkzHji-krHwOFs9CW6A3YVlg3bWUfNcYdj7ffUzh7KMDpvakIzR7MmUrX4HYm9rptmcoLnhtvhD8WP7X0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ
در تروث سوشال
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/139957" target="_blank">📅 11:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139956">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a0d9b3137.mp4?token=ZPCqaH88CzIIKKjPRK8f14BZXg1CDFqsiYZr1m1kM-eAj1KiM9yrnCT9urp4cOPlj3q71IO7vUwtHH2vJmC8cSk8z3k4_QEl-svbXnDTFrSvcJpZ9dwME8aBZhUUxOU2rcLK77A-GSDDyp4Ev0XYHLFwomEPVxaZXExTAW7D7k0FJuoMtd9ucVvAUo9tfh5Q1PtPM-_QAiQPqi0NI_PhLf5AiVbgj26IA8__QM3nuXDCGprb00dTj1dtIpIeIJ-LBcuhY5ievwdi2FDgxBkpVnyz8clPFCEFa-p0AnsD2D2NOVPCueul88zEY3YxsExW_SgDqQ11HUCrPsu-vgQY2xT_42Hi7R1ABNgewTG9Gqf5B8oJ_tTXr4PReK2MI_AOFKM5ycvsPCA3ZUix6j0C7OIDXx4fBX6E-ygVUC5hOWTqvQJkejVSQB3Y9EXleX77C5o4eFDX_yFVUdXcisS4yOHysVG_Qebk4WO9R9MwlCnogKc2E7cX2bSXNTbFW5eGeRdY4GUNdxz3enbKhr7oHayriQ_cWbhwWXTAacjvdS8R6neuxFF46FuzRJjsXxRiAbHcKr2vvSbdpS0I5PGxb2xwb-hY444HSw8Ms9IVlcFrqCoI-XLZijxA_8lI27EKxuQV3ntE6-ncd9aKTM2fb9H0FgFCmkZw530YuIttfCs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a0d9b3137.mp4?token=ZPCqaH88CzIIKKjPRK8f14BZXg1CDFqsiYZr1m1kM-eAj1KiM9yrnCT9urp4cOPlj3q71IO7vUwtHH2vJmC8cSk8z3k4_QEl-svbXnDTFrSvcJpZ9dwME8aBZhUUxOU2rcLK77A-GSDDyp4Ev0XYHLFwomEPVxaZXExTAW7D7k0FJuoMtd9ucVvAUo9tfh5Q1PtPM-_QAiQPqi0NI_PhLf5AiVbgj26IA8__QM3nuXDCGprb00dTj1dtIpIeIJ-LBcuhY5ievwdi2FDgxBkpVnyz8clPFCEFa-p0AnsD2D2NOVPCueul88zEY3YxsExW_SgDqQ11HUCrPsu-vgQY2xT_42Hi7R1ABNgewTG9Gqf5B8oJ_tTXr4PReK2MI_AOFKM5ycvsPCA3ZUix6j0C7OIDXx4fBX6E-ygVUC5hOWTqvQJkejVSQB3Y9EXleX77C5o4eFDX_yFVUdXcisS4yOHysVG_Qebk4WO9R9MwlCnogKc2E7cX2bSXNTbFW5eGeRdY4GUNdxz3enbKhr7oHayriQ_cWbhwWXTAacjvdS8R6neuxFF46FuzRJjsXxRiAbHcKr2vvSbdpS0I5PGxb2xwb-hY444HSw8Ms9IVlcFrqCoI-XLZijxA_8lI27EKxuQV3ntE6-ncd9aKTM2fb9H0FgFCmkZw530YuIttfCs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بگومگوی مجری صداوسیما با ناصر هادیان بر سر مدیریت تنگه هرمز
🔴
مجری صداوسیما: ولو همه دنیا علیه ایران بسیج شود! چیزی نمی‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/139956" target="_blank">📅 11:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139955">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
آتش‌سوزی در جزیره آشوراده با حضور نیروهای امدادی و عملیات هوایی بالگرد هلال‌احمر گلستان مهار شد.
🔴
در این عملیات، بالگرد هلال‌احمر طی چهار مرحله پرواز عملیاتی و ۱۰ مرحله آبگیری، ۴۰ هزار لیتر آب را بر کانون‌های آتش تخلیه کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/139955" target="_blank">📅 11:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139954">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H11LNoJyKafL4_IemfIw3MvN0hqhebYqp3motsP0NN5UON4PHeFsX4eVAFbYBTo-Z_lgoiwAeNcLMWA6HfqOMVTBh5Wj8IizDD4CgneDngO15f7trxqG4HCmxZp6jgWFhAKYf3AMyJlXKUHsSl5aJBzPmkIPj_xUQEzpvwuKwkaM4EK6156TcWoAv8mBLGhO0Sg1DiOFT5rCxERDhE6gz3CLeq0dNw0ZVm8ie_771hk8M0mNYiQfCPxHGX4vF0WG-kRcIzZMy8OIxapwim-eCZr382GSbaVbesPMJsr1AzKVUy48hj6rkzGsmICsnqbtw45NEC_UAIRkRJCrbzxH2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش رسانه‌های پاکستانی، نخست‌وزیر این کشور شهباز شریف برای انجام گفت‌وگوهای سطح‌بالا با مقام‌های ارشد سعودی، این هفته در سفری دو روزه، راهی عربستان می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/139954" target="_blank">📅 10:57 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139953">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
سخنگوی نظامی انصارالله یمن: ما یک فروند کشتی نفت‌کش سعودی را در شمال دریای سرخ در نزدیکی ینبع با موشک هدف قرار دادیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/139953" target="_blank">📅 10:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139952">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27bd2658b8.mp4?token=fBQDTh1EGQifnWO6i09dtMBduq91pNV60a8P9xGJcjPR5_NZsOt4UOOTMltPdnjJzQVUXM7ObxxexCZARMHzQQgYUe99e0JFU2C-7MOs1Y6MKgwMaUCDNcsu52kMJm4GAUVRGcolxhnQBy9Si0950N4tpKvGckrb7Z7Vt4mFFMVIw8LOEQFLOimuA2ZzsvnL7v3ZBvifHod2wluxjhJuIgxu-Rm_r9AfBWwl2qzTN9ulTRiK8pPR27hDmX5D50Tep47Uq29wr8YugqelOyKRzAUOM5oveJfDeOaFHO6O_ty2p79F26tLr4h1yq9qMNQ1Q2xQkptfXLmWEtF0GW0bMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27bd2658b8.mp4?token=fBQDTh1EGQifnWO6i09dtMBduq91pNV60a8P9xGJcjPR5_NZsOt4UOOTMltPdnjJzQVUXM7ObxxexCZARMHzQQgYUe99e0JFU2C-7MOs1Y6MKgwMaUCDNcsu52kMJm4GAUVRGcolxhnQBy9Si0950N4tpKvGckrb7Z7Vt4mFFMVIw8LOEQFLOimuA2ZzsvnL7v3ZBvifHod2wluxjhJuIgxu-Rm_r9AfBWwl2qzTN9ulTRiK8pPR27hDmX5D50Tep47Uq29wr8YugqelOyKRzAUOM5oveJfDeOaFHO6O_ty2p79F26tLr4h1yq9qMNQ1Q2xQkptfXLmWEtF0GW0bMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کوثری، عضو کمیسیون امنیت ملی مجلس: ترامپ ۱۰۶ بار گفته ما ایران را شکست دادیم، ۹۵ بار گفته ما ایران را نابود کردیم، ۸۸ بار گفته توافق با ایران قریب‌الوقوع است.
🔴
او همچنین ۷۵ بار گفته تنگۀ هرمز باز است؛ اگر باز است چرا دوباره جنگ ۱۷ روزۀ هرمز را راه انداختند؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/139952" target="_blank">📅 10:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139951">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8096a4af3.mp4?token=DMTI_eQ44YVIPUNPyjhuIsDtvoj5rMGaCKswLmiH7zQWCy8UAjmGr5bGXzU1sKkH9uY37nsA6uG8DtY7GEdD02B8sky0MJ0363MkAvCphHgI9_nH6m7i66ZB13P5Wq6K9iEOQGitJ3CrHkbxwpm1lR_0ImOHwTssGMn6fAe3pnRnAUTcT-G4FkruW1Yp0HfyFyhGug9wNWHV2l7fwM4uXy2RJKBU0-6cZm8HRFWvaHIZcyAd-sDUMDLpZUWIc_ItM0uvpEQkOZQlPgLfQB3SCV4LVouPcQi8W5Eh1XtyLiiBL6hMmkacVQDMVDe3jIT44VzplPw-zecAyvogE_03DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8096a4af3.mp4?token=DMTI_eQ44YVIPUNPyjhuIsDtvoj5rMGaCKswLmiH7zQWCy8UAjmGr5bGXzU1sKkH9uY37nsA6uG8DtY7GEdD02B8sky0MJ0363MkAvCphHgI9_nH6m7i66ZB13P5Wq6K9iEOQGitJ3CrHkbxwpm1lR_0ImOHwTssGMn6fAe3pnRnAUTcT-G4FkruW1Yp0HfyFyhGug9wNWHV2l7fwM4uXy2RJKBU0-6cZm8HRFWvaHIZcyAd-sDUMDLpZUWIc_ItM0uvpEQkOZQlPgLfQB3SCV4LVouPcQi8W5Eh1XtyLiiBL6hMmkacVQDMVDe3jIT44VzplPw-zecAyvogE_03DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کوثری، عضو کمیسیون امنیت ملی: ۱۸ تا ۲۵ درصد انرژی دنیا از تنگه هرمز عبور میکنه و تنگه الان کاملاً دست ماست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/139951" target="_blank">📅 10:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139950">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1cec14cfb.mp4?token=eluuGbse8LWbQdD-rfEWuZSPMN8FVHPTLQbbKxozhNU5h-Zr7Z_2K-uaf3XUylcSadx1WlqMo3URqTdAPZydMyriZX-acuzFYtsp2JcF7jEIoOC9xW8JmabbCP4sEcCTw1gbKbDYHjSEivxa6yTC9bvNxcz6rT6vlFXVDneYumDcUVERzX7GsCc30e0yeBNQQ9KWjT_xEoaLWzlUgaCteXmelEjZ08xxbryM9_5I9Js8JJVJstTHVxMv_woS_0wios8YZLCArjYRHB3Cb1Cv6KGB7U47nKDgS-cX_VrNv2EMFwB7d6NEfM0A5lR_Vy1yIQpc8vzQV5zEKoh_DLKzPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1cec14cfb.mp4?token=eluuGbse8LWbQdD-rfEWuZSPMN8FVHPTLQbbKxozhNU5h-Zr7Z_2K-uaf3XUylcSadx1WlqMo3URqTdAPZydMyriZX-acuzFYtsp2JcF7jEIoOC9xW8JmabbCP4sEcCTw1gbKbDYHjSEivxa6yTC9bvNxcz6rT6vlFXVDneYumDcUVERzX7GsCc30e0yeBNQQ9KWjT_xEoaLWzlUgaCteXmelEjZ08xxbryM9_5I9Js8JJVJstTHVxMv_woS_0wios8YZLCArjYRHB3Cb1Cv6KGB7U47nKDgS-cX_VrNv2EMFwB7d6NEfM0A5lR_Vy1yIQpc8vzQV5zEKoh_DLKzPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طرفداران حکومت کربلا راهم سیاسی کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/139950" target="_blank">📅 10:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139948">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q56M-j3jiG3QNI4ZuYInxH1naeOWy0RNHvUzz_t66Hiq8gGjOQrZVHIkubCJcCIIV9w5l2P1EL1Lqgd7IcamRPR2JIZFhsaDXMWB--yZoI_BQZV4_hVIHqt5FlE3cOY_MKV8eEgCQD8GRZDkl-jyb9LJmuh7ndSG_YKO7LgfBuoD6tBTx97U1Gh5hm5-pEzJzEtyDUSHCOLYhFFADTvRYCUVXChcTA3fUKX688gjwjlvf0EcAF-PgL52ov7xgdDzZ2MPXG2RmHSQZ8LVwKvSS6xG-KitGXAE982YCnQq0i3ug1Xs9ML26RnbzjVnnSXfxEXG77xqAjyfZhxhRIdtDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f04fb1663.mp4?token=lrY0_644-EpNnNRmc6nNEX9VfNJQ5bel4ZPhiGX-57FTfr3cniADcAEcc3jG-mjaQvWNuu2YiyedNAJhfIbj7_4VyWpIVQZ1xmwMB3w2Vtoe89-REswcQ77QjLNtqcfWeMHrn2tJ-9LoDWw21YnhLJnJZlBgegx-oIdMHXmVUAdAUY2vDKw_-Y1FDTreNEhXDZulutHRy2p1KNhOH2olJTsvuQ3vWsG_A0VpNKx3ke2UNnstzPH_EnmihhWDeMqku9nmB5Wqky4TXn3Keogdq3gDKGp-pAik_OrzIoEuevTOplS0TNLnCTiiS9RwRsZshlukNS7PD_Z4bvhGet0MFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f04fb1663.mp4?token=lrY0_644-EpNnNRmc6nNEX9VfNJQ5bel4ZPhiGX-57FTfr3cniADcAEcc3jG-mjaQvWNuu2YiyedNAJhfIbj7_4VyWpIVQZ1xmwMB3w2Vtoe89-REswcQ77QjLNtqcfWeMHrn2tJ-9LoDWw21YnhLJnJZlBgegx-oIdMHXmVUAdAUY2vDKw_-Y1FDTreNEhXDZulutHRy2p1KNhOH2olJTsvuQ3vWsG_A0VpNKx3ke2UNnstzPH_EnmihhWDeMqku9nmB5Wqky4TXn3Keogdq3gDKGp-pAik_OrzIoEuevTOplS0TNLnCTiiS9RwRsZshlukNS7PD_Z4bvhGet0MFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
داده‌های رهگیری کشتی‌ها در روز ۱۳ مرداد، برابر با ۴ اوت ۲۰۲۶ نشان می‌دهد تردد در تنگه باب‌المندب همچنان پایین است. در محدوده ۴۵ مایلی باریک‌ترین بخش تنگه، تنها ۳۶ شناور شناسایی شدند و در میان نفتکش‌های حامل نفت خام، دو نفتکش روسی در مسیر هند دیده شدند.
🔴
هم‌زمان، گزارش‌ها حاکی است نفتکش‌های حامل نفت عربستان برای عبور از منطقه با محدودیت امنیتی مواجه‌اند و برخی ناچار شده‌اند سامانه شناسایی خود را خاموش کنند. بنابراین باب‌المندب کاملاً بسته نیست، اما ظاهراً عبور کشتی‌ها به‌صورت گزینشی و بر اساس مبدأ محموله انجام می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/139948" target="_blank">📅 10:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139947">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
یحیی سریع، سخنگوی نیروهای مسلح یمن: نفت‌کش سعودی «وفاء» را در مقابل منطقه «ینبع» با تعدادی موشک بالستیک هدف قرار دادیم و اصابت دقیق بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/139947" target="_blank">📅 10:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139946">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
فایننشال‌تایمز به نقل از سخنگوی کاخ سفید: تنگه هرمز هم‌اکنون تحت کنترل کامل نیروی دریایی آمریکا قرار دارد و واشنگتن به اعمال محاصره دریایی در این منطقه ادامه می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/139946" target="_blank">📅 10:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139945">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
سنتکام: مسیر جنوبی عبور از تنگه هرمز همچنان برای همه کشتی‌های تجاری که قصد گذر از این آبراه بین‌المللی را دارند، آزاد و باز است.
🔴
طی سه ماه گذشته، نیروهای آمریکایی با وجود تجاوز بی‌دلیل ایران، به بیش از ۱۰۰۰ کشتی کمک کرده‌اند تا با موفقیت از این تنگه عبور کنند و این ترددها امروز نیز ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/139945" target="_blank">📅 10:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139944">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/474cba356d.mp4?token=ABfKafzrzNJit4096yNTdej4fzoEO4AmeMK5lew7l1y05V0-yibcMG-fpnt0Oayi-efg-u4J1QemGwOqlR1q7ishuP8T7mvFDXsAl1cszgLYdcWF73s0dHHsn0tyMGDKTTGx3URIWalF1wtf4bpeIf81_hCEUtxvcfXkHO5xCDTVHnOkk8KlKub1aTRt-M1TzhwEdsQLm_11OZfMLqCjfiz8NRUQDwULsO14G0zKJcaifK8ugB6cu5NpyiUGMEmyG5MvTQEicIlpt1QmrFzJPiU5CQVUW4lx1ETxtUY71q-nfXQOZJm_m0HNeWLPOtjrIoeU-ofvIIkhu3sQYYHDjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/474cba356d.mp4?token=ABfKafzrzNJit4096yNTdej4fzoEO4AmeMK5lew7l1y05V0-yibcMG-fpnt0Oayi-efg-u4J1QemGwOqlR1q7ishuP8T7mvFDXsAl1cszgLYdcWF73s0dHHsn0tyMGDKTTGx3URIWalF1wtf4bpeIf81_hCEUtxvcfXkHO5xCDTVHnOkk8KlKub1aTRt-M1TzhwEdsQLm_11OZfMLqCjfiz8NRUQDwULsO14G0zKJcaifK8ugB6cu5NpyiUGMEmyG5MvTQEicIlpt1QmrFzJPiU5CQVUW4lx1ETxtUY71q-nfXQOZJm_m0HNeWLPOtjrIoeU-ofvIIkhu3sQYYHDjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو صداسیما تمرین کردن گفتن «خبر مرگ ترامپ» انجام شد و مرگشو اعلام کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/139944" target="_blank">📅 10:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139943">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
یک مقام آمریکایی به شبکه ۱۲ اسرائیل گفت: «ترامپ می‌خواهد به هر قیمتی به یک توافق برسد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/139943" target="_blank">📅 10:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139942">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
شرکت کابلر برای ردیابی کشتی‌ها:فقط ۸ کشتی روز گذشته از تنگه هرمز عبور کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/139942" target="_blank">📅 10:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139941">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3c611dcd0.mp4?token=k3c8K-4CfHh52FQMOcfeq6h7cXnBzzYhyJsXbHJhRu76DprCt9rEitNuzSOAHEBGJMtegvTXarCMCMGeun6TTVZjuoHew8NESKAOOEOP4Gj8jzW0ovGQR91gx57l709a-By4fo-yQxx6jRLSg0sYx2Jq_xQ0KCaznJ48_Tul7DoR2bLdFZuTeFcXQThfGj9lU5m5b0WE1MDy1V5U5tTDlO7saa6hYkOQLFPZvdIF2N7qCLRhx2sH-TRQBVp1NRwIc4BEJXBsP8vsUJuDe6xH0irw1xK_0YGKdplXwl6v78jmx_rOEsjUYkuxVgDQwBnylAPO4mW-qn126y-yQGXtQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3c611dcd0.mp4?token=k3c8K-4CfHh52FQMOcfeq6h7cXnBzzYhyJsXbHJhRu76DprCt9rEitNuzSOAHEBGJMtegvTXarCMCMGeun6TTVZjuoHew8NESKAOOEOP4Gj8jzW0ovGQR91gx57l709a-By4fo-yQxx6jRLSg0sYx2Jq_xQ0KCaznJ48_Tul7DoR2bLdFZuTeFcXQThfGj9lU5m5b0WE1MDy1V5U5tTDlO7saa6hYkOQLFPZvdIF2N7qCLRhx2sH-TRQBVp1NRwIc4BEJXBsP8vsUJuDe6xH0irw1xK_0YGKdplXwl6v78jmx_rOEsjUYkuxVgDQwBnylAPO4mW-qn126y-yQGXtQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیدا شدن مهمات جنگ جهانی دوم در فرانسه پس از آتش سوزی جنگلی
‏
🔴
خبرگزاری فرانسه: آتش‌سوزی بزرگ در یک روستای فرانسه، بیش از ۱۸۰ خانه را نابود کرد و در میان خاکسترها، ۴۰۰ عدد پوکه و قطعه مهمات از جنگ جهانی دوم پیدا شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/139941" target="_blank">📅 09:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139940">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
سفیر پاکستان در روسیه: کانال‌های ارتباطی علنی و غیر علنی برای حل مسائل ایران و آمریکا داریم
🔴
یک مسئول پاکستانی تاکید کرد این کشور کانال‌های ارتباطی برای حل اختلافات و رسیدن به حل و فصل بین آمریکا و ایران دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/139940" target="_blank">📅 09:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139939">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجار کنترل شده اطراف شهر بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/139939" target="_blank">📅 09:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139938">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
روزنامه اطلاعات: هزینه مصرف آب و برق مردم تا ۳۰۰ درصد افزایش یافته؛ مثلاً فیش ۳۰۰ هزارتومانی خرداد در تیر به ۸۰۰هزار تا یک میلیون تومان رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/139938" target="_blank">📅 09:32 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139937">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
شرکت اطلاعات دریایی ویندوارد: دو نفتکش با پرچم پاکستان که نفت خام عربستان را حمل می‌کردند، بدون هیچ حادثه‌ای از باب‌المندب عبور کردند
🔴
شرکت اطلاعات دریایی ویندوارد، اعلام کرد دو نفتکش با پرچم پاکستان که نفت خام عربستان را حمل می‌کردند، بدون هیچ حادثه‌ای از دریای سرخ و تنگه باب‌المندب عبور کردند؛ با وجود آنکه انصارالله یمن علیه عربستان محاصره دریایی اعلام کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/139937" target="_blank">📅 09:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139936">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
کیهان: ترامپ بلوف می‌زند؛ ذخایر تسلیحاتی‌اش ته کشیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/139936" target="_blank">📅 09:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139935">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/452e603846.mp4?token=sjsNp6kJpHaWGuZ-0uZlJZHESpM2dWqTSV-aDoHfVj8QwnttxeJUVpU7mEExPJeqZI4zzyohhHZ5dwf8w-_Ep_-0mYXeExG5-OB10L52Jm8UJcDWk7lenr7xvNerURdSS2t1HSRfqd9JtYtYC7kSPySoqJsF05WA1PWDgosd54fgCQZgVXAHMK606jcQUb_vCCKaUHTxy_bMhXUFOCWOLCyZbMGb_NUjB1vlwSrSSF-aRYnbbYJHPCnI4HwuSsviQElGCr3EqjJy-udtoWUSjwq6MeIzUTpshgywYaOlDU58ObpQnSNz-s8tqNflya0i01cqioZHYvndUl7ihNIdnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/452e603846.mp4?token=sjsNp6kJpHaWGuZ-0uZlJZHESpM2dWqTSV-aDoHfVj8QwnttxeJUVpU7mEExPJeqZI4zzyohhHZ5dwf8w-_Ep_-0mYXeExG5-OB10L52Jm8UJcDWk7lenr7xvNerURdSS2t1HSRfqd9JtYtYC7kSPySoqJsF05WA1PWDgosd54fgCQZgVXAHMK606jcQUb_vCCKaUHTxy_bMhXUFOCWOLCyZbMGb_NUjB1vlwSrSSF-aRYnbbYJHPCnI4HwuSsviQElGCr3EqjJy-udtoWUSjwq6MeIzUTpshgywYaOlDU58ObpQnSNz-s8tqNflya0i01cqioZHYvndUl7ihNIdnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سؤال : چه زمانی می‌گی دیگه بسه و دیگه راه برگشتی برای ایران نیست؟
🔴
ترامپ : من وقت زیاد دارم، آره
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/139935" target="_blank">📅 09:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139934">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32644a9c3a.mp4?token=iGyIwYEL8M6CGrACJECfs4uYgWFtiZ0GjAVT-eonTmjnI5dgt_zBs4ej-VnZb87APmUbLmwIuTNbeMUWCtyo04CUMKquFiab5CrlHXeXLlq_cRwpC1DTFYz-f_f8YRh0B7sFoPzfx_TDeOdB2nNwaJjQGkITZx_3o7udOxBmpa-lTShKTpcYHft_jO0xwnYCKl4DD3wSQ845d5E-LLCF0f-5qoQwt-n4FJb4W9YAeASvDrDKkhxhReKTNGlxfildF5ulh2yhlE83Wn6Pxv33wjsJ4fQoJPst6qHHO0SSRVL9scdNYybJI7NJHFV7YzAFjP5CadpU8BSX9IMXGGng8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32644a9c3a.mp4?token=iGyIwYEL8M6CGrACJECfs4uYgWFtiZ0GjAVT-eonTmjnI5dgt_zBs4ej-VnZb87APmUbLmwIuTNbeMUWCtyo04CUMKquFiab5CrlHXeXLlq_cRwpC1DTFYz-f_f8YRh0B7sFoPzfx_TDeOdB2nNwaJjQGkITZx_3o7udOxBmpa-lTShKTpcYHft_jO0xwnYCKl4DD3wSQ845d5E-LLCF0f-5qoQwt-n4FJb4W9YAeASvDrDKkhxhReKTNGlxfildF5ulh2yhlE83Wn6Pxv33wjsJ4fQoJPst6qHHO0SSRVL9scdNYybJI7NJHFV7YzAFjP5CadpU8BSX9IMXGGng8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ضربه اصلی هنوز مونده
🔴
ولی امیدوارم کار به جایی نرسه که مجبور بشیم ازش استفاده کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/139934" target="_blank">📅 09:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139933">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ترامپ : اگه ایران دوباره از توافق عقب بکشه، ضربه خیلی سختی می‌خوره
🔴
اوباما سر ایران سرش کلاه رفت
🔴
فکر می‌کرد با پول دادن می‌تونه قضیه رو جمع کنه و میلیاردها دلار بهشون داد
🔴
با رشوه دادن نمی‌شه از این ماجرا رد شد؛ فقط باید با قدرت جلو رفت
🔴
داریم مذاکرات خیلی خوبی با ایران انجام می‌دیم، خودشون دوست ندارن اینو قبول کنند
🔴
بعد من می‌گم مذاکرات عالی پیش می‌ره، یکی از ایران میاد می‌گه اصلاً دیداری انجام نشده و این دروغه
🔴
ولی واقعیت اینه که اونا می‌خوان توافق کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/139933" target="_blank">📅 09:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139932">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
اکسیوس: آمریکا، ایران و عمان به توافق ۶۰ روزه برای بازگشایی تنگه هرمز نزدیک شده‌اند
🔴
پایگاه خبری اکسیوس گزارش داد که آمریکا، ایران و عمان به دستیابی به یک توافق موقت ۶۰ روزه برای بازگشایی تنگه هرمز نزدیک شده‌اند و واشنگتن قصد دارد این توافق را روز چهارشنبه اعلام کند.
🔴
بر اساس این گزارش، در چارچوب این توافق موقت، کشتی‌های ورودی از آب‌های ایران و کشتی‌های خروجی از آب‌های عمان عبور خواهند کرد و هیچ‌گونه عوارضی برای تردد آن‌ها دریافت نخواهد شد.
🔴
اکسیوس همچنین گزارش داد که در مدت اجرای این توافق، دو طرف برای پاکسازی مین‌های دریایی و مذاکره درباره یک توافق دائمی برای کشتیرانی در تنگه هرمز تلاش خواهند کرد.
🔴
به نوشته این رسانه، هدف از این توافق حفظ آتش‌بس میان ایران و آمریکا و ازسرگیری مذاکرات هسته‌ای پس از هفته‌ها تنش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/139932" target="_blank">📅 09:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139931">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
الجزیره: شرکت‌های موسوم به «غول‌های نفتی»، سود‌های کم سابقه‌ای از پیامد‌های بسته شدن تنگه هرمز کسب کرده‌اند
🔴
«اکسون موبیل»، بزرگ‌ترین شرکت نفتی آمریکا، سود تعدیل شده خود را ۱۴.۷ دلار اعلام کرد؛ بالاترین رقم در چهار سال گذشته
🔴
شرکت آرامکوی عربستان هم از افزایش ۴۴ درصدی سود سه ماهه خود نسبت به سال گذشته خبر داد
🔴
«شل»، بزرگ‌ترین شرکت نفتی اروپا سود خود را به نزدیک ۱۰ میلیارد دلار رساند که بیش از دو برابر شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/139931" target="_blank">📅 08:57 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139930">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
سنتکام:
مسیر جنوبی از تنگه هرمز همچنان برای کلیه کشتی‌های تجاری که قصد عبور از این آبراه بین‌المللی را دارند، باز و آزاد است. در طول سه ماه گذشته، نیروهای آمریکایی به بیش از ۱۰۰۰ فروند کشتی در عبور موفقیت‌آمیز از این تنگه کمک کرده‌اند،
علی‌رغم اقدامات تحریک‌آمیز و غیرضروری ایران، و این عبورها همچنان امروز نیز ادامه دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/alonews/139930" target="_blank">📅 03:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139929">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
مهلت ترامپ تموم شد و الان میاد میگه بخاطر تماس طالبان، به ایران یه فرصت دگ میدم
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/alonews/139929" target="_blank">📅 03:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139928">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
گزارشات اولیه تایید نشده از رسانه های آمریکایی از بررسی وجود دست سازمان اطلاعاتی ایران در ترور ناموفق ترامپ توسط FBi آمریکا پلیس فدرال در حال بررسی این موضوع است و هنوز تایید نشده
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/alonews/139928" target="_blank">📅 03:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139927">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
یه کشتی تو تنگه موشک خورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/alonews/139927" target="_blank">📅 03:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139926">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfvPRB5DVJzZkzFqm0sPjYn7hc5TgZxxuPJ9USJOOdgUaMj0gMSZbCS4Xlujc0brBZ1v8CgPj1RSWNR-2kEABmBAqSLJCf17_oE64GdTFFLnsFwSovCkAY4AQ46Q6vsfqPay4hAzlho-zQPDuvGRKbqog7QcjuwoXfu_6-HNJRYsYEExX765dvNYBYbBQPPUnKrCp9wlEdsQ3b1ST1pSrjHiAhwHOfZSdp6CTR3sGx23-lhF0fjk79a5yb9wlYc7iVlQCTgUql8HAJNKZNj7PdwC-Lodqv0e4UlT4L0rqNSm5gThOS-dcgvEnYHGFx0M3fokQbjM0KAofAiCPh7y9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون دوبای
✅
@AloNews</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/alonews/139926" target="_blank">📅 03:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139925">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAajKLwFCgbIP_YOFXghgfF1LQ3o7onQ8_TMCWGnnAjxipjj8lRK235ytHeU-NtMF461NadqkVF--D3507FOIm52Uk5eIwg1eT_ndqyAILaphBxQMrWUdLojXtVK6Utlb1kopVlr2Qrg6PReqiGCttFsVLdfDnYNlkXQmrav_6a7wqs1ki53qZ8apHOWr2lS3k1rao4ULZn0dYULMBOUULKSgJLGvEFgRtIQngKSxMm_9G42YG6hb2NCjqrs8aFk7NqfsuQz8qG-bGJs1Ac8AnaWZ1OEQ9MLyOLUPemowtPJVhcB5OAEATaCQPx3zdhIUEN5vOcNX6rVje5Px0rNPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ستون های دود در دبی
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/139925" target="_blank">📅 03:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139924">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrHWvTaRWVgegaDdy1_g0mdXc4cf2QQ_nMTNPLgNwaxzxvhgHUNBYj8QO1nEOOhEGEW10nMy5shQECsZvM2iJIu0iV4lXl99ERaQUuBvy9Te8r9cY1x0GUP14cua_PsikKR4jLr02AMUy1gyz5e38BA1M0xW4iZ7KP2aeMtXmsDP7ciBKHQTqfk3dwe8qDngKMXRb2uFnmpOxAs5vdj1Yci5hhPGrJQZCKTs94Fj8cy4xei2O8Keef5-FdKWt5KeVDl4c5172H0PPvIR1dPmhYMUSW-77byfPMpa-KsndKfuWoPWH_uzqWe77eBrn_5PVr9JQStYnS-xotrcCTBjBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارشات از انفجار کپسول گاز در دبی
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/139924" target="_blank">📅 03:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139923">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
فاکس‌نیوز
:
یک فرد مسلح در زمین گلف ترامپ نشنال بازداشت شده است.
او متهم است که اقدامات امنیتی پیش از سفر ترامپ به این محل را زیر نظر داشته است.
پس از بازرسی خانه‌اش، مأموران موارد زیر را کشف کردند:
یک تفنگ با تغییرات غیرقانونی، خشاب‌های با ظرفیت بالا، جلیقه ضدگلوله،
و دفترچه‌ای حاوی نوشته‌های نگران‌کننده
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/alonews/139923" target="_blank">📅 02:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139922">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
سوءقصد به ترامپ ناکام ماند
زن مسلح با تفنگ AR، جلیقه ضدگلوله و مهمات بازداشت شد.
رسانه‌های آمریکایی گزارش می‌دهند مقامات انتظامی یک زن مسلح به نام «جینین جان تیل» ۳۸ ساله را در زمین گلف ملی ترامپ بازداشت کرده‌اند.
این زن ادعا کرده بود که برای نظارت بر آمادگی‌های امنیتی پیش از حضور رئیس‌جمهور ترامپ در محل حضور داشته است.
پلیس اعلام کرد در بازرسی از منزل او یک تفنگ AR که به‌طور غیرقانونی تغییر داده شده، جلیقه ضدگلوله، چندین خشاب پر، مقادیر زیادی مهمات و دفترچه‌هایی حاوی «اظهارات نگران‌کننده» کشف شده است.
مقام‌های آمریکایی در حال بررسی انگیزه و احتمال ارتباط این پرونده با تهدید علیه ترامپ هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/139922" target="_blank">📅 02:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139921">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
مجری صداسیما: مردم میگن حاضریم کل زندگیمون رو بدیم اما انتقام اقا گرفته بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/139921" target="_blank">📅 02:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139918">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DPUN77XciA8EJesLC5Up1KclRL7gyYWdPVSbYGDKseYyRNRD1jsZIo5z0b8GCJdiYlZfaGW9vUYbcmMqnXS2h_w2bisNtvN-76TIeNRlyw5zjC4dZxlMkqXtxkGoJJpixP1mwnW4vCiNARsL_LgUJpfBliwbrxW1H2ptilbQT-zXMaMhrOeiKfLL07w9EIhkowPOkoeo6yrKtNdyla4WWsw9cbFeDKZN5wtCnQ7UoeJxwaRYWlI4ICQZKRUbq3L8ACNU51_4__nAlPcjR3Nlap3AD9unz4ylYhHoyGKLKoz5UZpQL-quJxIARTbRgl71XdTKNPWfEugidE2VY19nbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CSbA0-pNhAce2KmNkpArbKmEwPK2GLIYMEwX4GKfEdAJwBN1iIBKDOp5gZgJ4J23thYPBXTp_7RD5TNpJmS-ZI5mRrNuAnedWSqVQF9_bXOAcRAh1TUQUTVYCiVesTt68F8sbkz-3X11Yj5wo9RN9wXyX6juVO_1Ri3iLlzi3i421BzxVwDEkHl6gVUvE9e_nyH6VSYQ7IABRhkn9DHx3-oIAKIOt2cN1jLlTfshdwEG69gVCq1knbZpkoBxc51wZRlDyThOfPSIBzjWKWcatgzIiRWFt-7mJ6ks89UMLuy7-o-q8Q7W3RODmY8cmJLkXjdUWwfyPjPzGgSIawt2GA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d579f85e4e.mp4?token=mz_hNQMBuxgRlhEt8xrPf0R_CXoc9xbmHwepWmR5UFPd5eOd_d4xRkI-fbLHysK51Q_z6lQNGqAwtI_h0tw259x6iUJ5srATc6QfNYc8IcnVp3QMp_a76PgCFwdLK4gCAZAZNWjIYpKdwPfeJFya3K9EWxSdMeD8ZRIYBMo4_Z8Tcu5Gxqz9r2rbN11ybs9EsUDcWNrdTxCjCmD702nFs_ZbwimLUog9B-OLZpu3QFDvIjqyb-UxyWXZSEiLfWHtIK6TuLicsk21o_k8oXrHLRjemOe5zd-qDE8CzHPRihJs2SS0nvlZmLyJ9PW5xZEz6WLjM4kx3YSFNKrQpyM2wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d579f85e4e.mp4?token=mz_hNQMBuxgRlhEt8xrPf0R_CXoc9xbmHwepWmR5UFPd5eOd_d4xRkI-fbLHysK51Q_z6lQNGqAwtI_h0tw259x6iUJ5srATc6QfNYc8IcnVp3QMp_a76PgCFwdLK4gCAZAZNWjIYpKdwPfeJFya3K9EWxSdMeD8ZRIYBMo4_Z8Tcu5Gxqz9r2rbN11ybs9EsUDcWNrdTxCjCmD702nFs_ZbwimLUog9B-OLZpu3QFDvIjqyb-UxyWXZSEiLfWHtIK6TuLicsk21o_k8oXrHLRjemOe5zd-qDE8CzHPRihJs2SS0nvlZmLyJ9PW5xZEz6WLjM4kx3YSFNKrQpyM2wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات بسیار شدید و بی سابقه موشکی روسیه به کی‌یف اوکراین
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/139918" target="_blank">📅 01:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139917">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNmFw_CKOEkzSdFDazXP8onT6ZXHQxlYnUP3jEAFlwKtylEo0noVinM3ocCZ91pOBJQJJ0jNaNBJzTxyz6gIBi6hVz-f7hN4sUfS9XHveVesup8ge0He1pgkiHkq36gPXmOX-cJxGTYVGCbJ80ZK3R5n8Cs86aLbyFVgzkIEMBJ5epkaSkNcZp0Q5dWDkW7sw5k-MzjUAcslW_Kd6LbESGo-77lZHhOoo2fP6sPlLGyyK2mizE0CSfnq-PU_vehGO8IsSvG1oJx1qvjBCiG_vjXW41DeTTRdWBUcAXoqqWxMPZ4mrQ5NqNLUnMH4UkaFX9BwonTT0lDIl7nfE9ajcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هگست، وزیر جنگ آمریکا، خطاب به CNN، درباره کمبود ذخایر موشکی
:
اون خبرتون حقیقت نداره، خجالت بکشید شرم بر شما
ما باید خیلی بیشتر از این رسانه‌های جعلی بدمون بیاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/alonews/139917" target="_blank">📅 01:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139916">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ارتش آمریکا اعلام کرد طی سه ماه گذشته، حدود هزار کشتی با کمک نیروهای این کشور از تنگه هرمز عبور کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/alonews/139916" target="_blank">📅 01:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139915">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
خبرنگار المیادین در اسلام‌آباد به نقل از منابع اعلام کرد که در حال آماده‌سازی یک یادداشت تفاهم دوم هستیم که به عنوان پیوست به یادداشت تفاهم اول خواهد بود و تنها به تنگه هرمز محدود می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/139915" target="_blank">📅 01:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139914">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
مهلت ۴۸ساعته ترامپ، ۲ساعت دیگه تموم میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/alonews/139914" target="_blank">📅 01:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139913">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b407081b1d.mp4?token=Iw7sZoGO9S2U7fOYDDgXlrMEMejGOtbarsuGPq-zNc8WTcyng9x9FM5oOHW914MUVaEp57QLRbQQ2DfMO6t50mKMSoDFPFEM-4fNkk0vwalAjDS6lf3X1KzyplOtPfEfdkvY2w_dxLKjoxHmyd6rN2X0NnT9ccojCXmONKIef_gSsTBEXkRBuswo5aSx0bsDi3yFf8ge87PnSP0JfdsrNdIRON-cJ3d8gg-HYqEwPRa5GHRvlT9GOsMDVFQsz1cVe8HBbKkSkdLqIPOkdtYk3ChmdosWFUurZBI1CIboMIZdpJW9-2sJ1puhvPicMFJyErgCdm0b83iu3eAyWDOyzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b407081b1d.mp4?token=Iw7sZoGO9S2U7fOYDDgXlrMEMejGOtbarsuGPq-zNc8WTcyng9x9FM5oOHW914MUVaEp57QLRbQQ2DfMO6t50mKMSoDFPFEM-4fNkk0vwalAjDS6lf3X1KzyplOtPfEfdkvY2w_dxLKjoxHmyd6rN2X0NnT9ccojCXmONKIef_gSsTBEXkRBuswo5aSx0bsDi3yFf8ge87PnSP0JfdsrNdIRON-cJ3d8gg-HYqEwPRa5GHRvlT9GOsMDVFQsz1cVe8HBbKkSkdLqIPOkdtYk3ChmdosWFUurZBI1CIboMIZdpJW9-2sJ1puhvPicMFJyErgCdm0b83iu3eAyWDOyzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری هندی تلوزیون: باید تا ابد با کل دنیا بجنگیم
🔴
پ.ن: خاک بر سر مملکتی که یه هندی بشه تصمیم گیرش
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/alonews/139913" target="_blank">📅 00:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139912">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ترامپ:
بازار سهام به بالاترین رکورد خود رسیده است زیرا سرمایه‌گذاران متوجه شده‌اند که آمریکا در حال برنده شدن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/alonews/139912" target="_blank">📅 00:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139911">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از دو منبع
:
ارتش آمریکا نزدیک به ۸۰ درصد از موشک‌های رهگیر سامانه تاد (THAAD) و حدود ۵۰ درصد از موشک‌های رهگیر سامانه پاتریوت (Patriot) را استفاده کرده است.
🔴
کشورهای حوزه خلیج فارس نسبت به کمبود سامانه‌های دفاع هوایی ابراز نگرانی کرده‌اند؛ مسئله‌ای که بر توانایی آن‌ها برای مقابله با پاسخ‌های ایران تأثیر می‌گذارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/alonews/139911" target="_blank">📅 00:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139910">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f44155df6.mp4?token=lAzk6kP994FWEI_6Drk7NkPLRqQa2HwmfUAxHspEQQN_0OhFWec3NijUXIj0cFUBQya9Grhi_-25ty1eyCYuE4HtO30mM24NhVolrMn96boPO5JV6uBn18fkf9V6szmJRWhSUmkVTPeofBxxhka1JUjB2aAoBdJKnfuBM6LBBdHY6B-b86qy8tWqxCYDfrHOOE0h6kyEC7HGdI0YoH_jFLl194-yA-RseRlT82LTCT2E_D5jRpJNp2Pp-bQFQX3XUsI-xVuW8YWD_6R1B90jhsVUsVNGUhQOYn2mWTgVy0dYuR0yiP13RnNuVwkFxlSkB_NftXUq8b11mQSXi_cw_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f44155df6.mp4?token=lAzk6kP994FWEI_6Drk7NkPLRqQa2HwmfUAxHspEQQN_0OhFWec3NijUXIj0cFUBQya9Grhi_-25ty1eyCYuE4HtO30mM24NhVolrMn96boPO5JV6uBn18fkf9V6szmJRWhSUmkVTPeofBxxhka1JUjB2aAoBdJKnfuBM6LBBdHY6B-b86qy8tWqxCYDfrHOOE0h6kyEC7HGdI0YoH_jFLl194-yA-RseRlT82LTCT2E_D5jRpJNp2Pp-bQFQX3XUsI-xVuW8YWD_6R1B90jhsVUsVNGUhQOYn2mWTgVy0dYuR0yiP13RnNuVwkFxlSkB_NftXUq8b11mQSXi_cw_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چه بر سر این مردم داره میاد
😔
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/alonews/139910" target="_blank">📅 00:25 · 14 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

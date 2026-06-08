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
<img src="https://cdn5.telesco.pe/file/VgNbf-e1ZHXDCRREoYooY-RC33BOoPlCj2W1jKXwT58HOf_-KZQNoJYpHJ9IMm5zr2kIbNdWaxzh_icZ3oe3DSyZJQKuT1HYmRwWlJJUYZ03VAEyesLwB-P2ep3t-KRO3LuyYSBvwa-qXVQfzRycYn5tm1xEhuLgviO-JabNdBbNAudgvMBU6c8rzK6o0FtRPvd-v0zUziZT_YTINCDe1G1xyAEChC08UbQFaBZdaPv6PkGMfZdre3Hyx9csnyZmr9pdzXvf1GguUzfBVcmZc_oTG0Udc-Tjgs9mv2BUqX6EwG8vecQR5fY3W6MKK4K-hDClRrzedsv9n7mE67iCwQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 270K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 14:56:10</div>
<hr>

<div class="tg-post" id="msg-91541">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XjFnzRzehCUy2niFR0je9XZp6Bz1g6YG3JsZYYAZ8113u5rTa7rCiYdzFNwudSbIkLIgxDkfVDyDoVUC361gGiboVxLLNc2zTs6Mw3b_grxtqX1AWlm3nD2wsWHITU5zgCxwwSptX3vVF9uABkOYorvYLcIVmzNuPeXnW7kpA1kwJBB9fJip5HW8Im1x97ACCOo_cgOM2LVJE2nKEiGAewPEpt77X36zD7gdITr0iJ1S0jq-L32vwsAh4Mmmaz4NHKJFpKc-OJ61E5m2MGgt9fNIYyTl0py0a1Z9oOCHE9Zty3_LNaIT50ktyySSZN_17zwnyPa4ha6Bp9DCkm3V-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BbuUUxX7JrPsjKPcT0tFRh7CGER7AzGcgsDMhoASg78SLTrVEehRiroy3gmbJzV5gtAhMvudRBJI4v0EaJJR2hebsxkt9hADIm7BTByBLFuqklveocxo2xJB5tePzzjuEAuXQ6pqAkXimfRXLY-3Seh_ZraolJ0MVyLqBvX-LbG4xLe8ZioaKg_bY0-Q5OULUh0VjW6tw-s5kPxgibPi4mgFcLzSQHljPuKanOnF-gTBcU1K1dKCFLHw38cc7roM21nco0pbI1FN1fKrEERE7dtN40uY_GS1_Q2Pj8EITX5vhXauWX9JgZonsraZBDcqYqWNWzXTWGB-6-ohMpiXtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇮🇷
#فوری
؛ قرارگاه خاتم‌الانبیا: پاسخ دردناک داده شد و پایان عملیات اعلام می‌شود
🚨
🇮🇱
#مهم
؛ اسرائیل هیوم: اگر ایران حمله نکند، اسرائیل هم حمله دیگری نخواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 309 · <a href="https://t.me/Futball180TV/91541" target="_blank">📅 14:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91539">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
فوری | قرارگاه خاتم الانبیاء:
ما توقف عملیات نظامی را اعلام می‌کنیم و تأکید می‌کنیم که اگر حملات، به ویژه در جنوب لبنان، ادامه یابد، پاسخ ما بسیار قوی‌تر خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/Futball180TV/91539" target="_blank">📅 14:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91538">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDeTSxf5UrJ3jkifW16vGGXPF3U2K6nUnd8L3SENOHr2K3YSCcoqiIXOXz3e1dM0zDPxV1eAtqgaAYfi00UHdHYBb1gvruhFFCEhf4P8M5tPffxKFzEeJ9K9XdOkA0ZO4SxaSvjOvCo9CNR-d5f3DGuoCWVtkFOlUGMign4ODgCZOA0iIR0bFP08MvGTqH3huhqaPH7SNKrbkfpNkyobcvqp7lULNrP13EK_nipmdc_98990gp3sOHDlgjildnITHVm0c5rHk-XUyfk-UEuWHxW7qfEdeY34cdEuq2DT2oHMg3CXQHfRp51JIci0MveXqXffGc7z-oogEyUWs7Hr4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حریف تو من هستم نتانیاهوی قمارباز
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/Futball180TV/91538" target="_blank">📅 14:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91537">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AElQfbLda3N1FWYg1qnsqeYVcbaFJZ_9fIqcx8ES_Uoc0fzUazYZ_uwd0OaEDoj5LrT1t1bg6gxUO23FT3jj-uMnV3LPZmXRk5NbWMv5IFFlkTvErY8AJasXl2XTcl6Y0mzqZwKuzMHw_j3uKeHLOWpDwVcun7goCpbmuhi7eFMskoVMdbqbXeMorqzoLjxGa0c7hIKSEI9f9pz9DsZjMzzE0faDRQoj5Ngu4A-Ux93etPLbLT5JlWVVRFEc6g6losORwhcLf063kl-5i2OcgNykfgoKGjf-Id7RqeYVwUb3hQg0XMtGr2GyjHGD77nqVmuyrDol9YsNjPm4O4dqvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
‼️
🇪🇸
هفده‌سال پیش در چنین‌روزی کاکا با رقم 68 میلیون یورو به رئال‌مادرید اومد و‌ در 129 بازی با ثبت 29 گل، 39 پاس گل و 2 جام این تیم‌رو‌ ترک کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/Futball180TV/91537" target="_blank">📅 14:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91536">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/662d05e7ae.mp4?token=m3gvvAOACuUKlyoprIf6i2tizh0CNslTouA_S7p7rpLqRXp01y1Pq38El2fxW3VAbQqcfjD2RUffLbgiVEXv_idxBBB0i0jBijPk3QoMDKV97RQZjaLFoptT-KHHoWuz8y-_wuwnuX0I7yowIIQzJBlhCCwQYwHaHwHHE6IVsVbhwVOB16t9PtRyMGaEviFnO6gWOzFzk85rSWIIbiwEpxIEOjRhJofJjkQhWBklaK1cQh9YgfOsNV1p-8jHl3X3BSLF8foge9UmCSgwjvaVzF3jbCmuD_TUq6bxyKEJhOecnHEzbKNsSip-tjjf1CPp_ve2XtU-URy0J3U8LooMsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/662d05e7ae.mp4?token=m3gvvAOACuUKlyoprIf6i2tizh0CNslTouA_S7p7rpLqRXp01y1Pq38El2fxW3VAbQqcfjD2RUffLbgiVEXv_idxBBB0i0jBijPk3QoMDKV97RQZjaLFoptT-KHHoWuz8y-_wuwnuX0I7yowIIQzJBlhCCwQYwHaHwHHE6IVsVbhwVOB16t9PtRyMGaEviFnO6gWOzFzk85rSWIIbiwEpxIEOjRhJofJjkQhWBklaK1cQh9YgfOsNV1p-8jHl3X3BSLF8foge9UmCSgwjvaVzF3jbCmuD_TUq6bxyKEJhOecnHEzbKNsSip-tjjf1CPp_ve2XtU-URy0J3U8LooMsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استاد باقری هم سایدشو برای جام جهانی مشخص کرد
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/91536" target="_blank">📅 14:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91534">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKo71zL6MISRcGViopOA0y13wdbT6eAUQsA7vk5-mpLn7FQMVe2bAvioSJipG6LqJERBNT30W0_rDcvWWawCCMeEe5J6ZY520zM4cDShgKeh55DRDrK69eGpF2NGYwq2E8El0gaF2IZU42Wv6cPw04HTB5e0g8PN1jLI52tpd8aQpe7QzXPJf5zDaEcU00M8v_taHXqCy8fVTze39te5IsIYZ_VzcrqL3WP21rHe85UY9YnJOSm4BmzbO8A9cBC8qE3BkxSU8fDnpC0_7cnr-Zpw5PRjQoM4hdYIGzX2bymjL0ldnSEaFNWdXloeNaRCuAXpU2qwn2xHD5JVBc0-VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا یا من پولدار بشم یا دنیا جهانبخت تو روبیکا و بله چنل بزنه.
واکنش خدا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/91534" target="_blank">📅 13:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91532">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPrP6Udh5H4jOdn117UX2yNH9S-sRou3kxbTjB_foz_BqoNN4DzMsfermfUodoRjIOibYbCVmPl_4MujN9ecG8AgtNOfbSNjWSSTeB6-B9Jc255-bMoKzyVomeLcITB8csdLqnQ0gofl_Jao77BAvvUAbzWGvMrZfcN_qEy2Kg1xs9vH0zXOWzOYxxkC9lNpLSAu3eMVOyfxR8iDaUtl0howk212RFYT0kIOWdJh0A9vLsnHZ47jmSQEnnDfA9iVnhAmExD4QJIhb6hfELOKaN1mvu-CTxDSrDFICkkD8I1Aa7v-C-7sLpd0wUWqclEW6465EvvNLOScgGGiRFyT4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
⭕️
🚨
تنها 3 روز تا شروع جام جهانی
تلویزیون دولتی ترکیه مسابقات جام جهانی فوتبال را به صورت زنده و با کیفیت 4K و Super HD در ماهواره ترکست پخش خواهد کرد.
TRT 4K
TURKSAT 42°E
11767 V 15000
TRT SPOR HD
TRT 1 HD
TURKSAT 42°E
11054 V 30000
11794 V 30000
تلویزیون دولتی ترکیه با بهره‌گیری از تجهیزات مدرن پخش، استانداردهای فنی بالا و جلوگیری از فشرده‌سازی‌های مکرر به‌واسطه دسترسی به پهنای باند مناسب، تصاویری با کیفیت بسیار بالا ارائه می‌دهد. به همین دلیل، حتی در مواردی که بیت‌ریت برخی شبکه‌ها تقریباً برابر است، کیفیت تصویر TRT بالاتر به نظر می‌رسد. برای نمونه، شبکه TRT 1 HD با وجود بیت‌ریت نسبتاً مشابه با بین اسپورت، در بسیاری از برنامه‌ها تصویری شفاف‌تر، رنگ‌هایی طبیعی‌تر و جزئیات بیشتری را به بیننده ارائه می‌کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/91532" target="_blank">📅 13:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91529">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ملی شکن⚡🔥.npvt</div>
  <div class="tg-doc-extra">2.3 KB</div>
</div>
<a href="https://t.me/Futball180TV/91529" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚨
🚨
🚨
✅
به اشتراک بذارید دوستاتون وصل‌شن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/91529" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91528">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJG86fHanvps-mGeCENDQMlgFA144h8woyCWCbqAY_uRX3IW1e5HuyivuGpqmLBxen7ZiIIFYw0PYfSDUq-LdiM9FtHfHHVK9hArzTofussfqPS3iaWp1T1rIafFVkZ_z5IiCcqBaMeyMR0rWagcYCuiWtJwqjRULHgfJe4UACnNX0xSac8xQTr8x41-0wn8Mxc_BLk3yqzq3n6-QrY5G4FRqmGAdl8oJt6TeglRcUtKe668CCDDLB2EY05l0rqDWywMwfwNDSoZNw-kFRDDCRZaHBUvMYejpY4IOE7LhU-2tjsWd03lNkmwuxlK4VCaves5y96TlaIQuyv0kk20cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سر صبحی خواهران منصوریان اینجوری به شکل عجیبی به دفتر رئیس فدراسیون ووشو حمله ور شدن و خیلی وضع بگایی رقم خورده
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/91528" target="_blank">📅 13:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91527">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
فورییییی ترامپ:   اسرائیل و ایران باید فوراً «شلیک» را متوقف کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/91527" target="_blank">📅 13:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91525">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
فورییییی ترامپ:
اسرائیل و ایران باید فوراً «شلیک» را متوقف کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/91525" target="_blank">📅 13:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91524">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سازمان ملل باز هم ابراز نگرانی کرد
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/91524" target="_blank">📅 12:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91523">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
تا این لحظه دستوری از سوی شعام برای قطعی اینترنت صادر نشده و شاید دلیلش این باشه که حملات دو طرف بزودی با میانجیگری برخی کشورها متوقف بشه و‌ دو طرف شرایط سکوت نظامی رو در پیش بگیرن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/91523" target="_blank">📅 12:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91522">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3D9e62PINlq247hXVkNocjZt5aE7CE1-PoRclpf7e74I2NolueQ_EOSIiSK7qSUuvh7fB-ZGfOPEixfiWsQUYlMkWvjLeDH1jB0UFNoLNzGlrCtaKHy7pvxPEWfK5p_ZOUMSgIFvRVhksAFga8bOYHTiKuzamVvi8405MEFjBeYzYm9wIzIDBNtvHcqwlv4VK5fekuoxNeDENel6ffl3NiaWoASrBMnWhKAC3TNFa2dwYoYLentIayMEa78vw_g_CBAR6mgrTYMX5HMYavlqldxwn9-n4JImaOxqO-NlHTJOx_hg2y7iXJNk-llJEg3m75TZQC6XWQHrGGwYxGamQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عموی ترامپ الانا زیر پتو کنار یا روی زنش خوابیده. تا بیدار بشه یه حرکتی بزنه یکی دو ساعت دیگه زمان میبره. احتمالا این سری علاوه بر ایران، کیرشو سفت حواله نتانیاهو هم بکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/91522" target="_blank">📅 12:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91521">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
تا این لحظه دستوری از سوی شعام برای قطعی اینترنت صادر نشده و شاید دلیلش این باشه که حملات دو طرف بزودی با میانجیگری برخی کشورها متوقف بشه و‌ دو طرف شرایط سکوت نظامی رو در پیش بگیرن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/91521" target="_blank">📅 12:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91518">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmDrbWnlZJEF8EZoUEgnbT43-kKIErSj7PTHjWCXu2KKvH1E2oszV0PYNc0fWsqXPFQpYnJytfFDB1rFXQu6ZKqhB0Ct-M_-E0_7roHOLwq6TME4p5MssU_7Vzkr146VtC9KvjDhV1Hepxnc9lfgGzYDEIhIF1RRvIJcge4VKoXGoPC-3y6IGmV2NT9usZ9EboYmNNSlVnhHjcDW5f2NfXZ0oPTK8KKXNT_BuRFfmHiwk4r90KTqqYKI60RlfNQGSJCxB9dai7-rBqZFrGIt13qsuLZWZJi6BqoKTZm6iM5dju7kG5w7NQnh8M5x-0bW5ZDPiaOipJFfkhRoVAsLCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
#فووووری
؛ عبدالصمد الزلزولی ستاره مراکش بدلیل مصدومیت از ناحیه رباط جانبی جام‌جهانی را از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/Futball180TV/91518" target="_blank">📅 12:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91517">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3302fb4017.mp4?token=cq6UcyB53PwegMWf4y7xA4ftSMJwZCgXGDEA4P-zKz2DLPjlyZokQb5JZdP-X592lZG9I0Z0PqF159P-FoT4KcwIOZaV7n_fE10d5iKZm1aKCAHiHRBpxCas7oUYBZRz8wSLZy025OmOQZFXMj3fUnG8E0aSbduJ36Va1AtrLJLH1tfFhmV7-HibSmz34AWX0rCYD7XETG-u8K27LKS67gxj395RaKtMcCyIg2qxKcztX9Pm70pJz_U8dZL9C8CPwpZjqOZgjtOJWIgYs1mECkKyD-ZgbtSsa4ANHAivqKIUFVZdhG4HC_yU9umbhP-hD3ZHS-kxcBkezHHZALzHKp7j55VT7ZfqWNPXooStaijeLMxvpEHrx7FU_3gkidz4leDjDs8Z2guRSAuVbleTrCeuIIk2rFz3AWkkf0hgv97I_p7fVuBd9HoExXtCpTbeFODkfC_KbYkmEpN3nT_sAMfruE12qYADPfxH_wAgLCTcORmBGk0Xl2UdwuzzYf2zf7kyQwkceYYWgHQJKJn8ihbEqzRn2UzgUxXF3lVoXNou5Et5yk6Nh0VRwC-YbowaHRSveKDRBu9Ph-RklEGVKO9oBWeQvX-O_gaxpWatwA7Ygt9XBN3qycO1Qte2dvcM2Pmv2IPtaeyMX7nS4l_pMFz3NgYsm7W_DX6IfjFt8Oo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3302fb4017.mp4?token=cq6UcyB53PwegMWf4y7xA4ftSMJwZCgXGDEA4P-zKz2DLPjlyZokQb5JZdP-X592lZG9I0Z0PqF159P-FoT4KcwIOZaV7n_fE10d5iKZm1aKCAHiHRBpxCas7oUYBZRz8wSLZy025OmOQZFXMj3fUnG8E0aSbduJ36Va1AtrLJLH1tfFhmV7-HibSmz34AWX0rCYD7XETG-u8K27LKS67gxj395RaKtMcCyIg2qxKcztX9Pm70pJz_U8dZL9C8CPwpZjqOZgjtOJWIgYs1mECkKyD-ZgbtSsa4ANHAivqKIUFVZdhG4HC_yU9umbhP-hD3ZHS-kxcBkezHHZALzHKp7j55VT7ZfqWNPXooStaijeLMxvpEHrx7FU_3gkidz4leDjDs8Z2guRSAuVbleTrCeuIIk2rFz3AWkkf0hgv97I_p7fVuBd9HoExXtCpTbeFODkfC_KbYkmEpN3nT_sAMfruE12qYADPfxH_wAgLCTcORmBGk0Xl2UdwuzzYf2zf7kyQwkceYYWgHQJKJn8ihbEqzRn2UzgUxXF3lVoXNou5Et5yk6Nh0VRwC-YbowaHRSveKDRBu9Ph-RklEGVKO9oBWeQvX-O_gaxpWatwA7Ygt9XBN3qycO1Qte2dvcM2Pmv2IPtaeyMX7nS4l_pMFz3NgYsm7W_DX6IfjFt8Oo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
سر صبحی خواهران منصوریان اینجوری به شکل عجیبی به دفتر رئیس فدراسیون ووشو حمله ور شدن و خیلی وضع بگایی رقم خورده
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/Futball180TV/91517" target="_blank">📅 12:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91516">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
تا این لحظه دستوری از سوی شعام برای قطعی اینترنت صادر نشده و شاید دلیلش این باشه که حملات دو طرف بزودی با میانجیگری برخی کشورها متوقف بشه و‌ دو طرف شرایط سکوت نظامی رو در پیش بگیرن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/Futball180TV/91516" target="_blank">📅 12:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91515">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کاش یکی به این کصمشنگا بگه اگه با قطع اینترنت فکر می‌کنید اسرائیل حمله نمیکنه و فیلمی منتشر نمیشه از خر، خرترید  اونی که بخواد فیلم بفرسته نیاز به نت کسشر بین‌المللی که به خرد مردم میدید نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/Futball180TV/91515" target="_blank">📅 12:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91514">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
حمید رسایی: از آن فرد بی‌خردی که اینترنت را وصل کرد در مراجع قانونی شکایت می‌کنیم. در شرایط جنگی و حتی پساجنگ بازگشت اینترنت یعنی خیانت به جمهوری اسلامی!!  +منظورش مسعود پزشکیان هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/Futball180TV/91514" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91513">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
حمید رسایی: از آن فرد بی‌خردی که اینترنت را وصل کرد در مراجع قانونی شکایت می‌کنیم. در شرایط جنگی و حتی پساجنگ بازگشت اینترنت یعنی خیانت به جمهوری اسلامی!!
+منظورش مسعود پزشکیان هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/Futball180TV/91513" target="_blank">📅 12:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91512">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
لشکر10 سیدالشهداء سپاه کرج مورد حمله اسرائیل قرار گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/91512" target="_blank">📅 12:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91511">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_s05tQ1uuThu7ygpHliy6aMZgJLAEuQrIk6FKBTY3thNJ5LOVoD440VHj6VRiS4_vN9xsoco0ASUUyhn3T7jlsqCWXklHESlaqmK2Sl6rcMF3JCiGLSQtLAwJZBKpqDJH1X5UGsmzxZ7tjauaPpNclISC9-hddayy1pI_ARHOv7s24xvIAKKDJ6ufeP8aCiUQ1u3XoMxtBdZVWjxhaW2tFB65wHCSjoNJY0MOGH3Se0aRJjXv8vzegu1vrH6dt96bIPFDwJ3F5rWV-rlQYxBH01DcmHOVVsLexoaYyRoATPdr-6XzBeKm2vOjUvUm2PY0k691TdyRNvKUi_r9m3mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب ایتالیا در آخرین جام جهانی که حضور داشتن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/91511" target="_blank">📅 12:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91510">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
فوووریییییی صدای انفجار در تهران!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/91510" target="_blank">📅 11:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91509">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">هنوز آتش بس نقض نشده!
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/91509" target="_blank">📅 11:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91502">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RAu1N3O1gNxdfu2C7OIv8kE1Oyu0fdg0doF7y0b_g4kYlhHSVKwoO_tcF9D8MjuVNDdbanolNF5LRP0niLyK-tboTyN0af-R_cgJDFIKxL7pR8g_RI7a6Px3FCeNCOpCLWuBYKAPLQNCdWsvobpFvKXyUGI6EMnKPpkwbOP9tEeZAwEZc7tJ1hHtt2wM7RNaulIKLgaWumvINT8iiX8DJE0FI6PjkEqx7wsjzUtcs1ok9V7mQBEqYcj0fIj1O4iwUN8lwjTgFA5DBbG--6YBE_-ZrwuQuMTUsVhpKNFs2RukBZPVkXmyAADx528_bTHO8hySBEPDnZZTfspdngt1rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a-VJuZwaiHVonNU10syijPUR2iFH340xXNWslavzYSWTfrCy3bDp5fMy0Zm4KGCc-vjEOYW3ixbzyuvBZmGv-plmq44Uu-10pH4sRDofg6trFkrhUBbAifDmuxIrTxjSpEp0HFt2qIyMqdsaaqGhS_qquuowhZT2vgrOedXadBQqlGUqEHg6lPEk_bYcikwxfIuTB3ugZYgXtMuRCjIATJBMVzs_32UW5Bc-rC_VGiv3_BuJxXwnjQy_2qbNZ7vSEQsgWL3RYTGOpyGIUMiIYaPq_fYadEAjehhtWCZ6LTntUq7du3yVSX_UU88Zi2hQtA_czaxb13vZvJThOK4t3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZA0Mn3c0YgcOQBmsdstrwe-5nsSjLYv8CMIfux9pOVCBISvc9v9dVC2H9CaM6yaLYLPkwLwWe7vW9qGcRWuHDw9ym5dHRwIi7jVeBdLdsaEbiMRTjWUzbcjqd5Ron0jLMgiX_kqwqxjqGKxTyWvEiYfkR6CzFIQruzGmTg1tB9ExC_-CcN-x4HAJotJ01w838MRFCxHM3NUE4-0fAzmWujqPRTPodHhn5wO0ZPYFrt3dO4uZFSK6fvDdtWSdseHrvU2gSD0ps2oOYkA8LyKHVO4kot-kE2NZd6KssI3wSH16tXxDBX6QIPlHNyG7HIPWwqIefgF8uMuM8aB9XFIvpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MP3lJo3DwungLjuo9xjvx2quGLUwSmYIj6es29_Qb-yiqNLrZnQ1SnwHUIq-ln0Eh0cUzmdTr1ZxXPoGXrOSsO1TwCymBKLriX8O1F0cgfzDcn1uSeSDlGBSCn03f5-EHGLX7sPUQBSkj2KceYrvf88TaAOsUu7K4atazndB-KWI480VbA3L7OqfFmNbP3C3Rg6k2sALy3WYopSuC5iDCJ_5hPeGDcoi6Wwz2zb7lnhgbAEvnnyflXd-LrYUNUnUCgWcrtvC6CjPFlIxrC7L5EZzWVAje4cHiCMFEhNALe5ALAG7vVv1wMJMrkrL_Yp4LcaJ24Sl8KrwJBNF1fmx-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g3qz0mE4yD0Ap5zckNYeBuzhnG_R-Au13rRqIHcGf-XGMo82YtddThk-4Z99ys96lKCIbprrVBQcJ8ceofivcYyzUF7SG55KlrEv_WkupdDlsrw_xfxMwZJgDp3Bho-Ms-Bx0QZPK-GbB_sIyOquNgQii9y9_OZjYGQAQPkl99511YiaOiTxCuICwQVU9ZutvL8fgEBZlMzTxQOLuB256lTcx3kT4mAm9G62SfpU32yW2mKMES5hHk8Tg7EyxAE_JJcBfLVzlVLgXusZzk3UO3hdpuHx4J_0FVeFS2wZH4CXU7CnR6eGAkAHfDiXGEg1SWMLbpBYqKNFkKLdCx-T6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ceUL3wRPEv6zEWCgFJO--AQRytzeEKZsxTBtLGzWvT-2FnIt2uoPXNf9wRidYL788y_ufUDD_KjSOfLAQOTlqhex9JNU4E4K_85Ycqr1iJmeWzzTAAreBO5_nVQ35uMa5-AXl6MvGI2ukYR2446Cf8fg8GTWbifL0vgJVyXdRmG9k1N0j6T0v7DaaCZCwOurKl-J-YUGrG0rPhB8jFVyFvTHDBuPgFOjV9euJFa5n720hK4rcdes2FUbqNlUs_ShlHiH8VjkkpH7wPPYHVf8cGYKM9jSF10gPp5kFx0WIlJQhSVUipGgj7SK-10aaQFuHk7de9SRH-x1fFkXV6lZcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g1tOKVohpdgs5FvRGQPdTuO7DDsEtmpsJQoELQ90zHQ90XoZEh8j0uO2prz8C9fFRpn7QFiXtYuH586W6doK6PjEHwWHxG-XNliY-iibt9US_5hjQfD3T-EusqbQCRxWzjiLAgZMHKfPelrrNUWGjdZUruHN9zdlykcH7mtZnOk0g8tqyyBz3RWZXpze4A3U190EzHXILpPbPNy5h1qiOFDxZPZrdio4GRnH6wdhAmU3t-LblyN4A7VVGa3I_OVbre_jmshELGGpk-hAISQIIj4IumeGArkzI5UzvY2Vohj9FBD-gEYtPRIqZAk-Q6qYr0iJzu995sQFxUhO9TJs6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚪️
تیم افسانه‌ای رئال مادرید 2010/11 و وضعیت فعلی آن‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/91502" target="_blank">📅 11:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91501">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
فوووریییییی صدای انفجار در تهران!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/91501" target="_blank">📅 11:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91500">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
فوووریییییی
صدای انفجار در تهران!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/91500" target="_blank">📅 11:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91499">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jd4sfeevlJzPkeNE4UFq4Ge8dSw3l3CSPgfps_7QPCpdxHtgGXV0zLYI-RXbdrBFtIjCJ7JF9Jtpo8XVWfvRI1Ws5ihQZhqzWy3Cr3dLdRrWHs1Q9SgnBggdNU_Kiuhd11dZjwDNZ_F6TcbaNX0wrY8ORkqHLM27GJtTzn4gpXPDZZ_Zmha1sC3QsobnPpAkqJOd3IQ4xLkRCCawfdbo_wFsZstvih5javcf5xCS7ckT8f6X7ki-EW4la5gSnYAV5DXDeEBAqO_uDMnUcvBFItXXLCuyptUzD_ss8GJlGS6t3RyMm0Ttxy9tM5LoD5jeZfpqEqAdUmuIC14J2ucKPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فووووووری؛ فدراسیون دانمارک اعلام کرد که خطر از سر اریکسن رفع شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/91499" target="_blank">📅 11:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91498">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0kd0oDJpLEPZxiO3cwZLVkYD5Ggu2cCb7yuuMDmEi8wQIz2hfHM2VJqYi6vVNdwJW5nGk4iKWjSV9jHGkbbCqaxVZHdwig4AePgrxF4On_JXL-MJDgs9Ys4x-qjex_GcUYo2CAcmn7Q9S_egm12HEbSO9qlREH_s6Wm8FLCKXIgVk-o0-aedcJEBLxfLXDFhkxcAqHwOwhhbLlc_AHIxhbGvusLmsF_1wqmRDA7YSTNFXJl6kV6KITOlvohWOGBlRDNEHFJKvtW24ZMlZ6VqdCwo1wRGV6l5gH4Or8xaRrY83gft0NLOQA4sMr7W_Uii85qpS6dIDd852QNMpMHxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
پوستر رسمی باشگاه استقلال پس از دریافت مجوز حرفه‌ای AFC و قطعی شدن حضورشان در فصل آینده لیگ نخبگان آسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/91498" target="_blank">📅 11:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91497">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
موج بعدی حملات‌ اسرائیل شروع شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/91497" target="_blank">📅 11:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91496">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXkxO6XTrjnsGd_QJNG0DqvOrdzxNX_A6vGZbUTHcKZAFrOJQA3w7th4T7Bs70Vx9cWuBm9xR1SpPy2Ijl5B-WfkyW8YRw6cQGmql7eQrdsSqNFI6ZG_Ysbc2X2F18lT1WarKjZ6NdVIoT68iGk1PVTu64_23If0MLVp5ELZ4LMflJIiV43-W1_F8Ef-pqQGuOCf2UUka1MkgwGIM5t9p8HSGEySBae_j_o_bIJKmF5L6_-5bQsVG6VIR3yBAyBl3HZRHevl-wKAKl4KyDRLEVQdqvlptS2pvcjKFUSit5MSl_Ac0_VrGowBrLsPqtzFj8oSZWR95Dtzwka_LOh_MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ایلان ماسک: تنگه هرمز به نام اهورا مزدا از آیین زرتشت نامگذاری شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/91496" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91495">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚬
بیانیه اتحادیه اروپا: جنگ خوب نیست. متوقف بشید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/91495" target="_blank">📅 10:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91494">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
حمله موشکی ایران به مرکز انرژی اسرائیل در حیفا و ناصره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/91494" target="_blank">📅 10:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91493">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnWf7p46zPU9c5gXJHQRCNAkpON2Odpz9dWNw30dxMFYGpie1LGvXlSv9imA7S1LxUJ1jIasXb6MfPiOq3x9iFN1FLMkYFFTIEyfRCxEg647tMDFRLdy7jIG6SR69AjuiPQDrUPKIHhwIyD1OdQIEYJ1kewi7sazlJg0JBaWL8OxKA5AjXWobjkHT69fK-gMAzPsqGgsHoEp-DjBm3bbCu05Fsi6vws0dwVn1NeWd20RXsZ06bSYwTE6YFySPGiizCHOI-Clqes2GuCKzXHskI_2N3_z-iP_O1bVqGJH6nI4rZl_0lrQV8gywDHLhpKkLjUReOabe9ftwWEhTSP3Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مرکز اسرائیل هم اکنون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/91493" target="_blank">📅 10:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91492">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووری؛ موج جدید حملات سپاه به اسرائیل هم‌اکنون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/91492" target="_blank">📅 10:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91491">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Huy7hFaqX_iMv3MdL3c2DI1oyRVqa6rqSYBk9rnDsKCn1BI53zyaMMw7CTi5Bs0VgzgioXxRnpYexaJCZ9Tc2S_RymvpRlLqdE6YJCEMQdADSWQSSr3JTeU49j1wY2koXstbeg5gJG_vSBFpYbixkqJYWwKilQxdZyP-o1iKWvUPZEWaoeMcrMK9Jfn5cDANUO6_nEdhYsoGvl-tszTs2tyHz1ochxmFO6nztJX8_2HOG3GC4BjeuxoNF_gnB5ABsv5kus-MCpBHMQ1zEDXRaljCmWL9SP2LxKppAs20wOK_0pk1q29_tKOA6ICkraiJXkwiVTAumT6muI4HcwJVqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
تفاوت‌قدی عجیب هافبک و دروازه‌بان پاناما که در فضای‌مجازی حسابی وایرال شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/91491" target="_blank">📅 10:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91490">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
سپاه پاسداران: ثابت کردیم آسمان اسرائیل در اختیار ماست و هر جا رو که اراده کنیم میزنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/91490" target="_blank">📅 09:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91489">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
فوووووری از رویترز: با اعلام انصارالله یمن، یکی از مهمترین تنگه های جهانی باب‌المندب برای آمریکا و اسرائیل و متحدانش بسته شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/91489" target="_blank">📅 09:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91488">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d14bce5f84.mp4?token=oovmh8DaC14xcjQN-Io9fT_-ymM020oZSwZNFjqzjq5hbrXYDzU2TO8-aUsCsnK73q2l1oPjANQPf0EQTx59Wzu4MVQZT8oW3nyTW3RKaba5DhHn1hdR9GWIn2ls1BMCMzznfeGo3BzEBqoRkemy8Yqw-fKSguJXrr_mw3k6rJCvwmdDnTQfDiHilKjYvn-Sncv2gGcRf9PU3EQ2W4XjHiFxCN8PFX2L3Es3j4hkaSjA849fKz8CQ-3v0gDKAQpcQzA0lz21x9fxTtwyM47drNV_EJz7IRKU6hA57cM92xsozdfZfQsoqbUKfd2y1L07PLKlF_l-QkdOyG8YWbqkiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d14bce5f84.mp4?token=oovmh8DaC14xcjQN-Io9fT_-ymM020oZSwZNFjqzjq5hbrXYDzU2TO8-aUsCsnK73q2l1oPjANQPf0EQTx59Wzu4MVQZT8oW3nyTW3RKaba5DhHn1hdR9GWIn2ls1BMCMzznfeGo3BzEBqoRkemy8Yqw-fKSguJXrr_mw3k6rJCvwmdDnTQfDiHilKjYvn-Sncv2gGcRf9PU3EQ2W4XjHiFxCN8PFX2L3Es3j4hkaSjA849fKz8CQ-3v0gDKAQpcQzA0lz21x9fxTtwyM47drNV_EJz7IRKU6hA57cM92xsozdfZfQsoqbUKfd2y1L07PLKlF_l-QkdOyG8YWbqkiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه ورزش عجيب و غريب تو اروپا اختراع شده به اسم اسب چوبی که هرچی از سم بودنش بگم کمه و تازه براش مسابقات قهرمانی اروپا هم گذاشتن. فقط این ویدیو رو ببینید
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/91488" target="_blank">📅 09:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91487">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
رادیو ارتش اسرائیل:
تبادل آتش میان ایران و اسرائیل احتمالا چند روز ادامه خواهد داشت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/91487" target="_blank">📅 09:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91486">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88d8579a12.mp4?token=QtMjLxdUp5SFALZ_KFrdxiyDGoRBhbX4fYUNHy69lV878Gvi_R2sl4rNbEds0i5ds8764-Bdg2KN1GW9nekKVC1YWPf-Oz635NaL6uvJ2SdGZD6zMzMQANF0F1FWIV1mLlTH23K_zDjqVwOsaLguMKnTUU3uNxLmTfjNLmED15q4YLamLXy0ReLoXt4dKnWd1m7m6Li6L8c4cLE73IZU9NjB7bp7TiYCH1z9ai9ltZzJ7M2AHe8Rl7EJ2i4Y0WSqsaR2_lP0rg6JX2CFeyWpwIGPcpyxsji6QLvNoYB60bnqOZCkT94c4xOfbDzErXGhu6TG3UXJ_5PFXo1yqYYtGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88d8579a12.mp4?token=QtMjLxdUp5SFALZ_KFrdxiyDGoRBhbX4fYUNHy69lV878Gvi_R2sl4rNbEds0i5ds8764-Bdg2KN1GW9nekKVC1YWPf-Oz635NaL6uvJ2SdGZD6zMzMQANF0F1FWIV1mLlTH23K_zDjqVwOsaLguMKnTUU3uNxLmTfjNLmED15q4YLamLXy0ReLoXt4dKnWd1m7m6Li6L8c4cLE73IZU9NjB7bp7TiYCH1z9ai9ltZzJ7M2AHe8Rl7EJ2i4Y0WSqsaR2_lP0rg6JX2CFeyWpwIGPcpyxsji6QLvNoYB60bnqOZCkT94c4xOfbDzErXGhu6TG3UXJ_5PFXo1yqYYtGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
خانم جورجینا درحال ترتیب دادن موهاش قبل سفر به آمریکا برای دیدن جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/91486" target="_blank">📅 09:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91485">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
سپاه پاسداران:
دقایقی پیش، عملیات نصر را با هدف قرار دادن مراکز مهم پایگاه های هوایی راهبردی نواتیم و تلنوف آغاز کردیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/91485" target="_blank">📅 09:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91484">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32a069e77f.mp4?token=eRtdOBPxTP7VCIQKLKfEo-7IvAh7KxbBsWYjNNekNjElqbdFQwTkzmdWLYgR_iGD3-9hLvudvOaT0qXO4B_DTNb3ov6bwoYweE7dMRxHyxey_jj6oJwZ37CENb9o6uXxISAKaNp5ZdpOF43tgdG-AKgNAJgtQkYF-tZA9oFttE8NA0jaxlPOWtOL3zip3kPL_IlIhB7c_5snDOdgcO9oavrdYUYRAT0Zp5V4cqEJXlU50ixjV6LnuNHFMbEHF7Zp5kMjQn91SDRODzjddiKDGvaAUFk1XFunvgd0S8XiPJSZYzY9-GenpPLrEjJcFeOLV0eIdZ-_eavTSffDSisp2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32a069e77f.mp4?token=eRtdOBPxTP7VCIQKLKfEo-7IvAh7KxbBsWYjNNekNjElqbdFQwTkzmdWLYgR_iGD3-9hLvudvOaT0qXO4B_DTNb3ov6bwoYweE7dMRxHyxey_jj6oJwZ37CENb9o6uXxISAKaNp5ZdpOF43tgdG-AKgNAJgtQkYF-tZA9oFttE8NA0jaxlPOWtOL3zip3kPL_IlIhB7c_5snDOdgcO9oavrdYUYRAT0Zp5V4cqEJXlU50ixjV6LnuNHFMbEHF7Zp5kMjQn91SDRODzjddiKDGvaAUFk1XFunvgd0S8XiPJSZYzY9-GenpPLrEjJcFeOLV0eIdZ-_eavTSffDSisp2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صبح‌دوشنبه و پارت پنجم ورزش در خانه
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/91484" target="_blank">📅 09:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91483">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
احتمالا با دخالت ترامپ وضعیت جنگی ایران و اسرائیل موقتا تا بعد جام‌جهانی متوقف بشه. البته اگه ترامپ این‌سری واقعا بتونه خایه‌های نتانیاهو رو بکشه و مثل دیشب کیر نخوره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/91483" target="_blank">📅 08:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91482">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌ها از یک انفجار مهیب در پتروشیمی کارون ماهشهر حکایت دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/91482" target="_blank">📅 08:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91481">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
کانال ۱۲ اسرائیل: طی چندساعت اخیر به ۲۰ هدف تو ایران حمله کردیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/91481" target="_blank">📅 08:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91480">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9d994e5a.mp4?token=WK3D3At0HvuwdnA40bSjQdcKxXTZpYSIkoHtIqMyfFh_epxENyAcdiZZ6VbEMuI3UGHRKAmZHenzZ-H4yr9UpX2wemXWt-qKYqBwlEHVizddFV1q6q4BlToRPwkqGc70T-8IjbcTnoRT2aGkHcLt1oGK5Fc1jpBYEXOYIB3BSb66KgW70LQam_JaDrf7vmRpRCb2QbHG6T_nxCwcgGxIuhdFRLX35kmEx7l1ITAwK7XNNgN7ssjV0Sib-L9B9bGgDlGG4UG7wskEIjZo_B75A4i_BRh_Fwy8GEwrAeqxlNX9WtLlbnWPG28p-WASRyknx0Ss2CVVdJ2zqtvdQFte7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9d994e5a.mp4?token=WK3D3At0HvuwdnA40bSjQdcKxXTZpYSIkoHtIqMyfFh_epxENyAcdiZZ6VbEMuI3UGHRKAmZHenzZ-H4yr9UpX2wemXWt-qKYqBwlEHVizddFV1q6q4BlToRPwkqGc70T-8IjbcTnoRT2aGkHcLt1oGK5Fc1jpBYEXOYIB3BSb66KgW70LQam_JaDrf7vmRpRCb2QbHG6T_nxCwcgGxIuhdFRLX35kmEx7l1ITAwK7XNNgN7ssjV0Sib-L9B9bGgDlGG4UG7wskEIjZo_B75A4i_BRh_Fwy8GEwrAeqxlNX9WtLlbnWPG28p-WASRyknx0Ss2CVVdJ2zqtvdQFte7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌ها از یک انفجار مهیب در پتروشیمی کارون ماهشهر حکایت دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/91480" target="_blank">📅 08:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91479">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌ها از یک انفجار مهیب در پتروشیمی کارون ماهشهر حکایت دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/91479" target="_blank">📅 08:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91478">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇮🇱
گزارش‌ها از شلیک موشک از مبدا یمن به اسرائیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/91478" target="_blank">📅 06:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91477">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
آژیرهای هشدار در سراسر نقاط اسرائیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/91477" target="_blank">📅 06:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91476">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2NYvGydUtzxJOy2i047YHcRfsjRQemKx55n5596i3qRFNIpJyf2cLGr8NW9Kd2YP9pzHUYNOqGc4optA1d8wECEpaG7mWud8GrNH-ceqOGd253cXqPGYIoYcAnPgPfB8eA2qDDh8qD_WAiYqiXnPQsQPFJxbxgIiCp0xvculUtonPOvSx7X_YVv4MJ_hV_anLlz7949fy16Sh8QwHa097iLyDlEflAVTq3I5sGU4ipOCYRkLDhbsIYKJr5uwa0-RMCmcDd6RKxN0VqR6IsFeR0ZW3ARd5PvAIUXmS2xK1deKgZKD1FoXx8I_EHAKrvGFLl3K4DPLs769oY3wIAidg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
آژیرهای هشدار در سراسر نقاط اسرائیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/91476" target="_blank">📅 06:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91474">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02c5f07bd9.mp4?token=QvQI0JZBORKX1tendCXiuAweX4tDGE8u49THbPSnUzqfJTuTnAwEI-9czFbmO_j7NmNY4M8AGxteMu4oGvfWYmRW0ZfTdS4GW-dvLzLApVqPlyr6fLLH08ta68eymp8UCR9KzYA8phtSOKsL9IBfnDITY5fAi9nx_Bfgb6hU2HgZH09WmgbQEXAsr3Pvk6MK1oHLSaijL8qHww80fNXHtPl8ud04dU7iap7c4Nh6XsoA_sXElhZvatZobQ6bi3W5KlPo_JmmavOCec80Y2dZ8Frvp_bJELYWctccA2OBi4CpwNSz2nDHquL8j-_xgCpev9yNLtldP3kfgEyU9lDKmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02c5f07bd9.mp4?token=QvQI0JZBORKX1tendCXiuAweX4tDGE8u49THbPSnUzqfJTuTnAwEI-9czFbmO_j7NmNY4M8AGxteMu4oGvfWYmRW0ZfTdS4GW-dvLzLApVqPlyr6fLLH08ta68eymp8UCR9KzYA8phtSOKsL9IBfnDITY5fAi9nx_Bfgb6hU2HgZH09WmgbQEXAsr3Pvk6MK1oHLSaijL8qHww80fNXHtPl8ud04dU7iap7c4Nh6XsoA_sXElhZvatZobQ6bi3W5KlPo_JmmavOCec80Y2dZ8Frvp_bJELYWctccA2OBi4CpwNSz2nDHquL8j-_xgCpev9yNLtldP3kfgEyU9lDKmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
انفجار و آتش سوزی در غرب تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/91474" target="_blank">📅 05:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91473">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
⭕️
چند نکته ضروری هنگام وقوع انفجار
در این ویدیوی آموزشی، جمعیت هلال احمر چند نکته مهم برای جلوگیری از آسیب در زمان حمله هوایی و انفجار ارائه می دهد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/91473" target="_blank">📅 05:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91472">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FszcdQWSP2Ue0qWv4tcbcTsFek2Wbd4Z4yVJe3kuKP5zNQeleOIjFOOQPEwBVvAbbUCgvtdjMoEZNvkWRO7PrfALFVnwjL0yHw8mxnVIaYgMTYd112zZrSW0ijp5GYtvTGLLKZAxDzG3meePKHoZhDQ5SsW2jdyewuHtk03stOakR_CLKKkrofJf8qc9T4j2tgUyQ-adAJN7xOvmW520SpVhzgY_ilt3BMknt_iOTRdPRR8ZepHJzhfDtc874nsngIjAB2X1taZa9MHnqiDkdpC4kqsyesi1MKVd2erQaf9jQIyc6g3M8LaFFgWHiTleprMDDdeEKrWhEL1K8kDObw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
♨️
انفجارهای شدید در نجف‌آباد اصفهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/91472" target="_blank">📅 05:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91470">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
💪
#فووووووری
؛ فرودگاه مهرآباد تهران مورد حمله قرار گرفته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/91470" target="_blank">📅 05:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91469">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
کانال ۱۲ اسرائیل: پدافند اسرائیل در آمادگی کامل برای مقابله با حملات موشکی ایران است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/91469" target="_blank">📅 05:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91468">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23e78148f7.mp4?token=KkeC870s9RE1hQFd_21N1R19UVvmVre59OQzArgnl2pCxHPWBRyq37Z9eEzMJTcrIULzx0TAtgNLDbbhTgDKgK_gQIFQo_YfvH7LTL0BZafku5Dr0g_Rz2imKfKAXMbcoQ-wC4-K4Wg1wbMrwbeFNV3lpXV1rv61aWzQRHHAZpCPO4imW3Dv4vDmO151ejlDNdMkCix33eNZXfspa8ADzi7H0XebGgHgKmAdaFAwKlA7LnHj4-OBk-75fyd0bmeRQrW_Zbc1vXa7n1ihG43ed5b3HKSjQTpRO6q3RLQIngCdE-PaT4cUk8bATfibZ7wz0dTao9xGsNtOGa4nGxFhBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23e78148f7.mp4?token=KkeC870s9RE1hQFd_21N1R19UVvmVre59OQzArgnl2pCxHPWBRyq37Z9eEzMJTcrIULzx0TAtgNLDbbhTgDKgK_gQIFQo_YfvH7LTL0BZafku5Dr0g_Rz2imKfKAXMbcoQ-wC4-K4Wg1wbMrwbeFNV3lpXV1rv61aWzQRHHAZpCPO4imW3Dv4vDmO151ejlDNdMkCix33eNZXfspa8ADzi7H0XebGgHgKmAdaFAwKlA7LnHj4-OBk-75fyd0bmeRQrW_Zbc1vXa7n1ihG43ed5b3HKSjQTpRO6q3RLQIngCdE-PaT4cUk8bATfibZ7wz0dTao9xGsNtOGa4nGxFhBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
🇮🇱
تصاویری از اصفهان، ایران، دود را نشان می‌دهد که از یک انبار تولید پهپاد پس از یک حمله اسرائیلی بلند می‌شود
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/91468" target="_blank">📅 05:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91467">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWdfszMo6lqc2TiQ9IXbnfzEzII3B8qBrnCeNdI0LuG1MU7qhemCt3mr29nuthlLfqDnrsQriYqxSrJa5lRg4bVJbm7ajADz0Kw_jcHrx14QRYXLyJ3y8nPJfNu6qRj8P3ug7tqM8tMbBz38dqfSzLrPxcyVPAMVCBGgdX62PoUoiHg13aw56EMQfDpmZy5wimnPVk67mJlLesdtUCByZqVvmiUlb9Be7oVZaQ_p37F4SLJvEDT3eud9fNs_3E1q5_ZKU2onT53I37KDpmX2v41ZCQA2vZNMe3nqsI7fkXZQyvlsZycuUZQ5sfGJBqr4Q0O9oLmkXaJCNJUXJNrG1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تصویری از انفجار در تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/91467" target="_blank">📅 05:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91466">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
🚨
شنیده شدن صدای انفجار از سه شهر تبریز، اصفهان و تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/91466" target="_blank">📅 05:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91464">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NhrvMTUA5uzatoYG0CxVFZKTpzJgk8v5MIPtpOzvtO3gkhWsucxHKa-ku_hp3vmk7NkHMKDWIa7PVdA4QiPIpRCKD-nR1JIRvzrzzGDNTg0Uxu9DidPMr1rPaskyxW4WpmHolXO_R5biepK8UX4azKf87tjzl17_CExAHB0c62pGhlG08m4rroAryHP_jfxQZRVKhF0Qlsi0jlBnCWbMYdUbqKEjrFQhTI6akDOyEPcHsgTKYmCQr8dCQaSU9MT6GZx1G0BzCOleqPZIi7yDvJ5YIp2WWZ2e32MObRNaKCDg7lc2aMeFNYKURwgAE32NlOzBFkBzDw6jLFnnYjCc4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aGHzUHzqLei06BWq1eK5AEVNq24utka_pr2Aa2ZbREp0ApSD-BSgI53ZelsMzJ9ARFVdJd8SqgtMIiyKJWQ3UdTinwD773uf7GhVz1idfMj9C-P-T6CDkVN3nIoqIWUgZXYmbj0CnBh_6MTPi7NDfQyRR8zRREhBTYzgNV4yhZ0o9fjRWs4qKUiFy1B59paKmklgyiCLzAS5JsjN9D0O7iD7HifNNWqA1vlMmCbQCUrUWeE3PCoyCWf2qSGBh9jiCeOFBCTyNeUoUorc-z4jGWXaX1ij57MenT6XNBg-sXJ6WX6OmTO4Yh8KKO1Nk3fFnPXN0-wqQH_bnuqWX2WgLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اولین‌تصاویر از انفجارهای شدید در اصفهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/91464" target="_blank">📅 05:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91463">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
🚨
شنیده شدن صدای انفجار از سه شهر تبریز، اصفهان و تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/91463" target="_blank">📅 05:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91462">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اخبار محلی از آغاز حملات نظامی سپاه پاسداران به مواضع اسرائیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/91462" target="_blank">📅 05:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91461">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-8ddiNzkupU5tCTgLFpfb3xTOTnc-iVhdE_kJOy2etMa3VKd9lmtUM6qTWH9mZiRBgJfgN1C894lE_aIbz5dMA5ad0vCmixtVb-dtMgnN-bd6fkGFAwNiJx9ZJYEgVIhMO8U1evp9L70EcqxdDMWTf7bB_MTqk4uNSJc7AeXoUrH7rzAwYOLRENJSZnE5ReZn_fy4bwB-RU04TYTkjS1iPvsOIial-Zi0Off0BKtgOT91FiiLqxr4JCk7xRr9xy_XgYda934zD1ihVMZeQbqrV-P8c1HwIV_FN5kyHrr1eZ-4s2urtAW-Fe9594I8SUU3Mr7phjGTq_xkEGPrwxfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
ارتش‌اسرائیل از انجام عملیات نظامی در خاک ایران خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/91461" target="_blank">📅 05:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91459">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEXQSuHIzAJxmmFQQGGowkMnuevR3KGAhtHtn6AAvOVl_wvifO9Rm3zeKqE1xvN_D1PoacI5PfmNkLIe9tLN1MQz24dfzTC3x0tUmbeCU0wRJ254XASeM8dxx_dMNgbqJchaN5Bfak8ujONiPomRTsX3Knbu-LBe8vcAC0es1VNfAqwOqP8Hz_iN9_1Wmz0EL8Nu34PFKqWd-8iwXdEhLCUAJaX9QxDqE4u_N4jIf6V6KCe4vPAJ7QgBnHGGqlOgQzv_2OOKOJI-mJnEQyepupeinhfSIvb5WIwy0Adfowow3KvCbhhTVbS1-kHlwM8HjrtrEYJDSQj5x5W2P1FxbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
👍
🏆
علیرضا فغانی شریف در مراسم تصویر برداری رسمی از داوران جام‌جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/91459" target="_blank">📅 04:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91456">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I1AX0fj5vpob5-a-EMeWWHYcInx3O_nBR9RGCi7Ypxmz2oSx16BxafGiGlxaB-kqwy8EjYsTg6gqIcmhdw0WQkmzoKxXWhPir1RtOAIpdZGLlBDT1m3MjhPB4DjfgN_l69uEyPxNkJJbHOaS_EyejDnEH6dGD1Kb8JrmE8oui94bZ6ljuxEjXxDYP_Aa9VS5P7tp-kmKHkIBeunpyhgUiESLLBNeYsea3_-uoWB-_js2Ptn01ikDOH3kqT1qBl2n8_RnYAGJ1KyW4pzSw1y6n7QWbdKvuZu272OMjfLK3HzXnKnrYuhLBPDnFN4k3REss8O-4Re5CTIRLX7CbIYcoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cysSrVgr9p4837bmLs3Z-2yiap2PjRHyzkh-fQK_OBLU8NkwzVBW4z1LvnS3VGAKhCGDtKmZp-Ao_sOjhtvvvJ_tkVr4F1P5ukgshN5Wt0hwQq4XNUe4aRI6s_EJ4JeGBMtpO23PndRF_uJbXcYZ-KAX-Tgpsi_ZJ-HyQttP82C2XNnUu1BDKJI9APRA6OLo_7dkRDGHk8LgqxdoVpDpSjyxTpUTospZg1NASdsDUN90l_THBFnzLIgaqQy7pHZaW-qHSHCwc2vBuuMBcMs-3w8CEpUTpSOsRmoIccq-zl9IYNr38VSDl4EirYqR57YY2KA15T9bF2ZrMeStsPFgJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bhGfATt8kp5PYB5X-e_qDTbuV5ZKV50-iYHtVoldLedp_YV--jlaFXTvAR-AEBMKD3AaUob3vSBh2oTqTMv-MoDZj_ydE9dt3H_Ga01km1MuuidtUZG9f3iLkZqVy2-fZ0StTWJ8hTEspqsA64lsrlApWIxzrMmT-kTZ51ljDP_xVNwsQPBmui-eSb9OLwue7AmtCmPPL3cgCoEpo8UhWTdmHjdcSfjTe40Q7VbT63jfVCEDF11QmZydJEndiM-itTMKfUJK-kkdqtfneTypnY6h_VmB0tt8df4JbuYswGKNuJu2ydbLAKnuX05MW8Gk8n7rvmoDNfWOUPbBoOEQGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
تیتر رسمی دیلی میل در ارتباط با این فاجعه اخلاقی
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/91456" target="_blank">📅 03:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91455">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4yfPykKNN9d35DUGBo_p52OCxQButIpumFEYuW_yvqEzLaJ6P22xUuphXrriulKsabFay0XlfqS5F3aKKrQhEM08Wc4rczuWUTDU8-E1Q8Tr67eohQmiMxWhcjHTRoZOvX4pqXmih1SZ1gf80RFFyzPu0f3lRSmXG1vUIksmB-ftioaP0adGopkO8OD6n7ccMI-oooHeNB2ml-PCSS3ZcJh6zxh0n6AQQg_XN__9D938bmch4eVrzTKjJ_H1lmSge77g8CepJKcB5Q7U22Ti2_MLi_fGY6BV4h20OUD5vKDtNW42Qj8Z3b-7SAkOmQNo8K3CQYPbD5f3MgccIt6Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙️
فلورنتینو پرز:
آیا ریکلمه رقیب خوبی بود؟ نمیدونم اون کیه
😅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/91455" target="_blank">📅 03:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91454">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_6YFHrJAHdcP1nKO0r2YzMbde9_FUciFKoLtyFmTYpYJyf0ETLcaWJoRdq_QaEhxPEKV5p4oYlvpAKwZsq5OsQKTX5ZJM7QMPBmDsoBYSLKRu1KJthUilDE5iJszloZinAoHvzFOZonDL6ZswnO58qZWs1sW-YtJuFO1lhdwhKHri-gBgTF0yiVXPphD1mSaaBIi_yHpCCbH6as49Os9Dn1FpQNXvyJTUg7e2oAysoyoUo1-7-SIeiyfFhvB1PfbrbPXiOaDFBx857syPCjXD40iVl_SBq-UB7Jdqw-RIJ9M3leLXep88g6czIg41UISCUSsAknHJzErcvXZbszrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
فاجعه اخلاقی و آبروریزی بازیکنان هول تیم قلعه‌نویی در ترکیه
‼️
‼️
‼️
گزارش رسانه دیلی‌میل از فاجعه اخلاقی تیم جمهوری اسلامی در ترکیه  فوتبالیست یکی از تیم‌های جام جهانی که در ترکیه اردو زده بود، می‌خواست دختر ۱۴ ساله بریتانیایی را در هتل، برای تعرض به پشت…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/91454" target="_blank">📅 03:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91453">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSF4i2Wg8LzWMykIF8Am6WKg6gKyXr0SQReQopEpRImXsBfPXY06uiVtFQ1LDwil6kKyUkDpzR0HDe6exeIDLwhkOa-SdDnVL55TBSUuRCNmtC609YXRBQcCJJyClB34ochJzzkumnY6nOwvnw0Qn2_G_Y9yY3PfpSAzgze-abR5CjNt35QA04TvsuJFeVA2GonWg5k2tjBEJgjcHc0E1Ui3NTMDYzywtA70YgMGVkrhZ7__yjXwQW2HS7D4b8QXQIjtUJ-brHOFhUDcxIC9AenhP2dlqEFfks6XmEQ3LPi0lxL7XBqLVjKNIXTT92bzoTW1NvAkIIFX8YdZ7pjlEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
فاجعه اخلاقی و آبروریزی بازیکنان هول تیم قلعه‌نویی در ترکیه
‼️
‼️
‼️
گزارش رسانه دیلی‌میل از فاجعه اخلاقی تیم جمهوری اسلامی در ترکیه
فوتبالیست یکی از تیم‌های جام جهانی که در ترکیه اردو زده بود، می‌خواست دختر ۱۴ ساله بریتانیایی را در هتل، برای تعرض به پشت پرچین بکشاند.
این خانواده وقتی متوجه شدند در هتلی اقامت دارند که یک تیم فوتبال عازم جام جهانی است، به نظرشان هیجان‌انگیز بود. کودک بریتانیایی، با فوتبالیست سلفی گرفت.
آن بازیکن، اینستاگرام دختر را گرفت و با وجود اطلاع از ۱۴ ساله بودنش، پیام‌هایی مثل «hot» فرستاد و خواست روی پایش بنشیند. پدر این نوجوان گفت دختر وحشتزده‌ام پس از حادثه، در حالی که با خواهر ۱۰ ساله‌اش کنار استخر بود، می‌گریست.
پدر خشمگین، فوراً به هتل اطلاع داد. از پذیرش با او تماس گرفتند تا با مربی و مسئولین تیم ملاقات کند. آنها عذرخواهی کرده و گفتند بازیکن از هتل اخراج خواهد شد. پدر گفت روز بعد متوجه شدم آن بازیکن نه تنها از هتل خارج نشده، بلکه هرگونه تخلفی را انکار می‌کند!
مادر دختر می‌گوید: دختر دیگری در همین هتل، توسط همان فوتبالیست آزار دیده.
خانوادهٔ اول، نتوانستند خانوادهٔ دوم را برای شکایت به پلیس قانع کنند. از طرفی، مسئولین هتل به خانواده بریتانیایی گفتند هیچ فیلم دوربین مداربسته‌ای وجود ندارد.
باتوجه به اینکه تنها یک روز از تعطیلاتشان باقی مانده بود، پدر تصمیم گرفت در بریتانیا موضوع را بطور گسترده‌تری مطرح کند. می‌گوید «نگران بودم به محض اینکه آنجا را ترک کنیم، آن بازیکن دوباره به استخر برگردد و همین کار را با کودکان دیگر انجام دهد.
پدر از آن زمان با مقامات ترکیه و نماینده مجلس محلی خود تماس گرفته. می‌گوید: «هتل، آنها را در اولویت قرار داد. با آنها رفتار متفاوتی می‌شد و می‌توانستند از هر کاری که می‌خواهند قسر در بروند.»
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/91453" target="_blank">📅 03:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91452">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SK-5lXNx-ZP_jlKy6emeomwCiHNrKfhHE7N_9S8IzVevnlnPuHPHArO9Ag1qGtOWy2XLru7mXu8ZqnbmR1oQfBE5-7NqCm5nEIeSCvzBlOLesIdA5Iii1TldXlff4R76Z1E_O4YmmRHRLUgH5hvE0fc3AnbsK0YbeAq53H21jK4fKImUr_a1J_2IH0om4kOvy79Zdrau5Qao519kYLP4c0DaP_qDGAfo-uhSTyegeM7jIDNswBGeFGMKj-L5givGEjEuy_otk7UU-Nh7JBd4-8BpmhUT-qj6q4kgwDWDxu4BIP8mqWPQ0KMLHcIdjFJHnnLvK0PixM-19U7TMFXYEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
💣
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/91452" target="_blank">📅 02:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91451">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🇪🇸
#رسمییییییی؛ با اعلام باشگاه رئال‌مادرید، ژوزه‌مورینیو با عقد قرارداد دو ساله با قابلیت تمدید برای سال سوم، سرمربی کهکشانی‌ها در فصل‌آینده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/91451" target="_blank">📅 02:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91450">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGF1O9fYJvmUivMnisTBCvCzVzjrE6hIe1GD1hf6bzv5IIpqM0qepo92Yznh_KVuhWfD7hT3PkWQuK8LxJgoqpIBhZiZyCekdTuldsluMk-sV37KwP_OyZYj0R0JnExaUKZC9GSAqnGm1Y0bxXMEEFmdCCZSYy5B3tQ8HI0zBW40TP-8yduSbQPXsnHeDLZSzAz5QSOUMoyQqyYfxsgaoaCERiMfXF1r4GafsfFYc9O_aAyyFVbQEnvwtMKCGzlYLl3SUXn8MrOug7Pp1rJUg68-dQrnP-GqrRp2tFGrY2bo2v2AK7OEetl0bBdNwPG-Xc4TDAnhYj3JErOyqjiC5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚪️
فوری و رسمی:  پرز برنده انتخابات شد و تا سال 2030 رئیس باشگاه رئال‌مادرید می‌مونه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/91450" target="_blank">📅 02:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91449">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9P5eOba-og4B8iOxOswSGWE_NcTMbmlW5JFY0LdKIwLJLY7GnTKrbGinxgeF0-_zheU_meZ5Zg6Ulr9V-LyQt59sDB6QKsKYk1YRQdZSFsKPhpMV6OryrsW8INRT-KMJev1fEysom0xqH9c9vKk37Ftn0fQGPfZKKsTJa4UHVT-TsKzp7Y6oRpNO39vDTcY4dpTI-RE71l9HjXqrZNBXfzLW0J2OeOQmYbwrPmToIcOC_zkV0Llel3BR0Iz-cJukGmOuTMaEqPw9PBwYPHBW0pJXr_h3D_s8vx1OEY_zfdtnB3kvhYQl1NceQPWmsmBdJqlJX5FuYfsbmTFDx3cfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚪️
فوری و رسمی:
پرز برنده انتخابات شد و تا سال 2030 رئیس باشگاه رئال‌مادرید می‌مونه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/91449" target="_blank">📅 02:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91448">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvhqYpIb0nUsr-gU1pF2AAsqleB8fVz4EVI7apknYtmWgV0NniLTFjYKfYavg8RI0LSr9twVGAvusedyyBiWnBnsUflYNEp2e2_hFG6CZ2b6qXHuNqENfbVKJu-64P2C1OfNHkSEPuSCvyD9QaTLy0sPTcCrhDanEejsKSGeqjRquo_ZPLUb68nALCvigCaKMTF_bjdmdZjZZU6opFPCwEK6PXeEzyXm98dDuOIsk_LLekCqe8NmlfoNUYLbj4I3-L7y0B3jW9GeCrNpOoYG1LlF68S3S-H1LwGHdtk_fbp1Ebf1J8_VDL1h-eUKzk5-PYrbQvrpuQ728PQGgT6B6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
خوزه فلیکس دیاز: پرز در تمام 60 میز انتخاباتی مقابل ریکلمه پیروز شد.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/91448" target="_blank">📅 01:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91447">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
ترامپ: نتانیاهو چاره‌ای نخواهد داشت جز اینکه توافق با ایران را بپذیرد.
من همه فرمان‌ها را صادر می‌کنم. نتانیاهو فرمان‌ها را صادر نمی‌کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/91447" target="_blank">📅 01:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91446">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fG5dgRbpFoyUs57CdM7aDqsYhJlJLPQLOBHNaEKfuxZS_x0dQXXfYR-UP5lo_qMdFgYJo8lcB9wUV_xqAgPckpydVvw3vXn2qf9ch6aIr2DEGyPFHefEEncVJpa-aCjwbqBnyx9ovAaJvTZTqLSQyCnkLrsunRu4d7NlN1UYgmF2yjp2M5d0eR-XpBY-jtIt0YvPlVzhkeuuVGQ60SyE3jlidsafAgjMb1c6p4tek1OaRJtExu2HT7-s27kG2utMejEqzpGwyhRrx-87rR3ErhNVKtHWlsmCNm-a34vFInpqhew1J3gEtNbik6JfUntDqSij6jMc3An_PjDSM-mGZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
منابع مختلف اسپانیایی مدعی شدند که پرز یه گزینه جذاب دیگه بجای اولیسه تو آب‌نمک داره که ارزش ۱۵۰ میلیون یورویی تعیین کرده و بزودی اگه اولیسه رو جذب نکنه، سراغ این بازیکن میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/91446" target="_blank">📅 01:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91445">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/46b3a86a4f.mp4?token=s6wPggOJc3qRHyZ7zoGaKksZZVVvEvttGcD4O0DJ_gDU2nlbznxoghT6irZby2B5mLIn4fWHB5AgKVHr1AZLRZeHsSYSJuKiY2uBj0MASAB6oT5Wx4mNoK0ie1e8oCTPXYa79rOpLbI2-mFe4r9Z7hLqj5OLyeg3lKvHmEXCYXfc69f0VSbzmATy-vdFefujlOwjfX95UNJt-jYRbwOO5oI27mW8Jbga60n7Z87jPZ-eXuwEBER54atxPDgfdGEKLTcYRYuXSgAvMZoKkjTyAZauYOKB-hCguGKthzuVjFbWNPTd8jAU-iqqwOqIfSxTKdYcVekVYEzUZux6zoks3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/46b3a86a4f.mp4?token=s6wPggOJc3qRHyZ7zoGaKksZZVVvEvttGcD4O0DJ_gDU2nlbznxoghT6irZby2B5mLIn4fWHB5AgKVHr1AZLRZeHsSYSJuKiY2uBj0MASAB6oT5Wx4mNoK0ie1e8oCTPXYa79rOpLbI2-mFe4r9Z7hLqj5OLyeg3lKvHmEXCYXfc69f0VSbzmATy-vdFefujlOwjfX95UNJt-jYRbwOO5oI27mW8Jbga60n7Z87jPZ-eXuwEBER54atxPDgfdGEKLTcYRYuXSgAvMZoKkjTyAZauYOKB-hCguGKthzuVjFbWNPTd8jAU-iqqwOqIfSxTKdYcVekVYEzUZux6zoks3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این لامصب توی چهار دوره جام جهانی و در طول ۲۰ سال، انگار اصلاً پیر نشده و چهره‌اش هیچ تغییری نکرده!
🙄
کدوم آهنگش؟
۲۰۰۶
👍🏻
۲۰۱۰
❤️
۲۰۱۴
👎🏻
۲۰۲۶
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/91445" target="_blank">📅 01:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91444">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a15a206df4.mp4?token=Jf8cwTIsCX9LHFYROyJ_7ZWDTYBPhLcFT6lBqGpOHnLVTxGAzigETAmYO05VSzHib2IqybMba4lOKhGCWV4lBucnFlk-bCdeJcRdc47JeiKA6xnbuXAd6CnWti5vfdNLFehVIT1KWuK14TKdTjQgzUa-51r8O5_s8xvd2oPMj-3HHKwknNvHO8lF0xVvElVV70r5gvCnS2U48_d8SGJ9pVSOdZY_qtrSkGcLyDDYQDEP8BeA8Wg6mXqKdRdCJgkraHKpf6ueAbId6MUOBZOtbaYyEgNJbEybI2jccAqcoATvrrh-H_Tzgws-C0Qj7CSWQE3ezTTrNbeEdn14uRZURQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a15a206df4.mp4?token=Jf8cwTIsCX9LHFYROyJ_7ZWDTYBPhLcFT6lBqGpOHnLVTxGAzigETAmYO05VSzHib2IqybMba4lOKhGCWV4lBucnFlk-bCdeJcRdc47JeiKA6xnbuXAd6CnWti5vfdNLFehVIT1KWuK14TKdTjQgzUa-51r8O5_s8xvd2oPMj-3HHKwknNvHO8lF0xVvElVV70r5gvCnS2U48_d8SGJ9pVSOdZY_qtrSkGcLyDDYQDEP8BeA8Wg6mXqKdRdCJgkraHKpf6ueAbId6MUOBZOtbaYyEgNJbEybI2jccAqcoATvrrh-H_Tzgws-C0Qj7CSWQE3ezTTrNbeEdn14uRZURQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت صداوسیما امشب:
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/91444" target="_blank">📅 01:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91440">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sWtbUsOifn1otdJC8jG3kCJLD-NqaYz6xifXrEtDKNM64FHkSKp798cySq1r6h76o_u1PqdlXvwXAuYVVWlRAut1ob7MLuGJM1oZDFZ690Y_sYoEZpzKKMjSw5wT90tTc03vcavEzON4J1PGMRs3ZZeLIs4QE0oz7DVDIOC6zxCMyqzT9rXYmWKYXGA-I7Lxhc3wMIYcu6VLH0OYG67JvEYGZPPUTBbkMLXw-iyxrqBDyvvynHwckgAcx_tstd8WUEPYKGJf64rKjihh_paazNJ9T6WuK5ZpbubEI192ivx8H19aG8bzI80JqG1WXPSCbIYSyigGpAbiP9f-w_2UGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QcDobAnXgd-Bmrvuc0zsg6llj_v86OtOpXc8JTM-bW8-ABcRmuYMnAeoaFN_1a5W9tN4ryXhSsJkTYGSQuxoIuyN3MJdCG7xFZ1k9YLP-QgDQy_FtRfvUGEwqq7YS3CQFPU5xQ95-qxARB4Wluk7B6quf89dCF3AnPkc4nBsxkAkO8qI3JvHpJAEhXFTzh741xwccoYTsc9L6T5SgwC5PxEvhAMKf1tVrpiFKqaaqX69utJlFoeoM4GgSHd3MWybg_oOz0C1D4arXmq9bb1g8wp5XzfbRLQmvXaMjIJEuBg-5zQYF6QyD48dpm9jX1jMzLE64cf0mURHzarQO4BREA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qgogB9WDEYBgYYIysycHu8ezeb8V6LHbLzWmY0I4pS_ku-CSk_PxWadlD7pUtUTT57MZVWh1vVOMOYbuDyqtsSNRu15E5sb_TprUUo4xi0Ni7qO_YLq5DzEmc2AqUEA29c2b-QElYBD5Yp1CsF7lZfaGq85er9eeJpnhmlvkqGOtnaHu5Dk4D23Tk7mGn9SnUiYDhlQfBnLgAyEdHzeiY4TFqNx8b8oyzWCMevNNR1Zpwt9kdiWWZUjZN8XMc_oPMFpWlCBtx_O_SwVNFkIjMAVRXvD66Ja-CI8iWnpv8gaDWij8rg8GLPLZij3zYch67EvSJT_6cik0EjcNtDaMCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fGIzbZ4fkq27-ANBBqNlyA_Hg5f2BQDpXh9B6fGRD9oRyi5LhqnSM1MbvQF2-RDunKTbVz4zZmaOnlHjNIUEAbi9dHAPk0F2VJTnGkuLfDItrySijVn3iauCL8YzHWLdt_a454LUAzL0_8NvD2o_MHjrGCb0FTrhbOPL9vGFbPI4n5n12hIiBfhuBCIdRGgxLcCSie6GHj-jyrsBwuVQhDoL-Cnz-HKg5NamP3lA5kcr_niFXsdW_h3gJpzFGrIVDTUdN9jnu0RxWN2ITNyNiJyVf5Kj4X9OofrqRGBJI6BT2FvpkbmkSNMB1oj0n50GQUPKfvDKzLryXhcwRAwldg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
شروعش که اینجوری بوده خدا ادامشو بخیر کنه..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/91440" target="_blank">📅 01:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91439">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
یدیعوت آحارونوت: در گفتگویی که کمی پیش به پایان رسید، نتانیاهو به ترامپ اطلاع داد که قصد حمله‌ای قدرتمند به ایران را دارد. رئیس‌جمهور آمریکا اعلام کرد که اگر چنین حمله‌ای انجام شود، آمریکایی‌ها در آن شرکت نخواهند کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/91439" target="_blank">📅 01:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91438">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: اسرائیل و ایران هر دو ضربات خودشان را دریافت کرده‌اند و منطقه به درگیری یا حملات بیشتری نیاز ندارد
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/91438" target="_blank">📅 00:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91437">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
پروازهای فرودگاه امام از امشب تا اطلاع ثانوی متوقف شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/91437" target="_blank">📅 00:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91436">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/U2i67D4Z0c7d8LFmo8Uett_-_JBGTmMeGpnTTE4S_r6rVgJAal3QZdTQfPupO0JpoRhy-HrKaQDovbD-GHBpqk2LIcu20x3gT-ipAjOKbkMqSRWwV1xCu-GSP3cNrY_rSrKJK54ae0W0aw2HxDbAVLcs4CFRhqwV03wbp1HZzW63TPIub9_Ykt6T2Naxy6yRTr3c32bXC4HhRZntwsPM4w4RNsNT6mti48J7ZOPKO2C4ayDlaFhJUEqALKoLnN_P-wRrfOcELB53d439vXPctd4cvKmaspiVlxhGLcmMlWOKRRWeoj2R7NfvvY4V3IrU_c79MLGXLXF3uhAqgBgY8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوریییی :
🇪🇸
Miguel Blazquez :
خولیان آلوارز 100 درصد به بارسلونا خواهد اومد
‼️
وقتی باشگاه پیشنهاد 130 میلیون یورویی رو ارائه کنه، او بازیکن بارسا خواهد شد
باشگاه در حال کار روی مراسم معارفه با حضور تماشاگران در نیوکمپ است
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/91436" target="_blank">📅 00:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91435">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jowdc1Ae1mF4GdbzrnxSi4CxljujnZlKFDiHbTnxJVIsorXyXpCyqPRLFojPs6IaKaPT00BOd_DzA_1TnX3DA28uTIRk1ZLf-kac5NZpSQiRGBk8JIrdluGwfFLXtmsn9B59n-NMN-sjGIklJ-kvQCJIKRimhRYHAb50nwX4U0e4m1etyjjkLgY9ItaeGQ83yDONumHX5I28nepMqrB2ixb8wT14Uee9PcgQEPuM5Clkkd7bD5KoqODVfsNtxE4Il-QXXdzjEp0vbOakN-5UtiFAXx9gdf8lkxvBnVl8ix2h61KW033VhNdyYOyX2yV-Ka9SeyqKL4kO7vtVzug9VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرفایی که ترامپ تو تماس تلفنی به نتانیاهو میزنه تا آرومش کنه و جلوی حمله رو بگیره :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/91435" target="_blank">📅 00:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91434">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFRdRL8kGJOiUXdB16IctrzzwJKLzM_1n-R6ELZRJbKoeCDGzrEtGlfI1464bEKExvwLlHb1CTIzIQVozFIxXld6ehi4OK-jfIdNGbe_PCoUAkfIqmqryZhF6H5WZUFDe8aSAYqAxqEwUt4Qh6waWkNaURSnfwMbBXBsl6q8vbI0PpfsK6eUgOka0g5JeqSR5_GEVibG0IympZ9FRoo7lnAd_twyiaVZm2dZ7YCJMjQjvwknBUrWpDKhzYURuwZdM_Wge95oKfb0MaDfaFxdQNfSZDnXabPosV8xSHNx3w6b-wUu_xZcUGXTVoC9hnH04s8U8uLJd6kZIgIRQ7tNHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه چیز به نفع کارلتو در جریان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/91434" target="_blank">📅 00:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91433">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc3b1eadd2.mp4?token=cvZzForzokulMT35YgwTqNn1lxttu64nAM9gJAMtojihQ4Vsw-3IyAFkcGZlOBCuWByt4cj4hlGtwh_PCQzzLHqRt9SPbV9Eq2iDpHFXt9LPi8KRdGnRacRBA-rxCoBu3lDv6v2gjMLVgj-5KEwbP_lN2fuMNLjuoDCWP7bcTBb4WxFbRipCX2KKXu4qaMjzgJFTA3KWgnzszVAgvsoMT-b4WQszAyaSTBoB1TQEB9h0jbwFO5rTUicp8Sj619Z3fEAJXcmNZ3B7EBHiCEKKquI-y8ULVCVMsjolT9DvPg-OILBOy5Uti-Vt3Tj3NgoulLkYUSZ20mTNoAqFORycLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc3b1eadd2.mp4?token=cvZzForzokulMT35YgwTqNn1lxttu64nAM9gJAMtojihQ4Vsw-3IyAFkcGZlOBCuWByt4cj4hlGtwh_PCQzzLHqRt9SPbV9Eq2iDpHFXt9LPi8KRdGnRacRBA-rxCoBu3lDv6v2gjMLVgj-5KEwbP_lN2fuMNLjuoDCWP7bcTBb4WxFbRipCX2KKXu4qaMjzgJFTA3KWgnzszVAgvsoMT-b4WQszAyaSTBoB1TQEB9h0jbwFO5rTUicp8Sj619Z3fEAJXcmNZ3B7EBHiCEKKquI-y8ULVCVMsjolT9DvPg-OILBOy5Uti-Vt3Tj3NgoulLkYUSZ20mTNoAqFORycLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
#
فوری
؛ فاکس نیوز :
با اینکه ترامپ به اسرائیل گفته پاسخ نده اما اسرائیل همین الان جلسه اضطراری تشکیل داده تا تصمیم بگیره آیا به حملات اخیر پاسخ می‌ده یا نه؛ و اگه پاسخ بده، چطور این کار رو انجام خواهد داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/91433" target="_blank">📅 00:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91432">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paHdePMaQlL1y_gVTPUN7JcroUWOYqLXzqPJA-PiR7xLwFM7dyj1QOvqXdqBbeD0HDCB39eDgOiuKCHAwazJKrm4MrazYKIMOjpfd30P_jPzo9vumj6j8HSDNoetXjLJcwxYhbv_DWqVZfux1KO7I8CrKqUyuC9vWdvFOHEpzXsHBA1MyvH-wUxsScrLIYtvDIgWIH7aEAARZ7JLuNlNbvU0KyLxTnGAGzcXMOfa3ET1X60Ci3dLqZ8KigNCrvwr4G5ViSHY8U2V-MZmVGFEMkPsL_X0O3o83Lq9kj2jSUDCcC14E5p5Ea31QUNPK_xSSg4nFkydfjfcSmSnvy3bXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
مراکش
🇲🇦
-
🇳🇴
نروژ
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
یکشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه ردبول آرنا
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
مراکش در
۱۰
دیدار اخیر خود،
هفت
برد و
سه
تساوی کسب کرده است.
✅
نروژ در
۱۰
دیدار اخیر خود،
هفت
برد و
دو
تساوی کسب کرده و در
یک
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر مراکش
۲.۵
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر نروژ
۳
.
۸
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۱.۵
- ضریب:
۱.۲۷
🧠
وقتی از بازی لذت نمی‌برید، متوقف شوید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/91432" target="_blank">📅 00:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91431">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
بیانیه رسمی ارتش اسرائیل در واکنش به حملات موشکی سپاه پاسداران
‼️
‼️
رژیم تروریستی ایران در تلاش است معادله‌ای جدید ایجاد کرده و با انجام شلیک مستقیم به خاک ما، در واکنش به حملات ارتش اسرائیل به ضاحیه ، قواعد جدیدی را تحمیل کند - ما اجازه چنین کاری را نخواهیم داد!
‼️
‼️
ما در واکنش به شلیک‌های بی‌وقفه حزب‌الله به سوی شهرک‌ها و مناطق مسکونی شمال اسرائیل دست به حمله زدیم. اجازه نخواهیم داد حملات علیه شهروندان کشور اسرائیل ادامه پیدا کند.
‼️
‼️
ارتش اسرائیل در دفاع و هم در حمله قدرتمند عمل می‌کند. سامانه‌های پدافند هوایی در سراسر کشور مستقر می باشند.
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/91431" target="_blank">📅 00:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91429">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IFU-ZEbp9QGHW9VyMccPzAebjqiiB_TJkuLIFfV7XEiqMbiP5V-C9TZ15oiglwWEBdhMQ54UrQO5F_kzjMTbZHKbTrJHApdBqbZJI2TplJh6d3RnptKjSODVdCJougwI0zjO7XeFpdu-LNpaUTLsbl9yuhsF_5VQno1jRjV3B5VhQwW0BGGAlQZSTbC4jqmhf4bXq9QyYYW9T6BojRT69F4-sfI_h6Q15I1AgAhDNn_KcIRrkzyLo7j_K2DnSo46Y75GLWYB2YsHV4B1lDzX3CCQQ54X4S-VfY6hXHx23kJsIslrT8KcXdHRDMEfHjILp5-t5hm73SLDDXZGYQsInQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qZcRH2v-HtfSEL-v-3hvrGFGc_Aodb1gV6Q5IYMvzA6-kguzOPa86-5wav32PKRtNUXFhgrFuNiCLBr2HoLQLQWs_qS0QpIoIuhTap0NCv5OebBBCKcOxtvRwgawV8jBNj6gDqBo46j6zXi7_VRIiyYMZzFBtpUYDs48-Z9nMojj0fmHJa8cM0zCI5yaIXRHbyZEFPOpSd_w_7nIsiAhLnskzIOlLKPaFj5nRtTGzyINuzVxM4UMzfDvKxo-WwFFJB53iRQGd-xcynOfEkwJpxSu5b6G0UlOg-cXknvtvYY3bP21wFh4t7WGI6f-CeWEp8RgFbM1cSX1WcVxzmmBJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇨🇭
فدراسیون فوتبال سوئیس از وجود مارهای سمی در کنار محل تمرین شکایت دارند.
‼️
اونا در ساعات گذشته به دنبال راه حلی در سریع‌ترین زمان ممکن هستن تا به محل دیگری منتقل شوند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/91429" target="_blank">📅 00:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91428">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
ترامپ : نتانیاهو جوابمو نمی ده اس ام اس دادم‌ نگران نباشید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/91428" target="_blank">📅 00:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91427">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
ترامپ : نتانیاهو جوابمو نمی ده اس ام اس دادم‌ نگران نباشید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/91427" target="_blank">📅 00:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91425">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
فووریی ترامپ:  اگه تا آخر هفته توافق شد میام تهران تاسوعا عاشورا غذا میدم تا ۱ ماه هم سیبیل و ریشامو نمیزنم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/91425" target="_blank">📅 00:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91424">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDU0mJeU3LTzSFDF_vyEqa0rZqTeB2_u8XcJBb-lalfmfTIZR7aTYvChmexcDdscTx-0K3dbAnyasAYoxJLOCCJJd-w7mJVCWpPu-d9VDwm8FJErstmoFSQAVRiLPIZJLSH8mxw_sUx1GS42U9pDvxkngR2VzuiOKdRdWnQm9C0mEzJ8pWkczoxK1IQaw4pUQEgYAIogDCkNVer-IQwikDt2m6c0frl5J64UpTyBmxfOrA989jACYXhMf9e9J7H-6U_BP-gZ44n4LgWynMwvlzH-tR7EbhdvgVvtiZhOp522SnvyaaPxuUgeWkqWynwYh8WS0C6cIHH7fEUPRXDizQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عزیز ییلدریم به عنوان رئیس باشگاه فنرباغچه در انتخابات پیروز شد و هاکان صافی را شکست داد؛ وعده هایی که صافی در صورت پیروزی انتخابات داده بود:
❌
لوئیس سوارز
❌
میسون گرینوود
❌
هاکان چالهان‌اوغلو
❌
مریح دمیرال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/91424" target="_blank">📅 00:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91423">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
ارتش اسرائیل : ما به عملیات خود در سراسر لبنان در واکنش به حمله جمهوری اسلامی ادامه خواهیم داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/91423" target="_blank">📅 00:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91422">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9d9632a96.mp4?token=u9OMCIzslidBuKU5Phrgc5JqdHyxNLe_8lgyXkIe8QbtJurGQEpQ3-UywLOL6aaM_zYqa4MYLLQE5h__AQWFy0JxYpaGAwF8yrNkyhvKsCgHIDvrM-NYSsADjq6Ln3Xm9mvitxvP01dMo4mW2-N_kFVGgHodxoDGs0_ipXmlHykdIa6Iq3KskVG3-MwE_dZ9q9GX2bbRzi9IrOB5vM91qpbsCkf_ecSiG0yw5wcfdzmEHisE3ex5q4mws9CBgFaFkDcKihRETnxJOe5p4syfsrQxMS77NIcobfduMCJb8ai_zGgwFBmR-8kIMdqHJE-qEfqWE9DgZI6pRZq3Ju7pbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9d9632a96.mp4?token=u9OMCIzslidBuKU5Phrgc5JqdHyxNLe_8lgyXkIe8QbtJurGQEpQ3-UywLOL6aaM_zYqa4MYLLQE5h__AQWFy0JxYpaGAwF8yrNkyhvKsCgHIDvrM-NYSsADjq6Ln3Xm9mvitxvP01dMo4mW2-N_kFVGgHodxoDGs0_ipXmlHykdIa6Iq3KskVG3-MwE_dZ9q9GX2bbRzi9IrOB5vM91qpbsCkf_ecSiG0yw5wcfdzmEHisE3ex5q4mws9CBgFaFkDcKihRETnxJOe5p4syfsrQxMS77NIcobfduMCJb8ai_zGgwFBmR-8kIMdqHJE-qEfqWE9DgZI6pRZq3Ju7pbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
این بار ۴۶۲۰۴۷۲۱ ام بود باعث صلح شدم به خودم افتخار میکنم الحق که جایزه نوبل حق منه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/91422" target="_blank">📅 00:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91421">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">خوب برگردیم به فوتبال
مراکش تا دقیقه ۷۰ یک هیچ از  وایکینگ های کله کیری پیشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/91421" target="_blank">📅 00:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91420">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
فووریی ترامپ:
اگه تا آخر هفته توافق شد میام تهران تاسوعا عاشورا غذا میدم تا ۱ ماه هم سیبیل و ریشامو نمیزنم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/91420" target="_blank">📅 00:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91419">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
ادعای سخنگوی ارتش اسرائیل:
هم اکنون رئیس ستاد ارتش در حال تصویب طرح‌هایی برای حمله به ایران است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/91419" target="_blank">📅 00:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91417">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
ترامپ : هر کدام از آنها خوش گذراندند، اسرائیل حمله خود را داشت و ایران هم حمله خود را، ما به حمله دیگری نیاز نداریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/91417" target="_blank">📅 23:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91416">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی قرارگاه خاتم بالاخره پیداش شد: اسرائیل باید حمله به لبنان رو متوقف کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/91416" target="_blank">📅 23:47 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

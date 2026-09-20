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
<img src="https://cdn4.telesco.pe/file/D2MBelVTSvrvcdkQmlH1G2ecDqMFTw4hTw_YK09b2DIuid47tV_7AC242yoah_4XR7-EVVUtbkxSUMstu83Clnl7MqdTCBk-C6BkZ3GcihwsOjMA2tyJbXm77SE-jnEyFqFuC7KxLA9YwgbZPoS8UMv4l2FQ83lf220wq_LMegGqFoKRRqWospps-vCzjg-eBDNM0LUMEencf5fvTfyUBZ34DjWpO3viHvwk-k3IZhddsGZm76ga7xH7p2WVcDEoMN4Xm4BYOQx9BqqRHD1j3CXgFBn4F6T8vsOby3LQhjCMBflQYvgn2WNgp-QxwLXkJw_JNSJys-g-7L6NhlMa6g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 453K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-30 02:04:20</div>
<hr>

<div class="tg-post" id="msg-23661">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نور های هواپیما چه معنایی دارند @WarRoom</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/withyashar/23661" target="_blank">📅 02:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23660">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRyrD0ZxenoTyQw92x-ZIscOTtVd__Uzhtc_h7MUwUvTQcTtdchHSwrrGnsEB70uT7UUfmegmoihEkKto_dDCwppmfHWdGIDj0dV8Sjbjt9ZpF3aaCow7BbluZpO-Wb8-yLyknI5ow4gWNUYi9PlOiERP4dR18ITSFHAD4NlXCSOhMTnUKmn3XI26U81EYhEHEKn-8Qz-SMfiOkoKFTNFrceJhvv2Zl9j13NN7TBCfRZtc3TQr4HnqEdU7ntDk73H4GRElCerJrmCxAsmQWtnWTtABW4aFmNutNS7GWKnYj0TZdut20nnJ9Shbi25AoN_7KCPDcQhX0piJb0I2AMGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادمین های فیک بیسواد تلگرام این هواپیما رو جای یو اف او قالب کردن ملت
😂
😭
@WarRoom</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/withyashar/23660" target="_blank">📅 01:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23659">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd534fa54f.mp4?token=smJbA5s7t7rFe_ILyRVCDOfukjhmTO_w4w4JoX0QbUdOD3Cf2ugXRfrUD2rnurlwqo27TUpE7St1gs8jwmkZPe0As-Y46fcCGTXxV7MMUvvfaLbrU_XC5Wo3A7D9uk0PNHLGGwAJV3TGyX53Jq7QMwKu71CfUps2gvhzDzMxTed8evfPoSfxcjs-BENkCzHuX29ICfCopvuSi-VOXX4H6EVH9WPvXS0ShMMAYJtCTPnErE31cHPEGPcaolosMrD9b582IF4s0Bl3BYNzZw7bzxKpvNugwcxnbgfhokAfzAeJV1jDBVHfu-i4fVtFjl4SaaPCtUkkV_r6K_ocrU0_Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd534fa54f.mp4?token=smJbA5s7t7rFe_ILyRVCDOfukjhmTO_w4w4JoX0QbUdOD3Cf2ugXRfrUD2rnurlwqo27TUpE7St1gs8jwmkZPe0As-Y46fcCGTXxV7MMUvvfaLbrU_XC5Wo3A7D9uk0PNHLGGwAJV3TGyX53Jq7QMwKu71CfUps2gvhzDzMxTed8evfPoSfxcjs-BENkCzHuX29ICfCopvuSi-VOXX4H6EVH9WPvXS0ShMMAYJtCTPnErE31cHPEGPcaolosMrD9b582IF4s0Bl3BYNzZw7bzxKpvNugwcxnbgfhokAfzAeJV1jDBVHfu-i4fVtFjl4SaaPCtUkkV_r6K_ocrU0_Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادمین های فیک بیسواد تلگرام این هواپیما رو جای یو اف او قالب کردن ملت
😂
😭
@WarRoom</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/withyashar/23659" target="_blank">📅 01:57 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23658">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ارسالی : یه سوله کنار ‌ایران خودرو در آتش میسوزد
@WarRoom</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/withyashar/23658" target="_blank">📅 01:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23657">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گزارش صدای انفجار/پرتاب ؟!؟ سیریک
@WarRoom</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/withyashar/23657" target="_blank">📅 00:55 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23656">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28d06fec75.mp4?token=dVbo2cVZjgfZApFf9T3ciCHjDDdP22ubt49gSy885BZS9yU2vRoD-JGQwmCy5W38FAsgPa4kyG5diY5bZ07-RQ1B3Tk85qXbTYrWqsobNsG7M0rkxA3cygS8uxY4TYYahoifx5n2RmHuMIQxNYNIkL43RL4Siq6NU-35hDI6EYaKlGzXy-yj7bnxfXFVSrWH2VN1046EguQ5NKQzoaZ3Olr2isrBJiU9r_j0KHfQrvWGc3NGrRYMDnOVbM0vnoPFcaOYy36_9Jm8M2zzl2YnCFkqSImjd1CNz-1He_aq5Usbmj2XhnDuwJ9zPRFN3xABGyV-EHM76AFKElZmomv0Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28d06fec75.mp4?token=dVbo2cVZjgfZApFf9T3ciCHjDDdP22ubt49gSy885BZS9yU2vRoD-JGQwmCy5W38FAsgPa4kyG5diY5bZ07-RQ1B3Tk85qXbTYrWqsobNsG7M0rkxA3cygS8uxY4TYYahoifx5n2RmHuMIQxNYNIkL43RL4Siq6NU-35hDI6EYaKlGzXy-yj7bnxfXFVSrWH2VN1046EguQ5NKQzoaZ3Olr2isrBJiU9r_j0KHfQrvWGc3NGrRYMDnOVbM0vnoPFcaOYy36_9Jm8M2zzl2YnCFkqSImjd1CNz-1He_aq5Usbmj2XhnDuwJ9zPRFN3xABGyV-EHM76AFKElZmomv0Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر تتلو 39 ساله شد، امیدوارم مشکلاتش حل بشه، جاش تو این روزا خالیه.
@WarRoom</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/withyashar/23656" target="_blank">📅 00:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23655">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/el5R2NN3B2OIMBtOIdW_tXk5HSkPmgE0yqwsVzi2GC_N9Z3FdvpXLZb27NFfTdiarjrULm2Cah5vf9UhKVycXesqVkGoX0PfZdZ6YubHpcwE8nIPWGTwigUKUzOAt_fXQZ46mveG0JU2uqP5XramyKM8wMXp-mCOWrsp2rEavrhl7h44OUqtbhe_TcsL_ObXVDHTZcj32TKdKJOwiqC_apMQgpmvIWnS4gFbixS_s-qoQ3L4soRx8Wcibhi0OmEpfUyJF5IFtM7B12eU2UmFcbgiK5KGXqVgf8ZcO72nhdEHX6LwJn9H3Kxl39Hxt-eidi1L3LSnMY9u8UtBjcPIAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشت سوخترسان آمریکایی و دو سوخترسان از کشورهای حوزه خلیج فارس هم اکنون در حال انجام مأموریت در آسمان منطقه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/23655" target="_blank">📅 00:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23654">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/23654" target="_blank">📅 23:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23653">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/23653" target="_blank">📅 23:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23652">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وال استریت جورنال به نقل از مقامات آمریکایی: دولت ترامپ در حال آماده‌سازی برای تحریم‌های گسترده علیه دادگاه کیفری بین‌المللی است.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23652" target="_blank">📅 23:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23651">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بر اساس گزارش نشریه "اکسیوس" به نقل از یک منبع آگاه، ترامپ بارها از زلنسکی درخواست کرده است تا حملات به پالایشگاه‌های نفت روسیه را متوقف کند، زیرا این حملات باعث افزایش قیمت جهانی گازوئیل می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23651" target="_blank">📅 23:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23650">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23650" target="_blank">📅 23:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23649">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMC9Dql7e41zdCBTPcmNI-NNNuiKVGwcYHdXCWqHKgQkvLZ8-NOZAclU4Dd0t7OglPymAgGA2ZgqEGDTFLvb9Dso67YvADCIpTvZgl_HjE3WiBc7pjizDKTNmZmf59mDOB1iym6PyxQSRSOCDYCwC7NyiX-JIyTmOh3kYeWM2_Qp3rgotlLvNrvdM4YOCy0L7e2BLQnIsI6AjLlkASuEucXzDAnjy812tjARTLP6F8xrQ8yt-h-90fYgTlIvJiqwFowFLxKyt0xlN8MHebq0qbmtUnJXJWDutZh8fzHOGskhO42IokFNaff_zFG0xPDxMPL0Igl-9j0AZzCcKnZgjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفارت آنلاین آمریکا در ایران از تمام شهروندان آمریکایی حاضر در خاورمیانه خواست برای احتمال لغو پروازها و بسته‌شدن حریم‌های هوایی آمادگی داشته باشن
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23649" target="_blank">📅 23:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23648">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23648" target="_blank">📅 23:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23647">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مستندی برگرفته از اسناد محرمانه ی ایالات متحده درباره ی رخدادهای شب بیست و ششم شهریور سال ۱۳۵۵.  به همراه مکالمات رادیویی واقعی از گفتگوی خلبان های نیروی هوایی ارتش ایران با برج مراقبت و مرکز فرماندهی.ماجرا از این قرار است که شبی آرام در اواخر شهریور ماه حوالی ساعت 10 شب تلفن برج مراقبت فرودگاه مهرآباد به صدا در می آید و حسین پیروزی 35 ساله مسئول برج گوشی را بر می دارد. پشت خط خانمی با صدای نگران خبر از رویت چیزی عجیب با پره هایی شبیه پروانه های اتومبیل در آسمان می دهد...
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23647" target="_blank">📅 23:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23646">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBCpL670CsGRXrZTI9FAtxepujzNVvYAn2-Ygb7oDFShWmnVNJTizSj95T3IXxG-n6Ib3BlvtgNwhxXw9TGbyhOMh70QKnB8kK247rXsQvX6DpeFpSZh_KqN5L9C3UiTXhdmnpGjKaNomoF7_GzMwaw_0B7C_OqIEFISTSFdyKjj9ZhEKovG4LR91p1og0Bq7hL_g_l0snRfM1rlcLlEcQTqVYQ4bYEvIewG-FRl_cH8kEvzy_SBcIv6PhOs1uLbZhcPVkXP0AzLp9A_Y8vFDwX_fCZ5mZaUQMnNHBBRIqZ-hPZkqIPtVp0MkMTqPwDPxJ00BK4IuPeqXfTCnHxOdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از بى نظير ترين عكس‌های بشقاب پرنده در جهان (پارک جنگلى تپه‌هاى عباس آباد تهران) قبل از انقلاب
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23646" target="_blank">📅 22:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23645">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95feb353e9.mp4?token=gbhRvuWPUc4bepoAO0TGYS910LKKU2OmxtGXr-0TENlCXaD00X9uX38PlL2oVau-QqyZHxNZvaAlbcQiGOyAyBVDXxto-WfCCIZQ3eRd9EBIZ8ezCIiodjYT5dVOv6rv0FPx7YxpnhXH_kLoz9yV_ROb7vvQbgJ2lT0TVN91cqL-x-2wOVpD_wxH0yKKMfvVNHvcE8vmOU4cbiP81ZKJ2NxZnDps1OVj3O17OPla__z9U9d5ceCM93d8kqILr27zfHlG_C0G-Wy8jESAdm0diotduXwKCCunxgCvw5y7VBCZUz3OuoAto1-miE8bWQPnOhbqbgCv2nHIQs-JESTsbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95feb353e9.mp4?token=gbhRvuWPUc4bepoAO0TGYS910LKKU2OmxtGXr-0TENlCXaD00X9uX38PlL2oVau-QqyZHxNZvaAlbcQiGOyAyBVDXxto-WfCCIZQ3eRd9EBIZ8ezCIiodjYT5dVOv6rv0FPx7YxpnhXH_kLoz9yV_ROb7vvQbgJ2lT0TVN91cqL-x-2wOVpD_wxH0yKKMfvVNHvcE8vmOU4cbiP81ZKJ2NxZnDps1OVj3O17OPla__z9U9d5ceCM93d8kqILr27zfHlG_C0G-Wy8jESAdm0diotduXwKCCunxgCvw5y7VBCZUz3OuoAto1-miE8bWQPnOhbqbgCv2nHIQs-JESTsbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از بهترین فیلم‌هایی که در طول بیست سال تحقیق و جستجوی من در مورد فرازمینی‌ها دیدم، مخصوصاً این‌که در ایران است. هم اکنون توسط دیدبان اتاق جنگ با یاشار در اتوبان آزادگان گرفته شد @WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23645" target="_blank">📅 22:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23644">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6GqQna3fYIMwl1wba5ZiRkGALT7SthDrQCtGgVtd1lL3pppW0EM7F3nxf1d_iPTwvdFmGpqgupXzSftq51pypWdNZ-cHtIIx9_FcFH6LxvfaPTsLwfGYGcuTEe0gZEs0jtEuWVwzqYheKmAk97v4kjEgC5rrJrSlchLU3tpqnOdpothqHwP2g_XBHL-OvC-6G8PSwWx57ph_VLaj_CIK1FJl6Htvx0JrKdOE3IZZy3bRaHp8P85HZ6m0CWJOkgOp3_cTIi830ibT93p_95DdjtHWldlNWi3DJwhe439PjUZNVlOfSIFap7KNgx46_tFI4eXhTTK6dpqbAoEb3x7pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای عراقچی بعد از توقف کوتاهی در دوحه قطر دوباره به تهران بازگشت و میان انبوهی از هواپیماهای سوخت‌رسان و جنگندههای رادارگریز آمریکا عبور کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23644" target="_blank">📅 22:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23643">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یکی از بهترین فیلم‌هایی که در طول بیست سال تحقیق و جستجوی من در مورد فرازمینی‌ها دیدم، مخصوصاً این‌که در ایران است. هم اکنون توسط دیدبان اتاق جنگ با یاشار در اتوبان آزادگان گرفته شد @WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23643" target="_blank">📅 22:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23642">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5d2baa686.mp4?token=B8VJYfszYEW5n2UhkUC3uxYUcqkRecrY37hND_5PoNFeRCoIB6I-zwLRqst-r-p2yZaQZWixwkLIYF_GTgRLy8puUxPl2aYIjpO7yrW1NToQbihL2cag38V19Ixo_65j7hlmhn5M08eDHyY9kgT0SWs1CpGOyfVtiSshFPz-vWav8S1rqbue1I5qmENmNVtt64YPQpxU-_7QeT_FNPDa1CruWsVi-eAa4VZhczorp4sWxF3wMHneWfGeq7Vh1KE-UOI5PNa5WzhVC1D2hjZXm3Kwf0NeEWXnL2pcRuv1aAnTfUQe1k1NL0aftR9rWvZlYmeDIiEGaAYyXPoGXz0dFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5d2baa686.mp4?token=B8VJYfszYEW5n2UhkUC3uxYUcqkRecrY37hND_5PoNFeRCoIB6I-zwLRqst-r-p2yZaQZWixwkLIYF_GTgRLy8puUxPl2aYIjpO7yrW1NToQbihL2cag38V19Ixo_65j7hlmhn5M08eDHyY9kgT0SWs1CpGOyfVtiSshFPz-vWav8S1rqbue1I5qmENmNVtt64YPQpxU-_7QeT_FNPDa1CruWsVi-eAa4VZhczorp4sWxF3wMHneWfGeq7Vh1KE-UOI5PNa5WzhVC1D2hjZXm3Kwf0NeEWXnL2pcRuv1aAnTfUQe1k1NL0aftR9rWvZlYmeDIiEGaAYyXPoGXz0dFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از بهترین فیلم‌هایی که در طول بیست سال تحقیق و جستجوی من در مورد فرازمینی‌ها دیدم، مخصوصاً این‌که در ایران است. هم اکنون توسط دیدبان اتاق جنگ با یاشار در اتوبان آزادگان گرفته شد
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/23642" target="_blank">📅 22:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23641">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23641" target="_blank">📅 22:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23640">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23640" target="_blank">📅 22:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23639">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : جنگنده‌های F-22 رپتور هم‌اکنون در نمایش هوایی نیروی دریایی آمریکا در پایگاه اوشیانا در ویرجینیا بیچ در حال اجرای نمایش هوایی هستند. نمایشگاه NAS Oceana Air Show امروز، ۲۰ سپتامبر، در حال برگزاری است و تیم نمایش هوایی F-22 رپتور یکی از اجراکنندگان رسمی این مراسم است.
در نتیجه خبر پرواز پنهانی F22 ها فیک نیوز است
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23639" target="_blank">📅 21:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23638">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cdf7c3621.mp4?token=UjgrTTS2aQ9vXsH1nXFNw2bpZ3TuqLC_zOW-qnCRrNFUFypHp4RYukfJWmv4CrUsnFPZseBsoLiUrGDxXRwxxrX32iKS3l9v9OwUjVEmrIsTDoTj4o3OIa9HZQNyvtlzEGUgLjRHqyUSla_ySM4--_KaaluOBSMqFwHTJ1Ah03_JOASjRaGPApqx25f-rAZHc03TXYz4BDTfoaOEn-gMnhDMM6IKjSTpJ00UsB9vSF7nAhQ-I8hGmVnoYy3YIain-lK3Tf2xUdpPjuXIBxWT2wk4Bj2jiYQQtm7wfyFE5ucmtRBkYy0ZfL1tjgbmhIGZKMfxZIK8wdiek7H4kkSXVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cdf7c3621.mp4?token=UjgrTTS2aQ9vXsH1nXFNw2bpZ3TuqLC_zOW-qnCRrNFUFypHp4RYukfJWmv4CrUsnFPZseBsoLiUrGDxXRwxxrX32iKS3l9v9OwUjVEmrIsTDoTj4o3OIa9HZQNyvtlzEGUgLjRHqyUSla_ySM4--_KaaluOBSMqFwHTJ1Ah03_JOASjRaGPApqx25f-rAZHc03TXYz4BDTfoaOEn-gMnhDMM6IKjSTpJ00UsB9vSF7nAhQ-I8hGmVnoYy3YIain-lK3Tf2xUdpPjuXIBxWT2wk4Bj2jiYQQtm7wfyFE5ucmtRBkYy0ZfL1tjgbmhIGZKMfxZIK8wdiek7H4kkSXVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23638" target="_blank">📅 21:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23637">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : اسرائیل از امشب همزمان با آغاز یوم‌کیپور، حریم هوایی خود را به روی پروازها می‌بندد و فعالیت فرودگاه‌ها متوقف می‌شود. این تعطیلی مطابق برنامه یوم‌کیپور انجام می‌شود و حمل‌ونقل عمومی نیز در سراسر کشور متوقف خواهد شد. یوم‌کیپور، یا «روز کفاره»،…</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23637" target="_blank">📅 21:29 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23636">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حقیقت یاب اتاق جنگ :
اسرائیل از امشب همزمان با آغاز یوم‌کیپور، حریم هوایی خود را به روی پروازها می‌بندد و فعالیت فرودگاه‌ها متوقف می‌شود.
این تعطیلی مطابق برنامه یوم‌کیپور انجام می‌شود و حمل‌ونقل عمومی نیز در سراسر کشور متوقف خواهد شد.
یوم‌کیپور، یا «روز کفاره»، مقدس‌ترین روز در تقویم یهودیان است؛ روزی برای
روزه، دعا و توبه
. در این روز زندگی عمومی اسرائیل تقریباً به‌طور کامل متوقف می‌شود؛ پروازها و حمل‌ونقل عمومی تعطیل می‌شوند و کسب‌وکارها نیز فعالیت نمی‌کنند
@WarRoom
یاشار : جو چنل های دروغ و زرد رو باور نکنید</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23636" target="_blank">📅 21:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23635">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJm4WYcwyLwXjcJg9fwK4-rMFqGo6IPtUBJQRK-e1vlniHNpJ2swL24uSfCFOAMvqBIjRruLSFVFBAMNOQ9a-5kisYAVglzPUGOhvv5wntVntCrkKQ15WEDPL_HqUHLoXMVXlCcdns8xQiibI2-ap0_MD6lzTfa1O_WmvIW3DsrqUkVEVXHaZs5k6VZ_bzdbBHNY0-rxP8eNuuilAIz6Vh3LRlmQOB7zQ8dILYFhYLl2iKmcVMDL9iK9Bbznp25xUgZ6Cls2TFkj4gbMhGDmP-LZ-PMkciOGn7K5icM2pCLPE2oQC818SWDyWYBP0tMO5d1VFnwf_J2oxe8uFhMKZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : فرمول   اگه دلت تنگشده شده برای اتاق جنگ کامنت کن بگو،  پستم برا همه بفرست و اد استوری و کارای اداری رو بکن  https://www.instagram.com/reel/Ddg_S1cI4zx/?stkn=c2hueTJ1bmoybXI5</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23635" target="_blank">📅 21:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23634">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uz1KPkVBHA5gO_G5SaeY4r68t2euWJJ-lkrt5Hp5uxCrHZrbae0QijKLf4nWC30xCiPZ87OzLk70G4MuBftSh395hM42QULCubrEeZf9OFxtQYuy1p_25d_xG-U7uTSXxpePmccY6vaDkB0vGL_S0zCOha_aibobsOvEkdNisXxJI4e6rwmhHpkszzZmhObru-hXUsTod_AKXflsrI6NmFn3Pf-G8RZXkJ_cht1uD2TxK_sdHTwOKDMS2MfBReXSp1D1QqPzPKDOXD0LurzmzeZXsEHEnsmvKedhXlXDJ-P7CA5anXoI983q4ggSqfZoiKV-mRRNpojDPzs6vKx7Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره‌ای جدید نشان می‌دهد چین در یک میدان تمرینی در نزدیکی لوپ‌نور با ماکتهای جنگنده‌های اف-۳۵ و اف-۱۶ آمریکا، سامانه‌های پاتریوت و هواپیمای آواکس ای-۷۶۷متعلق به ژاپن را ساخته است.
اهمیت ای-۷۶۷ در این است که
ژاپن تنها اپراتور این هواپیماست و فقط چهار فروند از آن دارد
؛ موضوعی که می‌تواند نشان‌دهنده تمرین برای
سناریوی احتمالی درگیری بر سر تایوان و ژاپن
باشد. چین از سال ۲۰۲۱ در بیابان‌های سین‌کیانگ ماکت تجهیزات نظامی آمریکا و ژاپن را برای
تمرین‌های تیراندازی و آزمایش موشک‌ها
می‌سازد و اکنون با اضافه‌شدن پاتریوت و تجهیزات اختصاصی ژاپن، مجموعه اهداف خود را گسترش داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23634" target="_blank">📅 20:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23633">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZTnuvssLGglvwI9Ec2ifZj8CTtTJ76fEIzv88kXZs5-RBkWlFM6fleTIfgBdu_lRW-jNqcpxNJ8ZR7zR2-YA5HENJkpuPTTknnI_SCGxaIf3labbMz1GCz40-J-_S0rmwYfbQETgmPtHZ0a_duNls5VRH6qan807MVCJbiC7A7zeO15AUhoad_ooHweM0XovwamWiXjaFUM1r2Qvu-D3NZrV5D4f_BbaVYDPVIW-bMKoxUmnuHcVSpEl2SBQTUOeZMnaLDagbg856o8qd6LBHqs8bxFFI-b7iPfdBqZJho7v-CytVN0m2qzNLo5jWmaVaX9oGf4lA0KrdA0bxG-Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفارت ایالات متحده در عربستان سعودی اعلام کرد
که به دلیل شرایط امنیتی فعلی در این کشور، برای تمامی کارکنان دولت ایالات متحده که قصد سفر به شهرهای یانبو و طائف در غرب عربستان سعودی را دارند، مجوز ویژه‌ای لازم است.
این اطلاعیه پس از حملات موشکی و پهپادی سازمان انصارالله به تاسیسات شرکت آرامکو در یانبو و پایگاه هوایی پادشاه فهد در طائف منتشر شد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23633" target="_blank">📅 20:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23632">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogtw5Edi7LoR2jdvLe7rusWFQhqXJGsbMaFjf5t_SEjLDiQHEnzx5v5Kpox_P_xWLExA-CHmfab81DOI8j-JfokC_d1zOxJMoH3tiAuSaXCVVOnxFVB0p6AkX7S39qkGxDXmiVEJWiWR7LmIo6CJWuUOyO2uBkjSLrw0LLauqvU2ntMPlGBLo37UIzWCAIxsaQ9rw-g73UvKiGixwZKxXEBYtBDrzen-QT6H-pZRbPikwWmVcXoQDoPfg3tGlwwzl7jv4mKkTSijWyqoqG5hkfwS3f4EVHOszxe4iLrdFqsiPyJuSO3xFydR1yKFZktEtqqx6KOWheGS8dBpUqLDnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید پرزیدنت ترامپ دیس به خبرگزاری هایی که اجازه ورودشون‌به کاخ سفید رو نداده
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23632" target="_blank">📅 20:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23631">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qr_Z7yJa0xTHXAbYQRouZmGFrUCCAdtuGL8JV7Gi1iChBONALhQ5JOUg1r7_tIhGyEK_giMm4fBe0CfDmIq0n18KVCEpBGo3sYPxF8Fah3TriiZy23MPv6LEVTCnq8Kym7DNZlZBDZwJFnUNhcfewqHFg8R7ZWHsFu_gSZat7WWJ7Z-jXfsw9fZMFE7k4ZgsaPqVYMbuyENPbyp5DClDHJC1fM6cx5vn-wMzzAWCjipm2HfYleO4FRG8sm_TsH20Ch4d8Zca64no6SxRgii1gAM6IiVyGnZFfPaqFm3e3fcL-jO8_KS68lUQpnl5jp8KiZSDZXQu8o-p4k6KrBXxrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو سال پیش، در همین ساعت، تروریست عبد القادر و تعدادی از رهبران جنبش مقاومت، به هلاکت رسیدند. این خبر، ضربه روحی شدیدی به حسن خرسی، وارد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23631" target="_blank">📅 20:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23630">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دیدار وزیر خزانه‌داری آمریکا و معاون نخست‌وزیر چین در نیویورک:
اسکات بسنت، وزیر خزانه‌داری آمریکا، با «هه لی‌فنگ»، معاون نخست‌وزیر چین، در نیویورک دیدار کرد.
این نشست در آستانه
دیدار احتمالی دونالد ترامپ و شی جین‌پینگ
انجام شده است. بسنت درباره این دیدار گفت مذاکرات دو طرف به
زمینه‌سازی برای پیشبرد منافع اقتصادی آمریکا و دستیابی به نتایج ملموس برای مردم این کشور
کمک می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23630" target="_blank">📅 20:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23629">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">الکس پلیتساس، تحلیلگر امنیت ملی CNN:
به من گفته شده جلسه
دونالد ترامپ در کمپ دیوید برای بررسی و رایزنی درباره گزینه‌های حمله به یمن
برگزار شده است. پلیتساس همچنین گفت که همزمان، سفارتخانه‌های آمریکا در کشورهای خاورمیانه که ممکن است در صورت حمله هدف حملات تلافی‌جویانه قرار بگیرند،
هشدارهای امنیتی صادر کرده‌اند
و ترامپ نیز زودتر از برنامه اعلام‌شده به کاخ سفید بازگشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23629" target="_blank">📅 20:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23628">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ به فاکس‌نیوز : مایلم با پزشکیان در حاشیه اجلاس سازمان ملل دیدار کنم @WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23628" target="_blank">📅 20:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23627">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اتاق جنگ با یاشار : فرمول   اگه دلت تنگشده شده برای اتاق جنگ کامنت کن بگو،  پستم برا همه بفرست و اد استوری و کارای اداری رو بکن  https://www.instagram.com/reel/Ddg_S1cI4zx/?stkn=c2hueTJ1bmoybXI5</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23627" target="_blank">📅 20:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23626">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23626" target="_blank">📅 20:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23625">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اتاق جنگ با یاشار : فرمول   اگه دلت تنگشده شده برای اتاق جنگ کامنت کن بگو،  پستم برا همه بفرست و اد استوری و کارای اداری رو بکن  https://www.instagram.com/reel/Ddg_S1cI4zx/?stkn=c2hueTJ1bmoybXI5</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23625" target="_blank">📅 20:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23624">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMs2JI7ZszeVacAuS4213i7mbJTI-CMYfRon4l1V2ZE4_G68ZpiXFczUCPL5dCDVY0H1K2m7aCwu-Yhbv_lrVTLhZ72vpfWbEzDNh0FjZEOAz8PpOrMYU8rdffSHCE9nMOzRJm5C50fzWK_YGoRytILw8rVgfLtQGbwy3XPd14c1yJNq8br8O-xfAxMueyMpR9Peh4nLg-NO6V-40C0Mp_PKAFP9yfWOS1c6-v2XeG7gSFylc6s4TbkMKsU-MEXU5NyJw4O_KGzS2WNg0CQ1x6mlLX6r587vO67dkExytwLQjc8P9Sz3f1TG965YijdDVIKSSW7xN3VxCoZ9kCsk5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : فرمول
اگه دلت تنگشده شده برای اتاق جنگ کامنت کن بگو،  پستم برا همه بفرست و اد استوری و کارای اداری رو بکن
https://www.instagram.com/reel/Ddg_S1cI4zx/?stkn=c2hueTJ1bmoybXI5</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23624" target="_blank">📅 19:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23623">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23623" target="_blank">📅 19:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23622">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baJ2ZEMPPaD2X5uroEqxUbyvnHD3I7UpFGVXvlY_PpEu3x5pChcCyhUBpZHg5eHQFKXnMm3t_jMesxgDaOQm6pnMzixIeku4862hUMkn6lkBGZVlMri_2hk-tO-EDnuRgMZoLwLIEPFM39n5f4N7uQsct1rwuboPHz8g-OxoOrP2k0g0mXkNGr3mvb5vhWstKq7mli7T2tWVp8-SXgN9x4ojUzvnc8xpFXaYiWpYXrsf6hG9r6cU-FBJDieWkDo2J3T4bYEjo3QcALzr3uOxHdww4JIPLA6PZ4jYnFMkI1F_TPR5nLe_kDskQj2abTTP_8dDce4CNHt-eRS5Qgt6Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی از خرم آباد لرستان ، وضعیت امنیتی در سرتاسر این شهر
البته کل ایران همینه و حکومت پاپیون کرده
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23622" target="_blank">📅 18:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23621">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRQVtP-2LCkSiObkJibA9KweWvIV_bS5W1yIQks3Rrh5c2OsIZmaoLYHCfwO_VKFv71xDyyyC4g7Dmvs79YLyXfCp0ZZWVu8GQZ6TU2Jix5UUBhY8E9wDWOZd-gi7iuVjPFSocKtAXE5RZcj2xRDADHY0E_JHZ0__4VHvIegiQZu4N57m_6fsaexcuGJkcb6ZG4IlSJGO7kxFo04AMFVIo1nYZ4h5LTt2YwJWfNWMETIvNACojd__RWaboHWbz-_0wC3R5qT9wu3QQTMRAhv4jNzzRDkAE5zaeafUeEf3jxROam1Q1r6T_ReYj0zO_t9u0CIwTJM4NrclaK8_yIWDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام
:
نیروهای آمریکا در چارچوب
محاصره بنادر ایران، مسیر ۱۰۹ کشتی تجاری را تغییر داده‌اند.
این آمار نسبت به آخرین به‌روزرسانی سنتکام در روز جمعه،
۴ کشتی افزایش یافته است.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23621" target="_blank">📅 18:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23618">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eeb6a24e5.mp4?token=oP8f6YaQNejt40CXNDXSUJn98hBXhqeRQI7hpgDpWojvfv47JW4ajE2UraNZnNGZwJln1TTGvmLjr9gjFK9aXj2iw2GU8KQRt5lzSETcfZrsiRv-Af6RLpYMxCtDErrRueQGcFjyghhXbft06YyCHBfBxcuF_IvaRkSuPFEi05eRgSXO-KrjTBxVTqF-BGKgwP4CLxtZAZ5fcho50sFSbUbF4uXAwsBT4qZ5SnGLj0eR9RWrynneMOxKLWWgkhrAuUvwE3GitTkY93-ADA04PX6_XPkod_Y5crCDCI83pBHcFRHCzgwhlUQPWHWaETYwCboEbMWSrnKa2yZWz0sSvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eeb6a24e5.mp4?token=oP8f6YaQNejt40CXNDXSUJn98hBXhqeRQI7hpgDpWojvfv47JW4ajE2UraNZnNGZwJln1TTGvmLjr9gjFK9aXj2iw2GU8KQRt5lzSETcfZrsiRv-Af6RLpYMxCtDErrRueQGcFjyghhXbft06YyCHBfBxcuF_IvaRkSuPFEi05eRgSXO-KrjTBxVTqF-BGKgwP4CLxtZAZ5fcho50sFSbUbF4uXAwsBT4qZ5SnGLj0eR9RWrynneMOxKLWWgkhrAuUvwE3GitTkY93-ADA04PX6_XPkod_Y5crCDCI83pBHcFRHCzgwhlUQPWHWaETYwCboEbMWSrnKa2yZWz0sSvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز:
پدافند هوایی در اربیل، مرکز اقلیم کردستان عراق، یک پهپاد را در نزدیکی فرودگاه بین‌المللی اربیل سرنگون کرد.
فرودگاه اربیل محل استقرار نیروها و تأسیسات ائتلاف به رهبری آمریکاست و در ماه‌های اخیر بارها هدف حملات پهپادی قرار گرفته است.
هنوز مشخص نشده این پهپاد متعلق به چه طرفی بوده و آیا قصد حمله به فرودگاه یا نیروهای آمریکایی را داشته است.
همچنین تاکنون گزارشی از تلفات یا خسارت ناشی از این حادثه منتشر نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23618" target="_blank">📅 18:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23617">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9165e4cc1c.mp4?token=d8S_oeoy4kcSnZz9NQHP3tGnvoVqexqXwbd8_8sQlbmpC6lbDNIDQiDN1dRK2KI9nsxrbfp9fdGalFi3MD_XP6V5wP1raXcs9kZ6RyuHr0O4MSZoEZ1pwyIufdOjuE_mJDC4tvMAkImKMBu66xsokMI05-y3S3_9yAaBQY25XbubnbvJKSyb0Hrcf-w0M5KNcAJS-xcoG9JVCYk2YnuAal7-21aRBFPDVj_XRCxhJBzl_2vHmNwAECU_bIAlMnS-imdqtd48vsgBVVAVG5pMRJ8yfBl5mrEsE3awvUlGvfjgt0zNY0oiE6eKlCh1jHtiCabtnXeXN5CGL-YfNNuZJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9165e4cc1c.mp4?token=d8S_oeoy4kcSnZz9NQHP3tGnvoVqexqXwbd8_8sQlbmpC6lbDNIDQiDN1dRK2KI9nsxrbfp9fdGalFi3MD_XP6V5wP1raXcs9kZ6RyuHr0O4MSZoEZ1pwyIufdOjuE_mJDC4tvMAkImKMBu66xsokMI05-y3S3_9yAaBQY25XbubnbvJKSyb0Hrcf-w0M5KNcAJS-xcoG9JVCYk2YnuAal7-21aRBFPDVj_XRCxhJBzl_2vHmNwAECU_bIAlMnS-imdqtd48vsgBVVAVG5pMRJ8yfBl5mrEsE3awvUlGvfjgt0zNY0oiE6eKlCh1jHtiCabtnXeXN5CGL-YfNNuZJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به فاکس نیوز
:
برخی از مقامات ایرانی مانند موش‌صحرایی پنهان شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23617" target="_blank">📅 18:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23616">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل:  نیروهای ما در تمام جبهه‌ها در آماده‌باش کامل، مستقر و آماده هستند
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23616" target="_blank">📅 17:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23615">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ به فاکس نیوز : ایالات متحده با حوثی‌ها در ارتباط مداوم است و آن‌ها موافقت کرده‌اند که با ما وارد جنگ نشوند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23615" target="_blank">📅 17:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23614">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ به فاکس نیوز: با وجود هشدارهایی که به شهروندانمان در سراسر منطقه داده‌ایم. این هفته با هفته‌های دیگر در خاورمیانه تفاوتی ندارد
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23614" target="_blank">📅 17:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23613">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دونالد ترامپ به شبکه فاکس نیوز گفت: برخی از مقامات ایرانی پنهان شده‌اند و نمی‌توان افرادی را پیدا کرد که قادر به انجام یک توافق باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23613" target="_blank">📅 17:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23612">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپبه فاکس‌نیوز: من در حال حاضر در "حالت تصمیم‌گیری" هستم و اتفاقات بسیار مهمی در آینده‌ای نه چندان دور رخ خواهد داد. انتخاب‌ها اینها هستند: نابودی ایران، اجازه دادن به فروپاشی اقتصادی آنها، یا امضای یک توافق. آنها باید رفتار بهتری داشته باشند! @WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23612" target="_blank">📅 17:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23611">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3cbef80a4.mp4?token=t3vDMao6f7yDdGDXCw3lMBINUzwiINWliVw0kVFwnZWGMB80egp4ZJHTLUdKSpJXWyr9EjrrpI7SijeZcMo74GweI5Xu3vROLW1xmVkA3_HM0jBfH-1L69PdLc6EsXojnaq8kChSlEl_5ksSQL5I1-EZ-T653Y5Yp2LVah3NPo9C9oTeWOKg-YM85ba89LI9rZlo-Ro2lxV6uCrmWlLN21KeiJXR3TV4ut-UvE0kCiY39K8ots9IURQhwQJLABrDMp5J6T6MVMwMnGThqk-4k3oJTvEn7uiN9L8I56vdLuka5y-BtyCeDb8xyg0lIzchwQ9Xx0DH_fwJFO9tu5qbQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3cbef80a4.mp4?token=t3vDMao6f7yDdGDXCw3lMBINUzwiINWliVw0kVFwnZWGMB80egp4ZJHTLUdKSpJXWyr9EjrrpI7SijeZcMo74GweI5Xu3vROLW1xmVkA3_HM0jBfH-1L69PdLc6EsXojnaq8kChSlEl_5ksSQL5I1-EZ-T653Y5Yp2LVah3NPo9C9oTeWOKg-YM85ba89LI9rZlo-Ro2lxV6uCrmWlLN21KeiJXR3TV4ut-UvE0kCiY39K8ots9IURQhwQJLABrDMp5J6T6MVMwMnGThqk-4k3oJTvEn7uiN9L8I56vdLuka5y-BtyCeDb8xyg0lIzchwQ9Xx0DH_fwJFO9tu5qbQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به فاکس‌نیوز : گزینه‌های فعلی روی میز، محو کردن ایران، رها کردن آن به پوسیدگی اقتصادی یا رسیدن به توافق است.‌‌ @WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23611" target="_blank">📅 17:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23609">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ به فاکس‌نیوز : گزینه‌های فعلی روی میز، محو کردن ایران، رها کردن آن به پوسیدگی اقتصادی یا رسیدن به توافق است.‌‌ @WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23609" target="_blank">📅 17:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23608">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ به فاکس‌نیوز : گزینه‌های فعلی روی میز، محو کردن ایران، رها کردن آن به پوسیدگی اقتصادی یا رسیدن به توافق است.‌‌
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23608" target="_blank">📅 17:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23607">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رسانه های عبری : انتظار می‌رود ظرف چند ساعت آینده حمله‌ای قابل توجه از سوی آمریکا به «کوه کلنگ گزلا»در ایران یا حمله‌ای بزرگ به حوثی‌ها صورت گیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23607" target="_blank">📅 17:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23606">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZJ5RydnJEIdV-eiKf80Qn4GhwdqsaJm5NCWO0iDw2TYsQ6k3oSHU6np8hBGWfpmxpMwUoiuMLfflQdLpvRaEZOnAXRltjeQ-vkjJsiWeo6S2qgriUrb_f12GoJCGct_7T7JNvZuprlHif_gp-xaO8p47a_u75oQhexR_WZvDxY66cC6zNhb2bL9upqV4q2oA46G7Xl47P2c6gSjXEQlyqTiuqx_8DwGPHlkVZPsH_4sjXWMjVfvvBccijn2n1KCiZU-7cOfk3OEmSCTlKN678Dl-K8OPAAbu1-j-ew1oI6wnVvwpuFEjaEwFMdqknKfATTOQ6GUx44cUgt1ZC0inA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس تصاویر ماهواره‌ای «سنتینل-۲» داغ داغ امروز، پایگاه هوایی «العدید» در قطر مملو از هواپیماهای سوخت‌رسان نیروی هوایی ایالات متحده است.
این وضعیت نشان می‌دهد که در ساعات پیشِ رو هیچ‌گونه حمله آمریکایی صورت نخواهد گرفت، چرا که انجام چنین اقدامی این هواپیماها را در معرض خطر قرار می‌دهد.
@WarRoom
⚠️</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23606" target="_blank">📅 16:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23605">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">معاون سیاسی پیشین سازمان صداوسیمای جمهوری اسلامی اعلام کرد که در شب ۱۸ دی ۱۴۰۴ ، معترضان آزادی خواه به ۱۳ مرکز این سازمان در شهرهای مختلف حمله کردند و مرکز
صدا و سیما جزیره کیش به تصرف
آن‌ها درآمد.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23605" target="_blank">📅 16:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23604">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">العربیه: مذاکره‌ای در کار نیست و فقط جنگ تکلیف رو مشخص میکنه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23604" target="_blank">📅 16:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23603">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iz1fs8z4lNu5gaasbHJPoyknIrcDoLhK4ogeIv-c_H-GZcXRUDP6yj_Xe6QhENw-CpLbpuQCYGKaXja2lKizkpbwcMVX9r1ZcSoMdzcvx8iaKxNIG07SjY-B0i1suHDyscBCFXxWzLmZ4dMc6qMggomLq5WZEmx_TnSyE1GN06TB17faPL1GD2eVzmj3dzcKmqVopQh1HV3rM5ieGTrtcc8QJaaeAr3HwmDTdU6GUwD2R3e4f6ppWoroF_hsQP7Rt6ioybwXMpcvcLRFctmY2vC5cnmFj5FGwLQCOs_B8PHh5013YMJelgt92eUOUjrnM7OB8ZUo1HDsQhSklVumOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ
در‌تروث
:
به درخواست جدی ارتش آمریکا و با هدف حفظ امنیت ملی، موافقت کرده‌ام که
طاق پیروزی باشکوهی
را که طرح ساخت آن از دوران جنگ داخلی آمریکا، سال‌ها پیش، مطرح بوده و در
میدان مدور مجاور پل یادبود آرلینگتون
قرار دارد، به یک
مجتمع نظامی درجه‌یک و طاق پیروزی
تبدیل کنیم؛ مکانی برای استقرار و نگهداری و همچنین امکان استفاده سریع از
تعداد زیادی پهپاد
، به‌علاوه
تک‌تیراندازها روی سقف و در محوطه میدان
و همچنین نگهداری و ذخیره
مقادیر زیادی مهمات تک‌تیرانداز
.
هیچ تأسیساتی مانند این در هیچ جای دنیا وجود نخواهد داشت.
از میان ۵۹ شهر و پایتخت بزرگ،
واشنگتن دی‌سی تنها شهر در جهان است که طاق پیروزی ندارد، اما حالا خواهد داشت و با فاصله، بزرگ‌ترینِ همه آنها خواهد بود!
از توجه شما به این موضوع سپاسگزارم.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23603" target="_blank">📅 15:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23602">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/106a710ba4.mp4?token=hbaW9qltzvJ4TZ8EKbBAyCwsKtUz_HfxAQGllwXYVEIe0juF5BPaXSakJ72Q7pray5bXU-jz3b4w5rlKto4e7Veu1VfJX04ZM3ABfuUT3UCN0yeC69NtjJF-eXdPH7v_vzxC9EQGg9wVfOp2FAUoW9D7ZSMyGrIQDSka429957zNUm-nGG2TqlX_NrrX0QtKWLaQUWs0YT5DX8vq0LuH53Cu2prT709bfXcFseqkIJkGXuLrR9S0ohVEUbZLPGFa7CDtPfr5Fi21jv277TbYXT6gy9TMYWpLJeq5lQdtf1Nr4ePeYZinqauCAOxKhIhNFuvleIPgVvs5Hcw9afBk9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/106a710ba4.mp4?token=hbaW9qltzvJ4TZ8EKbBAyCwsKtUz_HfxAQGllwXYVEIe0juF5BPaXSakJ72Q7pray5bXU-jz3b4w5rlKto4e7Veu1VfJX04ZM3ABfuUT3UCN0yeC69NtjJF-eXdPH7v_vzxC9EQGg9wVfOp2FAUoW9D7ZSMyGrIQDSka429957zNUm-nGG2TqlX_NrrX0QtKWLaQUWs0YT5DX8vq0LuH53Cu2prT709bfXcFseqkIJkGXuLrR9S0ohVEUbZLPGFa7CDtPfr5Fi21jv277TbYXT6gy9TMYWpLJeq5lQdtf1Nr4ePeYZinqauCAOxKhIhNFuvleIPgVvs5Hcw9afBk9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی : موشتبی مفقود است
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23602" target="_blank">📅 15:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23601">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6RgLz3fkoaKkbS8CgfdlLmXukOaW7r7KMbLQSjn21vglyZivfLPx9SkwjFQii3Nf1ckP9jj7ybPaKWU1_V21z_XzNcPQDX0VJgi7G5cBcbZQVOI312uiU-FukPYDHQjZ_q2DaTCRmr3Ek5KbDaLIxdf41OBnlWCKNqZSUs0m_oYbmXg8bU4u-eGMdFfiqNuBb7uhrkRyLdP2PN0DmZwMMs17VD2Mafrv3AKXsYwCChBjUlURC2dKTbdyQV03vMYo4v2GyPMdvRaF8_InUavZwZZspj2RE32gpsTUPtGM1ytP6aAxynTEe5G0oT_8AXd15QoXmD1J0JR6tfxyzgHSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناو هواپیمابر آبراهام لینکلن در جزیره گوام مشاهده شد
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23601" target="_blank">📅 15:44 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23600">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">رویترز: Anthropic به‌صورت مخفیانه یک آزمایشگاه زیست‌شناسی در منطقه خلیج سان‌فرانسیسکو راه‌اندازی کرده است. این شرکت هوش مصنوعی در حال گسترش فعالیت خود به زیست‌شناسی فیزیکی و استفاده از هوش مصنوعی برای پژوهش‌های دارویی و زیستی است.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23600" target="_blank">📅 15:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23599">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">مهر: ایالات متحده مجوز لازم را از چندین کشور منطقه برای از سرگیری جنگ گسترده علیه ایران دریافت کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23599" target="_blank">📅 15:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23598">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">کوین‌دسک:
بیت‌کوین بالای ۸۰ هزار دلار باقی مانده و بازار رمزارزها پس از افت‌های اخیر دوباره تقویت شده است.
در آخرین موج صعودی گزارش‌شده، اتریوم حدود ۷.۳ درصد، XRP حدود ۸.۹ درصد و سولانا بیش از ۱۲ درصد رشد کردند و ارزش کل بازار کریپتو به حدود ۲.۶۶ تریلیون دلار رسید.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23598" target="_blank">📅 15:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23597">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">صداوسیما: حمله به ایران قطعی است و در وضعیت آماده‌باش هستیم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23597" target="_blank">📅 15:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23596">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خبر گزاری صدى‌البلد:
جان راتکلیف، رئیس سازمان سیا، به‌طور ناگهانی وارد قاهره شد و با عبدالفتاح السیسی، رئیس‌جمهور مصر، دیدار کرد.
طبق این گزارش، دو طرف درباره همکاری‌های اطلاعاتی و امنیتی و همچنین
بحران ایران و تحولات امنیتی خاورمیانه
گفت‌وگو کردند. جزئیات بیشتری از این سفر اعلام نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23596" target="_blank">📅 15:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23595">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">محسن کج بند رضایی در گفت‌وگو با الجزیرة:
اگر جنگی دوباره آغاز شود، کشتی‌های آمریکا حتی اینکه اقیانوس هند را ترک کنند ، در هر نقطه‌ای از این اقیانوس که باشند، هدف حمله قرار خواهند گرفت..
ما سرعت موشک‌های هایپرسونیک خود را از ۶ ماخ به ۱۰ ماخ افزایش داده‌ایم.
همچنین سامانه‌های جنگ الکترونیک خود را توسعه داده و پدافند هوایی‌مان را ارتقا بخشیده‌ایم؛ علاوه بر این، تاکتیک های دیگری نیز در اختیار داریم که در زمان مناسب از آن‌ها استفاده خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23595" target="_blank">📅 14:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23594">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نتانیاهو: نیروهای امنیتی ما در حال حاضر در تعقیب مهاجمی هستند که حمله را در بنیامین انجام داد. هیچ مهاجمی در امان نخواهد ماند، همچنین کسانی که به آنها کمک کرده‌اند. ما همه آنها را در غزه، لبنان، یهودا و سامریا پاسخگو خواهیم کرد. همزمان، نیروهای ما یک مهاجم…</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23594" target="_blank">📅 14:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23593">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بیانیه قرارگاه تروریستی خاتم‌الانبیا:
اگر آمریکا علیه ایران خطایی مرتکب شود، تمامی مراکز و منافع این کشور در منطقه هدف حملات مستمر، مؤثر و دردناک قرار خواهند گرفت.
همچنین کشورهای منطقه‌ای که با اقدامات آمریکا علیه جمهوری اسلامی همراه شوند،
شریک این اقدامات تلقی خواهند شد و دیگر نباید انتظار خویشتنداری نیروهای مسلح ایران را داشته باشند.
در این بیانیه همچنین آمده است که آمریکا با چراغ سبز برخی کشورهای منطقه
در حال برنامه‌ریزی برای ازسرگیری اقدامات علیه ایران
است
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23593" target="_blank">📅 14:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23592">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نتانیاهو:
نیروهای امنیتی ما در حال حاضر در تعقیب مهاجمی هستند که حمله را در
بنیامین
انجام داد.
هیچ مهاجمی در امان نخواهد ماند، همچنین کسانی که به آنها کمک کرده‌اند.
ما همه آنها را در
غزه، لبنان، یهودا و سامریا
پاسخگو خواهیم کرد. همزمان، نیروهای ما
یک مهاجم دیگر را که قصد انجام حمله در سامریا داشت، خنثی کردند.
من دستور دادم
ارتش و شاباک با نیروهای بیشتری در یهودا و سامریا مستقر شوند، محدودیت‌هایی اعمال شود و عملیات و بازداشت‌ها افزایش پیدا کند
تا امنیت شهروندان اسرائیلی حفظ شود. همچنین دستور دادم
خانه این مهاجم به‌سرعت تخریب شود
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23592" target="_blank">📅 14:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23591">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پولیتیکو گزارش داده محموله‌ای از قطعات اف-۳۵ که از استرالیا برای تعمیر به آمریکا فرستاده می‌شد، در میانه مسیر اقیانوس آرام به هنگ‌کنگ منحرف شده است. سه منبع مطلع گفته‌اند برخی از قطعات این محموله ناپدید شده و پنتاگون نیز مفقودشدن تعدادی از قطعات را تأیید کرده است. این اتفاق باعث نگرانی در کنگره آمریکا شده، چون هنگ‌کنگ تحت کنترل چین است و احتمال دسترسی چین به قطعات و فناوری حساس اف-۳۵ مطرح شده است. کنگره آمریکا اکنون در حال بررسی این ماجراست و هنوز مشخص نیست این انحراف چگونه اتفاق افتاده و آیا قطعات به دست طرف‌های چینی رسیده‌اند یا نه.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23591" target="_blank">📅 13:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23590">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رئیس مرکز امور بین‌الملل و مدارس خارج از کشور وزارت آموزش و پرورش ایران اعلام کرد
دولت کویت مدارس ایرانی فعال در این کشور را تعطیل کرده و مانع ادامه فعالیت آموزشی آنها شده است.
او این اقدام را «غیرقانونی» توصیف کرد. جزئیات بیشتری درباره تعداد مدارس تعطیل‌شده و دلیل اعلام‌شده از سوی دولت کویت منتشر نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/23590" target="_blank">📅 13:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23589">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کوین‌دسک: وزارت خزانه‌داری آمریکا مدعی شد پولی که کشتی‌ها برای عبور امن از تنگه هرمز پرداخت می‌کردند، از طریق صرافی ایرانی «بیت‌بانک» جابه‌جا می‌شده است
؛ بیت بانک از ماه ژوئن مبالغی دریافت‌شده از کشتی‌ها را منتقل کرده و در مجموع صدها میلیون دلار بیت‌کوین نیز به سپاه پاسداران رسانده است. آمریکا می‌گوید این صرافی تحت کنترل بابک زنجانی بوده و بخشی از زیرساخت مالی ایران برای دور زدن تحریم‌ها محسوب می‌شود.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/23589" target="_blank">📅 13:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23588">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رویترز:
سقوط بازارهای خلیج فارس پس از حملات حوثی‌ها ادامه یافت؛ شاخص بورس عربستان
۰.۵ درصد
و شاخص قطر
۰.۹ درصد
کاهش یافت و سهام آرامکو نیز حدود ۰.۶ درصد پایین آمد. نگرانی اصلی بازار، گسترش حملات به زیرساخت‌های انرژی و مسیرهای صادرات نفت است.
@WarRoom</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/withyashar/23588" target="_blank">📅 13:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23587">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WArHbAY18X4bQl2aHWHUUunbPWU2iJn3q_iUx_TUmVxogLBvlOQRvwD_gmw6QCQvjbZJ52XMlkYNWl0yfuO6w3xH-2Y6awsqxfXJMxMlZXW40Re7pnCQwWL7IcTlobKYampaq0Xkbw3Ngzm20qwKFpsdQG3Ja6BCD3LuScOAfOJYDLIim7vVu0gmfsTl3OVaIomT31rlLbhUvd_TcpmRzN9iPn0lT8gLYsXj6mkKTIFpefZHTQuHhuU0bRk39xutOI8s0WauVxJO0Q50F5ScFzintY-w4WNUbKVSFrWZ2hhuXM4XSZ_9mkhAqUsw4YrOpztxsw6plEORynwYYW4QIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : تصاویر ماهواره‌ای جدید نشان میدهد ایران در حال بازسازی سریع تأسیسات طالقان ۲ است: تصاویر ماهواره‌ای شرکت وانتور از ۱۳ سپتامبر ۲۰۲۶ نشان می‌دهد ایران بازسازی تأسیسات طالقان ۲ در مجموعه نظامی پارچین حدود ۳۰ کیلومتری جنوب‌شرق تهران را با سرعت…</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/23587" target="_blank">📅 13:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23586">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qf-PcoVOMpjofZ0j-h5wJkgEvZkSl8CYdEaWzIrbB6r7yn9yUpHpvDEUJTiI7xbxptWBBGThd0MHp7MDmhoTvZOEplCH7Lksiim8caHelQCJvO-oyHjdBjDg_-sMN1FtDcVHQGB9PXMuyCf2oilIkAEuvBZyAj10Kkwu_ACGBdcaGQ1iDoB5fZIZs6f5b5h1JJ0OrFoOoODCBADL_DYpeRBZoVF2Dn6IzVCWw76QROIovMb9CpPbp_R-K9wChpv5WUblQWpY1Q6LvYyioyM5HqApS_MCYNV0gcF0FxnxqEGfPU_i3tZupj8TjfgVQI2vXBE-nQYbjXayysObmPLN4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فناوری جدید برای مقابله با طوفان‌ها :
پژوهشگران با بررسی حدود ۳۰ سال داده‌های هواپیماهای موسوم به
Hurricane Hunters
چهار نشانه را شناسایی کرده که می‌تواند به پیش‌بینی بهتر زمان تقویت سریع یک طوفان گرمسیری کمک کند. این موضوع می‌تواند برای هشدار زودهنگام در برابر طوفان‌های شدید اهمیت داشته باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/23586" target="_blank">📅 13:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23585">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پژوهشگران پس از
۵۰ سال
منشأ یک گروه خونی بسیار نادر را کشف کردند. این وضعیت که
AnWj منفی
نام دارد، از سال ۱۹۷۲ شناخته شده بود و حالا مشخص شده به ژن
MAL
مربوط است. بیش از
۹۹.۹ درصد مردم AnWj مثبت
هستند و انتقال خون نامتناسب به افراد AnWj منفی می‌تواند باعث واکنش خطرناک ایمنی شود. این کشف به شناسایی این افراد و پیدا کردن خون سازگار کمک می‌کند و
سیستم MAL به‌عنوان چهل‌وهفتمین سیستم گروه خونی انسان
به رسمیت شناخته شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/23585" target="_blank">📅 13:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23584">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اسپیس‌ایکس مجوز بین‌المللی Starlink Mobile را دریافت کرد
؛ کمیسیون ارتباطات فدرال آمریکا (FCC) در
۱۷ سپتامبر
مجوز فعالیت بین‌المللی سرویس موبایلی استارلینک را صادر کرد. این مجوز گام مهمی برای توسعه فناوری
اتصال مستقیم ماهواره به گوشی‌های معمولی
است؛ فناوری‌ای که استارلینک قصد دارد در نسل بعدی آن، تماس، پیام، اینترنت و خدمات ارتباطی را بدون نیاز به آنتن زمینی در مناطق فاقد پوشش موبایل ارائه کند. البته برای فعال شدن این سرویس در هر کشور، دریافت مجوزهای محلی همچنان ضروری است.
@WarRoom</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/23584" target="_blank">📅 13:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23583">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رویترز:
یک پیشرفت مهم فناوری در چین اعلام شد.
شرکت چینی CXMT اعلام کرده نسل پنجم فناوری تولید تراشه‌های حافظه DRAM این شرکت وارد تولید انبوه شده است. این فناوری با فاصله ساختاری ۱۱.۹۵ نانومتری طراحی شده و چین می‌گوید می‌تواند تولید تراشه روی هر ویفر را دست‌کم ۵۰ درصد افزایش دهد. این تحول برای چین در رقابت با
سامسونگ، SK Hynix و Micron
اهمیت استراتژیک دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/23583" target="_blank">📅 13:26 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23582">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">جنوب لبنان صدای ناله های حسن خرسی میاد @WarRoom</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/23582" target="_blank">📅 13:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23581">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">تایمز اسرائیل:
اسرائیل در حال بررسی نقش احتمالی خود در دفاع از عربستان است.
این موضوع در پی گسترش حملات حوثی‌ها و فشار همزمان بر مسیرهای هرمز و باب‌المندب مطرح شده است
@WarRoom</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/23581" target="_blank">📅 13:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23580">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رویترز:
آمریکا و چین امروز مذاکرات مهمی را در نیویورک آغاز می‌کنند.
اسکات بسنت، وزیر خزانه‌داری آمریکا، و هه لیفنگ، معاون نخست‌وزیر چین ؛ این مذاکرات چند روز پیش از دیدار ترامپ و شی جین‌پینگ در واشنگتن انجام می‌شود
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/23580" target="_blank">📅 13:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23579">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یاهو نیوز :
ارتش تایوان برای نخستین‌بار رزمایش مشترک با چند نوع پهپاد تهاجمی برگزار کرد.
این رزمایش شامل موشک‌های ضدکشتی بومی و سامانه‌های HIMARS نیز بود و رئیس‌جمهور تایوان گفت ارتش در حال تطبیق خود با جنگ مدرن و افزایش تهدید چین است
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23579" target="_blank">📅 13:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23578">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">رویترز:
ایران اعلام کرده تنگه هرمز تا تحقق شروط تهران بازگشایی نخواهد شد.
محمدباقر قالیباف، رئیس مجلس ایران، گفته بازگشایی تنگه به اجرای تعهدات آمریکا و برآورده شدن شروط ایران بستگی دارد. همزمان محسن رضایی اعلام کرده تهران هفت شرط برای آغاز مذاکرات با واشنگتن از طریق میانجی‌ها مطرح کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23578" target="_blank">📅 13:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23577">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">رویترز:
رهبران جهان این هفته برای نشست مجمع عمومی سازمان ملل به نیویورک می‌روند.
نزدیک به ۱۳۰ رئیس دولت و کشور در این نشست حضور خواهند داشت و جنگ ایران، بحران اوکراین، بحران انرژی و خطرات هوش مصنوعی از موضوعات اصلی هستند. ترامپ قرار است بار دیگر در مجمع عمومی سخنرانی کند و پزشکیان و نتانیاهو نیز در برنامه سخنرانی دارند.
شی جین‌پینگ به نیویورک نمی‌رود و به‌جای آن احتمالا مستقیماً در واشنگتن با ترامپ دیدار خواهد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23577" target="_blank">📅 12:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23576">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فرمانداری دزفول اعلام کرد صدای انفجاری که دقایقی قبل در بعضی مناطق شهرستان شنیده شد، به دلیل منفجر کردن و از بین بردن مهمات بوده و مربوط به حادثه یا حمله جدیدی نبوده است
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23576" target="_blank">📅 10:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23575">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23575" target="_blank">📅 09:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23574">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23574" target="_blank">📅 09:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23573">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23573" target="_blank">📅 09:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23572">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f301cc57.mp4?token=cSRCdeT3Y00sXl9OPX9vRv1UPYvONDJmEfHoRR5Qw1ys6vdsFdDMCI8VHdr_8H8p2FUh9mBt5kcslvR9GbdPQeamdHwpWAPGiOYP8POhyvKO-NxkapQjTAip5c7olhQcA5AfodY_fJDiWzzOk_Yy-2qm0iysECULYk0KZaIJeQ8XdxsaK7072UmeqJKTt9wCD9eBDmRwvCpdnhzAv1GYuu1C7YaPVTmpNs1I1PKsWlaU_dWHBax3FqT0ITtgLdsTRgXn9HRRSTvR5Ojl7Ljhzxex_n6vqrOdwiNNjb4ztvjiYPOvFKXDZecyeJsPLYSbtsQWSmfApcgyLcRoSEXEqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f301cc57.mp4?token=cSRCdeT3Y00sXl9OPX9vRv1UPYvONDJmEfHoRR5Qw1ys6vdsFdDMCI8VHdr_8H8p2FUh9mBt5kcslvR9GbdPQeamdHwpWAPGiOYP8POhyvKO-NxkapQjTAip5c7olhQcA5AfodY_fJDiWzzOk_Yy-2qm0iysECULYk0KZaIJeQ8XdxsaK7072UmeqJKTt9wCD9eBDmRwvCpdnhzAv1GYuu1C7YaPVTmpNs1I1PKsWlaU_dWHBax3FqT0ITtgLdsTRgXn9HRRSTvR5Ojl7Ljhzxex_n6vqrOdwiNNjb4ztvjiYPOvFKXDZecyeJsPLYSbtsQWSmfApcgyLcRoSEXEqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب «محسن نامجو» یهو با صدای بلند تو خیابون شروع کرد به آواز خوندن که یه هموطن اینطوری رید بهش و با یه خفه شو کار رو بست تا مزاحم مردم نشه
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23572" target="_blank">📅 09:44 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23571">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6efb269a37.mp4?token=qyrs4OQOoafLA0ET5z-GgPa75jJ9t0d5LlAfV2UIDjYIBtxlUm1Dq6jji2o4h5qSh1HbOxdRbDURN7puA2Ui2_JWWhYEkHs0Sndb-43brXW7--uPXpDAQA5tm9cgOlDQb9MntMQf7rK3SEYMQ2HwgutgcNTHwYA2FGmrtg0rP91t2ITU7aVRTlOyRMtsNsFKZuszLACOegTEE8iLIlOFcraeM3DHcdeueKfTYJhhLdE1SAEpJBWC5QwXP5q0LePZ3SIfazO_K8Z9Fw6dJYtYwxSwS_UEcKr1Q5EK4NiLeiObJ-IrNlBm4dDryviL-y-8-_hLfebPcSvsoahj1gFQdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6efb269a37.mp4?token=qyrs4OQOoafLA0ET5z-GgPa75jJ9t0d5LlAfV2UIDjYIBtxlUm1Dq6jji2o4h5qSh1HbOxdRbDURN7puA2Ui2_JWWhYEkHs0Sndb-43brXW7--uPXpDAQA5tm9cgOlDQb9MntMQf7rK3SEYMQ2HwgutgcNTHwYA2FGmrtg0rP91t2ITU7aVRTlOyRMtsNsFKZuszLACOegTEE8iLIlOFcraeM3DHcdeueKfTYJhhLdE1SAEpJBWC5QwXP5q0LePZ3SIfazO_K8Z9Fw6dJYtYwxSwS_UEcKr1Q5EK4NiLeiObJ-IrNlBm4dDryviL-y-8-_hLfebPcSvsoahj1gFQdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاله سینا اشکبوسی جاویدنام ۱۶ ساله در مراسم کوروش کبیر دو از شدت تأثر از حال رفت
@WarRoom
💔</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23571" target="_blank">📅 09:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23570">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88e48ca2a7.mp4?token=tG-F3W7PaMYfhQY-CZZmLAKDm-tMJB2ogjOHC_mPBLA4pNMvfd9OuBnBtQLP9wQ9UyBe18dmm0vTNvJ8RyIUwQdusnmxwmUa2iUO6loVojkLRuM1RTMI3oe9_qPfldDEkZPg37TN40ekrm55pzS3R2eslLzzQG6ghQ4v25kL61RMn4uwHk-hXaflt6qa627jchgBu3GPtPr1vDvmZaIqD0cyKK0HF8EcvBfe7FTVFSqeVGKyfWnNR1RSqws_lNIrbCZqLS8j5ElixEuUbvJwQo0iZR1ffFg94qihYQ7N2w6_Gbcy898wHp97wfSYqIY_E4SZZfOuDX8Yu9IJmnOlGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88e48ca2a7.mp4?token=tG-F3W7PaMYfhQY-CZZmLAKDm-tMJB2ogjOHC_mPBLA4pNMvfd9OuBnBtQLP9wQ9UyBe18dmm0vTNvJ8RyIUwQdusnmxwmUa2iUO6loVojkLRuM1RTMI3oe9_qPfldDEkZPg37TN40ekrm55pzS3R2eslLzzQG6ghQ4v25kL61RMn4uwHk-hXaflt6qa627jchgBu3GPtPr1vDvmZaIqD0cyKK0HF8EcvBfe7FTVFSqeVGKyfWnNR1RSqws_lNIrbCZqLS8j5ElixEuUbvJwQo0iZR1ffFg94qihYQ7N2w6_Gbcy898wHp97wfSYqIY_E4SZZfOuDX8Yu9IJmnOlGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک هموطن با غیرت از مایک جانسون، رئیس مجلس نمایندگان آمریکا، می‌خواهد کار نیمه‌تمام را تمام کند و به این رژیم پایان دهد. مایک جانسون ماه پیش هم در سخنرانی خود در مورد حملات به ایران گفته بود که
ما سر مار را زدیم
و همچنین در ابتدای جنگ هم گفته بود مردم ایران دهه‌ها زیر یک رژیم تروریستی استبدادی زندگی کرده‌اند و اگر تغییر رژیم در حال رخ دادن باشد، این می‌تواند برای مردم ایران فرصتی برای چشیدن آزادی باشد.
مردم ایران باید برای به‌دست آوردن و حفظ آزادی قیام کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23570" target="_blank">📅 09:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23569">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22a2f841f0.mp4?token=OkX3BX1N82vta4zuVJIxxB3XKyLdceXP3iKLZ84qxRpyx4nvaxBvgzwekjbkiGk4pYNBFypeKZVuwMoE8oDBBQi7QrFqR0Umfy4iuZ-mEyHWSOY5TFUdc-culFHNf0zjAUPX4ST9w85jh6JnEmeGKiJ-S_LDP6kHvGYFpg-SbOZom5lAgIdvQ46jxvtmr-YE-sbUWqRa88e8FDUC4LS8kofPPtLDq1cyhBsSb3H-lbseFCSU-tpACJFWvZtPksgIB8LC0Ds08-qZ-dOA_UETVgaPkdvxeT5h-qZ1u9L8vkBneXPZXHHClhtIcbNFB9ARvxGfsFlARR9BEOG4HnZQMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22a2f841f0.mp4?token=OkX3BX1N82vta4zuVJIxxB3XKyLdceXP3iKLZ84qxRpyx4nvaxBvgzwekjbkiGk4pYNBFypeKZVuwMoE8oDBBQi7QrFqR0Umfy4iuZ-mEyHWSOY5TFUdc-culFHNf0zjAUPX4ST9w85jh6JnEmeGKiJ-S_LDP6kHvGYFpg-SbOZom5lAgIdvQ46jxvtmr-YE-sbUWqRa88e8FDUC4LS8kofPPtLDq1cyhBsSb3H-lbseFCSU-tpACJFWvZtPksgIB8LC0Ds08-qZ-dOA_UETVgaPkdvxeT5h-qZ1u9L8vkBneXPZXHHClhtIcbNFB9ARvxGfsFlARR9BEOG4HnZQMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏یه پیام اضطراری خیلی کوتاه ۱۷ کاراکتری (EAM) ساعاتی پیش روی شبکه HFGCS آمریکا پخش شد. آخرین بار بعد از شروع جنگ با ایران همچین چیز مشابهی شنیده شد..
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23569" target="_blank">📅 09:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23568">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">فیزیک
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23568" target="_blank">📅 08:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23567">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ویدیو اختصاصی زیبا از دیشب
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23567" target="_blank">📅 07:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23566">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دیدبان اتاق جنگ : ديشب چندتا موشك خورده ب قايق هاي سپاه داخل قشم  جزايره ناز سوزا ، شايدم قايق صياد های بسیجی بوده که میرن شهپاد های آمریکارو بدزدن بوده معلوم نيست ، ولي برخورد انجام شده
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23566" target="_blank">📅 07:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23565">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebf28a7f1e.mp4?token=jC1IO4swNPQSjvEoDEZaLy_rVTrpClo4rXhn1eTAAiC4B16FO_ocpPmhPmbHaBjTSLaycKjUt14xlSOiZCjZ3JZ5IsOwur-ShoMzh2_DVd2Lh8nsPtZORWEgkfPsdsSZ1Z7Vor5ICzV-8XBT3hp2cUUEhHUAXf4atuKwJHG88Ys7sTlCWuuLoaib8ocuVMHxxx2pHJU1z63MeDoLyKQu0XVDfqLQdNC-BrMdaE0RrFNTkC5LTLEyG3wdT8b4g6ibumEvaDyf27XYgklwOK0JBH4mC0NL3w_LzhcE3PA0Z3m1gEHQ-1YwK5s7m6S7a5I_rE2dMgNRiKUPo9W_PGX3kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebf28a7f1e.mp4?token=jC1IO4swNPQSjvEoDEZaLy_rVTrpClo4rXhn1eTAAiC4B16FO_ocpPmhPmbHaBjTSLaycKjUt14xlSOiZCjZ3JZ5IsOwur-ShoMzh2_DVd2Lh8nsPtZORWEgkfPsdsSZ1Z7Vor5ICzV-8XBT3hp2cUUEhHUAXf4atuKwJHG88Ys7sTlCWuuLoaib8ocuVMHxxx2pHJU1z63MeDoLyKQu0XVDfqLQdNC-BrMdaE0RrFNTkC5LTLEyG3wdT8b4g6ibumEvaDyf27XYgklwOK0JBH4mC0NL3w_LzhcE3PA0Z3m1gEHQ-1YwK5s7m6S7a5I_rE2dMgNRiKUPo9W_PGX3kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک فروند بمب‌افکن
B-1B Lancer
آمریکا امشب با پس‌سوز کامل از پایگاه
RAF Fairford
در بریتانیا برخاست. برخاستن با پس‌سوز معمولاً نشان‌دهنده وزن بالای هواپیما و احتمال حمل محموله تسلیحاتی سنگین است، هرچند در پروازهای آموزشی هم استفاده می‌شود. حدود
۱۲ فروند B-1B
همچنان در فرفورد مستقر هستند و این پایگاه از ماه مارس یکی از مراکز اصلی عملیات
Epic Fury
علیه اهدافی در ایران بوده است.
در اطراف پایگاه نیز برخی خبرنگاران و عکاسان هوانوردی شبانه‌روز در مستقر می‌شوند
و با هر پرواز سریعاً عکس و فیلم تهیه می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/23565" target="_blank">📅 06:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23564">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نوراد: یک جنگنده اف-۱۶ یک هواپیمای غیرنظامی را که وارد حریم هوایی ممنوعه کمپ دیوید در مریلند شده بود، رهگیری کرد. این حادثه ساعت ۱۵:۲۰ به وقت تهران (۷:۵۰ صبح به وقت محلی) رخ داد. جنگنده برای برقراری ارتباط با خلبان، شراره‌های هشدار شلیک کرد و سپس هواپیما را…</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/23564" target="_blank">📅 06:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23563">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">وزارت امور خارجه ایالات متحده:
احتمال تشدید درگیری بین عربستان سعودی و حوثی‌های تحت حمایت ایران , آمریکایی‌های خارج از خاورمیانه باید سفر به این منطقه یا عبور از آن را به طور جدی مورد بازنگری قرار دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/23563" target="_blank">📅 06:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23562">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b3db75582.mp4?token=TRRZgecfW5h0RV5qGUizrpK2u2bmlpazifF4OPVq2TH3V5T_5bR1_ffEn_otZO_kELykXynKbC8zK6ur_fLHFPfiqxfoRjWScI17I3E6bpmzF8pKIqriLzcXU0joqJLlqsF0qy-ytdWhFTSPNREM6aKOF6bglJriV6swYnk3oOMHRDwFBKEw_bthIT2x03GLhU4bLP9np01fj9XucHtOzkpe7DF3uIgiS-Mc5lmT6I1PqBBD-sSQsonqwjadE8u4n7kWi_6vz_bScr0MUnXhln8fFqWYKu1Qe77UgIWH8xCbVZBb0hCPKX0-pC12-pCz5awwlGgnFfg_zoJv9jw3tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b3db75582.mp4?token=TRRZgecfW5h0RV5qGUizrpK2u2bmlpazifF4OPVq2TH3V5T_5bR1_ffEn_otZO_kELykXynKbC8zK6ur_fLHFPfiqxfoRjWScI17I3E6bpmzF8pKIqriLzcXU0joqJLlqsF0qy-ytdWhFTSPNREM6aKOF6bglJriV6swYnk3oOMHRDwFBKEw_bthIT2x03GLhU4bLP9np01fj9XucHtOzkpe7DF3uIgiS-Mc5lmT6I1PqBBD-sSQsonqwjadE8u4n7kWi_6vz_bScr0MUnXhln8fFqWYKu1Qe77UgIWH8xCbVZBb0hCPKX0-pC12-pCz5awwlGgnFfg_zoJv9jw3tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی در رویداد «کوروش کبیر ۲» در تورنتو : «حماسه دی» نتیجه یک هیجان زودگذر نبود؛ پشت آن یک مسیر طولانی و پرهزینه بود. جمهوری اسلامی که در روزهای ۱۸ و ۱۹ دی سقوط خودش را قطعی می‌دید، دست به یکی از بزرگ‌ترین جنایت‌های تاریخ زد. ما امروز از همیشه باتجربه‌تر و مصمم‌تریم. هدفمان مشخص است: سرنگونی جمهوری اسلامی و رسیدن به یک ایران آزاد و آباد. چهار اصل اصلی ما هم روشن است: حفظ تمامیت ارضی ایران، جدایی دین از حکومت، آزادی‌های فردی و برابری همه شهروندان در برابر قانون، و اینکه مردم خودشان با رأی آزاد و عادلانه شکل آینده حکومت ایران را تعیین کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/23562" target="_blank">📅 01:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23561">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سفارت آمریکا در لبنان، بغداد، بحرین و اردن نیز هشدار مشابهی دادند. @WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/23561" target="_blank">📅 01:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23560">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سفارت آمریکا در اورشلیم به شهروندان آمریکایی در اسرائیل و منطقه هشدار داده است که با توجه به افزایش تنش‌ها، احتمال بسته‌شدن فضای هوایی، لغو یا اختلال در پروازها و محدودیت‌های تردد وجود دارد و از مسافران خواسته وضعیت پروازها و فعالیت فرودگاه‌ها را مرتب بررسی…</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/23560" target="_blank">📅 01:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23559">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7efc866236.mp4?token=o1ft_xnqaNajbHY3uVG5J_NOgX4YYvw7tlNjV78WnUZr2xYndTQc8rttxQEMTtFw0KFWSzlZPv2y88b9dx03pZfqiKIH69i-5KGk2kM7cv_zwwoPtpue8XfjWESr9sObf-OMPbDhsVXZ2CCoZ9rqSXJZ3lZb4-d702Zmg6l2QC3N7zw9NqUzuc5Lv6EzmnDN337BZjjVY23HSTjFoHLZiVACp7x9D-322atKxsbZYLbQceOQ7o4l4dxqwpOtT1dy-84zrfr3qAoK8oXikVzTmUdXjrPMTNu-_EJTgJQon0irsw7Zttmozz_dxUPOUD4P1CNpdGYgMvJW68gFiIui2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7efc866236.mp4?token=o1ft_xnqaNajbHY3uVG5J_NOgX4YYvw7tlNjV78WnUZr2xYndTQc8rttxQEMTtFw0KFWSzlZPv2y88b9dx03pZfqiKIH69i-5KGk2kM7cv_zwwoPtpue8XfjWESr9sObf-OMPbDhsVXZ2CCoZ9rqSXJZ3lZb4-d702Zmg6l2QC3N7zw9NqUzuc5Lv6EzmnDN337BZjjVY23HSTjFoHLZiVACp7x9D-322atKxsbZYLbQceOQ7o4l4dxqwpOtT1dy-84zrfr3qAoK8oXikVzTmUdXjrPMTNu-_EJTgJQon0irsw7Zttmozz_dxUPOUD4P1CNpdGYgMvJW68gFiIui2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/23559" target="_blank">📅 01:03 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/F64n2Ox_ZfqP2x1r_7p9hd8wQjQYsxt7wwfqWgfEKEW5LQ_9bOc9J_WSfkKEtALS1bVcw-FZiJ1OzDmxPUc_4tW9AkXnfBKvVP7t5a1-r0BGlxDicnhVelQ995_EnBdtJboAc8LvJ5IssDxtUdC7ZKMscsWht0h1XWMUuiUCIaPG2PwliKYJrRURSiA7tjn5vUTo_96iMrzWz02dEmsJIBRLL_J8ddYIYaVpjJ1R3-Arhkr4wiwb9dfJaHsitLucyWhvdDuVWY8NXr3EYhoXr9FIeKG6X0hB78Td-29VUw-Y3v9usvgOBdYwUUP352teABDs1ksUTbyq-WFLYi0myg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.44M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 18:08:14</div>
<hr>

<div class="tg-post" id="msg-661469">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41e56de999.mp4?token=GA4EZlfa1uqOxOhZU-Qzw7HXCdMaEPvktvBTSaD8rF-3rL2zcJ7ALfjhsRfygZcttgxNNQx6lJ2Sf9jWKQRwTGzwUfhgmuWHQKaQQYFGM5dyWMhDg1wFQMms9l486EnLOYV6QJ0OBaitMmN4McXt9ZFXQKMOIu35nhQyEJsHqStpkC-n2TJqTinJVh2T4I71_oGqiW1tSRpTOkg-onPJdYVDcQhVQ1p023oSS6hJKZSQcpuZNZG2nf3RyRm9pgNgfDwgsiX8HjrZ14Jk3s0DT9TkB7AfwJLrhCKAZq0QbaGDOG8SE7oFKJOa0V7T_rpQx4GscCmg1OL1AMq0xfQjMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41e56de999.mp4?token=GA4EZlfa1uqOxOhZU-Qzw7HXCdMaEPvktvBTSaD8rF-3rL2zcJ7ALfjhsRfygZcttgxNNQx6lJ2Sf9jWKQRwTGzwUfhgmuWHQKaQQYFGM5dyWMhDg1wFQMms9l486EnLOYV6QJ0OBaitMmN4McXt9ZFXQKMOIu35nhQyEJsHqStpkC-n2TJqTinJVh2T4I71_oGqiW1tSRpTOkg-onPJdYVDcQhVQ1p023oSS6hJKZSQcpuZNZG2nf3RyRm9pgNgfDwgsiX8HjrZ14Jk3s0DT9TkB7AfwJLrhCKAZq0QbaGDOG8SE7oFKJOa0V7T_rpQx4GscCmg1OL1AMq0xfQjMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اتفاقی عجیب جاخالی دادن کامیون سوخت روسی از پهپاد اوکراینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13 · <a href="https://t.me/akhbarefori/661469" target="_blank">📅 18:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661468">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMG8Gy_iXwNB6xmUCWCMIB-kJcmzYDnnYRWWzgBMF1zwDXQsURIirGYLDsLE3muolcxb5vC2A2IFKsvoTFpMcYOtvIvHHglwwblq4OeyvEI6xB0318BNZSkp_6fREdSevp783Kq2xXPk9aVcLYIXumMK4VStf13pIxEdG8ltcCzJbGk7CTPBuEXq5nAVIk2Mud-vhxRwkn47V6ON91J0EDVsSBw_u2Xya-FuSkymq3BMOe4lIO_-927e4pUS1uyPD0_onGA2FE3ZhbV3uj-nn_SAb3Fi2S_jFWVSu3pIa3105P5xIJCad-Tn3VC9CI0Y7SLr2sjxqcMYrNv2F6Mxog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج بی‌سابقه حذف حساب‌های اینستاگرام؛ باگ یا سیاست امنیتی جدید متا؟
متأسفانه در روز‌ها و هفته‌های اخیر، گزارش‌های متعددی از غیرفعال شدن و از دسترس خارج شدن حساب‌های اینستاگرام  در نقاط مختلف جهان منتشر شده است؛ موضوعی که صرفاً به کاربران ایرانی محدود نمی‌شود و بسیاری از کاربران در کشورهای مختلف نیز با آن مواجه شده‌اند.
امید مهربان، پژوهشگر حوزه هک و امنیت، در گفت‌وگو با ما می‌گوید: «از زمانی که متا سیاست‌های خود را در زمینه مقابله با حساب‌های جعلی، مجهول‌الهویه، ربات‌گونه و شبکه‌های فعالیت غیرواقعی تشدید کرده، حساسیت سیستم‌های نظارتی این شرکت نیز افزایش یافته است. این روند را پیش‌تر در جریان پاکسازی گسترده حساب‌های غیرواقعی و کاهش میلیون‌ها دنبال‌کننده از صفحات برخی چهره‌های شناخته‌شده مشاهده کردیم.»
به گفته وی، در بسیاری از موارد زمانی که یک حساب به‌عنوان حساب جعلی یا مشکوک شناسایی و غیرفعال می‌شود، ایجاد حساب‌های جدید با مشخصات مشابه می‌تواند ریسک شناسایی مجدد را افزایش دهد. استفاده از نام کاربری مشابه، اطلاعات هویتی یکسان، تصاویر پروفایل تکراری یا الگوهای رفتاری مشابه، ممکن است باعث شود سیستم‌های امنیتی ارتباط میان حساب‌ها را تشخیص دهند و محدودیت‌های بیشتری اعمال شود.
مهربان معتقد است: «بسیاری از کاربران پس از غیرفعال شدن حساب خود، از روی نگرانی و استرس اقدام به ساخت چندین حساب جدید می‌کنند؛ در حالی که این تصمیم در برخی موارد نه‌تنها کمکی به حل مشکل نمی‌کند، بلکه می‌تواند روند بررسی و بازگردانی حساب اصلی را پیچیده‌تر و زمان‌برتر کند.»
او تأکید می‌کند که بهترین راهکار، بررسی دقیق علت غیرفعال شدن حساب و پیگیری اصولی موضوع از مسیرهای رسمی است؛ زیرا تلاش برای دور زدن محدودیت‌ها یا ایجاد حساب‌های متعدد، ممکن است دامنه مشکل را گسترش دهد و ریسک از دست رفتن حساب‌های بیشتری را افزایش دهد.</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/akhbarefori/661468" target="_blank">📅 18:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661467">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ابلاغ دستورالعمل فروش ارز اربعین؛ سهم هر زائر ۲۰۰ هزار دینار
🔹
بانک مرکزی دستورالعمل تأمین و فروش ارز زیارتی اربعین سال ۱۴۰۵ را ابلاغ کرد که بر اساس آن هر متقاضی بالای پنج سال می‌تواند تا سقف ۲۰۰ هزار دینار عراق دریافت کند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/akhbarefori/661467" target="_blank">📅 17:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661466">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
سفر ترامپ به کمپ دیوید در شرایط توقف مذاکرات با ایران
🔹
در شرایطی که مذاکرات بین تهران و واشنگتن تحت تاثیر تهاجم رژیم صهیونیستی به بیروت متوقف شده است، رئیس جمهوری آمریکا آخر این هفته عازم اقامتگاه کمپ دیوید می‌شود.
🔹
دومین حضور او در این مجموعه در شرایطی انجام می‌شود که ترامپ در تلاش برای دستیابی به توافقی نهایی جهت پایان دادن به جنگ علیه ایران است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/akhbarefori/661466" target="_blank">📅 17:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661465">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbHzUdSYnbA4DRv-P_bgIlZRT6hB7zKW5ODSZslqPi2LekroOQrmUpQFqQdHGmxr-yEhkOd-_0uMzVIdBa0GU3Lwpcf37tH_kjGj0_2h_-GxNRnezVkT_o2utIIVCgRKOKFxwg9NkDu5LuarQcL3-xBacYuChStionTY2X5ufd16UKZvP4_pX9B7rKXmT_P3sDAMZ0ENc4StelcIJE47XI7z9RAPR39_L8VZPpxqj3md7v6nc1joXcwxiVpqZc8jA3gGLAfvYHJaVV488oIkpLQouXvg8qlnZLvn1uHd6x9MEIMGywEvIEbXi5ay78j4StTI1mRsmdTtLwUgaqk4cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدام گروه خونی در جهان رایج‌تر است؟
🔹
O+ رایج‌ترین گروه خونی جهان است، اما در اروپا A+ بیشترین سهم را دارد.
🔹
O- می‌تواند به همه خون بدهد، در حالی که AB+ تقریباً از همه دریافت می‌کند.
🔹
توزیع گروه‌های خونی در جهان یکنواخت نیست و هر منطقه الگوی خاص خودش را دارد.
@amarfact</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/akhbarefori/661465" target="_blank">📅 17:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661464">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
خبرگزاری رویترز به نقل از وزارت امور خارجه سوئیس: ما همچنان یک محیط محرمانه و قابل اعتماد را برای تسهیل گفت‌وگوها فراهم می‌کنیم
🔹
دیپلمات‌های کشورهای مختلف که هم‌اکنون در این روند حضور دارند، به تلاش‌های خود برای برقراری گفت‌وگو ادامه می‌دهند.
🔹
به دلایل…</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/akhbarefori/661464" target="_blank">📅 17:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661463">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9PyMudf89LT_lGaxLVy8ffnVoEZPKCgzr16MfSe263-N9ixAgrFub_ggbAEpEUlgsOX1ujdCyj1cDcD1wqvVPhGUT7IqvM_HlA-PlfULo0uJ_clyuUCEdcMq32Kv6Hsxc2RcIOjTPhSAKrD2ZO3A8k-HNEJjfvJNkDozTmJ5s_qMgxJ7BmnL5px4ioeC01qG-mEvbhSCePqsF_h56vU3QJ-ubczHTERyUtSJh8fmr-eZ6RS9p074CVxPcqjJffTSAzpQGb_1w77kAJ1C6rAad3N6Wr1XuvDg6ds5Dn-0K6vb4DZUi8dt-4Tx-kT9qqf4bTYAWpXeZFhUHpyeGUkwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازی صعود؛ رویای ایران و نیاز بلژیک | نتیجه بازی چه خواهد شد؟
🔹
تیم ملی فوتبال ایران شامگاه یکشنبه در یکی از حساس‌ترین مسابقات مرحله گروهی جام جهانی ۲۰۲۶ به مصاف بلژیک خواهد رفت؛ دیداری که می‌تواند مسیر صعود هر دو تیم به مرحله حذفی را تا حد زیادی مشخص کند.
نظر شما چیست؟ کامنت بگذارید
👇
khabarfoori.com/fa/tiny/news-3224518</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/akhbarefori/661463" target="_blank">📅 17:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661462">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e98b351dd.mp4?token=uUjjiJvNOijdryuXqdW7iWU3YWu7EfwiUTJtHwgfDeHLytrSdqC7pOQYkoumsXt6nI31BcTiCihDIFCII9goO6X_iRSPqNLo4vG-QBOvcxipEcPM9OouFBwP_T8SPtiMcnmtlBjGiDpM8BiQtKPjC2_obhSFdAyGmFhipzXUDtsxmxTBTQkV7X7SJX__BlHQ4Uf3QaN4zNVV3erCh-y_uSMlyj6_FaK4NYlOs9kfIuFNTDlhmyjfyT1brqtl1sZ8xlqsGbgGBp4bvTQFzhU5yZJMGSaMGePKdjuvnEkP1uGmzY3XbOxU9C3QaNpp3EJst2SBMHsGcmL6LXBULQrpcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e98b351dd.mp4?token=uUjjiJvNOijdryuXqdW7iWU3YWu7EfwiUTJtHwgfDeHLytrSdqC7pOQYkoumsXt6nI31BcTiCihDIFCII9goO6X_iRSPqNLo4vG-QBOvcxipEcPM9OouFBwP_T8SPtiMcnmtlBjGiDpM8BiQtKPjC2_obhSFdAyGmFhipzXUDtsxmxTBTQkV7X7SJX__BlHQ4Uf3QaN4zNVV3erCh-y_uSMlyj6_FaK4NYlOs9kfIuFNTDlhmyjfyT1brqtl1sZ8xlqsGbgGBp4bvTQFzhU5yZJMGSaMGePKdjuvnEkP1uGmzY3XbOxU9C3QaNpp3EJst2SBMHsGcmL6LXBULQrpcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمایت از ایران در خیابان‌های نیوزیلند
🔹
شهر اوکلند در نیوزیلند شاهد برگزاری تجمعی اعتراضی بود که در آن شرکت‌کنندگان با برافراشتن پرچم‌های ایران، فلسطین و لبنان، ضمن تأکید بر لزوم برقراری صلح، مخالفت صریح خود را با سیاست‌های جنگ‌طلبانه ترامپ اعلام کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/661462" target="_blank">📅 17:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661461">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
تنگه هرمز مجددا بسته شد  قرارگاه مرکزی حضرت خاتم‌الانبیا:
🔹
وَإِنْ نَكَثُوا أَیْمَانَهُمْ مِنْ بَعْدِ عَهْدِهِمْ وَطَعَنُوا فِی دِینِكُمْ فَقَاتِلُوا أَئِمَّةَ الْكُفْرِ ۙ إِنَّهُمْ لَا أَیْمَانَ لَهُمْ لَعَلَّهُمْ یَنْتَهُونَ(۱۲ توبه)
🔹
نظر به بدعهدی‌ و پیمان‌شکنی…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/661461" target="_blank">📅 17:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661460">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
سفارت ایتالیا در تهران روز جمعه بازگشایی می‌شود
🔹
وزیر امور خارجه ایتالیا اعلام کرد که بعد از چندین ماه تنش در پی تجاوز آمریکا و اسراییل به ایران، سفارت این کشور در تهران  روز جمعه بازگشایی خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/661460" target="_blank">📅 17:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661458">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
جی‌دی ونس به فاکس نیوز: دیروز واقعاً ۱۶ میلیون بشکه نفت از تنگه هرمز خارج کردیم
🔹
ترامپ به ما گفت تنگه‌ها را باز کنیم، و حالا این اتفاق افتاده است.
🔹
این یک رکورد است، حتی از قبل از شروع درگیری‌ها نیز بی‌سابقه بوده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/661458" target="_blank">📅 17:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661457">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
تنگه هرمز مجددا بسته شد  قرارگاه مرکزی حضرت خاتم‌الانبیا:
🔹
وَإِنْ نَكَثُوا أَیْمَانَهُمْ مِنْ بَعْدِ عَهْدِهِمْ وَطَعَنُوا فِی دِینِكُمْ فَقَاتِلُوا أَئِمَّةَ الْكُفْرِ ۙ إِنَّهُمْ لَا أَیْمَانَ لَهُمْ لَعَلَّهُمْ یَنْتَهُونَ(۱۲ توبه)
🔹
نظر به بدعهدی‌ و پیمان‌شکنی…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/661457" target="_blank">📅 17:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661456">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‌
♦️
سخنگوی وزارت خارجه: ما تعهد را امضا نکردیم که اجرا نشود؛ رویکرد ما تعهد در برابر تعهد است
🔹
اگر طرف مقابل ار اجرای تعهداتش سرباز بزند ایران هم با تدابیر لازم پاسخ خواهد داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/661456" target="_blank">📅 17:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661455">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
خبرگزاری رویترز به نقل از وزارت امور خارجه سوئیس: ما همچنان یک محیط محرمانه و قابل اعتماد را برای تسهیل گفت‌وگوها فراهم می‌کنیم
🔹
دیپلمات‌های کشورهای مختلف که هم‌اکنون در این روند حضور دارند، به تلاش‌های خود برای برقراری گفت‌وگو ادامه می‌دهند.
🔹
به دلایل مربوط به محرمانگی، امکان ارائه اطلاعات بیشتری درباره حاضران یا محتوای مذاکرات وجود ندارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/661455" target="_blank">📅 17:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661454">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
درخواست‌ برای افزایش ۱۴۰ درصدی قیمت نان!
امیرکرملو، سخنگوی اتحادیه نانوایان تهران در
#گفتگو
با خبرفوری:
🔹
در حالی که نرخ جدید نان هنوز توسط وزارت کشور ابلاغ نشده، مسئولان صنفی اعلام کردند گرانی نان صرفاً به خاطر آرد نیست (آرد حدود ۱۲ درصد تاثیرگذار است)؛ بلکه هزینه دستمزد، انرژی و اجاره‌بها افزایش چشمگیری داشته است
🔹
با وجود ابلاغ نرخ‌ها در اکثر استان‌ها، تهران هنوز در انتظار ابلاغ رسمی است و نانوایان خواستار افزایش ۱۳۰ تا ۱۴۰ درصدی قیمت‌ها هستند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/661454" target="_blank">📅 17:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661453">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e38565964d.mp4?token=czdvgxsqXWSe6_tAaE34iO4aHN_g49kM3GgtYqmNbujDXVHrY3-Z-1LjMndQ6WOWYSTvJi8VeMo0-dqfjEnkGPUxsIQpA5rDHfGBJQVi4BHv4QlzaUcTlCWEmQ3XqO2ZLBR6R5Ed0TPeyqoKmdFgco0hytOi0aGJXxUUkpCLAJpwLj7wuUeA-E66qgvRejwq0H7vL6r-6szpkBOP83lAooK14W5KXi5BFTEKvVJ7qmVKfUN8knRIYzsbiqG_KQ-zn7_DxZVS78lOifCNEoNULIdh-k8TTPN4oTICcMoEM916CJiGK_Q938Xt4IeM6QXkqlCLTdT2eSZdSTs7U_hvlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e38565964d.mp4?token=czdvgxsqXWSe6_tAaE34iO4aHN_g49kM3GgtYqmNbujDXVHrY3-Z-1LjMndQ6WOWYSTvJi8VeMo0-dqfjEnkGPUxsIQpA5rDHfGBJQVi4BHv4QlzaUcTlCWEmQ3XqO2ZLBR6R5Ed0TPeyqoKmdFgco0hytOi0aGJXxUUkpCLAJpwLj7wuUeA-E66qgvRejwq0H7vL6r-6szpkBOP83lAooK14W5KXi5BFTEKvVJ7qmVKfUN8knRIYzsbiqG_KQ-zn7_DxZVS78lOifCNEoNULIdh-k8TTPN4oTICcMoEM916CJiGK_Q938Xt4IeM6QXkqlCLTdT2eSZdSTs7U_hvlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی‌دی ونس به فاکس نیوز: دیروز واقعاً ۱۶ میلیون بشکه نفت از تنگه هرمز خارج کردیم
🔹
ترامپ به ما گفت تنگه‌ها را باز کنیم، و حالا این اتفاق افتاده است
.
🔹
این یک رکورد است، حتی از قبل از شروع درگیری‌ها نیز بی‌سابقه بوده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/661453" target="_blank">📅 17:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661452">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a838204259.mp4?token=EZTXXUOG_DsjUtAw-Zt91ompJ2CUl0S2A4bY6KewADHl9O8RNaHBAKvQ_iD5TMq0Gs2pDQ0pRNYAEYr505JzbY7sP4H9wX9mLFRjF99qoTgxv3HOVobzHsEYry7hbZG7xAWvKTOp3wOZbC8wgM8bSYPrGTzEu4srrQAkGF5Sr6jlEs_pKeYExTrDvmIilH_M6bvMQUTMSSpBPjqEEYt02lhFNcLylqAVn8afdE0NSWjh4wKGI3EcO9KArNleftfiQ2Wa4WJMezuDms-bBIxQa-Gqi_EiWdC4nmfBuW9A-dOaNfeoQlMTNxKtGElb2n1yH6WGkcE0CziKn5pabqNzMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a838204259.mp4?token=EZTXXUOG_DsjUtAw-Zt91ompJ2CUl0S2A4bY6KewADHl9O8RNaHBAKvQ_iD5TMq0Gs2pDQ0pRNYAEYr505JzbY7sP4H9wX9mLFRjF99qoTgxv3HOVobzHsEYry7hbZG7xAWvKTOp3wOZbC8wgM8bSYPrGTzEu4srrQAkGF5Sr6jlEs_pKeYExTrDvmIilH_M6bvMQUTMSSpBPjqEEYt02lhFNcLylqAVn8afdE0NSWjh4wKGI3EcO9KArNleftfiQ2Wa4WJMezuDms-bBIxQa-Gqi_EiWdC4nmfBuW9A-dOaNfeoQlMTNxKtGElb2n1yH6WGkcE0CziKn5pabqNzMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی‌دی ونس، معاون ترامپ: من بسیار مطمئنم که می‌توانیم این آتش‌بس را حفظ کنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/661452" target="_blank">📅 17:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661451">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‌
♦️
سخنگوی وزارت خارجه: اگر بخشی از تعهدات طرف مقابل اجرا نشود کلیت تفاهم دچار مشکل می‌شود
🔹
طرف مقابل باید هرچه سریع‌تر تدابیر لازم را به کار بگیرد وگرنه کلیت تفاهم دچار مشکل خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/661451" target="_blank">📅 17:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661450">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mho1zYX_tewnTeKAFeIDBZBrigqBj2McKurzwC87E6P-fjia3O4PQ0fPyYZJejPezjFjRr4kH2cYTsht6NZV1ITWS8Jzj-f6jsLiBRU2YgFmywbPgUWnQhBrRqd8PR0GAbn-pibKmmLZrC8nYhWtjJH7w-y_VTxmykwpzLwYupUWerxs96x9vmn6naeJmUYw6WanfriXGRQcHCVUOV5WnMVyUQfYIZliTELOwE7yXhcyQ7xCW4O7gVu9D6bWzL_WIbRNB2S8qX2i8FFmm4iz7epf9PAeRyCQ4ejVS1FSKqu4rWxiqVDkogS9eftc5HUssxb0VtZrWwUr8AM5WMBlXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بهترین پاسخ ایران به حمله بزرگ اسرائیل به لبنان/ این اقدام تهران ترامپ را به وحشت می اندازد
🔹
شکی نیست که اسرائیل از تفاهم اسلام آباد راضی نیست و شکی هم نیست که تمام تلاش خود را می کند که تفاهم اسلام آباد را نقض کرده یا نابود کند. بهترین روش هم برای نابود کردن این تفاهم، حمله شدید به لبنان، نقض آتش بس و مجبور کردن ایران به حمله موشکی به اراضی اشغالی است. بدین ترتیب، جنگ، مجددا از سر گرفته شده و تفاهم از بین می رود.
گزارش تحلیلی خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3224502</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/661450" target="_blank">📅 17:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661449">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ritPiNDMhzL2AgZSZ2CCA0KMbL8XbjqrDFGUiCBPIonXYvnQ8cnEy07SF4g4OkwgQO_swZhHJ6Tn-Ae1lVPJxkxHmiE3cXH1L6HucRb3MIUxKUl5dmKYQJiJApPlNQe0zc8soFl5TBtc934rXV-mlC4Fj9vt4FSbehzi67kG5ZGz3tw5iYwJ0jWTkLQQ73H3U7SVEn3_7gW9apVSvumR-XRx944S0sViODORHwqeYMhZ5cf5ZUPC8naHq1PuDeUXzb3Gh7GE8jRftzKzBdNonNAkRksM9cNJkqnYsETTe40mFfrVTwUVAwkD6BSvbEz7PP_M4PSrSnyVGLcti5wuuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روضه حسینی
🔹
همراهان عزیز خبرفوری اگر در این ایام محرم در خانه‌های خود روضه برپا کرده‌اید، عکس‌ها و ویدئوهای کوتاه آن را برای ما ارسال کنید.
🔹
منتخبی از این تصاویر در کانال خبرفوری منتشر خواهد شد.
🔸
عکس ها و ویدئو های خودتان را با ما به اشتراک بگذارید
👇
#ایران_حسینی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/661449" target="_blank">📅 17:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661448">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: ما به تعهداتمان پایبند بودیم و طرف مقابل موظف است رژیم صهیونیستی را به توقف حمله به لبنان وادار کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/661448" target="_blank">📅 17:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661447">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: ما به تعهداتمان پایبند بودیم و طرف مقابل موظف است رژیم صهیونیستی را به توقف حمله به لبنان وادار کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/661447" target="_blank">📅 17:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661446">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: هیئت ایرانی برای پیگیری و مطالبۀ اجرای تعهدات طرف مقابل به سوئیس سفر خواهد کرد  ‌
🔹
در سوئیس قرار است دربارۀ اجرای تعهدات طرف مقابل مطالبه‌گری داشته باشیم و مشخص شود آن‌ها چطور می‌خواهند به تعهداتشان عمل کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/661446" target="_blank">📅 16:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661444">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
تنگه هرمز مجددا بسته شد  قرارگاه مرکزی حضرت خاتم‌الانبیا:
🔹
وَإِنْ نَكَثُوا أَیْمَانَهُمْ مِنْ بَعْدِ عَهْدِهِمْ وَطَعَنُوا فِی دِینِكُمْ فَقَاتِلُوا أَئِمَّةَ الْكُفْرِ ۙ إِنَّهُمْ لَا أَیْمَانَ لَهُمْ لَعَلَّهُمْ یَنْتَهُونَ(۱۲ توبه)
🔹
نظر به بدعهدی‌ و پیمان‌شکنی…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/661444" target="_blank">📅 16:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661443">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
حادثه در فرودگاه مهرآباد | پرواز شیراز به تهران از باند خارج شد
🔹
هواپیمای پرواز شیراز به تهران، هنگام فرود در فرودگاه مهرآباد، از باند خارج و در حاشیه باند متوقف شد.
🔹
در این حادثه به هواپیما و تاسیسات فرودگاه آسیب وارد شد اما خوشبختانه تلفات جانی و مصدوم نداشت.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/661443" target="_blank">📅 16:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661442">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWYt_ZoP99a80Mc4CK6UQmB4NSqDgtvuW_rlBRg9oGI_3H9N1MAeXwJpkDpXMQQXo8QfGJuWd4ACEuJC_SJTmysW1Zp0F9lYWDidzNC8XKiUn2MJgLaWrhLNraLerXHMwNUEL_ePRc5wuJ9mtIBaqfCxWhVPEHTlMOU-1Zmadq-LeUm6PRJiZdBoQ5ebwonCD19jz01swXp1sGOoSSb37MIpdLzyGWhOytHt1B52eMgDn6FOeLuBa3sv-2qtBo9T5gKt75rhUDT-l33NZW5MaV-DmUzjLJbmjza4Fe3xnC9RRbZR1PwJMUJBK0JW8OtoajSVNog86wlP3ArYTDYqvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ بار دیگر ملونی، نخست وزیر ایتالیا را تحقیر کرد
ترامپ با انتقاد از موضع ایتالیا در قبال جنگ آمریکا علیه ایران نوشته:
🔹
او زمانی که بحث جلوگیری از دستیابی ایران به سلاح هسته‌ای مطرح بود، از آمریکا حمایت نکرد. حتی اجازه استفاده از باندها و فرودگاه‌های ایتالیا را هم به ما نداد که یک دردسر لجستیکی بزرگ ایجاد کرد. با وجود اینکه آمریکا سالانه صدها میلیارد دلار برای حفاظت از ایتالیا و دیگر متحدان ناتو هزینه می‌کند، آنها از ما حمایت نکردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/661442" target="_blank">📅 16:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661441">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
ونس: به مذاکره با ایران فرصتی خواهیم داد
معاون رئیس جمهور آمریکا:
🔹
مذاکرات با ایران فردا امکان‌پذیر است و وایومینگ و کوشنر برای انجام این مذاکرات آنجا هستند.
🔹
اوضاع در مذاکرات ایران خوب پیش می‌رود و انتظار دارم به سوئیس بروم
🔹
ما به توانایی خود برای حفظ آتش بس اطمینان داریم.
🔹
به مذاکره با ایران فرصتی خواهیم داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/661441" target="_blank">📅 16:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661440">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
حمله مجدد اسرائیل به جنوب لبنان
🔹
رژیم صهیونیستی بار دیگر جنوب لبنان را هدف حملات هوایی خود قرار داد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/661440" target="_blank">📅 16:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661438">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
تنگه هرمز مجددا بسته شد
قرارگاه مرکزی حضرت خاتم‌الانبیا:
🔹
وَإِنْ نَكَثُوا أَیْمَانَهُمْ مِنْ بَعْدِ عَهْدِهِمْ وَطَعَنُوا فِی دِینِكُمْ فَقَاتِلُوا أَئِمَّةَ الْكُفْرِ ۙ إِنَّهُمْ لَا أَیْمَانَ لَهُمْ لَعَلَّهُمْ یَنْتَهُونَ(۱۲ توبه)
🔹
نظر به بدعهدی‌ و پیمان‌شکنی آشکار آمریکا نسبت به عدم اجرای بند اول تفاهم‌نامه‌ پایان جنگ، و در واکنش به نقض بی‌وقفه و مستمر آتش‌بس توسط رژیم صهیونیستی در جنوب لبنان و کشتار بی‌رحمانه و آوارگی صدها هزار نفر از مردم مظلوم این سرزمین و همچنین با توجه به عدم عقب‌نشینی نیروهای اشغالگر صهیونی از اراضی جنوب لبنان، اعلام می‌دارد تنگه هرمز به روی تردد شناورها بسته خواهد شد.
🔹
متذکر می‌گردد این گام اول پاسخ به عهدشکنی دشمن است و در صورت ادامه تجاوز گام‌های بعدی برای پایبند کردن دشمن به اجرای تعهدات برنامه ریزی و اقدام خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/661438" target="_blank">📅 16:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661437">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
شکستن طلسم ۳۰ ساله بوکس ایران در جام جهانی
🔹
مهدی حبیبی‌نژاد با شکست نماینده انگلیس مدال برنز خود را قطعی کرد و طلسم ۳۰ ساله بوکس ایران در این مسابقات را شکست.
🔹
او فردا در مرحله نیمه‌ نهایی به مصاف نماینده آمریکا می‌رود. #ورزشی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/661437" target="_blank">📅 16:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661436">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9975898851.mp4?token=UBkFiFDGl75p08zfB0xecXyiT89_owOEvx4iPwLSC9cAfDK4W5nN4YDoV2UMgQjjpPH5w4ayjc2VSWfizwQZkoodWAbSZUI1UtvWYSSsaFcYwj8wUWr9TlE3B4GcYHuYqL0SwMaDnzTBCCqvdAy_5RobBGPWvbI_EaMho-RtkoBSXZ5D5jM4edxwT1wszldO4iqbDsbkX4blM2SJloLBUDTBWNNIeUtcFg-NCcJANFYEW4RrtjzGfh8YjLcn0t-8Z715K4GeYZzzMAZ68JHN1e8n7e2iCG1hfmyETddQ8BLROSnSHnsYuuYGjEAm7XlHqR4ddtaXhwgE5AHco07oxBox7ioy6aNvkcvhKCaW_KwKvD1XISrUDIDGo9Lt3h_OqTA0qcQGlfJ_xPD31eQMHiZWsvRVcPdFNQfit-FytAOx7heVnuS-iHUZYSWGyLRGeGAQ3rCCrjxfqoP_cID9Qi-blsmq7q_6fcf4e8_NcSWTMjeb5OgB42L_R8YnJqp5PMsv2ZXBT4uJ3oEzfN6m8vsxmd-gC8pR2REAcJeJgE4l0RhuFrYzINwNoG8f11tf0yzYX2zyasKMRxrc2KL30EFMNwtaF1SJjmzy-eCERaYSV4dM7dNOowMw6XoTvdyBkIIMXaYEeGARMunlNDv5VDGZaUv3KGJ3i33Oeio93dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9975898851.mp4?token=UBkFiFDGl75p08zfB0xecXyiT89_owOEvx4iPwLSC9cAfDK4W5nN4YDoV2UMgQjjpPH5w4ayjc2VSWfizwQZkoodWAbSZUI1UtvWYSSsaFcYwj8wUWr9TlE3B4GcYHuYqL0SwMaDnzTBCCqvdAy_5RobBGPWvbI_EaMho-RtkoBSXZ5D5jM4edxwT1wszldO4iqbDsbkX4blM2SJloLBUDTBWNNIeUtcFg-NCcJANFYEW4RrtjzGfh8YjLcn0t-8Z715K4GeYZzzMAZ68JHN1e8n7e2iCG1hfmyETddQ8BLROSnSHnsYuuYGjEAm7XlHqR4ddtaXhwgE5AHco07oxBox7ioy6aNvkcvhKCaW_KwKvD1XISrUDIDGo9Lt3h_OqTA0qcQGlfJ_xPD31eQMHiZWsvRVcPdFNQfit-FytAOx7heVnuS-iHUZYSWGyLRGeGAQ3rCCrjxfqoP_cID9Qi-blsmq7q_6fcf4e8_NcSWTMjeb5OgB42L_R8YnJqp5PMsv2ZXBT4uJ3oEzfN6m8vsxmd-gC8pR2REAcJeJgE4l0RhuFrYzINwNoG8f11tf0yzYX2zyasKMRxrc2KL30EFMNwtaF1SJjmzy-eCERaYSV4dM7dNOowMw6XoTvdyBkIIMXaYEeGARMunlNDv5VDGZaUv3KGJ3i33Oeio93dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جایگاه VIP استادیوم سوفی آمریکا
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/661436" target="_blank">📅 16:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661435">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPp43CSYqI8vWSR9U29XdCq1ckln3ybHntI0LXIlHsmk_5rJi_nmdL_jFpqnK_9OjV2XUml0uLYlvW21cRP11EgKbaWsd26F2kJXxZBvHJR22c5j8X_cMJZcPGaytnEwqnmpby9aajxIFdJsequp-K3Lpdff2I9O3tAPLRxv4HgsG_1lVHDfdY4WThH5GVUtfTszZail4-cFU4B_Cc3K7U54txqHSYCuLELTHoN1TpSap3E9BbrlEpK4XeieNU3SiGUfvWEYSiRZh9lH1myHuRka2OEG6ENTusO1WKkLaBTDIzbzcxj5UZredeqy9Go_ZJ1C0qKLCo2LhKEnhKYOyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وام بانکی: طنابِ دار یا سکوی پرتاب؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/661435" target="_blank">📅 16:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661434">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dc19b6b7d.mp4?token=cdhUT0QwXqHOr4p1YxJoabz5Jen4pSE4tPfKmewCKPEBDfOUod0Y5WzzDztW6oAxGtFA4MO2_Wfb9nA1IJAHjLYscidVvmWl6R_HZmxbEILe6u5wiMIWH0WbRUaIx4F51sK-zectE4YAzEpAVaeEIXuzRUZDrefGDAWijCHJUpGjpkYtsRyKTfk_fBdYbPBMZPvWMvVnGABsYZ1LaeV0XJBBNeDyfIoTLpaA-vaw5rnpzovq3wfn97f8Lz-HKXPOqks99Oc-NNAESONzUSfcbbJYauFGtDszsAagPi3gjOJh8LI3NEJlcX9WWyRA-VFIvGLYeMe0yRByVZwVSDlZAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dc19b6b7d.mp4?token=cdhUT0QwXqHOr4p1YxJoabz5Jen4pSE4tPfKmewCKPEBDfOUod0Y5WzzDztW6oAxGtFA4MO2_Wfb9nA1IJAHjLYscidVvmWl6R_HZmxbEILe6u5wiMIWH0WbRUaIx4F51sK-zectE4YAzEpAVaeEIXuzRUZDrefGDAWijCHJUpGjpkYtsRyKTfk_fBdYbPBMZPvWMvVnGABsYZ1LaeV0XJBBNeDyfIoTLpaA-vaw5rnpzovq3wfn97f8Lz-HKXPOqks99Oc-NNAESONzUSfcbbJYauFGtDszsAagPi3gjOJh8LI3NEJlcX9WWyRA-VFIvGLYeMe0yRByVZwVSDlZAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر کشور پاکستان با عراقچی دیدار و گفتگو کرد
🔹
سید محسن نقوی، وزیر کشور پاکستان با سید عباس عراقچی وزیر امور خارجه کشورمان دیدار و گفت‌وگو کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661434" target="_blank">📅 16:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661433">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrsxKRNpD7RCDotIQLKniLfmBdB8930lEJQ7lDPs8UrdahT7FPBmIfd7yHXKdVQ2Sf2r4ljRgRvEDmlAZGSpuhL_6w7qtLANfkmw7x3kPT2lup0vSMJIlca665gVcTtTqBXyyLNSb8aE2LTRhzzM0u1MIdn-7ZfoT3UmEj0Nm057NC01ItD6Vm-_lyyLke7UodfAMI463MKV-nh95YohgL8lGCDXm586smP9OZaeEhPTyvcIKfcxdEvPZO5ys5WmVQny20K6EFv1cWjcwgeW5frsMXd2L8vqqABvyU-HeAwzuGNwSYAAjPSvAEyy8ubLQwKyIQAJ3H0w5i7B_piasw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ پستی درباره تاثیر خود بر آینده سیاسی نتانیاهو را بازنشر کرد
🔹
در تیتر مقاله آمده است: «ترامپ برگ‌های برنده را در سرنوشت انتخاباتی متزلزل نتانیاهو در اختیار دارد.»
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/661433" target="_blank">📅 16:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661429">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NIl-rlD3WOzbshc6louxZhdFXW88l25twSb2_4SHZ6EI-j13CCa9bOzGC-01LjEfrE-FcP3ApGjP3rwNP0zw-NKeHRDVSXAl6q2CYGFfGxnKbN2uWQFvbGBqoAE_VSeV9vFPL2U3LzEId213s-AGwvoMweDz6bAivAL7wx9TPTvUkA0ia0JjugKQpFIWnmG33L6wQOIRQevGL2kqyKvycFCgPW1GZFVPwbcYNc7kY1-qfiYiHLE6euBPtflgXzRgdEOFkQcQjvt5zvpYm9SPepb3kJl4w1ZWYVHnjnc4E77-4rNRWjrMADgeE5bfB18uSSuyRImIrUurvwsO68NXkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iebQHqmdWBJck4LJ3OBJfXs0UoX9Yhj9e3gmkafj1uSY1TFurUsSQQTDkT6jyQEA5xnhWgFHboZdtpSLxfrcrO082UqRB38LwSLvfkqohZnN_XWhZ7eEp3GXKS5BZ95m1eJ1Z81xL6JP19NHCOmFsDY-xgWKmNadUGuyY2uRiNiJafWInAzFowtcwrE_1J2kxcmpwaIxvBFIB_-v6lfDTJOTvn8A6koHEqtMyXtX2J2isorQci0BaF-UqJzF35ZepRgJsA6hAFnnmtrcfTtCt__nbjY5U7mFP8Lxs6YbyecbSeVwfDG5_6toVfEqHvqeT8S0oB7johIFKHE7gHs5Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WkCN4uamW_QtSoi5N0qLeVxPt1huXnjObgx_-1fv5mMZyzqgqZQbAatEo39c6JdYU7JJg-epetbK17mjEgh6U8wEylb_UT3HY7x34EG2bqB2sx4Ji8MJ2qLQcQESfB1kqNyZneldmyS4ivmBSZrnxFN46_xZNdEkoxgxFEvFK0ukI5aPFx3dkknwSDkYbmciNGl08EpCO8I6GHIy2UQf4LYjx2WMj0LtE2OUSaGcA3W7QTKfYkIFWo7LIFEIBoO8xRUOg-_vtc8QzX65CIHC9kVRZ_JapLOgjIwBBjB90ooWBB4J9Va5O-ozYCQgwPfXyZ3SJq563BQ2RMvnRVXFaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HX_1E8Ymuk84uDRptqcIogAjoJRVBbCvhYBlEyIbzVZUDgxijs-MYAclyzWbC3myyf9enFLHzyv-0tFReBoD5pwpV7C0nbW5M7k0W0PIzWKJJ5M2JdwYVRmdoVAS5GolSZVTpN5b-l_rAWkil2ZSdl8ZxvDwxtQA7vbQ7x5gtp6Is5NKw_iVns_iKknT-OGI08jpwVEW3Bbn_m3eYIoMkrsPVLFePfloCfgdS2czEKKdua1G6B8oeAOsEdMWAY_GXQcA8yGLRzG7rGDnJrvfGO0esn2XNNMqSvwRVOjZR0BPn9MKQwOJo391oFjqj4EOevGGzLWBvd7c8GGuEQH4Pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگه دنبال یک کیک خونگی خوش‌طعم هستید، این دستور رو از دست ندید!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/661429" target="_blank">📅 16:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661428">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2_EaXHyQXFZS8aoSNRzskWFOIJPRTHrXkv3UE3MCQHKuuE7XiqU3HCozVdkJJJKdskrOFxVeg1OoANuNdNdfhgRIRscR9Nv-A6Yt-04uY5OFX1GSnBv_PI7yzXd7xBj2J0l7UnT_yaA9O47bvtarl50UoSeZBxN-Ei2FZZo3Ge5WsVW27AlcdGRvuYt4xMtKR5gNNgfqAyz7F6zyPdBym9cg6KQlAFlcTJQ0rZF6opY-Oyl76dCcOsvrjpFFXsSJNobrT-CoUDsMzI1EguZt2FJ1-Rz3GqKMVtihOjfwtHqNA4POAkpcMkoTYC0vij9fIeKU0KmqYwlXAZmcYlVOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
کشف یک شگفتانه شورانگیز در «سیاره صورتی»!
🔹
تلسکوپ فضایی «جیمز وب» شگفتی شورانگیزی را در «سیاره صورتی» معروف کشف کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/661428" target="_blank">📅 16:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661425">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNx4LsxPa9tBJEvp3rMLXE7TrSi7ei7dZXc0eeph9JVAJljwY6b3gooWNuHPV99CyqjKTBK79hauoHsG9_8sOz7a_DF39Q71vyBlbeV489D4zlhDAYuQR_vLkwUSMwY4P8cxpkslg6Ta4mp0obFzuf5l8wIDhCZJE7a0ZeGPjWgTfrB406OMhYMOBHUysHi-exiDWDQAY9LsIwB0j6okYT8CF9Ug8uck7UCMdSWpPEkAvyFLfX6CmrI1GuXBGkOyIQLCaeqYB5TGsZODtLkL_H4BPj03VOCeMICFph5qrE5icP4nYI9FnEdGKbQIl9vhIRrxs-lP_B6YWg8rTEmOdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pq7JR9Wc5VF1nlm6hc50OKFZcmayMgM1y8STRON5PVdGkzQKlZJJYgTM7gSkq4V5ye975GLOpOu9EFwo1GSpWqT0FyLR81PvYFUBDCU7DUlWg9phPEIYx9OoLcUjWbSZrPqWp6JXnlZtyPq0-J37qwN65xitsKnM_riE578CHMI_R8COjs95_fEP-llzemelL7mw2nf-ApD8T9yv-isaYA4pM_oG9VQu5FayLwszonYNoQoDAQr_b3Y-TPvbMA0QVn-vnQ3t5U-y3_RIXqsNoiHRN9S3OIs49J0CnvkdzlZ_vo96vn71hhkWfzc10OkbZy4Oag4N0efkkoRABRhTBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ah4JoLD4TNv_kHDD9ow_RC7JsGFVhESSldJz8z6hgN5MyA2ZvXQovCaj6fizb9KuypPu35lhvqQAAMFeGSmjBqBdBvsCfNipdl4aQT38hPRttSt_0DOq8ENTEmXvAusCE18c1m5mzM-B-heMohN4Rj0MwLSIf9uSDTSA7bbgN2V6E4hDcJMi2L-xvzejrHAd3Zq9KuRdAEuf2spQBITBfFsICBSKpq6jkQcotZ-8zIslUMOcSf_QLh2TdZDqW0wj2zaccQ6upLoUXnuvcuJ4VPTzCyXNth_i1slqK6B59QEPXIlqo18OwN4idaAnDOZwjgAMbAQb5XNWfLImA98U2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حمله مجدد اسرائیل به جنوب لبنان
🔹
رژیم صهیونیستی بار دیگر جنوب لبنان را هدف حملات هوایی خود قرار داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661425" target="_blank">📅 15:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661424">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c0899f051.mp4?token=qeWUJgESQA9Aq_m1cs6exvr2OueCmRBkNqUGcE7mlj7AM5OhbXaNyJPDXfMU19GTysYXCJ0BWXSxcQLNGw0L-AaTkLSxeigokeg8NjIfn89ZoasBTCLgnbklT6TuM4dl8pSqtASNckZYKc125TY8ip6QWkPrFslL8F0ocFfCtWtSufL-6-Oywq5cRsL9xRW01oDoRjpDnR7NUphib7LKEES5MFTRDnbbCoWotTaia3J-nLzWxy53Bl7pNlMo8vXK4AUDRPKPU3Dyty7ehIeuEWglMNFvynkAPxbJe3ZwqmC3gS2z3oCjlvbjTj4P6WTKUhbeCg-v-xE2LJuudW7QrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c0899f051.mp4?token=qeWUJgESQA9Aq_m1cs6exvr2OueCmRBkNqUGcE7mlj7AM5OhbXaNyJPDXfMU19GTysYXCJ0BWXSxcQLNGw0L-AaTkLSxeigokeg8NjIfn89ZoasBTCLgnbklT6TuM4dl8pSqtASNckZYKc125TY8ip6QWkPrFslL8F0ocFfCtWtSufL-6-Oywq5cRsL9xRW01oDoRjpDnR7NUphib7LKEES5MFTRDnbbCoWotTaia3J-nLzWxy53Bl7pNlMo8vXK4AUDRPKPU3Dyty7ehIeuEWglMNFvynkAPxbJe3ZwqmC3gS2z3oCjlvbjTj4P6WTKUhbeCg-v-xE2LJuudW7QrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر یک از نقوش اصیل ایرانی، نماد چیست؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661424" target="_blank">📅 15:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661423">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKpFPDxjI1McbSb8rRWXp-sMD3rKCf1_qfAMH9AzR6NcHjXOYh8Zd85pxMZu6sKInwDulNyUhc9mjhA85gVTdeORZgJWcls33enVNXDye62UaRrFA88eVEfXvdUA48KtL9Mp0HRHrNhHuRpqbndH9IahjXw_TYLhbhtVVfhJQXd6j8dXSzLSXE61m2wijDjLM61i4BxuMp03yeTZFzkF3yYgD3Q-gwcQ_0A-DzX7wrltyWnafoUvAMBhYMHq2DWMPqg60P2QKU4lpfo606ExsvejB9MsrgULhvi25gQSkEumxwZhC8eLj3ILbW58tJd0b-kN5wT0NFgQMPX0eV4j9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
«سِروال»، سوپر مدل دنیای حیوانات
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661423" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661422">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
یارانه خردادماه ۱۴۰۵ به حساب سرپرستان خانوار دهک‌های چهارم تا نهم واریز شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/661422" target="_blank">📅 15:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661421">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/972310ae87.mp4?token=Cm443kqXA9kOJZkzfwiYFYjVE86xlkkaChLXVDxz12u-X4z_XXaNInq7KUSfJNfMQ11F5vOBh-7WZ0wqML9SoqdIVXBEJGDTZCWOQcFoSZEpxTuFs-6gwzVuDnUYyAjykkSVNjuQcbeCOVEr6o6F0B0ml_SNbPO4j6-wSdjofP_n8Xj36PgeXJMXzNNY8RDQEOVRoRqaGQh9JhXBTjhnKRBt4uqSfHk-xRHd0GlZRRFd7E_fCu35QaamDtRVFV3CbjW3GAnrxmzFz6TF5isdmzZ-BRHnjmiQN_oRB3pxPmLsYoNIE9fIV9N16xwl1HeWRnNdmILckzcFA71seGvUkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/972310ae87.mp4?token=Cm443kqXA9kOJZkzfwiYFYjVE86xlkkaChLXVDxz12u-X4z_XXaNInq7KUSfJNfMQ11F5vOBh-7WZ0wqML9SoqdIVXBEJGDTZCWOQcFoSZEpxTuFs-6gwzVuDnUYyAjykkSVNjuQcbeCOVEr6o6F0B0ml_SNbPO4j6-wSdjofP_n8Xj36PgeXJMXzNNY8RDQEOVRoRqaGQh9JhXBTjhnKRBt4uqSfHk-xRHd0GlZRRFd7E_fCu35QaamDtRVFV3CbjW3GAnrxmzFz6TF5isdmzZ-BRHnjmiQN_oRB3pxPmLsYoNIE9fIV9N16xwl1HeWRnNdmILckzcFA71seGvUkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ونزوئلایی‌ها تصاویر ترامپ و روبیو را به نشانه اعتراض سوزاندند
🔹
تصاویر سیاستمداران آمریکایی که بیشترین ارتباط را با تجاوز آمریکا به ونزوئلا دارند، توسط معترضان مخالف موضع واشنگتن نسبت به این کشور در خیابان‌های کاراکاس لگدمال و به آتش کشیده شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661421" target="_blank">📅 15:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661420">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/254877efcb.mp4?token=MfBeQGJA8DfdHqSM8ZVgFHTuJW3IpJOcOQlvzH8tohfFfkpJA00fhVTwuuIb6apjXfO7HlKZ1UC_XslJqnGi3Nj82_UBV2ncf1hJzrRK3iQqHt4AN7tJnVzFkalA5y-TIAtYROOCnJ9B225WiwZTXzkNnVZGVavPPqqo9d7AT9D89hcLxpfN2W7IGhMo5jstrqyLtrKHSJhyfs7V1sDxmBaq1ct2ELDC-q2P8SvdJG_XeGJCJQED1NKj98kDeXqaNC0YqOBKrNHtw9FBh70giRJDJTJsOCTvhJhm5D_4TQzRn9kfNx0CwGnw3WXQtsrAPLqgyBhfeeb4n76wYS3IzRZPX9DEIsW6AfdSjv1V59N31xiPIPmaaD_aUC_5FU5VNg8fFkwWZHxvdEV3B6oxLdgBtWNB5f0rK02rY-XzQlBiRUx6FC6sO_zc28hCzKxZUhNL1hBbTVGKirrW1Ve-J4wSX_oJTRLyrmrs5NUEvZ6eBYdzt6csuGMdukhHYjElY2E8vA95mxA50gRJRHkfzwikVWcbFANAA4uJM1H0eQUBKNSb_SaO3puExmPTYLKZhh8H5K-zSCSqCnq54mXHdy9FeMS302Lutk-Ep_tW5iZ3fTbqwAve_3Eq57dw6LFPEf2nmhgj-jV9jRfI_r5dEqvHPDTCdEsa2L-lcp2Mnvs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/254877efcb.mp4?token=MfBeQGJA8DfdHqSM8ZVgFHTuJW3IpJOcOQlvzH8tohfFfkpJA00fhVTwuuIb6apjXfO7HlKZ1UC_XslJqnGi3Nj82_UBV2ncf1hJzrRK3iQqHt4AN7tJnVzFkalA5y-TIAtYROOCnJ9B225WiwZTXzkNnVZGVavPPqqo9d7AT9D89hcLxpfN2W7IGhMo5jstrqyLtrKHSJhyfs7V1sDxmBaq1ct2ELDC-q2P8SvdJG_XeGJCJQED1NKj98kDeXqaNC0YqOBKrNHtw9FBh70giRJDJTJsOCTvhJhm5D_4TQzRn9kfNx0CwGnw3WXQtsrAPLqgyBhfeeb4n76wYS3IzRZPX9DEIsW6AfdSjv1V59N31xiPIPmaaD_aUC_5FU5VNg8fFkwWZHxvdEV3B6oxLdgBtWNB5f0rK02rY-XzQlBiRUx6FC6sO_zc28hCzKxZUhNL1hBbTVGKirrW1Ve-J4wSX_oJTRLyrmrs5NUEvZ6eBYdzt6csuGMdukhHYjElY2E8vA95mxA50gRJRHkfzwikVWcbFANAA4uJM1H0eQUBKNSb_SaO3puExmPTYLKZhh8H5K-zSCSqCnq54mXHdy9FeMS302Lutk-Ep_tW5iZ3fTbqwAve_3Eq57dw6LFPEf2nmhgj-jV9jRfI_r5dEqvHPDTCdEsa2L-lcp2Mnvs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوشه‌ای از تمرینات پرفشار کره‌جنوبی در راه آماده سازی برای جام جهانی آمریکا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661420" target="_blank">📅 15:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661419">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
دادخواست رسمی خانواده شهدای مدرسه میناب علیه آمریکا ثبت شد
🔹
رئیس مرکز وکلا، کارشناسان رسمی و مشاوران خانوادهٔ قوه‌قضاییه از ثبت دادخواست به وکالت از خانواده شهدای مدرسهٔ «شجرهٔ طیبه» میناب علیه دولت آمریکا خبر داد و اعلام کرد این اقدام پس‌از دریافت وکالت از خانوادهٔ شهدا انجام شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661419" target="_blank">📅 15:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661418">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1960e5024c.mp4?token=pQoA7r_Tf69VvnASZtrBk2bbFHTQOlMF4NcHcrzEbviYGaIsoSD3mUdJZ-5nined7cTeXnqrbFUTZO3ASZFk4JqECr4z-_NCkQWDuWSXcgzqSBg1vMEBnt6mnGUG4Bu7-K5zyrVCJAr8MnP4SPdhYPvJCGWFyILBebbJzeFJw68-AtTL_c5tTIVmyMWGS82aWybBRkK3y3AabJhdw6momc34b5qZ6pYI7HIrND51DjrbmbeCwf-HiOwbTBVdImfSGkvBQZiobDXevzuzUsqqCk7W4yEW4urrPQNB6TqCnrqoCKX2u6sWMPrhF_dzM3hMXMZOY30Wv0ToQ-e5GjhSLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1960e5024c.mp4?token=pQoA7r_Tf69VvnASZtrBk2bbFHTQOlMF4NcHcrzEbviYGaIsoSD3mUdJZ-5nined7cTeXnqrbFUTZO3ASZFk4JqECr4z-_NCkQWDuWSXcgzqSBg1vMEBnt6mnGUG4Bu7-K5zyrVCJAr8MnP4SPdhYPvJCGWFyILBebbJzeFJw68-AtTL_c5tTIVmyMWGS82aWybBRkK3y3AabJhdw6momc34b5qZ6pYI7HIrND51DjrbmbeCwf-HiOwbTBVdImfSGkvBQZiobDXevzuzUsqqCk7W4yEW4urrPQNB6TqCnrqoCKX2u6sWMPrhF_dzM3hMXMZOY30Wv0ToQ-e5GjhSLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لاپید: تنگه هرمز قلب معادله جنگ ایران است
🔹
رهبر اپوزیسیون اسرائیل می‌گوید هر تصمیم نظامی علیه ایران، بدون در نظر گرفتن اثرش بر بازار انرژی جهانی و تنگه هرمز، عملاً نادیده گرفتن واقعیت‌های اقتصادی آمریکا و سیاست داخلی آن است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661418" target="_blank">📅 15:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661417">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd6d14fba.mp4?token=Dp1Xk_p6sph2iWcsSWYwkYJ6i4J1x6vpijXEPoGsAOWqCjzjOe_GwfT6VFyKHJKtb5tVlvaeLDYra2RPsWUfOgh5tircD79uzlT7M4HB-Hq9aFWTmctlNKoc1yxW1UXFKBCI5w84l2WB53Nuc_0wdv9irVNW5Wts8G0kA8WY3bgAIASb9JXOJEYseHRCgAlTzfLFNLePnufm77dAxhfc4-wSPZQv70tgjqUeca6HR6tTXxNsnhU_BkGmAzOXok2ynXAxu26WvRWXLsnCnJc4QNsUvo1RtlQDZtoN8rzELqeQQsTdS9OvJ4aaWWqjwi-LwIfWKW6rg0mMW9q6TQWutYPEOUDxc8n-3HK3-P-oasSMRrVNFPhB-tyDEIaUXP4rnBGgqRPtmXR0AqdDxJ391uXNPV3b2OxO2uG8mt1GMmsWVQ6nskPBLU_jRbL4gVAJYHNldYmaEFy_4XiRgkzTbpx-jzvycmCj3FBu2ahGFfg3OB-EVia5_fkSGMR9Z_P0ugXsuJofoX9N9jDuovAn1peHgI4g18M7DUY9_TGKBtPHkgtAUv5hXqyOow_nTWLkXqZ8zrzLYMpuMxtQB9h4PvWIjdH6YtkQ_BtEElFGhHH3GrBPw0LGCHyrxLDLAE_YO2qfL4cCHdIv5_J3nwxzcXBhkn7vOoSj1clIpOgyuj8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd6d14fba.mp4?token=Dp1Xk_p6sph2iWcsSWYwkYJ6i4J1x6vpijXEPoGsAOWqCjzjOe_GwfT6VFyKHJKtb5tVlvaeLDYra2RPsWUfOgh5tircD79uzlT7M4HB-Hq9aFWTmctlNKoc1yxW1UXFKBCI5w84l2WB53Nuc_0wdv9irVNW5Wts8G0kA8WY3bgAIASb9JXOJEYseHRCgAlTzfLFNLePnufm77dAxhfc4-wSPZQv70tgjqUeca6HR6tTXxNsnhU_BkGmAzOXok2ynXAxu26WvRWXLsnCnJc4QNsUvo1RtlQDZtoN8rzELqeQQsTdS9OvJ4aaWWqjwi-LwIfWKW6rg0mMW9q6TQWutYPEOUDxc8n-3HK3-P-oasSMRrVNFPhB-tyDEIaUXP4rnBGgqRPtmXR0AqdDxJ391uXNPV3b2OxO2uG8mt1GMmsWVQ6nskPBLU_jRbL4gVAJYHNldYmaEFy_4XiRgkzTbpx-jzvycmCj3FBu2ahGFfg3OB-EVia5_fkSGMR9Z_P0ugXsuJofoX9N9jDuovAn1peHgI4g18M7DUY9_TGKBtPHkgtAUv5hXqyOow_nTWLkXqZ8zrzLYMpuMxtQB9h4PvWIjdH6YtkQ_BtEElFGhHH3GrBPw0LGCHyrxLDLAE_YO2qfL4cCHdIv5_J3nwxzcXBhkn7vOoSj1clIpOgyuj8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تحریم و اغتشاش دستپخت ما برای نابودی ایران بود
نفتالی بنت:
🔹
در زمان نخست‌وزیریم، با همکاری موساد و سایر گروه‌ها رویکردی ۱۳گانه در قبال ایران اتخاذ کرده بودم.
🔹
این رویکرد شامل فشارهای اقتصادی، سیاسی، امنیتی و غیره بود.
🔹
یکی از کارهایی که کردیم این بود که هزاران ماهواره استارلینک را داخل این کشور قاچاق کردیم تا در اغتشاشات، اتصال اینترنت برقرار بماند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/661417" target="_blank">📅 15:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661416">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f33afe1d58.mp4?token=c3Af2IF6w8syDgKRVTTVAq6SKdcF4fEzWR8A--SUaIix7ycdNun-Bs_2J5CVVAdqLBQP8rYWR0zHOMgP2uoLFme_KSH2ZoCup6RMH_g4cZeitRDUEBa8TNpVBhO2TeUjBKblec8JbRaxNv42LZHNUxmy94qau2lrIlu7GP64v1-XVlMfsQeXyG1Ga4ypXujTwx1Ye8JQoCw732Iw0eus6TtcN9C1Y2dZyFtOV7VbTj8JaAie9H4aBEnxQ9yl89YaTjySJEw-WFCpa2fjyI5-rZytbsw4zr9LoQa8gc4FrPLrI8BdKFxQPoxm0pNJV1bKQlNHiboqdIteR0hU1_rVyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f33afe1d58.mp4?token=c3Af2IF6w8syDgKRVTTVAq6SKdcF4fEzWR8A--SUaIix7ycdNun-Bs_2J5CVVAdqLBQP8rYWR0zHOMgP2uoLFme_KSH2ZoCup6RMH_g4cZeitRDUEBa8TNpVBhO2TeUjBKblec8JbRaxNv42LZHNUxmy94qau2lrIlu7GP64v1-XVlMfsQeXyG1Ga4ypXujTwx1Ye8JQoCw732Iw0eus6TtcN9C1Y2dZyFtOV7VbTj8JaAie9H4aBEnxQ9yl89YaTjySJEw-WFCpa2fjyI5-rZytbsw4zr9LoQa8gc4FrPLrI8BdKFxQPoxm0pNJV1bKQlNHiboqdIteR0hU1_rVyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پروفسور جیانگ تحلیلگر سیاسی: از نظر راهبردی ایران نباید آتش بس را می‌پذیرفت
🔹
اگر ۶ ماه دیگر جنگ ادامه پیدا می‌کرد کار آمریکا و اسرائیل تمام بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661416" target="_blank">📅 15:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661415">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/738e76890c.mp4?token=EDuuwfFyPM3trE05UDr1cuwlfMHCmQhyxYafEDZvG9-mHZFk9rq0yYHSDCyeAp65AMHuaTXb9O-oI_1MBpuNdGVoiOMHLgMs31zvolEq2bSQzXbDZWB4-9ajadRtlXo5DJ2333JgUKWUQTk8xbGCH0wPA3fT98J_I3xPf73H9PNfKL9W05zF8eCSBlDcUcgW3fg8oZveHgYv5qUM5Cg-ZbioCQ-Jt0Plm7BnIVp7OH-uUWcbL8Vt1q1LubJWTNjNmA4dBxbjwps15Cp3MwQO89ybTPF72eUXH1Mk9oT3u3AyXGha3JvoMyHg8ke-spJ45ZUCvLp7JWJX-BXO4aXVgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/738e76890c.mp4?token=EDuuwfFyPM3trE05UDr1cuwlfMHCmQhyxYafEDZvG9-mHZFk9rq0yYHSDCyeAp65AMHuaTXb9O-oI_1MBpuNdGVoiOMHLgMs31zvolEq2bSQzXbDZWB4-9ajadRtlXo5DJ2333JgUKWUQTk8xbGCH0wPA3fT98J_I3xPf73H9PNfKL9W05zF8eCSBlDcUcgW3fg8oZveHgYv5qUM5Cg-ZbioCQ-Jt0Plm7BnIVp7OH-uUWcbL8Vt1q1LubJWTNjNmA4dBxbjwps15Cp3MwQO89ybTPF72eUXH1Mk9oT3u3AyXGha3JvoMyHg8ke-spJ45ZUCvLp7JWJX-BXO4aXVgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لاپید: تنگه هرمز قلب معادله جنگ ایران است
🔹
رهبر اپوزیسیون اسرائیل می‌گوید هر تصمیم نظامی علیه ایران، بدون در نظر گرفتن اثرش بر بازار انرژی جهانی و تنگه هرمز، عملاً نادیده گرفتن واقعیت‌های اقتصادی آمریکا و سیاست داخلی آن است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/661415" target="_blank">📅 15:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661414">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
وزارت امور خارجه سوئیس: ما به فراهم کردن محیطی محرمانه و قابل اعتماد جهت تسهیل گفتگوها در بورگونشتوک پیرامون اجرای یادداشت تفاهم ادامه می‌دهیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/661414" target="_blank">📅 15:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661413">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ee9dcec1c.mp4?token=mRvbiFdfNt5QuO39NzDA_jhluCbXj9rdAo0p1-bkkvQlWy_y7HOF0lQ7XFSIDA2XdEzZo8oH23MYqgkYpMmGHInv14Ol7EvTTTx3DTazc9MRBaGGWG44Op_brZ1KU_etMuAVk0nY8pVzKoKmz-BTozZ-ZuTcjP-OVMMS7l6QfmgrS_KShdAD-J9riNFOvOMArzsceiXu-zup7OCqncZ_U74sOWmPFsmoCUBynueCGSR2_KN_I8A_DgklzM-GdGvkeNPXaP7LE6KYFNcS9vySDBcdU9HhKnrkbkxQiMCmgvJnSeBiyUzqcbLk9-nLM9eIkgJGK153wCnoZc_5frZzWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ee9dcec1c.mp4?token=mRvbiFdfNt5QuO39NzDA_jhluCbXj9rdAo0p1-bkkvQlWy_y7HOF0lQ7XFSIDA2XdEzZo8oH23MYqgkYpMmGHInv14Ol7EvTTTx3DTazc9MRBaGGWG44Op_brZ1KU_etMuAVk0nY8pVzKoKmz-BTozZ-ZuTcjP-OVMMS7l6QfmgrS_KShdAD-J9riNFOvOMArzsceiXu-zup7OCqncZ_U74sOWmPFsmoCUBynueCGSR2_KN_I8A_DgklzM-GdGvkeNPXaP7LE6KYFNcS9vySDBcdU9HhKnrkbkxQiMCmgvJnSeBiyUzqcbLk9-nLM9eIkgJGK153wCnoZc_5frZzWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اندیشمند برجسته آمریکایی؛ این واقعا شگفت‌انگیز است، این یک تسلیم بی‌قیدوشرط بود/ایران به هر آنچه می‌خواست رسید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/661413" target="_blank">📅 14:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661412">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139b8a8525.mp4?token=TaecoO_u4-Q4vEqOOl-zXj7ZJtfKjbLahhUHj6_C-7QsZK1WfQxvSJFYTrPMpUaJv-DwjTDLQBC--K4UnC7YPxOSVHwBBBsVKje_TzeJO3URydee2d7JGW8WTnv3gUXZtxLwi_xxKAUEo_ZP7Jff3n5ngPy_EKZ8Dw1AaUSYkSl3uY2jArCis6_bpzjhr52sA_LYnxGf5dmt43bvOCm4YkB0njIknSvm0IBsTWJl42sV4NUumL5dbh2a3YZb_RF9qabWe_7p4ttlNRmcvOpoAYs-Qiw2Lkc2gU6JjzM9NTaCQGyQQdGtmf3920A6zaYDTDmqaGqg3BA8BjUQdRxU1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139b8a8525.mp4?token=TaecoO_u4-Q4vEqOOl-zXj7ZJtfKjbLahhUHj6_C-7QsZK1WfQxvSJFYTrPMpUaJv-DwjTDLQBC--K4UnC7YPxOSVHwBBBsVKje_TzeJO3URydee2d7JGW8WTnv3gUXZtxLwi_xxKAUEo_ZP7Jff3n5ngPy_EKZ8Dw1AaUSYkSl3uY2jArCis6_bpzjhr52sA_LYnxGf5dmt43bvOCm4YkB0njIknSvm0IBsTWJl42sV4NUumL5dbh2a3YZb_RF9qabWe_7p4ttlNRmcvOpoAYs-Qiw2Lkc2gU6JjzM9NTaCQGyQQdGtmf3920A6zaYDTDmqaGqg3BA8BjUQdRxU1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر معظم انقلاب: رئیس‌جمهور ایالات متحده بود که برای این یادداشت تفاهم التماس می‌کرد
🔹
ترامپ: بدون توافق ذخایر نفت تنها ۴ هفته دوام می‌آورد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/661412" target="_blank">📅 14:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661411">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wtm30eyedmAFUIYyaN8ZT_gKuZUnfplu3mzqnZxQUPG-aNnfEDbswKdklxAh57YWvo_gxEiu7EJo7ewyfyF4Pn6rmzAPT0gOV1yYiKSTdU30f1x1GZigehEhPOZIKkYx240PMuk-mUr8A5kXNiwJtDzpJ-I4HJiAbc0ilvIYqr3nIKbwF-m7zz2HwxjhYmUzWuzkUiSiDdpBgy3OgthAbr75TLk9B3xwUZk6sYp_SXHuwhxVVro8hpNH2XqVvyKp3XckdkehJbQmUg5mNYuUx8lmxzJwA5NpaAYxc07goGdGG_i8uVAnEHUa5j7aPnXD7k19Ycyf-SslMysIgMCB9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: ما در جنگ خود علیه ایران چقدر خوب عمل کردیم، کشوری که از نظر نظامی کاملاً شکست خورد
🔹
دولت‌های اوباما و بایدن در قبال ایران ضعیف عمل کرده‌اند. با روی کار آمدن من، سیاست آمریکا در قبال ایران تغییر کرد.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/661411" target="_blank">📅 14:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661410">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
حزب الله: در مقابل تلاش دشمن برای تصرف اراضی لبنان کوتاه نمی‌آییم
🔹
اتاق عملیات حزب الله لبنان با صدور بیانیه‌ای اعلام کرد که همزمان با پایبندی مقاومت اسلامی به آتش‌بس، در مقابله با هرگونه تلاش دشمن برای تصرف اراضی و گسترش اشغالگری کوتاهی نخواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/661410" target="_blank">📅 14:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661409">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
نیروی دریایی سپاه: اگر شناورها مسیر دریایی جنوب جزیرۀ لارک را رعایت نکنند، مسئولیت هر اتفاقی با خودشان است
🔹
از برخورد احتمالی با مین تا تصادف‌های دریایی و حتی هدف قرار گرفتن.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/661409" target="_blank">📅 14:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661408">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b36f5f37d.mp4?token=TeDqvbkmkdjVfD5g2jgj4EIaWEkk2gF0LG1VqLWXQTJykTaKG6WRTEQKDyNY1tYjvEFsS_y-PjMa_Ql4kbgNOqHtqJkWvotPKWzQIOi6yQ0NvmcUbjCSUNZ_6eYBZKISRviRD42A9yiqi9x8k5SpxQtC5PPdd-C87sPWiV4WqfU0kHo4RwPuGtdEkCFFJL-BD5Yz2cIwLS7m6lc1-R3ea3vYCVz4IB-xU1msEZ-G1f0pdmnNmRm2KKnGnJst-bRuZ8TngdvwXG6sDAVtCYQNBgQJLS8NlS6Z9aeRXEONSlXMN7BCAZ9FojMez3GE66Weev1Y2DHzo4v8O_DJFHFyJiJphBk4P1sxfydcY-qqMqw2EOFn0ep46ZgeU5qwoBB0tzbwfHMCr-idmhfn_tEZL96Vls4Aj-XvlJf2W2I2b_dg5CnDQynMZb89mtx9S1bfXWwWMSMEqv-kscI6nrLE8bd0CGH7044a0Lh6Q40tsfcsfzI3tjIwH1tXZkBFCSOp5rxTnaoEs8hKT3ZqLp7yhKr1w8fRP2Bn6mtmi3bnGWrSVK2XWzhJqr3DO-U52cPPAE-xM9X9EvNWV4Yc8sXSb8JlbmlkzxNaKRMu-T5D6zIYoTv6wd0JHkbYsPKWwek8M9jaqKiKC-hsG9QeQ9BLnLIuoZAIG5pfk3sI4AEfecA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b36f5f37d.mp4?token=TeDqvbkmkdjVfD5g2jgj4EIaWEkk2gF0LG1VqLWXQTJykTaKG6WRTEQKDyNY1tYjvEFsS_y-PjMa_Ql4kbgNOqHtqJkWvotPKWzQIOi6yQ0NvmcUbjCSUNZ_6eYBZKISRviRD42A9yiqi9x8k5SpxQtC5PPdd-C87sPWiV4WqfU0kHo4RwPuGtdEkCFFJL-BD5Yz2cIwLS7m6lc1-R3ea3vYCVz4IB-xU1msEZ-G1f0pdmnNmRm2KKnGnJst-bRuZ8TngdvwXG6sDAVtCYQNBgQJLS8NlS6Z9aeRXEONSlXMN7BCAZ9FojMez3GE66Weev1Y2DHzo4v8O_DJFHFyJiJphBk4P1sxfydcY-qqMqw2EOFn0ep46ZgeU5qwoBB0tzbwfHMCr-idmhfn_tEZL96Vls4Aj-XvlJf2W2I2b_dg5CnDQynMZb89mtx9S1bfXWwWMSMEqv-kscI6nrLE8bd0CGH7044a0Lh6Q40tsfcsfzI3tjIwH1tXZkBFCSOp5rxTnaoEs8hKT3ZqLp7yhKr1w8fRP2Bn6mtmi3bnGWrSVK2XWzhJqr3DO-U52cPPAE-xM9X9EvNWV4Yc8sXSb8JlbmlkzxNaKRMu-T5D6zIYoTv6wd0JHkbYsPKWwek8M9jaqKiKC-hsG9QeQ9BLnLIuoZAIG5pfk3sI4AEfecA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چیزی به نام آتش‌بس در لبنان وجود ندارد!
🔹
خبرنگار: شاهد یکی از شدیدترین حملات به منطقه نبطیه هستیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/661408" target="_blank">📅 14:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661405">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2029917f7.mp4?token=YBvVjryGQSuWxs8OScW5hZvaiV-etnpXqqQNd2a5qct0SbQqwB5JFNr_-_gWXW1l6e0IEj9HApD2e2YRfKEgEOPQWZsKYO-3eqCE9xu-u8SHwHsiplroD2rGKWOdXoRHmQ1R2QFK_wxEZ-pks-ZvvpGjIrwsF1odgKS0SbXfxDVt7jEAp_E3-wiFuF8AzWm4fIwlv7_bsU1wCGmQyVLSQFaNR81lJknJ5DSxUQuf5IEp7wDDh6GcrF8FczOP_KOQMGXqsq1zCaHFkluUzF71oHJ1C9k67ZU53yk6OylhDjYsYdrS9CBFxc8ZP7YQrG6s9nw8hS-F-l34T255EQ2y_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2029917f7.mp4?token=YBvVjryGQSuWxs8OScW5hZvaiV-etnpXqqQNd2a5qct0SbQqwB5JFNr_-_gWXW1l6e0IEj9HApD2e2YRfKEgEOPQWZsKYO-3eqCE9xu-u8SHwHsiplroD2rGKWOdXoRHmQ1R2QFK_wxEZ-pks-ZvvpGjIrwsF1odgKS0SbXfxDVt7jEAp_E3-wiFuF8AzWm4fIwlv7_bsU1wCGmQyVLSQFaNR81lJknJ5DSxUQuf5IEp7wDDh6GcrF8FczOP_KOQMGXqsq1zCaHFkluUzF71oHJ1C9k67ZU53yk6OylhDjYsYdrS9CBFxc8ZP7YQrG6s9nw8hS-F-l34T255EQ2y_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنایت در شهرک قناریت در جنوب لبنان
🔹
منابع لبنانی از حملات شدید و پیوسته به شهرک قناریت در جنوب این کشور خبر دادند که تا این لحظه به شهادت دست‌کم ۷ نفر و مجروح‌شدن ۱۷ تن دیگر منجر شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/661405" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661404">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
ابلاغ دستورالعمل فروش ارز اربعین؛ سهم هر زائر ۲۰۰ هزار دینار
🔹
بانک مرکزی دستورالعمل تأمین و فروش ارز زیارتی اربعین سال ۱۴۰۵ را ابلاغ کرد که بر اساس آن هر متقاضی بالای پنج سال می‌تواند تا سقف ۲۰۰ هزار دینار عراق دریافت کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/661404" target="_blank">📅 14:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661403">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a971dbe16.mp4?token=piBImmlDU4umo-YqcHAQjZYd6vKo-ZB9ucnr9VfZzkhwX-YWN39_LWWtX0B3p9bxDt8vRPD4BGjsjF1lwQw40Cp23lM9e5pkJnQwi1vOZYpNMpJdne2z_84RlbOISZ5KFaoFMGvM37getmMN9rTrGrtvzWxfMipoeSGMvh-GcO7MfI_cbjgkIT25DeNso6aVFzOGEtwkdgIKLIZItyvH5QGnGHQ1ZyTqR5xCnW1insOS5uWM0gaPBZJNiRZXZI2xzQ2Qd-XIKI8MBZibluUsdOJQZ5Llk8rg5AdKQmIf5oVPTorFTB3yiT1AFE0NGxEqEZwqXk3shZadrht7BqXckQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a971dbe16.mp4?token=piBImmlDU4umo-YqcHAQjZYd6vKo-ZB9ucnr9VfZzkhwX-YWN39_LWWtX0B3p9bxDt8vRPD4BGjsjF1lwQw40Cp23lM9e5pkJnQwi1vOZYpNMpJdne2z_84RlbOISZ5KFaoFMGvM37getmMN9rTrGrtvzWxfMipoeSGMvh-GcO7MfI_cbjgkIT25DeNso6aVFzOGEtwkdgIKLIZItyvH5QGnGHQ1ZyTqR5xCnW1insOS5uWM0gaPBZJNiRZXZI2xzQ2Qd-XIKI8MBZibluUsdOJQZ5Llk8rg5AdKQmIf5oVPTorFTB3yiT1AFE0NGxEqEZwqXk3shZadrht7BqXckQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت پرده لباس‌های یک‌شکل مدیرعامل انویدیا؛ سادگی به سبک میلیاردرها: هر روز مشکی می‌پوشم تا یک تصمیم کمتر بگیرم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/661403" target="_blank">📅 14:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661401">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U942zxZWRxOHHOtWHvJ7jGcd-cBWddVwNWA2Ktq3jtwVREvHHQhdXNGKSWey5_88tz8HaDn4phfiqGKDPyaA3-4D6fWtSZMbjVzabreUqE_vs9a4X5f8TlxcBn7nxpmyNFgNnjvyn66oQdO8IdZA-nbUzNJbjp9YfOboiRZh3aZ093tK01n8_T9LqUMfvqZk56G0oFeJ6F_-0QLbm-CHNluoBN82W2h2MAPwhQQZtoJmsfkHtXTEm3PbO3r144jzwheTvtXNLLCaF7LwzlVt-QZdEx3bUP-oImLrd9-v00uP9ZLAieGWyzYCsuDfMlxqfaMV4qtPJAgox49FP_5fdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۰ درصد بازار پوشاک در اختیار کالای قاچاق
🔸
سالانه حدود ۲.۵ تا ۳ میلیارد دلار از بازار پوشاک کشور به کالای قاچاق اختصاص دارد.
🔸
برآوردها نشان می‌دهد سهم قاچاق در این بازار تا حدود ۳۰٪ کل مصرف است.
@amarfact</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/661401" target="_blank">📅 14:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661400">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d08bb1e1.mp4?token=I9XgkGQh-qXqV43q-b9apft94wX7ntGUBGtewtyKw5FNy49Vd2-6B00ArMpv3-OXfdpsGIlCypZfrGGPvYjr6JKqn4OEss1i-gPW-7yIN-edkJ5ImXU1jgyRJeOaR0QQruUJ30kQG31VjgYgDSRWma_YxvYEpMtcu7xxA0exH2OWtOlMhqXp5zBCDDCFEtV-kqjpMqkTLUIuh6pYLgx78KE_Ygkv2bLCHJKzVXYBnAPLqbpp9nZq2d4a5kkHtmoezxoCXTRqk5NkVNqdYszL5CdVt4SlZ_sUQ5oR5LUeiitvWlihe63pZza3v13Y9LA8OokLe0084Hg2GEySewWxIpgmL_R9JQpiTcO2qScN_GkIzj_V0fnhYInMB0LU-CX3jls95RpwPxY4P50jHsmE1b1dOEgrkT0DmSf8jkWXrc9TraxVDheFI3wAZ1jQYKktCZxzYFiKRJ5zdHUaLF1AJyXferv8rBOM9VwFIJity0BM0WPDTx8AGsKiMT085SAauA_2ztrOvXiYJwtJlbJO8NgOk4zniAJJEvuA5VqJGaZHqiNfn84aq8NaMx_8B8sZ_BOFklTdVq9uNlRTSywkCk1B8xA9Z311WmXNFh-NXI0M5ErCu0uGqjjv8KWiXMY2287gpud1FL2aMiThTeZMIaWyia1b5o4y8pKsU4_5pWI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d08bb1e1.mp4?token=I9XgkGQh-qXqV43q-b9apft94wX7ntGUBGtewtyKw5FNy49Vd2-6B00ArMpv3-OXfdpsGIlCypZfrGGPvYjr6JKqn4OEss1i-gPW-7yIN-edkJ5ImXU1jgyRJeOaR0QQruUJ30kQG31VjgYgDSRWma_YxvYEpMtcu7xxA0exH2OWtOlMhqXp5zBCDDCFEtV-kqjpMqkTLUIuh6pYLgx78KE_Ygkv2bLCHJKzVXYBnAPLqbpp9nZq2d4a5kkHtmoezxoCXTRqk5NkVNqdYszL5CdVt4SlZ_sUQ5oR5LUeiitvWlihe63pZza3v13Y9LA8OokLe0084Hg2GEySewWxIpgmL_R9JQpiTcO2qScN_GkIzj_V0fnhYInMB0LU-CX3jls95RpwPxY4P50jHsmE1b1dOEgrkT0DmSf8jkWXrc9TraxVDheFI3wAZ1jQYKktCZxzYFiKRJ5zdHUaLF1AJyXferv8rBOM9VwFIJity0BM0WPDTx8AGsKiMT085SAauA_2ztrOvXiYJwtJlbJO8NgOk4zniAJJEvuA5VqJGaZHqiNfn84aq8NaMx_8B8sZ_BOFklTdVq9uNlRTSywkCk1B8xA9Z311WmXNFh-NXI0M5ErCu0uGqjjv8KWiXMY2287gpud1FL2aMiThTeZMIaWyia1b5o4y8pKsU4_5pWI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیزر قسمت نوزدهم از فصل چهارم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ خانم اعظم فکریان که در قالی‌بافی مشغول به کار بودند و یک روز به دلیل بی احترامی فرزندشان دلشکسته شده و اقدام به خودکشی می‌کنند و روح از بدن جدا و به عالم برزخ سفر کرده و تشنگی مفرط و عذاب‌آوری را درک می‌کنند را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: اعظم فکریان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/661400" target="_blank">📅 14:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661398">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71bb3ee9dd.mp4?token=mLt8Xazrjd_iS8sRu5vevcEkMXKZECHp1BqoAbkXtfOgS5M0Kj82VN_3nalzciJMPo6Lz3NmTCUJvgGlsVscNvEwkVI8G0MzVZB8rTJx_OqFU6I8sCB0SpXn4OKpZ2PxPNNYeVlwOKRtx7GDwzPX5caVTHiLx0018oWBXHvD7039vqilfWbFTpSPXL9N4ASRHZqqMm0ej0T3rXD6VN2YPZ4kCx5yQxlQcE3et2BgpVbwSlhkSb9fcxMT6XSjwCH8yd4ib0HEvNZktAj9DAIZyRo5eUlSYjV4D8l1gk2S3pyW4ZMWQuMXXT2jLGwWoITv1_AIRGfo4T3zRKzYCd1umg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71bb3ee9dd.mp4?token=mLt8Xazrjd_iS8sRu5vevcEkMXKZECHp1BqoAbkXtfOgS5M0Kj82VN_3nalzciJMPo6Lz3NmTCUJvgGlsVscNvEwkVI8G0MzVZB8rTJx_OqFU6I8sCB0SpXn4OKpZ2PxPNNYeVlwOKRtx7GDwzPX5caVTHiLx0018oWBXHvD7039vqilfWbFTpSPXL9N4ASRHZqqMm0ej0T3rXD6VN2YPZ4kCx5yQxlQcE3et2BgpVbwSlhkSb9fcxMT6XSjwCH8yd4ib0HEvNZktAj9DAIZyRo5eUlSYjV4D8l1gk2S3pyW4ZMWQuMXXT2jLGwWoITv1_AIRGfo4T3zRKzYCd1umg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تماشای بازی ترکیه در آمفی‌تئاتر باستانی کاش
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/661398" target="_blank">📅 14:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661397">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJIThEQ4EU0-ZD5LXZfbWrq8vRu5eGnoWb2VQCW6cdEoBqzduPDsR47XrVhLDDvzfga1n4codpeX9d8-UbFBHmnYyHinu9E0lTBW4sHKH7zeAmS-CpLov_Uryr1hLFmJCZgJaPO5h7E-qyaYCMLzUeMOxMUmRoxspuAP49kaA2Iu9dgqBAvuNkboV_mVgcVJfsCXrDetYu6Wn8DfpW9zOVGKcH94f8T1MUDdpRtNi8Ai_mjIr_pGcHJDoSSpYiXdIl5pH5WtBm07VvCcPjSXBFQqiwL_UMzZ3Krcxrg-LPcfAyogWJmWGQs_MfLNLD4AEHd5271R6iKH5_P_rDxY3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«قرار بازداشت» رو زیاد شنیدیم، ولی دقیقاً یعنی چی؟ #واژه_کاوی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/661397" target="_blank">📅 14:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661396">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291962135c.mp4?token=Jzm22rC9fHZkzFF6oh3_3-J3cqQMflnxsBuwqMtWsBqDBVvQ1T2ax8WdHJ3OAhYvU6md2OcaW4V4sZfWBRwlZI0X4XxGbjXXLUZgwy1aEAP9RiEXTj2mmP4wBRlpt8KWCXoPdxaNbSBnj112_C-9AdYbTbnI-XN62RHztPT-MemG7BH7vuyEDaxWyFhKM2RYiNLBX9pSS0qEFdI2hw64eSZb0n39WN-Ss9Jpr9Ah4JjpIfNm3PCAPESj8ztoi4YBPjVgAQ5Pc59LAyi-H4cHmL2X2sirOug4DBLVvexVFyxIulF_4lfsmKAM02DHQa9SEIBkNjF_zY32NIdYkuQcfR40BUve2o3YiAxXptcvvibqbAVhwwiRSA3Rog_XiYXgySxz5PTbTbqRRW-WT6S5p8Wz3wtmRWUq7BFH4m_pCAN86BexL5-tVetT6XjHs2rPxyuVGjS9hMFgxUiLRE58HMu8qCo4O-pLJI6ZI_luf-CfP0JplRBeehqLr3PmunUScDvfEufqslK4q5e84WNVBGC9yL5D5glGeElsibYQskVtlQffBYE6ey1nv65c0O-k2RVnR4BK8zRbH8vPj6rD83i5He1eiDwJMtM6Pw-bw8dK5C86RJXwvnRIrURppyAc2A_48Hz_-71zizLlDoN88cxmizF37J_J_0OJW_fP8ac" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291962135c.mp4?token=Jzm22rC9fHZkzFF6oh3_3-J3cqQMflnxsBuwqMtWsBqDBVvQ1T2ax8WdHJ3OAhYvU6md2OcaW4V4sZfWBRwlZI0X4XxGbjXXLUZgwy1aEAP9RiEXTj2mmP4wBRlpt8KWCXoPdxaNbSBnj112_C-9AdYbTbnI-XN62RHztPT-MemG7BH7vuyEDaxWyFhKM2RYiNLBX9pSS0qEFdI2hw64eSZb0n39WN-Ss9Jpr9Ah4JjpIfNm3PCAPESj8ztoi4YBPjVgAQ5Pc59LAyi-H4cHmL2X2sirOug4DBLVvexVFyxIulF_4lfsmKAM02DHQa9SEIBkNjF_zY32NIdYkuQcfR40BUve2o3YiAxXptcvvibqbAVhwwiRSA3Rog_XiYXgySxz5PTbTbqRRW-WT6S5p8Wz3wtmRWUq7BFH4m_pCAN86BexL5-tVetT6XjHs2rPxyuVGjS9hMFgxUiLRE58HMu8qCo4O-pLJI6ZI_luf-CfP0JplRBeehqLr3PmunUScDvfEufqslK4q5e84WNVBGC9yL5D5glGeElsibYQskVtlQffBYE6ey1nv65c0O-k2RVnR4BK8zRbH8vPj6rD83i5He1eiDwJMtM6Pw-bw8dK5C86RJXwvnRIrURppyAc2A_48Hz_-71zizLlDoN88cxmizF37J_J_0OJW_fP8ac" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نبویان جزئیات جدید درباره نامه‌های رهبری ارائه کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/661396" target="_blank">📅 13:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661395">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
وزیر کشور پاکستان وارد مشهد شد
🔹
پیش از ظهر شنبه هواپیمای حامل وزیر کشور پاکستان که به منظور دیدار با مقامات جمهوری اسلامی به کشورمان سفر کرده است، در مشهد به زمین نشست.  #اخبار_مشهد در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/661395" target="_blank">📅 13:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661394">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab51b559a8.mp4?token=bzpy39wPkhuKOKAKoO5S1TYV__tf2MVYY-uizJNec-YpluGNtTW-gDwbYES0yI2qFvWvAgHrGaGLSzynW-hvoFHOWtDrj86sGXRE2MWPRlhoJbazs3RUWY8man8oJTgbXKOWvz4PYQQ1XfqBXpJxtQp0l2leNg0sJ7-ZXPZktYW1A6vl9wwONVMMthQq4JdMHOKq3dzY2QkAIU0l0ChX4AmgJXA7wThWD8ANsg7c8q_0b6xFZSOi_qzk3gFfX7_dWAscV0LOz95LA9-5rYospxpXMjDPuLzDGv4fw_Bt-xFtspi4696J3mic03EKjutTWLYXSqgdHF69BSj5Opm1LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab51b559a8.mp4?token=bzpy39wPkhuKOKAKoO5S1TYV__tf2MVYY-uizJNec-YpluGNtTW-gDwbYES0yI2qFvWvAgHrGaGLSzynW-hvoFHOWtDrj86sGXRE2MWPRlhoJbazs3RUWY8man8oJTgbXKOWvz4PYQQ1XfqBXpJxtQp0l2leNg0sJ7-ZXPZktYW1A6vl9wwONVMMthQq4JdMHOKq3dzY2QkAIU0l0ChX4AmgJXA7wThWD8ANsg7c8q_0b6xFZSOi_qzk3gFfX7_dWAscV0LOz95LA9-5rYospxpXMjDPuLzDGv4fw_Bt-xFtspi4696J3mic03EKjutTWLYXSqgdHF69BSj5Opm1LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزارت اطلاعات از شناسایی و دستگیری سه تن از لیدرهای میدانی و ۱۴ نفر از مزدوران شبکه خرابکاری خیابانی دشمن آمریکایی-صهیونیستی در استان ایلام
خبر داد
#اخبار_ایلام
در فضای مجازی
👇
@akhbarilam</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/661394" target="_blank">📅 13:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661392">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e1db5f80.mp4?token=PtsIvCv3ooSIHfx2Zwln1RbnCl8sHkHSEVTh4YHhNAg76QoLqqOZ0AW9q691neSjm7L68pL2zX2NH8Ak8panolVrIPSmqPkTz3eSdQUWh0ouS-ebp__uX32E5JkQab7ejrmDIDeaXIMUXTJE4dGrjnXNxq-dxrZmyMg0c-wbbN9UHnT_RBvzouuEEloXyVcJauFM71PGl936PKg-vmU_xjSnawcQofNLe7xZY_O3WcEIQry0ZaQjm0V0jW5lNtcxiXUkI1-sNy3jT7Jw9WYOh5_bG4JTwkI-vDzYktLGoMG6BEAdgCdWoV6CFTl2zdK2lpzIspML4T3MgUuiqC1fYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e1db5f80.mp4?token=PtsIvCv3ooSIHfx2Zwln1RbnCl8sHkHSEVTh4YHhNAg76QoLqqOZ0AW9q691neSjm7L68pL2zX2NH8Ak8panolVrIPSmqPkTz3eSdQUWh0ouS-ebp__uX32E5JkQab7ejrmDIDeaXIMUXTJE4dGrjnXNxq-dxrZmyMg0c-wbbN9UHnT_RBvzouuEEloXyVcJauFM71PGl936PKg-vmU_xjSnawcQofNLe7xZY_O3WcEIQry0ZaQjm0V0jW5lNtcxiXUkI1-sNy3jT7Jw9WYOh5_bG4JTwkI-vDzYktLGoMG6BEAdgCdWoV6CFTl2zdK2lpzIspML4T3MgUuiqC1fYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل در ووهان چین
🔹
به دنبال جاری شدن سیل در ووهان چین، حمل و نقل در شهر مختل شده و خودروها در خیابان‌های آبگرفته، شناور شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/661392" target="_blank">📅 13:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661391">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مشمولان اعزامی تیرماه ۱۴۰۵ برای دریافت برگ محل مراجعه و معرفی‌نامه به دفاتر پلیس+۱۰ مراجعه کنند.
🔹
هلاکت یک نظامی دیگر رژیم صهیونیستی در جنوب لبنان
🔹
یک شهید و ۸ زخمی در حمله هوایی اسرائیل به منطقه صیدا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/661391" target="_blank">📅 13:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661390">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpcMQ28Lo5ETFKaZKzNCAkzQ-Fx1DezVcpm5h0bI8r1K8W8J3FBVHy1rX72Cb6VQDhZet7jOBbGg1pAgBmQS8BbQCZb46VHV009wodKjEqRLuaLILXoTNCmRgWRJnOh9bHnM9K2hkUDqRwtHHYZ3bq7_79QiCKbc1c2emSvOriilALAZD_HPJKqymNxxuX9MMsXTQrqjHwHDwc6NUSTus0vde-NWDcAtUNo8IkYs2hgzMsJxn5u2AT7hcY74hfhR84VhfvHbpaEIMdpI2Udlqr8Gj5XUl4CaXh8qCWX2A9KMsEW0_LjCKlwiTWLxk1fZQ5lXwjmhcoAu4TZKlyF6qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت کاربر آمریکایی درباره مادورو و نتانیاهو: یکی این تناقض رو برام توضیح بده
کاربر آمریکایی:
🔹
ما مادورو را براساس یک حکمِ بازداشت دستگیر کردیم، اما نتانیاهو که در ۱۲۴ کشور تحت تعقیبه، شش بار به کاخ سفید دعوت شده؟ یکی این تناقض رو برام توضیح بده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/661390" target="_blank">📅 13:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661389">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
حمایت خواننده لس‌آنجلسی از ایران و تیم ملی
🔹
گورگن زرگریان خواننده لس آنجلسی که در حمایت از تیم ملی فوتبال تا تیخوانا آمده، برای ایران و تیم ملی کشورمان آرزوی موفقیت کرد.
🔹
گفتنی است، او خواننده‌ای است که پیش از این از مواضع قیصر انتقاد می‌کرد!
خبرهای لحظه به لحظه جام جهانی را اینجل کلیک کنید
👇
https://www.khabarfoori.com/worldcup</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/661389" target="_blank">📅 13:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661388">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENMIvHaRTIjf6YjcjLkRhHIbBczE5TvlBh3dOXcmvV1ukkBYRDs4pgrkQ2pmggux1SzlXr9dChHdqtrNIBxIfEEZE7bf34xZFfsaJ6sFi8g04bB_XZHIu22SvwOdTKaLJrcREVOBFmdXVECevs13luT4BsacX4kPVQDuOGjNaLaQex7qke8qmLc-YJBrmCNdMLjjjGaehN0NPgQVJF2eZrq6liBAq5w0egSQPLkBcPs4_eMI3DvtIuzMS05JofEGCt2v-o_ptkdaYTmz1NxIFEGY94793IBOS0C8AdnTwHy4bdGdWZRRyQoq1GJJjFRO1CcO50_ppYBEafIzqO254Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قاب هولناک جنایت میناب، برندۀ جایزۀ بهترین عکس سال جهان شد
🔹
مرتضی آخوندی، عکاس ایرانی، به خاطر تصویر هوایی تحسین‌شده‌اش از مراسم تشییع جنازه باشکوه ۱۶۸ دانش‌آموز شهید در میناب، مقام اول جوایز معتبر گلدن شات ۲۰۲۶ را از آن خود کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/661388" target="_blank">📅 13:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661387">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
واشنگتن پست به نقل از یک مقام پاکستانی: اسلام آباد با تهران و واشنگتن در تماس است و با جدیت برای رفع موانع تلاش می کند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/661387" target="_blank">📅 13:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661384">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
واشنگتن پست به نقل از یک مقام پاکستانی: اسلام آباد با تهران و واشنگتن در تماس است و با جدیت برای رفع موانع تلاش می کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/661384" target="_blank">📅 13:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661383">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ادعای ارتش اسرائیل در حال بمباران جنوب لبنان
:
اگر حزب الله از نقض توافقات و انجام عملیات خصمانه دست بردارد، ثبات برای هر دو طرف ممکن خواهد شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/661383" target="_blank">📅 13:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661382">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from️لوازم خانگی بهشت بانه️(admin)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qh7HqxNQGOn5QY7xDQlervCdcAGLMx4lsBBwVF-3GZMzrkw26Pw1iihKUjI5vlNHQ6pT8UNyd0yAS6Or-J3qx0Qh6GqlzEIPeUC29HjK2Yj8zzi-IQUw74kiWGM117slF8aNrB_x4qiT6DBnG07GnPsHK-RV8YSLFct8TcwiFMn5diw7gRn6d-wskwfaYGuAN1-9flJoLtDREdcOvhTbYELKNdAgI0pouc23B2W-N9RZZynhckV6giQ0yJaqNXIWG44Oz4zdymD70JmwyYqF8tP6C2sj1lEJSX2CQs8OFMWvtQLJcOTMHm_4pCJMSX-fgpkfVMH81Vx3CfN6I2efVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش اجناس با نرخ دلار150.000
💵
✅
فروشگاه  بهشت بانه سلیمانیه عراق
✅
لوازم خانگی عمده برندهای معتبر
✅
الجی کره
✅
بوش المان
✅
سامسونگ
✅
تحویل درب منزل باگارانتی شرکتی
✅
تسویه درب منزل
✅
لینک ورود به کانال تلگرامی فروشگاه
👇
📱
https://t.me/beheshtbaneh2021
📱
https://t.me/beheshtbaneh2021
✅
مشاوره کامل خرید تلفنی خانم ها فلاحی
👇
😮
😬
09188806440
🥳
😬
09182643758
✅
مشاوره حرفه ای در پی وی
👇
👇
✅
@banehonline2025
✅
@ORGINAL3758</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/661382" target="_blank">📅 13:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661381">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiliHeGd1JZMG4e95eBA_Kz3Ont4Fahq-BfmKHYKSqGV7IVoNBmc4fgXBbXXRRsaWVes9QCTWb5F3s9D1rRfR2CpSk8UBmDLYLY31r571f0m8MZT_v96vcywg8tQaX86DbIEWLyLAdllczgu89F9mbPGjhBbUI8wrV_bZ2HbZOWUXqQ2QcjMkEPPl8EV8KhYWkQcIrZa16qtB3GVb88qDRmwqrCbKkEUbSbmCvdE8CXZZJPBzhpFZu787UjOF0m9jWkOtwGOeGQ_fn-mmxO-aXdv_cDzglfezspdCnoGf1fvthD_7bVvZHYFpE64ObLtjEApIwa4Zj4pKa4KePGXvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عکس روز ناسا
🔹
ناسا در بخش «عکس روز نجومی» خود تصویری خیره‌کننده از پدیده اختفای سیاره زهره توسط ماه منتشر کرده است؛ رویدادی آسمانی که در آن زهره برای مدتی پشت قرص ماه پنهان شد و سپس از لبه روشن آن دوباره ظاهر شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/661381" target="_blank">📅 12:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661380">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79e74710a9.mp4?token=Z-vkxLpwC8FPDUG4k6xQt9h-lCeASNp-WXkwU0OKrU1iZmIP5XakZEgtfmd6XhaYJgzEDTxsFXq6vsf8ZApuR6XMj8FmVN7_f0ltgQ0t36p9Cn9UCgouXf2Ud93bUYq_dihVDAfLgBi1Q14WO5tY6oH1mLZZn9oEI1PZatNRu5ptcI5kOT5hXyABm4Sigi2Ko3VBH2cdK-MAxOGCTud9V8LK69bYr1wqsYmNabo2uaRF-jqFz5g9CN6YmyHP0-95PDbAuicQ3p-sOBg8vc2MlRYTLLSyafnceWFT3VNK7wudK6lAvJJbkUIn_XL9YpdQyXAiX_eUYqs2RrREPgfwOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79e74710a9.mp4?token=Z-vkxLpwC8FPDUG4k6xQt9h-lCeASNp-WXkwU0OKrU1iZmIP5XakZEgtfmd6XhaYJgzEDTxsFXq6vsf8ZApuR6XMj8FmVN7_f0ltgQ0t36p9Cn9UCgouXf2Ud93bUYq_dihVDAfLgBi1Q14WO5tY6oH1mLZZn9oEI1PZatNRu5ptcI5kOT5hXyABm4Sigi2Ko3VBH2cdK-MAxOGCTud9V8LK69bYr1wqsYmNabo2uaRF-jqFz5g9CN6YmyHP0-95PDbAuicQ3p-sOBg8vc2MlRYTLLSyafnceWFT3VNK7wudK6lAvJJbkUIn_XL9YpdQyXAiX_eUYqs2RrREPgfwOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکات موزون بازیکنان و سرمربی در رختکن مکزیک بعد صعود به مرحله حذفی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/661380" target="_blank">📅 12:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661378">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1b20f033d.mp4?token=UAJQayd0VJWHOcdkzF12kyJQQjh1fKYlxh7CrnWIlVMMEhQodafAAIui4WSQ5yySr5Ko3YScVnoRD9lCOiP5kOPzhIVqb6H_pYdXsRppW6XYFixFiJ022NWuLNq-h_0enw46sNep-lOuSTDZXN4wLXtJTlhHNAjBsRZhEUuc-jtVOfhwrsknwXeq727biNgmvE05ESrO7FDJ7CLuSguhR_gGcCjsxtL2wB9WU5ouFIYmNNfo1c4efL9od34lqaXgFhYPVI1Cwe8qqnxJ7BEGKNlicnuPqCDgBMOtB3ysvSas9r07xhpJn6rXbGbvu6un4yfR5FjsG5vESBPyEkZGVHYYgtgsefKiYIuuTibBrZaAG3KlhwGJcnF-obu73QNpizUvN0_groPEJ8AiONXgCfnOPkWHq-3Kpjvr46EyYgMbeDxRq3hatKeS0-VzBzyjR3eq3aFaetr9VWp4gSZSHVRCMYHNVcZLoMLJWkDFyWfDRJB7kO0Y203U1vRsca0sFVZ8anqvgsPKYFQ-15W5ssAOs4QW0s3mbc5YH4jF9xWeyQprxlA2rAt8E4dqUWo4FQJeDd_1wS65UlqE9SVAEt0wNvKdmusafhuPFNHGLNKt5qAJ2E2uMzkT9AYpWyG_hUYkhVmA5eCbg3T3lFhcJNoys82ufh22vvzydX-qNPE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1b20f033d.mp4?token=UAJQayd0VJWHOcdkzF12kyJQQjh1fKYlxh7CrnWIlVMMEhQodafAAIui4WSQ5yySr5Ko3YScVnoRD9lCOiP5kOPzhIVqb6H_pYdXsRppW6XYFixFiJ022NWuLNq-h_0enw46sNep-lOuSTDZXN4wLXtJTlhHNAjBsRZhEUuc-jtVOfhwrsknwXeq727biNgmvE05ESrO7FDJ7CLuSguhR_gGcCjsxtL2wB9WU5ouFIYmNNfo1c4efL9od34lqaXgFhYPVI1Cwe8qqnxJ7BEGKNlicnuPqCDgBMOtB3ysvSas9r07xhpJn6rXbGbvu6un4yfR5FjsG5vESBPyEkZGVHYYgtgsefKiYIuuTibBrZaAG3KlhwGJcnF-obu73QNpizUvN0_groPEJ8AiONXgCfnOPkWHq-3Kpjvr46EyYgMbeDxRq3hatKeS0-VzBzyjR3eq3aFaetr9VWp4gSZSHVRCMYHNVcZLoMLJWkDFyWfDRJB7kO0Y203U1vRsca0sFVZ8anqvgsPKYFQ-15W5ssAOs4QW0s3mbc5YH4jF9xWeyQprxlA2rAt8E4dqUWo4FQJeDd_1wS65UlqE9SVAEt0wNvKdmusafhuPFNHGLNKt5qAJ2E2uMzkT9AYpWyG_hUYkhVmA5eCbg3T3lFhcJNoys82ufh22vvzydX-qNPE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از جنگ روسیه و اوکراین چه‌خبر؟
خلاصه آخرین تحولات جنگ بین روسیه و اوکراین
🔹
آخرین تحولات جنگ بین روسیه و اوکراین از صبح ۱۹ ژوئن
برای دیدن کامل ویدیو کلیک کنید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/661378" target="_blank">📅 12:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661376">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
تغییر ناگهانی در هیئت مدیره خلیج فارس/محمود امین نژاد جایگزین ایلکا شد
یک رسانه اقتصادی مدعی شد:
🔹
در اقدامی عجیب ، شنیده ها حکایت از آن دارد، محمود امین نژاد جایگزین ایلکا شد.
🔹
دلیل این جابجایی های ناگهانی هنوز مشخص نیست و باید منتظر نتیجه بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/661376" target="_blank">📅 12:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661375">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5860865c54.mp4?token=AnlmznI0Yr9dqz1gOwoTF-_aeZ5UpwITJ2sJI3U9kTSkz_ipTuKyk2W19lgdFCNAJuBBKPEuUQVTfGr-ssHmG3FqjXgt5cWKBPhO54TTNMJGs04Pn6Wmr2X4mFfUIu_3M858l4HqRzbr_hSObfGzMv0jBf6G3b9rfZMQqPp3ngLhLSmHLtJ7BKJFjCDxOZ-b1uh2z_4TEj6pQ3PtfqVK0ReDI9Em3uMHnj0BL2sIIZoIPqRtOiYwUHWVFd9D6WnpMqfirYTohBRMH2ulOOs85lQbZUDOIifHVEux4E-SIAXZKQacG4mdxIms6aqUFzdstYq1VEQWfSf4rK7bx9n0rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5860865c54.mp4?token=AnlmznI0Yr9dqz1gOwoTF-_aeZ5UpwITJ2sJI3U9kTSkz_ipTuKyk2W19lgdFCNAJuBBKPEuUQVTfGr-ssHmG3FqjXgt5cWKBPhO54TTNMJGs04Pn6Wmr2X4mFfUIu_3M858l4HqRzbr_hSObfGzMv0jBf6G3b9rfZMQqPp3ngLhLSmHLtJ7BKJFjCDxOZ-b1uh2z_4TEj6pQ3PtfqVK0ReDI9Em3uMHnj0BL2sIIZoIPqRtOiYwUHWVFd9D6WnpMqfirYTohBRMH2ulOOs85lQbZUDOIifHVEux4E-SIAXZKQacG4mdxIms6aqUFzdstYq1VEQWfSf4rK7bx9n0rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از صعود آمریکا و مکزیک تا حذف ترکیه و خط و نشون کورتوآ برای تیم ملی
▪️
قسمت ششم برنامه جام تایم
#جام_۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/661375" target="_blank">📅 12:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661363">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KeNdfeU8wVwEe867-qNPerWwW80G-kiyjRsFKFfOvq4rbbVqRD7FfFtQcAZgUx2emNJc1QUhY1fgjV1BprTWd6Ln5XTQpjYqNXOCecsDP5IuinJDFWEQMqoCJ-q-Ab_WEoCovYpahM2HhZcQy8phYViKiEwOUMSYOyPQ_4sTd_t-m999bX_3yGY0Fu61iSavWerXPeI5G2PZdgKEryd8FwcY_Xfh0SaT_m4J7FqlDW3onT68iHMSKynzkWAFIwCPPT3nSXIi53KKpjKSH9gBYbic11a_TF1oOMu3M2_2vz0tedm5wqrb2wYAS_HNeKRf8SXlKfVGLDKT8C1p0zVGpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ArvyBZUf3W_NHB9kdCNkSIPBW4-TgVXgv3tW6zXMhuHPwXhfYGV1OoNMR_yHVqo7SFl2RIbyASMt1OqjwWzuVN3xkMiEP3XPSqy5MkhJcvl0i5loFYULdQeEw81K6fn5sz_m0tMVOlC6F3nAwe4Lt2qIpMyLtIlViNhdrPGxtTcQDfSONlA88B3ouOfkXBqs0Y3NoLjDsVv07Qz6ftI7n8ZDMCx2NFX_wI9vvyMgxFGU5bewBbdcxUYxidBPfzw3NQj-itakQN8NPGn3YCnsir9qC5F5y58F1EGUjBzHUpsrK0Vx4frIh5okZSLdAkqVt-pMy2MOupADUQNfqlTHcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NscBnIPA-rkHsOXYnntHo0I9SI0r-gWwkqQ0EiT2tZjTYGq1Lrc4O6zkU9hszbsmDjtOSHnclbxQiOuPZmubP-OfsNvcGJ4EnBeD69jPaMj7vWK5FUzls4WrDAGIsku2Gy-0rGF43hZIL9V8k3IIpF5BcY4RoaQENw2ue9bPxCUtPFy86lmW6byxj5SqiX5a0MzatxKhCyhRH5A-b4o7k5uzRKw7LTih5Jho5pt1IZLTALhxTVD_YZXn5tRrcEJcbXzxytrXMgJHu2nWZ5V6o7MHDhJ40wp48gaeAG_0BT2KzgrdVH48SGddWeHREDkp1q5h1x2JE1M9_bAy6jSUCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fFRVEvm7EUUN9kOhC_mEzClrGRFxphxFt7elALj59ttMX9JeZxq0oMMe5FtUBLZUmieILzlaWNpLDrQQIwpxj6UFac3FKl5J0GHsarbDFcrnOeZJNmS-ooqW70jXvSZwTONy6PdZHEGiPg28E5csV9Ch_nVYVx22YZWKGjHvHOkHaC8uYUoPsiyX7PTHRRqlA8_LDAK1nqPOrzhDoLzwCv7VbY4Z_Zkl38__ElRqGXRG66LFhvQQKfjm70AQKzAzmyLg9CoXZ9-TmDiHRTt_8wddvlAtufI6phBaC_oF5hgVfLXdE4eLsvrosZHhz9O-sWd55al_j2cp2ZiXwD5DTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PyOXE3L7DaxBiTgQfG8PUnyMwyhXqeCKdocGnD06DY_Z_DPSLwXhmjQhOSnskb_8jQPng035-N5Gj_KAahJKkZ5oJzt32E75oI60HKmBq4SNodzHuWg88DTipg0rqC7JX9bhb-xW4zm7qDZNeBX8DOqUfJyuveu3qg2eNUVbWAJ6T4FcUqmFkcceVrjzxuT_MgmDwvSZVZs-DlXMfllWVdqZcygP-wR3Bf9BRz5NZIqfDqHkx5pQAn0FNJKQdN6pBYUjkT4XmtAlxLzVR85TwslNBD3vpjtK0cv90LKPBF8icNbdREFqfv-p0Xb5vjMXicdxe1SIUxyNOcdkETn_nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WFMkCIjwWX5ifIMdIExuC7VNtamwIYiUjg6GsYwYKfuEwaJvxYz6oeDkTBbPF7GYeUi8CCqmRqmeX53RqL9B1FAKiD7O-qwW_v0_oZcjdlQKHQY6RgEPgAZCfyvitrAxJrMwEheiZpnprwRaCWVDtu1xsFdAfEF0ERk0BjuwshyU6KEo811sbneLd19kIn92Ksy21YxntnJz7q4NtSJftE7P6QTjLsEXgA4Mp-_5zQFDqfOPubKEUOuuwG6jj3pKBvYNUJ5H_LK5gLBDZDiRNaoi3jBPlKpUeK__xvex0HEqMi_CqcdYA3owGPNgaLgOsv4sbQDbUKsmnL9J3eJp0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MXO73YKX8S2R3PfqJeQWauJ9Y8gLYFfL0ND7e5R3wyreLvLLZ7OBmNLmUyokqCnPzFDljB6qk8xv41_W6f6O-0roLIyVauxmAUDGqa9xZPpRmLqjzyFsL5CiUPFPsbre-phiX_w8Qll8lAJnSYWPKTTtvTIHxGibFRT3bRRBETdHvL1rEyUu8xMgOQ2IaaTyf4m8MWoUeoRR01ItBbHSRz2cXTNwSZ-XuZtIQdwhRNwiAJsQxxemiQNWRGpHVNJI-s79yslMgovjB-WOhPiWipsC6mVoZGFrh2TKBh-SNIhvCP2aSKEAweuXWXCFUwec-EbrZB2Ah46SzUUZz55g9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LFGCXsYbBnntiOn0CZUMpd2CTxSXtW9H9Z2gu6WsBBKGWxq94z58m512Nue4KKK1YGGOMOpRkq9sCSdAT2zxMYfyEY1M2QHv6DxnkNLOBg1rZr3V6BWlJE_86ym9h19xyDCoBhqS7EduS2FkSydxRkFjHcM15tko_vOttyhIkWnMCNNs36Hmu6fYu3PceRJTfem0S77xfB1XDcTkuCffcCsfrfCi8039TAHaAnNu9bTZTlWhh_VlPF7wLSeAWCPvBeAmlaBk-IkD-b2y1yCXszcAxCfbxq9FcXHoMXE22qOZWRPkj-OxnjoMKfd4YVvdS0hvcktIl4OWlvlbDMDfQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jT1gBoEwk1Z4w_4H-ewUZh_T-x1IzOcS1divYK_bxQ0tF72nEZzsR4ll02_bq4KaEP4I_oBAAzc8LP8ySKQHNY4wsGB4cMwk4R5r71DIRuRzdR_aRnc3H0o3xTkSfTNPooSgxRmdHJESOxV68Xhi_I3tfM-abOTgbiCiDM33fn9Ua7YmyF5bDV_iyMb7NKKa1QFhTN9il2IQhQq1Y32XVDsDQHTI8NA2mNc5BKsIxY_tY7Za4FG_lpWWRuB_BoymxC4l2M5uCGcoKuVCbMrvYYuzKn4lYRY7qUeULWmYZopaNB5TPzQgbz78k-SYjkWy9-tbM0gIVijneAOMniQKdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vcc_6tcIxt-lC871ZTOJS_wtfVybtNGq3m_SH6W-KtSIakKE-sOY8YZUXQ2rFEnFVxzA_crMv5M_ML8BBSxoCBbyRiTCQWYGbUQ0Th5Ax1QxZX3x0g0bLgWC2VmBffDUs8PjIbEZlajaIliDy9TT1Z0ri8oEvkUEQIySg0_u25o0sNfGa1mz9EZum_mejleKmWYR0H9skZYJZanVB_sixvxqfL4zt00AEKzgBDkEIQzS0VyqYs6-A4AkrcjDIbmBhKeus-2iZ69lS1bdtRdeZsoToRefJeaBLgWsvpkhunw3N9czDxg2V8GuXcyFGuKZ6JCyIiSJV1yNYbqsVvG3rQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شیرخوارگان حسینی
🔹
بخشی از تصاویر ارسالی مخاطبان خبرفوری در پویش بزرگ شیرخوارگان حسینی.
🔸
الوفوری را دنبال کنید
👇
#ایران_حسینی
@Alo_fori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/661363" target="_blank">📅 12:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661362">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPhSJO9hO1--58k2WrEfxhlq9XiiJrZvn0wL2hS70ca6_5e7xOLCun3yWVdUqjcwT26wMJ8yAP3Dy_lbMivs6rl6V6fFX0xqBJkiai2lmewqK89KMousZH5iA5-PYEvbzsunxAV8tw-N6el88o6e6PE74cAkK14xt3AuRLKv0H-bG6p-pBcHAsXs5VWnOjxo7DkB5edfcHiwHPS_SVEZVb19OwDOX0UTJmh41UBbvgsmmsGUs6KqbMAuDVJorz33AkHy1qm-_KByEhrtBQgkRUUbahXITKtp-do6QLRNBnBUJgDKNm8M3K3h2dtEMitGpiChnXEViVXff1YgyaaCuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
گرفتگی عضلات داور آلمانی، بازی آمریکا و استرالیا را ۲ دقیقه متوقف کرد
🔹
داور ۴۵ ساله آلمانی، فلیکس تسوایر، در دقیقه ۹۳ نیمه دوم، هنگام اعلام خطا ناگهان به دلیل گرفتگی شدید عضلات پا بر روی زمین افتاد. این صحنه که در آستانه سوت پایان بازی رخ داد، باعث توقف حدود دو دقیقه‌ای مسابقه شد.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/661362" target="_blank">📅 12:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661360">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AM-q4NZpTyi4KUaRtCY_qta0jRLqb3wzvRu0qtyF_hrU35erVp4xpJjg9Nq5kL4DCXZDnj4IswE97AOY5jX_vsaVIxRThXMw5qZTGPHOKpjtaHHF8_7ylcJjBNtc4TqarwuwspX1TyVuRsd4bJxSE6hXzd3e71YifrerPOJQCg9JpVowDFOVrGpMO_9LgkAUJTxgqOxWUnP9sUGq1p1nkew0kSP-2lxdun3HmDbf_tHRm5JAwJFnCgjoYsmnJkhHeLpuLpA9YwkRj-RWHjsN8ly4-6Hv3J1KWBTBiRaW0xe6jCAtvLgi1W0aFV_QByGIHJM3y6W_SCTj8hB1a5nzMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویر کنایه‌آمیز حزب‌الله از آتش‌سوزی یک تانک مرکاوا
🔹
حزب‌الله با انتشار تصویر آتش‌سوزی یک تانک مرکاوا در بلندی علی الطاهر به شعار لشکر ۴۰۱ زرهی ارتش اسرائیل اشاره کرد: «نیروی زرهی پیروز است»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/661360" target="_blank">📅 12:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661359">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f66a56e223.mp4?token=NdBU1TiKdt028jJZVJHmE4-JMRMYjzSulDKAytlkAbP4KMsaupXpWgqVmXLopVFEfOkVjC8FZjYxM5DejLGzgRkqSL13xRiAWA7eveAXfKl9yzPjCpZO0dquP7lqDplzomQYns6_rs0G8MnAVRpwz3ljGbrw7oamvGd0XOKicgS5gbxFdbVYSlAiFmnjwpyIqqR31SDk2gT0hvo2PmDSmhie4gTklWS9TIaqUxPq5eKDSGlyNdvWekVWCwQUkUvJVpgFoYjz3TC51WzEwz_sC8G7pUy-K-mWFHPTC1BqVYvY61cy9hQuzsq9LlW7q1f3VkUxq9c_m5azdsRO_uSkNamjJc-cyRsZJpL2MgErNlOsoEvepVZANALGT0MskU-jp-w9fbDuv2hsTYynHSQ1_0T6r_3n-b9gRB2gJwvqllg9hN8cX-92JHOyDciUOEr6kXHbnKGawGpx3dUEFmIV6KuXGX_Xh4YhIn211pT4PZ-PluxsK1ZXqDP0g1eDQ3pVipRCTAwLsBPL-avDh7cFP9RWLqX9EPevzDXbmsfcrsKcqjZEeHV_DIVSxN3n3nKlnnRU7gkucaA9t6zdbto8-MrnoYMR7t_6PbqEJF48XMDKVYd2Qshlu61bfKlf_G4jiG-1kONWNdGttdRUC3XGRHx4Z3M_tnWfqNGRbwahzYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f66a56e223.mp4?token=NdBU1TiKdt028jJZVJHmE4-JMRMYjzSulDKAytlkAbP4KMsaupXpWgqVmXLopVFEfOkVjC8FZjYxM5DejLGzgRkqSL13xRiAWA7eveAXfKl9yzPjCpZO0dquP7lqDplzomQYns6_rs0G8MnAVRpwz3ljGbrw7oamvGd0XOKicgS5gbxFdbVYSlAiFmnjwpyIqqR31SDk2gT0hvo2PmDSmhie4gTklWS9TIaqUxPq5eKDSGlyNdvWekVWCwQUkUvJVpgFoYjz3TC51WzEwz_sC8G7pUy-K-mWFHPTC1BqVYvY61cy9hQuzsq9LlW7q1f3VkUxq9c_m5azdsRO_uSkNamjJc-cyRsZJpL2MgErNlOsoEvepVZANALGT0MskU-jp-w9fbDuv2hsTYynHSQ1_0T6r_3n-b9gRB2gJwvqllg9hN8cX-92JHOyDciUOEr6kXHbnKGawGpx3dUEFmIV6KuXGX_Xh4YhIn211pT4PZ-PluxsK1ZXqDP0g1eDQ3pVipRCTAwLsBPL-avDh7cFP9RWLqX9EPevzDXbmsfcrsKcqjZEeHV_DIVSxN3n3nKlnnRU7gkucaA9t6zdbto8-MrnoYMR7t_6PbqEJF48XMDKVYd2Qshlu61bfKlf_G4jiG-1kONWNdGttdRUC3XGRHx4Z3M_tnWfqNGRbwahzYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صهیونیست‌ها می‌خواستند پسرم را با پرچم ایران بکشند!
🔹
پزشکی که برای حمایت از تیم ملی از لس آنجلس امریکا اومده تیخوانا مکزیک آمده، در گفتگو با خبرفوری می‌گوید: سخت‌ترین زمان عمرم آن چند ساعتی بود که در جنگ دوازده روزه منتظر پاسخ دادن ایران بودم!
خبرهای جام‌جهانی را اینجا هر لحظه دنبال کنید
👇
https://www.khabarfoori.com/worldcup</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/661359" target="_blank">📅 12:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661358">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSkZ3xf4fwVnWSjYrEn0tf2NGB_ecbCrXBnWtjsESZln-r7nIL3jcz5tTZgqBReNIRkst01NlPBx-EK8eBDlTwdGi9HNwojNn9mgdQebfIs9U_89CBWgAlWBLH5FKtTB0hX4xJ5hfc0NlSsvViLbUFVkFDbNrNM8tgF--HAu6ZyC-ta6T0b8_t-uBKbtbkfIEM6udSZMNyBdzfVK1P6GtQLk0e5dh3BS-4oqW_WdzrU18cg0Nl6N7tVe3lF2_HxbGM7oEnk-JK5SFl3fgTsa3RP21B9orBqsXGkH3laLBm12P5Vw37XoY2ebhJT8vZg1aTJZOsUgAm4Uh3xbX1giRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۸ نکتۀ مهم پیام رهبر معظم انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/661358" target="_blank">📅 12:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661357">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4df5454c51.mp4?token=sQ6g2qwtIBmbAPXGAmcC4dJbgE_pR_2YQHODfrk6pqWxU6d18rWhwzSTz2X6Gd-n7IysxLbPsSdZ81RwfHBSUP3mTGGcbQjoW9yskUBaLTmzpdDaBvMsNvKwHRFcqg3RjMpGjWJHvMfWuAub021f3ByTw50dBp4OBhDXzLTjkT4Z6qL_9cTo-RyFdzxx-2CDCKIC7Cckb-YxaD7NgRr-m_lxdqkqoWXwcG_tIE6nSFx1nAHr04iX_O2B1Rp-eWc1GLcVvNr7_RXXBFm0CkNNMy_ZFOV5Cf7zbtnMl1OLscYzApmPfzgnKy7tjX8oYewXNK10-U7N199xsbp7h5OvdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4df5454c51.mp4?token=sQ6g2qwtIBmbAPXGAmcC4dJbgE_pR_2YQHODfrk6pqWxU6d18rWhwzSTz2X6Gd-n7IysxLbPsSdZ81RwfHBSUP3mTGGcbQjoW9yskUBaLTmzpdDaBvMsNvKwHRFcqg3RjMpGjWJHvMfWuAub021f3ByTw50dBp4OBhDXzLTjkT4Z6qL_9cTo-RyFdzxx-2CDCKIC7Cckb-YxaD7NgRr-m_lxdqkqoWXwcG_tIE6nSFx1nAHr04iX_O2B1Rp-eWc1GLcVvNr7_RXXBFm0CkNNMy_ZFOV5Cf7zbtnMl1OLscYzApmPfzgnKy7tjX8oYewXNK10-U7N199xsbp7h5OvdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ با استفاده از تروریسم کلامی به دنبال چیست؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/661357" target="_blank">📅 12:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661355">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9b0e42be7.mp4?token=unkEsiUSQsBJfeQsAOeaCr50vGirSFMbB8o6CuPOH-U6KqYk50_hOa8O6lpUK5VlkThGBTgLffFe7JNs99IysFHjWlVwwZ1PWOsivhBz0gEWnD-IFkd_XwY30sNARdJSh5NjqP5hfjjoGDdycotDjj1uZZ6DGcIGM3GTmDxDz8SHvkMA728gnu3coUvPeWJbxaov9UDcPDq0qHxi8o9NkSAM54IistgWj1p3wtcDOZhIXwW7bad-OPGSAxCdAISnBGb3Su1KaJ5pzDH1vYioFgFZVMWmc7-DoXY6iClB4uGnFltpHL4uO0SswWVb5HF4i4DOOzebcCwIqeLZJy5Nkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9b0e42be7.mp4?token=unkEsiUSQsBJfeQsAOeaCr50vGirSFMbB8o6CuPOH-U6KqYk50_hOa8O6lpUK5VlkThGBTgLffFe7JNs99IysFHjWlVwwZ1PWOsivhBz0gEWnD-IFkd_XwY30sNARdJSh5NjqP5hfjjoGDdycotDjj1uZZ6DGcIGM3GTmDxDz8SHvkMA728gnu3coUvPeWJbxaov9UDcPDq0qHxi8o9NkSAM54IistgWj1p3wtcDOZhIXwW7bad-OPGSAxCdAISnBGb3Su1KaJ5pzDH1vYioFgFZVMWmc7-DoXY6iClB4uGnFltpHL4uO0SswWVb5HF4i4DOOzebcCwIqeLZJy5Nkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات هم اکنون اسرائیل به جنوب لبنان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/661355" target="_blank">📅 12:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661353">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
آموزش و پرورش: ثبت‌نام دانش‌آموزان هفتمی در مدارس نمونه‌دولتی براساس محدوده جغرافیایی انجام شود
🔹
اخذ شهریه ممنوع است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/661353" target="_blank">📅 12:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661352">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
وزیر کشور پاکستان عازم تهران شد
🔹
سناتور سیدمحسن رضا نقوی وزیر کشور پاکستان برای دیدار با مسئولان بلندپایه ایرانی لحظاتی قبل عازم‌ تهران شده است.
🔹
وزیر کشور پاکستان پیشبرد مذاکرات بین ایران و آمریکا را در تهران پیگیری خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/661352" target="_blank">📅 11:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661351">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf3a7754df.mp4?token=kvabYfPRcHiKWHmdK7RXp-wQiJanOGlzGIehD5jMr_NRWvmobB5wugS377qFiugWcaXxJ0IgmSLb-33vwQBztmZHgCUwaZPxicMqq2u_D8gTQFXAhNrmCLKXx3Q3gy1n2BoaoviU2TzHHyTEzFrL8K_9bz_fF5oow_93zZ0L3Lt7_vSWQgy0bLgfSLaPUOELoAFTWC8fGOuF4_IgVE9Cj5WTFkA5gioFlmfnZHXcXAg48RCGS80g2sutAmkwz-32Ld5Mtv5xJp32-G_65T5XjJ1FZuuA6JDMjLLloFTq6HXC07A9nF6AC0-Yc3tItExyUZC1fT45qw6qxi2tyeFGx4RkrwlEUx1-01uwTTgD7VURZ2UCj7OR0lmZfJxC8eHIaB8NzF_szVYtyBx0lS0-h4H0soLSkBQk9Cmr2qIDGZF2gkPJfiG44ImsKzONORQwWUGmAdZJvtoyPF0Hb182IiN8ABqopevKbYzPVGiwnQFBvcU6D1-d5u4hJoND1gOuMNoFvpLCiCGBb42OgiQvAd89UluiQ_jemNGR5FsgQNbfXZ_zSVAqfH3mEzgqrwoKxzZh26UChfGPWEE7E-pDo0xWLdqkG1_bxuufwXvwopv-lAZgWYiX_s2neaNPOgbl8EKh-xANxfrHatyzDc0X6c3pk3UpHVMIUSivxQ1iPJ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf3a7754df.mp4?token=kvabYfPRcHiKWHmdK7RXp-wQiJanOGlzGIehD5jMr_NRWvmobB5wugS377qFiugWcaXxJ0IgmSLb-33vwQBztmZHgCUwaZPxicMqq2u_D8gTQFXAhNrmCLKXx3Q3gy1n2BoaoviU2TzHHyTEzFrL8K_9bz_fF5oow_93zZ0L3Lt7_vSWQgy0bLgfSLaPUOELoAFTWC8fGOuF4_IgVE9Cj5WTFkA5gioFlmfnZHXcXAg48RCGS80g2sutAmkwz-32Ld5Mtv5xJp32-G_65T5XjJ1FZuuA6JDMjLLloFTq6HXC07A9nF6AC0-Yc3tItExyUZC1fT45qw6qxi2tyeFGx4RkrwlEUx1-01uwTTgD7VURZ2UCj7OR0lmZfJxC8eHIaB8NzF_szVYtyBx0lS0-h4H0soLSkBQk9Cmr2qIDGZF2gkPJfiG44ImsKzONORQwWUGmAdZJvtoyPF0Hb182IiN8ABqopevKbYzPVGiwnQFBvcU6D1-d5u4hJoND1gOuMNoFvpLCiCGBb42OgiQvAd89UluiQ_jemNGR5FsgQNbfXZ_zSVAqfH3mEzgqrwoKxzZh26UChfGPWEE7E-pDo0xWLdqkG1_bxuufwXvwopv-lAZgWYiX_s2neaNPOgbl8EKh-xANxfrHatyzDc0X6c3pk3UpHVMIUSivxQ1iPJ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خلاصه بازی هائیتی و برزیل
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/661351" target="_blank">📅 11:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661350">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e94943171.mp4?token=T6f4Kg5-3zvrZstwatSInIbrVn7QFGWJQvZD3YKsyn2sbwvg15xty5xZXmol6oPsC8hSrpMil58MtSYcd8eeSz7hFwDOgZDg3wKWrxNzMe1DF4zJ5EGcsX4yZ8ADUMUCu8FKxufRz2UJIxMROSoL7X1z_wXvJ9bMkuKBoy1LenZ1w683zIeJThkrVWPbz5PWvC9YKO-vMeppEzXgMkDXUB-gAcDMN8jIHuT0dO-LbwtMhKm6gcweB4qPOx1PttBksnNHmV_pXnzc4jRA-fyn2jC0jybmXk1g5dazfwGcFd67DXW-gZ7x83_XUuXzoZVU1_gX3Vvdv-lOUPMqfDuUkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e94943171.mp4?token=T6f4Kg5-3zvrZstwatSInIbrVn7QFGWJQvZD3YKsyn2sbwvg15xty5xZXmol6oPsC8hSrpMil58MtSYcd8eeSz7hFwDOgZDg3wKWrxNzMe1DF4zJ5EGcsX4yZ8ADUMUCu8FKxufRz2UJIxMROSoL7X1z_wXvJ9bMkuKBoy1LenZ1w683zIeJThkrVWPbz5PWvC9YKO-vMeppEzXgMkDXUB-gAcDMN8jIHuT0dO-LbwtMhKm6gcweB4qPOx1PttBksnNHmV_pXnzc4jRA-fyn2jC0jybmXk1g5dazfwGcFd67DXW-gZ7x83_XUuXzoZVU1_gX3Vvdv-lOUPMqfDuUkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زباله‌ها در هلند چطور زیر زمین جمع‌آوری می‌شوند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/661350" target="_blank">📅 11:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661348">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
یک جفت لاستیک موتورسیکلت ۴ میلیون تومان / نگهداری سی جی ۱۲۵ هم سخت شد!
🔹
قیمت لاستیک موتورسیکلت به حدود ۲ میلیون تومان برای هر حلقه رسیده و برای یک جفت حدود ۴ میلیون تومان هزینه دارد.
🔹
این در حالی است که ۱۰ سال پیش قیمت هر لاستیک حدود ۴۰ تا ۷۰ هزار تومان بوده و حالا نسبت به درآمدها هم فشار زیادی ایجاد کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/661348" target="_blank">📅 11:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661347">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NcJfF7-c5Clwlzvtx0XPPb7eLv5IqccrPn9fry_OxK2waBq-Q3D5ixbS8ny0DkRJPqGwvS8U9Vk754mzKPCe262sw5oEqawzjbBDdgMUN5EG_EHhMM3EAIINSt2f3Z2-EzD95uICtfHU93TBFuuT_2raH3FOqimBNcjWZ2I5IW1nP6ZmkY3k76XqzAZe7riWrqpIfAN4_2YtqwICkXeIsgtvofQ1oSBf5hmVzZVr59lKlW4sfTgkfZn32eZ23P1zr0rHepRVhs2scytwaumKd2Xga0UyCgg7zRWD0RsMRuH1ApIAxpbhfu4vYl3prbsl8hF4ehSgCBEaeXCSZD4f8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/661347" target="_blank">📅 11:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661345">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrNB-Y-nvcnTuv2p_SYN_iWCN-34ClaQ6QMFKl4lJMa-zUEXKywfnyFiNN2vKXPuHI0K7YMPuqiS37idedDMAreW2J3hbNsN8QK8o9Hx0HvA43MY6fz-NEbbtNz0lsLxz8-rRJFBhRDBoxIO8lVM3mw4XTDENF2u0bU9V2bpP9m72MDY7PHXh9-DS-VCfES4XDRcfALVZlCiFBWlSxCwD31XtZM44OZNVEEVEOjBbrGO6tUZvKUNj9VdToiNbFrqqNdFRxMVYT4i0vkM3gnVRMtbtiZ4FND4oSQ9tWEP4YQgw2ZE0yXMlpRAiHySjrLZj8CE0YBmGud2M_m0kdgoow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک تنظیم مخفی که می‌تونه گوشی‌ات رو نجات بده، قبل از اینکه دزد گوشیت رو خاموش کنه، این قابلیت رو فعال کن! #نبض_تکنولوژی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/661345" target="_blank">📅 11:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661340">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f6aecc6ee.mp4?token=PGilxfiGkYD-18xfb3s6ICCzd6RUdLAeUexOXdElNAzGKLgTkmUQYt3tohThRrPrLGmxNDqu7pAhEmTY3aiiT5lu53W21d1kh7gPZe7kJcifwniufC2y37Gvcf6izuUFy79NRj_e3gkWqxakaQR3TBe1AW4oXGsJslOHPScZmozBjBznwxv5ELzHuaACuVPsxT7n0gji7FI9VSfsN0G9EdxvtVw9r8UwTdxN4tGUf5LYjqfj6DaUcDZF6aUVHn0Q_yTfHqPiXRb9EOMsafDhOQjlfG03pzNjRSORQFCt1BHicwZ42yjDSdVOe79ZQ6Rp3aiirKUOIgu_Q0yVrfrCow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f6aecc6ee.mp4?token=PGilxfiGkYD-18xfb3s6ICCzd6RUdLAeUexOXdElNAzGKLgTkmUQYt3tohThRrPrLGmxNDqu7pAhEmTY3aiiT5lu53W21d1kh7gPZe7kJcifwniufC2y37Gvcf6izuUFy79NRj_e3gkWqxakaQR3TBe1AW4oXGsJslOHPScZmozBjBznwxv5ELzHuaACuVPsxT7n0gji7FI9VSfsN0G9EdxvtVw9r8UwTdxN4tGUf5LYjqfj6DaUcDZF6aUVHn0Q_yTfHqPiXRb9EOMsafDhOQjlfG03pzNjRSORQFCt1BHicwZ42yjDSdVOe79ZQ6Rp3aiirKUOIgu_Q0yVrfrCow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۴ شهید در حمله اسرائیل به شهرک باریس در جنوب لبنان
🔹
منابع خبری لبنان گزارش دادند که در حمله هوایی رژیم صهیونیستی به شهرک باریس در جنوب لبنان ۴ نفر به شهادت رسیدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/661340" target="_blank">📅 11:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661339">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
سخنگوی وزارت کشور: همه شرکت کنندگان در مراسم تشییع و تدفین رهبر شهید در شهرهای تهران، مشهد و قم تحت پوشش بیمه رایگان قرار می‌گیرند
علی زینی‌وند:
🔹
همچنین همه جاماندگان از مراسم اربعین که در مسیر حرم مطهر حضرت عبدالعظیم حسنی علیه السلام خواهند بود شامل بیمه رایگان خواهند بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/661339" target="_blank">📅 11:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661338">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtdwUCUlScYDj9jmX7ZjtX8mMulZL6NQR_Hm82ZYMM1td-qrC01guz68XMBwOGpayutpVif29_AEBUDK-hvQ86VTSpoYrKZj9uMf9gIx85oEiRiGpok_zhfI5oE0m06V5Bta_NYqB8_MBVBOe2_INnmTAzKhJiBgmCjYP--LiQduA_6xzCUiVvOmRsV11lGdtGRe3HmxcYacQXe1asXBfmoEzaMJP3Q6Zk8CXTJNGCdQ3Xr7DQyz_yEAb0gxCoHVsrfBSsc9LqTX-mU46KNeqnxjsFrvsVk39sbIrLvvGxlMWHoxLDbBx7p0mgGkoy3FiHo93BSlR2uvZ1XesXCgLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردم سالاری در آینه اعتماد
یادداشت محسن بیگلربیگی در روزنامه اعتماد
در راستای پیام مقام معظم رهبری
آنجا که رهبر انقلاب با وجود داشتن دیدگاه یا نظر متفاوت، به تعهد رئیس‌جمهور در پاسداری از حقوق ملت ایران اعتماد می‌کنند و مسئولیت تصمیم را به دولت واگذار می‌نمایند، یکی از ارزشمندترین صحنه‌های بلوغ سیاسی و حکمرانی در جمهوری اسلامی به نمایش گذاشته می‌شود. این رفتار نشان می‌دهد که مردم‌سالاری دینی نه یک شعار، بلکه سازوکاری عملی برای پیوند میان رأی مردم، مسئولیت مدیران و نظارت و هدایت کلان نظام است.
اعتماد، سرمایه‌ای است که به آسانی به دست نمی‌آید. همان‌گونه که رئیس‌جمهور در برابر ملت مسئول است، این اعتماد نیز مسئولیتی مضاعف بر دوش دولت قرار می‌دهد تا در همه تصمیمات، منافع ملی را بر هر ملاحظه دیگری ترجیح دهد و پاسخگوی نتایج عملکرد خود باشد. در چنین شرایطی، مردم نیز با مشاهده این پیوند میان اعتماد و مسئولیت، احساس می‌کنند رأی آنان در عالی‌ترین سطوح تصمیم‌گیری کشور اثرگذار و محترم شمرده می‌شود.
امروز بیش از هر زمان دیگری کشور نیازمند تقویت همین سرمایه اجتماعی است. سرمایه‌ای که از تعامل سازنده، اعتماد متقابل و مسئولیت‌پذیری شکل می‌گیرد و می‌تواند پشتوانه عبور از دشواری‌ها و چالش‌های پیش رو باشد. اقتدار ایران تنها در توان نظامی یا ظرفیت‌های اقتصادی خلاصه نمی‌شود؛ بخشی مهم از این اقتدار از اعتماد میان مردم و حاکمیت و میان ارکان مختلف نظام سرچشمه می‌گیرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/661338" target="_blank">📅 11:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661337">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
رئیس سازمان سنجش: کنکور سراسری ۱۴۰۵ در ۲۹ و ۳۰ مرداد برگزار می‌شود و زمان آن تغییر نمی‌کند
🔹
نتایج نهایی کنکور احتمالاً در
نیمه اول آبان
یا
نیمه اول آذر
اعلام خواهد شد.
🔹
برای
آسیب‌دیدگان جنگ
نیز سهمیه‌ای در نظر گرفته شده که پس از بررسی نهایی به تصویب خواهد رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/661337" target="_blank">📅 11:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661334">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJzPQmDFQ_emlav0OCuzZ3_p_zQHH2NsOllyj4YNkv-9lkWxuD5gvjDrkuIn42cpVn-m2p_VdILMv_DfxOF65lBHhAiCBMmDGYLvd6rbpiV1H5YLkMHH5RLgNVf91nAzb5AIDeXgFCbNUGdtDTxnH7PKX2yl6zLicQABpUJjniCvRmA_mTs-OpdIUcfSQPbp9FNbB56O9b7dS1NMpl84Mt_mPnWO924BxfFv0cDcIlsQ2reQ6v74hWLxKIxl8YOzWsJcTqyMGfLxIpQ1dLTgAm244BNkU0TxnkUfCFniU5mzLUnyWnjhvRHIliQMM0FBC_VZ5Vtbgfa4pqiBDjAYUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تداوم برتری شبکه سه در تجربه تماشای فوتبال در ایران
🔸
در این نظرسنجی بیش از ۳۶ هزار نفر شرکت کردند که سهم روبیکا ۴۴٪، سهم بله حدود ۳۱٪ و تلگرام ۲۵٪ بوده است.
🔸
بیش از ۷۱٪ شرکت‌کنندگان مسابقات جام جهانی را از طریق شبکه سه صداوسیما پیگیری می‌کنند.
🔸
شبکه سه صداوسیما همچنان نقش غالب در پخش و جذب مخاطب برای رویدادهای بزرگ ورزشی دارد و جایگاه پررنگی را در تجربه جمعی تماشای جام جهانی حفظ کرده است.
@amarfact</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/661334" target="_blank">📅 11:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661332">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
وزیر کشور پاکستان عازم تهران شد
🔹
سناتور سیدمحسن رضا نقوی وزیر کشور پاکستان برای دیدار با مسئولان بلندپایه ایرانی لحظاتی قبل عازم‌ تهران شده است.
🔹
وزیر کشور پاکستان پیشبرد مذاکرات بین ایران و آمریکا را در تهران پیگیری خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/661332" target="_blank">📅 11:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661331">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f067281ed7.mp4?token=q2hq0JKmWMUDX3dmazg5PXqlEERlfV1SACEvtNcmx5eT6qogt-rjGhgf0uSrS3IU28JVPjyKYV4p-Wb1zIvUA6At_focjyGtj9WFlIMNG8-cwBCjtlXxyMu0yDR1dOvR1THUrMSDyRS7dEuagS2ASEiHuiEV9xDVdzevddaNLFfDHXbHeCCskaUhhEUi15-_jiSM_BY5brPyzA4tZye8f-oJiXylxt2g16QYiPPWkJzZ8-wO8PPbvfZuMV__qUtUgCEnJH3jdA7vxvr4d8HlZDsCtqcrr33VsyQil1O_tL08q9PgAmX9QD38gEvsYNinapX9KgjtvAIBRTqNFOXgnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f067281ed7.mp4?token=q2hq0JKmWMUDX3dmazg5PXqlEERlfV1SACEvtNcmx5eT6qogt-rjGhgf0uSrS3IU28JVPjyKYV4p-Wb1zIvUA6At_focjyGtj9WFlIMNG8-cwBCjtlXxyMu0yDR1dOvR1THUrMSDyRS7dEuagS2ASEiHuiEV9xDVdzevddaNLFfDHXbHeCCskaUhhEUi15-_jiSM_BY5brPyzA4tZye8f-oJiXylxt2g16QYiPPWkJzZ8-wO8PPbvfZuMV__qUtUgCEnJH3jdA7vxvr4d8HlZDsCtqcrr33VsyQil1O_tL08q9PgAmX9QD38gEvsYNinapX9KgjtvAIBRTqNFOXgnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت کشور:
برچسب تندرو زدن به منتقدین تفاهم را قبول نداریم/ طبیعی است مذاکره و تفاهم مخالف و موافق داشته باشد/ جنگ و صلح دست رهبری است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/661331" target="_blank">📅 11:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661330">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
وزیر کشور پاکستان عازم تهران شد
🔹
سناتور سیدمحسن رضا نقوی وزیر کشور پاکستان برای دیدار با مسئولان بلندپایه ایرانی لحظاتی قبل عازم‌ تهران شده است.
🔹
وزیر کشور پاکستان پیشبرد مذاکرات بین ایران و آمریکا را در تهران پیگیری خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/661330" target="_blank">📅 11:02 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

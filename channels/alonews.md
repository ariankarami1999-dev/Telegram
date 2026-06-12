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
<img src="https://cdn4.telesco.pe/file/QtJj4gA4RFpnucMxrw2sYGix7DgdUfZPkgyatjoxIMexLBCafxxHFCP6ewiYKyLIjbf0iEbJR-4lU6WmBWP9iM1ZgShfMdc0sT6coH_zZfcQt20ASAKdppOyCzLlO1gxzSn5dnzitNBIHim7BakKHEDX-m3XmrITCLNR9keYAfyIzB6SuQuTGXu924sOgf4YBjXQXMGu9FFmdlPE_8q78x8EBeAHP7LaWxAtrepZ4UZ_byy197x_gZi4tNtPo4q9PQti-0y5RFoozpOfEfluA3-ame-6FPO0CtlbnFV14edw4Kolbt1LNpRvx5ugI_mbiH-ZbwmkJsPWkcUcq87PNw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 982K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 17:28:34</div>
<hr>

<div class="tg-post" id="msg-127414">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSIl2sledBDOCeDTLVxcis9AuDebW09fQLQ4g_ZPzE1GmMshCD6DwroSkwrEcpmrCuEEbLb8nNPaH1fbXzZL14I_ttG8vMVoEogRR55WFnrLZWJetaxteGnLvbx1ZbAdYDX574QQugyHb8lFBg-WLZlKzi5zWS7YP3Iefv3xj1GTbfcxWBDVzTFZl3ATd_ZEogKVwZRYA_TJmw23nfCP-7qIwieb_kxYS5mTxnFon2UurgnNE-MgFfFBhdVYUPsnskTijvSv0NPS78FEsbqrRbJg7WuswZb2gjyFBckiT2l-SYSy_7Uasj0fWYkHW3vTaXCvsbppgHPF0NziBMMk9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
شرایطی که ایران به اخبار جعلی داده است، هیچ ارتباطی با شرایطی که به صورت کتبی توافق شده ندارد. آنچه آنها گفتند، از جمله بیانیه ضعیف و ناامیدکننده‌شان درباره انجام معامله، هیچ ربطی به حقیقت ندارد.
🔴
افراد بسیار بی‌انصاف برای انجام معاملات. با آنها مفهومی به نام مذاکره منصفانه وجود ندارد. شگفت‌انگیز! علاوه بر این، حمله پهپادی کاملاً منعکس‌شده آنها دیشب به کشتی‌های هندی که از تنگه هرمز خارج می‌شدند، کاملاً غیرقابل قبول است.
🔴
بهتر است سریعاً به خودشان بیایند! رئیس‌جمهور دونالد ج. ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/127414" target="_blank">📅 17:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127413">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
یک مقام کاخ سفید به فاکس نیوز گفت: مواد هسته‌ای ایران نابود و منتقل خواهد شد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/127413" target="_blank">📅 17:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127412">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
یک مقام کاخ سفید به فاکس نیوز گفت: مواد هسته‌ای ایران نابود و منتقل خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/127412" target="_blank">📅 17:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127411">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
امیرحسین ثابتی: کسی حق ندارد تنگه هرمز را به امید رفع تحریم یا محاصره باز کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/127411" target="_blank">📅 17:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127410">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMsW1bUje5Y9w8s1IJffGlE41LiwM_soytyEMQmyxqwOfraLeUQ2SwD8OFz7ud0ubjOoJ2bJmRigZQxBmVXcgdh1TvAE56xdKGepIguG5Em61ROIo76uatPNGRbpQPl0BzsFCYGvyS1P6NC6i04jVVpGz7CsYCehs1OFKCSuApCUHBAgC5UWuA6B984awN5n79qh5gSU3BHMdfJukobKCzdDN3NUmDX_1-y_kIanltaV_bRkF-Ae331TX14zD08Gc3dS3gloZTjyQgMuUWkjWv51IsTBO1jsc2_RLM4VqFlvdPIbyOmYx58pYYdbaKHlmWfRjzS30bc8ilLbFgebTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد مرندی:
روز یکشنبه هیچ اتفاقی در ژنو نمی‌افتد. هنوز کارهایی برای انجام دادن وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/127410" target="_blank">📅 16:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127409">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
وزیر قطع ارتباطات:
از سرعت اینترنت راضی نیستم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/127409" target="_blank">📅 16:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127408">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnxu_1LxPOtV6sfVDowZvT7M4wjDiNEmiWg9wZJi1b8X2fSXd-td3iDXRuTZWH68oSS4Q1Q3ZpVtN6c_pERpoE3yRxNt0PTuqAJza2dW3s5iOCsOmayMqSCsbluwmItemIXDEhWNwYkc2ftSng_4r_-Gu3L7OqwJw1OSWDxVokopm-46V8WFNiUEMGOXBtahZLLZsKl8djUuKNFT0BGTh9o_CohjEXAN7XzdGjvVgbBwoq7WfywBkVU4aLrZQD9RtsAocr8VDUmk8Q9DHTNCOJGnHsaQdQcCKHM4Uc88DrZGv4I_mesYJRr5XL1wifOW0oARBDlLKbghIX0W2p73rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژست‌ گروهبان در مراسم‌ فتوشات جام‌جهانی
😎
ساعتشو دیدید یا نه کرد تو چشممون
@AloSport</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/127408" target="_blank">📅 16:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127407">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCfXtIsKfJeKIFhUpx93BDS05Fp28K7kC-hqhPpoImBV1-L7pyVFS7seO9jm6M4HZlYNVv9o5URS-dlDape6JA7YssYPYqjKeUQGpwFO5eOcpz2PvooQ7jxk_jszKlwF42be9a4lL1zPe9KQXbIezokr-ui_sw4M95JQ2foLTMGunujOJ9q4eEibzYTB6QG3v7zP_NNIDNIR565RztB8SOgQXOzj8Ha7HlHjNRy_Q1dR5VHP4BjsktK4llJf5-3omanu9Hl0O0AT8g6_-GmbZE3BiE2kxnYBv3UkWW63U1Wi6kJeabCLMsaTQGnWFOxloVGQYAOERw9mBHa6H8E0IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علم الهدی: هیچ تفاهمی تا به امضای رهبری نرسد، کوچک‌ترین فرد از امت ما ولو کودک ما قبول نخواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/127407" target="_blank">📅 16:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127406">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
فوری / فارس: ادعای امضای توافق در روز یکشنبه در ژنو کذب محض است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/127406" target="_blank">📅 16:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127405">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
فوری / فارس
:
ادعای امضای توافق در روز یکشنبه در ژنو کذب محض است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/127405" target="_blank">📅 16:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127404">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKsdfpd9XrWVT_vRYGgJWi54iE2OfbcvJxOPp0o_XFyg17EPWaHy3rz2u4nRf14eMpysYioAH22PYS-YoRgR71xyn4UNZapyjTHPnYkwXxbEZ3R_qUaekAv7gD_lZN17qpoGMyM8FnUXpCbChLSag4bK0yVcDqDFiVxWV2JnhIeQ2qCE2jDiQFNR3RGQVBWZ4aaLJLD7G9gn5F36dgMQZk8JlMKCMvqapX_GV6CCiGjDZTPULoxc8J3SyGDPDgD7HHJcsGeuK-GA517sFaZxM2j7hwNXUd7JEiNunAg0IrFswm_WR1f8Pba0_WjUTd4YaYbPHZlFqQX5m03MuCfssw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل، یونان، قبرس و ایالات متحده روز جمعه مرکز انرژی شرق مدیترانه را راه‌اندازی کردند که سکویی جدید برای همکاری در زمینه انرژی، فناوری، نوآوری و پژوهش ایجاد می‌کند.
🔴
اسرائیل می‌گوید این ابتکار با هدف تقویت همکاری‌ها در امنیت انرژی، امنیت سایبری، زیرساخت‌های حیاتی و توسعه فناوری از طریق اتصال دولت‌ها، مؤسسات دانشگاهی، پژوهشگران و رهبران بخش خصوصی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/127404" target="_blank">📅 16:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127403">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
اداره ملی اقیانوسی و جوی آمریکا (NOAA): شرایط ال نینو اکنون در بخش گرمسیری اقیانوس آرام شکل گرفته و دمای سطح آب دریا در ماه‌های اخیر به طور قابل توجهی افزایش یافته است.
🔴
بسیاری از پیش‌بینی‌ها نشان می‌دهند که این دوره ممکن است به یک «ابر ال نینو» تبدیل شود و حتی در میان قوی‌ترین نمونه‌های ثبت شده قرار گیرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/127403" target="_blank">📅 16:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127402">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqvoziIZ4YdyrcZwvSQhvFTdvjwCVnb7p0ZUPq2nzbJsQ0T3KbtzZV7muH7YliUoQXk88rI1u9kMpBmqiZy5uQcFP02cwbIpEZ2LgR-YUMIGXLT1B25rTeznEGM4m4SZP8SMDnK4wlHPoQ-nNPH8aKxyThnvFXy1n_5jci74wWbfvTWRJLPyDKoByvt-xrZVpNfth_XTNCAbou1EtXKNGLc-LIwS8uUfMAXd4Agw6cLeCmjURLypNYu99n8dQYFs6GyW3taU9fvFY7jPIVBTNy_a1GkHIVMT2H7ReLtoF-fgGb03K8DmEIDF6pMoH2XCRarWHRObkI750kk63plD5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری یونهاپ کره‌جنوبی: سامانه پیشرفته پدافند موشکی KM-SAM (Cheongung-II) که هم‌اکنون در امارات متحده عربی مستقر است، در جریان حملات ایران بیش از ۶۰ موشک رهگیر شلیک کرده است.
🔴
بر اساس این گزارش، این سامانه موفق شده حدود ۹۶ درصد از اهداف مهاجم را رهگیری و منهدم کند که نشان‌دهنده عملکرد بسیار بالای آن در مقابله با حملات موشکی و پهپادی بوده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/127402" target="_blank">📅 16:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127401">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
خبر فوری رویترز:
توافق توسط جی‌دی ونس و قالیباف امضا می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/127401" target="_blank">📅 16:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127398">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VJFbfVePlGZcqsn-6MK_iDY3R8j8tUqnBQMs_-6zt5rlb2hxf06b-OpGT9UhrPOaEylKERAJ90pF6jT2eShndnwCxXpz7OIUmbN-5RxPGzZXjtUuQPNevp-YzhuKMAPlo5qS7oDGZOVUiH8k1L0kcsfj2Y-OXc5Zc9PTxycHo3BK8DfAwogafUQT_IPmnhJAaGcMxgrj6D1zf5mXK2W-Vr-AdOpAaIzU0PCWiIAhAkjXnlTOcKAG3cyll0b-cjpoPE6xxkAYwxXHhKIeML1MHqmw4ZAVPTSHeXhgVENc6X6PQldYkpRxQl6j3b7DzF5-yHKzlmwor8grsb6J9cn4Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j-kUVyfrNbTb359Fj3zvItRvzrIR0Ttv0Yjjng23jgZaMBt_0h6TTdtRDJFi0ULUBgtQJPWKHVrgGXCVdnAp5-Cm98OFKJ6nk65h6z37xQSr34J7Ng6khjsEiwlmG9EhYKzLJ1jEzWQwVKUMOnosnup2lrIJBHonxrvgSrupPDk6Y1ak22Q6nTfMNYfzSkQSMvHSc-iIhOPVDGj9EwPqaCH1ILjDuQx0PVzKH9afI-gOGPHaCXHbD3znSJmhsrRMV4T5qrMjRkjYhhCu8BBggAafmcAojc9CVGDlHL5IShSAGRXv9L0I6FUtFxWXwRDu_xyZIih310pLVPpS8akXtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OqqSnQQ-0AclDjGqtgaySFJYXSinU4y-6WcoZR_KHz4HmY8uyF8TLuTQjTSGeSkT26viIJN2WZUaVslsd_wpV4BMdE4VYMv89K4Ja4gHqqQkNLbCVBj4j7CTZ9aiIpAqNQGyvHOww9MEOaGBDzUQgBiUw0D6qbRpa1iZpAeQZ5p9bRFeCSfzCWMfIZ3BeCW_BX0xNF1sNK084HhypUYzeN9KgE0s6Pv9MlJHOyq6Pd1tdIqZ0QXPf3w8L8D75JjmoPou8o9IqFUmA73v3bkAWebXQZMWU3lawvC-QhZU3U6QuM7N9uTIopFe-_LG9xWVhneijUaafP9uPRQTOnNJ_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دیروز دونالد ترامپ جونیور در هتل لوکس د آنگلتِر در کپنهاگ، دانمارک، همراه با گروهی از مأموران سرویس مخفی دیده شد.
🔴
دلیل حضور او در دانمارک مشخص نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/127398" target="_blank">📅 16:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127397">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
سی‌ان‌ان با نقل از منبع آگاه : اسرائیل به آمریکا فشار آورده تا تو تفاهم‌نامه، دارایی‌های بلوکه‌شده ایران آزاد نشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/127397" target="_blank">📅 15:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127396">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
رویترز: دولت ترامپ بنا دارد برخی مهاجران ایرانی را به آفریقای مرکزی بفرستد!
🔴
دو وکیل و یک مقام آگاه به خبرگزاری رویترز گفته‌اند دولت دونالد ترامپ قصد دارد شماری از شهروندان ایرانی و دیگر مهاجران را به جمهوری آفریقای مرکزی اخراج کند؛ کشوری که سال‌هاست با بی‌ثباتی، خشونت و فقر گسترده دست و پنجه نرم می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/127396" target="_blank">📅 15:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127395">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
سنتکام : ۱۳۶ کشتی رو منحرف کردیم و ۹ تا رو از کار انداختیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/127395" target="_blank">📅 15:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127394">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTvEx6qll4KAJ28kmh9SHfqCjZJKGJlTR0AzwbWdSv8E2lrtk4Or-OeeDJEbStZ5dZrCzjUUuT39Q9_ncmYCXMf9xzooLdH-uK0eN7X6eDCDOMSkn-pFBQKIBYWETUSwwwKE47-nDXGw1M2AM91oq4WNB5WAFSCAYs0l46b1Cf321hAhNkkeX-8w96hEeo_71Nx0k6cXmz33CpymuzHxbSpmQWEk3sAozybz0EUJkNi8N4vX2zPZzwAty9xWqOgqLZoJJOo9P1AnANhV4nq3RNcPI4473bfwHr2oV5r1WlqmR-wvk-xLR8ouAF0pHdTPHa2FN3i5qFvC7ijXZNNceA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره: در مذاکرات اولیه، ممکن است به همه چیزهایی که می‌خواهید دست پیدا نکنید، اما به تفاهمات مورد توافق خواهید رسید.
🔴
برخی از این تفاهمات ممکن است سپس به مذاکرات اصلی و جامع برای حل و فصل بر اساس برد-برد منتقل شوند - منظورم مذاکرات آمریکا و ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/127394" target="_blank">📅 15:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127393">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
وزارت امور خارجه روسیه به شهروندان روس هشدار داده است که هنگام سفر به تایلند احتیاط کنند و ادعا کرده است که آنها در معرض خطر بازداشت یا دستگیری به درخواست آمریکا قرار دارند.
🔴
مسکو ادعا می‌کند که سازمان‌های آمریکایی در تایلند عملیات‌هایی برای دستگیری روس‌هایی که مورد توجه هستند انجام می‌دهند، گاهی بدون اطلاع دادن به مقامات تایلندی، و ادعا می‌کند که بازداشت‌شدگان تحت تهدید، ارعاب و فشار روانی برای گرفتن اعتراف یا پذیرش گناه قرار می‌گیرند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/127393" target="_blank">📅 15:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127392">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3fa4b0e2c.mp4?token=U2e8UTIolqV6TPqMqjP1qHu8PWrfrf8zXjI2Q4GnYKa1grncapG1o0iCZ2NYDEwjqgGcDyp-ZBw__2_EyK4e1br9M0Tp0Lc7LpWhzfbgw_K6nvcKVzyKv0tBKXx-wACUzZUohmnaJsVqQww3XiypEPKDOwwUOirvY79YPnc1aqTTjh_TkPuNvUiK3XIIjhGoWqw3pqxrP8qQ9H-7qxhec2YSrXSbHRrZDKgJuERHDwMEvgN-jniHP-gReIVFGc3gOwQbLOwqZgtEWgCb85J2bAGgOuDbMOcugO0fAW7NWPgeN4kiDK03NB_lbEI8f1rGSY2ZEObwOoYVCMPrk5ZxUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3fa4b0e2c.mp4?token=U2e8UTIolqV6TPqMqjP1qHu8PWrfrf8zXjI2Q4GnYKa1grncapG1o0iCZ2NYDEwjqgGcDyp-ZBw__2_EyK4e1br9M0Tp0Lc7LpWhzfbgw_K6nvcKVzyKv0tBKXx-wACUzZUohmnaJsVqQww3XiypEPKDOwwUOirvY79YPnc1aqTTjh_TkPuNvUiK3XIIjhGoWqw3pqxrP8qQ9H-7qxhec2YSrXSbHRrZDKgJuERHDwMEvgN-jniHP-gReIVFGc3gOwQbLOwqZgtEWgCb85J2bAGgOuDbMOcugO0fAW7NWPgeN4kiDK03NB_lbEI8f1rGSY2ZEObwOoYVCMPrk5ZxUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
‏سی ان ان تمام ۳۹ باری که ترامپ در این ۹۰ روز به رسانه ها گفته «توافق با ایران نزدیکه» رو کنار هم چیده که بسیار چیز هم عجیبی شده!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/127392" target="_blank">📅 15:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127391">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
قیمت نفت در معامله‌های روز جمعه (۲۲ خرداد) پس از ادعای ترامپ مبنی بر پیشرفت مذاکرات پایان جنگ بین تهران و واشینگتن، بیش از ۴ درصد کاهش یافت و به پایین‌ترین حد خود در حدود ۲ ماه گذشته رسید. این اقدام، نگرانی‌ها از تشدید تنش‌ها پس از حمله‌های تلافی‌جویانه اوایل هفته را کاهش داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/127391" target="_blank">📅 15:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127390">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2c410ab66.mp4?token=T-knushMztkc9UM9FFJUiiUAJ8hK3mdr24FzkXCFgChfP0HpZEGGFzIvoC098iyXR7hLviSdU9iQ_XN-mpltKVF7eBSISgKKVye74JDJpvDDZ42BUlUfO5e3pQbLZXMvN2zRJASuPkB2m6Um9da2Yo-Xv4BmydCTZewr4-Ebyv5722tw2yDqxMyF5wNGwSW0a_LYOqzMJpwFY93xS4Mgn67VXbtNloIQLENOXBJXqIpJOu3X-QRz8RARSgKPL6yGuZc34euR3XqzhKnrOoOmu1IjpMQch0EoZCUfmp0bMG1jzPWlweYMslrEIfcLd7p3NFBOSjZ6yIy1FCwVStIjug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2c410ab66.mp4?token=T-knushMztkc9UM9FFJUiiUAJ8hK3mdr24FzkXCFgChfP0HpZEGGFzIvoC098iyXR7hLviSdU9iQ_XN-mpltKVF7eBSISgKKVye74JDJpvDDZ42BUlUfO5e3pQbLZXMvN2zRJASuPkB2m6Um9da2Yo-Xv4BmydCTZewr4-Ebyv5722tw2yDqxMyF5wNGwSW0a_LYOqzMJpwFY93xS4Mgn67VXbtNloIQLENOXBJXqIpJOu3X-QRz8RARSgKPL6yGuZc34euR3XqzhKnrOoOmu1IjpMQch0EoZCUfmp0bMG1jzPWlweYMslrEIfcLd7p3NFBOSjZ6yIy1FCwVStIjug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روسیه به تقویت شبکه دفاع هوایی خود در مسکو ادامه می‌دهد و سیستم‌ها را بر فراز ساختمان‌های بلند مستقر می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/127390" target="_blank">📅 15:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127389">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
رویترز: ایران برای حفظ لبنان به عنوان اهرم فشار در توافق پرمخاطره آمریکا می‌جنگد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/127389" target="_blank">📅 15:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127388">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">📱
لطفا توییتر الونیوز رو دنبال کنین
🔴
پست های انگلیسی در رابطه با جنایت های حکومت به انگلیسی نوشته شده و افراد مهم منشن و هشتگ های مهم قرار داده شده.
🔴
ریپست کنین. مهمترین کمک این روزها جلوگیری از پروپاگاندا حکومت علیه این قتل عام مردم هستش. خونشون نباید پایمال…</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/127388" target="_blank">📅 15:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127387">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
نتانیاهو: تا زمانی که من نخست وزیر اسرائیل هستم، ایران سلاح هسته ای نخواهد داشت.
🔴
ما و ترامپ در مورد عدم دستیابی ایران به سلاح هسته‌ای اتفاق نظر داریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/127387" target="_blank">📅 15:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127386">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
بر اساس محاسبات ریانووستی با استناد به داده‌های گمرک آمریکا، ایالات متحده در طول دو ماه درگیری در خاورمیانه، 8.28 میلیارد دلار از صادرات نفت و 6.84 میلیارد دلار از صادرات فرآورده‌های نفتی درآمد کسب کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/127386" target="_blank">📅 15:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127385">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idj377ZyOtsMR4kpNMJNlywH89ey3fI9o96x6z9ZZp0AzJdbiT6Ov7XtHpUKVg36nCpT7lQEdRnKMweiUy4VjfylL__18Phzl-PnVHAit1Uh9VgtpSVpkpi4EoJPBc5znC2T9g3lSCuQBz_0j_cjWzFjLqwNX6gJfxMfRvIk_42uyHDnRswuCcqJxVtEhB3M_u9DU8bPScx1v0rn7JoMuoEIv4z26aH1pMUMAs4Oe6tKnlhEobquMJdCBi9CAP9k6Qhz4Cwcdamat5ckl5Pr65JmSFMty9ti-bK122AWGfF56gMYji0ZJfH4aEzV3gansHc_hBBkxUi09FfpE4dwKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل دستور تخلیه فوری سرافند، توفاهتا و مزرعه سینا تو لُبنان رو داده
🔴
دلیلش هم نقض آتش‌بس از سوی حزب‌الله اعلام شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/127385" target="_blank">📅 15:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127384">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hT4WZlz9ymGUccOGyQvWxQtr4p9PPznoFh_CuEVK-ofQ3L1O_ZxdTdKuKs2ZKCLLMPj3vWlyiHoflquTeILx2qz5n6fy6r3zSWx8ivB5rnb4s_PoFSuzNHtrE8uT5VbrWmdHgpSNZUYc0TA1Zb7HBmzp3hqOso__mS-Dh61A3kDZ7ornIHRv91MoBg7NozbVUcUFf5ec2WWwT9L654vKorg65ZI_2QQ42rOnbD2lDnGu0rA_cJ9TqGMpB8JUsfQR82vXvEzlqeaPnIgWdpaMJ9_Zbq-U0YS1XTz3ZrvyHDDlXd_u3QK4aRvkJzpBdga6f9A_eEukiJsI0iuX_rcT8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رائفی پور: خون آقا رو پایمال نکنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/127384" target="_blank">📅 14:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127383">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UerQNrslxkbekq0BaFqXYoIiqiFy9LkJgI2IlYIGZ--p6pwnP7Ff6v5bz-366B6P4X8Dt6tiCJnfs1sz4QXBSic2BoM8Hj4sPqxzpxcFu0Qs9aOj376ZGbAi8kvkUm-pYuMx9o-A3ZP3ZmpDgDZ9rvvJX7TQp7367yHeFFHl8eO2csfESkxtsMS0u0ZbFcI8QbpoB15-tzEjJZcem6c97LAF2-TfigPNi6PdZSAvGMTmtbqQg3M5-PWeTJBMHOsgHEwmlapdrkQIxcSi_m9H13iWilUa_ISmOdhNmX2-8m-KvV0N3fo1KZtue0VV0eQDWYsQDaIp65K-8ji8_4CTRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امام جمعه اهواز: سازش با دشمن در هیچ سطحی جایز نیست
🔴
عقب‌نشینی در مقابل امریکا و اسرائیل ممنوع است، باید انتقام بگیریم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/127383" target="_blank">📅 14:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127382">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbcWV0seMIfKo8vZgc5MbFTcW2aKvkXGsl5vAyrExGpeXOirdURsynC05Vh6OYtgzKTwhd4adEDE1spSE6ooQEgE4kzLcxVYVROK4PDkKxK9jussnJ2_jAjMz7PorhKlbmNIvPMsR8z4L2CnLVwsYcMZiYoYfIqPYQutNqmsE8e00J69s1ViljVJ8yiuc_-ehFbxZN-UyT3bu0lCvxA63wUzhqcSATiUo3B5VIdWOEqD5p35p7k2c6FZmbh5qqQnIfZDX7Q81n_AyMjIUCsectLHN52PvPkqc0dJphpwonC6WmgcTr0aDbEKRwQB-pH9AMdVDzLHFfkHkvi_zaf8OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش تند نبویان به خبر توافق: می‌خواهند متنی خسارت بار را به عنوان پیروزی جا بزنند/ مدیریت تنگه هرمز از دست خواهد رفت و تحریم ها هم لغو نمی‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/127382" target="_blank">📅 14:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127381">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
تیراندازی در نزدیکی کمپ تیم ملی آرژانتین در کانزاس سیتی آمریکا
🔴
حادثه تیراندازی در یک ساختمان مسکونی رخ داده است که منجر به مرگ یک نوجوان و زخمی شدن دو نفر شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/127381" target="_blank">📅 14:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127380">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/390974dead.mp4?token=cwrtGR1viE9zSBN9o0aop1MTFtJZjbZ40yP-h4X-dfeDsLJiun-85i9SdR0CC64X7i7nlMUI2ljUgb7IuQrhKwlc3IfHMm2qB-wVfzzW5K1XTZkwskUxWxnsHimNIUtUXEcSTlICejg2RuGKfJ3zLL5UIyUOxoPk0zMdpl_nXWVb4XSNPWUMD1wgOgxKOgoFHXVhiazog9Hd3iXvENSs9KiAqEi78GrIswnHPI0cv1wFNIAGkLOxSTKfdN09yWxGizO9wlq-TsSzHygoTlN-WeD5QSyAk7z9aQD4nDvXdiBaWPStnr27JsyLoUiI6r3Ru6bNFuOnhanrY5-TuAVQU5yEoHsL9-Grd7vopw4PllUhxU8S8Jn_N3wOyGLSIYQXwqGcp3RBhgkC1S7seZVj62s-h5-2zvfx-msxkBE0znc9lobENYV4tDw4Imv5QhyVhExXxZ0VJRYGP0YuWuzd2NM56XiA5wOXIEwxCicWPHC3PBIUs4pCiKfMJABYZJg2i1dTM_yp1IGeEWGuIRtfIIb4xXYGmKPP9MUbkKER4_kX_bShcFBVwnUmF3Dv5DisZWR5O1VOxJFXG3ITqig4LD6hbGS6b6NtFC5s2WR4TBsCKJ5jfLAK1jYzDCysGSd2kcdy5fmck1QshPCFpCaTBxRCwrV3dQhguUs1Wzpr2Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/390974dead.mp4?token=cwrtGR1viE9zSBN9o0aop1MTFtJZjbZ40yP-h4X-dfeDsLJiun-85i9SdR0CC64X7i7nlMUI2ljUgb7IuQrhKwlc3IfHMm2qB-wVfzzW5K1XTZkwskUxWxnsHimNIUtUXEcSTlICejg2RuGKfJ3zLL5UIyUOxoPk0zMdpl_nXWVb4XSNPWUMD1wgOgxKOgoFHXVhiazog9Hd3iXvENSs9KiAqEi78GrIswnHPI0cv1wFNIAGkLOxSTKfdN09yWxGizO9wlq-TsSzHygoTlN-WeD5QSyAk7z9aQD4nDvXdiBaWPStnr27JsyLoUiI6r3Ru6bNFuOnhanrY5-TuAVQU5yEoHsL9-Grd7vopw4PllUhxU8S8Jn_N3wOyGLSIYQXwqGcp3RBhgkC1S7seZVj62s-h5-2zvfx-msxkBE0znc9lobENYV4tDw4Imv5QhyVhExXxZ0VJRYGP0YuWuzd2NM56XiA5wOXIEwxCicWPHC3PBIUs4pCiKfMJABYZJg2i1dTM_yp1IGeEWGuIRtfIIb4xXYGmKPP9MUbkKER4_kX_bShcFBVwnUmF3Dv5DisZWR5O1VOxJFXG3ITqig4LD6hbGS6b6NtFC5s2WR4TBsCKJ5jfLAK1jYzDCysGSd2kcdy5fmck1QshPCFpCaTBxRCwrV3dQhguUs1Wzpr2Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار صداوسیما: اکنون تنگه هرمز کاملاً آرام است و نظم ایرانی در آن حاکم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/127380" target="_blank">📅 14:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127379">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glmsNzP-F9Xg-99Y2824bhPnbCUcyu4rM7BlV151lsmzftol6sgOEvl0oJkbYaJHBa9AXOTV7fSZ_fbW-8PEfxdIKlCUJdJJBRljxG6s0iJjXvMBjdBPwyW3aSqw_rQXf2Gl9SLsiqkWx0ukV8Bh-tYBCSmnXPF7a4JOgbyjdsU0TBtkRhJ7j-51lMCFznI1cledR3o8zXmCyKOSuw93NiDomZaRdOmrqK0fxB9nrgF4JDyc3pEObUZqS1KdYLb7wS7RoClGrDhtfmKZleILCtasTiinTKhrCZMDYuhCbJiflC9xaxLSITuaK5RHKG5iokVi2mHAB5AiMaa_ap8iRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خودروسازان در حال ایجاد یک ائتلاف مشترک برای اعمال فشار جهت وضع مقررات جدید هستند.
🔴
این اقدام با هدف ایجاد شرایطی برابر و افزایش توان رقابت با ورود گسترده و موج فزاینده خودروهای مقرون‌به‌صرفه و ارزان‌قیمت چینی به بازارها صورت می‌گیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/127379" target="_blank">📅 14:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127378">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0QY32Y4XQlFKD1pZDZzCWj-4gfocOci-0kqjibd_koI-ypoHsmCvf3nlufKWxB8WsoN7v0qh_xo-_6tRH0PIJtS0_tH8NPO5OyB_35v1jCyYM_Yp-O9iQ4SFv3ABN51Igxv1uuwCuHPZBndWljmlw8rOMgOjBSHUvA2z_0zWxr11Ep426ZmeEDjVMCatiRwOihq-2QeDnKEX0sU4DF_y_jsM1ywFP9BbuCnGLtTPhedXXid5pnrak8YC3pmfIWoemU8yNgAgtjGpmDn36i7JzNWo53TBs0zPfinmmYURWZn8oTutVcZh0ymyqa68EeB3fv2gvMoA5tEYQCw3QLJSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/127378" target="_blank">📅 14:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127377">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c811e80be0.mp4?token=eDFvjK-PUX74wy5zjPZOKqoc7szR09l1l_4PxWfWazwtGUpwJ-_3-eferzQjiWDdPFcNwaN27D9Bvvy9nmSSMlh1TqW1_vXsfFxHKKR13Zu2qlLoWqXbbUGHmfTfUMIlJdRFW6P2tbX_74K9Hg22CazQaeGhKixOzUSTK-Gng69BBKmNydTg7MKQGqZk8Jyn2cfo-Sq-0_1JEeyhYGO9GPNG94rnZBtZqDoaDIrwFSiTjl2vpPy_usBcsMIxqe_zliFA_jFu667rvII82p2W5vcBU9ycPdsY-moXtMnDYKtQ8zP9UqgXEyFuq4hYG6fxiu9nz97TE-_36q4ZK2Gb3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c811e80be0.mp4?token=eDFvjK-PUX74wy5zjPZOKqoc7szR09l1l_4PxWfWazwtGUpwJ-_3-eferzQjiWDdPFcNwaN27D9Bvvy9nmSSMlh1TqW1_vXsfFxHKKR13Zu2qlLoWqXbbUGHmfTfUMIlJdRFW6P2tbX_74K9Hg22CazQaeGhKixOzUSTK-Gng69BBKmNydTg7MKQGqZk8Jyn2cfo-Sq-0_1JEeyhYGO9GPNG94rnZBtZqDoaDIrwFSiTjl2vpPy_usBcsMIxqe_zliFA_jFu667rvII82p2W5vcBU9ycPdsY-moXtMnDYKtQ8zP9UqgXEyFuq4hYG6fxiu9nz97TE-_36q4ZK2Gb3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این ویدیو قدیمی مجدد وایرال شده!
🔴
فائزه هاشمی: مجتبی، بن سلمان ایرانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/127377" target="_blank">📅 14:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127376">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
العربیه: وزیر امور خارجهٔ پاکستان در گفت‌وگوی تلفنی با مسئول سیاست خارجی اتحادیه اروپا دربارهٔ تلاش‌ها برای دستیابی به تفاهم میان آمریکا و ایران گفت‌وگو کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/127376" target="_blank">📅 14:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127375">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
خبرگزاری ایرنا: تهران تضمین‌های مشخصی در مورد دریافت خسارات از طرف‌های ثالث دریافت کرده‌ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/127375" target="_blank">📅 14:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127374">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5tnQmn0wrh8tm4gZBcc5sSWEz6yCKG_itU810uwi5Y3-C9wE-FMqC-nXz0q4bED7SeU61RUtC0EfJEo2A4yhhuh-AAPYes7PTI0E6QtbQVYUnsXTBlFl7hLgD97F5IIBsXSIk5pCiUjtgd6TIbycdEhz4FPP8ps3F3RBC6j3FxAQ6u63KomARDwsf64gX8GnY4JzMUvIaLF-iDSe90K28W9lF0Rsbv-qcHv67M_9EXJyhp88ca683PS6fZZ-SJJwsMMl6_wmRcyZfrQnnIPmwQfe3CELs2tJMwMgvwLnMT1HR01oWYmNQA103zG5oPd8OUxgOMDzi4aMx4Kkqxxow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمید رسایی:
توافق چیه؟؟؟؟ اینترنت رو قطع کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/127374" target="_blank">📅 14:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127373">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6v1BvlKK9w5C1-6FB_d9LIyCgnX8vUcrQE_mUHTJl5WqebEGjV62mdbw0xj5QhQ4ZW6IhObvBLY5LgyMZPDF7r3GsI2ls4kM8s78yT2BuJGtkA680Do1Dq3NiUQ3i7WuirEfLSVxIFMzMBf5LI0GV8QWjMHjVud8-j_0xBUCge1xFMrVJ2_tRXhgT-8NmRn7bVsWAhd7a00Qik0Pwmh3ULcUu8OPy0lCKruwZrDIqRYpQHxigrNwXnm_laI5dSBnex1XINMNp78YPW0ln98Q0flMmPjy7PP0JuLgZMJCUg1AJVJe6zZJTKSfYUYmPIyCQItmAeQ-LCAPYwcMhm0vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جزئیات خواسته های ایران در تفاهم به روایت ایرنا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/127373" target="_blank">📅 14:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127372">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گویا تجمعات شبانه امروز هم ادامه داره</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/127372" target="_blank">📅 14:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127371">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بعد از علی کرار! علم‌ماند برقرار! که مجتبی آمد و رفت به رزم و امضا</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/127371" target="_blank">📅 14:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127370">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a44893f6f.mp4?token=vW7Un_Yz4CS15_4PpGs3s0a8_qvo_XX3VMuA53OwYOJzN__O4fB92SX-aRsLdNtkL9FwZsFwcng49uoz7W0DwdLIMgGUEsjuuRTlIvpznUQKBV5IblN0-CgO9MYjJpY47WyJ4oEB6L0suJy4Sunew9CwkbfNbOHlNSobaE-_PT1A7VwRDVol13ES201wNZYCuc0WiOAY98-U82qEeVCqJ6i0M_vv-QHPAU_e6CZmRol6G5-ZEtOvWzTBtPUtW7_dKc_wx2i-gQEVUZ4I3tU1h36-W1dQKVhnnjcXi3hXrGpu6yxrpw7Q-5MAFX7pXC0rCRwQhtaUS2Qo2EMJ2N_o4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a44893f6f.mp4?token=vW7Un_Yz4CS15_4PpGs3s0a8_qvo_XX3VMuA53OwYOJzN__O4fB92SX-aRsLdNtkL9FwZsFwcng49uoz7W0DwdLIMgGUEsjuuRTlIvpznUQKBV5IblN0-CgO9MYjJpY47WyJ4oEB6L0suJy4Sunew9CwkbfNbOHlNSobaE-_PT1A7VwRDVol13ES201wNZYCuc0WiOAY98-U82qEeVCqJ6i0M_vv-QHPAU_e6CZmRol6G5-ZEtOvWzTBtPUtW7_dKc_wx2i-gQEVUZ4I3tU1h36-W1dQKVhnnjcXi3hXrGpu6yxrpw7Q-5MAFX7pXC0rCRwQhtaUS2Qo2EMJ2N_o4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
۶ سال پیش"علی خامنه‌ای" گفته بود :
- اصلاً پیامی مستقیم برای ترامپ ندارم، چون حتی در حدی نمی‌دونمش که بخوام باهاش پیام رد و بدل کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/127370" target="_blank">📅 14:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127369">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
فایننشال تایمز: هفته‌ها بمباران ایالات متحده و اسرائیل، مجتمع‌های موشکی زیرزمینی ایران، از جمله یک سایت اصلی در نزدیکی یزد را هدف قرار داد.
🔴
با وجود حملات مکرر، ساکنان و تحلیلگران می‌گویند که ایران در طول درگیری به پرتاب موشک ادامه داده است.
🔴
در حالی که به نظر می‌رسد بمباران، میزان شلیک ایران را کاهش داده و به ورودی‌های تونل آسیب رسانده است، ارزیابی‌های اطلاعاتی و دیپلمات‌های غربی معتقدند که تهران بخش عمده‌ای از زرادخانه موشکی، پرتابگرها و زیرساخت‌های زیرزمینی خود را حفظ کرده است. طبق گزارش‌ها، بسیاری از تأسیسات ظرف چند ساعت یا چند روز بازگشایی یا تعمیر شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/127369" target="_blank">📅 14:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127368">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
فوری/سخنگوی وزارت خارجه: متن توافق پایان درگیری ایران و آمریکا تقریباً نهایی شده و منتظر تأیید نهایی نهادهای تصمیم‌گیر است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/127368" target="_blank">📅 14:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127367">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
فوری/سخنگوی وزارت خارجه:
متن توافق پایان درگیری ایران و آمریکا تقریباً نهایی شده و منتظر تأیید نهایی نهادهای تصمیم‌گیر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/127367" target="_blank">📅 14:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127366">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
فرودگاه هامبورگ در پی یک حادثه امنیتی تخلیه شد
🔴
شبکه ان‌دی‌آر به‌نقل از پلیس هامبورگ اعلام کرد که فرودگاه این شهر در پی یک حادثه امنیتی به‌طور کامل تخلیه و تمام پروازهای آن متوقف شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/127366" target="_blank">📅 14:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127365">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
خبرگزاری دولت: هدف اصلی امضای تفاهم‌نامه، پایان جنگ در تمامی جبهه‌ها در منطقه است. در این تفاهم‌نامه پایان جنگ علیه ایران به اضافه تمامی جبهه‌های دیگر منطقه به شمول لبنان مورد اشاره قرار گرفته‌است.
🔴
نام کشور لبنان به عنوان بخشی از توافق پایان جنگ در صورت امضای متن فعلی تفاهم‌نامه مورد اشاره قرار گرفته‌است و
آمریکا تعهد می‌دهد که رژیم اسرائیل را وادار به پایان جنگ در لبنان، کند
.
🔴
عبارت تمدید آتش‌بس در متن فعلی ذکر نشده‌است و اشاره به چنین عبارتی در برخی گزارش‌های رسانه‌ای نادرست است؛ متن تفاهم‌نامه خواهان پایان قاطع جنگ در تمام جبهه‌ها می‌شود.
🔴
تهران تضمین‌های روشنی برای آزادی دارایی‌های مسدود شده بر اساس ساز و کارهای مشخص و مورد نظر تهران دریافت کرده‌ است و در صورت تصمیم تهران به امضای تفاهم‌نامه پایان جنگ، بخشی از دارایی‌های مسدود شده بلافاصله و بقیه به تدریج در طول مذاکرات، آزاد خواهند شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/127365" target="_blank">📅 14:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127364">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d242dab561.mp4?token=JGKdn5b7yDy57MCt4hz2TAmRzj23h1aROemnkSm6c7FZ7Ma8AZ09nEes0muSv3aXZPx2tuhMLLThvaGO29hCLrbyPt-oTlMsJ7sIeX0w04quIAjANzuhnlE6cUvFPxtimCHztQgCEMnoQU2uFWJkyq-BCeZSO_4iATaJCVMj8NoT9b-KVIHLCRiMTEv2DnkraeoVQyOsiSjGxD2cOaFH4Z6i3TZxwZBiOltm_1m56PNngmBABHgnAINHhfQdodednOuwyc0J51fT3B-ckp3gIJyqcyIqvjEaN3Y7jaJ1PjS56lb5tEnsULB7uiMyEjb-liJGE1cbW6D3O8UaC48JUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d242dab561.mp4?token=JGKdn5b7yDy57MCt4hz2TAmRzj23h1aROemnkSm6c7FZ7Ma8AZ09nEes0muSv3aXZPx2tuhMLLThvaGO29hCLrbyPt-oTlMsJ7sIeX0w04quIAjANzuhnlE6cUvFPxtimCHztQgCEMnoQU2uFWJkyq-BCeZSO_4iATaJCVMj8NoT9b-KVIHLCRiMTEv2DnkraeoVQyOsiSjGxD2cOaFH4Z6i3TZxwZBiOltm_1m56PNngmBABHgnAINHhfQdodednOuwyc0J51fT3B-ckp3gIJyqcyIqvjEaN3Y7jaJ1PjS56lb5tEnsULB7uiMyEjb-liJGE1cbW6D3O8UaC48JUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت ملت وقتی به تحلیل‌های خوش چشم اعتماد کردن
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/127364" target="_blank">📅 13:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127363">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
خبرگزاری دولت: متن نهایی تفاهم‌نامه تا زمان پذیرش قطعی آن توسط دو طرف منتشر نخواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/127363" target="_blank">📅 13:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127362">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
خبرگزاری دولت: به گفته سخنگوی وزارت امور خارجه جمهوری اسلامی ایران، کلیات و متن تفاهم‌نامه پایان جنگ میان ایران و آمریکا تقریباً نهایی شده‌است و در انتظار تصمیم نهایی نهادهای تصمیم‌گیری در ایران است
🔴
تهران در طول دوران تبادل پیام‌ها، برای اطمینان از اجرای برخی مفاد تفاهم‌نامه تضمین‌های معتبری از برخی طرف‌های ثالث برای اجرای تعهدات پیش‌بینی شده دریافت کرده‌است
🔴
بر خلاف برخی ادعاها که از سوی برخی جریان‌ها و فعالان سیاسی در طول قریب به یک ماه گذشته مطرح شده‌است، متن تفاهم‌نامه پایان جنگ میان ایران و آمریکا با دقت و وسواس بسیار تهیه شده‌است تا جای هیچگونه تفسیر به رأی و فرار از تعهدی برای طرف مقابل وجود نداشته‌باشد.
🔴
تا زمان پذیرش کامل متن توسط جمهوری اسلامی ایران، تمامی متن‌های منتشر شده در رسانه‌ها، صرفا گمانه‌زنی‌های رسانه‌ای هستند و متن نهایی تلقی نمی‌شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/127362" target="_blank">📅 13:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127361">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/127361" target="_blank">📅 13:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127360">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
پزشکیان: ملت ایران با وجود همهٔ فشارها و تهدیدها، از استقلال، عزت و تمامیت ارضی کشور دفاع خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/127360" target="_blank">📅 13:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127359">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
تسنیم به نقل از منابع آگاه: فشار نظامی و دیپلماتیک آمریکا برای تغییر در متن ۱۴ ماده‌ای پاسخ نداده و آمریکا از طریق واسطه قطری اعلام کرده است که نیازی به اصلاحیه‌های اخیر آمریکا نیست.
🔴
این متن همچنان نیازمند بررسی و نهایی شدن در نهادهای ذیربط در ایران است و تا آن زمان سایر گمانه زنی‌ها و خبرها، معتبر نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/127359" target="_blank">📅 13:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127358">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
اسرائیل هیوم: ایران موافقت کرده است اورانیوم غنی‌شده خود را تحویل دهد.
🔴
از غنی‌سازی بلندمدت صرف‌نظر کندو  آمریکا ۱۵ میلیارد دلار از دارایی‌های ایرانی (در قطر) را برای نیازهای بشردوستانه آزاد کند.
🔴
ایران باید متعهد شود که به دنبال دستیابی به سلاح هسته‌ای نباشد. تنگه هرمز بدون محدودیت باز خواهد شد. هر دو طرف متعهد می‌شوند که اقدامات نظامی بیشتری علیه یکدیگر انجام ندهند.
🔴
پرونده لبنان همچنان شکافی بین آمریکا و ایران باقی مانده است. انتظار می‌رود یادداشت تفاهم روز یکشنبه در ژنو امضا شود، در حالی که ترامپ برای اجلاس جی۷ در فرانسه حضور دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/127358" target="_blank">📅 13:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127357">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
کلش ریپورت: مصر و ترکیه در حال برگزاری یک تمرین هوایی مشترک در چندین پایگاه هوایی مصر هستند.
🔴
این تمرین شامل مراحل نظری (یکپارچه‌سازی مفاهیم رزمی، تبادل تخصص‌های آموزشی) و پروازهای عملیاتی متمرکز بر مأموریت‌های عملیاتی مشترک است.
🔴
هیچ نوع هواپیما یا تعداد آن‌ها به صورت عمومی اعلام نشده است
🔴
این تمرین پس از مانور دریایی مشترک «دریای دوستی» در سپتامبر ۲۰۲۵ برگزار می‌شود، که اولین تمرین‌های دریایی مصر و ترکیه در ۱۳ سال گذشته بود.
🔴
دو سال پیش، برگزاری یک تمرین هوایی مشترک بین این دو کشور غیرقابل تصور بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/127357" target="_blank">📅 13:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127355">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
فارس: آمریکا عقب‌نشینی کرده، ایران بررسی را آغاز کرده و هنوز هیچ توافقی حاصل نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/127355" target="_blank">📅 13:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127354">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
بلومبرگ به نقل از یک مقام گروه هفت: توافق بین واشنگتن و تهران به احتمال زیاد یک یادداشت تفاهم خواهد بود، نه یک توافق نهایی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/127354" target="_blank">📅 13:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127353">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
بلومبرگ به نقل از منابع: توافق بین تهران و واشنگتن ممکن است یکشنبه آینده در ژنو امضا شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/127353" target="_blank">📅 13:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127352">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a72e0fc3c.mp4?token=lKatXpEwNURKls4j4gWoSMdvwO0P1NPPGSrNPA96bfGGJmxPJ4KsR48zzLIyVObbbPZydJgZGbHcPR2fLCd9Gv_dYyESssNoZj8tnipesNQmak0GhMhKvRekUgLm6bzWyiN5q9SF0feAUWyQnZISSzqceSHFVRQamBZDwTtr6tTClUQs-5boIbxSeWgSiC6tv18mCwksM1VfOb1OaHvHTs1gi3tNwIuKKy2hmwWWxOHzBMUqGKSWAYExaflyDeba9MYPAWL3XIoWo59E7_vut7BX9dY_wkP--bh1-gXT8H1IH4b8y_gProKrf3HLHJUo-BUigotmQwFJYkH6q271oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a72e0fc3c.mp4?token=lKatXpEwNURKls4j4gWoSMdvwO0P1NPPGSrNPA96bfGGJmxPJ4KsR48zzLIyVObbbPZydJgZGbHcPR2fLCd9Gv_dYyESssNoZj8tnipesNQmak0GhMhKvRekUgLm6bzWyiN5q9SF0feAUWyQnZISSzqceSHFVRQamBZDwTtr6tTClUQs-5boIbxSeWgSiC6tv18mCwksM1VfOb1OaHvHTs1gi3tNwIuKKy2hmwWWxOHzBMUqGKSWAYExaflyDeba9MYPAWL3XIoWo59E7_vut7BX9dY_wkP--bh1-gXT8H1IH4b8y_gProKrf3HLHJUo-BUigotmQwFJYkH6q271oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروی هوایی اسرائیل داره به روستای تبنین تو جنوب لُبنان حملهِ می‌کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/127352" target="_blank">📅 12:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127351">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
مقامات گروه ۷: تفاهم‌نامه آمریکا و ایران ممکن است همین یکشنبه در ژنو امضا شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127351" target="_blank">📅 12:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127350">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceca5f8bc2.mp4?token=a5TlP1OoWLXNgZDI01dyhFAGsfLlcAoQ3Dxo20N6AK8WYcQUjOYHIAIvErikXN4FH2K46iylm7bu_wmi5VaR0GVaJRZ8J9mLzdyafJLdKlmgifY_gQXAqcKNNoq4_9K0aP3kWGmZCQEWy33HiCRdP8_oeQb029ddMyKTafnj3zQeulDHIVZIEWX_WWBJLdPsyksO7b9oF0as4Po41BuGLdRziaC4lT6409g2vrcF-bjYrPC6tS1RXMNXrbBvfDvbasCEAFkN9n7tPE_PDpffvnO4zwlhVFjmWG9goLn3FtvJHZpX2aQmNF75KlGi_QLjtHYiWpGp0cVbAWXoJytEoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceca5f8bc2.mp4?token=a5TlP1OoWLXNgZDI01dyhFAGsfLlcAoQ3Dxo20N6AK8WYcQUjOYHIAIvErikXN4FH2K46iylm7bu_wmi5VaR0GVaJRZ8J9mLzdyafJLdKlmgifY_gQXAqcKNNoq4_9K0aP3kWGmZCQEWy33HiCRdP8_oeQb029ddMyKTafnj3zQeulDHIVZIEWX_WWBJLdPsyksO7b9oF0as4Po41BuGLdRziaC4lT6409g2vrcF-bjYrPC6tS1RXMNXrbBvfDvbasCEAFkN9n7tPE_PDpffvnO4zwlhVFjmWG9goLn3FtvJHZpX2aQmNF75KlGi_QLjtHYiWpGp0cVbAWXoJytEoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگست به مناسبت توافق ۴۴تا پرس سینه زد و فیلمشو منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/127350" target="_blank">📅 12:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127349">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
خبرنگار العربیه: یک تیم حقوقی پاکستانی در مراسم امضای توافق ایران و آمریکا در یک کشور اروپایی حضور خواهد داشت.
🔴
ایران درخواست کرده است که امضای توافق با آمریکا در یک کشور اروپایی انجام شود تا به آن جنبه بین‌المللی بدهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/127349" target="_blank">📅 12:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127348">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
مقام آمریکایی به Reuters : دو تا پهپاد ایرانی دیشب خواستن به کشتی‌های تجاری تو تنگه هرمز حملهِ کنن، ولی رهگیری کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/127348" target="_blank">📅 12:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127347">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
رسانه عبری i24: از جزئیات توافقی که تاکنون اعلام شده کاملاً مشخص است که ایران تضمین‌هایی از آمریکایی دریافت خواهد کرد مبنی بر این‌که اسرائیل تا پایان دوران ترامپ هیچ‌گونه فعالیتی در خاک ایران انجام ندهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/127347" target="_blank">📅 12:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127346">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل: مذاکرات نهایی ایران و آمریکا بر مسائل اقتصادی و هسته‌ای متمرکز خواهد بود و شامل بحث‌هایی درباره برنامه موشک‌های بالستیک ایران نخواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/127346" target="_blank">📅 12:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127345">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
عضو کمیسیون عمران: بیش از ۷۰ درصد درآمد خانوار صرف اجاره خانه می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/127345" target="_blank">📅 12:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127344">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f73bf5f98.mp4?token=NYnz8TZqEoIVD94pGQiIrdGTe8vmbktUyE-oObcd6T7aCJMxu9UHgVJvUakYvp34WW_sIielbWWw_7w5SZlRIeKQ9pG63C4GN-vIqlw4abeRTqmL5YS7WIifIrU2qTe8M7W7Z_Q6v0c4GmSfHcFiPdrR7a00D2FoVvPdbXOaMF6zQcLaWbD2xkh98eWMx3a_GSwc6VpiANB62Dtc5y3wp_AIMAOll-mjGqgIu3lCoXBi9dP3AsmnmnmYlBRK0rHUNfHMnV9rppO2bmTgRLY9eKOogGYk-i-duxzx-UV4_g2Pf4wo5rDe_OSk6YuQSjsZ2WBgV7uzMK8RMT_qLBaMtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f73bf5f98.mp4?token=NYnz8TZqEoIVD94pGQiIrdGTe8vmbktUyE-oObcd6T7aCJMxu9UHgVJvUakYvp34WW_sIielbWWw_7w5SZlRIeKQ9pG63C4GN-vIqlw4abeRTqmL5YS7WIifIrU2qTe8M7W7Z_Q6v0c4GmSfHcFiPdrR7a00D2FoVvPdbXOaMF6zQcLaWbD2xkh98eWMx3a_GSwc6VpiANB62Dtc5y3wp_AIMAOll-mjGqgIu3lCoXBi9dP3AsmnmnmYlBRK0rHUNfHMnV9rppO2bmTgRLY9eKOogGYk-i-duxzx-UV4_g2Pf4wo5rDe_OSk6YuQSjsZ2WBgV7uzMK8RMT_qLBaMtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری صدا سیما: هک تصویر انفجار اتمی در تلویزیون، سیگنال آمریکا بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/127344" target="_blank">📅 12:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127343">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
مراد ویسی: با توافق احتمالی، دست ترامپ هم به خون جوانان کشته شده دی ماه آغشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/127343" target="_blank">📅 12:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127342">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2UimXL6VVz2lUflquN0DHzcF2aOMo86b1xL_eAVW6l4SL9k2YBShxXT-2L-7B9idAMz0yyfYpvPTyxr7ra9e7MrGPt71ADjwr8g4J8QY6EyxCi80UxTu1K-04i92OJZh4iiQaF96BAkrCId5BiA5ZLdV1ANJm5DUJlne703N08LluIRCShlN414KUik0wy_KwOw9wqaHFNbjotmja81D9pEOupSFK-1fd7W1QFVyVvpAhZf-gOYhaD1Q9ZaLrhGMAOUaBjhSMYvOFnZOG4zp0ru76I7J6bu4IGRC2B-t66aD0or2Ptxxq_VeOAe1CFjdGcTSipPF_uyg_cVZttNCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبی:هنوز ویزاها نیامده است
امیدوارم اینفانتینو به وعده‌هایش عمل کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/127342" target="_blank">📅 12:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127341">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3dQTKeNr4kqR-hE79fFx0rGYEQB4zqg2Xbh0GKR6aUekxSvKpz9BjYguFyv4hHS9FrRGhOAXysjrktDz9s5Lt9Hx8q1Qev0TBs8suTQbO9_s8kfE9YpMMDowl9g6Rix_dB3AGfPoruI6QvBum9JDA7h3WyOs1PUks7MPK6Yf7K_1PmpudSToROa7V12uVhgd5zCEB6jlxn4QI-TRvLnZflXBaxC8fqRpFwpgxaQw093SsO4qUTysUC4LWjVkQ_ueyfqnUmisPSBVEqvagm3iXmrvG1kCVGROdsP34fyFW-mXQ-vR2GL4tv8VNclR1wfJcQKb7Adzct4OPL2iwhkgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کلش ریپورت: به نظر می‌رسد ایران به رادار هشدار اولیه AR-327 در جبل الدخان، بلندترین نقطه بحرین با ارتفاع ۱۳۴ متر، حمله کرده است.
🔴
این سایت میزبان یک رادار مراقبت هوایی سه‌بعدی برد بلند ساخت شرکت بریتانیایی BAE Systems با برد حدود ۴۷۰ کیلومتر است که در یک رادوم ثابت قرار دارد و مسیرهای دریایی خلیج فارس و مسیرهای هوایی منتهی به تنگه هرمز را تحت نظر دارد.
🔴
ستون‌های دود در تصاویر منتشرشده توسط ایران، توسط تحلیلگران OSINT به‌طور مستقیم به محوطه راداری در مختصات حدود ‎26.0375°N, 50.5420°E‎ مکان‌یابی شده‌اند.
🔴
این رادار یکی از گره‌های شبکه منطقه‌ای هشدار اولیه و دفاع موشکی مرتبط با ایالات متحده است که به عملیات ناوگان پنجم (Fifth Fleet) متصل می‌باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/127341" target="_blank">📅 12:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127340">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wv20CWZC0OoDGB1Ih_aLUns8FNycgb2NiedQroI1m_1rPm5HAeHSJBvbkfkpjQF_gN9TAB-Z6J-tDXU42AMz5Do7zshanklgrh8-Uw_qYhR6p7CmmAeyY18rPDqUjbgMB4mg9BEEu3CfgFcHNCbLZ91L73b3-6rh2zUmtOCBGNnJzJqWNwNiMu_6hsYNAiTEqXdiMyFNk7v5fT4ZE1kDhGwMUAxdx5uSGIkJ5tbpsQjTOZ1-6TKjWOV7Vxz5Ar1htSgCIyyQoGU0Uwivlp28WEEMbLzr9TYABCNR3jm_LGXk_Hm41cx_AJ-n9hDyHHir677gmnKLH7feV5utjy7bLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت آمریکا در ساعات گذشته ۳.۲ درصد کاهش یافت و به پایین‌ترین حد خود در ۵۶ روز گذشته یعنی ۸۲ دلار رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/127340" target="_blank">📅 12:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127338">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
تصویری وایرال شده از تجمعات شبانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/127338" target="_blank">📅 12:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127337">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
حاییم رامون، وزیر پیشین اسرائیل:
توافق میان واشنگتن و تهران توافقی بد است و به اسرائیل آسیب می‌زند؛ همچنین این توافق پیامدهایی برای سرنوشت سیاسی نتانیاهو نیز دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/127337" target="_blank">📅 12:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127336">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBSMawcaTjf4JzyJ8UQbhCV9omxQAnY-EgTDPotgeZTeMPfAFz5WNI6QAgiWbHCSABrHuCFnCU9dcqxxpkLugZoOmnCT7EpxwAZrHVo9G1KxHXcx-96G6PEzXbJguYGTaJX_WkR9tlPZgHsjUvNQM2D2aR90_OqggT0kJaWdx_tRyJKU9xvGk6W_NiGISIM8ofY-WZXfqa4Je9ZiUdzF7C_gtSgaWhEi-LcJOXArO1KsIOEdqj4XRlKdeVWG9QfTvqoFTsUtD-g_WI0zKyIHGbMQSIqndjjxWS023BDo2_WK4lhDUX_AieYf6ENWz08iugI4rmKoGkOgVSh7gb__Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای روسی بیش از نیمی از کنستانتینوکا در منطقه دونتسک را پس از عقب‌نشینی بی‌صدا نیروهای اوکراینی از حومه جنوب غربی، تصرف کرده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/127336" target="_blank">📅 11:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127335">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYAjA6ESLwdhGwt58rEdPP4jWdeHQzOwmdjsZvDRpp2n7t-4RhdihEOF6htbbtNODWFFzVrR-7vLLtLqgmhPK1KEqrFlYNwkz79GQWTXzkEfAzeKVHF6FSnhJ2-DPesDFWDnSiGYXjmHv6MO-0H57-kr8X-Osrhizx-CjeFrs8zeTS-P5hL4qFhFaaRrJXRHCfrg3_oFEEyqAriMH3Itp7fPUMzVZitdTX21Rl4Uz6sAaq_nCY1HSfzfQ75-MxmMVf1YAwZJRXrAGHOtagKx1hh7VzLVJFRfkYURQO_yXIp4hytfmxVO8_IG2de8ajlQRQgEQpw-coyM7sUlAir9Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/127335" target="_blank">📅 11:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127333">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
مهر: جزئیات جدید از پیش نویس تفاهمنامه ۱۴ ماده ای ایران و آمریکا توسط منبع نزدیک به تیم مذاکره کننده ایرانی منتشر شد.
🔴
جزییات این پیش‌نویس به شرح ذیل است:
۱-
توقف دائمی و فوری جنگ در همه جبهه ها از جمله لبنان
۲-
تعهد آمریکا به عدم مداخله در امور داخلی ایران و احترام به حاکمیت جمهوری اسلامی ایران.
۳-
رفع کامل محاصره دریایی ظرف ۳۰ روز
۴-
تعهد آمریکا به خروج نیروهایش از پیرامون ایران
۵-
بازگشایی تنگه هرمز ظرف ۳۰ روز با ترتیبات ایرانی
۶-
تعلیق تحریم های فروش نفت، محصولات پتروشیمی و مشتقات و دسترسی کامل ایران به منابع مالی آن.
۷-
لزوم ارائه طرح های بازسازی ایران حداقل به مبلغ ۳۰۰ میلیارد دلار توسط آمریکا و متحدانش
۸-
۶۰ روز مذاکره برای رسیدن به توافق نهایی مبتنی بر موضوعات هسته ای و لغو کامل تحریم های اولیه، ثانویه، آمریکا و قطعنامه های شورای امنیت سازمان ملل و شورای حکام آژانس بین المللی انرژی اتمی
۹-
تکرار تعهد ایران در پیمان ان پی تی مبنی بر عدم تولید سلاح هسته ای
۱۰-
در دوره مذاکرات آمریکا متعهد شده به نیروهای خود در منطقه اضافه نمی کند و تحریم جدیدی هم وضع نخواهد کرد.
۱۱-
آزادسازی ۲۴ میلیارد دلار پول های بلوکه شده ایران در دوره ۶۰ روزه مذاکرات نهایی. نیمی از این مبلغ قبل از شروع مذاکرات باید در دسترس ایران قرار گیرد.
۱۲-
تشکیل سازوکار نظارتی برای اجرایی کردن توافق.
۱۳-
توافق نامه نهایی توسط قطعنامه شورای امنیت سازمان ملل به تایید می رسد.
۱۴-
مذاکره نهایی قبل از آزادسازی نیمی از پول های بلوکه شده ایران، تعلیق تحریم های نفتی ایران و رفع محاصره دریایی آغاز نمی شود و توافق نهایی صرفا در موضوع سرنوشت مواد غنی شده و غنی سازی، رفع تحریم ها، برنامه بازسازی اقتصاد ایران انجام می شود و بحث درباره برنامه موشکی ایران و حمایت از گروه های مقاومت به صورت قطعی از دستور کار خارج شده است.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/127333" target="_blank">📅 11:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127332">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
نیوزویک به نقل از یک منبع آگاه گفت ترامپ به نتانیاهو هشدار داده که در روتد توافق دخالت نکند و الا با اسرائیل برخورد خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/127332" target="_blank">📅 11:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127331">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
یدیعوت آحارونوت:
نتانیاهو، گفته است که به ترامپ تأکید کرده که درک می‌کند او در پی دستیابی به توافقی با ایران است،
اما اسرائیل نباید قربانی این توافق شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/127331" target="_blank">📅 11:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127330">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2lreCUEU0QZ3nmNxp99UtkdMEbgaPvtMkRkQnRCfOljwqEfzAtbXq-VARRIz5FORryUDsAgEN_aB6lUzyCRZMKEezY7RroRAbri6pPhCZ6QMgwZt7IOt3OnGsC73Jmg95T6c-P7YnOEDJ0HMEzQEVhpRzfIkd4GNKccP2maV3f27fT8c0lEc9ftMFjah3wZodD2MnnJY66tFFgUoaEVzPaCAqhI26XySk-J-abXprQ8-QFnxEz39jhy5QpwVowDGFo770_yb3g1kzXoCMryhg1Ok4ytpz-NOGTFKtRLguragDiU_msvMlQrBeRxI8fUyjGtteBaq2MtNIErtAcEHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا قالیباف هم به ژنو خواهد رفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/127330" target="_blank">📅 11:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127329">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
الاخبار: ایران پاسخ نهایی را از ایالات متحده دریافت کرده که مبنی بر گنجاندن لبنان در تفاهم‌نامه‌های آتش‌بس است
🔴
تفاهم‌نامه پیشنهادی شامل توقف کامل عملیات نظامی، تعیین جدول زمانی برای خروج اشغالگران از خاک لبنان، توقف عملیات تخریب و آزادی زندانیان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/127329" target="_blank">📅 11:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127327">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a0T1x2QvtWSufXi4146YzNwEpcYMnfluPewgJw2FQUfnwVWgkzx7IPqulFtEWX2VuYxZbkYcQOinQ_XknK24vqLf9BeHnOG0WL4nleHWLRDeVV0V6TVtNTdTabURdiUsm1FWNKltw2JJVg5040hP9RskNfBqTql-JTzAXznKfSlzgp_q1U4I4vlqjr1_aK9sh1KS-p1XT5ESajbvavG8iClS8hteEl7F67Zxx7YTvFoM71SyQ8LFd6Smm_P2NRcz3u99UT_0KhtMTS4OvU78d6kGYr5ElFqENsHLLsKyVrRrs7-hwQmUqiEbd0LYYycBmQB71vvJlqzATh7plpZ83g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fozkoj5HCbV9lqwJrpa25ItbGKBcD5HS_b1awD4RXuWThVosslymCrDcZt88Ik5R3oPIpj44lLUn3EYDkZDXojQ-YWTSIaVPl1uVIVkl0boLvCi0zyJ1VIuT-uVno7LN1VrWEQBGy_ob5667IclGQy8eQbivwShH48eit5vU1OoQL8FDL47mc7-gDlviiiHtkWcrof1X1Sm7KbmKTl_ARmGeO03E_7geBQ80pAvbTFmqAnL4stq6waOZIg5kxFQ9m68ilJlMidfEacNQ0-Asj3Y4TD9B-uRjBJt_THEqj5v2L7fmEDTNulncnLG1DFiGhpmJkoOOuh9GWOu_ginJxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصویری از کابین دو نسخه متفاوت از بالگرد شینوک
🔴
نسخه قدیمی‌تر سی که در دهه ۱۹۷۰ ساخته شد و در ایران نیز خدمت کرد
و کابین آخرین نسخه تولیدی که هم اکنون نیز در حال تولید است نسخه اف
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/127327" target="_blank">📅 11:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127326">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
آکسیوس: هواپیمای آمریکایی حامل تجهیزات جی دی ونس برای امضای توافق احتمالی با ایران دیروز به اروپا پرواز کرد‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/127326" target="_blank">📅 11:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127325">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
اکسیوس :  توافق ایران و آمریکا در ژنو سوئیس امضا خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/127325" target="_blank">📅 11:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127324">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
پولتیکو به نقل از مقامات آمریکایی: پس از آنکه رئیس جمهور آمریکا صبح پنج‌شنبه ایران را تهدید به حمله مجدد کرد، امیر قطر، رئیس امارات و مارشال عاصم منیر فرمانده ارتش پاکستان  با ترامپ تماس گرفتند
🔴
آن‌ها به او اطمینان دادند که یک توافق اولیه که راه را برای مذاکرات جزئی‌تر هموار می‌کند، در واقع در دسترس است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127324" target="_blank">📅 11:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127323">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
خبرنگار الجزیره:  تاکنون، هیچ تصمیم نهایی در تهران در مورد تفاهم‌نامه با ایالات متحده گرفته نشده است. هرگونه توافقی باید از لایه‌های مختلف فرآیند تصمیم‌گیری کشور عبور کند.
🔴
برداشت من این است که بیشتر مراحلی که تصویب را تسهیل می‌کنند، پشت سر گذاشته شده است، اما در سطح تصمیم‌گیری نهایی همچنان با مشکلاتی مواجه است. اکنون شبی طولانی از جلسات در جریان است و نتیجه آن هنوز نامشخص است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/127323" target="_blank">📅 11:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127322">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
منابع آگاه مدعی‌اند لبنان نیز در توافق ایران و آمریکا گنجانده شده و پایان جنگ شامل توقف کامل عملیات، خروج اسرائیل و آزادی اسیران لبنانی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/127322" target="_blank">📅 10:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127321">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
الجزیره: بازارهای سهام پس از اعلام دونالد ترامپ، رئیس جمهور آمریکا، مبنی بر لغو حملات برنامه‌ریزی شده علیه ایران و قریب‌الوقوع بودن توافق صلح با تهران، افزایش یافته‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/127321" target="_blank">📅 10:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127320">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKccisSy6cWb-3uQyIygcA0r8v8czCoSP4ZIAdVan37OHOVTVsYeOLEV-1-DoNMDzJWgwOKerEcrA-fpV456JAHO6NGLkjsspdxy-QhhWg-PTSHelvwrStjEzqenG9QM6Ngi4TDZE2eO5k8Jjpne9TPBLcSqYEq8DUE-B1tLZrgNgvZPF0EPRz-dkNWJ9VrxgmnSpdLq1d0kKFV-jsyN6ACMfzDcxwrKDVQz5IR6Glv85-J1d6b0UOwDj9a0_2shOZ4-CzjZFo6_6qJm64csegDfoY1odVdqn43d9sPdn0x6l2KqmDywFCdYpX5sorHzxoT_eMKT6jser335pS1HIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جروزالم پست: رهبران جنوب آسیا و خلیج فارس برای جلوگیری از حمله ترامپ به ایران با هم رقابت کردند و به او توافقی ارائه دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/127320" target="_blank">📅 10:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127319">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYleyv84kTZxwojKK8ZWosKqRsFypDBS_c1T5L2DACcelyUIsHPxn8FudtZ2ggNg1Vvq8Vy83nElcSlN_QLJIjhBHbygz4mENobjVKH_dBV6SoPCi1qpCc8-t5PhQNe5NxfzlKnY4PCaV6klviW4wmUKGr8QLPTuWzGn3nPiobRa41qwcHnzw2pzsP0Z5OUO5vHTi04cJSykbGJcMbXVLsj5rpK73MKrRIcTHscKsPud45DLfl2X0Y_SsGbP3E2CxCeHE-LVqQkKzIXr0gG6wYuWu0EHJCw8eAN2t0TkBhJcvCnRPvxLq77B62Fn-CllMWeptk69_RJ-u_63spAS7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: امیدها برای صلح بین ایران و ایالات متحده افزایش یافت پس از آنکه رئیس جمهور ترامپ گفت که به محض این آخر هفته می تواند توافق نامه امضا شود ، حتی اگر تهران گفت که تصمیم نهایی در مورد پیمان اتخاذ نکرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127319" target="_blank">📅 10:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127318">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9d9b52544.mp4?token=ZQe-6MpCJRwdA5O-rqyWiwU0gJgOm3DQAO5Dr-V_VWEN6kFH2ZRuP0_GxueFs7c2vEXl4LQLmIDNOY-p5H8inJsaKygscTf5Qoe4iT9EjffVQ4Q1VA1BJ5ajZ6XhCU2jOU9Z_2B_jjAnWzo_rX-dNPvDj7BHsPtNIaf1s57RPXBsCKZSPsN4u4KJQ7q7H1I3fYF5ARAfqOKXD-YVpn-nHk_cb3HxyQVzcRFadGbCwsgS1xfT_0w8Aqw5yKbATKFrT4EPGL55P6UIQEBzPvBGThG4GOaKToLcPncYWqdM-U5r7Aj6MveC5NWt1WztFAg-qajiGAV1Zx536NJ0HRiCcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9d9b52544.mp4?token=ZQe-6MpCJRwdA5O-rqyWiwU0gJgOm3DQAO5Dr-V_VWEN6kFH2ZRuP0_GxueFs7c2vEXl4LQLmIDNOY-p5H8inJsaKygscTf5Qoe4iT9EjffVQ4Q1VA1BJ5ajZ6XhCU2jOU9Z_2B_jjAnWzo_rX-dNPvDj7BHsPtNIaf1s57RPXBsCKZSPsN4u4KJQ7q7H1I3fYF5ARAfqOKXD-YVpn-nHk_cb3HxyQVzcRFadGbCwsgS1xfT_0w8Aqw5yKbATKFrT4EPGL55P6UIQEBzPvBGThG4GOaKToLcPncYWqdM-U5r7Aj6MveC5NWt1WztFAg-qajiGAV1Zx536NJ0HRiCcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گروهی از دختران که با حجاب کامل در حال قدم زدن بودند توسط افراد طالبان با ماشین زیر گرفته شدند!!!
🔴
در افغانستان زنان دیگه اجازه نفس کشیدن هم ندارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/127318" target="_blank">📅 10:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127317">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVEmsWqKccQGfzOVRsCdNiwNEjDLcfQg2tswYmOX25nsIV0cycuQ7R3D0Gn1pW-vE-LNZE5avcDVuPmfdqzaRL7uMpIFWzIK2TVY_xuf_7JIZYvGrXufqQAMIIqhv7csWK8xRbxSlvHUIDyFKFV4UJmwoHECLXTQ9M3w_6uIWn8e6QUk2QZossnBMGIYs9re_nOEyNGAhWhHIhVb6XIUbkaOsX_ImncBMqhPf9hYzDqdHCQiorO28Q2Omk0M9MkyQH8D0s0IrBjrTZYeTZMq7JGFKSxR6DnJJVlTcne_oPPUbQephjH6NWvU-zhGH4dUvzd1eJmiTgN7jdMfqnNvVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکونومیست: آشفتگی‌ای که دونالد ترامپ با شروع جنگ با ایران ایجاد کرد، می‌تواند بیش از آنچه بازارها انتظار دارند، طول بکشد. جهان باید برای قیمت‌های بالاتر انرژی آماده شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127317" target="_blank">📅 10:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127316">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
یدیعوت آحارانوت به نقل از منابع: نتانیاهو گفت به ترامپ اطمینان داده که تمایل او برای توافق با ایران را درک می‌کند، اما اسرائیل نباید قربانی شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/127316" target="_blank">📅 10:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127315">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
وال‌استریت ژورنال به نقل از مقام‌های آمریکایی: واشنگتن در روزهای اخیر عمداً از حمله به زیرساخت‌های ایران خودداری کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/127315" target="_blank">📅 10:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127314">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
جی‌دی ونس، معاون اول رئیس‌جمهور آمریکا در مصاحبه‌ای با شبکه CBS گفت که بنیامین نتانیاهو «قطعاً در چیزی اشتباه کرده است»، که جدیدترین نشانه از فاصله گرفتن آمریکا از اسرائیل به امید حل و فصل جنگ است
🔴
ونس همچنین اذعان کرد که نتانیاهو «به شدت منافع کشورش را دنبال می‌کند - گاهی این به معنای هم‌نظر بودن ماست و گاهی به معنای نبود آن است»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/127314" target="_blank">📅 10:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127313">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
آکسیوس: موضوع دارایی‌های بلوکه‌شده ممکن است در قالب یک توافق محرمانه جانبی حل‌وفصل شده باشد؛ هرچند یک مقام آمریکایی اخیراً این احتمال را رد کرده است.
🔴
به گفته یک مقام آمریکایی و یک منبع از کشورهای میانجی، آمریکا، ایران و قطر در روزهای اخیر درباره سازوکاری گفت‌وگو کرده‌اند که بر اساس آن ایران بتواند برای خرید کالاهای بشردوستانه به بخشی از دارایی‌های مسدودشده خود در قطر دسترسی پیدا کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/127313" target="_blank">📅 10:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127312">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCO4gxGmuMjPz1XFGDE2QgrECvKxGZs1ZIAPemO810QzeLHQ8GrX1-_MwegAMpHz3e_fItfWbhiVWsHv_h2c6TUHFtXQclyoT59u0o5pI6I1KtQpx6Y-ZaEZt5kQzeZ9av4MNbc_vqZIMiLo7RuBZkHHFnclv80OCfmH5-TeZyF8WU5L83CPC3wKpi6H1edOLtzfKIWMmKzfym7qePB-1kIHYtAH7ZzCzK37ID2S6PW-HZcFDtN3M0vPy8eihWxfYq4fd0HtYNZlnBsNghXjSa7RERvHHnzhXZzbwXlezkQSLeYHJ_zvloZc6z-rPZ90EMVTVgZEhSys3zKvikanQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قدیمی ترین کتاب فارسی چاپ شده در لیدن، در سال ۱۶۳۹ که درباره دستور زبان فارسی است
🔴
لَیدن (به هلندی: Leiden) شهری دانشگاهی در استان هلند جنوبی و در نزدیکی لاهه در کشور هلند است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/127312" target="_blank">📅 09:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127311">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
رایزنی پادشاه بحرین و ترامپ درباره تحولات ایران و آمریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127311" target="_blank">📅 09:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127310">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
واشنگتن پست: جنگ ایران رشد اقتصادی جهان را به ضعیف‌ترین سطح خود از زمان کرونا خواهد رساند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127310" target="_blank">📅 09:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127309">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbepVtHBPl9x8R_dRc9RvYMx6y7Xf2Z4y2vmI8VTYXzr0U8J0rVsYpKZKOMaurYfG91oDmx7L6KKydoLnhkpoCKBz1-siyD2ELCCM7Bat5SCJcBu6NuyP0QtYykk3hyEP16khgsOinDQTfP_O-DTseFeC9hLR4LvxDUUpC148DCZvrCFJ7EB4QrNepJJbrT-QrP4GH9tmy0A5n7rVl0SG_VNq6tum6lsqodUUxjhu6lQM_bQ4eekBrM_w8lUq8iVVPkg1d65sAnHm0yGQpeWXlbVTzc0aHwQ8ONH0VE_qkA8OdpdL5l10PatftFx0XweuGQuxE0oGKKSgJKfvYvANw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پس از بریدن سر یک انگلیسی توسط یک مهاجر سودانی در شهر بل‌فاست ایرلند شمالی و همچنین خبر تجاوز ۴مهاجر افغان به یک نوجوان بریتانیایی، شورش‌های گسترده‌ای علیه مهاجران مسلمان در بریتانیا رخ داده و ده‌های خانه و خودروی مهاجران توسط معترضین به آتش کشیده شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/127309" target="_blank">📅 09:40 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

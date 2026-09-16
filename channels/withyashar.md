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
<img src="https://cdn4.telesco.pe/file/oY6b9zbiSkKI7AQwSRFxYk2EnNX6LvnzNADCgDKX3r-fOCfbDoTb7vO5GCz3PNpt4DxVXzq4okc91nlozY1ZdMb2GpwAbzsnOww2PlqzA8qxRUDAvsEGL7Z32Y9VHNPYymLFDdjBCvbD-KWzXU6hRGb9TzWi_ZeMkro_pbUzbbCOYnwU-L3RrRMNfW98InSH_GDgJFDfkCBnh84zW_Ep4qBBxSwd8XJ9mJEAiLKVO-FhmOWrxdu695vqbErkerYvKHxao0RyNo27JqrC5jocAAsnJQqkjCaxutkIe1eGLioLdBgyLMiKapf_opp6hHWm-bDRptXaPLT0737Kp5v_lA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 451K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 14:01:41</div>
<hr>

<div class="tg-post" id="msg-23269">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">زلنسکی: روسیه دو بار تلاش کرد هواپیمای من را هدف قرار دهد
رئیس‌جمهور اوکراین در مصاحبه با CBS گفت پهپادهای روسی در دو نوبت اخیر حریم هوایی مولداوی را نقض کردند؛ هر دو مورد زمانی رخ داد که هواپیمای ریاست‌جمهوری او در حال عبور از منطقه بود. زلنسکی گفت این حوادث ممکن است بخشی از تلاش روسیه برای ایجاد تهدید و ارعاب او و دیگر رهبران خارجی باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/withyashar/23269" target="_blank">📅 12:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23268">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خبرگزاری واپو: دولت ترامپ در حال آماده‌سازی یک فروش تسلیحاتی به ارزش ۲.۸ میلیارد دلار به اسرائیل است که شامل ۴۰,۰۰۰ بمب ۲,۰۰۰ پوندی (۲۰,۰۰۰ بمب MK-84 و ۲۰,۰۰۰ بمب BLU-117) به علاوه ۲۰,۰۰۰ سر جنگی نفوذگر I-2000 خواهد بود. @WarRoom</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/withyashar/23268" target="_blank">📅 12:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23267">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/withyashar/23267" target="_blank">📅 12:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23266">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/withyashar/23266" target="_blank">📅 12:17 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23265">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سی‌ان‌ان:
۱۴ ماهواره جاسوسی روسیه در روزهای پیش از حمله موشکی و پهپادی ایران به پایگاه هوایی پرنس سلطان آمریکا در عربستان سعودی، چندین بار از فراز این پایگاه عبور کرده‌اند. مقام‌های آمریکایی در حال بررسی این احتمال هستند که اطلاعات جمع‌آوری‌شده توسط این ماهواره‌ها در اختیار ایران قرار گرفته و به تهران در شناسایی دقیق اهداف و اجرای حمله کمک کرده باشد. این موضوع در حالی مطرح شده که حملات ایران به مواضع آمریکا در منطقه، خسارات و تلفات قابل‌توجهی به نیروهای آمریکایی وارد کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/withyashar/23265" target="_blank">📅 12:16 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23264">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/withyashar/23264" target="_blank">📅 12:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23263">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/withyashar/23263" target="_blank">📅 12:06 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23262">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/withyashar/23262" target="_blank">📅 12:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23261">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تازه‌ترین گزارش‌ها حاکی از آن است که در شهرهای سنندج، کرمانشاه، سقز، مهاباد، پاوه، بوکان، مریوان، اشنویه و دیواندره، بسیاری از مغازه‌ها و واحدهای صنفی تعطیل هستند و کسبه محلی به مشارکت در این اعتصاب  سنگین ادامه می‌دهند. @WarRoom</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/withyashar/23261" target="_blank">📅 12:00 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23260">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a55785df5e.mp4?token=XqSU0v7415ZLbmAICYB0IXdVCmgMxYu2FV-lwDf-3ecGL3SU1EzgyVGnbc4_fhxh8WuiDRONhXEiN_LY0XwnvTFhkr2S3yGnNlNlaei2QzFrRxUSxBiObt8LHAnnRZLKV3SXPadjCtMR5pDalWjRUB0G_gS7nmQPhcAJNE4zmxFLnBGCpVvXcvJT7WvE9fT9LGd3W49vTaXas1EBlRBntYVt83O5MOrRJP0IbY2OsUYVmZ7qlaUWcU0pGLCIPjG8r0HrjEjod3O7mwplPLY3FC_H_XaieqJIAuLbAe5Lu_kq5T77JcHioaUHgIllNoQBEn2OS1tBwa4UknHt-karhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a55785df5e.mp4?token=XqSU0v7415ZLbmAICYB0IXdVCmgMxYu2FV-lwDf-3ecGL3SU1EzgyVGnbc4_fhxh8WuiDRONhXEiN_LY0XwnvTFhkr2S3yGnNlNlaei2QzFrRxUSxBiObt8LHAnnRZLKV3SXPadjCtMR5pDalWjRUB0G_gS7nmQPhcAJNE4zmxFLnBGCpVvXcvJT7WvE9fT9LGd3W49vTaXas1EBlRBntYVt83O5MOrRJP0IbY2OsUYVmZ7qlaUWcU0pGLCIPjG8r0HrjEjod3O7mwplPLY3FC_H_XaieqJIAuLbAe5Lu_kq5T77JcHioaUHgIllNoQBEn2OS1tBwa4UknHt-karhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تازه‌ترین گزارش‌ها حاکی از آن است که در شهرهای سنندج، کرمانشاه، سقز، مهاباد، پاوه، بوکان، مریوان، اشنویه و دیواندره، بسیاری از مغازه‌ها و واحدهای صنفی تعطیل هستند و کسبه محلی به مشارکت در این اعتصاب  سنگین ادامه می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/withyashar/23260" target="_blank">📅 11:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23259">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/withyashar/23259" target="_blank">📅 11:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23258">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/withyashar/23258" target="_blank">📅 11:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23257">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏اعتصاب عمومی در سنندج و شماری دیگر از شهرهای استان کردستان ایران آغاز شده است. @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/23257" target="_blank">📅 11:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23256">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5da33205e.mp4?token=g6O8HvkMOX2gO2coZotPiY_VGJ5YTFhc-_Zuo4v5XZIOLQF4J584l1nFG0yH6vNQsbaplP5qh1MU4k0g-6tvg_LSutZaifHXJYphH9-jfJURLfkhs_mY85Iw5Me-E_lxAoqINn3_WhEfgnVPbnwczSRDpcmv8Ewq3htdHT55UGp8UchzWByoYLCw_-mS87BzYAeHXAbPy7AZYwqP_s0ccDo7F8DlH71Fio0NSjA6LB22tzSZcRKbcFaw0bA8uWe8s7O3SiqJLCa-j_XoM7y2PR9jYCdyZRxkugxqb9TW648YWAik-7AIKOIWDVTM7zyjzJv75zfUAnzphGnwK31SjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5da33205e.mp4?token=g6O8HvkMOX2gO2coZotPiY_VGJ5YTFhc-_Zuo4v5XZIOLQF4J584l1nFG0yH6vNQsbaplP5qh1MU4k0g-6tvg_LSutZaifHXJYphH9-jfJURLfkhs_mY85Iw5Me-E_lxAoqINn3_WhEfgnVPbnwczSRDpcmv8Ewq3htdHT55UGp8UchzWByoYLCw_-mS87BzYAeHXAbPy7AZYwqP_s0ccDo7F8DlH71Fio0NSjA6LB22tzSZcRKbcFaw0bA8uWe8s7O3SiqJLCa-j_XoM7y2PR9jYCdyZRxkugxqb9TW648YWAik-7AIKOIWDVTM7zyjzJv75zfUAnzphGnwK31SjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏اعتصاب عمومی در سنندج و شماری دیگر از شهرهای استان کردستان ایران آغاز شده است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/withyashar/23256" target="_blank">📅 11:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23255">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : هیچ هدف‌گیری‌ای داخل شهر مکه مکرمه صورت نگرفته است. دو پایگاه هوایی در نزدیکی مکه قرار دارند: پایگاه هوایی ملک فهد در طائف و پایگاه هوایی ملک عبدالله در جده. هواپیماهای جنگی سعودی از این پایگاه‌ها برای انجام عملیات و بمباران در یمن پرواز…</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/withyashar/23255" target="_blank">📅 11:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23254">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رئیس‌جمهور ترامپ: راستش را بخواهید، عمویم احتمالاً بهترینِ تمام دوران بود؛ او ۴۱ یا ۴۲ سال استاد دانشگاه ام‌آی‌تی (MIT) بود و به عنوان یکی از درخشان‌ترین افراد شناخته می‌شد. بنابراین، اگر به «نظریه وراثت» (یا قدرت ژنتیکی) اعتقاد داشته باشید، من هم از چنین…</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/23254" target="_blank">📅 11:06 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23253">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/withyashar/23253" target="_blank">📅 11:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23251">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QORi6FVSXr5Bj9twe-cn8cdGDxZJeJCKIroQiCba9RCVwbQvTY4OWLh8NhfIl9lbYkspm7BkBW0PEFwsNiRqTuiaTYuPeUKf3jlTVIqCmHhvzbVlgKMh5M_zmNYGyoaI38bwDEWo_tMUmxe21zQa2A_wlzG-FKXNB3_cpksXWoGVLxeV5E912lcxR6uj9Yrat69XkzAQHeUkpapv1DdamoZYSKaHveEhfjkYdA4X4srQwmRhmNmaZWtftJV96IHhitANf3dwS9Wcbx9K1-EOPEAsebLLkGudhyDGUniMN5pUmcNuf8d7j20GE7fzEg6kfyV1JDBEXcl8ZYoCY03v2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e27cc230e.mp4?token=PV9namPFhxkTYXRAk9ZE_FINGzILoea8JNvloYbJ-8rjBU5iZe15Y0W1Tr0H42VZBHy6hURa_hm-hgOatUVFxfEJIncwBK3S0gkwcilsrn8eVXp7lhUmSrCkEdp_v6qFMlukG5bB-2pBF2OCpc70Q01saprgz1Oc5Pz-86068SrOE-qwtV6PYo9ZjbU7t_n25Gpgy32j02OW2weFBMg41O1nEOFlBDhSp-V1bxRwIXiVCB-fqVstI9NmDLSj_V_9rTXFsUtQv63caavR_8N3le-K9XO-c_PV2ywH4b3QBR2SVEIl8-8hxnpLC9BOPMhhemWIKPVWmKxgFE_yR5f8qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e27cc230e.mp4?token=PV9namPFhxkTYXRAk9ZE_FINGzILoea8JNvloYbJ-8rjBU5iZe15Y0W1Tr0H42VZBHy6hURa_hm-hgOatUVFxfEJIncwBK3S0gkwcilsrn8eVXp7lhUmSrCkEdp_v6qFMlukG5bB-2pBF2OCpc70Q01saprgz1Oc5Pz-86068SrOE-qwtV6PYo9ZjbU7t_n25Gpgy32j02OW2weFBMg41O1nEOFlBDhSp-V1bxRwIXiVCB-fqVstI9NmDLSj_V_9rTXFsUtQv63caavR_8N3le-K9XO-c_PV2ywH4b3QBR2SVEIl8-8hxnpLC9BOPMhhemWIKPVWmKxgFE_yR5f8qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : این ویدیو قدیمی و مربوط به سال ۲۰۲۵ است؛ زمانی که پدافند عربستان موشکی را که از یمن به سمت اسرائیل در حرکت بود، سرنگون کرد. نکته خنده دار این اصلا مکه نیست، بلکه مدینه است!!!! خاک بر سر ادمین های زرد بی سواد
😂
@WarRoom</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/23251" target="_blank">📅 10:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23250">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9Oef2Z5YbYtanVnnJnmmuA0NjOPh-KQ3Ah5Bu79j4jrjiwrVqSg7T2SgTTLF6axODe5v5hkJDR2Gac8Jx6VKeGiBOBLQLtlmsDSdQb1SOKY6vWbjNTLC-J_TZBaJSU4amg4bKXGKxT_9Mw2kLZ0pdgPvzZQck02gvc52DBMWh5AKovAujyUTXfzQ5zoRQcBTryh3t54NHNbpFbhpH1Gx4i1K7yC75vsOdu2E8iJ4N7WDTEACNIdaeTSMrKk0TdjxPIXM5JeI4dgkUz91gp_Eqah5NpfQDHMD6LErslgrnCStHJj7jYThwpkJmxLA33MBUUW3A9o43D3FJ16uQHDmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نظرسنجی جدید کانال ۱۴ اسرائیل: لیکود به رهبری بنیامین نتانیاهو با ۳۰ کرسی همچنان بزرگ‌ترین حزب است، اما یک کرسی کاهش داشته؛ حزب «یاشار» به رهبری گادی آیزنکوت نیز از ۲۲ به ۲۱ کرسی رسیده است. شاس ۱۰ کرسی، دموکرات‌ها ۹، صهیونیسم مذهبی-زهوت و عوتسما یهودیت هرکدام ۸ کرسی دارند. حزب نفتالی بنت و یهودیت متحد تورات هرکدام به ۸ کرسی رسیده‌اند و اسرائیل بیتنو از ۷ به ۶ کرسی کاهش یافته است. در میان احزاب عرب، حدش-تعال-بلد از ۶ به ۷ و رعام از ۶ به ۵ کرسی رسیده‌اند؛ مجموع احزاب عرب ۱۲ کرسی باقی مانده است. در سطح بلوک‌ها نیز راست ۶۴، چپ ۴۴ و احزاب عرب ۱۲ کرسی دارند و موازنه نسبت به هفته گذشته تغییری نکرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23250" target="_blank">📅 05:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23249">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">وال‌استریت ژورنال، به نقل از مقام‌های آمریکایی و منطقه‌ای مطلع از موضوع: نیروهای آمریکایی برای مقابله با حمله موشکی بالستیک ایران به پایگاه‌های آمریکا در اردن که هفته گذشته با حدود ۲۰ موشک بالستیک انجام شد،
۶۰ تا ۷۰ رهگیر MIM-104 پاتریوت و بیش از ۱۲ رهگیر تاد
شلیک کردند. مقام‌ها همچنین به وال‌استریت ژورنال تأیید کردند که ایران در این حمله از
مهمات خوشه‌ای
استفاده کرده و برخی موشک‌های بالستیک از سامانه‌های دفاع هوایی عبور کرده و به هواپیماهای نظامی، از جمله جنگنده‌ها، در پایگاه هوایی موفق‌السلطی اصابت کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/23249" target="_blank">📅 05:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23248">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کانال ۱۴ اسرائیل : ترکیه به یک شریان حیاتی مهم برای ایران تبدیل شده و به تهران کمک می‌کند از فروپاشی اقتصادی جلوگیری کند؛ از جمله از طریق ارزهای دیجیتال و مسیرهای تجاری زمینی و دریایی. بر اساس اطلاعات منابع اطلاعاتی، ایران همچنین ده‌ها میلیون دلار را از طریق کریدور ترکیه به حماس در ترکیه منتقل کرده است؛ در حالی که تهران برای حمایت از نیروی نیابتی خود تلاش می‌کند.
@WarRoom
🚨
🚨
🚨
🚨
مارک لوین با بازنشر این خبر : اردوغان در حال تأمین مالی رژیم ایران و حماس است.</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/23248" target="_blank">📅 04:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23247">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">معاون رئیس‌جمهور، جی‌دی ونس، درباره ایران: «ببینید، رئیس‌جمهور ترامپ روی کار آمد و بله، او می‌خواست آمریکا را از درگیری‌ها و گرفتارشدن در مناقشات خارجی دور نگه دارد. اما او همچنین گفت که متعهد است اجازه ندهد ایران به سلاح هسته‌ای دست پیدا کند. به نظر من، اینکه…</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/23247" target="_blank">📅 04:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23246">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/660d9d9e22.mp4?token=JHkuFA_-x6342JzrPcGfUzHH_9wvc93T-Asma1bDAnzQkA2S83BwMqHTUvERyePiabncQkvySgZYk_9qrmyj4OajLD8vGQz6duShWF-MKPi0x0r35Gbgmm-1LcWtGt_wqCGFKSCpknF5C3PPILJnfZ7PwjYxYxu6EQXpCZKGtcALwhTFZjin_b45t4PsZ8a7U6VEg4SMVMLCcCoyfuubipP_eVZTy9w_VCQCX29HcAJJdhr00TXHdBd_nZp4Yskpt7uMC37e2SA3LaIyVMP1vCCOXmbvmmc42uUGrrnBa_h0RS4-UTTAU-Kij5QhesHGuCv6O2tIrobLIEV1N4SWLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/660d9d9e22.mp4?token=JHkuFA_-x6342JzrPcGfUzHH_9wvc93T-Asma1bDAnzQkA2S83BwMqHTUvERyePiabncQkvySgZYk_9qrmyj4OajLD8vGQz6duShWF-MKPi0x0r35Gbgmm-1LcWtGt_wqCGFKSCpknF5C3PPILJnfZ7PwjYxYxu6EQXpCZKGtcALwhTFZjin_b45t4PsZ8a7U6VEg4SMVMLCcCoyfuubipP_eVZTy9w_VCQCX29HcAJJdhr00TXHdBd_nZp4Yskpt7uMC37e2SA3LaIyVMP1vCCOXmbvmmc42uUGrrnBa_h0RS4-UTTAU-Kij5QhesHGuCv6O2tIrobLIEV1N4SWLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس‌جمهور، جی‌دی ونس، درباره ایران: «ببینید، رئیس‌جمهور ترامپ روی کار آمد و بله، او می‌خواست آمریکا را از درگیری‌ها و گرفتارشدن در مناقشات خارجی دور نگه دارد. اما او همچنین گفت که متعهد است اجازه ندهد ایران به سلاح هسته‌ای دست پیدا کند. به نظر من، اینکه بخواهیم آمریکا را از درگیری‌های خارجی دور نگه داریم،
به این معنا نیست که هرگز نمی‌توان از نیروی نظامی برای تحقق اهداف مردم آمریکا استفاده کرد
.»
@WarRoom</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/23246" target="_blank">📅 04:14 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23245">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h87acgB6punA8MtcPXBo5NwhwV6kfNt1RVEiTMLFIGvWkargCnbNTS1nn3HdItsxRJTX-JK5f9ycEv_fRBO6BMM71fJzoPyE97nrlnqS_XMS-tA6j_YNt7BdQjZ4ATUW5zgS0iQMgxHoCzxe_TTF9Z3tghn3NNqlmMpoxbwunbitCwkLUIKLX8afqrYkSbp9BgE-Tn0Fw0ywMGX7cciINoNYYaLVJuFjPqJ2CzRw0dsUL9yru-mlg69YIPJ6SBAYN0obVRBUJus737je5ZgbfNvI4uEH1fw92G9jY4TaBSOdtMXh0RvTjLvHsED9DLIY1Psm7PfgZXra815XXkYF-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفارت آمریکا
در ریاض سطح هشدار سفر به عربستان سعودی را به سطح ۳، یعنی «در سفر تجدیدنظر کنید»، افزایش داده است. در این هشدار، به خطرات ناشی از حملات پهپادی و موشکی ایران علیه منافع آمریکا، درگیری‌های مسلحانه و تروریسم اشاره شده است. این هشدار همچنین درباره احتمال ممنوعیت خروج از عربستان و خطرات مرتبط با قوانین سعودی در زمینه فعالیت در شبکه‌های اجتماعی هشدار می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/withyashar/23245" target="_blank">📅 04:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23240">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lp9Nu-fnlj40NXG8jyqLC2mDG3ekAIRFm0RQpLbSIwwT6omb-BD3XaLc_OLpZbQtEH60a1jKOsjQmWSP-zhDD-w9DQSuK_ETFQpqFCUAvsFYmjl--M0AgRd9jEDrQR6LVAhX9tGkx-nDvDov_sd3anIbiu1trtrfJM3iJi4IO1eYJd8wO-zCyNBUt3P4nAXUtlJ_pWAefklWCoCuqBhKGuSm7oR6DxjLsSkUu5tR15UTKF1RZi0rMUxFBHSHLBucmG9AsLhMO3XomW2HNue8Lm9gejABuQtJy-58tuOddGL6SW23geRBw8ysbeHjGh6Y8qbH_M_wplZLrt62dXpFqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EPqf3b1pNdYV529A3gsEUbLnapsga2mxmSygBJPbg_U131E2zPK46JLdVJozBKi520YPVm19sWYDUMAqTFUFzfBW6Y57zdDaNT8z-ISzQbZOik6yoR55xn5TahviTFyykm5fY7aXrhDI9vDqrc2f8rapTnj5svlmD4EGUAG5q3jF86JqBXi3uLdHW5z6vxqiLNgrnZPGGcM4jcHS45Cqn0Q_mUztkBm_KWPSVNb8TorN4MYb3uSQlzpgFbu4szFsV4pdsFii9rBmTi-hbf_V83wEohrzDxGlMM7TpubQdPv4R-N5G0ah4uiaIx6ekCOF8oezG2_ksm-T9mwFRgYrkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TfQdVldiYXxHqtFH-YUbK2jBXjypBSVQWWTbGcJYvkaXdMBC0iNAk7VWIj7kdpCYLhUSRcU2LXgMqSVUkVS7dHuTb2wsSx3mavv80T4gwBQQeMQfWnc8_E87eI75jf10rzMkr1EtVLlLjw9xiCxF0DRHccMo6jT7XNtiFbFCQDtlRkGwXDKBhvcTF-STUlRkKAuNruO03Uls2QOpgtaA938Oq1VyjfFgQUqDiMmhlBr7weX8fA8vKwLK7bTugWin2fUa2Uw3O8cErkH9s9gw4RAJodbpW-QO0iAF02IDBz1NZ8laWdDnn8QOZGybOxex52b49M8dw7S41_IA8zZfSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P8-LrXAktnfFGAJmJxgM7Oe0XaPeJiqsAa0SU38BF2QI2MXuBNwnA0xtmxThCiBySLhjXPdkkNW8ODEC3AEDmbSTfpUdzejFrCcdDB1lnQbwvuiJd2AJLn45Ae2qpDvbwGnXzkf8SiAUEcYlMjZuNCsi0hDf1-NYecyDPvkhCRNks4FzUdGKB8U5I7YnFN0qFbORRKs6wfs41wz6U-aAs1iIs_99GBdBSDH4AaJ3aJ9UrL4DVsOmU_V0-gsIWoFS0wHKWkx_si7AVVsA5H2B6mHrEsCNZhmtrQRhoWt5JRqFHCo1iNXqnJJ2WyLVTKMlEGP0foEIIVRkDxGBHd9B7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p31TSnpvTrE-umSWdDgSZ2xEoqo7SF1Sd8MqirpNHLBDZhJRQMpx1mFbcuh5RLG10ISggAyinJHBTen5cqXCKX0chglLV4YYZxHolkv9Mv0gBDb3vxQ8XUxqA6JRnJHI6oK6Av6WhUbyMtaIUOiCuDIXVk70JBZC_83P3OxMe9AbAGjqKEWpAKQyr1Fg8uDiro7pPs55Qxye0gs2dKaW7o07NDIeFwzF6-wKo3oYLndJ2PtvxsinHsH98Cv2UmD2o2kxd-hAf4A3HVGCUbJqJw8YDfKa4jphDo-OO7n1mEFWXgGXZfcC7EADqoipkqH2Vw3CbZ_8X2C4EiVBMAxiTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر جدید، خسارت گسترده حملات موشکی و پهپادی ایران به مواضع آمریکا در خاورمیانه را نشان می‌دهد:
تصاویر اختصاصی که توسط چند نظامی آمریکایی و به‌صورت ناشناس برایمان ارسال شده، آسیب شدید به پایگاه‌های آمریکا در
عربستان و کویت
را نشان می‌دهد. در یکی از تصاویر، یک فروند
هواپیمای آواکس E-3 Sentry
در پایگاه هوایی پرنس سلطان عربستان دیده می‌شود که بخش پشتی و دم آن بر اثر اصابت منهدم شده است. تصاویر دیگری نیز ساختمان‌ها، خودروها و تأسیسات آسیب‌دیده در کمپ بوریحینگ و کمپ عریفجان کویت را نشان می‌دهد. همزمان، گزارش جدید بازرس کل وزارت دفاع آمریکا از
تا ۳.۷ میلیارد دلار خسارت تجهیزات، شامل نزدیک به ۶۰ فروند هواپیما
خبر داده و تأیید کرده که حملات ایران پایگاه‌های آمریکا در سراسر خاورمیانه را هدف قرار داده است
@WarRoom</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/23240" target="_blank">📅 03:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23239">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bada91535.mp4?token=JkPCa1tS9ZHjubyIa7xR_vCmef3tg6pcLxG_oGsIL3-pl3_KfecAMn6rQoKabODO7x9BMqSe5Jb85Ghi5slpkTaUb0O1JmoN_VxCOdrCl6rvODIEz2L_2S7bNOST_xlBAM20DaxRA-dpf-0hOCil7DZyGzrYCvgxrqweDqYOnabIcDSlaFVldUZFShPM9Y1bR_r2C4UtEi6g-G2sg3H1YyHaVPkdo4FtQwBM_qisCOcRSHXVAJbl1h1EIue8YAV_FvPuhc3pXwbbm96hi87zYXnDoOO4lymeCSqu1c8PpFoqJIkxDlbXXRUu61zMZapOheO4CMYs1BsxXv2V1OKHL4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bada91535.mp4?token=JkPCa1tS9ZHjubyIa7xR_vCmef3tg6pcLxG_oGsIL3-pl3_KfecAMn6rQoKabODO7x9BMqSe5Jb85Ghi5slpkTaUb0O1JmoN_VxCOdrCl6rvODIEz2L_2S7bNOST_xlBAM20DaxRA-dpf-0hOCil7DZyGzrYCvgxrqweDqYOnabIcDSlaFVldUZFShPM9Y1bR_r2C4UtEi6g-G2sg3H1YyHaVPkdo4FtQwBM_qisCOcRSHXVAJbl1h1EIue8YAV_FvPuhc3pXwbbm96hi87zYXnDoOO4lymeCSqu1c8PpFoqJIkxDlbXXRUu61zMZapOheO4CMYs1BsxXv2V1OKHL4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا درباره ایران:
«ما شاهد شلیک ایرانی‌ها به کشتی‌های تجاری حتی در جریان مذاکرات صلح بوده‌ایم. فکر می‌کنم رئیس‌جمهور ترامپ در اینجا کار مسئولانه‌ای انجام داده و تلاش کرده اطمینان حاصل کند که با وجود اقدامات ایران، جریان نفت و گاز در بازارهای انرژی جهان ادامه داشته باشد. اگر آمریکا به خاورمیانه بگوید “خودتان از پس خودتان بربیایید”، تا زمانی که ایران به شلیک به کشتی‌ها ادامه دهد، نتیجه آن ناگزیر یک
بحران جهانی انرژی
خواهد بود. رئیس‌جمهور ترامپ مسیر مسئولانه را در پیش گرفته است. او ضمن حفاظت از منافع و دارایی‌های آمریکا در منطقه، اطمینان حاصل می‌کند که بازارهای انرژی جهان همچنان به عرضه نفت و گاز دسترسی داشته باشند.»
@WarRoom</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/23239" target="_blank">📅 03:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23238">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">رویترز: بسنت می‌گوید آمریکا با چین درباره فشار بر کشورهایی که به ایران کمک می‌کنند مذاکره کرده است. وزیر خزانه‌داری آمریکا گفت واشنگتن در گفت‌وگوهای خصوصی با چین درباره برخورد با کشورهایی که از ایران حمایت می‌کنند پیشرفت داشته و قرار است آخر هفته با هه لیفنگ، معاون نخست‌وزیر چین، دیدار کند؛ این موضوع احتمالاً در دیدار آینده ترامپ و شی جین‌پینگ نیز مطرح خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/23238" target="_blank">📅 03:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23237">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">For Terminators Only
@WarRoom</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/23237" target="_blank">📅 03:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23236">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/23236" target="_blank">📅 02:59 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23235">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/23235" target="_blank">📅 02:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23234">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAli</strong></div>
<div class="tg-text">سلام داداش یه چیز میخوام بگم که البته به من مربوط نیست ولی چون واقعا دوست دارم باهات حال میکنم میگم گفتن این خاطراتت به نظرم من جالب نیست به چند دلیل اول یه قشری که ندارن دیگه باهات همزادپنداری نخواهند کرد دوم که من نمیدونم و قضاوت نمیکنم ولی به ظاهر چون بیشتر ما شناخت نداریم ازت به دور از واقعیات میرسه و سوم بردار من از قدیم گفتن درخت هر چه …..و به نظر من با این مسائل داری از هدف اصلیت دور میشی چون ما تورو به عنوان یک لیدر میبینیم امیدوار متوجه حرفام شد باشی و ناراحت نشی
🙏
🙏</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/23234" target="_blank">📅 02:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23233">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تحولات بسیار قابل‌توجهی در خاورمیانه در حال وقوع است و احتمال یک تشدید بزرگ و جدید درگیری‌ها مطرح شده است. در طول امروز، جنگنده‌های اسرائیلی در چند نوبت وارد حریم هوایی ایران شدند، بدون آنکه حمله هوایی انجام دهند؛ اما این پروازها موجب فعال‌شدن پدافند هوایی…</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/23233" target="_blank">📅 02:16 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23232">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/23232" target="_blank">📅 01:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23231">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/withyashar/23231" target="_blank">📅 01:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23230">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/23230" target="_blank">📅 01:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23229">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/23229" target="_blank">📅 01:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23228">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/23228" target="_blank">📅 01:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23227">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vK69tGz116Dbwy9MjnRqZ3yswpQAsouTJzQl59vGc8GVwUTe8-IHthBvmvKANBBo06hPbLnyE7INxag3pEWEh68QtotOP63NYqrKJjg4HH5QLEHS9MbcV6jCziT_LNfI673tG60DH28s4meqXg0IbgjgU5VrJcUG_5200YrrSc_VWhcj8C9b-76afRtzsS2tr74H-MHJbYNFjXVr69KsJKkS2-Tc-uFooWLjIWWAcuAJalf7YZoZgl8UP0NKk3nopBcmqL9xGPkV6yH5XJqX6CdY5g8TVn-cZpD_PzEcBNEO325DATwLUkw8DEPsAlXgUcJbIVKssVY8dW9BIH-qSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر نوری، بازیگر چند روز بعد از انجام مصاحبه‌ای و اعلام پولدار بودن ، در پی یک حادثه رانندگی در یکی از بیمارستان‌های تهران بستری شد.
طبق آخرین اطلاعات منتشرشده از وضعیت پزشکی، سطح هوشیاری او پایین است ولی در مقایسه با ساعات ابتدایی پس از حادثه افزایش یافته و شرایط او از این نظر بهتر شده است.
با این حال، روند درمان هنوز به پایان نرسیده و پزشکان با توجه به آسیب‌های ناشی از تصادف، انجام یک عمل جراحی را برای او در نظر گرفته‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/23227" target="_blank">📅 01:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23226">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/viXOwRpo22G3Jqen_MBRq2-OjsHa9Ko_qTvRx4BZKUhf7Q4w6KHoOpNzUWOVe5GZA4X7_kA1sqqhkfkdFBBHuV3bBmcOJKhcpJh46LsnPwCAqLC-3WOVQPv71voo-5y1n5RiYMu4tX3xsc0XBlNZ3LuGNvREwDM9BPgB6klfSD7xjDmEkohqdooDAB8bWUEX9_facuhoqHcRXxR-QmI8CoW1klFuGqwNbQID73ZuBboEK52FTN6YmzUx7yqtKMT-dk0UWMfX2qSpP_VFVo_rorZ6qJ_Nlpz6mJRvHa8BD3Kmh9UAbPqRAvSoLPHC5aMAd0HoRHw43rsxIU7tTsll_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحولات بسیار قابل‌توجهی در خاورمیانه در حال وقوع است و احتمال یک تشدید بزرگ و جدید درگیری‌ها مطرح شده است.
در طول امروز، جنگنده‌های اسرائیلی در چند نوبت وارد حریم هوایی ایران شدند، بدون آنکه حمله هوایی انجام دهند؛ اما این پروازها موجب فعال‌شدن پدافند هوایی ایران و مهم‌تر از آن،
تخلیه و اعلام وضعیت آماده‌باش در برخی پایگاه‌های سپاه پاسداران
شده است. از سوی دیگر، هفته گذشته یک نشست سطح‌بالای نظامی در آلمان به ابتکار
دریاسالار برد کوپر، فرمانده سنتکام
برگزار شد که فرماندهان نظامی اسرائیل، آمریکا و کشورهای عربی منطقه از جمله عربستان، امارات، بحرین، کویت، قطر، اردن و مصر در آن حضور داشتند. این نشست به‌صورت محرمانه برگزار شد و به گفته آکسیوس درباره
جنگ با ایران و افزایش تنش‌های منطقه‌ای
بود. با این حال، هنوز مشخص نیست این تحولات مقدمه یک عملیات جدید است و
نشانه قطعی و مستقیمی از قریب‌الوقوع بودن حمله جدید وجود ندارد
.
@WarRoom</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/withyashar/23226" target="_blank">📅 01:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23225">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohOupK-bFOG1QeCxe0oAnwrtWCv3UL9tdEOW5envstnrffFGRV0o2x8gyzMpUl-or4K1aCaVkZyLVaAzAjcOemrZSGJg11WooJ0mDltp6i9UBp52LyDIrbPrMVLQ_fBRTYCHng8p_4pKWEWREQ-1zzuhaWOSGIBntRwDaeL7uxSrHLcKMzl3OwKHLtkVfuar2CPmOsD-bZNIxUEtrGMjvqVgZ3NOdr2v203yIZDsTUrOzgPrigUstSlYI48YIg3bG2-bQSyg9cAlWTun7ybZb3knfLHrAH46mEOl98s2VQNsCqDh9-CM9urZCRI1WsNwhPxi2Es9a4ZhlHfV5tjU7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادر ابی رئیسی                  فوت کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/23225" target="_blank">📅 01:09 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23224">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGit_uftzW1O68Sj_JLnxI5YmvdWZMir9ZVzx9mdVPsChuDaFNMcOOh2os9Gd2h3LKrOyaO13asV34K382JZvD5h5rnH8YOBL1-j8ieb7DMLcjZ_17Ltl4kiPM9ohOEnkSkCvexQOYFni3e4YHNDYpPedG5pjbM12fa9No0osxexE-geE-UO06mjQdP_-kjW0K841G3ZxwHPO-hVzYcjqxosk1kzDLecWI8XXFFnWCF8GFCKsSGLNYm-JNV2pt27VEBgjITgav0y0mvq-ZIf10LYMgFZ48BptSKUFvrIdW3Vy97a_S9FUHvsGvoAvd6Bo3K6FXiYhq_v48XU28YIng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلس نمایندگان آمریکا با رأی ۲۳۲ به ۱۴۷ و ۴۷ رأی «حاضر»، طرحی برای آغاز روند استیضاح دونالد ترامپ را کنار گذاشت؛ بنابراین این طرح پیش از رسیدن به رأی‌گیری درباره خودِ استیضاح، عملاً متوقف شد.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/23224" target="_blank">📅 01:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23223">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">جی‌دی ونس در گفت‌وگو با نیویورک‌پست:
درگیری با ایران طی چند ماه آینده وارد «مرحله‌ای کاملاً متفاوت» خواهد شد و دولت ترامپ انتظار دارد این درگیری پس از انتخابات میان‌دوره‌ای آمریکا وارد مرحله پایانی شود. عملیات تهاجمی آمریکا کاهش یافته، اما واشنگتن همچنان روی جلوگیری از بازسازی توانمندی‌های ایران تمرکز دارد؛ توان موشکی و پهپادی ایران و همچنین برنامه هسته‌ای این کشور به‌شدت تضعیف شده است. در
تنگه هرمز
، ایران همچنان حملات محدودی علیه کشتیرانی تجاری انجام می‌دهد و تردد کشتی‌ها بسیار پایین‌تر از سطح عادی است؛ نیروهای آمریکایی عملیات
مین‌روبی تنگه
را انجام داده‌اند و آمریکا به‌صورت محرمانه نفتکش‌ها را از مسیرهای دریایی عبور می‌دهد. همزمان واشنگتن به هدف قرار دادن نفتکش‌های مرتبط با ایران و اعمال تحریم علیه نهادهای حامی حکومت ادامه می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23223" target="_blank">📅 00:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23222">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23222" target="_blank">📅 00:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23221">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">@WarRoom
سامورائی</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23221" target="_blank">📅 00:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23220">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گزارش انفجار اربیل عراق
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23220" target="_blank">📅 00:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23219">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گزارش صدای انفجار قشم ۱۲:۰۷
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23219" target="_blank">📅 00:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23218">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سی‌بی‌اس نیوز به نقل از العربی الجدید :
مصر پیشنهاد حوثی‌ها برای
مذاکرات مستقیم درباره هماهنگی کشتیرانی در دریای سرخ و تنگه باب‌المندب
را رد کرده است. به گزارش CBS، این پیشنهاد از سوی یک مقام حوثی به اتاق بین‌المللی کشتیرانی در لندن ارائه شده و سپس با طرف مصری مطرح شده است. قاهره نگران است که ورود به چنین چارچوبی به حوثی‌ها یا هر طرف دیگری امکان دهد
ادعای اختیار یا حاکمیت بر تنگه باب‌المندب
داشته باشند و به‌نوعی جایگاه آنها به‌عنوان طرف دارای اختیار بر این آبراه به رسمیت شناخته شود.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23218" target="_blank">📅 00:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23217">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نویسنده کیهان و کارشناس صداوسیما : شروط جدید ایران برای آغاز مذاکرات؛ رفع حصر دریایی، خروج اسرائیل از غزه و توقف عملیات در کرانه باختری است.
پرونده هسته‌ای هم از دستور کار خارج شده؛ «تحت هیچ شرایطی حاضر به مذاکره درباره موضوع هسته‌ای نیستیم».
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23217" target="_blank">📅 23:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23216">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اتاق جنگ با یاشار :
گزارش‌ها از درباره فروپاشی سریع نیروهای دولت یمن نشان می‌دهد یکی از عوامل مهم، اختلاف شدید میان شمار نیروهای ثبت‌شده و نیروهای واقعی در برخی یگان‌ها بوده است.
بر اساس گزارش‌ها ، در برخی واحدهای نیروهای تحت حمایت عربستان، تا حدود
۸۰ درصد از نیروهای ثبت‌شده «سربازان خیالی»
بوده‌اند؛ یعنی افرادی که در فهرست حقوق و سازمان نیروها قرار داشتند اما در عمل نیروی نظامی حاضر در میدان نبودند. در نتیجه، نیروی واقعی برخی یگان‌ها تنها حدود
۲۰ درصدِ تعداد اعلام‌شده
بوده است. این سازوکار به فرماندهان اجازه می‌داد حقوق نیروهای ثبت‌شده را دریافت کنند و به جیب بزنند،  عربستان از سال‌های گذشته برای پرداخت حقوق نیروهای یمنی تحت حمایت خود هزینه‌های قابل‌توجهی اختصاص داده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23216" target="_blank">📅 23:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23215">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رسانه های عبری : ساعتی پیش، فرمانده یک گردان از کتائب القسام شاخه نظامی حماس در رفح شهری در جنوب نوار غزه و در مجاورت مرز مصر، ترور شده است. @WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23215" target="_blank">📅 23:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23214">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">زلنسکی:
روسیه حملات به زیرساخت‌های انرژی و حیاتی اوکراین را متوقف نکرده و ما نیز به این حملات پاسخ می‌دهیم. رئیس‌جمهور اوکراین همچنین از
حمله به پالایشگاه نفت سیزران در استان سامارا روسیه
و چند تأسیسات مرتبط با تولید پهپاد خبر داد.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23214" target="_blank">📅 23:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23213">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c693031947.mp4?token=rxcJYgO1qLEX2lYogPZDkqSAlPd5mPgruFSShJMRmhsJa0t5abGb8Ju1FvOXOOFq8qoWsQzOa1SZUP5297fTuvC8VheKKnl4fmUkQrx9Zf2VKjdNMymTIPt-bItZfeIJ49gKjWRXlhqB6QJg7WCMeNI0SYmspkMfyANeqPFkjOA52cSZf6Y-avzZobQaX3GgBY8_6MwbqPkTodzmcfx1GNzJr4Lhnpn2Sh_2P489bg5sFJS8hVvDVRaOlpHtliZ_0NomK__FMJDtRgnVkOeD2xBOAWTBspFHY9WPYs1X3tiWWyRTSDGM_2I4vtTdgUkV5TVvjiVfhBM-LPfnQ4wFCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c693031947.mp4?token=rxcJYgO1qLEX2lYogPZDkqSAlPd5mPgruFSShJMRmhsJa0t5abGb8Ju1FvOXOOFq8qoWsQzOa1SZUP5297fTuvC8VheKKnl4fmUkQrx9Zf2VKjdNMymTIPt-bItZfeIJ49gKjWRXlhqB6QJg7WCMeNI0SYmspkMfyANeqPFkjOA52cSZf6Y-avzZobQaX3GgBY8_6MwbqPkTodzmcfx1GNzJr4Lhnpn2Sh_2P489bg5sFJS8hVvDVRaOlpHtliZ_0NomK__FMJDtRgnVkOeD2xBOAWTBspFHY9WPYs1X3tiWWyRTSDGM_2I4vtTdgUkV5TVvjiVfhBM-LPfnQ4wFCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام:
یک فروند بالگرد
MH-60 سی‌هاوک
از عرشه ناوشکن موشک‌انداز
یو‌اس‌اس رافائل پرالتا (DDG-115)
در حالی به پرواز درآمد که این ناو در چارچوب اجرای محاصره دریایی آمریکا علیه ایران در
دریای عرب
فعالیت می‌کند.
تا امروز
۱۵ سپتامبر
، نیروهای ما مسیر
۱۰۳ (
۲ کشتی فقط امروز )
کشتی تجاری
را برای اطمینان از رعایت مقررات محاصره ایران تغییر داده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23213" target="_blank">📅 23:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23212">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">رسانه های عبری : ساعتی پیش، فرمانده یک گردان از کتائب القسام شاخه نظامی
حماس
در
رفح
شهری در
جنوب نوار غزه
و در مجاورت مرز
مصر
، ترور شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23212" target="_blank">📅 23:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23211">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23211" target="_blank">📅 22:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23210">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">رأی امروز سنای آمریکا برای پیشبرد CLARITY Act شکست خورد.
این قانون قرار بود چارچوب مشخصی برای بازار رمزارز آمریکا ایجاد کند و حدود اختیارات SEC و CFTC را تعیین کند. شکست رأی به معنی رد دائمی قانون نیست و امکان دارد نسخه اصلاح‌شده آن دوباره در سنا مطرح شود، اما فعلاً مسیر تصویب متوقف شده و
ابهام مقرراتی در بازار کریپتو ادامه پیدا می‌کند
؛ موضوعی که می‌تواند در کوتاه‌مدت فشار منفی بر بازار ایجاد کند.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23210" target="_blank">📅 22:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23209">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e060275b19.mp4?token=qHi2YL4TFztMUPURt7SXgaxmXOBfsruZ6GNEnU4vljrLQRSL17eCAJeTvscNqmak0C_STJn5HsAQs7aMRd-OsgYXt2-Q58-xWtFKTXnGR4dUxJ1oy6yUzzT2Oa-gcFEIep5YrrR3lojiUYQiDSgGM36I820YLD5OPCEzuH9zvjIaugvGFc5_8NkQ47_GtVI4m3eC9EDZCALBBL-RE82l7rni3OeUmTkaEcTuAV0QjyrPtofUxepHrJVfI0YXp5niWOTBSeUDUw1ngRCQ1ek2cHKKQMsXtTJUxWvu70E1a9wjhLZ6BFQHme5DYqMfKY5yz8M5V3dAB2B3T0lXW9_BUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e060275b19.mp4?token=qHi2YL4TFztMUPURt7SXgaxmXOBfsruZ6GNEnU4vljrLQRSL17eCAJeTvscNqmak0C_STJn5HsAQs7aMRd-OsgYXt2-Q58-xWtFKTXnGR4dUxJ1oy6yUzzT2Oa-gcFEIep5YrrR3lojiUYQiDSgGM36I820YLD5OPCEzuH9zvjIaugvGFc5_8NkQ47_GtVI4m3eC9EDZCALBBL-RE82l7rni3OeUmTkaEcTuAV0QjyrPtofUxepHrJVfI0YXp5niWOTBSeUDUw1ngRCQ1ek2cHKKQMsXtTJUxWvu70E1a9wjhLZ6BFQHme5DYqMfKY5yz8M5V3dAB2B3T0lXW9_BUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : هیچ هدف‌گیری‌ای داخل شهر مکه مکرمه صورت نگرفته است. دو پایگاه هوایی در نزدیکی مکه قرار دارند: پایگاه هوایی ملک فهد در طائف و پایگاه هوایی ملک عبدالله در جده. هواپیماهای جنگی سعودی از این پایگاه‌ها برای انجام عملیات و بمباران در یمن پرواز…</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23209" target="_blank">📅 22:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23208">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">فعالیت پدافند هوایی در استان آذربایجان غربی، واقع در شمال غرب ایران، در پی گزارش‌هایی مبنی بر فعالیت پهپادها در این منطقه.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23208" target="_blank">📅 22:13 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23207">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23207" target="_blank">📅 22:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23206">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ادعای یک فعال رسانه‌ای و سیاسی : امروز اطلاعاتی مبنی بر حمله قریب الوقوع آمد و ساعت ۱۱ظهر به تمام مراکز نظامی دستور تخلیه فوری داده شد. آمریکا بخاطر مسائل مختلف از جمله پیوستگی و وحدت تنگه های هرمز و باب المندب تحت فشار است و نتانیاهو نیز نقش تحریک کننده را بر عهده دارد. دشمن درپی ترور مسئولان عالی رتبه است
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23206" target="_blank">📅 21:51 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23205">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ائتلاف نیروهای سیاسی کردستان ایران برای ۲۵ شهریور فراخوان اعتصاب سراسری داد: این ائتلاف همزمان با چهارمین سالگرد کشته‌شدن مهسا ژینا امینی و آغاز جنبش «زن، زندگی، آزادی» از مردم در سراسر ایران خواست روز چهارشنبه ۲۵ شهریور با بستن مغازه‌ها و بازارها و خودداری…</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23205" target="_blank">📅 21:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23204">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1pg16DDPHqAWtPzC9yDsqoS1e0eNXsA93UhT44PXEMFdtjVp04vxDp5QUFcdByNP1NeCyi9PPJCXb5eQm82cL6FenHB-eW5NLILnQJ8hpQbo8vMvFyjIOEQK4VKL2SxbiLCnjPt0RHkVCBYO_TO-EAAzjaCBdWlXy726e7upKAHEFbKhhFOgGkUQ6ydBHVAVtXZuefRIogeCwNHgvCik5r-cJIxyoFnszqpr7WcRBF23qs-6gYie4pEQnbbVTxaIQRYvxZsrQ9ksbKEXO2Xe9H_9YPCxtJI5AxGOa17fsjIP2XCi146Z_p7GdRQSGThXl5q4VOPRfhH_GwThyWZ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت وارد کانال ۱۰۹$
📈
شد
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23204" target="_blank">📅 21:37 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23203">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خبرگزاری کان اسرائیل: موساد و ارتش اسرائیل از طریق سنتکام، اطلاعات بسیار گسترده حساسی از حوثی های یمن را در اختیار عربستان سعودی قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23203" target="_blank">📅 21:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23202">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSyOaTZYoUNsOfBUQPBfvz-lKJryjZvGtg617pj9A6vOk__pY3QNze1XJZ3Pp8bDXBwjYSEw8AnVSokz0hTqOFIJe_QEqU-SFDuNcANI80Kc6QA8qguuqH6gSP20W8TUQgNxiewb2p_o-NVZBu42PjyhB40HpD6WZvVA2EnETZ0I4Dkn5xzkaVK3x58kru45qNsFJNObfpZeF9ZDUScSXrw-DbkG7_9FnhAEviq-PZsJMQ2q6XVKhgvw5rhnZlzJmmNKvN5kX-F3sKYiYPlbgJ-YBZIcA-8pZJ91qH7A4v8LPcimxercLWgOcc6pzp4O9-meCjIcYTNKB2OKWlr9fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان:
در قراردادی که آن را «مشکوک‌ترین قرارداد تاریخ نفت ایران» دانسته،
۸۰ میلیون بشکه نفت
پس از توافق اسلام‌آباد به چهار تراستی
علی بایندریان، روح‌الله رضوی، محمدهادی مومنین و حسین شمخانی
واگذار شده است. کیهان می‌گوید این چهار تراستی
سابقه بدهی جدی به وزارت نفت
داشته‌اند و طبق مصوبات شعام و وزارت نفت، نباید پیش از تسویه بدهی سهمیه نفت می‌گرفتند. ابهام دیگر،
فروش اعتباری و حساب‌باز نفت بدون مشخص بودن تضامین و مسئول ریسک وصول مطالبات
است. همچنین حدود
۸ درصد تخفیف
برای این معامله در نظر گرفته شده که به گفته کیهان، با توجه به حجم نفت، ارزش آن به
چند میلیارد دلار
می‌رسد و یک رکورد تاریخی محسوب می‌شود. کیهان همچنین از
درخواست نهادهای نظارتی برای ارائه مستندات درباره نحوه واگذاری، شرایط فروش و تضامین
خبر داده و خواستار ورود فوری
بازرسی دفتر رهبر انقلاب و سازمان بازرسی کل کشور
به این قرارداد شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23202" target="_blank">📅 21:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23201">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سخنگوی گروه تروریستی حوثی یمن، یحیی سریع:
هواپیماهای جنگی سعودی در ۲۴ ساعت گذشته، ۵۲ حمله هوایی با استفاده از هواپیماهای "F15" و "تایفون" که از پایگاه‌های خمیس مشیت و طائف پرواز کرده بودند، انجام دادند. این حملات وحشیانه، بدون پاسخ نخواهند ماند.
@WarRoom</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/23201" target="_blank">📅 21:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23200">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خبرگزاری واپو:
دولت ترامپ در حال آماده‌سازی یک فروش تسلیحاتی به ارزش ۲.۸ میلیارد دلار به اسرائیل است که شامل ۴۰,۰۰۰ بمب ۲,۰۰۰ پوندی (۲۰,۰۰۰ بمب MK-84 و ۲۰,۰۰۰ بمب BLU-117) به علاوه ۲۰,۰۰۰ سر جنگی نفوذگر I-2000 خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23200" target="_blank">📅 21:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23199">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سروان تیم هاوکینز، سخنگوی سنتکام، امروز سه‌شنبه ۲۴ شهریور به سوران خاطری از بخش فارسی صدای آمریکا گفت: «می‌توانم تأیید کنم که قایق‌های کوچک ایرانی اخیراً تلاش کردند یک شناور بی‌سرنشین سطحی آمریکا را تصرف کنند، اما پس از واکنش قاطع نیروهای سنتکام در این کار ناکام ماندند.»
سخنگوی سنتکام تصریح کرد که این شِهپاد «همچنان تحت کنترل عملیاتی ایالات متحده است.» «شِهپاد» سرنامی است که از حروف نخست عبارت «شناور هدایت‌پذیر از دور» تشکیل شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23199" target="_blank">📅 20:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23198">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">باراک راوید، آکسیوس:
یک مقام آمریکایی گفت ارتش آمریکا و کشورهای حوزه خلیج فارس، عبور روزانه و در طول ساعات روشن روزِ نفتکش‌ها از تنگه هرمز را آغاز کرده‌اند و دیگر مانند ماه‌های اخیر، عبور نفتکش‌ها فقط در ساعات شب انجام نمی‌شود.
همچنین
ارتش آمریکا روز دوشنبه
دیروز
دو قایق کوچک ایرانی را منهدم کرد
؛ پس از آنکه سپاه پاسداران انقلاب اسلامی تلاش کرد یک شهپاد نیروی دریایی آمریکا را که در حال گشت‌زنی در تنگه هرمز بود، تصرف کند
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23198" target="_blank">📅 20:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23196">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b49ca62412.mp4?token=e8HV7VXWsgEOc4Xij22r4hHrq8nmM-FQkergS-J0M5RsQj8cPgsm8ydzSj1YgWtwiloxrEhQdFUsxI5puVbVrRLiFkG3wcRB4F0takqmiIl9sZQ5eHAQz7z_kAI8xoY5NLEk6bGTyGgCi_8Qa43Yggub2_2vsQl6i-X_ZgoZ-EvPIl1HFdK2qrJUwYxGZ_Zcge_OT23VmfUVyHHLJUGulQMcNo7m1zbg8OgsJHdDZYUxSTlqBO_QQb4p9X-IHiiI-OyGISVcDJaQ4ZhrfWjaCs5xpRwz1HY0evShb6JXSC8eHw-yrOiegRVKAR55K7QaSUXjfQFvNsFwYM9owjhJTgHd71wuUIXl7TaVD6xrU1F3WBN8jN-GfrjhCj8BnVtgmbfLEnr7T340paP_DGpmA2Fpjt7kJauGtpJQ2N2MbXHnBurqCHatrOjgzo9tWQmm9Lig7F1eYaQg4yDpyMyWGZ2Dnj-b_aCCGVxVzuVc4rhuh53ppWYITwnJlNCZpl289qX6ZcxBCnQhTLDZOHkJs-abgPzo_hBqyvVZghv8SIqg9Gwb6S0yl-W08jkAoy0evB9B2f6Zduz3XQWwal2Y-wiSrfrXpSL75QHJq-czMff5yHdB7eLIQ-IOU4-d2_F1myXlpqV7vPtDAvOiB5kLf27srllwx36mQqlqJ-2eXRM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b49ca62412.mp4?token=e8HV7VXWsgEOc4Xij22r4hHrq8nmM-FQkergS-J0M5RsQj8cPgsm8ydzSj1YgWtwiloxrEhQdFUsxI5puVbVrRLiFkG3wcRB4F0takqmiIl9sZQ5eHAQz7z_kAI8xoY5NLEk6bGTyGgCi_8Qa43Yggub2_2vsQl6i-X_ZgoZ-EvPIl1HFdK2qrJUwYxGZ_Zcge_OT23VmfUVyHHLJUGulQMcNo7m1zbg8OgsJHdDZYUxSTlqBO_QQb4p9X-IHiiI-OyGISVcDJaQ4ZhrfWjaCs5xpRwz1HY0evShb6JXSC8eHw-yrOiegRVKAR55K7QaSUXjfQFvNsFwYM9owjhJTgHd71wuUIXl7TaVD6xrU1F3WBN8jN-GfrjhCj8BnVtgmbfLEnr7T340paP_DGpmA2Fpjt7kJauGtpJQ2N2MbXHnBurqCHatrOjgzo9tWQmm9Lig7F1eYaQg4yDpyMyWGZ2Dnj-b_aCCGVxVzuVc4rhuh53ppWYITwnJlNCZpl289qX6ZcxBCnQhTLDZOHkJs-abgPzo_hBqyvVZghv8SIqg9Gwb6S0yl-W08jkAoy0evB9B2f6Zduz3XQWwal2Y-wiSrfrXpSL75QHJq-czMff5yHdB7eLIQ-IOU4-d2_F1myXlpqV7vPtDAvOiB5kLf27srllwx36mQqlqJ-2eXRM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر از نفتکش الگایا که ادعا شده در اثر برخورد با مین‌های سپاه منفجر شده
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/23196" target="_blank">📅 20:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23195">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ادعای رسانه های عربی حامی رژیم ج.ا : رهبران ارتش‌های ایالات متحده، اسرائیل و کشورهای عربی، جلسه‌ای مخفی درباره ایران برگزار کردند. @WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23195" target="_blank">📅 20:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23194">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAs-DO-oUP_vvTudjyaiCYC-mrH_ZNRL9-dIhylrG9JOexFmvG72sTa4rGBm-0tZOmdvi1nirJJdFlc4JgZ4l5Zegz8Aq9AUZJJkDj5j3giok0iB3uprbQV9pYVjrfHLIjmPtg9nakcseX-fkAZOR99YXTg5hDnyL6nK-TmbUNGX30eP767BJ469DfA5cT-nRvKhkCvv9fHtbvQtghcgiJfJidOlFtzrcEgZQmY0aCROyW-6_mDqUBl9ouHP18RvyNF5ewM7XcFG-7lfie2WYm1MmILewMOcMPSaZx-V-GyCUAfnn-6mN4ZBlYBbg3j0VdpKLhx1sZVAVhyaz56v_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت دوباره به کانال ۱۰۸$
📈
وارد شد
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/23194" target="_blank">📅 20:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23193">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">وزارت دادگستری آمریکا: دولت آمریکا برای مصادره حدود ۶۱ میلیون دلار رمزارز مرتبط با درآمد حاصل از فروش غیرقانونی نفت ایران اقدام قضایی کرده است. طبق شکایت دادستانی ناحیه جنوبی نیویورک و اف‌بی‌آی، شبکه‌ای از شرکت‌ها و آدرس‌های رمزارزی با عنوان Entity A بیش از…</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/23193" target="_blank">📅 20:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23192">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ادعای رسانه های عربی حامی رژیم ج.ا :
رهبران ارتش‌های ایالات متحده، اسرائیل و کشورهای عربی، جلسه‌ای مخفی درباره ایران برگزار کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/23192" target="_blank">📅 19:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23191">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f106a591ad.mp4?token=CIGo30e_BQ_pB_d1Yyn1Y5YD1hEl37maZjjjSGyz1--H9JL_YIdgVKVuIq_Ac6uMBX2xLDkeCbMH6d4w2LB2lLTm-_9mWYpbbJ7qZ6cZT5Rqn94r-mn3Sf-aDfljJTCM4VGNf6N4o7u4qZx7uIozbIVDuG6nAoUddAN2UuOc9BGv-UJRMkUP37kx52uJC0_tEuw9n2EKvOJvK4LwyV823wb16kGT9HHQjcoryW4--um1hTTBsoK0W5aGGrEbzA_Q-4yMxzFykCXbDDf1l0DCdw4eggAhEP8xLcyG4lUlToUVdWqGPEWU-Scw2lN36aZuG2JBX7xI6xt5Q-lXfhj_Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f106a591ad.mp4?token=CIGo30e_BQ_pB_d1Yyn1Y5YD1hEl37maZjjjSGyz1--H9JL_YIdgVKVuIq_Ac6uMBX2xLDkeCbMH6d4w2LB2lLTm-_9mWYpbbJ7qZ6cZT5Rqn94r-mn3Sf-aDfljJTCM4VGNf6N4o7u4qZx7uIozbIVDuG6nAoUddAN2UuOc9BGv-UJRMkUP37kx52uJC0_tEuw9n2EKvOJvK4LwyV823wb16kGT9HHQjcoryW4--um1hTTBsoK0W5aGGrEbzA_Q-4yMxzFykCXbDDf1l0DCdw4eggAhEP8xLcyG4lUlToUVdWqGPEWU-Scw2lN36aZuG2JBX7xI6xt5Q-lXfhj_Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشات حاکی از این دارد مخفیگاه‌های مظنون به داعش در صحرای سوریه امروز بعد از ظهر توسط هواپیماهای A-10 نیروی هوایی ایالات متحده مورد حمله قرار گرفتند. این اولین حملات هوایی شناخته شده پس از ماه‌ها است.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23191" target="_blank">📅 19:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23190">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">یک فروند هواپیمای بوئینگ ۷۳۷ متعلق به شرکت هواپیمایی سپهران که از مشهد عازم کرمانشاه بود، پس از برخاستن اعلام وضعیت اضطراری کرد و به مشهد بازگشت و به سلامت فرود آمد. علت گزارش‌شده برای این حادثه، مشکل در یکی از چرخ‌ها هنگام برخاستن و احتمال آسیب‌دیدگی موتور…</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/23190" target="_blank">📅 19:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23189">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b83c064733.mp4?token=RjvwIqbLm_J23yVsRaVMZAYzF7_1EgMjT-cLLrMOJe3NzJy9_6JFAk8WmUvPTZAy4MpeDcEHkljNUjOfuczkkiBSKnbuFHhkqUO3oIRhD5nFj_5BvjDzykF4z9yTxo5yDGTgA1E5oPFY-neVsSn8fi75V54JvEOU3rATkqXO5lnyjYBFcMNz8okso4IbWyrOsysZcHC_AiF-ZVApYpXv90XV_D22meKi6Ja7tPGJSgCN4zcA5YSnB_ACnQuoaChrAAcdyYzKve88CKXU4xt76VGI1KxwnVFplFY08pmpAM_Lwy78tf_bWktfq206Ipc1-xGY24jQqII_76-pcKCZj3zU8pLzX_pFgvVuJepGt9pUCIcssKSChincrmZOyJmqLdrqrHW_tmQppbZW2ZH_gl-06kD8HkvW668A0LMFV5v7nJeJqXcdNdeuoEFCGwL87TjnIe34o79GMG9SuZ3tZIXAnb1jJqqgA6Lrc_CfBZ0JZPSkDqtRkyycPyBdKcZb0UoYFyp2cqk-JP3WfJ7NtBEJz9bPlIqwPWtfkHxGxv10IH-WuJzJOh0TzUaHl1qndI7EO67QVW-evYavqya9Ssi0CIVFR55XHhCub3QZQ0jCYlsUcT3ZbaxrJCCvk0Qa9Y-KcQz4ivKgMaH51udMit-kNYXRuhLgkMym_x6c8kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b83c064733.mp4?token=RjvwIqbLm_J23yVsRaVMZAYzF7_1EgMjT-cLLrMOJe3NzJy9_6JFAk8WmUvPTZAy4MpeDcEHkljNUjOfuczkkiBSKnbuFHhkqUO3oIRhD5nFj_5BvjDzykF4z9yTxo5yDGTgA1E5oPFY-neVsSn8fi75V54JvEOU3rATkqXO5lnyjYBFcMNz8okso4IbWyrOsysZcHC_AiF-ZVApYpXv90XV_D22meKi6Ja7tPGJSgCN4zcA5YSnB_ACnQuoaChrAAcdyYzKve88CKXU4xt76VGI1KxwnVFplFY08pmpAM_Lwy78tf_bWktfq206Ipc1-xGY24jQqII_76-pcKCZj3zU8pLzX_pFgvVuJepGt9pUCIcssKSChincrmZOyJmqLdrqrHW_tmQppbZW2ZH_gl-06kD8HkvW668A0LMFV5v7nJeJqXcdNdeuoEFCGwL87TjnIe34o79GMG9SuZ3tZIXAnb1jJqqgA6Lrc_CfBZ0JZPSkDqtRkyycPyBdKcZb0UoYFyp2cqk-JP3WfJ7NtBEJz9bPlIqwPWtfkHxGxv10IH-WuJzJOh0TzUaHl1qndI7EO67QVW-evYavqya9Ssi0CIVFR55XHhCub3QZQ0jCYlsUcT3ZbaxrJCCvk0Qa9Y-KcQz4ivKgMaH51udMit-kNYXRuhLgkMym_x6c8kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : مردم شریف ایران، شرایط ایمنی حمل‌ونقل کشور به‌شدت نگران‌کننده شده است. در بخش هوانوردی، گزارش‌هایی از اختلال سامانه‌های ناوبری گزارش شده همچنین بعد از‌جنگ اکثر سامانه های راداری نابود شده اند و از ترس حملات خاموش کردن عمدی ترانسپوندر برخی…</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23189" target="_blank">📅 19:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23188">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbcfdfe8fd.mp4?token=MwJosyodoNzJQZ4QNy0E2bLF2J-jMcUpeEqw5foyEfvBFiO5PdKBQqwTJHUN41S_qtv3-AoK9A4Da35SlNH_RNB3UiJgCGFvUyIUta-kIQYBr063_IEkm0vP3Hi74NnD8sEW8guLcE4k_gYcK9CIvVc8fEVD3lxIXbTpuDDFUGgTio0TqFgVwD9WZbEU_cFl2UC6hLwJOjFb4vIlqLb-tsnhIzCaJMGhhxnMPqf1cwvGvywDwCBLnIM760GBwzNe26_uRxyyH05Lla1g3RoeEWGSFzNI4vyzhia2WcRvkbk3H7O7jKV2aJWsFgDXzI6Biul55-AgP7xilS9CfRWYOl6uFlo33UPTSDOua0GwtbIxXkW4JuicsARCZC3oSEOxE8kDuP3jfAAobM9g4kMxth6z6R41TDj8vIaoI1jW2d9ReQjpWmLdgUJrhOYh6F6QE3C5GRAF1aWXsAm4kb-aq4XOQmM3n7hIDpvYYIC7nUKdReZ_z9JPzwcN67fR03TqTW_eWhSR5t9tiMUXz4GZZH1wMwGZmvJPDg9iqR5fu7njwCDT5ct760Gdj26crf75HbpxocO6uXiZzuVLi76KOaG8pItIwcs_kUlPKz9Ykjzkqmp0Lm49EbM3c5iw9gErimsoCluN7oGM_dUnZJqcYIOf5XpE84gtgXF8xJ4d0Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbcfdfe8fd.mp4?token=MwJosyodoNzJQZ4QNy0E2bLF2J-jMcUpeEqw5foyEfvBFiO5PdKBQqwTJHUN41S_qtv3-AoK9A4Da35SlNH_RNB3UiJgCGFvUyIUta-kIQYBr063_IEkm0vP3Hi74NnD8sEW8guLcE4k_gYcK9CIvVc8fEVD3lxIXbTpuDDFUGgTio0TqFgVwD9WZbEU_cFl2UC6hLwJOjFb4vIlqLb-tsnhIzCaJMGhhxnMPqf1cwvGvywDwCBLnIM760GBwzNe26_uRxyyH05Lla1g3RoeEWGSFzNI4vyzhia2WcRvkbk3H7O7jKV2aJWsFgDXzI6Biul55-AgP7xilS9CfRWYOl6uFlo33UPTSDOua0GwtbIxXkW4JuicsARCZC3oSEOxE8kDuP3jfAAobM9g4kMxth6z6R41TDj8vIaoI1jW2d9ReQjpWmLdgUJrhOYh6F6QE3C5GRAF1aWXsAm4kb-aq4XOQmM3n7hIDpvYYIC7nUKdReZ_z9JPzwcN67fR03TqTW_eWhSR5t9tiMUXz4GZZH1wMwGZmvJPDg9iqR5fu7njwCDT5ct760Gdj26crf75HbpxocO6uXiZzuVLi76KOaG8pItIwcs_kUlPKz9Ykjzkqmp0Lm49EbM3c5iw9gErimsoCluN7oGM_dUnZJqcYIOf5XpE84gtgXF8xJ4d0Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا:
«من فقط به اظهارات رئیس‌جمهور ایران، رئیس مجلس و رئیس بانک مرکزی استناد می‌کنم که گفته‌اند اقتصاد کشور در وضعیت بسیار وخیمی قرار دارد. او به همکاران و همفکران تندروی خود در سپاه پاسداران و همچنین مردم ایران هشدار داده بود. ما شاهد سقوط ارزش پول ملی و تورم سرسام‌آور بوده‌ایم و به‌طرز باورنکردنی، در کشوری که سومین منابع بزرگ انرژی جهان را در اختیار دارد، حالا مردم با صف‌های سه تا چهار ساعته برای دریافت بنزین مواجه‌اند، زیرا ایران مجبور است سوخت خود را وارد کند. بنابراین، فروپاشی اقتصادی به دلیل محاصره امکان‌پذیر است. ترکیب محاصره، به‌علاوه ماه‌هایی که صرف شناسایی و ترسیم شبکه‌های موجود در سامانه پرداخت کرده‌ایم، به ما اجازه داده تا فشار بر آنها را افزایش دهیم و من معتقدم این فوران‌های خشونت‌آمیزی که از سوی آنها شاهد هستیم، نتیجه واکنش یک حیوان زخمی و به‌دام‌افتاده است.»
@WarRoom</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/23188" target="_blank">📅 19:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23187">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">امشب میخوام بیام تویتر اسپیس (x)
و با همه شما لایو حرف بزنم بیارمتون بالا شما سوال کنید و … اگه نمیدونید چیه دقیقا مثل کلاب هاوس است ولی در پلتفروم اکس
x.com/yasharrapfa
ساعت دقیق رو کمی دیگه اعلام میکنم ، شما کاراتونو بکنید آماده بشید</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/23187" target="_blank">📅 19:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23186">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آژانس بین‌المللی انرژی اتمی:
ایران در جریان هفتادمین کنفرانس عمومی آژانس به عضویت کمیته عمومی (General Committee) این کنفرانس انتخاب شد.
این انتخاب در جریان نشست سالانه آژانس در وین انجام شده است.
برخی گزارش‌های ایرانی می‌گویند این انتخاب در یک رأی‌گیری مخفی انجام شده، اما جزئیات رسمی رأی‌گیری هنوز منتشر نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/23186" target="_blank">📅 19:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23185">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اسکات بسنت امروز اعلام کرد آمریکا فشار مالی علیه ایران را تشدید می‌کند و از افراد در سراسر جهان خواست اطلاعات مربوط به شرکت‌ها، بانک‌ها و اشخاصی را که به ایران برای دور زدن تحریم‌ها یا انتقال پول کمک می‌کنند، به خزانه‌داری آمریکا گزارش کنند.
بسنت گفت افرادی که اطلاعات قابل اقدام ارائه دهند، صرف‌نظر از محل زندگی یا محل کارشان، ممکن است واجد شرایط دریافت پاداش مالی باشند. این اقدام بخشی از
Operation Economic Outcast
است که هدف آن قطع «راه‌های مالی» باقی‌مانده برای حکومت ایران و شبکه‌های وابسته به آن عنوان شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23185" target="_blank">📅 18:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23184">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-QnhyXf_b8g6T0vVHyrLDWHQ43NPKR-7anDFUkoKp_IEeztsL41BLuxzqr5J6HcS90vPmcUi5CA5Wuq9muuB1tXCa1p4nN44lJpSNZBzPxhSr5lH-gz5uVaKLCRdrlsZCmE8jQrGWYXmSJBe6kgH6A-K283xugEJd8G_xRi4urnDF6IZ0Gd44vFkSimm4HaLKZI6qjD4EJ5GzYg2fdQzr995491KIbYalgEXB8ztxcDaEgvQj0gz41CAcbvhBVJCgH_zeVyh9voF5f1bnBdNS4Dw6c--mF0UtC5IqH-zJ90_1BLV1VFW7fbeQNUq9Y6sK71u5w5lmV25JMPpvWKTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون آتش سوزی محدوده پیروزی/محلاتی تهران
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23184" target="_blank">📅 18:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23183">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سنتکام : آمریکا و اردن رزمایش دوسالانه «Eager Lion 2026» را امروز ۱۵ سپتامبر در فورت کارسون، کلرادو آغاز کردند. بیش از ۲۰۰ نیروی آمریکایی و اردنی در این رزمایش دو هفته‌ای حضور دارند و تمرین‌ها بر
پدافند هوایی، امنیت دریایی، مقابله با تروریسم، جنگ سایبری و واکنش به بحران‌ها
متمرکز است. این نخستین‌بار است که آمریکا میزبان رزمایش Eager Lion می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23183" target="_blank">📅 18:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23180">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fff5fc67b.mp4?token=TthA4qQ7kGNLr2DJFhCBQYU_qQYOiL8r8VWStDCN4rHnqMec1SnpaH_WXhYd_v_Ycfux8RCj0bc06TUPDf1KZPaWh5Vj17y_SK0fU1D0Qtr_XY6OViwZXz5dgKQTRH8m41qGBD3KDUfeHnNyjqO6froydWtBap86Pnp5ypI1IZWTa0Pw-Y_BVrspSwQbS3e_5k73WW5EyX7sCXJSnF5QcpKcLH0NPNDZa5CT1NQSPvprlRF6rDERxBoQPrM1OhK1POc6K57pJepueMuKAEpyX2VLPTiimsmz-VUIEymPAOIAmYXU_2UrQ21QQKr9i3jH8BPESem4oAqDUq1w-ocbOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fff5fc67b.mp4?token=TthA4qQ7kGNLr2DJFhCBQYU_qQYOiL8r8VWStDCN4rHnqMec1SnpaH_WXhYd_v_Ycfux8RCj0bc06TUPDf1KZPaWh5Vj17y_SK0fU1D0Qtr_XY6OViwZXz5dgKQTRH8m41qGBD3KDUfeHnNyjqO6froydWtBap86Pnp5ypI1IZWTa0Pw-Y_BVrspSwQbS3e_5k73WW5EyX7sCXJSnF5QcpKcLH0NPNDZa5CT1NQSPvprlRF6rDERxBoQPrM1OhK1POc6K57pJepueMuKAEpyX2VLPTiimsmz-VUIEymPAOIAmYXU_2UrQ21QQKr9i3jH8BPESem4oAqDUq1w-ocbOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏لحظۀ ترور یوسف گرگیج امام جماعت حامی حکومت در زاهدان
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23180" target="_blank">📅 18:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23179">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">وزارت دادگستری آمریکا: دولت آمریکا برای مصادره حدود
۶۱ میلیون دلار رمزارز
مرتبط با درآمد حاصل از فروش غیرقانونی نفت ایران اقدام قضایی کرده است. طبق شکایت دادستانی ناحیه جنوبی نیویورک و اف‌بی‌آی، شبکه‌ای از شرکت‌ها و آدرس‌های رمزارزی با عنوان
Entity A
بیش از
۱.۵ میلیارد دلار
از درآمدهای فروش غیرقانونی نفت ایران را دریافت و منتقل کرده‌اند. دو شرکت هنگ‌کنگی
Blessed Trust
و
Hexa Whale
نیز از حساب‌های خود در صرافی
بایننس
برای انتقال بخشی از این پول‌ها استفاده کرده‌اند؛ وجوهی که به گفته آمریکا در نهایت به دولت ایران و شبکه‌های مرتبط با
سپاه پاسداران
منتقل شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23179" target="_blank">📅 16:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23177">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">خبرگزاری آکسیوس به نقل از مقامات آمریکایی : نیروهای آمریکایی در واکنش به تلاش سپاه برای توقیف شناور بدون‌سرنشین آن دو قایق ایرانی را در نزدیکی تنگه هرمز هدف قرار دادند. این حادثه نشان می‌دهد رویارویی مستقیم نیروهای دریایی آمریکا و سپاه در هرمز همچنان ادامه…</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23177" target="_blank">📅 16:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23176">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اتاق جنگ با یاشار : در درگیری امروز گزارش شده از دیدبان اتاق جنگ ,  ۲ قایق تندرو سپاه که از اهالی کرگان(میناب) بودند(اکثر این اهالی با حکومت هستند و پاسدارند) عصر امروز هدف حمله آمریکا در تنگه قرار گرفتن ۱ جسد پیدا شد و ۳ نفر  دیگه فعلا تا این لحظه نگارش این…</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23176" target="_blank">📅 16:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23175">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59afb2fe58.mp4?token=pbFFdJO5UYk-ttsiSoVB4epKD7PsNwKxlsezD--jw6HQjOdASJN3rOWQzYAo5V9l3zG_3L_Y8cGq2V74imIIXxSvuPkDA8m_b8R95rt9h89q_DzWrJXSWC-vWaiDlIG9OQhZCAn18TuH5_No5iYqDE7AeK-tDeu0tkwQRlDk5ukXfBVfq8rOphOl0eKRIcPuBWno3QPFQY8eAeGMmErBYWk_BpOrAxypshPLVPenAnz0BHrOoYZYHkLZiNxasnFjh6DWG3swbqkHskkhXrA6DoQSjPD_ErKPzR4wN_nvpRmOnnmBlGPZj56jXm_08m4BrW08g-TYwXGYuBmHzB7apw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59afb2fe58.mp4?token=pbFFdJO5UYk-ttsiSoVB4epKD7PsNwKxlsezD--jw6HQjOdASJN3rOWQzYAo5V9l3zG_3L_Y8cGq2V74imIIXxSvuPkDA8m_b8R95rt9h89q_DzWrJXSWC-vWaiDlIG9OQhZCAn18TuH5_No5iYqDE7AeK-tDeu0tkwQRlDk5ukXfBVfq8rOphOl0eKRIcPuBWno3QPFQY8eAeGMmErBYWk_BpOrAxypshPLVPenAnz0BHrOoYZYHkLZiNxasnFjh6DWG3swbqkHskkhXrA6DoQSjPD_ErKPzR4wN_nvpRmOnnmBlGPZj56jXm_08m4BrW08g-TYwXGYuBmHzB7apw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاملترین نسخه و با بهترین ترجمه و خواناترین زیرنویس فارسی از گزارش ویژه «۶۰ دقیقه» شبکه CBS درباره عملیات نجات افسر تسلیحات یک فروند F-15E آمریکایی که پس از سقوط جنگنده در ایران، حدود ۵۰ ساعت در خاک ایران مخفی ماند و در نهایت طی یک عملیات ویژه نجات پیدا کرد.…</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23175" target="_blank">📅 15:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23174">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وزارت جنگ آمریکا برای نخستین بار به‌طور رسمی در گزارشی به کنگره تأیید کرد که یک جنگنده رادارگریز اف-۳۵ ارتش آمریکا در جریان مأموریت بر فراز ایران، هدف آتش قرار گرفته و آسیب دیده است؛ موضوعی که پیش از این تنها به‌عنوان فرود اضطراری یک فروند اف-۳۵ اعلام شده بود
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23174" target="_blank">📅 15:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23173">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">شایعه شده است که فردی در هتل اسپیناس، واقع در بلوار کشاورز در مرکز تهران، کشته شده است.
یک «منبع آگاه پلیس» در گفتگو با خبرگزاری دولتی مهر، ضمن تکذیب این ادعا، افزود: «پلیس هیچ‌گونه گزارشی مبنی بر وقوع حادثه در هتل اسپیناس دریافت نکرده است.»
@WarRoom
یاشار : خبر‌های از این دست فقط برای گمراه کردن افکار عمومی هست نظر من فقط باید روی اعتصابات تمرکز بشه ! با دقت بگردین از روی ساعت  انتشار ببینید این خبر از چه رسانه هایی پخش شده و از کجا سرمنشأ (قدیمی ترین پست و اولین ) گرفته و بعد بایکوتشون کنید.</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23173" target="_blank">📅 15:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23172">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">حقیقت یاب اتاق جنگ (از سری خبر های فیک ادمین های بیسواد تلگرام) : در دوره هخامنشی، به‌ویژه از زمان داریوش بزرگ،
دَریک سکه طلای هخامنشی
و
سیگلوس سکه نقره‌ای
بود و این دو، نظام پولی دوفلزی هخامنشیان را تشکیل می‌دادند. اما «شِکِل» داستان قدیمی‌تری دارد:
شِکِل در اصل یک واحد وزن در خاور نزدیک باستان بود
و ریشه آن به زبان‌های سامی باستان بازمی‌گردد؛ این واژه بعدها در سنت‌های مختلف، از جمله عبری، به‌عنوان نام یک واحد پول نیز به کار رفت. حتی «سیگلوس» هخامنشی نیز از نظر نام‌شناسی با واژه شِکِل مرتبط دانسته می‌شود. بنابراین اینکه بگوییم
«شِکِل نام واحد پول هخامنشیان یا یک واژه ایرانیِ هخامنشی بوده» دقیق نیست
؛ این واژه ریشه‌ای بسیار کهن در خاور نزدیک داشته و امروزه نیز نام پول اسرائیل است
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23172" target="_blank">📅 14:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23171">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25a166b96b.mp4?token=WhXLvMalsAIBXc94lmuL89vc7xUc-BAaU4zVN8-I7pirWtMTDurXyPbb2Rz1cIU_D5Vi-DGUk8CbiPVkn0loZpALWu0rGmuMVM7VksNpwa7Zv2FAXCVRF1vu4P8DSMo__005fsoxs_GRCZK5IIiA3gRZwjDmchoMpBpU1Xkss5x_w_JZa5ovubFNE619Am1dVFy5i42B5fpbIICMcvqG24kcYGy18msuXlDYab5TX3hPfgdas-Ca8pXO0F69C8RhZcvZ9-saZxwLRUDaAneH9J_5xJTb75waSJ-3tQSqFQf-l0CMN8Lg8Vrz8ww7Xtjh8mcq6uqAT5_4VdNJjO9dpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25a166b96b.mp4?token=WhXLvMalsAIBXc94lmuL89vc7xUc-BAaU4zVN8-I7pirWtMTDurXyPbb2Rz1cIU_D5Vi-DGUk8CbiPVkn0loZpALWu0rGmuMVM7VksNpwa7Zv2FAXCVRF1vu4P8DSMo__005fsoxs_GRCZK5IIiA3gRZwjDmchoMpBpU1Xkss5x_w_JZa5ovubFNE619Am1dVFy5i42B5fpbIICMcvqG24kcYGy18msuXlDYab5TX3hPfgdas-Ca8pXO0F69C8RhZcvZ9-saZxwLRUDaAneH9J_5xJTb75waSJ-3tQSqFQf-l0CMN8Lg8Vrz8ww7Xtjh8mcq6uqAT5_4VdNJjO9dpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افشاگری حسن قشقاوی، سخنگوی کمیسیون امنیت ملی مجلس از پیشنهاد همکاری ۵۰۰ میلیارد دلاری جمهوری اسلامی به ترامپ!
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23171" target="_blank">📅 14:51 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23170">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea5de76aae.mp4?token=iQiUS0MgY5wjdxRWtAG8FwTK7c3fygaRwWivyldixFodDXVlxz7R8dinlkZFk6T5Aj34DJTqAwNpgULi9fHzr-w8fIP3m9bpIruy14VFy-mJvTeTqpKVQMHkh0WYgy8um2lTiRGSrEu9cOdt24tVSTsPsAslfUVurkI0CzxQfLobbA0MURzaZZw1uwvsgua0LUv2UnB5fEYrRg7tsX4CjMFbTbVV8nFRawIvmpuvRnWSpCYpW1SyhEPf95NqLZDIzwHWjUyesPj9UtJv6FBaMBxDoRppOfJIPiAghuLCNzo7TaENrDxoXkfh6c27qUsDonTMWeWUVKpejdc63hTLsDfr1bSXjVQNN5a0uxNjflwI4ncUyJuRVbYFYjEB-AHtsmYGgAIXfgfDbXlQ8hbLaxiFNKY9YoCCJrcKQcjl-0P0D6L1-cyygdEaTPMH2tA3jfIH_c123yWrGGT4LmLeQAkuu2jSIgennCrD-SRzCYp-OuNWFowPDPBdiCxCLBhK0QhxV1eNrlyYWNF_uJXArIzczAcyvIPtSbX9rHIyYXgiXkvm7Jc8yvdatdHipEplG_e5BkuWIsVZ798rVDPjRAWFxyLfngcKNDeDksL0x7n8XSgivaDGfF_pAzDfPGp1Farqq5kJWQiZR7KmFudKjtl54wVrj3fxas_gojhKoYM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea5de76aae.mp4?token=iQiUS0MgY5wjdxRWtAG8FwTK7c3fygaRwWivyldixFodDXVlxz7R8dinlkZFk6T5Aj34DJTqAwNpgULi9fHzr-w8fIP3m9bpIruy14VFy-mJvTeTqpKVQMHkh0WYgy8um2lTiRGSrEu9cOdt24tVSTsPsAslfUVurkI0CzxQfLobbA0MURzaZZw1uwvsgua0LUv2UnB5fEYrRg7tsX4CjMFbTbVV8nFRawIvmpuvRnWSpCYpW1SyhEPf95NqLZDIzwHWjUyesPj9UtJv6FBaMBxDoRppOfJIPiAghuLCNzo7TaENrDxoXkfh6c27qUsDonTMWeWUVKpejdc63hTLsDfr1bSXjVQNN5a0uxNjflwI4ncUyJuRVbYFYjEB-AHtsmYGgAIXfgfDbXlQ8hbLaxiFNKY9YoCCJrcKQcjl-0P0D6L1-cyygdEaTPMH2tA3jfIH_c123yWrGGT4LmLeQAkuu2jSIgennCrD-SRzCYp-OuNWFowPDPBdiCxCLBhK0QhxV1eNrlyYWNF_uJXArIzczAcyvIPtSbX9rHIyYXgiXkvm7Jc8yvdatdHipEplG_e5BkuWIsVZ798rVDPjRAWFxyLfngcKNDeDksL0x7n8XSgivaDGfF_pAzDfPGp1Farqq5kJWQiZR7KmFudKjtl54wVrj3fxas_gojhKoYM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ترامپ:
راستش را بخواهید، عمویم احتمالاً بهترینِ تمام دوران بود؛ او ۴۱ یا ۴۲ سال استاد دانشگاه ام‌آی‌تی (MIT) بود و به عنوان یکی از درخشان‌ترین افراد شناخته می‌شد.
بنابراین، اگر به «نظریه وراثت» (یا قدرت ژنتیکی) اعتقاد داشته باشید، من هم از چنین توان ژنتیکی‌ای برخوردارم. من که معتقدم؛ ژنتیک در من وجود دارد. من از هوش مصنوعی هم سر در می‌آورم.
ربات‌ها قرار نیست کنترل امور را به دست بگیرند. هوش مصنوعی قرار نیست بر بقیه جهان مسلط شود. کل این ماجرا یک فریب و حقه است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23170" target="_blank">📅 14:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23169">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کانال ۱۴ : نیروهای دفاعی اسرائیل در حملات دقیق و هدفمند در
خان‌یونس و شهر غزه
، دو عضو ارشد شاخه نظامی حماس را از بین بردند. بر اساس اعلام ارتش اسرائیل، این افراد در
تولید و توسعه تسلیحات، برنامه‌ریزی حملات علیه نیروهای اسرائیلی و بازسازی توان نظامی حماس
فعالیت داشتند و این اقدامات را نقض آتش‌بس می‌داند.
همچنین در روزهای اخیر، ارتش اسرائیل اعلام کرده بود
محمد عبدالرحمن الیزوری، فرمانده تیپ خان‌یونس حماس و عضو شورای رهبری این گروه
نیز در حمله‌ای هدفمند کشته شده است؛ حماس نیز کشته‌شدن او را تأیید کرده ، او در برنامه‌ریزی حمله ۷ اکتبر نقش مهمی داشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23169" target="_blank">📅 14:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23168">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : هیچ هدف‌گیری‌ای داخل شهر مکه مکرمه صورت نگرفته است. دو پایگاه هوایی در نزدیکی مکه قرار دارند: پایگاه هوایی ملک فهد در طائف و پایگاه هوایی ملک عبدالله در جده. هواپیماهای جنگی سعودی از این پایگاه‌ها برای انجام عملیات و بمباران در یمن پرواز می‌کنند. طی روزهای گذشته نیز شاهد تحرکات هواپیماهای جنگی سعودی از پایگاه هوایی ملک فهد در طائف به سمت یمن برای انجام عملیات بمباران بوده‌ایم. از سوی دیگر، شهر جده از نظر تقسیمات اداری در منطقه مکه مکرمه قرار دارد، نه در محدوده خود شهر مکه. بنابراین هنگام انتشار این اخبار، باید میان «شهر مکه مکرمه» و «منطقه مکه مکرمه» تفاوت قائل شد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23168" target="_blank">📅 13:54 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23167">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23167" target="_blank">📅 13:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23166">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دیدبان اتاق جنگ : یاشار پرسنل برج مراقبت امام و معراباد اعتصاب کردن از دیشب تمام پروازا تاخیر دارن هنوز پروازای داخلی رو باند نشستن
مثلا پرواز مشهد به زاهدان باید ساعت ۹ صبح میپریده هنوز رو بانده
@WarRoom
رسانه های رژیم بدون توضیح : در پی تاخیر در تعدادی از پروازهای روز گذشته و نارضایتی مسافران، دادستانی تهران در راستای حفظ حقوق عامه به موضوع ورود کرد.در همین رابطه با موضوع تاخیر پروازها و بررسی آن پرونده قضایی تشکیل شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23166" target="_blank">📅 13:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23165">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یکی از رهبران حزب دموکرات کردستان: یک راکت در داخل اردوگاه حزب در منطقه بالیسان، شمال اربیل، سقوط کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23165" target="_blank">📅 13:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23164">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نیروی دریایی سپاه : تنگه هرمز مسدود است و همچنان تحت کنترل هوشمند نیروی دریایی سپاه  قرار دارد یک تانکر نفتی بزرگ به نام «EL GAIA ال گایا» پس از برخورد با مین‌های دریایی در حین تلاش برای عبور از منطقه ممنوعه در جنوب تنگه هرمز، منفجر شد. تلاش‌ها برای مهار آتش…</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23164" target="_blank">📅 13:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23163">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">هواپیمای دولتی با شناسه پروازی «IRAN06» یک مقام رژیم جمهوری اسلامی از تهران در فرودگاه ریاض، عربستان سعودی به زمین نشست @WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23163" target="_blank">📅 13:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23162">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">آسوشیتدپرس: بحران جدید بر سر محمد اسلامی
: ایران رسماً اتریش را به دلیل جلوگیری از ورود محمد اسلامی، رئیس سازمان انرژی اتمی ایران، به نشست آژانس در وین محکوم کرده است. کمیته شورای امنیت با مخالفت آمریکا حاضر نشده معافیت سفر اسلامی را صادر کند. روسیه از اعتراض ایران حمایت کرده و تهران این اقدام را نقض تعهدات اتریش به‌عنوان کشور میزبان نهادهای سازمان ملل دانسته است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23162" target="_blank">📅 13:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23161">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fazwtN_iF7G-kicLiCPzw5_RE1qTkNckvp30ajqobl3kVKKujbNKnL56Jq5OwgpDx81LdcLSOq0y3KZgjNYGDZXCXhuTZpvlQEOb_D9GOzkGU6yB-QEFNEM7y7UyIgwsMPEW8Zbyl2pLsCY7F06KeGEFS5eYLSYzGkkRzVhFF3tKi52IKAEKKijQq7eub8cn4fy7TRzKyPPH0oqrTzSQtK8wBNv_6ggmmZ3_t_O5RyqB3JWWcs53iXQZAaj6I3UZQOWYEJUQyaLQStMTKiBMr9iZmzYjyILxcmpRz4Yf59HozlHFpfcFmZYuKsn-Q1EscP1j4pZY5o8c6r9msWcijQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا:  گزارشی‌در‌دست بررسی درباره هدف قرار گرفتن یک کشتی با یک پهپاد در تنگه هرمز دریافت شده است. @WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23161" target="_blank">📅 12:47 · 24 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

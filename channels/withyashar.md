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
<img src="https://cdn4.telesco.pe/file/Y_pPS72kVjp-fxgM73Uv4hLPJ6HVnl3m5oOD2Lu1hqZaIXDZltJu9Jg8BrFPtPkSCNW8LzjRJegKne6yrWs3fn5ANIZHwE73R9AIZVwd_M_9hZ5uWe01em77Ze2u_4XsBg1p1oQ8FSw67zOhof2TIFZ84Qs1unIGoDeX4tcFJBwING8nSLFpLbKtC1hL2YZDrym9HkWZwDQfXRrGhfaNMR-5wkyiQLnUvCjNDRni3VbKiiSdN-BREUsICpwWRxTamJL4AbgOsgHtTJiqZikTzDh_73u8RL2qp2beGWYGDUyBFPiUGjt7GLpLo8x_pAt5xuGPqFzsKivxKxYHT2X2Cg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 451K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 09:03:26</div>
<hr>

<div class="tg-post" id="msg-23568">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فیزیک
@WarRoom</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/withyashar/23568" target="_blank">📅 08:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23567">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ویدیو اختصاصی زیبا از دیشب
@WarRoom</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/withyashar/23567" target="_blank">📅 07:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23566">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دیدبان اتاق جنگ : ديشب چندتا موشك خورده ب قايق هاي سپاه داخل قشم  جزايره ناز سوزا ، شايدم قايق صياد های بسیجی بوده که میرن شهپاد های آمریکارو بدزدن بوده معلوم نيست ، ولي برخورد انجام شده
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/withyashar/23566" target="_blank">📅 07:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23565">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebf28a7f1e.mp4?token=NUk7rBO6WUXbuc3nSXTME4LF5n7AN4cqXS7Am-9dab1tFXsf9PvmgboAI9tLS_lD8kOR6RJexEXF26S6ciVKm8AdifMgPAHQmkquBlbvsRgjKV7b08hWKocqFly1O6qjCwtz0UoI0C79K0aTCCgf1di8JR-iJMJNc82rwPEk9O4SGE9pC-3h-29RfGIo1BKkhpa6Dt8prHM4kkh8WFUBxFerAaf1zYvfh3P9RGV4dX6HRwq5pzqzS786GDYXaPC48VJN2hQgcAWPpZNLO3ysCwkS2FiXg6t9QPBO95OoPt7OpswCGoAYhGVxUtSiVPjSvHBK2VNQNCyWPIzTsFX-bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebf28a7f1e.mp4?token=NUk7rBO6WUXbuc3nSXTME4LF5n7AN4cqXS7Am-9dab1tFXsf9PvmgboAI9tLS_lD8kOR6RJexEXF26S6ciVKm8AdifMgPAHQmkquBlbvsRgjKV7b08hWKocqFly1O6qjCwtz0UoI0C79K0aTCCgf1di8JR-iJMJNc82rwPEk9O4SGE9pC-3h-29RfGIo1BKkhpa6Dt8prHM4kkh8WFUBxFerAaf1zYvfh3P9RGV4dX6HRwq5pzqzS786GDYXaPC48VJN2hQgcAWPpZNLO3ysCwkS2FiXg6t9QPBO95OoPt7OpswCGoAYhGVxUtSiVPjSvHBK2VNQNCyWPIzTsFX-bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 49K · <a href="https://t.me/withyashar/23565" target="_blank">📅 06:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23564">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نوراد: یک جنگنده اف-۱۶ یک هواپیمای غیرنظامی را که وارد حریم هوایی ممنوعه کمپ دیوید در مریلند شده بود، رهگیری کرد. این حادثه ساعت ۱۵:۲۰ به وقت تهران (۷:۵۰ صبح به وقت محلی) رخ داد. جنگنده برای برقراری ارتباط با خلبان، شراره‌های هشدار شلیک کرد و سپس هواپیما را…</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/withyashar/23564" target="_blank">📅 06:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23563">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وزارت امور خارجه ایالات متحده:
احتمال تشدید درگیری بین عربستان سعودی و حوثی‌های تحت حمایت ایران , آمریکایی‌های خارج از خاورمیانه باید سفر به این منطقه یا عبور از آن را به طور جدی مورد بازنگری قرار دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/withyashar/23563" target="_blank">📅 06:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23562">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b3db75582.mp4?token=iFIH5e2CGH5kM18oPYdVpxbPYGEbpUUMAChqHxWoEwp-Ro4lyRU1fTXqjUIaMxYzaGRGZZgO0DXD8ZZpATU5kjs4g5LfCLYpro3L6ZCXLbjyJAdkb1PubFwpOJjCU9GAdet0ZQYCNCR25PF9aqy7NU5PZwnp2BstjraWPR5jpNzL9D-mpU4FZ2OmJjlh9WS6WGJRMyb3xEs8Gmzun5J95-lnOedq0q86Bg14HCtfiWog2VsvqYUj8n4Qe-E8D8xI10P4G2C9gPe_axCl6tUs50fxiJedCybm7z-Cfb7n8bfh7OD6gORrXyGWBWMpnMZaIA4uctowOyfKiT6MYWel3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b3db75582.mp4?token=iFIH5e2CGH5kM18oPYdVpxbPYGEbpUUMAChqHxWoEwp-Ro4lyRU1fTXqjUIaMxYzaGRGZZgO0DXD8ZZpATU5kjs4g5LfCLYpro3L6ZCXLbjyJAdkb1PubFwpOJjCU9GAdet0ZQYCNCR25PF9aqy7NU5PZwnp2BstjraWPR5jpNzL9D-mpU4FZ2OmJjlh9WS6WGJRMyb3xEs8Gmzun5J95-lnOedq0q86Bg14HCtfiWog2VsvqYUj8n4Qe-E8D8xI10P4G2C9gPe_axCl6tUs50fxiJedCybm7z-Cfb7n8bfh7OD6gORrXyGWBWMpnMZaIA4uctowOyfKiT6MYWel3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی در رویداد «کوروش کبیر ۲» در تورنتو : «حماسه دی» نتیجه یک هیجان زودگذر نبود؛ پشت آن یک مسیر طولانی و پرهزینه بود. جمهوری اسلامی که در روزهای ۱۸ و ۱۹ دی سقوط خودش را قطعی می‌دید، دست به یکی از بزرگ‌ترین جنایت‌های تاریخ زد. ما امروز از همیشه باتجربه‌تر و مصمم‌تریم. هدفمان مشخص است: سرنگونی جمهوری اسلامی و رسیدن به یک ایران آزاد و آباد. چهار اصل اصلی ما هم روشن است: حفظ تمامیت ارضی ایران، جدایی دین از حکومت، آزادی‌های فردی و برابری همه شهروندان در برابر قانون، و اینکه مردم خودشان با رأی آزاد و عادلانه شکل آینده حکومت ایران را تعیین کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/23562" target="_blank">📅 01:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23561">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سفارت آمریکا در لبنان، بغداد، بحرین و اردن نیز هشدار مشابهی دادند. @WarRoom</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/23561" target="_blank">📅 01:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23560">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سفارت آمریکا در اورشلیم به شهروندان آمریکایی در اسرائیل و منطقه هشدار داده است که با توجه به افزایش تنش‌ها، احتمال بسته‌شدن فضای هوایی، لغو یا اختلال در پروازها و محدودیت‌های تردد وجود دارد و از مسافران خواسته وضعیت پروازها و فعالیت فرودگاه‌ها را مرتب بررسی…</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/23560" target="_blank">📅 01:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23559">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7efc866236.mp4?token=PPgTe4XfFWdP4O2cjCO7rAIjIRZkkTAG98cB9vhBHE9stOApguDsNXoNbhm95W0iMsEQHpiHQ4__XQ9uAlk-4PIZL2aIpRCJouOGE66r1kcp96_7WYYjlok3LKqieUjkwk-_inpBnNwXPqQr5wnjKqcxRE8K8SzcJUdnRVCutmWAnqO-gFgEw9x2nmqJi9SfeXLXoxSE8GIM8v6vHMfgpl2ywqUfvRhdQus9Bss3zwfjjXNWEt3uE9P0fJfCqOvu9fZxddVZehkXytEAwwd2qdR_ia2TfQfOWAuvgVDbmcC52oIvVVrwU6pkfGBPZcNKBOAl9jLQu2RVre0ax85wog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7efc866236.mp4?token=PPgTe4XfFWdP4O2cjCO7rAIjIRZkkTAG98cB9vhBHE9stOApguDsNXoNbhm95W0iMsEQHpiHQ4__XQ9uAlk-4PIZL2aIpRCJouOGE66r1kcp96_7WYYjlok3LKqieUjkwk-_inpBnNwXPqQr5wnjKqcxRE8K8SzcJUdnRVCutmWAnqO-gFgEw9x2nmqJi9SfeXLXoxSE8GIM8v6vHMfgpl2ywqUfvRhdQus9Bss3zwfjjXNWEt3uE9P0fJfCqOvu9fZxddVZehkXytEAwwd2qdR_ia2TfQfOWAuvgVDbmcC52oIvVVrwU6pkfGBPZcNKBOAl9jLQu2RVre0ax85wog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/withyashar/23559" target="_blank">📅 01:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23558">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">رضاتون کجاس حرومی?</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/23558" target="_blank">📅 00:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23557">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1a9813c09.mp4?token=k8EZCuBVAIX8Hwd3yLITiZZ6Dgk105ze0epI9JcsJSBKiqrEoZxa_8UN6gePtgN9p9qSe4GVuMLJXg0jC1TI-B-R0UHZZnGJiPoaRHLxvweTF9sTKPr8FRYmYWcy2awJ6O4b2l4Gl9yKGZh99ZMRAW9asBCI9Zmtl11yIrGz5BsKDIEDzFpI_71a5r6GOyODqdOQgfrj-b2_zZWem2qugEUrGvkN6vV4Shdg0K9U_jyo_hpTZIDxTWyy4QiYQalc3z1xr4M5qGHudnW6uKIAqUDjl98gzzPzuQTJ7ya-LLydh2UdGBncCVVvF1VMBSmNb6usxWsWMfPEZP3IR9E_CU5bCFypcy0l9IePHDNQ7f_Ozdf6ALKbY4zCq216cx69ONxSyRE_su25dprPSUW0N2lEH8wURs-yw-7L4GQrhfp6NGz7nvfTBQA4-xneJ_ljS0ZTjWJKeoJ-TyvPphmtEJeLprYpLmQioMOxA0PaqyZyZiZtU_d_iHNlJcxCFpLsof2D229OSHrtWdT9pZjg4MvPfy7X7XqQo9T3i9Wq7jE8IlLesHqw4-FKWIgOu9Cr-xu7XcRuLdbpHO_4mr4yAPHzX1p_or74DymQull4WtJ6781HVamMRdeqcLrCUTcsHBQMJ3etZfdr5DcduzmIhsa7m0D2G4L94toS1Pxol8k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1a9813c09.mp4?token=k8EZCuBVAIX8Hwd3yLITiZZ6Dgk105ze0epI9JcsJSBKiqrEoZxa_8UN6gePtgN9p9qSe4GVuMLJXg0jC1TI-B-R0UHZZnGJiPoaRHLxvweTF9sTKPr8FRYmYWcy2awJ6O4b2l4Gl9yKGZh99ZMRAW9asBCI9Zmtl11yIrGz5BsKDIEDzFpI_71a5r6GOyODqdOQgfrj-b2_zZWem2qugEUrGvkN6vV4Shdg0K9U_jyo_hpTZIDxTWyy4QiYQalc3z1xr4M5qGHudnW6uKIAqUDjl98gzzPzuQTJ7ya-LLydh2UdGBncCVVvF1VMBSmNb6usxWsWMfPEZP3IR9E_CU5bCFypcy0l9IePHDNQ7f_Ozdf6ALKbY4zCq216cx69ONxSyRE_su25dprPSUW0N2lEH8wURs-yw-7L4GQrhfp6NGz7nvfTBQA4-xneJ_ljS0ZTjWJKeoJ-TyvPphmtEJeLprYpLmQioMOxA0PaqyZyZiZtU_d_iHNlJcxCFpLsof2D229OSHrtWdT9pZjg4MvPfy7X7XqQo9T3i9Wq7jE8IlLesHqw4-FKWIgOu9Cr-xu7XcRuLdbpHO_4mr4yAPHzX1p_or74DymQull4WtJ6781HVamMRdeqcLrCUTcsHBQMJ3etZfdr5DcduzmIhsa7m0D2G4L94toS1Pxol8k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون شاهزاده در همایش کوروش ۲ در کانادا، همچنین ۲ جنرال کانادایی هم در تصویر دیده میشوند
@WarRoom</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/23557" target="_blank">📅 00:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23556">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmin</strong></div>
<div class="tg-text">رضاتون کجاس حرومی?</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/withyashar/23556" target="_blank">📅 00:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23555">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">جنوب لبنان صدای ناله های حسن خرسی میاد
@WarRoom</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/23555" target="_blank">📅 00:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23554">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">چند گزارش از فعالیت کوتاه پدافند شیراز
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23554" target="_blank">📅 00:29 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23553">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سفارت آمریکا در اورشلیم به شهروندان آمریکایی در اسرائیل و منطقه هشدار داده است که با توجه به افزایش تنش‌ها، احتمال
بسته‌شدن فضای هوایی، لغو یا اختلال در پروازها و محدودیت‌های تردد
وجود دارد و از مسافران خواسته وضعیت پروازها و فعالیت فرودگاه‌ها را مرتب بررسی کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23553" target="_blank">📅 00:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23552">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پدافند شرق تحرک ریزی انجام داد قطع شد
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23552" target="_blank">📅 23:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23551">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">انتخابات پارلمانی روسیه در حالی ادامه دارد که مقام‌های روس از
حملات سایبری به سامانه رأی‌گیری و شبکه‌های ارتباطی
خبر داده‌اند. مسکو اوکراین را متهم کرده، اما برای این اتهام مدرکی ارائه نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23551" target="_blank">📅 23:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23550">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">نوراد: یک جنگنده
اف-۱۶
یک هواپیمای غیرنظامی را که وارد
حریم هوایی ممنوعه کمپ دیوید
در مریلند شده بود، رهگیری کرد. این حادثه ساعت
۱۵:۲۰ به وقت تهران
(۷:۵۰ صبح به وقت محلی) رخ داد. جنگنده برای برقراری ارتباط با خلبان،
شراره‌های هشدار
شلیک کرد و سپس هواپیما را به‌سلامت از منطقه خارج کرد.
دونالد ترامپ
هنگام این حادثه در کمپ دیوید حضور داشت
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/23550" target="_blank">📅 22:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23549">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">رویترز: دونالد ترامپ اعلام کرد آمریکا یک «نیروی هوش مصنوعی» تشکیل خواهد داد؛ طرحی که به گفته او مشابه نیروی فضایی است که در دوره اول ریاست‌جمهوری‌اش ایجاد کرد. ترامپ همچنین گفت به‌زودی یک «تزار هوش مصنوعی» برای نظارت بر این طرح منصوب خواهد کرد. هنوز مشخص نیست این نیرو یک شاخه نظامی مستقل خواهد بود یا یک نهاد فدرال برای نظارت و توسعه هوش مصنوعی.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/23549" target="_blank">📅 22:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23548">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">رویترز: کره‌جنوبی اینبار اعلام آمادگی کرد در بازگشایی هرمز مشارکت کند
؛ وزیر خارجه کره‌جنوبی در دیدار با مارکو روبیو اعلام کرده سئول آماده است «مشارکت اساسی» در بازگرداندن عبور آزاد کشتی‌ها از تنگه هرمز داشته باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/23548" target="_blank">📅 21:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23547">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">آسوشیتدپرس: زنان بدون حجاب در یک مسابقه دو در تهران شرکت کردند
؛ صدها زن بدون حجاب اجباری در یکی از بزرگ‌ترین نمایش‌های نافرمانی اجتماعی در سال‌های اخیر در یک مسابقه دو در بوستان ولایت تهران شرکت کردند. همزمان در همان روز تجمعی حکومتی در تهران برگزار شد و زنان محجبه در حمایت از حکومت و جنگ حضور داشتند.وزارت ورزش از یک ماه قبل مجوز داده بود ولی دادستانی تهران اعلام کرد علیه عوامل و دست‌اندرکاران برگزاری مسابقه دو در بوستان ولایت اعلام جرم کرده و پرونده قضایی تشکیل داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/23547" target="_blank">📅 21:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23546">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">الجزیره: ۱۱ سرباز سوری در انفجار انبار مهمات کشته شدند
؛ انفجار در یک موضع نظامی در منطقه عیّاش در استان دیرالزور رخ داده و ۹ سرباز دیگر زخمی شده‌اند. علت انفجار هنوز مشخص نیست و تحقیقات ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23546" target="_blank">📅 21:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23545">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94774fe4a2.mp4?token=k6s5or3w3pGBPnxjmAUwTingOo6fv6hgytcbHu8zpqTs3nc3X12aFx7heEMI2cCwYNPAiH3K16Z7ha33yI7vl51SFp6nQx_Gj35QZs_aZE5CoKchqyRquLE8wq6Xv4x50cWJKO6B7SkecCsRmgLYT4SS1HaM2DCq6-YSPtk9RJJvR2HhZ2FXVz0TGnfwpOiNyBHve7xIibAt2oF9uFk8T9XT7OTS33CGJWZYLwr5S_uka_ZshEu_4moGLNj5hQaeWzBxlFARmllPTSgHMh6ueR0A9r4zGzdgoV-M2vDT0VYoNpQTe5a4jwLUEG4wDnv3ZihJPeVe8pUfRkrrajuTk4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94774fe4a2.mp4?token=k6s5or3w3pGBPnxjmAUwTingOo6fv6hgytcbHu8zpqTs3nc3X12aFx7heEMI2cCwYNPAiH3K16Z7ha33yI7vl51SFp6nQx_Gj35QZs_aZE5CoKchqyRquLE8wq6Xv4x50cWJKO6B7SkecCsRmgLYT4SS1HaM2DCq6-YSPtk9RJJvR2HhZ2FXVz0TGnfwpOiNyBHve7xIibAt2oF9uFk8T9XT7OTS33CGJWZYLwr5S_uka_ZshEu_4moGLNj5hQaeWzBxlFARmllPTSgHMh6ueR0A9r4zGzdgoV-M2vDT0VYoNpQTe5a4jwLUEG4wDnv3ZihJPeVe8pUfRkrrajuTk4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق روایت و ویدیو منتشرشده، چند جوان در خیابان دانشگاه زاهدان با خودرو در حال تردد بودند که ناگهان گلوله‌ای به سمت خودرو شلیک شد؛ گلوله گردن سرنشین صندلی شاگرد را خراش داد و از کنار گوش سرنشین عقب عبور کرد. گفته شده حال افراد داخل خودرو خوب است. در مقابل،
خبرگزاری فارس
گزارش داده بامداد جمعه حدود ساعت ۱۲:۳۰، نیروهای امنیتی به یک خودروی پژو مشکوک شدند و پس از مشاهده سلاح در خودرو، درگیری رخ داد که در جریان آن
۳ نفر کشته شدند
. درباره ارتباط این دو روایت، اطلاعات مستقلی منتشر نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23545" target="_blank">📅 21:11 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23544">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">واشینگتن پست: رئیس‌جمهور ترامپ در اظهارات علنی خود همواره تأکید کرده است که سیاست‌های انتخاباتی میان‌دوره‌ای بر تصمیمات او درباره ایران تأثیری ندارند.
اما ترامپ در محافل خصوصی نشان داده است که می‌داند تصمیماتش در شکل‌گیری فضای سیاسی نامساعدی که حزبش با آن مواجه است، نقش داشته‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23544" target="_blank">📅 21:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23543">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ: متأسفانه دیوان عالی آمریکا شجاعت لازم برای «دوباره بزرگ کردن آمریکا» را نداشته است. آنها در شش ماه گذشته با تصمیم‌های سیاسی، نادرست و مضحک خود درباره تعرفه‌ها و حق شهروندی از طریق تولد، تریلیون‌ها دلار به ایالات متحده خسارت زده‌اند و برای همیشه به نحوه شهروند شدن افراد در کشور بزرگ ما آسیب وارد کرده‌اند. این فصل غم‌انگیزی در تاریخ آمریکا بوده، اما ما پیروز خواهیم شد.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23543" target="_blank">📅 21:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23542">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBvq1klMmSxPqPE73P7FDxrSEy-2PlIcFxEwBAkTtSiiNosom113tdLDkfZPJnkphSNXlUctRWj2y-efCsIG-TC5upr6iPGRxaRD8T_lF83YJ7bpGMB7J8eJV_u-i6va2eZ33JoAK6a4T61aw6L7djTTdMZtn1EL4dl02m_3ocFyG0I33-A0u6H4K6PNeYfFcnN0hYzv73M6P1Xg6JEYx1KsqoZF5zS4AMxsWi9jLwa24u0xrEmX11vt8nEBu1_kkT_XSPMrWWvUHYp6KFOQ7Et_6K9qgb3XcxeKX9P5uLCazyg4D9TC5_dlpUOAfDSF0YQLgAFTLpYPHGnErHuwSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رژه جن فدا ها ، اخطار اگه تصویرو زوم کنید ‌شب ادراری‌ میگیرن
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23542" target="_blank">📅 20:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23541">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کانال 13 اسرائیل:
قطر شروط تهران برای پایان جنگ را به آمریکا منتقل کرده و ایران اکنون منتظر واکنش دونالد ترامپ است
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23541" target="_blank">📅 20:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23540">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خبرگزاری i24news : بنیامین نتانیاهو سفر خود به آمریکا را کوتاه کرده و برخلاف برنامه قبلی، به تگزاس نمی‌رود و دیدار برنامه‌ریزی‌شده با ایلان ماسک نیز لغو شده است. نتانیاهو اکنون قرار است پنجشنبه مستقیماً به نیویورک برود، در مجمع عمومی سازمان ملل سخنرانی کند و بلافاصله پس از آن به اسرائیل بازگردد. در برنامه فعلی همچنین دیداری با دونالد ترامپ وجود ندارد؛ مقام‌های آمریکایی دلیل آن را محدودیت زمانی و تفاوت برنامه سفر دو رهبر اعلام کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23540" target="_blank">📅 20:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23539">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db86a12457.mp4?token=PbSUUtf8FVDiUpayrVkMWg6oeCqITFw0K66u8KCl39bctEp523X8GHUay_wDB-Fk_RetAnGIiPcIin5vUKUkD_MsOtiJ1rxTcvESnQU1eTHc3S0uNzbKJYhfriZPaAo98ameQA37mGpViSwHB9WuTkhAe6oTZxs9LcA_hTXiXDhwOk_mInCNxqhvewkEj_CLw2s9spWodv4sRs3w5jqTQWpFij_9akoq-TkNw5WE9_x1fXQkKClNIz5NbOHyAyg51zFJ1gxoMYxkqyNOzJGYFG60yh7b9DByBGzEpp04SESIIVGOZ37kzKzndXKnieMweDuJCMYuRgRpcRUK0sBB0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db86a12457.mp4?token=PbSUUtf8FVDiUpayrVkMWg6oeCqITFw0K66u8KCl39bctEp523X8GHUay_wDB-Fk_RetAnGIiPcIin5vUKUkD_MsOtiJ1rxTcvESnQU1eTHc3S0uNzbKJYhfriZPaAo98ameQA37mGpViSwHB9WuTkhAe6oTZxs9LcA_hTXiXDhwOk_mInCNxqhvewkEj_CLw2s9spWodv4sRs3w5jqTQWpFij_9akoq-TkNw5WE9_x1fXQkKClNIz5NbOHyAyg51zFJ1gxoMYxkqyNOzJGYFG60yh7b9DByBGzEpp04SESIIVGOZ37kzKzndXKnieMweDuJCMYuRgRpcRUK0sBB0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارک لوین بازنشر کرد
صحبتهای
، رندی فاین، نماینده کنگره آمریکا:
شبکه‌های اجتماعی، اینفلوئنسرها و اعتراضات، همگی برای
بی‌ثبات کردن آمریکا از داخل
طراحی شده‌اند. بخش زیادی از این اقدامات توسط
روسیه، چین، ایران، ترکیه و قطر
تأمین مالی می‌شود. ما باید همین حالا درباره این موضوع صحبت کنیم تا مردم
قبل از اینکه خیلی دیر شود، بیدار شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23539" target="_blank">📅 19:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23538">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">صدای انفجارهای کنترل شده در ملارد
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23538" target="_blank">📅 19:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23537">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">آکسیوس: جنگ ایران باعث افزایش شدید قیمت بنزین و گازوئیل در سراسر جهان شده و فشار اقتصادی و تورمی را حتی به کشورهایی که مستقیماً در جنگ دخالت ندارند منتقل کرده است. دولت‌ها اکنون با افزایش هزینه سوخت و فشار عمومی مواجه‌اند و در صورت ادامه جنگ، احتمال تشدید این فشارها وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23537" target="_blank">📅 19:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23536">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">محسن رضایی به شبکه الجزیره گفت:
از نظر واشنگتن، پذیرش شرایط ما برای خروج از جنگ، کار درستی است. تهدیدات ترامپ هیچ نتیجه‌ای نخواهد داشت و ما برای یک جنگ قاطع آماده هستیم. ارزیابی‌ها و محاسبات رئیس جمهور آمریکا درباره ایران نادرست بود و جنگ با تحریک نتانیاهو آغاز شد.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23536" target="_blank">📅 18:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23535">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd58a1e73c.mp4?token=g_BBbtC-iP1QXmkhbTYk0OHkBPwT3j-h4Matfb7c1mPYaUx_Y43VOArrqZAL4CMzNX_4HbvayJ_JUYklN-yb4lxPbhnb0TqhqzLB6MvmWEJIs7ygAxr3mkLNCRCo9PUyUoBtsAAlRbDWvXNTh0xnHlDr791fCpVfYIxJxw_S-NM5kBP6BeaiE52m52_Y9r4DTDUjXC6tgAy1wGgKUvzi_8ZXS0C_-kHy3GWyqH8qXqN9g9CDRmyE3XWMejxzw0kqOcse2AhKwH6GLFw-xqD-Y7Nk7TsM5k8GNxzNzqwkri5p1JPLCS9aXJzUapqKWHHCaJ9y_XvHqLZ2mskZI08SUbn1ZpRJb0_OWf-_m4qND_VH5ewW0_amXxYpguHfvmMB5nY6DRW37DUNxa78wdqC_NT0_BwZmwiyFGO_jOmLUWMO2VSWOt1nmcj00eVKtIoZ3hZGJ2XHeEuizwr_Rv_AA9n2OjsMjEJ6ctfzWaWPxfu6Uq3W2kUww5AMVfIEXV1eluxbUzDEqOjiQuzgbSPoSLtBH2mYLeavZsMi3NV3SBWpfad4l5Hfi7eSUAJJ4Q2AaOgLiMdEmZ-YDuGAOcPuSFdRAjKiSYqigLmSo1coAd2gySsvnAZTC-eH9QxGtcKBCRT9VUjnhFzb-46_11oJVu6f3cEkfsxthPK6pNFkEkc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd58a1e73c.mp4?token=g_BBbtC-iP1QXmkhbTYk0OHkBPwT3j-h4Matfb7c1mPYaUx_Y43VOArrqZAL4CMzNX_4HbvayJ_JUYklN-yb4lxPbhnb0TqhqzLB6MvmWEJIs7ygAxr3mkLNCRCo9PUyUoBtsAAlRbDWvXNTh0xnHlDr791fCpVfYIxJxw_S-NM5kBP6BeaiE52m52_Y9r4DTDUjXC6tgAy1wGgKUvzi_8ZXS0C_-kHy3GWyqH8qXqN9g9CDRmyE3XWMejxzw0kqOcse2AhKwH6GLFw-xqD-Y7Nk7TsM5k8GNxzNzqwkri5p1JPLCS9aXJzUapqKWHHCaJ9y_XvHqLZ2mskZI08SUbn1ZpRJb0_OWf-_m4qND_VH5ewW0_amXxYpguHfvmMB5nY6DRW37DUNxa78wdqC_NT0_BwZmwiyFGO_jOmLUWMO2VSWOt1nmcj00eVKtIoZ3hZGJ2XHeEuizwr_Rv_AA9n2OjsMjEJ6ctfzWaWPxfu6Uq3W2kUww5AMVfIEXV1eluxbUzDEqOjiQuzgbSPoSLtBH2mYLeavZsMi3NV3SBWpfad4l5Hfi7eSUAJJ4Q2AaOgLiMdEmZ-YDuGAOcPuSFdRAjKiSYqigLmSo1coAd2gySsvnAZTC-eH9QxGtcKBCRT9VUjnhFzb-46_11oJVu6f3cEkfsxthPK6pNFkEkc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
کنگره از چه زمانی باید وارد عمل شود و درباره جنگ ایران تصمیم‌گیری کند؟
مایک جانسون، رئیس مجلس نمایندگان آمریکا:
ببینید، دولت این را یک جنگ در حال انجام نمی‌داند. چنین چیزی نیست. آنها در تلاش هستند یک عملیات را به پایان برسانند؛
عملیات «خشم حماسی» که موفقیتی بزرگ بود.
من فکر نمی‌کنم در شرایط فعلی نیازی باشد
دموکرات‌های مارکسیست لیبرال در کنگره
به فرمانده کل نیروهای مسلح بگویند با ارتش چه کار کند.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23535" target="_blank">📅 18:37 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23534">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75e72d7fb2.mp4?token=dYfq_qKCnhQftbX6bQE4wjHs6nHKfdJUwze3sBhP-8vFk69JbBcFbbS5VFxl8WDRaadcUe4wOhpZA92hshdYxDvyg1hWv6WG7-tHOJZMAF02i7rC_xRP7uuEEG4T6hs_obhOj1AZ5NZBRcKya1G90Vec8kMeGXIwnDOGzI-NiO6Q74G3wfZs6PX9Bgh0vMHYd68GPkCRw1bauB5DZ8bTHsQSt0M7h2SqmmFGJMwIVqWt3eICc00JErfbkXeOPn_-RrOjLeM4pkgzRsBN6Zz4a2EaBndZvYRAiRFqTMdOs8KkXTTkRinOYGRrBEV5Zxwg372wFWJ5IL-50GHEPge1-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75e72d7fb2.mp4?token=dYfq_qKCnhQftbX6bQE4wjHs6nHKfdJUwze3sBhP-8vFk69JbBcFbbS5VFxl8WDRaadcUe4wOhpZA92hshdYxDvyg1hWv6WG7-tHOJZMAF02i7rC_xRP7uuEEG4T6hs_obhOj1AZ5NZBRcKya1G90Vec8kMeGXIwnDOGzI-NiO6Q74G3wfZs6PX9Bgh0vMHYd68GPkCRw1bauB5DZ8bTHsQSt0M7h2SqmmFGJMwIVqWt3eICc00JErfbkXeOPn_-RrOjLeM4pkgzRsBN6Zz4a2EaBndZvYRAiRFqTMdOs8KkXTTkRinOYGRrBEV5Zxwg372wFWJ5IL-50GHEPge1-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کلاغ پر بازی کردن ناتنیاهو در سخنرانی :
نتانیاهو: حسن نصرالله کجاست؟
جمعیت: حذف شد.(پرر)
نتانیاهو: یحیی سنوار کجاست؟
جمعیت: حذف شد.(پررر)
نتانیاهو: اسماعیل هنیه کجاست؟
جمعیت: حذف شد.(پرررر)
نتانیاهو: علی خامنه ای کجاست؟
جمعیت: حذف شد(پررررر)
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23534" target="_blank">📅 17:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23533">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">رویترز(کل ماجرا): اروپا در پی تشدید حملات روسیه به اوکراین وارد مرحله تازه‌ای از آماده‌باش شده است. روسیه حملات موشکی و پهپادی را افزایش داده و کشورهای اروپایی نگران سرایت جنگ به خاک ناتو، حملات سایبری، خرابکاری و حملات پهپادی هستند. لهستان امروز برای احتیاط جنگنده‌ها و پدافند هوایی خود را به حالت آماده‌باش درآورد، در حالی که حریم هوایی این کشور نقض نشده بود. بریتانیا از مردم خواسته برای شرایط اضطراری آب، غذای ماندگار و وسایل ضروری در خانه داشته باشند؛ سوئیس نیز راهبرد امنیتی جدیدی تصویب کرده و ذخیره آب و غذا برای شرایط بحرانی را توصیه کرده است. فرانسه و دیگر کشورهای اروپایی نیز حفاظت از زیرساخت‌های حیاتی و توان دفاعی خود را افزایش داده‌اند. با وجود این اقدامات، اروپا رسماً وارد جنگ نشده است؛ اما سطح آمادگی نظامی و غیرنظامی در برابر احتمال گسترش جنگ روسیه و اوکراین و بحران‌های منطقه‌ای به شکل محسوسی افزایش یافته است.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23533" target="_blank">📅 17:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23532">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b85e47807.mp4?token=cMWmA5kK94SNhWw5xfmdcJ53YVbWZTGSNLuwq46_VBi3WQR8k2JAvZsKBZLBZ_qCRBK_IxIw6-Irpr7JL1dwLGreGF4JYd2cdiLOjM-irm0CrYdVwYHS6sKoxWmoPe20tn6tvjatq0Cj3xhkDmBAE_ojh_6yqcEC2jJfB8b6tplQeJUHkuNHaamMQqbBXQWbPom-6tj7D9nhR1fmKhTgcsdMZSMykpdBFYKfcusLUrAe6SDcKqkajTfW7dpvhLf6fdlD_OLM0ftKR3R0R0S9yOOraYl1OOR-XCm1t9LmBZaFrnqZ0iX0jE7RehXng8OvCW3PV5BotL2uKqdodu6opQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b85e47807.mp4?token=cMWmA5kK94SNhWw5xfmdcJ53YVbWZTGSNLuwq46_VBi3WQR8k2JAvZsKBZLBZ_qCRBK_IxIw6-Irpr7JL1dwLGreGF4JYd2cdiLOjM-irm0CrYdVwYHS6sKoxWmoPe20tn6tvjatq0Cj3xhkDmBAE_ojh_6yqcEC2jJfB8b6tplQeJUHkuNHaamMQqbBXQWbPom-6tj7D9nhR1fmKhTgcsdMZSMykpdBFYKfcusLUrAe6SDcKqkajTfW7dpvhLf6fdlD_OLM0ftKR3R0R0S9yOOraYl1OOR-XCm1t9LmBZaFrnqZ0iX0jE7RehXng8OvCW3PV5BotL2uKqdodu6opQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دریادار برد کوپر، فرمانده سنتکام:
ما با تمرکز کامل و جدیت به کار خود ادامه می‌دهیم و با نهادهای مختلف دولت آمریکا، کشورهای عضو شورای همکاری خلیج فارس و همچنین شرکت‌های بیمه و کشتیرانی همکاری می‌کنیم تا
حجم تردد کشتی‌ها از تنگه هرمز افزایش پیدا کند.
این تلاش‌ها نتیجه داده است؛
حجم عبور نفت خام، محموله‌های تجاری و گاز طبیعی مایع‌شده در دو هفته گذشته، از هر زمان دیگری در شش ماه اخیر بیشتر بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23532" target="_blank">📅 16:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23531">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b5c1e187f.mp4?token=TVTtooM6et3LTf7sUlKsT5J-k3CIrDKFSGlI6iKeXoCP2c6xKfgcqcIN5M3qw5liDRBPTVDcqPdZd6HFRG7yqtKetP_bu9iZ09aXB4Sfev_eN643T09n0o7KoftVaPtW8cGL5fLGuUx9_cId_5_zTduf3Jy97ptAK7nrdXQ0LhDK0HLv9Gh0yZiLS1D78rEldotjs-Cms_jgEzv9gxSY1GqAq6FBsuLfO2GYbGGQTNFsQS_1xn7y8F8qjrG1Tm8Y-CbsvCbV3Y3ta2E_JZQw0jnknTsXR2NijZuGQyU_ZzuSI_b5cH0W6_JOm3fPEBbdFjTCUE5EDnkJS2kKjbXN6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b5c1e187f.mp4?token=TVTtooM6et3LTf7sUlKsT5J-k3CIrDKFSGlI6iKeXoCP2c6xKfgcqcIN5M3qw5liDRBPTVDcqPdZd6HFRG7yqtKetP_bu9iZ09aXB4Sfev_eN643T09n0o7KoftVaPtW8cGL5fLGuUx9_cId_5_zTduf3Jy97ptAK7nrdXQ0LhDK0HLv9Gh0yZiLS1D78rEldotjs-Cms_jgEzv9gxSY1GqAq6FBsuLfO2GYbGGQTNFsQS_1xn7y8F8qjrG1Tm8Y-CbsvCbV3Y3ta2E_JZQw0jnknTsXR2NijZuGQyU_ZzuSI_b5cH0W6_JOm3fPEBbdFjTCUE5EDnkJS2kKjbXN6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دریادار برد کوپر، فرمانده سنتکام:
نیروهای سنتکام طی دو ماه گذشته از خروج
بیش از یک میلیارد بشکه نفت خام
از خلیج فارس از طریق تنگه هرمز پشتیبانی کرده‌اند. سنتکام همچنین با تأمین حفاظت و هماهنگی، به عبور
بیش از ۲ هزار کشتی تجاری
از تنگه هرمز کمک کرده است.
مسیرهای اصلی عبور در تنگه هرمز عاری از مین هستند
و هزاران کشتی از این تنگه عبور کرده‌اند. بیش از
یک میلیارد بشکه نفت خام
از کشورهای شریک در خلیج فارس از طریق تنگه هرمز صادر شده، در حالی که
ایران به لطف محاصره کامل و مستحکم آمریکا، حتی یک بشکه نفت هم صادر نکرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23531" target="_blank">📅 16:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23530">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خبرگزاری i24NEWS: جزئیات بیشتری از پرونده مرحوم حسین پدران منتشر شده؛ طبق روایت مقام‌های ایرانی، او از طریق واتس‌اپ با فردی که خود را «بن» معرفی کرده بود ارتباط داشته و متهم به انتقال اطلاعات حساس نظامی به موساد شده است.  @WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23530" target="_blank">📅 16:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23529">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">حکم اعدام حسین پدران، فرزند حمیدرضا اجرا شد؛ رسانه‌های ایران به نقل از مرکز رسانه قوه قضاییه اعلام کرده‌اند که او به اتهام همکاری اطلاعاتی با موساد و انتقال اطلاعات درباره سایت‌های موشکی و نظامی در اصفهان محکوم شده بود. @WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23529" target="_blank">📅 16:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23528">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">رویترز: بانک ملت تنها تحول مالی امروز نیست؛ ترکیه در هفته‌های اخیر تحت فشار واشنگتن برای تشدید محدودیت‌های اقتصادی علیه ایران قرار گرفته و لغو مجوز بانک ملت در همین فضای فشار اقتصادی انجام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23528" target="_blank">📅 15:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23527">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23527" target="_blank">📅 14:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23526">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝘼𝙢𝙞𝙧 𝙎𝙩𝙧𝙞𝙠𝙚</strong></div>
<div class="tg-text">داداش دیدی شاهزاده یه چیزی میدونست از اعتصاب کردا حمایت نکرد</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23526" target="_blank">📅 14:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23525">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">استوری پدر ریاکار مهسا امینی با پرچم تجزیه‌طلبهای کردستان که خط قرمز ما محسوب میشه. این استوری هم‌اکنون پاک شده. توضیحات رو در وویس براتون میدم. پرچم ایران فقط شیر و خورشید است و این خط قرمز ماست. @WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23525" target="_blank">📅 14:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23524">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/363a420621.mp4?token=RQil0y_A2Tkq3vdZMn-ULNGVzOxybAhqgnfPuUgFExINsysEyp1IwzMnR2XP8WJOXhNJy2rSAtEk1k1MowlDtu2RquC51zyjQ8qxOFjS7jMfXJtCnlV7Q3iB7JKkfbXUl9yJYUTmsnbpubAiUM0XeMwJF4LcV1CfhzPXXkmG6Z-wgH62KHyn5XMohYIH48r5xCRYcv0YDFqMmtmfLFf6L5Np3BunNfWxp5CHaRTiYaRoZR5r5mTNjBJD4CxSB3kbfyLEO2_zVFG3gYw5Y6PNVFC33dP62w_7pLKqYZX4-T8MwGZs_yxOxpZ8vQQD3KTRPMFW_fp9k8Um1A-ARGuNDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/363a420621.mp4?token=RQil0y_A2Tkq3vdZMn-ULNGVzOxybAhqgnfPuUgFExINsysEyp1IwzMnR2XP8WJOXhNJy2rSAtEk1k1MowlDtu2RquC51zyjQ8qxOFjS7jMfXJtCnlV7Q3iB7JKkfbXUl9yJYUTmsnbpubAiUM0XeMwJF4LcV1CfhzPXXkmG6Z-wgH62KHyn5XMohYIH48r5xCRYcv0YDFqMmtmfLFf6L5Np3BunNfWxp5CHaRTiYaRoZR5r5mTNjBJD4CxSB3kbfyLEO2_zVFG3gYw5Y6PNVFC33dP62w_7pLKqYZX4-T8MwGZs_yxOxpZ8vQQD3KTRPMFW_fp9k8Um1A-ARGuNDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی دیشب رفت تجمعات
😂
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23524" target="_blank">📅 14:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23523">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بانک مرکزی واردات خودروهای لوکس را متوقف می‌کند
بانک مرکزی اعلام کرده است که برای واردات خودروهای لوکس مانند لکسوس LX700، مرسدس‌بنز کلاس S و بی‌ام‌و سری ۷، کد ساتا صادر نمی‌شود.کد ساتا مجوزی است که پس از تأیید منشأ ارز صادر می‌شود و برای ترخیص خودرو از گمرک ضروری است. بنابراین، خودروهای مشمول این تصمیم تا زمان دریافت مجوز امکان ترخیص نخواهند داشت.این تصمیم برای جلوگیری از سودجویی در واردات خودروهای گران‌قیمت و کاهش فشار بر بازار ارز گرفته شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23523" target="_blank">📅 14:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23522">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ان‌بی‌سی: مارکو روبیو، وزیر خارجه آمریکا، برخلاف جی‌دی ونس، در طول جنگ از قرار گرفتن در کانون توجهات درباره جنگ نامحبوب ایران اجتناب کرده است؛ رویکردی که ممکن است از نظر سیاسی به سود او باشد. به گفته منابع نزدیک به روبیو، او در تمام مدت جنگ یک «دست پنهان» بوده و در تدوین راهبرد دولت ترامپ نقش داشته است. این منابع همچنین می‌گویند احتمال نامزدی روبیو برای ریاست‌جمهوری در آینده می‌تواند همچنان روی میز باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23522" target="_blank">📅 13:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23521">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حریق در انبار کباب‌سرای محمد در تهران، در خیابان دولت (کلاهدوز)، نرسیده به سه راه نشاط (پلاک ۳۳۵) @WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23521" target="_blank">📅 13:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23520">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23520" target="_blank">📅 13:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23519">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گزارش‌ها از کشته شدن ژنرال فراق العسّار از فرماندهان ارشد حوثی‌ها حکایت دارد. این گروه در بیانیه‌ای از او به‌عنوان فرمانده تیپ یکم کماندو یاد کرده است. العسّار در جریان حمله‌ای در جبهه کَهْبوب، در نزدیکی تنگه باب‌المندب، کشته شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23519" target="_blank">📅 13:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23518">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79606f3b2f.mp4?token=Mg15zS6o9ayD4Jp7Czp7aX8pKhyX_WDAPpPMXQjkR7YP1ckdgDOvlFtuvEYAo-MO1JguEYQFfXOhuvOLxGySceLe52k-uDM12eNA_5wxiiUQf1iTOsUVhKpkOPpfcsniq2V06600m0hElskX1BcQrO-kRtaDNxmZ2m5_4bwmgBDpkluctH_nhk_6IpE7WPg2DbvNvAFg7WacFil5dKG5GXTQqme1JBTJDc36asjaOIwHcWAlEmAfDizLj7XfSA3kX_t2P_iZPk6kE_FFN0EqyuMNxrgg5IIyne_pUDh-bbIF0dXA6_CyWXZjdXmgRMjcVeNC3QOJOy5bZ8oSeR47vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79606f3b2f.mp4?token=Mg15zS6o9ayD4Jp7Czp7aX8pKhyX_WDAPpPMXQjkR7YP1ckdgDOvlFtuvEYAo-MO1JguEYQFfXOhuvOLxGySceLe52k-uDM12eNA_5wxiiUQf1iTOsUVhKpkOPpfcsniq2V06600m0hElskX1BcQrO-kRtaDNxmZ2m5_4bwmgBDpkluctH_nhk_6IpE7WPg2DbvNvAFg7WacFil5dKG5GXTQqme1JBTJDc36asjaOIwHcWAlEmAfDizLj7XfSA3kX_t2P_iZPk6kE_FFN0EqyuMNxrgg5IIyne_pUDh-bbIF0dXA6_CyWXZjdXmgRMjcVeNC3QOJOy5bZ8oSeR47vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختر پزشکیان: من هم جان‌فدا هستم
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23518" target="_blank">📅 13:11 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23517">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23517" target="_blank">📅 13:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23516">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23516" target="_blank">📅 13:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23515">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23515" target="_blank">📅 13:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23514">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝘼𝙧𝙖𝙙</strong></div>
<div class="tg-text">داداش یعنی چی که میگی تجزیه طلب
تو حق مردم کردستان رو بده بهشون چرا بخوان جدا شن؟؟
وقتی رضا پهلوی دوم بتونه برابری ایجاد کنه و عدالت ، هیچ قومی خواستار جدایی نیست بلکه اونایی هم که هستن میشن طرفدارش و طرفدار کشور.....</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23514" target="_blank">📅 13:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23513">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromℛℯ𝒷𝒾𝓃 𝒟ℯ𝓁𝒶𝓋𝒾𝓏</strong></div>
<div class="tg-text">وقتی خاکمونو پس گرفتیم توهم تو همین کانال کونت میسوزه</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23513" target="_blank">📅 13:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23512">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23512" target="_blank">📅 12:11 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23511">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏بهمن کارگر، رییس ستاد مرکزی گرامیداشت «مناسبت‌های دفاع مقدس و مقاومت» گفت که امسال با توجه به شرایط جنگی، رژه نیروهای مسلح برگزار نمی‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23511" target="_blank">📅 12:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23510">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">داداش نگو ریاکار عقیده خودش رو داره بچشو همشریا و هموطن خودمون کشتن</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23510" target="_blank">📅 11:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23509">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗬𝗮𝘀𝗶𝗻</strong></div>
<div class="tg-text">داداش نگو ریاکار عقیده خودش رو داره بچشو همشریا و هموطن خودمون کشتن</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23509" target="_blank">📅 11:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23508">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23508" target="_blank">📅 11:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23507">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">الجزیره: قانون جدید تحریم‌های ترامپ، تمدید ۵ساله «قانون تحریم‌های ایران» را تصویب کرده و اختیارات کلیدی تحریمی آمریکا علیه بخش‌های انرژی و تسلیحاتی جمهوری اسلامی را تا پایان سال ۲۰۳۱ حفظ می‌کند. این قانون همچنین ابزارهای جدیدی برای اعمال تحریم و تعرفه علیه روسیه و خریداران انرژی روسیه در اختیار رئیس‌جمهور آمریکا قرار می‌دهد
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23507" target="_blank">📅 11:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23506">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">استوری پدر ریاکار مهسا امینی با پرچم تجزیه‌طلبهای کردستان که خط قرمز ما محسوب میشه. این استوری هم‌اکنون پاک شده. توضیحات رو در وویس براتون میدم. پرچم ایران فقط شیر و خورشید است و این خط قرمز ماست. @WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23506" target="_blank">📅 11:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23505">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c64jmDkTJhbro3pnG6ic0tMDSsLyG7o2hQVlNfCLd_cLRV-ng9nVgrd0b49Q3cdf7vZSierEmwOXXabOPDnYPGn9Mr3rYQpvQDg4n7Y6d9pg2TLyzewA9LS71ouNjLhgqZNDilCEqRpzryhH2MieUtA1rm1QYdZK4p3nqUKVfeXMK1_ikXLULOc7de6n2DTdhyEZeOBfkpz9Q09xEMvGYfKv0szE4WTOBNsxpn6yvHW0PAbOGuPNFgYut_BD7_6j-AM1WGRr34UiUpkpMy03cGpfxxNWyP1HyZUQi6K-yVYZCFU9_mcb_Dpko2d5a9Sx6qcSSa_JShD9CLZqdzK9nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری پدر ریاکار مهسا امینی با پرچم تجزیه‌طلبهای کردستان که خط قرمز ما محسوب میشه. این استوری هم‌اکنون پاک شده. توضیحات رو در وویس براتون میدم. پرچم ایران فقط شیر و خورشید است و این خط قرمز ماست.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23505" target="_blank">📅 11:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23504">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">هم اکنون تهران ، خیابان دولت ، چهار راه نشاط @WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23504" target="_blank">📅 11:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23503">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23503" target="_blank">📅 11:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23502">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23502" target="_blank">📅 11:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23501">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc408f38d4.mp4?token=rfBWkNF5TxPGAn7wJPwmeGGKu6dincmoi3E4chUrT0wWyCn_jwVD9RDW6EdYzLYbyPb9Y2vG9R3g8VTSoSYPLHCmUPaTT3jaMwxuQ1XWIjHhluMQEx0tcUPrbKfc02l6lHGKGDXak3V0PaJAGOorr7TpIWQotCSq28SzQy7Y7J_4HjHaegv7R7CP6KQdmLHYzspORW5axBgGdd_rl1zO3bqnAgWHmBdlKtlToko5zDPYPprZKeSK1b-9kjTvZHNdsGwKJUEPKdRpN8XHnFL6_TL9-_Wlrh0DsRXu1AnrZeos-J-JNRvlLL96Ujg0AazWjkhWKb7cmCafnBkyXJuS0xDuTBI82aIr5Kp3h6v_qPlbQGxGT6L-s82YXT3nm5Qk79-LCzT2O_7-edLOB70z2izZ2BcEyRpGPGVc3YGdogKKpkMB9YJunNIIzJKgpKal-tUzgQ3t2bV42sF1i-OzWwGaRPsLpCEXdCsrd_y3pjrCYu__L36Bwbq_cIXvjhe0tp1V78TWZiDKNCPHt8tnBZ8v8kkZIE-dvAt_Ga9fKSiDUQEawiCSeFtGSGhI7wHFiH5ly0_fXpu_HRk9oren5kVUusr4FWfa-p3sSkQammCb-87QReXDeNQo1KrcbzCM6SCQhaZ-AvjL3I-koFyyjzHuS1Zn2GJajT9cTM7Keyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc408f38d4.mp4?token=rfBWkNF5TxPGAn7wJPwmeGGKu6dincmoi3E4chUrT0wWyCn_jwVD9RDW6EdYzLYbyPb9Y2vG9R3g8VTSoSYPLHCmUPaTT3jaMwxuQ1XWIjHhluMQEx0tcUPrbKfc02l6lHGKGDXak3V0PaJAGOorr7TpIWQotCSq28SzQy7Y7J_4HjHaegv7R7CP6KQdmLHYzspORW5axBgGdd_rl1zO3bqnAgWHmBdlKtlToko5zDPYPprZKeSK1b-9kjTvZHNdsGwKJUEPKdRpN8XHnFL6_TL9-_Wlrh0DsRXu1AnrZeos-J-JNRvlLL96Ujg0AazWjkhWKb7cmCafnBkyXJuS0xDuTBI82aIr5Kp3h6v_qPlbQGxGT6L-s82YXT3nm5Qk79-LCzT2O_7-edLOB70z2izZ2BcEyRpGPGVc3YGdogKKpkMB9YJunNIIzJKgpKal-tUzgQ3t2bV42sF1i-OzWwGaRPsLpCEXdCsrd_y3pjrCYu__L36Bwbq_cIXvjhe0tp1V78TWZiDKNCPHt8tnBZ8v8kkZIE-dvAt_Ga9fKSiDUQEawiCSeFtGSGhI7wHFiH5ly0_fXpu_HRk9oren5kVUusr4FWfa-p3sSkQammCb-87QReXDeNQo1KrcbzCM6SCQhaZ-AvjL3I-koFyyjzHuS1Zn2GJajT9cTM7Keyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون تهران ، خیابان دولت ، چهار راه نشاط
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23501" target="_blank">📅 10:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23500">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdc97b83ba.mp4?token=pJk1au7x12LIUgQtHPTd7my2L2bftG6jh1ZrhOsYw1QYdFStFHQo2E_s53b0IlEBhle-XrZe2M6y55u199LqVm28zywfDj1AWqBRefuksNyYneSPP7eR06K_dYuKjL_F3s9a_eU8w0sQsbW5BvsDSL41rq8kBVo1r1Uf1SyqP91mkgSl00fC-CtMNveTRoKmz2Hc9hy9ifjJE0zH8yYKkKWeMI9fUruTyjrnNrKnscxJ5pRIfbt7NfGOO9CMA_XX-_K398Q1pmLJteHJWUYiX78sUFiN5F3liOBtflyVa3LjJa0bj7qQCdOnSb8ibXTrxTo169BSgaxz2bLwf0jhIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdc97b83ba.mp4?token=pJk1au7x12LIUgQtHPTd7my2L2bftG6jh1ZrhOsYw1QYdFStFHQo2E_s53b0IlEBhle-XrZe2M6y55u199LqVm28zywfDj1AWqBRefuksNyYneSPP7eR06K_dYuKjL_F3s9a_eU8w0sQsbW5BvsDSL41rq8kBVo1r1Uf1SyqP91mkgSl00fC-CtMNveTRoKmz2Hc9hy9ifjJE0zH8yYKkKWeMI9fUruTyjrnNrKnscxJ5pRIfbt7NfGOO9CMA_XX-_K398Q1pmLJteHJWUYiX78sUFiN5F3liOBtflyVa3LjJa0bj7qQCdOnSb8ibXTrxTo169BSgaxz2bLwf0jhIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان تهران شمال شرق ، محدوده شریعتی میرداماد ستون دود عظیم @WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23500" target="_blank">📅 10:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23499">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzINSDC9qToVuVgC2obXqeTGnRed9sR88TtwvSo-9fCnUwbjRaYB1aWL8kPiSq53JJvkLaAVaRP80zBKSW2NQAfWngK6TyACAGvDHr_t3USsx1jVABewflV2eLAd3oB3_LsH0248yTVVvuKXYx4MaqmhLNNsGVsbzDbig-BsCyOMpP6j4J2cS0FX1aTLwcAQt22-V5WJ2efJf9wvSl-aLeucmBBDv-RXssOw3d4juSknrDluyqxkO-c3c5pT0-uSn6iyh56E8AjW6V-pwFMTqxBbqB3slmjAJTxgsYzF--vveqSJ5oNpgvC8nwEx6GnH7XEWWZ2ePREtrvxqcD_4aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان تهران شمال شرق ، محدوده شریعتی میرداماد ستون دود عظیم
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23499" target="_blank">📅 10:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23498">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maGHag9W91MVxSe0WPaHctQ3aoqD5rUJjcazo30Dnu7CoqIN1DRIQc5Sx0YdJF-3leZWROctNr9fGm4RuWU8y59mjnPeE6UOruTiUYbbul4dbXr7EF_V-S8nHYFs-AjWM50H4tHUGnMcOgZz5u5K7C07MUlATJSWpEFiMoLDpKe74_P5mElemPN9G1YQupephdOFAkhwr05SXNew2THYpnubgeoGbhrC9ViBcZpZ_MMwo0vuMTEI2DqtSigdo50GVJLUNQEtxoEcHKuzY2VurqmjSVanLEhSEe7xCFn9i4KptqPsaT2z4tcF0vyS5VfQaPAmFzAHwbscwImlMIKlvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن‌ کج بند رضایی: منتظر موشکای با سر‌جنگی ۱ تن به بالا باشید
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23498" target="_blank">📅 10:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23497">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57b8923ab5.mp4?token=OvKIPcL2_BG5yPuHYb86tPvv_Z5FrFlYgcT2zV7uW5eyYsMsb1W2RCsv2NjgHoLmc-w1iVde5gj8LVuluyzlUwlPbfnrjl93mdJ2qKc4zqIfjPRwA8mAEU2hNPGdncHd9fAFWnP7gzygXc3ffETM1PwipA85rjUFkcKRL7UKTuty-SdAAbCoXPwL1JGIOnZ6RRqxXY7tk7AxTjxNYOkwUSrx_YdKLOhdSZum9V4thHr9LMKbN8wevxJx9yX2DoDOZF9WXPr76ti7diKjW_3bt8hldMK9qyAVXd3eQri-UNf0mI7p_xq2yv8w838l-izIqTRlgJh6fU8y13k6YdbdnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57b8923ab5.mp4?token=OvKIPcL2_BG5yPuHYb86tPvv_Z5FrFlYgcT2zV7uW5eyYsMsb1W2RCsv2NjgHoLmc-w1iVde5gj8LVuluyzlUwlPbfnrjl93mdJ2qKc4zqIfjPRwA8mAEU2hNPGdncHd9fAFWnP7gzygXc3ffETM1PwipA85rjUFkcKRL7UKTuty-SdAAbCoXPwL1JGIOnZ6RRqxXY7tk7AxTjxNYOkwUSrx_YdKLOhdSZum9V4thHr9LMKbN8wevxJx9yX2DoDOZF9WXPr76ti7diKjW_3bt8hldMK9qyAVXd3eQri-UNf0mI7p_xq2yv8w838l-izIqTRlgJh6fU8y13k6YdbdnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست درباره ایران: ویرانگری حملات نظامی ما علیه ایران تاریخی و بی‌سابقه بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23497" target="_blank">📅 09:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23496">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ec58e117.mp4?token=q4ZXWNlS261GcIu_Azof2_1Zd7MavsIm9RbmJAMVW49YwvW0z9Fttt-Mesz6LCEE7qHJ3VFx2Z--qHT56cCCr23m1DAoyzY4fpoGPGZgPoBKjtXT_4MXWlz6nVrdOoq0zEN678G8rEK_etIpglumsjcS6nZa83pL89FwDWSuNHXK9_k8mr1Fc3Be0u5wFMoBVnQ3W7Q8tT5q5_ltfZjDqiSdqQm-BV_wjosJXVSjGVgG-YR1PnFf8gSQz2RgnMxk8lXyB-bP1RKyfPwp1hsd-jXoMiB9hXAuc2F4dSKZD5Lbs1xVsF24XotUxyY-bY-ixfG8RdiBYbyCifVkrlzNtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ec58e117.mp4?token=q4ZXWNlS261GcIu_Azof2_1Zd7MavsIm9RbmJAMVW49YwvW0z9Fttt-Mesz6LCEE7qHJ3VFx2Z--qHT56cCCr23m1DAoyzY4fpoGPGZgPoBKjtXT_4MXWlz6nVrdOoq0zEN678G8rEK_etIpglumsjcS6nZa83pL89FwDWSuNHXK9_k8mr1Fc3Be0u5wFMoBVnQ3W7Q8tT5q5_ltfZjDqiSdqQm-BV_wjosJXVSjGVgG-YR1PnFf8gSQz2RgnMxk8lXyB-bP1RKyfPwp1hsd-jXoMiB9hXAuc2F4dSKZD5Lbs1xVsF24XotUxyY-bY-ixfG8RdiBYbyCifVkrlzNtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ما در جنگ با ایران با اختلاف زیادی در حال پیروزی هستیم.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23496" target="_blank">📅 09:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23495">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd8ba38435.mp4?token=a8mFDjGIvGXFv6Iz900vIdp54g9ZJ93OaOwmmeuY6lpo1-p-b_Phy6HbNsX_Gvr9RDLP74da6W2NCkz1VjDEbUZAki_vdpS3fJSr65n46pTuiKK0x_PP8AgP7aKCPnGSxLq4Xo-JKMlvbZyPQVRCENXQXnU0hMymOhZ6_dr1BD5bO1I997xdRFochhe2oa0F1zFbiNri4sdeOW-OIw3LKeK5rLOo2itprG1TA6Zt7aeBhJsIaUcnMqii4gsAUpiqMGWjFEtDewZEFHjhSfT3fg4YZg8PLXCgZqguVxsSzsTfoFeP1eU2DNCv32-FtFsUjwVtNYsfJPIFZuE-P4wktQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd8ba38435.mp4?token=a8mFDjGIvGXFv6Iz900vIdp54g9ZJ93OaOwmmeuY6lpo1-p-b_Phy6HbNsX_Gvr9RDLP74da6W2NCkz1VjDEbUZAki_vdpS3fJSr65n46pTuiKK0x_PP8AgP7aKCPnGSxLq4Xo-JKMlvbZyPQVRCENXQXnU0hMymOhZ6_dr1BD5bO1I997xdRFochhe2oa0F1zFbiNri4sdeOW-OIw3LKeK5rLOo2itprG1TA6Zt7aeBhJsIaUcnMqii4gsAUpiqMGWjFEtDewZEFHjhSfT3fg4YZg8PLXCgZqguVxsSzsTfoFeP1eU2DNCv32-FtFsUjwVtNYsfJPIFZuE-P4wktQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: هفته آینده در سازمان ملل سخنرانی می‌کنید. پیام شما چیست؟ ترامپ: سال گذشته، اپراتور تله‌پرامپتر من را از ورود به سالن منع کردند. بنابراین مجبور شدم بدون تله‌پرامپتر آنجا بایستم. جالب نیست؟ خبرنگار: پیام شما چیست؟ ترامپ: یادتان هست؟ آن‌ها پله‌برقی را خاموش کردند. خوشبختانه بانوی اولم خیلی محکم بود و توانستم پشت او یا بخش دیگری از بدنش را بگیرم. در واقع، دستم کمی پایین‌تر از پشت او قرار گرفت و محکم گرفتمش.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23495" target="_blank">📅 09:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23494">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4f409e707.mp4?token=ndbbK9rv0PYk1U7Vdm8lrCkoO5hp0UzAhgTLNUCFxGiUcFA0TlpTgO4kJXqcOrUckK5RVprN9ywZLkEbfjX-5JTrb_jz04l5GfsYmtCwbYAE4m779ZsQXglJza-_uzS0q1bywQ1pWIw_Pv2zcCR9HS-pf0mZufHYduVkdPrRhi9dNrzQC2LZUXaQ3VLv9F-MUyVj2dNtdhtNxysdWq96SxUERfhhm_pYkMQXp8IkGiVZQ2lrgBxlBlskx7M3-dzaZunvTrwHJr-jAOjMPWsh8Dz3hIwCrXcFI5Z7MUj4S9_Ulvo4wD_6lwooc8zAtrEaW06FOxieo3Zc2jtax9bD7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4f409e707.mp4?token=ndbbK9rv0PYk1U7Vdm8lrCkoO5hp0UzAhgTLNUCFxGiUcFA0TlpTgO4kJXqcOrUckK5RVprN9ywZLkEbfjX-5JTrb_jz04l5GfsYmtCwbYAE4m779ZsQXglJza-_uzS0q1bywQ1pWIw_Pv2zcCR9HS-pf0mZufHYduVkdPrRhi9dNrzQC2LZUXaQ3VLv9F-MUyVj2dNtdhtNxysdWq96SxUERfhhm_pYkMQXp8IkGiVZQ2lrgBxlBlskx7M3-dzaZunvTrwHJr-jAOjMPWsh8Dz3hIwCrXcFI5Z7MUj4S9_Ulvo4wD_6lwooc8zAtrEaW06FOxieo3Zc2jtax9bD7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: اگر از مردم بپرسند که کاهش قیمت بنزین را می‌خواهند یا اجازه بدهند ایران به سلاح هسته‌ای دست پیدا کند، نتیجه رأی‌گیری با اختلاف بسیار زیادی به نفع جلوگیری از دستیابی ایران به سلاح هسته‌ای خواهد بود. مردم نمی‌خواهند ایران سلاح هسته‌ای داشته باشد
@WarRoom</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/23494" target="_blank">📅 09:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23493">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcyF1mCud7IHLuqlA_9rj4ku0pBsmo0RaOT7j4aO9Mb8ZH-1WKdnwyAPTzMCIOrGU1haa5bVrIJO4PhEdXrkOMApb0VWcA3YHfMNVpgBFF9-5Bv1Z-0UQC4gJuUelVmOrDGf24yhzk2tzhZ9N1YrIYZpTiw1uSo3dsAybSK1OKBSpDiZZJATWn8_ptNUR69RjPeK4Bjqi88HG7vFefylSf7-kT6zGtGF98r36Km-BuyoFFpRshJeQ4IJ5n7yJnej9jkYE4qV16wbBL2DcpGO3i5l9whwNnXCt_tqM7MbyzDEWJGvH99wPbjQFbgYUWkkx_7oad1aFWeDDglxG1qWBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام
حسین پدران،
فرزند حمیدرضا اجرا شد؛ رسانه‌های ایران به نقل از مرکز رسانه قوه قضاییه اعلام کرده‌اند که او به اتهام همکاری اطلاعاتی با موساد و انتقال اطلاعات درباره سایت‌های موشکی و نظامی در اصفهان محکوم شده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/23493" target="_blank">📅 09:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23491">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d34xtGUvCY5RboTsUbbLSnCo_nOFevnWPDU44K8pdEujTNXfDYVSAvS2aHkPKPL_1giSZujLF78EngfgZKXzpDJAXMcKvXgTHOA_f9S9yJcVrxBR5h2pT_MvGIt9mYHxuyXCtBav9SPZYlj242tPtwaBCKUiZrYCgjsUdsvN0xIu7Zaaz75AqVqc16pzIM43lGsfw_HczfKQmok8F2e_G_KnkKPigiGWsMnGeRrl6Eh7z4_GTvFL_UnN-DVb2rvDy3PsBIXcvoR7fftnrzHjJag-1l-wbOJmcbpN9Arx8wjgqdtXnyZMGOIUPJlBsO2xwmaOGx1_cyLyhTaHUCpwPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qu2RkRmN-KJyJrlzs1BmaaCcDBbrQD1yXB893prxcAlqh4phpP9YRUP0Xf9GHy3C8D4E73oZfxaMxel0KtZCYi8sVa2-K1Px9pyC9qokL5YUleTFohEk8d8m73nyLTuAsm46mXwqTuqMc0sFoPWW5vNGyH9-cBv1nRYDdOYTPw7qSyptCLlWlBiIHXCdHPE8OuU9Nhv7t37Fd_GJwR__pO-ru7bFxBUCuxEEsEa9q7WBx-RINZI4ZR-yslMH7wC5zDkryM0D-11VoHWXy31fkZom2kRKTtEY2yc_oyigwAjrnS4A6XKybSoKpoYdatfOq-Ka0dorfxMc_cJB8icyyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ در پستی در شبکه اجتماعی تروث سوشال، فهرستی با عنوان «۲۵ دستاورد برتر ترامپ در سال‌های ۲۰۲۵ و ۲۰۲۶» منتشر کرد و در آن، از سیاست‌های مهاجرتی، کاهش مالیات، اعمال تعرفه‌های تجاری، افزایش بودجه نظامی، گسترش حفاری نفت و گاز و لغو برخی سیاست‌های اقلیمی به‌عنوان دستاوردهای دولت خود نام برد. مورد مرتبط با ایران در این فهرست، بند ۱۱ است؛ جایی که ترامپ مدعی شد آمریکا در عملیات‌های «چکش نیمه‌شب» و «خشم حماسی»، ظرفیت غنی‌سازی هسته‌ای ایران را نابود کرده تا به گفته او، ایران «هرگز» به سلاح هسته‌ای دست نیابد.بند ۹ نیز به افزایش بودجه نیروهای مسلح آمریکا تا یک تریلیون دلار در سال جاری و برنامه برای رساندن آن به ۱.۵ تریلیون دلار در سال آینده اختصاص دارد
@WarRoom</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/withyashar/23491" target="_blank">📅 09:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23490">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VL_U4nr3HgbGTShYyH-gOsPzvIr-RL1BO4E5shrbTWzyVwegjTCRLjnaS-nxya-kVrhLTEg7JnSdZgk8LXz9pdea1caPtaz9PSCQi3eeDucaIoQhj_YPQTCUxOLuNtwMMxRZ7hshL5sl0rL54gEidMf0t2I7c5jXkyc1XMvrBoOBXAPK7J9zRaYs7Z8fzc3oPAkGLyF4lmKX5SqTxltfZLGZ3l_1mDazNmGlcydFQ9jV8bElXTzCHDr54stKKqIIWDoS6vbB6NDZh6Ifi6AMGEJQrvFFw2C8MTxMHq2G9ArZ5gJV60FdhR9S8z6lOWVHLTh63wApIxM37n5LbnnLbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیم جونگ‌اون از خط تولید پهپادهای انتحاری یک‌طرفه بازدید می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/23490" target="_blank">📅 09:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23489">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qakvzLXTo5pP35RdB24w5_pA8uryBb1qgpwzxpEJSEAWEsY40g9CAynY35DLMk5rtsy42o9kFmFgI_OVQowt5accqF1Rpu-dvXAdG7qGpVjSF3hVXVb6fhnbwxBOfXkX2ZibCbKF_2MZ12CoCSJYN7Exfqz-Zn_CiEa0GgZCe6Z71ci05Zow2T-Bz2PpmwDzsAYd8ssCrxKmRyVl-8uOleuL5BvED7h0TAXUjPvL-O1U6Jj-XTgzWh6Ee-LG-N9J6HFSB2vWQ94JQA1r90vqHiLcssXsBW3o8xpe_JBML3tzuEN7l9LkuN4ECl5HUvw8mWHsy4_PtEK0T7Fw_cLIVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نهاد ناظر بر امور بانکی ترکیه مجوز فعالیت شعبه استانبول «بانک ملت» را لغو کرد؛ بانکی که صددرصد متعلق به دولت ایران است و از سال ۱۹۸۲ در ترکیه فعالیت داشته است.سازمان تنظیم مقررات و نظارت بانکی ترکیه (BDDK) دلیل این اقدام را تهدید علیه ثبات نظام مالی عنوان کرده است.این بانک پیش‌تر و در پی تحریم‌های آمریکا تا حد زیادی از شبکه بانکی جدا شده بود (قطع دسترسی به سوئیفت و حذف از سامانه انتقال الکترونیکی وجوه یا EFT ترکیه)، اما این تصمیم به معنای پایان رسمی فعالیت‌های آن است.
@WarRoom</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/23489" target="_blank">📅 08:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23488">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08184bf9e6.mp4?token=WSglex7TzHbS_Ylzx8Y3C57_QC12YzQsvyATy5urY3_tHk6ly_wlRzsKB1HYNAIADbr4tnMOPrPRI59nHH9EIndBNO8Fq0b0kiGK2Ik1Fz8kP2TNZ_JEfcK-5tRDWW2UPXR1HP-FAvaU9D-kRrFzcu4mnjZk8Fol00Z5RbrolOdM9qJsNpG-zZONhemYioM6teY2jSnD3vFIT2U-TxT3yt21z89iJJP0ITb0KXEdVv_ayNOIPl0WKBWKxvaR4aMEu85_rTxYz0VMCpmrRg9BD2v-wOAkIhIgEjsdyAfCkvnFb7ZMDbQvREJij52WSbkrqqFuoKjGkC3pu-lSnkQOMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08184bf9e6.mp4?token=WSglex7TzHbS_Ylzx8Y3C57_QC12YzQsvyATy5urY3_tHk6ly_wlRzsKB1HYNAIADbr4tnMOPrPRI59nHH9EIndBNO8Fq0b0kiGK2Ik1Fz8kP2TNZ_JEfcK-5tRDWW2UPXR1HP-FAvaU9D-kRrFzcu4mnjZk8Fol00Z5RbrolOdM9qJsNpG-zZONhemYioM6teY2jSnD3vFIT2U-TxT3yt21z89iJJP0ITb0KXEdVv_ayNOIPl0WKBWKxvaR4aMEu85_rTxYz0VMCpmrRg9BD2v-wOAkIhIgEjsdyAfCkvnFb7ZMDbQvREJij52WSbkrqqFuoKjGkC3pu-lSnkQOMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست: در طول ۲۵۰ سال گذشته، ما همواره به آمریکایی‌هایی نیاز داشته‌ایم که برخیزند و بگویند: «مرا بفرستید.»
چه کسی با «قرمزپوشان» (نیروهای بریتانیایی) خواهد جنگید؟ چه کسی به نبرد با کمونیست‌ها خواهد رفت؟ چه کسی با اسلام‌گرایان خواهد جنگید؟ چه کسی مبارزه خواهد کرد؟همواره آمریکایی‌هایی بوده‌اند که گفته‌اند: «مرا بفرستید.»
@WarRoom</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/23488" target="_blank">📅 08:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23487">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3mVKKNiKh3Oyh8su63D5cUdkeCU_Xa7u6fwh_7mAl18HjUjzg_ZdkM5VlOoW7GGtbwxdN9HfilRMqFpMAJfU6e44DE_aPL2u7PGXL5j-Yc41oFDgmlUKk_6KvAIkYEl1Gfa7Stwvq7E1SWGIooXZ2-yjFN7CMOHo8UPcxxpynVQPS2m-UBLIQjfsayYBOpQpnpUJ9Ria6gaVCYQMbA-FIvhzGzl3LRc_d2rPlQmgpRww9CfzR8VKqqdPNv7EhIuHFd5eT0HZxvLsLaqUCFzuO2zx8sr2a6L-LtzzIBOKFmiayAidoCQNzO-snZUop7kOwD7JTGzLc0ATPELSrKPTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنتاگون پس از توقف موقت این طرح در اوایل ماه جاری، اکنون در حال پیشبرد برنامه غربالگری اجباری سطح تستوسترون برای نظامیان مرد ۳۰ سال و بالاترِ ارتش ایالات متحده است. بر اساس دستورالعمل‌های جدید، این آزمایش در معاینات دوره‌ای سلامت و ارزیابی‌های سالانه گنجانده خواهد شد و مسیرهای درمانی استانداردی نیز برای موارد کمبود تستوسترون در نظر گرفته شده است. نظامیان جوان‌تر نیز می‌توانند به‌صورت داوطلبانه درخواست انجام این آزمایش را بدهند.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23487" target="_blank">📅 08:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23486">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpjbWbA0Trbz60y8RbOkORosdE-1oN1HXgAIat5JoANpQQB8KnOEgtpF3-GlnrgRCE10Xxnnqpa2pzlGkeKM763H5wupX9PqGw-CBVwf9JNeDNOIvYZPR--UbB1fyIZO0Vf1Jv2YcCRMqC7QXR_H93LrSo2M_c-IV660RDOUiMX5h-MSvc44AzckRzbEVAT-Hrmn5lyx9pTEwTlsY_X09uy3m8-1V88msSiKxf6r8BLcVuWZv2I3hK-Ju-CKrsY-SIhcIgc4Tzf3Svnxs-Gg-pjOlcKsO8cGS6tbEE7wZfN9WVXlSJZfKCKEMTcSmXKBvpG9FEG-M_L9wL5MrDiy9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه ایالات متحده با فروش تجهیزات پدافند هوایی و خدمات پشتیبانی به ارزش ۲.۶۸ میلیارد دلار به اوکراین موافقت کرده است.این بسته شامل سامانه‌های پدافند هوایی با برد بیشتر، پرتابگرهای متحرک، رادارهای مقابله با پهپاد، قطعات یدکی، نرم‌افزار و پشتیبانی فنی است.اوکراین هزینه این خرید را از طریق کمک‌های اروپایی و بودجه‌ای که پیش‌تر تحت برنامه «تأمین مالی نظامی خارجی» ایالات متحده اختصاص یافته بود، تأمین خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/23486" target="_blank">📅 08:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23485">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ قانون «تحریم روسیه و ایران، لیندسی او. گراهام» در سال ۲۰۲۶ را امضا کرد. این قانون تحریم‌های موجود علیه ایران در حوزه انرژی و تسلیحات را برای ۵ سال تمدید می‌کند و امکان تحریم پوتین، الیگارش‌ها، بانک‌ها، شرکت‌های انرژی و دفاعی و ناوگان نفتکش‌های سایه روسیه را فراهم می‌کند. همچنین به رئیس‌جمهور آمریکا اختیار اعمال تعرفه تا ۱۰۰ درصد بر کالاهای کشورهایی مانند چین و هند که نفت و گاز روسیه می‌خرند و تا ۵۰۰ درصد بر برخی واردات روسیه را می‌دهد. ترامپ می‌تواند این اقدامات را تعلیق یا لغو کند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/23485" target="_blank">📅 05:58 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23484">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ برای گذراندن آخر هفته راهی کمپ دیوید شده است؛ طبق برنامه رسمی، او شنبه و یکشنبه در این اقامتگاه خواهد بود و برنامه‌های این دو روز با عنوان «زمان اجرایی» و بدون حضور رسانه‌ها ثبت شده است.  هم‌زمانی این سفر با تحولات جنگ ایران مورد توجه قرار گرفته
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/23484" target="_blank">📅 00:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23483">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گزارش ها از
هدف قرار گرفتن نزدیکی اقامتگاه بن سلمان
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/23483" target="_blank">📅 00:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23482">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8fa371e84.mp4?token=OFM6M8IKgpbnwlO3RTmRIkkd59Uqkxexn3MxbBjg1WE7i8JtBlLpAUNDqOzNAlnyZmIJa79qE99RU2HIqiaNsYOCUCwv1mrxTmdXmq95PDC9wOLa5DXXhgOFdquOQglc5vv_JFXKfGWAJgosLUvfUOmJRjLjwOSLHSgzLSXWUjZOJNjmQd31c1uSBLLXYx-DXZt_E-DD4-mUrXZE3GMIh5bL1zpWEklBpmyKdwMDYfQBJIBRO8DjkwjXZsjkdGgYt79GVWonWQ2hztHpsi06MNB--tLuPnf2WfZUldXq7gPEPl8xtlfRgS3AI6WI9NfgaQtJMnXrlS4morUvDuKWqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8fa371e84.mp4?token=OFM6M8IKgpbnwlO3RTmRIkkd59Uqkxexn3MxbBjg1WE7i8JtBlLpAUNDqOzNAlnyZmIJa79qE99RU2HIqiaNsYOCUCwv1mrxTmdXmq95PDC9wOLa5DXXhgOFdquOQglc5vv_JFXKfGWAJgosLUvfUOmJRjLjwOSLHSgzLSXWUjZOJNjmQd31c1uSBLLXYx-DXZt_E-DD4-mUrXZE3GMIh5bL1zpWEklBpmyKdwMDYfQBJIBRO8DjkwjXZsjkdGgYt79GVWonWQ2hztHpsi06MNB--tLuPnf2WfZUldXq7gPEPl8xtlfRgS3AI6WI9NfgaQtJMnXrlS4morUvDuKWqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: جنگ به زودی به پایان خواهد رسید و وقتی این اتفاق بیفتد، قیمت بنزین شما به سطحی که قبل از آن داشت، کاهش خواهد یافت، شاید حتی کمتر از آن.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/23482" target="_blank">📅 23:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23481">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">العربیه: وزیر خارجه پاکستان محسن نقوی در ساعات آتی به ایران عزیمت می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/23481" target="_blank">📅 21:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23480">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">المانیتور: یک منبع ارشد اطلاعاتی اسرائیل می‌گوید نهادهای امنیتی اسرائیل در حال حاضر با
حمله پیش‌دستانه علیه حوثی‌ها مخالف‌اند
. به گفته او، حوثی‌ها اکنون هیچ بازدارندگی مؤثری از سوی آمریکا، اسرائیل یا عربستان ندارند و به «اسب تیره» منطقه تبدیل شده‌اند؛ تهدیدی غیرقابل‌پیش‌بینی که می‌تواند عربستان و متحدانش را به اسرائیل نزدیک‌تر و وابسته‌تر به توانمندی‌ها و اطلاعات اسرائیل کند
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/23480" target="_blank">📅 21:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23479">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آسوشیتدپرس:
سقوط بقایای یک پهپاد حوثی پس از رهگیری در عربستان باعث کشته‌شدن یک نفر شد.
پدافند عربستان پهپاد را منهدم کرد اما بقایای آن روی منطقه مسکونی سقوط کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/23479" target="_blank">📅 21:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23478">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">الجزیره: یک منبع مطلع آمریکایی اعلام کرده حدود
۶۰ میلیون بشکه نفت ایران، یا نفتی که مشکوک به منشأ ایرانی است،
روی نفتکش‌های تحت تحریم سرگردان مانده است. به گفته این منبع، نفتکش‌هایی که خارج از محدوده محاصره دریایی قرار دارند نیز در معرض رهگیری هستند و به همین دلیل با سرعت کمتری محموله‌های خود را تخلیه می‌کنند. همزمان، واردات نفت چین از ایران یا محموله‌های مشکوک به ایرانی بودن به حدود
۴۴۰ هزار بشکه در روز
کاهش یافته است
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/23478" target="_blank">📅 21:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23477">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKinyfrZkpaoqud2TN9hoslEaWIyo0NW1qKXhJM7130F0j5-OHUui-D3zgZ7yfj7JWTlD8wVDyfWy14sxL7vW5mRspumdL-RWIBJqdYdDi4koO1L8gXTs1rcF5VgkDJeTtT7uf2BpOzjZEE8OkUJG5bC9us9a--Q1ipBtgnhZB8y5LCEXGGUQqcbkHBk2uxE4V8EvAhHHbART5Uzcj0fwyajGBAVwjFQi6JhuxY9NQCKb0-nGmnRmRmR0iJFWXz1qNo2wkQY35veyUosGBVQSmCkoz0Q0zi8CoUpj6rFaAJSZQlwsIKG0qQHT87nCkAAU8_XWcq3Emsq3lrlpqybUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاليباف
:
دوره‌ای که در آن F-35ها و F-15های شما شکار می‌شوند و مجبورید گزارش دهید که آسیب دیده‌اند
🤏
از قبل آغاز شده است.
آنچه زمانی سوخت خالص کابوس بود، اکنون واقعیت روزانه است. با آن زندگی کنید.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/23477" target="_blank">📅 21:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23476">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">الجزیره: وزارت خزانه‌داری آمریکا اعلام کرده اقدامات سختگیرانه‌ای علیه بانک‌ها و مؤسسات مالی در امارات و ترکیه که به گفته واشینگتن از ماهان‌ایر و شبکه‌های مرتبط با آن حمایت می‌کنند، آغاز کرده است. این اقدامات با هدف قطع مسیرهای مالی و خدماتی مرتبط با جمهوری اسلامی و ماهان‌ایر انجام می‌شود. آمریکا پیش‌تر نیز چند شرکت در امارات و ترکیه را به اتهام ارائه خدمات به ماهان‌ایر تحریم کرده بود. هنوز نام بانک‌های هدف، نوع دقیق محدودیت‌ها و زمان اجرای کامل این اقدامات اعلام نشده است. همزمان، ماهان‌ایر اعلام کرده از ۳۰ شهریور پروازهای خود به استانبول و آنکارا را متوقف می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/23476" target="_blank">📅 20:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23475">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بر اساس گزارش رسانه‌های تحلیلی مستقل، دولت ترکیه ابلاغیه جدیدی به سنتکام ارسال کرده و هرگونه بهره‌برداری از پایگاه هوایی اینجرلیک برای سوخت‌رسانی یا هدایت پروازهای رزمی علیه هدف‌های منطقه‌ای را اکیداً ممنوع اعلام کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/23475" target="_blank">📅 20:30 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23474">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ به نیوزنیشن : باید ببینیم که آیا ایران نابود خواهد شد یا خیر
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/23474" target="_blank">📅 20:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23473">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ در پاسخ به سئوال نیوزنیشن درمورد گزارش روز پنجشنبهِ اکسیوس درباره «تصمیم بزرگ» او: «آنها حالا می‌خواهند به توافق برسند. اگر این توافق، توافقِ درستی نباشد، حتی به آن فکر هم نمی‌کنم.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/23473" target="_blank">📅 20:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23472">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ: ممکن است به سمت جنگی تمام‌عیار با ایران پیش برویم.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/23472" target="_blank">📅 20:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23471">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ: ایالات متحده در حال مذاکره با حوثی‌هاست و آن‌ها نیز به دستیابی به توافق با آمریکا تمایل دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/23471" target="_blank">📅 20:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23470">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">برنامه «پاداش برای عدالت» وزارت خارجه آمریکا برای اطلاعاتی که به مختل کردن سازوکارهای مالی سپاه پاسداران، از جمله حساب‌های رمزارزی، متولیان نگهداری دارایی‌ها و شرکت‌های پوششی، کمک کند، تا سقف ۱۵ میلیون دلار جایزه تعیین کرد. و همچنین اعلام کرد سپاه پاسداران…</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/23470" target="_blank">📅 20:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23469">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/23469" target="_blank">📅 20:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23468">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">رویترز: آمریکا به هیات اصلی جمهوری اسلامی، از جمله مسعود پزشکیان و عباس عراقچی، اجازه داده است هفته آینده برای شرکت در مجمع عمومی سازمان ملل به نیویورک سفر کنند. این هیات کوچک‌تر از سال گذشته خواهد بود، اما اعضای آن با محدودیت تردد در مناطق مشخص نیویورک و ممنوعیت خرید کالاهای لوکس و برخی کالاهای دیگر، از جمله عضویت در فروشگاه‌های عمده‌فروشی، مواجه خواهند بود.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/23468" target="_blank">📅 18:23 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

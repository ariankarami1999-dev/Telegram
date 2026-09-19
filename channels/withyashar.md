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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 15:29:19</div>
<hr>

<div class="tg-post" id="msg-23527">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/withyashar/23527" target="_blank">📅 14:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23526">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝘼𝙢𝙞𝙧 𝙎𝙩𝙧𝙞𝙠𝙚</strong></div>
<div class="tg-text">داداش دیدی شاهزاده یه چیزی میدونست از اعتصاب کردا حمایت نکرد</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/withyashar/23526" target="_blank">📅 14:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23525">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">استوری پدر ریاکار مهسا امینی با پرچم تجزیه‌طلبهای کردستان که خط قرمز ما محسوب میشه. این استوری هم‌اکنون پاک شده. توضیحات رو در وویس براتون میدم. پرچم ایران فقط شیر و خورشید است و این خط قرمز ماست. @WarRoom</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/withyashar/23525" target="_blank">📅 14:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23524">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/withyashar/23524" target="_blank">📅 14:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23523">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بانک مرکزی واردات خودروهای لوکس را متوقف می‌کند
بانک مرکزی اعلام کرده است که برای واردات خودروهای لوکس مانند لکسوس LX700، مرسدس‌بنز کلاس S و بی‌ام‌و سری ۷، کد ساتا صادر نمی‌شود.کد ساتا مجوزی است که پس از تأیید منشأ ارز صادر می‌شود و برای ترخیص خودرو از گمرک ضروری است. بنابراین، خودروهای مشمول این تصمیم تا زمان دریافت مجوز امکان ترخیص نخواهند داشت.این تصمیم برای جلوگیری از سودجویی در واردات خودروهای گران‌قیمت و کاهش فشار بر بازار ارز گرفته شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/withyashar/23523" target="_blank">📅 14:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23522">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ان‌بی‌سی: مارکو روبیو، وزیر خارجه آمریکا، برخلاف جی‌دی ونس، در طول جنگ از قرار گرفتن در کانون توجهات درباره جنگ نامحبوب ایران اجتناب کرده است؛ رویکردی که ممکن است از نظر سیاسی به سود او باشد. به گفته منابع نزدیک به روبیو، او در تمام مدت جنگ یک «دست پنهان» بوده و در تدوین راهبرد دولت ترامپ نقش داشته است. این منابع همچنین می‌گویند احتمال نامزدی روبیو برای ریاست‌جمهوری در آینده می‌تواند همچنان روی میز باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/withyashar/23522" target="_blank">📅 13:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23521">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">حریق در انبار کباب‌سرای محمد در تهران، در خیابان دولت (کلاهدوز)، نرسیده به سه راه نشاط (پلاک ۳۳۵) @WarRoom</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/withyashar/23521" target="_blank">📅 13:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23520">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/withyashar/23520" target="_blank">📅 13:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23519">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">گزارش‌ها از کشته شدن ژنرال فراق العسّار از فرماندهان ارشد حوثی‌ها حکایت دارد. این گروه در بیانیه‌ای از او به‌عنوان فرمانده تیپ یکم کماندو یاد کرده است. العسّار در جریان حمله‌ای در جبهه کَهْبوب، در نزدیکی تنگه باب‌المندب، کشته شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/withyashar/23519" target="_blank">📅 13:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23518">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79606f3b2f.mp4?token=Mg15zS6o9ayD4Jp7Czp7aX8pKhyX_WDAPpPMXQjkR7YP1ckdgDOvlFtuvEYAo-MO1JguEYQFfXOhuvOLxGySceLe52k-uDM12eNA_5wxiiUQf1iTOsUVhKpkOPpfcsniq2V06600m0hElskX1BcQrO-kRtaDNxmZ2m5_4bwmgBDpkluctH_nhk_6IpE7WPg2DbvNvAFg7WacFil5dKG5GXTQqme1JBTJDc36asjaOIwHcWAlEmAfDizLj7XfSA3kX_t2P_iZPk6kE_FFN0EqyuMNxrgg5IIyne_pUDh-bbIF0dXA6_CyWXZjdXmgRMjcVeNC3QOJOy5bZ8oSeR47vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79606f3b2f.mp4?token=Mg15zS6o9ayD4Jp7Czp7aX8pKhyX_WDAPpPMXQjkR7YP1ckdgDOvlFtuvEYAo-MO1JguEYQFfXOhuvOLxGySceLe52k-uDM12eNA_5wxiiUQf1iTOsUVhKpkOPpfcsniq2V06600m0hElskX1BcQrO-kRtaDNxmZ2m5_4bwmgBDpkluctH_nhk_6IpE7WPg2DbvNvAFg7WacFil5dKG5GXTQqme1JBTJDc36asjaOIwHcWAlEmAfDizLj7XfSA3kX_t2P_iZPk6kE_FFN0EqyuMNxrgg5IIyne_pUDh-bbIF0dXA6_CyWXZjdXmgRMjcVeNC3QOJOy5bZ8oSeR47vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختر پزشکیان: من هم جان‌فدا هستم
@WarRoom</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/withyashar/23518" target="_blank">📅 13:11 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23517">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/withyashar/23517" target="_blank">📅 13:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23516">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/withyashar/23516" target="_blank">📅 13:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23515">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/withyashar/23515" target="_blank">📅 13:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23514">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝘼𝙧𝙖𝙙</strong></div>
<div class="tg-text">داداش یعنی چی که میگی تجزیه طلب
تو حق مردم کردستان رو بده بهشون چرا بخوان جدا شن؟؟
وقتی رضا پهلوی دوم بتونه برابری ایجاد کنه و عدالت ، هیچ قومی خواستار جدایی نیست بلکه اونایی هم که هستن میشن طرفدارش و طرفدار کشور.....</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/withyashar/23514" target="_blank">📅 13:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23513">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromℛℯ𝒷𝒾𝓃 𝒟ℯ𝓁𝒶𝓋𝒾𝓏</strong></div>
<div class="tg-text">وقتی خاکمونو پس گرفتیم توهم تو همین کانال کونت میسوزه</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/withyashar/23513" target="_blank">📅 13:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23512">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/23512" target="_blank">📅 12:11 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23511">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‏بهمن کارگر، رییس ستاد مرکزی گرامیداشت «مناسبت‌های دفاع مقدس و مقاومت» گفت که امسال با توجه به شرایط جنگی، رژه نیروهای مسلح برگزار نمی‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/withyashar/23511" target="_blank">📅 12:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23510">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">داداش نگو ریاکار عقیده خودش رو داره بچشو همشریا و هموطن خودمون کشتن</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/withyashar/23510" target="_blank">📅 11:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23509">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗬𝗮𝘀𝗶𝗻</strong></div>
<div class="tg-text">داداش نگو ریاکار عقیده خودش رو داره بچشو همشریا و هموطن خودمون کشتن</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/withyashar/23509" target="_blank">📅 11:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23508">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/23508" target="_blank">📅 11:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23507">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">الجزیره: قانون جدید تحریم‌های ترامپ، تمدید ۵ساله «قانون تحریم‌های ایران» را تصویب کرده و اختیارات کلیدی تحریمی آمریکا علیه بخش‌های انرژی و تسلیحاتی جمهوری اسلامی را تا پایان سال ۲۰۳۱ حفظ می‌کند. این قانون همچنین ابزارهای جدیدی برای اعمال تحریم و تعرفه علیه روسیه و خریداران انرژی روسیه در اختیار رئیس‌جمهور آمریکا قرار می‌دهد
@WarRoom</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/23507" target="_blank">📅 11:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23506">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">استوری پدر ریاکار مهسا امینی با پرچم تجزیه‌طلبهای کردستان که خط قرمز ما محسوب میشه. این استوری هم‌اکنون پاک شده. توضیحات رو در وویس براتون میدم. پرچم ایران فقط شیر و خورشید است و این خط قرمز ماست. @WarRoom</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/23506" target="_blank">📅 11:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23505">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWfoOa-fm9fkGtKRklb_abDflUCg--0ShcZTvnh-hevrzcdwaKZoA1smDM6pw47ypyUEsaTH-N4VJ79znw_u3KXkrjdNnNd39iv0BYeiAwL8c1IOJYtkPwjt_TXCm4iNNKuBhyDkCaw06Oj1PWYXY7uHYZ6kkODCWiYUfoZvTyhS-zOftcgQqdzXy35g6iOMS-OD-v0zR1P3HVyFd59mdylwVAkulh19TSkMgxjBUM3BoGsD_h1KEi6vHz4R4NysHULEP7ZQjzGTh5v0nOVMbeJEJ26KZTBBEatpVw-g-BetkmekArhvABLEPvkgrXczsxW4U9vab_oTiZ05A-piEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری پدر ریاکار مهسا امینی با پرچم تجزیه‌طلبهای کردستان که خط قرمز ما محسوب میشه. این استوری هم‌اکنون پاک شده. توضیحات رو در وویس براتون میدم. پرچم ایران فقط شیر و خورشید است و این خط قرمز ماست.
@WarRoom</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/23505" target="_blank">📅 11:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23504">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">هم اکنون تهران ، خیابان دولت ، چهار راه نشاط @WarRoom</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/23504" target="_blank">📅 11:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23503">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/23503" target="_blank">📅 11:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23502">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/23502" target="_blank">📅 11:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23501">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc408f38d4.mp4?token=YzGbRYJD6f3eJMyIiXJEkNVAM_tPfESxTMi3WBxROKFsBnHhHbxVI4PK2dNjBiAKOebcykei50bIqDleaHTBiCFv6alQBS-xCh3cLdDp_0pVGc7JurYDtW75iXmq-mIFHaiwnQ7PKPzt3omt1notSmjGxWTWcMffR2FI0GZOBIQFXhkUtzvsP2OQvXAKCQ9hf20-Qm1IwG1PRfkN-kwtYpI9_jVFAmaiiTsq6cwHs06bdWW9Vj40o0dUZsCHHgV65C6EYrPlfhzIkWXoQBYOPNgNnr8EkMxeuYVJ0-6Xpos5hIfToGX22p5HwO2WQeStPFhOl6BCwJiZ_olH4KD96XsSr_5VVi-n0JoUPzPvqxQHl6TR1i02ZybA86eMPRRntW0b625L-iq074EfQlOSfcbjgVOdTnwic12QIGD-5OQumxvjWwDgugIw1GzEVdYGd07TpKl4dpRUgYH8YaElQocpvZhp4eCgnIAH4MtBb92dCq_cpph_VUQ6k1vlTjMvXkb-GRFAo4yT5YTs46bJDPKUH5s4B51yN1mQdHg3pWGkTn5Bwk5dORO8HWesJnqPTiYe42hzWidNsKp0n8u4qf9Q3EoTG47cSf-v9cBao2vPTNwTCZXiPBtwEK-XH6MPOJ5CT9yd6k3JvYdQiFvaksVk74Zm0_kY31iFunXDvFk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc408f38d4.mp4?token=YzGbRYJD6f3eJMyIiXJEkNVAM_tPfESxTMi3WBxROKFsBnHhHbxVI4PK2dNjBiAKOebcykei50bIqDleaHTBiCFv6alQBS-xCh3cLdDp_0pVGc7JurYDtW75iXmq-mIFHaiwnQ7PKPzt3omt1notSmjGxWTWcMffR2FI0GZOBIQFXhkUtzvsP2OQvXAKCQ9hf20-Qm1IwG1PRfkN-kwtYpI9_jVFAmaiiTsq6cwHs06bdWW9Vj40o0dUZsCHHgV65C6EYrPlfhzIkWXoQBYOPNgNnr8EkMxeuYVJ0-6Xpos5hIfToGX22p5HwO2WQeStPFhOl6BCwJiZ_olH4KD96XsSr_5VVi-n0JoUPzPvqxQHl6TR1i02ZybA86eMPRRntW0b625L-iq074EfQlOSfcbjgVOdTnwic12QIGD-5OQumxvjWwDgugIw1GzEVdYGd07TpKl4dpRUgYH8YaElQocpvZhp4eCgnIAH4MtBb92dCq_cpph_VUQ6k1vlTjMvXkb-GRFAo4yT5YTs46bJDPKUH5s4B51yN1mQdHg3pWGkTn5Bwk5dORO8HWesJnqPTiYe42hzWidNsKp0n8u4qf9Q3EoTG47cSf-v9cBao2vPTNwTCZXiPBtwEK-XH6MPOJ5CT9yd6k3JvYdQiFvaksVk74Zm0_kY31iFunXDvFk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون تهران ، خیابان دولت ، چهار راه نشاط
@WarRoom</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/23501" target="_blank">📅 10:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23500">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdc97b83ba.mp4?token=S1O17RHT6s0JWzQyscz9p5TdT_amuT1BlNhahZ8U90OK2MgWXq8GI_qmUiACD-cq6F9RrQuwbSwxQMVOGQSAEsocQryVN20LFyNLw9-IfY5BmWB7kEmgTNT5UJWFjves2gumxjguOWUN0JpoUZdpQxQ4d8sSiSnGEH7muhXMrjTs9i03Ky4Y_Wi_FVB_fZlT3KpzaDvDiUxd2YLnSc9Yy33v4R25rTgjzoSggJOh_OFT86h8HdHudImPk_TaJk15uPxlWtLFHiP6wzHVCthGbS5ROvCYU7f1eEYG9TGlFS6VnYqlorNWvASk7Q7uRBht9eCR1Y4KfbNLcb8MsquQXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdc97b83ba.mp4?token=S1O17RHT6s0JWzQyscz9p5TdT_amuT1BlNhahZ8U90OK2MgWXq8GI_qmUiACD-cq6F9RrQuwbSwxQMVOGQSAEsocQryVN20LFyNLw9-IfY5BmWB7kEmgTNT5UJWFjves2gumxjguOWUN0JpoUZdpQxQ4d8sSiSnGEH7muhXMrjTs9i03Ky4Y_Wi_FVB_fZlT3KpzaDvDiUxd2YLnSc9Yy33v4R25rTgjzoSggJOh_OFT86h8HdHudImPk_TaJk15uPxlWtLFHiP6wzHVCthGbS5ROvCYU7f1eEYG9TGlFS6VnYqlorNWvASk7Q7uRBht9eCR1Y4KfbNLcb8MsquQXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان تهران شمال شرق ، محدوده شریعتی میرداماد ستون دود عظیم @WarRoom</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/23500" target="_blank">📅 10:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23499">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzINSDC9qToVuVgC2obXqeTGnRed9sR88TtwvSo-9fCnUwbjRaYB1aWL8kPiSq53JJvkLaAVaRP80zBKSW2NQAfWngK6TyACAGvDHr_t3USsx1jVABewflV2eLAd3oB3_LsH0248yTVVvuKXYx4MaqmhLNNsGVsbzDbig-BsCyOMpP6j4J2cS0FX1aTLwcAQt22-V5WJ2efJf9wvSl-aLeucmBBDv-RXssOw3d4juSknrDluyqxkO-c3c5pT0-uSn6iyh56E8AjW6V-pwFMTqxBbqB3slmjAJTxgsYzF--vveqSJ5oNpgvC8nwEx6GnH7XEWWZ2ePREtrvxqcD_4aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان تهران شمال شرق ، محدوده شریعتی میرداماد ستون دود عظیم
@WarRoom</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/23499" target="_blank">📅 10:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23498">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bC3hLAdqUmC3O1qOFDYDCuFJqazIRf1kibxIfjfDAzKvuyaK8Si0AkciZ0h3-hM0anNUhSF3ti7mHLRXaSXHPqMShYTzUnRlx-HdxbHN-4VP-u1fr0oZIAOMDtkgYvFZSFuTgFTqf_AU9Q5LMI6g4jtzszJ0B2dIHG9jxi3DUa-vwIj98IXzp1mR7EcjHw2XVu7wA-qhGMOlGJqT9Ov5NYQMTsqXBfsKGBueenJmb0ysRxjWTrZpZUEIwlBzTNBzIc9VtJki_k3Tt8HmYO2GrI1Tk6ZJThCgGpUsyZvxG1blsW0nfuUeiPTJRf3pMJWyGnjcyu9wqwhnnyh5iXgQtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن‌ کج بند رضایی: منتظر موشکای با سر‌جنگی ۱ تن به بالا باشید
@WarRoom</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/23498" target="_blank">📅 10:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23497">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57b8923ab5.mp4?token=OvKIPcL2_BG5yPuHYb86tPvv_Z5FrFlYgcT2zV7uW5eyYsMsb1W2RCsv2NjgHoLmc-w1iVde5gj8LVuluyzlUwlPbfnrjl93mdJ2qKc4zqIfjPRwA8mAEU2hNPGdncHd9fAFWnP7gzygXc3ffETM1PwipA85rjUFkcKRL7UKTuty-SdAAbCoXPwL1JGIOnZ6RRqxXY7tk7AxTjxNYOkwUSrx_YdKLOhdSZum9V4thHr9LMKbN8wevxJx9yX2DoDOZF9WXPr76ti7diKjW_3bt8hldMK9qyAVXd3eQri-UNf0mI7p_xq2yv8w838l-izIqTRlgJh6fU8y13k6YdbdnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57b8923ab5.mp4?token=OvKIPcL2_BG5yPuHYb86tPvv_Z5FrFlYgcT2zV7uW5eyYsMsb1W2RCsv2NjgHoLmc-w1iVde5gj8LVuluyzlUwlPbfnrjl93mdJ2qKc4zqIfjPRwA8mAEU2hNPGdncHd9fAFWnP7gzygXc3ffETM1PwipA85rjUFkcKRL7UKTuty-SdAAbCoXPwL1JGIOnZ6RRqxXY7tk7AxTjxNYOkwUSrx_YdKLOhdSZum9V4thHr9LMKbN8wevxJx9yX2DoDOZF9WXPr76ti7diKjW_3bt8hldMK9qyAVXd3eQri-UNf0mI7p_xq2yv8w838l-izIqTRlgJh6fU8y13k6YdbdnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست درباره ایران: ویرانگری حملات نظامی ما علیه ایران تاریخی و بی‌سابقه بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/23497" target="_blank">📅 09:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23496">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ec58e117.mp4?token=H51OQnTlE8uaESx2qCq_PjuVLmDv-o6EAYyrjJvd8CcoolndxeCJRtk_mAr8MLenJ0UzsHjNjRDG1-CM_XjiC5_uA5EyQ8GrkhUn9hkEaJw34IuMPlcSoTOzroUJ52rU8e-p7nycxWpVZvxAm_n_2Dxp0DRyZwyBzKoO2eVsXMnmWYRhLFXPHN1kDooqBKpbN02j5mV2dnk6yqhdmr0IP6it00gPD43XOek-4wooD7QSn9xBruK4DHaWS9mOhez_FhWchnxCjF9pVX4BZ1p5haZt5Gx4G070X83jUb1LxOUAfuop_x_YwiRenoZKR_lHPhQsZt6b_7cobxa4sr5Tjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ec58e117.mp4?token=H51OQnTlE8uaESx2qCq_PjuVLmDv-o6EAYyrjJvd8CcoolndxeCJRtk_mAr8MLenJ0UzsHjNjRDG1-CM_XjiC5_uA5EyQ8GrkhUn9hkEaJw34IuMPlcSoTOzroUJ52rU8e-p7nycxWpVZvxAm_n_2Dxp0DRyZwyBzKoO2eVsXMnmWYRhLFXPHN1kDooqBKpbN02j5mV2dnk6yqhdmr0IP6it00gPD43XOek-4wooD7QSn9xBruK4DHaWS9mOhez_FhWchnxCjF9pVX4BZ1p5haZt5Gx4G070X83jUb1LxOUAfuop_x_YwiRenoZKR_lHPhQsZt6b_7cobxa4sr5Tjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ما در جنگ با ایران با اختلاف زیادی در حال پیروزی هستیم.
@WarRoom</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/23496" target="_blank">📅 09:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23495">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd8ba38435.mp4?token=eybqIuZX7eT6C23UvhlKdZKDC1xdEvr2llB2B0DEOiVp3NgpsXC1NNdE1o-Zeamw1zw0du2-kdKHj4ga-2wLsHeub97Po_r79CgtHbU5vAfVVJLc1dSmSnw3t0Yrd59giGvncgjcSJztfNL0DFdymR_T8sRQtcWrRMBoGHC-qmayKb6GBr7W0iNaTmT-Lk348qkiMzR4SRSH2ue2RX-8Z1rVkRO9sWfTTPgRg1HH9TpXwdJrJWn5P9Kx4dHTFuxIhdaayXg-_-McRBvvpikV1dqZdvG3PRc1Wn7pq3q4nQDhhmeD_c5MWltXpDEp6jY3sG2K33dXzdKSFv6sKRQ9cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd8ba38435.mp4?token=eybqIuZX7eT6C23UvhlKdZKDC1xdEvr2llB2B0DEOiVp3NgpsXC1NNdE1o-Zeamw1zw0du2-kdKHj4ga-2wLsHeub97Po_r79CgtHbU5vAfVVJLc1dSmSnw3t0Yrd59giGvncgjcSJztfNL0DFdymR_T8sRQtcWrRMBoGHC-qmayKb6GBr7W0iNaTmT-Lk348qkiMzR4SRSH2ue2RX-8Z1rVkRO9sWfTTPgRg1HH9TpXwdJrJWn5P9Kx4dHTFuxIhdaayXg-_-McRBvvpikV1dqZdvG3PRc1Wn7pq3q4nQDhhmeD_c5MWltXpDEp6jY3sG2K33dXzdKSFv6sKRQ9cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: هفته آینده در سازمان ملل سخنرانی می‌کنید. پیام شما چیست؟ ترامپ: سال گذشته، اپراتور تله‌پرامپتر من را از ورود به سالن منع کردند. بنابراین مجبور شدم بدون تله‌پرامپتر آنجا بایستم. جالب نیست؟ خبرنگار: پیام شما چیست؟ ترامپ: یادتان هست؟ آن‌ها پله‌برقی را خاموش کردند. خوشبختانه بانوی اولم خیلی محکم بود و توانستم پشت او یا بخش دیگری از بدنش را بگیرم. در واقع، دستم کمی پایین‌تر از پشت او قرار گرفت و محکم گرفتمش.
@WarRoom</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/23495" target="_blank">📅 09:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23494">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4f409e707.mp4?token=hAK3kGvplb_Mb-QtHb18NXJJuINNl0UNS7lYk1CZi0DFwXmc1zF7PGtUvvVT4gSSs7SgXXD_OFhDmSb5c3hiYWSWzteH13jQxUOc_kalKgJui4fJpjpHu2kVOW074FS6TjIj0WSWmrQobUmQVuGzae_b9rcmCIEcoMfn0Dr5rneDnC5a8VqqAG_WZS-935J08kyJ_lCUCRBOhqWX9U-PaI4TEVCWmEZ1CvlDrctvOjI7riA8t8I5czB3JA7WpeULsHH-LUlouiEGa_jFJgNGyI3tRp29w6cuEqE7Lqmyvx7yqhvii_c8LomWq0gv2R-KSb9dTk07uDApkzo90sqnGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4f409e707.mp4?token=hAK3kGvplb_Mb-QtHb18NXJJuINNl0UNS7lYk1CZi0DFwXmc1zF7PGtUvvVT4gSSs7SgXXD_OFhDmSb5c3hiYWSWzteH13jQxUOc_kalKgJui4fJpjpHu2kVOW074FS6TjIj0WSWmrQobUmQVuGzae_b9rcmCIEcoMfn0Dr5rneDnC5a8VqqAG_WZS-935J08kyJ_lCUCRBOhqWX9U-PaI4TEVCWmEZ1CvlDrctvOjI7riA8t8I5czB3JA7WpeULsHH-LUlouiEGa_jFJgNGyI3tRp29w6cuEqE7Lqmyvx7yqhvii_c8LomWq0gv2R-KSb9dTk07uDApkzo90sqnGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: اگر از مردم بپرسند که کاهش قیمت بنزین را می‌خواهند یا اجازه بدهند ایران به سلاح هسته‌ای دست پیدا کند، نتیجه رأی‌گیری با اختلاف بسیار زیادی به نفع جلوگیری از دستیابی ایران به سلاح هسته‌ای خواهد بود. مردم نمی‌خواهند ایران سلاح هسته‌ای داشته باشد
@WarRoom</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/23494" target="_blank">📅 09:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23493">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ilaer43TEWgIh7Pi5Th_vXyKJOjSFQ9yMUsyqx6IJBFgMFZfM6J7Kun4gwChh9Dr4Oks4CLnkS_7Fu_8yM60vuzD3ImifKQDwCkqVlkSEk84XH9U_P1hT8AxjbIYsHPPq6o5fFwXQ8vfpGa-fp2XUzokGq7C7TXbsBFS6Ivvx77YNPvoD6zLCN_GgIQjY9quDIA-Ij_WSWZS_oNDU5G2ZTZaghI17YW6Vw0-kJ59Q2Chk859IWrApOx_BFBErivnLQY935gyf5KfgMmbXIoFX2q7sEanQo6XZwzpP1F_ySTFgLRu_WaD8rjFOUNouUidvWFiNlDvw1gWt6hTSwjgmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام
حسین پدران،
فرزند حمیدرضا اجرا شد؛ رسانه‌های ایران به نقل از مرکز رسانه قوه قضاییه اعلام کرده‌اند که او به اتهام همکاری اطلاعاتی با موساد و انتقال اطلاعات درباره سایت‌های موشکی و نظامی در اصفهان محکوم شده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/23493" target="_blank">📅 09:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23491">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lmRAknNBEC3ANpjS5E3iuMP4Y90Q3MFBNpZJU8GvwF2tX9Nxb3j6Myjz_ntDRA-CX2LSknMcefAogLufkPL3poQmGQ1uRwTJwwt8pdQWVCtbmvy4bCI6G5gKHqR3MjlSTdEMf7UwNZ2eladKXyadVK7ywUQaCO4o1USddECfmvDoycGB1_0dshjK-E6zYzwN2JrSJlWHJ1RoXqQjGHa8x1lr0Kz6Xh_M4KfGzNIeZXkaReNYhhs2g1drjzsZSEwWE14swoDMVzFX9MSSB1Z-jQSvxVrRHsooCmNwcBvcp4FzgDSIxhCN-p8MEYSXBjeQV1clTJZeZBdqCR_H5S5d5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/POoSxjJ8tkBnwo7_StGjk6KMlLoFOOeL-VHoLSIOHKQlwbdEiay2JaCnVOu2YZeCRA4aN_IC_Nr0SzpJlAJsHkCCWfc5UeD4SaxYyPh81RLsYANmVZWPijNPDwD85zZZwKhiApVVfXZRYZRU-9V-ymf2R2KAJlKEGV51x2lC7H4EZnhFvURQQmzFt9ZTHqpQmFfe2Zagiada1Qc67Z6bQbIVlxhOS1_Rz74CAHnJKqCzXs-1OeNA23S6LTsb36aux0a2m4m3v8zY0Vqu4SLz7iLuRmYzYgXiY1_-JZc1pAK0NVbeET-1uPFSCQEfUdIvv771UReBCjrzpMqmQkv59A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ در پستی در شبکه اجتماعی تروث سوشال، فهرستی با عنوان «۲۵ دستاورد برتر ترامپ در سال‌های ۲۰۲۵ و ۲۰۲۶» منتشر کرد و در آن، از سیاست‌های مهاجرتی، کاهش مالیات، اعمال تعرفه‌های تجاری، افزایش بودجه نظامی، گسترش حفاری نفت و گاز و لغو برخی سیاست‌های اقلیمی به‌عنوان دستاوردهای دولت خود نام برد. مورد مرتبط با ایران در این فهرست، بند ۱۱ است؛ جایی که ترامپ مدعی شد آمریکا در عملیات‌های «چکش نیمه‌شب» و «خشم حماسی»، ظرفیت غنی‌سازی هسته‌ای ایران را نابود کرده تا به گفته او، ایران «هرگز» به سلاح هسته‌ای دست نیابد.بند ۹ نیز به افزایش بودجه نیروهای مسلح آمریکا تا یک تریلیون دلار در سال جاری و برنامه برای رساندن آن به ۱.۵ تریلیون دلار در سال آینده اختصاص دارد
@WarRoom</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/withyashar/23491" target="_blank">📅 09:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23490">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ExDrXP00tLBqh3UR_Ign69aAL58g-uk2Wp-7mHQcd9F2GR8GdQxHWlKm85mLxcCG-AWVpa8fLDFGGtKcNu_4mPa-8EkAUtMFasM7xUAlGKzk7lgMT4OgPDppTKqwFkiPXjkOfEBB1m63JWTyZkm2EADPUjAoRSDeRrVi42wCjvrL_sJHDvdD_Dr-8zY8d7OfNLO1dqDZb2mzcHMV0mmG01Bzpi3vTtnjACpkHS3Ys9bregOecMp5P8p1ia1KFiQd8C4dOuSBip2vcejZoghCtDMbGEBUIyZOZ2g-mdqpdCOFO8OvVmCgkuhS-pgaMwqU5QeXDMtEtuMZxy_v7eq57A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیم جونگ‌اون از خط تولید پهپادهای انتحاری یک‌طرفه بازدید می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/23490" target="_blank">📅 09:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23489">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUIuvLlGY-U-uhplEMIIiEDskSIaWygkSB-AQP8ADwUhXu2_B3BdePBHIiHXAD4ADJkD7pzT7CLCDYfp2jT9oHLi-tHbrxRtlCagMEyPqopm7jCkxNQo-UtcuHUe3DL2t_zAF1YfxXe-H_tEhHdCFz0l6HMB9_B-ZiFqSn5-e-xwtuEC7GC9MwuUlslV0-DA1lcmooDciJoNrb0IxlfgLAbn842IoCUHJ2FYosfQ0lTcUHtG48JnXYLz2Yt3784vcLDJkpLzX_D7VnMa46Bz_wvPka5GgMx2_hU29R_a9GcmOADIwk9i5p_gquTBIQO8zwIF0inNrL_lrTzdU2lupQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نهاد ناظر بر امور بانکی ترکیه مجوز فعالیت شعبه استانبول «بانک ملت» را لغو کرد؛ بانکی که صددرصد متعلق به دولت ایران است و از سال ۱۹۸۲ در ترکیه فعالیت داشته است.سازمان تنظیم مقررات و نظارت بانکی ترکیه (BDDK) دلیل این اقدام را تهدید علیه ثبات نظام مالی عنوان کرده است.این بانک پیش‌تر و در پی تحریم‌های آمریکا تا حد زیادی از شبکه بانکی جدا شده بود (قطع دسترسی به سوئیفت و حذف از سامانه انتقال الکترونیکی وجوه یا EFT ترکیه)، اما این تصمیم به معنای پایان رسمی فعالیت‌های آن است.
@WarRoom</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/withyashar/23489" target="_blank">📅 08:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23488">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08184bf9e6.mp4?token=qEeOO00yCX8EaLkJ7tqXqKv38X3coqTealufeaboyaGbQ4LE8_5HoIIwwfYl-T7U4TOdTEwn0MyXMzz_T-ZgaEaDk5zlITC3YpvTTQ1QJD0MMS0uPU-TTWFiWFBn9qkAah2SCK8Xzq1CFNfgUMoDr1oztEB0LyaIdCR86f0jSlfc3c_r-ElQV7fB6EjZ6YVzlSd90DvTE_RgoPQRNjkeYIPGunq9E5OzofFKpWTBl7a2hviCZr23GsZf9Ou8pMnqSbfFiDDc_ekW_k60RsgkUigFDa4jMYyLOYDE9wHjDXXQUSl-ZcPOiH1bBIHCJ2gnGuZRJZLQsvhomOvwYtWOsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08184bf9e6.mp4?token=qEeOO00yCX8EaLkJ7tqXqKv38X3coqTealufeaboyaGbQ4LE8_5HoIIwwfYl-T7U4TOdTEwn0MyXMzz_T-ZgaEaDk5zlITC3YpvTTQ1QJD0MMS0uPU-TTWFiWFBn9qkAah2SCK8Xzq1CFNfgUMoDr1oztEB0LyaIdCR86f0jSlfc3c_r-ElQV7fB6EjZ6YVzlSd90DvTE_RgoPQRNjkeYIPGunq9E5OzofFKpWTBl7a2hviCZr23GsZf9Ou8pMnqSbfFiDDc_ekW_k60RsgkUigFDa4jMYyLOYDE9wHjDXXQUSl-ZcPOiH1bBIHCJ2gnGuZRJZLQsvhomOvwYtWOsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست: در طول ۲۵۰ سال گذشته، ما همواره به آمریکایی‌هایی نیاز داشته‌ایم که برخیزند و بگویند: «مرا بفرستید.»
چه کسی با «قرمزپوشان» (نیروهای بریتانیایی) خواهد جنگید؟ چه کسی به نبرد با کمونیست‌ها خواهد رفت؟ چه کسی با اسلام‌گرایان خواهد جنگید؟ چه کسی مبارزه خواهد کرد؟همواره آمریکایی‌هایی بوده‌اند که گفته‌اند: «مرا بفرستید.»
@WarRoom</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/23488" target="_blank">📅 08:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23487">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdI2AuyfYz8yJ-a6_j-QWOP8_mXTG1PoLbVwoRPsZMl4FxL2pg3bjRk0Wb117osTuCA1zMBWhV3G3oMvE782cD98zq900TkU-bPPCTxiK3uCMEc1qtXf5B_VI1OlaZ9LgLP1lDP3BcqOhHi-Cq_2X7uuj8rZAE7IG0R0lGxwqDJxkXn7omM4AFRpcyNsn1nsleZfqwrYzTlHZVMrHo_vksGBdW5qrh1dKcf1yDbbSyTg1cDiCF5Ty7N9TYI2Mf8cnWkvksVHwTxmssEZSnao6m43OBAOgZofsJZQ2dAqvc9lKAnlVDwGSB8Jk-3fxuucd8aXOYZPOVhIs2kTIO5VmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنتاگون پس از توقف موقت این طرح در اوایل ماه جاری، اکنون در حال پیشبرد برنامه غربالگری اجباری سطح تستوسترون برای نظامیان مرد ۳۰ سال و بالاترِ ارتش ایالات متحده است. بر اساس دستورالعمل‌های جدید، این آزمایش در معاینات دوره‌ای سلامت و ارزیابی‌های سالانه گنجانده خواهد شد و مسیرهای درمانی استانداردی نیز برای موارد کمبود تستوسترون در نظر گرفته شده است. نظامیان جوان‌تر نیز می‌توانند به‌صورت داوطلبانه درخواست انجام این آزمایش را بدهند.
@WarRoom</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/23487" target="_blank">📅 08:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23486">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4q5RfehQhEQrkpQP6nlv8DjzeOLn9giBtFJ0sUfCkdDpr0M8CT30ATxVxJR-dSg_pJTl1UX2nd0TmsFgJ7vnZj3ge77gXF_d2dwsU1b9c1fMhNijryxKQDQJoSH-uKz0eYov96r-9yZfketCkUrp2tpBW8Ywj1EHIv1_xhcqTn2dKw2zQ30YB1ACZTuqv5TuaNG6HP6DBWcy1GjVUwgx4A4I3qERbeMmKvLnvJc2C0QYklw5qg_HDjVg-q3me_AeB9Fd6dimD_ca7DMrcaGyZo__gk06aP1972HHUOfkq5aBaxiSl7sCp2KN7mHV9uajdv6zCuwoXJNDPCArkZwMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه ایالات متحده با فروش تجهیزات پدافند هوایی و خدمات پشتیبانی به ارزش ۲.۶۸ میلیارد دلار به اوکراین موافقت کرده است.این بسته شامل سامانه‌های پدافند هوایی با برد بیشتر، پرتابگرهای متحرک، رادارهای مقابله با پهپاد، قطعات یدکی، نرم‌افزار و پشتیبانی فنی است.اوکراین هزینه این خرید را از طریق کمک‌های اروپایی و بودجه‌ای که پیش‌تر تحت برنامه «تأمین مالی نظامی خارجی» ایالات متحده اختصاص یافته بود، تأمین خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/23486" target="_blank">📅 08:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23485">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ قانون «تحریم روسیه و ایران، لیندسی او. گراهام» در سال ۲۰۲۶ را امضا کرد. این قانون تحریم‌های موجود علیه ایران در حوزه انرژی و تسلیحات را برای ۵ سال تمدید می‌کند و امکان تحریم پوتین، الیگارش‌ها، بانک‌ها، شرکت‌های انرژی و دفاعی و ناوگان نفتکش‌های سایه روسیه را فراهم می‌کند. همچنین به رئیس‌جمهور آمریکا اختیار اعمال تعرفه تا ۱۰۰ درصد بر کالاهای کشورهایی مانند چین و هند که نفت و گاز روسیه می‌خرند و تا ۵۰۰ درصد بر برخی واردات روسیه را می‌دهد. ترامپ می‌تواند این اقدامات را تعلیق یا لغو کند.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23485" target="_blank">📅 05:58 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23484">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ برای گذراندن آخر هفته راهی کمپ دیوید شده است؛ طبق برنامه رسمی، او شنبه و یکشنبه در این اقامتگاه خواهد بود و برنامه‌های این دو روز با عنوان «زمان اجرایی» و بدون حضور رسانه‌ها ثبت شده است.  هم‌زمانی این سفر با تحولات جنگ ایران مورد توجه قرار گرفته
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/23484" target="_blank">📅 00:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23483">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">گزارش ها از
هدف قرار گرفتن نزدیکی اقامتگاه بن سلمان
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/23483" target="_blank">📅 00:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23482">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8fa371e84.mp4?token=g2KPaCWfgPkGusIa_mKnX7Tkn4PelQqlkilu43rhCtTDwMsho6524NXy_OQfR0M6OfBc79KcBU7Cl-tzDKk3ovD_aJIw1TkuPWVa10abBpr5xjNRgz5fwzr6cflZLli5vo4UtCa7NryDyr_VM_8k3WNYei1SVn49dxnwyH_SLkXwOPZJDujDKvVQFrtPFVGpT4RqGsVZ03hdr-x039kSAT0SE_Jhww8kIxKBOB4GO8qkz3c5Raq6kab38MR10nCkYC5ahEotq3X6DJBUPFGRI8cR1R6Qi_RJ6ohC2DXMOMMNKSQp5EbWTsRUZZoXiGTwLB0eTJmFhsqgacvoRy1rsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8fa371e84.mp4?token=g2KPaCWfgPkGusIa_mKnX7Tkn4PelQqlkilu43rhCtTDwMsho6524NXy_OQfR0M6OfBc79KcBU7Cl-tzDKk3ovD_aJIw1TkuPWVa10abBpr5xjNRgz5fwzr6cflZLli5vo4UtCa7NryDyr_VM_8k3WNYei1SVn49dxnwyH_SLkXwOPZJDujDKvVQFrtPFVGpT4RqGsVZ03hdr-x039kSAT0SE_Jhww8kIxKBOB4GO8qkz3c5Raq6kab38MR10nCkYC5ahEotq3X6DJBUPFGRI8cR1R6Qi_RJ6ohC2DXMOMMNKSQp5EbWTsRUZZoXiGTwLB0eTJmFhsqgacvoRy1rsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: جنگ به زودی به پایان خواهد رسید و وقتی این اتفاق بیفتد، قیمت بنزین شما به سطحی که قبل از آن داشت، کاهش خواهد یافت، شاید حتی کمتر از آن.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/23482" target="_blank">📅 23:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23481">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">العربیه: وزیر خارجه پاکستان محسن نقوی در ساعات آتی به ایران عزیمت می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/23481" target="_blank">📅 21:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23480">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">المانیتور: یک منبع ارشد اطلاعاتی اسرائیل می‌گوید نهادهای امنیتی اسرائیل در حال حاضر با
حمله پیش‌دستانه علیه حوثی‌ها مخالف‌اند
. به گفته او، حوثی‌ها اکنون هیچ بازدارندگی مؤثری از سوی آمریکا، اسرائیل یا عربستان ندارند و به «اسب تیره» منطقه تبدیل شده‌اند؛ تهدیدی غیرقابل‌پیش‌بینی که می‌تواند عربستان و متحدانش را به اسرائیل نزدیک‌تر و وابسته‌تر به توانمندی‌ها و اطلاعات اسرائیل کند
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/23480" target="_blank">📅 21:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23479">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آسوشیتدپرس:
سقوط بقایای یک پهپاد حوثی پس از رهگیری در عربستان باعث کشته‌شدن یک نفر شد.
پدافند عربستان پهپاد را منهدم کرد اما بقایای آن روی منطقه مسکونی سقوط کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/23479" target="_blank">📅 21:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23478">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">الجزیره: یک منبع مطلع آمریکایی اعلام کرده حدود
۶۰ میلیون بشکه نفت ایران، یا نفتی که مشکوک به منشأ ایرانی است،
روی نفتکش‌های تحت تحریم سرگردان مانده است. به گفته این منبع، نفتکش‌هایی که خارج از محدوده محاصره دریایی قرار دارند نیز در معرض رهگیری هستند و به همین دلیل با سرعت کمتری محموله‌های خود را تخلیه می‌کنند. همزمان، واردات نفت چین از ایران یا محموله‌های مشکوک به ایرانی بودن به حدود
۴۴۰ هزار بشکه در روز
کاهش یافته است
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/23478" target="_blank">📅 21:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23477">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJvuwr6fF69GynC9bqoBUo1H-1FwKMGXfWusKAPS-N2RBYorPzCNGS_VjZT_GJj4mf7NIIICJ3zSqfshaqPQhVJ6IsNEiqOwV9YFw4H5e__sW3ZHGz0tdBpdsoBzBhwaLH23DrSYeaqBJZqwDlE8A98NHV15noPyxi7qMG4lEQ_30f5c8CumqRSenM5mk-moqkpr-8S8yrSyPsYUS5sbGkIgRLUAveLuyfDtsWpLRde1_O1wrQOvXOF9cB_shP-PEUCaq1qr9Fdh-zZwR3gfxBrdZ__TVoi-_KLB0Jvlw8QWzDg7bsIhxbfO8YK03kh1Z6jdqG7ziwkZgJ20MZphqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاليباف
:
دوره‌ای که در آن F-35ها و F-15های شما شکار می‌شوند و مجبورید گزارش دهید که آسیب دیده‌اند
🤏
از قبل آغاز شده است.
آنچه زمانی سوخت خالص کابوس بود، اکنون واقعیت روزانه است. با آن زندگی کنید.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/23477" target="_blank">📅 21:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23476">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">الجزیره: وزارت خزانه‌داری آمریکا اعلام کرده اقدامات سختگیرانه‌ای علیه بانک‌ها و مؤسسات مالی در امارات و ترکیه که به گفته واشینگتن از ماهان‌ایر و شبکه‌های مرتبط با آن حمایت می‌کنند، آغاز کرده است. این اقدامات با هدف قطع مسیرهای مالی و خدماتی مرتبط با جمهوری اسلامی و ماهان‌ایر انجام می‌شود. آمریکا پیش‌تر نیز چند شرکت در امارات و ترکیه را به اتهام ارائه خدمات به ماهان‌ایر تحریم کرده بود. هنوز نام بانک‌های هدف، نوع دقیق محدودیت‌ها و زمان اجرای کامل این اقدامات اعلام نشده است. همزمان، ماهان‌ایر اعلام کرده از ۳۰ شهریور پروازهای خود به استانبول و آنکارا را متوقف می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23476" target="_blank">📅 20:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23475">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بر اساس گزارش رسانه‌های تحلیلی مستقل، دولت ترکیه ابلاغیه جدیدی به سنتکام ارسال کرده و هرگونه بهره‌برداری از پایگاه هوایی اینجرلیک برای سوخت‌رسانی یا هدایت پروازهای رزمی علیه هدف‌های منطقه‌ای را اکیداً ممنوع اعلام کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23475" target="_blank">📅 20:30 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23474">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ به نیوزنیشن : باید ببینیم که آیا ایران نابود خواهد شد یا خیر
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/23474" target="_blank">📅 20:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23473">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ در پاسخ به سئوال نیوزنیشن درمورد گزارش روز پنجشنبهِ اکسیوس درباره «تصمیم بزرگ» او: «آنها حالا می‌خواهند به توافق برسند. اگر این توافق، توافقِ درستی نباشد، حتی به آن فکر هم نمی‌کنم.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/23473" target="_blank">📅 20:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23472">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ: ممکن است به سمت جنگی تمام‌عیار با ایران پیش برویم.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/23472" target="_blank">📅 20:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23471">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ: ایالات متحده در حال مذاکره با حوثی‌هاست و آن‌ها نیز به دستیابی به توافق با آمریکا تمایل دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23471" target="_blank">📅 20:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23470">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">برنامه «پاداش برای عدالت» وزارت خارجه آمریکا برای اطلاعاتی که به مختل کردن سازوکارهای مالی سپاه پاسداران، از جمله حساب‌های رمزارزی، متولیان نگهداری دارایی‌ها و شرکت‌های پوششی، کمک کند، تا سقف ۱۵ میلیون دلار جایزه تعیین کرد. و همچنین اعلام کرد سپاه پاسداران…</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/23470" target="_blank">📅 20:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23469">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23469" target="_blank">📅 20:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23468">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">رویترز: آمریکا به هیات اصلی جمهوری اسلامی، از جمله مسعود پزشکیان و عباس عراقچی، اجازه داده است هفته آینده برای شرکت در مجمع عمومی سازمان ملل به نیویورک سفر کنند. این هیات کوچک‌تر از سال گذشته خواهد بود، اما اعضای آن با محدودیت تردد در مناطق مشخص نیویورک و ممنوعیت خرید کالاهای لوکس و برخی کالاهای دیگر، از جمله عضویت در فروشگاه‌های عمده‌فروشی، مواجه خواهند بود.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/23468" target="_blank">📅 18:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23467">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وال‌استریت ژورنال: تلاش جمهوری اسلامی برای دور زدن محاصره دریایی آمریکا از طریق انتقال تجارت به مسیرهای زمینی با مشکل جدی روبه‌رو شده است. صدها کامیون در مرز پاکستان و هزاران کامیون در مرزهای ترکیه، ترکمنستان و افغانستان گرفتار شده‌اند و تأخیرهای گمرکی و افزایش هزینه‌ها روند انتقال کالا را مختل کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/23467" target="_blank">📅 18:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23466">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">حکم اعدام امید گودرزوند چگینی، ۳۷ ساله و از بازداشت‌شدگان اعتراضات ۱۸ دی در قزوین، در دیوان تایید شده است. او در زندان چوبیندر قزوین محبوس است و پس از ۴۰ روز نگهداری در سلول انفرادی بازداشتگاه اطلاعات سپاه، بدون دسترسی به وکیل محاکمه شد. به گفته این منابع،
این زندانی پیشتر از کارکنان نیروی انتظامی بوده و استعفا داده بود
.
@WarRiom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23466" target="_blank">📅 18:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23465">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تنگه صدای زوزه ابومهدی المهندس میاد
@WarRoom
😂</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23465" target="_blank">📅 17:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23464">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ادعای رسانه های رژیم :  شلیک ۴ فروند موشک کروز «ابومهدی المهندس» از جزایر ایران به سوی اهداف متخاصم در دریای عمان
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23464" target="_blank">📅 17:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23463">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بیانیه نیروی انتظامی‌ ، فرد دستگیر شده در ماجرای تبریز دارای چه سوابقی بوده؟
نوامیس مردمو تو تاریکی با قمه خفت کرده! با چاقو زده لب و شکم یکیو پاره کرده
با قمه زده شُش یه نفرو سوراخ کرده، یکی از آنها با شیلنگ نفس می‌کشه!‌
مواد فروش هم بوده و
….
نیروی انتظامی همچنین اعلام کرد این سوابق به هیچ عنوان رفتار خارج از قانون مأموران را توجیه نمی‌کند. مأموران خاطی تنبیه انضباطی شده و پیگیری‌های قضایی ادامه دارد.
@WarRoom
یاشار : من انقدر به این مامورای نیروی انتظامی پول دادم که تمام رفتارشون رو توی شرایط خاص می‌دونم. از لحظه اولی که ویدیو رو دیدم کاملاً متوجه شدم که این قضیه ناموسی هست. در نتیجه با این‌که پیام های بسیار برای انتشار این ویدیو فرستادین ، از انتشار اون خودداری کردم. مثال خیلی ساده‌ای از طرز فکر و نگاه من و کسانی که این ویدیو رو فرستادن و بارها اصرار کردن تا منتشر کنم.</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/23463" target="_blank">📅 16:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23462">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گزارش فاکس‌نیوز : دونالد ترامپ، رئیس‌جمهور آمریکا، در حالی وارد
هفته‌ای سرنوشت‌ساز در سازمان ملل
می‌شود که موضوعات ایران، چین و هوش مصنوعی هم‌زمان در کانون توجه قرار گرفته‌اند. نتایج یک نظرسنجی جدید «فاکس‌نیوز» نشان می‌دهد که ۷۱ درصد از رأی‌دهندگان معتقدند دولت ترامپ فاقد راهبردی روشن برای پایان دادن به جنگ با ایران است؛ این در حالی است که ترامپ در حال بررسی احتمال انجام حملات بیشتر علیه تهران است.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23462" target="_blank">📅 15:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23461">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">فایننشال‌تایمز: ایران برای دور زدن محاصره دریایی آمریکا، انتقال بخشی از تجارت خود از مسیر دریا به مسیرهای زمینی، به‌ویژه مرز ترکیه، را افزایش داده است؛ ترافیک واردات از این مسیر در اوایل سال ۲۰۲۶ حدود ۲۵۰ درصد رشد کرده، اما تأخیرهای گمرکی و هزینه حمل‌ونقل افزایش یافته است
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23461" target="_blank">📅 15:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23460">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">آسوشیتدپرس: چندین هزار نفر روز جمعه ۱۸ سپتامبر در تهران در تجمعی حکومتی علیه آمریکا و اسرائیل شرکت کردند؛ مقام‌های جمهوری اسلامی از ثبت‌نام بیش از ۶۰۰ هزار نفر برای آموزش نظامی خبر داده‌اند، اما این آمار مستقلانه تأیید نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23460" target="_blank">📅 15:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23459">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">شرکت آرامکو سعودی به پالایشگاه‌های نفت اروپایی اطلاع داده است که در ماه آینده نیز هیچ محموله‌ای از نفت دریافت نخواهند کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23459" target="_blank">📅 14:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23458">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نتانیاهو درباره ایران: اول از همه، ما باید رژیم ایران را سرنگون کنیم. این مأموریت من است و این مأموریت اصلی ماست. @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/23458" target="_blank">📅 14:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23457">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">رویترز:
کره جنوبی اعلام کرد هیچ نیروی نظامی را برای ورود به درگیری خاورمیانه اعزام نخواهد کرد. سئول در عین حال در حال بررسی راه‌هایی برای حفاظت از کشتی‌های تجاری، مسیرهای انرژی و شهروندان خود در منطقه است
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23457" target="_blank">📅 14:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23456">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ایلان ماسک: «یا باید ویدیوگیم بازی کنید یا احمق بمانید؛ فقط همین دو انتخاب را دارید.» این اظهارنظر در واکنش به پژوهشی روی ۹۲۳ نفر مطرح شد که نشان می‌دهد گیمرها در عملکردهای شناختی، مشابه افراد حدود ۱۳.۷ سال جوان‌تر عمل می‌کنند. این مطالعه همچنین ارتباط بازی منظم با عملکرد بهتر حافظه، استدلال و سرعت پردازش اطلاعات را نشان داده، اما ثابت نمی‌کند که بازی‌کردن مستقیماً باعث جوان‌تر شدن مغز می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/23456" target="_blank">📅 13:30 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23455">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXFZYRwzHsgZOWPetSTQMo8ofbTIMfvgSU17c9aySSqBgGKpmuAhM0-WjcaiMKz2oLElB0STT7ZSzlEdDKZAROHCSLD9dbbouT4W9IxKLvgcj2FHeGHNR4B0Bwqkb0fQb1sksd41bx-rfQdbECuD17QBQBuriuU2Ebt9X41KpRYYrrC0n6JjSziXp_-F0DGMgAjuRWAWgvXa2Fb0JQLCNqjuPsMRLHLMa8l5yP8nqJDPoFNMF91l_owHH5kI9DVVNFrObkqde2y1ywzcdNHIquMzDDLopqSDUximLIUFZSswHkNfhXvwQiV4DZPVjdnzwyaQVno-Uc2vuVHohuM1sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون ستون دود شرق تهران
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/23455" target="_blank">📅 12:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23454">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">جی‌پی مورگان: بیت‌کوین می‌تواند از طلا جلو بزند؛ تحلیلگران این بانک می‌گویند اگر سرمایه‌گذاران از مواضع دفاعی خود در
صندوق‌های قابل معامله در بورس (ETF)
بیت‌کوین خارج شوند، احتمال افزایش تقاضا برای بیت‌کوین و عملکرد بهتر آن نسبت به طلا وجود دارد. این بانک همچنین اعلام کرده صندوق‌های طلا بخش عمده خروج سرمایه‌های سال ۲۰۲۶ را جبران کرده‌اند، در حالی که صندوق‌های بیت‌کوین تنها حدود نیمی از خروجی‌های قبلی را بازیابی کرده‌اند.
بیتکین در این لحظه از 78,000$ عبور کرد
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/23454" target="_blank">📅 12:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23453">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpmWEEWBt7xpQz6WYb8a8tH21T7pbhncmFDgKs1arsWYbEv8NT0voN0eXNviwTgEJpRuAAJ4Ttsysv-HSOy2gMPmBs5eVhw5PZvO-dupkTXJFv7Zgdyo4OFJRcPzUsrDSYINPnJyKto0FvrL5oLQYJEUfw989RZRKwRHCBGbv7UUgwRMzXNo4buG3HK0oo-vgWf1m29WrX4bnRKBLtAGc__UFmwE6aSttCQkGEYvjP82nm9luWOEFMFYmpWdz4Mtfp5rswo6aadGCaCHygjhnaG60-1IRzZvmSVVlxSGkt7874HiNsQZaZRr4kAm6HiMkBdf5Sd7gCko3vmELdv8Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز جان فدا ریختن بیرون، رژه میرن. این وسط هم دوتاشون مزدوج شدن. قیافه داماد شبیه کندفیله(یه مار حشره خوار) نمیدونم بشناسینش یا نه
@WarRoom
😂</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/23453" target="_blank">📅 12:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23451">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HxNvaV2ijlwxfFrwhFeqfNvlwF9eN8BDPi7_VU7d4b-XB8k1aWTck9L1DZ6mFB8-mirVKTfswd7SU6_X2cJ2yoz8EODwsbgKOEHUX3QbY4IzcLfubHto5R8bih_HSB53blOJntIgqEKJp90HwSxEo8HBNZPSAh7jfmEj_rIdz0HEjLZC_Ro8HexcdCkOnGwiAaY_9Zg5vpyjEOkYPTGAFydKVisFb0DSkqNLFQXVrmKg_38X5WgJT-WHD6U0ywJErOs3l6AX1Lro_xcqlU9ArObY2oc0HUUdTuL08hFz4eE8rjWqahDo53Pxfl13oXRdolPARvWzu-tfztrPSwY-9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XS-SB8AknhnZkKx28_M0A_1n_RW78BbiArugzsjE6vM0OsDROfKJrtrPMFbITa5UoHdts05Jc7XTpkJQIYVbDghWHrXAUvFAo2DHiJoUC2I8tpSkVlAPDOu45pziILZeCKLQwceH8s1jkW5JqBZyeV40KEGeIYPJHTw3Aet6viyX2iCaZYkgOPJc2mKHUmPsbWwRrwzzZ27qGs2xiKUcj0fVxSXhPN61vI2jSQcSDfAGRLSpi-rl--zjFanypqmpJ6rpY1xnT0LCdov9ceyU_DvfyzSWfrcLvkNV3Gp8dCYasrNeT-at6gGv1WJzizL56D-BmKPoLwsbuJjCjx8L3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمله به سه نفتکش در حوالی تنگه هرمز
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از دو حادثه جداگانه علیه نفتکش‌ها در منطقه تنگه هرمز خبر داد.
حادثه اول: طبق هشدار شماره ۱۳۸-۲۶، یک نفتکش در تنگه هرمز هدف پرتابه‌ای ناشناس قرار گرفت. اصابت پرتابه باعث آتش‌سوزی در کشتی شد، اما آتش بعداً مهار شد. خدمه سالم گزارش شده‌اند و میزان خسارت هنوز اعلام نشده است.
حادثه دوم: طبق هشدار شماره ۱۳۹-۲۶، یک نفتکش در هنگام حرکت به سمت خروج از تنگه هرمز، هدف پرتابه‌ای ناشناس قرار گرفت. در این گزارش، آتش‌سوزی اعلام نشده و جزئیاتی از میزان خسارت نیز منتشر نشده است. خدمه کشتی سالم هستند.
حادثه سوم : تایید نشده دیدبان های اتاق جنگ به من از حمله به کشتی سوم هم خبر میدهند
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23451" target="_blank">📅 11:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23450">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XeAgCA-viY-J1uyF1T7pkK3jy1TBipZSIvZatE88SxEPehKKt0dtYPkYvMqSixWgZHtKUKiCgfM1QQUR6bq0KGNX5HoD_5a3ldDdRLLE3ohtBddUKu8UjAl-g9OO5cMRxLyUhpFUULH_HZEQpy-KfG3PEhw0YsNPJaiZ4X2OdFiudJqRygSybl-VJA0MSpZzo1aMqod05CVCeEuaNqNeXjx2ESzoIMxMZBPwBEceNhDCIrat-qzNnVZSYyoexYu6WY1Bk96mZnzRomuMcK8SBXEVs1ANe4ndAP1YwYoqPNELWG54yEl-yH5HIgUxfpgtj558Z39dlzG7V5rn96wZjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث‌ با بازنشر مقاله‌ای از واشنگتن‌پست درباره افشاگری‌های داخلی پیرامون جنگ ایران نوشت: «خیلی جالب است. حتماً بخوانید! به افشاگری ادامه دهید،
سگ‌های کثیف
!
وقتی شما را پیدا کنیم، بهای سنگینی خواهید پرداخت!!!
» مقاله مارک تیسن، ستون‌نویس واشنگتن‌پست، استدلال می‌کند افشاگری‌ها درباره هشدارهای تولسی گبرد، مقام‌های ارشد نظامی و جی‌دی ونس درباره خطرات حمله به ایران، به‌جای اثبات اشتباه ترامپ، نشان می‌دهد او برخلاف توصیه‌های مخالفان جنگ عمل کرده و تهدیدهای حکومت ایران را جدی گرفته است. تیسن همچنین اقدامات ترامپ علیه ایران را یکی از جسورانه‌ترین تصمیم‌های سیاست خارجی یک رئیس‌جمهور در دوران زندگی خود توصیف کرده است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23450" target="_blank">📅 11:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23449">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">نیویورک‌تایمز به نقل از مقامات آمریکایی:
ترامپ در حال تقویت رویکرد متفاوت برای پایان جنگ اوکراین است؛ پیشنهاد قرارداد تجاری با روسیه
کاخ سفید در حال بررسی امضای قراردادهای تجاری با روسیه، حتی پیش از توقف درگیری‌ها ست
ترامپ می‌خواهد انگیزه‌های بیشتری برای نخبگان روسیه ایجاد کند تا برای صلح فشار بیاورند
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23449" target="_blank">📅 11:36 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23448">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">وزارت خارجه آمریکا اعلام کرد ایالات متحده رسماً از
شورای حقوق بشر سازمان ملل متحد
خارج شده است. واشنگتن این شورا را به ترویج «ادبیات ضدآمریکایی» و اتخاذ رویکردی مماشات‌گرانه در قبال حکومت‌هایی که به سرکوب مردم متهم هستند، متهم کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23448" target="_blank">📅 10:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23444">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qgZSJ0mAtzO_QRPAYjpH5U1x-XImLTnkNd0kHIMAqEaiODoHyawsH4Ygo_vKAJ2MhHF6ebyax_0j1k2-ZV2c8aG1Z_0nLoYh5YAkD5U0sGxhfQjpbtbLcrtwVxbAnN5crfghtoj1wbhG190zhM1HNFb2LkXkAReHf8P4mVHm4nvuRgzUo3bCmazzzPnp-aSjLWc-1FhSCUph6mo9wwaaSnhBpcTOGckmfbIELjkwNYR0JaVGKU4jxAWuwyg17nNB1TIx1Oa-xa_IMGrH9YoTJTj00-1BqxJJITc4sMnRpQ8T6uSEpEUXIXm452jfxaXTXzoJG3ULlVHWwNdOZxxdJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s1F4E8Nva04jZ8TfcVcVHtaN8Fnv7Pc0gR6lBgJ-ExKCOLM1woeZem2qVMF9HOZe1X5t4hsVZQtd_Al8eTJR3sHBJ-qv1NBUYnjCaKLUEaEtxTAJ3eGDUG6fJztQqD0ZkzIn46OpRN65do290CH3dPgUQIupi4gBrC4v1Np28KhKXR4c7U5P1qDknAuhulDoCXcrMFCPiIl_ThkBCDS9nLoJYLK_SzxUGXBu9boQFmgJE3nsu7cYjJoLDIybIlTyriROeWmPL1CQpmP6lzwtHBEWVS2If0D18bY9VSNWGyj0orLGgutEo1wU1B55v47DabniH1L6kzVg6irOLLQo7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UrWuNdz3RHV1WbvIHA31juDogF4zjrqBfqV0HmORx4y04SPxfh5oaRov0sQ4kJBg-YwDdV_GyennGNRnbZy-zD3YNMfYuxoQ9hvY1ou3GPG8Yya1aGJx5VddIsQjDEH7FjbCCvwFzl5mZqVqUWAANeFVG3NOOWz9CR0NFOn1zdQnuEcTapKflSD9AnACxBwSrDBldZfaNHUZeGrZkZuO5hGb8QY1dTbsasH-y9Q7WKxbnI8yQtyhDrphNVNvs7orDFDCP7IxlOKxIlq1ONUxIgFNW_iUovPOIdoykbgaNB2ji-HhOeDApBOnLBuw_Yb-ON80oNs6vWq5ZbRsLItCug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lbiSPKJU24i-QgCEvUTEEimg1ZVqJVk0-bNQ_93a521HOm3nC_FO7AP8QgihjBC3dMJulpGS5NZgJPdkEqrDBOyWTIy6jMxSWkJGlYtgqq1WZxw9Rk4sBq3H8MvgJOvOgAawfJjnvbE7vPVLAlwnKZFfuxGK3hOPIfaRxjkEzPVIF7Ae3ZfQBoUHaI8OxwUPhIOxMdroTnhzB3feOFL9Zh4_fMZBEjCHdOAohYztpsrCoV0bAfSuuJBKr3Jhb_1VGTIHo4MiSxJuWGQD7g4f2TvgqfmeutHZtkWjXDV36Rnai_UuDb-QLaE4ogMcp9qvrWEle3KciYju3HtOV6whWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آسوشیتدپرس: آمریکا در حال تکمیل خروج نیروهایش از عراق تا ۳۰ سپتامبر است و یک مقام نظامی آمریکایی گفته صدها نیروی باقی‌مانده در شمال عراق عمدتاً به اردن و دیگر کشورهای منطقه منتقل خواهند شد. تجهیزات نظامی، از جمله سامانه‌های پدافند هوایی نیز از عراق خارج می‌شوند. روز گذشته گزارش داد یک کاروان تجهیزات سنگین آمریکایی شامل خودروهای زرهی و کامیون‌های نظامی در غرب عراق مشاهده شده که در حال انتقال به سمت اردن بوده است. جزئیات دقیق نوع تجهیزات و مقصد نهایی آن‌ها هنوز به‌صورت مستقل تأیید نشده است.
یک مقام نظامی آمریکایی گفته خروج از شمال عراق «ریسک ما را برای عملیات‌های پیشرو کاهش می‌دهد».
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23444" target="_blank">📅 10:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23443">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مجلس نمایندگان آمریکا با رأی ۲۵۲ موافق در برابر ۱۵۴ مخالف، اصلاحات سنا در طرح «قانون تحریم روسیه و ایرانِ لیندسی اُ. گراهام در سال ۲۰۲۶» را تصویب کرد. در این رأی‌گیری، ۱۹۷ جمهوری‌خواه، ۵۴ دموکرات و یک نماینده مستقل رأی موافق دادند. در مقابل، ۶ جمهوری‌خواه…</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23443" target="_blank">📅 10:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23442">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یک مقام سعودی در قبال تحولات یمن در گفت‌وگو با شبکه ۱۲ تلویزیون اسرائیل: «از سوی پاکستان یا ترکیه چیزی جز اظهارات نرسیده و هیچ همکاری‌ای صورت نگرفته است. آنها فقط می‌خواهند سلاح بفروشند.»
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23442" target="_blank">📅 09:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23441">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a920abf92.mp4?token=Srvj3wzQ3g0149E20K-OUfUYE3KCXjj9OgGYWAcHV2uyP_5gnEL5JZog_deRpVqiHDZHl4EQT_pjR0oVESpQNb-179KnA5aueEc5FdDB54Kj_x6FkfvHX13TKJvkqCRnsZrk_yJ3n22Qx04xPylGbDAlKys_2YoceJoNtHLmaJ2wHAboo_TOv5PRbjYl8sOS3FDpZ20M5cTKmt8at1D1UwahT6C-a_GNAosIwh9wuaPnRY8nV8wJb1O0Gyc7NqQA18rh3lB_pBzc2VEGtaAFDsFmQBelv5irzYsHlpQKTRxcYQNeqbCbrioeYpt_R9CQ6L6Wop6VC2X2OC0k0iLucw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a920abf92.mp4?token=Srvj3wzQ3g0149E20K-OUfUYE3KCXjj9OgGYWAcHV2uyP_5gnEL5JZog_deRpVqiHDZHl4EQT_pjR0oVESpQNb-179KnA5aueEc5FdDB54Kj_x6FkfvHX13TKJvkqCRnsZrk_yJ3n22Qx04xPylGbDAlKys_2YoceJoNtHLmaJ2wHAboo_TOv5PRbjYl8sOS3FDpZ20M5cTKmt8at1D1UwahT6C-a_GNAosIwh9wuaPnRY8nV8wJb1O0Gyc7NqQA18rh3lB_pBzc2VEGtaAFDsFmQBelv5irzYsHlpQKTRxcYQNeqbCbrioeYpt_R9CQ6L6Wop6VC2X2OC0k0iLucw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره جمهوري اسلامي:
فکر می‌کنم در نهایت پیروز خواهیم شد.
نمی‌دانم آیا از طریق یک توافق‌نامه باشد یا نه، اما ما از همین حالا در حال پیروزی هستیم. اما فکر می‌کنم در نهایت پیروز خواهیم شد.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23441" target="_blank">📅 09:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23440">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a3d694c10.mp4?token=ucf5TpGN2-qx1ikRycAjsLNKxKxnxwCPGZj3EdRRFH9peZ0MSlLX0kDH9yDXK5uJgLcDq_obBf8EqJuLzlRA-TpKwyJDUg-ceTnOoGI3-lOTsGRnSILPADFz4l1zp3Kit0ilYoRvFbs6bVZJ_fXejVSVcycnWM1LBKXVxhOJmveXj7QdHHYuPNdSZP4P2EcG4WrC4w6Wgj02tWaH-cOET1LqPUfvXAN04uSMFgrRrjUIV2WKQNhhCZyoGtGgx22hAbnBBBO082RC3Ew9cswKSC2ZQB-hkn11kcKnUXlAHY_TsjMrGUXaz4Mon0W6UToyJjB_T-rCEQqlo9x1AhucLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a3d694c10.mp4?token=ucf5TpGN2-qx1ikRycAjsLNKxKxnxwCPGZj3EdRRFH9peZ0MSlLX0kDH9yDXK5uJgLcDq_obBf8EqJuLzlRA-TpKwyJDUg-ceTnOoGI3-lOTsGRnSILPADFz4l1zp3Kit0ilYoRvFbs6bVZJ_fXejVSVcycnWM1LBKXVxhOJmveXj7QdHHYuPNdSZP4P2EcG4WrC4w6Wgj02tWaH-cOET1LqPUfvXAN04uSMFgrRrjUIV2WKQNhhCZyoGtGgx22hAbnBBBO082RC3Ew9cswKSC2ZQB-hkn11kcKnUXlAHY_TsjMrGUXaz4Mon0W6UToyJjB_T-rCEQqlo9x1AhucLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره جمهوري اسلامي:
هر جا را در جهان نگاه کنید، ایران به عنوان بدترین کشور جهان شناخته می‌شود و مدت طولانی است که این‌گونه بوده است.
ما کار را انجام خواهیم داد. آن‌ها در وضعیت بسیار ضعیفی قرار دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23440" target="_blank">📅 08:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23439">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4f45e1be2.mp4?token=gXcVUZusMkx8qzQ-lRmifY5BD4JV1d8KDhhWXibnGyGIcNOxCWy8Qr3UmeaJ_B2mjadA4V-aRyuqpp0qvyffxZpFUJ0mkjTi3UMqEUmXy-KrUgB5R2tquVJUn7k4TXJDHGSbCO_K9gMA4AjwaJU_KQuiiJzg1nODMK7dedWtUDJbanrVTJwKH-tWqDssC7Ri7QYRR5mTvI_hBplJpK8dLPRT9ptSyhc5RsJmxSVM5FQQsOy3j0JMGY-YzpILuUE2TXh-yBxuhJUuno65ij8Rp_oOo18x6d3ucvMA67MSQc9Q9U1aMuuP4xdt3CCTWWTu6OLCnBg_oTHwKTbrsKu_vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4f45e1be2.mp4?token=gXcVUZusMkx8qzQ-lRmifY5BD4JV1d8KDhhWXibnGyGIcNOxCWy8Qr3UmeaJ_B2mjadA4V-aRyuqpp0qvyffxZpFUJ0mkjTi3UMqEUmXy-KrUgB5R2tquVJUn7k4TXJDHGSbCO_K9gMA4AjwaJU_KQuiiJzg1nODMK7dedWtUDJbanrVTJwKH-tWqDssC7Ri7QYRR5mTvI_hBplJpK8dLPRT9ptSyhc5RsJmxSVM5FQQsOy3j0JMGY-YzpILuUE2TXh-yBxuhJUuno65ij8Rp_oOo18x6d3ucvMA67MSQc9Q9U1aMuuP4xdt3CCTWWTu6OLCnBg_oTHwKTbrsKu_vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره جمهوري اسلامي ایران:
فکر می‌کنم در حال فروپاشی هستند.
می‌دانید، اقتصادشان در حال حاضر در سطحی است که هرگز پیش از این ندیده‌اند. بدترین اقتصاد تاریخشان است.
تورم آن‌ها بیش از ۳۰۰ درصد است. به سربازانشان حقوق نمی‌دهند. به ارتششان حقوق نمی‌دهند. به پلیسشان حقوق نمی‌دهند.آن‌ها در آشفتگی هستند. خواهیم دید چه اتفاقی می‌افتد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23439" target="_blank">📅 08:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23438">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">رویترز:
قیمت نفت برای سومین روز متوالی کاهش یافت؛ برنت حدود
۱۰۴ دلار
و WTI حدود
۱۰۱.۲۰ دلار
معامله شد. کاهش نگرانی‌ها درباره اختلال طولانی‌مدت در صادرات عربستان، از جمله تلاش برای بازگرداندن بخشی از ظرفیت خط لوله شرق-غرب، عامل اصلی کاهش قیمت عنوان شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23438" target="_blank">📅 08:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23437">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اتاق جنگ با یاشار: اگر پرونده ایران در شورای امنیت به رأی‌گیری برسد، باید بین دو حالت فرق بگذاریم: اگر رأی‌گیری درباره یک قطعنامه معمولی و الزام‌آور باشد، روسیه یا چین می‌توانند با وتو جلوی تصویب آن را بگیرند. اما اگر رأی‌گیری از نوع رویه‌ای باشد، روسیه و…</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23437" target="_blank">📅 07:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23436">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb6a10ce6c.mp4?token=kEk_PTfS8YgDpjdvNgZb2Oh5xIHxxSiGT60pMag-0xT-uLJCj89ywaqDo_tKgrMSIVe5dayV8CfQ1vOIymNRMlRNQjkkUScgZrbR-JInH13O-wPNd33EChnVaZ06_RSz_L6XBQ9NBBtc0LllPFbkBgcg3lbVwLwlPzHDGEUl3RQwY_4XoBi13uE0XjNBN3f1bIZ4h9F8T4OycHOkSxqZPGxLH4aoaNJxN6b-NKoezzNO4b35RaPeeLBbagKF06pj1AKX165EXSBlFn_WRLFgLBLlK8F2yYdcSbWGvKWHivutrdIFFKL1Th9nec317lA1-PqEv6jwFjKPAGWULUZq9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb6a10ce6c.mp4?token=kEk_PTfS8YgDpjdvNgZb2Oh5xIHxxSiGT60pMag-0xT-uLJCj89ywaqDo_tKgrMSIVe5dayV8CfQ1vOIymNRMlRNQjkkUScgZrbR-JInH13O-wPNd33EChnVaZ06_RSz_L6XBQ9NBBtc0LllPFbkBgcg3lbVwLwlPzHDGEUl3RQwY_4XoBi13uE0XjNBN3f1bIZ4h9F8T4OycHOkSxqZPGxLH4aoaNJxN6b-NKoezzNO4b35RaPeeLBbagKF06pj1AKX165EXSBlFn_WRLFgLBLlK8F2yYdcSbWGvKWHivutrdIFFKL1Th9nec317lA1-PqEv6jwFjKPAGWULUZq9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارسالی : سلام یاشار جان زاهدان حدود ساعت 12 نیم بامداد امشب درگیری افراد مسلح شروع شد تا همین الان درگیرن صدا تیر میاد بین خیابون دانشگاه و دانشجو خیلی کشته دادن حدود 9 تا امبولانس فقط امده بود سر صحنه
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/23436" target="_blank">📅 02:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23435">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">وزیر دفاع ایتالیا: ما کشتی‌های جنگی خود را مستقر خواهیم کرد تا از عبور ایمن در تنگه باب‌المندب اطمینان حاصل کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/23435" target="_blank">📅 01:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23434">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا: گزارشی از یک حادثه امنیتی در تنگه هرمز، در ۱۶ مایلی دریایی شمال شرقی خصب در عمان دریافت شده است. بر اساس این گزارش، هیچ خسارتی به کشتی وارد نشده و هیچ‌یک از خدمه نیز زخمی نشده‌اند. @WarRoom
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/23434" target="_blank">📅 01:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23433">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گزارش حمله پهپادی رژیم به کمپ های کرد های عراق اطراف اربیل
شبکه المیادین از شنیده شدن صدای انفجار در منطقه «مصیف» واقع در حومه اربیل، مرکز اقلیم کردستان عراق خبر داد.
همزمان منابع غیر رسمی از به پرواز در آمدن هواپیماهای جنگی آمریکایی در اطراف این شهر خبر دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/23433" target="_blank">📅 01:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23432">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/23432" target="_blank">📅 01:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23431">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/23431" target="_blank">📅 01:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23430">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اتاق جنگ با یاشار: آیا حلقه اطلاعاتی آمریکا درباره شبکه‌های جمهوری اسلامی در حال گسترش است؟!   یکی از احتمالاتی که می‌توان درباره بازگشت برخی چهره‌ها و افراد ایرانی به کشور مطرح کرد، گسترش دامنه دستگیری‌ها و تحقیقات آمریکا درباره افرادی است که با جمهوری اسلامی،…</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/23430" target="_blank">📅 01:13 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23429">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gV0gNSc18Gi6-i3Yt2qEM8eXJc6tn_Muz9WjOkw21ofVdqjm2MO6yDsWBrV9P-6kMgpcIeex-MvV53RbCLU4gbSr9_Wcq_Cv53kQY83SP3s6pPH0rVQzlux5QP3q-meizIbb-BPP75KjJ9YvbeC04-fy__RsjmQUpKRNw1XeQraHPbV9TOxkzOZkDP650qY8RocukUWG__sieprNurwE2cbfFoVodO9sPA7F1zMy6AumnrdaOyFvw6l7PFLj9z8ebl2ENMBj6Eo_atiYg3W9ty9ciz1ql0veX5EmXRUTTp9KpbzbBXH02pH2LxbWjtxAWNGBytvJc04mPqIdRex27w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار: آیا حلقه اطلاعاتی آمریکا درباره شبکه‌های جمهوری اسلامی در حال گسترش است؟!   یکی از احتمالاتی که می‌توان درباره بازگشت برخی چهره‌ها و افراد ایرانی به کشور مطرح کرد، گسترش دامنه دستگیری‌ها و تحقیقات آمریکا درباره افرادی است که با جمهوری اسلامی،…</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/23429" target="_blank">📅 01:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23428">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23428" target="_blank">📅 01:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23427">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23427" target="_blank">📅 00:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23426">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">میدل ایست آی: دونالد ترامپ «وسلی هانت»، نماینده جمهوری‌خواه تگزاس، حامی سرسخت اسرائیل و از منتقدان شریعت اسلامی را به عنوان سفیر بعدی آمریکا در عربستان سعودی معرفی کرده است. هانت، افسر سابق ارتش آمریکا، پیش‌تر دو سال به عنوان افسر رابط دیپلماتیک در عربستان خدمت کرده بود. این انتخاب در شرایطی حساس برای روابط آمریکا و کشورهای خلیج فارس و همزمان با جنگ ایران و آمریکا و تشدید درگیری‌ها در یمن انجام شده است. انتصاب هانت برای نهایی شدن به تأیید سنای آمریکا نیاز دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/23426" target="_blank">📅 00:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23425">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23425" target="_blank">📅 00:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23424">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پدافند شرق تهران درگیر شد ، اگه ادامه دار بود گزارش بدید</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/23424" target="_blank">📅 00:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23423">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSina</strong></div>
<div class="tg-text">داداش فکر کنم دارن تهران و میزنن
هم صدای جنگنده اومد هم صدای انفجار شیشه‌های خونه ما لرزید مادرم از ترس رفت پایین
شرق تهرانم</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/23423" target="_blank">📅 00:37 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

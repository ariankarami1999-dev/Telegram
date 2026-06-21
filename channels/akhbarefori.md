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
<img src="https://cdn4.telesco.pe/file/R0QujRp0kFMGFtf6GFXynj4rVje2RDKrKsBeb3RNzUpdc3X2eJ98d2R991Ej8CwSnFNxcTHIkRoao110YM8KpDwMsdSbQ50buVGrNVxD5-hn44FWYbOrcA0yKc2Ggo_YU1RYjzJo8TG3j1C9FbnXG_2nKZFR-kJm6gk-JxQO0HuhCTR29-3V7RDsfdRqnZZ3xdIxL5T2ziIcQRcRjd9N6LhBknGb1B0Ux-BJ-93N28C-HpF6jN-a259ATY9yZhzh1IlF_Gg70nMRru1zCHv_C9SvwahXvUM3IFeFHS4V9nx7q3vCVsOw7Uo384ZLFktqSslbpccLKgixcSS7IrUsvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.41M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 18:51:00</div>
<hr>

<div class="tg-post" id="msg-661861">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d0bcc2190.mp4?token=ixiAhDOVJ6rNGdD7zcF4TDrYc-1-_Yhb38fQJx7omO6Odwovg7jqE-CZinovXRUWp7b5e4MpwGRaD_SUUzDpJMkpbOqw1Ul2ccwBhuqxoFoA_tbQGHkq2dbq_5xLioFnErC_62HXrtpQr1j72WUNm9SI6JDBNXrYL0gT_Bbxj5nqAshCl5BJoFNnPwVihtk4d5qKuXYHjYAgEC2imAOnS9XfP5snueOxR3rHftu9Nd2aWjIcYQx4V9cHDvA0GlCdjJSilAz10Lzj6wZib4j-JGpcyaIgbj09zxZnMO7uBizvV076-xf9-dYOQPlyPYpI3ss51_lJKH1uV226QM6b3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d0bcc2190.mp4?token=ixiAhDOVJ6rNGdD7zcF4TDrYc-1-_Yhb38fQJx7omO6Odwovg7jqE-CZinovXRUWp7b5e4MpwGRaD_SUUzDpJMkpbOqw1Ul2ccwBhuqxoFoA_tbQGHkq2dbq_5xLioFnErC_62HXrtpQr1j72WUNm9SI6JDBNXrYL0gT_Bbxj5nqAshCl5BJoFNnPwVihtk4d5qKuXYHjYAgEC2imAOnS9XfP5snueOxR3rHftu9Nd2aWjIcYQx4V9cHDvA0GlCdjJSilAz10Lzj6wZib4j-JGpcyaIgbj09zxZnMO7uBizvV076-xf9-dYOQPlyPYpI3ss51_lJKH1uV226QM6b3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لیندسی گراهام: به مسئولین ایران می گویم؛ اگر گوش می‌دهید: وقتی از حزب‌ الله برای حمله به اسرائیل استفاده می‌کنید، سیاست جدید این خواهد بود که ما به ایران حمله خواهیم کرد
#Trash
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/akhbarefori/661861" target="_blank">📅 18:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661859">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cAdWCPyNkJmLb7o6IwfzrcNElhtvC_PZC25IhR3ZaUWdtk84YGtU-hjX8-14q2nOofjKYgcGkMM_blmyALUb7wRDFNHL7HDUwf0UcoLlSrlKzn467emiRJ4oYsNLNbzYtpHc7s7lLbZ1L4H91wVFrCdHdhr-XapltEVe2vcBpPG7cs4GdzAOrk2TWDSRCeImPJFLyIAwnD4XLpnkhA4LgnwpzP_kIf83pOIbX7lLK-TL9i3LO4wOSNjuLOMxbEFkmkN9GiLTMiryx7CVQ2wkQO-KdGztud_ble6l6voEy-fJ_N5x_6fkgYdoW1-GF9WdIT89JrnSAEGAPjq4rJdWQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N6Ln8S62kMCthVIgGKCdv_TU5gVH22yOamQSE7lSIqCvxig0ExBsPirGnYQ4EJOrujZ_aWsXZKDwQrv4tvdNP-QnLKfT5DtfrsWWjysKSF1X1xjbC32yv3w-NL5a5QsggwsyOQ-J6-vcjWCjp6PwtknbM2eiRgJaAI8tc3C5mlpHyNHA3Bu2GFPsvPsxRO9IRqGQEysy7VcSGlptYvvur3r2ZQ0HOUtHk8hYX8B7TgPNEiIHd_fuhYAiwNGXOwqwo2NwHCuTFzFIJtA9fJbD6sqm_wxTPPg3lvYRexl-dWl8LeaxYCyzIwdqa_rWAW3n72kfs__jZFVGg7cfTsOpTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نشان‌سینه محمدباقر قالیباف، رئیس هیئت مذاکره‌کننده «میناب ۱۶۸» در مذاکرات امروز
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/akhbarefori/661859" target="_blank">📅 18:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661858">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
یک منبع آگاه در تیم مذاکره‌کننده ایران در سوئیس: هم‌اکنون دور اول مذاکره ۴ جانبه به اتمام رسید/ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/akhbarefori/661858" target="_blank">📅 18:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661857">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
سی‌ان‌ان: تمرکز اولیه مذاکرات ایران و آمریکا بر لبنان
سی‌ان‌ان به نقل از منابع دیپلماتیک:
🔹
مذاکرات ایران و آمریکا در سوئیس با تمرکز بر جنگ لبنان، تنگه هرمز و ذخایر هسته‌ای ایران آغاز شده است.
🔹
به گفته این منبع، گفت‌وگوها با فضایی «صریح و بسیار صادقانه» شروع شده و طرف‌ها همچنین درباره ساختار یک دوره مذاکراتی ۶۰ روزه بر اساس یادداشت تفاهم ۱۴ ماده‌ای هفته گذشته بحث می‌کنند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/akhbarefori/661857" target="_blank">📅 18:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661856">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
یک منبع آگاه در تیم مذاکره‌کننده ایران در سوئیس: هم‌اکنون دور اول مذاکره ۴ جانبه به اتمام رسید/ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/661856" target="_blank">📅 18:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661855">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNb2x_2Eraoj7YBZVHjVRbwLrdyRGEXD80rPbfB6nk3PY5ywrN9w-l6xs59Op0e73V_mqcaHusDBRDLMWZ8rBNHgLV74ERDUgFLmWXiDJhnz7MgoAo46o3ZKHZ4MBvugcAZWxb8AAQ_qdZUxDDvNYV00biYDF_1PQfINyrLWl0YkdQIGn5jjMuxmmYOv-hmiztYa_mi-ILSlSvFuZauVhyBTMBTCxIdlJkhpCaz2BT4VE5B8QJk98SXBFSc3LeJAX-VgXddJD-_aUumWMWhZ8OBCWoux2cvD0p8vLpzbcM23MqQiD944FG3q83zSKi9q_Hi8pxLDVX9D0IPcwnY1mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرندی: ایران دیشب پس از آتش‌بس در لبنان تنگه هرمز را به تدریج بازگشایی کرد
تحلیلگر مسائل بین‌الملل:
🔹
ظرف چند ساعت پس از بستن تنگه هرمز توسط ایران، رژیم صهیونیستی با آتش‌بس موافقت کرد و کشتار کودکان لبنانی را متوقف کرد.
🔹
تا صبح، ایران به تدریج تنگه را بازگشایی کرد. ترامپ اکنون تهدیدهای توخالی می‌کند تا اعتبار این بازگشایی را از آن خود کند - اما زمان‌بندی چیز دیگری می‌گوید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/661855" target="_blank">📅 18:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661854">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
ادعای وزیر انرژی آمریکا در گفت‌وگو با ای‌بی‌سی: ۶۷ کشتی دیروز از تنگه هرمز عبور کردند و حجم نفت در حال عبور، نزدیک به میزان پیش از جنگ است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/661854" target="_blank">📅 18:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661853">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f6f22c4f.mp4?token=MFNwzfI5JdaSgNq-Sw8vGN-m5SsUR8punUXrAU94pQP4m3TVVSuLFwGtbL8oee0lW7gpHpQktH-xEhJirAFG26_ny41OMOJG3z66q_ftRODXx-0q7Evy2T6bv_N2kY9BLcm6iWuoQvCvXTGCsBEz0G45p7ShulmsskKerUSD9OZAruOZpvcP9EgMTmzFi4nXcHuXQdnZNvvP3hCIlyl_xUy6Gr2pXO8IFk9tOuFYF8OBXDvtk33aeZQvPL2V9ut857QAQJK3hFj8ZKrrfqjsth6A_62eRaJNLxMnfDMphh11FmU5IEnDtSg6Qqe2eVo5yUDedGfT3WXCj8HtBeBn5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f6f22c4f.mp4?token=MFNwzfI5JdaSgNq-Sw8vGN-m5SsUR8punUXrAU94pQP4m3TVVSuLFwGtbL8oee0lW7gpHpQktH-xEhJirAFG26_ny41OMOJG3z66q_ftRODXx-0q7Evy2T6bv_N2kY9BLcm6iWuoQvCvXTGCsBEz0G45p7ShulmsskKerUSD9OZAruOZpvcP9EgMTmzFi4nXcHuXQdnZNvvP3hCIlyl_xUy6Gr2pXO8IFk9tOuFYF8OBXDvtk33aeZQvPL2V9ut857QAQJK3hFj8ZKrrfqjsth6A_62eRaJNLxMnfDMphh11FmU5IEnDtSg6Qqe2eVo5yUDedGfT3WXCj8HtBeBn5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نجاح: اسرائیل ممکن است توافق را برهم بزند؛ ایران باید تضمین‌های عملی بگیرد
نجاح محمدعلی کارشناس مسائل خاورمیانه در
#گفتگو
با خبرفوری:
🔹
«تنگه هرمز را باید خوب از آن استفاده کرد و نباید یک لحظه از آن اغماض کنیم؛ این امروز یک سلاح جدید است.»
🔹
هرچند ایران به نتیجه خوبی رسیده، اما چون اسرائیل احساس شکست می‌کند، ممکن است برای برهم زدن توافق تلاش کند، بنابراین ایران باید از آمریکا تعهدات قوی‌تری بگیرد و این تعهدات نباید در حد وعده باشد، بلکه باید کاملاً عملی و قابل اجرا باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/661853" target="_blank">📅 18:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661852">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
ارجاع پروندۀ یکی از معاونان رئیس‌جمهور به دادسرای دیوان محاسبات
دیوان محاسبات کشور:
🔹
درپی طرح موضوع واردات بنزین و اعلام آمارهای غیرمستند، پرونده یکی از معاونان رئیس‌جمهور به دادسرای دیوان محاسبات ارجاع شده است.
🔹
این نهاد همچنین با اشاره به مغایرت رقم اعلامی «۶ میلیارد دلار» واردات بنزین در سال ۱۴۰۴ با داده‌های رسمی، خواستار ارائه مستندات مربوط به این ادعا شد./ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661852" target="_blank">📅 17:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661851">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
زنگ خطر HIV؛ سن ابتلا به ۲۵ تا ۳۵ سال رسید
حسین پور، مسئول پیشگیری از بیماری‌های ایدز و هپاتیت دانشگاه علوم پزشکی مشهد:
🔹
آمار مبتلایان به ایدز به ۶۵۰ نفر رسیده و سالانه ۵۰ تا ۶۰ بیمار جدید شناسایی می‌شوند. ۷۰ درصد موارد جدید از طریق روابط جنسی پرخطر منتقل شده‌اند و سهم زنان از مبتلایان به بیش از ۳۰ درصد افزایش یافته است.
🔹
متخصصان تأکید می‌کنند تشخیص به‌موقع و مصرف دارو به مدت ۳ تا ۶ ماه می‌تواند ویروس را کنترل کرده و احتمال انتقال آن را از بین ببرد./ اخبارمشهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661851" target="_blank">📅 17:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661849">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
حادثه دریایی نزدیک سواحل یمن
سازمان تجارت دریایی بریتانیا (UKMTO):
🔹
حادثه‌ای در فاصله ۵۰ مایل دریایی جنوب‌شرق شهر الشحر در یمن رخ داده است.
🔹
طبق گزارش کاپیتان یک نفتکش حامل فرآورده‌ها، یک قایق کوچک با پنج فرد مسلح به کشتی نزدیک شده و تلاش کرده‌اند سوار آن شوند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661849" target="_blank">📅 17:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661848">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
محسن زنگنه، نماینده مجلس: پزشکیان فرآیند ارزیابی عملکرد وزرا را آغاز کرده است/ اگر لازم است دولت وزیر نفت را تغییر دهد
محسن زنگنه, عضو کمیسیون برنامه و بودجه مجلس:
🔹
پزشکیان فرآیندی را برای ارزیابی عملکرد وزرا و مدیران دولت آغاز کرده‌اند. اکنون نزدیک به دو سال از عمر دولت گذشته و طبیعی است که ارزیابی عملکرد اعضای کابینه در دستور کار قرار گیرد.
🔹
همان نکات و مسائلی که پیش از جنگ هم مجلس درباره آن‌ها به دولت محترم تذکر داده می‌شد، در دوران جنگ نیز خود را نشان داد.
🔹
بخش‌هایی که در طول جنگ با ضعف‌هایی مواجه بودند و علی‌رغم تلاش دولتمردان بعضاً مشکلاتی ایجاد کردند، عمدتاً همان حوزه‌هایی بودند که پیش از آن نیز درباره عملکرد آن‌ها نقدها و تذکراتی مطرح شده بود و نیاز به اصلاحات و تغییرات در آن‌ها احساس می‌شد مانند وزارت نفت/سندنیوز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661848" target="_blank">📅 17:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661847">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
سقوط هواپیمای اسرائیلی در نزدیکی واشنگتن
🔹
گزارش‌های اولیه از سقوط یک هواپیما متعلق به رژیم صهیونیستی در شرق واشنگتن دی‌سی خبر می‌دهد؛ حادثه‌ای که به کشته شدن خلبان و دو سرنشین آن انجامید.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661847" target="_blank">📅 17:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661846">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8bZ84Pcz2bWxVmv9XVzPZy2hr7zNbAy_lPutZTSLp3rFqakLj2Dxl3F4EQq9Qy4ro_1muQuWwc6pziYFiCH8hrCVOKxAYtGwjbeDltq6lAzHjx9rd_OigXWc9UYgvOESSJr5cfb7LJ6Fy2DnlXbt2B-0c0oCO5exlwbIUDv7dzacCEaAW2ht4sD3aNB3LeUCXSXU6OHp3ZfGHJxByhfTvlCBKerGqCtTsDoK1dgoelv3rnPHN11DWjJTiLle_OzrsoZaH6kw8-vUBT542SN_Oia1rG-ol9COM30bGFf4QVjIaxVNl4dOC5O94MmWNqdISuimH_8SpOTAtAnyPNpsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش قاطع مرندی به ادعای ترامپ در مورد تنگه هرمز/ هزینه دریافت خواهد شد
🔹
تحلیلگر مسائل بین‌الملل: هزینه‌ای دریافت خواهد شد. این قطعی است.
🔹
ترامپ شب گذشته مدعی شده بود «در طول دوره آتش‌بس، به مدت ۶۰ روز هیچ عوارضی در تنگه هرمز وجود نخواهد داشت و پس از پایان دوره ۶۰ روزه نیز هیچ عوارضی وجود نخواهد داشت»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661846" target="_blank">📅 17:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661845">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3XNsn5jGBn3SfHNPUCDRYY_kPwI8k3AXr9QPFOa3vMTOCIR2rc1P0nC8FHHhJ2q4SXENeHI3Hka5sARw5WW1ZCl6YnFcfabJvqN0-qBo0Q9nQwEEJKpRmuC8Jdum9aNoc-QVyxE8Mld62E8BTgnd34tX9CgW63S-OlQnttGzSZm6J6NH7KD8xgIwGaG-wucze-6KyE7VdbVRokqEXXYM1QwTceRAI92Y1R0BC3md_DheDvzJfowA_326fpVp5GxM0aPkNkSSSHpe0Yo1fVv-CIqjCyfAFtOkVlW1keQxm-142bDS-OyytpPWTduhSyN9aC8dblTHvc6P-FBR-0Xvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکثریت آلمانی‌ها از مشارکت در مأموریت اروپایی برای تأمین امنیت تنگه هرمز حمایت می‌کنند
🔹
بر اساس یک نظرسنجی، ۵۷ درصد از شهروندان آلمان از مشارکت این کشور در یک مأموریت اروپایی برای حفاظت از کشتیرانی در تنگه هرمز حمایت می‌کنند.
🔹
با این حال، توان عملیاتی برلین محدود است و آلمان عمدتاً می‌تواند نقش پشتیبانی، شناسایی و مین‌روبی ایفا کند. مقام‌های نیروی دریایی آلمان نیز اذعان کرده‌اند که این کشور با «کوچک‌ترین ناوگان تاریخ خود» روبه‌رو است، در حالی که با مأموریت‌های فزاینده‌ای مواجه شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661845" target="_blank">📅 17:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661844">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
فرانس ۲۴: ملوانان در تنگه هرمز گرفتار شدند
🔹
با وجود آغاز مذاکرات ایران و آمریکا در سوئیس، تنگه هرمز توسط ایران بسته شده و هزاران ملوان در این منطقه گرفتار شده‌اند؛ موضوعی که می‌تواند پیامدهای اقتصادی گسترده‌ای داشته باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661844" target="_blank">📅 17:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661842">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه قطر: تیم‌های فنی ویژه مذاکره درباره مفاد توافق نهایی تشکیل شده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/661842" target="_blank">📅 17:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661841">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e60fd748c1.mp4?token=OX7NzZ1TPzyfwcvOvE-D18TjCKAsArbinBnmSkNvAi1ji7ZSEfKNPqXpugOIbeWAl9vRUPHX5PYBzWrs06LSWihoKWkAlsJ5RQUzyzruK1LzJCxnPrrjT7ca_fVfOyDQD9WD6vX_0IjFM7ZUlw1vX1eeapJU8ojJ6NNXwfD8cIfLa1t-tTeFnlfebvQsHufng1NuCDGtxtU4sYrxWuEESmMh7aE7blY8206wPHjIUQX-z0j7GlEq_uk67eUq-1s4X8-gQ9tmu4OBgjq2obUIsqsZkOAkDYOEYixA9yXfnVqhJx3vqVEt6CfGFw32Hcb0BPgLOLZxQl-GH5KNvmahxoI31KEeBj5XZCWIawgO8QI_s-CV2DNkADAZsaUYBQMOYBFgSWD7RiWIAENUff3yNFe0J3GvbGrJ9uGHBAI-qNxnO8-JvZLZl2cGuDCCDf5FVTojsqTvME6Sv035-4mLOQP8mB2OunX4edVysbxarzgnxnc9rRf10Ee2Hb_YJn-QtRb2pVtLjzHkU23ZNL88LPhGvMQVh0IIrYinP7DS3sJWXIQKONFDadlvM-3AqRixJu8zeoTl1Go3CkwUW6RI6I_wkEBQydlN_D40ZhcjQSGc048NEdkibicZZDYMWoopEzu5dK0EsdtgjVYvIYgjMn5hkMTUUT014sF6JvmTKKE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e60fd748c1.mp4?token=OX7NzZ1TPzyfwcvOvE-D18TjCKAsArbinBnmSkNvAi1ji7ZSEfKNPqXpugOIbeWAl9vRUPHX5PYBzWrs06LSWihoKWkAlsJ5RQUzyzruK1LzJCxnPrrjT7ca_fVfOyDQD9WD6vX_0IjFM7ZUlw1vX1eeapJU8ojJ6NNXwfD8cIfLa1t-tTeFnlfebvQsHufng1NuCDGtxtU4sYrxWuEESmMh7aE7blY8206wPHjIUQX-z0j7GlEq_uk67eUq-1s4X8-gQ9tmu4OBgjq2obUIsqsZkOAkDYOEYixA9yXfnVqhJx3vqVEt6CfGFw32Hcb0BPgLOLZxQl-GH5KNvmahxoI31KEeBj5XZCWIawgO8QI_s-CV2DNkADAZsaUYBQMOYBFgSWD7RiWIAENUff3yNFe0J3GvbGrJ9uGHBAI-qNxnO8-JvZLZl2cGuDCCDf5FVTojsqTvME6Sv035-4mLOQP8mB2OunX4edVysbxarzgnxnc9rRf10Ee2Hb_YJn-QtRb2pVtLjzHkU23ZNL88LPhGvMQVh0IIrYinP7DS3sJWXIQKONFDadlvM-3AqRixJu8zeoTl1Go3CkwUW6RI6I_wkEBQydlN_D40ZhcjQSGc048NEdkibicZZDYMWoopEzu5dK0EsdtgjVYvIYgjMn5hkMTUUT014sF6JvmTKKE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رژیم صهیونیستی به این توافق تن نمی‌دهد؛ ایران باید هوشیار باشد
نجاح محمدعلی کارشناس مسائل خاورمیانه در
#گفتگو
با خبرفوری:
🔹
اگر کسی فکر می‌کند رژیم صهیونیستی به فشارهای تحمیل‌شده تن می‌دهد، اشتباه می‌کند.»
🔹
آتش‌بس احتمالی می‌تواند تاکتیکی و موقت باشد و جنگ هنوز پایان نیافته است.
🔹
فاصله‌گیری ظاهری آمریکا از رژیم صهیونیستی ممکن است صرفاً یک بازی سیاسی باشد و ایران باید هوشیار بماند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/661841" target="_blank">📅 17:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661840">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
ترامپ به فاکس نیوز: اگر با ایران به توافق نرسیم، از کشتی‌های عبوری در تنگه هرمز عوارض می‌گیریم #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/661840" target="_blank">📅 17:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661839">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClnfVdqEQ_kqD1Dvam5A6HrQF5VuwC_Yl-FoiJXqO-eEVzg5suVkftFy18rBiaT_jNzhFuMkqB5M5_4KhRDgiKi8SBl1TcFGlOQjRQK9re_ioe33_Xgh10EPiAPrZTGcoS9PGz54sgyTZDrO8S5bHQ4fpJZZ26CvQRdB7RHyzqdmq1udMJC3uqx-XRl8DRlelQ4EMzT99AlhEdoCVTMThR2TWr_xJK2IQHU4-ir6PzLfR-3toc1TVGEHqqOJnBMVfXKcCILlC49-kltUSkw7ygi4BNE89LvFrkKoWFxF3eOm4AQRprw7scDxc8akJKAIvzBtRK8pNmX-F0aSHQsaEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ ایران را تهدید به بمباران کرد
🔹
ایران باید فوراً از ایجاد مشکل توسط نمایندگان پر دستمزد خود در لبنان جلوگیری کند.
🔹
اگر این کار را نکنند، ما دوباره به ایران ضربه‌ای سخت خواهیم زد، درست مانند هفته گذشته، فقط سخت‌تر!!!
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/661839" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661838">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
ترامپ درباره ایران: دیروز ۱۹ میلیون بشکه نفت خام به دلیل این تفاهم‌نامه با ایرانی‌ها از خلیج فارس خارج شد #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/661838" target="_blank">📅 17:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661837">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
توهین ترامپ به پزشکیان: مواظب حرف زدنت باش!
🔹
رئیس‌جمهور ایران، پزشکیان: ما از حق خود برای غنی‌سازی کوتاه نخواهیم آمد.
🔹
ترامپ، رئیس جمهور کشور بازنده جنگ: بهتر است مواظب حرف‌هایش باشد. بهتر است خود را اصلاح کند، وگرنه ما بقیه کشور را تصاحب خواهیم کرد! #Devil…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/661837" target="_blank">📅 17:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661836">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/803b709f3e.mp4?token=FeOff773HPljMbcQQ3rgke09x7ihMS1ZxFbii10i6IMiq3K7RHTviMsIJk8LG0DXkyIH0GV2bMyGtT2dmTBOnWHAHF1jO4MmLX_abwcf1ZuPz0gTwWgJ2ka0pFnGrEgtmxJ8BYLf2jzBmHaZ9h6xRK--nUm2qkOe3mKQLq1RrP1mm9hRv1716d2xGNbqxW1pSG4ER2oEwUU8_3EDxyfkpAjThez6rjK6T_Yu8eu-sf3sU89eVwdMx0ji7o_5u5VE6b3_Gk_jb6tkrWMR7hir_GUZ-9TB06lUaLXsVhUCJP0ySJNdKFgyoaAuEPeNvfoOQuXK5b2lNuIpEpRq0SQoQ766jc8aIRmKzjKANHhvlPA3R2edRq5u46rLYRXnBTdZL6Tc28iqGDaIKuwXaXHU1gMiIZS6nsIz8UtR2tLbB8LCvlOaPqZAoVPDCvbu-aUOdWwrPsJB6rvgy6wo-OoXsroYL3AMrlWwl_ASr-ZQQm4Onus-sjrVO-qZnoznRlPZHu1mkIaUYPiTiiEEcsJ1t8sI1lknJGoZBM223-GPsPE2ctXAz-rp3fEPts4k2FeT8yofMbIoOFsdH1hN9nxU9ChpKXwml2NnmF5I7sEywNvNDiYGqT69WaXAiygoE4OYvBswi6_-1UmMUqqewVoAsF6RwaJz5H2guYLX3X5i41U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/803b709f3e.mp4?token=FeOff773HPljMbcQQ3rgke09x7ihMS1ZxFbii10i6IMiq3K7RHTviMsIJk8LG0DXkyIH0GV2bMyGtT2dmTBOnWHAHF1jO4MmLX_abwcf1ZuPz0gTwWgJ2ka0pFnGrEgtmxJ8BYLf2jzBmHaZ9h6xRK--nUm2qkOe3mKQLq1RrP1mm9hRv1716d2xGNbqxW1pSG4ER2oEwUU8_3EDxyfkpAjThez6rjK6T_Yu8eu-sf3sU89eVwdMx0ji7o_5u5VE6b3_Gk_jb6tkrWMR7hir_GUZ-9TB06lUaLXsVhUCJP0ySJNdKFgyoaAuEPeNvfoOQuXK5b2lNuIpEpRq0SQoQ766jc8aIRmKzjKANHhvlPA3R2edRq5u46rLYRXnBTdZL6Tc28iqGDaIKuwXaXHU1gMiIZS6nsIz8UtR2tLbB8LCvlOaPqZAoVPDCvbu-aUOdWwrPsJB6rvgy6wo-OoXsroYL3AMrlWwl_ASr-ZQQm4Onus-sjrVO-qZnoznRlPZHu1mkIaUYPiTiiEEcsJ1t8sI1lknJGoZBM223-GPsPE2ctXAz-rp3fEPts4k2FeT8yofMbIoOFsdH1hN9nxU9ChpKXwml2NnmF5I7sEywNvNDiYGqT69WaXAiygoE4OYvBswi6_-1UmMUqqewVoAsF6RwaJz5H2guYLX3X5i41U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توهین
ترامپ به پزشکیان: مواظب حرف زدنت باش!
🔹
رئیس‌جمهور ایران، پزشکیان: ما از حق خود برای غنی‌سازی کوتاه نخواهیم آمد.
🔹
ترامپ، رئیس جمهور کشور بازنده جنگ: بهتر است مواظب حرف‌هایش باشد. بهتر است خود را اصلاح کند، وگرنه ما بقیه کشور را تصاحب خواهیم کرد!
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/661836" target="_blank">📅 16:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661835">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/635a9253a5.mp4?token=HYPPlsUAlIO0Dmli6cLkqTuKUOWoSLoK6jPKHsKf0fjtVBbyilDg-XoLiYBax2tjpyff6wFS7krsm6H06erDKfQDtp47p744a2bf6S0YCG2YBEsXwjNE3_AaJUNEDu46uT1X17rb-YxBtzlQEkCQQKAWyusHpmsDCIFGq8pBI9zgRg4UVe8lBJfsOrgFU05BVDpmMBIRtzpqpKF-Y3CLTMYt3CMR50VmgwUr2Xk-SrzjSWwg4bO3Os5r5kdNRzFCa26i70asob5Qdi_nEgX9WLofs8h86tFFjvPl7s19xLxD9EoStOnX5Uc85CLkQE-VOLPE2mUUwrB9WA57MDZMMTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/635a9253a5.mp4?token=HYPPlsUAlIO0Dmli6cLkqTuKUOWoSLoK6jPKHsKf0fjtVBbyilDg-XoLiYBax2tjpyff6wFS7krsm6H06erDKfQDtp47p744a2bf6S0YCG2YBEsXwjNE3_AaJUNEDu46uT1X17rb-YxBtzlQEkCQQKAWyusHpmsDCIFGq8pBI9zgRg4UVe8lBJfsOrgFU05BVDpmMBIRtzpqpKF-Y3CLTMYt3CMR50VmgwUr2Xk-SrzjSWwg4bO3Os5r5kdNRzFCa26i70asob5Qdi_nEgX9WLofs8h86tFFjvPl7s19xLxD9EoStOnX5Uc85CLkQE-VOLPE2mUUwrB9WA57MDZMMTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ مسئولین مذاکراتی ایران را تهدید کرد
🔹
ترامپ گفت که با مقامات ایرانی صحبت کرده و به آنها گفته است: «اگر تنگه هرمز را ببندید، دیگر کشوری نخواهید داشت. حتی به کشور لعنتی‌تان هم برنمی‌گردید.»
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/661835" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661834">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
چند کلمه با هم‌وطنان لس‌آنجلسی!
🔹
محمدرضا احمدی گزارشگر تلویزیون در بازی ایران و نیوزلند و بعد از گل دوم ایران، شاید ناخواسته یکی از عمیق‌ترین تصاویر این جام جهانی را در چند کلمه به تصویر کشید "ایرانی‌ها رو با هم دیگه می‌بینیم، با هر شکلی، با هر شرایطی، با هر پرچم اورجینال و فیکی؛ نیم‌خیز بودن تو ورزشگاه و دلشون با تیم ملی بود."
🔹
بله؛ می‌شود بر سر هزار مسئله اختلاف داشت، می‌شود سال‌ها از هم دور افتاد، می‌شود جهان را از پنجره‌های متفاوت دید، اما بعضی نام‌ها آن‌قدر بزرگ‌اند که اختلاف‌ها در برابرشان کوچک می‌شوند. ایران یکی از آن نام‌هاست.
🔹
گاهی یک مسابقه فوتبال، آینه‌ای می‌شود برای تماشای حقیقتی عمیق‌تر. حقیقتِ مردمانی که شاید در زندگی روزمره کنار هم نایستند، اما وقتی نام ایران بر سینه بازیکنان نقش می‌بندد، چیزی در اعماق جانشان بیدار می‌شود؛ حسی که نه مرز می‌شناسد، نه فاصله و نه اختلاف.
چرا؟ چون تاریخ همیشه افتخارها را حفظ می‌کند، نه اختلاف‌ها را.
🔹
ایران فقط یک کشور نیست؛ روایتی است که هزاران سال نوشته شده است. از تیر آرش که بر افق نشست تا واژه‌های فردوسی که این سرزمین را از فراموشی نجات داد. از اشک مادران تا لبخند کودکان، از شکست‌ها تا پیروزی‌ها، همه در یک نام خلاصه شده‌اند؛ ایران.
🔹
امروز وقتی از گذشته سخن می‌گوییم، کسی جدال‌های کنار میدان را به خاطر نمی‌آورد، همانطور که هیاهوی منافقین در جام‌جهانی ۹۸ فرانسه ماندگار نشد. آنچه مانده، تصویر غرور یک ملت است که برای چند لحظه، یک‌دل و یک‌صدا شد.
🔹
در روزهایی که تیم ملی به میدان می‌رود، هر گل ایران فقط یک گل نیست؛ لبخند میلیون‌ها ایرانی است. این لبخند را دریغ نکنیم.
🔹
جام‌ها و روزها می‌گذرند اما آنچه می‌ماند، خاطره ایستادن زیر یک نام است. سال‌ها بعد، فرزندان این سرزمین از ما نخواهند پرسید در آن روزها چه اختلافی داشتیم؛ خواهند پرسید وقتی نام ایران در جهان طنین انداخت، دل ما برای کدام سو می‌تپید.
🔹
و چه خوش گفته‌اند که وطن، فقط خاک نیست؛ وطن بخشی از روح آدمی است، روحی که نامش ایران است.
@TV_Fori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661834" target="_blank">📅 16:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661832">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
ادعای
ترامپ درباره توافق با ایران: من یک گزینه ۶۰ روزه دارم. بعد از آن می‌توانم هر کاری که بخواهم انجام دهم
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661832" target="_blank">📅 16:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661831">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
جزئیات مذاکرات ایران و آمریکا از زبان وزیر خارجه پاکستان
🔹
وزیر امور خارجه پاکستان، با ابراز خوش‌بینی نسبت به نتایج مذاکرات ایران و آمریکا گفت کمیته‌های فنی در حال بررسی پرونده هسته‌ای، پول‌های بلوکه‌ شده و مسئله لبنان هستند.
🔹
سه تیم فنی در این مذاکرات حضور دارند و اسلام‌آباد پس از ۴۷ سال موفق به انجام یک میانجی‌گری تاریخی میان تهران و واشنگتن شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/661831" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661830">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
مذاکرات هیات‌های دیپلماتیک و سیاسی ایران و آمریکا با حضور میانجی‌گران پاکستانی و قطری در محل هتل «بورگن‌اشتوک» آغاز شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/661830" target="_blank">📅 16:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661829">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3522dcaf.mp4?token=gmOuhP4zcTu6aqZe_cWXqi3UR_V9qsmCwjzGdbnXOnrUqeX6MRXDogjKlG8P3cdHtk2mvNPQR_g2uPVkfMiymhXqU5O-QqdAIwg7xnccLpBeKH1nsAVvWm0NUUNZcIBccrfx5FSVVzP6Ng09QLTGmpPFLQA0_cIWVXG4B7beqJXCMbhoWZkZhaSB7i5l8G0uwkPwBz16GGM0uGCgHjW-a0232iGGEUdArjxRWoc0v76Tg62GO1KKlOBG4MSHEOl20bZG4kLjJPsqNoVh6cCiObs2kJOjcgF9TvuD5uIO5bIW6r-Xq_Y_SVhZg6smSCxyJxUpCGTrtARyCx3Oo9WnIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3522dcaf.mp4?token=gmOuhP4zcTu6aqZe_cWXqi3UR_V9qsmCwjzGdbnXOnrUqeX6MRXDogjKlG8P3cdHtk2mvNPQR_g2uPVkfMiymhXqU5O-QqdAIwg7xnccLpBeKH1nsAVvWm0NUUNZcIBccrfx5FSVVzP6Ng09QLTGmpPFLQA0_cIWVXG4B7beqJXCMbhoWZkZhaSB7i5l8G0uwkPwBz16GGM0uGCgHjW-a0232iGGEUdArjxRWoc0v76Tg62GO1KKlOBG4MSHEOl20bZG4kLjJPsqNoVh6cCiObs2kJOjcgF9TvuD5uIO5bIW6r-Xq_Y_SVhZg6smSCxyJxUpCGTrtARyCx3Oo9WnIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیم مذاکره‌کننده آمریکایی وارد محل برگزاری مذاکرات شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/661829" target="_blank">📅 16:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661828">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
مخالفت هیات ایرانی با عکس مشترک در ژنو
یک منبع نزدیک به تیم مذاکره‌کننده:
🔹
هیات ایرانی با برگزاری مراسم دست دادن و عکس مشترک با هیات آمریکایی در آغاز مذاکرات ژنو مخالفت کرد.
🔹
در پی این تصمیم، پخش مستقیم و مراسم عکس لغو شد و نشست بدون حضور هیات ایرانی در بخش تشریفات برگزار شد./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/661828" target="_blank">📅 16:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661827">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
ترامپ به فاکس نیوز: اگر ایرانی‌ها تنگه هرمز را ببندند، کشورشان نابود خواهد شد #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/661827" target="_blank">📅 16:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661826">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
ترامپ به فاکس نیوز: اگر ایرانی‌ها تنگه هرمز را ببندند، کشورشان نابود خواهد شد
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/661826" target="_blank">📅 16:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661825">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7a642d2a1.mp4?token=NUjEukbIq_nPhAPIomlXGCYA7gDzjFoJT3rBBeXSJI_Os02FCgcONl0gXHvgo105-NtBgedwAoBMuMm1HFzgdy0GSQjCVH-GBYtv32VsUspAEapIMCHvbolOEpXIJqfFs019leUOuVxzcNX0gjmugZVK_0kgBvbabA_CN68Ofa9DL6vwulFVmRUxeXc97iXxzlyK9Y2V6nDvXU3AQH75wJWxHFn-3DRfoJjw4iN_YEZWhgFkWo2VK-w0-QkSd9fu95gNFnzZh8EXtQBpCZA1HwjOGiq55fd-XUDpTutl-y6z0i1MOO30lAlA4J4aIbnDuAfVU61ZjLNSJgafxn39AELUzQTV5wpw4QVpzwu0rPuspHAZcOcXRhOqbHyVBUNxOwhGu4MxNgEV6V3FO7EfpCHWFdfhihd-_XIsj5k0ADHhZZNcPo2HuPeTHOS3l2reDnXyLyYBF1ocBJxcL-gh3Xqgn8YK8mfXlZLrQaDyIx6HyPhij9FaC3gh-1LcUAPrN30uV23AI3iJrvgIBB0g8mVCcQggn1hsLcAMrQcnGdxgP7uGafD0lM31PZefvhjFrD0P7VbqLnLhNsE5Aie7qsMC2sjYSMQMlU0jxazc8AMXk6L-68eSOqUfqzAi87IswYj8Ng4mYw1TiYR1KTPzhWTY77et5auG8c03CbvDW78" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7a642d2a1.mp4?token=NUjEukbIq_nPhAPIomlXGCYA7gDzjFoJT3rBBeXSJI_Os02FCgcONl0gXHvgo105-NtBgedwAoBMuMm1HFzgdy0GSQjCVH-GBYtv32VsUspAEapIMCHvbolOEpXIJqfFs019leUOuVxzcNX0gjmugZVK_0kgBvbabA_CN68Ofa9DL6vwulFVmRUxeXc97iXxzlyK9Y2V6nDvXU3AQH75wJWxHFn-3DRfoJjw4iN_YEZWhgFkWo2VK-w0-QkSd9fu95gNFnzZh8EXtQBpCZA1HwjOGiq55fd-XUDpTutl-y6z0i1MOO30lAlA4J4aIbnDuAfVU61ZjLNSJgafxn39AELUzQTV5wpw4QVpzwu0rPuspHAZcOcXRhOqbHyVBUNxOwhGu4MxNgEV6V3FO7EfpCHWFdfhihd-_XIsj5k0ADHhZZNcPo2HuPeTHOS3l2reDnXyLyYBF1ocBJxcL-gh3Xqgn8YK8mfXlZLrQaDyIx6HyPhij9FaC3gh-1LcUAPrN30uV23AI3iJrvgIBB0g8mVCcQggn1hsLcAMrQcnGdxgP7uGafD0lM31PZefvhjFrD0P7VbqLnLhNsE5Aie7qsMC2sjYSMQMlU0jxazc8AMXk6L-68eSOqUfqzAi87IswYj8Ng4mYw1TiYR1KTPzhWTY77et5auG8c03CbvDW78" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خروج خبرنگاران از محل نشست چهارجانبه در پی شرط قالیباف برای عدم حضور رسانه‌ها در این نشست
🔹
درحالی که ونس و هیئت‌های میانجی در محل گفت‌وگوها مستقر شده بودند اما هیئت ایرانی تا زمانی که رسانه‌ها محل این نشست را ترک نکردند وارد اتاق نشدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/661825" target="_blank">📅 16:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661824">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e86ce32a0.mp4?token=dG9RhAQxmnIibzOJG4cpVfQ_Bv6gU8ks4NoCEZWtCuuSD7lp7x4n-Ht1Bd6pQyQR-6US0DlGMKZbb-EcTeFQ7B9DtYz6qsaD6xfwsbiez5Wjt9044gy0xvY4NHpwm7Xxg1zSQvN-7WNOqFF6hNZQFzBGcSSw9vK1WVpBbvWjWJ3R2uP_e1oS1JzY4BLbGbAFdHlWJsGLzkfzH9VTvmw5QTZJd_b7uFjG2t1_VB8o6nIxPeUKsjb8d2fOsXb8f4zYiqqiR_GKMp71jC8BXDMZXPQ975EfCk508BbCIy4PxCEzqLFYAtTjFw5Y4C1qmG4I5TyEs7gSix5_kxbPcqwqtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e86ce32a0.mp4?token=dG9RhAQxmnIibzOJG4cpVfQ_Bv6gU8ks4NoCEZWtCuuSD7lp7x4n-Ht1Bd6pQyQR-6US0DlGMKZbb-EcTeFQ7B9DtYz6qsaD6xfwsbiez5Wjt9044gy0xvY4NHpwm7Xxg1zSQvN-7WNOqFF6hNZQFzBGcSSw9vK1WVpBbvWjWJ3R2uP_e1oS1JzY4BLbGbAFdHlWJsGLzkfzH9VTvmw5QTZJd_b7uFjG2t1_VB8o6nIxPeUKsjb8d2fOsXb8f4zYiqqiR_GKMp71jC8BXDMZXPQ975EfCk508BbCIy4PxCEzqLFYAtTjFw5Y4C1qmG4I5TyEs7gSix5_kxbPcqwqtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور هیئت ایران به محل برگزاری مذاکرات چهارجانبه در سوئیس
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/661824" target="_blank">📅 16:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661823">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
مذاکرات هنوز به طور رسمی شروع نشده در عین حال هیات‌ها در سالن مذاکرات منتظر اخرین هماهنگی‌ها هستند/ ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/661823" target="_blank">📅 16:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661822">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bbd0a5906.mp4?token=vfKqfcuwtxe3g1Z_U_mzwBowQCarajiY2kGp_qRXaX_RjTyZgCtBZzjyiULfA0UbQsTRjbx_aDiX4y86jOt5rIuTTEgVRQ50a1UyDu214o0VyAuC3PHNVeqDrrTw52t56jzK5QsMHtz9Lqk6ankTVF9kvnMDT9TmAT8GKvYCHxWnCbk-nkG-rNZFgE42amOKbHCwxHUo3JBmmBcM_-SsOlq8wcMNGTTCObK20AEY0xTLZU81jlpz7ARnhACj75OpyTa-zkTbsW6D8UUpoONbYj5XPZsVTzfLlfPAD3xSl1_RUm_gDNEjXsggPkiEHrBPsebXEAf8qysHm8IdeYNXpV9nN2xYEN5-uN4QHfeTNgxNw7u2TZTM6czoAgTToLjcMHjTXMuXhtknT-GH9zuw-OXRyi4A9WzwXMhpXDrZJ5_gZhOk8XMeIoYrZ5YVUcUK2CiTX19GilIXcq6FaH9MwvEPafdN89g3Z3cYxjBHwzvypaEBuo1u8X6Omyaz6OcrbSZftZob6Mi-A9wsfnBDQcpF8BXbSxHwojrkt5wipPbu1OjNXjdlMy5Ik8d2a7k6T31SBLNFrMF3EvAUelOAByL6wnz2kaxVE13vcLh9Scsr4ZwydHCJbWdrvi0HkZRYIF0q46Kkn52TsIQSV3kW-DOJwoaKNgiVWiLNZ48KdQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bbd0a5906.mp4?token=vfKqfcuwtxe3g1Z_U_mzwBowQCarajiY2kGp_qRXaX_RjTyZgCtBZzjyiULfA0UbQsTRjbx_aDiX4y86jOt5rIuTTEgVRQ50a1UyDu214o0VyAuC3PHNVeqDrrTw52t56jzK5QsMHtz9Lqk6ankTVF9kvnMDT9TmAT8GKvYCHxWnCbk-nkG-rNZFgE42amOKbHCwxHUo3JBmmBcM_-SsOlq8wcMNGTTCObK20AEY0xTLZU81jlpz7ARnhACj75OpyTa-zkTbsW6D8UUpoONbYj5XPZsVTzfLlfPAD3xSl1_RUm_gDNEjXsggPkiEHrBPsebXEAf8qysHm8IdeYNXpV9nN2xYEN5-uN4QHfeTNgxNw7u2TZTM6czoAgTToLjcMHjTXMuXhtknT-GH9zuw-OXRyi4A9WzwXMhpXDrZJ5_gZhOk8XMeIoYrZ5YVUcUK2CiTX19GilIXcq6FaH9MwvEPafdN89g3Z3cYxjBHwzvypaEBuo1u8X6Omyaz6OcrbSZftZob6Mi-A9wsfnBDQcpF8BXbSxHwojrkt5wipPbu1OjNXjdlMy5Ik8d2a7k6T31SBLNFrMF3EvAUelOAByL6wnz2kaxVE13vcLh9Scsr4ZwydHCJbWdrvi0HkZRYIF0q46Kkn52TsIQSV3kW-DOJwoaKNgiVWiLNZ48KdQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی‌دی ونس: از وضعیت لبنان احساس خوبی دارم؛ همچنان برای صلح منطقه‌ای تلاش می‌کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/661822" target="_blank">📅 16:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661821">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3167b827a1.mp4?token=aydkQMRRg8kWwmu_WqUNkhx9-bbW_w0WUoBQsQhToDtrNmRwRHAHU12UiyBz6jEM2Rfitl8bYkKWWXo-PIS0k_F7PY0Abskt_FtM3LjTvx1IFEH2UWQdp_5AONs4m-utrzKJWOrxzWpZRjk4wuiTR_tF1AU8fSCXIA3v5oV70ev-hbqihvo1k9mxAxu7uwQiFBATZ705Lkg8uAzX_TNO_Xh-T54E2tGchv5uLbpZupE7qtb-nYKeHuOSVChr5T4GeROO7YzUle5kJkQZ7E3wRNbmV2gCrNH4a2B-evDALSfhEEzBfqOR_igwU-4-ZZe5spFAGzPeWxsiaAPk5LLsgFYr_Y8zNjiODa5nD1yom1c1fByJx9lYihZTYbUbT-DHtpshtKcjNXLZCkpUnf93ahV-c-sFh-uhECjj6uoVSntnL2iEbx04JEfks10gfK2IS32hNscg6z8lJYIste7Gy_N26nZ_Xty2lGj9DswJY_Ui7fZhQBYonq_Xe1Eu97JKazzjqFGwuBfDbBM7X32_RY19ImvoH1UKKDrRDi26bBvAzrHzjgUUgS2t_IxDF44criB-RD6nSpbUZit54H1IsJY3AMfpFlmXLqlQaYpH3WFGiK6op-MubqvS9FhFTS-f00WBacd8D-Cd-ej8Xt-Kgvf8PS4vZSVObmIhfvaURPE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3167b827a1.mp4?token=aydkQMRRg8kWwmu_WqUNkhx9-bbW_w0WUoBQsQhToDtrNmRwRHAHU12UiyBz6jEM2Rfitl8bYkKWWXo-PIS0k_F7PY0Abskt_FtM3LjTvx1IFEH2UWQdp_5AONs4m-utrzKJWOrxzWpZRjk4wuiTR_tF1AU8fSCXIA3v5oV70ev-hbqihvo1k9mxAxu7uwQiFBATZ705Lkg8uAzX_TNO_Xh-T54E2tGchv5uLbpZupE7qtb-nYKeHuOSVChr5T4GeROO7YzUle5kJkQZ7E3wRNbmV2gCrNH4a2B-evDALSfhEEzBfqOR_igwU-4-ZZe5spFAGzPeWxsiaAPk5LLsgFYr_Y8zNjiODa5nD1yom1c1fByJx9lYihZTYbUbT-DHtpshtKcjNXLZCkpUnf93ahV-c-sFh-uhECjj6uoVSntnL2iEbx04JEfks10gfK2IS32hNscg6z8lJYIste7Gy_N26nZ_Xty2lGj9DswJY_Ui7fZhQBYonq_Xe1Eu97JKazzjqFGwuBfDbBM7X32_RY19ImvoH1UKKDrRDi26bBvAzrHzjgUUgS2t_IxDF44criB-RD6nSpbUZit54H1IsJY3AMfpFlmXLqlQaYpH3WFGiK6op-MubqvS9FhFTS-f00WBacd8D-Cd-ej8Xt-Kgvf8PS4vZSVObmIhfvaURPE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ونس: تنگه هرمز باز است؛ باید نظم جدیدی در خاورمیانه ایجاد کنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661821" target="_blank">📅 16:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661819">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/381a23e1f4.mp4?token=DtkL_n4lBf5sS07vZ8A0lBxpJpNQPIgI6_SAL2uIy5j0Nkje--cDysw3LX2aJIiXEsE1qvv0vGr2-V7aLK_uD9veGSb_gq0YcYDrJRdLhlVvLb3ifAFzCt60N9HP_FUW2lN4SAz3lEsmNtkDF5Xn_bctulusIYFsIqwS7Lkf28SthDW8m1jtKFv08FSqp77XNgYk_-D_HE6jVqHOEkbILTYI-46h76fVpF9zpYQ6U3x77BCIzACieNWSQPOUADrDW6lJudNf-rbQfRQoOETNQhVVjiAGNEnyy100A6kUNjrANlQDbu5JqeKEcXgHLm4BvPHzpDfncLbCCRrck2xUJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/381a23e1f4.mp4?token=DtkL_n4lBf5sS07vZ8A0lBxpJpNQPIgI6_SAL2uIy5j0Nkje--cDysw3LX2aJIiXEsE1qvv0vGr2-V7aLK_uD9veGSb_gq0YcYDrJRdLhlVvLb3ifAFzCt60N9HP_FUW2lN4SAz3lEsmNtkDF5Xn_bctulusIYFsIqwS7Lkf28SthDW8m1jtKFv08FSqp77XNgYk_-D_HE6jVqHOEkbILTYI-46h76fVpF9zpYQ6U3x77BCIzACieNWSQPOUADrDW6lJudNf-rbQfRQoOETNQhVVjiAGNEnyy100A6kUNjrANlQDbu5JqeKEcXgHLm4BvPHzpDfncLbCCRrck2xUJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ونس: تنگه هرمز باز است؛ باید نظم جدیدی در خاورمیانه ایجاد کنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/661819" target="_blank">📅 16:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661818">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
سوال و جواب خبرنگار صداوسیما با ونس معاون اول آمریکا
🔹
خبرنگار صداوسیما: متحد شما اسرائیل چیزی شبیه نسل‌کشی در لبنان انجام داده است. مسئله اصلی متوقف کردن این است
🔹
ونس: خانم، من فکر می‌کنم ترامپ و آمریکا بیشتر از هر دولت دیگری در جهان برای متوقف کردن درگیری…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661818" target="_blank">📅 16:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661817">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
نخست وزیر قطر: آنچه امروز در این نشست اتفاق می‌افتد برای امنیت منطقه و جهان مهم است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/661817" target="_blank">📅 16:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661816">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e934f458a.mp4?token=eA5oV-GNI_tXJv5XUch5rsevprIKXlJV50P-fdD-h2Q40wyi02XFjq2RpCZfV1RE0A2HRoMVDjoNBhIQ5qSSKwD-LS7MZpU22RcKXX0tLgmPIiu_JHFMRma9R4W3rbonBl0kUFjPhWhl6T5gbT6hxO2I-gK6H6s4s3iN4FcajjVhdovTGblCHhy9rW3tK7p4RE1oDaI-DVVfvwZ2zuYYC2p8ymclB7nSdDZFAf3tkX7wOcdO77BQeAgg3ock5ZZXHbkcMF5zdOTQgaY3tP_IGtjpXqIL0DT8d9lxPMn7HpaA-WXbq6Sa-aQwh33M6D6_h-bKRPXuZGbGyGOHzTYEMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e934f458a.mp4?token=eA5oV-GNI_tXJv5XUch5rsevprIKXlJV50P-fdD-h2Q40wyi02XFjq2RpCZfV1RE0A2HRoMVDjoNBhIQ5qSSKwD-LS7MZpU22RcKXX0tLgmPIiu_JHFMRma9R4W3rbonBl0kUFjPhWhl6T5gbT6hxO2I-gK6H6s4s3iN4FcajjVhdovTGblCHhy9rW3tK7p4RE1oDaI-DVVfvwZ2zuYYC2p8ymclB7nSdDZFAf3tkX7wOcdO77BQeAgg3ock5ZZXHbkcMF5zdOTQgaY3tP_IGtjpXqIL0DT8d9lxPMn7HpaA-WXbq6Sa-aQwh33M6D6_h-bKRPXuZGbGyGOHzTYEMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سوال و جواب خبرنگار صداوسیما با ونس معاون اول آمریکا
🔹
خبرنگار صداوسیما: متحد شما اسرائیل چیزی شبیه نسل‌کشی در لبنان انجام داده است. مسئله اصلی متوقف کردن این است
🔹
ونس: خانم، من فکر می‌کنم ترامپ و آمریکا بیشتر از هر دولت دیگری در جهان برای متوقف کردن درگیری در لبنان تلاش کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661816" target="_blank">📅 16:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661815">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940e599964.mp4?token=lYvgCq687v4jT0JBi6UW01eOnfi2DJCI4LgtoyhfB9ZR7oO1FwbtRPLDzm5nWK6sCh6ZfTufeFRsaPkMGKA1V4dJjiZg50Agh_kVgZvwy-v64RQojtv9tQy01S2PdZYe8Q0owGcEUHlsYXI8AvQS2rL-Vnf8amCYWTGXxb2hm7qHdV3XuceMG5K-QRoifZnLuWtmyLCuqAfZOLEN_US6XtgLuUi10OvVXbV3r6Or2CziYxl-yTXEMGi4bIR8BOGSmV0wuH7KWlxBlc_ou2GQi2PH9EvCqniDLSNGPFtK9UPxY8YliU0OebW1NUovB33c71NH1zNIH__1WgyDd-tg3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940e599964.mp4?token=lYvgCq687v4jT0JBi6UW01eOnfi2DJCI4LgtoyhfB9ZR7oO1FwbtRPLDzm5nWK6sCh6ZfTufeFRsaPkMGKA1V4dJjiZg50Agh_kVgZvwy-v64RQojtv9tQy01S2PdZYe8Q0owGcEUHlsYXI8AvQS2rL-Vnf8amCYWTGXxb2hm7qHdV3XuceMG5K-QRoifZnLuWtmyLCuqAfZOLEN_US6XtgLuUi10OvVXbV3r6Or2CziYxl-yTXEMGi4bIR8BOGSmV0wuH7KWlxBlc_ou2GQi2PH9EvCqniDLSNGPFtK9UPxY8YliU0OebW1NUovB33c71NH1zNIH__1WgyDd-tg3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قانون پول برای مدیریت درست نیازها #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/661815" target="_blank">📅 16:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661814">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
حضور هیئت ایران به محل برگزاری مذاکرات چهارجانبه در سوئیس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/661814" target="_blank">📅 16:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661813">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8ee2d1f5e.mp4?token=SOzBwc961fOcobWBXMcEiwYVoANEJJr-m4puYeDraVqbvah72VCPCjfhtxYEK22qwOc1MeHiChv1t_8FP0yY8z9_yMgKv1Yog7wrKE6uHn0caeNMFKhRbtLI3Us2B0UkqiJBs4t-gTNjBa3Yl9DO2hvrHRrdyP7vUGrcNDm0xHqaQnFokZ75U2NU1FBzASLbQsXacq786y0KIt_cDBnWXkkpZOpYRgT9VW8OWbMcnh_EqG9EzWUHLxa36RXL_N-jTpBnYFCDvIGtJI0UYvqhLk_SX2FfNbwPwufwzzLg9QY8lb5PYQk5DG0BsjLq_LscW3P1xr3zNQIAMchMG8Z-aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8ee2d1f5e.mp4?token=SOzBwc961fOcobWBXMcEiwYVoANEJJr-m4puYeDraVqbvah72VCPCjfhtxYEK22qwOc1MeHiChv1t_8FP0yY8z9_yMgKv1Yog7wrKE6uHn0caeNMFKhRbtLI3Us2B0UkqiJBs4t-gTNjBa3Yl9DO2hvrHRrdyP7vUGrcNDm0xHqaQnFokZ75U2NU1FBzASLbQsXacq786y0KIt_cDBnWXkkpZOpYRgT9VW8OWbMcnh_EqG9EzWUHLxa36RXL_N-jTpBnYFCDvIGtJI0UYvqhLk_SX2FfNbwPwufwzzLg9QY8lb5PYQk5DG0BsjLq_LscW3P1xr3zNQIAMchMG8Z-aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتظار هیات آمریکایی برای ورود تیم مذاکره کنندگان جمهوری اسلامی ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/661813" target="_blank">📅 16:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661812">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
هیات پاکستانی وارد اتاق گفتگوهای چهارجانبه شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/661812" target="_blank">📅 16:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661811">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cab144afd0.mov?token=fhez8sW8_aV7YkE6JXDTuTDgPvUrc1__sdJDtfDbemrwWOGfkGymo0kFVUVrS20Y8Vms1uGZCvWs55sOTNdKis-TYiG4eXMU1IaFfQZucRaVdUlXurkwk78YxZUntZzYR4f6DE8ujmJvdQSFycIb0rOKdC-hjdAXujOpixW2J-ig-OrJlvDClq5LB2QU-V4XftUa4wWKnl73BJxFz37t-1_pSXIpf8ojviSXUftspMt8dbPvXzoTRk3ThaRnq2LINHhN8gaFBVhn8eVZ6d7wgMrrPeuFzF0oszTMO8d5urrlr_0MjKsCeq3bm7aPJmtvAY_ZNllNjbCyJBM3EkObuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cab144afd0.mov?token=fhez8sW8_aV7YkE6JXDTuTDgPvUrc1__sdJDtfDbemrwWOGfkGymo0kFVUVrS20Y8Vms1uGZCvWs55sOTNdKis-TYiG4eXMU1IaFfQZucRaVdUlXurkwk78YxZUntZzYR4f6DE8ujmJvdQSFycIb0rOKdC-hjdAXujOpixW2J-ig-OrJlvDClq5LB2QU-V4XftUa4wWKnl73BJxFz37t-1_pSXIpf8ojviSXUftspMt8dbPvXzoTRk3ThaRnq2LINHhN8gaFBVhn8eVZ6d7wgMrrPeuFzF0oszTMO8d5urrlr_0MjKsCeq3bm7aPJmtvAY_ZNllNjbCyJBM3EkObuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هیات پاکستانی وارد اتاق گفتگوهای چهارجانبه شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/661811" target="_blank">📅 16:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661810">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pH4MOP7xKnXcCPuqq-xDBDfX4MVFeMAds3Tw7x2Vth4iELBYsAhxZP7DVhXkmBQp6lWlzylBTVaaPB8Zudez2XB_6kFA2O_USn0xJVAH8WZomvQOTuAb0_Q0s6JhwKYDofFdnhq51w7moGNMo5RuRBZ_jNZK8hdUZxHdum_4xd8DlvfEjpp7lwy5Q4c1UPBzqWL00TLnH7Bio3ITKQt3wQVH5w4UnrIYBkShJ2MRiJkyOTep-aXM0XbU9XMqnkRu_pZz9QiXwgnY97PvTHecmYbQnAlbcbvFL78gX9-SQiWc5emriiWojho0BylaKELD2wbRiCwbL9BQSFYotqou0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آینده ونس به صلح با ایران گره خورد!
نشریه اسپکتاتور:
🔹
ونس به چهره اصلی روند صلح با ایران تبدیل شده و آینده سیاسی او به سرنوشت این توافق گره خورده است.
🔹
اگر توافق شکست بخورد یا در افکار عمومی، عقب‌نشینی و تضعیف جایگاه آمریکا تلقی شود، ممکن است اعتبار سیاسی او آسیب ببیند.
🔹
او اکنون در حال بررسی این موضوع است که آیا اصلاً در سال ۲۰۲۸ نامزد شود یا نه./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/661810" target="_blank">📅 16:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661809">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWt-B1QQOF626xgvIHSpIH1MZV-C7hnock3_9PxPQS87fMvEjrPRAxp4MsL0b57oA_fcZzRwuPKgEd0g0KWPM8lieZtscCYGaCSL50qEYnF1oxfX46Yn7QGx0qz0f8Na22ojI3kIYD4dysuzQmwem44zVjTS1JClHT3oR6E3JCpIcMSaIGSJkCh5IhwRnykIl60dk5V3eUiona_Auu41MkR8TIgJ2igFuPbeHmP_dysPlZLyOjL7DTY_wkEWMUQt-OyVa9pi6ZqmLTlXQPpP34BJ4sckI9fjxUpS3pw-IMVdeaRtL0J-RX1fiWNwZpwm-SsIDQKlKJsRmm2fyDzb0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محل نشست چهارجانبه ایران، پاکستان، قطر و امریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/661809" target="_blank">📅 16:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661808">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
عضو کمیسیون کشاورزی: قیمت آب افزایش می‌یابد
محمد جلالی، نماینده مجلس:
🔹
امسال به دلیل بارندگی بهتر وضعیت کلی سدهای کشور بهتر است. وزارت نیرو هر ساله این اختیار را دارد تعرفه‌ها را نسبت به سال قبل افزایش دهد اما این تغییر نرخ برای آب شرب، پلکانی اعمال می‌شود.
🔹
دشمن در جنگ اخیر با حمله به آب شیرین کن‌ها، خطوط انتقال و مخازن، تاثیر مستقیمی بر وضعیت آب کشور گذاشت اما این موضوع مشکلی برای سدهای کشور ایجاد نکرد.
🔹
استان‌های قم، تهران و مرکزی از متوسط بارش کشور پایین‌تر هستند و مردم این استان‌ها باید صرفه‌جویی و همکاری بهتری داشته باشند./ همصدا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/661808" target="_blank">📅 16:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661807">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbXsaoME50OrjmugM5AgFdk4ybAZKQyRjS2w5QC8bCoOjRs950SwTqcmcoywKzT7UveRhDeBCHmTOufeqOG4R7h9oWVilpS-h8c0zvScUxgHYG_QgQSSMhysynu0Hf66d34K-ucbQq4ZLEFHL583Tjy4T45ztuQl8q1M-GC3XN8e1l8Xw7GQGxuzjGDI8cB36-nhPCcma1GraiTgj7pVok-1BwDH32BRv4cQKH6R9jk0zJAR-tFEIbloZCyJzcf2ScezVpN60yKlaKnZIXp9ci3OxhPbOL41I-AWfWbWIEWeyK492IdkwE4sLnLtnYiuRx5Z3ym72aFtjSUCo5abaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پوستر صفحه رسمی جام جهانی برای دیدار امشب تیم‌های ایران و بلژیک
🔹
این بازی ساعت ۲۲:۳۰ به وقت تهران برگزار می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/661807" target="_blank">📅 16:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661806">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qon6aFNl5dH6sfN6kweh6R3c_pbepR5z9MNu1Nnv3pMInziXwyyVHUfF5Ybfr3a5OSmoUZij3MHRKf3W80u5wLG8cbYzmY6-VqL6-kdZWKk6DnB_DYVNnFvwTM7YsxhQQoB0SfHjB5-_l5WVwVbYht_b8fV1XIEE6x8F3vYxzOoUOn2_QdGsfu0olyFtG28l_wgTErqIkk8cAdR0rBri7z9fRzfVtn5TLSLzJLzNyV-AeKE4oLd2w7BLvGsc5YhUyC9rgUaoYSuOPIEWnPKztEEGUe1z9u56M_lXZrr9EiNx2R83EMGj3p8HqW0qy2ZSUp7aR7hyGG0h4WMgwCSWJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ضربه مرگبار حزب‌الله به گردان ۵۲؛ ارتش اسرائیل از کشته شدن فرمانده و نیروهایش خبر داد
معاون فرمانده گردان ۵۲ ارتش اسرائیل پس از تلفات سنگین در نبرد با حزب‌الله:
🔹
«چند روز گذشته از سخت‌ترین روزهای تاریخ این گردان بود؛ فرمانده گردان و شماری از سربازان‌مان را از دست دادیم و با خلأیی بزرگ و دردی عمیق روبه‌رو هستیم.»/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/661806" target="_blank">📅 16:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661805">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
حمله هوایی رژیم صهیونیستی به خان‌یونس
🔹
در حمله هوایی رژیم صهیونیستی به غرب خان‌یونس دو نفر به شهادت رسیدند و تعدادی زخمی شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/661805" target="_blank">📅 16:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661799">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd545f3887.mp4?token=J-OLi_yBupjuDoTjKyylvqVQoy-xOnPIOEOGdbo3XYRFl2o-ibBR878cSJCSFZMpQo2_UkwvRptuixAEgprUPajSsjgB6_z4V-Wd3KOvZEa6iYGiSa2u02cAaFQ4EMnMuYiQFZDix689CESNuU0D1jsJYybUv3k7Di_kk81szAanRL41VMgG1vgXxUPXEB3QD-gx8ru-5RnBKbmCh6CZacL3uDu55kox2GPFweS7UitLdn4EwEGEO4xjN8qpL6sx8otrq6SAmdQYMAfzqTCmfsisib4BqSNC6Fu5-dD26rp5Kvs9xumT34Bh02tsHnu0xyxY-IEDekc9t4uJTCWOKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd545f3887.mp4?token=J-OLi_yBupjuDoTjKyylvqVQoy-xOnPIOEOGdbo3XYRFl2o-ibBR878cSJCSFZMpQo2_UkwvRptuixAEgprUPajSsjgB6_z4V-Wd3KOvZEa6iYGiSa2u02cAaFQ4EMnMuYiQFZDix689CESNuU0D1jsJYybUv3k7Di_kk81szAanRL41VMgG1vgXxUPXEB3QD-gx8ru-5RnBKbmCh6CZacL3uDu55kox2GPFweS7UitLdn4EwEGEO4xjN8qpL6sx8otrq6SAmdQYMAfzqTCmfsisib4BqSNC6Fu5-dD26rp5Kvs9xumT34Bh02tsHnu0xyxY-IEDekc9t4uJTCWOKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نسل حسینی
🔹
مخاطبان خبرفوری در این ایام محرم، ویدئوهایی از عشق و ارادت کودکانشان به امام حسین (ع) را با ما به اشتراک گذاشته‌اند.
🔸
شماهم با ارسال ویدئو مداحی نوجوانان خود به پویش نسل حسینی بپیوندید
👇
#ایران_حسینی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/661799" target="_blank">📅 16:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661798">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hy7-N7De7rkM-ddDnQyXDMgz-Nlp9RcXXGyJdb13WpFdoRBlItLMudMA-nvFWMBGNQTwXd7WbsW6fy_wgM7pY50MWSzJMAgvuBlTv8qeEXftRc7py3WeR8Esh41QCPf7LbpzEo9WZV4GLRaZ8TR0uN-64PkSD-t22a8i9cAOGLG4UBZzgCfn2YANZTNnV_WRfKzqe_i1u_6XP8_t41Ib_Duj5WDogx9JzHyrnrYtNgRRGzOTsQ-Y8wIGHAJVXcGqTuOTrudkYKpF6D8GJbP5JqHlVYhtrA8RgU35LCPvIaH_aBG7pcGJyleO8sEvGTHdnwu1MDOtIfqQ4UJJTOQucQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رابطه ایران و آمریکا در دو ماه آتی/ همه چیز مجددا «استپ» می شود؟
🔹
بعد از جنگ ۴۰ روزه بسیاری گمان داشتند فضای «تعلیق» بالاخره از بین می رود و ایران و آمریکا «تصمیم» می گیرند که به مشکلاتشان «پایان» دهند اما تفاهم دو ماهه به نحوی منعقد شده که به نظر می رسد این فضا همچنان بر روابط ایران و آمریکا حکمفرما خواهد بود.
گزازش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3224767</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/661798" target="_blank">📅 16:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661797">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
فایننشال تایمز به نقل از دیپلمات آگاه: مقامات قطری به ایران گفتند که اگر هیئتی اعزام نکند، عملاً به نتانیاهو «حق وتو بر جنگ» را داده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/661797" target="_blank">📅 16:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661795">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9356253177.mp4?token=hFmqYWhuDmCtgEH8sIe-9NRRWY1vRqx0OovxwkAK0QT8a22oVQjNlDIJa_liMXYzw1vv5qBB6i3h1IupttzlnA7je0E9W6mdwadpvpP_LHoCPSaGOtfUTRgQW2b1RsGw5POz5H2QBc83gKpj-r2LwELn6qQbFQZ0E83YGlSyfg2_sbTttDUyT4C-ftXsSHzJ0GfbZcA6o3xP5qS5vqLgzFmhasOY-TVO_ji4D_TxeFDbfxoUivUH1qunrzVt-NrazpH6ehB3sR2RHgo--eJMNXICuHoYFoGdF7_8OIH0tAH-CXlULgar08PhvluniqUJcI5AJzgSs8T_Wp0BlrxXUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9356253177.mp4?token=hFmqYWhuDmCtgEH8sIe-9NRRWY1vRqx0OovxwkAK0QT8a22oVQjNlDIJa_liMXYzw1vv5qBB6i3h1IupttzlnA7je0E9W6mdwadpvpP_LHoCPSaGOtfUTRgQW2b1RsGw5POz5H2QBc83gKpj-r2LwELn6qQbFQZ0E83YGlSyfg2_sbTttDUyT4C-ftXsSHzJ0GfbZcA6o3xP5qS5vqLgzFmhasOY-TVO_ji4D_TxeFDbfxoUivUH1qunrzVt-NrazpH6ehB3sR2RHgo--eJMNXICuHoYFoGdF7_8OIH0tAH-CXlULgar08PhvluniqUJcI5AJzgSs8T_Wp0BlrxXUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشاور علوم و فناوری ترامپ: «این توافق یک دستاورد بزرگ است؛ جایگزین آن، جنگی فاجعه‌بار و بی‌پایان با ایران خواهد بود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/661795" target="_blank">📅 15:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661794">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
قطر آغاز نشست سران در سوئیس را اعلام کرد  وزارت امور خارجه قطر:
🔹
نشست سران در سوئیس آغاز شده است. نخستین دیدار میان واشنگتن و تهران با حضور دو کشور میانجی، یعنی قطر و پاکستان، در این نشست برگزار می‌شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/661794" target="_blank">📅 15:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661792">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
وزیر خارجه پاکستان به الحدث: ما توانستیم آمریکا و ایران را برای نخستین بار پس از ۴۷ سال پای میز مذاکره بنشانیم
🔹
سه تیم فنی در مذاکرات بین آمریکا و ایران مشارکت دارند.
🔹
کمیته‌های فنی در حال بحث دربارهٔ پرونده هسته‌ای، دارایی‌های مسدودشده ایران و موضوع لبنان…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/661792" target="_blank">📅 15:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661791">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کوثری: ۵ بند تفاهم‌نامه باید زودتر از بندهای دیگر عملیاتی شود
اسماعیل کوثری، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
اصل قضیه این است که ۵ بند زودتر از مذاکره باید عملیاتی شود؛ بندها ۱، ۴، ۵، ۱۰ و ۱۱. اگر این بندها عملیاتی نشود، به بندهای دیگر مراجعه نمی‌شود.
🔹
محاصره دریایی به عنوان یکی از بندها از سوی آمریکا برداشته شده است، اما حریف سگ هارشان یعنی اسراییل نشدند. باید آنجا آتش‌بس را رعایت می‌کردند، اما به مراتب بدتر از روزهای گذشته جنایت کردند و تعدادی از مردم و رزمندگان حزب‌الله را به شهادت رساندند.
🔹
طبق همان روال ما هم تنگه را بستیم و اعلام کردیم تا زمانی که آنها رعایت نکنند ما هم تنگه را به هیچ وجه باز نمی‌کنیم. ما باید یا تنگه هرمز را ببندیم یا با موشک اسراییل را مورد هدف قرار دهیم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/661791" target="_blank">📅 15:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661789">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
عصبانیت ترامپ از نتانیاهو
وب‌سایت «زتیو» به نقل از منابع آگاه:
🔹
ترامپ به شدت از نتانیاهو عصبانی است؛ او گفته که دولت اسرائیل سعی دارد او را فریب دهد تا دوباره جنگی تمام عیار با ایران راه بیندازد
🔹
رئیس‌جمهور آمریکا به شدت در این باره فحش می‌دهد. در حال حاضر، او قطعاً از اسرائیلی‌ها بیشتر از ایرانی‌ها عصبانی است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/661789" target="_blank">📅 15:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661788">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
مدیرعامل سایپا: پرداخت جریمه تاخیر خودروها از سرگرفته شده است و واریزها بصورت هفتگی انجام می‌شود
🔹
برنامه ریزی شده تا تولید روزانه از ۱۳۰۰ به ۱۸۰۰ دستگاه برسد و با افزایش تولید، میزان معوقات را کاهش یابد.
🔹
انحصار برخی تامین کنندگان قطعات را شکستیم و با تامین قطعه از منابع مختلف در تلاشیم مانع از توقف چرخه تولید شویم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/661788" target="_blank">📅 15:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661787">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c5461519b.mp4?token=uaTk3hAjwZoPnZDJtxfguhlzYa_abXzMSE2q1kLi3f0JNnXuWXPr6OJN4-kvUjoQ1kmHgoY8AFZKNvZCavA-rRUgHhXNWxPlOKTNiCW8edVPxY9mORSgiGKj28q73hEukTf3ugXEdTr7sY88ekPgXT-tQ4x66YHzvaSGxWZfasyGxnNXNVlyY3ksyqKO3CJoNEsIxMjfsmp6ZFNAXjJ-VKF0jiJEDI0gn6a9I3YGSqE8oDelCuX6UrOtM1wjK6wCnRjvO5tS3FBpCYtyY5B25UDn5PhlqSJiWAxwsEZaV_dTP-tV_aazHSHbdDGrOr0e_86iGtHtVjqQ9KgbKQoAfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c5461519b.mp4?token=uaTk3hAjwZoPnZDJtxfguhlzYa_abXzMSE2q1kLi3f0JNnXuWXPr6OJN4-kvUjoQ1kmHgoY8AFZKNvZCavA-rRUgHhXNWxPlOKTNiCW8edVPxY9mORSgiGKj28q73hEukTf3ugXEdTr7sY88ekPgXT-tQ4x66YHzvaSGxWZfasyGxnNXNVlyY3ksyqKO3CJoNEsIxMjfsmp6ZFNAXjJ-VKF0jiJEDI0gn6a9I3YGSqE8oDelCuX6UrOtM1wjK6wCnRjvO5tS3FBpCYtyY5B25UDn5PhlqSJiWAxwsEZaV_dTP-tV_aazHSHbdDGrOr0e_86iGtHtVjqQ9KgbKQoAfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چه مبلی بخریم که مد باشه؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/661787" target="_blank">📅 15:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661785">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sI_OBZTmr0lzEO3HmVMNCGc3B64yp62ysV9Yc8o92uQHdPMULD4PRRhHBL-NeGMpS4h3_mbZyq4QiSo5mAwmr1RgY_6aqoZjF0KgFK9rwsU9VNByqKHFdGDGlLyA_vNJlLFLEarDY7qaTz3LqZh-5vDHXCscW3Jfu8ROzSMcgwt2uKq3Z3m6nuiAj_Kk069_GOMttG18Zrm6hFtOTGx0H0nog1Q8I1Cpy_jtfA9n_F0FFMQV2V3vIEr0VWr_dniVG_Lx-KynOZ8ld9pGstMjhchnYSwiYYXzKHpGpdb3glepWWBgP9LDUco7JJCteJmL3sYkYEHEOD7E18boQMjzVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تکنولوژی بومی؛ پلی برای عبور از بحران‌ها
🔹
هدف نهایی هر سیستم مدیریتی، بهبود زندگی مردم و رفع موانع است.
🔹
تصویری که می‌بینید، استفاده از یک ابزار کاملاً ایرانی برای هماهنگی‌های فوری در شرایط حساس است.
🔹
پایداری زیرساخت‌های داخلی این اطمینان را می‌دهد که در سخت‌ترین روزها هم ارتباط مسئولان با نیازهای جامعه قطع نخواهد شد.
🔹
ما در اسکای‌روم، فراهم‌کننده بستری برای این گفتگوهای گره‌گشا هستیم.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/661785" target="_blank">📅 15:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661776">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tSZr3_BI5bO9IHyqpT5M5Qz2G2a6fTKW7L1vB6q-uU7eWulv2t4GFebZ1vcHfIl5OcokhTnFGIwlmhaderEDG3U7bH3x4Nl71x0cyBZ4Ks9jk4W2MwsoHaJ4pGWIwHr_LAYGKuqGiTHFt0-jl93GP7jJS8DgWcpAOhapBLVLUO_Q9E22CtAV_-7bGtf0qNJmkT0zYCpQ_xL0wHXwu3mHbRyTmmpxdr3pkOQHL8bapeuJzJdv14XbxSMfarDNp2qKeLDnSwgLgDLU5tuFYLcsPEBU_2SyXxTrz3SxWJU55n8ETAdSx7EAXYHAgT4nH2vcep3VvjAuFpyMy4aPvLielg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H58ojKJ2IzjPd8zu7ZgPuCTnqSqi257tjjlo2kIpH0whT91oESalTQx-ra2dz2I-C6JbPzhO93BuWGfU0RKY9TeSfxq68oidIqZaCM7SzUlk6aWfMSq0AIPXHlI1jYbLhfo3MNfLqbTOOmRq58g9s6O-W0IT3KoKH3iyfm1gEvPG2FsrprrksHFn3xV7fVgaeamm5LzHSGkGI_wIdvzJkDcb_5Ye5_P3omHwdJNYTVoSsVUo8UdMWWMFEGq95UzJEOLRaFhprcSzPlCRoaxyZ1l2MK6Az76DhJxBZxDsaKaDxTF5LRQCW6ZHAJHQsq1QkP8CAmKf_TtWnlEMbSvJbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g5IMgnICjScjt6eVm5BgaTBW011KUioSprkUcXcPWl9P2NPWLBF3Xlr6YBmNEtc8RKFN9EC086W8OtzJXjLAfzyxrHqr3-sFZPzuCx43Kh7vBTvROPb5vqsm2CZsPTRTr7dMXgsiKCSVJHCqaTRIpC2cegcFl9HqANB8u3noGHV_PPlASfulXBM0x9MuVerJZjvLFyb9XiwSauwSw9ORTBDFk-bXeof7_E9gunNj2EHCiwRfCRKS8WhwHqa2RKYYNOKyOflpssg2RpzcWXoHN9DfGG0OH8KGFdUUzOyNJ_6tbZl2NemNf047zze0gWKOQEXLTGoGzucQp8qS67PRpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ia5KmJ2OXBvUJ-1g6saYnL-LhiCI-WObSXVJrmxiYiHuFu8IzQlWQ3WNrhImysDor-Pyf2dmCy-_GNNqIecrcC9aBImriZkNy6BmbyiVHWJLnZXqc0OyKdh8biMqPm1_1PJvFqstg5rpSkaKSTbv1uynv9hFRST0RKg7R8FHz1HrR2da3nKUnsVBbqlDrRoAzjypbUf9es0fyMYXhhkxGtWnfiTn8plSoxn6j_d2RbcDJzakC20cy5n6f9GEVrxhgITj86UDMWPTx_YYsYlIdEWhOzPCF7P-vKZ9mSQjhC8R-19kAQpMWGw0xb8PplZt_Ep8Bv_gagmJscuQi3HWkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OjhVKYrSxkbZYkl21Tj7Px-QvI-SMBzp5FWka3m_7u1xrlg3u1tsh_zq-SJCP7Vsx-Mw8L6-d3VMJl0ZGMkwfn6wy96afH7qYQ5gzvE9dlo2iJP0hPwZ8_LwHM5_pArYd095bshxgrXRA15KC20TD20rkT7l-wgrVo_3HvggdTyfO_jQv7K3SlycxGN5j8p53OqVOvuS-EJIkOiH5SavbsuXsrMTAESzwfL7x5wEUtcAVKZhhBuThHl58YNspxqNgc3_6VX3Ec5rbv7M7Q_2_7seyx3VugY_jdPZWUl_FatWSaKzHn6b1ac9phxaU00_RM-8rhdpF6q50TePGV-j8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rw7RS-sivZSosD2n00VhdGGMu0Jpx5pRdkdyIcLA8v9CPSKP2Q0N6FHZ9sWBSKBp3fzkOo0pHTV1iaUmoZltMrFJG0Ni0Y8JXc5pLq9hgg0kFBc3cnCDAzKC4ESv4SxASvqWEmbXLooYXwDtNHZRdGu0cX_f3d8goHDzNfm5vE5n57Tj7tguqHyXEKPsT-DleBNC6MwY-Y1uiZu8wbVw790vd1wfGooZYKWkIsGV4SPIw7MxWq89tHv2zNdd7txc3XaFIsT-ibSSx298ICeCaDxNSD_iZx7vwmN7st34IysX4-7ClLHRsqxP4IPZ19ubewtJR0QPtt65WjZjz_cD6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H-IKrrC4G2L0Rpc6rLGTbFGS2uCfo84qxQ3FuA1fUoW_fpbCCAhnSqDL00GKBCEbAbi-VsbXzMCQY1NAtN7ZbIpumTEyueV0lD0Dg0RfYx7ttNTEvwTYKutgY2Rc-lpwKBiPy14vR1N_wiZhXhdStepuzsGTlrWHAudmBCyRyOs60VcbQ5aZ-oY83MURYLoZ2a0hHA_I0ntOd8Ox9AXoY7WJjx61yqmHkD_dinspRRcQCexHbvr0b_LujRA-0mjv2bwuehIVuHaQ6G3B6OfALJJtGa8ysTlLH8fLzwwXFz3fiKX9-stc2XqI4UiM1Zfi5DZ9Nu4Zwv2c3iGitPUpEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C1aXhTSCOfhfV7D5bkkSmHhXIpuRwpPX4TLcJ2a9AZC458RFmnohTNMB46otzG1X-8FgVfgaB99gMdbIwLYv6m2ofUx-MOhT_oHSeh7_fswT252FDrb5weM9zk6uKgzEhcZ8tK6xrAEDJISEJl6EWG5NWxejtxCiSiy3l0rgWOS1Jz_m4FRhQ6Ul9CQGRPb2PTRVwa0lKTZMRXusu63QXfOgxA5eRjhL5J0GpqMmU1BZpD2-WN6u6I_GoFiMvl8xH9GslD2YbMmJoT8hcjNa28knz2trzDCtFYA2dAXTVfWYA4PXuz2vfyPof7jL-avrixlRZHjHWs4-WjuPzmNRVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PVrNuVlNWDZXAW39VIpXosJ6wVJwsVyR5wauTqZEjGo_Kch4MVh6QKPBzjeHcVHw7WnXEqWQ_9LOVmxXnLUKP49NboXwEEyq2-hEPtSwMphmPGw32xkm2ARQvqSUIEXacBOpmSxMzCxE3EJbNDgIyKATxEOMz7vreNSvcdmdO-bLNBlaKHeTYYyS8Io43xsmH6l46pYGpESP-6fZhmLMlnmNcnHVXCGdVL4vU-t9JGaRWRj5hJN3Hs7CSxcMZPE2xfbex7aSFHul3c9LaIV3_GojbYWBfv9mkXpOixRtrhrHX8kcTkBEQuE9BFmO2iIVosO1gKJwanUxq36xAYAlBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
در روزهایی که
#همدلی
معنای تازه‌ای پیدا کرده است، حضور شما عزیزان در کنار
#هیات_قرار
، پشتوانه ادامه این مسیر نورانی است.
💫
آنچه به ثمر می‌رسد، حاصل همراهی دل‌هایی‌ست که با محبت اهل‌بیت علیهم‌السلام، شریک این خیر ماندگار شده‌اند.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/661776" target="_blank">📅 15:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661775">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSeXRnOmHNlskycP_hwuymcJvNzUJ2k0c2SZm9GC56gZ_7DOsDigzBXv5Z0gY7_5OvVQ-0s15DryDpRGiGqUPSyTRODLFmKmpNbb057OveGVjL7rkygg6GTy7DHFO4hGVSJ3CeK-W23fyC-ZEXFOUq7DluqDCo3c7HxlIxI3uvuQR9yh8sFV0S6hOydo04OSSzppCAsIZAnWg8w1Kx3L7_Oii1GT2nVSvOoiIALtruYi_LeXjcne7gau8jX88GfYKQmFPG2vK3pCpCpWb0aRjmA4Pg405yiyXWLq_IRoiHwctGbJ01nBS_ZCVfCVI3Fl_aCsMNmyM3Ao_ldxuBycCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدودف می‌گوید روسیه دیگر به قواعد جنگی پایبند نیست | جنگ هسته‌ای در راه است؟
🔹
گزارش تازه دیلی میل به بررسی احتمال تغییر رویکرد روسیه در جنگ اوکراین و بحث‌های مرتبط با استفاده احتمالی از سلاح‌های هسته‌ای توسط مسکو می‌پردازد.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3224713</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/661775" target="_blank">📅 15:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661774">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a48d6a91cb.mp4?token=VPcU1mOBIbc8dS1GP_r8W8sGoqbJAGF2TyBdldn1Ma9eSDxg0PlZBXUi0xEvEkzxMQ7p3MwA5-4gghpw_ZlWZhk4Ev-5lBNpinQT7uV8vR6ySBEL3cXxnaNUHHZ7iMkSDkNn5FsoXSObPQI4cZahnEua1KYkN75_7NXL7pbTUMv1lSqa9XwMvg8pM3y6E9O2rj7Eaje44z1AuXnwTG3LJ7pamyGSkkdOG9MWjnPhZVaGGcI8cEQjz_U2yQFj7f3wO1ZMlk0ZQ7CdZ2ioPaS1bIvDAxeCQzLG-Hr-FTWMnkNm6iBStlrp5_K8nZCsJ_h37OZ25Xx31zLcsDaN9yRz8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a48d6a91cb.mp4?token=VPcU1mOBIbc8dS1GP_r8W8sGoqbJAGF2TyBdldn1Ma9eSDxg0PlZBXUi0xEvEkzxMQ7p3MwA5-4gghpw_ZlWZhk4Ev-5lBNpinQT7uV8vR6ySBEL3cXxnaNUHHZ7iMkSDkNn5FsoXSObPQI4cZahnEua1KYkN75_7NXL7pbTUMv1lSqa9XwMvg8pM3y6E9O2rj7Eaje44z1AuXnwTG3LJ7pamyGSkkdOG9MWjnPhZVaGGcI8cEQjz_U2yQFj7f3wO1ZMlk0ZQ7CdZ2ioPaS1bIvDAxeCQzLG-Hr-FTWMnkNm6iBStlrp5_K8nZCsJ_h37OZ25Xx31zLcsDaN9yRz8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دانش‌آموزان میناب در کنار تیم ملی‌اند؛ در میدان افتخار
و در هر فریاد «ایران، ایران»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/661774" target="_blank">📅 15:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661773">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12ba50d6cf.mp4?token=Ihs8xBh_eNnEhSM6iUp-IBJ56OODUptUXMc515eV-4xnRnhXDq63usM5LYtnBfvif_PvVqCQmEKVX4aJfBq5Sx_-PPTJgmW8dljJr_Geg5URveHZltk82SZivG8fPEcVQiK_XAfuW8t4RK29g-BB2bpDj3Fb2Iw8cb0JDsGrhTSbxAUwl0Tle4ot8bW2cQPeiimcfLcJXDigg2RVeoxQdpyzxnydyc5Vtf3VIwWUQZkazq2NPhiWNBOB_ZxcnT6BZvls7awOYih3O2z9Sj4_a2K52vMTekJF4V6vH3JNDCz0o9AsD0Batcwp1WosbVEvITEBNLqLdAjLb9HgusSSwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12ba50d6cf.mp4?token=Ihs8xBh_eNnEhSM6iUp-IBJ56OODUptUXMc515eV-4xnRnhXDq63usM5LYtnBfvif_PvVqCQmEKVX4aJfBq5Sx_-PPTJgmW8dljJr_Geg5URveHZltk82SZivG8fPEcVQiK_XAfuW8t4RK29g-BB2bpDj3Fb2Iw8cb0JDsGrhTSbxAUwl0Tle4ot8bW2cQPeiimcfLcJXDigg2RVeoxQdpyzxnydyc5Vtf3VIwWUQZkazq2NPhiWNBOB_ZxcnT6BZvls7awOYih3O2z9Sj4_a2K52vMTekJF4V6vH3JNDCz0o9AsD0Batcwp1WosbVEvITEBNLqLdAjLb9HgusSSwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امیر قلعه نویی در نشست خبری پیش از دیدار با تیم ملی بلژیک: کمتر از ۱۶ ساعت به ما وقت دادند و مجبور شدیم تمرین نصف و نیمه‌ای انجام دهیم و این کار ما را سخت کرد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/661773" target="_blank">📅 15:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661772">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cF2JgIrwJgyldYxmLRcTfXt-t3xJnz9Vlg1jnaFkuQRAP-VrHlNG901h_D9Y8Es1aOtlf03v9IHpkVHcL6b7OYM4L-mQhP5bJBxkQUTCr__mDUIoVkr6JIjky3OrtR9DJAg9Lv3DyrNX074tYwx2mP1ph87-l6jiRIo5o4pV8yj0tHtxf0y2YlxcB8_E_RrcEECSr0tjrZd56MqEiyXpzmWzfkMMPs1hN6gQ0oPgOMKERIn2_93Abk8qYl3L8EAPlHzelWWW3N79jZTRWAh1BJtOvhkeDZ5GT2YbE4ZOkxSBQl0pa7c1kYEtS_AliDIRT3G06sUEMLhaT_amNGl1Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سعید برند، دبیر ستاد رسانه‌ای تشییع رهبر انقلاب در هلدینگ خبرفوری شد
🔹
طی حکمی، سعید برند به عنوان دبیر ستاد رسانه‌ای تشییع رهبر انقلاب در هلدینگ خبرفوری منصوب شد. وی مسئولیت هماهنگی، راهبری و مدیریت فعالیت‌های رسانه‌ای این هلدینگ در پوشش مراسم و برنامه‌های مرتبط را بر عهده خواهد داشت.
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/661772" target="_blank">📅 15:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661771">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/607a870e5c.mp4?token=JyX6uhjKfREdNEgO3HdSHdvo-32dxp-1ucK5mRPF2vn0PBsvAC0K9tIAJl8wN79bn0bNN7YnI-4vVGQCdyIOEus4YZaHHoGTdhWPgltukBo5-nlhc26X0-U-1VR54rB7yh7_mFA0BQOITz8oIurSv7ADsRRdSSd0WqBBgXBG4IYGAs2uAYWzPKBIqKjKGBCM2vpX3RNKu5IR5Z1I0neq7LK0tFzZnQajIsk7mrWMRv8OsE_CwCJfrA7XOkSqfZEvd4A3J5F0GcRLGluzQxPOuH24iGBgkKZtr1EP6NsAoz42l2arCD30tZ7XOIWs4pj__-NSGPxdml4fsQqw7Nyimg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/607a870e5c.mp4?token=JyX6uhjKfREdNEgO3HdSHdvo-32dxp-1ucK5mRPF2vn0PBsvAC0K9tIAJl8wN79bn0bNN7YnI-4vVGQCdyIOEus4YZaHHoGTdhWPgltukBo5-nlhc26X0-U-1VR54rB7yh7_mFA0BQOITz8oIurSv7ADsRRdSSd0WqBBgXBG4IYGAs2uAYWzPKBIqKjKGBCM2vpX3RNKu5IR5Z1I0neq7LK0tFzZnQajIsk7mrWMRv8OsE_CwCJfrA7XOkSqfZEvd4A3J5F0GcRLGluzQxPOuH24iGBgkKZtr1EP6NsAoz42l2arCD30tZ7XOIWs4pj__-NSGPxdml4fsQqw7Nyimg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از شهدای میناب که قالیباف لحظاتی قبل در صفحهٔ خود منتشر کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/661771" target="_blank">📅 15:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661770">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
دیدار شهباز شریف نخست وزیر و عاصم منیر فرمانده ارتش پاکستان با محمدباقر قالیباف رئیس هیئت ایرانی میناب ۱۶۸ - زوریخ سوئیس
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661770" target="_blank">📅 15:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661769">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81bb35deb.mp4?token=QvSXawXL10actVB4AXbROWO2J0RE4Z7Hqdwz1pIHprTjm31KBxcF9-_P8Emg6sXU48hXz8R-hLgKRxQvN50TXG7XVMdolfDFobpZ-ngShzJewM_1ycEo1YndCU9O6GhPtZ9jMLN-HdNk2tF7bZmjq8FtcDfWcvAIfSjDrH35BJmlq6jdxFjfaQ17i_SWGHTzdNo2XFEoGPOZPl8RJFlcp-FVc_kcJz-WKoeAYQ1xQ6ZjPJZQ6-NtOJe9wqXVDZiTynWlUZ5RZZHvEEYpahhn-0T_vlP7WrBe_-uu_bZa9rTLE8cG5ufhvBtey_gAKmtNJvdnUsubHk702Q1z3-gKdDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81bb35deb.mp4?token=QvSXawXL10actVB4AXbROWO2J0RE4Z7Hqdwz1pIHprTjm31KBxcF9-_P8Emg6sXU48hXz8R-hLgKRxQvN50TXG7XVMdolfDFobpZ-ngShzJewM_1ycEo1YndCU9O6GhPtZ9jMLN-HdNk2tF7bZmjq8FtcDfWcvAIfSjDrH35BJmlq6jdxFjfaQ17i_SWGHTzdNo2XFEoGPOZPl8RJFlcp-FVc_kcJz-WKoeAYQ1xQ6ZjPJZQ6-NtOJe9wqXVDZiTynWlUZ5RZZHvEEYpahhn-0T_vlP7WrBe_-uu_bZa9rTLE8cG5ufhvBtey_gAKmtNJvdnUsubHk702Q1z3-gKdDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کشتی کانتیری با گذشتن از محاصره دریایی حامل کالاهای اساسی در حال تخلیه در بندر شهید رجایی است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661769" target="_blank">📅 15:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661768">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 شما این روزها بیشتر از کدام ابزار هوش مصنوعی استفاده می‌کنید؟</h4>
<ul>
<li>✓ چت‌جی‌پی‌تی (ChatGPT)</li>
<li>✓ کلاد (Claude)</li>
<li>✓ جمینای (Gemini)</li>
<li>✓ دیپ‌سیک (DeepSeek)</li>
<li>✓ گراک (Grok)</li>
<li>✓ میدجرنی (Midjourney)</li>
<li>✓ سایر ابزارها</li>
<li>✓ استفاده خاصی ندارم</li>
</ul>
</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661768" target="_blank">📅 15:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661767">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
علت عدم واریز حقوق برخی از بازنشستگان کشوری در خرداد ۱۴۰۵ اعلام شد
🔹
به دلیل بروز اختلال در سامانه پیامکی بانک عامل، ممکن است پیامک واریز حقوق برای بخشی از بازنشستگان و وظیفه‌بگیران ارسال نشده باشد؛ بنابراین عدم دریافت پیامک لزوماً به معنای عدم واریز حقوق نیست و مشمولان می‌توانند از طریق درگاه‌های بانکی نسبت به بررسی موجودی حساب خود اقدام کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/661767" target="_blank">📅 14:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661766">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
انهدام مهمات عمل نکرده دشمن در بندرعباس
روابط عمومی سپاه امام سجاد (ع) :
🔹
دوشنبه اول تیر ماه از ساعت ۸ صبح تا ۱۱ ظهر در برخی مناطق حومه بندرعباس (سرخون وایسین) عملیات انهدام مهمات جنگ رمضان با حضور تیم تخصصی چک وخنثی اجرا می‌شود.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/661766" target="_blank">📅 14:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661765">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPkMPiib8MO9HuclYiuS1oe1XpmQMz8wNLb8nfue9ah068Rh9PgjXftTiHx9AkSg7UBrHEgs8t2oScB8BaVjJWOFDJBjPA4wlTlbe-pajLnCF5iMbXSozi2cj7sY968SusQEV1ms1L8GRIhcfYlbYz4mIP_0SGu2QR61S6iDTqKDu9nxn8p8AEUHyWh2ebOlyW5ZHS_T1LQIQBRqXcK0XMKCg_NEDOdt8FGNX6B56wZkkhmSBBuTVZRFK7TShky68kFuxholR57GUr08WeNw_PfgOomckLd7rvTfdWr6AD6j_HQzNUaIiWf9Pa8wVxT4pUCcypu5YE3Mu8mdEZgi2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیدار شهباز شریف نخست وزیر و عاصم منیر فرمانده ارتش پاکستان با محمدباقر قالیباف رئیس هیئت ایرانی میناب ۱۶۸ - زوریخ سوئیس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/661765" target="_blank">📅 14:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661763">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
قطر آغاز نشست سران در سوئیس را اعلام کرد
وزارت امور خارجه قطر:
🔹
نشست سران در سوئیس آغاز شده است. نخستین دیدار میان واشنگتن و تهران با حضور دو کشور میانجی، یعنی قطر و پاکستان، در این نشست برگزار می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661763" target="_blank">📅 14:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661762">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
منبع نزدیک به تیم مذاکره‌کننده: تنگه هرمز بدون مهار اسرائیل در لبنان باز نخواهد شد
🔹
رفع محاصره دریایی برای بازگشایی تنگه هرمز کافی نیست
🔹
همچنانکه در بند ۱۳ به صراحت آمده، عدم اجرای تعهد آمریکا در بند یک، به معنای عدم اجرای بند ۵ نیز هست و این بدان معنی است که تنگه هرمز باز نخواهد شد.
🔹
اجرای بند یک درباره جنگ در تمام جبهه‌ها از جمله لبنان، رفع کامل محاصره و صدور اسقاطیه‌های فروش نفت، پتروشیمی و مشتقات ایران، شرط بازگشایی تنگه هرمز است./ تسنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/661762" target="_blank">📅 14:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661761">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
خبرنگار صداو سیما: یک دور رفت و برگشت پیام با واسطه پاکستان بین دو‌طرف انجام شده و یک دیدار هم با هیئت قطری برگزار شده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/661761" target="_blank">📅 14:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661760">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
خبرنگار صداو سیما: یک دور رفت و برگشت پیام با واسطه پاکستان بین دو‌طرف انجام شده و یک دیدار هم با هیئت قطری برگزار شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/661760" target="_blank">📅 14:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661759">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnapp | اسنپ</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbCNquslmFk5ZQtFfHeX2nFpqpW2wbVFJMrDV1H7yh-dcdNJ1n4cf91AKMme7GXRu1bOiBB2vjEVXBy8iNv0mnzTYhTBzxcsS0-kbnIH_Kf2iE1tLKIpFUbE_yy_GLzpPtTT1pfD3oZXTACTBZ40679nllagf3Fl16xxx5VhvDiUOyCE4qyEi48juuU3Mn_1a3zk-IwI_escbIw9T_ipL88Zz8r-0saQQ35cbtE969NZH8zjuYBip6AjSKGByoK3UJbuqW7QOW-9-X6D-_gxUq_gwqYHpZuENHG3p7Qh-FtqVSR4xmYUQhtG53BWTAF39bQIcZVGZ5hFHawXlGpm6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥳
چیزی به شروع بازی
ایران - بلژیک
نمونده.
🇮🇷
⚽️
🇧🇪
⭐️
با پیش‌بینی این بازی، هم
۲ برابر امتیاز
می‌گیری و هم وارد قرعه‌کشی
iPhone 17
می‌شی.
📱
‌
🔥
با جمع کردن امتیاز این بازی، یک قدم به برنده شدن موتور، توپ طلا، PS5، iPhone17  و ده‌ها جایزه‌ی هیجان‌انگیز دیگه نزدیک‌تر شو.
🛵
📱
🎮
‌
فرصت رو از دست نده و همین حالا پیش‌بینیت رو ثبت کن
👇
🔗
روی «
لینک
» بزن!
@Snappofficial
🏆</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661759" target="_blank">📅 14:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661758">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
وزیر اقتصاد: قرار است رقم کالابرگ افزایش پیدا کند اما فقط برای ۶ دهک پایین جامعه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/661758" target="_blank">📅 14:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661757">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
مذاکرات ایران و قطر در سوئیس در مورد آزادسازی اموال و سرمایه‌گذاری ۳۰۰ میلیارد دلاری
🔹
دستور کار دیدار ایران با هیئت قطری در کنار اجرای کامل بند ۱ تفاهم، پیگیری اجرای بند ۶  و ۱۱ تفاهم یعنی سرمایه‌گذاری ۳۰۰ میلیارد دلاری و آزادسازی اموال بلوکه شده ایران است به نحوی که
۱۲ میلیارد دلار آن با فوریت در دسترس قرارگیرد
.
🔹
قطری‌ها در این نشست در سطح نخست وزیر حضور یافته‌اند که نشان دهنده پیگیری سطح بالای آزادسازی اموال بلوکه شده است./ جماران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/661757" target="_blank">📅 14:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661756">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
هیئت ایرانی شرکت کننده در مذاکرات ‎سوئیس دیداری با ‎گروسی نخواهد داشت
🔹
رافائل گروسی که به سوییس سفر کرده است صبح امروز با وزیر امور خارجه سوئیس در بویگن‌اشتوک دیدار کرد ولی هیات ایرانی حاضر در این نشست برنامه ای برای دیدار گروسی ندارد .
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/661756" target="_blank">📅 14:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661755">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
هنوز ۶۰ قطعه از پیکر دانش‌آموزان شهید میناب خاکسپاری نشده است
رئیس دادگستری هرمزگان:
🔹
هنوز ۶۰ قطعه از پیکر شهدای دانش‌آموز میناب که در تفحص‌ها از محیط مدرسه و فضای پیرامون یافت شده، خاکسپاری نشده و باید شناسایی از طریق آزمایش دی‌ان‌ای روی آن‌ها انجام شود.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/661755" target="_blank">📅 14:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661754">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d513861ce4.mp4?token=UaagAm5NroixkOHJmgrj7IpUiO5F_tZVw4GM1gtD_sZvfuxEQNsiXh_Ul9DMOlNJ9dH0MqXz3zHIe7IG8DnO30x25E69uVrOtMdRNVELVxUQ1IQ5jvIw5kYiYNfcpoT_u13gJnLkMhNR0wLIczD40UHjTsoMWEkXziymw2Civ_O_pBqITVFj2xdM9yPvSOC5aQqdlTAKzManIIhK4UhXJykaqm1i_20lUEexdjbcJa_W4r3NC94UDJBouLtgSDQLfMq4o03P3vVo6tsF0BnHW1TcyqJ-9mAIhk8Ns-DfgD5DnlEOzqeSJlfwFjDyFMAQ5SnLTP0bBYjIDn54FoGhKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d513861ce4.mp4?token=UaagAm5NroixkOHJmgrj7IpUiO5F_tZVw4GM1gtD_sZvfuxEQNsiXh_Ul9DMOlNJ9dH0MqXz3zHIe7IG8DnO30x25E69uVrOtMdRNVELVxUQ1IQ5jvIw5kYiYNfcpoT_u13gJnLkMhNR0wLIczD40UHjTsoMWEkXziymw2Civ_O_pBqITVFj2xdM9yPvSOC5aQqdlTAKzManIIhK4UhXJykaqm1i_20lUEexdjbcJa_W4r3NC94UDJBouLtgSDQLfMq4o03P3vVo6tsF0BnHW1TcyqJ-9mAIhk8Ns-DfgD5DnlEOzqeSJlfwFjDyFMAQ5SnLTP0bBYjIDn54FoGhKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دانشجوی ۱۹ ساله‌ای که با ۲۰ دلار، ۵۵۰ هزار دلار درآمد کسب کرد
🔹
دانشجوی ۱۹ ساله چینی با کمک Claude، تنها با ۲۰ دلار و در یک ماه، رادار هوشمند ساخت؛ سیستمی که سرعت خودرو را تشخیص می‌دهد، ویدیو ثبت می‌کند، پلاک را می‌خواند و جریمه را خودکار ارسال می‌کند.
او این ایده را به دولت هنگ‌کنگ ارائه داد و با قرارداد ۵۵۰ هزار دلاری بیرون آمد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/661754" target="_blank">📅 14:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661753">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ریزش ۳۴ هزار واحدی شاخص بورس
🔹
تخفیف ۲۰ درصدی قبوض آب برای مشترکان کم‌مصرف
🔹
تشکیل ۴هزار پرونده اغتشاشات دی ماه در اصفهان
🔹
رسانه‌های عبری: نتانیاهو به باری سنگین برای اسرائیل تبدیل شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/661753" target="_blank">📅 14:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661752">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
پزشکیان: چرا مردم به خرید طلا و ارز روی می‌آورند؟ به این دلیل که پول خود را در بانک می‌گذارند، اما پولی که ۶ ماه یا یک سال بعد دریافت می‌کنند، دیگر همان ارزش گذشته را ندارد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/661752" target="_blank">📅 14:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661751">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
پزشکیان: ادامه جنگ به نفع هیچ فرد یا گروهی نیست
🔹
بر اساس همه تحقیقاتی که در جهان انجام شده است، هر جنگی موجب اختلال در رشد، توسعه اقتصادی و اجتماعی و افزایش فقر و بیکاری می‌شود.
🔹
این سخن به معنای ترس از جنگ نیست. ارتش، سپاه، نیروهای هوافضا و مردم ما نشان دادند که با قدرت در برابر تجاوز ایستادگی می‌کنند و اگر جنگ ادامه پیدا می‌کرد، با قدرت مقاومت می‌کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/661751" target="_blank">📅 14:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661750">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
پزشکیان: صدا و سیما نیز باید ملاحظات لازم را رعایت کند و مراقب باشد اجازه داده نشود تلاش‌هایی که در حال انجام است، با طرح مطالب یا حضور در تریبون‌ها خدشه‌دار شود
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/661750" target="_blank">📅 14:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661749">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌ویکم از فصل چهارم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای باقر حسین‌زاده که به وجود خداوند بی‌اعتقاد بوده و به خاطر اعتیاد و در حال مصرف مواد به ناگاه روح از جسم به طور سخت و وحشتناکی جدا و در آتش برزخ می‌سوزد و خاکستر شدن تمام سلول‌های بدن را درک می‌کند و با التماس به درگاه خداوند و ارادت قلبی به امام حسین(ع) در طول زندگی توسط اشاره‌ای از جانب اهل بیت به جسم باز می‌گردد را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: باقر حسین‌زاده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/661749" target="_blank">📅 14:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661748">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e342b75637.mp4?token=A_syqA5qxRyIVuQ2RqR3TGzZTJkuBStubkSuEKHjMUtiPr7qnL1G7w9LrMgsa8EKhK8clQfD90OWkAGL4ZMxYFA2T2-OGJPHBEd2_XRxwz53y83-kRkOuc7z6A1_xghTOdi2Jyn3P36O2wamzlxevK5KMlLsQNGk2ZkqyGBkwOkA34XkFsWPcGI12jcVu8gLUNQc8-MTs6ytQf2NKNOTV4l8Jc_2A9pj0HL-1ZPdBVR9rvfnTi6PPL_KlwWoBjabPTq_tWpo1JDN622O2IGWGxWEvQ18YzBPE7JHb8mx9PYadQvnP6vDzjSEECnN4HL0-qwWjNi-6KVS8dXCtrMqJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e342b75637.mp4?token=A_syqA5qxRyIVuQ2RqR3TGzZTJkuBStubkSuEKHjMUtiPr7qnL1G7w9LrMgsa8EKhK8clQfD90OWkAGL4ZMxYFA2T2-OGJPHBEd2_XRxwz53y83-kRkOuc7z6A1_xghTOdi2Jyn3P36O2wamzlxevK5KMlLsQNGk2ZkqyGBkwOkA34XkFsWPcGI12jcVu8gLUNQc8-MTs6ytQf2NKNOTV4l8Jc_2A9pj0HL-1ZPdBVR9rvfnTi6PPL_KlwWoBjabPTq_tWpo1JDN622O2IGWGxWEvQ18YzBPE7JHb8mx9PYadQvnP6vDzjSEECnN4HL0-qwWjNi-6KVS8dXCtrMqJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهباز شریف نخست وزیر پاکستان با ونس معاون رییس جمهور امریکا، در حضور کوشنر، ویتکوف و فرمانده ارتش پاکستان دیدار کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/661748" target="_blank">📅 14:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661747">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSY69YjRktOubaKeA1HD7z2DJGUZhyn_aejW4EQ-35DidiXWP0xi3O8hHzZVrENpWmnW54yvDMYq4gDbdfiKfIOFYQAg0nUFkZFRh1ftyFN24u2wkYpzLBs9FN_H4iHnsoUjhZc4Cgr1TmxQL63hv58uiJs4CmnGVC5SPgA8EC1g3fceIArfeKQcMp67GT-Gk_lIiEPLlHWCNgJ7WQeakxBujCnjml_jER_KNJS3sp0KSiY1D2ZKnP3g4qpEqwaboTr0-I43o38QRcN1tgbxanV1ZFobNWD02KKEsLYAq2rAZ78p02rmNnRQc2z7TYl9str2MbCNKpDay-DrAnQQ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۳۱ خرداد ۱۴۰۵؛ ساعت ۱۳:۰۵
🔹
قیمت دلار امروز با کاهش ۲ هزار تومانی نسبت به روز گذشته به ۱۵۹ هزار تومان رسید؛ در حالی که این ارز روز قبل در سطح ۱۶۱ هزار تومان بسته شده بود.
🔹
کاهش قیمت دلار همزمان با سفر هیات ایرانی به سوئیس برای مذاکره با مقامات آمریکایی رخ داد و امیدواری‌ها نسبت به پیشرفت گفت‌وگوها را افزایش داد.
🔹
در همین حال آتش‌بس در لبنان نیز تا حدی از تنش‌های منطقه‌ای کاسته و فضای روانی بازار ارز را کاهشی کرده است.
🔹
با این حال، به دلیل تردید معامله‌گران نسبت به نتیجه مذاکرات، افت قیمت‌ها محدود مانده و یورو نیز با کاهش هزار تومانی به ۱۸۵ هزار تومان رسیده است./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/661747" target="_blank">📅 14:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661746">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhsYiY0u1t3QxabZKtH9ULHTsQzaXSV5pD3q_wFjxIHDYH_HkRtRylVvn50oBYBYzWGMXjcJyFfFvSFuA-2GMDW31cfkBiW8o5BMUX9ntx-YuMaNnnHxREaPZ7Xhl2Aps-_4xboeflWLAFei4keiZlGflCXfoxYL7S6GQuJn5orVEvw59NNc6MB3pw6N2dSHVtUh7JsVusB5mkXlMWXm0ZPEIgwHzwS0lTDYPUeNhvCvCRZsvUGCIzQ8CmixK0gSiTpsBdkulKg99i73_yhqfM8bOVy4GRzUAU1f3JR2ZHgrTX7h_9ffktTyhkw9ZdWwagYFUcbSqWVs3p5r5c-mzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«تورم» رو زیاد شنیدیم، ولی دقیقاً یعنی چی؟
🔹
هر روز یک واژه برای فهم بهتر جهان #واژه_کاوی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/661746" target="_blank">📅 14:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661745">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b12443b818.mp4?token=IUwGFonb6SP7pHbcYvlkcwm8hCPvSIAey3zYi0i641RwnilawPNzcozgSGy2on1wH9y7JyK-XJ97XvsgJiqiv6Hrkd1wJI-5JZMX3WhZggkTP77CIkkWWOkDd6yLAgs7iR2th3NJSaIi9I5oZouu6yuIe_AJ53iHrab4AJT4Ces8O1tZBY8ClMcSYpJxnAOAEfd5QucWusgEjo8Dw_18uLVeJ7ANhLZzGPxnLFEi_7OBK0qvLxbgVTTOUoJoNYrSahs36MsM3PPynP7_zRMLiscmGgdhYlI7m636B4FVxxPE2ZLfC31dbuuoDyBj2fncpuiEv2cbrUE-X-fHoD51cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b12443b818.mp4?token=IUwGFonb6SP7pHbcYvlkcwm8hCPvSIAey3zYi0i641RwnilawPNzcozgSGy2on1wH9y7JyK-XJ97XvsgJiqiv6Hrkd1wJI-5JZMX3WhZggkTP77CIkkWWOkDd6yLAgs7iR2th3NJSaIi9I5oZouu6yuIe_AJ53iHrab4AJT4Ces8O1tZBY8ClMcSYpJxnAOAEfd5QucWusgEjo8Dw_18uLVeJ7ANhLZzGPxnLFEi_7OBK0qvLxbgVTTOUoJoNYrSahs36MsM3PPynP7_zRMLiscmGgdhYlI7m636B4FVxxPE2ZLfC31dbuuoDyBj2fncpuiEv2cbrUE-X-fHoD51cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تماس تلفنی، دعای خیر و آرزوی موفقیت خانواده شهید میکائیل میردورقی از شهدای دانش آموز مدرسه شجره طیبه برای قالیباف رئیس تیم مذاکره کننده ایرانی در ژنو
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/661745" target="_blank">📅 14:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661744">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
زمان مصاحبه‌های دکتری ۱۴۰۵ به هفته پایانی تیرماه موکول شد
سازمان سنجش:
🔹
به‌منظور فراهم شدن زمینه حضور متقاضیان در آیین وداع و تشییع رهبر شهید انقلاب، زمان مصاحبه داوطلبانی که پیش‌تر برای بازه زمانی ۱۳ تا ۱۷ تیر برنامه‌ریزی شده بود، به هفته بعد و در فاصله ۲۰ تا ۲۴ تیر منتقل شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/661744" target="_blank">📅 13:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661743">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0-N_M4-dmmXstowERLBT2W4feedNtOoJpOUL_AJYMxNtGUC6seJ7tAHHHjVUKmP6rV83WUAB7yGYd-U-g9im0JArNieingyrYURMoV8w7WZNG12S8I653zdipsz9DmY4ozF8PBHitqcisSBByBJ0xjAvh--aN4cyMJENUiTKGOxFJXbko3zh_unGb2fwlSlpbJ301-cfUruXtAp6y2DVr5prH8dT8-eIP66EpcGjdldvORfxd9yHGdQytcUs04EtYPmSxgATqc1sQScQRcYHwNQvWwIA7C1KP6e0Tcsogud020JCayUtsfcj1VlcrmCe8DpLpzF0sXoVwWT-32jCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام ایگنازیو کاسیس وزیر امور خارجه سوئیس پس از دیدار با عراقچی
🔹
جناب عراقچی به سوئیس خوش آمدید.
🔹
در نشست دریاچه لوسرن، ما چارچوبی برای گفت‌وگو و تبادل نظر فراهم می‌کنیم.
🔹
در شرایطی دشوار و پیچیده، رابطه مبتنی بر اعتماد میان سوئیس و ایران، همچنان در خدمت دیپلماسی و در راستای صلح و امنیت در خاورمیانه قرار دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/661743" target="_blank">📅 13:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661742">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
پزشکیان: در شورای‌عالی امنیت ملی تقریباً همه اعضا متفق بودند که این اتفاق باید رخ دهد و تنها یک نفر نظر متفاوت داشت که وجود یک نظر مخالف در یک مجموعه نیز ایرادی ندارد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/661742" target="_blank">📅 13:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661741">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
پزشکیان:هر پیامی که بوی تفرقه و اختلاف بدهد، در جهت راهبردهایی است که نتانیاهو و سازمان سیا دنبال می‌کنند
🔹
اگر قرار باشد بر اساس نیت‌ها و سخنان گروهی در کشور شقاق ایجاد کنیم، دیگر نیازی به اسرائیل و آمریکا نخواهد بود و خودمان کشور را نابود خواهیم کرد.
📲
🇮🇷
…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/661741" target="_blank">📅 13:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661740">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
پزشکیان: قاعده تغییر کرده است
🔹
پیش از این می‌گفتند باید درباره موشک‌های ایران نیز مذاکره شود؛ اما اکنون می‌گویند همان‌گونه که کشورهای دیگر موشک دارند، ایران نیز باید موشک بالستیک داشته باشد.
🔹
اگر طرح‌ها و راهبردهایی را که نتانیاهو و سازمان سیا تدوین می‌کنند،…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/661740" target="_blank">📅 13:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661739">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
پزشکیان: در همین مدت کوتاه توانستیم بخشی از اعتبارات و منابع خود را بازگردانیم و اقدامات متعددی انجام دهیم
🔹
برخی موضوعات پیش از این، مورد تفاهم قرار گرفته بود و در همان چارچوب پیگیری خواهد شد؛ اما از حق غنی‌سازی خود صرف‌نظر نخواهیم کرد و طرف مقابل نیز ناچار…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/661739" target="_blank">📅 13:49 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

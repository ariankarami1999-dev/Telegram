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
<img src="https://cdn4.telesco.pe/file/O1Pr5_Mi2_gIV_f_6QVQGagTiV3XtIV7Sn-7hMkatfTMScX28YRRw5Z0Z1VXqFSfBWQPtr0LaUSB1kK_xPkpI4DjCCLTD9MKQm9jVQkOxDKvhydOu29PHAIEznjUZqMLF9Iqotyv7rnMHLTt-_8t-no7IrpjBE12MAHCQqRQnUvNaNSaGRsBCvbqt65-9YQXozgqEheTVyk6i7i3f3m8-zatXoRGU9AROMd5AyDv8CyA0-5tE2tGmfAbl8X_jPU2CHpbQ5-V-NSZJ3H1lR46VqG9xYK0hyKM_OhZVOku9fLhr8nqSrsY4RZks0nCVpWlkK23fDieNa6UoNHDQh-PHw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.48M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 21:11:13</div>
<hr>

<div class="tg-post" id="msg-660918">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✉️
متن کامل رهبر انقلاب اسلامی خطاب به ملت ایران درباره تفاهم‌نامه رئیس‌جمهوران ایران و امریکا
✏️
بسم‌ الله‌ الرّحمن ‌الرّحیم
🔸
ملّت پرشور و باوفای ایران
💬
همانگونه که مطلع شُدید، تفاهم‌نامه‌ای بین رئیس‌جمهوران ایران و امریکا امضا شد. در مسیر رسیدن به این…</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/660918" target="_blank">📅 21:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660917">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خبرفوری
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/660917" target="_blank">📅 21:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660915">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jL0COiMZyQzaOLe6bH-f4XSe0NdjCLTnFVXLc2B6f9AWdDu8n9MZVtBQdd0nKctbG3yAY66CRFBKl6RfoKFrFXoiO0rxT6mWwci06Xv4OzEc8KP99sSqmmT05B6U1PZ75KMHJQzm4dmYTdMVmTh0X03U9t2TGXZb-ztdTbc_2qceBhl40k918-JupB7fqcyn5g_z4IsGbpQ8IRCIioLVnIOtBFuLkeOnfL3JSfeeXA-6W_7eO24w8ycXSrG-GMp9-xQ_HZlqVUxVsQbsN38NK6aWiyF4eM7Ju3dSdCMUpODor9leu2rLW5zWuXs4YpnUilqsOJAFJyvZcSEYMGV0bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✉️
متن کامل رهبر انقلاب اسلامی خطاب به ملت ایران درباره تفاهم‌نامه رئیس‌جمهوران ایران و امریکا
✏️
بسم‌ الله‌ الرّحمن ‌الرّحیم
🔸
ملّت پرشور و باوفای ایران
💬
همانگونه که مطلع شُدید، تفاهم‌نامه‌ای بین رئیس‌جمهوران ایران و امریکا امضا شد. در مسیر رسیدن به این مرحله، مسئولین امر، از سر دلسوزی و با حُسن نظر، تلاش‌های زیادی را به‌عمل آوردند و البته این رئیس‌جمهور آمریکا بود که از روی استیصال، از انواع اهرم‌ها برای این امر استفاده می‌کرد.
💬
بنده علی‌الاصول، نظر دیگری داشتم ولی از باب تعهّدی که رئیس‌جمهور محترم به‌عنوان رئیس شورای عالی امنیّت ملّی از طرف خود و سایر اعضا در پاسداشت حقوق ملّت ایران و جبهه مقاومت به بنده دادند و تصریح به قبول مسئولیت آن نمودند، اجازه‌ی آن را صادر نمودم‌. ایشان همچنین تصریح کرده‌اند که اگر طرف آمریکایی بخواهد زیاده‌خواهی کند زیر بار آن نخواهند رفت. از این لحظه، ما یعنی شما ملت سرافراز و این خادم ناچیز، منتظر تحقّق شروط گفته‌شده خواهیم بود. امّا بدیهی است مذاکرات حضوری که در آینده برقرار خواهد شد، به معنی پذیرش نظر دشمن نخواهد بود. امیدواریم که دعای خیر سرورمان عجّل‌الله‌تعالی‌فرجه‌الشّریف انواع نصرت‌ها و فتوحات، برای ملّت باشرف ایران به ارمغان آورد.
🔻
والسّلام علیکم و رحمة الله و برکاته
✍
سید مجتبی حسینی خامنه‌ای
🗓
۲۸/خرداد/۱۴۰۵
📲
@rahbar_enghelab_ir</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/akhbarefori/660915" target="_blank">📅 21:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660914">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ر
هبر انقلاب: ملت پرشور و باوفای ایران
همانگونه که مطلع شدید، تفاهم‌نامه‌ای بین روسای جمهور ایران و امریکا امضا شد. در مسیر رسیدن به این مرحله، مسئولین از سر دلسوزی و حسن نظر، تلاشهای زیادی کردند و البته این رئیس‌جمهور امریکا بود که از روی استیصال، از انواع اهرم‌ها برای این امر استفاده می‌کرد
.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/akhbarefori/660914" target="_blank">📅 21:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660913">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
تا دقایقی دیگر، پیام بسیار مهم رهبر معظم انقلاب درباره تفاهم پایان جنگ خطاب به ملت ایران منتشر خواهد شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/akhbarefori/660913" target="_blank">📅 20:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660912">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfpPHDUEGyQH2Ao_1z7fUuPNVJX4eSzGBRH_rjBhfBF8m7vFelIw1OSTfgCVNBBlNMAWBCxe1qMNgB_iIo6grsxe_ERFMdR7QzoaHq6W0R5GW_vFcRLRDEUN_xIl-GQqgi7hFaRzPZUYp0SncHDnZFEMAxH6ekBOzavstQjeIFLvqpEnQp-0dB8AuFRHIS0HEYgJMvei6dIZTFVuQCjG4Wl5cbz1O9sHK4PUVIIgWx7rlvsKK9yj6Pnq6GrTHcQagozn5VozQUOoOkDwaQjC3Rcdm_k70wftQJn45cwoW0KZ0fZExYTX09warXh9Bx0bf39tEIGxJguBQV1cQt4OQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مِثْلِي لا يُبَايِعُ مِثْلَهُ
رهبر شهید انقلاب:
🔹
اولین و بزرگترین درس محرّم این است که نشان داد که کسى در حدّ عظمتِ شخصیّتِ حسین‌‌بن‌‌على، فرزندانش را، زنان و دختران و ناموس الهى و حرم پیغمبر را، همه را برداشت آورد به قربانگاه.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/akhbarefori/660912" target="_blank">📅 20:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660911">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62f6989de6.mp4?token=vC_9Ybb4kq8VEgiDq8MO2c-hjMznB2v5dnnxUYoCfIYjMr0naW-eRJ-yFFqk5_DyDR8jY-Zd9umOJeoynBS-QJAHNLMQVkD9VcSDBOwamEuutRpUZIuA7D0RtW8-tqoG5xOlrmLUfqznBMVQCh9pQ6tinP5opCMeebPalWmYSlyFvhXf6bxVmLDvGjHbURDcmphH7ytl-jqqEjt931RQ9_fgHhKXzt6QTRbr9iBwjTPFu6D-NRv0K0Kc0qSae2c2unoBadD6b5i2ns8By-KioASgXG1Bfm1N18mQUQDjq4acJonagXfw3CfDwGCsPcUmDxmKVktlKGU4xXhlbwNF4W0Zk48k8ksSjJSXJe4YnLvtk7NfA9gUPNBsaxTXhkW0E-cpPiRuaJLiadFEmjvo8enCvSP-ODCxMeziO53s_3jn8Iw8nT0zB0R51W_55HRtfvLHz1dpTY-2w_EdTBjMAUfg-xeniHm9HaaTmWAqeo6Djjt-IRxeWG4puUR0z9f3Z5SPbQ5TkawfIHNh5uIDI5shP9RBvIpjGR0-8expx5kS_-Ett3YR0dUlCRsTcRT06kspOCjqlh6goL1yat3Lz60MuRMBGGYZ686yPcnU02AK9Vw-Zu5-QFKhHCTWVVeLvx0n44dL6CA_9OQ061pFNkx2hGWOwPyrXnKenPekF54" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62f6989de6.mp4?token=vC_9Ybb4kq8VEgiDq8MO2c-hjMznB2v5dnnxUYoCfIYjMr0naW-eRJ-yFFqk5_DyDR8jY-Zd9umOJeoynBS-QJAHNLMQVkD9VcSDBOwamEuutRpUZIuA7D0RtW8-tqoG5xOlrmLUfqznBMVQCh9pQ6tinP5opCMeebPalWmYSlyFvhXf6bxVmLDvGjHbURDcmphH7ytl-jqqEjt931RQ9_fgHhKXzt6QTRbr9iBwjTPFu6D-NRv0K0Kc0qSae2c2unoBadD6b5i2ns8By-KioASgXG1Bfm1N18mQUQDjq4acJonagXfw3CfDwGCsPcUmDxmKVktlKGU4xXhlbwNF4W0Zk48k8ksSjJSXJe4YnLvtk7NfA9gUPNBsaxTXhkW0E-cpPiRuaJLiadFEmjvo8enCvSP-ODCxMeziO53s_3jn8Iw8nT0zB0R51W_55HRtfvLHz1dpTY-2w_EdTBjMAUfg-xeniHm9HaaTmWAqeo6Djjt-IRxeWG4puUR0z9f3Z5SPbQ5TkawfIHNh5uIDI5shP9RBvIpjGR0-8expx5kS_-Ett3YR0dUlCRsTcRT06kspOCjqlh6goL1yat3Lz60MuRMBGGYZ686yPcnU02AK9Vw-Zu5-QFKhHCTWVVeLvx0n44dL6CA_9OQ061pFNkx2hGWOwPyrXnKenPekF54" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیگانگان واقعی‌اند؟ پاسخ مبهم ونس درباره یوفوها
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/akhbarefori/660911" target="_blank">📅 20:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660910">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله به ایران آماده شوند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/660910" target="_blank">📅 20:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660909">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
از کمای عمیق تا ارتباط با ارواح؛ تصادف هولناکی که مسیر زندگی دختر را تغییر داد
🔹
00:09:20 قطع امید کردن جامعه پزشکی از زنده ماندنم
🔹
00:26:30 عدم رعایت حجاب قبل از تجربه
🔹
00:34:00 رؤیت حضرت زینب در کما و پیام ایشان برای مادرم
🔹
00:40:00 مرد زیبارو با میوه‌های بهشتی
🔹
00:44:35 ارتباط عجیب و باور نکردنی با ارواح بعد از کما
🔹
00:49:00 روح دختر ژولیده و پریشان که درخواست کمک داشت
🔹
00:57:30 مادرم با توسل به امام حسین (ع)، از خداوند خواست که دیگر ارواح را نبینم
🔹
01:02:30 تبدیل خودخواهی به مهربانی بعد از تجربه
🔹
قسمت هفدهم (خودسوزی)، فصل چهارم
🔹
#تجربه‌گر
: راحله خمسه
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/660909" target="_blank">📅 20:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660908">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9OrR2XUS-unbwVOwpsPkZdpoy7jw6B2Cn_56rJrzpzGr0A1K5e8nzuQaQR6eNhNN3WvgH1nowBX_OWs0GU-djtGdqEiX71n7l3DlAQ-41ibeTS9C1DIeox3aNN4qau7HN7LDCwjpmK2hj8w6jB7wPI9qaKQKQqiL-iZLRy7VKqaBgH_UO7efaHwGHjO2T-kR8EkqmN3mHDMw3bJbtx2bsPPxGy9gnH5ZDR6O2IN9Hx-4ViolfGriZetVMeS9Fb6uOWF9C2d-e_RJh0NZfXVuZmDrSeuIZL77cxQDGim32Gvr8c4i1V_a80gtptlEXxtV5giZZsM_Ec27pM-DJoRaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سنت‌کام از لغو محاصره دریایی ایران خبر داد
فرماندهی مرکزی آمریکا:
🔹
نیروهای آمریکایی طبق دستور رئیس‌جمهور، محاصره دریایی ترددهای ورودی و خروجی از بنادر و مناطق ساحلی ایران را لغو کرده‌اند و دیگر مانع تردد کشتی‌ها در خلیج فارس و دریای عمان نمی‌شوند.
🔹
در این بیانیه همچنین آمده ناوهای جنگی آمریکا در منطقه باقی می‌مانند تا اجرای توافق را نظارت کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/660908" target="_blank">📅 20:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660907">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rO8ivenEgp01DtxSXcNVBvmapZW1dHtFdWYUZAb0ptjHVnYiBH-VvxYTnGUAZ2F-QgYgbOCP-1xnpr-iIhK2p74TEmJvwfjuL75LrOmc8-Ur-Ye1bDkOm0wx_J7LhJFmd2Hwlt3EoTnS51fWb__df11LQ7sUjMuoJw7a-U6e5W2B7-dZ05xnMpRf7Goiimf1nubsN26ZJJDTmMwk2M2Jj80xYQfv2t5829p6QMbdx3BnNnKOKSrdnEB1Q1JHo5uX9jt6YNJ3FARquazIesFVKXMD_6c5ysWn3XJhW1uF6LqCBbbGak76OfxaKaceOZqbNEvRzZKaSdAUa5BMUNTpGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شمارش معکوس برای حکم نهایی
🔹
بررسی‌های فضای بانکی کشور نشان می‌دهد که عملکرد آقای قربان اسکندری در دوره سرپرستی بانک صادرات ایران مورد توجه نهادهای بالادستی قرار گرفته است. کارشناسان، مدیریت ماه‌های اخیر بانک صادرات را یکی از عوامل تقویت جایگاه ایشان برای تصدی مسئولیت دائمی این بانک ارزیابی می‌کنند.
🔹
بر همین اساس، پیش‌بینی می‌شود معرفی آقای قربان اسکندری به‌عنوان مدیرعامل بانک صادرات ایران قطعی شده و در صورت نهایی‌شدن تصمیم مراجع ذی‌صلاح، حکم مدیرعاملی ایشان در آینده نزدیک صادر و ابلاغ شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/660907" target="_blank">📅 20:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660906">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KY9D1jS1jGuygrmW5zWEkkkVE--sF3dtWJ1GzzPoeVaeYN3BvhDbzb2qlmbelJjk_9ax3vj-pBoguuV40IATSP4wFpsqY6xvhZfvfSBo701sBroXzOW3MNwye5a5MdrIz7--_LLcjb-T3v1u1sa3q2UiBgbMXodLwd6UAyYWoK4aLF7Yos8QbDOdnMFFd9ImNzllYgrIaRDPqYrsFcJeM7RmjxBue9LKf0WIFiV0oZWZhviqu0YzxIiWCvVFV8YMuRKCDW_HkAvbgy_l9T2HL0j5dYvIWwJiHh6XysOVX_V7FLZJofPNbhEJ_o2nnVUgbL38uHJOosrz2lTNY7u73Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ قمارباز: هیچ پرداخت ۳۰۰ میلیارد دلاری از سوی آمریکا به ایران وجود ندارد و این خبر دروغ است
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/660906" target="_blank">📅 20:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660905">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
تحریم‌های خصمانه آمریکا علیه حزب‌الله
🔹
وزارت خزانه داری آمریکا در راستای حمایت مستمر از جنایات وحشیانه و ضد بشری رژیم صهیونیستی، تحریمهای جدیدی را علیه حزب الله لبنان به سبب حمایت از مردم لبنان در برابر جنایات اشغالگران تحریم کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/660905" target="_blank">📅 20:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660904">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNhF4cnrilNEfnlgcat9jM36T0dvtakaLkfdd4a0qxHC7Ia_E_-em68RtvcgmgepDQenISOPonlrdzy4iHsgOGHU8i8pC8zUIaI836ocyeiXabC5DUjhoqIm_nWEt8f8PuhWibq_GZXACXa9n9qGeUSjbnLpPYd-lP7OfVzqX_QQJlExEec49FxDWK9pLtu_HxH70NAYGZ5IpLUosy1uBPfxSo34He7ewKtd5Ffua9-q0Q3hCfKmmMODR-EM6ujaZCxROxsEwyYR_1WmuhluN3LCfZea7KF5CGNQvyqzzEJqX_FYBzhV_NTILtGCLCTXAZSkZQyoYxLOCkCb2KPFVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طبیعت زیبای ترکمن صحرا، گلستان
🇮🇷
#ایران_زیبا
#اخبار_گلستان
در فضای مجازی
👇
@akhbaregolestan</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/660904" target="_blank">📅 20:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660903">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2tJHrKiBBm6qsQURfHSYcM8L5hT-rAMogovOIsvMIp5fkfIFvZAgZanh3ymDqJeAKF7NqnbhE8zqkuCrUI93DQmRDwOujlFgx8BCw2QTw_YsynymdmyexUDMJ0uJNC4cz-otpl2S_uNjE2EnhzydcfTC1jl8p5RtO-633UtYUc1rz4hgpA-z8N5XOBUB2S_4lwIOVTqmqfz9AReU-Q9TMe_G3CN874koPwbroWYD_FYq2I_DNHf12oXkJFliXJAaEjnD5dmntql6cgdMkY3u2b-Du6tMt1mYoQQGgjCf0xw1FPx3uGivQErPE2yC6lbzCb6E4XlSffzDeIAARVOUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/660903" target="_blank">📅 20:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660902">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYmaug7pPYXfB3SyEEvG7wc1LmXWDHULNxwBqigw-voJKc7tbqpJPgnojb4qTWYg4HaGqFp41n6H6GLaGjVCGE1A0pTBL3MdNPcwEQpoYcbpPFUUXN0JWB8bjtfdWUafEr_UFI84uudYNlbIbbar4UNQODUDfAa1NWiGiG9SG9gG8LNqJj_q4EwR5tCarlMVrcsJnhDxJdQlTEd0tCpMUTyhrNr2-PF3EI6oWiS56fB8p4ga-Vit0OT-ctkJURjcvYshWkpbjo-oB1WiQXKNylDIACCnktdOWjyhrNWxSi0QeqSpAzUjUYyZw7y3qUNMvAM5Drqcmg-FHz-tIVBjeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه جدیدی از دارایی‌های بلوکه شده ایران در دنیا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/660902" target="_blank">📅 20:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660901">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
نرخ دیه سال ۱۴۰۵ اعلام شد
🔹
بر اساس این بخشنامه که در اجرای ماده ۵۴۹ قانون مجازات اسلامی مصوب سال ۱۳۹۲ و پس از انجام بررسی‌های لازم صادر شده است، مبلغ دیه کامل از ابتدای سال ۱۴۰۵ در ماه‌های غیرحرام، ۲۱ میلیارد ریال تعیین شده است.
🔹
این بخشنامه از سوی رئیس قوه قضائیه به مراجع قضایی سراسر کشور ابلاغ شده و از ابتدای سال ۱۴۰۵ ملاک محاسبه دیه خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/660901" target="_blank">📅 20:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660900">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
تا ساعتی دیگر، پیام حضرت آیت‌الله سیدمجتبی خامنه‌ای، رهبر انقلاب اسلامی خطاب به ملت ایران درباره تفاهم‌نامه رؤسای جمهوری ایران و امریکا منتشر خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/660900" target="_blank">📅 19:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660898">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd31f766ad.mp4?token=pY5gCaBzMLEZ71Y2LAgfS5VuqX7s2MqaxLZWcZ5p2f1Q-lCWLKkyj8uJI311AUF1_Z5nQytG9EICTc4FWqmgRc9JDH-3T_ZbQsnnlMlJxQNvYmUvUCMn7R8tJ9GVXqXZmWU1dFDhAJKoPcGp8AsFcjYATiRxFIK3l7BmMu6mFXeef8Aezmx_AeuTFvqiimgRyT3IP20GCZeu38zsf3X5yejKWM6vp3LnqM4bjFh_6p2CHJ_5Iatc1FGfl2PtFJXEEuy9XCrqZ-IarkmyapfVDkum5RLj-0T2aEboTVQU2mPXKWrj1G2ezrZ4ydrRUz4hjxAc-DK1f46GA8S6UpR4dp59Tu1BTuVU2slyqgUqVsF6FwI-MLHOwXJubu2f2SeDG6APcoN-uVBxL_RLLBTId0hh26S2xn7aKf4o9TESz5efhO3Ru9ORSBYsnaqmBelZD7XHUBULb2bFzuPp6YWjSG7qdDTVZyYy3A7AwSES9pZwHj3KXwSHXaRTtmJDsY8tK4E84Tdq6lq9jzflrC7N0uKKYl4wr5NxHklf6WyvY3xbME9Eqa7ixSEwr6bRlV5EPYAxN677lubix5DlkiV8ypvdvDabycCRKyRPobAMkcWsqURch7WHP1Ae5OjMGrWfdgkCNenipDWW7_WdYySJ8oz2auUIHrIjZWOEqfjsnfE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd31f766ad.mp4?token=pY5gCaBzMLEZ71Y2LAgfS5VuqX7s2MqaxLZWcZ5p2f1Q-lCWLKkyj8uJI311AUF1_Z5nQytG9EICTc4FWqmgRc9JDH-3T_ZbQsnnlMlJxQNvYmUvUCMn7R8tJ9GVXqXZmWU1dFDhAJKoPcGp8AsFcjYATiRxFIK3l7BmMu6mFXeef8Aezmx_AeuTFvqiimgRyT3IP20GCZeu38zsf3X5yejKWM6vp3LnqM4bjFh_6p2CHJ_5Iatc1FGfl2PtFJXEEuy9XCrqZ-IarkmyapfVDkum5RLj-0T2aEboTVQU2mPXKWrj1G2ezrZ4ydrRUz4hjxAc-DK1f46GA8S6UpR4dp59Tu1BTuVU2slyqgUqVsF6FwI-MLHOwXJubu2f2SeDG6APcoN-uVBxL_RLLBTId0hh26S2xn7aKf4o9TESz5efhO3Ru9ORSBYsnaqmBelZD7XHUBULb2bFzuPp6YWjSG7qdDTVZyYy3A7AwSES9pZwHj3KXwSHXaRTtmJDsY8tK4E84Tdq6lq9jzflrC7N0uKKYl4wr5NxHklf6WyvY3xbME9Eqa7ixSEwr6bRlV5EPYAxN677lubix5DlkiV8ypvdvDabycCRKyRPobAMkcWsqURch7WHP1Ae5OjMGrWfdgkCNenipDWW7_WdYySJ8oz2auUIHrIjZWOEqfjsnfE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ونس: دو سوم سلاح‌های دفاعی اسرائیل ساخت آمریکا است
معاون رئیس‌جمهور آمریکا:
🔹
طی سه ماه گذشته دو سوم سلاح‌های دفاعی که از اسرائیل محافظت کرده‌اند در آمریکا ساخته شده و هزینه آن از مالیات مردم آمریکا پرداخت شده است.
🔹
مشکل اسرائیل دونالد ترامپ نیست و کسانی که چنین تصوری دارند باید واقعیت موقعیت کشورشان را درک کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/660898" target="_blank">📅 19:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660897">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
ادعای رویترز: کاخ سفید متن یادداشت تفاهم بین آمریکا و ایران را به کنگره ارائه کرده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/660897" target="_blank">📅 19:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660896">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
ادعای رویترز: کاخ سفید متن یادداشت تفاهم بین آمریکا و ایران را به کنگره ارائه کرده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/660896" target="_blank">📅 19:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660895">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
جی دی ونس:آنچه ما می‌گوییم این است که نیروهایمان را به سطح پیش از درگیری بازخواهیم گرداند؛ قرار نیست چند گروه ناو هواپیمابر اضافی را آنجا نگه داریم
🔹
ایرانی‌ها این را نمی‌خواهند؛ راستش را بخواهید، ما هم نمی‌خواهیم.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/660895" target="_blank">📅 19:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660894">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
جی‌دی ونس: رقم دقیق دارایی‌های مسدودشده را نمی‌دانم
🔹
رقم‌های مختلفی درباره دارایی‌های مسدودشده مطرح شده و حتی ارقامی بالاتر از ۱۰۰ تا ۲۰۰ میلیارد دلار شنیده است، اما مقدار دقیق آن را نمی‌داند.
🔹
بیشتر این دارایی‌ها در حساب‌های آمریکا نیست و در کشورهای حوزه…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/660894" target="_blank">📅 19:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660892">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vmxULJR45iP1qbMGo4g0_OtRhQuQgKlfjqeLyMDOdN5x1jlXZp8GiuQQUovxcd-krXG_rLe2Kw1HDORKdgQga6RsSzWYFOqrXiQzcaS9hh7x_VVyr-fFG4z1sFVZRpRsv4EG80fs7aKZEWOqqx7DwECVSegytpKRTGtj4H55PNiPKS6JwU1f6EkvMvm0kHuKaqTTTG3Md4YsTfznhRAkpocA0tQQa_vVjdK0ozfqCH651ztoswAL9SXywIi1l7wyasopbT9psiLl_Ubm6vwjUbgv5OAqtw7cpkpow4rHsnYMgE1kn-htLKg_V-HfSCgg4442jiJMBFuafxslrC3eDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EKtZMaDOhGWbGjK-NnPmdA1sKcvfRaal0wF2mUplhw2cwhfI5Zyy6FzwesohMywoX4Aro4SFubUhKLH9rHGsxzOBLPna-JXcRpna5SWfQT6cNQPYLsSxL_GbIzSATAVVZk0-TmyvtAUmRuokKJ6byYeOWZKmE43_lpKPhIBpJaJhU1EYRzQ23rjPN0nbJ6HlTm1NpmcJwQab50UpFfSUOqpgbIZ9-Q65FmZd6hnLCfZulKVhBTHaSAMkii0SJtFgOL1y7OA1_w3jGUoHoL-ysE4miP6neoKnqdsU8hDEqf0VLG8qUmjOoU39ylDFoQ_ZtWObqib1CuUw8hsJkK0nrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر قرار باشد فقط یک کتاب درباره تربیت فرزند بخوانید، «نیک‌سرشت» را از دست ندهید
🔹
این کتاب به شما می‌آموزد به‌جای مقابله با احساسات کودک، آن‌ها را درک و مدیریت کنید. حقیقت این است که ما بزرگ‌ترها هم در طوفان‌های احساسی، بیش از هر چیز به همدلی، درک شدن و همراهی نیاز داریم. «نیک‌سرشت» راهنمایی کاربردی برای تربیت بهتر فرزندان و ساختن رابطه‌هایی عمیق‌تر و سالم‌تر است.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/660892" target="_blank">📅 19:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660891">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
جی دی ونس در مورد برنامه هسته‌ای ایران: توافق هسته‌ای اوباما اجازه غنی‌سازی را داد - توافق ما این کار را نخواهد کرد
🔹
توافق اوباما اجازه انباشت مواد غنی‌شده در سطح تسلیحاتی را داد؛ توافق ما در واقع منجر به نابودی آن ذخایر مواد غنی‌شده می‌شود.
🔹
توافق اوباما…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/660891" target="_blank">📅 19:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660890">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCgWjgo5bZHtvH7y6KuVRYD7r5IYBYTlH3Q9Lms0OqaZEkvsVyr33cXRoJvl8E1_SO6XxWBzpVMACTewby8GBXUWS4ZgrjcgLl8UTbEOm3yqp-JyK0mrcrIm7IdWnIdM5CyfZJ8O_OKAWv_BDHGKy2RqhMgsc9Iflm51OyhTPP-pwMNjEX2wv31_0AFxmsr8Nf8AeVgAONDHUuyGIH8RhTL-75_6QqOx7JCn6IJtiz_ANBYKUDTA0z_gps4Cz-3FayCgb0bAzYYIdruJGplqtlSdFoMXOKfVZC25IoDYrtNGvFUgBqe_atdBsIM1rv1BhQR2wnTdJZVdknDWladzxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهنمای سقف انتقال وجه بانک‌ها
🔹
سقف خرید با کارت برای اشخاص حقیقی مبلغ ۴۰۰ میلیون تومان تعیین شده است.
🔹
سقف انتقال پول از طریق سامانه‌های پایا و ساتنا، هر کدام ۲۰۰ میلیون تومان است.
🔹
برداشت نقدی از دستگاه‌های خودپرداز همچنان روی رقم ۵۰۰ هزار تومان باقی مانده است.
@amarfact</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/660890" target="_blank">📅 19:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660889">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
جی دی ونس در مورد اسرائیل: به نظر می‌رسد که ما درست در آستانهٔ یک پیشرفت بزرگ در توافق بودیم، و بعد ناگهان یک انفجار بزرگ در یک منطقهٔ غیرنظامی در بیروت رخ می‌دهد، و تعداد زیادی از مردم که هیچ ارتباطی با حزب‌الله ندارند جان خود را از دست می‌دهند. این قابل…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/660889" target="_blank">📅 19:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660888">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
ونس: مطمئن هستیم که می‌توانیم بدون کنگره تحریم‌ها را به طور موقت لغو کنیم  معاون رئیس دولت تروریستی آمریکا:
🔹
دولت آمریکا اختیار دارد تحریم‌های اعمال‌شده علیه ایران را به‌صورت موقت و بدون نیاز به کسب مجوز از کنگره معلق کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/660888" target="_blank">📅 19:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660887">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3093423e56.mp4?token=GITA8Mv8vZa5PKk2L3qAMbYvX_phsS66YJj8qiTS8DPwa21gdRdE8ny2dinhN4vXa_udJum7loCjGoqUbIk98BjLOpIXUsw2Py69yiHlt3jzhHFR0eG3LuSjjHdCs-ehOlZrDFNA_52HZFrB5DxLhXO2kduLdMb9lE8KCMZ2BDPcSB-83LE-7JmcbXGT2CpOBqtWWnQ4iqDr8kiOK_UaC1QMjpIu3dteaFQIhUGg4VhTlD-00RJuvopuwenAl9lfsPfwRQfmffx1NCDmG-YYzAe3Xatb4u8FW4asJ9M2f1WR9i5pk1MOzi5WwrkNs4HQaZWLLgNoh0afwLPolhrRfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3093423e56.mp4?token=GITA8Mv8vZa5PKk2L3qAMbYvX_phsS66YJj8qiTS8DPwa21gdRdE8ny2dinhN4vXa_udJum7loCjGoqUbIk98BjLOpIXUsw2Py69yiHlt3jzhHFR0eG3LuSjjHdCs-ehOlZrDFNA_52HZFrB5DxLhXO2kduLdMb9lE8KCMZ2BDPcSB-83LE-7JmcbXGT2CpOBqtWWnQ4iqDr8kiOK_UaC1QMjpIu3dteaFQIhUGg4VhTlD-00RJuvopuwenAl9lfsPfwRQfmffx1NCDmG-YYzAe3Xatb4u8FW4asJ9M2f1WR9i5pk1MOzi5WwrkNs4HQaZWLLgNoh0afwLPolhrRfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ونس درباره برداشتن تحریم‌ها: ما صادقانه این موضوع را یک امتیاز بزرگ به ایرانی‌ها تلقی نکردیم، ایران هم آن را یک امتیاز به خودش نمی‌دید، چون چیزی که مانع فروش نفت آن‌ها می‌شد، تحریم‌ها نبود
🔹
آن‌ها بدون هیچ تخفیفی مقدار زیادی نفت می‌فروختند، چون تحریم‌ها…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/660887" target="_blank">📅 19:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660886">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
معاون ترامپ: نباید از تنگه‌ها برای فشار بر اقتصاد جهان استفاده شود  معاون ترامپ:
🔹
ما هرگز نمی‌خواهیم که چنین اتفاقی دوباره تکرار شود، درست است؟ موضوع اصلاً بحثِ عوارض گرفتن نیست.
🔹
موضوع این است که اطمینان حاصل کنیم تنگه‌ها دیگر هرگز به عنوان یک «نقطه فشار»…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/660886" target="_blank">📅 19:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660885">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">جی دی ونس: تمام چیزی که رئیس‌جمهور دیروز گفت این بود که، بدیهی است، کشورها حق دفاع از خود را واگذار نمی‌کنند
🔹
اسرائیل اگر حزب‌الله به سوی آن راکت یا پهپاد شلیک کند، حق دفاع از خود را از دست نمی‌دهد.
🔹
ایرانی‌ها نیز حق دفاع از خود در کشورشان را از دست نمی‌دهند؛…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/660885" target="_blank">📅 19:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660884">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fac0ba5a10.mp4?token=XGS_wEm0_2vcXECSrRTmRLHQLFyTYbXwQg_IabcSy0ZU5TxttZAQiGxerCiWfsfS5dgRstdnPhjD9pgEiKNkylHQmiCh_hfaMUu6pXtxSDAT9ARasmxEXyUb9Z352X2wA7rJkx-o_mXpePwknyqpv4r7LxR0rVY1Wkl1DwzMjzGw437sNjtzhcuxZDKjUjxhMCxDCvtkhySp-YoatKILkeoR_SB5jpnCL5pWRQJYKML6fUAjOLjar8L1QQwAJG2g7eh88a9D8kkFFLhsYdh6RjKpqqkN8H6kbWOOONTgyY8saKlufuy9Uup5jC4fTnjuaX-P1yXf3iXeVcF_3OlEeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fac0ba5a10.mp4?token=XGS_wEm0_2vcXECSrRTmRLHQLFyTYbXwQg_IabcSy0ZU5TxttZAQiGxerCiWfsfS5dgRstdnPhjD9pgEiKNkylHQmiCh_hfaMUu6pXtxSDAT9ARasmxEXyUb9Z352X2wA7rJkx-o_mXpePwknyqpv4r7LxR0rVY1Wkl1DwzMjzGw437sNjtzhcuxZDKjUjxhMCxDCvtkhySp-YoatKILkeoR_SB5jpnCL5pWRQJYKML6fUAjOLjar8L1QQwAJG2g7eh88a9D8kkFFLhsYdh6RjKpqqkN8H6kbWOOONTgyY8saKlufuy9Uup5jC4fTnjuaX-P1yXf3iXeVcF_3OlEeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون ترامپ: تحریم‌ها علیه ایران را لغو نخواهیم کرد
🔹
آنچه تاکنون اتفاق افتاده، صرف‌نظر از اقدامات ایرانی‌ها، یک پیروزی برای مردم آمریکا و رئیس‌جمهور ترامپ است.
🔹
ایران دیشب به هیچ کشتی شلیک نکرد، و تا زمانی که رفتار مورد نظر را از ایرانی‌ها نبینیم تحریم‌ها…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/660884" target="_blank">📅 19:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660883">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/236c140d81.mp4?token=iYGCcJCGw6Z1ApBM-UjtBBa9UHDZKFBh24tr2iLfzLbCLErgc8MQpcOk44msTPbKeTU379ySbnoffyboX1-4NUAO5W2TR774rQON3Oo23v8uAr9PapK-LzE5BhHzQGpEu_Kbdc9sxMT5Wovu0lYO_2iAHZkY7RCilJF7pcJAiafxA8JYqGaJ2m5Dj9JBDiQfB0R6AsvbSGgFOyN3Mp4aJRv41CTu8HeYDokHA3P6T0jXX4hOjC4Zhb3l6JLdAxsPsKJcU38hiSYFy3d6k1e9OYcaOYnEmLbf8TsSB4CZVR79qWl_0YjNJZ2vQFYI3QHnn-BrhQIsE7FCnTfgjP25Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/236c140d81.mp4?token=iYGCcJCGw6Z1ApBM-UjtBBa9UHDZKFBh24tr2iLfzLbCLErgc8MQpcOk44msTPbKeTU379ySbnoffyboX1-4NUAO5W2TR774rQON3Oo23v8uAr9PapK-LzE5BhHzQGpEu_Kbdc9sxMT5Wovu0lYO_2iAHZkY7RCilJF7pcJAiafxA8JYqGaJ2m5Dj9JBDiQfB0R6AsvbSGgFOyN3Mp4aJRv41CTu8HeYDokHA3P6T0jXX4hOjC4Zhb3l6JLdAxsPsKJcU38hiSYFy3d6k1e9OYcaOYnEmLbf8TsSB4CZVR79qWl_0YjNJZ2vQFYI3QHnn-BrhQIsE7FCnTfgjP25Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رویترز تأیید کرد که محاصره دریایی ایالات متحده بعد از ۱۰۰ روز لغو شده و کشتی‌ها بدون دردسر از تنگه هرمز عبور کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/660883" target="_blank">📅 19:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660882">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
ادعای معاون ترامپ: شب گذشته ۱۲.۵ میلیون بشکه نفت از تنگه هرمز عبور کرده است  ونس، معاون ترامپ:
🔹
شب گذشته ۱۲.۵ میلیون بشکه نفت از تنگه هرمز عبور کرده که این میزان، بالاترین رقم ثبت‌شده از زمان آغاز جنگ علیه ایران بوده است.
🔹
نیروهای ما در خاورمیانه به بیش…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/660882" target="_blank">📅 19:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660881">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
ادعای معاون ترامپ: شب گذشته ۱۲.۵ میلیون بشکه نفت از تنگه هرمز عبور کرده است
ونس، معاون ترامپ:
🔹
شب گذشته ۱۲.۵ میلیون بشکه نفت از تنگه هرمز عبور کرده که این میزان، بالاترین رقم ثبت‌شده از زمان آغاز جنگ علیه ایران بوده است.
🔹
نیروهای ما در خاورمیانه به بیش از ۱۲ کشتی اجازه دادند تا از محاصره دریایی عبور کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/660881" target="_blank">📅 19:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660880">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOheIVUOMskyJXtj5gMyoRp4rwZsog6VcHmTHkvXFHaSHcNIKedxET-xYQkp5TdYGXIkh9tdIrjEfHQAX6Xi6fCGA9r8XRYu6vhW6zYPRsGYlu-k7g3J7mnU_CsaLPUtTfQHwqEhdYofvUwfjY3ebavuwoudwEyJz3R9NkoKR63JTu0tFojH8czZN9DqQu9eH0v2XR9GiVKJSEsoUpyf5K_4SqhBs1pNjko6KHPHLaqZFJgjLQYUNPekxPG-n5pZPXkneFHMsSf5NBRbgqXOa93a0GqlrapETWotAcISR6tjhtymnJc_zd4z7ULBkG16mjfjtBM8NOYZdR7vA8qABg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/660880" target="_blank">📅 19:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660879">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1lvrJxixUjnE-zw53nzQa3RUOpXZPxOZ4WURIMMHdK2A8Df63l5Ok9Kt7H5v0uOE6zDa13gWOsZhk71C3YHrf1xmTbupBXcg6f_838N8jYobn_GZuWzTwXsmmXrAhx7DdlsvZTlLhDulJGiLQ0v1iSg7x-r581isw15rXjV1dYqQGkr1NuhrfTiDZcJNX0Hb0EYJVp6SnEPCsmYOy7JMx0Z_bbFQ82lMAcCmcwOfcPehbj5p2hd_QswfLc3TK-y_Artxs-2YXxLAJv8oyvvzFeLI3yh-iXd9JsCdjF1YDqoVzVfBGiiEhrS6ZJicMjAWqBAzOswaZxnz1UsqC7ivg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش ترامپ به انتقادات گسترده در آمریکا به توافق او با ایران
🔹
این احمق‌هایی که فکر می‌کنند من به اندازه کافی در برابر ایران سخت‌گیر نبوده‌ام، در حالی که بازار سهام به تازگی به یک رکورد تاریخی دست یافته و قیمت نفت در حال «سقوط» است، یا حسود هستند، یا آدم‌های بدی هستند و یا نادان. دوباره آمریکا را با عظمت کنیم!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/660879" target="_blank">📅 18:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660878">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvQS_aBbzE_qmoJDlHfMH0jeSS3rrd4gmBFs_XyRHPqHINANLwTqmDKTRu4s1ZhIHWt8DwgD8KwpyKwI0d6yxWgTEx1yfIn0YWKyqMvU87ZoE_nLVuChheq17MpELn_WaFuK27xx0W0fgSHv7gYg3VdFLTryzEWEOgIpxhzcPF8wdylgfRsDtvkCCsONLRtyvaHy5FBZzmNBrzwU0U0f6pS6VYS67slE2KIvfHzcJ5-6Wjgi5jww7ggOAB9E4rtxcHWAxcP9E_0h66PX9ZzluHOHmMdsyZSHszuN5qClSWcB4PnA7_kWLtt17hjvM8Xph7UGSRROns3Q3J_bfp0x0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنی که مرگ فرزندش، سرنوشت میلیون‌ها کودک ایرانی را تغییر داد
🔹
وقتی بیشتر مردم حتی نامش را نشنیده‌اند، میلیون‌ها کودک ایرانی با میراث او بزرگ شده‌اند. توران میرهادی کسی که «غم بزرگ را به کاری بزرگ تبدیل کرد». او با وقف کردن عمرش در آموزش و فرهنگ کودکان…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/660878" target="_blank">📅 18:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660877">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
۵ میلیون بشکه نفت ایران به آب‌های آزاد رسید
شرکت تحلیل انرژی کپلر:
🔹
ما حداقل ۳ نفتکش با پرچم ایران را رصد کرده‌ایم که مجموعاً ۵ میلیون بشکه نفت خام را از محدوده محاصره دریایی آمریکا در خلیج عمان و دریای عرب عبور داده‌اند.
🔹
همچنین یک نفتکش دیگر با حدود ۲ میلیون بشکه نفت در حال نزدیک شدن به این محدوده است. نفتکش‌های دیگری با پرچم ایران نیز احتمالاً از روز یکشنبه (روز امضای توافق) از خط محاصره عبور کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/660877" target="_blank">📅 18:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660876">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0kMZHefvqcC3V7jhK5CNAg9zLVy8bnR5mw6ew62TktPYJKjWVtx8h7XtokmMmQGtUXvNnycp8kQd12doU3O0ivVeMdjshdZxS46dLbw5-Pdd253T8kGFHUSZlrPhLSrNvvAfZtiy8tCVbr0M1sTUvliUOnpHgBMoaCH7HugN5R63OvAY0An6e_WBAafpJXsHfTymJnnxnNlLhFjRAGER2dk6NnrM_kcbvVhkwyuU9fG7xehgpa42cFnBKTN_k_FJf56SVXGaMnuik0RfGG1vxb9oTob6pqpDYlXNuZNhCbId_Wmk1A-7cFJnC3dD4uzyey-PBT0ChudF1aHRiwQcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلندترین و کوتاه‌ترین بازیکن در جام جهانی
🔹
دروازه‌بان اتریش بلندترین، با قد ۲.۰۵ متر
🔹
مهاجم پاناما کوتاه‌ترین، با قد ۱.۶۰ متر
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/660876" target="_blank">📅 18:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660875">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faae639bb0.mp4?token=v0tR2rnmgOmkgElXe_LR7HJKcT6SGu_40IhZIjGRwJtwJbMKfy6-AyQZWMHCIgBkeeTt4o6WpqK-JPpblFaMihPvfZx-qXr4IF9j-WHKY6zHjtLFp7F6stLflvgUIIdLTRhA1wQjsOQWGiqmsw1GswlsGedtjfKC1AYOY7QDhrd6k0dc8bGJRaHzicWVKhbefeRg6WF2LoC5Mr74DncswkAEsG3QATiIamgk5NqyfPa1I3QZAUMt-44OACi8oEprNdsdgof6DM1rtVSDaA2fvhHPS4vefz4WLn7LQxeJV6mIWLsM0TpkWS86JOk39zsugOTrU0SHoYqAr2YYzCWGNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faae639bb0.mp4?token=v0tR2rnmgOmkgElXe_LR7HJKcT6SGu_40IhZIjGRwJtwJbMKfy6-AyQZWMHCIgBkeeTt4o6WpqK-JPpblFaMihPvfZx-qXr4IF9j-WHKY6zHjtLFp7F6stLflvgUIIdLTRhA1wQjsOQWGiqmsw1GswlsGedtjfKC1AYOY7QDhrd6k0dc8bGJRaHzicWVKhbefeRg6WF2LoC5Mr74DncswkAEsG3QATiIamgk5NqyfPa1I3QZAUMt-44OACi8oEprNdsdgof6DM1rtVSDaA2fvhHPS4vefz4WLn7LQxeJV6mIWLsM0TpkWS86JOk39zsugOTrU0SHoYqAr2YYzCWGNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنگ روز عاشورای امام حسین علیه‌السلام یک بخش از جهاد ایشان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/660875" target="_blank">📅 18:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660874">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
حملات اسرائیل به جنوب لبنان با استفاده از بمب‌های ممنوعه فسفری
🔹
ارتش رژیم صهیونیستی با استفاده از تسلیحات توپخانه‌ای و ممنوعه فسفری، مناطق مسکونی جنوب لبنان را هدف حملات خود قرار داد. این حملات شدید، ارتفاعات علی‌الطاهر در جنوب لبنان را هدف قرار داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/660874" target="_blank">📅 18:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660873">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پاسخ به چندتا سوال ساده میتونه تو این روزای بحرانی سرمایه‌ خیلی‌ها رو نجات بده
ما در حال بررسی دغدغه‌های مردم درباره امنیت سرمایه توی شرایط بحرانی هستیم. تجربه و نگاه شما می‌تونه کمک کنه این مسئله بهتر فهمیده بشه و راه‌حل دقیق‌تری براش درست کنیم.
اگه چند دقیقه زمان دارید، خیلی خوشحال میشیم، این پرسشنامه رو پر کنید.
تکمیل پرسشنامه
ممنون که توی ساختن یه مسیر امن‌تر برای سرمایه همه هم‌وطنامون همراه ما میشید.
❤️</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/660873" target="_blank">📅 18:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660872">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9c038fcf.mp4?token=YA2VB4pk-h737JbeBpriJdUwjUAL1p6R9vtSXlcuvPxvCV7rtB_SB1H3xgiJu9Q9b9siaylwiSebZ19rwogoKqIaZvgSErCgbamfPnvSL6PoB7lrKn-WIPbhdqXFXxRRyWbNi7Q9U_W9cdJXdChFs54Wjtnj8fr0Vj5VMit_Zxtp9lG0wRCHAvgQK5JJnxnHrZhd_dxpuNY0DfeLmb6Bf9aqQSMY2zb5ictl55Vi45XmOV5QxO98sRBgYwak2AjFAdfbfGDNhNyEGKAhnQlnR0d9VT9RVZseSBUSJY1As4QFoxsVjkyh7c0UyZP0RYwHPRtO6XoIwi5d_Qk_-bCc4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9c038fcf.mp4?token=YA2VB4pk-h737JbeBpriJdUwjUAL1p6R9vtSXlcuvPxvCV7rtB_SB1H3xgiJu9Q9b9siaylwiSebZ19rwogoKqIaZvgSErCgbamfPnvSL6PoB7lrKn-WIPbhdqXFXxRRyWbNi7Q9U_W9cdJXdChFs54Wjtnj8fr0Vj5VMit_Zxtp9lG0wRCHAvgQK5JJnxnHrZhd_dxpuNY0DfeLmb6Bf9aqQSMY2zb5ictl55Vi45XmOV5QxO98sRBgYwak2AjFAdfbfGDNhNyEGKAhnQlnR0d9VT9RVZseSBUSJY1As4QFoxsVjkyh7c0UyZP0RYwHPRtO6XoIwi5d_Qk_-bCc4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نقشه شوم براندازی در ایران از زبان نفتالی بنت؛ یک برنامه جامع و دقیق برای سرنگونی دارم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/660872" target="_blank">📅 18:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660870">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BICbWujUkxROrplDtCbfgeSUCdENnZAJDCmTdgRIJBGvztfLSjLLYhZAOdKFm0bzcQeg6NB-9lSYHL-BZlZnQ9XdS9SAtLoEE3kz1LS-oVrMPT14weY-L2CtA_N4zprQ1A8psTTLR2vWI4lAB-0z0EjM016IbslxJ8vE9VHLyOTnqIDqkF7b_JlnlA5eiWAYd_KGB3ihwzmovem0iJ9KeekD7TcgtArehPY0GDPQaFdCATrQhpvnTwCFHMVzKb0phI7JTv1DeRyHb-2dmrZp9KWuhW14jAbmdEmEqk0LwnuewZVqq7MS844k_Mj0TLhQINz6gqOdSlohUirytrr70w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XMOQQxkyDjHvQdusG9moiEmwwpj7f2qTsCcaMANr1iGHjZgHkisAupiLOhJA33zMTPXifiB7vft9AebS8Y4jXZqrplZMna_5A9_U01JjAzEkwgUp6Ma01MBmnrXAYh8b2RTEVMDx8hpot08pyttuxJv8xSvOTymFVv3hnFH9chkaDbRuAf-E1Vs2DtplA17vJxtvPZkBAfiSB2viTimxyneotnERMb6V7Atf9Kp5YfJJ6drtg-rdNLnPHL7GERzC8QjreBTbxPGDl3lCVfAWEHWWthPDgZKNRfJRMjcb2ieLWCh61jevSx2D4ce2ixS16JjRvU2zH8TV6lptnQohnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
متن کامل تفاهم‌نامه ایران و آمریکا به زبان فارسی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/660870" target="_blank">📅 18:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660869">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
علی‌هاشم(خبرنگار الجزیره): مسعود پزشکیان شاید تنها رئیس‌جمهور ایران باشد که چندین حیات سیاسی مختلف را در یک دوره تجربه کرده است
🔹
او پس از جان باختن رئیس‌جمهور قبلی در سقوط هلیکوپتر به قدرت رسید. پس از مراسم تحلیف او، ترور اسماعیل هنیه، رهبر حماس، که مهمان آن مراسم بود، رقم خورد.
🔹
سپس ایران مستقیماً به اسرائیل حمله کرد. پس از آن، رهبر حزب‌الله توسط اسرائیل ترور شد. بشار اسد سقوط کرد. جنگ به مرزهای ایران رسید.
🔹
چند ماه بعد، اعتراضات شعله‌ور شد. سپس جنگ دیگری رخ داد که در میان آتش آن، رهبری کشور تغییر کرد؛ رهبر جدید در شرایطی انتخاب شد که کشور همچنان در وضعیت جنگی قرار داشت.
🔹
و اکنون، همان رئیس‌جمهوری که در میان تشییع جنازه‌ها و موشک‌ها وارد پاستور شده بود، در حال امضای یک توافق صلح با رئیس‌جمهور ایالات متحده است.
🔹
در دوران پزشکیان، ایران هرگز از حرکت و گذار از یک مرحله به مرحله‌ای دیگر باز نایستاده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/660869" target="_blank">📅 18:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660868">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
مدیریت تنگه هرمز قبل از درگیری به خوبی کار می‌کرد. هیچ مشکلی وجود نداشت
شاهزاده فیصل بن فرحان آل سعود، وزیر امور خارجه عربستان سعودی:
🔹
کشتی‌ها آزادانه در حال تردد بودند. هیچ مشکل ایمنی وجود نداشت. هیچ مشکل زیست‌محیطی وجود نداشت.
🔹
پس چرا اکنون، در نتیجه یک درگیری، باید ترتیبات جدیدی را که قرار است به آن تحمیل شود، بپذیریم؟ این، به نظر من، منطقی نیست.
🔹
بنابراین فکر می‌کنم باید به روشی که قبلاً بود برگردیم، و آن روش به خوبی کار می‌کرد، و این باید پایان آن باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/660868" target="_blank">📅 18:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660867">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/US14nWIJ1mRsDFGblkdVRpgi0B7ivA1MskBQmFvmsAvlLbpqfyaDPF9RyJFu8nDV2KQzjbRH8JNNoEQN6Zspuo4N3q-pShlg1wG78eUu72ItBYCJ6-5RcZHHX311g2wOXrgqGoseaUuWBEe4aIbVNCTCXD7ylZBfioAz8EUjlUVvM-6kF10_WnBYpC2-Vkb7yItMp-uymQZhB43U---aN5kGMb4z91S7qNaxPfLmhmAMk6tF9dMd2zIi4ApxKE1mj3AM4-yNKpcfIsl5kGYLnGsJ4DGqRLNGhlM0EE5W9QNt372QBnEIblxPMOflbZKkIcSD19ao8v_QMrMBb_s9PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طبق نسخه ایران
🔹
پس از هفته‌ها تنش و رویارویی، دونالد ترامپ و مسعود پزشکیان سرانجام تفاهم‌نامه‌ای ۱۴ بندی را امضا کردند؛ سندی که به باور شماری از تحلیلگران و رسانه‌های غربی، مفاد آن از دست برتر ایران در روند مذاکرات حکایت دارد. ناظران سیاسی معتقدند فشارهای ناشی از جنگ و ایستادگی تهران، معادلات واشنگتن را تحت تأثیر قرار داد و دولت آمریکا را به پذیرش چارچوبی نزدیک‌تر به خواسته‌های ایران سوق داد. برخی رسانه‌ها حتی از این توافق با عنوان «امضا زیر نسخه ایران» یاد کرده و تأکید دارند که متن نهایی بیش از آنکه بازتاب‌دهنده مطالبات واشنگتن باشد، در چارچوب شروط و اولویت‌های تهران تنظیم شده است؛ موضوعی که از نگاه آنان، ایران را در موقعیت برتر این توافق قرار داده است.
🔹
هفتصدوهفتادوهشتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/660867" target="_blank">📅 18:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660866">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYibZU1eYUyNOAzgRDdo_F4ZwulXcOsaaIsZaZxqMjJrek7c_UCwYt6d7kufIR1nzMJC4p-N00BeKYTFOsPV6ZYSjCeNhzP46cdlixAqi5-dwSQZt-vWjNZ8lHGkfDFyGc31qFGLK8ZNXz2ZgPaY-JgcVdyrEzjpwL3uWct1yJeyLB_G0b2O5lVAAi3r8RAuRjBEtzhGyqjxp8AtamhOukB_3iCEjygQycuONo5vmumQwBRgQ7Nq5aEWc9vqL69mGlIT6t2gtDCgJyjgcLUf4KNbl2YedZp54U7adT1UMhS-UWixCM5uklbzcdRS-h4i9JE7zUQ04YS03EwysJaIDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتشار نخستین‌بار؛ تصویری از دیدار سردار سرلشکر شهید حاجی‌زاده با فرمانده شهید کل قوا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/660866" target="_blank">📅 18:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660865">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkZEnYpCEgDFsVMsRA6V8vA3eLu0ox-ifo9CjoXxfCurot05ltSrt_0o4dyCoWmwvG57G-Tf6SXvkz1R5t1btz7W2llTYIQC7QrbFtM8udbXcaQgTHW5Qxt5CKbI3upXrvB6b1TY3y-BNoUwYOQ-iLN1d20y4O5BllDRH46zcnaES8XlgOgwm5grj0Ghwld0uU20CNkyaOftpcSbnPtU23kv_NThQkbdvHobYxeIWJPrX4S3DRc-2_zNzCvYAjGPLZKCAK0ri5WEYxONHiLU_rfTDP_R9MKWMeBKnQGmgxjKspxlKk6SEpqRI_67vkLHwILuHQ2-hDj2asHZld7GMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کهکشان راه شیری بر فراز قله دماوند
#اخبار_تهران
در فضای مجازی
👇
@AkhbarTehran</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/660865" target="_blank">📅 18:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660864">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b7d1aae69.mp4?token=PbA-8A04Qw25hClqk4cifWUcvbCNBQiCXtfYFbFN0c9jXQo7YLixYZOryLCPUgg2QTz919QU4V-2_thXLDux2xK7n8ev33lJIw8zkFb143KRW_xfDD2X8zo1Zrn9DNts4nLHN0RLNSagfaKLU_lfXFssa1-YKEXqvZ2fB0Kze_1yOU4T77_ZaBcwyMetqZ4FkEC6ZmTMi1amCAH2VomGY1aKivGKlywypXkke5st38DNOwdFght6Ml6qLJ4a_PQ0UWgqb_kyYlJOw-NX5m8H9y2TZTgL5AuPmSNgTBO4rCpSTU1cYFk7Ts9H5Uw_sFl649_HmUpiURrfOJREPh8CkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b7d1aae69.mp4?token=PbA-8A04Qw25hClqk4cifWUcvbCNBQiCXtfYFbFN0c9jXQo7YLixYZOryLCPUgg2QTz919QU4V-2_thXLDux2xK7n8ev33lJIw8zkFb143KRW_xfDD2X8zo1Zrn9DNts4nLHN0RLNSagfaKLU_lfXFssa1-YKEXqvZ2fB0Kze_1yOU4T77_ZaBcwyMetqZ4FkEC6ZmTMi1amCAH2VomGY1aKivGKlywypXkke5st38DNOwdFght6Ml6qLJ4a_PQ0UWgqb_kyYlJOw-NX5m8H9y2TZTgL5AuPmSNgTBO4rCpSTU1cYFk7Ts9H5Uw_sFl649_HmUpiURrfOJREPh8CkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا با اسرائیل دارای سلاح هسته‌ای برخورد نمی‌کنید؟
🔹
گروسی: چون عضو ان پی تی نیست! خواهش میکنم عضو شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/660864" target="_blank">📅 18:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660863">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
مجری و فعال رسانه‌ای آمریکایی: آفرین به ترامپ؛ تجربه‌هایش از ورشکستگی به او کمک کرد این بار از سقوط به لبهٔ پرتگاه جلوگیری کند
🔹
احتمالا اسرائیل تصور می‌کرد که وقتی او را وارد این ماجرا کرد، می‌تواند درگیر نگهش دارد؛ چون هیچ سیاستمداری دوست ندارد در یک جنگ مقابل ایران بازنده به نظر برسد. اما ترامپ این‌طور به مسائل نگاه نمی‌کند
🔹
ما که قرار نبود ایران را فتح کنیم و آن را تحت اشغال در اوریم ، اسرائیل او را متقاعد کرده بود ایران سقوط خواهد کرد. او هم ساده‌لوحانه باور کرد ، پس اصلا فایدهٔ این کار چه بود؟ کاری را که اسرائیل می‌خواست امتحان کرد، نتیجه نداد، پس ضرر را پذیرفت و از ماجرا عبور کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/660863" target="_blank">📅 18:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660862">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaQvckhHtWWKwD-i71BcQRBehNKZoeiYX-7mEcfk5kYgN1CRhwy9K7vvAusolXISOuDj6Ji7LZ5KzN-iG9MEcTV1q-KhKUw2b_mVqPTp6jIh8S7DvyC-Sqoeei_AYXbnBNgsilhirvlaIi4rgSwc91xhIP6_mA8JoPvoAzwsc3NJWDhi89IkiaX_0m4m73lE9Yx0Ax5IXe-Ct2EnSEi7F0arfeUHd66kwmhrwiyRwg4FY8jONHQttc9HMGkAirelYOQYaObVqEifg1xoWGLMYG1NXxMhUg1kGF86S7pmyV_VVgpLexmbIQoe0tdXMHY5kaQBef9KpjmREU7TeUcfjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نتانیاهو: ما نباید از لبنان عقب‌نشینی کنیم
نخست وزیر رژیم صهیونیستی:
🔹
ما نباید از لبنان عقب‌نشینی کنیم. ما چالش‌های بیشتری پیش رو داریم که نیازمند پایبندی به منافع امنیتی و حفظ روابط با دوستان آمریکایی ما است
#Demon
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/660862" target="_blank">📅 18:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660858">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftgn39hSnQR7vFDwY8oNYkDhBKWkDtY4RtszulT0lsOLZsEfA8Rn9BC_byycaosGwYPrSndl-YDdMqKCPO3ROqmgKBJVQd-O7bLKVoA3lBKjnm6IX8LSgJIcksgbSJ0rmTcn6OuinzODVbDfMWQvEQM4Hd_v5PExynQr-Zp_yzJOA3MnCFEDX91Z_zzH22oUKSeb3-F4gyY8XY8hAmSCZ1I6eYPCfrQariAks2p4fpDpe1n3wWeMYEExB6qCCjJkLGJfH2lEnJ3ntkSpJuhYJ7uxoVM96A1e4odsqRL3MD6GtidkYBDYgl-hQVb_M2SUjuMbBEz1oAAR9Xhy_iA-2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مارک کلی، سناتور آمریکایی: ترامپ ما را بدون هیچ طرح و برنامه‌ای وارد جنگ کرد
🔹
خانواده‌ها عزیزان خود را از دست داده‌اند. میلیاردها دلار هزینه شده است. برای چه؟ این توافقی که او امضا کرده، ایران را قوی‌تر و مسلط بر تنگه هرمز باقی می‌گذارد، اما در عمل پیشرفت چندانی در راستای منافع آمریکا ایجاد نمی‌کند.
🔹
این معامله‌گر حرفه‌ای یکی از بدترین توافق‌های تاریخ آمریکا را انجام داد. این یک تسلیم کامل است! قدم بعدی چیست، روس‌ها آلاسکا را می‌گیرند؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/660858" target="_blank">📅 17:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660857">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
گفتگوی تلفنی سران ایران و پاکستان
🔹
پزشکیان: تلاش‌های پاکستان در مسیر دستیابی به توافق پایان جنگ در حافظه ملت ایران ماندگار خواهد شد.
🔹
شهباز شریف: صبر، استقامت و رویکرد مبتنی بر عقلانیت و تدبیر مسئولان و ملت ایران ستودنی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/660857" target="_blank">📅 17:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660856">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
ایهود باراک: باید نتانیاهو را با چماق از نخست‌وزیری کنار بزنیم
🔹
ایهود باراک در مصاحبه‌ با شبکه ۱۲ اسرائیل تأکید کرد که احتمالا نتانیاهو در آستانه انتخابات رژیم، به لبنان حمله خواهد کرد، و در تلاش است یک جنگ ابدی را با ایران و حزب‌الله آغاز کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/660856" target="_blank">📅 17:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660855">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
ترامپ به شبکه کان: احتمال خوبی وجود دارد که از نتانیاهو در انتخابات حمایت کنم، اما منتظر هستم تا نامزدهای دیگر را بشناسم. او باید منطقی‌تر باشد
/ انتخاب
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/660855" target="_blank">📅 17:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660854">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e96275c4a5.mp4?token=iUkdSBwsMaDYtUhTPXtCi9NtDVPEFo3MfJnvlIu2wKhgJQSh6p2mxBZA5Q_NhnAXrGn4aN_DKCA4UFy5F3hZc5xDDCQc_zH-SuUsbI9Drl-vrPHJgriiOJsuNBGyUnk_WPxDbdeOEOlydFCUwJCpkKcIRXipf8dC2hxYYQn1YQX02F6j3xlIYzzk7OJRTSV4PvzCCnsUgpwLny19Qq2fjsbAaW6dxAbJDqDVUCNDkUuPyRMNRfpB-D8eZn-Ru0jtXUFYlS6-_JI_14Jz52cC5Ah_vfXV6578vr6UEfIqEyAm4miUiT4yk0Y353IvdEw_nJsgCs779J6OU0j9ZCxJTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e96275c4a5.mp4?token=iUkdSBwsMaDYtUhTPXtCi9NtDVPEFo3MfJnvlIu2wKhgJQSh6p2mxBZA5Q_NhnAXrGn4aN_DKCA4UFy5F3hZc5xDDCQc_zH-SuUsbI9Drl-vrPHJgriiOJsuNBGyUnk_WPxDbdeOEOlydFCUwJCpkKcIRXipf8dC2hxYYQn1YQX02F6j3xlIYzzk7OJRTSV4PvzCCnsUgpwLny19Qq2fjsbAaW6dxAbJDqDVUCNDkUuPyRMNRfpB-D8eZn-Ru0jtXUFYlS6-_JI_14Jz52cC5Ah_vfXV6578vr6UEfIqEyAm4miUiT4yk0Y353IvdEw_nJsgCs779J6OU0j9ZCxJTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ در اول آوریل: ما اکنون کاملاً از خاورمیانه مستقل هستیم. ما به نفت آنها نیاز نداریم
🔹
ترامپ در هفدهم ژوئن: اگر با تفاهم‌نامه موافقت نمی‌کردم، ذخایر ما در حدود ۴ هفته تمام می‌شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/660854" target="_blank">📅 17:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660852">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
ادعای منابع پاکستانی: ایران به پاکستان اطلاع داده دیگر نیازی به برگزاری جلسه حضوری در سوئیس نیست/ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/660852" target="_blank">📅 17:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660851">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
لغو سفر شهباز شریف به سوئیس  الجزیره:
🔹
سفر برنامه‌ریزی‌شده شهباز شریف، نخست‌وزیر این کشور به سوئیس، بدون اعلام دلیل رسمی لغو شده است.
🔹
این سفر که قرار بود در دستور کار نخست‌وزیر پاکستان قرار گیرد، به طور ناگهانی و بدون ارائه جزئیاتی از سوی دفتر شهباز شریف…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/660851" target="_blank">📅 17:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660850">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGlbQkKB_rJX_rrXphSM5ksZy6uuB7l28GPIKhcVuekXnuXDVj8ed4Opz2BzxGlrr4PgaNuiTNP-mPkc89CDuON13MObOrEFOej04nSEXsIBOZV7t0XVbZStbq9RG8kM8mxgyClsMvqkLTeufN7sbNk7wTQ-xnwRXYwqkjKrxaQ5UydR5b8f2VxPMp0uN3tc6s8y50JH_CEL6SAAEMBO37VKIJI89WWZcJt6icLQyLSKT4OhJxfOWNiJ_WuNYE058YPCMaSQ-JDy8EcNyOeg4Oxtt72ksjRNvi_vOGNU1_XcsIyeaikK1Qi_l75lfVe0wDwIZHgCrMcCy56aZS_I8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست جدید ترامپ: قابل شما را نداشت!
🔹
نفت در جریان است، ایران هرگز نمی‌تواند سلاح هسته‌ای داشته باشد (جهان امن خواهد بود!)، بازارهای سهام در حال رونق هستند، مشاغل رکورد زده‌اند و قیمت‌ها در حال کاهش هستند (توانایی خرید!). کشور ما قوی، امن و محترم‌تر از همیشه است. قابل شما را نداشت!
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/660850" target="_blank">📅 17:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660849">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBwYaSdl_RJXZArpuwh9LPjhx9XS2o7qtAC00eZWRzIsi6g8looofQbMz-HgUvbyG6AiI28X0Axb8hlMsoGdZlZPIEJ2m2m8dolsnBchY3m9QrfEzmrQxjS_UqLa41hz5K5c2D-pvRyE7wb5MjG1Vc6lbooNC2_OVR41l-INB3aEbNmn3Cwmdrba3y-oCUAyFSR9oFXsYgDLam2n6OYN6x_nglNxbv10T6LP0SK5nz0-TBnqTrKBvbkyQC8alT61xcMxtF5kQVy4z5mpaIk66lyvx_hXF_SlTWhktBEqTRYBDrij19DBryBsjKW04GFYyIZL6fJJBYSJjlAjyMlWtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران خودرو قیمت افزایش داده‌اش را کمی اصلاح کرد!
🔹
این کاهش در شرایطی رقم خورد که این شرکت در یک سال گذشته چندین بار قیمت خودروهایش را افزایش داده.
🔹
در این اصلاحیه تارا توربو حدود ۲۰ میلیون، دنا پلاس ۶ دنده حدود ۱۳ میلیون و پژو ۲۰۷ هیدرولیک حدود ۷۵ میلیون تومان کاهش یافته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/660849" target="_blank">📅 17:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660848">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
رفع محدودیت تردد کشتی‌های تجاری در بنادر جنوبی ایران/تردد ۵ فروند کشتی حامل کالای اساسی
دبیر انجمن کشتیرانی:
🔹
تردد کشتی‌های تجاری به بنادر ایران از دوشنبه هفته جاری به حالت عادی بازگشته است. تنگه هرمز همچنان تحت نظارت نیروهای مسلح جمهوری اسلامی ایران قرار دارد و شناورها باید با هماهنگی مراجع ذی‌ربط تردد کنند.
🔹
تا کنون سه فروند کشتی حامل کالاهای اساسی و غلات وارد و دو فروند خروجی نفت خام داشتیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/660848" target="_blank">📅 17:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660847">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
ادعای اطلاعات آلمان درباره ایران
🔹
بر اساس گزارشی ۱۴۰ صفحه‌ای که به تازگی منتشر شده، سازمان اطلاعاتی آلمان مدعی شده ایران به عنوان یکی از چهار بازیگر فعال خارجی در زمینه «جاسوسی در برلین» فعالیت دارد.
🔹
این گزارش همچنین روسیه، چین و ترکیه را به عنوان دیگر بازیگران اصلی در این عرصه معرفی کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/660847" target="_blank">📅 17:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660846">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVf4tQb4x-r4tK52nfDK3ACiULgpQ3AVIaQyXcZbqze-Klzm-01yHcAxUanan15kMZ3Fw-9ZF9w2CYyFp-UyDYlXeoMgq7ax1yrzOVtCs26UtJO1o8TorQICGLFj_zJOymSfVW9ZdkKJH1WlFos3lr6ga8MkhJ_csN1OUZc7dq57-XpscBCvhwi_-mCtVnsIGJhOl5QrK7K1lROFrFmyamU1UuIIOovS0cY3ZjKR216ZKlESyC2k1y_uziiGgqV4Ra5OVmRB5V7fhn5lCKdw-6jt1qwAFkBbebQJ0IBC8WilSZCsCpQHthXCHxXt8sVS1U5FZvsqv-ez57mVP66iMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاخ ورسای فرانسه
🔹
دیشب ترامپ سند حقارت شکست نظامی اش با ایران را اینجا امضا کرد و تمام دنیا نیز دارند همین نکته را در مورد امریکا و ترامپ میگویند
🔹
در کاخ ورسای، جلسه پایان جنگ جهانی اول انجام شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/660846" target="_blank">📅 17:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660845">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
لغو سفر شهباز شریف به سوئیس
الجزیره:
🔹
سفر برنامه‌ریزی‌شده شهباز شریف، نخست‌وزیر این کشور به سوئیس، بدون اعلام دلیل رسمی لغو شده است.
🔹
این سفر که قرار بود در دستور کار نخست‌وزیر پاکستان قرار گیرد، به طور ناگهانی و بدون ارائه جزئیاتی از سوی دفتر شهباز شریف لغو شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/660845" target="_blank">📅 17:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660844">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idBSHgmbs3aqa9fIwPlKEEqZYGSqww5VXF4lBJGpwvxfIy9ayqOt0EcYzeXuyvKkzCJVSAjaxmLKiy5fGadbOgDIqcXb2yDOLxt37hHyPCx50XVJ0bt6oT4r05kLeLBzc5CShs4MWi6Z-SbL6Qaf3H0p4UfClYVsG1VfnOlBIIyOjqtyeq992XJn3QDDHL0nvipHKKbn-Fw6DEbA1wghw97YOPJHrBk22_AwMy5Rp-LQcpaB5M2SOEz_Qb3__gTv0yGNq5waOMJHEiDDB_4tm5nMNCNoUBIs5739ltAZKeXYGfLhURL8yhjjuXO5NcmoH70Cwly8FUTNv3FeRasWcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعا یک فعال رسانه‌ای درباره رودرویی وزیر نفت و رئیس در ماجرای هلدینگ خلیج فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/660844" target="_blank">📅 17:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660843">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eeffe02ee.mp4?token=MmKJSEIBuZLepvVL_31G8SPbnHNkOkKPLzicp8DxJUw5pwx_UwpJ4qT1-xRbwrrRVDgpZ1OkizVeEHJtpYBjdxz9GTcxC_W6WkCtwvP0Y2u9os5Hr1ZL9pZrUQfyvkDCb1bNeACMROhZ0r5hyY5FcwwkhAF5GAcwoxsExbgCSg33MbXZylZqo7SxRimpMwOCNrIewF-UAghyhr6QxxOXu-1SXG_Ew8H-KayrxtdVM9vActQ4QGkaKujNHluAV9ihW94zFkWuISkFEcVTuvbIgJK1a_e0fY0xn_q4mkI4MEEPvus6KF-7KHxZSjFVXo1ylSnEKq34C5rzk5wuA7p3jx6gr0gyFx-kcSDLb51Wa5Ru3hCIin6rXdAndSDJq05PHFItSVLZV2OAFZs9h61RNSvIyJV_0fAU44ay0l3oWUs4wD4vIFOgizBSVdY9Fu-NavuXETu-MLSiA7b030Yo1l6T8_iCy4nwEw2jC_2Hurf3MWserUn9nTNl8j1ZY9uMALCjiNHTNK3i9LUlT0WxjaFojglJjvJoN1_9_u13iN-6lax3gAOivrDMhHNqUFLl12ohpu5gIKr045u7-HSkzQHITbZYfA73Zjcec4yriDOpZ5EXc-df42SbK4shsfyrc6zvRIkZxyvq6_Ve-xJaZ_lQlPJG7Tel15efLv6-PHM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eeffe02ee.mp4?token=MmKJSEIBuZLepvVL_31G8SPbnHNkOkKPLzicp8DxJUw5pwx_UwpJ4qT1-xRbwrrRVDgpZ1OkizVeEHJtpYBjdxz9GTcxC_W6WkCtwvP0Y2u9os5Hr1ZL9pZrUQfyvkDCb1bNeACMROhZ0r5hyY5FcwwkhAF5GAcwoxsExbgCSg33MbXZylZqo7SxRimpMwOCNrIewF-UAghyhr6QxxOXu-1SXG_Ew8H-KayrxtdVM9vActQ4QGkaKujNHluAV9ihW94zFkWuISkFEcVTuvbIgJK1a_e0fY0xn_q4mkI4MEEPvus6KF-7KHxZSjFVXo1ylSnEKq34C5rzk5wuA7p3jx6gr0gyFx-kcSDLb51Wa5Ru3hCIin6rXdAndSDJq05PHFItSVLZV2OAFZs9h61RNSvIyJV_0fAU44ay0l3oWUs4wD4vIFOgizBSVdY9Fu-NavuXETu-MLSiA7b030Yo1l6T8_iCy4nwEw2jC_2Hurf3MWserUn9nTNl8j1ZY9uMALCjiNHTNK3i9LUlT0WxjaFojglJjvJoN1_9_u13iN-6lax3gAOivrDMhHNqUFLl12ohpu5gIKr045u7-HSkzQHITbZYfA73Zjcec4yriDOpZ5EXc-df42SbK4shsfyrc6zvRIkZxyvq6_Ve-xJaZ_lQlPJG7Tel15efLv6-PHM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد جالب مجید بنی فاطمه و مهدی رسولی با مداحی نوجوانی که در حسینیه معلی شروع به فالش خواندن کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/660843" target="_blank">📅 17:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660842">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kk22sBu3P8QfQoUYG8pYfB-lLMYxHNUugPgsr92cekX4hdBduiybE9iRzkjebJVhZjLMcJacnxr58z5DTS1NuZA5x1kzEiPNxs9dp2honFKBMb04dwI-pTDDSvSygYE9Y9MG8stu0ys6bEf_yh1DVuJOanEMlvuP6Mx5c1gW1ICrcmi1arqSvKmCx-9ltTrNfoEvFN3v7678P5g9v8CTFcN2jc89YLLqETgaF7IHwjTXSslbJ-3Lzztb9Q0YRxUCJO5WOG1XmdQAaUt26KjFyzzb59ZD_TG1lUoU4aS9fk9M9qpYLt5VERKtY8_krQn84E9XR9ZiPUUJ0Et4TxpsZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جان بولتون: توافق آمریکا به معنای واگذاری کنترل تنگه هرمز به ایران است؛ اکنون تهران می‌تواند جریان انرژی را مانند کلید برق قطع و وصل کند....
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/660842" target="_blank">📅 17:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660841">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
وندی شرمن: دونالد ترامپ به نظر من عملاً در برابر ایران تسلیم بی‌قید و شرط شد...
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/660841" target="_blank">📅 17:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660840">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
تا این لحظه سفر هیات ایرانی به ژنو قطعی نشده است
یک منبع آگاه:
🔹
تا این لحظه هیچ چیزی درباره سفر هیات ایرانی به ژنو قطعی نشده و بررسی‌ها و رایزنی‌ها در این زمینه نهایی نشده است.
🔹
این موضوع طی ساعات آینده مشخص خواهد شد که هیات ایرانی فردا در ژنو حضور می‌یابد یا خیر؟ و اگر پاسخ آری باشد، درباره جزئیات آن اطلاع‌رسانی خواهد شد./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/660840" target="_blank">📅 17:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660839">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db64afb394.mp4?token=J9uNOC5fEpNMp9ZMSjARzBd5ilPPE6Z48DaO08sPBwj74oMGGTrBP0-9V-HL9eashmAKmfa1y78hfuYugP5SUYWtar5I5-R0By3E9ReYy8d6--8ktnZPpsWBMHcG7fTmehl1JpnrH4xPv4lw-R0QXd-dYLXkeOY8YRBWhpEc_VvIEQRXqwYpiHhFHeukx3as8Snkc_kIllR5H_vPvGqmpmscfGrb074OHQcfyGvRKaFEUob3NcYXbjGGPf0_ZUzvYR_lNKm8Fodnr0MhTV_QuhtlA4RzGDYNVLFEB8r77IBnzCXsYEr4MsgPJWvHSGvWhbfsqOP-UsmC4qrMbDWWnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db64afb394.mp4?token=J9uNOC5fEpNMp9ZMSjARzBd5ilPPE6Z48DaO08sPBwj74oMGGTrBP0-9V-HL9eashmAKmfa1y78hfuYugP5SUYWtar5I5-R0By3E9ReYy8d6--8ktnZPpsWBMHcG7fTmehl1JpnrH4xPv4lw-R0QXd-dYLXkeOY8YRBWhpEc_VvIEQRXqwYpiHhFHeukx3as8Snkc_kIllR5H_vPvGqmpmscfGrb074OHQcfyGvRKaFEUob3NcYXbjGGPf0_ZUzvYR_lNKm8Fodnr0MhTV_QuhtlA4RzGDYNVLFEB8r77IBnzCXsYEr4MsgPJWvHSGvWhbfsqOP-UsmC4qrMbDWWnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار شدیداللحن مسکو به تهدیدات احتمالی ناتو
سخنگوی وزارت خارجه روسیه:
🔹
در صورت وقوع هرگونه تجاوز از سوی کشورهای عضو ناتو به هر یک از مناطق روسیه، پاسخ مسکو «قاطع و ویرانگر» خواهد بود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/660839" target="_blank">📅 17:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660838">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
وضعیت عجیب «بازار رضا» بعد از بارش سیل‌آسای دیروز مشهد
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/660838" target="_blank">📅 17:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660837">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
نتانیاهو بار دیگر هرگونه عقب‌نشینی از خاک لبنان را رد کرد
🔹
نخست وزیر رژیم صهیونیستی در تازه‌ترین اظهارات خود، بر تداوم حضور تجاوز کارانه نظامی اسرائیل در خاک لبنان تأکید کرد و آن را شرط اصلی بازگشت امنیت به شمال سرزمین‌های اشغالی دانست.
#Demon
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/660837" target="_blank">📅 17:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660836">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c13ba4587.mp4?token=VN2Gv99OBZuESh7bvxaay5lm_HbGPHKAhBfCCayCK_DDhKqwOUuuzb0qQ-7zkGsk8OqHGK9bDVZe7ANy4Ni8Z5a6hnMrS2Xpvm9auwVodFyquhcPFasyn4lbMh0gAC8W3kVVKMsQ3-n2B49VGG324VEnJT_8AQg6J5nF2JSoJ0jK_KBF6d-7JPlFlbD7LHtp2IIHIxCVidhTT5VXM5PvuNZc7uqacxBMdRqh808U5pYtN7_-mrrtTy9GSuBXtpmUnCaYtlpEcz3-0uF2rWr8YaDRgkxgpCG6Nz4fhfD8NzEsLq9jA_xM2raLDIlqr28giegstG7j9xyvSaZxvgsjcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c13ba4587.mp4?token=VN2Gv99OBZuESh7bvxaay5lm_HbGPHKAhBfCCayCK_DDhKqwOUuuzb0qQ-7zkGsk8OqHGK9bDVZe7ANy4Ni8Z5a6hnMrS2Xpvm9auwVodFyquhcPFasyn4lbMh0gAC8W3kVVKMsQ3-n2B49VGG324VEnJT_8AQg6J5nF2JSoJ0jK_KBF6d-7JPlFlbD7LHtp2IIHIxCVidhTT5VXM5PvuNZc7uqacxBMdRqh808U5pYtN7_-mrrtTy9GSuBXtpmUnCaYtlpEcz3-0uF2rWr8YaDRgkxgpCG6Nz4fhfD8NzEsLq9jA_xM2raLDIlqr28giegstG7j9xyvSaZxvgsjcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دهکده‌ای در شمال نروژ که برای فوتبال کوه را منفجر کردند
🔹
در شمالی‌ترین نقطه نروژ و بالای مدار قطب شمال، ساکنان یک دهکده ماهیگیری برای ساخت زمین فوتبال بخشی از کوه را با مواد منفجره صاف کردند.
🔹
زمین‌های منطقه صخره‌ای و ناهموار بود و اهالی با تلاش جمعی این زمین را ساختند؛ جایی که در تابستان خورشید غروب نمی‌کند و در زمستان همیشه شب است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/660836" target="_blank">📅 16:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660826">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/040fc246ec.mp4?token=bBuN-8-wAFtn3_OY30RDqdKelVmtdKwyDOruSLj2i5aCdXuGw6QBRE-JkKnGbnkeqgXcf1owHRqfBsQFWcQeQA9NezbJk_ldyEYIqpaFqvp_ju_1I2M3DyVG5viOkUmEeZH86irBzFox5v94lt4LbGCEB_gdzC2L0E5c9WjRqFwZC3JM8jUtderJ4ZlODxbPJ-Y0ekDTmEmgEOOJ5bDaudYQiLylpr_4dukMasIc4822zaR6TZbKpaXhr-HPsX8YhBauYX7MNefSYCb_27KP6EbWGHuQx-8rd_tv4hBt2PQYWHR31s1VH3SmXOJ-Z7LQSOYtVW8bgGpLgN_VH1ElRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/040fc246ec.mp4?token=bBuN-8-wAFtn3_OY30RDqdKelVmtdKwyDOruSLj2i5aCdXuGw6QBRE-JkKnGbnkeqgXcf1owHRqfBsQFWcQeQA9NezbJk_ldyEYIqpaFqvp_ju_1I2M3DyVG5viOkUmEeZH86irBzFox5v94lt4LbGCEB_gdzC2L0E5c9WjRqFwZC3JM8jUtderJ4ZlODxbPJ-Y0ekDTmEmgEOOJ5bDaudYQiLylpr_4dukMasIc4822zaR6TZbKpaXhr-HPsX8YhBauYX7MNefSYCb_27KP6EbWGHuQx-8rd_tv4hBt2PQYWHR31s1VH3SmXOJ-Z7LQSOYtVW8bgGpLgN_VH1ElRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی آب و فاضلاب کشور: رقابت های جام جهانی مصرف آب را در کشور افزایش داده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/660826" target="_blank">📅 16:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660825">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcIhRDUs9wMZvOlt1EyGtyt7z3pp1MfHszR9OevlTbBS456LvxRNgKxW_uESqZwmp8oLoYM2FqyylxkpS-0SFTZnOuJlJhnjQZEMVe6bxouT0UoWyB4hRNM_jSyBn1OKrjgJcfhzQFuvPQYJFlfxez0g1Eve9_-gTUxgefmOR6f-kbKWyG_pPWtHnZ0pjE2Ugde7AtU83KfIY32C8WOKtrQbnheE5sD37tl-FQA6OSH1TqedQ8BBGQ_sDv9HygQbHoA3M7qCKhRWXxHcPrUbabsw6HVr6tlnmq8jLt21AJ81MLcrdKoHm24EdTaXZelQ0HKrHlTGeIVa1OuVccEi5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶۹٪ آمریکایی‌ها از مسیر حرکت کشورشان ناراضی‌اند
🔹
طبق نظرسنجی مرکز تحقیقات پیو، ۲۹ درصد از مسیر حرکت آمریکا راضی و ۶۹ درصد ناراضی هستند.
🔹
براساس این پیمایش اکثر آمریکایی‌ها  انتظار دارند اقتصاد ضعیف شود، کشور دچار تفرقه بیشتر شود و ایالات متحده تا سال ۲۰۵۰ اهمیت کمتری در جهان پیدا کند.
@amarfact</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/660825" target="_blank">📅 16:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660824">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Osh69XRfEwIO_UiVrFiiCB_cBU_Ds38GR2bvOCTWnjP2kT0gYE-2Lu0pXS7YY2C_2tWuxRqRN9rIoLK28T8nuXjVezd9LE0bJD7DQAn22_j-NWgmHvPrtdGcNKwl8ZDlDLpvo5Q0XXzkaPE1SrvJjMFRon5LE0OgTL0So47oXvnF6RmhKH71zcTWE3QPntpyoAuPshD9i5JVGqkSTLSjTUK3FjwlvchukX8Wu_MNzQlXx2ywHqiwmTiKnOR-NSrq40fH7oDhE3NJ179eekT4deMPsB--mvuyURUMZ9CyLzRrsMR3SdZvgnD0D2g5hkEiaxFHgHojUlq8TcQGJvnsnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۸
تکه یخ جادویی برای پوستی شفاف، درخشان و بی‌نقص
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/660824" target="_blank">📅 16:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660822">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3u990wlyfBMhJN9Y54kOZglDLFarGbntigfGhpoFFQG2OTYcJTIuQ1Krv7HtM6znN3adNNRTevebECZKDFt8ViUHyEb6dm9PHifPewLNz2TfbPtIc8wfUJjh45z7y-6GToTOjuGQzu9qU4zV8cSlcYJ26mvX2vHEN1ZiLZ3xvnmCBFfhxeqhN3kfGxg3mp9xTPhFK2xEzNAyVp4YUC4y1aJ2bYCrkNAEckHNQ9RIL8OyN5Y3EC7ojELrpPl9cujvXqXX1moU3jZ0P4iOPU4s1ylv1KuSVKocucNd_6WkIR5kKhMdDuFRkoL0Q55WiiB7mW1cvFa_RZI9D1cMHk4iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
داریو هررا، داور آرژانتینی، قضاوت دیدار مقابل بلژیک را بر عهده خواهد داشت
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/660822" target="_blank">📅 16:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660821">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abae2a6c46.mp4?token=qdppbDfq2dRWA28puA2OoGl7c-OUTng2lIXWSGW9rc8Zk1sY6MWCT3goq3OpVdoa1keRG5h-QvPfv7meeHhwXccSJennYx4vN_DqrDlLTeMh5jTpCKxPxl0QgJDIXwhpqsSL1EMC4jUrv_K4ddwmhEKOMsEIg_LuEm-598o7vN7ztrXuYysOBJ9U0Kun5JJyoLipd1BHPDBHCA7NbMke5Vv-Y8SbItC3_MtRvfmWDZcBtd7EVygIoEQ0w20k5KI-aBaYS-HXXD3eWKbiDvfjw1WVhiBCNmjZGGqy7OO7OwneNFFXf8GKMB-W6KCSSghvpMimmeG-YbrJN3tkw1ZfdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abae2a6c46.mp4?token=qdppbDfq2dRWA28puA2OoGl7c-OUTng2lIXWSGW9rc8Zk1sY6MWCT3goq3OpVdoa1keRG5h-QvPfv7meeHhwXccSJennYx4vN_DqrDlLTeMh5jTpCKxPxl0QgJDIXwhpqsSL1EMC4jUrv_K4ddwmhEKOMsEIg_LuEm-598o7vN7ztrXuYysOBJ9U0Kun5JJyoLipd1BHPDBHCA7NbMke5Vv-Y8SbItC3_MtRvfmWDZcBtd7EVygIoEQ0w20k5KI-aBaYS-HXXD3eWKbiDvfjw1WVhiBCNmjZGGqy7OO7OwneNFFXf8GKMB-W6KCSSghvpMimmeG-YbrJN3tkw1ZfdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توهم وزیر جنگ تروریست آمریکا: تفاوت توافق فعلی با برجام این است که از دل قدرت آمریکا به وجود آمد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/660821" target="_blank">📅 16:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660820">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIi07duclle-5IaUw2E8R0JckhgUAi4HWZGudYWaGW93Etc1hosCoK0sv2mimXZiIDYz1-Ss8p5pW329i5N_-ed4DX-64WMD8CL4FjvGOMmci3vlIWk4-dXYKy0C81McGoNqfFh-eLbEVNkqaYvBxwXeh_lxnSXdmVXIuNc5p5ztCe6T-JJ-0ugg03UhVlhS5o861km8Us17t-LamV0p5IC9LV0OCkBx2e8Fj8Q__PwG9EBI3cMFJF0cyITq1mD5GXfFAtJ_a9GKKOYvhqgxZteLFHGHYiI0ycL-NFkgcjENJ94E_hl9pDH5uwQ3uyb4eehsacjMQ4snq9_Wu5oz_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رونالدو و مسی تنها بازیکنانی هستند که برای ششمین حضورشان در جام جهانی، نشان ویژه میراث را به لباس‌شان زده‌اند
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/660820" target="_blank">📅 16:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660818">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d83f88a49b.mp4?token=JIopd4r2WjtWWoZTnHJC0plEzCofX0AM1ZkA4OwbfFbNAM8BJ2NRjS7fgTdcKXm_QJ-Rr60zhxDODno3jK7QoAzkQgeqfh73XFBLAeMQffu7tWGbDYP0pJ4P2QyfjKfTP2jCC02XcL-icg7DHkp5uBZxiOpsMEr4iDei29t88UAu84VoHLRV6e08mMWPMSPW8gX1qiUdZ0g6tcggC_krQrHkHdEhVDqOR2IpQ7WlwOTW8lv9TJUs9O9fihrADKRAsGFykXC2H2jdEaGa2sozCIvzNo2e4YijTuiLb2waKdzrcrFs_lnnaY17-nfGRyuUcj56le6OUwc7cRAt7fGphg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d83f88a49b.mp4?token=JIopd4r2WjtWWoZTnHJC0plEzCofX0AM1ZkA4OwbfFbNAM8BJ2NRjS7fgTdcKXm_QJ-Rr60zhxDODno3jK7QoAzkQgeqfh73XFBLAeMQffu7tWGbDYP0pJ4P2QyfjKfTP2jCC02XcL-icg7DHkp5uBZxiOpsMEr4iDei29t88UAu84VoHLRV6e08mMWPMSPW8gX1qiUdZ0g6tcggC_krQrHkHdEhVDqOR2IpQ7WlwOTW8lv9TJUs9O9fihrADKRAsGFykXC2H2jdEaGa2sozCIvzNo2e4YijTuiLb2waKdzrcrFs_lnnaY17-nfGRyuUcj56le6OUwc7cRAt7fGphg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علم از دست علمداران نمی‌افتد، حتی در سهمگین‌ترین طوفان‌ها...
🔹
پرچم میدان احمدآباد مشهد که از روز ششم جنگ برافراشته شد، با گذشت بیش از ۱۰۰ روز حتی در طوفان‌ شدید روز گذشته استوار و سربلند در اهتزاز ماند.
🔹
پرچمی که، روایت ایستادگی، همدلی و عشق مردمی است که اجازه نداده‌اند نماد وطن لحظه‌ای بر زمین بنشیند و این چنین صحنه شگفت‌انگیزی خلق کردند.
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/660818" target="_blank">📅 15:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660817">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzJaus-kH275_AdguQJoEwySYhR-lLxzv8Tebr156U_9z3hKRfto_ws-N_Pe7QrOJGIRas_qZUtwXvytX__1O5PcwwE_d4nwtNXVAwri350-BSLKIvvjSqnnsfnjE1dh2e4-GLDVIid9k2UjWw7O1go44VNwFYx2IbSHFBo7aQ0uFuV7LMnWzqfFVkWjcoj5kI1lkCEEPIHHDcuwQGiufDGTd0YHvvzrflp9T_cimHavanH4Etc9V7RsEYrn7dWilMc5ZB63ZyFAvD-vjcj_WLGGDj_cca08Hfj_f5YeMPhe5DX8tNxd_86OznKqG70GLEO1CnhpKPYnUYQQU9xF-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستیار رهبر انقلاب: از مولفه‌های قدرت خود هوشیارانه مراقبت کنیم تا دستاوردها تثبیت شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/660817" target="_blank">📅 15:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660816">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPCTF4MpIjhFwhvk5_Pd82rv12oorVFypY2YVj4RLNkew2zsDL_Kyxc_wgjct0rceScA8DCIDyeMP587dzd1yd4Bfi2tVHh2MXl7pSaC5CiRJE-rsZk5Hy4EFX7pTCFudVUv40WFLOpe3QUvjYVP-bdm4GAJqaf6CRPAn8K-QO2h7lU_w7XT9WgImhOPsOIQVZVdiGGOvVbOQ2kOSfpXBA1wy1qCw0OOfM3zMfh2qUyJc4ka-uBn_POrt1-Msa9n_Wy1lqQdPhSR8sKHwqeEsfv4lTON1nRJRcE-vXVz34B8UeK5yRKEQahXk4Hm-0MgdzYMCw3UhoDqCsClqgpgog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: این یک سند تاریخی و پیامی از ایران مقتدر است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/660816" target="_blank">📅 15:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660815">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b25a6559.mp4?token=G7OTphPfF5VpGd_uzPTmD2HVh7hdg4ieQzcT8o4C9ldfQOmawcG8ap-5-CUQVheEVgw5crgrWZdsZsiXHza7dHmJ4y8D_b71yW4t8l6z_dZFmXeUUVUPnzKZZf4hqZrGXwvASKfeHD2K8_3MxYjmUte2LUbButGNrdmcrJEOY1z_j9f0xWwFGZs8_dtMa3OMiIWhCW3pDa7xZ2W9BYWjjLVdAjP2Lwd3uoyCcK7NtQOgCCVm4GAJDhlFrsVeRc3-uew4r918EdpjzXqZYD3xdYdStP9nB87J2irUta0r-vT4EOYR6lp3qgvmmV6lrpNx69wFxRT3ysCEDJYd0YmjXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b25a6559.mp4?token=G7OTphPfF5VpGd_uzPTmD2HVh7hdg4ieQzcT8o4C9ldfQOmawcG8ap-5-CUQVheEVgw5crgrWZdsZsiXHza7dHmJ4y8D_b71yW4t8l6z_dZFmXeUUVUPnzKZZf4hqZrGXwvASKfeHD2K8_3MxYjmUte2LUbButGNrdmcrJEOY1z_j9f0xWwFGZs8_dtMa3OMiIWhCW3pDa7xZ2W9BYWjjLVdAjP2Lwd3uoyCcK7NtQOgCCVm4GAJDhlFrsVeRc3-uew4r918EdpjzXqZYD3xdYdStP9nB87J2irUta0r-vT4EOYR6lp3qgvmmV6lrpNx69wFxRT3ysCEDJYd0YmjXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کپلر: کشتی‌ها همچنان مسیر ساحلی ایران را ترجیح می‌دهند
🔹
با وجود گذشت زمان از تنش‌های اخیر، الگوی تردد دریایی همچنان محتاطانه است و حجم عبور کشتی‌ها به حداقل تاریخی رسیده است. تا ۱۷ ژوئن تنها ۶ عبور تأییدشده ثبت شده و بیشتر کشتی‌ها از مسیرهای ساحلی ایران حرکت کرده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/660815" target="_blank">📅 15:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660813">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWCH5_7yiENQ3EvZVdFyWQbolKpDsx67_21wYe03owMUH_RPG0aI6O7M69f6jZ6kLAALCRxfzVBnCPsmKw0WJoRm0N3IjR_xrp7sQGXWBe_pHCd2DwYqzYa3qo7Ynuz9gsxktaG2MX91ZZh0nCTXpjaI3UO-OWsr4q8976io1IfIDV_FtGammK6kAXxwQM-uIMHB4e7iM7nw9Q-3J1WniVXuqTSjWzWHIuM6rO1BgDl5vbSClPyKa72cfxA1Mtq_FDLm7PXYOdIDYnK8L0sjSJFW02s14sxbJ7jvsjkFWk5VwVCyCNoSwgBEVBFaozcn_9Q8GB4uCGN02GyZybbRJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیشترین دریبل موفق در هفته اول جام‌جهانی ۲۰۲۶
🔹
آماد دیالو که تنها ۳۴ دقیقه فرصت بازی داشت با ۶ دریبل موفق، صدرنشین دریبل‌زن‌های جام است.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/660813" target="_blank">📅 15:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660812">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
سی‌ان‌ان از تلاش نتانیاهو برای اثرگذاری بر توافق آمریکا و ایران خبر داد
ادعای سی‌ان‌ان:
🔹
بنیامین نتانیاهو در تلاش است با استفاده از چهره‌های رسانه‌ای راست‌گرا و سناتورهای حامی اسرائیل، بر توافق نهایی آمریکا و ایران تأثیر بگذارد و بر ترامپ فشار وارد کند.
🔹
او انتقاد از توافق را از طریق چهره‌هایی مانند مارک لوین تشدید کرده و در حال لابی‌گری با سناتورهای نزدیک به خود است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/660812" target="_blank">📅 15:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660810">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRqRdpew9lx1AyfzuzpQh8DQdqRXrX2qMSKOZnNCb357iYh7TDUOVdPnCU5DoNIQhMhnaqpw_xUcut-9m3rvgROg6oX-ZbVMyw1rvYe7EsWFJ7ugXdsbHX8sZTbvBk7h9kafOYnN8liAsEay-5OOXfkkFIIJ5M7qdaAIe5JVP95N9tnSeg-Ll97O7iEH14yfF311dApfAve2ccddi6G5KJv9-P_F0ZX4xcQqctIUKc8hIvFG1xgZuNKcsxbuovSkYgYzvPv6wHQuyigIu9irBqZkEqX4RmEWgB3yYIZDRcqKY2axXrtvBf02oMdxxbtKD2YovsW49_aKKR_-M8ABPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنامه پخش روزانه خبرفوری
مطالب مورد علاقه خود را از طریق هشتگ‌های زیر دنبال کنید
👇
🧠
روانشناسی |
#سلامت_روان
| ساعت ۱۰
💻
آموزش سواد رسانه
|
#آگاهی_رسانه‌ای
| ساعت ۱۲
🥛
معرفی اصطلاحات مختلف
|
#واژه_کاوی
| ساعت ۱۴
💰
آموزش دنیای اقتصادی و سواد مالی
|
#دارایی_هوشمند
| ساعت ۱۶
👑
معرفی شخصیت‌های تاریخی
|
#نامداران_تاریخ
| ساعت ۱۸
📚
معرفی انواع کتاب‌ها
|
#فوری_کتاب
| ساعت ۲۰
🔸
نهج‌البلاغه
|
#نهج‌_البلاغه_بخوانیم
| ساعت ۲۲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/660810" target="_blank">📅 14:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660809">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1QDITFfpJ_scuGoIrt-lfGGom040hI58sI-D0PeDejuvxbgPT-wyj8TWgSgSQ0ucCty2UGQc8-ePgxtaLhF5EK8FjY8g6pPUUSoSlK68QG_EaajjQskNmi8Squ8C_XLvugY08sdzOHneC5w81k2jJRSs_zWDstYUtQ36gACgLfx-uT0IYHUrIFLHY2xpVN40KQJRiD0EHyQh3qI25LCn9CT19MmV6CfaHzn-CFGvFxiZp6KMhrlAaxqfroDzF-h5OT6htHi1Brd4c2GXQQ6N_TeK3_xxEeylowCb8q0EOaSg0x4hqy-LcGhw77PFCMAEYIMP6-_AklhLN9I9mkw7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تأکید بقایی بر مسئولیت ایران در بازگشایی تنگه هرمز
سخنگوی وزارت امور خارجه:
🔹
همان‌طور که در طول مذاکرات نیز تصریح شده، بازگشایی تنگه هرمز بر اساس تفاهم‌نامه، صراحتاً بر عهده طرف ایرانی است.
🔹
مطلقاً نیازی به هیچ‌گونه مداخله از سوی هیچ طرف خارجی نیست. هرگونه مداخله از این دست، صرفاً وضعیت را پیچیده‌تر خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/660809" target="_blank">📅 14:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660807">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاطلاع‌رسانی بانک سینا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBLtJtnnoQQjVGGEcz5i0n-NMkpzz0P30pal5zLkbbo3piStMjrB6U3juWashpNnI5J6R63xyflOwLT73pcNYtgrLvfXSLnXTH5jlZlhjG467nLUu8tIUSnsds4M9WkiMMU2reVtBT2OU2cxKtJAoWcOzkp4bLo9onH4b5hkIxY7JApzQoB8jESD1S1NP5P75lozLjJfNqXhEt8GRDkoczBm7hEegqFUpAcOR8gbEouI57Ph7iWrP57tp_a8w1tkCGGuR0ZGERubLTH14ibRg7_2jgEB4I5oXOSN05AiPa6YlzhUQdoc-zoHhG5kJPWsYCRlYMGsF2aFr4dq3IEGRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بانک سینا به رتبه دوم شبکه بانکی در ارزیابی سامانه آرش ارتقا یافت
🟨
بر اساس آخرین گزارش اعلام وضعیت بانک‌ها در سامانه آرش بانک مرکزی جمهوری اسلامی ایران، بانک سینا با بهبود عملکرد در شاخص‌های ارزیابی این سامانه، برای اولین بار به رتبه دوم بانک‌های کشور ارتقا یافت.
🟦
ارتقای جایگاه بانک سینا در این رتبه‌بندی، بیانگر توجه مستمر این بانک به بهبود فرآیندهای پاسخگویی، صیانت از حقوق مشتریان و ارتقای کیفیت خدمات به مشتریان بوده که نتایج مطلوبی به همراه داشته است.
🟨
گفتنی است این بانک، ماه گذشته نیز در ارزیابی و رتبه‌بندی بانک‌ها بر اساس مدل ارزیابی کملز (Camels) که توسط بانک مرکزی صورت گرفت، برای دومین سال پیاپی جزو پنج بانک برتر کشور شد.
▫️
@sinabank
| بانک سینا
▫️</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/660807" target="_blank">📅 14:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660806">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tscXyjq0rQG6g7Mo3mqQJKAmYx0IE5i3ehRzm6N_G_Y7AOv7PZqldHSe3uUbeMLY7d8KSz2EzZ-_cp3i71mqT3bWWpMFP4lKTFqOUoJ3pf6_c_zC67KDlWHPlt_u9sp3iunGM1Jsess_RTXjt9yMALBMZ40pQPzx2CmWnCd8zTJl4uyJG9vCX7fTIBx1KoCd1j4Chc9kw9n88csw8ylIJMEKkeergtcECnYVvT5qDkZcAGEoMBCZ7ruIGY12UAb1CrCB5EWcvCXtOZQU1FqKkuxi0s3_2oms6-YXUxCNihq9Ye8PUVoxQ2B1gOCc0D6PCtF3G25K64awMAnoMLmyTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دروازه‌بان‌هایی که بیشترین فالوور رو در جهان دارند
🔹
ووژینیا، دروازه‌بان کیپ ورد پس از عملکرد فوق‌العاده‌اش در مقابل اسپانیا. تعداد فالورهایش از ۵۰ هزار نفر به ۱۱ ملیون نفر در عرض چند روز رسید.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/660806" target="_blank">📅 14:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660805">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNYq4Oy-0mp2tRJRp8IgFqoD5Nqh19rG_LnGbwi23qJ_Q8NoRDas2tGZXYrcO9xYDKromt31dfjiH_DsUqxIyPwPj3M5INZMT7s412jFeKFe9BDfUqGCpkEMhB1ZVAjmxilXTSG-0x55xDH0FuyMwppHJ0D-w_Iz1U4Ko20r3JjquXV288LA-fB9y7TN-HL-PvE1uQ-ScgITMfXS_g9CLN42hGy8om2wgDbV71sOghiBdvc9xbyiguZSggxsikYuSQd1G4U1ltyzyhovlU_GGLSzncGwXWFQC3OG20ekC7oRaU1ohT5xYOfcZqOd2csPMeBiAcF-B5N6ALFoz9QgvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: این یک سند تاریخی و پیامی از ایران مقتدر است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/660805" target="_blank">📅 14:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660803">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb1bea6b1.mp4?token=YoVi9baxaBkdVcAIWU9TuqYVWIBnuvKVnJgWBdrTe8af9w8Kuh-YEjC2Gp0YRJpu0Em4-JRlXhZrwltvzaduMC-bvPZyJkeKiceCoSLWeeh1EaChUHH0QJvz7TVW-rLCqwxUeY8FoR5YvY7qXiyzjCwwfEfdy4wUDHk1L6ZjHQBvvw_Ez695UhLZp6uGzEUXoJUm1WvuWPZpZ7akRjPGDdphoTyHX5N_CovfnGMo9xK5fPyJ89PrYDVyT_tIg-zMDL7Fkrhc--qU1-Qok8_hWmcb7p11U9AreXXVO1YaLQnH4Gk3s5Lr0w1Hz6eWtGRV1xkrw21_iUOGOk2jm65dsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb1bea6b1.mp4?token=YoVi9baxaBkdVcAIWU9TuqYVWIBnuvKVnJgWBdrTe8af9w8Kuh-YEjC2Gp0YRJpu0Em4-JRlXhZrwltvzaduMC-bvPZyJkeKiceCoSLWeeh1EaChUHH0QJvz7TVW-rLCqwxUeY8FoR5YvY7qXiyzjCwwfEfdy4wUDHk1L6ZjHQBvvw_Ez695UhLZp6uGzEUXoJUm1WvuWPZpZ7akRjPGDdphoTyHX5N_CovfnGMo9xK5fPyJ89PrYDVyT_tIg-zMDL7Fkrhc--qU1-Qok8_hWmcb7p11U9AreXXVO1YaLQnH4Gk3s5Lr0w1Hz6eWtGRV1xkrw21_iUOGOk2jm65dsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
از مساوی پرتغال تا چهارتایی کرواسی؛ دور اول حوصله کسی رو سر نبرد
🔹
قسمت پنجم برنامه جام تایم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/660803" target="_blank">📅 14:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660802">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1irBYp7WVhUwrOsdWPFGeJ3YCPRpxjqa0YprG9u62CiZ0zvfq8inXlqcWhhc0kNFbuKhhjg3Gtl5aAdWyY8uPpag2cGb-1gC0k_KXg8JV2g2T5kB4aszrHrgJAnB3PMWJXnwjzSJ8SB7vs9eckbaiTOo4ETuwHrVhDJSDwhoL4YsV6pv33a28xA9_4IPhTBkgmjH29k5ntlznt8lS2Tvlw9UBWYpHwUO6eKwhfoztiazoeKu48FeJyL4B9ELYBvtgpUp7no-MXk-kpQG6ipN4SK37C_AYbeATtzChNBPBXIob2vJEwlbvPapHyCv5JeNQ_jC1M7Pk2JDd80qSdPCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کشورهایی بر سکوی المپیادهای جهانی ایستاده‌اند؟
🔹
چین در هر پنج المپیاد جهانی ریاضی، زیست‌شناسی، شیمی، فیزیک و انفورماتیک رتبه نخست را در اختیار دارد.
🔹
ایران در چهار رشته از پنج المپیاد، در میان ۱۰ کشور برتر جهان قرار گرفته است.
🔹
فهرست برترین‌ها نشان می‌دهد کشورهای آسیایی سهم پررنگی در صدر جدول المپیادهای علمی جهان دارند.
@amarfact</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/660802" target="_blank">📅 14:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660801">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQwcjxsIoXZXD1SRUX20xP1Rz35xtV1B7S5Dy07-W_Fdw3cyg3xNBbOh9L72ScrByefdZzRlK0F2QJ-N_Yj8etS-iIbapz-gSiIPRsh0cBMuYHYHo8wQAAHpbcRRha0kNb9gQ2eECJHbUXaWk3hkMTjQDO0MdX8LYLjjGeXlmzZBpm-PfLd01y-iDwMKxwAu39APlGnPGNxLrm6neBSDdATrIQ913VqF6BTRoCxGQjw8JDt_xLJBz5Qi0B8kwDO5qHWQjIfW1jlnqo3Z0o6r2MH2raVuuwfJVqZsPNHiuF57MSO8MGghlgFbzFkooD3d9owZHIBrtnEramZxD2kuDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استقبال گروسی از توافق: اکنون نوبت کار فنی است
مدیرکل آژانس بین‌المللی انرژی اتمی:
🔹
خوب است که این تفاهم‌نامه (آمریکا و ایران) وجود دارد. اکنون کار فنی آغاز شده است. اکنون زمان آن رسیده است که با همکاران آمریکایی و ایرانی خود بنشینیم و تدوین گام‌های مشخصی را که باید برداشته شود، آغاز کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/660801" target="_blank">📅 14:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660800">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uX054MQLcv1cQ1g5BSMab4ybSnlaj5gsnFejsWTbK3hLSRMmKYOE7R_qPPNwSyL49hABOFQN3v5hLHlLRdcp6E-wdQoAjG0ZWN0-DcswxfGPMFitScLcfGqIMXERqBzzHhBzB4D8YhEWxZvT_ujEF995faxnW36Y5z5iuFsKwqTMroabsPgeMcjFPrzkso3Mg9fZ2D5DZ8sFz0BtihETkO98-dQYqhYUhggnDRQyrr0Z7yc35NnAXNTfWtWAI6fHmk6r1FvIso3pXvF7MiqeCqqahd6_ld19cGU_lFr758-heuS6h7mP82kxeV4eedb1hAQvS_Ld5cXhhqyXukZ5Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«آندرداگ» رو زیاد شنیدیم، ولی دقیقاً یعنی چی؟ #واژه_کاوی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/660800" target="_blank">📅 14:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660799">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
تیزر قسمت هفدهم از فصل چهارم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ خانم راحله خمسه که به دلیل تصادف شدید در دوران دانشجویی روح از جسم جدا شده و بخاطر تجربیاتی که در برزخ داشته‌اند تغییرات چشم‌گیری در نوع حجاب و رفتار ایشان بعد از کما رؤیت می‌شود و همچنین ارتباط با ارواح بعد از بازگشت به دنیا ادامه یافته را نظاره می کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: راحله خمسه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/660799" target="_blank">📅 14:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660798">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtoGemK0-8IMtjRht_17akmdNDgLTEn-oaZteZnDRN0tIcBiNXWkDMs9h7ri5vGzHACPDSQZJExnoyZVo8kvf5adl4wtFp82YcSu9WrfYYLHtbPDP7Z7leO9AK-SKLs356gZyplhG57h2lZLKmT-yACXP96q5cW67ax8xsSo2mvD1CV-9y4iDWW4AnyartzMiPwv3F8PlNbqsq76efvaYYPCBQIho3CfyZyLdC_BDwJ6ld9u59stDNiFLY2d0cqP8xUwDmR9b4iY1sbHY6fFc_LPmWhrTROlY5ADlslRvt-nDVeb5WiAfDN9hOCoIJ1e3KGI9koV04N3sBtO3yjwJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری که آمریکایی‌‌ها زیر پست‌های جمهوری‌خواهان و جنبش MAGA دارن منتشر میکنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/660798" target="_blank">📅 14:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660796">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7Lha3sCsoX7_yeeQMqH9N72uhkeyT1f1gmzlFSu6jUArAdtRyEC-7DTibg5j4ZgamTyYoAixVwKHDr3XrWX_Hfyn5i02ikAGa35HKhXbiavMe-WoNA0Wh-jOoLSZNVf_L2JexeF8xNF20KQrJ63UqQqtGmCURs8MWJ5Zgy_FIz5a1_lcb2H1VhP8WLFYu8UxYjetDgIwd-YDstz6f-NSnrAaaHrMJyT6Lp4RD-NhsIRX2En0TW6o3I6dni5d23sX4S1t0FnMPjGXWi34YzD_aAOnvWqdK459IkDtMNT9AR0jLkVJkVvBhtD2BukMNMqFnuDhoRUfVYht1FdIkLycg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/660796" target="_blank">📅 13:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660795">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
سکوت معنادار نتانیاهو پس از انتشار سند تفاهم ایران و آمریکا
🔹
بیش از ۱۲ ساعت از انتشار رسمی سند تفاهم ایران و آمریکا گذشته، اما نتانیاهو که پیش‌تر از «پیروزی کامل» سخن می‌گفت، هنوز واکنشی نشان نداده است.
🔹
همچنین برخی گزارش‌ها حاکی از نارضایتی نتانیاهو از مفاد تفاهم، به‌ویژه گنجانده شدن موضوع لبنان در چارچوب آتش‌بس است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/660795" target="_blank">📅 13:50 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

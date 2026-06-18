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
<p>@akhbarefori • 👥 4.49M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 17:57:40</div>
<hr>

<div class="tg-post" id="msg-660858">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 21 · <a href="https://t.me/akhbarefori/660858" target="_blank">📅 17:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660857">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
گفتگوی تلفنی سران ایران و پاکستان
🔹
پزشکیان: تلاش‌های پاکستان در مسیر دستیابی به توافق پایان جنگ در حافظه ملت ایران ماندگار خواهد شد.
🔹
شهباز شریف: صبر، استقامت و رویکرد مبتنی بر عقلانیت و تدبیر مسئولان و ملت ایران ستودنی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/akhbarefori/660857" target="_blank">📅 17:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660856">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ایهود باراک: باید نتانیاهو را با چماق از نخست‌وزیری کنار بزنیم
🔹
ایهود باراک در مصاحبه‌ با شبکه ۱۲ اسرائیل تأکید کرد که احتمالا نتانیاهو در آستانه انتخابات رژیم، به لبنان حمله خواهد کرد، و در تلاش است یک جنگ ابدی را با ایران و حزب‌الله آغاز کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/akhbarefori/660856" target="_blank">📅 17:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660855">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ترامپ به شبکه کان: احتمال خوبی وجود دارد که از نتانیاهو در انتخابات حمایت کنم، اما منتظر هستم تا نامزدهای دیگر را بشناسم. او باید منطقی‌تر باشد
/ انتخاب
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/akhbarefori/660855" target="_blank">📅 17:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660854">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/akhbarefori/660854" target="_blank">📅 17:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660853">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
بقائی: بازگشایی تنگه هرمز بر اساس تفاهم‌نامه بر عهده ایران است
سخنگوی وزارت امور خارجه ایران:
🔹
بازگشایی تنگه هرمز صراحتا بر اساس تفاهم‌نامه بر عهده طرف ایرانی است و هرگونه ادعای دخالت خارجی را رد می‌کنیم.
🔹
مطلقا هیچ نیازی به مداخله هیچ خارجی نیست و هرگونه مداخله‌ای صرفا اوضاع را پیچیده‌تر می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/akhbarefori/660853" target="_blank">📅 17:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660852">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
ادعای منابع پاکستانی: ایران به پاکستان اطلاع داده دیگر نیازی به برگزاری جلسه حضوری در سوئیس نیست/ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/akhbarefori/660852" target="_blank">📅 17:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660851">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
لغو سفر شهباز شریف به سوئیس  الجزیره:
🔹
سفر برنامه‌ریزی‌شده شهباز شریف، نخست‌وزیر این کشور به سوئیس، بدون اعلام دلیل رسمی لغو شده است.
🔹
این سفر که قرار بود در دستور کار نخست‌وزیر پاکستان قرار گیرد، به طور ناگهانی و بدون ارائه جزئیاتی از سوی دفتر شهباز شریف…</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/akhbarefori/660851" target="_blank">📅 17:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660850">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGlbQkKB_rJX_rrXphSM5ksZy6uuB7l28GPIKhcVuekXnuXDVj8ed4Opz2BzxGlrr4PgaNuiTNP-mPkc89CDuON13MObOrEFOej04nSEXsIBOZV7t0XVbZStbq9RG8kM8mxgyClsMvqkLTeufN7sbNk7wTQ-xnwRXYwqkjKrxaQ5UydR5b8f2VxPMp0uN3tc6s8y50JH_CEL6SAAEMBO37VKIJI89WWZcJt6icLQyLSKT4OhJxfOWNiJ_WuNYE058YPCMaSQ-JDy8EcNyOeg4Oxtt72ksjRNvi_vOGNU1_XcsIyeaikK1Qi_l75lfVe0wDwIZHgCrMcCy56aZS_I8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست جدید ترامپ: قابل شما را نداشت!
🔹
نفت در جریان است، ایران هرگز نمی‌تواند سلاح هسته‌ای داشته باشد (جهان امن خواهد بود!)، بازارهای سهام در حال رونق هستند، مشاغل رکورد زده‌اند و قیمت‌ها در حال کاهش هستند (توانایی خرید!). کشور ما قوی، امن و محترم‌تر از همیشه است. قابل شما را نداشت!
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/akhbarefori/660850" target="_blank">📅 17:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660849">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/akhbarefori/660849" target="_blank">📅 17:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660848">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/akhbarefori/660848" target="_blank">📅 17:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660847">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
ادعای اطلاعات آلمان درباره ایران
🔹
بر اساس گزارشی ۱۴۰ صفحه‌ای که به تازگی منتشر شده، سازمان اطلاعاتی آلمان مدعی شده ایران به عنوان یکی از چهار بازیگر فعال خارجی در زمینه «جاسوسی در برلین» فعالیت دارد.
🔹
این گزارش همچنین روسیه، چین و ترکیه را به عنوان دیگر بازیگران اصلی در این عرصه معرفی کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/akhbarefori/660847" target="_blank">📅 17:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660846">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVf4tQb4x-r4tK52nfDK3ACiULgpQ3AVIaQyXcZbqze-Klzm-01yHcAxUanan15kMZ3Fw-9ZF9w2CYyFp-UyDYlXeoMgq7ax1yrzOVtCs26UtJO1o8TorQICGLFj_zJOymSfVW9ZdkKJH1WlFos3lr6ga8MkhJ_csN1OUZc7dq57-XpscBCvhwi_-mCtVnsIGJhOl5QrK7K1lROFrFmyamU1UuIIOovS0cY3ZjKR216ZKlESyC2k1y_uziiGgqV4Ra5OVmRB5V7fhn5lCKdw-6jt1qwAFkBbebQJ0IBC8WilSZCsCpQHthXCHxXt8sVS1U5FZvsqv-ez57mVP66iMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاخ ورسای فرانسه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/660846" target="_blank">📅 17:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660845">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/660845" target="_blank">📅 17:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660844">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
امارات شبکه‌های اجتماعی را برای افراد زیر ۱۵ سال ممنوع کرد
🔹
براساس این مصوبه، کودکان زیر ۱۵ سال حق ساخت حساب، کامنت گذاشتن و اشتراک‌گذاری محتوا را ندارند و پلتفرم‌ها موظف به حذف اکانت‌های آنها هستند. نوجوانان ۱۵ تا ۱۶ ساله نیز تنها با نظارت والدین و کنترل‌های شدید به این برنامه‌ها دسترسی خواهند داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/660844" target="_blank">📅 17:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660843">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/660843" target="_blank">📅 17:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660842">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kk22sBu3P8QfQoUYG8pYfB-lLMYxHNUugPgsr92cekX4hdBduiybE9iRzkjebJVhZjLMcJacnxr58z5DTS1NuZA5x1kzEiPNxs9dp2honFKBMb04dwI-pTDDSvSygYE9Y9MG8stu0ys6bEf_yh1DVuJOanEMlvuP6Mx5c1gW1ICrcmi1arqSvKmCx-9ltTrNfoEvFN3v7678P5g9v8CTFcN2jc89YLLqETgaF7IHwjTXSslbJ-3Lzztb9Q0YRxUCJO5WOG1XmdQAaUt26KjFyzzb59ZD_TG1lUoU4aS9fk9M9qpYLt5VERKtY8_krQn84E9XR9ZiPUUJ0Et4TxpsZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جان بولتون: توافق آمریکا به معنای واگذاری کنترل تنگه هرمز به ایران است؛ اکنون تهران می‌تواند جریان انرژی را مانند کلید برق قطع و وصل کند....
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/660842" target="_blank">📅 17:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660841">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
وندی شرمن: دونالد ترامپ به نظر من عملاً در برابر ایران تسلیم بی‌قید و شرط شد...
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/660841" target="_blank">📅 17:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660840">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/660840" target="_blank">📅 17:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660839">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/660839" target="_blank">📅 17:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660838">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
وضعیت عجیب «بازار رضا» بعد از بارش سیل‌آسای دیروز مشهد
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/660838" target="_blank">📅 17:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660837">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/660837" target="_blank">📅 17:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660836">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/660836" target="_blank">📅 16:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660829">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
حملات توپخانه‌ای ارتش اسرائیل به جنوب لبنان
🔹
ارتش رژیم صهیونیستی در ادامه تجاوزات خود، ارتفاعات علی‌الطاهر در جنوب لبنان را هدف حملات گسترده توپخانه‌ای قرار داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/660829" target="_blank">📅 16:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660828">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
سوئیس از برگزاری مذاکرات اولیه ایران و آمریکا در جمعه خبر داد
وزارت امور خارجه سوئیس:
🔹
طبق برنامه، ایران و آمریکا به همراه میانجیگران پاکستانی و قطری و برخی کشورهای دیگر، روز جمعه در بورگن‌استوک برای مذاکرات اولیه درباره اجرای توافق دیدار خواهند کرد.
🔹
جزئیات بیشتری از این جلسه اعلام نشده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/660828" target="_blank">📅 16:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660827">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
پوتین: یادداشت تفاهم ایران و آمریکا می‌تواند مبنای توافق‌های آینده باشد
رئیس جمهور روسیه:
🔹
امضای این یادداشت تفاهم توسط دو رئیس دولت (ایالات متحده و ایران) مبنایی را برای ما فراهم می‌کند تا انتظار داشته باشیم که این یادداشت تفاهم، پایه و اساس توافقات آینده را تشکیل دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/660827" target="_blank">📅 16:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660826">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/660826" target="_blank">📅 16:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660825">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcIhRDUs9wMZvOlt1EyGtyt7z3pp1MfHszR9OevlTbBS456LvxRNgKxW_uESqZwmp8oLoYM2FqyylxkpS-0SFTZnOuJlJhnjQZEMVe6bxouT0UoWyB4hRNM_jSyBn1OKrjgJcfhzQFuvPQYJFlfxez0g1Eve9_-gTUxgefmOR6f-kbKWyG_pPWtHnZ0pjE2Ugde7AtU83KfIY32C8WOKtrQbnheE5sD37tl-FQA6OSH1TqedQ8BBGQ_sDv9HygQbHoA3M7qCKhRWXxHcPrUbabsw6HVr6tlnmq8jLt21AJ81MLcrdKoHm24EdTaXZelQ0HKrHlTGeIVa1OuVccEi5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶۹٪ آمریکایی‌ها از مسیر حرکت کشورشان ناراضی‌اند
🔹
طبق نظرسنجی مرکز تحقیقات پیو، ۲۹ درصد از مسیر حرکت آمریکا راضی و ۶۹ درصد ناراضی هستند.
🔹
براساس این پیمایش اکثر آمریکایی‌ها  انتظار دارند اقتصاد ضعیف شود، کشور دچار تفرقه بیشتر شود و ایالات متحده تا سال ۲۰۵۰ اهمیت کمتری در جهان پیدا کند.
@amarfact</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/660825" target="_blank">📅 16:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660824">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Osh69XRfEwIO_UiVrFiiCB_cBU_Ds38GR2bvOCTWnjP2kT0gYE-2Lu0pXS7YY2C_2tWuxRqRN9rIoLK28T8nuXjVezd9LE0bJD7DQAn22_j-NWgmHvPrtdGcNKwl8ZDlDLpvo5Q0XXzkaPE1SrvJjMFRon5LE0OgTL0So47oXvnF6RmhKH71zcTWE3QPntpyoAuPshD9i5JVGqkSTLSjTUK3FjwlvchukX8Wu_MNzQlXx2ywHqiwmTiKnOR-NSrq40fH7oDhE3NJ179eekT4deMPsB--mvuyURUMZ9CyLzRrsMR3SdZvgnD0D2g5hkEiaxFHgHojUlq8TcQGJvnsnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۸
تکه یخ جادویی برای پوستی شفاف، درخشان و بی‌نقص
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/660824" target="_blank">📅 16:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660823">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmNFDRZ5MI5UKjiyeD1IRvbsG_PWd94otCisKrUbxD_xKMEQ_KUFfpR8t7cqMChWUjJ21Q9nh0FIwkpRNY9LqhUipka9SNvGFsbioeBn8Z0kIpFsBCYkZ1TxZ3rHyEL3waD1UlDiV6j7w2vqE_a_28X1TrMDknJUL6fbr2qb4hqumZTunjqXFBGHiSqnd-A3T1kAW8vFA3SbAoNAQ_Ak3GaH6m8VSEQ49S9zMmhLXugjV-Pq1HZPXYfTgDdoC-fzpOhE0ovpeYFZn2VFd_KC4FNHCLGnsSnwsLT-YLgB46-3AzhKVMlFKY9Ecxenaysodh24PKhi7wFJp9nDM0iVoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارتش رژیم صهیونیستی: بنا به نیازهای عملیاتی، نیروهای ما در منطقه امنیتی ۱۰ کیلومتری عمق خاک لبنان مستقر شده‌اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/660823" target="_blank">📅 16:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660822">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3u990wlyfBMhJN9Y54kOZglDLFarGbntigfGhpoFFQG2OTYcJTIuQ1Krv7HtM6znN3adNNRTevebECZKDFt8ViUHyEb6dm9PHifPewLNz2TfbPtIc8wfUJjh45z7y-6GToTOjuGQzu9qU4zV8cSlcYJ26mvX2vHEN1ZiLZ3xvnmCBFfhxeqhN3kfGxg3mp9xTPhFK2xEzNAyVp4YUC4y1aJ2bYCrkNAEckHNQ9RIL8OyN5Y3EC7ojELrpPl9cujvXqXX1moU3jZ0P4iOPU4s1ylv1KuSVKocucNd_6WkIR5kKhMdDuFRkoL0Q55WiiB7mW1cvFa_RZI9D1cMHk4iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
داریو هررا، داور آرژانتینی، قضاوت دیدار مقابل بلژیک را بر عهده خواهد داشت
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/660822" target="_blank">📅 16:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660821">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/660821" target="_blank">📅 16:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660820">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIi07duclle-5IaUw2E8R0JckhgUAi4HWZGudYWaGW93Etc1hosCoK0sv2mimXZiIDYz1-Ss8p5pW329i5N_-ed4DX-64WMD8CL4FjvGOMmci3vlIWk4-dXYKy0C81McGoNqfFh-eLbEVNkqaYvBxwXeh_lxnSXdmVXIuNc5p5ztCe6T-JJ-0ugg03UhVlhS5o861km8Us17t-LamV0p5IC9LV0OCkBx2e8Fj8Q__PwG9EBI3cMFJF0cyITq1mD5GXfFAtJ_a9GKKOYvhqgxZteLFHGHYiI0ycL-NFkgcjENJ94E_hl9pDH5uwQ3uyb4eehsacjMQ4snq9_Wu5oz_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رونالدو و مسی تنها بازیکنانی هستند که برای ششمین حضورشان در جام جهانی، نشان ویژه میراث را به لباس‌شان زده‌اند
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/660820" target="_blank">📅 16:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660819">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
استقبال قطر از تفاهم تهران و واشنگتن
🔹
وزارت خارجه قطر از امضای یادداشت تفاهم میان تهران و واشنگتن، توقف عملیات نظامی و تضمین آزادی دریانوردی استقبال کرد و آن را زمینه‌ای برای ادامه مذاکرات دانست.
🔹
همچنین از تلاش‌های پاکستان و دیگر طرف‌ها برای کاهش تنش قدردانی شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/660819" target="_blank">📅 15:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660818">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/660818" target="_blank">📅 15:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660817">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzJaus-kH275_AdguQJoEwySYhR-lLxzv8Tebr156U_9z3hKRfto_ws-N_Pe7QrOJGIRas_qZUtwXvytX__1O5PcwwE_d4nwtNXVAwri350-BSLKIvvjSqnnsfnjE1dh2e4-GLDVIid9k2UjWw7O1go44VNwFYx2IbSHFBo7aQ0uFuV7LMnWzqfFVkWjcoj5kI1lkCEEPIHHDcuwQGiufDGTd0YHvvzrflp9T_cimHavanH4Etc9V7RsEYrn7dWilMc5ZB63ZyFAvD-vjcj_WLGGDj_cca08Hfj_f5YeMPhe5DX8tNxd_86OznKqG70GLEO1CnhpKPYnUYQQU9xF-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستیار رهبر انقلاب: از مولفه‌های قدرت خود هوشیارانه مراقبت کنیم تا دستاوردها تثبیت شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/660817" target="_blank">📅 15:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660816">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPCTF4MpIjhFwhvk5_Pd82rv12oorVFypY2YVj4RLNkew2zsDL_Kyxc_wgjct0rceScA8DCIDyeMP587dzd1yd4Bfi2tVHh2MXl7pSaC5CiRJE-rsZk5Hy4EFX7pTCFudVUv40WFLOpe3QUvjYVP-bdm4GAJqaf6CRPAn8K-QO2h7lU_w7XT9WgImhOPsOIQVZVdiGGOvVbOQ2kOSfpXBA1wy1qCw0OOfM3zMfh2qUyJc4ka-uBn_POrt1-Msa9n_Wy1lqQdPhSR8sKHwqeEsfv4lTON1nRJRcE-vXVz34B8UeK5yRKEQahXk4Hm-0MgdzYMCw3UhoDqCsClqgpgog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: این یک سند تاریخی و پیامی از ایران مقتدر است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/660816" target="_blank">📅 15:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660815">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/660815" target="_blank">📅 15:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660814">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8068006920.mp4?token=hC-O6sn3pWHJ0EKYssFLIC7vfqIjTGhspKM3wyoiuSAsRYnP48-TzOxzVM4EnETNvla4qJ0wCYOuNtl4e7lA4Tre60pkIvFR_dAdE5AAMv9OVNhGGLbESPMT8E-Xbm_VutqfigT2vnoJPmGtBotHJPSmE45AyJdurey5clL2RQbNWe7tlYj0M7h5yDHWoZi7dGnBxVFou6aNgrtZFXxw0hpUTpCeXh0q78_LmZWV30uE8KjdoLgyG3DDbbJhSP699lZ08_8oBUUUGDvV3vP45ViQwPkfwUfUEdhI1V_gJCnYda2uPdtmCEgD_-yB9yhH0ZnFd__hZ863EDbkJsQsZjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8068006920.mp4?token=hC-O6sn3pWHJ0EKYssFLIC7vfqIjTGhspKM3wyoiuSAsRYnP48-TzOxzVM4EnETNvla4qJ0wCYOuNtl4e7lA4Tre60pkIvFR_dAdE5AAMv9OVNhGGLbESPMT8E-Xbm_VutqfigT2vnoJPmGtBotHJPSmE45AyJdurey5clL2RQbNWe7tlYj0M7h5yDHWoZi7dGnBxVFou6aNgrtZFXxw0hpUTpCeXh0q78_LmZWV30uE8KjdoLgyG3DDbbJhSP699lZ08_8oBUUUGDvV3vP45ViQwPkfwUfUEdhI1V_gJCnYda2uPdtmCEgD_-yB9yhH0ZnFd__hZ863EDbkJsQsZjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اندیشمند برجسته آمریکایی: ایران نه‌تنها در نتیجه این بمباران‌ها سقوط نکرد، بلکه از آن قدرتمندتر بیرون آمد و بر تنگه هرمز مسلط شد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/660814" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660813">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/660813" target="_blank">📅 15:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660812">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/660812" target="_blank">📅 15:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660810">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRqRdpew9lx1AyfzuzpQh8DQdqRXrX2qMSKOZnNCb357iYh7TDUOVdPnCU5DoNIQhMhnaqpw_xUcut-9m3rvgROg6oX-ZbVMyw1rvYe7EsWFJ7ugXdsbHX8sZTbvBk7h9kafOYnN8liAsEay-5OOXfkkFIIJ5M7qdaAIe5JVP95N9tnSeg-Ll97O7iEH14yfF311dApfAve2ccddi6G5KJv9-P_F0ZX4xcQqctIUKc8hIvFG1xgZuNKcsxbuovSkYgYzvPv6wHQuyigIu9irBqZkEqX4RmEWgB3yYIZDRcqKY2axXrtvBf02oMdxxbtKD2YovsW49_aKKR_-M8ABPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ب
رنامه پخش روزانه خبرفوری
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/660810" target="_blank">📅 14:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660809">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/660809" target="_blank">📅 14:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660808">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfeae072c7.mp4?token=J7xN3QXz8-_7uCBdGt1FhNmNTN93zqdfOjjB_a1OWOnfHvn59qvqzGZaA6hOfqHZA6ZsiKmmlWxykytc52HFdBN4kv4y2NyQbItibpJQEvAhh6IO7iTgyv_3x9mrgnYxM71MOHbngqR_WOEsI_DZx5sp_0WwPEE6xBHmd6RFiAbSg0lO4QT2gxXagrlqmfScoezFAQMjFXdJGQLXTV8pRIyzELtqcGHDTGJB8OhWxjq0jWtWnrhfBZ5QuYG-PCRojHpsBZbDIUsN03WzUSo8ZRjRYuN_EBTwTC8EHi9IU6TubBeAmUNTMQdggl1zxl6sVJ49TPJLcwh5Xn9cDtV2ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfeae072c7.mp4?token=J7xN3QXz8-_7uCBdGt1FhNmNTN93zqdfOjjB_a1OWOnfHvn59qvqzGZaA6hOfqHZA6ZsiKmmlWxykytc52HFdBN4kv4y2NyQbItibpJQEvAhh6IO7iTgyv_3x9mrgnYxM71MOHbngqR_WOEsI_DZx5sp_0WwPEE6xBHmd6RFiAbSg0lO4QT2gxXagrlqmfScoezFAQMjFXdJGQLXTV8pRIyzELtqcGHDTGJB8OhWxjq0jWtWnrhfBZ5QuYG-PCRojHpsBZbDIUsN03WzUSo8ZRjRYuN_EBTwTC8EHi9IU6TubBeAmUNTMQdggl1zxl6sVJ49TPJLcwh5Xn9cDtV2ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تازه ترین اخبار از تنگه هرمز؛ روایتی از دست برتر ایران و کشتی‌هایی که از تنگه عبور می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/660808" target="_blank">📅 14:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660807">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/660807" target="_blank">📅 14:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660806">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/660806" target="_blank">📅 14:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660805">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNYq4Oy-0mp2tRJRp8IgFqoD5Nqh19rG_LnGbwi23qJ_Q8NoRDas2tGZXYrcO9xYDKromt31dfjiH_DsUqxIyPwPj3M5INZMT7s412jFeKFe9BDfUqGCpkEMhB1ZVAjmxilXTSG-0x55xDH0FuyMwppHJ0D-w_Iz1U4Ko20r3JjquXV288LA-fB9y7TN-HL-PvE1uQ-ScgITMfXS_g9CLN42hGy8om2wgDbV71sOghiBdvc9xbyiguZSggxsikYuSQd1G4U1ltyzyhovlU_GGLSzncGwXWFQC3OG20ekC7oRaU1ohT5xYOfcZqOd2csPMeBiAcF-B5N6ALFoz9QgvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: این یک سند تاریخی و پیامی از ایران مقتدر است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/660805" target="_blank">📅 14:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660804">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3660da3d6.mp4?token=ANU93xqDllcAjcMH3EKbatR2y_-skM0aifGeTt6RYiRj9MmF2B5FgAPpwB6F1LoDkww1sExhCEJMhueOOG12PAjsS0aeGWHMeEeOAuz1KimCKilIthnxGu8d4zGsNy1xUWtfMSjgwgvADFe3xiid55YLCrxJe78VS2R670eyP6zASDbMqSmPZQYb3myi1Mhjis8aDfLYPoETXUJ1GzORHpSabGTbmqIuU96-Mqwnsv3oXsyviEGaXQq4VLxofi3PNg5Xc-Blc0rMSRvcz7DkCoibq6aiENcJszaEnic3UdxuOD3FJr9n9DoK3gJKk6ZFiBZ9HMpZonJP1yCvOHpASQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3660da3d6.mp4?token=ANU93xqDllcAjcMH3EKbatR2y_-skM0aifGeTt6RYiRj9MmF2B5FgAPpwB6F1LoDkww1sExhCEJMhueOOG12PAjsS0aeGWHMeEeOAuz1KimCKilIthnxGu8d4zGsNy1xUWtfMSjgwgvADFe3xiid55YLCrxJe78VS2R670eyP6zASDbMqSmPZQYb3myi1Mhjis8aDfLYPoETXUJ1GzORHpSabGTbmqIuU96-Mqwnsv3oXsyviEGaXQq4VLxofi3PNg5Xc-Blc0rMSRvcz7DkCoibq6aiENcJszaEnic3UdxuOD3FJr9n9DoK3gJKk6ZFiBZ9HMpZonJP1yCvOHpASQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زلنسکی پوتین را تهدید کرد؛ اگر اوکراین بسوزد، مسکو هم خواهد سوخت
رئیس‌جمهور اوکراین در یک مصاحبه با تهدید پوتین:
🔹
اگر پوتین نخواهد این جنگ را پایان دهد و بخواهد آن را ادامه دهد، ما ساکت نخواهیم نشست. ما پاسخ خواهیم داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/660804" target="_blank">📅 14:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660803">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/660803" target="_blank">📅 14:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660802">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/660802" target="_blank">📅 14:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660801">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQwcjxsIoXZXD1SRUX20xP1Rz35xtV1B7S5Dy07-W_Fdw3cyg3xNBbOh9L72ScrByefdZzRlK0F2QJ-N_Yj8etS-iIbapz-gSiIPRsh0cBMuYHYHo8wQAAHpbcRRha0kNb9gQ2eECJHbUXaWk3hkMTjQDO0MdX8LYLjjGeXlmzZBpm-PfLd01y-iDwMKxwAu39APlGnPGNxLrm6neBSDdATrIQ913VqF6BTRoCxGQjw8JDt_xLJBz5Qi0B8kwDO5qHWQjIfW1jlnqo3Z0o6r2MH2raVuuwfJVqZsPNHiuF57MSO8MGghlgFbzFkooD3d9owZHIBrtnEramZxD2kuDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استقبال گروسی از توافق: اکنون نوبت کار فنی است
مدیرکل آژانس بین‌المللی انرژی اتمی:
🔹
خوب است که این تفاهم‌نامه (آمریکا و ایران) وجود دارد. اکنون کار فنی آغاز شده است. اکنون زمان آن رسیده است که با همکاران آمریکایی و ایرانی خود بنشینیم و تدوین گام‌های مشخصی را که باید برداشته شود، آغاز کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/660801" target="_blank">📅 14:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660800">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uX054MQLcv1cQ1g5BSMab4ybSnlaj5gsnFejsWTbK3hLSRMmKYOE7R_qPPNwSyL49hABOFQN3v5hLHlLRdcp6E-wdQoAjG0ZWN0-DcswxfGPMFitScLcfGqIMXERqBzzHhBzB4D8YhEWxZvT_ujEF995faxnW36Y5z5iuFsKwqTMroabsPgeMcjFPrzkso3Mg9fZ2D5DZ8sFz0BtihETkO98-dQYqhYUhggnDRQyrr0Z7yc35NnAXNTfWtWAI6fHmk6r1FvIso3pXvF7MiqeCqqahd6_ld19cGU_lFr758-heuS6h7mP82kxeV4eedb1hAQvS_Ld5cXhhqyXukZ5Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«آندرداگ» رو زیاد شنیدیم، ولی دقیقاً یعنی چی؟ #واژه_کاوی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/660800" target="_blank">📅 14:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660799">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/660799" target="_blank">📅 14:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660798">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtoGemK0-8IMtjRht_17akmdNDgLTEn-oaZteZnDRN0tIcBiNXWkDMs9h7ri5vGzHACPDSQZJExnoyZVo8kvf5adl4wtFp82YcSu9WrfYYLHtbPDP7Z7leO9AK-SKLs356gZyplhG57h2lZLKmT-yACXP96q5cW67ax8xsSo2mvD1CV-9y4iDWW4AnyartzMiPwv3F8PlNbqsq76efvaYYPCBQIho3CfyZyLdC_BDwJ6ld9u59stDNiFLY2d0cqP8xUwDmR9b4iY1sbHY6fFc_LPmWhrTROlY5ADlslRvt-nDVeb5WiAfDN9hOCoIJ1e3KGI9koV04N3sBtO3yjwJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری که آمریکایی‌‌ها زیر پست‌های جمهوری‌خواهان و جنبش MAGA دارن منتشر میکنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/660798" target="_blank">📅 14:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660797">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b1e2cb577.mp4?token=fdWrf1GB_DMlvaOV0YaD1618DpoTXcxuoJxg6B8Tj2MNeHs5596yDRZssK58RH01h06cLBkt_8YumiurarVuq8BeVpH7LCUwQ6wUu5bkrO4dmtz8XGcHoiwGTW_OA9FYHx8i6dQEUS3PQrZ7w-GoJemiBfIQuJRhNQcV7weZNCS-ccqJwe4y3lnOsdWXNSQs70gDqRNb6ONvq-k-LZbK62E64Vk8pirNaTxI0EH5--nVuK8wB6Qa0maZE9c8ghDf9gEu7KeFSMcARQRF15QPV5NUTgc7UQhWPOSaZqVME2qjsmcfUDlAVugHu3PSSzW9_oxoUexMS3HOnSYnMe5CY308YjL-VNnRUEUMxOHRJB4_dTbKsVmAYd8YdVMPrujoXpmO7JbPyZGiPdgVFzKQqAAEyWpEdQ2plP9Ue7P6aaHqV9be41xceLJC8J5XHPU09nOjeL98vYpw6rattnyiQTMzU17ATD9lujCJQ8nIssnyM8dNWStJMy5KCnKwFEYlP_CTNAzV_AHoqVkZeaYF6TJs2yQqxFGrbmPmViOOiEx9IgDPBRy65qS9x4S0hzsimy_U89WMDOfF5Crg57c-32-rtRVO-Vbvye-P-m5C5vq0hGIMMl5Nq3XtFWnlrf3w8KWsJiTD_UVN6XZdH7BJNJDhAUHPwRI417DJz7d9om0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b1e2cb577.mp4?token=fdWrf1GB_DMlvaOV0YaD1618DpoTXcxuoJxg6B8Tj2MNeHs5596yDRZssK58RH01h06cLBkt_8YumiurarVuq8BeVpH7LCUwQ6wUu5bkrO4dmtz8XGcHoiwGTW_OA9FYHx8i6dQEUS3PQrZ7w-GoJemiBfIQuJRhNQcV7weZNCS-ccqJwe4y3lnOsdWXNSQs70gDqRNb6ONvq-k-LZbK62E64Vk8pirNaTxI0EH5--nVuK8wB6Qa0maZE9c8ghDf9gEu7KeFSMcARQRF15QPV5NUTgc7UQhWPOSaZqVME2qjsmcfUDlAVugHu3PSSzW9_oxoUexMS3HOnSYnMe5CY308YjL-VNnRUEUMxOHRJB4_dTbKsVmAYd8YdVMPrujoXpmO7JbPyZGiPdgVFzKQqAAEyWpEdQ2plP9Ue7P6aaHqV9be41xceLJC8J5XHPU09nOjeL98vYpw6rattnyiQTMzU17ATD9lujCJQ8nIssnyM8dNWStJMy5KCnKwFEYlP_CTNAzV_AHoqVkZeaYF6TJs2yQqxFGrbmPmViOOiEx9IgDPBRy65qS9x4S0hzsimy_U89WMDOfF5Crg57c-32-rtRVO-Vbvye-P-m5C5vq0hGIMMl5Nq3XtFWnlrf3w8KWsJiTD_UVN6XZdH7BJNJDhAUHPwRI417DJz7d9om0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازگشت مردم لبنان به شهرک حداثا
🔹
ساکنان شهرک حداثا در جنوب لبنان در حال بازگشت به منازل خود هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/660797" target="_blank">📅 14:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660796">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/660796" target="_blank">📅 13:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660795">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
سکوت معنادار نتانیاهو پس از انتشار سند تفاهم ایران و آمریکا
🔹
بیش از ۱۲ ساعت از انتشار رسمی سند تفاهم ایران و آمریکا گذشته، اما نتانیاهو که پیش‌تر از «پیروزی کامل» سخن می‌گفت، هنوز واکنشی نشان نداده است.
🔹
همچنین برخی گزارش‌ها حاکی از نارضایتی نتانیاهو از مفاد تفاهم، به‌ویژه گنجانده شدن موضوع لبنان در چارچوب آتش‌بس است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/660795" target="_blank">📅 13:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660794">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMWPjZ_NhvYm4f_fmJf5URNSOWU4Myt7z0zfgDdukqnA0AJ49_JhDS20EceKBV1hKWwf-q591VS-b0YsRBJk3At1hhWCuHuvkZ-6sM1BeatqeRPWgT5SUhJlf_OpNBVDfoAUyl46d9bAIuTuJ_yF9mSa0bRem_pnrZLH2-GcvbpXgtGTsYAdDfrgAb_jCOV8EDF3gJrCCVUDnnT-c7sdrnbPxPZAjwQX64opeCFbrJLgNlod1mBNwmO9QudzrhrpRvCskZ_zPigbmBxnfuLz8pLCBsyHR-dmxFlqQyRRnqCFp9OJk-IjD20vLWlwQsAHRf58NPUB8tHXtW8iMtUY_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدول گلزنان جام جهانی در پایان دور اول مرحله گروهی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/660794" target="_blank">📅 13:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660792">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
حمله اسرائیل به جنوب لبنان یک شهید و یک زخمی برجا گذاشت
🔹
حمله پهپادی امروز اسرائیل به یک خودرو در جنوب لبنان، یک شهید و یک زخمی برجا گذاشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/660792" target="_blank">📅 13:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660791">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41e201c6ac.mp4?token=rzKTbJM_1NGY04FmdeC3FfK-42iDvc6dLaJaxD4K6KS0d190adZ3RZBWcMpNikxS_KXGgEWvmJ3iRYxsQL7ES_14iQJ-uEPdyba3HaPSbkabHBu5uFSDgJZOLaDfwplVYSWvCA2ck0U4tMTd9Ro2C1Z8kMHyCRWyN5V9MDCC4bly1Mg4iOoTECLqhjXAUYlt4_y_30f5UyRoaAa6zduiRgAaXx07SP4G1TUWtQdwsooy7qvgpJ4mJ5YKXGSXTrjbqCUbdvbURBQh4iohYtunevT4hnH0daD1OXGmP98XEPBLIWqgtyCorT6Auyx461mUeZt4jgcGo-iWi9TiYyt6Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41e201c6ac.mp4?token=rzKTbJM_1NGY04FmdeC3FfK-42iDvc6dLaJaxD4K6KS0d190adZ3RZBWcMpNikxS_KXGgEWvmJ3iRYxsQL7ES_14iQJ-uEPdyba3HaPSbkabHBu5uFSDgJZOLaDfwplVYSWvCA2ck0U4tMTd9Ro2C1Z8kMHyCRWyN5V9MDCC4bly1Mg4iOoTECLqhjXAUYlt4_y_30f5UyRoaAa6zduiRgAaXx07SP4G1TUWtQdwsooy7qvgpJ4mJ5YKXGSXTrjbqCUbdvbURBQh4iohYtunevT4hnH0daD1OXGmP98XEPBLIWqgtyCorT6Auyx461mUeZt4jgcGo-iWi9TiYyt6Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور ارشد آمریکایی: با ایران سند تسلیم امضا کردیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/660791" target="_blank">📅 13:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660790">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fno49PS4ivCU8O5cga0SzUu5yW74xfbVNUmDVnrOIyNJfPUXX1wy-gC1PMrvHgDJYXu0IqctAj0dZmLr3s_L5cWdlITvjhq7usizCGsFTpHU5oUO3Qjg7AKbZJ73XmmZ9sJnZuIpgfR3ZGC8twKBkyeii7C3Jiv6LU3eAIBF0sINCw6R67dffMjMptDski8__1MrhmGepW3_uo69Pmc8lzsNFonpwtNByWrGstEBUrTV0101PagT7GM1GWrS763A4ss_ZK1073HufYrH_QlY_bUy74qufUUXSYZODwwOCbbv8v6F1KbEKNT8PPqqhmwsBzJBuSFScuEDApUXINgfiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعتراف تلویحی خبرنگار آکسیوس به «پیروزی کامل ایران»
🔹
باراک راوید، خبرنگار آکسیوس پستی از یک کاربر اسرائیلی را بازنشر کرده که در واکنش به انتشار مفاد سند یادداشت تفاهم میان ایران و آمریکا نوشت است: «به ما وعده پیروزی کامل دادند فقط نگفتند که طرف پیروز کیست.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/660790" target="_blank">📅 13:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660789">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b647c3af5.mp4?token=rTUkO-hEJtc8XhFjy3osMMVIDgN9PCxKF7L5Zx3VQO1Mm_HnUwwNQfLhIZPV3PqifS-FEi83vInKvTUx-vDEUp5KA4kWE7f02ShhSgcaqJqtwy0Cm4fmXPV5O0byn2Fs68sBAYuGz1S5P51brpuNlod5ie8Xx8NNA1sFaGG97-Hfq9LIbuQFzFyan9TSuvyasbJxUC_-jpv8cJgjRuj7mbInZFB3AXeKflOG4RPpNdxeVV9qEGbCf2th3hZDwRH7xa-uGYTVBxGqOqvKBaMxpCtr8n5xEQtTEg8WMxewnWyxsAb2cAnLC3aN8v5NhA58RhvnXJkXTL5zYVJC68qCnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b647c3af5.mp4?token=rTUkO-hEJtc8XhFjy3osMMVIDgN9PCxKF7L5Zx3VQO1Mm_HnUwwNQfLhIZPV3PqifS-FEi83vInKvTUx-vDEUp5KA4kWE7f02ShhSgcaqJqtwy0Cm4fmXPV5O0byn2Fs68sBAYuGz1S5P51brpuNlod5ie8Xx8NNA1sFaGG97-Hfq9LIbuQFzFyan9TSuvyasbJxUC_-jpv8cJgjRuj7mbInZFB3AXeKflOG4RPpNdxeVV9qEGbCf2th3hZDwRH7xa-uGYTVBxGqOqvKBaMxpCtr8n5xEQtTEg8WMxewnWyxsAb2cAnLC3aN8v5NhA58RhvnXJkXTL5zYVJC68qCnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ سناتور تندرو درباره موشکهای ایران: ترجیح می‌دهم ایران موشک نداشته باشد، اما معتقدم باید بتواند از خود دفاع کند، وگرنه جنگ بی‌پایان می‌شود و بدون نیروی زمینی نمی‌توان ایران را به تسلیم کامل واداشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/660789" target="_blank">📅 13:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660788">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRtdRh3eSXBUiq6K9AG1xXJZqZKNWZDiXL5ki5h5kZRt7HVUubOMpUM5X0PRTTSUVnL-NEzZSDFqKQksr42aBbqpbZJ9YiUYBM6i34fMs1brKbKW2O2hEvJZ3NOkZ0xpPceq7tDwtZzOHIZQGtQ41ZKBAyzdXrNBFyHUvyyZUrVcf4GcVLcak6berh_okLEZQRL9Yr0Pd5C77C-HyzfyGqYyFAl9ys6-mXyq8y0fJKh55V5lJEJQZF7TekvTNdbGdDQBsuDN34OVdI6HiCjMkn5-56rI0X73ySF7L6UHUdTpEX_6x3tt_V_AqMtxY3Lq5jou-CFn8H5zQr4e_Ob7ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۸ خرداد ۱۴۰۵؛ ساعت ۱۲:۵۵
🔹
قیمت دلار امروز به محدوده ۱۵۷ هزار تومان بازگشت و در میانه کریدور ۱۵۰ هزار تومانی متوقف شد.
🔹
این عقب‌نشینی همزمان با آغاز فضای جدید سیاسی و اعلام مذاکرات ۶۰ روزه ایران و آمریکا رخ داده و باعث کاهش تحرک در بازار ارز شده است.
🔹
افزایش خوش‌بینی نسبت به نتایج مذاکرات، تقاضای سفته‌بازی را کاهش داده و قیمت‌ها را در وضعیت نسبتاً منجمد قرار داده است.
🔹
در همین حال یورو نیز بدون تغییر نسبت به روز گذشته در سطح ۱۸۰ هزار تومان معامله می‌شود./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/660788" target="_blank">📅 13:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660787">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGy4o7q5kh3eCRZu6vB_4xLCsVx2zcGy5x7EUm73Ew0SNfpenHSqLDABppagB_0PJmQzhea89Op-TAZunzS0560J7L_Y3n4VeILQ32v-dtWDkfgoqnVELeEXXOg2WNrqVketLyYj3InTr9gy4cGErIoo-etqhmRRdLDWUmP_Wtm1rVPyeIsdSB2h0GO43fh70okC2cHZsbX94unR5047B6J-6WnE40HBd0gagZAtZgZozsnGH77nXyGpV8m9Fc0v0Szx39H1FUbg0Tr76R9_AhfxuwLxUCRvTjKBNcOL2Z1ILcK-g0OFQ7_H-zh8fyAqaW1u8pV-FVbXjj0I5MgQsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افشای جلسات فوق‌محرمانه ترامپ | خشم ترامپ از افشای مذاکرات جنگ ایران | احتمال ضبط گفت‌وگوهای طبقه‌بندی‌شده
🔹
مایکل گودوین در یادداشتی می‌نویسد گزارش‌هایی منتشر شده که نشان می‌دهد مشاوران کاخ سفید به‌طور ناگهانی نگران این موضوع شده‌اند که گفت‌وگوهای فوق‌محرمانه درباره امنیت ملی در اتاق وضعیت ضبط شده و به نیویورک تایمز درز کرده باشد.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3223914</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/660787" target="_blank">📅 13:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660786">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
نانسی پلوسی: توافق با ایران شکست برای آمریکاست
رئیس سابق مجلس نمایندگان آمریکا:
🔹
ما یک توافق خوب با ایران را پاره کردیم، وارد جنگ شدیم و متأسفانه شاهد تلفات جانی نیروهای آمریکایی بودیم و این یک شکست محسوب می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/660786" target="_blank">📅 13:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660785">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/do4Lh0f2dajyaMCDKECP-DCgKfqNW7hAHLvpWLD1V7iUbIxxa_hUXwFtCT94Vov6eL6-FDqPGJXg6gDRWK79uGqXimsWxAzPBr0Ox0CDYXqiN6gpU6bzMyJ_LnGnM6zoWWotHrcxq0D8e-9pt9tLxMaf1DKkP9Rh2j_f8ismN8_37HaRKEEvHF5gJooadyRrWtpYWPcp2zRoDex6ZwK1s_uW3LtHOJ7BQ3UL9NsY_1CVMavjcU3eBAoBFAaAe0g_FBfVXxBxl-JEafE9_LkrsewrO2ieNYQoW7xX5XOZiS8GiT6XSDdkisgFp7JPrHD45ujW5-yonsJXxYPCf29N5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اطلاعیه شماره ۳ ستاد بزرگداشت عروج خونین امام مجاهد شهید حضرت آیت‌الله‌العظمی خامنه‌ای‌ قدّس‌الله‌نفسه‌الزکیه  بسم الله الرّحمن الرّحیم
🔸
«مِنَ الْمُؤْمِنِینَ رِجَالٌ صَدَقُوا مَا عَاهَدُوا اللَّهَ عَلَیْهِ فَمِنْهُم مَّن قَضَى نَحْبَهُ وَمِنْهُم مَّن یَنتَظِرُ…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/660785" target="_blank">📅 13:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660784">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rawbG6taLGIS2BOPxpmHJeZAjD8OAba-CPO6LZgi6LedK7gledNkVqMloKvqYW_Z78qtv4fwNq2bljX5R51_DRiZ_yEbV36e0Zbarnj7VeFJoDTrMPY0hNYWB8hTMFC7CNDguJVofJBnm0O5_j_8o5Cr2V5zS-ePvc468j1JVPym1B4ii7NErLqseBYnTuPo-utFSsZCSeHlZcCggd9TFw1EU7jZXHDQboTSfFECJg3LaIIgnsBWAUrkiULVFHOV_9I3_thS6wlnGUWSZWL-qzH10nUF70X1pTfJoxTgKp48LzI71YDGBzaWlPNDt1cK1-bwkKL7kgEOUqG6w2KybQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طالبان استفاده از گوشی هوشمند را برای همه کارمندان و مجاهدین ممنوع کرد
🔹
متخلفان مجازات شرعی می‌شوند و دستگاهشان خرد می‌گردد. تنها استثنا با دستور کتبی رهبر طالبان ممکن است. هدف: جلوگیری از درز اطلاعات و کنترل اخبار. نگرانی از گسترش ممنوعیت به همه شهروندان.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/660784" target="_blank">📅 13:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660783">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b21440bf8c.mp4?token=UIF7fO1s2RuC5TEWr2JIYUcRg8tF8wJKtifL_DXKFJKV9g32dMUqhdPxoXvvPEjUhj48wesCbO1BjWo-Oz72n12g04f4_tqZdkztIG0Mmy2zzLoCzRTKVPzqdnXc7dxeduGO43LpwEes_UVGFX4PMuI8yDQ5fOuEBHkdUjLP_0MPlUBegIKeq2JQKHGF6GHdepewwr8p-tZZ3uWMc_sASMBO829VApPZVFEEK5i4kFELzJKF5TzfhTd4zUcqKWlMcGTLFuWZSnv5KJaZ024afI5Bvq2Tjy_11aVaayT97145s-rXmLj6cc3Hk5Z-v5yoIGOsEtxRvdmwT__sJgMshw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b21440bf8c.mp4?token=UIF7fO1s2RuC5TEWr2JIYUcRg8tF8wJKtifL_DXKFJKV9g32dMUqhdPxoXvvPEjUhj48wesCbO1BjWo-Oz72n12g04f4_tqZdkztIG0Mmy2zzLoCzRTKVPzqdnXc7dxeduGO43LpwEes_UVGFX4PMuI8yDQ5fOuEBHkdUjLP_0MPlUBegIKeq2JQKHGF6GHdepewwr8p-tZZ3uWMc_sASMBO829VApPZVFEEK5i4kFELzJKF5TzfhTd4zUcqKWlMcGTLFuWZSnv5KJaZ024afI5Bvq2Tjy_11aVaayT97145s-rXmLj6cc3Hk5Z-v5yoIGOsEtxRvdmwT__sJgMshw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای اکسیوس از انتشار متن کامل توافق ایران و آمریکا
🔹
متن کامل یادداشت تفاهم ایالات متحده و ایران، توسط یک مقام ارشد دولتی در جلسه توجیهی با خبرنگاران آمریکایی ارائه شده است.
🔹
این یادداشت تفاهم پایان جنگ را اعلام می‌کند، از ایران می‌خواهد تنگه هرمز را…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/660783" target="_blank">📅 13:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660779">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W8PVGamkA1d_gPs6Av0jNEZCzptNVd6WoYgCzcXPqR6-7ZGysUxabjGIOdrKH-FyIfZPwCtqXrh9UVDbbOwiBSoKsf1BRv-JlZeznF3hKVHKRshtyy1a2_rIvkv45PObkU2rM5sT7mv-pIZ20aFs23KZI-f1EBtx3MBzfy7S4-cvIqtmQoeE1iMwcMcpa2Y3fBbWCaGkPc2I_DXlV5-l7TFaNupDfk0xf_F-_wESNCMYj8cYeY1wGkn4ZI_wIL7d-hauivKSoqQ3gCVS3HMFp_ulg-W2Jh2O_IryQvkv-1TzNykd35xjjsMO4BxxswGvVR1NiZtzCEbqQC1B-AlV3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pg0R8KuowwzgM3rQhoNqkgbuqi05dnWhrwUnk1hsu6zp7B-etDPssp7r8MsGu1sw7uBVoG_2U3P_FsO82_jkbJMeufwzKlNGkNFTEHowqbmFQ9AECSPLZ8rGEydWE-lhteU-QZ5IBQNzW0B0YZOwXy6Ul1uIK0o41AXtTUiXK8pJsL0aitF7ubTYObPxK0Y6xaEB10Ilg9dPypDFWCKPDXRAB0Enq2tX6PoEiI-MGdRyo0URb5Z3b2UhDMAUYX6paZ9FhNZ8-azAR_G0ZELoRY33UI4yzM5nWnwD3DL2XKZMoD-ZZLjVjvgFaKWCoLN_7olwctwUOUePZtXDq9136Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mcmh5hCAR7-92HCLUClA-AX0OiFM_DymicotqgvRiFPbPANHL945354hVk8cUoUS5UKPhOIu-44noyFQ5-pb8Jaw_vHEfq_W3u58teltKASl2kefioJY2hMT5ecschZeZz_ABDjbPzLfheJSn9lKnTNYjKA0qTb0FAkg4B4Q_3quTflIOvKvsTlFQ5s5yiciEcGVBLkbP_i_WN2q27xNY3TsnUOt-_it-SENeLUIlnLnSQDn1MoxLbEOY9Jvz_A-O-1Pk0J-3EoKvarCmR39Y90N3-UhuVtfyYuEoRsU6VzOM2PuuQigPZ_epXbvqW8h8gi4nPzwJM-hXrOuzdoezw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18315aa54b.mp4?token=lesbUTxMNWcSZ-MO6Rh3CubUmEeB8o9eeLJMhcoEjAFMMPtdouLvFNxcVqQE8A0U_2zY9xv_oob49G3ZliNL2AstYOK8Virn6Wdn22OuQT3ab04felNRsqZKqP3Ppx64w-MIUonyDCJkoOpTJ72iNhNf661Smsb2BV7RCZlt-jrzOEGyfvRO9Wr3bRR_AB0jtC0iamn3eGDa-oVJ5BEZwFUbl2muzTLdeVNwKquRmzs8A_xmHv-7wdnFSARFOjUocEdB3Odqd6KQqEQ-vehWwX7U7PrkFj8q5VL2jY-EAXwd2iWV5x9yPNJqLh3m9iSHaICDKjY9HwY4AlLxTwai14i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18315aa54b.mp4?token=lesbUTxMNWcSZ-MO6Rh3CubUmEeB8o9eeLJMhcoEjAFMMPtdouLvFNxcVqQE8A0U_2zY9xv_oob49G3ZliNL2AstYOK8Virn6Wdn22OuQT3ab04felNRsqZKqP3Ppx64w-MIUonyDCJkoOpTJ72iNhNf661Smsb2BV7RCZlt-jrzOEGyfvRO9Wr3bRR_AB0jtC0iamn3eGDa-oVJ5BEZwFUbl2muzTLdeVNwKquRmzs8A_xmHv-7wdnFSARFOjUocEdB3Odqd6KQqEQ-vehWwX7U7PrkFj8q5VL2jY-EAXwd2iWV5x9yPNJqLh3m9iSHaICDKjY9HwY4AlLxTwai14i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر پهپادی جالب از گردباد افینگهام، ایلینوی آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/660779" target="_blank">📅 12:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660778">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
تداوم نقض آتش بس/ حملات رژیم صهیونیستی به کفرتبنیت و حداثا در جنوب لبنان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/660778" target="_blank">📅 12:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660776">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKe9uhmfgML1le-HjS-yzJU8cyugv7vPZJYhJgGwq2-4Q-jpaFH0pIuSWVQmZqDz9xWc3m63cbyaJyyqV_2yfvuBPcbSTOv7m_f0nwhlj_t4o-qNB_sf0c5xthGdLJ5_GVb1uEZQW1d3Jb-qS8gW9DQvcQMkrExgDHhx3iBE91mOXkvJ1uef5im0P5d1hDMgSRb1aMSHOR58q1fpn7IoWUyIywFYaJgLkmrwHLsbwuL9Aw2vBmAsldcYEkV_H9uh2-QUwgZYQqtvKWdlcAX08vkvVFIU9ESFP6ZXEQmfwN7Q1HpTJhxeL3tJqoRxLZ4ooWFBMeQHQjouQW5ARng42Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با حضور رامین رضاییان از ایران؛
ترکیب منتخب دور اول جام جهانی از نگاه «Who scored
»
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/660776" target="_blank">📅 12:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660775">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ترامپ: منتقدان به توافق با ایران حسود هستند
🔹
رئیس‌جمهور آمریکا در واکنش به منتقدان به امضای تفاهم با ایران در شبکه تروث سوشال نوشت «این احمق‌هایی که فکر می‌کنند من به‌اندازه کافی با ایران سخت‌گیری نکرده‌ام، در حالی که بازار بورس همین الان به بالاترین رکورد…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/660775" target="_blank">📅 12:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660774">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5NSwdTkCYIjNbJcOgmAXky_RpRnzajqCE8zC0-SYA3peZXnHEacrxIDzV_uTja8VQ4gcTmCD-XYcDAhM9SUC43wO0wj9Yl2SWbQ4N230YVHzGaLVvIHXOT3ivuHw_bHCHDa0sYJor7XasMRyluNqGsAmmEwNYJGCNlYMnsXlyaWUWfsoq7DcXsmN4n_1Q1-0BE9wv7vkaXMQJv7sjJt9AEq8cKrpn_wSii8aEwVbRNqX39Kn-guXwR75M2ZTd-SR0rvkF5sZ-yMgnC8xKtl-H9zsb36-D9rpA5F4WCuN7LlPzAiY0WBIGgRoVrmULpO8oAa14rMHdM3EdxZirAIFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چه کسانی از توافق ترامپ با ایران ضرر می‌کنند؟ | جنجال در میان جنگ‌طلبان واشنگتن | ترامپ از ایران فریب خورد!
🔹
پس از انتشار گزارش‌هایی درباره تلاش دونالد ترامپ برای پایان دادن به جنگ با ایران از طریق یک توافق، چهره‌های تندرو و نئوکان‌های سیاست خارجی در آمریکا واکنش‌های شدیدی نشان داده‌اند.
ترجمه گزارش ریسپانسیبل استیت کرفت را در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3223852</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/660774" target="_blank">📅 12:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660766">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r4GOm4BzLE-JdvkQXotsJlOIPgiEUxGV4fn0hfWnISAiubpG95dnvZd_bv_0VH8kknnKHELEvTdf9qNy_z3YhDnER49FkdTNcyFO77qnewAknQiQn6vcOUPXHvNF0elYwhT20-xL-NDCmNT4rbBhcYjI6Ctbi4HoCWYGgqr0qquz33MbiwEjGbzzVLTFydB60W_RLvqQc4rsUEJvuvRMyFaWRdp-kc6BJGU7GU5CMAZyLoZGRLtaB7_VISNN0PEleOXFlICD94FhX349D7XwOd5eVnGdK6pA9PjU0kKNYpy35E2DE8EOEKzTbhFWRRySyHs8I9VnQwNZip4jSpxGTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JOnTuG0gY1jj2UgEMg5R0ZPi5DccOybijz0DjP4WuqiVTM6OBzuyL9NtLjZHVy0PHA0R4p82Ra0LN0V5BsE0kcwl085RvmgPDm3UVZLzEKe3CHM_MNE9aSTFFX2AdBLXdJUje9EcQpLXvLBMGbA93o2leIOezkCUl9FIg-9LtUzuG6dCC9ezKtl7JKFqk9hrIA4CCTDXff1ft7dbzNpoHCkCniSaWW3Uo5gsQ6l3CuYb-FGHzG83meCHtldiZwpBr-r128qVGm84VAERE2-rgsmYib-hnm6cKTkXrL_Co-1FA1N-_Q96KhXoziDO0GiUQSGGShURP3_H5ryhAbT6YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HIrgR_ucC-5ayMOiTp2W6R3GhJnrbakrA-bATbyP0k0qgyMusDavWVxbLlycfvAQ6TwN2zkFsAXxQZ19uGmbnPvf-pYpHXzUQtFWHjUOEMmo6q_PGaJU76QI1QgXHr75qrbBCnE5QAWxZ18Ez-_gdLrKYlmOxIVc_LbI88G5uawkaTIM0L-RIoJsm8Ate0Bo0HqKCW4dwE5yOyXorJwr8mFgwJ0SI2l4eXfhHnRr1tvcUnKJZdbqZi4A_srl4-Rgne4OVg7iN2HRO0GA8h47GLs2zB5IJHK3Ta_IK8rXPpM8QQ3DtIJlOMVgOg5f7mqESkro2nqknlsjpSnFNi3jjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BQCwo_XtoOkuSVQ-WAXfaFN9gioo-ryVsFqXbRcbBQNWi3icTee774fv1tqp0KGr573UmvMXGnkAE5HrihzkZ7LoVe1KYGhAudeaP_1BflOvTl-W3z0VCKj3n0PKBICkFsd8o6vri8HBx-sNHhp04wgTQxw6zErqEdKRyVa14wfXrzoR4manMNTFleYfTn8JFtEnu8HcvrNIDwP4PjJ9XoByZuFiIqDtG1SDWay7A5-SVoMs7kp-UsVk6C4DOfZcHmg4LPAJUsZ4Jkm1XlAg2dtG_m5wuORFFVkQhCiExQBOuF0Bv3Easx4_L_87OMCO0p7euK7PJr3dfp7EX3zRdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KwiaH0h_ZfBEOWu7IlfoEARKN08jwc8cwwTeYhjpKcHB8xgqjvIA1NAm8fWwSIVGT5tnFAsMWGYlgzkoUz6DKULNkrBFbRNtUbpqKoZ1h9GCLkJVWieqNZbZb36Ccc2tMGryE1i75jQjpSSbz9KRmmjj0WgIMW24P9m7YLsWM-iSRVln245_u2aDtVaancggCMFjC3nt9Tvrq2ZkGUzx_L9VD9ggEtBDqnTjL1GTyxMq4l7IISBKrvO9tzqkqytRxx67qVmIbLzZQU2FXHMclVZzkvyGcgNJJkyHlBFjC5vRiK72JTClu49E7eONO9MPOCUtTT1KGxOqEi16ab_NqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XD0wbeVsoXaUwHtapEJxn63QQ_qv73Ac7ZkOTg6GRY5InWudE9bnUKSlyNXF-R5Rph8Mdo4RnjcAMrwEWs3bH49-xTq6ryxRO29jnP2BznJSh4DGc6d0LEVJdoMdyxqDTKUrbHSZX9CuVMs0Pv1wtUzQe-2lMRjLXQyjkWErxxJAX8jPvbTHQU5fVmU3XUOfh7ox47WcQQZ3sfNh5ajCCyL7ibhPCa6rQ70GW1MUjr2hIEcyXuTza0KvrILnlyKxET7_2hu4qiLD1tVMBFBss4xDdBRo5vs8titXEGBV4meuv4Q0CDJSLUFBJNNB-OeV1cDsXy6xMAjmIdDbTy4tmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v3kUVfFmGxt-9bPXceWRPNmyzL10B4pGjM7D-OPGVqW16tMtDUOiCe7Aoo395Z7ceOMLX7kXh9DETHSP5-7zeKIyIoUTn32eOv7GNb10AfXwJsugW8xt8Qx7JmX3ueDL0bTYz62rqd7uE7SWwIq-wOM1pI9M6wr_bm94S-fBwuDCp_OkJaLWQ7wIdi537mjzzedxETWaIlTyyu5hvueY2jiGgEf0bZY5GlmZiyD1UJJAD4GVdbW7JSwBlluA4NgCC9o-jebsb-L06lrNv1hRj3Es3qUj4eB9hqqwv7zCaieGwVmuopR6T6HyPseoNygdQJjpYhleZV08TjEgi0zriw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W1Tpm7XTB0FE69znvsjT90-YIlfnX3BdiyDlUDUQh5_MJo9Q5vr9dxYB8yYHKCtma-OCDdqKmsXRyraA_3AJ0N0j3edOnTDDp_VsC-wFdXoMWdJCz3Wa_ROp8bFoHlyQfUIp0BPxvodk3Rtp8K2zsvl16_XcuBKwuT_ni_DQAKeD3HfgkHFGUC9IJpLGYrDNG64vUeNbjTE3sHmqDxIjmuEIF_uzmfsJgIMG531V_GPjOqV8xWak-L2F20IPn-mpiKlGjGo4igVVgjVpsztW2oBA1y3aAIzAs8EM3oBqGCUC-MJXlr0Do62MX6OWSAugy7Y8zJkRXpt0tYRJPu6omw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ثبت لحظات هیجان‌انگیز فوتبال در پشت دروازه
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/660766" target="_blank">📅 12:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660765">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4503c3828c.mp4?token=ftl3xK5GLIG9_sochkNB4CydBb3sUHzHFw1JGO3NMuORgLalbBB_XATXSa3CZgQoPfrCTyTWd9DuCPxgX4LNJ-6-4efy-M0C1zkqOF-wQ0XwLFXVfXKIBwIuyVBPiG5DH7VBrMepofUFhybvibHSmdKS23VwBPhlx6Am6KvyGDojpSMxkccsHKFAXw8dG91c-IdM0kWgWOjv09aBMsYltEsUHBjAxBUCcsEbiz8s7XUobABOXx9ttDMP_H7hP70OjFUfktmhY2F5n2-4bgMBjZfxpOMAv57jdxYKir9KNUh2ttVbE4WwT4AoGcQ3PgU4i35aE4euZWW4ognM-rXi9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4503c3828c.mp4?token=ftl3xK5GLIG9_sochkNB4CydBb3sUHzHFw1JGO3NMuORgLalbBB_XATXSa3CZgQoPfrCTyTWd9DuCPxgX4LNJ-6-4efy-M0C1zkqOF-wQ0XwLFXVfXKIBwIuyVBPiG5DH7VBrMepofUFhybvibHSmdKS23VwBPhlx6Am6KvyGDojpSMxkccsHKFAXw8dG91c-IdM0kWgWOjv09aBMsYltEsUHBjAxBUCcsEbiz8s7XUobABOXx9ttDMP_H7hP70OjFUfktmhY2F5n2-4bgMBjZfxpOMAv57jdxYKir9KNUh2ttVbE4WwT4AoGcQ3PgU4i35aE4euZWW4ognM-rXi9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تماشایی‌ترین مسیر ریلی جهان
زیباترین مسیر ریلی جهان در کانادا
🔹
قطار گردشگری Rocky Mountaineer از میان کوه‌های راکی عبور می‌کند و مناظر خیره‌کننده‌ای مثل کوه‌های برفی و دریاچه‌های فیروزه‌ای را به نمایش می‌گذارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/660765" target="_blank">📅 12:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660764">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
شهباز شریف هم یادداشت تفاهم ایران و آمریکا را امضا کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/660764" target="_blank">📅 12:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660763">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
المیرا شریفی مقدم، مجری صداوسیما: مسیر تشییع رهبر شهید انقلاب در تهران تغییر خواهد کرد/ با توجه به پیش‌بینی حضور ۱۵ تا ۲۰ میلیون نفر از سراسر کشور در تهران برای شرکت در مراسم تشییع رهبر انقلاب، مسیر خیابان دماوند تا آزادی پاسخگوی این میزان جمعیت نخواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/660763" target="_blank">📅 12:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660762">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCsGh8tQ2t8PO4h7vHsxX12SXN8bT8peCTJzYH922FeGeE7fGB2uJi68EeQ4pGQbafqBvW17i6-0kpEzDevKbEIXqPFIvHuwrM5sMoVC-rXSha_4vv6Mu0t9PRhF4HA2IulwuZvuI4xXCrfLkiRrHNF_9VIBjBX19e6d_yx5JwP-GPLIyKqGO6bTnQWFgpOnVDN5XK-0aNCCfwYYwhpKGdFA2HOb2ORt_79EtRF-vkUE1FnoLpg7k6tcCnVYOj_8Q-SpbplhvTVugp3gjhq8KT-si0pAKbmeNWAgfSHVwhnQkVt7ct6RZkVJHrDYJeCThZ-96rdbECUSbbKu_bqr6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: اسرائیل برای ماندن نیروهایش در جنوب لبنان با آمریکا مذاکره می‌کند
🔹
رویترز به نقل از دو مقام اسرائیلی گزارش داد تل‌آویو در حال رایزنی با واشنگتن برای حفظ حضور نظامی خود در جنوب لبنان است.
🔹
اسرائیل با تأکید بر ضرورت حفظ «حائل امنیتی»، در برابر فشارها برای عقب‌نشینی از مناطق جنوب رود لیتانی مقاومت می‌کند/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/660762" target="_blank">📅 12:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660761">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrnQCpfIb0jCpwlroUikRXxgqRtqmyOPol7NKwwvtkxnipAKE-kjVDLdZkJACM3QWoGcx4qKjh1XMKwnTTZvYfSrgYl4hICt829LLrGzw6eiNro4728ToTG8DbwriimSVihykS6cfMCYYSJxwvicLblvUYId3WRVBz9Fw641ewSLH4uwoC2Q45NCyDvNSyaservBJM-DrHarUSdtXSxOV5gmkXOkYVpksIEwxJid60fHwahKkxDWKSpWpSs8dASUOOuhFzLAv4I4S6htvWhPf70dzuYFTW5hYq7AmO03eJCXcJYVLT4igWsoXqjQKctTwE9bEbO1mfUiTUuvNrz2OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: منتقدان به توافق با ایران حسود هستند
🔹
رئیس‌جمهور آمریکا در واکنش به منتقدان به امضای تفاهم با ایران در شبکه تروث سوشال نوشت «این احمق‌هایی که فکر می‌کنند من به‌اندازه کافی با ایران سخت‌گیری نکرده‌ام، در حالی که بازار بورس همین الان به بالاترین رکورد تاریخ خود رسید و قیمت نفت در حال «سقوط» است، یا حسودند، یا آدم‌های بدی هستند، یا احمق. عظمت را به آمریکا بازگردانیم»
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/660761" target="_blank">📅 12:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660760">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4ZnYu7au4LaWV9qu4mBkKOhLBw4qQatswBcUBil-GiT737uN5cm2svaTMj5Ggpu0Vl-ts0SLU-bZhObYV1plR0INnHKtRXyPU7DKwzaojQS0-lI_rmSOKSuWuT1hgFoLe_SVguazxKpRPBmeGvoxA69zcfP0gS5WXSB4cFJ-p-pqx_l8sIHMIdp4HtoTmETWrTB_bwD4YR0b2ZVwty4jVZIRPYFybbPsm0YFR4THrzGzfH8Py73rzfT20Oed6CMjcoR9s9_VsALNabyacdGcm2S9Ysz9MBkdIhKzUzXEmBKPDk59-qjruiGwJgjjhiXCqijIhacslTjHQKZ1E17jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت پرده جنگ روانی؛ چه کسانی افکار عمومی را هدایت می‌کنند؟ #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/660760" target="_blank">📅 12:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660759">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28fa1acf22.mp4?token=lKPyNvFS9DOKEffpukJmEt5p2IrFp-obG--tkh2H6bglrUKUoodE9ttNAWPyObufe5UpTbPQNPkF4HgWDnUpWk_xDprP7_0xhZDKVcsNGBLxEal0ZTYmb1geuJceZKvJL-CbbElbiXfQDe6CNCgi6990H-MU9xby376q1Q98OQZ0MMQmBpNV-y2UC_uQ3AVS5ZnavGdKkIOPc0qS088LhEQD4_FBbbjZHw6J7ZLcGmUytYw8xNV84cynkOMHpHllMv0gMzVSUFbxn1us_shDqaZpJlwEtzEdCp635bKKB4YyQikFSaItKC0xrYwSvuxpQb3QD67ywq0laA6wmuElDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28fa1acf22.mp4?token=lKPyNvFS9DOKEffpukJmEt5p2IrFp-obG--tkh2H6bglrUKUoodE9ttNAWPyObufe5UpTbPQNPkF4HgWDnUpWk_xDprP7_0xhZDKVcsNGBLxEal0ZTYmb1geuJceZKvJL-CbbElbiXfQDe6CNCgi6990H-MU9xby376q1Q98OQZ0MMQmBpNV-y2UC_uQ3AVS5ZnavGdKkIOPc0qS088LhEQD4_FBbbjZHw6J7ZLcGmUytYw8xNV84cynkOMHpHllMv0gMzVSUFbxn1us_shDqaZpJlwEtzEdCp635bKKB4YyQikFSaItKC0xrYwSvuxpQb3QD67ywq0laA6wmuElDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصاویر لحظۀ امضای رئیس جمهور کشورمان پای یادداشت تفاهم نامۀ اسلام‌آباد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/660759" target="_blank">📅 11:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660758">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
درخشش سه‌شیرها در شب پیروزی شیرین مقابل کرواسی/ انگلیس خط و نشان کشید
🔹
انگلیس ۴ــ۲ کرواسی
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
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/660758" target="_blank">📅 11:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660757">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
مذاکرات پیچیده اسرائیل و واشنگتن درباره لبنان
رویترز به نقل از یک مقام اسرائیلی نزدیک به بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
🔹
اسرائیل مذاکرات پیچیده‌ای با واشنگتن درباره حضور خود در جنوب لبنان انجام می‌دهد./ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/660757" target="_blank">📅 11:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660756">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52901b859.mp4?token=QXT0zSwPwwHTj8xy5QXp1hdQYtdhzk_G2i82jeRu4BPftGtXS-r5QF6aqRjuWEifb_O9V5kwiOm2_UQNV4FSMvfoHdpA3qH3fWEVnyQ1CqP0r-fbsU_AOwefDjq1TEOXX88HO1zJamSL-OrICQ5tUQmOavwHL0CEMucoxWNMDmrTfF4dGBcAxg8EXE5BCkqWKPrmjxP-LxqddvLisCeal8TOxXhDsXc6udoabPkNzpwp0vU5j3RUKNry67fbyX6sAuK4vjWMlGDfmFdTfGZiMU9cgR5FYgfr9ziOjwNoYoVqrL472uANEJ97fedbQYN2YEI6gAyVLPocyXS5mePUow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52901b859.mp4?token=QXT0zSwPwwHTj8xy5QXp1hdQYtdhzk_G2i82jeRu4BPftGtXS-r5QF6aqRjuWEifb_O9V5kwiOm2_UQNV4FSMvfoHdpA3qH3fWEVnyQ1CqP0r-fbsU_AOwefDjq1TEOXX88HO1zJamSL-OrICQ5tUQmOavwHL0CEMucoxWNMDmrTfF4dGBcAxg8EXE5BCkqWKPrmjxP-LxqddvLisCeal8TOxXhDsXc6udoabPkNzpwp0vU5j3RUKNry67fbyX6sAuK4vjWMlGDfmFdTfGZiMU9cgR5FYgfr9ziOjwNoYoVqrL472uANEJ97fedbQYN2YEI6gAyVLPocyXS5mePUow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شکار اوباش قمه‌کش در جنوب تهران؛ ۶ مهاجم در چنگال پلیس
مرکز اطلاع رسانی پلیس تهران:
🔹
ماجرا از یک خصومت شخصی شروع شد؛ فردی کینه‌توز ، اوباش محلی را فراخواند و در یک یورش دسته‌جمعی، با سلاح‌های سرد (قمه و چاقو) به مغازه حمله‌ور شدند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/660756" target="_blank">📅 11:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660755">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
ادعای رسانه پاکستانی: شهباز شریف امروز عازم سوئیس می شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/660755" target="_blank">📅 11:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660754">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6cad599f3.mp4?token=Q5PqGTEzXOV4T0mLx5NtNQWtN27UgM2PSbS9fc-MZrVKFE0DMcKc8rE-C8jtCiUCL-C6FPLd98j_xeSLjdaSaYGOvTHyOPHdQWH3EzUN9hDkkgDWtsxAjUFKgJl_dzh_umt0RCNzaxmfg1dhymWRuPelpuwIhz3WerVX2WMjmrBuzmOZbt--OmatBk3fU2syZ_-95VCqMwUq_BGpmkAp1CVqsiz6I45JinS6xPmkrjBSICSNWWHRs4ShFZR9If7MK99vuSIUMzd204FMBG9PTc3QJCf_LRlHKPeoMOJtVyRfitIr7futZ60QMMoGJAxO3IByQyR9M1ueVNBdTOvd8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6cad599f3.mp4?token=Q5PqGTEzXOV4T0mLx5NtNQWtN27UgM2PSbS9fc-MZrVKFE0DMcKc8rE-C8jtCiUCL-C6FPLd98j_xeSLjdaSaYGOvTHyOPHdQWH3EzUN9hDkkgDWtsxAjUFKgJl_dzh_umt0RCNzaxmfg1dhymWRuPelpuwIhz3WerVX2WMjmrBuzmOZbt--OmatBk3fU2syZ_-95VCqMwUq_BGpmkAp1CVqsiz6I45JinS6xPmkrjBSICSNWWHRs4ShFZR9If7MK99vuSIUMzd204FMBG9PTc3QJCf_LRlHKPeoMOJtVyRfitIr7futZ60QMMoGJAxO3IByQyR9M1ueVNBdTOvd8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیت هگستث، وزیرجنگ آمریکا: برای مدت طولانی، ناتو یک ببر کاغذی و یک خیابان یک طرفه بوده است، دیگر نه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/660754" target="_blank">📅 11:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660753">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
سوئیس از برگزاری دور اولیه مذاکرات ایران و آمریکا در روز جمعه خبر داد
🔹
سوئیس از برگزاری نشستی با حضور نمایندگانی از آمریکا، ایران، پاکستان، قطر و دیگر کشورهای مربوطه در روز جمعه برای مذاکرات اولیه خبر داد./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/660753" target="_blank">📅 11:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660752">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cu_MAv9U6eAv4Yh0NAmipVTMHe4XUlaS2LZSWzZoJryrnRLSBVYxwpTDUz3bVgxZduCWTvVHzgWhh2ePCDLStv4JHOMAMdQG9Y-myEA4SGQLDUYoopdcHWL3YRoBDlTEj83KcEuBNc0Gdl0LNMfFNu99IL9rXmYdUbISMdCHzoPGlmQEU1ygruRVC1998UMiiVxGJ9Kot8bnsiZBCbAzVl2w_p7ByuLJHe1FLYP3PXRStCbHcrQTn6EASBIFg_SVmai9KcWz-3_Wf3awAKe3Cyx75qaglRI9VWCcqvTWVmNQjhDV-nbYyvb2xGl4LUmfKPTpSWWq_da1Nz10D77EpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نسل حسینی
🔹
همراهان عزیز خبرفوری؛ عشق به امام حسین (ع) از کودکی در دل‌ها جوانه می‌زند. در این شب‌های پرفضیلت محرم، منتظر دریافت ویدئوهای کوتاه از مداحی و عرض ارادت کودکان شما به ساحت مقدس اهل‌بیت (ع) هستیم.
🔹
منتخب  ویدئوها در کانال خبرفوری بازنشر خواهد شد.
🔸
ویدئو های خود را با الوفوری به اشتراک بگذارید
👇
#ایران_حسینی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/660752" target="_blank">📅 11:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660748">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4cd354ae1.mp4?token=HyCMeo58rSG5blTH6JQZMo8C6rmrmjbMLqX7Hm4iLffgZV7q4fry7pzpG4Y0Rj8z7AOggmSiiwdKpu6P-o8ITwZFfaXi659rUa5VpUT1zZZ4-uO9x3CaIkIG10bsYo7hOhsqaSvRHVCktUkTPFjiw6bFVqCg_JKOb01L7jQQ7jO3es-huJXDyKAsv13tfajx2vV1iqqALwIar2VrvYljwxqsqP0wZqO4owiYQR25R0RIiNvc5eWIOt0FnTnMb6gA-iJZT503dWrVToPoupBwxhzdnX0EywRspeSlNfRcVjKblIDT4hl8rBcDqxxCMh-FJ00pa7_y_esjgXZcWZWeqYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4cd354ae1.mp4?token=HyCMeo58rSG5blTH6JQZMo8C6rmrmjbMLqX7Hm4iLffgZV7q4fry7pzpG4Y0Rj8z7AOggmSiiwdKpu6P-o8ITwZFfaXi659rUa5VpUT1zZZ4-uO9x3CaIkIG10bsYo7hOhsqaSvRHVCktUkTPFjiw6bFVqCg_JKOb01L7jQQ7jO3es-huJXDyKAsv13tfajx2vV1iqqALwIar2VrvYljwxqsqP0wZqO4owiYQR25R0RIiNvc5eWIOt0FnTnMb6gA-iJZT503dWrVToPoupBwxhzdnX0EywRspeSlNfRcVjKblIDT4hl8rBcDqxxCMh-FJ00pa7_y_esjgXZcWZWeqYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر بیش‌تر از حمله اوکراین به پالایشگاه مسکو
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/660748" target="_blank">📅 11:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660747">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
مدیرکل آژانس بین‌المللی انرژی اتمی اعلام کرد که در مذاکراتی که قرار است در سوئیس بین واشنگتن و تهران برگزار شود، شرکت خواهیم کرد./تسنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/660747" target="_blank">📅 11:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660746">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
پیام حسن روحانی پس از امضای یادداشت تفاهم ایران و آمریکا
حسن روحانی:
🔹
باید از دستاورد تفاهم اولیه ایران و آمریکا حراست کرد و نسبت به توطئه و عهدشکنی دشمن هوشیار بود.
🔹
وی با تقدیر از نقش رهبری، نیروهای مسلح و انسجام ملی، تأکید کرد امروز ایرانیان به هویت خود می‌بالند.
🔹
روحانی همچنین گفت همسایگان ایران می‌توانند از ثمرات امنیت و توسعه مشترک منطقه بهره‌مند شوند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/660746" target="_blank">📅 11:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660745">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGT2HanXq2dYLaa8JGskmBPNprUbNvz0w7nCpPG2Z4tJENfX1ewz28QhD1iLayN16faQoLh_NPayAjZvi9Rsupv_9nwj5yFxD7CMQbKjya8LklvwI5z8YGkZyRsoJ1hZbyecIEGfIQhP5wcWbMKn1kuDF7Ffpr5Iw6uQNXfjwpwxTXz4-rfebnK5KYzTLKcpT-4CgRFmQSPg6EpFmcgpC3FY_otQnA8lrvwa12m3MIWY5a8URwg2n6VBycMxLdL9kyy15KZJchvZfUr1wjg0gMs0hGUuBZToJhVIous-E5244GtnYvWq0DRUiWSc2XQoe-0IBJOSUdbeFuE6HxCVAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سناتور اندی کیم: ترامپ ما را به یک جنگ بی‌ملاحظه با ایران فرستاد تا ما را در موقعیت بدتری نسبت به قبل قرار دهد
سناتور اندی کیم:
🔹
ترامپ آمریکا را وارد جنگی پرهزینه با ایران کرد که ۱۳ کشته، ده‌ها میلیارد دلار هزینه و آسیب به امنیت ملی آمریکا به‌جا گذاشت.
🔹
او مدعی شد توافق پایان جنگ، ایران را قدرتمندتر و ثروتمندتر کرده، در حالی که ابهام‌ها درباره برنامه هسته‌ای و تنگه هرمز باقی مانده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/660745" target="_blank">📅 11:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660744">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9627f0fd63.mp4?token=G7Kg6h6VMW_edta6ZWx5E1EI3S466xonblugPinX27j1q8unV2eWmtG2t35_raM47qCi7mZqx6XtJ2GesRWi8VQiWNWfxMgzZ6N9n5sgntP5nGAKGTPwICH13kwHz0FdA6nP-AoqPjClabcr4ed2k9MKujhdCnMVO0APgE9MZ0cacRAei2uLJyysOWGounuui4EVyokvU8vkJyVR9q0YSm3KebiG4_mDG2rSrb4RyzlFC_w8HJqYepfMKJCGVSMNLGkePsjAYfwU0MoUlURIKoNWefRDgZuEU1LD4b69ZZJo-rC8qyJCg5JDXnPSaMYSRB6zxdMEQR4svab-pxvTVycZ20Qq8OzcYoLBLaKvEETPYfQ0m3xJxmjEmzNMsI5BcjShzbKK2_aCyPgAO3wUaIERwuvh8OZ92oNfOi86nbGuLYqpiP4l1b6yyHCz3s6eggfgDFSXrZhLud0AEMDjNCSFmPQvmFpzvwSKPCwQF-lB6Q1aq3uVX5xnSLzPombcqeku82egyMm4am9QDEAJPjyI1596YMCwr61M6WswIh0Z20Z_g95Pa9q_8vrJNLmqjQ3yH9Qd8XIQmWwZ506WZ_yZSlH7vKhPd1IiNcV1CZ1QdIzTzzez90YUJ5hI37wPlI1JV0Ue7sdxhI6l0n65pS50eLSxDyMrtpJrALgwYrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9627f0fd63.mp4?token=G7Kg6h6VMW_edta6ZWx5E1EI3S466xonblugPinX27j1q8unV2eWmtG2t35_raM47qCi7mZqx6XtJ2GesRWi8VQiWNWfxMgzZ6N9n5sgntP5nGAKGTPwICH13kwHz0FdA6nP-AoqPjClabcr4ed2k9MKujhdCnMVO0APgE9MZ0cacRAei2uLJyysOWGounuui4EVyokvU8vkJyVR9q0YSm3KebiG4_mDG2rSrb4RyzlFC_w8HJqYepfMKJCGVSMNLGkePsjAYfwU0MoUlURIKoNWefRDgZuEU1LD4b69ZZJo-rC8qyJCg5JDXnPSaMYSRB6zxdMEQR4svab-pxvTVycZ20Qq8OzcYoLBLaKvEETPYfQ0m3xJxmjEmzNMsI5BcjShzbKK2_aCyPgAO3wUaIERwuvh8OZ92oNfOi86nbGuLYqpiP4l1b6yyHCz3s6eggfgDFSXrZhLud0AEMDjNCSFmPQvmFpzvwSKPCwQF-lB6Q1aq3uVX5xnSLzPombcqeku82egyMm4am9QDEAJPjyI1596YMCwr61M6WswIh0Z20Z_g95Pa9q_8vrJNLmqjQ3yH9Qd8XIQmWwZ506WZ_yZSlH7vKhPd1IiNcV1CZ1QdIzTzzez90YUJ5hI37wPlI1JV0Ue7sdxhI6l0n65pS50eLSxDyMrtpJrALgwYrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خلاصه بازی پرتغال-کنگو در چارچوب رقابت های گروه K جام جهانی ۲۰۲۶
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
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/660744" target="_blank">📅 11:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660743">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkSbdhlcKO8SP4A8G50kC0XPQpeFD0u0UL7j2YtIlxH4DTB-LsfrLQ-6VsWEEbpwiSugk5EbA-SB0QTwUFTT3FwEeI3Uz8A9-pwMymw6IIp6k5NSFbVcsHP-q7udBWm_ZemmH4VxsuQ38yIBuWrNWXHjLxRnT8SxKuxcGnpJiIV1UAcd43JQo-4YEB_nkXxhv62KHrGQaeQS-FX37-ZI-Or8On8LrfCIyR12ZyaswtA0amUPFT4qtnsordWOs_pMLvjfFbAYoXHT7zg-zRdJS3cYCjpZEjpqc1s78IqZTKFScR8Nb8dLd_X7ZX7VEd39oWl4_YHcJHqw7PVFouwjTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیرس مورگان، مجری مشهور آمریکایی: این توافق ایران تقریباً به اندازه هر توافق دیگری در تاریخ سیاره زمین از «تسلیم بی‌قید و شرط» فاصله دارد
🔹
خوشحالم که رئیس جمهور ترامپ از این رسوایی بیرون می‌آید، اما شرط می‌بندم اگر دوباره فرصت داشت، هرگز وارد آن نمی‌شد یا مزخرفات نتانیاهو را باور نمی‌کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/660743" target="_blank">📅 11:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660742">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
رئیس کمیسیون انرژی: تفاهم‌نامه با آمریکا یک پیروزی مهم برای ایران است
🔹
دشمن به اهداف خود نرسید و بازگشت آزادانه درآمدهای نفتی از دستاوردهای مهم این توافق است.
🔹
ادامه مسیر به عملکرد طرف مقابل بستگی دارد./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/660742" target="_blank">📅 10:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660741">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دروس و ضرایب امتحانی آزمون ارشد ۱۴۰۶ اعلام شد
🔹
رئیس اتحادیه مشاوران املاک: نرخ مجاز افزایش اجاره ۲۷ درصد است
🔹
روسیه: همسو با تهران برای لغو تحریم‌ها علیه ایران تلاش خواهیم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/660741" target="_blank">📅 10:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660740">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4120a36b2.mp4?token=dYJfEDMLcPga2wGLMWJbWVTh66VEje2jnnLXHOMHCdd9usWphPYuyv5dsNTURu_CGZho9SlUNcHLW1OyiAhG7y3EhM1uIYyEwmIIyN68Pnn23zlHte2Ikrv2uURXr4poUkkdkArSX3xUOmKgXjZyRKV1NHZhUrbObtKRhoNGlmkzylX4UyRnKOiYDbCTtAvXnxcld3dCBYuCMTkVodV4nTDRK7HNFLfEfZHxkzjfXEfn8fVuc7EI8imjgfOO0O2PWhCF8DJarLEHtNskj03V1pSzh1LUA4rmmqiRoKgiFzdsQ7NhAB5eyz3R1gGfeQa4I5a9CI9EsfWhKXLIr70M9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4120a36b2.mp4?token=dYJfEDMLcPga2wGLMWJbWVTh66VEje2jnnLXHOMHCdd9usWphPYuyv5dsNTURu_CGZho9SlUNcHLW1OyiAhG7y3EhM1uIYyEwmIIyN68Pnn23zlHte2Ikrv2uURXr4poUkkdkArSX3xUOmKgXjZyRKV1NHZhUrbObtKRhoNGlmkzylX4UyRnKOiYDbCTtAvXnxcld3dCBYuCMTkVodV4nTDRK7HNFLfEfZHxkzjfXEfn8fVuc7EI8imjgfOO0O2PWhCF8DJarLEHtNskj03V1pSzh1LUA4rmmqiRoKgiFzdsQ7NhAB5eyz3R1gGfeQa4I5a9CI9EsfWhKXLIr70M9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عصبانیت اینترنشنال از امتیازهایی که ترامپ مجبور شد به ایران بدهد
مجری اینترنشنال:
🔹
امتیازاتی که ترامپ به جمهوری اسلامی داده یعنی کمپین فشار حداکثری، تحریم و... کشک!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/660740" target="_blank">📅 10:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660732">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c2J1xbQkV4YONIqQLMyl4P54pT59YmvSok3K40wjPSw6GB2ugWxByFObkllVKWsMHwaYAbQtZKGKkoSSpryK3wgtpL6PXuBU74GhDD_EiN09GrIf2GNkKBSnqSzdxcH81rF56gTsKPHNHWaMgFZenGzy_78_1jWMdC-6OFJfB3HEDXMvO3xr_Oscd9Ry8vEB99C2Rrfnq7JkiFeE0oz3aX05KRhWu5YrSNwJRTC1RNr_VH92Df50SAGBZQh25I023iPn99Gdt3-0dMWuTnuF4E5vBC4jExXM5g3lC6aCgcXGd5sNjHdzY4RbVUfywEtebcSDgIm-zyJqxaPUfgKH3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OEA4q74ZX3LxcBz_zD031PqgxTdrSQfdptE48yoy-uQLOC2BuCA4L5vn7j2c7Lm_YqLxTLM_DCPY9x633fZMJtzTSWPvvKIXRcijb3hEsoRlWV4X_Y0BwUTGU-2rbKMZkb32ApBmPFC7BuPKhq0jHdEVqB94q9P0WhOU0rlZXtkF1SFop98wjm1IdEnvGrw60V3z8Jv6iw2Q0bpbkD0sxKJRbjc0uFJjnjJGN-vKzf-Msb-i1XnfjCMrrHgDedXOFnKmBQJsgmm7QRKrlKRGol2iU641LssXIatEvYNNI1H-tz9kWoBhGSaH5EE9gr713ixvPr9pmp7Y1mxPYUIxSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cEfy9nKWm3bwMCOrZ3BCmPtpCaDwX7KRQ2wIvCfLcrUd-tfftCRfQQ26tzkxwJqWEc5rDSUoerLiN6MaHVj7ql5vrUMRrvvFvAHV5bSSXzHgCAz-awU7NrMxPvVDjBcpNdqG9wdIwCa7Q2OSuv35T1Y0-MoO8Qag_vG4Dined70AEAsMOoGHHnV7ShQ-XmFwDZFi9IwIwKED_vsUUrpjkmd8QONY-FjlmSYHsfXo4KjaxirYRkiIP6ZpUmeYpS2AivlruVee_p-HC6wiJ2hBBDhLMDd03bB0YhgtDi4hTtpv1afeSIg9q0EgDXcpdlAq8QQhRFR7qzqm9tMcpqLfKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G34-LcsqAY6aewqXrOD4-RMr1EjOeTXTdFTDYx1vwFI8T_vd1K-6PhFsoWX8YDmI0Yt3KSbVkF69xRPMfEpsCH5qjnfpCXxyzgLqqdufOuZvF8JU3Tdcha9y0CWSaiF0T06tHOkgpWME7iUlV4iaMFVFrkaSM61YBL2fbVKUpNzWN4ZdZqeim-ZZceIcwB40dr3u9OvAHnSOcnN3en78GNmsdYrDNTuco_CLf0b7xMyH0aAuY3kX4d9EbD4zSzdV9GHEqHRPm-WAzZh5b5l06MTk7aUJ_8Ia7smdgb8Bv53SArT0PLzdGVlHl_egp-QgBRa1_HmNqA_yUnPE0_kihg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/afWAvf7lmIDGo1P0ODkvJs8K6QFdgeEZByQHqCVNpNukrCWXn7U78kq9gANel6WSTHMa-BI0SIM2V4-IUnu-GkBYJoAdogzkU2lUcvF28y7qud0lmQAuC1wej5pa-q88RTO8gojHXr8PKCphFJ59YxJ2jQHd_yWkbWdnmaGqISo97czStofugWjA-L3BYgwp45uCO-0mBsl-9sNZt7iJsf64veUt-GImkd3ImhERryNyvivG6fCbpgEW4Asizvj3CnVY4vJovOXSJZ3s0tVGvwsLXlBnd_ocHDKxWHy4IPRtRwI_6em572FW1yljCE5h_S4EGnd1X6-6c8-CnvWCgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXelC51VRHHBZ6a-IK2iodE1hHMpgq0cj0yxnsSQLj2LH8cQ89yfkjv78ANzH6SK2OGuOh5hGswbQxVCTo6otd54xmqtEr7m2T9l7rBRps0EoOZWGJvI6nhA-sPFMGWnyfZMxrXs4sFZ3sQQBrmnU46IHojwz0P58pDOl9zFKRsT9gSQzw7SlkOSE9EaNnFpjj2BEirZ4twNa3IPK00OJDy5RMBHNytLY6gi0vgw5HxRh2ZlgxeiFr1Oxlw77jKRH10WiXIe7WOhGLpZM1vBscWdEfnaIQayfAVvvOzwW7pP8mWCnteh1TC-XHNYOV8-e_LA7cHLZOvzR6J2bAQUxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RArd1Mqg2ojIaL88nWAX-z1kFz45LQjvL3z3tu-a2lcuV7ir_yzFEn0QTibRRm9FHju6Sa-DFNS8l8Mr9Rd4Xi8u-_hOwjmOCkhreD3ZHjCy5danr2jeGtfNshqDwGxamJuh7pAlIjocuuf_QHZN76lp065RRJcuNVyGugL6eXk8i9GDfyX11gGPe6ocGOfbS9IZOC1yxOudw5SW1ZBRUdu1TUyAHKsRWe3MpgdELG4KN8wMMrhvnFusdmMWRFcbr3BGdEBbS8ys9ZGISAYvwEI33H4gj-pfsnQ1lUfClfARhuINBp21cYT7Kd40RHxMLNHaqaim1HoXb0oKXdvjKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نقشه تأسیسات اصلی فرماندهی مرکزی ایالات متحده که در جریان جنگ رمضان مورد حمله ایران قرار گرفت
🔹
Camp Buehring → اردوگاه بوهرینگ (کویت)
🔹
Ali Al Salem → پایگاه هوایی علی السالم (کویت)
🔹
Camp Arifjan → اردوگاه عریفجان (کویت)
🔹
NSA Bahrain → فعالیت پشتیبانی دریایی…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/660732" target="_blank">📅 10:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660731">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaXKSXDcs-rT5DGFO-4oM_XcAPpc61JT5xZseYMWCh5o3AXM-9e2_LaTVKtsRoLrMsh6fq8znxgfzlVUqgKKY5UGovmJeBHz7D2iV1OCkkPXeQxyK9LkoBBD5L4jLUvgiVjqGxLS7Tr0tpQcnAbVaP_owRrZ4N_9XFbJNDfCpZH7WH3Evdlnzqcd9GHEhDMDRXLAlv-r9OJ_0Xl2CvP8R4BuG6yEnLO-m9ZZ7POZ3CZOvDkE15pr1J6tBITB5U996hydkBx8nYjvTwsN6XUWFmr37VB9ELlkIfjxrxN3-LOnHotDBfa6iz0QM1xA7LFZyXRpM4Q6w0NWzGLmfUf9ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بمب یک تنی آمریکایی ـ صهیونی در سنندج خنثی شد
#اخبار_کردستان
در فضای مجازی
👇
@akhbarkordestan</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/660731" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660730">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XISONFoKwl2rbtOJ8iMjfqykjBAPJCU3YCldardNOGu20crqGdh3GK6fObnEFu1RZBkkNnOb88AsnkgYV_-R6_Q7yJ83tUPWF3-AcpwjAcx6PAX--yRYMdQeVIBIxKsMS4yckrmp5ZsiYTCbVTRoJXuh87sC04M-B1DEmqClg59reNl-SyPcs_0TG89sj93JR7kP2q2Cq-pkg9WfNOdJlw_pcrJzulYoCW27v81QZCf5lrjcrkQuVt7W2OVBPB4Vp9B9p3-OAs-J7Fj-5Tk9clvVYRmCTBw6Nn8LjyfPP3SGsCIRmYKq4nkdafKpdVPo1yI9Ks528N-yQqo_7WE1qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه تأسیسات اصلی فرماندهی مرکزی ایالات متحده که در جریان جنگ رمضان مورد حمله ایران قرار گرفت
🔹
Camp Buehring → اردوگاه بوهرینگ (کویت)
🔹
Ali Al Salem → پایگاه هوایی علی السالم (کویت)
🔹
Camp Arifjan → اردوگاه عریفجان (کویت)
🔹
NSA Bahrain → فعالیت پشتیبانی دریایی بحرین (پایگاه نیروی دریایی آمریکا در بحرین)
🔹
ISA Air Base → پایگاه هوایی عیسی (بحرین)
🔹
Al Dhafra Air Base → پایگاه هوایی الظفره (امارات متحده عربی)
🔹
Long Range AD/Radar Sites at Different Locations → سامانه‌های پدافند هوایی و سایت‌های راداری برد بلند در نقاط مختلف
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/660730" target="_blank">📅 10:36 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

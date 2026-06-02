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
<img src="https://cdn4.telesco.pe/file/CYmjr-x9uLu12tVcN89f4EPKRSCW-iJ0vcLSZoz6WpS4YEE4r-P40kipEEVDx5Zjel7R83iyHKQ6g_zhbpQPN9SdHGSYhxAiS-N45iCfY3bK_6AdPYRGVodCQPJmtx04sUTGNTyYfRxx6IlIz7UHd-VHiyULVgbQjApRS5zHM4PgTUg4HQBTlV41MOqWAU5vrOBGL9dh43s6aGTAGDgmXyevds8eEjcDi0GcIFKmLS5zWCETgwvOpNIXMEp_LBNdOl8xs0Xgz39GOYm2d-FG0YyB7wH4Ys1CcM-UJJ67rHjxyJL6rkO1ET5DMr2Wk1-qT3SNXua3lj-IP1cSU5m9iQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.01M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 02:45:20</div>
<hr>

<div class="tg-post" id="msg-655640">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
حملات به بحرین و کویت ادامه دارد
رسانه‌های عربی:
🔹
حملات موشکی و پهپادی به محل استقرار نظامیان آمریکایی در کویت و بحرین ادامه داشته و آژیرهای هشدار قطع نمی‌شوند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/akhbarefori/655640" target="_blank">📅 02:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655639">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0969cd4eb.mp4?token=Vib-Rz96Qsgo7Jj0vkxrLQqgNArRE2XojguKWgZIzJhDbPRatKLheHDO61HzZqNoiszqaFqt8puBYJ6SOK5LegOOkAxU8OoGXDkdjVmLiDHCDg-hEzOyOlriTZBC2Puglus0qHd163-hEvLAxHZiWVBEHFl61RZvesbyq49iplEteV80TBi6Xuz1WGaql2k82ThLCvmbk-YY4JsPKV7MpA2Lx9QRvqQXUkApGw_6Fb_fqDVZhs4f9yn0y15Qx8HcJ7W1gnrECk-2vinQuOAVu07bG0pFnHy8gr-3q72WEnSpJej85O6bPDPgZ_7d1T6dcNXyy9olKfUWa4aKqMnoyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0969cd4eb.mp4?token=Vib-Rz96Qsgo7Jj0vkxrLQqgNArRE2XojguKWgZIzJhDbPRatKLheHDO61HzZqNoiszqaFqt8puBYJ6SOK5LegOOkAxU8OoGXDkdjVmLiDHCDg-hEzOyOlriTZBC2Puglus0qHd163-hEvLAxHZiWVBEHFl61RZvesbyq49iplEteV80TBi6Xuz1WGaql2k82ThLCvmbk-YY4JsPKV7MpA2Lx9QRvqQXUkApGw_6Fb_fqDVZhs4f9yn0y15Qx8HcJ7W1gnrECk-2vinQuOAVu07bG0pFnHy8gr-3q72WEnSpJej85O6bPDPgZ_7d1T6dcNXyy9olKfUWa4aKqMnoyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جولان موشک‌ها در آسمان بحرین
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/akhbarefori/655639" target="_blank">📅 02:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655638">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
دفتر آیت‌الله دکتر محسن حیدری با صدور اطلاعیه‌ای، ضمن تایید خبر سانحه رانندگی برای خودروی حامل این عضو مجلس خبرگان رهبری در جاده هویزه، از سلامت کامل وی و تیم همراه خبر داد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/akhbarefori/655638" target="_blank">📅 02:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655637">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
منابع عربی: آژیرهای هشدار برای بار دوم در بحرین فعال شد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/akhbarefori/655637" target="_blank">📅 02:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655635">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09037a0fb6.mp4?token=lzotbB_NvgUGtAGrlh1tR-tYkmWcIYssjOzB9OVCPlgIyqGyUPkDh1nZxI3C76HrMpcXfe8XmHJiBl7rXo4S_2X2dfmQkP3CGqanvicLlKRoWoxwUomUio_0TyNYJgyDwqd1xMG4dymV1QBdvT-R1xSFZ4JqYrBfGd4iivjAJH0NmluJJFk50wWL7s_HZnfKCvM9rSru21zasDrXxh9DVgbYiH1A09uzgiQ1FORjzuRlfAltLfF9KoN2hNOdWn9ac3zhROZ2ZiiI0y2z700Wa2kujH25sZ6mSnCoT6CyPlZSwPxm_NSbBsNOATiWPEsCpoCVEw1TnrCxF2UYRSGNbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09037a0fb6.mp4?token=lzotbB_NvgUGtAGrlh1tR-tYkmWcIYssjOzB9OVCPlgIyqGyUPkDh1nZxI3C76HrMpcXfe8XmHJiBl7rXo4S_2X2dfmQkP3CGqanvicLlKRoWoxwUomUio_0TyNYJgyDwqd1xMG4dymV1QBdvT-R1xSFZ4JqYrBfGd4iivjAJH0NmluJJFk50wWL7s_HZnfKCvM9rSru21zasDrXxh9DVgbYiH1A09uzgiQ1FORjzuRlfAltLfF9KoN2hNOdWn9ac3zhROZ2ZiiI0y2z700Wa2kujH25sZ6mSnCoT6CyPlZSwPxm_NSbBsNOATiWPEsCpoCVEw1TnrCxF2UYRSGNbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع خبری از شنیده شدن صدای چندین انفجار شدی در پایگاه‌های آمریکا در بحرین خبر دادند
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/akhbarefori/655635" target="_blank">📅 02:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655634">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7331c1131.mp4?token=EfS1yF2mRpBrnFHTf_2LTrvW-RySI5NuA4bv71P2anUPb-qzeZnG729hfSATWjfH72djWsSwn-wGDFu2kVFk6fwpSPQpsuLO7-wfdMV3NPz1jvj-6QFYGANZMUeUMJVK1_reLzC7ZigX0dn_vtpfbDPLn_854WUzE6IftbHOV1gJ9EnIZP-k2v6penNP1dfXIYqoKVlUuCbDWNO6jEGybGxPqjfb3UGxffPmnsTM2V_eOzA8VAUtgAFGv6ZwgVzNh-uBHk1q8Am6umJyn6cvRUg5L3TxwtBcjU54ea9wqJZrlzSg3KwVgyZ0G7NyCogh6mNdYLvkAe9P-ueRtjzJng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7331c1131.mp4?token=EfS1yF2mRpBrnFHTf_2LTrvW-RySI5NuA4bv71P2anUPb-qzeZnG729hfSATWjfH72djWsSwn-wGDFu2kVFk6fwpSPQpsuLO7-wfdMV3NPz1jvj-6QFYGANZMUeUMJVK1_reLzC7ZigX0dn_vtpfbDPLn_854WUzE6IftbHOV1gJ9EnIZP-k2v6penNP1dfXIYqoKVlUuCbDWNO6jEGybGxPqjfb3UGxffPmnsTM2V_eOzA8VAUtgAFGv6ZwgVzNh-uBHk1q8Am6umJyn6cvRUg5L3TxwtBcjU54ea9wqJZrlzSg3KwVgyZ0G7NyCogh6mNdYLvkAe9P-ueRtjzJng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از کویتی‌هایی که هنگام رانندگی سعی دارند از فعالیت پدافند هوایی فیلمبرداری کنند و با ماشین تصادف می‌کنند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/akhbarefori/655634" target="_blank">📅 02:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655633">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
منابع عربی از به صدا درآمدن آژیرهای هشدار در بحرین خبر دادند
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/akhbarefori/655633" target="_blank">📅 02:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655632">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
منابع عربی از به صدا درآمدن آژیرهای هشدار در بحرین خبر دادند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/akhbarefori/655632" target="_blank">📅 02:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655631">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
منابع عربی از حملات جدید علیه مواضع امریکا در کویت خبر می‌دهند/ حداقل ۲ موشک‌های جدید گزارش شده است
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/akhbarefori/655631" target="_blank">📅 02:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655630">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
منابع عربی از حملات جدید علیه مواضع امریکا در کویت خبر می‌دهند/ حداقل ۲ موشک‌های جدید گزارش شده است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/akhbarefori/655630" target="_blank">📅 02:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655629">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
آژیرهای هشدار در کویت بار دیگر فعال شدند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/akhbarefori/655629" target="_blank">📅 02:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655628">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
مشاهده شدن بقایای موشک رهگیر MIM-104 PAC-3 پاتریوت در کویت
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/akhbarefori/655628" target="_blank">📅 02:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655627">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
‏گزارش‌ها از عراق: وقوع انفجارها در استان اربیل
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/akhbarefori/655627" target="_blank">📅 02:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655626">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
‏گزارش‌ها از عراق: وقوع انفجارها در استان اربیل
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/akhbarefori/655626" target="_blank">📅 02:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655625">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
اکانت اوسینت تکنیکال: حمله امشب به کویت به نظر می‌رسد گسترده‌تر از دو حمله موشکی قبلی باشد
🔹
ساکنان محلی از چندین انفجار (بیش از ۴ یا ۵ انفجار) پشت سر هم خبر می‌دهند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/akhbarefori/655625" target="_blank">📅 02:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655624">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23967e641e.mp4?token=A8SddDRbdrplj5yntrQm5GGtTx2H_6NatiXrLZEXGcrAUnXuzIneHDPSCFn1byL-5KRzQVkppenHTnxk5E_VvHSMT0i_icsZy_ODsGtX9XYtIMjImriU-cAO_7iU0c9fi0Y5sL1hAmefwSSr7z6IsSH5KNiz1wE24L25LIwB2T-MYjLMa5Szfg9Yu_C3Dkr-Wq12D_k2iiMJJw0EhZvP-LkCOk-895cR1rGxDEhRgmWwDmVx-JLiVvbxol7_IbqFs04cZQT1PxcwEzBg015rb22Hq6dgluo4vVqZ19g4raE6gQDlJ4ZnSwGDHvWT6qR72ndMdQYBtPLFvpKjvnE7lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23967e641e.mp4?token=A8SddDRbdrplj5yntrQm5GGtTx2H_6NatiXrLZEXGcrAUnXuzIneHDPSCFn1byL-5KRzQVkppenHTnxk5E_VvHSMT0i_icsZy_ODsGtX9XYtIMjImriU-cAO_7iU0c9fi0Y5sL1hAmefwSSr7z6IsSH5KNiz1wE24L25LIwB2T-MYjLMa5Szfg9Yu_C3Dkr-Wq12D_k2iiMJJw0EhZvP-LkCOk-895cR1rGxDEhRgmWwDmVx-JLiVvbxol7_IbqFs04cZQT1PxcwEzBg015rb22Hq6dgluo4vVqZ19g4raE6gQDlJ4ZnSwGDHvWT6qR72ndMdQYBtPLFvpKjvnE7lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشاهده شدن بقایای موشک رهگیر MIM-104 PAC-3 پاتریوت در کویت
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/akhbarefori/655624" target="_blank">📅 02:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655623">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در محدوده جزیره قشم
🔹
بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است.
🔹
بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست و هیچ‌ یک از نهادهای رسمی نظامی و انتظامی…</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/akhbarefori/655623" target="_blank">📅 01:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655622">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
صداوسیما به نقل از منابع عربی: انفجارهایی در پایگاه هوایی «علی السالم» محل استقرار نظامیان آمریکایی رخ داده است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/akhbarefori/655622" target="_blank">📅 01:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655621">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bf52095be.mp4?token=QknG6FsphHwzxTYd_xzyephGOh2yfVQRJZP9Jv94bR7dni2cFuFIqsvpQ_SBxDlfHN9wStAHBwFc2p8UW6InawrK8W9GF_i7RkikLGwpVdfu4Eq3wyxvR7nTtc0LiysTCxZ4cfWLbiqyxwiiFmk2pB4tn9CW4s5z2mLxMQafr9M0zm6xS7D_zWU7p0n5Jw24vAOlTO72ey3rJt_V20IYQR_MNJDram-4E3coj6gC_5cYq3kRNWHBxel3lIGXUe1xRXp3E-Azt7orK2ZnJr6WUrT9ZePbgQpnU8c7RPaADq6NEoS1hkLFzclF446a8HMEbjUPK94BUR3kUxwHkv8g9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bf52095be.mp4?token=QknG6FsphHwzxTYd_xzyephGOh2yfVQRJZP9Jv94bR7dni2cFuFIqsvpQ_SBxDlfHN9wStAHBwFc2p8UW6InawrK8W9GF_i7RkikLGwpVdfu4Eq3wyxvR7nTtc0LiysTCxZ4cfWLbiqyxwiiFmk2pB4tn9CW4s5z2mLxMQafr9M0zm6xS7D_zWU7p0n5Jw24vAOlTO72ey3rJt_V20IYQR_MNJDram-4E3coj6gC_5cYq3kRNWHBxel3lIGXUe1xRXp3E-Azt7orK2ZnJr6WUrT9ZePbgQpnU8c7RPaADq6NEoS1hkLFzclF446a8HMEbjUPK94BUR3kUxwHkv8g9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری تایید نشده از رفتن موشک‌ها به کویت
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/655621" target="_blank">📅 01:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655620">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d593af6ec.mp4?token=amH5yJ7fZOSiqP0TZ5dCpz1uMzi9B1cJ1s8r1YRmwjYVkF1jinOlk52RQSTf4q2l-MNxFKjOYRGiyEAVpNHOPPlTR1JVOIDwwKi9LtFfCJGO46OntKsWZEzLXmhyNsprfybu7JJuAzsZZB5Tc8f1NqqgHQQz8HD_pBt_8HlgVtCL4UnRhMM-CmZiHGTcPb04BcSDRz5GWEaFDtcnOMh3TQnK7jdEtL3SDmykiEUUA9PiT1ySqQcLgJJv7hxnV5ZWx25jyLiLAIlGABcW78yM2rbseS0HZf4z7vFsVcBnY0hp19iiaGQKOlqdFSXo4CpolL74ChGBbeJc5EiGgYYXsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d593af6ec.mp4?token=amH5yJ7fZOSiqP0TZ5dCpz1uMzi9B1cJ1s8r1YRmwjYVkF1jinOlk52RQSTf4q2l-MNxFKjOYRGiyEAVpNHOPPlTR1JVOIDwwKi9LtFfCJGO46OntKsWZEzLXmhyNsprfybu7JJuAzsZZB5Tc8f1NqqgHQQz8HD_pBt_8HlgVtCL4UnRhMM-CmZiHGTcPb04BcSDRz5GWEaFDtcnOMh3TQnK7jdEtL3SDmykiEUUA9PiT1ySqQcLgJJv7hxnV5ZWx25jyLiLAIlGABcW78yM2rbseS0HZf4z7vFsVcBnY0hp19iiaGQKOlqdFSXo4CpolL74ChGBbeJc5EiGgYYXsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع عربی: مردم محلی می‌گویند که چندین برخورد در پایگاه‌های آمریکایی کویت رخ داده است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/655620" target="_blank">📅 01:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655619">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
تکمیلی/ گزارش‌ها از حمله به پایگاه «علی السالم»
🔹
برخی منابع عربی می‌گویند که انفجارهایی در شهر «السره» در جنوب کویت و همچنین پایگاه هوایی «علی السالم» محل استقرار نظامیان آمریکایی رخ داده است.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/655619" target="_blank">📅 01:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655618">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
ادعای سنتکام: نیروهای ما یک نفتکش خالی را در خلیج‌فارس که به سمت یکی از بنادر ایران در حرکت بود، متوقف کردند
🔹
نفتکش توقیف‌ شده توسط نیروهای ما، پرچم بوتسوانا را برافراشته بود و خدمه آن به دستورات داده‌ شده تمکین نکردند. یک هواپیمای آمریکایی با شلیک موشک به موتورخانه نفتکش، آن را از کار انداخت
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/655618" target="_blank">📅 01:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655617">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
بیانیه کویت درباره حملات هوایی
🔹
وزارت دفاع کویت بامداد چهارشنبه: ما تحت حمله موشک‌ها و پهپادها هستیم.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/655617" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655616">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PuXHvBJiMhZJldjeur7QXLPCsNdo5L-7IzEff4zeTVrsZKgB1Ze6aj0EuDwQeAdAMJGwMFsQLxxGmQgdk_1O5doWMafeTWwQZjFz5POJCMA9TSlAXWfY8FZpI2pm-cUgmaXBGfP4tcXMXT0wPtAMVAyE_ABK_jfACiEkJNypWtMPkKzVQhyDUbqwyg3rNH4UJzv1hwuP3LaKfsgQDUSYOZ4_z_tyQ71r6YRVApxqh_1mAIsH8RPGfrYEYyMNzljffRUVQHHo2yxZmmWpWZISAWTmOJiRGU0gWzT-VGAsHte-1xQLMV1C3mSDFTlZzD4oy9aNSNybXSG57nN975vJqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش‌ها از وقوع انفجار در کویت
🔹
رسانه‌های عربی بامداد چهارشنبه از فعال‌ شدن آژیرهای هشدار در کویت و شنیده‌شدن انفجارهایی در این کشور خبر دادند.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/655616" target="_blank">📅 01:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655615">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
گزارش‌ها از وقوع انفجار در کویت
🔹
رسانه‌های عربی بامداد چهارشنبه از فعال‌ شدن آژیرهای هشدار در کویت و شنیده‌شدن انفجارهایی در این کشور خبر دادند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/akhbarefori/655615" target="_blank">📅 01:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655614">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jltGqmim6iOGGxyN9uHAO_4ozTbIZsstVIweqmUM6d-pnj6kJk703maoWlZ3svc63iwu29XUTl7h0E9bg8m4x6alb6akkPffv87jAECU-nmTZo_sZtQ2rA18JQ9eLEfHcbPmiOBR_HA9b6yV8hgIajdNEVM9QxOYcqPVJpI9HL3Kw4Bv1KfxArct5JqtwPWkW3zrXpQcIeak0BmIqI-iCL1BsA0hglfZB-d-B3XZIEwgKVQC0puxm6wxL2qfUlYyIV2Av0lWAz7giJNmzbScJCVmgScYKboaVc0UnNHodzROQQ2W1haoP4xdKaqoOVs_28oQ1O5ZJ3AxFW0rSyqyvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مانیا، فرشته‌ی ۶ ساله‌ی همدانی، مبتلا به سرطان خون، برای تهیه‌ی دارو، نیاز به کمک مالی دارد
💔
🥺
پدرش، کارگر و ساکن خانهٔ اجاره‌ای، توان تأمین مخارج سنگین درمان را ندارد.
😭
❤️‍🩹
هر کمکِ شما، قدمی بزرگ برای کاهش رنج‌های این خانواده و بازگرداندنِ زندگی به این کودک معصوم است. نذرِ سلامتیِ عزیزانتان، مانیا را دوباره راهیِ زندگی کنید.
🙏
😭
🌹
💳
شماره کارت/شبا خیریه: برای کپی کلیک کنید
6037691990480709
5892107047084630
IR420190000000216756895002
پرونده بیمار
|
مجوزها
|
پرونده‌های تسویه‌شده
|
تلگرام مهرآمن
|
سایت خیریه
| برای گزارش پرونده های درمان زیر ۱۸ سال پیام دهید
@PoshtibaniDarman
👈🏻
خیریه مهرآمن با هدف کمک به کودکان بیمار، تهیه دارو و درمان، و حمایت از کودکان بی‌سرپرست و کودکان کار فعالیت می‌کند. مازاد کمک‌های مردمی صرف امور مؤسسه و یاری به سایر کودکان محروم می‌شود.
💚
کانال ما
👈🏻
https://t.me/mehreamencharityy</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/akhbarefori/655614" target="_blank">📅 01:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655613">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jk6SONKwZkrxrqvxO8lgpG0mFJV_3CNUwt9Qxfn3O831pPlNpqiP_mnPSP9DN6WVj6O3Jj3Or7pxAsWB2i9HFJ11LW3A5Qpjjkc-HdE7AdLy9CabhosFbdDKPlQpjHO1NYe3diCjB6bBJ54JYCKohUZv6qZpuroBO193DsHX-EmoXkdwFUSXbjgz8Y6b1ZxCMCzvcpFigLksZ6ZM0InOgK_F_kbc32bmmBJLJqWC5ewjGyyXfiUqI6NJONXnr4bamqH02AxIpVS6atd9xs9zn4I1p4QVU527tx3EHsOCNyBADnhanKCmQIU3hskD898M7omRIRzUEDKiymjzKH2ogg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦷
ایمپلنت کره‌ای با روکش
💰
فقط ۲۴,۶۰۰,۰۰۰ تومان
🎯
ویژه ۱۰۰ نفر اول
✅
ثبت‌نام و استفاده از این شرایط ویژه فقط با:
عضویت در کانال تلگرام
و ارسال *نام و شماره تماس* به آیدی زیر
👇
📩
ادمین:
@robindentalclinic
📌
کانال:
https://t.me/RobinClinic</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/akhbarefori/655613" target="_blank">📅 01:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655612">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در محدوده جزیره قشم
🔹
بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است.
🔹
بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست و هیچ‌ یک از نهادهای رسمی نظامی و انتظامی تا این لحظه درباره علت وقوع این صداها اظهارنظری نکرده‌اند. پیگیری‌ها برای کسب اطلاع از ماهیت دقیق این انفجار ادامه دارد./ مهر
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/655612" target="_blank">📅 01:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655609">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruxcfhSNEMFbX297pfmESOTUeC2t9SYflLL7SvfQTC5GksA4YOOwvnYfUWEPNMoffJ-m2KK5FVp8lBEdzkLrZNW7gRfWZoK8EZzpeI2BTqqk5oK8SjP1G-fN_dqdeGDorOZPtXBErij-i6GeShKr_JNT3N4ddK06vInYe0sYwGAcWoFBRy72zw8CSAJ3J8DhcHPV865RRgRfGLS3J0V1gq_3knO67ABgPBP62qQdSZ5n7uycP1C5NUrLYJo-yD4OLnCIn4Prl8eHzxqWd_rdvYL-e9nx6HB47mx0dSNkawWBvGs3sOVjSkCrgDQnWlwmvrWkSuU-itOcsrzY5EjBwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
متوهم
🔹
مارکو روبیو، وزیر خارجه آمریکا، در اظهاراتی در کنگره که از سوی ناظران متوهمانه و دور از واقعیت‌های میدانی ارزیابی می‌شود، مدعی شد بازگشایی تنگه به‌تنهایی نمی‌تواند زمینه‌ساز لغو تحریم‌ها علیه ایران باشد. وی با رد هرگونه گمانه‌زنی درباره کاهش تحریم‌ها در ازای تضمین امنیت تردد در تنگه، تأکید کرد واشنگتن تنها در صورت توقف غنی‌سازی اورانیوم و رفع آنچه «دلایل اعمال تحریم‌ها» خواند، موضوع کاهش محدود و مشروط تحریم‌ها را بررسی خواهد کرد.
🔹
هفتصدوشصت‌وپنجمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/655609" target="_blank">📅 00:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655605">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sB0peTdfZCmGgyPtYyoVyx2Ndn0iaUPd0c8T_ASHGivlf3OyLqaSBSuZCHqiAgg18TSwLbF2rclrgWQkHkyRM2lS1zrXk2gAEG7LJyz8jpx44NjQaufwhwHx-T2iyXLcv-EYChYAegqMNusfx7do0Dc5sjjFC3G6x0mYB_yEdPNzIYSjAYh2AjzxSB0wEfV2L8WoKWq4225P77xIYZ8Msux6BC-ELhjsbJeJqsjmeg3xHG--eORSLqdtipochXCeMQyVs3vvUwIZ5qGmjtVf1xiGOCoZnp6k31r8JseKeOQ_MAxXfVdpC4MwmLWHcvgHvvyk5L5XKQ8X4ARW5WoQ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/akhbarefori/655605" target="_blank">📅 23:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655604">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
وزارت خزانه‌داری آمریکا: ما بزرگترین پلتفرم معاملات دارایی‌های دیجیتال در ایران را به دلیل دور زدن تحریم‌ها تحریم کرده‌ایم
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/655604" target="_blank">📅 23:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655603">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
تحریم‌های جدید آمریکا علیه ایران
🔹
وزارت خزانه‌داری آمریکا روز سه‌شنبه اعلام کرد که تحریم‌های جدیدی علیه ایران اعمال کرده است.
🔹
طبق بیانیه دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا (اوفک)، چهار فرد و چهار نهاد مرتبط با ایران، به فهرست تحریمی آمریکا…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/655603" target="_blank">📅 23:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655602">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
العربی الجدید: مذاکرات لبنان و اسرائیل در واشنگتن به پایان رسید و قرار است فردا ادامه یابد
/ انتخاب
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/655602" target="_blank">📅 23:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655601">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
وزیر امور خارجه آمریکا: ما به ایران اجازه نخواهیم داد که هر کسی را که با سپاه پاسداران مرتبط است در هیات اعزامی جام جهانی خود بگنجاند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/655601" target="_blank">📅 23:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655600">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تعداد خنک‌کننده‌های ایران؛ ۶ میلیون کولر گازی و ۲۵ میلیون کولر آبی!
عبدالامیر یاقوتی، مدیرکل دفتر مدیریت انرژی و برنامه‌ریزی امور مشتریان شرکت توانیر در
#گفتگو
با خبرفوری:
🔹
بر اساس اطلاعات مصرفی ما، قریب به ۶ میلیون کولر گازی و حدود ۲۵ میلیون کولر آبی در کشور وجود دارد.
🔹
از مجموع ۴۳ میلیون مشترک ما، ۳۳ میلیون مربوط به بخش خانگی، ۶ میلیون مربوط کسبه و مشترکین تجاری، ۲ میلیون و ۲۰۰ هزار مورد مربوط به مشترکین بخش کاربردهای عمومی مانند ساختمان‌های اداری و پارک‌ها و...، یک میلیون و ۸۰۰ هزار مورد نیز مربوط به تعرفه کشاورزی هستند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/655600" target="_blank">📅 23:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655599">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
یورش نظامیان صهیونیست به حومه قنیطره سوریه
🔹
منابع رسانه‌ای سوری از ورود یک گشتی نظامی رژیم صهیونیستی به مناطقی از خاک سوریه در حومه استان قنیطره خبر دادند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/655599" target="_blank">📅 23:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655598">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
میدل ایست آی: مالک برجسته کشتی‌های یونانی حاضر به پرداخت عوارض عبور از تنگه هرمز به ایران است
غول کشتیرانی یونان و مالک بیش از ۱۵۰ فروند کشتی:
🔹
این عوارض می‌تواند «خسارات» وارد شده به ایران در اثر جنگ آمریکا و اسرائیل را جبران کند/ انتخاب
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/655598" target="_blank">📅 23:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655588">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QuV1BqYc6oqY78Cdr7IgfFk44Ktw5z_bjeFwNtIfu2xJzn7wcqwvbwdvlBVN6mclRstPxbT7VDBKo0L--qM8BrGK1-rKU9eS4JVWfUvduRq1g5LjsWkdRqLFyXrY-af8oo5xy1bewdjzjkxy1lvHXXxpeuJrrW9CwJTs_nAplPJtpy3vd9BU1EeoG0AuBtl7xJ1K-suXBN1sS7PADa_iwzp-JvqAiSsw3gc63zRynFgFoYT9-NrNwKV8T8UbCx7l2NsWeFDLwJUXl-OqSdS0SVEaAKhNz2jvtiDGTY4WRWGRU6EXkg8awYb1G7i_A3mMW31rhPa3KueuHINNr_3-Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SVtZq-o4weV1ILwgECW6_FMpfaz_T04E5b2ZiV9WSDaRFYV0yHsBmBNj7vSdlyW5dofWAdFpFe4BILWJ4_E4vEhFgLlNuUHioUHYz1RRf_9XEb5udbpJL7PKMu6fi_ZEUKZaWMEvLN-Mn_rdhSzKKhekFCrGgm1xQ1jdx2XGyqMfDYEeFDMxG1ufgGzV6FAUnfCsrBZnvNMFu5M5aiFYVChglzNC2DjIJrAjG7EP8D3trM0eGg1OR8aspY27m2FLn7YIYlJ9SBcTuUb5LA7sHm0TOMz2G-QuVKt67Kq9afD5IGBwXRT94H8LMkbQGkHWJHsZPAtoOtgMAfHzofcXAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/svZkRAHUhdFaEllHoA3b1_raiXFuxFQBJsnwZp_CZjjcDlXRR3OVVmDCzjO2f3T2Y5Q4W_Z0x4aXXcH0EfjqRHCxZfNLfZ5JKJpr4vVxcvT_QtE_823P8Qy9iqk1v7p-ob4IZrdA2S4t0lemFEyMWnKNMCuCnPWJBfuN1QxgevG7d3QtV6-zh55xuPLLdidWjVxrXvyNwAJ1eJMZGQkwqXMfNO8DQ-_TUArBFVxm6-DbV8DrJWz8cj537lQcY6yqeL9UrcCE3BeYQ5rOJU4K9Xm0V8xjzLooRmP2TVLpXlynaTGdipllN14KRj4Bpx8kh97hXYGiitBXiNdtqSXYEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ccq0C8JCMIFRtKqOOXWP6PJwT0d4vfetjbfTizGwbfFBd0_CLFxuGwQOlUdahwZJFBRkg6RBY1mBI0AAPi8ZaJR-MDLsFKdHHqc7GDbhcLQm6LPtiXSVopo4rxqmaeZcX002-sS5fHR_SWVHzJ_1zKFmVtU7uoutfwkmTxpbALUzsHzG-L3W0Hu-E2WtaUWOnsaNRIn9Qvm-vRiOaZp0V_x5UU8MLzUBSgNnb7EJJIy6Bp5ss11fk4mO0gGckE-j0Nc7adkG0dgMU7NIzTA6iql8gmRF45KF2UOHFa92KFktjcujQbRp5FVvWePpSwuNxHUsE4Jak0Zi8QFWKIZaZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ePgDJQQp1XhSw5FAZxxNcRSgymiIH64tR4Q6HzJ7OFb2tZlqz1NdubQwYJDQWkiVCm09p7SHQbDJUbDzP9PXL9b8t1FoGghe9Nc8jGAMKSEsQW_J87ustVzuzQ_k_eB-W1vEtcmoHvbVWewFsa36Ol1flVYhJNCyMN5Irxzvxjftau3cP3MTOOm_et0PtzPJB84FDhwIkzBOk6oABa3PyWs8Ap7rovvVKzjNvFwry_FvFC5FcaILI6nknn1O20ANoIajYocQCoJdTtaWhrxC3XxhrLWJX0grS5PUSi5AnUdiVLDxyrOrbPPHBJ-7wpIJ5tTX6VmmYaIAJmXqNiyoNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/au2xZ8Tm8RQ2hcO3rsw-WG0Ec5eiZ2_zeEkMHm7sxKZQgyknYXHRX_44j0p1dJC6u8-g34Q-cEkddwTxBEJ7HSLrDbtMYzgoG_eG0xavjjrExlkxYkJgV-8O8PMbXLlglYUL4Hybb6jX1PsB_5fsyB1asthsV6RZAtLu5jmuZeTLkooG5YDIKUruptHCcf_bsGmhD8bsXjGSfxNGoXgP1X0tyj7nHmh363Isaweq9m4IJj8cjG3RHg6HirLacy7EyE5fTAVAeoSxR16g-tvx8xQz-KKA0KGdz6KWszN821S3gLNnQaZYtbGBSwpl7MuJxfq24s0CzmgwL_p0AHBnyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Simh_iveBEfwrQfftHeh9dDNqhc6HnSkS5PijmHyliTdhF9Bzq_qnLwy_xInVwALILLrW3tr_0Jn7I-n3zBR-SI9jsI3UMMbc_kJSNkOvXm9kbf0m0ADcm94i447vP96sg6JBFWMvz2RWhafXaHHW6t-OA3uzNIasXenXp4jUKt59apNldWGpysHW1aaTMrwzyXokwX09pX-lOyodk3sdr9STo7olj33Ibq_1tN7-z3qhkU2_ji_AEbESpOLqI6ufiDpqt9au9yWNvQYacbYobXUMqORwyY6L4p67QYcxaMKrXF7u4zpYOGo-XLTpPdHJSPILrB0UQmkD2mZK_TLFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bbMl0pkAaVlyF6jSM_DWV39740pAP_5cCeRCieP_619liIZVgrb6fTauDFVycja284DVIC8mCvHuwOmzd8zDzhWvi0dUIAUBKw3ikAxEtOQW8HdF08wAu800PM_PUDyFYZqB-TtQ-KghOSnw37Xc3nUle6GC7XgTEsy1-R3T3ICa_hQDS3uPBUBUnMVxEC-p8w0jRxHmfbpuOs0-0dg6XKgPxZ0Az9C9C5siz9QPtPKkE3V-ZTQskl4joKrBTYwWsA82Yz3mG0MJJ4_dWpeG_GTGAtdsVnlT1FP8HWRBtLxT30ZEx4k90S9nmU_eLkjcfUsUCgm-nQkPQxNDbRCzYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pWOsptmPBXZIuSKV2UVdLYFOYQJMZiBMrv0NertyHuscdE-lXjbIX9QFWCVn486qrbh7CFdS-DcxdklezfJJ9ULvy5yD0r15XRB__1oKusZhSRbvD2bBPbrl4t-C0vwkaMsB6LZ0IvRmvI0v_eFIDDkKx4g8iZ_kOL75KldVBPfpdkzz2Z7WAqSTKAB9dMeI6_sjeNZ8ra8WyOHkXelcgHgD4nJe9Std8JhU68_TtIQuW19DvnTsKtC-7WjZ7CPmtaVWIUkoC4b_VetspImCXyjFYZ7gy5xsnuznX-h6irXoa4RbJgHDM988rSnN1npsC7kLslO7ZloPLgrQ8nCJQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ak70l-4JfQUO3LFwsKQAZdo-O0D20gehLDLdBIf5blBSvIhrMCPN1Jh3oJxdzuhW-eHXRmaZ8YbeuVCobnLZEtpp7n7_gHy4ZqUrKQ_rsVlx6fKVa95omyxR89aL0LkVJbzYjWhk8sY5SDx819oh48wLvYrlM4eDZhope4YXZr1gJF7uKargycmfETHcnbznN5sj0-35RGOM8ImDBFAwMAUF-I3gO4t8Mkr1SOq8JxjMURbhwVxB3GgIzeMGxchGz1UCcFyxARLAdYUiJqGyAn2M9ro2-LjzFOPbrqmuo3Ojh67kAvs2EZ54z7rfizn_hRn_2kXx0KNaiZQeucaizQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قاب ماندگار ۳۶ سال سخنرانی رهبر شهید انقلاب در سالگرد رحلت حضرت امام خمینی(ره)
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/655588" target="_blank">📅 23:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655587">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔹
خبرهای داغ امروز و امشب را از دست ندهید
🔹
🔹
افشاگری آکسیوس از تماس تلفنی محرمانه ترامپ و نتانیاهو/ تو دیوانه ای لعنتی!
👇
khabarfoori.com/fa/tiny/news-3219715
🔹
جزئیات ادعایی نیویورک‌تایمز از پیش‌نویس توافق تهران و واشنگتن
👇
khabarfoori.com/fa/tiny/news-3219710
🔹
آیا کیم کارداشیان می‌تواند رئیس جمهور آمریکا شود؟
👇
khabarfoori.com/fa/tiny/news-3219908
🔹
سود هنگفت سوریه از جنگ آمریکا با ایران
👇
khabarfoori.com/fa/tiny/news-3219965
🔹
همسر بازیگر مشهور سه‌ ماه پس از مرگ او ازدواج کرد
👇
khabarfoori.com/fa/tiny/news-3219631
🔹
ویدئو‌های جذاب را در آپارات ما ببینید
🔹
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/655587" target="_blank">📅 23:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655586">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اعلام زمان دیدار تدارکاتی مردان والیبال ایران با برزیل
🔹
ساعت ۳۰ دقیقه بامداد روز یکشنبه ۱۷ خرداد به وقت تهران تیم ملی والیبال برزیل به مصاف تیم ایران می‌رود
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/655586" target="_blank">📅 23:23 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655585">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعای یک نماینده: کالابرگ تنها کفاف کمتر از نصف کالری مورد نیاز مردم را می‌دهد!
حامد یزدیان، عضو کمیسیون کشاورزی مجلس در
#گفتگو
با خبرفوری:
🔹
در حال حاضر با نوساناتی که در بازار اتفاق می‌افتد عملا عددی که در قالب کالابرگ پرداخت می‌شود کفاف کالری مورد نیاز مردم را نمی‌دهد و شاید کمتر از نصف میزان مورد نیاز است و باید دوبرابر شود. مردم به خصوص مواد پروتئینی را به خاطر افزایش قیمت‌ها کمتر استفاده می‌کنند.
🔹
یکی از اتفاقات بد در سیستم وزارت جهاد کشاورزی تغییر مدیریت‌ها و معاونت‌هایی است که به‌ خصوص در این دو سال گذشته زیاد اتفاق افتاده و عمدتا نگاه سیاسی بوده که موجب شده است ثبات تصمیم‌گیری را در زمینه واردات نهاده و تولید دام و طیور نداشته باشیم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/655585" target="_blank">📅 23:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655584">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOzs6rotKj6mEcXXupYVyp6TptUmuyAvt8obzEz3JdNva4Q5prutuGP4fknHOUNY9KmLlcJDssaFAFZyr7JbkrdISesHk2fxreTkWcqRoNbBQ3Xutvz0hXixv6J8PnckI3SI59WsR0bly_IQqXnE-HyFZJEgGlc0VySlcyUIjioRS799b48zBRXOHQ015U-ZrrMCurrCusulBeTjsBPr629_TACGJbK-mIiIBWEzM8_-J_89rFWHhF4pS4sXTGf8g947OSbAQD4VFjEoIrKyMNNbUromCqqZx_80mCE3kFgeNg81NuHQJzv1iEUMXxfvKVlgrpMCL7kQGb_H_n7ZyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط آزاد قدرت خرید وام مسکن از ۲۷ متر به ۶ متر
🔹
قدرت خرید وام مسکن در ایران که در اواسط دولت احمدی‌نژاد به کمتر از ۶ متر مربع رسیده بود، در سال ۱۳۹۷ با افزایش پیاپی وام در دولت روحانی به حدود ۲۷ متر مربع جهش کرد.
🔹
اما از آن سال به بعد، تندباد تورم مسکن، ارزش واقعی وام را در هم کوبید. به طوری که قدرت خرید این تسهیلات در اواسط ۱۴۰۲ دوباره به ۶ متر مربع سقوط کرد.
🔹
با فرض میانگین ۹۶ متری خانه‌های تهران، وام مسکن اکنون کمتر از ۱۰ درصد قیمت یک خانه معمولی را پوشش می‌دهد. نسبتی که در سال ۹۷ بالای ۲۵ درصد بود. میانگین بلندمدت این نسبت نیز زیر ۱۴ درصد است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/655584" target="_blank">📅 23:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655583">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
گروسی: توافق برای پایان جنگ ایران بدون راستی‌آزمایی و نظارت بسیار قوی بر مفاد آن قابل تصور نیست
🔹
مدیرکل آژانس انرژی اتمی مدعی شد فعالیت‌های هسته‌ای در ایران، اکنون «متوقف شده است».
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/655583" target="_blank">📅 23:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655582">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
گفتگوی تلفنی وزرای امور خارجه ایران و عربستان
🔹
عراقچی و فیصل بن فرحان وزرای امور خارجه ایران و عربستان درباره آخرین روندهای دیپلماتیک برای کاهش تنش در منطقه غرب آسیا گفتگو و تبادل نظر شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/655582" target="_blank">📅 23:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655581">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc167b19f2.mp4?token=TH1PxQ8rs9hUrT_yUmq1edQuYJG6Cfi_grYyvyUNS5I0KwlNP0Ze4AK3gRH87Md0LHXgNAPfwz_UOe1AZ5EoINux_7hv2oz99eUWKjcyP7ziSdf6w3lcBgwhp0dmz07sH37Pc1ndg2RRbf5EnnBop0SRB5ycog5vfHj-11nCyzdxoOaOLbhBxGT9JG_xy0ADcWtBOLEZJfEuk7lzSCvRo7heTAsY4yEl9yRZiu1-RYkSjixh9GBrz0YFdxO20LbmTVPLasaQessWG9G0FqD7oCSgRnNW8kGHXCAivq-sqBbja3sRrNJk8lxmfuvwuPkhgKwifw_jzPoI7EBqClo79A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc167b19f2.mp4?token=TH1PxQ8rs9hUrT_yUmq1edQuYJG6Cfi_grYyvyUNS5I0KwlNP0Ze4AK3gRH87Md0LHXgNAPfwz_UOe1AZ5EoINux_7hv2oz99eUWKjcyP7ziSdf6w3lcBgwhp0dmz07sH37Pc1ndg2RRbf5EnnBop0SRB5ycog5vfHj-11nCyzdxoOaOLbhBxGT9JG_xy0ADcWtBOLEZJfEuk7lzSCvRo7heTAsY4yEl9yRZiu1-RYkSjixh9GBrz0YFdxO20LbmTVPLasaQessWG9G0FqD7oCSgRnNW8kGHXCAivq-sqBbja3sRrNJk8lxmfuvwuPkhgKwifw_jzPoI7EBqClo79A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور معترضان به نسل‌کشی در فلسطین در جلسه استماع روبیو
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/655581" target="_blank">📅 23:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655580">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
استعفای فرمانده ارشد عملیات ارتش رژیم صهیونیستی
🔹
سرتیپ و فرمانده تیپ عملیات ارتش رژیم صهیونیستی، در پی آغاز تحقیقات علیه خود، از سمتش کناره‌گیری کرد و خواستار پایان خدمت خود شد.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/655580" target="_blank">📅 23:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655574">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/muF3l0ni7g7hf_Oy7kLr2O8LaZDONTjcRpu9CGUcbiuA423I7xyVJTnMIv9F7oXdvC5bX7C_9k0itpe_b8AcrZKQYaJOwomwYrOtfZhQVY6Z1P9So4n4K2xzPUiamwgQE3fjlmt2PA9fikTiPyQ4HgARNNJlrHVUmEUuU4YuJ7Pf817FojhWE-PVuinDhatrJmZjU_EF8ZgkT_ZHDdLWqMPW4h8Ys6xSfkDAfpD0CLeH3LgjRmG2AP9KZ_EBSN-WxtZ0gjjVMOuTFTmC60o0Bic_BTsOzkniHm3fyiGaZuWSkrdejoSAb1j6LA4QitgHHSugTXoaIY2A-VvINooaUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vfChISFEtcz3-D7bDj3X3zbK0eLxg_8ErXvmTNLJsrw2V6tKSy8D-CbWF7IqE9OcnIjfKOQ_6SEJvpC_JMC9GhW8hPnBvt9urwuo2JJyQLM4PXYK7vRKAy7jCFbUSkRmqaxXtA9D4s05TtRy5psUGGPlvIK3s7kFjBXmgyt_hFQFI3r-X4pzOn5G2QEG1SNTXJePMkWVgdLIl1ltXPOr3QyuFY_M_SLJ_WVYC-lSih5c94jWHieknznuLpWMosmr55E8fqUS3AR5VEI8vVmihoXdqUXNLQulZTPKwJFtn3O7uBWws1k2VxBDzBgutdXwR-7SHv1ZWrho3_YcNCf6vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rkCuqaHtk0hRr_KIzuBW7p8NY9m3ecBPLCs24evrzLPnyIQ-U0ZKHrgcCLbHQxYW-oGOKAVYaZi5gdrMmCNX5grVy5AOl_9SbWBg0YKrgDy1EGr3PmPpeU4GclMNfprGogW-rLPlZYOz_OGxUsUVkDzobdaBP-doKxx2PPmh4JZ0UYdmtyl3OkIOSHb_IHkYZPCLGWA7vVBSCgUFUlItnrDaPTT0O6Bf54_9yNJ46hpzX_eOxeXxFXmLqGi3MVlaXgSz2PM-x7zeq96KjCsZlucelS2M8UfmqAtJpeduUua8wMX2gM_VTO2uCDqgh-1FebZ8xvoxuFHAbRPxfRWqkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QnbVnuAqNwZaQuD9vaHmuYLkuvPYQeBdlmifpQ8laV1yCVoKzep7TyWZxaYvAbdZRAmIeiWNs7e3p30h0VpMl9AueI4MBSQVhtOwXMVHZvd65bh3O15bgjn0N0lcZwCl1wx3q2_lW7cJbPzy4tjUDFImkfuwvxCMxhrZN1bHtAGibjP-t8xSfYKO86SQVUPX2levO1-HU9BXMH_LO6Bqj3faAtfMIsbNczoUZpEL48ykOmPtH6Mq90BPNz_E8X2T0_rwHFo7Brs56c5pZfj3cyPhxD8zjUGPcXcPL1WKZea6mArnGxvcg1NVIWr5yKFpsP1lhwaw8EpyJ4QROJAxhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EqtqWSWmMTlC3pfIchimreSjvz5-Jb7iVMxH9D5mDgaQXheNHyeG4KI56O5DlFWb42P9fFhIrQcA__JhTnBNGWkoe3L0TjLBWEclGSU_4Ibr455hhID7df4cMTzSXndOwvyWdV7JqTu_pJsv8nmfzMNZBn5lxvr929zdPgE95OPFzzEGloCW2ChjIP3GMiXbSiZ2S3xw0V9O4Sf72VjZ8tohaxv8JI2x5PD_wgTsw1wEdA0KPq6yqMG3C1WU9lelRj-42vjfKONUaZoejOclvHf_-eObtGqKpA6uXJC9B4eWtOwG5cldKm3iv2gsMcnQVythhFnHiuaHTxUl61k1Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O21XBnReZLULgX1K1jjaf16icnbB_qk8rt5qpqtyzd0ZK3-h6029U4M0GRkWTtNSZVpYoifL_T0mapRtfIfSzg02I-kj5-OtVuQ6MmU3HdskpoR49L1eKUSHrSA8y2rc3jm0NJ3i5AL8zEVCV43RHmBkonHOOiTSOv3UxMx6w0jwilvT0M9DHQMJTBZZ5bTDP0InvNDlmGBaPKS2qhjT187uPCcx5Cus20J6BN8p_hO4-h_Fwjcaitr6MwAIhrGeerfS0Sa8eybAlPwpXF3NTJ-ylwkBdF8NkcgIWmYgFWYzynFuDp7dblRkgqEp9m3cNKoGbUGuPTbnHtq4EXwW8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چند نشانه از یک اعتیاد پنهان و خطرناک در کودکان
🔹
اگر کودک شما بدون موبایل بی‌قرار می‌شود، هنگام محدودیت عصبانی می‌شود یا مدام صفحه گوشی را چک می‌کند، این اسلایدها را تا آخر ببینید.
🔹
اتفاق خطرناکی در حال وقوع است!
@Tv_Fori</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/655574" target="_blank">📅 23:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655573">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
تحریم‌های جدید آمریکا علیه ایران
🔹
وزارت خزانه‌داری آمریکا روز سه‌شنبه اعلام کرد که تحریم‌های جدیدی علیه ایران اعمال کرده است.
🔹
طبق بیانیه دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا (اوفک)، چهار فرد و چهار نهاد مرتبط با ایران، به فهرست تحریمی آمریکا افزوده شدند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/655573" target="_blank">📅 22:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655572">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqZ7-Z5ym1yNNZtvp07E7QQCtqE_5JVGoFP06gKO9_fzdn9CPXswUbjhaLTEDcKEQtd4e4Mt39SqmJgD-1G6SVps3farGIoXp4ozsP5hSziquYB6jT9G99vXNgbrzZz-rU04eK_NMtQYKg7b3WRJXQOjwHVvAa_Mml_OuUoFkAAoDQatbJaUjO_9AhLQODUla-VGAJHMBgMcpPOR2F80Ywk6SjgC3jJ6KcWrNiQZhbgZVLCYBOfU6vkQrOPGgsCMA7PITbnWHKTCSvt_Hz0_JxY0inuOSYOvwwfqY9IyDJ8AesEIx6sX-IXIMrBpXEy8woecDcPvt_rmnbmtxEP72A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این علیِ جوان را نمی‌توان دوست نداشت... شجاع چون شیر، اما با وقار و صداقت و عطوفتی که شایسته‌ی سواران نامدار مسیحی بود.»توماس کارلایل، فیلسوف و مورخ اسکاتلندی، این عبارات را در ستایش امام علی (علیه‌السلام) نوشته است.
توییتر خبرفوری را دنبال کنید
👇🏻
https://x.com/Akhbare_Fori</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/655572" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655571">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZ0Gyrdftzy5N2k5FspN5mDRyspeqnuaecS8C6SpB0Lziwdag3W8TXpH2wPFFPIpZjTcuRS7pl32UpNiKX2g7O-onVtp95DT8rx4zb_7abHWIu4MLlAHRbcJp7Rw99peiQX2TWOFmRXWKmkImogzigUBtlcmEDHzJioOh7CxyanJjBAF963SMEWyKwF0_Z9dbJIDVfYWbwGtspsSp8u6mrv-BkWGCRPnJQj99L3Q-eAR1GqIhwenlBOnwv-RjlcQKcxtrFer9AsKJ8URYrdYWz1U28ds3X13nG-w6kyVsCFi3_uUW1NtXPkA8DkGobYXEdJyT_5knMrD9vULa-xHmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از ناوگان پنجم تا تردید راهبردی | خلیج فارس دیگر برای آمریکا همان منطقه سابق نیست | پایان حضور آمریکا در خلیج فارس
🔹
تحلیلگران حوزه ژئوپلیتیک معتقدند تحول مهمی در خلیج فارس در حال وقوع است؛ تغییری که تا چند سال پیش بیان آن دشوار به نظر می‌رسید: دوران حضور گسترده و پایگاه‌های نظامی پیشروی آمریکا در خاورمیانه شاید به پایان خود نزدیک شده باشد.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3219954</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/655571" target="_blank">📅 22:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655570">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFkShfk2jP9hzH-Z18K7F7uQ6cyRogVz5vkE26pG6nTcmuXb_tD_liqZbMa8RB7TS57PQQ2A0aXgtQdUT2TTMIBMGlclo_MEpS-7tH0D5sMDrSYrs3xD9PNNKKRc_L31V3P24g5j1CRac3sUHwatmsGUf85Msr21X_xuZzqOjTgv1C2z08GhNLb3IHpPNj4p5T74_dbE0hKfLE2aAywziEFQQIQS-4tiwOk9t_BVrPG4dDcgr_PJcLRplL2M6-Qv-5Mb2TRgLbyqYLj93IFTIvYxSaaCDXorfMfm5LoTN8aNXaRA6TqrQFg67bc4_2feW98uGCYxoQ6MQMjoXFbmmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری متفاوت و ماندگار از حضور شهیدان شادمانی و تنگسیری در آیین پهلوانی و ورزش زورخانه‌ای
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/655570" target="_blank">📅 22:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655569">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0eztgqVoX8b7p_ObCO8Iy9SC_ghbA4SuRlw7A6pCxP7bGIRThYDCsBHblR72LEz6pRxxnVoiYhiSQCB5hZjyV_NBvfnpC4dS6__jcIER0M4QEhW6FYJndzY4RULnKeVeEJRaEaYTijSg2_AD9oc7Bqyg0lvH78wstXYnIoGJRmNTGgcZqD7j9fAOawYRbHNRxkvfI4gNz3ay6-youfMYEorpELgKs8kFaZorAlZ3d2HCPVLEjw_pJvnA8HyB1wJgJCfgf7V83RB3a29QYQuWwmDtnkLhPvIhBuMuBqom800Y48tmGlXl2DNvZMhLNOUCwZ00VuBx8Hw_Sp-5BTGGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قابلیت جدید اینستاگرام که شوکه‌تان می‌کند!
🔹
آدام موسری، مدیر اینستاگرام، خبر داد که قابلیت فوق‌العاده تله‌پرامپتر از اپلیکیشن Edits به دوربین اصلی پلتفرم منتقل شده است.
🔹
یعنی هنگام ضبط ویدئو، متن از پیش آماده‌ شده درست جلوی چشمانتان اسکرول می‌شود و بدون نیاز به حفظ کردن یا تکرارهای خسته‌کننده، می‌توانید روان و حرفه‌ای صحبت کنید. ضمن اینکه امکان تنظیم سرعت حرکت متن با ریتم صحبت شما هم وجود دارد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/655569" target="_blank">📅 22:38 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655568">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZbrqHqoCqrkYEQ9oxYFdfp_TLQKLANMaVQSiFyeZkBD3HamR-WVLJRleFG4-2g_xzcUk0Tzc_7DxHR87QtCpal7kcvlaYiSUCsqsry250Ta0r6Wkzgsc9XR6JuStvrPlGmunfU5h9AqVSyvLiYxATf91w3iaCmeGjh2cK8UYv7otvZBCSaYyn76ZhuUUT73iIOzHmhXJDpDhjZKTOMitj4ac6KcezP_hSHnkdqfp9Q6S_AvOKvjc-zaaoSD4ZRSd16_3u-STLaOprc7KwetFecnBMxMBJMv9av9tqc_08jFans2c3wm_v7OtO1xnI-dn6-GrM0zXN9km31qpd4uKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برپایی بزرگ ترین شهربازی دنیا در روز غدیر تهران
بزرگ ترین شهربازی دنیا در مهمونی ده کیلومتری روز غدیر برپا خواهد شد. برای درک ابعاد این رویداد نگاهی به بزرگ‌ترین شهربازی‌های جهان بیندازیم. مثلاً خیابان اصلی «مجیک کینگدام» در دیزنی‌ورلد حدود ۱.۵ کیلومتر طول دارد، در حالی که «مهمونی ۱۰ کیلومتری غدیر» بیش از شش برابر آن است.
«مهمانی ۱۰ کیلومتری غدیر» با ده‌ها قلعهٔ بادی بزرگ، استخرهای توپ غول‌پیکر و صدها غرفهٔ متنوع، به طور همزمان میزبان میلیون‌ها خانواده از سراسر تهران و شهرهای اطراف است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/655568" target="_blank">📅 22:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655567">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قدیری‌ابیانه: نتانیاهو فیلم تجاوز ترامپ به دختربچه‌های کوچک را دارد
قدیری‌ابیانه، فعال اصول‌گرا در
#گفتگو
با خبرفوری:
🔹
جنگ آمریکا علیه ایران قطعی است و این بار گسترده‌تر از گذشته خواهد بود. هم تهاجم هوایی و دریایی، هم دریا به ساحل علیه جزایر ما و هم تلاش برای ورود آمریکایی‌ها و عوامل دشمن از راه زمینی و نیروهای چترباز و ویژه خواهد بود.
🔹
اگر این عملیات را انجام دهند، هزاران کشته و اسیر خواهند داد و این میخ آخر بر تابوت حضور آمریکایی‌ها در منطقه ما خواهد بود.
🔹
علت جنگ آمریکا علیه ایران این است که نتانیاهو علیه ترامپ آتو دارد و فیلم تجاوز ترامپ به دختربچه‌های کوچک را دارد و نتانیاهو این را اهرم فشار علیه ترامپ قرار داده تا هر کاری اسرائیل می‌خواهد، آمریکا انجام دهد.
🔹
ترامپ بین دوراهی اطاعت نکردن از نتانیاهو و انتشار اسناد و برکناری خود، یا گذشتن از جان سربازان آمریکایی و ریسک کردن برای موفقیت، مانده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/655567" target="_blank">📅 22:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655563">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fAqSoG4QaCkuqWjvY_JOukjRiZwlGyxcgfyh_W2GxAo3Ht5mjRdIFddyUnmKDiCwk9WnAalmJfG77tqitnLh5Ru3YieNJzO1pzJVNjH9vfj10OZC814bm6p1IEEnH4mJnwMluHJjOn6dUOdut2JndqcK9qsctEPBhTC7Kko9Ul6V5GpbSxT2Xbt1MiG10oheO6V1XIpuiivuAAx4mG2Gqpl5jcL_xg-GWbQ8Wf93Ge2p9IyBUXsucCBmsIx_v6bArv0tQQEmMQJYnmzbghLcrpx_0svajQ5DcualOzuqU_1WPdagXkCZmG1Lln-xv9tKmuMAmG6i6uOAhHBjO6J3Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MufsaztEfEfDtlYLwrnmr-bW52r07zeQyBLHrnKfSifOSBxy7k4bEj_FQ8ehjicQKbeH-PDbEPoeSklwwAJgNhDnGKKmMYcccVDDLmDYj3xc9hz3BV2w7x2xC0cH5i1rm6PuDK5SQgPVKSkiw34BpdhacOOMYGNQ7Xzea6_aX_Nfqy03JpZHzxyudbVfuRtvfx402afodbo1Tp4aoszF4D-TsxazdKngr__3h2qrEjITbDrcKenVGfNh2T7fz5LfLeAzTavsgPel2rH4OepH4Zy6KwfBDCcXZjLbejyLeQdMTsu_2dMDmCc2CMROPfiYNFL41jbzwVZpz2406r8vxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/odMiPDlvMPwlYCdmehL8cPAbmB8fWFHKdj6TjOwRVnTBeF0oat11PO0JJXAX5AvWBOqNk2EOfNmM2S1ddGnRd3FLHCPYM_sJjbvAFkweeFn71Rxd9uTFkuILb4VY1eMFDJJUr1uznXHvZcb9kxh1BrXjAJwLa8ArAA17W4D0vs-Zx3592hTfn9EIxlNRl6AzDJ2TmMNysQnDaOsCUwckGETzfnRSg43N6tNYW2hViAXZR0Dqm91VnHgFY6_8DgnBIrKKQozouffhM9REQvvn6eCfoy89vPmnfA4BQUR7YADDjcvIACnFIkwQ_r2iPhuw8tIGln8CByQtf8hAVyaxkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آموزش کار با سلاح در میدان ونک
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/655563" target="_blank">📅 22:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655562">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی استاد رائفی پور</div>
  <div class="tg-doc-extra">مراسم دعای ندبه_جلسه 63</div>
</div>
<a href="https://t.me/akhbarefori/655562" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
مراسم دعای ندبه - جلسه شصت‌وسوم
رائفی‌پور:
🔹
0:04:25 آرامشی که خداوند به پیامبر و مؤمنان می رساند
🔹
0:30:00  انتظار واقعی ارزشمند است
🔹
0:36:00 علت بسته شدن تمام درهای رو به مسجد بجز خانه حضرت علی(ع)
🔹
0:47:00 ماجرای رقیه دختر پیامبر(ص)
🔹
0:56:00 معجزه قرآن در نزول است به چه معناست؟
🔹
1:06:50 وضوح دشمنی صحابه پیامبر با حضرت علی(ع)
🔹
1:20:40 سه خصلت حسرت برانگیز حضرت علی(ع) برای اطرافیانش
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/655562" target="_blank">📅 22:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655561">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8X7iesoZ_3kKBK8-E9Z3Hv8lnPjd3-XKC4PWfpdgJDuIw6eTbK-lEGXdE9ui8u_rPkx-Vo6bU2EvDfk7NB7ibSUa9QUFau72lRqJcMVavbBLj3l9Y6nbE1sFcqSDRqSRg2dbi5RdNtBd0Lo51OwDqAgKxGXA-j4oazgBJjzpgebscanxMTqECOStN9o4L-vzfCbrT7XTJf10hii-j1JzYsbrgo8kwgdMD0_bIJIBRaSh9uPcC4F085zrrizjUWOMNWyJGcfNl6fHHUtPaYQULZ62jikjhrOLpU3sbRRe12y1_y5T8IfK2klWEyVn2I5ZzWUolsv3ugzVBHc-Utw_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پوشش خبرساز رابرت دنیرو با نشانی از ایران
🔹
به‌تازگی تصویری از رابرت دنیرو در شبکه‌های اجتماعی منتشر شده که تی‌شرتی به تن دارد با عبارت برجسته «Hormuz Strait» یا «تنگه هرمز».
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/655561" target="_blank">📅 22:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655560">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
جنگنده‌های اسرائیلی ۲ شهرک در جنوب لبنان را بمباران کردند
🔹
جنگنده‌های رژیم صهیونیستی در ادامه تجاوزات هوایی خود به خاک لبنان، ساعاتی پیش دو منطقه در جنوب این کشور را هدف حملات مستقیم قرار دادند.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/655560" target="_blank">📅 22:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655559">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cfb7fae65.mp4?token=NEry9YOTZWf7AaCbijvGtmiD96zuvvofOdKsnTbq5BBiS8Np0RkVkMgxqoy2pW5WKdSfmlKE08QAqtdUc8-K3VbATKNNWQnAiY4xhaOs0QvcBWRysMLb9qYFbOZkIC-mnYxVegj0HVv1uXwZLk_jDE8eRzx7MPYLN4p17OHQa6NcDI8GIZVXX7KVH87xPHH94f17cE1UCRkShhNKS_rAolanGD_YVCL73F1DE4KIEPMINHQGHyLuD-2AkiDwdtDlTE73dv33Ba5jaxsL-jBXNmHkOLYCiI3VRo04P8UWsxTnboJi0VEs5WyKiFq24DTWhyiqnLFUGI9JskPZRNkAQXkpGMa4sJkQJp-rn4zaMrFvwKTL78LkTjJ2ylDsWZN6TlxPFya8nzmKkZtmOr65q0ILVrEKX4kKFifXWmzPxDyO4zhLfKVlrQhv3Hq-8Mnfq3tB5Y-m82wNWq9ZoXogFiPm09-DcSePkE9SYupoiPVKcl6TPj0CARiCiiM3qMFeiziDKefp5F4_xjTem_GpS9X1h_3z21yFFeJepdfIxfoc9uE5tHzyv3K-PTkZahk9GrpTIHYn2ejxjO_9lomd5Dg7t9wo_EUeEYvrjrqCoULbtRk3iPRA-RY6j6KJCHdxo4CBfclgPaCTC0EqINpE8zHEsx05kr2NG23NdDuaP44" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cfb7fae65.mp4?token=NEry9YOTZWf7AaCbijvGtmiD96zuvvofOdKsnTbq5BBiS8Np0RkVkMgxqoy2pW5WKdSfmlKE08QAqtdUc8-K3VbATKNNWQnAiY4xhaOs0QvcBWRysMLb9qYFbOZkIC-mnYxVegj0HVv1uXwZLk_jDE8eRzx7MPYLN4p17OHQa6NcDI8GIZVXX7KVH87xPHH94f17cE1UCRkShhNKS_rAolanGD_YVCL73F1DE4KIEPMINHQGHyLuD-2AkiDwdtDlTE73dv33Ba5jaxsL-jBXNmHkOLYCiI3VRo04P8UWsxTnboJi0VEs5WyKiFq24DTWhyiqnLFUGI9JskPZRNkAQXkpGMa4sJkQJp-rn4zaMrFvwKTL78LkTjJ2ylDsWZN6TlxPFya8nzmKkZtmOr65q0ILVrEKX4kKFifXWmzPxDyO4zhLfKVlrQhv3Hq-8Mnfq3tB5Y-m82wNWq9ZoXogFiPm09-DcSePkE9SYupoiPVKcl6TPj0CARiCiiM3qMFeiziDKefp5F4_xjTem_GpS9X1h_3z21yFFeJepdfIxfoc9uE5tHzyv3K-PTkZahk9GrpTIHYn2ejxjO_9lomd5Dg7t9wo_EUeEYvrjrqCoULbtRk3iPRA-RY6j6KJCHdxo4CBfclgPaCTC0EqINpE8zHEsx05kr2NG23NdDuaP44" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیام اکبر عبدی به مردم از بیمارستان و قول ‌گرفتن از ده‌نمکی برای اخراجی‌های آخر
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/655559" target="_blank">📅 21:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655549">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d132rJyko-vtdz5txwOjqjdZJeh9t_51rd9BWRXzneTYgeXjwwlkrj3uBVEKqRY3l9oP_Ho27Yi9DQ1yI4M3XI-Mdsj3nYGFfxtiEkKU59WmyweiI2-F3yE4olMGRsk2FxE8nTXk4VnvMHGpTQpofFu3X4K8Gv0YT6x-DL0Tcd2PiIA5EBOH6INl5Ae9uLNFIP62DYtdZIOEcaKs4bUHtLG0u5C-6MJIp5x1gzWKipMUN6Qhxj7_l92sy8GNmSyvgn14LApycWBZ8Z-tMbwwW4VRZd0JbyknHcHLUEYAkyrVJXRcwMAB1CF1etMgmOH7JOuTjnAxR0qOTbHiGXJthQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g633mIe4-BN5iA_w49KcGoh2HEZ4IxzOsS1zzpt3DnArEzGx_7q2Jszv2N-u4MKfDrMOVKntjUXifdw48BjQd_eroDMsM85bPqioGvP6UfYP7hJjHfXAYsLnw7v8ugoYl7_PNCjwhcwJNXgDReF2E9bCmyCKWLo4GVBmZRi-2bgrJLidXvXHBt1cyvNy2vrxrxntyDC2bbB20y4VaFT_lXsTs8y8YHggG7ve-GvHfm73EkJWUw2tBPB8XQv4h7zVxSN03JBz5SsvNWBX0k2hbwPVIoXCYi5GpvGHIRcTflrm6TTNFNv-3xu6n-G69uB8uK-d6L44cm6TjSa7G-zjDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PI_UnzbFLBlPuCYXXwdv0vTUWJ7Mifpg0TnpPivXJG78lty_ta8tkourAUSYrDvFYfAlO40c_LX8-RKOw6LmUm4Upjhvcg4TVCymO_M2crpg-1QQ9QF4ebGeqeSyRn8cu3DHrURL_ivzJoalqhK5K89km6ETvpQNHIvb1ac5BVCXB0mL8_KXRLBW_Qu-7htFUVm9QIWbTLHLWw2s1Uj6zE-ZrR8Xm7_lfZtTb9Zw7b7p5P_MCOqOoy2WnOkUnaJ6ZOq7vStQAYGBPVC3XDyyY6V6OpuLH22PlNnFUvceoFTFgcwESy9JMhySdBeaWBbrhjieOuMEeuLjKIgjDzpZbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qaULlvEabwZabA-thf1DXvAzbjUqEsUrTt7izNzQtnU1bTqLU9PtU3vaeEy-4O6_FnRoRNKHDH4fu_IAggHPm2MsjDdxH6182nhqnBDEnbAaechigVoQKQxCvQPDUP3R0C12ql2ZLhpTlVxFMN8NR2pwHpIvclNIhPZXUXQUPjAAI00WlRPMaXF75yhAEmqEcBCpw2X2Rs83AweFLInkKFY2lGEWDovctl3r2rpNsD9ZR_83AXlpIPKAAHkFGFkRUQbIwOhOsAyq6dMTGggQco1qBLkoP-7PrNb_TRQ6J1QgFXf-gRgUV925jaB826fSIpb0SyCjeAEMAfpj5ANl0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F2NSpkovKP11OpL04W52Q-0UpYy8uityTTDBX3sptSGd_WEPEtARApKnJUwK8bT3ltQlCJTA8thO1oqBehjVLc0I2pfdcUIBahf65AVft4eTBzHehpleM2Pb_1Wkei4R7JoQyg3AW-3ujRLU9VexGgrLhsgY9pYBfj9-2xXb2tzvid6L99n4g-mjqvaA1i_Wyyqqmn5EgpLl2rrBzuoAuiZwWtZ8yBVhRSncRvhvCOiMBJg-c5EegNTOYR5HLgbvr3llRvgacF7HzdJSgogstMRz4zb8KXnqYb6tuePvpXhc930_1REYDxuqzhg-cHWOoOGV46gBymWWdlUE3W1pDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QRQrXKFPVc5eKvL-Hc5HuOUoyefvLcKneWHzfEWQqaigTtPrc7hp49E5F0hIktSzAWgb2jROUOnqX-gHEdjGiRR0D1A4vRxp49aLyHGKZvfFQ3Yb6RBL9QwVL3FFJGrL_zPGq_jGIlqFwXQcFTKjN9WWsOXgv8JWIPxnxUD6jeoCBwK-Ey5DMomXz4pTEG_gk72sxhglh1Svj2iOeHIfIN2XGKE3IFYZabxzExPcV1Lw9IprkmX_ziys0rzROrPeLOMKK4sA640VKuwJJM3uNRE_g2FBC0YUiuaV1o3_kDYDpgh0zItEuE3u92-SYQEQFvEfOCXEg9UuerHQDYwCtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F7e0G_RtEe8KnzEkCeAgE9fLLUH6JoDLGdMKLf7NuhyKm_Tj3cgq6hud_V34O2NwFDWdRBHsmwMGyMpfltdr1bLzDrR27yWPJz2H9U-KPH2tXAKME50wk2DT9-wGqqlT2DNeHZCcxfpGAzespqgWvrLeDAZd5fc7kdbGRLupbl_Ypug8o0_IHvTPgeGy21f8Ly7zUUQMaxfK89_4TOpcgj3Vl6RR0IE5FHjI9OZH4IbJyrbg4tAav-7YAsXM5VPA5LeUUDEc7JLlr0BONU5zkG07DWw3ElGiMmMPiVbhh6OKl96JN8MZDAJLIoTSyonfx5yXJM-BEi5DU2RGZjgxqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O7T_oC-dmX1678QRs9SOfTPLU9U8ptQvXykpQ-c6wKcGx8H0cxJGRfsdbcZxdNKOC6wcNQTbwl0X4hjetSzdgJKkpvTB1YXzuTmx9yUadjpED8b3yEpz6oPra9eegV27pn_gboCuIrLEX9pLWhDqE2IJMxB2CAyPIpXkTJmlPwpXeMWzxVYUEfUJ9kNRjZztT_4zLRzOr9oGev4q9refVMbNiUby-zDRcx3kFMYBpe6E1PoP7E-SRM40ycHaWHrLkalNfCwykIV-349ZUrksIyXyxyq--1eQIoVWZvqtWgPlIm12dqbxFYZrZt1vy3GMIGmNUUXdARHe3WMkKibkzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g8MafbqZXVt9ws9NCqL5ytDkz5xJXCpk_m6X2Rm0B7S4p0BXLmxk9pY3T0LjqvgsphmGQqHNb211LPMIHTqzCIP6P8pnF3y0lEBWo12ClO8J6hGtrg5Z6CE0mgKUkcf_3c-9JlhrPbuBIw5L7Ys_kfNryYAI2w8qYYzwhOl1OnSBLWTYY0s941tIi-yPo4qIRkkGqfBub0iU9eLsMG4fMAAZ4s0l63Dx_79eAPnZcrKroTH3YiyXHUOMZgh0W6hEyBTyh7NzhO7ltdJE0nyUN3eTAuU-ZGJZKe_8mzpzlLjHDS7Zs1nCi3D0VvZalCDpWst5f5dMt41SiuoiAmZ_oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oZ_S7ozEpUCISeSFV7antMAyFk7d4UidXDQSXxpCTWi51Tc4_Q15uLv1VrotRfYGHu3m1vMTpnmmbxXR_5q1C46n4EHw8t4KLLoVS0ScX1zEcc2u_XBZdZm2GlL6BVuqFXiYd5-E3EQ9f4dui4dot20DEGmZrXWifkbGz6DI5N6XOp_7mRAKuM9D22oxE1pIgwr3hvqTrZh3Zn9hlzCj6BHYEgdLMngIKQk9yZIss598SkYULh3rCzpw2Osmnoi5i7JxhqmGlNLlyhVGveJD5yIOHg8NGrn9X1dWhlQg27xZjPVPZZ0wSAkzAlj-b_j6xiHz4HNW4n5LTEsEQJno3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
قدمی کوچک برای مردم زابل | بخش سوم
💫
🔸
#گزارش‌تصویری
از توزیع ۱۲۰ کیسه آرد در روستاهای کم‌برخوردار و مرزی شهرستان زابل، به همت
#هیأت_قرار
و دستان مهربان خیرین عزیز
💳
گزارش اقدامات هیئت قرار را در کانال
زیر ببینید
👇
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/655549" target="_blank">📅 21:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655548">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ms393MMm1leuoRc0u-XtOYuBSb9poVnh5HResgSJXx6KiC-xjRjjkZ17Cbwfo3Ip8OZi7OtPZrRpvIQ2oMARffkZcQL3Gh33CoFrBVJFPNSg71SBDu1LULTH5n3oGYN0tFbmuUjskuy6nVcd5nGDoAuxyR-2HgaWNNoigMSAS7Mm03Lxu5aD0PBjLV8XQG6S2f6-QtgTg1Q7R04s144J_HnN40ETLGntzscM6Q2OtbChJjRsbgo2cjmbWOYh93iZrW5XSRNWkIJN19FV1_AnAfSxqykqpiUFLlHWirxYjBTC-wlSdTPRyBYUkm8A9qB5Q-rWVREF9xrM149PJXxIVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۳ روایت از مکالمه تلفنی بر سر حمله اسرائیل به لبنان؛ ترامپ به نتانیاهو چه گفت؟
🔹
مکالمه تلفنی دونالد ترامپ و بنیامین نتانیاهو که به گفته رئیس‌جمهور آمریکا مانع حمله برنامه‌ریزی‌شده اسرائیل به ضاحیه بیروت شد، بازتاب گسترده‌ای در رسانه‌ها داشته است؛ هرچند روایت‌های رسمی و غیر‌رسمی از محتوا و لحن این گفت‌و‌گوی تلفنی متفاوت است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3219934</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/655548" target="_blank">📅 21:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655547">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سخنگوی دولت: امتحانات نهایی دانش آموزان و داوطلبان آزاد ۱۳ تا ۲۳ تیرماه آغاز می‌شود.
🔹
وزیر خارجهٔ ترکیه: اسرائیل نمی‌خواهد منطقه ثبات داشته باشد.
🔹
زلنسکی: ما از طریق اطلاعات می‌دانیم که ممکن است حمله عظیم روسیه همین امشب رخ دهد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/655547" target="_blank">📅 21:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655546">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYN7PjfmFlwiO2EeY9cLOrXCF01oCkzes1qUAzvU6Q3P3RmJzi-czWmE0TI_TodbzuafQJQvFyEy2P7Vt7E9g0Zz35VHt3hK8J6YGTR3Oa3lxFUmmcOc60V71UebjMdpItsJ6YVk7ls7PMwRn_YuJ7iQNsSg-3QHvM6K0gSpVrI8GcxoTxUO1agwfT0HwtLx4te5NdDV6B9pO9AFsgEpweZx0iPBZ-PxoGksaUV5opxYOXzOpBzuTkJnnsxe8d6PweDQ_FzMNNEEr5o90bqlVyIZcWc26zysvERNW7jX58W-C5OT6xooJFufvD52bVu4zN5ChCnmsmoTgPRW09aOWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
باشگاه‌های ایرانی با بیشترین نماینده در جام‌جهانی
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/655546" target="_blank">📅 21:35 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655545">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار کودک</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIc6Cl1nMRtwALaHEZJxhjOT8DXRnbZdvRzMevjVP2saoqxD8j-ny6Jq4up4ZgTT3AhyMDwfArjuSkyMrtDUMnivpRejHEQLCDZ0qEdka4qQi6sJ1O5t7L73_p5xLLSUSiAp_5JpzmhQpIHShOOldXxOY-HBbmGzH1owmSj0HuyTUHvJfeg0ffronfXdMZflRLsbpl9d95tHzB4GsjyCDctCzicaTkwlh8mW-R9YJwY_R1IKMEpJnSxbgaCB72QT0IeIkiss546q_9ANOM6z3C7ldfmpn4a_h6SJ1Sv9O8ww61zZCE_sw2h3euqwMUXK1Fiy2mvuhQll4-z4aW8alA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌼
✨
پویش قرا‌رِ غدیری
✨
🌼
بچه‌های عزیزمون قراره با دل‌های قشنگشون، خونه‌ها رو برای عید بزرگ غدیر حسابی رنگی کنن
💚
با نقاشی
🎨
، پرچم، ریسه و کلی خلاقیت خونه
🏡
یا اتاق‌تون رو غدیری کنین از تزیینات قشنگتون عکس بگیرین
و برای ما بفرستین تا همه با هم شادی‌هامون رو شریک بشیم
✨
📸
منتظر دیدن هنرهای قشنگتون هستیم
👇🏻
👇🏻
:
@ertebat_gharar
🌟
بیاین با هم یه دنیا شادی غدیری بسازیم
🌟</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/655545" target="_blank">📅 21:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655544">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
اقتصاددان مشهور: ترامپ یک هفته فرصت دارد تا با ایران توافق کند، در غیر این صورت آمریکا با «مشکل واقعی» مواجه می‌شود
مارک زندی، اقتصاددان ارشد مودیز:
🔹
مذاکرات صلح متوقف‌ شده بین آمریکا و ایران باید هرچه سریعتر به نتیجه برسد تا آمریکا از درد عمیق‌تر اقتصادی جلوگیری کند.
🔹
دونالد ترامپ حدود یک هفته فرصت دارد تا توافق صلح را نهایی کند؛ پیش از آنکه اثرات جنگ، احتمال سقوط اقتصاد به رکود را افزایش دهد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/655544" target="_blank">📅 21:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655543">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZXDIgzLvIAJogxwtc7jReW_lFEpwNQVMBNZP0PFccnBEm3IkTANxp8XrLeop5UaixvnhpZqa2VLt_tyB0cBnYU_tZ3PtOQJg2S80yPkCHt1_UKmJCBF0cfoNPqco6MmGgI9TDJ1JaYDjy9k13BUKCMZRm-xLYJQ7MgTObD7Nsj5BUrq-WF_xQy-3ILmH-rE-zOokJDgMdzrNjqcED-e2U370-I5zBzWOyA_s_-OKZTkEs57nUk93S0hFt_4WHuSiiz0n9n3TK93P-B_s649RhB2W5JL4GmilMIcsNHjJ_DOR3ACfjxbaSd2tn9hw29Uj3XKAqXSeWHqBFG2rKfAMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهمونی کیلومتری غدیر امسال به یاد رهبر شهید انقلاب در تهران
پنجشنبه ۱۴ خرداد همزمان با سالروز ارتحال امام راحل (ره) از ساعت ۱۵ تا ۲۰ (شروع تجمعات شبانه میادین)
از میدان امام حسین علیه السلام تا میدان آزادی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/655543" target="_blank">📅 21:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655542">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/905db85c9e.mp4?token=eQ1amCW2HQeKh1f0qmPrFS3_3uptpRtQ3bAvZCiQN5-qtT_y2sx6NkzJhMI51QEnGuJTAy7LndPXspBFd_n4B5dmgPgv3MGS8LLdT-0_QzgQeelmf57Us4mknCjHEgbchsMVrnoawCoCTAwO0KFevsZemih2Ur9rPg-SbYAe9heXyhyjtA8xuyylM6kFetTe6Y_Tn3QrLoJ5_IXnVv4MrTNRqSs_YU8KLsZfvsWMrnh1iXwKcxMvhw6s-vTHILCzYj9_x5FlNCcgsUT4NRsCr4HxGtpmA7-d8aAZHqhwTcPLPRZjgAATRRqik9ieE3SVtCG4Pf0ohzPbZL4jW5I1mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/905db85c9e.mp4?token=eQ1amCW2HQeKh1f0qmPrFS3_3uptpRtQ3bAvZCiQN5-qtT_y2sx6NkzJhMI51QEnGuJTAy7LndPXspBFd_n4B5dmgPgv3MGS8LLdT-0_QzgQeelmf57Us4mknCjHEgbchsMVrnoawCoCTAwO0KFevsZemih2Ur9rPg-SbYAe9heXyhyjtA8xuyylM6kFetTe6Y_Tn3QrLoJ5_IXnVv4MrTNRqSs_YU8KLsZfvsWMrnh1iXwKcxMvhw6s-vTHILCzYj9_x5FlNCcgsUT4NRsCr4HxGtpmA7-d8aAZHqhwTcPLPRZjgAATRRqik9ieE3SVtCG4Pf0ohzPbZL4jW5I1mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قاتل بی‌رحمی که سالی ۶۰ هزار ایرانی را می‌کشد!
@Tv_Fori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/655542" target="_blank">📅 21:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655541">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d68585caf7.mp4?token=khNC3lqvinbBRAi5ILIe2XKNiCoojFHDkEpSQRHGBB-PIcRvU4t3jNmKUCQ3sYio5NeE741G_dh9t5GACXVopsQK4oBMAD5JTPuh6mQwtqftJibSPPmUEfVYw-N0gkQbIN8hxI11Gept0Ut7pvnfQKGuatEYrFHjalD9fbmRZ7RrlmovdirznPohvZxP4KMLGfbP8pRfDjsWM9WhySGqcIsJBjozYBVcmBM8Wp3ygOoK1Q7wvD3jtY4Z2P2zP1DcG98yhb_XbY78aClCXWvZL4zHq6GVT6XxJPcPyPrpk5ttCSHBXoMWY6n-cWUdvRagtWNtQqoj8TD0d9cBUqXzEQ7qpDHhs23nc-agx9Zq-aZjmW8Oy6xiuSQdQv67-Xo9AbZe9q4UwiAkwY4alOnPA_n1NS6VURQlxh7Nvrin5JOcixH1UT4Y2rmIvF6bN6kLEBnEcQArWhk5OOboWybzft4xx8ZD_G9S8FAQ1KY5sJeYBYKj9SeZRk07qU7rBwwkNTkKNIulv5JGPaOwnOVyLP358SoItYBou8qRj26y0JYReUgoNQQS635tC2BAvUkzBqIYCcKg1QJ_E3vvq1U-GmBoEw86s8IM1Qrb86e5gpkiFuwjbaJH7cLkcQ71l5DYxs-OmaHx3SDKPuPi-N4v8zxYmkvpEcx5gomEeqYhkGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d68585caf7.mp4?token=khNC3lqvinbBRAi5ILIe2XKNiCoojFHDkEpSQRHGBB-PIcRvU4t3jNmKUCQ3sYio5NeE741G_dh9t5GACXVopsQK4oBMAD5JTPuh6mQwtqftJibSPPmUEfVYw-N0gkQbIN8hxI11Gept0Ut7pvnfQKGuatEYrFHjalD9fbmRZ7RrlmovdirznPohvZxP4KMLGfbP8pRfDjsWM9WhySGqcIsJBjozYBVcmBM8Wp3ygOoK1Q7wvD3jtY4Z2P2zP1DcG98yhb_XbY78aClCXWvZL4zHq6GVT6XxJPcPyPrpk5ttCSHBXoMWY6n-cWUdvRagtWNtQqoj8TD0d9cBUqXzEQ7qpDHhs23nc-agx9Zq-aZjmW8Oy6xiuSQdQv67-Xo9AbZe9q4UwiAkwY4alOnPA_n1NS6VURQlxh7Nvrin5JOcixH1UT4Y2rmIvF6bN6kLEBnEcQArWhk5OOboWybzft4xx8ZD_G9S8FAQ1KY5sJeYBYKj9SeZRk07qU7rBwwkNTkKNIulv5JGPaOwnOVyLP358SoItYBou8qRj26y0JYReUgoNQQS635tC2BAvUkzBqIYCcKg1QJ_E3vvq1U-GmBoEw86s8IM1Qrb86e5gpkiFuwjbaJH7cLkcQ71l5DYxs-OmaHx3SDKPuPi-N4v8zxYmkvpEcx5gomEeqYhkGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازسازی نبردهای جنگ داخلی در چین
🔹
چین بازسازی‌های واقعی از نبردهای دوران جنگ داخلی خود برگزار می‌کند. در یکی از این برنامه‌ها، یک بلاگر در شبیه‌ساز نبرد گذرگاه لوشان با حضور مردم محلی، یونیفرم‌ها، پرچم‌ها و آتش‌بازی شرکت کرد.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/655541" target="_blank">📅 21:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655540">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00f37e27a0.mp4?token=PRaPY4DTmXR7FLXZCWfae-YDJZ8WLkG4EHPnNq1joWLmVd-WtH-dXY4VXGJDmyioB1F6zbYLsknd7MO-NlBlMeVlkGdh_IvJ4mv8lxIh4rXU84vJU6bEkCtDMu82YqnFldwdM5mp9HZ0xTlnbntpovNR0ytPKQftxsZ-P7JXx-22dqmVuS9KE1apjlkqF70tew0I9zobyi8_kVy2m8XC0f167EyFS7lKKZPEgYXr_9OZyCJgAFvokWK5xEu4072mewc0ocOASd-F-ag798AgQuWyYVtTP3WUFqMewUrNVYWkVWegJU_5rjJWODUY5b2_eX7dyCp6SJI29xNjUWAKWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00f37e27a0.mp4?token=PRaPY4DTmXR7FLXZCWfae-YDJZ8WLkG4EHPnNq1joWLmVd-WtH-dXY4VXGJDmyioB1F6zbYLsknd7MO-NlBlMeVlkGdh_IvJ4mv8lxIh4rXU84vJU6bEkCtDMu82YqnFldwdM5mp9HZ0xTlnbntpovNR0ytPKQftxsZ-P7JXx-22dqmVuS9KE1apjlkqF70tew0I9zobyi8_kVy2m8XC0f167EyFS7lKKZPEgYXr_9OZyCJgAFvokWK5xEu4072mewc0ocOASd-F-ag798AgQuWyYVtTP3WUFqMewUrNVYWkVWegJU_5rjJWODUY5b2_eX7dyCp6SJI29xNjUWAKWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لیبرمن: ترامپ ثابت کرد نتانیاهو اسرائیل را به جمهوری موز تبدیل کرده است
وزیر جنگ پیشین و رئیس حزب «اسرائیل خانه ما»:
🔹
ترامپ ثابت کرده که نتانیاهو، اسرائیل را به یک «جمهوری موز» تبدیل کرده است.
🔹
نتانیاهو «فردی کاملاً بی‌اراده» است که توانایی گرفتن هیچ تصمیمی را ندارد.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/655540" target="_blank">📅 20:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655539">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HoeGZXANnPYpZ1g9lSOYw13MZqFycVXNT5BSupxfY6fs125lrTi6sQGLMFHSSrpDJfI2BFMGdbZ1aWEEz-irOiNd1oyO-XL927P68nYoOfwszN7F8MP9NdLDOQAR_k-vTdAg5prmB7Dl6ahOL9Cw8_EDMDyESiAoMQppJ6lehHf43V2zC9pZPFM4Vcwb59TMjuJkab_AW-s2XBBiYoOkQjt5AYOVG5tYSL50ZwA9avPvO4_4QrxtnP4Je2DZRNlEUwGfJTFY_S8VnbmPQbU0hKeiMioCLJKDFU0i32tM5ZfiRs3K7DKUEOe0izi58qu4BgZlqcA7OHMCfAdrP2EvoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراخوان خبرفوری برای روز عید غدیر خم؛ «به عشق علی»
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی‌ست امسال در روز عید غدیر، به عشق حضرت علی(ع)، یک کار خوب انجام دهید؛ حتی اگر به اندازه یک هدیه کوچک، یک اطعام ساده یا یک مهربانی کوتاه باشد.
عکس، فیلم یا روایت کوتاهی از اقدام خود را برای خبرفوری ارسال کنید تا با انتشار آن، دیگران را نیز به انجام کارهای خیر و ترویج فرهنگ نیکی و بخشش دعوت کنیم.
مهربانی خود را برای ما بفرستید
👇
#به_عشق_علی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/655539" target="_blank">📅 20:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655538">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d20a2ef19.mp4?token=BQVL7kp8MAJ30kxHkpCky5ow9Guvwl2R1VcOJO0drTB0O8J9-ypbj8bPTIDepKSu-3BUzlZ4eT0ezrJ1Y3dUONOJdoTNnqNjDOaT5hNjGQAmemO17WfOlII5uz7XGpZYYFa0QZ5KWWiOGjAqB4uZOG6yMlFDPPGu05C1kky6nJ412jiac-tUtPhiq6H_V9s-Wt6d3qMP5HCkYul7fAz_ISSpl0b1zU3MtGXbHlPzO9qqjEoRV72i1HZ281I6i-rjq1zxjRQAmX-jTn3-m4rZsYlhhrxcZn7NkmZ0df2PWEwvB3dUi1hCvVrKwnArtdGg8z17AjWcyfUi8Alr14g9eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d20a2ef19.mp4?token=BQVL7kp8MAJ30kxHkpCky5ow9Guvwl2R1VcOJO0drTB0O8J9-ypbj8bPTIDepKSu-3BUzlZ4eT0ezrJ1Y3dUONOJdoTNnqNjDOaT5hNjGQAmemO17WfOlII5uz7XGpZYYFa0QZ5KWWiOGjAqB4uZOG6yMlFDPPGu05C1kky6nJ412jiac-tUtPhiq6H_V9s-Wt6d3qMP5HCkYul7fAz_ISSpl0b1zU3MtGXbHlPzO9qqjEoRV72i1HZ281I6i-rjq1zxjRQAmX-jTn3-m4rZsYlhhrxcZn7NkmZ0df2PWEwvB3dUi1hCvVrKwnArtdGg8z17AjWcyfUi8Alr14g9eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل‌آرایی حرم امیرالمؤمنین(ع) در آستانهٔ عید غدیر
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/655538" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655537">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_6Vr03syTwKNgiTZSjDfJJrvC5BAf5I2KhicsoZmlA1y-MiBYu4mD_A15rGXFMuM7OKB3r2rIODm4GmoWZGxbGAhY-g5BlbtVMsbxvFM3abDD-e6-sFH8Yw9-mH10oZzigt7teAnVZ4BmTKX3WQLHHm04clNXfgjFXZKlKAJzW-j3E1lVHt9WRBmTFWCNzZ3713qDJ6dJNB9VbHpycCknnTqnXJ5aCiF_or1_RplQMUELSu87jsiwxjXr0K3pvgC2KjPJvi5gs_Gqp0ScRUvl0dKx0KB_xv-fdeCWRTddMwxnMoNf8mPFEkpoTnGtuNgiO3EQYWudbMuRGe0AQbLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌱
مهمونی بزرگ در پناه ِ غدیر،
🔹
با حضور ۱۱۰ موکب پذیرایی، بازی کودکان، غرفه‌های فرهنگی و هنری و ...
🔸
با اجرای: مژده لواسانی و امیر مهدی باقری
🔸
با کلام: حجت الاسلام برمایی
🔸
با حضور: حسین حقیقی
🔸
با نوای: کربلایی علی اکبر حائری
✨
وعده ما: پنجشنبه ۱۴ خردادماه از ساعت ۱۹  الی ۲۳
✨
مکان: مشهد، حدفاصل چهارراه نخریسی تا چهارراه چمن
@Heyate_gharar</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/655537" target="_blank">📅 20:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655536">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ca748c1a8.mp4?token=omjsPBzHUOQZ7KG3RL3jhdPyl-AwMZPOM30ap-0Y4DmO1oNOIdz0jH7XZyM6uVUn6nnfFKXOn0uw40KyLkNkxkRYHNgcDh70O9hJ4gKyBV8OusUEWAXcyG1oZXOhyiJ53ctW1efzuCXt6s7gyZLxMgFjLyQ94J_c41727rEA63tO6rH0iic7CMXvXpxgts_ISdNYn7qPJwVwpYPMaqmvMk-3P8wFJ1sFQumCp_V_x1ysjiyUT0OmeRDPAlSiEB_ouowsdp4XtMeZFtnvWoHyoK3Cgn935ebW97OKg8nTEP_KJe86dDcFoRUcfgE77bh07VNW95vPKqo7g6ecHlEXuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ca748c1a8.mp4?token=omjsPBzHUOQZ7KG3RL3jhdPyl-AwMZPOM30ap-0Y4DmO1oNOIdz0jH7XZyM6uVUn6nnfFKXOn0uw40KyLkNkxkRYHNgcDh70O9hJ4gKyBV8OusUEWAXcyG1oZXOhyiJ53ctW1efzuCXt6s7gyZLxMgFjLyQ94J_c41727rEA63tO6rH0iic7CMXvXpxgts_ISdNYn7qPJwVwpYPMaqmvMk-3P8wFJ1sFQumCp_V_x1ysjiyUT0OmeRDPAlSiEB_ouowsdp4XtMeZFtnvWoHyoK3Cgn935ebW97OKg8nTEP_KJe86dDcFoRUcfgE77bh07VNW95vPKqo7g6ecHlEXuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی جالب از رها کردن جوجه اردک‌ها در رودخانه ایبر اسپانیا
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/655536" target="_blank">📅 20:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655535">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
مردم، آمبولانس آسیب دیده در حملات آمریکا و اسرائیل را گلباران کردند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/655535" target="_blank">📅 20:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655534">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
رفتن به کما؛ پنجره‌ای میان مرگ و زندگی و مواجهه با خطاهای گذشته
🔹
00:07:00 دید وسیع در تاریکی مطلق
🔹
00:10:05 دو نوری که همیشه همراه من بودند
🔹
00:17:00 باز شدن پنجره‌ای رو به زیبایی
🔹
00:27:00 ماجرای نذری دادن خانواده و رخ دادن اتفاقاتی برای من در کما
🔹
00:37:10 درخواست خداوند برای بخشش دوستی که به من تهمت سنگینی زده بود
🔹
00:46:40  مشاهده عمل دزدی که در نوجوانی انجام داده بودم
🔹
قسمت پنجم، (نمی‌بخشم)، فصل چهارم
🔹
#تجربه‌گر
: محمدحسن تاج‌میری
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/655534" target="_blank">📅 20:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655533">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۵ هشدار بزرگ جهان درباره جنگ ایران
🔹
محافل نخبگانی و اتاق‌های فکر غربی، حالا با داده‌های رسمی هشدارهای بزرگی درباره ادامه درگیری با ایران می‌دهند.
🔹
در این ویدئو ناگفته‌هایی را خواهید شنید که رسانه‌ها کمتر به آن می‌پردازند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/655533" target="_blank">📅 20:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655532">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpRSLiKZZ4NL2SeQApSDPU4zF4xGsi4AFZ8jxEH2ZWvHbAGsZUa3XZaaFxzIA7wkGeydebBKZ4cJ1j4RR3324a_Oy2nWGDHsiWAl7ihoEyoTESxB8u6qWxzU6NVrVYWLsn2KNfRyXC7UUmF2BbvfTsfYiM4PYK29ZJOd7UNiQqwIaGTyDX6R9Apc0Ztn2xGercso3guDI7JhwHfd0HhQPuUnzuaR1ZIbJtgv1W_-Grp3oOTMdLktm8G31-O6UvQNjkBVmhh3ZIB8XilfB9agxhs9Z33FKYZ76rXVeYRsRYGN0zdODyOOx5h-G2E0qa78ZyEb4t6LI3IPHv4xWgHgUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تغییر چهره حسین فریدون؛ پس از ۹ سال
🔹
از سال ۱۳۹۶ در هیئت دولت تا ۱۱ خرداد ۱۴۰۵ در مراسم یادبود خواهر سیدمحمد خاتمی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/655532" target="_blank">📅 20:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655531">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ce27379fc.mp4?token=q7arPlWHEuwZKxIB9B4dsngZ8tyrwWm2bERQmGR0hPXDB407oUXMJvBCDovNiO5TiBXJA-b8qjKdoGu2yZQ27FQKUin3JfKDQkCKuVLIUdFJsR-xC5K9oy2eeLB4WL9Lnxtx25p54Sh0Y_rAXQSZoaj1RREU6HjJx_NZWvdZYzXe5DgOFP5yORc0fLWp9TKBBkZuPU8eZwb-4Np-AKvBfL5OzZTuT9QfzfhroW05dy-1ghIopq-Ecew2FSIdfHilJW7wdUpWgK9ngnyV7esqZEaINgypUBxVKkrLMJ3QMj4yF15KblWWftuAZtZ1n14CZxR_zcepiq_wElF4Piv9Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ce27379fc.mp4?token=q7arPlWHEuwZKxIB9B4dsngZ8tyrwWm2bERQmGR0hPXDB407oUXMJvBCDovNiO5TiBXJA-b8qjKdoGu2yZQ27FQKUin3JfKDQkCKuVLIUdFJsR-xC5K9oy2eeLB4WL9Lnxtx25p54Sh0Y_rAXQSZoaj1RREU6HjJx_NZWvdZYzXe5DgOFP5yORc0fLWp9TKBBkZuPU8eZwb-4Np-AKvBfL5OzZTuT9QfzfhroW05dy-1ghIopq-Ecew2FSIdfHilJW7wdUpWgK9ngnyV7esqZEaINgypUBxVKkrLMJ3QMj4yF15KblWWftuAZtZ1n14CZxR_zcepiq_wElF4Piv9Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور دموکرات در جلسه استیضاح روبیو: تنگهٔ هرمز به‌دلیل حملهٔ ما به ایران بسته شده و این پیامد اقدام نظامی ماست  کریس مورفی خطاب به وزیر خارجۀ ترامپ:
🔹
در حال حاضر تنها سوالی است که برای مردم آمریکا اهمیت دارد این است که آیا تنگه قرار است بازگشایی شود یا…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/655531" target="_blank">📅 20:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655530">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خبرفوری
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/655530" target="_blank">📅 20:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655529">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KexmPPgxqS71aJdmvN6X6gDvOsZE7qsscP4fSMEQ3rNBG7bu_mLWe5l7nchA4_AtsOfbOriuZt_wvWVPIoJ90jhYGcLW3uw7A1czfnSHw5uRnhEr8mYMA97BxxDFMtEKX9w5PNFJ6OzZ7ANieyF_MkNMg6dgW1E-vpgEPPZ4ptDIYLeGKlq0wLJxeYdY8nv4o1WE0P6vLtaYzhbiv57liwREO51kpkziFjmGEQet6Wj6hUdBLJO6AVi5vklADJamvmg151ZPRdYMJ9-dY_3UsMj5tnpfBBgYF4opex_fz-uMGgNDx_CshFlq4SkOTsSzIJ_-smQk7-gukwS3QUHGBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
چرا رقبایتان همیشه جلوترند؟
چون از قدرت خبرفوری استفاده می‌کنند.
✅
تبلیغات در پربازدیدترین کانال‌های خبری
✅
پوشش همزمان سراسر کشور و استان‌ها
جای شما خالی نباشد.
همین حالا پیام دهید
👇
👇
👇
@newsadmin</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/655529" target="_blank">📅 20:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655528">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/547b26b4ef.mp4?token=a5SiBkISXLsUnolxhnmaqiFkE6U1WOcNWC2FD4MPveJ6DYCRCv9KNhX6IMGm6jNoe-sXJYIEgFvEK-XBri1jIdICQn0hJKU1LneSCIXh2tbl0fqaR-LyOBKtjErlXODSqIZf411ToT8Umu6bMEljRcMsGVdo8cA64BqXbT1QzgvcQbfRvlKqbFwFegpbbZ5mhzHOS-31R9pY5tJGGy2rfRvOzBRndhNp-FGYN-dnU6bEOYHfbZIqoOcHIv-Ptzf8-g-nr0uiHtASe0k5uuGcIqs-cjz9y_SOj5uzireGyJu8QdeFJGDnwp3nXoRGHNR4cdvjJiO7c-ciaF1hszd0ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/547b26b4ef.mp4?token=a5SiBkISXLsUnolxhnmaqiFkE6U1WOcNWC2FD4MPveJ6DYCRCv9KNhX6IMGm6jNoe-sXJYIEgFvEK-XBri1jIdICQn0hJKU1LneSCIXh2tbl0fqaR-LyOBKtjErlXODSqIZf411ToT8Umu6bMEljRcMsGVdo8cA64BqXbT1QzgvcQbfRvlKqbFwFegpbbZ5mhzHOS-31R9pY5tJGGy2rfRvOzBRndhNp-FGYN-dnU6bEOYHfbZIqoOcHIv-Ptzf8-g-nr0uiHtASe0k5uuGcIqs-cjz9y_SOj5uzireGyJu8QdeFJGDnwp3nXoRGHNR4cdvjJiO7c-ciaF1hszd0ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور آمریکایی: داریم به ایران برای بازگشت به توافق التماس می‌کنیم
🔹
یک سناتور آمریکایی در جلسه کنگره خطاب به مارکو روبیو گفت که ایالات متحده هم‌اکنون در حال التماس کردن به ایران برای بازگشت به توافقی است که دولت دونالد ترامپ آن را به هم زد.
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/655528" target="_blank">📅 19:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655527">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf407a52ce.mp4?token=ErCSWHd6f2rrkEmKNppDjcHeSYk5od0Ba4F0aGnQIupT2CR_6MTVB39_d5N-shDjFjXBSzemnSY5-DZvoK3fEZyR6oyv4KVi-7qxpiAKCgXBsKTL6m5bUu0o0kvOqmD54HEiTfjGDiKDk1hleUwIBnAwqlQaODs9ZbVFzHZIPpq-3GlkU1HmZ8unz8JPuUqyCOGb7U5qn-mZoTbY1gkpWuRNgwldA4J98s_D2tPCbc9M4qx8cZT8ai-uLAw-2VtnlAYPCURaXjhNbj4FmyDr5WN7MnV9rIezJPfykX056P-1OstDvJsz326v2rl3tWCDeLsLZziCJXikytDdeks5Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf407a52ce.mp4?token=ErCSWHd6f2rrkEmKNppDjcHeSYk5od0Ba4F0aGnQIupT2CR_6MTVB39_d5N-shDjFjXBSzemnSY5-DZvoK3fEZyR6oyv4KVi-7qxpiAKCgXBsKTL6m5bUu0o0kvOqmD54HEiTfjGDiKDk1hleUwIBnAwqlQaODs9ZbVFzHZIPpq-3GlkU1HmZ8unz8JPuUqyCOGb7U5qn-mZoTbY1gkpWuRNgwldA4J98s_D2tPCbc9M4qx8cZT8ai-uLAw-2VtnlAYPCURaXjhNbj4FmyDr5WN7MnV9rIezJPfykX056P-1OstDvJsz326v2rl3tWCDeLsLZziCJXikytDdeks5Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر خارجهٔ آمریکا: ایرانی‌ها می‌خواستند یک سپر متعارف دفاعی برای خودشان بسازد و ما به‌ همین دلیل به آن‌ها حمله کردیم
🔹
آن‌ها قصد داشتند آن‌قدر موشک، پهپاد و تسلیحات متعارف، از جمله یک نیروی دریایی، برای خود بسازند که دیگر نتوان کاری در برابرشان انجام داد.…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/655527" target="_blank">📅 19:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655526">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5998cf8f9c.mp4?token=f7w5voWYfYf_VvLYDbVXD1qLPyOLGzJiNj_B5y-7z9qqfUjIFdMQCf2TCzO056EOr1HB6F1wI-rmfUr12hH0-SoiqL3nrj8UZO82fVWPWgNv4xSQTaPYfGA2HsY9zrSyk_4R5b4BpMqktESVlKEFBEjY4gBBGmXflX7TNfmEmc3Iy82wT2DeYvYZ7EIgy5Tj7K0-YZ-rhpDjTEqcx11S0B4Lm6yj41Nc3OPruS3AHWvciQOS4cXZ9dO-a6Pn9r1MY1mD8MxTPTu78hQCJNXh4GcCzlLxw3fPKGTIFy10kAlBluD6BFjcbJllqd5qzy31SQb4Wa6VBMS4W-OxP2RR2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5998cf8f9c.mp4?token=f7w5voWYfYf_VvLYDbVXD1qLPyOLGzJiNj_B5y-7z9qqfUjIFdMQCf2TCzO056EOr1HB6F1wI-rmfUr12hH0-SoiqL3nrj8UZO82fVWPWgNv4xSQTaPYfGA2HsY9zrSyk_4R5b4BpMqktESVlKEFBEjY4gBBGmXflX7TNfmEmc3Iy82wT2DeYvYZ7EIgy5Tj7K0-YZ-rhpDjTEqcx11S0B4Lm6yj41Nc3OPruS3AHWvciQOS4cXZ9dO-a6Pn9r1MY1mD8MxTPTu78hQCJNXh4GcCzlLxw3fPKGTIFy10kAlBluD6BFjcbJllqd5qzy31SQb4Wa6VBMS4W-OxP2RR2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای روبیو: ممکن است تا ۶ روز طول بکشد تا از ایران پاسخ دریافت کنیم
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/655526" target="_blank">📅 19:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655525">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouFsXD2fSZwUAak9xKSQ5W-omZu6gW3L8bY8-mxCBKRmOh9u7r27QgHmPNfIifz0z1g1uecU1lqGugE64oDs9kUV687UsJcn8OvT5tVDk79fu5Ifpg5iLGUx2WO4MMFuNqjTA5dxeLWfRmG5Vu0jWOE7Q6IZqSZe2eDB9RHNNBMn-S9BORnum62qjkSHI3dmw97g8UZhyaSsfIi8zDkSu5cAt5eA9a5_UBVzi1mSPHUfdHQ03CCrHNvbnqiAqfm3dCVaaRUDrtB6I6Q3E4j2_i2raAqKznYdoXEOBc9wnHoYQ_aOB-MDGO0giYamhZcDxBafAXfXbi25g3_IF_3zRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ناو «یو‌اس‌اس باکسر» (USS Boxer) که مدتها قبل به منظور عملیات آبی-خاکی در ایران اعزام شده بود، علی‌رغم انتظارات به دریای جنوبی چین رفت و از منطقه دورتر شد!
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/655525" target="_blank">📅 19:38 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655524">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74f74207fb.mp4?token=d70rNzGfBD7qO_0-uCgl2U7ftVSy1eFC_sYb_FhQNQYmyuZI1ncVuXzLpKdd_0SzsNS3zNa08kGzDNDlU7b1HYQkHRChQC5TqPnpuZ6_LXPFHqb6ede_OtiuH0pAVlDnSAx6F_XbhKHkqYNcTRBamwPqhQpLfwQkke8k2EwRoAspmaYNqQoZuEwm7PUrp0_SofbKOKDaUsSHjN-N_JmMBSeP5np-U8Myh9UbflbFrYuMbRjbMt5WyoN_85nmO8IV8uGXfwqmCh4ZQH27qmqvP1IhAADQdtmb_Nr7ehn9KUb3Tgve_ONSu_7k_zhHmk272NZHHqThVUhhiai_J_z19w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74f74207fb.mp4?token=d70rNzGfBD7qO_0-uCgl2U7ftVSy1eFC_sYb_FhQNQYmyuZI1ncVuXzLpKdd_0SzsNS3zNa08kGzDNDlU7b1HYQkHRChQC5TqPnpuZ6_LXPFHqb6ede_OtiuH0pAVlDnSAx6F_XbhKHkqYNcTRBamwPqhQpLfwQkke8k2EwRoAspmaYNqQoZuEwm7PUrp0_SofbKOKDaUsSHjN-N_JmMBSeP5np-U8Myh9UbflbFrYuMbRjbMt5WyoN_85nmO8IV8uGXfwqmCh4ZQH27qmqvP1IhAADQdtmb_Nr7ehn9KUb3Tgve_ONSu_7k_zhHmk272NZHHqThVUhhiai_J_z19w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاردستی جالب دانش‌آموز سیستان و بلوچستانی؛ پدافند!
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/655524" target="_blank">📅 19:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655523">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
اظهار بی‌اطلاعی وزارت بهداشت از وضعیت محمود احمدی‌نژاد
حسین کرمانپور، مدیر مرکز روابط عمومی و اطلاع‌رسانی وزارت بهداشت در
#گفتگو
با خبرفوری:
🔹
از محمود احمدی‌نژاد خبر ندارم و از یک تا دو منبع دیگر پرسیدم، منابع من نیز خبری از اینکه چه اتفاقی برایشان افتاده است، ندارند. در واقع اینکه آیا آقای احمدی‌نژاد زخمی شده اند یا خیر، اطلاعی ندارم.
🔹
سایر مسئولان همان‌هایی بودند که تقریبا اسامی آنها منتشر شده است؛ چه کسانی که به درجه رفیع شهادت نایل شدند و چه کسانی که دچار حادثه شدند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/655523" target="_blank">📅 19:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655521">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYraxnepUj0YTq18UT_8kgf2w9E_J7d7V2Q_DXLc8OqggLhu-5OTc4LLkxpSrpY6_hqa6Lf620smfo0QkoRGaTYdD5NtW9lPeenMoVI0SWjN7RTKNocz3edRaOiUYaMYEVCYO5tEu82_frNfj3UTlWZGSt-54i53MPleiSOAypAKDu4CGiOZGXsOXc-sdCjtpkC46wL1bdatSO0j_tq3-agVBQgi5Et-mCgu3O76t4q3Cm1NgLgnFsCdTc3ZN3qhSsVZosf4tBBm5BRgvofRE2qVnO9bnV4q_dOqQLIXDh5MYDHsirpbHsndQdgegkFfCDqFxNKyxLMFRcnDds2pgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط بیت کوین به زیر ۶۷۰۰۰ دلار
🔹
۷۰۰ میلیون دلار از بازار ارزهای دیجیتال در ۲ ساعت گذشته نقد شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/655521" target="_blank">📅 19:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655515">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bgMZ9tvjff494-TfjrBrJ5-9m9y6Z9edj047_YQwFzobgWnncLvSLoCKGsgrheVCj2voWdFA4XhyB1cIJQwK5qzVIcchAQqZ-MAYpxlzY2qhZU1ePsjnbdfg8KIDFrxcc0WfZ_dM27pruJVZSztYsTjf2TGQfgOA_8XgJOMXHt6z2nSwCXokOvJX6PfBsjw5R4BjZNhwAvAjeyIOAnESxwSVHAqxJ9K1Tz2AlvfM7i0ofaOd0T5Ai4D02wLfhF8E1pGvM5V-6slZeupETtAE1xcoz00H1NxrFz7r-9CLulo6pcNhKyaNoMaCd6uvE78jUA9zWNjk8tg2RnNDXfH7jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u7efw9zGPMshYzqCN7l7y1uVrWVHowg-_XPJjwQA_sIeMnmLM4jmz5myeinSrtPS3p7HQ5ps1x7qsrk7RsXzmjy6jSmaeSrCoVUcUbERi6Pj4ZVw_Mx6AEHk6H2heSV0d9AhkbRGIStoBbqizWnYI6z7UpOhwZln_54aZsfhMZxv5xHqJazLMb-8cTKrhiH2FjqQqWyzmzkelLEMi22F7wmNKs1qBDdJPTEP2KFwQcxJE6JNHfvTTqUdIqzsKDC4R_d95N1L9RMfTEB2Hls4L0c--8CjmcP6wdRt5whKmKWNKLRZNw3r3gpPNRvKBvpjpBvhvd9KDO_WUxoI014p4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BmhY1xnCvDNcyySE9t94248AtT-1uxyc4kQTIW1NKiRRv5OPCI0wY9b5cj335h_V2yHeA11xTF8KzeqUUjQyS87nOtK7v1pQaFuMeveMB9iW--F9VzFdfxH_qzxU1YKKoqdFVzF2t2eryQFisyOTn6vMQkdm6iLnfeMbipoJ4o6ZuscTJvzuVhQYhVqvmFOCWXHHwWexYxgRA41JF57s78S4xs-Vo8WgVhVhfd4fx3fgy-PADvdcin2yf8TS6wzjPMVeSEC79wLoIKHmKr09qpp3xs5SmpIFpDcGzxfNfJUcealWpuMzylPrdCTT0jAzKeXsTt1mFNTpb912JidMsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FdjFY796Nc9ZihWRfsTCOgPHTlBdMdspzMzerFYys71hlbD5TKtCMEkWrqhNZAqmJCTgawxrbLrnAXhkvuzngE6DeoP3pS0wvSMMUcazFQxrfSNpWhsghiTB6oO1X6wajteNZADyRf3N9W4oMiypKia2TOBeRBkkEcXkztth8j_dM0PNLP19T9w9gAu6Jd8F8mnBGtCptWyXO_wv4pbHw2Gdb51bukOX4b0OEXXWwiL7D6wZRaZyzPDusvltnP5puiVGsiv4CFOB0CakzYVtKWfZT8MeOwmJUPbefTthFZEqXQn6EhEkreRIeuNejyM3FNLtDBONxJEfO0EKNgluww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/npfEtgzAF1fphWYEBFXinEexaJUsizYLFCZ5pZyKj5Z25UVF-WfNPiDsjZhOPZBEVE2on269w0iPp_0JyTIG90sNFGLV_QL5JHb6SC1T4dXzGNyOOlL8qGvPI7Toa-P0tMyVOhyHlpXWjrQe2lfVGBOzEeUp9X5WqiAlfTg4DGwZpkJgGk_t_ue6FgRSDOunZXGTj22snggvrE0NQk3imHqX9gDNQT7B38gNrxZ9qKkCXUtud0-odkXTXRq-IHm_NGWlpu3yGUVhQmKRrOLYX2Y4P7K9VgARnZV9b8gN5yEH_nnmc7xfAmPntpoXSIl0kwKjFztgs0FVLp_o6G0BHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vvEa-LtgB_9hQlw6ogF_TuIs77zlvtzb4v2qBQXFpWMrhdFtbkXvxGFfCyWdmKWdMGSuJVjv7B_Zq022DVt1IaprJ6TqRFjNAaGpvQLUENZhUyFUZMG9M8dKBsrpCdeoIoG5ywphoG4FcBhs_vHXqEUPrXGlS_-Qqqp5f22tWjEap9bU9O4p-WJfHa8hyJo1PXq0BDumzo_1JyQZfQ9T8vuIMTDdWDTW4wz2iW34b-6t24kRiHEXHxI4l1-nwPo-T2JGmU6n2OyqsCvOhmeGVtDGNDuruEaQZ1F67u3I_i2mrTscRtNb1kHeqrFJrjowxeKXG4RFZHu-hqIjEoXEKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
آماده‌سازی حرم امیرالمومنین(ع) برای استقبال از عید ولایت
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/655515" target="_blank">📅 19:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655514">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
ادعای روبیو: فرماندهان ایران با برنامه‌ریزی وارد میدان جنگ شدند   وزیر خارجه دولت تروریستی آمریکا:
🔹
کاملاً واضح است که در آغاز درگیری، آنها تصمیم‌گیری را به فرماندهان میدانی واگذار کرده بودند.
🔹
برخلاف سیستم آمریکا که رئیس‌جمهور، وزیر جنگ یا رئیس ستاد مشترک…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/655514" target="_blank">📅 19:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655513">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCTgSv_0_g02YgvP9IiqjwJhX9lWPlTfiB9R8J009OkaGkYmlnxL9_1ZrSoEEPBWCqVAfbRXK9yvPr-LtFZkr2-AetoxnJzE3G06AX8IHey_DsvGWws033ikKr4sqlkFCh2gwQgYO6LhwcP7rhxXZG9Khhx9Yg6fAaOQ5ugSu3fSbfml_MxZVgjKCvdgXhltdNal0iYaaCfYX30a1vL03L_LzYPGgyNoWtIoVuD1nzcCOq-_PKCrSj-Erd5UjiA4FkPTpislzZWH3Tp6SpfH10UzXG2zJaj5XYybxfKG1kp0hpm7aH4UFf6bFrBOsmUUzyz55NljV4NATBlu4BE52A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/655513" target="_blank">📅 19:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655512">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQeroki6bPa5e5NTo-EsTXU-cevR-oS2U5rnyGkJ2iOa-CWWuhGPdf735Jv2EDGGwuu2lqocXfDVuoyGdgH9kGXt5hiWc6--zxVYDDqD8RqBU5pUnJoVtKpzWmYlWg6h1YiQBm9piChc7Tt60oSiTF6yDoO5qm7r2OaYhZtTx-TDEpEqN0eFVDBl8IGKQLC68Hbk0GMMF_1KOAkzSQhGiXoiGZsaphp1F_1wqknI4bXUwUh3NjtDyoN8eFRZseH2m46D4uYp0Vgwkbl3paX5PVUsfmNVOQiFgjkp5Jl7oXoOEV9rbKWSwzGkYu1FqUZ35ecceQbZt3TSGnZ01VRVvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیات جدید از خلبان اف-۱۵ سرنگون‌شده بر فراز ایران
🔹
خلبان جنگنده اف-۱۵ استرایک ایگل که در ۳ آوریل (۱۴ فروردین) بر فراز ایران سرنگون شد، همان خلبان یکی از سه فروند اف-۱۵ بود که کمتر از پنج هفته پیش در یک حادثه آتش خودی توسط یک اف/ای-۱۸ کویتی سرنگون شده بود.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/655512" target="_blank">📅 19:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655511">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
زیاده گویی وزیر خارجه آمریکا درباره تحویل اورانیوم غنی‌شده    روبیو:
🔹
اگر در مقابل چیزی به دست آوریم، می‌توانیم تحریم‌ها علیه ایران را کاهش دهیم.
🔹
ایران باید اعلام کند که با حذف اورانیوم با غنای بالا موافقت دارد.
🔹
اگر ایران می‌خواهد نفت خود را از طریق…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/655511" target="_blank">📅 18:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655510">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
شاهکار شهرسازی چین
🔹
پل معلق «هواجیانگ گرند کنیون» در استان کوهستانی گویژو چین واقع شده‌است.
🔹
طول کلی پل به ۲هزار و ۸۹۰ متر می‌رسد و بلندترین پل معلق جهان است و سالانه هزاران گردشگر بدلیل مناظر طبیعی زیبایش جذب می‌کند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/655510" target="_blank">📅 18:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655509">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
خبر ناگوار؛ تابستان امسال یک تا دو درجه گرم‌تر از میانگین بلندمدت است
صادق ضیائیان، رئیس مرکز ملی پیش‌بینی و مدیریت بحران مخاطرات وضع هوا در‌
#گفتگو
با خبرفوری:
🔹
روند ملایم برای افزایش دما را طی روزهای آینده در اغلب نقاط کشور داریم. در مجموع انتظار داریم هفته آینده هفته گرمتری نسبت به این هفته باشد.
🔹
انتظار داریم در تابستان امسال بین یک تا دو درجه از میانگین بلندمدت افزایش دما را داشته باشیم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/655509" target="_blank">📅 18:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655508">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
ادعای روبیو: شرط اول در مذاکرات با ایران، باز کردن تنگهٔ هرمز است
🔹
لازم است ایران به وضوح اعلام کند که تنگهٔ هرمز از این پس باز است.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/655508" target="_blank">📅 18:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655507">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
روبیو: هیچ کشوری به جز ایران و شاید عمان، طرفدار اقدامات ایران در تنگه هرمز نیستند   ادعای وزیرخارجه آمریکا:
🔹
اگر ایران با توقف هدف قرار دادن کشتی‌ها موافقت کند، به محاصره پایان خواهیم داد
🔹
هیچ کشوری از ادامهٔ بسته بودن تنگهٔ هرمز حمایت نمی‌کند، از جمله…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/655507" target="_blank">📅 18:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655506">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbde4ebdb7.mp4?token=S2E9Qb4HQDjakJWcek1JB4wXHFhNNo3q-V_asZ1dKWP1e7HrlSxhYyasYy1sF0aatJITXchLdgOtK5TOf_sSQrIBLjCts05tv-VT-8KMvcpTQ9HR_hSef6m6U7fDTtZkF0zOo9wCUQAzar85gOWHec-kBZrLgJBISBXnSfSdO4QwGYRyCfPQBhThwlg-55qXzO1s4qRpSrfc4wORJ9s-SDI3S0z-KRO-bgHIYWMgUFKF11neqrK6If58EJUz7F7Bk5JupoNSNbMHGsmQurZWqRPMFX-cMMpoH0o2LtcFnqcpDEDxBPwbnCPXWV9ByO25Lk-S20fex_ffbhIJGhrn7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbde4ebdb7.mp4?token=S2E9Qb4HQDjakJWcek1JB4wXHFhNNo3q-V_asZ1dKWP1e7HrlSxhYyasYy1sF0aatJITXchLdgOtK5TOf_sSQrIBLjCts05tv-VT-8KMvcpTQ9HR_hSef6m6U7fDTtZkF0zOo9wCUQAzar85gOWHec-kBZrLgJBISBXnSfSdO4QwGYRyCfPQBhThwlg-55qXzO1s4qRpSrfc4wORJ9s-SDI3S0z-KRO-bgHIYWMgUFKF11neqrK6If58EJUz7F7Bk5JupoNSNbMHGsmQurZWqRPMFX-cMMpoH0o2LtcFnqcpDEDxBPwbnCPXWV9ByO25Lk-S20fex_ffbhIJGhrn7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای روبیو: ایالات متحده همچنان در حال مذاکره با ایران است  وزیرخارجه آمریکا:
🔹
توافق با ایران ممکن است امروز، می‌تواند فردا، می‌تواند هفته آینده انجام شود.
🔹
امیدواریم با ایران به توافقی برسیم که منجر به بازگشایی تنگه‌ها شود.
🔹
مذاکره با ایران شبیه مذاکره…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/655506" target="_blank">📅 18:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655505">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k29irR09dlMR_Rdd_OuKkesFH6kblYjG71Dwrltv1QgoIvdYsjemR42KiBJpo2X55tBvJX76-n77Xi0yOtCmZBV2jcLTMfUiGsR_BaSFqEqdKHx0u0AYb2WV0cKetf65PxUNL3cCfAjcikcCNSCIjFXcreZcdheSFpF2cnrSjSvtjmdxzz3nXrPHZ_dYDSkGJE-5qyi21w4wieHidgU8FHbgonpaTNWDFgA3vxl1bhutmRym9J7Qu-7gP0_jzs5fuNXp2GKg7OzJ358mtSJ7qSiu8ipNl5ZDYNni3Fd3joOZYelzVPS8o7vA7cXafZIm1jxXI0aEHZpFVOtKiwJAqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امیرعلی‌شیر نوایی؛ مردی میان سیاست، شعر و هنر
🔹
امیرعلی‌شیر نوایی از آن آدم‌های کم‌نظیر تاریخ بود؛ وزیری بانفوذ در دربار تیموری که فقط اهل سیاست نبود. هم شاعر بود، هم دستی در موسیقی داشت و هم از بزرگ‌ترین حامیان هنر زمان خودش به حساب می‌آمد. از ساخت بخش‌هایی…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/655505" target="_blank">📅 18:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655504">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkDfNNDrrc60dxelOk3kKdTBn-p-eDEaSr0E-WvjY0RsJONQAEBuZX0i8lJd66UOVa46i3ptuKmYgMLG9vG69TfTq99TFnaz1vi4LNrEntcz_aoByA4dRtcX-rvm_j88ftDmpcVfWemIGubg1v36YRXJh5e-WK8t4rkRW6KULQqbqnEGgbN5yDHoWmNWBtKYBfi9vhQSYDzNSy42v4lPwFmw1K5S7nW8yB5NTP3FqWo-Zkfb837GN2hlUe1X8gdWmnjfTQeb_xaIyAnyjPgnyi4Yv6lzCoOIUvpTYG2-cF8zYojMPHauuwBMwDhl_tEtrmqj-QeSDHNPzHGjDxFzeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فاکس‌نیوز: روبیو برای استیضاح آماده می‌شود
فاکس‌نیوز:
🔹
روبیو برای استیضاح کنگره آماده می‌شود، زیرا جمهوری‌خواهان به تلاش برای محدود کردن اختیارات جنگی ترامپ علیه ایران می‌پیوندند.
🔹
هر دو مجلس می‌توانند این هفته قانونی را برای توقف دخالت ایالات متحده در جنگ ایران، بدون مجوز کنگره، تصویب کنند.
🔹
با توجه به وتوی مورد انتظار ریاست جمهوری و عدم وجود اکثریت ضد وتو، یک قطعنامه موفقیت‌آمیز در مورد اختیارات جنگی احتمالاً ضربه‌ای نمادین به دولت خواهد بود./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/655504" target="_blank">📅 18:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655503">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
اعتراف وزیر خارجه آمریکا: ایران همچنان پهپادهای زیادی در اختیار دارد
🔹
مارکو روبیو، وزیر امور خارجه دولت تروریستی آمریکا، در اظهاراتی درباره توانمندی‌های نظامی جمهوری اسلامی ایران، اذعان کرد که ایران همچنان از ذخایر قابل‌توجهی از پهپادهای تهاجمی و شناسایی…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/655503" target="_blank">📅 18:03 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

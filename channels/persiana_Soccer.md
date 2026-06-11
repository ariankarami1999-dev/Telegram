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
<img src="https://cdn4.telesco.pe/file/dPqY9QQV9S6tjg_RMDBo9DPYTJrlqg3NYmoPyCE5hS9oQVslh8vk8g3_5JUa_N9b3D7FtlyQyQfQJQWsx1vpNPXGwRy-9C62-5VQMhplOaH53wgLj238jH7In7t1FjIuc8Sdjj_gMGGt-NNTjfCiLI6p6t9aLyjFjiaWGnv04jTAWUDHrKnyZtJ_qnwihftul86ReJ-xejRCCj_6yH1MaJBN8NIg4DRX4OvDoQHTTKPGdunrIcPHNzpKIqZo9v-B5v0q2oyvxwoNb8SCtOcbHP_u3ViRShh6VNqvq3qm4T-zVe5pgXXXKajEt9rZwiVfu7xLp13gyXfMp9wx18a6Cw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 195K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 22:11:38</div>
<hr>

<div class="tg-post" id="msg-23215">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDFWYSzd8c3LCDiVLc8Gnofil7g8vaMwJEceKguBPlN4sF78WuSVeug8yMFsNFQrTlCOBMubJlFEDwvI58Rzkbu2Sv8_PfaBNk-b_0xK2mP3CTDAm2mJeVHG364RZNhugk0UgHI-pTGkvNoYrB9bJak8SBRW1hsHc9h6NIMWkCoAtMBkOevzez4LbawHv5n_hL96Rutv5nkJDUCIF7V8JWGpvyd8TL6JbVEKGZGeTxG0fLM_rm4EfcW8qMBs7Ra_O34zOjL0REwH3Q-EhrZZlfzrC8XFBajXbFpLxAryWKNkEruO4eV9i7iUBtQdFWLuEahWQRTQSgO-MDHfXW7Uqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇵🇹
#فوری؛‌ خوزه‌فلیکس‌دیاز: برناردو سیلوا ستاره 31 ساله تیم ملی پرتغال برای عقد قراردادی 3 ساله با تیم رئال مادرید با پرز به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/persiana_Soccer/23215" target="_blank">📅 22:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23214">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6a0329db5.mp4?token=Yixy0jLn_FGV7PuvBnlq1TvA5szmcGi4GJgpWZ9P2-vJD-qhWbsCvUdtv6kATMba0zWwyvfAnTCG9NUUFik9Z-wRjdAeXk0iYX51oiKShymwnwt69MZCa9tgeSV4hyIuJ9ZeMSw5jJASQ5gYMSMUIqW04vUCTC5nNcEC49rjrjy40jmWO7DySR7H_XxnHDqKU0No-CgXs9w4l12d3AREmlhTZ3YgPA9dV0G0zlbYH2A1-jCHuVXS0oxcI_VNPq91K9ZtQRt-9tS1Nk8uB9uLNu3oI5XPkKQcK-ish7W5mKKyUGwjL_UyHIZot4JznpOdseiVdno94wxg9lVillIThA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6a0329db5.mp4?token=Yixy0jLn_FGV7PuvBnlq1TvA5szmcGi4GJgpWZ9P2-vJD-qhWbsCvUdtv6kATMba0zWwyvfAnTCG9NUUFik9Z-wRjdAeXk0iYX51oiKShymwnwt69MZCa9tgeSV4hyIuJ9ZeMSw5jJASQ5gYMSMUIqW04vUCTC5nNcEC49rjrjy40jmWO7DySR7H_XxnHDqKU0No-CgXs9w4l12d3AREmlhTZ3YgPA9dV0G0zlbYH2A1-jCHuVXS0oxcI_VNPq91K9ZtQRt-9tS1Nk8uB9uLNu3oI5XPkKQcK-ish7W5mKKyUGwjL_UyHIZot4JznpOdseiVdno94wxg9lVillIThA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جواد نکونام در برنامه زنده خطاب به عادل: پائولو دیبالا لامصب چقدر خوشکلهه این پسر
🗿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/persiana_Soccer/23214" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23213">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⚽️
ویدیوکامل‌اجرای‌امشب شکیرا خواننده کلمبیایی معروف در مراسم افتتاحیه جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/persiana_Soccer/23213" target="_blank">📅 21:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23212">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L42VW5EeJ5_hdZ7Y6KAhT2cJc01aMKwjn2A_5_jRIbcnaNuDSpzoFcUnDprOoNzLDqkDFmxtSm2fJvLn5_llfM2lg5tb2xU6NKhM9hJAaqNZPoDRgCoYlEx_zEqD-cpj_nI_0sN-3oGcxt-n07tiQ915EGIy-68tliTeP2DxAN8znrwVgL-iEfGFZ9eBGfYU33fv-S3Fa6KOuxnAnUlCnPAK0HfbjA8ErGpCft9Ce-axSSSoAhcq94KvOGpbf91eBsp5CPPib_4hve8YOzrTA_R5-TIp8bn0fjZdfJXCfYbtd_UEXTjV3nWXSQ7xhA6fCIEIM3UgGhtjNX0d-GDFVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
🇦🇷
صحبت‌های جالب پائولو دیبالا ستاره تیم ملی آرژانتین در گفتگو با عادل؛ برگای جواد نکونام و کاوه رضایی از این مهمون برنامه عادل ریخت قشنگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/23212" target="_blank">📅 21:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23211">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTusUy8DzuqVvANVkzZ71uEUjBigTeZTiIio1CoNDW8cRt3OqWFM1b7Dj10xSZS94oRXS4t7_6ylDojoX7ce7NhIsz4r3uKVvD0EWKouO_kx_r9RLw-vv18OiPQzKKGd07xTWMeKwZpWWG5Rgcx65lXJ750iju6ptGJPKuDBiXwspypY2HWkW7oQaitdAFVVzoHFfGNCdrwanDk7jbVyj80-fVrHjM5n3a6woLcZ1kU9sd4hmDvMyTRzIsFiVFlMwwMaoKSYRGzqLJj9ZNozNlzjV9rYZ6D0XUxRSXk9TRtYzgtmoFpH3lh9UHyOUAJfiDDBRBZyT451JaL_97eujA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛ باشگاه رئال‌مادرید تا ساعات آینده خبر عقد قرارداد سه ساله با ژوزه مورینیو رو منتشر خواهد کرد و رسما اعلام خواهدکرد که این سرمربی پرتغالی بار دیگر به جمع کهکشانی ها پیوسته است‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/23211" target="_blank">📅 21:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23210">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9Vq_XEWrvs8Piu-YGfeuH5wUXW7qau_aTs4LkIModGPzxw7ECvWuO78STMBjkYLhT3EFD5KQUZxyHPScVTrGhgaxsFsqVhZnqNmHUdBtk_6xqkqDBAIlUkXQDprGShl4bB6ATgWySLv3SOvXTQ64Jfv8ejMggcIbm7gjbnprKF-_LSCxzjB6jux7YOm4RUNcc_aD15psXReC0-jbPDX9OknmHeNqjzYhy8vVhXjcpFef5z8TTDFfKg09c3G-yJ_4E6ER2JJx9gQlzE73--MCOltbCiJAzVkdlkkeLnAztw7tebb_e0I__miWO-f8G-GEb9szHznOy_lCfYZ1J_mtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
حدادی مدیرعامل پرسپولیس امروز به ایجنت علی‌علیپور اعلام‌کرده‌درصورتیکه‌رقم قراردادش رو باتوجه بشرایط باشگاه کاهش دهد و قراردادش رو تمدید کنه فصل‌آینده کاپیتان‌اول‌این‌تیم خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/23210" target="_blank">📅 21:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23209">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0af0ad9722.mp4?token=KHvsjYfxqQiKP34sEUQEezR6ZGyVYKlKFEBhh47Vu7YTS7gR-Cz4fi7zsgA62CP8H8qWNozK88jlEB0kQ-ebttIAEheiTXGpamfUR1nsz55kZ_V2cC2XSpIvAlXtpni3Vs6CUNXowR595ahJAARV87b1cOmwng9hTFRs7j-86Awty1mNB2p6Ow9F3b4ylhYASp_6rjUzxO95r7IXvJEwwJUoE3XicsHwBSMiwk3xpHP_v0JEQwZ0-ZmtpAi29kB8z4K4NALuIakrDCyAAIStiaQJj2ebwTEBwmpJ2ANlNeqtZDaBIO_3l8bwLFPxYjV9AM-JRwc1wC2Qk9X4-nIj4kjS9n_NYigB996mN8t3XBXbxEt9KCoG8hiqwipAisGk47Kj5v-AsqPbUC_VZTZ58XhAn8Qh9jU2rhS3toRFay662w-JEM1ydxpnUa0PP-mQNtNAJfwbnhD4B_4WdoTWMXUrRQoHfPEqQzeaNXrzlcY2t6vLboAVlaxxMOToJ537W_LCw5tpDFogJrO8UYeCO3XXRB6wM6f7QZJIqs9fsq7h2joGldClzO3d5K1NemsxxDzityTNVK7jH65O8ha3BJoH1cGQeZhGrzwWaPeRyfY4eklO6kXpNG4DdkjOLaFhmgnVnfDtRZnkg5rOJTutEI3ECV3YrbHkxlePDM1Jw40" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0af0ad9722.mp4?token=KHvsjYfxqQiKP34sEUQEezR6ZGyVYKlKFEBhh47Vu7YTS7gR-Cz4fi7zsgA62CP8H8qWNozK88jlEB0kQ-ebttIAEheiTXGpamfUR1nsz55kZ_V2cC2XSpIvAlXtpni3Vs6CUNXowR595ahJAARV87b1cOmwng9hTFRs7j-86Awty1mNB2p6Ow9F3b4ylhYASp_6rjUzxO95r7IXvJEwwJUoE3XicsHwBSMiwk3xpHP_v0JEQwZ0-ZmtpAi29kB8z4K4NALuIakrDCyAAIStiaQJj2ebwTEBwmpJ2ANlNeqtZDaBIO_3l8bwLFPxYjV9AM-JRwc1wC2Qk9X4-nIj4kjS9n_NYigB996mN8t3XBXbxEt9KCoG8hiqwipAisGk47Kj5v-AsqPbUC_VZTZ58XhAn8Qh9jU2rhS3toRFay662w-JEM1ydxpnUa0PP-mQNtNAJfwbnhD4B_4WdoTWMXUrRQoHfPEqQzeaNXrzlcY2t6vLboAVlaxxMOToJ537W_LCw5tpDFogJrO8UYeCO3XXRB6wM6f7QZJIqs9fsq7h2joGldClzO3d5K1NemsxxDzityTNVK7jH65O8ha3BJoH1cGQeZhGrzwWaPeRyfY4eklO6kXpNG4DdkjOLaFhmgnVnfDtRZnkg5rOJTutEI3ECV3YrbHkxlePDM1Jw40" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
حالا دوستانیکه‌ماهواره‌ندارند میتونن اپلیکیشن My Satellite Aand Tv رو ازپلی‌استور نصب‌کنن و مراسم افتتاحیه جام جهانی رو بدون‌سانسور و با کیفیت بالا از طریق تلفن همراشون مشاهده کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/23209" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23208">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/709c123d60.mp4?token=i8VuX0GLO3PAlDBkOFfYdKCMWpQoYpeUsCo8u6Tod6xBeR55LJS9hBpjJ6Cbs7uUADkyINxCA_N9rEJobkVilLGBHSKFFfncsJmkx8n3R8hJIBZ2-eltKVrajpOm9PJz3ZmWCwCviK7tFQQUwsJQFJ6rzAJDDb2uNYFIfMhNWQUKCGOVP5c1p5xtiErhu7JvdNSJFIJ5qzPkXg-YAf22kHlAQSuAKZRYqUM7BANdY1L-n3LqGiEfkYnbFKVFeSn1OYTd-Rf9pKhca3CrAwJalNJT0xrb-CR9ZMERWwH4hi7WOGJ2KOH27KMzNz3hV1ZRY_7ML3YuVJtfOqZ96pu-dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/709c123d60.mp4?token=i8VuX0GLO3PAlDBkOFfYdKCMWpQoYpeUsCo8u6Tod6xBeR55LJS9hBpjJ6Cbs7uUADkyINxCA_N9rEJobkVilLGBHSKFFfncsJmkx8n3R8hJIBZ2-eltKVrajpOm9PJz3ZmWCwCviK7tFQQUwsJQFJ6rzAJDDb2uNYFIfMhNWQUKCGOVP5c1p5xtiErhu7JvdNSJFIJ5qzPkXg-YAf22kHlAQSuAKZRYqUM7BANdY1L-n3LqGiEfkYnbFKVFeSn1OYTd-Rf9pKhca3CrAwJalNJT0xrb-CR9ZMERWwH4hi7WOGJ2KOH27KMzNz3hV1ZRY_7ML3YuVJtfOqZ96pu-dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل فردوسی پور تو ویژه برنامه امشب پائولو دیبالا ستاره سابق‌تیم‌ملی آرژانتین و سابق یوونتوس رو بالا اورده و داره باهاش حرف میزنه؛ صداوسیما هم داره با خداداد عزیزی حرفای کارشناسانه میزنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/23208" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23207">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPBHq0HBuJiGLdlBNTXYjfvX9muQuVV9x2jEhsCyZsf4QMv82rhE3TkvAm0G70BDZh_QFuMJT_abAdD0_NZ-i_WvLkopIyyUFvYnAwoAC_miTKpuvMOZpgZWIxpLL6xCMOpAxkUUx88J4NFz7zgLD3Jl0lrifsCsOkX7ipkPfEMhzMY-VgaTSZimdYqWnIsV2wzkFG48QxjdRJSAKvlGv3ISc2Y_645VAh7fWXWIZrX0auPIxwj61HXFLg93azagWmlaS7243y9QCRKuqqCf3Ib7VVaf5UAx1WZDWyp_KnIkJbagP-R7KaFiQ-7eJsOOu0JHc4EQRZcRlcLJUgHqaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
گروه همفکری شرط بندی | Tips Group
⚽️
دنبال پیش‌بینی‌های بهتر و تصمیم‌های منطقی‌تر هستی؟
📊
تو
Tips Group
خبری از سیگنال‌فروشی و وعده‌های غیرواقعی نیست! اینجا اعضا با هم مسابقات رو تحلیل می‌کنن، آمار بررسی می‌کنن و ایده‌هاشون رو به اشتراک می‌ذارن.
✅
همفکری روی بازی‌های روز
✅
بررسی آمار و فرم تیم‌ها
✅
تبادل نظر بین اعضای فعال
✅
پیدا کردن ارزش در ضرایب
✅
محیط دوستانه و حرفه‌ای
🔥
اگر به شرط‌بندی ورزشی علاقه داری و دوست داری قبل از هر انتخاب نظر بقیه رو هم بدونی، به جمع ما ملحق شو.
⏬
@Bet_talking
⏬
Download betting apps</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/23207" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23206">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXQYH367n-FB8ZB-FSOPex96yrjlX__EdwesqOptg1QWNGOwxHT5EHnbPxnBqfh7nULOYri5yr_Ur6qm3nzkMDktDSTA72iTi41opyrMtYJDITTsZosRQ9m7AbNyFjzzq_w4tx5zyZeM6WrEDu3exO7GzRIvANWbyzxTuSVWULTHlovm3YDYudewxSKOPhWpKuIPDCPl4UPoi6737_RV8-hbptNWBKNoNb_5VDTu9T4i_JNNX-9wWpWPzLQG1G79GsxYE2x9KO1ApdCwKzjQ0M4dEy7Rlc4LsJVWvmQyVYUt-PnRPV7Luezi5dtolbQ6fEySKsQrLvm9HSSiZGBgNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینم‌یه‌لیست‌دیگه ازشبکه‌های رایگان ماهواره که قراره جام جهانی رو به بهترین شکل پوشش بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/23206" target="_blank">📅 21:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23205">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dB6jyR4eIuWmpmTVUjytqF5IFeJykCmPo8WHgyERfKGHFETjIsaq4hXr3q-6g-xlH0mSV6XQsJaDX9OroCF0CijvOGljNXQUI6v-dTMYTctvzrxVWtMrpmnL7W2DmKTMm-h3wwF-pa7gjLac6BsrgOXO8xtexHQhSMmBKgGTdkgV2G68zEr4dNSBUY-c5H7c6ZehD8rHHDCDLtn6N0GExcd02_VtZnSEo5SBkpVwpHs709w8ifaoQhSB5Okeg4rZkUUYRVzo2qNd_GCEc22OyW_XmA2hVS_4Y6ol9ol0NWjBwoQWlE8hC5FXL5uHudVLgtvG2FrGSpL_mbEmabcocQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇵🇹
با اعلام رسمی فابریزیو رومانو: باشگاه رئال مادرید مذاکرات‌جدی‌خود رابرای جذب برناردو سیلوا  کاپیتان دوم تیم ملی پرتغال آغاز کرده و به احتمال زیاد این انتقال بزودی رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/persiana_Soccer/23205" target="_blank">📅 21:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23204">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBC9wMqR5ic2Lzvz0mATe1ELFe6XZMhCWYbPJJae-dP3Nyar5vpSgbdVX_j0k61LUN8CuWNSe4JIbyTC7PxuHpSDCatxKdBSH3WvDODC4gcy3FYMvYwswrHHKLHuA6CyAFkCmfpmy62Xs-dksbTtvZskailrcsZPWIMl-GgAme3M79Iw7y7tkE-sUFCJ6fAPg3XedYilZ2m-v8OKwMykCmyd3edwYAWqYzELLU7G3mwwnyPN11NQ9r3eerTrAFcVpPYmiknnve5moNPWZuY99r73KzgBqZLZskqPXfhgWNMFoCsbDBOKYDa32SvYy_Gn8LZD_1Hou_w-7kMXPb3aXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌فعلی‌آبی‌پوشان موافقت خود را با پذیزفتن دستیاری دراگان اسکوچیچ درصورت عقد قرارداد با استقلال به علی تاجرنیا اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/persiana_Soccer/23204" target="_blank">📅 21:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23203">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePQ5kYzkhcAjsb5wo43q0BhglCVQI5rLfkmDOyK5eDUiFWRZzJJqnkCBdVHgeHg-F2im6SbHNG5GaExPxyQth48yua-fxq7Mp_NB_mYNlReB6LM6ZeV9rhlH_Eqd-6HKBUKNGpoMHzkV_rIwk9wi1fP6_mNYZW9uZHBgM2c9trHjBhpjhomL36FaS_lW2gyscJnFfyYn_WYLbkPljB6EJHXWsOmOYPD5W0LIZLmB03vF5hZLu_k09fhtxH5ZGPdB8dgdGFuWXHk8VfJV0OI67sr1ht1n_5kvPtc5UAOEA6DO2TuFNTP_NRY3mbZCQpdMxgYz01x_VCLz3kiJGWomFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
حالا دوستانیکه‌ماهواره‌ندارند میتونن اپلیکیشن My Satellite Aand Tv رو ازپلی‌استور نصب‌کنن و مراسم افتتاحیه جام جهانی رو بدون‌سانسور و با کیفیت بالا از طریق تلفن همراشون مشاهده کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/persiana_Soccer/23203" target="_blank">📅 20:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23202">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWZuN9Ev_SASnpfPkYoJ0N3IkP9mmSUmVqzV_CqbbNqdapgDfxPKHEElPHN3tyH235enG-hLQ6yyQJizNi69sXRpQ6jOUoor1lVw4cvLo2cwn8J1CgmjUTTvneHStf7J8fGP-HhBwmAKvhsbCQ260hwebWcZPYqpN0oWyxIxvfZxJCsvO8t7f0eEkvzVDPCq7HyP4FhVkrlc28o7QxmYrQz1Uc7fR_B7CGZgKOlo527LUg1efvJNlv48uhvJci_ty2yZ0rV9EzpSFXSuBph8sf-rGi2CYZK__sWp07O1psTSc0XWsPLQur3K05TD7DpNrtWIE71Jc_cmKgZOfdAdow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
مدیر برنامه‌های نیکو پاز: ما با باشگاه رئال مادرید بر سر تمام بندها به توافق کامل رسیده‌ایم و نیکو درپایان فصل‌جاری به این تیم بازخواهد گشت. منچسترسیتی، چلسی، اینترمیلان به دنبال جذب او بودند اما نیکو علاقه داشت به رئال مادرید برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/persiana_Soccer/23202" target="_blank">📅 20:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23201">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8BFp6AOtqg05-uYrj_O3FpV2HrlWXPWNsNOHukSelMMDO6MnCMS4q3YpLZDhLfPlY08tNsB2MX6_oraooeGizwhS_UwOSNCpHk7sccNVvBpICckhwUSot3kNeTSetfPRqtPZ5UTRpoQ0JXbN2uv8D2RWDGCOyxgnnVLM3CthaSM3qPxcSLmU69C96_bNUHs7LoypH2bEQZUp73T6BzPaA94tMwSHCliN7C397en0U8NGcfpxKkRnmhRD-Te9vBGq1TP1gQMcoQWf5m6Alyl9jAzbBauJ0bRZAk6KRWEWqsYLZqVF23pvrwVRha5u2PwIEvX5GVw-RuBwTwa9xCAZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇵🇹
با اعلام رسمی فابریزیو رومانو:
باشگاه رئال مادرید مذاکرات‌جدی‌خود رابرای جذب برناردو سیلوا  کاپیتان دوم تیم ملی پرتغال آغاز کرده و به احتمال زیاد این انتقال بزودی رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/persiana_Soccer/23201" target="_blank">📅 20:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23200">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2P3XPQejSKOPhba5gRnvnAHQUKaFCAwJJxN8jAThzsz1U8SHu_5BJgbWNeFvGHv1Ou1mgOBbz6_EiKdxuPX1QQkpB8bG9uUcPKzaM8N8KnlLZ_bkqyOS2LNA-yV3bAZZSGsuweuTiNBNvCkT6JSp9RYJGSvcW7BYvUVaviWwn-O_VCjAuSbfz6H1FwXbbBzNGdir9Tu16Kx5P5j3qVL1XfEZHSBKIM_b2pCNXf-Q2jB43BGnqMCi2OjBBwJ4GqQh01bZyGfpPubZ18pOf0lR9rsW7vhUZkQHPxadQ0dFlqzsfEHv-zXBF1Gg-OYAbG1cOJPH_3ASzsh3wgbFqxpeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رفقا از طریق‌کانالای‌بالامیتونید مراسم افتتاحیه جام جهانی رو بدون سانسور ببینید. خودمونم سعی میکنیم در پایان مراسم ویدیو کاملش رو در کانال قراربدیم برای دوستانیکه نتونستن مشاهده کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/persiana_Soccer/23200" target="_blank">📅 20:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23199">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FaZyNY7WEQzkBwrMi1fHDAYd9adFiM9Tk9mS2SLpzo3mmJyIYc_NXE8eUXUcFZbL9Q66Oq8TSvcIh0By65ugdSAjt569fDRxOolJZUUoJEni5w-JlM7c3UtxP832Hs8PIVV3Djhu8q1lvvZ7g9yYeHjhaI7yrB6X_UYXyabUoONsSCozD-hhcpv9_iE03a6yhkBv2KYpsxZSqBGN0oRL6r_7Y5bUlSCsPP-ScOfkX_ckeYSfBufB15Mk7BSPeZwuj0wrc740BWXGwwffddRfHHWe9WD6lRGqETNuldoX_hGcsjpN_tivu5iCg72fZgn4Ixphe1VKMKqRW01k8_pIxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
فدراسیون‌فوتبال‌ازبکستان: بعداز MRI مشخص شدمصدومیت ماشاریپوف ازناحیه کمره و این‌بازیکن رباط صلیبی پاره‌نکرده. براساس‌نتایج MRI، مشخص گردید که فتق دیسک بین‌مهره‌ای او عودکرده. بزودی میزان دقیق دوری او از میادین مشخص میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/persiana_Soccer/23199" target="_blank">📅 19:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23198">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flpcspEXHEd6n0rPcI4RwCVV-kwsH8A7nZrEDsPrYywvJ5wAAU9SMU6mI6XgYw7KVTQGlPzLOusOB923_LYrLqDBqHiEhAH7uTSl2Vwmat0I4cAxQUGw4r5ryFTB6ZggT1jSS5E6fkORbZ1GY2qHpbeiJWpSh8pr9zSN3kOopyGOiCOnFok1AmcXj1iGGkabQIBNj_pV94m181NSWmAM1ovhTJKIb33cRNKQ5ECp5Xw7Twwqv9tpOEU6m_1ocNni08WU3WROLDl1SY_pD9d6GNQ-bfvC1027LkdF5mldIOy3MCBRAEhRfc815YvsaXOQO2jk0NMb49dnajIjndUAxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌تراکتور به‌دانیال اسماعیلی فر مدافع راست خود نیز پیشنهاد تمدید قرارداد سه ساله داده و قصدداره دانیال رومجاب‌کنه که بزودی قراردادش رو تا پیش از  پایان فصل تمدید کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/persiana_Soccer/23198" target="_blank">📅 19:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23197">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSwFppBjponuuwkzzXJ_7-rF1X6dYJmkLeQqXIPuKllacymlTOOFv_sUlxLVsAYui5cJ5AVZQMk0xsum7dIDsItWQNuFNqKa2ua45mduR0cl6WnNr8uvDUBTyzMExodgF5hqdMYCbusl2LXeMKqOv09Sz8jUfwRv7y-e8-pau3PV_LIq4ZcqBxGBMjDJ4b79dWvJSwtUc7_vm8n7hVnlGwcYp7MAfAAEWmVpBSKNzWPoJ-cCNgqWCJYQT9rJX7MfMJHR83aOCWS5-ijmoEO87dOIdem6VccL5nhS-k9qrmvEwCG4b0Luyy5WI45nHOtFAilKel9a6rJe7wxOvAK-7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/persiana_Soccer/23197" target="_blank">📅 19:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23196">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kDO4YTQ3xrFLqNnGxMe6VhjjbTnlubj1SeccuXWaoGHgKNhEW33LRlPl7XhsZrodQ6WgXYZ4gIrZHuUAP4JMj07adAfMoQBYYgAb7XurHcVUBlShm9hEqOkt4WIpBiZ2OAG3OOrpBdAWy6Yntv3Mx6ypYhT5JAM7dIO_cquA4lWiAYD6GrRjda-323jttnOhMyaQTvmh9SESmLI_y0HgMIe2yCnXkfSorw0VUREdi3Il5VJhmu3misL3E65GRyi81kb3gx8kRAoARzHGgyFBJOABy9acio1r9fNWImvdwbFgRB49mSGKTt9SfuCYV8DAGiaEElyrW7GPDJ68R0uFrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل‌افتتاحیه‌رقابت‌های جام جهانی ۲۰۲۶
🔴
برنامه افتتاحیه در مکزیک
؛ پنج‌شنبه ۲۱ خرداد پیش از بازی مکزیک و آفریقای جنوبی؛ ساعت ۲۰:۳۰: آغاز مراسم افتتاحیه؛ساعت ۲۱:۴۰: گرم‌کردن تیم‌ها؛ ساعت۲۲:۳۰:آغاز بازی مکزیک-آفریقای جنوبی شکیرا، برنا، آلخاندرو فرناندز، بلیندا، دنی اوشن، جی بالوین.
🔴
برنامه‌افتتاحیه‌درکانادا
؛جمعه ۲۲ خرداد؛ پیش از بازی کانادا-بوسنی؛ساعت۲۱:۰۰: آغاز مراسم افتتاحیه؛ ساعت ۲۲:۳۰:آغازبازی کانادا-بوسنی؛ آلنيس موریست، آلسیا کارا، الیانا، جسی ریز، مایکل بوبله، نورا فتحی، سانجوی، وگدریم و ویلیام پرینس
🔴
برنامه‌روزافتتاحیه‌در‌آمریکا؛بامدادشنبه۲۳ خرداد؛ پیش از بازی آمریکا-پاراگوئه؛ساعت ۳:۰۰: آغاز مراسم افتتاحیه؛ ساعت ۴:۳۰: آغاز دیدار آمریکا و پاراگوئه؛ کیتی پری، فیوچر، آنیتا، لیسا، رما و تایلا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/persiana_Soccer/23196" target="_blank">📅 19:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23195">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukftnOZ6gYHnYLZPkZSsfFi6HUnRV8nUqRz7gVfrjICaFx7z4yCsLRHZk04bYCjuCfx0fnNAxQqoWIPB_3TupqSrjlmeLDQVOW_d2DTKePV2Wa2sEcalRAT3dOb8UIu_jGwI5revV6XtospgT4pvMYBr5sYrq_D8ZFDk6a_WD-SbOO80-Mr4ZM9cQy3ESzwU1Mo8jht8tSJxZ76SbNSNjKbT-h0C9FqDu6RTQ38UsfLBk-2J16d0pbxJO_kx6-d8UOO3STDubfruaPImZkJED1PUXbx3TnQyKV-lTdCn7PFhhywCNs7seirdurntKf-p8TLar10JBlvFxj96iXqj_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا eg21
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/persiana_Soccer/23195" target="_blank">📅 19:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23194">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsiJ9xRdnn9GtpW_au47JJvEE_qee5ZDgbdJn8FJyVlrd7JhRI0H_xLmb4zaVRzTRiQvrgex9sli_EFBOV1e43rXIEbLPkPhFMhvyCcnMjva_GON074Rct26yGDz3nF1aFychcYEZ-tdiaBwgWds6w3xdqoYP_EQUG3Q_21UGyKd0AhoI1bIMGfQu1PdUUrwqcEVqmKzmSVot2pHjdjNcnmikiYAhjG6TJQvle8JMbILwy8QVK30PAP7DfOSJcF9KYnCGdCWa5mBf1_HM4k5gmRJynjTtl-P3jAkEg3FsWckfZF5MsxjUIgqDf6BXmqYYUteeL6ryvsSgturzA3v6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یادآوری؛شبکه‌های‌رایگان‌که‌قراره‌ رقابت‌های جام جهانی رو از امشب با کیفیت‌ بالا، با گزارش فارسی و جلو تر از صداوسیما پخش کنند.
📹
شبکه گرند اسپورت هم جدیدا برای جام جهانی افتتاح شده اون هم میتونید فرکانسش رو دستی رو رسیورتون سرچ کنید بالا بیارید.
‼️
خودمونم‌ازامشب‌لینک…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/23194" target="_blank">📅 19:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23193">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5yqJXy61M12wDh1HbFW9i__RdqfFbHWfAc7YvLn41b4lWlauwI5-Cq20badQ2o4QhH9Z6joHsux1w04GYHPy2eJdYUYnSyeQYr-KcW4E8bA0V4pyTCTuRbEVx2m-Ow6BF6WQkrNYfR-55_5MKGrX3kaTjuKpnl1IVWkWHLBHiLiIJPx4SPsaUVkRWKm_TRsWsWI9BPvYuaQE4DW1SF3FXwyhGK55QGV-J0qL4mGCb7nsbdnSSqe7-k56sPqSEDU5cKpTZ_zwDx-H9eOYN4YWcXmdpdFAXTvsn8TJbhUfSY9VV7S3p1taTtk0hqsIWCaEpdspxpa0FXrGMPc2kIaSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول به نماینده‌ اش گفته باتوجه به اینکه از دوباشگاه رئال مادرید و بارسلونا پیشنهاد داره‌برنامه‌ای برای‌تمدید قراردادش باسیتیرن‌ها نداره. قرارداد فعلی گواردیول با باشگاه منچستر سیتی تا تابستان 2028 اعتبار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/persiana_Soccer/23193" target="_blank">📅 18:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23192">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88bf35c2a3.mp4?token=CPs3jJEQK2HOaouuGjhgLyfqf9tjeKJTVo7trX6AJu_qzzupGXtGS2f_C_69ax4wOW1IeXF9oEn0AOVp6zHxxgsTTYGG0n3RFak8G84Vv2dcmILyKhGIOwvSmGtAKl4vvcuJTX4kbezaIyytt8AV4uqvfFaH-y4mfQYnKQy_8ur-4cKnwd6OCfw17z3eYCZQls7y24K9Y8QkOmgXjwOtd9d5vs2ueOmFw4QSd1vyOeOvVTfVMdpwyV4FnS9HOq_-FAaqTzF7m0zjwBDFL6ysqirN_lLryl7dEGMQWd9seAp5OJBkBsKbRVsvKm9w3Z8m-y4v_XPMgjXmC8ccKCe70mOOvQ32pGwKa8_CcJdJTlHlGIUBaxOOFQ_yRu6kPGyjrpbssA4D_kLtTSWASP_y6XAQFo55arDYyAjp_yhZ7amcay76_DxNJ8WXLgMdGeWtSCfAMhnVDDBIAUKy0QIdyWOG1CnZ1tHZnoGB226UKNqHykYU0TE9eTT4S_yFH86h4KwPJxf36YymM5n7fBGSDv-J8S9mvMBGFSk8LI3ENUYYx062ClrQuqeUUuz8aqsCqEjUlsnzTEWHjqQTkTI8Z9-s9wlJ0JdInWponoIC-8Gxg7y0mNDSUDI9jxmHZw4V9rmuzHHOJbYikjLKqUdSFRaMHVMmR0j4PgxMIAavWDI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88bf35c2a3.mp4?token=CPs3jJEQK2HOaouuGjhgLyfqf9tjeKJTVo7trX6AJu_qzzupGXtGS2f_C_69ax4wOW1IeXF9oEn0AOVp6zHxxgsTTYGG0n3RFak8G84Vv2dcmILyKhGIOwvSmGtAKl4vvcuJTX4kbezaIyytt8AV4uqvfFaH-y4mfQYnKQy_8ur-4cKnwd6OCfw17z3eYCZQls7y24K9Y8QkOmgXjwOtd9d5vs2ueOmFw4QSd1vyOeOvVTfVMdpwyV4FnS9HOq_-FAaqTzF7m0zjwBDFL6ysqirN_lLryl7dEGMQWd9seAp5OJBkBsKbRVsvKm9w3Z8m-y4v_XPMgjXmC8ccKCe70mOOvQ32pGwKa8_CcJdJTlHlGIUBaxOOFQ_yRu6kPGyjrpbssA4D_kLtTSWASP_y6XAQFo55arDYyAjp_yhZ7amcay76_DxNJ8WXLgMdGeWtSCfAMhnVDDBIAUKy0QIdyWOG1CnZ1tHZnoGB226UKNqHykYU0TE9eTT4S_yFH86h4KwPJxf36YymM5n7fBGSDv-J8S9mvMBGFSk8LI3ENUYYx062ClrQuqeUUuz8aqsCqEjUlsnzTEWHjqQTkTI8Z9-s9wlJ0JdInWponoIC-8Gxg7y0mNDSUDI9jxmHZw4V9rmuzHHOJbYikjLKqUdSFRaMHVMmR0j4PgxMIAavWDI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ رسانه‌های اسپانیایی: درصورتیکه باشگاه بارسلونا آفر 150 میلیون یورویی برای جذب خولیان آلوارز ارائه کنه مدیران تیم اتلتیکو با این آفر موافقت خواهند کرد و آلوارز رو خواهند فروخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/23192" target="_blank">📅 18:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23191">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTySVwZfIey8ZUE2OBeeEYPqkoN6deazvKEYUw7KtOtSwzzi4H4exUhFzcQlCQHRLj3Od96XvQwksiemzQ8DcE9E5i1TR1KIaL67vJRdKOSP3--1onEATf6ah70zaIJAjgX7Mg3EU3TvXkPhy5hElVLkoyp40gY6RKynbXxAr6fXZ_wj2j1ISTGE8nn8WbDbyD0NLTY9j0q34a4oHhSkaVvsGvOmAWMr6d422hXXnSx1o8mpu33leglElilDL98N1tQp3nw87gA9WldChfIemRcfCvue2107DtrenWABCNFzkgJ9cxsZxLTSPuanRISU9WuLj8q6G9eYxAye4TW09A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همانطور که دو هفته پیش خبر دادیم؛ باشگاه سپاهان مشکلی با فروش محمد امین حزباوی مدافع جوان این‌تیم‌ندارد و رقم 70 میلیارد تومان برای این بازیکن تعیین کرده است. هم آریا یوسفی هم امین حزباوی مدنظر اوسمار ویرا برزیلی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/23191" target="_blank">📅 17:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23190">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmPdpmVSfK_8ABu3-lohN76r8kV9x9cee0C3bvYozlANdBeHyuUHaQHwznGrjnsc9SAmgZ13599uXTGAkQ7Sox0lf0C0QdZIZUk6SuZ40HJNL6ggADW0ED4B80oLZhBaBHQMNboCQ6XWT5V6sxdc5VI_wSU0pGMJ0L7JW__73eBP3xSBv11av0kt5Xek-KFgQuGt2SMHd4pJ1fjcegvIhR77t_OU1L4gZ6AkHQ8fDFx9KEmqKOmMHTcm9oW-ARdRoozsYTKXEh7POuX6TOPlbN_tNsVCgdafdm1DZwuPmNI2iNzu2uaxtI9TeQ8ZfN4DoF-MM_ENNjE3QLjrWWDayw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/23190" target="_blank">📅 17:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23189">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_3M2vUg0hvtybZ3WEumhcJCWOem_haVxPOFthAhvxS2lwJj6tt5M5WdcpUlfpD7GSJloTvo1bc259fyhWefFcgHS2HE3woipHFMdOqKE_xeD2l8JdQ0Oq7bFEEWwDtDWI7QeSeFm7zA36faS2JLmXzu4QuOy0ipO2lXWsmdAIJsmhSmOPFje6ofo9SZP-ZWhDHu3Ue1J4LUUhcGskq2ZRu0tkDQOaKfJ8Pw9finQHsDKx2P1JNi-BGfSGk3gGRGkx1F-9zWOLRxwmaV6YTkJGBoQ_-Mw0-3I3HywtsazZ8Jwx5OgQZARURwcJeHRdwRVaZBcJV3rzL47Kq6yIGIIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیستی‌از اموال‌برخی از افراد معروف کشورمون که درماه‌های اخیر توسط قوه قضائیه مصادره شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/23189" target="_blank">📅 17:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23188">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uV0fHxocDBSCnLpUQRRCB5vDs4bJn5bAMyeJ1jMKg-d8Q2PoYPOeGYKUT4P0e511ubsL61AMLFe2dwXZOtcrn4gvAp9PosKTuKTl9NsanxHZQZQy3BpkzHXt3FpVW1hT2UusLjR_mKwaZSc4b2Kjee3vaaPMh1v40XJlghpymfH00CZ6mUge6R5Rgl5737gkkqr7sBNq6jjGWA1q95dcm4MANp8Uiu_aRMuXR18jHfKBBTYhLj8CyA1ZeX39I4HaRtWnJZ_mWIrQXvrGHC7v7zIH2tA_UE5zKxtqC1VLBjaVf73mXl44nUACvrmnC4L2r8SFwz3voejkpf_uIDcsHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول به نماینده‌ اش گفته باتوجه به اینکه از دوباشگاه رئال مادرید و بارسلونا پیشنهاد داره‌برنامه‌ای برای‌تمدید قراردادش باسیتیرن‌ها نداره. قرارداد فعلی گواردیول با باشگاه منچستر سیتی تا تابستان 2028 اعتبار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/23188" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23187">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyZt8ReuktX6a6bcwS0Jl4LARjtb1NHweMx9aCqDccHiInlnqYsmC2JK7GltSHQcxm66xQAJ5JjFd0hX2SyhWsJWnDrgJFMWei9i93LbAe6LJDjpa0r1Lhquayv47BpJi5BlBc85YmK1XgIt7eEZFzqZiTSJyt2YgUgQPejv4uzMU-a9k6YrXqcjZPFD3KPtylA7SA7Gt4P1wpfe18BtNqwRU1PnkO8qGwiS11MbmC9OAo7zXG4_iv6mgP1kMJ8lMpVaERMH1nskAHcnRoZ0Z98iW61YQlJcjg5PEL_UjGcgH8nP8dR7C4NGruLkCtT1DWaLefVy_s3Q-xibSsGcXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
حدادی مدیرعامل پرسپولیس امروز به ایجنت علی‌علیپور اعلام‌کرده‌درصورتیکه‌رقم قراردادش رو باتوجه بشرایط باشگاه کاهش دهد و قراردادش رو تمدید کنه فصل‌آینده کاپیتان‌اول‌این‌تیم خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/23187" target="_blank">📅 16:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23186">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hG4o0UwptNahOBlCDLu9EFQyd4OSEMcWx7QS1dCo7H5elusQUeKlMwkhJwjK-oOAjHEj4Yzz1MZTD38iKF0W14-0lV7tcw8dXPPf29fAms52gte6geD4uU7wBa5IRP0S1cMjL4ynju4J8RLT_fnxI8FgVhUK_4RqbN1gboBWz_4cxyqeqncxo5gaeigl-LEM2uTWaNR23bOFzvqQjjeI9wVJDIsppBH2vpGawrr6pxrY06FvLDObYKfaSCfvpcFakwaTc2EOXqA3CTRHbUZ_em4CJNM02-lIDROjvd4b42esXq4zIIw-b88aRbCTW8FHWLCjQUYaA0MRFNKdM3edUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل‌مرحله‌گروهی رقابت‌های جام جهانی 2026 در یک نگاه؛ این پست رو که کامل و جامعه هست ذخیره کن و برای دوستات هم بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/23186" target="_blank">📅 16:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23183">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlypvmNt-BkeO_E0B69m4uviI7FmVvoePTcNXzNuEPYj5-hbUvZ6x9y2BBPcJen21Diz-o8b8RD3IIr6KgjORVx1OAD_DrqJjs5ogfLTHg7oVS8UwMfzYV_LF5rzyPRVgETLUG-YEs9C3fHMXXE9_oIyQkFRCWQvWrT0t5fza1RZ-nITUNyImyvRkqg0MJwMbp_K0MqkJlKn9XdekpfQDFjk4pwK9_GSUu4YBkGN8yS6pHklfyhW9qWOIdHCyt44RzA6ezmxokLPhgcGRYyg-BPsPp7JysCPyjwih9ZI5rGu7YbFkffvb0G2mpky5SM1JZoAEOXv4ZeatVZ8akJlww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f875912f.mp4?token=MdUsYZJIaQ85iX2zp8FQZQj9pgzpmesQlGm-gT7Fx3V5wRLKKnbiJywxnOLah0ufpD4WGpbv75LRWgALGJzqTcs0uW_oMmw6NHZ5ZjUg5wiVG_knrlMi8pQNBl9CYoy7qkWNnn9557NBCV-AvD558uZMpAZI4uso96Ef3uJImv4FWE7cii3nzUyaGdxOvloiWElDY8xkahd_NLO2E0ivyEVD_tFvb97s-QKBwQRW0R-BLuSSigHJPEDn9y0LSUbfX7ULqAoiP0hDNGs9QE0ZHpakQU1UICD8riu1WlDz_LMhMzFlHlFesrOf96iTh9-R4LFt0UN6qE4dT4bdlC00Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f875912f.mp4?token=MdUsYZJIaQ85iX2zp8FQZQj9pgzpmesQlGm-gT7Fx3V5wRLKKnbiJywxnOLah0ufpD4WGpbv75LRWgALGJzqTcs0uW_oMmw6NHZ5ZjUg5wiVG_knrlMi8pQNBl9CYoy7qkWNnn9557NBCV-AvD558uZMpAZI4uso96Ef3uJImv4FWE7cii3nzUyaGdxOvloiWElDY8xkahd_NLO2E0ivyEVD_tFvb97s-QKBwQRW0R-BLuSSigHJPEDn9y0LSUbfX7ULqAoiP0hDNGs9QE0ZHpakQU1UICD8riu1WlDz_LMhMzFlHlFesrOf96iTh9-R4LFt0UN6qE4dT4bdlC00Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
مجریان ویژه برنامه مسابقات جام جهانی 2026 از شبکه معروف TRT SPOR؛ فرکانس شبکه رومیتونید ازماهواره ترکست پیدا کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/23183" target="_blank">📅 16:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23182">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hs2x9_rq81HYLTc3dmG05ec880sHJhbp9tlNo_vMEYhq59OGkyLRKZD2is1zXnU08Sya94AsQYhjIH4-wZeCrVlQnl21TaFYXerlDwZmx0JNBp_oR56LccgkDKV9oOf5tjaRlAnm9z86Xsob016K64bO1wssYeYfk2u-UHqEcpgMw-AbeXGIOdhtt2x6Una6-PLee7apJaexapoUFPGDsxZmlbi7I8mkbZGLBlr8gMFSD7_q7tvor4zJBWndRTFFc9ysru_PzBfBAW0QykPRGqLO0e-6MqGK0vgcT1rF2X5U3GsUZ-AoBmlozJF87jpy6k9OKQ4D5ve_6e-hzYByng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رتبه بندی تیم‌های ملی حاضر در رقابت‌های جام جهانی 2026؛ یاران لیونل مسی در رتبه اول جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/23182" target="_blank">📅 15:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23181">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWX8dBCyB-o8l61SRRy6zTrl9aCWWdair4c4dE9vslIZOW2jPbweBdo1ZGW4iB9iacoIcongjJ76X6vDFZmg98kEem_c0wM_DUl_CMQyOf_SsDLIbkQRwuKAObkUwz06ne_KJa9P24dUPPvYJTsjCOR81oIn4VGWWWwtVq5BaqR7JLSW6IryVigybddge0Fjd3xat4cBFQ2oPFt1K42T2WPgKcV7gtG4do7Krw6gE6zAD1m5FrpHRx_5S0Xd-5GJM4iwzeWHcrC_NNxLo6nw1DK1gVnM1RUEqKyzpoFHHSgzPzBNU5oSYBTcbe5Gl-lLM2C41924gdbhvSqGqlGcqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول به نماینده‌ اش گفته باتوجه به اینکه از دوباشگاه رئال مادرید و بارسلونا پیشنهاد داره‌برنامه‌ای برای‌تمدید قراردادش باسیتیرن‌ها نداره. قرارداد فعلی گواردیول با باشگاه منچستر سیتی تا تابستان 2028 اعتبار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/23181" target="_blank">📅 15:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23180">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e075d0a791.mp4?token=FQwOOAllXYB05rcOZaNAQZXjLAAnEq3dX2Xx6ezISxyOcjqXzfx8RhzsMEEh6o7m2E7sLEkWW8j3Cn3eEkgSUoWY5mlTZcyySpjwzhYakWCem2Sde_0UVm0MBnADsWrm25xzkY8oGzAor3Z3SfK47BKLAqZBjac4q0ExWn_QnK8nKdnVJZ0zQoDQKRX-0ikHDYUjamsgmNFQqekiNwSHcTHuDKZP8lZF9OUKMb_HRsQcIMPqurJ2siCLM5iiVTJjqB6D5hisuO-fBP8abr4VkJku_4lLM3T1c3qN63_ZKwWDR6MNOrHvF1VVgudfh2hlLreMbJAXqHb_vBetcFccxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e075d0a791.mp4?token=FQwOOAllXYB05rcOZaNAQZXjLAAnEq3dX2Xx6ezISxyOcjqXzfx8RhzsMEEh6o7m2E7sLEkWW8j3Cn3eEkgSUoWY5mlTZcyySpjwzhYakWCem2Sde_0UVm0MBnADsWrm25xzkY8oGzAor3Z3SfK47BKLAqZBjac4q0ExWn_QnK8nKdnVJZ0zQoDQKRX-0ikHDYUjamsgmNFQqekiNwSHcTHuDKZP8lZF9OUKMb_HRsQcIMPqurJ2siCLM5iiVTJjqB6D5hisuO-fBP8abr4VkJku_4lLM3T1c3qN63_ZKwWDR6MNOrHvF1VVgudfh2hlLreMbJAXqHb_vBetcFccxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
جوادخیابانی:
سردارجان تو الان تیم ملی نیستی ولی هستی، بعضیا وقتی نیستن نیستن؛ بعضیا وقتی هستن نیستن؛ بعضیا وقتی نیستن هستند.
👤
سردارآزمون:
آقاجواد حقیقتش اصالتا ترکمنمی هستم فهمیدن اینجور مسائل یه مقدار برام سخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/23180" target="_blank">📅 15:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23179">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca2e774e3.mp4?token=k02C-y28CulMeFD9A0-XkKuiN-lfHarewDS2rlJKmd7qA01s7uRI58nA3hldNLWSMYLGpl71oqxSTwbz3HCPUZJNp5Ol0ujFQRSpJmGxiKpLmkNdJZIDCRj6CxZVSX7AenVKAAMBFBWIkhKYIToJccJFdnCVgUiV2BuXVcsWX8XqcWEjqW8MR8epEq4NEfQlBWvRlvY-ZQVdTG4UXfwec-990y-GDSlQRdXl_EaefVhp-EfkgVCnjmf1WL2Dg7HJ2uXgHbub_oMfBwn5T3HbgIVDt1ZUUFlHYlsfhkXqCBSQes2P0tcY1Ce1rZgiJGrvLM99rh_uoR2mH3ArCZnopQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca2e774e3.mp4?token=k02C-y28CulMeFD9A0-XkKuiN-lfHarewDS2rlJKmd7qA01s7uRI58nA3hldNLWSMYLGpl71oqxSTwbz3HCPUZJNp5Ol0ujFQRSpJmGxiKpLmkNdJZIDCRj6CxZVSX7AenVKAAMBFBWIkhKYIToJccJFdnCVgUiV2BuXVcsWX8XqcWEjqW8MR8epEq4NEfQlBWvRlvY-ZQVdTG4UXfwec-990y-GDSlQRdXl_EaefVhp-EfkgVCnjmf1WL2Dg7HJ2uXgHbub_oMfBwn5T3HbgIVDt1ZUUFlHYlsfhkXqCBSQes2P0tcY1Ce1rZgiJGrvLM99rh_uoR2mH3ArCZnopQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
#تقویم
؛
خیلی‌جالب‌شد؛
دقیقا 16 سال پیش در چنین روزی؛ آفریقای‌جنوبی‌میزبان جام جهانی 2010 دربازی افتتاحیه به مصاف مکزیک رفت که با این گل دیدنی اون‌بازی رو برد.حالا بعداز 16 سال امشب این دوتیم دوباره افتتاحیه جام جهانی رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/23179" target="_blank">📅 14:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23178">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4PTcxzqtKBEFSjfpweXXEk9nQ1Wlj_tT9DBgmzHs9vccCqPU3Ztlgj3Fdiwv7QlLIpA9YgXLNFpq63b3hKCYIkPNVbNXkTszDyBKVa-H0UE9sehXDQW0hZSrlYahARgwPGz_Yizwm8ydw6u4LdP_SEwhopPNIyZiNr3vYnR4LCi9gP_Vg7AzVZbp0Q6ltAQ1KLGj81ROHw1FJbn6yb4GObL10WLKLnQD_kNJUjOLTnItmNmErGyvWCP7mB-cgU1eSlLmQdxk58lGo87Hzgh7MxkgJvHowOdQarLYI2QwsX-435WQUi2R5Q60zbv5abzKLE0peoUMLua0Cs-7c1R-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ادعای‌‌سانتی‌اونا: باشگاه‌بارسلونا ساعتی قبل پیشنهادی 80 میلیون‌یورویی برای جذب یوشکو گواردیول برای باشگاه منچسترسیتی ارسال کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/23178" target="_blank">📅 14:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23177">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcQke7jTHwkRkNrkuefXrQsX5twN2zEld2vUHWMKz86pEXd50ZBCQMKKAU0GWATexojGCTWa7wCHr2U_QSguImSUpNvT9hRTUWTl5cnVh2MKkwJj2MN5sBZdkyJLpCrujQ9GnV9jfrL1MHjUqHQ-OB5OfxpwKifsJgGawDy8eShiGySJmX70DnLSFOj_ipWG0yxVm4VP_Ax8pOnXt_OTCDh_MR8NjAFpMTb33oCeoWQhk44oW7mo39WF1dR2xU51Z0w6CvEqTYPb6ZVMOICL53WOeiX5rWgwerIuVYaKbtf8JBwZ6-6xFbQ5jIY9ZF7vz7_-Ew817ZmMisGD9m_uZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق شنیده‌های پرشیانا از باشگاه استقلال؛ علی تاجرنیا برای تمدید قرارداد محمدحسین اسلامی بمدت 3فصل‌دیگر با ایجنت او به توافق کامل رسیده و این بازیکن 25 ساله به زودی با حضور در باشگاه استقلال قراردادش رو رسما تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/23177" target="_blank">📅 14:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23176">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18448ed5c3.mp4?token=f9uEN4CJ-3FzBaCAQOHHOOg9LbWUuy_v5oTRt-ytL2ID8kEQVtfdT32oZ8oxKvdEnNWVhqI2M8U_vh1UQ7RzQOP6FpBznJ7g2ysAhHI537WRRFeE-Nu4RRcdxWSG44CLTPQ_xL6_sAmaolUec_z-9SacNHTPNGAUbu9fCyV9MOqwjHIH0pP-qrbBgrApWu-nOF5AWf6s-cmQGDzO2XPFYtzR3R9S6lA4LgG_K3_mTpkvb2c-DWLRRQx-g087E9OBI7xjHmDRNKa5YK-8I9IB-qqPeSwIF9GNG44tOfVxg90sFRghBB27K3cpDV1bI4odBAvhbZnm-WlO0qa7Ud26RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18448ed5c3.mp4?token=f9uEN4CJ-3FzBaCAQOHHOOg9LbWUuy_v5oTRt-ytL2ID8kEQVtfdT32oZ8oxKvdEnNWVhqI2M8U_vh1UQ7RzQOP6FpBznJ7g2ysAhHI537WRRFeE-Nu4RRcdxWSG44CLTPQ_xL6_sAmaolUec_z-9SacNHTPNGAUbu9fCyV9MOqwjHIH0pP-qrbBgrApWu-nOF5AWf6s-cmQGDzO2XPFYtzR3R9S6lA4LgG_K3_mTpkvb2c-DWLRRQx-g087E9OBI7xjHmDRNKa5YK-8I9IB-qqPeSwIF9GNG44tOfVxg90sFRghBB27K3cpDV1bI4odBAvhbZnm-WlO0qa7Ud26RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
5 تااز بهترین‌پاس‌‌گل‌های دیدنی در تاریخ رقابت های باشگاهی؛ کدومشون رو بیشتر دوس داشتی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/23176" target="_blank">📅 13:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23175">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T893ID1fPActj8WnOa1wxe6qN0nvKwHNpzUznIpflx4X6SOyXF3CHKoHcnKlPDKQo133mTHYxPpzg7_r_3k6n5mAMpOnV9ox7CRY_oMN9hhctu7p1eLr-FZnTw4onMpHQnKYgnJKkUvB_KheZDag2ZXp1M1fEfM2GROwQ2iuOTy7v7dDbvHk03ySh0PTA7tEB9qiMga8taTwAppSRO3OY7C2cNATR9eSOTcHJDkNqV-S_E4X-xUtNThpquGrnbet2aGk0zU8f12A7DyS5O5oTLQCE_bpnFiEw-4WfCgY0ghiUHhWE2hYLwN9nOG7bmG-lB7Dh8LxjbUr-BVwFkFc6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
🔴
#اختصاصی_پرشیانا #فوری؛برای اولین بار اعلام میکنیم که اگه شرایط کشور برای فصل بعد مساعد شود نظمی گریپشی فوق‌ستاره‌البانبایی روبین کازان به لیگ‌برتر خواهد امد. هر سه باشگاه استقلال، پرسپولیس و تراکتور بدنبال‌جذب این بازیکن هستند. باایجنت ایرانی نزدیک به…</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/23175" target="_blank">📅 12:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23174">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOpCrV7FV4Xe56vnk5_9Fn61bA2QJTpkQvRCEB3dxep-KmI3p61ONyqBRTZQg288ao-GZ880mgZRUhrlcgjQHCU-IvHjU6AYxVa3Tk4wN-BFEmfn1NeuFILZtqz443GP5it5F3_UCny9snHgPDXCgGrolb8MsA2AZzacoVuj1wabC05bE8_FBmIbDPy0zYyjIxMc7JS7YToUaXG35wPvKAJzfRDRl5rGFqC6pW9jS_lFvGpD8jKnyGdbfaFZMUx3YDYukfkoeX0uIJT7yU7okWZVVpYFkLKFFioQEDullLBOQBiP_atARAiuMNYZr_Fqzww0KAHgoOhsSCXX7Ut6UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
مارکو باکیچ هافبک سرخپوشان و نماینده‌اش این هفته‌حضوری بامدیریت‌باشگاه پرسپولیس جلسه خواهند داشت تا تکلیف نهایی ستاره مونته نگرویی برای‌فصل‌اینده رقابت های لیگ برتر مشخص شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/23174" target="_blank">📅 12:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23173">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDsg4AvHeLJEHyhhrP1CsSAJmkC3Y8aDq_B2jI0KpplqViyvtA38TksJTW32iopy7AnjuQaP_u4AHlmpeZkERjWVm18LwKKbqlXJStVT7Dc_AZiSbCYwUACfu4dI4m4kwv-oR01jMx7sQRomSlx-4zMx0QuVK_aApxNrxqnjdUZbAlhYO3smGUn3xZB7WWtT8p-YyelG74nqVMY5Lma_clA6OFCst9BWBgH3NGmFSM1yP7ToISAI-r52yKHMQ1cKRRl054WNoIv08avuNnmt0f6Bg-99ng-QRGFBJxJRGqrNuLVOx-h5Nx8UHLVthFEzTM_ZQxoQcLREQ0vvocfDrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد فوق العاده شش ستاره فوتبال اروپا در فصلی که گذشت؛ جای ستاره‌گرجی در WC خالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/23173" target="_blank">📅 12:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23172">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e4d302a86.mp4?token=qTjs276Gd05CdBcKb4LxMqkOGSW_WHOWYEfkOfmyBZ4U2BzPMNcFrTjqedoTabM0Vd2s6nPz8GxP6q1hJnnWJEna_U4w1qfO1WXDYJ69Ryftysj4b_KNeZTaaRY1P5gJLr-D1Vi9i_APN_DcabP7d4oDGdXq9R7wf9P7WZFld-azjzxb_MyNmFK35G4LNKvakZVpL2lFl988JfnUsh5e8zsZ_MWLOnzhgqYnLzJv9FYJOgVUr19I6CJlLjJZ9NcVvlOqbXsasFDywljdsvUROcNFuOMdywxx-xkQxQJA_KT2mVU_eTNRfu2bIM8bM7_fzVpvepygdXPh9qyz9sFL8jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e4d302a86.mp4?token=qTjs276Gd05CdBcKb4LxMqkOGSW_WHOWYEfkOfmyBZ4U2BzPMNcFrTjqedoTabM0Vd2s6nPz8GxP6q1hJnnWJEna_U4w1qfO1WXDYJ69Ryftysj4b_KNeZTaaRY1P5gJLr-D1Vi9i_APN_DcabP7d4oDGdXq9R7wf9P7WZFld-azjzxb_MyNmFK35G4LNKvakZVpL2lFl988JfnUsh5e8zsZ_MWLOnzhgqYnLzJv9FYJOgVUr19I6CJlLjJZ9NcVvlOqbXsasFDywljdsvUROcNFuOMdywxx-xkQxQJA_KT2mVU_eTNRfu2bIM8bM7_fzVpvepygdXPh9qyz9sFL8jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی‌ نوستالژی‌وخاطره‌انگیز از اوج هماهنگی فوق العاده لیونل مسی و اندرس اینیستا در بارسلونا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/23172" target="_blank">📅 11:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23171">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwqmmZEafLwrw4AuH6kXSKPpesJYK--845xyhUCZ_UFamxMMEDvGigqX2G5b0MUpGqYV2aHwlDlYyOe3AOykMWQ85JtScq7dQArQ9uVHXy8ZfbXburz6q4eYaQegZ5p5Uj3SnTmnwUWGfMsivgLny3ZTTArhOKApt1qK4Jl0my8uPvKEYnql5zVuVcON73Qr4pKGqqvtwKjPws5Osr3g5z4OvYCYh2LgrJFNiNWlM7OivJ2J6vWnBblRMuymraXl8_kSAkWbhaxRIyXkP1kd8wnROe9oCYiHkEiOQzRQSWC547jVeLu1aTqcEGw3Dzkg6FVzjELW-1V4L5QDwWw4nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ باشگاه استقلال طی‌ساعات‌آینده مطالبات یاسر اسانی ستاره آلبانیایی آبی‌پوشان پایتخت رو پرداخت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23171" target="_blank">📅 11:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23169">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cwZZgTN8KtLfZvNfwpYfh709f9-0XtxDf0S1s5Ma2yxwi9y2AoKjSi2XUZDyv0upAC0wXjNSFQfKqo_3uaLAD29JfAybyn_PnFYj0OwicrBZ1WQQv2w2jnKuprL6VZCGqhUx9XG5-xbjaiE_HDSKUnve7VstgxnzxJeP91p2m7DMKAeRPgkHXcOkMB9Vt6rHlK7j9g9TW094R76yMDlCFhGXHx8VJugXAqVogMVvMUj0tqpE95V4lFp_TyvQEivMf1CtWwUZibbQSW3Q6sC30Z7zkYf0WdP5kbN74xdHM_R2e4aqo6G3mHKGleuGmWMIB3bIYeyxBA4KnsnSujbAcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZCCXE7u7K6ey3-SpetuBxfkLCp0DhM62NlYIs1LH3Tj2RPddRTqtkg2MieygBc_P4Nbmn7SxR-z64WF0qcv8Ah01dAqO6gI-ozZVfxZq8YkKejfVxo0M_wBG1t6spOV1nTmjLKxEiHJw_XZq8sX-fgUgFLTNbOXJmdo7gkplsCwoEh_BmHj4MtdlXboXJWWAp1JqdKIFadGOZwfHp4oPtZW14iW70Rnq95peqIFF-JHQhQMmai24IW_UBOkwwi4L5OesAfaPRiWrsHgmXX-ue4-_oPAnD55aUCDXf1X5hoMzq2vUPb_bT5h4IWYs68uekHYZd0SM5bdgPbU5lRe8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
یادآوری
؛شبکه‌های‌رایگان‌که‌قراره‌ رقابت‌های جام جهانی رو از امشب با کیفیت‌ بالا، با گزارش فارسی و جلو تر از صداوسیما پخش کنند.
📹
شبکه گرند اسپورت هم جدیدا برای جام جهانی افتتاح شده اون هم میتونید فرکانسش رو دستی رو رسیورتون سرچ کنید بالا بیارید.
‼️
خودمونم‌ازامشب‌لینک تموم بازی‌هارو سعی میکنیم پیدا کنیم بزاریم. اپ آپارات اسپرت هم که چندروزپیش تو کانال گذاشتیم دانلود کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/23169" target="_blank">📅 11:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23168">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RURlI03MOKNnZNhB2MJVYRxVNMi4JIB75csk2mGUgnG74ECVP_fvoHoTvf734nLuiYnbbdUHuc8V5oN_bPj2vIAWiTyUhR6sxGGEGC7v2HLAgfz8CTervxFMV02rRcSEAAHupdpZwiLqiQs4lE7MvyPXLcbu13ijEvkArFbo0W4oSqDy7Nksz7jHz-bnr2m2uNxu9F4lLvXL3rbYAoi4_LAuoccIj5gRoMJqhXuFZmip65UFnDo_9cTE9bN_KMmqgqzjR0jlmDFUQzBh_ESsuv3ERYa9q6Iiesm6ICIQ3oDgHCoHwDtd1O2IuqnUacvvTI39thpskVEM2A5UUvXjSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛شهریار مغانلو مهاجم‌ملی‌پوش‌باشگاه اتحاد کلبا نیز از دو باشگاه تراکتور تبریز و پرسپولیس آفر هایی دریافت‌کرده و درپایان رقابت های جام جهانی پاسخ نهایی خود را به پیشنهادات خود خواهد داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23168" target="_blank">📅 10:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23167">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22d9a8eaf2.mp4?token=VgCc_GXdzj-IjF7kLJx_RTced0-7kztpp6iUuvOZaco4xNjB0E99Z0zu9cld2O3z8yqNZHbaYKjcAc1KXdmpaJLG1VoCQJnu8iz0A4-uucX-jmdPFVXeq10XwryhvqXrYi7TfsSZ7UTpboBpr9i-r7kqdJwl_PF9_0zAfn3YmLbTp5DfsZBprDCAbh_Ll0czkqXtRt-iZuaT-GzJ0L5R6alax_IvSgZM57uUMx559tnoVGs7HRKfFtpcHMlmQpolV-_3d7z1uPstU85LVkhC0P6oYBpgOmCq5ALJZlotv2zRH2gajxSttoHOYiMS2C0WJrW250Es8LN3WcD0aPd-Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22d9a8eaf2.mp4?token=VgCc_GXdzj-IjF7kLJx_RTced0-7kztpp6iUuvOZaco4xNjB0E99Z0zu9cld2O3z8yqNZHbaYKjcAc1KXdmpaJLG1VoCQJnu8iz0A4-uucX-jmdPFVXeq10XwryhvqXrYi7TfsSZ7UTpboBpr9i-r7kqdJwl_PF9_0zAfn3YmLbTp5DfsZBprDCAbh_Ll0czkqXtRt-iZuaT-GzJ0L5R6alax_IvSgZM57uUMx559tnoVGs7HRKfFtpcHMlmQpolV-_3d7z1uPstU85LVkhC0P6oYBpgOmCq5ALJZlotv2zRH2gajxSttoHOYiMS2C0WJrW250Es8LN3WcD0aPd-Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ فیفا امروز صبح به فدراسیون‌ فوتبال اعلام کرده در بازی هفته سوم مقابل تیم ملی مصر؛ شاگردان قلعه نویی باید با بازوبند رنگین کمانی که نشونه حمایت‌از همجنسگراهاست‌واردزمین شوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/23167" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23166">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmN99d6zr0Nq3xSbt0O9mudtQKeDgyUhV5Y657y_XKraw6bPiFynFRPequoJti_5Iz2jTdGUpy3B1pSQeeNnr0rllOkNztw9QDTaSJTrGl-FVbJTqThAwjXFwsezGCwcdVyWJV0nRaz1sPgsGEtuBlFv6BEcjRw2J91ZsINSsy9xLtbnOaYP5isdv7X2v3GLgUsixQKzRISDivrDFt07PfALpitwQzB1Xdz_PmCgqRkKSGxcGXkVtRRTMURHmCNEzZz2eO3GjMpHLJiPQ1Nvf-gDVfRoCEMSB9eeb0J8PMmnI3h_HvVpqUtGV7yEC2BYB3q1D0SNC8MshcsUPGp_FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تورنمنت جام جهانی 2026 بادیدارافتتاحیه مکزیک و آفریقای جنوبی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/23166" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23165">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uj-jshcnUnejIkeCb2gtDtQ9MG0jZrIcy8tNA2roODVHK_KbFNIv9jhcD_hzO5hDaILdHupW1CV4V_LU31_KxmIZDQLRbwxr3sZkZ3bCDfTPlxMeMYelK4nJjxZpBrK7g4DiXFaXxBBx39zuJWvtr5uM--lCukOY2D4WVPycrAa3NVQOuAFvy5XPRp00noTCo-9_ElJSxyFgKl_WRQQ51Byq4G8Xxp86TJtpL2o0I_Kx9GGY3g94ZB1M8ACnosyZ1ldICRKMQ7aFoxYsd76c1GNTw84gIcLG5QD5LwifhC2yhQTcYmGjP5uCoSPpDrpvxfNm8EBn8fi-aPt4JXqwkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕔
انتظارها به پایان رسید
📃
از سایت وینرو رونمایی شد. معتبرترین سایت ایرانی
🤩
🤩
🤩
🤩
بونوس اضافه به ازای اولین واریز
🔴
فرصت تکرارنشدنی به مناسبت افتتاحیه
🔴
⚡️
هر چقدر شارژ کنی، بیشتر هدیه می‌گیری
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
و هزاران امکانات خاص دیگه
💰
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا er21
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/23165" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23164">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e065f47574.mp4?token=VnodEqh5epSeFjC1AG2-ABKE-kaQO9VbLk70EtzW6cWRzTj1NeZ_6Nuwtd_Cjc85cB06kcbzV94OUA-FKgspq-DUBbUNDX6Z0IrOfd0BYr4fC7yh3PG5NDEkjGGMXYGtB9SePjBSyHGCmqdjdO3Y_Kg4qWgtMZO7l6ataJSOZcLLS2hlttk7U8EUYW26O-jJtKs33PjvI1D567D3ujwTwgzqQrR8_b5teqyx5Nh1w7iVCj8ATYKb06Dua9oqYo0EIe6D0tGBGg0AGlHPy8IloyMBjgNKL8CJ3vjgk-1OJ3Mb7xpecStAjK23t1XPzkxi5XeKXxTlmxDUmAZtNjRauX36_-HJwhBRxOU0N3ZMZR1pQHB0_7UM9B3QKtKC_9vV1w5B5cggwwcovQl8Ly6I8r5jn2iTDL1cVVIKCPsVuCjvmf8qsAJPfGR5Wbx4RAZ_gTgAvFxLm1qMODIGpK1R_AUThyzBMLkby1RxEUOxvjEsaoHQ2ob_m630lyFLIjSGenmaN4hx3_E96Ds-_yUZUgO8sitDEwSQKY1WmVJTB0J9mS2_U9HknakKoUPGKlGNjpWwjAI_CTK42Bp1iuLoIENTJY20uwBg6RLvCTacaRr3IxtEQlOqSs-Ge40JtuH8gjCeP0JFm3O4QWBxwgJAetm-L8RFV82YWNdNMAZPDq8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e065f47574.mp4?token=VnodEqh5epSeFjC1AG2-ABKE-kaQO9VbLk70EtzW6cWRzTj1NeZ_6Nuwtd_Cjc85cB06kcbzV94OUA-FKgspq-DUBbUNDX6Z0IrOfd0BYr4fC7yh3PG5NDEkjGGMXYGtB9SePjBSyHGCmqdjdO3Y_Kg4qWgtMZO7l6ataJSOZcLLS2hlttk7U8EUYW26O-jJtKs33PjvI1D567D3ujwTwgzqQrR8_b5teqyx5Nh1w7iVCj8ATYKb06Dua9oqYo0EIe6D0tGBGg0AGlHPy8IloyMBjgNKL8CJ3vjgk-1OJ3Mb7xpecStAjK23t1XPzkxi5XeKXxTlmxDUmAZtNjRauX36_-HJwhBRxOU0N3ZMZR1pQHB0_7UM9B3QKtKC_9vV1w5B5cggwwcovQl8Ly6I8r5jn2iTDL1cVVIKCPsVuCjvmf8qsAJPfGR5Wbx4RAZ_gTgAvFxLm1qMODIGpK1R_AUThyzBMLkby1RxEUOxvjEsaoHQ2ob_m630lyFLIjSGenmaN4hx3_E96Ds-_yUZUgO8sitDEwSQKY1WmVJTB0J9mS2_U9HknakKoUPGKlGNjpWwjAI_CTK42Bp1iuLoIENTJY20uwBg6RLvCTacaRr3IxtEQlOqSs-Ge40JtuH8gjCeP0JFm3O4QWBxwgJAetm-L8RFV82YWNdNMAZPDq8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
مجموعه‌ای از بهترین آهنگ‌های ادوار جام‌ جهانی از سال 1998 تا 2022؛ کدومشو دوست داشتید؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/23164" target="_blank">📅 09:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23163">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJEiBj2yF-RejoDEih52D4SFwnjPdAFEx7qbXMmuPQaqU1uFSYS3BVC7JH2TwcrfzlMSU1dUVAY8ui2BfI6MgBEJoMbygkWtxqn4hc0rW0336IAbMv2AEwsgOsHIt8VKguyky4Q-EFxbsRadlq267j0VLUS6G-m2FeJkWpNrGqQfOIGh1xyWeoRbl1XTAcDnZHSOv6RPsIhK-QY9CxKj2D4YpWeZ7XCXlFBDJPNhcV5-YgOxi5cMfg4bq1-Dhzbbdho6x0dT48g20IUgilCLR9RRzIlXOzcPo3imEWjmHDGxeS82S-lUD2IPtA_gutOsJyG8_DBGg7WDFfvJHt5mug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
مجریان ویژه برنامه مسابقات جام جهانی 2026 از شبکه معروف TRT SPOR؛ فرکانس شبکه رومیتونید ازماهواره ترکست پیدا کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/23163" target="_blank">📅 09:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23162">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VX_FykYT2c7ggN673H-mXYpF_Kq1kfWnA_9FmAkViWAJbhRP1r-ienkA3HZIyJtcYzqJhsq-_7KjMVRhQla2myLSDGwpDOASIAiNy7xDwi6OrKVhd91-qdUh2dnVGHvIAmp_s65PWYe19JJRXNmFU5FXFY3W6LFfBjz-9R-vHQVJVgeQHQFoS7m58xSfqXjS8xBCDyyGfefHw-TjoXnvWRw-3qAvJNnki3k_lRE3KysK0i9kbWV3iAoAMb5qAPe8B003VJlOLoAjGcTaGyqyoDb7bin1NCAPw-8oLYjKX5Se_3CZ6X0kqABmTy2GunjqX-_f1viodksDALEJXv2l6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادی‌ترین‌مدل‌‌موهای‌بازیکنان‌وقتی قراره تو جام‌ جهانی بازی کنن؛ گل‌سرسبدشونم که برزیلیهاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/23162" target="_blank">📅 09:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23161">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1bdb0ad97.mp4?token=ec1-jxbqZ6ryWOUSvn8nwZWZ6DhTA3ALpsIjD1kzHGzFXYEIp84C5P1aGszXirBVnByf2eQc8EgfuD-ijzZcMyNOHe1Ivko26QqKBVhnoo9hFu9tGVbE2EhTSOxBabRKKzzWsYqsqjjJp2Yvs3QpmvG63iWYmsFUDc0aQZ7ku6txhm8cyJkzL8OJo3KkgR0OkEsYoUMeY9gMwcUXLD_9tBeSE0Guj7iefphVttTHszS6FVRJU_CK7F_mD0bzcfM_bYQ8lW7oqmUPzbMjngDxBPwIqfCoVLru773nwjbwDk14YZuT5UwJRp44ypyedcFVToP4ZsBfA1fIhUOrQ4WPWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1bdb0ad97.mp4?token=ec1-jxbqZ6ryWOUSvn8nwZWZ6DhTA3ALpsIjD1kzHGzFXYEIp84C5P1aGszXirBVnByf2eQc8EgfuD-ijzZcMyNOHe1Ivko26QqKBVhnoo9hFu9tGVbE2EhTSOxBabRKKzzWsYqsqjjJp2Yvs3QpmvG63iWYmsFUDc0aQZ7ku6txhm8cyJkzL8OJo3KkgR0OkEsYoUMeY9gMwcUXLD_9tBeSE0Guj7iefphVttTHszS6FVRJU_CK7F_mD0bzcfM_bYQ8lW7oqmUPzbMjngDxBPwIqfCoVLru773nwjbwDk14YZuT5UwJRp44ypyedcFVToP4ZsBfA1fIhUOrQ4WPWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇺🇾
جالبه بدونید
؛ مینا بونینو، مجری سرشناس آرژانتینی، تنهااز‌طریق‌چت‌اینستاگرام با فده والورده ستاره رئال مادرید در ارتباط بود و قصد صمیمی‌ تر شدن نداشت؛ اما شنیدن یک پیام صوتی از فده همه‌ چیز را تغییر داد و او در جا عاشق لحن والورده شد.
‼️
درادامه مینا دراقدامی‌جنون‌آمیز و ریسکی شغل موفقش درتلویزیون را رهاکرد و بایک بلیط یک‌طرفه راهی مادریدشد تابرای‌اولین بار او را از نزدیک ببیند؛ تصمیمی بزرگ که‌سرآغاز یکی از وفادارترین و پایدار ترین زوج‌های حال حاضر دنیای فوتبال شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23161" target="_blank">📅 09:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23160">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea36e1943.mp4?token=kxqtHwI7o3wVgZNZLWlI6anhTcEk0E2EeID9vGetocW1fjZUdFhVxxi6FmbIMslhobObyig6WADz5jN_AIraXNHsUKtfvBh0nDVD6-OSFbwhlfFuotUxExjCqP_Rz7pUsFPqibCzomwCKTn1-GoItbYj1tLyX0ps8TVyDbTEzDA0d9T54nmQR-PjQD9WKGk8xL5kNDKH8tgqmBg3uE-TDCsm8RDRMQhxhbl_BkaW6_u1Nz3IGw2novra3-4GRw9S7pNC5K_n4GADKEab-IOjnpnZZoyVYLZJE2L3_mgc3vLD7xhbJqqColDMR8C8w5TZ37NB6DTZ9LsAjRCHmxc63pPf7rde7c7bLakYDXwf6vU601Dp7lLlQV2_VCjxFJITm4S5uAVGplrg4AX3bAyrirACHdwGR2DRmIxGOkAnMSMCqPemtNZUQ4RA1GcWTmyY9CJiDBXNzcbijQ-TQxYmdvCikk1JAti50iAszsKxvWoyDTixAJOEUaeHbMvQZLvxF0I3D335t8TguYBeu-lyNi12_qJIt90nVdufKrlokYY0b2uuZh1Hi7mrV97LuiWD6x2pHrzOin4rhpgpuuDSn2cb3MoGFkpswTD_QM8J9WUttTtubvVzQJzfFw5ahVy6ISFbiJJD-vV55GJ2bPu_aytilR3RUNTBRwjyP6aP5_M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea36e1943.mp4?token=kxqtHwI7o3wVgZNZLWlI6anhTcEk0E2EeID9vGetocW1fjZUdFhVxxi6FmbIMslhobObyig6WADz5jN_AIraXNHsUKtfvBh0nDVD6-OSFbwhlfFuotUxExjCqP_Rz7pUsFPqibCzomwCKTn1-GoItbYj1tLyX0ps8TVyDbTEzDA0d9T54nmQR-PjQD9WKGk8xL5kNDKH8tgqmBg3uE-TDCsm8RDRMQhxhbl_BkaW6_u1Nz3IGw2novra3-4GRw9S7pNC5K_n4GADKEab-IOjnpnZZoyVYLZJE2L3_mgc3vLD7xhbJqqColDMR8C8w5TZ37NB6DTZ9LsAjRCHmxc63pPf7rde7c7bLakYDXwf6vU601Dp7lLlQV2_VCjxFJITm4S5uAVGplrg4AX3bAyrirACHdwGR2DRmIxGOkAnMSMCqPemtNZUQ4RA1GcWTmyY9CJiDBXNzcbijQ-TQxYmdvCikk1JAti50iAszsKxvWoyDTixAJOEUaeHbMvQZLvxF0I3D335t8TguYBeu-lyNi12_qJIt90nVdufKrlokYY0b2uuZh1Hi7mrV97LuiWD6x2pHrzOin4rhpgpuuDSn2cb3MoGFkpswTD_QM8J9WUttTtubvVzQJzfFw5ahVy6ISFbiJJD-vV55GJ2bPu_aytilR3RUNTBRwjyP6aP5_M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاگردان‌جوان‌روبرتوپیاتزا درحالیکه ست اول رو مقابل تیم پرقدرت‌برزیل فوق العاده شروع کردند اما درنهایت 25 بر 21 این ست رو واگذار کردند. پیاتزا درتیم امسال پوست اندازی بسیار زیادی انجام داده و بازیکنان جوان زیادی رو به تیمش اورده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23160" target="_blank">📅 07:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23159">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfa3df8180.mp4?token=RzwxnAwdYPIMZrHP4bF0kjyaUh1wyLf7-6dQBxMS8p_gZwxJx9vMj5jd2ykyTRb-bVprfkHCN7iPtU9AfR3DrTlbzeWblb2boh5pyhwlp207bX6Kcyxy40UJROlLngobY8EUvYxiPxNAUnsgNUmBMbcDnAFCnljLQYYovsDOnl7o_H2vAsA3VSat0FSaRLK1EYtAL60LvvYVYbkUV6YfUjf8B1UCJV8UbPWe9rim74wLy7Hx8zIC_ToO2qKlSeAhJpbTm-D_ukjplbLuhkwYaeYgpGao1n3ocRkLPGxe3lIj3hoSlthx3NMug1MEJIXT8UuCmQlX6T4Zks4aP-M7YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfa3df8180.mp4?token=RzwxnAwdYPIMZrHP4bF0kjyaUh1wyLf7-6dQBxMS8p_gZwxJx9vMj5jd2ykyTRb-bVprfkHCN7iPtU9AfR3DrTlbzeWblb2boh5pyhwlp207bX6Kcyxy40UJROlLngobY8EUvYxiPxNAUnsgNUmBMbcDnAFCnljLQYYovsDOnl7o_H2vAsA3VSat0FSaRLK1EYtAL60LvvYVYbkUV6YfUjf8B1UCJV8UbPWe9rim74wLy7Hx8zIC_ToO2qKlSeAhJpbTm-D_ukjplbLuhkwYaeYgpGao1n3ocRkLPGxe3lIj3hoSlthx3NMug1MEJIXT8UuCmQlX6T4Zks4aP-M7YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🏐
برنامه کامل مسابقات شاگردان روبرتو پیاتزا ایتالیایی در رقابت های لیگ ملت‌های والیبال 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23159" target="_blank">📅 03:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23157">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JISVUcOsyG1N8Se3hZIAXqI5kC0fxcAH6_D5uyTC4RNzNZYEIM1sVz-FakL0Rl-ODF0Np_I1St6ZI54WIP_7WbHCPUTnzZihf3_OYARMcAu1VIyFx4hMzZgqmx2Jax6zo6i0-AzhXSk5FDvKIDP__qCUkmwCbB-f9nuAP11zSlLpeMNuZVxXegLmOXAU7qPdzGnuJdes8z_KMwzfHvoNM45W3m4Q6Q6YfMZtLY9Pc-pTck3nvNNWhMqEyh0iYOUlzNeUnUeqHYNru2dhRYLs6WXQP_N9S1g6L8DN_l5aQ9X1ico9vYJXet1S9oLR1A275kASYTIsbuOEa9Wvl78h5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
آغاز تورنمنت جام جهانی 2026 بادیدارافتتاحیه مکزیک و آفریقای جنوبی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23157" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23156">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cgu-0i0HwcHnShBGk8o0SgOSl-kzkdDDhQkhVErQqObqVPPQiqvqs9ROzX7IzTUPxPbJVEi9rwEVeHqlaaUS5UEMtpYMj4G0zL9n9JT0SCCHNIP4zHeSf4RvskpscCczACYdoLn-UQTDtNWeCpgEKsDDcs5PvrrDYEodEZAu0r2HGn_HI_NTs1PAl8CYCcIkSUcQ8EI1z6goQ3wXw-kZ9qkOSwPdMeX6AOfkHtgwCaRHE3rmmUyOhMCy8dwD6JKiKumxjHB2t3CBpJyWTfL9rcruB8HF5jraoN8uMIiEfhj3mydMq6RYxsRVDVi94NxK6uhsuVjP_mqoRL0eeZgYJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌دیروز؛
برتری‌آرژانتین‌وپرتغال برابر ایسلند و نیجریه‌پیش‌ازشروع‌جام‌؛ انگلیس هم تاپایان نیمه اول با تک گل رایس از کاستاریکا پیش افتاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23156" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23155">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDeMNqu71_8mYGU2YOgVuBXusXusvH07ObMjrbtCVN0RlqYtGmz2Yy2AkwvDURoS2gO1Flh-2p6J7MomJPf5NztjoJ0CTV-mRXo0CoV_Mgy1ZTKsLTPfhgISq04CSRoqYrIlRUYzg1V37rm0v1k3rw5IelfltBgLg2rqv2BvR8esBHg7TbFJODjVfXfh6hBHX_xXtbN74c2yz4RscT9OdGFkaasAMRSrSs4C8RsVKmKBDFOXdFtGf21JXrHmtGgPvPw2L-zkmfUZ7rS27DDBJ1fMYFCRh9HE2l7H42XnGUYPfMRiK4U8WOkB41U_9Jak8ORnBo7R9JcNvDNAW8dZnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
❌
🇮🇷
— سنتکام آغاز حملات علیه ایران را که از ۲۰ دقیقه پیش آغاز شده است، اعلام کرد.</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23155" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23154">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">▶️
هایلایتی‌ جدید و کامل از عملکرد نظمی‌ گریپشی فوق ستاره تیم‌ملی آلبانی که مدنظر سه باشگاه بزرگ پرسپولیس، استقلال و تراکتور قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23154" target="_blank">📅 01:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23153">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCo8nSv38jnXCgl1FmPbM0eysqL_gecfQgEXv0T3V9TzyD01G7uXzINE2kxj6MsLu9o-qgePaLQ9pvnW0B_gCSOE2V_iaheUKz24y7TohJdW_O0wIDV_ZCY322IfK3zI5PdTgM62f0Kih2DWNxsuwskmoLRetgBQKaCxFwbZHjX8MHwQ1noj1Jq5q6tvUDUuiNqmNFih7kyaLYjD4EjYPSzSBZSk2HjrxFXcE8RBSiGzxClfgE1AcjboozBbm2U4w9Eoq4kVZxBPecKTVb4e2Pd6FpR5TXz2MU019WxXrfUv6eA-LzjWBhq7rp71clmfYl-rLTRjHiLZ3JpVCPEYvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ادعای‌‌سانتی‌اونا: باشگاه‌بارسلونا ساعتی قبل پیشنهادی 80 میلیون‌یورویی برای جذب یوشکو گواردیول برای باشگاه منچسترسیتی ارسال کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23153" target="_blank">📅 00:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23152">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d36c28277.mp4?token=M7KAoRnL9pz81wP0JlL89g_cv-qOHU3nA5TbhdCd4LqL9NPGyYOBAfGzgW9FneAjIzmh8ozUo0PRgPfnNaCfaL3vAJ97c64r_pO2cAcdwGKajHbL-tcQwIywdoFw5cK7AjM8wm8BZ1swqO11BxblV7Tgj58Q6R48A8XZtTeT3pw648Ho9IwaVW6A0zJOyHXNA37hVc3mNFoLbTeotf3Tq1rMyrGynmY854CtMS0uEOklD1hIepvzoicpC49CyM1dpY3MQ0oYJA4FRUKv5jJFyaJvyyWW5T1i49NKsMfKbvxFbNQOOua7x247cUQx-7hU2U0n1swYfE63FdVF2UXvSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d36c28277.mp4?token=M7KAoRnL9pz81wP0JlL89g_cv-qOHU3nA5TbhdCd4LqL9NPGyYOBAfGzgW9FneAjIzmh8ozUo0PRgPfnNaCfaL3vAJ97c64r_pO2cAcdwGKajHbL-tcQwIywdoFw5cK7AjM8wm8BZ1swqO11BxblV7Tgj58Q6R48A8XZtTeT3pw648Ho9IwaVW6A0zJOyHXNA37hVc3mNFoLbTeotf3Tq1rMyrGynmY854CtMS0uEOklD1hIepvzoicpC49CyM1dpY3MQ0oYJA4FRUKv5jJFyaJvyyWW5T1i49NKsMfKbvxFbNQOOua7x247cUQx-7hU2U0n1swYfE63FdVF2UXvSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادی‌ترین‌مدل‌‌موهای‌بازیکنان‌وقتی قراره تو جام‌ جهانی بازی کنن؛ گل‌سرسبدشونم که برزیلیهاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23152" target="_blank">📅 00:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23150">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WG0hfBafyUvxZt9C1o6Y_XNmBpjzAFOqVy8KwY4Zrhu2uqfBOCkyktPUy6R1HkYnkgQuQ36qa8S1fuRJECoHc0g46ZlN1Q6dZXo4WRiFXSv3SAlbMqXnEk9Yv3rXQUhyaEbZ64fJKmbMkeZJRAu5nm0vRWGP7YDmZbdGEIqWFwEcLMt_JMEAYcfECArlzlDdVN1TidmVtFa1EkSigULBbOn7cakqKVyRYrykMLIy0Fq1hG3VwP3eTIYyxqKKGtBYqHNfm_YBoGMeJHyNlloKIV5cKaq_7WcMvGQ_MefYzuoYSqZgH0sbtUdRAzFcUMBVdKpk7DAs8bymOy98WI4zkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ دیمارتزیو: ژوزه مورینیو سرمربی رئال مادرید از پرز خواسته از بین یوشکو گواردیول، ریکاردو کالافیوری و نیکو اشلوتربک‌آلمانی دومدافع رو برای فصل بعد به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23150" target="_blank">📅 00:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23148">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxsxLPmbpPWlPAL-xJPVwqSnzhcc2FWfUX2iywuUcTLPCCtkwZpoRoE62QJi9dVe9KpmfUPgvAON4--Zv1gcV5HHG-FlLOxBBxFocqwib5bji0d1tPHWSFT-9hr8uJotZK_vZCDstlvMZTfjkO1R4mB2mpEetpzCI6dac8WWfWTCDHL-QUFvrxqJJi0CsHsUVwaSGwlOABoEuNuj5PQX1ljqOoFsJNWnqRfswsel7eqdgxYhMkYuIgxTIro6jDAnA4IKuoykCjyyW7hloiVN-NgDfYow0c8Z5N_OpHH2GfKvTBWIUTUHOS1RPovBZZU4I7VxjH_hhasD70vWdX3nPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23148" target="_blank">📅 00:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23147">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ace048c41.mp4?token=MUcBGKMRVwhbfC1Nws3IEY7hvI_gIVFnb1pFE4VawpQlXcu3aM9YRdGTuRSF4nUovYFo1A9WhIFTSR_1_nsgdQFjHMxLGEw-noW0p94Uz_YpWdcMAXAqnb4qFugnrSdjuZn72LiKyovIOH7XA9tEpsEvoEdbGkPDP27NdJHqNQCSZJ-TzSzuOxKmRxtv_8KF_3MZ1fFK3Dh-bCUZDPqPGshN3Y0nyB560wKxY7iUGpe2rDWvkWAvsMsw_Czn6mfgi9TXhTMGSTEZDvxYZkqZ2MVVsN4ZyefGA0cauGZP9hUmSTAFRydgg_uTODU3uumjX8t_2OdeTARUNGCN-6hc-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ace048c41.mp4?token=MUcBGKMRVwhbfC1Nws3IEY7hvI_gIVFnb1pFE4VawpQlXcu3aM9YRdGTuRSF4nUovYFo1A9WhIFTSR_1_nsgdQFjHMxLGEw-noW0p94Uz_YpWdcMAXAqnb4qFugnrSdjuZn72LiKyovIOH7XA9tEpsEvoEdbGkPDP27NdJHqNQCSZJ-TzSzuOxKmRxtv_8KF_3MZ1fFK3Dh-bCUZDPqPGshN3Y0nyB560wKxY7iUGpe2rDWvkWAvsMsw_Czn6mfgi9TXhTMGSTEZDvxYZkqZ2MVVsN4ZyefGA0cauGZP9hUmSTAFRydgg_uTODU3uumjX8t_2OdeTARUNGCN-6hc-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
#فوری
از پیت‌هگست وزیرجنگ‌آمریکا:
سنتکام امشب درگیره چون پرزیدنت ترامپ گفت ما امشب ایران را بسختی خواهیم زد و این کار را می‌کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23147" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23146">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDGNjWOmDlIlRLpFG4bYaBtWODNtajbhPY8Dy3Ul9Os9NboJbRs4u09c4BoiSuo8gaUeTX2kPEpGEvUs5Zb27FM_IxxI0J_70PjIQQZ1x6ARqTNdZ5t7-NQhIWRce6NCoBszhHroOdcNymNxcJ370MQWhJvjdyoYWdYwMOo5GhpccQMKk6o9-Fydo4LFqwQ46l0ZGj7qG-ROY42E6sUaC2vqxfozfw0xpAcKitU_3apIBUgcnqak7qaqzPNmT4Vd3ttShMZbAho7ifthiMjVgXOkq7A15DfErWt9Yj2nhZQZ5EslH--g_z1hGwI3JIJl2hoRNlzVVENKi07iJp7NRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23146" target="_blank">📅 00:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23145">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6jtiF4ZY1FUdNy_Mz7l5Z3F4ZGqs-cAUer5Lk7H5KE00cyjV0Y0ymviCYTe4MK7D_SaMHUFZ4wTBKz65urc-P_gO1w2GzFjIum2PjHPvzTGvPhQGBbeR0qRURfQxqdV3PF7vEgeBTcK1p1T_DQjlgWTRIBkH_kcpRSFY7nwApU3HzmoAJn2IhK68Cm_preCm9SzfHqiI33lxMfIM4pa4wf_tIqWK3JfzTfEEDa7K3itc4A5kqBLYGIzRiemd_G2xzIhN3FJVwL3Z92QY-aqrJgMDKzsRgXyEAkL6KCRT3qPm4c0vTQEF0Yj3Fn3w3MZOo8XcTA0NcU89dAT9WYL1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛شرط مالی علی علیپور برای ماندن در پرسپولیس مسخص شد.
🔴
طبق شنیده‌ها؛ ایجنت علی علیپور به مدیرعامل باشگاه پرسپولیس اعلام کرده که این بازیکن علاقمند به‌ماندن در این تیم است اما برای تمدید قرارداد خود به مدت دو فصل 250 میلیارد تومان میخواهد.…</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23145" target="_blank">📅 23:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23144">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngvupn1QJQaHFOL2SbNOAhg4s5MxsXctPOZXkgt8sw8ULyE7u2QUf9vQUYo2Iwb_9hCgVbCpXjRD5MxAV_SF2QXRoQmUca2fMKz6K0wHO8CRTO55vxG7idLLjwz_aZuYZ-pnr6AijjuBpctfCH3bCV9cI59U25NhxHYIOzpHVQHS0ZJBhSAeDwoVXc6yuJVbyRQdTCscLIZ1_SXmlD_8pC9UceVlyZbcOX7rSyyiuPhIVBs7w8oP52reILaSJrLmWdZeUWU8qZLfzs3bL55jjn3mu8BfPUPLG5BgSivQO0es57JnrPm-7nDYDiNSPEwRHOHMrPLx_LD5MYY5qx4Jhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛شرط مالی علی علیپور برای ماندن در پرسپولیس مسخص شد.
🔴
طبق شنیده‌ها؛ ایجنت علی علیپور به مدیرعامل باشگاه پرسپولیس اعلام کرده که این بازیکن علاقمند به‌ماندن در این تیم است اما برای تمدید قرارداد خود به مدت دو فصل 250 میلیارد تومان میخواهد.…</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23144" target="_blank">📅 23:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23143">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfaKBaNokTQ9AQf2myWmkQ6qDA9N7jsjAV1sO9komPhKEvy655LIxWdMaaqWFiQ1vFwh2FFa_J1wpgQjmp8M6Y-z8cqYdmROuXro14M_hDvlY34zYfVnkWXTqbbiz5M7ytZ6rgT1OsS3tTH2CWuc8vacmVvG4o1rtiuCXZs5HnIrISf2s-PJl4aZBI3VJL_1mSvP4Z1Jykbvdj-Yti4DLpFCytF8tqLQSBHmCBX7FuAdGt1SoQ0SCyHmd2cPyQdaG31YZ1JDblIveNaLndKa1fiET_rU8vrnn9yMwukK2ySfiCDfyjAkluYHen7wnAvT2EjAo1QPeGJQyqKfIJQ8-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23143" target="_blank">📅 23:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23142">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0ABNACcD0nahynud1RW3R5sK4ppq4G-RWNAhrd8_xxxPsmTnByVT3oY07Yy3KWHSv5eOdf6dB16aq4TSTWdQyk-jBRFp3_cadv2ntLDu60Ej12V2V-xluVv_Yu0MiWC7tVgebay29i3aZtgknyzh_p0ZUNltKescQWbFugLkdxpCYs409lw4SPOYBFhzzb9gtz5CDUL8oDy5wlN_s2WGXbqJhFTkxfVJ7aeEJQ8BiRKErG9cAnhCTj4H2NuBA2MX0RJCABpTFaCERUjsCaewa6S15CI6_APIXvvSQSIdmAwNH_MihBmtd_gYdUvJmFNHxT7XL47B8rK0VdQZHH4Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از امشب‌اخبار داغ نقل‌وانتقالات باشگاه‌های لیگ برتر مخصوصا چهار باشگاه بزرگ ایران رو هر شب با جزئیات کامل و دقیق برسی خواهیم کرد.
👍
بارسانه‌مردمی‌پرشیاناهمراه‌باشید.قراره بترکونیم. اخبار جام‌جهانی رو هم زودتر از هر رسانه ای دیگر در سریع ترین زمان ممکنه اطلاع…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23142" target="_blank">📅 23:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23141">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwBe4HF0Fl9L34IRWhmRUr4OheqQsRG-7SEZwlPpBEptaLbmcfssseA99HQh7B40s8yos6dq7dcOSfLf_vGRqxjMiwRzW8g9ypvGu5i3vY-K_kMoKgI1Y3RS-uUuiRL4GVHVnFLEvb71bold8DUBAa-BLlCixo-Qj_eaVRbp33IO9iI6QYYhcD6YE4OkuBvzjURyiPjlMEhW-vTSTv5ui6Y2YcmYdhSpE83NXC5IVwpENw_gOTlJvtS-U8p7KMNUGh73Wdwx38l663uC0uGZEUOYafJ09l4nJLobCpwcUhr3riHnrSWmRbqO0xDL92DKPk7ZBjRi76beEGC4UM4Z7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ متاسفانه اموال و حساب‌های بانکی و خط موبایل وریا غفوری توقیف و مصادره گردید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23141" target="_blank">📅 22:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23140">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64161e2ff3.mp4?token=ex_0qyoqjMULN6IElbo-CBTzG83tDrhMaleFDsRz2P8vtewYpP3RnRFmnFjt6aKMSn27_h18xzU02rEy4hpjpnNmjv2xQ46GpUHigGIGPs6QLgRGDy31Taw5KX_updYu8PanHCBRCWlzAjdZMMNVvPlejftb2moG5AEzESIziNYqqFGY1VvKOvkEEJ1rnkv8EIsE0AnvS_H4b6d4JwtJQqCXbD0H2awlMhohENJ3m3WpD1EPojno0rg0ATb5NhK805KbZfuB1CUGumadJAPr38Qao3Z_W9xe9PlX0VBuK32MkOn790kP7tXfydZSnLZWxOHlcmG67U2bn9t8BFFEUp76aIe6HkWTleREWmxLeY9RYh299SzvCukB1Wj8maskydyu7QjqqFOy5qxX4xiYWkLxq40hcRQbg6-2OaW3UU_swwfUX81hycv8YHfAAp3DQo6FPNPMKwOwbfL1cWPMPysTj5-H3-06JOYpkCG2lD7SNniPSR-Sq6Qb8aYT9qitsgGN6L-18lBmJulNS5usEtU-aSdPiQrkpnP45Lk-IzFlBoIq5nCEIYIHJA-SvVYDdA8TSbp_cRpEhDpGiu5-Bn3GKDmUQINIlT5duX7qrWfbTbu8Hs4r_LT-pSkITIDKrY7EDyzriCyF1UTcWKJYvnyCmcWhtCtoKQLoJg3N7N4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64161e2ff3.mp4?token=ex_0qyoqjMULN6IElbo-CBTzG83tDrhMaleFDsRz2P8vtewYpP3RnRFmnFjt6aKMSn27_h18xzU02rEy4hpjpnNmjv2xQ46GpUHigGIGPs6QLgRGDy31Taw5KX_updYu8PanHCBRCWlzAjdZMMNVvPlejftb2moG5AEzESIziNYqqFGY1VvKOvkEEJ1rnkv8EIsE0AnvS_H4b6d4JwtJQqCXbD0H2awlMhohENJ3m3WpD1EPojno0rg0ATb5NhK805KbZfuB1CUGumadJAPr38Qao3Z_W9xe9PlX0VBuK32MkOn790kP7tXfydZSnLZWxOHlcmG67U2bn9t8BFFEUp76aIe6HkWTleREWmxLeY9RYh299SzvCukB1Wj8maskydyu7QjqqFOy5qxX4xiYWkLxq40hcRQbg6-2OaW3UU_swwfUX81hycv8YHfAAp3DQo6FPNPMKwOwbfL1cWPMPysTj5-H3-06JOYpkCG2lD7SNniPSR-Sq6Qb8aYT9qitsgGN6L-18lBmJulNS5usEtU-aSdPiQrkpnP45Lk-IzFlBoIq5nCEIYIHJA-SvVYDdA8TSbp_cRpEhDpGiu5-Bn3GKDmUQINIlT5duX7qrWfbTbu8Hs4r_LT-pSkITIDKrY7EDyzriCyF1UTcWKJYvnyCmcWhtCtoKQLoJg3N7N4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضاییان مدافع راست تیم‌دعوتی امیر قلعه نویی: جرمی‌دوکو؟ من اصلا نمیشناسمش. کی هس؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23140" target="_blank">📅 22:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23139">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eba85793af.mp4?token=HcctzCGlL23ZSMROmM3xqkKki1JypaIWQ2BqezeIb9JmIVwZVVu2Yu5ka90PSgIjhqgojaIXsO77XdMRSVnMtwoukh7EmcWzxKc43AqwhaYsGwH7kRbIz3Qa_-QTrcpSwApoZswKu9z1C09xV1YNtAR1-r4zOTf_QWv6fZTXbXf4RNzYnvI5TnUbeGG6wU7o4YakyQRTo7in0v9tb0-j1O8i3Vuk-68nkFZQ8reW8k-J7MAQAjGSU4G-9eQTF-zyyxw3yf0kERuCV22ysH0s5qrid9US7v16S8tSV13GpYve1hbq4yTb4WiSoN-2Fww4UMfM8xYLHvK4ZDgzH8ZeKiTt42BqaWVWH_ZjMd_dJZ1QGPAUtI9GkWQOr3FTU3cr1VGEgKOs8efH78zH5mus7xhTJMjreb168Xq6rCip38Fl38JPxyusE5hK93qVL7gmxlQn6F2SZK8SO2zGXJfA6-SZk8zEtmN3eaIfVSzE41KQGHtbf_OFFLN5mUsp-C5X1RAWo57uO7qb_pgLKVPYJ-G8YzR87C0xqfI8Oal0xAbqC6u_C_D4rWErndbhwrcYbJxMRZfoYqOzxnXjsHyPuYcZgRaeOqh9uDbDitC7RsKzGFro2m3_7xL2GygTZmROe7HnsxeB-an3kfoSwWZbb-A5jVkplgZtmAXnVqe-ttg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eba85793af.mp4?token=HcctzCGlL23ZSMROmM3xqkKki1JypaIWQ2BqezeIb9JmIVwZVVu2Yu5ka90PSgIjhqgojaIXsO77XdMRSVnMtwoukh7EmcWzxKc43AqwhaYsGwH7kRbIz3Qa_-QTrcpSwApoZswKu9z1C09xV1YNtAR1-r4zOTf_QWv6fZTXbXf4RNzYnvI5TnUbeGG6wU7o4YakyQRTo7in0v9tb0-j1O8i3Vuk-68nkFZQ8reW8k-J7MAQAjGSU4G-9eQTF-zyyxw3yf0kERuCV22ysH0s5qrid9US7v16S8tSV13GpYve1hbq4yTb4WiSoN-2Fww4UMfM8xYLHvK4ZDgzH8ZeKiTt42BqaWVWH_ZjMd_dJZ1QGPAUtI9GkWQOr3FTU3cr1VGEgKOs8efH78zH5mus7xhTJMjreb168Xq6rCip38Fl38JPxyusE5hK93qVL7gmxlQn6F2SZK8SO2zGXJfA6-SZk8zEtmN3eaIfVSzE41KQGHtbf_OFFLN5mUsp-C5X1RAWo57uO7qb_pgLKVPYJ-G8YzR87C0xqfI8Oal0xAbqC6u_C_D4rWErndbhwrcYbJxMRZfoYqOzxnXjsHyPuYcZgRaeOqh9uDbDitC7RsKzGFro2m3_7xL2GygTZmROe7HnsxeB-an3kfoSwWZbb-A5jVkplgZtmAXnVqe-ttg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
در آستانه شروع رقابت‌های جام جهانی 2026؛ جواد خیابانی رسما از صداوسیما خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23139" target="_blank">📅 22:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23138">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vh6klbP26wlJHSgwbDmVdeeRyCw2oxoa6CxWufdDvKNr4GR1JsFI8pA1xI2I3wxr2TTNzIADf-EmeMRTzht6ZstBzPZEHNYZhg_i4H_RgreaMnvn0pI5DIzB8EOHHkqtm9osBFJl0ASyuDYCLnPN08HHJ9EN936SpmoO9DoYuRKxLgGt0vLO_NkfFcXkL0q1tPEhM8yblkmW2gljsw94JQdvk_oAFaU9IpAx3vbqJJRVtRMmU5E3Uqd8Nuq7nsccDqrYwBokk14R_0DVoboMYyQ9XiBmTuXVjw0sPv6S-a8fZpxaDXYGAnRlAZi83aL2xOsosUPGYuOgjeMhNJouLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ دیگر مجری ویژه مسابقات جام جهانی شبکه TRT SPOR؛ از هرجانگاه‌میکنید بکنید فقط از صداوسیما باحضوراون‌دومجری عنتر نبینید. از شبکه های خارجی‌ببینید از هر نظر واقعا فوق العاده هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23138" target="_blank">📅 22:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23137">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bc7bZ7XuLIz00A1TNi-cKX8OqDBc6RPBYf7BTLBdsMWBRhXcYToZ98lYOeFUWrokTZe-zIFMOyLUZXhsPpwKGCd9iMuD6kG1_xY7skB76ZE1yEGLqlqwjnQpA2DoC3V-6kQ0gExSbApmiDw7MN85tN2DMzgCqQDczR91UZR8zmYc2x1COzyXplpApnCeqjTgkTZdjglFqxlppY6MaJGHbuPrqEDCWm4jYnUqW-Z-JtsrVotaFSoZS830KEFuaMCcYzuN182W4_tR0v70ajbDLyVIPj3IMcTyKYGI6_aSiZ-rUQx8XAITdf63qC5SOSrFme-6racEW_i9KUOpeEZBQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23137" target="_blank">📅 21:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23136">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RF3VDeHeVNr2F-HEi0IVL7O8obshN-LTF2ebVMAVKbzfNvmcdLuTuOfMsoFUq2QwHd1RKtj9-wvekpJ1MBT_4t0dkkh8QnmYyEizmvT1obgnB8GaxBKFEPDOY75ZF20VNM6jaCRMPQDZAvz-bA2yahiD2SPMPzoAYVwRVWeXO-FoSXTi_O3lkOOygH-x9VcDwcomouF7UiZcF5IOU6_dajZ3iOn-teUHOOzKcL9tlXurKGm9d3CwHjauEquDZhH4F74x1L0A6i5X9o_ZaIwmHw7BfdDzfewWr850QSzfx9uDwR2xmSKTxYa5EBOH6DH9xXz4ogWfLfiHvXxsst4Bfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌اشتباه درطراحی نیست؛
پرچم لهستان روی پیراهن هائیتی؛درسال ۱۸۰۲ ناپلئون سربازان لهستانی رابرای سرکوب انقلاب هائیتی فرستاد، اما بسیاری از آن‌ها به جای جنگیدن، به انقلابیون هائیتی پیوستند و در راه‌ استقلال این کشور جنگیدند. پس‌از استقلال هائیتی در ۱۸۰۴ ژان ژاک‌دسالین به لهستانی‌ها تابعیت اعطا کرد. اکنون و بیش‌از ۲۰۰ سال بعد هائیتی با قرار دادن پرچم‌لهستان‌روی‌پیراهنش در جام جهانی ۲۰۲۶، یاد این دوستی تاریخی را زنده نگه می‌دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23136" target="_blank">📅 21:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23135">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giw4s_5iYPeOkVY1g1dbbXJ0ReUCxqaYL5DZ-x46GqlMAzPjm8Mz9tLa4_ooGWWlbtb87i7uGhQvT8OhelPrMsgwWXTVkbhfpAGv68wbjFmiK23qmumHFFpOleuvbTeQoRCJ8JNukJr2Wlia_RAcvmLgs0g9cXnP7Th95BhQm5u9GG_GGjnpMXK50XwlD66FUSFBT3O2FbLCI_D5hoar616sbzPwLnxQhygqh0uoaKcUJNgzAWTCuqo-arsx7roaVCaAO4EahF-vFCk0XhZYeX5tWSZlzfhE8X4_AmM7eqnZO1krcOqFWGYCWjn9JqxOnDb2LNDjERjDmxecaI6pTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از امشب‌اخبار داغ نقل‌وانتقالات باشگاه‌های لیگ برتر مخصوصا چهار باشگاه بزرگ ایران رو هر شب با جزئیات کامل و دقیق برسی خواهیم کرد.
👍
بارسانه‌مردمی‌پرشیاناهمراه‌باشید.قراره بترکونیم. اخبار جام‌جهانی رو هم زودتر از هر رسانه ای دیگر در سریع ترین زمان ممکنه اطلاع…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23135" target="_blank">📅 20:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23134">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/if2xgGEnIpHeci46UOVX7ZEL5YTl3xg-QV4kEk6JFt2wGKzLcXLEQqabK8G_AfBhMWIHF-Is77fmpTHRkE8YTZytDLiQDsYt1SeboEJx6vXtAMHmJkdjShazzd65YloW4-RhnxtoNIbayPtYLQ00Byg2xky5HDvigbSHO48Ab3Wh_h9cx-9FJ7NqLUhi4vRzhSJbG9tJ3A8Rx1meSs4eakSKhWVmU4AA_mFxaFAsUhEzLR0oZmv9o5BJMIStgkXymsaNV-QXVwDQwvDsSOuyncoYD8NmxRXq_huPTlGBejcFjKLA2sJZa3LxQenxPCOfKBnbmXFXv0eNhToZlKYMBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
مجریان ویژه برنامه مسابقات جام جهانی 2026 از شبکه معروف TRT SPOR؛ فرکانس شبکه رومیتونید ازماهواره ترکست پیدا کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23134" target="_blank">📅 20:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23133">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3FJvmdfkenqznQAOgkqp8UQblCJz6iKUK7f2q6Tna3pRChlYTTlxWZYMGK3iwQUJ2-s4JGE54c5Ia89L2NghXZstfR2ss0aa9oVJIvlGDpIX57xJWbf9--rsKtXCECgYvd0otpUrDNdayvVnIHWbJluRn5DLJgawgwjh6JFVNOfT6P7m8VajZWThtNSNwDCAnM8MJttkJxII5gy3FzFeGmt9UQwAA7uxi0aabnXpO9ugEd7DWt2BtVXvDMAfsSqffwTgOpcBWnw5tmfmCzrKfOK61_-TPSEjlUWCLe6lIvTptzZ8JCFd5u6RM83_0n3mdFmSu_A0d1QhbwAltTV0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال بزودی خبر تمدید قرارداد علیرضا کوشکی بمدت سه فصل دیگر رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23133" target="_blank">📅 20:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23131">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FrISlmvRmA05OE6RNMEUm1M83lXa2WHEdIWMd1MjN7SkFadO0aQBKrnTQzDOQMeLSE-AOvs3erIdcviRCGkBHUk1HTRzT9yjUrYK-s0nAA32Ft3U735H_rdqpEyj2DXxk218P41gQqRBnY_-4Gj04ST1xUTOmTkDw2BMkGWTSK5FoyMY3puRyVGcdlo1dYd0iXFLte7GFnhsm6yDOniKLD5cYLHxWi65Yuzyprz7jwqeIzFkm7_hDdcZyrzlVwR1MVWmGPf1HfYlaMDynhdMJXhijkCyZ9Mvba8S-QK486JykPbFZVaP-hVD0aNUgEj1mNTmLNXK0vZP8J6HOZSy-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pfv09XznU5WMXD3ylN43ONQuBFFsHwUJ-N0O6I0O7mxXsHrcAeSoHj5NJnWcXeG5vx3EXfnGcAasFMaB7EBSOkpg2ASyMF83rm60rR-JNGNmjQ0s0U-o5QOw3qbVShmuuG6FvfO4FUhe4lyfiRgh12baCBCnD9jZdOVD8l91l6YDC8AyoSUNA9J62An7570_eRgSAQvXO2fYX13pmExfpLKmNZoX6PZIQ4bXdcMqGn9KQgNZ6qMAYk7y1sAyLxCwK46KdGoesVUBRaXaGB0NYezYylJXLdknZrDI1PMbieOoIxFtaFvjOC4hmWxQqUnSHqeHSh4e4SoaMYlF3l02JA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
خبرخوش: تولد و بقای پنج توله یوزپلنگ در پناهگاه میاندشت‌. ‏«هلیا»، یوزپلنگ ماده‌ای است که در آخرین زایمان خود در پناهگاه حیات‌وحش میاندشت خراسان شمالی، پنج توله به دنیا آورد. طی یک سال گذشته، این مادر و توله‌هایش بارها توسط محیط‌بانان مشاهده شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23131" target="_blank">📅 20:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23130">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e58078f0d1.mp4?token=X3k0G6XA8UzmKTcqva_Y9wt9LR7TXOvx4f7nqz1rB0G3isHNcTltuENfk69tGBU3dVHl7t_xgT8gXrgkB4ugVzyIuWUZ43d_38iM-nkoydLcpkCFKqG-Wb-NdV-xOngA7Jag9Wlg96Qm15h79_te2CXYLox-IXK5Iiwh3EqoxPI8zDwWo20oCOuQZnL5vgzBjeNLy7X0y3gfDxvB52bK7Hnh882TlvU49CchK3iJDyu2bW5FeHglL74iEoz4_2vcRqkaHp9lU8MQzAbxmimw_vZHp8m-OOiWffVffl2y6GY-oTnbaiG5gyMezX0AFz-znjBk5qZGrvVJEmYLgv4adQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e58078f0d1.mp4?token=X3k0G6XA8UzmKTcqva_Y9wt9LR7TXOvx4f7nqz1rB0G3isHNcTltuENfk69tGBU3dVHl7t_xgT8gXrgkB4ugVzyIuWUZ43d_38iM-nkoydLcpkCFKqG-Wb-NdV-xOngA7Jag9Wlg96Qm15h79_te2CXYLox-IXK5Iiwh3EqoxPI8zDwWo20oCOuQZnL5vgzBjeNLy7X0y3gfDxvB52bK7Hnh882TlvU49CchK3iJDyu2bW5FeHglL74iEoz4_2vcRqkaHp9lU8MQzAbxmimw_vZHp8m-OOiWffVffl2y6GY-oTnbaiG5gyMezX0AFz-znjBk5qZGrvVJEmYLgv4adQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇦🇷
حس و حالی که از آهنگ‌های تیم قلعه‌نویی و بازیکنان منتبخش و تیم ملی آرژانتین میگیرم:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23130" target="_blank">📅 20:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23128">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMTaQGQOFzjdYFXtqpQ58Zg6MAlkoY-YOEReneC-ORHaonjyaF4i2CR1JOukfsy1UGSUVKAtn5n_lj7w17COpliYRTRz7U1bkbePbqOUhlYuJOC94Tfud3BHVteFsj9jHYHtvpJNd9jh6pXBLqOLie9tiPl_tPvBlJDFvhxwTNjRCRXW-lQuh6YuEqJz8Uk8eh2qdahRvpijZjzyZbuy3jtmoE5G9e9HeGeb-dUvB9tGPY1XxwDsB3g4YNiEGfvKldWJLmGx0A02Ng1acsfn7R0l8TAHpLkLbVPMgzF_KOBRyt2xM7H5v1vkMhrwRHC_qlIgyFiww8Attit3ZkNUOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
مارکو باکیچ هافبک سرخپوشان و نماینده‌اش این هفته‌حضوری بامدیریت‌باشگاه پرسپولیس جلسه خواهند داشت تا تکلیف نهایی ستاره مونته نگرویی برای‌فصل‌اینده رقابت های لیگ برتر مشخص شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23128" target="_blank">📅 19:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23127">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4htC_dY0NiZ_53ckziQnm9vkk4IESgT2SvgoHzzzeg4T2V3DL1F95IGEoEAtyGkkzWYsv9UV2pCKppE0BBcTXK7B3IFGymZrZj0zV7rOcYw33mBiSRzB5ncPfNMgeY5Bhuxo6VbOO1w0Y_Sbcv3ZoggsyqnFv_uAL7NN4l_gdcDFdiFLfRebny5jgKJCZbn3gm9b6WJeQiK3E4neUMFQnFPyYG_4RSWoq6t5LnPRkNhx_yP5TV_YuOkTfxRalAgAr08hWj7FV6FMSkYjLei7FkAU7MGNnfI6hJkKIDOJyhraVqbAB0qm3v93LsfOBfwaMcJvk0JewAG8jlOGmEjsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
#تکمیلی؛ خبرنگار موندو: داروین نونیز از طریق مدیرام الهلال آمادگی‌خود را برای پیوستن به بارسلونا اعلام کرده‌است. باشگاه الهلال اخیرا ستاره اروگوئه‌ای خود را به آبی‌اناری‌ها پیشنهاد داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23127" target="_blank">📅 18:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23126">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Orudj4pcc9Tg5qUxpmnn4TdwbOkq4u-32rEH_7w4f3xoBZ20dJtmWnolgYyXtctYwxXW77gcLTQccIrdCkj9w5sCFl4gfooiNEStPvrL2PubuvhavrpKnWULE3b_9vLAirKWtrPQgGgtwcOyrcZGh9q1JyKFPQ9QwI7gqdbna4mQYzfjSXhOylDKJ5zgEzWfrYme9qqaywIg1m06s1m57ujFpQzZuMlCdFKRVHdgI3aNzKyAqFvTdMb1GHEkqQbtKl1pyRMYMdwXqHj9IctVeNAFW1z6Ky7cS_GCE-Wmt21FHidF-TCmQ1vjkQ4rxFXMBICb_SPOMjvGgNffBMrOzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
#تکمیلی؛ رئیس‌اتلتیکومادرید: هر باشگاهی خولیان آلوارز رو میخواهد باید 150 میلیون یورو به حساب باشگاه ما واریز کند. نماینده آلوارز به ما گفته که اولویت او پیوستن به باشگاه بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23126" target="_blank">📅 17:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23124">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J33ouY3DIja8hFJ4IJxlvuEJkluPxcaEGeRQl9co5FckE_XAffFbVBPCR98UtwXiOs0m9F5lMBonNuhPPjsZOG2vMU3AT7fS5i3wOgpsrKe1sxUSyKBTbD8CmMy29CdivbLmqCnuxEGbEpyEUS5a5xXVGfTgsKbhypa7WbmsuBlkPysq5XA4uF1qT2Uwgl4YfLJufmX9vfQKTJcKer1N25icDdczYfWNYqu_GNtriq8s_kz-vH8GpydtQpvc26ogp4F0-HrOR-y7Y7vTD35MvGYPwbJ66kMlHk3FFYhL_p05K3rq_-7zLlKFdI2QjWvivZKzDEyq3FuZUvPgcRlYRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U8Y7SbQjTVMU38UXcfcHbwlGoDtoMtkTmvJt1mF_-MGgJEOCAD0aZj3J_vBknARYh_k7RqkOKYjAewlPtj8d2QOOqAb9tzsAjUXqCat-IF7vqKd7Y19XVXUFzmCpW0sRTBt6sQZjM3tG6n1yUJQbrsMktFL5y2SkES40RfNCBRy-Qg0-CtC9ptpVB34NeafMX6zZS4ug8od8DtbRti_GjRgSomY5hipVdF2kCT2iYmlxSsk4J8ZNKTw8q0T4MHhTmddcL7HCb6yBvm8-yddgz0RJTDP0qhOEGE3A6Gm0scWvFLzO7x_GKwIyik_KnBxFKvMGwEICP2HYOrPICygonw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
🇦🇷
درشب‌پیروزی 3بر0 آرژانتین برابر ایسلند در دیداری دوستانه؛ لیونل مسی کاپیتان آلبی سلسته به این شکل موفق به گلزنی در این مسابقه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23124" target="_blank">📅 16:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23123">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZv2WNr2XWc3Y9xtNytVtL_wtZJwED3MOfwsA1Bb1VljX0v_ncKTwGllPnUeNhtNy9dObRcVSHdX1GzzuqtAOA2vClRWpQkG0ivyf8-xkqwwZiNWg-yBEFv7GckbPhULdV35LPv94xNE7MJ_pLnxCBFlhyWcr8K5ZZUZPuXJ6VlhRtnZBKd3pXKYZ_nGpI9pmaI16PchMHyycY4En0oe3jZSoYtU1jfawQYd1ph83KBLNlw0ui0q6-3N1sVYjCgwGXIDswihFw-7rLS8Lz2cEEm2blBgJ3NfklVrCPnVpKWMW7jCeXSovCLtHjRZkniF2qzCPnlrOEtwzIddbrCWhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23123" target="_blank">📅 16:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23122">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
میراث‌ترسناک‌ضدحمله‌های منچستر که بعد از یه توپ‌گیری آغاز میشه بامربیگری کریک پس از سال‌ها که توسط سر الکس فرگوسن اجرا میشد برگشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23122" target="_blank">📅 16:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23120">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jP3YkhNOvIUTjXy5MdRIy73l5fKvzkxCrgD9c8gm3EKSXEkugJ8419R5ESTc3qy5rM1oQ-gfmtt868oKwf8zauaEo9bA-Y5fewtZUVUG2d4t2M_ZVmQx2V-g1gY4QgBzuBg5aF9M4USMypp5ptltYwGyQjLxkPcczHXqpFvuPStqBhJE5P8XstDB6zxdUOOUTXZ47Z0pQWZKrRd-XJ8xCEly_O0vpH9fqNPREgIB9m8fNbuGykvQjCqe3zEXj7rcPSWC1UUeibWKybN19xSU5EnzbCkWxkGHZHb-dooGAA9ElR5MO4T_SZ3U5fDGB2HtZAMxM_SDkcmfn5aTKuzuoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uYF1o6AZkDqP6RiSsokpzPo9QgJys2pvNMjz7EekSyUuPj7WFJQot826ifLur93iOEmcOG0cijhgXyIaSvF_r7HUVLdOttVZiRutz6GQI5aZ5hzbMxhb0f5EzB1jhrxOjdba_Ax6bd2DU-j1w6S_Xro0XJQkkMknOvhcTj0q2SIyMx-qjG3y8yDrilUDcd00zIHxURjdcINwbzKMhf0sKu0mSxrb6yEnoaK_iZSriaBs6S0HDbW6Yqgj_2TXwbNG_M30P8uhbdoOQ2kvpVjQ3PaiSsCT_IY6TNZekLne6jYJrgjl-QwoAiOwSDUyb_0hzr06rsLxNCI4js7-VbKR0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
مجریان ویژه برنامه مسابقات جام جهانی 2026 از شبکه معروف TRT SPOR؛ فرکانس شبکه رومیتونید ازماهواره ترکست پیدا کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23120" target="_blank">📅 15:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23119">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8Q7XM_VM8taJg4dHl9JBODh5oqb39Yh2GWyLdUHEsGmNOrMi0TewodZjFwTFtZic7TMh-cjTvB-xwiNa3cEIXs_k4SIbyUF6zS_4pYihAJq5jAbcJUXVOuMoPYQM5EnwUI_r3vWau60tdRRLjSOwgyBrarWb5dM1vu7PXuD6BpXQXvUOqHFlHZmf0vBAJomYl_Kt6-uPPmliiTeWYBcvInmXxIHNCsuU6IRd2lGZNy4QyCa0uHtGotJqRG6nOb0L_YsWbN32yW4yDGYJuhsjb_rtMIAlvnCzhqcYrHkVayI3NizXU-4-f-uMkCRx6gjeKVgzzLewbjGiMnb6fFpCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام نماینده مجلس؛ یوتیوب و واتساپ تا پایان هفته کامل رفع‌فیلتر خواهند شد. دیگ میمونه اینستاگرام، تلگرام و توییتر؛یعنی یه روزی در آینده نزدیک میرسه این سه تا هم رفع فیلتر بشن؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23119" target="_blank">📅 15:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23118">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dpJxU8AfrGU2Y9ll-eLxXfiMGkMWXc32sDNKLai4RPe--Mx4Qd9OveTTnoVGdVLiK_Y9CusZkw_b6HbdZLKrekW14mnKbWahXLDBhgDXTMTbKRu7WFUk0KQuHCYIxq8qH1c-TU_3uqizTmFzOl0wxIaQkBkHJH0lSYpxV9NwJjf7WoDVF_uLTMFTEg_vrUZsZRR7vaPpRkcpxjf1kiC9DA6VuBC4bCEJKRLIeefpsZLELJ-R6P8wsLFIAdynt9uAt1VT64wQtXN_Sqz5m8lylqLrFYpyVE0NrrlZif4AD-V8-zcynFn4RO9HnqxJNw30G3K5x6qSTRz3n5GIFbCoSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇩🇪
شهربرلین‌آلمان تازگی‌ها یه مکان برای شنا زده که خانوم‌ها در اون مکان حق پوشیدن سوتین ندارند! همونطوری که مردا سینه هاشون پیداست خانوما هم مجبورند بدون سوتین وارد اونجا بشن و شنا کنند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23118" target="_blank">📅 15:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23117">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhTEScHw52J3UDcNduDe1EHku7bpi9EchX0LQeK7zqx5tnO74b8yRH_lSAV55vpO3VJbkF-_vo4liyfBySxuQb59Afq6iKDOlfM15XlA1aSmo0L75KW7UDGvWD_mS6ybEDIL-JDPXMJRHblB_gD4SvvWQTmzatEbbaT6bwkAQbxrFRL06M6xqRktQJimCV20NRQTehNSf5GLIMPYM8uFgCceA_GfJdiYoLlOIjZARpLzqXFQjST6WUsa0Frtgstsp4OKs1e1kPD3Rmg9E9jXx-wnx-ki157ZMPHtOeKW5oli75YEh25lJFtXeHE1zFi5on6nLiwli8JoOz8c2288zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
🤩
#رسمی؛باشگاه‌اتلتیکومادرید در اقدامی عجیب پیشنهاد 150 میلیون‌یورویی رئال مادرید رو برای جذب خولیان آلوارز رو کرد و اعلام کرد مبلغ رضایت نامه این بازیکن 550 میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23117" target="_blank">📅 15:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23116">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vaNm5ywQZAIlmQh6PvIWZ6kAc2x73hwxDr3GqgzfhbSsJGea4G8oRgkWxWY2MB4h4AGzLOwOF21uphVi9kZRR7Kf_7AMghYMEk3fKekfdzWrH2VNAW2W122Ue6cvcZ8P7y3IL_3MPPvEYJbiQEYP59p8Cw2PMs8JCehRKsbuiv2se1NOanO3Qz40-RNBF9SpW-Ikk_ZZJE8FK-qRH2mxCNCxudadUlfyRfrL457gqEpclSPWZ6NigrGUdd7AvLkXDi1qf82DLiWM7A70NqRIrzGC249s7nDsFJaTU_4jACOahUWNOWF6uqVDTAW0DXkq5CteWYb9wmX9orEnb-8EHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ دیمارتزیو: ژوزه مورینیو سرمربی رئال مادرید از پرز خواسته از بین یوشکو گواردیول، ریکاردو کالافیوری و نیکو اشلوتربک‌آلمانی دومدافع رو برای فصل بعد به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23116" target="_blank">📅 14:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23115">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6Wz4FHzv4KXvKpe9raPGtc8B6U5aZWtcmFktK5OqQ-JyXZsSZb9BaoTz1awZRYh5eRUhv1-_cgTUk61pSZ4lh-P0qbQvXUCq0zxLX3bVi4_5zUZthGcrh9L4ucfZ7UKs7wRaYuwTSnlYJPE8ZyIfkxZQSrbUD51puox3uArPX6CUEmlFsL0j1e6Giavm_uJxdjJkcFsyvgm6maTTYGmZISdrSn3Tduaz_byq2Jg1J10R-8ir9PQD-A2Ntd6K55tsTNyWV5lo_sNISOKDmf2N8P5yn0yJ7TIZigbbNC6vmy7tn7L3X15kV5oodi8eBU2QiDmYAdJ2dBMf2PB2XFtfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23115" target="_blank">📅 14:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23114">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6BtBB0zRCDHc9XYuK_6QblZwMuazQWHIXE89LaTE39642QeSa15RTSf5GWMfzlHsQaEGs0TZDspVhCh6fhFCxZTryYdEpdXznw7Y_N-bCswmlgyp3HxFzpO-eH351qqLwk_O1oSF-w9d4z0_AzVsOiK0568cXuZVgt-3ZO5bbv0zF5lBc9mY1r8885zBvdxaN0BTK_8S5WhJhVIg0jgQ9BXsUe41HgaMiSF5Qa1Hug4ScsJ_iFfyqEivZZuFvCGuyXpHM1odnsRxfhdSTOtLrXCjmJz1GaB0yuNk5DA7xRApmV-5FqW71pbNzOud7_3dlFx-4Bp7WKQ4Xt0zl4Tiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ ایجنت محمد جواد حسین نژاد به باشگاه‌استقلال اعلام‌کرده‌مبلغ 1.5 الی 2 میلیون دلار برای رضایت‌نامه حسین‌نژاد کنار بگذارند. خودِ حسین نژاد موافقت خود را با عقد قرار داد سه ساله با آبی پوشان پایتخت در این تابستان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23114" target="_blank">📅 14:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23113">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b4b886447.mp4?token=Gpm8ZFYmuM68Gv_CThsuVbBZ3n14M5qSWLAma8Eyr08-HXkSIWoJ15GkU0OBWPEGh5NSNZQuM3C5pxjkGSpiOPgBsYNmEiPGp1ef04PD3m2i2C_m8Cfm3sE4cVGXWvoRaGSO1_3LBJ7Qs9TttuUP93YLBQkS_5RGEa2fKInNN2Dw6FyEaVQAu91uChH1790XmyMbnwv4jETUsMXa7z-WlnLlC_jgGiN-hjA9UI856lnYt9clyREy4BOFUXqgooDOaqOMEol692v_RipNhFnWpMuGo8vONT2tcva3KERBTj1UnEl8bsCxEHm3aONILdOEV0okPtyvIMeMRtkAL7pfXYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b4b886447.mp4?token=Gpm8ZFYmuM68Gv_CThsuVbBZ3n14M5qSWLAma8Eyr08-HXkSIWoJ15GkU0OBWPEGh5NSNZQuM3C5pxjkGSpiOPgBsYNmEiPGp1ef04PD3m2i2C_m8Cfm3sE4cVGXWvoRaGSO1_3LBJ7Qs9TttuUP93YLBQkS_5RGEa2fKInNN2Dw6FyEaVQAu91uChH1790XmyMbnwv4jETUsMXa7z-WlnLlC_jgGiN-hjA9UI856lnYt9clyREy4BOFUXqgooDOaqOMEol692v_RipNhFnWpMuGo8vONT2tcva3KERBTj1UnEl8bsCxEHm3aONILdOEV0okPtyvIMeMRtkAL7pfXYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اسپید یوتیوبر معروف رفته‌سرتمرین تیم برزیل؛ بهش میگن شوت بزن اگ گلش نکردی باید شنا بری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23113" target="_blank">📅 13:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23112">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzLi6Ccj_zOYVAlFBp7cdPXOvzsO-JESLsJaUF9qmnoNTpRbUJgHwIPzjnL4Xuzjvzov1Yp78wXQaY1JI5mwARS29WNA79dt1SYnRogQSob-U5GgLadXAnhYazPBYanofG3WsJv8VrNSB_Cgcin7TmUp_TumBjJqCzg1RrG-87Wj7aZVF72PRtxjTyICfQGUK_hoa2ijEqly1TWXlrZERq2LO6eq2cO8vyi5yQyF9rBUevY7f1vw-b9Yxo40DgYoyycdVBfAlA6yntTWr4ycGLMJnual7lV2smfDBVmqi8nAvvO0fhCy2V9oCVskKKf4GvgumkG3fG5Xa2zGhKjh0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23112" target="_blank">📅 13:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23111">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmyO_CZTX-zu82tg5PdGJrYAK5HHVqTX9SMC90Ucs1ErjLjfZb-nlhoksO5DyHzfUW_bMiyP-VM0ltnISbVfH7vDcVAkbDNIGBTpWl1nm5W5sfiqfSh5wgsm6LrTLP44RIcATeLAxFrGgvINyV25koQM8iMuc1EzAT9uP1Y44W6uwmuLZxDZA3he_uq3Ggom_Lxo6ZZOzDIq9pgZ28NlrgXgzRThbusQYVunrWH6MCmUgAnTOsMk_hie5GwiezqA4LSlyBRP5AlfmNPOTrTDlbiUFpGnqpXb9jJjP4amGch9V5zPb28EM2GC_ujfbrjlPNF4LtUE6WM-JgeUCAVA4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|بارسا آمادس که ۱۳ میلیون یورو بابت فعال کردن بند فسخ قرار داد رشفورد به منچستریونایتد پرداخت‌کنه اما شیاطین سرخ مبلغ ۲۲ میلیون یورو برای فروش رشفورد میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23111" target="_blank">📅 13:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23110">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9f0297d3.mp4?token=lyrfI5Q5PlFJm29ZH3MLr8Ew9gVQI0X7KLsBa0t0HqA0f9aLWH1KiJz0vXSSaMtz_NjfBWMSxKhs_mxCEDD-VsSPuGNpx_2XoXa_vBFYZQp51cgJEcDQegDK6xoNihGUgKb79gTRhLCfoj1d-kT5fE5MzBPuW297sSKi18e8UoCPTWyfFLZILs_ZUshukEC08T4KuL6ZjnI6VPJbp6Y4TvxnUmKGOABrzHcTk5tKnRlGSWJ2EaKhYGO8_WqNUgsYLNAfo54GOOUoERmmcOO2oCTwDH0PU0qt8yt-bGBK2vtKDe56VQJszMDLrAb3am43-wS3rpsqqpShww82kV63gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9f0297d3.mp4?token=lyrfI5Q5PlFJm29ZH3MLr8Ew9gVQI0X7KLsBa0t0HqA0f9aLWH1KiJz0vXSSaMtz_NjfBWMSxKhs_mxCEDD-VsSPuGNpx_2XoXa_vBFYZQp51cgJEcDQegDK6xoNihGUgKb79gTRhLCfoj1d-kT5fE5MzBPuW297sSKi18e8UoCPTWyfFLZILs_ZUshukEC08T4KuL6ZjnI6VPJbp6Y4TvxnUmKGOABrzHcTk5tKnRlGSWJ2EaKhYGO8_WqNUgsYLNAfo54GOOUoERmmcOO2oCTwDH0PU0qt8yt-bGBK2vtKDe56VQJszMDLrAb3am43-wS3rpsqqpShww82kV63gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضابیرانوند گلرتیم‌قلعه‌نویی‌وقتی میبینه باید مقابل دوکو،دیبروین،صلاح و مرموش کلین‌شیت کنه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23110" target="_blank">📅 13:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23109">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuvvsD686UgX9O2T8efaqXcqIRvQ3YPUUWw-Lm-5eSp_J6DYI08jvQGZ5YXPMXvm20Cih-l0F8XQ4zm1imtQfvV0Blwvs-gd2zgvwIciKg74gwe2kEALLRwsF-Ch2MMl5_59QOqYljlV9hdd4XdsoODTXmL4mQVcE-8RzCcduJPvzJWh6zrmymRVmebG767H2VK5d0NLh6MLAu-VHRNOjt29E11zTQtah6gYWIAW3C1lOAxvxjDLJIXa35yc0EIpM-INBcE5mHl44jyWUx2mMPImFZqvmt0RAtm7wQty7mg3S7M8-gJBjOj4lQ6kEbcJiU6Nk2KWjbvISaOd5s4JiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
دیمارتزیو: باشگاه رئال‌مادریدمذاکرات خود رابا باشگاه آرسنال برای‌جذب ریکاردو کالافیوری آغاز کرده. کالافیوری خودش برای عقد قرار دادی 5 ساله با کهکشانی ها با پرز به توافق نهایی رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23109" target="_blank">📅 13:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23106">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOl4u4lZw2QILv0yACRYimzxvkPYqLGrs8ME8JaX58_NJKAoBn4-YMgJsP285MBg2c-kdyPMnGJfx8l9_-DHJ6dngHpSaMvsq0Dqam0zt5J6ovcrhsr7ohkchZeL0thbni6bMaymtgHMzBcDndl7mMkTxY2By02eoQiAvCsmpjzhhM6mlf_SN6c_gP5NMJlKlTkaHQ7y7OvcvXBjKhUYJNZv8Omk9BbnnSXda29GJA07ViXKTbLLQysJnVHr06U6BDrd-BxxKiQmFvrRm_whi0mlS_DhYGMQd-_Trc4vozbjSgBGszeDmS-LmnBNcNYx-fDEkgXyaXAgaeGrrxURAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرداشب و پس‌فرداشب‌ازلیست دقیق ورودی و خروجی‌هردوباشگاه‌پرسپولیس و استقلال رونمایی خواهیم کرد. اینکه‌این‌مدت کامل همه چی رو نگفتیم بخاطر این‌بودکه ویو کانال برگرده بروال طبق و همه رفقا آنلاین شن. فرداشب از لیست باشگاه پرسپولیس رونمایی میکنیم. پس‌فرداشب‌هم‌بازیکنانی‌که…</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23106" target="_blank">📅 12:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23105">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKxp7WK0rpGAFhLuRYaFvvvtSDKTBBrG6mZ0FY4aX4UwwcWrzz7VPoo5Sb6jyUwGg_Wb0NPLUJwLJoEW5PoQzGQSQo2bZaeHZHVufMNd2MS59tjeYjbo3NmfQPsuDZdt9XHlkVR-6aUOu6TznJ7EmNTkaWqrGWV5dxe48gxGtFQpbMKSDoZvsWff8pNSxyCtWM9SCy1EOFFPkWDUwEH2s8JnKdfuC3NFjrm9lIW5-mKTxA_8Dzd0yqzrNRBOfKa4YVhGEsJDCfXHLxK4JtcKIChWRGGdPnq61W0MkwGQvkwh65BepLP9UfmTYE62x0UWUcN0VMfP8jAIDU2aMX4Llg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23105" target="_blank">📅 12:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23103">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nkv8U0oJCN5VoVdbdYXNtSF3RQDQ-Lf3mGXw5vmeIQD6si2hR27HgrAI0zUhbFX40q9vYoFfPq2fPZF4VFzZe7DH7ws0cIBPPEdt2HmAWhgivXfErSnV5jsQl2rJKSOoUU2oQ2oWWEVrCMrzU_JWG8IucgE1psitSv7_Rq1Sp0UGctpsmZaC0TGf0NsQIr5hCwGTGYFNm4HN7u9e3t5afA41vbnPVWbH2fCvu78KrOfcg3DUhVFFNfH8avM3PsX872T2I5h2VkdyS4Iki0-dBpTTklBmATox8RDGed0h14KSYtz_dMWXp1GtoiBwfbyU2g2HeBeypRHna33Lmd8rJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UTAHEnwj938Ve5pHt7I9IEP9QOkDtXJZA4Jj1cFpjlLw27g-xIBgoARvoq8_UIKbzg0IYAat5zWywq0iwlpXv1vZJUJq3Gq0AjPBjz0g2kCS3g0qlQAS0GRjrIxcx-l4TjPMthwGQc3q8XSIaO71ip9H446T5mKaJaSx1htn7qFguO7R86snR-B5xdUQgTWYghGSf8wDxRoD54DnDdlLtPbne1n_MVEyCvNu5qAwCaitvcoDchGjY2TNm0qhEGmnbbC-ACxwbYT93DYi5Ne6kzM9v2v2Fhp3BlwGswShj1u7QsalroFHmnJO-IcrCpDEAoiTJVSpBbzNBXrrU25WQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23103" target="_blank">📅 11:49 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

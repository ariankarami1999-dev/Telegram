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
<img src="https://cdn4.telesco.pe/file/ZXgNxLRwGeFgrDEcxLYBwncoRleNzzsGzS8a6uz6ogWlj1d4lmtFsDXOqTiNH5_ohJqZIP6j5NfKEaU4s2RlIUy-F0rbA3C5_WR4OZ2oS-jMQLUXpXufhKVtdK9eR_M-9BlOIA419_nKHySppgwFZoe1kr7MDmGp_DP0LWTxAQe2sdBbD3lnrvfxLOwYXfLqWqY6q0PqcWLpn6hqwItlWNEqfa0NJNCHOs-9A4ZDvJmVasBlSKxv3LdpHawF-cwQsu9j_ErKIHRl4D87sPAIZ9_xrFOJjf_T6EUsyxX3l58GQUmy6gIfFmhuZ0vS1DOm6sjppqDJfOG83Y70s1OtbA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 124K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 14:04:32</div>
<hr>

<div class="tg-post" id="msg-90276">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThkrgbjTwkYQEtBcqiAFVgbEFaWw7cUSmcXx5mkwCApxPaYIVXSvaIxHbkc7eq8FYac-hx7ylIFIyy_HhIXg7G8zWssaj8PD0UoaUpVH8aMA5tpHCViWSaScElCiYRnNcOjExQZ8xFunVJHd94M4hpxKA5r9HpDb3iCuR6LJxgBirHiOYZqRCX0-RLvqHbv72nQipQT4i1qcvFQ_wXOr9Fu-Z0rbDL5KLTeGfczElyZ2BXhNEh_RTgWcLi299ysYengs5gNZeWQc1sW3kT6UO23yXbumiim8r6cBdBj0H2yiN92I0N8d0Bi7DMXzvGSqFAvJjDE1XjEp7kBn6Ex94w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین باری که باشگاه بارسلونا ۸ بازیکن در تیم‌ملی اسپانیا داشت، این کشور قهرمان جام‌جهانی شد و حالا پس از گذشت ۱۶ سال بار دیگر ممکن است تاریخ تکرار شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/Futball180TV/90276" target="_blank">📅 13:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90275">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=QY_2vAYOKxGmLv-qZPRSgj_nPsoNCc-SG5FNlOvwTN1FxNvs-Y2P31NUEyBx59VTUU5oCzw0r87BraHD_YJp4xs-HbzRFmVqilCEBysLZgL1gx6UDaksQTRVa6Rt67jq9fTqIDhSZl_kOhE0_JMsrQKuMgdaP_3wmwraEvZrDUsPrLiWLOLV80PZuxGHHoim7jP3szUO7B0HhreU5x54YpDPzHPQg2M_PnHCDtbtcw5W0FPbZ_JB-IcKYnAHq-mSNZDvcITZqhPP_-QQ21NFFpWl3exVGZEZ4R5cpg7AnMEJcN7OdzdqS0j9jDY8Wv3ZvbknCJ9UgHtbCzLkOtLinQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=QY_2vAYOKxGmLv-qZPRSgj_nPsoNCc-SG5FNlOvwTN1FxNvs-Y2P31NUEyBx59VTUU5oCzw0r87BraHD_YJp4xs-HbzRFmVqilCEBysLZgL1gx6UDaksQTRVa6Rt67jq9fTqIDhSZl_kOhE0_JMsrQKuMgdaP_3wmwraEvZrDUsPrLiWLOLV80PZuxGHHoim7jP3szUO7B0HhreU5x54YpDPzHPQg2M_PnHCDtbtcw5W0FPbZ_JB-IcKYnAHq-mSNZDvcITZqhPP_-QQ21NFFpWl3exVGZEZ4R5cpg7AnMEJcN7OdzdqS0j9jDY8Wv3ZvbknCJ9UgHtbCzLkOtLinQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از عجایب فوتبال بانوان در آمریکا؛ بازیکنی باردار درحال انجام بازی🫪
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/Futball180TV/90275" target="_blank">📅 13:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90274">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMolkyy4GZIjfMPJIci9P6Q9LZ1tJiiLuknNWO4jIjL-GbXhe9OjvSD-jc9gXbE3wBWJJP-_MJJa_0FafozdAloCl79QQtpnKtRbA5VwQWPDaeeeYNV90jPQxohp-fWSFwKpC9qWliCwDWD8Fay6BEojOzNvoDCJOWDhNq4Wgf_F6lpwJqVta3P6q8bJEV7rtaVeV2GCvQx0OdWwnxLuBypzR0m2aqI_FyEofsgtSkuo-xBY0ga5oIN723ExHt6QkaMsTnbjGR404PovKm5ZCVFUOOr4ghVSMopETtc5-yrbxCdd2OLlx6iVGy8AWwhGpfmsNqWrMxlkgAi9o7e1fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
متئو مورتو:
مذاکرات بین بارسلونا و نیوکاسل برای جذب آنتونی گوردون در حال انجام است. با وجود علاقه باشگاه‌های لیگ برتری و بایرن مونیخ، گوردون اولویت خود را به بارسا داده است. نیوکاسل برای جدایی او آماده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/Futball180TV/90274" target="_blank">📅 13:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90273">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rL2VHTcMfywk8L202XFA9ptpGQ9uPVhylLDsXgukp4HDV01_f6QztiR07l22KvWt6JoFrrGFHcFUVOtKB71NUw-shm0dEWVVzcKsc1rQRJjw4xsFwbe-lRghyJm1oI7x7g6FwZEPUv92eRCZw_LrHAGJycQtavPvS9hp8gB_Hnqjuwp1q-SJfEsNMYZZaT_4-JWy1_d36Ye4Xt1tafuXZzT2CPb258Pl-Moz95QGX-CK4csgOi_RhbTNIPsALyWWlznyYFkueUzfgX-nStWimnmeiKybWApClUcTlb2y4QfD36RZ58Dx83KEAzLo31ew4p8Qpt-RB2SzW00QNVUwIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین گلزنان فصول اخیر لیگ‌قهرمانان اروپا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/Futball180TV/90273" target="_blank">📅 12:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90272">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا #وینرو  بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io…</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/Futball180TV/90272" target="_blank">📅 12:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90269">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejZt9fe6UkoXe0Kamvw7y8LJCXY4jwHTYZXiuJ_2yZP5I3IczxHObl-QKQS7OzlDnc-EgT2jVVZKjwkuOzFzvRzL1byAyNd76UV9BYJQJb0rAa4Uc5Y8rCqQYHlDwYbXoAQCMsCvMg2JXanfeCrDfpbmL7AZPXZ8lW35t_W5nt5hoyWsRBKcFvCuZGe-KArGBd9MZZoJRfSoUNNVgJ6-btYdDKVVSyKQr9wDD2GnDJRzF5o8URgpRKKu0qCUD4HShxtlSvkjlqh2rAUGT91R6GdGKJLeMnkJfWosHYm1eZzee2GYxwy-qeivX8uPeoKTEJWX50JOxl-69mX2E2WXOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا
#وینرو
بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r6
📱
@winro_io</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/Futball180TV/90269" target="_blank">📅 12:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90268">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cf55f690d.mp4?token=mrWYiTgoDaY72J9di8zZkvULMffgWX3EPKobFxXZJ9SI0m4E3cKuxk42Kf838dPLVbEM9oM0F8VMudqgHrjumHIsXrA5-G2FRF9PPIsNt6JNMfXeGePPhL8_JmokmSRPcOc-oWzKPEQWHZhHdN-q-MTMKh1eF8HnKibLUPOXrnrFslEpk4v08XgE6lP1inIAo0akKUq0cKXYzcFybnTu56hXuBsykd9WfWMea6zA9eaPNdKS8x6GNP4Ns9nyKtVX0_Bnwvjm7_d1gd5d9BRJG5JLnK0IUaatN92pgBtw9ukwoTkMtaC_y7xwCpaB8VmfzyBRzdMwqP49YK8KD0Yl3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cf55f690d.mp4?token=mrWYiTgoDaY72J9di8zZkvULMffgWX3EPKobFxXZJ9SI0m4E3cKuxk42Kf838dPLVbEM9oM0F8VMudqgHrjumHIsXrA5-G2FRF9PPIsNt6JNMfXeGePPhL8_JmokmSRPcOc-oWzKPEQWHZhHdN-q-MTMKh1eF8HnKibLUPOXrnrFslEpk4v08XgE6lP1inIAo0akKUq0cKXYzcFybnTu56hXuBsykd9WfWMea6zA9eaPNdKS8x6GNP4Ns9nyKtVX0_Bnwvjm7_d1gd5d9BRJG5JLnK0IUaatN92pgBtw9ukwoTkMtaC_y7xwCpaB8VmfzyBRzdMwqP49YK8KD0Yl3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهارات تند نیکبخت واحدی: افشین قطبی کاره‌ای نبود. چرا در تیم ملی نتیجه نگرفت؟ قطبی ذات قشنگی نداشت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/Futball180TV/90268" target="_blank">📅 12:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90267">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98d2b87299.mp4?token=S8QvqawS2cO6n-_SDB_yzUmn6AEPON28vKCocAlz79L1O6J-28D4wT4lpzhRzirAMd5u-BuoAJQqL8luwXfpLohKhZpVceQcr-C8oVyjb3Jac4Evwz0daYsfnJhor3okzB4r9f06cCiYkbrwEKsD_Wd1xjfPd0XrLD-lsIsl9qey_LmRa4Q32pyCnJ-wRPoVImnLK2-Yo85fJlV5ZI_YEV8FiDIaYO1dYUtWSZniz2HnR8Tz9xoAwdH_JCXvp4Nz5X0hcT9ql7xEAHPQYDWtdShvpijaKwVFdqaA1xlFYws-40sTbk0x5WTdfCUPiIwLWccdLQ9L0nOhBacsytswAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98d2b87299.mp4?token=S8QvqawS2cO6n-_SDB_yzUmn6AEPON28vKCocAlz79L1O6J-28D4wT4lpzhRzirAMd5u-BuoAJQqL8luwXfpLohKhZpVceQcr-C8oVyjb3Jac4Evwz0daYsfnJhor3okzB4r9f06cCiYkbrwEKsD_Wd1xjfPd0XrLD-lsIsl9qey_LmRa4Q32pyCnJ-wRPoVImnLK2-Yo85fJlV5ZI_YEV8FiDIaYO1dYUtWSZniz2HnR8Tz9xoAwdH_JCXvp4Nz5X0hcT9ql7xEAHPQYDWtdShvpijaKwVFdqaA1xlFYws-40sTbk0x5WTdfCUPiIwLWccdLQ9L0nOhBacsytswAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اسپویلِ بازی آرسنال و پی اس جی.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/Futball180TV/90267" target="_blank">📅 12:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90266">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99be172cd9.mp4?token=sm1bEC9RENAiixs2J0u_9GtXdOcgb6-QbG276IijDwFFlzzcOStJwDOke-SEDW-_IRDsI1elhXDUk498C8VR65GNVzLkVtcEiGa3UtD6NqP_fwSZF8vkT8F5iVHsQ_7AVIg6dcvpFUJLOsrHEIi49AKLElctYFi5_0zWzF5LV2DPKlhx4Xr87HjpToWhTI1jiPo5f3_lFnLvKyhtnajEzpIXCg_JeAiUPrQWksfh5SkaSGtWj9s_-6CVDBv7WUY_eNboCZ84GXOyccw6fDm01t6Pnlno9qxncXQfel9P5dAwqQS3Yj97czsi8YAWu41YyIBRpAPkXY7btm-90-Ql6gUKBYPzHV_Y1fwFhy9ktEXQukn5Yr7q04xwYOC9pMS83jvg32rTy6NoEuhTJ05QLRWfdu_r4y569RJ6CGIwQOupslSXD284n-PnvzLTfXILvXiY5i7xDIgehL5FS-2sFmCmM55cJNFDvWHKVmnWKC5KcA4uChuPErv1qT_VZlv33CmtjIEC5R0_qBe9Yta7mBgegrSnynbcfSJSVWbkVOjdBBfMxG20DYwuqv1spEQXRIQ3NZwWWhx4AWM3wE-tIXwCkmVZKpBC_TMmHcqPzikbSXKD1HC1FuhVWWfMISUxbxP9eQLrLM7M06GZo4AlWohrwUXH1mU5rARcHZ3pLNU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99be172cd9.mp4?token=sm1bEC9RENAiixs2J0u_9GtXdOcgb6-QbG276IijDwFFlzzcOStJwDOke-SEDW-_IRDsI1elhXDUk498C8VR65GNVzLkVtcEiGa3UtD6NqP_fwSZF8vkT8F5iVHsQ_7AVIg6dcvpFUJLOsrHEIi49AKLElctYFi5_0zWzF5LV2DPKlhx4Xr87HjpToWhTI1jiPo5f3_lFnLvKyhtnajEzpIXCg_JeAiUPrQWksfh5SkaSGtWj9s_-6CVDBv7WUY_eNboCZ84GXOyccw6fDm01t6Pnlno9qxncXQfel9P5dAwqQS3Yj97czsi8YAWu41YyIBRpAPkXY7btm-90-Ql6gUKBYPzHV_Y1fwFhy9ktEXQukn5Yr7q04xwYOC9pMS83jvg32rTy6NoEuhTJ05QLRWfdu_r4y569RJ6CGIwQOupslSXD284n-PnvzLTfXILvXiY5i7xDIgehL5FS-2sFmCmM55cJNFDvWHKVmnWKC5KcA4uChuPErv1qT_VZlv33CmtjIEC5R0_qBe9Yta7mBgegrSnynbcfSJSVWbkVOjdBBfMxG20DYwuqv1spEQXRIQ3NZwWWhx4AWM3wE-tIXwCkmVZKpBC_TMmHcqPzikbSXKD1HC1FuhVWWfMISUxbxP9eQLrLM7M06GZo4AlWohrwUXH1mU5rARcHZ3pLNU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاسخ شفاف سهراب بختیاری‌زاده سرمربی استقلال به پرسپولیسی‌ها: فاسد نیستم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/Futball180TV/90266" target="_blank">📅 11:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90265">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNDnq0wzrNdDzTYnBlLOoMvXLbMGTsUhKckiepBlnS5Ja_tiV22vy-xtKvxN_kd3MGwu2hgSgdmCCaA4jddlmWSdQw2Kj6IuFnPwwYU8m3drYZMRiyXDdSb2cC5ntsrIhMZ4TjqXpSpsXMBiLjxBKU-qZE-Q8mXpvsy1g3jL8yv0vOHCg2WL_8DiX9QFn1KWIus1230qFc8scyJ1d3UtP-7Nnp2y9dyRY0cB7lnSMx653yu7TdrrPLZ3af6H8RlZQ7FLSMSh64IIQ29GHvydhF-dFM5WwP9SIGhwQKJCZNkd1GB18UetuColLSw51QXX_mq1QHSWPrSUX5xaQpkAdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
به گزارش رومانو، باشگاه بارسلونا بدنبال عقد قرارداد با آنتونی گوردون ستاره نیوکاسل است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/Futball180TV/90265" target="_blank">📅 11:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90264">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/426e74bc07.mp4?token=ot9F94mn8WicqtB02S7skhFNy_1cpUJnroCxlM6iW7gwPkklPS6GpjxAcF9jTfOMHkHZxQfB7MMCPu7bS2HN4yMNtOe55djHS3oDWhtaAuqrJ1241vxiMzNC5B93qw6hH-guhubXMI8I9Ak5NAUao0bVPohJ9vZr9oNgfM6_56BbH6nKCQ73r1BkgATK3uV_g2rJrn4hrxF8yZqer6NRIG836ITPqMed5rBdC6AbUUjvpabEpJUYMQerjNOkNX4tOtq0C99XkzFbyDhFih-jgtgB9dUmu6qqTSP4hJDVdLRzFVtkroDiMm6XQJP6hkTv4x5tWBGsrVcpNU3l_djtMCKfiM6Mj_s2MuLSH3mNebvIFtOI9Pm4gQiQE8SS6-rTtYTLUsfppu1Jg7dFnrFW-bQblD1jHQ9WbReeNSu94rH5XWdZPGvPPdGXJyQNxC8bkhNvImMKQw4RvT6DKoR9Y9ho0vXqdQOX4pohFGCWNA4R40IxKJ89OHYCHIgNoqjUS-Hox6JB9xfBSWYQtRkmOblk06oQvYGlhd14gL5Swat7_3bq6gPyGgO14G0G__WHyglr2CpCballuGABXpy3SH4tD7QEjKrW_ZIB7UKi4oqGgxNRWxLu0FkePS4HJYxj7Nlou2UqdrAV0E4Q1N9-VGqRibjrlYAT82inT-IuEwU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/426e74bc07.mp4?token=ot9F94mn8WicqtB02S7skhFNy_1cpUJnroCxlM6iW7gwPkklPS6GpjxAcF9jTfOMHkHZxQfB7MMCPu7bS2HN4yMNtOe55djHS3oDWhtaAuqrJ1241vxiMzNC5B93qw6hH-guhubXMI8I9Ak5NAUao0bVPohJ9vZr9oNgfM6_56BbH6nKCQ73r1BkgATK3uV_g2rJrn4hrxF8yZqer6NRIG836ITPqMed5rBdC6AbUUjvpabEpJUYMQerjNOkNX4tOtq0C99XkzFbyDhFih-jgtgB9dUmu6qqTSP4hJDVdLRzFVtkroDiMm6XQJP6hkTv4x5tWBGsrVcpNU3l_djtMCKfiM6Mj_s2MuLSH3mNebvIFtOI9Pm4gQiQE8SS6-rTtYTLUsfppu1Jg7dFnrFW-bQblD1jHQ9WbReeNSu94rH5XWdZPGvPPdGXJyQNxC8bkhNvImMKQw4RvT6DKoR9Y9ho0vXqdQOX4pohFGCWNA4R40IxKJ89OHYCHIgNoqjUS-Hox6JB9xfBSWYQtRkmOblk06oQvYGlhd14gL5Swat7_3bq6gPyGgO14G0G__WHyglr2CpCballuGABXpy3SH4tD7QEjKrW_ZIB7UKi4oqGgxNRWxLu0FkePS4HJYxj7Nlou2UqdrAV0E4Q1N9-VGqRibjrlYAT82inT-IuEwU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از اظهارات عجیب شیدا یوسفی بازیگر گمنام سینمای خانگی: در کارخانه پدرم، روی شمش‌های طلا راه می‌رفتم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/Futball180TV/90264" target="_blank">📅 11:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90263">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b5959b18a.mp4?token=f4ZHVnhw5oiJs1xJjMWWdgYxfZ1_kKgzaHnOE0dHQ9Rr3X9Sntw5MHTLdrRnPt7EdPazZ3Nz-GP8RezGkQ0_RM_k8W7634CkJSIrg1zZ2hN4kMN4HWRIQyo9sW3AiemGVnexeW9yOjsTDx7HVZr1R4P0S8pyOuAmEEtFaC3t1NLUhERU5Iz1kdvvVzaj1PyxT9mzpHhbfocVz-dHFF36niNK3zyYTB4Vg67bOriD6AnWFk1ndHA383k3i-YKwEs8XARwvda_Wx-DnIg-9TzMmbUHcDA0K9r2375273XxiLofHbcmbYNiaHMEdxvuuKQo21LCxhrF4aHRMlqB8DhaIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b5959b18a.mp4?token=f4ZHVnhw5oiJs1xJjMWWdgYxfZ1_kKgzaHnOE0dHQ9Rr3X9Sntw5MHTLdrRnPt7EdPazZ3Nz-GP8RezGkQ0_RM_k8W7634CkJSIrg1zZ2hN4kMN4HWRIQyo9sW3AiemGVnexeW9yOjsTDx7HVZr1R4P0S8pyOuAmEEtFaC3t1NLUhERU5Iz1kdvvVzaj1PyxT9mzpHhbfocVz-dHFF36niNK3zyYTB4Vg67bOriD6AnWFk1ndHA383k3i-YKwEs8XARwvda_Wx-DnIg-9TzMmbUHcDA0K9r2375273XxiLofHbcmbYNiaHMEdxvuuKQo21LCxhrF4aHRMlqB8DhaIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی صحبت از مهارت و دقت میشه
🔥
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/Futball180TV/90263" target="_blank">📅 10:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90262">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWhhTmfl5omiq0MChMEiRKuSHvzGI9LLv7cRCbWNaYKmfnViRg3GoOYyhRJ4tx0Pnm5xfU_Psxfmq5Y41nBQoAWu4avgMYhew5x3HWZUhtcmWofkQ2flRnU-2StjoDQvAKmXcx_oT69Yv0N2cKlur6NVh4L8Rb5cdw0PU5mvIemxw058xmSbhzqQ8Au-uCr_ib9MM_VtbMA-mBt4cIte_iYC2ejpj3BqPFztKp9mBYt2TGM2mEmcbR_qRsQ6fU0Bobn0xP4eVl7TDQQzjELWhscJuI7pi_rbjRiIqrmsMIZin1aYFXjKqnDFhujgH5868TkoRWjjVcLNF9oRtrtCcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ترکیب اصلی رئال‌مادرید در فصل گذشته هیچ بازیکنی از اسپانیا فیکس نبود و بنظر عدم حضور بازیکنی از این تیم در تیم‌ملی اسپانیا برخلاف بارسلونا طبیعی است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/Futball180TV/90262" target="_blank">📅 10:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90261">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d64b58d74.mp4?token=eKcavSO-R9I4VQjH7Gks-yOmiNR1EvkfYp6KqWHHO5V4beVHxtyml5OsDgPhbelLhms7ySWQK0anBuieQiGV_USZ7taD-1-vJ96kfT7m6dgdcfLUL_euSsU0VfMynCNKHUDKjsHa9yJMPzJ8lMTp1lqc09CuMAaMUPdEXU2JHdMpSMRGOnyhbemMwKOJZyv7ER-KojkO32QruXHUlLE9ittdjtBk703UvVKloNXzxTfh8c2kUM_Prc365-U2Y29TnVC96sTV69WbVjLLmzdpRhX1EU3mllOeo1Afj5mzXuFPqhC9X8KRMm0yyIjq58wkxcBlbZUydaKYNxNzsndBSIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d64b58d74.mp4?token=eKcavSO-R9I4VQjH7Gks-yOmiNR1EvkfYp6KqWHHO5V4beVHxtyml5OsDgPhbelLhms7ySWQK0anBuieQiGV_USZ7taD-1-vJ96kfT7m6dgdcfLUL_euSsU0VfMynCNKHUDKjsHa9yJMPzJ8lMTp1lqc09CuMAaMUPdEXU2JHdMpSMRGOnyhbemMwKOJZyv7ER-KojkO32QruXHUlLE9ittdjtBk703UvVKloNXzxTfh8c2kUM_Prc365-U2Y29TnVC96sTV69WbVjLLmzdpRhX1EU3mllOeo1Afj5mzXuFPqhC9X8KRMm0yyIjq58wkxcBlbZUydaKYNxNzsndBSIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین گل‌های فعلی در سال ۲۰۲۶ فوتبال
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/Futball180TV/90261" target="_blank">📅 09:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90260">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26b4bc8543.mp4?token=nMc_Gikoq9ouO3MdhYKTjxHEbD8q5smHrHTSsfw7SLUQ20TZa7DWTPFdG3Tk95P2m10zKwdu43LnOcNHr-r14YzDjuEDfFxTe5L3rBzc4Od9R9cp3NjCHCxCsHX2MdggtH6AojdfmkRtFiSs87c3t5PI-q2DRGJvTZQOHjxDWe1Fwp7eNUQvUveVMGTHokScevakAAzD2bXH_k66jdv1NnwSFaT91wPT1TloAHAT4DrHHOstF1TvAo2SwTES92HKC90vzSeyeXIVEbo-UfhLTebvZSWvwyS_Z_91Hflc2WjW573b8fDTO8AQiMGqwDwqse9-NVIcuUWq6Vl2izx4Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26b4bc8543.mp4?token=nMc_Gikoq9ouO3MdhYKTjxHEbD8q5smHrHTSsfw7SLUQ20TZa7DWTPFdG3Tk95P2m10zKwdu43LnOcNHr-r14YzDjuEDfFxTe5L3rBzc4Od9R9cp3NjCHCxCsHX2MdggtH6AojdfmkRtFiSs87c3t5PI-q2DRGJvTZQOHjxDWe1Fwp7eNUQvUveVMGTHokScevakAAzD2bXH_k66jdv1NnwSFaT91wPT1TloAHAT4DrHHOstF1TvAo2SwTES92HKC90vzSeyeXIVEbo-UfhLTebvZSWvwyS_Z_91Hflc2WjW573b8fDTO8AQiMGqwDwqse9-NVIcuUWq6Vl2izx4Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحید قلیچ برا خودش عالمی داره
😂
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/Futball180TV/90260" target="_blank">📅 09:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90259">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4b0e0df75.mp4?token=gMtvYpWe9e3QL-V3ueMwbYkDNGBdpy_g-vrB6yMll7KPqLT6qCJSMREcXHJP1cjSk06RJ7B6zGi55V7I-S0y6pG663lcZEi64OPRl3tWUYZ54fdpybVBQDJGKh-nyuS84twf8jdDFT_X7xQtme_aOxEqtNuKCE_8XdHR7bX0dl3xrDx8DAL6w9PIULy100h4qTt2dP1nt56OZsDgdgHhIMXvefyABf9ztP_GnEhnMGvoHPPIxnMW8zzqZ6EsT71dOKo6SRCPFkRd79L4kRFmhcDTjP3nQRfQBaer4lbp9jIciZYv7WSD-jViqZG83Ab8_MqprDgd5_TXkNVw4I8u2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4b0e0df75.mp4?token=gMtvYpWe9e3QL-V3ueMwbYkDNGBdpy_g-vrB6yMll7KPqLT6qCJSMREcXHJP1cjSk06RJ7B6zGi55V7I-S0y6pG663lcZEi64OPRl3tWUYZ54fdpybVBQDJGKh-nyuS84twf8jdDFT_X7xQtme_aOxEqtNuKCE_8XdHR7bX0dl3xrDx8DAL6w9PIULy100h4qTt2dP1nt56OZsDgdgHhIMXvefyABf9ztP_GnEhnMGvoHPPIxnMW8zzqZ6EsT71dOKo6SRCPFkRd79L4kRFmhcDTjP3nQRfQBaer4lbp9jIciZYv7WSD-jViqZG83Ab8_MqprDgd5_TXkNVw4I8u2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
همسر ناصر حجازی: به او یک میلیون تومان پیشنهاد دادند تا گل بخورد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/Futball180TV/90259" target="_blank">📅 08:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90258">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">روایت قرارداد نجومی فرزاد آشوبی با راه‌آهن در ایام مالکیت بابک زنجانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/Futball180TV/90258" target="_blank">📅 08:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90257">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">Soren-VPN.apk</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/Futball180TV/90257" target="_blank">📅 01:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90256">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Soren-VPN.apk</div>
  <div class="tg-doc-extra">62.2 MB</div>
</div>
<a href="https://t.me/Futball180TV/90256" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔵
فیلترشکن سورن (اندروید)
• نسخه 2.1
برای اینترنت ملی و بین‌الملل، عملکرد خوبی داره.
وصل نشد، مجدداً برای اتصال تلاش کنید.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90256" target="_blank">📅 01:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90255">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otW_lbD7_zKRILGsNTJiDsO4xPkC9nMAGHL5kZTz8PX_j1potRSAp9r8zD950KViOYF0OCD_HXxYeLQX8gzuGEkDQbPCuSXeQwYBqYTOpcgaubvQKuBow37BGpsXlS5PVM7bRkwaZ5PSqkcQQBP2fInHgQ2opNf-YXTSvt47LjBIP5nHpDc14PNxa7cJyDDZnh09NqxB2-DSNYeGwu38JMz_jqkaIhrZGchK1Clc1KLQt22eMRLd1yBAWTE6IjBtuxkS0E_jerEqJGmgsJMzqRRR4XrdVT2j2os5cjECvBMasEcQXncUWY9f69PL8MIZTF_hdmPflCJwAchJ3VDAZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکل آرتتا بهترین سرمربی فصل لیگ‌برتر شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90255" target="_blank">📅 00:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90254">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔥
برترین گل‌های این فصل سوبوسلای در لیورپول
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/Futball180TV/90254" target="_blank">📅 00:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90253">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsjaYvtQcrNXuEXtUjP3r392s-b1I0c8pNv70lLZOQORh6soYezQXLs3GDtSRyW2amFxf7PkN6yOxlm0j8MnyaXa0-wlJNh0CxBdPuE332I9qVXKWYXxackOUfeiQmU9UwwFxDOm7MXH7j1Amm0VJoifIhZPjIfZEFMZ2zwLA816q_-Pio1VTq6wil3lgaSMVP8IIqmrY28d2iYLkxbijfRYm2N1v1-2xrCp--jbsvokOZhCNkmg9CIEqJVIDxVH37KNEKLTIOPoXwqookXPMZ26DmIS1lcIIgjtDy0zzFXPGMKb_7gi8xuDUq6zjVCGhepev0eBThFr72EmikXixQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الکسیا پوتیاس بعد از ۱۴ سال از بارسا جدا شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90253" target="_blank">📅 21:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90252">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea61c87680.mp4?token=oXP73a7yRfLXcqW90WVqm4UPDXJdkm6giFjsb46Tgy09fAztdRKDbvIGNsw6uF8k7Ws6zFsIMYkzWAwhqxwmkeWyPvknnBcA48I0KNz8LhHdqyONeAUFzz1cq-EvcXA_bifD-4HdbXQeisFYyA4iUIeNlvC9jHWurP1p4WvmH_wJLq277Fl17LmCTLES_cJRY7CIk4-7JqyN1rwyWjS1THN5ovPy1Km8lYKYua3C4WyEWwYAvbj53sdd94wcQ0OOih_YCZa-smf4YYBMHZyUkxsBPOywI8YL0Y5o_rmTNoQeUtVHE1VYXk7EZzbeqMi_A77NT5ok41WtL7YAd8MTdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea61c87680.mp4?token=oXP73a7yRfLXcqW90WVqm4UPDXJdkm6giFjsb46Tgy09fAztdRKDbvIGNsw6uF8k7Ws6zFsIMYkzWAwhqxwmkeWyPvknnBcA48I0KNz8LhHdqyONeAUFzz1cq-EvcXA_bifD-4HdbXQeisFYyA4iUIeNlvC9jHWurP1p4WvmH_wJLq277Fl17LmCTLES_cJRY7CIk4-7JqyN1rwyWjS1THN5ovPy1Km8lYKYua3C4WyEWwYAvbj53sdd94wcQ0OOih_YCZa-smf4YYBMHZyUkxsBPOywI8YL0Y5o_rmTNoQeUtVHE1VYXk7EZzbeqMi_A77NT5ok41WtL7YAd8MTdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش ناصر حجازی به پیشنهاد گرین کارت؛ آمریکایی ها باید به دستبوس ما بیایند!
همسر مرحوم حجازی: وقتی بهش پیشنهاد گرین کارت آمریکا رو دادم چنان فریادهایی میزد که ستون خونه می‌لرزید!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/Futball180TV/90252" target="_blank">📅 21:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90251">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90251" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/Futball180TV/90251" target="_blank">📅 21:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90250">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFHiFk-5QS-c0z-3t3otl7d6bVIPiWprqOgzenRHv72gIdxosxbiziDORJsKwdMdEGemTqPfUniTgw94CyNjY0kgX0PHdMHMWIt62WbHllPCvpVu41wTsDwk-fo08rem2xy4fN5SuhELaBgDPlooojwzVo13Qi8TH-mTuog0DN-QXFKmqcAwO-bIzjP6Pt6qAzcBVVMcDgTFkypV0z81eMpKrT7TxNG0IF-CBP-V5GksFi8Eg2ILL06hTSxbmcUGoBi2cBDYvjktL_UsU9Zuwt2RqAygBO5oCHhZ_DFl4211nScTy8uilkwG-QtJJU1xw70jfiTTa8GbqfcUacAQKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/Futball180TV/90250" target="_blank">📅 21:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90249">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baad93a3a8.mp4?token=f7fLfoLQsOl6ygnGNpIQidxjIjtiXpzUkz6lLUqWuC30kSAvLpUKl6PoQn1Xgq5H_P-oDLjKZaP8QwHfHOLNz8CsLV-hb5PLu6bn3r-CyqBmcHIECP07oZH_JrjJTLXCp6c2isn05HuOuYBkXe1gfrzfIEI8yxOllPcrMINsm4HykjObaU9mNUnjG4bZTpa3LMjl5MSw_EF3P0fp8B98VMfLeYDD3EaXlU0oZK78xk7wuZMSxRhcBRyaUILRzTF_Hs68N7nkpY1LemW0KabcswHaTJcyNcatFY07uhZJLTw84GultCgA2FJZDrvRQEjd3SwgUSQAtot3whA2nwX0_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baad93a3a8.mp4?token=f7fLfoLQsOl6ygnGNpIQidxjIjtiXpzUkz6lLUqWuC30kSAvLpUKl6PoQn1Xgq5H_P-oDLjKZaP8QwHfHOLNz8CsLV-hb5PLu6bn3r-CyqBmcHIECP07oZH_JrjJTLXCp6c2isn05HuOuYBkXe1gfrzfIEI8yxOllPcrMINsm4HykjObaU9mNUnjG4bZTpa3LMjl5MSw_EF3P0fp8B98VMfLeYDD3EaXlU0oZK78xk7wuZMSxRhcBRyaUILRzTF_Hs68N7nkpY1LemW0KabcswHaTJcyNcatFY07uhZJLTw84GultCgA2FJZDrvRQEjd3SwgUSQAtot3whA2nwX0_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ازبک‌ها آماده حضور در جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/Futball180TV/90249" target="_blank">📅 20:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90248">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yvp_bRKf5rSoZnkPqyyb_SLKn8SMPgWB2FONvjUNRu4mtwOJ0g4uhF6Oojv6h1Gp21gcmBkTcTu_CiosdFmPAOCBf0XdBj_lt1IcoEnzQvNDhN452hrFmOFPsrbcPSAI8FLQ3XvxqwEWpuLpQ2ifoBd1P8uNtiyX22b5Agzto1K3SnwrmwVFJMk8tqGageM59IoYjjLBwfo8PUIY2jQQNoMopfnL_CY5JA2YpOunD4BldiHaCAVcHEUKztjhctMmwqpThac4igOavQnQBaDW_WRQchwTRuCEe9w-7sV6vouVdQQbPWwDR2P7UcfGBO_zRS4RB8PUrZmLWRrc9s9yRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با اعلام رومانو، قرارداد آنتونی رودیگر با رئال‌مادرید یکسال دیگر تمدید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/Futball180TV/90248" target="_blank">📅 20:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90247">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🔺
دسترسی به ChatGPT روی خطوط همراه اول و ایرانسل برقرار شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/Futball180TV/90247" target="_blank">📅 19:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90246">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niWTgW7LtW2Q4b0unV5XEkhOTTwz36IEklDrlUGtBMWPztzYdybuFzd5eFqULS7KAiINklAXuhH2DMkuM-A5a10upxBZqhXc5bwV557N4j7OYpG4kLxHeAvC5OrFog8-m-8T-ZEwpSPKRgFgoZoemnStMLhWTGAJIsT_YM68_-REs-ZiZMJXIhZrHLhorMKtT1Wdml3HGc1ILmzW5aCLLxJJJBTg_bR2v-J3dElA9wx3WQSYfeoROG8aL2K7-kMuZieqaFWzntdC0PkW8cxOAkVHweJIW4XoHl5ZZDyuVTn_MNiNVD5kkyIqHpi6g4Avd76kgReoZybealISAembbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سیدبندی فصل‌آینده لیگ‌قهرمانان مشخص شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/Futball180TV/90246" target="_blank">📅 19:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90245">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تا ۲۴ ساعت آینده سطح دسترسی به اینترنت به حالت قبلی برخواهد گشت. درحال حاضر اتصال وای‌فای درحال بازگشت به شرایط قبل است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/Futball180TV/90245" target="_blank">📅 19:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90244">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">تا ۲۴ ساعت آینده سطح دسترسی به اینترنت به حالت قبلی برخواهد گشت. درحال حاضر اتصال وای‌فای درحال بازگشت به شرایط قبل است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/Futball180TV/90244" target="_blank">📅 19:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90243">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbyxTqmG7rkw-aB0CI_Y33FF93gYMV_URbGdBsGVs1i-Ewz-MdhzrmeZpObPjJkFJHbqvqLBxkT-sa0SwMKJESgc4T-xGShGEWYy8BnFFD1w1VNztuOTts3jZRfXpyoWV22VM6N6QGIQ6RxOCHJErjjElXTVNAk4nDHU_KTGqz7Ohn-cUtXAwao-1Otsh1CWQtVEhsXXoUXACQS5ztgdEG7LRrnRwslw4hUIGYHJnX51H0Rlaf3JdumeanCLUC47GvDmLhfOA9ctZXldE8BPt8TO6mpW2dOcpM9fgBjPB49d9q98ccxZjsUS08hTsHhNQ0KXvi5KcisgD2Tsr80CvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ‌فصل 2026/27 سری‌آ ایتالیا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/Futball180TV/90243" target="_blank">📅 18:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90242">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtPVb823pNJV9rPvV3rp1LEXk36Md0QnFpz0cY367RLb5giKv5u7MxnJKLTmK1wxwaydW1LgQxGU6gDDRNj2kQUWNkUNAtmCIBtJ0o7xhBvkfBOlhR_rpTwcF9IHuEt7NflIbRap9OqbyFHWgs_6EM9LY_4rt7XpKLVJxcE6ZCnE7MPJBGp5GRpJfaApEhuSFtZiJjJXBV9VawInL81n1Z6urvYC_DXZvJSkWndVMDVxMrRAaRWMfI4wpK5jLoOKpBZU8rYkWc3TYm4AU1lQjDoeJ0S8gHaNfMJ3LVsTYa6OWOSHiGxDCUnMHhqe0xxLPRo8YoJe5XXiZ8qhRw88Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ فصل 2026/27 لیگ‌برتر جزیره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/Futball180TV/90242" target="_blank">📅 17:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90241">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxT6aj6UXE_F93jeoilM8jP4El7OUgoLdsbFG20Mi6mV8KYmTDvvsnbA04pXSdpDa7WfW8AKaJ3c1pDtRG8c1Bf6OejUKDBHSqDPP80y4Kq_B9Ij76HkyoUc0qP_DBF2QPjnxG5VgwPw76stp-1LN8t8oE1Gxrg4hvrRZXVoFJHebfp3G5Tabd6eW0MTJZhpxGgW814gqgU351cMO38GXrFP_wu9fxIPAMF01Wtjht8IUFBSwmQEioXYaD-8ugTt0cKt0A9lCArF99O9MArjVgJTBzs_oO-nIWqKRkzTGlCCccmX1b3Q3ju3MD6wcTd8QInWBF8e8Ps0X1tcuudXOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باشگاه بارسلونا برای جذب آلوارز پیشنهاد پرداخت ۱۰۰ میلیون یورو + مارک کاسادو را به اتلتیکومادرید ارائه کرده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/Futball180TV/90241" target="_blank">📅 17:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90240">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYlnRrSc7256Y_UqfU6uoBGrxcfkgXVkCYG9S9F3jp41LfO7l4_PY9LyCNBYF4fbeFvKuDKBW7jXEcZjRnLExwX2R4dxyv--6QpwUtvlILVbwU_o5AqDh1UACNRqUgpCREJ8d9DJ9w19zXMoAnGmRPteNzlVTQF_a1wzJ2Q-daaSOwmXRk3weIBVXDmshIB7t1JjwRPQzafPAOw4CHuzG21-2YXJzQld5pNPHX4kjCFvKmf70LdUCfbduPLepBCjcknQARDoqkdn9WHw8gff3NpvmO8qhoel6t_3PIEsGo2nk5Z6EdzAO0WEmqFh3M-xNIV_54T5zumhXVLSnh9sCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۶ ورزشگاهی که میزبان بازی‌های جام‌جهانی هستند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/Futball180TV/90240" target="_blank">📅 17:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90239">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0e6MZtwTp3OsNdu2ob7pqlesHH8g6uCYZJidgSawb88rOB_buoUAh8RqDcviaiJ6PpbYS_3cW3i5PsDs8XCZTx79xBZwCdyED7MGS-jL83HCcAHGoQfeSKCF6qHR6hVxwD5nMHV9DOhaivDoQdbybpFrjQP7BELDWxIVh7w7biRxJL4PzY07mruF5HDWgmbylSa9DfDVSgaZKyyEXAuMOELMeYkGw89HuJKSJt0sfrRolMGzAoqtEreAIreXgrogkf8xCBTPB1W0kUZfz-1t_Sq_cpnNsEY0weD24NfCw6KENbQp0Ko6ody4coKe6YCWGJat-FCyBqS-lQ_QJ0hDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
محمدرضا عارف معاون اول پزشکیان: اینترنت بین‌الملل در دسترس قرار گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/Futball180TV/90239" target="_blank">📅 16:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90238">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">مخصوص وای‌فای :
https://t.me/proxy?server=87.248.129.199&port=25565&secret=79e344818749bd7ac519130220c25d09</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/Futball180TV/90238" target="_blank">📅 16:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90237">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4MOMxwtYBQA74Uzo5G5h9iOA3dthJGRI3rk5XmoQE13PjYVNJFQqDO5keUek80MiqmZ4hyXf45DR2ntz9dXKC7rk4qG3c4qZyvk9jKDuD2iSQmddrapleJbGZyzUIft8NKQKT1D4GXCWVTccMHjVCft-KysvFeuBTIEKcsRSMD6-7LDGdyXzT5yAMgstgH54rgsPRp0goyJW7s49wNmuQA4mq41ikVSMtSf2F_qjraqXc21YsK2ouMc_0cVX4u5Uc36uwkhY6UNrHknn56C4CfKC-D4vndZdW7fu-1vHnfSuysTUs0G5TOGJKF8rzOQnqwUIfm67no5T80DyEdWsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نت بلاکس: نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/Futball180TV/90237" target="_blank">📅 16:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90236">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGL69um6NUdbpOTiZCih067x5jPAMApR-ZbO_K5KuaXhDNGk9A4AAdW0fc5YTXU_PXvfWAGuSLmywTt4uhL6MBYObqw_M5OTOzEcyLkIW01sKxgY-fGeJY55oNvzztProIW9x_FnkIIBvczYZPSPByoyCp34O_wXxdS2-PBc5PoMYFZgiIlAa9JkcGXjtbzM3nKxPyiVWfXn_CirnTQASR8dkNyf8hnzADKv0ysVtrt-oKZmHdxPLS4aSAQyeejoVssNL4kogpEEEV934cW0KYGspkcRfZEhe72zGVSpIwoEgNSMJH6sSUeRfsoNXST5qdL7w47KqYRbLmjpxolgHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور خوسلو در مراسم خداحافظی کارواخال؛ این دو نفر باجناق هستن و با خواهران دوقلو ازدواج کردند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/Futball180TV/90236" target="_blank">📅 14:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90235">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQk1NKMDRFt0J9nq3ByaSt4-BpIeIhX-iNq_eTJ1V_sU2TJsApkwswQUu_hqQ_Af8BXlO0ZapHwo6th9oDO8VCSCDlG7hErFl4JNPuEmfQ3OQkKm1rSBweY1xHUVHs1vCWWTyEReri79ENsdhPxDDNjxhWtD6lrRt96usQZK-0qGRTWrKLrTzsexXtlTv1qtMFZu_RP-FDHvtoLiR4HCf3UOMGz82oRy60W5uuQ2GNAGDtIoCKrxzgtFhC9eDAyqaMwI-MKC22fYca9TzDAVqEcYq4EmPZ7tCV3WDzKUG-rw95yfqNlUEu3GOObnkefBi5cka9rA_oFoWckEEF6wgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
این ۴ نفر، شاکی قضایی «اتصال اینترنت بین‌الملل» هستند
خبرنگار «انتخاب» دقایقی پیش کسب اطلاع کرد که ۴ نفر شاکی حقیقیِ «توقف اتصال اینترنت بین‌الملل» هستند. این ۴ نفر که گرایش سیاسی آن‌ها کاملاً مشخص است و تحت راهبری یک مقام ابقا شده‌ی دولت رییسی، دست به شکایت زده‌اند، عبارتند از
کامیار ثقفی، رضا تقی پور، رسول جلیلی و محمد حسن انتظاری
. / انتخاب
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/Futball180TV/90235" target="_blank">📅 14:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90234">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
وزیر علوم اعلام کرد که تکلیف امتحانات پایان ترم دانشجویان کارشناسی طی چند روز آینده مشخص و اعلام خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/Futball180TV/90234" target="_blank">📅 13:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90233">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
#فوری؛ سیتنا:
🔸
دستور وزیر ارتباطات برای اتصال اینترنت صادر شد؛ اتصال جهانی ایران از همین دقایق احیا می‌شود؛ اتصال کامل مردم تا 24 ساعت آینده
🔸
معاون سیاست گذاری و برنامه‌ریزی توسعه فاوا و اقتصاد دیجیتال وزارت ارتباطات، در پی دستور رییس جمهور از بازگشایی…</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/Futball180TV/90233" target="_blank">📅 13:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90232">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDoqHBi9WRzs985VHN81rrlp1XEq9tukswlahwky-r95YNpZHlylCMGPuhXURtu_UhZvjqUG-pnMH1-C9Pf0L7ol-Bn_NUz9qrnh5Jw658klFNSyrw67G10O-8b9uoNxozkczOvdWFCC2l6p3vimplnju4myHeTRjsZLtIO00-9kFQL2HAdn2io7wvODgCcVivjc-RVsK9i-5v7NtPjTRPZFQeDkZpiky-AT1PQHHb3MKZzBINFS-l0xsC-YFXmMYp3SLai05N5CcoqJtVHfC_xkJLIXV91cQVQmHD2vOaaxzOcvEXBfNOWOnHCysNi4PKTulgKqq3XxsOVmBa68oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ سیتنا:
🔸
دستور وزیر ارتباطات برای اتصال اینترنت صادر شد؛ اتصال جهانی ایران از همین دقایق احیا می‌شود؛ اتصال کامل مردم تا 24 ساعت آینده
🔸
معاون سیاست گذاری و برنامه‌ریزی توسعه فاوا و اقتصاد دیجیتال وزارت ارتباطات، در پی دستور رییس جمهور از بازگشایی تدریجی اینترنت تا دقایقی دیگر خبر داد و گفت: دسترسی کامل مردم به اینترنت تا 24 ساعت آینده میسر می شود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/Futball180TV/90232" target="_blank">📅 13:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90231">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0edb93becd.mp4?token=k41IUuCOhgQ6Xgc2POgUVWxPFA-yCPhWL4j362auNbP8oGfbff_AKEEQcEm4XxptuRAo4XPksxqSKZ0I8wdZ6q0HENTa1RhAqjzmozghDfX853QGM1Y3j4WOnZW2tUG3wTfTDfN5ib9p6BA3tHOA4zoBLFRaif0uSXcGCGv4U3e9TUopYXrCjKlxHun7OB08j0UhXc_6Wfa2BEX4axBixTF--hBQ9IwF6geGQrcM8XBEQOsqy07m6Nmbj3Gr9Xx2X739nJz9i_NDJVoeIFZ-7qp9lJn8x86zpFsqE_q_FHewU9HSg9dgxyZj5-AhujRnfbnS7fznH1Jkv_SdPcg-ahU8agpwnAKo6sUNfB8F_A3hLgP-dsCDvgX81vF_AkpM2iunpUNHlNUtQieUUaZGfqGTEkbqvl9rLPAqbj-Cq1rPw6UUO2m-SIzUcJ1rxtIHlS9AcMVXZbpSlOIj00ztLTCAZhiQiSHm-7NsjMdBeHV7K2ifSN6ObqwxkJaBHYG6rOjlxFDNefqM2iXalsR8sdCZLKL3-yl4DwzWBxgjOfL1C9FdvXG6Z4w_6OPya3TIHobHGpf0z93dPCmpw-4-f8nFn1VoJQVk8GJfQD5R-ELL_yvR94w2gIB0f8uTSpa5aobPkv4ETTY4E7TwW9ClUp__XsejqzF4bCpLLmwbKIc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0edb93becd.mp4?token=k41IUuCOhgQ6Xgc2POgUVWxPFA-yCPhWL4j362auNbP8oGfbff_AKEEQcEm4XxptuRAo4XPksxqSKZ0I8wdZ6q0HENTa1RhAqjzmozghDfX853QGM1Y3j4WOnZW2tUG3wTfTDfN5ib9p6BA3tHOA4zoBLFRaif0uSXcGCGv4U3e9TUopYXrCjKlxHun7OB08j0UhXc_6Wfa2BEX4axBixTF--hBQ9IwF6geGQrcM8XBEQOsqy07m6Nmbj3Gr9Xx2X739nJz9i_NDJVoeIFZ-7qp9lJn8x86zpFsqE_q_FHewU9HSg9dgxyZj5-AhujRnfbnS7fznH1Jkv_SdPcg-ahU8agpwnAKo6sUNfB8F_A3hLgP-dsCDvgX81vF_AkpM2iunpUNHlNUtQieUUaZGfqGTEkbqvl9rLPAqbj-Cq1rPw6UUO2m-SIzUcJ1rxtIHlS9AcMVXZbpSlOIj00ztLTCAZhiQiSHm-7NsjMdBeHV7K2ifSN6ObqwxkJaBHYG6rOjlxFDNefqM2iXalsR8sdCZLKL3-yl4DwzWBxgjOfL1C9FdvXG6Z4w_6OPya3TIHobHGpf0z93dPCmpw-4-f8nFn1VoJQVk8GJfQD5R-ELL_yvR94w2gIB0f8uTSpa5aobPkv4ETTY4E7TwW9ClUp__XsejqzF4bCpLLmwbKIc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
جزئیات درگیری علی دایی و علی کریمی در مراکش:
🔺
رضا جباری: فکر نمی کردم اینقدر علنی و شدید با هم اختلاف داشته باشند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/Futball180TV/90231" target="_blank">📅 12:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90230">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90230" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/Futball180TV/90230" target="_blank">📅 12:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90229">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doyZwLGTbSj_isy9BJwcWD1rrjFEYW0cJF9IGT1cWDBJAtMsbJSn1VVezsqAXs0gOyr5BpAomxJIjObf82Pk2H7uu3G-M6L3NdvAd16pMwJuJt0tzAZd_DO8n14GRnCUtPl1SYFVstBvLZyjHsvUfCTItItou2WXw3ef4gnUYgfV2NkrGdF8NCFmQnNdtM7oJWT80W4xNoRMgPO5WeNIWsA0lQoiTVqZ3Ws6amcc-kBnMeB0AZkyDem9uNNWB4rO-f0ikce-gw1VZOkv0eml3KJfetAxtD6KBg-AfR6ZbU-Y1eZ3V6auuX3e83uo9VFbaa_bkaJ-lfyDMHL9XfObEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/Futball180TV/90229" target="_blank">📅 12:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90228">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d9611d964.mp4?token=gQpBSQXfMsIENneXhMS8hS-GpK25LHobqbqHATWPON19hh_WWMKwtzrNfmfr9D0b1XgKjko1YcqZJzepSuGijAZy7aMoJ004HDVLIi-8CSckYpGoZvWGsjSibUCVf7oa8YxfByMGFI4VIL0P0v-T48e-RmQ7dbjijCawjzZNaf0FMVYXxMwZiWBA2605d3bNqzLagewhz6QHaw0K1chdhMl5vVdT6ST_nbz1p6g9Tvx3bPyE3YGoqRLij0nY-_AV2igZmCsDi8679S-bOPBHYyTLQhLeBb_1UVddpz43O9-naFwTnNfFTEQPxIWp_ydDv8rpshrfSFTIky2fMH-1yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d9611d964.mp4?token=gQpBSQXfMsIENneXhMS8hS-GpK25LHobqbqHATWPON19hh_WWMKwtzrNfmfr9D0b1XgKjko1YcqZJzepSuGijAZy7aMoJ004HDVLIi-8CSckYpGoZvWGsjSibUCVf7oa8YxfByMGFI4VIL0P0v-T48e-RmQ7dbjijCawjzZNaf0FMVYXxMwZiWBA2605d3bNqzLagewhz6QHaw0K1chdhMl5vVdT6ST_nbz1p6g9Tvx3bPyE3YGoqRLij0nY-_AV2igZmCsDi8679S-bOPBHYyTLQhLeBb_1UVddpz43O9-naFwTnNfFTEQPxIWp_ydDv8rpshrfSFTIky2fMH-1yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریکشن گاوی و لامین‌یامال پس از حضور در جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/Futball180TV/90228" target="_blank">📅 11:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90227">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
آیت‌الله مجتبی خامنه‌ای: رژیم صهیونیستی مطابق گفته پدرم، ۲۵ سال آینده را نخواهد دید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/Futball180TV/90227" target="_blank">📅 11:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90226">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d0834d346.mp4?token=VGC3cwn-V_aHTGbrM1szQ18BwZat9C3WVX6rtVZ2BBqbA4gX-NSzTJCBh-ReEOwlPUEPDlAmBQQRvAuV70sSXjB1bP32jyYzN9MjlLwzLW7C_jXNoqRZqH3AtXJGkZfjjCBY13NcXjkbV-PQyB5Cf7EmNBPa5pV_FMNpbI7nH3X0OwcfzdJmxgkxI2l5XVLvIec87GPjMTC9ZB9wCMg9MNwPGyAEEi1XnaBcKJxc427wF2ZyjP7O-FHrHkPywqEfuyz0WmYqEL9Cwa0I7eWvnE1NW6KxrPR6inIkdwgiCa6WsyPDVlC23Szggr2IQzNasOdFmdEzqfOAodPpDg_H8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d0834d346.mp4?token=VGC3cwn-V_aHTGbrM1szQ18BwZat9C3WVX6rtVZ2BBqbA4gX-NSzTJCBh-ReEOwlPUEPDlAmBQQRvAuV70sSXjB1bP32jyYzN9MjlLwzLW7C_jXNoqRZqH3AtXJGkZfjjCBY13NcXjkbV-PQyB5Cf7EmNBPa5pV_FMNpbI7nH3X0OwcfzdJmxgkxI2l5XVLvIec87GPjMTC9ZB9wCMg9MNwPGyAEEi1XnaBcKJxc427wF2ZyjP7O-FHrHkPywqEfuyz0WmYqEL9Cwa0I7eWvnE1NW6KxrPR6inIkdwgiCa6WsyPDVlC23Szggr2IQzNasOdFmdEzqfOAodPpDg_H8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینترنت بین الملل چه زمانی وصل می‌شود؟
🔘
سخنگوی دولت: امیدواریم با ابلاغ رئیس جمهور ظرف روزهای آتی اینترنت بین الملل بازگشایی شود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/Futball180TV/90226" target="_blank">📅 11:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90225">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9Y6Fla1XMPborb0mnsH0Sl3ys9VZPO55TWXRLbpllpIp4sYCtEg5GMhmYd-c4IryZlDEf86n0vvWohx5CWV5hk8iDvVxawaTgKmzR4s45Nb8DZR8GjOPPydrCxGxCCvrEjnu5K1apa-_4LrbzflQkUsBk1vTUWCqF_h1Qdbg1lGMcYx9PT8_h6g5QD3_ojgW7MEWDF0NuiEACwaKi0ogzUtgtGnTcbs_bLslocw7yl4vj6Bx58aNsHMjvRZby3pSdYoP6_-thZvfkhV4LDbInW1Ztgqsm_XW3149__56IRPSl06fa7g2RjWGQ2vYulgPmjrqiTaBOPG9eDHuVssKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قهرمانان دو جام‌جهانی اخیر در مرحله گروهی در گروه C قرار داشتند. برزیل مهمترین تیم گروه C در جام‌جهانی است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/Futball180TV/90225" target="_blank">📅 11:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90224">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDcUNuu5X8nBkiuTEt_w8MWj_y2_Ark0BrOQYn1iLizCtRymq0QhYydgDN16GYOT648d4D417O85xVcoJl4uhH7qA4KwfCeqo7IUjALfR2_Kk-PKGjkxiMsbPfLB-Ba0oqJenysnlnhyvFIY8ljW6KWmOkQTJFfzuhLT51DQCCAAEYI_e9DYpvUfv7pigHQAMEACGap0F8lAuaoHUyx2KKj4CScO29HWM7R2LrS3lOrQl-eesgaobzkMBZ9iXFAKKg51BunsfyKTw4hpe7JbenOvZy_ddY5Bp7LKNqB0PE-cUhhiMeBqXMgIJccUGPl2EerNJHpMnM66v1sIWfJr5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با آغاز اتصال احتمالی اینترنت بین‌الملل؛
ساعاتی است جیمیل در دسترس کاربران ایران قرار گرفت.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/Futball180TV/90224" target="_blank">📅 10:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90223">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7673ee9149.mp4?token=C4lz-UmfADm01i25aVr_NPEfON77DUdkLNG7zUJtsWg5DgTr7X61LbHpkw30T8e7gS6RfuBz9piFjMPAnNFsBiZm512oHcG1dzy4IfFg2rFMU2eqJmk5UHOWPljlbPOQYqVbfBDe2xi5gsLdzItqgZMcrJmKOqGC1eizR8yTJMRpn59UPH5JZ9zLXVyfzvS9Cbit2ul7NyTlYXTa8yQSGXIFL8w1AYyczV6U7cVnQcHow-6u66aND5irusV0NDrHygc8rBpbB5-WPeHqJx0yDYldT8OUjjiHx6CVskBUSSKer0gZOIoMkbGYT5KjuToj-S8X425OELacWrPP-eCvDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7673ee9149.mp4?token=C4lz-UmfADm01i25aVr_NPEfON77DUdkLNG7zUJtsWg5DgTr7X61LbHpkw30T8e7gS6RfuBz9piFjMPAnNFsBiZm512oHcG1dzy4IfFg2rFMU2eqJmk5UHOWPljlbPOQYqVbfBDe2xi5gsLdzItqgZMcrJmKOqGC1eizR8yTJMRpn59UPH5JZ9zLXVyfzvS9Cbit2ul7NyTlYXTa8yQSGXIFL8w1AYyczV6U7cVnQcHow-6u66aND5irusV0NDrHygc8rBpbB5-WPeHqJx0yDYldT8OUjjiHx6CVskBUSSKer0gZOIoMkbGYT5KjuToj-S8X425OELacWrPP-eCvDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هواداران ترکیه در آستانه جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/Futball180TV/90223" target="_blank">📅 10:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90222">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ed589fd9b.mp4?token=baV14zF-TLhMtEA7BzjoQwYCCnFmM6xQ24igO7rjoCBdGM6ersNCakxIURGj3bEAsmB8J0qqCgdL1JY9UtMpaO0PIPuyJ0fi9q2YliJw-Bl55Kd8iWx0HWpleMaLBBLbnZZWJtAJ2-Pm13481yqcjfK3NfVqKcbDMmqEjl4sWgXpqoNAMdFor5pLuj4whzOJpJQce6-tBR7A_yeZFlRcATRNIdr1ygMDCH3E5h8Fziw4Rp13Dl5nNP5vCL07xv7vW9iEKqMPDC_LxhdTtTTFpHVWNG7lkHs3oQ6ygG7j_46jtotTIyy2hq3SZEaiYAq5C3YWRsJxT3-b8zym3yamLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ed589fd9b.mp4?token=baV14zF-TLhMtEA7BzjoQwYCCnFmM6xQ24igO7rjoCBdGM6ersNCakxIURGj3bEAsmB8J0qqCgdL1JY9UtMpaO0PIPuyJ0fi9q2YliJw-Bl55Kd8iWx0HWpleMaLBBLbnZZWJtAJ2-Pm13481yqcjfK3NfVqKcbDMmqEjl4sWgXpqoNAMdFor5pLuj4whzOJpJQce6-tBR7A_yeZFlRcATRNIdr1ygMDCH3E5h8Fziw4Rp13Dl5nNP5vCL07xv7vW9iEKqMPDC_LxhdTtTTFpHVWNG7lkHs3oQ6ygG7j_46jtotTIyy2hq3SZEaiYAq5C3YWRsJxT3-b8zym3yamLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
سیاوش اکبرپور: جرمی دوکو رو می‌شه مهار کرد!
😁
محسن مسلمان: ولی نمی‌شه؛ فکر نکنم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/Futball180TV/90222" target="_blank">📅 08:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90221">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90221" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/Futball180TV/90221" target="_blank">📅 00:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90220">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLso4Xx4CkoP9oJq5kDhh14N0dI4dYOBqQoQtEvcfc48IllKv3zYtct4SH7Za7rIR9Zxbcl_wZMWCjODbdCNSOteeOhXa-330NNPc1kUALcmYaw6iooQCNf8GFxEChCA6DVRqAsTFB1LYGiQV4DUfJI28WJhsgtlKaCugJhL7X-gMdGtSXxDzu9-KXHHpdSYDisDlno5nkptk4OMEeDabkTWIHzZSnEVrnp9tdXq3tPebsgsmy1pC2kkqZVY8SO7CeWNGOtWBQLbhRx7xqveG8_5LzDtjnIOvdacrCymCF7AzJddnc8f0bvYzayj7pJz88diOEJCu0fHORjHJEX25Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
با پیش‌بینی روی مسابقات افسانه‌ای Roland Garros در پروموی Grand Slam Tournaments، فری‌بت‌های تضمینی و شانس برنده شدن جوایز بزرگ رو به دست بیارین!
🏆
جوایز ویژه قرعه‌کشی:
📱
گوشی iPhone 17 Pro Max
📱
گوشی Samsung Galaxy Z Flip7
⌚️
ساعت Apple Watch Ultra 2
🎧
هدفون Samsung Galaxy Buds3 Pro
🎫
فری‌بت و امتیازهای بونوس
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/Futball180TV/90220" target="_blank">📅 00:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90219">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuABEr23abHGi_iuO5ht7uTo4e0SvabaT_YdnAFzClsPlApnX_5GEbMMpJGwfupH8fDQKVW1ckg9T54uYPCF2QBMFlzT7FWiaaAuCJqQ0mnDQGQQMoEW7E2rhY3HBfrxl6gh5yfCNQ-T_-rsnFaSEIVxS2Wy0mYRiRIZ74t-KZJ0EPdmJa-JxeU1aKvVFhql1-UDq9wPIzncQnG71H7RpO0LrhDzJ6gWrQnqow9yPppvoR4rYUWMwHxIkhGcesxfJwjrtpEkwqTsJ2q3BBl3uPpcXlCGjWhLZgWBi_qXPI2sbMWjkpzLuP-qySpE5ijP-OfVkNCm7qeAte8SR17L8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇴
لیست تیم ملی کلمبیا برای
#جام_جهانی2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/Futball180TV/90219" target="_blank">📅 23:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90218">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdh5mDyGkFs6R8YjbsiAJ9B-bjLcgvjMvWH_XRZuDMBOIIO3xs8Dtdy3z_ck3C5juK0qLNP2Hl0CraLz5kqvKodrkvmY_zzRc1MEh1ib2A5ZXeSSAF_ZuGcg-4XElHM3EChVsxARCrs7114wwMu6u2NjBjngd50HC3apHA3v3ywIW3FeH7Md8xjBvx5lf3pppeqRrlfHcneSjfEyIRFWL3jdOsAY5KXuk3IOKYVeIixd1-7a7yXi93i1D558hTJi4ZaO4Hcq9q-h9rzrpxKCqguL9tKX3U42mh0acKSPoTiUEEDp2E4wwRP7Z3TGgdXpLUMxbhi08le47ZqqX0n_jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مکس آلگری از هدایت میلان برکنار شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/Futball180TV/90218" target="_blank">📅 23:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90217">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3602a6e5c9.mp4?token=d3BttHlJhxAc9_6M9vNt5CpVhv2rp4f0aH_HD8DGn4tSE-QRx4dfQCVEKyqLrVf5CyjQFwftzk8S7OXsXjJaLtGTAOlxjDps1sfWsKalsTIFLiy3vt7plBTxXSsns1q0nkk1uq32tMMh8lDgphAX3mUAikplCKAthrtlBC3HbMMt3WYxv_8SUH5xFncOeC9k1u6oLdInGHbH3PqBt1lhqPuhsSkZ1I0EFLVkyN8ix6X-Ha_57znv_bH-FlK55nae2WA3CqZqAV8ve87vQxCUztV6Yg_h0DuX1dyqDHGzR68s116OQKKysnJ54_It_GMBJeASHmusQPU9-KDEnJi2ySdOx5InQxRaguwB6v8tLrAbH7VsuPZu8LESU1kAcGgaQL-4dxXs4x803vpDi-UqEDGmSTFyZi6vAfy6VKXSwebfNfmkzt1Oin5haLXvnl0EHf9-6VhUVPIzYLiJxi71xJJOnQoPUVRO2ktbsnC6j-DleZw8wHsA-O7NPpqf34ZXbA5ZqzfGdhExeLMXTS25a1nEMAOp2joY7iwDpVPr0xDwyk2HzH_awBpJlGSCp4ShX0eskzcImt2aK0eaTBupWAQijZNpLOyQqIx_5Do7hxITZ622vy-Tzvo1gt9j_LgE30GniXEdUnTxCkqRn4PGorL_pqbv1SfIX9wkpA8QLHY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3602a6e5c9.mp4?token=d3BttHlJhxAc9_6M9vNt5CpVhv2rp4f0aH_HD8DGn4tSE-QRx4dfQCVEKyqLrVf5CyjQFwftzk8S7OXsXjJaLtGTAOlxjDps1sfWsKalsTIFLiy3vt7plBTxXSsns1q0nkk1uq32tMMh8lDgphAX3mUAikplCKAthrtlBC3HbMMt3WYxv_8SUH5xFncOeC9k1u6oLdInGHbH3PqBt1lhqPuhsSkZ1I0EFLVkyN8ix6X-Ha_57znv_bH-FlK55nae2WA3CqZqAV8ve87vQxCUztV6Yg_h0DuX1dyqDHGzR68s116OQKKysnJ54_It_GMBJeASHmusQPU9-KDEnJi2ySdOx5InQxRaguwB6v8tLrAbH7VsuPZu8LESU1kAcGgaQL-4dxXs4x803vpDi-UqEDGmSTFyZi6vAfy6VKXSwebfNfmkzt1Oin5haLXvnl0EHf9-6VhUVPIzYLiJxi71xJJOnQoPUVRO2ktbsnC6j-DleZw8wHsA-O7NPpqf34ZXbA5ZqzfGdhExeLMXTS25a1nEMAOp2joY7iwDpVPr0xDwyk2HzH_awBpJlGSCp4ShX0eskzcImt2aK0eaTBupWAQijZNpLOyQqIx_5Do7hxITZ622vy-Tzvo1gt9j_LgE30GniXEdUnTxCkqRn4PGorL_pqbv1SfIX9wkpA8QLHY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما ۱۳ نظامی در عملیات خشم حماسی از دست دادیم تا مطمئن شویم ایران به سلاح اتمی دست پیدا نمی‌کند.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/Futball180TV/90217" target="_blank">📅 21:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90216">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POcuLBtdo_ZB3o8K1EWHBYUfEc8H9RsGvCNxosGJbpAAXVdw779bPPjh9AVxEWqBmfM8voo23ykwfblSEImyM4o99p9Vsdj36jXqNUk_H_KQz4smijl1GYL67k3bFxentVgTqPKXBzHv3RPBgWYKuLQ_gpQFAIuHMI44zburk5TcOJCCpRAWYpQhr2buor2ZNfWjemyasbxdrW5FXoLQ6aGB1NEKxHQONZwq2dj6hwAUeP778FOT6gi_jKnqtoFv4V93B2TOb4tPFArpz187h7os4qzevasnp7BYQQWoqn4vKj2dtbmqwcdy2QuOCXHcUe7TdZSTHgOkb3Fu0iSONQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
سن-اتین - نیس
🏆
پلی‌آف لیگ ۱ فرانسه
🇫🇷
⏰
سه‌شنبه ساعت ۲۲:۱۵
🏟
ورزشگاه جفری-گیشارد
🎲
با بیش از ۴۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
سن-اتین در
۱۰
دیدار اخیر خود، چهار برد و سه تساوی کسب کرده و در سه بازی شکست خورده است.
✅
نیس در
۱۰
دیدار اخیر خود،
پنج
تساوی کسب کرده و در
چهار
بازی شکست خورده و تنها در
یک
بازی پیروز شده است.
📈
میانگین گل در
۱۰
دیدار اخیر سن-اتین
۲.۵
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر نیس
۲.۳
گل در هر بازی بوده است.
🧠
اطمینان صددرصدی نشانه خطای شناختی است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/Futball180TV/90216" target="_blank">📅 21:09 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90215">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7263cfb5.mp4?token=VPt2D3ruMChfQ_5JwcGUL77MLHcVKcDGb4W1k5kV--wK5huB7_PQVxdcTqNh55i9m--BIeCFhT6AuT7Ayhcrp3F3bOvzV-MLXA4zMjzqv77bfb_MeGyP1xPoxALXSzhhoSPao9qcGxnlLyMZF7klEJ7oaM7YYxHGYDyWRqLRULCl3ibASBDewdB-S_34Ti-A795RXaaL4EvS6UD8n81oOCIlA6HHG4HDmp5PaLvfzJ6I3rw-hA8y314AhdYVVX1Q0f0gShHjBNj6MeM-mQlS7M7SgwILRkwGCTzy_cmHALF_8NWZchfj7t_oWa0pDaWusDE6kucq8gXmCRFHWW7Kag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7263cfb5.mp4?token=VPt2D3ruMChfQ_5JwcGUL77MLHcVKcDGb4W1k5kV--wK5huB7_PQVxdcTqNh55i9m--BIeCFhT6AuT7Ayhcrp3F3bOvzV-MLXA4zMjzqv77bfb_MeGyP1xPoxALXSzhhoSPao9qcGxnlLyMZF7klEJ7oaM7YYxHGYDyWRqLRULCl3ibASBDewdB-S_34Ti-A795RXaaL4EvS6UD8n81oOCIlA6HHG4HDmp5PaLvfzJ6I3rw-hA8y314AhdYVVX1Q0f0gShHjBNj6MeM-mQlS7M7SgwILRkwGCTzy_cmHALF_8NWZchfj7t_oWa0pDaWusDE6kucq8gXmCRFHWW7Kag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن‌روشن: فيتيله ترامپ رو بكشيد پايين وگرنه با "اسلحه ژ ٣ "ميريم آمريكا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/Futball180TV/90215" target="_blank">📅 20:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90214">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/Futball180TV/90214" target="_blank">📅 20:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90213">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lHdR15plks81JZdTlR4A_f68p2w-kcI4tEJPW4FNToTE4aS0Yp2skPZ9AJooq6XADRtBoMob1Ti3e2BlI2pLScFjHJQXwOeB2jJD6Rs4jcoSCZFMQTi4lbvJ0o4frojlHrJSOXD6kwnYXMYRAhiWW-KySc_HP_TROUZCYFzNjLQ-NL71m6Knbpp0ApjJyGwEF4HaD5Nhqh1HDmCkcGdf01gp3d5i9WonSsbLmd2GxJ34JHCl4O7ndYGEgVuQ8jBnBhj-ImjxdB6tZFSVrD5iEYt3eCDeGflLx0DWRyrtXc81gmHR-2sIRl0RTOgafRPHupcrD5Zir340sT4KSPVIvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/Futball180TV/90213" target="_blank">📅 20:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90212">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🔷
جواد نکونام سرمربی سابق استقلال از طریق ارتباطات خود با افشین عبداللهیان مجری سابق شبکه ورزش که نفوذ گسترده‌ای در هلدینگ‌خلیج‌فارس دارد، خود را برای سرمربیگری فصل‌آینده استقلال معرفی کرده هرچند که در این میان تاجرنیا قصد دارد با سهراب بختیاری‌زاده در فصل‌آینده ادامه دهد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/Futball180TV/90212" target="_blank">📅 16:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90211">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPhiENCmPmoaatWU75ox5ivF5UbnZdBUGiH_H73pCt7V7JOduAZ538VIRb-abHUecnGzBlv7KgBFdhMgO2OP-oJm9h7jWgd6WwybD_GiKQ1g7zk5sCmEkavSrtZ3SpIQqiwt6u1wqDV0-TOcwwfvXIzYJS7i1IXc06POTX7iinkyRkMiXC8jppsryYf1zlRAVBG7aI5u8VZf1eVjJhvoLDTPxqJeNcN6_NZ57aGQ8gss62WZ75yhzV1scbnM76NBh5PHKBTq1Yk533kH69vjz6htIh8ZtdEq51dWPK8lQ3qnOreOuZUBOwxPQNzEJP_HGqufs-sFECf5mmgVw6n90Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست تیم‌ ملی اسپانیا برای جام جهانی 2026؛ بدون حضور حتی یک بازیکن از رئال مادرید!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/Futball180TV/90211" target="_blank">📅 14:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90210">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromV2rayYar</strong></div>
<div class="tg-text">🔐
سرور اختصاصی با پینگ فوق‌العاده پایین
مناسب گیم، ترید، استریم و استفاده حرفه‌ای
✅
سرعت و کیفیت عالی
✅
آی‌پی ترکیه واقعی
✅
پایداری بالا و بدون قطعی
✅
مناسب استفاده 24/7
✅
بدون محدودیت زمان و بدون ضریب
💰
قیمت تک: هر گیگ 150 هزار تومان
🤝
قیمت همکاری: هر گیگ فقط 120 هزار تومان
با ضمانت عودت وجه در صورت قطعی
🙏
برای تست و ثبت سفارش پیام بدید و از طریق ربات هم میتونید خرید هاتونو انجام بدید
✉️
:
@V2rayYar_bot
@V2rayyar_sup</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/Futball180TV/90210" target="_blank">📅 13:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90209">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
ستاد راهبردی فضای مجازی صبح امروز موضوع اتصال اینترنت بین‌الملل را مشابه دی‌ماه سال ۱۴۰۴ مصوب و به رئیس جمهور ابلاغ کرد تا در صورت تایید نهایی،‌ وزارت ارتباطات موضوع اتصال اینترنت را اجرایی کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/90209" target="_blank">📅 12:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90208">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfa22a668b.mp4?token=LJcshljLliOrkYKFOCYxgdAQWduM7yaTNsoYpXv_zz_ldhUXu0dtT5VeR4EfFSdXuCBUk6M67V6nQbO_HS_6B1LLn8xDRW_loHRguzV4Urtwn9RcCOcQO58mt4eeVWdho9japBFRoX21bLt4RtkiAFfD5wwkuVETklODdlzXEKgbT_E2mnSJQ9ZWvjLDy582kcS9sSbdkr92_16ut0NCFJ_uXoeD4-KKsLIo_lpBUy3Ry8__m_BUgTGkNfrbbBCk75A3GR6nzCILJU7DNCxO7ce8PFGdrmZmhoWWYb1FBD8sDDbJjL3SThcI-j6rUV-tATBEw6Ui_MLB92ibV0UgCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfa22a668b.mp4?token=LJcshljLliOrkYKFOCYxgdAQWduM7yaTNsoYpXv_zz_ldhUXu0dtT5VeR4EfFSdXuCBUk6M67V6nQbO_HS_6B1LLn8xDRW_loHRguzV4Urtwn9RcCOcQO58mt4eeVWdho9japBFRoX21bLt4RtkiAFfD5wwkuVETklODdlzXEKgbT_E2mnSJQ9ZWvjLDy582kcS9sSbdkr92_16ut0NCFJ_uXoeD4-KKsLIo_lpBUy3Ry8__m_BUgTGkNfrbbBCk75A3GR6nzCILJU7DNCxO7ce8PFGdrmZmhoWWYb1FBD8sDDbJjL3SThcI-j6rUV-tATBEw6Ui_MLB92ibV0UgCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین ریکشن‌های پپ‌گواردیولا در منچسترسیتی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/Futball180TV/90208" target="_blank">📅 12:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90207">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90207" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/Futball180TV/90207" target="_blank">📅 12:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90206">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_gRDlLbYzLwAqOmgZdEazZ2LCLVICKGAPsTko4JH6yZAU3li1hshzRwLUvfT36nuWxwrZY4PxzoqVtbf6EHuy4Zj0vUsQuN3BwX54iift4ObeYV7di_LfFkEXEwL9PKwMiFPd0gxenWyhhdmUPaMNP1jNdqYRrvPqW_2tvLN5a-hvzMBTvoqwXaqXaXfgq5iwF7ugvoIi9LETXJ3UJ7GiRlH1h2JKu6TwGxWDbULtERxTeddL-rso1K1qVA8YjVDfMz02LuTpYj0StPbMgubVtvFkDdJtSVxx45Rw1G8prl1GCldaPyjc6r6VbJmQgMs8PkxYsbsvLGq__Z_eFcaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎰
با 1XBET راه خود را به سوی ثروت بچرخانید و از سرگرمی های بی وقفه لذت ببرید!
🎁
تنوع گسترده از اسلات ها و جوایز فوق العاده را از دست ندهید!
💸
فقط کافیست ثبت نام و واریز کنید تا از جوایز و بونوس های فراوان 1XBET جا نمانید.
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/Futball180TV/90206" target="_blank">📅 12:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90205">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940870b589.mp4?token=rM6xOH0kCLSmblL59XNOK8EShPr0MZr7QxYqMq43UAZVabdJWmLRxM3A0Ahj6wgEdosf5yBdBuYrFP4CXFOBlLj-1vUONjx8CzdBWCHf-vhnRcLYfD1_w_ON1qQ_CP-PI2-ZlEj3w628hhk64iwhkM7tpoXQkkLj9bWuhIZo-rQ8VNWV3pK1HxqQ4nMN3McPyA0aj9mHiydKVDN2mN3jY3YwHvBUWJaZ-_INMQ0lrCTtxdgGKATDg-_FfFeJcwHqMyS-hCJvfssBX2iPsjpcfn_oQCFvxcTKaQBgX_5Kfgp1qUUkDIcpLCFMV5yWgRXb3ERH2pf3G-6hlz_lohDY_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940870b589.mp4?token=rM6xOH0kCLSmblL59XNOK8EShPr0MZr7QxYqMq43UAZVabdJWmLRxM3A0Ahj6wgEdosf5yBdBuYrFP4CXFOBlLj-1vUONjx8CzdBWCHf-vhnRcLYfD1_w_ON1qQ_CP-PI2-ZlEj3w628hhk64iwhkM7tpoXQkkLj9bWuhIZo-rQ8VNWV3pK1HxqQ4nMN3McPyA0aj9mHiydKVDN2mN3jY3YwHvBUWJaZ-_INMQ0lrCTtxdgGKATDg-_FfFeJcwHqMyS-hCJvfssBX2iPsjpcfn_oQCFvxcTKaQBgX_5Kfgp1qUUkDIcpLCFMV5yWgRXb3ERH2pf3G-6hlz_lohDY_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و دیگه محمد صلاح تنها قدم خواهد زد.
💔
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/Futball180TV/90205" target="_blank">📅 11:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90204">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392ebb3ce3.mp4?token=k2UjROBCdENlKKRjV8fGYKF0gKbRsYn8-_DQxkc_wKewsT0aknJ_zfVNQvqvHhYh6RrRJ5KscdYOeBQHWJaMtnvsayHIBZzqM3QRxzD359GtLlUSFUFxa9N7Wj1jK-NBl7osvzOGqhgnbv75BGczxyxHJ4Z3NlfC5QuSkxAZd0SWxCXUjI7C00QH4sh4lEbPSX7Ir3x9FiGRVsV3EywGZVaDyLK3KsuiK9y8J-n81jPSU9CUXmbFKQpPUhNSDb174num1cPltRDnpudYR-OGVRUFaf8jG5ebB2puiXARlow5LFXZ8NmAYbXNIJ3J1GeZwB0VaaxLo2LgeRsX-jUmcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392ebb3ce3.mp4?token=k2UjROBCdENlKKRjV8fGYKF0gKbRsYn8-_DQxkc_wKewsT0aknJ_zfVNQvqvHhYh6RrRJ5KscdYOeBQHWJaMtnvsayHIBZzqM3QRxzD359GtLlUSFUFxa9N7Wj1jK-NBl7osvzOGqhgnbv75BGczxyxHJ4Z3NlfC5QuSkxAZd0SWxCXUjI7C00QH4sh4lEbPSX7Ir3x9FiGRVsV3EywGZVaDyLK3KsuiK9y8J-n81jPSU9CUXmbFKQpPUhNSDb174num1cPltRDnpudYR-OGVRUFaf8jG5ebB2puiXARlow5LFXZ8NmAYbXNIJ3J1GeZwB0VaaxLo2LgeRsX-jUmcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدومیت لیونل‌مسی در فاصله ۱۷ روز تا جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/Futball180TV/90204" target="_blank">📅 09:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90203">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76980eb486.mp4?token=CcbE9R8wWDMpRgwkzc2CDhwUWYcK4XO1BVcC3ysb7Mm-yLf31XdS0iCOyorTohei1wYQKhEy6O5mMeV0mVji12B9d54zasZo0P-FErz-IJIaJZWvO7YciS4BzDeTpwR-mGTDzf2rD5ssM3cpWwTYK1dcMzqfbUUi2jD1DJjnEN-qNG7K5deyFosmqku8283NdUb-NdI3f8L7GMJW9--qklOATBKx8aYcZ0i9fpSOB_dxWmCblACfhCPItpImGQMG1TdqYuWNsou9ljt1Ip9-ZjZAT4M94I9WYtLW00ISrKSzQRhlrc7iuyru-6lgw-l28MOyEAqVFmIm6HEd8wFs1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76980eb486.mp4?token=CcbE9R8wWDMpRgwkzc2CDhwUWYcK4XO1BVcC3ysb7Mm-yLf31XdS0iCOyorTohei1wYQKhEy6O5mMeV0mVji12B9d54zasZo0P-FErz-IJIaJZWvO7YciS4BzDeTpwR-mGTDzf2rD5ssM3cpWwTYK1dcMzqfbUUi2jD1DJjnEN-qNG7K5deyFosmqku8283NdUb-NdI3f8L7GMJW9--qklOATBKx8aYcZ0i9fpSOB_dxWmCblACfhCPItpImGQMG1TdqYuWNsou9ljt1Ip9-ZjZAT4M94I9WYtLW00ISrKSzQRhlrc7iuyru-6lgw-l28MOyEAqVFmIm6HEd8wFs1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحید قلیچ در گفتگو با بهاره افشاری: امیر قلعه‌نویی واقعا غیرت و معرفت دارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/Futball180TV/90203" target="_blank">📅 09:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90200">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpPa1T2xXhG8gz0_VEwVbuzHnjxo_KvAl3uiZkO_vuPp0JsMvo5I7X-D4-MJp3esCnPqrjgtFz-A4zjLA8FiE0UynAm3AUbHu-2UKbc0Uz5O7uTPs6fm0yWzFmQK92Su8_gxafJpavTU0TWGJIfXHH32X-NC7JVfB5t1fSjY9m3VEuVgrlapZYM96jJ_O5a-m0T7pbTr5gR7zMz9w_NY37qJK39yAH0uBc4yP2JK4Gsf6XocitXfwLpd7cOXy0nYjNL1H0vJExKwoTN57T0A7o6k6eDZq_CT6q08eaVLYIOpAHi2DkhI6BFoGG8tlEw7TzI2ieOwwRkFZ0kDrsL1Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درخشش کومان ستاره النصر در دوران باشگاهی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/Futball180TV/90200" target="_blank">📅 00:11 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90199">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bf21c6839.mp4?token=i52DOr6XFXKDT9CopVZeR9hQP6beLDmGnbzQ-0EzfWBtMGGUHlb139hX3n6wHlPDu7dWDBsgcp5IBv75N-GpyAuFyIFsQY70RJl5twoELvm8kIPSye_KAx6Exw_UcRxwR-Etxlbh9Pz6vsAtrrPnwuvdzRwv_f9xSt2p_HdlO9EoLOenrpukMWxeBPdXFzH9fbMv3XMFF8my8R197pOt33dvpWO98pGP0J4nUN_-kqR3O7_fKanKD2W5saLLbq48e-0erS4ROYpPKbD0hOYYGUYpk4W7Jbd2aDGmbmLrK--oV_5vJMiJpl4yKXkt-Zp7XPocBIqeB3i1qQj54_z0AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bf21c6839.mp4?token=i52DOr6XFXKDT9CopVZeR9hQP6beLDmGnbzQ-0EzfWBtMGGUHlb139hX3n6wHlPDu7dWDBsgcp5IBv75N-GpyAuFyIFsQY70RJl5twoELvm8kIPSye_KAx6Exw_UcRxwR-Etxlbh9Pz6vsAtrrPnwuvdzRwv_f9xSt2p_HdlO9EoLOenrpukMWxeBPdXFzH9fbMv3XMFF8my8R197pOt33dvpWO98pGP0J4nUN_-kqR3O7_fKanKD2W5saLLbq48e-0erS4ROYpPKbD0hOYYGUYpk4W7Jbd2aDGmbmLrK--oV_5vJMiJpl4yKXkt-Zp7XPocBIqeB3i1qQj54_z0AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
بازیکن تیم‌ملی والیبال ترکیه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/Futball180TV/90199" target="_blank">📅 21:43 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90197">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/028fa17067.mp4?token=linZrbRDeCyPov1ll19Al6kDbkwFDp9SvRQDGyLqT0J_RCHIzxKToYF5sdPt3D4kjextU7a2nYVQTQeF3Qjq9ULjNWCg2LvneCJp6WwxeMCGh3RWfn780z8I-A5jnsvJPEsqN3WP5XI5i8EJ5UJX0ic78Ra80URlavuAU_L7_WIM_3sjuobPTJ8rsd_NNj7adLCa8g1fxwijwOZUJ-TI3i5vfHr1GfZHUSfZrHC4A5tUcO300ZvtSB0GYfcGTWQ2jUbzBIsHDiIGU20-sWFZ7xud_oprgK_s3suaQaA8XraDVW0WubatbHtoWoMQfElUTxYdrlLssg_bgr7jiatX7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/028fa17067.mp4?token=linZrbRDeCyPov1ll19Al6kDbkwFDp9SvRQDGyLqT0J_RCHIzxKToYF5sdPt3D4kjextU7a2nYVQTQeF3Qjq9ULjNWCg2LvneCJp6WwxeMCGh3RWfn780z8I-A5jnsvJPEsqN3WP5XI5i8EJ5UJX0ic78Ra80URlavuAU_L7_WIM_3sjuobPTJ8rsd_NNj7adLCa8g1fxwijwOZUJ-TI3i5vfHr1GfZHUSfZrHC4A5tUcO300ZvtSB0GYfcGTWQ2jUbzBIsHDiIGU20-sWFZ7xud_oprgK_s3suaQaA8XraDVW0WubatbHtoWoMQfElUTxYdrlLssg_bgr7jiatX7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و دیشب آخرین بازیِ دنی کارواخال با پیراهن رئال مادرید بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/Futball180TV/90197" target="_blank">📅 20:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90194">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7d995db72.mp4?token=gtMjIv2HEJT3_csXZVBOIP9FPYOybBJi3S1LwbUkYX0nJHgK4RJpfx4BR_zALErGbO6uAaACuDOBR4Z4zUGVdUnD5V1pRzaoGFxo0p3PVnxtsuHDGXQDnzq6Ac0gMunHpweBXIkV8tZQ1AjvkG-nmLKT1JhP-syka2SV48w6S72y74Cbn0SaOvJbHZqaZgV9iSAbUdzMYoqDFO1cXpHsYdVhATY6ikSX8vAPuOfPCCOtRFH60ITHUmnpEfQ6Cialmf7GLRttDBh7GdBkAYj5b9pqficlNFBPNzVFWoB6Y_w92x-3D2PUqoDEPW-bYXoj_mqw9gdBTQ-2_KcpHjeUWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7d995db72.mp4?token=gtMjIv2HEJT3_csXZVBOIP9FPYOybBJi3S1LwbUkYX0nJHgK4RJpfx4BR_zALErGbO6uAaACuDOBR4Z4zUGVdUnD5V1pRzaoGFxo0p3PVnxtsuHDGXQDnzq6Ac0gMunHpweBXIkV8tZQ1AjvkG-nmLKT1JhP-syka2SV48w6S72y74Cbn0SaOvJbHZqaZgV9iSAbUdzMYoqDFO1cXpHsYdVhATY6ikSX8vAPuOfPCCOtRFH60ITHUmnpEfQ6Cialmf7GLRttDBh7GdBkAYj5b9pqficlNFBPNzVFWoB6Y_w92x-3D2PUqoDEPW-bYXoj_mqw9gdBTQ-2_KcpHjeUWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بهناز شفیعی :«می‌گفتم ناصرخان یک کم کلاس بگذار و با زنگ اول تلفن را جواب نده اما ناصر قبول نمی‌کرد!»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/Futball180TV/90194" target="_blank">📅 19:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90193">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
آکسیوس: تفاهم‌نامه ایالات متحده و ایران:
🔴
- تمدید آتش‌بس به مدت ۶۰ روز.
🔴
- هیچ عوارضی از سوی ایران بر تنگه هرمز دریافت نخواهد شد.
🔴
- ایران ابتدا تمام مین‌ها را پاکسازی کرده و محاصره خود را برمی‌دارد. ایالات متحده محاصره خود را تنها پس از برآورده شدن این خواسته‌ها توسط ایران به پایان خواهد رساند.
🔴
- ایالات متحده برخی معافیت‌های تحریمی مرتبط با صنعت نفت ایران را صادر خواهد کرد.
🔴
- تعهد ایران به اینکه هرگز به دنبال سلاح هسته‌ای نخواهد بود.
🔴
- ایران متعهد می‌شود که در مورد تعلیق کامل برنامه غنی‌سازی اورانیوم و حذف ذخایر اورانیوم غنی‌شده خود مذاکره کند.
🔴
- ایالات متحده متعهد می‌شود که در مورد تدریجی برداشتن تحریم‌ها از ایران و بحث درباره دارایی‌های مسدود شده ایران مذاکره کند.
🔴
- ایالات متحده هیچ نیرویی را از اطراف ایران پس نخواهد کشید. خروج نیروها تنها پس از رسیدن به یک توافق نهایی در پایان ۶۰ روز رخ خواهد داد.
🔴
- جنگ بین حزب‌الله و اسرائیل به پایان می‌رسد – به اسرائیل اجازه داده می‌شود اقدامات پیش‌دستانه‌ای برای جلوگیری از بازسازی سلاح‌های حزب‌الله انجام دهد؛ این شامل حملات هوایی و پهپادی به لبنان خواهد بود. «اگر حزب‌الله رفتار مناسبی داشته باشد، اسرائیل نیز همین‌طور خواهد کرد.»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/Futball180TV/90193" target="_blank">📅 17:53 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90192">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mi1nI4Vgkk5WALlpWZnnvmIjuGCAtyTm_XikAzOkn1aPPBFeRSuc6ZyprsNdPggBXFm2Xjqn8WI2vWrdA-QhFeIVFxDneCQ1tcBpu3Geiamb6ni5QcO0u1Bcv-CExv_7F5X7P8j2Q-yxRqHehR0ir2B03PXxaSK32Shh_5vNzLXpMBvA5602GYxOkHdTccR7l7apFmJFqNjAQJ398JsL2_5IQhPqVz3OLTiRGUawtnFFpgNvwJUEldrEpsKZAjattCp1SyWOrvKDV-gB3jmtEEo4e4pJd5VDIzYcv9eGkkUJ9kQSnFw20KTnNNhdrLKaW-gLChOq1wLJj3q4Ll_efA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاب مشترک داکنز نازون مهاجم استقلال و روماریو اسطوره فوتبال برزیل در پاریس؛ هائیتی و برزیل در یک گروه جام جهانی 2026 حضور دارند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/Futball180TV/90192" target="_blank">📅 17:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90191">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXmN8XnJbZv1C5a5GmDwWFDh2x_QFRqK7FL9HhtmgAjicepLALefCXsSPOT0Q2bqQcmQFJtBaQJd_S-TotD-IaJGQIAJt1z4h_XuTvWgdhkD00Jdl3ptLsgbsqFzzl4Nvme3euGnOhi64SxDrxXUxCvW26QdboxCmUPBGvaeGWxlihkJHos_jC5SCVnkOryCVUFavWmX36JkJRV-XvaHQxvWosDIBz2A8bc9wtgbBlkCBHdw7kIj44eBPDaOibpCofgqKR10NBNQ4eaWrvycQiv8Gx8KybsvVYhE7_QWgnhBuKMepikq7nVjjYv8neC1HK-WEvPR_92kOEDLyOf_WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ: خدانگهدار
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/Futball180TV/90191" target="_blank">📅 16:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90190">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67618efab5.mp4?token=R3B3gWh0_OfUyU9C8nWZtZ6OeCBodF7xwuYfn_bdOY7OJKehyJreDtBINXdEcGzrtThjEyKQHUHp4V-hqaKAbhLAntxhI90yrGq6SpKpBrqST-6ZH1tvhTamz35pPwf49ZwvxC5TamUalcnpW3mSrn6bCjknPBNUhv5UV4fFCz5OQHTFW8-uVgsBDxObpY9-5flY-jfJHctMMga1syhppiXkAFmKmT7PBQqCgkTugs4OMJEcfEQ7tT4mJ2Ffe98A8MXein8FM-WA-wVrVhtakWJG3-KLMtgVKx8E7ZkT2VxbNeYLE0JFQaP7Uw_EhsUvncoyYVVGRsNARhZdHzUZz4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67618efab5.mp4?token=R3B3gWh0_OfUyU9C8nWZtZ6OeCBodF7xwuYfn_bdOY7OJKehyJreDtBINXdEcGzrtThjEyKQHUHp4V-hqaKAbhLAntxhI90yrGq6SpKpBrqST-6ZH1tvhTamz35pPwf49ZwvxC5TamUalcnpW3mSrn6bCjknPBNUhv5UV4fFCz5OQHTFW8-uVgsBDxObpY9-5flY-jfJHctMMga1syhppiXkAFmKmT7PBQqCgkTugs4OMJEcfEQ7tT4mJ2Ffe98A8MXein8FM-WA-wVrVhtakWJG3-KLMtgVKx8E7ZkT2VxbNeYLE0JFQaP7Uw_EhsUvncoyYVVGRsNARhZdHzUZz4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همسر حجازی: دامادم گل زد، تیم ناصر سقوط کرد، دخترم گفت طلاق می گیرم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/Futball180TV/90190" target="_blank">📅 13:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90187">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fbdde7379.mp4?token=kBfGDKr1OCwLWoJOKZqsI6hVlttexDrSHdPHKCy0q35LkSko59zE60wNUlr6n-c7t7jh_-gmLdWibgFcKai25lJNEg8iDMPZSc5o-_syWZ_7zuOVdYlpPnnHok7UFovVLnwimUw65A-28wxGXo1a8Wxe5_FYiZdtT6sQ7FDTvVAqmHavc3udJUxeBLHyuzmD2Z6Bd5qE-OmkNxFQay_XEM1ZdRKpMvHYmFjTy66vMaDpXPXNfJd34ZXbL4ij5PSaGkwD11d1Wavg_mGSlnMUsefeCkcC1FrefCwMLC8nWQwFqPZ2gRG2OKWbDfSfb1Zrs9S0ha5DnFDjf-2Bb7NBujS7YVlATmai0hR6Iz_8142ej14KtuKAlwU63Ww6Qnjzs4Oh0pX27zJF8ImQWx9OqDXHSP5iHA0oSonq6wXZDiwICFjDolpDl9TLTvpUJZdLqRF7LNnD5tZtEU6yxSwxMdt4K8j3OYcFsN7Ugsu13skqjWL_OSp9-fygP4f4ZQBBgQkKXX9WGY9WBoNpwY5OucN6LCqNABvxGsOEV0Y-dSgiE2JpUNskssGMB0eU1IOM6Gj64wJZpCtvuYTjxY7iZ-xbu8alursZUJZS1jie9IK9GC3xg7s8t3H3m9aI8FfSoFFX8JBBlXtWU3vFTLVnyEJ9i35U5v2Vm413qZz7m4I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fbdde7379.mp4?token=kBfGDKr1OCwLWoJOKZqsI6hVlttexDrSHdPHKCy0q35LkSko59zE60wNUlr6n-c7t7jh_-gmLdWibgFcKai25lJNEg8iDMPZSc5o-_syWZ_7zuOVdYlpPnnHok7UFovVLnwimUw65A-28wxGXo1a8Wxe5_FYiZdtT6sQ7FDTvVAqmHavc3udJUxeBLHyuzmD2Z6Bd5qE-OmkNxFQay_XEM1ZdRKpMvHYmFjTy66vMaDpXPXNfJd34ZXbL4ij5PSaGkwD11d1Wavg_mGSlnMUsefeCkcC1FrefCwMLC8nWQwFqPZ2gRG2OKWbDfSfb1Zrs9S0ha5DnFDjf-2Bb7NBujS7YVlATmai0hR6Iz_8142ej14KtuKAlwU63Ww6Qnjzs4Oh0pX27zJF8ImQWx9OqDXHSP5iHA0oSonq6wXZDiwICFjDolpDl9TLTvpUJZdLqRF7LNnD5tZtEU6yxSwxMdt4K8j3OYcFsN7Ugsu13skqjWL_OSp9-fygP4f4ZQBBgQkKXX9WGY9WBoNpwY5OucN6LCqNABvxGsOEV0Y-dSgiE2JpUNskssGMB0eU1IOM6Gj64wJZpCtvuYTjxY7iZ-xbu8alursZUJZS1jie9IK9GC3xg7s8t3H3m9aI8FfSoFFX8JBBlXtWU3vFTLVnyEJ9i35U5v2Vm413qZz7m4I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روایت همسر ناصر حجازی از روزی که شُهره به همسرش پیشنهاد شام مشترک داد
همسر حجازی: هم خودم را باور داشتم، هم به ناصر مطمئن بودم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/Futball180TV/90187" target="_blank">📅 10:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90186">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
روزبه‌چشمی بدلیل مصدومیت از اردوی تیم‌ملی جدا شد و به دبی رفت تا مراحل درمانی خود را طی کند. احتمال خط خوردن این بازیکن از لیست تیم‌ملی برای جام‌جهانی وجود دارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/Futball180TV/90186" target="_blank">📅 10:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90185">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4f0bLR5tHw3_hz17rXmJHar1jVL7LgTfySpIl3sz9vhUpasBZoolBRaJWtl-wygmbh6vA_I95ZPrD8-bpN5_WOMtV3K6dPiIUYnveHyaf4_RH50lf5ln6aZWCbpmJrt_xyn2sFWVluOs1ZOgBHNobEXFz2eEpU0vRn0XAYj9qZ6lFxixEEqUaE3EJRp7W25RCAlVleZUfPrjzEyxgMFFILDPn73C_ilBGIfAacz0zMuMDrRWU7hkCBiEqISGNs2YJl2fp1MltVoXXUamUX0NVF46PSgl7eDpig5j8zDUABOEi6SSlQPDh9wSV4p5speh8hBdAq71q_VARAajulhsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت بورس ایران پس از شایعات توافق:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/Futball180TV/90185" target="_blank">📅 09:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90184">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f849fc0fcc.mp4?token=hg76Q247NWy9-v2_INImnIVdLSf8DtTcnVCad7NZ1snHG3NG16DCu7-zfzJviGig2pskNXPnE3n-iGS4bmLciqk1ARiAPJuGfvrE9bWKn5UfGU_vVRWV0PP0Qxrh8YIfBxPvKmg_vjQw4BPpAdFy9volG0DspsiZqVnZBym7P5ItOXV3hqqelbOtJmYsEY31aVkdBVJfRYNWCJgAYA5Fo0QI1C9vLf71UVh0f16pqj7WG4yiCyY3Ll3vOg4kttGG_08uRhjXtaWH69GxFB5QPl26w80-G24KgsSNateLj6sIpJCwJ96wbnNg9apL4VlGVMnI77jAQAbRof1yKz6iVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f849fc0fcc.mp4?token=hg76Q247NWy9-v2_INImnIVdLSf8DtTcnVCad7NZ1snHG3NG16DCu7-zfzJviGig2pskNXPnE3n-iGS4bmLciqk1ARiAPJuGfvrE9bWKn5UfGU_vVRWV0PP0Qxrh8YIfBxPvKmg_vjQw4BPpAdFy9volG0DspsiZqVnZBym7P5ItOXV3hqqelbOtJmYsEY31aVkdBVJfRYNWCJgAYA5Fo0QI1C9vLf71UVh0f16pqj7WG4yiCyY3Ll3vOg4kttGG_08uRhjXtaWH69GxFB5QPl26w80-G24KgsSNateLj6sIpJCwJ96wbnNg9apL4VlGVMnI77jAQAbRof1yKz6iVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداحافظی باشکوه کارواخال از رئال‌مادرید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/Futball180TV/90184" target="_blank">📅 09:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90181">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOkB3uJcjcx05D0BBnTw1HITO0m-fY0wgmvjIF17qCzooByLZjhowRxZdV0N75P9rtE_JR9MMFQ6HFB6Zdh8LRJj4AHjCviWIg6mUOtB9dSPDxW3_U1n4zbpR8CTqgv2R-Jk5mSBlALIfO6bm7hdCBIWsQVMswKMif2ubom6Obljkl1dcrbF4bjW3NCyGW2vw_XQILuLX_tWNoxZCqiOHa1oMSHgRAOwEhLyFi4YAr7RPJcfvUzTmFKnJkTUEl0RypGQN3nvdZDtdQTiSHKipNoTW9XPMLsR-EmozUOZ6_dmVX1r2q8DWVtJOe_JKkQPi_gYzY4LmBpkWBRNvpcaQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
ترامپ: یادداشت تفاهم با ایران تا حد زیادی مورد مذاکره قرار گرفته و در حال نهایی شدن است و به زودی اعلام خواهد شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/Futball180TV/90181" target="_blank">📅 00:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90180">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCpdnitGWtpQl4qrFja6Im07y3lJHp7JLkaEQyUcbY5OF-dnfRgYeinAsM2ltcOeLKLMTyvZhqgGIdJcwgKwMlI2r8ZGvfL-EIwV3LLwOD3jxCK7ZkaDEheb0NZfEWvm6Eg8Jt6D1GXSEAOiunr1bBRTJLwcxtRfMplDJeyh7OY6r-ZIX-V0GNCTW9N-77NlImoKxQEO3d4qN4NNbj-uU6rtq25-OZGYufh_lXTgh0A91xlKhvJp3RmEJPEObOiAoSPgOmJ-WavnlL6vG6rmISvIdCm81n-0ooi3Fo_Q6vpcrzg6FeBx4oJ26Q6h5lOyL5jXaQimD05RxpHgllwxeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تیم‌فوتبال زنان بارسلونا با برتری قاطع مقابل لیون قهرمان لیگ‌قهرمانان اروپا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/Futball180TV/90180" target="_blank">📅 23:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90179">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HClEKZ3wY2Liofbc7x3djd2rbftzgPQXAp95MGO9SYIFXs4ZIGToV_dkacLXYQSW1M1qo5y1nrOe4ZNiCnd3OyBXOiSji4L_3W8Nyx_KV-z2jT2yfe-bHjN0e48BFAUoDVZE3j5nytBn9AxuFDF677MMkZX7Ew_7QapVIhyj9nXue145omcL6KEIxymRNKIQ4j9AffhfczLFzxB8L0Vj0S5ZDC-W8QZ1C_5u-Cdb__ObnC420ZEia7Lilgmd74n9O0OeDoeBm2T3kIq9aXDQRzEHWT3Yw7mOSzcx2fD472l4hjM8t9PamShqVduiJLF72hdj8ZQhj1wWTko07hRu0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار آزمون درگذشت پرویز قلیچ‌خانی را تسلیت گفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/Futball180TV/90179" target="_blank">📅 22:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90177">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b1b20643b.mp4?token=KBUlCVpl7Xua8OBFx6qDSjs-1JXwbTkieMrw17OL7FCQZ9zFByASXnshZSAwJNx7AxF4KbY-PkR4jbcarHesPMO6UeIua3ibWH6b0JDUKvhvX0AlgBchuEozweXsgRVbEpLgQ7tr9DBf7FQRQWfALbzF7zK-A4DLu1-vOytWz5AORatSDIC_kC3a04Y_PLGif1lkfGYk5s-cq-tLAqzUhVHhgEW3KDuLDjVQ_F8TnK9qmFtmBMpNFtMPlNYhMLsIhCjAv7EWmtscLVBBfXV__OVwnUO8Lh_X_ksV72PD_nPW4tD0m8fc4d9UYWVKLm-ZvwM6PGzsGj1f2hvcDqrVmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b1b20643b.mp4?token=KBUlCVpl7Xua8OBFx6qDSjs-1JXwbTkieMrw17OL7FCQZ9zFByASXnshZSAwJNx7AxF4KbY-PkR4jbcarHesPMO6UeIua3ibWH6b0JDUKvhvX0AlgBchuEozweXsgRVbEpLgQ7tr9DBf7FQRQWfALbzF7zK-A4DLu1-vOytWz5AORatSDIC_kC3a04Y_PLGif1lkfGYk5s-cq-tLAqzUhVHhgEW3KDuLDjVQ_F8TnK9qmFtmBMpNFtMPlNYhMLsIhCjAv7EWmtscLVBBfXV__OVwnUO8Lh_X_ksV72PD_nPW4tD0m8fc4d9UYWVKLm-ZvwM6PGzsGj1f2hvcDqrVmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
افشاگری همسر ناصر حجازی؛ علی دایی تمام هزینه‌های درمان را پرداخت کرد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/Futball180TV/90177" target="_blank">📅 20:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90176">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsXmJ3M-SJH8fogI3xOGvKoz0sudfapUBqzE4OgnPamYRCO70vwiO4fb5KiKlzMcKyW1c2NmkjSbx9Fl6wrnCJN3X2Lndh8JtLOHbLozi0eI0ZJS2xwxdwKXPard9_6uDdgdrNsb91QbQJ2hrEK7Oi_iI08x95A4rCSUrQC4tVtzcV7an-VfwjZgZzyUUq6i4cjyhOFYQQeNatc-iBOmIbhiiAxaCk1Ef8quo-x94enU8tmTommP3aPupu7p1d2NJEf-m5-Qgso_qXmRhLSe1fFvgnT5dDoZdXWelhzL5TjDLaqbM4KeEnvItXmEdSU7VraXe04K567rzBURnL8UXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مائوریتسیو ساری با جدایی از تیم فوتبال لاتزیو سرمربی آتالانتا در فصل‌آینده شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/Futball180TV/90176" target="_blank">📅 20:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90175">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fa5fa3b89.mp4?token=oT-_U20h6mLyjHy-rRVXr8-M5rkC44cDfkq2ZhKjKaWa-togSs73O3dY2EG_vPqO8hntrE8DW8CiLiYpt1sFmi6z7Xy62qH_lxsLglxeNrV82aIpXxN-stwqgDczmRhi2VJf2DrF2du2SSL_nB-uG5DT6NPueV8pVYy_UhR5XgtSv7HuUNtPMNnifgwt0U-KzUzJnMtqfWhZ-l1qC1kend1PIQSe_eSOhJBO4EsnVjxKXooL0ggNpoEEqBlZx5r9kjG8u8PWFro35mACzqv49tNqpnrr4Np6H7bASEI4UZR1L6UHxRUY1ylXQ7wp-jnE4J1XeOn9JgnkXwbqb_9i4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fa5fa3b89.mp4?token=oT-_U20h6mLyjHy-rRVXr8-M5rkC44cDfkq2ZhKjKaWa-togSs73O3dY2EG_vPqO8hntrE8DW8CiLiYpt1sFmi6z7Xy62qH_lxsLglxeNrV82aIpXxN-stwqgDczmRhi2VJf2DrF2du2SSL_nB-uG5DT6NPueV8pVYy_UhR5XgtSv7HuUNtPMNnifgwt0U-KzUzJnMtqfWhZ-l1qC1kend1PIQSe_eSOhJBO4EsnVjxKXooL0ggNpoEEqBlZx5r9kjG8u8PWFro35mACzqv49tNqpnrr4Np6H7bASEI4UZR1L6UHxRUY1ylXQ7wp-jnE4J1XeOn9JgnkXwbqb_9i4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهناز شفیعی، همسر اسطوره فوتبال ایران ناصر حجازی، گفت حقوق بازنشستگی او ۲ میلیون تومان است.
او در ادامه با انتقاد از وضعیت مالی در فوتبال ایران گفت چرا باید کارلوس کی‌روش با پول این مردم به سطحی از درآمد برسد که بتواند برای خود در پرتغال جزیره‌ای بخرد، در حالی که ناصر حجازی در آن زمان حقوقی بسیار پایین دریافت می‌کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/Futball180TV/90175" target="_blank">📅 19:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90172">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba990f9ec.mp4?token=tr8ui-v3QcAfI_yNDgNCz9TROV8uCPuTNA-kUuW9bk5QCJC3DPiMkxcpgMJ5QKXv0G4AfooqEigO5_43sjZc6kY3KPIV6zTyeAkjyWmjiHRpfyFgRwMc-CpG1jSixKxCUYTG0u5j4jb-NkdCqYCvsxRZgWjHE3F_madQZMqkgmxwKxXR39faV5CanePUpKC8VgtUcOdxa10TfHPH9eaXdN2YALaYqS-vCHppA25-EaPxLtnDt7mojn8JXjoCkhR_zCTUDDUO46cL-xgHtlbbysgNY7A95r6Je4i2_ZDoHcE63hajXLfs2PIwLslPIeW1R849d_AhwEzS_EOqp5jXvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba990f9ec.mp4?token=tr8ui-v3QcAfI_yNDgNCz9TROV8uCPuTNA-kUuW9bk5QCJC3DPiMkxcpgMJ5QKXv0G4AfooqEigO5_43sjZc6kY3KPIV6zTyeAkjyWmjiHRpfyFgRwMc-CpG1jSixKxCUYTG0u5j4jb-NkdCqYCvsxRZgWjHE3F_madQZMqkgmxwKxXR39faV5CanePUpKC8VgtUcOdxa10TfHPH9eaXdN2YALaYqS-vCHppA25-EaPxLtnDt7mojn8JXjoCkhR_zCTUDDUO46cL-xgHtlbbysgNY7A95r6Je4i2_ZDoHcE63hajXLfs2PIwLslPIeW1R849d_AhwEzS_EOqp5jXvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
دوم خرداد، سالگرد زنده‌یاد ناصر حجازی، اسطوره باشگاه استقلال و فوتبال ایران است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/Futball180TV/90172" target="_blank">📅 18:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90171">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6RQmj7AIQVnisptpDaGRbmtEmNN_C8kxHlXp9ujik_ZR2NIiQNCBsIXDLUNcWSN0uc57h04Ojqb8TntyEi0NVA8H4r_xOByVQuJAnZm-EZ1OXe6WFN2H58h6-VyKeg9-mKgxm5lEAAUDQqesb82msqbmA0oZ1yk2ifJGlV8icCRRL6rgJlnLMKlaW3i3kv1Jno1sgIunlyeB1FQERUiTmb3BacELh3N6z5YYna93ADgGTc4cq4O7OiFCEE5bsPfZb279QeANdnBO97LEVzYRsGEw6H2h8ATo2L3LVc77mfkgeEHVYspTHTcWTX3D538C6-uZj5LP3XrcCIh3GPjiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
تلخ و ناگوار؛ درگذشت چهره افسانه‌ای فوتبال ایران
پرویز قلیچ‌خانی، چهره تاریخی فوتبال ایران و یکی از بزرگ‌ترین تاریخ این رشته ورزشی ساعاتی قبل در حومه پاریس جان به جان آفرین تسلیم کرد. قلیچ‌خانی متولد ۱۳۲۴ و در 81 سالگی پس از ماه‌ها تحمل بیماری از دنیا رفت. او تنها بازیکن تاریخ فوتبال ایران است که سه بار به صورت متوالی قهرمان جام ملت‌های آسیا شده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/Futball180TV/90171" target="_blank">📅 18:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90170">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-WVCMtQq52Dw8Dc7nJO7GJ_ejLyahcJLJtLemRNIFqwXNhUYr_IAvwDxat3aAxXDzRYBAQf6MpAuBp7oVY2JkMUZdqRbtRT_TX7PWPeNh3ZCGWaYWhL2KcbZEvCDnKers_Np_rPvdqIJsn94h1y6bYHugspt61NGQzEYvRr4YqyDAaUr-B8tJwIb0s3uMmma9CzxMfnqke4wm-FyYS9kzaKjfaLTsdDdX8PcAfTg7Ellv-5jFYOM0j2lqLqWKkAI247mGpN9Ls6ceppsUKYvRpDBiPMplva0SmOmRfRc3m9xnJy3twCDetxLtY3pUkpRkL3FISYPtUoCqJ8zeJfrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
عکس جدیدی که ترامپ منتشر کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/Futball180TV/90170" target="_blank">📅 17:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90169">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=ssMexSqNfSdEbkH3ldLO3C8z8lK5UHeDIRHyzIDDyvd2lxi1-jpAaM353hofAnBvNm8vCYq2xUXhCmlCwSsT_ymh_rdrRXKQICb939qwEGuM1sT0N1QcX8liJeJB8btQfdjtriLDtF6ODS5cerzVu9X9IgnW76xL5h4mHTYJ27vdMZD2CCUVU0gWJDvD7xpGPQHt3uLCwfZgOp5BTgMlnPftRhVWptOW2V6uFInIr7lsfyZFrUBrvNlC5_uWKCRX5XoGWCtvQj3FV8U_LVL_XTJgvnI3nAnsVMODpnk9Iy2FQEKAVXJdqlH-CY9wxvhaACOdqxt0oqF8joYb-QPjPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=ssMexSqNfSdEbkH3ldLO3C8z8lK5UHeDIRHyzIDDyvd2lxi1-jpAaM353hofAnBvNm8vCYq2xUXhCmlCwSsT_ymh_rdrRXKQICb939qwEGuM1sT0N1QcX8liJeJB8btQfdjtriLDtF6ODS5cerzVu9X9IgnW76xL5h4mHTYJ27vdMZD2CCUVU0gWJDvD7xpGPQHt3uLCwfZgOp5BTgMlnPftRhVWptOW2V6uFInIr7lsfyZFrUBrvNlC5_uWKCRX5XoGWCtvQj3FV8U_LVL_XTJgvnI3nAnsVMODpnk9Iy2FQEKAVXJdqlH-CY9wxvhaACOdqxt0oqF8joYb-QPjPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پادرمیانی همسر ناصر حجازی برای برگشت فرهاد مجیدی به تمرینات تیم استقلال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/Futball180TV/90169" target="_blank">📅 14:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90168">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5ngzBOJTqXTT44MhBuuYnF8GMQICHNNpdlBtisc0r-1_abVDOKQjmLqbmMVUwPuQUoscemsY11amYMFxGcAFhkn8omtfRtc5AcO8_PpECLGJTI1I1ZvTcSnD_uRMfFqYuF30YH4Ac35lTghHt6hQXE6sFy2KKnsBaxK1jtgwUquk24KWAFcKn4wnPrPhwLCP7Z_5f74M1LHJdsWm4o5Ya0_SQJ5lP3gMB6EHGRuQefZp-V15-DOuCdXgQ4YB12MC1Pxw2NIfOQsA4qInIfgWInZQu4LxdvOSgwV3J0BJjZTXCi_PepEtn5UhUIvsITy4eP8I5hGZaCoTeaCTDyY8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برونو فرناندز به عنوان بهترین بازیکن فصل ۲۰۲۵/۲۶ پرمیرلیگ انتخاب شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/Futball180TV/90168" target="_blank">📅 14:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90167">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/megtbqMqpjBBliaHd5qD8DF0DwKIvZ0UfR0HJXS7GVKZqYz5On2sX-HS-3DMmmZTNjUZGPb2KvSTl36ELROSUk0A1fiEDgCVYnXbbIm1ZYSw-Rz0-NPEie-axOmCWHk8hLYW4Bd5OKe92oY3yXx0Gry-KO_jcWLOFFqO0KI2AVWVnTryk7dCP7by7BFRnY5nMYNzlqEnknn2GcbviBpRvAVzbVyh4WKu0SWp0gqxWhhFXT1gDcI7uWUptMm4PlOqUgfIcPker2sydiR652i0M9ohFssK84FaBvE_4vtfbnkkZ4W0IFrQXoW554YTGGyc_aKcVa2p3zAcoQWWDoCy0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گستون ایدول (روزنامه‌نگار آرژانتینی):
🔻
فکر می‌کنم ۲۰٪ احتمال داره بره آرسنال، ۳۵٪ پاری‌سن‌ژرمن، و ۴۵٪ بارسلونا.
🔻
اگه بارسلونا واقعاً می‌خوادش، باید این رو با یه پیشنهاد قوی ثابت کنه. تنها تیمی که واقعاً قدم برداشته پاری‌سن‌ژرمنه. بهش قول یه حقوق خوب دادن و پول کافی برای مذاکره با اتلتیکو مادرید رو هم دارن.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/Futball180TV/90167" target="_blank">📅 12:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90164">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4bb02d75b.mp4?token=snmVb6XMPcW8zpRkV03uUhja9LcMMELSh39bUuONCA7RHXf-Id-7JBQ2ryxKA0QAAsLJbv7DiOPWADj9pyUkZnoUf5gyjmUTyaVy71mxpRzeUo-1a2cIWZagyxYx6gS9yF6a6QUaFVDCMZgcWWaflADdUlSb2KGTkieYmfKsEUyann8Ks5QIc-seB4HpHcmqS0qKagthJ6aVF4eD6cud02hxfdrtot3u8E1Q0FGCAPrIYmiC0jzZKA2dn5ZQcyEEQ9fRoHzAn-9D1U_7XkpuSvy0JEfXyvh_eudFVb0mKRxHl4jEuJMIgsi3-ZwjJQPOCmXgibmh4E5u5TT2ZFnQx16URgmHv8fdIZP5EhP4CEjO0oFEfZRNRVth7AJBMGx8Fv6RnhxGi02SQZWSVfX-aED8J1M1k-VqmVRDj8Dxv4uI16340dqg61tyRMEIaARwjvDLjKKoYffYogRAqZfKeSrIZCFaMvT7itCkLRnXd-51W_2lqMMQCXAcmeL9X0QeUzepj81LzQ5bS5nlGQN_PyZMY4zPGhXnu3mm8M-daTCrvqyA5Rm17cQ0-Ee1L4FVfSXhMk3CzbN6MV0G688cLQdJ9HsykaANiZXBPJLWhXV8ncaVzeWLRssylHm8xUnIUvM-v5KQu2SVitBjIkVEmyV4ESCvztLmgxkFglVkiVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4bb02d75b.mp4?token=snmVb6XMPcW8zpRkV03uUhja9LcMMELSh39bUuONCA7RHXf-Id-7JBQ2ryxKA0QAAsLJbv7DiOPWADj9pyUkZnoUf5gyjmUTyaVy71mxpRzeUo-1a2cIWZagyxYx6gS9yF6a6QUaFVDCMZgcWWaflADdUlSb2KGTkieYmfKsEUyann8Ks5QIc-seB4HpHcmqS0qKagthJ6aVF4eD6cud02hxfdrtot3u8E1Q0FGCAPrIYmiC0jzZKA2dn5ZQcyEEQ9fRoHzAn-9D1U_7XkpuSvy0JEfXyvh_eudFVb0mKRxHl4jEuJMIgsi3-ZwjJQPOCmXgibmh4E5u5TT2ZFnQx16URgmHv8fdIZP5EhP4CEjO0oFEfZRNRVth7AJBMGx8Fv6RnhxGi02SQZWSVfX-aED8J1M1k-VqmVRDj8Dxv4uI16340dqg61tyRMEIaARwjvDLjKKoYffYogRAqZfKeSrIZCFaMvT7itCkLRnXd-51W_2lqMMQCXAcmeL9X0QeUzepj81LzQ5bS5nlGQN_PyZMY4zPGhXnu3mm8M-daTCrvqyA5Rm17cQ0-Ee1L4FVfSXhMk3CzbN6MV0G688cLQdJ9HsykaANiZXBPJLWhXV8ncaVzeWLRssylHm8xUnIUvM-v5KQu2SVitBjIkVEmyV4ESCvztLmgxkFglVkiVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
یکی از جذابیت‌های فصل آینده لالیگا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/Futball180TV/90164" target="_blank">📅 11:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90163">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
⭕️
شنیده می‌شود کشور آمریکا ویزای مهدی طارمی، احسان حاج‌صفی و شجاع خلیل‌زاده را بدلیل گذراندن خدمت سربازی خود در سپاه صادر نخواهد کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/Futball180TV/90163" target="_blank">📅 11:19 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90162">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbRliL1JXOWT7FjI05Bs8R9YIkqWra05eYge3dmvfWsNQ_TXwssXxql0AqaDgNhUiiqXEBJzy7hrVjl0_3J_1OZUHLsKHHTeI97lH7Hm1gji2ZL03RBRSAfawN10e9ks4U5zKlMFB3COUgGRvm-juPZsEV-AeX2DClnq1cg2M06OTNgtdT3mZ-BhI2t8Yp8GxTB0PTyzHkRSGWY6E3N-Xm5C6xtQ9Cxv96orDXLSLH8GsNtFudK6BbHX3hBO5-NQWF07Yf18DawxY4OJObbtMukZcmzHxbej-aqXB2-hwJpdkWXiwqq6ibY-E6ZjfRpyD-cHjPHRiqp8II2HfwRT8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توخل: این فقط یک مسئله ساختاری برای ایجاد تیمی متوازن است تا پنج بازیکن در پست شماره 10 نداشته باشیم. حتی اگر این تصمیم دردناک باشد، معتقدم که برای تیم ملی انگلیس تصمیم درستی بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/90162" target="_blank">📅 09:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90159">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12eda9dfdf.mp4?token=bZu-WRDfgCTGQrup-z1Xbk1TW9tQKKR0hEKwuizMu5IRPEJFG46Ie18vyUJ1M_lz64DKq5h8oYX_yawTypBYZmtJfgJO3808CZa3qCaOGscJEAima4LSF4d-ccHFz0LHvlNb09qF3cC3zSdbXMjxz0MujCelUjIhm4rFUI5mHLuXtn4d5zO1MPNFu1Y1uZ5svuGu74HybpIAnFaz4U8vPkp8h2wXGxnu57mFb1QLwaQAtuo0onVea-iLefxcA40JWRD9tinNY9DOwX4f7s3MVBZt00ZY2gA2piF2DD8vT-PCHRJOgKuoIU8MEq4nKIVbPiJRQ3gqcszWGabH74iGAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12eda9dfdf.mp4?token=bZu-WRDfgCTGQrup-z1Xbk1TW9tQKKR0hEKwuizMu5IRPEJFG46Ie18vyUJ1M_lz64DKq5h8oYX_yawTypBYZmtJfgJO3808CZa3qCaOGscJEAima4LSF4d-ccHFz0LHvlNb09qF3cC3zSdbXMjxz0MujCelUjIhm4rFUI5mHLuXtn4d5zO1MPNFu1Y1uZ5svuGu74HybpIAnFaz4U8vPkp8h2wXGxnu57mFb1QLwaQAtuo0onVea-iLefxcA40JWRD9tinNY9DOwX4f7s3MVBZt00ZY2gA2piF2DD8vT-PCHRJOgKuoIU8MEq4nKIVbPiJRQ3gqcszWGabH74iGAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت ترامپ در سخرانی امشبش:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/Futball180TV/90159" target="_blank">📅 00:09 · 02 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

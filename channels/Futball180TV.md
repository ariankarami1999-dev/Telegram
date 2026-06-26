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
<img src="https://cdn5.telesco.pe/file/d8FMdeVjuv8LA-TrPQ7By5mi-gnmKO12JacByxiSGIREAuZl3OlK04IMWDx-HoZEd_-0vE5wW5hETgz9GIji41EZDVnR2FVOrPZy70IvNbEFVwTDQPfO7CkY-LkbehH9SwEv7ti9RPtVx-LDdO_0dWWP9bQIbfbUDtCJ-lqmpyiWDkYGMbZ52WPMKlfYtNGn3XMYt-YzZ6d2uXrERmdikaaM_knNDpjcCXfibgqACK9XL9tEgOqZLE0yViOirAroPwjhxQtu2O-cU2KtXn2MPq5ATvL8R4pLTCFW4dLLwUToIgWV-FBKzIqmrkat64yHmpqHnpR8H5U96IleP3o4Sg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 692K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 02:11:51</div>
<hr>

<div class="tg-post" id="msg-96181">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAnMMhkzbSjKkeoWyUgAqDQ_432x6WNEvsAMKR4w4ZVpIqQWRDlRE5tOGS5nII38QEclMMqekKHzXqir8oko1AS_t7h56cqpCHPr0B8qZPD9bnC4yBXk68A7cxHbbVR9UP7XkvwHQ-X5mu8J1rIMHVlDN9UVPJ0iMatm_0OnqrdO-Yn7GariXDzcShH0CrcVjakr034JyUwtqMUUh03g3Hyqh7lTlV66DOqK5uL3j9dRwNBkhQMTnfC1PkB6g3FEywpQo1c-G-6EauTNIqGdTj7NyFWkuybrrhHFz64kLfadNHolgN2gnMnnyW9qSFaK8W4yurgqRpZQpKiM8mshJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب رسمی اسپانیا مقابل اروگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/Futball180TV/96181" target="_blank">📅 02:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96180">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9970f0db9.mp4?token=dWvXomQxBwWCALAQby-6kip1I-2pWuUnYDA-R36kpq18kGxxiN9r61SjWC0JTu35JZoVphXHateqXBDj6N5yqdjj_lDXNwDirZ-YAH21SVzN-rfDpPojK6929a2XFZnqARbd_tU2vOsRnFaFnZ9Gq3xskA-bxXlnCztC8J3d2CmPuZJOM59JOduqNqkJiVe66R1IWF6aTqX2Umv4dxGgTIxWMzmwlT8iLhHUS9fx7f8EppjEVYCY4tjWN8m7yY98o2oRM5HSQ0amSC7dEj3Hi_JnHQ9FyO5S5cqVs981f-qKLsGetgWGTz2oZmJ516kEgR7TjkRNRN3eT1jJLio-qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9970f0db9.mp4?token=dWvXomQxBwWCALAQby-6kip1I-2pWuUnYDA-R36kpq18kGxxiN9r61SjWC0JTu35JZoVphXHateqXBDj6N5yqdjj_lDXNwDirZ-YAH21SVzN-rfDpPojK6929a2XFZnqARbd_tU2vOsRnFaFnZ9Gq3xskA-bxXlnCztC8J3d2CmPuZJOM59JOduqNqkJiVe66R1IWF6aTqX2Umv4dxGgTIxWMzmwlT8iLhHUS9fx7f8EppjEVYCY4tjWN8m7yY98o2oRM5HSQ0amSC7dEj3Hi_JnHQ9FyO5S5cqVs981f-qKLsGetgWGTz2oZmJ516kEgR7TjkRNRN3eT1jJLio-qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
خوشحالی هوادار مراکش از صعود به مرحله‌بعد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/Futball180TV/96180" target="_blank">📅 02:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96179">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92e9b9ed52.mp4?token=C4iA1lWlSqjH2jvPc5QUVFDkPWRkwWeiBvhMdp3wDpf8lPoi40AmXreOZlztGTLrCc4Ks0Tf_rqGj8xykhmhPiq8t8xzkIej8HGjhu64XhiMYNYEMBGU7371nrS2XNPIMrXOcIFMvWXjgEixgoWkfatm-7qMdDzedC1ZnM_Zr_QUxZGYZAOg_hjKaVmqiwMmPsd7VYmEhUZT4MwmVeH-uN0f6qhtVdOmKNmMPJhbQU_S6IAMp0KfhvZV2HttlJSC1xn0H9b26gpj_QkunBGdRLqZOC8VD-L_7vvHPeWzMT54g_5YcP_U0TFf-tV7HA2C1sVTAqRWwkTFTVErxrzniA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92e9b9ed52.mp4?token=C4iA1lWlSqjH2jvPc5QUVFDkPWRkwWeiBvhMdp3wDpf8lPoi40AmXreOZlztGTLrCc4Ks0Tf_rqGj8xykhmhPiq8t8xzkIej8HGjhu64XhiMYNYEMBGU7371nrS2XNPIMrXOcIFMvWXjgEixgoWkfatm-7qMdDzedC1ZnM_Zr_QUxZGYZAOg_hjKaVmqiwMmPsd7VYmEhUZT4MwmVeH-uN0f6qhtVdOmKNmMPJhbQU_S6IAMp0KfhvZV2HttlJSC1xn0H9b26gpj_QkunBGdRLqZOC8VD-L_7vvHPeWzMT54g_5YcP_U0TFf-tV7HA2C1sVTAqRWwkTFTVErxrzniA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
بنظر با این پیش‌بینی، صبح کار دراومده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/Futball180TV/96179" target="_blank">📅 01:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96178">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8F_spiSHFn3-woX2VRSGR3v6tSu6xwazBYfaZxww5Rw98cPHNmL8S-JEbg-UuZCOowWOzcC-HTuhGfDIte-nSzSP8fSUxF_whAY7LAHuFNUUhG8VzmiYoy9vVw5YoYNXHqkVQqDIVdqYNc8rgrBqbVCAWHy6oq3dl3wMQ-q9OWzWNFfZnJEuX-VwU6mtpz7sqR5Q4Ovq_5pXQaTMZaDHqtWvqxMQal50y-920_5-03RGrjWT7tBaK0LAYiig8oPTubcGoUxOFKep6fjaPxBFvC24dsWtfE_Mj5KzfZptnk9zblt775-T70Cro-3gREimtDvB240GucaRAS2SnNtbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب رسمی اسپانیا مقابل اروگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/Futball180TV/96178" target="_blank">📅 01:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96177">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsPl2sWBUiFO6tHvu_rh4uUQHqI7ddo2vuJZXCUXvwAfIzKEjXR2SYC02olqovE1ocfM4InMVHxZ_qyQp4taBFXtPm3ywFh-pAC38Ai9pypnZpimBgbIUyNGFaY9_SLHLZWZOJ_DyKZybXLNMRujhCm_jrFsiBVRZ9UWyQrPDvWTSuvnf15oixox5vnhN64WKqV2eOOv2vz0j9cbPJE_HeOy8q9CdUzxXoyI_jTiSviEZTXdt60tn0dFu4_OMlqS0M_Xf2IaTc3I8DtpaeTDv3GMe9mWbKSR-LsKtYJTg_gSLxdpjuRJetY4A2t3sHNnxyFolM7jKwrrpu9fJ3m0wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🏴󠁧󠁢󠁳󠁣󠁴󠁿
اسکاتلند تقریباً اولین حذف شده بین تیم‌های سوم شد. فقط یه معجزه میتونه نجاتشون بده اونم:
👇
🇩🇿
باخت الجزایر با اختلاف بیش از ۲ گل
🇪🇬
🇳🇿
برد مصر و نیوزیلند مقابل رقبا
🇸🇦
🇨🇻
مساوی کیپ ورد و عربستان
🇺🇿
و برد یا مساوی ازبکستان مقابل کنگو
این همه اتفاق باید بی افته که تو جام بمونن که بعیده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/96177" target="_blank">📅 01:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96176">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbOk_ptpdfd1PtQ3idFnl0gXauhqH1iTSLJiaNeC3yeovJozb3FUdITYfhIPO9YURe-e8seh5SHryUQge0z4tTXy_-2HeNPadlblHgtISaCtOYRevW2qx02UDtLNDVcH7KkxF1jsCKGXcI7ExFrmDA76Y6gH4U4QQVwvR-t9W8tG4BZzX4OKg7tq0ADa8u6EZYp2XeX9w5lJB4O-MVore4wlEa43wejJC2yKe_5XMrRLYbY2gXvAKBArVPg8EkXr9IyEXgtjHWPvpXybXzgGA4_rKeT5TTzXaWP1QL3M8XPa5hHKlRnbq9dtbykFEHBpzzLfo34XH3iA-9OPFJTr2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
ورزشگاه محل بازی اسپانیا و اروگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/96176" target="_blank">📅 01:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96175">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mj72ZZahWwN-9cLGAQV1WQxJVOw4IvvH6I8cTMK1lgF9FEfqVb09_t9omuUjRwWcT1vCqrqf4xrPDmUN7XptTsiLwTcna4qUHtz0eE2qXonPCgXkaeSZXpS-6Rawv00I__d2ggwdw1V1y7zctllPh2Bq-84Y6NYcgNGza4G87rz9rkOhgg9oqH1vCahHdkiL2x8KoQyi0ufkL4LVf2Dx7-6Ab1nccRKzpr1Ib9XEMMb5sE1XcbMLSptVdZkddMfp8c7sSRdxecv7q7oaTYTHNfgIpAGLCA2K0rFJ5K0dw5cXowEhnq0AVhdlOa9JxNNYDugJkYbQWN2FMWMM7nrLWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنگال اولین تیم آفریقایی شد که در یک بازی جام جهانی پنج گل به ثمر میرساند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/96175" target="_blank">📅 01:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96174">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
‼️
دیشب یه زوج ایرانی تو مکزیک رفته بودن بازی رو ببینن که اینجوری گوشیاشون دزدیده شده
😢
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/96174" target="_blank">📅 01:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96173">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea90a3e17c.mp4?token=h06E__9CcIs_xBPSVp_EgI72_hnUdj1nLRJgxnle02idoW2Fy3TclklLMgH5j-L7nsZaiJQMGBiBTvDbv6qRjr03e_dJ9GJC-KcDPEWFIHS_mhfKo1ONcaZBIOrO1jKA6qrTCdDDf900zZw7KjeycHee4xuM4c0O5qNSXYppVDuKnPLin9FWiXwlre45djnPWh3tEi1_cAeZahc662NnYzc3ik0Sol7b7Fane0A-JII8BTm70dhhnL0qjJVrGNYu-J3nfiZzolz_Ii-X-vbClV2u9J55iOPZicpbS8FNDxG9Yf6oJNymagTom-41gAZd05lazU6j46S6qxqsQaMVNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea90a3e17c.mp4?token=h06E__9CcIs_xBPSVp_EgI72_hnUdj1nLRJgxnle02idoW2Fy3TclklLMgH5j-L7nsZaiJQMGBiBTvDbv6qRjr03e_dJ9GJC-KcDPEWFIHS_mhfKo1ONcaZBIOrO1jKA6qrTCdDDf900zZw7KjeycHee4xuM4c0O5qNSXYppVDuKnPLin9FWiXwlre45djnPWh3tEi1_cAeZahc662NnYzc3ik0Sol7b7Fane0A-JII8BTm70dhhnL0qjJVrGNYu-J3nfiZzolz_Ii-X-vbClV2u9J55iOPZicpbS8FNDxG9Yf6oJNymagTom-41gAZd05lazU6j46S6qxqsQaMVNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
تصور بازیکنان تیم‌منتخب ایران اگه دختر بودن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/96173" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96172">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGS8A6fb3-am8g41dRaRI4uExctIpMkw-agOoKtKoFq0KqGj-4armYKXrAEoewjLHy1BZpwmdqWUbK25TYpKwS3FgDP44Tt4m7z3KUfkuGmA4-F5e4Se7P80uQjlwa48fh30UGdZVTocnPCkxQIXKP47Ivn7BIO-gWppYW107ATUObG2OTcWDjnZo7FngKiV8fMwhGyymPq4Vxrxkhk70_RPnoeinq35INrCLLUV_Nwm8IPVpuJK1dWjSgApcxDwuq4ZijnWcrMKDrggDceUGQq5PpNKL8RZN75L_VDBg971W4BrXJ1oVe4XRljDP03RfGgtfuZCZByAMBgKnTNTCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
؛ ریس‌جیمز مدافع راست انگلیس بدلیل مصدومیت ۱۰‌روز غایبه و ظاهرا دوتا بازی بعدی تیمشو از دست میده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/96172" target="_blank">📅 00:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96171">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozuTNizh7S4XOIbOmpCgURlPXv9wL2pbH11QOF5pFIX8l2AYiLCAUkI29NYv2yZUb4llt7l-k5ATYn2eayW4yT0te3SWHx5UF53UmCi_aNBQ3d1soltJ1QbGrnastPa0s5G2DIwnW2q6LtFzW0reReexksocoxr5NKg1A8JghFJBObpa_AzrADhv9ySEZEB4MUYGweK7kZUQQG35WESytD2U4qecdk0RdKTpY5RY6FxhJRjC8X2xHKQD87W0zTS9DmM5MbX--sScX6ImQWdUlCqKOWMymY33EWBvNTjk39euM79AvKlmhYpdLScTPk9TTt8pdxhhvf56vX4Okji6OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
آپدیت نمودار مراحل حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/96171" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96170">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImEatoFKfqu65Ge4uikliIWM0SkcyC00StKyybjDbzRDrTZeNHqBBbBWz-0CSWkJpEhrTjGYpo5UGGH-h4q9S6xwip0sB2bC6lgDYT9wqAiCyldD7icuUYJIC6uNkzdMheTVsiAZSM__-4_-Bnt4lhlWdxdVuDfEMg1QnPMMdvStXwLr5DleGgnpXU1SYybmCe6q6TwhpFpNKbG2u21z9VTnyG4xJ9hTUlEBOFzZyZn-KR1gu-IJXcJZKKxmQ1bykQKLRalppWiwBLocSEOiVeWLs2CTGbtOZt-ShoRCGtxrSsCVv5qCeBTKTUjfhoRWUQXACbwA1O3-dK94n1h3xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مرحله یک‌شانزدهم نهایی جام‌جهانی
🇫🇷
فرانسه
🆚
سوئد
🇸🇪
🗓
چهارشنبه ۱۰ تیرماه ساعت ۰۰:۳۰ بامداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/96170" target="_blank">📅 00:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96169">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3_JTn35-3K2_UDA07AqNs7A-dUcdrAh1crjGPXYbSYp7jxzmeL59oW4LcW0whpnFzGrpQx0JFmL_BKbYqtsEl3ZLL1mtYtKuuoYtJwqQ_LCOpeTs4k9txGHVoarKAmfFIA0fixjvrdNO9ny_3KVsLmiUpGBUwWUikp4bQNBBylqprGZ5_NHtlQ3PlkCGCZVGjYeM6UVE4yYreayAOoFNekl-EosE_-hmrQxJ8Sn9nkunG_zQJBPySrT9yekXjARODwYfk8bG-aSIwHs9ETXW3rbVp5xa86UDWobQQJIPdda9Ten9cYEJqMktoyen0WooQvAqaaKC5G491ibQEz-8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عثمان دمبله جایزه بهترین بازیکن زمین رو دریافت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/96169" target="_blank">📅 00:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96168">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjFE8MLTbnW1OZGVFUfVSqOS-kKXQ80pplhkwE3k8s6qpQD2aQJ6edgPn3A2E-83Bce0FXjQB-dEIy_skxHPSqj_5SKDK7ZOw0jvltRMjD40FBLViGy9BFMeYuWLvyQwopLxRZ9_4wdmCyPE76E9AR_2yDjNoaueDbMBUNA2J6wtbmp9DagKFxG2H7W7b_ymHtV2yWL9JLotQNKKE6eFuJGBHlS_sCDWTKWo2XDEo7bXgL4YEHVRq3KrX2WInB7e41UG1pUO2LBi8SQbjhQjtFXPQ-Xgw7uIbAq7yl0f5bT3ql_W2anJgHu2BuqD1Agw8X3tQfBhkl1hYXcAGWBLyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مرحله یک‌شانزدهم نهایی جام‌جهانی
🇳🇴
نروژ
🆚
ساحل‌عاج
🇨🇮
🗓
سه‌شنبه ۹ تیرماه ساعت ۲۰:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/96168" target="_blank">📅 00:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96167">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری؛باراک راوید به نقل از منابع آمریکایی:  ارتش آمریکا به اهداف ایرانی در منطقه تنگه هرمز حمله کرد.  @News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/96167" target="_blank">📅 00:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96166">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇸🇳
گل پنجم سنگال به عراق توسط اندیایه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/96166" target="_blank">📅 00:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96165">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdFK7if_rV0GX_wfMxeK6xRlyrZxfUiteIugtVMpTDQywvlRtznEGO5IAxQiFvf0ZeTRichbfcOoCxRc6Uf9MUC2SBhht3QQ-C4WC7bqYp-1u9tp3elchTzjZMII_dGkYITRdQWm4LnNxZ-Lzj7pVgwUsxGL7NpJLVFqMQBFo_xrOQGMpPrbhrygbYZyGloYI0av2BGBm5FpvtZya2HH79eEV-9M5Vaj1xcljH-R6zaUD81e_7SAsYgomqcxDYvJm1tmczhelz7YRlRKr6dV0ShcLKVtxZNjcz8oGGHR5h-q3yWJ6Ee2M8qDM9Tp1SLUsdKFOJu1hAJ4zu_-_poegQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|گلباران وایکینگ‌ها با درخشش ستارگان پاری‌سن‌ژرمن در جنگ صدرنشینی
🇫🇷
فرانسه
😀
😃
نروژ
🇳🇴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/96165" target="_blank">📅 00:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96164">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/96164" target="_blank">📅 00:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96163">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QUSgaTBxKUD6XYApV0GOzlkm-L3jolT0slVu2PdKoqL0Ca_A3k8hOuyKT1PNRu9V6O7SsNduLWKBaceG_uAaiO23_f3vOflMb4BDJmkCoFFnFuULVqa6akDz6UkU5NbY1Lle8CfNcKtGlbz_gzKO6c3MhAYHcWv3cDzfyiaBgl3oee8N1ACOU-gSt_ukSO_e9VejrVoHGdepraiuGwTYQJ_XFzQqhtoS81hfKnhmQQncJh9dR9Rpkm5F9m9_dkwZB-LZfpj4O01VtbFcuHsYR60QLpsY0CLTJidSwsqf3zAxy-Eg029eP8pNycQAzoYxY3nkN2fhSVGj2d-rr5l-dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/96163" target="_blank">📅 00:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96162">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🏆
پایان‌بازی|گلباران وایکینگ‌ها با درخشش ستارگان پاری‌سن‌ژرمن در جنگ صدرنشینی
🇫🇷
فرانسه
😀
😃
نروژ
🇳🇴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/96162" target="_blank">📅 00:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96161">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دوئههههه</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/96161" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96160">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فرانسه چهارمییییب</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/96160" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96159">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گلگلگگاگلگل</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/96159" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96158">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5a0f064511.mp4?token=l6TVqUM8lbm34Md5YhevUXHhnliTRP5Zi_BqhVmsnGc6AVFazOwtcfVzyddIxEHYbKesSnhjXCMN7dAOAQj5hUeJsDZs-74h3eoAzMyFtxC7kVgKsuBpBQ36P7_zJiqpqr0rCbq6n5u7GmYPR2zrLMQdq4L8MYMi2h4SCjBVqFK7n0L6mYhpYJTf-xt7FEZYkzh-hgKwO2h5jTD9__SpysDgb3QFv2OsLSFOTCwMOgvDHpCv_QY7RzWgzf_BDcvI7vNfFU74QQv-mTPcK4-r1MGsmENxZeue1Be4DxuhiV7sGubyRXyr4MN8blDK6Htw4wIr9JxxGh5SvNB1s9vF2kjzCcsPb0O5fr14rtUpgzcEzpgX2umASqmx2Lu6WvgeyHLCi65y-e24rWBieUNaapQ2_OBgcMgtexfVdC3RpfWRV691SRKgrA1f3mTpSrijAp5qaZLG_8iX3kLUhmOJiMmpL4vsRegYqDVmMrlpVpGnAABx4ysMob4phOJ7Zt3ZcAuzXpBfWgDX_fbr80ccXUmNPlbejNMcNi4zk3ARpYoB9s0SJlBSQqc20nv_4Sq8DYaBziAh1at7rcZ_P9awKwGT9ucjk3thGX9ltOpGYUgQVQl0lCO93ALaqXrm3eC1eF8vKVXXFJbPo4KBwpKdWh9WcoGVaxCzpab5Kt9IJ90" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5a0f064511.mp4?token=l6TVqUM8lbm34Md5YhevUXHhnliTRP5Zi_BqhVmsnGc6AVFazOwtcfVzyddIxEHYbKesSnhjXCMN7dAOAQj5hUeJsDZs-74h3eoAzMyFtxC7kVgKsuBpBQ36P7_zJiqpqr0rCbq6n5u7GmYPR2zrLMQdq4L8MYMi2h4SCjBVqFK7n0L6mYhpYJTf-xt7FEZYkzh-hgKwO2h5jTD9__SpysDgb3QFv2OsLSFOTCwMOgvDHpCv_QY7RzWgzf_BDcvI7vNfFU74QQv-mTPcK4-r1MGsmENxZeue1Be4DxuhiV7sGubyRXyr4MN8blDK6Htw4wIr9JxxGh5SvNB1s9vF2kjzCcsPb0O5fr14rtUpgzcEzpgX2umASqmx2Lu6WvgeyHLCi65y-e24rWBieUNaapQ2_OBgcMgtexfVdC3RpfWRV691SRKgrA1f3mTpSrijAp5qaZLG_8iX3kLUhmOJiMmpL4vsRegYqDVmMrlpVpGnAABx4ysMob4phOJ7Zt3ZcAuzXpBfWgDX_fbr80ccXUmNPlbejNMcNi4zk3ARpYoB9s0SJlBSQqc20nv_4Sq8DYaBziAh1at7rcZ_P9awKwGT9ucjk3thGX9ltOpGYUgQVQl0lCO93ALaqXrm3eC1eF8vKVXXFJbPo4KBwpKdWh9WcoGVaxCzpab5Kt9IJ90" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇳
گل پنجم سنگال به عراق توسط اندیایه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/96158" target="_blank">📅 00:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96157">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">تجاوز سخت و خشن به عراق</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/96157" target="_blank">📅 00:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96156">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گل پنجممممم سنگال</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/96156" target="_blank">📅 00:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96155">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7vdl8Tl1Y8AM3ag2ztmmrtBdAFZeXJ6LQFT66zetJ7himNbQcelHHzcGiGKi9iDBTat1k9NUZDKMxLFM-AzYzU06aoQdX6p569ZN1B8ljCukmubiLXH2Cor_STqhsyVSEGt2fG37xIzTMZrYQihoaIRpQuu6L8JwMxJuTYwdj3UqBnJvVcD7CAQiw8tlUFlazvAfXIHnEwELMHOkr_Rm1R7P99RjgSGJKg7r4iRdPFpTDXRLa8Sbw1EzMcK86A1NJ2Vktcp6x-rOGe21k_DVaiE10w1JILMwE5zwR1-3T_Vj87x4kAiElfJdAbbtkIQDg1BLzdqmEmL4BSlBh1iZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دو تا لبای همو ماچیدن و حلقه انداختن به هم محرم شدن.
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/96155" target="_blank">📅 00:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96154">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9f26eabfb4.mp4?token=LNZCwLCHmWu6KKdf31F8Igq60yLL2jsDODsDKifTJYnrQzbKks-F_ei2XrXDet1wFNauJq0kzO5g4Zn0LoGNNVkAhHGF-v1MkCGp1ma-uaermZVPt3lkpz2W75wf-f6vAk5iSpkO5SgS0etlEN1CMHzDHxYE29CUO8F6nnHCEIW9Jo0o-lLRfPgQtPjxcOjtiAqeIEZTY2FMG9qWi8VgotM9Olu7A0jQR1suybAwDrkdgZTTS3eD-3_8VE8knfFDsl9cBLkIMCwAomXLkRCUyKpoD1yFu5upmehx4g_TYnDJHDLCJZVEqpoI7g_HZN-BvBYHe-e9pOg-d8ti_UkmUKPVgThF5GvCvJHRusf6Ob5mjzIImvrZP0wAJ5cjm3FwORC79vap77vp0Qg7MXxpO7TaCS02APzIuWmDuMvv-lYY4GdghgOWsPgiVdnUgNHRqYdIsupDmvZzJt3NeZPRRtlLp6ElxH5GNr0x3UOsyY1rDHMcj7W_ug6ihrV3UbjzNm6kXYq3D3lwoWf4gia2vzu1XjLuqlamH5IJ_0k5KvOX8HFLkDNZ5pxMArvXSSOrOhpOMQ8zE3Kr1juyaSQeTifm340F30ZUtKOhMl5-hYpEZff5FSRx_K7nOMeTV4vHHmvIocG4cw-tIn3mSRaKSz4qJGTUn7nNdx9JHaqUje0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9f26eabfb4.mp4?token=LNZCwLCHmWu6KKdf31F8Igq60yLL2jsDODsDKifTJYnrQzbKks-F_ei2XrXDet1wFNauJq0kzO5g4Zn0LoGNNVkAhHGF-v1MkCGp1ma-uaermZVPt3lkpz2W75wf-f6vAk5iSpkO5SgS0etlEN1CMHzDHxYE29CUO8F6nnHCEIW9Jo0o-lLRfPgQtPjxcOjtiAqeIEZTY2FMG9qWi8VgotM9Olu7A0jQR1suybAwDrkdgZTTS3eD-3_8VE8knfFDsl9cBLkIMCwAomXLkRCUyKpoD1yFu5upmehx4g_TYnDJHDLCJZVEqpoI7g_HZN-BvBYHe-e9pOg-d8ti_UkmUKPVgThF5GvCvJHRusf6Ob5mjzIImvrZP0wAJ5cjm3FwORC79vap77vp0Qg7MXxpO7TaCS02APzIuWmDuMvv-lYY4GdghgOWsPgiVdnUgNHRqYdIsupDmvZzJt3NeZPRRtlLp6ElxH5GNr0x3UOsyY1rDHMcj7W_ug6ihrV3UbjzNm6kXYq3D3lwoWf4gia2vzu1XjLuqlamH5IJ_0k5KvOX8HFLkDNZ5pxMArvXSSOrOhpOMQ8zE3Kr1juyaSQeTifm340F30ZUtKOhMl5-hYpEZff5FSRx_K7nOMeTV4vHHmvIocG4cw-tIn3mSRaKSz4qJGTUn7nNdx9JHaqUje0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇸🇳
گل‌چهارم سنگال به عراق توسط پاپه‌گی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/96154" target="_blank">📅 00:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96153">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سنگال گل چهارممم زد</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/96153" target="_blank">📅 00:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96152">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a56fb088f1.mp4?token=qiw5sOE0VuoVX6wD7Y7gQP-g-xIDJa9fjk9PScP1yPX2tCLDwTwoI4cweEXdO4sJldbo734x7IVtwDEHngu_Gnf_-HiXVK-CCcrtTb7DRhe_RvqfA-c_oFVldtIUJitsmZs9hfxnQ5sWxSEQpATRUXwu2rQqiI4tDlMnyBGi3-mHYGzxYJ5NnlL1zLTrzkEuG99ExGzu5G9956QGGKfq190LZfweLkRsAvkrN8K4Jr91pYYyfgFSCCcmx2TLDbbG5OwXo7d4tb5Jq-75MjU_U5om9r6r2VD9gikRm9h-pVQk7F7y-MqV6gsK1pVn6IHNHVrIZCxN_u3WuxNWa9Rd-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a56fb088f1.mp4?token=qiw5sOE0VuoVX6wD7Y7gQP-g-xIDJa9fjk9PScP1yPX2tCLDwTwoI4cweEXdO4sJldbo734x7IVtwDEHngu_Gnf_-HiXVK-CCcrtTb7DRhe_RvqfA-c_oFVldtIUJitsmZs9hfxnQ5sWxSEQpATRUXwu2rQqiI4tDlMnyBGi3-mHYGzxYJ5NnlL1zLTrzkEuG99ExGzu5G9956QGGKfq190LZfweLkRsAvkrN8K4Jr91pYYyfgFSCCcmx2TLDbbG5OwXo7d4tb5Jq-75MjU_U5om9r6r2VD9gikRm9h-pVQk7F7y-MqV6gsK1pVn6IHNHVrIZCxN_u3WuxNWa9Rd-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🔴
کنایه‌های تند کریم باقری به پیمان حدادی و بازیکنان پرسپولیس: بد بازی کردیم و باختیم
با صحبت حدادی شدیدا مخالفم. در یکی دو سال شرایطی خوبی نداشتیم. مذاکره با اسکوچیچ؟ این رفتار فقط در ایران است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/96152" target="_blank">📅 00:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96151">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a09e259859.mp4?token=k9CA43Ycz7IEHEugJlC8qiRINe3HnJPwtzN5RUEY8j4KSnWL81vZxxbdLQs3qUPZpnvmv6MltwDGIopaqLMsqhWOlENFYTpZRyiYN2pNqQTbSrcUmsjdHF8_FbHw6HWQgqZ4LW6OHtYnsOOSrjQrK7MNgCCxJJeXEhQ8D9f55cj8yYv4vim4_MM_tKxwXiv0Jgn-SjRJJxhcTQ0OkIk73sikmSfRM01VWmw6HpgUzcxl5eINrKBDsb_MoBykThsysF2NzqW7qUuo9HPDRBPINZnZxcH8muSLQJgPw16sHAb1C4T5pR4vWKMpAKvorCKXInHJ31ckL5Fx5Uy7l8Ping" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a09e259859.mp4?token=k9CA43Ycz7IEHEugJlC8qiRINe3HnJPwtzN5RUEY8j4KSnWL81vZxxbdLQs3qUPZpnvmv6MltwDGIopaqLMsqhWOlENFYTpZRyiYN2pNqQTbSrcUmsjdHF8_FbHw6HWQgqZ4LW6OHtYnsOOSrjQrK7MNgCCxJJeXEhQ8D9f55cj8yYv4vim4_MM_tKxwXiv0Jgn-SjRJJxhcTQ0OkIk73sikmSfRM01VWmw6HpgUzcxl5eINrKBDsb_MoBykThsysF2NzqW7qUuo9HPDRBPINZnZxcH8muSLQJgPw16sHAb1C4T5pR4vWKMpAKvorCKXInHJ31ckL5Fx5Uy7l8Ping" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
واکنش میثاقی به باخت پرسپولیس: مدیران پرسپولیس ابر و باد و ماه و فلک و خورشید را دیدند تا این تورنمنت برگزار شود که شاید سهمیه آسیا بگیرند و بعد به چادرملو باختند که این تیم حتی تمرین هم نکرده بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/96151" target="_blank">📅 00:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96150">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ea98176deb.mp4?token=movXN18faMWKeXGlNx8C9BPQnTYSt5WnJCzSfnoqwcrGG0BaLoeb4RBFiQa3Q4M06MxOccQ3HZoxTLLXL4TOMf_mgTHvzAgSyf4ZPWkREs_9b1FRluGGz-0s0P9x8raQb8zB0R7-rlBLJFhK3KU5mTYjDyzU4zHGzl-VHwQ5Wr2fa2YfMoTlXEgILJE08aVkc-tfxtdYpYm4u4WJ1pUI-bFFNdrJHsHmIsY_fqBgaKluNkS_lAvcnfMx98njESpv5HicHc0VCsiX02fDQBIdv95zoLHObCkaxK4WiiuJ46S4-Be8w2DSJYwEH9Jk-vtZwkRZCxh4aY-cOFN7Wj-urx5mdxvivYNXAQxh_pYXaMvqgtwkNmlbeb6LyMGQqtXcyde8cuAexTJ0uG4iEZRNJhF4vQ1_9wNg1SL3iN9LBA3jNPU_Zm0siVc1q6CbwaQ-HwJO63e9EkueN7wsT1sfGAkuk1OfrCFR-4PqAl22jxKnG6ePaue1WizIBPNVrex9tG9fOdsb25TimuEpFnLrgZHe1ethx5p4n373XeG2A5__C7ravlKAjexbgbyNDELWmpFKYLFPvoxiEBppDQQ8sCrCg9FH2XIt_qwibFWarPQ-4YqC4gULdvkMPmhxThlnXFVccbJ_L0d5gXsc-AdEcjbDE_6PN0CZM-0XWnI3WjA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ea98176deb.mp4?token=movXN18faMWKeXGlNx8C9BPQnTYSt5WnJCzSfnoqwcrGG0BaLoeb4RBFiQa3Q4M06MxOccQ3HZoxTLLXL4TOMf_mgTHvzAgSyf4ZPWkREs_9b1FRluGGz-0s0P9x8raQb8zB0R7-rlBLJFhK3KU5mTYjDyzU4zHGzl-VHwQ5Wr2fa2YfMoTlXEgILJE08aVkc-tfxtdYpYm4u4WJ1pUI-bFFNdrJHsHmIsY_fqBgaKluNkS_lAvcnfMx98njESpv5HicHc0VCsiX02fDQBIdv95zoLHObCkaxK4WiiuJ46S4-Be8w2DSJYwEH9Jk-vtZwkRZCxh4aY-cOFN7Wj-urx5mdxvivYNXAQxh_pYXaMvqgtwkNmlbeb6LyMGQqtXcyde8cuAexTJ0uG4iEZRNJhF4vQ1_9wNg1SL3iN9LBA3jNPU_Zm0siVc1q6CbwaQ-HwJO63e9EkueN7wsT1sfGAkuk1OfrCFR-4PqAl22jxKnG6ePaue1WizIBPNVrex9tG9fOdsb25TimuEpFnLrgZHe1ethx5p4n373XeG2A5__C7ravlKAjexbgbyNDELWmpFKYLFPvoxiEBppDQQ8sCrCg9FH2XIt_qwibFWarPQ-4YqC4gULdvkMPmhxThlnXFVccbJ_L0d5gXsc-AdEcjbDE_6PN0CZM-0XWnI3WjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇸🇳
گل‌سوم سنگال به عراق توسط پاپه‌گی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/96150" target="_blank">📅 23:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96149">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d1e0f39ac4.mp4?token=O6sNf7Zs0QPn4LaAspq2vAJrm_uC1OjZU3e3G5P0f3D1Azdq_bhZVNL8Bl6lYQ5wO3WdB8oNSJMm6K6Y9zkD2Cc0d8-WRD1QfzGyGLn59iDjvdF77-U_CLZJpuAXM_sfORKzXhPS4J1objR3OFfqXJA4BElBuZXbHJUenLpkhm_KM6oC_hla7QpG3yMMkGCNLnzm8Nr3jjLYXUqINOob_SeQdAiVI76uZsOnB730VpI1D2wM8xwGzbV_pfi5ZBgbsMAYKCRSugVXoOKjvdWqt0BEC0wFPm0nFzzP6tBoQGwpTYpu-MQfE87G8Rhw3zgzqGWaJXlJUVUOrvi6uBqknCfxx0PDUH9PHedLImBds2ztiBCZJ2SO0FXZwBcNjJyT8K04NbNO1Qudr9J1mibC9NW91MsctQ2BBvBi6xkxh1qbifhmBv73YleTxgMzNIxM4DfidlpHuEoinfOzXnlz2kVmgerVNPI0lWy_K7B8W9Gy7A670CLZuDmBO_asY5P0tmdgH-f-LatbTqAvn6vIAKU7vkcVLMQ8EgfQkChVyLVbW1XAF1MOp_pRA4pxurh0O43qEQ9XdETu-sgtXAax1pEHXeN9tSYMN_ulpynNRkX0pYs19R27Z_S-WxUuceBURG-yQT7g5saRu1QEtFolLF_Kmar4f4T4SHpHg9rZOdc" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d1e0f39ac4.mp4?token=O6sNf7Zs0QPn4LaAspq2vAJrm_uC1OjZU3e3G5P0f3D1Azdq_bhZVNL8Bl6lYQ5wO3WdB8oNSJMm6K6Y9zkD2Cc0d8-WRD1QfzGyGLn59iDjvdF77-U_CLZJpuAXM_sfORKzXhPS4J1objR3OFfqXJA4BElBuZXbHJUenLpkhm_KM6oC_hla7QpG3yMMkGCNLnzm8Nr3jjLYXUqINOob_SeQdAiVI76uZsOnB730VpI1D2wM8xwGzbV_pfi5ZBgbsMAYKCRSugVXoOKjvdWqt0BEC0wFPm0nFzzP6tBoQGwpTYpu-MQfE87G8Rhw3zgzqGWaJXlJUVUOrvi6uBqknCfxx0PDUH9PHedLImBds2ztiBCZJ2SO0FXZwBcNjJyT8K04NbNO1Qudr9J1mibC9NW91MsctQ2BBvBi6xkxh1qbifhmBv73YleTxgMzNIxM4DfidlpHuEoinfOzXnlz2kVmgerVNPI0lWy_K7B8W9Gy7A670CLZuDmBO_asY5P0tmdgH-f-LatbTqAvn6vIAKU7vkcVLMQ8EgfQkChVyLVbW1XAF1MOp_pRA4pxurh0O43qEQ9XdETu-sgtXAax1pEHXeN9tSYMN_ulpynNRkX0pYs19R27Z_S-WxUuceBURG-yQT7g5saRu1QEtFolLF_Kmar4f4T4SHpHg9rZOdc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇸🇳
گل‌دوم سنگال به عراق توسط اسماعیل سار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/Futball180TV/96149" target="_blank">📅 23:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96147">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گللللللللللللل سنگال سومییییی</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/Futball180TV/96147" target="_blank">📅 23:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96144">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سنگال دومی هم زد</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/Futball180TV/96144" target="_blank">📅 23:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96143">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55ee125817.mp4?token=JvpOuJQfgMsjLQRVRmomcDtBBxTS-S1KWBwajpeSpDbF9O5787kgU2Galo1nJ_vsQykIykRREuOyOVTWOnDK4PwbCOhTjRYG0QIZrE7ZDFAHJnL5wzaF1HEQnWY3Uti5YyqcBhkU_KvJHFB1tH1lsrV7idfHmFZt6kboZx_aYbr0D9kpllPYxChpI9PxEchqtv1Jx7uMd-Ypajsd9mNFShfzGIxYPu6sYaGo1mVHasQywG12gYYnmObTgFDEeJGTeKhz5gJzVitiK08ZyXr52i9_13AnKN_o6TSIAUu8OVrvI3E2hvIxPgpX9iQK0Tbl1-sqrJD4RgcC50ywT2Cf6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55ee125817.mp4?token=JvpOuJQfgMsjLQRVRmomcDtBBxTS-S1KWBwajpeSpDbF9O5787kgU2Galo1nJ_vsQykIykRREuOyOVTWOnDK4PwbCOhTjRYG0QIZrE7ZDFAHJnL5wzaF1HEQnWY3Uti5YyqcBhkU_KvJHFB1tH1lsrV7idfHmFZt6kboZx_aYbr0D9kpllPYxChpI9PxEchqtv1Jx7uMd-Ypajsd9mNFShfzGIxYPu6sYaGo1mVHasQywG12gYYnmObTgFDEeJGTeKhz5gJzVitiK08ZyXr52i9_13AnKN_o6TSIAUu8OVrvI3E2hvIxPgpX9iQK0Tbl1-sqrJD4RgcC50ywT2Cf6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
حمله شدید کریم‌باقری به بازیکنان پرسپولیس: خاک بر سرتون. لیاقت آسیا رو ندارید بی‌عرضه‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/Futball180TV/96143" target="_blank">📅 23:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96142">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
⭕️
حمله شدید حدادی به بازیکنان پرسپولیس
مدیرعامل پرسپولیس: این چه نوع بازی کردن است؟ مگر برایتان کم گذاشتیم؟‌بیشترین قرارداد را دارید و فقط دنبال اسم و رسم هستید؟ گاریدو، کارتال، وحید هاشمیان همگی مشکل داشتند؟  ما نتوانستیم چادرملو که سه جلسه تمرین کرده را ببریم. بدون سرمربی هم باید چادرملو را می‌بردیم. با این وضعیت بازیکنان باید بیایند فسخ کنند و بروند. قطعا خانه تکانی اساسی خواهیم داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/Futball180TV/96142" target="_blank">📅 23:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96141">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پنالتی برای نروژ</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/Futball180TV/96141" target="_blank">📅 23:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96140">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
فوووووووری گزارش چند انفجار در سیریک، استان هرمزگان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/Futball180TV/96140" target="_blank">📅 23:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96139">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پنالتی برای نروژ</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/Futball180TV/96139" target="_blank">📅 23:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96138">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">نیمه دوم بازی ها شروع شده</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/Futball180TV/96138" target="_blank">📅 23:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96137">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
فوووووووری گزارش چند انفجار در سیریک، استان هرمزگان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/Futball180TV/96137" target="_blank">📅 23:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96136">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❤️
💙
پایان بازی پرسپولیس 1 _ 2 چادرملو
⚽️
گل‌ها: محمد امین کاظمیان( 27) برای پرسپولیس/سیروس صادقیان (56) برای چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/Futball180TV/96136" target="_blank">📅 23:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96135">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
❌
🤩
#فوری #اختصاصی_فوتبال‌180
🔻
اگر اتفاق خاصی رخ‌ندهد، اوسمار ویرا سرمربی پرسپولیس طی یک‌هفته تا ده روز آینده از هدایت سرخپوشان جدا خواهد شد. اوسمار بدلیل مشکلات خانوادگی و البته درخواست حقوق بیشتر نسبت به فصل‌قبل، موانع مهمی در مسیر تمدید قراردادش گذاشته…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/Futball180TV/96135" target="_blank">📅 23:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96134">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dd73927f8.mp4?token=BJnf2rPfoq5Lz2W2NiTxScPDiSI_Cq7q2IVW_zkUZEwDQTxoK_VuCaVm-G4UT9OVrnRbqe-WdaOK9s6Ap8Nc1MQJtKHSo_Y5IzcjAFRTzOv5Q7gFg1b-YqWzVqGPaC0mhgAVL8w5gq8q92inJ1ysQmx22yNSve4nsndOBV7CBs-QM1Xt50HGc2Vj1laHOutiKhppuOHqckl-oDY75H1oWGiUIIi6-TXgxaNLCfm0K0oX7eU_prnx8WWxmIBWYYoMbWQHuKRD-JSNqI5KXMoqAYeg3st5qWPZq8-zwqoHMZx3wuN8Tbo1_YZnkwlxEJyT-ExLF_FILqc60mE4aeyuaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dd73927f8.mp4?token=BJnf2rPfoq5Lz2W2NiTxScPDiSI_Cq7q2IVW_zkUZEwDQTxoK_VuCaVm-G4UT9OVrnRbqe-WdaOK9s6Ap8Nc1MQJtKHSo_Y5IzcjAFRTzOv5Q7gFg1b-YqWzVqGPaC0mhgAVL8w5gq8q92inJ1ysQmx22yNSve4nsndOBV7CBs-QM1Xt50HGc2Vj1laHOutiKhppuOHqckl-oDY75H1oWGiUIIi6-TXgxaNLCfm0K0oX7eU_prnx8WWxmIBWYYoMbWQHuKRD-JSNqI5KXMoqAYeg3st5qWPZq8-zwqoHMZx3wuN8Tbo1_YZnkwlxEJyT-ExLF_FILqc60mE4aeyuaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
💙
پایان بازی پرسپولیس 1 _ 2 چادرملو
⚽️
گل‌ها: محمد امین کاظمیان( 27) برای پرسپولیس/سیروس صادقیان (56) برای چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/Futball180TV/96134" target="_blank">📅 23:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96133">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mH58lxztJ9-Aws7qDXfKEbZz5HL59mF16H89fJNtxhkIpx9WMpJHVeVMEMsaP8apdHS9jtGOPrRnD81qPqkpHX4HSJs6wM-t8JYNswACkcTDaIAFAOQVhKwqItBnNuqSqGwFCI8NIcGFJ3FKIWwSjZmPPklFaxWt2RKqSjCxZRrY_86Rrb0CbjQAniH-ePZ8wp4dXJBQhZq47VbHw-_UDYV410dV0ONAGFzaKW7n7noWBq8J_AUiBnLztZK4aw8vhOxM_flZjiVPogY1k72RFqwHekLi4mP7HjxyCBhwpuQZBjPx_H-_d3-vWYGkhELARyMPWpE-ZACaZWkqS7QKhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/96133" target="_blank">📅 23:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96132">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❤️
💙
پایان بازی پرسپولیس 1 _ 2 چادرملو
⚽️
گل‌ها: محمد امین کاظمیان( 27) برای پرسپولیس/سیروس صادقیان (56) برای چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/96132" target="_blank">📅 23:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96131">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❤️
💙
پایان بازی پرسپولیس 1 _ 2 چادرملو
⚽️
گل‌ها: محمد امین کاظمیان( 27) برای پرسپولیس/سیروس صادقیان (56) برای چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/96131" target="_blank">📅 23:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96130">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇫🇷
گل سوم فرانسه به نروژ هتریک دمبله.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/Futball180TV/96130" target="_blank">📅 23:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96129">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">توپ طلای دمبوزو بدین بره</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/96129" target="_blank">📅 23:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96128">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">چیکار میکنه این دمبله
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/96128" target="_blank">📅 23:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96127">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گللللللللللللل سوم فرانسه هتریککککک دمبله</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/96127" target="_blank">📅 23:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96126">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0786fc77e5.mp4?token=KHVgyZ4ooyccQTIBjsmsfW-uC4-xna1NT9GdOXf_iV-Ja0af7AQkpaD2e5mWu57TOvE4988-mahn-vfNh_DOFPtPS8l-2SAbt6jZqExnitN41tmcnIEorN8DtpGv8OH5N04x0e938ZoEHhylPsseBWPa_Tj4O794lgiGgebPB7aL92MZLdn1IBxde75EIxvE4UiK5i9dY39x8XTGF92-XY0Hu0GoQilyVdgu9QV-UHCKIV9EMgEkh753_KnYOSGymzLgQAQfoN_bTX5W0qigPONV_0ifqNIOZRTYZ_-rndzMncc15QFkZYq08GjIJ7vZIP0AU-7MNoAlz82hc298-n_b8kudpqfPOFINh86gg2qfEvEe41SO_r49aT8F_bTnMTcymd5YWzbwkxNmkebJOac2s_sfT8LBbVKMw76DZsXg6Wn5M1cbeIlyWjV-3hKCPfkjZr71ySGJ93ybPl1Wq5nrry5YWmVKwajhUegojksgGkQOubqemsFM4cZohvk30hssBTvRSw5j4H_Ik6bdMy6gFvy_KPd1TBcuvjduhzwKpqLD06X0fitmiUpRGqeZBU3kIC7u1iZQzAM-ER8tA_1TMmw6Y0QVGhwpUHQxfn49w_XyYu6Qyb1sAewTysLm-S2TW-7sZ5EUcx3AfMtMF8MVxwnIsZRaYLKYxH6OdLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0786fc77e5.mp4?token=KHVgyZ4ooyccQTIBjsmsfW-uC4-xna1NT9GdOXf_iV-Ja0af7AQkpaD2e5mWu57TOvE4988-mahn-vfNh_DOFPtPS8l-2SAbt6jZqExnitN41tmcnIEorN8DtpGv8OH5N04x0e938ZoEHhylPsseBWPa_Tj4O794lgiGgebPB7aL92MZLdn1IBxde75EIxvE4UiK5i9dY39x8XTGF92-XY0Hu0GoQilyVdgu9QV-UHCKIV9EMgEkh753_KnYOSGymzLgQAQfoN_bTX5W0qigPONV_0ifqNIOZRTYZ_-rndzMncc15QFkZYq08GjIJ7vZIP0AU-7MNoAlz82hc298-n_b8kudpqfPOFINh86gg2qfEvEe41SO_r49aT8F_bTnMTcymd5YWzbwkxNmkebJOac2s_sfT8LBbVKMw76DZsXg6Wn5M1cbeIlyWjV-3hKCPfkjZr71ySGJ93ybPl1Wq5nrry5YWmVKwajhUegojksgGkQOubqemsFM4cZohvk30hssBTvRSw5j4H_Ik6bdMy6gFvy_KPd1TBcuvjduhzwKpqLD06X0fitmiUpRGqeZBU3kIC7u1iZQzAM-ER8tA_1TMmw6Y0QVGhwpUHQxfn49w_XyYu6Qyb1sAewTysLm-S2TW-7sZ5EUcx3AfMtMF8MVxwnIsZRaYLKYxH6OdLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
گل اول نروژ به فرانسه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/96126" target="_blank">📅 23:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96125">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6bac1b0776.mp4?token=FSvXNOKvmsUyzy99XqfxnowKyILDr3PBa2MQ4YDKny-L-FJYZpStgZZ40Y5zh4pW6lI4RkKTetnt8Unyz8rU3dFs62FmQhG28q5_-Y6b3JtXsHcqBaskVuA62DfsoHHjgQMa7brD4YsN1Rwra7GSuTIN6I5FLYoiI-Y3lAPc4Oo5KK3R1I4VLV3HKujWlY5HAdPYtssv4q8zOitPZdxwkGNaXQUrVUk70SxLsQqejG9P2vh5W4y8uQBEZQ4ccgedDPUDR0H6uCtg5tqlB-p2NLqHk79QZrGiJsSAADtSBNylpg937Lh7-xHjoRfsyh91z-tZSZY-CBnlgIcnF61gdVJyQq-Dn55ZmjWit6SBSugoL-1ToIlKmRctRdghwUBfQKvPicErOV8satou4E2MWupR0o3ZXpXAjlf0zZRNs7m6kiPfmxMu6kA-HD9aGXcar2LGs6bFLtsIu9xziAvzYWiDBFt-jPhBCYBOQJ3nfIRDADNtqMwByxUfuq_PQcvzDewjacqeZwNd3OGnv_5KbOmOfhIJ5P-ln0xyCsvWxVMUVTrl6OBmJWers3CbTEOTeXf0ylExFccU1A2H5CvBnP7P8h8nUzS5RYWeaD_pvsDU8XAc7Km1eyTo7-s3LNbd1PCQ1x7eBNAFt9BV8dK-Br8NPaka5qYAwtYbAfULWUU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6bac1b0776.mp4?token=FSvXNOKvmsUyzy99XqfxnowKyILDr3PBa2MQ4YDKny-L-FJYZpStgZZ40Y5zh4pW6lI4RkKTetnt8Unyz8rU3dFs62FmQhG28q5_-Y6b3JtXsHcqBaskVuA62DfsoHHjgQMa7brD4YsN1Rwra7GSuTIN6I5FLYoiI-Y3lAPc4Oo5KK3R1I4VLV3HKujWlY5HAdPYtssv4q8zOitPZdxwkGNaXQUrVUk70SxLsQqejG9P2vh5W4y8uQBEZQ4ccgedDPUDR0H6uCtg5tqlB-p2NLqHk79QZrGiJsSAADtSBNylpg937Lh7-xHjoRfsyh91z-tZSZY-CBnlgIcnF61gdVJyQq-Dn55ZmjWit6SBSugoL-1ToIlKmRctRdghwUBfQKvPicErOV8satou4E2MWupR0o3ZXpXAjlf0zZRNs7m6kiPfmxMu6kA-HD9aGXcar2LGs6bFLtsIu9xziAvzYWiDBFt-jPhBCYBOQJ3nfIRDADNtqMwByxUfuq_PQcvzDewjacqeZwNd3OGnv_5KbOmOfhIJ5P-ln0xyCsvWxVMUVTrl6OBmJWers3CbTEOTeXf0ylExFccU1A2H5CvBnP7P8h8nUzS5RYWeaD_pvsDU8XAc7Km1eyTo7-s3LNbd1PCQ1x7eBNAFt9BV8dK-Br8NPaka5qYAwtYbAfULWUU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
گل دوم فرانسه به نروژ دبل دمبله.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/96125" target="_blank">📅 22:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96124">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گللللللللللللل اول نروژژژژژ</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/96124" target="_blank">📅 22:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96122">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گللللللللللللل دوم فرانسهههه</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/96122" target="_blank">📅 22:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96121">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گلگلگلگلگلگلگغگ دبل دمبلهههههه</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/96121" target="_blank">📅 22:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96120">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">عراق اخراجی داااددددد</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/96120" target="_blank">📅 22:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96119">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گل اول فرانسه به نروژ توسط دمبله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/96119" target="_blank">📅 22:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96118">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dca6328400.mp4?token=myewQoUEoH8AVyfTnrcbUtUsJyiSnwHRetTC6vqQSXGJWBjLRMN7096PH5HBE-tZQxaLCqYIzrlb-Yb49QpIMMg6Qb-10QiYKyze0abD-WrFO6L0bNWQHBATEFwujqQQef6d9wezYKgGPuXjdaHscS-EmZ6bCKXWC0xR7iqcT12lKnWvd-qa68R6ZBWd6_hwESDGgKbBss4-vn4kociKu2oLRWmcIMyPGMczEt1Y99-V2Q7I0QdmIlxSCtjsAhlSHqnAWRGhDu4nm7nLAubfacS3oG5Yne11ROmLXkZJTt1YixFWwjy0IGZD7u7Ib10PU29j3DOp4u6VBlLzJRvkbawdVkKPA9I77XGjnd2AnIJhXtWDIy37061lpx-SxMyixVFiWGFxjW-s0FVas886RZFoaUUWb36jzhoaVG4sbecX6GucY-sW5MWXECCp8kdtYnsJH49VZGLnf6NADnkMfly8aO1iFOoY22YJsxmeICTpq-5nGDZVezoiKc9EiWiCqSYINE4LlzxcMjaSdVZ2haHES9HRbOx7lb0_xsg0U8BP0S5S3YkUpI8wkb5BWKpzRaB8td0xt_ZoELudmlGSeKr6OeOlkivRPcYKXPNGj2sJx5fK8GUKOjtsDJtfoUq8i3xinRkduM5R-_K4WVqvnrG_n8IE6ycj32kxno9C47c" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dca6328400.mp4?token=myewQoUEoH8AVyfTnrcbUtUsJyiSnwHRetTC6vqQSXGJWBjLRMN7096PH5HBE-tZQxaLCqYIzrlb-Yb49QpIMMg6Qb-10QiYKyze0abD-WrFO6L0bNWQHBATEFwujqQQef6d9wezYKgGPuXjdaHscS-EmZ6bCKXWC0xR7iqcT12lKnWvd-qa68R6ZBWd6_hwESDGgKbBss4-vn4kociKu2oLRWmcIMyPGMczEt1Y99-V2Q7I0QdmIlxSCtjsAhlSHqnAWRGhDu4nm7nLAubfacS3oG5Yne11ROmLXkZJTt1YixFWwjy0IGZD7u7Ib10PU29j3DOp4u6VBlLzJRvkbawdVkKPA9I77XGjnd2AnIJhXtWDIy37061lpx-SxMyixVFiWGFxjW-s0FVas886RZFoaUUWb36jzhoaVG4sbecX6GucY-sW5MWXECCp8kdtYnsJH49VZGLnf6NADnkMfly8aO1iFOoY22YJsxmeICTpq-5nGDZVezoiKc9EiWiCqSYINE4LlzxcMjaSdVZ2haHES9HRbOx7lb0_xsg0U8BP0S5S3YkUpI8wkb5BWKpzRaB8td0xt_ZoELudmlGSeKr6OeOlkivRPcYKXPNGj2sJx5fK8GUKOjtsDJtfoUq8i3xinRkduM5R-_K4WVqvnrG_n8IE6ycj32kxno9C47c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول سنگال به عراق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/96118" target="_blank">📅 22:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96117">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فرانسه اولی رو زدددد دمبله</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/96117" target="_blank">📅 22:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96116">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گللللللللللللل اول سنگااال زد به عراق</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/96116" target="_blank">📅 22:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96115">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">شروع بازی ها
نروژ و فرانسه
سنگال و عراق</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/96115" target="_blank">📅 22:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96114">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqJASjRc0G_7wy6F1LfRGXBcJxCv019XlvcDk7L-HZMsf1qlGU43u2Awsnr-hAXOND_IRQ3esVj-Rm5CxDoin3D84J_y9McVRSzJkx7RzpmZu-ZwirF-Z5enWGenrNHoBHdjvcW_-8iq9_WzEO9z0oBusYeLKSfiyRe6jhv_B8bOgy34hIdreY5Fs28o0V16Zqp_mD2LSRq9R9xlRyo-t9l6jVFwMAcMjid3B2eYm6zMJlqskKhP-Upfo5iB4hLqo17W2nMcmajXXTI5YpSBziadbVcA2XYBSAGDgQZxUav_QWebKtbIXio27M-ClXiGr3XweIUwNiXlyPgSyHBZ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کن 15 دقیقه دیگه از این قاب جذاب سوئیچ‌ کنی رو اون قاب زشت و تکراری جام جهانی.
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/96114" target="_blank">📅 22:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96113">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/814f149c24.mp4?token=dn08eCI7db2S7-mapth74SVlOAwAJpxoqqhbVep0izAGg6oNKjewc9IBIN3T2jEFKcb8aJ5RmdFXJrJOU6Fvs5uucCrqWFi52IkuhvCG6JZd0qA2SVlVPYVVqdcVUIwuMmKe5f6rf9oOCnT_sm1JckcoGkWFLbyZ_ocrgCzP_55_iH9uXkU84I57Bg_oqYTgP0LJ0YkFgAKjhBWHFWjRTqs-Jg2itrZvAV5v57CLb-yNZhlb3URtJA2afjZc0v47rs019yeUuHNk3j41RtUXAs-3npP7PU_iLIjqThH2UsRQyfm3eG-B4cWL24sp-WfvGLDMp4tygIiKEHjj53RcLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/814f149c24.mp4?token=dn08eCI7db2S7-mapth74SVlOAwAJpxoqqhbVep0izAGg6oNKjewc9IBIN3T2jEFKcb8aJ5RmdFXJrJOU6Fvs5uucCrqWFi52IkuhvCG6JZd0qA2SVlVPYVVqdcVUIwuMmKe5f6rf9oOCnT_sm1JckcoGkWFLbyZ_ocrgCzP_55_iH9uXkU84I57Bg_oqYTgP0LJ0YkFgAKjhBWHFWjRTqs-Jg2itrZvAV5v57CLb-yNZhlb3URtJA2afjZc0v47rs019yeUuHNk3j41RtUXAs-3npP7PU_iLIjqThH2UsRQyfm3eG-B4cWL24sp-WfvGLDMp4tygIiKEHjj53RcLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤩
گل اول چادرملو به پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/96113" target="_blank">📅 21:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96112">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b610b221.mp4?token=W9AjyscdJryL-iiJTsSQBXpoi3bPhEZZR5FqWbES3wFBl8AjvWVmdGynQL7WC-0m1MtliWSxx9M4ROnLM2VfVlxd8ujngbWAPBQNGwQqrNe3-5w1XVD-LsSxlRJOpXZgmUS2YUfVMaHzUcReQrbQFueSCphm5nHPKT2e2RVnP75a-VQJqtUCIOftp9hWBAz0xSbuRJE-DC2ZcXc7pGJ93kaXJUcyBCkSbW1A9E68JqZALqb4C9LyiAMfmEeBo0qytMbBdowuqcM7qGN7NZ_JnqinLMgy1gUK83x8uLvT1qVDYt28bJ30CR5oJcLu8BSlfb7zyO1K_O8kWKexMUvl0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b610b221.mp4?token=W9AjyscdJryL-iiJTsSQBXpoi3bPhEZZR5FqWbES3wFBl8AjvWVmdGynQL7WC-0m1MtliWSxx9M4ROnLM2VfVlxd8ujngbWAPBQNGwQqrNe3-5w1XVD-LsSxlRJOpXZgmUS2YUfVMaHzUcReQrbQFueSCphm5nHPKT2e2RVnP75a-VQJqtUCIOftp9hWBAz0xSbuRJE-DC2ZcXc7pGJ93kaXJUcyBCkSbW1A9E68JqZALqb4C9LyiAMfmEeBo0qytMbBdowuqcM7qGN7NZ_JnqinLMgy1gUK83x8uLvT1qVDYt28bJ30CR5oJcLu8BSlfb7zyO1K_O8kWKexMUvl0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادار تیم ملی اسپانیا واسه بازی حساس با اروگوئه آماده میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/96112" target="_blank">📅 21:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96111">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMWUI330AA2tFW2Wpd5R18aGtlmwJmSmaAeklJ9Tc1zMlF5736HxprGrPnnD8ErmjN-cYbQ6NWdZxaxG5kKgSDnIJpVHyswL3sHo5VvRuSXutgaJ3Yx1HuZNQC3iexXjucX0R1ni4oZg_3Jlt--YqVxx1_WJKuyFvrWZd8DXVUvjkHL5PxHD-05kyvPQ3uZoVBVnmoSVwpqfrFkeExvu1Tm7j_l8p_9OyLc0Qln5Cx-0KFq05OXfmcp-3Ythh6LVK8xTQqqnC3_Y9KPNMYsUAR5gw7-dp72woIJkFhpj8vFT8Dqyv34NnviYSixWOXstV1faTLoqA7PEBPGyf6FBCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آرسنال در حال آماده شدن برای ارائه پیشنهاد دوم به نیوکاسل برای برونو گیمارش است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/96111" target="_blank">📅 21:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96110">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0GrYdVzH0SPa5bTtEqbL59nSjZWohGAeGoITM-E1j7LH2rxijAfxRkwYEq_MXsmKJDdy_yaShFzppVPsIWCU7UPzsJHzGOUyROF4LaMsna6zFoDfZ-elBqGPS85Hd38Z4eIiXZ2XUy2vTLuE8cydceOFEo991DZ2-KBP-fKVQlK6FVuRhCG1yQhYAJXx24g7FwnneWXkQ6dJi3hDq74_5MYCOZA91ekAmFya6MDBpH8KBZmSu372za8lhfTWbfpQH-7MHpwV5SXdV9zGY94VoXjiGT-z_5YeC1-gwOseG_X0U4aSsV8Qcx4oapcnSmC9sVPYvXY1G0KTuSNaRuaUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
ایران - مصر | نبرد صعود
دو تمدن بزرگ، دو تاریخ کهن، یک میدان سرنوشت‌ساز…
این فقط یک بازی فوتبال نیست؛ جنگی برای بقا، افتخار و رسیدن به مرحله بعد است.
ایران اگر این بازی را ببرد، صعودش قطعی می‌شود؛ یعنی ۹۰ دقیقه تا یک جشن بزرگ ملی
🇮🇷
🎁
شرط رایگان ورزشی
💰
۲۶ میلیون تومان بونوس
🌍
فعالیت در ۴۹ کشور
📡
رسانه بین‌المللی
📺
پخش زنده بدون سانسور بازی داخل کانال تلگرام
📅
ششم تیر
⏰
ساعت ۶:۳۰ صبح
⚽
ایران vs مصر
صبح زود بیدار می‌شیم، چون بعضی بازی‌ها ارزش نخوابیدن دارن.
ایران برای صعود، ایران برای افتخار، ایران برای تاریخ
❤️
🇮🇷
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/96110" target="_blank">📅 21:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96109">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9dqNa8RSiimuo3COOJmDcz9iPg-qdBGl9VM5ybv_L8Ou7OqKVEUUDKXcv2zidtU6ycdekZdVKKky0rHiSoUpWKD784p1xafeTTuwNynCX_c_VrKrfaDWGRFjfPcTnnxSmzGdPbd4kcQNxDcMjULjKZvDNrO9R14AWCsqb40udUUekwXP-Ot0kLZ4ULzC6Cv8yGoqYKEQhcW4P0XEbc7a3rowx4HGJebuFsqgbAM5MY38rV2T-SpXwwJUAQRoroovDnsREt9PEA6DlLXGApD-luQoq7lF_Kz4UOQGbuzX2Lf--gY1lLZOde7CSKEHD5HTjGADV-EP-P-ukw7sfq3YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رئال مادرید از فسخ قرارداد دنی سبایوس خبر داد.‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/96109" target="_blank">📅 21:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96108">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpHk8EOKpEQHoQzQLQejpVfl83D5-DRMcvI96p1tgVE35fWgx-WmZlDpLeDzxasBZvX5ceXV3JnOp73LwGvadV_Fbes56JgPbxcuFYfOHI4hrzb6lQvTR4YzxwpFDN9vE8ekimQxhUPpJDcopVAPl2V-TRg7iwWZaO6wCVXrMxOLvikDViYz2yuqsWzcaShiNf4urNbi3H-mQ7sbrbhFjdWlRXBRF7XC2tBOQEI8b1nMrxPqUHi8gM6lk79-6MRlpIucYAHH97CQdaWmGZKUzD01_6FjaQ3o1gv1Sfb6brmBiRSx-eACTID3LaIvix4X9iL-F9rhoXIYUKK1GAzDdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/96108" target="_blank">📅 21:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96107">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0QJcIWciH7Ah_oHW2JBpDdwjoThzMDdw34hOyhlzCKYXWdVoutjItV--dFvnD3A02GhxyyTawzHKiQi3hDXRdI0vQhYkLl5aV5NCpkY_z9MyvGJYgqIJm4YP9bHxlFFA64s5lqYIbTh6RbYHrM3sHDJu2Z3Zo83QxkR8vSD0Oofj24FbVDq9bdS_v5W__8F9OVtXBYDl1PeCFUVUc_Zb5QVNCtF9aUIbvYsq2fNf4guUzKP1QzWKvzZbgnWQ5VJ3-rjkYou5MV9Q8kSNpc3Rg-hLcUAeUlj7Q6o26sJrcpMGDJ73TduFST1JsjcwOgil7tuvNPPS_p5kWmC1DhMbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل موی جدید پدری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/96107" target="_blank">📅 21:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96106">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOuphPhKqg-t8REMk4re9fqtfztfU1aiWuFUcm5jCjxp_uAf2owuPaaplVqi-zOdbL1YlcznD-N-14GRda1bpkX63A2F25iaOFst39GbGHsani1rmhR9yPpSajh9xJUHEU2sDZbpNe95Wmc-UVrq5pS-xZDv2SD6Drum1GEcZqHAXIXUnMCMO1NSyLpv_0ZK9xAGctNORoXA0rZsF9rk94ig3XbZPEnPjBf-Vio0KszDMdzoqvruqHD_T5sB7zu1vcoadkBx-ioKdQfHjLhdaTXZicD2Fd4EjAHQiqY6Jmc88R_ZfgFvuHD7gcah_StjzlHmD-lNarHoIjpiCz4oKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥳
چیزی به شروع بازی
ایران
-
مصر
نمونده.
🇮🇷
⚽️
🇪🇬
⭐️
با پیش‌بینی این بازی، هم
۲ برابر
امتیاز
می‌گیری و هم وارد
قرعه‌کشی
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/96106" target="_blank">📅 21:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96105">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔥
🇫🇷
🏆
🇳🇴
تنها 60 دقیقه تا آغاز جدال تماشایی وایکینگ‌ها و دیکتاتور امباپه؛ از دستش ندید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/96105" target="_blank">📅 21:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96104">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Alx0Hf-hURh820FlPZFLZTxY_LBtAkboqaIrsRlPK8oKtKb-ph2uaQiYQhTNk38qG61d56j9AwrQ955B89tWNrNi5x7B8Sr2LK81H29PbZMXMdfKS5R1CU7mdCsbj0KtiUoqTSMWKj11NTxIGUloILPbuhsAxNrXK0oZDIcxzChEqI0ejitfZxr-0BuXr3THOPXLDeriU23Fcs2SB6zxgBWgO98YXH02RZxe2Pik7QmlsLiOOUMDdtz0gc2fFJ51nMYh6qzE030-6av-U6YiMwnV4HDYhMGvkg0HkRXD09mIKZUufM4x1YKDdnupjIj8WC_fEp-DrDl-ZvhEuhiIgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇪🇸
#غیررسمی
؛ به ترتیب از چپ به راست: پیراهن‌های اول، دوم، سوم و چهارم بارسلونا برای فصل ۲۰۲۶/۲۷
⁉️
کدومش پسنده با ریکشن نشون بدید:
اول
❤️
دوم
👍
سوم
👏🏻
چهارم
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/96104" target="_blank">📅 21:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96103">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🏐
✔️
ست چهارم ایران برد.   ژاپن
2️⃣
-  ایران
2️⃣
🇯🇵
25 | 25 | 20 | 23 |
🇮🇷
19 | 19 | 25 | 25 |
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/96103" target="_blank">📅 21:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96101">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XMuhokp29SERbN56Xq44D6orjy8RVGC-usjOdqCBfsVY95Y8k1WEzTo0dOkuBs-ppHHMnMFS8ZMcLo-275N_8sfbXSLlJh5ULLWy06cYS0lv6ZeXBcAG0E3e3S3uV04g7Sc1g7q3_ikW_l9SAdjZA0mpd7oCiujZ8JDeI31HDG8twuVVBn4joweWNnz9deS1itM2N475nmgy96QSQp_UgFwBWnSBw1JsWu5I6Atrpzd5FtiqjLrk5RfMAliqg_M6GJ2QAJM5T4FslircdZJpReie82k5ka9h7rsLtbpTaCyVsXvX_7qD7ilVlBi_BCjUTDW1LcCMcIO4ZbJmrdY0Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eIw8oXDJychXXI-W5Bao5BhqklYsWmPciFK9QDSWWvpDC96ZeO2IWZJeVnwcuPYTAwHruEGj8QqaK3_7G-Bahtf6F78xytMNbKbfSGZoehztvaLJfUUnx_YfZSCYTq3AS4q-_NSrej5W_1nUOTSUttndKP2eAh46uCcO43yIngaq3GMXGDfoSHCpI-rF0fdkWprWqNvOTDJ6XHKHpqduk2yFmilnXqB_kIL0tVEVlAK7su9QSoAlUUkHgbRizoW0d3S1xWQvfF9zSbSpzT-79IN4e26hoKqIPLPUR236G6Fhb70DxrhrIH6UvQ05ylJMHblqmNgX1s5Tm_wc96q73Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🇫🇷
🏆
🇳🇴
ترکیب‌رسمی دو تیم فرانسه و نروژ با حضور نفرات ذخیره وایکینگ‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/96101" target="_blank">📅 21:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96100">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8c_GIofPj5ee6uPQRJ49mQ6bjv5J6K4bNYFkHF8V2owlkPr-RrncSaWNzJAj22HR3YGBRrbsz-C7QRnPAm_GFQ6dcB61Dn8ryzAdwKWIM0EtDSI6DYu6g-w0ECumTnGHgzC15udvx0Kat7uO3cwe2LHiNXFSBuFrVyRaINfxN4lk1Vbo1l8O1b9Xt27gCIwNnU71GaXoN8SPaQpB4UNZq-w3hyx_X1Wh4SiptRwZiJmOvL36krUL7LJTkGqp2ABEwcYqO6J4ob2XHhX6AiRPk2Y2emKDbntrtSxL0u0wuMTobHEmk3JM1a2jY1JeHIJ7cAM5tiWh5mbp1HMc_N1Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇶
🏆
ترکیب تیم‌ملی عراق مقابل سنگال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/Futball180TV/96100" target="_blank">📅 21:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96099">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGyrIvokg3wK_IEwXmTt9nBuE8f9uPnpO5kBPQWKmQJTGIa9fsVwgbF4uhyG12mEql19b8MdwnNSk3hw7TPyTz9sYYIwolNduiR8aGNGmfF2EI0rdOaa1A8wTxxxh_mvVoF5fwNy9s-mYDzfMR48GO-vWtpZDAN9EWLmCvIdI3H4MVqwZbNPaNe1ffVEeqqc52X7hhPeqT9xohlwoKOiuKfVe-hGrCMjQFCyf7BeSrd-btWIa1GxUcgoAZNuMrbTisnqfUinNR8cLZP4VhIVBV2aVD7z0vgmF6vGYc1y5ezehZGMKcLW5qdXYkU4UURw4Czgw8zD2z8Rw3hDpN7drw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇶
🏆
ترکیب تیم‌ملی عراق مقابل سنگال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/96099" target="_blank">📅 21:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96098">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc25ce70cb.mp4?token=NcSJxlu3qFP-ZC-OmpDjgKA8QC7I8uIOQSUB4ql19JABIT86TtGyC0f9IHHcqszKpwrsvxVD8XNIupq_NOlrxMvuzBlZvBhhc0BfxmZvVjPfTyCaipBfxqeSqy0W3xghyQYoUOHA1AwI13MqDFZdr5KcO3kRev2jpnjr7wumoS2fRbS0xUAVeAtqYnHKdvzcXpyCkuAbFKGs8OvU4x3wF5hh_OJXckZrGPGUNQylPR7qmIqQyJdI4SGmMJlnK4AJHi-VYwLl4sUB15GuJgbgCWBd9S5mDLvbjKW0C0gtiEkD3Vy8l-Uwcx4rsG3_uyWVcLXiE7ujvqaO8xoViO84YRL-3_rawA-v-cZM5jSf6mJu-NzQRdBop3GDwu5BE8xmRqj9zHnufA3XvBXV-8toPXEAGaD42k6eVUUg9SO3hbJoF5S0GpJ335ldMJBQ7N5riUlKM6UaoKuY75Osns-VqVkm58YMozGKid-J_CFBldzcSnYYXBhcyotDqkP1f6QeCgbvKNocOFryB-p7z3DHpXJyVKrhwnfHq4HDZDoJkDWlBDSfbu5ttY-507xUK15Rm8Q_jwqAfFN3r8lsll3SkxVi02AGDjk-7qpfeE_ZfApHaO0XDSh7X4iDZAFK-ssszTNkcGedtfYelnaiQP9Zeh9FX_igxpRjftlb4z9jhIs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc25ce70cb.mp4?token=NcSJxlu3qFP-ZC-OmpDjgKA8QC7I8uIOQSUB4ql19JABIT86TtGyC0f9IHHcqszKpwrsvxVD8XNIupq_NOlrxMvuzBlZvBhhc0BfxmZvVjPfTyCaipBfxqeSqy0W3xghyQYoUOHA1AwI13MqDFZdr5KcO3kRev2jpnjr7wumoS2fRbS0xUAVeAtqYnHKdvzcXpyCkuAbFKGs8OvU4x3wF5hh_OJXckZrGPGUNQylPR7qmIqQyJdI4SGmMJlnK4AJHi-VYwLl4sUB15GuJgbgCWBd9S5mDLvbjKW0C0gtiEkD3Vy8l-Uwcx4rsG3_uyWVcLXiE7ujvqaO8xoViO84YRL-3_rawA-v-cZM5jSf6mJu-NzQRdBop3GDwu5BE8xmRqj9zHnufA3XvBXV-8toPXEAGaD42k6eVUUg9SO3hbJoF5S0GpJ335ldMJBQ7N5riUlKM6UaoKuY75Osns-VqVkm58YMozGKid-J_CFBldzcSnYYXBhcyotDqkP1f6QeCgbvKNocOFryB-p7z3DHpXJyVKrhwnfHq4HDZDoJkDWlBDSfbu5ttY-507xUK15Rm8Q_jwqAfFN3r8lsll3SkxVi02AGDjk-7qpfeE_ZfApHaO0XDSh7X4iDZAFK-ssszTNkcGedtfYelnaiQP9Zeh9FX_igxpRjftlb4z9jhIs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤩
گل‌اول پرسپولیس به چادرملو اردکان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/96098" target="_blank">📅 21:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96097">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZzk8Jw5DMVbONB9zr9x2Ej9rvzAcokY4MUrYECab3FYm-dXsEStC3nhzmWL0-s13IceSYLER7Q_51akR4YgnU3tZo2M5PoYnRrjUqYoI-J_ICGmLiakvzvEXceCrngn2nG23v7kw1oY6kZipDTPo9EFNwr9QIJnBxqFsuYj27bil02bLw3YI_HGYrNu90bn9qUmJziCwprZjpNBpIg0wryHOS0vPaUvtlByrCGihR58cxKRWS4_jkvMHhTnmLzVb5NFmj2bAVD1z188Ir5wdub6qZB0JOvKV0oYPqRTINN5IV_IyGoFrC2APNPzIrxEx074FWFym14wYUjyAed5ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جسیکا آلبای عزیز که اول صبحم تو استادیوم بودن مصداق بارز جمله مادرو ببین دخترو بگیر هستن. البته تو این مورد باید مادرم گرفت
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/Futball180TV/96097" target="_blank">📅 21:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96096">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPetOGyMePb9gLzycnOyTKrMbdILIhsZVUokiUMOPpHb2chGAyRxElg-nEgESirmEv_64iPjFojIXWo6jcrP38Pz4r7clViGpCtmv-UNJdca9Ny5oQUFap3DTomJp8ej6LFT1RJn5aRkuEI3P5-2_90l6UEAn-_6kLwHdtOMkikE9LZJwvg9uoqG54_4SYcs-9mtYOJwbpD082jEjCug1CJirOYF7ddLJaaFzZuWwXTG1460eUtcrfPSUrXqxU-k87WGlGW8Br88Wow-sFooawUmKmRye8GjqID8xJ2Idy-B1EMHJivrdHO9gA2c7xbIiOwj9FfKoxoAmUcWCya3YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇶
عراقی‌ها در آستانه بازی با سنگال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/Futball180TV/96096" target="_blank">📅 20:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96094">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🏐
✔️
ست سوم ایران برد.   ژاپن
2️⃣
-  ایران
1️⃣
🇯🇵
25 | 25 | 20 |
🇮🇷
19 | 19 | 25 |
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/Futball180TV/96094" target="_blank">📅 20:49 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96093">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjPq1RlFCm7p4O00YCdkW8AyDSGUEfv1Ou6roGC29FL2yjtxE099dDiXXWYcsjb5GyuPzAFo7Ipbd4pKBht5hq26TH8N73xqOhuquPB8QdFpASb-C1ReFEalbCoQaRjL5hIaysrw5WC92-PwZH6LST5E11cmAI2BMxtT7YC5QmCvJBKxgPnlzzHhSxq1E9YOCsjSM6jtPK1mJ_03J_h6f5EeZS6NLkN7pwpaWlrwypZQLhq2OTGv4SMVEUL08M8wYny-gxDQCX3u-RzSlrfGhzv9hEUy5DrzDNfmv1KOPNfycIVcl61gL-wZ0isFLxexttennD1LiDDXlaSIaII_Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
🇫🇷
💸
#تکمیلی؛ میلان برای تکمیل قرارداد رقم ۵۰ میلیون یورو پرداخت کرد و قرارداد تا سال ۲۰۳۱ خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/Futball180TV/96093" target="_blank">📅 20:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96092">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
#فوووووری؛ با اعلام‌ رومانو گونزالو راموس مهاجم پرتغالی PSG به میلان پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/96092" target="_blank">📅 20:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96091">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A53f6AKXzEaEP69DSwDbPmcY-p_J6L7elAPp5LXY3AJj9sfiizj3WQre1vUMhFo85TvwE1QBFixzFzpGGbtJcs6BL7VVr3ZVtcbf9kG0Vh858cXZJcYBIoZAFDumT3LlBaQjhKXMp_fwK6HmihjamOcKVy9uDJvg-drYcC3x8tJLhg-zdieVcl424Lg37p3rz__AZVmMCBRLsSgFGQ4ur-iffVQwYiUudpbktWMJV8aW9Mt4mJqmDZ5JYCgp7i6rbQxemmWl5OkGD9770h97-gJS3vVSc5Wpgrin7yKl3d91-QSIpfXgo3soajR3ST2ykSi7oEFV6XO48vIqVHAIoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
#فوووووری
؛ با اعلام‌ رومانو گونزالو راموس مهاجم پرتغالی PSG به میلان پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/96091" target="_blank">📅 20:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96090">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9zFdKCbj9ktVP3gbtaxLqxPrtwZ9Vti_YBg7M0ABw7cWbkGvYMqgiG-BC1ZXmI6CTayFqTLZ9-YEyGNVGbEFNOXzr38nPvndrlN0yPL-MG58kgMYPwEk0HUx3NxeyyjFqMjTeXelLUqaUkm2g5nqRMeZ-t_VYIIO4xZU8F_DzfCsEWHpRRSNxuFHO7utf2UtecCJ97ujzlTWtPoWxJv2QTef4O97VK3NNEQ7hXtvHNHnMMMlGV3LR6Elsm1YNEFzVyTqU1FBSHKV2FanbDtCZSQh29onNDtWROxNnkRSYl1YaGA9rTJ14RQMseC_hYwNxkuuM4ipQG6Xa-j3OdFmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🔺
۱۰ سال پیش در چنین‌روزی لیونل مسی از تیم ملی آرژانتین خداحافظی کرد.
🎙
مصاحبه لئو مسی: «من تمام تلاشم رو کردم. چهار فینال بود و نتوانستم برنده شوم. هر کاری که در توانم بود انجام دادم. این بیشتر از هر کس دیگری مرا آزار می‌دهد. من بیشتر از هر کس دیگری می‌خواستم با تیم ملی قهرمان شوم، اما متأسفانه این اتفاق نیفتاد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/Futball180TV/96090" target="_blank">📅 20:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96089">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhD7zxVdeLqgspFsdHBHNUsoanGjYDcQG4neeGuu2VmKdXcsggcU33oJZoDtiU1VnsuQPYtZBp1SFFzvuFI_BJh1KyTwewcvgmmgCZSuTa8t8qoAh-cJM-Nxg7kDU2hkpYm0omYvrZ2iFLFoWV7AVc1BMaWpnvlH1hB6i-3lWBcQy-OpKR770D2IzsY_Cm0IHXvvPd5D1SVAC8z6jtrRAXceQInqZeScyJKFSjg9SfGsQ5G_AnOcjJXivOvHkjOaOLAkjw0jTa-25VECJ_tmp7tSpvHb9rq25jyDM03nL16leDfo8C2vIlMXM6XeekTAdsxDQaigTcHLjfTg5oKkRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
؛ نیوکاسل یونایتد با ارائه پیشنهادی به ارزش ۸۵ میلیون یورو بدنبال عقد قرارداد با انمچا ستاره تیم‌ملی آلمان است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/Futball180TV/96089" target="_blank">📅 20:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96088">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2fs-7R1JjmpmOjIFjgpaPPhR9avY4lxx7YCjhLzMjQIkxclZ-AuR5ZNFFQ3cqWk9SB3uqelKEnP-GAWYk-SiMBksQT6rdwiqm2Wj639fOHwF3_AUMuS4tXW1F2xXDVEj9xj9joQ9mO5kcYc7u8JOKrWdMxYbIHCprLfizqX_fcgEmNcsNaszBC_N5mSjYZ5ZgBgu9VNRgcgb3Nq9l4xvMSZ81nuxjFo2FG73Vw2s7ch43WeumUaP-Fxwb_CdkAXYl7EL2QcASh8sVW35HvEp7MEX3e7pLv9q2KkAneehGkmn3KCd7nljlbvJvaYl9lwFBmyjMQvN_zxag6cQcXMHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به بازیای جام‌جهانی ببره
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/Futball180TV/96088" target="_blank">📅 20:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96087">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🏐
❌
ست دوم هم ایران باخت.   ژاپن
2️⃣
-  ایران
0️⃣
🇯🇵
25 | 25 |
🇮🇷
19 | 19 |
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/Futball180TV/96087" target="_blank">📅 20:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96085">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZQ4JAHUzNxkaojCDbe4mj-G9Z2_vLKizsM9hspovKZv2DY5Odvd9FIyJJEMdS3sTV7sK9spUkuLgAH0d6zjnB00Pw9BFNzYm_qGpOCQK9SaVL4sjWHQL3puxCVISYSBT-T_oXTyOX5606DEkG8NPF0Hs10DtYeYhEV8YkQpiWwoOZmhX3YLKa95-OwsEg3srQfJC4SbEm143mtB16UPWT-wSwPnVfOfvdGnl39TbScIU9scIoXb-JsfqYW6sK7I7D0eH1duZiZI3xFCnfe-ZvaMwAakoIywtXIrQwdj1xeEPiJbuHrO3_tJWRgYtoFToGJ9Te1M66qACa78KfzQA_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Anyg4yV5HNDHtTLKIL84nBoz41VD5pd0VbZLhG_OLr3Q8EVzMt2C3ptv8uzhjWmxU2ESLxonUUjGIrujX4p-zQZPqwRL3C2hLteJcEGzhGrgNZRGEnlldBT2m4BMemfW95H67XN7py_IzV7oRHy3A5HHvNgc9BBPR1xodo78FbK8ZTq-hYt7deMDC3tSYStMp-V_j2Ycq864BXD7zhkO9805EEH_Yl48Jk2KLERFDtFrp7TKDF7YKNMa8JTbjmAPM1FUlGY4H1wbxp5mVnnek0uBxXN-GJohSsGieAaPigxXBQp08K3_dzDUaElr1BhahOmz7MnorQNtA_-nsSbu6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
پشمامممممممم
برونا مندوزا مدل ترنس برزیلی گفته که حدود دو سال با یکی از بازیکنان تیم‌ملی برزیل به صورت مخفیانه رابطه داشته.
🔺
به گفته او این فوتبالیست ترس زیادی از افشای رابطش داشته در حدی که قراردادی 500 هزار دلاری بسته تا رابطشون محرمانه بمونه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/Futball180TV/96085" target="_blank">📅 20:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96079">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/szcZoTiRGGH8UTDclz2-9IU0tzZ_0SNVq9h6twXgWTmD2P7evUVAcuob1W5WIqqYUfcZVG7t9F-2YkbFiGobbnHcPdR75s5dQXSSZw0TvRQ5JYo6UBftxN7L3cMlAUMxytAM0yJUP8mDVKxNe6ztrJu9ALjHhocQuXamuU9Yc9PzgT2Oj1mkmFTVANqWBLZD28lw1ndzP4sU1-ozIjX7HCMplKD1VXDktecvbpBCCXry-zEHwa1uvlnoprkKsOnj7sUdydngdu2En66Lm6YWyLBjismH9PvsLKNeTdUgbQp1Uo1Mj3CTdgrlAHHrc38VMHuWEUZObs0yp0YOe2Ai6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s5SQMsXqv2BpPe_115ZvAxFSZbkn-oNynkOSEYSP64s27dp5p7aW2TmWRF9N-asTd2sbfnBiU213g2eapIgmlshdNVYuP77FrhjzqcuD_ioIWgihnqD4Zpcga7w_5DMEQ2dBnKcc4bqwIB3YQ03dX4QDz-xC3J9szUAhL1rvTFMKDIbhnqOrwxHjpbZL_T1iC8rAL4d_JF9jWgqC1hiqaSYqhoD0PXz1Wv3mNfp31uYFzs31AMz11Qr3QC44cdIn-LUuDpk1AON3eR75qjTtU7L2lE40Er1VUtGhXSRoftSe2MUqjN98v-23KWHDdKjDN18yzc02gFBBBEv7u5L5zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lFn8I5DEq5W1b4C7gqU-E03fPIYlNgFXvD3eSJd9As4ue1RWmp4qRmyyBAEJx13h96JJst9G4I8OEGbDwAIPWYZdpS2Rfc9Hx2bCNWYT4Y2jaFvdjFoHzpDRbvLERJdwxARcsm8jj3YEZ4Jk5RiakI7Bu5YEfgHNM4VUnUbKUJqCehf6-oJzcTr4XOaNo_zqa-CwF0_RBXj2F7hbn1nlReVluZ_18axZbKxKTL_Qlh51h-VbjPhRWp6MWt2dLQfubjFwmgzDuMKL1_BEKOpuPdc6wl6pT6QzZm_arQd9AiS_xZ-pqsigIH6JQkyKUGPd-t9V30WG74fF6RB4g9Lqkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cLSaxpw6_4ZujVATT369g7T10_aB9-77p2KRXNyL7WxSDSxPGoWLzI3iVlFpyNs1u9gdwdypw97k_X47QVeKk6aawTi2JJdabl9GkeAzPqvz6cWO31hlimZbXW5H4Mru45xdEIC3IO0LqwmRFWAa7QkBeUE7zO70HgDydlFmgRf4M9-aCDHeUMo4N56pI36fg0WcmHbRXTK-iZzzGQxN40U1h6gOdTfY4IcAhpUWgldWMq5czRLNNECQWE4PQ9XtPKGVFtHOzkY5cQhik4mN9t8H3pYIFoCOeSJmaJQPn3Fjm9etWLwZmszzU9Tg6dExf78w4vU_WDb-nevTe1Zh0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d565175c8.mp4?token=cl4N7ZeBAJbtbDf7CBMKqs1eT6ten0mnCrusrCfYVnkFhxJNFiyRjDkRVKlDVrmiHkQpi2qrsn2Ee9kwjbgJ8cE5C2aTHP9_bXqpst-fXtoF1D8aescBbxVU9ueKmnDJoLu3wbTAzXG-vHzmYBfjnYnEZPHIoKNMbxCc_YiXSQYE6hhQ7uMwwQMaoXvQcOAxPMt83R2j7ZkUQ3FRELWv9xbwY5XKXIo8pS3fASyrZy-noMdKHMbmHfh557Kn_7rQivWZBS4pE8Z8lC7Q_RBc01n028bTOU_BTWQqs4z2DDBQIQqJ63IItoHSUyqJtrrCzroZMm6isLf4i-AyDeRIPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d565175c8.mp4?token=cl4N7ZeBAJbtbDf7CBMKqs1eT6ten0mnCrusrCfYVnkFhxJNFiyRjDkRVKlDVrmiHkQpi2qrsn2Ee9kwjbgJ8cE5C2aTHP9_bXqpst-fXtoF1D8aescBbxVU9ueKmnDJoLu3wbTAzXG-vHzmYBfjnYnEZPHIoKNMbxCc_YiXSQYE6hhQ7uMwwQMaoXvQcOAxPMt83R2j7ZkUQ3FRELWv9xbwY5XKXIo8pS3fASyrZy-noMdKHMbmHfh557Kn_7rQivWZBS4pE8Z8lC7Q_RBc01n028bTOU_BTWQqs4z2DDBQIQqJ63IItoHSUyqJtrrCzroZMm6isLf4i-AyDeRIPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👀
یکی از خفن‌ترین قابلیت‌های گرافیکی GTA 6 سیستم نورپردازی و بازتاب‌های واقع‌گرایانه‌شه.
نور خورشید، چراغ ماشین‌ها، بارون، شیشه‌ها و حتی آب، همشون فوق‌العاده طبیعی به نظر میان.
از اون طرف انیمیشن چهره و جزئیات محیط هم انقدر دقیق شده که بعضی صحنه‌ها بیشتر شبیه فیلمه تا بازی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/Futball180TV/96079" target="_blank">📅 19:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96078">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🏐
❌
ست اول والیبال؛ باخت ایران
🇮🇷
19
🇯🇵
25
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/96078" target="_blank">📅 19:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96077">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSU-jXUOu6muA7guOBRdlDznnhA5AyLKFURKU1t1-Pase2c_gd3rG1k7FEfNFaCutJdG60dvrVqz4w7boLkO0f_Qq-cvCwSFB1DJHY0Tktmp98S6IulHG7JjhgjKqFjxDo7ubIPMq1BOUYCM9-6YAiJeELahCoJ2vIpqoJtHfLBw331HKwEfWoE-v9kHb0Mgr5rDNrPzJ6acQMGk5hURJWpULs3Y1BTljIJEN49Z7y4FpC1ON4tILb_px4UosE61AZC23eE9fU5FUSEoRjJhqZgCRnWxH2isaIIYl6qtwXYp6q9vIz37WIKQpimsSofIGzAQnM9-5nhuz4QcHRx0dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
🤩
لیست‌کامل بازی پرسپولیس و چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/96077" target="_blank">📅 19:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96076">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🇮🇷
🇪🇬
فوری: تیم‌های ملی مصر و ایران اعلام کردند که در صورت مشاهده هرگونه شعار غیرمجاز یا نمایش مرتبط با جامعه همجنس‌گرایان برای بازیکنان یا کارکنانشان، از زمین مسابقه خارج خواهند شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/96076" target="_blank">📅 19:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96075">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🏐
❌
ست اول والیبال؛ باخت ایران
🇮🇷
19
🇯🇵
25
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/96075" target="_blank">📅 19:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96074">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewb77FLJnZI1U5Z9p41Ywpqada1ouZJ50mhu-kQzyl7WQwcGfudIk1QQLg5ZyCkm-Yg9hpHn4yf4NpfRNFsFrcDhOWDZE8eoZbL4eQKrnapd45C3fHEE5N53iXgW3nIM4uvJdKlyWHeI4m_UTJEMdIZ6GmUqZapEbiNR8SsMolZKZFcUKY0lgU3VzGjeRPdZBCSFSKWgxyznPOICjxHuyG-8wSEVnGTewO1FKtDwaG_gn9NECb2GFyyFKA0nOhOQmiMREFhtAcp1GRdCxzq0ZJliohtGNQAxuE6A8qIQidYjD4GFOjaaFrPRysGNPoN4QX7pkeEpBCfJhOduXRWpDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
اکیپ:
نروژ با ترکیب ذخیره مقابل فرانسه بازی خواهد کرد. 10 بازیکن از جمله هالند و اودگارد استراحت خواهند کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/Futball180TV/96074" target="_blank">📅 18:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96073">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lID2V7ocB3nrbTXqIHjTl6zaIaK5yxAjBQHvO4SvgFnwQFjz4rZRWeCjTtmqa2drdXcFLHoLp6MISt3d9y2xRFtL27T09bMVErlLLMvrvwhrvQrfugNuKa65JVUL8N7KiIc9OpQNTpNU9a6NR9qob4vKO5GKOk6j-V5mpDjqXq_bS3EZsUG9s6sg1pmrzXzKtTO4P8Ej2ndfXJRzN2trOwkcY8kiyvL88-dsIOnGkr6KIDYj7ooGav3nXcUMJm8QOaDYAAnm5YRe0XEzkJiG95l-CNyfF4v4hKOkdPjBDp6TjRsf18yDcAu2DvROMZm7cEsPmfSBY5wUDWiKOw2imQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لئو دیاز خبرنگار برزیلی : پدر رافینیا از حق‌وحقوق مربوط به تصویر و تبلیغات پسرش سوءاستفاده کرده و حدود 80 درصد درآمدهای اون رو دزدیده، ظاهراً این موضوع زمانی لو رفته که رافینیا و همسرش میخواستن یک عمارت بزرگ بخرن و متوجه شدن با مشکلات مالی روبه‌رو هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/96073" target="_blank">📅 18:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96072">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4NI_6qBW77kDI1Bhu-zcCzlrBB8YbtSv9m8xGnAHh47ETb2XaKkrbmID68SJliTmkQmQ0Z5c3s9CHhD3GaG8H3gXH2iRmIaS7JrqjeG_ejw0t5zkhGsKJKNjw34A4FEXvrM2cc0GLuahpqO0VOQpvaDo_d_nJVwDF3YD6LjmeY5P7blR6dIkItRaSmXtVGdr7IR0lbRGvgeKj3LZM347J79dNpwky1jawHFf7XxpDOEPuiHD71qLJLMhFeYyFe-zLSb8N6gYXGpKqev3RKyEyM1dnu6f2rTvhUYqKzjTTcWsqf15B5vvTqlxiYc_-Z16a4SlmQF3B-6s5asmZVugA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
مسی
18 گل در 5 جام جهانی
5 گل در این جام
34% شانس بردن کفش طلا در پلی مارکت
⚡️
در برابر
⚡️
🇫🇷
امباپه
16 گل در 3 جام جهانی
4 گل در این جام
31.5% شانس بردن کفش طلا در پلی مارکت
⚽️
حالا پیش‌بینی کن چه کسی کفش طلا می‌بره؟
شرط بندی روی بازارهای پلی مارکت از تلگرام تو کمتر از 30 ثانیه
👇
https://t.me/PolyBaaz_Bot</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/96072" target="_blank">📅 18:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96071">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JX7JKJh2gk7XhiYy57akh9IaEl0ZQvUs2npVzw98riI7R-goZ1cp2_hWXFzwUi0zre99ZdfHDQfsjEDNtF1o6gezDmS9dwNpQpvYdFYAgITp_k_EYx0jacpxs1qhXr88wsSWDHAyN25Z77k6LWZEdp3SxWKyThPQa84AAEwQ4ntVjQYNqTzvhqJedQnVFetDQJcYYY6hJMXfuoYaklGNViTrZjYiorw7MM3W051KRCgI0dUxK6SsG7V-zu6ZG06IcawFtp974PsRESok8ulLu7MKIYkVZhGpKpV0LyagSL6XJXU8uoBBEfILqEzsI8CwdJV9i2kHuh4Ov4ruYxcU_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت ترکیه تو مرحله گروهی جام‌جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/96071" target="_blank">📅 18:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96070">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd55ccb496.mp4?token=sKrfnatLRdZaZGY5ORYoEJDMe0lHQYzoZdu8IqRQseUprA1QAqiV4J2S1NBpEItVT7IQMfPn1QHGsmrO4oTrU5FpNR7u2f1ZsoQPnMFKq_NHwdbW54ofz0DlzWGnQQyzh7E3nPVweZwT2XqNgsvzoIN0rte8VdjBfXV4lvuyKG08lho9D5gl9zBuagul-q9UnNDUrreTmtnHvqZwXsJNYDZJ2jdjo46SI_rTLFubosKEKfBfRLh_5eLy6v-0ZUl9s9q4YzkHun8YHiAdD0bBvtgKjtoVet18EphKURjPIf1DiGH6vdIdnqd9pxOMT9l9qPYrX6LQpEXkwzmeKbi1fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd55ccb496.mp4?token=sKrfnatLRdZaZGY5ORYoEJDMe0lHQYzoZdu8IqRQseUprA1QAqiV4J2S1NBpEItVT7IQMfPn1QHGsmrO4oTrU5FpNR7u2f1ZsoQPnMFKq_NHwdbW54ofz0DlzWGnQQyzh7E3nPVweZwT2XqNgsvzoIN0rte8VdjBfXV4lvuyKG08lho9D5gl9zBuagul-q9UnNDUrreTmtnHvqZwXsJNYDZJ2jdjo46SI_rTLFubosKEKfBfRLh_5eLy6v-0ZUl9s9q4YzkHun8YHiAdD0bBvtgKjtoVet18EphKURjPIf1DiGH6vdIdnqd9pxOMT9l9qPYrX6LQpEXkwzmeKbi1fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اکوادوریا به این شکل تانک آوردن کف خیابون تا صعودشون رو به مرحله بعدی جام‌جهانی جشن بگیرن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/96070" target="_blank">📅 18:33 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

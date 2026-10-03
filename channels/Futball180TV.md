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
<img src="https://cdn5.telesco.pe/file/Aj2aWSJG0UXKpRu9MOq0_S_E2bDOfE9AChne8WTpd6SndE0yl1ggeGJDztFQ_tR4qJDIRXnYA6K3WB8sdMCGgnxfh9HSFRSIw4PZAJ9aUx5d5J6XFfpJJ4eDI9K0xdvXa15QNiEVmt6g2BCgUC4FC4i3a_MvDD6v9UV5viPXNzsUndc90McBwz0E2WsUFVI6VnKe0t7dBOx1nRb76MOhyrCQ-vwTg3icGQ_YnMxAISUK9R20sL7npEq0MQZWuiq9GiVNqwnUnaTD6JNJ0ysGUq4lmUFWHo2c9W9n2zwP5OHZ_HxLzLhDOM83XkZtUtpIRemM0paNxwKNsuhFm6NyCA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 392K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 01:05:37</div>
<hr>

<div class="tg-post" id="msg-107782">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107782" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 123 · <a href="https://t.me/Futball180TV/107782" target="_blank">📅 01:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107781">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsfYxixG7GvR3TUho17zXwM3w7C_k77kPJ-s6H02_lLOJi6MNLSvAt4kEO12oYUvOY-sIcQgHrW8l4JBCbYhGjyaA55dcYoevsqTUM8XF19tN0q3GhfqskCKFoKdd2EuMY81ox3911TWX3eC7NgDUBXnrWSzFsJnmrlzfBreP4SJkI0a3cHtZaUBXqIt6xTBVW3WhUzjG40FwUgTMY608yRcRebcuHLBFFuSrEEz6r4uj46edPEeubEWIVvpuxWhCN0oT8PDOUkCuncFSLVuMYwBVsX7AM8DCPg4SFreS5haMFUs4vq-5XebQYHCfUjUwKrUeH6jpH0UALPath7K9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 123 · <a href="https://t.me/Futball180TV/107781" target="_blank">📅 01:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107780">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df11e10418.mp4?token=n0vUXIHw91YJ9splOCtSODkVUSNiP8iAPskP0eFDTDOPhXLFCVapJvYqRbB-MubaqV0IjrYbL05CpP-bvGaxxt1d99efIeqf9Ov4e9qwyeoG9TrP0Z6bKIBRf-qD7_fzTW-khgr7TYFFdUvqbRJ86CXzUQH5pindHlJJPoc24tywMAR-dSimgKOIjH6JDm7k18l44-Ce9eseOkW2BGEqcoPpabdkPpa8ymVmg1yXr3G8F-_A5zRihCZ55YSjEvxlF3vG6e1wy3i1EwrK0PQrwJhAAnr4_leSj7irUCrv2gYmQlFpSl9k5zgKE3aM32V_nEGR-VCZZ-esp0OsFiPcLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df11e10418.mp4?token=n0vUXIHw91YJ9splOCtSODkVUSNiP8iAPskP0eFDTDOPhXLFCVapJvYqRbB-MubaqV0IjrYbL05CpP-bvGaxxt1d99efIeqf9Ov4e9qwyeoG9TrP0Z6bKIBRf-qD7_fzTW-khgr7TYFFdUvqbRJ86CXzUQH5pindHlJJPoc24tywMAR-dSimgKOIjH6JDm7k18l44-Ce9eseOkW2BGEqcoPpabdkPpa8ymVmg1yXr3G8F-_A5zRihCZ55YSjEvxlF3vG6e1wy3i1EwrK0PQrwJhAAnr4_leSj7irUCrv2gYmQlFpSl9k5zgKE3aM32V_nEGR-VCZZ-esp0OsFiPcLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎁
زلاتان ابراهیموویچ به مناسبت تولد ۴۵ سالگی‌اش، یک خودروی فراری مدل F80 کادو داده. قیمت این فراری، حدود ۳.۶ میلیون یورو تخمین زده می‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/Futball180TV/107780" target="_blank">📅 00:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107779">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f84ad4f46e.mp4?token=UNWg02HeXnT7UhaWp7OzpCYbj-TvkTtNwQWTT7JJtrjLC5BgBLgr3l7pGEKBT8-xzZVE_9d1RU1zfMeajZC4vk6Eci2Tz303xGEQCKS0MQwVzKW9UdKxc1JciBorvIXd5TOzreoS7XH3XTlT6jq5WyJKEJCOGYLtw08dvUGqahZLUMM3TfnlBg-ffKynj72y6ZXGnDxDHJh8Y-6VgDiHn2aKeNVf-_Nh0TfC9uGSRs4FVfO1xIGE4ZbXyjAFvN7bx39NsbUVmt-jSKMd8mjrlKoooqjNWNjflYdMJjcd4Y3auDvFNdO7PhjmEAutNNcFjXM_wEK8gfiG9ypiOXdTrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f84ad4f46e.mp4?token=UNWg02HeXnT7UhaWp7OzpCYbj-TvkTtNwQWTT7JJtrjLC5BgBLgr3l7pGEKBT8-xzZVE_9d1RU1zfMeajZC4vk6Eci2Tz303xGEQCKS0MQwVzKW9UdKxc1JciBorvIXd5TOzreoS7XH3XTlT6jq5WyJKEJCOGYLtw08dvUGqahZLUMM3TfnlBg-ffKynj72y6ZXGnDxDHJh8Y-6VgDiHn2aKeNVf-_Nh0TfC9uGSRs4FVfO1xIGE4ZbXyjAFvN7bx39NsbUVmt-jSKMd8mjrlKoooqjNWNjflYdMJjcd4Y3auDvFNdO7PhjmEAutNNcFjXM_wEK8gfiG9ypiOXdTrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
‏لحظه
اصابت صاعقه به برج میلاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/Futball180TV/107779" target="_blank">📅 00:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107778">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzzIrk3VOr5iicReytVtmA4lcfY_y_QZnXOqD5rJeR-BHxL1qy0dI_tXZC8ZLliNaO06ye-DeGWtKWgmX-Z_ZZT-vyIsyoT5FwjpOikcVifA2Bce9zCni_gqxrIZXV8xXyu7AhgL75yJVdu_MJIPOkgOXk5izag1DpBopocxbrKY-SotH8EuIL8zAQuzhiR-Al_VqUC0atD5DJX33JSVwpWnV3EZGP4Vfvak2RKzHDJouRUm9RXVoNW5WgHYm4TVZzUX9ADhXqQTiteEj8CBW7lBDPhTxTOjkVP8N-6JNPlbspOWVmrJU1Yx9aSP-OqNwxEvEjGTU8opWP7ciMAFXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
لیگ ملت‌های اروپا| تیم اول و دوم ندارد؛ اسپانیا با هر ترکیبی برنده می‌شود
اسپانیا سه - ‌چک یک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/Futball180TV/107778" target="_blank">📅 00:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107777">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abea032aaf.mp4?token=Rezygc2-vupeKGZfjNMjrfq0zzSKKWkJjUw5c-Q8Ep2nFYFlh59w_2Fn31kkhPyf2dzAK8UriQ-4Sd1jpyI31EAX_Km4FRMPnfl1MErF6kOXYQNbUlR0w4p5b8SpZl7FsNS5KztgAMBTXZT2VuH_a8tibPeHFoXjGatnpX3FuiyprsY_5pAjYdt8pQ_Naw_O-L30_rvBLptAsi3UTYr1FAdlxDAJBjOOD6edwQvzQQDRmuyYQdGW8enESEr4ezNQ2JXb1yoCEaKwbMD5aCg1Zey-73lmV6pqSzA7WQ_Yaf3JvDlNW7sSbauLdRYSlek_gQGHjWLKdOEJ3uBtygqPcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abea032aaf.mp4?token=Rezygc2-vupeKGZfjNMjrfq0zzSKKWkJjUw5c-Q8Ep2nFYFlh59w_2Fn31kkhPyf2dzAK8UriQ-4Sd1jpyI31EAX_Km4FRMPnfl1MErF6kOXYQNbUlR0w4p5b8SpZl7FsNS5KztgAMBTXZT2VuH_a8tibPeHFoXjGatnpX3FuiyprsY_5pAjYdt8pQ_Naw_O-L30_rvBLptAsi3UTYr1FAdlxDAJBjOOD6edwQvzQQDRmuyYQdGW8enESEr4ezNQ2JXb1yoCEaKwbMD5aCg1Zey-73lmV6pqSzA7WQ_Yaf3JvDlNW7sSbauLdRYSlek_gQGHjWLKdOEJ3uBtygqPcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم اسپانیا به جمهوری چک توسط میکل مرینو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/Futball180TV/107777" target="_blank">📅 00:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107775">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f7684655.mp4?token=K_nMilXULm7w_LsACBlrEXCJcTcz2-6TjKxdiBDswl-U7DMzLM5i2YXsOlktjoQoZiS5kNe7TdHJke3dmuUGRy2d_6raJgp1j4AlJ13XtfuWQDOLN662h2RgPjGeMbXWYEgy6R-irJVBeaDCXTFZAP-n08rG1XYSei3Le85wgY9T1cnlaiDkCv79ryrU3mp8qKOUj1xQlyS8dmu1WhHG9tfplMi_iKI2f2OWRGxyEx-PTFekyY4jsNLcYraYCTPA3dqRFAog4ub-c5k21Qx9EfkQqpBJeRTofKwR-MegEMn92tCeDnm0TJvk1j6bkV0EoCEhaAGXEq-5pD7KyWd63Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f7684655.mp4?token=K_nMilXULm7w_LsACBlrEXCJcTcz2-6TjKxdiBDswl-U7DMzLM5i2YXsOlktjoQoZiS5kNe7TdHJke3dmuUGRy2d_6raJgp1j4AlJ13XtfuWQDOLN662h2RgPjGeMbXWYEgy6R-irJVBeaDCXTFZAP-n08rG1XYSei3Le85wgY9T1cnlaiDkCv79ryrU3mp8qKOUj1xQlyS8dmu1WhHG9tfplMi_iKI2f2OWRGxyEx-PTFekyY4jsNLcYraYCTPA3dqRFAog4ub-c5k21Qx9EfkQqpBJeRTofKwR-MegEMn92tCeDnm0TJvk1j6bkV0EoCEhaAGXEq-5pD7KyWd63Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول جمهوری چک به اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/Futball180TV/107775" target="_blank">📅 23:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107774">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdcc4901e9.mp4?token=B-WUf-g24rvuepHh4Y4fKDcRZIhfdy1FLMB1MT2JGht7e9fpvBF80MQ6rajjTWHe6fsv1leQ5kghtV4p18L9IUgbJ2P0EOfmokpalEd7Oy_DkS688phmNUqutEPmd6IGl46xO0aouNr80ENEJXkaXi7XMRM73MC8ygF-WBSTt5BrLOEqAKdfL_TqT9tORA-LpNNHfPO6IUW2DR41M9T0BXEq870bwh_uP54J1m6089DPSC2LhwIPafB_vlfA50OGJHZnhQTEq2JEwaPmkUtWrkdAFwkY-VAmgnXtfMKFIGaPIEwwHV5ndtmeGQsUncK57Ug1vRszDbWYAO7akU7SlZxm3L3o9JqIp3wIFq_sg7EVFkHsT2JEsZPIheKVtZxp7V-3h8ElOuuuUWj-UN1LDj7nmpXC0WP7ka-1k5TLlo4euix0g96XqcbIiMUJzEbS_mEgc6XiNt3RLG0lfYKfoXgJfeJMtVgA-Bd56G14JjurXNlHwR-l-e9mRlqiNOUeP_m3Zu9-csiYGwOlYgBsJ4XwGGmr0rS2WVCmboRDme2-LatG9-x5YIMfZwiKthZFQCVZre928KoUqrb-CCWt8RBG8J_JjiFtZvHZKMfu-U6bNGe2AXBdaLH3m6yuTBN0bBILrRVkRYCWXvBkGSZYRqZXqIeivISgG6tCQzaRj_M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdcc4901e9.mp4?token=B-WUf-g24rvuepHh4Y4fKDcRZIhfdy1FLMB1MT2JGht7e9fpvBF80MQ6rajjTWHe6fsv1leQ5kghtV4p18L9IUgbJ2P0EOfmokpalEd7Oy_DkS688phmNUqutEPmd6IGl46xO0aouNr80ENEJXkaXi7XMRM73MC8ygF-WBSTt5BrLOEqAKdfL_TqT9tORA-LpNNHfPO6IUW2DR41M9T0BXEq870bwh_uP54J1m6089DPSC2LhwIPafB_vlfA50OGJHZnhQTEq2JEwaPmkUtWrkdAFwkY-VAmgnXtfMKFIGaPIEwwHV5ndtmeGQsUncK57Ug1vRszDbWYAO7akU7SlZxm3L3o9JqIp3wIFq_sg7EVFkHsT2JEsZPIheKVtZxp7V-3h8ElOuuuUWj-UN1LDj7nmpXC0WP7ka-1k5TLlo4euix0g96XqcbIiMUJzEbS_mEgc6XiNt3RLG0lfYKfoXgJfeJMtVgA-Bd56G14JjurXNlHwR-l-e9mRlqiNOUeP_m3Zu9-csiYGwOlYgBsJ4XwGGmr0rS2WVCmboRDme2-LatG9-x5YIMfZwiKthZFQCVZre928KoUqrb-CCWt8RBG8J_JjiFtZvHZKMfu-U6bNGe2AXBdaLH3m6yuTBN0bBILrRVkRYCWXvBkGSZYRqZXqIeivISgG6tCQzaRj_M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
کارشناس صداوسیما: چین دیگه بهمون تصاویر ماهواره‌ای نمیده و بهمون گفته اول برید مشکلتون با آمریکا رو حل کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/Futball180TV/107774" target="_blank">📅 23:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107773">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‼️
💵
دلار به 271 تومن رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/Futball180TV/107773" target="_blank">📅 23:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107772">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a91b6171a6.mp4?token=pAq4Gyxb1yZXULGldq6vMyqi2uCNa9abf37RAXHbeLAAevDi6UaGN5rkhAoOwi3MX7Gz5GQ9bt4LAbl7LmaaPK9hUAPYdjnZNu6VE7vdrznmW9eNIIhWuRIeX91uZ-4foilL7Ypei7a8CwYpxU6St2ds0wjX-d81jkMXyHhFheoKKU80WPWvDgMr_cTTS80UeLtX2utjV4gDhb1j1R9ERU0H4gumCmpm_ohxvlKXeXL442MYsVoxWHgCDmzcEY5TQknLKhQOjX4VxxDMxoWJH8TprqzZawBkjz4-Oz5aFhzjd2HwyQOuyCfxToxFvCJmMbMyb1BolodBe4o6LImFfodgwiVNW_slLknCFlBj2ZriWYtQLbtp7dev5oGvLPmJDhgToiLuGNOhniLVt5MvoryVJJxlyW5mfY0z9AE-ffrdtSWEhM6wJ1-iwrg0zk2XQSxgv0enVfDwdfqYXhW5Mr_2YGdz0M7NpYHyQXOhcmq0dUejrXWDsPOEenn2n9VumBfd3e2H5i9pqLuT_mzGzrKvgKXIxdVGAv37yAmzUwBUA4K7db0PlU_tSjMVr86YpYYLOnz-0ck7tjZTrfGhXBtTFffnye62SA5dutxYvO89YV4NWKdTnhzaze6j3fcTZRAciEqPMVw8FN8ltgEPlZH-4g9xAcx69N8LUj7Yevw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a91b6171a6.mp4?token=pAq4Gyxb1yZXULGldq6vMyqi2uCNa9abf37RAXHbeLAAevDi6UaGN5rkhAoOwi3MX7Gz5GQ9bt4LAbl7LmaaPK9hUAPYdjnZNu6VE7vdrznmW9eNIIhWuRIeX91uZ-4foilL7Ypei7a8CwYpxU6St2ds0wjX-d81jkMXyHhFheoKKU80WPWvDgMr_cTTS80UeLtX2utjV4gDhb1j1R9ERU0H4gumCmpm_ohxvlKXeXL442MYsVoxWHgCDmzcEY5TQknLKhQOjX4VxxDMxoWJH8TprqzZawBkjz4-Oz5aFhzjd2HwyQOuyCfxToxFvCJmMbMyb1BolodBe4o6LImFfodgwiVNW_slLknCFlBj2ZriWYtQLbtp7dev5oGvLPmJDhgToiLuGNOhniLVt5MvoryVJJxlyW5mfY0z9AE-ffrdtSWEhM6wJ1-iwrg0zk2XQSxgv0enVfDwdfqYXhW5Mr_2YGdz0M7NpYHyQXOhcmq0dUejrXWDsPOEenn2n9VumBfd3e2H5i9pqLuT_mzGzrKvgKXIxdVGAv37yAmzUwBUA4K7db0PlU_tSjMVr86YpYYLOnz-0ck7tjZTrfGhXBtTFffnye62SA5dutxYvO89YV4NWKdTnhzaze6j3fcTZRAciEqPMVw8FN8ltgEPlZH-4g9xAcx69N8LUj7Yevw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
جواد خیابانی بعد چند ماه نمایش خداحافظی از تلویزیون امشب دوباره به شبکه‌ورزش برگشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/107772" target="_blank">📅 23:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107771">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd54269d70.mp4?token=g7_vkOirtzBfRd25d5o9OE_ID12Ny5rLnb8B-UPMqifB_XxJHa76Z6yMtffKuUd-CTKnIcbynnoNz4YECOxIbQJaK3qTH9v3Zoa2Uf8LEnrmpYAWNsGbN9Qzxr8CqLZ51-5eMLrG59cT_dQyef3ckOgv7YNfpk8zcesP_5m9bZG2cHD3r7UVMi-S4tesYRp5HzPrrMje3xJNAZ0EnjOFGkBbScTZJg80uijkyCjFFvtDo_kBjJpdrfCuGCPk2DmfLeb_Z-hL4eoZaLaQUE7vXhZZfCgKCLy7aK98Le3kAPZnjLwDQJJ7sJIYW_PqnVszwUMINa5-dbdoAzLPtpQEqh5wntKZjUYNtWwiSyxhmKcFvx1-_k9WXYU7lKjHODZjcttU2zTsSUlHsLjKdxjj3D8oOlqvLmHrpojLEgTqJ0ioAtZPsSMh5l2dZlkGlNyv7o3njGT4roEXG1akuzZGn8-3Ihu-cguXyJSG6YQGEpWG4FH1_QeB7dRoMJY7xMmj3aU4c8cf_B0rr2xVmhfXI-lHguhtR3ZJiuFnEWyL0w-0oLz5-B8WduYBb5UiJZIGklX8PBumbo26M9Xn2Howo9as8GGyev5UN8c4_wzfZGm5RAgx6gSEf2Ws-v6zv845pUVv5sp77nIgGotgj4Jvp7v69yYusogFkMo_q68d1oo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd54269d70.mp4?token=g7_vkOirtzBfRd25d5o9OE_ID12Ny5rLnb8B-UPMqifB_XxJHa76Z6yMtffKuUd-CTKnIcbynnoNz4YECOxIbQJaK3qTH9v3Zoa2Uf8LEnrmpYAWNsGbN9Qzxr8CqLZ51-5eMLrG59cT_dQyef3ckOgv7YNfpk8zcesP_5m9bZG2cHD3r7UVMi-S4tesYRp5HzPrrMje3xJNAZ0EnjOFGkBbScTZJg80uijkyCjFFvtDo_kBjJpdrfCuGCPk2DmfLeb_Z-hL4eoZaLaQUE7vXhZZfCgKCLy7aK98Le3kAPZnjLwDQJJ7sJIYW_PqnVszwUMINa5-dbdoAzLPtpQEqh5wntKZjUYNtWwiSyxhmKcFvx1-_k9WXYU7lKjHODZjcttU2zTsSUlHsLjKdxjj3D8oOlqvLmHrpojLEgTqJ0ioAtZPsSMh5l2dZlkGlNyv7o3njGT4roEXG1akuzZGn8-3Ihu-cguXyJSG6YQGEpWG4FH1_QeB7dRoMJY7xMmj3aU4c8cf_B0rr2xVmhfXI-lHguhtR3ZJiuFnEWyL0w-0oLz5-B8WduYBb5UiJZIGklX8PBumbo26M9Xn2Howo9as8GGyev5UN8c4_wzfZGm5RAgx6gSEf2Ws-v6zv845pUVv5sp77nIgGotgj4Jvp7v69yYusogFkMo_q68d1oo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
هنوز چند روز مونده تا پدیده ال‌نینو وارد کشور بشه بعد وضعیت امروز عظیمیه کرج:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/107771" target="_blank">📅 23:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107770">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9943a67dd4.mp4?token=a_fLBHa0AyuKp4K3CKWp2kIeU6gJ8Nosn_-Y3zjt6kSfXwvhOFQ84d5SzC7klaky5FejXDcGGbKjk4NFhP412XEjpTjlXvGPCbRP_4_iCevEqL4ltIUUkcXeO1uhwSOI_DC9-OnLBs5jCgI8AJSiI-LzO7ZNacGEd2AHbpuIx8rocsUSv9JaN5Zr0JzUo2q7EwMMFJb_f4dBgZTGpWe6aXP0ppkXf60YaxQelTqbRWaLkYa5tMDcFrlfWZUP6fli2sygLGl1F4JTGqH6CJDkpayCwpEvGXd8X_ue0IAgzMXW3ajMh0_nxWYRpCxCOwxQSWZV2Go1ulD48YyvGrbNZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9943a67dd4.mp4?token=a_fLBHa0AyuKp4K3CKWp2kIeU6gJ8Nosn_-Y3zjt6kSfXwvhOFQ84d5SzC7klaky5FejXDcGGbKjk4NFhP412XEjpTjlXvGPCbRP_4_iCevEqL4ltIUUkcXeO1uhwSOI_DC9-OnLBs5jCgI8AJSiI-LzO7ZNacGEd2AHbpuIx8rocsUSv9JaN5Zr0JzUo2q7EwMMFJb_f4dBgZTGpWe6aXP0ppkXf60YaxQelTqbRWaLkYa5tMDcFrlfWZUP6fli2sygLGl1F4JTGqH6CJDkpayCwpEvGXd8X_ue0IAgzMXW3ajMh0_nxWYRpCxCOwxQSWZV2Go1ulD48YyvGrbNZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل دوم اسپانیا به جمهوری چک توسط رودری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/107770" target="_blank">📅 22:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107769">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a73573624.mp4?token=ThIEsKep5ehq55GEYuTTahHQ4cvd9pdX_6K71CK8opVOuginY_YvrwplqDgCheGcE7obYuVRTY2VJaGjagqseIE4B-FVVXrrvokMiEuegtg1E8N7cfRL3EqthMrZ3-txwKTBYZW8mZBcZ47w1Wuzn43iqufgK6BiLd_oD4DswMxThRpNbhfST9czBmUjxF1r8mJYNk4CieuUFEyyIrtmTFMCkX7Hz2KYivElxWE8jgIlEc7yD-wby1ttbV8aqZYYsoRXgr_Lt13xgOBKSzmqonB3xHfNfCx8Pxuq6cTImO_O3kIcH3LLcIj0QkQWV8nhPSmK1dO2YGQJeiG2DBPCqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a73573624.mp4?token=ThIEsKep5ehq55GEYuTTahHQ4cvd9pdX_6K71CK8opVOuginY_YvrwplqDgCheGcE7obYuVRTY2VJaGjagqseIE4B-FVVXrrvokMiEuegtg1E8N7cfRL3EqthMrZ3-txwKTBYZW8mZBcZ47w1Wuzn43iqufgK6BiLd_oD4DswMxThRpNbhfST9czBmUjxF1r8mJYNk4CieuUFEyyIrtmTFMCkX7Hz2KYivElxWE8jgIlEc7yD-wby1ttbV8aqZYYsoRXgr_Lt13xgOBKSzmqonB3xHfNfCx8Pxuq6cTImO_O3kIcH3LLcIj0QkQWV8nhPSmK1dO2YGQJeiG2DBPCqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
گل اول اسپانیا به جمهوری چک توسط یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/107769" target="_blank">📅 22:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107768">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اشک شوق قهرمانی و معافیت از سربازی
بازیکنان تیم امید کره جنوبی چهارمین قهرمانی متوالی این کشور در بازی‌های آسیایی را رقم زدند و این قهرمانی برای بازیکنان کره به معنای معافیت از خدمت سربازی ۲ ساله بود تا این گونه اشک از چشمانشان جاری شود
البته لازم به ذکر است که همه بازیکنان این تیم همچنان ملزم به گذراندن دوره آموزشی هستند، مسیری که سون هیونگ مین هم قبلا طی کرده بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/107768" target="_blank">📅 21:52 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107767">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">انگلیس هفتا به کرواسی زده
😐
😳</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/107767" target="_blank">📅 21:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107766">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3svZS0ooJ2I66H3WhLNCP5FQvLaHkCkNEmtC9qwPgat-zRI8cxubJxyd1Q30pIaQ5ZDhqh_ktszUs14OHor96u1cx9lT5z8Vie5TMDqwzZxHL9dPxAPAhKr1HjWfXlStCy5GOQS43DXGSXmsCJv-62LcUdRd_M42nMesy2uOWJJSuPuj34oFBT9VWPybAWKlrq4PKDKdv4W1gmAvepozmzltnWyV_M1SQxj4F0LYuxG1B1DtjIE-dv2G0wEIyzn9pHBHExKTLJBKkgPQT6nmY-zhq6VEXGJ4J9oJ2Ng4jftequaAZ5vThuDUAM_iyDEwIsNRYgEQR7qjQzILA6bwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترکیب تیم‌ملی اسپانیا مقابل جمهوری چک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107766" target="_blank">📅 20:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107765">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXph2F0NtG56tvfXdaYrsWwdfGF8Tq6eMMTFSEyfY72QmKc4ifGw3Q25nW0y6xv21Wdei6VBs7cNCpIKfiPe6sQyxg8ycu_cerkB1PIRvHQySD4R7Zy3UxCkVSqMVCksUZimOdvtry1gPCyjZyexRTaN4hDWUIYjN4XquuwBE9K_MnCHRtI0B6qiXt2E-VKar9eTGNFd9WUOHk6cGq0ZJXhLsB0LrY12kSx5K_QqLDKyAVIj43kITJF-iTsU-mOkD-Rc_n-vcGn0TM5PCm_8p7xWxoBOEiWC1Qs52AT3mCiguVjDqom3O_mgzAPWtcfX_1kPcY899i_HUOdIIUS7TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
🇧🇷
در سال ۲۰۲۲ رافینیا از لحاظ تعداد گل های زده شده در مقایسه وینیسیوس بسیار عقب تر بود اما او امروز توانسته دو گل بیشتر از وینیسیوس به ثمر برساند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107765" target="_blank">📅 20:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107764">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4IltgvkgfwZtP624X-YKWY2STuc_aHA5pxBCTHT1P25fdIKr1gInNmFpGjFHCpI6P2j2WYIjX3OGTp0zfnXr9INHXKPhsyPzMAikrerWH5FXI5-OzNIj8uDZw-blvReApwus7bFsC3AwEi05v0kdottScn3jE-TD-hGYyLYiPSW-L41msI-M_gA-uAuS7Hge2r0UpZecMjBmm4JoguKlrZtE2MyOct-gSlb_cBGBXbsbEWH_QOo0dHkm08KFvplRoJqmtGinomf9IgPQHK3D6QxA-qsopwziyN1YJ3VURLA5rb1M-lW_-BfNmqRoyEJ0ynCLtb4jSDNd6IpdlKcmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
ویرجیل فن‌دایک در سال ٢٠٢۶ به اندازه کریستیانو رونالدو گل ملی بثمر رسانده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107764" target="_blank">📅 19:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107763">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsLc39PKvNz5b9njfPK9FwSIqKH-oqO-UgdOj6e2J6sJIzuZhjULRo2CldxIgdnZ4Ifzske_G8NlWdFbTnTpJNDaya2yWMPGZTiMWYm4JwzILzUzfqxXtFvNTRFseRZ0qPC0YEgoggXGYdgqDdfCa6uWbwTo3mrha7Uk-gxPApsBGd0YCp64S_Z-HGdx0IEQ_ljUuifDTCkzfQLso1n1OpPrvA4lvbOuArIy2UiiAiteg1GHloyCdLkN6T2wKaeJamCRa0jsndADa0GsRRT66cdEzHheMIV6ksqOnU-XbSG_u8LGaSbBvZzydDF6gMRFlCySfQpxCLn8k03XRz66IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
روبرت لواندوفسکی پس از هت‌تریک برای تیم ملی لهستان در بازی امشب، شادی گل معروف لامین یامال کنار پرچم کرنر را تکرار کرد
🥹
🚩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107763" target="_blank">📅 19:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107762">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f408d58b0b.mp4?token=j7NdWejDYgSIe5ojRH6qHcBBB2ewl_2FxqvEf04sSz4KhMfGxLrGqqGExWJnlmd-JDhHqgaLReDEJtd8tWhe-TRDWkRJIabFcOCA6rX-HXtzb3lVg5_VY22ikk-xqEk-eDzRdVUB6W2oNKcXTAOX27e5LWL5vRFiuWAfJKUm37UrAM37h4xaeM_xO49ioNjbiXgadtGILbSsKQnSMAZ0wwGCq5JAo8Zp8R-TGTWuYX1HcyctkIguDuK7rAYoincZphxUVVni4YuAaikZKPwSzOGVz3MoXcfn3thF9PRJz4HNHZl1rmirsLYbXeJRszeO0Y8CN-vrnGS4fveCLTdQBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f408d58b0b.mp4?token=j7NdWejDYgSIe5ojRH6qHcBBB2ewl_2FxqvEf04sSz4KhMfGxLrGqqGExWJnlmd-JDhHqgaLReDEJtd8tWhe-TRDWkRJIabFcOCA6rX-HXtzb3lVg5_VY22ikk-xqEk-eDzRdVUB6W2oNKcXTAOX27e5LWL5vRFiuWAfJKUm37UrAM37h4xaeM_xO49ioNjbiXgadtGILbSsKQnSMAZ0wwGCq5JAo8Zp8R-TGTWuYX1HcyctkIguDuK7rAYoincZphxUVVni4YuAaikZKPwSzOGVz3MoXcfn3thF9PRJz4HNHZl1rmirsLYbXeJRszeO0Y8CN-vrnGS4fveCLTdQBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
ترو خدا هوش مصنوعی رو از ایرانیا جدا کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107762" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107761">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsYaius3CufDqDDgnewrZ87grfdoop6QP-_y444OL5tvk6O1bO5tKq-4tgrrNBmHtTRUteawlICM9X-rjKs1iEDIHEaGIw_kpUqDlLGwTwEtEUV2TaOqMAPjCx2UaU2qM6KwxJETp0ykzL-x5h7HKuJW3dIlTah7rvlLpKTnSjXDM_kSUV7tKIuqsP5IdWaBMO08jotXEJk4i6dzGfkGkUzviR67RP2fuBscT4fPdabPQAOo9379GeZh-zYYLG_Mg9lqeTnFKGGERk44DWdiIgIvU3ZGGqSy3q2cjnxwSl0GfYc-l0F03EwGgl8ybr5Kh5iIiRW1N6EXVp0fFKQUNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇭🇷
ترکیب انگلیس و کرواسی؛ ساعت ۱۹:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107761" target="_blank">📅 18:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107760">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58fe91d1ea.mp4?token=Ohc1y4YZn7OUhMrFUXNcVN3s57N4y1vgTLkfRtTC_ttH8-VGbUuqvGoUJb8BmPmRiVX_DDts7cXEW8AP1X8gl2FhPywjyX1aVcHL9MVY2Iw8Ze3yE1nB2IO0klBuPGc3Wl-85ex_GHgLHQRVSwl_d8hUJOw7zZIp9okO0Hw3EFL3ABD0mhDarvU2l3DUupKp7LWh1Dz8mPex870n_OgghuvtUWnBhp0Pz7U8PbJ0MPBp6Il_foEobeo83HI0I109ezyQDaaL8QTODml0RF4kxy0WM1YRsj4Y-eN_1kUmcxh69z30j5EBn3jfdBN8Ei1j9xl67nDXPA4PPqbMB17XKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58fe91d1ea.mp4?token=Ohc1y4YZn7OUhMrFUXNcVN3s57N4y1vgTLkfRtTC_ttH8-VGbUuqvGoUJb8BmPmRiVX_DDts7cXEW8AP1X8gl2FhPywjyX1aVcHL9MVY2Iw8Ze3yE1nB2IO0klBuPGc3Wl-85ex_GHgLHQRVSwl_d8hUJOw7zZIp9okO0Hw3EFL3ABD0mhDarvU2l3DUupKp7LWh1Dz8mPex870n_OgghuvtUWnBhp0Pz7U8PbJ0MPBp6Il_foEobeo83HI0I109ezyQDaaL8QTODml0RF4kxy0WM1YRsj4Y-eN_1kUmcxh69z30j5EBn3jfdBN8Ei1j9xl67nDXPA4PPqbMB17XKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚪️
احسان حاج‌صفی: سعید الهویی، هومن افاضلی و رحمان رضایی جزو بهترین‌ها هستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/107760" target="_blank">📅 18:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107759">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
‼️
کنفدراسیون فوتبال آسیا برای فصل آینده مسابقات تنها ورزشگاه‌هایی را قابل استفاده می‌داند که دارای سقف استاندارد باشند و بدین ترتیب تقریبا هیچکدام از ورزشگاه‌های ایرانی شرایط میزبانی از رقابت‌های آسیایی را ندارند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/107759" target="_blank">📅 17:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107758">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxdopRhKSpNyt5SVK5505vsG4h4V9gexyPWOA_BGSsW-1OiinOBnCfmB-YD_5vHOGvS92RssmAlH5Otv2kxCV7St_FvtxRJn800OjN12RySVkHP4f4AQxTNAEuFbgo_yp19onc1yJXplwXZkkxMeYUDcdGWpSOGLjiawhkSVsoO0Fop5UuwH0gC-R7QcBnQ63btg-yyROLH-rozWQB32vEwnUQYekuSR-LJ_luZJIY2bYOVV5puhfR3Io_OctcChSHp3P6iDOzGAMmzIk2tBvC6pgI8TSrYz7JGE1DreIkgXS_i6uQg7m8n-M-NueirDDrsRXdYV2TY2Du1RcCeCTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💵
دلار به 271 تومن رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107758" target="_blank">📅 17:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107757">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfd85597f0.mp4?token=fiIiAs9SQAu-2FTpHqP2Gnh5sBScrgOHl4fMy4h6XqN0tobGWfNrQX6sHKt-XHV5rX3AQmM35di-8_xTTQjFtMNvVS6BHUTKsel2B1DCWj1O1tnFLV-VeIqXRklM6u__-65DCYat7Ma2GalsBPjShm9t7uPdj_P6GdqLJWnuHFCU_K06i9sXgs8PkbcNXirxxLKXPonubQn5SRlcq3z7BEBb0FEOM6vpRwysxy9cYsr2ji-NifKDfW-qZA2n7smFgafq1Oq6wnhs_dvnliHNnDLKmCGEeu2TwpuBqmxd9YRTodk1qVFUk2z23qu_UlhGbeItZopfLfYGeGy99XSx-mC8QtVw2gRC9xgiV4hmgXs5_HB2xyk5E_AKUSYY7jDdVwgN4vgw5J7S7PdHz-XV_r2C0J0tyjzF0PmUFF3RY_LMvCKZAZewY_CZl-t8QDTlLFbyevew84_9FHpinu1Sv6I9g5Hbu16fBpRAMSuAd87z6gPa7z9GdYjzt7dzU_TdQzccuYak6PEGQAYJ_3-uYIJaRQ0kATvuCrkGOHHapRdbYhWLx1agttjfcgYig9GnV5_0o_LMXJ0XU77yQjhWbdPpRYSXpgXp59vVAdx-DdkK9tqjS9iKgmRe3shMsXNcJ1M0ZnovZEJn8Z8Qu1e_-EG65AVQBzQhpRbVaPckjdM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfd85597f0.mp4?token=fiIiAs9SQAu-2FTpHqP2Gnh5sBScrgOHl4fMy4h6XqN0tobGWfNrQX6sHKt-XHV5rX3AQmM35di-8_xTTQjFtMNvVS6BHUTKsel2B1DCWj1O1tnFLV-VeIqXRklM6u__-65DCYat7Ma2GalsBPjShm9t7uPdj_P6GdqLJWnuHFCU_K06i9sXgs8PkbcNXirxxLKXPonubQn5SRlcq3z7BEBb0FEOM6vpRwysxy9cYsr2ji-NifKDfW-qZA2n7smFgafq1Oq6wnhs_dvnliHNnDLKmCGEeu2TwpuBqmxd9YRTodk1qVFUk2z23qu_UlhGbeItZopfLfYGeGy99XSx-mC8QtVw2gRC9xgiV4hmgXs5_HB2xyk5E_AKUSYY7jDdVwgN4vgw5J7S7PdHz-XV_r2C0J0tyjzF0PmUFF3RY_LMvCKZAZewY_CZl-t8QDTlLFbyevew84_9FHpinu1Sv6I9g5Hbu16fBpRAMSuAd87z6gPa7z9GdYjzt7dzU_TdQzccuYak6PEGQAYJ_3-uYIJaRQ0kATvuCrkGOHHapRdbYhWLx1agttjfcgYig9GnV5_0o_LMXJ0XU77yQjhWbdPpRYSXpgXp59vVAdx-DdkK9tqjS9iKgmRe3shMsXNcJ1M0ZnovZEJn8Z8Qu1e_-EG65AVQBzQhpRbVaPckjdM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
گریه‌های بی پایان بازیکن سابق استقلال در شب دستگیری در کلانتری دماوند!
❌
خاطره بامزه بابک مرادی از دستگیری بازیکنان استقلال در شب سالگرد ازدواج مهدی قائدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107757" target="_blank">📅 17:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107756">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107756" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/107756" target="_blank">📅 17:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107755">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvNiERxKCQzLvLcWpx9PljuRSbyGZUTTG7G6VGOGvBbfBDpX9UCvQcTy_FyR22RHRYJBXJGYWl7H8tJLC70AmWqu7twRVtdsOmvnRB8CbJhcBEPD_O02dc4BqtlF4XMncbCSaMmDsob3lTMPIcNpHl9afILZSAVLYZJ0X0ofkwph25bi6Tq8rO0_blSl-U2Z_Tf8y7PntdaMOZTMdzT81TYfsr5u1s8f34XWc6r-SvVXdOzmk4KEJ_SVGHenAiCCI_dsUHO8b5iY703GqP7tlWPGfAXjbn1tsRTt2c6nQY486OmxsNRCvAIw5FU3ASdRhItNVwCaQ25mzd7J4KFALA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز انگلیس
🆚
کرواسی را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
انگلیس: ۳ برد، ۲ شکست و ۱۳ گل زده
کرواسی: ۳ برد، ۲ شکست و ۷ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/107755" target="_blank">📅 17:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107754">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967556808b.mp4?token=jGxO8HW_Aw_YqMQ1OvjzPQ5YcY2wua0Vr8nATI-sED2DiRonGZ3nicTztTq2qfa2lpLzQenc3w5cX9TmzJEIyqEzGwfSny2IiN344zXbUrOvAm1fsTnVDEz2haWEgkXvBsdvYOzi40e-g3xoeUY9JnS8TGXYH5WaMFUY78s9ZacMyN3dNpo7otwfneAvTNrq8L-kyZcTYRxdXY5-1J4TRYAWXoMma-qeov_sQ3K1Jffa-rZBjd8YOoURYl-Mv9oIgAojsMTENNKeRH5NgluUWjK579o6jOPr1U--MtLXInXVCsiRmEu4a1P09Eon7XEov6JGGkUut-O9z8sktr_nIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967556808b.mp4?token=jGxO8HW_Aw_YqMQ1OvjzPQ5YcY2wua0Vr8nATI-sED2DiRonGZ3nicTztTq2qfa2lpLzQenc3w5cX9TmzJEIyqEzGwfSny2IiN344zXbUrOvAm1fsTnVDEz2haWEgkXvBsdvYOzi40e-g3xoeUY9JnS8TGXYH5WaMFUY78s9ZacMyN3dNpo7otwfneAvTNrq8L-kyZcTYRxdXY5-1J4TRYAWXoMma-qeov_sQ3K1Jffa-rZBjd8YOoURYl-Mv9oIgAojsMTENNKeRH5NgluUWjK579o6jOPr1U--MtLXInXVCsiRmEu4a1P09Eon7XEov6JGGkUut-O9z8sktr_nIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇸
و بشنوید از مدل ماشین دروازه‌بان اصلی و معروف تیم‌ملی اسپانیا یعنی اونای سیمون
👀
🚘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/107754" target="_blank">📅 16:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107753">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b23bb5ad12.mp4?token=A8a7_Z-c11gu1NoNk49UkO8xbt8AlRXM3KQfcJmkENalqg5zVStqq6EtLd7XHp-kqNxyYvxrJtoSn2qPl8UOTugmY7YLq4RbPwHGfNPbBh_ydgKqyy8UOP8qByICEYtpQJ9KfGe2iZg2V1UWCvPnsYXW8x1C414U5NQW-KRab1pb9fPyAy8Xcb4A4WAtazXNcllIkQA1TsBikpZk21EHvAb5FqztivuXISUqoT6d7JhjJU7tDXsYGVMV9oMzJboOpKYtLlGZBlnTr46zd_wVYIcWmoKwPMxehs9c9w-PNKj3Kg9SR2bCoS73zoK8cKFL6yZBd69ucIfKmOIF-DL8Koi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b23bb5ad12.mp4?token=A8a7_Z-c11gu1NoNk49UkO8xbt8AlRXM3KQfcJmkENalqg5zVStqq6EtLd7XHp-kqNxyYvxrJtoSn2qPl8UOTugmY7YLq4RbPwHGfNPbBh_ydgKqyy8UOP8qByICEYtpQJ9KfGe2iZg2V1UWCvPnsYXW8x1C414U5NQW-KRab1pb9fPyAy8Xcb4A4WAtazXNcllIkQA1TsBikpZk21EHvAb5FqztivuXISUqoT6d7JhjJU7tDXsYGVMV9oMzJboOpKYtLlGZBlnTr46zd_wVYIcWmoKwPMxehs9c9w-PNKj3Kg9SR2bCoS73zoK8cKFL6yZBd69ucIfKmOIF-DL8Koi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
✅
ویدیو کاربردی از نحوه جدید سوخت‌گیری که به تدریج در کل کشور اجرا خواهد شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/107753" target="_blank">📅 16:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107752">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b48e9e7f4b.mp4?token=e5nDSRW9PjIXJSF7POIo9mORgBDJWJQBFUO22o6-z69TwHb9ekQFQUMJm6dBpkVkBSiv030HeLOl7cM24_h6D6Fl_YI2q0Y01anIhKex9cNYDtSNDH2aoWwJbl_gDbtYDqu7xLIJEPQFm5llVs9jJ0Oh2YDwpOG_dR3sfBKZUQupmwUAyJQzMsfgFBFOH5B1nUVAd9js3oBS0-WlmwV9dVmiQ7HrrPaA-9YApyv6OGKmpH9JLxxcZB89ExGKK449hcpfOtP9aKEd0evU8fMm_B5L_qL330EIFoJ1HIMv-DFQvcqKZHFopmjshuf8Hv8_iZPCLFO8vyl5_hmz0b62zx3W0fpusrpp-B1piQVNFxLUajXokuV0dt7Rnf0ubODnXNI3uonH4-BuDp_p0OeBEV8EplUtFy2fJUrW6VRjfJO3vbqzk-EN3vry-UDq-q-bB5IM_06b3PLy3lbA6xJN1yR-vtkIrsk92qiSNCQIHGZugh_SgwQ8vblOQsw_eX6lQlDc9ccG1G7W7dpup3rQ3TVQ4BzkbMgXWnQrPAtolQYKEDJ_zyyUR0CCtZipDNNLdElZnLk2T5c9z130fXa71mQtbG9C9HO6AM63pRG1IxfhBbeBr6qc_96Sg0VxdjoEKLyY2TQ3oslihh0MgHnZYBWOCwu67-PaHkYGgiYL3TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b48e9e7f4b.mp4?token=e5nDSRW9PjIXJSF7POIo9mORgBDJWJQBFUO22o6-z69TwHb9ekQFQUMJm6dBpkVkBSiv030HeLOl7cM24_h6D6Fl_YI2q0Y01anIhKex9cNYDtSNDH2aoWwJbl_gDbtYDqu7xLIJEPQFm5llVs9jJ0Oh2YDwpOG_dR3sfBKZUQupmwUAyJQzMsfgFBFOH5B1nUVAd9js3oBS0-WlmwV9dVmiQ7HrrPaA-9YApyv6OGKmpH9JLxxcZB89ExGKK449hcpfOtP9aKEd0evU8fMm_B5L_qL330EIFoJ1HIMv-DFQvcqKZHFopmjshuf8Hv8_iZPCLFO8vyl5_hmz0b62zx3W0fpusrpp-B1piQVNFxLUajXokuV0dt7Rnf0ubODnXNI3uonH4-BuDp_p0OeBEV8EplUtFy2fJUrW6VRjfJO3vbqzk-EN3vry-UDq-q-bB5IM_06b3PLy3lbA6xJN1yR-vtkIrsk92qiSNCQIHGZugh_SgwQ8vblOQsw_eX6lQlDc9ccG1G7W7dpup3rQ3TVQ4BzkbMgXWnQrPAtolQYKEDJ_zyyUR0CCtZipDNNLdElZnLk2T5c9z130fXa71mQtbG9C9HO6AM63pRG1IxfhBbeBr6qc_96Sg0VxdjoEKLyY2TQ3oslihh0MgHnZYBWOCwu67-PaHkYGgiYL3TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عجب دوران‌کودکی جذابی رو‌ پشت‌سر گذاشتیم...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/107752" target="_blank">📅 16:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107751">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9d2f3d6a6.mp4?token=ALhoXvt3fGD_5MIrVfF71E8NZ73wZXvBrMYAUjU75WSJwb48GCqd1LwHntC-vdMxhtSsll051ysUadAYykDM6guOMksjwwDz5H4CheZJBD-rj44HcJVefDHDWqVbjReTlaom7LD_7jkoko5FWP0LEmIu6DXbRl6tdl1m59kBBNG1X8vHcgu3mT4deErGprLlwEn5Xc_6DrOVl5txg2hvE05Oqxv9E1D-9tdO4a_mXAH2Dn1nUeXLlsoKpXVywxnVubXkiMsl7BPyz-igFETHeXXQai5a4rF_HyfpvC8Cft7jrRysZ1ek37LsSiUPnw6BnDCrMvyM0n8VDfxqqXuKfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9d2f3d6a6.mp4?token=ALhoXvt3fGD_5MIrVfF71E8NZ73wZXvBrMYAUjU75WSJwb48GCqd1LwHntC-vdMxhtSsll051ysUadAYykDM6guOMksjwwDz5H4CheZJBD-rj44HcJVefDHDWqVbjReTlaom7LD_7jkoko5FWP0LEmIu6DXbRl6tdl1m59kBBNG1X8vHcgu3mT4deErGprLlwEn5Xc_6DrOVl5txg2hvE05Oqxv9E1D-9tdO4a_mXAH2Dn1nUeXLlsoKpXVywxnVubXkiMsl7BPyz-igFETHeXXQai5a4rF_HyfpvC8Cft7jrRysZ1ek37LsSiUPnw6BnDCrMvyM0n8VDfxqqXuKfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⚪️
بازنده‌های پر سروصدا یعنی اعضای تیم‌ملی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/107751" target="_blank">📅 15:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107750">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhy9EdnXRPc30bmjUsTtWZru-EjOOS9xEHmlyN5UHuA_uupXHeeCZ1rUnZEl5-CPgmvTyeGruy3zw1fckzZmZW4QRclOUlyu6NYJgU8qm0a-5WgI5_JOsWHO3f9vWg9bvDFq4dXK41ER3F0oROaKI5xiQRJ2fd45P0sfzUmUmhPzrNz0z2tVt-6A26TeDDuUS6X8CjiKwn1HqGzfcvms2FxJh_vkObEIhPK1Shbl0_wbTklFmhJDIFt5NqH6xRf4ZJKf97ZfkYB1VxqcHcOJp_YEO7Gd4gEZ53Teo133Fq8oYeaOMmMnz96II0Hlhs6p--OTDtTDboq8QsLDsPl_cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇺
میسا رودریگز "تحت تاثیر" قانون "پنالتی به سبک مارک پوبیل" قرار گرفت که اکنون توسط یوفا اعمال می‌شود.
❌
در بازی پاریس و آرسنال در لیگ قهرمانان زنان، یک حرکت مشابه حرکتی که مدافع اتلتیکو و دروازه‌بان موسو در برابر بارسلونا انجام دادند، به عنوان یک خطا (پنالتی) اعلام شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/107750" target="_blank">📅 15:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107749">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🇪🇸
رومانو: بارسلونا پس از فیفادی قرارداد سه بازیکن یعنی رافینیا، برنال و ژاوی اسپارت را تمدید میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107749" target="_blank">📅 15:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107748">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86371ca1ee.mp4?token=n_slhyvr_8X-4mH85LnbcxDVZz-9nW9anS-9cf9ZauP3C_hJKsNubCGucXpqHVBHJa2cl5agX6FinPUP7YAcRHDU-q-Xe8cNNCYeolErPSX4FWBJZvzANgNLUGmaGOM8b7nhjALDH0aTPvdXFS1q7RnN3nwlBRLO2Yuj9arnPTDJT_IjROTBFbuGY7dSFMTsZOoOGa7-rhuSwhQxuKxzp16Au8k4NoO_3BgzfTby9nfAikRSvYd9-j_P2qkLmf5BNkw1pMUqyLS0TejzD_dIrK6x73rCTpjHXU6YOADyLv8zPmWI0fGuspJJ89-bbWxzy0TkevljKhLt66kWqGsCxTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86371ca1ee.mp4?token=n_slhyvr_8X-4mH85LnbcxDVZz-9nW9anS-9cf9ZauP3C_hJKsNubCGucXpqHVBHJa2cl5agX6FinPUP7YAcRHDU-q-Xe8cNNCYeolErPSX4FWBJZvzANgNLUGmaGOM8b7nhjALDH0aTPvdXFS1q7RnN3nwlBRLO2Yuj9arnPTDJT_IjROTBFbuGY7dSFMTsZOoOGa7-rhuSwhQxuKxzp16Au8k4NoO_3BgzfTby9nfAikRSvYd9-j_P2qkLmf5BNkw1pMUqyLS0TejzD_dIrK6x73rCTpjHXU6YOADyLv8zPmWI0fGuspJJ89-bbWxzy0TkevljKhLt66kWqGsCxTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
مهدوی‌کیا: دوره پرولایسنس در آلمان در یک سال برگزار می‌شود؛ در ایران ٩ روزه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107748" target="_blank">📅 14:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107747">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e10be0d86.mp4?token=KdxyZRvbHH1Pr9MAw2ZNOWR0X_jxsXUVJcnxqB6I8YTMuw8f5EPpzmfmO2bt17VENpVQHyam6xTdaPDL1XaEHoLYZU8WpkGQWJUGvSTHT1t33KidPZD340rMOlN7-a7LlJLdrPH9iMckD3wiFMOXfuPGQpD86BiEpzhUZQOAjdSAtqJ2QwLr6fpmk0FZlBIxG1sKxb0Z2zIQZkKpmSoaT1-pJklq8Zol-HsJivwPJO67ctsUzbIysLwTtAnPfG0_EDGMttZ0Odh7fHb_gpHL7sXtMByLbwV4p0M_OFu-MNhK15Tf9rqv3q__oRn-SdvkoFvl2yC3QpAVUTW4CrlUHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e10be0d86.mp4?token=KdxyZRvbHH1Pr9MAw2ZNOWR0X_jxsXUVJcnxqB6I8YTMuw8f5EPpzmfmO2bt17VENpVQHyam6xTdaPDL1XaEHoLYZU8WpkGQWJUGvSTHT1t33KidPZD340rMOlN7-a7LlJLdrPH9iMckD3wiFMOXfuPGQpD86BiEpzhUZQOAjdSAtqJ2QwLr6fpmk0FZlBIxG1sKxb0Z2zIQZkKpmSoaT1-pJklq8Zol-HsJivwPJO67ctsUzbIysLwTtAnPfG0_EDGMttZ0Odh7fHb_gpHL7sXtMByLbwV4p0M_OFu-MNhK15Tf9rqv3q__oRn-SdvkoFvl2yC3QpAVUTW4CrlUHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
😳
ویدیوی وایرال شده از کلاس تخلیه گریه برای بانوان در تهران! این خانم‌ها برای تخلیه احساسات خود در کلاس‌ها پول پرداخت می‌کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107747" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107746">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd4b89af76.mp4?token=AJH3ByaB5mn5Z-aLqqLREFN52o-_Lrd94FCNVwB0tp3YxkMkGO7syxzMY0Qj6JjjunvVB_R9UccYcjhpValvwxR_UrqRsX3uJq5DVQ-4Fu3qIHWZhnTT0Xq4EANN00Wke1K5ZVjpbYb8UpVPbTkSfpbnoVeqVi_taO8QWUWhpJ_Q3AxFZ3FsFtkO_MKYyiaTH5E5IWz_EexMhwVmROi6WRD_gjSxCNjAua3fHhPerAnDKSyThAJtTgigH-BrOLJosUkIAd1sRSEETEUNI0iuC5PT6Oa5JipXswEV-4hAb_lxnNHkBaZ1BRDl_KorWLvj8De0IEuGDiTxZ_68jP-oQLZSryAWF5FPJVo9BsYoxAy_-5wDEaLikEJywRyJB-ciVCCkM35lDwzjpLZjkLdzhVlAnveyZBelc_Y5U2qedIDZ9e1GYEheeGiBzZrib9gfImdJ9eOVI00LrvGkhBca2b_PQhzV9nqrovwlTBhkWypwlQjT2ZFGzjkGftjDRs2Cu8NAsynpLJkhYd01modT0K77uVq4IOzBTRRMng-Wpyvfct-1ImUglxPDsp-WuwM_5Pw-RbjhAr2FYpQHErSBQfFC8RXAOFu1OYqNdgNqBPjP36lupn5D291zxEksljnX_55jRTFIhC8a2zZMMf1-OT0MCsEEHKvwk5XN8T8e9ro" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd4b89af76.mp4?token=AJH3ByaB5mn5Z-aLqqLREFN52o-_Lrd94FCNVwB0tp3YxkMkGO7syxzMY0Qj6JjjunvVB_R9UccYcjhpValvwxR_UrqRsX3uJq5DVQ-4Fu3qIHWZhnTT0Xq4EANN00Wke1K5ZVjpbYb8UpVPbTkSfpbnoVeqVi_taO8QWUWhpJ_Q3AxFZ3FsFtkO_MKYyiaTH5E5IWz_EexMhwVmROi6WRD_gjSxCNjAua3fHhPerAnDKSyThAJtTgigH-BrOLJosUkIAd1sRSEETEUNI0iuC5PT6Oa5JipXswEV-4hAb_lxnNHkBaZ1BRDl_KorWLvj8De0IEuGDiTxZ_68jP-oQLZSryAWF5FPJVo9BsYoxAy_-5wDEaLikEJywRyJB-ciVCCkM35lDwzjpLZjkLdzhVlAnveyZBelc_Y5U2qedIDZ9e1GYEheeGiBzZrib9gfImdJ9eOVI00LrvGkhBca2b_PQhzV9nqrovwlTBhkWypwlQjT2ZFGzjkGftjDRs2Cu8NAsynpLJkhYd01modT0K77uVq4IOzBTRRMng-Wpyvfct-1ImUglxPDsp-WuwM_5Pw-RbjhAr2FYpQHErSBQfFC8RXAOFu1OYqNdgNqBPjP36lupn5D291zxEksljnX_55jRTFIhC8a2zZMMf1-OT0MCsEEHKvwk5XN8T8e9ro" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇹
یکسال پیش در چنین روزی برتری پرتغال به رهبری رونالدو مقابل اسپانیا در فینال لیگ‌ملت‌های اروپا و قهرمانی در این مسابقات!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/107746" target="_blank">📅 14:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107745">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9decbe8c9.mp4?token=quFPAjmM8fI3S56DEj3NruPLnnrJ7B-POa4WE3YeqjseQKCJoLK7zODJgn6qWMc9M273K0dnam6hIACd_6e9_pQsjET5pYWzpetMGUHiEnPWk-yc7b7B2fXJF9FifGv96t_ci23m9qy5WFH1XlGjHkJCtojpflEbNy-VLmU6axI5YHnB5gyt4oKwFJHNXbVtif6CZ68N5FDGcLxIOF1lGluf-ncJu1WSmxo1dOraWIfjG88gw11HJc9KNOgzn5eFb-y-3f-Ae9msPUrItn60OHOquVXO-ySe2UugBiRxhDKOwmgqDfxDyqhdRCVrofkHBPekmitRaaqYMtmM-wTIxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9decbe8c9.mp4?token=quFPAjmM8fI3S56DEj3NruPLnnrJ7B-POa4WE3YeqjseQKCJoLK7zODJgn6qWMc9M273K0dnam6hIACd_6e9_pQsjET5pYWzpetMGUHiEnPWk-yc7b7B2fXJF9FifGv96t_ci23m9qy5WFH1XlGjHkJCtojpflEbNy-VLmU6axI5YHnB5gyt4oKwFJHNXbVtif6CZ68N5FDGcLxIOF1lGluf-ncJu1WSmxo1dOraWIfjG88gw11HJc9KNOgzn5eFb-y-3f-Ae9msPUrItn60OHOquVXO-ySe2UugBiRxhDKOwmgqDfxDyqhdRCVrofkHBPekmitRaaqYMtmM-wTIxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
یک شرکت فرآورده‌های گوشتی به این شکل کاملا منطقی تبلیغ سوسیس‌هاشو کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107745" target="_blank">📅 13:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107744">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c197e3a2a3.mp4?token=rP-Y3J9rz7LqNcHjb4k_tItCfk_7ymL4RxL_ghvMQ0rkLXXJRRnrYbZVBjPXHEY9Tgje1L_hdUFTogdbJelAZzxR39r8r1tr9iI1Kv-drRZAhDg731nGb9JYl5FYBrJGoeLDCvRgHbJE9oEISiKDMUxhqU_4Jhk9O_9PLOQ0-R-dE1IfBAU95N6Lxrs2jKtoGDCvLU6mimE5v8Z109e_LvZ8RXdpnK_kr08T9IgJzExOxc6cFB_Z010YgBoqmTwd6541_WRM9g4xyCvfNUqUno68a_psUrvgc-vssQ9Azk_by30Wd9ZMDjw4nVjlujd6EFCHOmCeElrr1ZgOWW6XwKnrrYBNU-oecVOph83VZng1XfUE1BBYoGdu-zSHHV9RV-Qrd719O1sH2WAVKH1eRWBVUhBWQfrEcahht1__elhstBUOQ9af9pmRxaxWGnIupVr4Fp0cYkE88GF7EiPeB2gUFnwuLuRBkJvW_5EkpVg00sKB9BgeTfRoU_Yiw7RrLE16L6l3r0qFb967zOeRjDmw3Y-X1IEEmorpuTXXfn6p3C3rZgpG8NG4E8X-n6gLU6n1x_dWQ4pmZKC9l6RmpXDvIkcsqJL2bN04SLo_eeNWX1i2gM5_PRwwGwcFdRH8E_DYt-ryycI-GjZNLsU_akz6mDWUXfJQe3JE-fgGnAk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c197e3a2a3.mp4?token=rP-Y3J9rz7LqNcHjb4k_tItCfk_7ymL4RxL_ghvMQ0rkLXXJRRnrYbZVBjPXHEY9Tgje1L_hdUFTogdbJelAZzxR39r8r1tr9iI1Kv-drRZAhDg731nGb9JYl5FYBrJGoeLDCvRgHbJE9oEISiKDMUxhqU_4Jhk9O_9PLOQ0-R-dE1IfBAU95N6Lxrs2jKtoGDCvLU6mimE5v8Z109e_LvZ8RXdpnK_kr08T9IgJzExOxc6cFB_Z010YgBoqmTwd6541_WRM9g4xyCvfNUqUno68a_psUrvgc-vssQ9Azk_by30Wd9ZMDjw4nVjlujd6EFCHOmCeElrr1ZgOWW6XwKnrrYBNU-oecVOph83VZng1XfUE1BBYoGdu-zSHHV9RV-Qrd719O1sH2WAVKH1eRWBVUhBWQfrEcahht1__elhstBUOQ9af9pmRxaxWGnIupVr4Fp0cYkE88GF7EiPeB2gUFnwuLuRBkJvW_5EkpVg00sKB9BgeTfRoU_Yiw7RrLE16L6l3r0qFb967zOeRjDmw3Y-X1IEEmorpuTXXfn6p3C3rZgpG8NG4E8X-n6gLU6n1x_dWQ4pmZKC9l6RmpXDvIkcsqJL2bN04SLo_eeNWX1i2gM5_PRwwGwcFdRH8E_DYt-ryycI-GjZNLsU_akz6mDWUXfJQe3JE-fgGnAk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🥇
کامبک جانانه یونس امامی در مقابل کشتی گیر ژاپنی و کسب مدال طلا بازی های آسیایی ناگویا با گزارش ابوذر کرمی نیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107744" target="_blank">📅 13:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107743">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnpqjvDqCg6qCRet0Oxw78HIKw9QzmWSsElcEBbBX7Hx8EXufmnjxu-ORASRVAaZOlvjjCORLYCI63iOWnQ8km2_FJU18Q8lYUwk-RNZaq6dJdpnLZe16XCuILPYrS9sA3OZ0XKqWz-7eej0dghHx1RfsX6FYwCGHAE6SUoiqYvYvppeCFnMg9zMiICwD4SWfWG-gitcYlaGmW2cpBTsP8UTAZX3DOZaMMkpBW3Us6jciZ6-i3vfY79jYOxT3iTsCNH59RJhFF0Mba31ALGsXjvSlKT2mIF4R3xoLfEpx4MiCGulci5A9LaZo662TStNGz2eFdSvnicImyPIL5PUaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
رافینیا در این‌فصل از مسابقات فوتبال:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107743" target="_blank">📅 13:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107742">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/096e7cab86.mp4?token=f4z1qpXfllLXGM2mrIbL89Pc7UHwbPJoi4VxOgoJbMYjQ5n5ws0pxpZhoV44aF3vHr33l18pfPT_hrOkpuhmkrKE0Vl5eKWQIecrJaT8jU5cmqpVMMv4YrHU5juknYRyesizZhV6ckLxTC9bdZjPwb1oFddzdT2-7jTF80EOq12vGF9eUX0GjlrFuK_ufEhbsvZVopbtThzxHB4LMHddnDmXZBExahcUJ2Di7Lzhq5a5_i-mhlgZL1KYXWtx3L8SGY-yQudK-HbC5ScuDsVOBpTGgwKpymdq3jiTTXfQcZXDsmmRL2n6-jLiOMpql7SsHMxsOm3b2obx_NmRh0Hlog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/096e7cab86.mp4?token=f4z1qpXfllLXGM2mrIbL89Pc7UHwbPJoi4VxOgoJbMYjQ5n5ws0pxpZhoV44aF3vHr33l18pfPT_hrOkpuhmkrKE0Vl5eKWQIecrJaT8jU5cmqpVMMv4YrHU5juknYRyesizZhV6ckLxTC9bdZjPwb1oFddzdT2-7jTF80EOq12vGF9eUX0GjlrFuK_ufEhbsvZVopbtThzxHB4LMHddnDmXZBExahcUJ2Di7Lzhq5a5_i-mhlgZL1KYXWtx3L8SGY-yQudK-HbC5ScuDsVOBpTGgwKpymdq3jiTTXfQcZXDsmmRL2n6-jLiOMpql7SsHMxsOm3b2obx_NmRh0Hlog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
میکروفون باز، کار دست گزارشگر داد؛ جمله جنجالی هادی عامل علیه حسن یزدانی!
🔻
در حالی که پیروزی امیرعلی آذرپیرا مقابل آرش یوشیدا یکی از مهم‌ترین اتفاقات صبح کشتی ایران در بازی‌های آسیایی ناگویا بود، صحبت‌های پشت صحنه و خارج از گزارش روی آنتن زنده، یک حاشیه بزرگ برای کشتی ایران ساخت.
🔹
❌
👀
هادی عامل: صبر کنید ببینید اگه (یوشیدا) تو مسابقات جهانی به حسن (یزدانی) بخوره، ببینید با حسن چیکار می‌کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107742" target="_blank">📅 13:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107741">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b35b732453.mp4?token=rdSplSXen1FHjiH_m_hEB3faK_W71fMk4nxqfc5FO56Ao_oLIK8G-B6c02RbrlpEUyvaVJiOC2un7XMz602htAhyeHATfMHRig8j2WDVvI5BEWysvnPXexpW2i-ScAMFWPjXva11FSXoGmwBoxKa3ndcAFg9Rqbn_fsUUbl9o9jQ4zY2IQ1JhKFSYmCkiqDruenYt0nTzetiI8JGqv1SkUIBybJfX_EvOc37zDLdAn2cO2O09RS6y0vTKhhh8gdNBNqEgoxT3CXosqqOL-MbnF-WioNih6jB_bQ9N0rXMIRoe3Nri8i98AFWwNEmRfMCrc0yIaoGa_FtSSHWCeZFbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b35b732453.mp4?token=rdSplSXen1FHjiH_m_hEB3faK_W71fMk4nxqfc5FO56Ao_oLIK8G-B6c02RbrlpEUyvaVJiOC2un7XMz602htAhyeHATfMHRig8j2WDVvI5BEWysvnPXexpW2i-ScAMFWPjXva11FSXoGmwBoxKa3ndcAFg9Rqbn_fsUUbl9o9jQ4zY2IQ1JhKFSYmCkiqDruenYt0nTzetiI8JGqv1SkUIBybJfX_EvOc37zDLdAn2cO2O09RS6y0vTKhhh8gdNBNqEgoxT3CXosqqOL-MbnF-WioNih6jB_bQ9N0rXMIRoe3Nri8i98AFWwNEmRfMCrc0yIaoGa_FtSSHWCeZFbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
گزارش‌های مستهجن و عجیب گزارشگر تکواندو صداوسیما در بازی‌های آسیایی ناگویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107741" target="_blank">📅 13:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107740">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2uxrbP4Rw0o4GMJTN25gOH4tOaa4XAqftcNk4ylw8T02Y3jzh5EN4MTZmbBg3j4gkzbDG5ug4i5I7Il69_9bRF9IqBSt5VdliY6quYDFHt7THX24TxcTU6UaoK55BM3MD3eiFPmtZqifYztu61na41F0zCuA3QX3CH-PRVe_biIoKL68XVgO6fW3avXCramdFX_06XRSSM5ZNyOrYSEDnVvreCc2L6TWv9ciYBgBB4B1xPEb8YUe778VpWnXm-_XaN3NDb4ln_8A82-gf9_sjINv8C_QQM6iLpt-FVFmZ0XefHM6KJ1DOwiYrMgZaXhEnDpck_dHAzel4K4lh6Nlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
📊
برترین گلزنان تاریخ‌بازی‌های ملی؛ حضور اسطوره علی‌دایی از ایران در رده سوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107740" target="_blank">📅 12:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107739">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/888405197c.mp4?token=ThG6tFU-iZ2GXa24GRbu9z5kSKfHpFeDtINpTNAr9hiAOnVNg8p7ImGLCdokpGGElXnCmuMavz_YW8QGaLz5yLFAXBe8I9Y0jQh2UmOI8DUrsowkGDlr4aSOxcnxeNhVso7JZMkFr0520-2wwgZKCLnK3vI0QSBZ3yNYrV1qpxaul-mq2sUgzGYSdYP4vPrV7Vg3F1tnEOoxpiVaQoZps0I3LwIyrr7GV6UNlMYpHz6hHISneo9zAUQ8b9yj7j0dn9Z3-pGrIWJPh2lR_GT6xLhOEBrd6UmUxeYMEf9RNEnAyFGBzjNhal5xq5gRmpWys5QrBFc1k2y6j9wp5IrIcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/888405197c.mp4?token=ThG6tFU-iZ2GXa24GRbu9z5kSKfHpFeDtINpTNAr9hiAOnVNg8p7ImGLCdokpGGElXnCmuMavz_YW8QGaLz5yLFAXBe8I9Y0jQh2UmOI8DUrsowkGDlr4aSOxcnxeNhVso7JZMkFr0520-2wwgZKCLnK3vI0QSBZ3yNYrV1qpxaul-mq2sUgzGYSdYP4vPrV7Vg3F1tnEOoxpiVaQoZps0I3LwIyrr7GV6UNlMYpHz6hHISneo9zAUQ8b9yj7j0dn9Z3-pGrIWJPh2lR_GT6xLhOEBrd6UmUxeYMEf9RNEnAyFGBzjNhal5xq5gRmpWys5QrBFc1k2y6j9wp5IrIcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
ناراحتی‌ و گریه ناهید‌کیانی بعد حذف شدن از مسابقات آسیایی تکواندو ناگویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107739" target="_blank">📅 12:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107738">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56498866f7.mp4?token=gjcV6f7XLyUdoZ-yyCrWTo0JjNAF_eA_cXK33oi8gPlL0zTLRQ2n0tzi-AU2-Lbh6B0yPCGi0p8ArpggfYC4Kt1mHl-qnJAVWb4jGzvL840hGzKqHSCzMOR1oD2c3v32bEU-BG4zlWaYolzfiWRH8QP46FjZpYjyYOCUEIlqIDNZGLEaZAgwxz1FpsdZ0KnqMWU53HeJywYK6uwi79SVGiT9gzx7I4EV-1j41t2jQi8uGxHhTLK0jkxJRxBIXb68aB6Td_Zsowd8Ggccsy9ymriB7uQ16yPGStJt94vpXdyNlm9EVOZCU4pgG8pDn58k7yxZo7hFh0WhyXRsqjpLlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56498866f7.mp4?token=gjcV6f7XLyUdoZ-yyCrWTo0JjNAF_eA_cXK33oi8gPlL0zTLRQ2n0tzi-AU2-Lbh6B0yPCGi0p8ArpggfYC4Kt1mHl-qnJAVWb4jGzvL840hGzKqHSCzMOR1oD2c3v32bEU-BG4zlWaYolzfiWRH8QP46FjZpYjyYOCUEIlqIDNZGLEaZAgwxz1FpsdZ0KnqMWU53HeJywYK6uwi79SVGiT9gzx7I4EV-1j41t2jQi8uGxHhTLK0jkxJRxBIXb68aB6Td_Zsowd8Ggccsy9ymriB7uQ16yPGStJt94vpXdyNlm9EVOZCU4pgG8pDn58k7yxZo7hFh0WhyXRsqjpLlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
👀
گزارشگر تکواندو رو مشاهده میکنید این چنین در اوج در حال گزارش است
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107738" target="_blank">📅 12:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107737">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dW1I-D5yIZ0VYU3RZg8whvpipAkemamzrUCeSU04viw9iiywIkMXfDLPk8KQ7lw6NEoMwrhj5QolzJTVBbIEBfs_PspdDZV-jXlXUWZHYIKLapnuC8QQAKtUj9Yqu7YhQLk-1rv9TkKJpLH79yIQRGe17n5rE6nKeEyzca9UShiRoqCKbwM8huPoi85F92qepIGQv02sGEThwKYWu-WkUyZ3hcfybnuUqJF-kSaFAzqVStFgtyYB4TGrtP4kpwaG6NP1O2vkbRymGs0lI9LoF2TKkRaWkOgIpD2QGpS9sFccz2Ax4uHWl9wxAK-QWqxuzS0MIbHiDr0OhMlbijeLaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
مسابقات لیگ‌ملت‌های آسیا به شکل اروپا قرار است از شهریور ۱۴۰۶ آغاز شود. ایران در سطح یک این مسابقات قرار خواهد گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107737" target="_blank">📅 12:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107736">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKb7eIRKMNEeBwly_28snI8a8pMCHJlvD_7opjUx2Y1K5C4cRzfqkEcEr4ogQ3MJHm4ITJLYcfb29iQyx6VmO9U4jRD3J5J_20wBkCqbTHh4u4DlFnkJBbSSxy-3IrPu7ciNYkqHVgLjwWuGxLynR4tJrBUWbtNoGUqodtPkTyludfL7-QPFPkHmpQKJFAWkJr8DB_Rq3HypXharGYVD6v13sJ7Cc7FOvxXfJJS2fD5BzDUDq4hw4vgUi4vYXkVLncVOkqujlteNcCBPPHkLqW140ynpHnqUOuw7Fv27Pa6e7eU3_W_U7Tt4B2qKa1I7H2AlJf6CVvTGQfdaDL3Kog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
اسامی نفرات برتر آزمون کنکور ۱۴۰۵؛ نتایج اولیه برای تمامی داوطلبان تا ساعاتی دیگه اعلام میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107736" target="_blank">📅 11:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107735">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6316faf3f3.mp4?token=W-36-ejA3bxLBwE9IGhjbyiUKLPZvTAYCSP_a--TKeTs2Splur1uOGWPc3DUJ6MEadTlJIGbjODRrx4t306PZFcK4cxOjIbimc90GczF04JivaiH3asykIN2TOXjrKW7hFquvMPzNRYahlLSDyK3m09mjwOlLRJHbQXclGanIbv3OxDJU27MLUeBI6Vhj6U8Cje2TLCsYre3TasXyg3ZbUZL53VCvC7GL0thQJXQeGLXs0eHIJI_03ePu0ZyfBHKYDlW4UGoMLXerO--Eoi1ZEE0-U_NT5Sh75QT4r2lI1VdsSCwdxSKOL55-gKqUWY6ztLqmQQdDrbb8ODLkQd26A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6316faf3f3.mp4?token=W-36-ejA3bxLBwE9IGhjbyiUKLPZvTAYCSP_a--TKeTs2Splur1uOGWPc3DUJ6MEadTlJIGbjODRrx4t306PZFcK4cxOjIbimc90GczF04JivaiH3asykIN2TOXjrKW7hFquvMPzNRYahlLSDyK3m09mjwOlLRJHbQXclGanIbv3OxDJU27MLUeBI6Vhj6U8Cje2TLCsYre3TasXyg3ZbUZL53VCvC7GL0thQJXQeGLXs0eHIJI_03ePu0ZyfBHKYDlW4UGoMLXerO--Eoi1ZEE0-U_NT5Sh75QT4r2lI1VdsSCwdxSKOL55-gKqUWY6ztLqmQQdDrbb8ODLkQd26A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
شبکه سه اومد بازی جودوکار خانم ایران تو مسابقات آسیایی رو پخش کنه که جودکار ایرانی تو ثانیه اول درجا بازیو باخت و حذف شد ...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107735" target="_blank">📅 11:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107734">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107734" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107734" target="_blank">📅 11:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107733">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCkQQ6L1FZNd_o2yZSDw0vbeYg0UVL_ait_y2koLtfsEFy3bgQQg86YMDtaepsi_tIOnMZ5HTKwcSB_OrSo6DH0Az56e6VazYkkE4tulDvD_AUqDKmUIG5cHJD4Xd5aLZmA6LWodye98gxRpovD8t0pcHEPtBbMx3tmg-sFpbFUdIaqMmcGhFYTs1e9AbuJ_28dJm13od9xVqFavBBRLRX3MKpUSWzbFz5Uc3k_vWJEmrqLFYp2leZr8iBj7VRVy0y9bsweagsZ2taaJqaS0ezn_3W0yFA4CJpSGA-_8auue8DZWc7Lu9cIV81j7KEYotLIWm6y-6uQc7jHAz4mn7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
انگلیس
🆚
کرواسی
چک
🆚
اسپانیا
اسلوونی
🆚
سوئیس
لومتزانه
🆚
اینتر
یووه استابیا
🆚
لاتزیو
برزیل
🆚
هند
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107733" target="_blank">📅 11:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107732">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68d8475315.mp4?token=uYQcE5JG_iITzzfrGGu0ZJi88P4vpn3mDEc3Dao2IPWh6q_MbaacSS-gjg7zvDZ5vuEDzEtA2Tgh8lv9OfqkvjH7AcEc-N0eSa-hw8Nx4H-wJi2KhAsgjmMWDX1y2_U6m0co6Od9_jf9ZCDstBo95tHEG2nnKCM2uCUY0Qbcjxob-SuLYqAEDuvYtRasZOiz9MxddljC3vdz5X3ZmNQ0HHGcPTcrK-JTogkFbbevCr9Fc2VfqWIjAoLAleL5bDqKmbQDD4TuS1yp7Iw_0bXljTUEGomVeA2VKnIhcTQumqGEe3M8qap4W9DBG6w-DidhhKiVfGs2InmGDHZVmjX8Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68d8475315.mp4?token=uYQcE5JG_iITzzfrGGu0ZJi88P4vpn3mDEc3Dao2IPWh6q_MbaacSS-gjg7zvDZ5vuEDzEtA2Tgh8lv9OfqkvjH7AcEc-N0eSa-hw8Nx4H-wJi2KhAsgjmMWDX1y2_U6m0co6Od9_jf9ZCDstBo95tHEG2nnKCM2uCUY0Qbcjxob-SuLYqAEDuvYtRasZOiz9MxddljC3vdz5X3ZmNQ0HHGcPTcrK-JTogkFbbevCr9Fc2VfqWIjAoLAleL5bDqKmbQDD4TuS1yp7Iw_0bXljTUEGomVeA2VKnIhcTQumqGEe3M8qap4W9DBG6w-DidhhKiVfGs2InmGDHZVmjX8Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
⚠️
دو قاب از بيژن‌مرتضوی به فاصله ۴ سال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107732" target="_blank">📅 11:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107731">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fbb258d04.mp4?token=oB3Bv6Wnx8FOQ5x1wAj9GNxcbVY8duNjG-ZqGULbAmF4PmkKzzs9M0mxEE6sJ-8qEU4rbx0WTfsSqxJAO81EVUOsJzk_MXKLfJpU8H0BctUwlzb-AjZR_CtjrhHJRJJRF53Qu2AXKbDyZIlUNdGdreGd7hZlxrlP85hP7McMPLz97WpODZ-kWjxuIM6wOFGyFK8ATZWjWpwi4GES-49WtYKtGqcDBk96dvBmqfOaLPzk1b1IZfcl6Ou8qIWyeyNRMTDNkN1qbMRtKnxZQYqNadrbYWw62ctJGkaftcZJB7BzK0KcK-06DaC6mm_1xDD2GV_VGYEFRXv8N8hvg8Xn8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fbb258d04.mp4?token=oB3Bv6Wnx8FOQ5x1wAj9GNxcbVY8duNjG-ZqGULbAmF4PmkKzzs9M0mxEE6sJ-8qEU4rbx0WTfsSqxJAO81EVUOsJzk_MXKLfJpU8H0BctUwlzb-AjZR_CtjrhHJRJJRF53Qu2AXKbDyZIlUNdGdreGd7hZlxrlP85hP7McMPLz97WpODZ-kWjxuIM6wOFGyFK8ATZWjWpwi4GES-49WtYKtGqcDBk96dvBmqfOaLPzk1b1IZfcl6Ou8qIWyeyNRMTDNkN1qbMRtKnxZQYqNadrbYWw62ctJGkaftcZJB7BzK0KcK-06DaC6mm_1xDD2GV_VGYEFRXv8N8hvg8Xn8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚪️
نه به تیم‌ملی چیز جدید اضافه کردن و نه تونستن جام خاصی به ارمغان بیارن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107731" target="_blank">📅 11:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107730">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8086af61bd.mp4?token=V5M6b7E7V-12Wos2WBUjzZbkgHJiuNbssWfdYhqCcfKP-AdZMK-vhWhmMZQblZocKY-jqz7GszdZiMDK0lG3THXZf2qkp9_bEpPbbowdgQW2d-UV3e33GHwYUmLXSqyMYMjToqa-5CXFn8zAOZunjKnK0EPQf9p6sqJvDfNquGajRLBA5pl3lkre3FkhBzaVLZ0f0qA44ph8xo-xVox8NSOL-M21rsfITDDxWnAmOeVCbW607NqIekZM9S0iumrQY5kF4JSBLOswQB70iEbYywCK829d4NZnzsxmIyyErofJfCH07FK05qZF3F9JG_sgbWwbAx4EuVPYyyQRHdwd3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8086af61bd.mp4?token=V5M6b7E7V-12Wos2WBUjzZbkgHJiuNbssWfdYhqCcfKP-AdZMK-vhWhmMZQblZocKY-jqz7GszdZiMDK0lG3THXZf2qkp9_bEpPbbowdgQW2d-UV3e33GHwYUmLXSqyMYMjToqa-5CXFn8zAOZunjKnK0EPQf9p6sqJvDfNquGajRLBA5pl3lkre3FkhBzaVLZ0f0qA44ph8xo-xVox8NSOL-M21rsfITDDxWnAmOeVCbW607NqIekZM9S0iumrQY5kF4JSBLOswQB70iEbYywCK829d4NZnzsxmIyyErofJfCH07FK05qZF3F9JG_sgbWwbAx4EuVPYyyQRHdwd3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
▶️
تلخ‌ترین صحبت‌های مالک موبو نیوز در گفتگو با امیرحسین قیاسی...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107730" target="_blank">📅 10:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107729">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdae91c6ba.mp4?token=uDdpxzdTXcazmZGkHMqiAmoRNUtY2aMz_lIZ1YAudIgpK5xra3-GrZfgLi9ZIgbCKVCc2XR8ZJlAvJtB84ch9BOzYwn3JNTudg3fvKL28SWg7hOOTuv5T8ID0EhcEWyB-leZ4te4qNDkCE_FMGKIQ1muImIeTFag04xGXP8tnYihn1785Ns3HLfBnYkm_-TFWsVOBcfmbCG5paM2TRtWmMxLjYnojJZyEh4YoeNtQGZc_3JDrPkDgKv6tqq4iXGd2WMOmeQBT4qL9vbDiCTHu4_PDOjTjjxVyhKwnZ1vzrH0B-Zrl2ctTlqA4UL3_VL0mmCFDiu3GbJes8MW_1VL3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdae91c6ba.mp4?token=uDdpxzdTXcazmZGkHMqiAmoRNUtY2aMz_lIZ1YAudIgpK5xra3-GrZfgLi9ZIgbCKVCc2XR8ZJlAvJtB84ch9BOzYwn3JNTudg3fvKL28SWg7hOOTuv5T8ID0EhcEWyB-leZ4te4qNDkCE_FMGKIQ1muImIeTFag04xGXP8tnYihn1785Ns3HLfBnYkm_-TFWsVOBcfmbCG5paM2TRtWmMxLjYnojJZyEh4YoeNtQGZc_3JDrPkDgKv6tqq4iXGd2WMOmeQBT4qL9vbDiCTHu4_PDOjTjjxVyhKwnZ1vzrH0B-Zrl2ctTlqA4UL3_VL0mmCFDiu3GbJes8MW_1VL3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
یه راه خوب برای کنترل هزینه‌های اینترنت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107729" target="_blank">📅 10:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107728">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c37b6c6ac.mp4?token=MWjERDyw-tg7WEaQ8ylhRboQKa5FCxxTzIAYtRIlFqh4qY0LxOtOmXNaNix7IuIRMJxCPsjZTmVZjiUbZTxGQ1lDe8TbCFfjLiGKG7FV3th2_LvXN2aXUiqCTcugqgTWP7hHzS7Aa48TEBPlcwuctozmOhvOJ7F7lHxCikCkdXqWlw6ujwDORDA9qbZOOg09wqILrR0fOZJ5UIzPnQGM14XX-qiH1ILi0WjJIfCTmnyr2YqGktkYwaPBM-K8LpFwOEnc_mYhMCFYHLpR8Hp9G_dEny5HvPr8xOHK1wpRmGZFjLdTkBDQDNSX66GzdmseghlPsHRkNgqmTQeRg_qfnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c37b6c6ac.mp4?token=MWjERDyw-tg7WEaQ8ylhRboQKa5FCxxTzIAYtRIlFqh4qY0LxOtOmXNaNix7IuIRMJxCPsjZTmVZjiUbZTxGQ1lDe8TbCFfjLiGKG7FV3th2_LvXN2aXUiqCTcugqgTWP7hHzS7Aa48TEBPlcwuctozmOhvOJ7F7lHxCikCkdXqWlw6ujwDORDA9qbZOOg09wqILrR0fOZJ5UIzPnQGM14XX-qiH1ILi0WjJIfCTmnyr2YqGktkYwaPBM-K8LpFwOEnc_mYhMCFYHLpR8Hp9G_dEny5HvPr8xOHK1wpRmGZFjLdTkBDQDNSX66GzdmseghlPsHRkNgqmTQeRg_qfnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
بیخیالی بازیکن های پرتغال از رفتن رونالدو دقیقا یاد این سکانس تاریخی میندازه !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107728" target="_blank">📅 09:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107727">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faRpQW3HdK9MluR3RdoCnHHPJWAzWO83a49qZlL2hU5CZiQkN3xtpRcF5jBNgZ8SHnSHTmiC0CM6_MCY3hSKvqfr7z4wyxZ762vdv5Z4xU8YOw2YSyIgjAPz4jSIS8I5tTW5Wva6a-la-RNMPVZaidmsLoeZhzzDRahxgJidm31KIOOAa1O7CHqOXDbpEy0mmGKq0y4nEDs5vfdyS1rzQvdaXB-5QB-vrqGIKSFFO9OZPzWQlrMKSr7LzIiRrXCvxUSkci9L76RdCSBGWfL-Dv8DdWZxSsJAEPalQ9Rn3_VlL2JvRWryCc_kPxgOXyt0OU24OKQ6WYjMFZKJgOZgDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇶🇦
با اعلام‌رومانو: ریاض‌محرز با عقد قراردادی به الشمال قطر، رقیب استقلال و تراکتور در لیگ‌نخبگان آسیا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107727" target="_blank">📅 09:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107726">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b5c7684c2.mp4?token=X_OKzcp4JD9HRtRDSfxlmDRgsBPub-reCxStULcNXLTOE5BqBeJT8oFzTWb6PzAw8KKc_caLR9n9fRVfLdqPYjw5tv-mbq-1-x3zkRANnABLSVM-MPU7-NKGaDbbTzhVBC4BtrJQ2ukl8bQe-R-ynMf1JWHfYqngVNs5YJENmqgcu2RyGuwQT1ZbS4HQrcGcUJLSWFpRULcDt8D742BrWGfjovsYuNr9VcoXD8GddYhvDVVNdEY-7PF8qb0OJDdnrTG0KceHHCxo740kAYHjLwBcCTZjZeau0sWIpS5Y0V5PnNs3A266XRWZbfxJlpkRalKPf_CAyrihXzyvo-jPjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b5c7684c2.mp4?token=X_OKzcp4JD9HRtRDSfxlmDRgsBPub-reCxStULcNXLTOE5BqBeJT8oFzTWb6PzAw8KKc_caLR9n9fRVfLdqPYjw5tv-mbq-1-x3zkRANnABLSVM-MPU7-NKGaDbbTzhVBC4BtrJQ2ukl8bQe-R-ynMf1JWHfYqngVNs5YJENmqgcu2RyGuwQT1ZbS4HQrcGcUJLSWFpRULcDt8D742BrWGfjovsYuNr9VcoXD8GddYhvDVVNdEY-7PF8qb0OJDdnrTG0KceHHCxo740kAYHjLwBcCTZjZeau0sWIpS5Y0V5PnNs3A266XRWZbfxJlpkRalKPf_CAyrihXzyvo-jPjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚪️
سقوط تیم‌ملی به روایت اصغر مازیار!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107726" target="_blank">📅 09:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107725">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d02e44cc.mp4?token=XyPoY8Y7j-gacsKBZlnHdGFggMjHTxMftZ7RwuEf0ZQtg1IP2yIfx9IHnNcWtik_AnSw4_q0KzQ-9F9DD0XoMkG_DagndQRgk1dIBW_d9pT8_I0x6eusg2BucakihVo2HXatFCkqrvRYjaq_IPZ663D85PaZkdtomLUbMOoZIHUIKBxcbEZpognOE0qhoeik2A1Hg7-i_PNlub4ZY7U6iuV-9Zcy4VYLjazROeWOnTtm6NslXK3kPSNjfAVDZveu9rFczYIrpXV9Nuie-Pg0FY6yqb3h9QepZcJNe4pwjaAabP_7A4xCv0qb7qzPHXSpFTnDQbFzmHBfYMqhopos1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d02e44cc.mp4?token=XyPoY8Y7j-gacsKBZlnHdGFggMjHTxMftZ7RwuEf0ZQtg1IP2yIfx9IHnNcWtik_AnSw4_q0KzQ-9F9DD0XoMkG_DagndQRgk1dIBW_d9pT8_I0x6eusg2BucakihVo2HXatFCkqrvRYjaq_IPZ663D85PaZkdtomLUbMOoZIHUIKBxcbEZpognOE0qhoeik2A1Hg7-i_PNlub4ZY7U6iuV-9Zcy4VYLjazROeWOnTtm6NslXK3kPSNjfAVDZveu9rFczYIrpXV9Nuie-Pg0FY6yqb3h9QepZcJNe4pwjaAabP_7A4xCv0qb7qzPHXSpFTnDQbFzmHBfYMqhopos1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وای این چه سمی بوددددد
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107725" target="_blank">📅 08:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107721">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107721" target="_blank">📅 00:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107720">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGelMiLKyW_3vvrZsaOSCusuK9NymL0e_5z1tiIxHhHVvp3onKYPIzLtu-p0NEQEjl7WnyB4NlAVcmiT1DAmsSuv2I-HAT2a8fiYnZm773HTRvhQFh6_OtMzF87mJyyB5Bi0pqSVQKUskjE-VA86KnuJBltCFL6ygIJGhA96SoEiG_2vIOjE7tIhcpv5YdOiS-MwnmZeRl6XP81gxTgK2CrPdMEIZ9dm9BvbZ7TbRlfU9zo0zRVmnPAiRop5x-thQwCu-3q_gdTR2zMHSN0oiUWBGvglS0REY_eax7lsqExOPCppMv8_tROAe-cLWVPKyV9RKWR3imY7LiaKNEKwTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
بنر هواداران عربستانی برای بازی مقابل قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107720" target="_blank">📅 00:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107719">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇮🇹
🇫🇷
هایلایت بازی فرانسه یک - یک ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107719" target="_blank">📅 00:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107718">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
❌
🇮🇷
علوی، سخنگوی فدراسیون فوتبال: استقلال قهرمان فصل گذشته نشده و بحث جدیدی درمورد اهدای جام به این تیم نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107718" target="_blank">📅 00:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107717">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b540d3428e.mp4?token=MXFcNUoq4mymNyc_tb_QY5DHAGLIu3IGwqxDd_VloGJy6BlJRjM5hjSH7DwVvXAcISMMi0qeGgAtwwukdkcnBjWR7-47Iw7Cd_GlLcCHZN8dzeGWC_zSJs80QmeQD_3sREGox6jP3pAobDCRrxkrd7mTBl9aWHvYZ4BHBfesY7dMsqVPO8uEepXSiNuHKKgpx_6LxJZ2oFfCrNK6fa7GjT96TBGqoaHQv2QBVhOGO10a0hx8Cx9TGHeApa4EQlH-3HumkedE7aYCTGksrv9_7r6BZGzagTBTVWiOtvKFFVzbrnbixioIs5nw0GZSJoTPNLcwPH0mT7EZ1c7_SyhwKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b540d3428e.mp4?token=MXFcNUoq4mymNyc_tb_QY5DHAGLIu3IGwqxDd_VloGJy6BlJRjM5hjSH7DwVvXAcISMMi0qeGgAtwwukdkcnBjWR7-47Iw7Cd_GlLcCHZN8dzeGWC_zSJs80QmeQD_3sREGox6jP3pAobDCRrxkrd7mTBl9aWHvYZ4BHBfesY7dMsqVPO8uEepXSiNuHKKgpx_6LxJZ2oFfCrNK6fa7GjT96TBGqoaHQv2QBVhOGO10a0hx8Cx9TGHeApa4EQlH-3HumkedE7aYCTGksrv9_7r6BZGzagTBTVWiOtvKFFVzbrnbixioIs5nw0GZSJoTPNLcwPH0mT7EZ1c7_SyhwKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇧🇪
گل‌سوم بلژیک به ترکیه توسط لوکاکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107717" target="_blank">📅 23:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107716">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5cfe007c4.mp4?token=FK8CfQ1mRLLI7XEnxnT9r9IGpVraqG8XnqlO7Pc23qHJqgNoqNym9PADQEY3o7HxbE1pExKwmu7gSRuwDLYHH4Tr0CiDa83aF-PBQZQBnyHhDL9fVPpTzFE1TTJrvZa1X-8aIxJAp4p4oRVtUKjCe3t87CaCrYx9FLIn97YU7LRC7ay5G8_pP-TlofC1J-cW6BirdSqRujQ-2h_mAiQxhM-wOaDTicIJFZJfsM0AAjBisbXmsGbOUjyshxfv4Mk3Q2uk_coW2-Z9beEc0-G3XUT_uepdL89CUUQ2bmrN2TxkG6FMgTDgAh4Y1DU9j2DQeFksArpE5afhxobUTIF_fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5cfe007c4.mp4?token=FK8CfQ1mRLLI7XEnxnT9r9IGpVraqG8XnqlO7Pc23qHJqgNoqNym9PADQEY3o7HxbE1pExKwmu7gSRuwDLYHH4Tr0CiDa83aF-PBQZQBnyHhDL9fVPpTzFE1TTJrvZa1X-8aIxJAp4p4oRVtUKjCe3t87CaCrYx9FLIn97YU7LRC7ay5G8_pP-TlofC1J-cW6BirdSqRujQ-2h_mAiQxhM-wOaDTicIJFZJfsM0AAjBisbXmsGbOUjyshxfv4Mk3Q2uk_coW2-Z9beEc0-G3XUT_uepdL89CUUQ2bmrN2TxkG6FMgTDgAh4Y1DU9j2DQeFksArpE5afhxobUTIF_fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇹
گل‌اول ایتالیا به فرانسه توسط باستونی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107716" target="_blank">📅 23:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107715">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f73a4fb35.mp4?token=E9ujpFyazFG3VJzJoJThrI2Q5fA6NPk3RskH3coUi1ezCuu7AHXmSiegs3hBe5zkWdohd398HBr9PNb5VtuJxEjG9s4j7zQGgnnV8uAzQKk9evSEfeNo5tVyDTKgmuGfCwc-Jx0oUEJKGcU2p8LeLvBN9oqiPv81Z8FhCVPz47esCQswETcbGEdUHa7PtANsAPgaF-aIRhUzF1GT30aOk2fj-VxxvzaqFE83z-k0IeQSbFKuuEOycknY4jC9RFSSzPEAjU1ormIT3629sLLjfbD4mEfF2xfQCHSoAELSckaxSW3Xuf8MuRDGXkr5nICT2blvQrsVDq96DV7GFC7udQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f73a4fb35.mp4?token=E9ujpFyazFG3VJzJoJThrI2Q5fA6NPk3RskH3coUi1ezCuu7AHXmSiegs3hBe5zkWdohd398HBr9PNb5VtuJxEjG9s4j7zQGgnnV8uAzQKk9evSEfeNo5tVyDTKgmuGfCwc-Jx0oUEJKGcU2p8LeLvBN9oqiPv81Z8FhCVPz47esCQswETcbGEdUHa7PtANsAPgaF-aIRhUzF1GT30aOk2fj-VxxvzaqFE83z-k0IeQSbFKuuEOycknY4jC9RFSSzPEAjU1ormIT3629sLLjfbD4mEfF2xfQCHSoAELSckaxSW3Xuf8MuRDGXkr5nICT2blvQrsVDq96DV7GFC7udQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
✔️
گل‌تماشایی کوین دیبروینه مقابل ترکیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107715" target="_blank">📅 23:44 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107714">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گلگلگلگلگلگلگ دوم بلژیک به ترکیهههههه دیبروینهههه</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107714" target="_blank">📅 23:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107713">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3dc430d99.mp4?token=TEKCAq9GH_AesNxCXdsIASwmmv5DfTfdSNtnuwq99lKBpi95TLgpYrpYQ-tEI-l-8Nm7xG2QvgxSRyggw23Ev_h4VjGHdRzN--XzF3K830N-YSmQKt7fPt9A5hEehIRxt7UWpoqedHCOld8munDfv-vXTffwQ4Kg4CzP3vEEDnXh_cVbsQZzeMt8b8jxCLRcUKyjpfjViYfFzYcU1p6fNQqwJ8fiAWgamy974SQY46xnpZjuPeUOHEl9NFJb0gIlx102USbUdmDHNYTPTzzbBRfBswoolQv_mmzxXPL4By-lGKj7U9cUSVxsSKRch7ex8gRTtOWntIPDTi6b1CiEqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3dc430d99.mp4?token=TEKCAq9GH_AesNxCXdsIASwmmv5DfTfdSNtnuwq99lKBpi95TLgpYrpYQ-tEI-l-8Nm7xG2QvgxSRyggw23Ev_h4VjGHdRzN--XzF3K830N-YSmQKt7fPt9A5hEehIRxt7UWpoqedHCOld8munDfv-vXTffwQ4Kg4CzP3vEEDnXh_cVbsQZzeMt8b8jxCLRcUKyjpfjViYfFzYcU1p6fNQqwJ8fiAWgamy974SQY46xnpZjuPeUOHEl9NFJb0gIlx102USbUdmDHNYTPTzzbBRfBswoolQv_mmzxXPL4By-lGKj7U9cUSVxsSKRch7ex8gRTtOWntIPDTi6b1CiEqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🤯
سوپرگل دیدنی اولیسه مقابل ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107713" target="_blank">📅 23:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107712">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سوپرگل اولیسهههههههههه</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107712" target="_blank">📅 23:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107711">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">فرانسهههههه زددددددد</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107711" target="_blank">📅 23:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107710">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گلگلگلگگلگلگلگلگل</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107710" target="_blank">📅 23:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107709">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e970c7c18a.mp4?token=R6YedRvBcqSSLo5TeYxj8WrUYSmKZBf7832vHeiHmzqBPsxeMl6sXFGyeezcCfPxFelgUoTeus3ek2J-gNgfU3Ufccr9dVfbaITxUp_D2YUUG7_uFFn839cReqtq0TssYkLFdniCF5HthBJ-AxbeZhQe3hlUOlec5K7_Dx0izmNzSmPki6Ar23SQAjAjvphd24N7-RYANyq8el2fFi9R1ZMOaDa3mbn2VWDNBo9lSfA3yQR3l-p1lfWuOPaQcC6SMYmMmsJJA830nRsGFGqY9pNpY8OzKBQAMNBRRCI3ZsS35-XI7BCl-DhM7My30LrWnrhfqh_TpoVcucI0UtVUTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e970c7c18a.mp4?token=R6YedRvBcqSSLo5TeYxj8WrUYSmKZBf7832vHeiHmzqBPsxeMl6sXFGyeezcCfPxFelgUoTeus3ek2J-gNgfU3Ufccr9dVfbaITxUp_D2YUUG7_uFFn839cReqtq0TssYkLFdniCF5HthBJ-AxbeZhQe3hlUOlec5K7_Dx0izmNzSmPki6Ar23SQAjAjvphd24N7-RYANyq8el2fFi9R1ZMOaDa3mbn2VWDNBo9lSfA3yQR3l-p1lfWuOPaQcC6SMYmMmsJJA830nRsGFGqY9pNpY8OzKBQAMNBRRCI3ZsS35-XI7BCl-DhM7My30LrWnrhfqh_TpoVcucI0UtVUTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
استقبال بی نظیر و خوش آمدگویی هواداران به زین الدین زیدان سرمربی جدید فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107709" target="_blank">📅 22:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107708">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0312a011f.mp4?token=DTFJapExweuMOy9p0lil7dcaDH6Y4d-yebKRdZnJRWZjXX4zbb4TMFec7ZgX11071eSmPlp8YtBOlCVG35oweHgIfD_RwcPM0apGTptXcyoFqT3l6Jh5xJpoX6RsfKE1ep1m5qPNLzWuHixH5KYKOItmlD4CERL05QaIuxILlzsdfg8svasczD0trgBQahGqJP7JZsjso0hzXfxnTpqEJnWIsDjv81feO2wsr7gsNNt7fX3BjMaDxYnVNayy6nCdc2brBzNoN6HKDwBOFaFaphmPJLQymJdq18HAaYosdmHnrq9WJz_KboEc2yiMTqRk-FX_TZpUptERVPqUaJgfUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0312a011f.mp4?token=DTFJapExweuMOy9p0lil7dcaDH6Y4d-yebKRdZnJRWZjXX4zbb4TMFec7ZgX11071eSmPlp8YtBOlCVG35oweHgIfD_RwcPM0apGTptXcyoFqT3l6Jh5xJpoX6RsfKE1ep1m5qPNLzWuHixH5KYKOItmlD4CERL05QaIuxILlzsdfg8svasczD0trgBQahGqJP7JZsjso0hzXfxnTpqEJnWIsDjv81feO2wsr7gsNNt7fX3BjMaDxYnVNayy6nCdc2brBzNoN6HKDwBOFaFaphmPJLQymJdq18HAaYosdmHnrq9WJz_KboEc2yiMTqRk-FX_TZpUptERVPqUaJgfUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل‌اول بلژیک به ترکیه توسط کوین دیبروینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107708" target="_blank">📅 22:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107707">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f5c780577.mp4?token=U7K3N7V8y-E4ncniQ9E1-AHyU9cm_DHzNjmg22AVmSkknb5ujykkK_w5Lr72y-GZwe6pbc36RjLMxjEHnNfMKX8iHgxgbok-c5QlF0mLTYx23Ne1QJRzTyrwGdjcgwYtem-fJ4VbH2MWC47PLqB1eTkUZOzmJp55vtzjYkZnEPxkv8WHaMf6Wi2m6t2Lon8uM4sTbTOfdkPeWfKyXzFirVJZoaVddiIsSgla7JX-Nik9M9XFgRhcV6ZXWMxVID4NYiRx6RY6DLC490tiyYfC-mZdKI45do78vXYbm3Zr1D138WOgK71JRE2xggMqysoZBPpW8plBd-Odihw_g-PBxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f5c780577.mp4?token=U7K3N7V8y-E4ncniQ9E1-AHyU9cm_DHzNjmg22AVmSkknb5ujykkK_w5Lr72y-GZwe6pbc36RjLMxjEHnNfMKX8iHgxgbok-c5QlF0mLTYx23Ne1QJRzTyrwGdjcgwYtem-fJ4VbH2MWC47PLqB1eTkUZOzmJp55vtzjYkZnEPxkv8WHaMf6Wi2m6t2Lon8uM4sTbTOfdkPeWfKyXzFirVJZoaVddiIsSgla7JX-Nik9M9XFgRhcV6ZXWMxVID4NYiRx6RY6DLC490tiyYfC-mZdKI45do78vXYbm3Zr1D138WOgK71JRE2xggMqysoZBPpW8plBd-Odihw_g-PBxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
علوی، سخنگوی فدراسیون فوتبال: استقلال قهرمان فصل گذشته نشده و بحث جدیدی درمورد اهدای جام به این تیم نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107707" target="_blank">📅 22:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107706">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3539953949.mp4?token=Y_lU39BOCiKYRpNcYatZiGOzbgq6TIT9qejYxW2_-mIf4QMw3f3DQgz1goX7col8gjR90T1a-MZlmYh8Kwej6z-8fKpgxt2UcNOAHIa60jzhT89CpQ3AfCavZ5ZjJD7JvCF0eECD3VnJcKhezyhURSmw21lPAtJ8FJeISaUSs_tX0WRYI1XYfGSQgtSKHllYlxExOfrTqrBPNMHg1Pem5BmIg_mrgUVIu2cf4dgKKQPkd0jnJMU_S0gJgulJKOQfJyoBGOA6uH9kYGCmu9qajiHu4VsQfTEFl4rPESy1Rfb693JacL6gdvL9aR1LDhlN1ltRvbxhFTjbKK-vOMNSKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3539953949.mp4?token=Y_lU39BOCiKYRpNcYatZiGOzbgq6TIT9qejYxW2_-mIf4QMw3f3DQgz1goX7col8gjR90T1a-MZlmYh8Kwej6z-8fKpgxt2UcNOAHIa60jzhT89CpQ3AfCavZ5ZjJD7JvCF0eECD3VnJcKhezyhURSmw21lPAtJ8FJeISaUSs_tX0WRYI1XYfGSQgtSKHllYlxExOfrTqrBPNMHg1Pem5BmIg_mrgUVIu2cf4dgKKQPkd0jnJMU_S0gJgulJKOQfJyoBGOA6uH9kYGCmu9qajiHu4VsQfTEFl4rPESy1Rfb693JacL6gdvL9aR1LDhlN1ltRvbxhFTjbKK-vOMNSKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حاج صفی: می گویند آقای قلعه نویی با یک نفر(جواد نکونام) مشکل دارد که من را به تیم ملی دعوت کند تا رکورد آن فرد را بزنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107706" target="_blank">📅 21:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107705">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZ5wQup9Rr9ilOH5tUEQaQS9RwOanV4v00Inor6MqOelge6bdXbXYem0rIDwPtcbCeoZuMzsbnuW7t2HolLOMsi5wVkRlT_eXSVhI9-n0X3vqzUAiUKHTmjcGTZcR6MOPYDWe9ckVQAuLz67CeRm7UgxbIGoKh-eHNehB2i64FVsPvjIPHlV5rlUgPAfGTgDCQ_dGIlRUcglLQOigg6VWQSkW5wLcv_jPycc2UT6nm-5fGgnU8SwBd2h9g4G6w5dIbeG-IlLJDgBPoIhNZOiccZJCuo6A8mDouRLfD4bcxXdVJAnHJshl5qX2lng4qDls0kp8vsl0vBVbxAtOY4Now.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب تیم‌ملی فرانسه مقابل ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107705" target="_blank">📅 21:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107704">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmswOL7ROena0z5jYObXqebCXv7BHqKRkFd_caOTJeDvhvykb0YfQDLo-csw0bRZ8T8Is_SW-k03v3t5e0K6ObabPXBqhfBXGihtaGaZcsOEvRyJG7npJYSg8n8gAKDiUkor1Ze-KoxjoLcQ8jA5LYEYlAp8zajCuR48TX5iYUy1JoDwEK6IDhJr_n9BVv5zrLV3-9VvkIIYfj0eIuDyc4DMQFnzD7D9-RtpxQ5FyTEGQGdbzZrVZx6KceN_aPFR5h_GhbYh0mN0HMoVKIbBqmsj4WgK-jeP3jhicurE14ZtG9R3qkuGNaU5Xm7mxgFm9JSjVIkty5cx16633J1qbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
پیش‌بینی‌های زلاتان از برخی نتایج فصل:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیگ برتر انگلیس؟ منچستر سیتی.
🇪🇸
🇪🇸
لیگ اسپانیا؟ بارسلونا.
🇪🇺
🇪🇸
لیگ قهرمانان اروپا؟ بارسلونا.
🏆
توپ طلایی؟ لامین یامال.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107704" target="_blank">📅 20:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107703">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKECXDqWbaZZsudvGM5_9jJXPI__D24VVV0ntBHxOGIsu4lujjQT_uh1y3tcC9-OY8sz9bPi65dju_JWsPOINl2LsBm2sVD47V5Xk7Z0wYYPOjWJCx2P9RnK1W5SSZ6FtJHbVMH4BNAI_hR8hkkhh_6YbVzDgfsCPa0SyboFRde_WAvy2Hf1p1byBDjm8CHbAVQMXmS3CAisuLaCKWthd2XBZwjDg7b9GZacNuQj9aT2-116FKLoryaiOYZe4mrNhdWMm86-9WoA7lfBV7rG6eAK_wjOdIF9lMQnP2CkoHgwysSBMGrQQ0t1TzyR_eyCztYvH5VIdzsyk3UP7ACjGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب تیم‌ملی فرانسه مقابل ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107703" target="_blank">📅 20:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107702">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtX4vzX4tE3squnihabAnA2-Y3n6NimtSEQOMmhozyOTLQbWgdy2P55M38Q2P41-xvcEcmv1anerPAmCYaiPvhk1HlpdhJsJP_br4xIzI9Rz5wj1mum6P0oa8Sbqdb3uG5Pa4lamxPa4rxkFguxt3lZZn_l7UJTZgkMgZuHmHDHzWmzYSJxeNRTSo5kQWJw6LlSh0iQt-nBEArW46-7TeXEW7rEoWxnygD0-lZw2SxAsm0daONxQRSJJI_WVOOgtNWc6u2WKWXL8IRHSR0DXnZnoucdLOkcT8RFPZsetdoXw8Rm8FlaTi3DgJG6sJgjJ4wOg2i1Mgbbo3J2zxxLWug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📱
نشریه The Athletic
در فصل 2017/18، گواردیولا اولین عنوان قهرمانی لیگ را با منچسترسیتی به دست آورد.
منچسترسیتی حدود 100 میلیون پوند قوانین مالی (PSR) را نقض کرده است.
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107702" target="_blank">📅 20:24 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107701">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af474384fb.mp4?token=FFJIf-CDBtkIMRHGG2F_kINoL4b2AVxFvjfPaTJIUOVkRSHudqi-at8LSFuefpnw-FG8sczl_LArz_m7cbqtQsRHoRy9MItik3mo556NaRQavwbUtFcm9NC0VR8ini9wSM1KldbapycZX9BaoJhZ65yo9qvmq5bP3c7gDp6nTCTQlUBEEij_wSb2PsoWXLsbL5rJdhgEWVJZ4K4N0NZnAbyGYexC2q0IrpTQ6TxgHSon0bxUhaLZyOV0za62S21kuCk4kirpge2KNgKhSB5LCGeDgq-S44ZZPv1SurPZn6CEgoQV5gSMIyWocPwjuOXvYfCucVzEj_TYEwdXCKDTdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af474384fb.mp4?token=FFJIf-CDBtkIMRHGG2F_kINoL4b2AVxFvjfPaTJIUOVkRSHudqi-at8LSFuefpnw-FG8sczl_LArz_m7cbqtQsRHoRy9MItik3mo556NaRQavwbUtFcm9NC0VR8ini9wSM1KldbapycZX9BaoJhZ65yo9qvmq5bP3c7gDp6nTCTQlUBEEij_wSb2PsoWXLsbL5rJdhgEWVJZ4K4N0NZnAbyGYexC2q0IrpTQ6TxgHSon0bxUhaLZyOV0za62S21kuCk4kirpge2KNgKhSB5LCGeDgq-S44ZZPv1SurPZn6CEgoQV5gSMIyWocPwjuOXvYfCucVzEj_TYEwdXCKDTdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚠️
رضا علیپور، نایب‌قهرمان سنگ‌نوردی بازی‌های آسیایی ۲۰۲۶ ناگویا، با انتشار ویدیویی در اینستاگرام، به پخش نشدن مسابقاتش از صدا و سیما اعتراض کرد: «همه مسابقات را صدا و سیما نشان می‌دهد؛ سکو، فینال، چه برده، چه بازنده، اما به ما که می‌رسد،‌ نشان نمی‌دهد. قضاوت با خودتان.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107701" target="_blank">📅 20:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107700">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad5607ff2b.mp4?token=rZZfdavDltfoRJyluuB8TpCjsbspr1gpv4JEIribpWsLLBkcqn7NnP0V07Bscg4DT8qUQn2GCKByH3Lh5XKtmPhGls6lfnDJK2yM7SbsMlcyptSFYW2v3L2CEGT6LFQM0VlRDM5Sbo4SpiM3bDMqSkrM7dTTdaQy_R1lKPSil3sp01W5_29YK0C5K9Lq8Xb2cu5pTMrOA4mQiIdNEiMHHjN1rKhX6zWeldFVtQXSwRdMJ8jFc4ecNnRC3Xk8eiz-610rPCXQR3SrMPi9kxA0DCnKyZJ4Qx1OeAX8ymZwHC-6L7uskruSvT7jAR13I5CjmQeis_npBFwsKdMJANJCLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad5607ff2b.mp4?token=rZZfdavDltfoRJyluuB8TpCjsbspr1gpv4JEIribpWsLLBkcqn7NnP0V07Bscg4DT8qUQn2GCKByH3Lh5XKtmPhGls6lfnDJK2yM7SbsMlcyptSFYW2v3L2CEGT6LFQM0VlRDM5Sbo4SpiM3bDMqSkrM7dTTdaQy_R1lKPSil3sp01W5_29YK0C5K9Lq8Xb2cu5pTMrOA4mQiIdNEiMHHjN1rKhX6zWeldFVtQXSwRdMJ8jFc4ecNnRC3Xk8eiz-610rPCXQR3SrMPi9kxA0DCnKyZJ4Qx1OeAX8ymZwHC-6L7uskruSvT7jAR13I5CjmQeis_npBFwsKdMJANJCLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
حاج‌صفی: در کار آقای قلعه‌نویی و کادر فنی تیم ملی اصلا دخالتی نمی کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107700" target="_blank">📅 20:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107699">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f60d798d01.mp4?token=CNmKy5QVjZZjubZT6o2qXBglc3CN_4v0fp3mPbycnYRM32-7QtTLe67q93LTXpYXQ99UW8oXEEhtlQSOlRlg96GUQSZIhhTTkgWe_RvQxvxPQaxXaO2I3VIRGqalNr13btZrBbgNCi6PQ7p_L2X2EtWE4kYBO1xAopHYZN-mn7Ih0H-32JLdlD2fjHuZP8QA4qOdQHBz9q1TWdZtApj8PghYOGPO1EEIO1JzR11uMN-tJ1yp6zE_v87aOeUv_Dudq8FGsq3gTDE8Nwqlf5LciEJSzjXyqOta3mY-ij2uu7VtnCrzStYh3hxxZMfjUjUlaDNXVgyuuXHwOhLeBzeO_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f60d798d01.mp4?token=CNmKy5QVjZZjubZT6o2qXBglc3CN_4v0fp3mPbycnYRM32-7QtTLe67q93LTXpYXQ99UW8oXEEhtlQSOlRlg96GUQSZIhhTTkgWe_RvQxvxPQaxXaO2I3VIRGqalNr13btZrBbgNCi6PQ7p_L2X2EtWE4kYBO1xAopHYZN-mn7Ih0H-32JLdlD2fjHuZP8QA4qOdQHBz9q1TWdZtApj8PghYOGPO1EEIO1JzR11uMN-tJ1yp6zE_v87aOeUv_Dudq8FGsq3gTDE8Nwqlf5LciEJSzjXyqOta3mY-ij2uu7VtnCrzStYh3hxxZMfjUjUlaDNXVgyuuXHwOhLeBzeO_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
درآمد ۲۰۰ میلیاردی مهدی شجاری مالک موبو نیوز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107699" target="_blank">📅 20:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107698">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8956163759.mp4?token=eiyRPR3qdeLG5AO8VUR_lHIc30CDHqcuKVJDsWK94Z3kSHWEntSlfDCTkEMxfj5Ask1_hlqjbFV4VPQa9cyLmElfpIAxLfNIS0P0tHAMWja1P1nEWIH9M-D5hTA-RcW8RXqW1Ap8zd2_u--I8gbRaXI2cenS7OCvxs2AmKOZHj6xWF84rE_GuDHHZND-KzEH_It9eMrqHoFxNRyVEvoF6G4Rl5bX1S3Svjcy0v6LrpQc8AvScGAVbwl0gM8LmBhPFEhHH-1wcCf0hHvRmQQOYk9Ryt7HB_Ogr05mJX_N_GhT3BBUZ0DxN-tbr86ljdosTy8Uag-z8eP1R27Giw6-Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8956163759.mp4?token=eiyRPR3qdeLG5AO8VUR_lHIc30CDHqcuKVJDsWK94Z3kSHWEntSlfDCTkEMxfj5Ask1_hlqjbFV4VPQa9cyLmElfpIAxLfNIS0P0tHAMWja1P1nEWIH9M-D5hTA-RcW8RXqW1Ap8zd2_u--I8gbRaXI2cenS7OCvxs2AmKOZHj6xWF84rE_GuDHHZND-KzEH_It9eMrqHoFxNRyVEvoF6G4Rl5bX1S3Svjcy0v6LrpQc8AvScGAVbwl0gM8LmBhPFEhHH-1wcCf0hHvRmQQOYk9Ryt7HB_Ogr05mJX_N_GhT3BBUZ0DxN-tbr86ljdosTy8Uag-z8eP1R27Giw6-Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤡
کیف کوک ژسوس بعد جدایی رونالدو از پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107698" target="_blank">📅 19:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107697">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/263935f09a.mp4?token=MTQdQYz-V2tC6w1xLP7B2m_l65XBNUS4_vrTLxu6sqP9AHIdvNSxGAyKBEmdy9KAUUJVWkfRq5RY0cEF1gQKxxf_VG1wSd7N5iB__-r9LfXxvNF2ahQRJiMs36r_1RZ5z9iE-G0IlGmFzuI_MfouWv-LQQkAb9z1_FDzbiCOqgV0UjnjYNxvRGfLGnsAdavZfsK23FznxxA4C2kv9KKEdxfMn54v_8DnbkrCHoL4fQ4bSwKbsbERjrPAzheAiveTmSKRm0hS7uRv-8T851Am3Wfonnr2omzCiQHcMHDHJybBnz_H4YbBfvXdmeZBamgohgtZ1yUB3vKSeMf5ZiKqLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/263935f09a.mp4?token=MTQdQYz-V2tC6w1xLP7B2m_l65XBNUS4_vrTLxu6sqP9AHIdvNSxGAyKBEmdy9KAUUJVWkfRq5RY0cEF1gQKxxf_VG1wSd7N5iB__-r9LfXxvNF2ahQRJiMs36r_1RZ5z9iE-G0IlGmFzuI_MfouWv-LQQkAb9z1_FDzbiCOqgV0UjnjYNxvRGfLGnsAdavZfsK23FznxxA4C2kv9KKEdxfMn54v_8DnbkrCHoL4fQ4bSwKbsbERjrPAzheAiveTmSKRm0hS7uRv-8T851Am3Wfonnr2omzCiQHcMHDHJybBnz_H4YbBfvXdmeZBamgohgtZ1yUB3vKSeMf5ZiKqLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
انتقادات از صحبت‌های عجیب احسان حدادی رئیس فدراسیون دوومیدانی جمهوری اسلامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107697" target="_blank">📅 19:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107696">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a8b7a5dd.mp4?token=HWtlqEytjXfbCW6B-zbBdB4xiJgzwk4XwY-MakZywz7H3gAn9uJ1FX4phNVpryt8MbolMC7Mo1IjQ8wjeH04uSMW35p-wCdOk8qMp5BIGXjubAq596O_eegMfKD_gObXiWfBtmk383wqKcEU5RgmKu4GgUbXoT9uyMDRMEayZ4Li9rDObh98SEZrJqI-hU5Hb65U3GuylnfCQ2vSC7KA6XzflBapXVvWrQ3KjyHsTlmfmSU_lX23xyO95yZ-NEBeJre7FDWbdjN5-cG3xWAvGMeRofR5CaziXEbICjK_YjzjbSOOJviHTazNxbfAd5HRqH2P1G5K_TmIN3rLa0NDSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a8b7a5dd.mp4?token=HWtlqEytjXfbCW6B-zbBdB4xiJgzwk4XwY-MakZywz7H3gAn9uJ1FX4phNVpryt8MbolMC7Mo1IjQ8wjeH04uSMW35p-wCdOk8qMp5BIGXjubAq596O_eegMfKD_gObXiWfBtmk383wqKcEU5RgmKu4GgUbXoT9uyMDRMEayZ4Li9rDObh98SEZrJqI-hU5Hb65U3GuylnfCQ2vSC7KA6XzflBapXVvWrQ3KjyHsTlmfmSU_lX23xyO95yZ-NEBeJre7FDWbdjN5-cG3xWAvGMeRofR5CaziXEbICjK_YjzjbSOOJviHTazNxbfAd5HRqH2P1G5K_TmIN3rLa0NDSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
✅
کیفیت تصویربرداری با آیفون 18 و یک سوپر دوربین فوق‌العاده از سونی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107696" target="_blank">📅 18:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107695">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYumBVQSBCbROqaL4qVg1b8iDIvw4D0vVb63RGyREiSk6WgVencACXX_8sT6y_Pcvh3_vCRT2rkT9OED_D7iiZLk15izjc1N3adVcyCMpwxgd7AyEL8lBt1gyk2lKeer2YEry8S8i1dbcFsDCqakGHuyDI-utYS0XIuDr3PlnzhqBtNivgKxb0VUMgkSjPkm-yWAh5-uuVGG0Y6P33DiJZ30Y4HgNTqANnYriJ7f0kagtUA9WLCm09ieZHFpqV_KZx04cAl8gPWLM9c3emtsxpRKClHH11w01I8V_E0qVPSk07J0y0nEFvgED4CtIJtGTOzDndtJt7U5JFsUFLt7tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
✔️
پرسپولیس در دیدار تدارکاتی مقابل گل‌گهر سیرجان با گل‌های محبی و محمدحسین صادقی به برتری رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107695" target="_blank">📅 18:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107694">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VD5prXoXO8fY25RWGeSMF3a5F2xy_y4ZyEItL0ELEETmRJGD3I36sTlJLS8g0qkzEjs_U9ywzh_54h8RD4AJLIXeblmaWZSUrhdsCknazVpFVZWrnTUpJdok-vPCG3tlpWXsjFvjdbSdLaa0hseGxSUVzb4RO10_BSIYFip-zNoleny0m49LSGgjCrbeiTnH89F8PAQuyqGArmgyi6-KcljV5prk6AkFPt_81qkdq-0bukKKO_bx5zJnX3Rp3TKGVhIKy5byymduCRPZZ1RhZ-IL5xcqdiojFJEFqc4jiHhjoZMvbzxKDNUQycjk2kWHy3y9f6HwHRqTknjI8FZLRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
یوونتوس قصد دارد تابستان آینده به عنوان بازیکن آزاد با ویرجیل‌فن‌دایک قرارداد ببندد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107694" target="_blank">📅 17:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107693">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/507dbd5bf2.mp4?token=mDvLtfxLB_oiAj17bFmmWIjf4_912HJ2lWJdfwO75J0wDHMJuRKrqgtWP5aVLXDuqeGF3MhX3CEzDo3M09KwvroyB-5C6G5UdCovL5MMWo6PiQC96b-W7rNtb0oHsezYHCk8OlBxwc7jXKQPGd-2sOULsYjewM_OepAkJrbkmDiT2lZE9f-2V3FIUG4h0_q5I9z6qwAizC8g0uK_v5qjgd3nx0FUYw01bQsPBggYLihlKrqZrSg7HvSxcNFIUf0Xv1Lnk9HcsBrjgAqU5EiMDBOlZ016afM6u8p7L3XDbh40gWZSohG8nkhNb3Mv7AvafH6BRYaJYgbiYds9aFjklg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/507dbd5bf2.mp4?token=mDvLtfxLB_oiAj17bFmmWIjf4_912HJ2lWJdfwO75J0wDHMJuRKrqgtWP5aVLXDuqeGF3MhX3CEzDo3M09KwvroyB-5C6G5UdCovL5MMWo6PiQC96b-W7rNtb0oHsezYHCk8OlBxwc7jXKQPGd-2sOULsYjewM_OepAkJrbkmDiT2lZE9f-2V3FIUG4h0_q5I9z6qwAizC8g0uK_v5qjgd3nx0FUYw01bQsPBggYLihlKrqZrSg7HvSxcNFIUf0Xv1Lnk9HcsBrjgAqU5EiMDBOlZ016afM6u8p7L3XDbh40gWZSohG8nkhNb3Mv7AvafH6BRYaJYgbiYds9aFjklg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
امیرحسین صادقی: علی منصوریان بهم گفت چون شبیه نیکبختی، یا باید زن بگیری یا نمیذارم فوتبال بازی کنی! با حاج محمود سفت وایسادن تا زن بگیرم حتی شاهد عقدم بودن که خیالشون راحت شه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107693" target="_blank">📅 17:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107690">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa4517b308.mp4?token=lUdQm8hIEJ5l3JQA973BY49Fbp9ZrRY2-73_Lz_3ZfzemQBeyKpy3jIWBHH5plx8Do_PsfKYFg34T2q2q7yZQRN4h_WWp7YnQh5ewVIXl1uwzejbnApkx9YU4bnyvZJ_hlEhuzuk1WkaC6iZba2i4qtTdJYT2yaLOMuGubPs02KxBfQY4RSU9wqajxNa12xOUWIIVTf_2qUJSaNok7fOVNuqUGSLLlx_xiInVyhKR2tAMRy2GqKJ7QPnYFZrV29Z16LXm45ykvLi1vF4nTmkUD7SlZ-wWw2mM0K1bFI1gqh-1Hq9yqnzU0IIMfXAGIAe8xY1K8pNRrzGabBS5dfXcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa4517b308.mp4?token=lUdQm8hIEJ5l3JQA973BY49Fbp9ZrRY2-73_Lz_3ZfzemQBeyKpy3jIWBHH5plx8Do_PsfKYFg34T2q2q7yZQRN4h_WWp7YnQh5ewVIXl1uwzejbnApkx9YU4bnyvZJ_hlEhuzuk1WkaC6iZba2i4qtTdJYT2yaLOMuGubPs02KxBfQY4RSU9wqajxNa12xOUWIIVTf_2qUJSaNok7fOVNuqUGSLLlx_xiInVyhKR2tAMRy2GqKJ7QPnYFZrV29Z16LXm45ykvLi1vF4nTmkUD7SlZ-wWw2mM0K1bFI1gqh-1Hq9yqnzU0IIMfXAGIAe8xY1K8pNRrzGabBS5dfXcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
تعجب و عصبانیت قیاسی از قیمت دلار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107690" target="_blank">📅 17:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107689">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fac9f22f0e.mp4?token=Y2CZLhhDakhYxfLQBbr29XUQZj8MAOlFagUPDql1WNXurFm5pMjiedCb2jU90aYVo58KTSQaqLFxZWjtx8knRLM_bzUb20kzXY58oAFQ8Dcxy5tzEoVmn_qQp9vAZs05vFLlThHxyd05g0Eem8LsoMXZ4qcchJxLu8jJRmf1ECPWNyEQsC2nSlUuP68HAcmX-RaJBczBG5Ge9A6oSE7S2-adkem5jDblazADQ53SyRBUTtGbUeCgwpPEjg0uq875fbO5huwbXHw4xQVPJ9tLe7UYuih90yRZHKmrhxCDvkYiOkh2pa_oK-xdnSt7xsLnq57_qYgydcVB9BirgDFhkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fac9f22f0e.mp4?token=Y2CZLhhDakhYxfLQBbr29XUQZj8MAOlFagUPDql1WNXurFm5pMjiedCb2jU90aYVo58KTSQaqLFxZWjtx8knRLM_bzUb20kzXY58oAFQ8Dcxy5tzEoVmn_qQp9vAZs05vFLlThHxyd05g0Eem8LsoMXZ4qcchJxLu8jJRmf1ECPWNyEQsC2nSlUuP68HAcmX-RaJBczBG5Ge9A6oSE7S2-adkem5jDblazADQ53SyRBUTtGbUeCgwpPEjg0uq875fbO5huwbXHw4xQVPJ9tLe7UYuih90yRZHKmrhxCDvkYiOkh2pa_oK-xdnSt7xsLnq57_qYgydcVB9BirgDFhkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
امیرمحمد، خواننده آهنگ سنی نردن گوردوم رو بردن برنامه تلویزیونی ترکیه، اولش براش دست زدن و کلی تشویقش کردن،
ولی به آخرش که رسید دیگه نتونستن جلو خنده‌شون بگیرن و همه زدن زیر خنده :)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107689" target="_blank">📅 16:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107688">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c643f6bb4.mp4?token=YN_7ic8lxBxxvoD8qwG1wQpzipB3xqxGpzSOaSwkMY4CNGHB7luF6dC56h7Aj7SAA722-enKvdwMYZPyXoe6j97qeWeqExqPmHNAyzluIJpmY_CX-uTs_ALzhU4lyUzZHZ58aXY9rQZT6JZixC3bH25DUy2fH2tdsHSqqbxGR6BD7qOKyDqQXEk13lXunm8rZrExoIWokIx1_Yh0e3uCGO61uvBer0NP9ViklCFJGKBADYxadE0qVd_51VJGZ0dYBZzP-yzV7WCmsoLBx-1KkzJovaJMYoqpmXD6jkcTY_Og5HV7wM6xMlV6Rrii0BVkhXJv9xC_GT630117LE74rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c643f6bb4.mp4?token=YN_7ic8lxBxxvoD8qwG1wQpzipB3xqxGpzSOaSwkMY4CNGHB7luF6dC56h7Aj7SAA722-enKvdwMYZPyXoe6j97qeWeqExqPmHNAyzluIJpmY_CX-uTs_ALzhU4lyUzZHZ58aXY9rQZT6JZixC3bH25DUy2fH2tdsHSqqbxGR6BD7qOKyDqQXEk13lXunm8rZrExoIWokIx1_Yh0e3uCGO61uvBer0NP9ViklCFJGKBADYxadE0qVd_51VJGZ0dYBZzP-yzV7WCmsoLBx-1KkzJovaJMYoqpmXD6jkcTY_Og5HV7wM6xMlV6Rrii0BVkhXJv9xC_GT630117LE74rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
خوانندگی فرزند محمد شریعتمداری وزیر اسبق کار و صمت و مدیرعامل هلدینگ‌خلیج‌فارس مالک باشگاه استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107688" target="_blank">📅 16:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107687">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebc463f33d.mp4?token=cHJK3wS3VaxGhN_B0dolakDuYLIZ9xdYO8oYbQLG-kDPCVTH45x12C-mfTpTHZIT-eGZkj5ytsAucW-tZe7GAyZ6oVyouKfDz5dCREn2Uy9iuuJY0vDSdGEBVHO5PpJdZJrGdhqmvF1cKpy90vKfrp1HbNpIx5Wlkw3ECqKweDKzsk0-E_UdWVr57gzhxotI5mbg00gK1c2GLr5o1WapOIHMU8yiKPvo3s_BdA4UHVy3B1f0scGCnqUHiGA3iJ3YggSRMqLiP3T51HpBXG1fCd0py3RiopHirsImceiHhe7jQckshKh84cBf0ernNem4r64ra-V6aI9jtASpnH2aYAa6fr5pjXPrPl9VctpEbJXTo0gikq18XUtzigkUfSRhg2CTwL89W3tkiC7SIuhtnentK54GHKqRqDMgZIzmISEril1HqHwlmMYr1gLbKVjMgnEmmOUS_9nsmfYjWS1lynAo30Hw5o6YYlazMwk5gsI3fFgYXB1BUF_stffKjigJdOGJZIMktl-K09XhBLiheLwUOCZ4Ld7iwrwGJbr__oivVgYinUWh3jZMe_NRTPa9gf-4_0aaiZmspNx1pcKHGz10TOXCl45T9CexlCxxr7f1FUXcoZtMkno8_wY87klDaGBengBl1a-9E5axkmbJCXPGXCqWdIgq4bNr2BxVy3E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebc463f33d.mp4?token=cHJK3wS3VaxGhN_B0dolakDuYLIZ9xdYO8oYbQLG-kDPCVTH45x12C-mfTpTHZIT-eGZkj5ytsAucW-tZe7GAyZ6oVyouKfDz5dCREn2Uy9iuuJY0vDSdGEBVHO5PpJdZJrGdhqmvF1cKpy90vKfrp1HbNpIx5Wlkw3ECqKweDKzsk0-E_UdWVr57gzhxotI5mbg00gK1c2GLr5o1WapOIHMU8yiKPvo3s_BdA4UHVy3B1f0scGCnqUHiGA3iJ3YggSRMqLiP3T51HpBXG1fCd0py3RiopHirsImceiHhe7jQckshKh84cBf0ernNem4r64ra-V6aI9jtASpnH2aYAa6fr5pjXPrPl9VctpEbJXTo0gikq18XUtzigkUfSRhg2CTwL89W3tkiC7SIuhtnentK54GHKqRqDMgZIzmISEril1HqHwlmMYr1gLbKVjMgnEmmOUS_9nsmfYjWS1lynAo30Hw5o6YYlazMwk5gsI3fFgYXB1BUF_stffKjigJdOGJZIMktl-K09XhBLiheLwUOCZ4Ld7iwrwGJbr__oivVgYinUWh3jZMe_NRTPa9gf-4_0aaiZmspNx1pcKHGz10TOXCl45T9CexlCxxr7f1FUXcoZtMkno8_wY87klDaGBengBl1a-9E5axkmbJCXPGXCqWdIgq4bNr2BxVy3E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
یک‌دقیقه با اسطوره رونالدو در لباس پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107687" target="_blank">📅 16:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107686">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/098c9ea234.mp4?token=D6HmnfMsIeMlDY1PkrO6tWS9B1ifHNZCWxMREJZ9BXpKyPwChKVItpUp8E9e_9IjZLLcp6qz2cYmFiv2mH5hLkDbsVpzIL-NJyj_16n-YUJzqbcbnUgASt13g9aKNSssv6Cr-whLZRUn4YNxqHCmUPqhKMYzybPdxguBd0OVV9wwaWs0I4qh_tZPoBT5O1orHjd8AZsPBXwbjYmwVmPGLDfYoB7uUd_Y57_uHPMb90K_B7lKIGaeIPZDP_H8acrce_i9qF5Ti8ZAWdExG31YkkAtGLcVp5VvFEfyUjAadLNCoTHnWBdInQYiHwy-xS3ROIxeZRCtxaHppBisS_ymXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/098c9ea234.mp4?token=D6HmnfMsIeMlDY1PkrO6tWS9B1ifHNZCWxMREJZ9BXpKyPwChKVItpUp8E9e_9IjZLLcp6qz2cYmFiv2mH5hLkDbsVpzIL-NJyj_16n-YUJzqbcbnUgASt13g9aKNSssv6Cr-whLZRUn4YNxqHCmUPqhKMYzybPdxguBd0OVV9wwaWs0I4qh_tZPoBT5O1orHjd8AZsPBXwbjYmwVmPGLDfYoB7uUd_Y57_uHPMb90K_B7lKIGaeIPZDP_H8acrce_i9qF5Ti8ZAWdExG31YkkAtGLcVp5VvFEfyUjAadLNCoTHnWBdInQYiHwy-xS3ROIxeZRCtxaHppBisS_ymXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ابراهیم شکوری تا رحمان رضایی ...
‼️
در جواب ناکامی بگویید: یخورده سرما دارم
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107686" target="_blank">📅 15:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107685">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/086fe81733.mp4?token=aBJBRXRJxe4mITNUtPl_s_VKBJvvAaLrsY0skdtWZcHqeMFpaNn23iHdgzLTSvAESx_y_faCKb9-BqMYsEwyskXgooYiCs76a4VUZb31JnYI1lEYAcRv2ZfgTRR50s3eh43g_3sPeMGv6gnYn84Vb_bcTyY-ntu1JYw5PjcKt5jyz3T7ptFeZmmFzKxlHZ7UsDoadeubDyWjBcsjUaiKDbP6FThfgRZ8omsdfEVvCiRcrZgpMM8FIQCUW3c-lJD2FpmAan5qc6IlaTek15kiQfE6lKmZvFWi33cIXXvQ611TnxsOnXqtvbFuHKPyRwEH4Pjt_0dPJ0Sr2bBby0SUIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/086fe81733.mp4?token=aBJBRXRJxe4mITNUtPl_s_VKBJvvAaLrsY0skdtWZcHqeMFpaNn23iHdgzLTSvAESx_y_faCKb9-BqMYsEwyskXgooYiCs76a4VUZb31JnYI1lEYAcRv2ZfgTRR50s3eh43g_3sPeMGv6gnYn84Vb_bcTyY-ntu1JYw5PjcKt5jyz3T7ptFeZmmFzKxlHZ7UsDoadeubDyWjBcsjUaiKDbP6FThfgRZ8omsdfEVvCiRcrZgpMM8FIQCUW3c-lJD2FpmAan5qc6IlaTek15kiQfE6lKmZvFWi33cIXXvQ611TnxsOnXqtvbFuHKPyRwEH4Pjt_0dPJ0Sr2bBby0SUIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
‼️
رونالدو رفت و پرتغال تمام شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107685" target="_blank">📅 15:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107684">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QG3hZL4kLuKo73jW_GP8TmU3tcPk6G_eDr9NmJo1MT8SpUBXG9su3cUmh8z7_oiQlQ49p9UOBJ0MCmRwAIgaYZLtYT9zw3gVXBGrKPNeWvqE-GeUDQSa1VdNMV_NKFLWXFhhRBoyfMkpHOkCxHNsTANtp8gP2aADVETrK9IasIkc2lNHyIPtKo3OnuSvkxb94sdFYbUCAjhxKSN4bxVXmRjPi5rcJ_WVfyyV95C_RdnCW8a6iuN1VRkjVC5RNRD5PO11l2OD79PW2ArbTYOvAhFuCjd68IvzYeli9q3dO_oMs7sSbjdm-W3mVz99N32uGclRnKE0pM_9_Xd-H4YXsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✔️
🇪🇸
فابریزیو رومانو:
🔻
نتایج آزمایش‌های کادر پزشکی بارسلونا تایید می‌کند که مصدومیت عضلانی رافینیا که در اردوی تیم ملی برزیل دچار آن شد، جدی نیست. رافینیا از هفته آینده در دسترس خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107684" target="_blank">📅 15:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107683">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2fc633f5.mp4?token=Av2Vo9Y97_ksWnK42XAK_PYr4dP_zTp3FQUEEhg6UnRQnjTCi3IT8EsLDjcDCnpoH202DAXpe2PIo6W6x-DOAGvTh4VdK2umkxnQ9BMVNdHYYHPA29fJwxiWVo7EMBcHDkn6LcgjottRqzS-TBq7DfUcgpiX7xRppHEqAMAQeM5vQUU7XlEy_HGGOSRZHv4sBWcUmejFAOS0uzpGcV27F12FrtgyMZAwBkRKd3LMvq74uiX3xj8nwI9F7sDFcgiOxnqNyZQsZ5FI5DpK_6FhPAh28dfnX3-f64RSKNTfCP2vLv0JELervKBuSI1fEC_feKW5bjbkNyCpiUSuBcPQug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2fc633f5.mp4?token=Av2Vo9Y97_ksWnK42XAK_PYr4dP_zTp3FQUEEhg6UnRQnjTCi3IT8EsLDjcDCnpoH202DAXpe2PIo6W6x-DOAGvTh4VdK2umkxnQ9BMVNdHYYHPA29fJwxiWVo7EMBcHDkn6LcgjottRqzS-TBq7DfUcgpiX7xRppHEqAMAQeM5vQUU7XlEy_HGGOSRZHv4sBWcUmejFAOS0uzpGcV27F12FrtgyMZAwBkRKd3LMvq74uiX3xj8nwI9F7sDFcgiOxnqNyZQsZ5FI5DpK_6FhPAh28dfnX3-f64RSKNTfCP2vLv0JELervKBuSI1fEC_feKW5bjbkNyCpiUSuBcPQug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔝
🌟
رسانه‌ها با انتشار این تصاویر مدعی شدن که نیروهای خنثی‌سازی هسته‌ای آمریکا همراه با یگان 75 عملیات ویژه، شبیه‌سازی و تمریناتی برای تصرف و پاکسازی تاسیسات هسته‌ای زیرزمینی ایران انجام دادن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107683" target="_blank">📅 15:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107682">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0274908694.mp4?token=NcVLSx3b0w9MIl7M_B-FO726cqPk6zSTGw-Qp0UvR6kWDQkB8GmQZLRj6XrG6Bf7ubPVhmIKSZVOUw9V72VlAkPUsghzjcaXvpNEXMSR9LLXm90UyToAWiNbzOaD_BKWmR2x3TEYWvd5Qu5ezOvDz6FLc17EDzEqyCY1eCUCFmuKiVwoicHU0yYwJrPklzXxMlcN3rDV322QrMx7XCYITh76u3nKL6mbU7dEXb6ycoSUh20N7vwi3oCZ2ygjqg4Ht18NJP6e6cF-OR5eLx0VA3X8makfwKj0CghskesSXgyVA96NLOkk4H8TnYQM85gvh1QfGtIGhaAaM1kcssq4fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0274908694.mp4?token=NcVLSx3b0w9MIl7M_B-FO726cqPk6zSTGw-Qp0UvR6kWDQkB8GmQZLRj6XrG6Bf7ubPVhmIKSZVOUw9V72VlAkPUsghzjcaXvpNEXMSR9LLXm90UyToAWiNbzOaD_BKWmR2x3TEYWvd5Qu5ezOvDz6FLc17EDzEqyCY1eCUCFmuKiVwoicHU0yYwJrPklzXxMlcN3rDV322QrMx7XCYITh76u3nKL6mbU7dEXb6ycoSUh20N7vwi3oCZ2ygjqg4Ht18NJP6e6cF-OR5eLx0VA3X8makfwKj0CghskesSXgyVA96NLOkk4H8TnYQM85gvh1QfGtIGhaAaM1kcssq4fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
⚽️
پایانِ متفاوتِ دو اسطوره.
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107682" target="_blank">📅 14:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107681">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6703d31fc.mp4?token=I892iV1c1Bt0nmUqH_NYihFxbgYWZpcKMMs8XFNrkgyQ6vRu0QBiIGdIVJVdbZy6EQzC_Pmr1RBwSaxaN1husFO5lvATzJph-asCWDPqPycz6rwQgo_M9g2stsYyI-Nk5MNnV3s4uRlx3XMhOfnVVaPbKLgDKk1ujVDckxwZRO93lrUArcowFp8sjZP41nnB011GgreyRd5PyLIvZMK202Q9B6sXL6mHFLAcYfzx_go4WmkUPew245nuhlJ1gR-dg2y8yGuXder5ysiVKg7RDJzNi_B3ck76PzO3cB822Trgbx-uzX7NF8uH6ZtroQ0LZGs6ZSDgY3A31oxwgoJSvq-u0Ov-SgEC7hu2jtfNC3CyzCRaD3Ygu0heSuQFJtErh0QY9wE7cZ9hPkgAUpWOLy0greCcMi_e8jSiHiewFgXUQVYyJsIbtJshFgrKmbIji9V-9ib_5F2H3ypT3LFJwWD7P-Eq_VLEfdCdWO-riwFcjct2sJt6VzNso6tlp-mgutKYkb8EFfcdLdlYB1cQTrYVZP8mPcV6ydUFopFEO0xcCcKOJ5hBvtzWI2QPVr6SLYOwWiEvjJ9Zv8db9G8rKGUpyDjer_o8vZ4BDzVVpjni0iTa26hl1J-WS35s2V1pMvXEg9bWOO4PkupqTOA0N2oiYJGxExn5CcMmTlIl-Cc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6703d31fc.mp4?token=I892iV1c1Bt0nmUqH_NYihFxbgYWZpcKMMs8XFNrkgyQ6vRu0QBiIGdIVJVdbZy6EQzC_Pmr1RBwSaxaN1husFO5lvATzJph-asCWDPqPycz6rwQgo_M9g2stsYyI-Nk5MNnV3s4uRlx3XMhOfnVVaPbKLgDKk1ujVDckxwZRO93lrUArcowFp8sjZP41nnB011GgreyRd5PyLIvZMK202Q9B6sXL6mHFLAcYfzx_go4WmkUPew245nuhlJ1gR-dg2y8yGuXder5ysiVKg7RDJzNi_B3ck76PzO3cB822Trgbx-uzX7NF8uH6ZtroQ0LZGs6ZSDgY3A31oxwgoJSvq-u0Ov-SgEC7hu2jtfNC3CyzCRaD3Ygu0heSuQFJtErh0QY9wE7cZ9hPkgAUpWOLy0greCcMi_e8jSiHiewFgXUQVYyJsIbtJshFgrKmbIji9V-9ib_5F2H3ypT3LFJwWD7P-Eq_VLEfdCdWO-riwFcjct2sJt6VzNso6tlp-mgutKYkb8EFfcdLdlYB1cQTrYVZP8mPcV6ydUFopFEO0xcCcKOJ5hBvtzWI2QPVr6SLYOwWiEvjJ9Zv8db9G8rKGUpyDjer_o8vZ4BDzVVpjni0iTa26hl1J-WS35s2V1pMvXEg9bWOO4PkupqTOA0N2oiYJGxExn5CcMmTlIl-Cc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سکانس جدید از گزارشگر تکواندو براتون آوردم
😆
😆
😆
😆
😆
😆
کسب مدال طلا توسط ساغر مرادی در رشته تکواندو با شکست حریف ازبکستانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107681" target="_blank">📅 14:41 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107680">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/353ac7dbfb.mp4?token=utvD3Pc_1LzRFIU2m9L9f5qF47hAtkkVhWKIAW4-6ASOV5jje_6b_FPJJCbluNYIvfIAo6OETWl2po-6cc69B_7k1gxX3Q3zoLNt4K-EOGI7j74PZajJACF4rHiNgry_i-kKNmkoBlM5hcAB7RlzamWBQU2PKpLDV3MnfcTuqROpdOK44TDvzLclE16O5_k-RvOSCGhhFny99QI4BlcfaZFqZhGTeMMB_YcmD5LIvPsocWxI_2ZU0uvjcjLBFXm-X8dvZRfcbGeJqeTiJ3wW538EE_nMb5vt9oCdtNhSQ0LzoDOLfypSgRNnEoBCqXbcMm7N73oYE1Lll5N_gS3qyKZ2aVVZCxuo_x8B4nIZrvtjMz0aNneefL6wLxWn4Ny6PtqqSaHtuac5qi8Yd4IuKG25ihySbkijn8s6RuioO8akWZ_Ts9rgAedXy0Tef54LhL-BTT_ilURBOeULx-wbqZMuJ_vNqbUECOnKIyA1GR7QHmeuWfznMIY_8rTwMC0z5faeWaolixfpWKLXAUJq6mAkYOLMMp-WfLgs0YjKec-pRMYAxKkwZ_29rFfV5RVJxekv0FP9yPNxqcGa7IuBicShYdZ5Wj-6O4__5ySws7MHIJbmEFT95OusFsAqMUSBXaF7V12a5CeHVZJj9_rjGe0vCkPBOj_0jyrc0pHD5Cc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/353ac7dbfb.mp4?token=utvD3Pc_1LzRFIU2m9L9f5qF47hAtkkVhWKIAW4-6ASOV5jje_6b_FPJJCbluNYIvfIAo6OETWl2po-6cc69B_7k1gxX3Q3zoLNt4K-EOGI7j74PZajJACF4rHiNgry_i-kKNmkoBlM5hcAB7RlzamWBQU2PKpLDV3MnfcTuqROpdOK44TDvzLclE16O5_k-RvOSCGhhFny99QI4BlcfaZFqZhGTeMMB_YcmD5LIvPsocWxI_2ZU0uvjcjLBFXm-X8dvZRfcbGeJqeTiJ3wW538EE_nMb5vt9oCdtNhSQ0LzoDOLfypSgRNnEoBCqXbcMm7N73oYE1Lll5N_gS3qyKZ2aVVZCxuo_x8B4nIZrvtjMz0aNneefL6wLxWn4Ny6PtqqSaHtuac5qi8Yd4IuKG25ihySbkijn8s6RuioO8akWZ_Ts9rgAedXy0Tef54LhL-BTT_ilURBOeULx-wbqZMuJ_vNqbUECOnKIyA1GR7QHmeuWfznMIY_8rTwMC0z5faeWaolixfpWKLXAUJq6mAkYOLMMp-WfLgs0YjKec-pRMYAxKkwZ_29rFfV5RVJxekv0FP9yPNxqcGa7IuBicShYdZ5Wj-6O4__5ySws7MHIJbmEFT95OusFsAqMUSBXaF7V12a5CeHVZJj9_rjGe0vCkPBOj_0jyrc0pHD5Cc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥇
کسب مدال طلا توسط امیرحسین زارع با شکست حریف چینی در فینال بازی های آسیایی ناگویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107680" target="_blank">📅 14:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107679">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‼️
وضعیت عجیب عدم پاسخگویی اعضای تیم قلعه‌نویی درباره نتایج ضعیف اخیر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107679" target="_blank">📅 14:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107678">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmLYcT5ToXuTyy64vXtwUOL0xSALquu82fdUmKF53URSMK8_Y7BvGCqaKUcNmpco3Ap3zDvv7MNXDvRou4utZqeNkCQ878sVXr_5ZltaIhgnuGomulE2IfkbvVaexn4I5HU0o8j1Zo3T2XWkc8w7ChZQ0V8InOg12z7LZnNcvO8nNfD-m3DyShKblq05SOV4ApmelYPJctLcsLFPQwME-NaWeyknxoBZ7hfXMy_KrbOEBdHMpV6Mq05q4RjJGfkhxpKmAhaX251TVKVTBE_1wWhtt2wcpxC0ig7HY6uEubc8IdsUooqkJaQZLi--wI8evMJaanGNSBWW9qepCSZNSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
⁉️
مسی یا رونالدو؟
👀
🤩
توماس مولر:
"در طول ۱۰ سال اول دوران حرفه‌ای‌ام، همیشه کریستیانو رونالدو را انتخاب می‌کردم و همیشه در مقابل او شکست می‌خوردم. اما وقتی به کل تصویر نگاه می‌کنم، متوجه می‌شوم که لیونل مسی، بزرگترین فوتبالیست است."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107678" target="_blank">📅 14:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107677">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3d0d9fde.mp4?token=T5Ox6r9Hn_SiIgYZs88viXprseokIbcWSK09TXSQJstHiZVnWznbjGyhGGC0UZq7bDLW462-7GIFxPb-hWvsTlyWEVlBDfJH5-4978T6_rnLDXUmN1us5hkx2-xz3lENQotZ5nh5JwmtVCQ2GeuogxXFF3jl-8lxHRhuHPG09NlOky2dOq1HCCnuBTt1mc7s9gT6EztEdVO1FYybDNTqvwIGPU0zUQucGJGIgw0OxbwtADzq9r-941gxmS2eJInyDm884lH8XCKFd3A_qUuW2wxYHMJ-yazVpZFTW4Ef_x-7DdstZLLE0Xsa777fjSMV2YRwGa5ogcGQZq5blEiz1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3d0d9fde.mp4?token=T5Ox6r9Hn_SiIgYZs88viXprseokIbcWSK09TXSQJstHiZVnWznbjGyhGGC0UZq7bDLW462-7GIFxPb-hWvsTlyWEVlBDfJH5-4978T6_rnLDXUmN1us5hkx2-xz3lENQotZ5nh5JwmtVCQ2GeuogxXFF3jl-8lxHRhuHPG09NlOky2dOq1HCCnuBTt1mc7s9gT6EztEdVO1FYybDNTqvwIGPU0zUQucGJGIgw0OxbwtADzq9r-941gxmS2eJInyDm884lH8XCKFd3A_qUuW2wxYHMJ-yazVpZFTW4Ef_x-7DdstZLLE0Xsa777fjSMV2YRwGa5ogcGQZq5blEiz1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚽️
دیس سنگین ژوله به قلعه‌نویی بدلیل سوال عجیبش از خبرنگار ازبکستانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107677" target="_blank">📅 14:03 · 10 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/XP37CadWaq5oiZz5omsQZVNmPh49tGQ_gUTGJyJHSObyF8dsQCUhLa28nu6ofrmoa-j1Ak03PH6KqGtrNE_uQKcLKkIrRPoZQIDiuBh4PzmmKUw0QwyD0eS7p1mYOll3ON5MQaBEDJUBwceVEs5y1gGYuwPiJ4VDNBVoUJm3drIPskwGUfGn40ApK0jCC_eyp623kkNrhMncmqPYGvRD0jJRiJL05rfw5qDtzSspZinGfO5r5QF9Z_d2oheIehR-Aw5mGbxTPGu2Ksr4Y4pRqLeiqrK0xAlsuIKQqxe5EKu5rQNKhHscJI7TVJJ_sLBQVgAIW6qoOvdimnVqPIP6Fw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 178K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 19:19:40</div>
<hr>

<div class="tg-post" id="msg-22615">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gb3szWmW03vpmLsEk9QoDWQl_hBpeLSsv5dq6KxTbQEppTJpDGqVE0ty2kyUuEGE2ULHvng9xyu3F0sJCkCyADagOLWxYJvuYBJgyu8ry6lLN41UmnZ60UsHLTqoiouKx_3WBl-rouEwBS2NSeZPmFyLK20pBGi7zNtzcWPmCADFcwjsDpysn520L1_dNAvFW58ABRouEAC9ontYm9b-ZsuhxzcByZ7eoyfLCGfhKV7shGtSF3C2Org-p7ujOjAbXCJO4WnHZTrVLJiuzou3sNy6tr1FRbp_lCnlHKT_C0ZSgnhgFIE572F_vv5LHa82V3_zh0MQRw5wFtInnJ0aIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیدمهدی رحمتی سرمربی شمس آذر: من با باشگاه شمس آذر قرارداد دارم و همچنان روی حرفم هستم که فعلا در حد و قواره سرمربی استقلال نیستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22615" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22614">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d191ac7bce.mp4?token=iW7ZmP1TxK1EhYgeupdvCRHDAutlemLJzxQTfplvn-QgPtBJuQ7hOABVSgegTivBaEKgJ9usIk6nF9qkyMyTKCCU5R7Nm2-hlsKKlHnAygwqnW5V94l3Xe44nXfKnow1uyLOppQIki6fd3I6TXnE8x_nptZvoA1TV2-Qd04lD_s57Km_dE9QOCAhCrVP3Ab-rEVLsDWJKsPq0UsIjT9VfbD55aMvsZhOlRBB7kdkf0L3PvmGc_2lutHTETqnzuxZFw8IIbfatkd6gFMcm6J4_ZauqaxuySosPIEtN7O6xRo5RDi0Wl-h2KnKWTXhRppedJcL--WL75pWKiHXnXXDZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d191ac7bce.mp4?token=iW7ZmP1TxK1EhYgeupdvCRHDAutlemLJzxQTfplvn-QgPtBJuQ7hOABVSgegTivBaEKgJ9usIk6nF9qkyMyTKCCU5R7Nm2-hlsKKlHnAygwqnW5V94l3Xe44nXfKnow1uyLOppQIki6fd3I6TXnE8x_nptZvoA1TV2-Qd04lD_s57Km_dE9QOCAhCrVP3Ab-rEVLsDWJKsPq0UsIjT9VfbD55aMvsZhOlRBB7kdkf0L3PvmGc_2lutHTETqnzuxZFw8IIbfatkd6gFMcm6J4_ZauqaxuySosPIEtN7O6xRo5RDi0Wl-h2KnKWTXhRppedJcL--WL75pWKiHXnXXDZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدئوباشگاه‌گلف‌یونایتدحاضر دردسته ۲ امارات برای رونمایی از«آندرس‌اینیستا»سرمربی جدید تیم؛ اسطوره اسپانیایی وارد دوران سرمربیگری شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22614" target="_blank">📅 18:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22613">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b369b688f8.mp4?token=kGMnwJpUB11tg9QCFu8U3JAdfp7nOOGiKL-4W5bMD9QzTPFW63eXF5qKzfBZ6MpV6pIjVNLCh2C0XTZEsxKpaucK_igD0LQgFDwlzBglENzdryO1KHNhWcG9-kcNwJiprsiXMWlFqtbk2HKKjXzzW09jtAXzyIho8bhi0xnqhRWNLqSU4vVNHqBXrUwCw6tN3bIjm6cc1Iqn-QQaZDltNVI3OKhZws3GGzgjAdPeEg0Je-IwxojacMN7utpewSeQejywDqRBCeC_QzD09wD67TOl1hKXZ2bamrdih1sz6N_7NJQX6RHMV4LyuKFTaYKuHKsniyqJ9UqZi7CrUizWpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b369b688f8.mp4?token=kGMnwJpUB11tg9QCFu8U3JAdfp7nOOGiKL-4W5bMD9QzTPFW63eXF5qKzfBZ6MpV6pIjVNLCh2C0XTZEsxKpaucK_igD0LQgFDwlzBglENzdryO1KHNhWcG9-kcNwJiprsiXMWlFqtbk2HKKjXzzW09jtAXzyIho8bhi0xnqhRWNLqSU4vVNHqBXrUwCw6tN3bIjm6cc1Iqn-QQaZDltNVI3OKhZws3GGzgjAdPeEg0Je-IwxojacMN7utpewSeQejywDqRBCeC_QzD09wD67TOl1hKXZ2bamrdih1sz6N_7NJQX6RHMV4LyuKFTaYKuHKsniyqJ9UqZi7CrUizWpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گزارشگر‌های‌عرب‌اصلا بابیننده‌های تلویزیون هیچ گونه رودروایسی‌ای ندارند و خیلی راحتند.
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/persiana_Soccer/22613" target="_blank">📅 18:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22612">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnV7e5B5XFyspuQTtklCbixb0WYriKHY4JdYU_WXAT7mmTTRDHuBxkHgcX4DZlaVc7FilECHkGWuVL4s5kbZTAJl5SXey9krNfpWFCiQo1nBLCjP0d71pFwSgNI9VlTYUUMd90VTvi6FEZ1k1pHgV-7K554NarLI-QUzrAPyD2flnLQ-FtoLMvdIu9OC20Aa9WVFxFRhcAbRV844q-lrwUVBgeVBfROhxA2LfelFtavCSmzbl-m_ZMzKYxKN-ZFd-NfoGl6vU_Orxl9fNy76TbFdo9Rw7TvO5a6OweWTE0ldoxZUWvjnVdY7bVNvkOlAz541bcRQhAblEWbcWWApJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت
؛ ویلیام پاچو مدافع‌پاریسن‌ژرمن این‌فصل در اروپا هر ۱۷ تامسابقه‌روکامل‌و بدون تعویض شدن بازی کرده که‌یک‌رکورد خارق‌العاده‌حساب میشه.
🤯
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/22612" target="_blank">📅 17:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22609">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f31679a7dc.mp4?token=GGWtfgeKy_e9Txo1nkPx6Lf8r_NpdQD5Aqqxf2CXx3yRBAEJJBUff9wmeB6MnitnZvXm8JdxWDQtXcNm0xzy0z99k-qm3B5njLnCI6y-PocywVTWZb9k01TqDTrizw257FCRFUbP-25E5Ndykr554KE0uxsY8OOArOU7wq1YH_tY-jr4uyU5_ESwrFjABii4R-IgYl80UYo8Nw4YPAw9NhfViWKxrNYMJhf87iCBGDbiej1FECiTswwWax2GXNg18pYUwJ2eQDf8xsRXAb4mEGUW0-pLvykY-Co-hh3QYfHhwQpwpGaoqeT2-BrkgthR68rZDbmGGqZdlKYRnTnCXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f31679a7dc.mp4?token=GGWtfgeKy_e9Txo1nkPx6Lf8r_NpdQD5Aqqxf2CXx3yRBAEJJBUff9wmeB6MnitnZvXm8JdxWDQtXcNm0xzy0z99k-qm3B5njLnCI6y-PocywVTWZb9k01TqDTrizw257FCRFUbP-25E5Ndykr554KE0uxsY8OOArOU7wq1YH_tY-jr4uyU5_ESwrFjABii4R-IgYl80UYo8Nw4YPAw9NhfViWKxrNYMJhf87iCBGDbiej1FECiTswwWax2GXNg18pYUwJ2eQDf8xsRXAb4mEGUW0-pLvykY-Co-hh3QYfHhwQpwpGaoqeT2-BrkgthR68rZDbmGGqZdlKYRnTnCXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/persiana_Soccer/22609" target="_blank">📅 17:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22608">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdKhnayBVbV9BhHLsSxSu8CgIUswVIjjNV1ZYePSUM03J_is7bxmvrovpDthau4wZpvTomcQr8r_TGtZ7y3FLYE75G1vMbNiFCULwJXn_-u68Tdy1jrlebnBkZNiQ6_fWFDbfw72dIVpPzhPNuJ7BNF3nQdOgVZYO4_TiOAwnTjGSObPpAHtPx1pRf8cVEBEQwqwEDJfG4JgoXNivkWEhVNhQwqJZDxA582tKCog2JC_jchwKAZ6Xa-kQKNGvoLrF0uaGgWZcFdcJ2eZoIdh6KhAaGmHCZxHz6Nhfy5PHH14mWT13T1zSFogiqsTme0kIrj2p4l2xkKQYuZpnYLx0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/persiana_Soccer/22608" target="_blank">📅 16:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22607">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3dS7F4qOkhNOkAUn6kjzmffdvENRCFlcABC-mGemvufch9Ott_guiq3QSINCAZ0ikO8n71fqotpOVlDFmCdHbbb-lkK6c6lfpIntoJcRmLlwVqKHrBNz9QHZaY8SfLMJvU-GWYOCXh1W7l5zFTlbhtAZUB1ZJUS4Axh-sD0t-dI4Wz76OBK-ZTI5KKibTwA9teC43CksFYlLdWZlw3lMiQT732udUXq7GFNhcuL2PlScP7urgH7aRDWOTpOhOvwU1Y3F79HXYTB77hcobVuqkMvpIva7zVm7DefkmhTff9wBf1ogemmdFCbGq7qwlURt8TY35gMFk3NQe7YhGmWBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/22607" target="_blank">📅 16:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22606">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZIYiwl1LdrWw-prSk7sEh4hcri_IWwJfSOihW-O5XRc8JaMxsmx7Euqb264PPnyYBePCBTd6EwMNyYimzF0CNQaUvmyoe5kBhkwi4lEznknrDM6CI3Y7iOInkC-02MLtdW-VL3ysxJvKf356IGDoA4rdVoMASLEoczuCxz4cztKdci0-GZxQ3bhQdMG9M3HR5YUGM6hS-aTZBnIfh2Pi3Jd3N7QQBFQIFl-Wx3LbU8wYSe0tT0AagB7U9rSRBQBSdeeNTPiNfy13BN1DYifUIWYT9AZ_LfqqnIQqRztZQZR2d2wNApJi7cQwLGMwx6F1RjDHkGG8MzVSg9R3r1OqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/22606" target="_blank">📅 15:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22605">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onRJdPxzR-GKbdzHU3Hhcj_Iio6KbaWWRof-pZCM9Jt0YmgmU0lqDoet_xxd4wNB2IMtOCTaXZbX6k9n1fs0IHvhRhbKrsqPji47kybHRprddVQajdt86fxeAzzdklojJutUmuy5o2M2Kslmk52dUbVarrU89555tP8tBsQjqa0M1v-UlBTGZzGnFvSsOdsvJAoRJcFrwjVm9VQ8iclSrXq8guOkGgcnhectsu3UJiMltil5liiXQqfcR1VYgIFHFANGLz9h-OezHjG1vSG_AzlahElRYNFPQ7B8xI_SVTvI4l83udOZAVBzwwjwE4J-vH6JawKj2g-EfZegKXICJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مارکینیوش کاپیتانPSG با عبور از دنی‌آلوز حالا تبدیل به دومین بازیکن پرافتخار تاریخ فوتبال شده و‌ فقط لیونل‌مسی از این بازیکن جلوتر هست
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/22605" target="_blank">📅 15:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22604">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnH87hh3K0GGn7r81fTnGwVnu_YkpvH35j9hNpnH5N14hRiFxGtb620lx732kCpMKEn99iIBasBTS3HfmqLQUCFa-P9UWxTb4yljrUE221CpBTsvBlrV5HBe9LCeINPNFt4xLEutLaUSPIeHwrTZXJX2f44Zt60SKMfNRLpeePuHrdbKNjpJ_O8ChKWARM6wF0vglcmiRjaBNt64nx6Ci9-XvJo8IFboEJt_s7omjgUqK7yApttNGLKDfksg8sx6KYXXPq-2EfoNaKQ7zDkJDW-Kpe9kK3bMwV7I-byaSg650_eaqsEZZQIu8Ef5S33vWsFudWQAJ36xwoDemWm3YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
آنسو فاتی ستاره22ساله‌موناکو تاقبل‌از شروع هشتم؛ با 5 گل در صدر بهترین گلزنان لوشامپیونه قرار داره. فاتی در پایان فصل به بارسا برمیگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/22604" target="_blank">📅 15:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22603">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDBqFCWHqwdzaUMgYjZGnmzbh4H0KQdVwB-Nuc8ch8bR7YKtxaMbN-pyrolfvgW1ibugpjglDkUAwekeWCseY0Wdck3wut8UNoHV-gfxvLYL0XfRsdpddajLCiA_bzaclETGScLlML68PXGNZelDAiaJ8kI32aI7C-NOgau17JNlNeFtdU4jeRskCscjxzQTC6pKENyMhnToNDO6sI5bG0hCWcGHm4YwxDI-pjmkWriiPg7VU3AuOQoRUn-b7fTamzucCyD3ekQyYJOpAZf0x1MI0Fo1X3LyWIorS8p0pYoBqvvAq1ETHT_9XAzlYqasfLppUnON5dohvCwynqawqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
کوارتسخلیا: بازیکنان‌تیم‌آرسنال بویی از رقابت جوانمردانه نبرده بودن. اونا خیلی سعی کردن منو به بد ترین شکل مصدوم کنن هرچند تا حدودی موفق بودن ولی درس خیلی خوبی بهشون دادیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/22603" target="_blank">📅 14:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22602">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tI-I9ZNY3H-KzsXnUQbRiDOSxmEnuD8LIAbqD81aj0j3jwoDqtKjgUBK4PKpe_YguCyfpUFmZ1s07pUJJlKzw72BNAt70iEYJoXcK9s6eX8GalvJ9ZspUNypguNbqSqXRMSn6rlfIuT8KhyfCdR8XvkkmtuWxP03Lcz_4isWN2HFTx7eQu6OuhAZs2Q_sryTQ89OdZX3etYLdBUp8f5ijPKRdCx71tezMKfqNm6H8do111IHGiPPIaaeMipGMORosvASbysssVyLlhiSdSyX6zCicfcV3Kew49SW8iOW03LjodXodNzKfLN-zjkFXlvc5mFuTBJPuWqCpyPiP-Ld1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
هرکی‌بهتون گفت که چرا اینقدر به فوتبال علاقه داری؟ چیش به تومیرسه این ویدیو رو براش بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/22602" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22601">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdS4zP0frXKa1LQgpxdAD-8jFrCQyASV4FKyHV0Y1K8zl5GkvH8BF63SnZXbQtjAQvCtbTUyc3xx9bWXlAvSVhYft_-jVmbQqYZkkEVtOgOSleuCv9OV8YwFpXrabdTonVnCAlezGhafjZqBSk1uKi6FxIubG4lchv6RZmH3491CreVPornnxs2EAwuNLM6vg5Q2yOPnBG6z_Y_S3kert7PzjyYjYN3JZujWn2R40mkDIg4pdTm_ZuJY3DWaIUATyyWiEsMT_WQjJZ58SRoLs9KYCk20gi1wbR4mLd3PcP8xJJU4GGHv8eriw34E2E-ps2GsLbsMDzWIlOJPSMR1fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
کوارتسخلیا
: بازیکنان‌تیم‌آرسنال بویی از رقابت جوانمردانه نبرده بودن. اونا خیلی سعی کردن منو به بد ترین شکل مصدوم کنن هرچند تا حدودی موفق بودن ولی درس خیلی خوبی بهشون دادیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/22601" target="_blank">📅 13:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22600">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ff67e8c4.mp4?token=Vr_as737yAGvlV7_70qgL9dOdo1fhUR9XHbA2m9xPDrt7dCzL2ul-WBic17a4tFOgFl4DOPGnPaDPjXF61X9CECaUTqSPw0OWYnLy107BXH1n8K4XW-zZ5fw7Ed_m1NZwOZwFMKN4Vfx0ptDfr7SJBWK4XY6G6QZyHvFOlyv2Iax-lX8a-k2kOf-F4n8lE0mHKsHbldDgWj6twShm5ebbexuD7Z9DsIRw0cz3WC6hm8CRHqeG50OMkLs2YQpV6K4erBt0iljHX-Fj_MXawtA8TPzYUytbVu3m4IAqyZ2y0Yi03P7iB4wbKhb5BcHbkekUdJ5R6rqJ33UcD1hsuNBqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ff67e8c4.mp4?token=Vr_as737yAGvlV7_70qgL9dOdo1fhUR9XHbA2m9xPDrt7dCzL2ul-WBic17a4tFOgFl4DOPGnPaDPjXF61X9CECaUTqSPw0OWYnLy107BXH1n8K4XW-zZ5fw7Ed_m1NZwOZwFMKN4Vfx0ptDfr7SJBWK4XY6G6QZyHvFOlyv2Iax-lX8a-k2kOf-F4n8lE0mHKsHbldDgWj6twShm5ebbexuD7Z9DsIRw0cz3WC6hm8CRHqeG50OMkLs2YQpV6K4erBt0iljHX-Fj_MXawtA8TPzYUytbVu3m4IAqyZ2y0Yi03P7iB4wbKhb5BcHbkekUdJ5R6rqJ33UcD1hsuNBqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
اکسپوزیتو زید جدیدکیلیان‌امباپه ستاره تیم رئال درحال قر دادن در کنسرت روز گذشته بدبانی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/22600" target="_blank">📅 13:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22599">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ab989954.mp4?token=FSaFU6DwOva3n9mL6zMMDeA9jaanc6BvWOlzNiz9B2M0XErSi8-nM-GcztK1IZzU-uYfYZZ-gQioTAr13O2dEzMprf6zt0KbjGxmIaBh6slrD54GjHHRieyH7x15WkLmPdh-Q6Wr6_pCSvr9S2ZnE3-Gflly2QWsPiWCvXsPztyYeVd4Qj0XSMsGbsDu3Su6zSLmJ7OLCcHaOtNqF2ZAQkJOklklxXNJJp0TYmuhfhPE5HWSlg5l8HswzVNIK2KqX3Nb7laV7oGScp2WXfBqx5wz9aQnJJls74WO-q0Xkccyf5s7im8cLMo-S84xkbaw7wTzh2ZjSYDSMyXJtoi_UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ab989954.mp4?token=FSaFU6DwOva3n9mL6zMMDeA9jaanc6BvWOlzNiz9B2M0XErSi8-nM-GcztK1IZzU-uYfYZZ-gQioTAr13O2dEzMprf6zt0KbjGxmIaBh6slrD54GjHHRieyH7x15WkLmPdh-Q6Wr6_pCSvr9S2ZnE3-Gflly2QWsPiWCvXsPztyYeVd4Qj0XSMsGbsDu3Su6zSLmJ7OLCcHaOtNqF2ZAQkJOklklxXNJJp0TYmuhfhPE5HWSlg5l8HswzVNIK2KqX3Nb7laV7oGScp2WXfBqx5wz9aQnJJls74WO-q0Xkccyf5s7im8cLMo-S84xkbaw7wTzh2ZjSYDSMyXJtoi_UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
قشنگ ترین توضیح درخصوص بازی تخته و این زندگی؛ واقعا هم همینطوره. عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/22599" target="_blank">📅 13:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22598">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSOEfCsf-kQoER68Jnx5H0a3UzOCgtsODKyBJgWGBj0BvLpVjHA5QvZ5eX01IEVAWSe5Xgruru2fLiQFFuPSGEcWquIdy7GHr10iuu0MzWelPC0wEO7KzyEc1sZa3ltPZVczXQbRnMsg-mnIMFTpfbp61omP1f1HaU8xL8kCjmsfrLHFOK85cC4N2hhUwMASY2MIL9CvNumgo8NsebOWUhDLdz53h5ingCDB6p4fZ1O3QgYRKo0jtnOi6YL2uIqsXv_dpsl9bEJBUZ19LEaUbk9XWvfuK3fHyLFit1bU-sNfOWAlSoKHmDnF-fwmn6QSBT_o84QzYebWYjzJVRbfBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|گاتزتا:سران‌باشگاه منچستر یونایتد مذاکرات‌رسمی‌خود رابرای جذب رافائل لیائو ستاره پرتغالی‌آث‌میلان‌آغاز کرده‌اند و قصد دارند این بازیکن روبعداز جام جهانی 2026 به خدمت بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/22598" target="_blank">📅 12:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22597">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a3a620208.mp4?token=M-zzoCl35HRqU3ge_RG_RozybfnHWrRKHzn1pBJDC3IpBO0uW04MKGP3j9SflBlQTtc9FS8vIeT6KS7Mc9uOputhAo6AEbPETs6R12ydPDGERKACbpjQkLFr6GiM_zK2xuqf0ZjxUtjQnK4Sc0Hu8-hpVSYpVkLnznQNJpZEBwTkE9rYUcZyFAeX-SSPSpcpW-Ts19O7YYW1XxCVk-ZXSDUYGjn08vzu_qzONJk_W4xKiSt_rsdQo_747EZw-g_0cnBVm39wVP-7y6xA_KQxo6acbzn-ulzCoJMaBcLwOvZcDtDlAUeIlzGDdWZBaIxY8o7e_KXeOMKRZMSlKqMRIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a3a620208.mp4?token=M-zzoCl35HRqU3ge_RG_RozybfnHWrRKHzn1pBJDC3IpBO0uW04MKGP3j9SflBlQTtc9FS8vIeT6KS7Mc9uOputhAo6AEbPETs6R12ydPDGERKACbpjQkLFr6GiM_zK2xuqf0ZjxUtjQnK4Sc0Hu8-hpVSYpVkLnznQNJpZEBwTkE9rYUcZyFAeX-SSPSpcpW-Ts19O7YYW1XxCVk-ZXSDUYGjn08vzu_qzONJk_W4xKiSt_rsdQo_747EZw-g_0cnBVm39wVP-7y6xA_KQxo6acbzn-ulzCoJMaBcLwOvZcDtDlAUeIlzGDdWZBaIxY8o7e_KXeOMKRZMSlKqMRIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه وقتی‌میبینه که با خوب بازی کردن در جام‌جهانی و قهرمانی‌فرانسه به عثمان دمبله توی گرفتن دومین‌توپ‌طلا قطعی‌اش کمک میکنه
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/22597" target="_blank">📅 12:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22596">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SuevOqArDmPBRL47Irf8PkkLbtXcBwu0ppmOjHnlKWEJLAPkYiCZQZS-YxtM8LYlTsvHg9PzctCqY9oLmUSqPaRAy4TWel__uTlIABYZKpXJ9mWHQU8IjqcIGUZb3dDaUzrBZoeNDxHagskmJ3hVFOdf6ZZ_5Fl7myEUnjp87ig1X8IUq8FLil3fm08-jBIofoHZAsx1mjlEQWjRzYIw0QVW4zUDnxKi3tGMt314YvL5Cf4L2KXY3EwPNI_0-L_6ybtTlG58WQ32dnBR99fObRQ8TxSOEuaZDxuMfWRQ6P-lJaPfcPJL5ufeJAfNviAuguxb-BhwLtl5qH0cDCAgng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لحظه حک شدن نام باشگاه پاری‌ سن‌ ژرمن روی جام قهرمانی فصل 26-2025 لیگ قهرمانان اروپا؛ این دومین قهرمانی UCL در تاریخ PSG بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/22596" target="_blank">📅 12:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22595">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H66DFs371PTNbNuLz1h_P3bDqZEB3cZE2wwGpCrZ_3OCSqEUzrJMQlbutnCbPZWzxQ7cpxPOi9lzu2TGnkbT6g0TZrMcE8oatLaoIGjkls0Jk2xv1hWNzsFCI8OcU0KxFkQMbqe5ipb6vu-Hv5uKWNLFO5DNrekiF6TSokuVT3H7vAOPXQEB1Sr4gG9Ijsyl1vS8qkS-NGvCLBjQZm23tMDhSvlaBlPDymIqIp-K-yIvrTP_AgDzLWDysm5MJC3MZaUUIej2OwZ_Jk94qoKoPyX3vwKQRXqoqXBVmbwJKkLhg4RHFQOKs-4kBUSGmNnKis29nDdgJFfMa4B833my4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جرارد رومرو: یوشکو گواردیول مدافع سیتی نیز همچون خولیان آلوارز در خواست جدایی از منچستر سیتی کرده. فلیک عملا با تماس هاش داره راه انتقال ستاره‌های مدنظر خود به نیوکمپ رو هموار میکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/22595" target="_blank">📅 11:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22594">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3238aa793a.mp4?token=Ssb-6oMi6ZXpJfp0-7WaGMtxl6tSLgdmNpJfvpFG_JgKrn7D_Ag9yskEO93VNEaHnCck3lQ2Wk7TtGK7tanEn9JsHGRNbW06faxr0MACkMBRwL8Iu1t7AgQBYnLReyacVDiJVp87LLI7CaSEmAFVKnvOpHxVuHrGAwwDuhajoyj-8jVWUwiU6VQaB4YexgMdDKJASTb1Ko-t5mNQNyuvhQj57IrUc2aVFuxFDAOObd-RF4A9ediaixfMmuNwWUeyldqS74UduuhaPS_P8HCAH0rN1nClbz3SNbr27Ak9wnw5lVAfYXjlr3XrRq5EZ0nNFAW8His1Tl19yExhBzaksltw4CsyX4I46JCH-yv5AwZNDrskIAF4_534S_kPRgFE_u5m8C-aqKtICTxss6jbwgE24ySLYkxW39dnU5rsIdA6z4bJk1IMoBap_KmqQabYCRojh7Cry6FOEBM4wxMMAmfk6Wz7rmQ_EOnGIkOwnraFMHJ-HE_-T4YQL1mIHtz76mM9sWNciYztTPVlYh9vdB3NaBoF6vq5aEP0kdJoPGBuYhdthrIKlTWinaB2Sevut3rmryHvXxC7t1MedcR5KfYrgWBnrjAamcpn1qe2RA0th16kzxTROoyhifXZQgJMUE-AVizOkVzkgyWMs-B28gLv0n15dpPcRDzflZ0I-zk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3238aa793a.mp4?token=Ssb-6oMi6ZXpJfp0-7WaGMtxl6tSLgdmNpJfvpFG_JgKrn7D_Ag9yskEO93VNEaHnCck3lQ2Wk7TtGK7tanEn9JsHGRNbW06faxr0MACkMBRwL8Iu1t7AgQBYnLReyacVDiJVp87LLI7CaSEmAFVKnvOpHxVuHrGAwwDuhajoyj-8jVWUwiU6VQaB4YexgMdDKJASTb1Ko-t5mNQNyuvhQj57IrUc2aVFuxFDAOObd-RF4A9ediaixfMmuNwWUeyldqS74UduuhaPS_P8HCAH0rN1nClbz3SNbr27Ak9wnw5lVAfYXjlr3XrRq5EZ0nNFAW8His1Tl19yExhBzaksltw4CsyX4I46JCH-yv5AwZNDrskIAF4_534S_kPRgFE_u5m8C-aqKtICTxss6jbwgE24ySLYkxW39dnU5rsIdA6z4bJk1IMoBap_KmqQabYCRojh7Cry6FOEBM4wxMMAmfk6Wz7rmQ_EOnGIkOwnraFMHJ-HE_-T4YQL1mIHtz76mM9sWNciYztTPVlYh9vdB3NaBoF6vq5aEP0kdJoPGBuYhdthrIKlTWinaB2Sevut3rmryHvXxC7t1MedcR5KfYrgWBnrjAamcpn1qe2RA0th16kzxTROoyhifXZQgJMUE-AVizOkVzkgyWMs-B28gLv0n15dpPcRDzflZ0I-zk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
قشنگ ترین توضیح درخصوص بازی تخته و این زندگی؛ واقعا هم همینطوره. عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/22594" target="_blank">📅 11:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22593">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gW3MGIlTEZQKTaH8kb5b60x8wdckerAh5lIswEfOY3qzFc1dtBnzMOh6YDZG0UORT9Wzp0tYRXOfOZ72duWnA5eKS95HqlivBYyITpntWmaGZn-psj6LVncqGtuvdTFvLFJ6bgep2YJ4kUJYVZbAzmJY0L0yNgDzUJoswYhzZ5IS_O7WEY60Q1ALnVRnm_uG6KhtxtQZuxnYi9fjoENy4xTyxEMSnbA9K6ZDSB9pnImg8yAQ7qHPTxsveC9OZ3zhKTXq4QUdNZ2oy9XSb-8CwfY4siy2_Ss497qH1EDxmLWCsQJRSwFCobBQt8mv4P1qNFfRP-p4HgPt-Xl0jAmLOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردفوق‌العادهCR7: حضور در6امین جام جهانی؛ لیست پر ستاره تیم ملی پرتغال برای جام جهانی.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/22593" target="_blank">📅 11:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22592">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQJg94Mf16w8J8gFfetNDRBlM7N0gWKmSNHiHjScaEBJuySrpISmXQOZ1IWCp8A-FhLmRXZ42FZ2dWQ3QhhtuuL-IkbPrY7cqljgp8_jpPIpHMdoil13yICEIkdVtq6H12D1wjqkGgbyjlIaDBZIj_01aA3lbp2q1eL5lhwM78hY-HQFRgIxGtQ9kemr5YPOaeZD-MbfbSuzfQ4r_OB4cKKQfVEPNEjEsMX0r_4Nygo4yy0sfnNQ6O4ubQLOOpuSfVlzOIJ9DNmFdB0RSUlKw0sEK4YGJ1pO2oWIiwjQ-Ft5P-k4FityUlno8WPVA-2024uT-I7X0HDp71CfnckdrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌های حاضر در مرحله یک چهارم نهایی رقابت های جام حذفی؛ تراکتور تبریز نیز حدف شد!
✅
استقلال، فولاد، شمس آذر قزوین، ملوان انزلی، خیبر، پیکان، سایپا،گلگهر؛قرعه‌کشی‌این مرحله بزودی انجام میشه و بازی‌هااواخر اسفند برگزار خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/22592" target="_blank">📅 11:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22591">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjUbbmlF5AbRNz-6hyQAFwfaIg18-iv5vmrJN4Q1pPpvAbR60xpLhvQCEP4VqpM8PrmWRpuKALoI6WlHVLCSxl_zOYO0IBaQPMX7os4T4dl0d1q9anJQRqpWq1F-S-fuIhIDpnqdkCBfQpCkEYzwWd22GGfX9W7OrdaVjIQJfQZEiuBW0mx2Z9Aib8WtyoqjJ-ZmrW8n_MMuFb0Lh99I5ZqrxZdRVv0y6jHMuMbRXfB8GDfMFMtuqpqAelpWTxNaokOiVPRcWpmwKPxpI0sph3ZuYfUIW0aqLzlsSkrmbFFIY3t2kWh9Ri8gIKo7mV4-TFlyoY3II_HB4uLGauRd-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد صلاح فوق ستاره سابق لیورپول از طریق نماینده خود به عربستانی‌ها گفته هر باشگاهی به من دستمزد سالانه میده، قرارداد 3 ساله میبنده و تیمش روبرای قهرمانی میبنده من اوکیم که به آن‌ تیم بروم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/22591" target="_blank">📅 11:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22590">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeI_GIvRMLywwDHzx4KSbl4mMsLsGPgbK5nCv6GR_ZWAzM-hMV50s589DOul4waNkB4BXn_8GK1XhNP7-jqyaeUIiqzyrxdrtXGcLJJK_Oo1TcNO2YrSD_xcc_P6hCVzyYGZsqU_1p-bc7H99ESXfMGMa6u7l_9v9vsTjf2_mjbvbyRBbH1-uvPYsAyirf2I0MV6GhJv6VvOKqmu2ogRn4QzXiJ7gGTUFpjN89qbcD487d7Va3BdXLVwlMp3jPy5wF8gzQEBnCFeaU0r44tNKZ81QmqatUJ5bXa5C5Mq1zCaMBD1bKfW7qFwyI6UlAD6rBviFxKSU7WsErR4rb6lcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
شانستو
#رایگان
امتحان کن
⚠️
میدونستی توی
#وینرو
میتونی  رایگان شرط ببندی؟
👍
تنها کاری که باید بکنی اینه که عضو سایتش بشید و
🤩
🤩
🤩
هزارتومان جایزه بگیرید بدون نیاز به واریز
💖
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r11
📱
@winro_io</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/22590" target="_blank">📅 11:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22589">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxyyEioMtDohreMhThjEhSXIZ-2c7a7pmyb9ZJXrLFHPW3xkNaYBCFTBzBXAjnjDD2bSdKafyH-moNa4MyS_BL15pnoOGRGhYAfljeSUV2uus6SYDPK9yifx1BqoUtPWb61zJ5l2oW8UFBl908gBQvNpRMYjJDQMHlb_I05lI8pFE2aM_lmYKHdiyB8ArUreCtcF7i1ykpT5ISbMGlATRQET4tfWWsTTyZQYZoRY9bSW9iTRMX6Xgdd14RicJKernS8iAa-EGtc6MfhZFaPidFV4VR1D6htTzuljzwomzaBUEQF8050re7xZ4On_PO42VYQ3xZMIsvPVvEsXlDaKcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|رسانه‌ های معتبر فرانسوی خبر از احتمال مذاکرات‌باشگاه رئال مادرید با ژائو نوس ستاره پرتغالی تیم PSG در روزهای اینده میدهند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/22589" target="_blank">📅 10:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22588">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppH_dGXXT5vbkh5zDw1FoaAcVbOki-H3WwWAYPLz8yyISH7p4Ks45a2uEqioEw3tWbizO8x6xFLAS_L1YJgZWqwjG_wLGOq6xswFqaVteBk3e12YQtCBOdw2xcSHD_RS1P9mfNlr1YSsp3hmzhGvvyzD2wPRj_t4gE9gfPEV6KSfU29neWBJ7aw1IUl72b84o7gfhj5oVdFacr7K3zHQF2lpcfCOr9qAfxzbBg97sAPsGeRtrdba-4xk3jZuI2ZfKjk6NWoLCYw4wr3PVrf0298KpZb_X1d3y0sysjMKKCzJoZ7khG2BGrwPFcD8guALCA_bzWMNxI-Qrb21vM9yfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداحافظی فرعون مصر با هواداران لیورپول با چشمانی اشک‌ بار؛ محمد صلاح فوق ستاره مصری لیورپول بعد از انجام 442 بازی برای این‌تیم بالاخره از جمع لک لک‌ها جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/22588" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22587">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f927e35e14.mp4?token=GStwOGlJWuBsJnccdNFmN4ndVGbXLSTIQdm-mr1KqREkTXwY0e0SbyRh-Ir8B45EnU97sWMjZk-oT9E56LbqQBWi7_bROYFFJkLI14w0iSxgEBsVr_wWKYZ3UCT1jJZCk8AT340reRLdfSvzxkKzyCw4xqwTx2ARyHVY_GKokBgz46_xL5jaEi3CZ17jtyVKudpqPkqFdRkVBXJRsy-gxkCKTju0J6PsW73PbqqfLS3IG6Ru8jbZgLs8RA4SdHPikJy2C_0bsBYwkqWgbrYgyF5dvkGd_73UUF7-x61iXuoQoKrtwJ6q9A7il6vOOqDdxFG8aTruE4czkXO6E3z1Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f927e35e14.mp4?token=GStwOGlJWuBsJnccdNFmN4ndVGbXLSTIQdm-mr1KqREkTXwY0e0SbyRh-Ir8B45EnU97sWMjZk-oT9E56LbqQBWi7_bROYFFJkLI14w0iSxgEBsVr_wWKYZ3UCT1jJZCk8AT340reRLdfSvzxkKzyCw4xqwTx2ARyHVY_GKokBgz46_xL5jaEi3CZ17jtyVKudpqPkqFdRkVBXJRsy-gxkCKTju0J6PsW73PbqqfLS3IG6Ru8jbZgLs8RA4SdHPikJy2C_0bsBYwkqWgbrYgyF5dvkGd_73UUF7-x61iXuoQoKrtwJ6q9A7il6vOOqDdxFG8aTruE4czkXO6E3z1Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تو رژه قهرمانی آرسنال بیشتر از جام لیگ برتر به باسن هینکاپیه‌پرداختن؛بن‌وایت میکروفن‌گرفته دست داره اهنگ میخونه هینکااااپیه
🍑
تو نشونمون بده
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/22587" target="_blank">📅 09:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22585">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYs0vgL6iXnJAS4uoA96lkocX_wSIWx-SBST0rMV9ys0YArIsfYWyTEvVqb8HSc-TNZCqf2cgDt6n5PHYyRoruUJ7YICxs61DJTKiNA-oQ4MBa77o_awMCuKmqPCDjHDOUr-KH-TCXfjHVtjSUvYz5fBVPWopEGSI-DLL9ot5xS-t-leFIUsdUefrZsBKZjQx3RXpxqzl-RIF9xRUUGeIywBHPIAl1Ck_fwLD0a1_S1W8H4QGGPXGVDAzycOj2OuAyYcXDOJL-sowbpoHquAchUcK4sk0C7OllyndPYin3OhhRWIxkWtGXActRBtt7S9-hFUDsNT-yKGwJxC43sikg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار‌های دیروز؛ از برد قاطع مانشافت برابر فنلاند تا برتری آمریکایی‌ها مقابل سنگال  بازی شاگردای آنجلوتی مقابل پاناما هم تا پایان نیمه‌اول با نتیجه 2-1 به سود سلسائو در جریانه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/22585" target="_blank">📅 09:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22584">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9282b8e98b.mp4?token=rr1v9onKhKyl3GyUmeASouVQwnWu_2fo7TNOed52a4o55a3H3mUCsMVAJzVDKjas_qc07kqec7MdGHg2WZ88KvkFZuHngb52cAiuiEXycrs2bXP1ANJirx2Vp5X-gs6HNMISFMqjL3tiQRbECYKGpeexwy_7dJBzGaDQ1H-_9gmEkZKawny9TepVgsx7a8YFPuT1CIv_GRPd7gsuANeKKM8d78i0VRmTmQJx4C4d6kMDoQkG8FJ2v6JuBlmR3KvWYPOBNj55VUEI1wVpTPv6BMg_nw2uSrYLoBFMTCyyCkxuCW_B6305UD6w5azGvV-9wE6LmmQie8n3Ock0Xlov5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9282b8e98b.mp4?token=rr1v9onKhKyl3GyUmeASouVQwnWu_2fo7TNOed52a4o55a3H3mUCsMVAJzVDKjas_qc07kqec7MdGHg2WZ88KvkFZuHngb52cAiuiEXycrs2bXP1ANJirx2Vp5X-gs6HNMISFMqjL3tiQRbECYKGpeexwy_7dJBzGaDQ1H-_9gmEkZKawny9TepVgsx7a8YFPuT1CIv_GRPd7gsuANeKKM8d78i0VRmTmQJx4C4d6kMDoQkG8FJ2v6JuBlmR3KvWYPOBNj55VUEI1wVpTPv6BMg_nw2uSrYLoBFMTCyyCkxuCW_B6305UD6w5azGvV-9wE6LmmQie8n3Ock0Xlov5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یادی‌ کنیم از این ویدیو پارسال؛ میکا ریچاردز به‌مارکینیوش‌میگه‌میتونم مدالتو لمس کنم؟ هانری هم میپره وسط و میگه بخاطر اینه تاحالا بدستش نیاورده؛ مارکینیوش هم میگه منم مثل تو بودم
😂
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22584" target="_blank">📅 09:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22582">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9pcKMKUj_wTsiKyhRh7AS5U4SD4CJoWxtyCCtgifrTrsoMDz409SrdkJBuLIQ6fjVL4GNBV3fardK50iSvtQRCg0H7eHWnhxJv8GLpb1hrkM2Oucx4op8ty5DFx7dwEvPJQ5MJxMxFDuZIReiV6lMnMRIN-XIZA4wSe-qSUEXPmQunbdUWo_oLgqemZI7p3UXsx_ClN1oeYSN_nFUNj0n1W6t7x0K2pNxnSniltww7vsXbqMEsrR_DVFN9-XYGY8hSuVIFX877bwEcDwhd4JL-ltsBhKIHxA5kPyy0i9e5rqnAHvHBx657_5wEa3B6E45F5degX5nPUOH_qIo7GRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
از جدال یاران هالند برابر سوئد تا تقابل ازبک‌ها با میزبان جام‌جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22582" target="_blank">📅 01:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22581">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjdsbCDMbuuKKn-rSG6XHZ1EG979ZAe5_eUVFmJ6-WDdX9xi4z-mrUX2MXUWFLLu5LnNfRZJnozpWrffx7bcrkoifh2oNbZGxzdP3QCBPN4bTDoxi46m_N8hOrdU2TjPuEK4VfMKXHOFlxgxxSRIK7UFEctXik1I6msTfDMCZuZomwi2RlVJ_LlmK9oUtewi_L4RxswMdLEBmeAAiEnICHdiiJeGtJByn5h_XIh1x5WlAyaxL5y51A5OHBACW3_fZH8gl847cV83c3PY0DATwya6tU_rRcdM_NJzhxTLIYdhVPiFBawXGGFf7HqTFs0cA5Ej9icINKXLAGRKbOeGJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار‌های دیروز؛
از برد قاطع مانشافت برابر فنلاند تا برتری آمریکایی‌ها مقابل سنگال
بازی شاگردای آنجلوتی مقابل پاناما هم تا پایان نیمه‌اول با نتیجه 2-1 به سود سلسائو در جریانه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22581" target="_blank">📅 01:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22579">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VH339z54zPZ6GtjXvQnCb6HyhuB3ySfLOIiN6B9F7lCqwsyJw_1e09pW_CuSD-bV7BrJ-UkpJOcB5PSEcN9g5hb8ZosLg9dbsU0fIEvOo54IPkPPsiuqKosI-YH5sovNisiQSZm1mAsu209986z2nl75FTnnk2gacnQevflJuBtJ0EB1drtmHw6yRTprl5xR-noNToLvworVunneXneuYCbI3ebD7fOSlk8iTHgJYR_M8jsHTVYmfTpmje98b6wOP7s5c77g3hPVsb-7OrLjReGG9beGeLzHgN0zG9hkHsy4wM2cfidHC7btTdhhjpi1aYkhKMr6g7g-3K2C4a_TwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/resn5S05V_Usp9I-1BKHCkgp95lBVESULgi8wEFvXH1XIRh88YuCQPVkHgoqqRL5qVUJzD9miECBAzMq7_9rGU3sMzdlL2MBa_eEuisYd4K0x4W7Fty9yRM6v41JX1gjViKHarwmgAIv5WrqOePWcnWbN2qvXpirCseZ2gVgPrG20FCwXdEQHpUAGgXJt6YiXa6Yc7gKr6xvdXPGSjyo3cp4-5VSfrn9kVWJxSRH6fDjK6G06tZPjibYQ-MkB7BrqAJ-1zzps0C86qc025vioaxZu3sueVEE9qdTngP0Zcapodx6_L4ul5k2VafAFluTmm_GWGW3eXHTFFuea9XjAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
مری‌راک مدل اونلی‌فنز قبل بازی فینال لیگ قهرمانان به سافونوف وعده یک «شب پرشور» به ازای هر سیو رو داد. همسر سافونوف که از این موضوع مطلع شده بود گفت: شوهرم اصلاً نمیدونه که «شب پرشور» چیه. برای اون شور و هیجان یعنی حل کردن پازل، تماشای مسابقه تلویزیونی‌وخوابیدن‌راس‌ساعت ۱۱:۳۰ شب چون صبح باید بره‌سرتمرین؛ بخاطر سبک بازی آرتتا، سافونوف در طول ۱۲۰ دقیقه سیوی نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22579" target="_blank">📅 00:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22578">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHw3Yr1Vn85zWW8vncH61rHHrnmlXgEUTJ7jkUR0ogdrYhofkGQfhZ_1FQowaoLYPZF8rGVma-ikQM_JTjDJ0kGjZ95cAvumisaYquKTG-bGq3lmH3FX2Z3HmeZsn2cZEDxB80kNeCikX9EstLlKaHu3q23-es1ukW20Ynf-ITMJeAA9nW7QBrn2QF0cQ7y98Ume74VP0rA5y3g7CqH9OEjIiNxwP-7GEWwXKXFtThXhdocrcNIj4wMuzu5Y3vM3QeRT_P2Qie4umJ3tH46jC_jweDEFDF6cs0LRZTdaf9jH0drW-L2rsSYVoxoaWs55EgoUxp7UnLzzz1pM_T3y7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درحالیکه اخیرا رسانه‌ها خبر از مذاکرات باشگاه استقلال با محمدخلیفه گلرآلومینیوم دادند اما اعلام کردیم خلیفه‌ازتراکتور آفر دریافت کرده نه استقلال؛ حالا امشب‌هم علی تاجرنیا رئیس‌هیات‌مدیره باشگاه استقلال نیز اعلام کرده که هیییچ گونه صحبتی با او و باشگاه آلومینیوم…</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22578" target="_blank">📅 00:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22577">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/909763a6a9.mp4?token=tedmBAEq7r9qfPh1VsfAfyqTUg_VKOMMufOqHXlvHV1qBkZDxwB06sGqpkuqTKZ3kBtuwaSX5RzA8kUoCmGSi3wimmmKS9SYmg89RdmCia6ILbx3RFPI6N2g7GPta72Y9-78I_fheJMh89PMtPbbWXjLlsWSLscgAcOvOMU8_fjD5w6ALKBBDSfqw9PnA8wK-qEw7wc60-85BnhNXxWGX8FsZ36g7R7pkXt3zoXEgIwttmUi3QNWW_a4f7wJOH25Lip_2ha9M55WMoYG9DDBumtkEMp_19S0gCvRYAC7hMYBcqEqYtIlIOJbIvfF9kc_cifWhdeNyB9HyI5tJDhgyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/909763a6a9.mp4?token=tedmBAEq7r9qfPh1VsfAfyqTUg_VKOMMufOqHXlvHV1qBkZDxwB06sGqpkuqTKZ3kBtuwaSX5RzA8kUoCmGSi3wimmmKS9SYmg89RdmCia6ILbx3RFPI6N2g7GPta72Y9-78I_fheJMh89PMtPbbWXjLlsWSLscgAcOvOMU8_fjD5w6ALKBBDSfqw9PnA8wK-qEw7wc60-85BnhNXxWGX8FsZ36g7R7pkXt3zoXEgIwttmUi3QNWW_a4f7wJOH25Lip_2ha9M55WMoYG9DDBumtkEMp_19S0gCvRYAC7hMYBcqEqYtIlIOJbIvfF9kc_cifWhdeNyB9HyI5tJDhgyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
پاری سن ژرمن انریکه کاری کرده که دیگه تیم ها برای قرار گرفتن در بین 8 تیم برتر اونقدر تقلا نکنن؛ جالبه که از این 8 تیم 6 تیم رو امسال برده، مقابل سیتی بازی نکرده و فقط مقابل اسپورتینگ باخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22577" target="_blank">📅 00:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22576">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4LDL4giYXAAnedqUS1FrDS_-Q78J_N1pdxuWrcSjCFMH-YzsJTz-mrtRhVd4GjGj_XQvi33GyFyODgv0u1_zx_ubUXh2pHWR_Ejgi29696ka6l2OQOYg4r68N39sgYgjsEKhe91cjqSm6js56wD9zhYOm0ZQDCxNNI13ybcvZvzrabiXVSwdRqfOTZS2fDXvuPpW1ynTLBJo-gTSLPfP9Mt3zMOST0SCLQLMw9O2MCEJvirJqgo9YDIbd9VoDwuCcoCaUmEWpSEfOWY3Ll0hSmSigFbJjjAR3yHac0gdzFVrZc9FjQojxiXwkuGtsMxqaQ2aE2qsBajqakYPk29ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اگر همین الان توی سایت
#وینرو
عضو بشی
🤩
🤩
🤩
هزار تومان شارژ رایگان میگیری
❕
✅
من خودم عضو شدم بدون واریز ۵۰۰ تومان گرفتم باهاش فوتبال پیش بینی کردم پولم شد ۲ میلیون
❕
💚
خیلی راحت هم برداشت کردم کل پولم رو
💵
💳
پرداخت‌مستقیم وسریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
🔴
این فرصت محدود رو از دست ندید:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
a10
📱
@winro_io</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22576" target="_blank">📅 00:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22575">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DekuGZJXLlt_HvjLEC4ZX3ONL5gSJ-U_w19K25MNFABsF8xfysk_w9bVfWMdlTznmYFanmrnqvJKXu01aSOjmy51zWfRfZGQQxHXCEhR1ifwmscEF1xPvF2ka76POLbVHGBteaiYDBAXzQ6KyMXTl7s8H1wXfrhbbdYQkGK9zR43XUMvwfhgLDtdnJp0FmF_Ic48nB6BOpv20uNJ8UmBAQkez2vHMC1siKPJCJOI8whO4Kq32ZvVr0PiLqlhWXg-WJTwTp6GeTINBP856uu8OZcT_X4m0IGds2Jbv_-dLQJvYwhE9ltnEN0mMUtl2n5Wq3KXHBtdq8rYLrg4uIc_ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
پاریسن‌ژرمن بعدِ قهرمانی در لیگ قهرمانان اروپا فصل ۲۰۲۵/۲۰۲۶ توانست‌درآمدی‌نزدیک‌به ۱۵۰ میلیون یورو از محل جوایز نقدی این رقابت‌ها کسب کند.
🔵
نکته‌قابل توجه اینه طی دو فصل اخیر، مجموع درآمد این باشگاه از UCL به حدود ۳۰۰ میلیون یورو رسیده؛ رقمی که بدون در…</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22575" target="_blank">📅 00:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22574">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pr0PbmG2N1iLVKEBBoXhygxJhKJ2OsCXMQhZ5qsEKc_6V2GrbmDky-5JLQN_gq2byuKMf0kSn7BT7RSDilHNFbiZnqeUVZQ7MP2NZGNhs0ai3JL0zLWE4xnXZfDFD0hDvZBlfw09_d2NcPiUJLh-yKqK0OCUBQFNC1_RcTBzZ1uFyItaaPrJ07Pj2B-fnCK6bBbDtCrFGdFaC6JgtryEggrJANbIsetBMUcOQ7XMJGLe-KeSc_FJ5ysW2D9FYqCwcq52zuOTBpQjBmcskmaPlStvgL_pdVFZxnMhfuuszShqT8oEQEZxuWt9dUuiWvPFTijwOyxbExGSP2Cw8Z8wpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باشگاه پرسپولیس پیشنهاد مالی بسیار بالایی رو بمدت‌سه‌فصل به آریا یوسفی داده و احتمال قبول‌کردن‌این‌آفر فوق العاده از سوی این بازیکن ملی‌پوش‌بسیارزیاد است. سالانه 80 میلیارد تومان پایه دستمزد + 20 میلیارد تومان آپشن.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22574" target="_blank">📅 23:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22573">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiCTv4xKNen_00pxXG2TLlPumb6TkZ5coxVZe1e1Q1dTQPxA-LAcR0bl2e5UYu4WavEMxLdUeUmpp1MCTiTHupEWL1JPywajX2Id6Z-8F3_zvOOUK0CJxEKI82phHpAzxc8idb6Rjkgptp6Qscy2iUHzsUpdRcYWCZysxDJiCdSDh_0oAH0FflftOFYsYs_6PQA9uHES6wRXo3Dy54htR53Reaus4E9RSkH8qIi0d4ChTOwt-xOmcIgjZ4dkrwzGU0lHhuxAfm82u3Hm_InxtiqZ9RFt8FNRFl9bBMJIvAdRMlDg8Hb-yPtFjttGQ4XgajiYhedr6p-Gxc-5smzlfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22573" target="_blank">📅 23:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22572">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3f2e6ecbb.mp4?token=Ds58ju1pUfCFxqBzzxH3bECRL69ZmSYQNmn9oyNLPPZ8CFjGB262KsWJJve3tZvgXVZGA3aDVWVcI6CUwCMzQozTKYZoQPYfFWtAc68xfPnS9XmZtw9PynH0s6TcymIUhksUZ_N7PoQV0mz-TMLJO0RS-TaZSNG-wMPdRichIHQN1o2mZGPwotABGgCPag8XhjK5SLf0KIpAR15aaOBfF_G-wCidWeIDRpK8s0ZX9nCmH1AmwMdi_ttcK_dj3eF-51Vb0pjDPKNMjxF8y0QHs00td_ut_28BXr-VIDCkbJUeerj36XeA1KCQiyESf6ZlfAUtaYfbueJrTmpx8Pn_XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3f2e6ecbb.mp4?token=Ds58ju1pUfCFxqBzzxH3bECRL69ZmSYQNmn9oyNLPPZ8CFjGB262KsWJJve3tZvgXVZGA3aDVWVcI6CUwCMzQozTKYZoQPYfFWtAc68xfPnS9XmZtw9PynH0s6TcymIUhksUZ_N7PoQV0mz-TMLJO0RS-TaZSNG-wMPdRichIHQN1o2mZGPwotABGgCPag8XhjK5SLf0KIpAR15aaOBfF_G-wCidWeIDRpK8s0ZX9nCmH1AmwMdi_ttcK_dj3eF-51Vb0pjDPKNMjxF8y0QHs00td_ut_28BXr-VIDCkbJUeerj36XeA1KCQiyESf6ZlfAUtaYfbueJrTmpx8Pn_XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
یه فلش بک بزنیم به زمانی که لالیگا اسپانیا برای رئال‌ مادرید و بارسلونا درواقع یه فارمرلیگ بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22572" target="_blank">📅 23:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22571">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNpPXuLUbfZlLy7X3al3zMl6tddPAbqBJkmlAlT-2SBl-cRkcW3FlkHutIdRmZi5onslfYsw2cq7blGgrj9IP09AVRBkVRQaPJ6jQeIH6A9Tm6zvFM4n6X-P2MlUt3qAcOKTdr0Po_yO4PWRnDXIy4AJFG4oB2JX-gIVW74v0ygWRnN_0nFnD3ITSnnVLBDVONBTJ4cvfOgdRoQwogh4C4waQiJ_1a4bimWcQjih2Pfz26CBUF-PKrko2ls-iUTh6lJq3Q2Nfq5EzDIr3QaonFYKLjnm3T0RseHp3YjRwnNshHvb4u3mNy3koE36zp6VPIfgQqcHaUD_QOcNwYiwQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ابراهیم کوناته‌مدافع‌فرانسوی‌لیورپول قراردادش رو با این باشگاه تمدید نکرد و رسما از جمع لک لک‌ها جدا شد. کوناته هم اکنون بازیکن آزاد بشمار می‌آید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22571" target="_blank">📅 23:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22570">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7N4yts73V3RMAzNufduT82myXUF8klB7HdzYvLY1W_eefLJBFXTcD2api5IgbDed4RVH1FybV20pUDtoQVhKfGu-sXsLwNsJdl7J6FJjjQDH50gLjzK7__KoXrlTsnu0pTYJVL3ZPGGWaa3BzKlDs_49Zid3YSX-oG-o3Y_deqU5-ROzXKCCHPnoBjGMgplaVuGFGd7RQOLRqO1iZ6KQwmNC_y-CDgHQlY3gmAcf8_YTen_CYJhoqNToxt1odOI4-K2xVVy5XnDk7tmKmEtdyCEaXfHu0ab32PlE3sErZkoRUByQIoOxon3eR0AI9qgK_jJioyBUibgIP52PfcBxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ایجنت نونو مندس مدافع‌چپ پرتعالی PSG در تلاشه که درتابستان پیش رو این بازیکن رو راهی رئال مادرید کنه. مندس اعلام کرده درصورت جدایی ازPSGتنهاحاضره راهی رئال مادرید بشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22570" target="_blank">📅 22:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22568">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S3xToXfdCK5KFJLhFAbE09DMSuncsjdwghR5FupsOTqE4zlTZQgHEpgoMaRkCGZ1vH_1Zz76Qbl7ajBNU_E_5ixFa6l5Cf8-DS3YvoLr2V2SMbv0pTrNmaOGF3QZDmD0UqZGh9YroNsr3vEFOlBt7Icopv30QmJYTJiWyV2locnw3bjEwNpswlELCQspcxLiyoltUDgaCs-p6SPn8GF7CO1dsBy09s8ePykr94lpXChjpm0yjcyG1ZaESc33wE7qVPSLB0Zlbv6U4eAdPGm49XMS9ny1D5b9LJB_HVDSOpwVClH7c1jCoQ9jTkJ_3pRAK4W2aXoRhXy6NT49RyTGBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dp3nlHwwsbFT6BQvY69mXgtFSdqNCmFYxqNQpRTYty1iqR2c3P1z4nEv3AvDRT7e-ft3DnwlU0OP9p_0vQOQFhI3gXOvvTnsg1Xcchd2c-DxYGJzA2RmGJbeA0-f8GGV-ywpsw0JQ9gs6obnGjFUI8XzsPvgszV2GeEgIE64nqQAp1Gia-axk_Esu9YIr0W8jf2Suq2Ez8-1Oz7AmgozfH8tUblAO_I7CjDq1y2jnIGpUKpCE2izU0WQGa1tk_90lkPc6FLXhe1dIacLEjnUr-X7YlGWI94wiSjV48ASeFM6cHD6d8IqO6otQRnAgLwbCbpCA5aHvDzaalPkp91jIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
فواید پیاده روی رو ببینید؛ گشاد بازی رو کنار بزارید؛ فقط یه‌ساعت پیاده روی عادی میتونه بیشتر ازاون چیزیکه فکرش رو میکنی بدنت رو تغییر بده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22568" target="_blank">📅 22:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22567">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-3q_QbpYSkkHdgH2AF6BOs4WDDBsV_b-HyO4aJvaDZRkpLbvkfYQW5UjkkrZwTzGkhF3JaJ6Klcij-xaFT2kdVPfZElEt2XxKosbcdcuq9DygixINlvQ-uj6Grs3-_o9HTeS6vRUtA5DbVyCCiFVNMi6kI5FZM0VgyA-9r5tQSNJhrQ_urdKJ1ul-NKpqOgw_Gi4ekzwBkWbCnqMQS12M-6EqKUpzMemRN2wVzHA7ninUkUdVobHywAXbOYecnzTU5DPRDUWdiwObLyLAX9-O2u16K-Y3BXQBGOQqXdH4Vf7JjS3Mun8L1B_sD_MnlQzOhYJEWu5f0JiS16MrPrdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌انتقالات|فرناندو پولو خبرنگار موندو: خولیان آلوارز بزودی‌قراردادش رو با باشگاه بارسلونا امضا خواهدکرد. ایجنت آلوارز به باشگاه‌های آرسنال و چلسی اعلام‌کرده‌است که ستاره آرژانتینی اتلتیکو مادرید با آبی اناری به توافق کامل رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22567" target="_blank">📅 22:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22566">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COa_P3P8UWnmdk5qGZ5mzfWc2ZN-899Q0q7yg0j5lyFm-q1V9AhBOg3YiyOhlKEUoJJ0VtWFWpyyZR7wsC-jXqQRRqgjErnFB2P6v0xDMv86A0hrc32h13_tf7c3pblvafg1L8nYgSOD8e71GuQp0q8FYJh33Odgw6zO-WJoLW4FlbrISMqAScAxic0F2xNdo36BydX3LqrJrxxwxCh3CN1ycA3kP4Og32UYwF124Z2lrPUcKWX6IF5kIU9tBgYd9CqFcZfJOa09IRmhTYvWDobwDwbwjhyw9Tgn8dE8ul87YAP9CQ_qufdEIbC4e82mRne9e0oeuhOWXIhM8cUh1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 20 روز پیش پرشیانا
🎙
رئیس‌سازمان‌لیگ: به این نتیجه‌رسیدیم که امکان برگزاری ادامه رقابت های این فصل لیگ برتر مقدور نمیباشد و براساس جدول فعلی سه تیم اول رو به رقابت‌های آسیایی فصل اینده معرفی کردیم.
‼️
همچنین درصورتی که سنگ اندازی نشود بعد…</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22566" target="_blank">📅 22:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22564">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e-e9orZww9-i4OSZlPJ5hH4kHXCxoBf4F4IxPBdghO0l7w-Vo4NAK7ogbcEX9FeSWO3KEyrj8gGlbgo9tTka5paAAnnxuF__-EdhyeF9KwbS4E7IBETdqQj4GXuvX-wZm6TyzWDzSM8DbVm6JyIC3cQWP4DtHQnCqwnWJYjLuOmFDCrjPlDDFJ5T9F4SLUghtvjKJSqwaynGKHl2k5_CwEAlAUq3gj-D1W3xhgU5QE1tQe6phnn4g1nKRPWzcvUfurvk_F3FP3aEiLOxDa6DRJVc2MDXiLQd-2xNBrjf0CM6M72tjf3lwSdL3WX6Ztvyf3fUDBvvcU_JADMzFy5-AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g92M-EPe7dyIQUUvfRA4jygWqhN73Hz9P5RFe3wrWCR_OUq34iEPc0fl6c5GnvsvfBe5JpcaReICBcJdNS7qrxSxEgTfM-piMOfW6wVlSjKI1WczYyLtQlVgVfXPuvKuUbVEOyF2xitBAt7_7lqMW1F38fAvw0mE6nQaCESR6N-BCGqMGofB6r0XwPxv45KJJLky6rgyvayjwBuzMr_MU9AgYktI6miNbkLtpUXlcVP1ketcipTG6d37lNAxk1jnCAw-7Ut3ZAyaOvVCFzMdv4VFNKex-MsiGSIz2keUVAYtZkKPmmva0uI8t2XWS0eRjOH0k2S8-CPFTC_XZ54GPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
خبرنگار معروف ترکیه‌ای:
رویایم قهرمانی پرتعال با کریس رونالدو در جام جهانی است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22564" target="_blank">📅 21:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22563">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1dc755209.mp4?token=iHmDxzpQqzx68--GlMKLO7QDE_VaspRJch5G1FK-1F58yQcC_A6L_FAeuElWBWCa9dR6vGvdMcdlwFCJu8vDCc7w21Oo-0rF1fPu3ApLJeS4Zc3rd8NP0lFqV2AwSA4nHSX9eoeshuDcz6jbKJSW1a-W2HiYuJEqcRMO327OG-36q94HRTBVb1roWCJS-7W8wvPZ2jzROd7IBPfmxpYqPTYXy8m9BezIYwXWkeKH18cv6ZOnmqzezVSasa2lZQNLRHWwKXW9iRghxpfPkP3an7U7-kZeQKwS-kkOEmt9K9X1Yh7Lpd1RIH5OD0G34rOft4JGZ88BTMonTK1MHcRVq6ScfQT0Ko2fM5DQJvpicP0Wj0fJgqucU9Vw3bmoXvCz1LCaXJRHZHfUTFu0tjTPkArIDyX6gzUTMzd-b30LsehkeZkWn1yUYrihSAD6rMSfzNpWSCfKrgj3jG0n1wcdl85Ns17usPwYa6yqC-GBrYlNVTJoXhn8TSGo1DQ_sE3l41HOBGn7Ev91KEWXFXZpyc8cgAUFd9BowoyxwMkEs3qRvz0T9aJX9cF8V6NjhYY5B8RCWeCfKnIvK12tM93ITNX1PmrvBkElJTw7cEE2TDYIEYkTB1CJwpybJQJjBFg_aCZ_hWXIVU1ic-MJGJMH7xolObSKdDWENRTKcTb9BEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1dc755209.mp4?token=iHmDxzpQqzx68--GlMKLO7QDE_VaspRJch5G1FK-1F58yQcC_A6L_FAeuElWBWCa9dR6vGvdMcdlwFCJu8vDCc7w21Oo-0rF1fPu3ApLJeS4Zc3rd8NP0lFqV2AwSA4nHSX9eoeshuDcz6jbKJSW1a-W2HiYuJEqcRMO327OG-36q94HRTBVb1roWCJS-7W8wvPZ2jzROd7IBPfmxpYqPTYXy8m9BezIYwXWkeKH18cv6ZOnmqzezVSasa2lZQNLRHWwKXW9iRghxpfPkP3an7U7-kZeQKwS-kkOEmt9K9X1Yh7Lpd1RIH5OD0G34rOft4JGZ88BTMonTK1MHcRVq6ScfQT0Ko2fM5DQJvpicP0Wj0fJgqucU9Vw3bmoXvCz1LCaXJRHZHfUTFu0tjTPkArIDyX6gzUTMzd-b30LsehkeZkWn1yUYrihSAD6rMSfzNpWSCfKrgj3jG0n1wcdl85Ns17usPwYa6yqC-GBrYlNVTJoXhn8TSGo1DQ_sE3l41HOBGn7Ev91KEWXFXZpyc8cgAUFd9BowoyxwMkEs3qRvz0T9aJX9cF8V6NjhYY5B8RCWeCfKnIvK12tM93ITNX1PmrvBkElJTw7cEE2TDYIEYkTB1CJwpybJQJjBFg_aCZ_hWXIVU1ic-MJGJMH7xolObSKdDWENRTKcTb9BEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفت قیچی‌ برگردون‌های برتر تاریخ رقابت های لیگ برتر انگلیس؛ عالی بودند از دست ندید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22563" target="_blank">📅 21:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22562">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjAx14jGp44fCrQivc4MzIQda2FIDld0VSdR9vmb6dhyw3QHDrx3LmekdABFXNyF8W5WPea6hQ297ETNlQ23EecOxlWhvFctBgNX2RnlKY_EN4rJ4h2J-mDwlgDb8hbMXr9r6KXmEp9WRNhHbJ5z0kAvmUCl5EIKzMNvv45x_FZFKhClVTTcNODn86W-0jBdx1hbjxsuZCWYjvUyzquyK8AoRR3JTh530SdfL55Ry9UhW8K_uay-csM084yJeJO2EKpuApTWvUdf6N8Ol8PIC9eCAP4Qxpavxeqq71mhGPh9EBrn0QO44U1YS_NV3mjg8O4tZdACfJKLuNZTu8V75A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
#تکمیلی؛ خبرنگار موندو: داروین نونیز از طریق مدیرام الهلال آمادگی‌خود را برای پیوستن به بارسلونا اعلام کرده‌است. باشگاه الهلال اخیرا ستاره اروگوئه‌ای خود را به آبی‌اناری‌ها پیشنهاد داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22562" target="_blank">📅 21:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22561">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKWKbHT8O8xtPsikR0n69nawI2ZtkpSixxmR2tFRLYYOcFfxsKy0iC7vF6nf6kJg9z4uo8_CN50YXaAVceWJJ3afReFLIPIUNSe910q9cFSXhTih_IELDZ6MlH7yASvwio56dBoi7apK2hcOlrYLByvgfv0PeN0dmCqF-wf-EUIgDB2cjXkuODlfW_qKzcXGhmpRprgbD1drZ7LVkuhS4bBsue_yg80BIyzlNDwGxFyfciJRMmvkoc8C0QZwozMY7KX3wwHqDNGqWHr4pbos58UrRChgv-TMrMUO3wyFHh0UOd9bNgutfGAyqVuRIHoVcIIgurrJqIZhE8W-6suwQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ مدیران باشگاه پرسپولیس بامدیران‌دوتیم چادرملو اردکان و گل گهر سیرجان تماس‌گرفته‌اند تا رضایت این دو باشگاه رو برای رفتن سرخپوشان به آسیا بدست بیاورند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22561" target="_blank">📅 21:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22560">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3OTw0tKaUKgyBqvfNIZ9bS_wQvjKs_m-HdQfohChybv7xsnSqYVVUS2-S-5uFY7jduhoQn-54-22XCVkQNKlT1wR8kaskXrbFsyrXa8whPmYiS-xSpjiEc9TfUwGEW8z3Pd4WmcWvzJT2cnBdqh5dN2QL-GVjlg-tu0r32yhJ9fY7setfAr5XIxWzkIFRTO8gpHbRO4fc-oGOqTgaUyJaUaUWjxpk1FbfFaH29Ldi4MmnSy4BOfs8ZlGYwYAjFbV2oc41NlNbywLNULZLlsl7moyIhHIHrdZLSdx8AconhqJ3bG0I2Oh_OVXNYlXPuMw0PyT0ViTWL8_HgSpG_32w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی اسطوره‌داوری ایران در اعتراض به کشتار بیش از ۵۰ هزار نفر توسط نیروی سرکوب جمهوری اسلامی در جریان انقلاب ملی ایرانیان، با بازنشر یک‌ویدیونوشت: «برای بقای کثیف خودتون، جون عزیزانمونو بلعیدید. قرار ما با شما؛ نه دادگاه، نه‌بخشش. رقص و پایکوبی روی…</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22560" target="_blank">📅 20:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22559">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJLJ_9yM-LKCByCs-wU0eBaFgN2zVIhRWD48VHQZ9YJ0pjy22i8j7pU9gYFTKhC1282mLUCIHIMn56qa58BONymZrXmO-yfriVd1_9_UpLJcM6katEeimQFwCjKUjyC4NpwEI3oUSb-MOHn1ngnKAv7nFQeuYDrNhoBMNRCapuOhU-px68Y35s8fFZ6ccNA0Y9_bytao2FruldFjJwruugplkLbMTPBVdh0yuA0NuJEXl-OQAXRp-Le6TsZYcB6HhXfLh8WoQOZ0zA2QtmNJRlCWGk_PtWqjy3v5e0n4xlfiE4noR58M6oActkA42QnXkhCWSCM-bmJavJ89svniQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرنوشت عجیب امباپه در UCL: سه فصل آفر رئال مادرید رو رد کرد همون سه فصل رئال قهرمان چمپیونزلیگ شد. بعدش این دو فصله که اومده رئال مادرید که PSG تیمش سابق داره پیاپی قهرمان این رقابت‌ها میشه. دمبله هم تو قهرمانی دبل کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22559" target="_blank">📅 20:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22558">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55a2c0be9f.mp4?token=XmjjZtCnqlY0D1_1o4OqrZzCyTHM3aUL_xsLJlflqnN2x9Ce74XgeqnsyNWJwpLG3Gy2JvrrZ1zWBypMsIqsJew9KQ1z-4FLYqS1m0BA7ei0mIeO66g-gDUwthc8GWYbCJDMhnNkm_E6jBFDHRbF_VUciMWxKDWburuYGLd7lUcAbHmiI45eYQXElwjR8L455hfF88N1W1LszLdCvPmQsp1gseISm1SGOvyGqfFv-GPhkiB68WlyLL_r1YzHBh1TiDk2tofC_fvaAUcYs2JLUErSqzZFgeUjxrMjsFAUhMi4-jOM7MjpVRQlvJ4jtKW56sDtdPZGoA9r1ZDn2AX8gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55a2c0be9f.mp4?token=XmjjZtCnqlY0D1_1o4OqrZzCyTHM3aUL_xsLJlflqnN2x9Ce74XgeqnsyNWJwpLG3Gy2JvrrZ1zWBypMsIqsJew9KQ1z-4FLYqS1m0BA7ei0mIeO66g-gDUwthc8GWYbCJDMhnNkm_E6jBFDHRbF_VUciMWxKDWburuYGLd7lUcAbHmiI45eYQXElwjR8L455hfF88N1W1LszLdCvPmQsp1gseISm1SGOvyGqfFv-GPhkiB68WlyLL_r1YzHBh1TiDk2tofC_fvaAUcYs2JLUErSqzZFgeUjxrMjsFAUhMi4-jOM7MjpVRQlvJ4jtKW56sDtdPZGoA9r1ZDn2AX8gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ازهواداران‌بانو تیم‌های حاضر در رقابت های جام جهانی 2026؛ شما طرفدار کدوم تیمید؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22558" target="_blank">📅 20:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22557">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHkDzem2VjToDub_COZ2R7ztEVrtIE6eHXvt5VgBNXOyVAmRpGz2XfQdfZYpADGvgoRB8Z1K65y8UyAD2wLJgb5GGqPDa_9K3BkJVQGeuH4kh5O-CjXDUZX65aapp9grMcpe_7pl_6_84ns5FoxXL9cYYZ8ADZeO2HBx1_eKfiZUaX0raG0SnVBcoX0L0-iqj0hxp3LPcjKXIDT7fUVEcgm2HcSU8kHFJxpap3EED-dlhfX7-_FdCnek26oSY8JnB5BLIz5SqpvNKCE2znxKxBsDhvsoaUtH-DAxUvr0zwK3U6cGkWO4qcQe_90dB09-MTXMb9w6h-zofw0zFr_g8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#فوری
؛ مسعودپزشکیان دقایقی‌قبل به دلیل تسلط کامل‌فرماندهان‌سپاه ازسمت‌خود استعفا داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22557" target="_blank">📅 20:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22556">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqVkzB2KXTWdqe1LO-Kk9U9rdO51LIvIz7CT5NiOaEWKZ8MlQQD2MmcE30qIBVahcsWNz-fvLdxKxM9FCAAgSLvQt1ipvpu1E1hVk1wxeFpq10mLu53k1nUehpMlO0fO-RZ9znqVJhGcFlobiOUQ3OYlDaeFcqOA5qOvehUdVwDiEb8ebLbtaVBJphjAM7VaXvPZeZgNAr3OTQVtIhnft6NRROZIwslRvJmmuFAuTmmcsuJZjPjm-_955_t59HitgbcT1HvDgEBzK9_B8JGhNbFxtTEnIHGoj77olmTr5Updb9Nen1gm_H3xxESa5snS2iqelabXxGFSm-_Fieab3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بااعلام‌کنفدراسیون فوتبال آسیا؛ مجوز حرفه ای باشگاه سپاهان برای حضور در سطح دوم رقابت های لیگ‌ قهرمانان‌ آسیا صادر نشد و فدراسیون موظفه که یک باشگاه لیگ برتری دیگر رو به AFC معرفی کند.
🔴
درصورتیکه که فدراسیون باشگاه پرسپولیس رو به AFC معرفی کند. اونوقت سرخ…</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22556" target="_blank">📅 19:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22555">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9e3xciTkyTYKOgHoH6DiliYGXtRQA74bvRwH_Wr-6tS8H75W6fYtNXQ8QCLovUK2SIlo09V4ruornsbWO2_Z4S11Ss4RMzS5udiX6NCF9eIGeNwaDcXibA9iUProBbq63X0kVhveCC_Rxtg5ddUnRly4DUMDCaq6fF0faROL2Z4f-WW93y4fmly7HghpWDkrRJGgb2211baYIo7swep4KQX90OaUJ06YzDZB9cnCFupMvRnnqhbxYJNrWSKCLjugxd6rWgvzmlGIIaLPdN53UTca_-ayAyp8tA3eEKYRQzjSVGFY2oMQnHv7gXj7jpAIYLQK7LQwuqVhn7WD0YDnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|کوناته مدافع‌ فرانسوی لیورپول به‌سران این‌باشگاه اعلام کرده که پس از جام‌جهانی از جمع شاگردان اسلوت جدا میشه. از رئال‌ مادرید به عنوان مقصد احتمالی این بازیکن یاد می‌شود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22555" target="_blank">📅 19:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22553">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnk7yj_WzSV5Fela2Yv_ECjMsyuVHmOBt0exwzXr_iE6jmRJ8miOY8CqgE9frCCOIzSSMxJXsC0l7ff-byowgPAMttetKDueee7GmJ4UmbqA7j5RZksFdPkztx43YNe9CqyFaFDg_Hv8r3mommY1_p8_ZWVmKkx_HJ6oqPROwmSFfXtX5Ws8kblznYiEgzs1cqbPqiI7QhiiPu1GsAGX0wBzssMEmekUte0mzGKWJUkL_kZLLmNhOZk6rskJBk8ipZB-I-JuGojdcL5KsAl3yLcnlvqfjKFVgb1fqPrUYSMVyMBE3033lD0ctcvXmj2val_jr0K5BfcL4Ac3FLlTLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌انتقالات|موندو:برناردو سیلوا پرتغالی تصمیم نهایی‌اش را برای‌پیوستن به بارسا گرفته و به هانسی فلیک برای‌عقدقرارداد دو ساله با آبی اناری‌ها قول داده. انتظار میره بزودی رونمایی انجام بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22553" target="_blank">📅 19:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22552">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrHl81pD3wxI8QB-I4YaiUzdRmyixkFgv45p6IptQS1Q6t_SCWx9Oe5-oVNH07JTbg-71bUmNoer788OZraZY5k42mZ0Mhehr5GzKoC6m0e-CKzB2j5ct6ICummFAPoC-n-FG1jpbiTMLRxw41N2KfeDzKM20V2tUr_ZyOi2WN9wRVQ_T7tUEPjhVXgt2fXU1c5oWViNtJaGDn4DABGVJQjkYvPu1BlbZJ3JZzVm8GRRutGAbK8ykMtT-MeF8kFnueEV7TsXYXfz-f_UM7awzop7uTOK8N9PwAmPPYASAmoPt9iVsgFIEAS2iYXvDcNJzdRprY2p6AuVdL5nlqqZag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛مدیران‌پرسپولیس به فدراسیون فوتبال اعلام کرده اند درصورتیکه این باشگاه فصل اینده در سطح دوم‌رقابت‌های‌لیگ قهرمانان‌آسیا حضور داشته باشد موافقت خود را با قهرمانی این فصل استقلال اعلام خواهند کرد. پیش‌تر تنها باشگاهی که مخالف قهرمانی استقلال در این…</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22552" target="_blank">📅 18:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22550">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eXFdGKaRtfYuHs3AhP_DI0o-vlusjb9L1ZeDqyV3UyVQXeonB34FQLBnADS7JTviWgmh3BF6dJNO_EvahXzeDDpvKn-CQ6aZzPo8A54Vqhyim9ERxbs5DObAf1HgHZgd4xJGnX6QldTVHkzuxAD8j08CA4WwOxw58sOyLkvvF1EiJDKDMFGWM7mcfKqTcDCl4wLwBA8lMS0pTxrBs3hBkfp3_C0LuneBus7fZWhuAcE3ij9jD_wVBxenamSvnKFPVnge8ajm21Tb0Tnb72aEWD42pft_5j9btB2YJ_fCipTkC6Aeg4bECDBqa0CJaVGCS92vSgpgMGu_0uBYaQUawQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RZorKf_njMkBQBmu6j9L_hzOSeOpeHI5riQsNNenkqziNmKRXGw8xdcqyFiCsB65FE4_rVV3sY4gVGeDOWDnOIwTUEgEhcCU68CGl_1zWl1Yn9iFfU6Sb-bNanxqCtm8sLO2f6oXE8yUvMwpnt9hWKRrG477FGekGvmEvxekWqfVmGuhz6rT7zPch8UqGmN2yEMMULgPi44TNui2S99M1KhgqqDDPWzRKtSdyp8bIdAcQoa9dby7syWt3mYy6QEjH7UqQwA7qBDBWcDdqgAQgRCZHbPRT7Wu1IzEaqQRO4UA78usGQikP8r8Htl4d7UPqkoLrOkqbAQxJHJC95E_jA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
👤
رقص‌تماشایی خوزه مورایس بعداز قهرمانی الشارجه درسوپرکاپ امارات؛ برگای بازیکنان ریخته. انصافا دانش‌سرمربیگری‌رو داره فقط تو ایران خیلی زود قضاوت‌ها شروع شد. حتی یه جام هم آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22550" target="_blank">📅 18:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22547">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfO7pK0yaXihTVQbwLZ_dJp-j5QqMjA7bdx8xrg4bnfJ9hBnAmfZCzAywQOiKq7KeLWoAdq_Mv78mp8PgiDSk6GKd3DP_0GHyZsyY8aXGgtI9eSi5J8WuV9uAsULmHkD3_GEI3q_qk-_f7UJw9QaI1mHTyyD77vvfyWNrhDDd0Gg6sAi24BbFNV1fg--Ui70pXxCbqr7MzxQkhYbkTvNcA_XTghMrKRT3d6VfBoWZtq__yg5QOWmARxvapYF_Rb3YyuL5A0IMosl6Rrw6uTu9sZOpul9giAs7faZPDRHLGmlG0kM9E8AGeYdOHvWzD3RjR39Y7KT312MSPqZ7zd5Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛
مالکان باشگاه پرسپولیس از عملکرد مدیریت سرخپوشان در فصل گذشته‌رضایت‌کافی ندارند و ممکن است بزودی اولویت‌نهایی و آخرین فرصت‌رو به حدادی مدیرعامل فعلی‌این‌تیم بدهند و درصورت‌ادامه عملکرد ضعیفش او رو از مدیرعاملی باشگاه پرسپولیس کنار بگذارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22547" target="_blank">📅 18:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22546">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa9a136cd.mp4?token=cxkuir0ZbdHYeoot0fhB-STd06HezttMH8hqRYIFtE1WUsUtFxJpCOBY5rs9U_kMT-a2mQF3T67XRBfSr5wC6VVyqcCGE8Kp3JP2gBpl6Ctns8n8dRAz-N1Zlbt7FEq_hVfgBjIDJuJp0b6MasV8fT__xd_OZbu-TmvWNKMduaqucKxWbWaZ3i_1HV24WxCycvxhlLza-KaFDe9X132NeMB03t3qbaqHO4QmTNV94HdC1M8evFR99yNpylNKF0248-6YDWNw86ctsHnBHtZMIaMI76AJC8fkfaSwCIQcUjqNS1sMJURpd9zu9rRLHS8OJofVC9eN3b7kgFwtrWgAFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa9a136cd.mp4?token=cxkuir0ZbdHYeoot0fhB-STd06HezttMH8hqRYIFtE1WUsUtFxJpCOBY5rs9U_kMT-a2mQF3T67XRBfSr5wC6VVyqcCGE8Kp3JP2gBpl6Ctns8n8dRAz-N1Zlbt7FEq_hVfgBjIDJuJp0b6MasV8fT__xd_OZbu-TmvWNKMduaqucKxWbWaZ3i_1HV24WxCycvxhlLza-KaFDe9X132NeMB03t3qbaqHO4QmTNV94HdC1M8evFR99yNpylNKF0248-6YDWNw86ctsHnBHtZMIaMI76AJC8fkfaSwCIQcUjqNS1sMJURpd9zu9rRLHS8OJofVC9eN3b7kgFwtrWgAFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
آماده‌ترین و بهترین‌خط هافبک حال حاضر در جام جهانی؛ بنظرتون پرتغال میتونی امسال قهرمان بشه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22546" target="_blank">📅 17:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22545">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-uqKQrfv5phA2fli8KtSXGmOqa0rrnS_RCNxcPTvsNF7NOVwV6ebpHvI_kUZ1llXzAZWLhAHQCimktCqCrP1YIfENItHvuHTi0xRU5_biz4w6HYgro3k-sL-IhBgpYuwPbNSbm27WN2ehFfa-_dPGHl05KLSxe1sQXBoCy25V2nrpvUoo_GP1_u5CJ6P58Q0rWinZB38nheCj5fg05EO2D5vMtmAANFdW5It7FIbptQBMIkdJ9Qpvb8BMWITxN_2c4CBwxSbk20oJOMuMetoma2AB-4wvnaSj0Kpi0dENnRxq7M5oT7VSbD1E0mkI5k2tHeZlmqVpw2wPH5deLXiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیویی جالب از جمع‌آوری سریع و پشم‌ ریزون صحنه کنسرت فینال دیشب در کمتر از دو دقیقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22545" target="_blank">📅 17:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22544">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeP2BUXzI-NlRcRbneR4LwPhSCdQ2CENEWUtNkEqT2wO7S7PQXj4uX4cJfs2NmvmjC0QfhzWt1U1hwUCcVsvAf_XxebIMcY_FPafxv_IYa8X4eWs3GqPvFbdjaotWUzh3CPIn3_urEHMVub0nTQvFQYg2eIzEg6LQZmHZfGXfSUJZta5iiu04iYRr1x9m9hrD6oyuph8lmJOYABLZwur2xSou5h7XP2hGoR2lRcCFV8Hxzpcb6pn6NoSFQnxmFWCdVVXM1DjAr6D_HFAawsPS29eWk82lP2_mow-37nOQOJLmrE2zlSlqqFCCkDg0Tw50gyk3UUfHw27CuPY821F2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|بارسا آمادس که ۱۳ میلیون یورو بابت فعال کردن بند فسخ قرار داد رشفورد به منچستریونایتد پرداخت‌کنه اما شیاطین سرخ مبلغ ۲۲ میلیون یورو برای فروش رشفورد میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22544" target="_blank">📅 17:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22542">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-iBKb8VWY_YdWKDNXsyx4rIuTYJUctbE8BbUj4tU25YxlJtoDVHXEjleKBefVzOp0ZQvVvifqLbVBiwFa_HJLuUxzp7uxjzofkXqZ0bA5FhIjjq6S9eqFlN-Z3SX3RiNduCCi5JF8JeDd0---qsZVY1tCs_UJ0Cfr5-BCjs70Ysgf7A4vZzV7VNCya8E3JZUy9zkcGlX96-CKa8bfuRTnZF4OQKWilcjbvfZdYh_PmzUsmlRlwwrwKeXFWPSE1uEjtcIYcmcyPBUOXgU7vR15-17hkvy27OpBn2d_zfTNUWUt0laXf6GPQTCsMavF69LWsu8r7hMir60qVsridtDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22542" target="_blank">📅 17:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22541">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11672147cd.mp4?token=gmsIOBCnrF2ip3i99B6qkuURpKjnagtfRZRjXrrvz4s4UGwdQ83ADn2qSlq8D4tMnOZSqhQMoCCefmoW8vkAV1N32UE4DaOS5cCCBaLy-xn3GWCDgZ19JTfFcDu4LD6F7mJvoHVgNrVTqQWS1jFpWaz6rmWixFCwFHaBdv2F1BJ81bEHan7VYPIzzXXBjlfvYLz0WkoAg8EbveJ-VNFSwDGGvPMWCjKIpz3gBxj5CrFanoSc66kgmSqcZvoqAJFItV8JDyslgGRIntePKDyqujsupc7dnwKQUI_yilFIVcUlyjZut6HTLaMBsknO27168yv5vVSyTXZhuNoAJnusknpo1LUyYfppIL4_GHWPI7Ua15RuY3jFMMfgSQTkzqXfDZLw3b1PFY8sBHeU4tx1jGgT7L2CNVOmC-BaR1GSUzLs8KDP9c4ICEaRwYjbeFqZUPgLNviHGNkdmklbKU2LYv950tey7GqUpD6_reCkkM2-ShTmT-U5PRu0sB-m7NTNMquA9L-Kv3a-OGT_oosQRvEnN_I5jcAgfFo9MgJ4N79SjPiymN9QjCLyFZXPRI0XF3aADS1P4RZjD28gc8jvJHmDRTfMtbACnzf6yhYIW6ho-_QN5CTQVsGDkelyXHlfk_8T9uxon925F0ezsYFv5nRb4OfN4pujpve2gI28XFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11672147cd.mp4?token=gmsIOBCnrF2ip3i99B6qkuURpKjnagtfRZRjXrrvz4s4UGwdQ83ADn2qSlq8D4tMnOZSqhQMoCCefmoW8vkAV1N32UE4DaOS5cCCBaLy-xn3GWCDgZ19JTfFcDu4LD6F7mJvoHVgNrVTqQWS1jFpWaz6rmWixFCwFHaBdv2F1BJ81bEHan7VYPIzzXXBjlfvYLz0WkoAg8EbveJ-VNFSwDGGvPMWCjKIpz3gBxj5CrFanoSc66kgmSqcZvoqAJFItV8JDyslgGRIntePKDyqujsupc7dnwKQUI_yilFIVcUlyjZut6HTLaMBsknO27168yv5vVSyTXZhuNoAJnusknpo1LUyYfppIL4_GHWPI7Ua15RuY3jFMMfgSQTkzqXfDZLw3b1PFY8sBHeU4tx1jGgT7L2CNVOmC-BaR1GSUzLs8KDP9c4ICEaRwYjbeFqZUPgLNviHGNkdmklbKU2LYv950tey7GqUpD6_reCkkM2-ShTmT-U5PRu0sB-m7NTNMquA9L-Kv3a-OGT_oosQRvEnN_I5jcAgfFo9MgJ4N79SjPiymN9QjCLyFZXPRI0XF3aADS1P4RZjD28gc8jvJHmDRTfMtbACnzf6yhYIW6ho-_QN5CTQVsGDkelyXHlfk_8T9uxon925F0ezsYFv5nRb4OfN4pujpve2gI28XFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی جالب از جمع‌آوری سریع و پشم‌ ریزون صحنه کنسرت فینال دیشب در کمتر از دو دقیقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22541" target="_blank">📅 17:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22540">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa0b950725.mp4?token=Oe-t5fMoNdEp-R6swdoH2WisXk6dZ37Z1MkwH_E2ng4ab6Ulz8zm9YuWhpaAFzLNkneMC0naBAK99aIqNP9tDWfztk10i9RC3iXqTNS9n7edcFi-UsSyDiXJyFjtvMhcut0KVimNmlktuw5QqNB7KBr5Rc1RV35x2cILyVRtcDFdYDFL_O-S7kZqT1RH2yMv4eT1CiweB129fkOdrK9byfat2R0YFtxMQNfXGxyJGOwMa01j4gbgruwkaJG1LXou_60Q7NvZxRyQYcmzbdNTVqT6avz-mTdTMk0XoZmuT4pYrkJAfxPz7K5CiPJe4zIrFXfeKlXag3zv8DD3Nn73Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa0b950725.mp4?token=Oe-t5fMoNdEp-R6swdoH2WisXk6dZ37Z1MkwH_E2ng4ab6Ulz8zm9YuWhpaAFzLNkneMC0naBAK99aIqNP9tDWfztk10i9RC3iXqTNS9n7edcFi-UsSyDiXJyFjtvMhcut0KVimNmlktuw5QqNB7KBr5Rc1RV35x2cILyVRtcDFdYDFL_O-S7kZqT1RH2yMv4eT1CiweB129fkOdrK9byfat2R0YFtxMQNfXGxyJGOwMa01j4gbgruwkaJG1LXou_60Q7NvZxRyQYcmzbdNTVqT6avz-mTdTMk0XoZmuT4pYrkJAfxPz7K5CiPJe4zIrFXfeKlXag3zv8DD3Nn73Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
پاریسن‌ژرمن بعدِ قهرمانی در لیگ قهرمانان اروپا فصل ۲۰۲۵/۲۰۲۶ توانست‌درآمدی‌نزدیک‌به ۱۵۰ میلیون یورو از محل جوایز نقدی این رقابت‌ها کسب کند.
🔵
نکته‌قابل توجه اینه طی دو فصل اخیر، مجموع درآمد این باشگاه از UCL به حدود ۳۰۰ میلیون یورو رسیده؛ رقمی که بدون در نظر گرفتن درآمدهای روز مسابقه و فروش بلیت محاسبه شده و صرفاً مربوط به جوایز و سهم‌های مالی یوفا است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22540" target="_blank">📅 16:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22539">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c4b71efa6.mp4?token=u_DnuyTFK4Aq1VdDAfCOYkIMSJuYVU_OAkZKlDLllSgU-8tKhbpIRdnK9ZCmWIKqJ_TSeIU4JfXaBnbCT4bBp091fg4ukjotJ9Y7XAY3ZJRr02r1QuVVfMnhE10ZEwweqYzgJe9CnunwSdhA1tNID8Qnh5t60Zd9z7qBvrVl9sbkbLqf6OtaOm5hDeiDYtnBvKWvWzFhP4WHnmuC9kIjOdWKQY2Z-PNtP65DlUJ6FGZApMIqVNaTZZVNuXpY7SdS1Qe7Idhc7AyybNXy6sEEuhjGL-QUAkXuIYPNLLBegLDbw3t62xKhs91u3CHYmmhGC_2UAFFfD61tRT7VEa7fpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c4b71efa6.mp4?token=u_DnuyTFK4Aq1VdDAfCOYkIMSJuYVU_OAkZKlDLllSgU-8tKhbpIRdnK9ZCmWIKqJ_TSeIU4JfXaBnbCT4bBp091fg4ukjotJ9Y7XAY3ZJRr02r1QuVVfMnhE10ZEwweqYzgJe9CnunwSdhA1tNID8Qnh5t60Zd9z7qBvrVl9sbkbLqf6OtaOm5hDeiDYtnBvKWvWzFhP4WHnmuC9kIjOdWKQY2Z-PNtP65DlUJ6FGZApMIqVNaTZZVNuXpY7SdS1Qe7Idhc7AyybNXy6sEEuhjGL-QUAkXuIYPNLLBegLDbw3t62xKhs91u3CHYmmhGC_2UAFFfD61tRT7VEa7fpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ایشون هم یه مدل اسپانیایی هستن که دیشب روقهرمانیPSGمبلغ 3 میلیون‌دلار شرط بسته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22539" target="_blank">📅 16:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22538">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇮🇹
برترین گل‌های فصل سوبوسلای در لیورپول؛ دومینیک سوبوسلای مجاری از باشگاه میلان نیز آفر رسمی دریافت کرده و احتمال این انتقال بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22538" target="_blank">📅 16:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22537">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3p1tolloXvkCeRV5gj3GCxJjygi2uZsDi2H_abu3t-2WZba21ZQ1qQRKHXV-FjMTzNR320WEt_OQbireYGGXbJ_HCdqu4JxfmmazMjcItkKyEz7f6tTfq3NzRj1GN_R4AcutsAvU4mdgv2buy4XxPAVF2lT1TBAZR1qL7h_zE7sbSOLHuWRIq6wBcop6q3Sg7-fC3r4hHNwJE9AAqdGY3EMkIis2nqGcNR3vdWiYc73MR5gnjfnhoHqFIb_tXBEmFyeWdOzbxpzPgXEOHfOklk-2mfJYKr_TE6m_37uVuGDLIwBJ4bU79AKiuLbcIwQlqTCB95ujZHgOys_JBiUXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
یه احتمال فوق‌العاده جذاب؛ اگه پرتغال و آرژانتین در گروه‌ های خود بعنوان صدرنشین صعود کنند و درمراحل حذف بالا بیان در یک چهارم نهایی بهم میخورند و یک جنگ تمام عیار بین یاران کریس رونالدو - لیونل مسی خواهیم‌دید. تقابلی تاریخی که شاید اخرین تقابل این دو…</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22537" target="_blank">📅 15:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22536">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWYgEvPaRaYN9cg-KkrUfxmBiA3RduYfO1cmHV9Cfi0J2Yi0ac8mJ_Yen3UAR5YbZ24MUlG5aY1WsFFlxznQ4wNRDdMs2yZrb1BxBVy3uPnvqS14YVznq_8kxK2Rd-uyGACuakeTKn09mCRWZKmNH6RrZp1JB4bbjVqQ52ATnm1TXeP5fxaArCiImewG8ozLqKQmjXTp-mqBpnp9sIIDe6bhgeIv1UF2zuK6zKdW0OsR2wwPd5_RAX0dsyNVUPhCZ6qe_3sdWK-35jx3-MUkSTJeiMMLkk4-fRmP6jWoBLJibsSIQC-s7aaPl0FNhLRF_PWOBDuI3zurEZL4YD49Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ علی تاجرنیا صحبت هایی با وکیل علیرضا بیرانوند انجام داده تا درصورتیکه پنجره آبی‌ها در تابستان باز شود بیرو پس‌از کش و قوس های فراوان آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22536" target="_blank">📅 15:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22535">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHiTh-MGc_oWmi2DezjVRtlLrdufwhIgvWRZiDwS0ejr-5N0kybXDTwkKJl4is3nfCUyopW4hZHFLCm1kLsLL9QuoRvJYuaSPe6WvVTZY27Lk8Y8b-oMKD0v-glslp8LIEXdg5rLNPukfBY0QJEl4oOL7t-QFQQEr8pxKHVeEW6Od9ZOU8onC1DBTRXuaNLga1Yi4NDeRUYayouvhUXUs4BIdTBjcRElhohjdWHuDmqAvqCscmBBIuo0i_axvS4YwXYTOFKsQygs3-u7bhEKw4_mnfLltbI74esFTMU-1PZC0XWrkCDHY4Cte9PgLZaZOFY7ZWGJ55wsL75M99z5Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اکیپ فرانسه: باشگاه رئال مادرید مذاکرات اولیه‌خود را بانماینده مایکل اولیسه وینگر راست فرانسوی بایرن مونیخ آغاز کرده. سران رئال میخوان اولیسه رو در این تابستون جذب کنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22535" target="_blank">📅 14:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22534">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHNRtZNpJBRsBhHAyMAu719vdm-wkr0B2iW9TrJtsONeJps5OBy1LhpUIltZLlOCrvdIeCK4Ghrjxhsa-b_bgKSZNentuVaF43IWgalH43IgbVru5u29nLu-UE4FxNtBbiu0z1jEXRKNLYTIR5sZ3mUya8uEGYr2CQMVjfVu7qQsSoYrTwahcOsIon8af3FA9KETs4nHXjzxHZWYEx9IZyzYcNJVZi5tBwad4rGAQKpKjpIHQqMifLoudtS9HQDN9UdZourMKclaYECfL1wTskXRzJ3oTXSSrg54bZSz_liW_2s15-AkIHCCj4rSTSf1u4XiPGh2iYo5YkDZVJQTqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22534" target="_blank">📅 14:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22533">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇫🇷
عاشقانه‌های‌بازیکنان‌باشگاه پاری‌سن‌ژرمن با زن و بچه هاشون بعد فینال شب گذشته و قهرمانی UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22533" target="_blank">📅 13:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22532">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSDCYvgb_7G5YIV56Pm3EFoyptQ1Bil_MmdASisyDIAVuULpHMpqhdyyDcfdIyyBnXWT4JQsmz2oTJ7J6V2JB3JxkbMtfTrFM_7GuXkv_MrsCte3bquODD2NbMNstAxSksvEKcN-zKlolgjFdIglDvJ-ZHAGheYFZpasM7E_rXifZKQDaI111XiOzJTVbAqYI-aynTUFIlO3XanZEUwAMhhlN1MtION1f13k6gKIckzdfbZWClPS2hr5OyGcvB9yl9M8pRAUUfhmgHhd-X4oZIW_VcILLV7P6eGtHvxHHGjwUp-pZMflbOxF5Ioicc8rihVGpaQ7V1LdkfkOravL0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرنوشت عجیب امباپه در UCL: سه فصل آفر رئال مادرید رو رد کرد همون سه فصل رئال قهرمان چمپیونزلیگ شد. بعدش این دو فصله که اومده رئال مادرید که PSG تیمش سابق داره پیاپی قهرمان این رقابت‌ها میشه. دمبله هم تو قهرمانی دبل کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22532" target="_blank">📅 13:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22531">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">▶️
تعدادی از آیکونیک‌ترین و فوق‌العاده‌ترین گل‌های والی که قبلش هم توپ رد با سینه کنترل کردن.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22531" target="_blank">📅 13:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22530">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMftY-evrxQcCjOEnjtzYqQHIrB9sa7AuSfZVcFlfTnkBrlrQE76WlIeP0l_K1gycpn3g4UKjheHwbhGcRCNiMNPLtGEVXSq0WqhGIJdRG1ipXGJueY0pfNpfFq7xGV1TrCITmShraNzaSSPmDmaLUFPvzebyZP8Ymh-u8uT3nZMzbvq0JlSauaFtKWZvtlHJm0er2slOAAHApt4mxT6p1uMBWcmxjhychSzkAcG-AgAlql7BmeWqVyJlJNt-c1WXvArvPZ9td_LMOKGbqVd-RrdchBTzdmF6-40QzZEgYjr9UeSpOFg-Nb7fWHvLRlQBIFID7JkNdigkW9UOHJqPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇵🇹
#نقل‌وانتقالات|رافائل لیائو به شکل رسمی اعلام‌کرد که‌دراین‌تابستون‌رسما از میلان جدا خواهد شد. مقصد بعدی ستاره تیم ملی پرتغالی یکی از تیم های لیگ برتر انگلیسه. منچستریونایتد اولویت اوله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22530" target="_blank">📅 13:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22529">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHSw7lPouEJbKgJsGEoRgvurt9sSJbp0nsNMYTxamXq7Mug7vOAZ7Zqulc0FBVruBesKk-OuBMI57IgcGvC_WgmoDdI1Yl8GZ7RmuMaTdYslj6kkfxR0-bK1MV72-dTSjb0BEtu_WJxYq9Y2ppADzmnEtTnmjlGjnt2EUklQRp6LuQyV4dfEeWBm-eiHxePA7mUWod3QRgMeHechCFTAOuoIJ7w9fMnMXwA5aJHc3jOO8msYTUTVocQnt6O6Df36PbuDHZ3r0-oyUMafW9zuUcaXqSeR-USU00heWgaRhBUf-8KIxKymhE8jGvaT0Qn273aSLpsNevftf0PBQ-Hr5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو آموزشی‌نحوه‌واردکردن‌فرکانس جدید بصورت دستی در رسیورماهواریاهست؛ شبکه‌های یاهست که بالا معرفی کردیم همشون تاپ ترین هستن که بازیارو باگزارش‌فارسی، کیفیت فوق العاده، بدون سانسور و تبلیغات‌آزاد دهنده و جلوترازصداوسیماپخش میکنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22529" target="_blank">📅 12:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22528">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aH2qEzUjexyiK_4fM3lwrftMo5hbWYhbwIsmIrZ0Ei5JCkgaWH60AwjrppjhcPAhPMEHLSAy7mDSEsMz394FLE28pXJCusj3tWQFgSVYwhqJvrIDa9GVVug5ZWiEbcMHqLYEGh3QxosxpHYes5qYFIFc38P-A2CqvskBCG3j0n9MjYb0v1YlADtL5uO2TfsF1DL4MepxVAf28iFFyzsbjrGTgs0TxxawottSnbDKTXOg7dqy_nVa7-6shmuUs698Cx5nvO83QjnHv3rqvf56vGjmLNUHwMs4KjZuqNMv7nJg1fJUHToTj-knoWRtUtPClCsu7ssY4KB0I3c4ZMXyrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخرین‌اخبار منتشر شده؛ باشگاه بارسا طی ساعات آینده پیشنهاد برگ ریزون 135 میلیون یورو برای جذب خولیان آلوارز به اتلتیکو ارائه خواهد کرد و این بار این باشگاه با این آفر موافقت خواهد کرد و این انتقال رسما انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22528" target="_blank">📅 12:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22527">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/460d6cadb7.mp4?token=UWyhBUW6v7LFTQCcZBPvvnWhn-4R99FuW-axbNj_DVKWTzus9I79f9ALWBGOHf4tJvGNgmHMLqNyUbHkWfJqxnQsRmufOPY26mNZ-hj6pgePPuht7uMjlJO9s9eBdDtW3OxCsG1gQlcuPbhma41lnD-QKTsyr1N4zUbXNp4eeOSze9sT8XRonzS0AHd91-CeYiQHanAXbDzZjHXz3QlP0Hr9D23d_56V5fSjOXmPWn6st_AyOrXvyJf3p2JXvPN7iPInXg0iInX0IMxQiNBKyIHb32v2fCstZ2fHhH2IWV1XanJpckhAwpVRMQ8fTID1pEvLzwRw4PVfEJ6EgrKCKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/460d6cadb7.mp4?token=UWyhBUW6v7LFTQCcZBPvvnWhn-4R99FuW-axbNj_DVKWTzus9I79f9ALWBGOHf4tJvGNgmHMLqNyUbHkWfJqxnQsRmufOPY26mNZ-hj6pgePPuht7uMjlJO9s9eBdDtW3OxCsG1gQlcuPbhma41lnD-QKTsyr1N4zUbXNp4eeOSze9sT8XRonzS0AHd91-CeYiQHanAXbDzZjHXz3QlP0Hr9D23d_56V5fSjOXmPWn6st_AyOrXvyJf3p2JXvPN7iPInXg0iInX0IMxQiNBKyIHb32v2fCstZ2fHhH2IWV1XanJpckhAwpVRMQ8fTID1pEvLzwRw4PVfEJ6EgrKCKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی بااعتماد به نفس کامل به کراشت گفتی بیاد ورزشگاه بازیتو ببینه که تحت تاثیر قرارش بدی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22527" target="_blank">📅 12:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22526">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfySGL35fOKmqv3ndf5HPUiuLe8YrcC_Y9P6sSPurYx0vCCKdAkfCZjhmIl0GrdmDJiKI0M9YWA5oBg7PJOrlKPS4gWNb2ixEpm2HlGmAPNvz8qznoKYNBOnjr9riPhmOosF6bRqfYOhG0EsrsMymzg5CiNDka4xK3LjPPCX4qAbytDuROec0Fl2Yx0LagTr9SdRibFXgIO02ZvUZQ_eSeE3XPcLP4zNQRfoCem9Agv6tOnB32ZFSfqFABjGQAubDe-ueeMhTAVdKT6mHEldxM8hbAa8WLCdj8rFIgqBUwP7SY6mG6Vv2ERi9yI4hTFe5fb_rWXwTZBHs9MxSXnE-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ به احتمال فراوان فصل اینده رقابت‌های لیگ برتر 18 تیمی خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22526" target="_blank">📅 12:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22525">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55166b2d48.mp4?token=N6fvGFJUlUTQn_UwvGva0tkOMiehKTLAzC6GZdISvEObP4S8RfYPWXDkhQIawGgelKHKeKBISfim0fakkmczd6XmO-u24vwZbv35xS_K0Ax8ebKh1AEXlEN-tLIn04uj1l8BmsxszT4a80nA5pguVyE_gaYci5yWZ09WjeD7IDZ_hEfKMIpwqF4TBn6IPHDErSQZdqWZtrfhFGv8E8_7ra1nuYzgJy-8fXHkS6Qf0Q80JqYlHntGsDk0e_lnM0Tvg7kzXuq5PQPlg62Qviv-HydfXysYTMCXTd-SHILzHEUL5nHOz2gqThFg2Nn9AmDm35L8QsRq2Z_Z5FplcK4Hqx5DlK_apLoY0cvip3lrOezYErLuz6r13n8cTvNP45sdAC6zyaph78gseAh_SK_xOTRNWLOPSImzjwI0Xm2iPeNsjc8LPxNGieuacKQsvuxKY8RjtvrxxIjS1Ns_eA2PAmoao5iYga1ge0hISS2Eix0suNFe9W78V9PTrTF0Shmv1k5q5v5T8XS4lQNLvzVecQr7m9Q6lzLlFdP90gry09t6kDfiE_CqKhn0tZ9ZchY-KfnouWzdwXDgBqEn61JIiH4i6Nu1ZOMXQu3yiTTxSmTgXPat2q2FXdZ0fJ6ZcRpaKlNAm9QUkqbyGN1Y4eWxMRLnHyrq9XjDu3zSdl-DdPk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55166b2d48.mp4?token=N6fvGFJUlUTQn_UwvGva0tkOMiehKTLAzC6GZdISvEObP4S8RfYPWXDkhQIawGgelKHKeKBISfim0fakkmczd6XmO-u24vwZbv35xS_K0Ax8ebKh1AEXlEN-tLIn04uj1l8BmsxszT4a80nA5pguVyE_gaYci5yWZ09WjeD7IDZ_hEfKMIpwqF4TBn6IPHDErSQZdqWZtrfhFGv8E8_7ra1nuYzgJy-8fXHkS6Qf0Q80JqYlHntGsDk0e_lnM0Tvg7kzXuq5PQPlg62Qviv-HydfXysYTMCXTd-SHILzHEUL5nHOz2gqThFg2Nn9AmDm35L8QsRq2Z_Z5FplcK4Hqx5DlK_apLoY0cvip3lrOezYErLuz6r13n8cTvNP45sdAC6zyaph78gseAh_SK_xOTRNWLOPSImzjwI0Xm2iPeNsjc8LPxNGieuacKQsvuxKY8RjtvrxxIjS1Ns_eA2PAmoao5iYga1ge0hISS2Eix0suNFe9W78V9PTrTF0Shmv1k5q5v5T8XS4lQNLvzVecQr7m9Q6lzLlFdP90gry09t6kDfiE_CqKhn0tZ9ZchY-KfnouWzdwXDgBqEn61JIiH4i6Nu1ZOMXQu3yiTTxSmTgXPat2q2FXdZ0fJ6ZcRpaKlNAm9QUkqbyGN1Y4eWxMRLnHyrq9XjDu3zSdl-DdPk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لحظه پنالتی آخر آرسنال و قهرمانی پاری سن ژرمن در فینال لیگ قهرمانان با گزارش جذاب فرشاد محمدی مرام که یکی‌از آرسنالی‌های دو آتیشه هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22525" target="_blank">📅 11:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22524">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91b2ba8656.mp4?token=HAVzJGfzIskYzjnmeGZhsstIE9q6Bp8pvhKbWC2oZB9aPuxsrlGCF4kyoO32b53RcsasnXkgWn7wF4_v0JyhvcRSjOQlclt0OFkubycsSQuWOVwRQlFFLyQ1tDjbpStBAygTBbE648yjZTLpreIpf9s4RemBF2fXPOeZLU20V9JFo2spqzMXU3KjKIGB-JED0NiKaBw6v_kf6AeSFEkU-tCXj_dDXCRmcIdwuARiIMjA5G7RPu5-LXwuHZWMCBjTSX8u8eh2aEEmsVtp_xvXhPZqAVO36pbxw1KjPakciWunGo2ZKY6si7020M_MrfDhajbm-Qr2ZGZ5t-FiQ-hgJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91b2ba8656.mp4?token=HAVzJGfzIskYzjnmeGZhsstIE9q6Bp8pvhKbWC2oZB9aPuxsrlGCF4kyoO32b53RcsasnXkgWn7wF4_v0JyhvcRSjOQlclt0OFkubycsSQuWOVwRQlFFLyQ1tDjbpStBAygTBbE648yjZTLpreIpf9s4RemBF2fXPOeZLU20V9JFo2spqzMXU3KjKIGB-JED0NiKaBw6v_kf6AeSFEkU-tCXj_dDXCRmcIdwuARiIMjA5G7RPu5-LXwuHZWMCBjTSX8u8eh2aEEmsVtp_xvXhPZqAVO36pbxw1KjPakciWunGo2ZKY6si7020M_MrfDhajbm-Qr2ZGZ5t-FiQ-hgJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
واکنش عجیب ایوان تونی بازیکن تیم الاهلی به قیچی برگردون کریس رونالدو ستاره النصر
😳
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22524" target="_blank">📅 11:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22523">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JE_mh5yAetevXMcib51dIdTzBy13NwXvRWiVBNLdGUuvivWNRra_oQN3kXPMHV20wzkbbudTcaQHTuDhkF2vVoPXkp6KDZIHeIVfjlX5e0dOZg1ipOy2UO9267g6Wkh1bd_H0OmIf1y6sHL-T_GdXWlUAhhs6AEFNzXvWrF1yNRzarel1BLVgNfiCdW_M_DINA3lw8_vaqj0AvA-gv_o3Nll4uG_wVqhOWMj68tg9x6bzZ98_BOTGnsTVkH6zB-xRziFGLtS8cG04OIxm_ySAMplfm2ezN1H9WJQc1_AQkW8W6O092hvuh6dVzW7NdpA5SPLXzD_jpQJonOPibz6FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ مدیر برنامه های الهیار صیادمنش مهاجم24ساله سابق تیم فنرباغچه و هال‌سیتی درگفتگویی‌کوتاه بارسانه پرشیانا اعلام کرد اولویت این بازیکن برای فصل آینده حضور در فوتبال اروپاست اما اگر تصمیم‌به‌بازگشت به لیگ برتر داشته باشد اولویت او باشگاه…</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22523" target="_blank">📅 10:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22522">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1346d9dda7.mp4?token=e2CAPg3Mk0BCZw2tYMVyEI-wAjQv4My3mlAIOjKVrWYaXcyG-218BMDMIdzk2V4py570V4gDcD3bQIYfxXfhPnZKHOEZR-WMvuGW8jxAavFvwq_l5bN0LeSiIXUGRumsN_Gr0XTscfcqBof192A0YBNm1LNMU3Q6T8pm60hA85lAkhIF2zli2b7VK2v0d7kOBCI4jvYRHq_SPxcN8cH7AyiwhnoTMMlPW53GvqYG2xQApaGoqVWJhN_vPjMS9z5yjSKo43xfnLCeSs8C8k_yIkWqpFQHEHubS4S9GstQvh1ENQcBOPHodRTtM8Kg90Mxea4xvT8RZt0EsU9q72taMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1346d9dda7.mp4?token=e2CAPg3Mk0BCZw2tYMVyEI-wAjQv4My3mlAIOjKVrWYaXcyG-218BMDMIdzk2V4py570V4gDcD3bQIYfxXfhPnZKHOEZR-WMvuGW8jxAavFvwq_l5bN0LeSiIXUGRumsN_Gr0XTscfcqBof192A0YBNm1LNMU3Q6T8pm60hA85lAkhIF2zli2b7VK2v0d7kOBCI4jvYRHq_SPxcN8cH7AyiwhnoTMMlPW53GvqYG2xQApaGoqVWJhN_vPjMS9z5yjSKo43xfnLCeSs8C8k_yIkWqpFQHEHubS4S9GstQvh1ENQcBOPHodRTtM8Kg90Mxea4xvT8RZt0EsU9q72taMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ژوزه مورینیو سرمربی‌ سابق چلسی:
ابراموویچ مالک چلسی به من‌گفت‌که برای مهاجم کی رو در نظر داری؟ منم بهش گفتم دیدیه دروگبا؛ گفت اون کیه؟ کجاست؟ گفتم شما فقط پول بده و حرف نزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22522" target="_blank">📅 10:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22521">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c743e5df08.mp4?token=swYLcRc1az0a4_6YF672h6MAsQp6yMy1_7unWq16zYWdP7MAKh_zPj93xZnVzmHs4yZq9cZeG0bcGMztKF6y18n5MOmadFYsvR3qIM-vCE1t536jDHqJw2r6o2j0DjYkZCI9Bzm8_cpsEtkloMY6QUU8_zNplKAIuBT3zUc39wYsBYNOn-DKVtVsSeYmrl-BDiMNDwmqLOOG53Z9z0hY6J_U7KNzgyZqx5SxgZgXBsvozaO16_f6kMqevZietSS8YYDJ-hLVICO_XqDQlkuhp0el0ZOreNY26KmiSRn5TP0Fz0Nwk77O8UcDn5gC6196GldyMDe_3XO4tDoN-1pGxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c743e5df08.mp4?token=swYLcRc1az0a4_6YF672h6MAsQp6yMy1_7unWq16zYWdP7MAKh_zPj93xZnVzmHs4yZq9cZeG0bcGMztKF6y18n5MOmadFYsvR3qIM-vCE1t536jDHqJw2r6o2j0DjYkZCI9Bzm8_cpsEtkloMY6QUU8_zNplKAIuBT3zUc39wYsBYNOn-DKVtVsSeYmrl-BDiMNDwmqLOOG53Z9z0hY6J_U7KNzgyZqx5SxgZgXBsvozaO16_f6kMqevZietSS8YYDJ-hLVICO_XqDQlkuhp0el0ZOreNY26KmiSRn5TP0Fz0Nwk77O8UcDn5gC6196GldyMDe_3XO4tDoN-1pGxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یجوری هم متعجب شد از اخراج شدنش که فکر کردم یه خطای ساده انجام داده!!! دِ اخه مرد حسابی زمین فوتبال رو با رینگ بوکس اشتباه گرفتی
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22521" target="_blank">📅 10:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22520">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b417aa36e.mp4?token=QGeAuTLLq7khV32ifATVK0F99Kyb98NSFnGBDqwWUMWvFEFZDn48KXESFBiPhW9HX_f1TXD2Y3Ix6hhqKnSCPY9iXuMWL39SZDOYgMTb5zSssFSXr8OkVp8ylljd_zAoOm461Bi9SIXMO1TqWLEESkYB_JKS5kHUCa55lN3XFMTEh-x75ljmuUzI0b1iOgiNzP-Naj9KSaFQJcFgDXdgoD357LXdlJejH9z_1xqy8B-l8iLiVIgVe-HqAxQo7e1gf3YI5pRLYitw9AmXT3pE2TaEvkx8oFJDL6UFxPejKeJx2TPQGtvUCYiSB97PNvEfSUeCYF9i93xhU39Jk5L2nJ6lHGFDEJcvqNYa0wt0yJzfDSHAxLuOPOlFAxYLYtYsC_J_smSRdeMU77iqiGA4DIKnh4OQkJA8OgkLM2ee-1VrvozqRu1WJKjHvVL4ERuuSjAeW1f9rev9rb1BPCcG6-3LYLfmddJNqWIHnRhT2egQzfkmx-_hFcmoFVf8_lPoEsnd6Zr1K4ig6qPquG1XX-KQSvgQa7TgL47ZdfcV3q660J8PTtLhKh10zO_KZLpndNu0gn7J_2HSzuCHJ6DmZJqqfojQwJ5_mVnws6qP28aKw8smn02AMwi6yCs0829e592jRBQnRqK2lFJIYSSRtC-41VHrmX8dg6lGbblW4Lo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b417aa36e.mp4?token=QGeAuTLLq7khV32ifATVK0F99Kyb98NSFnGBDqwWUMWvFEFZDn48KXESFBiPhW9HX_f1TXD2Y3Ix6hhqKnSCPY9iXuMWL39SZDOYgMTb5zSssFSXr8OkVp8ylljd_zAoOm461Bi9SIXMO1TqWLEESkYB_JKS5kHUCa55lN3XFMTEh-x75ljmuUzI0b1iOgiNzP-Naj9KSaFQJcFgDXdgoD357LXdlJejH9z_1xqy8B-l8iLiVIgVe-HqAxQo7e1gf3YI5pRLYitw9AmXT3pE2TaEvkx8oFJDL6UFxPejKeJx2TPQGtvUCYiSB97PNvEfSUeCYF9i93xhU39Jk5L2nJ6lHGFDEJcvqNYa0wt0yJzfDSHAxLuOPOlFAxYLYtYsC_J_smSRdeMU77iqiGA4DIKnh4OQkJA8OgkLM2ee-1VrvozqRu1WJKjHvVL4ERuuSjAeW1f9rev9rb1BPCcG6-3LYLfmddJNqWIHnRhT2egQzfkmx-_hFcmoFVf8_lPoEsnd6Zr1K4ig6qPquG1XX-KQSvgQa7TgL47ZdfcV3q660J8PTtLhKh10zO_KZLpndNu0gn7J_2HSzuCHJ6DmZJqqfojQwJ5_mVnws6qP28aKw8smn02AMwi6yCs0829e592jRBQnRqK2lFJIYSSRtC-41VHrmX8dg6lGbblW4Lo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
کدبیس سه‌شبکه‌جذاب ماهواره‌ یاهست که بعد بالااومدن نیاز به‌واردکردن‌کدبیس دارند. اولش دکمه F1 میزنید بعدپشت‌بندش‌سه تا 3 بعدش یه صفحه میاد که باید کدبیس رو وارد کنی:  کدبیس شبکه جام جهانی HD:  BISS:2585AB552585CD77  کدبیس شبکه ورزش تاجیک HD: BISS:03A01BBE20C16D4E…</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22520" target="_blank">📅 10:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22519">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baebe6400d.mp4?token=FkzsEPJmIxwtO72NHZC8sPp-nPF9rjZW0gud1wik6L6Gs-4TlSpFh1pyw6l3lIy1egmIUC0qxU9Oe5taKGNW7hrnRGOOXTRV4bzzUIl_y2VoUOkb0XusLGdW3AlJ7YyZhMXn9SVRkCCLO3CRVNmh2yrhZtsXqZwYmuH3S1DKIitHdBd0JlcAbnYEDGyPgXc8XOMbty_UdWM-Qm-38HIlSxjeLEVahSmPI2Dq0UYJGk-T3FJVFVE50aA08Nfr7uY7g2IgsGawX8_5vHUA4iKodSlebAnt81vlm4D4mQ5ZxLktx-iV4R02nqxQ4EBZDEVPb9_aRNrr4obwabbwafSiCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baebe6400d.mp4?token=FkzsEPJmIxwtO72NHZC8sPp-nPF9rjZW0gud1wik6L6Gs-4TlSpFh1pyw6l3lIy1egmIUC0qxU9Oe5taKGNW7hrnRGOOXTRV4bzzUIl_y2VoUOkb0XusLGdW3AlJ7YyZhMXn9SVRkCCLO3CRVNmh2yrhZtsXqZwYmuH3S1DKIitHdBd0JlcAbnYEDGyPgXc8XOMbty_UdWM-Qm-38HIlSxjeLEVahSmPI2Dq0UYJGk-T3FJVFVE50aA08Nfr7uY7g2IgsGawX8_5vHUA4iKodSlebAnt81vlm4D4mQ5ZxLktx-iV4R02nqxQ4EBZDEVPb9_aRNrr4obwabbwafSiCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ویتینیا: اونا تا میتونستن وقت تلفی کردن، اما در همچین بازی‌هایی بایدصبورباشی؛
ویتینیا علاوه برکسب‌جایزه بهترین بازیکن فینال یه‌آمار فوق‌العاده هم ثبت کرد؛ هافبک پرتغالی، در فینال لیگ قهرمانان اروپا مقابل آرسنال باثبت ۱۴۱ پاس صحیح، با رکورد تاریخی ژاوی درسال ۲۰۱۱ مقابل‌منچستریونایتد برای بیشترین تعداد پاس‌صحیح دریک‌بازی فینال از زمان شروع ثبت‌دقیق‌داده‌ها درفصل ۲۰۰۳/۰۴ برابری کرد؛ او همچنین باثبت مجموع ۱,۵۸۹ پاس صحیح در این فصل‌از رقابت‌ها و تعداد پاس‌های‌بالای ۱۰۰ در ۹ بازی مختلف، به‌تنها بازیکنی در کنار ژاوی تبدیل شد که به چنین دستاورد بی‌نظیری دست یافته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22519" target="_blank">📅 10:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22517">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZhyt0rvwYQMI3u99NzNPeexzDKmAXWVrLaBNS4PvdJRWGwGjF34a5Hr2EKOBDDftfHcpBxJDcTk0c54ze3DhFMvwxyibT4BYprghALvcs6cDAz-2-Wvod81DcDMWaRrAsLpWqCCAeh31kknF8VnQIlMWS4nVhewWMv52wW2Aga0jbEQ6ECBwe1W4S71I1b5TWjUNy2sNhquXiZWkm1Bp4v03SceNI3tOd1RNJOmAi8nCW_ADDqctt9y69nez0RFAOcm15JaaFuuiBVKBC7GLas6nRPuYWzvLhjglxWvZ2YwvwlovRrYQqzb9czrw1WcyT9W-O9Y5OX3X3vUKxHzMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با بازگشت نیمار جونیور به تیم ملی برزیل برای جام جهانی؛ وینیسیوس جونیور شماره 10 این تیم رو به نیمار برگردوند و خودش شماره 7 پوشید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/22517" target="_blank">📅 09:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22516">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjjVu5d2EAYyF455izJ_n30xQ_T9bm8KrP9Bis0OplmDcWh4bYz7zaQ3_nrS2XK6Ya5n88PzrXYKbWw1Enle-vZQXjLsSKS0fmFu9visNxK7PoIyrm5UPvt_89Jaqz9Qw9bgba-S1sJTrQb9u9GZhIYLOv0yRHYMEihVdfwi5q71t3MPCwxpPffG5ZZ3jPErJP4_r2naVOeaNqMAurOCHA5ZGgNAlmP9-RNcv-iirbT0fPU1KoOba7q_GITmZFFIIldNOdImv3NYZW35KA5qAQJdzDVs46bwalUPCyUO0P29PvLgUk9iLH46yxPMfMGXEHfH464ePznJyjGq3eiOXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|گاتزتا:سران‌باشگاه منچستر یونایتد مذاکرات‌رسمی‌خود رابرای جذب رافائل لیائو ستاره پرتغالی‌آث‌میلان‌آغاز کرده‌اند و قصد دارند این بازیکن روبعداز جام جهانی 2026 به خدمت بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22516" target="_blank">📅 09:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22515">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivdAArTKV30hXmXQj5XqP6VSiYtPT7V4mt8MKq65AQwHXMDRCJ0TvHy_5pucqYBIa1sjQsV21pUsCugq4oanmB6RxldNe6nL7brvVV6Ym5O5Wuv3ZIIp01pmJU8vreZDa5dH-KMjYKJH-zWnEihIoo8xlPy5zM9cdDplOd5f9E4iMdURrLqTJEIsudM0BAYpA1a16ULqyM-GngoOAJiRbYbYne6qNlHrw4sj1vSiulo0i8uEo7c2MrDXrU4laBfJzzzNMNmt0YcjM642cZHreyJ5HerkzoxWT51sxA7YEXx3h4Q-4ho4qJxSxSrnI7j4aaOp6acdiICKTo0HY7woxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛ برناردو سیلوا ستاره سابق باشگاه منچسترسیتی؛علاوه‌بر بارسا از اتلتیکومادرید نیز آفر دریافت کرده که اعلام کرده اولویتش عقد قرارداد و پیوستن به‌باشگاه بارسلونا است. این انتقال بزودی و به شکل رسمی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22515" target="_blank">📅 09:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22514">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYa_Lvwzamjggx4lWMXWezTQvx3d4vt9nhaugnQPDjqNWvcJgHzs0QQRYF21kzrMFz3B0JqHLNEK5iDj6Zz_IK8mm0B0p60VRLvJSv1PP1FSLh2bKEQ6hYyznO_9-kF2SehLwCZfxnnTUEbmmmcO8tFSIhSnIZ9jzr48_PoaDbHvWcdVrrWNQwaZaF4KJB34gyjMWAvGEMVLmkgyNM04jVGwLz1cvgWXclUKWX-hjJ3XS0aMI2VDQNg2KX62uqG1huQQBuv3hdIIFM9k2f0gc60jihvG9eKYUZ_vxnQJwPeWkt9PgLtV2oosPCIrJ19Xl2SvUuUY25I3FjQudsTBUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👤
مدیربرنامه‌‌های دراگان اسکوچیچ سرمربی سابق‌تراکتور: به‌باشگاه‌تراکتور قول دادیم که امسال اسکوچیچ راهی تیمی از ایران نشود اما اسکوچیچ از ابتدای فصل آینده با یکی از سه باشگاه سپاهان، پرسپولیس یا استقلال قرارداد امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22514" target="_blank">📅 00:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22512">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2CGRyzGhQXFuqkZXZNZ4YuK-_zzDOycYtthSLv6YkH46nDZGo41jlaeDfVIKD8C9iy-Kl2EaCA--ABcSLu_KI1-3MYHRtfgQiBJDRisRb14NCkEOO8i4sYdUIthUdZ9gvLXaRiz1OqXQRk3Op4W9NCNrmCTvg7VLcgm_kTjFUi8scH0SRwhReVj-_8cDIqOktbR4vWSUFxLChIa9Rzu7aZJBHKlD-relBrLVw8IgAK3eQeE4tdEeUTSx82hWrz-yUz8OvXVsZIxKp22FNGO9p8DVHVgSgA2dXld63ImkWf_u_2sFCy9xOh5dyzteK5uNQ2kleRTuCJLoeI4Giny1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌بازی‌های‌مهم‌‌امروز؛
آغاز مسابقات دوستانه ملی پیش از آغاز رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22512" target="_blank">📅 00:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22511">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plMdOYL7JolNI1VOkuo4PljSUXunE0r1HTFG3UYpqqYxhkzIrMry31sH7bnU8cBk9U1GtjcUzWIgeBRBPYYeErCCJPLrWGNA8-Kp0251tq4tzyTDnQdQ0W0o19JuoDRR0wPwNAJTqNZrxODS3fXXJ8M-eEE2RSacvtzPV0khMRfo4Niw0_CHGRi3utxqKHBw5VcVbLSj1wuZoFuvwG0wjEnTIf2bNbvPLkeQb1dkQJFudMKT5TBZkH-0YsPt22u1ePMhlrFO5jKqUXFVsCiW9tw3JRg1vKTta72VOpruKBtkd4m20OHVFA7yyhWW4dipdqjx_oPRrN1H_omCpoj6OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنهادیدارمهم‌دیروز؛
دومین قهرمانی پیاپی شاگردان انریکه در UCL با شکست توپچی‌های لندن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22511" target="_blank">📅 00:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22509">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYTfYzp3kXkQiQGC1dZ2FUP1MdhmokDo5fTh2sSw369DcdPf1H9ovfenH-vOKBxYqbrawtgbinSVHN-L0K1_uf5_cZGVQAnF8GTPutIJitUxUw7Pa8CLTOuAaY-uQ_57LUTjxTe-WkTj-qpR3MsQ5lphXLBPbHhB4TMq93K0VtuFBO9myxHLYJVo-Ou6TMRW5Aq1G2A1wPMeYhGrpDMaQ3c2VdFeoe-_dhuD-5okPUxwX2GygDuKnmuqnQL72ljGxfKf0s7wz44Ra8Q6fdcncb5u1jU6SK41PohWCLL3QOFTk-NoVTPEEYp5PDdG_UiAenGu6Y-ailwnHHjuEdmgAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های دوران سرمربیگری هانسی فلیک‌ و ژوزه مورینیو سرمربیان فصل‌آینده بارسلونا
🆚
رئال
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22509" target="_blank">📅 00:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22508">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MfpLgF_7PX_RonPgeFrwG3j75Y2cmOqMqn2sjLL0ELiP5_EtZBKqNJGkuafyNd-WI3dXHF82A5uvalmWupfQS5Mhec7AUF97Ec07SCBTpPr_BHrVIVxDv60Aq0e28nT2q7-bfGvZy50zyYN_eFbBSoUu0liWa8H2Jg1WsLzPXdasso_6JrafZaakHfpf2dI8FmX-uHzTIVcEB-EzL9HCJBlZqngfPyCkOVFS3k0EqpmOtj3GkDyXiMV8CKH6yum6Qk6ntBR5zd-32cJHDyqr1q-66cK70IC7yIuN8T2gSVqgakIy5VmfCvXRM9K1DJpGQN3FutHC1bRv7p3VYhzE-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس به دلیل سفر افشین پیروانی به آمریکا باسرپرست چندین ساله خود قطع همکاری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22508" target="_blank">📅 00:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22507">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAVvftBgHwQ5PGLWUZrseAHKGdAQOU15b4POKbNRBBTzWlbO8B6fH3MR2VDAxvlvmjRpmOT3omf4a0MyeUeA2M6phTzuL1WxFpkONdWLPxwsx1nc-YdHtULohF40JMafPPmG0lACkcFjCjY-ewEyZj19o7MARo8d9WfZ9rI7BvCncP5jPNvHScZTz-PY4ijWIDvfV0Eewz0qYYT5te8ajLKopKetCqHoon6lOp-A1mxuaf3L5n_jGHyceKir_8RxM3q7lNbZvqDQBTxFuy9stFPqqEfI7pK0ER58DJ7djuu-8TeskGoIbazfVcPh2pNGUX8Zi4GjJWBMu9woD9-HxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
تمامی قهرمانان ادوار مختلف رقابت های لیگ قهرمانان اروپا؛ رئالی‌ها همچنان‌بااختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22507" target="_blank">📅 23:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22506">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYrBLnxCPE0ykGX3c3vbgiil1iaFftR59YCKxXzHIboyN6Qj80Ub0z_bRr50NEKwGPNLGIRE057aZzIuEgv9Zuk3VgSPmvO9G2UDPTjPjOu1qWNRICdHVcCzAfvfcybnLEybrNdoeMfb8hn3v-RhSrlpkLvHkha0UAkn_NIS_Rgpsqo3Z_jy-vwnq-VR7MpLw2UMzhsfKobs87QdMm4ghog-7yp8yArr9T-rvRwDB0NyV36b_4XAOp74uiyyNkRvNEAfooOtDYvvdrERN2pH9YYY6FOnLo5F-Wj0BoIaB_bMCmiF52EPAvOxXmqaCUEhv2wAf2AZEOku7VexSYT6Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیوکامل‌ضربات‌پنالتی دیدار حساس امشب دو تیم آرسنال
🆚
پاری‌سن ژرمن در فینال چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22506" target="_blank">📅 23:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22505">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78d5a3b7a3.mp4?token=kfsYzpDXpo7rPOUXMdvwRP8diEvJ9N-g7LuaOKMa-VrzniHIXpT9SQo7O-NR8coig-8RNAoEmrcGplSmfFD1OrEl7zM6xE5A4sZktcqlBearcrMbdbjBEa0FmbJKdXPyC4O3Jytz9Wi2MAlZPYr_D4x4ShYmNdgLBJ0rBcL9MPjIsWrZtCCTdF3r_Uzk_1QT7CZ9-loIzY7KpbPhnPRAF-nW8luRLA_k-ab3kl9bFRg2eZcAV4c_JnEaLLQqqpzGRAcMTxLNwhxPTyxwqcT7OmigGo0AUKOLULARSW6hm4U5HhqiMdTjfYsx2hSzXo7MJZ7_N-icIhqVbwYzCBapIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78d5a3b7a3.mp4?token=kfsYzpDXpo7rPOUXMdvwRP8diEvJ9N-g7LuaOKMa-VrzniHIXpT9SQo7O-NR8coig-8RNAoEmrcGplSmfFD1OrEl7zM6xE5A4sZktcqlBearcrMbdbjBEa0FmbJKdXPyC4O3Jytz9Wi2MAlZPYr_D4x4ShYmNdgLBJ0rBcL9MPjIsWrZtCCTdF3r_Uzk_1QT7CZ9-loIzY7KpbPhnPRAF-nW8luRLA_k-ab3kl9bFRg2eZcAV4c_JnEaLLQqqpzGRAcMTxLNwhxPTyxwqcT7OmigGo0AUKOLULARSW6hm4U5HhqiMdTjfYsx2hSzXo7MJZ7_N-icIhqVbwYzCBapIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اینم‌نسخه‌اصلی صحبت‌های امشب عادل فردوسی پور برای دوستانی که قصد استوری کردنش رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22505" target="_blank">📅 23:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22504">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52a1e84d8c.mp4?token=DrEXfRR7xHtreHHc02GROdbPg8QFFwlltbO3P37rb1OAHFLX6mMdAahX_0CsICuKU6TPGYqLZh4qIvHCFSiPQunzuYADhpUIdan14t3qDz1dHfK5G_2DA9SxUXThafkrWElKNtI_04m--OdpmAzEt7EMpdvRgZPfw0lqx1kLtX-y7htwc-tqSsNkFU5O-Al779DChhyiw8pu802qPjeol-RqHHY1pHjfYWRH4GsJu6fpeuMDREaY45-U6OE4TPUQJYJ2w5s5vMnnurOXOb9RLxkWyY4uvz2DnjW3eZhk65olK5fSeycaUM9AGahFCuQc8jQCeEQF94JSlynRBwOKbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52a1e84d8c.mp4?token=DrEXfRR7xHtreHHc02GROdbPg8QFFwlltbO3P37rb1OAHFLX6mMdAahX_0CsICuKU6TPGYqLZh4qIvHCFSiPQunzuYADhpUIdan14t3qDz1dHfK5G_2DA9SxUXThafkrWElKNtI_04m--OdpmAzEt7EMpdvRgZPfw0lqx1kLtX-y7htwc-tqSsNkFU5O-Al779DChhyiw8pu802qPjeol-RqHHY1pHjfYWRH4GsJu6fpeuMDREaY45-U6OE4TPUQJYJ2w5s5vMnnurOXOb9RLxkWyY4uvz2DnjW3eZhk65olK5fSeycaUM9AGahFCuQc8jQCeEQF94JSlynRBwOKbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👤
صحبت‌‌های فوق العاده ارزشمند و گران‌ بهای عادل خان فردوسی‌پور درشروع‌مسابقه امشب فینال چمپیونزلیگ و تسلیت به خانواده‌های داغدار دی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22504" target="_blank">📅 23:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22503">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qT_42ujXnHp2k_LipTlWJoxMCAEcgm1ogomDpMTqtoTK9Q19jf5wMTuDAJIZPWopECtH8aOgHg7pE_CkIHWWrQfaEcg-xcusZkfPSh0n_IJwNrFAe_DsPi139Bfkh2VAQC-p6ZWseS-f9__QsVHs68Jp-76FlrhNH9K_Ry3QbsqdYQ3FmI7lsNM6CYvJZSRCsZ08Xq06NYS1NaOgXBnLAkiXLZv4R2tML0oyo0GLj5S6hN-i6MDgAE3OjqO50svXTNA88aayCVc6OPiRgxZWbS7R58vHIZ37UyY-TVVfDcKLMeiGUZvuI3v2e9wU5boOmD5h8KnjSiKAvofpZhvwLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لحظه حک شدن نام باشگاه پاری‌ سن‌ ژرمن روی جام قهرمانی فصل 26-2025 لیگ قهرمانان اروپا؛ این دومین قهرمانی UCL در تاریخ PSG بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22503" target="_blank">📅 22:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22502">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d915ebc4d.mp4?token=rtyhrSZjgBAkv7xIhceTi9CDmpppGvyFnqi7P_cNMREtY_VdIPTdOnqogNVNVUuDdY2a_9R41cBClConvYTAiF6VRO5-un7Z_jpWx-j7n0sSWvdgx1pPGpdOJ8EaXlPvN6pr-_-CKKiTmAI-35GjJF0zZzi6ClGqfYiIZcgHaM0S_hq9TkVakL65VxGcxQS0otcWH317QaFmtH4ZjWXvplQMx2G4e3rKbg-tuX170nwyIB1LOY5Ymvp1E2ozzZM_IVgGDYnUM_zOgsjEQyBC4g73roPbaGIeXLM2FpB5D7wKRCJ5SX_G4dS4vOLcoq7yE7tJpp1JDx4afb1nCrFPPk9bK3r_ClKx5TuXKWHfLvhmnOtd-2PvfN8HAbv-enIuQhN74DFkK3IOZ7_qNTWbCqy8uhSKEPUj6uiP_cMl-nVI6Va4b8L4DERN4fMQuHCH2BZ5BqRhck9Dw353fI7kBPLl3MhTmKQA7v_atkm8tRlFy4A9t1O-hgqbV0Ikzw8KKU6SZbJU5EMayKdvEPAOQ6cd4iThTykAgTx1-QjiKozybmuk4FB1HVB9l0bYjqTxmoi6dwEycsMG4QZ81fGKX_AQe5-mTyAh4nVXJBVrdU9wG_0odKnKpfSr_7cXci1EUZWHT5f05qwoOwi2Q3px43_uqSNCiAfcCDJTtHC0PeY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d915ebc4d.mp4?token=rtyhrSZjgBAkv7xIhceTi9CDmpppGvyFnqi7P_cNMREtY_VdIPTdOnqogNVNVUuDdY2a_9R41cBClConvYTAiF6VRO5-un7Z_jpWx-j7n0sSWvdgx1pPGpdOJ8EaXlPvN6pr-_-CKKiTmAI-35GjJF0zZzi6ClGqfYiIZcgHaM0S_hq9TkVakL65VxGcxQS0otcWH317QaFmtH4ZjWXvplQMx2G4e3rKbg-tuX170nwyIB1LOY5Ymvp1E2ozzZM_IVgGDYnUM_zOgsjEQyBC4g73roPbaGIeXLM2FpB5D7wKRCJ5SX_G4dS4vOLcoq7yE7tJpp1JDx4afb1nCrFPPk9bK3r_ClKx5TuXKWHfLvhmnOtd-2PvfN8HAbv-enIuQhN74DFkK3IOZ7_qNTWbCqy8uhSKEPUj6uiP_cMl-nVI6Va4b8L4DERN4fMQuHCH2BZ5BqRhck9Dw353fI7kBPLl3MhTmKQA7v_atkm8tRlFy4A9t1O-hgqbV0Ikzw8KKU6SZbJU5EMayKdvEPAOQ6cd4iThTykAgTx1-QjiKozybmuk4FB1HVB9l0bYjqTxmoi6dwEycsMG4QZ81fGKX_AQe5-mTyAh4nVXJBVrdU9wG_0odKnKpfSr_7cXci1EUZWHT5f05qwoOwi2Q3px43_uqSNCiAfcCDJTtHC0PeY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیوکامل‌ضربات‌پنالتی دیدار حساس امشب دو تیم آرسنال
🆚
پاری‌سن ژرمن در فینال چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22502" target="_blank">📅 22:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22501">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50097d1448.mp4?token=kmC3VodN2HtrwSl_YUhRAVTHy6qTcgH_C7D0qJA7MGSjyBeAsA9Yug0JcFXHODtcA1Ggo1KY2JjDum7pJOE1xhhBSrm2Zce3Em3mZJqXHjH3JKov0Vuxzp2hE1gim_h6eQ8RbwEhgfSmfXNCuh0Ca6LwPnfDOeqbSlAPEeuhotwWp5PtEc64MFgAKhxyq8_T0u7j3ZLLP9Vq9AvzBTD0IsmuOZK4sQ7AAUZ0VjzFuX212tZ9uSW6Ys_Xiuzha9RrNQRvSWaIrA_n89ed258NkIwPsAXcmgKnQk5Dp-YuaCzHrV4tsLxy9Y1zar3OPge-tj97Lk30l1nBGiZyR73TzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50097d1448.mp4?token=kmC3VodN2HtrwSl_YUhRAVTHy6qTcgH_C7D0qJA7MGSjyBeAsA9Yug0JcFXHODtcA1Ggo1KY2JjDum7pJOE1xhhBSrm2Zce3Em3mZJqXHjH3JKov0Vuxzp2hE1gim_h6eQ8RbwEhgfSmfXNCuh0Ca6LwPnfDOeqbSlAPEeuhotwWp5PtEc64MFgAKhxyq8_T0u7j3ZLLP9Vq9AvzBTD0IsmuOZK4sQ7AAUZ0VjzFuX212tZ9uSW6Ys_Xiuzha9RrNQRvSWaIrA_n89ed258NkIwPsAXcmgKnQk5Dp-YuaCzHrV4tsLxy9Y1zar3OPge-tj97Lk30l1nBGiZyR73TzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
لحظه حک شدن نام باشگاه پاری‌ سن‌ ژرمن روی جام قهرمانی فصل 26-2025 لیگ قهرمانان اروپا؛ این دومین قهرمانی UCL در تاریخ PSG بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22501" target="_blank">📅 22:41 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

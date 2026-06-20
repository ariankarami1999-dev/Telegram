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
<img src="https://cdn4.telesco.pe/file/ohJkvxcbBl1svpoh22ptzIfbPgMl0XMzaWEmrgsnZJpNTCho_HFgis0_dxAbh3Y2ik5ra_6q4R82w0G5X_lEXfsI6FBzaDDr-iWzY98DJLGisDiRf60yITCO8Y23QuXs07LIvJNJAhJArDVCpDaUtvHmk3xm-IUlIMU6dv5z2Bj6lTU59IOBsdUAQgEpIZabcT234PBD4LTbLb0Kr5lQTqNS169P_I_l8enRSHcgAOfKXvIAHjbYmXeVVyor4C25gJhOrbN7m177UJIN8TcIgIMTu7Lcn52Nefzy8412r1EZdgBPLdI2UKl_zfvwkULqxea8V3CUxtKjJNwF7BZd6w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 222K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 11:47:27</div>
<hr>

<div class="tg-post" id="msg-66540">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda1b3db16.mp4?token=pjNHMs9qtLIRlV47A1VXKuHtX83FdvIai1dASQTfKSJU2eaqG0cwn2F-g9F7RoLe_qoDCRIwU-c-pkKbLK7qxiOsxxjkUeRHjrnt3EIQpuI_nZzZgee0ENb66fJbxuC8RX3brxoATdc_l6172qg-qGOubXpcXeUrqZVRH1URu9rxr5ehPTGxbHG3FuwLvILQ90V2EURyDsQpU0CTSyX9_D0jD2BVFYlfum9g9_0ROIzPrsoHovo7lrpEXKv7SnVNKH_Zxb-Co4YmswYalaGJM-5nh3A9N6KBXU7dWJ1N6SX0yJhpCZ6_lPsmWiJ38fEeFZM1EGDHqqquAOwvGAsEeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda1b3db16.mp4?token=pjNHMs9qtLIRlV47A1VXKuHtX83FdvIai1dASQTfKSJU2eaqG0cwn2F-g9F7RoLe_qoDCRIwU-c-pkKbLK7qxiOsxxjkUeRHjrnt3EIQpuI_nZzZgee0ENb66fJbxuC8RX3brxoATdc_l6172qg-qGOubXpcXeUrqZVRH1URu9rxr5ehPTGxbHG3FuwLvILQ90V2EURyDsQpU0CTSyX9_D0jD2BVFYlfum9g9_0ROIzPrsoHovo7lrpEXKv7SnVNKH_Zxb-Co4YmswYalaGJM-5nh3A9N6KBXU7dWJ1N6SX0yJhpCZ6_lPsmWiJ38fEeFZM1EGDHqqquAOwvGAsEeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری صدا وسیما : خواهش می‌کنم سلام من رو به مجتبی خامنه‌ای برسونید.
حدادعادل: والا منم به دامادم دسترسی ندارم، از همین‌جا بهش سلام می‌رسونم.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/news_hut/66540" target="_blank">📅 11:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66539">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4121482563.mp4?token=somjypIJQkeXmQnY6A21d8xpjQ5rRhWbOqMhtNx9fqa_zeJfVQ_3K1Q_-op8baN7DdjTiC-v7oSDJh72t_Cc-WbrEyiHIBdftHQ6gVQm22bnK0ziLC38BO5-dMBQh3-8ouc3_gZEmi4V3XYDEq-OYYFxD0-kKm_bPK9mTMOcV-7SEwnYnpIsbNGiEAT0zWY01pUQiOkucgzHc4552YomLUMVSQWimRJtbJsCpKJjC5GtSscICr1XlwvN6oXb0FglCqI0htlCFZO2i2ficx0n2sGiinHn4EZq3u98CbOLHDkyoM7_OOCKA1X4pZ58LH9izge6Se9NLQutsQzLRsSD3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4121482563.mp4?token=somjypIJQkeXmQnY6A21d8xpjQ5rRhWbOqMhtNx9fqa_zeJfVQ_3K1Q_-op8baN7DdjTiC-v7oSDJh72t_Cc-WbrEyiHIBdftHQ6gVQm22bnK0ziLC38BO5-dMBQh3-8ouc3_gZEmi4V3XYDEq-OYYFxD0-kKm_bPK9mTMOcV-7SEwnYnpIsbNGiEAT0zWY01pUQiOkucgzHc4552YomLUMVSQWimRJtbJsCpKJjC5GtSscICr1XlwvN6oXb0FglCqI0htlCFZO2i2ficx0n2sGiinHn4EZq3u98CbOLHDkyoM7_OOCKA1X4pZ58LH9izge6Se9NLQutsQzLRsSD3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇺🇸
‏ترامپ درباره کشته شدن قاسم سلیمانی:
اسرائیل در آخرین لحظه، زمانی که من سلیمانی را کشتم، از عملیات کنار کشید. قرار بود این کار با اسرائیل انجام شود. یک عملیات مشترک بود.
ما ۳۰ روز روی آن کار کرده بودیم. او فقط با هواپیماهای مسافربری و در میان تعداد زیادی از مردم سفر می‌کرد، چون می‌دانست ما آن هواپیما را سرنگون نخواهیم کرد. می‌دانید، هواپیمای نظامی قضیه‌اش فرق می‌کند.
او سوار هواپیما شد و همه چیز طبق برنامه پیش می‌رفت. اما یک روز قبل از عملیات، اسرائیل به ما گفت که در حمله شرکت نخواهد کرد. من هم این را درک کردم، چون برای آن‌ها چندان مناسب نبود.
اما من سراغ چند ژنرال رفتم؛ نه آدم‌های نادانی مثل میلی و بعضی از این افراد که واقعاً آدم‌های احمقی بودند و تصمیم گرفتند تجهیزات راجا بگذارند. من هیچ‌وقت تجهیزات را جا نمی‌گذارم.
به چند نفر از افراد کاربلد مراجعه کردم و گفتم: “نظر شما چیست؟
آن‌ها گفتند: “می‌توانیم بدون آن‌ها هم این کار را انجام دهیم؛ نیازی به آن‌ها نداریم، قربان.
پرسیدم: “آیا به همان خوبی خواهد بود؟
گفتند: “به همان خوبی یا حتی بهتر.
و آن حمله بدون هیچ نقصی انجام شد
@News_Hut</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/news_hut/66539" target="_blank">📅 10:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66538">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aceb39213f.mp4?token=WePaD2_p1JFvHSLloG8smPfQA2x2__n2nswpneAelsHMTsl7HxUY1nkcZ-NU0m9Oa8OQPQaKG5BOwy8QUTo7HVM37BO-d3X3ZUyXd5iggZSk417-s9HA_RY3sH7Jml5GwOvaNEGY3jxvWu1FgI1v6imSAWwHUXT-JI0Lqe0OJCclcfJG_kdHZSdHZ-iToiH4ByUrbGXgt3SskEUGOryTiRZiSUBx-eKak4iV_pzefuRPwO3fRxiNync5O239pDqkaUj0WjRGY-QtsI505jGpUzqd0Lvn-Wcs-dWh8VdjiPfJBb-X8tZjoOLz5tifP-WrAE2cmbEC05Y5e8aBzy24ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aceb39213f.mp4?token=WePaD2_p1JFvHSLloG8smPfQA2x2__n2nswpneAelsHMTsl7HxUY1nkcZ-NU0m9Oa8OQPQaKG5BOwy8QUTo7HVM37BO-d3X3ZUyXd5iggZSk417-s9HA_RY3sH7Jml5GwOvaNEGY3jxvWu1FgI1v6imSAWwHUXT-JI0Lqe0OJCclcfJG_kdHZSdHZ-iToiH4ByUrbGXgt3SskEUGOryTiRZiSUBx-eKak4iV_pzefuRPwO3fRxiNync5O239pDqkaUj0WjRGY-QtsI505jGpUzqd0Lvn-Wcs-dWh8VdjiPfJBb-X8tZjoOLz5tifP-WrAE2cmbEC05Y5e8aBzy24ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تهدید به قتل پزشکیان توسط مداح حکومت
😂
@News_Hut</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/news_hut/66538" target="_blank">📅 10:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66537">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae617fb56.mp4?token=l-uKTmmoTR276k9YVjapm1sgLq9iAQND-72VzMGsax5QKaEryAv4xqYl8myaHJ4RgdI-pCq31I1NXQIVKA0PFS6Qs66ix2BJlbEu_TTQ01TO5GV4P9eqssy8vR1-7Wx6ENx0Zdixtnl4TZwqniik79vrAAT5AbVzmtR8ecR7JvVNEC0ErarOK9cpWTnlBhNXIuWOkxUEsa1th-_3T8T5dTDInQMiivPpU4PPlQvnJgP-4iLYdZZyR6h9XNYu0gY1ovY-HxzFQqn1Y1O-UGV9XagOCMlMkwrmrMPwLwcIIqx88myaaahEkDIPPKS6x4Tf3By6C73qUibSq9yej2oOQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae617fb56.mp4?token=l-uKTmmoTR276k9YVjapm1sgLq9iAQND-72VzMGsax5QKaEryAv4xqYl8myaHJ4RgdI-pCq31I1NXQIVKA0PFS6Qs66ix2BJlbEu_TTQ01TO5GV4P9eqssy8vR1-7Wx6ENx0Zdixtnl4TZwqniik79vrAAT5AbVzmtR8ecR7JvVNEC0ErarOK9cpWTnlBhNXIuWOkxUEsa1th-_3T8T5dTDInQMiivPpU4PPlQvnJgP-4iLYdZZyR6h9XNYu0gY1ovY-HxzFQqn1Y1O-UGV9XagOCMlMkwrmrMPwLwcIIqx88myaaahEkDIPPKS6x4Tf3By6C73qUibSq9yej2oOQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حملات اسرائیل به مواضع حزب‌الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/66537" target="_blank">📅 09:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66536">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7deed372.mp4?token=OGqZUzJNCbj8f00zo8-6h4OBbdAq_htvpPBcjTbURB4IOReNWD5nQaQOYoLyqgqTfBeW50_cYF1ySOQOs9O0klPXOn1mkUIOJnNe-xC2fpXQd2N91DZrvDwZRFJUnNs-jUupUv96v658HOYn51ku78m28GzhRN_g-pFOUtLG0BVIFYvOc2CI1A3E7mecFaNP0LRI9s8D-yJlY-PV9FVWi_1fC3l5cDN3LhQEvXMg3TljyEAzVzFOziDnNaT3S7FyEcm5E5dB_vw0K4H-tHGCQeRdrF-BX7nxA2cEfXZ4Ilunpvr8ma1ocFcDcgQ7UO51S0UDXb8a8tmVV3f-w3EQow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7deed372.mp4?token=OGqZUzJNCbj8f00zo8-6h4OBbdAq_htvpPBcjTbURB4IOReNWD5nQaQOYoLyqgqTfBeW50_cYF1ySOQOs9O0klPXOn1mkUIOJnNe-xC2fpXQd2N91DZrvDwZRFJUnNs-jUupUv96v658HOYn51ku78m28GzhRN_g-pFOUtLG0BVIFYvOc2CI1A3E7mecFaNP0LRI9s8D-yJlY-PV9FVWi_1fC3l5cDN3LhQEvXMg3TljyEAzVzFOziDnNaT3S7FyEcm5E5dB_vw0K4H-tHGCQeRdrF-BX7nxA2cEfXZ4Ilunpvr8ma1ocFcDcgQ7UO51S0UDXb8a8tmVV3f-w3EQow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ هواپیمای «ایر فورس وان»را که از قطر به عنوان هدیه دریافت کرده بود معرفی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/66536" target="_blank">📅 09:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66535">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a046173b76.mp4?token=mTyt2q_5NwuI79H5URLbLxIulv5Y2wxjPmTa5Xk6GV5zu4Tjna_DVtYk6tvT6XsgtaD7IRnfqWHxshO5wqUNxCyMGeu6yqE4peEyCElr4RjkXFMxbvTh235z6UM4FzT-BpT5LOsBmMISpDFpQXBg-Kwo-Tvi5an0zxIty1F4wzLDidF9kTsNtz10o20LmqXz_SEtKldrRsToq6wtGi8XsniNebD2YIVEU2GZi7YW14IK82qDO7eUz-e3rVyVgcl6u7RhscPYPGv9NMNSreHkkv08enNYChvaEHMGjQhpewuJzq9jQelgRdAgDpmg8fARIEfkbNk4E-K8KPX3hOiCSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a046173b76.mp4?token=mTyt2q_5NwuI79H5URLbLxIulv5Y2wxjPmTa5Xk6GV5zu4Tjna_DVtYk6tvT6XsgtaD7IRnfqWHxshO5wqUNxCyMGeu6yqE4peEyCElr4RjkXFMxbvTh235z6UM4FzT-BpT5LOsBmMISpDFpQXBg-Kwo-Tvi5an0zxIty1F4wzLDidF9kTsNtz10o20LmqXz_SEtKldrRsToq6wtGi8XsniNebD2YIVEU2GZi7YW14IK82qDO7eUz-e3rVyVgcl6u7RhscPYPGv9NMNSreHkkv08enNYChvaEHMGjQhpewuJzq9jQelgRdAgDpmg8fARIEfkbNk4E-K8KPX3hOiCSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف در حال اهدای تندیس حاج قاسم به نیکلاس مادورو (خرداد۱۴۰۴)
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/66535" target="_blank">📅 09:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66534">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
🔴
فقط نظاره گر فوتبال نباش پیش بینی کن و پول دربیار
💵
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66534" target="_blank">📅 01:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66533">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUqoJ4iOUxQuTDI9k3DMWqxSXpL0MHJjL1pV4eQiOz66lUWSwE1AmTCXK9Q6tB5gHtFCfxGPYj4MBdhO4FcX6TFQFSJSLt3q6vH6fSdBm0q7-Rf9KLcYVXYrMm0rJrgtSUht7kPeLLfcNTy58ng2RYM6Soteui2HhxCKOguB445Be9dVVRAkIHaqfMN_M1OvpzvavVQztecC03tmk0VMjZ0LBsOJLkuUUMUAshLzp7B21ihP4kk3ExW8KDGzjun9txMjL6hVTSpe_NOVkHgT46gWPR86zcgNN40iOb9E85Fnv4TY1tUcJrVzFNmKgqYPSThYNGIg44B1V67IUdYWLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آمار فقط مال روز اول
جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو
پلنگ بت
جویین شو
بهت آموزش میدم چطور پول دربیاری و تا اخر
جام جهانی
سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66533" target="_blank">📅 01:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66532">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb104aecb9.mp4?token=NOoE_K6gSOZbFGFlQRl8hvZTi9Qw-43OKUbZEMtPx54VHHYdmZQminRSmKTRLrMVudwarKAuIY4Qgs2Zo1bO9ryTtFCCNUo-vN4iUibdwXCNlalBa8COcz9XNyLy1eNyeEg_F30wwTH7-0dEUCtkKZUhPpiST-M5SSQbIzzJ7r75v76vXgIh0LPJ7hQnusb_BIiz6wD1DwC6glb1bLzlBRRsO1_GZey9ZaX_Jf23DHKekVEPPHDT4wc-j2Ny_sQYhzJ7ASARVwLhlPDJNy6tbF2SIHRbem1wXYZ1YNca0JVaTdpacEwEko3N2xWuE-Xpxz-em8J9IyDNxDXkgOQK4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb104aecb9.mp4?token=NOoE_K6gSOZbFGFlQRl8hvZTi9Qw-43OKUbZEMtPx54VHHYdmZQminRSmKTRLrMVudwarKAuIY4Qgs2Zo1bO9ryTtFCCNUo-vN4iUibdwXCNlalBa8COcz9XNyLy1eNyeEg_F30wwTH7-0dEUCtkKZUhPpiST-M5SSQbIzzJ7r75v76vXgIh0LPJ7hQnusb_BIiz6wD1DwC6glb1bLzlBRRsO1_GZey9ZaX_Jf23DHKekVEPPHDT4wc-j2Ny_sQYhzJ7ASARVwLhlPDJNy6tbF2SIHRbem1wXYZ1YNca0JVaTdpacEwEko3N2xWuE-Xpxz-em8J9IyDNxDXkgOQK4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هم اکنون شیرینی آتش‌بس در لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66532" target="_blank">📅 00:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66531">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d8d08f74c.mp4?token=hkfBz-zGtSfbvRuxM7kWiQPtZro56VDtwpUAJ4QPcC6Mntv5ymBHtXYNtQpazr1t2mivUaCdI4FRfR_GU4wiDs4RWz5XJhHHioABysseZTcIjuRzLHiagtFJNuTkVcozEz9SHWtcXJIbQPLDsONbgYqMSiY8qg33_sK7zYpY2nNk8Iic_393au1wbnJj_1Zi58NLvdccGKErMvWT7dW2mS1FxNJn94a_3pSwcvsbYW1OYvZYfnZ2jswXcR0iSy_-ZoL1IVtnH8DoT-9HBE8eKz7rH1ObfYo1OVGTL-41l8TlSSkVGrsQJ049LyaudXuVtFLdYl_WjCoXidaYPdDWzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d8d08f74c.mp4?token=hkfBz-zGtSfbvRuxM7kWiQPtZro56VDtwpUAJ4QPcC6Mntv5ymBHtXYNtQpazr1t2mivUaCdI4FRfR_GU4wiDs4RWz5XJhHHioABysseZTcIjuRzLHiagtFJNuTkVcozEz9SHWtcXJIbQPLDsONbgYqMSiY8qg33_sK7zYpY2nNk8Iic_393au1wbnJj_1Zi58NLvdccGKErMvWT7dW2mS1FxNJn94a_3pSwcvsbYW1OYvZYfnZ2jswXcR0iSy_-ZoL1IVtnH8DoT-9HBE8eKz7rH1ObfYo1OVGTL-41l8TlSSkVGrsQJ049LyaudXuVtFLdYl_WjCoXidaYPdDWzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت پزشکیان
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66531" target="_blank">📅 00:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66530">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21fdcbfae8.mp4?token=tM3nc8jODxvczAHNyyUZbU4ecAsazZIOkSnDW_tOW_T42riGwtPYp9e7Gu67vLO0rhLtJmbUiEgcHNEPdr9-VITh6IRtXISRQDDciwOAOvOZ2UW5k3SXwrEudgk5XUtCjBeoYIcfaEl8m8lYCkAu_FwZWEStcBTMWOenpjNwytj_rYqbecCQIlPdiU-jOktn602exo6bGRe2ZZoR7ZLVkWsRK73tIjkzGetD1mtEMbKPqVjA0m1sBMpbJwp-b4Mft7PXn2PnJGQAmMNM0iByovpGeLl4a6eXhzG6AN6TYNNHProhoGzQ6i5lAXu-kM0_oOVIJ2aXtCui4KCNkWaPYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21fdcbfae8.mp4?token=tM3nc8jODxvczAHNyyUZbU4ecAsazZIOkSnDW_tOW_T42riGwtPYp9e7Gu67vLO0rhLtJmbUiEgcHNEPdr9-VITh6IRtXISRQDDciwOAOvOZ2UW5k3SXwrEudgk5XUtCjBeoYIcfaEl8m8lYCkAu_FwZWEStcBTMWOenpjNwytj_rYqbecCQIlPdiU-jOktn602exo6bGRe2ZZoR7ZLVkWsRK73tIjkzGetD1mtEMbKPqVjA0m1sBMpbJwp-b4Mft7PXn2PnJGQAmMNM0iByovpGeLl4a6eXhzG6AN6TYNNHProhoGzQ6i5lAXu-kM0_oOVIJ2aXtCui4KCNkWaPYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در مورد بایدن:
ما مردی داشتیم که نمی‌توانست از پله‌ها بالا برود، و من نمی‌خواهم در مورد این صحبت کنم چون اگر کمی زمین بخورم، می‌گویند: «اوه، این وحشتناک است.»
باشه، می‌تواند اتفاق بیفتد.
اما شما نمی‌توانید هر بار که روی صحنه می‌روید، زمین بخورید.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66530" target="_blank">📅 23:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66529">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5871cd20e4.mp4?token=IwrTUkyt-LyXeU_S4_zZqlbuMxhy-Z8UBt6c5tE4OlLvRMlFUJQrHlIYFemEqsqlo0F8_u0NueqPNNjG-AyXXQenx-q34eghUFIY7agZ7GJMxrL0qpufmVUcq8EoijBj79t854b-NMVP6mMCtCUqyrBiWY7QwpkTqRlmsyeb8AotVFJkzOG_J8jBAhSoXxvcK85stEqoQLky6wTa3qhzpieJlMWfjRNfyEh0IFTGQUwpF-ET-zMV4NJmWE1XNzVr7IW_jW9azdpiGs6DFBgNiM9o0xzteN64e_JeDjJE0VU_LsbE--1GSrHpFC4BlRGvrmVY6A0WO9grdC_c-RpgJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5871cd20e4.mp4?token=IwrTUkyt-LyXeU_S4_zZqlbuMxhy-Z8UBt6c5tE4OlLvRMlFUJQrHlIYFemEqsqlo0F8_u0NueqPNNjG-AyXXQenx-q34eghUFIY7agZ7GJMxrL0qpufmVUcq8EoijBj79t854b-NMVP6mMCtCUqyrBiWY7QwpkTqRlmsyeb8AotVFJkzOG_J8jBAhSoXxvcK85stEqoQLky6wTa3qhzpieJlMWfjRNfyEh0IFTGQUwpF-ET-zMV4NJmWE1XNzVr7IW_jW9azdpiGs6DFBgNiM9o0xzteN64e_JeDjJE0VU_LsbE--1GSrHpFC4BlRGvrmVY6A0WO9grdC_c-RpgJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت
ترامپ در مورد ایران:
من بزرگترین پل آنها را خراب کردم چون آنها دیر به جلسه آمدند. آنها گفتند که این خیلی خوب نیست.
آن پل، این پل جورج واشنگتن آنهاست. من آن را در سه دقیقه از بین بردم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66529" target="_blank">📅 23:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66528">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e43d6d5b.mp4?token=b7gfrBqAKQ-Q5gaj2qefWY0zfMDE_OksJytD9fD0VaR9BcdLThEpi36m-b2tuYAXTDdXo_mT_RHNYQX5hpRzmBR7O50vJsHmxlibK8A5tj1PryaSz53leaFWRUti6n_-7ysgB_L8iU-7pElulqB6F__Lo4-KtxLXWm9dwCRx-D3t85mMF2yXha4IjSnN3uQRst8JmGQwEoF4c04Y774vO4GWrZXitbEGOLR2eiVaHynXXbohnQN58CgqdPUyeej1emoi0wKs16YHsGVkyFp0wjQ8QbDT8ykFAnEakNiXM9qAu4rQI_Pnzr3AnF7jd6VJusIYXiGbrXkXRZ2nh1LFKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e43d6d5b.mp4?token=b7gfrBqAKQ-Q5gaj2qefWY0zfMDE_OksJytD9fD0VaR9BcdLThEpi36m-b2tuYAXTDdXo_mT_RHNYQX5hpRzmBR7O50vJsHmxlibK8A5tj1PryaSz53leaFWRUti6n_-7ysgB_L8iU-7pElulqB6F__Lo4-KtxLXWm9dwCRx-D3t85mMF2yXha4IjSnN3uQRst8JmGQwEoF4c04Y774vO4GWrZXitbEGOLR2eiVaHynXXbohnQN58CgqdPUyeej1emoi0wKs16YHsGVkyFp0wjQ8QbDT8ykFAnEakNiXM9qAu4rQI_Pnzr3AnF7jd6VJusIYXiGbrXkXRZ2nh1LFKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
اگر همین حالا به آن‌ها حمله می‌کردم—در حالی که ما قرار نیست نیروی زمینی بفرستیم، و شما هم نیروی زمینی نمی‌خواهید، درست است؟
اگر نیروی زمینی نفرستیم، احتمالاً همان افراد به اعماق غارها می‌روند. به آن‌ها “غارهای گرانیتی” می‌گویند. آن‌ها بسیار مستحکم هستند.
آن‌ها خیلی عمیق می‌روند، و بعد وقتی ما متوقف شویم، بیرون می‌آیند و احتمالاً همان رهبران قبلی خواهند بود.
در حال حاضر تنگه هرمز کاملاً بسته شده بود.
پر از مین می‌شد و موشک‌ها از بالای کشتی‌های میلیارددلاری عبور می‌کردند. آن کشتی‌ها دیگر هرگز عبور نمی‌کردند.
ما برای ماه‌ها نفت نداشتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66528" target="_blank">📅 23:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66527">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7522060f48.mp4?token=MTHfaxlGCssuos9k2MAgOgonjB7TufQ26ifK7QgdZG3mwdetwbAFBp9-6pJUd7zrKYyCdBb9lxGSnP5T65ugzsEHEZf3Z8fYy9lSiiu6v4UbsQN6r1HfJa15NwbC4hBwwzX2R91HDfMcCc0ZDLVaspmN_Kw9F7DxSmK9VvqgK4qalHxs9JFK3ZrSF02UgtXh7jIA611aHrztaBTAKyzAuRTJCm256_IC0OYo-m5k7C9W9l0WW_TPab-EUOpcDno7KKvDddSoEsL_5bMgv5xM4YEIlw3x_oJVafKRX01fTNb4TZSd2fioYCKvOiTmVHdeD9wntEJgc6NHO-5rDsA0dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7522060f48.mp4?token=MTHfaxlGCssuos9k2MAgOgonjB7TufQ26ifK7QgdZG3mwdetwbAFBp9-6pJUd7zrKYyCdBb9lxGSnP5T65ugzsEHEZf3Z8fYy9lSiiu6v4UbsQN6r1HfJa15NwbC4hBwwzX2R91HDfMcCc0ZDLVaspmN_Kw9F7DxSmK9VvqgK4qalHxs9JFK3ZrSF02UgtXh7jIA611aHrztaBTAKyzAuRTJCm256_IC0OYo-m5k7C9W9l0WW_TPab-EUOpcDno7KKvDddSoEsL_5bMgv5xM4YEIlw3x_oJVafKRX01fTNb4TZSd2fioYCKvOiTmVHdeD9wntEJgc6NHO-5rDsA0dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آتش‌سوزی کلیسا در خیابان بوشویک در بروکلین
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66527" target="_blank">📅 23:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66526">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2baf2d277c.mp4?token=OR6nQOY7uTzlOpYyZDyRRt3pcdv1G49NH8bwqnxTpBuXRHq19dG81T6bIQhHGkHeeIUes_CWJIqAsyLo9SS93vDfRGAXcYu1rqfoWtTPmO1gyYSBYf0vjb1bQpy2u6ziPqyDFqHhOUBUAQ8liqqFW3hcaQwv4yg4No0yfEc77Nt7L52h3F2HHzyUomq0Horihr1VwqZTXyEtdzphbB-zvNxTS-TQGQFt8lawxh1Z5H0axryJ5Z2oILzTm1sLkMZ6UAxw1Owxyw8qy9NarIElhEAHClB0-FUFX_4XdQ1_08j3iSATOIUlikj1hHWeEIgYr2T4sFZCXlfZt2dyMNkrbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2baf2d277c.mp4?token=OR6nQOY7uTzlOpYyZDyRRt3pcdv1G49NH8bwqnxTpBuXRHq19dG81T6bIQhHGkHeeIUes_CWJIqAsyLo9SS93vDfRGAXcYu1rqfoWtTPmO1gyYSBYf0vjb1bQpy2u6ziPqyDFqHhOUBUAQ8liqqFW3hcaQwv4yg4No0yfEc77Nt7L52h3F2HHzyUomq0Horihr1VwqZTXyEtdzphbB-zvNxTS-TQGQFt8lawxh1Z5H0axryJ5Z2oILzTm1sLkMZ6UAxw1Owxyw8qy9NarIElhEAHClB0-FUFX_4XdQ1_08j3iSATOIUlikj1hHWeEIgYr2T4sFZCXlfZt2dyMNkrbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارک کاپوتو از اکسیوس:
این چه تغییر رژیمی است که‌ انجام داده اید؟ شما خامنه‌ای جونیور (جوان) را همچنان در ایران دارید.
پرزیدنت ترامپ: خامنه‌ای جونیور با پدر متفاوت است. آن‌ها افراد متفاوتی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66526" target="_blank">📅 22:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66525">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5016d97e5.mp4?token=SYkaDuzatfvNAxLA3tPDNdap8-5JAAEmRUMA3_0k60_OdfbwejDg614k50bqqtpouyxqwTxkf-X-q6TqkleI3o71mmrE2YlCItTUZNKm02ezU_05Z_jwGuehce0D09KHSSSFpDMcho2sTOUFBvK_jjFksmMLhydu1I2v6tj4ZfruF956mpwKhP-qt6zmjCWleIR_oRshGymKmxCVSc00eVbJzyhUUzYD3RW7zhUlvoXgh3c8vPhj5bJqjgrTqC5CjbTYUF-3bHdbnjlTCrcj30MH93m5Q4GB-We6XVZpNSXTzanATDoXf2waevS9lRIaNlNXcA8d4j3uOduCc9Mn1oTz5c2kvlNh4xWOh2wIYYuLm9koViWfktgF-LbZkuwmIxLCc6tyO9WjjS5XppFZ3bL-Lgr_yOdB-ODTudtUkx6QS9l52CkouvjLXWpMJC9bgkL7UXB1UOvGVuD4lo6qhUgXoEeWwbMqjk9TOH8ScUOVLf6_v_v5ZeTe-MLyE2mVEeLONqiP1hPvrrFJ2MS6F_v05orkmAsM4TmIlm0rX3EQkJPJ6-_06eUzr1fW88jwkpDOH0bKdaFgx2HaGGjix-7Yls4Lkn2IfaVvZr0ZOEWMHxfxBjPklNhBMFcHoIHUDaXPPZu9dzRhydIAACpqYOHxFl-Tjio8dWN3n6XJ83o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5016d97e5.mp4?token=SYkaDuzatfvNAxLA3tPDNdap8-5JAAEmRUMA3_0k60_OdfbwejDg614k50bqqtpouyxqwTxkf-X-q6TqkleI3o71mmrE2YlCItTUZNKm02ezU_05Z_jwGuehce0D09KHSSSFpDMcho2sTOUFBvK_jjFksmMLhydu1I2v6tj4ZfruF956mpwKhP-qt6zmjCWleIR_oRshGymKmxCVSc00eVbJzyhUUzYD3RW7zhUlvoXgh3c8vPhj5bJqjgrTqC5CjbTYUF-3bHdbnjlTCrcj30MH93m5Q4GB-We6XVZpNSXTzanATDoXf2waevS9lRIaNlNXcA8d4j3uOduCc9Mn1oTz5c2kvlNh4xWOh2wIYYuLm9koViWfktgF-LbZkuwmIxLCc6tyO9WjjS5XppFZ3bL-Lgr_yOdB-ODTudtUkx6QS9l52CkouvjLXWpMJC9bgkL7UXB1UOvGVuD4lo6qhUgXoEeWwbMqjk9TOH8ScUOVLf6_v_v5ZeTe-MLyE2mVEeLONqiP1hPvrrFJ2MS6F_v05orkmAsM4TmIlm0rX3EQkJPJ6-_06eUzr1fW88jwkpDOH0bKdaFgx2HaGGjix-7Yls4Lkn2IfaVvZr0ZOEWMHxfxBjPklNhBMFcHoIHUDaXPPZu9dzRhydIAACpqYOHxFl-Tjio8dWN3n6XJ83o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره مجتبی خامنه‌ای:
من آیت الله را کشتم و متأسفانه آیت الله دیگر را آزار دادم.
من او را ملاقات نکردم. من با او صحبت نکردم، اما مردم از او صحبت می کردند.
اما او شجاعت خاصی دارد زیرا به شدت مجروح شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66525" target="_blank">📅 22:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66524">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb514f4019.mp4?token=GOwGETRcNY_j_zgpQrTLRL5bf8vUElgL_weQhwgsdTgl5x-rCyr8QkOhlFg0SLY7TWlschYqqVj97viky_kHKTZc27dQ7s5tq1RmNaTwB9RfgRG6uAa_8g70x5z63JzAyx0fBUdGkyQuyJTVI_4uef6S-nNn-2Ipqnk38qT9YSozeEQRxqW-pXSCG3I8hcQ-lTj-vJMy4LlFnHN4u-FY9x97zgIQJs1XW8QXs25_ztAzp5Yd6tyXD-gXo0TJrfLsn97IFh8ewfGlpeVdu5gJlQ-JNTH_-kYljJm4a4P42aInQuV7aGpRJlbJCERLeAwqLBadnfLhl9_TRRxcy9RJSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb514f4019.mp4?token=GOwGETRcNY_j_zgpQrTLRL5bf8vUElgL_weQhwgsdTgl5x-rCyr8QkOhlFg0SLY7TWlschYqqVj97viky_kHKTZc27dQ7s5tq1RmNaTwB9RfgRG6uAa_8g70x5z63JzAyx0fBUdGkyQuyJTVI_4uef6S-nNn-2Ipqnk38qT9YSozeEQRxqW-pXSCG3I8hcQ-lTj-vJMy4LlFnHN4u-FY9x97zgIQJs1XW8QXs25_ztAzp5Yd6tyXD-gXo0TJrfLsn97IFh8ewfGlpeVdu5gJlQ-JNTH_-kYljJm4a4P42aInQuV7aGpRJlbJCERLeAwqLBadnfLhl9_TRRxcy9RJSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس درباره ایران:
این ایده که اماراتی‌ها قرار است یک میلیارد دلار برای ساخت نیروگاه در ایران سرمایه‌گذاری کنند، اگر ایرانی‌ها رفتار خود را تغییر نداده باشند، پوچ است.
آنها این کار را نخواهند کرد. ما اجازه این کار را نخواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66524" target="_blank">📅 22:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66523">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e9895e96f.mp4?token=nXHTT8xSUn8cl7b0bT-bFTTZjCFMm-cRaiBV-w2_g1qcSFZzaelfT6UFdIYsr_sVZJeDrqZPGXDYTrFMDNwhWbccyfLGtl6BrQ62VRsfL-5x93crJANoQW_x2QidbkyVEbVs-0LWcsN1OXfXxPKZe6dSk_seuB2_fOOUqj2Hb2cKlWIvHDaf_48Q2naxkAfejf3_dps0Kt6wcllms-0pv1Va_M_Fa96k0iqZ5aCGDpsszIjeqzoHSr3YQfdJaO-x0qgh88vic6kBySbVUCvsOvP-T5VhHtZYDfZBaAOOoO9TGBFuHOQWD_hFYHRf7WKSL6CTB5jVY4DMVuqvwtsOPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e9895e96f.mp4?token=nXHTT8xSUn8cl7b0bT-bFTTZjCFMm-cRaiBV-w2_g1qcSFZzaelfT6UFdIYsr_sVZJeDrqZPGXDYTrFMDNwhWbccyfLGtl6BrQ62VRsfL-5x93crJANoQW_x2QidbkyVEbVs-0LWcsN1OXfXxPKZe6dSk_seuB2_fOOUqj2Hb2cKlWIvHDaf_48Q2naxkAfejf3_dps0Kt6wcllms-0pv1Va_M_Fa96k0iqZ5aCGDpsszIjeqzoHSr3YQfdJaO-x0qgh88vic6kBySbVUCvsOvP-T5VhHtZYDfZBaAOOoO9TGBFuHOQWD_hFYHRf7WKSL6CTB5jVY4DMVuqvwtsOPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
‏پیشنهاد جی‌دی‌ونس به ایران:
گزینه الف این است که شما همچنان مانند یک رژیم تروریستی رفتار کنید، که در این صورت به معنای واقعی کلمه هیچ چیزی به دست نمی‌آورید.
گزینه ب این است که شما مانند یک رژیم عادی رفتار کنید، و ایالات متحده، به عنوان مثال، اگر قطری‌ها یا اماراتی‌ها می‌خواستند در کشور شما سرمایه‌گذاری کنند، در واقع به آنها اجازه می‌داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66523" target="_blank">📅 22:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66522">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03f005383e.mp4?token=rhRrvQ-QZuDNg71Kwz4oABbt8EdPy5pe9KaN1TORpzBrpt9YcQfAr9b8rexpndyjHYJZEc0MU0iug_nfSwDhsSShX6RUpT12AF2TTctoWQ3c1PTKtjLbbtnneNPvZZyWhknji8_kT3GYdd2nrAn-dszg-FfJVpkA0N9vuCMStzLhHVdhAKZYYIHgBVU9fap-PQ4FNxdpHkviyiWbo8WXsnEguMJYS_FyZhJm3KIeElHrJxZmoPjkQ8VUnMiSun_wD7V6pY-lxePDXPX62vhiqeUCY1Ix5PWeoOPzidCF6aQIEyIO_LmpBfSE90jc3WOgMGQBt7xf0UFBwetlCkWZsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03f005383e.mp4?token=rhRrvQ-QZuDNg71Kwz4oABbt8EdPy5pe9KaN1TORpzBrpt9YcQfAr9b8rexpndyjHYJZEc0MU0iug_nfSwDhsSShX6RUpT12AF2TTctoWQ3c1PTKtjLbbtnneNPvZZyWhknji8_kT3GYdd2nrAn-dszg-FfJVpkA0N9vuCMStzLhHVdhAKZYYIHgBVU9fap-PQ4FNxdpHkviyiWbo8WXsnEguMJYS_FyZhJm3KIeElHrJxZmoPjkQ8VUnMiSun_wD7V6pY-lxePDXPX62vhiqeUCY1Ix5PWeoOPzidCF6aQIEyIO_LmpBfSE90jc3WOgMGQBt7xf0UFBwetlCkWZsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی ونس درباره اسرائیل:
من از تصمیم ترامپ برای پایان دادن به توافق ایران دفاع کرده‌ام و اغلب متوجه شده‌ام که استدلال‌ها این است که «اسرائیل فکر نمی‌کند این خوب است، بنابراین بد است.»
واکنش من این است: نظرات اسرائیل مهم است، اما اساساً آنها از هم جدا هستند
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66522" target="_blank">📅 21:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66521">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ebdd0a4c.mp4?token=oo_ocYEUJD0vHZRZtomHvmYWhx5cqpJiOV9TKnL6qwU8vHTMzsus8N4erCMD3rRvZ9x1TonEP95XZ47nGQPDA7fPYhgrUGp-bv7WrZUQE75zuIu5EbezKs4juo55DIGc0J1aCqZGym-VnBAz0-TJwxSGwx7NMiWjTs4cRwt8FbCNedOKppkhvkUyvAT_HTHZftV2zWD25BqbbvczjDrmo4wkapEXfnKolSf1DdJXZrNPmUiZ6ykk9QcCYWr_TUpjluZNJuqXTcidOk94AG3IZv3LDuAUd90ITvbxZMkUrKO8uXEW7RHaYTUqUBzb-86cVeJgLXluoYlGEG4kgHF_nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ebdd0a4c.mp4?token=oo_ocYEUJD0vHZRZtomHvmYWhx5cqpJiOV9TKnL6qwU8vHTMzsus8N4erCMD3rRvZ9x1TonEP95XZ47nGQPDA7fPYhgrUGp-bv7WrZUQE75zuIu5EbezKs4juo55DIGc0J1aCqZGym-VnBAz0-TJwxSGwx7NMiWjTs4cRwt8FbCNedOKppkhvkUyvAT_HTHZftV2zWD25BqbbvczjDrmo4wkapEXfnKolSf1DdJXZrNPmUiZ6ykk9QcCYWr_TUpjluZNJuqXTcidOk94AG3IZv3LDuAUd90ITvbxZMkUrKO8uXEW7RHaYTUqUBzb-86cVeJgLXluoYlGEG4kgHF_nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس درباره اسرائیل:
اسرائیل شریک خوبی است، همانطور که بریتانیا یا فرانسه شرکای خوبی هستند.
این بدان معنا نیست که ما همیشه منافع همسو خواهیم داشت
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66521" target="_blank">📅 21:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66520">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c3443a503.mp4?token=o5f05IBHt0hKL6QxHLqwQCAT4hclO6s7D0nwa122S0_AVMxA_sKQxDz-L6n9xT8BhWFcwEnbzpiHZXsOyzjPAd7xcBjvT1KfT1coHpDAdrehskoExMMPSZpCmNIzHlnNVYSMF4B5jGVA_KjTm7261Kb979lMuirYEaef-na-uIbFjs5GCIf6SO7fS8IX007We1QBkbpe2Tun_beqtl4T9WpmPSI9BigkD1ysDk9FMhJxis2sXQhYcQNU-DKymk0InWdAh2v4E8jZjT9tvkGvvsEagSpMsa6aGematt8c1tq0Q8O8X5G65c9rTeW098W-8QghmUq24c7eCz_rTcJjvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c3443a503.mp4?token=o5f05IBHt0hKL6QxHLqwQCAT4hclO6s7D0nwa122S0_AVMxA_sKQxDz-L6n9xT8BhWFcwEnbzpiHZXsOyzjPAd7xcBjvT1KfT1coHpDAdrehskoExMMPSZpCmNIzHlnNVYSMF4B5jGVA_KjTm7261Kb979lMuirYEaef-na-uIbFjs5GCIf6SO7fS8IX007We1QBkbpe2Tun_beqtl4T9WpmPSI9BigkD1ysDk9FMhJxis2sXQhYcQNU-DKymk0InWdAh2v4E8jZjT9tvkGvvsEagSpMsa6aGematt8c1tq0Q8O8X5G65c9rTeW098W-8QghmUq24c7eCz_rTcJjvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی ونس درباره ایران:
باز کردن تنگه هرمز دلیل کاهش قیمت نفت از اوج ۱۲۶ دلار به حدود ۷۵ دلار در امروز است.
و همچنین به همین دلیل است که قیمت بنزین، اکنون که ما صحبت می‌کنیم، برای اولین بار از ماه مارس، با وجود افزایش به میانگین حدود ۴.۶۰ دلار، به زیر ۴ دلار رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66520" target="_blank">📅 21:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66519">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q751ZHJaVnZ9QlYe2kZGRIbNSBRhxJrq5Ej1NbU0VsqEls_cF-WKuu_Jmp-yEuFXeUu65aCYJptz8yf2U4Uc1Lbstl3R4pKCZ_s1QnaZ-ACPWLksyHLk61axGK5AtiFcXZQLguYBC8eCsaYZ3hz-i5zGPjw8M7_F981812LJilDy9fwWVA7ZLL8jT64wC22-6JIa19EpAR2qhoyS33Ei0Rkvojv5KeOaxD69LHGZ-F1SKZR-X039sP90Z273EOiCgoZYcbWzJOi7maUCpWZorEd0Fovkf1SXz6Xe5ULmKB3B_Lotu0MiTbe42SWTnqQfOB9187AQ9E1g9OJ8RKOeqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هیئت قطری رفته سوئیس ولی ایران و آمریکا نرفتن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66519" target="_blank">📅 21:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66518">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pB9jbM1WbD2lFuw4E6Mj_LO_zJJRHbvqgKeaCxu-awioBhUDJGMyPey-p15SgAhg7bKxaM5AnFzQjWesTmYeq8AAsXwunPJR90G-0L6XwXGiEN-O0Fi-0X7HL4iYFdmC2QZfGY8H7BqKG0WA2JPga9uQoWmSpw1jFRRn1VZfTWEk4dTcTL6Ugd96irhL3Puv5MBOu6BN64ENNPe_-iEjkUO0MJTwmTB7Qy8oCXT1slFoZ1t6FFEF-IM_WnW380xeXgz2zd3ZojMIjuOoYtsD8AKKmRERd_mKKQPbOe8T8kkv59m8E09ZJFCnTmVKXbk9bkDtOi5oQsaGgM75Xvibtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌پست:
آمریکا ادعای «مزخرف» مبنی بر اینکه امارات متحده عربی - یا هر کشور دیگری - دارایی‌های مسدود شده ایران را آزاد کرده است، رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66518" target="_blank">📅 21:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66517">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4VamswQSOglcfWTa3CUiVyxNNyxmxkHwr8UUZ94QfLXCMUpiE9w9oruNJ-ZwQdBHppsvkIDLzGbZ1HslCeL-F3Zf_o9_xpRna5o9pGtsQ3D4H-QNCS91HwN0d-ha6oVAvMqXRtmBeJgEdA2fA85Cjk1s4W3A036qB9v0UTPcxVi1KDdFlRPPhvMdESDUC1ftIVo1rb2oaFW7ITpN-a4ad0rN9VSuI4hSh8XIckTFGn2o_XtDiLwQAagqg1X8RlUQXpgzHXOk4tt7AG6pdRWVFyV-altiQ_y7xp4R9NPIEnpz4uoCuSnJu44ObssLi6-O_6ep-G1C1dIm8JZzteR2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سازمان‌های اطلاعاتی ایالات متحده به دولت ترامپ هشدار دادند که نتانیاهو احتمالاً اقداماتی انجام خواهد داد که می‌تواند توافق صلح جدید ایالات متحده و ایران را تضعیف کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66517" target="_blank">📅 20:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66516">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700e55c3c3.mp4?token=pswvFv6J4uqxZiXLAslHA5tALG_dB_kdecdJSojNjdqPkxyBo68Ys57T_PhoiTdQknF0RwCTcVxc3SEMcAXCRgOaEBVYq6LCCD09NJ6vgFsl6L7IMnw4wZj2LHtRmtjfI_3Fxiu8XnEos3b-YfUMVeZ5GNBk13uy_o3TStveIP8ijWqX8JXFNHxfDApCrgTAmtY-PbWcXbV8cWdLgkGk4FGSdjNr5JN9tqlCMuYQ1tZrhhliR5OQB493s7zePLuRUMPMPgHh3TO1t4Y65VBMduA0xoJUizZEDzl0Z0L9rB5tzDeLFPEwO09X0QZadw_KVjujE0QXeSaRb7EzwFmQ8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700e55c3c3.mp4?token=pswvFv6J4uqxZiXLAslHA5tALG_dB_kdecdJSojNjdqPkxyBo68Ys57T_PhoiTdQknF0RwCTcVxc3SEMcAXCRgOaEBVYq6LCCD09NJ6vgFsl6L7IMnw4wZj2LHtRmtjfI_3Fxiu8XnEos3b-YfUMVeZ5GNBk13uy_o3TStveIP8ijWqX8JXFNHxfDApCrgTAmtY-PbWcXbV8cWdLgkGk4FGSdjNr5JN9tqlCMuYQ1tZrhhliR5OQB493s7zePLuRUMPMPgHh3TO1t4Y65VBMduA0xoJUizZEDzl0Z0L9rB5tzDeLFPEwO09X0QZadw_KVjujE0QXeSaRb7EzwFmQ8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇱🇧
نعیم قاسم، دبیر کل حزب‌الله:
امروز در لبنان، ما با خطرناک‌ترین مرحله تاریخ خود و بزرگترین توطئه مشترک آمریکایی، اسرائیلی و بین‌المللی روبرو هستیم که آینده کشور و فرزندانمان را تهدید می‌کند.
هدف اصلی این طرح، ریشه‌کن کردن و حذف کامل مقاومت و پایگاه مردمی آن در لبنان است.
دشمنان برای دستیابی به این هدف، ابتدا جنگی جنایتکارانه و بی‌حد و حصر را آغاز کردند و با کشتار غیرنظامیان و تخریب گسترده، مقاومت را به زانو درآوردند.
در گام بعدی، ایالات متحده و رژیم صهیونیستی پس از مشاهده تغییرات در معادلات منطقه‌ای پس از تحولات سوریه، توافقات قبلی را نقض کردند تا موازنه قدرت را به نفع خود تغییر دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66516" target="_blank">📅 20:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66515">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46f332c84e.mp4?token=pWsMSRNpixzPkVhr1fqOnOD7p_REz1VUsUgx5-IpW1xTIYOX0GR26Ml7mPqry7jhwWS8rM3iVLPwW9JrKOvrYCnANR5HORyd4xmPhO3nBdYp2NU8JPSbxnx7PbMUpFJN97HPoFqFE5LpFA4Y6_JInNqGLfrl1DNOCpTWpCPCPOpaevoexHg5YoZKFsiXq_4W0ZqNnFEe8SLKXpmH4AeCGEt7xTwx1h7puNUfEESolQAhRfTtOuMa4-ZR4RGO6cwmvvOckUhJ6MLJJ-QDhNqjRMeb7q-HXIScKbQYarnHvP9wjnhJQOa4agb6d04Ze8Xz24k3A1Ldo-dls_e5sNQ8oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46f332c84e.mp4?token=pWsMSRNpixzPkVhr1fqOnOD7p_REz1VUsUgx5-IpW1xTIYOX0GR26Ml7mPqry7jhwWS8rM3iVLPwW9JrKOvrYCnANR5HORyd4xmPhO3nBdYp2NU8JPSbxnx7PbMUpFJN97HPoFqFE5LpFA4Y6_JInNqGLfrl1DNOCpTWpCPCPOpaevoexHg5YoZKFsiXq_4W0ZqNnFEe8SLKXpmH4AeCGEt7xTwx1h7puNUfEESolQAhRfTtOuMa4-ZR4RGO6cwmvvOckUhJ6MLJJ-QDhNqjRMeb7q-HXIScKbQYarnHvP9wjnhJQOa4agb6d04Ze8Xz24k3A1Ldo-dls_e5sNQ8oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇱🇧
نعیم قاسم دبیر کل حزب‌الله:
پروژه نابودی حزب‌الله شکست خورده است، نقشه‌های اسرائیل به بن‌بست رسیده است و پیروزی نهایی، یعنی اخراج کامل و قطعی اشغالگران از هر وجب از خاک لبنان اجتناب‌ناپذیر است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66515" target="_blank">📅 20:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66514">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66514" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66514" target="_blank">📅 20:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66513">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66513" target="_blank">📅 20:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66512">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
نعیم قاسم، دبیرکل حزب‌الله لبنان:«تا زمانی که توان ایستادگی داریم، چرا باید تسلیم شویم؟.»
حزب‌الله خلع سلاح نخواهد شد. این سلاح‌ها برای مقابله با اسرائیل هستند.ما تصمیمی «به سبک کربلا» گرفتیم و این تصمیم همچنان به قوت خود باقی است.
«ما وحدت نیروهای مقاومت را حفظ کرده‌ایم و وحدت جنبش امل، حزب‌الله و سایر نیروها همچنان در کنار ما برقرار است.»
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66512" target="_blank">📅 19:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66511">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRKaZnoVoVh_PwmoRC9STLgRYj-s8VGFIWMgvLOFQy_GMRV-L7PhJLC5lbWrjp0I8TCWLkig76bYK529I0zWqoZUc3sVu-gn28D-dbC4CBleHvAaYa-lsHw03d4wn2PpwIK-MRS3l49aZyeokqwHtNGwlJTGu6EJ29mlVM1tco3v7Bo8ZpQEmKuGSLPzwLN9Xhi2w5WaWoD6rnZeJaFIrQqLbYxZd6MywXF96xztjl5SO8TtOdl4Uk7eQ4kvKPGT9jxyKapCx4RpJvGGwuMHGFJEK3EyxCnU5sQI_THUgfjim3JS9L3V6LBlC7Tgc4mSxrgbJ5WDaMN3xbqfgi5OtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اتاق جنگ اسرائیل:
رژیم تروریستی ایران از نیروی نیابتی خود، حزب‌الله، برای حمله به اسرائیل استفاده می‌کند، به این امید که بتواند وقتی اسرائیل پاسخ می‌دهد، اسرائیل را به خاطر از مسیر خارج کردن مذاکرات سرزنش کند.
ایالات متحده باید به حمایت از حق اسرائیل برای دفاع از خود در برابر رژیم نسل‌کش ایران و نیروهای نیابتی آن ادامه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66511" target="_blank">📅 19:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66510">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d0ea7af18.mp4?token=Mb20T0uqPXDfqVz5-fye3UCzxZ2njVwhFI0zLUXsxk4hb6mwGMTjEFaa2lt8HXrb8HKjm0bfzAbZ3nQQGUtIt9ySFlAqSKNqmEoeIZiUgYLCTvAzdofBcjdk419btM99a2egeRQr4W-LOeYHz7uynqIjk6407FmWxuNny4xoERjfcSiK4YOX7nrHTbIGov5XKS43QVWpeHQhgFGuAQ29c6Bx6usqEGgHtcm1fXNq2TwGLlcT_fAN4XV9SOLo0e7nCZVG7fCVahKXyYX3tnRqpXZSgo0AQp-vJqw_wwdIKXyS4E7mgVtEC8o4xwLafry_lSfe-gKmunT9tGS2EMS42A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d0ea7af18.mp4?token=Mb20T0uqPXDfqVz5-fye3UCzxZ2njVwhFI0zLUXsxk4hb6mwGMTjEFaa2lt8HXrb8HKjm0bfzAbZ3nQQGUtIt9ySFlAqSKNqmEoeIZiUgYLCTvAzdofBcjdk419btM99a2egeRQr4W-LOeYHz7uynqIjk6407FmWxuNny4xoERjfcSiK4YOX7nrHTbIGov5XKS43QVWpeHQhgFGuAQ29c6Bx6usqEGgHtcm1fXNq2TwGLlcT_fAN4XV9SOLo0e7nCZVG7fCVahKXyYX3tnRqpXZSgo0AQp-vJqw_wwdIKXyS4E7mgVtEC8o4xwLafry_lSfe-gKmunT9tGS2EMS42A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
«هر مشکلی در خاورمیانه مستقیماً به ایران برمی‌گردد. حزب‌الله؟ ایران. شبه‌نظامیان شیعه که عراق را نابود و تهدید می‌کنند؟ ایران. حماس؟ ایران. حوثی‌ها؟ ایران. اسد که در سوریه مردم را قتل عام می‌کند؟ ایران. این رژیم هزاران هزار نفر را کشته است.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66510" target="_blank">📅 19:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66509">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLIRB8MqmCqyXHfU10UU1fkc59Vghyl8hqw4GgLKpNNFhJJtaCbbJit8RJmQOE_jHZqHsml7FW3BXk_i-tgoEidIDgVSRxrJIMxIB22VjhxWAIRF6XggQLb8vJFl3-oBN99qugVjd24zEbFDKzxYZly5Ay7xsCPrswCtzpF-6do5KVhvqitXgJx3vY1bCigRYkVU5AWezwb8naS5XqQptNUK-CCqssktk2WyHsGIaW3PbelIL2OPZgI6pd_tLB3HdEmC8As5rFam8812GbkT71toCpcf7Yx-1MuWFTctwDIqCS9mJUwhQtjwRoSPoVbtwF55spaHThsEbVK2JRjCIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اسرائیل هیوم به ترامپ:
می‌تونستی بزرگ‌ترین رئیس‌جمهور تاریخ باشی، اما شکست خوردی
شما به منافع جهان متمدن ضربه زدی و ممکنه به‌عنوان رئیس‌جمهوری در یادها بمانی که باعث تحقیر آمریکا شد
به اسرائیل خیانت کردی و حالا تمام تحقیرهایی که قبلا باهاش روبه‌رو بودی، کاملا موجه به نظر می‌رسد
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66509" target="_blank">📅 18:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66508">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامپ:
ما از روی استیصال پای میز مذاکره نرفته ایم.این ایران بود که از سر استیصال آمد. کارشان تمام شده است!
ما این دوره ۶۰ روزه را تا آخر پیش می‌بریم. آن‌ها هیچ پولی دریافت نخواهند کرد؛ حتی یک سنت هم نه!
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66508" target="_blank">📅 18:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66507">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c09804d09.mp4?token=v9Rykgkj1E6U8L-_UioBcsx86O_1libQv8AAFuhHfIEnMtmLmhC23H3P1CRSuy8XLciAjG3gKJLYCwURScH_hw18nu-2ChuUy4URhLSwx8dlgI5vtKooYWdvHKytsgcf6Vx6rMLp9HqHtvFCI-iVzQ7OJCzQRI-RFECFcSHLHCh-jBzhWb0yuOVPMLVY43mUibzgjbs1EuvzlfQsp1KIx5xkHm7N6WyDTwXC0P39g8Px2xFyfiRh93lxguOLTkcexvW-qqIY_-zNBjWmhfcz29cxgtnPPpS_1NUZk5kXghsiNKzMjHOTCQfDuxkgvoHWXIAjzA5Xd7H7oitKp_u-gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c09804d09.mp4?token=v9Rykgkj1E6U8L-_UioBcsx86O_1libQv8AAFuhHfIEnMtmLmhC23H3P1CRSuy8XLciAjG3gKJLYCwURScH_hw18nu-2ChuUy4URhLSwx8dlgI5vtKooYWdvHKytsgcf6Vx6rMLp9HqHtvFCI-iVzQ7OJCzQRI-RFECFcSHLHCh-jBzhWb0yuOVPMLVY43mUibzgjbs1EuvzlfQsp1KIx5xkHm7N6WyDTwXC0P39g8Px2xFyfiRh93lxguOLTkcexvW-qqIY_-zNBjWmhfcz29cxgtnPPpS_1NUZk5kXghsiNKzMjHOTCQfDuxkgvoHWXIAjzA5Xd7H7oitKp_u-gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
همانطور که دستور دادم، ارتش اسرائیل با قدرت به ۱۵۰ هدف حزب‌الله در لبنان حمله کرد و ده‌ها تروریست را از بین برد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66507" target="_blank">📅 18:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66506">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">Live Tennis</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66506" target="_blank">📅 18:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66505">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faa1be6643.mp4?token=YoeyvmIF4KyMeth-KlrcPOSOC9qB_AyY07ieHLYi9k4Z-T7VASrctArWG-dAwps9M53fD51dZPSarGkEdG52RL8FFd8CMYB_a1fGaMMBXejZrYTqCIXaLxsnHR5tm7GnOV95qPcTPdRiNZbLR9tgmM5pwMxaDctobQA2JtqM4I1F5lef7X0I9itXsFeLQ_10yOMpNzDCbKjRhY3Y50n2IHk949qq0NIgAXCCHX0MQF344ae0E-wbSf5dDVgEDsSyFTl-Jicly1kVYB0eU3s2OsSUlxkTuglO-CmnO4D8vpQGwJELrh9ilmX42CZjZoB8XD44tLsTBfbdWFm0gqOIbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faa1be6643.mp4?token=YoeyvmIF4KyMeth-KlrcPOSOC9qB_AyY07ieHLYi9k4Z-T7VASrctArWG-dAwps9M53fD51dZPSarGkEdG52RL8FFd8CMYB_a1fGaMMBXejZrYTqCIXaLxsnHR5tm7GnOV95qPcTPdRiNZbLR9tgmM5pwMxaDctobQA2JtqM4I1F5lef7X0I9itXsFeLQ_10yOMpNzDCbKjRhY3Y50n2IHk949qq0NIgAXCCHX0MQF344ae0E-wbSf5dDVgEDsSyFTl-Jicly1kVYB0eU3s2OsSUlxkTuglO-CmnO4D8vpQGwJELrh9ilmX42CZjZoB8XD44tLsTBfbdWFm0gqOIbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محکم تر بززززن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66505" target="_blank">📅 18:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66504">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4b87f1a5b.mp4?token=S8L27DTXfSs2VUUThUyDecSSQWKkqaY9YjbAxo2dKy2niCmgYCcoI_OfXBfdyLBtiKDF_BR4JhPhjesrxpqa4eS5Hs-CSAhFdpMODo-M4tsU5NYDZ6Lo2Ef-4Ipod3oU9F14ece2wkzgFEhnKUP5hFYxP_R-XqA523orUjZNEUkK3fXp9vTPe0I_OCzy-LWd-XUSpsTZA98h68O2BprmyVGVbrW24smUmOXtHDTZstpong1qpvRYH2QDywmGAUtPKryyGv00MIeG3bTg4Xy2CftrTc210Yn-k1fuzAYUjusAWZtycy6KfBgfZNrhSFnWAo8uJSz3987u_MPNeZ62IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4b87f1a5b.mp4?token=S8L27DTXfSs2VUUThUyDecSSQWKkqaY9YjbAxo2dKy2niCmgYCcoI_OfXBfdyLBtiKDF_BR4JhPhjesrxpqa4eS5Hs-CSAhFdpMODo-M4tsU5NYDZ6Lo2Ef-4Ipod3oU9F14ece2wkzgFEhnKUP5hFYxP_R-XqA523orUjZNEUkK3fXp9vTPe0I_OCzy-LWd-XUSpsTZA98h68O2BprmyVGVbrW24smUmOXtHDTZstpong1qpvRYH2QDywmGAUtPKryyGv00MIeG3bTg4Xy2CftrTc210Yn-k1fuzAYUjusAWZtycy6KfBgfZNrhSFnWAo8uJSz3987u_MPNeZ62IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از لحظه سوخت‌گیری جت های جنگنده F16در حین انجام عملیات گشت زنی بر فراز خاورمیانه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66504" target="_blank">📅 17:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66503">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3273d3f5c.mp4?token=IiuT9K_cRo98kxFs9zR1sNaEkPUEVsOEtxq02tlJrh-qgt6ebIQluwNiP0scAi81dilrWmOC4OZ6lPN-l84pMZTdPBEW8cp02isfzEeceTlbJEi8kKekbDjFO4V_N1R0OKk5rEQg3tQUWoBLBbZDQul6kN_-BCQWFctsU-nwnGuWOYQsfWqItDL2hUS2G-LKtmQKAhukQxzqcrSFZui6VUrGcsGKADTFHi6ooL5G7EKIqU1oZ4m5z4ivEdBwKIxWkmPjotii3kc03TfCVuJYsHI1tq4_6eLiEgRzb_kr-2wZCcDDRmBjMv-zxWEKxz38apLE-crFDgIcb9v_LSPq2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3273d3f5c.mp4?token=IiuT9K_cRo98kxFs9zR1sNaEkPUEVsOEtxq02tlJrh-qgt6ebIQluwNiP0scAi81dilrWmOC4OZ6lPN-l84pMZTdPBEW8cp02isfzEeceTlbJEi8kKekbDjFO4V_N1R0OKk5rEQg3tQUWoBLBbZDQul6kN_-BCQWFctsU-nwnGuWOYQsfWqItDL2hUS2G-LKtmQKAhukQxzqcrSFZui6VUrGcsGKADTFHi6ooL5G7EKIqU1oZ4m5z4ivEdBwKIxWkmPjotii3kc03TfCVuJYsHI1tq4_6eLiEgRzb_kr-2wZCcDDRmBjMv-zxWEKxz38apLE-crFDgIcb9v_LSPq2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ بعد از نشست G7 پشت سر جرجیا ملونی نخست وزیر ایتالیا گفته:
این زن همش التماس میکرد باهاش عکس بگیرم. حالا جرجیا در جوابش گفته:دروغه، شوکه شده‌‌م. نمی‌دونم چرا ترامپ با متحدانش این‌طور رفتار می‌کنه؟
ولی یک چیز رو به خاطر داشته باش: من و ایتالیا هرگز التماس نمی‌کنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66503" target="_blank">📅 17:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66502">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
سخنگوی ارتش اسرائیل:
منطقه امنیتی در جنوب لبنان ۱۰ کیلومتر امتداد دارد و ما به تقویت نیروهای خود در آنجا ادامه خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66502" target="_blank">📅 16:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66501">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPz4AD9KEgJ4QP2sbpbDgJBjwg6dx2KD5s07ZIBRQVU4FB59VXvCio6MjZvPhqmSPh7KJD4d1fCb0vFatMp217EfNG0o3YKLfpYOZWShwNsXRKaCOpCAoOu0YJQdBYHnmxA6EAjpUyALoHmYcWmN1pURG4bR5rtV2Yhnc_s05y-ddWS8qajsl3PIfO5j1HbBNahaGQqRbQW40pWRpC_NW1tohKXz65A96N1uv36ljpNOQ_GojYXdWWkvcBwyPWK24VF0KnxVh1alD1-CrQQ_bisig9jBCk0_mB5YB6OOQxy0EHE-7Lqx9Hyo4c53QWGfm5y3YHrVbjPcfVQ5YJ0ALw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اتاق جنگ اسرائیل:
اسرائیل و حزب‌الله به توافق آتش‌بس جدیدی دست یافته‌اند. حزب‌الله از توقف بمباران اسرائیل و پایبندی به توافق‌های آتش‌بس قبلی خودداری کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66501" target="_blank">📅 16:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66500">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvdYgGTid9qFRtM6gDI00Qd_1Y1THq6_n_enVvSywf-CtDQtokvCEU9c3WVcLAuxFlPT55Kd9rQKNiOrWnx0ajTKWt3ucvSZuGi56uJ2dUUsmLAYI4kUR_ka1NrbgOQS92oqZGPVDo9mgeJn2HUL4FLO_7-spGQRWiswRfYEyA005DqKESchi3nrPxb6dw53oleq3FxDJIi9KYhVj-2VrwZhI3eYlxAE1rmJ_4NaUd3rpwYzABCibgoPRsd1fq8sfpJDIs1BeDkFBFA_iPEbF5YloYzUQN9nj1CWIvFCZLjY75_a9yyK5vkm2Ht5EPnt_E_4Jj_dRcnyPf-q0nZfRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:
یک مقام ارشد آمریکایی به من گفت: اسرائیل و حزب‌الله بر سر آتش‌بس مجدد از ساعت ۴ بعد از ظهر به وقت اسرائیل توافق کرده‌اند. این توافق جدید با میانجیگری آمریکا و قطر پس از مذاکرات با اسرائیل و ایران حاصل شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66500" target="_blank">📅 16:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66499">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5NCQHU0gKTAeTf6aoIzi-LQbLyd4SCqJuLgBYh-dRPY_arGIeXBgsLTqbV26cbCv7HYt7i1SNcoq7cDfKmpM7J_PX0Y8jUHvKNlBuFH6RzwriGjA1sNSgffqs5aA8vSLwQcNe_RnY-EUmtbPcoRdUIP3p4pvUegQ3nZ3BLMkq61P8g8LMOvTN7E1iIm6KDY2zxpk_ekoS6vCMm_kH4qdnHQ6KokcdjNd8EYYQbZVJ8RNMc2m3QexLus0-pAz1a-8P8VFvm6SQXjb0UPhsmav1egQ4KQ44bNP-PNKEjg3DiVQ9OADIMZAuU8Jy-uumxE-QKCw_8z2bSpRc5dtKjiZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما از روی ناچاری ملاقات نکردیم، ایران این کار را کرد. آنها کارشان تمام است! ما 60 روز را بازی خواهیم کرد. آنها نه پولی می‌گیرند، نه ده سنت!
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66499" target="_blank">📅 16:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66498">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALlj2HY5P4vJJAiZ0CoK8K_hQuVVa6mGtL7c0AjcFANbffyZHiNS6GENKG4XEXv7Q-518M2_P7HTys0c8U6L5GqTlgLZDdD_S8iRrvpBFSYXh_nex3fDOwJC99-fRHwpQK6bF8M6_cPGjerDk9575u_wwLrzAmdctE9xVWNy6h_QGLHvStmxW6doQ2RJJ13kN1MOG2uaBgqYR7cymZ1EgpbIKpAe67Xp9tPQpzpjF_fLtdBdOxuMqAqVnayeQv6c2k-7fy78Ro2A9fb3-Gx8sTkfZ01jKujz_Tei5WRiToYJ-8LL5jgg3RiCrzYRZnnbAU3HP9yxK2B8iA4WVq149A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
این جنگ ایران را تضعیف کرده است! ایران دیگر نه نیروی هوایی دارد، نه نیروی دریایی، نه تجهیزات پدافند هوایی، نه رادار، و تقریباً هیچ چیز دیگری. با این حال، دموکرات‌ها می‌گویند ایران اکنون نسبت به چهار ماه پیش وضعیت بهتری دارد.
می‌توانید تصور کنید که کسی چنین حرفی بزند و از آن جان سالم به در ببرد؟ بعضی‌ها واقعاً تا چه حد می‌توانند احمق باشند؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66498" target="_blank">📅 16:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66497">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
‏اسماعیل بقایی سخنگوی وزارت خارجه:
آمریکا مسئول حملات اسرائیل به لبنان است. جمهوری اسلامی همه تدابیر لازم را برای صیانت از منافع، امنیت و حقوق خود و متحدانش اتخاذ می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66497" target="_blank">📅 16:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66496">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIHlr2HSB8US79RPb3d_UkSKAQVDrTz3mGhUr9TBUqrnR9ZxHc6cP2fmbxtjglg5BQ2W8qbTwl8Rg3NCiFFpbCx6MZLostuxSDgVgm5CxwDUKum9mnxQQacjkjHmU_mnDE_8y7gjnVzyasehL8HgpZgQk8s2qNXM0rQsUPpVE7s90ZZFPFARWjD2pK1sXJMdj1tArlVGSOfkf4sNHdB7NDWL6ZWrULpVH4VEbAvcEf43Xse8pHKIt1KmesKzNh6HKPyGZD1NFxy0opjWI4H1wTbjXoY3h7N9eiM1OCuMONAp-SoHE9o24G30GT0nPzvTVvDwVNqpyzAqLuKb-djp1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اینفوگرافی خدمات فعال‌شده پس از رفع اختلال فنی</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66496" target="_blank">📅 16:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66495">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cec2c7bdfe.mp4?token=gRDbR22oHuzDClWHnRGNLJ5qs8g4HqzHu4WyfR8wr00awEKGmCsG7QLkXsCl6xk0HNwkD4dkaYzKYb--LTL_Suaj9IHGJUFgCP71ZO9jolMG5CcE_-uVmjN9NhFm0O3AFbxNKnjkMo3dZsGqupx6iAt5diVPUuQHchGnultNKE4i9WZw5QlBUZbS3H7ida40cI1gYsgT3dtOBUILePGCxgtSQP1PEkdud6HYF1lPxmDvIRz6kYHCxaIQjWR0YNFQ5VHHZtky3n-hHx9VPtr-7Zq8I_U1kdum37yLfyChpmhDoz-rfsNbZx1V8oRntW-ihBe01sV97PMXOmQR23_J1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cec2c7bdfe.mp4?token=gRDbR22oHuzDClWHnRGNLJ5qs8g4HqzHu4WyfR8wr00awEKGmCsG7QLkXsCl6xk0HNwkD4dkaYzKYb--LTL_Suaj9IHGJUFgCP71ZO9jolMG5CcE_-uVmjN9NhFm0O3AFbxNKnjkMo3dZsGqupx6iAt5diVPUuQHchGnultNKE4i9WZw5QlBUZbS3H7ida40cI1gYsgT3dtOBUILePGCxgtSQP1PEkdud6HYF1lPxmDvIRz6kYHCxaIQjWR0YNFQ5VHHZtky3n-hHx9VPtr-7Zq8I_U1kdum37yLfyChpmhDoz-rfsNbZx1V8oRntW-ihBe01sV97PMXOmQR23_J1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران شهر نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66495" target="_blank">📅 15:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66494">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f017f858a.mp4?token=iuK-Md0Qjtcb91SQBPT1kk6OcyDBoal3CEdVs6sBjj3eqXdH1o6dSjhqURc6bCAAKna6mLwoestxH-CkSHQGLH-q7YTDqEtRNDTwQqqaLMBI0RrhsLW7PqBClRgXfds6wuwgYDcG1FptoIjrycQA15kxQobXsi9npYcTSeFGQ63HgTHoeHLlvAPs2H_usydWG4svt1MtPmA6gZTdF9tezST_qPjeAY0V8RidiELmfTwKQw7c-vYd13EyRf7rOc2oQTTwIrhaT1Ua-8kXGtUSvfN2jij-q0Q4vYqdXJ541ZwICvZgeWTRiQ2krWaJrRiKIa2fIlqVh7WxZxO6Czn0iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f017f858a.mp4?token=iuK-Md0Qjtcb91SQBPT1kk6OcyDBoal3CEdVs6sBjj3eqXdH1o6dSjhqURc6bCAAKna6mLwoestxH-CkSHQGLH-q7YTDqEtRNDTwQqqaLMBI0RrhsLW7PqBClRgXfds6wuwgYDcG1FptoIjrycQA15kxQobXsi9npYcTSeFGQ63HgTHoeHLlvAPs2H_usydWG4svt1MtPmA6gZTdF9tezST_qPjeAY0V8RidiELmfTwKQw7c-vYd13EyRf7rOc2oQTTwIrhaT1Ua-8kXGtUSvfN2jij-q0Q4vYqdXJ541ZwICvZgeWTRiQ2krWaJrRiKIa2fIlqVh7WxZxO6Czn0iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آیا می‌توانید جلوی حملهٔ اسرائیل به لبنان را بگیرید؟
ترامپ: «بله. آن‌ها احترام زیادی برای من قائل هستند و هر چه بگویم انجام می‌دهند.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66494" target="_blank">📅 15:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66493">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66493" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66493" target="_blank">📅 15:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66492">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-JM18jZKYw8bS7yrMsI-1s6LDV11ZjqSwq_FvZKdP0yaPGNEg64thl1TqiLKe0DiiBjRT-sz7mT4NoJfM4ivIOBgDu06Z-s9gz18NdiekjtRqPwmH1ehll9T1zA_hQk5wL_iM7pCyYOkV02zlP0x86fft4XQfatYTU7FJoip03-FsHE-cnCDHMV0QEpUYqzrzC63TquyZ9oOdCGL6PdU3p6Dvbxc_xXM9orFvvO39O0Dysfg8LQN8est-6e_c0Q8qW_U8NiUXK7yD8gKqmmZ3h9FSJIUCGPEdj_JQcT1o9WIBlnTEJHW4Pdxpyk5V-0mx-vGdVqSyiZXoDYEaJVQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66492" target="_blank">📅 15:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66491">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vg8LPr1D_F0ap7M953pBqYC4euSemwyb9arTITuQVNb7adJ2JFzH1f5JD62g9OaDzYYmjzhNTRnr-4RdGppE12rOiS8y1x1ol21k6PcUYXN8Aw3t-9LOU5DXxoDE6ofEqcezKwqucoerR9kxJ9goy0EOh_rrzK9keiEfZ0bT_rJPBzBWACRK3HIXTYwyfeTKtYQqYLQAWrqjnglCxbSE6qhoGol5KQW8IfO4CJxMkikNETu8i9sunTs1iMDVzxSlyDJVDWAy0Zrm8jhAbteMS6qJjrpVTz1LumyZLDoAvusPlY--2pB3sa4BWR7oDrZyDEKwlpSKb_EvZs6z3meaLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسرائیل به فارسی؛نخست وزیر نتانیاهو:
پس از حمله جنایتکارانه حزب‌الله که نقض آشکار آتش‌بس است، دیشب به ارتش اسرائیل دستور دادم که با قدرت به حزب‌الله حمله کند.
ارتش اسرائیل به بیش از ۸۰ هدف تروریستی حمله کرد و ده‌ها تروریست را از بین برد. متعاقباً، ارتش اسرائیل امروز صبح به مقر حزب‌الله در بقاع حمله کرد.
امروز صبح با وزیر دفاع و رئیس ستاد کل، ارزیابی وضعیت را انجام دادم.
دستور من واضح است: اسرائیل حمله به سربازان یا خاک ما را تحمل نخواهد کرد و بهای بسیار سنگینی را برای این حملات از حزب‌الله خواهد گرفت.
ارتش اسرائیل برای خنثی کردن هرگونه تهدیدی علیه نیروها و خاک ما اقدام خواهد کرد.
همانطور که به صراحت تاکید کردم: اسرائیل تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان باقی خواهد ماند تا از شهرهای شمالی محافظت کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66491" target="_blank">📅 15:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66490">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc6524eaa.mp4?token=sSfoBc1Sb3WvvltSE0CDotog8j7nzCEp3_YrZMY2ieA4tveWRbeJF29kbY9e9cZWV9_fw2JVTtFnOv5lKkhz6Mh8ROXhabHdV7xYDcO82l3hQO6dEhKLYaMgXi_tjAq9jskJj7kuo_ZEZ6-325nPD9WzUWx75QvJv3jCRyNFC_M9t6QvqXASoQe7eNh94rFfhMBU8tahZvnTD1d4GYkP_zG47o_cwtGbnhNzyu2Z61zd6-52oxU4dzfB5N2zm1ZvSP2ag6QF1gm_PZokgq842fgJUSW5bZTStkFqY-ECXpRGgb_5jxsHatwiiKPvwCn9BK4lMXCcgv3DR2ucHIh_cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc6524eaa.mp4?token=sSfoBc1Sb3WvvltSE0CDotog8j7nzCEp3_YrZMY2ieA4tveWRbeJF29kbY9e9cZWV9_fw2JVTtFnOv5lKkhz6Mh8ROXhabHdV7xYDcO82l3hQO6dEhKLYaMgXi_tjAq9jskJj7kuo_ZEZ6-325nPD9WzUWx75QvJv3jCRyNFC_M9t6QvqXASoQe7eNh94rFfhMBU8tahZvnTD1d4GYkP_zG47o_cwtGbnhNzyu2Z61zd6-52oxU4dzfB5N2zm1ZvSP2ag6QF1gm_PZokgq842fgJUSW5bZTStkFqY-ECXpRGgb_5jxsHatwiiKPvwCn9BK4lMXCcgv3DR2ucHIh_cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضائیان: ما در مقابل نیوزیلند لایق برد بودیم/ اگر گل اول را می‌زدیم شرایط عوض می‌شد. امیدوارم خدا کمک کند و موفق شویم.  @News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66490" target="_blank">📅 15:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66489">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71570c04a1.mp4?token=L-lzlKTakfakcIk_1XcRjbWoQYU9SeJnsuBx8OyQH4RwH4lbNQz2qVTxOfjYXTv2p9BUwLY_oOinZgxOET_4fu9tQO91Qvn13fxAl6GJEoGSMPKpcZBbhL6knPs3oFFl4sUeuke2sqZjcp3M3pNgILmdnXXzUb3bwf2YiLyk32xYcQer0xyJVbsHUtk5mVpLoUzsmEgEmeTgM3UyP3Zd7iFiMoVhUmEFOSo4kxrgNqbEBee7wuhfze0868Wp819TFDQ51FJLYO17JzpM51_JpdFtBd1L80VeeVaY6eQpi92U_UsqYK3ccXE1gOLZOEqsDL14Au10I4io3x-hdpbOtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71570c04a1.mp4?token=L-lzlKTakfakcIk_1XcRjbWoQYU9SeJnsuBx8OyQH4RwH4lbNQz2qVTxOfjYXTv2p9BUwLY_oOinZgxOET_4fu9tQO91Qvn13fxAl6GJEoGSMPKpcZBbhL6knPs3oFFl4sUeuke2sqZjcp3M3pNgILmdnXXzUb3bwf2YiLyk32xYcQer0xyJVbsHUtk5mVpLoUzsmEgEmeTgM3UyP3Zd7iFiMoVhUmEFOSo4kxrgNqbEBee7wuhfze0868Wp819TFDQ51FJLYO17JzpM51_JpdFtBd1L80VeeVaY6eQpi92U_UsqYK3ccXE1gOLZOEqsDL14Au10I4io3x-hdpbOtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضائیان: ما در مقابل نیوزیلند لایق برد بودیم/ اگر گل اول را می‌زدیم شرایط عوض می‌شد. امیدوارم خدا کمک کند و موفق شویم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66489" target="_blank">📅 15:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66488">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3bba52e8.mp4?token=thBD3W5jAP6as27clmzxM-6D9duau-j9iU5WvCFzQkVJO8K-O1_b9EKAXweFCgGj9zCRO0d7X9Kn6hGUCr6Ycx23nf6V92uHKFQ2IiMGvKNcTnb4bF1pPh5JtLzmBNwOZ8Kq0_7FSgCuHKk5WBf9BJK3rhL7OhR5KVWDzGigdfA2MkY_KeorrmP1lchXgO4F5TbXfj-8YagqmoDsED0DZro0qt3mFyqfVD7JQtz0mhC8jcqixk2jhqPil95kGulGylj9L0XtueLAqPSoAGJQ1e3DpgWHMZxWAwXXgIrGbNYTombO1Gee6_KCPsXNaj5ERtX_SDy4g8fXauF7xQcPBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3bba52e8.mp4?token=thBD3W5jAP6as27clmzxM-6D9duau-j9iU5WvCFzQkVJO8K-O1_b9EKAXweFCgGj9zCRO0d7X9Kn6hGUCr6Ycx23nf6V92uHKFQ2IiMGvKNcTnb4bF1pPh5JtLzmBNwOZ8Kq0_7FSgCuHKk5WBf9BJK3rhL7OhR5KVWDzGigdfA2MkY_KeorrmP1lchXgO4F5TbXfj-8YagqmoDsED0DZro0qt3mFyqfVD7JQtz0mhC8jcqixk2jhqPil95kGulGylj9L0XtueLAqPSoAGJQ1e3DpgWHMZxWAwXXgIrGbNYTombO1Gee6_KCPsXNaj5ERtX_SDy4g8fXauF7xQcPBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
هم‌اکنون سپاه در بیسیم کانال ۱۶ دریایی.
“از آنجا که خروج اسرائیل از لبنان و لغو کامل محاصره دریایی و خروج نیروهای تروریستی آمریکایی از خلیج فارس و منطقه از جمله شرایط اصلی توافق بین ایران و ایالات متحده است. تنگه هرمز تا زمان تحقق این دو شرط بسته خواهد ماند، به همه کشتی‌ها دستور داده شده برای امنیت و سلامت خود به تنگه هرمز نزدیک نشود، هر شناوری که از این دستور سرپیچی کند مورد هدف قرار خواهد گرفت.”
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66488" target="_blank">📅 14:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66487">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
مرندی عضو تیم مذاکرات :
ترامپ بار دیگر ثابت کرد به تعهداتش پایبند نیست.
رژیم صهیونیستی مجازات میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66487" target="_blank">📅 14:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66485">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">شعارهای دیشب مداح حکومتی در مراسم محرم
😐
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66485" target="_blank">📅 14:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66484">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddac5fcdb8.mp4?token=d3aUTFl_K3dz1Rd0F_rTEgHqJA2eRMP17JfbgUhW1WInF5O5M9Hd0hjgDxazUQI5E3uIJgqZpve7MrWIYFjEMiK0DjtSk2cEM6vrodvTlIvJlnRLBJ7BGAzYcyzaUbWyGNLRbRBx6j0Do-3Uje1uRWG0FOu4UBoZx5J-MVbUf5JJG5gDnQdkugrzBZkrCqooHaYaVaKv_vrh1ttHq1oBR6aoo1VvyK7jIxNbFULY4LxiNkjrHHiTVQzDrhNRyJ82XNyo91dj_CJzyasnAePX0iLnW-bumdlvLlyY2yQiLQm9Z_LJ1s0Y-KH1hIvYdoeGTgSog0p7tjntflIrzwhtTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddac5fcdb8.mp4?token=d3aUTFl_K3dz1Rd0F_rTEgHqJA2eRMP17JfbgUhW1WInF5O5M9Hd0hjgDxazUQI5E3uIJgqZpve7MrWIYFjEMiK0DjtSk2cEM6vrodvTlIvJlnRLBJ7BGAzYcyzaUbWyGNLRbRBx6j0Do-3Uje1uRWG0FOu4UBoZx5J-MVbUf5JJG5gDnQdkugrzBZkrCqooHaYaVaKv_vrh1ttHq1oBR6aoo1VvyK7jIxNbFULY4LxiNkjrHHiTVQzDrhNRyJ82XNyo91dj_CJzyasnAePX0iLnW-bumdlvLlyY2yQiLQm9Z_LJ1s0Y-KH1hIvYdoeGTgSog0p7tjntflIrzwhtTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
املاکی در مراسم اعطای مدال هرکاری کرد نتونست گیره مدال رو بندازه داخل و گفت میخوام یک مدل دیگه برات ببندم و مدال رو گره زد و نزدیک بود طرف رو خفه کنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66484" target="_blank">📅 13:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66483">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
‼️
وزیر خارجه پاکستان: مذاکرات سوئیس بدلیل مشغله کاری مسئولان ایرانی در ایام محرم به تعویق افتاد
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66483" target="_blank">📅 13:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66482">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd02588050.mp4?token=jcF2Tki54ZzcPZfOUdnmUlUYGX0hTMq74HHj4UpgIbpg7BraJM7BusYgkqA_uwAUOTPljXBrnYjygReOgKf64n5kTvCud_Er3tvQhENkcbEjwagtkAFTCww7yz190oyF8FMgFEWuI6umRL6i0Qu1uqJu6UvU2Pmnruqx4f3LZH4gv42mDx51aF0K3iNRIUgo0c9GDF4ninlNhOWcZhR_8mY5ciz9Ps81wT9Z7Sio3bvjmmR3qUKrl4SVA228oWoGRoQBgtxSYrYebHoRWO8P7gNVJJw4o4jAdqyFQSx5URhG7iW5Cy3fI-dexOXgYJjv046ZPo6tnXhg7WNOqez4BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd02588050.mp4?token=jcF2Tki54ZzcPZfOUdnmUlUYGX0hTMq74HHj4UpgIbpg7BraJM7BusYgkqA_uwAUOTPljXBrnYjygReOgKf64n5kTvCud_Er3tvQhENkcbEjwagtkAFTCww7yz190oyF8FMgFEWuI6umRL6i0Qu1uqJu6UvU2Pmnruqx4f3LZH4gv42mDx51aF0K3iNRIUgo0c9GDF4ninlNhOWcZhR_8mY5ciz9Ps81wT9Z7Sio3bvjmmR3qUKrl4SVA228oWoGRoQBgtxSYrYebHoRWO8P7gNVJJw4o4jAdqyFQSx5URhG7iW5Cy3fI-dexOXgYJjv046ZPo6tnXhg7WNOqez4BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تلاش سربازان روس برای سرنگونی پهبادها
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66482" target="_blank">📅 13:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66481">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98d70873ad.mp4?token=XvLtwYGWXt6dqwrne5DFdKhx2ILaht_SYBUlb60FO6fRjGi9bEXMRRjGfWlWFvHBOuYIDxue8Cnh7OqHeQIfQpV2KYCeis3kJmQBpmiQyjxTGxi_WJXw7pmD9OTEoMH-98ddCttqtyT8q0SOhiGEfZXlu_WyMNdNMqbTtVyFChUfe3iE2Su6_y39CznM6dmbLy5wQkM2RQtFTVvFi7_zJkKiFxf34FJM5RPeXZbAX7MDrxHz9ltnvg1IiFzT_s3xag8AaPMi3_nybBc7Izv5A2WctKzG2gfr3cEAy-MN7uB94Yq-4YY0mVGlzw6yyDoflgofJlbvwi_TJsho9d317Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98d70873ad.mp4?token=XvLtwYGWXt6dqwrne5DFdKhx2ILaht_SYBUlb60FO6fRjGi9bEXMRRjGfWlWFvHBOuYIDxue8Cnh7OqHeQIfQpV2KYCeis3kJmQBpmiQyjxTGxi_WJXw7pmD9OTEoMH-98ddCttqtyT8q0SOhiGEfZXlu_WyMNdNMqbTtVyFChUfe3iE2Su6_y39CznM6dmbLy5wQkM2RQtFTVvFi7_zJkKiFxf34FJM5RPeXZbAX7MDrxHz9ltnvg1IiFzT_s3xag8AaPMi3_nybBc7Izv5A2WctKzG2gfr3cEAy-MN7uB94Yq-4YY0mVGlzw6yyDoflgofJlbvwi_TJsho9d317Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل کاتز، وزیر دفاع اسرائیل، درباره سوریه:
ما آنجا می‌جنگیم. ما به الجولانی نیاز نداریم. الجولانی، تروریست کت و شلواری، نیازی ندارد که بیاید و به ما کمک کند.
ما سوریه را خوب می‌شناسیم. او قرار نیست در لبنان به ما کمک کند. او باید در سوریه بماند، در کار ما دخالت نکند و ما را مجبور به دخالت در کار خود نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66481" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66480">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e15d1aff21.mp4?token=GuuqfKnbPL74ny7sj1r9zmkTVwWzT8asMuqIAMgdEWVKpmX6mvddEZCDeAzLMPadDCrjEpI_dzsGj5alvr4M-s7_P_fcoWblYhrsz2v6plizDcYfJPBGm8UpeXARjCwRc0D-iAXxe31Vx5i9jO2IHCxipA-tdkEPZANmobwCBfqbfU8MhAdLwmjrGWUR1hFAGx4deOZRF4PPre4H1EBdfD1XWNSkUC_TVU3rixGEPM1tNw3tw1CJ0vrRrB1WHc3Ufgx3ybzpMN7TJByn9jYeIc5FiUNK4SqmHG9bGXE8pKQEqtwKD-Gszt3zprEHTUF1fBnpQwGXhQ8wsyAcu5nVOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e15d1aff21.mp4?token=GuuqfKnbPL74ny7sj1r9zmkTVwWzT8asMuqIAMgdEWVKpmX6mvddEZCDeAzLMPadDCrjEpI_dzsGj5alvr4M-s7_P_fcoWblYhrsz2v6plizDcYfJPBGm8UpeXARjCwRc0D-iAXxe31Vx5i9jO2IHCxipA-tdkEPZANmobwCBfqbfU8MhAdLwmjrGWUR1hFAGx4deOZRF4PPre4H1EBdfD1XWNSkUC_TVU3rixGEPM1tNw3tw1CJ0vrRrB1WHc3Ufgx3ybzpMN7TJByn9jYeIc5FiUNK4SqmHG9bGXE8pKQEqtwKD-Gszt3zprEHTUF1fBnpQwGXhQ8wsyAcu5nVOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
حملات گسترده ارتش اسرائیل به مواضع حزب‌الله
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66480" target="_blank">📅 12:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66479">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae8db95bdf.mp4?token=AyDP9QKDmNz6FOaxSkU1AJe8v6AJnbygZRk1K9H8BA1Ixxa1BQLtt0njND87PxxDY8USKLxH20MFneo9KTugHDx8BQnmmnb2dmR8JWlfILVBNcUIT_AjFRKYO0t5pNyPEnPYOtpHiFT0lMtUr5gtfzl2_BgDxnVkbrFwyjw5PbK1k9ncYIq2G4aY9_-dXjSNngrYmX8IHHMvuZGT6ZuT87oA9b_28Ald_0bjbSpkis4tLRsz8LGlEbDNsRTY2T_qakzLRjt0aMAxcJPniQWWpt-FIe8q_0zhVvPbAIK6B4VVKsTqvSminQJn6h1CKi5yt0JRBhUwPx7hUfG1XfxWeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae8db95bdf.mp4?token=AyDP9QKDmNz6FOaxSkU1AJe8v6AJnbygZRk1K9H8BA1Ixxa1BQLtt0njND87PxxDY8USKLxH20MFneo9KTugHDx8BQnmmnb2dmR8JWlfILVBNcUIT_AjFRKYO0t5pNyPEnPYOtpHiFT0lMtUr5gtfzl2_BgDxnVkbrFwyjw5PbK1k9ncYIq2G4aY9_-dXjSNngrYmX8IHHMvuZGT6ZuT87oA9b_28Ald_0bjbSpkis4tLRsz8LGlEbDNsRTY2T_qakzLRjt0aMAxcJPniQWWpt-FIe8q_0zhVvPbAIK6B4VVKsTqvSminQJn6h1CKi5yt0JRBhUwPx7hUfG1XfxWeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز، وزیر دفاع اسرائیل:
ارتش اسرائیل باید در آن سوی مرز، فراتر از مرز، از کشور اسرائیل در برابر سازمان‌های جهادی در لبنان، سوریه و غزه دفاع کند.
ما از «مناطق امنیتی» حرکت نخواهیم کرد، نه در سوریه، نه در غزه و نه در لبنان.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66479" target="_blank">📅 12:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66478">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwSRuhPBm0AmfGenSpObLZ0-hhbpjjuENGP1356Uk1vS8nF2FETxHAPM9GOgZ4TIIcQv6oIL8FhZlExB4S3E_O4Pls1iQ4PoTSKw9omhDhHrPhnNMrOkzh7g5I0Xh3ec-A28PJq6LaUjiPhpscFIBR5zEke1A6JMRPoc_-OUkBF6FMPxYBnreUZjmSxJyD8TLNV-vdjXl1BA1fSUkiUF0d-YEWh_ATAOZ_vlxlkXQxzen1gBP4C5nxv35FRqyFj8mQNopzyEwlCrhAacrdNMX0Bfg3z24L-iu6qPRH3la-jpgCIg6_ikPmyGbMa4gdhLeBbLHfS463g0xIQyFvOrYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
گوش‌بفرمانیم، وظیفهٔ محول‌شده به ما توسط مقام معظم رهبری پیگیری تحقق شروط و بندهای تفاهم است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66478" target="_blank">📅 12:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66477">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c84fc04d4.mp4?token=AjftUWqtZ6dbcyIynsI2omPbhyT4mO_7_8_hw-knY7Yg7L4UQ96p4cJBULi-6Lp-Sb2AdmUBmEOMTlakGOoT9EvOY7go4WyOcbXli0bL8q0UakSf2twueHBo9mv7iu91DMX18XRz5SRDWj6q3qQ6obbX50pSwqAJ63pIWhjMukYTrl-BRH8DVQXSij6sZ9XKUtuG27S26HK8oef5iB-OLPDEaW9-WTccq0QCHUinuiE5GfUndou1I9o7oRntbCaSJiq2hWECbDzBaZ8Hb2dOWTLqMZueQL9lDSbum_6sFIOuP-noPW9Z_H4_J22rzZOKI1_vtlEMwCOBurcIeEpRpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c84fc04d4.mp4?token=AjftUWqtZ6dbcyIynsI2omPbhyT4mO_7_8_hw-knY7Yg7L4UQ96p4cJBULi-6Lp-Sb2AdmUBmEOMTlakGOoT9EvOY7go4WyOcbXli0bL8q0UakSf2twueHBo9mv7iu91DMX18XRz5SRDWj6q3qQ6obbX50pSwqAJ63pIWhjMukYTrl-BRH8DVQXSij6sZ9XKUtuG27S26HK8oef5iB-OLPDEaW9-WTccq0QCHUinuiE5GfUndou1I9o7oRntbCaSJiq2hWECbDzBaZ8Hb2dOWTLqMZueQL9lDSbum_6sFIOuP-noPW9Z_H4_J22rzZOKI1_vtlEMwCOBurcIeEpRpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
بمباران شدید نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66477" target="_blank">📅 12:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66476">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99cbfc5535.mp4?token=pZrODkL5_a4NOrLLdGoyFu2SmI4hrde35Fx9YmGMxyFzamHbzM5TUShLGrpiSS5I7XYuQC11VjKrLiKVWaoPsmwW6291atbto6hniMZPzvjlkV1DZm0WBICPlUba4sQE_MLgcP2IIr0SY57rLQtnW9LaiGcJpulpbJqhZ8yM69BK6LIzmdStwAseDCtxwKRRRNK_Jq4T-HVjgmxAaz0VtVQ96S6VHcET-I3L-DlOfd2EQkeGtjyVfkQlOoX3oXOaxZAVNxziHTBuiGkxS_aQ3R2YuMXtfnIdRryYscyGOdhTVS95s_tnV6hb_hpCadUwmEwmXfiTY7ZPV8EeLGP3Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99cbfc5535.mp4?token=pZrODkL5_a4NOrLLdGoyFu2SmI4hrde35Fx9YmGMxyFzamHbzM5TUShLGrpiSS5I7XYuQC11VjKrLiKVWaoPsmwW6291atbto6hniMZPzvjlkV1DZm0WBICPlUba4sQE_MLgcP2IIr0SY57rLQtnW9LaiGcJpulpbJqhZ8yM69BK6LIzmdStwAseDCtxwKRRRNK_Jq4T-HVjgmxAaz0VtVQ96S6VHcET-I3L-DlOfd2EQkeGtjyVfkQlOoX3oXOaxZAVNxziHTBuiGkxS_aQ3R2YuMXtfnIdRryYscyGOdhTVS95s_tnV6hb_hpCadUwmEwmXfiTY7ZPV8EeLGP3Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل کاتس، وزیر جنگ اسرائیل:«حتی اگر ترامپ چیز دیگری بگوید، هیچ‌کس نمی‌تواند به ما بگوید چه کار کنیم و ما قبلاً این را ثابت کرده‌ایم.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66476" target="_blank">📅 12:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66474">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba86fa7681.mp4?token=LStF7FJhwsQOWBZEkRF8iRCBNU3RgiBJZf2_r9Wiu8muzoHrvGncO14-9GuhDWIILXNVH004zA844DyE9XN5_O9qNOmuYKd5BQ2ODaW7HQ5EW4wvTG37JZyMRpbVFplGP2rP6rCxUqtZvzXwtL5R80sDKkpSZBAfLaaiNIqkOZqa-FSR_5C3sSHhXJ0Od0mCr8i2d1ibaSGwZMWrVj5E0c96O6kfdtfP8k39Kwh-B-IfaKw_VUZWEeshvYp_EHbwaXsqVqtvyfKobrfHUMVMvLu4qYFZe7ruRW1eb1qyGL8BXBWywwFFVX4v25EraAJ9pa7gF5zBsCQ97QyOMEFX_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba86fa7681.mp4?token=LStF7FJhwsQOWBZEkRF8iRCBNU3RgiBJZf2_r9Wiu8muzoHrvGncO14-9GuhDWIILXNVH004zA844DyE9XN5_O9qNOmuYKd5BQ2ODaW7HQ5EW4wvTG37JZyMRpbVFplGP2rP6rCxUqtZvzXwtL5R80sDKkpSZBAfLaaiNIqkOZqa-FSR_5C3sSHhXJ0Od0mCr8i2d1ibaSGwZMWrVj5E0c96O6kfdtfP8k39Kwh-B-IfaKw_VUZWEeshvYp_EHbwaXsqVqtvyfKobrfHUMVMvLu4qYFZe7ruRW1eb1qyGL8BXBWywwFFVX4v25EraAJ9pa7gF5zBsCQ97QyOMEFX_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی شبا میری اعتراضات و روزا میری راهپیمایی:
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66474" target="_blank">📅 12:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66473">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc0be5a6ce.mp4?token=sbHBH2aXd3VeleKV5QpdZTC8X6CbYh32q7Bt0gy4cJVocgFWDBkfrvpYu2Lip4G0Xqek6LbuIdMkx-ibY98UMyk9vFEenjAklxB0IZvhWj365a1oef9SI7vx87aU3okHRrGw8Ev2BLjdZT4IcXFUhzdv8gbKSlDsSCQErvgsN1Z12ruvMfsjlGiFD6K9c1oz_abha7lC3I7LAkyhrDiSzFDnckZKvBVxBK0EYS5CLk4PTAAv9dCsCxqK7ntN1JLCeFeIDGfkzaYEmKLk_NYEB1GkETWcPsMm2JALsLY-5F-3WGduQqAR92yk8AC7DCzN6fmpNNnqLbRDGhdwgcpVOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc0be5a6ce.mp4?token=sbHBH2aXd3VeleKV5QpdZTC8X6CbYh32q7Bt0gy4cJVocgFWDBkfrvpYu2Lip4G0Xqek6LbuIdMkx-ibY98UMyk9vFEenjAklxB0IZvhWj365a1oef9SI7vx87aU3okHRrGw8Ev2BLjdZT4IcXFUhzdv8gbKSlDsSCQErvgsN1Z12ruvMfsjlGiFD6K9c1oz_abha7lC3I7LAkyhrDiSzFDnckZKvBVxBK0EYS5CLk4PTAAv9dCsCxqK7ntN1JLCeFeIDGfkzaYEmKLk_NYEB1GkETWcPsMm2JALsLY-5F-3WGduQqAR92yk8AC7DCzN6fmpNNnqLbRDGhdwgcpVOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
نبوغ اوکراینی ها در شکار پهباد
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66473" target="_blank">📅 11:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66469">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CHAVNHZCtN-Kpd8GuWCILORG_AMv13X8k32njZIe6AdzaCA4H9UOb9tF_5NYn9fE-cO7rddio_7-eMCwOKxpc51oFQyISlUC8kL_R5cdArb8mJ8e5Zs14PAPCLPfa-mrEeIZ9QMoBKrvbFvOp8XKTlaG3WmfMQmtbnK27EexdcFkDYWMvWp7h07Qh3P7Q-GFYom9ZCEaRWFVBnaC8d5e8HYiubI0M6ICYfIz1Js5vVcKZ4P0tsyfXDKJSQUE_7MHK6GFjG7bL1BPUXJrpWPF5sCBNgd4ljOwRe4uYVaTWiE2SOwvR4eV27w8u-qJCL8yLJHKoZUqkrnuYvGha2Xj1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T720apePlZlhjF771v6HlWztcp8WXbJTRHT8VZ4fk-JhxIwzTiy2EgXhpAlD2rNdtlpH4_Zb6hH-UcODVfHjzrunCZ4lCMaABZYSeGKc6G14gmnsPmD0Y0ObWqDm17Xr4uQahHA5LH9shIX6OHe5A64sAnuiXZfd-L5s94sim73jlfuV7qwQhCHTmCjxpeZWAnuzRQREWDd9ngKoj9ZexijVkAwPd5nfgScLD6EYVCrOe_dIN8Qcs4ywMYZb3iQQLGljSn3iLYLaATkBka5xNTjlNFjTeOxQI5CGJLn08LV8IR6bVD08ut9KJKQyQlEhAnQs08Sw2bEDKcnvlkVU4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jaN8QogcTZz8hnRdtd-gbSuqxqxk2JfMjvGcq3Jh_xam2GvvaFHTfldWgskm0-WLyePAPYRotu8j5RJJtGm9_VpCsutJimqgV1tZbOc7AilqDQxkC0NBJR2LOJf2uswf_tcR2GxKzBJ6sbzlyqckst7OXGiZRbpVAUBTcXewmf4iH9KeoQ21Va2zmnOoG8GmRiTp7VFxlQOdRdWumj9BHY_wWb69DzB_oWoW61bg4AjzwOv-xNGRNBop9OGk4-yKCRXy-OzT_24l6OpquAYgND0oaWx45BLkU4MJSJX0BZ9stG9lkxsMEqT8pM1tnNq20rmOVJ2_LQaCZetIZQ8pXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cb0e601ac.mp4?token=Bc446_-D_CO_gNLl89K7HFh6PzIRdEHeK34M91xujHEK8wzUngHVl3rhCG162CteG3lcgEpFJ6tYppHI192dJjfvq7qpaJSI2toJVnypbQEDQTTnwXgTMuHOcjHy2xgp9k-U4llmiO4g20kPGRGb_e72ZGcDjcX7bogMw9u3aGlMHP1LAUa5_t-3HDDw5s9LqYOPxooaypzW3umNHa4mTnc57v_GDsMPyBFpIGIHNcHJOc_086RgnzDErkqy3Yo9eC5cQZ5UUeXo28p1wwEOmgHj21JC-7Jlk1m9TpQWWiKrl8RWJvV46s9h2X33PHnPTAZW1QOx0ArLfU9zUtQPPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cb0e601ac.mp4?token=Bc446_-D_CO_gNLl89K7HFh6PzIRdEHeK34M91xujHEK8wzUngHVl3rhCG162CteG3lcgEpFJ6tYppHI192dJjfvq7qpaJSI2toJVnypbQEDQTTnwXgTMuHOcjHy2xgp9k-U4llmiO4g20kPGRGb_e72ZGcDjcX7bogMw9u3aGlMHP1LAUa5_t-3HDDw5s9LqYOPxooaypzW3umNHa4mTnc57v_GDsMPyBFpIGIHNcHJOc_086RgnzDErkqy3Yo9eC5cQZ5UUeXo28p1wwEOmgHj21JC-7Jlk1m9TpQWWiKrl8RWJvV46s9h2X33PHnPTAZW1QOx0ArLfU9zUtQPPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حملات ارتش اسرائیل به نقاط مختلف در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66469" target="_blank">📅 11:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66468">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwAdNZq4HUELdabQdNrObpdVXYpxujTE62s7jQBQ-HHOyqYJubpzId6uwOc8H4dYktfRNA1_WefryOQCaR0d7qKwcKnmO8QjuOrcBYmmqvNylWSdFh5YAmSEl7G2bQ3CV9FxexshNRgfYRd9J60UGBEcCv4VHZS87C7lmeZ7d7LRQPD7zUsYBQBhga33sPubezizhv_ST2ZY8bLGlIWxWvJko4CoXgrAF7EFo7KLAPCulEmJtCR8TdrOctvgRhcfwGDwOsH7pejetzNRbWNrTuXd80u2iCpg7zNEdEIf3CmcgKQBe03AAHYa3PowyXdAVuQfOPp8bLeg8a8P2x4Fbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت ‏مسکو، روز ۱۵۷۶م عملیات نظامی ‌ویژه ۳ روزه پوتین در اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66468" target="_blank">📅 10:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66467">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7be955089.mp4?token=VH4yAe1B1EdocCP2wb1f591A52MthOzG7U5sTW0PGyWiNjXL6nJmF7sa4USBUBv69dHqIWzDGJTS-ytCdzfXe49e5elBN0K_4jbHoMSGtvoHhLvdSw403v6c6UqkcTVR9jvQRSJfKfJT0w1Z-0QlhLjYKgCYpaSrlURvzRoCCMaaNqc-SZTGlZiWQcd480aneft9D10MHmAew7cVP_mUZBiWF8hgOgBBtCbmHtI4p98VXTIcdn3jlFb2NcyVROjR2_Tbd-Vlh2V1N0DTNAwqRgKuN0XqYemaaqghtFyczBVu3eeaoBenakILNmoeQfpKgy_pu6NEK3xS07yxsIFFmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7be955089.mp4?token=VH4yAe1B1EdocCP2wb1f591A52MthOzG7U5sTW0PGyWiNjXL6nJmF7sa4USBUBv69dHqIWzDGJTS-ytCdzfXe49e5elBN0K_4jbHoMSGtvoHhLvdSw403v6c6UqkcTVR9jvQRSJfKfJT0w1Z-0QlhLjYKgCYpaSrlURvzRoCCMaaNqc-SZTGlZiWQcd480aneft9D10MHmAew7cVP_mUZBiWF8hgOgBBtCbmHtI4p98VXTIcdn3jlFb2NcyVROjR2_Tbd-Vlh2V1N0DTNAwqRgKuN0XqYemaaqghtFyczBVu3eeaoBenakILNmoeQfpKgy_pu6NEK3xS07yxsIFFmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری: شما گفته بودید که فقط تسلیم بی‌قیدوشرط را می‌خواهید. اما این تفاهم‌نامه شبیه تسلیم بی‌قیدوشرط به نظر نمی‌رسد.
ترامپ: خب، در واقع احتمالا تسلیم بی‌قیدوشرط است.
مجری: واقعا؟
ترامپ: من این‌طور فکر می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66467" target="_blank">📅 10:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66466">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/040ce8f378.mp4?token=SSoSdRqd3CoH8e3hn394VT-d4i9acdwQVEdbufn3ZHhgmJPTp0vdwTldqCI8qa1y897DS7huCIrD891bm6EAI-0WaBHoFVWKoKtBgmFFk-t9DgIOBgnFBFQOFTy8x47rCK46pe1pBr78zw7onxNLGzctayRYkzaevvap6-V4N9YT6exucYubx3XgG3j2wwayDz9biK_kzjQGLPm-5eBchZqor6Ik6zHubhs5On7UVceL4GGG435JZt-n55ODsV0dPQHDnclLTwGgsK9gcS3AeadWfeMw_jPOiYj52BQuPrZy7gX5laHt5ashNN7lxgYTpzP6_im4x_6fxYBadnWAnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/040ce8f378.mp4?token=SSoSdRqd3CoH8e3hn394VT-d4i9acdwQVEdbufn3ZHhgmJPTp0vdwTldqCI8qa1y897DS7huCIrD891bm6EAI-0WaBHoFVWKoKtBgmFFk-t9DgIOBgnFBFQOFTy8x47rCK46pe1pBr78zw7onxNLGzctayRYkzaevvap6-V4N9YT6exucYubx3XgG3j2wwayDz9biK_kzjQGLPm-5eBchZqor6Ik6zHubhs5On7UVceL4GGG435JZt-n55ODsV0dPQHDnclLTwGgsK9gcS3AeadWfeMw_jPOiYj52BQuPrZy7gX5laHt5ashNN7lxgYTpzP6_im4x_6fxYBadnWAnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ به شیخ محمد بن زاید:
وقتی انقدر ثروتمند باشی، میتونی انقدر آروم صحبت کنی.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66466" target="_blank">📅 10:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66465">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/635e862fe5.mp4?token=vsIFxvlhFQQeKJs9hR04s6ujMoezr5T5PPfXLU6wlSPhIdNRMuVLntoX7LAd23SHW5Yw_vvZzfS24HA7cVEz4idFpBT6_0o6d4owxRzXZQfhrewpPZMm1x11vMRWLD4yfIUUA5mka4gq7hH4VDXZvST5JOWleNGWQyMUeXL5yX5FXjTrpJTKqb3MoSRrJBTjcr14Pwv-erZTH2_vTJOlMcp40koLDJSN8OYeO8jKV27K9MdFGxOUjZ947iDva8mlwI-qDg7iRmm55aF1pyKZ4Mvbpj4D-wsxdtNbcbEl4aUIkCJn9VDREu6xYJBRjBgqJDpKPLmh9lmxNffMBltbyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/635e862fe5.mp4?token=vsIFxvlhFQQeKJs9hR04s6ujMoezr5T5PPfXLU6wlSPhIdNRMuVLntoX7LAd23SHW5Yw_vvZzfS24HA7cVEz4idFpBT6_0o6d4owxRzXZQfhrewpPZMm1x11vMRWLD4yfIUUA5mka4gq7hH4VDXZvST5JOWleNGWQyMUeXL5yX5FXjTrpJTKqb3MoSRrJBTjcr14Pwv-erZTH2_vTJOlMcp40koLDJSN8OYeO8jKV27K9MdFGxOUjZ947iDva8mlwI-qDg7iRmm55aF1pyKZ4Mvbpj4D-wsxdtNbcbEl4aUIkCJn9VDREu6xYJBRjBgqJDpKPLmh9lmxNffMBltbyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختران حاج گاسم
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66465" target="_blank">📅 09:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66461">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQKiZIoiSJEyWoddysVK49srdFlspat2tuNr29T33hNTvA2hzrIFobeQupGlO0Eqyjyiv_-p5Z9HvBzpIIMstadQO0NyGoNVS8MZ4O9coKlydP2I4O3pO3NVa88CHvJhgqklWjQHZHOWn8lL3Fgf2FMKz2aruoFXXIaXw9MEW67yqNRoUOE7cyP-NTBORIvBBNhYd71Ajv69Q-MglNx_bQjB3G-s1BPnti9yYayDvKrKEcx2WJdIURhAX279uTZ5iGpVHWbW_mGWXPyzMlc2I2a7QV5oWhBbX25THMhzi54fXeBoOOG-9wv9r6Eh722998tYU0_YqYWSGcgJE-adRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a17f4667.mp4?token=Uf9SpIwWtePkLRIrMeXrArTtKRbH4zYIDLqBR-otufSDqHD6ZE1EvzfyUZ8SMl0JyQHXg4Kq0pDMrbCGa8RRqUD7osKb0T5_zWjQoCnqGlaTqi-SHFoD8gfWLcRTzfPPPHirDTCZ3xe7nD5LEwUebKTASlfAwXgWx9ppFOvYPHS3N5UAWjXGJtzVHQ_yX_Y9OiQA4VkF63AQTr7YTH36je7JpvceIbGgIjcbRes2YQEPKMSKM1eCoO5r3BcYPIYjbNZmVc1ihm6O8pwL0r9QZcJqt3YMJd2gs-524PCmQ7hRiUDKxdeIrdxGWf1FY97NgJM9Rd4b3QdUtol5El5zrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a17f4667.mp4?token=Uf9SpIwWtePkLRIrMeXrArTtKRbH4zYIDLqBR-otufSDqHD6ZE1EvzfyUZ8SMl0JyQHXg4Kq0pDMrbCGa8RRqUD7osKb0T5_zWjQoCnqGlaTqi-SHFoD8gfWLcRTzfPPPHirDTCZ3xe7nD5LEwUebKTASlfAwXgWx9ppFOvYPHS3N5UAWjXGJtzVHQ_yX_Y9OiQA4VkF63AQTr7YTH36je7JpvceIbGgIjcbRes2YQEPKMSKM1eCoO5r3BcYPIYjbNZmVc1ihm6O8pwL0r9QZcJqt3YMJd2gs-524PCmQ7hRiUDKxdeIrdxGWf1FY97NgJM9Rd4b3QdUtol5El5zrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات شبانه ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66461" target="_blank">📅 09:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66460">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66460" target="_blank">📅 01:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66459">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cWtROrNNVyNV83VLwXhQcoyXo0R6-_b88QpWMT_xFMsKuSjFsxtIcfd4R8sVOKSbat1dZkiFdYbXqJ0pDBcyh75O_QPIWU8XqvXO7833UNS1XBf5yYERlmOHxhk6RdHvNoh5l42ifVYYm0AvaBGD6FvasJTt4zyIpr3MMtoIjeMRqXP-XX270F8L_nj9aJ8XtLXlBgUvhNky5oYl7TbyVfle54e2GOuOUUpdFxhEFxG5A2EkSR2iKD8EP1qz98jfr3eNilpkXY3680iLLXpaZbCzAk9fRJSE1CHYFfD53guVQu5-Y8xLkqPbpYzWMWzPS_f6R8clKRFNEoWhyAoloA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66459" target="_blank">📅 01:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66458">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
‏به گزارش المیادین، هیات مذاکره‌کننده جمهوری اسلامی در پی تداوم حملات اسرائیل به جنوب لبنان، سفر خود به سوئیس را تعلیق کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66458" target="_blank">📅 00:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66457">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30a4159b30.mp4?token=sYNxi5TYzzCOXr_oN3CdtaKaAiSbkOyWGRm3MtNvWIjo5IW10RHUrLzefSQPZ7XSJpUI-scbMtnChEy5sZf8lFjmO_kS9kjmiZL9aFe2ryUlbsnpsxk3p0d0pcbjPM0fFs0-Z-Ph5KI7AX25KS1hh9ZMyLiC0As0Dyst9-E4TsV0pmZe-tJ6GtOsAGSKj6OFOO_7ZOcbKZxdj10N6cN7pQtFeTm2VYmLS8nOz1S4nhVO_UF2oxw00lr1rQJVycpmmlAuPJWFIQ7PoNu_CUiIa03mIDibxvEHdeUx8yaOr8-SKt0jna9UUeGs0HmerRMYZoRQa1wIOqPJG5Zbnpd2kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30a4159b30.mp4?token=sYNxi5TYzzCOXr_oN3CdtaKaAiSbkOyWGRm3MtNvWIjo5IW10RHUrLzefSQPZ7XSJpUI-scbMtnChEy5sZf8lFjmO_kS9kjmiZL9aFe2ryUlbsnpsxk3p0d0pcbjPM0fFs0-Z-Ph5KI7AX25KS1hh9ZMyLiC0As0Dyst9-E4TsV0pmZe-tJ6GtOsAGSKj6OFOO_7ZOcbKZxdj10N6cN7pQtFeTm2VYmLS8nOz1S4nhVO_UF2oxw00lr1rQJVycpmmlAuPJWFIQ7PoNu_CUiIa03mIDibxvEHdeUx8yaOr8-SKt0jna9UUeGs0HmerRMYZoRQa1wIOqPJG5Zbnpd2kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس:
آیا در جامعه اسرائیل افرادی هستند که بخواهند ایران را به لیبی تبدیل کنند، یعنی یک دولت شکست‌خورده با ۹۰ میلیون جمعیت؟ احتمالا بله.
اما نمی‌دانم که بی‌بی (نتانیاهو) چنین چیزی بخواهد.
من شخصا هیچ‌وقت چنین گفت‌وگویی با او نداشته‌ام. گفت‌وگوی جالبی هم می‌تواند باشد.
اما همین را الان می‌گویم: آیا تبدیل شدن ایران به یک «لیبی ایرانی» برای ایالات متحده آمریکا خوب است؟ قطعا نه.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/66457" target="_blank">📅 00:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66456">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47cfe42200.mp4?token=FaLJL8vN6n98s55hXs-R31KZ8z8sBoxKoD3Q4-fih_ZeFB2ME4S9a6uPx6MOStM_bY73wnTl3iAWNA4NUMcUdASKm6HwWg1_BO19-QbV-2QXcYy9V0LfcWlcanNWCd4cFp1l7P_5L1V1KCxzxXeDVDSQEfk48WZRP1LLipdIQFWYQVu0RFsgjVNetytai3vXkpLcMb1tBcnaDTBPNkq1I9RWwGIXbs_St6IDCYjcbIsDYeLMi4W-fDppS4s3jKA56L7CPNDfr_Nt7bGklL__bhBVGMDmlMZ3_WHcpceAL3RT7LYcMIu9iicB77RY_wnprd5uL89km_MDQdqKbdYftg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47cfe42200.mp4?token=FaLJL8vN6n98s55hXs-R31KZ8z8sBoxKoD3Q4-fih_ZeFB2ME4S9a6uPx6MOStM_bY73wnTl3iAWNA4NUMcUdASKm6HwWg1_BO19-QbV-2QXcYy9V0LfcWlcanNWCd4cFp1l7P_5L1V1KCxzxXeDVDSQEfk48WZRP1LLipdIQFWYQVu0RFsgjVNetytai3vXkpLcMb1tBcnaDTBPNkq1I9RWwGIXbs_St6IDCYjcbIsDYeLMi4W-fDppS4s3jKA56L7CPNDfr_Nt7bGklL__bhBVGMDmlMZ3_WHcpceAL3RT7LYcMIu9iicB77RY_wnprd5uL89km_MDQdqKbdYftg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس این انتقام ما چیشد؟
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/66456" target="_blank">📅 23:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66455">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ad18edc1d.mp4?token=qDQl5OW5shlglCdr4Hp3WZnqLgxa2dNo6IeKSpR6tm-vMfV6ClLNtfJwya045Qr7tfRH99VTlDighBJadKQKMPxNmeMmUfITyj1hWMfHE1_i6-FRCd5bOlhqQ-yEYN6j58yV-D7i8YU9q_SbR5dDFOnNr9DIe_-apiTqreebHgQuRWCtmFJfyBzv4QOjG6qyFCI4x2JAF9c_SkuCPC_UegNNYNO44Q7pZvKjnH2vhUzkWGFfJjbqT2ml4DUmBlXL-plwX2mzRcxnFzsplTo2lz0qY8vbNylvE4PIr1emPiJHWLLc3uwOfbhVvzO7rYmfEZDZ0AxukjmCogP1MwXc6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ad18edc1d.mp4?token=qDQl5OW5shlglCdr4Hp3WZnqLgxa2dNo6IeKSpR6tm-vMfV6ClLNtfJwya045Qr7tfRH99VTlDighBJadKQKMPxNmeMmUfITyj1hWMfHE1_i6-FRCd5bOlhqQ-yEYN6j58yV-D7i8YU9q_SbR5dDFOnNr9DIe_-apiTqreebHgQuRWCtmFJfyBzv4QOjG6qyFCI4x2JAF9c_SkuCPC_UegNNYNO44Q7pZvKjnH2vhUzkWGFfJjbqT2ml4DUmBlXL-plwX2mzRcxnFzsplTo2lz0qY8vbNylvE4PIr1emPiJHWLLc3uwOfbhVvzO7rYmfEZDZ0AxukjmCogP1MwXc6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس:
آنچه من به برخی از منتقدان این توافق که شنیده‌ام می‌گویم این است که آن‌ها می‌گویند: “خب، ایران این همه منفعت به دست خواهد آورد.”
من دوباره همان چیزی را که قبلاً گفته‌ام تکرار می‌کنم و احتمالاً مجبور خواهم بود چندین بار دیگر هم تکرارش کنم: ایران دقیقاً چه منفعتی به دست می‌آورد که قبلاً نداشت؟ پاسخ این است: هیچ چیز.
آن‌ها هیچ چیزی به دست نمی‌آورند مگر اینکه رفتارشان را تغییر دهند. اگر رفتارشان را تغییر دهند، آن چیزی است که باید از آن استقبال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66455" target="_blank">📅 23:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66453">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‼️
یسرائیل کاتز به کانال ۱۴:
ارتش اسرائیل دستورهایی دریافت کرده است تا در صورت لزوم، برای عملیات دیگری در ایران آماده شود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/66453" target="_blank">📅 22:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66452">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DquFsOKhiq7Y0--MVtCVgawx9UUKjVKHlPfpHkiJ6DYPTcPi_INdCjIZyAUZNm4CXaAd-ZysUHdEqKpGlja2H9Uvwyl0r9zGEH0mfPBzUtAtaGZwdjrSNkWbfD5zMTWYrqzrYdGtgkzngxHpzj19WlwsMuZrn4D2ysCuDJs_oZjHPENwjB525wrrzodhM1zK7kNGBAVx0uCI-bfuJj3sJXpB5LWTUkr6oubk9NRBFYC012AX7EVMsT8vXL6aReTib4nZAuPOGAX6HZVMbiAwDv-JYS2iHJk3mQG7wAVtzLYW4_T6xW24Rj-FyWvW7jhs9F4A3W4qi65LcFHma-FoQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در تروث سوشال:
ایالات متحده به صلح متعهد است و ما همه را در منطقه خاورمیانه تشویق می‌کنیم که به تعهد خود برای پیشبرد مذاکرات ما به زیبایی پایبند باشند. بازارها از آنچه که با کاهش قیمت نفت و افزایش سهام اتفاق می‌افتد، لذت می‌برند. ما انتظار آتش‌بس کامل در همه جبهه‌ها، از جمله لبنان، حزب‌الله و اسرائیل را داریم. از توجه شما به این موضوع متشکریم!
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/66452" target="_blank">📅 21:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66451">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">هات نیوز | HotNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/news_hut/66451" target="_blank">📅 21:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66450">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
پیام جدید مجتبی خامنه ای درباره تفاهم‌نامه:من مخالف بودم اما چون بقیه تصمیم گرفته بودن منم موافقت کردم  @News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66450" target="_blank">📅 21:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66449">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">این پیام یعنی پایان پزشکیان و جریان اصلاح‌طلب در ایران، و آغاز حکومت نظامیان به سردستگی قالیباف #hjAly‌</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66449" target="_blank">📅 21:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66448">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
پیام جدید مجتبی خامنه ای درباره تفاهم‌نامه:من مخالف بودم اما چون بقیه تصمیم گرفته بودن منم موافقت کردم  @News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66448" target="_blank">📅 21:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66447">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlzS38GuBmOQIHUsOgUz3o8eLBUHPrppkGlkYTf8gu7DwR4ImkxXDJIpRoMGRR4c3ZWi8x9gyBaclvZKYZrTPlD_FktsrvHOjA2aih9O98yoBqfKbdEhdwWXqUfcGDTcSxU1IzMgFEHfGYS3Ox3Q3g4lWPlOKebwiiGQvmGJFJ89ZPEf3lTUPO20PluZZibOH8r0TQvmfzWA_tvdo5Rzwgxh2zfWaJaj8QI9ZkdJ_cBJdnnBBs1kCN2VR5Ul4ikxaIGVtqQIPp0L6r5ZtM3ufH8y8jorikDb02wQwyxejQB7cmoOGNORFynz28BVtGVzVLp8Sn7FWgGhfS6ZR9LSXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پیام جدید مجتبی خامنه ای درباره تفاهم‌نامه:من مخالف بودم اما چون بقیه تصمیم گرفته بودن منم موافقت کردم
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/66447" target="_blank">📅 21:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66446">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3gLPqleWGUdyGgUvJOUdDx_Ccql6189k5h-Q6jUu6XNR6-SFIULkkwlDUSpE2OoVl4Q-kOlnRG6RS-HtVYoba9hWwBzzJkP6A4vHhgZMm2yDdndiRG2WZXxkKVpQ6u43G0ZXi6h_X9nIF_V_WEzFxPWRxzpgSkWODW3NAewrjrLDmDzx-SYVTcW6dsBDNTFfLzOmuSniyLjzhjvdVgiRpKlQyGUC9mm6pULjnuYvZA1tNCLiinC4EATLsjjDTEqGxj0NTbaTRpC1ZAq-0f2-JB7NGI34ZF79XxkhNy9UZ8mFzXZ4u-u1T8xoDs-9SLNOsSeq2qNrRRgnAz8U2Aa9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ: آمریکا هیچ پولی به ایران نمی‌دهد. اخبار پرداخت 300 میلیارد دلار به ایران فیک است. تمام آنچه برای آمریکا وجود دارد، موفقیت، کاهش قیمت نفت و پیروزی است. وضعیت بازار سهام را بررسی کنید. پروپاگاندای دموکرات‌ها در کار است!!!
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66446" target="_blank">📅 20:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66445">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‏
🚨
🚨
🚨
⭕️
سنتکام اعلام کرد، نیروهای آمریکایی محاصره اعمال‌شده بر تمامی ترددهای دریایی ورودی و خروجی به بنادر و مناطق ساحلی ایران را لغو کرده‌اند
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66445" target="_blank">📅 20:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66444">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f51df7dfe.mp4?token=m9l_GmaJXQUKcJ3fyfniYRHiIHJCq6kEgagYvg2F41qz2l0pH3e8iELMdI6wj3JMzf4zdSnltGZcHSk-C_W6yJeX1qydBeXKruzCYQQUm8Kx7l-tM7AvnxetsR9Vt9prfYxIO4vHOJIuJOFwUlKw0AhuLvVbeqshJFThZ70HsBaC8KmFrtzPDBtgWw7bVPbaFspTDZM0M9YlFAllXf3c7E2iCC3O_LWpRoCQ0wVCXXNU1IT2Avnh6rcJtSrfGj6zlSV267h3Rxt_ILK0eqF7FlsU_bl6fo8jqacpt2NmqGjtq_e8tvwVqI4QHzNotSLrFZXXHmYZlBdNo6_ApCtbjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f51df7dfe.mp4?token=m9l_GmaJXQUKcJ3fyfniYRHiIHJCq6kEgagYvg2F41qz2l0pH3e8iELMdI6wj3JMzf4zdSnltGZcHSk-C_W6yJeX1qydBeXKruzCYQQUm8Kx7l-tM7AvnxetsR9Vt9prfYxIO4vHOJIuJOFwUlKw0AhuLvVbeqshJFThZ70HsBaC8KmFrtzPDBtgWw7bVPbaFspTDZM0M9YlFAllXf3c7E2iCC3O_LWpRoCQ0wVCXXNU1IT2Avnh6rcJtSrfGj6zlSV267h3Rxt_ILK0eqF7FlsU_bl6fo8jqacpt2NmqGjtq_e8tvwVqI4QHzNotSLrFZXXHmYZlBdNo6_ApCtbjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس در مورد اسرائیل:
در طول سه ماه گذشته، دو سوم سلاح‌های دفاعی که از اسرائیل محافظت کرده‌اند، توسط آمریکایی‌ها ساخته شده و با پول مالیات آمریکایی‌ها هزینه شده‌اند.
مشکل اسرائیل دونالد جی ترامپ نیست و هر کسی در اسرائیل که فکر می‌کند بزرگترین مشکلش رئیس جمهور ایالات متحده است، باید از خواب بیدار شود و واقعیت وضعیتی را که کشور در آن قرار دارد، ببیند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66444" target="_blank">📅 20:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66443">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab365474cc.mp4?token=nM3loDEDgHNraKX_eAj0fpA92lTJ_fxvELhIbJH3Y9GDHmCiED0TCPAh4ywxqpKJ1rQ11AQgWSP9iQMMXCNdQu79DVMBVLhJQsBVY_ppjHDCTmWQWZ6fJUaZEHCKvFaTqQmbgwnzW19_0RCVbJG03NGhH8cPiqovwbq0dnKM0ejI0kzu6693yme5tFTEPi8EzfdLL15wuPBSDPKcRNeUrwvphbXM0NL5z-wi51KEyGAVV1M9i4yBcxbZgXVtwUnRJEfpVNCmsA_8e_i7RsOrmCYp-k2mKfAFZEUJrwxkLbynQQA44K8mlQx4TrytaxieQJK-u6FUQeWeGGSJjfJgRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab365474cc.mp4?token=nM3loDEDgHNraKX_eAj0fpA92lTJ_fxvELhIbJH3Y9GDHmCiED0TCPAh4ywxqpKJ1rQ11AQgWSP9iQMMXCNdQu79DVMBVLhJQsBVY_ppjHDCTmWQWZ6fJUaZEHCKvFaTqQmbgwnzW19_0RCVbJG03NGhH8cPiqovwbq0dnKM0ejI0kzu6693yme5tFTEPi8EzfdLL15wuPBSDPKcRNeUrwvphbXM0NL5z-wi51KEyGAVV1M9i4yBcxbZgXVtwUnRJEfpVNCmsA_8e_i7RsOrmCYp-k2mKfAFZEUJrwxkLbynQQA44K8mlQx4TrytaxieQJK-u6FUQeWeGGSJjfJgRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏جی دی ونس درباره ایران:
آنچه واقعاً اینجا اتفاق افتاد این بود که ما روز یکشنبه تفاهم‌نامه را امضا کردیم. این توافق‌نامه مفاد توافق‌نامه را تثبیت کرد.
چیزی که ایرانی‌ها پیش ما آمدند و گفتند این بود: «ما دوست داریم متن را تا جمعه منتشر نکنیم.» من واقعاً متوجه این موضوع نشدم - می‌خواستم متن را فوراً منتشر کنیم. اما برای اینکه با آنها کنار بیاییم، گفتیم: «مطمئناً، باشه، تا جمعه صبر می‌کنیم.»
و سپس آنچه در روزهای دوشنبه و سه‌شنبه، در حالی که رئیس جمهور در اجلاس گروه 7 بود، اتفاق افتاد این بود که شاید رهبران خارجی با ایرانی‌ها صحبت می‌کردند و آنها را به انجام این کار تشویق می‌کردند.
ما قطعاً به آنها می‌گفتیم: «ما تمایل شما را برای منتشر نشدن متن تا جمعه درک می‌کنیم، اما می‌دانید، ما در یک سیستم دموکراتیک زندگی می‌کنیم. مردم آمریکا می‌خواهند متن این توافق‌نامه را ببینند. ما مطمئناً دوست داریم هر چه زودتر آن را منتشر کنیم.»
و بنابراین آنها به این نتیجه رسیدند که رئیس جمهورشان آن را امضا کند، رئیس جمهور ما آن را امضا کند، و مهمتر از آن، شعار را تکرار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66443" target="_blank">📅 20:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66442">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66442" target="_blank">📅 20:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66441">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qtOxsQ0WkN2YuU_hVAoQKdYm00PqVpmt1788d1T-h3ZxXYcNU8-PWO2DrwJYrDR6r9PxxfDUOKb6K1g_YsWKSbwXtenI8fqQPSMGTbalhc1ckHfr9OaUlmEl7Bz7_kNc_8XGbW53NHyM4pnnqnIJmU5LomJzPszeYX-lh43ciWRrtipJ0shZEBsRc7wSm3jsl-yZDQIq_JRG3slrJKrdKD85BrIESo_ZXmCj6bWbUWOyjFCRWMFP451m-LFzPftggZcETgU5BEmyBRRm-9r4cxjQ5uc5gZM5t4FdCb76BK22mK6TGernqQuc9rLyHlful-CULiAHgf1b9A7PLl5q1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66441" target="_blank">📅 20:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66440">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b31dd3b8.mp4?token=LaJ-Peea9d0E-gcN97Ym841UCYOAUQhyzDtyaPnPVfVgkTIAj0Dtqb-0O4He6XjGzke7E46tzD0YYOzwFBOEjo_h8fSiF4jYjpc62tiSEeUTXJxuNY8zCzcausaJ-0V1Jo2-s-ZF9gyR9Sun4jHQDZ0P-Z42cJcPnKBudi6rKFWwYkNWtIIck8sBLEi3nMeFW7jnYp20gVz9n6AVVghhNI6zHFR1GVEFDUKWoR-Hbmat-jpgnWBvqZogvFYc94EpATm5LAYYNO8D5YM0-ZbvwtvUQaqZYa1CaCw3P-xSKNHFFT_UYmJhoPrL6HyB6UEwDAtO1E8MeOW0xzgeJDEBZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b31dd3b8.mp4?token=LaJ-Peea9d0E-gcN97Ym841UCYOAUQhyzDtyaPnPVfVgkTIAj0Dtqb-0O4He6XjGzke7E46tzD0YYOzwFBOEjo_h8fSiF4jYjpc62tiSEeUTXJxuNY8zCzcausaJ-0V1Jo2-s-ZF9gyR9Sun4jHQDZ0P-Z42cJcPnKBudi6rKFWwYkNWtIIck8sBLEi3nMeFW7jnYp20gVz9n6AVVghhNI6zHFR1GVEFDUKWoR-Hbmat-jpgnWBvqZogvFYc94EpATm5LAYYNO8D5YM0-ZbvwtvUQaqZYa1CaCw3P-xSKNHFFT_UYmJhoPrL6HyB6UEwDAtO1E8MeOW0xzgeJDEBZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس:
ایرانی‌ها برای دومین شب متوالی به هیچ کشتی‌ای در تنگه هرمز شلیک نکردند. تا این لحظه، آن‌ها به تعهد خود پایبند بوده‌اند.
سنتکام اجازه داده است دوازده کشتی از محاصره دریایی ما عبور کنند، بنابراین ما نیز به سهم خود به تعهدمان پایبند هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66440" target="_blank">📅 20:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66439">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csl18mIi-LDXt97ed4phJGjzWZN3fC2F_HN1smxTM5g5bmApYWi9h50WnCkXQVL-WhPV91gGE0umnXZONyskZ5ihSQSGuKpq-V8vjBapHgExQ992AlrH1w2RnXfCRzW-g8LN-o0GNC48hoGqyHHd1rG81KCTbrebMLkirI5VYIt3DJMFYwPDEzvFEkKekfXis0VuzY3PGg5xVIKeMT966btIsbkzEWgrQjHf7z8mAkPOQ1fRYxaFUXONVPYZ3dHl2gjhcE2z1HqB4Nkax8pxhGEpuzuhlnQrdVz3lj0SjyQV6qzeIQ9qEqCArNEQ9nwCJDFsf1hHtpPeRoPWQlQk2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
فایننشال تایمز :
گزارش شده است که ایران به ۶ میلیارد دلار از دارایی‌های بلوکه‌شده خود دسترسی خواهد داشت تا کالاهای آمریکایی خریداری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66439" target="_blank">📅 20:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66438">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ht28gfq6O1b_nnm8JNhi2Ph8z0xAcgmzwlp1Fqn3rdLDgfAT5ID9jfdltkTMob0nPgXuzsqQKZLc3HNL3ynQgFIDF8gjjf4zfqIu5HdRKL19dKvXiJ9TGCx3TZ8q0-lZawQRQ0KyL6ejCGhN1-QKn1oPTKu_VJ8d9rIyVweiAHkJ-ilhfGfCH4QEBStGpKUxsCyUSc-FgyOTonFvWeA0GJWF9fyXevEg-vnY1xzjGNYAWROhxwpxvxQ8Gq3yyN2GatwEBbXyTK0yFRtLopZy4K_jzKGkCvBSjHPg_ey9_7u9VDG6RAhKnZCQu0SOk6YNDq5VWD5QGbgw_m9j1Kj-4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
ونس: کجا می روی دونالد! «امام مجتبی» منتظر توست!
دونالد: از روی امام شرم دارم ونس! شرم! توان دیدن جراحات ایشان را ندارم!
ونس: تو هر کار توانستی کردی! تصمیم امام اصلح است بر ما!
دونالد:‌ چه کنم! چه کنم ونس! با این جماعت هزار رنگ٬ که دروغ را چون «رج قالی» میبافند! امام مان تنهای تنهاست! شرم بر من ونس! شرم!
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66438" target="_blank">📅 19:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66437">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd4fb90d19.mp4?token=aAlLm6VX2N-qMJX48b2iYAFSZu6_jlfGfNCvogBMoCcl8oxNYj2Ra9nxFdC9ydcaV4nVfPcvBUHZAQhXYa8NZJ9k8qvCWPCouC8OsaPXrH-_-1ohgi-VKCZhwimbq1MqjKD1_ivxERB_HzI7oaiOz3gzrgplcBKvNte5SrrPD4KtaOsIFYF1hdMmbz7Cv8x9zg1IeEULA9Qm1QuCuFm0rFyenqa6nM7pDj69qRJJ7UEUEGph5oIF0AddW5OZxYf8L5HGy-3OsrxFFMXdiXbLd6m9u6bBMzvJysqU-oEDu7XFpJN-J980B0e0gR0DEEhJYmX7dIfcZqJVz-pYchA7ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd4fb90d19.mp4?token=aAlLm6VX2N-qMJX48b2iYAFSZu6_jlfGfNCvogBMoCcl8oxNYj2Ra9nxFdC9ydcaV4nVfPcvBUHZAQhXYa8NZJ9k8qvCWPCouC8OsaPXrH-_-1ohgi-VKCZhwimbq1MqjKD1_ivxERB_HzI7oaiOz3gzrgplcBKvNte5SrrPD4KtaOsIFYF1hdMmbz7Cv8x9zg1IeEULA9Qm1QuCuFm0rFyenqa6nM7pDj69qRJJ7UEUEGph5oIF0AddW5OZxYf8L5HGy-3OsrxFFMXdiXbLd6m9u6bBMzvJysqU-oEDu7XFpJN-J980B0e0gR0DEEhJYmX7dIfcZqJVz-pYchA7ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرنگار:یه مرد دانا سال 2020گفت ایران هیچ جنگی رو نبرده اما در هیچ مذاکره ای هم شکست نخورده
ترامپ:کی اینو گفته؟
خبرنگار:دونالد ترامپ.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66437" target="_blank">📅 19:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66436">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_O1Obv5PZkqxB2hgjG2RmyFt7OzkcxP8MMibN5fckRzGrXgYuBzGIT8d6K4WvR9-6c19SGTqdY0Ih6vegjtiS91m6BCY172skfgNzVPXrSOsqIPtCGTau7iZq7P6sNYmuyScBmUWWxu2_jkLnTT_dgOlLMFc_KwwEf6jpvl25SBNGpKMvfTlPYj-OGNqcn_J0MK10RscrnWOIaF89feuulbHbJaDlLfWkkl6OJwrTwd5Ee1csIeaxpGnj-wKSsWSee8QieRBxQZeuCilw9jJYoN4CTrkeayh46sS6566zyrrBYMa7vPtJwy41I7Js53Ggsehhk1kIosaeV7hH6A1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
الجزیره به نقل از تلویزیون پاکستان:
سفر برنامه ریزی شده شهباز شریف به سوییس بدون ذکر دلیل لغو شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66436" target="_blank">📅 18:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66435">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5PfuFxr9oYkg4KJyEl9TgAwpNrJhE8Ctby8JOKwnRmBe3zs6EL_HeJXdD_FNufNi6COin5_XBBESyhIpVcUcKm04mGB0PX6QRWU0iOcsyXTbrr61EFCGTJD6J-ky16okcSqstQApLCJQ1XMcOJyJ_5mGJPg3ErwFVa7hrv0571H4FDouciszv1cxV7GGe2GFmjPX8BxGT0KMKgOPjsK17pBes0hCK6_AbBDAawXjJkabl-rnj_FPEIoJEa-BXL8nq5n3zOvVFQtWR6pyFQ-cE9ItVuNTxiDefSYTtmHO3ai67MRSNJ6R82P4SYrm9YiMAwHAesugBnxjC_8HZ50qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
نفت جریان دارد، ایران هرگز نمی‌تواند سلاح هسته‌ای داشته باشد (جهان امن خواهد بود!)، بازارهای سهام در حال رونق هستند، مشاغل رکورد زده‌اند و قیمت‌ها در حال کاهش هستند (قابلیت خرید!). کشور ما قوی، امن و محترم‌تر از همیشه است. «خواهش می‌کنم!» رئیس جمهور دی‌جی‌تی
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66435" target="_blank">📅 18:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66432">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c-GfZAcLwlhLF1xBgPlhOu6Qwz7MW4vVOP6ZVkL492eqjPl87foInzHX_B8I76nZ9tMG4mbSjT6N9ca7WsyRv6rW4u3tIhqdMrHgLZn2Z0ycfM2xFYROvcqeScGb5BhdOrHQqwzMQlWjVRvB1WnivPJrhMpFiyUcuanVCkwrs6c3DzoSth9o9QNKqWbjkq5wfUxE7C7DBV8OSjb1366MDIRHDvOmVUS7pZ8vgD5y9A2qN-_5mKRFyB4wcBzgTbirf6s6DzmO_R7sqCdkkHOmFs289fi3bCrtefe6zsx5e18VKkmPbpfhACCc_UmPpjHUqCB4s_h3mEn1qTLl4oEuxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GvPVV78AHDX-x2VzKb_ZEvo8bk5xrox6HyTj1iqC8O4YhpJuEF2l3jTVv75dP-d_HwfkVPTCC4t51fOikto_Hl54V54Y6tEH9xwgqSNvC8Pok94P_4KsnOauajmpP5o-KRegPwVS7L8amzxVaiTrE-g4VRRnUOs6fMzyxzIey1L3eNVoWFaBAbDTR7kFlmhvC_mJIbKLM1JvB3kY3e9zbjcFwWLKzh9CVdjNUkNOYoHJGqNSYZAoLa1uw16W-DJU_FDs18YOFU1iiMkch-4SHvEy3kPchfGBYGXnmoABSGzaC-JTQxRAWr7Abg_gFr6_nUM-egoch8niRjtpd48h4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13c6e64c5c.mp4?token=K1WVXqMANFeiYCajNRIJJ6-zOf7jg8fhfpAEqKI8RgSheui39rLHSxqJlkU8_HHO854IOdzKVZOJ1-hJa98YBYu7ycCeouTRT8J9B7WIdL4pVpVtvKnTimWmqQJb3mcK9NRht7TulCje_QkYQ7DS_bcnLbk8bixquuCeac-uz7dvibKmZ8Z3tBte_s62BNovt8F63OLv6D-83emYJfPES1c_Iei5y4VKbvMBgvDilStgmuLjw-C3i4bqoyHq0aKkeeUpT2-ho5f4yDduav_2vbBHDLLWZg287XLWaak9l5KcvE8lWGBbvus7GudStx1WYJ49HwdRzV6QHY_juMEoLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13c6e64c5c.mp4?token=K1WVXqMANFeiYCajNRIJJ6-zOf7jg8fhfpAEqKI8RgSheui39rLHSxqJlkU8_HHO854IOdzKVZOJ1-hJa98YBYu7ycCeouTRT8J9B7WIdL4pVpVtvKnTimWmqQJb3mcK9NRht7TulCje_QkYQ7DS_bcnLbk8bixquuCeac-uz7dvibKmZ8Z3tBte_s62BNovt8F63OLv6D-83emYJfPES1c_Iei5y4VKbvMBgvDilStgmuLjw-C3i4bqoyHq0aKkeeUpT2-ho5f4yDduav_2vbBHDLLWZg287XLWaak9l5KcvE8lWGBbvus7GudStx1WYJ49HwdRzV6QHY_juMEoLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پختو پز اوکراین در مسکو پایتخت روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66432" target="_blank">📅 17:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66431">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bf3ba597d.mp4?token=XVeD0dt8iKVZHLRb1lY2A40ERxQTag-QdpJQGGJi1vVoAP24vmMf04onKbD6813r8RExpXwxIpo4g1faGuSocYs022Xm3AXW_dcl-pBlsp-CE0E5Re4Nuuu-MABjX9REysyAJsaTKK157cxIoColhRGm6UzQHwYDWxW-RJzYljVygOHfKZlp5avcVTwZ5OUYJrZ3ciZIKr8jCtekwVbET8lSx2ACaAlhM1S6Lt1MvMFXaPrVHT7VQeNVk5D5e8kJakPec7peTXYnKbxvnqJx1YosWAcrJB6aZJvGMCmQIwW9WsXILI6Q4iDu-8QocRhDj3hiIbR5jZuBcwiE1S7HZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bf3ba597d.mp4?token=XVeD0dt8iKVZHLRb1lY2A40ERxQTag-QdpJQGGJi1vVoAP24vmMf04onKbD6813r8RExpXwxIpo4g1faGuSocYs022Xm3AXW_dcl-pBlsp-CE0E5Re4Nuuu-MABjX9REysyAJsaTKK157cxIoColhRGm6UzQHwYDWxW-RJzYljVygOHfKZlp5avcVTwZ5OUYJrZ3ciZIKr8jCtekwVbET8lSx2ACaAlhM1S6Lt1MvMFXaPrVHT7VQeNVk5D5e8kJakPec7peTXYnKbxvnqJx1YosWAcrJB6aZJvGMCmQIwW9WsXILI6Q4iDu-8QocRhDj3hiIbR5jZuBcwiE1S7HZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تردد کشتی ها در تنگه هرمز پس از امضای توافق
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66431" target="_blank">📅 17:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66430">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdP3QAjIeoolXJ6_jpPb-vtoWg1z0JtcwDcuTQW7FNatrKyS_rmAQrQKdHdKVED2zsr79nVCKIO00KQzmlJMFPyO0FGQlANNpVX8IVis9aL2ETaNDyfR0Zx1OYKffTvk6BNJr8_S6x98HGTq6rUPZKIP1CDuaI6UAbxZZNvQURmrfTx6exJpHOhzRTzbJIn9YSZqBDIisbfVVHhZXmpxOIg-kBy1F0tMc6EMrXbZODXI3tdF1Z3HAzBz7ZPMUImnwaPpt2EaBqDjUF8oONtZ2VMih1y_EPMivemgzBUtz8hC4A8xIHYg3-TDrLFqEec7SvP-jiBZD4VGuNmkF0GNuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
ارتش اسرائیل؛منطقه امنیتی فوری در جنوب لبنان:
نقشه منطقه‌ای که نیروهای دفاعی اسرائیل در جنوب لبنان در آن فعالیت می‌کنند
بر اساس نیازهای عملیاتی، نیروهای دفاعی اسرائیل در منطقه امنیتی واقع در حدود 10 کیلومتری داخل خاک لبنان مستقر شده‌اند.
نیروهای ارتش اسرائیل در منطقه عملیاتی جنوب لبنان مستقر شده‌اند و به تلاش برای از بین بردن تهدیدها و بهبود دفاع از جمعیت شمالی ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66430" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

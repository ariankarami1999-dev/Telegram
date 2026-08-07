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
<img src="https://cdn4.telesco.pe/file/qhC7DGOhKx1GJPxUyQ7AGMq-2TqStP9D7Io1TgPE73D3sI7nhiV2RWXTEjm1kjwuO3sEwv0ikHxw6DKx0g4jTIt5T2N80Ok3a1G-nE33YFA0ThFJWvmansvqYN7_Zf800a-Fee9h_Z1oDzedbTMbNA8I6qfBGb5bYhsYRKM0qghYAo0uFSDkDCRCr7ZExtuvkCzENMhkk87inijm3PAPeypE3e_akUKJSrf6jwGCTeUyAejaD8ewry5xr1wRd2-0ov0lOkQExwTBwG7iog-78dA7Im7We-AijgnDy0jy0JvTyuD43gwlwm6s5KRgcsUIoWzmeQJDzBSGKa_PembK9A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 445K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-16 10:11:15</div>
<hr>

<div class="tg-post" id="msg-20622">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پس از آنکه وزارت حمل‌ونقل اسرائیل پارک کردن تعداد بیشتری از هواپیماهای سوخت‌رسان آمریکا در فرودگاه بن‌گوریون را ممنوع کرد، به آمریکا اعلام شد که هواپیماها باید در پایگاه‌های نظامی نیروی هوایی اسرائیل مستقر شوند، نه در فرودگاه غیرنظامی بن‌گوریون.شبکه i24News…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/withyashar/20622" target="_blank">📅 09:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20621">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">instagram.com/Yashar – Ruhollah zam and Msoud Molavi @WarRoom</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/withyashar/20621" target="_blank">📅 09:44 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20620">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d2de94a7.mp4?token=YmY3Ujx9A3lP0ULSwAWBGotaYQteniceyley0kjb0GquoGSVj_OsMwrUfjucWpynabZ7WkQaH3ZFdvwLBRtggVTOkYfhmDCmjFTv7rsFZse1-HGTWWt-xQGT8RUAqkJ3ZLgU_FZ0ZExLkbQ23tKJx0OicCK4Q_aJn6tei_hNN0MMi5sGpVW36KNyfi9nMoUaH0-BRRgeWv86pMl-_gBP6-0tEblr9f-7yqDukxGcgWe5v0nBMO9g6LEIeR1NTgHMS9SDVPa1_NvYllebbB5rhkdDPWJdt_vaNeFwL8PlzFYLYVLzwfTjXdmsHmlwN7cY9Zwt6uD8llw7SY-zQpSOV4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d2de94a7.mp4?token=YmY3Ujx9A3lP0ULSwAWBGotaYQteniceyley0kjb0GquoGSVj_OsMwrUfjucWpynabZ7WkQaH3ZFdvwLBRtggVTOkYfhmDCmjFTv7rsFZse1-HGTWWt-xQGT8RUAqkJ3ZLgU_FZ0ZExLkbQ23tKJx0OicCK4Q_aJn6tei_hNN0MMi5sGpVW36KNyfi9nMoUaH0-BRRgeWv86pMl-_gBP6-0tEblr9f-7yqDukxGcgWe5v0nBMO9g6LEIeR1NTgHMS9SDVPa1_NvYllebbB5rhkdDPWJdt_vaNeFwL8PlzFYLYVLzwfTjXdmsHmlwN7cY9Zwt6uD8llw7SY-zQpSOV4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز سی‌وچهارمین سالگرد درگذشت دکتر فریدون فرخزاد
۱۵ مهر ۱۳۱۵ متولد شد و در ۱۶ مرداد ۱۳۷۱ آسمانی…
@WarRoom</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/withyashar/20620" target="_blank">📅 09:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20619">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مارک لوین : رژیم ایران باید نابود شود وگرنه این [وضعیت] هرگز متوقف نخواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/20619" target="_blank">📅 01:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20618">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">العربیه : یک مقام ارشد سعودی می‌گوید چندین گزارش اطلاعاتی معتبر نشان می‌دهد که میان حوثی‌ها، شبه‌نظامیان عراقی و سپاه پاسداران انقلاب اسلامی ایران (IRGC) برای آماده‌سازی حملاتی علیه عربستان سعودی ائتلاف هماهنگ وجود دارد.
این مقام این گزارش‌ها را «تکان‌دهنده» توصیف کرد، زیرا در حالی منتشر شده‌اند که ریاض در تلاش برای کاهش تنش‌ها است و اعلام کرده بود مذاکرات به‌صورت مثبت در حال پیشرفت است.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20618" target="_blank">📅 00:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20617">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a684ce95a7.mp4?token=F0jmfkiDVm1q4HbJjmXKhdv1V8h6bdoo6mckSKnMm0KxM4vtS29WvEEsCRikKftGT-nNI9TIyL2O3L7OyPl4K2pt3v71W3RcClxsLG3VN03XMNWlVBDy6_XPyBS6vKIMXeEiiqEz7sVrh6DNJnr7KP_Am0wXP5_I8J5ibW1Wwz4kgc-9KjYXpWX5LnKJ7fwvXNloE8anM7Cqac6jOn8A5fqMEozeTMUlTLePPxMTL2OjT9kx-MnoxyoMRrvHKNST6ZaIzQwGqfUMx13d0RjfuPo7hOsmhkhmtQAlHQsb7kspDaULIEheMw6aUh_j5ujhL2257UggyPBTeEBmx7zOOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a684ce95a7.mp4?token=F0jmfkiDVm1q4HbJjmXKhdv1V8h6bdoo6mckSKnMm0KxM4vtS29WvEEsCRikKftGT-nNI9TIyL2O3L7OyPl4K2pt3v71W3RcClxsLG3VN03XMNWlVBDy6_XPyBS6vKIMXeEiiqEz7sVrh6DNJnr7KP_Am0wXP5_I8J5ibW1Wwz4kgc-9KjYXpWX5LnKJ7fwvXNloE8anM7Cqac6jOn8A5fqMEozeTMUlTLePPxMTL2OjT9kx-MnoxyoMRrvHKNST6ZaIzQwGqfUMx13d0RjfuPo7hOsmhkhmtQAlHQsb7kspDaULIEheMw6aUh_j5ujhL2257UggyPBTeEBmx7zOOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما در سراسر جهان مهمات داریم.
اگر زمانی به آنها نیاز پیدا کنیم، آنها را خواهیم گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20617" target="_blank">📅 00:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20616">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0117ccebfa.mp4?token=ERTw9z_2aHYaT587ljVk4xO3bFTEN0dwa5-PeqVHMy4O1nzy--hETwulhZytL4pgBMur-A0fLDhRbu_zplTaxdE2ghvWge95WBvidOCpHeI9Ad2qHr46Iz66DLyyrqwilOOXzgRrgN_0pOh5_bV5fQA0PQk4GcGkPmZuXfJ9jQ1Y6cAaXFJye0e1mY06K0ELqptjwprYw5ojVOKuj_KqVdtHniaxpDl-UN54mBjUVwdQZ3OAwPj6r1SSNLPBym8n9qnkRRIV_4Dlj9XmxYbhrVy8jRUdBwM5IxQ01LTpR0L-ISIwlLlzmgOo7FOrjK5PyHJeaWw9RZkX67BwFDAyHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0117ccebfa.mp4?token=ERTw9z_2aHYaT587ljVk4xO3bFTEN0dwa5-PeqVHMy4O1nzy--hETwulhZytL4pgBMur-A0fLDhRbu_zplTaxdE2ghvWge95WBvidOCpHeI9Ad2qHr46Iz66DLyyrqwilOOXzgRrgN_0pOh5_bV5fQA0PQk4GcGkPmZuXfJ9jQ1Y6cAaXFJye0e1mY06K0ELqptjwprYw5ojVOKuj_KqVdtHniaxpDl-UN54mBjUVwdQZ3OAwPj6r1SSNLPBym8n9qnkRRIV_4Dlj9XmxYbhrVy8jRUdBwM5IxQ01LTpR0L-ISIwlLlzmgOo7FOrjK5PyHJeaWw9RZkX67BwFDAyHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: گزارشی وجود دارد که می‌گوید شما به اهداکنندگان گفته‌اید که باید کاری کنند جی‌دی ونس انتخاب شود. آیا این حمایت رسمی شماست؟
ترامپ: نه. من فکر می‌کنم او عالی است، اما خیلی زود است.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20616" target="_blank">📅 00:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20615">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1081b3145.mp4?token=PjjrNjPR7x2gYA5l_T6z9eR7gTDu7M-j6ttZgE8HKOVMtN60n9djV-zjwFQ9KzBXr3aoyek9eK7kI6E6FOBPy62vTHw35gvyzqzBCz6t5bx-YNpTlCbrvmrZ1g_vnK-vewsSN-olueiGOPKzFc2bEs20f6NJKXwlCadj_eVFhlXNNb1buUtB_Q0q3cYFwkmTVk8OMWZZeOiZKSjMXu2o5cMHIubm_GVDwTdY1JjkY6hMky5nv2HdKurTX8FevrNsYZKIhR98NbBKYi79FIux8Jh54vdE27TMpuQE1oMCluRuWQVr4QOoifMc8FWcyR6zYRXvvtI6YJMwcLuoWgzPkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1081b3145.mp4?token=PjjrNjPR7x2gYA5l_T6z9eR7gTDu7M-j6ttZgE8HKOVMtN60n9djV-zjwFQ9KzBXr3aoyek9eK7kI6E6FOBPy62vTHw35gvyzqzBCz6t5bx-YNpTlCbrvmrZ1g_vnK-vewsSN-olueiGOPKzFc2bEs20f6NJKXwlCadj_eVFhlXNNb1buUtB_Q0q3cYFwkmTVk8OMWZZeOiZKSjMXu2o5cMHIubm_GVDwTdY1JjkY6hMky5nv2HdKurTX8FevrNsYZKIhR98NbBKYi79FIux8Jh54vdE27TMpuQE1oMCluRuWQVr4QOoifMc8FWcyR6zYRXvvtI6YJMwcLuoWgzPkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: فکر می‌کنم این جنگ خیلی زود به پایان خواهد رسید. به نظرم آنها دیگر نمی‌توانند مدت زیادی به این وضعیت ادامه دهند.
خبرنگار: آیا برای بازگشایی تنگه هرمز توافقی حاصل شده است؟
ترامپ: نمی‌خواهم بگویم که توافق انجام شده، اما در حال حاضر تا حدی باز است. ما کنترل تنگه را در اختیار داریم.
من در مذاکرات با ایران دخیل هستم. اوضاع به‌خوبی پیش می‌رود.
ممکن است به‌زودی توافقی حاصل شود.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20615" target="_blank">📅 00:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20614">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">محسن رضایی (محسن کج بند) دبیر شورای عالی امنیت ملی(جایگزین علی شمخانی) شد، اون سرش رفت اینم تهش میره @WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20614" target="_blank">📅 23:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20613">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تنگه دعوا شده
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20613" target="_blank">📅 23:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20612">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">آمریکا : اگر
هیچ‌یک از والدین شهروند یا گرین‌کارت‌دار نباشند
، دولت قصد دارد در برخی موارد دیگر به کودک متولدشده در آمریکا تابعیت خودکار ندهد. این سیاست به‌ویژه افرادی را هدف قرار می‌دهد که برای
«گردشگری زایمان» (Birth Tourism)
یا با اقامت موقت وارد آمریکا می‌شوند تا فرزندشان پاسپورت آمریکایی بگیرد
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20612" target="_blank">📅 23:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20611">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">تنگه دعوا شده
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20611" target="_blank">📅 23:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20610">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwolXaMNHmRlT8i8RDglx3R7KZWH6wq792Lin3p3FQYGWjGxp8lYo5w3xkzdmoiATPNOfgZPe9QgzNCJMDgl-hshBczwkpeCS8tsvcFjNtoR5s1WY2NQSvwukd0xBiFxdacrha37nc_YuwI5dImM9tgwm-6ynjns-dxXP-O5ltzz_yfW2Ov1EDqi1rvZv87LquXdAGK00nOoyUbR2z7eyKwH_J-wabG7XaD2-wYbk6e1nWVeRccOp8pAy58wxKog3oesnFvCVltreSEb-1f7ji5aKIirgibgx4NkJ3dMDCjP9c74rck38Wi8zbuU-TxvRj5g5FyHbrlmcTWb9n_L8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای هشدار زودهنگام E3B-Sentry با رادار AWACS هم اکنون در آسمان انجام مأموریت میکند. دوستان بسیاری اسکرین‌شات گرفته بودند که این هواپیما رفته، لازم به ذکر است چندین نسخه از این هواپیما در پایگاههای آمریکا در منطقه حضور دارند. ولی این هواپیمای به خصوص همچنان به مأموریت خود ادامه میدهد.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20610" target="_blank">📅 23:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20609">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏افشای تکان‌دهنده ژنرال جک کین :
‏"پاکستان و قطر بر سر منافع مشترکشان با جمهوری اسلامی، دولت ترامپ را درباره اهداف واقعی تهران فریب داده اند"
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20609" target="_blank">📅 23:39 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20608">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ایالات متحده، اقدام حوثی‌ها را که آن را "حمله ترسوانه" به نیروهای وفادار به عربستان سعودی توصیف کرده است، محکوم کرد و به خانواده‌های قربانیان تسلیت گفت. @WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/20608" target="_blank">📅 23:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20607">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMdtr383Mpl31Yh-ZwLuTVSARbWxA_RW_KBCL5b0fZrB5hgboEkvlAm03mnqUOXAHpjae0dBzLUv4F02tkR6jkC_N_8V7xUaGGWdcBBm2BQk6X-XiVYHmxY364W-TteX1JLfar8zjmLP_Bf5ouhsrQxkt0B-RqA6lZ46RiO6kCDZJm2jRoS0j7E93QwGK5H9SdW53A2QIurXFdkSEIqhnyrlTbDbis8MJxSJ9fb-l9_0DEsH5gMbJz77BC0Iy2Qp7o5Q0gdUP5LW82mA-Us8IbEAvMEgA6itNlYCQZr2LHTj_Evsto0KHMnWWHJ-C369r1hrg4O_VQ54Rt6iYsCuDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان ۴ دهه واردات نفت از عربستان؛ آمریکا به سراغ ونزوئلا رفت
برای نخستین‌بار از سال ۱۹۸۵، واردات نفت خام آمریکا از عربستان سعودی در ماه جولای به صفر رسید؛ تغییری بزرگ در نقشه انرژی جهان که پیامد مستقیم تنش‌های نظامی در خلیج‌فارس است.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20607" target="_blank">📅 23:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20606">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olnfcuGxBOZYz8ru7ETMXL66tKEyYt_Q3MPZJlCFJ0N17ncusgkYLz47mPqNf19A8pDEl_Y8tMWWdihjqcV3Ls_ps3ruL04rnP-xxq3S6MoTt0p1n413uNtbBj2q1ekQUwJ0d5WezV6H2eqN3QH10-ZbEPY902TuZjmy6d-Xrd5JjZZ0lvZMRlHkKA1ROdyhc0O_rVS6JHztqRTq8AoGe-F7kOoXFOBDa0uxmwBAJo-4C-ygeh4TKHuGq-3mEbRVQWnmrO9GVmZOdI7vl_1eJ-Q-ERc4AhyPJKtCknluejbCa2ef6F_I67g50BcszuoYaaVdCQ4eSrP9dlpryxt2_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در لحظه گزارش شلیک موشک، حداقل دو نفتکش در حال عبور از تنگه هرمز از طریق کریدور تحت حمایت ایالات متحده بودند.
NISSOS KEA و NISSOS KEROS، هر دو قبل از نزدیک شدن به تنگه، سیستم شناسایی خودکار خود را خاموش کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20606" target="_blank">📅 23:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20605">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">تسنیم
: منشأ صدای انفجار در قشم، هدف قرار دادن اهداف متخاصم بود
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20605" target="_blank">📅 23:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20604">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">تایید نشده انگار از ارومیه موشک پرتاب شد
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20604" target="_blank">📅 22:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20603">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">جنگ میشه ؟!</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20603" target="_blank">📅 22:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20602">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ok67E3SR5stQkPGtYKWSe32WvFkRkqY0kH0W1ZSwclDTg4lzmbETbStKQfY3viJ_05QHKri_J5KnIyYOPmkmbczxa-ZAPZLtnBduL9sj6Z8wbGIUVhJCM8Nk7r-xi8vwF4hILuzo0e4PfT3mMeStishpDyVeW-vfudwwTKHnxsWANrv8rvNsVOnMwOMiC_eQYg4VaY7EY9vqRisSHRwb-iuYCHsthiAlPb5Nmh16Ohwfptq3ENULc6HovFi75262QStcG_QZ5mrSLJ4bAz3P6A8FKjtBgA5bzu1H_G4uddrJYsn4hqAB1X1lS_96zV6f1rWS6bYxluJqnYg_AF5mug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون دود از پایگاه موشکی پارچین ، بی بی داره خنثی میکنه شاید براشون
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20602" target="_blank">📅 22:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20601">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20601" target="_blank">📅 22:33 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20600">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رویترز: طرح ایران برای تنگه هرمز نشدنی است، آمریکا اجازه نمی‌دهد!
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20600" target="_blank">📅 22:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20599">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اکسیوس : به گفته یک منبع آگاه آمریکایی، چند ساعت پیش ترامپ و محمد بن سلمان تلفنی با هم حرف زدند
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20599" target="_blank">📅 22:28 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20598">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">وزیر انرژی اسرائیل (از مردان نیک روزگار): حتی اگر آمریکا و ایران به توافق برسند، اگر ایران برای احیای برنامه هسته‌ای یا توسعه برنامه موشکی خود اقدام کند، ما پاسخ خواهیم داد.
ما به هیچ توافقی که امنیت اسرائیل را کاملاً تضمین نکند، متعهد نیستیم
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20598" target="_blank">📅 22:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20597">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گزارش پرتاب چندین موشک/پهپاد از سیرجان
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20597" target="_blank">📅 22:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20596">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گزارش های مردمی با سانسور : تنگه مال اقوام درجه اولشون نیست که شب خنثی سازی کنند
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20596" target="_blank">📅 22:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20595">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">قالیباف با صحبتهایی مانند آخرای شمخانی گفت:
حمله بزرگی در راه است... صبر کنید، نه، آن‌ها می‌خواهند مذاکره کنند. این دیپلماسی نمایشی است که بارها تکرار شده است.
استفاده از زور و تهدید، همراه با وعده‌های دروغین و اخبار جعلی، یک استراتژی شکست‌خورده است.
حقایق را بپذیرید و به تعهدات خود عمل کنید. ما به نمایش‌های بیشتر نیازی نداریم.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20595" target="_blank">📅 22:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20594">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گزارش مردمی : اطراف یا خود اسکله بهمن قشم رو ۲ بار زدن ۴ بار هم دروغه
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20594" target="_blank">📅 22:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20593">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بخشی از رسانه های رژیم : موشکی هشدار آمیز توسط نیروی دریایی سپاه پاسداران به سمت یک شناور متخلف در تنگه هرمز شلیک شد.
@WarRoom
بخشی دیگری از رسانه های رژیم: صداهای انفجار جزیره قشم مربوط به مهمات عمل نکرده زمان جنگه</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20593" target="_blank">📅 22:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20592">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">یک صدای انفجار جدبد از دور در قشم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20592" target="_blank">📅 21:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20591">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20591" target="_blank">📅 21:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20587">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گزارش صدای ۲ انفجار‌ در قشم
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20587" target="_blank">📅 21:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20586">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Ruhollah zam and Msoud Molavi @WarRoom</div>
  <div class="tg-doc-extra">instagram.com/Yashar</div>
</div>
<a href="https://t.me/withyashar/20586" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">صحبتهای افشا شده از مسعود مولوی با روح‌الله زم در مورد اسرار سیاست و پیشبینی جنگ ایران و آمریکا.
‏این صحبتها اولین بار چند روز پس از ترور مسعود مولوی در ۲۳ آبان ۱۳۹۸ پخش شد. همچنین روح‌الله زم در مهر ۱۳۹۸ توسط جمهوری اسلامی ربوده و یک سال بعد حکمش اجرا شد.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20586" target="_blank">📅 21:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20585">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گزارش حمله سپاه به اربیل عراق
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20585" target="_blank">📅 21:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20584">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">شاهزاده رضا پهلوی : جمهوری اسلامی تو شرایط ضعف و بحران مشروعیت، قصد اجرای کنوانسیون آکتائو (رژیم حقوقی دریای کاسپین) رو داره. این کار بدون اراده ملت و تضمین کامل حقوق تاریخی ایران، تهدیدی جدی علیه منافع ملیه. معاهدات 1921 و 1940 و اعلامیه آلماتی، حقوق مشترک و نیاز به توافق همه کشورهای ساحلی را تأکید کردن. اما کنوانسیون آکتائو با اجازه توافق‌های دوجانبه و چندجانبه، اصل اجماع رو دور می‌زنه و جایگاه ایران روتضعیف می‌کنه.
این اقدام از موضع ضعف و مغایر منافع ملی است. حقوق ایران تو دریای کاسپین قابل معامله نیست و هر تصمیمی بدون رضایت ملت، نامشروع و قابل بازخواست خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20584" target="_blank">📅 21:07 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20583">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">کانال ۱۲: رئیس سازمان موساد دو رئیس بخش را به دلیل شکست در تلاش برای تغییر رژیم در ایران، برکنار کرد
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20583" target="_blank">📅 21:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20582">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9xnyEYAPHZTG8RN1F7KpZ4aNOG8L_h2Rmg_M-w53awGMqDV6ixlg35mp3lq_LacrFRfuGoCL1TrxE6iLusTEmfNtmKAHZgNuq2aECk28DqTHgpmThIJGjoh3k0S411dTQz0v4ix7XMYsRsjuDPLsfz6zuysnLTOty0vAzhxuGRqMXgv3t1yjG80PK1VXmKBOCK75p3JUtrStzwRCNSRZ_W2UpMi5GC-pK0YAN4liXfYd-QOef_vI3_RCDYFHUsZ3t9XgcdvYfYglgp0krtMsvwtXy0baNCRtSqFQ6bogVXyai5s__cIjhUBuTr10v_9RA5OecbD0RvSOISxnqHtng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های جعلی، مثل همیشه، در حال انتشار شایعاتی دروغین و کاملاً بی‌اساس هستند. من از عملکرد پیت هگست کاملاً راضی و خوشحال هستم. همه چیز فوق‌العاده بوده است، از جمله حمله ما به ونزوئلا که در کمتر از یک روز به نتیجه رسید و به ما امکان داد یکی از خطرناک‌ترین جنایتکاران جهان، نیکلاس مادورو، را به دست عدالت بسپاریم. همچنین در مورد ایران نیز همه چیز به‌خوبی پیش می‌رود؛ کشوری که برای این هدف که هرگز به سلاح هسته‌ای دست پیدا نکند، به‌شدت تضعیف شده است. پیت در میان نیروهای نظامی احترام بسیار زیادی دارد و اصلاحات بزرگی انجام داده است؛ از جمله حذف برنامه‌های DEI (تنوع، برابری و شمول) و افزایش جذب نیرو به بالاترین سطح تاریخی. این شایعه را روزنامه واشنگتن کام‌پست، که یکی از بدترین رسانه‌های این حوزه است، منتشر کرده؛ آن هم با وجود اینکه ما به آنها گفته بودیم گزارششان کاملاً دروغ است. در واقع، من واقعاً معتقدم این نوع «خبررسانی» جعلی، مصداق خیانت است!
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20582" target="_blank">📅 20:35 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20581">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">توپ در زمین آمریکا است,ترامپ باید تصمیم بگیرد
الجزیره : در خصوص مذاکرات باید گفت که به نظر می‌رسد توپ از زمین ایران و عمان خارج شده و به زمین آمریکا افتاده است. اکنون چشم‌ها به رئیس‌جمهور ترامپ است تا در مورد جزئیات باقی‌مانده و تعهدات آمریکا تصمیم بگیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20581" target="_blank">📅 20:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20580">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-s-PeDJwLS4HUDKWjvvjh79aa0baJ6V3ETdBM_gXldAduQCeSY79siztOM8JI3nHfTFmiDi9ddBxxzkpwCSc6OVn2lYTDpGFCsOieKJvJnUQVVFu8HqVx-7MI76prKtntscfBDESpM0jfZUyzaoswAIYFbtlWbx-Hl7-m4twT5w7IIanF2sHYnZDYzgL0Zr5BHuj9FUt_nr3RaYSgxTc5EARdw8FmBj09NGpDVyFE1u-blhZIfsbnjuk9ryEuT9Lg_hrEH5YmvWD1SqwnOcDg0UmBMOkhJIyMG4qFSp7iJW3UIrqaWjkA8LOTJnCHe3tkOUrhBIbeUNr4BkgwBOqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمب‌افکن مخوف B-1b از فیرفورد بلند
شد تمرین کرد و با توجه به الگو احتمالأ سوختگیری هوایی هم امتحانی انجام داد ،  حسابی خودشو گرم کرد و آماده شد و دوباره به مبدأ برگشت
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20580" target="_blank">📅 19:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20579">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">محسن رضایی (محسن کج بند) دبیر شورای عالی امنیت ملی(جایگزین علی شمخانی) شد، اون سرش رفت اینم تهش میره @WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20579" target="_blank">📅 19:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20578">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">رسانه های رژیم : طبق چارچوب مذاکرات میان ایران و عمان که نهایی نشده است ، در مرحله نخست کشتی‌های ورودی از کریدور شمالی تنگه هرمز در نزدیکی ساحل ایران و کشتی‌های خروجی از کریدور جنوبی نزدیک ساحل عمان عبور خواهند کرد. پس از پایان این دوره، تردد از هر دو کریدور متوقف شده و همه کشتی‌ها از کریدور میانی عبور می‌کنند؛ به‌گونه‌ای که ورود کشتی‌ها تحت مدیریت ایران و خروج آنها با مدیریت مشترک ایران و عمان انجام خواهد شد. همچنین هزینه عبور به‌صورت بهای خدماتی مانند سوخت‌گیری، بیمه، خدمات محیط‌زیستی و سایر خدمات تعیین می‌شود و ادعای دریافت تعرفه ثابت ۳ یا ۷ درصد از ارزش محموله‌ها تکذیب شده است. بر اساس این گزارش، عبور کشتی‌های آمریکایی و اسرائیلی از تنگه هرمز نیز ممنوع خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/20578" target="_blank">📅 19:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20577">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">کانال ۱۲ : نیروی هوایی ایالات متحده تخلیه بخشی از سوخت‌رسان‌ها در فرودگاه بن گوریون را آغاز کرده است @WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20577" target="_blank">📅 19:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20576">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAHYT17zlSLlW4KP0foqjprBQw1J42C4tZlYcr8WKOhNT-YiXp_Z8fNHbyNJYNysI3ADeDrXSQEwc6cjt6AIQANjX-AggKcONA6N_whlEO5qHD-rzpoTASE9CUA5gKFuaSYD2Ymav7n1PktEwze4C9lwy8xCgxE8fJYpeA5WqxlbCUoOd8_74Y9SERBcJ8tsfSOc5a-zWwVTqGvrUIuzskDqb2O_9jg7N2kmcFdgVHGlF5hNsik2PR__Pc2J2cQTJ4IgTpp0ALFEVnhPhEuOuPAzCsYdyozr6wOOIeSLYU-JLkpIZdaMENE8-p8akXeWvcR2_hutIaam61cE5dxLbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی (محسن کج بند) دبیر شورای عالی امنیت ملی(جایگزین علی شمخانی) شد، اون سرش رفت اینم تهش میره
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20576" target="_blank">📅 19:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20575">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">تعدادی از نیروهای عربستان سعودی کشته و زخمی شدند، پس از آنکه یک موشک شلیک شده از یمن مستقیماً به پایگاه‌های نیروهای تیپ واکنش سریع اصابت کرد. @WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20575" target="_blank">📅 18:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20574">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ان‌بی‌سی نیوز: پنتاگون جلسه اضطراری برای تأمین تسلیحات برگزار می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20574" target="_blank">📅 17:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20573">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">حسین شریعتمداری نماینده ولی فقیه و مدیرمسئول روزنامه کیهان : باز شدن تنگه هرمز یعنی باز کردن راه فرار دشمن و از دست دادن یکی از مهم‌ترین اهرم‌های فشار جمهوری اسلامی.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20573" target="_blank">📅 17:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20572">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خبرگزاری رویترز : هنوز درباره نحوه اجرای «کنترل» ایران بر تنگه هرمز توافق نهایی حاصل نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20572" target="_blank">📅 16:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20571">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54aca75746.mp4?token=pqLDaSQDjZHq8oO_EUhynJTOjdkc26zC-cwm_kTHBXjdlpShbotCJ5rBBNq9dmyfDjIXhXxjgIiv4hlG7cg8EjAU5ds4nOg16NfnWXYlmF5keeutYMrvvdmX7lOQpo1mgFUILyR9nw7Qnk_pYPNVZkNcGFntbgf6yL76-u26wdw7Pt_cynv-KjhaSfJjpiB-OLEYeUBviWk8gXw5uhqMtRB9FUWNdls5IGJgBNVCIWLUHQUK2W9YvO4_Ue3UehvVIb_upR-Zr_LkiJge39ixc9sEde0hjNqRzdfB3-RWAiHfwll2sGd2f6HecGGie3fvSetda8L67eRuiVVsRFesAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54aca75746.mp4?token=pqLDaSQDjZHq8oO_EUhynJTOjdkc26zC-cwm_kTHBXjdlpShbotCJ5rBBNq9dmyfDjIXhXxjgIiv4hlG7cg8EjAU5ds4nOg16NfnWXYlmF5keeutYMrvvdmX7lOQpo1mgFUILyR9nw7Qnk_pYPNVZkNcGFntbgf6yL76-u26wdw7Pt_cynv-KjhaSfJjpiB-OLEYeUBviWk8gXw5uhqMtRB9FUWNdls5IGJgBNVCIWLUHQUK2W9YvO4_Ue3UehvVIb_upR-Zr_LkiJge39ixc9sEde0hjNqRzdfB3-RWAiHfwll2sGd2f6HecGGie3fvSetda8L67eRuiVVsRFesAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مجری: آیا هنوز معتقدید که نوعی تغییر رژیم در ایران امکان‌پذیر است؟
‏مایک پمپئو: 100٪
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20571" target="_blank">📅 16:36 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20570">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">منابعی از گروه تروریستی حوثی های یمن به رسانه های رژیم اعلام کردند تا دقایقی دیگر، نیروهای مسلح ما با انتشار بیانیه‌ای از یک عملیات نظامی گسترده و ویژه خبر خواهند داد.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20570" target="_blank">📅 16:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20569">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کویت با استناد به امنیت ملی، دستور تعطیلی فوری تنها مدرسه خصوصی ایرانی خود را صادر کرد
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20569" target="_blank">📅 15:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20568">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b68ab7702.mp4?token=vqSSGvPrUvQ-ymRJsWOaY1SEZiC9NSMai9dTci-d4GH_QalsqovkzeHIcdtHyIG2BCI8BTjIaRE36iE11s6fXzi2ZI8eu1O065OAv5i-ruu3ViZo1FQ6qALWs9lNk5l1ClQH1JvPQLuCjDDTogK4J2AnTU9Uetbq6HyNS9QB8mBdcCc9rA7Zb6mwj9qp2GaodBVpTS1Apnf4rg0JWip-OfqHEXV7hDjLgvY-Crw5xqcEWp-dHgiqnBzLjpLlM4Jrv_aYnyuRC53me2X0GbSuxdRZ6xSL0x2lKGYB5Zj3_75l_22SyopbG-pyRHMeLvoby7R7iA8XIZUkwffH5ipRJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b68ab7702.mp4?token=vqSSGvPrUvQ-ymRJsWOaY1SEZiC9NSMai9dTci-d4GH_QalsqovkzeHIcdtHyIG2BCI8BTjIaRE36iE11s6fXzi2ZI8eu1O065OAv5i-ruu3ViZo1FQ6qALWs9lNk5l1ClQH1JvPQLuCjDDTogK4J2AnTU9Uetbq6HyNS9QB8mBdcCc9rA7Zb6mwj9qp2GaodBVpTS1Apnf4rg0JWip-OfqHEXV7hDjLgvY-Crw5xqcEWp-dHgiqnBzLjpLlM4Jrv_aYnyuRC53me2X0GbSuxdRZ6xSL0x2lKGYB5Zj3_75l_22SyopbG-pyRHMeLvoby7R7iA8XIZUkwffH5ipRJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مایک جانسون، رئیس جمهوری‌خواه مجلس نمایندگان آمریکا، گفت:
‏«ما در انتخابات میان‌دوره‌ای پیروز خواهیم شد؛ چه مسئله رژیم تروریستی جمهوری اسلامی را پیش از انتخابات حل کرده باشیم و چه نکرده باشیم.»
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20568" target="_blank">📅 15:07 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20567">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">جروزالیم پست: اتهام جاسوسی به نفع ایران به دو زوج اهل عسقلان وارد شد.
این زوج، اقدام به تصویربرداری از مکان‌های حساس، از جمله بندر ایلات و کوه هرتزل کرده بودند و همچنین خانه‌های افراد امنیتی را تحت نظارت قرار داده بودند.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20567" target="_blank">📅 14:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20566">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJyuyZJC4TpTPJpNRwXcampu38UQjYgOPBdLnzz8fGdwTvctyl9e4ciAzUXsDkxA502-1D71nlR7JDkMqiGgA4MWpw9c1IzINCFxetuBl1u_shOWb3gdZV8cAvxm69_Hvq1Qxv366IL-Yh8-fs2LpK3PwCwrDZhRmDvFmasEkt-Qcd2u2stLX1rYZrVyRJPS8f06KA4SNI8IzC0WUwvUMVFL1_NiVAeOfqmM8bXIcrglCf0LHGw3EIRDyDUwIGWbUvY9xOHXbRYZEW-zQQmBSazwn2obYBnsmuMmA9rkOXnvOGhT1NRuw4IcWoKJu_DtYsd4_vtAln_Zmh0S-qWhmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۲ : نیروی هوایی ایالات متحده تخلیه بخشی از سوخت‌رسان‌ها در فرودگاه بن گوریون را آغاز کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20566" target="_blank">📅 14:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20565">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">حکومت ایران عوارض ۷٪ را بر تمام کشتی‌های تجاری عبوری از تنگه هرمز اعلام کرده است , این امر برای ایران ۳۸۵ میلیون دلار خالص روزانه یا بیش از ۱۰۰ میلیارد دلار خالص سالانه با حجم ترافیک پیش از جنگ ایجاد می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20565" target="_blank">📅 14:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20564">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">کمیسر عالی حقوق بشر سازمان ملل می‌گوید ایران از ماه مارس حداقل ۵۶ نفر را اعدام کرده است - افزایش چشمگیری نسبت به ۱۵ مورد تخمینی در مدت مشابه سال گذشته.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20564" target="_blank">📅 13:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20563">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‏واشینگتن پست گزارش داد که دونالد ترامپ، رییس‌جمهوری آمریکا، در دیداری خصوصی با حامیان مالی خود گفته است: در نهایت، باید جی‌دی را انتخاب کنیم. این اظهارنظر نشانه‌ای از احتمال حمایت او از جی‌دی ونس در انتخابات ریاست‌جمهوری ۲۰۲۸ است.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20563" target="_blank">📅 13:12 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20562">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">حوثی های یمن موشک شلیک کردند  @WarRoom
🚨</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20562" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20561">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">عبدال السید در انتخابات مقدماتی دموکرات‌ها برای کرسی سنای میشیگان پیروز شد. او در ماه نوامبر با مایک راجرز، نماینده پیشین جمهوری‌خواه، رقابت می‌کند و در صورت پیروزی، نخستین سناتور مسلمان تاریخ آمریکا خواهد شد @WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20561" target="_blank">📅 12:57 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20560">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">حوثی های یمن موشک شلیک کردند
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20560" target="_blank">📅 11:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20559">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یاشار : امروز سنای آمریکا قرار است ساعت
۱۰:۳۰ صبح به وقت شرق آمریکا
، برابر با
۱۸:۳۰ به وقت تهران
، درباره لایحه
CLARITY Act
رأی‌گیری کند. این لایحه با هدف ایجاد چارچوب قانونی شفاف برای بازار ارزهای دیجیتال تدوین شده و از مهم‌ترین قوانین تاریخ صنعت کریپتو به شمار می‌رود. در صورت تصویب، بسیاری از تحلیلگران انتظار دارند بیت‌کوین در کوتاه‌مدت بین
۳ تا ۸ درصد
رشد کند و آلت‌کوین‌ها نیز افزایش بیشتری را تجربه کنند. در صورت رد شدن، احتمال اصلاح
۵ تا ۱۰ درصدی
قیمت بیت‌کوین وجود دارد، هرچند شدت واکنش بازار به ادامه مذاکرات بستگی خواهد داشت. با توجه به وضعیت فعلی مذاکرات، احتمال پیشبرد این لایحه حدود
۵۵ تا ۶۵ درصد
و احتمال شکست آن
۳۵ تا ۴۵ درصد
برآورد می‌شود، اما هنوز اختلافات سیاسی بر سر برخی بندهای آن به‌طور کامل برطرف نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20559" target="_blank">📅 10:59 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20558">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPPSkNJ5WYGQm2ekmGnlDZb3OLTjmhjh64n8S2-o4C2nmOcuqUPt0cJ2_-xnCkVDPkHrkIZ_Sc4RDtA1zoMUw9oXcpbAKBwilb7HHM2gLsljNamvhqQnidPFeRYzff6lwKEwCTQQlKfYkz_kcfzT7Q_Rmrtfwy5A8X4S3JPqdBzJLbpvnoOJxAL_lSnQmM_3neLtDXs5fmfFOYsnhYqbaE33ouxNMmFfAk5jKFpVOLce-b4WmdTSvWxj7PvIF8bHMTpH-liaY1p8BfumTzRPSkp5S4Fc9pOX2ZsG4aB6a1-OT9iNd4bqHqRmlYb7yu2M4Qm9t56X2kDkgqXWzypR5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : ایالات متحده مقادیر عظیمی «مهمات»، به ویژه از انواع خاص، دارد. علاوه بر این، مقادیر زیادی از آنها در صورت نیاز تولید و به ما ارسال می‌شود. شرکت‌های دفاعی در حال ساخت بیشترین تعداد کارخانه و تأسیسات در تاریخ کشورمان هستند. «افشاگران» این اظهارات…</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20558" target="_blank">📅 10:03 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20557">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utgHV_Jgwr2Pgse7tfl8J0w5wAHtPYRIVjiwD0-TdwDog5ZHPAa4uCuHElcuUT7D8Rt4gsZW9_7pIpSTcRtAapffS_IxptlrLYqAZga_0q_9OANRwofr0jfdmeo8z0hcPLDpN9v-EnvPv6k9sJAakIoLWjVFuxC0TVH57hCOdFeWQxGMouZbJVPpD7BQ3C8jFEgL_7oIotrZJ-P6ttjfM86r6gn0nQcwHnpZPxUF7qnUFSeiD9q0iS2qNKzlzIhR6EVIZTfCxjkNJzMxLD71N1MSPKQzA4aCWUm43JjIRGsnvxMhRoJyi17wAZVAA3E1C8P9B0D4tudKEL4kKCWegA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره: قیمت نفت در پی امیدها به توافق ایران و آمریکا در مورد تنگه هرمز، کاهش یافت بهای معاملات آتی نفت خام برنت با کاهش، به ۷۹ دلار و 2 سنت در هر بشکه رسید
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20557" target="_blank">📅 09:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20556">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSLBb0zcFvkSRmVEFdOmD8zrHvmCttWOy05Yp1onmtDv-Q-vtSjEu1HgPWhNy7g5aNVDDBOL8DwmXOc8yh2mb8CIJvi2qWQku7UETWe8YJTwSjxweJ9yQvLt08IIPf-56S49tFV-rcSxfYv-1Tql-dRxrcmR0MbZ1Io2WVPP4lWWLeswUV6tfbPzYv0lTfuULHAYLn_NY18iHK8OQkL6sZYlLsFTCF-q28c7w_L7BO5hPARshwqhYLhfUgCaq4xv-1KtDJJQCsSsxs6HMERK0asUKaMl2G11Qn5NFfm7rBjuh18Hu6EBiAKlPYGAmHFDPAUe9-FzAdQrL17l5dGqrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : ایالات متحده مقادیر عظیمی «مهمات»، به ویژه از انواع خاص، دارد. علاوه بر این، مقادیر زیادی از آنها در صورت نیاز تولید و به ما ارسال می‌شود. شرکت‌های دفاعی در حال ساخت بیشترین تعداد کارخانه و تأسیسات در تاریخ کشورمان هستند. «
افشاگران» این اظهارات خیانت‌آمیز تحت تعقیب هستند. احکام حبس طولانی مدت برایشان
درخواست خواهد شد!
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20556" target="_blank">📅 09:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20555">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db57e2ad51.mp4?token=fqxUf9aMvIDvqRKsYvkCQ3vTxnDH38FModS8BH_mV7UmE6jw7TGBWiH_PVcABDp39AMAWNRfLGJnGuFQh8-mFJwRcTXyACoTeN6HhaJoeZ9R5C1YfqmTUyoTKA2MJjQYVne4jA6AsyGWl-wwCBG7RUk57mVeF2TcYett9ESz1MawdzV1t3bZKJ-6pS6UgpTgax_1qjP6YQBvFWh-aUSvFBYmKZkaheJR8__p6RaLrVGoZyTydwSXMIzOGlwMHNIqMk9RRW4i3clcdqay5T-6yIAaIOhz1CCzy3avOA6tObQVCJNRGfffH1x3OIKD5HZxNLdVivuFo0xTpb0kLHxgTqJBH6vx9oCufbi-eX9aD4JTVpMIrPHf7SD4979a9vWKrfzZSsYV5Ti7awPsoeWUM5MdHbJB1RfhNj9xWIc4wgDOEWNt7H0vJ-EN1K8W3ordsJx7wY2cd-QV6xZ7jknLoLpiYCID1Uv2wraaHQ4V79YbELBbrrlbUInzI-fIsbA9ZElZkdicuydx0cJXnOUUE95ZWd1vHy6k2tyZ345RzWQD4Z9VdiMeVtSafv6ajcTtfYsE6NtIOfesCwdARp4ixYoSA58L6e5JTf9fFhKXe4gN8P-1fmWPSqxRQM1vVbefxD_ppZ-MmWuokLaGK8Y0tOnGTp1aENL27lYD4wVL95Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db57e2ad51.mp4?token=fqxUf9aMvIDvqRKsYvkCQ3vTxnDH38FModS8BH_mV7UmE6jw7TGBWiH_PVcABDp39AMAWNRfLGJnGuFQh8-mFJwRcTXyACoTeN6HhaJoeZ9R5C1YfqmTUyoTKA2MJjQYVne4jA6AsyGWl-wwCBG7RUk57mVeF2TcYett9ESz1MawdzV1t3bZKJ-6pS6UgpTgax_1qjP6YQBvFWh-aUSvFBYmKZkaheJR8__p6RaLrVGoZyTydwSXMIzOGlwMHNIqMk9RRW4i3clcdqay5T-6yIAaIOhz1CCzy3avOA6tObQVCJNRGfffH1x3OIKD5HZxNLdVivuFo0xTpb0kLHxgTqJBH6vx9oCufbi-eX9aD4JTVpMIrPHf7SD4979a9vWKrfzZSsYV5Ti7awPsoeWUM5MdHbJB1RfhNj9xWIc4wgDOEWNt7H0vJ-EN1K8W3ordsJx7wY2cd-QV6xZ7jknLoLpiYCID1Uv2wraaHQ4V79YbELBbrrlbUInzI-fIsbA9ZElZkdicuydx0cJXnOUUE95ZWd1vHy6k2tyZ345RzWQD4Z9VdiMeVtSafv6ajcTtfYsE6NtIOfesCwdARp4ixYoSA58L6e5JTf9fFhKXe4gN8P-1fmWPSqxRQM1vVbefxD_ppZ-MmWuokLaGK8Y0tOnGTp1aENL27lYD4wVL95Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا : بر اساس این گزارش، فرمانده یک نفتکش در حال عبور از تنگه هرمز اعلام کرده است که در فاصله حدود ۹ مایل دریایی جنوب‌شرقی منطقه کُمزار عمان، صدای دو انفجار را شنیده است. @WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20555" target="_blank">📅 07:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20554">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">جی دی  ونس : من با ترامپ در مورد ایران اختلاف نظر ندارم.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20554" target="_blank">📅 07:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20553">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سناتور تام کاتن: «ارتش ما آماده است تا کار را تمام کند».
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20553" target="_blank">📅 07:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20552">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C89rLwE6SZg8zFlts5ElO3fDgJTrf1BPW1qcrtwBwFsoZafx6ZiyQdwmhORX5PGAYbcjwfhvb93ZVKgwEfrWohvUOZR-DpJb85Z4lVsd7Guovxvv6U-U4AxVPXR2kEdYYaNYcmqEjdoM81beTdBlc2GRuNQEQkJ4bDwV5vExXQMC93-3zbHeNPnYbhduAud77qFtbc9q4_-LViPP7Eb7dsMes7GStqTQQWSM1gv5HSuO7X00gpObPRdwywFce-HLBIAOXs4JQskIFrVSQOFgX4oh_f9fCcQt-LzrGMjAycXDDmLdmnf8hI_CgjXd58BfhHNyD0sxpQejrIA2YAacTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تگه دعوا شد
🚨
🚨
🚨
گزارش پرتاب موشک از‌ سیریک @WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20552" target="_blank">📅 07:36 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20551">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c627cc882.mp4?token=Ik812aXxCeC6TSOUO5mQwYsKDSPRLpM4VT8GeQGajZp1hYBa__bXAvm9xz9826FSCThHeRplBrXcWv8CMDFuicESJq9-_bnC_cNrEN4TkOHZ4oTnwgg85-E_cHhuwY29zweMTFSDKpQJrK2XUP-mTOL7GOFbHN1BW9eIUwwWDe3msenOR3pMXD7bN4mh97pH2XJDEiqJxw20T0TdOI5lL1qTJS2sCnw1N39Eu9zUzsjQHhdKlwE0iIQPQr1LInSCFcHWX4UDNY0A-SyxCVALCDst0bJufdOWL2NHXd7GRx8L_zdMh4KgKUbylN1wLy_RWsYgJXRXZyx8gC_w3OmtdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c627cc882.mp4?token=Ik812aXxCeC6TSOUO5mQwYsKDSPRLpM4VT8GeQGajZp1hYBa__bXAvm9xz9826FSCThHeRplBrXcWv8CMDFuicESJq9-_bnC_cNrEN4TkOHZ4oTnwgg85-E_cHhuwY29zweMTFSDKpQJrK2XUP-mTOL7GOFbHN1BW9eIUwwWDe3msenOR3pMXD7bN4mh97pH2XJDEiqJxw20T0TdOI5lL1qTJS2sCnw1N39Eu9zUzsjQHhdKlwE0iIQPQr1LInSCFcHWX4UDNY0A-SyxCVALCDst0bJufdOWL2NHXd7GRx8L_zdMh4KgKUbylN1wLy_RWsYgJXRXZyx8gC_w3OmtdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران:
ایران با من تماس گرفت. آنها بزرگترین حمله از زمان جنگ جهانی دوم را نمی‌خواستند.
ما گفتیم: "ترجیح می‌دهم این کار را به این شکل انجام دهم." من به دنبال کشتن مردم و نابودی کامل همه چیز نیستم. و این همان جایی بود که ما به سمت آن می‌رفتیم.
آنها می‌خواستند مذاکره کنند و ما در حال انجام این کار هستیم. و به نظر می‌رسد که این [مذاکره] کاملاً خوب پیش می‌رود.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20551" target="_blank">📅 07:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20550">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8609e5317a.mp4?token=X9ER2-DQAAAbt7NiJ3xeMWfn1i_DTnjjSZZuXSsNcJfy-B1YfiQDxOn3LXfHMQHEsw2PQabmCYIGw7kGXx5mKNcV4POSgH52XcgsicQzYi7LHWbrP5f6OSAy0Yzj9GXU-tfF7SsDuY6RqeVYwHWsfTWnTaLimK-ESB5amS3IMIZaVD-BAtwvEOxmZmK6_mL7HOzyaf9qs4E5cI_3u1vqXcX0AMPNcsu6_6iVmXGkqDt22799esOwxjBR_78WEz4yuNln5yONEeSpDFXP4oaiAHp_rGXSy_2nS69_LQbB0VbKsxdwx33zLrZwjc2F2vjsbuRg8BpJxb5JaVKs78rpnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8609e5317a.mp4?token=X9ER2-DQAAAbt7NiJ3xeMWfn1i_DTnjjSZZuXSsNcJfy-B1YfiQDxOn3LXfHMQHEsw2PQabmCYIGw7kGXx5mKNcV4POSgH52XcgsicQzYi7LHWbrP5f6OSAy0Yzj9GXU-tfF7SsDuY6RqeVYwHWsfTWnTaLimK-ESB5amS3IMIZaVD-BAtwvEOxmZmK6_mL7HOzyaf9qs4E5cI_3u1vqXcX0AMPNcsu6_6iVmXGkqDt22799esOwxjBR_78WEz4yuNln5yONEeSpDFXP4oaiAHp_rGXSy_2nS69_LQbB0VbKsxdwx33zLrZwjc2F2vjsbuRg8BpJxb5JaVKs78rpnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور ترامپ در مورد ایران:
ممکن است این بار با مذاکرات متفاوت باشد؛ ممکن است نباشد.
ما آماده حمله بودیم. در زندگی واقعی، آنها می‌دانند چه زمانی آماده حمله هستید و چه زمانی فقط بلوف می‌زنید.
و اگر مجبور باشیم، آماده حمله هستیم
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20550" target="_blank">📅 07:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20549">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">شبکه i24news درباره تنش‌ها با ایران: "وقتی بازدارندگی آمریکا تضعیف می‌شود، بازدارندگی اسرائیل نیز تضعیف می‌شود."
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20549" target="_blank">📅 07:21 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20548">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9266609aa.mp4?token=rjd1oYlaYvmpO9V7eXiTlIKGNTpDmqxaWZ0tTw1P1YUA1J1-qMC44ra4_WJG4Oh2FBpO8B5kYQZMTqMSW24eI-NDe-Lq_2rUwS7oS_sliHNB1164SD8cMR9ozCj-FyqaS9c25XZNIhsfLj2u20keG3lALQ6I9uxh5sCDTqITPxMBl3NUslllRIkdYzRFItwDh2lvriRfTjP7HV67QKIY9SHDIQR2NB11JVosIZYTBezJWaQNKmHs5oxBEILgJxba_8nKaY_6SgHRi7-Di3hXHV6Oyb35qNn3wfORa0GwDEhdWx_zaiJSotnpLhc9YoUJxKol-gJ8r38VG3EUK2Lldg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9266609aa.mp4?token=rjd1oYlaYvmpO9V7eXiTlIKGNTpDmqxaWZ0tTw1P1YUA1J1-qMC44ra4_WJG4Oh2FBpO8B5kYQZMTqMSW24eI-NDe-Lq_2rUwS7oS_sliHNB1164SD8cMR9ozCj-FyqaS9c25XZNIhsfLj2u20keG3lALQ6I9uxh5sCDTqITPxMBl3NUslllRIkdYzRFItwDh2lvriRfTjP7HV67QKIY9SHDIQR2NB11JVosIZYTBezJWaQNKmHs5oxBEILgJxba_8nKaY_6SgHRi7-Di3hXHV6Oyb35qNn3wfORa0GwDEhdWx_zaiJSotnpLhc9YoUJxKol-gJ8r38VG3EUK2Lldg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، درباره عبدال السید :
این آدم از یهودی‌ها متنفره. بعضیا می‌گن این حرف تنده، ولی نه؛ از یهودی‌ها و اسرائیل متنفره
عبدال السید! باورش می‌شه؟ فقط برای من همچین چیزی پیش میاد
عبدال السید ظاهرش محترمه، ولی آدم پر از نفرتیه
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20548" target="_blank">📅 07:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20547">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d4f4355b1.mp4?token=fOmBZpVz8PSZUG7QSS7Fv3o329a4-o08dN0G70BgtHvWJ9JCuVY9iJCPt4Rq2wzqYeHfR5kCh4U_elzsEUOmP21S-OK9ZuBTVB_STjjQyQ66R8_ickjdqbY7LQWs1GQG_qrJGYetlSuNm7R7Bnf_n8OfGRQlBOnYRNsJ-QyPG3SWOneYZCyyHTlekxCQroQBZOvSTfPXHAF1LF6VqoxuUSCBFFT5Y_jvjz1nUlkwFxgWXbxQYKvzJcuNMJZx_oWpBgZAI4uZGtxe-rb1sBJCCg_UWBR1-z1H7f3FYLWGnUrspe3b5zWOI_TXj6AtpVNs6HMQ-R-9ymXCqKjDlzPOSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d4f4355b1.mp4?token=fOmBZpVz8PSZUG7QSS7Fv3o329a4-o08dN0G70BgtHvWJ9JCuVY9iJCPt4Rq2wzqYeHfR5kCh4U_elzsEUOmP21S-OK9ZuBTVB_STjjQyQ66R8_ickjdqbY7LQWs1GQG_qrJGYetlSuNm7R7Bnf_n8OfGRQlBOnYRNsJ-QyPG3SWOneYZCyyHTlekxCQroQBZOvSTfPXHAF1LF6VqoxuUSCBFFT5Y_jvjz1nUlkwFxgWXbxQYKvzJcuNMJZx_oWpBgZAI4uZGtxe-rb1sBJCCg_UWBR1-z1H7f3FYLWGnUrspe3b5zWOI_TXj6AtpVNs6HMQ-R-9ymXCqKjDlzPOSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدال السید در انتخابات مقدماتی دموکرات‌ها برای کرسی سنای میشیگان پیروز شد. او در ماه نوامبر با مایک راجرز، نماینده پیشین جمهوری‌خواه، رقابت می‌کند و در صورت پیروزی، نخستین سناتور مسلمان تاریخ آمریکا خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20547" target="_blank">📅 07:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20546">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تگه دعوا شد
🚨
🚨
🚨
گزارش پرتاب موشک از‌ سیریک
@WarRoom</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/withyashar/20546" target="_blank">📅 23:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20545">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">به گزارش رویترز، به نقل از ۵ منبع:
رژیم ایران به کشورهای خلیج فارس هشدار داده است که هرگونه حمله جدید آمریکا به خاک این کشور، منجر به انتقام‌جویی علیه زیرساخت‌های حیاتی انرژی در سراسر منطقه خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 172K · <a href="https://t.me/withyashar/20545" target="_blank">📅 23:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20544">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رئیس تروریستی سپاه، احمد وحیدی: «هیچ بحثی درباره اورانیوم غنی‌شده یا سلاح‌های هسته‌ای صورت نخواهد گرفت. تا زمانی که ایالات متحده آمریکا و اسرائیل سلاح‌های هسته‌ای در اختیار داشته باشند، ما به کار خود در این زمینه برای امنیت ملی خود ادامه خواهیم داد. اگر آن‌ها…</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/withyashar/20544" target="_blank">📅 23:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20543">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/withyashar/20543" target="_blank">📅 22:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20542">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/withyashar/20542" target="_blank">📅 22:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20541">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پزشکیان: حوادث دی‌ماه پارسال قابل فراموشی نیست؛ کسانی‌که کشته‌شدگان را 30-40 هزار نفر اعلام می‌کنند، نامرد و وطن‌فروش هستن
@WarRoom</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/withyashar/20541" target="_blank">📅 22:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20540">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نیروهای یمنی اعلام کردند که با استفاده از یک موشک بالستیک، یک تانکر نفتی به نام "دیزی" که متعلق به عربستان سعودی است، را در خلیج عدن مورد هدف قرار داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/withyashar/20540" target="_blank">📅 21:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20539">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">محسن کج بند : به عنوان یه سرباز از‌ همه ایرانیا تقاضا میکنم یکمی دیگه این شرایط رو تحمل کنن، چون ما داریم بعد از آمریکا؛ چین و روسیه به قدرت چهارم جهان تبدیل میشیم؛ این شرایط گذاره
@WarRoom</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/withyashar/20539" target="_blank">📅 21:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20538">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">آکسیوس : دور جدید مذاکرات بین اسرائیل و لبنان که با میانجی‌گری ایالات متحده برگزار می‌شد، امروز ساعت 15:30 به وقت رم به پایان رسید. به دلیل تحولات میدانی، مذاکرات زودتر از موعد به پایان رسید، اما فردا صبح از سر گرفته خواهد شد.
بحث‌ها بر روی طیف وسیعی از مسائل سیاسی و نظامی متمرکز بود و بسیار سازنده بودند. تیم‌های فنی پیشرفت‌هایی در تعیین جزئیات کلیدی مربوط به اجرای چارچوب سه‌جانبه داشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/20538" target="_blank">📅 20:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20537">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نبیل الحمر، مشاور رسانه‌ای پادشاه بحرین، مدعی شد پدافند هوایی این کشور در حال مقابله با حملات هوایی ایران است.
وی افزود که در ساعات گذشته چندین حمله هوایی ایران رهگیری و دفع شده است.
پیش‌تر نیز هم‌زمان با هشدار درباره احتمال حمله هوایی، آژیرهای خطر در بحرین به صدا درآمده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/20537" target="_blank">📅 19:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20536">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">منابع عربی از حملۀ موشکی به بحرین خبر می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20536" target="_blank">📅 19:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20535">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نتانیاهو : ترامپ یکی از بزرگ‌ترین دوست‌های ماست،اما یه چیز رو روشن بگم، موجودیت اسرائیل قابل مذاکره نیست چه توافقی بشه چه نشه، هر کاری لازم باشه برای حفظ آینده‌مون انجام می‌دیم
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20535" target="_blank">📅 19:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20534">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گزارش‌ها از حادثه امنیتی برای
بالگرد ترامپ در آسمان واشنگتن
رسانه‌های عبری گزارش دادند بالگرد دونالد ترامپ، روز گذشته هنگام حضور او در بالگرد، در آسمان واشنگتن درگیر یک حادثه ایمنی شد.
گفته شده در این حادثه هیچ‌کس آسیب ندید.
سازمان هوانوردی آمریکا در حال بررسی ابعاد این رویداد است.
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20534" target="_blank">📅 19:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20533">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20533" target="_blank">📅 18:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20532">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ce2c280b.mp4?token=DmSrPwo1UE8HCNZtXA42dhrXN1m3S4JXAnDd1akE75Za9l1nrj1cRLyQ4D8JUQhzKFn9eaB0X-1D1kwZ0v97LTlqrTDL_pUPSedJNG3tY99bXIMYrQ0mkz19pGxU10JfMToQPl7kJoUtZIIHVd1lSmZvFehA9hgdhZ4ostRyDYalvqt57A84bibmpWQR3edfkqiHoFBJ16Lpz2pTiNp_OrflQgum3KmSb1kkcAXNm57R-gF2fCAheByXu8erx-O9X8oJEUWJGO9nglRKdxcRIRh01e-Q349FG8_RXQzhei2VU2jLdpBVGkhol5zeoNwWSwzcZgOjR0Qu68cu5oI1Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ce2c280b.mp4?token=DmSrPwo1UE8HCNZtXA42dhrXN1m3S4JXAnDd1akE75Za9l1nrj1cRLyQ4D8JUQhzKFn9eaB0X-1D1kwZ0v97LTlqrTDL_pUPSedJNG3tY99bXIMYrQ0mkz19pGxU10JfMToQPl7kJoUtZIIHVd1lSmZvFehA9hgdhZ4ostRyDYalvqt57A84bibmpWQR3edfkqiHoFBJ16Lpz2pTiNp_OrflQgum3KmSb1kkcAXNm57R-gF2fCAheByXu8erx-O9X8oJEUWJGO9nglRKdxcRIRh01e-Q349FG8_RXQzhei2VU2jLdpBVGkhol5zeoNwWSwzcZgOjR0Qu68cu5oI1Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل نتانیاهو در یک مراسم:
نیازهای سیاسی فوری این لحظه از من می‌خواهند که پیش از پایان این مراسم مهم ترک کنم.
ما در حال حاضر در میانه رویدادهای نظامی و سیاسی مهمی هستیم.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20532" target="_blank">📅 18:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20531">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سخنگوی وزارت خارجه درباره احتمال سفر قالیباف یا عراقچی به پاکستان یا قطر در پایان این هفته: برنامه‌ای برای سفر به این کشورها نداریم
سخنگوی وزارت خارجه: مختصات جغرافیایی مسیر مد نظر ایران و عمان، مورد تفاهم قرار گرفته
چنانچه برخی طرف‌های ثالث در این زمینه کارشکنی نکنند، بیانیه مشترک دو کشور مشتمل بر ملاحظات و نکات عمده مورد توافق نیز در مرحله بررسی و تدوین نهایی است.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20531" target="_blank">📅 18:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20530">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">داشتون مثل پلنگ اینجاست
🐅</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20530" target="_blank">📅 18:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20529">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اتاق جنگ با یاشار : رویترز تبر خورده خبر اشتباه زده
😂
https://ofac.treasury.gov/recent-actions/20260805  در این سند هیچ شرکت هواپیمایی ایرانی از فهرست تحریم خارج نشده است. آنچه حذف شده، همگی مربوط به شرکت هواپیمایی عراقی Fly Baghdad است که قبلاً به دلیل ارتباط…</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20529" target="_blank">📅 18:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20527">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اتاق جنگ با یاشار : رویترز تبر خورده خبر اشتباه زده
😂
https://ofac.treasury.gov/recent-actions/20260805
در این سند
هیچ شرکت هواپیمایی ایرانی از فهرست تحریم خارج نشده است.
آنچه حذف شده، همگی مربوط به
شرکت هواپیمایی عراقی Fly Baghdad
است که قبلاً به دلیل ارتباط ادعایی با نیروی قدس سپاه تحریم شده بود
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20527" target="_blank">📅 18:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20526">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">عراقچی روز جمعه به پاکستان سفر می کند.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20526" target="_blank">📅 18:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20525">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وال استریت ژورنال: ایران همه چیز را به کنترل تنگه هرمز گره زده است.
رویکرد تند تهران، اقتصاد و روابطش با همسایگان را تهدید به نابودی می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20525" target="_blank">📅 18:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20524">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رویترز : بر اساس جزئیاتی که روز چهارشنبه در وب‌سایت وزارت خزانه‌داری آمریکا منتشر شد، ایالات متحده تحریم‌های مرتبط با مقابله با تروریسم علیه دو فروند هواپیما و سه شرکت هواپیمایی مرتبط با سپاه پاسداران انقلاب اسلامی ایران را لغو کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20524" target="_blank">📅 18:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20522">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کانال۱۴ : مقامات آمریکایی تأیید می‌کنند که در هرگونه توافق احتمالی با ایران، تضمین می‌شود که تهران کنترل تنگه هرمز را دیگر در اختیار نخواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20522" target="_blank">📅 17:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20520">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">رئیس تروریستی سپاه، احمد وحیدی:
«هیچ بحثی درباره اورانیوم غنی‌شده یا سلاح‌های هسته‌ای صورت نخواهد گرفت. تا زمانی که ایالات متحده آمریکا و اسرائیل سلاح‌های هسته‌ای در اختیار داشته باشند، ما به کار خود در این زمینه برای امنیت ملی خود ادامه خواهیم داد.
اگر آن‌ها سلاح‌های خود را کنار بگذارند، ما نیز این کار را خواهیم کرد
.»
@WarRoom
این رژیم قصد ندارد از اهداف هسته‌ای خود دست بکشد. آن‌ها در حال به دست آوردن زمان هستند. هیچ توافقی حاصل نخواهد شد.</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20520" target="_blank">📅 17:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20519">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ارتش اسرائیل: ما حملات متمرکز در جنوب لبنان را آغاز کرده‌ایم در پاسخ به نقض آتش‌بس توسط حزب‌الله.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20519" target="_blank">📅 16:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20518">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">برای اولین بار پس از حدود یک و نیم ماه، ارتش اسرائیل دستور تخلیه را در جنوب لبنان منتشر کرد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20518" target="_blank">📅 16:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20517">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یک مقام ارشد خلیج فارس به سی‌ان‌ان گفت که احتمال رسیدن ایالات متحده و ایران به یک توافق موقت در روز جمعه ۵۰ به ۵۰ است، هرچند تندروهای اصلی ایران هنوز آن را امضا نکرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20517" target="_blank">📅 16:35 · 14 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

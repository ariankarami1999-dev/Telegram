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
<img src="https://cdn4.telesco.pe/file/FM_GxKHcHxLBB4pUvkoAXVrNvCSCgPp6UJToGDEojdtO2rEtF56h3oUS4y87XfF4-is8SlW3FpVYxawf_2gzMDTACNx-i5C_4N52KjGm8Y_y7xzHQ2tIa_8oT3fLiPT_M0Z-q9xSfNGLOdzHRbtKi2V-UKp3rZu-i1YNUOvHlq6yNkDxf7eU8WWFI1I2GjQAtTMBW1JSFGABKNLLhDo14gwQ1CtKyygdDkZuU7-Y-6mvjnf0dexWOSVy_5Q7EdvF-il26wGjsssgNd_-sbTymq1itAQUDLC3-2ajNedO9OscZ8Z9ZYCEVG1bJKKecVqyGRLjByayOyyAl1i1MKVezQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 272K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-03 02:56:48</div>
<hr>

<div class="tg-post" id="msg-12281">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تیرانداز به هلاکت رسید و فرد حاضر زنده و هوشیار است. هر دو به بیمارستان منتقل شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/withyashar/12281" target="_blank">📅 02:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12280">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ds9BVYoM4G5DddDo9EqTDrqtMKGdrUShDtv2KLKfGccDcmIWoLzwAhTUIUBuQvE9hQI0Es_oVPlHI36XIFs_e6gDvS_iq-E7LIxfSfSyHsAWYUCiaz9u5cfw3zl37HvHMHUDlOVh1KTrwaC_s53ClqoT98E8hIjFwvsDelwQNZpmvPISXOATwjhuq8_-KYubNxBNCiJYIp2mhKhpbQVg48HYNSSWfJX5wlxYthmGa5isEq3as9IqjJpS71QrVc3aGs9Bz8QFBdDIX4doMNYOWYKvJ5WBoTIIiUSnlR9lqtlxOgdlVxvtzUM6vEoEA8HI0KsFllTZSC3tbDgC4Rvjow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرویس مخفی پس از شروع تیراندازی در سمت غرب کاخ سفید به یک مظنون مسلح شلیک کرد، به گزارش فاکس نیوز.
یک عابر پیاده در این حادثه زخمی شد و تأیید شده است که رئیس‌جمهور ترامپ در امنیت است.
@withyashar</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/withyashar/12280" target="_blank">📅 02:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12279">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بی‌بی‌اس نیوز گزارش داد: در تیراندازی نزدیک کاخ سفید دو نفر زخمی شدند که یکی از آن‌ها مظنون است.
@withyashar</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/withyashar/12279" target="_blank">📅 02:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12278">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22e5d7ca97.mp4?token=bHu1BD75yBDj7yKQt9prbAZkTxM1HY4ykTDmNY5pkm9nGPJcMXPfqyadtYkPBPIlPXXbn9cgEs4l8rC8Ka6eO35nijHS-hHtXvR9qhq7pNF-B6ViKbNFqqeOKJlFxM-0iY0Nc9H4qBYShSb6DZUCDo0QOk71WXTGOa-DvUIoUoFLT7AayOY1-wf4j0bQ5QNZ7PFI8OpbGEud2TiqDdqtB_7_92GaBretq9URRx2VwTzIGJa80afojmVEWx71ImJtyCJHVeBeyY5ygkwxEzjGlhNTyZm3vrA-8YXk4WqJsTUpMoxiwV5R5WUFubUHfiNMsDHtNvpZFH_WKRQWbDcb7IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22e5d7ca97.mp4?token=bHu1BD75yBDj7yKQt9prbAZkTxM1HY4ykTDmNY5pkm9nGPJcMXPfqyadtYkPBPIlPXXbn9cgEs4l8rC8Ka6eO35nijHS-hHtXvR9qhq7pNF-B6ViKbNFqqeOKJlFxM-0iY0Nc9H4qBYShSb6DZUCDo0QOk71WXTGOa-DvUIoUoFLT7AayOY1-wf4j0bQ5QNZ7PFI8OpbGEud2TiqDdqtB_7_92GaBretq9URRx2VwTzIGJa80afojmVEWx71ImJtyCJHVeBeyY5ygkwxEzjGlhNTyZm3vrA-8YXk4WqJsTUpMoxiwV5R5WUFubUHfiNMsDHtNvpZFH_WKRQWbDcb7IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar
تیرندازی از دیدی دیگر</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/withyashar/12278" target="_blank">📅 02:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12277">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egwzg8gTuNYZRuG5GU9vnmttflidrmqCj1N4sOZAxNOBYor0dV5VlI0TCe_ZH_BQ0t5p_a451DG5-xoFhcglvm7EVzoZCzWNePdNEZDDMma0zmey6eh_Xmbq5TGkm3N91E4zx7BhzGGJVpr-bAXIyDUVqdi_IXUcyC2OYjaEUytcbsfxPXBJQY77TottU1eWxpSxZDJHWAREfnGG8RE9qUO-uNztDR-kIr2fp4y79opKUTtZzwh89ku2ALLNdSCP0NlLF3-HCn9jrnn_CfDe7EzVDzuYaIT16FWXkAaUWUcHUUA9Hz20SS-gVxH3Pps5sDCpegLpmT24y_AzYR-gjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحنه هایی از خارج از کاخ سفید.
@withyashar</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/withyashar/12277" target="_blank">📅 02:24 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12276">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مدیر اف‌بی‌آی کاش پاتل:
اف‌بی‌آی در محل حاضر است و از سرویس مخفی که به شلیک‌های نزدیک محوطه کاخ سفید پاسخ می‌دهد، حمایت می‌کند, ما به محض امکان، به‌روزرسانی‌های لازم را به عموم ارائه خواهیم داد
@withyashar</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/withyashar/12276" target="_blank">📅 02:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12275">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/978b6cb95d.mp4?token=Z6Z8lL-ICvRXP8PHBfb_zdP8shs_5XJQpdvsCADxbS8PHMOUjky2OzgKS940l7TWJn7SyeJL4vDf-bCesGdiUlUgqigHPbfNnp8g50JQv4IQ4kAUt2_cw7tT-Tgp9pHBg-ZC7JgjfK0kslBLZ8NIzpt6bf3N5PNwqKviyNiYEP7UCcePgaM8gwYlX9NCwb4JdGpHZVLzGuCQO3n7Tm9bdkvIDeaWLyADEd35RZA7_BgXHCxqNzfs8mekxIz62AJuPoZdNEn8bd-0YdxtSjLvXaS0eC3e0G-F6alN3u349uXnqaYbGuS9sKSwRfLU0HhI3Hjpu24WKj9rGuWkCbl7fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/978b6cb95d.mp4?token=Z6Z8lL-ICvRXP8PHBfb_zdP8shs_5XJQpdvsCADxbS8PHMOUjky2OzgKS940l7TWJn7SyeJL4vDf-bCesGdiUlUgqigHPbfNnp8g50JQv4IQ4kAUt2_cw7tT-Tgp9pHBg-ZC7JgjfK0kslBLZ8NIzpt6bf3N5PNwqKviyNiYEP7UCcePgaM8gwYlX9NCwb4JdGpHZVLzGuCQO3n7Tm9bdkvIDeaWLyADEd35RZA7_BgXHCxqNzfs8mekxIz62AJuPoZdNEn8bd-0YdxtSjLvXaS0eC3e0G-F6alN3u349uXnqaYbGuS9sKSwRfLU0HhI3Hjpu24WKj9rGuWkCbl7fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/withyashar/12275" target="_blank">📅 02:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12274">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91d610a95e.mp4?token=F7aQmyCLpewNHO1PrZxZdpZraW7wRmDRMKZJYEu5s9Z8VpW3RbsptHiVxGh0jV4RLE4N7s3_IsCP6th5vt5DR5hIjucHjGXY3MDVSobziCrKsEmpWOHFiKOHi2gEF0LwuKO8wkL0YwEE4HPUT7lUQkLlro2ulSFvfT5UbPFGdKgINA0NXBPhnMyP4pmItLVV-XHMWsO-rTf5JjIcSYl5X9wQzyICRT8ElzJdt15-OvPJtnL2pcf7SQwjX67zJDGQoBi6i1vGIIgSSCfpbq44ES_0d_1fReANeWO6EdUSWJvRjgZocgZzYFuHlEFDH5jdnAOoCw8-Xjq2kpD-TfgpDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91d610a95e.mp4?token=F7aQmyCLpewNHO1PrZxZdpZraW7wRmDRMKZJYEu5s9Z8VpW3RbsptHiVxGh0jV4RLE4N7s3_IsCP6th5vt5DR5hIjucHjGXY3MDVSobziCrKsEmpWOHFiKOHi2gEF0LwuKO8wkL0YwEE4HPUT7lUQkLlro2ulSFvfT5UbPFGdKgINA0NXBPhnMyP4pmItLVV-XHMWsO-rTf5JjIcSYl5X9wQzyICRT8ElzJdt15-OvPJtnL2pcf7SQwjX67zJDGQoBi6i1vGIIgSSCfpbq44ES_0d_1fReANeWO6EdUSWJvRjgZocgZzYFuHlEFDH5jdnAOoCw8-Xjq2kpD-TfgpDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گزارش‌ها، تیم‌های تک‌تیرانداز سرویس مخفی اکنون بر روی پشت‌بام کاخ سفید قابل مشاهده هستند.
این یک واکنش حفاظتی استاندارد پس از یک حادثه امنیتی است که در آن تیم‌ها برای ایمن‌سازی محوطه به موقعیت‌های مرتفع اعزام می‌شوند.
این با وضعیت فعال پس از گزارش‌های قبلی تیراندازی و انتقال خبرنگاران به داخل کاخ مطابقت دارد.
@withyashar</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/withyashar/12274" target="_blank">📅 02:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12273">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34a4f39d6.mp4?token=NJYaskUo2b2JxBYJjk_nkfE8H9v_mjYwJVKjWLHESuo66lMnrj5dRM44iy464LfzoxubZlAh0HH3SO5pwFIUZ98qOi5xTxdLhb30jS53FKIfOGSCL3nxpign4_y_074Q-LvXJlBg8PoKDfQZdYCVQS86ZiVwsbq0CPR-nzkOMysJ5Lepri6Tj0L4QJc43Ebx1n7xoKGk7_5XCyrsZNCRIgirv9qQgL9vyuGT674kqh0WSLS6dVfJ9jZ7XdlrU-FUfzHhclIm3RKZZVi952azp6cvqETJW-8p1CrB8cSdvvmIMRHgIMAnjbPdL1QO2orHimV8bz1iIRBICx3KIcT03w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34a4f39d6.mp4?token=NJYaskUo2b2JxBYJjk_nkfE8H9v_mjYwJVKjWLHESuo66lMnrj5dRM44iy464LfzoxubZlAh0HH3SO5pwFIUZ98qOi5xTxdLhb30jS53FKIfOGSCL3nxpign4_y_074Q-LvXJlBg8PoKDfQZdYCVQS86ZiVwsbq0CPR-nzkOMysJ5Lepri6Tj0L4QJc43Ebx1n7xoKGk7_5XCyrsZNCRIgirv9qQgL9vyuGT674kqh0WSLS6dVfJ9jZ7XdlrU-FUfzHhclIm3RKZZVi952azp6cvqETJW-8p1CrB8cSdvvmIMRHgIMAnjbPdL1QO2orHimV8bz1iIRBICx3KIcT03w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلمی از اخبار ABC لحظه‌ای را ثبت می‌کند که تیراندازی در خارج از کاخ سفید رخ داد.
@withyashar
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/withyashar/12273" target="_blank">📅 01:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12272">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">طبق گزارش NBC News، صدای تیراندازی در خارج از کاخ سفید شنیده شد، با حدود ۲۰ تا ۳۰ گلوله شلیک شده. سرویس مخفی به اعضای مطبوعات که در چمن شمالی جمع شده‌اند دستور داده است که به داخل اتاق جلسه بروند.
@withyashar</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/withyashar/12272" target="_blank">📅 01:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12271">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87c6f32ee8.mp4?token=GuYYmYjEfnX-c48gCU-NFXvjSeDSxJ3LaSnEuhgtrJamihPPi1h3Ip6Uehf9UJnDEml5ukZswqQiCdmsMGHAn8-LI1aFAzeMCm_c_aVj0AiRqt8uw1CORGWcPex1GPXZ9nj53DzN1uvCfT6p1kS_ShK4w1_i-uEqAo-sa5pXB4u7U1ZZR5y4iZQ5dXMrXy-9VZ0kWhJzQ7DSYmxIGkZ0AcXuExJ8TW5evwwIxERvBh4CJzpZRtUBADEKIDC2zvoHZIidI7AoB3gMdWhun2l_bto9B5Zgjxh5cIMYiRu4qIkAxpl6eTGvXko86qmUwDaGmu9XUQM0jYr_61CzcJzTyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87c6f32ee8.mp4?token=GuYYmYjEfnX-c48gCU-NFXvjSeDSxJ3LaSnEuhgtrJamihPPi1h3Ip6Uehf9UJnDEml5ukZswqQiCdmsMGHAn8-LI1aFAzeMCm_c_aVj0AiRqt8uw1CORGWcPex1GPXZ9nj53DzN1uvCfT6p1kS_ShK4w1_i-uEqAo-sa5pXB4u7U1ZZR5y4iZQ5dXMrXy-9VZ0kWhJzQ7DSYmxIGkZ0AcXuExJ8TW5evwwIxERvBh4CJzpZRtUBADEKIDC2zvoHZIidI7AoB3gMdWhun2l_bto9B5Zgjxh5cIMYiRu4qIkAxpl6eTGvXko86qmUwDaGmu9XUQM0jYr_61CzcJzTyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت اعصاب و روان من الان
👺
@withyashar</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/withyashar/12271" target="_blank">📅 01:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12270">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">الحدث: ایران و آمریکا به دشمنی طولانی مدتشون پایان دادن!
@withyashar</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/withyashar/12270" target="_blank">📅 01:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12269">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/withyashar/12269" target="_blank">📅 01:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12268">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">«نیویورک تایمز به نقل از سه مقام ایرانی: در این توافق موضوع هسته‌ای را به مرحله‌ای بعدی موکول می‌کند.
ولی این توافق به آزادسازی ۲۵ میلیارد دلار از دارایی‌های مسدودشده در خارج از کشور منجر خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/withyashar/12268" target="_blank">📅 01:24 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12267">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">المیادین:
آنچه پیشنهاد می شود یک توافق نهایی نیست، بلکه یک یادداشت تفاهم است.
این یادداشت تفاهم شامل هیچ بند مرتبط با پرونده هسته ای ایران نمی شود.
این یادداشت بر پایان جنگ و ترتیبات آتش بس متمرکز است. این تفاهم نامه شامل تسهیل دریانوردی در تنگه هرمز است.
این تفاهم نامه شامل خروج ناوگان آمریکایی از مجاورت ایران است.
این تفاهم نامه شامل آزادسازی نیمی از وجوه مسدود شده ایران است که بالغ بر 12 میلیارد دلار است.
این یادداشت شامل پایان محاصره نظامی دریایی ایالات متحده است. مهلت 30 روزه برای دستیابی به توافق هسته ای پس از امضای چارچوب توافق داده شد.
@withyashar</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/withyashar/12267" target="_blank">📅 01:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12266">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">فارس : ایران هیچ توافق هسته ای هم با امریکا نداشته
@withyashar</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/withyashar/12266" target="_blank">📅 01:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12265">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دقایقی پیش صداسیما گفت ادعای ترامپ در خصوص بازگشایی تنگه هرمز دروغ است و تنگه دست ایران خواهد ماند
@withyashar</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/withyashar/12265" target="_blank">📅 00:58 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12264">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScfjMM9ruvVmulGwgg7vRHMHOtNdJdUPB68RFPln6TyalxaQvIzlebDvSbwxxz9qKynKg0_ZyY2DTicjRDrXOSb_SvQsCfP3j90VbXz6LkoPCxLhkOSiR2ZAAoajJWO2N-tkK70XFQnjc8cuotuTQUAidXKgFQJHcVNrvlhM1GN25yrEVdciNSm78xfAJq1hvQnNZN2G8R61PgSJhyL6U4CfeRrL8QHbSkH9zgy7akV9PF865KemLuW_OO4yM6_b_oCn5GdchNv36zxrzONPkrrmfOp_1te1BDTP40Pl4SF07Kv9Yh46_IUYS2Md_6nyGU8q6Bqu4sqAOZCIHEDM0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ کمی پیش در حال تماس با سران کشورها
@withyashar</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/withyashar/12264" target="_blank">📅 00:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12263">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خبرنگار کانال 12 اسرائیل:
ترامپ تسلیم خواسته های ایران شد
@withyashar</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/withyashar/12263" target="_blank">📅 00:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12262">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer"><a href="https://t.me/withyashar/12262" target="_blank">📅 00:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12261">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/withyashar/12261" target="_blank">📅 00:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12260">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA M</strong></div>
<div class="tg-text">یاشار فکر میکنم خیلیا که پنیک میکنن تازه به جمعمون اضافه شدن
اونای که قدیمین فقط میشینن به این اتفاقات میخندن چون از چیزای با خبرن و شناخت دارن که بقیه نمیفهمن
البته این اتفاق زمانی میفته که نقشه راهو نداشته باشی
ولی ما که میدونیم چه خبره
😉</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/withyashar/12260" target="_blank">📅 00:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12259">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/withyashar/12259" target="_blank">📅 00:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12258">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/withyashar/12258" target="_blank">📅 00:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12257">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/withyashar/12257" target="_blank">📅 00:24 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12256">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChhT0jrhuBy3hc6C8PI_JIDM4OQREeX96am0qwmfPMvuqCGEaeVTpCX94PVQp4zPqUA8Vkj4aM93njJJ8V5r77k6St_I5oToxtIkthqqegh27F9atK32z6_hxetVNrCusi3CkCA_eRIOfvX4MyYiXiqDgJQ3FjwLHrAAMvBE4XO4pKLzG4fldWvL1T2DCsvLccHJoC-rDz9NQ0EEQdzCv6kvoqszxSVsDbBiUX1e669SmqBGucYGaUph8tYzGM-V9kpUgvNVVLCgmJx4IiptBuCbagRb-Ak3QFsPXhOwgvJxdo80XBS3RraDJxjxuG2m7lX064YRVRgZEmRuBKDxjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۸ سوخت رسان از اسرائیل بلند شدن شاید بیشترم بشن هنوز چند تا رو باندن دارن پا میشن !!!!!
@withyashar</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/withyashar/12256" target="_blank">📅 00:17 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12255">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فقط کی حالتو خوب‌ میکنه ؟ عمو یاشار حالا اگه این پست رو ریکشن آتیش فقط بزنی میگم</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/withyashar/12255" target="_blank">📅 00:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12254">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anvZM_3HMyeD_J6MZSB6lJpJDYZfKRZ6oV7_sai4enh47cPJsQzoHl3aN538ccZykOgkiKeaT51vdjySkazZiXjd0aBxy47cv_P5ru2rhas6GyUUf9SbR9XV1X1nQqwwCQ2MCse77vb3gFmLKrhuMLvjJNKCPN9i492s9C7a2mnPUOVGy9uYyPyU32ztP6It_9ZOn82t98uHvtex441l7kUUjWE2Ed_m5mNJuKdVk4sN2jsGN8TenrZNSY5kIcOqFtaltoew-SgpZQkzkiGj01SXTqJ7WdWhgrep1bk_ldJkw5JWqMEND6EJmVDSmglw-ozp3xGygC_jEG4LvQd5dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : «من اکنون در دفتر بیضی کاخ سفید هستم؛ جایی که همین حالا گفت‌وگوی بسیار خوبی با محمد بن سلمان آل سعود، عربستان سعودی؛ محمد بن زاید آل نهیان، امارات متحده عربی؛ امیر تمیم بن حمد آل ثانی، نخست‌وزیر محمد بن عبدالرحمن بن جاسم آل ثانی و وزیر علی الثوادی از قطر؛ فیلدمارشال سید عاصم منیر احمد شاه از پاکستان؛ رجب طیب اردوغان، رئیس‌جمهور ترکیه؛ عبدالفتاح السیسی، رئیس‌جمهور مصر؛ ملک عبدالله دوم، پادشاه اردن؛ و حمد بن عیسی آل خلیفه، پادشاه بحرین، دربارهٔ جمهوری اسلامی ایران و همهٔ مسائل مرتبط با یک یادداشت تفاهم مربوط به صلح داشتیم.
@withyashar
یک توافق تا حد زیادی مذاکره و تنظیم شده است، اما نهایی شدن آن میان ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلفی که نام برده شد، همچنان منوط به تکمیل جزئیات است.
@withyashar
به‌طور جداگانه، با نخست‌وزیر اسرائیل، بیبی نتانیاهو، نیز گفت‌وگو کردم که آن هم بسیار خوب پیش رفت.
جنبه‌ها و جزئیات نهایی توافق در حال حاضر در دست بررسی است و به‌زودی اعلام خواهد شد.
علاوه بر بسیاری از بخش‌های دیگر این توافق، تنگهٔ هرمز نیز بازگشایی خواهد شد.
از توجه شما به این موضوع سپاسگزارم
@withyashar</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/withyashar/12254" target="_blank">📅 00:03 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12253">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/withyashar/12253" target="_blank">📅 23:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12252">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ در تروث:  ممنونم رئیس‌جمهور اردوغان!  ترامپ همون رهبریه که دنیا قرن‌ها منتظرش بود فقط از قدرت حرف نمی‌زنه، خودش نماد قدرته. @withyashar</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/withyashar/12252" target="_blank">📅 23:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12251">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/withyashar/12251" target="_blank">📅 23:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12250">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/withyashar/12250" target="_blank">📅 23:42 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12249">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خبرنگار العربیه: مقر گروه‌های مخالف نظام ایران در «وادی آلانه» در اربیل با 4 پهپاد هدف حمله قرار گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/withyashar/12249" target="_blank">📅 23:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12248">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/withyashar/12248" target="_blank">📅 23:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12247">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18b7da70d7.mp4?token=i7l0JyjQ2DxbdwD3xC3Oq0XRuaKC9X9837DyOkt1B8yA-KQUKy4IdKo-Vam_NnG3QSQmJMJZDdnb03Uh8_-QY93zJ7bf_oMDxpsVG9sJYUD5_I0NS8zmRKr3u9srlDB3khSMYxxp7ieptzw_c8rCVROnRMgNO7iFS89MD_R3dhdOpYq8HuMjcjtjibsY3re0Y1Itek1IY8CLT1bCa6ONoGLBNr-MPULkMzKHrZvwkxw2HB1rq5AqR07qXJiVrXUdlsTVn3tYodebkMLCSRoKDLfOZ7ZVCIAVuHxSicbB52nf1aPXSnA3fQgnnKGltF8H5X47zz0yxIniJ72w8YyiNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b7da70d7.mp4?token=i7l0JyjQ2DxbdwD3xC3Oq0XRuaKC9X9837DyOkt1B8yA-KQUKy4IdKo-Vam_NnG3QSQmJMJZDdnb03Uh8_-QY93zJ7bf_oMDxpsVG9sJYUD5_I0NS8zmRKr3u9srlDB3khSMYxxp7ieptzw_c8rCVROnRMgNO7iFS89MD_R3dhdOpYq8HuMjcjtjibsY3re0Y1Itek1IY8CLT1bCa6ONoGLBNr-MPULkMzKHrZvwkxw2HB1rq5AqR07qXJiVrXUdlsTVn3tYodebkMLCSRoKDLfOZ7ZVCIAVuHxSicbB52nf1aPXSnA3fQgnnKGltF8H5X47zz0yxIniJ72w8YyiNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیت رهبری رو جوری زدن که شده بیابان
@withyashar</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/withyashar/12247" target="_blank">📅 23:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12246">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">رویترز:
یک چارچوب سه مرحله‌ای برای مذاکرات آمریکا و ایران پیشنهاد شده:
پایان رسمی جنگ.
حل و فصل بن‌بست تنگه هرمز .
باز کردن پنجره مذاکره ۳۰ روزه برای توافقی گسترده‌تر.
امکان تمدید آتش بس نیز وجود دارد.
@withyashar</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/withyashar/12246" target="_blank">📅 23:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12245">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">کنسول جمهوری آذربایجان در تبریز بر اثر تصادف در اتوبان جلفا-تبریز جان باخت.
@withyashar</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/withyashar/12245" target="_blank">📅 23:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12244">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سناتور لیندسی گراهام:
اگه با ایران توافق کنیم فقط بخاطر اینه که چون فهمیدیم نمی‌تونیم تنگه هرمز رو از دست ایران حفظ کنیم و ایران هنوز هم میتونه زیرساخت‌های نفتی خلیج فارس رو نابود کنه؛ یعنی اون‌وقت ایران به‌عنوان قدرت غالب منطقه شناخته میشه و همه مجبور میشن باهاش دیپلماتیک کنار بیان.
اینکه ایران بتونه همیشه تنگه هرمز رو به‌هم بریزه و همزمان توان ضربه سنگین به نفت خلیج فارس رو داشته باشه، موازنه قدرت منطقه رو کامل عوض میکنه و در آینده واسه اسرائیل تبدیل به کابوس میشه.
من شخصاً قبول ندارم که نشه جلوی توان ایران رو گرفت یا منطقه نتونه از خودش در برابر قدرت نظامی ایران دفاع کنه. باید خیلی حواسمون باشه که این قضیه رو خراب نکنیم.
@withyashar</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/withyashar/12244" target="_blank">📅 23:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12243">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خبرنگار لبنانی در شبکه سه: حزب‌الله بر روی نابودکردن گنبد آهنین اسرائیل تمرکز کرده است!
@withyashar</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/withyashar/12243" target="_blank">📅 23:12 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12242">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">توییت مارک لوین:
شما متحدی را که در یک عملیات نظامی بزرگ در کنار شما جنگیده است، کنار نمی‌گذارید. یا این فقط یکی دیگر از فهرست طولانی تهمت‌ها علیه نتانیاهو است که نیویورک تایمز و جروزالم پست بدنام از او متنفرند، یا یک اشتباه استراتژیک بسیار بزرگ است.
@withyashar</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/withyashar/12242" target="_blank">📅 23:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12241">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/withyashar/12241" target="_blank">📅 23:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12240">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/withyashar/12240" target="_blank">📅 23:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12239">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پرواز گسترده جنگنده های آمریکایی در نزدیکی مرز ایران
@withyashar</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/withyashar/12239" target="_blank">📅 23:02 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12238">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">علی خضریان، عضو کمیسیون امنیت ملی مجلس :
در هر توافقی ایران حتما باید غرامت جنگ را دریافت کند.
شرایط تنگه هرمز به قبل از جنگ برنخواهد گشت این دستاورد و  مطالبه رهبری است .
مطالبه ملت ایران است که از مدیریت تنگه هرمز عقب‌نشینی نشود
@withyashar</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/withyashar/12238" target="_blank">📅 22:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12237">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گروه کرد ایرانی کومله می‌گوید پهپادها کمی پیش پایگاه‌های آن را در استان اربیل، کردستان عراق، مورد حمله قرار دادند، در حالی که پهپادهایی توسط «هواپیماهای ائتلاف» سرنگون شدند.
@withyashar</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/withyashar/12237" target="_blank">📅 22:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12236">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">همین الان دارن میجنگن فقط تو عراق
😂</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/withyashar/12236" target="_blank">📅 22:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12235">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">جنگنده‌های نیروی هوایی ایالات متحده در حال حاضر بر فراز منطقه خلیفان در استان اربیل در شمال عراق پرواز می‌کنند تا پهپادهای ایرانی را که گروه‌های مخالف کرد-ایرانی در منطقه را هدف قرار داده‌اند، رهگیری کنند.
@withyashar</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/withyashar/12235" target="_blank">📅 22:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12234">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فاکس نیوز:هنوز هیچ توافقی بین رژیم جمهوری اسلامی و آمریکا صورت نگرفته
@withyashar</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/withyashar/12234" target="_blank">📅 22:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12233">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یاشار جان این ترامپ اشتباهی بجای اینکه مارو ببره قاهره داره میبره بورکینافاسو
😂
😂
😂</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/withyashar/12233" target="_blank">📅 22:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12232">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahdi</strong></div>
<div class="tg-text">یاشار جان این ترامپ اشتباهی بجای اینکه مارو ببره قاهره داره میبره بورکینافاسو
😂
😂
😂</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/withyashar/12232" target="_blank">📅 22:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12231">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کانال 14 اسرائیل: چند منبع معتبر تأیید می‌کنند که ایران با برخی از درخواست‌های کلیدی ایالات متحده موافقت کرده است و کمتر از 24 ساعت دیگر اعلام توافق انجام خواهد شد که به تهران چند ماه فرصت می‌دهد تا کاملاً تسلیم شود
@withyashar</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/withyashar/12231" target="_blank">📅 22:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12230">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نخست‌وزیر اسرائیل، بنیامین نتانیاهو، به منظور بررسی آخرین تحولات مذاکرات با ایران، جلسه امنیتی محدودی برگزار خواهد کرد. یک منبع اسرائیلی در گفت‌وگو با سی‌ان‌ان این خبر را اعلام کرد.
@withyashar</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/withyashar/12230" target="_blank">📅 22:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12229">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کانال ۱۴ اسرائیل:
چند منبع معتبر تأیید می‌کنند که ایران با برخی از درخواست‌های کلیدی ایالات متحده موافقت کرده است و کمتر از ۲۴ ساعت دیگر اعلام توافق انجام خواهد شد که به تهران چند ماه فرصت می‌دهد تا کاملاً تسلیم شود.
﻿
@withyashar</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/withyashar/12229" target="_blank">📅 22:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12228">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">هم اکنون تماس تلفنی نتانیاهو و ترامپ! @withyashar</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/withyashar/12228" target="_blank">📅 22:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12227">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ با سران منطقه گفتگو کرد
آکسیوس:
ترامپ روز شنبه با رهبران عربستان سعودی، امارات متحده عربی، قطر، مصر، ترکیه و پاکستان تماس تلفنی داشت.
به گفته منبعی که از جزئیات این تماس مطلع شده، چند تن از این رهبران عرب از ترامپ خواستند که توافق را بپذیرد.
@withyashar</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/withyashar/12227" target="_blank">📅 22:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12226">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">هم اکنون تماس تلفنی نتانیاهو و ترامپ!
@withyashar</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/withyashar/12226" target="_blank">📅 22:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12225">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/withyashar/12225" target="_blank">📅 21:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12224">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">هم اکنون جلسه اضطراری امنیت ملی دولت ترامپ در اتاق جنگ کاخ سفید در حال برگزاری است.
@withyashar</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/withyashar/12224" target="_blank">📅 21:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12223">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/withyashar/12223" target="_blank">📅 21:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12222">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">به گفته یک مقام آمریکایی که توسط اکسیوس نقل شده است، دونالد ترامپ هنوز تصمیم نهایی خود را در مورد این توافق نگرفته است
@withyashar</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/withyashar/12222" target="_blank">📅 21:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12221">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">من که میدونیم ترامپ کار رو در میاره ولی این رسمش‌ نبود که این کارا رو با ما بکنه
😂
@withyashar</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/withyashar/12221" target="_blank">📅 21:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12220">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">الحدث به نقل از یک منبع عالی‌رتبه: تنها ساعات کمی تا اعلام توافق بین آمریکا و ایران فاصله است
@withyashar</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/withyashar/12220" target="_blank">📅 21:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12219">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">معاون رئیس‌جمهور ونس به کاخ سفید رسید
۱ دقیقه تا تماس تصویری ترامپ با شیوخ کشور های خلیج فارس
@withyashar</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/withyashar/12219" target="_blank">📅 21:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12218">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/withyashar/12218" target="_blank">📅 21:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12217">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromParisa</strong></div>
<div class="tg-text">یاشار جان خسته نباشی
تو ویس های آخرت احساس ناامیدی کردم والا تو ماشین نشستم گریه میکنم
ما به امید شما امیدواریم
من پدرام مادرم بالای ۸۰ دارن و مریضن و من دیگه نمیتونم برم ایران ببینمشون
به امید ویس  و تحلیل های شما تا حالا گذروندم
✌🏼
💔</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/withyashar/12217" target="_blank">📅 21:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12216">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c3610291d.mp4?token=pfmiCDRl_z5UBBV7h8RdfW5I-IwdpflbFXOvc7m02i_6pCTjKNWr3pmaklECl8_83xuUjHu-DQxG8VCA5nTgbA5No4OZYQyy0kmdzHqbIPQg91VzDd3b2E4RbNWeWlM2i2HUB-jXgVD44FRmrKrZHVYRpDbySm_oSbnONPywee4cyOQRmLqIqYk-OEe2RfoqS59fcdzJZUgubQ8hGQ82NS2ZYGq4j52BIRw6tHSltzIWWv29rVwllvP2tiH9MLkzQzQuMKyNtBuzuKvrBP9BXduPp9loTUQZfuSvtlA5mD0cKUhz6DpVQCBETqrSqMYjNISEQwlqC4vLrNM0n0ie_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c3610291d.mp4?token=pfmiCDRl_z5UBBV7h8RdfW5I-IwdpflbFXOvc7m02i_6pCTjKNWr3pmaklECl8_83xuUjHu-DQxG8VCA5nTgbA5No4OZYQyy0kmdzHqbIPQg91VzDd3b2E4RbNWeWlM2i2HUB-jXgVD44FRmrKrZHVYRpDbySm_oSbnONPywee4cyOQRmLqIqYk-OEe2RfoqS59fcdzJZUgubQ8hGQ82NS2ZYGq4j52BIRw6tHSltzIWWv29rVwllvP2tiH9MLkzQzQuMKyNtBuzuKvrBP9BXduPp9loTUQZfuSvtlA5mD0cKUhz6DpVQCBETqrSqMYjNISEQwlqC4vLrNM0n0ie_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر جنگ پیتر هگستث
:
اولین حمله هوایی که هرگز انجام دادم و یک دسته را در وسط شب در بغداد رهبری کردم. ما ۳۶ ساعت برای آماده‌سازی داشتیم و من هر دقیقه از آن ۳۶ ساعت را صرف آماده‌سازی کردم.
وقتی خلبان‌ها ما را چند صد متر در نقطه اشتباهی در وسط یک زمین گل‌آلود فرود آوردند و GPS کار نمی‌کرد.
یک مرد بود که آن دسته به او نگاه می‌کردند و آن مرد من بودم.
@withyashar</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/withyashar/12216" target="_blank">📅 21:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12215">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/withyashar/12215" target="_blank">📅 21:19 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12214">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/withyashar/12214" target="_blank">📅 21:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12213">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/withyashar/12213" target="_blank">📅 21:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12212">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/withyashar/12212" target="_blank">📅 21:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12211">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/withyashar/12211" target="_blank">📅 21:12 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12210">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">انتظار می‌رود ایالات متحده و ایران تا بعدازظهر یکشنبه توافقنامه صلحی را اعلام کنند که هدف آن پایان دادن به درگیری‌ها در تمام جبهه‌ها است، طبق گزارش واشنگتن تایمز.
پیش‌نویس پیشنهادی اوایل شنبه نهایی شد و برای تأیید نهایی به رهبران هر دو کشور ارسال گردید.
شخصیت‌های کلیدی در تأیید این پیش‌نویس شامل محمدباقر قالیباف، رئیس مجلس ایران، معاون رئیس‌جمهور جی‌دی ونس، استیو ویتکاف و جارد کوشنر بودند.
@withyashar</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/withyashar/12210" target="_blank">📅 21:07 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12209">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91cac439eb.webm?token=AAteWRnCYfYkkB4ueuiF63OYgSB8RBeDTM6z8MWAG4RjRLxEsMAi39J-_csWmTYphQGFQ-P-A2o8EtA4tG34yhPTN_hdebKHpkfA-9hB5Eokml9qj4OwzrmbP3iMHyHAxYOARPo32NNB4Z447a-iIl-XTr5ujEp1tpT4Tl6SYA4PlblcPxVaqCqz4mb6wE_xTgEic5_MdwdGlziuoM_9LONecCY5_65td3fIoTdh5PEpUuMV-AL7sDWPt0MJUlxVSFbiIerMctyvVkyRygUpngyg8EJ-z6RWJTeYq5lJUle2eVT0Sz9b0fme916vRFG9Agd1VclZEIwLi2XPLh4uTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91cac439eb.webm?token=AAteWRnCYfYkkB4ueuiF63OYgSB8RBeDTM6z8MWAG4RjRLxEsMAi39J-_csWmTYphQGFQ-P-A2o8EtA4tG34yhPTN_hdebKHpkfA-9hB5Eokml9qj4OwzrmbP3iMHyHAxYOARPo32NNB4Z447a-iIl-XTr5ujEp1tpT4Tl6SYA4PlblcPxVaqCqz4mb6wE_xTgEic5_MdwdGlziuoM_9LONecCY5_65td3fIoTdh5PEpUuMV-AL7sDWPt0MJUlxVSFbiIerMctyvVkyRygUpngyg8EJ-z6RWJTeYq5lJUle2eVT0Sz9b0fme916vRFG9Agd1VclZEIwLi2XPLh4uTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/withyashar/12209" target="_blank">📅 21:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12208">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اتاق جنگ با یاشار : متوجه شدین چی‌شده ؟ از امروز تا پایان جام جهانی میشه ۵۷ روز ! آتش بس ۶۰ روزه یعنی دقیق ۳ روز بعد از فینال که همه برگشتن !
@withyashar</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/withyashar/12208" target="_blank">📅 21:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12207">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">کانال ۱۳ اسرائیل: اگر آتش‌بس به مدت ۶۰ روز تمدید شود، این گام کاملا مغایر با خواسته‌ها و اهداف اسرائیل خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/withyashar/12207" target="_blank">📅 20:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12206">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">لیبرمن وزیر دفاع سابق اسرائیل:
هر توافق آمریکا با ایران برای ما فاجعه است.
@withyashar</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/withyashar/12206" target="_blank">📅 20:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12205">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گزارش‌ها حاکی از بازگشت اضطراری «جی‌دی ونس» معاون اول رئیس‌جمهور آمریکا به کاخ سفید و برگزاری نشست امنیتی ترامپ درباره ایران است.
«جی‌دی ونس» معاون اول رئیس‌جمهور آمریکا سفرهای خود را نیمه‌تمام گذاشته و به طور اضطراری به کاخ سفید بازگشت
@withyashar</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/withyashar/12205" target="_blank">📅 20:54 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12204">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">لیندری گراهام، سناتور ارشد جمهوری‌خواه و دوست نزدیک دونالد ترامپ، به آکسیوس گفت که رهبران منطقه در توصیه‌های خود به دونالد ترامپ اختلاف نظر دارند و برخی از او برای ضربه زدن به ایران برای تضعیف دولتش و دستیابی به توافقی بهتر فشار می‌آورند، در حالی که برخی دیگر به همراه برخی از مشاوران ارشد کاخ سفید از او خواستند که پیشنهاد فعلی را بپذیرد.
گروه اخیر استدلال کردند که ایران توانایی تخریب زیرساخت های نفتی مهم خلیج فارس را در صورت حمله حفظ می کند و امنیت تنگه هرمز را نمی توان در برابر نفوذ ایران تضمین کرد.
@withyashar</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/withyashar/12204" target="_blank">📅 20:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12203">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ در تروث:
ممنونم رئیس‌جمهور اردوغان!
ترامپ همون رهبریه که دنیا قرن‌ها منتظرش بود فقط از قدرت حرف نمی‌زنه، خودش نماد قدرته.
@withyashar</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/withyashar/12203" target="_blank">📅 20:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12202">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">کانال ۱۳ اسرائیل: نیروهای دفاعی اسرائیل در حالت آماده‌باش کامل به‌دلیل احتمال شکست مذاکرات و از سرگیری درگیری‌ها هستند.
نیروهای نظامی نگرانی‌هایی درباره مفاد کلیدی از جمله عدم توقف غنی‌سازی اورانیوم ایران و ادامه توسعه موشک‌های تهران ابراز کردند.
@withyashar</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/withyashar/12202" target="_blank">📅 20:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12201">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">شبکه 12 اسرائیل : نتانیاهو امشب با رهبران ائتلاف دولتیش یه جلسه برگزار می‌کنه
@withyashar</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/withyashar/12201" target="_blank">📅 20:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12200">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/withyashar/12200" target="_blank">📅 20:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12199">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کانال 13 اسرائیل:
اسرائیل اطلاعاتی دریافت کرده که توافق با ایران ممکن شده.
@withyashar</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/withyashar/12199" target="_blank">📅 20:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12198">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">منبعی عالی‌رتبه به العربیه: نشانه‌ها درباره توافق بین آمریکا و ایران بسیار مثبت است.
@withyashar</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/withyashar/12198" target="_blank">📅 20:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12197">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">آکسیوس به نقل از مقامات اسرائیلی:
نتانیاهو عمیقاً نگران توافق مورد بحث است؛ نتانیاهو از ترامپ خواست تا دور جدیدی از حملات به ایران رو آغاز کنه.
@withyashar</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/withyashar/12197" target="_blank">📅 20:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12196">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خبرنگار کانال ۱۵، یوسی یهوشوا، می‌گوید احتمال درگیری مجدد با ایران بالا است مگر اینکه یکی از طرفین انعطاف نشان دهد؛ او نسبت به گزارش‌های مربوط به یک پیشرفت بزرگ شکاک است و با توجه به حجم شایعات در ساعات اخیر، به احتیاط فراخوانده است
@withyashar</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/withyashar/12196" target="_blank">📅 20:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12195">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">کانال ۱۲ اسرائیل
: استیو ویتکوف، نماینده آمریکا، در تلاش است تا به هر قیمتی به یک توافق دست یابد و بر رئیس‌جمهور ترامپ فشار می‌آورد که به جنگ با ایران بازنگردد.
@withyashar</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/withyashar/12195" target="_blank">📅 20:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12194">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fM3b-NxQvQS6QYxhegC_UrxJOwZtA8UwVNhZlXSS3RLibJh1OFvZdCEkVuL9sffiNMrShmrwO9ujv3Tr14y3s2rjceq18uNluarSwbchQBcnTOKXLc8gX_iPCFFGwxfAQ2ePY_fm5ZGup8RF0DE4dElYCcgAx0qh16H0f-4NOiLuN6jx-B1Xm9QXy776owS5lZz65p5d22sYmv-2cABHNRi0S5AovtoHGDQR5Cu0gscURpBZX2O6AwM0rHVUH5taO7d2KH6WZ8bshafJ2_YFfDHeOJ41KSs749QSa0XYSiJ8X-FVNQWzQRc1Mfi7P1pBCvledjiHwwOPOYDIAlUGJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترفند جهانی ترامپ: چگونه حمله به ایران و ونزوئلا به بازگشت اقتصادی آمریکا و مهار چین دامن می‌زند…
این مقاله ادعا می‌کند که سیاست‌های خارجی دونالد ترامپ در سال ۲۰۲۶—از جمله فشار بر ایران و ونزوئلا—باعث تغییر در بازار جهانی انرژی، تضعیف تأمین نفت ارزان برای چین و تقویت اقتصاد آمریکا شده است.
به گفته نویسنده:
سرمایه‌گذاری خارجی در آمریکا افزایش یافته
ارزش و استفاده جهانی از دلار بیشتر شده
شرکت‌های بزرگ در حال انتقال تولید به آمریکا هستند
چین مجبور شده نفت را با قیمت بالاتر بخرد
و آمریکا در رقابت ژئوپلیتیکی با چین دست بالا را پیدا کرده است
در مجموع، متن نتیجه می‌گیرد که این سیاست‌ها باعث «تقویت اقتصاد و قدرت جهانی آمریکا» شده، هرچند منتقدان آن را پرریسک و تنش‌زا می‌دانند
@withyashar</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/withyashar/12194" target="_blank">📅 20:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12193">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وضعیت ما بعد از حمله ، به زودی</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/withyashar/12193" target="_blank">📅 20:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12192">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/withyashar/12192" target="_blank">📅 20:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12191">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">وضعیت ما مردم ایران الان</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/withyashar/12191" target="_blank">📅 20:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12190">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9fecf1e31.webm?token=uM3wL2nSTXozrVWKitj9OmSdD7EcbYc9TWRVMCkdEmJRENQTy0yRNoUiwDJi5FWfhMhkS53gejwTbIeQ6bCGZbQfRzzijVQcInbt547p4QRILBPci0LnaONGaJ_kHA1cFfcyFfGMSeX_WyHi8FK7IXEo9-kf1WCGo-OUHcSby7mAdrg3umJe-LMeyYygntWW0KRYfw9eYKwjTtRuqlKOl38YcVWwodiDIm8InbZJCclW1lh62VJULcrUjGZTu6LdqPXDXBIhT-Hfy3wpNBHxQqXGdidqnOjv_K7SSJtWaz2vkj8P8pb4E1coIg1NcniTr4pWR9XgKl8zGb4ZNxF-QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9fecf1e31.webm?token=uM3wL2nSTXozrVWKitj9OmSdD7EcbYc9TWRVMCkdEmJRENQTy0yRNoUiwDJi5FWfhMhkS53gejwTbIeQ6bCGZbQfRzzijVQcInbt547p4QRILBPci0LnaONGaJ_kHA1cFfcyFfGMSeX_WyHi8FK7IXEo9-kf1WCGo-OUHcSby7mAdrg3umJe-LMeyYygntWW0KRYfw9eYKwjTtRuqlKOl38YcVWwodiDIm8InbZJCclW1lh62VJULcrUjGZTu6LdqPXDXBIhT-Hfy3wpNBHxQqXGdidqnOjv_K7SSJtWaz2vkj8P8pb4E1coIg1NcniTr4pWR9XgKl8zGb4ZNxF-QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/withyashar/12190" target="_blank">📅 20:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12189">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">آکسیوس به نقل از منابع: تماس ویدیو کنفرانس بین ترامپ و رهبران کشورهای عربی در مورد پیش نویس توافق با ایران ساعت ۵ بعد از ظهر به وقت گرینویچ انجام خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/withyashar/12189" target="_blank">📅 19:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12188">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ به کانال 12 اسرائیل   :
به نتانیاهو گفتم نگران نباش چون من توافقی که به نفع اسرائیل نباشه نمیکنم ، نتانیاهو نباید نگران باشه ، بعضیا خواهان توافقن و بعضی جنگ و نتانیاهو مابین این دو گیر کرده
@withyashar</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/withyashar/12188" target="_blank">📅 19:54 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12187">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رویترز از شکست مذاکرات در تهران خبر داد،
تهران هیچ امتیاز بیشتری در مذاکرات نداده و این امر منجر به شکست مذاکرات و بازگشت هیئت های پاکستانی و قطری از تهران شد.
@withyashar</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/withyashar/12187" target="_blank">📅 19:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12186">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سی‌بی‌اس در گفتگو با ترامپ: من پیش‌نویس یک توافق با ایران را دیده‌ام که برای من ارسال شده است.
او می‌گوید: «نمی‌توانم به رسانه‌ها بگویم که آیا با آن موافقت کرده‌ام یا نه، قبل از اینکه ایران را در جریان بگذارم.»
@withyashar</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/withyashar/12186" target="_blank">📅 19:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12185">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ به آکسیوس: برخی ترجیح میدهند توافق را منعقد کنند ، برخی دیگر ترجیح میدهند جنگ را از سر بگیرند‌‌
@withyashar</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/withyashar/12185" target="_blank">📅 19:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12184">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">هگست، وزیر جنگ آمریکا: ارتش ما عاشق غرق کردن نیروی دریایی دشمنه و من بهشون گفتم که تنها نیروی دریایی‌ای که درحال حاضر می‌تونید غرق کنید، نیروی دریایی ایرانه
@withyashar</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/withyashar/12184" target="_blank">📅 19:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12183">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ به اکسیوس:
شانس توافق یا جنگ 50/50 است. بعد از دیدار با نمایندگانم تصمیم میگیرم!
امروز با نمایندگان خود دیدار خواهم کرد و تا فردا(یکشنبه) تصمیم خواهم گرفت!
تنها توافقی را در رابطه با غنی سازی اورانیوم و سرنوشت ذخایر آن است را میپذیرم‌‌
یا چنان محکم‌تر از همیشه به آنها حمله نظامی می کنم که تا حالا مثل آن را ندیده‌اند، یا توافقی خوب را امضا می‌کنیم
@withyashar</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/withyashar/12183" target="_blank">📅 19:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12182">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">العربیه : ایران پیشنهاد تعلیق غنی‌سازی اورانیوم بالای 3.6% را به مدت 10 سال ارائه داد @withyashar</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/withyashar/12182" target="_blank">📅 19:04 · 02 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

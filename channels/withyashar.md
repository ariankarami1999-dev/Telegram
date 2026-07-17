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
<img src="https://cdn4.telesco.pe/file/dL9sMLxqA4yDGGTsZhOrp9saIv2hCznBtK5sqbXZUHHLYRfW7Sa7-BvTY3nQz_tTNWeN52cYqShsiJjEPTlyXiDt0LLAoeItlT021Q9U5CYHb8E58HbvVcKiCD17jy-XDd0UbXrtTd8StZffNfVq2Y5rivJNvEdPPSEfNACBkhDVF10voTlYota7a-qR3UqpIzfHiTFPaXtxGP8xEckVMDXkhW5A98CqV0cj6_QRHIyovEwHA9VkTgGHjUbARCLMq1BHr4pLaHYgBPFMPP24cOeGnMAQsrOov_pbUxQOlstxQufGyoLGpKQTBxKP1Ovd9XFi3dV-FFrr_2CI0GYDAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 400K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 14:08:44</div>
<hr>

<div class="tg-post" id="msg-18543">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C79NYK6W9Natm7F47m9Qk-Xpcek8nqFjI2K5k6NaOejuPXiv97qMW_BXXwv-OwoNqf_LEs2jh3XHV5NkKafQC_HSFSb5O284WeliKf68ygcmNZNm-61eZTyGO_zAJuV4F1Y1W3M51d7q2eLbTeCizn7jAuXD4p9C3pNgAW_MumC6NJEqHlbLTB4nBM0Kh7W2nwHkdRPNSkT6egUtm_rJ4tIjMG1BLE_vt0ccganqzLD1rTAyarkQnbefXICHTYlXEkVLa2VVtD7Wh5p5Q2I-SbP-quABu-XPYeA6qvcj0RDl6aAc1rjfvaiOB8YVczFGT0-vTElOC4PA9lPSNNXS4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تتر تا ۱۹۵،۰۰۰ تومان پرواز کرد و هم اکنون ۱۹۲،۰۰۰ معامله میشود
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/withyashar/18543" target="_blank">📅 13:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18542">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/315ffdb490.mp4?token=WFEYCQ0Y231IzhUkiCKbPzVoI5-w52zt94KCgXguqecQwi3CfXDJmbj6WxFkaa_S8XM9VpDCl1Fzx6tcEtShcwoDxaYGaerPbC4iIXHP_ykqpz43Ktnav6SQ7HYN-uh4Y5fHVGEhQ22POc39M7DCxz8t9nyrxjdMNI0xqte05MwSMapOrgwaLXMG1ITV5Y-GEEkFlwfmEJ22oXjIIifJhdMBkPPNHIgLPbQ-s_hJDHEGM5lnAXAVRpnDJdsWLgN56awAcDh_xtSG9THMdt5eYu0vQXZr67OvpbeHVu47svRxK5KqI0pN1ByEkggrp4aCzcTYeYFGj54z3iLY6aTbhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/315ffdb490.mp4?token=WFEYCQ0Y231IzhUkiCKbPzVoI5-w52zt94KCgXguqecQwi3CfXDJmbj6WxFkaa_S8XM9VpDCl1Fzx6tcEtShcwoDxaYGaerPbC4iIXHP_ykqpz43Ktnav6SQ7HYN-uh4Y5fHVGEhQ22POc39M7DCxz8t9nyrxjdMNI0xqte05MwSMapOrgwaLXMG1ITV5Y-GEEkFlwfmEJ22oXjIIifJhdMBkPPNHIgLPbQ-s_hJDHEGM5lnAXAVRpnDJdsWLgN56awAcDh_xtSG9THMdt5eYu0vQXZr67OvpbeHVu47svRxK5KqI0pN1ByEkggrp4aCzcTYeYFGj54z3iLY6aTbhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پل مسیر به گچین و بندرعباس
@WarRoom</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/withyashar/18542" target="_blank">📅 13:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18541">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خبرگزاری CNN: ترامپ در حال دریافت گزینه‌هایی برای گسترش عملیات نظامی آمریکا علیه ایران است
@WarRoom</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/withyashar/18541" target="_blank">📅 13:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18540">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ونس به NBC نیوز : فکر نکنید کنترل امنیت تنگه هرمز کار آسونیه؛ این کار حسابی دردسر داره، چون با پهپادهای ارزون‌ قیمت خیلی راحت میشه کشتی‌ها رو هدف قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/withyashar/18540" target="_blank">📅 13:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18539">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سپاه: جنگنده‌ها و سوخت‌رسان‌های آمریکا در اردن و مواضع آمریکا در کویت را هدف قرار دادیم
سپاه پاسداران اعلام کرد در
موج ۱۴ عملیات نصر ۲
و در واکنش به حملات پنجشنبه شب آمریکا، با موشک‌های بالستیک و پهپادها جنگنده‌ها و سوخت‌رسان‌های آمریکا در
اردن
را در دو مرحله هدف قرار داده که به ادعای این نهاد،
چند فروند سوخت‌رسان و جنگنده منهدم و تعدادی دیگر به‌شدت آسیب دیده‌اند.
سپاه همچنین در
موج ۱۵ عملیات نصر ۲
مدعی شد علاوه بر
انهدام سکو و موشک‌های هایمارس در کویت
، با حمله موشکی و پهپادی
چندین محل استقرار نیروهای آمریکایی و «ضدانقلاب»
را هدف قرار داده است. این نهاد مشخص نکرده منظور از «ضدانقلاب» چه گروه‌هایی است.
@WarRoom</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/withyashar/18539" target="_blank">📅 13:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18538">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d31df15619.mp4?token=A5E8S4G2TcRYsYoLQHmYQ0F72HEENbB_1uV6dU4vYtIBy-2owkpMgv4JEe6Ca1us-3-1KkMWLMZ_vibWPND8yFxaIUnGbVjEciiAOv4vLvgrCr9sgR4xxJZj4iTJZeGBCZxTQTp5Lqx0IMDGkWWKQfLSapTvU96QX-50fnn6Ky8Rj03vNiU8uEDZsDKMV7tQ_T2lPMaFFj-HnBd1YwXQaHeL877okZN9qpoMMlMMP-rwQi6yXmwHZcT0aQXbx6kpb8SyHG0Xe7rv7vB-frGvDN70n9DBLb8LKg0_HkjVT4B-54mOUWiFzOuJ4IwhMPazpICyX9OXCu5-zOd4eyIxcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d31df15619.mp4?token=A5E8S4G2TcRYsYoLQHmYQ0F72HEENbB_1uV6dU4vYtIBy-2owkpMgv4JEe6Ca1us-3-1KkMWLMZ_vibWPND8yFxaIUnGbVjEciiAOv4vLvgrCr9sgR4xxJZj4iTJZeGBCZxTQTp5Lqx0IMDGkWWKQfLSapTvU96QX-50fnn6Ky8Rj03vNiU8uEDZsDKMV7tQ_T2lPMaFFj-HnBd1YwXQaHeL877okZN9qpoMMlMMP-rwQi6yXmwHZcT0aQXbx6kpb8SyHG0Xe7rv7vB-frGvDN70n9DBLb8LKg0_HkjVT4B-54mOUWiFzOuJ4IwhMPazpICyX9OXCu5-zOd4eyIxcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏کل وزارت صنعت معدن تجارت این روزا:
@WarRoom</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/withyashar/18538" target="_blank">📅 13:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18537">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca43767734.mp4?token=ViZKKC3vueqCYvLN2dpV8QAOQlj1qYckH5cRXSJdEaWGWB3_Ye8RSI2osfr8zUMyGfuCRCfrYWXGdTSXWuo9973x37Z-9gvqGrYaI7WwJBCFhTXEvKiBAkO5b49Ns88EZYy4Uw5xNKTyBxHNuUpMMbevH2YfxpgjiPm2BnL2v6RCF60Dx08ev72tW4nhHtFtlLMUdFYWiX3oNJXTNAzmKmsznL0USNDSnrOkSXR0JCa60AtAeokXqIY_I2BdIir5IuX_WXd0pA2k40mo_ddCYdXyENyzKwrMiSUvXZHUnA8lyYV6RLfi88kLAHFtvVXR2XnE6N1KFckbNKlmZz4FYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca43767734.mp4?token=ViZKKC3vueqCYvLN2dpV8QAOQlj1qYckH5cRXSJdEaWGWB3_Ye8RSI2osfr8zUMyGfuCRCfrYWXGdTSXWuo9973x37Z-9gvqGrYaI7WwJBCFhTXEvKiBAkO5b49Ns88EZYy4Uw5xNKTyBxHNuUpMMbevH2YfxpgjiPm2BnL2v6RCF60Dx08ev72tW4nhHtFtlLMUdFYWiX3oNJXTNAzmKmsznL0USNDSnrOkSXR0JCa60AtAeokXqIY_I2BdIir5IuX_WXd0pA2k40mo_ddCYdXyENyzKwrMiSUvXZHUnA8lyYV6RLfi88kLAHFtvVXR2XnE6N1KFckbNKlmZz4FYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایگاه هوایی  عقاب  در جنوب که در زیر کوه ساخته شده و قرار بود از جنگنده‌های نیروی هوایی ایران در مقابل حملات هوایی دشمن محافظت کند با حمله مواجه شده و تونل‌های ورودی و خروجی بسته شده
@WarRoom</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/withyashar/18537" target="_blank">📅 13:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18536">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc0c4907fb.mp4?token=uVGSBrVH42d8yJDCc5m2ORGDkAUbKtw443vNyoYJEp5P2C1y4QakljZ2OI3RMV0XFKXy8V1iHyjfXLFmt2N0fWUHRq1cPN5QXR4x5AxHsxHlxejohINz-IyZn0DPbCdwIARo1WPU54FsY2tAyoMmqocWmxe6EhJ8_SzclZuKr1tluR9CuE9Ehw42cMQBEMRL60RRt-uPpFlP7eUArGcppgFcsW1y4ifg0zTpIPKxTVkVj-V8S0mfb6q0e72qr5CJABrSqgdViCn20zr5ndCbIo9G-nQJLA93iKtLF01zC4M2u9ytu_8f0Fw24H2NOYFuAkZaQ26BOdrqugu2tAggNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc0c4907fb.mp4?token=uVGSBrVH42d8yJDCc5m2ORGDkAUbKtw443vNyoYJEp5P2C1y4QakljZ2OI3RMV0XFKXy8V1iHyjfXLFmt2N0fWUHRq1cPN5QXR4x5AxHsxHlxejohINz-IyZn0DPbCdwIARo1WPU54FsY2tAyoMmqocWmxe6EhJ8_SzclZuKr1tluR9CuE9Ehw42cMQBEMRL60RRt-uPpFlP7eUArGcppgFcsW1y4ifg0zTpIPKxTVkVj-V8S0mfb6q0e72qr5CJABrSqgdViCn20zr5ndCbIo9G-nQJLA93iKtLF01zC4M2u9ytu_8f0Fw24H2NOYFuAkZaQ26BOdrqugu2tAggNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت همین الان پل بندر خمیر که کامل از بین نرفته و خودرو سبک عبور میکند
@WarRoom</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/18536" target="_blank">📅 13:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18535">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حوثی‌های یمن به یک کشتی در تنگه باب‌المندب حمله کردند @WarRoom
🚨</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/withyashar/18535" target="_blank">📅 12:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18534">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ادعای اینتل‌واچ: سناتور لیندسی گراهام توسط سم نوویچوک تماسی
(استنشاق، بلع یا تماس پوستی)
کشته شده است
.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/18534" target="_blank">📅 12:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18533">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کانال ۱۲ اسرائیل : موج بعدی حملات آمریکا قراره خیلی شدیدتر باشه و‌ احتمالا تهران و بقیه شهر هارو هم بزنه.
@WarRoom</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/18533" target="_blank">📅 12:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18532">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">حوثی‌های یمن به یک کشتی در تنگه باب‌المندب حمله کردند
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/18532" target="_blank">📅 12:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18531">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کویت اعلام کرد که یکی از ایستگاه‌های تولید برق و تصفیه آب مورد حمله ایران قرار گرفته است، که این حمله خسارات زیادی به واحدهای تولید برق وارد کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/18531" target="_blank">📅 12:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18530">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/896d0f778e.mp4?token=oY4J06yYTzxo7FNw8tiBNukVWW1stsE1trKxBxkWaxND60BT0mJAwnDBAAxjvKX_VCklHDXOJg-GRT_IiSJIMjHD5fCDPKFcBmCCTYptXYAMRnqx6V3IMU5nBVG8AjQTnAhqPrkq_bE4SPRLVi22qPhRfVBZxlIH1OpYES2mGgSRhow4uo6bEPWx5-5GvT6pigd4uhJkUpt5S_kcpXx2SLZ8RHsAwz3m4YlJ9JzOh7il5Ym00Rdph-DBUvAP-i9wGDV11IFfQcBlmBc5jeCe4cvbohgnMP2Dew2Ft6RagTkHLcdP2K_hGkb-s13aGiQSnN1DYC9JJg8-y23lDOV1ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/896d0f778e.mp4?token=oY4J06yYTzxo7FNw8tiBNukVWW1stsE1trKxBxkWaxND60BT0mJAwnDBAAxjvKX_VCklHDXOJg-GRT_IiSJIMjHD5fCDPKFcBmCCTYptXYAMRnqx6V3IMU5nBVG8AjQTnAhqPrkq_bE4SPRLVi22qPhRfVBZxlIH1OpYES2mGgSRhow4uo6bEPWx5-5GvT6pigd4uhJkUpt5S_kcpXx2SLZ8RHsAwz3m4YlJ9JzOh7il5Ym00Rdph-DBUvAP-i9wGDV11IFfQcBlmBc5jeCe4cvbohgnMP2Dew2Ft6RagTkHLcdP2K_hGkb-s13aGiQSnN1DYC9JJg8-y23lDOV1ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همکنون با صدا درآمدن آلارم حمله هوایی در دوحه، پایتخت قطر، پدافند مشغول دفع حملات است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/18530" target="_blank">📅 12:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18529">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">آلارم حمله موشکی در پایتخت قطر دوحه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/18529" target="_blank">📅 12:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18528">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e27b43e6c.mp4?token=slsX7xgOfejKc_GqUE4Yj2VsW_f2oA4ftMyiUnluGnTkJP3sfDxxusRTmRSDDRrEfrvhcaqoadjUUMX9xqAoglVUqDxU7C2jMcuxWKtqyg1NzLUhplX-nSyg1Vlt2_6BXH1DscQ37h21srix4tEF87mhN7Af6d2ys5dRKIxupbuAXDYvMeWuqITe35K3yoDg3tvRfAE7anhxlWiAG7NSm_R0rUx2zM8lNUsQ_RLGHCgQiifxHMnDUc-Rd-W5sgqzlJsNwkskrQQBN1OQG3c3Ncl3tnvACqZIq3p-aCxv_-mIi8JvX2c-MnYS1E1rWP9hM6MMOkfUptR0iOyItZJoQzIUVKA5WmxEIvrcO07ZVbc2JtTKWF2zGyStjQOMWjcy_KK_axkuSW8SHSbiEIxIZJS1r7Wzt1w1rELmLCOYycnbsqti1HUT7QM23st_tsLMNXIZapUvIE-_xqHg-bE3Qlb3u2gIrqXPq9F7GiYs_yhrbM_P9gYZXJ61RQOT33mNioQZeaf1AdFAI8C-brRS_sbB7mOGj4r7IOFql8HlagMJsPXkz2BMfAtRL6yYN-bJj1Ytxdju5eOrYrDvF6kTdl_AT6yBhGeixmGqgJaP5mDbvrpGuBJL9-7r-HXVmp3DVExpAyoEhNMk7oWsrxqo8CQOtri3A6y7Sagar1W_yvM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e27b43e6c.mp4?token=slsX7xgOfejKc_GqUE4Yj2VsW_f2oA4ftMyiUnluGnTkJP3sfDxxusRTmRSDDRrEfrvhcaqoadjUUMX9xqAoglVUqDxU7C2jMcuxWKtqyg1NzLUhplX-nSyg1Vlt2_6BXH1DscQ37h21srix4tEF87mhN7Af6d2ys5dRKIxupbuAXDYvMeWuqITe35K3yoDg3tvRfAE7anhxlWiAG7NSm_R0rUx2zM8lNUsQ_RLGHCgQiifxHMnDUc-Rd-W5sgqzlJsNwkskrQQBN1OQG3c3Ncl3tnvACqZIq3p-aCxv_-mIi8JvX2c-MnYS1E1rWP9hM6MMOkfUptR0iOyItZJoQzIUVKA5WmxEIvrcO07ZVbc2JtTKWF2zGyStjQOMWjcy_KK_axkuSW8SHSbiEIxIZJS1r7Wzt1w1rELmLCOYycnbsqti1HUT7QM23st_tsLMNXIZapUvIE-_xqHg-bE3Qlb3u2gIrqXPq9F7GiYs_yhrbM_P9gYZXJ61RQOT33mNioQZeaf1AdFAI8C-brRS_sbB7mOGj4r7IOFql8HlagMJsPXkz2BMfAtRL6yYN-bJj1Ytxdju5eOrYrDvF6kTdl_AT6yBhGeixmGqgJaP5mDbvrpGuBJL9-7r-HXVmp3DVExpAyoEhNMk7oWsrxqo8CQOtri3A6y7Sagar1W_yvM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خیلی وطنپرستی ‌نبین حالت بد میشه
@WarRoom</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/18528" target="_blank">📅 12:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18527">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ورود تانک‌های ارتش اسرائیل در مناطق حداتا و حاریص در جنوب لبنان
@WarRoom</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/18527" target="_blank">📅 12:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18526">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">علیرضا فغانی داور فینال نشد.
فیفا رسماً اعلام کرد اسلاوکو وینچیچ، داور اسلوونیایی، قضاوت فینال جام جهانی 2026 بین آرژانتین و اسپانیا رو برعهده داره.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/18526" target="_blank">📅 12:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18525">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یک مسئول در حزب کومله کردستان ایران:
شش موشک به مقر ما شلیک شد، از این تعداد، سه موشک به مکانی اصابت کردند که در آن هشت نفر از نیروهای پیشمرگه کشته شدند، و سه موشک دیگر نیز در نزدیکی همان مکان سقوط کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/18525" target="_blank">📅 11:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18524">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ: هفته آینده خاورمیانه تغییر خواهد کرد و همه باید برای آن آماده باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/18524" target="_blank">📅 11:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18523">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کانال ۱۲ عبری: آمریکا در حال تهیه فهرست تازه‌ای از اهداف در ایران است که تاسیسات تولید و انتقال برق را شامل می‌شود
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/18523" target="_blank">📅 11:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18522">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فیلمه لحظه زدن پدافند کنار نیروگاه اتمی بوشهر @withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/18522" target="_blank">📅 11:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18521">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : ویدئوی منتسب به بندرعباس که راننده ای در حال رانندگی شیشه های ماشینش بر اثر موج انفجار خرد میشود، بسیار قدیمی و مربوط به جنگ چهل روزه و در مکان دیگری است من در میان جنگ پست کرده بودم
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/18521" target="_blank">📅 11:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18520">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نیروی دفاعی بحرین اعلام کرد امروز چندین حمله موشکی و پهپادی ایران را رهگیری و منهدم کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/18520" target="_blank">📅 11:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18519">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">وال استریت ژورنال: اختلاف میان محافل تصمیم‌گیرنده در ایران گسترش یافت
‏ گروهی به دنبال تشدید تقابل با آمریکا و کنترل تنگه هرمز هستند و گروهی با در نظر گرفتن محاصره دریایی و تشدید جنگ نگران وخامت اقتصادی هستند
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/18519" target="_blank">📅 11:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18518">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سپاه پاسداران صبح جمعه در بیانیه‌ای از «حمله غافلگیرانه» به سوریه خبر داد. در این اطلاعیه هدف حمله منطقه تنف و پایگاه نیروهای آمریکایی عنوان شده
@WarRoom
یاشار : خوب سوریه هم اضافه میشه به حمله کنندگان از امشب</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/18518" target="_blank">📅 11:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18517">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBhIegXES6v3lpoXNS-kDw_BdRcd7KYSZYOhth7oTGaKZJgsCo7H8fLlHAoGY6XRsoLISUUE-I5ISOY_4z8sAZAJzJWTv5gFiny8vvQaBXHmkb0DE6HRyHLVtrsEtI99iix-_hCs4mn6JAPnJ7kPLCIgaw2VwKL6gTBCJEmtNvDONob6PvJhCMroo5O4n6nSL2eFDBLKybxHqwuB0u2vNtWS9q0S-wI3h4d_m5TPIPOAb1MWbfR2KVR-WUAck7o8rwwvnhYlelpAhOSF0OVy7lJWALD5x99-RWF3zNfa68QVv-fCGrFDoLYEZl83CUyPB9QXpls3SBXf0_Kp6hP8_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵ صبح کل چابهار برج ریخت @WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/18517" target="_blank">📅 11:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18516">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxAIstTIriBy7VXBvAI40Kr9k9-_WcIFryactzwPsKPuvZQqMg9C8CP6S0UIn6QjwxS6er9PX_c9dv2_hP6EJ4XKR3LkieXuAITArghFyQmrwmkv7YAZo410yfnF2d6FvycPjhnTLrH2TKn56QeSBFx8kraKx1hJGZ9yRTqcpXWQbG5_MggiVK87-JB7BhNnq4_Iofpu002kIE1CkDXyzGmJJ331KJVJPG0XHulWRZB80TqEfJmj4sm8_j0P9hW8kZxdVbxd9C6N7a3tyYzBjU5dGtvHnH7GVQKQ9Tz3UQpt0hiePhKaGBhhrnRFPBjUUY-OC7IdH3NO_CVzdfksig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات هوایی اسرائیل با پهپاد،
یک مسجد در لبنان را هدف قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/18516" target="_blank">📅 10:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18515">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : دیشب عباس چپقچی هیچ جا نرفت و اون یک هواپیمای معراج چارتر ایران ترکیه معمولی بوده ادمین های بیسواد دنده دادن
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/18515" target="_blank">📅 10:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18514">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKa27mbgpiVBziYVXDizNd1-1NLUzfad8IlFbYsty708IfQBF5krcvBpic6tmZ5VHebhGMKQ3okOrJuoDCkjMoV4SgwFdTj9PtZ8Hv9Y2_GH6HihYT0hd563CnuiBSYNFrX_M-cFhWCgC3XQRfJErVK9lpuIkeWx8LfuxZVDzNDiDy07K2923K7snWD2NjZDh9zUCFSNrWgDvaD0w62WrAkQSOo-MR9Uz2Q7DSalx2T34oaMUbbFgMbqJJTEjCU4ZLcGvnNMjV82AbUUg_XNnloZ47OOCYUTG8slaw7_vnnhf4W3P-DFdSN3eM55_HmWOSdGywMuhlhrbevJMBGM6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکسی قدیمی از جی‌دی ونس، معاون رئیس‌جمهور آمریکا، با تی‌شرتی دارای نماد اتحاد جماهیر شوروی در شبکه‌های اجتماعی خبرساز شده است.
وب‌سایت راستی‌آزمایی Snopes تأیید کرده که عکس واقعی است، اما توضیح داده این تصویر مربوط به یک مهمانی هالووین است و ونس در آن لباس شخصیت کشتی‌کج نیکلای ولوکوف را پوشیده بود؛ کشتی‌گیری که با نمادهای شوروی شناخته می‌شد
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/18514" target="_blank">📅 10:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18513">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">حمله به یک نفتکش در نزدیکی سواحل عمان
سازمان عملیات تجاری دریایی بریتانیا اعلام کرد یک فروند نفتکش در شرق خصب در نزدیکی سواحل عمان با پرتابه‌ای ناشناخته مورد حمله قرار گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/18513" target="_blank">📅 10:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18512">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">رسانه هی رژیم
: پالایشگاه‌های نفت و پایگاه‌های نظامی آمریکا در بحرین مورد حملۀ مستقیم پهپادی قرار گرفتند.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18512" target="_blank">📅 09:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18511">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05fd2e417b.mp4?token=oKmE_dhVWRIZGGMnQes7HLh6xKHeIOTC0H82EA1or2KKLLEmOhwG3GoVndr-Lzjs4dPxNaNjLXmZwz42AdKgwYwBI-eYi89aI7h7Wh4ibLqqZ46OqCzn7sZoF9Xlp3NzEie9p3jnDaYB2u6OhZB95d9Ai5oVoPShWfoRDg1xUbHCgDucAVnh6XbLkjnkaRmmOPtS4eeQPf9Ywt75LjrnJCCbUCuA8YP3kv4zfyoXUrbsQEPsAIUBHDcI-JrZyQctnqzh4PjLY4-7mFcRKkqgb1J8e5pPHW8Qi6pTM_21cAiEK61YNSbWwmpCDwYoe84SDgEykxZiZ4k2yaVxmrKutw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05fd2e417b.mp4?token=oKmE_dhVWRIZGGMnQes7HLh6xKHeIOTC0H82EA1or2KKLLEmOhwG3GoVndr-Lzjs4dPxNaNjLXmZwz42AdKgwYwBI-eYi89aI7h7Wh4ibLqqZ46OqCzn7sZoF9Xlp3NzEie9p3jnDaYB2u6OhZB95d9Ai5oVoPShWfoRDg1xUbHCgDucAVnh6XbLkjnkaRmmOPtS4eeQPf9Ywt75LjrnJCCbUCuA8YP3kv4zfyoXUrbsQEPsAIUBHDcI-JrZyQctnqzh4PjLY4-7mFcRKkqgb1J8e5pPHW8Qi6pTM_21cAiEK61YNSbWwmpCDwYoe84SDgEykxZiZ4k2yaVxmrKutw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپاد MQ-9 در آسمان چابهار.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18511" target="_blank">📅 07:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18510">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/18510" target="_blank">📅 07:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18509">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12de77f1cb.mp4?token=oXOd1DVL0dMTWLCm0XdYgzj0MGQ0BgvqpFmlxfsCdZyMIBcgmjjDUo37YIkkYCiqCI5AQpBswZXh5z-cmctjPQiYHG2LvcgcuzFp9H0czvwL3QNHCY1iBtaYoWcxCnZAprOtiIIlYmfPpMXF-wW9okWn6u0Hhpe2HuI539zMr4wAGbBaIDT_SmS-0Y2GBblvb5a5AlNrddaR_Zp5i-ARiLH5nZjixGBm9jC-AF2e5pMsl50O-VSd09RJyC-5Ad-tq_ewAG-IXEJlxqyQhQM89JQtDNP0jnSUlefRTw9-fZKfAJ-MmG0t6r4HCmhrVi3boWcepJd9xlInrcqr5HD9TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12de77f1cb.mp4?token=oXOd1DVL0dMTWLCm0XdYgzj0MGQ0BgvqpFmlxfsCdZyMIBcgmjjDUo37YIkkYCiqCI5AQpBswZXh5z-cmctjPQiYHG2LvcgcuzFp9H0czvwL3QNHCY1iBtaYoWcxCnZAprOtiIIlYmfPpMXF-wW9okWn6u0Hhpe2HuI539zMr4wAGbBaIDT_SmS-0Y2GBblvb5a5AlNrddaR_Zp5i-ARiLH5nZjixGBm9jC-AF2e5pMsl50O-VSd09RJyC-5Ad-tq_ewAG-IXEJlxqyQhQM89JQtDNP0jnSUlefRTw9-fZKfAJ-MmG0t6r4HCmhrVi3boWcepJd9xlInrcqr5HD9TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب موشکاز لار ، جنوب شرقی فارس
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/18509" target="_blank">📅 07:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18508">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/766440ca91.mp4?token=J5paqaqoCjHJkGljy6Mh1kJNi8g9C8wGrxHnkMpuRcaxYhqcna_sZll1xfGJNsOw81SIgEkkme5Du9yiolUHRKaj_-MmpKyVP1lx1IG6Y7Slm3xt9EmNSQjKe5f2-IBzU9Z0BipDZl2MKjY6MfhwFlnytfb5RXXD1C_7EavF1g-gHYKevp3ZpKpmM-nEImhpL1iqtgg2fZfxAse-tyjFsCY_h8u-Uq6Ggj7bgNntiJGndLk4Y9HwcaD2Lygh1mx8RNphG9zAHxi_e3rPo6K1Jr8c663mTMMGo1lvIKz-7dW1ZUUsjjCqPxHEon0WY8D_QQMk608pEuH3lxsmeMKycA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/766440ca91.mp4?token=J5paqaqoCjHJkGljy6Mh1kJNi8g9C8wGrxHnkMpuRcaxYhqcna_sZll1xfGJNsOw81SIgEkkme5Du9yiolUHRKaj_-MmpKyVP1lx1IG6Y7Slm3xt9EmNSQjKe5f2-IBzU9Z0BipDZl2MKjY6MfhwFlnytfb5RXXD1C_7EavF1g-gHYKevp3ZpKpmM-nEImhpL1iqtgg2fZfxAse-tyjFsCY_h8u-Uq6Ggj7bgNntiJGndLk4Y9HwcaD2Lygh1mx8RNphG9zAHxi_e3rPo6K1Jr8c663mTMMGo1lvIKz-7dW1ZUUsjjCqPxHEon0WY8D_QQMk608pEuH3lxsmeMKycA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما در ایران پیروزی بزرگی به دست می‌آوریم و شما خیلی زود ثمره این تلاش را خواهید دید.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18508" target="_blank">📅 07:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18507">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">وزارت کشور قطر اعلام کرد که در پی حمله ایران به این کشور در بامداد جمعه، کودکی بر اثر اصابت ترکش‌های سقوط‌ کرده مجروح شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/18507" target="_blank">📅 07:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18506">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/881e02f1c1.mp4?token=Hhh9bTNdW8d8eq6xT7yFsqClB9LGl_ARgqJyXhnJzfKGhDSK5qV73dep30LUkGDTuE-uOH0Kfr1su_EIylpGCzQ2LoK-z9oU_f-Z-ZN_vRaDwMqbYFUxFsmpKxkWdx27U2mIe7u9ySZNxNsaLgydrJ6_K5ufG0YIbugcHs7HsihHCpx8wKFN8OPjei_cjcySQVXHtrrmR4lVk5ZEbShWOnMDBaKMXoJPP66dlm_WuNLpKllz2dnp5AF-_TtCNiHvyEtyzm6ip0g8Qz4eNEnOAeb06r3iA41VBzgL_PdfBlaxlqPqvFY-o-aOfBk5kmKaiVvockeIaRGQqzhN2WpLSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/881e02f1c1.mp4?token=Hhh9bTNdW8d8eq6xT7yFsqClB9LGl_ARgqJyXhnJzfKGhDSK5qV73dep30LUkGDTuE-uOH0Kfr1su_EIylpGCzQ2LoK-z9oU_f-Z-ZN_vRaDwMqbYFUxFsmpKxkWdx27U2mIe7u9ySZNxNsaLgydrJ6_K5ufG0YIbugcHs7HsihHCpx8wKFN8OPjei_cjcySQVXHtrrmR4lVk5ZEbShWOnMDBaKMXoJPP66dlm_WuNLpKllz2dnp5AF-_TtCNiHvyEtyzm6ip0g8Qz4eNEnOAeb06r3iA41VBzgL_PdfBlaxlqPqvFY-o-aOfBk5kmKaiVvockeIaRGQqzhN2WpLSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون موج جدید حملات خصمانه سپاه پرتاب موشک از پاوه کرمانشاه
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18506" target="_blank">📅 07:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18505">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ma30O2KQBThPbjsjnbwkSnDJ43BjYAr3TFOE3bA5HEAx_lwguGxiPq0-fha_TnoWVAjKq6--_DDMXiYH0Bin84xg_5m5SVFvrIKcXjvGP3sVRHyLsQKv4r1798BDmBGJfzvtBBKNJtcG6p5OFpdxP2wsXNcOwMok795Z9iryu7dc8FaMX99oiNt9tA2R3hymIweAsjjBIUvwWUnj-8yOb0D-djpiymuVxVhWo3FVDPhxKBGTKH45t8UDiB2xt1kuUy5VyV5TwqjXLqhPitlB2-Chtoy-d7Z9ioel1OC6lgo2pNofgEWdgvYTA5SjVTAFwv_5QQXdiJxqof0OdFlWlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان چیزی از برج چابهار باقی نمونده
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18505" target="_blank">📅 07:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18504">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pR_CEL5cgfkhzxR1pMb9VSaSjidE6Uat2s6e4nxwkTlqM_2lIjOg86FpxBwY9Ko5oilzWH3sTXLy3eZ-PQocKf_RKSukfkLDQri4qqShNF4sUvMAorwuEFBPmUwnu2xfHskdLgM8CN-KuDrz5Lz6GTZ9xqwvF0wa0OGpjcWsShOMU4t8CMEA2i1yOql3i1uasAzTgrX0LIEg0VoHL0Vln2Y-NIz51sv1FZVPUDQU3uLzADRYWztAde72V-6Yr8FoT4sEbF4WBADmZJe3jnbxz4koM6DPbzjPhGXbN15yJ3A_t-5w9C-g5lahjbgvXkXg5mxJYw8H741lD8lhyd3wdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵ صبح کل چابهار برج ریخت
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18504" target="_blank">📅 07:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18503">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2QqgH2aheRypn9RXqMPMZDwGSkRYX1LVUw90OQuXoJEwIATU16gnkcdP0zH0EWSixfePhkpPEVx8kabvHxAauHTRrjmQ6ziArKJknDb5kO42G5jMr7Mx0L-2UJ_3WQPRgClZ8SonJB_KDRJCHkvHZgmNE_5d5utE-CEWXbGOl5LC9fgv-tUet7GrphspFW1KI2cTtgDzYvNjsRxTkXkueIPEgH7dQDMzMfrnmYpTESawG25dTMwwouJmiEq2IxmEegTbDcqil2AFxBeNWk80f7Oog5V-KiM6gRNvklzujka4L4AuZWsHAUoKj69mFmVOst8yQ-zXwSJYQPxypuMrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتاب موشک از استان هرمزگان شهرستان بستک شهر کوهیج همین الان
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18503" target="_blank">📅 06:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18502">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe0dc5a19f.mp4?token=Pmrgh0jSbJa_nsNPM12cPGBHg5iXLxKA_rjMffFdZDksljlmnnD81yzYjowQOI1pdPhYPm1H4WnEU5AdRIvQSycopsQzmBqgT0Iv-07wkGI06cLCHHbLQrs6hcct0gJq2H18ghrtIT5q3E32OLVTY3uabg6aI7O6gIuAJeb7VwMSTy9EjCd76P0at6_wosFYjEQy50SFSeBAXME5YsDr0LEQqjiKQQXTEGW-NgrBVhLmn7GeQCilfMP4oaKhN9_Ego2WzwK1lxnM8vMDn8xWKPafWMzINh43VdIqAhI4lE_9MYEsG3PNigy9wNLW2t4psVQfRSSZHgWdNPOOfH6k7A7xbdXvbnXxBLIG7CpcrBqa9aytaOXfbE41EM87urnV-qXPoLHU8sY_-PfHHwqBo72nGNa5uTAVn5xZJ2RU7PrKJwfBhVDrtuWeSyBpNxV4GbZPXYgGJt9XGL-h05tgO5-9c1bGydVEv0b9ldSLTJHr8C5e9ESsEnvFhi2-gFQD9BJVyhjYujicZMhm6GwAxdKWpaBoevKmx_Pul1hrsyEOM_Ted5AndnjsUGxvMZK6oduhdjkn2qqsnz4ekblnPEIgNPYBnT8BwDtjBZuknh0etiXa20ssrB7Tuyy5sxVYllSnkNuM7EpRf_s76OvvXZA9M8J40LmdbLKihpeRJEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe0dc5a19f.mp4?token=Pmrgh0jSbJa_nsNPM12cPGBHg5iXLxKA_rjMffFdZDksljlmnnD81yzYjowQOI1pdPhYPm1H4WnEU5AdRIvQSycopsQzmBqgT0Iv-07wkGI06cLCHHbLQrs6hcct0gJq2H18ghrtIT5q3E32OLVTY3uabg6aI7O6gIuAJeb7VwMSTy9EjCd76P0at6_wosFYjEQy50SFSeBAXME5YsDr0LEQqjiKQQXTEGW-NgrBVhLmn7GeQCilfMP4oaKhN9_Ego2WzwK1lxnM8vMDn8xWKPafWMzINh43VdIqAhI4lE_9MYEsG3PNigy9wNLW2t4psVQfRSSZHgWdNPOOfH6k7A7xbdXvbnXxBLIG7CpcrBqa9aytaOXfbE41EM87urnV-qXPoLHU8sY_-PfHHwqBo72nGNa5uTAVn5xZJ2RU7PrKJwfBhVDrtuWeSyBpNxV4GbZPXYgGJt9XGL-h05tgO5-9c1bGydVEv0b9ldSLTJHr8C5e9ESsEnvFhi2-gFQD9BJVyhjYujicZMhm6GwAxdKWpaBoevKmx_Pul1hrsyEOM_Ted5AndnjsUGxvMZK6oduhdjkn2qqsnz4ekblnPEIgNPYBnT8BwDtjBZuknh0etiXa20ssrB7Tuyy5sxVYllSnkNuM7EpRf_s76OvvXZA9M8J40LmdbLKihpeRJEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: ششمین شب متوالی حملات گسترده آمریکا علیه ایران به پایان رسید
سنتکام اعلام کرد
امروز ساعت ۹:۴۰ شب به وقت شرق آمریکا (ET) (۰۵:۱۰ بامداد روز بعد به وقت تهران)
، تازه‌ترین موج گسترده حملات آمریکا علیه ایران به پایان رسید.
به گفته سنتکام، نیروهای آمریکایی با استفاده از
جنگنده‌ها، پهپادها و ناوهای جنگی
و با به‌کارگیری
مهمات هدایت‌شونده دقیق
، ده‌ها هدف نظامی ایران از جمله
سامانه‌های دیده‌بانی ساحلی و پدافند هوایی، زیرساخت‌های لجستیکی نظامی و توانمندی‌های دریایی
را هدف قرار دادند
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18502" target="_blank">📅 06:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18501">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نیوز CBS : اگر ایران نتونه پاسخ قاطع به پل‌های تخریب شده بده٫ حملات بعدی امریکا به زیرساخت حیاتی‌تر ادامه خواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/18501" target="_blank">📅 06:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18500">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بندر یدونه زد ملت نیم متر پریدن
@WarRoom</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/withyashar/18500" target="_blank">📅 01:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18499">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">از سیریک موشک پرتاب شد
@WarRoom</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/withyashar/18499" target="_blank">📅 01:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18498">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">حملات موشکی/پهپادی سپاه شروع شد و تمام پرواز ها رو هم کنسل کردند
@WarRoom</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/withyashar/18498" target="_blank">📅 01:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18497">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4661b5383.mp4?token=P_PCRam0oKjtBJsRAWX9PaBp-mh49vMLnpYMbfwMkwiIq654uxVJFoKthMyaNvfMVdC6m-qzkiNDgq2cQjfkQH7ui_AJiYTL7lgyY5jQx-AteavNqrNQCQNClPyOnLYPmpqzvYdIEcJvHgGP9Y669kD5h561BKagggFzsYbntjfy_ZSZarwUMVkiQmk-CaeNFjbq7uzBz9NiRy_st2RHmK1-9FVgTNWWwDlNuTKjITf_Blfh0z3K6_JFTZGRJ5fFo0G3TnG6a8fOKWRrYEJWLXxDcGdTaRhqDtJO2fiFxidy-oqjGKlWwnn2ImsqCra3a2VjMuxbLxsqO3LNJijczg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4661b5383.mp4?token=P_PCRam0oKjtBJsRAWX9PaBp-mh49vMLnpYMbfwMkwiIq654uxVJFoKthMyaNvfMVdC6m-qzkiNDgq2cQjfkQH7ui_AJiYTL7lgyY5jQx-AteavNqrNQCQNClPyOnLYPmpqzvYdIEcJvHgGP9Y669kD5h561BKagggFzsYbntjfy_ZSZarwUMVkiQmk-CaeNFjbq7uzBz9NiRy_st2RHmK1-9FVgTNWWwDlNuTKjITf_Blfh0z3K6_JFTZGRJ5fFo0G3TnG6a8fOKWRrYEJWLXxDcGdTaRhqDtJO2fiFxidy-oqjGKlWwnn2ImsqCra3a2VjMuxbLxsqO3LNJijczg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام اعلام کرد تفنگداران دریایی آمریکا از یگان اعزامی یازدهم نیروی دریایی (11th MEU) در
۱۶ ژوئیه
عملیات بازرسی و راستی‌آزمایی (هلی برن)را روی نفتکش
M/T Wen Yao
در دریای عمان انجام دادند. به گفته سنتکام، تاکنون نیروهای آمریکایی در چارچوب اجرای محاصره دریایی علیه ایران،
۳ کشتی تجاری
را که قصد عبور از محاصره را داشتند تغییر مسیر داده‌اند،
۱ کشتی
را به دلیل عدم تبعیت از دستورات از کار انداخته‌اند و
۱ کشتی دیگر
را نیز برای اطمینان از اجرای کامل این محاصره بازرسی کرده‌اند. سنتکام همچنین مدعی شد
تنگه هرمز و آب‌های اطراف آن همچنان برای کشتیرانی آزاد و باز است، به‌جز برای شناورهایی که قصد نقض محاصره دریایی آمریکا علیه ایران را داشته باشند
@WarRoom</div>
<div class="tg-footer">👁️ 180K · <a href="https://t.me/withyashar/18497" target="_blank">📅 01:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18496">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">برق مناطقی از کیش قطع شد @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/withyashar/18496" target="_blank">📅 01:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18495">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">۷-۸ انفجار رگباری بوشهر
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/withyashar/18495" target="_blank">📅 00:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18494">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">شاهزاده رضا پهلوی در مصاحبه تصویری با شبکه آی24 فرانسه گفت، امروز پس از ۴۷ سال تجربه جمهوری اسلامی، بیش از هر زمان دیگر آشگار شده که بدون تغییر این رژیم، دستیابی به ثباتی پایدار در منطقه ممکن نخواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/withyashar/18494" target="_blank">📅 00:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18493">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پدافند تهران درگیر شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/withyashar/18493" target="_blank">📅 00:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18492">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">انفجار قشم
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/withyashar/18492" target="_blank">📅 00:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18491">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سخنگوی سنتکام: ما آماده انجام هر ماموریتی هستیم و در حال حاضر 50 هزار نیرو در خاورمیانه داریم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 172K · <a href="https://t.me/withyashar/18491" target="_blank">📅 00:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18490">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">فارس: حمله به پل خمیر ۶ کشته و زخمی داشته
@WarRoom</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/18490" target="_blank">📅 00:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18489">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ حدود ۳ ساعت دیگه صحبت میکنه
@WarRoom
⚠️
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/withyashar/18489" target="_blank">📅 00:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18488">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W831MBi7xOexlH3x5HmprsC1Ng2K3i-BeW-SxfKWwLHQQO6M5d82jJbbNGnwuLMZcJAvRRqRjL66ps0kGW346gUb0LSrvXN7mxU5BEWeWnD4D_ot6Y3mSB91XeIOULBTiQtYvGeU6dD5ssIZZiAhTgF64JcWEGuFlbxLKa7IkxjRMKiX-QvX7wMAwcAvwA4CJM-BYLgLkYPFdb643z3zCKfXJoUF48EmH1nZeogjlrtkrhfgfMXzg9-2FmaqYGlnPozkOAV6FO6VwJnilM0IxMfCPdMH2atf2UWb3BAYjASBplf8bAI1PRkJLoB22yderhWURQj4xowBNeQPwhH3dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمامی پل هایی که بندر خمیر را به بندرعباس متصل می کرد توسط ارتش آمریکا مورد اصابت قرار گرفت.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/withyashar/18488" target="_blank">📅 00:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18487">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/049770daef.mp4?token=rCfDH3x3FJeu5C6Tw76B1fWpzz-3pX0fZV_EesNTkVuy4Amc_9O6bYa7-IhvjPV2F_vpUAm2HXIHvkLZLS6-KeMiUfY81os92npM7YlY9FRmx4Hut0Ryge9StS2C8Gv-gss4czxzDQHiSInR9zgNx4NiosNXN7F2f3pcqi-GD6Z8azUSyX-E_r0-DkKgloCp3kjGcl50HGMXpHUewZJpZsGkYNue4xiTOKCLUbL1c26fl2Di7QcbloJmlC-iHoazek8gcCjPZs3jupshejlTg0Bp-Tw63Q8MsrZKSXAg2wv0FxXo-ZXGoPww5io5oPjlT0OTtpGEuenyzvlgepwReg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/049770daef.mp4?token=rCfDH3x3FJeu5C6Tw76B1fWpzz-3pX0fZV_EesNTkVuy4Amc_9O6bYa7-IhvjPV2F_vpUAm2HXIHvkLZLS6-KeMiUfY81os92npM7YlY9FRmx4Hut0Ryge9StS2C8Gv-gss4czxzDQHiSInR9zgNx4NiosNXN7F2f3pcqi-GD6Z8azUSyX-E_r0-DkKgloCp3kjGcl50HGMXpHUewZJpZsGkYNue4xiTOKCLUbL1c26fl2Di7QcbloJmlC-iHoazek8gcCjPZs3jupshejlTg0Bp-Tw63Q8MsrZKSXAg2wv0FxXo-ZXGoPww5io5oPjlT0OTtpGEuenyzvlgepwReg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حجم زیاد از پهباد شناسایی در اندیمشک نزدیک پایگاه چهارم شکاری
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/18487" target="_blank">📅 00:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18486">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">حمله آمریکا به یک نقطه در اطراف شهر بستان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/18486" target="_blank">📅 00:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18485">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">برق مناطقی از کیش قطع شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/18485" target="_blank">📅 00:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18484">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خبرگزاریCBS به نقل از مقام آمریکایی:
دستورالعمل‌های مربوط به حملات آمریکا به‌روزرسانی شده‌اند تا شامل پل‌ها و اهداف ارتباطی و تدارکاتی شود، با هدف افزایش فشار بر ‌رژیم ایران!
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/18484" target="_blank">📅 00:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18483">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWPz4NDqOZkyyNYzeyHoVxUy5ymLlUbcRs4XEX3gBD9oXEjYxhbILG71oSEBKMDCxqaE8-26uCgRJ_RjHs4QacjbBo3iPf4D4uR4VwhJdbIdoaZrKekxeS1AlVQYKg7oTVzbehzGZ1xMK_rzAro5FFuPK0PZJw7KTD8e939xoXoGQrGuG1FA9IB1bLQHjYaOkcqiwQ-2mCCJkBLkeDG20m-WDxkXz1Vl6Y-TyEP0dWmgmKDA9W_Kmof4PskCwF5tX3lQrBkkOKkMB192t9cx_x81tYO7HO6bB_1gU6FB7GN0rtQROMea_yrgzbOMkrVHK4UWUpHQd76Kv3o2dERjPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه F35 رادارگریز آمریکا داره فرود اضطراری‌ میکنه
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/18483" target="_blank">📅 00:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18482">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">راه آهن بندر عباس رفت رو هوا
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/18482" target="_blank">📅 00:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18481">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">قشم رو زدن ( گویا فرودگاه)
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/18481" target="_blank">📅 00:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18480">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">شکارچی سخنگوی ارشد نیروهای مسلح : مدیریت تنگه هرمز به قبل از ۹ اسفند بازنخواهد گشت
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/18480" target="_blank">📅 00:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18479">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">صداوسیما:تاکنون دو پل استراتژیک مواصلاتی بندر عباس، شیراز، لار و بندر خمیر بمباران شدند و تخریب شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/18479" target="_blank">📅 00:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18478">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">انفجار سیریک
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/18478" target="_blank">📅 00:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18477">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یاشار همین الان صدای انفجار بندرعباس کنار پارک جنگلی
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/18477" target="_blank">📅 00:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18476">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d02804dc2d.mp4?token=fY309ajTybgjpg0N-Zm-zRjldb08n00wxpxClx2JfWHUbfQcnUjP3DVdLyuS9nguD9uV0sHJn4kHZZXReqX9eGtmHg69hku5eA6VrLcSFsWQNeik9o7Dw8TvIcSclTI1XOqKeC8Mnn7fvIS8uB28tckXj-JmMveniD7k0aApuJ1RLTYavhHdmTQTZ3t1L02hWnUIz4UOdNmumLfl6PUzfX18esKGIulrcyd4wgJkyta9X7n7beAISQkuhaoQcqdXufQnxBuqCfBfPCtIftx0KPE8gnRKGkdx31VPgNxXqDHZPhXQGr2my5DXDqzc8iqH7h6nkpiLLthPED6w48C03YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d02804dc2d.mp4?token=fY309ajTybgjpg0N-Zm-zRjldb08n00wxpxClx2JfWHUbfQcnUjP3DVdLyuS9nguD9uV0sHJn4kHZZXReqX9eGtmHg69hku5eA6VrLcSFsWQNeik9o7Dw8TvIcSclTI1XOqKeC8Mnn7fvIS8uB28tckXj-JmMveniD7k0aApuJ1RLTYavhHdmTQTZ3t1L02hWnUIz4UOdNmumLfl6PUzfX18esKGIulrcyd4wgJkyta9X7n7beAISQkuhaoQcqdXufQnxBuqCfBfPCtIftx0KPE8gnRKGkdx31VPgNxXqDHZPhXQGr2my5DXDqzc8iqH7h6nkpiLLthPED6w48C03YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کهورستان بندرعباس
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/18476" target="_blank">📅 00:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18475">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/18475" target="_blank">📅 23:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18474">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer"><a href="https://t.me/withyashar/18474" target="_blank">📅 23:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18473">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1b7bcf1e5.mp4?token=BxhRS2dPeyeixzaJtFTvMlcqBpOvzc5mKUYVcUQm-J4kaYnrptId7cGpvVcowpt-z1CWKSQ08xlEpwPi5S0nTBtfE7ye4Ulpmol_5Y6QXpqXV8kwrOMo8o54YtC64GGYUpn3i4Rgu0N0tlSWFGREcrYyPEke25tQ3iWl7dM9OWjuE_ISNOSzoRz2NjHgGJWNPdIr3fijWlhkUSo1_2ylxktrk29Lxqj-5Vyycm5z0TTfEq28aUpBAoDQv3Yalx1dX4X74Yzg-BU5c7kOY3iL64t_cVMZWuRKXL2UPPsbIXx_i85MYaFsBkqRXj0rRLdIIajdzuSh0qCArYTOBXvxzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1b7bcf1e5.mp4?token=BxhRS2dPeyeixzaJtFTvMlcqBpOvzc5mKUYVcUQm-J4kaYnrptId7cGpvVcowpt-z1CWKSQ08xlEpwPi5S0nTBtfE7ye4Ulpmol_5Y6QXpqXV8kwrOMo8o54YtC64GGYUpn3i4Rgu0N0tlSWFGREcrYyPEke25tQ3iWl7dM9OWjuE_ISNOSzoRz2NjHgGJWNPdIr3fijWlhkUSo1_2ylxktrk29Lxqj-5Vyycm5z0TTfEq28aUpBAoDQv3Yalx1dX4X74Yzg-BU5c7kOY3iL64t_cVMZWuRKXL2UPPsbIXx_i85MYaFsBkqRXj0rRLdIIajdzuSh0qCArYTOBXvxzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کهورستان بندرعباس ۳ تا پل رو زدن
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/18473" target="_blank">📅 23:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18472">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1qr79n24WsRpg5TU9cloAqRJ_c5dVN6sGEYaIRnMLnH6m3MmblzIHvkC-Uj8t3fHIPU3duJY6G8iaUoZYVmi7EL9u3glxC41RNjv8I-5aBKTblaMotjWyObuFNslTpuZ1v0q6hDELacGUtAzkdAr0TM5mlYuJa02BH1FzLgktSLi7ErjMoBx925VLVxk35n90TJOKd_2m8yp8GAPthS9B3d5a3Vp4o0HOUnbtED5BTqWzr_DNI6vmLOVrJUdySBWkUwmeQgXTZotcRNC-V0vnwNbE3nHYVndZTW9Q5xhkv8klDlhbRAmvTLYkWzDb8jvo2SXu1ZBhTQeSlY2DiEhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرودگاه ایرانشهر
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/18472" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18471">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مهر: دقایقی پیش، صدای حدود ۶ انفجار پیاپی در حوالی شهرستان حمیدیه شنیده شد
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/18471" target="_blank">📅 23:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18470">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cd2970e89.mp4?token=fQuDIaDjX3kWbQ52wUNjlPTeEVI0rhKDBm0gLz3cHnuK6q5M_ibd_IFH4H8Gn7Kmr8XPeeOL1DTYsTJWyHQGXQK3PFXLh-GqcgcMRtPqxoBSaEzV_3PglFdaVlPv6gPwj2vRTc7W_XlwbLK3czcfG2HcE0cRnwbORa9HMztSg0krkppuRAcqlyuSPMWbIcwnl07WXxxAJjo2m3cxNwaxy6_VSaOSCRZiXUsFTVUXavYE657zDp0t4KE_cFrlLiXwbgsgYCv0zRzF9ONsDP4aJFI-4JOInEGpbTjTLddbRXDUhhE5HKRcoMMS0ud-9tcIywpSZUzUObsgnQ6gbvVuSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cd2970e89.mp4?token=fQuDIaDjX3kWbQ52wUNjlPTeEVI0rhKDBm0gLz3cHnuK6q5M_ibd_IFH4H8Gn7Kmr8XPeeOL1DTYsTJWyHQGXQK3PFXLh-GqcgcMRtPqxoBSaEzV_3PglFdaVlPv6gPwj2vRTc7W_XlwbLK3czcfG2HcE0cRnwbORa9HMztSg0krkppuRAcqlyuSPMWbIcwnl07WXxxAJjo2m3cxNwaxy6_VSaOSCRZiXUsFTVUXavYE657zDp0t4KE_cFrlLiXwbgsgYCv0zRzF9ONsDP4aJFI-4JOInEGpbTjTLddbRXDUhhE5HKRcoMMS0ud-9tcIywpSZUzUObsgnQ6gbvVuSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پل گچین رو زدن
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/18470" target="_blank">📅 23:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18469">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer"><a href="https://t.me/withyashar/18469" target="_blank">📅 23:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18468">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پل گچین رو زدن
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18468" target="_blank">📅 23:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18467">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">انفجار اهوازززز بازم
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18467" target="_blank">📅 23:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18466">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b364528971.mp4?token=op2rkgtdQiKAuGYz9I-lWBSukNxR4G2j0dx20pOqPQ7jfy9YrlsbjiHZZz7RuawD_Dq6lW-852GBemEkrl9pNHDBfZkxNQhXgnyhL5I35kHqN6TtFop8pv7GX0dEbuFHOBc3lIK-PRuHIUtIDbe6Kdv4a1FOx2TnJAF-yk0c0wunEXeEIL_T283CwKeDZ1LgDeS8kWxriuUukFCUdFRrYbVShbD4rLZ9_jZANWDo50ck9s6u1wjrpScMsX4LRdM8dj3q612YFyr_vQDtVu9IYDRxzMgpiLzoixixqe8Obbh9ULWmX_N0yXo7gP3Rj53PpzS9Ydj6x-9JVJobwR6RSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b364528971.mp4?token=op2rkgtdQiKAuGYz9I-lWBSukNxR4G2j0dx20pOqPQ7jfy9YrlsbjiHZZz7RuawD_Dq6lW-852GBemEkrl9pNHDBfZkxNQhXgnyhL5I35kHqN6TtFop8pv7GX0dEbuFHOBc3lIK-PRuHIUtIDbe6Kdv4a1FOx2TnJAF-yk0c0wunEXeEIL_T283CwKeDZ1LgDeS8kWxriuUukFCUdFRrYbVShbD4rLZ9_jZANWDo50ck9s6u1wjrpScMsX4LRdM8dj3q612YFyr_vQDtVu9IYDRxzMgpiLzoixixqe8Obbh9ULWmX_N0yXo7gP3Rj53PpzS9Ydj6x-9JVJobwR6RSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندر عباس جهنم شده
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/18466" target="_blank">📅 23:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18464">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بوشهررررر سنگین
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/18464" target="_blank">📅 23:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18463">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">قشم روستای مسن رو زذن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/18463" target="_blank">📅 23:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18462">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">همدان ، احتمالا نوژه رو زدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/18462" target="_blank">📅 23:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18461">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">فرودگاه ایرانشهر رو زدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18461" target="_blank">📅 23:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18460">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">روابط عمومی دانشگاه علوم پزشکی هرمزگان:
در پی حمله دقایقی پیش به محله تپه الله‌اکبر شهر بندرعباس، تاکنون ۷ نفر از هموطنان مجروح شده‌اند.
بلافاصله پس از وقوع حادثه، تمامی نیروهای امدادی و درمانی دانشگاه علوم پزشکی هرمزگان در حالت آماده‌باش کامل قرار گرفته‌اند و اقدامات درمانی لازم برای رسیدگی به مصدومان در حال انجام است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18460" target="_blank">📅 23:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18459">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سخنگوی سنتکام: ما در پاکسازی مین‌هایی که سپاه پاسداران در هرمز کار گذاشته است، به پیشرفت‌هایی دست یافته‌ایم و ادامه میدهیم
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/18459" target="_blank">📅 23:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18458">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تسنیم: دقایقی پیش تپه الله اکبر بندرعباس مجددا مورد حمله دشمن قرار گرفت.
حجم این اتفاق به حدی بود که برق این منطقه در بندرعباس در حال حاضر قطع شده است، هدف مورد اصابت در این حمله یک دکل مخابراتی بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/18458" target="_blank">📅 23:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18457">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سلام یاشار پایگاه هوایی بندرو رگباری داره میزنه الان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/18457" target="_blank">📅 23:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18456">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">قشممممم بد زددد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/18456" target="_blank">📅 23:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18455">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دارن گرم میکنین ۱ ساعت دیگه میان شهر های عمیقتر
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18455" target="_blank">📅 23:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18454">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">انفجار قشم
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/18454" target="_blank">📅 23:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18453">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بندر عباس میگن عباس هم رفت فقط خود بندر مونده
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/18453" target="_blank">📅 22:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18452">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اهواز باز زد سه باررررررره
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/18452" target="_blank">📅 22:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18451">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18451" target="_blank">📅 22:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18450">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گزارش انفجار در جم
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/18450" target="_blank">📅 22:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18449">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18449" target="_blank">📅 22:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18448">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کبودراهنگ همدانو کوبیدن
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18448" target="_blank">📅 22:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18447">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9358a92cf5.mp4?token=ZFkdk08FT9vL2SPH7Ms8m6roHeKq4VxgRV963B62shZ2XNTLvJlANqK94WsTmAEQ9vjcLC65p48cK5AiRlfF1ffSNYNIhNo7T9tJovpAgs3c3_DA5cGgPxhu0DqcQaGb0NttTGVOlMlukpl2ExivlFEyPBUYw6Y4DXB3twyNnu1moEB8ye_fAwti7wLa-9k5PjU1nARAXR0GrHMp5JkRJwzuobR3qxHoUN6Z2irb391j74m2F14TF7z9ayNbb3LDmITFusqvdWkrpRZfDp5gOR6Wa3RRLWaItOaYYj0x1kfN1axn4zQiKsBHe9Rcul70MC-S-4d975H6pawW3ludww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9358a92cf5.mp4?token=ZFkdk08FT9vL2SPH7Ms8m6roHeKq4VxgRV963B62shZ2XNTLvJlANqK94WsTmAEQ9vjcLC65p48cK5AiRlfF1ffSNYNIhNo7T9tJovpAgs3c3_DA5cGgPxhu0DqcQaGb0NttTGVOlMlukpl2ExivlFEyPBUYw6Y4DXB3twyNnu1moEB8ye_fAwti7wLa-9k5PjU1nARAXR0GrHMp5JkRJwzuobR3qxHoUN6Z2irb391j74m2F14TF7z9ayNbb3LDmITFusqvdWkrpRZfDp5gOR6Wa3RRLWaItOaYYj0x1kfN1axn4zQiKsBHe9Rcul70MC-S-4d975H6pawW3ludww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله موشکی آمریکا از کویت
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/18447" target="_blank">📅 22:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18446">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">انفجار در قشم
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18446" target="_blank">📅 22:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18445">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">انفجار دوباره بندر عباس
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18445" target="_blank">📅 22:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18444">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">انفجار جزیره لارک
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18444" target="_blank">📅 22:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18443">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اهواز ۷-۸ انفجار در مجموع
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18443" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

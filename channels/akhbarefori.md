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
<img src="https://cdn4.telesco.pe/file/R0QujRp0kFMGFtf6GFXynj4rVje2RDKrKsBeb3RNzUpdc3X2eJ98d2R991Ej8CwSnFNxcTHIkRoao110YM8KpDwMsdSbQ50buVGrNVxD5-hn44FWYbOrcA0yKc2Ggo_YU1RYjzJo8TG3j1C9FbnXG_2nKZFR-kJm6gk-JxQO0HuhCTR29-3V7RDsfdRqnZZ3xdIxL5T2ziIcQRcRjd9N6LhBknGb1B0Ux-BJ-93N28C-HpF6jN-a259ATY9yZhzh1IlF_Gg70nMRru1zCHv_C9SvwahXvUM3IFeFHS4V9nx7q3vCVsOw7Uo384ZLFktqSslbpccLKgixcSS7IrUsvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.41M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 16:31:23</div>
<hr>

<div class="tg-post" id="msg-661819">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/381a23e1f4.mp4?token=DtkL_n4lBf5sS07vZ8A0lBxpJpNQPIgI6_SAL2uIy5j0Nkje--cDysw3LX2aJIiXEsE1qvv0vGr2-V7aLK_uD9veGSb_gq0YcYDrJRdLhlVvLb3ifAFzCt60N9HP_FUW2lN4SAz3lEsmNtkDF5Xn_bctulusIYFsIqwS7Lkf28SthDW8m1jtKFv08FSqp77XNgYk_-D_HE6jVqHOEkbILTYI-46h76fVpF9zpYQ6U3x77BCIzACieNWSQPOUADrDW6lJudNf-rbQfRQoOETNQhVVjiAGNEnyy100A6kUNjrANlQDbu5JqeKEcXgHLm4BvPHzpDfncLbCCRrck2xUJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/381a23e1f4.mp4?token=DtkL_n4lBf5sS07vZ8A0lBxpJpNQPIgI6_SAL2uIy5j0Nkje--cDysw3LX2aJIiXEsE1qvv0vGr2-V7aLK_uD9veGSb_gq0YcYDrJRdLhlVvLb3ifAFzCt60N9HP_FUW2lN4SAz3lEsmNtkDF5Xn_bctulusIYFsIqwS7Lkf28SthDW8m1jtKFv08FSqp77XNgYk_-D_HE6jVqHOEkbILTYI-46h76fVpF9zpYQ6U3x77BCIzACieNWSQPOUADrDW6lJudNf-rbQfRQoOETNQhVVjiAGNEnyy100A6kUNjrANlQDbu5JqeKEcXgHLm4BvPHzpDfncLbCCRrck2xUJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ونس: تنگه هرمز باز است؛ باید نظم جدیدی در خاورمیانه ایجاد کنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/akhbarefori/661819" target="_blank">📅 16:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661818">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
جی‌دی ونس: تنگه هرمز بازگشایی شد/ به دنبال خاورمیانه‌ای متفاوت هستیم  معاون رئیس‌ دولت تروریستی آمریکا:
🔹
دولت ترامپ مأموریت دارد تا با دیپلماسی فعال، مسائل پیچیده خاورمیانه را حل‌وفصل کند.
🔹
ترامپ به دنبال ترسیم آینده‌ای متفاوت و باثبات برای خاورمیانه است.…</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/akhbarefori/661818" target="_blank">📅 16:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661817">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
نخست وزیر قطر: آنچه امروز در این نشست اتفاق می‌افتد برای امنیت منطقه و جهان مهم است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/akhbarefori/661817" target="_blank">📅 16:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661816">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
جی‌دی ونس: تنگه هرمز بازگشایی شد/ به دنبال خاورمیانه‌ای متفاوت هستیم
معاون رئیس‌ دولت تروریستی آمریکا:
🔹
دولت ترامپ مأموریت دارد تا با دیپلماسی فعال، مسائل پیچیده خاورمیانه را حل‌وفصل کند.
🔹
ترامپ به دنبال ترسیم آینده‌ای متفاوت و باثبات برای خاورمیانه است.
🔹
نقش نخست‌وزیر قطر در رسیدن به نقطه فعلی مذاکرات، بسیار حیاتی و تعیین‌کننده بوده است.
🔹
معاون ترامپ مدعی بازگشایی تنگه هرمز شد و هدف اصلی واشنگتن را تضمین جریان آزاد انرژی در منطقه عنوان کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/akhbarefori/661816" target="_blank">📅 16:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661815">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940e599964.mp4?token=lYvgCq687v4jT0JBi6UW01eOnfi2DJCI4LgtoyhfB9ZR7oO1FwbtRPLDzm5nWK6sCh6ZfTufeFRsaPkMGKA1V4dJjiZg50Agh_kVgZvwy-v64RQojtv9tQy01S2PdZYe8Q0owGcEUHlsYXI8AvQS2rL-Vnf8amCYWTGXxb2hm7qHdV3XuceMG5K-QRoifZnLuWtmyLCuqAfZOLEN_US6XtgLuUi10OvVXbV3r6Or2CziYxl-yTXEMGi4bIR8BOGSmV0wuH7KWlxBlc_ou2GQi2PH9EvCqniDLSNGPFtK9UPxY8YliU0OebW1NUovB33c71NH1zNIH__1WgyDd-tg3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940e599964.mp4?token=lYvgCq687v4jT0JBi6UW01eOnfi2DJCI4LgtoyhfB9ZR7oO1FwbtRPLDzm5nWK6sCh6ZfTufeFRsaPkMGKA1V4dJjiZg50Agh_kVgZvwy-v64RQojtv9tQy01S2PdZYe8Q0owGcEUHlsYXI8AvQS2rL-Vnf8amCYWTGXxb2hm7qHdV3XuceMG5K-QRoifZnLuWtmyLCuqAfZOLEN_US6XtgLuUi10OvVXbV3r6Or2CziYxl-yTXEMGi4bIR8BOGSmV0wuH7KWlxBlc_ou2GQi2PH9EvCqniDLSNGPFtK9UPxY8YliU0OebW1NUovB33c71NH1zNIH__1WgyDd-tg3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قانون پول برای مدیریت درست نیازها #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/akhbarefori/661815" target="_blank">📅 16:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661814">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
حضور هیئت ایران به محل برگزاری مذاکرات چهارجانبه در سوئیس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/akhbarefori/661814" target="_blank">📅 16:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661813">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8ee2d1f5e.mp4?token=SOzBwc961fOcobWBXMcEiwYVoANEJJr-m4puYeDraVqbvah72VCPCjfhtxYEK22qwOc1MeHiChv1t_8FP0yY8z9_yMgKv1Yog7wrKE6uHn0caeNMFKhRbtLI3Us2B0UkqiJBs4t-gTNjBa3Yl9DO2hvrHRrdyP7vUGrcNDm0xHqaQnFokZ75U2NU1FBzASLbQsXacq786y0KIt_cDBnWXkkpZOpYRgT9VW8OWbMcnh_EqG9EzWUHLxa36RXL_N-jTpBnYFCDvIGtJI0UYvqhLk_SX2FfNbwPwufwzzLg9QY8lb5PYQk5DG0BsjLq_LscW3P1xr3zNQIAMchMG8Z-aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8ee2d1f5e.mp4?token=SOzBwc961fOcobWBXMcEiwYVoANEJJr-m4puYeDraVqbvah72VCPCjfhtxYEK22qwOc1MeHiChv1t_8FP0yY8z9_yMgKv1Yog7wrKE6uHn0caeNMFKhRbtLI3Us2B0UkqiJBs4t-gTNjBa3Yl9DO2hvrHRrdyP7vUGrcNDm0xHqaQnFokZ75U2NU1FBzASLbQsXacq786y0KIt_cDBnWXkkpZOpYRgT9VW8OWbMcnh_EqG9EzWUHLxa36RXL_N-jTpBnYFCDvIGtJI0UYvqhLk_SX2FfNbwPwufwzzLg9QY8lb5PYQk5DG0BsjLq_LscW3P1xr3zNQIAMchMG8Z-aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتظار هیات آمریکایی برای ورود تیم مذاکره کنندگان جمهوری اسلامی ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/akhbarefori/661813" target="_blank">📅 16:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661812">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
هیات پاکستانی وارد اتاق گفتگوهای چهارجانبه شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/akhbarefori/661812" target="_blank">📅 16:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661811">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cab144afd0.mov?token=fhez8sW8_aV7YkE6JXDTuTDgPvUrc1__sdJDtfDbemrwWOGfkGymo0kFVUVrS20Y8Vms1uGZCvWs55sOTNdKis-TYiG4eXMU1IaFfQZucRaVdUlXurkwk78YxZUntZzYR4f6DE8ujmJvdQSFycIb0rOKdC-hjdAXujOpixW2J-ig-OrJlvDClq5LB2QU-V4XftUa4wWKnl73BJxFz37t-1_pSXIpf8ojviSXUftspMt8dbPvXzoTRk3ThaRnq2LINHhN8gaFBVhn8eVZ6d7wgMrrPeuFzF0oszTMO8d5urrlr_0MjKsCeq3bm7aPJmtvAY_ZNllNjbCyJBM3EkObuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cab144afd0.mov?token=fhez8sW8_aV7YkE6JXDTuTDgPvUrc1__sdJDtfDbemrwWOGfkGymo0kFVUVrS20Y8Vms1uGZCvWs55sOTNdKis-TYiG4eXMU1IaFfQZucRaVdUlXurkwk78YxZUntZzYR4f6DE8ujmJvdQSFycIb0rOKdC-hjdAXujOpixW2J-ig-OrJlvDClq5LB2QU-V4XftUa4wWKnl73BJxFz37t-1_pSXIpf8ojviSXUftspMt8dbPvXzoTRk3ThaRnq2LINHhN8gaFBVhn8eVZ6d7wgMrrPeuFzF0oszTMO8d5urrlr_0MjKsCeq3bm7aPJmtvAY_ZNllNjbCyJBM3EkObuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هیات پاکستانی وارد اتاق گفتگوهای چهارجانبه شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/akhbarefori/661811" target="_blank">📅 16:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661810">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pH4MOP7xKnXcCPuqq-xDBDfX4MVFeMAds3Tw7x2Vth4iELBYsAhxZP7DVhXkmBQp6lWlzylBTVaaPB8Zudez2XB_6kFA2O_USn0xJVAH8WZomvQOTuAb0_Q0s6JhwKYDofFdnhq51w7moGNMo5RuRBZ_jNZK8hdUZxHdum_4xd8DlvfEjpp7lwy5Q4c1UPBzqWL00TLnH7Bio3ITKQt3wQVH5w4UnrIYBkShJ2MRiJkyOTep-aXM0XbU9XMqnkRu_pZz9QiXwgnY97PvTHecmYbQnAlbcbvFL78gX9-SQiWc5emriiWojho0BylaKELD2wbRiCwbL9BQSFYotqou0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آینده ونس به صلح با ایران گره خورد!
نشریه اسپکتاتور:
🔹
ونس به چهره اصلی روند صلح با ایران تبدیل شده و آینده سیاسی او به سرنوشت این توافق گره خورده است.
🔹
اگر توافق شکست بخورد یا در افکار عمومی، عقب‌نشینی و تضعیف جایگاه آمریکا تلقی شود، ممکن است اعتبار سیاسی او آسیب ببیند.
🔹
او اکنون در حال بررسی این موضوع است که آیا اصلاً در سال ۲۰۲۸ نامزد شود یا نه./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/akhbarefori/661810" target="_blank">📅 16:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661809">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWt-B1QQOF626xgvIHSpIH1MZV-C7hnock3_9PxPQS87fMvEjrPRAxp4MsL0b57oA_fcZzRwuPKgEd0g0KWPM8lieZtscCYGaCSL50qEYnF1oxfX46Yn7QGx0qz0f8Na22ojI3kIYD4dysuzQmwem44zVjTS1JClHT3oR6E3JCpIcMSaIGSJkCh5IhwRnykIl60dk5V3eUiona_Auu41MkR8TIgJ2igFuPbeHmP_dysPlZLyOjL7DTY_wkEWMUQt-OyVa9pi6ZqmLTlXQPpP34BJ4sckI9fjxUpS3pw-IMVdeaRtL0J-RX1fiWNwZpwm-SsIDQKlKJsRmm2fyDzb0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محل نشست چهارجانبه ایران، پاکستان، قطر و امریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/akhbarefori/661809" target="_blank">📅 16:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661808">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
عضو کمیسیون کشاورزی: قیمت آب افزایش می‌یابد
محمد جلالی، نماینده مجلس:
🔹
امسال به دلیل بارندگی بهتر وضعیت کلی سدهای کشور بهتر است. وزارت نیرو هر ساله این اختیار را دارد تعرفه‌ها را نسبت به سال قبل افزایش دهد اما این تغییر نرخ برای آب شرب، پلکانی اعمال می‌شود.
🔹
دشمن در جنگ اخیر با حمله به آب شیرین کن‌ها، خطوط انتقال و مخازن، تاثیر مستقیمی بر وضعیت آب کشور گذاشت اما این موضوع مشکلی برای سدهای کشور ایجاد نکرد.
🔹
استان‌های قم، تهران و مرکزی از متوسط بارش کشور پایین‌تر هستند و مردم این استان‌ها باید صرفه‌جویی و همکاری بهتری داشته باشند./ همصدا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/akhbarefori/661808" target="_blank">📅 16:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661807">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbXsaoME50OrjmugM5AgFdk4ybAZKQyRjS2w5QC8bCoOjRs950SwTqcmcoywKzT7UveRhDeBCHmTOufeqOG4R7h9oWVilpS-h8c0zvScUxgHYG_QgQSSMhysynu0Hf66d34K-ucbQq4ZLEFHL583Tjy4T45ztuQl8q1M-GC3XN8e1l8Xw7GQGxuzjGDI8cB36-nhPCcma1GraiTgj7pVok-1BwDH32BRv4cQKH6R9jk0zJAR-tFEIbloZCyJzcf2ScezVpN60yKlaKnZIXp9ci3OxhPbOL41I-AWfWbWIEWeyK492IdkwE4sLnLtnYiuRx5Z3ym72aFtjSUCo5abaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پوستر صفحه رسمی جام جهانی برای دیدار امشب تیم‌های ایران و بلژیک
🔹
این بازی ساعت ۲۲:۳۰ به وقت تهران برگزار می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/akhbarefori/661807" target="_blank">📅 16:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661806">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qon6aFNl5dH6sfN6kweh6R3c_pbepR5z9MNu1Nnv3pMInziXwyyVHUfF5Ybfr3a5OSmoUZij3MHRKf3W80u5wLG8cbYzmY6-VqL6-kdZWKk6DnB_DYVNnFvwTM7YsxhQQoB0SfHjB5-_l5WVwVbYht_b8fV1XIEE6x8F3vYxzOoUOn2_QdGsfu0olyFtG28l_wgTErqIkk8cAdR0rBri7z9fRzfVtn5TLSLzJLzNyV-AeKE4oLd2w7BLvGsc5YhUyC9rgUaoYSuOPIEWnPKztEEGUe1z9u56M_lXZrr9EiNx2R83EMGj3p8HqW0qy2ZSUp7aR7hyGG0h4WMgwCSWJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ضربه مرگبار حزب‌الله به گردان ۵۲؛ ارتش اسرائیل از کشته شدن فرمانده و نیروهایش خبر داد
معاون فرمانده گردان ۵۲ ارتش اسرائیل پس از تلفات سنگین در نبرد با حزب‌الله:
🔹
«چند روز گذشته از سخت‌ترین روزهای تاریخ این گردان بود؛ فرمانده گردان و شماری از سربازان‌مان را از دست دادیم و با خلأیی بزرگ و دردی عمیق روبه‌رو هستیم.»/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/akhbarefori/661806" target="_blank">📅 16:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661805">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
حمله هوایی رژیم صهیونیستی به خان‌یونس
🔹
در حمله هوایی رژیم صهیونیستی به غرب خان‌یونس دو نفر به شهادت رسیدند و تعدادی زخمی شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/akhbarefori/661805" target="_blank">📅 16:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661799">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd545f3887.mp4?token=J-OLi_yBupjuDoTjKyylvqVQoy-xOnPIOEOGdbo3XYRFl2o-ibBR878cSJCSFZMpQo2_UkwvRptuixAEgprUPajSsjgB6_z4V-Wd3KOvZEa6iYGiSa2u02cAaFQ4EMnMuYiQFZDix689CESNuU0D1jsJYybUv3k7Di_kk81szAanRL41VMgG1vgXxUPXEB3QD-gx8ru-5RnBKbmCh6CZacL3uDu55kox2GPFweS7UitLdn4EwEGEO4xjN8qpL6sx8otrq6SAmdQYMAfzqTCmfsisib4BqSNC6Fu5-dD26rp5Kvs9xumT34Bh02tsHnu0xyxY-IEDekc9t4uJTCWOKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd545f3887.mp4?token=J-OLi_yBupjuDoTjKyylvqVQoy-xOnPIOEOGdbo3XYRFl2o-ibBR878cSJCSFZMpQo2_UkwvRptuixAEgprUPajSsjgB6_z4V-Wd3KOvZEa6iYGiSa2u02cAaFQ4EMnMuYiQFZDix689CESNuU0D1jsJYybUv3k7Di_kk81szAanRL41VMgG1vgXxUPXEB3QD-gx8ru-5RnBKbmCh6CZacL3uDu55kox2GPFweS7UitLdn4EwEGEO4xjN8qpL6sx8otrq6SAmdQYMAfzqTCmfsisib4BqSNC6Fu5-dD26rp5Kvs9xumT34Bh02tsHnu0xyxY-IEDekc9t4uJTCWOKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نسل حسینی
🔹
مخاطبان خبرفوری در این ایام محرم، ویدئوهایی از عشق و ارادت کودکانشان به امام حسین (ع) را با ما به اشتراک گذاشته‌اند.
🔸
شماهم با ارسال ویدئو مداحی نوجوانان خود به پویش نسل حسینی بپیوندید
👇
#ایران_حسینی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/akhbarefori/661799" target="_blank">📅 16:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661798">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hy7-N7De7rkM-ddDnQyXDMgz-Nlp9RcXXGyJdb13WpFdoRBlItLMudMA-nvFWMBGNQTwXd7WbsW6fy_wgM7pY50MWSzJMAgvuBlTv8qeEXftRc7py3WeR8Esh41QCPf7LbpzEo9WZV4GLRaZ8TR0uN-64PkSD-t22a8i9cAOGLG4UBZzgCfn2YANZTNnV_WRfKzqe_i1u_6XP8_t41Ib_Duj5WDogx9JzHyrnrYtNgRRGzOTsQ-Y8wIGHAJVXcGqTuOTrudkYKpF6D8GJbP5JqHlVYhtrA8RgU35LCPvIaH_aBG7pcGJyleO8sEvGTHdnwu1MDOtIfqQ4UJJTOQucQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رابطه ایران و آمریکا در دو ماه آتی/ همه چیز مجددا «استپ» می شود؟
🔹
بعد از جنگ ۴۰ روزه بسیاری گمان داشتند فضای «تعلیق» بالاخره از بین می رود و ایران و آمریکا «تصمیم» می گیرند که به مشکلاتشان «پایان» دهند اما تفاهم دو ماهه به نحوی منعقد شده که به نظر می رسد این فضا همچنان بر روابط ایران و آمریکا حکمفرما خواهد بود.
گزازش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3224767</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/akhbarefori/661798" target="_blank">📅 16:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661797">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
فایننشال تایمز به نقل از دیپلمات آگاه: مقامات قطری به ایران گفتند که اگر هیئتی اعزام نکند، عملاً به نتانیاهو «حق وتو بر جنگ» را داده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/akhbarefori/661797" target="_blank">📅 16:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661795">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9356253177.mp4?token=hFmqYWhuDmCtgEH8sIe-9NRRWY1vRqx0OovxwkAK0QT8a22oVQjNlDIJa_liMXYzw1vv5qBB6i3h1IupttzlnA7je0E9W6mdwadpvpP_LHoCPSaGOtfUTRgQW2b1RsGw5POz5H2QBc83gKpj-r2LwELn6qQbFQZ0E83YGlSyfg2_sbTttDUyT4C-ftXsSHzJ0GfbZcA6o3xP5qS5vqLgzFmhasOY-TVO_ji4D_TxeFDbfxoUivUH1qunrzVt-NrazpH6ehB3sR2RHgo--eJMNXICuHoYFoGdF7_8OIH0tAH-CXlULgar08PhvluniqUJcI5AJzgSs8T_Wp0BlrxXUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9356253177.mp4?token=hFmqYWhuDmCtgEH8sIe-9NRRWY1vRqx0OovxwkAK0QT8a22oVQjNlDIJa_liMXYzw1vv5qBB6i3h1IupttzlnA7je0E9W6mdwadpvpP_LHoCPSaGOtfUTRgQW2b1RsGw5POz5H2QBc83gKpj-r2LwELn6qQbFQZ0E83YGlSyfg2_sbTttDUyT4C-ftXsSHzJ0GfbZcA6o3xP5qS5vqLgzFmhasOY-TVO_ji4D_TxeFDbfxoUivUH1qunrzVt-NrazpH6ehB3sR2RHgo--eJMNXICuHoYFoGdF7_8OIH0tAH-CXlULgar08PhvluniqUJcI5AJzgSs8T_Wp0BlrxXUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشاور علوم و فناوری ترامپ: «این توافق یک دستاورد بزرگ است؛ جایگزین آن، جنگی فاجعه‌بار و بی‌پایان با ایران خواهد بود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/akhbarefori/661795" target="_blank">📅 15:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661794">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
قطر آغاز نشست سران در سوئیس را اعلام کرد  وزارت امور خارجه قطر:
🔹
نشست سران در سوئیس آغاز شده است. نخستین دیدار میان واشنگتن و تهران با حضور دو کشور میانجی، یعنی قطر و پاکستان، در این نشست برگزار می‌شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/akhbarefori/661794" target="_blank">📅 15:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661792">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
وزیر خارجه پاکستان به الحدث: ما توانستیم آمریکا و ایران را برای نخستین بار پس از ۴۷ سال پای میز مذاکره بنشانیم
🔹
سه تیم فنی در مذاکرات بین آمریکا و ایران مشارکت دارند.
🔹
کمیته‌های فنی در حال بحث دربارهٔ پرونده هسته‌ای، دارایی‌های مسدودشده ایران و موضوع لبنان…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/661792" target="_blank">📅 15:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661791">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کوثری: ۵ بند تفاهم‌نامه باید زودتر از بندهای دیگر عملیاتی شود
اسماعیل کوثری، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
اصل قضیه این است که ۵ بند زودتر از مذاکره باید عملیاتی شود؛ بندها ۱، ۴، ۵، ۱۰ و ۱۱. اگر این بندها عملیاتی نشود، به بندهای دیگر مراجعه نمی‌شود.
🔹
محاصره دریایی به عنوان یکی از بندها از سوی آمریکا برداشته شده است، اما حریف سگ هارشان یعنی اسراییل نشدند. باید آنجا آتش‌بس را رعایت می‌کردند، اما به مراتب بدتر از روزهای گذشته جنایت کردند و تعدادی از مردم و رزمندگان حزب‌الله را به شهادت رساندند.
🔹
طبق همان روال ما هم تنگه را بستیم و اعلام کردیم تا زمانی که آنها رعایت نکنند ما هم تنگه را به هیچ وجه باز نمی‌کنیم. ما باید یا تنگه هرمز را ببندیم یا با موشک اسراییل را مورد هدف قرار دهیم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/akhbarefori/661791" target="_blank">📅 15:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661789">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
عصبانیت ترامپ از نتانیاهو
وب‌سایت «زتیو» به نقل از منابع آگاه:
🔹
ترامپ به شدت از نتانیاهو عصبانی است؛ او گفته که دولت اسرائیل سعی دارد او را فریب دهد تا دوباره جنگی تمام عیار با ایران راه بیندازد
🔹
رئیس‌جمهور آمریکا به شدت در این باره فحش می‌دهد. در حال حاضر، او قطعاً از اسرائیلی‌ها بیشتر از ایرانی‌ها عصبانی است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/661789" target="_blank">📅 15:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661788">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
مدیرعامل سایپا: پرداخت جریمه تاخیر خودروها از سرگرفته شده است و واریزها بصورت هفتگی انجام می‌شود
🔹
برنامه ریزی شده تا تولید روزانه از ۱۳۰۰ به ۱۸۰۰ دستگاه برسد و با افزایش تولید، میزان معوقات را کاهش یابد.
🔹
انحصار برخی تامین کنندگان قطعات را شکستیم و با تامین قطعه از منابع مختلف در تلاشیم مانع از توقف چرخه تولید شویم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/661788" target="_blank">📅 15:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661787">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c5461519b.mp4?token=uaTk3hAjwZoPnZDJtxfguhlzYa_abXzMSE2q1kLi3f0JNnXuWXPr6OJN4-kvUjoQ1kmHgoY8AFZKNvZCavA-rRUgHhXNWxPlOKTNiCW8edVPxY9mORSgiGKj28q73hEukTf3ugXEdTr7sY88ekPgXT-tQ4x66YHzvaSGxWZfasyGxnNXNVlyY3ksyqKO3CJoNEsIxMjfsmp6ZFNAXjJ-VKF0jiJEDI0gn6a9I3YGSqE8oDelCuX6UrOtM1wjK6wCnRjvO5tS3FBpCYtyY5B25UDn5PhlqSJiWAxwsEZaV_dTP-tV_aazHSHbdDGrOr0e_86iGtHtVjqQ9KgbKQoAfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c5461519b.mp4?token=uaTk3hAjwZoPnZDJtxfguhlzYa_abXzMSE2q1kLi3f0JNnXuWXPr6OJN4-kvUjoQ1kmHgoY8AFZKNvZCavA-rRUgHhXNWxPlOKTNiCW8edVPxY9mORSgiGKj28q73hEukTf3ugXEdTr7sY88ekPgXT-tQ4x66YHzvaSGxWZfasyGxnNXNVlyY3ksyqKO3CJoNEsIxMjfsmp6ZFNAXjJ-VKF0jiJEDI0gn6a9I3YGSqE8oDelCuX6UrOtM1wjK6wCnRjvO5tS3FBpCYtyY5B25UDn5PhlqSJiWAxwsEZaV_dTP-tV_aazHSHbdDGrOr0e_86iGtHtVjqQ9KgbKQoAfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چه مبلی بخریم که مد باشه؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/661787" target="_blank">📅 15:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661785">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sI_OBZTmr0lzEO3HmVMNCGc3B64yp62ysV9Yc8o92uQHdPMULD4PRRhHBL-NeGMpS4h3_mbZyq4QiSo5mAwmr1RgY_6aqoZjF0KgFK9rwsU9VNByqKHFdGDGlLyA_vNJlLFLEarDY7qaTz3LqZh-5vDHXCscW3Jfu8ROzSMcgwt2uKq3Z3m6nuiAj_Kk069_GOMttG18Zrm6hFtOTGx0H0nog1Q8I1Cpy_jtfA9n_F0FFMQV2V3vIEr0VWr_dniVG_Lx-KynOZ8ld9pGstMjhchnYSwiYYXzKHpGpdb3glepWWBgP9LDUco7JJCteJmL3sYkYEHEOD7E18boQMjzVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تکنولوژی بومی؛ پلی برای عبور از بحران‌ها
🔹
هدف نهایی هر سیستم مدیریتی، بهبود زندگی مردم و رفع موانع است.
🔹
تصویری که می‌بینید، استفاده از یک ابزار کاملاً ایرانی برای هماهنگی‌های فوری در شرایط حساس است.
🔹
پایداری زیرساخت‌های داخلی این اطمینان را می‌دهد که در سخت‌ترین روزها هم ارتباط مسئولان با نیازهای جامعه قطع نخواهد شد.
🔹
ما در اسکای‌روم، فراهم‌کننده بستری برای این گفتگوهای گره‌گشا هستیم.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/661785" target="_blank">📅 15:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661776">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tSZr3_BI5bO9IHyqpT5M5Qz2G2a6fTKW7L1vB6q-uU7eWulv2t4GFebZ1vcHfIl5OcokhTnFGIwlmhaderEDG3U7bH3x4Nl71x0cyBZ4Ks9jk4W2MwsoHaJ4pGWIwHr_LAYGKuqGiTHFt0-jl93GP7jJS8DgWcpAOhapBLVLUO_Q9E22CtAV_-7bGtf0qNJmkT0zYCpQ_xL0wHXwu3mHbRyTmmpxdr3pkOQHL8bapeuJzJdv14XbxSMfarDNp2qKeLDnSwgLgDLU5tuFYLcsPEBU_2SyXxTrz3SxWJU55n8ETAdSx7EAXYHAgT4nH2vcep3VvjAuFpyMy4aPvLielg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H58ojKJ2IzjPd8zu7ZgPuCTnqSqi257tjjlo2kIpH0whT91oESalTQx-ra2dz2I-C6JbPzhO93BuWGfU0RKY9TeSfxq68oidIqZaCM7SzUlk6aWfMSq0AIPXHlI1jYbLhfo3MNfLqbTOOmRq58g9s6O-W0IT3KoKH3iyfm1gEvPG2FsrprrksHFn3xV7fVgaeamm5LzHSGkGI_wIdvzJkDcb_5Ye5_P3omHwdJNYTVoSsVUo8UdMWWMFEGq95UzJEOLRaFhprcSzPlCRoaxyZ1l2MK6Az76DhJxBZxDsaKaDxTF5LRQCW6ZHAJHQsq1QkP8CAmKf_TtWnlEMbSvJbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g5IMgnICjScjt6eVm5BgaTBW011KUioSprkUcXcPWl9P2NPWLBF3Xlr6YBmNEtc8RKFN9EC086W8OtzJXjLAfzyxrHqr3-sFZPzuCx43Kh7vBTvROPb5vqsm2CZsPTRTr7dMXgsiKCSVJHCqaTRIpC2cegcFl9HqANB8u3noGHV_PPlASfulXBM0x9MuVerJZjvLFyb9XiwSauwSw9ORTBDFk-bXeof7_E9gunNj2EHCiwRfCRKS8WhwHqa2RKYYNOKyOflpssg2RpzcWXoHN9DfGG0OH8KGFdUUzOyNJ_6tbZl2NemNf047zze0gWKOQEXLTGoGzucQp8qS67PRpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ia5KmJ2OXBvUJ-1g6saYnL-LhiCI-WObSXVJrmxiYiHuFu8IzQlWQ3WNrhImysDor-Pyf2dmCy-_GNNqIecrcC9aBImriZkNy6BmbyiVHWJLnZXqc0OyKdh8biMqPm1_1PJvFqstg5rpSkaKSTbv1uynv9hFRST0RKg7R8FHz1HrR2da3nKUnsVBbqlDrRoAzjypbUf9es0fyMYXhhkxGtWnfiTn8plSoxn6j_d2RbcDJzakC20cy5n6f9GEVrxhgITj86UDMWPTx_YYsYlIdEWhOzPCF7P-vKZ9mSQjhC8R-19kAQpMWGw0xb8PplZt_Ep8Bv_gagmJscuQi3HWkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OjhVKYrSxkbZYkl21Tj7Px-QvI-SMBzp5FWka3m_7u1xrlg3u1tsh_zq-SJCP7Vsx-Mw8L6-d3VMJl0ZGMkwfn6wy96afH7qYQ5gzvE9dlo2iJP0hPwZ8_LwHM5_pArYd095bshxgrXRA15KC20TD20rkT7l-wgrVo_3HvggdTyfO_jQv7K3SlycxGN5j8p53OqVOvuS-EJIkOiH5SavbsuXsrMTAESzwfL7x5wEUtcAVKZhhBuThHl58YNspxqNgc3_6VX3Ec5rbv7M7Q_2_7seyx3VugY_jdPZWUl_FatWSaKzHn6b1ac9phxaU00_RM-8rhdpF6q50TePGV-j8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rw7RS-sivZSosD2n00VhdGGMu0Jpx5pRdkdyIcLA8v9CPSKP2Q0N6FHZ9sWBSKBp3fzkOo0pHTV1iaUmoZltMrFJG0Ni0Y8JXc5pLq9hgg0kFBc3cnCDAzKC4ESv4SxASvqWEmbXLooYXwDtNHZRdGu0cX_f3d8goHDzNfm5vE5n57Tj7tguqHyXEKPsT-DleBNC6MwY-Y1uiZu8wbVw790vd1wfGooZYKWkIsGV4SPIw7MxWq89tHv2zNdd7txc3XaFIsT-ibSSx298ICeCaDxNSD_iZx7vwmN7st34IysX4-7ClLHRsqxP4IPZ19ubewtJR0QPtt65WjZjz_cD6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H-IKrrC4G2L0Rpc6rLGTbFGS2uCfo84qxQ3FuA1fUoW_fpbCCAhnSqDL00GKBCEbAbi-VsbXzMCQY1NAtN7ZbIpumTEyueV0lD0Dg0RfYx7ttNTEvwTYKutgY2Rc-lpwKBiPy14vR1N_wiZhXhdStepuzsGTlrWHAudmBCyRyOs60VcbQ5aZ-oY83MURYLoZ2a0hHA_I0ntOd8Ox9AXoY7WJjx61yqmHkD_dinspRRcQCexHbvr0b_LujRA-0mjv2bwuehIVuHaQ6G3B6OfALJJtGa8ysTlLH8fLzwwXFz3fiKX9-stc2XqI4UiM1Zfi5DZ9Nu4Zwv2c3iGitPUpEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C1aXhTSCOfhfV7D5bkkSmHhXIpuRwpPX4TLcJ2a9AZC458RFmnohTNMB46otzG1X-8FgVfgaB99gMdbIwLYv6m2ofUx-MOhT_oHSeh7_fswT252FDrb5weM9zk6uKgzEhcZ8tK6xrAEDJISEJl6EWG5NWxejtxCiSiy3l0rgWOS1Jz_m4FRhQ6Ul9CQGRPb2PTRVwa0lKTZMRXusu63QXfOgxA5eRjhL5J0GpqMmU1BZpD2-WN6u6I_GoFiMvl8xH9GslD2YbMmJoT8hcjNa28knz2trzDCtFYA2dAXTVfWYA4PXuz2vfyPof7jL-avrixlRZHjHWs4-WjuPzmNRVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PVrNuVlNWDZXAW39VIpXosJ6wVJwsVyR5wauTqZEjGo_Kch4MVh6QKPBzjeHcVHw7WnXEqWQ_9LOVmxXnLUKP49NboXwEEyq2-hEPtSwMphmPGw32xkm2ARQvqSUIEXacBOpmSxMzCxE3EJbNDgIyKATxEOMz7vreNSvcdmdO-bLNBlaKHeTYYyS8Io43xsmH6l46pYGpESP-6fZhmLMlnmNcnHVXCGdVL4vU-t9JGaRWRj5hJN3Hs7CSxcMZPE2xfbex7aSFHul3c9LaIV3_GojbYWBfv9mkXpOixRtrhrHX8kcTkBEQuE9BFmO2iIVosO1gKJwanUxq36xAYAlBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
در روزهایی که
#همدلی
معنای تازه‌ای پیدا کرده است، حضور شما عزیزان در کنار
#هیات_قرار
، پشتوانه ادامه این مسیر نورانی است.
💫
آنچه به ثمر می‌رسد، حاصل همراهی دل‌هایی‌ست که با محبت اهل‌بیت علیهم‌السلام، شریک این خیر ماندگار شده‌اند.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/661776" target="_blank">📅 15:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661775">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSeXRnOmHNlskycP_hwuymcJvNzUJ2k0c2SZm9GC56gZ_7DOsDigzBXv5Z0gY7_5OvVQ-0s15DryDpRGiGqUPSyTRODLFmKmpNbb057OveGVjL7rkygg6GTy7DHFO4hGVSJ3CeK-W23fyC-ZEXFOUq7DluqDCo3c7HxlIxI3uvuQR9yh8sFV0S6hOydo04OSSzppCAsIZAnWg8w1Kx3L7_Oii1GT2nVSvOoiIALtruYi_LeXjcne7gau8jX88GfYKQmFPG2vK3pCpCpWb0aRjmA4Pg405yiyXWLq_IRoiHwctGbJ01nBS_ZCVfCVI3Fl_aCsMNmyM3Ao_ldxuBycCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدودف می‌گوید روسیه دیگر به قواعد جنگی پایبند نیست | جنگ هسته‌ای در راه است؟
🔹
گزارش تازه دیلی میل به بررسی احتمال تغییر رویکرد روسیه در جنگ اوکراین و بحث‌های مرتبط با استفاده احتمالی از سلاح‌های هسته‌ای توسط مسکو می‌پردازد.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3224713</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/661775" target="_blank">📅 15:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661774">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a48d6a91cb.mp4?token=VPcU1mOBIbc8dS1GP_r8W8sGoqbJAGF2TyBdldn1Ma9eSDxg0PlZBXUi0xEvEkzxMQ7p3MwA5-4gghpw_ZlWZhk4Ev-5lBNpinQT7uV8vR6ySBEL3cXxnaNUHHZ7iMkSDkNn5FsoXSObPQI4cZahnEua1KYkN75_7NXL7pbTUMv1lSqa9XwMvg8pM3y6E9O2rj7Eaje44z1AuXnwTG3LJ7pamyGSkkdOG9MWjnPhZVaGGcI8cEQjz_U2yQFj7f3wO1ZMlk0ZQ7CdZ2ioPaS1bIvDAxeCQzLG-Hr-FTWMnkNm6iBStlrp5_K8nZCsJ_h37OZ25Xx31zLcsDaN9yRz8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a48d6a91cb.mp4?token=VPcU1mOBIbc8dS1GP_r8W8sGoqbJAGF2TyBdldn1Ma9eSDxg0PlZBXUi0xEvEkzxMQ7p3MwA5-4gghpw_ZlWZhk4Ev-5lBNpinQT7uV8vR6ySBEL3cXxnaNUHHZ7iMkSDkNn5FsoXSObPQI4cZahnEua1KYkN75_7NXL7pbTUMv1lSqa9XwMvg8pM3y6E9O2rj7Eaje44z1AuXnwTG3LJ7pamyGSkkdOG9MWjnPhZVaGGcI8cEQjz_U2yQFj7f3wO1ZMlk0ZQ7CdZ2ioPaS1bIvDAxeCQzLG-Hr-FTWMnkNm6iBStlrp5_K8nZCsJ_h37OZ25Xx31zLcsDaN9yRz8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دانش‌آموزان میناب در کنار تیم ملی‌اند؛ در میدان افتخار
و در هر فریاد «ایران، ایران»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/661774" target="_blank">📅 15:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661773">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12ba50d6cf.mp4?token=Ihs8xBh_eNnEhSM6iUp-IBJ56OODUptUXMc515eV-4xnRnhXDq63usM5LYtnBfvif_PvVqCQmEKVX4aJfBq5Sx_-PPTJgmW8dljJr_Geg5URveHZltk82SZivG8fPEcVQiK_XAfuW8t4RK29g-BB2bpDj3Fb2Iw8cb0JDsGrhTSbxAUwl0Tle4ot8bW2cQPeiimcfLcJXDigg2RVeoxQdpyzxnydyc5Vtf3VIwWUQZkazq2NPhiWNBOB_ZxcnT6BZvls7awOYih3O2z9Sj4_a2K52vMTekJF4V6vH3JNDCz0o9AsD0Batcwp1WosbVEvITEBNLqLdAjLb9HgusSSwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12ba50d6cf.mp4?token=Ihs8xBh_eNnEhSM6iUp-IBJ56OODUptUXMc515eV-4xnRnhXDq63usM5LYtnBfvif_PvVqCQmEKVX4aJfBq5Sx_-PPTJgmW8dljJr_Geg5URveHZltk82SZivG8fPEcVQiK_XAfuW8t4RK29g-BB2bpDj3Fb2Iw8cb0JDsGrhTSbxAUwl0Tle4ot8bW2cQPeiimcfLcJXDigg2RVeoxQdpyzxnydyc5Vtf3VIwWUQZkazq2NPhiWNBOB_ZxcnT6BZvls7awOYih3O2z9Sj4_a2K52vMTekJF4V6vH3JNDCz0o9AsD0Batcwp1WosbVEvITEBNLqLdAjLb9HgusSSwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امیر قلعه نویی در نشست خبری پیش از دیدار با تیم ملی بلژیک: کمتر از ۱۶ ساعت به ما وقت دادند و مجبور شدیم تمرین نصف و نیمه‌ای انجام دهیم و این کار ما را سخت کرد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/661773" target="_blank">📅 15:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661772">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cF2JgIrwJgyldYxmLRcTfXt-t3xJnz9Vlg1jnaFkuQRAP-VrHlNG901h_D9Y8Es1aOtlf03v9IHpkVHcL6b7OYM4L-mQhP5bJBxkQUTCr__mDUIoVkr6JIjky3OrtR9DJAg9Lv3DyrNX074tYwx2mP1ph87-l6jiRIo5o4pV8yj0tHtxf0y2YlxcB8_E_RrcEECSr0tjrZd56MqEiyXpzmWzfkMMPs1hN6gQ0oPgOMKERIn2_93Abk8qYl3L8EAPlHzelWWW3N79jZTRWAh1BJtOvhkeDZ5GT2YbE4ZOkxSBQl0pa7c1kYEtS_AliDIRT3G06sUEMLhaT_amNGl1Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سعید برند، دبیر ستاد رسانه‌ای تشییع رهبر انقلاب در هلدینگ خبرفوری شد
🔹
طی حکمی، سعید برند به عنوان دبیر ستاد رسانه‌ای تشییع رهبر انقلاب در هلدینگ خبرفوری منصوب شد. وی مسئولیت هماهنگی، راهبری و مدیریت فعالیت‌های رسانه‌ای این هلدینگ در پوشش مراسم و برنامه‌های مرتبط را بر عهده خواهد داشت.
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/661772" target="_blank">📅 15:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661771">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/607a870e5c.mp4?token=JyX6uhjKfREdNEgO3HdSHdvo-32dxp-1ucK5mRPF2vn0PBsvAC0K9tIAJl8wN79bn0bNN7YnI-4vVGQCdyIOEus4YZaHHoGTdhWPgltukBo5-nlhc26X0-U-1VR54rB7yh7_mFA0BQOITz8oIurSv7ADsRRdSSd0WqBBgXBG4IYGAs2uAYWzPKBIqKjKGBCM2vpX3RNKu5IR5Z1I0neq7LK0tFzZnQajIsk7mrWMRv8OsE_CwCJfrA7XOkSqfZEvd4A3J5F0GcRLGluzQxPOuH24iGBgkKZtr1EP6NsAoz42l2arCD30tZ7XOIWs4pj__-NSGPxdml4fsQqw7Nyimg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/607a870e5c.mp4?token=JyX6uhjKfREdNEgO3HdSHdvo-32dxp-1ucK5mRPF2vn0PBsvAC0K9tIAJl8wN79bn0bNN7YnI-4vVGQCdyIOEus4YZaHHoGTdhWPgltukBo5-nlhc26X0-U-1VR54rB7yh7_mFA0BQOITz8oIurSv7ADsRRdSSd0WqBBgXBG4IYGAs2uAYWzPKBIqKjKGBCM2vpX3RNKu5IR5Z1I0neq7LK0tFzZnQajIsk7mrWMRv8OsE_CwCJfrA7XOkSqfZEvd4A3J5F0GcRLGluzQxPOuH24iGBgkKZtr1EP6NsAoz42l2arCD30tZ7XOIWs4pj__-NSGPxdml4fsQqw7Nyimg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از شهدای میناب که قالیباف لحظاتی قبل در صفحهٔ خود منتشر کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/661771" target="_blank">📅 15:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661770">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
دیدار شهباز شریف نخست وزیر و عاصم منیر فرمانده ارتش پاکستان با محمدباقر قالیباف رئیس هیئت ایرانی میناب ۱۶۸ - زوریخ سوئیس
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/661770" target="_blank">📅 15:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661769">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81bb35deb.mp4?token=QvSXawXL10actVB4AXbROWO2J0RE4Z7Hqdwz1pIHprTjm31KBxcF9-_P8Emg6sXU48hXz8R-hLgKRxQvN50TXG7XVMdolfDFobpZ-ngShzJewM_1ycEo1YndCU9O6GhPtZ9jMLN-HdNk2tF7bZmjq8FtcDfWcvAIfSjDrH35BJmlq6jdxFjfaQ17i_SWGHTzdNo2XFEoGPOZPl8RJFlcp-FVc_kcJz-WKoeAYQ1xQ6ZjPJZQ6-NtOJe9wqXVDZiTynWlUZ5RZZHvEEYpahhn-0T_vlP7WrBe_-uu_bZa9rTLE8cG5ufhvBtey_gAKmtNJvdnUsubHk702Q1z3-gKdDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81bb35deb.mp4?token=QvSXawXL10actVB4AXbROWO2J0RE4Z7Hqdwz1pIHprTjm31KBxcF9-_P8Emg6sXU48hXz8R-hLgKRxQvN50TXG7XVMdolfDFobpZ-ngShzJewM_1ycEo1YndCU9O6GhPtZ9jMLN-HdNk2tF7bZmjq8FtcDfWcvAIfSjDrH35BJmlq6jdxFjfaQ17i_SWGHTzdNo2XFEoGPOZPl8RJFlcp-FVc_kcJz-WKoeAYQ1xQ6ZjPJZQ6-NtOJe9wqXVDZiTynWlUZ5RZZHvEEYpahhn-0T_vlP7WrBe_-uu_bZa9rTLE8cG5ufhvBtey_gAKmtNJvdnUsubHk702Q1z3-gKdDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کشتی کانتیری با گذشتن از محاصره دریایی حامل کالاهای اساسی در حال تخلیه در بندر شهید رجایی است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/661769" target="_blank">📅 15:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661768">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 شما این روزها بیشتر از کدام ابزار هوش مصنوعی استفاده می‌کنید؟</h4>
<ul>
<li>✓ چت‌جی‌پی‌تی (ChatGPT)</li>
<li>✓ کلاد (Claude)</li>
<li>✓ جمینای (Gemini)</li>
<li>✓ دیپ‌سیک (DeepSeek)</li>
<li>✓ گراک (Grok)</li>
<li>✓ میدجرنی (Midjourney)</li>
<li>✓ سایر ابزارها</li>
<li>✓ استفاده خاصی ندارم</li>
</ul>
</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/661768" target="_blank">📅 15:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661767">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
علت عدم واریز حقوق برخی از بازنشستگان کشوری در خرداد ۱۴۰۵ اعلام شد
🔹
به دلیل بروز اختلال در سامانه پیامکی بانک عامل، ممکن است پیامک واریز حقوق برای بخشی از بازنشستگان و وظیفه‌بگیران ارسال نشده باشد؛ بنابراین عدم دریافت پیامک لزوماً به معنای عدم واریز حقوق نیست و مشمولان می‌توانند از طریق درگاه‌های بانکی نسبت به بررسی موجودی حساب خود اقدام کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/661767" target="_blank">📅 14:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661766">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
انهدام مهمات عمل نکرده دشمن در بندرعباس
روابط عمومی سپاه امام سجاد (ع) :
🔹
دوشنبه اول تیر ماه از ساعت ۸ صبح تا ۱۱ ظهر در برخی مناطق حومه بندرعباس (سرخون وایسین) عملیات انهدام مهمات جنگ رمضان با حضور تیم تخصصی چک وخنثی اجرا می‌شود.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/661766" target="_blank">📅 14:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661765">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPkMPiib8MO9HuclYiuS1oe1XpmQMz8wNLb8nfue9ah068Rh9PgjXftTiHx9AkSg7UBrHEgs8t2oScB8BaVjJWOFDJBjPA4wlTlbe-pajLnCF5iMbXSozi2cj7sY968SusQEV1ms1L8GRIhcfYlbYz4mIP_0SGu2QR61S6iDTqKDu9nxn8p8AEUHyWh2ebOlyW5ZHS_T1LQIQBRqXcK0XMKCg_NEDOdt8FGNX6B56wZkkhmSBBuTVZRFK7TShky68kFuxholR57GUr08WeNw_PfgOomckLd7rvTfdWr6AD6j_HQzNUaIiWf9Pa8wVxT4pUCcypu5YE3Mu8mdEZgi2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیدار شهباز شریف نخست وزیر و عاصم منیر فرمانده ارتش پاکستان با محمدباقر قالیباف رئیس هیئت ایرانی میناب ۱۶۸ - زوریخ سوئیس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/661765" target="_blank">📅 14:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661763">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
قطر آغاز نشست سران در سوئیس را اعلام کرد
وزارت امور خارجه قطر:
🔹
نشست سران در سوئیس آغاز شده است. نخستین دیدار میان واشنگتن و تهران با حضور دو کشور میانجی، یعنی قطر و پاکستان، در این نشست برگزار می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/661763" target="_blank">📅 14:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661762">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
منبع نزدیک به تیم مذاکره‌کننده: تنگه هرمز بدون مهار اسرائیل در لبنان باز نخواهد شد
🔹
رفع محاصره دریایی برای بازگشایی تنگه هرمز کافی نیست
🔹
همچنانکه در بند ۱۳ به صراحت آمده، عدم اجرای تعهد آمریکا در بند یک، به معنای عدم اجرای بند ۵ نیز هست و این بدان معنی است که تنگه هرمز باز نخواهد شد.
🔹
اجرای بند یک درباره جنگ در تمام جبهه‌ها از جمله لبنان، رفع کامل محاصره و صدور اسقاطیه‌های فروش نفت، پتروشیمی و مشتقات ایران، شرط بازگشایی تنگه هرمز است./ تسنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/661762" target="_blank">📅 14:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661761">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
خبرنگار صداو سیما: یک دور رفت و برگشت پیام با واسطه پاکستان بین دو‌طرف انجام شده و یک دیدار هم با هیئت قطری برگزار شده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/661761" target="_blank">📅 14:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661760">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
خبرنگار صداو سیما: یک دور رفت و برگشت پیام با واسطه پاکستان بین دو‌طرف انجام شده و یک دیدار هم با هیئت قطری برگزار شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/661760" target="_blank">📅 14:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661759">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnapp | اسنپ</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbCNquslmFk5ZQtFfHeX2nFpqpW2wbVFJMrDV1H7yh-dcdNJ1n4cf91AKMme7GXRu1bOiBB2vjEVXBy8iNv0mnzTYhTBzxcsS0-kbnIH_Kf2iE1tLKIpFUbE_yy_GLzpPtTT1pfD3oZXTACTBZ40679nllagf3Fl16xxx5VhvDiUOyCE4qyEi48juuU3Mn_1a3zk-IwI_escbIw9T_ipL88Zz8r-0saQQ35cbtE969NZH8zjuYBip6AjSKGByoK3UJbuqW7QOW-9-X6D-_gxUq_gwqYHpZuENHG3p7Qh-FtqVSR4xmYUQhtG53BWTAF39bQIcZVGZ5hFHawXlGpm6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥳
چیزی به شروع بازی
ایران - بلژیک
نمونده.
🇮🇷
⚽️
🇧🇪
⭐️
با پیش‌بینی این بازی، هم
۲ برابر امتیاز
می‌گیری و هم وارد قرعه‌کشی
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/661759" target="_blank">📅 14:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661758">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
وزیر اقتصاد: قرار است رقم کالابرگ افزایش پیدا کند اما فقط برای ۶ دهک پایین جامعه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/661758" target="_blank">📅 14:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661757">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
مذاکرات ایران و قطر در سوئیس در مورد آزادسازی اموال و سرمایه‌گذاری ۳۰۰ میلیارد دلاری
🔹
دستور کار دیدار ایران با هیئت قطری در کنار اجرای کامل بند ۱ تفاهم، پیگیری اجرای بند ۶  و ۱۱ تفاهم یعنی سرمایه‌گذاری ۳۰۰ میلیارد دلاری و آزادسازی اموال بلوکه شده ایران است به نحوی که
۱۲ میلیارد دلار آن با فوریت در دسترس قرارگیرد
.
🔹
قطری‌ها در این نشست در سطح نخست وزیر حضور یافته‌اند که نشان دهنده پیگیری سطح بالای آزادسازی اموال بلوکه شده است./ جماران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/661757" target="_blank">📅 14:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661756">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
هیئت ایرانی شرکت کننده در مذاکرات ‎سوئیس دیداری با ‎گروسی نخواهد داشت
🔹
رافائل گروسی که به سوییس سفر کرده است صبح امروز با وزیر امور خارجه سوئیس در بویگن‌اشتوک دیدار کرد ولی هیات ایرانی حاضر در این نشست برنامه ای برای دیدار گروسی ندارد .
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/661756" target="_blank">📅 14:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661755">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
هنوز ۶۰ قطعه از پیکر دانش‌آموزان شهید میناب خاکسپاری نشده است
رئیس دادگستری هرمزگان:
🔹
هنوز ۶۰ قطعه از پیکر شهدای دانش‌آموز میناب که در تفحص‌ها از محیط مدرسه و فضای پیرامون یافت شده، خاکسپاری نشده و باید شناسایی از طریق آزمایش دی‌ان‌ای روی آن‌ها انجام شود.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/661755" target="_blank">📅 14:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661754">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d513861ce4.mp4?token=UaagAm5NroixkOHJmgrj7IpUiO5F_tZVw4GM1gtD_sZvfuxEQNsiXh_Ul9DMOlNJ9dH0MqXz3zHIe7IG8DnO30x25E69uVrOtMdRNVELVxUQ1IQ5jvIw5kYiYNfcpoT_u13gJnLkMhNR0wLIczD40UHjTsoMWEkXziymw2Civ_O_pBqITVFj2xdM9yPvSOC5aQqdlTAKzManIIhK4UhXJykaqm1i_20lUEexdjbcJa_W4r3NC94UDJBouLtgSDQLfMq4o03P3vVo6tsF0BnHW1TcyqJ-9mAIhk8Ns-DfgD5DnlEOzqeSJlfwFjDyFMAQ5SnLTP0bBYjIDn54FoGhKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d513861ce4.mp4?token=UaagAm5NroixkOHJmgrj7IpUiO5F_tZVw4GM1gtD_sZvfuxEQNsiXh_Ul9DMOlNJ9dH0MqXz3zHIe7IG8DnO30x25E69uVrOtMdRNVELVxUQ1IQ5jvIw5kYiYNfcpoT_u13gJnLkMhNR0wLIczD40UHjTsoMWEkXziymw2Civ_O_pBqITVFj2xdM9yPvSOC5aQqdlTAKzManIIhK4UhXJykaqm1i_20lUEexdjbcJa_W4r3NC94UDJBouLtgSDQLfMq4o03P3vVo6tsF0BnHW1TcyqJ-9mAIhk8Ns-DfgD5DnlEOzqeSJlfwFjDyFMAQ5SnLTP0bBYjIDn54FoGhKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دانشجوی ۱۹ ساله‌ای که با ۲۰ دلار، ۵۵۰ هزار دلار درآمد کسب کرد
🔹
دانشجوی ۱۹ ساله چینی با کمک Claude، تنها با ۲۰ دلار و در یک ماه، رادار هوشمند ساخت؛ سیستمی که سرعت خودرو را تشخیص می‌دهد، ویدیو ثبت می‌کند، پلاک را می‌خواند و جریمه را خودکار ارسال می‌کند.
او این ایده را به دولت هنگ‌کنگ ارائه داد و با قرارداد ۵۵۰ هزار دلاری بیرون آمد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/661754" target="_blank">📅 14:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661753">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ریزش ۳۴ هزار واحدی شاخص بورس
🔹
تخفیف ۲۰ درصدی قبوض آب برای مشترکان کم‌مصرف
🔹
تشکیل ۴هزار پرونده اغتشاشات دی ماه در اصفهان
🔹
رسانه‌های عبری: نتانیاهو به باری سنگین برای اسرائیل تبدیل شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/661753" target="_blank">📅 14:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661752">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
پزشکیان: چرا مردم به خرید طلا و ارز روی می‌آورند؟ به این دلیل که پول خود را در بانک می‌گذارند، اما پولی که ۶ ماه یا یک سال بعد دریافت می‌کنند، دیگر همان ارزش گذشته را ندارد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/661752" target="_blank">📅 14:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661751">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
پزشکیان: ادامه جنگ به نفع هیچ فرد یا گروهی نیست
🔹
بر اساس همه تحقیقاتی که در جهان انجام شده است، هر جنگی موجب اختلال در رشد، توسعه اقتصادی و اجتماعی و افزایش فقر و بیکاری می‌شود.
🔹
این سخن به معنای ترس از جنگ نیست. ارتش، سپاه، نیروهای هوافضا و مردم ما نشان دادند که با قدرت در برابر تجاوز ایستادگی می‌کنند و اگر جنگ ادامه پیدا می‌کرد، با قدرت مقاومت می‌کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/661751" target="_blank">📅 14:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661750">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
پزشکیان: صدا و سیما نیز باید ملاحظات لازم را رعایت کند و مراقب باشد اجازه داده نشود تلاش‌هایی که در حال انجام است، با طرح مطالب یا حضور در تریبون‌ها خدشه‌دار شود
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/661750" target="_blank">📅 14:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661749">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌ویکم از فصل چهارم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای باقر حسین‌زاده که به وجود خداوند بی‌اعتقاد بوده و به خاطر اعتیاد و در حال مصرف مواد به ناگاه روح از جسم به طور سخت و وحشتناکی جدا و در آتش برزخ می‌سوزد و خاکستر شدن تمام سلول‌های بدن را درک می‌کند و با التماس به درگاه خداوند و ارادت قلبی به امام حسین(ع) در طول زندگی توسط اشاره‌ای از جانب اهل بیت به جسم باز می‌گردد را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: باقر حسین‌زاده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/661749" target="_blank">📅 14:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661748">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e342b75637.mp4?token=A_syqA5qxRyIVuQ2RqR3TGzZTJkuBStubkSuEKHjMUtiPr7qnL1G7w9LrMgsa8EKhK8clQfD90OWkAGL4ZMxYFA2T2-OGJPHBEd2_XRxwz53y83-kRkOuc7z6A1_xghTOdi2Jyn3P36O2wamzlxevK5KMlLsQNGk2ZkqyGBkwOkA34XkFsWPcGI12jcVu8gLUNQc8-MTs6ytQf2NKNOTV4l8Jc_2A9pj0HL-1ZPdBVR9rvfnTi6PPL_KlwWoBjabPTq_tWpo1JDN622O2IGWGxWEvQ18YzBPE7JHb8mx9PYadQvnP6vDzjSEECnN4HL0-qwWjNi-6KVS8dXCtrMqJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e342b75637.mp4?token=A_syqA5qxRyIVuQ2RqR3TGzZTJkuBStubkSuEKHjMUtiPr7qnL1G7w9LrMgsa8EKhK8clQfD90OWkAGL4ZMxYFA2T2-OGJPHBEd2_XRxwz53y83-kRkOuc7z6A1_xghTOdi2Jyn3P36O2wamzlxevK5KMlLsQNGk2ZkqyGBkwOkA34XkFsWPcGI12jcVu8gLUNQc8-MTs6ytQf2NKNOTV4l8Jc_2A9pj0HL-1ZPdBVR9rvfnTi6PPL_KlwWoBjabPTq_tWpo1JDN622O2IGWGxWEvQ18YzBPE7JHb8mx9PYadQvnP6vDzjSEECnN4HL0-qwWjNi-6KVS8dXCtrMqJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهباز شریف نخست وزیر پاکستان با ونس معاون رییس جمهور امریکا، در حضور کوشنر، ویتکوف و فرمانده ارتش پاکستان دیدار کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/661748" target="_blank">📅 14:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661747">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSY69YjRktOubaKeA1HD7z2DJGUZhyn_aejW4EQ-35DidiXWP0xi3O8hHzZVrENpWmnW54yvDMYq4gDbdfiKfIOFYQAg0nUFkZFRh1ftyFN24u2wkYpzLBs9FN_H4iHnsoUjhZc4Cgr1TmxQL63hv58uiJs4CmnGVC5SPgA8EC1g3fceIArfeKQcMp67GT-Gk_lIiEPLlHWCNgJ7WQeakxBujCnjml_jER_KNJS3sp0KSiY1D2ZKnP3g4qpEqwaboTr0-I43o38QRcN1tgbxanV1ZFobNWD02KKEsLYAq2rAZ78p02rmNnRQc2z7TYl9str2MbCNKpDay-DrAnQQ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۳۱ خرداد ۱۴۰۵؛ ساعت ۱۳:۰۵
🔹
قیمت دلار امروز با کاهش ۲ هزار تومانی نسبت به روز گذشته به ۱۵۹ هزار تومان رسید؛ در حالی که این ارز روز قبل در سطح ۱۶۱ هزار تومان بسته شده بود.
🔹
کاهش قیمت دلار همزمان با سفر هیات ایرانی به سوئیس برای مذاکره با مقامات آمریکایی رخ داد و امیدواری‌ها نسبت به پیشرفت گفت‌وگوها را افزایش داد.
🔹
در همین حال آتش‌بس در لبنان نیز تا حدی از تنش‌های منطقه‌ای کاسته و فضای روانی بازار ارز را کاهشی کرده است.
🔹
با این حال، به دلیل تردید معامله‌گران نسبت به نتیجه مذاکرات، افت قیمت‌ها محدود مانده و یورو نیز با کاهش هزار تومانی به ۱۸۵ هزار تومان رسیده است./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/661747" target="_blank">📅 14:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661746">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhsYiY0u1t3QxabZKtH9ULHTsQzaXSV5pD3q_wFjxIHDYH_HkRtRylVvn50oBYBYzWGMXjcJyFfFvSFuA-2GMDW31cfkBiW8o5BMUX9ntx-YuMaNnnHxREaPZ7Xhl2Aps-_4xboeflWLAFei4keiZlGflCXfoxYL7S6GQuJn5orVEvw59NNc6MB3pw6N2dSHVtUh7JsVusB5mkXlMWXm0ZPEIgwHzwS0lTDYPUeNhvCvCRZsvUGCIzQ8CmixK0gSiTpsBdkulKg99i73_yhqfM8bOVy4GRzUAU1f3JR2ZHgrTX7h_9ffktTyhkw9ZdWwagYFUcbSqWVs3p5r5c-mzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«تورم» رو زیاد شنیدیم، ولی دقیقاً یعنی چی؟
🔹
هر روز یک واژه برای فهم بهتر جهان #واژه_کاوی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/661746" target="_blank">📅 14:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661745">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b12443b818.mp4?token=IUwGFonb6SP7pHbcYvlkcwm8hCPvSIAey3zYi0i641RwnilawPNzcozgSGy2on1wH9y7JyK-XJ97XvsgJiqiv6Hrkd1wJI-5JZMX3WhZggkTP77CIkkWWOkDd6yLAgs7iR2th3NJSaIi9I5oZouu6yuIe_AJ53iHrab4AJT4Ces8O1tZBY8ClMcSYpJxnAOAEfd5QucWusgEjo8Dw_18uLVeJ7ANhLZzGPxnLFEi_7OBK0qvLxbgVTTOUoJoNYrSahs36MsM3PPynP7_zRMLiscmGgdhYlI7m636B4FVxxPE2ZLfC31dbuuoDyBj2fncpuiEv2cbrUE-X-fHoD51cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b12443b818.mp4?token=IUwGFonb6SP7pHbcYvlkcwm8hCPvSIAey3zYi0i641RwnilawPNzcozgSGy2on1wH9y7JyK-XJ97XvsgJiqiv6Hrkd1wJI-5JZMX3WhZggkTP77CIkkWWOkDd6yLAgs7iR2th3NJSaIi9I5oZouu6yuIe_AJ53iHrab4AJT4Ces8O1tZBY8ClMcSYpJxnAOAEfd5QucWusgEjo8Dw_18uLVeJ7ANhLZzGPxnLFEi_7OBK0qvLxbgVTTOUoJoNYrSahs36MsM3PPynP7_zRMLiscmGgdhYlI7m636B4FVxxPE2ZLfC31dbuuoDyBj2fncpuiEv2cbrUE-X-fHoD51cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تماس تلفنی، دعای خیر و آرزوی موفیقت خانواده شهید میکائیل میردورقی از شهدای دانش آموز مدرسه شجره طیبه برای قالیباف رئیس تیم مذاکره کننده ایرانی در ژنو
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/661745" target="_blank">📅 14:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661744">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
زمان مصاحبه‌های دکتری ۱۴۰۵ به هفته پایانی تیرماه موکول شد
سازمان سنجش:
🔹
به‌منظور فراهم شدن زمینه حضور متقاضیان در آیین وداع و تشییع رهبر شهید انقلاب، زمان مصاحبه داوطلبانی که پیش‌تر برای بازه زمانی ۱۳ تا ۱۷ تیر برنامه‌ریزی شده بود، به هفته بعد و در فاصله ۲۰ تا ۲۴ تیر منتقل شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/661744" target="_blank">📅 13:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661743">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0-N_M4-dmmXstowERLBT2W4feedNtOoJpOUL_AJYMxNtGUC6seJ7tAHHHjVUKmP6rV83WUAB7yGYd-U-g9im0JArNieingyrYURMoV8w7WZNG12S8I653zdipsz9DmY4ozF8PBHitqcisSBByBJ0xjAvh--aN4cyMJENUiTKGOxFJXbko3zh_unGb2fwlSlpbJ301-cfUruXtAp6y2DVr5prH8dT8-eIP66EpcGjdldvORfxd9yHGdQytcUs04EtYPmSxgATqc1sQScQRcYHwNQvWwIA7C1KP6e0Tcsogud020JCayUtsfcj1VlcrmCe8DpLpzF0sXoVwWT-32jCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام ایگنازیو کاسیس وزیر امور خارجه سوئیس پس از دیدار با عراقچی
🔹
جناب عراقچی به سوئیس خوش آمدید.
🔹
در نشست دریاچه لوسرن، ما چارچوبی برای گفت‌وگو و تبادل نظر فراهم می‌کنیم.
🔹
در شرایطی دشوار و پیچیده، رابطه مبتنی بر اعتماد میان سوئیس و ایران، همچنان در خدمت دیپلماسی و در راستای صلح و امنیت در خاورمیانه قرار دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/661743" target="_blank">📅 13:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661742">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
پزشکیان: در شورای‌عالی امنیت ملی تقریباً همه اعضا متفق بودند که این اتفاق باید رخ دهد و تنها یک نفر نظر متفاوت داشت که وجود یک نظر مخالف در یک مجموعه نیز ایرادی ندارد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/661742" target="_blank">📅 13:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661741">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
پزشکیان:هر پیامی که بوی تفرقه و اختلاف بدهد، در جهت راهبردهایی است که نتانیاهو و سازمان سیا دنبال می‌کنند
🔹
اگر قرار باشد بر اساس نیت‌ها و سخنان گروهی در کشور شقاق ایجاد کنیم، دیگر نیازی به اسرائیل و آمریکا نخواهد بود و خودمان کشور را نابود خواهیم کرد.
📲
🇮🇷
…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/661741" target="_blank">📅 13:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661740">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
پزشکیان: قاعده تغییر کرده است
🔹
پیش از این می‌گفتند باید درباره موشک‌های ایران نیز مذاکره شود؛ اما اکنون می‌گویند همان‌گونه که کشورهای دیگر موشک دارند، ایران نیز باید موشک بالستیک داشته باشد.
🔹
اگر طرح‌ها و راهبردهایی را که نتانیاهو و سازمان سیا تدوین می‌کنند،…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/661740" target="_blank">📅 13:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661739">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
پزشکیان: در همین مدت کوتاه توانستیم بخشی از اعتبارات و منابع خود را بازگردانیم و اقدامات متعددی انجام دهیم
🔹
برخی موضوعات پیش از این، مورد تفاهم قرار گرفته بود و در همان چارچوب پیگیری خواهد شد؛ اما از حق غنی‌سازی خود صرف‌نظر نخواهیم کرد و طرف مقابل نیز ناچار…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/661739" target="_blank">📅 13:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661738">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
پزشکیان: امیدوارم مجموعه افرادی که در مذاکرات فعالیت می‌کنند، از جمله برادرم آقای دکتر قالیباف، آقای دکتر عراقچی و تیمی که از بانک مرکزی در این گفت‌وگوها حضور یافته‌اند، بتوانند مسیر را با موفقیت ادامه دهند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/661738" target="_blank">📅 13:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661737">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
پزشکیان: پول داریم، علم داریم، پشتوانه داریم؛ ادعاهایی که می کردیم را باید عمل کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661737" target="_blank">📅 13:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661736">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HY2UhmeSyefG58mMOniu0UIehkjgzMjrdneHGVLDiqSp7K2dru_K3oa6KFHZUK1ZS4wMVVP0Lgn5EEj2oJrkbXl6UB8wfHXjSnn_VVaVbaTw-89UDDZDhZFeH0zA6cx6-AYju1Z6HcPDXmFch1jiHBohhBXKayttIaNAGv6LbyugHBnXOaLQC1QD9WkZUgdSQgUD_WfhKr07g7TwmnDDG4X9zlBU2k3VQisjbw8dt-nEpxmxQGS3S-c5QHgw0QmPqc1d4ZuoPsYkc8r2ebIUJX3tPLvDlEDuSIbrGbcIBLd0UCGNQOZ6ty68lVXNJAPp18a1yJzWXi4pkzQn7UaM3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
هواداران ژاپن بار دیگر با پاکسازی ورزشگاه تحسین جهان را برانگیختند
🔹
هواداران ژاپنی پس از پیروزی پرگل تیم ملی کشورشان مقابل تونس در جام جهانی، مانند همیشه پس از پایان مسابقه در ورزشگاه ماندند و زباله‌های اطراف خود را جمع‌آوری کردند. این اقدام که بخشی از فرهنگ…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661736" target="_blank">📅 13:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661735">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5654ba754.mp4?token=O-VQZySRYsGpwPLd_9965wkAdlr9Hp2s3bY7tg_ymJ_iD_xcl5iNbTfdUDdwBrWXYeBW8jiMwmVmh7arkZyXNZgkMAXRXJgj839p6aCDcLBHUVlP1reaz6LgN54ZJfa_MZk8kk108YLCDwGzDQwrE_hRw45Wvn29YIfFVDdjUliREYamiBQEcRPgnsHC2Hw10Hink-WyJe7wG2_HIaIj9JN_aBehlI_gso4rCEH9Zi8oq2TncHHuDJqE_DgbwoqN2rWolM9IFm-k9KdMprWxOJMAuoR8b-tgLl0HsuhIjq9xKC6_7p0Hkr5n1BUz-VkD7ie0nbXKo493dPnr6vKSzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5654ba754.mp4?token=O-VQZySRYsGpwPLd_9965wkAdlr9Hp2s3bY7tg_ymJ_iD_xcl5iNbTfdUDdwBrWXYeBW8jiMwmVmh7arkZyXNZgkMAXRXJgj839p6aCDcLBHUVlP1reaz6LgN54ZJfa_MZk8kk108YLCDwGzDQwrE_hRw45Wvn29YIfFVDdjUliREYamiBQEcRPgnsHC2Hw10Hink-WyJe7wG2_HIaIj9JN_aBehlI_gso4rCEH9Zi8oq2TncHHuDJqE_DgbwoqN2rWolM9IFm-k9KdMprWxOJMAuoR8b-tgLl0HsuhIjq9xKC6_7p0Hkr5n1BUz-VkD7ie0nbXKo493dPnr6vKSzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی سهمگین در مجتمع بین‌المللی خودرو در چین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661735" target="_blank">📅 13:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661731">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmkHhBHvwXkpmPgxQPlPe2RIMYrG564ffyTVd26qy4H9qSIZoR4rGfNWiURl5ds0h8J2k_WhwGrmWhBRBFrGUrm6Trbl8DaZM3dG7b5JRip5k2vfyJ7aN6Uqg74yaFjjDQ91u-FQQXbYG1TVPvcq2lzDSbCmGFwYMFhFyrOqYrVedoXLG02mDvsOt-YlBjyaNEUF2oEwUHt0-Rj5gqh5XARrqXsY-X_rO3DGiHcpazr2njcgZBoe5_y8PZ2zdOzuJmbSSApSFrL2kSSNuVe_cNi1PZspvcQNR0ef6ESduJGLLN9novA6mMHb6l_K8nsOO3sXI7Y3gebE8avFk4Ndsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی هیئت مذاکره‌کننده: ایران مصمم است روند اجرای تعهدات طرف مقابل را با وسواس و جدیت پیگیری کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/661731" target="_blank">📅 13:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661730">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940e5d97cb.mp4?token=Lx8Jquhf4EeGcT----Dew_k7rx7eYdfUlkU_UHvUMPrSiS_sBuyIgfQEc-FzRousq6ycaMVXvsx-h-stzSZ_qPLm_efBuVN14cenrORZbcCp_dsx3CFzRoZdXF9QYjkQ8BN2LXijitZUu8YUutVZDAJNb3dbj1yfQrWCEqfYr4EHFcL5If3irOwCkdOPANr2BCMIIbGT9ksFVcQJlbCt7ytvuEkPRu9e9rAtuw3dHVSC_p8bYSLjI36L9cPadkuwuigYcetor4JpcW1W23jITA49Mpf1JXpmtKSVCJ7DgCs-z1s-l8d2Xbjan3VFsp2dexAzuEuewX_50YGI-xQqSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940e5d97cb.mp4?token=Lx8Jquhf4EeGcT----Dew_k7rx7eYdfUlkU_UHvUMPrSiS_sBuyIgfQEc-FzRousq6ycaMVXvsx-h-stzSZ_qPLm_efBuVN14cenrORZbcCp_dsx3CFzRoZdXF9QYjkQ8BN2LXijitZUu8YUutVZDAJNb3dbj1yfQrWCEqfYr4EHFcL5If3irOwCkdOPANr2BCMIIbGT9ksFVcQJlbCt7ytvuEkPRu9e9rAtuw3dHVSC_p8bYSLjI36L9cPadkuwuigYcetor4JpcW1W23jITA49Mpf1JXpmtKSVCJ7DgCs-z1s-l8d2Xbjan3VFsp2dexAzuEuewX_50YGI-xQqSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی که مه‌لقا باقری برای تولدش در کنار سگش منتشر کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/661730" target="_blank">📅 13:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661729">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5e1446eb5.mp4?token=o2Ogpht4yoX3e8C5tcLVrgy_1TzEd32JGZsJKLVDcZ0PtPYjOa3o6YojJaR2wKa5H58oxRzywC5ubVkxknX2KU-VMJft-YS4Qd8CuMW1V5HEEWzipZcJXPTPd0FeagsGksVLcvlQeXPC5MapKDdS6-zdCzO4zHrsW0wNWyEmJJKfo-kABjoQz8OAMACHQgDBK1rqwvoMo4_xQujRoaTjS8tF-bcKgJqf11aDuTSPE7VD6WoA9mTafsdmOJMDkZAVoatDddKH5KhtTxg0ZiqZ04CTVStzsn3hURxzpGtSefElBacWRps83EyhoVdMUCgxUeO1ltdfly4Mczo1J9mBBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5e1446eb5.mp4?token=o2Ogpht4yoX3e8C5tcLVrgy_1TzEd32JGZsJKLVDcZ0PtPYjOa3o6YojJaR2wKa5H58oxRzywC5ubVkxknX2KU-VMJft-YS4Qd8CuMW1V5HEEWzipZcJXPTPd0FeagsGksVLcvlQeXPC5MapKDdS6-zdCzO4zHrsW0wNWyEmJJKfo-kABjoQz8OAMACHQgDBK1rqwvoMo4_xQujRoaTjS8tF-bcKgJqf11aDuTSPE7VD6WoA9mTafsdmOJMDkZAVoatDddKH5KhtTxg0ZiqZ04CTVStzsn3hURxzpGtSefElBacWRps83EyhoVdMUCgxUeO1ltdfly4Mczo1J9mBBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در آرژانتین از مجسمه ۲۶ متری مسی به وزن ۵۰ تن رونمایی کردند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/661729" target="_blank">📅 13:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661727">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b2ab19bf.mp4?token=v6Aj6WwsdtBAsm6WdlEodlVvDdKrWdi8N_ZdpL1aWrXY34ryNEPcRuuRXpGLPW2LmsQItHMICq-xvvDIl79LPUwwo7vo5r2JcJsfQdBXup4WS8V90rE-PK3aDBIz5YKBmBzay7-3jz58xhxmlfjYGXXW9GKMtBDSM9FU_6fJBqUf6d1mUCcishoZZ_V-KT0dtqAEPb-vZrHdU_VcgrpM7Pb3Z2l2n8Tk2xbgwdiCyEyc8809pDJV2IX367yOj7qDBU5coQQCmH6cn29Rs3pC8eRk637cfYwnuRo3kCMk1Sg09BeHGS7gx0GwVLj9bDkUxrL0FRKNWPzK4CcENEyGWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b2ab19bf.mp4?token=v6Aj6WwsdtBAsm6WdlEodlVvDdKrWdi8N_ZdpL1aWrXY34ryNEPcRuuRXpGLPW2LmsQItHMICq-xvvDIl79LPUwwo7vo5r2JcJsfQdBXup4WS8V90rE-PK3aDBIz5YKBmBzay7-3jz58xhxmlfjYGXXW9GKMtBDSM9FU_6fJBqUf6d1mUCcishoZZ_V-KT0dtqAEPb-vZrHdU_VcgrpM7Pb3Z2l2n8Tk2xbgwdiCyEyc8809pDJV2IX367yOj7qDBU5coQQCmH6cn29Rs3pC8eRk637cfYwnuRo3kCMk1Sg09BeHGS7gx0GwVLj9bDkUxrL0FRKNWPzK4CcENEyGWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: ما ۲۰ میلیون بشکه از «نفت خودمان» را دادیم به هوافضای سپاه تا بتواند بجنگد/ در شعام فرماندهان قرارگاه، ارتش و سپاه تفاهم را امضا کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/661727" target="_blank">📅 13:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661726">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
تامین اجتماعی: با توجه به اختلالات و محدودیت‌های اخیر پیش‌آمده در تعدادی از بانک‌های عامل، بر اساس پیگیری‌های سازمان و اعلام بانک‌ها، ممکن است بخشی از واریزی‌های بازنشستگان به صبح فردا (دوشنبه ۱ تیر) موکول شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/661726" target="_blank">📅 13:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661724">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
شهباز شریف نخست وزیر پاکستان با ونس معاون رییس جمهور امریکا، در حضور کوشنر، ویتکوف و فرمانده ارتش پاکستان دیدار کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/661724" target="_blank">📅 13:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661720">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3ea3749ae.mp4?token=iTqal26w3V9f7M09qH29JwRTEkGInSyExsRffYyiRcmNN74stM_aEttRKRvQEIaDJ2ZGXyBYW7mcea1IVR2X2aDhJJx3_noD_olavVBK7p9MnZltFTfTBOAXBGLUr9FTgrj6CVXIuajweGI--41c_Mx2dwKvJI7rmNCkXhKQyYr4A84jfkjGphFmajBmJBV0PGJKIdWCP0bse3HCWIUQIoJhkZpp795uYcF_7L8GbHIG792uYe94ne3lEvjr41YfLRFxs6-8QPIHLN6iS2gbdEVvC7CTbJhfNvXj1Mf6HMM1bz8oYk2sHF-xvbA1-momYIm5m7wMwVZ95S3GA3ehEQZE5qINl5a2tDJw0DLKlSqDA3k-BNE83TbNR3G4coMnvAdza8o8Jl9js0uGd7ldPUKz4p0R0M99AJvs2gw7rm_SjEDm_kUl0jzX3Jj6gqTXmrJgZudjw582qulugM5n32vIAgkk7QTs-bsE--06uZ4AkS0Qq5uVBHmL6-_cWiYecxbbnEDFCAb2UDgPdgH4ZhksLCl1WMfSYFKqDxGiYKur0HBtMbtMjqCiqPmY4heFnt50OxNxoiGQETeWcLM3Q9Eza1ePT8Jl8SpUcsb1QsOcrmZlxB0Q44okSh4VuD_6PKUUxeKXultMxHcAct5y3FuttBcoCrhHLBiwnUF0muI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3ea3749ae.mp4?token=iTqal26w3V9f7M09qH29JwRTEkGInSyExsRffYyiRcmNN74stM_aEttRKRvQEIaDJ2ZGXyBYW7mcea1IVR2X2aDhJJx3_noD_olavVBK7p9MnZltFTfTBOAXBGLUr9FTgrj6CVXIuajweGI--41c_Mx2dwKvJI7rmNCkXhKQyYr4A84jfkjGphFmajBmJBV0PGJKIdWCP0bse3HCWIUQIoJhkZpp795uYcF_7L8GbHIG792uYe94ne3lEvjr41YfLRFxs6-8QPIHLN6iS2gbdEVvC7CTbJhfNvXj1Mf6HMM1bz8oYk2sHF-xvbA1-momYIm5m7wMwVZ95S3GA3ehEQZE5qINl5a2tDJw0DLKlSqDA3k-BNE83TbNR3G4coMnvAdza8o8Jl9js0uGd7ldPUKz4p0R0M99AJvs2gw7rm_SjEDm_kUl0jzX3Jj6gqTXmrJgZudjw582qulugM5n32vIAgkk7QTs-bsE--06uZ4AkS0Qq5uVBHmL6-_cWiYecxbbnEDFCAb2UDgPdgH4ZhksLCl1WMfSYFKqDxGiYKur0HBtMbtMjqCiqPmY4heFnt50OxNxoiGQETeWcLM3Q9Eza1ePT8Jl8SpUcsb1QsOcrmZlxB0Q44okSh4VuD_6PKUUxeKXultMxHcAct5y3FuttBcoCrhHLBiwnUF0muI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: وحدت از بین برود دیگر هر حرفی بزنیم به جایی نمی‌رسد
🔹
مهم ترین مولفه ما وحدت ملی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/661720" target="_blank">📅 13:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661718">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzIkwAxryFQ5Z6hHHU3DqFY6ny0yQ9YVRF0I1JyjXhnsDV8nA1UhE_16k8q4J3boblEdsjEtw_KeKDov2X2qXHCbta42pCi5cBC18K2aZfceyXgYmiSViCTVag3frKR-TC57FstcfRya8mWWkMY9VPkPUEeFmPlWNdLh0roFb1NKuuLXjcF2sUxo2Sxt4GOeHsml4p8jV8Y6WpXviZHoUH6hE6ukywVYVwCfjnqXHMJWOEfBF78d7_vyQLWFmPogw_pRvhCsM5zywKDmfozRG1wp6NHuYHrYSbuMH7Opa05QJEkoTKwVXItzrPxh_3pBUiu_Aai2_HWP9ISG-XYq-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرادو ۲۰۲۵ در امارات ۵۰ هزار دلار است، در ایران ۴۳میلیارد تومان
🔹
حتی اگر دلار را ۱۸۰ هزار تومان در نظر بگیریم و ضرب در ۴ بکنیم هم به قیمت ۳۸ الی ۴۳ میلیاردی این خودرو در ایران نمیرسیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/661718" target="_blank">📅 13:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661716">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_0PYKWhln0hn87HeDHnRJxq9xh7awR-38v50BsGYOqYjKrnrAyd_f2wFKJnSUZ36golK254b6hP_0kyquBQatSH2BXMO08AoArcO07WrGPM1eSxOgYkrndism9ao1fryqJabh4-GmiDe-FbCO6HhdyhBs-fBDs7MSHSNLDrEdwFVTJ0LKKzunEOGjbxnxDcKWR7NgEyW2EnSh6_ocXDTW73jwvaIorHf12eechyrNLWaII2_F9YlC0PSVQA0ivLJ7NVaFjARmA6tSkq2W7qN-x9tKmHvgNlyRMflHwKfpdP1IRgkLsB6FBsFW3pW3P83LbCxrkV99kvTjIaEPCcPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
هواداران ژاپن بار دیگر با پاکسازی ورزشگاه تحسین جهان را برانگیختند
🔹
هواداران ژاپنی پس از پیروزی پرگل تیم ملی کشورشان مقابل تونس در جام جهانی، مانند همیشه پس از پایان مسابقه در ورزشگاه ماندند و زباله‌های اطراف خود را جمع‌آوری کردند. این اقدام که بخشی از فرهنگ «گومی هیروی» در ژاپن است، نمادی از مسئولیت‌پذیری اجتماعی و احترام به فضاهای عمومی به شمار می‌رود.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/661716" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661714">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebe3edb590.mp4?token=drXcR7PfjdWMB7WkB2hjk6k68m0Tcec3ju1DWPOwmqd1MG1xe360ARYsu8-woTZXbWkX7HahteTTSRbLCoslylvugbAXqMOAp1dPGtlCrXhTeObhItcuVAwhQ4MWgc4564J-xpXGXXvMwxpkklh6LTTmMf605-3RpLoWENVSPSxsWa0r3dJ8eXDYyJp6ie2N8JpVXSloNOXYsV45pTPkvMPrAcwHFrNWbO_GI9K45K2It0dUf7plh4hg1l1F5f-feX8m_FKdGhJ8dxY_XiWwsXOK3xMdjf4unU18FEMrMm_NBhj4admVQ7xBrEl6oVdBwQVQIFmS74yW8_z4SBdGtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebe3edb590.mp4?token=drXcR7PfjdWMB7WkB2hjk6k68m0Tcec3ju1DWPOwmqd1MG1xe360ARYsu8-woTZXbWkX7HahteTTSRbLCoslylvugbAXqMOAp1dPGtlCrXhTeObhItcuVAwhQ4MWgc4564J-xpXGXXvMwxpkklh6LTTmMf605-3RpLoWENVSPSxsWa0r3dJ8eXDYyJp6ie2N8JpVXSloNOXYsV45pTPkvMPrAcwHFrNWbO_GI9K45K2It0dUf7plh4hg1l1F5f-feX8m_FKdGhJ8dxY_XiWwsXOK3xMdjf4unU18FEMrMm_NBhj4admVQ7xBrEl6oVdBwQVQIFmS74yW8_z4SBdGtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در چین، ربات‌های انسان‌نما همراه با انسان‌ها در مسابقات قایق‌رانی اژدها شرکت کردند!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/661714" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661712">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
دیدار و رایزنی محمد بن عبدالرحمن آل‌ثانی نخست وزیر قطر با قالیباف، رئیس هیئت مذاکره کننده کشور در هتل بورگن اشتوک سوئیس
🔹
پیگیری اجرای بندهای تفاهم از جمله بند ۱ و ۱۱ یعنی توقف جنگ در همه جبهه‌ها به خصوص لبنان و آزادسازی ۱۲ میلیارد دلار از اموال بلوکه شده ایران و نیز ماده ۶ تفاهم مربوط به ۳۰۰ میلیارد دلار سرمایه گذاری موضوع بازسازی، دستور کار این نشست است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/661712" target="_blank">📅 12:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661711">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
بقایی: امروز دو نشست در صبح و بعدازظهر داریم  سخنگوی وزارت امور خارجه:
🔹
قرار است یک جلسه یک روزه داشته باشیم. صبح دیدارهای دوجانبه با هیات‌های پاکستانی قطری به عنوان میانجی‌های این روند خواهیم داشت.
🔹
بعدازظهر هم نشست‌های چهار جانبه میان هیات‌های جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/661711" target="_blank">📅 12:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661710">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
تصاویر دیگر از ورود هیأت جمهوری اسلامی ایران به سوئیس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/661710" target="_blank">📅 12:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661709">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCG3Q5w5GkInTGlykTTwhyRaYva8MztR7vdNdK6zLrkH69U9rQ1XVQTOsfBZkxFjcHYefdI_lPPpDrxvluE2HC-QkpzctF0fHSCSLwe2V7iw8ucGOBP2bAAHP-kLBcW3d5SHqCNi1JSp9piR7WEufAzZBMEHjUrwvxBKv78l7Zx2Yetjr7e-v8DR-8voi4fhrN8rbKUcsTKyosCaVM3Kz6f2XnwuO2uwKBIRoa4jo0kEJqxfWNh4e3wGdwRJDqcSty-JVjAeonwhMUon6qHmsg-PobeJRXmaI_8uZ8XkqYrG_knSuKhe1O-fx3WaJtjKPyalQfHIXHewDKJ_k1QeoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همسر نخست وزیر اسپانیا ممنوع‌الخروج شد
🔹
«بگونیا گومز» همسر پدرو سانچز، نخست وزیر اسپانیا پیش از این پس از دو سال تحقیق، به اختلاس، اعمال نفوذ، فساد در معاملات تجاری و سوء استفاده از بودجه متهم شده بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/661709" target="_blank">📅 12:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661706">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
بقائی: آمریکا بند اول تفاهم را اجرا نکرد؛ توقف جنگ شرط ادامه مذاکرات است  سخنگوی وزارت خارجه:
🔹
در نشست چهارجانبه ایران، آمریکا، قطر و پاکستان، اجرای تعهدات آمریکا و توقف جنگ در همه جبهه‌ها، به‌ویژه لبنان، محور اصلی گفت‌وگوها خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/661706" target="_blank">📅 12:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661705">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emcG6__oaQLnLtoRcjNAuOm6HMbfFGSbl9NG8dKrv-3LtOmLJiZyr7yEjFNvQShWfKTAiBG_SHYOzLVy55nOvFjG0mqJVTOM1cMuFnMRmX1ZmfWtmputC077owm8tMuijzklw-nRpUlEs7kBlpIWIhDs1lXDTBNJqfpLOgPSChQWuSxzPOVnL9ihC2L8gNV9QwGLQnXEZVelQxIVcFHg5qx8x6FPPFVIrJCD_oQlODjCYs64ET-_pVs8aOniTU8rByztyZQOaNqgp2inFBV3hyBgA7Ts2G0AuE85GSVwTa2AqyYbFqVzJV6sAdaafd7CMZ7v2WluoyzdqoUCOBoIwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پوستر فدراسیون فوتبال ایران برای بازی امشب مقابل بلژیک با تصویری از بیرانوند و کورتوا
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/661705" target="_blank">📅 12:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661703">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5857eb70e1.mp4?token=Qjmx2jduoEp8xqALz-_gLpsTxL0i2O6M5jjU4CeyhzYd9jQv805wFxZMtyMVZb0U6UT6FTR-gDwrlXO7x1ymUiGKpQiaVgFRYJ_NZ3EpUQS9VvA7yIotmoOq3z0U1z1NJ7HxJ5SUYVwQpv56_f7hiEu9qNI3VNPKIgZbHtuOL-oWHCPeUXZj4Ft2F1jNrzvKwJ43aQdq0OKkYN7FtYnbRAEhSoGn_GaASu0wtYKxCB_Ec8yZZMQnEitCiHCzgeGWsXG8-tS1WU9KC3_7lwE3vphUtWA9vO6towdcghzFSyxIXnynuIfGrwfGphCg5zTZgExpul2QGe6wmEHaPkHk4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5857eb70e1.mp4?token=Qjmx2jduoEp8xqALz-_gLpsTxL0i2O6M5jjU4CeyhzYd9jQv805wFxZMtyMVZb0U6UT6FTR-gDwrlXO7x1ymUiGKpQiaVgFRYJ_NZ3EpUQS9VvA7yIotmoOq3z0U1z1NJ7HxJ5SUYVwQpv56_f7hiEu9qNI3VNPKIgZbHtuOL-oWHCPeUXZj4Ft2F1jNrzvKwJ43aQdq0OKkYN7FtYnbRAEhSoGn_GaASu0wtYKxCB_Ec8yZZMQnEitCiHCzgeGWsXG8-tS1WU9KC3_7lwE3vphUtWA9vO6towdcghzFSyxIXnynuIfGrwfGphCg5zTZgExpul2QGe6wmEHaPkHk4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تنها کشتی‌های ایرانی از تنگهٔ هرمز عبور می‌کنند
🔹
اچ‌اف‌ای، شرکت تحقیقاتی و تحلیلی در زمینهٔ سرمایه‌گذاری در بخش نفت و گاز می‌گوید، از روز گذشته تاکنون تنها کشتی‌هایی که به ایران می‌روند از تنگهٔ هرمز عبور کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/661703" target="_blank">📅 12:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661701">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xras6jlLJQ040UnboujApBACy6nitBGJjhxCEDJ-AcZcu9amW0hOzgt-oe9RDKmy-MWZPnUwEo4BCj0TvfUf3TjvJLAhf3mwb1CQGdzdELvCef3ikqisBSIaBnIJuOh8Erh2mIjTwrzGLazN3bnfwF-JSnyT8Yu0AAh4JWpTwoWn3uyfCYCZhIyLWJqaEs9KteJwPenBkCojUS73tvhnG5kQbLUVGstTWOo1DbwYHCTfjxFrON_5Pc1vVAASD1G9QiyTrVjd8hcqIbQx1u3qRsJSSbD_Xm-M96v53fAdjPvqDD19KeJYHM5VE1OvNihGZuk2ABwf4oyKLl1UUpOJoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هیات ایرانی عازم ساختمان محل مذاکرات شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/661701" target="_blank">📅 12:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661699">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a86d7bde5.mp4?token=LDjDCtaEO4ueLWz4CiglC2LTzmBRNkkurh07oU9R7nFFlgGzM2VejscDjVE_vQrVRBGrhRwY3vtVuGXkqDK4P9ajn85Jo6HnD86vKnmZchYino-nYSw9QjLB9XVRIpqfdfjN1EEfe9bisSo6NrRBbip3XWKaU7iiUSuIT3-aV7XPh3PtEjzYp7ITLjptm7HKWzPORKkJ5eMF8GD4ZVQo45d8oqU5jlIunhSxihJ73LJr7CVvAt1Wfs8d7A3UUrb604lBwdpMjqmTfORmBfXjG7lE54xwx_YsWx8Xn5mtcMXaoczq5-FhaVxxCiSGV46H2iuNuApL97zclJB7wB1FsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a86d7bde5.mp4?token=LDjDCtaEO4ueLWz4CiglC2LTzmBRNkkurh07oU9R7nFFlgGzM2VejscDjVE_vQrVRBGrhRwY3vtVuGXkqDK4P9ajn85Jo6HnD86vKnmZchYino-nYSw9QjLB9XVRIpqfdfjN1EEfe9bisSo6NrRBbip3XWKaU7iiUSuIT3-aV7XPh3PtEjzYp7ITLjptm7HKWzPORKkJ5eMF8GD4ZVQo45d8oqU5jlIunhSxihJ73LJr7CVvAt1Wfs8d7A3UUrb604lBwdpMjqmTfORmBfXjG7lE54xwx_YsWx8Xn5mtcMXaoczq5-FhaVxxCiSGV46H2iuNuApL97zclJB7wB1FsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: آمریکا بند اول تفاهم را اجرا نکرد؛ توقف جنگ شرط ادامه مذاکرات است  سخنگوی وزارت خارجه:
🔹
در نشست چهارجانبه ایران، آمریکا، قطر و پاکستان، اجرای تعهدات آمریکا و توقف جنگ در همه جبهه‌ها، به‌ویژه لبنان، محور اصلی گفت‌وگوها خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/661699" target="_blank">📅 12:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661696">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dM--RhCjqF3l0NED04Pon5nbBuXvW9FojmXQNNzNEM0WVfC88ej4xslKoax6BTIOf_HGBo3xV5y147QMawYulA2uOT4gzhqmGMEFMUo2jJp3ySC069jK242NXjOBtObs4g8G5iWz7oUmpBWcC_P4gP9N5Y2l2HQVb_Up7jnhsqOGmTKDWvaKbuGq-X6c26bJZ4H1AY1oJq2lHPcIIh_e0XF501yAHIzqcFg9rAeXvtbTcqsacD9mWnbLxNwYlSIq8HTuyrKskTZWkhxoEICDMxLPKaGcFLvHkJ9XCQmhdFPHTNi8UgH2HjVpErK8SC_eDWGoIboB-vECJshvdIeX-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۷ راهکار طلایی برای محافظت از حساب‌های آنلاین و اطلاعات شخصی #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/661696" target="_blank">📅 12:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661695">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
بقایی: امروز دو نشست در صبح و بعدازظهر داریم  سخنگوی وزارت امور خارجه:
🔹
قرار است یک جلسه یک روزه داشته باشیم. صبح دیدارهای دوجانبه با هیات‌های پاکستانی قطری به عنوان میانجی‌های این روند خواهیم داشت.
🔹
بعدازظهر هم نشست‌های چهار جانبه میان هیات‌های جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/661695" target="_blank">📅 12:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661694">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
پزشکیان: توافق با آمریکا به نفع ایران است  رئیس‌جمهور:
🔹
تمام مفاد تفاهم‌نامه ایران و آمریکا به نفع کشور است، ۶ میلیارد دلار از منابع ایران در قطر آزاد می‌شود و تنها خواسته آمریکا، نداشتن سلاح هسته‌ای از سوی ایران بوده که جمهوری اسلامی پیش‌تر نیز بر آن تأکید…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/661694" target="_blank">📅 11:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661693">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMICqAFrj2XCPQh8NI84bXr35zG4qet-VfpyBxArg5DYsjTn6kqScnHPOMmvZtjAmxWBGMNIxqXdou9lQs8pH-j9TDZhw7ihfgIAKJyreUSg-WGJJo07PYMPwNcg4p2I4qKVe4sBCDP3BOL_Qyiink9F3OKvyCH_yXR5TLmuq9Iz-nn4DzXUWadK1N_p3q6YLi9FoxF4XChH7QqIPEulHRdyozHnnC9vCOW4CnT97hGcB07sB12MqrnmbkQPKuTF0SnlnNEqKoD5ILctbSlqt0_g18rITV7LksoxxoVA73c79YmwJrTplRqVj-OEhlTTh3LJ2IZKZj7pJw4NXn00MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
یکی از قدیمی‌ترین تصاویر رنگی موجود از تهران ولیعصر در دهه ۴۰ در کنار تصویر امروزش
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/661693" target="_blank">📅 11:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661691">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
بقایی: امروز دو نشست در صبح و بعدازظهر داریم
سخنگوی وزارت امور خارجه:
🔹
قرار است یک جلسه یک روزه داشته باشیم. صبح دیدارهای دوجانبه با هیات‌های پاکستانی قطری به عنوان میانجی‌های این روند خواهیم داشت.
🔹
بعدازظهر هم نشست‌های چهار جانبه میان هیات‌های جمهوری اسلامی ایران و آمریکا و با حضور نمایندگان قطر و پاکستان برگزار خواهد شد./ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/661691" target="_blank">📅 11:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661690">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
دیدار عراقچی و وزیر خارجه سوئیس در بورگن‌اشتوک
🔹
سید عباس عراقچی وزیر خارجه در نخستین برنامه رسمی هیأت ایرانی در سوئیس با ایگناسیو کاسیس وزیر خارجه این کشور دیدار کردند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/661690" target="_blank">📅 11:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661685">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cetSnKdafQ5jJgk_obqe-4ocZ57TRfdJZosaMe1BFo_HT4btb7QEU1e05T_D2N_ne7dZTAiCJ2n1ddVrVJHwz7brFZMGJwyDbvA9fOQp9AtVw0T9rgWVlXVgjvtacKZs8YDMx3sax2KMmjIZ7GjwL4BbEj4gnBq__8cZg0UqkzY4NuVwg9rP0K39WX4E2h9vExEstTFiCh4yVexqzMCXm8kWbIVf5_ZLB_9wqAXOhwcaVFFgoTHCWyBudJR4j2xmCZB9otSiEBqZ4WeSOOh9_1t4dkB4TsirzY2alUrSgdEMRdPRpS2-ssE2MSnfXqkI_N7PZBPbnputjR4xLEK7Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PABMWglW7iwkq4aLkaCt6-IKjIf3KnMvmtJP9VPHIyQAJAwEEEs3Sy_u0zwsZKYKQ5_HCekURf3Gz2d2hgSGSglXLvM1UGv59K3eY4mwxbvmECE_eO_Lr91CjDvwfCdRZxO4LFgo5EGIGkBrKPhPn1JFwr--Bz50sM5Lirebjr61hBlQVZ3xqfbXrZqy7PVW_jRvOkX0GPO2scz5kPqxmTeELE4XSu5q1Bu-CWSxMsqTMDKjLokMBeBwwPFn6pAZFnV3KPIR08U3FzWcPqKv5Nui6lQfe9Xts0-bYkcN58gEimr08gIbCgUZHTLhGA-VKVyXKKQVoOfYJu0HkPnx8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZNnkcT2cCLTweVJVj8WXuAI7MNbLHBZuRx-7GHz97W6qD74LLHhHSB8K2yVUtQFBbRaUksUhMW_V5zlMNaMJVwAN1mUDrvFaQoKEaXIrfisftBNe2nK_PDZfKbaSF_ed8-5KriXUQX_LyLHmF-li5qgFzxFrHN83oPIp0mOpaXBycU5lU0YQIbIKzwG121sm-4eZWp_rbUWclh-h3h1aazUfnhrOzYmfpP1GiBO0nGUrQVttXc9_EdgTTuiLn2hks4rDhDArm3bbw44Bjn3R7gKW6ufNecqgerxeczyHblrpyfY1yUGAOXsnSLVlhFJLEr3PRk4rIhTQOwxwFVSBBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pVoJ7JUMX3DvvvUbbX4nFm5uZxn51szIMAAX6zCRdHLG32jCfYwcF5GnbFgVruM_2FjJuOSNZ8Bzn8L6j2zHOzUWFN_ws-6FGfpeCD2Sizmfvd8_T-wC_GfGgz9wJeuk6paU2m-UqJI3lcfv1SaQqy1el3zSWdOmcQgQTM58tMC7fw3GmcF0bPzQLeax_XLfq_tYq4D9ctNnTVonOo6VT4YtOclgBiG8JSOkAtlLV6AIQSv5J_EqB19VUlOUP1Ux-zgyvoCURd0mZuAEsrRb-EISma6JepQJNDW1ZUP6yI-v6Xz23f5VJ4WAf1vlXuGbbcxFw2wWQO3wS1hqiwe7HA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
با این چند دستور ساده و مجلسی، استاد حلواپزی میشی
🔹
حلوا فقط یک شیرینی نیست؛ یک ماشین زمان است که با اولین قاشق، ما را به دل خاطرات، خونه‌ مادربزرگ‌ها و سفره‌های پربرکت نذری می‌بره
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/661685" target="_blank">📅 11:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661684">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
تنگه هرمز مجددا بسته شد  قرارگاه مرکزی حضرت خاتم‌الانبیا:
🔹
وَإِنْ نَكَثُوا أَیْمَانَهُمْ مِنْ بَعْدِ عَهْدِهِمْ وَطَعَنُوا فِی دِینِكُمْ فَقَاتِلُوا أَئِمَّةَ الْكُفْرِ ۙ إِنَّهُمْ لَا أَیْمَانَ لَهُمْ لَعَلَّهُمْ یَنْتَهُونَ(۱۲ توبه)
🔹
نظر به بدعهدی‌ و پیمان‌شکنی…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/661684" target="_blank">📅 11:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661682">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
رئیس جمهور: مبلغ کالابرگ را افزایش می‌دهیم  پزشکیان:
🔹
ما وعده افزایش رقم کالابرگ را داده بودیم، مبلغ کالابرگ براساس تورم باید اصلاح شود.
🔹
بگوییم رشد ما ۱۰ درصد است اما مردم کماکان فقیر باشند به کار من نمی‌آید. من رشد ۵ درصدی توامان با رفاه مردم را ترجیح…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/661682" target="_blank">📅 11:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661681">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBzqpe-_rnMNQezcf4qcJPTwvBqL79scfFbj-9KeoczQw4A06sM3zxYH4MmhT-q0QdmJFSiqwqO63k-yr326wr_kCGbsaRH8f1kDc4mkDlbsYpnmexXnEzlWK7WymXAL817WHBbRXUxAdofdBEnYjR-BTxCNV7qMRa4OcZpyUk_r6h-qu9mFd7QoVTcbveYgL4npaAdBcBTSr2vTnQi3W3taFOB4r-cz2AmbIBWPHzCtUugWZoI4aqI4ptvhQu1K0Z_N8OFCBZCPZJkVrbuSlRJdnrrWW0En5lGXIeKKjofwG_nFH-EtWdCB3ZdSnn18EjqGhKrQ-A5i2jPMh9fLXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رونمایی از سریع‌ترین بازیکن جام جهانی | جوردن بوس کیست؟
🔹
وقتی فیفا آمار سریع‌ترین بازیکنان دور نخست جام جهانی ۲۰۲۶ را منتشر کرد، نامی در صدر فهرست دیده شد که برای بسیاری از هواداران فوتبال غافلگیرکننده بود؛ جوردن بوس، مدافع چپ تیم ملی استرالیا.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3224482</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/661681" target="_blank">📅 11:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661680">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
تصاویر دیگر از ورود هیأت جمهوری اسلامی ایران به سوئیس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/661680" target="_blank">📅 11:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661678">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e72e4364a.mp4?token=VIkcvWKXRJgUDd86Td6YktmGIYFEsGHSjUMC4gDPwsdZ40VsmgOAJ8IVcS3IZrH_E8mpEqqqCjECVl6C5pwxGfqK6AoPjMzwLOmM1-vzvr3f5FDr1Ge4lOJDpBKtypWTarwoP6QK2P-_-fnZGhDWAJcZqdYfk38nK5d5qvgLzOZWVAQ2SuL2NnUoex3Fmsp8S_G7WdojCC0ZX6WiOLK2iS2OyKzg7S_i6sCJUqwU2gsFkAvSTULdWs1idgB3fHBFKPkgtIFzmWJRTlsnWDLEawHRC_2d6ptc1e-UhOzj7HYlZoGbS0DrfnvZ3o9Dkf2N7_s218eXzBmDI18_pUrYGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e72e4364a.mp4?token=VIkcvWKXRJgUDd86Td6YktmGIYFEsGHSjUMC4gDPwsdZ40VsmgOAJ8IVcS3IZrH_E8mpEqqqCjECVl6C5pwxGfqK6AoPjMzwLOmM1-vzvr3f5FDr1Ge4lOJDpBKtypWTarwoP6QK2P-_-fnZGhDWAJcZqdYfk38nK5d5qvgLzOZWVAQ2SuL2NnUoex3Fmsp8S_G7WdojCC0ZX6WiOLK2iS2OyKzg7S_i6sCJUqwU2gsFkAvSTULdWs1idgB3fHBFKPkgtIFzmWJRTlsnWDLEawHRC_2d6ptc1e-UhOzj7HYlZoGbS0DrfnvZ3o9Dkf2N7_s218eXzBmDI18_pUrYGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برای ایران
🔹
در آستانه دومین دیدار تیم ملی فوتبال ایران در جام‌جهانی، مخاطبان با ارسال پیام‌های صوتی پیش‌بینی خود از نتیجه بازی ایران و بلژیک را با ما به اشتراک گذاشتند.
🔸
شما هم پیش‌بینی خود را ارسال کنید و در حمایت از ملی‌پوشان کشورمان همراه شوید
👇
#برای_ایران
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/661678" target="_blank">📅 11:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661676">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOlOZqI921hKYET9p9J0_yCQXXZez6B5e7Acjaaqb1gspbfFaietWy1o8jXZqq0YqrjzmqxdVXXfeOV03xai-Ku1jfpMFYFmbu2770wLaBBgifQHhxLzG2JlMBQLBzv9eu3yXO357qJrQeqhd7hhtjrs0LECFAkVrmZSMzdaovbOPjNmeKtI9P3pZ8Qo42T083pKnUf8KrIjQQt8frRQCQyWsltfwbnL3S8IOxl2VspfHqp7KXAKrAHhPiAl8j-f8zUgk1CDwQ7wc1ivGQwCilvV1FLCln0GSZjrdaY9IpDk7PQzAkJ-5-WleHF1n8os8943O56Yz9J6a0gOdLY5hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
لباس خاص داوران مسابقه ۱٠٠٠ تاریخ
🔹
دیدار بامداد امروز تونس و ژاپن در جام جهانی ۲٠۲۶ هزارمین مسابقه ادوار جام‌های جهانی خواهد بود و فیفا به این مناسبت کیت خاص و متفاوتی طراحی کرده است.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/661676" target="_blank">📅 11:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661675">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f5c0f6a0.mp4?token=UszmxzbF8o-TZOUrZmq22Rq35tZlHSe7nkkSeuCbKC4vD2TUYM1P9F6E977Kggc2DYiYPDsiin-qjySBFI9m4khCUZrdO1GmnHYSnbB8CVf2HeEK1XUUxCCka8T229Bi0lEFuR-mZX_cmuv--16NzUu1Z7Ko82RkkXoO1Eluc4h6OkyjbzdnvYX4WciCU3CaGPL-Y297xUPt0Tb5paNdzFk38dXBgERiEQhgyudi0xQDcbMEJ_iWv2rrtRWpVwstqoShN7oGGGRRuJCDEwQNpwZaKqQf4cG0LzKdqfo_yk3mck2lECUHkscwLC3UWmWir-_kI7XUlOH9OCTD88w4RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f5c0f6a0.mp4?token=UszmxzbF8o-TZOUrZmq22Rq35tZlHSe7nkkSeuCbKC4vD2TUYM1P9F6E977Kggc2DYiYPDsiin-qjySBFI9m4khCUZrdO1GmnHYSnbB8CVf2HeEK1XUUxCCka8T229Bi0lEFuR-mZX_cmuv--16NzUu1Z7Ko82RkkXoO1Eluc4h6OkyjbzdnvYX4WciCU3CaGPL-Y297xUPt0Tb5paNdzFk38dXBgERiEQhgyudi0xQDcbMEJ_iWv2rrtRWpVwstqoShN7oGGGRRuJCDEwQNpwZaKqQf4cG0LzKdqfo_yk3mck2lECUHkscwLC3UWmWir-_kI7XUlOH9OCTD88w4RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرواز آزمایشی پادشاه اسپانیا فیلیپ و دخترش شاهزاده لیونور
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/661675" target="_blank">📅 11:12 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

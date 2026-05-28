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
<img src="https://cdn4.telesco.pe/file/hQhajDmEeCBbEXLyUHM3soVJujc3Cz53kC_00iEpsN7MCQ5TcLsBfhMnBYHOaTf_dFCC19baWL6__XCy8_DI656WBrfyN5A_5AVMXUkCPAxKsMVivrG-FuQATBKsoQYi-cXRKymO28m76YNKNMWT1mEVR2ra65FNvIT_IFVfZCyXakWWmSK0f8L0quXkBVzoko0FV5dgq7gnlnBmcXKu6Qj1z3glTd7NiLZ67sjM7NbCL7d0T17CSqgou6GPn4TwA8WxRPFLiKvwajUnE_8Qgt0fSzowrkv6R49ksAGJ80IbkBsC_fFU0DsMvvxo8Q-JMwSnZgU9UvNtUMnbT_UF_w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 123K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 14:16:28</div>
<hr>

<div class="tg-post" id="msg-90339">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18e2b0b1c0.mp4?token=TL5aL77GD2dozUAD3Pp-Q_TkUQSKKcZuaDdBbEG11Z_3CZ0RLaG8dlc_kCDOIcF2yNCRuIDUYlqaAWehCTktxi71LAH_jB9CIz88Y4XLpzdzw0vHM36Y7qkT1LQHAM7uYsWN07-wvGwE42V6SKhDJHT3K1EzrgofIbaxVG_sYEKlRZLxyt2OzVxKFV-JFcJnUr3UXKNEAqGlBsALYGR1Y2iqPwxNmihbHEi4-cA16bxIHu5sEMeHrYSeH-mrOoy315SjvnA3tix2pWcWu6Wklcvf5-HAnQsd17Q1MfoBqweTeTdHAXudCx6YYShgR_vrHa8mfAMQ3wr_i4iHSgwzPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18e2b0b1c0.mp4?token=TL5aL77GD2dozUAD3Pp-Q_TkUQSKKcZuaDdBbEG11Z_3CZ0RLaG8dlc_kCDOIcF2yNCRuIDUYlqaAWehCTktxi71LAH_jB9CIz88Y4XLpzdzw0vHM36Y7qkT1LQHAM7uYsWN07-wvGwE42V6SKhDJHT3K1EzrgofIbaxVG_sYEKlRZLxyt2OzVxKFV-JFcJnUr3UXKNEAqGlBsALYGR1Y2iqPwxNmihbHEi4-cA16bxIHu5sEMeHrYSeH-mrOoy315SjvnA3tix2pWcWu6Wklcvf5-HAnQsd17Q1MfoBqweTeTdHAXudCx6YYShgR_vrHa8mfAMQ3wr_i4iHSgwzPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پيش بينى فرزاد آشوبى از عملكرد تيم ملى ايران
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/Futball180TV/90339" target="_blank">📅 13:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90338">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFyxN4Y3aGoJYAG0ITXVGRjItb97GXNAURJpOX52zI6qXXWiPO-jRQzrKref1IS4HtQ-q4Eyzv8NBF6ABSKbEaxQi-ALHsz8XwtVZfPuDvlVtrDlrD14ODyXzOTHXcLrB5smw6fwFZsjDxLUPXpAhFTpMx_yeS7VWnRxyDGUGnjQIqMBVMYWr582TRiYmu6A_Q_hj-14sWZLsTwouaCp_68p2FJxesIlP7GCG0E8lJ_SlvVkH4B5qZkboO8segrllMtEz6YxVeK1N7ffzdUIe406ZLiKsI4u53YX0PhWuSv-tUp7Bevp9qVrCIvxMD21QF5wsT40ze8LFgyrmkAJww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ۱۱ ژوئیه، ممکن است شاهد پرتماشاگرترین بازی در تاریخ جهانی باشیم.
🌍
اگر هر دو تیم آرژانتین و پرتغال صدرنشین گروه‌های خود شوند و تا مراحل پایانی ادامه دهند، طرفداران شاهد رویارویی نهایی بین کریستیانو رونالدو و لیونل مسی در مرحله یک‌چهارم نهایی جام جهانی خواهند بود.
🤯
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/Futball180TV/90338" target="_blank">📅 13:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90337">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkq23cUzjqdR9w6Eir9XLOiCsfZeHQnjFZPmC4KlxqyUIP9Ig8x_ET63QuEVtau4x1P61tFhjIaXbKEmAyQyiG8zqEA9NgY69Uxobvk7jwhP5jMhp0kA6pdg-wH9piugNtKOo1kd3za3Q66l49YfwHukCRMnJWhaQWOihY-f1hppQ7Mg84kNSZTh1uhLVTkXEAR8Y33_xf6i5MN5kOXMYFGYWH5GBMnRuFGKmBAdtp--nQgWdR9w0d0xP9AVjQ89q7kWrVE9cjw9GQgsDni87C5QnKkcm8ZJ5XOacHUhMfP2_zFDBA9JLwrpqRwWV27SpAcp8cmXI4X_KEvrU4nO6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماره ده‌های تاریخ تیم‌ملی برزیل در جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/Futball180TV/90337" target="_blank">📅 13:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90336">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31f588b63d.mp4?token=gdNwZFMgf8Rg1TRTTMKuHXe-sKnWK-IBahAHZxf1YQ6g318S_bfs31jKskMpls3tuqZtfFRziZeHBphK0VKxfQkkrtafaTZBdUBvLWmrHRcRa5wJn8H_sC2uJlTdK0HPsbtK-EZtLglJk5CxHnEJ7E8nPHLTNEMx4Z2WrPBK8ZuB-UfjJcp55zwYmWyGf52zMYKMEHeXCs6-rsILaUqJZ7eB6lAJ7PnhpNlWf1Ye4DJ6Q3D6Va3w-5bVnsNqmiCJBXA26yRPOVhAUpfvfjo5TRcG32EnfjSuonWjdp-keX56_9bD11BrI4ERlM5H0ciszks3OlTihzgkBNJdzIHa9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31f588b63d.mp4?token=gdNwZFMgf8Rg1TRTTMKuHXe-sKnWK-IBahAHZxf1YQ6g318S_bfs31jKskMpls3tuqZtfFRziZeHBphK0VKxfQkkrtafaTZBdUBvLWmrHRcRa5wJn8H_sC2uJlTdK0HPsbtK-EZtLglJk5CxHnEJ7E8nPHLTNEMx4Z2WrPBK8ZuB-UfjJcp55zwYmWyGf52zMYKMEHeXCs6-rsILaUqJZ7eB6lAJ7PnhpNlWf1Ye4DJ6Q3D6Va3w-5bVnsNqmiCJBXA26yRPOVhAUpfvfjo5TRcG32EnfjSuonWjdp-keX56_9bD11BrI4ERlM5H0ciszks3OlTihzgkBNJdzIHa9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکیب منتخب سهراب برای حضور در جام جهانی
👀
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/Futball180TV/90336" target="_blank">📅 13:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90334">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اولین پیشنهاد بارسلونا برای جذب آلوارز رقم ۹۰ میلیون یورو به علاوه آپشن‌ها خواهد بود. لاپورتا قصد داره قبل جام‌جهانی این بازیکن رو جذب کنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/Futball180TV/90334" target="_blank">📅 13:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90333">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فوری از فابریزیو رومانو :  بارسلونا در حال آماده‌سازی اولین پیشنهاد رسمی برای خولیان آلوارز است که به زودی ارسال خواهد شد؛ هیچ بازیکنی در آن گنجانده نشده است.  خولیان پس از رد قرارداد جدید ماه‌ها پیش، به اتلتیکو اطلاع داد که تمایل به ترک این تیم دارد.…</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/90333" target="_blank">📅 13:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90332">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqrSVKr5CWjynmOFt7cgyKTaPYREaS9XI57grwShCWyeRKiC6cYUQCL8o3P_slgw-n4c5-yCiS1ONi7EPRGFHrQ3fQAgflS-XFDGhm-r0SgLG7qfgrw1eyzkFx9S3XdUYB5uhkzuQbOzqTOcOoKzy8wj0fJdM6MBhntC7D7bVPRyLAeTx76EG_rFf2aTYMgof8aN5wOWWJNfmtIjgmnsI1QOBj5Z-gt2mZIFsX2NvvVBKOrIzOXEyw2XMxE6lW5NAKZGrtNhJ46uUUL3LkvEhH4vxPYzrSyn0y9AQQjMExhsWFX2XzZIL-oUJ2DyK5YWyX12b6DUC6Yu9IWQ2MEm_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فوری
از فابریزیو رومانو :
بارسلونا در حال آماده‌سازی اولین پیشنهاد رسمی برای خولیان آلوارز است که به زودی ارسال خواهد شد؛ هیچ بازیکنی در آن گنجانده نشده است.
خولیان پس از رد قرارداد جدید ماه‌ها پیش، به اتلتیکو اطلاع داد که تمایل به ترک این تیم دارد.
پس از ملاقات مستقیم با مدیربرنامه‌ها و واسطه‌ها، بارسا پیشنهادی ارسال خواهد کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/Futball180TV/90332" target="_blank">📅 12:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90331">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/858ae0e82d.mp4?token=pM21OkO-wqPlGyoKl276A-B7A9EOgpoqOM7SCOZ_3ZzO2wexyxm4BzQhITQ0c-cL6Ofw8o2q-qhghvUbdo0CHqtE127pTNCBz6z9ZBkhrtGqe4Ktf-CwMlXGzdmqJT07TtMv5gP76ODgOzulU8yRNVK0XfaNyX3Rspy9UhfYP0i3AX7FXg16uV35uXOULaTJjMGjA9rPzhBRpuGPeJNU7DmTiwNrRiw0zpPm0HTpAnIjIet0aBnNrX1xdBVkKdur3-X56CEtPGnO1_GYHx0I5-VjzDp35BL4xH4Kac3rc5KAp0SK44ZHpVSZv7F63PnNHpP0hkOH8XkUDHxz0vldaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/858ae0e82d.mp4?token=pM21OkO-wqPlGyoKl276A-B7A9EOgpoqOM7SCOZ_3ZzO2wexyxm4BzQhITQ0c-cL6Ofw8o2q-qhghvUbdo0CHqtE127pTNCBz6z9ZBkhrtGqe4Ktf-CwMlXGzdmqJT07TtMv5gP76ODgOzulU8yRNVK0XfaNyX3Rspy9UhfYP0i3AX7FXg16uV35uXOULaTJjMGjA9rPzhBRpuGPeJNU7DmTiwNrRiw0zpPm0HTpAnIjIet0aBnNrX1xdBVkKdur3-X56CEtPGnO1_GYHx0I5-VjzDp35BL4xH4Kac3rc5KAp0SK44ZHpVSZv7F63PnNHpP0hkOH8XkUDHxz0vldaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینترنت بین الملل وصل شد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/Futball180TV/90331" target="_blank">📅 12:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90330">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👍
👍
#اختصاصی #وینرو :
✅
ثبت نام کن
🤩
🤩
🤩
هزارتومان شارژ بی قیدوشرط بگیر!
💵
💬
به مدت محدود
📣
😮
تنها سایتی که با عضویت بدون  واریز 500,000 تومان شارژ بی قیدو شرط میده #وینرو هست
💰
👑
#معتبرترین سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال اخبار و هدایا r7…</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/Futball180TV/90330" target="_blank">📅 12:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90329">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdDXXFMpB3twd6F9qcISJUgV2YOkIIh90sy9CyG9vehkL0n4GKYU0VwLCZBuR_EKjEOX9S_1xSgXEDRRudUxfXNuII6WzxQN7tWNSbVaulXf9grVf-05CmJFHCpZCOG5KPx6ajCkr5B6-1hCEkqgVcOfjpPEVz5YuXlR1AGMWEppWQZrvl1FHi76CpQszRnTsLWEaMqUhuMgYBSP9kqvVOlJrj60Kfvnm8A2pBNyfHWnF_n3JWyyc_NvxKl_WJA_AnsvFVFYzMcpA-8CNY9s-Kah26AWqYz89I0UsMZx363YaE5ut2BW5rkOgvt58nWdAqI3pDoM2Hgxz100rflP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
👍
#اختصاصی
#وینرو
:
✅
ثبت نام کن
🤩
🤩
🤩
هزارتومان شارژ بی قیدوشرط بگیر!
💵
💬
به مدت محدود
📣
😮
تنها سایتی که با عضویت بدو
ن
واریز
500,000 تومان شارژ
بی قیدو شرط
میده
#وینرو
هست
💰
👑
#معتبرترین
سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال اخبار و هدایا r7
🎁
📱
@winro_io</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/Futball180TV/90329" target="_blank">📅 12:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90328">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97ac0d5890.mp4?token=YTYJrEv7cZNJG5VcnnumcRcbB12Zs1GuK8jbAmLnDSVMMYolpJ49wd0HhhdJTKEbjMEG85ySkHdTJaNIy401ZQP1vkameL5nM1keFFwUZI7zwyN-7p8_cDF4ZyeAXfonb5Mm0PV0G7078s1N4JjPSbMjxSN_jvoffszzR7nUqT4_hp73wHAZ6rqumbbwNiMYI9mmfKmg_DgSPjTkc41FeV2d8P4yXYoFP8uz8FGled8yXiWBySEnYFSlwc9SvbfdLQYWUKFGeN4iuosAHW__KU3bpfENCJMs9QX63jYA1L1LvHAY99Nc2aaVoQku1sEfqrWzk8NmtfOzSBNJh3ft3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97ac0d5890.mp4?token=YTYJrEv7cZNJG5VcnnumcRcbB12Zs1GuK8jbAmLnDSVMMYolpJ49wd0HhhdJTKEbjMEG85ySkHdTJaNIy401ZQP1vkameL5nM1keFFwUZI7zwyN-7p8_cDF4ZyeAXfonb5Mm0PV0G7078s1N4JjPSbMjxSN_jvoffszzR7nUqT4_hp73wHAZ6rqumbbwNiMYI9mmfKmg_DgSPjTkc41FeV2d8P4yXYoFP8uz8FGled8yXiWBySEnYFSlwc9SvbfdLQYWUKFGeN4iuosAHW__KU3bpfENCJMs9QX63jYA1L1LvHAY99Nc2aaVoQku1sEfqrWzk8NmtfOzSBNJh3ft3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازگشت لامین‌یامال به تمرینات اسپانیا برای حضور در جام‌جهانی فوتبال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/Futball180TV/90328" target="_blank">📅 12:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90327">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJhSaAb7ziiEHhfw2_YdMHkHG1bFR56vECrch6UGYrKX2oNeAjmy3MhHVU1_pwPjcjSS583NO3APUpHnWR3D6R5vE3lIDbHKDOt4G468iGkvHvqQZ5cwrLOa9-R5yUZY7a49iqacY76UOP-s7GwNHbItlLdDNT0isZcqN6s61joFemtBWKsdlV0eyM1dEE3Wibq3ExfdDdOUtxKkwnxioomPOlpncU_-wYCGuJhtP0Lp4ns_Vg6502UN19HdwFlcBDKs6AEYe4d_W9TPnb24Q8hJsmKyK-ePbC3U_1kafOWmCJ70nvercz_cUKACV9YGUkI_gPPDIsPixkm3s1AVbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیشترین حضور توی سطح اول فوتبال انگلیس
آرسنال تنها تیم بدون سقوط
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/Futball180TV/90327" target="_blank">📅 11:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90326">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e24e703cf.mp4?token=WZ0s0fTzoO7gFKD1eLIlI_XFxN4VyLWs5wpyZEEd3H869l2-dveo_NV5YXMny6J17DiPP_amCKIsxZ-VgnlPZfYSgrvQlx4fQ_4HztsKhZi8nZgy-Q1Joh5YSFCaubHzFJswbsBW6TbefcCjnR6znlUgVluWYkTuVYP0_40VmzjqZChi-kOM6tdB60J8bHK-N7ZrZmdj1HMPyUOBpglpPgPZxvoSGKf6jcawAho4pDJnmGMbwv1sp7UIZmpwEEsTQJCvFN83AvdX9fI-m_xQTDlXNMt76kfgG55Bai1gUyh5wE3MrYMroG_k0oiAV0oP_qn9KBeoZ-KcyB-2NiTMyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e24e703cf.mp4?token=WZ0s0fTzoO7gFKD1eLIlI_XFxN4VyLWs5wpyZEEd3H869l2-dveo_NV5YXMny6J17DiPP_amCKIsxZ-VgnlPZfYSgrvQlx4fQ_4HztsKhZi8nZgy-Q1Joh5YSFCaubHzFJswbsBW6TbefcCjnR6znlUgVluWYkTuVYP0_40VmzjqZChi-kOM6tdB60J8bHK-N7ZrZmdj1HMPyUOBpglpPgPZxvoSGKf6jcawAho4pDJnmGMbwv1sp7UIZmpwEEsTQJCvFN83AvdX9fI-m_xQTDlXNMt76kfgG55Bai1gUyh5wE3MrYMroG_k0oiAV0oP_qn9KBeoZ-KcyB-2NiTMyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«تازه خارجیش رو بهتر بلده ..»
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/Futball180TV/90326" target="_blank">📅 11:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90325">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔷
#اختصاصی_فوتبال‌180
؛ مونیرالحدادی و یاسر‌آسانی دو ستاره خارجی استقلال برای ادامه حضور در آبی‌پوشان خواستار افزایش دستمزد و پرداخت به موقع حقوق خود شده‌اند. سیاست مدیریت فعلی استقلال بر حفظ این دو بازیکن است زیرا پیدا کردن نفرات جایگزین در شرایط بسته‌بودن پنجره نقل‌وانتقالات عملا سخت و غیرممکن است. قرار است پس از جام‌جهانی و مشخص شدن تکلیف لیگ‌برتر، جلسات ویژه‌ای با نمایندگان این دوبازیکن برای ادامه حضور در جمع آبی‌پوشان برگزار شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/Futball180TV/90325" target="_blank">📅 11:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90324">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxaaxEk3p82le40iFMOx9ISLAUyMl5khaYWR5icNZ2adCSOCJDFNwMYF1CF89BDK-eN54cEDNDxc12atVzwuf7eHNxAR2th3ZIM4YEIMHVhSF49sp-op_nDeOOK4XfgfFqgj8DdILMiUM2LamwYsekRYBuyC-AomjAQJr32Ilo6RkL20D1TKszXCPV-kmDJB9nGVRMRoy5g4H9R6eWXoFUI2jcPgxt43XuYh5YRdkV-xl9RgPo5ku-94XWPQbqcYF3tulxN4tso4YeEdgdr9pKLV7Myev9P_dJidd1dcKPxdZhf3hipGAUesA6Lc4JPK7yhrAudleYWwZUQkajMqiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شب‌گذشته دیدار مهمی بین سران باشگاه بارسلونا و وکلای خولیان آلوارز برگزار شده است. این بازیکن شدیدا خواهان خروج از اتلتیکومادرید و پیوستن به بارسلونا است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/Futball180TV/90324" target="_blank">📅 11:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90323">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNnM7zZpL-vXBHwMB8jHMbKgKJUtm7fS-s9S5tCYys95-Q9SAXisnaO-b12mcsxMtJDdTM-f-wzBjBw0NX88s7tIbYPlmbYM0XiVw9elRtyE3APKXLuS0KG3aaQUqNVduWLRujzQ6b5O9Ajj8VxOrfq3DV3rwZ4ljLv34rcSqriy0zlt94AxW4jUwcnZHEb7L7h0G72Sq52RluD5K0Nb1bJXoT_7ZOT_hPg4c5lurowLO4yMplnJlb_mls3MX7tYLZM-s0e7Cxuk1HsH1nXkIp9MZ7cSbzKkljwB1hWg-autxDlN98-3qG3rSc6cBUdRWHe5n4kcC3J20eZXqubRlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین گلزنان تاریخ‌فوتبال برزیل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/Futball180TV/90323" target="_blank">📅 11:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90322">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f4a1291c.mp4?token=t37iWqIwhsBtLPoNznfCpx0n1uu39gqDuQbAilsNzSpO0yCg0Naf-Y31r55629mtd75KqdX5DJjDVB5KVKr3l9aoSfPh3-EoDIRzOWQFLgKa0JUWDAY6VZWFlawjTBja6zy8weN53kF8c9o6NS2ATT750z2Y_0jwhFGCuT_wO3F8FuWjTRK0C-aKNeYS9xqjszWhmODDurYhSbkLkf3aUraSEoYlGgMLM8JGHaJd-wZ9laE0ZhuiKNPp7AvlbnInD6Wq7Jh7Bt6xoprJbW05iUxHoDto1dSHMNlH8R2yi7SPuaOi7H3Q_rN4MWs0-6T3_8qEuxSyEMQ51a2_ERVuRS-NftlkCPQKqs0adIH9-R6nx5D5aT4zkCqnFneKBqJuWcTx9LBbtUEYRBZynIBc5hnvkC_aohF4gmPumZQgQRkPH4sOfVCJ7CF_rt9EUacoSwmDJrr6o6754l5CvhgVhdIAk62eS9JhDqp2_7_uokymxOoATy8I6l5OwrlCdrH218Gd69Ha7k_Yj6ZnoNojbj_YQquBhTUktA3Z7pcqTaeCU5mdPDZJqjPC9XcY2TfjhtzG3Lz5NMwGkW8KmeYPa3KqrW45kyK38m87JKEBG8k-8yfJ9fjaw-WzjBMyD2HgJq3veI5bfFJuqKc-Ocq3AlYBUb4FbVBIsCJRLNLntQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f4a1291c.mp4?token=t37iWqIwhsBtLPoNznfCpx0n1uu39gqDuQbAilsNzSpO0yCg0Naf-Y31r55629mtd75KqdX5DJjDVB5KVKr3l9aoSfPh3-EoDIRzOWQFLgKa0JUWDAY6VZWFlawjTBja6zy8weN53kF8c9o6NS2ATT750z2Y_0jwhFGCuT_wO3F8FuWjTRK0C-aKNeYS9xqjszWhmODDurYhSbkLkf3aUraSEoYlGgMLM8JGHaJd-wZ9laE0ZhuiKNPp7AvlbnInD6Wq7Jh7Bt6xoprJbW05iUxHoDto1dSHMNlH8R2yi7SPuaOi7H3Q_rN4MWs0-6T3_8qEuxSyEMQ51a2_ERVuRS-NftlkCPQKqs0adIH9-R6nx5D5aT4zkCqnFneKBqJuWcTx9LBbtUEYRBZynIBc5hnvkC_aohF4gmPumZQgQRkPH4sOfVCJ7CF_rt9EUacoSwmDJrr6o6754l5CvhgVhdIAk62eS9JhDqp2_7_uokymxOoATy8I6l5OwrlCdrH218Gd69Ha7k_Yj6ZnoNojbj_YQquBhTUktA3Z7pcqTaeCU5mdPDZJqjPC9XcY2TfjhtzG3Lz5NMwGkW8KmeYPa3KqrW45kyK38m87JKEBG8k-8yfJ9fjaw-WzjBMyD2HgJq3veI5bfFJuqKc-Ocq3AlYBUb4FbVBIsCJRLNLntQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از عجیب‌ترین وقت‌کشی‌های تاریخ
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/Futball180TV/90322" target="_blank">📅 10:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90321">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txN6JiZEyrhxUdR3jplFCLHxGpwDWsqkWyB4xJrVO1o9RjgFpgDR8KVjJhf_C9WA7jxgyzoh9_cS-j0tFo-jJD21XYyw-ivZa1YsY8FeWwWsvOizWjKo3QyytYt_eyf94tARuFDP0Kc9ENK037VamdXuZKMGJ7xNhSpSIQg0QY02CsRmFg7eY5GMvcsJ4y5ZAWdq4_wTsla3_1A0oPEqwAlykibmAhaqjlMGYOEykocuqyXeew6oqzgKGQesOz47bMhwhewlukIbvLylqaE969RvgAA7bCVZdW6H_xlc1QOqST7AsvWse3LAxoi-WWZcaEtgeeRymYW-z3dUrk-KnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فیلیپه‌لوئیز سرمربی جوان برزیلی هدایت تیم فوتبال موناکو را برعهده گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/Futball180TV/90321" target="_blank">📅 10:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90320">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njm0193h0GBAWTL_w-wMhf8VeXspC7k4EqIxWnAiSlsju-h5mK_0ti8jAy5zFOnR_2ezGbAV0drrit16X-qXc6TrVpUeAKlZmx5hEcke2d0k3xESTm4-BY6VkogffYvxxpMCThQNL6IooYSNZGQNPlya0xmDg_dF28_cr102aqaVzpZYq5MUx7L5PEXHTVd6fxBhS7lHJTmXfSStcVv5aV4GkUMRLvJHyTU7UhQz3POOc6qTghf74BNeWZnejbR5Bu8gLHK4WxPCyuzKD1Jq3FORJDVhLO8jV2B0iHJp1iMMt980TBGdL74VSKmvEhjGcAPw6SiQ1txL3euUapdeOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانسرهای پیراهن تیم‌های حاضر در جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/Futball180TV/90320" target="_blank">📅 10:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90319">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49f9845215.mp4?token=Higc6-I9oXt4iG-YOSWS2k777yB9yfoUG3sIZ5w8nQdhqkUZsVrkBuisx1RvMI5XHj68YmzJQw3FoX_7FtFyk5D855A7HLbqYqmuYZx1MrwX8Em2mQ3qAJ17wtNDrFm3JtJGPpFWnMlXmKjg_58KECg36krKmLD6kX5b2xOwzpRBof_N_w78fZld36TlT9n2EYBOV5O8iaiBHAEZoSHbNa9k4Wc0MD7grQOnVsfvmF5_TM8fw_rBoHyjRliU-K1QRqz-Gic1HsPnyG9Ckv7eQlVBXluls0b-p2sTgGXqSquj37c33yHYpf79YHOfXbeaFYpNrXLa76yZzLLkj17MKXlt71BvPbsGPPRsboiCnoHHWcUGsEAxl8VC76wOCeWJdbdy-hVSrhM920QGSbkFrKahw4HSp5SarsFb2y8pAP2-Not0icf4QkSLqp-UBPyOlI0mqguCMoraLCytULpeiShj5OOnbA5QQAZUb_1d3k9Ff1qBJrS9jbL_yp0dFGPTQ8O3XqvBW7wRzh5PVwpN3n0nkjL7qtKmp6JHf3W1CZ2nTs30_1lMIzO7f0Osqu2OaK9erZHGV9m-O2D1Z2FcWTgtl074xFwplaHe_uxiDKAnEk6I7Y6RuPDBkTT7VUOt8aA9EDwYBQ1qoN6yMGFK-n1mAUfeKQQ61jFlGZ8CdZY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49f9845215.mp4?token=Higc6-I9oXt4iG-YOSWS2k777yB9yfoUG3sIZ5w8nQdhqkUZsVrkBuisx1RvMI5XHj68YmzJQw3FoX_7FtFyk5D855A7HLbqYqmuYZx1MrwX8Em2mQ3qAJ17wtNDrFm3JtJGPpFWnMlXmKjg_58KECg36krKmLD6kX5b2xOwzpRBof_N_w78fZld36TlT9n2EYBOV5O8iaiBHAEZoSHbNa9k4Wc0MD7grQOnVsfvmF5_TM8fw_rBoHyjRliU-K1QRqz-Gic1HsPnyG9Ckv7eQlVBXluls0b-p2sTgGXqSquj37c33yHYpf79YHOfXbeaFYpNrXLa76yZzLLkj17MKXlt71BvPbsGPPRsboiCnoHHWcUGsEAxl8VC76wOCeWJdbdy-hVSrhM920QGSbkFrKahw4HSp5SarsFb2y8pAP2-Not0icf4QkSLqp-UBPyOlI0mqguCMoraLCytULpeiShj5OOnbA5QQAZUb_1d3k9Ff1qBJrS9jbL_yp0dFGPTQ8O3XqvBW7wRzh5PVwpN3n0nkjL7qtKmp6JHf3W1CZ2nTs30_1lMIzO7f0Osqu2OaK9erZHGV9m-O2D1Z2FcWTgtl074xFwplaHe_uxiDKAnEk6I7Y6RuPDBkTT7VUOt8aA9EDwYBQ1qoN6yMGFK-n1mAUfeKQQ61jFlGZ8CdZY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برزیل و هواداران جذابش در جام‌جهانی
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/Futball180TV/90319" target="_blank">📅 09:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90318">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-tzbO_IFHf8u1dVRjHKjudaQuxOU2a-H13RtimPxThje6QPN3XX7Azeg2FeBemdtwutdqDFiqcEBkDTMJd2o2sVQNDWwxLlIxk7lFRztXDsrgmXI_51KlYVR2YsA2YHg4xv3tIw-bIZLekUYC4Z8xjsqSZBU4vbiqa-15KSjl6yBQvmbbwlju8GHYUAjUz-fJedPe9h1bAG7QDWlKkbnEUlqulqjFLj0QF22Hfo9o7-jO5722a_sab-j-z0wJUM17y8ynArmEwQCWFqPJnLnF-OCBv01c4hIoYmFA12TgZyuGaoZuxxxM_Kb-8dWhqf0n1lgya-cimOGHfDmL6SSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرافتخارترین تیم‌های ملی تاریخ فوتبال جهان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/Futball180TV/90318" target="_blank">📅 09:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90317">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e84afd40a9.mp4?token=GY0lauXs2WMFWTnrDGtuU1OPEjBhASnx1ibgDVNQbuX2wij32q7B8lpcbqJRmyyKYb0cVAICA7oDO0g1LK6tnl9orAoHevKFk3R1BHCxZPFcCVgc0MY0WVIpbwRuJtMfh8A0MqW6NqRLJfSnvME_Jc_eVesbStEaliQzx7IxYm1LhxuQBJEtKp1CX0Fuz_3ubwD8OFRdqtWGhW4RYYUGiIX3ePjIZ39kl1KVmIBtR0Oen4_WOMS30AhrkZ9x7n4Y-IcSVfFgtXww00Dr621dyM8aadsCVweuMJLATCWHqr50dXeMFL8xDLcMUJ5y3GCjjRGHryeNyPATYjIK-mPDDj7nd05y64eqSQK4_RxY549vRF1dTxN-j_uXyTSMWroRBcH3Aew_qcso4UTIZcRZXIDvcnP_Wzu1KA2NFX3jE43WTBmUHyivzibEQJDX-0-HMY9P5UTbUs51aUJ_tHw9jrENPDwbFT4c3fZJOj01XbhXikNMagUc907F47pHJF0WubuuEYJh_Qbp7wqNB90eAarlyx_ohgiw6dPOAW-NQV8XNGoq4QuJyIiHMY68xoukRKGLnhyxNV5elE_2fOX7j7QoSkRVIteGmHCDkTHbNsGgKc52B5Jj5jX5wEwDz5Yh_U_xWz5XsSrcW-htm86a3Ivh8I3dLJspj9k0ppe9blo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e84afd40a9.mp4?token=GY0lauXs2WMFWTnrDGtuU1OPEjBhASnx1ibgDVNQbuX2wij32q7B8lpcbqJRmyyKYb0cVAICA7oDO0g1LK6tnl9orAoHevKFk3R1BHCxZPFcCVgc0MY0WVIpbwRuJtMfh8A0MqW6NqRLJfSnvME_Jc_eVesbStEaliQzx7IxYm1LhxuQBJEtKp1CX0Fuz_3ubwD8OFRdqtWGhW4RYYUGiIX3ePjIZ39kl1KVmIBtR0Oen4_WOMS30AhrkZ9x7n4Y-IcSVfFgtXww00Dr621dyM8aadsCVweuMJLATCWHqr50dXeMFL8xDLcMUJ5y3GCjjRGHryeNyPATYjIK-mPDDj7nd05y64eqSQK4_RxY549vRF1dTxN-j_uXyTSMWroRBcH3Aew_qcso4UTIZcRZXIDvcnP_Wzu1KA2NFX3jE43WTBmUHyivzibEQJDX-0-HMY9P5UTbUs51aUJ_tHw9jrENPDwbFT4c3fZJOj01XbhXikNMagUc907F47pHJF0WubuuEYJh_Qbp7wqNB90eAarlyx_ohgiw6dPOAW-NQV8XNGoq4QuJyIiHMY68xoukRKGLnhyxNV5elE_2fOX7j7QoSkRVIteGmHCDkTHbNsGgKc52B5Jj5jX5wEwDz5Yh_U_xWz5XsSrcW-htm86a3Ivh8I3dLJspj9k0ppe9blo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از جذاب‌ترین هواداران کشورهای حاضر در جام‌جهانی بدون شک کلمبیا هستن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/Futball180TV/90317" target="_blank">📅 08:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90316">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c6e129bd0.mp4?token=qjEb2kOkszOTTtktXJ_fsv8dbVjrXeI59r8U_eUbkJYIEsHzHwCQ27kA_03bpEkbQcyupBLlw2275oFlZf_uGwxEq3ZGmnkCxiPNpG4hyyl5iSInMFM5IuDg9TRUe2iJN862olIAQN3WTqi2q-lo1HIKsiBMwAeifHC6ddN-K33Mb2Q1JhS8PUd1BhC-4Y8gvJt_KUeBqJ0L8goZCll0JhDolD3ZW4a43vmrsMCIRMK5eoV6wzLcAIr-ex_iS5yiOGkKNi9ySuPFA58654NWHV6GRPCQuHbX8TE7uz0RqpfCYZDp9dKXlLcPnbibqF9ILCU5gQaPpUJkBYLfASdKPgfzDkBDorv0emIKEMFqu_Azgl01XcVj0cyfLNGvjOWauZZLpLsMyP1Z3R14SkMMf3Kd82fjF1tsAxnbuJpLu5Dp5KKroJv2fgfxoNAZXJi6QPOtqQePExWK0yKyH4bW_8nvSfURNIUnmZR1-0c1KXjLBLWaPt1SEZgx5l8AulZMx2vB28p1MbWnyTELH0l7xHzi_RZD43Jwj3h5FTEVfFAusAQJmCCp_roPhzmAiTahkXcfkbeQECFI7QglV4B31JMqhW2WxN9rK-R8j-PwM9SxVw5upsVZpfW3dY-MPMHW7lS04Xx0c2GS1ZVQZyxj1n7PDQgkMCKpMOQt7JhtN2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c6e129bd0.mp4?token=qjEb2kOkszOTTtktXJ_fsv8dbVjrXeI59r8U_eUbkJYIEsHzHwCQ27kA_03bpEkbQcyupBLlw2275oFlZf_uGwxEq3ZGmnkCxiPNpG4hyyl5iSInMFM5IuDg9TRUe2iJN862olIAQN3WTqi2q-lo1HIKsiBMwAeifHC6ddN-K33Mb2Q1JhS8PUd1BhC-4Y8gvJt_KUeBqJ0L8goZCll0JhDolD3ZW4a43vmrsMCIRMK5eoV6wzLcAIr-ex_iS5yiOGkKNi9ySuPFA58654NWHV6GRPCQuHbX8TE7uz0RqpfCYZDp9dKXlLcPnbibqF9ILCU5gQaPpUJkBYLfASdKPgfzDkBDorv0emIKEMFqu_Azgl01XcVj0cyfLNGvjOWauZZLpLsMyP1Z3R14SkMMf3Kd82fjF1tsAxnbuJpLu5Dp5KKroJv2fgfxoNAZXJi6QPOtqQePExWK0yKyH4bW_8nvSfURNIUnmZR1-0c1KXjLBLWaPt1SEZgx5l8AulZMx2vB28p1MbWnyTELH0l7xHzi_RZD43Jwj3h5FTEVfFAusAQJmCCp_roPhzmAiTahkXcfkbeQECFI7QglV4B31JMqhW2WxN9rK-R8j-PwM9SxVw5upsVZpfW3dY-MPMHW7lS04Xx0c2GS1ZVQZyxj1n7PDQgkMCKpMOQt7JhtN2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی لطیفی پیشکسوت فوتبال: کی روش شارلاتان بود، پول می گرفت و بازیکن دعوت می کرد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/Futball180TV/90316" target="_blank">📅 08:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90315">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🎯
شانستو #رایگان امتحان کن
⚠️
🤔
میدونستی توی #وینرو میتونی  رایگان شرط ببندی؟
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
Winro.io…</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/Futball180TV/90315" target="_blank">📅 01:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90313">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFBGWfbsmH2X--9Tf6XXoZFCJ2ixvTQ_ez9TxGmZV_ifilpwNOwcqD6ULGJsdWZk9-_taUXpPGl5_PcMYyHrYfulQUmlKz8dox8JtCsiND6lCRSX6cDPy5b3ExjwMBuE5y-tnnEdG_DU7-pdQjfHz1t9GE6p_5SGcHcqPSwraEw1BJxS1zEh52LQO_lOkCFF4CEwwqxF-RCa_XNazkx4qABedBQykNZJAdglIuRfbuMv0bE0ggdXZXx4gEvsZiSbbCu-iwtq8H6myq4RPSQKZaaEQzHQGCL70DIidr1ODFeIyBKxclEWbmBUNpduMzlCjukLR_q9ERUAMy3mSz8btQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
شانستو
#رایگان
امتحان کن
⚠️
🤔
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
a6
📱
@winro_io</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/Futball180TV/90313" target="_blank">📅 01:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90312">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRzMJReUmk8hwMRfWCy8xSvYXoZ6KaSGxdiQwN5cRaAKq4Sqvt9jZPk_n1atP-ncz7s_ScO6Xvp8atB14bZ8GgmDkpUCieR5ZEZs_TI0hwqO8JtI1imWZ-Ur3j45Iub9Oj1ypEbrOymUaTvfjoNboNNEOejz38pJqxgvnLe4uJiKwM79kAeyNkmzvDN8t9pWormPb4AQsgTQ2UskFFXii_efGyU5s47gOeeNEyGFJN_bA8AM7T_dddP9V4EdgiXdMRWuEVgaDsrCPrYG5mzUL0il5mE_KO8W63Sva12upOexZ9GZxwrcldJfr8V2Tt-6wYLabqE1L1pB9jBN53XWsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم‌فوتبال کریستال‌پالاس قهرمان لیگ‌کنفرانس شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/Futball180TV/90312" target="_blank">📅 01:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90311">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAc81RRyjuVoidZHMTmEXwJXhRd6SICxPzzINra_MBHHT58BQ-vC6kPoKGdyRtbD97LUSureFU2PGsxdlvjRFA8EggUQThW1JEj26nXRdAxqvDHrcfAVucATn8f9pwSenTZ6dqKBbpRsRrxEPc_1sPRyQXfbl_tB4n_ST_gS8G49GCnObt9vWwUiEtcZHhUFXutq1z7LaIsO9dQZLI8xZpUz-bhEDfEoQx066Vmf3u80qIWIPJMt5i2n6f3SJ7clqxirF4L2RN0il1vs3m5vtnVes62PUUCyFQ5DTeM_PsTHoqU0XkPVMiBussZSTKpD7-Rc2rImjf8iRb6hpjlxnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کافو تنها بازیکن تاریخ فوتبال است که توانسته سه دوره به فینال جام‌جهانی دست‌یابد. حالا لیونل‌مسی و امباپه این فرصت را دارند که در کنار کافو تاریخ‌ساز شوند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/Futball180TV/90311" target="_blank">📅 23:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90310">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
برخی اخبار کاربران گویا این است که سرویس گوگل‌پلی درحال‌حاضر رفع فیلتر شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90310" target="_blank">📅 23:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90309">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4BuwOmX5Q5hXdTzQJWh-J_RJgAf5JTQy7dw4YIepMpum9XXgOQw3HD0o67z5ILG-DzWoPYfrdBGbH0b8k8B9_u8U41zDh3qkTE4p_onJ5LoWlQVsTfqcg0uj8rITQC6oP1_1QWfo7c28dzx5GsHH66_HPyMDPHuQx_FWmmVZQwZd2ci6-IRvsI2M-AU_TmNhx_M1YbSvT9Htt8vBnWSA-xFUaof9Wc5bEhm_3dlctlM5lUuKFYb-vqp6Jw3rna2pO7gBNo2ER_xoE1q_mqCULdccTeIUqPeKxCPYchLAkw9_9mmI7gVzTNFCJsc-ez0Y3pBRCLMS0LXGvxVIQBv-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عملکرد تاریخی اسطوره فوتبال مردان و زنان بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90309" target="_blank">📅 23:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90308">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3evZK2281CBnBTeIzi5ZTiv3wdHSp5MH1pFnlFuLelmBDa1gjJvtt5IoMwpfsT-yp74Zd1ejUvmDG_mE6s_C7Gh_shh02lDwWur0W4vBH7yCcPjojVxqRygOxjBWTATMec8Ouhf78WTWW12yp6EEvPiupHR4Y0TQxnmUj7ohbm06P_zmxkX-JClgVzfkGfX-uGcM2l-ZPody6NGGmpFjfnCa-nyK9QtIq47QlyF8Z7HAeQuJLjb2XFuz4N6gpXRlCVpPadSa-O3UDWR1gFfcaixDR-e-fBRUFSbWUpV5Barnu3bZR3MosHP9LDRAyWgwL4gNfUA4U-6QZPxkTpxtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
گردونه شگفت‌انگیز جام جهانی
🏆
⏩
با پیش‌بینی رقابت‌های ورزشی و بازی‌های کازینویی، مراحل هفتگی «گردونه شگفت‌انگیز» ویژه جام جهانی را تکمیل کرده و هر هفته تا دو چرخش دریافت کنید.
اطلاعات بیش‌تر و قوانین:
🔗
bfrd.link/WCW
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/Futball180TV/90308" target="_blank">📅 23:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90307">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84204a485b.mp4?token=FNiHnsJ9tejIJH450uUiGl_vn409uzHytbHYk0qgqTjyX5jIO5QqmNVT5k-nQ2VK7dedbh0skW7xB9bcu2QB73QsRJC9hnb5ZLxgMusDjMsZP3gSKnJsMdvqOnbtGyjgTuoZwZTA53sGOO3DmpATbU98Pg-tkJM4UE4EzJENJN-rg-3TDZ-wvRvYfYuGNFxwErXbStcGTVfBwGbrpvFV3WPdZrfW0AmAyiud-Ma4qpnJHMlBo-wzhuTA2GD0fHUZvEmomT6Uy6D2i2thpyPW1C5o1GSq1w64z0Dvk39CztF4_RpDe8NpnDPb01JVGTh-Ayl2sM7XtZpntjpsz-KdDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84204a485b.mp4?token=FNiHnsJ9tejIJH450uUiGl_vn409uzHytbHYk0qgqTjyX5jIO5QqmNVT5k-nQ2VK7dedbh0skW7xB9bcu2QB73QsRJC9hnb5ZLxgMusDjMsZP3gSKnJsMdvqOnbtGyjgTuoZwZTA53sGOO3DmpATbU98Pg-tkJM4UE4EzJENJN-rg-3TDZ-wvRvYfYuGNFxwErXbStcGTVfBwGbrpvFV3WPdZrfW0AmAyiud-Ma4qpnJHMlBo-wzhuTA2GD0fHUZvEmomT6Uy6D2i2thpyPW1C5o1GSq1w64z0Dvk39CztF4_RpDe8NpnDPb01JVGTh-Ayl2sM7XtZpntjpsz-KdDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر قلعه‌نویی به سبک لوئیز انریکه درحال هدایت شاگردانش برای جام‌جهانی فوتبال!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/Futball180TV/90307" target="_blank">📅 23:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90306">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fa7TUkEfvWd3apo-jfpcfv5fovppJLiM8nRVN8bJW5JGowgQHYCHeAP8JfP4UOWqAFGE-EZa9RB-45SOUGnbTZjI1SA0qWUwhT7VnD9SQ2JovCoc7BBV46N7nFEEVguFx0h_cFet_wh_g2Qmdv605plb6aBnJsVDJKSZH0Q7rz9OAdzuxTxnxpkrues-OwdALcR7gqmnnjEqGB849543FRvUtqsI7zQGmsYm6EUfx2_qnv0qw8au7i_h37ehUIcngLBADc6A3LloJhiPfCPtxcA_n8NG3Po_UmS3PO_TtzxZimocEw8RU8wVMskPyxuZWitCjAuMA87YwwGFi34A3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندی رابرتسون ستاره خط‌دفاعی لیورپول با عقد قراردادی به عنوان بازیکن آزاد به تاتنهام پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/Futball180TV/90306" target="_blank">📅 22:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90305">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80080a6ded.mp4?token=hEuIBkcw_KhUmWPz7qRaLsyXfrT5OEsUdGRu54Yjr0b7rMu2x90GrPHAiIY4TFfdx5ELdsnrrXY_qtXWkOlZN7lhyDVvWPwObVY1mSy-00yMUW3LnZaKZXLYNVFB5g20XtWoTyflqSYcENLO3PuJvyYLSQPMRV1yEOmCLe1FSmkJ9xUqhkoVPG9h5OZo4mN_Kbl1BK6MX9Oxvg5o9K40w4RGc8KjKoLnBeiK-d9rMVJISpGstOf6AXbOoAHpFxR0P8BGaWL7UdnqTYjBwyNGzu0XQ8imHkABBVK_yNBgQ_P3XgS3KetgHyMPpilYdRlwqx9f0xk1hWjUtHMI2Hy3zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80080a6ded.mp4?token=hEuIBkcw_KhUmWPz7qRaLsyXfrT5OEsUdGRu54Yjr0b7rMu2x90GrPHAiIY4TFfdx5ELdsnrrXY_qtXWkOlZN7lhyDVvWPwObVY1mSy-00yMUW3LnZaKZXLYNVFB5g20XtWoTyflqSYcENLO3PuJvyYLSQPMRV1yEOmCLe1FSmkJ9xUqhkoVPG9h5OZo4mN_Kbl1BK6MX9Oxvg5o9K40w4RGc8KjKoLnBeiK-d9rMVJISpGstOf6AXbOoAHpFxR0P8BGaWL7UdnqTYjBwyNGzu0XQ8imHkABBVK_yNBgQ_P3XgS3KetgHyMPpilYdRlwqx9f0xk1hWjUtHMI2Hy3zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگ هادی‌چوپان با رقبایش برای عکس گرفتن با آرنولد در رقابت‌های اوهایو!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/Futball180TV/90305" target="_blank">📅 22:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90304">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35b0dae947.mp4?token=uSKvF1pAkWivot-Bq5-2hpjxtpgGnWhnn7FPgmz7-CiMxx6IzpO0Lo3qDBz0IYjmidLZHifeAXq9MHhdUF9hb3eTAIAd7iRnWsrsryWlaj78eszSYJtPAbQeAfMPWRnO5HDXvsFNuUAqz3L-oGiAVoNvrs15SpuvAkIFAOJYYrW6m_kvjdp_MkU9ZQDw0XUE1LEGGPo-RkjLWIrIimgkLVj1ZpL0Qg_kLZqgGzqVwg-ALon2zToeXuXg1GU71jpZCxE3DtqtRrZzm9tC8bJ4_LOM-yvx7jRU96D2fB426E9ZZf5J7F8BvcWtQzl4a5wQBa-4RF_Reie8-XPSN1mJuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35b0dae947.mp4?token=uSKvF1pAkWivot-Bq5-2hpjxtpgGnWhnn7FPgmz7-CiMxx6IzpO0Lo3qDBz0IYjmidLZHifeAXq9MHhdUF9hb3eTAIAd7iRnWsrsryWlaj78eszSYJtPAbQeAfMPWRnO5HDXvsFNuUAqz3L-oGiAVoNvrs15SpuvAkIFAOJYYrW6m_kvjdp_MkU9ZQDw0XUE1LEGGPo-RkjLWIrIimgkLVj1ZpL0Qg_kLZqgGzqVwg-ALon2zToeXuXg1GU71jpZCxE3DtqtRrZzm9tC8bJ4_LOM-yvx7jRU96D2fB426E9ZZf5J7F8BvcWtQzl4a5wQBa-4RF_Reie8-XPSN1mJuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حق‌ترین جمله‌ای که درباره وضعیت فعلی میشه گفت:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/Futball180TV/90304" target="_blank">📅 22:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90303">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05aa244672.mp4?token=S5Bs8B989P8yOojO8GbbWbghTAEu4aaZzoJD6ra8K01MTocVPRfR5GNriR_skic3uhwocElBE1EqqOYYnz3_GdGpMVz4EdUKmDlSdd-ZM8ydPrBXV4K59ZkG0f-4WGJf6QSEVpAAoTUQaNW31H9VlYQsdQ6Mtm6gwvln6S9SMhyx1zdFjwqYXV9OnQYtIhzDKp5vI6j4WiTY3TiVykxj2JesRO6qvbmD57_AIseQ9cxdpuQs4z0j7OqdSNjXqfonY2viXSdclueiwQVJxHsVp2hJkFi_qnt3IJ2vZzCd1eaIXJ8UTkYtBpMdzzMADcfdsWqDQHyDfeGxDKlSKhGHMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05aa244672.mp4?token=S5Bs8B989P8yOojO8GbbWbghTAEu4aaZzoJD6ra8K01MTocVPRfR5GNriR_skic3uhwocElBE1EqqOYYnz3_GdGpMVz4EdUKmDlSdd-ZM8ydPrBXV4K59ZkG0f-4WGJf6QSEVpAAoTUQaNW31H9VlYQsdQ6Mtm6gwvln6S9SMhyx1zdFjwqYXV9OnQYtIhzDKp5vI6j4WiTY3TiVykxj2JesRO6qvbmD57_AIseQ9cxdpuQs4z0j7OqdSNjXqfonY2viXSdclueiwQVJxHsVp2hJkFi_qnt3IJ2vZzCd1eaIXJ8UTkYtBpMdzzMADcfdsWqDQHyDfeGxDKlSKhGHMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دنیا برای آخرین جام جهانی شما آماده نیست.
💔
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90303" target="_blank">📅 21:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90302">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NthtgRDn9nWUDg6MyoVPh6chkWF7NAZ7NEvhnemShEhzp5eE-pGL7dDmiPCZZ3rvxkc89H5y-dwt7tzYHWnrSVuEwaL47BX7lIbeaPQye519qYfEf6oSjxVZ87PfdhZZ8G0a0StRSG9Wdpwf2pdQp1QjYyAStrgHTW1iAiL_uI_I1zn0cD1bWS7h6ZSAWwrcWTQoyI5DAoWsZ6ZfuGjq-Ab3QxU8BcpcUFax5BuYKHNulNugRGcptvgIVtCdIXqgmT1CCFxzjxSi7Q7hudozickn7Owk7ngAxR7iuK_gPYivvugLt9EfLBkH2pwMy3sOy9Fd-7b5EAPvxqfhVH7bxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#غیررسمی
؛ آنتونی گوردون با عقد قراردادی به ارزش ۷۰ میلیون یورو از نیوکاسل به بارسلونا پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90302" target="_blank">📅 21:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90301">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b45e4bbf26.mp4?token=aJlbmzh7TI7Fi5QDcaeo4kDJFWn5YxOOD2Wmt_sOfYprhHsGsi_lJhElp_2Aeeg-V02zOzCHSw0hPw80pTaIdcVru0oVKHzQa2k7S33ppp3DbmJE0_Yl2spt24KbLTZID2AfXZ_I8obLPmAd89wL0ihuk3IA0RdpUnSNyJN2gUqEM7OdIY9tPCo_dDQFwtVK21_g87zfjlznMeGQ8f7afJixKBUS628xpDgsgloZMD24veK0Jf2_cY25Ze-IdgH-gK0FCcVTwReD3VEbSiglnAJc8f43htnM6kJOKu__tLktHs5TiKfjU3SufmwJgnM6boiVZ5bCPds9PR_R1zob_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b45e4bbf26.mp4?token=aJlbmzh7TI7Fi5QDcaeo4kDJFWn5YxOOD2Wmt_sOfYprhHsGsi_lJhElp_2Aeeg-V02zOzCHSw0hPw80pTaIdcVru0oVKHzQa2k7S33ppp3DbmJE0_Yl2spt24KbLTZID2AfXZ_I8obLPmAd89wL0ihuk3IA0RdpUnSNyJN2gUqEM7OdIY9tPCo_dDQFwtVK21_g87zfjlznMeGQ8f7afJixKBUS628xpDgsgloZMD24veK0Jf2_cY25Ze-IdgH-gK0FCcVTwReD3VEbSiglnAJc8f43htnM6kJOKu__tLktHs5TiKfjU3SufmwJgnM6boiVZ5bCPds9PR_R1zob_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چالش جنجالى و جالب مجری با محمد نوری پيشكسوت باشگاه استقلال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/90301" target="_blank">📅 21:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90300">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KInlT9wEkb3vaIuEqlinV4EzZw_Hq53bRXbwjQ4-uiVjx0xxQkqplT2cvI9ULRBd0l-vxMhaoea-A0OWeL_iwFH2gZ7rCRdWk9SPZx6NLloWAp_dCOUAJyaj_keM0Lzh5q7HuFODt_Rgu5_lpapQHymSSoxptu-hHePMIaZDA2n03jiu9_9z7QD9gL5745wyaehpS_ZLgkHZDctw7kDE_T1IXbSeDjVKquHUYiW0veP__StD2Wp7lOD33S5mQtewaHkz_hT59EIRfyYGd1MkYOm3K26AKRD3goHqdK1FFGf8x7Gh6yYdu26GGKUl__BzfEbERiZXQVjOozBClsaH8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات‌تاریخی از مراسم جدایی الکس‌پوتیاس ستاره تاریخ فوتبال زنان بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90300" target="_blank">📅 21:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90299">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-trhlD_zjHfP9Z1RBOA8c8q0NsYhyPezdNUpaH6e-hjIuSZej5JtJLnSZQVoYX1NTE_laNDErlBjT4-UFu5jND1Cm443lzHWM-W4mBXzRTmk1VzOPdEunz1qOsw7OTfj62Rs0CY_2qbncA0J5Obh_Rshc5F-zM5fU1vRbIRWXgxlD3bALyxVG4Chy8WZX2Yhi31CB9MtA2Gv8DdS21XD8V9nWequWrB2j7MqNPWiS_ZaSG9Cm9VNotzrZYVy622SEEGq9pnrDM15CJRvakRITh0EkXEtpWLhY-aVuUPmOI-eq6pm8OPx8bW0hROA2HP45mobtrUngDolJxbsJnKTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قهرمانان تاریخ لیگ‌کنفرانس اروپا به مناسبت فینال امشب این‌فصل از رقابت‌ها
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90299" target="_blank">📅 20:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90298">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a28e2aed.mp4?token=pVF1O8YNWNx5oGtz249NF-_wpSku1kW4dPFXp4WTYoIVkyk1sru5KktfV6bSwPwmaGx7ng8IYot8J2JHpVoxDk5e1IZcW5a1Z1w390n_p2FEI8HaKhqvQ-u7DVn3_4OTuoEXvXWtl19BiROn_alqAbrK9PEmtGD3sTjyaGeJ0rnwqDWKW9elSm1tA6Bb9u6rw5AAY0z8SfPLT02zupw1q5bChMntp4Miyf7jfwsZ2NEyP_3ihHEsnYPnkTDRfKlt4qoC9ucszt3ulz2X_WWRTH-g4qVlg9KMTyplj1CEEHlz3lvj-pGM2k6BQJ_C3dbXQYh_PR7bwJXdVunGp1slnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a28e2aed.mp4?token=pVF1O8YNWNx5oGtz249NF-_wpSku1kW4dPFXp4WTYoIVkyk1sru5KktfV6bSwPwmaGx7ng8IYot8J2JHpVoxDk5e1IZcW5a1Z1w390n_p2FEI8HaKhqvQ-u7DVn3_4OTuoEXvXWtl19BiROn_alqAbrK9PEmtGD3sTjyaGeJ0rnwqDWKW9elSm1tA6Bb9u6rw5AAY0z8SfPLT02zupw1q5bChMntp4Miyf7jfwsZ2NEyP_3ihHEsnYPnkTDRfKlt4qoC9ucszt3ulz2X_WWRTH-g4qVlg9KMTyplj1CEEHlz3lvj-pGM2k6BQJ_C3dbXQYh_PR7bwJXdVunGp1slnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله عجیب مجری پرسپولیس صداوسیما به سروش رفیعی: پرسپولیس باید یقه بازیکنی را بگیرد که حال نداشت بازی کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/Futball180TV/90298" target="_blank">📅 20:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90297">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ac28b3311.mp4?token=tLIN2-KIzc7z12ZQb0uoxK9aGOuApf9JRddMMx_edPO1CBwnRx18lCbMaeswiOeRkcCppGjD7aWlEWDq_fgWXQtp2C8kLfrr2U_spJTtBLZEDls6bzJ9coQrcBBuYPeIQbbFzY5paKUaMkG8rJheZE9ntxyCeI3QZC4wMtYnmp8VsEMp_AGheKWKcdpYgVacvMnwDZW1gATl4GfeMOp582tdNr7r4-PNpA4vtOfKbqZSllCrPtoIHTZXgqN3qoDJzpAvHgBrDrpR2s6JAfENqbBR9wVMlR2CgnEqAluIj9Ganqj8D0WzRZtgDlau8Ou96gdeLYQF4Ovu0HZv2ZB3aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ac28b3311.mp4?token=tLIN2-KIzc7z12ZQb0uoxK9aGOuApf9JRddMMx_edPO1CBwnRx18lCbMaeswiOeRkcCppGjD7aWlEWDq_fgWXQtp2C8kLfrr2U_spJTtBLZEDls6bzJ9coQrcBBuYPeIQbbFzY5paKUaMkG8rJheZE9ntxyCeI3QZC4wMtYnmp8VsEMp_AGheKWKcdpYgVacvMnwDZW1gATl4GfeMOp582tdNr7r4-PNpA4vtOfKbqZSllCrPtoIHTZXgqN3qoDJzpAvHgBrDrpR2s6JAfENqbBR9wVMlR2CgnEqAluIj9Ganqj8D0WzRZtgDlau8Ou96gdeLYQF4Ovu0HZv2ZB3aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال شیک نمایندگان آمریکا از تیم‌ملی عربستان در بدو ورود به این کشور برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/Futball180TV/90297" target="_blank">📅 19:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90296">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4496fe5fe.mp4?token=OCoLVxE1kFCLVhEDIonDcm5Wyurqc82uMLd1l-WGuBbcWWNVUt-zZGpSCAOJKd6MWbKHPbpvtMX2YlRZiuJ0_8USV1qxsKv9tXo1e3luXRweHOuCo9_p92nPwOodQYX5zVxA2nHk55ZhE1Rz0hGjK-Fp5mJQErGsYX42QCOUXtq17yHRxGbz6O3EpSlKpAdOfkqd-QC9BshK0O2sbm0b8Bll76w-i0DltK92n_qOtN0X89JmdrT3mGww26Yvzvte507u5mPyK6AI-RlE8OuZRW2jmSWBigDAkIZfjk9HKcfP0FtSH_8MY6YuWMdfmyE92NHpHbdhStxeimpTVCdMzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4496fe5fe.mp4?token=OCoLVxE1kFCLVhEDIonDcm5Wyurqc82uMLd1l-WGuBbcWWNVUt-zZGpSCAOJKd6MWbKHPbpvtMX2YlRZiuJ0_8USV1qxsKv9tXo1e3luXRweHOuCo9_p92nPwOodQYX5zVxA2nHk55ZhE1Rz0hGjK-Fp5mJQErGsYX42QCOUXtq17yHRxGbz6O3EpSlKpAdOfkqd-QC9BshK0O2sbm0b8Bll76w-i0DltK92n_qOtN0X89JmdrT3mGww26Yvzvte507u5mPyK6AI-RlE8OuZRW2jmSWBigDAkIZfjk9HKcfP0FtSH_8MY6YuWMdfmyE92NHpHbdhStxeimpTVCdMzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور نیمار در اردوی‌تیم‌ملی برزیل با بالگرد شخصی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/Futball180TV/90296" target="_blank">📅 19:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90295">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFKqbup26FCEMHhtNHLFItxy8ExxXhmfrMcln3jTN4_4RS1Q7nDH3C2EWQNpqHgA9mYLe22lN09uf89PPIyGOouBvHYYB2fzSdqcQkzR1aY3o2baErX0t64NYBgWXHvfM6bX8ks7C5g38Zv-umLB1uSEzQcxHp2raifuG2nuPQPfkoDmDflk1IV2pB9he92PYdUwubtjAwcGsLmXnBJDT_wjq37V5-OoYD2eXsoksb0l1tKQZBFflbqttJrB1nemOfDaMLQLybXzBclPQUY0WRryoFMI1ru6hKv6EYtFLdALTsvRkVFNN6TgH0lu2Ms8lpsOdg8lH0cIIjQRpScOXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جیکوبز خبرنگار مطرح اروپایی: چلسی برای فروش انزو فرناندز درخواست ۱۲۰ میلیون یورو از رئال‌مادرید که جدی‌ترین مشتری وی است، داشته!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/Futball180TV/90295" target="_blank">📅 19:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90294">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c0fba26b8.mp4?token=vrb9jf-euJTJmMdkV-W2Icv_G5X274ea1ttQZIQVvcHVFldY9-IT3JGOHoWsHnr1T0EfL3kkTfFjBr5aCa6y631GFDHRyc2pbR5IAhloHlQ8vzb_KSQSOiPUydEFCnlV_gTnXKspEBbScjFiqKlVXtom7EahVwOA69b1NifNEP9sm3_mchE2KuSVmMK-UJQopZegTnvZOs3_YnVqlkWOKcJtqIEaylPwFpzEtqPR0H83C7e1koUAWxj4ZoUczP-zO8PCuXv15VNbHrYWk0R-WFS2fha4yFMwDCvC4UGe0k4niVMz1OhA1jHm1lX74mM_-deA7uS0TgMSSzDxULBrs1gZtWtZ8nDHuuYwIHWjXkXeEKcCIhpf6x7JPZaoy4C9JGM4uoRUVeZoMM_WG0z1L7vUxGa4gU1Fu1FM-QLLxzEonI76swZv2KLtf13TeWXc1Hq2oufS2Ls7hBCs2_XsA69KCBE02FSjJI4xjn3U3EZAtLP3Y8cerAyLKEeiK4PsNg_Fgdv-PPLIkmyO_3W_ltlohb91PCpalX7R8BBIT5WMkEmMb2iztj22sykcLUPdDMYJzlwRej0ESHmvAFr6_iNzS8JBZEvqOgYRq9BomicIA4JwRJQsJZN4R7fMBcswWaVYRUyH8NaWxtQ415UEdDHwDus5CuW3nQoW56vewYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c0fba26b8.mp4?token=vrb9jf-euJTJmMdkV-W2Icv_G5X274ea1ttQZIQVvcHVFldY9-IT3JGOHoWsHnr1T0EfL3kkTfFjBr5aCa6y631GFDHRyc2pbR5IAhloHlQ8vzb_KSQSOiPUydEFCnlV_gTnXKspEBbScjFiqKlVXtom7EahVwOA69b1NifNEP9sm3_mchE2KuSVmMK-UJQopZegTnvZOs3_YnVqlkWOKcJtqIEaylPwFpzEtqPR0H83C7e1koUAWxj4ZoUczP-zO8PCuXv15VNbHrYWk0R-WFS2fha4yFMwDCvC4UGe0k4niVMz1OhA1jHm1lX74mM_-deA7uS0TgMSSzDxULBrs1gZtWtZ8nDHuuYwIHWjXkXeEKcCIhpf6x7JPZaoy4C9JGM4uoRUVeZoMM_WG0z1L7vUxGa4gU1Fu1FM-QLLxzEonI76swZv2KLtf13TeWXc1Hq2oufS2Ls7hBCs2_XsA69KCBE02FSjJI4xjn3U3EZAtLP3Y8cerAyLKEeiK4PsNg_Fgdv-PPLIkmyO_3W_ltlohb91PCpalX7R8BBIT5WMkEmMb2iztj22sykcLUPdDMYJzlwRej0ESHmvAFr6_iNzS8JBZEvqOgYRq9BomicIA4JwRJQsJZN4R7fMBcswWaVYRUyH8NaWxtQ415UEdDHwDus5CuW3nQoW56vewYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماجرای بازداشت نیکبخت در پارتی شبانه؛ این همه آدم معروف آن‌شب آن‌جا بودند چرا فقط چسبیدید به علی نیکبخت؟ گفتم نفرینت می‌کنم یک روز جای من زندگی کنی ببینی جنبه‌اش را داری!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/Futball180TV/90294" target="_blank">📅 18:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90293">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvgOTvvQ9xpGz60O5qNam82e68sujU4h377XekGO4iPlKPK1vfkZmiQMECJcSCM9ZWU53Ca1JeewAYiVuIsIYwRsS_rEimyUjCyX6inDWPN9pe8MAxZe5JDpCM4qbZKAYPlDFdWwLRlRhzkNRIrrED6S5YNkqyfFM5T8ziG6zWS-WA8S7BY9Pgyfjg84OilKDuAgfNv8royGUPF2k5NSj6SjtU0K15onNZiH11bgteuvNe7wwiC60VETnuQHyGDkCa5ATQWd8icGHbslhNpou1zNgtSIvnOAzsXAXSH-XXeW6_zBRelIomHvmUJw3pDmcztx0w8pRMBuYOtQY01gYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین هتریک‌های تاریخ ستارگان فوتبال
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/Futball180TV/90293" target="_blank">📅 18:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90292">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⭕️
تا حالا بدون واریزی روی فوتبال ها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
شارژ سریع و امن با درگاه ریالی ، تتر یا ترون فقط با یک کلیک!
⌛
پشتیبانی 24 ساعته
💖
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:…</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/Futball180TV/90292" target="_blank">📅 18:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90291">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBMN4k15SFfLweXvwG9RYaJpfHf3kmxyFLWt5cA6LlerM9ySF4SbfXHTN_78R6QiTAtWgw19zk-Uxc4m07J6XQU4OhZevCT_rmLX6567bjDw7Pl28zuAughMhDfUyvPl_1YMEg9E8fK9eVcXrxvdBaSTv43F0ppGo4FlB6XYxDI1G9Ve7TqMovzN8NfnLg4KrCWulUMbdISn5PoYKzlLrSt6WYXd1dabOmB5eKaDboG2w-73cC-HCwWsxQ-MNCOsuHZbQnGgEhWu8vz9RwW84N3pyB9gF6sWS-gdbtNpqsNuzy5j2Lijl5nIgf_CckMAYkvPKQE1Fu-UEBd7zyu39A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تا حالا بدون واریزی روی فوتبال ها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
شارژ سریع و امن با درگاه ریالی ، تتر یا ترون فقط با یک کلیک!
⌛
پشتیبانی 24 ساعته
💖
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g6
📱
@winro_io</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/Futball180TV/90291" target="_blank">📅 18:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90290">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cs5XFl-scToXIR1p0vwnjz4hBffCfxhyPF4hh541h3-uy2xCrENigDuwhnSBlhmiuZn3PKhSXS5LoBCfSmuM3pbVM2pESSqh13vpsPygXdGPEPh63r3l_vjfhJqrqciY5PshiC--pJAH_j-c9anF-9fGrHt0vm6M_1FWa5nJ6qN-V0kEg-_9Rzw2e_M3pJP5Hm5bGc2qw_PbSpYVNvlrAq-PyxMOr-sBEgFGmM5QDhifq2RDziKT87vLTHbjgAoB7XCBMmzfi8-4AKPB0T6V3fUUi3sN5l1Wx8NrdL0bGjLjRHhfn1OgX4Z8jpQC-1zBjRD_RZiq5rgCFpKlqZNvZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمامی قهرمانان جام‌جهانی در یک نگاه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/Futball180TV/90290" target="_blank">📅 18:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90289">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Coe5SXlJ3GBuYSYiHIlHmtS8FHeabG6JQn42kdqxBVHz8db5JstUmCVxF2CAaebbVki7w78-vEzKTLKRoBpW5X7DCBVjlcfovcOxVmP4IFBaYRfZx1TMbc25f9qViV6qElYvtE7uGqBjgddUXOtvr541DR7C-i6G7I6JtotoIRIqM87NSj337LwApTNX5uNiJLbyBlpKljAZ71y098lUWFkYpYgoV4oE5H4Jf6yGB0KT-hJsoRH0ubSsIb5V4y-sFEpGt8rwnGMLKYzYPpVdMK40yOSk2Bxpp_5chfNt51BOac0NZ3eV18bI7R-vfqz9VqKIWbhchK3jw2YvHqksIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
به گفته اکثر منابع خبری، قرارداد آنتونی گوردون با بارسلونا تا ساعاتی دیگر نهایی خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/Futball180TV/90289" target="_blank">📅 17:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90288">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXzQW_o8F2W6gqwPid1kVl_qJF6SlrfJ6gmfjJRiR-ULDRwFvMS70YbwgPF4T5FhlTSY0YlrbTf3w6MFE15KkV5Z8e-l6xnBg5HZeu3-doF1Ir0KhXHf_nPiO20gw_D3hWuEYlBEgAsRWxgVWqGDD_nxgALi4zMetfDSwacnFppD7FvIq1cHs4keIwBnDhMZuqqM0Xsi5VbsUnFE3sUHOnZU3wuXnm_q6tsML3U08gQoSSXzv3TyqezOzTxSdZcQ6FJlyqHOMgeoOCQvDNLGPKqjedD3KRO1l3bxnvd0RqxtsC3g7ZcgZBLpWLuWtXg-qRt7Pw81G-ERHVCam1FjVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه میزان بازدید پست معروف جام‌جهانی با پست اخیر نیمار در صفحه شخصی‌اش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/Futball180TV/90288" target="_blank">📅 17:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90287">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hu729zj7E4x21Qjz9ZkvIK4XzNuvtPRNt6toX1q4hT4v3nJXQ8BmYt_JIw7cEeAC7wOqTuOMNEFjVPM7rPqHWfmjUP9dKqASVvQc5S9iJqAIkyOgvT9Wu0pelPdEpKrSiC_mxQNTOMFjlm-kOMT3vo-FdxwuIpsFcdtz3GIwsw9YVfKRNVpehKcdXm6DH5JvFzgmTft5YrJJJ2PyINjTY7SjZejKacRWaqkOmUDUKJGpc6BSkpGrn1CEHow27KNv7KxfAeIJ6CpScf9OBPym6eiM8dI0Qbd2ZouF6mYgn4xsF9m7P0YySXh8iUJVU51uwz3f8jBq1gqydx_m8YaXZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جرارد رومرو: بارسلونا قصد داره قبل از جام‌جهانی قرارداد گوردون رو نهایی کنه و سپس به آرامی در طول تابستان مذاکرات با آلوارز و اتلتیکومادرید رو جلو ببره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/Futball180TV/90287" target="_blank">📅 16:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90286">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30945cae67.mp4?token=sQmW_I_RMzPoLCGX04LpAYWfHi0RPlBCKBOSURqQfCZw7XhhlOPht1aScJLJrhZaRy4RYjSmt2zctV85H-G8opQYxf0oj-2xrRfy-MFP8ZDH1ncfKIfdidvMhYWj8LvHCOoK9YP5p94YUJScJ--tiS7nX3XxpZpq2W0kpKQa2GcXOBXeptuAeJgdF23hf0gWatQWxa13Edmtc0rjaY7ln0i74OEen4HHlL1rXVqwetStBGIAwecoHe_HkT67EZ7cB-E9VrOr5z8FV1kbEVB_QegSwL3XM-vh7bK4Fu1MEQgU82Qrblid8YYNOSRsGBr0m-HIFvBxYt3S3AEmXjs8wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30945cae67.mp4?token=sQmW_I_RMzPoLCGX04LpAYWfHi0RPlBCKBOSURqQfCZw7XhhlOPht1aScJLJrhZaRy4RYjSmt2zctV85H-G8opQYxf0oj-2xrRfy-MFP8ZDH1ncfKIfdidvMhYWj8LvHCOoK9YP5p94YUJScJ--tiS7nX3XxpZpq2W0kpKQa2GcXOBXeptuAeJgdF23hf0gWatQWxa13Edmtc0rjaY7ln0i74OEen4HHlL1rXVqwetStBGIAwecoHe_HkT67EZ7cB-E9VrOr5z8FV1kbEVB_QegSwL3XM-vh7bK4Fu1MEQgU82Qrblid8YYNOSRsGBr0m-HIFvBxYt3S3AEmXjs8wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از حواشی بامزه مراسم خداحافظی باشکوه پپ با سیتیزن‌ها
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/Futball180TV/90286" target="_blank">📅 16:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90285">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c42b3ba26.mp4?token=HsprUocrlvDe_Ki-suB-S_FbrGMwMGNk5rPP7LPI7wdcy2ElXMBGvPLoSnyCaSNRaBjQqC9jaOxuIuh5WpHTjTCNQKH7YOfFOmAT7tAMpVxz4WpzIxCaArsCNx5ZOi8UOnE2kYf7RIi83vzDby6PAUPybazLgvq8VsHijxMbwUGBdv7p5XPkmBCgN0AwlcNllW3ED3q2MdmAQiM4AIwjVujxM5KuyIjT0KzEBOrgg_SDz-568IXXx0Yr7UPO5KzrTTZw9-I0LJdbnPxc1NqLYrZ6PoUL54r82vjX_6zYZcTS9EUA1MRB_2zYCwVG3TQGQoDNzlNEIO_HM4NYw-uQCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c42b3ba26.mp4?token=HsprUocrlvDe_Ki-suB-S_FbrGMwMGNk5rPP7LPI7wdcy2ElXMBGvPLoSnyCaSNRaBjQqC9jaOxuIuh5WpHTjTCNQKH7YOfFOmAT7tAMpVxz4WpzIxCaArsCNx5ZOi8UOnE2kYf7RIi83vzDby6PAUPybazLgvq8VsHijxMbwUGBdv7p5XPkmBCgN0AwlcNllW3ED3q2MdmAQiM4AIwjVujxM5KuyIjT0KzEBOrgg_SDz-568IXXx0Yr7UPO5KzrTTZw9-I0LJdbnPxc1NqLYrZ6PoUL54r82vjX_6zYZcTS9EUA1MRB_2zYCwVG3TQGQoDNzlNEIO_HM4NYw-uQCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرتتا و همسرش در جشن قهرمانی آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/Futball180TV/90285" target="_blank">📅 16:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90284">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZZUBhClMlC2Pffqsey1BSCVonztJMGScNWDPvcguZDmO3pvHDOw5E9soAcI32tJP3RR4bTzFEvMdgrjFxnkNn3lcaJssnQ6SvrC1KBGb61oVanHiC4lIsdHhCO_U2qANWhoNI0-PyY_ZtTygkGSfT6PdIzqC1MIk5qShRDIMnkhgRMlCjoom2b2OHjjtB-GMYCSEv3z0j3QMzCg-wpx30-hLAFBTfflVz2foOQ0IOvqTpEiyhaoqHEUE-y0UxNAsvY4TlX8WTjV7SqDxfibiHi2035iYLDJEXF1Th8-MfaQoz2eVVivZ1joRfMdcXt5jcrrcoMIjQ_8CWeHHVmtvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست تیم‌ملی هلند برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/Futball180TV/90284" target="_blank">📅 15:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90283">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDAmxhI6I1VGqJBIMfP2JcSIIdO6Gr3YlkPzT4rxvVWBIEtVi5RZ8vbIiRhp-oxvlYUr335S1BXzSGkxCEDmxc6xSH_HdUbN0vpAJq7i7ziH-pPu0Sm2DENh_ohbc-T4SrfgJY_hHH9N6Z160ugx80MC2GCS5wYReB4ScNBDhv_s1QfWoaWJRv7_Hib-67MqWF0TL1rlyIomAAmkBuYKjb0nxwVWbuxYou7Y_WcMXQpd3xTGj-QvbTvl92gMTsCXDM3Mw75c5IIaoIyVyfGUo1_w2XoCPBpm78bippvdQHGAaj_pW0GYs5023RdnJUzMDqowLwX7Wq_eCbvGi9yFfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنج سال گذشته: کریستیانو رونالدو ۵ عنوان کسب کرده است، در حالی که لیونل مسی به طور چشمگیری ۱۳ عنوان به دست آورده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/Futball180TV/90283" target="_blank">📅 15:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90282">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZMVn6YWe3uDlsjKCPt1H469iSvqVsvHgWpYJS1rOt6-CtEvRWTftUVEYWvq49dbNtsnAu5sdwBpwyJyR8MhnE37pMmSCC6xaCPmHrJxX_2q3RViBaK4RBIks05r0N7HNpZ-j2DxTVydxdIL-VaK_5LkezCxv0LqMT0epYsAVvPBwHA08QJRFEq_0hs0pUXodNHyhAJSE2VVHyB3dvZJP9V9O2w3gnrlml4maY_ZP0vUxmF00umGQq2w1SVgOASR3CE4yDCv2_V9odvzDUtYinjDuQlD5DeWVA3GULK1EAEXhoignczJGvxUvbqXcUufZwMQk0xaMf6hzGF9il2GRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">180TV
🤩
🌐
دوست‌دختر جدید دوگلاس لوییس در عرض چند روز به ستاره اینستاگرام فوتبالی تبدیل شد.
👙
طرفداران نه تنها درباره رابطه عاشقانه این فوتبالیست‌، بلکه درباره عکس‌های نیمه‌برهنه این مدل ۱۹ ساله با مایو بحث می‌کنند.
1️⃣
جذاب‌ترین عکس‌های دوست‌دختر جدید این فوتبالیست در کانال ما قراردارد</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/Futball180TV/90282" target="_blank">📅 15:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90281">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">آخرین وضعیت بازسازی ورزشگاه آزادی؛ 3.2 هزار میلیارد تومان دیگر بودجه نیاز است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/Futball180TV/90281" target="_blank">📅 15:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90280">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbe3da6710.mp4?token=PyY4CFc5hOP5Jm2klbwah4LaQnsctRsXZNi5qAvB-QyjgFhcPx1FUFJWUWwq-FZ47CYViU_1U3vz9PxZqxR3JGsSdcjcTOM8u-FsyP20slkobce4b6R3RGuzJHP1ysSQjXPTW1PWnG1qJBCvOzqLbZ6jlUsB5QdW4zbZYDiX5xesbJwO3madtPj7AgN5wVPLWWYoN98flyTwX6OW5ejd9T5rYwOp4tpV4htgunCggjZ7OWEYN0DMNbTSvuGzp3-BG7QTMtce_EyFC8Gpuz1-5v1alHctItZSu1TL5yd3msOSiuoACumqk0HNvf1HuE5XinYyzsLd7JdJv8i17MKiAKZdghAV6N3RDlPEzggS7Iiw3H844wWcPuEnBKgIStn27tmDtFuSfGfa8ZIkYTNPrT2YIy1Qo8yPFnRnorc8xx-ruM-tooW-WGLZeV29ox8b4ybZT9dowdMTfRJRNOLjPNzV_gTZZk_ImfU-FvHq7QPOw1G0bRBN3L68h-T_shCnisYltGZRPfCZZObgmRA5YBsTQeiONmBSvxT29ii4Rws0q4v_DT2Rd66X4YCRdyRrwsxa4TElG-9sfeDt9l0VfDG4O6qMvjyZPvBiTN9HgCXWe6KSijWu9W_-6eOB8Qhzq43zoM2-h48jNtrOnjve9NHomwD1u3jn3SBLEFM4tI0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbe3da6710.mp4?token=PyY4CFc5hOP5Jm2klbwah4LaQnsctRsXZNi5qAvB-QyjgFhcPx1FUFJWUWwq-FZ47CYViU_1U3vz9PxZqxR3JGsSdcjcTOM8u-FsyP20slkobce4b6R3RGuzJHP1ysSQjXPTW1PWnG1qJBCvOzqLbZ6jlUsB5QdW4zbZYDiX5xesbJwO3madtPj7AgN5wVPLWWYoN98flyTwX6OW5ejd9T5rYwOp4tpV4htgunCggjZ7OWEYN0DMNbTSvuGzp3-BG7QTMtce_EyFC8Gpuz1-5v1alHctItZSu1TL5yd3msOSiuoACumqk0HNvf1HuE5XinYyzsLd7JdJv8i17MKiAKZdghAV6N3RDlPEzggS7Iiw3H844wWcPuEnBKgIStn27tmDtFuSfGfa8ZIkYTNPrT2YIy1Qo8yPFnRnorc8xx-ruM-tooW-WGLZeV29ox8b4ybZT9dowdMTfRJRNOLjPNzV_gTZZk_ImfU-FvHq7QPOw1G0bRBN3L68h-T_shCnisYltGZRPfCZZObgmRA5YBsTQeiONmBSvxT29ii4Rws0q4v_DT2Rd66X4YCRdyRrwsxa4TElG-9sfeDt9l0VfDG4O6qMvjyZPvBiTN9HgCXWe6KSijWu9W_-6eOB8Qhzq43zoM2-h48jNtrOnjve9NHomwD1u3jn3SBLEFM4tI0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رمزگشایی سامان آقازمانی بازیکن سابق پرسپولیس از علت اختلاف با قدیمی‌ترهای باشگاه: جوان بودم و خوب بازی می‌کردم برای همین از من خوششان نمی‌آمد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/Futball180TV/90280" target="_blank">📅 15:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90279">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7_BJmb0ABTb-aDUQFjvvcXEoEoZzQ_28-drbG7sjEN-PJOsNKAo-CGXDpP8UOZMCmBvTkOvdK4VkBbitMCo01zLiqlPKsvkUOVx83_H9q8iNv1s_us_N_jggmg7ymlpXL6nZ69iOsHO3UqGCwPaUnPVwiY-wfIZ3nivlr1vZn0WYxW77DNkADVHUBG67upnIw1DzjXQvbG2yphqFcmtKmFoHUK5byYBRvhFEL5qt8UJx0MnvKM0K8Db4drSbRXEBOQxBMkZTg-RfY2iUOiT6IcKkgkgeyThggiixefnomOZdDHqTmzU9pDpffZmT3BLGJmjfz6-kHbpIfk56G3-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم‌های ملی که توانسته‌اند دو بار پیاپی قهرمان رقابت‌های جام‌جهانی شوند؛ تاریخ برای آرژانتین رقم خواهد خورد؟!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/Futball180TV/90279" target="_blank">📅 15:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90278">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cbec1c58c.mp4?token=tJzVN8U2puyDIy-d8yR_vs0Yd18qpj9LkHcQY9PLodlkLzQ5ti4ea4vsV31pkqkz4_ull27V6b7Rsd0cHgqiTiEbBIjnBZgfdbeCHu01An1mzdsJTCzmoaUKfF3p0IZSpz-mQXKZzb9QNnDkIcZ4f3c2HffsH1b4RtbKdAFGsy0EEV6IdhHvMh03jjlQgblvEaF-scAIIWSsNpWVJBjDcFTWPFLrKbSIqgiJKoxL49D8HBYlKwV0fxdfJ_fBqz4D6rsaf8_PK328EwZHHwV1GaFh1WUMKbUXkbbc9JHxgr_THJ1gpda_mEYhVgyquvnp1agETH4mwAi8slblQ955Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cbec1c58c.mp4?token=tJzVN8U2puyDIy-d8yR_vs0Yd18qpj9LkHcQY9PLodlkLzQ5ti4ea4vsV31pkqkz4_ull27V6b7Rsd0cHgqiTiEbBIjnBZgfdbeCHu01An1mzdsJTCzmoaUKfF3p0IZSpz-mQXKZzb9QNnDkIcZ4f3c2HffsH1b4RtbKdAFGsy0EEV6IdhHvMh03jjlQgblvEaF-scAIIWSsNpWVJBjDcFTWPFLrKbSIqgiJKoxL49D8HBYlKwV0fxdfJ_fBqz4D6rsaf8_PK328EwZHHwV1GaFh1WUMKbUXkbbc9JHxgr_THJ1gpda_mEYhVgyquvnp1agETH4mwAi8slblQ955Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد شدید صداوسیما از دستور پزشکیان برای اتصال اینترنت بین‌الملل!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/Futball180TV/90278" target="_blank">📅 14:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90277">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/083cb252a0.mp4?token=MTU5wiY6T8gg1PhMSgXUD2SwC--kCil9WKMn4hmkQEWjr8C3foNhuhjnyy4COiU2CJYsIgp-LOSfLXOaLvGOXbC_6PQppNGQDGoWg2llA2uv671Qo5dcpKLNoPDhRPleiVkjfFnOd7xCN7N-s5YBzjSHC3EqrxBPdV0XeMiFOIaWHurmJq8RRIQYwZId9jj1YaobETbLkaFfwpLTAaDO4MNDorz24B3QpOl-HTYoVAHd1NXDXUxyDkrESg7FiEhfUusB559xXV0OFo2mOIGWFFQQ5s7ANvMKAx44xrOwWjLrQr6YD91mPcM4BcxKYFs0YnS5ReiKWstjVuhTziA-0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/083cb252a0.mp4?token=MTU5wiY6T8gg1PhMSgXUD2SwC--kCil9WKMn4hmkQEWjr8C3foNhuhjnyy4COiU2CJYsIgp-LOSfLXOaLvGOXbC_6PQppNGQDGoWg2llA2uv671Qo5dcpKLNoPDhRPleiVkjfFnOd7xCN7N-s5YBzjSHC3EqrxBPdV0XeMiFOIaWHurmJq8RRIQYwZId9jj1YaobETbLkaFfwpLTAaDO4MNDorz24B3QpOl-HTYoVAHd1NXDXUxyDkrESg7FiEhfUusB559xXV0OFo2mOIGWFFQQ5s7ANvMKAx44xrOwWjLrQr6YD91mPcM4BcxKYFs0YnS5ReiKWstjVuhTziA-0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد نوری پیشکسوت فوتبال: سردار آزمون را ببخشيد. اشتباه كرده و عذرخواهى ميكنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/Futball180TV/90277" target="_blank">📅 14:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90276">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llytHT4ygYCGUXKn9rdqYNcmgMOSJRiuYSXu69Q8jk5c5SX-X-cUGAGCiNuWO5wR-S61E5A-hNF8ZGJoR9bWEncYenEG-1jVMQr2VZNWgpJAaWaxqImY-gP04oZDulN7Q5ocToMoOyKnz-3qC-isUpghK3j7DuElVyiQBo4XxfJnOpk4uq4TO0T7tU-M2OxZTtFWqjmaR7h6q0OI3zQ_8C3H5PzzK9O5T3k-uM8WAp5geV6I8HCaXzApWUw-1SEsUjpM42TXiMylG6l0i_SVu3u4rflW2s3W2bn63TdV-YjaGjkdOCEawUhwKkm_0Yo5kkBJR9WKc8w5Nvu0k6h73A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین باری که باشگاه بارسلونا ۸ بازیکن در تیم‌ملی اسپانیا داشت، این کشور قهرمان جام‌جهانی شد و حالا پس از گذشت ۱۶ سال بار دیگر ممکن است تاریخ تکرار شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/Futball180TV/90276" target="_blank">📅 13:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90275">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=Qgiaw6oEZ6BW9CdiY3iLwNMgZpdmDJRiVDj3tzChePk4LidwQPNLi-FgjMMyifX4xYPdw9WvmJ5CxM5pR-yhj-7N9snIvShEN4moUPU5RYccEXKSXIvuSSQBHGI2CzW8iYzlDF2T7HX9dUZFw0FntdxfHy09IX21bbTbeb3SQcFkw_5IprbwyhBHj4ashhgYdRNRN3CHrB3i_Xyn48yBO55mAz0QQTcKU8LiteJiNlJsOkmk0k2mjrFUh0-ZVT6IgZ8LAHlVaBbKHeqQ6ks81FuZyztbR5u9k33BCTjozXiGNbgFbLjmqfLa8RSdtY68d_SEtzT-G8WOQAp2klq1ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=Qgiaw6oEZ6BW9CdiY3iLwNMgZpdmDJRiVDj3tzChePk4LidwQPNLi-FgjMMyifX4xYPdw9WvmJ5CxM5pR-yhj-7N9snIvShEN4moUPU5RYccEXKSXIvuSSQBHGI2CzW8iYzlDF2T7HX9dUZFw0FntdxfHy09IX21bbTbeb3SQcFkw_5IprbwyhBHj4ashhgYdRNRN3CHrB3i_Xyn48yBO55mAz0QQTcKU8LiteJiNlJsOkmk0k2mjrFUh0-ZVT6IgZ8LAHlVaBbKHeqQ6ks81FuZyztbR5u9k33BCTjozXiGNbgFbLjmqfLa8RSdtY68d_SEtzT-G8WOQAp2klq1ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از عجایب فوتبال بانوان در آمریکا؛ بازیکنی باردار درحال انجام بازی🫪
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/Futball180TV/90275" target="_blank">📅 13:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90274">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGdggo9ydx_mwv7Nqf1i24RwLJ1rokLKMPUs8UdLEVehmhL0SF0_PHNubzWXV2i56QtCWT6eQxMZbYDhumJ5IVuonebafA8nr1XOxs7ExBuGnudwiM3g6GkfA4kg9sPWXJBJU8-pxhmwVzeA3ir8ZDrfABKnmcNWRrbrE3TbdnG9QT3jt8XKZLoCEKgLzj0rohNN82dmXZ1GaJcZEVA0Xe1y0Ma1vvBjIBXTkysr5Un_97CC14_m3Xcx9ClNm8JYY4bwdEneLA1hDEUIDfT_hipySYw_-tGWGzUDTkOXg2_S-b5uu3fAdF76c_sbIEP0tic-Ap0ey9pnJZKJ3ojQ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
متئو مورتو:
مذاکرات بین بارسلونا و نیوکاسل برای جذب آنتونی گوردون در حال انجام است. با وجود علاقه باشگاه‌های لیگ برتری و بایرن مونیخ، گوردون اولویت خود را به بارسا داده است. نیوکاسل برای جدایی او آماده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/Futball180TV/90274" target="_blank">📅 13:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90273">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhfTNAdyaPS6KVnJ4nKO3fgSp0BUFcmjoXPtqrXX0G6Feo1twF5TJQz0N7a3Zfc5CwC_vMgspx1ddD7vs6_pg9iaUJY5V9VPIWLKhnowGyRiPUZh9nUV0Mqmhwj5UDgPOVTQbYDQ_ALFihfS8G-E3JoCSBtslDiJCMsnTPjENlQBniD3oYsM7sskZ4nF01Vmaru5LBpKmQBDjA8OmGsc3r6gqe1jC6jyY_0d3Td4GziohT8X7Qc4QbPnF7IsRYWR-_esico9TaUrfimCYOSKL9YJ7IMlZRTvw00r2uOhr1FiPbakzmI1qJKDpH6_VMx4XqSN89nXwbVbRr8SOTChCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین گلزنان فصول اخیر لیگ‌قهرمانان اروپا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/Futball180TV/90273" target="_blank">📅 12:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90272">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/Futball180TV/90272" target="_blank">📅 12:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90269">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ani4eEqVoReHBLXNds8t7YU8iLmzs4LahZylmTucAyhzmGiOIx_HGwdIrjg29vWBty8azmFKeyJ1JfzQsOwTpdFc6Gsddp4F9N7Bl2cWwuX98WL8G6KniB8QBm8crDDzUjLdw0xu7P8MGg1DDUBn5A9VnXNZP7DXgRvGkqvt9Pj6hP32g1ptdif2HWb_R-gKc3Kz_qU0B_jMR6-B4zf4EWVzqkblP9r0tnCdWrTiO70Ufs5KjWzuhR44wXpiL7Mfk4GWjBIZmoIdVOBQRZqGAreR469FSDYF0M9kpS95lliMwtcWf2H6j6IZQsrINowJEgQT0vE_mMp-hshRlcGh2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/Futball180TV/90269" target="_blank">📅 12:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90268">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cf55f690d.mp4?token=NEn5MAvmmw8ZMmnqdBHO8JV0EHaMIa7Ozf58WUc1d7gmXmKQRTOJF1L4yI5jswWPdbV6yhorUl4d7D2OlFo29DLmGDyVUpyZ9cLX6yskKtPT11IwGnd7Wnfjp7tNgo6YaYLApSbuSIdl7eZktjl5btlSwKIQDaO3fAzb0yAR97X3R3P0CApanRlsJObPitsRHsvn7QKkLc9x6mRq9dTqrVh8VANnQtZ3y5bQp0hXTykQbBDzdP_tk4PCtXgc0L7OQ57ol6QReFhvXmno_pfLvbmZ6GPKyWxIioLDRC0ZFAYcpIWYg10k53qJnkFgrQxSaVvuZSMihGQY56Dkgusd3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cf55f690d.mp4?token=NEn5MAvmmw8ZMmnqdBHO8JV0EHaMIa7Ozf58WUc1d7gmXmKQRTOJF1L4yI5jswWPdbV6yhorUl4d7D2OlFo29DLmGDyVUpyZ9cLX6yskKtPT11IwGnd7Wnfjp7tNgo6YaYLApSbuSIdl7eZktjl5btlSwKIQDaO3fAzb0yAR97X3R3P0CApanRlsJObPitsRHsvn7QKkLc9x6mRq9dTqrVh8VANnQtZ3y5bQp0hXTykQbBDzdP_tk4PCtXgc0L7OQ57ol6QReFhvXmno_pfLvbmZ6GPKyWxIioLDRC0ZFAYcpIWYg10k53qJnkFgrQxSaVvuZSMihGQY56Dkgusd3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهارات تند نیکبخت واحدی: افشین قطبی کاره‌ای نبود. چرا در تیم ملی نتیجه نگرفت؟ قطبی ذات قشنگی نداشت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/Futball180TV/90268" target="_blank">📅 12:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90267">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98d2b87299.mp4?token=jiObhr3yau-Oal_U-qvHKyhT9WywCAa3EcwXn5JMXCFkcz6cCbncmkVkphvfJLLoPvVJyiNqiMm0yNvxc2t6JOPEwDOn3yxt7i6eJrKyQgXmxEbfQBeGYQRfqd0Qyf1PunMU7B8OhcFylX_03BLOO4llLyc1BeYcExzKpV_nqAAI3euy0q3FP1lsDJ0pDm6fHs8inGMT0XvVJ-hII_zhCr9pyIuv4LQk88AFeM0w_ome8CLEiK9KCwKEvZlk4c12S7J4KcbgMHvktPL60iipOYW4bdrz7IGlANJS97Pp8xjOjzhzVEMhwLXrOhhaOuxKmhnRHoSAAlWW_nKe_cjmAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98d2b87299.mp4?token=jiObhr3yau-Oal_U-qvHKyhT9WywCAa3EcwXn5JMXCFkcz6cCbncmkVkphvfJLLoPvVJyiNqiMm0yNvxc2t6JOPEwDOn3yxt7i6eJrKyQgXmxEbfQBeGYQRfqd0Qyf1PunMU7B8OhcFylX_03BLOO4llLyc1BeYcExzKpV_nqAAI3euy0q3FP1lsDJ0pDm6fHs8inGMT0XvVJ-hII_zhCr9pyIuv4LQk88AFeM0w_ome8CLEiK9KCwKEvZlk4c12S7J4KcbgMHvktPL60iipOYW4bdrz7IGlANJS97Pp8xjOjzhzVEMhwLXrOhhaOuxKmhnRHoSAAlWW_nKe_cjmAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اسپویلِ بازی آرسنال و پی اس جی.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/Futball180TV/90267" target="_blank">📅 12:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90266">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99be172cd9.mp4?token=UFfQSCRebhDIHM7ryAHWyrRScjOoYBiU-H8dUrxIxRhsXRI4CbxVxwfBow6TFLO-J1R0a99BjPvcsq78tqrSYgUWacAKkLjDqYgHnhEeXo_TR9swR6qNBfM_DuBLpffGPCpjnMAXSJheWsRJL8K6RCTUmrNr5rbbK8SCM_eBxLAAo8GRfw_HDVj7CHulrb5j8mj_Yq5tEvYOloNpqDYqHYLzeOj3CajM2cwjbCoyaiKj-57cPvCTaoW_T7RKKXQdJzsfX1pLKmYDhWvb_y6wWRMR8XAAqqLcg671lno0cTjcBd9-yh_MeJ_ANtKEtLpIGptnbgWEi90fDRTw7snonlKw2uYICWZb94Tyxyu1V9fTXigOjmbDKFvbZ7bmTdGnvKbjcztOjrgqzxxKlWO6ICsEsidOy6O5rSQseV9YWb3cwDfF52FCnIQnyKk0DU8MP9iVvHGkRzn2sQzLN60alHcIA1PwP242My27Hj22JXjoP21fRIsP4FiEg6hA7nTojm5M_gNat2tkfHHmvCqfTpwxHfRx4MIxnLpKS8WJReNgB4GR3HVHH4lk0PwxEvUvJXyX0sLFJGBHVbB38JSEKbAAzPxpIr7PP0Wqc2UfX5EM-VaZiy8VIZvMi_IqyOfZkHO2BfY3tvYKnRItWAoGkkr6N6mohzNzPAZw02KRFHc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99be172cd9.mp4?token=UFfQSCRebhDIHM7ryAHWyrRScjOoYBiU-H8dUrxIxRhsXRI4CbxVxwfBow6TFLO-J1R0a99BjPvcsq78tqrSYgUWacAKkLjDqYgHnhEeXo_TR9swR6qNBfM_DuBLpffGPCpjnMAXSJheWsRJL8K6RCTUmrNr5rbbK8SCM_eBxLAAo8GRfw_HDVj7CHulrb5j8mj_Yq5tEvYOloNpqDYqHYLzeOj3CajM2cwjbCoyaiKj-57cPvCTaoW_T7RKKXQdJzsfX1pLKmYDhWvb_y6wWRMR8XAAqqLcg671lno0cTjcBd9-yh_MeJ_ANtKEtLpIGptnbgWEi90fDRTw7snonlKw2uYICWZb94Tyxyu1V9fTXigOjmbDKFvbZ7bmTdGnvKbjcztOjrgqzxxKlWO6ICsEsidOy6O5rSQseV9YWb3cwDfF52FCnIQnyKk0DU8MP9iVvHGkRzn2sQzLN60alHcIA1PwP242My27Hj22JXjoP21fRIsP4FiEg6hA7nTojm5M_gNat2tkfHHmvCqfTpwxHfRx4MIxnLpKS8WJReNgB4GR3HVHH4lk0PwxEvUvJXyX0sLFJGBHVbB38JSEKbAAzPxpIr7PP0Wqc2UfX5EM-VaZiy8VIZvMi_IqyOfZkHO2BfY3tvYKnRItWAoGkkr6N6mohzNzPAZw02KRFHc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاسخ شفاف سهراب بختیاری‌زاده سرمربی استقلال به پرسپولیسی‌ها: فاسد نیستم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/Futball180TV/90266" target="_blank">📅 11:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90265">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhHO2KCt0qZvdxL-HOIFx2EZd6cuYg4j63a-zCYOrh7UVmxG53QdzAKFpLpET0sOBYcK8u5Avag_r5GBkj9nLZjnKAdY0i8PNS9R1q83eaUvBKw2eQHE93wYBGsXqpkkO0pNTXAk5qeU-iOuhIUiA6viIfrE4VmiHu2_j1uN4Sw6hhqZVtTS3-OZBj2w362dDk7sv5-BBrArwlv5uWWy1q4VGc1Pl9qBaDDXEiw7PMDaf6VpKujp5oGLCjLYqnuXlJHWugH9jc7DRrOzU8TsjR7kYZMfJ0VtYBeqyApLzhGmmpwhxWGkoyWxxB5ronFdQkhx5Fw45vvOk-Ay6ritXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
به گزارش رومانو، باشگاه بارسلونا بدنبال عقد قرارداد با آنتونی گوردون ستاره نیوکاسل است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/Futball180TV/90265" target="_blank">📅 11:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90264">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/426e74bc07.mp4?token=Q7uYVi99tkh9OezohyyQYEYpFrJyffpCyOaoQ4DsE-f3UbTwDVOkpS-jzpv3Sctjia1ck8DgoEizfG0EXJJp9vLtLCXODljf8x6OAtTciau9uGgj_A7D-B1tnkuIOHCVhpND4XMMK_nivd1t3qeziVeKwgLYcoY_IBAaBXV_9JqWvRY-7JmBTo1Bu-PetBVclxA-uhxfLUgFkUUWT20nQcL1cWt6Y2Z3OaZYmOgRoaJ-fCL-SmXa4K_5plS_l2wT9T0t7Txp9YYA96jqaJapXBNk8jmgNhwu9GbHsFR8_ltufSnnlGQhExZsJ4IbNE6RV-NFgzvaGKNKkwhXIPS434WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/426e74bc07.mp4?token=Q7uYVi99tkh9OezohyyQYEYpFrJyffpCyOaoQ4DsE-f3UbTwDVOkpS-jzpv3Sctjia1ck8DgoEizfG0EXJJp9vLtLCXODljf8x6OAtTciau9uGgj_A7D-B1tnkuIOHCVhpND4XMMK_nivd1t3qeziVeKwgLYcoY_IBAaBXV_9JqWvRY-7JmBTo1Bu-PetBVclxA-uhxfLUgFkUUWT20nQcL1cWt6Y2Z3OaZYmOgRoaJ-fCL-SmXa4K_5plS_l2wT9T0t7Txp9YYA96jqaJapXBNk8jmgNhwu9GbHsFR8_ltufSnnlGQhExZsJ4IbNE6RV-NFgzvaGKNKkwhXIPS434WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از اظهارات عجیب شیدا یوسفی بازیگر گمنام سینمای خانگی: در کارخانه پدرم، روی شمش‌های طلا راه می‌رفتم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/Futball180TV/90264" target="_blank">📅 11:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90263">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b5959b18a.mp4?token=bGKoWUxqjhdC3d12IaaJQySExTBTtaJc7_VXCUuZq8EfSXcm134h9YEEjtPt6H24bc3IlFnw8q4kQIXzFtIlD9wn6SOnE8ZQjYNEL-tJoHUQdotYGTZeTXv0QItzeHodtdSvMJN3FShjOyNsoMszyHwIMH15J0hA7NC09pC3wkCwqpNB4UeWo6beASkwNsYM2vLMLdAA4NNWuztBS407JTnpdvcDuBM8Sdxw4XwND1j_MKhn2SUlitaBp5UTT7WaIb1v1JlVXK-0DiSh-yS__Q8a-6lRFzUwco01P1z6oIGsvUBSnvJzpx24VZJiagO8R3ORPnZyqkmTxCb1iBDZYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b5959b18a.mp4?token=bGKoWUxqjhdC3d12IaaJQySExTBTtaJc7_VXCUuZq8EfSXcm134h9YEEjtPt6H24bc3IlFnw8q4kQIXzFtIlD9wn6SOnE8ZQjYNEL-tJoHUQdotYGTZeTXv0QItzeHodtdSvMJN3FShjOyNsoMszyHwIMH15J0hA7NC09pC3wkCwqpNB4UeWo6beASkwNsYM2vLMLdAA4NNWuztBS407JTnpdvcDuBM8Sdxw4XwND1j_MKhn2SUlitaBp5UTT7WaIb1v1JlVXK-0DiSh-yS__Q8a-6lRFzUwco01P1z6oIGsvUBSnvJzpx24VZJiagO8R3ORPnZyqkmTxCb1iBDZYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی صحبت از مهارت و دقت میشه
🔥
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/Futball180TV/90263" target="_blank">📅 10:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90262">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPqQ4vmOCATaYcoJdmg7jTJaXzY9gltdnOCk43D5tqOZBtcxaCEi-_gDPZytsfbvUNeey5FuMbIxRQWC_eLQb1pLrOeecGcAHfFw6J-i5havIc4TjARIiB-KQtlGXkBifWaB-B3vl7XZtUA0RytV2K-j2G6eZB6kH3FHpVsX-rGYHu7uKZOV5XVGZJbPSBRexq8VTzCu0xA4gI-g48-XSjuIOFVEk_X8GNQMQQ7VZvKuBJTngFioyobx9iv7UnS0DtCweCjZLO03YcVnOAnlRavi7n5KqDPjQ4y6BhnXMruSOjTL52GQJlwI9QGN-Cf0N8RdiQk6xnKZ0iomSKV56Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ترکیب اصلی رئال‌مادرید در فصل گذشته هیچ بازیکنی از اسپانیا فیکس نبود و بنظر عدم حضور بازیکنی از این تیم در تیم‌ملی اسپانیا برخلاف بارسلونا طبیعی است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/Futball180TV/90262" target="_blank">📅 10:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90261">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d64b58d74.mp4?token=Um2Dx1pHn52DB4K9dyJyLIgJ7vkfFeFKvEVksGRfhVBRQBvdkmpi_WXxRUFiTIHFY8nvUO0_9N7rYEdRRrP-NsQUs-wsIhpM1d-AjqNt8I1xjk1PEzLqc_txZ8KM-xi4rEb1eMf89ylPGW4eX0Rvcj0CJ89UBuU45zNJ2h3x9wZqcDYz8oukSaTwfH8g73P1tsQ_BDKvQGoqzwD5RGGip3AvmlXuOs8mV-sp_FbYVb45KWOlm4FdF2Tl2AjwQnimRDZ5dRk8bVAwQ6TK32wz1_BBhOUQ2xr6C-SOKZQWszoPk1xc7hkKAgo0u_urTYyCLnGfODcD0AV6TMt93yadUIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d64b58d74.mp4?token=Um2Dx1pHn52DB4K9dyJyLIgJ7vkfFeFKvEVksGRfhVBRQBvdkmpi_WXxRUFiTIHFY8nvUO0_9N7rYEdRRrP-NsQUs-wsIhpM1d-AjqNt8I1xjk1PEzLqc_txZ8KM-xi4rEb1eMf89ylPGW4eX0Rvcj0CJ89UBuU45zNJ2h3x9wZqcDYz8oukSaTwfH8g73P1tsQ_BDKvQGoqzwD5RGGip3AvmlXuOs8mV-sp_FbYVb45KWOlm4FdF2Tl2AjwQnimRDZ5dRk8bVAwQ6TK32wz1_BBhOUQ2xr6C-SOKZQWszoPk1xc7hkKAgo0u_urTYyCLnGfODcD0AV6TMt93yadUIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین گل‌های فعلی در سال ۲۰۲۶ فوتبال
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/Futball180TV/90261" target="_blank">📅 09:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90260">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26b4bc8543.mp4?token=CZ2GNa256nyNyCOE0dFJ7tqH01FeUezX8N1U2FndsQm2Xzj1D00XiY_TUlaYXEKxDv-v-fZ4lU5WaqroZVzxHWfxNp5fX-K1V0rJludWX5dodwWoiEaR9CxrNwdfCmwxTtCrqskOUaXggtvhpTTYGY6zcyxbtVh0RKKmr8XESO19RzhyjIrQRkSQcC7lNZ4UjL1x8I8SZ7K3zGFITusfDaUU9vr_RlH_lTCL5hSwT6AL7GRqUkVrbvu35B6H9dzeQfZrD2CpC5Ux9-T6wQGRoMcFgnQCdTgPAz_EXnDAi9pov8ZWsbvvJ7PrlpnTpyNoRCYzH5EW291pMyNq1g4k3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26b4bc8543.mp4?token=CZ2GNa256nyNyCOE0dFJ7tqH01FeUezX8N1U2FndsQm2Xzj1D00XiY_TUlaYXEKxDv-v-fZ4lU5WaqroZVzxHWfxNp5fX-K1V0rJludWX5dodwWoiEaR9CxrNwdfCmwxTtCrqskOUaXggtvhpTTYGY6zcyxbtVh0RKKmr8XESO19RzhyjIrQRkSQcC7lNZ4UjL1x8I8SZ7K3zGFITusfDaUU9vr_RlH_lTCL5hSwT6AL7GRqUkVrbvu35B6H9dzeQfZrD2CpC5Ux9-T6wQGRoMcFgnQCdTgPAz_EXnDAi9pov8ZWsbvvJ7PrlpnTpyNoRCYzH5EW291pMyNq1g4k3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحید قلیچ برا خودش عالمی داره
😂
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/Futball180TV/90260" target="_blank">📅 09:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90259">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4b0e0df75.mp4?token=qiAO7dQXfKPHxm2N-9sSGWkeBYOJwOWGhFNn5xDhTkzy341swaosw50TurN8ABbe0FUUMLUcWod7TOYQRSwyzm7pqKHFlj0NcnKXm4QRB3VaATy3Ou8f28OMHAsNBbOe7lqjU3e8u0_WtGN9UUehsx0nSso7XxPkGe35Zes2w4Mn2jFwKqE7MNHiVYdnJF4WXG17OO6t5SSYgDb0YFIFvtvDvjL-EjmN8yDy4pMNDCx3piAxhz5Qn5ntxo5AUNYPepRdKWNG1Xxhu_nod3SUgnpRHu4l1ZLSO3a900LNZqHSXmnkUqknacscSTUSyMMRnRDHf5D62P2obi83hQ6tpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4b0e0df75.mp4?token=qiAO7dQXfKPHxm2N-9sSGWkeBYOJwOWGhFNn5xDhTkzy341swaosw50TurN8ABbe0FUUMLUcWod7TOYQRSwyzm7pqKHFlj0NcnKXm4QRB3VaATy3Ou8f28OMHAsNBbOe7lqjU3e8u0_WtGN9UUehsx0nSso7XxPkGe35Zes2w4Mn2jFwKqE7MNHiVYdnJF4WXG17OO6t5SSYgDb0YFIFvtvDvjL-EjmN8yDy4pMNDCx3piAxhz5Qn5ntxo5AUNYPepRdKWNG1Xxhu_nod3SUgnpRHu4l1ZLSO3a900LNZqHSXmnkUqknacscSTUSyMMRnRDHf5D62P2obi83hQ6tpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
همسر ناصر حجازی: به او یک میلیون تومان پیشنهاد دادند تا گل بخورد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90259" target="_blank">📅 08:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90258">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">روایت قرارداد نجومی فرزاد آشوبی با راه‌آهن در ایام مالکیت بابک زنجانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90258" target="_blank">📅 08:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90257">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">Soren-VPN.apk</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90257" target="_blank">📅 01:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90256">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90256" target="_blank">📅 01:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90255">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBTiS5WFoy-vi_N3SQC-hPh5efUG2_ZcfnGEz5wphKRjUoJqNQkp1I_vsOOEwESox195pd5DxeuujuT4Sl1jgsYLS2XqdU83jNVgfCJJZ59O2kl00NJuA9eS2XfNEAeisWjKNw7AoH1MiVS-nRCDOmy8JSAKPsqjULjhuiijeLqsYlbebgMnbbLgE_OmvAeY_tIR1twaiIHAMMZwIFnT-sgWAe5pNl1ZUfp6UwVS7f2rQDLpz2Ua_DSKBVjKUsh8dRFpMwvnJUgQ6Cm1B4ewcssWCxAHECrqsEL9VWgBcnrC7_ecyn4QcmVGavcY1Fvwxhyr9GBtuZq2QGeyFVm3TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکل آرتتا بهترین سرمربی فصل لیگ‌برتر شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90255" target="_blank">📅 00:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90254">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔥
برترین گل‌های این فصل سوبوسلای در لیورپول
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90254" target="_blank">📅 00:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90253">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaR4wL-x2AgZFse9v-0fyoVC6aHfmtyWMtNvwshb_v0jKKhn1sRybHKTswixQ5addIujABuiqBFL3dNBq3dD9Enzy7pU2oUokWvftqXpN9H6Rtfm1kY3hTASNFp2Lieaj19j-PkAghoMZxF5rYM0Y-QG1-G_7iZxOxoGrS0DHLd2y9RmbYd-yZGKnIu67VrzcvfUQeOGALqM69nQEpPX_3-VGIbgS0XJrkqEciFcU5YJeCaxmIhLkuBCC5vFd5QGyp6qkDWDeKMFLO9Xh8VtY9qCtCVBZcY1fiEYourOa8g6S0d-k3OSg6Ww3mKZh8yo16pCzVWrQJ2XBIhLjaCAFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الکسیا پوتیاس بعد از ۱۴ سال از بارسا جدا شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90253" target="_blank">📅 21:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90252">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea61c87680.mp4?token=LyO91iOr1_Wea65lvlk469cqMAV22PmtPt33e6v7gLvtmdBvJxWIGwCIRw33o1eEpsBx7KdnZLPyHs8h95-bT2PSWaJNQiwZaF2mk_-Obr6kwARzsJFAMhQv2vfzopC1ou6Ugs9qefydkqinzezrg2bfo7mdgx4C2eplmqvame4WMylKjkHMzEQw2K1gaQr_KiiTZOjdoJf6vxomm5zsvifpa2gX3fq5OhKrppYP_ZVsRfTnF7JEHushXLYR_GBtvOR9w0kQYLHRex5R6M81o3DP4welKD6drpiT0A-q-dRmIuT8xIwUPMVSs28hwjNMZJZoJA5D7YFMgNJi9gD7WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea61c87680.mp4?token=LyO91iOr1_Wea65lvlk469cqMAV22PmtPt33e6v7gLvtmdBvJxWIGwCIRw33o1eEpsBx7KdnZLPyHs8h95-bT2PSWaJNQiwZaF2mk_-Obr6kwARzsJFAMhQv2vfzopC1ou6Ugs9qefydkqinzezrg2bfo7mdgx4C2eplmqvame4WMylKjkHMzEQw2K1gaQr_KiiTZOjdoJf6vxomm5zsvifpa2gX3fq5OhKrppYP_ZVsRfTnF7JEHushXLYR_GBtvOR9w0kQYLHRex5R6M81o3DP4welKD6drpiT0A-q-dRmIuT8xIwUPMVSs28hwjNMZJZoJA5D7YFMgNJi9gD7WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش ناصر حجازی به پیشنهاد گرین کارت؛ آمریکایی ها باید به دستبوس ما بیایند!
همسر مرحوم حجازی: وقتی بهش پیشنهاد گرین کارت آمریکا رو دادم چنان فریادهایی میزد که ستون خونه می‌لرزید!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/Futball180TV/90252" target="_blank">📅 21:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90251">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/Futball180TV/90251" target="_blank">📅 21:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90250">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcHx3QLv_MblsUVI5RqS6hcB88xQgxmnhBDYzsqSa5_VFxFOKtYDKhMfJpXZkuIpjO-fb4pUS2ZFwXfgbgomFN_4gitf81SAoGrr14ku5CiHAvVLWCrowkIQwgQkd1mYJVS1hfhIeM15Y19AhmjUVWnqe8-VOzkgEPTDeUGHD9jNt1glyIQcnCKHWJXX9IztYOZqLbA3MxjrG5cQXGjadoKrnbvcORv1p1zrceVVjAqqmNTmnpuY7-x3VYhDtwVAKhkqBt0u8oXcxef_BvV1KPW-7ZEXFeehwT2CZdkSWTz_xl2gPWMmV_qq-vVLnZM329DlUIBDKdzK26v5k_nQRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/Futball180TV/90250" target="_blank">📅 21:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90249">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baad93a3a8.mp4?token=tL59T5YCJkRy-ORceU8RW4fWqogx-Y8UyNTfFR7gEcMUAqJo8kScFzux0BUiPZfNQnvhTNgo502zUBfr-mUr86WDbcbMplqM2ltVzj8-T09nnd4fKl4kAilB-ZNbJDGQzpbFrHL12ouIaMiqC-estukptFwjdjBfZBvMc9QCR9QBQeI0eOk3RHe0iXxhYz--ePwl7XqZiCsjCzHrQP07Ul9NAU5oEb19dsMNGU5xzpXpaKJwIZpJfkRuTatHFWztHraFoA1CtHnJTuqud_ls4u_aGERvmjlmeVAY3PVWw3i0uRM65F07YCleroOWi432jTjHoge0Rn8FYc0h3_xv1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baad93a3a8.mp4?token=tL59T5YCJkRy-ORceU8RW4fWqogx-Y8UyNTfFR7gEcMUAqJo8kScFzux0BUiPZfNQnvhTNgo502zUBfr-mUr86WDbcbMplqM2ltVzj8-T09nnd4fKl4kAilB-ZNbJDGQzpbFrHL12ouIaMiqC-estukptFwjdjBfZBvMc9QCR9QBQeI0eOk3RHe0iXxhYz--ePwl7XqZiCsjCzHrQP07Ul9NAU5oEb19dsMNGU5xzpXpaKJwIZpJfkRuTatHFWztHraFoA1CtHnJTuqud_ls4u_aGERvmjlmeVAY3PVWw3i0uRM65F07YCleroOWi432jTjHoge0Rn8FYc0h3_xv1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ازبک‌ها آماده حضور در جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/Futball180TV/90249" target="_blank">📅 20:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90248">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdtTJlafAijFBlISgrkAfgT8AYCPOWYNl6GPjuKYxVtMz3Uv8Ralenruo-9DVsu6Bqwn2zc6O38D_mmRaOaJIzKIWhlfPFv1utpcUsgs64fGXuBooUeQmT2SLtxj0hguLUMFvoKpPKzyeO3gKX27d7O-emfET7gPUWF28yEd1GcUxnC17aoQRk_iMCLMZLTC8jI2NFTcAbuSy4ChHuSezg_A6RRmU1Nw4Kzy-SBi2Ae92icyNBMOmLB-ktIaE2NzzXHbMFEiSSsidTdrTMSzbmbEW6vuVqQDyqGhOqL3QhSkg7LFwye3fTTcg_em8g4nAaP8AK7cDREu2ZCYQaRyog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با اعلام رومانو، قرارداد آنتونی رودیگر با رئال‌مادرید یکسال دیگر تمدید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/Futball180TV/90248" target="_blank">📅 20:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90247">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🔺
دسترسی به ChatGPT روی خطوط همراه اول و ایرانسل برقرار شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/Futball180TV/90247" target="_blank">📅 19:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90246">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmGsJYIPrC3jiR5Kf1QSBYJJZTaDpw9gu2IRgVoSstmXH5J8_4o3okBdJegif3r42Kp4tlnD6UStk1kGMlup_zqC9U9UVKnYrl3a3AZvkfSM1cFLFpOrNHmyoIjbH9mkZPW5NTi6aGf9Dnj8PMg62kJnZ3Yhy_EBeDSFSI5iMVMqPEuRE6ZzBgloYrE9mqlhIV6RWwC9aNHcSkI7HlQuyt0yUtYquGoYKOmJVFqIejJ4qFDbZPFQkYeiwE9IEl4A-T5y46XKe5fgR3ddw7rWzM-jsHCEvORgrUIGMqPgLp7rhFaRA7kbihvcnTaOqzVl8mDHLbAK-vGcrz7jVxlalg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سیدبندی فصل‌آینده لیگ‌قهرمانان مشخص شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/Futball180TV/90246" target="_blank">📅 19:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90245">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تا ۲۴ ساعت آینده سطح دسترسی به اینترنت به حالت قبلی برخواهد گشت. درحال حاضر اتصال وای‌فای درحال بازگشت به شرایط قبل است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/Futball180TV/90245" target="_blank">📅 19:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90244">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">تا ۲۴ ساعت آینده سطح دسترسی به اینترنت به حالت قبلی برخواهد گشت. درحال حاضر اتصال وای‌فای درحال بازگشت به شرایط قبل است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/Futball180TV/90244" target="_blank">📅 19:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90243">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwN_wJVHbbsrVcSRzJy_VkHI8WPDHHHTie9tjWEk2832plVbqZbDugQlAN9gXFGdXslWH_qwxDsdOdrpOggUgeKPKEQ-lAK5eQkKFNFWJUZxv9Prts8V05wCi9v6Xp3Oo0WoDyOwsYIDWhcVTJoWK86TH4Pyb4RrQiKlymTtyvZ5IclCemMQokhJI0vuhfxn6ycuvaIlgykVP1dpETW9m0GUWSScef6pk8K6rsI2rE5l7uVsOrvvcFgXKgHSdaSuSw-eA3r-_xdqZITCQJfysMTbU8KkBzIWu_B-a6wcX8WSvmTZ6bYzcDE4yrHhRh8Lq8Zy_qqZB5D2YsG1vNwrBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ‌فصل 2026/27 سری‌آ ایتالیا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/Futball180TV/90243" target="_blank">📅 18:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90242">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWGfcCqErxLfV2MXc4ZUq2Fo1ashcI4o0n83b3XAkoCKhB9ow-iPAwpYlNNzoLbGA8J54uHcsoW7GdAeReTAcyGXZ9EKcR2B4_3Csl07e3Qd7RcPqp5vMc2_25FmO4yo6aMIc0I35XmmLBAj4xq1Ade1Z7CLsmb5B9go8NRkRV2K5Q9qJ4asEVGteynKF48382_Tt4_eP3e5LnwNVjR31sPWtlLuolGaWFtXvXmuDdEV9yWob95JuX0z590CRlABB_TRu70yinUogpEHNmtRrFzmsqC45VRY5PLn1ZRS2rNV2htX-RPqm2JwwhZX-omgPZPQjOcXzlk02chCYn8ycg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ فصل 2026/27 لیگ‌برتر جزیره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/Futball180TV/90242" target="_blank">📅 17:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90241">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CW-2GuQZuhOuB-fQTPQmjsTQqJ4NyRdgvqe2u-vPc4UfA22_NF_d4O6F3sJAaXbGmfEZZjOfiemj5sAupR5mdBpzw8PI3KmHqDsPgFe32c6BFtw8wHBrVbDf8411v2MscHItK7JnKgPis2W75ssiAsLO42iWoNHEwa-HjbNH-b1NnKiIGW8_Q-ARB2-2wAFbud3pFhptchbb7uY5-ZHXxwKOWdRqKMEyeSVBkfPS7him4TLd_73Nf2NFCAdul4a-ZW6-w5xdVYLzLyzzIUfj7fUQkcK_HYhYMkgqRup0J0aonB1cztsiwwnMIzQoalo4H4kxo75PZDn5ww21enYECA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باشگاه بارسلونا برای جذب آلوارز پیشنهاد پرداخت ۱۰۰ میلیون یورو + مارک کاسادو را به اتلتیکومادرید ارائه کرده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/Futball180TV/90241" target="_blank">📅 17:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90240">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sakz31z8s2Am45tBLiUHAnhmJBsKKFdHQIInGTdkAtQ2dSWOrAV2Whxzt2AdLHmXySOAMFjjs-7JVohn21Lmn_gdbZp_DXMrnpmGeHsrYlDgSk4MiQqnXeWahdUoNI5YHIMVp1uM4dEvZ_oB-F1pC9iqKEqWDfqMFZVl5HauNglvjCGkx1IPRrPCYYdlkQ7gZgLnOa43hu-t255yaxkY1xcqEkCsX5Jy1CRp0hdnkQV22faMlx73x25giqxN07CRSKCR9KaKsNHsLkxiI_7aT-wnVi7m3YNTP6I1P2sc2OjHDhIk7MYA1OaY3q78uSRevThV64dCd4Ax4nxHvH6IfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۶ ورزشگاهی که میزبان بازی‌های جام‌جهانی هستند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/Futball180TV/90240" target="_blank">📅 17:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90239">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0ebREeHymf5wGA5AeSfdeFMOTNNKSKE0HI_XXxGXI40aJnFOzsZETyT3mUiJvvJFvRJvW9qO3izGUZ0synWnPe0pm2tVVu4VBSK7isgniMYjGTZwPsjyWKEirAwziICz3C9hqXdOZo3bNQLCLvOlWT69V1lKsPUQaNz00fhGM8Md6fa_XtXqC9z-D6eKsaDg3zX4YzMFXLJU1jJ5UHMt5xFdz-aJTNV_nIPxvfFEiFvtT6Jcn9oPpW329Wz1bsGidLFjzkUukX3YZPt2wdm4x8stpD7-mFX_jb4w7DlOpkF_owEJmCKTv7rNp83-39Cqst9nSDvNXf6cK5Ko8OHiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
محمدرضا عارف معاون اول پزشکیان: اینترنت بین‌الملل در دسترس قرار گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/Futball180TV/90239" target="_blank">📅 16:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90238">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مخصوص وای‌فای :
https://t.me/proxy?server=87.248.129.199&port=25565&secret=79e344818749bd7ac519130220c25d09</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/Futball180TV/90238" target="_blank">📅 16:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90237">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsWX1rg-b6oZdkQvsa2pWzLOPvrJXIiKzZflkEq1tORAW6UmDIkTIbI7oNVK_4W9qktNXf8NSbhKJkIwouxwpmoeTQCanV7VmLfpTlpzWQDaRhAa4QQ0H4GFQptLuefXxKENvYrPRjYmFP_Rt0I2NJIRmsdCwbFqz7_Dx0pI9kjWfp-UG2zm7Thty-3eV6gSni49sVyDZWnUal6T58Ehp0B3KoEpOcCr_Aap7bhj-dH-57hSfLgoK1If9qUQabi119LSKhezN5e3fWJVkf6rY8HsuItXvtpuFiJbOfHO2Ob2wIXvmkIm-GHMnMSUvXxGPlC4meRtHj-e0jE1K_FH7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نت بلاکس: نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/Futball180TV/90237" target="_blank">📅 16:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90236">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuqJaG30vPI0ypBMjWuDUR72YoQI6DV--6ZH4bkACCkV-HG_JDlBCmw9nsaQoVvbi-GhAAzbxweza7J0uMRYjpxUAjOgB4cpxy2j-J5F_Za41N9K-2Is6NFAiKbU4g65TocGQ1kpsqCDf8-lb0W-JSioWHADXY4BkQoZ9T1BRF3OZ7jnxWCoSLGoeMcm4x9NPgx3bgLKp-hTdkBve9Jh_NUCO0msNbL3ljAqe6_yUrhgzkhrQX60Ktiq0ol0W5UDXh6I8p1bM_5_4UjDZsQNbxw5S9aMeBf0sswT1H8pTI9xd80yLmLrtdwG39YXFwCJKSrx538T2OCYZTHPl9FOXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور خوسلو در مراسم خداحافظی کارواخال؛ این دو نفر باجناق هستن و با خواهران دوقلو ازدواج کردند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/Futball180TV/90236" target="_blank">📅 14:35 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

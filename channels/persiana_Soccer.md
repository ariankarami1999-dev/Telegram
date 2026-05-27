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
<img src="https://cdn4.telesco.pe/file/uS6TEvX0AbxU5_4YZmbrIq7ZkWqdW4qxEZ5NeWkd99gmsj0ktVpBvCR8-CLPxXIeYF3jhPtBYaNBp4Z17n5W0Pv5sDi1M0Z-MrCjfg6-tUJpxaOgxILINeygu2W5ANrANIqkKhnvfwDCwg1jOL10pfJrYhAwX_WcoF94aKARMQAH3qzizQkHbN3JBsOCRu64qV3XhN6M7zJ_jSElJh1Y7D0u4CehuOcnIh9rHLTTFeuDm2gpyvaKrG3J-4jABfx--m1klgMVTEUBz4OBm027v9mOjU8Xi5T5unHeHYwcZnl4AwcAOpSdS-IY7TMT4dr1CfIhqp9kt2fHIE9he9IczA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 186K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 03:12:00</div>
<hr>

<div class="tg-post" id="msg-22370">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbC3f2WrFQo0EwfqRE6y5nrVy-soXSYL0Xt0EzJMZ7TTfTrwXJfC3xpEQywdhWZh_snOOTquMp0yYJImBsOqttCRINpMnWJKEzZoYMHMUYwl6u-spc1ZFfaKjRHqZGlk_mPf06Aape-7pTu00Ifpv4Elbn3n9ktrMrVVwiwf5D1mFLN6bgpm3QBUR-ruit-OTd7bdPCCFxjwqFuoQZFHAAcV3nm1RjNxkfftk9wtU9Pn3DM4S74zdj_47S6rNtmdaQBrZnpjlv-t-rTpnxZUW0a8jGAmGjrd5UiMKOkpEcECsVhs4L0aaU-5E-nXzul6mWiULX7p2y7OPlw9mVJ5Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
نبرد یاران‌صلاح با روسیه در بازی‌های دوستانه ملی پیش‌ از جام‌جهانی 2026
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/persiana_Soccer/22370" target="_blank">📅 01:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22369">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IygrrdbWIaKnnZpU7SmIkfW7ZAfQCis2tvYU-q2jMjW5hy4jsoIhLSWjG2fCHZgV2G-a5fQ0gVrk3XQmLLVZ3K5p0B7IiBnhZz2qZWqwIA6NTNAyOm6ymT1h2-H2qM6AjFE8lZopo3otTqR3UfUKT-qD5DAHzt9DU_-cPu5JZ8GaFB-n5dZFVM0Q1yEIzL9_WoiqRLwXkXWNsG9Gkw1mKuqt9ODgM_3dD9PHur71yBMTV_xlb3i84KkTXqlNuA5FXwrnXmJ9Qhacc69c-1XJ9bMYouqOkffykyk3fs-N9Ghoso5HwSMZqkDMQbFsVwu8JvGECOmgAUBoHvKqL7QWmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه تنها دیدار دیروز؛
قهرمانی شاگردان الیور گلاسنر در لیگ کنفرانس اروپا با تک گل ماتتا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/persiana_Soccer/22369" target="_blank">📅 01:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22368">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Guw-6r_dZWUsVgp9rE_NdZShdF9GVvZn4rbSUFZYOt1e92e8vJgkf8UEI-uPaCHfw1JJ-H-cueAiAX2k0g4JXBngVY21kD1Hb1R9v3GQViNIieHXZmFhf2upzxPIH7QEy0eWK3B7CxJ67FJ_yqWdvuFrmidtKNoBhDhBGPDBANvKn_fWE_ZAQu4-DMhSYq6qPuoCJHtlaz7fR_R6s_UzB_m1MpP5jC1c-dwO7KdmTFkRAezuBI3c5O8m3iv5znx5Y1oDPIe9LYuGp5LgY8naoFXIrk2k4w49ZpclDaIaSybPEG4Mf0PIdBhI6XYn6nQ2wcDTYnXuOtsJcL7SaePYPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
اوستون اورونوف ستاره‌ازبکستانی و تکنیکی تیم پرسپولیس درگفتگوبارسانه‌های ازبکستانی اعلام کرد که در باشگاه پرسپولیس تهران خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22368" target="_blank">📅 00:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22367">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f6590fb1.mp4?token=Li5SnV8WfkLUNdiBHndQPbKbw38p13AbEzbgo8gUXFkqMJ_HfzOXrHFS4mImG5gC0OFf9ee5rCztONZAzaccyU-jHiLn0EV8XNFLuXewhq4itQy7YPI2f8GZQHVU62E3ImBDU7i0BWplWTKzZKsAPYGFdOpK-1iB6uzIBIwAkoHWNICFkMWvZd-SimEIt3BwmB5tHqbBdixkgY5NAyKIKdmwrJDwjn3q0QcTxZkBmo1Z_H2fG9goc77oV5BJyB9v_xaJfKreOqQe-8UMzY4nI3N2XHRXpw2Ufna5jjYjksHjY1nZeiAoEoZz56Cq1dR-lGt2gQxM0L_DCOXb8LFbLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f6590fb1.mp4?token=Li5SnV8WfkLUNdiBHndQPbKbw38p13AbEzbgo8gUXFkqMJ_HfzOXrHFS4mImG5gC0OFf9ee5rCztONZAzaccyU-jHiLn0EV8XNFLuXewhq4itQy7YPI2f8GZQHVU62E3ImBDU7i0BWplWTKzZKsAPYGFdOpK-1iB6uzIBIwAkoHWNICFkMWvZd-SimEIt3BwmB5tHqbBdixkgY5NAyKIKdmwrJDwjn3q0QcTxZkBmo1Z_H2fG9goc77oV5BJyB9v_xaJfKreOqQe-8UMzY4nI3N2XHRXpw2Ufna5jjYjksHjY1nZeiAoEoZz56Cq1dR-lGt2gQxM0L_DCOXb8LFbLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تعدادی‌از فوق ستاره‌هایی که جام جهانی 2026 آمریکا آخرین‌جام‌جهانی‌خواهدبود که در آن بوده‌اند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22367" target="_blank">📅 00:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22366">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjzE_qm6Uw-sR7yZFeN6qeQVCbzkFj2rvYWHQP3SZ_88EBExhN5QfmOlL-nyFCG6K6CAiJKeCA9DRA6yEfunxYw0IP_XEP4bPlqYwc-53KWkhV1ZogVPOGprU6Yys_YODvmcWoXpCb2alBpsxIiweTyasrvAO-2RqTgl1zAdqmCEW3FUG6x250I_2vEBXYEauVrl06_IGiSQpSiMKdFH9GWjcRrF6_8-vr8HBqnXKVfRQ5sKbanCFI3jhoqY8rPCv2bxy3RY1SAdnpRXfGkI37ebPdIO-4g_n899tpDeQkER8nZmQGb1PqbUh9G3utYvl08A3w3SqL4OGBRf_N2_Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه هتریک متفاوت و قابل تامل کریس رونالدو، لیونل مسی و لامین‌یامال ستاره 18 ساله بارسلونا!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22366" target="_blank">📅 00:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22365">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daYJH2IgPp1YH_BPzLDRId7cheQ386tKPLgwPm81TDC214CAa_YyHxtDjVvsUA8E-gr_iDOa02Lh8ivFMYg82GMXIed0lw_yQmmvSIU1KT6m4bIOmz_zX8g_H6up7cjaA4Jyancn3HZ7WpgeaXPm2RpPmHaogU95SXsQo8Dic2c5U5e-4znic4IYKV4j5ByUrQQXVeErOSKmIZA_Fpv0h0XKTkwG4M5r1nOODjEB453kjgqzs54hyDp1UeKb65OIHrY_XYgCIICKVW5-jlriVQny40tg3zOJ34YMfarOj90GrHohfOVUqZgRMw9IP08M-r8ZCvc1hnu8aT68bbJWYg.jpg" alt="photo" loading="lazy"/></div>
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
هزارتومان‌جایزه بگیریدبدون نیاز بواریز
💖
تنهاسایت‌مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
a6
📱
@winro_io</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22365" target="_blank">📅 00:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22364">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLxrQe-gCsYQdz2IUEf592FjjYMmWBU666NDoTC4spS7SGUgv9YdwAAAPdmFsGBvhHlztjzFdSSJAf5dRCqKCFyg7Nh2GP5o93rhH7TfCn6PSa_pBIvmRuhyOI4NezcLrIUutO5c5JhG4cfnW2WJbN6Rp0AV266e24RObLlypZRw69Y6TXnjlK5ZfVdPHegFzVNG-OfFWjZZuACs0mOXUZdYXLIgkyeHrFExp4MGonJMpYzjSLKDN8PffYwGiXbDgLkkNVkOa_8lLRNEqkrX0a8ubOLFhBvvCNo3aW8c9IYKehBvALpyEdYImtUj1g5tn9B6j2Zqc_up79AZUeGpBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ طبق‌شنیده‌های‌رسانه‌پرشیانا؛ نماینده محمد امین حزباوی بزودی یک جلسه با مدیران تیم سپاهان برگزار خواهد کرد تا توافقی از جمع طلایی پوشان زاینده‌رودجداشود و راهی پرسپولیس شود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22364" target="_blank">📅 00:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22363">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_KLKLdRxyXnlvVrQ_J0XzL0E1Dm2bnGtTe2UqKCCkpYl5bqhFSmjlTjZlDCcnkvC_9fh99Cv5LiQHtETXhlzj9-bEsghXG21OdL_0y2eJ3aPi-zXNSZfFe-rwr7qAiUsxGT1HfAsifpUERl0GMD8i7ne07_HU5bx8nMuF-M9xiKH5s6Cx5I7CvdSaoPNfylMxGEYVAXPnHDOwr-1zle3t3Dkxz4Imy87cFrIZA6i6evZheGmLwGEP7PAuYcKJBa50QJmBUbcx4NP3XHu9LzaeEsrL3Z88xEN-wODHcNDlNa648v0WmSQvTBYhvKbhcWCQG0LZnJ9Qop5r61vVTzYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ بااعلام فابریزیو رومانو؛ آنتونی گوردون ستاره نیوکاسل با عقد قراردادی رسما به بارسلونا پیوست. هزینه این انتقال 80 میلیون یورو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/persiana_Soccer/22363" target="_blank">📅 00:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22362">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owB7IhEE_7KlXugIvpl5eDTXy1e8lYLBwxK3OOg7RCyyq-STVTUEvIw8zXrn2Pr16t07I0JhRix_8nrCdg-FJhvvB9X5V-jHkYjQfmxR1YhWYWJqdBlRSV4_ijrI0X_YzgX5gDwioLdM4pftAILIHkaQuMvuNehrOk_ZqivZUGQMuEqW3-lCYLTJLaWfElpKaADOmPS6gztq73g42nLx8i_IPMfpXZ9eQAJ-sqaxtsl1onjjxGrZbJiXv7hZs8NX89c9hHT3uj2NMggJ1bOioGcsuGX4sR2RRvvf574DZZUj4SVS1ujynOHfDNANRarqcupy_jO6joZT0Ip9_qKMCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ آنتونی گوردون ستاره 25 ساله نیوکاسل درآستانه عقدقرارداد 5 ساله باباشگاه بارسلونا قرار دارد. توافق شخصی بین طرفین انجام شده و تنها توافق نهایی بین دو باشگاه باقی مونده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/persiana_Soccer/22362" target="_blank">📅 22:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22361">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=fjaGFx2g0m1igLXXBnLTxMOtW0sedPSVWWymqfc5aHTIUKCN-HlmQo5-w7ZWGvV65dcplXpXHmLA5RZVp83Cjo2rCPqcmqBbj0iUfCzz6WiD574E37aWeNTSTZ3dOm55t-P20EzBFUVqBJiWmkaTonbQyHSDxhOGpbcyPzzdgTSmwsOvuqPh3aPx2OFRaNjexvztgWaRhHYjsBQRU_RzoKdem1Ia6fPxuULeuUE6uj3FoqDrRmnCJjtYIRPZd9-WvJ7AUq_PBAETP3WZ3vPBlvGnLKmk7MAMqJN8ellxxwxqI9Ysl9-6t5EDkDCmYp7RfrG1MertTJDRYDweSXkYxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=fjaGFx2g0m1igLXXBnLTxMOtW0sedPSVWWymqfc5aHTIUKCN-HlmQo5-w7ZWGvV65dcplXpXHmLA5RZVp83Cjo2rCPqcmqBbj0iUfCzz6WiD574E37aWeNTSTZ3dOm55t-P20EzBFUVqBJiWmkaTonbQyHSDxhOGpbcyPzzdgTSmwsOvuqPh3aPx2OFRaNjexvztgWaRhHYjsBQRU_RzoKdem1Ia6fPxuULeuUE6uj3FoqDrRmnCJjtYIRPZd9-WvJ7AUq_PBAETP3WZ3vPBlvGnLKmk7MAMqJN8ellxxwxqI9Ysl9-6t5EDkDCmYp7RfrG1MertTJDRYDweSXkYxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
از عجایب فوتبال بانوان در لیگ MLS
؛ بازیکنی باردار درحال انجام بازی در یک مسابقه کاملا رسمی!
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/22361" target="_blank">📅 21:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22360">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nq36dL29N7GkQM6dwtBi9cv7-2oXdccHPogBxXjaWOb0NY-Ox88aF-zapYVCJCm_lvfQeRTOwhEvVTey428vFxq6jPi9AKsf0UraYW5PeufG5w3REbOezR6_v9Nv2h3fo9wFdC9NX731QqxQgdn7c8QAwtKV6SjTPmUn9CtzRQVYvKUGOw8DAKn_GGEkvQyNsRW4kl1Zz7Zcc0E0uj9V-8YeCb_kLfgJS9FUriSMWxV62qHrlTeaOFI1X1TIc-yKqe4Hr4WEk18XQxrV1KAJF1CiQP9DuorH-GnhCKey7fIdqGTWKNogG8awpUUytzW16A9R-U1l54YrDU1NAeUMxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ آنتونی گوردون ستاره 25 ساله نیوکاسل درآستانه عقدقرارداد 5 ساله باباشگاه بارسلونا قرار دارد. توافق شخصی بین طرفین انجام شده و تنها توافق نهایی بین دو باشگاه باقی مونده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/22360" target="_blank">📅 21:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22358">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30152b67bb.mp4?token=Da5jkPAF2Ypo79_1tzGKAHdid1cW6UOYjJ5LKcJ1N0iSp7zQjg9Y0E61vAHacLn8mMwxoeIWkEp8GEA3pm7_MzNuQH9SW9gSmmS3tz2oAVlJwmfOLXG5umpwzADlqn7Vy6veouZZP73LFKwWgmVgKDDy9w6e34P8pt4YjKBe_adVELooJNRGw7aml9g6B9PuLBOITdfGbtiYrNSFoakgkzfF8g8qPOXoxHyapSnCSL65gjDrqFSmQSIGIMWjaAt8V4OC_fZOk_0oTnXwSDrLbtszFOWYCzYDe6-XrWtFwahUU5BCebG0erXT7m7Jh1V6hr08TIx2tjNvw8sKSmQNRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30152b67bb.mp4?token=Da5jkPAF2Ypo79_1tzGKAHdid1cW6UOYjJ5LKcJ1N0iSp7zQjg9Y0E61vAHacLn8mMwxoeIWkEp8GEA3pm7_MzNuQH9SW9gSmmS3tz2oAVlJwmfOLXG5umpwzADlqn7Vy6veouZZP73LFKwWgmVgKDDy9w6e34P8pt4YjKBe_adVELooJNRGw7aml9g6B9PuLBOITdfGbtiYrNSFoakgkzfF8g8qPOXoxHyapSnCSL65gjDrqFSmQSIGIMWjaAt8V4OC_fZOk_0oTnXwSDrLbtszFOWYCzYDe6-XrWtFwahUU5BCebG0erXT7m7Jh1V6hr08TIx2tjNvw8sKSmQNRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوست دختر جدید کنان ییلدیز فوق ستاره تیم ملی ترکیه و باشگاه یوونتوس ایتالیا هستند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/persiana_Soccer/22358" target="_blank">📅 21:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22357">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjbcRtSnIUQZCdlnmg5FhIX2uWLOX2jAvpuKLDfHphEEVkuBmk3WQgT05SUd-bcXQiAG-PbabrNuVjFRMWj6k1-jXKKpn6dq6ltL1OZrbxpVM0X0iO77c3poqjsgURssSwB_wqPuAhTu0O-s2qAGdV4FHSeeqj6RAUHu__olLCu_i6R2YJSaw9FfS_liymN0wA7vheQKA3C5AalmC4LXfTJwMmwJXljtkJjGpzoix_CBOc-0DWcQMPrOdpRaLWoeISBNtud4a3qbOjVtO8q8h4vJTdgcV-iTb1gTECuFUshzQ1xO7RhV4GDJY-k3lpLW8YsgUjLZ1XupJvR40yR3Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فرناندو پولو و فابریزیو رومانو: بارسا گوردون رو از بایرن و لیورپول هایجک‌کرد. بازیکن تمایل زیادی به پوشیدن‌پیراهن‌بارسا داره و حاضره‌دستمزدشو کاهش بده. نیوکاسل برای‌این‌بازیکن ۸۰ میلیون یورو میخواد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/persiana_Soccer/22357" target="_blank">📅 21:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22356">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDZ9gkrlwbN3ogcGc-h0mAJlmktl3n8s05UFkcXQzfMRVPzM1hTOqimj8jFyUsyCjLVdSrdghEwAGHr3MLBPtT-KYJ5PoXv0Gp4a8FkQU02tASDudee9QxjQ1de4gzNQp1lQM77KfJvmf04izsnJOqSlDWXRqTXR5vFnr328jfs8ZNFOeBd6IpA-QJrja_bxtibEs7CDB_Ppv4lZExrDqDEJzuIZqezTaR029z3eX9QTEOjg_t1fvEdT_8pbN7WXXW3od-o5_sFXtheyGaflry5tyjHyxKlkH0AiHKINWaVLxfkGtpUkK4cycSThTGuyH0a4m28T0wFxUYXfx4LeXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ آزادگان درپایان هفته بیست و سوم؛ نساجی سایپا رو برد. صنعت نفت باخت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/22356" target="_blank">📅 20:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22355">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwtjMsch1ufA4HetBnHAJ2I2erjg8SNet83wjyhxdvEK84F7ELr4v26mBCEZfc_oIX5HH6VsKtaSQZnNK2B-rcCZYelXrk2KOmfYmvmLRz_Zxc3qLYumXLnvo1gK0JK1iwe3NbTq9BOsWl04w471hjswLqY-bj7ELhp3iyikPBfF1HmCoxEApN-_QyTut9ZSO38uKaiDRYTkc8-L5tTgF89jiArHdr89RMtPIblrZQwWS3NWMpyh42rr_U_6i6hyzrSNGrTu4OuACl59xMD6xAUf3lTDT0_UnjI4z6vvZ1VgrBLLBCVq6dGGZS6T1r2iMlRU4xtz9X90oRLx6OzALA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛‌طبق‌ شنیده‌های‌ پرشیانا؛ دوباشگاه لیگ برتری بار دیگر سراغ‌جذب‌حکیم‌زیاش ستاره مراکشی سابق چلسی رفته اند و این بار احتمال اینکه زیاش بالاخره به لیگ برتر بیاید بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/22355" target="_blank">📅 19:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22354">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rO48vIeDxHM1nQt_NHa9WdjnITW-IaBFNn-AqvsMH4oOjU5u5ZRIC58a7URUCoy6g_oJiLLRTznswg2I5OvgbsDUExZSDsBO4IYMU_Hv1qg1LrMAv0ojJ-EqQvNbBgjY9oPRwFBIgpx7O3UO5-14mkU4r19_RmbfEOSySeF92SjAZkppaUitdNyD1aI100i4Ubd6qECnF1vX-WKabZF7PjoRM9o6n2LjFOphXXXvQyKaDJQiSZDNBYurzBq5qHwMLRHmnE2UPejzJm48clI7a6ckHfVilHZWkuRdSMhJ-TjFuguiS0X2uAza0x3Ah9fiIKU5qWWyjY0U2WPPZV92kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ گارسیا دوست دختر جدید لامین یامال: لامین بهم‌گفت‌دوست‌دارم تو آخرین دوست دختر من باشی و دیگر علاقه ای به رفتن تو رابطه‌باهیچ دختر دیگه‌ای ندارم. لامین بخواهد براش بچه هم میارم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/22354" target="_blank">📅 19:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22353">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGre-FFffyY6HEz8-7It02g8qwFexCv_siPvt_lK9q4g0ipVpEFrOOme9a3ShmKf7Ma05dQ9SdcI1flkK583FjIPVZgRx7rPk-N6w-EZW7M3WvRkVzB37B5qLKY6Jw83tSHiivKDR3k5w-055e22yur-be3Fpovm9OXSyzC8bJnbEh7nnnWmNHKC1em_LudEy5FPcyirtag6gglmb81sBSV8fUUi3Zbh9AKN3Got-dXPLjg9aKkUhAkY8dTj2v8ykryakNhY0kS3Uia9y2qtEYGNlqBR5xOOuhccr_nHQeIl8k6FXfDZyt-OR9dsVeGgjJuXNjoVydNYky8RQ5vNNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#فکت؛ آرسنالِ آرتتا جاودانه شد‌. آرسنال در فصل 26-2025، اولین تیم تاریخ لیگ برتر انگلیس لقب گرفت که فصل را بدون دریافت کارت قرمز و دادن پنالتی به رقبای خود به پایان می‌رساند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/persiana_Soccer/22353" target="_blank">📅 19:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22352">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30945cae67.mp4?token=LFE69C_Auaj0PSfZNzp-un3IzBXsMO4M3mzw8bF43wZ8QVs4WJlUC77xFTQ8gNPRow9MuBggICNVGmoLGpRAvlMUj1DigAytC2bwSX_NjxJCS8RtoqO90XZ10Qjatn17PybQaZxwlJvKy22rFNzmvHXHe_n8qoUqPsFgTcWGw-p9JWgqbaSUl7F1S-yPJeBl-vtHLhr5xX-xJWnqCIZjDfWvS83Csr99RtLBYqf_7yYVfLt9GoKxmWyo085iHuyvd3--tokmjqVh3gwtEpBS0CVHdfGYY4bMxHePN-1WmGJmSshiOIy8EyTowerwzlhRwlN-HNQRJ7Dx6UUQPcc8VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30945cae67.mp4?token=LFE69C_Auaj0PSfZNzp-un3IzBXsMO4M3mzw8bF43wZ8QVs4WJlUC77xFTQ8gNPRow9MuBggICNVGmoLGpRAvlMUj1DigAytC2bwSX_NjxJCS8RtoqO90XZ10Qjatn17PybQaZxwlJvKy22rFNzmvHXHe_n8qoUqPsFgTcWGw-p9JWgqbaSUl7F1S-yPJeBl-vtHLhr5xX-xJWnqCIZjDfWvS83Csr99RtLBYqf_7yYVfLt9GoKxmWyo085iHuyvd3--tokmjqVh3gwtEpBS0CVHdfGYY4bMxHePN-1WmGJmSshiOIy8EyTowerwzlhRwlN-HNQRJ7Dx6UUQPcc8VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
از حواشی بامزه مراسم خداحافظی باشکوه پپ با سیتیزن‌ها و شوخی برناردو با صحنه مشهور پپ
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/persiana_Soccer/22352" target="_blank">📅 19:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22351">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPDvu5rblTQyljMbo9hnGPdLD9weTvUBWoRXaEh4_xMXYecPgIIPGP5NDl3tTV6oxNl5b5TRXOBL_UWkX5Ru9TmW4NDtDzcK1QEv7A6GGpuDkzm5YuC9nqGSeOCEpi4chBXycq9QzP5sUXcBsUieTmtXFHtEEZ_OwgMMssLZdMprKEAhKR2ldYya81zLAzyGAR9Zi4B-beobs6OYmNbn7HKTscBXXdVwV7VCBE7kba0--X4z0UlEa4gIM0raTnbyfPriUhXAfOVsDMYNdEouwq6ECXUFqB5Du1B1XresofPXYmYiNIN0CYqy9QExE7jyESSao5DR8JDTgNzGh4TuGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تاحالابدون واریزی‌روی‌فوتبالها شرط بستی؟!
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/22351" target="_blank">📅 19:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22350">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGyuqKJyYz0W6VtwXAMhgyWJncdL3AtBLpeA95ylnc7uOb6Hmas8DlP2vjm1qidIi8VPf0uxRKInAwkSnGqlIvd_KJxwfkvGneqYvjmgfMOEMnBEPfif0k10ArjY943fidFPpHp8twjt3BXbMWXtqh0qifWipWRkaSeLxPs_Pi9SHbV_Wm4PODwKx14OBRrtfIDQcFYph5v0LML-gMH8oA4ylBWSA1YK-xI09jBQTyNsYScz2bTEnWDGSoy1unGbKyGAju3OKH3WnvPrb5AaNE_bX5aXkyfa6bMEY4XJs5A82J4lsqzIfnoBs6x6cNiYirOm5mvQ8pcS_jqyOp28VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#فکت
؛ قهرمانان دو جام‌جهانی اخیر در مرحله گروهی در گروه C رقابت ها قرار داشتند. تیم ملی برزیل مهمترین تیم گروه C در جام‌جهانی است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/persiana_Soccer/22350" target="_blank">📅 18:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22349">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dt2JHXTTsDq61iTwnFHi43kK1g-p4jDmagEufJT7asW-Mi_qTGtHwjBl-tMKa2ERuEQQMKVvSto8lz2jAvsMwrovcTSQiiik2-1KLhEAg1XOvp271SNQ0uPMSMByiYoIaFIFQxdC2-Ba7gFbhA4blqGvw7H6boM9qEjyaplDOT3SaOieP7JODuMT88sHRBsclE9CLJTMpbmE_ez4z2yeFQWS7mfCu_Rn0ruVB0gbcMjU3LP0fVwUNwStsdXe3twLER5fHkfS_hQcOeJgfkSwd7w6YBpJEXoPOpgDeKxg-XDUw9cuTKZSC2XCkKyZ2gi9eeqg4SCa_g0hpJK-BTd7SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های فوتبال ایران حکیم زیاش رو به دو باشگاه لیگ‌برتری که یکی‌از آن‌ها شهرستانی است پیشنهاد داده که میتواند با قراردادی دو ساله به ارزش 3 میلیون یورو به ایران بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/persiana_Soccer/22349" target="_blank">📅 17:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22348">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d0b75c07.mp4?token=JoW2_AfTlFZOevBwXY_23Qhc-d_tkCYkPxrBGR7YNGSspKUmpLoaCt-YRdXi9f_jjRWzao9r1_PXYEeCt0mIj25i_r43wFRKdTkp-kGolKSlrO71-LjLjnr77vKETkdmE4jQn2tjhmZEI4PY4vB3e1dxnF4L60kEo3mWMgcVc9tYqxjNO5anB1ogG2G7ijMRIJIerksjgon85N9TYOdFK-x-tt_R_gC2XIQFydBLRuuo18OMfdiLRaZ1B80lQPq5IjRXbrEOi4RmKrrMI2RAL7OKtLRKciguQgYjGefKEUP7rQGMrDP-nGTIsRSaCx3x4bckLLKmsAg-EuXLIXhbKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d0b75c07.mp4?token=JoW2_AfTlFZOevBwXY_23Qhc-d_tkCYkPxrBGR7YNGSspKUmpLoaCt-YRdXi9f_jjRWzao9r1_PXYEeCt0mIj25i_r43wFRKdTkp-kGolKSlrO71-LjLjnr77vKETkdmE4jQn2tjhmZEI4PY4vB3e1dxnF4L60kEo3mWMgcVc9tYqxjNO5anB1ogG2G7ijMRIJIerksjgon85N9TYOdFK-x-tt_R_gC2XIQFydBLRuuo18OMfdiLRaZ1B80lQPq5IjRXbrEOi4RmKrrMI2RAL7OKtLRKciguQgYjGefKEUP7rQGMrDP-nGTIsRSaCx3x4bckLLKmsAg-EuXLIXhbKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تنها 15 روز تاشروع رقابت‌های داغ جام جهانی 2026 آمریکا؛
بنظرت کدوم‌تیم قهرمان خواهد شد؟
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/22348" target="_blank">📅 16:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22347">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxlhxWec4vikmYtDbIXItRHSiz_V0Z5cmEqaSJb-jaHg9UIglVJX5vUv-9eF9-PFVIBynzImyDAyespiOMyuw9czq21TCBlAvCijCoT6ATlV8GiL-NnXme0wbzS2sjQCY__7O1yD1fOG7rETUbFUic4Fe_PUHztzvEnDbVu7m6DJuWgtghAmR9y6qCFslhBU7xmAhG_GzRrhMakv7Bpi_tijKzwqqr5TdSizko7Xc6pLyTfBGHh_73-bC9ewLvkYDTyrGFBk1oBRz4hUjzfqiE5_xrgcVvkKW2DGQrrwkblCYyh8Ax6IMAvlEsg_Gx0ztwzZlP5VEvvQ4YgAQE6W9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نادیا خمز دختر خانوم پاکوخمز سرمربی سابق تراکتور: از طریق‌فالورهام و چندتا از دوستام متوجه شدم که مردم در ایران وضعیت خوبی ندارند و اخیرا جوانان‌زیادی در راه‌آزادی کشورشون کشته شدند. جا داره به مردم داغدار ایران تسلیت عرض کنم. مطمئن هستم که پیروزی نهایی از…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/22347" target="_blank">📅 15:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22346">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFH1yJW0WXMeCWizC5LHbFHNVYyzYn3IZ-ED18r5lU4U10jzfAyEoIGgDnACogi72mgkNx5sV_y3_vTFQ25abGR7C-pVSfzo1RbYGlufvQHV-V1fiFM87pygqQywj2e9lgDAXUU6HpacFFxK7wcUGPH_I45h-mJWUssNNZBDVvbS1F4JEJk0Kd_o9iQFfs4Imn2Os_YGJD8vAj7leU94ZaEPleGlv5qF0Cp_ByvM6_IOh49nOCxDHqfTWpKVd1VdOCJFXGEH_oVdcZYJ4dXRE-XBY21uD7MXcLLbQT5_tyGTak1U-7M5R_agr4X3ONjYU4dLRKNX0VeNu1khcOlR1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لوکا مودریچ مهندس کروات و محبوب مستطیل سبز میخواد بعدِ جام جهانی 2026 از دنیای فوتبال خداحافظی کنه. این‌ستاره با کلکسیونی از افتخارات از جمله برنده توپ‌طلا و کسب شش عنوان قهرمانی درلیگ‌قهرمانان نام خود را به عنوان یکی از اسطوره‌ های ماندگار رئال مادرید و تیم ملی کرواسی در تالار افتخارات این ورزش برای همیشه ثبت کرده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/persiana_Soccer/22346" target="_blank">📅 15:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22345">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWBmPe_d4xPyR9oYyMcTBQwdqmszxRcMuoDI-ZSh_YWb7xU4KoNgdEGxBhSakNjRhtEIhqGP0ouHb8bbkQIkgMD-Pq9HVggh5FqlR8bmv4nW4gpaHb5_HiAEfQEjudEOFehknNSHm5kpFjyRa2TClxVAuLjFoHMyRWJe7JM_DwaiCfIdG-vhatD_Su7d6Ysu8L70crwCYeA3BPg7eTqi7WeimMXrxxpnmWoWHb-J9J29jFE5hMeIFicPjkw_AqV9taqfmkdM1bRiv9ym66BC7bT7pPswOxbBE6mejfS2GHokCBDJihg1mVqS3Un787Y19WcNba9BD7osdKoij7DFew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/22345" target="_blank">📅 15:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22344">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXCXlT7yrbtl8LURdqvUcMzlv_cmvmFZiiyBhVbRc0LfM1NPH8LKUKyZj8KcVGxOyPGRG1CcTIwWUB7EI95Zam0rEDXqvvRimCf7bXYNVXkUFExcscncuy7A8hKfOTSAIvYju1UTcO3u7QEu8jPgGUZUiOn6HAngp-D0Q4vtT7Ssq0zN7BCKnLKFr5QhFVQfJ-iVT0-fmPHeqERD03j_-1yxahO1LK410RhXPOvpym6aq1RVYjpQ-pPBnbspE-NyyinZhv4wskO6FcUGljeSRFgY2vPSsLUCNF3AyRfwz5vg88mCoZOv4MmwYV4rd1EZqOUWELIEYHG27FU3-qMyXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکیپ:کریس‌رونالدو از نونو مندس خواسته برای انتخاب تیم جدیدش‌عجله‌نکنه و درصورت جدایی از پاری سن ژرمن راهی باشگاه رئال مادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/22344" target="_blank">📅 14:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22343">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsFjPn8wZNPaVob0Ni1PoAaeCceN4Km00bGrGimnnFvpUFIJAMG5FknJD074vFFVBG5tdUYMVQakX6jOfmvtnHdhvpRIa6IFjppNOcArdoH6pyWn1AiO_5zL7U0ynnsJNNYwp4sq9d8Cw8bhcRnqnSwuFzL3I4xCgQKFsqu1Zbn3HKZNqYnM3dQYWcBg2wo-s3VXCQh2gFatKWKpFGhTFUZKH_naLMmF_f97Qy_5JmiKDciOkGHXSJ8RIHpt2WcPm2QBsiSJKAfqbwkIjrsFerNB7GAc0piAs6ofAxtChFZEbkJhooogiJ4gT9eL_8fLlXDoZm071zfqiqWFbg0kBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کنفدراسیون فوتبال آسیا؛ سه باشگاه استقلال، تراکتور و سپاهان سه نماینده اصلی ایران در فصل آینده رقابت‌های‌آسیایی خواهند بود. باشگاه پرسپولیس ازفدراسیون فوتبال به فیفا شکایت کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/22343" target="_blank">📅 14:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22342">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkSYYhMkm8NaKKzJRoTI-8tzdGeoYnBcIQv3DT_ParqTlhqlOLtLvTbvSnIF4yWIokbUvuG5uZDo2Ivd870WI92W1ghhYFVugWbNWX9chu4PRaqG4Sjvwh-1BhH_8HYgWwNbu0cU3K-oaTHbx0YtQvZIwe_SZM1IreO9RENjrCbj3MIqw4W-5tdqHrkSUwno2rTCpz_YXmxh3nArtk_w4eTqeFommuzSfIbnZNtlj2eigwtgz1pEpLF7ORbnRTYfwuOPpkOV4HBntqiJF6H5IDfJKvDcJEb48z1pUgHbffU3KvT4zQdXdayZeBQozUv_Pu_IT8GvePjb2lX2X9FcrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ رسانه موندو: خولیان آلوارز تصمیم نهایی خود را برای پیوستن‌به‌ بارسلونا گرفته و درصورتیکه آبی اناری ها باتیم اتلتیکومادرید به توافق برسند این انتقال جذاب طی روزهای آینده انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/22342" target="_blank">📅 14:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22341">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APls6X90CjIMH6aDUr50WsSv7BjTTQ5-z7Z8WbwIrTyWAjiRAhOixt6pui_IzqZNrZVdLyCWi_KWE5cg24YMzaGwGthIMIkRLJNT54X1TBzWZJUZIzMjWFUmDgotTjMRJ6hWKDU5wqQ1eprcGbdPGrJ9l6_-oH-yXYwuzq59se9Xf32i-SxFna9JB_TVTtvV0sdIzTxpc4BBiSzLzGivd8HgdCNUB8mhiq8DomR3qEmOVOxS6lmOnAt8pXllcmEjrhdFnSz7yjSo4CMnFIr4D1dr2lsHW8-dMWwRXdD6n___GhJIOGfgXbATgUUm7bgrC1-NRhvlN6mgH8qDT2DloA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انریکه ریکلمه نامزد انتخابات رئال مادرید: دو بازیکن کلاس جهانی جذب کردم و اگه رئیس رئال مادرید بشم باهاشون قرارداد میبندم. ممکنه تو همین چند روز اسم‌شون روهم‌بگم. ریکلمه‌درادامه پرز رو به مناظره دعوت کرد ال موندو نوشته پرز قبول نمیکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/22341" target="_blank">📅 12:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22340">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuwueplFM2VUrEWBhy9N4UJWZ40Bqj9iwWPW23koxL6LVrcP0vege55wx5abxA62xjoqsvRn0ZWR466e6jF2yLwzEdljJs4LEuTrGVNxzWOMNaPKaAnKAHYvnTRoe82jlh-G18c-gfBtpDheo-fj7tmCnNB3vpGTRoMapnQiDGW4k0YXAoG8TIBEDdPluBx4egxQ0MEmoNaiV6ht9VPIaJkwZ4Z6NgQkBmyCWMMv0fOFNVE7pIXOFzqsAFytNzShj0gQ1piaAb62lCiGMZxsGljbSa70k9sr4DV55125ftf-vbESLEt7OUYh6ve7bRneF1qhhOaqa1gPFHGCeMQ_AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیران باشگاه بارسلونا قصد دارند که برای‌جذب خولیان‌ آلوارز 25 ساله؛ فران تورس همراه با 70 میلیون یورو به اتلتیکو پیشنهاد بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/22340" target="_blank">📅 12:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22339">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRr_0rEDfsAwJVoAUV6DIbGZBrsYQRTqG_mkKrmEJYQZfnBja33CEjS_f81hsXuLjmLuoyAdLK-U_ljq7RlnUKlSrs42tuI8K-3gCVKYCbpPhEvPFHNo5C0K8j_SFmWku3Nj2Arck2R6sxWeSfdXNCZMrfZuIctxdBny7oWqPQj1CAc7uIOZwANgbaGEL9VRt674-12Ya5F6NJ1kpWhQlHCAmWUsv5_hzbZ4DYDFlZRg-jB6dNeFuRKeX_gzbeg1Xh4dKgG1THeuMYY_ArIxJ_VIkLLuxAZNrrgF8BtAUE0Sb526ygZtfHFlpUu_WB3Q_u3gYuKT2xiAEqQy-07BBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
آنتونیو رودیگر مدافع میانی رئال مادرید به دلیل مصدومیت دراردوی تیم‌ملی‌آلمان در فیفادی از ناحیه ران پای چپ 3 ماه دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/22339" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22338">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJLgwSA19lJqb8K8PD3nKNiMMSGKWBty9d81x0V98-9AgdzxZZ8onWQhwDswE0ZTdxq3G3zxBIyIRHIujqVq2MDcPuCnLetcxJKkkw_PcWGgOIWLcbOKjpgMBpwina6K83cbQfzPyFKz_w6QmtlTI5L0sHKE_eLyb3Sa46SeKo8TWbTAGHiyVelBGi4dNql5E5R0yImIrM06X1YeEh-Nys_gHzrSlVqtZJL5CAGQqZUhaMhvl9fiFg5di20FtvcgWDxiY0V2hc9UzFNrt_uAiE15qg8q9t-_0bGLS0AglBINS5aNjL2EK0dFTo7M2JLdtNmwb8wxtdUrt9aWOurxtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی تیم ملی برزیل؛ مصدومیت نیمار جونیور کاپیتان سلسائو جزئی است و او قطعا به رقابت های جام جهانی 2026 خواهد رسید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/22338" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22336">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/561656d5b3.mp4?token=c5bbDLSrakzU3FinusH0_i0VBmtWXlzqG9nRfNhANd1QxAtFJ-xCZJvvN-SHVwj_5EmH7qcVJTlMj7K33p30fp0iul6Wau7nvYGM03oAcvGGwAMAtoRpXVzsLFG59J_tCmpEulFSdaQuu3I9GL8OyxOufVBqLVSt4uoeiAwUasKcqI7dbV5Nwi_8-l95d_lv-o45nUuvRaAeGSwkySKw0ct71zfgOrbjcagA77ZgrGP5prdvE0-VnmdKFRkiodO4zIhTsc9AXlozqPhvhIDZDjADi3TalpzgS0-4sc9N408Bs3hU2yv6mkMEpou8Uf4kCGKMbzahpMIc088U3vbYUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/561656d5b3.mp4?token=c5bbDLSrakzU3FinusH0_i0VBmtWXlzqG9nRfNhANd1QxAtFJ-xCZJvvN-SHVwj_5EmH7qcVJTlMj7K33p30fp0iul6Wau7nvYGM03oAcvGGwAMAtoRpXVzsLFG59J_tCmpEulFSdaQuu3I9GL8OyxOufVBqLVSt4uoeiAwUasKcqI7dbV5Nwi_8-l95d_lv-o45nUuvRaAeGSwkySKw0ct71zfgOrbjcagA77ZgrGP5prdvE0-VnmdKFRkiodO4zIhTsc9AXlozqPhvhIDZDjADi3TalpzgS0-4sc9N408Bs3hU2yv6mkMEpou8Uf4kCGKMbzahpMIc088U3vbYUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌از فوق‌ستاره‌هایی که در پایان این فصل رقابت های باشگاهی اروپا از تیم‌هاشون جدا شدند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/22336" target="_blank">📅 10:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22334">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qjcQ6ZYTu8rhQzWkJvfan88qphZqygncNope8HrDmWu5GaR1JPcuLpyc8C-Y2kKXxZtOmTUIM_-Im7gyq8kvq4-oWbJfnzLkGxfvaDvjYupxmZsERXq1geObPMeZk4yFblm8rWvEQq05N8W9qr6VIV8FaKMD2gMI45bVqoDFzoKg2CUsWACa5ybyZ_tMpi6MpqiZEa1o4szP7ldO429nHd4AgYgZBcMJfmJwFQcBvE95A_ApRPJFEf--8F9zSC0epX0p6CtXIAgPu2fzyqOHpG_pDvJaBpjq8agtraXhjuPp6UjYmUBT_MOyDSJjRWEmmhpjOvY5Dlutge3MylVGyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KKsfKFYC6gZWobqJ2ncczuAdB1nMxEfozd1f9eGiEq4u1lOWU8MO8kFcAgVjn_1eJi-YNjUZTGpjZUiQTqPuKgcdxmLekBCxxouO8L84gjmjB-hAsLPzz-1pkWOCxdVFPewu6yL4FNQPpbiyxzyb9IRxlA-ea3O6HMjU3v5w5TJ7bBavU35ImKFAxeGxORJSQtPuYp9gJvJTZYe_I-ZbkmqrDyooiOV5QCHXVxyQeVeMn0-6hEphpONhn_ConI6Wi5mje-0aTPeuu-PNR9BYs2FNPvkaQYVTv-3PasNBtVSBE9VYxhFwVXnWHPDZcXSc51SCLSNHvpkKDrIhpKYLew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#تکمیلی؛تموم‌سرمربیان‌حال‌حاضر فوتبال جهان که روزی شاگرد پپ گواردیولا در مستطیل سبز بودند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/22334" target="_blank">📅 09:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22333">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFwe3bgpyu9HkRx16i_oASw4VAcZEmV0EGfZuWs4vKpgknLLD_eqdIfBxhjNLff2vSgUpcZ4XmSssKBmhFnZBUljzHxw6yyrWR2OD0uaGApDinEkjnUGfiRtGgnttfaAHWYDoGChmbCXXkSySA4z0yLiirzq5vsIApo7YNyACkwM8eX7FaagkAz2vAhKJ7NyeqAy5lVme-Fne9ol0uewxppTVaBVz-T7qSovcVlhZH7pejIhNKmOnUSGg7iOUGTEoz79gj6D1b1TWkdZABSAYyY7QfFx42_Mo5G62CKmtIXmAXN4ROUC9UZTsJzLe83Q3WmPFVBBdLYnKl15U7Tdfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ نماینده محمد امین حزباوی امروزپیشنهادمالی‌مدنظر مدافع میانی سپاهان رو به مدیران باشگاه پرسپولیس ارائه کرده است. درصورت موافق با این پیشنهاد به احتمال فراوان حزباوی راهی پرسپولیس خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/persiana_Soccer/22333" target="_blank">📅 09:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22332">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drspk5_zMHjltM9x6dZ1nCzUkJvb_EK47Zfsn3ntRipDJiaxCQpt4uV29MAD-P5_bI4kfP-Opc37ELDzqBD2S4g5kGcpxEs67T_KmNaHnwEMdxd34Z66ob-3lRiqtK7ZoW2UM5vlUQeD9fnL2oLq4XFuU5IHRqd7k8lNdlooaeRHS2nX0OXm2eFIj0RwamWT6Wr5tpNW16EZyqwZP1lSvBd0FSKe_v2MbOa1smP1QC-nH4tI5l5BD_BGl4MeK5riGKNL3_OFddm5qYPKrmVB8WrFyFbEqeDtUtLWLM3vMGq0P59Ysb4AcjTW0Lep7t0WT793YJqqxeGnEkINQoR50Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ فوری از رسانه مارکا: خولیان آلوارز تمایل خود را برای جدایی از باشگاه اتلتیکو مادرید و پیوستن به بارسا نشون‌داده. اتلتیکو برای فروش ستاره آرژانتینی خود حدود 150M€ میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/22332" target="_blank">📅 09:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22331">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBTgQACfYl_CN7dTBCruiojJH7S83Y8KNhxrA5QSQWCiDksSJhkYqdHVqLxMB6XQwcdglK_MI5YXDqooduH3XtM78AA1LzOOBpk2o2qWdnOXj8rJwD_YFfVxZSlkyMLgT87D0rFHvcFT003r82b8fXFfResjB0sBcb8ICEyHE8RkCCBEt52J1ND65p8G4f4ubBubfHTgZTLtLDtC6CoZuyYjNy23YeLg5Ou2q8MdOb1_ApTfd5j9OPpdv-l1y-dFVR2x7rSg2z9XJONqdsQdvU4Af7eYJ0MY8qC7Wh-zqiwGA9qZxmQ6RlxsyhsshHvkmHe423vO-nlGZknY--GQ3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان تاریخ رقابت‌ های جام جهانی؛ میروسلاو کلوز با 16 گل‌زده‌همچنان درصدر جدول.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/persiana_Soccer/22331" target="_blank">📅 09:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22330">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNZkyQt-csJziWOOxt-vZcsKRMYJzdIFjozjMUXrjoZrB-xmptyw_ICb4mesTjHLfjcsnfRkot0oVfgSLLPTwaj0uGz4lpPTAxI81Gd61jABJ6y_RCA4BPVGXd28VHcBduaFs5XSWKD0Q_PsBVdbiUiw74fS4QgLa2n3MXy1oSvBt4KWi-jSf4muXMyntM1WeQ1gD8texZesDLyTMtueim1krdqakbinqw_SJFi21JqGPRcJOlO-3UqpwTuDV54RP2iBj10g90k1DH7EGSOPpF69UmdCoy2faw0JxsqRYNPiX_SaIbwEot-jlZkcJaGjIBjITGtGLuwSXB_G3jc_JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌پرشیاناازتبریز؛
مدیران تراکتور با علی نعمتی مدافع‌سابق‌فولاد و پرسپولیس برای عقد قراردادی دو ساله به توافق رسیده اند و بعد از جام جهانی قراردادش رو با پرشورها امضا خواهد کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/22330" target="_blank">📅 02:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22329">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oV7vqUDf14BFSbrsiZ31he85LkFLAiHxJv0q4pMe1pYsbhyZRVizKjQvEFkNKoEMyu0X6u5uWGSobnsp183lSlyyVfwuxCqiAXrS5eGi2Z1-XjWwBFcf8bHbZQ2kdDnNL4k4tjEn91U5EoTFLnMguOSGEtdJN-izkH4DqZF6WAkihHTPKl3z4AuB_9uoZiJqWdBaqOnYqTJjLBTgS1QDEhkKoKfNqUCRhhTxZeBTM2AkLVSrV7ZudUtFAP2BhcWkdmNlknFzQWf6vIpzBQUOWEwGLM7vLR8nAxOEHkeQyByV8vDWayWK2iR16UhjFK61h4SXTnNGBzp5rBUlFc_piQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/22329" target="_blank">📅 02:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22328">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339ed28585.mp4?token=r-zgWRamN6_Rl5CEtctaZxzdg8YMYfbykVRcQIt3T6yLxs6UNEBL8QDB8qCjmhCq3SMcaDp3zWfRJF4Q2XTSe1LwZI9a74Sg2usaOk9TWEJKop7FhAw4DM8m6YCbEcLGW6jReoGnj4OGwpXwxZt4tHkc2miQ2ldGprj3iULW2GLMXu7kyQH99bnG0UL_1JrXW1ZfsJ3MNReeCOPsWY1_8egnrFsOyKA2mMlit8jFJIDUcclgIwz7SZDMd-MueEZnzLlV6gfGRtA-wpr0iEjGyoyhxGA5UbXFgD7YC5gJ4FvKHOsTV3SoGeUScllkVXJNZNuQDkEkjaYCDTtIx72PlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339ed28585.mp4?token=r-zgWRamN6_Rl5CEtctaZxzdg8YMYfbykVRcQIt3T6yLxs6UNEBL8QDB8qCjmhCq3SMcaDp3zWfRJF4Q2XTSe1LwZI9a74Sg2usaOk9TWEJKop7FhAw4DM8m6YCbEcLGW6jReoGnj4OGwpXwxZt4tHkc2miQ2ldGprj3iULW2GLMXu7kyQH99bnG0UL_1JrXW1ZfsJ3MNReeCOPsWY1_8egnrFsOyKA2mMlit8jFJIDUcclgIwz7SZDMd-MueEZnzLlV6gfGRtA-wpr0iEjGyoyhxGA5UbXFgD7YC5gJ4FvKHOsTV3SoGeUScllkVXJNZNuQDkEkjaYCDTtIx72PlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طولانیترین‌وعجیبترین‌قطعی‌اینترنت‌بین‌الملل تاریخ جهان بالاخره بعد از گذشت سه ماه به پایان رسید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/22328" target="_blank">📅 01:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22327">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmbepLyRiVGAwaCrEMQ4_9oPD8kpD8YaEzr-loFmLo3Ipbdpt3tU_-UY0OdiJzz3sIGBuTIUmylwxTdPcc97Y2JBxbn6rTiVOOOkhIM0XYyxsNecJh8ZzkqZIbL0BngSfV3SwYksRUU8bQB4XFsOOWrc5OSp11OiFgj-EtYmy_A-EK4mx6mfS9uWFptO-_2xptkKeZhemE18QJXas89_j3VzH2eXZTEJGKasGEnqkTKhTWv0jghGhaabtDFxjs3PkcICCPQlDjm0WoGnaTPveKXQyhUF6INcMsrA6IDRkl3tSeikQpZr5iq82btb4ZE4f_Vh4hCwTjR3vxPzPwaQXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ سران‌باشگاه آث میلان قصد دارند که ژاوی هرناندز رو بعنوان سرمربی جدید روسونری انتخاب کنند و مذاکرات بین طرفین آغاز شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/22327" target="_blank">📅 00:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22326">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdjHbU3qGpeHepSePLZGCKk5o_FsBl0a0EiPPLE56slpT7YIOVlKvb5Gr6rKtsVcPbxfCQnVLVHgeuF6iS_Fd7-Q0sV2hSoNMN9aTReGH0o0Fi9cjXT0VTpjz_XnJdluPrDVmkw44dZYZe1nNOpc8R-dFxBiv028DJpGyhqN5HHbjbYQ4LWH5_iuynmvn_osT7yeEtmQ4OwTpz8nF2UiI7z2uA37IU9n4jUdkj-fxUZyeu6qBtSqNhLnJlMj9CnJHyLcB1H8F5HJD0gsuNJv3Y4YX6NmrbP_0ODUXKGshuOUk6Lhf_bRdzHySon9kkv4Rt_utb7DCfXbGGDTfafCzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه استقلال از طریق یک وکیل ایتالیایی مکاتبات خود را با فیفا برای بازکردن قطعی‌پنجره نقل‌وانتقالاتی آبی‌ها در تابستون آغاز کرده است. برخلاف‌پنجره قبلی احتمال باز شدن پنجره آبی پوشان در تابستون بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/22326" target="_blank">📅 00:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22325">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/437e19a5b8.mp4?token=OZBvGFcmwhv7d_MQnIHUItkIBSqbciSI7serguNN7m4Y4Rlsnaa9ykeXza338_-o3UUO7IdAn3-sxYchnMQnzhzrqAeb7SbymkGgMgM_0vdzyELSbsAaSlQrG2uQW5cqcowI6vclOrdIpzryguUPAWDBxQfMMpjDQh5LyaWJeXLwvKGgAIx14M8yDkgg0olEEFuBbMhPO9zykcLEuHKro9GPwHDDd6Kl48cvINZZlRd8LA3HCJL2RKpJpa37JMBdgi37aTYcxPP81EvkLhMOnH1yK69LTRM93xSvpDFChs6yUL5hGM2xiLU1fi4FO3CUxDlOQe9tsCuPXv9dVedsRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/437e19a5b8.mp4?token=OZBvGFcmwhv7d_MQnIHUItkIBSqbciSI7serguNN7m4Y4Rlsnaa9ykeXza338_-o3UUO7IdAn3-sxYchnMQnzhzrqAeb7SbymkGgMgM_0vdzyELSbsAaSlQrG2uQW5cqcowI6vclOrdIpzryguUPAWDBxQfMMpjDQh5LyaWJeXLwvKGgAIx14M8yDkgg0olEEFuBbMhPO9zykcLEuHKro9GPwHDDd6Kl48cvINZZlRd8LA3HCJL2RKpJpa37JMBdgi37aTYcxPP81EvkLhMOnH1yK69LTRM93xSvpDFChs6yUL5hGM2xiLU1fi4FO3CUxDlOQe9tsCuPXv9dVedsRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گلزنی فوق العاده تماشایی و دیدنی پسر لیونل مسی از روی ضربه کاشته و یک خوشحالی خاص
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/22325" target="_blank">📅 00:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22324">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAESbDMdXdhAzX87hOT27YJUV9fTPENaG4gJ_XubcUlyfGQJSkRyOxV3bVxf9QMjBDvcs5zvMJhycnfrHnhGXZT-sW-u6CpOiOdxPxvLt6xcvOaJPcWDx1pAVLGqDK63sQDVPRcZB0lFQ-kMMot4O-pqYuoYw3f8g06JGYmpKL9krLrxwVWszJ43BwYUdshI-iaFpikW_AaQGMfVbf28Q06_TYEZUHawFltl9766ht1sq6z8qyqePdxOQS7adv1wPAeK2uObdldzbsqdnGYU56ae_EsHNjAu1HD-pENm_0m8Cmduwmp2H5gQYWaxsz0upwGZWwaPMLq-PuPAkmQ0Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باتاییدیه رئیس‌مجلس و رئیس جمهور؛ اینترنت بین الملل مردم ایران بعد از 80 روز تا پایان همین هفته رسما وصل خواهد شد و نت به روال قبل برمیگرده. ایشالا هرچی زودتر همه 70 80 هزار نفری که همشون‌جز خانواده‌واقعی‌خودم‌هستن آنلاین بشن اخبار نقل و انتقالاتی…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/22324" target="_blank">📅 23:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22323">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDR4M61Cll2SSF5fRIH0eDDow_CqPUFfA_siwy4m6CCkASk0SOu9m0nq63fZsP2FJEbklj3v4UqPvkZ4LXlwxtfhOola8DhSzB4MI1sSaRVsXkvOXhIWUh1UlboeSXMFJj-iaZPmuxPqijsMWeG6d-xBPGGXle4OLdgVTHOqlaKkwmJ4LXbSpHoZsuUfHljhIdMyWUTqb2qFg-lfEsCn21z0G9739dHck85g8pu93eiLn2yNmcSd8cgJFk2W2GK2Ry0RzsydNTkuChkO2hQTS9o4XgGWvDbYzvQJiijTfNqGjGwacHgBitPCNDW0TLOteOYw1C4p_1gXu-McRhTDtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معاون وزارت ارتباطات: در پی دستور پزشکیان برای‌بازگشایی‌اینترنت تادقایقی‌دیگر فرآیند بازگشایی اینترنت‌بین‌الملل‌رسما آغاز و تا نهایت24ساعت آینده دسترسی مردم به اینترنت به طور کامل آزاد میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/22323" target="_blank">📅 19:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22322">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZhheVi37pghrszH0ginqEegr-m3OA-YJ1h0XR73shQs3tWbvy7Ssx7g9kPMHvJpHdOwzk9aRLUQoi3HtX0lzIU0bW00KQutoJe6GX16Gq1X9jAaVf-fEkxYWdfpQIvWoVqw20A5K0kLpKx9zLMAv5zS8wc-fozTPSWSDzE0isJ6XN9Jjk49WvrMX2k6gUehaI-ihNO9zwndYkNFW4nXeFZN0g8VuUnGJDv4JgQuzDQThBzG1vyJxXuvD4RceoLiYuScDNjhwbD9s96BoB9O9FSeYGAHSRCvTFAPQ_8WzTjklYC11VFSgRHDfgSeYHLi2riFMepxyqpjVsT4GNucTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معاون وزارت ارتباطات: در پی دستور پزشکیان برای‌بازگشایی‌اینترنت تادقایقی‌دیگر فرآیند بازگشایی اینترنت‌بین‌الملل‌رسما آغاز و تا نهایت24ساعت آینده دسترسی مردم به اینترنت به طور کامل آزاد میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/22322" target="_blank">📅 16:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22321">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJW9xaIJCP94202hfz6yF4229Cma8ZZmEOBB2QzysLwYepYdJvACgGTzlPhdfEYP8ttpzGrhvKJEgHcpWJaZ_Rlq9Zn4Rsm-M__2V_NN8V92Rh45dNJ0aWrrHWHnEbzFmLHs84wN2Ovcdd76S2bcjfZn4hWjtNNm4GnAnwCVQD331I4jWGkX0g7cZ367_bYm9Jh1QfRGJvmWFP6JUKpnXwtdlKib33S5fpAWHnIeLQ_exjjEGPYmfHVP2F5SV2C9GY8_tCVwXNH-3HXOzgphkPQf3GoKBh9KJgSe8riYvLtzJSlAZobTytkytCRqYdBHqOYQzJTsGBriqn4pHXjICQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ بعد از ناکامی تلخ در گرفتن سهمیه UCL؛ ماسیمیلیانو آلگری از هدایت باشگاه آث میلان برکنار شد. اولش خوب شروع کرد ولی بد تمومش کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/22321" target="_blank">📅 16:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22320">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2231444b22.mp4?token=SBKGIfz3hpbAsE32sv4y_YUTlueJAQ8ps_-O6Wqo8pW61qzm7hLk-LLGAtXtghT3CJ3m9v8UzzJfVtie47CSW2qHrWiu92z5xvp7eWu4MbpGvle5_f80NAiFuneC1iFpqgnDtmk8-jnmjRK2KwKAW8HLF2RMOHUyNh0yrvlSFQZ6GIK4UhoJc1HoHJwvNkQTwA4fs0_pqe_LDlrWZ8fzD231hj5Hfy9T1RdWcp4W7lCo-aDT73v6SwuzvjkkK4_60wNlO4SpzW5HEw9t0u6upMLj0kmwDoPEnRRn7GB6S9OR0SdllcR0J4yV8N3Z0R9wt2pEiLKyrQdYuJ6Hwr7GsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2231444b22.mp4?token=SBKGIfz3hpbAsE32sv4y_YUTlueJAQ8ps_-O6Wqo8pW61qzm7hLk-LLGAtXtghT3CJ3m9v8UzzJfVtie47CSW2qHrWiu92z5xvp7eWu4MbpGvle5_f80NAiFuneC1iFpqgnDtmk8-jnmjRK2KwKAW8HLF2RMOHUyNh0yrvlSFQZ6GIK4UhoJc1HoHJwvNkQTwA4fs0_pqe_LDlrWZ8fzD231hj5Hfy9T1RdWcp4W7lCo-aDT73v6SwuzvjkkK4_60wNlO4SpzW5HEw9t0u6upMLj0kmwDoPEnRRn7GB6S9OR0SdllcR0J4yV8N3Z0R9wt2pEiLKyrQdYuJ6Hwr7GsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
#فکت؛ آرسنالِ آرتتا جاودانه شد‌. آرسنال در فصل 26-2025، اولین تیم تاریخ لیگ برتر انگلیس لقب گرفت که فصل را بدون دریافت کارت قرمز و دادن پنالتی به رقبای خود به پایان می‌رساند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/persiana_Soccer/22320" target="_blank">📅 15:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22319">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbChnzKyUm9YqGAsuCh3_824bm3qd7VKg64-GQKLkNCuXl2cxy5Y0F4hB3XiLHCAhuyLyYawx_tucTt1CbRbOCi0CfoxGLTekMmdRb1o1H7lwBJNDZLJwNsjsbG3_sYB_Ncz6jCWOIDRm-d1AFtkUUyFuGToFTuY5Kt9qBTFM1ec6-YJFx-tLNBbY6wVS2LzWQKfipWjnF4WqrGEo9_4AJMRe4eGZkAQqkZg-HD_X8QxV_VOFZ7TtlGHaPQnc-Tdz6sbNPeCj0Y3B-U8tMjuyBPc4Fnrp1Gr-Lerkcm__w51V6-Nj9z2kKAEsow2XCcOLGJ4tJ7icXWjMFFAroSrdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/persiana_Soccer/22319" target="_blank">📅 13:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22318">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqjkfEt_xOT9-6g2y58OFBDZ5TLZASJfV4Kz9QwFD-STZ1KucZC6hZ81SCRk7X1vTlKKXWEtewKq37c4ltMKqpom634xTx4Rg5CvyPvB8eWuHy1dOkknbTYITWSD6Atk25lVe57xwziCyYfuQBfAWmWv78dYzr75Z-QlW_bvDsvaAGvaONcVrjGJOKHddL5Kcr9QwQ61ddXDU-VKnDw7GKH_U4hLufkMJFy8TyQ-WpTPTSn-h0j0ZvlI_33TKTZMfgCnh3wcpa5iLATVnoUHuTlG5uk2imVofUJtRx1h2sjPp-YlqJF9V1siGOEpaL6kHh1TMApitJBSvlc5yAkLuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛مصاحبه‌جدیدپزشکیان:اینترنت مردم ایران تا ساعت آینده به روال قبل خود باز خواهد گشت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/persiana_Soccer/22318" target="_blank">📅 13:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22317">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKzssiwJAI0pAfiMqwtqWIVz7DUgyUg7DybqNPBOjGacWR76kzXdnPKO5ROF6-622F117fIFIY8NLW_ChIEC2kjmdI2cC0998cKzMQFQVu0eqGBga1oddgPUyP6NsU0imvtQms-Pu60sc-mhikOJvxR78X4fELFsks_OIgaXsnXDlNm_mZs2aHERFAS655sj3WCalOt6GQrNlWPJOIBtjX6geSm_0EVBq8shal4SN7dSZnoum-tjMZrnLxjLfLlCb7wtd4A1U3jyF-qw0NE7E9EYv90TfqBXJEGcgZ6QKAxRwfxEUFK9-XW2NK2L66pMFZ9kYkaslNZjbXGH6lAZfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه کامل‌های مسابقات شاگردان روبرتو پیاتزا ایتالیایی در رقابت های لیگ ملت‌های والیبال.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/persiana_Soccer/22317" target="_blank">📅 13:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22316">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQ7sbzoVOPXV9Pp16WbJfKPxDT3zCYkkeUvUdXtxz2JpDcMRxiJ3eVgZEUsNR-ydvht6OKCgQmk2Hf3Us1r2V6o6kHaxX1H78x8P0WTVXPY94-XiE_PaHbsFUjvTvVvEMCl7cNj1r7SYcgcf_V27nQRnBTfECE4_61d6LcTQjnr-HQ1WAavdOEx3FoMZi50pJ_M6lTXsdcZF1LGcrBsA_RxqT_tWaNo8Dmd64Jko9ixiRlndmZNQAZBouicJ6OFe9h_jd4ME2jDk0gXuwW17Xyktgm3McB_yLXLwSNPDt2KMjiN3CxzhGzhc7xp1OqHKrdas5eUB0MxOrU-9s-BuUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇯🇵
شهاب زاهدی که علاقه زیادی به بازگشت به پرسپولیس داشت بعد از عدم تمایل مدیریت سرخ ها به‌جذبش‌قراردادش روبا آویسپا فوکوئوکا تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/persiana_Soccer/22316" target="_blank">📅 13:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22315">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lICJPxgpsVBnWVMbovwHH8nwYrNdWs1UbthEIkyV7M5PPyhzRc2zbewyh7vH3RwV8qRDzRvjmjhHhA5poFTKTQH4wm5PiwwVvCFVWKMzx9KQUJ5InC4Y-dnQrz4jD63P3NdBuE6lOL2elsVljuqS_x1cRe6SslmXRzl6YXM5jmwdQMGxEMptEYq7X-OIna9pcBpbqTWwYjihGadhvWokCxNMPBD-uYpyMzvjU_1SpXLwllbjhV-c0mcquw9zs2EwjPBTFtIVQgT8pDkMxMahOKnaHzBI7KwaVbQZ7oiVIfxQbQq3OB1cIr2ylpWo-eg7-gSua62TuYsZimlfQpxCag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی تیم ملی آرژانتین
؛ لئو مسی که درمسابقه‌اخیر اینترمیامی دچار مصدومیت جزئی شد مشکلی برای جام جهانی 2026 نخواهد داشت.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/persiana_Soccer/22315" target="_blank">📅 09:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22314">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3S_kq2cXxhb-REOMbjPlnmFhP0nx2dy6tgCk6i_QAuj0san8sy5ZBfpDGJFRVNdC1rW2AqEQmv7-gxa-SvtEsf2nQyWyJCgfd1x5wtVdhT0kafHX8WWDC83RM5mz4qZuz2CCX1ev3AltvNTz_C0QzuuliYyKfb0cNUzdEw-moLiZfMkLLQX_Ga7oOGht0PKnkaA2wTr5WbKHLkzG4ieZpqbMESAEY-FUhRMlCRBy9NQw1mXpSVL7uL91mG_rr-5R90Er5AWq191E_xru6CM8Lrc5lRslvS89aXwdzIA3hXQoYgs1R4KhzG4NH65T9b2dheRf5wF3H6mPtCgOC6ZZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛نماینده‌خولیان‌آلوارز: اگه باشگاه بارسا با اتلتیکو برسررقم آزادسازی خولیان آلوارز به توافق برسد این انتقال در تابستون پیش‌رو انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/22314" target="_blank">📅 01:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22313">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ndh5LBh-T9nlJjOVDQeOLqfFyCCYrk4JQwGe-AOkE1lb7C5VdzjCK3sxapm3Vdn6NmiKZ0dqfwjQDqLgNSWK0PujYnUjYpdyvCkjMl2UJZRi-RENIifFdOqA7C5Sj7gC6s2AZQ_f5XkD7gxXXSxoYutyZdqEYWBrQBK-g9f3Vlr_mIWCo9O3WSDhY2vA5APz5kyQPhLf-sT0YmDQNWyntpF02aq2mOWZXyncQrYkWbhwxvOolIP7lXteUnyzrl3ik-Lmq--LM16r_2SWW1wMJVYGfhaj_wglhGSsO0OYKeE-diHVcAy3KToRXbu6mTMda4pai69wpV7urntiTQwfdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ طبق گفته رسانه‌های نزدیک به حکومت؛ اینترنت بین الملل مردم ایران تا ساعات آینده وصل خواهد شد. انشالله این آخرین باری خواهد بود که اینترنت مردم عزیز ایران قطع خواهد شد.
❤️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/22313" target="_blank">📅 01:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22312">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQs-o317L1qOArIyN5Pj_Y6rLFXpMCq63nSTLFkBUf35HIYL_y66iQhokXKzYLIzsjpUQsRCUC9qZzpJNXuCWbMOGFrKfolR0xEXsUeArW5WMIME3c5ollJAaQO6wj3h5mAQaMCH0e3TMQ-_ds1up5yZVX0B6S0t-7RgBrkPqhtmfFjLiIOGSTOdgaOVVYhABvrg_Lz2Qq_cXcLhTuFyuqrRx6aL5bdw3CmDgssDyp7u3qdLytNW_OZopf6R2m3DOP6Edd2r3GgKjXT7c0OY3290eRjTc8Y_WdLjRRti3_yphBHjCIQWiG0WyAgmsOlMGRYhqQyQMeT7X78tVihGUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی ؛ خبرنگاران نزدیک به باشگاه النصر عربستان:احتمال‌داره کریس‌رونالدو سورپرایز بزرگ ژوزه‌مورینیو پرتغالی‌برای هواداران‌رئال‌مادرید باشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/persiana_Soccer/22312" target="_blank">📅 00:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22311">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWqX2CA5SY75FFVdAJGBaPMKVdT5_4WZX14wly3PWi2NLnEA2jFaQsqpeSy8kmkMQhMRYDDgOuNBGGYcR6bEB4mjXLZzmk8WAaSmF6c-8LUKgcbljLOlOCj1LSQcOVOOPrjSxf6-BJggtiU4p1-ncAKk-wmVI66BzGfYXQ3vsNdPKB9qDr1XFIYhIkbKXL2pxkymmFO0mNTEeKoTBbj2kY5kiOT8kLUtLBpa-GX7Knrgxj9tpgk0ild_G0iUmazASRL0ILiCpu4ykV9c6srieNRxdV_5Q129Myl4xBuADDHN9VvyOcE3Fo4CDrxdL4JLnhCVVS3FdvCYn4IJZw__mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/22311" target="_blank">📅 00:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22310">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9ZG9TGsgj2Wty3yJO45Rhq2-XjuQ5whoAExEtBW-Db3HZe_HzMg05BQBVBNuwueAK6SNboaBTCZPTe1fhL18hIJw9dyz2NkEfOWMHhGhxNpARBxII9ZsFyPpqZ0RzQrMh_5c-H_BbhHqc9VL8gpCdyO8lHRLzuWcuuJXRCd9ILVSlUE_h37fkgBDO_itxNxi9yTYtiWRt2bdQTHbYUoLPdZfrpIOHb4fedG11FTe0ihz015vH1KpJx-wrScsPtAyVtXmBPHh5a4ovtFfxFY-8TR1DTNd3tmxLDINC7kbWCaWmD_L3OHrNyB4AGsWX4z8O7o6WQcXyDJkLSOxZxoiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/persiana_Soccer/22310" target="_blank">📅 23:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22309">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8B2qcm-uzpwnIfyT0xwpL6Jctctv__-Ngkpu5zwxZ1f5SctODlQA6YV-JhGvVuoInlaVeNcD8ariEZuqADUpc7O5YYRVsbFAIRQdBp73l5DtPKSguNpTFNs1Alw9487Lza1XXH9__Hu8Im0lemNxVQlePml6OOtNMlzpOz0HNvObILZx1qbJCB9OXzojPZ1TJ0QYsTCN2S0xcoFq6EibuuAFwhSIzhrfVGNMHhHkc1qU5NiDkVh2uVGkITSgPIgbP6dusH8P0l0LxGoazG61puNgR7JCAGLh7ksJwgnvk_ihhySxT5bWCR08oiqgUzNdcXbHF6mOiHWgl9UmZ5nfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌سری‌آ ایتالیا در پایان رقابت های این فصل؛ افعی‌ها با اقتدار قهرمان شد. آث میلان آلگری سهمیه UCL رو هم از دست داد. کومو با فابرگاس اسپانیایی راهی لیگ قهرمانان اروپا 2027 شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/22309" target="_blank">📅 20:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22308">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_cKyID_WmgU91JUi_iEMdyIkxRmShZAO66vH8NAla3W_Bb-QVDMG9wbUVSZWqzRDFlYEYinRrK_jb0P4w1q8JVM-Vs8VzjrKx3hE8prduAER5oDxTCM4CgZ33ZeqG1wbJaIR5VXMmfT9oJlGUk1FWj8BqE523mQArG98UGGRyfZxwex1qZAwEkil-uA-5JCKPIhVLTgBa9P1CeTtCZz-7IjLsI4uVjMghucLz9dvHs6vDNg-9KPBfjOw0-rO4WAr2dswPsPinFn4uHNlSFMZmpM2mnPNwL5TLGNFfVei8nk7ZDmSH7RDWTFilVrlHn4MfxRfe930BvS7ba4otmkCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...ایوان سانچز ستاره‌اسپانیایی سپاهان توافقی از جمع شاگردان محرم نوید کیا جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/22308" target="_blank">📅 17:32 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22306">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z_vdAbmtITtq1broo2mSAeYsBHeYQl1pz1kffvZZ8_BFGCpI-FVF-vtIzCaLiLn0U8KOxng5DkwaCZUNTxfLtCPaCrrXR1r6bVF1GP4vsdj96VFp9tgzGhWTV83wWH20vS3hzRh1uMsp9-Zl1C220tVIZ1TriDNC4F5O_GLnMldK1ssWnabUCFOhLgwEcjpQ98ogemzxQz5FfUOmEpzmxs6yQ6F9OyPJmMBACaA2rb_8UYRqVI5MAeoD_bdt0CczyRFwlCN8c_VT9RFuD0GbrFzc0QuaFkMrF3s16zkc80buNJ-nK0jxe1Swh5OSZch3F1Z_0AwD-lX2vzdZWs714A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YpV6COcVVY29Vvb7PazjjlFbD6EqCGnk6c9OqUuNMPs1dmedT4z2dCmnVtsjJtjma220_KWOsImuphN1psXfrAGheYriMMf3rrJrAbmSLBSI81ILiwg36KYW3qBGZCpctHATmyci9F4KlUnaoLJQ5lfFx6y0X7Pg2b0tOVgbBomJ2RaIpg2vRdEDMfotIfJgbWh4ueI40-79SRiYIoPqOK3tWHkucYwRk7xnYazWHUjvTg3P5GVs_x3Zb9nug8whbNPm0CE1YlSMfFn7LqaNj9hPvdGM5I20o4B9MmKuEAzYXuLeHnkcGRrA3pTDSg_hKmm0e9YMWPIJRCozffCkOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مائوریتسیو ساری سرمربی‌فصل‌قبل‌ لاتزیو راهی آتالانتا شد. جنارو گتوزو سرمربی‌ سابق تیم‌ ملی ایتالیا با عقد قراردادی سرمربی تیم لاتزیو شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/persiana_Soccer/22306" target="_blank">📅 17:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22305">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqMeLkY08UYohhdAEZpZSe-0n9uusZfX8t-SgO104STJmJ0oqglVM45tSsjiQs-a8GlCpWB2pUPg04zGDr_6CgZ0xTj9yV7PsRrjRTc-RnujsyUnNSHpN_37xus_JPCz4xDSc4lG-CN3GhA6B5qSrRxE6ORiO58451oSyXXPdp15MUBzGLU3GUNFocrk-dWbEuLx_ISOvQh5K0WOFNObpRkE69WQCGT87ReyMN0ojZNW9urRyikYZtGIfONWd4QKcPb83hnOowQUx1wCB5Ag9WiZTbLyQ4_Usdxcgdn7ksHsMBIFKmc049Hx6IKUJChlGr88PZT3ecZZP1TKJ3q-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سردار آزمون ستاره سابق تیم ملی شب گذشته بین دوستان نزدیک خود: تا زمانی حکومت جمهوری اسلامی پا برجاباشد نه‌ برای این تیم بمیدان خواهم رفت و نه پام رو تو اون کشور خواهم گذاشت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/persiana_Soccer/22305" target="_blank">📅 17:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22304">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDXxwwxgGCxYgIk-mHzIIZkp9oJWOjaVnHcUlutDaH-H2oWaO0aC6KePcmU3v0-Qex9qhlYF6P8I9Q5FnDlrdKgy3uKc-wma9b5DPon1amhqbWCB6820aaz46kooMjQRhKzQBh6fQZm6jA3G3HvmcXAoPRdjvAZcON2ihv4uEc10N-IhpMMa8cE2gtlLY0YTKohoPhbD4J-mhTfq7du1x61mE6jRQNe637GWjjgzXx4yXo6DBSUZQvdcQazeKA9Ik3JpO7iXoHEj4u2Wy1mQvJJPajgkus--a3W6uCU8uzXmbbrpck9oEB4qpcJDIkdExf5KQo7a4nDFhMy8YptNjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... اوزجان بیزاتی مربی جدید استقلال و دستیار اول سهراب بختیاری‌زاده وارد ایران شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/persiana_Soccer/22304" target="_blank">📅 16:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22303">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N65ebFxzM6CjLqXGMb24Mu7zPtyg4MclJCZ8WRDuvB5fZMvNqim0gTemoLw6KKsVae5AND0tZ4OIVH63ANPMaUascN-VVn2YB219CYOdqjcbuOWl6ug9f82wVFg79rxy8-jBKmjMYKu13XbKaDUTYh7nwUxCLdVDtfTfcnvt7O3Jh2SJoJy_5BBFCLu8d4X4VGuWcqwj02f3kGbdhJAv9NR5l1tBVdr1QzK8tqWYZugSmdR8GdaMawMJLxz_2gyJ-Mpc-eCWfC7taVuJ-1dRc_WBaURybc_Xpa6_24zNAUPUevI0h8mV0VvAyuyFXphO4FvBL20z0lZXq_0CjIq3pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باتاییدیه رئیس‌مجلس و رئیس جمهور؛ اینترنت بین الملل مردم ایران بعد از 80 روز تا پایان همین هفته رسما وصل خواهد شد و نت به روال قبل برمیگرده. ایشالا هرچی زودتر همه 70 80 هزار نفری که همشون‌جز خانواده‌واقعی‌خودم‌هستن آنلاین بشن اخبار نقل و انتقالاتی…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/persiana_Soccer/22303" target="_blank">📅 16:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22302">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeIkXTn-5Rvj8chKEWDPlUH32qUl4ee1KZL7RryQqLtBQCpQ5wQ1SWni-eQUUj-vZ16ogmRoyaaBano2wgXPKNh77EggZqBRPc9FANlzmcQTWs3eWZl4J9SqtAO_Da4r1Zjxwfiw_j6lMgEp8I8SOvxXfQm4_VDwtCqjg0GV7KcSTrf-7EH9YKfeeZaib2e4RXk8fqSVTDbIV4kEFKXRXS12gQjhJQNc8rPTSiJrG88jGwbhomsJakoop0wPPm450V6kIMjtcJhD8BUea7IydxUHVUbX2uMcy_lwwzT_8BclxzffMa94NoHxZO87ox_zyo7-lrJ0LhuP_6PYZBAgdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌لیست‌نهایی‌تیم‌ملی‌فوتبال اسپانیا برای جام جهانی 2026؛ رئال مادرید بدون هیچ نماینده‌‌ای!!!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/persiana_Soccer/22302" target="_blank">📅 15:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22301">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I84Jex-QH1qE-d73ZMDtSKQmX-E1n9ubA1-Df1IgeE04W66C6MzBM4JJA0O1blO9EKckVcC7s80RDKzoKLtOxdOrcP6Cka6aKutuToa9CSFVh1gmGo6iEuE7HBNEvSLyx8ldGK1d1aY5Oz_VwUffq4mSNdrTHPgwS5h83mVwoKmLAOKqQ5kaBQlF5YKs_c4FECI8hM-GoXvqzwB6EjiJmQSV0FkUtrLvmImMg4LqFu17s_l5S6KrmzuZgr0ZpjvLefZWfkC9MxKwDG4v43Vt4stetLnlQFLUn4Ao3AOLCjC4uWRCsLJncyL_oiv4hT28H1iIfV0XHQjHvM-pUM50ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/22301" target="_blank">📅 14:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22300">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcxEfGau-TOpujuJG8s1jhQAiKHrTRFHpem6pvqdR1hpohLYLhrXKNTkiNKw7PTbNWgR1hujSV4pOgyXrqTpT0fB0MTiVQo0pgw2q64xmqjllRzz63qXqMfZF74gRUUBSxQ2cysQeofQQA03IP555yBdxcQ7YXoAlridgCW7tuDWBWNEFq9ih3thXgt6Y8dCSfNQPAYVDUDUWpBAch4ZvnNjGkPSnNND7NRlTxD1b0dRivQJ3l5Xm1S_gBru65h8qWYoYX2uiQ9_h_Wr_gTSFxKP10k0cfQq5ofjd3Cj26gSRqfeE_4oiz2xtxg1z4oqHIUMdnxachG8w_FKcweyAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/persiana_Soccer/22300" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22299">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSnxdYRIviJGE6KcvAWkTxGX6gUfTkgXf8JgSHyUlZDeb7PagA1ZZqDUGdLsz2USrhciIfzt5zCCrQfRfib1xdQ4Cso3AOF-B8xdgf4mJbMJCWX-K9j9Y8plKK18_FKoVXDlYeHIZVfDoro4027sIjok3y_wfJOOf-3O2Jtw-53IXsk5SE6m2Oe7Q2n1xczZTlbt66t2yT1jQ4R6qkEf716BHBk_ibUIeylspwhyBp283oIoTvGHAaTXbDujw3nqRR4lJenJRMrqjF_NBeq96PazXiUPKeTZ2iCjWFDR4dVZsjPiPbKg7uE3yUljKv71hNMTk2BdpPVJwq_JbbTj5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌لیست‌نهایی‌تیم‌ملی‌فوتبال اسپانیا برای جام جهانی 2026؛ رئال مادرید بدون هیچ نماینده‌‌ای!!!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/persiana_Soccer/22299" target="_blank">📅 14:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22297">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWoPDilR9O1MSaSXkSdxe7cvTRROwJErEgsm0hIfgEu2AX76LboQruaAtZfKQGN7zU7r4Rt9aY-p6o7IvgMf7qbND22Ayjk3lCM7ZI5VqRCl2qCeqiYtugAObbHEVavmf3EQEKl7FMgCJBs6HpGAjMsbscFBam859Y5grlhv2_dNw5yCfOlVSs89e5IM3zZE1H-SkjaN2DxjkhWq1ASgHYqilaHn53KQ3woxCfdiFUF9r-_yblWsq2Mmf-JgkwrM6ArOmOTQ5ZgLnrVw-8SW5XVPWXbbvBn01_VvmikzB3_fspU80rpADl1zut_z4BWxxQn4sKQEe-84RDgiDMNVOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌سری‌آ ایتالیا در پایان رقابت های این فصل؛ افعی‌ها با اقتدار قهرمان شد. آث میلان آلگری سهمیه UCL رو هم از دست داد. کومو با فابرگاس اسپانیایی راهی لیگ قهرمانان اروپا 2027 شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/persiana_Soccer/22297" target="_blank">📅 14:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22295">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_1LZUkYlVSF0GJ_kEo5LppfDY3k_1R8NugwtZqCQpgNtRT0iqasTmwbCcvlpewhnvsGT9of1rtNA8LAPk9UYaSdW1e3kLPTqeaNtWSIsm0CZmQHl7lbAHIKcIotI2z26BE0NmgZdWSOlNCTmOCLhlfz0EWH-Rg2tArAw3L4sl6A8c8GDY6ROjv4c7AeD3GyE-d7spBh1zQMLkpQdKg04nJ__oGepT8g8s2V0058926yi1QtWWpCdW3qHx7M8LkTTECPBqo5-2TDCpge7LwwYd_Xi9WHCZpMjyUaz3J7sXPICdZuOdAlkth3Zj3hZIpqIHGgonZHhUryUhyQIbb0tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رشیدی کوچی نماینده‌سابق‌مجلس نیز تایید کرد: اینترنت بین‌الملل‌مردم‌ایران این هفته به حالت قبل بر می‌گردد، یا ظرف 48 ساعت آینده یا تا پایان هفته!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/persiana_Soccer/22295" target="_blank">📅 13:06 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22294">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3IV6nRL5EfC3xKpyneFckT3nZNjE8JXch59-BXcQWxkpKHhYaMzbzclrTsukwrgT8MxvSQQoLfj9MDKfD1ysGekFJAyrHvCQAerLIBxpfrVOkk8APLQLRAASxT3Zlt5YtsSQVHmxgJ4f-yr0u-wFqz0C3NpJbonPm7JXfe0T-OVnWY0Gjt2vCglT8vRYyytUISmNYSmTI1n78EgOn0z2iq9X8wf7KIKJ5lktH96xNOJuv1v6b9NwH1dAeuTWNZvR9H09JlmUu0YeCKz6URZh8i6n1wfgZkJIaZ4XnHls9U5A3ydbBwBl7F1zZohTOVUIXuPVD-bANcoPS8xsVt0uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بعد از باشگاه استقلال؛ مجوز رسمی دو باشگاه تراکتور و پرسپولیس نیز صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/persiana_Soccer/22294" target="_blank">📅 00:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22293">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKjIDG_xsQgY_mKyZRmANDJnufVoQKcOHyIvWHBoLRAvOMIknU282WIIJNkUTj8o52Pk1P3AhY0_lXdW2bdSTi_fmRcK9Ut03c0qe8Ldx7ldDMSfY6RxI5YfRJhNtLaJmfM7j0sJIz9JLqMnms6lDufJeC8isxMEOsUYGqGisiXHIwHNOgV1y8GeZ8AC_vqS3S-ZBcfNU8o4UMjGZK6tvn2mkKCj2yFQk_NgG7kYE1ocaxHujRWgp9puiS7xc4jfZoV27PA8rwte18j1AeOWXm3Ft_IFjhYV8nTW7S1Arb0--t4lPpbKdVVco8gfKrozJh0cmF7TI0Eznvl_rROiLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بزرگ‌ ترین کشور های جهان براساس مساحت؛ روسیه با اختلاف در صدر، ایران در رتبه هفدهم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/persiana_Soccer/22293" target="_blank">📅 00:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22292">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Be-ySBAlMcCrv4kjKAMCmgRbn6dQ6pZFZ6xWInx8RTo_Mj5ugjmI64yfji97sUqJ_aAO7sYnH-f7kxU49uVGiadXk5braUZ_H1u3akBR0wEICImMQR3qb-bgYYwW2V3X0hVhjwtS4WAJDb_fp8-e3iIE97X9z4LY8MW75_264oMPhpdGiBRhEFCRUIBBfqxxGblsJenFyTlYS8eEvpMxcLEPTSbrYyLZ3-8WLOhzsu7oDjeJHBfdc_o8tY62XUklVDxLpeA62e-LsRaTXgvxez6nmZ2QgNhcbKvOn_W70fVj-buw6al_j9tm62taGmpogsso0vdgbkSA21RVQ0RUQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/persiana_Soccer/22292" target="_blank">📅 00:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22291">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gofOHeFXWvymuEk24zVzgECdUNsDgP3IxIMb0hL4T7BB02Ufd_-wxmWyLi1NzY_jq8vtktdkcBh4usRx_nBPJxJmvvYHsT7P4--20xatwFT7czGnGzk0rJnQ6MoDbrJ187HB_9RQIPuPmvJ7RAvbuavhhlL64vDN8IBD98in7-VjmYTlCz5gUyU6jB81eb9zG0pOBuvl1tx5mn02inOiNqksKWFXdn-BUYcevtGi7jAw6lIPTZ6ejQ8krzj_FaH_OvnB0FXg1yFu3JQo_ZFx6hS7o4oz0nv2H_N3yZzG-mp2gWS1HrY21YxCrpxRSBJIvu0fIwKhP8Omwv6Ukf5MlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعدادی خبر نقل‌وانتقالاتی‌دستمون رسیده. انشالله نت همه وصل شه همه رو خواهیم گذاشت. باشگاه‌ها نقل و انتقالات خود را از اواسط خرداد آغاز خواهند کرد. همانطور که پیش تر گفتیم لیگ امسال ادامه نخواهد داشت و تیم‌ها آماده‌فصل‌جدیدرقابت‌ها خواهند شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/22291" target="_blank">📅 00:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22290">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDlK4KbmIurfUHzrvK5jSTH_0d1HdtURuBMSDMvKLlaQd7nR0ur6nogLy4H6uJaW99kfkWkRBEM1xg_s7P3cu37WgD0Z1p-x4a4jXLQKMXH2dzNRe3x8b98Ew6KuA8AB8mNKnyNvruL4KUNXS_96UXFy1K0ti9_yO7Z2hC7vWoSbB1PaIl36TNws7eVBRmvYwROQ9c-75xOPZJyZO5qLctIRnOkxUmbCgwMSyaPqBLoXrDKD8KFZj9DvJgXIz-anwmFUm2HQuCASXzQ8FbzztSwxtMZ_XE6cupVFIOBtmI4x5SlKKOlkCdnk1xuU3C-_xii2Tpkp70nR3dCBXENodQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|انزو فرناندز ستاره آرژانتینی باشگاه چلسی درپایان‌بازی امروز آبی‌ها با هواداران این تیم خداحافظی کرد و از جمع آبی ها جداشد. فرناندز از رئال مادرید و منچسترسیتی آفردریافت‌کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/22290" target="_blank">📅 21:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22289">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYP5LEWfrbM-nFnr9PGisGQNzhFSGwJhO9eLJVkm0u6VunAnalDdLnNnTO7cIqzJa4CeNVVOAIcoBtoIBLEmn1rCfyVMPD0zfH73Sfrm3pX4uA4FtQA2UyeENljwK_N1LR6bZeYpurSDqvo_Ej69ZheIQXz8j4Tznpe8Uf6DF61cX7nZfxNQADOvHqJ-vePW6MhTMtzbeuL6lS3xdmrTdJPkJPNWxeffplmtiLERQk-_vHmpBy6n8ZP356AHb65SR-pPhgpwHPTbFk26F2RINrFg_KHDE7xBo3D6sFJ59ZeW9e_SnVm8uXUXWzA62JnBqcO55deN25-XAxKTxtWcwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
باتوجه‌به‌توافق‌‌مدیران استقلال با ایجنت آنتونیو آدان برای‌فسخ‌قراردادش‌درنیم فصل؛ برای پر شدن 60 درصد بازی‌کردن او و سوخته نشدن سهمیه خارجی‌آبی‌ها به‌احتمال زیاد او درون‌دروازه استقلال مقابل فولاد قرارخواهدگرفت.البته‌اگه بازی لغو نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/persiana_Soccer/22289" target="_blank">📅 21:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22288">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTlXP9f9smX1IrfbMlsEGeRdE6iDtB_KpuBSzKB3fOhvg0FQiH-qjJUzqgfwfSW9DUXpFEUgtyP7alagl5R_QfydzOytmHUu__MSLLt0ZoZ6-qbos5qlvjF7GSwcUprOmvJWvNpD8LIMyPDW-ool8rch2NmxdblK7Rt7h2NggenbkmEy5kWjZhiDuHeEy9OdrOJeXYfuto9JwfaA9pVhgRBYgROPfzGnHOdB4KT2Z5ofinPpXiO_OUXVBR9_gsmFxOa9pvsKCPn4d2MWAxecvZvP4Iz_KHYa_hADCeHM7yVUpX8OVPYU_Owk45vfy5L8JrLyfjbOb6WbuBFOyN_7TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/persiana_Soccer/22288" target="_blank">📅 21:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22286">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXDNUiMJHrYUXiCJe3Kz2j1X92BLmE94nG8zdY1r6zZHACl5k7HiWcHnXkAqGOiibB2_JdUEdKJM3JAnoLgF4t2w-Ynz9VLiKtQWl_Z6hEnUNYCvdX79IzT6CHKai8JeFPGtf3Swc5KM6AOf6H74natk4KobsFjdCtxn86W3n-SLy3WRCMr3wq0uL-WdeIOFzD6nuFUwnx5tDzcHVUyrERG3BWFvHRie3G7O9UiJ3A6cu4ko7PdELWZIiMR-zZVzkdz_xQIEzc-iYgUb8tx_p4S5zWZCIJXXPXZ0OcTfspdKOwFUHxzrOuBFz4RQQO_a4t3hMlUKhMy6ZKdTSyZL2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/22286" target="_blank">📅 21:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22284">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WUr2FjYvIYAl245VbevbHCZhhkrTz5Ow0kdMXdYsD4n2ez5UiMOU9ZOKqi0iAo6aQQlGxvDbN3O1ywGCOmwA-8yq_5uaa4rkuomePH64NCceh7YYin0u_yoVply0u5FaZdA50ktvETFhe06wyWbaV3Pd6ypNhjlLr9pY3sIiO2kJJ1n6HSzi0rhLVvZIQRfODXOH_PoAQx_Y9VTHuOCQRNW8t2Eds51gdHezObWdW5p9-MgvIboXl0t8Kz8Bz9u1BrBcWdLOIc2LULcddJzYbtWKDDP28DYWMt5P4rAdpSUmvXT5el0S0rzNTG-0S6thYo6JQa2mNavHTL8oxlftsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kII5uebWSE2A1CYc2DTEB48W_oXSFC4ImYi-rCSrzWfwF90ny9ImNvxBi5Ao9-NjiXe14FLkVT8o5bmK60AAtCwvuruOQJCCZzash5TLT3iwM5_ICNLZSJffBLRRnEoGUqnkcNpz8UlMAbHlAUbBQIgdCvlde7HVScRhqOcsM_JyQ7sxaPvtaHTzV6hhYhV64wl8sgsuFJ7369_fH31DkH9MWNsEZAWe96TT8Sf-AtJGxx2YbeEc__-Mgbi93fWqkudml6PrPkw806RLRhvV5a_aTRpPz3MWK-4NgDh4xbmNW4E3HUstehUcKH-Gh6R67sZjlxMQ4Y9UILS9JuCFOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/persiana_Soccer/22284" target="_blank">📅 21:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22282">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ez0PVKFmJg5tUJ2vvowo-sLBtkSKmNmhdsYgAuzaObgkHV8c44C3YsulK-XoHhneQ8IkH0KQtUP5Ewr-c1ChwRU6ApfrZJh_NsJi8Hdv9mxVFjWutLZ-rXFqpR28Gjbo2aMa-ORU5k9qfv7fvTouuOHr5l-b_63XP6g3GvIcnNKPbyvirLvZ0cUXCocU6H5yt3JVA98WEtMvTWG4MosTpAkHHzW7U9et3_6gLvBuIZ1XL9ar0J45xpP0MXU7xbUQ9EYIQWE0Jw1xTWcfvEk0LGK9V4UbfaYAH7oHdsdbrvzaWnlFfWVDE5nSnZusaOoQhgqltw0zvGG_KqryZayqzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sL33OFw5mfduBOzzL6Gg4D95NkkHuxSdSXjN-m8LoqZWg7z7aF4Ph_Zilk2KEIzHwUW4lURJsOGbC6MLzV_y7jC5NY-i5poi7z13LdjT7BQBcguQkzE89A3jbifWNHKYzt5Zk3SwZ__0R89eXl4M4QmeZ8WtzEjVwGXelVEgvSOguts1bFxKoDPzr1PE0DNMq43ZaVsepXKjM9rMuKaVMiti8I_J8TiFdtDxXckYjs76dbkSFsFHT-k1Sx7kBZIyN7m3sMWRP3X5hMFPslt_MEZLj9SQ3-YTPl_hzzKM9pStWfqPbEiMMPYZzUs_VmhoD8UPMyPnzAIq-ujEsxSssA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/persiana_Soccer/22282" target="_blank">📅 20:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22281">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXOyz7luOqL07sa9Zh3Py5J7Jo22H_FOFpldntpMCl7_V3irDMxGLdbCPSNqjNx8uqc2l1GX7c9pFk9Px8KWaqtW-lMleVNJi1OEbzO9IP60JPULiIhhl6XG8cZSfESv0QrL769sLSSkLUj6DvFTQMgQFSZj9mbAN4HdmViKq3GYhqx8weaX_7gyJ06UfmStC79Ej3vnjQYfOTfp9pZvRIVWMnPKynRY3zGqHBw1vuYZSBVPhWw0SV0IMfs4LP59ZmEP8B07KRXKFUcMxmpFRaFKylYjhmBgXyGSrKlptNOeBmzsx-myXPCMYg6gQSU-u5yDcrdzwq79IyA6Lp4iTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌لالیگا درپایان رقابت‌های این فصل؛ خیرونا که همین‌چندفصل‌پیش‌سهمیه اروپایی گرفته بود به لالیگا دو سقوط‌کرد. بارسلونا هم‌که چند هفته پیش قهرمانی‌اش قطعی شده‌بود نتونست به رکورد تاریخی 100 امتیاز در یک فصل لالیگا برسه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/22281" target="_blank">📅 20:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22280">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLi_8qodD9IDyPjzzFbyOXZOV8leNO2BYUbw1vATFnIS8GId08YkazpzseBDrkxK78iXVT3ctt0o57uTZJYKrd0GPwmznCQm3EFeb3vUvIoMN8uHiI8mdl9yjX5x2AERSM1-aLtBL_T_fH-wKZNN1fJUO-jPcF6k6b2Ap-dWTKC7QS7FajPbCVSy9nnswuAv59vuO5UxTxILF0HSX8bo0T4XBao9_gwVOWtpVaueLf3pZ0NSvkTDOHjASlBAm9gC7kZ1sRUkZ-zgtpoe95VG5vc5xdhAONfr7c-vShs5gtAwmYpa71FMWeZ2fQvddo9nYC0t8yY2LgiPgC2NYv1ylg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ محمد امین حزباوی مدافع میانی 23 ساله باشگاه سپاهان قصد داره از این‌تیم جدا شه. حزباوی از باشگاه پرسپولیس آفر رسمی دریافت کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/persiana_Soccer/22280" target="_blank">📅 19:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22279">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFzktHaVszeSStAt8PxgKs5KRLDpfVwMf5xEKdR9FhtCcGaLCdNtqdm5qg5ZG7YQDvpUxPeemgvlDyiq5-JXsFXc2DOSK6MjFEmgrE4ZX3GHRd3qX51VeqnNRJnR084yfW9J3tpdPE1v3rWts-f7oKmMS7L9En7otE1H0m4ltA6X7HAmvSUHkBE3EtwnoykurYnn7jibpyI-eX-0a-DZeht-PP69qVqI0RrfM4CV3jLIX2bKNv14n3I2bVakcNpGLpvP8AVIvf_iQJwkgWGCSlTxCa24pfLtlYzEC8RC6bu1_XfAwtmMqZ3p6MPFCQp3wHP5XurpA8oRP-2KKOtHCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیتنا پایگاه‌تخصصی اخبار اینترنت: به احتمال زیاد تا هفته آینده اینترنت بین الملل متصل خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/persiana_Soccer/22279" target="_blank">📅 16:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22278">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G19gjEhQ5-LBK9Fenvd9HHmixjId3og2iPu-EZLKrI9B1R2HdbfbQTSJUeCubdFamR_XYQrv3YAVAZpub-scxl1Geg9HXWJ25cycMVfe1rOcGz5du5WOeYjevtEvoHq6SThpaYgmDQyDj6H3SP-AMkPj-a-nB0Vr4iCPTfS0FB4ImgtYA2dWbLMPnQ0eEepmPsfgU-mDQ6udttfRbarx1hYE1_u2vnyMAqbt-dcIP7h5b5yV9lotVsLZ54GFCxO6s4aWE-9TC7DKrJPKqLMuz2gU_VxSckX8yLPwhG114RBZEpIQxmRYtqOk9IETE5TRe_LJ2MjMdDE5Qgp6nwKNmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات
|ادرسون‌سیلوا هافبک 26 ساله برزیلی آتالانتا در آستانه عقد قرار داد چهار ساله با منچستر یونایتد برای جانشینی کاسمیرو قرار دارد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/persiana_Soccer/22278" target="_blank">📅 16:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22277">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBwvCVurEp5_FZO2hRmIFcQi5y4dbZUrDkkVZ-6EQ9tysmEkpAepYRrOHgg3k1fdJF1o5S1qaqBfsIdTYE80pMI7UfVwihbOKgKyaBmSBOPNj2nUqnjW2GX_vp1R2GlkSUeMxggYF7ip3oj-bM9wTfHDihgvheqFmCdO6qcYUbvsdHp_Pegx5bKpBFZIfNLXICxzQ3-gY0uuv8Xeif84FVIx8j2_prlcQjAXnvhIkYXYzDT_-aik-uq50r_KdBnihxvaLYs81AYQRijwCy7Ji-3ygLOv9fWMSfzr8i943i3ce30bGvg1GZyodgDXMvxbFPdj4-Pb9D6kCaY5GI2XSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
هری کین بازیکنی فراتر از یک مهاجم؛ توپ‌گیری، حمل توپ و دریبل، پاس به موقع به هم‌تیمی و گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/22277" target="_blank">📅 15:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22276">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRe7KweMBLXBlPUMKd4Y7EAiXgddwO3eIKCfO8nzqgFVI086WFGQds7UTmD2bgj6J-MQaKo5_YWSY5RCrDTKHYJYAd-k5ctD-EuT6Mhd638VYtNPFPQfM0l6nliNpURe-2faxCREOAlNqJfIRpOiR8T0Fa2sfCIEynpAv9dYJUbFRXUak7Rguu9yFEkSLWFHkN1tuPYOm1pPdBh0jkvlj_yw4O8d_ncGFCdk7vXr0Pg1KJqGqA5acYBw38kclwF7zubg9pm5ByqtychzHGUsCsqIffLHR1uCdwZ6Fdbh7UGAZEnnt4ZfDou5WKpfDKZZY5iPN5EGOr4njG1gf-5-aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب منتخب فوق ستاره‌‌هایی که جام جهانی 2026 رو مفت و عین آب خوردن از دست دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/22276" target="_blank">📅 15:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22274">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReEOVda9d2Ts_LdJg9JS9yfV5l2CTKpJXAiWUCQujVRcHzl9ibTAFa1z3h5G6dw4YjiqTcR6lHacxHblvWJsyTlA7A39sWmyiz9Fh0JQo9SrXL7A3dOsekov7RNhvk--Ijt9cVdrx93VQNk1-V3cMXPElpiqE9j1gRKmEjiCMZ8BMCtGriAC4yafT5QEe16mj073f_ZMHKEXAydVmgk9NxDJE8OjT8P8HPk3Xm1i7TlVCR0pUsHulA7LrsQZxJvvD2GRTCS9MsC8b_lum5Ir2iiG-K5PvuHiP1-JltjnqZIwCDrUNZiZ8Nfld5N17CxuiWMk4iCBq5_VKlNy9bQzFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌گفته‌‌روزنامه‌های‌ حکومتی: اینترنت بین الملل مردم ایران تااواسط خردادماه حدود 15 خرداد وصل میشه‌. حدود 2 هزار ساعته که اینترنت مردم قطعه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/22274" target="_blank">📅 15:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22273">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tyh6oCPyB1MC15c1m5cxVLC06XnhHnNzsuRoC-fNvlueS7lbolIk1N0_D-bnjKrwL5w-UbndP18rrC5DZTAXev3o541EBiEZdrj-lwk_sNGf1Rp9X-sBS93HNabOPbrHKbDwf8HWSZGrg50cVwmHacm5kCfir8SqEJkI0RqXzHJUxsFTbtP0ogoapAygLBmNGwJN9krpWTVtHcKBHJ9bkhbbMnzFnmDPDVwhCo-FlKw_lxv4V9FqZZFIZZ9DJnEMQ1fvv8hY6EBk0aYz49qqOFPJ5lvlsprWzcWTVcX7zD_EEgHwyUOPvvmJjBmSPlagf5Ow8epKlLIVB4IfW3nmXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/persiana_Soccer/22273" target="_blank">📅 15:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22272">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/banQKfKQfXRbA9ZSUTXhg0k-Z7fnW04BpMheoc1-78QWqe8ynsPUlSOBl9dy7vG2YgN4smEX8hTBOoKIsp1gtA8n9rvnyCI60rLLTBIjkGNB5mvXQrNJtFCszU6BKzomMoIqKYPsMV-fcAFDPXvv9nXVQbP1E6Z1rmCQuvnEgEprhCN3Vp5mWMwi_KSwOX-tefLhhAZ7seTo3HyybRgVAkFN1KCaQo7OMeoRG5_GGi4cOhtD-9Zf0qTUnFmgiEUDJAT6wgvbgxWnjZTX1BpU3kwnEACXNkaboSv1YkCmYwCywfTRNPOg4fq2EPDYyfIhPZ4YeHPl2JPQ8i5WRnh2xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
درحالیکه وب سایت ویکی پدیا از تیم های حاضر در لیگ نخبگان درفصل آینده رونمایی کرده و در بالای جدول هم اعلام‌کرده این جدول غیر رسمیه اما برخی به اشتباه اعلام کرده اند که AFC اسامی باشگاه‌ها را منتشر کرده و برمبنای آن اعلام کرده اند که نمایندگان ایران از سوی فدراسیون استقلال و تراکتور هستند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/22272" target="_blank">📅 14:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22271">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb874305eb.mp4?token=SX6l3TvLz8LybuNOo2jhyZrJBm1uzhJhFNYUkqgqnby11BnskR2ib8iulzJh2NE770-2WFpSQm2H2bxwfShNdRBxJiHKMN-b6JskawKLFj_nAop0Yb93bgsuDtomWINh6m30aChJweVMY4pOPUpm4hzVv4IyhmK3TTjnl4QFskWMJqxMFGeTb0pkkX2s96etXGY_EM9orlnsWUGp1x_hNl8lwRi8w8rIhhREdDcKU07e05mjMJn3D12VEJ44sU2dJvYCgZBNQqm2SxlqySe3oqrQqpPfIyYHABbxcX4H9h4qH4L9uOhilVEC_jGJeuq_A7LOBXqBnF6dQh9SWG8BKqlOHyhpPwLWCPDPwjXd5QjDJfGb0HGrXqRJoT7sVYFx9KPdmtcYlKUiZe5nDeeTxU6zDz-9wTmYkDZc5Z8pw3ZZCfTo8N4FsZiK6FAa1PFoKqK7dL9seZaZgtS7NztFioSNCbwObMgt2S0q4YX91sJMUZwzSP-CQs2UCwNWwg8-r_JKTrA57RrKF5EPUliZXe6dDPxMj3t3aaGbPd1z1B6HLfDDVVzSND3fm4GGMe2tsYWqMwv0SafrkMSyi7KFoko97PGpfExzELevOKaOKtGd4D22iSrCqfCdovg-9tI9LQrJ2HOY23q1PnwG0FUC9YJTOcoeD9ezUYhIxYxdmY8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb874305eb.mp4?token=SX6l3TvLz8LybuNOo2jhyZrJBm1uzhJhFNYUkqgqnby11BnskR2ib8iulzJh2NE770-2WFpSQm2H2bxwfShNdRBxJiHKMN-b6JskawKLFj_nAop0Yb93bgsuDtomWINh6m30aChJweVMY4pOPUpm4hzVv4IyhmK3TTjnl4QFskWMJqxMFGeTb0pkkX2s96etXGY_EM9orlnsWUGp1x_hNl8lwRi8w8rIhhREdDcKU07e05mjMJn3D12VEJ44sU2dJvYCgZBNQqm2SxlqySe3oqrQqpPfIyYHABbxcX4H9h4qH4L9uOhilVEC_jGJeuq_A7LOBXqBnF6dQh9SWG8BKqlOHyhpPwLWCPDPwjXd5QjDJfGb0HGrXqRJoT7sVYFx9KPdmtcYlKUiZe5nDeeTxU6zDz-9wTmYkDZc5Z8pw3ZZCfTo8N4FsZiK6FAa1PFoKqK7dL9seZaZgtS7NztFioSNCbwObMgt2S0q4YX91sJMUZwzSP-CQs2UCwNWwg8-r_JKTrA57RrKF5EPUliZXe6dDPxMj3t3aaGbPd1z1B6HLfDDVVzSND3fm4GGMe2tsYWqMwv0SafrkMSyi7KFoko97PGpfExzELevOKaOKtGd4D22iSrCqfCdovg-9tI9LQrJ2HOY23q1PnwG0FUC9YJTOcoeD9ezUYhIxYxdmY8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوخی‌جالب‌روبرتو پیاتزا ایتالیایی با عرشیا به‌ نژاد: من 58 ساله‌هستم‌اما چربی‌خیلی‌کمتری از تو دارم!
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/22271" target="_blank">📅 12:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22270">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWnFMI9GiAmM-oEm37BlAfnbcGsvjHov2LHtsDhpX0rMXkcV578r8D3sPF3B8rxWORXC59NlfCL01Xsp6b6LoM7NuoP8vKdlVZxLdjGqiBuJrgPRSjLCLrip4B5OFW2wM9VpArIU1EJINioF1B1mBc0PJ_J0lY6VA7iB8x-cObyUHVGIuRp_gZYtNZEOtvyaAxFw5RM195ARUHjgYyN7Iwm5CiilanrZGX3NqM4-G_1kDkcEpcoiGB3_zHCDoZDLTTnSh7TwqB3hTpmt2xAAmUIRuDeU6YLptxTmUW1hk1fMBZqSEzW6lPqd3zHbhtHpZmUWtvLzh-2bLYDt8-8Cuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دنی کارواخال کاپیتان 34 ساله تیم رئال مادرید امشب آخرین بازی خود را برای کهکشانی‌ها انجام خواهد داد و رسما از این تیم جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/persiana_Soccer/22270" target="_blank">📅 12:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22269">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=VmDdgV4Bs-jHkWt9MWsABC1-O0fCEpHETt6N9ZS7-AHBANmENXh0Ed-7KXQ2tSPzNmXpCmpkUcwgqGuE8e2r1LFaHYa0o2506eAd4nJZOVRnGbpAsWPQlA6yvbiy-hvf7kqM5Of5wFJrMyUB32_qgFKfPPdWDBN4Q3PTwOhF2BdzRbgw3XJUjh8kBTnxz4CrRg53R_qRMv5mHXLQhQImRt0WALP0v2M50ab6d0wapXB2jdrPWynVfDN3JXFBhSklyFgexUhZej4sCAoYa1CMXJsyBL8nbcW3nGT2GaSLFh784ULUO1CD5HztRD0Xccs9YkZs7cPNJM0I2QhxICmjfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=VmDdgV4Bs-jHkWt9MWsABC1-O0fCEpHETt6N9ZS7-AHBANmENXh0Ed-7KXQ2tSPzNmXpCmpkUcwgqGuE8e2r1LFaHYa0o2506eAd4nJZOVRnGbpAsWPQlA6yvbiy-hvf7kqM5Of5wFJrMyUB32_qgFKfPPdWDBN4Q3PTwOhF2BdzRbgw3XJUjh8kBTnxz4CrRg53R_qRMv5mHXLQhQImRt0WALP0v2M50ab6d0wapXB2jdrPWynVfDN3JXFBhSklyFgexUhZej4sCAoYa1CMXJsyBL8nbcW3nGT2GaSLFh784ULUO1CD5HztRD0Xccs9YkZs7cPNJM0I2QhxICmjfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
روایت همسر ناصر حجازی از پادرمیانی برای برگشت فرهاد مجیدی به تمرینات تیم استقلال بدلیل تاخیر در حضور در تمرین بخاطر تفریح با دوست‌دخترش
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/persiana_Soccer/22269" target="_blank">📅 11:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22268">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7265d2cc05.mp4?token=PeeMqGk0hR9nyniq1t5o5EtLPKVcbAYtR33ZjujhTj30-5fH_qrPj2gxDqbAr0sC6XyShzmsTuVba1D-5rH0o89xQoyeYsSFlEbfmDoUt-pVjhv-IcbUs6sF_DwJ_FXx5zSyldRQ5oyEnTrHNcUn6bsikfP-snG7lgSuLBPmU3wgY7K7sb5kdGLN18WQZsQQT9kIFmV3RPe9xOStLe7pWizZOXO4FrDCAdj9Ye2Lw3N-pK8gQ23GWCZxqatPZd3nAl82UjpSjnZgWF6vbGIacR2t3_HnW4K3m-PDs5awUNZfPgKmgR6RwYmcXYKf7NO7UPcOkhwwv9SILzT1hiqQSQEeRoTZSo45nK3fs-wudRimpIrfx69nNhKztvPYMkUou2PURuzPCec4Em5UKq_DMjkuoS5aoJUmtuI1LK2O7jI5qKAp4QSMzdW0aY46keVewYlPnepQ3a4tjjQPmGR-kyfjmXcI1McMH-H17D5kYteOARqW9qHSNAlxggrEgXVSEN5-4z-IgDsEn_GSqaeVmgQLP61X_3OScZJaerGCMH-H7MoOMVKsJRrGVX3nyI4vBJZAg8aT2ct3f82rq9gAmPZZ2Giak7FNggAXH5IUW-q7fM5JXY7cC_Z5v_aSLY0dDKB9IBBMaVadVzku1nLccntO_oZq21aR-SFMvaeQGiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7265d2cc05.mp4?token=PeeMqGk0hR9nyniq1t5o5EtLPKVcbAYtR33ZjujhTj30-5fH_qrPj2gxDqbAr0sC6XyShzmsTuVba1D-5rH0o89xQoyeYsSFlEbfmDoUt-pVjhv-IcbUs6sF_DwJ_FXx5zSyldRQ5oyEnTrHNcUn6bsikfP-snG7lgSuLBPmU3wgY7K7sb5kdGLN18WQZsQQT9kIFmV3RPe9xOStLe7pWizZOXO4FrDCAdj9Ye2Lw3N-pK8gQ23GWCZxqatPZd3nAl82UjpSjnZgWF6vbGIacR2t3_HnW4K3m-PDs5awUNZfPgKmgR6RwYmcXYKf7NO7UPcOkhwwv9SILzT1hiqQSQEeRoTZSo45nK3fs-wudRimpIrfx69nNhKztvPYMkUou2PURuzPCec4Em5UKq_DMjkuoS5aoJUmtuI1LK2O7jI5qKAp4QSMzdW0aY46keVewYlPnepQ3a4tjjQPmGR-kyfjmXcI1McMH-H17D5kYteOARqW9qHSNAlxggrEgXVSEN5-4z-IgDsEn_GSqaeVmgQLP61X_3OScZJaerGCMH-H7MoOMVKsJRrGVX3nyI4vBJZAg8aT2ct3f82rq9gAmPZZ2Giak7FNggAXH5IUW-q7fM5JXY7cC_Z5v_aSLY0dDKB9IBBMaVadVzku1nLccntO_oZq21aR-SFMvaeQGiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌از تکنیک‌ ناب‌ودیدنی نیمار جونیور فوق ستاره برزیلی‌تاریخ‌فوتبال در دوران حضور در PSG
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/persiana_Soccer/22268" target="_blank">📅 19:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22267">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miemWmvjJiUscrepSaRO8lgtoQF9_jqqKICItUmdJuts5xDB6RAy3uO-s8zFJEPTCqWoNyuhxMaiJxDCbmDJ8LhXoUeFSE17Mi5HCOwqH6rQSInc8MABqLi8MivcC7hOjADLkZgFT71e8uuGgM55pLjUClaN8cqU974k0TqjaYNw4KiLvYZ1QRTN8Wr5CdVzVan1BInnmkwIJ3XJ2Rgbw-eE09AenNiLMDCtbtBR8My0YSdKHfPCGlluCu7vtoJOCzZLwIQq2ST1nJez7dkFt3lC4gkrk6m6NmZ2R2HdqY1RBPqFWr180wpdt1-gi_YpRugVHRSJtxfiugGrnYrOug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعدادی خبر نقل‌وانتقالاتی‌دستمون رسیده. انشالله نت همه وصل شه همه رو خواهیم گذاشت. باشگاه‌ها نقل و انتقالات خود را از اواسط خرداد آغاز خواهند کرد. همانطور که پیش تر گفتیم لیگ امسال ادامه نخواهد داشت و تیم‌ها آماده‌فصل‌جدیدرقابت‌ها خواهند شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/22267" target="_blank">📅 19:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22266">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asE3DkPtgWzFPOwXBYCqZLMrtbHc2sFHSeYqCURtJ0PU_I9LOSC7HfCmmdxegbR7R9aaI-zLl4agoaihKw-AjBYmGOt6jEpUuo8pGqZnT6V9_t8UjVxQ6lG7KQftBxe6RGav1I-YclBfP5vIAZ-jsAm9vn4VnI_vsDIc3ALct4L3QVK4UU8ii9VTGK0uFg227ssDjtfhGvObsmEdvLW_bB1q1PLH7ikhIFaAW8n9KNhf8uIqPHYVQO5lgwByA0A8ZQOnmL4QSVkYv-_eVEyKOAFCE4ojOgh7dXPNUTIxW7pnkgBEqZz6_sr-Ni-AsQgscIvdW0fiEp9mkRamaKCGhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/persiana_Soccer/22266" target="_blank">📅 19:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22265">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9n0oVVCnMmrvk4CeWhofT_uXPg64Uuqde-NgcbB2K9CoJ4eKWXGOFAi7ZncWVEoAjpnxg4joCVL0ZyRqSxVaUFZPPhY6QMVLiEtuxczlVlarhDBvDJLhF5auR4ilNAuLSfikqKsM62Z-ZowAnG9pQUWFEE2nimpZxNJDoKSGa3XpIdCoQgwteUGsnTK38zMknIrehDHKKGPD58qAcrXDx1toB2_ZWwjzIV7pikYqm5H3RaGm6WCeByCkhQCtnoGimPubSI8ACuvEFt0lhUJSs458nx6VUbm8ahIOzL8_YFGC8I_VxfbOv_NZm6u0o2MV1VXMv6nfKmhTIRC1t_eXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسمی: پایان راه آلابا در مادرید؛ با اعلام رئال مادرید، داوید آلابا، پس‌از پنج فصل، مادرید را ترک خواهد کرد و در تابستان، بازیکن آزاد خواهد بود.
‼️
داوید آلابای ۳۳ ساله، ۱۳۱ بار برای رئال به میدان رفت، ۵ گل و ۹ پاس‌گل ثبت کرد و ۲ بار فاتح لالیگا، لیگ قهرمانان…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/persiana_Soccer/22265" target="_blank">📅 19:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22263">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDKjoTpzYZBo7WVjYHeK30glvgeC4LYyimw1KCMdJrTtR3KKJvmIJuhY-h0zTmiITiklulzyVynDcfjKTgOBLNBZZAHF7CqRG34LogzN_7Lr7JRn0N8gk7klcud42fd4NS5PopTVn7fUmv1nAONHOaTGsasBwFez6wPqxB6VAiFrMcj44G8z360OmALBq8r5GSf7Fe7suV9lE2m_PiOrDrjhYYijONKtV3_Hs7yBz7l0Lc04TQi_aPd_Vin8_Fc0N3Q6V0NR4ba4B9Yh78VR411gQUcKmHk2SEdCfq9YPKQgvW9dd6k-7z8eG1A1uaSQEr9c_W5sKCIN1sAyTcocPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22263" target="_blank">📅 19:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22262">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4XnLWlIFfw7F92tLh0Rjpdy77UdBrzWHcPCTfZm5cN0ZLq1lBOue5q4Tvdy_WzCkp1Qu3uin_LEpbib_bn8acu8Eio0ucSSUASdDZUUwmfbK61pbNPGwcojkL0v8K-Wn1nI8sVsm95JYNPVDlwG-G_nppouYnHN8JVOOJG1HRnwS5ohCqVEbugxUgeG-uEOFG-izsG6GCtiNjwAb1x4CQ_Cb6XLc_y6MT0-gXfCRZ6SK8Y7F97f6iYoxcngyyVzlM7WBXQvbUIS1G6okUwi0Wic1U_Ig0waWMx6_6qy57UDC05-IwQorwLiueyRdrLpOo8mVT5sxNXGuH4Jmrvcqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌کامل‌مرحله گروهی رقابت‌های جام جهانی 2026 در یک قاب ؛ جام جهانی 2026 از تاریخ 21 خرداد ماه تا 28 تیرباحضور 48 تیم به میزبانی سه کشور آمریکا، کانادا و مکزیک برگزار خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/persiana_Soccer/22262" target="_blank">📅 18:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22261">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cnw9l5zTBFhDiUBZ1DL9DuDev1m_wwa6ZsogMw-XbHRgpKpp9r-0QCgGd3gZFHBvgFta3RY__BzDQTzWFuQ-EQ1LfTUQaOQwmpp49cGsTKUPyjYDp12Ap6CpPFhBm7wUT1U4VbksdvKzMSA2EbhUgek918hIBepKg5ZjiFjnpGgDp4t0s4TWtJj3NpixJ0cXXDaKvEMsC9DxF8cyj0qmP79TGTMjDoON1AlP2lr75loLuSoEc82z5HoRa_UaSXDKKY3GPF1RHDuesylb8Kr9wTCgKL_W0Kt3qXpJK4RVm_k7IS-0mvk6fuOpIJqPlrHY1x0yO7To0kCVF2-52_x5ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌کامل‌مرحله گروهی رقابت‌های جام جهانی 2026 در یک قاب ؛ جام جهانی 2026 از تاریخ 21 خرداد ماه تا 28 تیرباحضور 48 تیم به میزبانی سه کشور آمریکا، کانادا و مکزیک برگزار خواهد شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/22261" target="_blank">📅 18:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22260">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daxaoszAyb0yxdv7nywwZGu1O1xCqoKxno1nYe5RbETyvxa0d12yCcqf-Agoex5O64tAb1sgxD-JhrhCEt2NY_FfkCEiXKSObrJHJ3MmrcG2yRoX5snhclzWvURrtodozeCKaMZxpaCkJ9Rgs_1R37TXOZEnIslXeRAjucKevZR_p4WyRIedHQi1DuXba0bfuk7TwbMomwSXZb7ab7mNdJCYNUNqt3b8-VDX2zTCHyEGZz9YnFF-XAyc8-VIVje32SLd6BKKn2ms_ks73QOfp6JyhBck6xK5HrAwaRplHANXW_XNenf3D8oMeUeTmlkj4OCR37bPModofiX4aQZSMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛
باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/22260" target="_blank">📅 15:44 · 02 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

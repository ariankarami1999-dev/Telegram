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
<img src="https://cdn4.telesco.pe/file/Ryqj8MYsapvntTZpREfyy1ymTA70YeBMOZsBIgYH3ffSzlHmY8Ixo-wpTDE8EEmhiEo3kaxJLotocpdUs8o-NTNV05hTehGPSeSxeWMsS0YAocoqd5AHomTXkElPrykZeXi_PBMMBFdgstZQEZGdhBax1E9PeDdgYU4cOe9N894XFI7ZthQGCOG2XrHD-_n8nXHn4p1ahs7mrkn44ef199l9PJ0GSPciKtOuhFy3NyP492J9ZBiNTGYQD5CR0TBd4fdLCEm5HT6Fxw9rePBZnVG7dioBeJGdCfejNYIOId4Vw6RIsogm6KYYum2kxgSrApMBrRbBg7ZaULV2A00UMg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 185K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 10:05:14</div>
<hr>

<div class="tg-post" id="msg-22374">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAXrXdn9yQPqxpbNTmarBBvdl68iCSe4G1yHBJuiCOUqrQSJuVtFcOQ1LYI9N_Oe10cuz8wnXK3B3qqNr54bXo2bajlQhTgJ-shmDsuVcOAUBFUbN7pmXE02Kb4NAqVoPHO7v6FkbPA6r8d2srLMSUt7hwpW6TuFOhW07vGIyy0wg4KGCqZS08SeTthLkHrxUtVZxunCGxx0c8GwYte9NuvPTwsi-6p4QQTPd9PGqFq5iK2GQDLOBobDNfq5TwTJ8tT31ZqBKjwb69_ZGTijpXrZVd9EbQOZ4N8WcKrA8f7dv8rClaEPpedQIbO9jGHNZmC7gWYbpyJmCu_gVZ6bTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ کاسمیرو هافبک برزیلی تیم مچستر یونایتد، آخرین بازی خودش با پیراهن این باشگاه را انجام داد و پس‌از بازی‌از هواداران خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/persiana_Soccer/22374" target="_blank">📅 09:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22373">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJUl07PLynFV6ZQiLW54i7ttZNGXmXwGJKYe7eR9ZHVa4nFlsP1Xcg8Xdg33uU9Xo_M_3PPdHbn9A5ZkKj61OVEdo4ocshlD9hEsyq67snoPBzB7YrawAneGl0TmEzgcELdfuPl0zkwnDubcjoer1L7QaSTVxKXnIO83xpc43kUfXfoIdP0R54pqjISzCFdaYhu_FEoD7aweDoYb3or1n8FhTlFiRSNCR5R6j4eG9ErPvzHaNRxbCVbhkzwrCPVcRbYNAmWzZmQUXmRGzWsF8mXDaqr1pq2ADlSjWhU0YkUEsEEsNmfXDWGK7qLfROZ2b-gJppTFYy6X5YBd3ZSbjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کافو تنهابازیکن‌تاریخ‌فوتباله‌که‌ توانسته 3 دوره به فینال جام‌جهانی دست‌یابد. حالا لیونل‌مسی و امباپه این فرصت را دارند که در کنار کافو تاریخ‌ساز شوند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/persiana_Soccer/22373" target="_blank">📅 08:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22372">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20ca45cde3.mp4?token=c6eEGrctUQFPSvsc3g9fN4-P8OAT0IBKCAcLqR0RnY_zJNneksTuKzkmuvkda6YcWLWTyhDNuMqkDHjRQvFmOoThdQLDIzIoVDF67esyc6NNPeLFnDZ3HTDr5i8jnag4kKfGduTRnVCEl2zSqeCmcUt5MGtUXqH-mTe2RTi7E0wac1cw3Ew0HU5ONxnkMX45ZCm2ZZX-L01obdJ1If0vpdTR7-85RjBvCH98DZAiXMYR0QQAmLLWwmiqroKtNUK8c5i096s6WDMYHxzeYPEPqPkFgykIuZSKi5gCsw1LPFPQm_tYfq1NtEMZCrTjC-e-AYeAPW06RlwA7Db1mFIsxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20ca45cde3.mp4?token=c6eEGrctUQFPSvsc3g9fN4-P8OAT0IBKCAcLqR0RnY_zJNneksTuKzkmuvkda6YcWLWTyhDNuMqkDHjRQvFmOoThdQLDIzIoVDF67esyc6NNPeLFnDZ3HTDr5i8jnag4kKfGduTRnVCEl2zSqeCmcUt5MGtUXqH-mTe2RTi7E0wac1cw3Ew0HU5ONxnkMX45ZCm2ZZX-L01obdJ1If0vpdTR7-85RjBvCH98DZAiXMYR0QQAmLLWwmiqroKtNUK8c5i096s6WDMYHxzeYPEPqPkFgykIuZSKi5gCsw1LPFPQm_tYfq1NtEMZCrTjC-e-AYeAPW06RlwA7Db1mFIsxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های طعنه دار ابوطالب حسینی به وصل شدن اینترنت برخی از کابران بعد از حدود 90 روز. خیلیا هنوز نتونستن وصل شن. از 70 هزار نفری که همیشه پستارو میدیدن 30 هزارتا آنلاین شدند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/persiana_Soccer/22372" target="_blank">📅 08:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22370">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbC3f2WrFQo0EwfqRE6y5nrVy-soXSYL0Xt0EzJMZ7TTfTrwXJfC3xpEQywdhWZh_snOOTquMp0yYJImBsOqttCRINpMnWJKEzZoYMHMUYwl6u-spc1ZFfaKjRHqZGlk_mPf06Aape-7pTu00Ifpv4Elbn3n9ktrMrVVwiwf5D1mFLN6bgpm3QBUR-ruit-OTd7bdPCCFxjwqFuoQZFHAAcV3nm1RjNxkfftk9wtU9Pn3DM4S74zdj_47S6rNtmdaQBrZnpjlv-t-rTpnxZUW0a8jGAmGjrd5UiMKOkpEcECsVhs4L0aaU-5E-nXzul6mWiULX7p2y7OPlw9mVJ5Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
نبرد یاران‌صلاح با روسیه در بازی‌های دوستانه ملی پیش‌ از جام‌جهانی 2026
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/persiana_Soccer/22370" target="_blank">📅 01:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22369">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IygrrdbWIaKnnZpU7SmIkfW7ZAfQCis2tvYU-q2jMjW5hy4jsoIhLSWjG2fCHZgV2G-a5fQ0gVrk3XQmLLVZ3K5p0B7IiBnhZz2qZWqwIA6NTNAyOm6ymT1h2-H2qM6AjFE8lZopo3otTqR3UfUKT-qD5DAHzt9DU_-cPu5JZ8GaFB-n5dZFVM0Q1yEIzL9_WoiqRLwXkXWNsG9Gkw1mKuqt9ODgM_3dD9PHur71yBMTV_xlb3i84KkTXqlNuA5FXwrnXmJ9Qhacc69c-1XJ9bMYouqOkffykyk3fs-N9Ghoso5HwSMZqkDMQbFsVwu8JvGECOmgAUBoHvKqL7QWmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه تنها دیدار دیروز؛
قهرمانی شاگردان الیور گلاسنر در لیگ کنفرانس اروپا با تک گل ماتتا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/persiana_Soccer/22369" target="_blank">📅 01:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22368">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Guw-6r_dZWUsVgp9rE_NdZShdF9GVvZn4rbSUFZYOt1e92e8vJgkf8UEI-uPaCHfw1JJ-H-cueAiAX2k0g4JXBngVY21kD1Hb1R9v3GQViNIieHXZmFhf2upzxPIH7QEy0eWK3B7CxJ67FJ_yqWdvuFrmidtKNoBhDhBGPDBANvKn_fWE_ZAQu4-DMhSYq6qPuoCJHtlaz7fR_R6s_UzB_m1MpP5jC1c-dwO7KdmTFkRAezuBI3c5O8m3iv5znx5Y1oDPIe9LYuGp5LgY8naoFXIrk2k4w49ZpclDaIaSybPEG4Mf0PIdBhI6XYn6nQ2wcDTYnXuOtsJcL7SaePYPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
اوستون اورونوف ستاره‌ازبکستانی و تکنیکی تیم پرسپولیس درگفتگوبارسانه‌های ازبکستانی اعلام کرد که در باشگاه پرسپولیس تهران خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/persiana_Soccer/22368" target="_blank">📅 00:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22367">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/persiana_Soccer/22367" target="_blank">📅 00:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22366">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjzE_qm6Uw-sR7yZFeN6qeQVCbzkFj2rvYWHQP3SZ_88EBExhN5QfmOlL-nyFCG6K6CAiJKeCA9DRA6yEfunxYw0IP_XEP4bPlqYwc-53KWkhV1ZogVPOGprU6Yys_YODvmcWoXpCb2alBpsxIiweTyasrvAO-2RqTgl1zAdqmCEW3FUG6x250I_2vEBXYEauVrl06_IGiSQpSiMKdFH9GWjcRrF6_8-vr8HBqnXKVfRQ5sKbanCFI3jhoqY8rPCv2bxy3RY1SAdnpRXfGkI37ebPdIO-4g_n899tpDeQkER8nZmQGb1PqbUh9G3utYvl08A3w3SqL4OGBRf_N2_Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه هتریک متفاوت و قابل تامل کریس رونالدو، لیونل مسی و لامین‌یامال ستاره 18 ساله بارسلونا!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/persiana_Soccer/22366" target="_blank">📅 00:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22365">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/persiana_Soccer/22365" target="_blank">📅 00:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22364">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLxrQe-gCsYQdz2IUEf592FjjYMmWBU666NDoTC4spS7SGUgv9YdwAAAPdmFsGBvhHlztjzFdSSJAf5dRCqKCFyg7Nh2GP5o93rhH7TfCn6PSa_pBIvmRuhyOI4NezcLrIUutO5c5JhG4cfnW2WJbN6Rp0AV266e24RObLlypZRw69Y6TXnjlK5ZfVdPHegFzVNG-OfFWjZZuACs0mOXUZdYXLIgkyeHrFExp4MGonJMpYzjSLKDN8PffYwGiXbDgLkkNVkOa_8lLRNEqkrX0a8ubOLFhBvvCNo3aW8c9IYKehBvALpyEdYImtUj1g5tn9B6j2Zqc_up79AZUeGpBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ طبق‌شنیده‌های‌رسانه‌پرشیانا؛ نماینده محمد امین حزباوی بزودی یک جلسه با مدیران تیم سپاهان برگزار خواهد کرد تا توافقی از جمع طلایی پوشان زاینده‌رودجداشود و راهی پرسپولیس شود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/persiana_Soccer/22364" target="_blank">📅 00:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22363">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_KLKLdRxyXnlvVrQ_J0XzL0E1Dm2bnGtTe2UqKCCkpYl5bqhFSmjlTjZlDCcnkvC_9fh99Cv5LiQHtETXhlzj9-bEsghXG21OdL_0y2eJ3aPi-zXNSZfFe-rwr7qAiUsxGT1HfAsifpUERl0GMD8i7ne07_HU5bx8nMuF-M9xiKH5s6Cx5I7CvdSaoPNfylMxGEYVAXPnHDOwr-1zle3t3Dkxz4Imy87cFrIZA6i6evZheGmLwGEP7PAuYcKJBa50QJmBUbcx4NP3XHu9LzaeEsrL3Z88xEN-wODHcNDlNa648v0WmSQvTBYhvKbhcWCQG0LZnJ9Qop5r61vVTzYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ بااعلام فابریزیو رومانو؛ آنتونی گوردون ستاره نیوکاسل با عقد قراردادی رسما به بارسلونا پیوست. هزینه این انتقال 80 میلیون یورو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/22363" target="_blank">📅 00:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22362">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owB7IhEE_7KlXugIvpl5eDTXy1e8lYLBwxK3OOg7RCyyq-STVTUEvIw8zXrn2Pr16t07I0JhRix_8nrCdg-FJhvvB9X5V-jHkYjQfmxR1YhWYWJqdBlRSV4_ijrI0X_YzgX5gDwioLdM4pftAILIHkaQuMvuNehrOk_ZqivZUGQMuEqW3-lCYLTJLaWfElpKaADOmPS6gztq73g42nLx8i_IPMfpXZ9eQAJ-sqaxtsl1onjjxGrZbJiXv7hZs8NX89c9hHT3uj2NMggJ1bOioGcsuGX4sR2RRvvf574DZZUj4SVS1ujynOHfDNANRarqcupy_jO6joZT0Ip9_qKMCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ آنتونی گوردون ستاره 25 ساله نیوکاسل درآستانه عقدقرارداد 5 ساله باباشگاه بارسلونا قرار دارد. توافق شخصی بین طرفین انجام شده و تنها توافق نهایی بین دو باشگاه باقی مونده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/persiana_Soccer/22362" target="_blank">📅 22:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22361">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/persiana_Soccer/22361" target="_blank">📅 21:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22360">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nq36dL29N7GkQM6dwtBi9cv7-2oXdccHPogBxXjaWOb0NY-Ox88aF-zapYVCJCm_lvfQeRTOwhEvVTey428vFxq6jPi9AKsf0UraYW5PeufG5w3REbOezR6_v9Nv2h3fo9wFdC9NX731QqxQgdn7c8QAwtKV6SjTPmUn9CtzRQVYvKUGOw8DAKn_GGEkvQyNsRW4kl1Zz7Zcc0E0uj9V-8YeCb_kLfgJS9FUriSMWxV62qHrlTeaOFI1X1TIc-yKqe4Hr4WEk18XQxrV1KAJF1CiQP9DuorH-GnhCKey7fIdqGTWKNogG8awpUUytzW16A9R-U1l54YrDU1NAeUMxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ آنتونی گوردون ستاره 25 ساله نیوکاسل درآستانه عقدقرارداد 5 ساله باباشگاه بارسلونا قرار دارد. توافق شخصی بین طرفین انجام شده و تنها توافق نهایی بین دو باشگاه باقی مونده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/22360" target="_blank">📅 21:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22358">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30152b67bb.mp4?token=Da5jkPAF2Ypo79_1tzGKAHdid1cW6UOYjJ5LKcJ1N0iSp7zQjg9Y0E61vAHacLn8mMwxoeIWkEp8GEA3pm7_MzNuQH9SW9gSmmS3tz2oAVlJwmfOLXG5umpwzADlqn7Vy6veouZZP73LFKwWgmVgKDDy9w6e34P8pt4YjKBe_adVELooJNRGw7aml9g6B9PuLBOITdfGbtiYrNSFoakgkzfF8g8qPOXoxHyapSnCSL65gjDrqFSmQSIGIMWjaAt8V4OC_fZOk_0oTnXwSDrLbtszFOWYCzYDe6-XrWtFwahUU5BCebG0erXT7m7Jh1V6hr08TIx2tjNvw8sKSmQNRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30152b67bb.mp4?token=Da5jkPAF2Ypo79_1tzGKAHdid1cW6UOYjJ5LKcJ1N0iSp7zQjg9Y0E61vAHacLn8mMwxoeIWkEp8GEA3pm7_MzNuQH9SW9gSmmS3tz2oAVlJwmfOLXG5umpwzADlqn7Vy6veouZZP73LFKwWgmVgKDDy9w6e34P8pt4YjKBe_adVELooJNRGw7aml9g6B9PuLBOITdfGbtiYrNSFoakgkzfF8g8qPOXoxHyapSnCSL65gjDrqFSmQSIGIMWjaAt8V4OC_fZOk_0oTnXwSDrLbtszFOWYCzYDe6-XrWtFwahUU5BCebG0erXT7m7Jh1V6hr08TIx2tjNvw8sKSmQNRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوست دختر جدید کنان ییلدیز فوق ستاره تیم ملی ترکیه و باشگاه یوونتوس ایتالیا هستند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/22358" target="_blank">📅 21:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22357">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjbcRtSnIUQZCdlnmg5FhIX2uWLOX2jAvpuKLDfHphEEVkuBmk3WQgT05SUd-bcXQiAG-PbabrNuVjFRMWj6k1-jXKKpn6dq6ltL1OZrbxpVM0X0iO77c3poqjsgURssSwB_wqPuAhTu0O-s2qAGdV4FHSeeqj6RAUHu__olLCu_i6R2YJSaw9FfS_liymN0wA7vheQKA3C5AalmC4LXfTJwMmwJXljtkJjGpzoix_CBOc-0DWcQMPrOdpRaLWoeISBNtud4a3qbOjVtO8q8h4vJTdgcV-iTb1gTECuFUshzQ1xO7RhV4GDJY-k3lpLW8YsgUjLZ1XupJvR40yR3Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فرناندو پولو و فابریزیو رومانو: بارسا گوردون رو از بایرن و لیورپول هایجک‌کرد. بازیکن تمایل زیادی به پوشیدن‌پیراهن‌بارسا داره و حاضره‌دستمزدشو کاهش بده. نیوکاسل برای‌این‌بازیکن ۸۰ میلیون یورو میخواد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/persiana_Soccer/22357" target="_blank">📅 21:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22356">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDZ9gkrlwbN3ogcGc-h0mAJlmktl3n8s05UFkcXQzfMRVPzM1hTOqimj8jFyUsyCjLVdSrdghEwAGHr3MLBPtT-KYJ5PoXv0Gp4a8FkQU02tASDudee9QxjQ1de4gzNQp1lQM77KfJvmf04izsnJOqSlDWXRqTXR5vFnr328jfs8ZNFOeBd6IpA-QJrja_bxtibEs7CDB_Ppv4lZExrDqDEJzuIZqezTaR029z3eX9QTEOjg_t1fvEdT_8pbN7WXXW3od-o5_sFXtheyGaflry5tyjHyxKlkH0AiHKINWaVLxfkGtpUkK4cycSThTGuyH0a4m28T0wFxUYXfx4LeXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ آزادگان درپایان هفته بیست و سوم؛ نساجی سایپا رو برد. صنعت نفت باخت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/22356" target="_blank">📅 20:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22355">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwtjMsch1ufA4HetBnHAJ2I2erjg8SNet83wjyhxdvEK84F7ELr4v26mBCEZfc_oIX5HH6VsKtaSQZnNK2B-rcCZYelXrk2KOmfYmvmLRz_Zxc3qLYumXLnvo1gK0JK1iwe3NbTq9BOsWl04w471hjswLqY-bj7ELhp3iyikPBfF1HmCoxEApN-_QyTut9ZSO38uKaiDRYTkc8-L5tTgF89jiArHdr89RMtPIblrZQwWS3NWMpyh42rr_U_6i6hyzrSNGrTu4OuACl59xMD6xAUf3lTDT0_UnjI4z6vvZ1VgrBLLBCVq6dGGZS6T1r2iMlRU4xtz9X90oRLx6OzALA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛‌طبق‌ شنیده‌های‌ پرشیانا؛ دوباشگاه لیگ برتری بار دیگر سراغ‌جذب‌حکیم‌زیاش ستاره مراکشی سابق چلسی رفته اند و این بار احتمال اینکه زیاش بالاخره به لیگ برتر بیاید بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/22355" target="_blank">📅 19:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22354">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rO48vIeDxHM1nQt_NHa9WdjnITW-IaBFNn-AqvsMH4oOjU5u5ZRIC58a7URUCoy6g_oJiLLRTznswg2I5OvgbsDUExZSDsBO4IYMU_Hv1qg1LrMAv0ojJ-EqQvNbBgjY9oPRwFBIgpx7O3UO5-14mkU4r19_RmbfEOSySeF92SjAZkppaUitdNyD1aI100i4Ubd6qECnF1vX-WKabZF7PjoRM9o6n2LjFOphXXXvQyKaDJQiSZDNBYurzBq5qHwMLRHmnE2UPejzJm48clI7a6ckHfVilHZWkuRdSMhJ-TjFuguiS0X2uAza0x3Ah9fiIKU5qWWyjY0U2WPPZV92kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ گارسیا دوست دختر جدید لامین یامال: لامین بهم‌گفت‌دوست‌دارم تو آخرین دوست دختر من باشی و دیگر علاقه ای به رفتن تو رابطه‌باهیچ دختر دیگه‌ای ندارم. لامین بخواهد براش بچه هم میارم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/persiana_Soccer/22354" target="_blank">📅 19:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22353">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGre-FFffyY6HEz8-7It02g8qwFexCv_siPvt_lK9q4g0ipVpEFrOOme9a3ShmKf7Ma05dQ9SdcI1flkK583FjIPVZgRx7rPk-N6w-EZW7M3WvRkVzB37B5qLKY6Jw83tSHiivKDR3k5w-055e22yur-be3Fpovm9OXSyzC8bJnbEh7nnnWmNHKC1em_LudEy5FPcyirtag6gglmb81sBSV8fUUi3Zbh9AKN3Got-dXPLjg9aKkUhAkY8dTj2v8ykryakNhY0kS3Uia9y2qtEYGNlqBR5xOOuhccr_nHQeIl8k6FXfDZyt-OR9dsVeGgjJuXNjoVydNYky8RQ5vNNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#فکت؛ آرسنالِ آرتتا جاودانه شد‌. آرسنال در فصل 26-2025، اولین تیم تاریخ لیگ برتر انگلیس لقب گرفت که فصل را بدون دریافت کارت قرمز و دادن پنالتی به رقبای خود به پایان می‌رساند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/persiana_Soccer/22353" target="_blank">📅 19:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22352">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/22352" target="_blank">📅 19:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22350">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGyuqKJyYz0W6VtwXAMhgyWJncdL3AtBLpeA95ylnc7uOb6Hmas8DlP2vjm1qidIi8VPf0uxRKInAwkSnGqlIvd_KJxwfkvGneqYvjmgfMOEMnBEPfif0k10ArjY943fidFPpHp8twjt3BXbMWXtqh0qifWipWRkaSeLxPs_Pi9SHbV_Wm4PODwKx14OBRrtfIDQcFYph5v0LML-gMH8oA4ylBWSA1YK-xI09jBQTyNsYScz2bTEnWDGSoy1unGbKyGAju3OKH3WnvPrb5AaNE_bX5aXkyfa6bMEY4XJs5A82J4lsqzIfnoBs6x6cNiYirOm5mvQ8pcS_jqyOp28VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#فکت
؛ قهرمانان دو جام‌جهانی اخیر در مرحله گروهی در گروه C رقابت ها قرار داشتند. تیم ملی برزیل مهمترین تیم گروه C در جام‌جهانی است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/persiana_Soccer/22350" target="_blank">📅 18:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22349">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dt2JHXTTsDq61iTwnFHi43kK1g-p4jDmagEufJT7asW-Mi_qTGtHwjBl-tMKa2ERuEQQMKVvSto8lz2jAvsMwrovcTSQiiik2-1KLhEAg1XOvp271SNQ0uPMSMByiYoIaFIFQxdC2-Ba7gFbhA4blqGvw7H6boM9qEjyaplDOT3SaOieP7JODuMT88sHRBsclE9CLJTMpbmE_ez4z2yeFQWS7mfCu_Rn0ruVB0gbcMjU3LP0fVwUNwStsdXe3twLER5fHkfS_hQcOeJgfkSwd7w6YBpJEXoPOpgDeKxg-XDUw9cuTKZSC2XCkKyZ2gi9eeqg4SCa_g0hpJK-BTd7SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های فوتبال ایران حکیم زیاش رو به دو باشگاه لیگ‌برتری که یکی‌از آن‌ها شهرستانی است پیشنهاد داده که میتواند با قراردادی دو ساله به ارزش 3 میلیون یورو به ایران بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/22349" target="_blank">📅 17:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22348">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/22348" target="_blank">📅 16:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22347">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxlhxWec4vikmYtDbIXItRHSiz_V0Z5cmEqaSJb-jaHg9UIglVJX5vUv-9eF9-PFVIBynzImyDAyespiOMyuw9czq21TCBlAvCijCoT6ATlV8GiL-NnXme0wbzS2sjQCY__7O1yD1fOG7rETUbFUic4Fe_PUHztzvEnDbVu7m6DJuWgtghAmR9y6qCFslhBU7xmAhG_GzRrhMakv7Bpi_tijKzwqqr5TdSizko7Xc6pLyTfBGHh_73-bC9ewLvkYDTyrGFBk1oBRz4hUjzfqiE5_xrgcVvkKW2DGQrrwkblCYyh8Ax6IMAvlEsg_Gx0ztwzZlP5VEvvQ4YgAQE6W9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نادیا خمز دختر خانوم پاکوخمز سرمربی سابق تراکتور: از طریق‌فالورهام و چندتا از دوستام متوجه شدم که مردم در ایران وضعیت خوبی ندارند و اخیرا جوانان‌زیادی در راه‌آزادی کشورشون کشته شدند. جا داره به مردم داغدار ایران تسلیت عرض کنم. مطمئن هستم که پیروزی نهایی از…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/22347" target="_blank">📅 15:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22346">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFH1yJW0WXMeCWizC5LHbFHNVYyzYn3IZ-ED18r5lU4U10jzfAyEoIGgDnACogi72mgkNx5sV_y3_vTFQ25abGR7C-pVSfzo1RbYGlufvQHV-V1fiFM87pygqQywj2e9lgDAXUU6HpacFFxK7wcUGPH_I45h-mJWUssNNZBDVvbS1F4JEJk0Kd_o9iQFfs4Imn2Os_YGJD8vAj7leU94ZaEPleGlv5qF0Cp_ByvM6_IOh49nOCxDHqfTWpKVd1VdOCJFXGEH_oVdcZYJ4dXRE-XBY21uD7MXcLLbQT5_tyGTak1U-7M5R_agr4X3ONjYU4dLRKNX0VeNu1khcOlR1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لوکا مودریچ مهندس کروات و محبوب مستطیل سبز میخواد بعدِ جام جهانی 2026 از دنیای فوتبال خداحافظی کنه. این‌ستاره با کلکسیونی از افتخارات از جمله برنده توپ‌طلا و کسب شش عنوان قهرمانی درلیگ‌قهرمانان نام خود را به عنوان یکی از اسطوره‌ های ماندگار رئال مادرید و تیم ملی کرواسی در تالار افتخارات این ورزش برای همیشه ثبت کرده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/22346" target="_blank">📅 15:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22345">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWBmPe_d4xPyR9oYyMcTBQwdqmszxRcMuoDI-ZSh_YWb7xU4KoNgdEGxBhSakNjRhtEIhqGP0ouHb8bbkQIkgMD-Pq9HVggh5FqlR8bmv4nW4gpaHb5_HiAEfQEjudEOFehknNSHm5kpFjyRa2TClxVAuLjFoHMyRWJe7JM_DwaiCfIdG-vhatD_Su7d6Ysu8L70crwCYeA3BPg7eTqi7WeimMXrxxpnmWoWHb-J9J29jFE5hMeIFicPjkw_AqV9taqfmkdM1bRiv9ym66BC7bT7pPswOxbBE6mejfS2GHokCBDJihg1mVqS3Un787Y19WcNba9BD7osdKoij7DFew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/22345" target="_blank">📅 15:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22344">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXCXlT7yrbtl8LURdqvUcMzlv_cmvmFZiiyBhVbRc0LfM1NPH8LKUKyZj8KcVGxOyPGRG1CcTIwWUB7EI95Zam0rEDXqvvRimCf7bXYNVXkUFExcscncuy7A8hKfOTSAIvYju1UTcO3u7QEu8jPgGUZUiOn6HAngp-D0Q4vtT7Ssq0zN7BCKnLKFr5QhFVQfJ-iVT0-fmPHeqERD03j_-1yxahO1LK410RhXPOvpym6aq1RVYjpQ-pPBnbspE-NyyinZhv4wskO6FcUGljeSRFgY2vPSsLUCNF3AyRfwz5vg88mCoZOv4MmwYV4rd1EZqOUWELIEYHG27FU3-qMyXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکیپ:کریس‌رونالدو از نونو مندس خواسته برای انتخاب تیم جدیدش‌عجله‌نکنه و درصورت جدایی از پاری سن ژرمن راهی باشگاه رئال مادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/22344" target="_blank">📅 14:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22343">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsFjPn8wZNPaVob0Ni1PoAaeCceN4Km00bGrGimnnFvpUFIJAMG5FknJD074vFFVBG5tdUYMVQakX6jOfmvtnHdhvpRIa6IFjppNOcArdoH6pyWn1AiO_5zL7U0ynnsJNNYwp4sq9d8Cw8bhcRnqnSwuFzL3I4xCgQKFsqu1Zbn3HKZNqYnM3dQYWcBg2wo-s3VXCQh2gFatKWKpFGhTFUZKH_naLMmF_f97Qy_5JmiKDciOkGHXSJ8RIHpt2WcPm2QBsiSJKAfqbwkIjrsFerNB7GAc0piAs6ofAxtChFZEbkJhooogiJ4gT9eL_8fLlXDoZm071zfqiqWFbg0kBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کنفدراسیون فوتبال آسیا؛ سه باشگاه استقلال، تراکتور و سپاهان سه نماینده اصلی ایران در فصل آینده رقابت‌های‌آسیایی خواهند بود. باشگاه پرسپولیس ازفدراسیون فوتبال به فیفا شکایت کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/22343" target="_blank">📅 14:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22342">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkSYYhMkm8NaKKzJRoTI-8tzdGeoYnBcIQv3DT_ParqTlhqlOLtLvTbvSnIF4yWIokbUvuG5uZDo2Ivd870WI92W1ghhYFVugWbNWX9chu4PRaqG4Sjvwh-1BhH_8HYgWwNbu0cU3K-oaTHbx0YtQvZIwe_SZM1IreO9RENjrCbj3MIqw4W-5tdqHrkSUwno2rTCpz_YXmxh3nArtk_w4eTqeFommuzSfIbnZNtlj2eigwtgz1pEpLF7ORbnRTYfwuOPpkOV4HBntqiJF6H5IDfJKvDcJEb48z1pUgHbffU3KvT4zQdXdayZeBQozUv_Pu_IT8GvePjb2lX2X9FcrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ رسانه موندو: خولیان آلوارز تصمیم نهایی خود را برای پیوستن‌به‌ بارسلونا گرفته و درصورتیکه آبی اناری ها باتیم اتلتیکومادرید به توافق برسند این انتقال جذاب طی روزهای آینده انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/22342" target="_blank">📅 14:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22341">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APls6X90CjIMH6aDUr50WsSv7BjTTQ5-z7Z8WbwIrTyWAjiRAhOixt6pui_IzqZNrZVdLyCWi_KWE5cg24YMzaGwGthIMIkRLJNT54X1TBzWZJUZIzMjWFUmDgotTjMRJ6hWKDU5wqQ1eprcGbdPGrJ9l6_-oH-yXYwuzq59se9Xf32i-SxFna9JB_TVTtvV0sdIzTxpc4BBiSzLzGivd8HgdCNUB8mhiq8DomR3qEmOVOxS6lmOnAt8pXllcmEjrhdFnSz7yjSo4CMnFIr4D1dr2lsHW8-dMWwRXdD6n___GhJIOGfgXbATgUUm7bgrC1-NRhvlN6mgH8qDT2DloA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انریکه ریکلمه نامزد انتخابات رئال مادرید: دو بازیکن کلاس جهانی جذب کردم و اگه رئیس رئال مادرید بشم باهاشون قرارداد میبندم. ممکنه تو همین چند روز اسم‌شون روهم‌بگم. ریکلمه‌درادامه پرز رو به مناظره دعوت کرد ال موندو نوشته پرز قبول نمیکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/22341" target="_blank">📅 12:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22340">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuwueplFM2VUrEWBhy9N4UJWZ40Bqj9iwWPW23koxL6LVrcP0vege55wx5abxA62xjoqsvRn0ZWR466e6jF2yLwzEdljJs4LEuTrGVNxzWOMNaPKaAnKAHYvnTRoe82jlh-G18c-gfBtpDheo-fj7tmCnNB3vpGTRoMapnQiDGW4k0YXAoG8TIBEDdPluBx4egxQ0MEmoNaiV6ht9VPIaJkwZ4Z6NgQkBmyCWMMv0fOFNVE7pIXOFzqsAFytNzShj0gQ1piaAb62lCiGMZxsGljbSa70k9sr4DV55125ftf-vbESLEt7OUYh6ve7bRneF1qhhOaqa1gPFHGCeMQ_AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیران باشگاه بارسلونا قصد دارند که برای‌جذب خولیان‌ آلوارز 25 ساله؛ فران تورس همراه با 70 میلیون یورو به اتلتیکو پیشنهاد بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/22340" target="_blank">📅 12:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22339">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRr_0rEDfsAwJVoAUV6DIbGZBrsYQRTqG_mkKrmEJYQZfnBja33CEjS_f81hsXuLjmLuoyAdLK-U_ljq7RlnUKlSrs42tuI8K-3gCVKYCbpPhEvPFHNo5C0K8j_SFmWku3Nj2Arck2R6sxWeSfdXNCZMrfZuIctxdBny7oWqPQj1CAc7uIOZwANgbaGEL9VRt674-12Ya5F6NJ1kpWhQlHCAmWUsv5_hzbZ4DYDFlZRg-jB6dNeFuRKeX_gzbeg1Xh4dKgG1THeuMYY_ArIxJ_VIkLLuxAZNrrgF8BtAUE0Sb526ygZtfHFlpUu_WB3Q_u3gYuKT2xiAEqQy-07BBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
آنتونیو رودیگر مدافع میانی رئال مادرید به دلیل مصدومیت دراردوی تیم‌ملی‌آلمان در فیفادی از ناحیه ران پای چپ 3 ماه دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/22339" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22338">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJLgwSA19lJqb8K8PD3nKNiMMSGKWBty9d81x0V98-9AgdzxZZ8onWQhwDswE0ZTdxq3G3zxBIyIRHIujqVq2MDcPuCnLetcxJKkkw_PcWGgOIWLcbOKjpgMBpwina6K83cbQfzPyFKz_w6QmtlTI5L0sHKE_eLyb3Sa46SeKo8TWbTAGHiyVelBGi4dNql5E5R0yImIrM06X1YeEh-Nys_gHzrSlVqtZJL5CAGQqZUhaMhvl9fiFg5di20FtvcgWDxiY0V2hc9UzFNrt_uAiE15qg8q9t-_0bGLS0AglBINS5aNjL2EK0dFTo7M2JLdtNmwb8wxtdUrt9aWOurxtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی تیم ملی برزیل؛ مصدومیت نیمار جونیور کاپیتان سلسائو جزئی است و او قطعا به رقابت های جام جهانی 2026 خواهد رسید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/22338" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22336">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/22336" target="_blank">📅 10:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22334">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qjcQ6ZYTu8rhQzWkJvfan88qphZqygncNope8HrDmWu5GaR1JPcuLpyc8C-Y2kKXxZtOmTUIM_-Im7gyq8kvq4-oWbJfnzLkGxfvaDvjYupxmZsERXq1geObPMeZk4yFblm8rWvEQq05N8W9qr6VIV8FaKMD2gMI45bVqoDFzoKg2CUsWACa5ybyZ_tMpi6MpqiZEa1o4szP7ldO429nHd4AgYgZBcMJfmJwFQcBvE95A_ApRPJFEf--8F9zSC0epX0p6CtXIAgPu2fzyqOHpG_pDvJaBpjq8agtraXhjuPp6UjYmUBT_MOyDSJjRWEmmhpjOvY5Dlutge3MylVGyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KKsfKFYC6gZWobqJ2ncczuAdB1nMxEfozd1f9eGiEq4u1lOWU8MO8kFcAgVjn_1eJi-YNjUZTGpjZUiQTqPuKgcdxmLekBCxxouO8L84gjmjB-hAsLPzz-1pkWOCxdVFPewu6yL4FNQPpbiyxzyb9IRxlA-ea3O6HMjU3v5w5TJ7bBavU35ImKFAxeGxORJSQtPuYp9gJvJTZYe_I-ZbkmqrDyooiOV5QCHXVxyQeVeMn0-6hEphpONhn_ConI6Wi5mje-0aTPeuu-PNR9BYs2FNPvkaQYVTv-3PasNBtVSBE9VYxhFwVXnWHPDZcXSc51SCLSNHvpkKDrIhpKYLew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#تکمیلی؛تموم‌سرمربیان‌حال‌حاضر فوتبال جهان که روزی شاگرد پپ گواردیولا در مستطیل سبز بودند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/22334" target="_blank">📅 09:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22333">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFwe3bgpyu9HkRx16i_oASw4VAcZEmV0EGfZuWs4vKpgknLLD_eqdIfBxhjNLff2vSgUpcZ4XmSssKBmhFnZBUljzHxw6yyrWR2OD0uaGApDinEkjnUGfiRtGgnttfaAHWYDoGChmbCXXkSySA4z0yLiirzq5vsIApo7YNyACkwM8eX7FaagkAz2vAhKJ7NyeqAy5lVme-Fne9ol0uewxppTVaBVz-T7qSovcVlhZH7pejIhNKmOnUSGg7iOUGTEoz79gj6D1b1TWkdZABSAYyY7QfFx42_Mo5G62CKmtIXmAXN4ROUC9UZTsJzLe83Q3WmPFVBBdLYnKl15U7Tdfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ نماینده محمد امین حزباوی امروزپیشنهادمالی‌مدنظر مدافع میانی سپاهان رو به مدیران باشگاه پرسپولیس ارائه کرده است. درصورت موافق با این پیشنهاد به احتمال فراوان حزباوی راهی پرسپولیس خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/22333" target="_blank">📅 09:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22332">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drspk5_zMHjltM9x6dZ1nCzUkJvb_EK47Zfsn3ntRipDJiaxCQpt4uV29MAD-P5_bI4kfP-Opc37ELDzqBD2S4g5kGcpxEs67T_KmNaHnwEMdxd34Z66ob-3lRiqtK7ZoW2UM5vlUQeD9fnL2oLq4XFuU5IHRqd7k8lNdlooaeRHS2nX0OXm2eFIj0RwamWT6Wr5tpNW16EZyqwZP1lSvBd0FSKe_v2MbOa1smP1QC-nH4tI5l5BD_BGl4MeK5riGKNL3_OFddm5qYPKrmVB8WrFyFbEqeDtUtLWLM3vMGq0P59Ysb4AcjTW0Lep7t0WT793YJqqxeGnEkINQoR50Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ فوری از رسانه مارکا: خولیان آلوارز تمایل خود را برای جدایی از باشگاه اتلتیکو مادرید و پیوستن به بارسا نشون‌داده. اتلتیکو برای فروش ستاره آرژانتینی خود حدود 150M€ میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/22332" target="_blank">📅 09:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22331">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBTgQACfYl_CN7dTBCruiojJH7S83Y8KNhxrA5QSQWCiDksSJhkYqdHVqLxMB6XQwcdglK_MI5YXDqooduH3XtM78AA1LzOOBpk2o2qWdnOXj8rJwD_YFfVxZSlkyMLgT87D0rFHvcFT003r82b8fXFfResjB0sBcb8ICEyHE8RkCCBEt52J1ND65p8G4f4ubBubfHTgZTLtLDtC6CoZuyYjNy23YeLg5Ou2q8MdOb1_ApTfd5j9OPpdv-l1y-dFVR2x7rSg2z9XJONqdsQdvU4Af7eYJ0MY8qC7Wh-zqiwGA9qZxmQ6RlxsyhsshHvkmHe423vO-nlGZknY--GQ3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان تاریخ رقابت‌ های جام جهانی؛ میروسلاو کلوز با 16 گل‌زده‌همچنان درصدر جدول.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/22331" target="_blank">📅 09:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22330">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNZkyQt-csJziWOOxt-vZcsKRMYJzdIFjozjMUXrjoZrB-xmptyw_ICb4mesTjHLfjcsnfRkot0oVfgSLLPTwaj0uGz4lpPTAxI81Gd61jABJ6y_RCA4BPVGXd28VHcBduaFs5XSWKD0Q_PsBVdbiUiw74fS4QgLa2n3MXy1oSvBt4KWi-jSf4muXMyntM1WeQ1gD8texZesDLyTMtueim1krdqakbinqw_SJFi21JqGPRcJOlO-3UqpwTuDV54RP2iBj10g90k1DH7EGSOPpF69UmdCoy2faw0JxsqRYNPiX_SaIbwEot-jlZkcJaGjIBjITGtGLuwSXB_G3jc_JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌پرشیاناازتبریز؛
مدیران تراکتور با علی نعمتی مدافع‌سابق‌فولاد و پرسپولیس برای عقد قراردادی دو ساله به توافق رسیده اند و بعد از جام جهانی قراردادش رو با پرشورها امضا خواهد کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/22330" target="_blank">📅 02:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22329">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4F7Mrcyen4mGRJeMAwNGRg1RAicqa5TRr04FAaPron1sEjaoApZWoHc2yHd088iq4ZoZTtooPGaTeqnYV7pnVRzTVW6F2uyzWbQjmGb1kUchsG27m_TcoTF_hqcMXefIDGudLX7mEqkRAkQ0-g8zn7SRzq8N3Zr4R4totnNliUP2zFdnJvm79grpjJwMq1BM-N_FZLMBXus_dvJhrkTkbmd0905yL6jST-zfVhzhe6V1q1hoagNcLsOBWBVJOyeTiZdDaqwfA_GqrikKQ5jHAx8MTrGxI6UCos3DLpVYW10jboGQ85v32h7zZ7twtkpUJEhCCJT_iZwgu00ZMl7jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/22329" target="_blank">📅 02:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22328">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339ed28585.mp4?token=bBdNveu9r0HxNkXutUtVeGQ_aWioAGmNvoSOGHdQtk8IfnrMeZj3UvAKkLefDiBbvf0xu3bJESWO-CO8wunuOznEXEPR_22JH4lZ9xnNwFiM7NxfGREjaTzt-HBq3ojqWUO7CeNcMlrHFZBWj6bDSpytXPSBCHTYklKgCbhccgZCCdxK2d_3k56ECj9pd2vkXgqIFUA1DsK5Sw5bfdeNR8fij81eHO6zuT2_VdQt8w5i4WvWcBrpZ51hv7TlMak1GH_P5-vM9H_4jw77EjbfD21c90yO4gXClZeKP0ykpub6N6WgvRnmeKpLPJukJ1rdCrKuV13x7ihYDWuP3dV7dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339ed28585.mp4?token=bBdNveu9r0HxNkXutUtVeGQ_aWioAGmNvoSOGHdQtk8IfnrMeZj3UvAKkLefDiBbvf0xu3bJESWO-CO8wunuOznEXEPR_22JH4lZ9xnNwFiM7NxfGREjaTzt-HBq3ojqWUO7CeNcMlrHFZBWj6bDSpytXPSBCHTYklKgCbhccgZCCdxK2d_3k56ECj9pd2vkXgqIFUA1DsK5Sw5bfdeNR8fij81eHO6zuT2_VdQt8w5i4WvWcBrpZ51hv7TlMak1GH_P5-vM9H_4jw77EjbfD21c90yO4gXClZeKP0ykpub6N6WgvRnmeKpLPJukJ1rdCrKuV13x7ihYDWuP3dV7dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طولانیترین‌وعجیبترین‌قطعی‌اینترنت‌بین‌الملل تاریخ جهان بالاخره بعد از گذشت سه ماه به پایان رسید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/22328" target="_blank">📅 01:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22327">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnOo3WsSpAfnp0oXrkCxUgH1tOhzUilPtxz-XLPabMDsLAEGHrB9UVEiRsTqe1AgP0YaM46N6oQDwrPPLYQyEYWqb7n4wjT4rS_zKTtaKxfMAT1dFjFswe0UFeGfzv3LglJjS8kjopkenysFL-UEh6KBFBltRSylUE3IEXa5X_x64gvWe2hv1vflrnHa2tKVA6ec5lEiq-usuNFJzh6Ku0nHi9-9c7NVK-xacmsPDAisvj8nRewCwBCUg0wF2aYevomtPQWLVsufkgssDBcNmGTOV_9xPyHxLDTKj_LiHkIphMzpLvxA8J0kwOWLiNvboRXpvPKBa6B0aufB1H5SFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ سران‌باشگاه آث میلان قصد دارند که ژاوی هرناندز رو بعنوان سرمربی جدید روسونری انتخاب کنند و مذاکرات بین طرفین آغاز شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/22327" target="_blank">📅 00:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22326">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hivPA5j0tptXfiYYxFxpvnKd0wO00XMiXozjIUQmh3oHMzAPDU1swL61KFfoDt-JPGMQna6xOffIcZWfg6f5lcQ7uysnrICu0KRJCKW8SG5Jbw5m2KX3NqdUXJ6dJCwN8fvcJB36Cmq4mAYT3vL-ST4OpcRrxxjaTLxsqOEvN_6c5bO4XSlqqc6zuiftxLKDlKU3SpWK-QUv-vX3LuHEe3ZAKEaw_9s07mnibC4Pv6l0OEtmee8mi_xdVhMoDBhsps03LgIGakez9mx7w3-X4E0VL7K5r8OCxBC5VqEnOsCn-uYmuFMniphi9ntI-IVCOe2Dp96A4t-U70ZJhugcSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه استقلال از طریق یک وکیل ایتالیایی مکاتبات خود را با فیفا برای بازکردن قطعی‌پنجره نقل‌وانتقالاتی آبی‌ها در تابستون آغاز کرده است. برخلاف‌پنجره قبلی احتمال باز شدن پنجره آبی پوشان در تابستون بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/22326" target="_blank">📅 00:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22325">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/437e19a5b8.mp4?token=BmLcH-aMiKHjno5NSAfN4wwCUiVpH1aaWPay3u7aTSJWVwQ-WKAKr71fu4c-CwH1Su_Weg7CMu2EO_wEGpJkUg-LZE2-SNZuDKvLvWINuqHzNI4nqOPSm49J7PDLpGWWC7V8JmSPc8KNkzKADB9fzBcv2_27-ibtO1wwNcR-ysXd6rQiuWJ8XrQYTpLgRN3HPOGj9vpmh4mQftKB8Yg0e-Z_KGN8wCnTyLeio9ZIYt6PcVwsoTcdvwW_RKjDJV0A3oPNcUbfUxP1_zPjCX-mO_sWN98P9uvfjiQ494Fkm9-U8Qs0M9g_y5PSkp7PWzWdBERT8zG06be6BRoMabo7Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/437e19a5b8.mp4?token=BmLcH-aMiKHjno5NSAfN4wwCUiVpH1aaWPay3u7aTSJWVwQ-WKAKr71fu4c-CwH1Su_Weg7CMu2EO_wEGpJkUg-LZE2-SNZuDKvLvWINuqHzNI4nqOPSm49J7PDLpGWWC7V8JmSPc8KNkzKADB9fzBcv2_27-ibtO1wwNcR-ysXd6rQiuWJ8XrQYTpLgRN3HPOGj9vpmh4mQftKB8Yg0e-Z_KGN8wCnTyLeio9ZIYt6PcVwsoTcdvwW_RKjDJV0A3oPNcUbfUxP1_zPjCX-mO_sWN98P9uvfjiQ494Fkm9-U8Qs0M9g_y5PSkp7PWzWdBERT8zG06be6BRoMabo7Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گلزنی فوق العاده تماشایی و دیدنی پسر لیونل مسی از روی ضربه کاشته و یک خوشحالی خاص
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/22325" target="_blank">📅 00:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22324">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfbszOKLc3EP_5WHDwwE7MtAAKjWSvez-4j43NkeADKBiuaGwv4Y1rg-NpqBEjzKlaRMCNrqBqjv47rAsgiLmcFUAyEPbsZnIsEPh5EfAHjCaGTAlOHBMvCNniz_ylC8Y6H0KcbQq9YG8qMM-26IDDRStVXMb29I3wQ5z68lHnMbZrAuFAVUEjFwaBsuuRW5272L0oDAnwufRW3vejcjv8Ik25nX54T7EPBrHc_csn_523gk3N0gMtja42eCtJnw89vDxJA65BZZoqHHlKcwjOtgsT86erddGHnW4akAHORgxN8ol6lJdARgjXxCkcdXvJvbnExiGQHgbsewKQHE1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باتاییدیه رئیس‌مجلس و رئیس جمهور؛ اینترنت بین الملل مردم ایران بعد از 80 روز تا پایان همین هفته رسما وصل خواهد شد و نت به روال قبل برمیگرده. ایشالا هرچی زودتر همه 70 80 هزار نفری که همشون‌جز خانواده‌واقعی‌خودم‌هستن آنلاین بشن اخبار نقل و انتقالاتی…</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/22324" target="_blank">📅 23:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22323">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6lbA_W-JJgH8zDcwCpd4lEGTsFqWNvS5el6vWCVJ3ubTvSbA-YLjggXnCCJav5IsDrNr0b_-FFcXjRsTwduWLOnLhT5XhfMFxuQnmRAxXoBCunMGNbCtVQE-n4EvpsqUVkqt305yWrhCfYP0fERReR95gjGkfzphdgFw-GEWJVPCM7R7ttLwWUV2m57-p4WU83NPeeBqTN3edN_IQLfO4PLvCzFtcUN1kPlCP7-MhyQdYF5HOKLoiF3oPwyBVCHf93o0-Q9AM0d2-9PUa80tFMWicZwQZoVG7Qtd3vxoDPjBh-kc5kwzrW2cZ0DLy_vI17hXuZcbch4TcI5VpA93Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معاون وزارت ارتباطات: در پی دستور پزشکیان برای‌بازگشایی‌اینترنت تادقایقی‌دیگر فرآیند بازگشایی اینترنت‌بین‌الملل‌رسما آغاز و تا نهایت24ساعت آینده دسترسی مردم به اینترنت به طور کامل آزاد میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/22323" target="_blank">📅 19:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22322">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IaXKbtMpJS7UUwEWDx_gTznmFMzBWDCUm2Athc6WTlID--e9ZwdCq_7kSagqiHyWOR4OaC-pOXV2nbh0Z7Pf-sPqL1gHGhQ_bxl8JdZv2ukD0s6GGw4ROIwZyVh-hDjfLm4vfyRBkIsBzqOaUM1HKuqpaIhI7_N2cvU6ZGe_i6mIA_dZ0HcP0msmxRcfUxUyByCxW4CSM5-FOXmLoYlwZ7xAelCp1h3pnk4M9kYhj4jrE4w1fpo3fj39-V2Q4LBXyjfUYMsId5YAI1it6NwaleNFx9Zcu0o8kDaAPhbsA6Ktag6e1MF58CyQcsqAVmDte0XR3kqyQ8xKi5eZ1d09mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معاون وزارت ارتباطات: در پی دستور پزشکیان برای‌بازگشایی‌اینترنت تادقایقی‌دیگر فرآیند بازگشایی اینترنت‌بین‌الملل‌رسما آغاز و تا نهایت24ساعت آینده دسترسی مردم به اینترنت به طور کامل آزاد میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/22322" target="_blank">📅 16:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22321">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qH9Lodb-LL3AlZJN2S7e1ztPKJnLxWE3kcpfNf977MBZe7e69tXKVFbce4i3QuSywatAl-8X7rssyE6KeItSJnyo7Gcy94U0P6WdGZ3ZtKyeLXZjH3wlWGVPVKS5-XJ1CZr9xeeFOVGK4sSMTk0QDwndm0n04ZPv7z93Vq1s4fIpB2N1r3Wly0-8VhiN1D9QmeXdSeXZSGyTGfzsyAA4GdLiMb7oSg07YCnRiY9EvpsR80aZq81oJTMvdwBVHjOy8TuwOLlsEk2wPwoy8F1vW3NB1iUCQYHf1tqnOsFmVSIftxEY06YEmbRvaJKynQUPix7S_gUMvX3GaXrrbfWxYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ بعد از ناکامی تلخ در گرفتن سهمیه UCL؛ ماسیمیلیانو آلگری از هدایت باشگاه آث میلان برکنار شد. اولش خوب شروع کرد ولی بد تمومش کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/22321" target="_blank">📅 16:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22320">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2231444b22.mp4?token=sjMU-zSxJct7GrUE-3HlMwnjRQ61RGvGwYMmW3H1V1ibzdWxtEtOaTN5eM4aoc0sO8_XrRKw_oKXAqCyWXTN6Ycvt3LJMKnX_nYol_x3JnD7ECa5q2TYor7CYOR36U66qjEFzghaRlFkP0y5KR1vbkdP8uW_P_O6xAUaGYKYNIex1fE3YtdY03M6asCIsgY_E6UISK3sW0AWtn2uzfw4dsbYVXJXk7PuOBp4WjDZ-OD3YZ7aTyeq7wtY0SD8KdLcf2PtiPapulQsHaK79iQ1-6vuk-11iskpAx6nJqKUUntH_tycRA88JQga2cpKl-uYx2_NC8911k7BxB6vJ9cZvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2231444b22.mp4?token=sjMU-zSxJct7GrUE-3HlMwnjRQ61RGvGwYMmW3H1V1ibzdWxtEtOaTN5eM4aoc0sO8_XrRKw_oKXAqCyWXTN6Ycvt3LJMKnX_nYol_x3JnD7ECa5q2TYor7CYOR36U66qjEFzghaRlFkP0y5KR1vbkdP8uW_P_O6xAUaGYKYNIex1fE3YtdY03M6asCIsgY_E6UISK3sW0AWtn2uzfw4dsbYVXJXk7PuOBp4WjDZ-OD3YZ7aTyeq7wtY0SD8KdLcf2PtiPapulQsHaK79iQ1-6vuk-11iskpAx6nJqKUUntH_tycRA88JQga2cpKl-uYx2_NC8911k7BxB6vJ9cZvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
#فکت؛ آرسنالِ آرتتا جاودانه شد‌. آرسنال در فصل 26-2025، اولین تیم تاریخ لیگ برتر انگلیس لقب گرفت که فصل را بدون دریافت کارت قرمز و دادن پنالتی به رقبای خود به پایان می‌رساند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/22320" target="_blank">📅 15:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22319">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7tWa1FAVdlwVZ4qPkR1IgerSdKM0HlsiihpYArYD-pseTdlCCBmpcMco2YYd-1exU3lyw1CXKtJpa3KyPcSjDyIH1LG9lSfhaS3PHHzafXFkq6vUqEqdWKDzS_gH8bzH_yd-ofkl1vdzXEPgueKGzl1jP0ePwIj_hVFiE_INpj-d0R6EcxvBBwQye0A3pj9IV7S1ixRzhfOn8_niOGEphfoAygkVLgpGUm7Japa2o2fmwtlU5YyAdHBfNvru7t2G0tZp6u6ncDfCpIeOo5DOqLJ4yzK4Wr_NPo9j8I5HPp_nL3CrWLD1hMFwaCx1Fv1AE2Kf9A1YgZV_V_XcM1orw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/persiana_Soccer/22319" target="_blank">📅 13:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22318">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqWpPISQNAjhIj5xTAi7I2PDULNLW4CpmXZVOyMIABS0Mw41cP3KdKirb-PQYj63g-tpafCd7AabKd9zmf_hudJUmH94DrcELON6B0n2T5jkfXlG-yFdOYxb-iARXHVP4x2VQYxUuJbuGcVaeEHSpccvSAW4UmRXKFml5UB-YHKlRKjQL2D7MJKzHcmy9tHMVBk2R2BmuqUi09vV49phiKyORvIc5pWaUXGeluWtkdQ3b452YF7Q61tvNYQYoVcQTlOOcKoqA7roRd-rThfYoTxOv3H-4BRM2hGkEF-ZnqlJNCm7bWdmwaeWG4cPVM9Cck_FFgl5R_UowgGZPgJt0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛مصاحبه‌جدیدپزشکیان:اینترنت مردم ایران تا ساعت آینده به روال قبل خود باز خواهد گشت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/persiana_Soccer/22318" target="_blank">📅 13:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22317">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJMg5-XyY9mbUA_qrTzIKvS2KonGFgGgYl5iBveikXnhiG95m3B1ENHxt1BuimbMBouGJ1Mm7fhyCtqpRuROPU6uBzI1d2SiIsM40lvFdNqxweWIFWVyH3z51ngthTzICKsYQ0vhvja4b41JC3qCDqTpcSrsJzp_QZov6Ivj_EnZFUccJc4Kk_qCdg5sF9UAxMfwf8jbW4_4i3IJBWDS0HEOhAjvj11KtBn_GtBpa3nNrxeZiewbDfP0UbxDNybCzRqCGOa2q1mJV6G9rJbyXimvRLCZM6ilcaTOHai3EkXr5LP_YMJvZ9eV34gl67T68FemmtdoMbENUi1lmHsFbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه کامل‌های مسابقات شاگردان روبرتو پیاتزا ایتالیایی در رقابت های لیگ ملت‌های والیبال.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/persiana_Soccer/22317" target="_blank">📅 13:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22316">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJ1VRKWLp8bM0NzaiOQdK8tHSdf8KLLZKd6BiqYIEqB2Cahl-S-XyBEbnMz0W1MKxK0uEanSVB6fOmkZw5aCuq0xrckt-_6f96X-7C7bh-6y1klF1QDB_nOkGPKEUAP3rgee7P7jHJaS8FNJqlag_jpx6XSPDzh0jVzc3-zf3ABj3TzAEVAj8RJIK6H05z4tVzWK3GDIVz_GTTeDRnpbcHT7Iydb0MjgH2tasJ5C4RqTFLtIMx9H7ziULOthHLjFLb8xirXcVH1eoCSPJ0dfxByYYgsPYYZf3Qb_6cgJyZvAMINL3xcEMHtL7CuD3GcWoWpKJ6jjEHYXn7BJSYb_JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇯🇵
شهاب زاهدی که علاقه زیادی به بازگشت به پرسپولیس داشت بعد از عدم تمایل مدیریت سرخ ها به‌جذبش‌قراردادش روبا آویسپا فوکوئوکا تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/persiana_Soccer/22316" target="_blank">📅 13:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22315">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F57h8doYFLhUUbHA0ue9vsA9KwNIuT_L96lG3AjrE_N_1XLruCvBP2DKklygJEPNEsLq9XFm4cVYRDx-ZDICr-dsm6RvuD8Xbkb8PwEkRphtDLwMkl8qSqyExc_WVz-C4fS0j-hAQsfUgBkjtIaUA9n4juFynC_RSX4lmFRxG423QsIwTLI9DskU969Xkkc7lJ9h3BHk73bOCJUroIlUu57cQIItxl4ww20LP7mo8d4tqD22KK3KmRmAIv4QZC802ZXKSMC4Jjf8Kq3I6fpGKwSC34_K-e9v_U32jRCYQWN0NBLWZZXtMK7WoSYY7U__HvyZVOCSXbE-YdNTJT_guA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی تیم ملی آرژانتین
؛ لئو مسی که درمسابقه‌اخیر اینترمیامی دچار مصدومیت جزئی شد مشکلی برای جام جهانی 2026 نخواهد داشت.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/persiana_Soccer/22315" target="_blank">📅 09:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22314">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3xDC9qQ_L_A0R9IrEKZntGhnpmfbFAqaDH3ydR4jCK95JU2GsvEI0a7-hWPDvQhUtTrNN50sXvlseGlArsxALmo0GpmauZuPLyQdZiK1ZnSI0_im2CO1I0UWIABzuklPnCJTzM5M-4idG8KJ8AVmUk7MBIoL89mUmWgDlFwELz_4pBcKbvWTEc2YDpoZn9FVBWOibptqvDIm5oULvTOLH7hs3HSRH7RfcrZTGZNAqTfePN4CAbMwAHqi_MSV1CWVBM_X-51sFZ_MqPtJF7ViWBy10TD8JCgJi0cbQx4OLBslt3Ruz-0qe_nSFzcgQV2Y_sylioE1AjQ_2P8Yz2y2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛نماینده‌خولیان‌آلوارز: اگه باشگاه بارسا با اتلتیکو برسررقم آزادسازی خولیان آلوارز به توافق برسد این انتقال در تابستون پیش‌رو انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/persiana_Soccer/22314" target="_blank">📅 01:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22313">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jcxtjh_UTRksodrvS6SgmU7AkXhI2FHw3LkJOWPQYvnBoamz3Z970c18mnKJEzCCxKn7PJtGbGwjshr6C72g8TSmNQy9wfUgCGILtiIEKGP-JE9ZQPJK2-oxNbCHSG94Uqjjx5enO6OkrF1aciz-x1qZKg3-Cgbnfb3ZDI2_Ka_3pBmqWDa2S0hTpf2toCRtngCVnmjvrdzrnaUee7Uux12-8mT7YGyVNxXYgERa55aIOT0mr1AmXhEnkJRpERoMdl0TL1hGoJ_UgdKdxMCYJXeW35qCnPkatM7pXnob3QiJ8cxh49g3fI-OTz0RPfkvT17XPm_FaZMpWj-BM-iOxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ طبق گفته رسانه‌های نزدیک به حکومت؛ اینترنت بین الملل مردم ایران تا ساعات آینده وصل خواهد شد. انشالله این آخرین باری خواهد بود که اینترنت مردم عزیز ایران قطع خواهد شد.
❤️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/22313" target="_blank">📅 01:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22312">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcPfYhg4tdJRbeik8P2x96gf_PI6EABON-K4cZmSIo0JNE6_XR5MzauHszOLKjG42nluTFcVpSvbPEyuKM9vxnWZzU93XXamLc5iYTTl6q1tPg0un8_1vGyPDs-ZMbokHNymI-7rHqsjHiTfaMR736zeiuhbpIQq-clIKDVV0vnZKs-W_71Upa-3txZdX3GKuHI9gvMp4Hw1_lENgTI-0NhuiyTyP7lWpQHsKFr5gnEzAQPTc3Fg9opgzdkepsftRyWjbiyok2h1gPFlC8pBMm0uhQIKdi9BNG8omqBYV_WjTdOGO0SKHm8KwjkOLn1vHLqcCcfUdYC5KhYTOIYpkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی ؛ خبرنگاران نزدیک به باشگاه النصر عربستان:احتمال‌داره کریس‌رونالدو سورپرایز بزرگ ژوزه‌مورینیو پرتغالی‌برای هواداران‌رئال‌مادرید باشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/persiana_Soccer/22312" target="_blank">📅 00:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22311">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/po0I5FLbabm7V7M1pKXCbaJjdVxJk_VHZpVNKUUqg9VOPRnA3KQeiNRw8dcqIM-HRSrOTasSC80Ix13nDwHmb05edaurWIxE_iAlPcVlXazXEnrZv7s1VTmfAEjw6FzosiAaOa0I0xL-iRDEYUutCZ6xJI-UziPk2Saz7xSDwqV4CN2aV7rTGFnadygOlgZgKzwEhx6KJhlQU3LGxM244Hq9msQftauURlU4ZSrOf2YHjJyeAxh0M2WpR52HsjTZztsu1NezcsllOQniyd2OyL6OhB-OJ6M0Thfc8AfeMy0KereuRe8EtcfRuQYwPyLM0AebAG_pej24CmcIESEZWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/22311" target="_blank">📅 00:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22310">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBfKXilY3qi2E2TwaoDCWsfAfm5BQSmjCITmtWcbFACj8QtP3_rjvHOFQp51Tm5pmatPKtx3YdBnmUYIe6fW5qj4dz9odkqxjDd0pLIGL6jx7bXCG-iUc1BFv2K8BxModeZZIQEugwydUVyw5qhGjkpeXSO5XoFszVbkwS_a-KdO-zdryR_LxPZ_oUEy1ZAaeHHhQKadJayUsBNQrd2Bcmj3EUuOkAmfpNJccDnwKmk_eqzoymmQU9GS-HMyypZqVxiYGwrAs12ujf1woPmPr2lfJUf7_oGVKfDJUmWHphLSDRAe9jiD8YezgEOFnBfFQWh879uEDu7gUXRPNmL4Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/22310" target="_blank">📅 23:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22309">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMqUSTdFsy-IN14aV8nwkO8uC8dbebijZSgQ5FXv0D65SnCFepj0V5MKSW6aqyu70glWE1IOQommjROnEd1XTVNeh0JJZIY-Moe9zCaVSuPHdAYFKF1QIVplvxkwj-Tl3cVFTRQEtrIDo23YYD5b4R_P_fJWefWG9Vnc7iHWybGpB1b_Pg3qgqwzCpGp-148-6Bcjm-1cj3U6FJTAXJvzOaBsWFAXgVmX1XPb3XoS7w6uA6dlPGP9eXm0PWtBzSlchDptZctIsgoCqZ24vaIsRI-aBxkB3zadVVNXuq9eholY9R9P8TGMSQCpLQj_p4vbkDbOxth8qaCYloMtC77Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌سری‌آ ایتالیا در پایان رقابت های این فصل؛ افعی‌ها با اقتدار قهرمان شد. آث میلان آلگری سهمیه UCL رو هم از دست داد. کومو با فابرگاس اسپانیایی راهی لیگ قهرمانان اروپا 2027 شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/persiana_Soccer/22309" target="_blank">📅 20:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22308">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbo-VQFPvgGXj_weKaqFTKRNQ5uYFt4RWjaTfh0Tei26hHhpT1GWYdNBmFdBtpI_MurEQajIlcgIlGDP9HiQUf4YhHzhhXZitNe1ze8Gpk4x5qVceDyhBwY-PFoPPIZ0MzBs6C8HiINUpnsSdpIJhkQqc8C3S27HeFmgj3tQKFHk3Fin7HKfCEpNDcQ3515J_ipbiWctrN8fBrnQlWvng2j4Scvq6bnkDYoy9PmF5f6b0Br3YqG7yxwEmbtaS91kqS4XT0egWlE8PGIXFtC4UhHDmxFLf-pvcH8z2tjvQrfbn6d9E8g7PrGh9D2rTZQmJk_HRuENhkk6VlE-_221ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...ایوان سانچز ستاره‌اسپانیایی سپاهان توافقی از جمع شاگردان محرم نوید کیا جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/persiana_Soccer/22308" target="_blank">📅 17:32 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22306">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/txqBZOP0rshG2kFPMswuZj1jQHUZLae1DTcIDMHdynOCkvCYj11LlXeUZmCRTLbiQg5Mjzmd1PEVuj-9kaHd4RcYRmTLXa0oRifWUPwxDuMno6kzjVxJXd_gxV3OgxtHAKR_NMSvXI45NrfbtlyDUHO-Z5cV6xRF-NpzLAR-yJw54ETLnxp3rfwUVXhsea7ZRC0r19QYk8nEXYpjB9uIo315MA9mqWItYZqD9xwXZXYGR-HPpg-2ooFIxqU-kkzqPhy91_BqU8M1NNRe77DLSP89nrdaFbfOwGtBuPLP-3BLfKBn01i3oDftZT6hDg--ythCAd5DbXOG60Gd8OqQkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LTAHwy5oF-ugyBY3otczob8D1YzKpO2C8RP0uQzFqmp1YMhI_9NBVBKQMOPAuTJSUXsMdfusOV6L3NAX7IQGgS1wM0M3Wpp1V2LIHmmFxclJKzBKyrVixiuwLRQHBMLuy_DL5WlmhIn6TimlkgwMoAsDZliZG9MtWVq8Z04x31IQjSrsitOmhVueq7E2By8NiPqOkV21GnHlK2usQFdb0uslKLA60na4JaWd9nw7uyFk4vmKq9G3NMnV2vuHe_gBQ52Vv9P7lUHQGEae5lCrhcHobpnvOcTU3NH5jiV62DFu0isN3k4ptGIhgYO96CCk3af0ni9spZU318sJUbOW-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مائوریتسیو ساری سرمربی‌فصل‌قبل‌ لاتزیو راهی آتالانتا شد. جنارو گتوزو سرمربی‌ سابق تیم‌ ملی ایتالیا با عقد قراردادی سرمربی تیم لاتزیو شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/22306" target="_blank">📅 17:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22305">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpH0gBHFVPp5fq63rd3WnEY3Rt8_ZDGNa0yIvW3ES8pYOiq1fOKdw7FcCv614n7aBxkXKCaB7qaPU63y7nLBQqttbV7BJF2IN4E-4yIGvVIUu-mFiRmo_1xuDjkNwdPow52c1z4nyZu0peakYzNv0oLiLMoUkBJjtYyl6rtkKn8sqyrS25QhqCVEfi7xdUTddNegadidGqGpfCL02Wjij-56Ys0XsPm78q2fz-gd3gdtUCoyDadV1UUTAjYsTTgdsIC0HCutjfxpmJUbBdPiatg66AR2l0saWsyAox0aywAldgjYE8hzcaFl-0L-LqYbQXr5IOkFo6FDgJQNZ2uwTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سردار آزمون ستاره سابق تیم ملی شب گذشته بین دوستان نزدیک خود: تا زمانی حکومت جمهوری اسلامی پا برجاباشد نه‌ برای این تیم بمیدان خواهم رفت و نه پام رو تو اون کشور خواهم گذاشت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/persiana_Soccer/22305" target="_blank">📅 17:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22304">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfEntJeXNQXaaxW3mtiATcfn9srjYwOAqy78gKCY7SkdFk7CInmg2qim2n0y3jUNb9wN-xWdahu9dwnVLibyzLEvWu241vLATs9I0KP-Iivn1RbZ1zgeCG746J-hORZqiPA7bvSr4d4ZRr_1Ax7hbpx2TwTqyUS5t0drf0DQpkuLTJ0xtJtOGefI0z4uhzi5EZKOKdnf_MYc7S-RHPL_0qJkpsg36m59wdA_9VfcrlA0k5IBT5eHnSig8sxHsZRRPe7mqYdhR5kQlLCYfGqihrRwGNZX7xlryMEXEUbVI0dGKu1iY8_M6G1INODXxicPwA67mVOxMVXttAfgeDYi9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... اوزجان بیزاتی مربی جدید استقلال و دستیار اول سهراب بختیاری‌زاده وارد ایران شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/22304" target="_blank">📅 16:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22303">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_M6BQcBKCu0fLxaVf3knEgXb4cYK1_ZsUdDgoCc9HvlfXWgx8Jv_C0Ckuu8BqffnrzlON8VD_Wd-4x4kEx_w_uMTdCvlNlqNj1G0hYd_Vo5MoYFoyZJ2WtMHb0bdmt35rMuB1jT9naTwqOkfroaDCrlI1C_cVtzHP3X7qEZyP8mO2vDGhof1KcCr2_S0T17wzruWR-h_yYiLcbZVp12yB70Fmww7MWfLIJLk_sd9BR9UhwzKysCZQdNC04mzaAO8Jh-2RoXnHx_x4xQifd4CBiFb5nuIssM0Nsj2yJPA1sbEp1IOHLcBsXT5flQ3lYdmkV44XMbCzFOdv8Atfg5UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باتاییدیه رئیس‌مجلس و رئیس جمهور؛ اینترنت بین الملل مردم ایران بعد از 80 روز تا پایان همین هفته رسما وصل خواهد شد و نت به روال قبل برمیگرده. ایشالا هرچی زودتر همه 70 80 هزار نفری که همشون‌جز خانواده‌واقعی‌خودم‌هستن آنلاین بشن اخبار نقل و انتقالاتی…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/persiana_Soccer/22303" target="_blank">📅 16:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22302">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O45iTuYnxfrhMfpWKGkLt-aixtCOCYUWclHS6rZA_ASePTuL2UXoD0woXE4AmEiy_6GdEgHTKWGu7hUzeB4ZIIbpss80t1gdz_ELVrfCLSRFxIeEjzXlEPKV2hz2FRH88Tb8wpooMKNsgDT83ytSt0nWw8c95CeM8NpL18iHKL1FPBTGclZFZFo3IaR8BXmQymYOyxJbNOEZRRkcxM96SFtCTR8BYJJyrNJ4TKTWzJ_rCjM6WgUniFfkudWgNxcLM25YMdalbCjSnjH_KIZAhFLS_jHUT5IaFURqCSuNuM98JWMZXlF_9BW3HYLPSQAhlAj1g6YpHOHOP62MDmxlcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌لیست‌نهایی‌تیم‌ملی‌فوتبال اسپانیا برای جام جهانی 2026؛ رئال مادرید بدون هیچ نماینده‌‌ای!!!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/22302" target="_blank">📅 15:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22301">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPfJz3IL47Vxsnb6P5Zwvtit9LzYfFJpDLLblN__ERCnt8JmirNYx3LSLmX9sy31RWw5udC2ct__stmKBvQJdYYAuXvOvu2PO9auQtHdj_4M_iTMeBirV5WIhvyMOUbLFLFwIPcrRMJngDn9hRuvIEWftzhrzuSj7NaNNptJQQG6Uw-EdwX2vpz66uHH-_ZVz4U9p3gBy9xT9PKonwg3ISVTQFB7IcuSugoSrQtjLrlO0goBXMn21b7LWaxb0ZY0z9oTVaCvVOczQ_VcsBZ6K8Hde6oVHT2cc0gZl-bM9n_UGfKuJ_Ipbgf0SA3ddJnu3bLg-GTzWr7zar-qmukIRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/persiana_Soccer/22301" target="_blank">📅 14:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22300">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gp_2sx5_cubhVxeakSUAATfhlDmS9-BuEip9G8b-EWxqnD4oCFz-sEy69Ilp1fYyMfFEJ92-GYri4wiixn7g5EuMp1j09utJKjrwVZ1uClpO1Xz-t7N2N36vBJ--8Nz46QgNn9WjZZwzjgE5qepdhohJvnhV9q9Ag5R-JbHC4xoFFS77wh2PSh7Ly0gQBmDb_w4mtEiSw_tagXGdCdfEnHZNfBfqXGx_0T-u0aQC7DTlc8BVSFRKdqPU5jl65jQ4m54nu_YfGu3fOPmpwipF8W-nUk04t5pMCzqZXNuXAMZ9S9q9Ib8MwGP5P1Zp1p79yZrzFEF5NqOZnyBGoq58ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/persiana_Soccer/22300" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22299">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKt4FrIa8gGEcrAsOwnMVnBtl-NMax7tbpvJMmZBVfKFa7P1zQ4u6XZO4b42i3usMdV4uf1UznySArOk-j4pqCZ-B8XBQ6DzSfRHYG2bf_b3v99zGoiS1szNWuPG0BJV7MAPPPy8mq2lD681KX5-kM0B30eFDC7JpRptb-cOCPCNwyGdzK31Guwd1eW3qdMIQ1HpL_mg9H2jjiNyt8Kx-YLkP04WjCNP-R9ejNotK1hL02ogdvXMpiGxg3sKXym05LMJn7vXZzMU0d9Dkntl-rzrdVcQ0ywYqV3t0mn5VdshPEME2lqVxVSf2rdrc3Q45y_poPraSfpKuTKdgqQLXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌لیست‌نهایی‌تیم‌ملی‌فوتبال اسپانیا برای جام جهانی 2026؛ رئال مادرید بدون هیچ نماینده‌‌ای!!!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/22299" target="_blank">📅 14:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22297">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vcl34pKmU3nkqOAZP2obeCg4U0FlgyRX1ktvMUzOtQpa9UJQYYW6y-2RY9L1QlxbCgmyYqvcqsWfWjN7mwUPtCSyPcDHszoXlh0Ndyxka8O3NJnWlSSO4n9jiWq5-Maj52t6245fsbFtL7Ip0lLFbJie4PQCF8Q6jcTlAuLQiHvrdxaSN8vQ8oq8FRV5DwMM8CYoVpVDTmOuKGW3DdYXCkwXeV6CPhmBMb6ihN-NwyNxk50YPk1M5HUfcOLu6dxnOd1GapKDybNkLRVt0PxVNfc_Kji2KDHR9hIL0KXNL2JDwF7d4V5OqmAm5HurdDfoSgmy8Xlh8l2_IrzCq7E1qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌سری‌آ ایتالیا در پایان رقابت های این فصل؛ افعی‌ها با اقتدار قهرمان شد. آث میلان آلگری سهمیه UCL رو هم از دست داد. کومو با فابرگاس اسپانیایی راهی لیگ قهرمانان اروپا 2027 شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/22297" target="_blank">📅 14:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22295">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOe0ApfQxcFbEOZCZwdcuF1-Rg7gR-Vtr5LCSuIg2mPtp--51W8i2TMv7J0Bb8xeA3SQGjFYf4w09VBxK_OjstiZ94fnvCKq9Ohh3S72DRALEafru9TS-90UcY4jE-Aleudxxiy_MWL0P474jIo3msS2qNx7Bz-jteRXr0N499cDdMDIB0dmGu52NCuOVv_AC5yuVLJka9hJQL1Qsk8Llqgidu5HSwSVVYTLIphyJO93QOErrXg5gQOE0CZjbP5iAvLAaWKUjiVmLtbj0ZovJJwV1E8_5YEOnAH01gmC7lbtJeUmkBeeRfBQRGtxCNykB2DHN2gF_zjI37yZgRV_zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رشیدی کوچی نماینده‌سابق‌مجلس نیز تایید کرد: اینترنت بین‌الملل‌مردم‌ایران این هفته به حالت قبل بر می‌گردد، یا ظرف 48 ساعت آینده یا تا پایان هفته!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/persiana_Soccer/22295" target="_blank">📅 13:06 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22294">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSFEBiLEdAojDzOnu1I8bHS8G3ETdqb9il94mHldgJW0xmalHkrOQPEgkuGEHjI5YbQuEuSxZrbRivGTV8ZXPxXi8mSeTFQqpl-KKpIdqseQYM71do595oDOLEWin6eoSpMAJAEOP77s-CsMAK7UJbDWMHZV3nug8rzPYZGHr6mtXgZ5MVQDh9H2pzh-QYe65vYpAIbzwcQmPiwvvgefpCev2CPGVdduKzR_aVoJkxRDS1Zy6Lcrv5E07xeRONIbOI4cMHKAA5WzKUVbvUnWNAzp7bANqdlEovOejPG4PhzssdHvagMW2Wir-SlvIiKeTd45Rpq0tm2W-oeTbEvJkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بعد از باشگاه استقلال؛ مجوز رسمی دو باشگاه تراکتور و پرسپولیس نیز صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/22294" target="_blank">📅 00:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22293">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juWWO548DofvUrGHBWzDaYVyvcrXBST2Ix3wZScSn-hekQZjrXfotvvtE0-mBfmkWCFC1ovoRZ_D0xgjsbsVCFav9RYjNrR9IOtGjD6lXhqIIANICawnWpirEQz1AHS5PGGnTiQqlskjF-QZQvei3WKB3N2wDB5zo1nb9_P2q7glVS-B6Et7CFM8KPBpvT-RU-l1Mg3XrJ2NryS6qD-wtDkuoC1CgNFCoudqayjokH1FUPtj_3h3bdB7SHDud1NS8f2Ew5zmMJi4W9XZvP_qTpCXE_Em8HsDoKYkHqAmMspj8fFp2yVA7gl29I51PPwRJkXmdWN7PtfZ7P-h1vyDOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بزرگ‌ ترین کشور های جهان براساس مساحت؛ روسیه با اختلاف در صدر، ایران در رتبه هفدهم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/22293" target="_blank">📅 00:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22292">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQQS64m8lEAH6RWlkoxPGpBSPFjoaQkAwtYi73ggSFf4c7ex_wiSJ-ypze5rvNTzjCLpMG6glZw1mWEOFc-sM7sEFOOAZg9T7WJYCuypAjROEnWr86J8kp3OrElcjFSwdLuCJba6l9tXN40rYL69MIGn92suiSAPcZ6Z5PPAdxsT6j_DV7ssFUl04oQDy0VFWYtP2hoz2MRaF7E4WohYdRl0oY4R6C7ajNCni48e1gdJbGZ0ZAVaOMBL-UUnUMjRIcxUUttdQVSSxtqyhWC3CjMaeSrPV_KZTbIqydDO-Sjd6XGCWJ4tA5MMUlDB3y2Ul6u_0JgAEQUIKUU8kT0DrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/22292" target="_blank">📅 00:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22291">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/db5-OV6GxQE74w3qt5FC2lZGncVZZmcc7cBywIElx6XJbgqwC0AHQT399fW4jekkj0b74t3iHBEpvLVnHeYZ9DFERhO0YZwmeGbmVV_PAiSKiDK10TktyimIIGIjRkdBGXcFmEuBlCSWRYe3Xds-NWxUp7HdGV9wASVX2dOEchRl8ICGj9xkWEVv8strPunHMFZ0w8yZQJb2v4wLEcJl3QuA_CME3MoNYe6VwvtB3nfXCpwQ-q60X9EOaQnnxs9POOX1GRC15hcYnxQ7oW4fHbLc2tigRmJ2xyvjHMsZOHGQKO5eX1-q90e2AQmQcgb_FN8Chok9HdYmkGruvC0lYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعدادی خبر نقل‌وانتقالاتی‌دستمون رسیده. انشالله نت همه وصل شه همه رو خواهیم گذاشت. باشگاه‌ها نقل و انتقالات خود را از اواسط خرداد آغاز خواهند کرد. همانطور که پیش تر گفتیم لیگ امسال ادامه نخواهد داشت و تیم‌ها آماده‌فصل‌جدیدرقابت‌ها خواهند شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/persiana_Soccer/22291" target="_blank">📅 00:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22290">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ar_x9aZLBJEgi9neG30ZiAXNUzK_JkUc5F7nvtQwOZHYaVlPWjslksUufCmmWYhfQiLJdo0qweM5l3N8R3VU9OeZKDdcswFNxif95CtBa4M77pWpFAEGYfRaN5PP_HjMDgvUcwzLsb4oD4M471wJRpvbQDIAG260TXJdkyBMYO0UgncuLvctfRNCM3NzU2gQIyaEkozHunOJv640YZHf7HEUA3Q7xvGQ7datdnvCApHrF8VNTxalxyqOwOD4vr8Rw544Td8iuPH_I0UJQ8S_5C4VD-GY9K9VOX_KGFRYOAhoAtawC74Rdfzi8xrY6JzFw9lxQvOaDumxRaEC3fnTgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|انزو فرناندز ستاره آرژانتینی باشگاه چلسی درپایان‌بازی امروز آبی‌ها با هواداران این تیم خداحافظی کرد و از جمع آبی ها جداشد. فرناندز از رئال مادرید و منچسترسیتی آفردریافت‌کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/persiana_Soccer/22290" target="_blank">📅 21:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22289">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGFyY27jL3e_N-g_lsYipcWmey5IzEdCQjzjWgsfLjdugKCWvGadEws4hUKTDwY_73hWPoOk_mD_uSIfGIAImZ4Jm0XUN_c46HKmYnywCeEDcdQ71jmqF5lCG6Mr8Bjgby3hahfdBEc1pOo6N9Ogtb6jUW179_8Bts-__2HjsKCUtIzu5Cxw_4yC2N6OL6Wt8bNWGtJ4WMguat5oDqdO-5cZhw8Pk88ki6O7aGSdt3UMXxcwNSDBG7j7TspX4hpv2396h63dqHrVxlT1m54P_r_BdM7pDbtwG9q_6E4jKTd7o_PeoL6TE5bQAbJtGYQ4HafUJ6vYvWioL5Qsqw-Tww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
باتوجه‌به‌توافق‌‌مدیران استقلال با ایجنت آنتونیو آدان برای‌فسخ‌قراردادش‌درنیم فصل؛ برای پر شدن 60 درصد بازی‌کردن او و سوخته نشدن سهمیه خارجی‌آبی‌ها به‌احتمال زیاد او درون‌دروازه استقلال مقابل فولاد قرارخواهدگرفت.البته‌اگه بازی لغو نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/22289" target="_blank">📅 21:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22288">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRHHGLWDerq-ALbdI4fughHssbDikmEJ2lQjQB70UwUTdgh8iFx4hS5OovyXZp1IzRDswEFyqp67G2BQyM5NU5CoV0sfPQSnN7BtgROkLnVPCGCO1k5eYjKAWZ9TLorTFj37uWfHJSeo5irrnuqb_i6MF-doEOM6Ko1EQk1BjODoWoODe7W7V_3cBRxQ73k0v1YlEucowkRU0SQvJdk7PQGAjhR4fgncVEMh6Ztx-pQUlWjyIfqObVkoj7Uu4GokxIukChkrSwxM98yfy3YTLauqYt5HbUqnlGq-O0wVn6GiouW9h6mp-GHEipeAh7a8012wi_YwRWE645SgGahZIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/persiana_Soccer/22288" target="_blank">📅 21:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22286">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PoE2dpGHP5_63II6yCrw7ngEvilXR6G4zKoAPkaImhaJUOGI2YWZvEn7CG_-olULjuWQrcGTVzBfuSvnK5tNG8yK1CYQzDC4T1IF60ldagtpzTyFkommleCClxGYBGQo-Z6hBNpqrdtIoQdTmTpflwF5MR3Xp1GnHEnIWNW0brMhvSDWqUSQ4v7tptBA_vK3JkHqVSAsbIryhCODcMdNT3V1aGO4l25TkTngGEOxtI_LPtJ2U-qByoYZnCx6l1FvXR_RtXQU9wiX5xYM9Sou-qPOHJptvNJJebOOsowB4nw9bYssg-mu0MoVM9cAj2zuD5ln8jftfmBqK3B-V3u3xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/22286" target="_blank">📅 21:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22284">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XnnvHDNsco5Grom-wC_ncoMunbJY5YnVuATFsqUuRfiN3axkQdYPt2Oc8kl3YQcreTlcJQRWy0_NHZhGROrWdxG6o5CGETi4A0iblssAmbRupo89KL3KRGuJefYVXMx3Z1PIdULp7r0_7jTJKg5Qn67DXjYfHQoeS4jez5sWd7He6I-qQVzVPtT6ItJiUAnpm3US-Pu3jqZnX6wXPKnyloli8QHjG0npuBC5UaGetS5wejzAKUsuMZ-yFXIhc9mW5c5FDPiJ7Cd5LB_-iQs_EM4lFC4xPV3psOhFF0dq6FV6mWKXe1NlSRJREXmokuobjtMxyEpz0tycUY2hKLL-NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eqlXYLLj-dRumGKXInhxE3Jsa4j6jO9zGVk7_ehYOfgZkQCKDjtBPMQrbrGFpteci-tKptbjTcq7RHaogZYY30ex8PFlCyGXEJGwsZLFgt4nF8R_sm3VipWOE-83gM0un-gs26yX54q8fI5o_Q_7S-_NpAIYi8BIOHDNJB5cFM1a_UeoaqdHRh5SiEdWPpiqR4b0oABRHsDWqazg9mufIe8wLkuS5bOjUJ87fJIbXtkRPSBt3ryNR7_PrelMfZxCljv2fDSArqKSXJlLKQ_BTHtQizgKrAianZmRlcU_fy39cXG6ozyRhtFopeUx9XKNaOVBp9y8oG4o9sY_LdkrNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/22284" target="_blank">📅 21:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22282">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u8OvL8g-A9_o7vqUukYc3JkGI8hM1MYjIBQqlaCIpSSeazwkJW0QEGdwPXvdKrgr2cRgSbCUHZnr6K8-6IEbZKzbq_5IaJCbWiOZwLyAQ1O4ee_qUNY1Q2IRKjDMwwrnmlSalLDpNquFC7sGn09djP9Oili8JrDTDiK5GTD0GY03vNLCoBn9OmiME-G11iDzthLB_O-1HeNaPmIs0voNuKc2eW6nnVPETLrzrB0lNbc_N_TKhJcjEXp8Vx02EZgaj6jE9Ron3OX2fA8tchxyW1z-BJA7tZylbCHtNSQlkN0q-qa1k3mLkDAle8iSwKaGi8F4Hx4_hsVa_KLDyMZywg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qTwrpkeNouisblAHqHw7h8YARjozK4vM8fp_FONC47_vmVER-z1T46VYegq2ZKKpabrNVcWnkZG5fzE4X8QYoglLdKOXT42WKjc30nmpX11fJifFsFattuIcOn13zoeHT4Jx-0xvL5mszrz2uoSxUl4Uy9WTQd3Day5Qvd2oWO9hgMfjY8-ARf75SmnOu2zxeFPsMktHdjmd8wrUXw5Dq_h2Sq33cVJx1ZGYwLUVJvEUiHQOiOjVA0IKCy0u39OeHrW3stpQUdtcWIuXdEYEpr3iJRXYB5G34JfuY86CJLfAeflmoapVAJWHtrORynCWnSaaiUllz4seQ1cUdPvCgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/22282" target="_blank">📅 20:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22281">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aL4cH_a41pKxGh2zRTgf8Ho_FJxLSKo9B5intJeyk14qjN_f2RQVoZb07N4L0iqT8TtWtMdj6qytCz8QVHzRXzjFBbWWhw8qAqg2_TCtdLxjq1Co_l6WETs-zvQPMV7WaFDDREO0I-Qy0U13ksQw-V7sy9jZiKUUTBAuVmpFzoSlDoQjFxKn3uanmLPpRl7BJJ4bSUXIkmtSzAOPmYrXxvvMaA1chEyDrIXYiB_5LjwUv4IQgkteiVq8GLr3RlEZ_CVReAy9Bc3M7U66gOn0xmyC1s9WZKDK23bNqt7eILlHcI40KAwOyIl0p2jQT-eC_ARhlfV55sUTWOXSQnvGbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌لالیگا درپایان رقابت‌های این فصل؛ خیرونا که همین‌چندفصل‌پیش‌سهمیه اروپایی گرفته بود به لالیگا دو سقوط‌کرد. بارسلونا هم‌که چند هفته پیش قهرمانی‌اش قطعی شده‌بود نتونست به رکورد تاریخی 100 امتیاز در یک فصل لالیگا برسه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/persiana_Soccer/22281" target="_blank">📅 20:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22280">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbfAac7p74AotgVjNXIZktdOL_UapXdQvsUvBa9_delSoD6j3HgV-5nVSfyNH-kaV4qvMxd0hkSjoMcZHEenP6xMSjl6EIoy8kmnWT7gE672v1f04_MfrbnTvya4BGM7Zt9FOCLHEKVXq9jLSlDGN1wXc08YtDWqDkzKsn4SwFpU7yf7ovTVVjjC6j6nuwK5PLuZOeogpecUMY-74d01IQYRxSNK5eHhqj3jxU8Jc2w1QPomnKjqGYerPhIHFlAnhCtWkHHtzZtU1APHees1B0JTIREFeMUiKDOkH_tX2bseRq6zlo1hqAcCZNB8biuxACJRlYu3PjIq238-7rKWJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ محمد امین حزباوی مدافع میانی 23 ساله باشگاه سپاهان قصد داره از این‌تیم جدا شه. حزباوی از باشگاه پرسپولیس آفر رسمی دریافت کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/persiana_Soccer/22280" target="_blank">📅 19:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22279">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8szoA0UEkQvNqQQs8k-GMOetBHHElRVz5SbN21g29ggWig_rlZYgujeUrqnXCvcLHnHMqaV67-V3KJWc1D3APDmfrXTxt5CCdbcO9nDGdEIUhsHEjh0Vaeoq4BjJg7ElUofypAOId24lmRnMKeYSPXOgvru5FgXMCBtY4PbltqNjWUTq3pRL6vjuGAEe5sYrPh0YgdHjJV2J542X0FoLMeFtj29uOS2luA2ilPTJTvuSeGpkMnMgD2x9f4T9QyvC_i10furs1kDEqGOipw-LGMNE9fDELheSIb_6yef_50tJ6ieZgl2cGEZ5hg6z1rLIpnnmV6qT9QdFFv348G6mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیتنا پایگاه‌تخصصی اخبار اینترنت: به احتمال زیاد تا هفته آینده اینترنت بین الملل متصل خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/persiana_Soccer/22279" target="_blank">📅 16:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22278">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGeTlEJie4cDSkCGXmvcW_dh4DBSuX668ZENFgyJlbWwgFy_iAkzCQgrcgMC3eb-TjQNyHGm5BLOU-M1mYuINwLpwkNP6Ty904uPlLYOnCGV-V3jGZRdFqI4IZYDwsDu4aAI8PzVdqgGzArBQfuMnBHJjAVj3wUbzuFimXzglF7RLFyxzBTOVTgaxs_MkrYEAtPtOj13KLqip6QETz1N-lUmhYA7vJR6GHQGLq276owsQfrVBv3D0frj1nT_89fw1_17U8CGBdY83cfx0-U8X97232h73BkrHigd6d9GgpkV7e5lGZT2wYNup0pKl-KhHaNCsScYUcaojWl3e7lbJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات
|ادرسون‌سیلوا هافبک 26 ساله برزیلی آتالانتا در آستانه عقد قرار داد چهار ساله با منچستر یونایتد برای جانشینی کاسمیرو قرار دارد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/persiana_Soccer/22278" target="_blank">📅 16:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22277">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmMO5S5kXm3oVS782SKJDQA2IXswdoZquolgx7UCyQH66vGY0tx0dq8ist57z3VhoyRGWcalsBF3gAbuUrahFjj_mtIL3ji5LX8Z6eNRiELE4ZTMv-N-2k-NLdKQtPuUkVNLm_eBX8JPWZu40AGMltZZOWr_uuYknRmK4o7hWrgQML9EvhvEM5P_BMMQ52pc4sRR8d0B4yylwL-s_XRALM7Q2Qa-GM1ZmRhBW52yvWL09ixrMk7nRMNCGt83D6yiJ-3V30LcA9FQ3iNu2Zn1fyb24oS64z5ZKwOAp8g1T2dByn38NAjifm5hZHfp0Ng6ZBRiLDKi57LWirdkWZc44w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
هری کین بازیکنی فراتر از یک مهاجم؛ توپ‌گیری، حمل توپ و دریبل، پاس به موقع به هم‌تیمی و گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/persiana_Soccer/22277" target="_blank">📅 15:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22276">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oePqCjtf4Fw5v5fALG3tlZAAKnncU08aZfNdcHgqu_Kv_hnw-jalSJBD6066QtS5RJpANGiWGpRx1sEGmN1_lbtABiomb1mKICzI9AJ-4QF4bl1ibKtFVuH_HKsKQUzn8Tcd3WliMEHlqkb8Rby2CccS0qReJk9yiiEFHceHFiYUxJ6WFjMX5S8lerbVHcsRWEwMmid1YwB_pq6Z2XOKHTObrUhCkPvMBtBikrKjICkK5nZQfvaoXsZQHlcJ_3W1Qn1tdyGJ83FZgWzKjt0_X6SCTuSSY-A9n7f8qNYNalPsYFoJakspXdS5hq1DBNBShVWgL3KwdFb9SDdzr6gS4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب منتخب فوق ستاره‌‌هایی که جام جهانی 2026 رو مفت و عین آب خوردن از دست دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/persiana_Soccer/22276" target="_blank">📅 15:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22274">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBgkuskBLEybrOmQI3RdqWqNdPrmH-gJWSnshaETt35vrNo5B7QeuBF3yxbX_N1mz40TOdgBt1oZYv4pO8hPC7-7l-QBcBApSIAy1XLa52qTmOTmTuQL91b7q4_9Aw87_763Guua9mqwK9axEI1eFxWZaBxhAqhCWgcfedv1CQMYE-PlaZV1mU93fovI5hesLdRc1EYG0FKVm6xiRl81Skqt4qOjJ3VcIve_cxpD0KsqG1GJ1-qIfpR9fN5ZZTfgOdGvfVfG6KMsFZ920o2gQ5OpKiY-fJ240kmACtTNEbJSwEil4MPRFi3AF2DH41PI7imgl_YmxfCtmcWRketVFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌گفته‌‌روزنامه‌های‌ حکومتی: اینترنت بین الملل مردم ایران تااواسط خردادماه حدود 15 خرداد وصل میشه‌. حدود 2 هزار ساعته که اینترنت مردم قطعه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/22274" target="_blank">📅 15:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22273">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfCBf4ajQpqPRjaCNycH_tzNbaAW9NzL5giytYnq6fHZyhChaX7MIlooAP48Er2Xc0nYetBHy7d2mwXg33DpRJ67d5bs6jrnMi3lfijfh4oHwlDBeFyLak9Zt--cUb3wSlW9pamqMOEqUxvk2hjHFk-zeq26M4rMnAc1y-ybjNfpeN4zB0u55NP0mlJ5GH8sVWk4cpFE18cEvdNqzERkF78cHD3xTvlJn0BhpANoFx5534CdzuK36d8ZZgjARmD96XX2Qafwi9nIJfHcJqqGvH6kvECfj2Y4Mfu35HP412tho2AGqqtevhCMpSMJhmJ9e6jnRi2GeenuqJML01L43g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/22273" target="_blank">📅 15:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22272">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZAUVsGawfmWY_5dsGO9QNYsIrgkJxpBjN314yxNY6nUz-0QlHamy8pyH-h2hhhf1JZuXrlVthrkzAX-y9xy9K-cCaV4P3aM0XuagA9T8kmnU0J8SARmzlEnCF_g7cr6uItvsGoFEDWgkyGguBAdc8piu6CojBuKDcoZBz1eqZW67p2845SM96eLlGdlh6vBjB9MxiWgkXJik8uPn36zJcZZ-zZ1F1LEZRA4sHjchqOAdezpFD3k-kH4Ec_UXShFhtmXCV0E9j9LX7PFyFP0A5il4hyzlCe9ZzDmVKAF7Lalb8nm5LmAjai4ZtMCEAiTR44UgQU8mZ4_A2hkzbqS6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
درحالیکه وب سایت ویکی پدیا از تیم های حاضر در لیگ نخبگان درفصل آینده رونمایی کرده و در بالای جدول هم اعلام‌کرده این جدول غیر رسمیه اما برخی به اشتباه اعلام کرده اند که AFC اسامی باشگاه‌ها را منتشر کرده و برمبنای آن اعلام کرده اند که نمایندگان ایران از سوی فدراسیون استقلال و تراکتور هستند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/persiana_Soccer/22272" target="_blank">📅 14:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22271">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb874305eb.mp4?token=vIYZZionfp8FUHetZese3VMq17mzh16_kxzJlrPk-h4DxJNb_MuGtS9N-RgPbil1sxvfVgcLo9XZggqmz332okQUo6pTF0YcGgBZXMvZmF3merUb_S-pVrXhoL7MtZ_qt1RyQiO4zuIiB1b-UJb9v1I_Xjb11Q9MlhTg-VFZN5YpR0XY0EWEpslT6tFmuqaBugEJx3IPc3vn6h9-ESmNzM6Vsuf2PNtjEL8xvhRBupR75KAacksnADA3VzE8eUUb0ua3waon8g73xdtWgQP9zbPu71VHA1SFmvfn6BCFLZGhMI4h453dE6FdJK3BN9rwYLQeNnf9CTSQq4ovKqGBgJc9b-aBsVbHaWxnR4lISf99SI-ecj06AWkQ3DaRqvhm39VMbLgfya5LT_MDy0dIf8m1mJQ4OpI6V9JIycPw8f5YEfTXU2CiYoC9vpVcHfu5SCz_E3nSHKMCMQeCoo6VRLqq-0T8gDDfSTY7ceUfB-SDSgFplaKl0QiIXLYSBWXvP8pehHea1EVRldf7bMOpLzu5dfAwJapZ5lsyPPkVeERgvUyqWA64-Do0rgKivg5j3NSaum9jwdkiCLLbvfaAvGsJLflz50jHTVAL4lWHT9V5-9urZ28GsXqwv8Aa6nfOlw9r9KNOzguoKpEIp33A73BQvLb2uacSNXU-hyT4jMM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb874305eb.mp4?token=vIYZZionfp8FUHetZese3VMq17mzh16_kxzJlrPk-h4DxJNb_MuGtS9N-RgPbil1sxvfVgcLo9XZggqmz332okQUo6pTF0YcGgBZXMvZmF3merUb_S-pVrXhoL7MtZ_qt1RyQiO4zuIiB1b-UJb9v1I_Xjb11Q9MlhTg-VFZN5YpR0XY0EWEpslT6tFmuqaBugEJx3IPc3vn6h9-ESmNzM6Vsuf2PNtjEL8xvhRBupR75KAacksnADA3VzE8eUUb0ua3waon8g73xdtWgQP9zbPu71VHA1SFmvfn6BCFLZGhMI4h453dE6FdJK3BN9rwYLQeNnf9CTSQq4ovKqGBgJc9b-aBsVbHaWxnR4lISf99SI-ecj06AWkQ3DaRqvhm39VMbLgfya5LT_MDy0dIf8m1mJQ4OpI6V9JIycPw8f5YEfTXU2CiYoC9vpVcHfu5SCz_E3nSHKMCMQeCoo6VRLqq-0T8gDDfSTY7ceUfB-SDSgFplaKl0QiIXLYSBWXvP8pehHea1EVRldf7bMOpLzu5dfAwJapZ5lsyPPkVeERgvUyqWA64-Do0rgKivg5j3NSaum9jwdkiCLLbvfaAvGsJLflz50jHTVAL4lWHT9V5-9urZ28GsXqwv8Aa6nfOlw9r9KNOzguoKpEIp33A73BQvLb2uacSNXU-hyT4jMM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوخی‌جالب‌روبرتو پیاتزا ایتالیایی با عرشیا به‌ نژاد: من 58 ساله‌هستم‌اما چربی‌خیلی‌کمتری از تو دارم!
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/22271" target="_blank">📅 12:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22270">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmXp_GnGTRSMFgVMWAY13j4jBB_9vRfuaTUv6RWgYPe8B4V0-FiuWbJz7IkWXTQYNspJ1PYTdwr23jZsfx0dNK6jmlxPkFq8hVg9qhpsQJVBw0lRZajie_a43QBRBo_n4SZSBEqGtlY0SWZLJSBOwooe3Y8631vnUjbexJgF5lWBnc3a9b0PNTzPn06_0g5U6yJEeb8X2pafUK_CZBv2tQuD7wuo_03CuCyrkElnLH8wP-iGEs2BAkSsndGGrcy6sjoiKYK-n72dmN8CWGOU17P61h6ryFbzpCn32T-4aZVOPfYF40Ackcxua5gFARmGgVXGT5UPVQax2ckKWrLlWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دنی کارواخال کاپیتان 34 ساله تیم رئال مادرید امشب آخرین بازی خود را برای کهکشانی‌ها انجام خواهد داد و رسما از این تیم جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/22270" target="_blank">📅 12:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22269">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=XrzgM_v5jrDJJWYX2P46LE2vO2vKCb3BH4ajrD7PcFcQVqERTyJYvLcVcXyKykxaZWHTcPbjJqrbXti706-NMrbb4ez8h30t5A0Utiw28vq4wNffI1J0PBPfOvbuxfRw2A0gIJSywcH7vSxUkfEPhp5q8qjLMcBl5XUO6ibYiRyvApdmCd5vmZdWx_hBSMmz0At5x9GAUxNhDBOiQuSU1gUYx9xrbAb2T7iSBxij9OTXuS7C30eENrQXl0goi_7aK5kSwDX2-UY247bMyvV5AWv3zYFk_nI6Xza6p07G9j1-tI45bwbqS9HSpSopyEYQ4yJnh1TlgZevsnQgnwHK4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=XrzgM_v5jrDJJWYX2P46LE2vO2vKCb3BH4ajrD7PcFcQVqERTyJYvLcVcXyKykxaZWHTcPbjJqrbXti706-NMrbb4ez8h30t5A0Utiw28vq4wNffI1J0PBPfOvbuxfRw2A0gIJSywcH7vSxUkfEPhp5q8qjLMcBl5XUO6ibYiRyvApdmCd5vmZdWx_hBSMmz0At5x9GAUxNhDBOiQuSU1gUYx9xrbAb2T7iSBxij9OTXuS7C30eENrQXl0goi_7aK5kSwDX2-UY247bMyvV5AWv3zYFk_nI6Xza6p07G9j1-tI45bwbqS9HSpSopyEYQ4yJnh1TlgZevsnQgnwHK4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
روایت همسر ناصر حجازی از پادرمیانی برای برگشت فرهاد مجیدی به تمرینات تیم استقلال بدلیل تاخیر در حضور در تمرین بخاطر تفریح با دوست‌دخترش
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/22269" target="_blank">📅 11:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22268">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7265d2cc05.mp4?token=PeeMqGk0hR9nyniq1t5o5EtLPKVcbAYtR33ZjujhTj30-5fH_qrPj2gxDqbAr0sC6XyShzmsTuVba1D-5rH0o89xQoyeYsSFlEbfmDoUt-pVjhv-IcbUs6sF_DwJ_FXx5zSyldRQ5oyEnTrHNcUn6bsikfP-snG7lgSuLBPmU3wgY7K7sb5kdGLN18WQZsQQT9kIFmV3RPe9xOStLe7pWizZOXO4FrDCAdj9Ye2Lw3N-pK8gQ23GWCZxqatPZd3nAl82UjpSjnZgWF6vbGIacR2t3_HnW4K3m-PDs5awUNZfPgKmgR6RwYmcXYKf7NO7UPcOkhwwv9SILzT1hiqQSafIRVGEyvHTTek9n1LI-1hBu8vtQPS6Z5Hqc1LQqgAQtBU-HpXTUwuLJHTkxEhlK_r4PbFjo2K6pDJL1Z9XfaZbBherBFaXdB-3OspXZPkP6VP3tF9-6y0JOvIyNTTriWixflDgJ-j5pi9GnoVSAUSbMR567tWgOBL1p9mrk9rlp7qb9G8ruAwCf2mC_VnQ1WTnaT94ewbWihsB4dhRqRQZt47IGk07umaeGycoy6rIaVtcbFXB_aNZK5XbqaMv_UReEYuXj9HkB3eeaZzXcEA_64p_-rgFIVCqpGR-NyVnVNSPO9yphhXN6HFcikNMjh8kkSPYbqFVLlRqrjD632w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7265d2cc05.mp4?token=PeeMqGk0hR9nyniq1t5o5EtLPKVcbAYtR33ZjujhTj30-5fH_qrPj2gxDqbAr0sC6XyShzmsTuVba1D-5rH0o89xQoyeYsSFlEbfmDoUt-pVjhv-IcbUs6sF_DwJ_FXx5zSyldRQ5oyEnTrHNcUn6bsikfP-snG7lgSuLBPmU3wgY7K7sb5kdGLN18WQZsQQT9kIFmV3RPe9xOStLe7pWizZOXO4FrDCAdj9Ye2Lw3N-pK8gQ23GWCZxqatPZd3nAl82UjpSjnZgWF6vbGIacR2t3_HnW4K3m-PDs5awUNZfPgKmgR6RwYmcXYKf7NO7UPcOkhwwv9SILzT1hiqQSafIRVGEyvHTTek9n1LI-1hBu8vtQPS6Z5Hqc1LQqgAQtBU-HpXTUwuLJHTkxEhlK_r4PbFjo2K6pDJL1Z9XfaZbBherBFaXdB-3OspXZPkP6VP3tF9-6y0JOvIyNTTriWixflDgJ-j5pi9GnoVSAUSbMR567tWgOBL1p9mrk9rlp7qb9G8ruAwCf2mC_VnQ1WTnaT94ewbWihsB4dhRqRQZt47IGk07umaeGycoy6rIaVtcbFXB_aNZK5XbqaMv_UReEYuXj9HkB3eeaZzXcEA_64p_-rgFIVCqpGR-NyVnVNSPO9yphhXN6HFcikNMjh8kkSPYbqFVLlRqrjD632w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌از تکنیک‌ ناب‌ودیدنی نیمار جونیور فوق ستاره برزیلی‌تاریخ‌فوتبال در دوران حضور در PSG
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/persiana_Soccer/22268" target="_blank">📅 19:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22267">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrxKz5i311kxXpu9EfhtGe8niB0fJfqgck3F3gQfadYy_GZYNeBwll--F5K1S9lBWRa772kKi1bfCZYp6C6sWtFIpBMjdLGEWg_zDBREszKadY7Qv2LgtZERiORNKCiKEmv9S9XBiqEAD5SGFUsL7viG_0pfvlMuLZNZFj1Seq6D3CccQYE7PNFBULQrGg5hu1u98NWBvH7GcQIgsas8SZRqR-CL0iYp42zeYDaVLPLtcOZ9XjzHhQjry7spAVFiawWl-UIJcTdC4LNz977SunphKuGxaDy5mXpZ9b72WlGxcxUODKI64a3VWul0G2o1kBLWmkp2Y6C6DLEUVQdIzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعدادی خبر نقل‌وانتقالاتی‌دستمون رسیده. انشالله نت همه وصل شه همه رو خواهیم گذاشت. باشگاه‌ها نقل و انتقالات خود را از اواسط خرداد آغاز خواهند کرد. همانطور که پیش تر گفتیم لیگ امسال ادامه نخواهد داشت و تیم‌ها آماده‌فصل‌جدیدرقابت‌ها خواهند شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/persiana_Soccer/22267" target="_blank">📅 19:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22266">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8yWtxamtt_lKSDIo9Mr7dfrks9m1MiziPoJSp3g8inpZoSKB8rWmK7A3bTlklQ5LbXfjHwiKyvmniUNadQSy2QZgHI1LXNeT4cMBvS4qRVHqTgtU973tPHLE9KMlxPMelv2JRT5E0HSgqrSN_O5VcniuWN7NiE7rGpB7532gQEDvPUEf5MhV1Z50bzPvpo90Y2uRTLDHGbz1TceArMaQTJG_MwrUt0ym4a2YSB9OVi_dPOsWSldn-77--52hlQBa_MaZmLR-jnJqymN6PCnzeyr27nxXNaBAwz77k_f7xwkMhSWTbD0-Pm_0zXUgrTpphby1fsl9YvPR3TWOpQG0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/22266" target="_blank">📅 19:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22265">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEIUoQGbwGYhS9wDIUH8PbInDrJyfy1aBz-SHFYN2M7HjcaB2yYfa4ZD3Ldes4l_2tIiYgezSKMnnXrJBU7CBsY6U08LtuuPeVUGVmkVY_fBhxpFz5Jd3mQPVybaDhBhQz6ExOB0O7RdhDti-qv9bGvdepYzXH_-_UJWPJy6Iv68o3IUTm5LhJKtjktqW7KsPbRTo5KdGGuMBhNVycxACExnSquNoaQpYo7t0_OTJ_7ntdEhTGRvsA9-OeYN0QOAlJ_a6K27Eg4nl0zPk01ma49XnUyOm_8px4N89svy2v5bNeMJjEjeFH2Xb5c6MmKB8sCq2myk8UL8N9NQtj9R8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسمی: پایان راه آلابا در مادرید؛ با اعلام رئال مادرید، داوید آلابا، پس‌از پنج فصل، مادرید را ترک خواهد کرد و در تابستان، بازیکن آزاد خواهد بود.
‼️
داوید آلابای ۳۳ ساله، ۱۳۱ بار برای رئال به میدان رفت، ۵ گل و ۹ پاس‌گل ثبت کرد و ۲ بار فاتح لالیگا، لیگ قهرمانان…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/persiana_Soccer/22265" target="_blank">📅 19:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22263">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFz-7U2_7xjEJb1HmRcxMbM3Ie3rUsf7sSSZaOgi_gtVmFZKI_xDDZq6kTJFdb0hwNfnS3xrpbOojXfU13WX0jtQjUBxIhtTWc8aG1-uyjFX8UfYEiVLZyMDBN6SmGOGyBLUxFXGWBBwDY49Jo7PII1noKvSK8dEeQwcYKQChqn0fNV35DqG-SqMHkWHUZOemjG-eagDTz-j6NfNJ29_S7lZBuuU5iR0hiU-KbWQgr9Yswxx_WM2w-di9w7nP5e2cCKoR1NBkDaZP1QEvxrMw7mo87TbYXuqYBxC536uYtwb3r-SloTX7hVQjd7rnEuU2FGCAW4_KYrQoutNMwgw0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/22263" target="_blank">📅 19:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22262">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNQEJXUcwpHxawpUa3VFFhZ5a8qqWACutrHJh7zFrjv2Ovypaejvm4gC2jSBRkqvENxAfkAUK-5m21C1k137ZJuY1zozdQQmHTp3e87MMySmqe95Q6YqKFihRjI2yucmEVl5ewigNSpW2toqgK6NcYnV8jZghKlsg7-f2w3gsrgcK2gMterSJljgS_Bqv5CFj2yTfJfekhRZDBQmt6FyWS0a_E7tni49OjEQ1JItB9x0P40vPBPDWZdV8dC-w6JesLNIRZJ4J6AAtVRwJL1g6uJbBHHSVQcZMtUoCznLuF9mA3fnbU1MhmwGxg5dcXREnztF7EeEeJo8TZ_8A9XpWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌کامل‌مرحله گروهی رقابت‌های جام جهانی 2026 در یک قاب ؛ جام جهانی 2026 از تاریخ 21 خرداد ماه تا 28 تیرباحضور 48 تیم به میزبانی سه کشور آمریکا، کانادا و مکزیک برگزار خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/persiana_Soccer/22262" target="_blank">📅 18:57 · 02 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

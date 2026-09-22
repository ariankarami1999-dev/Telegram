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
<img src="https://cdn4.telesco.pe/file/pCk9_c_qhult3DUj9RBj2Xzs3hwBSwngvklLjKDB71KNhdH2qW1AvEXPih4h_k9Zso0vyj75CB6toKmqFcD63cuqcKoC0YAIO0hWTO1K6PuHnIR5oYtjOprRbg6CK1-OLdnD__dARESixlNWr5XFyB-eIzjs-VctMl3E0nohqX57le2pALfM4KAQMtfLzhxWVKrTyVlUoNrjBfj09esFWulovy4MOrFuyUgHJ0xUGhOkQQ8cZAUow_thLzXJAgOMgl8e5naPGBtHXSdidUvfnk5ZsG17xAJKc4kP_JVmTXL-2E8hpPQM-IZj_Shq4D4AMuF9QPSwNeHElGtrBSXmsg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 464K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 13:38:24</div>
<hr>

<div class="tg-post" id="msg-30232">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8babc4d6af.mp4?token=WI-Tg-y30GNB2kyB3PPaunAgiAK-G6Xq2M9zGRWeUoywHEQbInVNFsgDIJUhuY_WKosXG3BL8pt1VbInWGfhEduNTOUOBOvq7J8Qwx2bB3JYb1R-iBYlTe-m8Uq6BI4lrLarAyuqbOwu-3wTqW11-twc_Rh5VE5pK1wEH3v9XJetk-r1oYeS8zUZVpR2YloeVHkOzrJA-sS1u6kV_Q69icK61Jm5uv5RMfZu79uJnJgEERD5TY47VN1PbxEP0WtxN5Fu8aPKzIP1FSi4L4GU3Zdi-sEkVZJ8QQKxoMDd4fVzt5RvPF8yDafdo-1Z-pUzOLd5-xAhOs09ml0aLx8HO4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8babc4d6af.mp4?token=WI-Tg-y30GNB2kyB3PPaunAgiAK-G6Xq2M9zGRWeUoywHEQbInVNFsgDIJUhuY_WKosXG3BL8pt1VbInWGfhEduNTOUOBOvq7J8Qwx2bB3JYb1R-iBYlTe-m8Uq6BI4lrLarAyuqbOwu-3wTqW11-twc_Rh5VE5pK1wEH3v9XJetk-r1oYeS8zUZVpR2YloeVHkOzrJA-sS1u6kV_Q69icK61Jm5uv5RMfZu79uJnJgEERD5TY47VN1PbxEP0WtxN5Fu8aPKzIP1FSi4L4GU3Zdi-sEkVZJ8QQKxoMDd4fVzt5RvPF8yDafdo-1Z-pUzOLd5-xAhOs09ml0aLx8HO4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی‌خاطره‌انگیز و تماشایی‌از سوپر سیوهای تماشایی و خیره کننده دروازه‌بان در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 607 · <a href="https://t.me/persiana_Soccer/30232" target="_blank">📅 13:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30231">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hc4EfyrX7uBga12yzXHUs8WkM9SIRIu29_sLxvpz1jK7thUlwXk4TynWemRbEG9hVjeLn00ZZV3tEuH66kuJwvmpo1Y-TJVrfswN7-aT5FhGgQ14MQdrxLmLwXdA6m1UDgI6UmIWCs6V-7FTp6DDRcOvMN_UWG1whZT-a6MmwN-eZ9Bp_r6u5WO8ZTMgBUwMkjjkhN-RLH0xKdENyFaKQiRyHXRJTfWg7bz75_NJR9g4FqCIqlL8ryQ8Sz3zpTrD7RmCA5WOHzG9Wj3dw8dI5za1f6eaJ7Qm_hqgIUsJFlhPNQXgVO5UdtfWIAlqvthFNUnVpejm-yh2-wxEg_F-0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
منصور عظیمی معاون ورزشی باشگاه تراکتور که ارتباط خوبی باستاره‌های‌ایرانی و خارجی داره بعد از اختلاف بامالک‌تراکتور از این باشگاه جداشد. در طول سه سال‌اخیر عظیمی‌مسئول‌مذاکره با بازیکنان بود و مذاکرات حرفه‌ای او باعث شد که تراکتور ستاره های زیادی در طی این چند فصل جذب کنه. هر باشگاهی عظیمی رواستخدام‌کنه از همین حالا نقل و انتقالات نیم فصل اول رقابت‌های لیگ برتر رو برده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/30231" target="_blank">📅 12:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30230">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkXV051yzgHAAJR83YcehotCKkWVRSZJPoTF5VMXm-Wh44DqqWpkrUvi_M9uAs2cLXCu7bFMcyhpmGgZEppVfKzOV4Iosf3-bCUPV7ib7-d0TjYjeCf746tD2trIXPmeEejHSrk30K--CAsVboacgWO0-CsgFp0CEIo3mIehonlxwgaCMPqCjAE2rlhEHJejCczCnowm7fFmQnbZEUv-f0nAXXjjo22X1T5fx_EoIBQLgFa19WntiDsaPZLiyKh9D_Va2AMeMsIP6HuSLKG9RYz8vvcTO3IKjvLNo8DF-ubaj8mxb5IjmDI010ZYr0l4_60mSPOAngWKHVFgj3wblw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سعید الهویی مربی‌تیم‌ملی: با اللهیار صیادمنش در ارتباط بودیم و قصد داشتیم در این فیفادی او رو به تیم ملی دعوت کنیم اما مخالفت‌هایی شد. منظور الهویی احتمالا اون تتوی شیر و خورشید اللهیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/persiana_Soccer/30230" target="_blank">📅 12:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30229">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‼️
ویدیوکامل‌قسمت‌اول‌برنامه‌جدید و فان ابوطالب حسینی برای‌حواشی‌فصل جدید رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/persiana_Soccer/30229" target="_blank">📅 12:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30228">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال: توپ‌طلافوتبال به بهترین بازیکن دنیا داده میشه نه‌اینکه‌بدن به بازیکنی که فقط 80 گل‌ زده چون که برای‌گلزنی جایزه آقای گلی رو میدن. اینا خیلی‌ متفاوته! بهترین بازیکن جهان کسی هستش که وقتی به عنوان گزارشگر یا تماشاگر بازی رو بخاطرش میبینی لذت‌میبری…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/persiana_Soccer/30228" target="_blank">📅 11:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30227">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgzRiAsNDcNwDvjAG39xsdq6gYxz6Fe45ONkU-C9MFFJVn2l1-f_4JgBj130OLGOcm3UIdxULqXZYHfuctG7aRJ1IkRrBaOyNjENN4uf52ur2Vwx__R0xQHRDT29R8fwl8P5S3CgdkGCqrcWozIURCa4R4Pl0jzC8JZl8NbU3lOmzyQAzPKNOHmssFxqoWZDiO6jWeqaT3ZLQEg5SqZ6_QVhL0d68F0q4_Eb03V2OKmDdsYWKMe9RswOb52uq_KNAXKQr9PcGo_NAJ2ghFrlOLDBKHPBlBLlR33VC6VvUVExRbCV2zMqqBscoMOtBP354a2HcQT6ALqS7APUrHSn-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
مسی درتعقیب‌رکوردی تاریخی؛ لیونل مسی حالا تعدادگل‌هایش‌از روی‌ضربات ایستگاهی را به ۷۵ گل رسانده و تنها ۳ گل با مارسلینیو کاریوکا، برترین گلزن تاریخ فوتبال از روی ضربه آزاد، فاصله دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/persiana_Soccer/30227" target="_blank">📅 11:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30226">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇫🇷
ویدیویی از اولین تمرین تیم ملی فرانسه بعد از جام جهانی 2026 تحت هدایت زین الدیت زیدان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/persiana_Soccer/30226" target="_blank">📅 11:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30225">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46dfa14d7e.mp4?token=FubKMF8oYkQw0ELXK_Gs3O7Jjw_yoBGpjUQS8nHJMbCGMxFNc-UDDGo4pg1pSLegfWdkCxN6VXogZHf0jD-J7eYYSNsk5wrModtorbvgj3F9dgycZwwJntOfXHmfw8Gg2kNkFOtXQYRNAoU_gJbtv4YsfdgahxQitG0JQW6ysRAH1c3aRlWF2HnqvDYoPMeFOvOCpBwAhsr2Wy6oq8OtmwBroITkxhl52ZjtpuHjol_ulEagwHqelWVgZX41DND4D4Tcd5pXAmnxayCgelW4TiqkcHSMD688sgr6FamlKehFg5uddq9tOE6pOe2fhYdcB98R25SM-jRoCXHcYn7zSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46dfa14d7e.mp4?token=FubKMF8oYkQw0ELXK_Gs3O7Jjw_yoBGpjUQS8nHJMbCGMxFNc-UDDGo4pg1pSLegfWdkCxN6VXogZHf0jD-J7eYYSNsk5wrModtorbvgj3F9dgycZwwJntOfXHmfw8Gg2kNkFOtXQYRNAoU_gJbtv4YsfdgahxQitG0JQW6ysRAH1c3aRlWF2HnqvDYoPMeFOvOCpBwAhsr2Wy6oq8OtmwBroITkxhl52ZjtpuHjol_ulEagwHqelWVgZX41DND4D4Tcd5pXAmnxayCgelW4TiqkcHSMD688sgr6FamlKehFg5uddq9tOE6pOe2fhYdcB98R25SM-jRoCXHcYn7zSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پارادوکس‌شبانه‌ابوالفضل‌جلالی‌روی آنتن زنده:
من هیییچ جایی نگفتم که از بچگی استقلالی بودم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/persiana_Soccer/30225" target="_blank">📅 11:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30224">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGQFLLvF5Tfh9Mq0rTXijX8vdCG49pOwIvjA3AZxgpoMkl8GdLD9HD1BqVy8XK0H5iwTNUiD7bG63x0rH0GBiEQCV2n9CzQyuXtfxIV0Q5kWlJ8WgPapv68_YfBb6f6ZHnfOMpg8prXMQMcIDi38H60v3kYTqa9QleLcCGk8KUT-SghzQiGm2ziKlJ5H98EYP00x_y-pGay9tfltkcA1RVruebdedZ5HIjJrYUAZl_nol0q7sgTs0BTBxafh0GUew6BYv-Tsofg_z3cDupWgMv2BD_-tDZFkhbW-UrfpNItboznDSbRia7VzDS35X-SkPshZRdGgagi0ocZ7wb0DIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
💥
جمعه‌های انفجاری در یک بت
💥
🔄
🤩
🤩
🤩
بانس کازینو مخصوص بازی‌های انفجاری در یک بت
💬
پشتیبانی آنلاین 24 ساعته
🔈
کاربران میتوانند در روز جمعه پس از هر بار شارژ حساب کاربری خود از پشتیبانی بانس
🤩
🤩
🤩
کازینو را تا سقف 30.000.000 ریال دریافت نمایند
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
r31
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/30224" target="_blank">📅 11:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30223">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/619db5893c.mp4?token=dZIKLOJRVTZGkLvqdPeDGhq-261JP10tAUXiZ5BmCCYZvflRP5jRKBJ-XMs8LyA8EpH51oCmGl5oexXkDw3ImRNRQ00uELyD8JIuhJQmBaMmjY9u3vaxjlbAlis0vjpBZFOq6dcTkxDLD9MU7zgCCQVVQBmEbxFj6eiu1xY0HfUMAbcLldHjb3UmN3h4A_7Aly1bvhulgRf0I3Nr-3CuN0HcQysIJKgspWZdLaQd_u77eSRJ2G2Mgp4AKOaxgDDO0GvU1iJRiGQKysbe-WKkrgQq5BbeYLIbhroeIKdmaXa6AUwCJyaNQ-q2Md1NSItjF5ayqI1_uvBI3HpHclAEpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/619db5893c.mp4?token=dZIKLOJRVTZGkLvqdPeDGhq-261JP10tAUXiZ5BmCCYZvflRP5jRKBJ-XMs8LyA8EpH51oCmGl5oexXkDw3ImRNRQ00uELyD8JIuhJQmBaMmjY9u3vaxjlbAlis0vjpBZFOq6dcTkxDLD9MU7zgCCQVVQBmEbxFj6eiu1xY0HfUMAbcLldHjb3UmN3h4A_7Aly1bvhulgRf0I3Nr-3CuN0HcQysIJKgspWZdLaQd_u77eSRJ2G2Mgp4AKOaxgDDO0GvU1iJRiGQKysbe-WKkrgQq5BbeYLIbhroeIKdmaXa6AUwCJyaNQ-q2Md1NSItjF5ayqI1_uvBI3HpHclAEpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد ضیا مجری‌سابق‌صداوسیما که بعدِ اتفاقات 1401 از این سازمان اومد بیرون درباره خداداد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/30223" target="_blank">📅 10:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30222">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4c1024d94.mp4?token=vgnq1FiGXCvIpVmQA9dp9R9LYQikjFk5nFomwnL2mSG442v0d_reqk6qG9Yxj7GWw84pFpMLMevw33oMkV5PV3u8INXPfbPNaQ8c-XPXYL-MwZRp-xj60xhOu_PXeOgLRsqA_kAt2si8y7vDQFNdlN2R7wXakHsLb1ws9ojXqycQE7slPkgnhzi0hdtI-j-BtCmNqtrsxeHNW_hKThzGO2VpOA96APXqP39TZXimSAe8_3NZPIbrNULXdLDSrKUcjiRyO2OOuU8UilwsFiQ_YGwtHv1sXUVY5Y_KxlceAjmwHICMc6DCVGr7a0KobYcJiw7vle-uWrlM-guc6JxWcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4c1024d94.mp4?token=vgnq1FiGXCvIpVmQA9dp9R9LYQikjFk5nFomwnL2mSG442v0d_reqk6qG9Yxj7GWw84pFpMLMevw33oMkV5PV3u8INXPfbPNaQ8c-XPXYL-MwZRp-xj60xhOu_PXeOgLRsqA_kAt2si8y7vDQFNdlN2R7wXakHsLb1ws9ojXqycQE7slPkgnhzi0hdtI-j-BtCmNqtrsxeHNW_hKThzGO2VpOA96APXqP39TZXimSAe8_3NZPIbrNULXdLDSrKUcjiRyO2OOuU8UilwsFiQ_YGwtHv1sXUVY5Y_KxlceAjmwHICMc6DCVGr7a0KobYcJiw7vle-uWrlM-guc6JxWcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیس‌سنگین‌ابوطالب به خدادادعزیزی در قسمت اول برنامه جدیدش: قلب آدم صاف باشه نه پاهاش، شما قلبت پرانتزیه آقای خداداد عزیزی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/30222" target="_blank">📅 10:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30221">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyolV2tO0SG37ARp0g_I2BmmNtP1_K6n9zr8nkVkwrN85Bk2urzSluu84sxPNZkJWiYbOgjxfpPY25RRO5s1ZV0ojEOOliGJmtwoP4ltLCUjlXKkVAVIx3nCJ5_2BN1TsP0ugdtyHntOXvi4Zz4Ahu8TVq1HjQEDniCpL-muVOlzFS3Ay1ZSQYZJVxyVKoIlj2xkck8U39xRp0rUW22r0XtXq9Llxvwzkpl6LhZQzpSB4r3-wnF5hggkUcqDlr6LiUWmi_RDyDLUI_pC80wyaj_GPA3qgSfRnlhT5DG4BfeoLqOYpzuZbINMlUwzRPu6TkGJPEi7we1GMzEjfIyl2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویری از علیرضا بیرانوند در روزهای آینده در سالن تتو کارها. این‌بشر شده کل بدنش رو تتو میکنه مثل بدن امیر تتلو تا بالاخره معافیت رو بگیره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/30221" target="_blank">📅 09:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30220">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0ywFHAwxftJZsYQ88xzEJ9RLRLNHkf7EJKZCqfah8DFzWs_pNDxm2gTrzasvw1sBi8qCH4YpYETFpxPSScHXMuKsume_uSDPMNpKxuDRBKZ1V2gDYCCj4KU7kHoyDjo599XtNIrF6RKG31aw9CFOuFOLzfx_LFZu4Nyl9ZkdH3clml81X_Zkonvyfb3wEXRQ9VqrmHcjMGyxMj53S77x6bug_HWtm1mhaUIseMgzjYk8CdjhIKc8sCJRNXI54BYldU4PknQzmSNDKfkCMjbmIBb1kK25MFCKwdNEQp72UwI6M5kXQwDpfE9HTdZ9EaftNZP6viTphT4W8jK-o2miw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
استوری مدیربرنامه‌های یاسر آسانی در تایید خبر ظهرامروزپرشیانا: همیشه به‌آبی وفادار خواهیم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/30220" target="_blank">📅 09:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30219">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67b45eb828.mp4?token=Y-78dDlxl_FQ0aiDtMg4qlY4a1gj19Zf6mL4sOWMnVD4pZ2qFOR3goy8222sJFx6-a4Ydw5oIE7bsKsnfmggte3q88p7W-cg6c3QZICXdkfstEtxYmngNNZR7r19t0NzFg4DSD4pcFNIi2MKig6VGKbF_3LPxsdJZChKP4BGVyaWdWeKvglvCnlYiCpIY8UmPtaPy3OW8e7BjG2eihSaseBB0fCINEFhW-OQF92KguxlyP17_DKOiR1--08NJthQrULhW4GVFT-q4jCBJ3zzAZGAbyiCR7FVoQckzWZOYqv8wvyJbJoUM7SdpA6mEXMbeAeDLOCyk48WtP7xRncmlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67b45eb828.mp4?token=Y-78dDlxl_FQ0aiDtMg4qlY4a1gj19Zf6mL4sOWMnVD4pZ2qFOR3goy8222sJFx6-a4Ydw5oIE7bsKsnfmggte3q88p7W-cg6c3QZICXdkfstEtxYmngNNZR7r19t0NzFg4DSD4pcFNIi2MKig6VGKbF_3LPxsdJZChKP4BGVyaWdWeKvglvCnlYiCpIY8UmPtaPy3OW8e7BjG2eihSaseBB0fCINEFhW-OQF92KguxlyP17_DKOiR1--08NJthQrULhW4GVFT-q4jCBJ3zzAZGAbyiCR7FVoQckzWZOYqv8wvyJbJoUM7SdpA6mEXMbeAeDLOCyk48WtP7xRncmlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی‌هوش‌مصنوعی‌از قهرمان فصل گذشته لیگ برتر؛ رقابت بین دو تیم تراکتور
🆚
استقلال!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/30219" target="_blank">📅 01:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30218">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEwkNtBgB6UJPdyEFUzox8kj6oI_TMRqv6B67L6nKUgNdocwHlCJglWoKN7t3ZpZgoL9ILcD8ATqusXFpqy0I_BgEJ_AzRwHExuPVlAPQ195cyIH6BPu2B6cqtdsky8ZSMLwCiUndqt7IpgcfEz5FMXFXa6Zyh-iNE3lp6WUKIuIzUjvbFxHAa5WPfu9I14KBqZGD6aAf6lvtcvSIFL6Yb84WtcSU__euZN-IHvUY9bPAViYBqDJWEOHRY1uRgKzN4MD_07vOR-_qjwx7ib4m2_55Uto-z9TJKO2hu-hFomfbBAteZKItdxxgv-p4kVcCv2mv6QFnK0zZ5JtvTbZOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحبت‌های تند و جنجالی اللهیارصیادمنش فوق ستاره ایرانی لخ پوزنان: میدونستم قلعه نویی هیچ اعتقادی به سبک بازی من نداره. تا روزی او سرمربی تیم ملیه هیچوقت برای این تیم بازی نمیکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/30218" target="_blank">📅 01:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30217">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8PprnrHuUj6P1Qunh8ppUTWApMSOHpzLKuAYrTMjcFwskvJjqgGFG_3DN6VaFKGF1AM48s9dqnjc_vpWID9NXH8vnrQFjnABOkmnPkmmjqWmxWlYnuO_cZlWo9VIQRtOVIhLP0pFX1SDNmgGikKz8ggwxia6XeF9MtGKLmKbCtVTbh-lsBWNJRrUaUibnDyNjurBlnyJ4bSSpmfT5WUgqlzC9iaZ_Ya42g415XFTs6iKR7XU-lLNDag6ssfKJjvyY758j15DtIy0J1mxnk3XP-li8wqa1pbe3bea-JHeeXg9idgVEelQvyZ3Xm9lrrIOglP-W49PI3VxM1T10YXkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرشیداسماعیلی‌بازیکن‌سابق‌ آبی‌ها: رفته بودیم اردوی کیش با چندتا ازبچه‌ها عکس گرفتیم بعد از ۳۰ ثانیه همون عکس بین فن پیجا پخش شد. از اینکه به این سرعت عکس پخش شده بود تعجب کرده بودیم. بعداً فهمیدیم که خودِ سید حسین حسینی ادمین فن پیج خودش بوده و اون عکس…</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/30217" target="_blank">📅 01:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30215">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‼️
سعید الهویی مربی‌تیم‌ملی: با اللهیار صیادمنش در ارتباط بودیم و قصد داشتیم در این فیفادی او رو به تیم ملی دعوت کنیم اما مخالفت‌هایی شد. منظور الهویی احتمالا اون تتوی شیر و خورشید اللهیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/30215" target="_blank">📅 00:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30214">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff5c924093.mp4?token=kVacGnyS4ePa9VhUgq0Ql60zvajLbpOElM7CcgPyxQGDivrix2y0Af4EbCuZ7fUdzDsPCbRIeLRPd2_SYEejVxNbbZ_H1O8q_bO4aoiR6yd4WytGocTSuiph69rGtuyMhLuEv9wRu5V4A8eMZI1uWKbTX8-nmesnJODvH14zOOrtCP93SkX3fwBfWUr0VCvML4dCSa18F_aa3L4bQnAXC_ykbJongn7XS6w4MImUaKrEvzuPYy0hpI4L_C4kiWc-B662R1izrdpFlMDW9vd96X3X_D9XFmdp1OAnXA8Ns_7AYufBKGCPaFVcMHIXR8HL7eKhUV5-x3g7vpAf9MvIhLX-pAG_3FjrK7Nn66017ehdpHZnIi9k_wGE75JAJh7DDDKyJgbCR2s4ZZZ5eR39Wcoe3scv8kFQrOlGyNcgXFv55VqNdB_Yd8vZCh8fJr47aCgoH0YdnIJUj_2sajV9lAkSPB69ully5lf5PzYQNYV9Ps9vlqechqDRDtNdUvzydqP90L9Py7RFS68l_JMhmhdZjRYrLswNlT5kTEb-m2V2H4lTa6N3Ve3-3qMUtRCI-2Y6cM8zGDHd3XFyhiqGe87DhBtFVmKkFAqqyXmLh_-bYTn06yGa1SGemt_rYektlyHi4FVbFPzmTRGEvroR1JCgQFsOwp1KC4uQmWhGrdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff5c924093.mp4?token=kVacGnyS4ePa9VhUgq0Ql60zvajLbpOElM7CcgPyxQGDivrix2y0Af4EbCuZ7fUdzDsPCbRIeLRPd2_SYEejVxNbbZ_H1O8q_bO4aoiR6yd4WytGocTSuiph69rGtuyMhLuEv9wRu5V4A8eMZI1uWKbTX8-nmesnJODvH14zOOrtCP93SkX3fwBfWUr0VCvML4dCSa18F_aa3L4bQnAXC_ykbJongn7XS6w4MImUaKrEvzuPYy0hpI4L_C4kiWc-B662R1izrdpFlMDW9vd96X3X_D9XFmdp1OAnXA8Ns_7AYufBKGCPaFVcMHIXR8HL7eKhUV5-x3g7vpAf9MvIhLX-pAG_3FjrK7Nn66017ehdpHZnIi9k_wGE75JAJh7DDDKyJgbCR2s4ZZZ5eR39Wcoe3scv8kFQrOlGyNcgXFv55VqNdB_Yd8vZCh8fJr47aCgoH0YdnIJUj_2sajV9lAkSPB69ully5lf5PzYQNYV9Ps9vlqechqDRDtNdUvzydqP90L9Py7RFS68l_JMhmhdZjRYrLswNlT5kTEb-m2V2H4lTa6N3Ve3-3qMUtRCI-2Y6cM8zGDHd3XFyhiqGe87DhBtFVmKkFAqqyXmLh_-bYTn06yGa1SGemt_rYektlyHi4FVbFPzmTRGEvroR1JCgQFsOwp1KC4uQmWhGrdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
منفجرشدن عادل از حرف پوریا پورعلی؛ عادل پرسید مهدی زارع تو حموم چرا اونجوری شد پوریا گفت من و مهدی باهم بودیم که اونجوری شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/30214" target="_blank">📅 00:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30213">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5iOohwdnf-G_mYVgJRBpgJaUPLDFsIaYS1Z6Fln5P-_hPiAsbXJVAJLs_AyZrS0H0rgkm9H2g69-are2oOSRCU_GTSitu76yQXRsfnrKq8m1VtyFPYmv2acCWiinKVxJmI5Im87nGSenY8lzfQe7686OJfZCjHEtUHikad2uAKzDl4quXsswYJ_ZSnswb74u3pb1YeYFgtYaYXEru75UUJGCnPVnwGsvR9Egigg4A9EOOXXinf2Ftktr5oF4sSssvdhzl0QYFPLcSeV_JkMX_opRfKFVEJlxMJj_kMUG_nHVShaimsDCiBxMESORq_ss4zBsTPQKrk-cmABTFdE8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
نمایی‌واضح‌تر از خطای‌شدیدی که باعث شد فده والورده حدود یک‌ماه دور از میادین باشه. تموم کارشناسان گفتن اینجا اتلتیکو مادرید باید دهه نفره میشد اما داورمسابقه بازیکن‌حریف رو اخراج نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/30213" target="_blank">📅 00:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30212">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8W1VLChaLGrKD2_Y5sLsL9jaZnfqcZjvNTRjK331rjw7xZ2jDEm6DdlKk00fPgjyr0KpjaI9TFE8GuIexIDNKy28_hAfcAw-c636oECLjQgJO37K0KNSIOFtcS9NKRqYjWHqkacIG2btyaLu6ZMSoaUN2OGy1HQxp-Vkv0xXC8GvIynLMSHCNO2F6sIND8kmTtVDwvCD3e1Aa_pylEth7n21DgI7KnBDW4Ri_v4C16lk3wwO4SEsX65Hr3p_pVomzf0KIYQ7ybQKK_qXIeaZlK6h0rJlHunrZMAmwvV8I9d2Ffiiagmvge_7DCJumS5lM53E-n2CDcA-HxVXQC-nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سعید الهویی مربی‌تیم‌ملی: با اللهیار صیادمنش در ارتباط بودیم و قصد داشتیم در این فیفادی او رو به تیم ملی دعوت کنیم اما مخالفت‌هایی شد. منظور الهویی احتمالا اون تتوی شیر و خورشید اللهیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30212" target="_blank">📅 23:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30211">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9Iu2H3gnLgLov0a13u6c5tj7mjyWr7bdfAK6Aud92uGMACWy3h-uLB0qt1zF4eQSiJwTuVd5ojGehdlehlfQyP-QPFwpV8pqu9BJeWSjFwUNAFgplhRhn5g5NLm9SuQq2ZOBN-1PuU8bKaFTPIKEnE4CpVm413TWeNH4HcaJS5dwYG-MZrIIIHTdyhE2Y2LQZxJQvIe889mYQ3wdlHXp4RUoSqZtauz-gewslgJKl5MchIQFvU2dGLbBgGCenJvriDmFKgfGenUKck8SPmzskHSz56m29p78HBIfnVyebv6Kr0tIGMT4dkP3T_dkBEDzupFA7YuJWWrlhlwuTpStQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
طبق‌شنیده‌های رسانه پرشیانا؛ کادر فنی تیم ملی با اللهیار صیادمنش برای حضور در جمع شاگردان امیرقلعه‌نویی برای مسابقات جام ملت‌های آسیا تماس گرفته و این ستاره 24 ساله که عملکرد درخشانی در اروپا داشته احتمالا به تیم ملی دعوت خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30211" target="_blank">📅 23:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30210">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8d4ab1809.mp4?token=rZw_hptfWEmFIUPuZGzgRzb29nhKQaUX4QZ8oarWZuD1ZfiDp1yoD9l8FOi6SPuTFS_gARdaC83roTdly1qibCoCNBsfPIYjHrgoezTQRiVYI1LI2IRLEk3KuCx5-klnOIJKBszeIaa1K0nnszL-aKtfNzO65zxZf00-c-n3pukq4PyFuYOpeAzAsCp7Wa-_IJe0KDTRGYut8Ow9ivq4CTWtzUUNqJk60to2Qijb0bt5Tm6HoBSj0Z1Jvj-_Ca87Qdwj1fyyGB5VeVc8TSfhqY2Omx9kcjep6Iv3pmwB4u441JFXhJGnVCMVhZ2ZZUcSPlilOU0yo0O5k-JKMFH_KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8d4ab1809.mp4?token=rZw_hptfWEmFIUPuZGzgRzb29nhKQaUX4QZ8oarWZuD1ZfiDp1yoD9l8FOi6SPuTFS_gARdaC83roTdly1qibCoCNBsfPIYjHrgoezTQRiVYI1LI2IRLEk3KuCx5-klnOIJKBszeIaa1K0nnszL-aKtfNzO65zxZf00-c-n3pukq4PyFuYOpeAzAsCp7Wa-_IJe0KDTRGYut8Ow9ivq4CTWtzUUNqJk60to2Qijb0bt5Tm6HoBSj0Z1Jvj-_Ca87Qdwj1fyyGB5VeVc8TSfhqY2Omx9kcjep6Iv3pmwB4u441JFXhJGnVCMVhZ2ZZUcSPlilOU0yo0O5k-JKMFH_KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دلیل خط خوردن قایدی از اردوی تیم ملی توسط قلعه نویی رو میتونید تو ویدیو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30210" target="_blank">📅 22:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30209">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d21acb31ef.mp4?token=seEdeI-y23AR7H918btR9aeeikm5d8RXfdeEW4lmF2mSDqY6rbU1QXQW-0fni4EUN3I7vPaMMCvNQFaLj7mFOGQHNBhMj-1R8ClctpMuF4k0B_Wyu8BRUbnm2_8n9i-W1BJacZBqXqlp8KGeVBxc-OVnZ8wL-F7o8EKZq9SWSSCuDDuYLQlNCcTDqmP2DCUzGwjvGYvGFxPZJrgQTH6vyzTZEkLiE8iG7sKSPx6NIzGTNi7f5fuApMbDGDo9_vAa4CIWwDAw7hJAttQ9Eu3uJGpzskl2naHysTnUo-8Z0Yr9IQYSkKVbXHmgv9GciZ5Jzgj_iM1olO_sgDb9WxYJtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d21acb31ef.mp4?token=seEdeI-y23AR7H918btR9aeeikm5d8RXfdeEW4lmF2mSDqY6rbU1QXQW-0fni4EUN3I7vPaMMCvNQFaLj7mFOGQHNBhMj-1R8ClctpMuF4k0B_Wyu8BRUbnm2_8n9i-W1BJacZBqXqlp8KGeVBxc-OVnZ8wL-F7o8EKZq9SWSSCuDDuYLQlNCcTDqmP2DCUzGwjvGYvGFxPZJrgQTH6vyzTZEkLiE8iG7sKSPx6NIzGTNi7f5fuApMbDGDo9_vAa4CIWwDAw7hJAttQ9Eu3uJGpzskl2naHysTnUo-8Z0Yr9IQYSkKVbXHmgv9GciZ5Jzgj_iM1olO_sgDb9WxYJtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش‌جالب‌عادل‌فردوسی‌پور به برگزاری دیدار دوستانه شاگردان امیر قلعه نویی مقابل ازبکستان: دیگه پدرمون درومد ازبس با این تیم بازی کردیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30209" target="_blank">📅 22:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30208">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxQ0ZYkgijpvYN8gQq2KMMgheJAVIacQnOHGvIzR2f8pB6OPVsiTf7RmZLvZy3bnqexHmT57nI99DhEBAZwJtoAqWhZeQY-MTacgy646ybdcAoXP1CCVyNxOQ8wFeENmCc3Up-rdXggmjUOMYMDf0ITfEQBgPgBmiiGrwgo4vFIuFgYMISuBkK-gkXFNRn41f0MjDOOGuzU4oW2gQV8M9SywU4SYOlONa4zpzKDXvfZNDfWEPkQrv0RgusneNxia5n0fg5BVfpMte2OSVtfd-f6ziCIV7sp-4lO5jfdZ06VNcc0ST8H00YllmHYOp3STe8Mjg0l5igXYBPB8lN7xBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سال2022دورتموند هالند رو داد منچسترسیتی سال‌بعد منچسترسیتی‌قهرمان UCL شد. سال 2023 دورتموند جودبلینگهام روداد رئال‌مادرید سال بعدش قهرمان UCL شدند. سال 2026 دورتموند آدیمی رو داد به بارسا، یاران فلیک قهرمان UCL میشن؟
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30208" target="_blank">📅 21:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30207">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3VIk_G8_hRdrLsSxifKCP20kfQHR87QY7zwgj5VH7zMd9F0tR241Ieej8Y991IG--HPoela74S1Lm9Q9CPaqHH0_ZsFGDEvklvVwOKv2hlmR0ANxGKJcYnQwltyu0lO3BaNb4El6H5y6OSeADH5ZgsiSZzRr4coo5jXZ5bTWWwIbt4HaYoF1h4e-VHbVIFzHMLwvtz0tRBtm4R0XrbMo_wbwpjdNrCnfYbHXlycC6b8lcnx9Un5E57KG5Pu1SbQ9x7H3N3tn0jHOX3zPKf7Zfu8R5yVIgXLydRabvPXihUtWuJo9ADr795_8XlSk0I2_t7PD_KwZd2nL02FkfAnKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
👤
گلزنی تماشایی لیونل مسی در بازی بامداد امروز اینتر میامی در لیگ MLS؛ این 930 امین گل لئو مسی در کل دوران حرفه‌ایش در فوتبال بود‌.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30207" target="_blank">📅 21:17 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30205">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A8btCncxKCNox4f0KI-PrgY25AdwLNYSsDv65-13AesDAvlkrbb9RFpwyvNIMIzQg9kMCrq-UW-E1o-TrDmZzKiARMVAzA8lL5Jr-iy29lD0xbPz-iMgkATiW6pRTkM7uXAtLYkvA6xIjDUymdUS40T_Ho1cCZ9nJ7ulcS2jDjGeVK7LKVYuWS26SlmXoM27-Q33_tIEFHSGTgO2Jr8gZXqwHZDhmE9xNgIKTh-FKFlENpGBRW_70eFBb-YIx0sVZhHMXipYEWFlTA_FsUbdCsdfPVajZtj_YUga-hJ4t-BwJUAjCy9armCgbb-CkW9fvqQuBbmy-NZvsOMWV-0f1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s-w7hhQDVdhBLZHm7UGae26nYi5nZySGv6vsl1uxoEYWFI9F7zTmHlp2mw3V0z2rUN5gToFNrP3eM0RGuvema8WlcpaXEXwMQX2tj-DS1EIV2D_xfLuvBwFuCVZ4Mk77nCilAeWW6HHQZEWezsHry32Yg7H0JH8gBaIutjq0kFd9iRSmIK46PwXymenweMEWWzuLTG3NsWM7qRKUp-CY_cYJPKN5w1RWVJXOGof2Svp5iK3kid6g5g7f_KSzXzXPDU3U_McDh4aOeE2WLg1x4IynFV3PFSKHcU0ab35q7YHOBQEfXy0wRdgnZm55BXI1FOx0WOOTncxv2yAFSSipqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
پنج بازیکن برتر لالیگا و لیگ جزیره در فصل جدید تا پایان این‌ هفته از نگاه سوفا اسکور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30205" target="_blank">📅 20:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30204">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtO2v2p7Uebg_UYOnR8UabkAAX3YUD8S7mlV9lV0EtA5fKn7QHARBhiIw3BkfBXOS-ZPP2I0zQ0gsfYoP8WHd7LYKzQw1kXkYEa0gkDykDT3hznOcZs5razZKX0Vx2S9mfaTPk2kM3NRWy08sTZQ3lvx_7yJ158PqtQnWme3L5AA4baU4DL4aDX59XJo7UD6--WvQVLXor4S64wxMPgC2sCFBb_M0VXI51JS7pUoZ8k8ZJTVVHeyY8CGksThd3myPXkhELqgUJZvcbsR-3pUGu9-PXqJe-OwufCxJdQOMrQdQN9KGY5DxZ1TOyIYksBqEg_gpCQFFIZ8XYT_7dW9Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشود عربستان‌ سعودی و چند کشور خاور میانه‌ در آستانه‌ شروع رقابت‌های جام ملت های آسیا بافشار به فیفا به دنبال تعلیق فوتبال ایران هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30204" target="_blank">📅 20:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30203">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ada5d0f44.mp4?token=XpPkrCmXgVUjWoI9G_HAczDP1MCul7j5L-qI09RBNYifYzWtrLhT96PiEJUI4YFwh7AOaAToVjuc1fm4bvrHa__vlnNJ0DOHb2cCQolW5j_4mgPoikjhugBrkxdrRwEaEoTPMipnGDGUBYg6-Q07atmHciQYrro4iDtPeJ6ImAZMvhx2BR3dbHAirKAxYLKU1gSRhFDWN3FYO3AdIpekCB2Bi7MWyvlGFAdEpht67iHvxAZVSHo-xQl_aJYhehWYtkgAvsgCnkjz2RVEZlPbcQmmcNLUESOktna7U6he1RtfZGLnJQ3XZ5tkujb0HwnWlb0zvrmax5yBO4YZrYucKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ada5d0f44.mp4?token=XpPkrCmXgVUjWoI9G_HAczDP1MCul7j5L-qI09RBNYifYzWtrLhT96PiEJUI4YFwh7AOaAToVjuc1fm4bvrHa__vlnNJ0DOHb2cCQolW5j_4mgPoikjhugBrkxdrRwEaEoTPMipnGDGUBYg6-Q07atmHciQYrro4iDtPeJ6ImAZMvhx2BR3dbHAirKAxYLKU1gSRhFDWN3FYO3AdIpekCB2Bi7MWyvlGFAdEpht67iHvxAZVSHo-xQl_aJYhehWYtkgAvsgCnkjz2RVEZlPbcQmmcNLUESOktna7U6he1RtfZGLnJQ3XZ5tkujb0HwnWlb0zvrmax5yBO4YZrYucKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
فوق‌ستاره‌ای که بعد از خداحافظی از فوتبال نه تیم ملی کشورش روز خوش دید نه باشگاه‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30203" target="_blank">📅 20:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30202">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3f47656d4.mp4?token=O6AB8P9o_CFFnr7fjV7U6A9N1hUDSbz2PxHPSv1AQc8znA_W1Fe698ikmr_GZYAGXUe3OA7pTMgYbLXzaf90GN72KeSKr8tJ8YJwFyQss3qb-LLCs3SK19Fypw7wXo25X2R13EY5Hh8KksJgV1_ziBNRb4AbGiVCytSkZHmtV_LxwU4mvzG8MapIGm46tORnPEobF8gvZHuOJ69e2ayw5DBUpjlzJBEiENYdrvIhJ01cY5J0QvhxVxvo5t0iNRevLGlGmrpXAaHK53uKKAS-Ic6RooSztg9aJgrh00E-NBJ1F-nCspyVZtfTdC9E_Np_4W54XdM3clLU0CPS9A2kyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3f47656d4.mp4?token=O6AB8P9o_CFFnr7fjV7U6A9N1hUDSbz2PxHPSv1AQc8znA_W1Fe698ikmr_GZYAGXUe3OA7pTMgYbLXzaf90GN72KeSKr8tJ8YJwFyQss3qb-LLCs3SK19Fypw7wXo25X2R13EY5Hh8KksJgV1_ziBNRb4AbGiVCytSkZHmtV_LxwU4mvzG8MapIGm46tORnPEobF8gvZHuOJ69e2ayw5DBUpjlzJBEiENYdrvIhJ01cY5J0QvhxVxvo5t0iNRevLGlGmrpXAaHK53uKKAS-Ic6RooSztg9aJgrh00E-NBJ1F-nCspyVZtfTdC9E_Np_4W54XdM3clLU0CPS9A2kyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
فوق‌ستاره‌ای که بعد از خداحافظی از فوتبال نه تیم ملی کشورش روز خوش دید نه باشگاه‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30202" target="_blank">📅 19:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30200">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uYbtS3UldyLddT29fJo01lge9y101HQOp2yicoBQrGqsEgFKYROi-nMuw1IobfXj40GFuNsHkc3_VdhYUg5knqYtyCw-NEh93HHPAY8JOvm7fdxLDcmVyy3OeALGcf98pTUoxYHSjjdHMlFkBGvSy-U4y-HQ1zJe00g1kkbNV2zlfzRuuIvaoprCR4M-fM_KhhEL7F5-MXATvvLiakOumwtfYtmCW-RUGMrQ7VWqj4cPQizSx9GnyOHNLmeIKcLVKQi0gIPhmI1dX7QfSKarETaYSv1kSHW1hiap6Hk34DoA8dSib6SkZgEsQnqM_yw-EzrR92nZZ4apY4W9svd9qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kcRZ01_-A_mWhOe6BeKD8ZH1D2u82vXhTTXBmSfy4yHBB0tHBzuz-CkOdrj9cAWWAQ2HvzYogT_KXw22SdyoEVsARU08soFhKtSNlSlUYhYzbSd6zFC0S5NCS764gNxUoZwf6DNJbI-7LS7qmrASCXgFfcXjyn6sXyyl0K934GdArgK7H8xvQpU4LATd4Wn_qkmicg8tDQiCSfsPsrJLA_8dm-REMugrxZk1XdXxlSjiGNfiZ6mIc31XQ9ExueyIS1INILKHnYWGFBNgztzR9csWD-HXzkJi770-qnwY5gEBQgORBTzSDend1sY6TUQ4iBVxMMd6I7z_vVrWDaKmgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
👤
تعداد خیلی‌زیادی‌از هواداران منچستریونایتد از مدیریت و کادر فنی شیاطین سرخ خواسته اند که در نیم فصل کریس رونالدو رو به این تیم برگردونند. قرارداد 2.5 ساله با CR7 و خدافظی از دنیای فوتبال باپیراهن‌ منچستر یونایتد رویای هواداران این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30200" target="_blank">📅 19:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30199">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xtj-WChOLkjpSQVfGMxhf8-kyq7R_7FTSoY-xtNVdcKjtpoQLtaIntuX_JyUga2kd_Ou1HHReLDJIAT2yjI9YEkTjsCjly8r-wkVSpp6wIIAYNYr1e2eeYyvMDKeR3OhJ45vLabB7OpO0z0I8FYoU3XhCXruyAwEHNGpxce-n-DgBUmaPg9twMbbbKCIC8c7hopYpwUGnf6nAix_gmKIGn9PX4i4hz3pmmZl5QCOdNVuuycYNtnsok5DA_TxRvYce_LTcaO9g2GTivLTSHzYayMAQ0Da_DeC_o170hFn4Dwkras2bf1QyQJlo8SDzN7MMZArqN4RAhfMG16kF8zJkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قهرمانان10سال‌اخیر تمام لیگ معتبر اروپا؛ پاری سن ژرمن و بایرن رکورد قهرمانی در لیگ‌هاشون‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30199" target="_blank">📅 19:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30198">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vP4tzjEqchkSgHeCY4GxKtTiVyn5s4s7b7Y5wTiOkC7Q_mbZ3d3wVwGyGzIcNIM7TWWy58O-oFe3dsMWECMfO_4LUmbmfB9lOdKIEtHJ4H6yPKmJD6cx_3xtSi3tur3D2fccUMiugaoHWGaq_4H9e2t02QqKwgrR6l-3LQOANd_-e0hFrUaAAyuJJqFDJp3eU-dBDPD071UICU5umzmofNNXTz-qrUY4sU0A_qzY9R1GmU-cNEZv20ptw7WIgtl53p8pbfheST4_2WsHjq0krjqv2_5JIfu1CQkMSpRJzKyaSaYuvLGmPKbQ8HD8ehXR8_kbAHe_pzF3zfBFjtqJuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه عملکرد رافینیا و وینیسیوس جونیور در این فصل رقابت‌ ها؛ جالبه بدونید وینی سالانه 24 میلیون یورو دستمزد میگیره درحالی رافینیا در بارسا سالی 16 میلیون یورو حقوق میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30198" target="_blank">📅 19:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30196">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21bbbf6ac4.mp4?token=IfuxeXR4jiQ87qvpmTcGWqrkanOtkigqKrA5MRs2Z_neZS-NTlCaXtBsd48bPfYb_rCbWMVZB-vQUjBorachcZvDLuUFOhiHOzYFnGbsU788sZj5qwvBQ1tLJozWy3-_p9MqD-1wQFob4bfsPdjinznUQs0Otie11gMzBb8X4KBHEcO6Ekw_IuYfntnNIkP3m4wdCLjI97EKGDoZrHCouknKq7LqbeInUapFz6nb12bbVqiWl67wVC5PKV4TnVaLH0-bNvFgkRE6_TLort_eQsG_92_I-tXUvHLX_GTrxKcoxRIP-oiZM1qHrg6-ZwVRMEwstGEMYE1iXgppMl6ydBnizAA0Lp0hGyR9ssBMYCzCWlk-zGPuomPOn8ZoYLj7f1ySd2PcJ0YSPKClfrlgA8BjLdYXIY9Ur9wD0g-4ozuJlqS1CXrCUFsA9un96ZKN6bpqX5AtKugkgURDar7_wiauRMFHi-LzHLhdXrUj-kMSXoC88NYkAYyTyddBtJDi5vuhvHXylfUviMqQjWr8ZRkFBnSH1jgfPGTQn5spFoEtIGvCjHN2dJrkTLZEkmb1qtOn30WYCV6Xas06f9v-372DdgoXn4gr9bPw21c2l9awMdcio_gpauu6Su-jJBIYgm_QIGAoQR148T0HQ5O2RmKwtcrgOPAx9pHBUE4qugA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21bbbf6ac4.mp4?token=IfuxeXR4jiQ87qvpmTcGWqrkanOtkigqKrA5MRs2Z_neZS-NTlCaXtBsd48bPfYb_rCbWMVZB-vQUjBorachcZvDLuUFOhiHOzYFnGbsU788sZj5qwvBQ1tLJozWy3-_p9MqD-1wQFob4bfsPdjinznUQs0Otie11gMzBb8X4KBHEcO6Ekw_IuYfntnNIkP3m4wdCLjI97EKGDoZrHCouknKq7LqbeInUapFz6nb12bbVqiWl67wVC5PKV4TnVaLH0-bNvFgkRE6_TLort_eQsG_92_I-tXUvHLX_GTrxKcoxRIP-oiZM1qHrg6-ZwVRMEwstGEMYE1iXgppMl6ydBnizAA0Lp0hGyR9ssBMYCzCWlk-zGPuomPOn8ZoYLj7f1ySd2PcJ0YSPKClfrlgA8BjLdYXIY9Ur9wD0g-4ozuJlqS1CXrCUFsA9un96ZKN6bpqX5AtKugkgURDar7_wiauRMFHi-LzHLhdXrUj-kMSXoC88NYkAYyTyddBtJDi5vuhvHXylfUviMqQjWr8ZRkFBnSH1jgfPGTQn5spFoEtIGvCjHN2dJrkTLZEkmb1qtOn30WYCV6Xas06f9v-372DdgoXn4gr9bPw21c2l9awMdcio_gpauu6Su-jJBIYgm_QIGAoQR148T0HQ5O2RmKwtcrgOPAx9pHBUE4qugA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی از انالیز دقیق عملکرد خیره کننده بارسا هانسی فلیک در این فصل از رقابت های لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/30196" target="_blank">📅 18:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30194">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FwFQDyfHsqO_ncFA0QaJ9d1v4caNwR0ZkNabLV5bYFq7YEeqTLSpmqw15uG1hZOMLGxF7y9YlEoY2AWIXyikLiguzFbCJy3-Fh3M00emzUP3TgyfZahN3jJXKWW4_b8vcJy9NSasXi8K4WiUmduReleXDEzHNZzPdLyPX-xxQv_0NABHSBg-ghN72yO90yCwQTOqevfdlApFyY8MBx_U-A4WfKpcD025I2Oz3mu3p4ZfCgD_DwBoLE2iNa4wMbugTcASAdw9vtpED5u4ORV4ot0xamBwvHwDqxrThC0aNNO9ktxY_yCurUKaKxR1uWNRbnfgNeW9A1pyw6h5U8r4-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L_9ZbLJYlGJXiYl_JIjrC6qlIBAO3rY2jHLQHjgfS3INZzos6YLQaQoIImqBHPt-JJIVGikAITZ6Bmm682a4aTi8xD6jsr6tqejv6M_eodjwK3rrseExI5uXmTwnOvMVwGMLntEHaRTXR-7LnEISuzIW7iQc9muhfdgWvRKKL2cVgREqWsDfbNrIYegwtSp7B04nknDGvNkKmKGNAwTA-1Ldzn5HO3k0V6n2HrKb504jNPL7dUy9DGSUHUx-lIxJFD8CHVfU3DBM88OLAhe3R8VtZ3bL1r_F1JLvyJmBXOVMWnlbTPz35oZ_r3vsTI5zQjf_1ZU0FDczmC_6qWZSaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛ میلانِ اموریم در دیداری خانگی با سه گل از سد تیم‌لچه گذشت. میلان با این برد یازده امتیازی‌شد و در رتبه پنجم جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30194" target="_blank">📅 18:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30193">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSidsRWzD_HDsiqzSUsUHcBOvQBLKm4eC3tdlDHrwj2uFXDvBsMQKgA4ARFL4njlYd7WaGiuCgGYqxSbB40vn5IDYiCYp5EJ33GS1VVruWuiCKi9BDVKSw7uPJrJewct5voWKeZt4DcOG1oAjx-necjO_E6QbWHEDfRIry7SG5dqd9n8NcIeEf8nLhG3na7RTpCEWH6TWe7cXkpdyMcAQGFWl8NDwRJZUQT9T1tg4122jnMkyufcIC7KDjmH5RHuD3R1qs2oqs69LZlkx5kv-OpSZqUJufI2JsganAEcPCuob4LUudxxHvwWCu37ejSk8g6L4WF166IcZJL_-n1rIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
برگام‌این‌چه‌درخواست‌هایی بوده که بیرو داده!
‼️
علیرضا بیرانوند درخواست معافیت پزشکی داده و دو درخواست از کمیسون پزشکی داشته که اولیش این‌بوده‌گفته‌چون تتو زدم مشکل اعصاب و روان دارم دوم اینکه گفته در سال‌های گذشته رباط دستم بار ها پاره شد و با این دو دلیل…</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30193" target="_blank">📅 17:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30192">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9jwnouI5mnW1Tn2VFZlWwt-Lr93cITN5RGdqFwFTmN212cYnI1yzE6IkKmIwRvDQh3lCVFOJC68b4b0_S8ayub4WJfhQexz-MoD9mm4C9-28vERVLQlXNFOEAJYqSInzDd7s5Wkbshb1EBVmdLg0D9ZD5DULVNmrpzwUiyQvHT2EdFTiDFLNXFuzp9JtzfCdHVK7DIR05LTDAoOlfhUHKoE930qD5Q7V_BQgifq241THzL3UTgP70gb0bijgcJKU1VU4Kb2q9-gT5EJbu_B8u7-z60r7hM5WDLJOIUeXCkYl2PaIXGh_Y_-6c5jTFSvkGGvH5VE9YLyAAdF7ONuMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
خبرنگار:
بارسلونا این‌فصل خیلی خوب بازی میکنه‌نگران‌نیستین؟! ژوزه مورینیو: از نظر تاریخی و فرهنگی رئال مادرید با هیچ تیمی قابل قیاس نیست از مقایسه های مزخرفتون دست بردارید. بعد مسابقه الکلاسیکو از زدن این حرفتون پیشمون خواهید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30192" target="_blank">📅 17:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30191">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa95e86e27.mp4?token=rJ4-i8MES27FLA64UxDF5YFDhEZItpGZGMjvs3HMK5CVB0Vl6VI1Jp1gQQEXANMDkw-N7S7L3uMlKyfUbGykEfVEQJfMnFnPLnqsr4053f2pwqTAV6Tu8_ZyiXBM4eGbw97aGixdvi2-R2ls24HyHAR4A0zuns3x5N577GgpTU5UZzTZTOD1axmNd0D5B_jPhXm77c6nS3DswIHclSdUhBctc1RRfc5nhF7R6ddFlVXunhf8gzR4UJQaOJ-aLqc-8UXJ7R3tMZNvIXBVdcrK-WHeG9TItpPACqm7PzTLAx1RgSGbx5aff02jKolHKO0FfiHGw_6IdXyAlJcpYt7Utw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa95e86e27.mp4?token=rJ4-i8MES27FLA64UxDF5YFDhEZItpGZGMjvs3HMK5CVB0Vl6VI1Jp1gQQEXANMDkw-N7S7L3uMlKyfUbGykEfVEQJfMnFnPLnqsr4053f2pwqTAV6Tu8_ZyiXBM4eGbw97aGixdvi2-R2ls24HyHAR4A0zuns3x5N577GgpTU5UZzTZTOD1axmNd0D5B_jPhXm77c6nS3DswIHclSdUhBctc1RRfc5nhF7R6ddFlVXunhf8gzR4UJQaOJ-aLqc-8UXJ7R3tMZNvIXBVdcrK-WHeG9TItpPACqm7PzTLAx1RgSGbx5aff02jKolHKO0FfiHGw_6IdXyAlJcpYt7Utw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صدرنشینان لیگ برتر تا پایان هفته ششم رقابت های لیگ برتر؛ هر هفته کدوم تیم صدر نشین بود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30191" target="_blank">📅 17:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30190">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRtmJXyg-J0kL3i2lLPYf_sBfftWvn2XB7fUWJaCjYYNaLf74lsn0R-BRN2fy04H4xWOpuM9AozA_nk0QGE_AG1L_q4vF97y2rj4QsZM2XboTvU_ySFVNV_vXs3YhWQaCrS67K2X7H62-9zoxyfrsRktkqCMB1YZl3Rgh3TxybqeFBi1WK4HKvDu6Pp3zSSiiPrmqM2Ammy3Gd-PKAcw6SoOujk8wPbTHZuvZ2Sy5-rg5N6NNhrMTtUKLWc1F-Itp743hzZvKVLy_gmWO8TgXnIRt3_GJUpu_F3KKZbMrWm3gOSBGGnrrco2utQ4QI_i43PDwPqLAWS3wR9tnFzo9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلیمانی وکیل علیرضا بیرانوند امروز صبح بعد از کلی رایزنی باعث شد که سربازی‌ این گلر تا اوایل آذرماه به تعویق‌بیفته. او به بیرو قول داده که تا آذر ماهی راهی برای معافیت کامل او پیدا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30190" target="_blank">📅 16:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30188">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e07dd6207.mp4?token=LF7W_EQ-mYfvudicwYwERCIfUKGUHQe7Ah5_TcmBPO4qC0S5zzwKboQV1WxDbPQ9TeXvERrxz9jPEAnAGpl0o9r3ySgJjsuGu62zwZvI8m_kcgydN_yImoX2rjLffmZMkhRd3HjZI5nxrX21Z7sL083aJxDmPqBo7Pji0aP1IPYX90G5QKQbw24PwlVxjUu91nPLPonWcwmBlnnMVZPZOSGg-dT1tMtxabA38BpaqE2t5OPtQFm0QlnCQbUH897ujKx_u_bK-4w8oWKqfXL43qNfEHluWDNWjiswf_IuAeFavFE_BmZVbSLmMluXvG2WG2GwKclIdDK19uGfHHSkBIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e07dd6207.mp4?token=LF7W_EQ-mYfvudicwYwERCIfUKGUHQe7Ah5_TcmBPO4qC0S5zzwKboQV1WxDbPQ9TeXvERrxz9jPEAnAGpl0o9r3ySgJjsuGu62zwZvI8m_kcgydN_yImoX2rjLffmZMkhRd3HjZI5nxrX21Z7sL083aJxDmPqBo7Pji0aP1IPYX90G5QKQbw24PwlVxjUu91nPLPonWcwmBlnnMVZPZOSGg-dT1tMtxabA38BpaqE2t5OPtQFm0QlnCQbUH897ujKx_u_bK-4w8oWKqfXL43qNfEHluWDNWjiswf_IuAeFavFE_BmZVbSLmMluXvG2WG2GwKclIdDK19uGfHHSkBIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برسی‌لیست‌بازیکنان‌دعوت‌شده به اردوی تیم ملی برای دیدار دوستانه با ازبکستان و روسیه.
‼️
اللهیار صیادمنش،مهدی‌قایدی، سامان قدوس و علیرضا جهانبخش در این فیفادی غایب اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30188" target="_blank">📅 16:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30187">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4MvFYwPizY575iFaJyV8-gDFKby8SmFLgmh4SKao82xu_Bui6tD_OWlWRrHDZea70PI506c9Vj81rS6nvD7gnyJqriyfIofdUpoxtxtHh-4L_zQBMtrmJZEKorh6TGUlGygbRg1lTfsIqHPn6RT1_Ijwasr9_y1xNWvr3Hd0ZOuQySZF1j1wdKxJunQbBcHFBKnOr4_IWRgffWXWMUIsk3RQM6GtM2IMLcQrxCzSPue_IXXUy555lNPSGucocJuPFqmN-gbgN5oz1fdaM-9Fs0FFD6_wLZ_EH1VIyV2u5dgaDzYNozus2I8SdEdVy967foL34ql2DI5EZJ54ZG_Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گرانیت‌ژاکا ستاره‌ساندرلند تحت‌یک‌پیگرد قانونی قرار گرفته زیرا گفته میشود کارت واکسن کرونای او جعلی‌بوده و بازیکن‌حاضر به زدن‌واکسن نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30187" target="_blank">📅 15:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30185">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jfKMC3d_94C12Z8im3bseEh02OTeGhI6tMGSJzDs12rJm0ES4O5I6r2KLv30Whzcc7yru2KnJOVyXGLE_2Ca5WLMU2roCcAIx74fQwLzGeqG-2f5mlXXqXD1p2nwf7XNFqbZcCLmna8t5INKpEeukrnryCfz45XdWXNPTGKHFyTOBo6p0nL5vH3MqI-MTkHn9G5jOaxGDYOqGyHsWCUVZGoMHld1Br23JGtVeVKL9elB-8fweqbGXyZ_7xonq5YNODJFzbys_F3qLQvvn4EPJM1sYrfgCJUwUuGdn95nMnJ6Y8nTb7SjQK3uMGBRATkK4IP9e2nlAxOUyngXiun1GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dZUlfQNNhdhCbNoiDqcVC0b5MFMXG2XSOfc3RFOxSsgmhGsIcvj-DAdjsCy4HeMhDTr7wQDGMSSeac1uj0Skf2ANVXl2QmL4V0gLc_EucBlB2xT9CZg8WT2a3BwfK-dP8gIllknst9c0M0iUvGx1CzMft59WfN5UEYZvqAMjxw6_Cnroa4VlkHOXxVFb8513Q3AMqnvsy4Z3hK3lLuHwVgmI1Iru-vJ3Akx2lmOl662zig0KQ7EnjfNB3APhwjt0yGPaiS7RCxNJJvTxvwY4k6nSTRQrDK8iBArnBxIycMfqss9vKTgU9qpB6XAjAIVg3mNwjN7AmGYUSLYVqL6Skw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ سردار رسما به تیم ملی برگشت؛  فهرست هشت لژیونر دعوت شده: علی نعمتی، محمدمحبی، سعید عزت‌اللهی، محمد قربانی، طارمی، سردارآزمون، دنیس اکرت و شهاب زاهدی 8 بازیکنین که برای دو دیدار دوستانه برابر ازبکستان و روسیه به اردوی تیم ملی ایران…</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30185" target="_blank">📅 15:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30184">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8_WZr3WskXAV8ZhCbDrc8jQgkdaOjEJaURJOHafvK7KYDiv0PA7YirTjDaw1U_dCJ7vOKEN6a7fzpk0vVZxl1QFkkEVYsGjF2gG_rRmlTgNTnBMmJ86woZ6w7N426etn3a0p1ZyQAskkPimViBm5CM2U5ynUwt2-9ABrhR7e15Tjw-CNZpWX8swtK5e4BV8aNI079ZSVjWpjckWqgo0Wzw_-B24nql_oHlblQCnuEFk5uoR1ZtYFlHNYxi-E9Wg1VgiOkkZNuKx5Mih6trfCAzB7Kt9xRWfjKECmyHqgwUtu4tneCvft8IjZe996QSUrHMMUSDqr7E3EQ8bv-uczQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
👤
گلزنی تماشایی لیونل مسی در بازی بامداد امروز اینتر میامی در لیگ MLS؛ این 930 امین گل لئو مسی در کل دوران حرفه‌ایش در فوتبال بود‌.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30184" target="_blank">📅 14:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30183">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVeZGgusF-PBdZaTYkSEP2EnrtKwQUgUqSQ_8fBGZwFSVhyicXcoOchDiKunlS-gh2EMzorE6wU_UVw61u3zKL4IxQk7-yjmUT1tVyUfe7p6tP-6O8nDHZs9MwCUfT5bnRNa8FiNVemKG24p7nxRNpl-2q33Dyo_LHBv8lbk_QnyCX3d5v3EfYRRWW0Rx96ZN5x2RLtwyzbEBBqVhWwM14k7vaRWrENWXksHBgrSbcNbji0Q8dsUthn85hpYmk1T2QA93tanjkGtBykiMLDvNMZhynq4R5KdrQVJ89E8gU3XPzEx4QWvZmiZrQg1gLK_6Kp5uNwjHa3NFKF83hEUGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ سردار رسما به تیم ملی برگشت؛  فهرست هشت لژیونر دعوت شده: علی نعمتی، محمدمحبی، سعید عزت‌اللهی، محمد قربانی، طارمی، سردارآزمون، دنیس اکرت و شهاب زاهدی 8 بازیکنین که برای دو دیدار دوستانه برابر ازبکستان و روسیه به اردوی تیم ملی ایران…</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30183" target="_blank">📅 14:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30182">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVmC5RDc0LiVQyYX49cbxsPfRxIhac1UoGhfZ1svOkn-MaiZE2lRBL9epIEzLr8EITcXOQ2C-uV7SLomEq8x-dIP2FJmhgz7XUVb9GyKoxF_jXaP1OC9Zarw-IE2WqfZ8j7OMcrHM4fAGts_6cj0GHqWxRC38giwixzMNKs6WE-aiMi6o20nlflDBKAG45TCj8Az6DT_B9jRsPQ4xslBodrSguYDnq1tJunCSRfnWw9Y1kzr-aC751yYWCh4UIoy_pd0bfGQ1_zxoaBTWfN0K5TkglE1RSADUonKAcULfkPUI9T7VCbvmGV99jls_N6goOiG8DuZ0H_lSwiRbeqftA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمد عمری دیدار باذوب‌آهن رو ازدست داد؛ با اعلام پزشکان باشگاه پرسپولیس؛ رباط داخلی محمد عمری ستاره25ساله‌سرخ‌ها دچار کشیدگی شده و به احتمال فراوان حدود 4 الی 6 هفته دور از میادینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30182" target="_blank">📅 14:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30181">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‼️
آرزویی‌که محقق خواهد شد؟ درحالیکه خبرنگار فنرباغچه چندروزپیش‌ گفته‌بود آرزویش اینه رونالدو به این تیم بیاد حالا رسانه‌های عربستانی مدعی شده اند؛ رونالدو در نقل و انتقالات زمستانه به فنرباغچه خواهد پیوست و شاگرد کارتال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30181" target="_blank">📅 13:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30180">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dH9ISDvOsao2RNd8ZAqndUxdfu39OlAf7sB9tS0jXnzWjkRFXDn3NjYYEa198N4afmNsQ3MfWacIiKs_RBAqIFyHU9eMGolGHbFwmEfePVCO0HTK0MLC-cuUITXK371dMbc-PkYD85ioIxFYw9fzSQjTRRnJbAVxMJ33dGAKIS1JrGT7AEZ5inVlMIzJk-bpDmHD5_nmO38ROFUs7ZW_dHyVjqdQ_OfIV-BFsBssjRjfSzSGbKCKx8eps4Sh4syEWT5eXrTnF5F48v89ZZtMzQKJ5A0hfd2cj1PIAHdeeN0CBfb1nJvV6ClClDgT4vfUvEKcB7R3BvOn8EeE4Z0F4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
برگام‌این‌چه‌درخواست‌هایی بوده که بیرو داده!
‼️
علیرضا بیرانوند درخواست معافیت پزشکی داده و دو درخواست از کمیسون پزشکی داشته که اولیش این‌بوده‌گفته‌چون تتو زدم مشکل اعصاب و روان دارم دوم اینکه گفته در سال‌های گذشته رباط دستم بار ها پاره شد و با این دو دلیل…</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30180" target="_blank">📅 13:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30179">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ode7Ub9nXNI5Mx02ilGGnvU4VXOSTwDDNWPPfEDexDWCQ12mkYslbu_4Xgo7NhPWORQCEkyQdWIKyedHSxsXLTo28DyiEfvN20o4sVJO3evOIJcAn_4TlQPSuhSSuKB-fenZWDSziDVCOUcDL3od9NXmCXYGrxwLh8knFOHZ8CnNOCUqJk8dQ75RVhjTKU0RkCGoWZUCWFwzQYHQ8VGDwpeJ2xORyPNqs1i5E0GaVChk2YmkQXbczoBF7nc2seNUT2_BbwAR7k0VtPTyhJwB0AIX09_MlUZOZWR3TnE6YTBnrzwvjZotZl6VWQA-AwKjXnl_ENfrX7FZLrytJh9WAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
طبق شنیده‌های رسانه پرشیانا؛ سردار آزمون فوق‌ستاره‌خط‌حمله شباب الاهلی برای جام ملت های آسیا 2027 به تیم ملی ایران باز خواهد گشت. بازی های جام ملت های آسیا دی ماه برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30179" target="_blank">📅 12:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30178">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gc6cqfCXUtDlSqhksRmHEhzUBPON4cUytbb_kEsF0G-Qe3fh6i5KTUxvgR2U9Rgxcgfo3GnuFq9o0z0CScRrE5Rk07Dqr-A7_1ABWIIhC9Wj6e2PLYJNfZA0ulKUBnE8kWalv5xmgBS5_WQILtWd_6Gj049EWSa6cCs-oiB4pu_hg00dFYQpE9leoLLeCZ3VIvjl4dtx8C-JaReoYXcYeXGs3oYbRj07oFFU9621NRn_STt3tWAYhkw6Vx5I6TZJOUA75RSfirJpZIhgwyE0wnObEbShqk3qtMagGHj78FNsj_jtzXqQAjHJwd4JnVr8d2Fc_TVhggBtuLDxv-Zd7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا بیرانوند دروازه بان تراکتور در جدیدترین درخواست خود از سازمان نظام وظیفه خواسته کهه یک ماه سربازی‌اش به تعویق بندازند چون مریضه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30178" target="_blank">📅 12:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30177">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uV8k1SZSPq9H73a1JakClkVQ0BYYYncTn74uBMeCim7YwDROqg1prhDbqit6Xpepxqx-W24RPeLB6U5hYOoJW6ecgU_l44hTSUi-GCv95Wonqyx4OB5nptrwxMQnbGlH6MMFk9JU7dUEVYYX6k60P1JNSiTkBAaqGOHxKcRr_Zlatv6ppOwF9SqKGzpRW41FrfGDj9OKaV0WltH7DAdZnb5BNvH2RBNpwt1_U3Z_XXiT6GST3tngrseFc67oXec4D-U1LCSd7X63h1PvXp2KDblYZx2F0772UNe_q8pPtfv0wwwrT4udCUwmAOroMutrxrq-GGNKkuMGna6aUtsF4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
نمایی‌واضح‌تر از خطای‌شدیدی که باعث شد فده والورده حدود یک‌ماه دور از میادین باشه. تموم کارشناسان گفتن اینجا اتلتیکو مادرید باید دهه نفره میشد اما داورمسابقه بازیکن‌حریف رو اخراج نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30177" target="_blank">📅 12:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30176">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b904658a51.mp4?token=s3sN9ik5vTXLh137GOMCaygBHP4Qo21lnfZT7Bm1W45o-MlbCVfYwAFYJj1GTpGxJ0hNGsXAbvB1wS8OziXtEnzCcak_YueKtv_3a7YytZTkZkOrNLAplOA04unXrWJHX2APEW6QqV2z29rb7iMaJQ7iBTVjQ05IWrQndRJN4A96W-fvmRiVQ5Npsj-qNTehtfqWXn8hx3iGjCNtsQJfWc6OUemhrCFJ9LhkNrgXl4Z-waaRUlHIh_riZMYhgHu2_XQwf_94pC_0UhekqLlgUeyuzPpZ-d9ivkM5yf-i2LiIBpeDLK1d5N0LbnpCUjr0Dd9oLEXZoMRNQbpbFcq5Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b904658a51.mp4?token=s3sN9ik5vTXLh137GOMCaygBHP4Qo21lnfZT7Bm1W45o-MlbCVfYwAFYJj1GTpGxJ0hNGsXAbvB1wS8OziXtEnzCcak_YueKtv_3a7YytZTkZkOrNLAplOA04unXrWJHX2APEW6QqV2z29rb7iMaJQ7iBTVjQ05IWrQndRJN4A96W-fvmRiVQ5Npsj-qNTehtfqWXn8hx3iGjCNtsQJfWc6OUemhrCFJ9LhkNrgXl4Z-waaRUlHIh_riZMYhgHu2_XQwf_94pC_0UhekqLlgUeyuzPpZ-d9ivkM5yf-i2LiIBpeDLK1d5N0LbnpCUjr0Dd9oLEXZoMRNQbpbFcq5Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توصیه‌های‌محمدسیانکی‌گزارشگر بازیای فوتبال به شاگردان در مستطیل سبز که منجر به گلزنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30176" target="_blank">📅 12:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30174">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42e997aab4.mp4?token=cyH4Wnf8ZTrLDk7pHGo4vgCHsMF9ZwPFEaA9-vYvPjfvyJHiOqk6MX-l3SH82EoYe22un1_A20dWFYnOZ53Z2_VR1f1E9eTlgrTj1W1HZKoCeu02i9cVgUknMtvkyI761OFML0QjuMJZlg2Zup59yISffSwM8Zo9QNz7olHMyPheaSmkxlnsmbUHhHlki6nhuV_Q-QJOpw8Dl1SNm-2T8KPWUxd8behfCl-fQY6l_3m6E0ySHpP-PoMECd-Rbp1mKrb3twl4N2cJDgJvThknbFTSrVPHo_tL9HBIpVOSm1hTidASq03FhA48k-gNt2bAyMvRu-ANGRGdNrwOmYXj2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42e997aab4.mp4?token=cyH4Wnf8ZTrLDk7pHGo4vgCHsMF9ZwPFEaA9-vYvPjfvyJHiOqk6MX-l3SH82EoYe22un1_A20dWFYnOZ53Z2_VR1f1E9eTlgrTj1W1HZKoCeu02i9cVgUknMtvkyI761OFML0QjuMJZlg2Zup59yISffSwM8Zo9QNz7olHMyPheaSmkxlnsmbUHhHlki6nhuV_Q-QJOpw8Dl1SNm-2T8KPWUxd8behfCl-fQY6l_3m6E0ySHpP-PoMECd-Rbp1mKrb3twl4N2cJDgJvThknbFTSrVPHo_tL9HBIpVOSm1hTidASq03FhA48k-gNt2bAyMvRu-ANGRGdNrwOmYXj2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کل‌کل‌کردن دوستاره‌انگلیسی و آرژانتینی در بازی امشب رئال مادرید
🆚
اتلتیکو مادرید: جود بیلینگهام: تو لیگ قهرمانان اروپا داری رو من تکل میزنی؟ کوتی رومرو: تو جام جهانی داری با من حرف میزنی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/30174" target="_blank">📅 11:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30173">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TX05Yj96rvqxlpKg3K8o_pFzuzj29BC2K874g2ru_5tXADcK9Eg2ZfWc-wwo7IZiwZzzsyB-2T8uEjM75mTtfQdf54HdAym2JUpCBc_WHQ8LlePV30-RwPlEsKNPAEj7cXv4rlLSWwjZHQ1xw2jjM4hwU_jjuJUv8HC0sDfDnldeTKToio-tgrWkQXw1TpQ3lP6vapAA3I0TiEuLWxcD6hk0-RMiFhG5csLe2TTybr6MEDqlByIkaEDnxe3fO-V1L7naCd8Lv2bOxykSIjlzzXElQKoULTUVty7G2LzdOBaDRVEKn4Q9NzpEU67nfSNpJX94j8EvDKVy11k2fKmtDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینیYekBet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🫰
لذت بازی های کازینو با 100% هدیه خوش‌آمدگویی تا سقف 100 میلیون ریال
🎮
بیش از 5000 هزار بازی کازینو زنده و اسلات
💲
🤩
🤩
🤩
فریبت ویژه واریز با درگاه های کریپتو
⭐️
🤩
🤩
🤩
فریبت ورزشی برای واریزی‌های ووچر
💱
🤩
🤩
🤩
کشبک اسلات ماشین و کازینو زنده بدون سقف
🛎
گردونه شانس یک بت با هدایای نفیس
🪀
هر روز تا 180 فری اسپین (چرخش رایگان) در یک بت
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
r30
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30173" target="_blank">📅 11:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30172">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pl9gX_CBQPgQm-jJGE2GSld58eg201oU7Va3srpPpCPOELGmTvrJKtcEkvJXWXBaUXlGu2P6uUdh2fQdBTZsn2seCYJreYgxbejQfQOd8-VrPsbaVhhxJH2JBYR72AmvfwACbv0WURMgGNB6ZF_o9KpQCrlRnZALrULHE62hV_2xz4xtc9ey5kRXpa7fiRTa4NN5c_0H_v84zP6jSNQ3C00KnBvSVBYljDothP9G8gqyhiCurcXig0dq3kZjuT_S-GLneBDwzhlrjE0ZGAaT_o70XvARoC3ynuOVODUVcbsMXSeu12ruL6Wht9ana2ihMg574ppwNqCJmom0NibHCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
دو مسابقه استقلال-شمس‌آذر و تراکتور - فجر سپاسی شیراز در هفته یازدهم رقابت های لیگ برتر به دلیل بازی های آسیایی این دو تیم لغو خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30172" target="_blank">📅 11:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30171">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfnKW4JgQxiMmR9H12cWcYQ33B0X_t-omRK86RPKNz0tuQQhxXq3vZgIS4J3p8bl_UuzTHV28PSg4vT0ED_kII7gIqOu8Xazbs2YKTXF_yn68WHZHDngO1iM1okyZpruw4K3tNCJottabH1OyFG0qMjg6LllXZeJZ3BiQyQIAu7UdU427zilge1xO7uhHmVwa5UI5-6eBWw3MIltE_btzIc5RiIeoUuse86zNnz6SFMg8tkxjmA2nAFBjrO7kRcVnT2j8WMm5uDCTyAk6BMy2-7yreoRfEQwM8QTZg36fUSlnx13ktgrF05TcxBQBvf4qcGgVYkCgbR6mARetPYdyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت نهایی سه نوع آیفون 18 پرو، پرومکس و دائو اعلام شد؛ آیفون تاشو یک میلیاردتومان ناقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30171" target="_blank">📅 10:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30169">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iCe2ujkxNWfrv_tkOxsb-0FKW2O0tczyaPbJABgLenJL-gRSClGUqu8G6c7pD9Exr2vyXqm80kmNM-RheLoLxsilnTTM45_gZ8e_2ornWIHZuVb0S5MU9hpL7ngoOHDtQz0GYoWG72EfXoVjnjBf3txDP6itM5b0asIOT4GFNMqcON1nHZGgXe30nhid83df1Ki7ydXRCUPxAQYspA4sCUDo29bxfDaob7USfzWkbR4mSsekpmsWdsT_U6h-XG3LZZG0XJ0WcA96wrwdYfvybiyME32wef1TenZcPRz1p9bN8JOpWGeHrqSmSMFuXmfBsgNIcrMoHAPwxpUpyILvMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p-2m8YAG2wwOc2clum9yHjXn5Qil6NmBKpIUlsKt7rIbSTkQuXitmrd48Wjz7QPy1zPkzXcn0UxayUdA2UwNAsxHzS8KV2eC9kHQ-q6xLK2F5HFfOeehb4fjnN4EK7SiSq2_b2LiBS9JZW5wBQJDCzgRVVtuDsrJUIioYNwzlW9Y9YY-aNh7ZImLVF_z1RTmV_qFp8NvmmmN1vxX_BYLzxN5SqpraK6SYFeN-skQ9kcrTixI-4wjTsPpN1GM1KmnkJNuifyZZGQdKTsORTYX8EsS0IusdAlYunHa-DO8-Ihq7U07sGrEFuAm6ln8Ah0lTrRI_iRVjRVps8Lk6erd8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
برنامه دیدارهای آینده استقلال، پرسپولیس، تراکتور و سپاهان در تمام رقابتای لیگ و ACL.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30169" target="_blank">📅 10:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30168">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnhsLVAXHhA3QzpiocIboRs5AZ1K3n__tbB5SWuSdy1gmpY9k7AP2xj4M02q-r-wsZUO3EsOJCy25i0QIb2mUdkrg76E8nenywpNEwlJ5V3bU6PKfFJlx7DHYTzE1YEhHeLaiDe2Fvy1hHB4eNKRh-pS4KjVGEjRnkIU7kCK6j-SWb5MlmlEicZuwCO_ChgseqKj0ju36vkJH-j2UA2saSCF_0EYB6R2BNXBA7clm_er3mCZk7-xEnKzVErBulka7aDwR021A5i0_NwL9AkVKXn2FgwzZ4xoX--JTdr7KeaECU3BHG1SSWnSziDCqGwS7TNhKtONUPWsREYRUjYpPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اولی هوینس رئیس باشگاه بایرن‌مونیخ: فروش اولیسه به تیم‌رئال‌مادرید؟ ازخنده روده‌بر شدم! حتی امپراتور ژاپنم‌ بیاد پیش ما اولیسه رو بهش نمیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30168" target="_blank">📅 10:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30167">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015580725f.mp4?token=U8To5y52ETsrMMOAt8aYE7t9ffVa_yiFoshyx_j2kF0eeBCRFz8gZ0sJJD-DAKU-qfCaEhsksO95oQ5pJsDOwz_WQp-EOkmGe5Tly0cemWF6Sbpj58OzhfgdNsSc-RXXlME3s-hDBXI3lXEeeVaQ5eJgRx2P1kLF_CH1SMejF1YCLwlGhlQ4cn_NwcCarfwBim2LcCUt2ljYO7EXcEXrG2OdvatKa29GLRC_z9n3cXmp7vu1Ag-anZRrKHzEsL6NhW0XCLvmdfVRyYy0vVZbPPrytPDC2OLbopCPcy-jzCkk_FT1rP9rogzaatI2fKNCKFYnuPVaxYQNs-r0_WcvaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015580725f.mp4?token=U8To5y52ETsrMMOAt8aYE7t9ffVa_yiFoshyx_j2kF0eeBCRFz8gZ0sJJD-DAKU-qfCaEhsksO95oQ5pJsDOwz_WQp-EOkmGe5Tly0cemWF6Sbpj58OzhfgdNsSc-RXXlME3s-hDBXI3lXEeeVaQ5eJgRx2P1kLF_CH1SMejF1YCLwlGhlQ4cn_NwcCarfwBim2LcCUt2ljYO7EXcEXrG2OdvatKa29GLRC_z9n3cXmp7vu1Ag-anZRrKHzEsL6NhW0XCLvmdfVRyYy0vVZbPPrytPDC2OLbopCPcy-jzCkk_FT1rP9rogzaatI2fKNCKFYnuPVaxYQNs-r0_WcvaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
👤
گلزنی تماشایی لیونل مسی در بازی بامداد امروز اینتر میامی در لیگ MLS؛ این 930 امین گل لئو مسی در کل دوران حرفه‌ایش در فوتبال بود‌.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30167" target="_blank">📅 09:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30166">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkKFTYfmSONvkEMReRF7vXj7QR5tgu-HlpF0ua4HoZyUIJAaM2NSNy9meLptfMoiQDxBHj_fu-pRI47rIeaSFG4p6uvDoUNTnpUIGSmIAODkqw-qGTEqC3K8VxlxmskBnu_TwUQst5DFiy1CLYNFDp-UJGpiVj-K7o1zCcCvhqDl5PMI-7YhT5P0_fwElF7uFAHtGM1Y05LyJzkvrfpcI8QuE4ePglWFYrlf9JFXiVvgUojdff1_RUvWVnZ_UmHx65nSBycWgImvWGFXWQFYyLm_E-ThXBlXzdwAyfQn7ZxhFfPRqLhqOkMNj6iYGi1l-BRFdHledLU54xTcLJ0hRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛ میلانِ اموریم در دیداری خانگی با سه گل از سد تیم‌لچه گذشت. میلان با این برد یازده امتیازی‌شد و در رتبه پنجم جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30166" target="_blank">📅 09:22 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30165">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed8af73188.mp4?token=SnfH5eadpsZv-7jdCgXabSPBMOyWZ-vXTKv9eA00r8kqyjoyLeqPqDORLO1_LEkpnoNrFoWDRScNdeJHD5fBAGf4C1_ZzmYPvV3XfrmPQ0BwAsn6uc8dr4Iy8DOHMdaQj_5rwU6sIyJDCXQDGIxHuumpoqehHmBXWTNLqLIvzag6fnH01zsCwIYKl3BCPbJQ9IYXKc50l5EWcdP9WoNvS-KAeBpNgr0sWRnOIi2iUJPAbYSQb20h3Y-qvoNVOQwEajjqywCanZE1lDAHkCYubYfCFMK8ZDTYv95OGZc9W0GihWTfyifS6jc55t2oSrU2C-EvaUZx4JEyZq1B7LF-nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed8af73188.mp4?token=SnfH5eadpsZv-7jdCgXabSPBMOyWZ-vXTKv9eA00r8kqyjoyLeqPqDORLO1_LEkpnoNrFoWDRScNdeJHD5fBAGf4C1_ZzmYPvV3XfrmPQ0BwAsn6uc8dr4Iy8DOHMdaQj_5rwU6sIyJDCXQDGIxHuumpoqehHmBXWTNLqLIvzag6fnH01zsCwIYKl3BCPbJQ9IYXKc50l5EWcdP9WoNvS-KAeBpNgr0sWRnOIi2iUJPAbYSQb20h3Y-qvoNVOQwEajjqywCanZE1lDAHkCYubYfCFMK8ZDTYv95OGZc9W0GihWTfyifS6jc55t2oSrU2C-EvaUZx4JEyZq1B7LF-nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
مقایسه جذاب از عملکرد کریس رونالدو و لیونل مسی که ابر ستاره تاریخ در فوتبال اروپا رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30165" target="_blank">📅 09:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30164">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jg1ILyQyj56r5gdx1G3DRm9oPxn9MyO5B4VBGrrMM1pZxvpXKxocFqmINsACtBCTLBJAqslhf3sF6nNxOWdw6IGKlBJmeBzuiKZlUxCl6WYDvqJJ9Z5rWkVrUpW3RhtYDLHBkfLI4E9xV7JX5mW5BK7ay0J_N7uChSsHulrG90HR_hO-8RNMQpkM7PRpWf3gDN1LyIXV5KmpM_rQQ5RqEy3pDpEJMFtgDQVbp_2FTuDClP4xnWc3CBCGtS5w41K239SekUrzLuFKRQtvVcCCWLAvre-gZ5wzCnHPjRLTZamfdKsJm-OkPhX0ocu8v-ZHU4gUatDk9Uhxr_c8ghuG1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
پوریاپورعلی‌هافبک‌پرسپولیس درگفتگو با عادل: عروسی خواهر زادم بود ولی وقتی شما زنگ زدین دیگه قید حضور تو عروسی خواهر زاده‌ام رو زدم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/30164" target="_blank">📅 00:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30163">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fr8QW7F8GjjwhRU8yAvgGg7789al145zVjA59Kt3OABzwf4fxieXvROGRLOdH5aHmKbbxUhl8-dkb7bnpKCMkHWmSOCwIhj8_uk-Wid0-2nLUZ1P9jaODBi3CGjnMVg6hL0wFLzAEYuotPLLNnQnEXN6rZDbhfT9TRrmTBzwbA9eB12Un86Qg4l9XBUNIqZPHvhixIkw8Y-gB8jy2Xsm-rjJreb297CdwFrQO3Y2gEOgT6_q3ZTJtMGxisIu2JUaehqBActXp8y-UXbnEWB5rzsnwXeaC1S6JCqaweZ7tj-AQeSoJZETTfgOEkvL3TXqpM-YJMCRwh1P0qOC3OFn0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
الریاضیه‌عربستان:جدایی‌کریستیانو رونالدو از النصر در ژانویه قطعی شده. رونالدو قصد داره به فوتبال اروپا و لیگ جزیره برگرده مگر اینکه باشگاه الهلال پیشنهادی نجومی و سنگین به CR7 بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/30163" target="_blank">📅 00:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30161">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZztIBEml9MkNkl-Bced0SnWTpifFT3UNDMVMY9zK-1GkfXEPuIAZPBtPEKAF1yk4YEt0ffrlCF8hJV0hWzj5A2KrqIDBUnoVBNd9at4qt46AnpRWJLnyTpVBIG44qWAoBVJzWDnpPDrXZWQdHV6YliNFRSShhWIDSA6SZ8plVkp-96s4W4UIjhwKObm0wGeYAs8fpGsROX0oXga2xc2rpcR34fG68fA_E5iFciBpPbGEvzQMCjiHmtlKKsZJM26YfYhGS1r-LsN4lLaDu5LHLPp75pRuCSniXDm3xo71gZk6peLmN2eEl-gXONduE3AW4AvQCUKJbKeF2imjpQ1yrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها ‌‌‌‌‌‌‌دیدار مهم امروز
؛ جدال خانگی لیونل مسی و یارانش باسن‌دیگو پیش‌از آغازفیفادی و بازی‌های ملی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30161" target="_blank">📅 00:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30160">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLzDjHedSwnGRKrGcaKWmguyGMlZ9jGVbK12QzhVuHNeXrJ4V9Z652yx-V7TApaGR1LFaAM-AkXsAkXbmpKpGUh_0kft-ixVYVSpfgDe9P7GDSPAcSvQS6dTnhiiK4ODaIk4AOBbdR3poEOlFcKIE6oSqQ7AfdShmTFpKiw6w4K8M6gNzvlI71N65EAdgpXV2R85mP911g4CH-pmJz5sy70fj3uUAdbh3GBKjaFYc-BwyRm4vKyF_4uftFlZDf7nvcg3eVlpQ3-TN1JtF5L4DLMbGpRlSep35zBW-wOxD9mXHIzS1UXNcmdUIPHeS99YkBwtGyae2hNqOxYuz1jReQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
برتری‌بزرگ‌ال‌چولو در دربی مادرید و برد اقتصادی لیورپولی‌ها با تک‌گل ایساک!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30160" target="_blank">📅 00:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30158">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛ میلانِ اموریم در دیداری خانگی با سه گل از سد تیم‌لچه گذشت. میلان با این برد یازده امتیازی‌شد و در رتبه پنجم جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30158" target="_blank">📅 00:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30157">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba92349391.mp4?token=L4TX5j51Oo6-sA6-tN8X3e7k8b3YKlkSLN5u69LW0FnwxxTyTtCognzOe3oSRGwFG9nzBOcB3oYE_F5g0AqcINRVIRnOCoVt6UsAlsFnHYv2Kfqoz1i20y_28kOijLMSXRko3O7846HAcJtsjnrYFDx1e1WT_XRHgJNxdljpwxMM55VKGwpFkXybs1QTE2a4N6mOd-GqLBWieakw6C0jPf6sBbRYVwPuuakgmK--taavR1y2WJPpheH2nGJ9BGCKW_AU3gBmHsyZ2vUO-IhbgyImahJ1G-0kZWAlrjIBy-MGNmokWHuziJXYy0BnQPAnf_XtXAL9qA9qVgeGWPcGsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba92349391.mp4?token=L4TX5j51Oo6-sA6-tN8X3e7k8b3YKlkSLN5u69LW0FnwxxTyTtCognzOe3oSRGwFG9nzBOcB3oYE_F5g0AqcINRVIRnOCoVt6UsAlsFnHYv2Kfqoz1i20y_28kOijLMSXRko3O7846HAcJtsjnrYFDx1e1WT_XRHgJNxdljpwxMM55VKGwpFkXybs1QTE2a4N6mOd-GqLBWieakw6C0jPf6sBbRYVwPuuakgmK--taavR1y2WJPpheH2nGJ9BGCKW_AU3gBmHsyZ2vUO-IhbgyImahJ1G-0kZWAlrjIBy-MGNmokWHuziJXYy0BnQPAnf_XtXAL9qA9qVgeGWPcGsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛
میلانِ اموریم در دیداری خانگی با سه گل از سد تیم‌لچه گذشت. میلان با این برد یازده امتیازی‌شد و در رتبه پنجم جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30157" target="_blank">📅 00:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30156">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guGe2YULX6ae6fxlptbJLVSebWULLCUr5Xg7DVWMd14mExHNRQTZXcIqnpL5pfGCtb-XH1AU9uUkFqICL91fEeVrUDB4845_vjTCxEpTFuQ6MaQ23YmJmCHtAqlYZJ3-BeJMXenw8-azCjFxMlp-Na0jxCf0F2vg2Vgjg7pvILDbslYJwRnJ9LFdp9T8dECmxy6yQ9K2MZcgb7_z1MldionBMbfv4q35wpS0Db3dvYuFhntl4UGFrqt5U4jdJd0H8ZinvOVpq_AD7TcNb22ZXIxXyMKQ16fu20Wr8uNossoz81VvJpp5UwXDjdUTz7unp21MGj4o4we95Y7gKLkCvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇦🇷
کریستین رومرو با سران اتلتیکو مادرید برای عقد قراردادی چهار ساله با این باشگاه به توافق کامل رسید. رومرو در دوهفته‌گذشته پیشنهادات دو باشگاه آرسنال و بارسلونا رو رد کرده و گفته بود به سیمئونه قول داده بعد از جام‌جهانی‌راهی اتلتیکومادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30156" target="_blank">📅 23:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30154">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rfKEuCrKsCpfM4jAGmC0r9VxGr5CRXV3Kd1lNMTGWKWu43EQDI5sGoVaLuaFc2lcal3duOj0UriUNSfQ7TEusw_0e7NVsQ4PHjXen7YAm4FrPPmWyqnD0NkaZnoQKeBwtboVyCSJZ3exBeL9a-0IoQ_zQ5i3rLylsEzr9cjjdl0Kyi3ysAQq6zLiuGWG_tuBFK75Rfy72gqWAX2mo0HNQenWwL_MxZfqlwdvp7Ew5p0Z6MBgB3NTVU-MJp_RND7X-sTsQHXDqRO-uivlxYnt3iCb4j3oeLAMmOTHoQK_-rK8JgKxoStXn8XxUSYi9NBbILBWmwYGdjgsPO_b-nKZ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yh1PcRLr8jiiaEd0ZGKYCYkWEZxiNc4Wyp3fzy_J6fCS7CBCCEEGhhGWRIMcuSQRoEYzG3-widzAazsS1pQ671kWUghygBhGy40pM_oHwE4oMQE0CCBRINzf5t5UiRCbyPORKCsdCkoTeLmi0Yzv4diLCRPbME5u9Pl8QGMNTA0Z3qNuji-6V7EOALxBLmkgxMRBppcoiiawLjpPqOGwsNAroXkbVflLkAGkbQTpyBHDJP6W0_nLVdtXU-eAQXrQT_nIXwROcSy2-z3PYpJYDpBVSdKgf1TQUgUOul9xyDwt7z50NuF4EakNK7SwEK2aIu_3F2SQXcIHQmZ2xXzkxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
عملکرد رافینیا و یامال درفصل جاری همراه با عملکرد کلی رافینیا در بارسا؛ بازیکنیکه بعد از ژاوی داشتن میفروختنس فلیک احیاش کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30154" target="_blank">📅 23:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30153">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddfRrxek6ptFWjmCT8iRkXHC2ZtHFqAXhtkhF5YPCC2jreZJ1G3Ms8aN0m1pVzVCdG-9dKy-XrKcpEF5-5llAHpR6a--VdJ2ul7zbg8bwEu-Iw6qQSAYhVQ8o9JIfXGTjuSZSKnV6Q7_na65Ec5G16ApsXogOJU15cIwUdniJQHymP5PorRhYn80O1qRyspfchrIaL2UCkZRCs8eGA3nrGgX7n78gcRMkSKmN7cNha-2gXDMinRueb8_ejC6L6yWz-B0aPQ2oAUe0x_dGnn23p-ORud2Hp0SRPgIkyGYg4j2NA7O2Q-F_KzsEhs0hL_ysaIo9eG8S5yRCCv6_J5cmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
مصاحبه‌‌شدیدالحن خوزه مورینیو علیه داور بازی امروز مقابل اتلتیکو مادرید که از نگاه سرمربی پرتغالی رئال‌مادریدعامل‌اصلی شکست تیمش بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30153" target="_blank">📅 23:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30152">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYrsxJ0b63W-8nvBRV0Pn-Q0MvrkmMpCeAS2VPu7d_yFLchtMTU5PrK1aDVB6iwtzgUK3xTqe-VunkA7jH2_f3-ds9DW51ojcm9b0tWYszVvG5eNn3mRs_A488a8k8F70IE1iscS2zCRagQrhV3eZX0jEaVmGgk3nUNfFEa8CqRrVRKbru7ukjSEVp8aSnN9YcYNajB_Qok9a3JLOp_nbxE3xnZq36txce1CVUJnbMtAM024KHIJpA3Vww11oPboiJFlRVIjmHEhX4Fy_c0g4oekHfhjFiOGz3FByvzFNruEtf7l8wAy8LILi7SzAhMQ1wRDLBnxWoL2D6fqVfTDLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
به بهانه آغاز فصل جدید رقابتهای لیگ نخبگان آسیا
؛ نگاهی‌بندازیم‌به‌تموم‌قهرمانان و نایب قهرمانان باشگاه های ایرانی در رقابتهای لیگ قهرمانان آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/30152" target="_blank">📅 23:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30151">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇮🇷
👤
طبق‌شنیده‌های رسانه پرشیانا؛ کادر فنی تیم ملی با اللهیار صیادمنش برای حضور در جمع شاگردان امیرقلعه‌نویی برای مسابقات جام ملت‌های آسیا تماس گرفته و این ستاره 24 ساله که عملکرد درخشانی در اروپا داشته احتمالا به تیم ملی دعوت خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/30151" target="_blank">📅 22:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30150">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3bsIOgqxI9SQ1aQmJf62PdZshOL0qYNqzx5VG9tvQ94oylma6JMH78SzqJgh1IUyD19KXQVTTzfFw8NzY0qBdE_n6fzOToz4jw0xInfeRy-KjTd_7L9ziuheF728sOAMgwv7IfqHYpJ5m0l3uZWt3gmhPheUeROi0bUMNtfEUirltDT0l9FEeYANMcAB85HpJ-lkH6U_Yg9XfIHC_lCZFO-B9Iwl1ORGv4zNNvVQ7av8EMLjkDXgyecrkCnR5jXoLuzM4wD4F-IPy7Qd2seVpLRjHKIT4skTg-mn_II4rmqhUWzxzvqhqPOK6fHbcAvGuYZfZZnl4gNfOquxYNp1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبرنگار رسمی باشگاه فنرباغچه: بزرگ‌ ترین آرزویم این‌است که کریس رونالدو قبل از خداحافظی از دنیای فوتبال یک فصل برای فنرباغچه بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30150" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30149">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rG2LeKjnGJhpwuLIBEJD0gn87XiU5b245qpSl3YaC75O-_4lU2CaBxUae3160SCVTpX_-MbNryxFZwhZUoRZ6UNAeFjxtXLzHExpjymgUwYm6hETVVylx6dH5c43LznRJ_70rheQ__jU8oQYSQzm9-ilYXnP2EX-3tfDUXC9WE9Dvea6d-5TELVhl0QFKmXnnf2-dkWJhWJFniJY0Au2rUgf0i215x9-tYdFj1_6oAIhixwnNNidmYrlG5aeoP3TXksldz_S8WARBs7fvSmN3ZX93c3l6zVpG4iZoDnQ8qAbGbmmQc4BUubIdkAA6h8eEPHnczXfKpH8H23jpaFFHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فده وارده کاپیتان‌رئال‌مادرید به دلیل مصدومیت 3 هفته دور از میادین خواهدبود و احتمال داره دیدار الکلاسیکو که سه آبان برگزار میشه از دست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30149" target="_blank">📅 21:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30147">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⚽️
⚪️
شبکه رسمی رئال مادرید به شدت از عملکرد داوری دیدار امشب با اتلتیکو مادرید شاکیه و گفته سران‌باشگاه دارن برسی میکنن که لیگ کنار بکشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30147" target="_blank">📅 21:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30146">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u93KEXoAj0wiEu_CuVzpgDDla1hbGEwnRHoWV7SuxmBDHvIOq3QxEaXwzIwLrLd50OXM-nDtAlgt-5sa_Nq32bCnGdKyqkh7zZPJjVQJKo2oOkiYd3OCKuorecTQQWUhmrWbGsm2gOYkvQWDK13fdv9ZwDKXzprllTv048E1rASfQ6vPYstYAjBmkpiNNSmn-nCuqkJCqSARkIJe7bT9-rZC9BEhAkqpXP-n3JBWrfual-au71KrU8TQ_ZG_01GauGXZEgtM3if7ud5MvFUfLjPeZitK6Cd-gzNRHVrUkV3_BIhtVwdIoqIB_RObGc2PEMmtXBwqwAFJIMz43X3Itw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
آندریاس کریستنسن مدافع‌میانی‌بارسا به دلیل مصدومیت دربازی‌شب‌گذشته مقابل سویا، شش هفته دور از میادین‌خواهدبود و به احتمال فردا دیدار سوم آبان مقابل رئال مادرید رو از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30146" target="_blank">📅 21:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30145">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/584eeae99a.mp4?token=aaAn6iO77BmfaVKChCQW8anXQ7zSeeyeBBei995o4NqiDsf_LYIJ2rBGebefiVG0iSuTBxr1loZAoSGXmiewufFU0j0OPvI4yUUuR-sOlM3nVWEYTzdzUxqYgp_IA_sU_3sa9nxRwG3yDc8oBhZGzWBsMT2DSdMZ3dhXs0gvJBurNC4UpYfYDSXf_BSY-MAYXwr-nbB82sF9VEfWdiDbMYx1MwAFjEo41cJ3SGhFdPppoJK33l53pXkfE5nZxA8Ovlg2lhyYimBE0XVXxRk4F_n4nzHJquOdNcdbr-05xVTgbITRzECcSdrmITsxg0QPsIfSQoB24bJczHtb8vWnfC_JHIWasox3sQ9rA17Dl4Lo3YUBCgN_Ni6sKo0z2Urfr1ZWFOV69sVnJxEppCcvZpeMUoE768uaCPuAtj4LKystPI28QTX9smEU340HENz5IMnphHo_UWzSP908QbzpM2WiX7MSPzsthZBUhZXgdD0rE0oDVGk2JstYt5PCkY37GIiIWyOBm11AvocjNMiP3ekESs8Vsq44VV6ociSve3GDzUMvyg3wBfpPks4zzGYUN10sajdk4DlPAUQyhav8W4W9jZrA5Pyi4tAm-ltcpouiVroAH199ARM8TbqUCDUbGoU21oL9T_0fUSXSWmI2rHUcmJLDKUDlVOn0KRdDdOo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/584eeae99a.mp4?token=aaAn6iO77BmfaVKChCQW8anXQ7zSeeyeBBei995o4NqiDsf_LYIJ2rBGebefiVG0iSuTBxr1loZAoSGXmiewufFU0j0OPvI4yUUuR-sOlM3nVWEYTzdzUxqYgp_IA_sU_3sa9nxRwG3yDc8oBhZGzWBsMT2DSdMZ3dhXs0gvJBurNC4UpYfYDSXf_BSY-MAYXwr-nbB82sF9VEfWdiDbMYx1MwAFjEo41cJ3SGhFdPppoJK33l53pXkfE5nZxA8Ovlg2lhyYimBE0XVXxRk4F_n4nzHJquOdNcdbr-05xVTgbITRzECcSdrmITsxg0QPsIfSQoB24bJczHtb8vWnfC_JHIWasox3sQ9rA17Dl4Lo3YUBCgN_Ni6sKo0z2Urfr1ZWFOV69sVnJxEppCcvZpeMUoE768uaCPuAtj4LKystPI28QTX9smEU340HENz5IMnphHo_UWzSP908QbzpM2WiX7MSPzsthZBUhZXgdD0rE0oDVGk2JstYt5PCkY37GIiIWyOBm11AvocjNMiP3ekESs8Vsq44VV6ociSve3GDzUMvyg3wBfpPks4zzGYUN10sajdk4DlPAUQyhav8W4W9jZrA5Pyi4tAm-ltcpouiVroAH199ARM8TbqUCDUbGoU21oL9T_0fUSXSWmI2rHUcmJLDKUDlVOn0KRdDdOo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نامزدجایزه‌پوشکاش سال؛ ضربه قیچی برگردان فوق‌‌العاده و تماشایی‌از میگل بورخا، مهاجم تیم کلاب آمریکا مقابل تیم گوادالاخارا؛ چی زد!!!! حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30145" target="_blank">📅 20:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30144">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b82b6c09bf.mp4?token=TP22AM7SGwtOYZhOZ6dS7SviOULb3jVpl-YI8efFBxS3Xzh-Y5t857ZoWkmYZLM5jdHXZ80g0rHsywco1Ua7JAcymgU1wuAd6K9YBYg8b8eTwWgome3rgDgBVi6ea6eDFBjagB8rX8DrVLV1v0l5m0A2dArcOE3pbXYV8zu9TCfA6icy5XukgDEC-HMgYirB8gvfC21zdqEgBIIsTdCxrCqn9eun2AqTGyEddRbw8vb-y0PSsRB_Z9fJ91e9G0uj45Z2dkNjIWAae7N5CiYEZLcbGqcaCa4OeVqYli4FB2LEQBDIz_0TTEcFqsl-aczckp5GCW8V_N1ZpeJ2Tg_awg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b82b6c09bf.mp4?token=TP22AM7SGwtOYZhOZ6dS7SviOULb3jVpl-YI8efFBxS3Xzh-Y5t857ZoWkmYZLM5jdHXZ80g0rHsywco1Ua7JAcymgU1wuAd6K9YBYg8b8eTwWgome3rgDgBVi6ea6eDFBjagB8rX8DrVLV1v0l5m0A2dArcOE3pbXYV8zu9TCfA6icy5XukgDEC-HMgYirB8gvfC21zdqEgBIIsTdCxrCqn9eun2AqTGyEddRbw8vb-y0PSsRB_Z9fJ91e9G0uj45Z2dkNjIWAae7N5CiYEZLcbGqcaCa4OeVqYli4FB2LEQBDIz_0TTEcFqsl-aczckp5GCW8V_N1ZpeJ2Tg_awg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نامزدجایزه‌پوشکاش سال؛
ضربه قیچی برگردان فوق‌‌العاده و تماشایی‌از میگل بورخا، مهاجم تیم کلاب آمریکا مقابل تیم گوادالاخارا؛ چی زد!!!! حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30144" target="_blank">📅 20:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30143">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2be5ebfb1.mp4?token=YAnElo7zGA0lYu90kAHUfZhF3T-bUXeNdD0ZpKPhT2dT_Ib-FYujcz7KX9_I2iJJLV8ZO_u0WdKrIuFBSlNgq4lbIPq57_wP89sMs6w7JWUndy1RffE1nxZndd30ypTcJsy26dzQs1Yroy47O6sII7P297yLFduZvuO1vctOAFoAuIcFrt0ht7hnxTxb8W7qZyNFSDw63VBHwAbt5Y8T37It2nbzrDYqd5V3vSvRhqR3uP6U1kBrYc7HxnksrgebBDMH91FucEMH4jEj61tGG4ahGUMJQoyhd_0hzRNYeenU3Oxe5rk8nHgBt4A-r8jpB3mFNvbGBaAX2CFF9g0ROQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2be5ebfb1.mp4?token=YAnElo7zGA0lYu90kAHUfZhF3T-bUXeNdD0ZpKPhT2dT_Ib-FYujcz7KX9_I2iJJLV8ZO_u0WdKrIuFBSlNgq4lbIPq57_wP89sMs6w7JWUndy1RffE1nxZndd30ypTcJsy26dzQs1Yroy47O6sII7P297yLFduZvuO1vctOAFoAuIcFrt0ht7hnxTxb8W7qZyNFSDw63VBHwAbt5Y8T37It2nbzrDYqd5V3vSvRhqR3uP6U1kBrYc7HxnksrgebBDMH91FucEMH4jEj61tGG4ahGUMJQoyhd_0hzRNYeenU3Oxe5rk8nHgBt4A-r8jpB3mFNvbGBaAX2CFF9g0ROQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته هفتم لالیگا|دومین شکست فصل شاگردان آقای خاص این‌بارمقابل اتلتیکو مادرید؛ اختلاف رئال مادرید باصدرجدول به شش‌امتیاز رسید. بارسا مدل هانسی فلیک قهرمان زود هنگام این فصل؟!
🔴
اتلتیکو مادرید
2️⃣
-
1️⃣
رئال مادرید
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30143" target="_blank">📅 20:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30142">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0de9fsJD2lvMK1Q_9SK6CW7dHaJap_bvOVvo0sqbIh1yKPBGBkgAVUe6yDxTcbfNWv7hFqto9pfJpzqsZqoSWypSgIMvQSbDZWh2KquP1C81z18b-cg2UlAXHbIcDECpLlk4Gh3Q-3Qe5bbjl3YEaEw3LQdpUzTj5ZzpLRYjo-QHtXGryDhFpteDnfzRhxkPkl-fKQeOALvxZU6UBysqclsNkZs3laetA5j4mVNjeaGScxESlJMQi7AkXe_MOZX0tRa-VUV9isJZp8FisT2A-278_AHNRLskXDpNPavu6Y1PGT8G0jssDwH1D_tW24B7JsdMBepnC7xr6gPV2QimA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هفتم لالیگا|دومین شکست فصل شاگردان آقای خاص این‌بارمقابل اتلتیکو مادرید؛ اختلاف رئال مادرید باصدرجدول به شش‌امتیاز رسید. بارسا مدل هانسی فلیک قهرمان زود هنگام این فصل؟!
🔴
اتلتیکو مادرید
2️⃣
-
1️⃣
رئال مادرید
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30142" target="_blank">📅 19:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30141">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrnuJ9MlXtbB2x4JHzaOxa7CCt3ZxASU-bmhHYXnBFKHdribx-h0gyNPBdbEeFt07eRH50uJmvqTFLu2x0YrxcS-Mm26OIB-yAmyupjEDXShMycDTA9FlOMyDHGaWvBv8pLrWZu8A0y3jLOe_lgzuyRR7NWehJ1gBg_PCeAFVztT0ueSR1Mq6BSGFaTR0qRQIIgDh5CjcTjfH9SOztlueUJXdaGEcp9yXohXWShypLWKrykH_uKX98tVDhVp585kpClxtw_QbLggrRJ4TEnMRPxoB8uh1_bAxL-J6RQLxKnKadirw5UaBrVI4xFDXmRG_NkAXB_0kw7D527URq_jxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|شماتیک ترکیب دوتیم رئال مادرید
🆚
اتلتیکو؛ ساعت 17:45 از پرشیانا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30141" target="_blank">📅 19:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30140">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVJH68Mo0lSeTkx7IVxdoETNiTbruk3CqdLRYLj3KL58lQCW7Yii7UucnkDhcSeaZtZL503jzudIWhQrwW6-bledQALIxETsbZJccTFsMnvnsWEMBBRWs0vBdC9hJJXt5QGGtstVgdbtu30rUf0aTwgRPIqUy6pHc0I0momdm1S5-SkiQWmAzvSx7jHk7O8HiwtaLFmrWdTfwxxrMgEFdyzHfFp8n45-6x91hhL4wkbHjPc42oF2HsapjYMI-IorUkpxLAOOZrZrGmOu0rIV89uHI1qpeDIUnyfz4ZSTQGrylmb_aEp-dFMyjGG_IWK4qVDqrVev-Es3qMJQz98Xtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه کاشیوا ریسول درروزهای اخیر پیشنهادی دو ساله به ارزش 4.5 میلیون دلار به یاسر آسانی ستاره‌آلبانیایی‌استقلال داده بود که این بازیکن بعد از مشورت با مدیر برنامه‌ های خود این آفر رو رد کرده و آمادگی کامل خود را برای تمدید قراردادش با باشگاه استقلال…</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30140" target="_blank">📅 19:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30139">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43f4a8d8c8.mp4?token=GKbvNiWzO9OJXVoTIURTo6Hy1v490WSV2uM6oDFEKeoKsAgyAQr5_o8-Yt3ybBoalPAx8d_p6UJTfTAII9aRTWrhXhrC6Re2DzibVxDrfknFF4BKmz99exXbZrMNbSUiMmw3SIHVWq06OcKtvosmXpj4RtolVBIiPSxm-8Z_MtQ8kxfBcahhIoCb823LfUOHAY0eShWDcen4JzoZG7FlIUNc4aIKDidgInByAAB8ds1a3pPfY332PdOaZPrvDY38rbgQlHj4rT_slRxtdAYlEzOQkZHkVwDC-7ar8NInuKySJww07WoNTRc2TYHerQjAxJz0eFCNrG395K8ifeJ_Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43f4a8d8c8.mp4?token=GKbvNiWzO9OJXVoTIURTo6Hy1v490WSV2uM6oDFEKeoKsAgyAQr5_o8-Yt3ybBoalPAx8d_p6UJTfTAII9aRTWrhXhrC6Re2DzibVxDrfknFF4BKmz99exXbZrMNbSUiMmw3SIHVWq06OcKtvosmXpj4RtolVBIiPSxm-8Z_MtQ8kxfBcahhIoCb823LfUOHAY0eShWDcen4JzoZG7FlIUNc4aIKDidgInByAAB8ds1a3pPfY332PdOaZPrvDY38rbgQlHj4rT_slRxtdAYlEzOQkZHkVwDC-7ar8NInuKySJww07WoNTRc2TYHerQjAxJz0eFCNrG395K8ifeJ_Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاطرات سمی امیرحسین قیاسی از مصاحبه با علیرضابیرانوند و جواد خیابانی؛ بدترین مصاحبه کل عمرم رو با علیرضا بیرانوند گلر تیم ملی داشتم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30139" target="_blank">📅 19:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30137">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPWYsJmKmkje1e-J40G9cgemkPmawEsPbdmcNsLj9U-2RTVWwPUeUCfvNK1THETEmu2DK2SNHo4Iaa3MiBZz_yOaw_YU15pTOxfx7zka80jfpWVBH7g9LWABqro2dCebQQ8MuDVj3zm2r_LHs8FgTkBXOhJ4WA1oo7g3ZDi1xMVtwRYSoFzqdeQwol1Egd5PKYUlsV6ATeprIoXotvjunwE7hSp_hBsNX9XQP35mGebZ-PXSbpG_yL3T0BLnSwEQ2tUX7wwFATBAY4lKyrJcdothgJ2wtd-ZRhvSTGOCI_LlEIvKqnw8zTiFwEydOBLsvnsIvb9pGdFxqlRg_M2Kkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|پیروزی شیرین شاگردان هانسی فلیک درشب درخشش خیره‌کننده غایب بزرگ لیست توپ طلا؛ رافینیا دیاز یه تنه با هتریک‌اش سه امتیاز مهم بازی رو برای آبی اناری‌ها به ارمغان آورد؛ هفت مسابقه، 21 امتیاز، 31 گل زده در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30137" target="_blank">📅 19:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30136">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTCK7bnBJ7QfKfKBEnmBg481dp1NVDi19q1o6eyI_L7sO7n8dcNwcdVQzyeUTke-NqC4iz2mbYB5l16wX-5QPJ12-6_7ySFsG4vyj3hPCrwXkTjt5v43c5oQlmP24BWSeG9-nKiU3rD9h3xulpT7bSn90wpcLZH4h873Kd3fn8eoHfBlKvR8amPGkE8yFjbYYkB3r451drt5apLey63_Ah1IpgMskkBDGZMpHwxKh-oD1cBBoJZMvhpKDNXUerm98PWqdj7ODJL7pDrkfa_GwqBxU24jorkhOZBC_79a_xzjZa0lC3Q8dpkVztuCv3IKiQlYRcGoMHEFRaY_QGbBeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌ های رسانه پرشیانا از نزدیکان اوستون اورونوف؛ برخلاف ادعای رسانه‌ های ازبکی باشگاه تراکتور تبریز هیچ گونه مذاکره‌ای با اوستون اورونوف ستاره‌ازبکستانی‌سرخپوشان نداشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30136" target="_blank">📅 19:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30134">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eb0177e91.mp4?token=e2Wkk0ZRO2NtwxRD9734_QN5KUS_GsK70_Ou4190qwB0pC3YR2ULvr_AZw68u8hN5SivAiPzcCuYkYk2VSMWyUXAsNIMyI5n2JmKBA89-5AnoexNnShdpY5LuHpiV-u8eel1UOrX-jTqx4xJ-EldNG7HDnNpLSTDccghRgnlsP7UMPgSEXYyyd0ht9gQTwhnIgXVeQpBkaf2Hag2sGJxCi1edibjJtS6II4WszVm_31mdbnnSg17YVl_nA6fKhmHIw-aA4Qzw1p-_kaGtagX3V5uPOewuDcf7Lxy4Ws_zXq5I4YyGBq2D9CodQbvTfr8XX0DDlDMUrLQYYdCMETs6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eb0177e91.mp4?token=e2Wkk0ZRO2NtwxRD9734_QN5KUS_GsK70_Ou4190qwB0pC3YR2ULvr_AZw68u8hN5SivAiPzcCuYkYk2VSMWyUXAsNIMyI5n2JmKBA89-5AnoexNnShdpY5LuHpiV-u8eel1UOrX-jTqx4xJ-EldNG7HDnNpLSTDccghRgnlsP7UMPgSEXYyyd0ht9gQTwhnIgXVeQpBkaf2Hag2sGJxCi1edibjJtS6II4WszVm_31mdbnnSg17YVl_nA6fKhmHIw-aA4Qzw1p-_kaGtagX3V5uPOewuDcf7Lxy4Ws_zXq5I4YyGBq2D9CodQbvTfr8XX0DDlDMUrLQYYdCMETs6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌جزیره؛
پیروزی خفیف لک لک‌ ها در دیداری خارج از خانه و آتش بازی تماشایی سیتیزن ها در اتحاد با درخشش انزو فرناندز. گل‌های این دو مسابقه رو حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30134" target="_blank">📅 18:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30133">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocvO4Ottxhx6rYvzxhgcgOy_QoxmJJMl9kHPOKc79QSAT5LtGE-rghxVcTqF9ftkqYhrUZ05ntr0eIUEkqDtOfg2C5oA_WWp4ehC4PiJAPY9MPCE2wFtn-pw-oCI7sY_WKro8tfolzzcv4vEQMJxH041XaXu6IexvoJjuLPyuYN6_vG8TffCGDntgvh8DKe4uqLUsqD-N2eTk6I74TAgDuzMX4hPPWynyNwkyR3wsib4PGeCOmTp9uVG7LQ7fhe1ffPnSmdpMvz2U7Pz7_5zxMGtsa9hKBwX-IdozdRfnLQIHL1Ovvip8xpnGgo97a7xmO5X-43gYOG1WFS_rAbStA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رفتاریکه‌مایکل‌اولیسه بااونیکی خبرنگاره داشت این بنده خدا هم ترسید اولیسه اومد تو میسکدزون ازش پرسید گفت اجازه میدی که بغلت کنم؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30133" target="_blank">📅 18:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30132">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyIxWVsuIg-7mm2LAOWWGshV6amQCgGyo1m_0iJA8q7vP1j854UPX_YhCNGNIgCq766080gfQ865FxT1x-CviMSCW1kL4jqb0VbGoGvhdC74-A0g4i0IKObTELhsFDACCJ-EkjsxF8MF6nTQo57y1d2Tl_ui-mIrzi6E0We2aMh8-om3RCoa0NI9hInJv28CKX_maQO3_paMdCF7zmUU-BgOTsN3EAhOar0mm-h3hhCGwBkQJO0WUXnmv_CYwtGcF6QdCbNm3MY1_uSDF93zHdcgczj9Yo_AiWNkH_F4D9hJBo8zL6p28-NqIDN5eEoUJ4SeeLDYnCe4h7anm7y8QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
پارتنر لامین‌یامال:همه‌شواهدنشان میدهد که یامال شایسته‌ترین‌بازیکن‌برای گرفتن توپ طلا 2026 هست. اگه عدالت برقرار باشد یامال برنده توپ طلا خواهد شد او اسپانیا رو قهرمان جام جهانی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30132" target="_blank">📅 17:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30130">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d3be7a360.mp4?token=q6jQEkltZio6ZXLznB9zJFLGxKOHdyX2rlWGP5L_U6XMQMK91eFGsa3I6-PvADzRtPlKUDjvJEPATR0AyDiw7RHQybDQbwDncdR79_n3b7JrUn6UOuet_FGW3P8x1pwfSsgRSqpxe1Zb1Lpk9bFL-hTqt3qymluVUbdJ8JCTtJzjWZm0jBI4a7jz9htA_ntPq3eTYCVdOSkaOG35AQuxa8E4XLRGrYjbxDrTK6Jov_1s80elJ4VfToMRK7V2JDrTsd2KgS4lORAqazS9TfwCy3nxi7dPGfOjH7Gg8xkYHEgSLBTyut9neINAmN-JM3cYY74Okbk7dl8SIpRYxK4A8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d3be7a360.mp4?token=q6jQEkltZio6ZXLznB9zJFLGxKOHdyX2rlWGP5L_U6XMQMK91eFGsa3I6-PvADzRtPlKUDjvJEPATR0AyDiw7RHQybDQbwDncdR79_n3b7JrUn6UOuet_FGW3P8x1pwfSsgRSqpxe1Zb1Lpk9bFL-hTqt3qymluVUbdJ8JCTtJzjWZm0jBI4a7jz9htA_ntPq3eTYCVdOSkaOG35AQuxa8E4XLRGrYjbxDrTK6Jov_1s80elJ4VfToMRK7V2JDrTsd2KgS4lORAqazS9TfwCy3nxi7dPGfOjH7Gg8xkYHEgSLBTyut9neINAmN-JM3cYY74Okbk7dl8SIpRYxK4A8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌ از مصاحبه‌ تاریخی‌وفوق‌العاده گزارش گر صداوسیما با یه‌کشاورز؛ خیلی خوبه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30130" target="_blank">📅 17:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30129">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37c2e1f8d1.mp4?token=pyevhrNZkHNN9ApjN0QxiU83h17vAao1h9_XyS5feQ-uUgvpo4qXDcwFaeqEsibjyAK93WIcglWMTbNU1eNbTnFKyba9fuv35Vl0BbCRo6nNm2z7S7U1ior6N3lzAvFmoO_oQ7b6jwwtA2Cvy0n7jvnJ_g5AaS4ELrcm1W40yTVMAUm6CzYBuNxpcsJ7XPrTXdC9a6Vnne_eXCIk-aGriKanPyhAi7qsQCtuq9K6r_qZW4K1a0eUqwTW_Axr_ns5L60-hZvf_FOMyBotOt7pSGJv_7-niJtYC7SBam5rxBCa2EinNewIv9mCnpRmqaFUSljk3eDJPUAt6UqQI7Y54w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37c2e1f8d1.mp4?token=pyevhrNZkHNN9ApjN0QxiU83h17vAao1h9_XyS5feQ-uUgvpo4qXDcwFaeqEsibjyAK93WIcglWMTbNU1eNbTnFKyba9fuv35Vl0BbCRo6nNm2z7S7U1ior6N3lzAvFmoO_oQ7b6jwwtA2Cvy0n7jvnJ_g5AaS4ELrcm1W40yTVMAUm6CzYBuNxpcsJ7XPrTXdC9a6Vnne_eXCIk-aGriKanPyhAi7qsQCtuq9K6r_qZW4K1a0eUqwTW_Axr_ns5L60-hZvf_FOMyBotOt7pSGJv_7-niJtYC7SBam5rxBCa2EinNewIv9mCnpRmqaFUSljk3eDJPUAt6UqQI7Y54w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توصیه مهم مهدوی‌کیا اسطوره فوتبال ایران به والدین درباره زبان‌انگلیسی؛ حسرتی که مسیم دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30129" target="_blank">📅 16:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30127">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cYdQb-XnXw7I4zps-fR_Wd9Rkqu7vv1Cg2G4IhZM_TEaSrXM714pFAhVbP5Y7Ss6HPneQCh4z_bR5K8YdlhXCVg842N3tI8X2IHJEB0cNv1BaNmnVu7qcstGr6lFymuRuqU70L2J95AbRRZGEoNI6e1tM_paaCgAWNSplrY0yW194SXP4VdaPwl2w0J4gVgbNV6taGChdJrny7tzauD9IDEUsN5gtcG1L-t_BFnm4fsxezz_itEkSj7BWkdMG4XGzx2l3LxI8zOSIWSt-UMOLmFZ5jtgfmFpdzaA3jMS3hp2KpPiGFh62hoFPYHsQ8X1BfNnMOZU4OPxerWYR5LbJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j8FJwBgrNgZhKq4UM8OrTMcAMnGQiNHS0y3vYTDQZq99bZfgFL7BC2-Ees0HkYIcl6b1TUwl5owXDhxJwiwzxPH11D3lYuGXUlE5_gPdH47DLVmBtxX2SwCtF3HTPaK_AqT99e0JtNX7LP7svqTw8Xj6YUyOYsoGJruI0JTh1v3Hm1qSQo-6VskS1YpJLFHlZwQ9P5BvEoLtEPnO3ETbpfHIYgp8rDXXUdC8OAEzd_lpDECrKaLAsStCMvWY3FUip-XgRn23i7JvfQqIgcTq87N6BdgJfNkS8DSCr_ORbPLemWMOU4Vos8E_8Sud_I69XDAtvOokTJjTgcA5nN7RhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
آمار تقابل‌های لالیگایی اتلتیکو
🆚
رئال‌مادرید؛ کریستیانو رونالدو بهترین‌گلزن دربی؛ 22 گل؛ اتلتیکو در 10 دربی‌اخیر خانگی تنها 1 شکست داشته؛ 5 برد و 4 تساوی. مورینیو دربرابراتلتیکو:11 بازی و هشت پیروزی. سیمئونه در برابر رئال: 50 بازی و 14 برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30127" target="_blank">📅 16:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30126">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQg7MSpK1bFMiD8RPvzs1xLzHXTO0gGA9wqeqkajUIQtXE59qdwbhc3Gd9GIOXJnabSomr7Uou0SFiYfNHwxRMwsVnnxp-WTtBREs4eKlWSq_ZlNdclaTNtDxFEXMpI3AruIRli7jCMNvVwe_JI2PbyXgszS3Ibx6NeWrEh22PSjfhyRl5N206d0gjPxauTMVjCN643h3UIE-zhALLHDREal8S6kSeROr9sRhubHEoKcQ2ieK4Xf4TYQAZlMUaJWD8JPuN9Wr5fgPe2gUL9F4-l-9NBm_pDopS1mdAxsfohbVkIZ-NcGn---L8k-D4Mr6xp-2c3fxxMcq4bB0nBIpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های لالیگایی اتلتیکو
🆚
رئال‌مادرید؛ کریستیانو رونالدو بهترین‌گلزن دربی؛ 22 گل؛ اتلتیکو در 10 دربی‌اخیر خانگی تنها 1 شکست داشته؛ 5 برد و 4 تساوی. مورینیو دربرابراتلتیکو:11 بازی و هشت پیروزی. سیمئونه در برابر رئال: 50 بازی و 14 برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30126" target="_blank">📅 16:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30125">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLOCO-CG5Tlw0jH9Bo4gYVfoAzk7Em1Y22lowINQd1qcpMAWrFiu1fHQF2H7J3JnKy4xoa2oJw9Rs0wEe3vqWAtqFuZZbVaUiVPqL0icAzfnjgD92b-hAblLBsdi1NVhX3CRPgHbJ4ZOzq1wRKkgYHfOOiMdoyE0FgcZQfClqs-P5t4abLqw8cEbMmMrA9EYHugz3P-4v5bqwzpemYzTNaQNbi9ks56hdmWw7INGw_kRh81-g6Sf5hqu3vOg5zxqiU2vcujhatNZQcKcB5hW_CP9pmYYM7cjikcgE4_g_3N0sHKG7JAk9EUakmdE7O47lxT7AW9HShZ-nsudBqWfbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های لالیگایی اتلتیکو
🆚
رئال‌مادرید؛
کریستیانو رونالدو بهترین‌گلزن دربی؛ 22 گل؛ اتلتیکو در 10 دربی‌اخیر خانگی تنها 1 شکست داشته؛ 5 برد و 4 تساوی. مورینیو دربرابراتلتیکو:11 بازی و هشت پیروزی. سیمئونه در برابر رئال: 50 بازی و 14 برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30125" target="_blank">📅 16:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30124">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3Og7AWFgeen9ixVT1kIPK63ajNOnzVf-gvMgoAYctO-sfNWr9n-fLDRxe_EbqRaGNaLvoyncAkJvRAvTG4kfjhjjZmGBobcz1wwvUVUO-idO5utO4wj9SmJTXYdi3bHYXXpOvEKMULDhcPAdDJ6Pb-jDVvfTiYGxbXq3Diyzqjz6EMH7N_lts3pVC2pZQWw-buydRaP5YD2Wu0cHVQjkOUGnHKe76NQI1_pt09dIaeR12dCzNZhnU4xYr-i1YHsQlSCEhqoLWt5s2HEuyzBI2aK4Foq6BqxktIDRO4QvYAbfjKOdkkueOzaRpeiUvRsbzbiLg6cgneSDJxUEXU0Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ مدیریت استقلال و شخص‌علی‌تاجرنیا رئیس هیات مدیره آبی ها بعداز انتخاب‌مدیرعامل جدید آبی‌ها با مدیربرنامه‌ های یاسر آسانی برای تمدید قرار داد سه ساله ستاره آبی‌ها جلسه برگزارخواهدکرد. درباره مدیرعاملی هم چه فرشید سمیعی انتخاب…</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30124" target="_blank">📅 15:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30123">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4RBp9xXatGXM7w-BLqavKrVnxl5OFkyzQhmItHc4qn2YtrIkfu3sVPk_yhJn4FtFjX0OHeHTusj1ENJm0gGy_L2vUctP117qU7ckwcSgWRt6dkfP5DvnbvpXlN1ygqnURKiFSiTtpoShhKcD3dfASWeOZzOZxoYXlGbw_7qkyOWE5A48PuWyWmRwqDXYYtuupsVlXbQaZN8p2e1ly2EjKuow5EiXDg_QwUs6YkjYJSylCXb0V4m_Giw3M620LNmGOp4Ea77n-TPecSxpKght7iC-sTO56XZqiuycyGgyaof5IcxOOxDP33somKHcTdINQFNPBAmxqHWvrs1MJUYfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مقایسه عملکرد رابرت لواندوفسکی و هری کین در 150 مسابقه اول با پیراهن باشگاه بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30123" target="_blank">📅 14:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30122">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e09969a195.mp4?token=lRodxBjltSisZmPxC2SmbPC7-Sdvh-hnptycv0N1M3_yDgPSY-OZ9Wjg8XkqEVltPmiR6fDW9aCTQOWrdA3_dn6VbWflbK8soM8TVlJrFHDGBMpLQDuYeCQ74vH0Ena3yzlyQl4i-YiqYbrWzpqCAcRzkX1tjI3wz7Ei98_WmUCbPyx4hjdwoLWsSE40W_PWZhPDA16LDP__NtCM0rmj_vrt4rHBHzKqcyiJsSMDzIC-7DRUtlASu9Da2yV6bBiGJCDNryBM4kfCHh2MLy21EEDk8-G55pQPXjUSEL7UHAa8fHWN0D027cBZTYepSXvA04jGj_KKRB8nyb1nlPOFfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e09969a195.mp4?token=lRodxBjltSisZmPxC2SmbPC7-Sdvh-hnptycv0N1M3_yDgPSY-OZ9Wjg8XkqEVltPmiR6fDW9aCTQOWrdA3_dn6VbWflbK8soM8TVlJrFHDGBMpLQDuYeCQ74vH0Ena3yzlyQl4i-YiqYbrWzpqCAcRzkX1tjI3wz7Ei98_WmUCbPyx4hjdwoLWsSE40W_PWZhPDA16LDP__NtCM0rmj_vrt4rHBHzKqcyiJsSMDzIC-7DRUtlASu9Da2yV6bBiGJCDNryBM4kfCHh2MLy21EEDk8-G55pQPXjUSEL7UHAa8fHWN0D027cBZTYepSXvA04jGj_KKRB8nyb1nlPOFfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌جالب‌ و شنیدنی این نابغه هفت ساله اهل شهر تبریز: در آینده میخوام پروفسور بشوم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30122" target="_blank">📅 14:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30121">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Is2ooows6tr6YdV-ct7-S8uv7fsqvRyvfPmGgIR4kqJ6IWw1VcNtbV6sB455jcOUnKopEL7qp7vRVmvF3HKZopdqsHHrpkhU2WQ3YL-1O8pIZRH8PHJH97VfJU3K0Ei-Pgf2qka85wSAVC_8xfJJ3G4xnl9KObIG-eBCdKyR1TBbKpMtR7DlaU65ZvAYgNewmoJ_pKyvBpP9I20eYNWJvUD0rDGTr5Pg6DyB2yl1jl60Kwr2oG7n25v0mYtC6JX3mRNZ7j7jHqL8QIXv5eeQCu_p5WsINvBzUlyAhW3pMrVgwAQuQfTaKgPDUEdTy39reNO_5x02XHW3ZI5G_CUIgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق اخبار پرشیانا؛ به احتمال زیاد سعید دقیقی سرمربی‌جدید نساجی میشه‌. فرهاد مجیدی که مجوز فعالیتش درلیگ صادرشده دیشب ضمن تشکر از مالک نساجی به آفر این باشگاه پاسخ منفی داده است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30121" target="_blank">📅 13:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30120">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiEopbOEMC_YXrgObEiumicL5MFvkXo3yRv9_Z3jc2vy3YTvV_vKl2rniKc27mz8RXfxH4cRVT8nkliFsoEwjHb0ccb35v2BYp1oySxIvk2IIDNPsBJoTjDEXGp-nSkuO11maVpB1cysWI2uK1xFc7mdn_ZLRLi02KVvCM0Dk-VqNJsHkFuqISBZlJevHGNlBwTOtxo1b-Dvp2guYzMeQjsEwdWpjtw4Fu0vZX9Ls-KlAEVL7fOHcsdKYbbU24nKWFUzCNw_MV7RTi4fZJg51MCjnKAK-T1lk4jxjRRmihv9MfiyrrnxyGZDdMxdzicVjH3zXU1TXFEMiAroOwjRjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرشیداسماعیلی‌بازیکن‌سابق‌ آبی‌ها:
رفته بودیم اردوی کیش با چندتا ازبچه‌ها عکس گرفتیم بعد از ۳۰ ثانیه همون عکس بین فن پیجا پخش شد. از اینکه به این سرعت عکس پخش شده بود تعجب کرده بودیم. بعداً فهمیدیم که خودِ سید حسین حسینی ادمین فن پیج خودش بوده و اون عکس رو گذاشته بود. تعداد فالور های اون فن پیجش هم خیلی زیاد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30120" target="_blank">📅 13:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30119">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7061b4b2b5.mp4?token=tT5s8s5QJUP2ZvJnxUUpCrgH9SXC_gRFLrMn9iT3amr64t6duafTQz8MMYrnzfzVsyKmyvZXZMOamfHc5XxxPvf8ehVNiKcuohPN4fA_091tfTtN50H8bZRg689axbhWv2ydi26KFztcERywaAvxnyJdQbIesWSzBge4T2sxfm2QwcokThFNMP2iDiAF8DH65H6Cq-3kAYR6WwE7wIiMYzGbL3_5vj7XeX4WvlIRlaqzNHR8Qjz0UaX7Gkb_vkaVwN2cXvCv5t1o2Sm5tY5hFR84AsJ-EPKNoUX2Ko1gIL1BE7ow54P6al8Wj0gs95JDc1mIpYJgJir9ADFCstppYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7061b4b2b5.mp4?token=tT5s8s5QJUP2ZvJnxUUpCrgH9SXC_gRFLrMn9iT3amr64t6duafTQz8MMYrnzfzVsyKmyvZXZMOamfHc5XxxPvf8ehVNiKcuohPN4fA_091tfTtN50H8bZRg689axbhWv2ydi26KFztcERywaAvxnyJdQbIesWSzBge4T2sxfm2QwcokThFNMP2iDiAF8DH65H6Cq-3kAYR6WwE7wIiMYzGbL3_5vj7XeX4WvlIRlaqzNHR8Qjz0UaX7Gkb_vkaVwN2cXvCv5t1o2Sm5tY5hFR84AsJ-EPKNoUX2Ko1gIL1BE7ow54P6al8Wj0gs95JDc1mIpYJgJir9ADFCstppYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
👤
#تقویم
؛ 20 سال‌پیش درچنین روزی؛
ژابی آلونسو ستاره اسپانیایی لیورپول این سوپر گل فوق العاده تماشایی رو درلیگ‌برتر انگلیس به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30119" target="_blank">📅 13:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30118">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4XGaYlPQfRUKFV687MKmTUhV3aPCDeaLWvvxcfteFBlauc7t3FUBE0wm7Yw-0Usbk3SnzqV32avP65iU2TkZ2D2XsNTZbaEilTtZIDhdtpek_9d0Ey1SpcEK0VlbO3v3nzI598PBbbkAq1oJHVNPfZE8ZjV_4K2yDvNaKpmM6OnVL5K8OzIA7jkKkSuqx-mpmMI2S6JjFHwdzpSbDJcHvljE8hI5r4SVzDA6wz8vMZK9gzRRXh1t3i9U7sxC2ze6KsUTBbrCoj_XiaJ_URzO9HaGITt3dq3Br0hI3z4roVRHADFrHmOONArkcOSe1MKE8Kyta61wQO-fBEdJzRY3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|پیروزی شیرین شاگردان هانسی فلیک درشب درخشش خیره‌کننده غایب بزرگ لیست توپ طلا؛ رافینیا دیاز یه تنه با هتریک‌اش سه امتیاز مهم بازی رو برای آبی اناری‌ها به ارمغان آورد؛ هفت مسابقه، 21 امتیاز، 31 گل زده در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30118" target="_blank">📅 13:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30117">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAxlOwlOuiWs9p1HrAXnrYecgpL4avO-QJa_IDjXN0fXKvi995ZVp66uBfvDU3Bkx5Bt3jF1h-1EIEfLesjKhDenuLf4RV5LAjnO5RQeI6_VXBKj6CNFPw4vuR6Vl2IkZWRyNgzPob5cNH6Q5AhmjpiC-lG5rqxKTQdxFvnFKdC1CrPNYAg3lhXyxJ2whSxdxZ6XcLJwkvC-p0scvPSce-__ric9cdrwQ8LuUcfnmZYy2Ki3T2gesxcJSNUGlW90iATlU3ktqEZnKw5YOiCvU5XeuHyBy8_s6FVkXUJO_pTzzI-9Rqls-2xz0KG5ubeByH0CatTrK7LSXlOay2XHEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های دو تیم رئال مادرید و اتلتیکو در تمام رقابت‌ها به مناسبت بازی حساس امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30117" target="_blank">📅 12:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30116">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlhapGhTWweq_yc550WAukhnJ5im7qcY9qjjFUdTIDA0jHnmDUPzkHTBTTatqipeg0xV-0aSaFymXi_2UOAttWT7JSEtf2963Zw3yEvCEczZ7IQY7Qjgm9nn_stdPfYF88aJilM6LKI7S0IORIC4rd-KtHbK9n3GXS2nLEFd0xPxjOUrud2mVDnedun6m1b09GcAgi1SKe-QxByHTmovow1Kvq81R8fN6qDQljWskPM75sRkzNgsIjKsirozY0DXwNCxqYluWvyuoA3tG-uEv5Ma1mv28PI3BfcKM_9cQC30kOGra-7I91H1JPuCPx9wQmS2iwTd-SoY_jkQop1Qew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ عباس کهریزی وینگر20ساله آلومینیوم یکی دیگر از ستاره‌های‌جوان لیگ برتره که مدیربرنامه هاش درتلاش که در نیم فصل او رو به یکی از دو تیم استقلال یا پرسپولیس ببره. شانس سرخ‌ها برای‌جذب این‌ستاره 20 ساله کرمانشاهی در حال حاضر بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30116" target="_blank">📅 12:27 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

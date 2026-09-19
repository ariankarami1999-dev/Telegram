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
<img src="https://cdn4.telesco.pe/file/C8mdvrnepZewpqBIVOgnhrZ_eJI9jRG4D03fKEnqKY-EZeXUzVBWOe4s9alUCZ6r9ps46iim00Ep6h4-NGqzGobqt1AnARsZZ2KP6tti0z0YMXcu2xY8PC4ylW35YyzzVQGLF6MFnSYKYrrz4EvC14IT45-IWi8HW5grbl77g4rMsrLPprUU54g6BbA7n78OLrfacsUHh1cJbr1_WrfLQohkEhBkji3YyWvkosDVwIoxnkwdJdTVZGE9hp7Cl-l2HbpQB573BLBRpzP45Alp1KJsVxAkwJ39QKLW_z5VqZ2lDBLtBOe4DrLmxe5XnhIE8Z3NhfL_DRGMtHqgI8PMxQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 481K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 21:48:15</div>
<hr>

<div class="tg-post" id="msg-30084">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYXxwO-wa0k846V53zN4mHs5zFO0vZwnuWmxcvdMBgldEwJERcjhhqynKBW2J0IxI_BIKgdqaTQFbbhpvRLn5-YWtMtd9MnnQMVj03qtcW3o1MOqw_T_LP6IU5lh0gwbEoEAQwY9VLIMtE-D4gGEAOAZUntK6t1cvpLEovkmQO7L29GvAxu29viKa2h0sEpeV43rv7ts-APeKbFwcSubUxrFMO5q553vz-x0J9CEIbbrKM9lgqEjJ2qz-ByKE9_tDQcid-LhNYCOpVfXMdj_Smh671FlrjKbJMlh2P2CkrEo0-Qew3vZfFMQjzBmTm_ogLQqHao0ag5ObEDtHd5nCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛
دیدار تماشایی و مهیج دو تیم آاس رم
🆚
اینترمیلان بانتیجه مساوی 2 بر 2 به پایان رسید. گرگ‌ها در نیمه اول دو هیچ‌ جلو افتادند اما در نیمه دوم افعی‌‌ها به خودشون اومدند و با دبل لائوتارو مارتینز سه امتیاز گاسپرینی رو پر پر کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/persiana_Soccer/30084" target="_blank">📅 21:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30083">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvGY0yuOgZ0rQKNiMk5a4eiamxIuMdePRqUBnS3YQHjoGF6t4vo_iYdLvKgPEcRKEDVFPikme7sP8fLYfZdSlJ1GWWwuUJWc4O15hkqax8pyZJJ_yFPyiip85ptKNdWOkXr_f6axFcFTtpOlHn4cX8Q_aHrIwPrunQ0O8BU1qoXTqNdfUvkz67mVp6p_avto7KsEcPB89D6iWj4p1vOjv17VzVIoXPfVdHSzEOc5K1gbgO-SRsLYCJr0vshnCGOOiMxNNo_GJuS-_iSMKo6oBKzi0HFU6X2SysONogQ02qplCWZNZDI6jacQONZwAnp4NvVmBwVTra7T6BM56cK2Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا
|شماتیک‌ترکیب‌تیم بارسلونا برای دیدار امشب مقابل سویا؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/persiana_Soccer/30083" target="_blank">📅 21:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30082">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aer_wvcXldQxNzfAJPAfc-ADQdHew7uAZDeF9QLA_oMMdIz-R-TKtNxW5nJjyacp6tv9Msw9mOwanjNYNw6sCsWbWhon8vD-qbjpuIQ6-w8L1IY9W_-CcvdlIvgDGma3sLu2WSfQysmHcOJ_m_61tmlwOIu1MA33nyLVbjxj48Mot_JDq3XDdkpqx070PcwMZYmquB2xVguH9fcQPUnIFtusSDVpuEzjcrJ1d8TyzwMXsqvB2iBW0d8xv8Lt1u-zvymz8F8FqoBfKbbV41_D1o165ho9DfcqbqKZZn69YjglwCQgiNls4EexOByw40v_B27GSqWXXnm8JdmE-8r8mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
ویدیویی‌جالب‌درباره زهرا گونش ستاره تیم ملی والیبال بانوان ترکیه و یکی از بهترین‌های تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/30082" target="_blank">📅 21:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30081">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZmNg83CmHb3Ky4cbasjRik0_cOSK7UPloLP7OQ68JGLSAycmYwI8T5_l72AQzXV-qrkgrp05gs8P3Ie4UP4dzZS0m9Wrl6gr2QSApMQtGq2nPurFPY3CVZ0swzaJys0LtfXlv7H-JTC9SCbfEiYv6cLlXNXnMczK3XKc-Nc8pPUggVI-GZHM5xctV8dGzb3ecdtuUFs7oto2GJRhgfWiXkORVvRbgt0KkeQZ6AHYvKEwJ12QU0Mh8CEIWD3lFk-fRp0OvLpZKC3E0hYbbJQajeO-e9GbzDV53EfgWyt_amBBHXPOTgihhBZ-gGFRiuv-lJuzemgObUATnheigC7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمدرضااحمدی مجری فوتبال برتر از صداوسما انصراف داد و به مجموعه آپارات اسپرت اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/30081" target="_blank">📅 20:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30080">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d622da65b6.mp4?token=ONB_fjvLrDcWVsy6_2-10AvqwBt4PYyvdy7HQdlyWIureF4LXWdz8plhK1lUnqod-n8B-pXVNYjvCgRgh7qtOGR__ta4dx-Qi2wWCLLMcxKWDgUkbs9hrCrmULd7oSA3dbEXSKHkM0qyocNWrKO0Xga4GfU0AeV2LcajPUi6w56iuZ_AqDw9t8sUzWvTTAxFQ7-APtHDEqcr2hyLqY0slQufFIMYckJNe0_Soe5Lbb_25tRLREtIseHbv7zumcAILrGImTOTFzlA4-ucoksqomvLA8Sq5EQU7yjflS2vXYPOcGS9ADbeMwQeHOyQTAi5pAk6XB__Z09FGuHCG6FSMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d622da65b6.mp4?token=ONB_fjvLrDcWVsy6_2-10AvqwBt4PYyvdy7HQdlyWIureF4LXWdz8plhK1lUnqod-n8B-pXVNYjvCgRgh7qtOGR__ta4dx-Qi2wWCLLMcxKWDgUkbs9hrCrmULd7oSA3dbEXSKHkM0qyocNWrKO0Xga4GfU0AeV2LcajPUi6w56iuZ_AqDw9t8sUzWvTTAxFQ7-APtHDEqcr2hyLqY0slQufFIMYckJNe0_Soe5Lbb_25tRLREtIseHbv7zumcAILrGImTOTFzlA4-ucoksqomvLA8Sq5EQU7yjflS2vXYPOcGS9ADbeMwQeHOyQTAi5pAk6XB__Z09FGuHCG6FSMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
اولین‌گل مهدی طارمی با پیراهن الوصل با یک ضربه سر دیدنی؛ گلزنی ستاره ایرانی الوصل در بازی امشب این تیم مقابل العین در لیگ برتر امارات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/30080" target="_blank">📅 20:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30079">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqIaEgYmglcYwyHzt4M56AYTdwlihUGnZeoP4i2kAVe6PCZZnwpc3uUL2DLTIxclckZ1KYdlF1ETa-PPf0hmlRpN7swaaA35iC_yNR5ZMZxYAkMwbA7mHqk56dnaxDagTjIN5tMbqWZM65crB5DYkc1bEsrleXMiZu79BjypFl3mlgzOqHB_t9Ysd4M6iHGzd0mlncMxTrzb6LuZg-CuYzJQ8TBmBHSPP0bw2lF2KvH9e4SpAIS7cqGKTXM1qrleICyggDWvxQlEWf6gOwPXiFvde4eCyUFGR9ferylkRptnDQKKWRm0LVMusYW4N_dYVrRvR91luJhYiiWGwX0ymA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
شنیده‌میشود میلاد محمدی از وضعیت خود در لیگ بلاروس‌ راضی‌نیست و ازطریق نزدیکان خود در باشگاه پرسپولیس پالس‌های مثبتی نشون داده تا درصورت موافقت مهدی تارتار به این تیم برگردد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/30079" target="_blank">📅 20:37 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30078">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGugPRA5IQ9Z16qzKBce9N7np_gUEH2R19KJpUnK7apmwzIX6ejTbha95oQ40ZX6j_6F1mW1hAHEAhLidZL1eAOeGC6AJbBOW8vIyLdgo0uH32GQp0ozjz001xgtgQUKxZyHHPA5vdxUkOuemgAVDywYtQ3L6bu6he4mHSTkkVifk2JJdjjJKJFNIy26vgAyD3KKUIfQJ2CUYNQ9mJWle7eY5menbLO46vW0XD9ThByeIgueqJcy0VaDhguap-c4lud_-ochTs85-inNih1z6Mh9Bo9VAB-CXzzJYIudZ6exnxB5vf8jIvrR1-wBEh-1Rwey2ql2YCTDEx0Dz52VRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
ستاره‌جوان رئالی‌هانیومده صدرنشین شد؛ چهار بازیکن‌رکورددار بیشترین‌تعداد دریبل موفق در 90 دقیقه در رقابت‌های این فصل لالیگا. نکته جالب درباره دیومانده 19 ساله اینه که مورینیو فعلا زیاد بهش بازی نمیده اما این رکورد رو ثبت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/persiana_Soccer/30078" target="_blank">📅 20:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30077">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKSrAjgxEc3YuDvQukqrK9MIpH3oUEFj5wPwPkJaNwz-u-LUaS4ac_F9sJGDi5yyhFpBWo_gDiD5G8OADyUHbbtUhAI8gYstp-XkJVA8uCNpRpg5TTJQnnUdqtYhJobponHesiek8CYRHVRZ1wGWNOBqWRe3B2f48n7Bmnb9m0lANYg_hrnw4FpvNh62xmAsPGMlUDPreXVrgKb0FJob1ws3dZTKKKU_sp_kpE3odbiQHeGnCs86CT4pm-_LG0MdHl5MU6ESLCkHJ4ml-B5vceFQ9X4VLRaBDwLY27VTWFtAyFzBWC2mITJk5n8dMhKkBckunMEo2xF6zyGM-n1fFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درآمد لیگ‌های معتبر اروپا از فروش حق پخش تلویزیونی در فصل جدید؛ نوار سبز میزان درآمد از فروش داخلی و نوار آبی درآمد از فروش خارجی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/30077" target="_blank">📅 19:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30076">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🟣
در هفته پنجم لیگ برتر؛ شاگردان ژابی الونسو در در دیداری یک‌طرفه‌متحمل‌شکست سنگین سه بر صفر مقابل برنتفورد شدند. برنتفورد برای‌اولین‌بار بعداز 88 سال، تونست توی زمین‌خودش چلسی روشکست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/30076" target="_blank">📅 19:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30075">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5BSgqvybJGjsAQuXUIORRAgv3TVFUd8tAlQBbMM-mjR1QWRzvD3yW5cSEvVKo72JsS0K8Nk2T-L6ozc5v_ttIhfrhfAe-y7xuwvv8m-zAma7GEOUH4BybuZ8Ybf1KrIBy-pc_OhsjUAxWbAOMPvRX5UOvmTXAYKxoDRxW-JWr_uy_80naf-taBfpcflKYgZAr1dVU_wxgoOu7enT_uOaenllq_17jtl3f61iyE18BhnnO_T74EJB8PBlHczVQ_Hnwyf0_RrvmzUwek_CoEysdLbM2mdH86K3xUK7RbeldaYKOl2h1UvtcqeK-cbOzzBzqfGT79iS0mBLbnp17u0fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام دیوید اورنشتاین و رومانو؛ بعد از منتفی شدن حضور ژاکا در چلسی حالا این باشگاه به درخواست ژابی آلونسو درپی جذب جردن هندرسون کاپیتان 36 ساله سابق تیم ملی انگلیس است‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/30075" target="_blank">📅 19:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30074">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5018b3d28.mp4?token=akfxGfP88l7oyWZMGxHQnSpleMzOGeQCsSmuNK6odIKracjqZ91gUBgyFfgNOJRGW9OvZitergnI_hE6pl0wQd1NLPIZsmVUm05AlAbRRe2ndmShEJSLF6QeW9gzHtZ45Zz9YKz5wq6DScRhacCv5QDFSsAoCsfse0R5DZdPqaoEDyOEPH_NOTrg-ULbsyO1ZcC4FayApk7XKaM4423AojvMTpYfKTk40rPugepYG6yy9C-bTNLmcKHVr-c6DrxpVKMHlbRb7nOGXerjO4SX9BKrsXCme5e72YRFVFi7FAmTQcdgsA8-YW-CASjkBRGt7F15sxrypSORd4eL9XnspQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5018b3d28.mp4?token=akfxGfP88l7oyWZMGxHQnSpleMzOGeQCsSmuNK6odIKracjqZ91gUBgyFfgNOJRGW9OvZitergnI_hE6pl0wQd1NLPIZsmVUm05AlAbRRe2ndmShEJSLF6QeW9gzHtZ45Zz9YKz5wq6DScRhacCv5QDFSsAoCsfse0R5DZdPqaoEDyOEPH_NOTrg-ULbsyO1ZcC4FayApk7XKaM4423AojvMTpYfKTk40rPugepYG6yy9C-bTNLmcKHVr-c6DrxpVKMHlbRb7nOGXerjO4SX9BKrsXCme5e72YRFVFi7FAmTQcdgsA8-YW-CASjkBRGt7F15sxrypSORd4eL9XnspQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
گلزنی‌سامان‌قدوس‌ستاره33ساله الاتحاد کلبا دربازی‌امروز این تیم مقابل خورفکان در لیگ امارات؛ در پیش فصل باشگاه پرسپولیس خیلی تلاش کرد که قدوس رو به این‌تیم‌بیاره اما مخالفت همسر او باعث شد که این انتقال انجام نشود. همانند مخالف همسر مونیر الحدادی برای بازگشت…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/30074" target="_blank">📅 18:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30073">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCaWz05mtsQeGSQX64CGuOqS8wHN8TdoTsuWzYWwuQmFQvTEF1tOC30_7tR0kKIFD2UMnQrgxYWwcZNyu-QOyYn9vi7qA6rqy0CP2vHZAGlsGkqO0ovCvV3ygD1pMUQrRZaTmvxdG6j8vN9IepaHrrpBeIUPb0TTGBRe4x4LrXJLMGJvIj-yazwU9znC3cn3-LKv2Mqad1qB7V491wBlQhRcwAIMJvBK-XHw5tSKSYmFHdc5ia2TJgSe65uOlWK8exQxsPS2ssKWlR7QieP6aq6Ej4GeOfczYtFdmpDMid8jOQeVlnu7r105CTBqHM_HaEKqDeI9Q3e5WtSJ2_9YvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ دستمزد بشار رسن در پاختاکور سالانه 600 هزاردلار بود. این‌بازیکن در نیم فصل قراردادش به‌پایان‌میرسه و علی‌رغم اینکه پاختاکور دنبال تمدید قراردادشه اما گفته علاقمندم که به تیم پرسپولیس برگردم و اگه باشگاه بخواهد حاضرم مذاکره کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/30073" target="_blank">📅 18:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30072">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9989fc3781.mp4?token=WSpzLq0yQH6K570TqGcHmVr6zCJW1HbgkFjVh3yyxWfhYAdUwopSHjIvBP5U6BeVutCiy7dFtJF8lNkBt5-gyby9UUPKvEyZpAT4jJm-WWRbNg5Zr67wh0yPBp3MIJTq-puTN5gUWENUAJncZTAKlr-14SxlriZ6swaUPfDHpMCMMg_bKYq8pRiiZF3xujTWepp2KjX-GDtOT3SY1pZzOs5PxDScFKSD1ucXhNPlEOOq3Is1LDmjXN6Nda9McXHK_MkpLIUPwoFHB5rfAEKgNa1ujf1u-SGoLm91IqBeL_9dZqEnEx9skvMHGDRZ7z_ilFmjXe2L0u49hiXT4fOhAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9989fc3781.mp4?token=WSpzLq0yQH6K570TqGcHmVr6zCJW1HbgkFjVh3yyxWfhYAdUwopSHjIvBP5U6BeVutCiy7dFtJF8lNkBt5-gyby9UUPKvEyZpAT4jJm-WWRbNg5Zr67wh0yPBp3MIJTq-puTN5gUWENUAJncZTAKlr-14SxlriZ6swaUPfDHpMCMMg_bKYq8pRiiZF3xujTWepp2KjX-GDtOT3SY1pZzOs5PxDScFKSD1ucXhNPlEOOq3Is1LDmjXN6Nda9McXHK_MkpLIUPwoFHB5rfAEKgNa1ujf1u-SGoLm91IqBeL_9dZqEnEx9skvMHGDRZ7z_ilFmjXe2L0u49hiXT4fOhAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتایج الطلبه و دهوک که تحت هدایت علی رضا منصوریان و گلمحمدی اند در فصل جدید لیگ عراق.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/30072" target="_blank">📅 18:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30071">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDJWK9emWXq66yAxjVv2c2GevtCBvRn-X4jHo0fFXVAAVMlt8A9Rl9PW6GSawH2ICy2fSbClYk5xZSpdVDM9Nr5-mwP9vuJaUe6soc1UocZzBmjZL1t3h7FtUzPkU69lI2ujDM3P9wgKU9VvltsGOXr4TMG-LhWm5TB7kB5VNrT_Aufhmg-fMbKiKzOFXcqJrl86LB3K4lg2OokZAstXe45Zf2N8VmzODTUrcdsczuzXe5a1g9f8AOqHSORvzViYC4F1685Gt_DxQ45jWLDmx7z9ii40UyVzzkTYmuzjrZnv6yw3wBxcyJSH0YAn88l4lAfsEPunZvAEFnkhMwCYpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
احسان حاج صفی کاپیتان‌فعلی‌تیم ملی تنها دوبازی برای شکست رکورد بیشترین تعداد بازی در تیم ملی که دست جواد نکونامه فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/30071" target="_blank">📅 18:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30070">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUJKf5DItL38qdgIBMc5doNb-DyZdKUIHfqQ35BZ5IompZOuzYV7D9ECA17A1Xocc0_nDujmqrIpDZ2ApKTpghQVVqgzCa1bEbCi9IG258uW4omaeEJI4P46bEhfZrHeoSFhNio6LBU-2KlZozB8lqbU_OaodyJ9iBcB8mSedCNTHDZiEGDdXkgIDQukO6Tue1pi7ESbneki2NaG49swvN2qPKZSEVpAxXj4SkJ06d6-3alY7jZAQzAm0JHa9Lq1uOaV8oLoFmyb4AZwyKqg9hS_sIJKo4LCZ4vb8IU9CbE1ivDWV2yX3PR-5t9K2S6z1aAf6xcfNfme08CPeZC0iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روشنک مسئول مسابقات لیگ: یه چند روز صبر کنید مشخص می‌شود استقلال قهرمان‌ اعلام‌ میشود یاخیر! احتمالا امسال جام حذفی رو برگذار نکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/30070" target="_blank">📅 18:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30069">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnUlpJ0VUAls4vOa4Mzb8fMve2hI6Jd4M96IcmyyH4tGTq0avJW5XLg7FUhRYyYDB25ztN6EfGRNdHEsBIAJd7yeCrPAYiLRAvLqGMBBqUZPB8DX7BLKL5AvB7mJwBxRvF7JECgXeSP_ADXYPYwwwSP-brOVvY4xZQBELwV_TisDRoFVyFgLHnY3UpMOhFH0vHSsuLVwE8Xe1TsHzumo2gPUydtKjgDy2Od7LMtCSaamHsK_nQHinulenLsqRzaJbUE2vNCkXTGZXhpT01pB-z5AbckIqZhlN8sLiESnHzdPUsbTMqgOp2yL-S7p2S5wdFRjw8PUwRy5Dvt7SU6fMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی Yekbet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🔔
فرصت ویژه اولین واریز دلاری در یک بت
⭐️
یک واریز
🤩
دو جایزه
🎁
⚠️
یک انتخاب هوشمند، دو هدیه ویژه
تجربه متفاوت با اولین شارژ دلار
ی
🤩
🤩
🤩
فری‌بت ورزشی +
🤩
🤩
فری‌اسپین کازینو
👀
با اولین شارژ حساب از طریق ارز دیجیتال، یوتوپیا ووچر یا پرمیوم ووچر، هر دو جایزه رو دریافت کن
🗓
شرایط استفاده
🤩
⭐️
فری‌بت:شرط میکس حداقل ۲ مسابقه با ضریب حداقل ۱.۸۰ برای هر انتخاب
⭐️
فری‌اسپین:قابل استفاده در بازی Yummy از POPOK
﻿
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g28
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/30069" target="_blank">📅 18:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30068">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841d5e76bb.mp4?token=lEgOV0KeUh1hY9-b5u7GrU50dpQGjcTD6XPJo1KhNhXfcQds8aGreJB_stHe0x1CuJrQTy2xp7h7maWGhA3azh-FgnyapXIMx5mX7spgrt5g_fu7BvrAINwj-v28R2C3ynwaj81foWJd8Ssvrf7uY-c7VHHSrqcR-eQWry4tSplFdVElA_sH1EeCrhK5vwD9fQdvGBMRwd88sl1mSqxtKZuEq_XMiICay8rIsrvAS51q4CM11QPEWjerBK5oFnhgexnDAlS31M8tShHkRCXkn-TMrKW6S3a4aZFAKvfaHQ8GoSydXMS6zUwMKa8Q88VYvnoDjIpfO_qgKZR53IALvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841d5e76bb.mp4?token=lEgOV0KeUh1hY9-b5u7GrU50dpQGjcTD6XPJo1KhNhXfcQds8aGreJB_stHe0x1CuJrQTy2xp7h7maWGhA3azh-FgnyapXIMx5mX7spgrt5g_fu7BvrAINwj-v28R2C3ynwaj81foWJd8Ssvrf7uY-c7VHHSrqcR-eQWry4tSplFdVElA_sH1EeCrhK5vwD9fQdvGBMRwd88sl1mSqxtKZuEq_XMiICay8rIsrvAS51q4CM11QPEWjerBK5oFnhgexnDAlS31M8tShHkRCXkn-TMrKW6S3a4aZFAKvfaHQ8GoSydXMS6zUwMKa8Q88VYvnoDjIpfO_qgKZR53IALvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
عملکرد لژیونرها در رقابت‌های باشگاهی امشب:
🔴
الشمال
2️⃣
-
1️⃣
السیلیه؛ پیروزی‌مهم یاران امید ابراهیمی مقابل حریف خود با گلزنی بغداد بونجاح!
🟡
اتحاد کلبا
1️⃣
-
1️⃣
العین؛توقف‌اتحاد کلبایی‌ها با وجود درخشش ستاره‌های‌ایرانی خود؛ سامان‌قدوس ستاره تیم ملی ایران زمینه‌ساز…</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/30068" target="_blank">📅 17:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30067">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpRT8Dp6GEGF5RuR0wVVsbzCJ9yyK59HrgRm7RNJ5G3BhTbrpTRtXSFbI9_cAjAvkht-EPC37JfxDqjUYuLq-9DXXXgMmdTsKXc3qOX-Ps8FjlU1USEsV_8aJJAGEWhzL9uqG_jpXjfLBshlBA1HWvjPCjkDxzV0QSyDpOFsQwVNdnSPfTO3QNNTKBkjhpImvnEbcU-AwZOTOpEB-4pflp4qxQpE85P4iezLTe8H8lq90VSvSYnl0dCrKin6vPxqwgLOr1kxgfx6P7RfbUum8CwBpdSFYHskVOQ6n6Z7dCYUyDPzuNbM1Om_0A0_WeBBXABz_3ASXSABTxTQXDg5kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
🇧🇷
#تکمیلی؛ مدیران باشگاه بارسلونا بزودی مذاکرات خود را برای تمدید قرارداد رافینیا دیاز فوق ستاره برزیلی خود تا سال 2030 آغاز خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/30067" target="_blank">📅 17:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30066">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtbGFZvbb_9znM8Xa8Sb4lnZCrALLI4psh0AuWk77_EYGyKcdCfJwzvWyL3cN_u4UAOxW4jcmgUYvolSvBzIclnOX6b3fpFWc2UOCxou6-UJnTNaT9AwISlFoVVKlEmg3QrX6sHwkcgwvKE-729TXR0tkbVmFl0OKnt-rDCHXXPG1snVDVRBMFigV8-I_dkqSqFbSQaIvq52x2VG__f70f88ntQyRhEH7dwyc2JIpYzTBmlnTdkLvT886gWxrrtVCoSKRNqJQEiEgMcTDZcw7Zref-InEGINMja9VMpM3GhgxMBxzk8Ruf3OzC7JZoXSGtUguzdpbDkfSNkMCxP0uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
به مناسبت دعوت دوباره CR7 به پرتغال؛ نگاهی‌بیندازیم به‌عملکرد فوق العاده کریس رونالدو در تیم ملی پرتغال؛ نکته‌جالب اینه که پرتغال تموم افتخاراتش رو با حضور CR7 به دست آورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/30066" target="_blank">📅 17:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30065">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMOAnUzdVduC697Pjo868Zntg0st8J1-r1_qEdPcfu_ZMeOHkIwkf-aFg0sUz_oV5s6rYmi0H_KaOCKQ1KdUZTrYw6GXEuzPjWcmvQPOva3nvZk76o_ZMG6J1GzXQTdX5-1yzX112uUSL_76ND-RUM8Lqu1RZEY22rsL_RRhc8WJ1aYXzlIT1HTcOFmwz4_XnNcKBaaEWYlBNf0E6f2DPTLAg6xQaZr-7CG1ZUOdUoPP2RSwsUfPAFDkYbjoRs2Q0d1PW3HIrM97PW4t-C9fg9Kea1d4UgBhft7NJpurbuGqImb5NMZJTkPQmuXL2a0iCSzeZtDxnM9cYL_p-i98rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عملکردفاجعه تاتنهام دی‌زربی در این فصل لیگ جزیره: 5 مسابقه، 3 شکست، 2 مساوی، 0 پیروزی، 8 گل خورده و تنها 2 گل زده در این فصل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/30065" target="_blank">📅 17:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30064">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ig4DHNG-ttUbcyHrsZQ8-rTYCJ2IL7J8AS0bCOfyYeujEp6Y-sqXv2H5jmZbKdQBOUM6RAnaoGcXg9wfKiQJ4foesVOj5kx9rJjdGCBFWdEPB45v-l9H3-zHburTaIlw-Tlu6qNlFgvLJ0DHtI5SvkvoOm-7iC9B_s0CmOFV06igDPtm1ELnusQBNuITe7i84lXZfJAruL9HErskXI9dvsq576_1f9EkuP6m97r6z9XJO5njRBF9WKlpexb-fRlg6M-kYNhbQsdcZ-zepGrdnspjoarg9aMI-viAfaMHerVrMgWnF2LS-ORuQGE-90aKR0oGdQr8LhQ_1fdLLXiUaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی شب گذشته پرشیانا
◽️
مجتبی حسینی سرمربی آلومینیوم با عقد قرار دادی دوساله سرمربی تیم‌نساجی شد. درحالی گفته بودن بافجر امضا کرده گفتیم فقط مذاکرات مثبتی انجام شده که دیشب مالک نساجی پیشنهاد خیلی سنگینی به حسینی داد و مستقیم رفت نساجی.
⚪️
…</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/30064" target="_blank">📅 17:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30063">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a224e3381a.mp4?token=ZPJbOValGdbKk2faZw0IB85Ev2OsYWtcFvXG23dryZvKtUKjt0Ro7vkpacsZSa5ry6rfCpaRFmj9_7XWY2fgU86ufB-hAS_eTxnaFnNDtKJRdbfymZZrAXAgJ2TFjzb7YcY09I1Ij8g6ymwDoAvpNOEIBhOT9MwtNarJQRsYKO1Z4CtaY_5-4Ws7uYGRAunOfARiuUBIo069Y9Ie5eG7RGG2ux23M4jIxEJJH0rDIaBsgwc5jXQcsEe2a5i0q6TUgDzzxvnRQF3YCvYIE_jEv2vJNnZZwpfVdCObw7vBqUPgHKNyeiS3sCRJg0SOmEzK3wNGY9x-LUzLxMnvlZqn02OENKcVmdPQFvU8mH_eMj37FF5KsVWMHc6gbm1TFMPf0h1LBFMDZTi8Iq-mUeBnmIN8nid06QM4sDgrP1HDGfdkWy4lmU9k08Hwa78GhLpAoqrKIzLqwPXfAh0ZqR7I8DFV-FOBskFhDJSV2CuV96Vy9SNH8alNd5-1DsDbzu4XR7maDIz-VHK7oZUGyddfkiSq8HMgFxG0piEjRn86ptWCND1Ybqfmnn6ynDtKJq5TEMTDolgeTpSGpgj5lo81x4aLn8wLcL-oBbmQW85Xn1JuUwpQ2oa8iJXo8qzU3ibrkPe2jA2ixVetoKKZnj3IWYAJu9BJj3hDXApUh2aui50" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a224e3381a.mp4?token=ZPJbOValGdbKk2faZw0IB85Ev2OsYWtcFvXG23dryZvKtUKjt0Ro7vkpacsZSa5ry6rfCpaRFmj9_7XWY2fgU86ufB-hAS_eTxnaFnNDtKJRdbfymZZrAXAgJ2TFjzb7YcY09I1Ij8g6ymwDoAvpNOEIBhOT9MwtNarJQRsYKO1Z4CtaY_5-4Ws7uYGRAunOfARiuUBIo069Y9Ie5eG7RGG2ux23M4jIxEJJH0rDIaBsgwc5jXQcsEe2a5i0q6TUgDzzxvnRQF3YCvYIE_jEv2vJNnZZwpfVdCObw7vBqUPgHKNyeiS3sCRJg0SOmEzK3wNGY9x-LUzLxMnvlZqn02OENKcVmdPQFvU8mH_eMj37FF5KsVWMHc6gbm1TFMPf0h1LBFMDZTi8Iq-mUeBnmIN8nid06QM4sDgrP1HDGfdkWy4lmU9k08Hwa78GhLpAoqrKIzLqwPXfAh0ZqR7I8DFV-FOBskFhDJSV2CuV96Vy9SNH8alNd5-1DsDbzu4XR7maDIz-VHK7oZUGyddfkiSq8HMgFxG0piEjRn86ptWCND1Ybqfmnn6ynDtKJq5TEMTDolgeTpSGpgj5lo81x4aLn8wLcL-oBbmQW85Xn1JuUwpQ2oa8iJXo8qzU3ibrkPe2jA2ixVetoKKZnj3IWYAJu9BJj3hDXApUh2aui50" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین‌یامال زیراین ویدیو که یکی از فن پیج هاش گذاشته گفته همین‌کلیپ‌مشخص میکنه که من در حال حاضر بهترین بازیکن جهان هستم و مستحق بردن توپ طلا فوتبال جهان در سال 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/30063" target="_blank">📅 16:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30061">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwJIgCW_1JGNvlYOU4mffP-Y1nZKVjg_4gJbA3yjV91pEMMfucIRk50pH92as5dvxXLTP5_SZG2PvEmAwv7HBK45cdbS18FQTpqbfGySPmXbB6YncbIYmYV444s5QHG4ZmS7GKw6ARvcjBEw5pA32D_8cMKOQkNBvoVvitkFr89ddWxuP2x1upl7v4kOQEDqj_CY-0LjT-DLo2N3aZ5FL0smRICVZvJbi8EW4LQuhaVHZG7P73lzRZLgRgeC0T9fFNBWs1a6RqJglDx2CYU7IJLaSqvh0SD7fCVJZxpG_ry-KB5FBFlpsGDeu-X6nnWW4qKZbscfZ10o7L5UVSdObA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه فولاد برای فروش یوسف مزرعه وینگر جوان این تیم در نقل و انتقالات نیم فصل 150 میلیارد درخواست کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/30061" target="_blank">📅 15:58 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30060">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOIfCNl9gRHm8Uog2DXJpG4olmDAjikFuVbNOEf6hpCfQPldUZkSrZQCRhD5xyK_VZ8e7KUgMHVMqUO3u8Nq-O_r4yvllCCsNstri2LPoI1DCudRbD9AFZGF32J2EPyAQWWh4lNZs60yln1vV2nGmwiX8corLUZBIgeD8ftQo_XDNlatAcgdR9iGtn1rNUF-pEDzQsyYuMbGyy-0eqZ9UwazjaP0fBjDfQDvyG-Q_JiNM6Dp2bqqr1L_M0HUNKBGT_ozu-mlTOMKqZc_NUY7gWIWK7QHPTYF2zpJA9djZrsyv0FzK7YVFg94JCa4EFSHU26SwdkehpTdhB4dZ6iSHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛طبق‌اخباردریافتی‌پرشیانا؛رقم رضایت نامه عباس کهریزی 20ساله150 میلیاردتومان تعیین شده. حال‌باشگاه پرسپولیس میخواد که با رقم 110 میلیارد رضایت‌نامه کهریزی روقبل از پایان نیم فصل بگیره. کهریزی از استقلال نیز آفر دریافت کرده.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/30060" target="_blank">📅 15:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30059">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUxcqUNZwEM5ZN_AHoZTZMD6AoW-ctJE0CDzafLzSX2aUHSFH0Ubc6GtCGZYv0ruezYefl-ufhkVBcDE7bvgaB4DebZOXu3yt1jtbss8x1j_QoX-u0qMHjaWm5enlhSy1NqMu05ux3Ff60RDxWv6k4bdsG5PIMK-6N8DyMWjKvKjX6mQ1x8edk7OGNmBmyw_zeWA1gzlbkFYJCpRgBRhoBWd-KIsAr-F-XAbx7ht6W36qU43oMOWLFQrK27b7TGC0E2irJEtT6qSG674axWzQyniPPXqpcYoDzg-lt96G-_pyV_Pdt7Gf6BsQk-uTTLCpx_3K6wd2-9ue7Xx7nSUHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
👤
خبرنگارت: بین کریس‌رونالدو
🆚
لیونل مسی انتخاب‌توکدومه؟ مارسلو: کریس‌رونالدو تا ابد. بنظرم بهترین بازیکن تاریخ بدون تعصب کریس رونالدوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/30059" target="_blank">📅 15:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30058">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C907D7I9pc6lrtQVwRWz9fla8xVDNG99Ww9uZt4qZiJnwYJm16a3T_EmiTjXDvQVXcLmmAYYK9zYbg815j4MfB7GioRUbb9kSaCBPpaCkR4gASI0Y_wQOVyku_UdkYcR1v4P7paVITiA9RawzmM2DYQr7YK7wOPibA_7lUVKbJ8Gzhnb7AWJJ0C-ipm0TEdQjkelm7M4IXAhyjGqFdoDiaBejOmCaBqSNNhgzWU1dlHeYDOxGbZ9YKmHAE9Gk3YhAmGuq-AzBrzIO1cLUSZNbYPep2DOO91a4nx4vEZVIswszdhTmGpiIokzMTwurdPHNsZ34n8O8tJ_iQkGpLXTsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس امروز مدارک جدیدی درباره قرارداد یاسر آسانی به کمیته استیناف ارائه کرده و قراره تا اواسط آبان حکم این کمیته اعلام بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/30058" target="_blank">📅 14:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30057">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKS77uwWB9J97UPMoe3x49gxP41GlQZnGWSJSUQ4aO07Xh53-xVVAoABvFyloYkBMULO834NKO9pa_clSNCbpO4WOIXQ74U_RHdMHwL5ajnitFgeMOGOWNkyAfJb2n8DEqu5jh_eBKYPXrq-wOgnqAngK5B8DNDz-h3YZFUVoqwiY9k-W3EF4qfA3-5z6bIhWit2C7sDwiQ0FjYHvm1GZwCQ8oYscvB7acn1LptYU8GbcaNWN1OzwPn0CWErQv3jKLpTM9V5NQUIyUtiu_w8bMeIIQT3sG7R4FLUQaSParB5v3LCe4AOyLSeJ5J25-T175VmNlPWrE8tGceJnIQ6hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بیانیه‌رسمی‌کمیته‌انضباطی‌درباره شکایت باشگاه پرسپولیس از یاسر آسانی و رد شدن این شکایت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/30057" target="_blank">📅 14:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30056">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGxUWbHA-B6Id5-eN2mQYk-KmpTdYfdsj7QYosevC3redE5dPcxz8xCNcojzHAo5AwErNp7IHcFaKdP7BXxIMwhKKB2eL8cOYa3wf8rnsxYvpJko5I3MyXsL_quFWat6WyEveRYDUBMa7vxSp92wCneFdZS3WXzAAsO5pdE4NRO68ps-8awDjDYMdsyHfehUCBIstQEBlJBP75hsBJnZdJXHBp5plZtIf4IeC3DL3Iy6BG5ibyKJIQFhUgMcNXZyr0ZOqQ4tAX8q1QJ0Js_wRPs_mKeWtKxHTg3vU2yLDD6V4jgRLFol2XpgV8tIjACyg_1rod2_DYLx8BNBlBE2Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛مهدی‌تارتار سرمربی پرسپولیس در دوهفته‌اخیر بارها به مدیریت این باشگاه اعلام کرده بود بین امیر جعفری مدافع چپ گل گهر و ابوذر صفر زاده یکی رو جذب کنند که انتقال جعفری حدود 100 میلیارد تومان برای سرخ‌ها هزینه در برخواهد داشت اما انتقال صفرزاده به شکل…</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/30056" target="_blank">📅 14:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30055">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
🇫🇷
در پایان بازی شب گذشته بایرن مونیخ که با هتریک مایکل اولیسه همراه شد بعد بازی ستاره فرانسوی باواریایی‌ها حسابی سورپرایز شد. نیمارجونیور کیت‌خودش رو برای اولیسه فرستاد و باعث‌شد‌ بالاخره اون هم یه بخندی بزنه و چند جمله‌ای با خبرنگار صحبت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/30055" target="_blank">📅 13:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30054">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xk20zxfh5_6B5ZOaiOr72pcx8S3c_4kg-9sQoykWqeDCNqLrKQcvPH7z9Tp7KhIsE_aOxjbSeSc6E4ESarIyWNH3HpvoOO5mZkavZvuJ9KKkWS_xp024UKPfaZlnbsor6n8xJdIcdRqQuH_B9lf9JCFVoQIwWI2RuI7Ks4GORGeW_Wh-A_wbZp8MuFbgm3ksR7oKujhNYyu4-3cCBcHXll4wyM5pz9Jh5CiWetCJOr3g4rz7wPCs1pMW1_yn42jDGfO0fpWryLjII3wkM8aTG3l_Hwl4z8j1z9KAx_YT-qaYKZ_ZL6IxncztvrpgI5PiEYfSFIRHlDtlZNHrsJurgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇳🇱
وسلی اسنایدر سه گنجینه گرانبها از تاریخ حضورش در تیم هلند را برای مزایده گذاشت! توپ نقره‌ای جام جهانی ۲۰۱۰؛ مدال رتبه سوم سال ۲۰۱۴؛ توپ بازی هلند-برزیل درمرحله‌یک‌چهارم نهایی ۲۰۱۰
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/30054" target="_blank">📅 13:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30052">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OozZJWVTyHO2YbdGHSAsxsnxf37EluBouMXbvonWL7YC9rm_O2kalvvZP-SRBUHEhH16uEE4zQwZXw7hdUa5IcWbGeAHqUiijfJCncJO6I5BzGhOZqyS3AMOhYfNMrqgFpUJgNGjcub8cd3T8mZxV133xlPyvdiIegFPakJJZ0emaPXh-GIke2GNaj6Wpv56BmRtdk68SkLz-zdHU5_TTOG3lIHsVcqEX7hNaft_uDSZt1RcoGkCd4WFonyelsFJJqjyTvpTz15ksHAMQ_8kk8DjDG4W0Nuveij_hHkO51M01p74jA7T6_SkpdyqcPoK_TXXViwxkPEKdAisDJe5dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df5ef3d951.mp4?token=Jnoj8YMUsv0ud2KGRTrtIfIBWdjjEWyXgEucwc-Bqus9edQQZxFcl9EXSTTHkeetpixCnwy9ar3pI2PCwROB1NGbCueQjDT0pB4ukTZPe-ZU6Cp6mf0noM_ymatM6CV9D-ew1TF_RSy9V4BKB0egSiDop59xnPt9T0R6O6mF5jXzQTULCO8ztZxHZTtT-Oeq6OB2GKJ4zLDXPBqeR8ucOCun2nnxJFY0E7HpOwOC3nbNEfwEZT1Sa9vaKSCH00Fn7dq9wiJ-pUDGRqaI9Sf2hLCGP5kyY-TtNgTzQv7img5ZKJwSdWTh6KAYcRwShfx_bmJwwyxwY_mjh7jd3dx1wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df5ef3d951.mp4?token=Jnoj8YMUsv0ud2KGRTrtIfIBWdjjEWyXgEucwc-Bqus9edQQZxFcl9EXSTTHkeetpixCnwy9ar3pI2PCwROB1NGbCueQjDT0pB4ukTZPe-ZU6Cp6mf0noM_ymatM6CV9D-ew1TF_RSy9V4BKB0egSiDop59xnPt9T0R6O6mF5jXzQTULCO8ztZxHZTtT-Oeq6OB2GKJ4zLDXPBqeR8ucOCun2nnxJFY0E7HpOwOC3nbNEfwEZT1Sa9vaKSCH00Fn7dq9wiJ-pUDGRqaI9Sf2hLCGP5kyY-TtNgTzQv7img5ZKJwSdWTh6KAYcRwShfx_bmJwwyxwY_mjh7jd3dx1wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇫🇷
در پایان بازی شب گذشته بایرن مونیخ که با هتریک مایکل اولیسه همراه شد بعد بازی ستاره فرانسوی باواریایی‌ها حسابی سورپرایز شد. نیمارجونیور کیت‌خودش رو برای اولیسه فرستاد و باعث‌شد‌ بالاخره اون هم یه بخندی بزنه و چند جمله‌ای با خبرنگار صحبت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/30052" target="_blank">📅 13:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30051">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iI4H9mX3KYUktM4XxgxR3aJVLKxatbMilwWlijKE85PPGoL6x9cxAwHTpxaItORQfdM6KG3mxWQPp4xaEIXvRNP06kuYLmATUMWFkfLb1Av21rjvp_KiGCCq_J4HWWUWpCvnIrdxW1UZ_1zRtDh6n0K7T3zleEKe8VMpiuM6LIalgjMWbVL6S6NqeuFjUZVeerSanaNzuyhqTxrFovh3w_Iz75g-iY0KtpKE4gPORQ3bEhM0D2CiYN9WI6VZlJ7W5UBz7v1LI_cIxsU8zIr3M9bw_j1RSVlJgKIKEVtCn1o7uLP_Fj_9kvXzRUhO58HrWQneoKA8GSIWhzG4JFIfsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
هایلایتی‌ازعملکرددرخشان کریم آدیمی وینگر فوق‌العاده سرعتی‌ بارسا باپیراهن این‌تیم؛ آبی‌اناری‌ها برای جذب آدیمی تنها 20 میلیون یورو هزینه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/30051" target="_blank">📅 12:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30050">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6111cc9977.mp4?token=hjJ_J6a0UdRd7DecaKceJAb2H7VZeva6t1ou6p6f-Gc7ribSfgb9H1qvfSJr_peXWE33CUibjxcU9Qs7SJgyIgYUQ0HJc29YQIyERu8BtBF8g9CXu8Fqic4nTa91T5y1Uj-Zr8Jm8My7mBlWwexL7Y2eNjAhuC280Qkpqi0EReu2Sk0A-CX3ycTbtPLDyguN2SucDvnAIbo8ng9Evp732oZ1qS6wuOZ6jVplqCdaKykmgK8nEerj24sER49tzkA4iWU0sMe3PxJDtogsN1ocyqRBZsi_HDIzWDvZ7WHhWxo_bkuggxEWA4a2K_s6zshKdya8upTjCXRBhacuEKTjhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6111cc9977.mp4?token=hjJ_J6a0UdRd7DecaKceJAb2H7VZeva6t1ou6p6f-Gc7ribSfgb9H1qvfSJr_peXWE33CUibjxcU9Qs7SJgyIgYUQ0HJc29YQIyERu8BtBF8g9CXu8Fqic4nTa91T5y1Uj-Zr8Jm8My7mBlWwexL7Y2eNjAhuC280Qkpqi0EReu2Sk0A-CX3ycTbtPLDyguN2SucDvnAIbo8ng9Evp732oZ1qS6wuOZ6jVplqCdaKykmgK8nEerj24sER49tzkA4iWU0sMe3PxJDtogsN1ocyqRBZsi_HDIzWDvZ7WHhWxo_bkuggxEWA4a2K_s6zshKdya8upTjCXRBhacuEKTjhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
سوپرگل‌دیدنی‌فرانسیسکو ترینکائو ستاره الاهلی بعنوان بهترین گل هفته لیگ عربستان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/30050" target="_blank">📅 12:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30049">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlgwwVSknJefbxru4lAWI5GxVBr-NPlHfjsGDcX5chIg3_gqL5Nqmn2rulDSKEmSjF93y9kpeAmjU2VcaL8__Cg7tQsrHbRm69sZ6BWq4epAT3O7_j0erMcBkMw0alGoJQCC700rdu2yo_xdgAOavAs3IDOmbUs7__9LgJGO1LpmY8NKC86ESWJ-L-Z6B5R9TE2liBFoWs15OJn1TeSXvWDzI_w32-D2wQ52KrYeT6hVWCb7y7XSRPDtLGWjl31s85jMjwMdWzVI4od2hkuR_madZMXMntD9CLJ6KjjhJpTeyrSLNZrqp84FhGoThgqT8M7wNktu7Nz25xTODWoClA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آندرانیک تیموریان دستیار قلعه نویی در تیم ملی بعد از سه سال کار با او از کادرفنی تیم ملی جدا شد.
طبق شنیده‌ های پرشیانا؛ در صورت موافقت سهراب بختیاری زاده آندو به کادر استقلال اضافه میشود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/30049" target="_blank">📅 11:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30048">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssO30ULhKi7HGevhHcIZ761pYpv0v5uerju3Kort-7VS1fP3k6JY7f0moIdPPjjNLTsOuymmhVg29eq6IZ2oycfZKDY0-Hb0WSaA9Eba-mVKjq22cEY232R-l9SO2kov8F6-pZTW8jhRKe88taCfnOn_wT3T2Pnkfd9U23xqPmzkH8h0cJjPf601ShEAcTKmrMtchWS--q-ysj6ZGVkZ3dvohbkBRE66jvrjGEy55Rv3t82e7WAgiNQJt8hz6go2Mg4qupze4qjSHxWSZYVk8iJlBpltNEUp5nzKCTeXbCiiE-FBBy_Bec0JIgBlwR4Hv6-RqCIwJ0WjCU7ZJXrVEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جالب یونیون برلین بعدِ گل هفتم بایرن؛ کاش این پسر 19 ساله بارسلونا دهنشو ببنده! کین و اولیسه امروز واقعاً روی فرم هستن و ثابت کردن که شایستگی قرار گرفتن تو جمع مدعیان توپ طلا رو دارن. واکنش اکانت بایرن مونیخ هم ببینید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/30048" target="_blank">📅 11:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30047">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAlaALMLpWntuJ_zJffNLouUMksU-S7fJDdzXIviv3kjBWNLGz0SQJALMUund1yNSFb2_EQXU0bljn-z2VhE4OvpwIxHNIHJE5_KoIgvbZRRFSp7QdXXimA6z1XyVLniF8JhLqV0SEsJhyoi9n3nRb52bLbf9L-V5PN7_97ONhEiMCxtDsoiIyWJcZU6H2XElvPqXpXy3gDiAU5yegSQjCdipnsu_xlGh2_r-SHruACgqvOiXMxtZCIqYX2fJgDzdCg_0-XB-tvQ4R5GCyVgX77T-A4EgLEi-PsZUcppkYWIOuTbWb85em0Ibbi2p9V13lsgNp_2h0FT2YcJpxUuKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
یه فلش‌بک بزنیم به زمانی که ژوزه مورینیو سرمربی‌پرتغالی‌رئال‌مادرید برای اینکه خشونت بازی پپه را کم بکنه. فرستادش با تیم زنان تمرین کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/30047" target="_blank">📅 11:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30046">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Joc4HbUX4dC7Rtsqbc1QaDKQ5b5Zk3qemOaBE2nDlVz9K9pEurVUp-94Fv1je-mSSXNcUUsqneDEzkW0G0OK23oysoU59N3Z3izI_4bwhnlO4uhD1IftdooKc229kap4wrtFdao0BRmpQvPLbHdTnZnZ1sigbBzlQQLKkUnxRuSzXZZqjEqo04E1oUUoT0NelgjLlNOPNiRmt5dtDv_ptowLMP_58E2_I5WgJIRU9WiJQEKvEsoexMgSBoo4t4LIC7Icg72XV2P_dI-CuHAsIFFgtUIYe9CU9jc7utdAAGwrcULTKRe9N4130a_H5wj_gjP-x4rT6JqpfGg8OLpCcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کری سنگین مارسلو ستاره سابق رئال مادرید: خودم به تنهایی اندازه بارسلونا، چمپیونزلیگ دارم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/30046" target="_blank">📅 10:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30045">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIX4MF9cOxZ_iHRv3ZZgztHudlRXQioMHp3AzT4M4jfRUgxdndoBUPYgwtaHPYSO2fEMzz_Msa9NT02tNL02Fnm5ciOQGVMqJC998fO1t3ny20kYdyBLozmS2XDkd71qlAZtYGPEfZ7w5EpVyUVRhaZHXjWN6k_AQ0Anx45IqpK6gi7r9dpvWuBjpkKY-__72s15WalrwX3WMwDgLuD_w9WVTEigYOPuuxnBoyo1a1XbdA_Y6pYkqk0lAfRHdW-YP-Ow15muG-y53Z-ZT56rSiwESOYNc-4ZQ6gHR6yGphpiMdOMNXEUcCcqjuxwiCsdNK5OvYqLBeXu8ARctzwiFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌تعدادفصل‌های‌الکس‌فرگوسن و لئو مسی برای رسیدن به 49 جام در کل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/30045" target="_blank">📅 10:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30043">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83a5244f7f.mp4?token=JCjTA29iBWzviuQU_9iWS1bs4EjoNGaR7CIAzc0aOSZAU2OI6n-xgB3RizIZnKU_7w9bdu7akbOfZ2tltNDHSS8ah09j_Tjqm-oFNy1BqsRhVWOvt2HCuRwaVbCnBgU7DFQXvo2A_NfKh7G8OhD9VwKuzHkHp9d1jiXpJMnbs_OOwzy2q6MF-5D2k8P_z2yV48ge2H8BApkeufD0qWQ1h3wq6KFy-fJLEKauaDlWFRdFe74nPoYWCME0f2pUsvQTy1rWRAddHeXvQXbbtN5byvNLOHgzNQCcf24g-cdSar-fSfWQ5P3BN70J2ZkQRgdwSoppqqtISm7lKEQwLQipgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83a5244f7f.mp4?token=JCjTA29iBWzviuQU_9iWS1bs4EjoNGaR7CIAzc0aOSZAU2OI6n-xgB3RizIZnKU_7w9bdu7akbOfZ2tltNDHSS8ah09j_Tjqm-oFNy1BqsRhVWOvt2HCuRwaVbCnBgU7DFQXvo2A_NfKh7G8OhD9VwKuzHkHp9d1jiXpJMnbs_OOwzy2q6MF-5D2k8P_z2yV48ge2H8BApkeufD0qWQ1h3wq6KFy-fJLEKauaDlWFRdFe74nPoYWCME0f2pUsvQTy1rWRAddHeXvQXbbtN5byvNLOHgzNQCcf24g-cdSar-fSfWQ5P3BN70J2ZkQRgdwSoppqqtISm7lKEQwLQipgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین واکنش امید عالیشاه به فحاشی ناموسی خداداد: وقتی گوش دادم. دچار شرم نیابتی شدم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/30043" target="_blank">📅 10:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30042">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIhv2dx0Fw3NnbWqO-9bnW80jnel5UaHzLQztHKppzKzNFgZcWkQ1XLpLMHm3sOiP2aLS-Ons-bMUfzh__02eVCiYq0keDQ2csFCXeuCyix3ZTG_lRsPJd0g9Moley2VgezsVzv_mPB8wjzHUk-sA68rjgyh1kZtyJXBnTJDbf6MUbHBSstVr0vr4-PhXKN9E_HibExP-TMw0jI3M07a0s3812nOhmP6uTGGgws_QiFmElPV_Na6o8BV3z5-REuElrVSIn4e9dOkpzx8O2nqQQg-zhBsUvROv-yTAx9K8DHo6YYGnkoJRgv_DSZg289pBOVmF51gTJ5Ba4ccYZ6agg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
🇪🇸
🇧🇷
ادعای نشریه NC اسپانیا:
باشگاه رئال مادرید بار دیگر مذاکرات رسمی خود را برای جذب عبدالله اوزان ستاره 17 ساله مراکشی برای رقابت با وینیسیوس جونیور ستاره کهکشانی آغاز کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/30042" target="_blank">📅 10:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30041">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwgYD3HdLxrwn5dE04TIYsQSndIZZKVpyzEZI_ZhoDCJwyuvTAA0U7vNojxcxR_H9FowBDHUe_o02jUFr0RUTxW6DfqN2-EOrAfSMxanqP1vYaNJ_AtPOIfekcN6EPeaBDQsmqAgJ4m-HLG6NGJLCVO3nXxru1PN2Mk34anKTIB7uAW0AoRYC4k91kSZka8uiEM1JkssmnCpQvSEPbYdElMXNVpmJyZ95iLJWzNeCdf9rJHl3PdB4GTpNnYGD23PJNWJEFPfvQ0SfwWjurbQQ56-nSvL_SPK68TsfxW89wj2ky8zvKfmuAp6MgzCn6L6LJBNEPjRlWjddd_BqDdq9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
یکی از مدیران باشگاه استقلال: محمد خلیفه و حبیب‌ فرعباسی دو‌گلر تیم‌استقلال هستند و فعلا هیج برنامه ای برای جذب گلر جدید نداریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30041" target="_blank">📅 09:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30040">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjlVuBBMMW1HgTiugD0sDRvq-m9ZPkHV8Khk7-jOgVWN2DIH4OO75hnih2A01WmxdlFA3vow91TXdIWjvOcNHZZaNzJvY8Q-WZRBc0TX6_Wb64FWPeO8mlgHhEE1DtVQRdPUTrUQmg57hLdG__fOw1SiwjIgUnKXSlHV3M6rVnAcDG7uiA1E2qKDMHZLL_A90MXHc2TUsl1r7Ub3ENSulbAKOMkn0wSkGTj6efPyDjeFU9hhpMm7-LEMVq46jLNjkmULSqmaEXN4v-q7qs0BEWSOllziWZCFnYGXG4u1m5SSQY8q8LTiezxXDcutpCj-CjSHl1XlhjI7wDfGpI1XJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ محمد قربانی ستاره‌الوحده امارات امشب دربین دوستان نزدیک‌خود گفته از وضعیتم در الوحده راضی‌نیستم و نیم فصل یا با پرسپولیس قرار داد میبندم یا استقلال؛ هرکدومشون‌پول رضایت نامه ام رو پرداخت کنید مشکلی برای عقد قرارداد ندارم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30040" target="_blank">📅 09:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30039">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135cc26708.mp4?token=MGwvazXaOTO0J1gWrJAXAsaSDn6GB_X3f9KXtPLCmXSGFeUah1t8WSkPfpfewpm98C8JXXYqdOZrs7UgQ6lXymQ0ZRBdKNfGSH2PQd4d69C4XcqgWhVtDcAPioTWEIozlDMkmEWIBpIYvBxUFci6_qDV04QZLOmOyy7CQiLdhHhysWXh1nHV9X8AlGqrvR736HoDXlb6i-OfWAMU6T_Z0ldEg6E9TxCGOB7iBsz7gtT51Z4GbtOyaM68AqfJ2-9NRFu80XEPprhe1bHH4aiIAeTfXiXaClGUnXdttOWObn5wqESXc_t3EXY1u5UxEP9YNLrh-79e2tOEicFBTPQnuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135cc26708.mp4?token=MGwvazXaOTO0J1gWrJAXAsaSDn6GB_X3f9KXtPLCmXSGFeUah1t8WSkPfpfewpm98C8JXXYqdOZrs7UgQ6lXymQ0ZRBdKNfGSH2PQd4d69C4XcqgWhVtDcAPioTWEIozlDMkmEWIBpIYvBxUFci6_qDV04QZLOmOyy7CQiLdhHhysWXh1nHV9X8AlGqrvR736HoDXlb6i-OfWAMU6T_Z0ldEg6E9TxCGOB7iBsz7gtT51Z4GbtOyaM68AqfJ2-9NRFu80XEPprhe1bHH4aiIAeTfXiXaClGUnXdttOWObn5wqESXc_t3EXY1u5UxEP9YNLrh-79e2tOEicFBTPQnuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌سنگین مهران مدیری درقسمت سوم مرد سه هزار چهره درباره فرهنگ سازی تو جاده چالوس!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30039" target="_blank">📅 09:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30037">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ac719facd.mp4?token=FRaXTZF80vi6sUqFqsil-_uSLEM2iwPY0klFe23UF3UH5n9IpUX2LCBNpK0j1JvKjBaTUog1YZqCTj2jNms8yHXrJQx8u_Ak_MRkHFeYXktPtXrzfsh8OXL9UGnGpBAVRx4jYRLTsHfdPHANH3dqY3aUIT3C2q_PmJ94EYSGM5c4eSTFphtp_0uRVTj6Khk9DCpbarcIuv2RUUbQO6uTm1eFbI2ua1KHoyab7SQ9_syaQ252q5lds5A0niumVzOT8rrNXVCKdstrC_eGuMeuywDKvqPkIZaNffvAx3vBJFDeTsdGwdDRkDzZWh2LudN82tnFHcZthRo6nvCZG_v2fKR2_T8LfUKZj6erO4_ePUjOhFGIkQ8yMUowRFUPSBz6hLj1sZrDxQ05YbkkBKtwuFp_6TDjfKWKuDsx7J5RI-6BhU7IQS-9bcZtb5PLm2LTj4M25GGKU4otO5ly4OJtuJPx-wodGeCamrzIU6vNq2ranBCel6I01kQLXYewINv4DirZa8Iz_rNB-02QVVQ2bFgqlvlg2TU7xvAFa3qmYqr06TLttzvCW_AcF0SmZApfEzzeyeONLGTPFiY3tFMn-Z8Htv43vxpFYy48DxYABdYS4w2c_jDqYwrvpaB9wzHqWxnWMlabMEX9tWkIpoemhrKl8WmXawF2nTZMaJiv62k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ac719facd.mp4?token=FRaXTZF80vi6sUqFqsil-_uSLEM2iwPY0klFe23UF3UH5n9IpUX2LCBNpK0j1JvKjBaTUog1YZqCTj2jNms8yHXrJQx8u_Ak_MRkHFeYXktPtXrzfsh8OXL9UGnGpBAVRx4jYRLTsHfdPHANH3dqY3aUIT3C2q_PmJ94EYSGM5c4eSTFphtp_0uRVTj6Khk9DCpbarcIuv2RUUbQO6uTm1eFbI2ua1KHoyab7SQ9_syaQ252q5lds5A0niumVzOT8rrNXVCKdstrC_eGuMeuywDKvqPkIZaNffvAx3vBJFDeTsdGwdDRkDzZWh2LudN82tnFHcZthRo6nvCZG_v2fKR2_T8LfUKZj6erO4_ePUjOhFGIkQ8yMUowRFUPSBz6hLj1sZrDxQ05YbkkBKtwuFp_6TDjfKWKuDsx7J5RI-6BhU7IQS-9bcZtb5PLm2LTj4M25GGKU4otO5ly4OJtuJPx-wodGeCamrzIU6vNq2ranBCel6I01kQLXYewINv4DirZa8Iz_rNB-02QVVQ2bFgqlvlg2TU7xvAFa3qmYqr06TLttzvCW_AcF0SmZApfEzzeyeONLGTPFiY3tFMn-Z8Htv43vxpFYy48DxYABdYS4w2c_jDqYwrvpaB9wzHqWxnWMlabMEX9tWkIpoemhrKl8WmXawF2nTZMaJiv62k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌مهدی‌مهدوی‌کیااسطوره فوتبال ایران و باشگاه‌پرسپولیس‌درباره‌پیشنهاد 2.5 میلیون دلاری باشگاه چینی داریان که به آن پاسخ منفی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30037" target="_blank">📅 00:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30036">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIFBKtHTRDs7aU_1KvoqQSHF1cacWu8hNvj_Ez7UcKXU3Tr_3rZ7NprCr6hxGoFwnMw728UBI16-b8QDde_7d5b8Ktq-XUtLnsQ9fWHt0tynxnC2jz-yrF_Ift4-tTw5IDBirpNRYFzJTf8LTdie-7WmXKhd5yeSdPcWJs3ByTB2gU2XdYeYaOTnwP2eFE5wbqfGQRkerY4Hdh0RvCToF-CGoqmNTW65Y9zTZYd8orzvmsQGrr5AcB_OC6mUwCisAn4ZhBrylyn6khvvcgVLNjVYPpfxXR21VWVlrsgtFFOsGGXfJCeVTJA3l0NhowCF7x0KRuJV27GNJpErWsEGdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ دوئل‌تمام‌عیار یاران دیبالا vs لائوتارو مارتینز برای صدرنشینی در رقابت های سری‌آ و مصاف تماشایی شاگردان فلیک با سویا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30036" target="_blank">📅 00:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30035">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7MPn0wJWP4Onu7UNOyzCcUZdfkBStedbZYptlqVyo_Var2NyWyGhU-rJHs3LJ4tgnlL7k5cgrspHosn-vGRrSMU2zlS2Inb_rC8Bt5NLtx5hbaTfGQDTeX1pQ8lkxytxyTBpyd4X656uXhipltoYy6cHCZlcDSQjBLClSN4Jkb5m1O4-iKnwuQMZcGZ5TBRpzet8iMTROqL9rqAnoiXuwd2fRXnd1J7w7p4aTgLoZThyRSlYKDOKQ9daDnGRoVsa1VrtignucHMZl1FeGwdWdAMYrYPDXMgyKaIjhHp6f5apvSnjUYHhgzkWK-drPJ7-y9xKa5GFu4PGcScaa6mOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از نمایش ناامیدکننده یاران ژابی تاجشنواره گل‌مونیخی‌ها درشب هتریک اولیسه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30035" target="_blank">📅 00:56 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30033">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‼️
#تکمیلی؛بهداد اقبالی مالک‌جدیدتیم چلسی: از کادرفنی‌حمایت‌کامل‌میکنم و هرچقدر نیاز باشد برای این‌تیم هزینه‌خواهم کرد تا به قهرمانی لیگ جزیره و لیگ‌ قهرمانان‌ برسیم. به هواداران قول میدم چلسی رو درآینده‌نزدیک به جایگاه‌اصلی‌اش برمیگردونیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30033" target="_blank">📅 00:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30032">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTHBCnIlFgSy6a_CyurjN5dRsQAMCjpS5ZsSq4gvWe07bS92dc7IlhHo2MHtwNYrK2VVElD1guxckQePiLDKqNd4DLl9opuCJd0yx-3lOGzp0xO3e3wz-ceZ9P60RzjLAhhCiIPBv3m7yj5L1oMO3gD2-56R5xxj4-ym2oINLQriNCPLghQHApvxpTolfydElaMN2sFUSHLKJnMzOOg0GuoKMkVCRWU2BrPR2MKp2oMkSVqsrHOyjIGn0XbXILdCQkD0UZSLpbWb14Aro20GB8OYRazxTW0vPDdGOx-qmhM1kzgqEn4Y-ycDfyGpsHQC4hHBslEcbK7ibx77gFViHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال: دوس دارم در چمپیونز لیگ به رئال مادرید بخوریم. برای‌الکلاسیکو 3 آبان بی نهایت انگیزه داریم و میخوایم یه نتیجه تاریخی رقم بزنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30032" target="_blank">📅 00:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30031">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بایرن‌مونیخ‌امشب درهفته‌سوم بوندسلیگا با گلزنی هری‌کین فوق‌ستاره انگلیسی‌خود دو بر یک از سد الفرسبرگ گذشت. حالانکته‌جذاب‌این که در 100 پیروزی اخیر باواریایی‌ها در تمام مسابقات هری کین تو 97 مسابقه تاثیر گذاری مستقیم" گل یا پاس گل" داشته. امسال خیلی…</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30031" target="_blank">📅 00:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30030">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufjzT3iMtJH_w1cKPf2Y5hQb6tCcWrAkYUKl9NrMfS8jWviF8iOgkG2ZGmOXCsQJU9DhS18HCRyXs5MYM-EHPQT_YuDSndOHdElu55tLg0PKJJdQYNc2oFOIBkuSAcLLlxMaGcdYNaHfFipn9OYOKKzvzaRydx2ESvJm01C9j0DEHBRr2wuTkuzdock3iByTrwAxywbybKfmgjQQLG2F-ohs4WZnMgoh7RyaEpUshmDA8niPaKGGkiyP7LSFkTRZ67X6LyUdwTtXQNRj5GZntiOrIh9VDeR6luUUxnTRwFGa2mibAHbKkRuGxTrAKEBok503ZalgU_Byx8IfetBaFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سهم‌یک‌امتیازی‌یحیی و علیمنصور از هفته هشتم لیگ‌برتر عراق: دهوک‌مقابل المینا به تساوی یک بر یک رسید. الطلبه هم با الجولان 2ـ2 مساوی کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30030" target="_blank">📅 23:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30029">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCvDT3RWH8YiE-EWiiGT14L-DPmj6f7Jfnuerq_-aKgQqoDLMexb8FJh9FlfdmpNMwg0RbBxeks6ar6yzBt3Z2-VxNfVdLLTr9dFpQb-kxajUdlzZHdsvGeihjk2dEzH_WImmVuA_DJ2p251dJhn65ul5McbTVlckfyR0gsM8BxoHiT80lsujuIDPAGtPbT9saS1gCiwWPLXOo3rdpTK2uVgdghb7r26cvtigCjPRHURubyjTE6Jxb1JlVr3x37vmET5H-wUSgrQOpSQfUoZWL8PRk_DMdm4cUG5OdfoPGGyjVkLmkTTalXQsp8adkfe_B0twSyPpErPSQIVf7HGlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج دیدارهای هفته اول لیگ برتر بانوان؛ استارت پر قدرت استقلال، پرسپولیس و سپاهان با برتری قاطع مقابل حریفان در ایستگاه اول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30029" target="_blank">📅 23:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30028">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5df38636e.mp4?token=tYArVQ8i4OxdCswQc-7NK0gQy82i62Rfa1724bVxWip_7fSuz3CsHml4Bp0-QkAtjVDe1t57G9Zthaoit-O5Z7QdMAIQWmixgX9DGpKpVhrQHM-WjhyJSFDLyyYAcWxZo5xUo3TSTb3x_E1FvVcrjG0j1QhpxIxCtvVsURGGys_qT3IFzQRF9Y9SVDP2VqlNiMKM6PlvjB3Vg0PZAWffhRhuT1ZDn3_CPYJ4SAmeRD2W4tauXtmn_30hczProWScRC4AaRhCo31DrWytF0y61LaqixEnh7zqr1d16MQ_KL8V4z_Xq450YchUDj3ph6ReTXv5qVfLdThOO1yUV6a1Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5df38636e.mp4?token=tYArVQ8i4OxdCswQc-7NK0gQy82i62Rfa1724bVxWip_7fSuz3CsHml4Bp0-QkAtjVDe1t57G9Zthaoit-O5Z7QdMAIQWmixgX9DGpKpVhrQHM-WjhyJSFDLyyYAcWxZo5xUo3TSTb3x_E1FvVcrjG0j1QhpxIxCtvVsURGGys_qT3IFzQRF9Y9SVDP2VqlNiMKM6PlvjB3Vg0PZAWffhRhuT1ZDn3_CPYJ4SAmeRD2W4tauXtmn_30hczProWScRC4AaRhCo31DrWytF0y61LaqixEnh7zqr1d16MQ_KL8V4z_Xq450YchUDj3ph6ReTXv5qVfLdThOO1yUV6a1Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نحوه وام‌ گرفتن درایران به‌اینصورته که میبینید؛ تیکه‌سنگین مهران مدیری به وام های کلان بعضی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30028" target="_blank">📅 23:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30027">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4323ee05c8.mp4?token=bLYOMo9Sy3MiRK7o983EsJaVmy5i5bTMjOVAJmzOXxCm3mLo5XYquu6-w-oIwVJZKOxFxdVUT7IeKvfyJIDpET32qussyd2F8k4kNNvLvsrt6X3Slk9NdyBS2RiJFeCU9ivWvBy7ShE2dXOv3VomcOkBkS4_QFAGdZ6N8IyPA4VisyObwG6pitkW9J-M5yq6LdxtSuc8q2b2wLqdRY8-SN7X6lDIgD8OUskbeBE9FFHmuI_CVqqbGyeWhuDSMIE0-9a4PjiMY2WVR5jKuf7wB4QsL-aRIEkvBTLmJMwpWsnk1_L0QwXK61QmQFfSVCnvz9nzVJoqyMCHNloqDoAAOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4323ee05c8.mp4?token=bLYOMo9Sy3MiRK7o983EsJaVmy5i5bTMjOVAJmzOXxCm3mLo5XYquu6-w-oIwVJZKOxFxdVUT7IeKvfyJIDpET32qussyd2F8k4kNNvLvsrt6X3Slk9NdyBS2RiJFeCU9ivWvBy7ShE2dXOv3VomcOkBkS4_QFAGdZ6N8IyPA4VisyObwG6pitkW9J-M5yq6LdxtSuc8q2b2wLqdRY8-SN7X6lDIgD8OUskbeBE9FFHmuI_CVqqbGyeWhuDSMIE0-9a4PjiMY2WVR5jKuf7wB4QsL-aRIEkvBTLmJMwpWsnk1_L0QwXK61QmQFfSVCnvz9nzVJoqyMCHNloqDoAAOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
ویدیو باشگاه ماخاچ قلعه روسیه از شاهکار تماشایی محمدجواد حسین‌نژاد دربازی شب گذشته؛ تکنیک‌ و آگاهی محیطی حسین‌ نژاد خیلی بالاست سریعا هم تیمی‌اش رو در موقعیت گل قرار میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30027" target="_blank">📅 23:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30026">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDCjDKHooLCUR9cMUPXRwqKK_Yn1pX_HAQWsVXqJWOcJ9lHxuWiTfJSlFY-zRCawtgxXuTcFPTB1DmigAH-dc_H6P4fcaXIJTJrdk-uzPinwQ0AxjN_FNczk3sFGsOad8xR7D-CIhpKE7UR5pjyM80U3Q2io195J1BQowGMr5dKaeLuijYE7pL93cICIL5iR0BV_Evp9_hPkpzjO7SPHlRNtCPjWvm2GQMjBr0-sNpZLk1LOhiR0yz4aoMH5bq2OGveeswbK4uVt_EZjGoCy3xFNdLYQ_ALGfgGodtdlHG4LVYICvjnnKE6_kP-wCmhYAhQktCLG6CZFDtGLOyWYCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ بااعلام مدیربرنامه‌های داکنز نازون؛ بازگشت‌این‌بازیکن 31 ساله به جمع آبی پوشان منتفی شده و این بازیکن به مدیریت باشگاه استقلال اعلام کرده علاقه‌ای به بازگشت به لیگ برتر ایران ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30026" target="_blank">📅 22:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30025">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAV56BNtU_6hoPFNx5Rafaq6YiFKPz5tI6jpGUXUmfi4_FmObbPtV8hvIBXYU9AJTgidWBvyLQNsLSJ5IxNzopQ_vPbzKmKi-evhnkD31uEK5XLYcvojxnU8P2bxGHXfSDJwVuMz19g7T6t7pxFLM7MHGc3wgkT2bxvpccP-ww8ilkn5NJWMNDN-uRQ5dbditWNCqgXx1l8nYCVkj6OMMhtVf4UlOWdo3Xe5cw5U1TeibPf6m-11eHHj4nwy5ay9fE1HMaIelah__p-JX1FCrNYiAUROnmsh9OYswLz6lkN7jc0xx1PHvFJgPvmN38hi3U9I99Bj8vygfJ2f9XNzQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه‌اتلتیک: جی‌جی گابریل ستاره 15 ساله منچستریونایتد تصمیم‌نهایی‌خود را گرفته و بزودی با عقدقراردادی 10 ساله به رئال‌مادرید خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30025" target="_blank">📅 22:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30024">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqr7iG1CYVSS9cE9WFFKlr4UaZXcNpY0sGI557xsR8juDOL02arBuW68Ehubwla1_IETT61DfaE2fG-aKUIjw268vW-BGtnfADKKpbMLlFT_TW1XDThP4MmwwSbPnVxro_7vsHpAsygx6pCu_fDKmW1VvzOVpTmv727DotOiF0oq_gfO7ExbzwMU7B1dRx17QxLBOKT9-o_vNP5X-_O7hR2Tkbbhyj-nGY75tyTUCZAJH6gCWS2hX-ylcGiF-xbnSXUTSVCmjfWABmQjsXS_yNgOFrr3D9-zQLsnhITqZWGb-5rOUEYcJ5HqSKVoyqnVcMF2Qil_1l3HkT36d0yGkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30024" target="_blank">📅 21:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30023">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8gYIGDS4qHsx3OmyuMXgmh6iOot-XmvH15DativjmnLpH1hz_ag8rUVUDnj-lvaH2qCkDfSorY-igE4kW5pBVqQkjlZSMgO12BOVjUnDXYZsv2QpWq1Sg1Q9VyH8DBSx2BaBcASsm8THnLN8TOO2pbq-9MLvSjijIRqbbfc-3B8vcFArB9V0veCIcrrWVrtXc7QvTbkg8sUkm6riAytiybowMMbZwsAkULZ0jjReAHynzH_TWZUTSvhaSZ7UDQKKY19Q5sQ7fJIy18nhl-mbesaZMNPKVbSMySpbDnqk_qqFbbUa2vdLFjqeych3mzkmNr4L-IAcdY0Gch236ChjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
خورخه ژسوس سرمربی تیم ملی پرتغال؛ کریس رونالدو اسطوره پرتغالی 41 ساله تاریخ رو برای فیفادی پیش رو به تیم ملی دعوت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30023" target="_blank">📅 21:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30021">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRdRNBPEkhDxL5VJo-rfHiCeU-n9uY8C5PzRyvc6tRmGxPcf5N62ad051rTmYrqtJ5iBj8JQLt6vlotkrjnk9NrrXWo3RyjvZIs17A5SWfKdEmv9OtQu-6OSNg9-4e6ana1CnoX_xLhIy5zbwoh-PtApdKN2AKOe9p07g-KJRkdcn7iXM5IPcIbsDCaALsnOEonfNwnHXiM5a-XestkHblGDDkQqjfZ116_DN_b2RtIx4A025_Zq42-G4T9hiMQq4bxY4-KnCK50sLaTm65WiKtcVGx8fSXmBMTFD9n2LZ80dPHvt-33aKemhWmtHHfKIXzx6DW1c8cT2QsZEx_oIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
دوتیم بارسلونا
🆚
رئال مادرید روز یکشنبه سوم آبان ماه ساعت 23:30 در ورزشگاه نیوکمپ اولین الکلاسیکو این فصل رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30021" target="_blank">📅 20:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30020">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🟡
👤
سه‌سال‌پیش‌درچنین‌روزی؛
حین ورود رونالدو همراه با بازیکنان النصر به‌تهران این حماسه تاریخی و فراموش نشدنی توسط مردم خونگرد ما رقم خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30020" target="_blank">📅 20:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30019">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVeC5NHiGFv43Rifr-X64kX6nQCiVILLXxYd1O8qHVE5EeQqP8R9UlESCU8nWz5P1QH2bs8ImCFaAZ5Ian2NFFTcHOhAPWQvKQso2FPbPNOI4yvT_F815ruDWkD0oRRiQrZ0sZ5zGP7Mj40HYSnm3BLmPtpPhesyNbeHAJDkIYJ0PTLrQriPpDd7ATFI5VcQZ2pZ0zEZTVC8j-RxwpWzdnUkOGbFg7uc-9tXCRtcHLnx7XXsL6uJw_4dZCFZ8HZh4wUicNpJS9DvcjUd0KzE5ACe7LOU1AyyyvsgSjEMhdUCdzBWnREFziKpF1Z3Uqp0WyukrsadAAFQh9KMsReMKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری عجیب‌وغریب علی فروتن از سکانسی که باعث توقیف کامل برنامه فیتیله‌‌ای‌ ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30019" target="_blank">📅 20:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30018">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEczS7XzWh-ZsuVqyP2ohy4MfVeWzVISO9qmo_mblxqlft_FFxjGJDLRBoYU9OppA9hPLdppYKs80Gigwk3DjsSAkyU5MVKC6z4WmKlt3vIesUwVgATKCBmbkN-cbD10vBUl8THALErAZkQ_8hKaqj3wtBzqtxP6Hy2-fXIRuVZENhoLvsbBuoTzaKoIjfZy8PsO-dptbU5VdczfsQHCh7erD9U0bxhMiw_oVssn1sqpVkE88PY78zcUA1tEL758YXv-yoU9rhAJrnCNZzMLMDISHi4F6up0AYT_egwiCzcigwPJWk3MYcmnQeHXVADQcRifGF5mzs5ZqmglLsC-yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
فدراسیون‌فوتبال‌فرانسه؛ طی ساعات آینده زین الدین زیدان رو به عنوان سرمربی جدید خروس‌ها تا پایان رقابتای جام جهانی 2030 معرفی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/30018" target="_blank">📅 19:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30016">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U0VzZA0K5YqTRCcCjLn50hvWj4TFRTQxuSBe_edzxtg8TsqBSp18M_GFw_9KMe5ugr7lVFlXUQmIgdEN16_TZSSH1vTVdbOWZ2NJPX0DZ4XLOhkt5HAZCjRMpIEkMILRut4vxt5AR5fyKEwAXXFRfjHpRWqMS9naqtt0PD0Tz3Of0K9YxRzwJaHDaDTTZyuXaFiPylic0AAg-ayhkVxVppqG6qrkSDZ-9_MGDMDO20dtfgiqBTyE6yuIiTNTQaJZEcKq7rY50dm0dTR_8rM1sDYrtPD1yJ8D8DaGXg7DIYPqRENcT3Qwi6oynj1MNYsCd5XawmK8MG8-RWZGaiRlwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tbLJ97TCF5CKX5Lwh0TVxxJaTAJNzsaVzr-R_3aDTCDzwaOG7s9lIW57ktnLxRIVpmo2-QrmPvjIY48CspNkXeRBGPV5JFLyD3gvjUHQom333jDG9TDzlFi9Y3KzPRKGVmK4AIwUslk0ChBnHFsc358JJvZPksdf5902p8KG2PAQPSR_2wnqzs8biSO7QM3odyvNo3Kwfz4t5XxMJ1oxHqrqrrcJDgFKlt37UcrObS4RStcwAHhx8lxq2k42dUgmb-Y1htcdkybLiprWq4-vhTiKqH9SzqE8Vq1zxvRG9XRU1NfHeBa1cRK5CAwAeNFrN83VthT6_xLhEgZfcelStg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
نوزدهمین‌دوره‌لیگ‌برتر فوتبال زنان از فردا رسما آغاز می‌شود. رقاب‌هایی که به‌نظر می‌رسد با حضور تیم‌های اسم‌و‌رسم‌دار زیباتر از همیشه دنبال شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30016" target="_blank">📅 19:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30015">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a036b864e0.mp4?token=cNyJ-r9oQPmlZ7G9f_XpfZwhhh26KpRnMFbtDFexIfH4R77p_INUsQa-a5r8CuSR84jL6E_OhgA8vdILFaa19PB-8w_BujmLvSXjhbDZiAQ2zza66wqRDeDe_mBsC-dtG1ix1khvFNLjVrY1JrEgM5ZnSOxO_0YoNn4VHRS9lgGgpMaqlWelDL8pVIwrT3zAhZnc9BdjplApRWzCNQDbNsmzxG1Dz2yUWMbVfaUp_Qf5FicziUsBNZNrANo2ijKfNERTTKw6zQi72y-wfIGG3gAedrUth7w_zbvjv_L8S3agNHduzzYlAuHGI8o80I0gMPKHnyGOIY1OHRgdce42RQselpnFfbEgM0yxuu1UoLndBZ8sj6xn50kKcp6KY8yp2PNh6GTbbxou49yAjjhzwtYUHxrGGeaaVGdf2Kcp4Mylk3efjFauy-Hffi47CgPDPbKuE8s4kJJ8bQJRg_92L-JudGEAdE0m-skFEBWnrQZf4bMuzDi8Citv4cy4fdEWEDMabZn-4ZUKsyfJXFdl3zpAfVIos4WhG4SKywDLSPkUzaJiETaLXMcr3p7BHzJO7nOvQtKmKGyb-BmrICf6_O51iT4M_4V_yaGFKS3jRrKXK_Xod2pTHfgfgkPXOJMZelV21B7vT0vLbSFZT3sxvuNFQ1cpcvrMExGVpV_BQX4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a036b864e0.mp4?token=cNyJ-r9oQPmlZ7G9f_XpfZwhhh26KpRnMFbtDFexIfH4R77p_INUsQa-a5r8CuSR84jL6E_OhgA8vdILFaa19PB-8w_BujmLvSXjhbDZiAQ2zza66wqRDeDe_mBsC-dtG1ix1khvFNLjVrY1JrEgM5ZnSOxO_0YoNn4VHRS9lgGgpMaqlWelDL8pVIwrT3zAhZnc9BdjplApRWzCNQDbNsmzxG1Dz2yUWMbVfaUp_Qf5FicziUsBNZNrANo2ijKfNERTTKw6zQi72y-wfIGG3gAedrUth7w_zbvjv_L8S3agNHduzzYlAuHGI8o80I0gMPKHnyGOIY1OHRgdce42RQselpnFfbEgM0yxuu1UoLndBZ8sj6xn50kKcp6KY8yp2PNh6GTbbxou49yAjjhzwtYUHxrGGeaaVGdf2Kcp4Mylk3efjFauy-Hffi47CgPDPbKuE8s4kJJ8bQJRg_92L-JudGEAdE0m-skFEBWnrQZf4bMuzDi8Citv4cy4fdEWEDMabZn-4ZUKsyfJXFdl3zpAfVIos4WhG4SKywDLSPkUzaJiETaLXMcr3p7BHzJO7nOvQtKmKGyb-BmrICf6_O51iT4M_4V_yaGFKS3jRrKXK_Xod2pTHfgfgkPXOJMZelV21B7vT0vLbSFZT3sxvuNFQ1cpcvrMExGVpV_BQX4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بابک مرادی هافبک سابق استقلال: واقعا دوست دارم زودتر بمیرم. خسته شدم از این وضعیت!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30015" target="_blank">📅 19:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30014">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/595b48aa31.mp4?token=qCujdzFbYFU6ERBOZMMSLjn8qY-ZL4QNHRi8fNt5mwlzjV_k-eqMaPfUwPtfC_dDVcx8NOoiO2qqiyVtrMBU_im9jNer54oUfunLNhgWoVL7dGuqWOHZWfA3KtzkSCDQVh-nP-P8SIXbfKPbDqP6MZu-NwvX7qaAM1mi6irqPD4f7VNHi3IvM69ukV4XdexEfxHtsxGUkpIvFT6A4tzNJy_deRzd-sD3GJgZu9ZIq3i4F9schU_G-n8aX7ZvPYYAUpmhBK30_RrqTGUr8uj_7ore3PbhNg8lTVzVg_NYOKCNQzTI9vgLEqVYAmBJkmP96tFK0v5rbA7vRIZfBgzXnTOlGLfzE8ZVQtMxREQx_7jOpvTLCT1nmRQIMwX4_wYjujqR8E7iJrkN_cXIPGoR5JJVF_FQNdXprZgl5w_fali-UM5yG1ojLB3sGTcZ1tzadUqHSPxqr1y-94c7jlEH7d9gyKXxmECr1-nDJn2S9C8O2qeheZdWsvHJKuGQx2xYBg8FMAVPsX6GlEI-mw48RCx6AKwKUgiSvvwQOIFetqaHZ39eLYNNi583GLidKrgI2_W_E-0LXmE10J2P__Lm8tq90vGdSfFOXAkVGA4jkmIWu-WR3F2Cf1y2pOJpy9Q30xBiNVxfvXcUkWU5VQRqRwdM2QvkbvNw_6ymnQO8DRY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/595b48aa31.mp4?token=qCujdzFbYFU6ERBOZMMSLjn8qY-ZL4QNHRi8fNt5mwlzjV_k-eqMaPfUwPtfC_dDVcx8NOoiO2qqiyVtrMBU_im9jNer54oUfunLNhgWoVL7dGuqWOHZWfA3KtzkSCDQVh-nP-P8SIXbfKPbDqP6MZu-NwvX7qaAM1mi6irqPD4f7VNHi3IvM69ukV4XdexEfxHtsxGUkpIvFT6A4tzNJy_deRzd-sD3GJgZu9ZIq3i4F9schU_G-n8aX7ZvPYYAUpmhBK30_RrqTGUr8uj_7ore3PbhNg8lTVzVg_NYOKCNQzTI9vgLEqVYAmBJkmP96tFK0v5rbA7vRIZfBgzXnTOlGLfzE8ZVQtMxREQx_7jOpvTLCT1nmRQIMwX4_wYjujqR8E7iJrkN_cXIPGoR5JJVF_FQNdXprZgl5w_fali-UM5yG1ojLB3sGTcZ1tzadUqHSPxqr1y-94c7jlEH7d9gyKXxmECr1-nDJn2S9C8O2qeheZdWsvHJKuGQx2xYBg8FMAVPsX6GlEI-mw48RCx6AKwKUgiSvvwQOIFetqaHZ39eLYNNi583GLidKrgI2_W_E-0LXmE10J2P__Lm8tq90vGdSfFOXAkVGA4jkmIWu-WR3F2Cf1y2pOJpy9Q30xBiNVxfvXcUkWU5VQRqRwdM2QvkbvNw_6ymnQO8DRY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
#تقویم
؛ چهارده سال پیش در چنین روزی؛
کریس رونالدو فوق‌ستاره‌پرتغالی‌رئال مادرید این گل استثنایی رو در دقیقه 90 به تیم منچسترسیتی زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30014" target="_blank">📅 18:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30013">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2ctvj7Dc1b_3hzRgQozHq65oYqrnJqehCamcdfElkwsBf4wQSG3GGbclhru64X3OB-oDhcj3vu7A7a8S9SdPthF5j54AADs0YHKEyFmxvPanpw6MA32cr-DUQcqI1sWYy3BiZeVamDhk3BJHECWIAqMnzt7pX3p8eqPWIMS5sCUbDfwPAtukMrff_5jRUoACRT_SXHW5KzqL710tFwx7A6HcZitQndlcMKj5EtOX7upCKIY2gvo-R5or_0RNxErNEMeFploYHVSxrfyQ2pTHQ8w5JVLC63EUMihehLAlb7IPlkTl7VxupYcee--LTazfk5liRnnbvRTyqYZ9t-ghg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔴
#تقویم؛ سال1999میلادی درچنین روزی؛ تیری‌ هانری اسطوره فرانسوی باشگاه آرسنال این سوپرگل تماشایی و استثنایی رو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30013" target="_blank">📅 18:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30012">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0BaNSEERuRRUQNtaYwHbWWZKYNj5Yiaa5O7W9vGrvpg1S2MXh_D0ltZF0I3rvmV4Q-NGhrsaugsjEImWCCPDtUcKZFfwWlLlYNYnXXQsg-XWH7l7s1sh-00nqcBMAkhJuFEpoFqfKFHLTTWnQdBkyLDPgLcPA3JeYOSkkVhxxFQYpzMK5XlgHQlNKwaw3clSFGPNJgI0-sIOEhRYY7HkhrRreIWz5C2S6iw_ZLavvWEI8VY9FNkxBEu72GjXEZOPfEc8bTHmoUefAFdpa2-6jrCtTTVxS0wdgVldE-9LEY52fblzzToI0aBmcCaGuPMGmgfJT8qQGjZIxMaklfJ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛ تنها خروجی استقلال در نقل و انتقالات نیم‌فصل محمدرضا آزادی مهاجم  27 ساله آبی‌ها خواهد بود. مدیریت استقلال درنیم‌فصل 7 خرید خواهند داشت که جذب قایدی و حسین نژاد اصلی‌ترین اهداف هلدینگ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30012" target="_blank">📅 17:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30011">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggbDjQ3N7_eo4OHE_1C2c8POkMuzWgg_MdX-ZwB3ItRLRThDV_mR-UUT__IKF64muaOrmif1gUmAe_egthXkpg5VHU4a92ynSBdyNe_bNl51pbOaA7DhRV9AOj-JNJMypg0q7GYnbhD5LdtVC-lQNG5admCKbqWZxMHa9ONddZuiTs3s4raU1zaA172L26ITk1rr2Zud37njjPPOKsToN9Hb3Epk48xRBS5SllBSnPNGqH551kzOl7UiFpEOWVakJMM--i3uG3OTwlEFZMI07KlVRgJ6YxJyVQZWxpTQgHYS7b-EmDbmk5MAWW1xtB7knDwZfXJ1ZnDYIlrQeiOQ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلزنی آلیسا لمن برای تیم‌فوتبال بانوان یوونتوس در هفته گذشته رقابت‌های فصل سری‌آ ایتالیا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30011" target="_blank">📅 17:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30010">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9586b8df2a.mp4?token=H7n9_clRbh42BKC-1YRD3EzrRbHDG0eEW2fycqeZ7TpM_6DoWqNyrpr4k-dlCKdlmvk_PLecv1LGt5wqytgG2TXy2nD-hgVjA_Qh69B-lf6DGN-RbFq1qEHizzB2zaRquiepsZ3bPdJc5Xfq1FYJixUhYwJ-jnnV3DITrSQYCdejCHZwdRgmYlFhAuu6HvMCcuTR2a55hDlQRBjVbE5rP5TDdlgEyPhrETT45AKcVIyBEAMPT-V3qmgNlDlZlNvFWBjm3ltJQV6KHkafEnFS25C9Mvi6AK42Zkk0a6TTi1Zd2K4O_Eb_MVaROfwpbIf2Mg2lwfm_oGGa1JqMgFoXxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9586b8df2a.mp4?token=H7n9_clRbh42BKC-1YRD3EzrRbHDG0eEW2fycqeZ7TpM_6DoWqNyrpr4k-dlCKdlmvk_PLecv1LGt5wqytgG2TXy2nD-hgVjA_Qh69B-lf6DGN-RbFq1qEHizzB2zaRquiepsZ3bPdJc5Xfq1FYJixUhYwJ-jnnV3DITrSQYCdejCHZwdRgmYlFhAuu6HvMCcuTR2a55hDlQRBjVbE5rP5TDdlgEyPhrETT45AKcVIyBEAMPT-V3qmgNlDlZlNvFWBjm3ltJQV6KHkafEnFS25C9Mvi6AK42Zkk0a6TTi1Zd2K4O_Eb_MVaROfwpbIf2Mg2lwfm_oGGa1JqMgFoXxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🔴
#تقویم
؛ سال1999میلادی درچنین روزی؛
تیری‌ هانری اسطوره فرانسوی باشگاه آرسنال این سوپرگل تماشایی و استثنایی رو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30010" target="_blank">📅 17:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30009">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3HThkKzys5BunpwT7fwdmivYNwNXb_ieNwoZrRaj5u7gEqkghVm8kBXr8YG0TLnOddgskG-J7erusNEz9NzjZTE8ApPi8cepIIPkfxgJHm1Q1CG8OSBGnJwBbwdEJz3Rwx_yf7xMcbBu1NHaz7W2GPYK0BL84XSfRyvyQtcTpculqpPeFQD7J90QNNAoBxJTOE6uLCtpetTWCtEfWTK6FhXRWMp5qPRNBkLiJ64NpVFn4Ei7RboMdZjEx2fxsq7-9ycNeOjz7vS5YMzOM0yhKOqRlKKQF3HnE_1FWRqcuHUekirE_enwbUmYMbOW0jTXrqfGr9lnJvGJ8YGwpZ8uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بایرن‌مونیخ‌امشب درهفته‌سوم بوندسلیگا با گلزنی هری‌کین فوق‌ستاره انگلیسی‌خود دو بر یک از سد الفرسبرگ گذشت. حالانکته‌جذاب‌این که در 100 پیروزی اخیر باواریایی‌ها در تمام مسابقات هری کین تو 97 مسابقه تاثیر گذاری مستقیم" گل یا پاس گل" داشته. امسال خیلی…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30009" target="_blank">📅 17:16 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30008">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/656a3bfd79.mp4?token=JsVvtB_H7WXmSE0-F0kNKFq1j0_pgvcC9SgoHpDjzP8PM4eXcWJVHW4_Vlogc5GyGm3CTiKymlnTGKdQbN7MavpRXUyMvqGxcCCkUdmRwFGMva3jv9HIZ2ijdVPS2hnDveUV99QIugu3537jk7hdEBtQmDCPiNuK3J6zlPKL-mUGR-ylp7e97GgaeEqPaMG78K3A7qgJjia4CQ8q1NqttxbjeCe5B2W2ZoHsTKNt1H3R0scXrxmlzS2fL8oS52dPGBt8h9j__gkBSwQjC0EZieQbafusRX_Pi4vXt92vh3teSlf_O3blFbhLa31xLUjsWPwxycpbCmmF7tSFwuX5cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/656a3bfd79.mp4?token=JsVvtB_H7WXmSE0-F0kNKFq1j0_pgvcC9SgoHpDjzP8PM4eXcWJVHW4_Vlogc5GyGm3CTiKymlnTGKdQbN7MavpRXUyMvqGxcCCkUdmRwFGMva3jv9HIZ2ijdVPS2hnDveUV99QIugu3537jk7hdEBtQmDCPiNuK3J6zlPKL-mUGR-ylp7e97GgaeEqPaMG78K3A7qgJjia4CQ8q1NqttxbjeCe5B2W2ZoHsTKNt1H3R0scXrxmlzS2fL8oS52dPGBt8h9j__gkBSwQjC0EZieQbafusRX_Pi4vXt92vh3teSlf_O3blFbhLa31xLUjsWPwxycpbCmmF7tSFwuX5cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروزصبح‌یکی‌از بزرگترین دوهای ماراتن ۱۰ کیلو متری کشورمخصوص دخترا تو بوستان ولایت تهران برگزار شد که‌ چندین هزار دختر توش شرکت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/30008" target="_blank">📅 16:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30006">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rDtifmtRhIFQJEZOblsR2DDuQ_kOQqUZIj_2usg-oLD0Fmg0wAYtzksd8XMjw5BsDvPMs-TrllL4Kb_UzJK6f06_aTZaCsFii8KCv6zp0zIPWRTlumuE6HEnalyQdgxzElUFB4rLkCbpwdoISEQosHE0VfKm3mrQTzGZfRTx2tyYhQdAzUB68Sr9bDLj8CgQxNjsqxEFf3RX2ipQx5IILHy-RUl0jkF4GqOcMm2Xy0LiJ2gOT3JG3Iz1ddSIYRkwCxJRpPai7v8HhalSLIoLpxu5E36m8dY38XX8hx6kvf1D53yk1_iXUo_j6mki3DHUFbKUgxHklttr5NBTMBokLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VsVqxywHQVs0tsmSA8UyzqaGNn-doW_aBKRSUAAfOhZUytXUadLbowOoXOCHEAhUpDBLEPmngvT_xl8cTrKMaPOegIDoy5i6RpEv5rOdpFce5kibJHF9PcIy6l69diY7wOeNX2DiuW_V4arT-v0n0pCL8as1OFRjzSYHTFFU8cbuuNkU_1nC-uVxV6S90A78S68-zinoiwOK5epaGJAgRmRNn7KeUDvPWMgD4HUNHVvB6hyO3y2kh6LT3oGT5mT6sIcCDcH-lPXnuYNfBMi2bXvb4L4kR9Gi5Q6jy0vfrBNC0J4LGcjSMtcL3R2W9SiwPIQkGJAWbJGj-7rygivXvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚫️
#فکت؛ السد قطر تیم 78 میلیون یورویی آسیا امشب بعداز 22 مسابقه نتونست‌گلی به حریف بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/30006" target="_blank">📅 16:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30005">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOtDPuQ9Da7UNzjCv8DoxwVVwrqMBtSTeHOzeyfV3h3ThMRWoWlBrqbjA3ic8vEKINUbWAjs0Yrd6a9awagNPJMyC14kK4_Yf2g7eGuZUIakzsKCaLyW7BnygrKbkqvNPseF_tJy2pQqiyQeNElvgb6r6R5hv80N6jndZdfnaMCFtzR1yf5-YWVMIVhk2vNAjUKo9MQeQtK75_wq25rFfP9mf40BTpG9CR9j_XcdgkNnOdc__XLWfsykpwCnq-DkouxdUor4DZqgd6Fhahem4Df_ll3K4O75rpTVP8Zx9ptXa6577AzjhH1-eSmMopF2AoThCd1P-f_cTGVlEZIvWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#نوستالژی؛ یادی کنیم‌از مصاحبه قدیمی کارول سلیکو، همسر سابق کاکا و علت جدایی‌اش از او:
‼️
کاکا هرگز بهم خیانت نکرد او همیشه با من خوب رفتار میکرد و خانواده‌فوق‌العاده‌ای به من داد اما من خوشحال نبودم چون یک چیزی کم بود. مشکل این بود که او برای من خیلی کامل…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/30005" target="_blank">📅 16:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30004">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdRu82KuiQmrPnm-YOKMaOmaCCHuHqI9c--qQfu50J27CuCMBYaJokWqbOP8nDsp2BGAsiSYI9pCqFbxVXLLeHrudwSg8Z5bYiZFX1Qjzq9j3wjtb99CyxwnllOo52Ohq9v_L-cCmjFln6sT_BBbnAS-JXN39chjWVOFoN-A0FipwoCoowEhsvRJC5s34yLwVCbkqRCtFjxzaJD8IsrSc1kdvTiPGgZ1DMDzs7dERXjCjWTcKKH_7E8mr_aeaFjPLPmU43U9PNClR9QdKAiM8wnP6e-JmOiWGKnqew0QGUTQiTgoJhhM3Z7eoSd62SDDv0DJ6OSIDDohpthj4X-enQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌بازیکنان لیگ‌برتری دعوت شده به اردوی تیم ملی در فیفادی پیش رو: علیرضا بیرانوند، سید حسین حسینی، سیدپیام‌نیازمند، محمدنادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمدمهدی‌زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، حاجی‌عیدی،…</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30004" target="_blank">📅 15:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30003">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Luk-qCl1H3OooFtBPvP93sLl2thGnYBnl7gfDvpQ64P0_iqIutvIADj_j67ime7WDhcsFNWFAAthuNdZuVZUETIqW-A4dK-Xb3B08qLRhmCn80Df93SPRUQ_1kK6Thj6_jGpXhJuYd1boT1l3Q6yzC8DoLFhekslSu1zHBsltbweU_G3-d6vdvSgP1hQVyVZ_i-Fixu85NRL2mcfdUh0jM_2BzZ6mLapeaM8Nx1KPMqGalsbAc1QnqoRsiDDtJYCtoUi1asipgG3vAPkUqPlQjSGpNCWJIBEKdAUXPLxkxSCqWc2HbjGokwwyXzKULqynal8-mW3LiYKHkPwR_VSmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مدیریت پرسپولیس طی روز های آینده و تا پیش از نیم‌فصل‌قرارداد اوستون اورونوف ستاره 26 ساله‌ازبکستانی خود راتاسال 2030 تمدید خواهد کرد. توافقات بین طرفین انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/30003" target="_blank">📅 15:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30002">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5t69XRBHXopB2033akkbFJi0X_HAt4IdWiSk5dWP-H2f-f3iETFH5aHFSyAB07gBSZaRaUVdRJpDuZ6wm49MCFIejG3JebvmV5QQQM1OIdDfPxTFYYwz917XSUiK5QgWL0FkI0VIEMUj0A1anynNDG68bEV99mRwirxpZHXg7KGRhfFFIHzOWzPjz5jTB0IEssXLXREgPLb0aIj7XHJiVqA29r_C6SCAe5MecJIA9NV-OQ28h3umxfGjprJAGkP28ruI3BpkAs7G7WBWigE_dlO6oFf3xZIzPCuUuObZW760OIzyq40P99tujXHhrSl6Kz9-9nDKBeKlBRtrn_9FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ نشریه ESPN: فدراسیون فوتبال پرتغال داره تلاش میکنه که کریستیانو رونالدو راضی شه در یورو 2028 نیز حضور داشته باشه و در پایان این رقابت ها از دنیای بازی‌های ملی خدافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/30002" target="_blank">📅 15:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30001">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54c60e1877.mp4?token=igxOVWfJ_G3ZbwyKHlPv7UnWwXIEOOOJyyEuQqrNVWz8lBx69TVjfkDG3UZazjNZekZ1mLy9nv7oInsCZLKuv-k5g6hfcG1kELukaFnxjywOByYrBsUz4_nJnLc0oe5ejXx_dQLZUfWPnW19EazD5BQ0gD6B5WvGUisL72RdCCKGqfbWZDrTEjh1gSREAe3ahBwAUNupCOYTPcac-5FpbVXmUWNTxugyVR9_MHn41v31kwygolw31l0DuJ8OlRhubTolDZYL-1PTp99Jlme98lH7UwYuvJtbeGpBLgkva5f3JkJEOpNAGjfM8Cqhn-lNObk7Q4JYzJQSROFa4isw1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54c60e1877.mp4?token=igxOVWfJ_G3ZbwyKHlPv7UnWwXIEOOOJyyEuQqrNVWz8lBx69TVjfkDG3UZazjNZekZ1mLy9nv7oInsCZLKuv-k5g6hfcG1kELukaFnxjywOByYrBsUz4_nJnLc0oe5ejXx_dQLZUfWPnW19EazD5BQ0gD6B5WvGUisL72RdCCKGqfbWZDrTEjh1gSREAe3ahBwAUNupCOYTPcac-5FpbVXmUWNTxugyVR9_MHn41v31kwygolw31l0DuJ8OlRhubTolDZYL-1PTp99Jlme98lH7UwYuvJtbeGpBLgkva5f3JkJEOpNAGjfM8Cqhn-lNObk7Q4JYzJQSROFa4isw1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارسلو ستاره‌برزیلی‌سابق رئال مادرید: حاضرم تمام پنج قهرمانیم تو چمپیونزلیگ رو بدم تا فقط یک قهرمانی جام جهانی با تیم ملی برزیل داشته باشم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/30001" target="_blank">📅 15:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30000">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpBCgzKsuA4Mx5ey68ct0qIzExgrkNU1iENmwtq5TmKzxJxr4VwXut7-cqvdBFhsx-Lw5is9YdJTYIV_y-ZntvqcQ8nHTNafnHWgadwYMinhZ5QOzmw98EpQBR3cMOk5QQhHJx4RoALUmpVx74CYRlcwQUrvp1eALt5bE1sXdP74UQTbr8x9UhRxAwrSxd7LsYozrEqrgfAABRN-kHw-ycfYyJfXVjhUdK0vHwDnyCQRWQLR3qY_3zM2psa135cLe-29GafdpwlZS7K2VvfEnhPJdRKnIeEA5cLcM7Jj1Brk5b2CUJf0PryeMSfpJpXEqBxTTVLVWr5vKJV91s25eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‼️
#تکمیلی؛ امیرقلعه‌نویی سرمربی تیم ملی به فدراسیون فوتبال گفته علاوه بردستمزد 100 میلیارد تومانی‌اش برای جام‌ملت‌های‌آسیا؛ درصورت قهرمانی تیم ملی در این رقابت‌ ها 300 میلیارد تومان پاداش خواسته و از مهدی تاج درخواست کرده که تمام این بندها رو در قراردادجدیدش‌بافدراسیون…</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/30000" target="_blank">📅 14:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29999">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GA2J7KA3GnN1550TwqzBwxtsp4GqvxkBOT-ntZPrFWWSkTwwjRdDwYPmRm_94dQbu9k0LPaZ7QPBkg09oTNjQkxkJnkcO4tUm3pHiJdjnHlpzzRKaNY7Zbnb-CXgMPE9KjZmAS_9e2HXouwf7qkYDThtZazmxCEq0h6n9U4E7pCN1PW6KzNW8s70YefEE6sAxwEkzPWQxsdzwOcf6Pj5Dly3W6QHrtzPUlfxaGH2bzUEF32gu0ZAf_0I0s3jypI7Ogl2dszkYRAqLZrbQaKrkL-UDBHu8CuOfx6uV64DtRMkPCsp5N6Ifq3xfd0z6Id4PEBa7dKEPQKgQEWsACybRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔵
👤
عملکردفوق‌العاده درخشان تیم منچستر سیتی انزو مارسکا در فصل جدید در تمام رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/29999" target="_blank">📅 14:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29998">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzKu_fO5WMU1wIXNU2899gCdTekw2Ne0PPiWI17whE6q90WvoY-ixU53nmsW9eHdpjYVanKKy2rrZDlkScf3oUeuHUINWV-KRmXTryXcGTAj4yDFkAmake3oNYzKP1an-4_xkJlQgPqhhBf53mIxgff2eD3fISjql3c-vTjZ4k-gRwPs6oLlnSCGK8T2BOLHjqeysmTbsF4vdt4tTYjG1O5rBuYqN_5q4tlISxhDHhPSklp9mFaJmHsO9Qbe7q6Qrtlb1sI-Q-0oTgH1COT-21yef-rO9zuRKlW0jcXCqo3Y8zSUoIQxt22K2wgFP6oY8VCLZyzYcw3uzl1oGhXCaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علیرضا بیرانوند گلر33ساله تراکتور به دوستان نزدیک خود در تیم تراکتور گفته دیگر برنامه ای برای‌تمدیدقراردادم با تراکتور ندارم و بعد از اتمام خدمت سربازی ام به باشگاه استقلال خواهم رفت. با توجه به این‌که محمد خلیفه نیم فصل به استقلال باز خواهد گشت…</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/29998" target="_blank">📅 13:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29997">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe8697aa22.mp4?token=dwtG0NqxDGfKpLYlRAqjufXKMFXfqYzPpdmadstT0Y2sNQHncamag-JGh-VsNhbLdG3PpsS5BGcMJxRHMj948ew8E6Y1A12bFF-5zQupgWbOKdum-oUTRFbmD060yXHgAf0avDfdOlu9zqX26udPcEMY937mn8BcQYCFg6Jq6dsKzTJx8X31_w42i23ripp5ha4bjP7GDLppsYhbB2Qlpsh-Py7-7l63sYN1iRp0NP9d-3Top3OGCsJXcOHK073jA1Y4pAtpoZF05S-2Anm4j8ovKIv0zDgK3qAModh1sxGU24qTfdm_KZpftOGCNXMUtIfaWDAF-1Z5Dj_SHh0cjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe8697aa22.mp4?token=dwtG0NqxDGfKpLYlRAqjufXKMFXfqYzPpdmadstT0Y2sNQHncamag-JGh-VsNhbLdG3PpsS5BGcMJxRHMj948ew8E6Y1A12bFF-5zQupgWbOKdum-oUTRFbmD060yXHgAf0avDfdOlu9zqX26udPcEMY937mn8BcQYCFg6Jq6dsKzTJx8X31_w42i23ripp5ha4bjP7GDLppsYhbB2Qlpsh-Py7-7l63sYN1iRp0NP9d-3Top3OGCsJXcOHK073jA1Y4pAtpoZF05S-2Anm4j8ovKIv0zDgK3qAModh1sxGU24qTfdm_KZpftOGCNXMUtIfaWDAF-1Z5Dj_SHh0cjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🔴
#تقویم
؛ 15 سال پیش در چنین روزی؛
نانی ستاره پرتغالی منچستریونایتد این سوپرگل دیدنی رو در رقابت‌های لیگ جزیره به چلسی و پیتر چک زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/29997" target="_blank">📅 12:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29996">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0mhSQoZEJ5GDt7tJrIFx0IpGqs3t_wnmFKMpl3jJ0gw5kqado_BRche80ptYhoOcRbKf1TFcz2Zzacwv8c-uwTE9IOcu2odKukl37kr2XS68XAeAZsTV99Z8mdJxUcZqQn1f3J2fxPdAY7ZECevwBA90rZmq4zZlkHKcv42IZIWoKz0pe4TZGb0TbLo6z-MCJAax3VxoJzECesv-7IT1y4FbT-HO5pz8BmvyAZB0gUhEVvkXAmSDP4LKwJwzP16vnaloJlpWmVWEu04Xh01_dlrX4FcSu3hUryUO288GAxKU9T3Q3pCWXMVNpGTeI1xbx0SO1wi2zr6S-rCK9kyLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب پشم ریزون و استثنایی فوق ستاره‌ هایی که همگی‌موافقت‌ خود را برای‌حضور در مسابقه خدا حافظی کارلوس توز از دنیای فوتبال اعلام کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/29996" target="_blank">📅 12:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29995">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5cpHe0gAaLRolIO6VmIMtxGXKkwdo2YyJDhVo0tF81LL8TmOFZhcGKMR0OknwQR8eEq7O4pSOB4qTjGyahYKNu9e3FP0SzpV-SaE0gdWuT0oFW5n7Lx4nQGXNtWvXhtklnZLXxZzNvjtROexKKWcIrRq4_U7O_HsvWbc6TXUIefvaXFXLoGeyUDMTx3LZDFXHHX4sRuNw1FqfESCK4pamqhrKGDnEwlwyoTbt6PXcVlsuCJi4OfNgujrtOAIJDEJQ6sSKSYQIBLvqQb37JMD0dwH_ljjcwMzApzCFEIQN2dzXXk4pJ7-f2yC3JyZHMSzDa8RqPk8MTd0JHS84D8Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برنامه دیدارهای معوقه هفته هفتم لیگ مشخص شد؛ سه‌شنبه 21 مهرماه دربی‌اصفهان برگزار میشه و چهارشنبه 22 مهرماه راس ساعت 17:00 بازی خیبر خرم آباد و پرسپولیس تهران برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/29995" target="_blank">📅 12:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29994">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f8f92a53.mp4?token=FcUMq8uOWa7dw-V2DG3ufzKYjaojCDg8PgePMK9YM2QLxPspubtMFJpBR0RmuQKkJigrwHP6lSLC02NQNLucOxpTl307aIpxwEDEHxz0med4k5DtBbSNfzbmrUO0cLHM20q7W7h6HmcEEr8Sm4GPHKYGQubGWnvmoNl4aD0xPWQfbtMfC0G5SVtucjuvKjobBLARqIgNq-gA5-5ngCWjZaJOD3ng07xDkHmxbF4d0pT1X3AFqrw9wK9xwgTWcWPqTs6fKJXqmVRJxidGQVBnFX48FZn4puL6mFZavtDTv6sh_zXjqVDCn4knjQ3EtiLDGjg5XlhqHzHmyPD2C6bzCpQ8gCNRSXgxQ3X8RF6Zo_6JcwBCJnSk0NSQn83WYhKzc9jd_g4gJzmayz7GrQItBQmQJicYBfUCjp4eR_bhpxqkiyY2foo-AAO1SnX4S9nmbLUeHdFboGj1QZOpMDpIVHAhGlg_VR0AH6YOCszxThujlmtIQEb2bfIHG7ZHgRixxD_O6RDD_RPg3eAqfej9AaN2kdH5oFQgR-XqCfL-5hzM6TsB6GywJaaG5Ppvc0Z2zaWwaPawK_0oiiZAtkW9qw6QOxfIcjZsm2mcb4lB7GkaJCBId77zhqLHpJL-nfOBMw7fFVgVPuQE0055MKMFjcnOdOZelD7LkBMQ8QZcfY8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f8f92a53.mp4?token=FcUMq8uOWa7dw-V2DG3ufzKYjaojCDg8PgePMK9YM2QLxPspubtMFJpBR0RmuQKkJigrwHP6lSLC02NQNLucOxpTl307aIpxwEDEHxz0med4k5DtBbSNfzbmrUO0cLHM20q7W7h6HmcEEr8Sm4GPHKYGQubGWnvmoNl4aD0xPWQfbtMfC0G5SVtucjuvKjobBLARqIgNq-gA5-5ngCWjZaJOD3ng07xDkHmxbF4d0pT1X3AFqrw9wK9xwgTWcWPqTs6fKJXqmVRJxidGQVBnFX48FZn4puL6mFZavtDTv6sh_zXjqVDCn4knjQ3EtiLDGjg5XlhqHzHmyPD2C6bzCpQ8gCNRSXgxQ3X8RF6Zo_6JcwBCJnSk0NSQn83WYhKzc9jd_g4gJzmayz7GrQItBQmQJicYBfUCjp4eR_bhpxqkiyY2foo-AAO1SnX4S9nmbLUeHdFboGj1QZOpMDpIVHAhGlg_VR0AH6YOCszxThujlmtIQEb2bfIHG7ZHgRixxD_O6RDD_RPg3eAqfej9AaN2kdH5oFQgR-XqCfL-5hzM6TsB6GywJaaG5Ppvc0Z2zaWwaPawK_0oiiZAtkW9qw6QOxfIcjZsm2mcb4lB7GkaJCBId77zhqLHpJL-nfOBMw7fFVgVPuQE0055MKMFjcnOdOZelD7LkBMQ8QZcfY8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی زیبا از کاشته های دو ضرب در محوطه جریمه حریفان؛ همه خراب کردند تا اینکه بالاخره یه نفره یه بهترین شکل مملکن دروازه رو باز کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29994" target="_blank">📅 12:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29992">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAuEQq8reR73QGtwBFtsFFvXPMIwYhEXWsrmbG2YTbje-xfJmV-v5qQCoCHVU53q9LQGJ5XS7etTXeo9i7keNS4kO9nKPsOGZkeYy1kpU-xbfDX0xBaoeUU8tYlzSkq6e4ez80VMvFMHSVnyd2RAF3mC3FVi6e0X82s_TdxW_nLGKeJjOAR2P24vCIh6IQwrI5b7o8E6kXmnkrFBp_MXT0f1WfafByfG2wqlHcHTz1p3QCMJKyuI6tZg1ck3zUGHKykb3sFoVr8_6KU-Ud9gPOW5a6yc6LMZ49cJmxKrYnBpRx21g5csZvmI0Dw7tsZ-_MLNhT2X2TriXyPRvBstoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علیرضا بیرانوند گلر33ساله تراکتور به دوستان نزدیک خود در تیم تراکتور گفته دیگر برنامه ای برای‌تمدیدقراردادم با تراکتور ندارم و بعد از اتمام خدمت سربازی ام به باشگاه استقلال خواهم رفت. با توجه به این‌که محمد خلیفه نیم فصل به استقلال باز خواهد گشت…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29992" target="_blank">📅 11:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29991">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d818795d1f.mp4?token=dT2wfmVJ1AMeq1woUyOCmlxNnczm5CBeqiluI7n4SoRZbQswrfl-EOrkx0PhNcG_7UEEVXFYtKDl1Q_QZs9HBmf8rmJRBo40YMZdaDiWVVrOtWjveCC6AhjHgwCSCaMmRIZ2292ErZlvU1o8BVTPYPFzSnjJlU9tKAa-_JQynMQSHr9RVfik0Gw43duRBbJUlXdnh3mNypRjaoCp8PN_UWbmpERLElLzrtWH9qWeRM-UACSac-0TOaWzoRoyswH4DJh0evDAzMXcnViysunGV48M_IBau5tLaL1vYJ53Kn3SgUmJDhkzWYvBzC-j7mHCUKI8ivuCKNETL6Ve2Za7zbl1YA6G53oe1zh66TES8DmQI0LCANKoKO9Cgo7WxUCYPdfZknYQxxzprDsaFmxr2SfInu8Rn30jhjc4EXuIG2g3dDDvIc_M-7cLmZJ2ZVT7wm3P1Ld-XaN8nZFzoyZbhO4NvF_LsIQXylL4Dlc9fwQ2rBOCrwJ4DkBNdG_9IcNdzOzAoRQZxh4PBEu-uFp1Mic_m8hW1ZokDQQu7QpZhH9-JSQivGVos3lWUDeuhrw1kPnIkyh0dOfr2wtM7QLXni5qSggi4kTlnwmQOBwi-p6-rkakuQj9hNVWOy34_D21ORq1RSoREOGYHCbE00xoiNX4V0ENMTxzoysS80cOt2E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d818795d1f.mp4?token=dT2wfmVJ1AMeq1woUyOCmlxNnczm5CBeqiluI7n4SoRZbQswrfl-EOrkx0PhNcG_7UEEVXFYtKDl1Q_QZs9HBmf8rmJRBo40YMZdaDiWVVrOtWjveCC6AhjHgwCSCaMmRIZ2292ErZlvU1o8BVTPYPFzSnjJlU9tKAa-_JQynMQSHr9RVfik0Gw43duRBbJUlXdnh3mNypRjaoCp8PN_UWbmpERLElLzrtWH9qWeRM-UACSac-0TOaWzoRoyswH4DJh0evDAzMXcnViysunGV48M_IBau5tLaL1vYJ53Kn3SgUmJDhkzWYvBzC-j7mHCUKI8ivuCKNETL6Ve2Za7zbl1YA6G53oe1zh66TES8DmQI0LCANKoKO9Cgo7WxUCYPdfZknYQxxzprDsaFmxr2SfInu8Rn30jhjc4EXuIG2g3dDDvIc_M-7cLmZJ2ZVT7wm3P1Ld-XaN8nZFzoyZbhO4NvF_LsIQXylL4Dlc9fwQ2rBOCrwJ4DkBNdG_9IcNdzOzAoRQZxh4PBEu-uFp1Mic_m8hW1ZokDQQu7QpZhH9-JSQivGVos3lWUDeuhrw1kPnIkyh0dOfr2wtM7QLXni5qSggi4kTlnwmQOBwi-p6-rkakuQj9hNVWOy34_D21ORq1RSoREOGYHCbE00xoiNX4V0ENMTxzoysS80cOt2E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری دقیق و برگ‌ریزون عادل از پاداش 20 هزار دلاری مهدی تاج و دار و دسته‌ اش سر پیروزی شاگردان کی‌روش مقابل ولز درجام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29991" target="_blank">📅 11:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29990">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CU0qC1wnL8e9TUh5COQrXM8szK1VKhN7Jw1Xyw_qM_jpSugoalZL1sPbTXCmYywHanzSysND5oxV304St82fxF82iWXe8NTWPY-ON-VXkga-HDjVa0Nzfe5lL95ZE_fSAiBVaLlIgo1Or5RHuhoBpsoNwHEB8zbI_qFqw7gfISpLywYGcmjouFJMAnKnZJMdncZrrOI0EykQJPyKpvZefDEdTHePfJ4v-k3xl_vD2wSqPSZlLRwhnodzRxdrmRA79abvMc_GtSD6-tmlqr0zbmTZT4OZ_URn6J8xz7l37ryiyiEI0gtBryjzF9uthsKkQ-1rUd7dGtMg-GMH_YYo2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد نیمار جونیور
🆚
رافینیا دیاز با پیراهن بارسلونا؛ رافینیا همین امسال به تعداد گل‌ های نیمار در کل دوران حضورش در بارسا میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29990" target="_blank">📅 11:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29989">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJc64_pvSJ3yct8Ma-2L_cILVHAfMTw9B7UdS6xhqOGIa3_8kuakfQjLxpt3NAQYUdF1uIS_Cc97GLUPKXwPioTpgbvnwyl3XRpQLMdGai-eWWN1QsMvCE3p3YQU_88094DhjD43OCXAdNO8OiVxBXSjUzq0_Lz6rjeknsAZ6QMF8ISkRVAUAuAB97nHIjuyo05pcpH8CHKm4hROgi-oOAHp3XYs08UvC5fuOvAwH4pC-LCKMzWrpkU6KIjnSDcRWlscqqARWpUftJSXzyQ_iQFG9NZh3nuwHxQjR_cL3mzy5pZp-tMADxD-eh27wftg4Fgchpt7IzYQJUW7iyTKdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
برترین‌گلزنان‌ پنج‌ لیگ معتبر اروپایی تا پایان رقابت‌های این‌هفته؛ رافینیا دیاز با اختلاف در صدر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/29989" target="_blank">📅 10:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29988">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMRomwFHFJOlQ8Mnk9CfY9xx2n-OrlVXXUBjjdRTgezxxMkENTY6UAmKEoP0yDBOnbmINPjKZHIak1QeSBRAa0_8pEbpOp5fMvCdRcq2hiSZ3nnXKHpTZaqF7ZBUFYGesm3V7DQYHtgrHg8r4X6tuSOcnlTod6OQS7qcyWUE4-WYm9fUFHtbTd8p-_h88R3tjzHZQXa-Y9_kZ1XgIbuYe36seLe-SLSYbi3hYaZjyC0leGhe1kfbX1he58K3w7K-ycYbwRsDXFZ_IhAtu8uI-ecwlh87QBn1TdHs6Z6II5XoPD8OFTyuWkgNQ7JZmM91MgH70RBKshjH-di_NYeGdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارشناسان AFC؛ سعید سحر خیزان رو بهترین بازیکن دیدار امشب استقلال
🆚
السد انتخاب کردند. سایت فوتموب‌هم بانمره 8.9 لقب بهترین بازیکن این مسابقه رو به یاسر آسانی ستاره البانیایی آبی‌ها داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29988" target="_blank">📅 10:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29987">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d749b5d59.mp4?token=lA-JUt0e3GJWtCzLes0auy-tVF2MgYbr7JnJHKM3xEqD6mezK-Yf6tYCptU7SYtEb7SKn1tEJzyp3EsJD0R7JZ8LySkRYpbFlUvrpXUkFp0XzdUBVkq1d0FO9kkyk7vu_2_qtMY5xvdJ4nreLhR8PUR9poJ7MFDq3wzFammzNMvPZNfozUaoinMPtxTYvv8Sq_CwZyj7iDFKAWxkQoQJV4GScMcd2lZxLNEE8cg70I7yb-g6NF5IQVfXf31Fro-1Z5QZru_drEhyceT9sKxd24M7G70TaSuYR6y8WQ8zh2z_PI5EyrNsqKA9AwikWNnRyn7IZrXAI7z-R_cQ0s4scA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d749b5d59.mp4?token=lA-JUt0e3GJWtCzLes0auy-tVF2MgYbr7JnJHKM3xEqD6mezK-Yf6tYCptU7SYtEb7SKn1tEJzyp3EsJD0R7JZ8LySkRYpbFlUvrpXUkFp0XzdUBVkq1d0FO9kkyk7vu_2_qtMY5xvdJ4nreLhR8PUR9poJ7MFDq3wzFammzNMvPZNfozUaoinMPtxTYvv8Sq_CwZyj7iDFKAWxkQoQJV4GScMcd2lZxLNEE8cg70I7yb-g6NF5IQVfXf31Fro-1Z5QZru_drEhyceT9sKxd24M7G70TaSuYR6y8WQ8zh2z_PI5EyrNsqKA9AwikWNnRyn7IZrXAI7z-R_cQ0s4scA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی مثبت 18 مجری‌صداسیما روی آنتن زنده؛ طبق آماربببنده‌های‌صداوسیما از سال گذشته تا کنون به یک دهم‌تبدیل‌شده. مثلا یه برنامه تلویزیونی زنده شاید روی هم50هزار ببننده‌داشته‌باشه تو ‌کل ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/29987" target="_blank">📅 10:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29985">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a52708609.mp4?token=PbSSGmGhN9y58GwbsnLufcNTavkEWai9LTCvLK-ZaJALcV1qaNOkJVbY2HR47f4hYSrWPQk5J8EyTWP1m-HVTX_tXIAAV8Gj-e5T8_SXh1WSfosbuu7-nme1bnp6IE3iuFQmbDHLNhvC1pxPCYhLtu_gLPLgi-7Z1fbP7p89YFeCljCt616DwsAp6RQq-ELbEgF4yaQUh2lEFklH6X9S9eOYPW6R9M1XlecntqNUcOOU-tQHR0dfbFwcuXzPidz1r9FXt_Bwmsxk2KIOJkh5rr3jSlWLWmvq7eS1JdLcfcpqrj0OWvYalId3cY5pYc54gYBjH5gYNqe85lAHqDzoJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a52708609.mp4?token=PbSSGmGhN9y58GwbsnLufcNTavkEWai9LTCvLK-ZaJALcV1qaNOkJVbY2HR47f4hYSrWPQk5J8EyTWP1m-HVTX_tXIAAV8Gj-e5T8_SXh1WSfosbuu7-nme1bnp6IE3iuFQmbDHLNhvC1pxPCYhLtu_gLPLgi-7Z1fbP7p89YFeCljCt616DwsAp6RQq-ELbEgF4yaQUh2lEFklH6X9S9eOYPW6R9M1XlecntqNUcOOU-tQHR0dfbFwcuXzPidz1r9FXt_Bwmsxk2KIOJkh5rr3jSlWLWmvq7eS1JdLcfcpqrj0OWvYalId3cY5pYc54gYBjH5gYNqe85lAHqDzoJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
محمدجوادحسین‌نژاد که جدایی‌اش از ماخاچ قلعه در نیم‌فصل قطعی شده امشب از نیمه دوم برای تیمش به میدان رفت و با اینکه بازی رو سه بر یک واگذار کردند نمره خوب 7.0 دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/29985" target="_blank">📅 09:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29984">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UicIp0ABPnvWAEy3YtRElbDbNxuOFn9HXEVx56LXLt5m9-FBgbCITgPl-7GrSQip-YjFgd9J14Fkg3YOZTMVIyaQK-voo8doEh6PryzqcyUQnsp336zOYqrDw88zCWQWZSNCCqRNTso5pfw0h8-gnUo-CwzzeQWtM4O281V2qcFAe8HCT-xxW3qOqPyrsnpbJ8ICLC6_LcKDrjwM6z0uHhadKfBYpFRXt9Aqcwr14tJ9ekWck6CIX6qxv1dlcKbKRx5cbBJ-aZkiRxuMNUcygfw2FJAUlvQnKwEKPzHAsd7poTnLMs7JjjNlhV-8jY4TLT56wT3cXZjkJOyXRo7hNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
امباپه‌ستاره‌رئال:
اگه‌میتونستم یه بازیکن رو به رئال مادرید بیارم کریس رونالدو رو میاوردم. او در این سن هم میتونه موثر بازی کنه. اگه به رئال مادرید برگرده قطعا میتونیم یه زوج خطرناک تشکیل بدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/29984" target="_blank">📅 01:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29983">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBJ2NF6rrDezczhtLDprasm71Q3RF2ToJmgT-_gChAVQgUi4o_4rmkGOt_axR6U7oRA1FehZfTYplvVaMmPC1sNyZTjDy4YX6wXpruloiXHJmGs8jh6uneZoLy-_iW_TmpxzjlJco_Q0huhOGpDu6EandyTzX4Su5WH-Rl1ScAwNzYtfzyjpKZBxDIf8TaqmJKyyqFn3D0zn67KoW-ktl1cYa-DmKH68PqNlYhOxqDFtGiXwYYDsay7XUAbgKIa4JohOF6jIc8DzeAkzWEXzaZK2_N2MDHf3DybJZa58NOhXM5XmiETkoW_y2ODIpqTK6z_y7ObiP6aLI8Zd68CNRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇳🇱
بااعلام‌باشگاه‌بارسلونا؛ فرانکی دی‌یونگ کاپیتان هلندی آبی اناری ها رباط صلیبی پاره کرده و حدود 6 الی 9 ماه دوباره دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/29983" target="_blank">📅 01:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29981">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLeiT-FGGzmXh24rlnrL7LXSgnq20N5om_hNm-SfvU-jb8tLNo7rvwTVmQD8Q2vshdRS60-MKdBCYZ3oLx0meitOX4hymmv2ySZxXSnTG4rpMThaGPGF28HnUxEMpIISUOiN4LYR2ujsQ1HSVgT2jfcWxNlVVnGAly6SWokuUPkGZQKvUkjUx_f_K6J9Gk_MHpwqykVDVH5sJiD4yOkptAUJ3ftK-vjdPvBFB-wJQAzssB2lidqObV4AiA4zisWHAjWAWVB9m5MSfvqnJ6zs88K7PdBDw3BcSCEtBDNnVQpMU9kvNzVp1zZRvq2bXk0Joc-jsRalZ4-GqAUgGsVQnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛جدال آلونسو و شاگردانش با برنتفورد برای بازگشت به کورس صدرنشینی لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/29981" target="_blank">📅 01:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29980">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWv3sZossFyv7Y_WtMYIRDLFE1blzhqhdEazhaBYiYTz8c_7usmkRXhwwI5K6fJ8WjZhn_8jipT_YqORW9L4fAzYD4Xz2v5qSXxqEI9GopO_zch-OG0p7NEo2FZoqsN5U4lhNrJN4KMq4tSZ9ATYIVEWUqNOYRqdOk3dbiW28iqbbXrrSEANec-EQWA70XidECBLM0BlN2moBmQT91K-sQtpp6U4yeKUUTgwEuZs98ntyD_0G7EThVz_RDW54IQWm-2h4_3uYsxxD-o-ZgPEnM5ooePWO1BsJWgaNuKOe-OmHCnQ0HjfWhHgRBGpPegHEU-d3UUK8ZhSD1iWRPqfCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازچهل‌‌نهمین‌قهرمانی مسی افسانه‌ای تا برد پرگل یاران اسپالتی در آغاز لیگ‌اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/29980" target="_blank">📅 01:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29978">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">📊
عملکرد بازیکنان رئال‌مادرید درفصل‌جدید؛ امباپه با 8 گل‌زده و 2 پاس گل برترین بازبکن کهکشانی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/29978" target="_blank">📅 00:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29977">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hb3aBTreH2sfoJsQnv_qVEeJ3g8eaKN9becv9IciCXldcq2pT4qnUJFassRfXtt08SbNsy9rhzec9IxpDcnGrtSp-kTDVmvRGapcRvTyrNf_bIh3E-w4824fuTFo2l2oaNZHkocnIZQlV64KaE2XKAulxdo6wxPNNOC-zUuy8yjCABHqyDkQ75eL6cjZLNs06Uv8zGkz_GPdpYCv_5Vh66zHORCqHm6IJ8xYuXCffzaa6bZuzm7RmCVYnXlJlK6qG70Cig9Z0x4rLVUcsrum-3p-AffQ-jD_UREuF39qzqb16QVEDbMZgD5tj7UfKfjccdocTVM63OE6sles7eCJPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علیرضا بیرانوند گلر33ساله تراکتور به دوستان نزدیک خود در تیم تراکتور گفته دیگر برنامه ای برای‌تمدیدقراردادم با تراکتور ندارم و بعد از اتمام خدمت سربازی ام به باشگاه استقلال خواهم رفت. با توجه به این‌که محمد خلیفه نیم فصل به استقلال باز خواهد گشت…</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/29977" target="_blank">📅 00:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29976">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-BfNWnxBOcPe_jAnwszNqh888jMrx7ZsQNiDTX9NH7_MAoboQabum5XEQMzTP6q671ZQmnPqUlTSA2gM1mVId3iv_LANvOrEx4-vukmbmXWVjqRJZHk2MeDZZE3LTMirFPKGIK8RLLwI5DWaBZ1tWwGy4qpFKb-uxgpu6BCFk5S7nznouQdtgB-CA2jTUuj4ba3wzw6uR6OZzIAI0dzI04zSHAysgVaXuwO8YKkrGsmDCQGnie_vgCK-_aVFerxmluRDf0Rsb0Z94p-nPviZRft8ybEyTuPGPpmKCVH617bPKgQfbabiGiw1IjIcBnUSaHHnAto45ieCwY-ayqO9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌ امروز؛ رویارویی صیادمنش و لخ‌پوزنان با کریستال پالاس در هفته اول لیگ اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/29976" target="_blank">📅 00:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29975">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUDelbCKlH5AsJVhWq7mpaPsqn_sW4bF-1qS9Ct3cw-OLBdmN239ENn_JRT0e3V_6MO0Lx1vTNCq3LqNA0kg4T2Vs2-5PYLp4K5ltkqaPJnSo5GCwjRgrfCNmmOZOs50eg0hJ1ls3EBAk_AEdiYF6U0qC7spEjpNQKvqulUzdlBttAB5ATT5oOKlG4FBv40ylcCBPfW-HR-6m50am7x4G8c0VXcLCbKI0kPnGBwm3OeV2J6RGNt3EiVoO-6E9WuZ3inmisIvkWyWHEZpHeCkehhCgGsUoksMcH0bIgMZ-xEwujLnaoheK7zSUr8yu2z_FGU_ikGtsnmDYNYAm1kiTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این پست برای رفقایی که بدنسازی کار میکنند؛
ویتامین‌ها و مکمل‌های‌مهم برای وررزشکاران در کنار یک تمرین خوب برای ساختن یک بدن حرفه‌ای.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/29975" target="_blank">📅 00:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29974">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGG556NkUih1coZZkfmfm1py2MW8xtmoE_Z9qVvM2BStxlziDB-KWGN3xFdjLPxOvm9fA7rWbeOBVsWPFERKvVUBsNzPByVcFAm2A9EJ3JzICQd7YalgcoXbXhn4FYJqhBxzQOkwLvuNxm3dvOTRJOF5Y58WavSVrmomT7qViBAkwP3Ij0ezhYr-3gSTvOWGhzYKPKlBr8KanQaWBuwlVtOzCqnr-ws1syzNINCeVfAWyIBS19X02AwxBu8Rbl-djjx_6KzDdQdV5vKAOLa9YWp7PVQSZgVbsYx1GDIeWtXhonAso3vXYXZF3fKF9SsvwTLahmJ2XpCTisz3P-C1Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/29974" target="_blank">📅 23:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29973">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVwi9Rpomc387EdjEzkwaXfrNchYXtZ1n9TNqu0jF56i08RrMn-iZLvy2TPEGpH_9oFUpIp0gwESLg-ptY471XKd_I_fIMdpIxG1JFmxQQuWI0vTlK-tmwRGe0o0FN858Veqk6he5RPs3KJcZOgsjXyCBR7z8RVaqDfkoKE2YcTqnG1fLkczsYmFIQyig0PjC6USWoX1EbUziXVEXFuOg--9jxYTiV6KQFUvGf57nW5cH4nGa7biFAL86woFXA2kWioOixDlkFQWr0gDpMdJ21r94oWgEs7JlWNeTKkUmGHg9-AK7OV7Mlk7W6gQbhxZAQrgriAggWnXtk7aPDwoPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نشریهESPN
: درصورتیکه‌هانسی‌فلیک امسال تیم بارسلونا رو به‌قهرمانی لیگ قهرمانان اروپا برسونه لاپورتا قراردادش رو سه ساله دیگر تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/29973" target="_blank">📅 23:20 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/kfHfrG-F7S42UZS4SkgpODQGFGeM6JtXVwaLEKrXz2mdlO-Cgb-pfo67mIceLgv44P1DqBVtlh6fVs5GhuWwu4GLWV7Li3W4MPlH9EExvyV4Wk4s-l74tje4kov7EsM33sLMjq1l8bTfH7cyWyJVWSJQmuvuRhFpf-3VMEK9fDYjvgVKsxIyNrnCfZxLlvscXVSeKm3ylgQRnz34821peSBPNmDQHaDTmjr4XZrkrQw_wnbKqc05FfDf0ATgongMfsOLQuZY_WrGhnfRYctuDDFIV4thZVHi-s2R-se_A7zBVHEFJ5acOXQEjh6AQyQQ73pRJySHt-Irw0FjCnwQmQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 608K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 22:31:47</div>
<hr>

<div class="tg-post" id="msg-28881">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kR_tKEc0aD2F9TUeMAAtegwwK9SBn_IOdAKlunsA9qTK3vNHXWnTnhnyJxfPNkdWcf3KbZ_ocm1tRnD2drldt7fTZewYd4eYNRpgkaKqtdfVh7fVCo2FTjQj2SBXcXcG-tfnNjIGMnBOvLByo0OoT0TV84YYODuwoUNb88vlN4jMnNsJ90GXldH2WyDbzTU4SYK3gbYivvOf9eco5P_a6abbOnn_ns0srTTCdC-NVm001as60AMfcqu4nsutRAzD65oQPgzwmC-32MLceXa69WjFsSxdLuRpw4E1sVqoqUW4swKqNRjjKGPh7x03gg66m_GhAR0uz6NRzz20F4u6aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛ توقف شاگردان جواد نکونام  مقابل نماینده قزوین ایستگاه پنجم به کام بقیه رقبا.
🟢
شمس آذر
0️⃣
-
0️⃣
تراکتور
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/28881" target="_blank">📅 22:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28880">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b85bfda8fc.mp4?token=NQZNMoiSZOZgQPR5z15448BcH-zp119nMxeANHsAkp8RSQB8qjuEAOT7mlR_n7rDfORePINEY8LB5zT9xXmMpZU8urkNVeZ9Qx2n1LSoZWQ7K2n_pPg0AV0--u3LQvqABeTbyDY3GrQEtlUVPhCWLpdg3pQNk3dBEZHRjj_ThpEcv3wG6McNZfyU6kKi5tX8FqW4T3H_dEAVoAHWmnbIFBKmG8KxZkaFcdye5mXb3O-IfSOkV3RUJFUGdu2kkMHQ3EdBh_lMBtRo-gGyyDtu8P74pf_wiqhyA0oBcAwSRC51M0WOqGmuFH9w46NCJMnot40ID8eD3f2UmkCtrFXoaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b85bfda8fc.mp4?token=NQZNMoiSZOZgQPR5z15448BcH-zp119nMxeANHsAkp8RSQB8qjuEAOT7mlR_n7rDfORePINEY8LB5zT9xXmMpZU8urkNVeZ9Qx2n1LSoZWQ7K2n_pPg0AV0--u3LQvqABeTbyDY3GrQEtlUVPhCWLpdg3pQNk3dBEZHRjj_ThpEcv3wG6McNZfyU6kKi5tX8FqW4T3H_dEAVoAHWmnbIFBKmG8KxZkaFcdye5mXb3O-IfSOkV3RUJFUGdu2kkMHQ3EdBh_lMBtRo-gGyyDtu8P74pf_wiqhyA0oBcAwSRC51M0WOqGmuFH9w46NCJMnot40ID8eD3f2UmkCtrFXoaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
الان رونبینیدکه بازیکنانِ ایتالیایی عرضه‌ی صعود به جام جهانی هم ندارن، یه زمانی وقتی می‌خواستی مقابلِ این‌تیم‌بازی‌کنی تنهاتاکتیک و راهت دعا کردن و کمک خواستن‌ازخدابود! به معنای‌واقعی‌رقباشون برای سلامتی ورزش میکردند. این ویدیو رو حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/28880" target="_blank">📅 21:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28879">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWAwp4VD7vHtFBiRcRz4ma2DAvTaRNU5li7MvXS_KQfFGiHnD_ZrWEPGA5AeYEq9NOSmN1sphmBz4YxZ2yT-muoZBuKmKG-bynzjzSCVtYU8xGBJl91Uuav4zA321v10bgncTozRzjHZ7CCNGpZ3X0FmRMCt0msovtOg_-MpuDDLz3SDe-SCzmF3-oB9dVcSfGubkV4pdbCs80yAZCPv1aK5jTzoRoLVbTou41J0axPq9940jNCGMx8zPclyijg2ZU56Av6_w8stJAUkmj9tjLEo9WlDfxi6eLoCYV5jgihgKpLMKZ9ny45ORt0nVi8bS-MPFtZ44Q_QWMpNJTsYkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
به‌ درخواست ژوزه‌ مورینیو؛ باشگاه رئال مادرید قرارداد دنی‌سبایوس رو رسما فسخ‌ کرد و این بازیکن بعد از چند فصل حضور در این تیم جدا شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/persiana_Soccer/28879" target="_blank">📅 21:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28878">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5pvp6B4IZ8_6AYS-XksGwKPuakspRGWKe1G9-x5BzWIfoy6W3Q5JfOb3vazuQ78D0EbnleUb8ew_9WntOHB-74pvdhn4tFg-qqGl9Ulo4-ixpgXuktZOa1YkonJKz199d4UmvPHzK_V4q5fz3D-mc6vT9hksa7Wg2FuRwd3lEEfdehkyUa7AyUFgQvswyOsPeXILqONTAETUv6rwBI7ixw1Z9VCTapzXHfQxUJYX99CnKN2wq6Oih2FR4c8a77NZHX720rwGpR_yzxmZMcnWLa7Z_j2yJyNkCx9AvImRTJcYg4nEEFBM-9_w1HdR01Th71f9ttk3UTTIjZhCpB-Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر
؛ توقف شاگردان جواد نکونام  مقابل نماینده قزوین ایستگاه پنجم به کام بقیه رقبا.
🟢
شمس آذر
0️⃣
-
0️⃣
تراکتور
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/28878" target="_blank">📅 21:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28877">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af26bce4b8.mp4?token=DhfNFiL7DOereb2J1XR9lAxhZrqC_oJVnEkEikqgG3apg0Mn_RGrUGjjQC4J8jPwGaYYszUrC1MWhHCODOjF6TR3LSzlv4VXtD9DrJSPpDiHN9Yk8z9DqHspZ52UeNdiHNMOwWX_FhjivjcWm04qul-gD3v4KZ6NAkuQ_T1x_jhoS64UUbk-TCo6Gd_DL7m6JO4QmQaq7kkX8KnuRCdUGxkGaZusqrsOdqQ_mhHz9Q2r4mN9IMvfQGfdLaRkeWKjHtcU7t3lFcYNMLTQdYWm_gunaos8oqZt-1tbVpSnzgwgRqenTl4nyAgllp1sA0u1C2EQMtM6CyoQhpjrhrdfdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af26bce4b8.mp4?token=DhfNFiL7DOereb2J1XR9lAxhZrqC_oJVnEkEikqgG3apg0Mn_RGrUGjjQC4J8jPwGaYYszUrC1MWhHCODOjF6TR3LSzlv4VXtD9DrJSPpDiHN9Yk8z9DqHspZ52UeNdiHNMOwWX_FhjivjcWm04qul-gD3v4KZ6NAkuQ_T1x_jhoS64UUbk-TCo6Gd_DL7m6JO4QmQaq7kkX8KnuRCdUGxkGaZusqrsOdqQ_mhHz9Q2r4mN9IMvfQGfdLaRkeWKjHtcU7t3lFcYNMLTQdYWm_gunaos8oqZt-1tbVpSnzgwgRqenTl4nyAgllp1sA0u1C2EQMtM6CyoQhpjrhrdfdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نشریه‌‌بیلد: هکتور فورت برای پیوستن به‌‌‌بورسیا دورتموند به توافق رسیده بود اما مخااالفت پارتنر فورت برای زندگی در آلمان باعث شد که ستاره جوان بارساییا قید حضور در دورتموند رو بزنه و با قراردادی سه ساله به تیم رئال سوسیداد بپیونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/28877" target="_blank">📅 21:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28876">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPKQ6WvuZgCdOlNiZbn5QVo7bdJIYNAyHjNkz2NfeOGM1AIOeslDW2nzVueLwmYJjKt2ejsPf6osYnaHtRJtizW2iKPiHLtZ-AbuKDgqUsAkiawbWaE_WSU6N73I5w7JndJPP3a4AevZE8w_q37omGdQJrk_R-8RvWTjurRgLn-YtiPKBk2X595WA0g5PAf76B27n3LWml0x-l7r7hA1MWc1VCWUKrnjC3gtl7nKbgi6TyhpdwZewZSpvqNtHbCfldKHfQJM-UcYusSgVSe-ujouwgCQMKjIOTQSCHEdUuzRK4FKlfAFSANDzTcXG3y61etNQ33GWEZO-YY9ragXbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
نتیجه دربی رو پیش بینی کن !
استقلال
🔵
—  پرسپولیس
🔴
🚨
۵۰۰ دلار جایزه + ۱ گیگ اینترنت یک‌ماهه برای همه پیش‌بینی‌های صحیح
نتیجه بازی را تا قبل از شروع مسابقه ثبت کن.
🏆
مبلغ ۵۰۰ دلار بین برندگان تقسیم می‌شود.
🟨
هر برنده یک گیگ اینترنت یک‌ماهه هم دریافت می‌کند.
🎁
جوایز به‌صورت
FreeBet
پرداخت می‌شود.
👇
ثبت پیش‌بینی در ربات بتگرام :
https://t.me/betegram_bot?start=p12_r4EF37DCE</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/persiana_Soccer/28876" target="_blank">📅 21:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28875">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTmIZd4g-V4JrhhyF5kFKxV8sWEVe6xsmn4CkADL2BEog-bL2kGMV_jNz2JtpI85grJzf5FhhKJXkl6BbEUJ_HFeztBTDu4cYaOwGFNFKnbAFf6ZXXlYf5aZIXaFVBHzHAyhqgwkg7tDrdxtglUexKL5OaE5r7Yyr9zkx7Zy2u257cHhbUf-BBrGJKAUCAb7oOkcxAn2eEPI_rCMvHnosw7WemhazibVeFzkFG-aYqcl5xuPbaAMJvztrBhD0p9oPSfffSn2qPcdV1hdONNthAxw37n51D2AHU94BsNzG0ile_MHi4or7o4APxTEyS3hkZeXAdqd91l8_g9K0hUbcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگار نه انگار فردابزرگترین‌بازی باشگاهی ایران قراره برگزار بشه. نه تو مدیا، نه کف خیابون نه بین مردم‌هیچ‌اثری‌ازدربی‌نیست. خیلی‌ها حتی نمیدونن فردا بازیه. مسابقه‌ای که از چند وقت قبل از سوت آغازش سوژه اجتماعی بود الان رنگ و بویی نداره. فوتبال، استقلال و…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/28875" target="_blank">📅 20:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28874">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2sEgu3eGWPCUVaxPiWtJ3LRNZi43y3_e9ibbJ-JxdyvQLwYsOfVZopo_h0H3RGU-FV2CDiKJ0QRAa6UMmkTzWYwjh-kGm21ANAjewYnEwSokOjd84D0uLuXNJWj1R6qo-5rvjEpkYKSVEf1mUeXboxA07vZEinVFBM-G3WYWnv256OtVblLBMFyVA7PT6BNGialaOGfVe28-1FjOaZ5EDdIaXybnWIomYXu0zphJ6a3BUGq1v3MdDuvPmmCZfA7evdhUckc2wYMYV4-qnIV7idCP2oXp5L7zCJksEtHHeohWlkq9Ubonc_BpG7AEVBhvqML5EKi1_doolVSvop5NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خبرنگا رسمی باشگاه چلسی که گفته مطمئن هستم با ژابی آلونسو قهرمان لیگ برتر میشیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/28874" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28873">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNn_YzRhpHVFvQWDojWAsXA8BGJB3Nnxof8Ew_rz9UMpuXbZZkebd4-vp7v4nO9fUN-NPJ9JGk3iwk1VDgOyeE0OealxUQLLope-5p6yd0EpwUWYHUjrIBPionr-DPfSUUSaszj_oqfLOUs-U_3R5-XVcck6CrqC-oVs5L5FNDrmm861Pbi45jIim9-Wu1xKijekLhzx1oP3tQLmv3lppcBXFXIq5xzGkEwJqwdQEbGINQd44gRR2pvQ9Nk1dfFPsVaqrb-HPkQTG9hp54ANYXHeUKcRJBlZAA2mjFTdAB0wbOmVji6GlYvQAPcSoaYQqygc9CORKeNpMIPesNPpyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بااعلام‌باشگاه‌بارسا؛گابریل‌ژسوس‌مهاجم 29 ساله برزیلی با قراردادی تا سال 2029 به این تیم پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/28873" target="_blank">📅 19:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28872">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZnN7NH5nVtnrOjkQ48jSn-KSHytogwHIl_vPNwGJeFS9WIK1O9-GhCcBtf--2bD7_d1WSgBhZ4xraTkz0792nnMCWRIytW2Oe84xHbdWDcbTRYMX1SaSk5mhCUfRPPEngMR_K6R3_-1lpfTj4strS3nN6jxmxmadPDesG2NXoOYN-VGViuU7XNCvzIzw4VM1FNf_5Z8kLBNYy63x_383UZOqlAj--Ds9ybtrVVYuUvfH4NcY_cyemT9utXAXGeDPn0ba7fJYahA52QU42y9SRvowE0tG0C31Hnlsea7_6EnMB8CjVTnel7JLWr3tFt8Cx-WKPFlYOaQSmZp0QfzKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#تکمیلی؛ تا ساعات آینده انزو فرناندز ستاره آرژانتینی تیم‌چلسی با عقدقراردادی تا سال 2031 به منچسترسیتی خواهد پیوست. بند فسخ قرارداد انزو در منچستر سیتی 100 میلیون یورو خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/28872" target="_blank">📅 19:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28870">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cy9-8enC0EdoK029ZLbQIxSKfW0fhRh7Fyo_T08wTNSflGANaV7vkQS3vF1B6WcYaiEpV_dwOAFEXVeuVSTR0YXIPhz_sj6dqiBIsl4Zkj-9kzWohcdlCQEYT0GW8zJ5prQvld3iLLu6IUMZqpWOXxV3iE9aSYFg63ZlzmH2dIOYMZr3WE5ecrxF-2ka9nO9NveYaJFjduUjAQTgUMu9Pe1gaT7v3EotatKqjVUxMcPlgnnwaDCDSrLELFtnTYBCEALqrw83MBEw3iy2-pi-bZLdlvmLZz0_3YRAO9JuVKyshue-0Ih0GPPYpz5hiNrypPspszzeut16C54rJVd6kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qXGWOsgTKJ0ZNHX8cmysHUsm73pG9p44wWq0t3xOBr0FzQEnv7peFv-PoLK_Py-p6J9GCiMHBrlDBgLHXptQ17Ff1lkT4N0d7BMwkb0PJcd6IcPxQLtbBsuwZQOzqTOiAnW1Yd4C4uvRFiYEYePwFjehe-nqDhfit60kZg7WegefekGDSuzHf0MhHgVJAWqStflQ4S0rjpoN8gjZIeVaXATdDa-Gok0JcemRKl902A3yD8Dh3zMW_HNavWu1rvJq5DMP3tUqtdXtFywJ2fczQEDSZ7RQ6BiPBrFdO9NxRoOm0oSRivDj0_CVGYjsnlvonHgKZc3suAGq1E7otCFHoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📱
کاپل‌های‌ فوتبالی که رکورددار بیشترین تعداد دنبال‌کننده دراینستاگرام هستند؛ امباپه در صدر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/28870" target="_blank">📅 19:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28869">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QS_HxyVz3fSHjgWT27Jfd7xUiSDtAgnWllxsGEUeOO8yJf_t8crAnpsi5s-HOJ7UgSCifDIWJi4i2JqkCLQf7OzzIBIrSosVQr7PAFcnAsQhFQ9oO4ec-1weOvQMt-1Msa_EgtNFxP8QNlxxLlmVUlqq110rFajyuVsiDfdYWXB1_0dAgDMkEkiIUrM2SHXd5w1ZQEaOr0WyHOC2NW6zC60njLEDlEuF3O5vfUYNHgpb2seyw7sZkmQv4_sI2DoCeOcSuyjvO0mIRlcyToU1DZyTkFGgHkjhQiqClzV4uDnW9nksIMN_-qnzxmkutJ-5oLJEQMtfsfhnYhPR96khtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
دوتیم بارسلونا
🆚
رئال مادرید روز یکشنبه سوم آبان ماه ساعت 23:30 در ورزشگاه نیوکمپ اولین الکلاسیکو این فصل رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/28869" target="_blank">📅 18:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28868">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHrKXNBa9K5o1cmTSerigXQ0xOuXOW083SaBMjTN1r7ISGVvQgIx_hleJlDXfhhVeTLA4AZK6XFcZuDMdKrJZaqJDwXhKxNWoStMwGGs_M0wvGb9WEp8JjXJH7DfmuJlZ6X1fsERqO0reQhMKZX5zRjKOgmpz81vq0Z4lnljGFqafnzAk9vuQHnPkhruxr24t3Luz7DIbtXBllpWRE443nwZCdSSem1FxJnvoE7oS_a_p4TtG_mt2FuXHJSNZ-i-5xMbzzaRJyMsbfqpmYNKVFVKIF0kVWVGdVktXm8NZOZvUQCQF9rNdkBy1252-7iHolesD52Q4s6yEvnYKflCeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
#تقویم
؛ سال 2017 در چنین روزی؛
کیلیان‌ امباپه باعقدقراردادی قرضی همراه بابند خرید دائمی به PSG پیوست و با به ثمر رساندن 256 گل زده با اختلاف‌بعنوان‌بهترین گلزن تاریخ PSG تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/28868" target="_blank">📅 18:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28867">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADQjkDZyI9840VMJDkGygExKR6orhsb-8g3pUj2IFZ4DObLuxnhgwF6bgXxzw0cZq8LU4ZuOcIPPahN5YuedoOe_rG7DcAaSfHBsFD9qjFAcYCp2SSACoraMMd9iNj9529Ir9phqHFQCahL9-r0ihU672gSxrv9vkkOjLLzGUdQfrPq9Nt6JP25KSkdSKiiQ0tPFskioLyVyuVr9oKmjTyxJsYS8HAfqoJggpyIn29CvSzD18m2A7YDRqkmRLnKdp3Our9xn3WvljbaO65nLboeDt_iW42mkzod_WQwBmTQInHvE8PGVKJ7TaVkCl-Dvw6cdFlB2Jiazh_q7SQt5Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛
شماتیک ترکیب تراکتور برای دیدار با شمس آذر؛ ساعت 19:15 از شبکه ورزش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/28867" target="_blank">📅 18:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28866">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGKya4txi0ijFYfRoNwgWuaNzmvHdsSZyflt4K6a0WhzCiAPOYBfhu7hRAzw8uVRBd2tYwvXYg_mKBKVvbLpRbae3--ZFNDpASUo4lDou-exWRhdPbm0iGZ2SYWu3S3dbPYX1A4K5cJAd_fEnE8PSKnqrq_EfmF6OG3UXr-fwX5fxnwx8Ow5YgWSQc8zKYsaEHNN7_o0gYLBmyrgF6hiZqPiqLLfjnYhIdE4Lbyv8Nr8YqUZAGjaax48IuZwG-kXG8ZLwy_hYE8rrVMrDYbcXBG-5zjRv-x0XOxJ7Cx1fvoRZtJNBm3XNBKOYI5KiMTNuvixQKFmSFdhet-nlnl4Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگار نه انگار فردابزرگترین‌بازی باشگاهی ایران قراره برگزار بشه. نه تو مدیا، نه کف خیابون نه بین مردم‌هیچ‌اثری‌ازدربی‌نیست. خیلی‌ها حتی نمیدونن فردا بازیه. مسابقه‌ای که از چند وقت قبل از سوت آغازش سوژه اجتماعی بود الان رنگ و بویی نداره. فوتبال، استقلال و…</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/28866" target="_blank">📅 18:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28865">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cc-kxHlQe0gjdzT3OcT8sbdLgYMbZF2dC7vXk72RGefRYUsWkrCRkbFRUZk3V5JLdpQx7Pf_roCUK0d88PA0sIAhxPjxonRt3bV2i0HFEZl462nibNeoRU-FInAXCOgAQXGiY9D8FrZwUdxxeeub8r_mJCGpkRDW5CqQex-2pRLmIUfUe5jy0hx0p5H3-okcIZNArG4VoaMyW4V46CgWPqrGI8TnMQ_mghM0U-gxTwjyX9HsH7DerbXYcbzbSpCDRxTmiW7x3Jpe1zLGbK7vMXSKrgaUYMEXfkM3fesjxOHLm8gUrdtof38LNLc2J6c76-_LrC2MdmEA-1GkFvhX-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگار نه انگار فردابزرگترین‌بازی باشگاهی ایران قراره برگزار بشه. نه تو مدیا، نه کف خیابون نه بین مردم‌هیچ‌اثری‌ازدربی‌نیست. خیلی‌ها حتی نمیدونن فردا بازیه. مسابقه‌ای که از چند وقت قبل از سوت آغازش سوژه اجتماعی بود الان رنگ و بویی نداره. فوتبال، استقلال و پرسپولیس به بی اهمیت ترین موضوع‌بین‌مردم‌تبدیل‌شده و این‌حجم از بی‌تفاوتی قابلیت ثبت در تاریخ برای نسل‌های بعدی رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/28865" target="_blank">📅 17:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28864">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57ae770053.mp4?token=FXAukTO4h9PNj_ezbqlkHcPKx7QiS08E0jgfiMGK8dQfTmNjfKZTHL8gOx9zJ8gV0BV0vHDjwpUwxzY5GI7yR__RPV3JmOLZTX8y2Hq1hnHMpYvE7KMqA_O1Rx91THTrLTJZ7TE0-qF6yEEnu8Fx0wmpgzFIEvXEWSoACfIqABqLiL7tgtiudPwPYHCJfGQ5-vyURDhbY0vpKMC_z2sOHnaKX7T40G3WaZuujWfNqS93RUbfB4DOy2Y_axwWAFTuYyD8hAgpBipyaYbXJpqTPnxOmw6Cff69fKMR9l8vumnMrGwG_brZkk7tgTRse4tvRQTgRGZI2-2KDSQ3sB-KnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57ae770053.mp4?token=FXAukTO4h9PNj_ezbqlkHcPKx7QiS08E0jgfiMGK8dQfTmNjfKZTHL8gOx9zJ8gV0BV0vHDjwpUwxzY5GI7yR__RPV3JmOLZTX8y2Hq1hnHMpYvE7KMqA_O1Rx91THTrLTJZ7TE0-qF6yEEnu8Fx0wmpgzFIEvXEWSoACfIqABqLiL7tgtiudPwPYHCJfGQ5-vyURDhbY0vpKMC_z2sOHnaKX7T40G3WaZuujWfNqS93RUbfB4DOy2Y_axwWAFTuYyD8hAgpBipyaYbXJpqTPnxOmw6Cff69fKMR9l8vumnMrGwG_brZkk7tgTRse4tvRQTgRGZI2-2KDSQ3sB-KnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل بخودی های فصل جدید لیگ برتر تا پیش از شروع هفته پنجم؛ هر هفته گل بخودی داشتیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/28864" target="_blank">📅 17:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28863">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjexJtDgDJ6TaugGAU--wtNBQkbvItg1EUr52fgw9QIAr8B4EbF5q0nVy5ljyGUdxxoXbfeS5KdhWqH_gz22hm_4XVwLKBxAJ8xbpPoy5JEeZ5BBlSjNZiRug9MHbgT80zlK4us-eoz641rxnck1QwuAOlWB7X3KLeP0O_-Miz6gYlqjevBG27-3Q2g7uwyWxq2TCRIfXOPOrFNV5oRnwkMULnmb8ND9ZsvNzrvP5HAcdUtN-pzRg7EjZDsEydXANiLdA2y7hKogoUZz83R3Xslse383M-9kennsOa0fyvlAqBjzWrlnm_2sFKcGgxE5KrBmv5iIXazPgtRLXOeiXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بااعلام‌باشگاه‌بارسا؛گابریل‌ژسوس‌مهاجم 29 ساله برزیلی با قراردادی تا سال 2029 به این تیم پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/28863" target="_blank">📅 17:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28861">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XCWY8Xvedx-lX8gNFw7pow-Z44iXYBj_QajRGTrxGQWkG4mGd5qAG6y3qE_BTLgJyZE0hDglujkM-44RGO_UIYT3rJ8TB0OrKOZXn2vMKSHFR72yoCWWVNEi4lQ53UFH73CwPKLSJPdKOl1hMdN03YaUgD5Dp8VAIb_-EoR9p_lMyPmWZepcEDqWME5ozt0lyA_wA9nHrytZrD7Qh2Uo55BzE6rrJ1V8lWl09On46QcxgAWic7UE8EjUvW_UIcbHlNSeam4Iwbr5xSwNfWstIUPFZ3RJP5sGTPGlHWf50-jlZZe0nv04OxmaZ0d3D5RqMGYR_Lnbogqr6LMMr7IoZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZsU1GFwWvZ4UL4Hb3N2MTqxUKMynUWwh7bY6cN49oOPUvhMZ4GVEdA_kVfV3BAXy0PcokuvJEudeCt9-4kGYopDUHm6micIicSKvOyAs3xfBOyaPfcLqF5LlkhBVSmZgtcZ6sF6qV6dmFftyO5l2IKXhz2U8-0NtmdfgR37E3EkmKhZfXEQMbI_PcmTYpDYh1-7sS95m60YkUdmAqeoh04cOsP9LCm6R4dEujL5DeGte1t3OcSzj0TIGxfAIdlq5uyclIB49MzNNkM4fHkjiCkcAAFYOiue55MnHROm5FEYxqKRrBqAiGDYFcxzIPzeDeTDo-q0HPFU9Yz6fSA-iJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
خبرنگار رسمی باشگاه‌شباب‌الاهلی امارات هستند که از نگاه‌او سعید عزت‌اللهی بهترین بازیکن این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/28861" target="_blank">📅 16:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28860">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Suah6fjVqs7uLH_3WPn-nv6EZ2-3-_SsIJ3JyFmv_r534Lz9S9raqNyPliuakIsih0aoFSZkwkBu2itMvOveRbzBghC0ZGn-d_8s-vT1NOVFVDSx1SCnvjz7I7C1XV5VKJfXRWuQee3HutDAMawzqLi-ejKwfaVTSbXRF8uzqeyLDgXoc04NHTJimby4wvJVfMIkqiCBSVIquX4yJ-lTnPcYav3d_4bscN33DzIcfFGp9NCwrC51vLmAtGgz_H8LMplVmzLp67oaYVO71HLbbPAeN8OVmq395I11lUfwSgw71JDsDT3Q1r3NNETWKgMIdLyS0q6bhmbTzS8CYXzUVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ قرارداد ژسوس با بارسلونا قطعی و دو ساله توافق‌شده. سران‌بارسا10 میلیون یورو بابت این انتقال به باشگاه ارسنال پرداخت خواهد کرد. تا کنون بارسلونا 174 میلیون یورو پول رضایت نامه داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/28860" target="_blank">📅 16:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28859">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cShAPTJR2xcg0EGTx3o4NERnLursmXxmTyO4t8vKYn24wwgNNmWaXLKdOKRYgRJ9zmXDLR1CI9sJuCexgb9qmGK93enNQSkDqYwef_UEkVSvadOOy4LHeqUVUYAsOM9WHWVp1Lvj-tjzl0Z-uPgz-yvMqgOGdIvB_nOJLd9EA-Ogr8tnSC1lADZgzu0yYktGlI1WY69slbechWwt2TDcBKHlzRymdqydJ7j0XV6GSSrLIx-2G9dpDjPnDbPk2GIhJcCO-5-zYgcMsDelwxGAXIKcZpavb8fxURsDCe42J2lKGL-cfmDsq9ZNixVeztJgtKlv2U0IJR0vzuLsUmiQZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ لژیونرهای ایرانی حاضر در اروپا:
‼️
علی‌رضا جهانبخش: اکسلسیور هلند؛ الهیار صیاد منش و علی قلی‌زاده: لخ پوزنان لهستان؛ محمدجواد حسین‌نژاد: ریوه آوه پرتغال؛ میلاد محمدی: ویتبسک بلاروس: نادر محمدی: دسته دو فوتبال روسیه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/28859" target="_blank">📅 15:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28858">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUe9r5Nx9OkhdBPIa-Z_RINC1Rf0uVPHHSKV2EW2T_uJ67bObwaZf_riiNcORHV9gjYnpYD6CXn43SxE6F2t8ia0n6uJGe0oEo9i5bNqRi6xiinXwECIGaC5Al0UMfQQ2yABcwiJabZFiPZdmVQfcMx09CNWtVvMgYV_Lt5ZmOWlMfh2Gu70PYrTU4iuiFrO7RaI-AZiVhsVCfaSU3n8AXa2GcIiOL7UMORGLGrzO9f2vXD5-aObQ92DVC8Iuv2YQ9C3KcfB5GL5BmHO8o7RWsJsBaX7zXoTyW10XapKhfPrY0SVj0Ux54vAxaV0KrVrODylo7NfcYAhr-vPn2YRqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌رییکای‌کرواسی با انتشار این ویدیو خبر از عقد قرارداد با محمد محبی ستاره تیم ملی رو داد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/28858" target="_blank">📅 15:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28857">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgnXGnXoAZoQwYgfGtgs7p_kudFYvRtgGfd154HGWIJfRnK9W4dce5pfjz79RE4nrCoonl7SMWOk6XUzIfQ5Z2BSwlenhzCHX5LaaNm1dwv6wjBrs-w0dKcwwXEnPleNoeQ-pvMnW_YsyG6tbg2nCBR0M_HiKC3r3kIE_A6qJR-v6R9Qv7zDodxpO8ColjXhfrAfYaMnzSNPX_yI642vAbIchvJTi4LUzpaSgTHfz-F3tfKdrB5OTJIu_y3SvlZ6yHgKPBdKFl6QGQZJKcavJ5H6PbffqYt8EtdJVorXItYLlhT7oKragTiZ11UfRel4kjzCyjuDzi3GV1MfFZSnZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هوش مصنوعی دیگه داره کار رو به جاهای باریک میکشونه؛ یه چیزایی داره درست میکنه که با واقعیت مو نمیزنه لامصب. اینو ببینید‌!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/28857" target="_blank">📅 15:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28856">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqRJcT8GqTZew6Wp2CiaEb0iV1FBvINymOI4s0RfzgtXkL82forWNBXz5_c2Q5X8qMmiOAbSxcpeYn7-vXzV5huj07tFjyaExI5T5cXp-HdxACagZcUBCWvicvMtYGC6iTS8GScDM8LdcTwY-Q_tFqc-xZAWkixA7WDg8fj5IG40PlCFiZ7SgfwgJck9xBB1u961at2i58B9-9NZgLmSGieD7zslupo0tmD2TXQHU7rHfEe7zGqLVlbBHDeUmST4Vb3oif12Hrfs66ERO2SBgJavfb_JCwjbWRZajLW0Yh9XfELTBwoxIYd9I8BIV4rsUuj44KIxJgjQjcujltX5tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته پنجم لیگ برتر ایران
🟣
شمس آذر
🆚
تراکتور
🔴
⏰
ساعت ۱۹:۱۵
🔴
انواع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ شرط رایگان بر روی اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/28856" target="_blank">📅 15:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28855">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d453f3d9b.mp4?token=o0B3wGuJmN-dcbcPsuUS1U40LVMuWYCHqOBCybqKfSFn6yWUNRwyZznWK-kwufSQ5u7FPTRsugofLJyhm3fYCXAxeh2-GW8sPR4Qyfph4doUmO5AX7LKFQUk7iTPRoDEMhDAe2IZ5FcEg2CcC16MizwJZ-mLTWyGhMZcGFeLWz4BaJomfql5dE-HU52jYNhkqpmFy94zObMkES1R8cKAk4Mi3RfJyVHhuvKdwf-_BSIjOk5CYQu7pJZzNqEarweMIJxRqgjlYeePNoKuVVJ13Z6ZldC_NSKdjEA992NjRc7CfEqstxV99Bd-3GAUw4Oz7sSGjxN4gOQLZS7OQ_pVVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d453f3d9b.mp4?token=o0B3wGuJmN-dcbcPsuUS1U40LVMuWYCHqOBCybqKfSFn6yWUNRwyZznWK-kwufSQ5u7FPTRsugofLJyhm3fYCXAxeh2-GW8sPR4Qyfph4doUmO5AX7LKFQUk7iTPRoDEMhDAe2IZ5FcEg2CcC16MizwJZ-mLTWyGhMZcGFeLWz4BaJomfql5dE-HU52jYNhkqpmFy94zObMkES1R8cKAk4Mi3RfJyVHhuvKdwf-_BSIjOk5CYQu7pJZzNqEarweMIJxRqgjlYeePNoKuVVJ13Z6ZldC_NSKdjEA992NjRc7CfEqstxV99Bd-3GAUw4Oz7sSGjxN4gOQLZS7OQ_pVVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
باشگاه رییکای کرواسی بزودی از محمد محبی خرید جدید خود رونمایی میکنه. قرارداد دو ساله و رقم بند فسخ یک میلیون دلار توافق شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/28855" target="_blank">📅 14:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28854">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbM5RvReRumIRbolKdAwt6_3JuC5YJDX_KuPh2xa2YT9yzti0-XzOVFJkiiCtLKkHpjhWqROrui-TgUCWjmjLAsX8UkZAqcBvUTkXXpoMO6LLrlGlEmpmURHB-lhNxsnKYrUzkst4DgccAEK0ps1YCUYBrR1kJ-1hB0Pgt0sBMMBOpvDGkw9OqDkVrSo3X-1NCfHOtjlzHBG7D4Qm8pkNCUQYbhG6EvNP2Er1TkjRsjjfV6zgyOymY1fbG8WRodEGtjvvNwv6NE2O8bw-fEmxg38SUXiGtFDj-foUvkpdgGoJ226A818xAUC0SmVTJOKqkMfdN34SppdM0JtC1igbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
خبرنگار رسمی باشگاه‌گالاتاسرای ترکیه هستند که معتقده این تیم امسال قهرمان سوپرلیگ ترکیه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/28854" target="_blank">📅 14:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28853">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔵
🔴
درفاصله کمتر از 48 ساعت تا دیدار فرداشب استقلال
🆚
پرسپولیس؛نگاهی بیندازیم به زود هنگام ترین گل های تاریخ این تقابل بزرگ فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/28853" target="_blank">📅 14:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28851">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Et6Zkbem1VhsdbHLEzWOzlCMpGOKTgxiRJ2xsNw9AaKLSJsVOydpSMEiKuXz37H5JtdKJnxR7XMQBocodZKMuFthVa30K-k0S4I1N4YqT8ecrDxwh_hXY1tukKnDEtUue2KEOkNXuGqGzTIkWJ06fevM2-zeFEguG-6f3CIEB4X6309Jx4e7tLpVht9N0NNtPBl3VItyMFTrnbrVsrqnZd20Vv7SzkHTnbHAjpMccBu2N32UnVGxTZXsa8bXJTdjEOpAimgyD9d3tT6o4V2SeUR7NAeNsae9asPdG3iUFwa_B_NRNfncf90LKbUESBcXvZDzQwhBIsTCdwZfHtOV_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B16do5TEAKQTOwdX_LgctMu8G_oPLc6mydLjUuwxn91z6iOWuhQqHKA2KhgLO1CEMljwaQaV86oKnzlYiZ4b_ljVKStsmU6e5twIyNAWoXTdvLP0ls28iu4p-PztayserQ_7TvbpgMzbJ27-upGDg1ZbRdBeTc2RH6jhv-oDjtbIHvSauHqNU2i26-3ba0MCKOk49ac7Z5goZSHIup3yKZEzxzNGAaPAfG01KVmeGsl96wj2BdzjJz4Ky39YYCxiCWLVqQbFv6YDJi9VZaMzt7uLe2PmNorU2Rn1LdvbQsM-AO4c5IyzevYiA2_7VaYENqNCrlbJSYH_xx1Yse2Cig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/28851" target="_blank">📅 13:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28849">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bxjRZs-U0-YKEmH0W-d_JHmsbl59j2faGKi8AhwE72A6vrt2m1pFb4VGXfgbFNhCOoA6EMdc343vXhyV1N406ee_NVw_4LPznq8sTxftBNocEOch-_vtL7upkcPSUhAc3IawzKSqzXnNn2Gza9UHQAb1IsRlC7o9afRHOwDwdDk3e0pPuODMcllSxT8UTRqoxCQDVXUC-nkQA8OQmTHYah5c6tVBoFg05OagPEYyEUjR_0X6Ou0JsJsyffWzQciMBpFepjFpAqIDzmCmfWfs1PkqHBXpKmr9IFUfNsUgSJQizaw52MD5vkBthWxZUFnG-XguoABJ6E22wwLgdFMyOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cF8kko-gLUY7g8-rWSDgLvS4MqybXYkXee5YaJoJx1pLwFhR_ZUsFU2ICzjXQhrxtFs0-vPICpxtEj3nmTSQVy5oKDG1ikw0OBn-V7GPySb9RmobIW7R3QXS3GpqaP6yEdm1qvOU7ybsnd_IJYWUrfACUVPjFQbuXhW0Yk-QjPLTIk7KusRSvDM6ECl0_33NkkYlrFi0xjty9USTaTdCFYwYCFdtltc7lwBiADiJrYm4BTdV9nwbzsLcw9tT2itxZIpFajPRvoeHoz_GWMvzC4kMuNFNShauBg2fDUwIlCFWyeYv4HsZZC5HGofrwkz1kKuTiOJxxl_hDLMF1fQY_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
پوستر فدراسیون فوتبال آفریقای جنوبی برای پیتسو موسیمانه سرمربی‌جدید تیم‌ملی این کشور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/28849" target="_blank">📅 13:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28848">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYDRTBKXKsSZxy_YTTpSUy6b28GaNodnETOO6swwtnJqT1_B2aOGcb51jslQQ18aSZOD5Ry4E1ID8lpjpixyltRpSKBKu7fTCvtiGfUzdlBK1PNOBOdkUorKY3OVOiwYZ1mRMANfWvJSYSrxDCV5TjtDKCHqZCakfPlwE0wcjLCnPURgy76A8EdSSmu0YEDLpLx1rcI-4sYA5TRacAjyLRce2FGNwKlUCrP8KiPj1-XgToTBmVwOeagbXhACWHqbXTsBSfDo3yT3GyfwKO5rrOO9K4Nt99uqGymjWGsbM3XqMopg9IddOvcWdqgWRMKmNFl6UFHQIWQh1tB08pvx2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
فابریزیو رومانو: انتظار میره تا فرداشب که پنجره نقل‌وانتقالات‌تابستونی بسته میشه انتقال انزو فرناندز ستاره چلسی به منچستر سیتی نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/28848" target="_blank">📅 13:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28847">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oj-c0eG-n-ZFuOCiJ1WQowOA3U7-kD8dmP9GmVN6u7HjidTFK7gvbDMqY-RVDnhLfuDicgVDveIpn-Ei_d7s0DIbqJ9fy-LdWjZ_kWP1ov6HGN7QopSbY0tMEu9YND7rSxMdL7dnkku9_DvOHrvw2Dx9wwLNlHkOtgQDlrT4WjgEpExPqoxOVsp5Ge8pCYKQGCUTOB01nVlTGiZ3doM1-jh74LSrdu5tCsavWT5fTQCo4Ujj5cyRFjVdq7wq0X_3FIi3dfry2h8p4MhCRaiw8WH8Ch0Sf1SkXV0GNo6hmUV8hatSced0uthvgw0T57eqF5KP87FAELMFY9O1aArWjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مورد جذاب گابریل آرتتا پسر میکل آرتتا اینه که چشماش دو رنگیه؛یکی‌ تیره‌‌تر شبیه‌ پدر، یکی روشن و شیشه‌ای شبیه مادر که توجهات بسیار زیادی رو به خود جلب‌کرده. جالبه‌بدونید در دنیا تنها چهارصد نفر چشاشون‌دو رنگیه‌که پسر آرتتا یکی‌ازاین 400 نفره.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/28847" target="_blank">📅 12:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28846">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEntTZ-1Drb6yVAmO3O5gnaug4968cKFjZlXxtQqw7-50881wSunOMuFVAOiHuFm2r_uW8s235fPpOhPMbrVsAeeE0clivEyqNFC0RH8yIKbDbi11OqphdkCTB--PBh0j7uIoXe9kQrUTmP1NSsxAZreuUpzkw9M41e6plakLTwYN6TB5N-f2Kph04gBIorhoWx_UWq5MU5CAThmIwXX3W4rreKKDqBzpvWhP9ddgUhO6R4ASZnf9c3ErRb3oZ5B46s0E0PDZY3mA2KGus8m8JUoz4TxczkxigXeliqr1UIdaySXYYnYJJQrKiUNdHYXcxvo_ZQE0QNFz9X4ERkE5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
نشریه‌مارکا:خوزه‌مورینیو ازوضعیت ادواردو کاماوینگا هافبک‌فرانسوی رئال‌مادرید راضی نیست و به فلورنتینو پرز گفته او رو بفروشد. پرز برای فروش‌ کاماوینگا رقمی‌بین 60 الی 80 میلیون‌یورو میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/28846" target="_blank">📅 12:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28845">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">▶️
ویدیوکامل ویژه برنامه شب گذشته عادل درباره اتفاقات اخیر چهار هفته ابتدایی لیگ برترو افشاگری‌ های عادل علیه فدراسیون فوتبالِ مهدی تاج.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/28845" target="_blank">📅 11:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28844">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZpM5Z8HS-_U3D1LW6X6hOuUH5e4yIDbcogNzPIDeAfAYRR5gkicW7uH0aYKWS6fCphOxHbw_A-Tgu1uKz2nBGuqdo0_ybjdtPyNOELgI3SmFMAtrOy0LqBpe4Q_Neo1Y8Z758e3dyAym5lFsfAzMMf-wTIIj7Syv3PleCNwHk2vOoXPlexEwbP6Kk4CvjNuXxUqijmukEfQo956Hlzp-m4XujnWmYUxUdqz61PtBlpfhPiftHF1NKeFbMtlZoBnN-K2-Q3-a7UVzBLBnLCLozUKwB6W_2qHQpSVc7X2A9ehCQ6Y0cO1j9uhIYXqeAcHY3GnjSxL7kCCbuJ7ZmaKAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
دستیارسابق‌انریکه سرمربی تیم کره جنوبی شد
؛ روبرتو مورنو سرمربی۴۹ساله‌اسپانیایی‌ودستیار سابق لوئیس انریکه، به عنوان سرمربی تیم ملی فوتبال کره جنوبی منصوب شد تاجایگزین هونگ میونگ بو شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/28844" target="_blank">📅 11:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28843">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeXSB8kks4L_3rKvM4XQ8Jn7MFeGL6P8Haicw7ySSXqbP-VolS7mcsi8O3w_P0zYGRcbNPNALcJ0k8xAxw92kIPs7-nAPJOUXVed0m4GF0ukRzHF-gJI0JYR3HTVuiF3fuUAzjMhV3NUyMcWQxmICSgwqnfaiqldaZHU6--TrR3HOPdMJfub227j4fsKTortb9ntGpfuPsRNKAgx66bXRmiCRXKlzCHN_07-AjTpCjseetIACm6JyBpRcno-4N38ITGZJG8E7TvuD3i1cFNbGhEX_FQD-IrUiDjpoFTuL4doE14BJbhUnPd2oHu-JMjvIf2pVHswbStnqymYELI9Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئیس‌کمیته‌انضباطی فدراسیون فوتبال: بعد از برسی‌های کامل مشخص‌شدکه قرارداد یاسر آسانی با استقلال قانونی‌است و او مشکلی‌برای‌همراهی آبی‌ها نخواهد داشت. بدین ترتیب پرونده شکایت باشگاه‌ها ازاین بازیکن بسته شد؛ خبر ریپلای شده هم بخونید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/28843" target="_blank">📅 11:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28842">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afbdcb0fd.mp4?token=TFPFfbxiSoWdkPkdjCwv09KINlMWwQhcDqOZHJxwxWLTohQlc2AAS5rDQY53NpngP91YtJQ5kpWd46e-A2CGkQPZQssMMg9_F6LuF7r9JmK0OQFup9wECN-N29t1rwKoVJbvSm4cnAb9EyqkwdLVAgpvBB3gKtlf9fdrGyREXv_7aRhxNOSUHR58Y0pvnIOdyiTC8z2Tcdswa1zRC018IT5VmGy9DR96rtjcX5Nz95z4sVnF4tKpUuBGuS7MRUoQ1SkTsaTJ2otnPE_V6eCtUeblho2wOfof1UlPGLOKNZswpuN2jmgkFUsig139VS8Adf9yOEHnT4-gHURasqbeTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afbdcb0fd.mp4?token=TFPFfbxiSoWdkPkdjCwv09KINlMWwQhcDqOZHJxwxWLTohQlc2AAS5rDQY53NpngP91YtJQ5kpWd46e-A2CGkQPZQssMMg9_F6LuF7r9JmK0OQFup9wECN-N29t1rwKoVJbvSm4cnAb9EyqkwdLVAgpvBB3gKtlf9fdrGyREXv_7aRhxNOSUHR58Y0pvnIOdyiTC8z2Tcdswa1zRC018IT5VmGy9DR96rtjcX5Nz95z4sVnF4tKpUuBGuS7MRUoQ1SkTsaTJ2otnPE_V6eCtUeblho2wOfof1UlPGLOKNZswpuN2jmgkFUsig139VS8Adf9yOEHnT4-gHURasqbeTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
صحبت‌های جالب کریس رونالدو فوق ستاره پرتغالی باشگاه النصر درباره سختی‌هایی که کشیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/28842" target="_blank">📅 11:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28841">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYb_8v3cGHwgfUVpNaGkTnSQAzjYIhTfceIQs7XpQ6zVZP7yWVGmqqzFowIXkjdUb8pdOsim6Ho-fwhjmkD4RDpxSBPiD9GNN7q84VY-vV08uI3cGRPNYjCZeBvsN4ZJBnhwp7QEVYgoJbhpAAL9dnR59cvfUiSqMkcSwV3EYJcS9nAofy6jPynEJUoCnvu4HjvR30aoHfRhCCHk8vXqmiG9pDTPMzzjd7tKkcDoYECYSZMkL2wJhncdXtThWfOt_nvmeJTIVvHrrmhauTgruTNOHUOneJGzwgt2tkldJbjP5iOzrZtxTF3w3S1wuRVbTsl5RX-bN6l4Np3DlPk77g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب جدید بارسا درفصل‌جدید بعد از پیوستن گابریل ژسوس ستاره سابق آرسنالی‌ها به این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/28841" target="_blank">📅 11:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28840">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXEvf-aZ19lOdw4Rld6n1qTbZMjFR5q8dsv7VKjTICAqJ3pnNJbONFIobYWuusL4CBQqL0jA8nnvHrVejY39f1SbId5J2AP_006nCMeQ8CdFJme0pRTaZqGso42gjSQ-v-zDzE1_hkBcZG0q_uQC1faTjud-lLP7w2REMl8R1Y0r0r2uoNz4WKxp_xR-mwhTg3zmrdiXPH9t9k5JvZwKWbJl3ILIvLBhx8ik8JQc9sHAM6cd4rE2JCzQx1h5D6IMr2AJnl8dz5YGyvVm_M3SvZGtWE3SX4ccD6dPeaubKlZof4h1co0rEQtgoUo1ADLiwv4r5rsyHRDHAOWkeV6fvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/28840" target="_blank">📅 11:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28839">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQN-s0nHrTFvrnNk_C00l_ftfe3YGoxNn8NChCKjX-TmMaafUW0yTxqZQcBxDPBAvDuZWTyQYI9Ablo4NHX7g5iKgS6votXu_GEF_IYzFh52S6MQ8s15VlnRWCWt61vdHGUBtd_0l7m5_0SxjPGlL_tq7tIPFrOMO4cso1qdhZ8KqcUb37AkK6WOHpwjCbI4rpkGKyV4GzvfG7M1zwkroeKbmxz1bAug89BbfhkubyOidbJRB_F-8egMkvHANzjInat0FIVFDAcasMLRiAY9i3a4igy_AxWQs90_pSRlNTnSmqf2uUDl0iAeUR-zF4MJgZJcMOTJCs_7QwHGBHov2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
تکلیف نهایی داکنز نازون دیگر بازیکن خارجی استقلال نیز ظرف72ساعت‌آینده مشخص خواهد شد. یا به جمع آبی‌ها برمیگرده یااونم‌توافقی فسخ میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/28839" target="_blank">📅 10:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28838">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LudwxTjVbOZWjMI4DnNKUCdP5Gifk02athY5HWJYwysTWl86rwaddJdqLkrYCmEr83Q0CXKfGJH3RQ2ak1a-dbTr7x3SFEkG4KHOk5gCddMnawbNHkXS-jsLLtcaqjp_TTEVcxKaCTeCa04Ildq_cO8pJClcpKwJCNn2byhKdCLNBq_h8eHGZLyaahXVGMVAbgJLIY3TUjll2oWsSdSgN4JDkVrfAiCs-bMZYueXl22xpRs2x6vKasSI5lBUxs56PQavVSoNHIBi_ZajsL7WSvein2A_qu8VAgNQyQ4PaKwc7Lfqlt6kUqdglqZy8FpCoaXm0QQHx6lpXPXV7hHLfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو خرید برگ ریزون و فوق العاده الهلال ظرف 48 ساعت‌گذشته؛ گابریل مارتینلی و اولی واتکینز دو ستاره آرسنال و آستون ویلا به الهلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/28838" target="_blank">📅 10:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28837">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klJj78ndq_dLWwchWDKkSwt89uNqWxpe0fnckwyLx0Kj-J27MH_T9zlNW0jxjaBpWJAThn05LNIXwkP17zVMNXPeqFVhq7aSL03TYmjZWMvK3RYHbXSnVMmWPh-s7RpPUSfUJYuVickLYxK_OSJxHqcL0mPLfGFyYJ2Det2_MvtTwfaH6XcmY3yU2E8NqD6_YsLrpjJErEDrZRoB__lZZGa1SxdGOpZ_Jk6GfC_5LvkxVjYaWONHBdYNHuLRQZrjg5BpML73jXNlZ1frNpXPF7i-9LrZusnRWgbjrmWGmpZ3Ce3tuQm5jqlfWcpRYJ4V_dsrxypSs0RVZwGy2jXi0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
فاطیمه یوسفی فوق‌ستاره 21 ساله فوتبال بانوان ایران هستن که با عقد قراردادی به ملوان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/28837" target="_blank">📅 10:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28836">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUfBP-2yN4nJ57jxcNqWBLv81BuIfCNUhSK1UuUeXZGtv-Pzk0ZvVUwn-i6ob3zm0eoomYd6EgJJpSN3KGHi6PDSKsSrA1PEdxeGU1nA-0ZqNSBPEzF8Z_tYE3FrRDaue0jhyBK5N-ed9bDO2YThyQ0Jnf_CEa7NYz5SCTAbSMdgreYDOGLuj1RwoPAxC-yVDnKXhks_KUEzjzeZQ-FtTI9mVXcPji9cmkwC1Pqvopg8RkmVziDhisw7PycLUEdy77HyDIW12jWJSuJ2Quv6NCLxiCpFNfzFWJC5YkSI6mHEa_tKy_mji1Sv1wOLTxHza3v6Ga_Aj6_2HjrhZBnLow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امشب‌ساعت02:30 پنجره‌نقل‌وانتقالات تابستونی تموم لیگ‌های‌اروپایی بسته خواهد شد و از این به بعد باشگاه ها میتونن تنها بازیکنان آزاد رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/28836" target="_blank">📅 10:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28835">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ddec47474.mp4?token=LV5oz0VWWEvD5CSG6oLO3N5tK1W4i5FujN-4CbHqdkvlAwZeQ5JH-svd992EbFsRVBC0sCYCmqxRoTjBb37xZqVFSQhEGmZEF6nCBIF7ubCKtLVre_eo9xEWpQEK5nB6gqKqm5wID11NdgXVVHPCaS9Gv0CNtR88vh2VWX8bwh8-oHCg82Frl14S5Cderf9usVstjfiaS-guEbZm0GUEccsVZmYmavtoP8alZ4Yyr1aHEd2fahNRMvzfIkqZSKC1rHGT801hdU3HY0EPoqGM2ZBUBb2h6CAjc3pCxKcxVBtOyKzDNJN4iClCvXuCpiIa2SsK84gXakNbjCOiiGMBwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ddec47474.mp4?token=LV5oz0VWWEvD5CSG6oLO3N5tK1W4i5FujN-4CbHqdkvlAwZeQ5JH-svd992EbFsRVBC0sCYCmqxRoTjBb37xZqVFSQhEGmZEF6nCBIF7ubCKtLVre_eo9xEWpQEK5nB6gqKqm5wID11NdgXVVHPCaS9Gv0CNtR88vh2VWX8bwh8-oHCg82Frl14S5Cderf9usVstjfiaS-guEbZm0GUEccsVZmYmavtoP8alZ4Yyr1aHEd2fahNRMvzfIkqZSKC1rHGT801hdU3HY0EPoqGM2ZBUBb2h6CAjc3pCxKcxVBtOyKzDNJN4iClCvXuCpiIa2SsK84gXakNbjCOiiGMBwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
ویدیویی زببا به مناسبت خداحافظی لیونل مسی فوق‌ستاره39ساله آرژانتین از مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28835" target="_blank">📅 01:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28833">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcJz2Tgw7Bmzk8glrivRv_B2iLmZEiozTBeTnD5NTc61X7qGE01iEKzISsequ_U4sdxzhWbk_tUBfU9kUgwhDC8gHA7XeJyAO63p7Ym_n-mbxyp3MVH5WKUkkqzlQD-kFCIyQlqjSblc7ZeFNVqL6E9a_IY1hgnTC2kR_SwOKH2dN7NS1d5LNvV1oHVsglafLhTOSDrB7JV1d3Yx5P9mW3eOuXPIn5z9fdyIxpQzvRi7ddQktx6fOBWzYqeBsRwMeJXwR-BdzUFUmbn1Nve4CoKiS_F2yKwBm41ll0ccW9ecHav4_-SSsY-amooSVCfjfFPljLYCe6f-61Pt19UQiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛شروع‌هفته‌پنجم‌لیگ برتر با جدال یاران نکونام باشمس‌آذر برای حفظ صدرنشینی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28833" target="_blank">📅 01:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28832">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_s1A9yxL0xl8nDzU__r7GfyrwRs0OzsBD3faDZjw1WfxDeMQCl6qUErL6r3CiVt6Q261qSbenvfSdMn8ci4ONpYfgYLobLD6Snul6PwXYFnXyqVz9Kt9oiCaVmNqJt0u88M83ivCe0IepDlpOODurOwa9aezayDCQaAkRgJcsMFwuhu-Ii8QCmUnG02V0mCEMe2biKP8YC2_hAcD89Ne25vPs8vUpNYUZWSyduoX-Xwkr9RxrwlZRbul7miqHIbqvfZrHR5GjHfTYJpzAmSoEJWoWnkEldaTF87ufwa22JsVEX9oovAY64-hMPYgRGp7bPMiK2dqnHrJ8lFMMKcew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدار های‌‌‌ دیروز؛
برد اقتصادی آرسنال و جشنواره‌گل بلوگرانا بانمایش‌بی‌نظیر رافینیا و یامال
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28832" target="_blank">📅 01:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28831">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd806e1b22.mp4?token=EpND9X6YLOBazdPAXLtND448PiJ1SIbT1ZFWt_bCTcoDQnAaBk96KLYDMJWjUz3R9D8mPsELEu2b0B8u4XrWlBi0dF8t5DzWoeyEcZzuMDv3uBRO2lzf9iGKsdOxxKvGRNf18ZeNk-lYO5LG0XVJEwo_O8SZo6lKGTiKILDocEMN5waN8lBTWTySN5ZGbQWZXWAV3P0wyQGiYViTVuGNYrTB4JLlV3btMJgQtwJAIVa_ti2BghVUE8IMJrCz2eMnjyQcXf8zjz5Z_2FZGEKVYMFk3LmzXYn3eESAYC_L4beUxnVj-OlcGtnorKIbuR2I77gBNKJYxrl-Bc_J4owhJTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd806e1b22.mp4?token=EpND9X6YLOBazdPAXLtND448PiJ1SIbT1ZFWt_bCTcoDQnAaBk96KLYDMJWjUz3R9D8mPsELEu2b0B8u4XrWlBi0dF8t5DzWoeyEcZzuMDv3uBRO2lzf9iGKsdOxxKvGRNf18ZeNk-lYO5LG0XVJEwo_O8SZo6lKGTiKILDocEMN5waN8lBTWTySN5ZGbQWZXWAV3P0wyQGiYViTVuGNYrTB4JLlV3btMJgQtwJAIVa_ti2BghVUE8IMJrCz2eMnjyQcXf8zjz5Z_2FZGEKVYMFk3LmzXYn3eESAYC_L4beUxnVj-OlcGtnorKIbuR2I77gBNKJYxrl-Bc_J4owhJTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته سوم لالیگا|شروع طوفانی بارسا هانسی فلیک در فصل جدید با زدن 12 گل در 3 مسابقه؛ پیروزی پرگل آبی‌اناری‌ها با درخشش یامال.
🔵
بارسلونا
5️⃣
-
2️⃣
رایووایکانو
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/28831" target="_blank">📅 01:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28830">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSvavi7r6ychjwCdJ2aIe3l6TXkt5_rcf5rN-FzBcp7CqNwZD7dMhzxVmX7d36v85ZTTQVmmchohtmmqmrVjJaMd4TAlsfdZptmhIcuVcBzsFqVOwuaI-daUx5i1XyCc-pPUqkA4O48PDVtlH4SWkv-xCaIXrtBe5AHfM7MLspfHKRIOBNoEsz5pu0qxZS9lI9IoEK8fppnCIkGOJOXMfQc7AzM3J7OXDDh8gXyJM0GN_53q92ZWkyzh7KnJUQeoO4G9gTpeUZEHdcokWrZIXG9LUXywcjvhspqcME0vtCKktzgGivADebHJJ-8LmzE1ojIQJHxoRaWUC4HJHJN4rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته سوم لالیگا|شروع طوفانی بارسا هانسی فلیک در فصل جدید با زدن 12 گل در 3 مسابقه؛ پیروزی پرگل آبی‌اناری‌ها با درخشش یامال.
🔵
بارسلونا
5️⃣
-
2️⃣
رایووایکانو
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28830" target="_blank">📅 01:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28829">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3AaF3QcOIWgoJKlO2TpiBUlHrxQ22sU7DgCFh-ujy2-W6aeJMkZMe-A8FPk1DS9DZN4Z3dhj1MRrnliAkcJsFRcUKxOCFSr_9nOHNW-t-rVyfsvJpjiPlnh4md8moaQ2i0dNDYzH15fn3J8E1JHiRZmxQqdPl6jwQmc2O8FxqQQej1D3DSRYdQSfi1UV1iVdN9X3-oT91n7PwUL7DxUigUhz6cYP0XzH4Taw97FSUGZ-DYu2fHGzSbcU5JyAU6GAEZsveOmrKLLy0XgiQzUMOm1cmmMfgo9pH6Qxaafj4Ulg2rDPJTt4d3tWGuwz6iOYzbVaJOgPJfe3C_xSKep8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لالیگا|شماتیک‌ترکیب‌ بارسا برای دیدار امشب مقابل رایووایکانو؛ ساعت 23:00 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/28829" target="_blank">📅 01:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28828">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f678a57f6f.mp4?token=OC_UxofGk7XNp_5T5lYqbQxfxaOLlEMKntV2Stw5cIf9_JVGArrRVDO-8ZxCX1Z28LepkzrIKC329SqRhA85NzbjjjZP-kqKavtmQejjuinl8uTh3Hq94QoH4IqgA-gF9Vj9bD1mGcFzuVrUgFOIOlPJ4-HqWWA_Bhfo8CL24jlHiqZ0XJCkvpu4LXty_5M4RaAYOvoN8N6CChMEBoenRvT-iwlBfZQgrJ5H8jrP9vWmdSLaVQcyGYkUU6AgTrX2r5UqgNt69zFtHZMkYbo4O6k6sp-mxPUf5t9SNc1q1-P9s-MIjcNIZ4oOY4JeHOyHfthmvwT5DJoKHLWYcUaVWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f678a57f6f.mp4?token=OC_UxofGk7XNp_5T5lYqbQxfxaOLlEMKntV2Stw5cIf9_JVGArrRVDO-8ZxCX1Z28LepkzrIKC329SqRhA85NzbjjjZP-kqKavtmQejjuinl8uTh3Hq94QoH4IqgA-gF9Vj9bD1mGcFzuVrUgFOIOlPJ4-HqWWA_Bhfo8CL24jlHiqZ0XJCkvpu4LXty_5M4RaAYOvoN8N6CChMEBoenRvT-iwlBfZQgrJ5H8jrP9vWmdSLaVQcyGYkUU6AgTrX2r5UqgNt69zFtHZMkYbo4O6k6sp-mxPUf5t9SNc1q1-P9s-MIjcNIZ4oOY4JeHOyHfthmvwT5DJoKHLWYcUaVWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
باشگاه سپاهان از باشگاه‌استقلال و هواداران این تیم‌بابت‌حرکت‌زشت و زننده عارف حاجی عیدی عذر خواهی کرد؛ این باشگاه همچنیین موافقت خود را با قهرمانی باشگاه استقلال در فصل گذشته رقابت های لیگ به فدراسیون فوتبال و سازمان لیگ اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/28828" target="_blank">📅 01:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28825">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsfVHs0TQUzvfg0bTEvHy2ILKJzP-ZW53OdNWYuUZy8HG_fjGt9IVCvcqy8narR9kTQr5FIwluEeGd5kZMaUbAL9-xjPOvLNFctoS48FYR7KCo1O9TzbB1NtMGimLEseIHbhvh4yzXhNY6cmuDrjL6VXMKlwt9QuUEJ3teFQxTQTuAWbc9sfGte5jhxJQ3U9SSq9Jm8VIQ1EHq8HAFvrROEdcnUWRIuNrQRcAwhnAj_ly4G5rGPhyfcpJQualTj71eC0GRdB6TINQ7DZrv36LrIHEiRwCQ_xXLni_5NXSsp2pESLNSPqRa3-Q_hJaU0tMwcAJMbGTjaHzqRIBFq0CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مناسبت رسیدن شهرآورد پایتخت؛ مقایسه ارزشمند ترین بازیکن دو تیم استقلال
🆚
پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/28825" target="_blank">📅 00:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28824">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c6848cef.mp4?token=cUdwX-FrD7mi_EPgPDksyJrGuUhS05hx24-hjQgl8yHzAemzKWIjo_UUf12ryWUvw0Pcz360g8wEv2nm2nx54r7NOwAzfGRwACFNQpq-yCmppMjRvKdtiD7-f-u3aY13CU-vKgrdxyROkcmlgRgczHw7mkzYNum_oZ8urIQfyxoQ4-lGtmZzYS7AEomXOSEXcqVV54VpXWZubqrzDUlk8qGndfrhOVijIrWqBMzwpihFIaVdokezn66UgPYjJmTxdgttEi9GZFxuIcjb06HICcO9SlrNkC95zQ5obvyd8DzNNaX0Vvj-J9lbJCYqirt_dxItb8BYe3QTC_hzO2f1nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c6848cef.mp4?token=cUdwX-FrD7mi_EPgPDksyJrGuUhS05hx24-hjQgl8yHzAemzKWIjo_UUf12ryWUvw0Pcz360g8wEv2nm2nx54r7NOwAzfGRwACFNQpq-yCmppMjRvKdtiD7-f-u3aY13CU-vKgrdxyROkcmlgRgczHw7mkzYNum_oZ8urIQfyxoQ4-lGtmZzYS7AEomXOSEXcqVV54VpXWZubqrzDUlk8qGndfrhOVijIrWqBMzwpihFIaVdokezn66UgPYjJmTxdgttEi9GZFxuIcjb06HICcO9SlrNkC95zQ5obvyd8DzNNaX0Vvj-J9lbJCYqirt_dxItb8BYe3QTC_hzO2f1nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
ویدیویی زببا به مناسبت خداحافظی لیونل مسی فوق‌ستاره39ساله آرژانتین از مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/28824" target="_blank">📅 00:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28823">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWLFJakt-SW1oux1dtT2Brdd1GaJSekGePaHHqkJwY2XuYHs22mRXbkYdmBSqCkdjn-ryOjeiT0-BE4KbAaLGDAysSbzsk4ZKsFAWWf2g0WdWNuPBZiok4-T3TMW87lAWls1VVdCfe1T9bzw_mXhKrywWaPExwYNTGqfWFu7FE14XXIlkuxwgSj15JqcYXNTRyT_shjMLeCkmK6FA5EaLwLApi64MhfZcsbiwadyzkcs2SQHwteIfLky0RkSVM9cDFFaGle54nn4_aUkSWG3klkidldMfoECJbyG8AjyaVzqEpxzk-TLYDC9Pd-PEYJ8WNClzahvao1tELuRNHRxaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به‌مناسبت‌رسیدن شهرآورد 107 نگاهی بیندازیم به افتخارات دو باشگاه استقلال
🆚
پرسپولیس!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28823" target="_blank">📅 23:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28822">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWjPJsiS9_yuxuZQtGDgFHIpWx4rIYOPktlldaEsZIsq-ywflBVyKSOkwEfkSH0AQAMGqxPuWwTSxM5zsXlW1VHYxSUYnFzdgBtuGOdBOZTuHvRlcsoecuZUsNW6cMelLq14NloJddSfTPuFyC5VggGICtyYGqBTf_CFDjsEA27V95aMpw1CH81CP3O0eRSZpJbfflXyLwyIOSkYa_HwHpM74CoFYjoBoFJTP6TZrG1EHNDFEs56SJlZ3OTvzGNHvQI_jGGpC6-yykmlPCXjsBFNBhjsoJ4IK2XlWI_vEds0NXdjcWtJG5dqrS14EfIcKyVrrNpWRrzVh3HSHaFsLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل‌مسی؛ از کوچه‌های‌روزاریو تا قهرمان ملی آرژانتین در جام جهانی  دیگر لئو‌ را با لباس آلبی‌سلسته نخواهیم دید. "خداحافظی‌ام را در تاریخ ۲۱ ژوئیه ، ۲ روز پس از فینال جام جهانی نوشتم. امروز ، پس از فوت پدرم بیش از پیش به درستی این تصمیم اطمینان دارم"
⚪️
…</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28822" target="_blank">📅 23:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28821">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sh7nsayVYSYXPEzIXvP2qI9lHTxJPMxVw6yOA6snt9R3KK2P3J4AgB59kbYObz_A1hLI-T1LKnJ95sb018ppaxED1QUbLiEWcL8zDTNbqLeSmy1q5JFmfsOsxhylD7CRJRj4W7NsmQThJk2JZHUDUQkZjs7d-16VDhoSteLXpMWx8-hjn8rNMha8awjcKxZbj9v-4Qdkti_OciwdHZ_j1cFZvfAGeAfa3MOa-PuBJTbaVJ7NarvFCtdTvVACHJTAbMhJT3NJUFoU-LEIV4wFIu4pBqfgOyzLIsx4zYD_dpiMXFgbppHn20sFsnN4eEvBwBKLwYhK0SyNs9f_axvLTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف شایعاتی که امروز مطرح شد؛ همانطور که دو روزپیش‌گفتیم‌تمام‌مصدومان دو تیم استقلال و پرسپولیس یعنی‌مهران‌احمدی، رستم‌آشورماتف، جلال الدین ماشاریپوف و سیدابوالفضل جلالی درلیست دو تیم برای دربی قرار خواهند گرفت و مشکلی برای این مسابقه نخواهد داشت. حالا…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28821" target="_blank">📅 23:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28820">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d24f702f0.mp4?token=fP35v-uyvTAYPnzjX4Inf0DsDICkxgG4k0N5V3qTtIHnK4zmftRsOburuy2h8QCulj_HffXeJu702lsnrLwWjTt1JwWZ_vE7nRxDajWU9uclVMttS2ABeGxZ3YMX4GYoGfa7UTElcLtyb1EkAjiuAOj1vgdKmjdz7dNVOFD-LwhQMgLXYZXiLmy8ftJrXZ4kdCzHLxaVxQre2dRIkqLFCZOSpsCHeckNGj89bDUJ9WKuhdHrD-Pqu-JIHdT11iVRGfdHWY_pY9i0ONqR5HsVsHpmwT27Vm9coIYG27ieIBlVxlLhTwD6KpoIDPDMAVIjYlAchUthx7wdZICIFsuP5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d24f702f0.mp4?token=fP35v-uyvTAYPnzjX4Inf0DsDICkxgG4k0N5V3qTtIHnK4zmftRsOburuy2h8QCulj_HffXeJu702lsnrLwWjTt1JwWZ_vE7nRxDajWU9uclVMttS2ABeGxZ3YMX4GYoGfa7UTElcLtyb1EkAjiuAOj1vgdKmjdz7dNVOFD-LwhQMgLXYZXiLmy8ftJrXZ4kdCzHLxaVxQre2dRIkqLFCZOSpsCHeckNGj89bDUJ9WKuhdHrD-Pqu-JIHdT11iVRGfdHWY_pY9i0ONqR5HsVsHpmwT27Vm9coIYG27ieIBlVxlLhTwD6KpoIDPDMAVIjYlAchUthx7wdZICIFsuP5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر محمدی هم یه تنه تمامی قوانین فیزیک رو داره نقض می‌کنه؛ در جدیدترین اقدام این پرتاب 45 متری رو در لیگ یک روسیه انجام داده که کرک و پر تموم رسانه‌های دنیا از این پرتاباش ریخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/28820" target="_blank">📅 22:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28819">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SN2xCb9r06UDxitnGjw6woho5hVpMmHY-hZaewpFP77u_W1V-47B6mGpKlulZI-810bGCpt8dKkdpMY0bAybs2ChMeodgl_JJ9--nFc8PNCdGVPhHu4o8-Wy8oDPYKiBErtEPC64RIhr4w9hGs2xPuc5JwpykSh3Pj4nFv80-tp3FsGkTuUaO55wrrG_ADhk-YLwyqGMpg1oO2uSmuVYuvvtj-aNJwQYk0RkOSF4Zp1A79cMXvbpYLXYTVNfSzUTGj3iMvOX5bwQCiueIOk269hCNPZwktM8Ih5Aq1L-N1rO3HOIaoHmlUeBHUy3ELq5_0q234zxqNXmtUQejPOoHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به‌مناسبت‌شهرآورد 107 استقلال
🆚
پرسپولیس نگاهی بیندازیم به دیر هنگام ترین گل‌های این تقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28819" target="_blank">📅 22:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28818">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGjbcX_nicJCeMEun5is_VoVvCH3I9jX4NZXzjUb6S5JIbhVOpXqTWLmMTqZ6QWwXHDceHbT_MPmHBec0C2ZpjXuz1qojX3G0hOfZgscx48fPAUbsmAjKi1W8mTAPU-ljYoe84DYuv3Dk2mgbGJOQueUoi_Q4lvmuS_mHou8yMQNzgQVPPGOhSh1fY5up9R4Gb5ynacNnS2igvL3LDB0dzRolUJMC2mRT5UYgwuKpsqZ0SmnryXxQTAsmliNx45RNpknjnJ6Z_o8wGK7utjQV9a5qww5KOwnKBDXIoZyvKT9H9TkC-n5c3fbWBzwGtE9mF5uLSsZRU2FvqWz05Mc3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
ایلیمان اندیایه وینگر راست 26 ساله سنگالی اورتون باقراردادی 5 ساله به منچسترسیتی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28818" target="_blank">📅 21:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28817">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJ9ORJ1yBGqQ0W3L8nSB1s4pr8JZ3dkSjhhyV3gW5lwDUsMB4QcVhJeC51BCdjv7A7b90LL0S_NImcXYHNekBOcr_M8mbl3ZBUehBbQIOvm7c7avLIWDRVRG-lfRPmroijBntk083i9mbjYLRPvKVma3AaRiFHdtuODNR7kKKe20OpFxA-7LUvRvXig-ljf9GuiTqN_K10-h3kwBRvTHFcahOCsKTQVHx5P7zgrGK5DobcKBE-26qN_CZSYHov7GSH3uWlmEeoVMyYxUAZ0hluzfJRw4A1PyHjWbk91PpKUICrO5DiDH-tDMFJYCRgyfIhdh-GMDRfqFe9jNkXOMRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لالیگا
|شماتیک‌ترکیب‌ بارسا برای دیدار امشب مقابل رایووایکانو؛ ساعت 23:00 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28817" target="_blank">📅 21:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28816">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjGN_piAvnN09P7O8ejBnVJerOe8xYA52OEKMTawmxXR-5q4U_cZ_fwV1D56e7BzXIzsURybS3bDCPoSb7Z68m8uk_zHYmuA2E_qsyKmVGEnn0UNw10m07WbOG6-UCTQycw1hHww_Ng2IWqqPnjUhJpkTkisD7VL3o382fu99Y1oJTlgaHdkVjzwJ8tXG1n0K9HKO4Yw905dvKrdbuxCBBBCsuj7KI8e_ce_ljjNjJXmn-__nHtp407k0ev9secGJthhLrkQiwHWoQ9HhIvGkiD-5gQM-yWlGgPJStHJY4sS3X4LeUMnVUnqH9dlBlpJXx24MXdTc2bH3wwog4_cOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28816" target="_blank">📅 21:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28815">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‼️
به‌مناسبت‌شهرآورد 107 استقلال
🆚
پرسپولیس نگاهی بیندازیم به دیر هنگام ترین گل‌های این تقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/28815" target="_blank">📅 21:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28814">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYn17OzAmP5CLIQO5rsSIjbBxTQlXqzlrBm4qy57eDZS2N7auefAf0e1IMTvt75H41rqPm5xaAG2J8RUqP2yqUDkN77u3hisPyMF--0KHH0PswL4tBV_Qy-Tc6f3PL1XybeEEEByw3oVSQfM3UxiRO8SYNu7fARVIH8m94X_NmdetwPVZcu2UgBEd9R8Op_4d97AXF-NnzsCsBoOmj29dT5g92fE8ZbedPb3wE8QTQq_6Pln7Ywdto9aeuB7-Q9W7YQQuXu4KZg43kLvJCdGF4Sk6b2YmLtpaGwFrm_NDBRD5VHqB4UsgqZdQ4tiez4--3ZxvLhM0YOLiPH2A8Rz6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌اسامی داوران هفته پنجم لیگ برتر؛ موعود بنیادی فرد رسما داور شهرآورد 107 پایتخت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/28814" target="_blank">📅 20:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28813">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BigYFvCb4XBVvd6nw9i3dk7s4BarhUG9PBL394e6jnegODmUQaS8S83MS8sa_xNVIKhn4Si1PlKA_VKpAk4MNue7GxxfOepMcu8rREEeOwhPf3O6wbw32e8CX-N2vE7REb9U2qZJhAz_45mEV6v5za16dqO8dD8d8npCBCUA6_UwNtOsM5YjSZuzeXmYy5LJLXg1zEL7gfqF2Woo-zClt7TvffDjpN5CIBoSlfRo2Ick-Qseq0ZedXBJDQdZuEMeuu-8LbJB5Q2zgJD3j0ln6CYpqeQI2N05zklW2ahV0zCBMRx_ibg781D-pUK7ohQXgKrGIUSEjUXPTOvdSYqq5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
جای‌داوروسط و داوراتاق VAR شهرآورد پایتخت عوض شد؛ موعود بنیای‌فر بعنوان داور وسط دیدار روز چهار شنبه استقلال
🆚
پرسپولیس انتخاب شده و سازمان لیگ فردا این خبر رو منتشر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/28813" target="_blank">📅 20:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28812">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gs6jS9uPXZpNJ-7x49QUTu4exdQ6SfpGhZovRJ2K9kcPv_o4CZsw6z9H8DH4MpkCgRi2iZRcPVdSHzi0STbEgZspBs1VRQHDplFxIc0C3aZLDU738AWGWTI1zeOrU9zJ_avNiWBSGvZQzBvCWM1Qw_DO8LL6UHpESqg-6gu2ieyzeitfU9GzWWVtUqifABWj5Ajn2z5I3nm85AKj5LgGfpYqPYA1FIqcYlrdYF6EJHltXsxIlqbKfPEusIIvqOOWi_-hnbwHRl81AYhdncf9E82R6nnDXTBCiVlK79UPSK91CetEsgIQwj3PdxWsjDSpxY5Gbsw2m54Y8p-nMJap1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
آنتونیوآدان دروازه‌بان‌فصل‌قبل استقلال رسما اعلام کرد که بخاطرشرایط‌جنگی به ایران باز نخواهد گشت و مطالبات فصل گذشته اش رو نیز بخشیده و هیچ شکایتی از آبی پوشان به فیفا نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28812" target="_blank">📅 20:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28811">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVfjgGy_Cni3R1tW1oR3eidLqEBEprUmvFLNDAq8jzwq1CP5SLRezCG0iuCafF9VPaaqDbkaUxfSWgo7OIwWlIVdSUJCBOhqcQd13o4yPSNTuyL1TEc_DuKX-NafMmnlCB1AdSoGJ1Dm-dTRjttcZKRmePxJWc0jQ7ayHvcv7sS2L1wwLqgDP5ZgByn9AUaH-T4vzZ6kj4hmsbzhSLwRgINYB2ylP2HpnkBWDQhJJvM0_BLBuSXH4ZTOj9Uez5lt5L8BYS2srl_lCD7QwwgvPfzBKxZ5Ou7d3wq0Ekdzl7F0rrlT2CYNPJXUW15Xta5y9lVTBNqL_XqlQ6EDonj4gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
علی‌تاجرنیا رئیس‌هیات‌مدیره باشگاه استقلال: اتفاقات‌مثبتی برای اهدای جام قهرمانی فصل گذشته لیگ برتر به باشگاه استقلال رخ داده و به زودی اخبار رسمی دراین باره منتشر خواهدشد. در تلاش هستیم که‌زودتر آنتونیو آدان و نازون رو به تیم اضافه کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28811" target="_blank">📅 20:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28810">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDBidFtX49fxAYobOwHqVoNuYXKl4wCB9uiA_H0uJjhboDe8my8iNDBJl2SZE719r8_tTUzamtAp1j9bbtdjegy5ULZkJQBzmJfM5pLm7KC_D4f7BSDhn-s_QlYtix8aS-pLrVZ7l4m1cnQ_x5JySW7FEOI4B1mycavQ1UxIlvpeWPQkVUiYGfwf8aW_i4tHezFZiFYLl3wFpvGecUjWSsZMQxWGuhxmQw1R_V63T7q7QSMGKv75wxgLwJFgNvwbAfR0BuCgKtYRoRgNnU9lBi8D0JEY5SuoyBBtAWF4-RR5aX9E5nFZlMDiDzTFu2A4HBwOfFTRUVvlQ1c4rJCPjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#فوری؛ انزو فرناندز ستاره آرژانتینی چلسی با عقدقراردادی چهارساله به منچسترسیتی پیوست. فابریزیو رومانو بزودی هیر وی گو رو کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28810" target="_blank">📅 20:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28808">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVBOJMMSi7qqfbOmsAAuV_HMW_Cs_gV9ekddXVPctjwoUi3mrbmled1qAcnLe1Cfo5k6uGdANWDJkaB6JGZHRW3cDBVOlcGHaWrDrWywcE892Ox87Y05jgM-m_28dx8Srx_V3yblDgp35MP-uyFYnsczZNXLJpK0DDRBWjtxN5ZXGXpY4BI_9D9Tidum2Sd6yCy-mimBwdFb7jG0fPqoE4BS28dmAIzzZtN3cXL-cEcEgS2tb-37yBplCrCJwiNSgrB4D1jRHvVVswsSZ_MPfFA9AQ82t5TPq22ie8CkhbY25XMtVwhkkiD0AVviUuvs-A6LiYjEFmZRjw3qDxXUlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇱
#فوری؛دیویداورنشتاین: کودی گاکپو ستاره هلندی لیورپول تصمیم نهایی خود را برای پیوستن به منچسترسیتی‌گرفته و این‌انتقال بزودی انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28808" target="_blank">📅 19:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28807">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cae4f4c53.mp4?token=P0umw6gICTy7p8GfDNLTudZTN5Kp-3hQRQgIWcGFk_-oO29Ql92BmvfNpJbeyak5VqSYwLVn-h0u3ZaJI5ogXJ9Yf1dHtp8oj7GKtyKAJEJCU7ufJQoFbwY7GFWDu3cW2gDvn1ogO0wLy86OZNDkF-8W5NAtA2xN3MZLP74Jd5-9jHVtHHEVI1IsmTDb3iS8VzNcpGvXcdVsp6trbmvDjygIlPdW9Ww2_ozHJI80xD4aX3hoXNwGHlRpoRnWBmeMOxMOtJF8RYn185g6XfznmxyCpV83gBbCp93Uw3lzlPJSeBL9TVK8auZdmx29uLEN3gIrmUaZApjmCmk3AXzjfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cae4f4c53.mp4?token=P0umw6gICTy7p8GfDNLTudZTN5Kp-3hQRQgIWcGFk_-oO29Ql92BmvfNpJbeyak5VqSYwLVn-h0u3ZaJI5ogXJ9Yf1dHtp8oj7GKtyKAJEJCU7ufJQoFbwY7GFWDu3cW2gDvn1ogO0wLy86OZNDkF-8W5NAtA2xN3MZLP74Jd5-9jHVtHHEVI1IsmTDb3iS8VzNcpGvXcdVsp6trbmvDjygIlPdW9Ww2_ozHJI80xD4aX3hoXNwGHlRpoRnWBmeMOxMOtJF8RYn185g6XfznmxyCpV83gBbCp93Uw3lzlPJSeBL9TVK8auZdmx29uLEN3gIrmUaZApjmCmk3AXzjfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
لیونل‌مسی‌فوق‌ستاره تیم‌ملی آرژانتین با انتشار پستی رسما از بازی‌های ملی خدافظی کرد و اعلام کرد که دیگر برای تیم ملی آرزانتین بازی نخواهد کرد. خبر شوکه‌ کننده‌ای بود واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28807" target="_blank">📅 19:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28805">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C-Mfvb6bjKIZm2TpxfqVUmX_eYllN2XczOO-wR034_i_lBNPM0osw4zVA_GdwP2jQFyaCasMzblOoZpaMyg6pa1tbmeGfVJX2-pAAA2ezL-ZxB0awgSvAtK8neg9eouiyFucipspO6rupZruG_16M1ENFrZoEA_GU1MLMBkpwpyHX6v0FAJQ0ympbiFNhmo2D0lTBd-NTNzOaiTymbg_Z-fogcFpvtrRoahibywe3QL7The2s9Q1ACJX5gx0UigtXN1iIKk-CnBWp4G9CL_vjtnksTMu5w7stZW-_27NIN5FAQ422eggNFJPLy0QUlVnQfGMe2-8TD2oAk31X-vjBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vqvHpSwChTueaGlrVC8hwbyn3ZSGpx4Pja9tI6C_zL_Wj4Mdr_mA8_sx2tVSZitP9iit-CLsgMJICWGOFn-ZyweUBMy3KDUIL4OKQOTU0dhgjVYIEIzAYRxDZRX5V4zXI0vo_nhjh_FIAQom47n4uZIU5SfrMCiokTrSiq2Ki2JMyzCsM4eZ6DOIl8n7LEqFw9QJcshNDpDXRck2Fw2gOD_FMk708_41W32Hie3uVFawuZZ1GhjclOF2HwRVylBaqvbtcjw12jU9E6DK4iC42YppBsvRSTXAcvmxL8VJH6RlB7pp6oWH1a6srh6OWwh6hqjnYDjdmjqqQ0uE5J-lJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
🤩
لیونل‌مسی‌فوق‌ستاره تیم‌ملی آرژانتین با انتشار پستی رسما از بازی‌های ملی خدافظی کرد و اعلام کرد که دیگر برای تیم ملی آرزانتین بازی نخواهد کرد. خبر شوکه‌ کننده‌ای بود واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28805" target="_blank">📅 18:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28804">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDo37TsF3na8FJO7nhUJewwTake_ieB_JnSQADBwZ0z7su3PpyMpImclV5NU7IXH3oODxPb_wCa6W6CcKUn_QU2d8FTeUZSJk2nDzswjx9zMW6zlJtf_FwMrSTW5WOHV7oqAR8hDZT_3ug_mqieWdAO1WfpAfxn1B0zomI2UrM_lSu9VmhoBn4DxWESs6aYqswA8JTy3UZO0boxBYzOkfB4Q6UnsBapjzlGFlJuHWTEJ1ssCHljgyiQBezjNP_HQmd4ckIbQfLHJBmSvw5gU_f7j9kRAXZaHq2whwluXfCdfVIbtieYQBrTNmo__P-p1UfFWhNRvYRGtHJYhFVguSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف شایعاتی که امروز مطرح شد؛ همانطور که دو روزپیش‌گفتیم‌تمام‌مصدومان دو تیم استقلال و پرسپولیس یعنی‌مهران‌احمدی، رستم‌آشورماتف، جلال الدین ماشاریپوف و سیدابوالفضل جلالی درلیست دو تیم برای دربی قرار خواهند گرفت و مشکلی برای این مسابقه نخواهد داشت. حالا…</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28804" target="_blank">📅 18:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28803">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhc0UG6eO5jWwNOdj25bLP5mqyc7yXGkEVxFT7x_5LOkDlQ7M6TO6m_wtM0-VM015xdm7mYZHnBtS--EH2CidLawehQS6lpM94KGYQzewFMTsbOHkB5n6gAFNvUVwXESFvDQA1BJ9AJOrH0M7AOSIFQy4SQxch9lWEc8oYzqBiSROsJ2LjyINBqCCs7dhYYGtqNCo6O9OAeiuMkH2aDt9klDrQse1arHz_Ht7ITH45MDu_MV1IEku1qe5HAsZiNYOiU2G_RMWGSqJkBuU376hz4iEWmoCJRrfsYkOEhVcPlMu4zAxt65hX0j7emsX-1qt9DBRUYLMOzax8oFmGd0TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
👤
عملکرد فوق العاده لیونل مسی 39 ساله با پیراهن اینترمیامی: 98 گل‌زده درتنها 111 مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28803" target="_blank">📅 17:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28802">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcmVJRVkLPlREyYk4uJsCLDYf8ML-zov7mlj-9AaX1xbKUkArEZYQntfd0nyS0RwcdyrGGmttTbYPG69gKrA__tRxHVjfGBrUDi5gsn9_OZKSX6idZce8PWc4TKwwLr4tvsTwS_nW2s8au35zr-Fo0-CJ2zcd6LgA9loyTevUBgltoM4WYE0ROemi5AmfCwLZ7KEB-aIOIjNh6g94TlY7McQXuQ4GQ8DGRlAdX2Fc9RUSWejVkNCRS8UkYzyAidHeYW_kdy4bbSGQEt6BdikxEM_Pxc4cqwN2iR1jTQH834sYAfn4M07XtKhrLaRhdoD0s4bzh_JG2iBbs4m-8WUTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
#تکمیلی؛ سانتی‌آئونا: کریم بنزما ستاره 38 ساله فرانسوی‌قراردادش رو باباشگاه الهلال عربستان فسخ کرد و رسما از جمع آبی‌های عربستان جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/28802" target="_blank">📅 17:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28801">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwSQww9ILk8fnYSiBRRL6DJYDaiXyZvYsl7erX5A0DzBkQa-cwLQlRecfswVBWkTqrKcJBJeRXn2lVJ7-SlySFOJR075vLYJhKFUoGIGbRvqSSpU_FPS78TDhKnEzTRCh-y3XkM2G5RKh8jz7SwSp16UCGUIXOD3y5avg49yzsNx5JS3saEnKCy8XYtTRZY07BfBMydP1HhMrOuS9pmSk5iTBwIzgNLCwtohMjjmSK-yhBk5sBob19BdmmPQgY9lZk2ePlfjgAXCEl_n1MOojl5M7qxeD1kWbuzAfkWjrWJbOop6747Yp_cTTfDXrXktKUt3jfB_6i5iTjHdS_VVgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
سید ابوالفضل جلالی، مهران احمدی و رستم آشورماتف سه‌بازیکن‌مصدوم سرخابی‌های پایتخت به دیدارحساس‌شهراوردپایتخت رسیدند. تقابل‌ بزرگ دو تیم استقلال
🆚
پرسپولیس یازده شهریورماه ساعت 19:30 در نقش جهان اصفهان برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/28801" target="_blank">📅 17:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28800">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJVddP0XfyYI-HWR9KlYxqZQbM0ik7UZdjLQx0VcK-eTbUJ6pWSpLS_LTuSIOkffzejLmvCGJcYM7fhbpsWU1Uw3R1S2vYLgg5KGUvamPsTNP46RvAS01r-N28qveaULjbzXaP8RE-asoU1Tp9_KNhNYq7yqmQbZBKnTOR_UKcbnIUgP389n5o49sZ8OP-Yc2qTTTu--hVoZeefBzg5969fhF777XvXlXGfZoB5uqRtj7_ZLFERh-NZqA4PIdVri_CjpUCJVF4Vd3XX4FoyIBhjWwEgG-hjXpuEKAVopiWf-r40LStDX9JVKBXVWTWQw5SMOpXfj4XCPgkNyc_zAlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رونمایی رسمی باشگاه لیورپول از بردلی بارکولا ستاره فرانسوی جدید لک لک‌ها. لیورپول برای این انتقال 106+ 17 میلیون پوند هزینه کرده است.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28800" target="_blank">📅 16:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28799">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f80bffe56.mp4?token=GIluwOCU-1CeOUDzl0GlK8VCpDLVe864aT57sWSgPBRDhRtwHgrdlrC61KXa_SV0NFTr_w_q70KiOOP-mArnS1buluo76MIl_8CnI1sbo1N2Euy0vODViUwCHuq2ljJvhkpgyaZWY8Ib7kcN8Kx4-o7Ks8j1OKIQTMb8Q4rO_0rbt3V_A6mxeIWZ0EDnN9tk-a8sIR6RtHJ9rUBZsSUsKMwoDuUes401KP_xi6BCV8sLRwH_d_ZyJqmCnAhhJv2lMo-mbW31KUHPyXgOLgLhGUKs2Qx9T9cgb1gp1_1OWh-tyit_Li1h3s6UvoGGU61Z3sgJMYHQoIubzb8GyktE7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f80bffe56.mp4?token=GIluwOCU-1CeOUDzl0GlK8VCpDLVe864aT57sWSgPBRDhRtwHgrdlrC61KXa_SV0NFTr_w_q70KiOOP-mArnS1buluo76MIl_8CnI1sbo1N2Euy0vODViUwCHuq2ljJvhkpgyaZWY8Ib7kcN8Kx4-o7Ks8j1OKIQTMb8Q4rO_0rbt3V_A6mxeIWZ0EDnN9tk-a8sIR6RtHJ9rUBZsSUsKMwoDuUes401KP_xi6BCV8sLRwH_d_ZyJqmCnAhhJv2lMo-mbW31KUHPyXgOLgLhGUKs2Qx9T9cgb1gp1_1OWh-tyit_Li1h3s6UvoGGU61Z3sgJMYHQoIubzb8GyktE7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌جالب‌از استادیومی‌که.دولت تاجیکستان در عرض دو سال ساخته. اینجا هم ماشالله با وجود حدود سه سال هنوز ورزشگاه ازادی بازسازی نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28799" target="_blank">📅 16:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28798">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faeb0b6b1c.mp4?token=rG-AgfKgteHKNnLGdxUNO681F21BJoA2u1V6Ad3K6uaTCySNLxbjVH_DY68x0t9u3hl_ioXYNdQPtMYFpQWutbqVP3t68g2dEw779xvfeccWuuosJlGX4xkhhAcH-WUs_rwtRWQPRqKUNSqNSkZwhDfxUYDDUNAIWlw1c9qHOSM5d6esKS5kExGK8rCxprSeDYLJLLaz934CUZtJaGQqDiATDDg-RfmX172UimfRVZJ-36fxY5_uTcYJ1-uqYgooTWHsUqhabn-2m9clwP0NZo8NzICLM2EM0mN7qnUSl9b9H8IYYElbOKB1VDklTamDYKEC1w3quQvTQuKI-q3WVSiEtgsuUA2MUBJ64-p-cVvns0_28nsZefcZNFvkbJbPQnLk2e_brLZ0y1T6wAZ8Qn4wRta_Cdm58Z8jSuL7wwGQMYvFJ8mOEXtDFAuSIROvYoraIh-Y1eUs7-fDPfH8-XggHGcv2AdlFCarpljdwq2B4aS1Zmkw0z-_1lAm0alJlN7aYwCbBwhsezDONcMtuJ0I0jAz3xtlP1O2erQ8kqGs26kWb17QB3Ng6cDQgmaMhyPPYJfMCE6eJ9h7UTQRuvkhnwlGCKDHRqdsdO6x12X0yiJwzgG1ouv1FYBnYC19x64sBzAsRTEz8PMzLrQ2trIQRS7K-ywVoLIBukZ9aOc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faeb0b6b1c.mp4?token=rG-AgfKgteHKNnLGdxUNO681F21BJoA2u1V6Ad3K6uaTCySNLxbjVH_DY68x0t9u3hl_ioXYNdQPtMYFpQWutbqVP3t68g2dEw779xvfeccWuuosJlGX4xkhhAcH-WUs_rwtRWQPRqKUNSqNSkZwhDfxUYDDUNAIWlw1c9qHOSM5d6esKS5kExGK8rCxprSeDYLJLLaz934CUZtJaGQqDiATDDg-RfmX172UimfRVZJ-36fxY5_uTcYJ1-uqYgooTWHsUqhabn-2m9clwP0NZo8NzICLM2EM0mN7qnUSl9b9H8IYYElbOKB1VDklTamDYKEC1w3quQvTQuKI-q3WVSiEtgsuUA2MUBJ64-p-cVvns0_28nsZefcZNFvkbJbPQnLk2e_brLZ0y1T6wAZ8Qn4wRta_Cdm58Z8jSuL7wwGQMYvFJ8mOEXtDFAuSIROvYoraIh-Y1eUs7-fDPfH8-XggHGcv2AdlFCarpljdwq2B4aS1Zmkw0z-_1lAm0alJlN7aYwCbBwhsezDONcMtuJ0I0jAz3xtlP1O2erQ8kqGs26kWb17QB3Ng6cDQgmaMhyPPYJfMCE6eJ9h7UTQRuvkhnwlGCKDHRqdsdO6x12X0yiJwzgG1ouv1FYBnYC19x64sBzAsRTEz8PMzLrQ2trIQRS7K-ywVoLIBukZ9aOc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔵
باشگاه پاریسن ژرمن در این پنجره با فروش پنج‌ستاره‌خود 335 میلیون یورو درامد کسب کرده‌. البته انتقال بردلی بارکولا هنوز رسمی نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28798" target="_blank">📅 16:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28797">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3ujTkPQ63Fmn4VdpLeiakqB9NahMJyotypOsz-naNaKiIwk0BG2yXY5nmYoBhAD1Guw_N8Zypg6_QBnJYDtibMicKnoDLMweMs4IfA32LR-AH5g6b2Dqx6Tuw-qnc3HlP0vRPhuZ34qZonhnduJK9GE0kpZs9J_rk7TdQPI41h9Q4g3OXflZR18mZLW_5uUglXpmbrPLa9oksw-d0gSBJ7j1exO6E_kOF6wBWKz2V4hmsT4WeumUjRSUUYCMLYvTLpU-u9IEe7txs7w-JuDx8k3ZJgsslYYKL78HLX5dcYog7Fqvdyt_9BeLG81Kv0Nw8WAv9uzFk7Y8zeBSN9NaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
خبرنگار رسمی باشگاه‌گالاتاسرای ترکیه هستند که معتقده این تیم امسال قهرمان سوپرلیگ ترکیه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28797" target="_blank">📅 15:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28796">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-AiQDZlKCpzI7I_C_TOQfngbWvG3dUcFC_mGxd6CL15507HNI3AY8hQO9u4QwiJblh5pMiTTZOHSLuR6Cs7Z42ggA9y63bWSjZJOLaQIaeXKajDc4T4oisS-Z21-0L19JmImgyOdUmFVMrBvdof7HKhby3MLYh9lsgIz_KQL-cN6X3upAqP4OlVxrDU2XMNBBemgARcyToh3FZ0yvxwHVtTHxpoDhlS_daFLW4Xb7ISvHX1V4-1VxlnNPshBzWQD8kpMrTl7DjsWG9aytKXsmOeF0nfd8KVi2_KE_zFuupv40GKLAd9IJCU94PdVg2e_eSnybW-i2s4d2a_Zd6k3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛ درخصوص عزیز گانیف ستاره تیم ملی ازبکستان؛ پیشنهاد مالی باشگاه تراکتور بالاتر از پیشنهاد باشگاه استقلال است اما مدیر برنامه یاسر آسانی در حال تلاشه که گانیف 29 ساله استقلال رو انتخاب کنه و با آبی‌ها قراردادی سه ساله امضا کنه سپس بعنوان بازیکن‌قرضی‌راهی…</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28796" target="_blank">📅 14:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28795">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLGYI_XPc2ISKTf7uFVVxuK5-3sPfsqqu3cmB-CnhBQWG1PjJaUGbp5LE0npE3fy8_JU_pD9HYYm7s5zq39CfnoP_9-8-MKJ5XVjmc8mY4b5nfwdEtxDzI15bBtO7wxiseNR6srmknV1ykf_drC3qpEai5ATRnom67ZFwWduFMzbtuIlfTZ5Fr_7XjmzMOgHx9X26NojDR83XA9PmtymAGty1Rds6bQ3CAzgw1c4VuoM8vV5FhvBUzchnrIiUOknVjVweMw2e5c0jYo4kVb_LG0EbV9f2rnUiZbe1Ek_E28IbJMlIExxPM1ZkXTs1T-89Hn7JEQYWFtyUkaFkCFKQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه رییکای کرواسی بزودی از محمد محبی خرید جدید خود رونمایی میکنه. قرارداد دو ساله و رقم بند فسخ یک میلیون دلار توافق شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/28795" target="_blank">📅 14:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28794">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔵
🔴
درفاصله 48 ساعت تاشهراورد 107 پایتخت؛ ویدیویی ببینیم از زیباترین گل‌های تاریخ این مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28794" target="_blank">📅 14:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28793">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4XKGjkkzsOwU5BxlP9wyE9Ko1QSpVxacdBJHJKCM8fhKfAwN58lLdUotZraO7AgP0Y1AG4gmlI07coJ-RTGkaW_gdOF-Izah0L3GkbjowLWpq0jya_56wWvR_yADne4cOBb3pPyzMQKdv1LR5317D2ReYtzw8Yns3izDRA0E02O9NWqE14a07z1lfDQatqXvmSy60AdhW_yqmRenjvEJsn__-X5kV95QOL33pHsO7OJWn7NnDrVya5xVQZL3b3CG0D7T3H9kd0mxvmXw6XlD1Jw0NWPrvP3qvo7k4x0Zcv2f7P5KQJUzNIYzifFGu-ezoyIKhnKPOc3qJlLy1qDKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های کرواسی: آفر باشگاه رییکا به محمد محبی دو ساله به ارزش 1.6 میلیون دلار بوده. یعنی سالی 800 هزار دلار بود. پیشنهاد استقلال به محبی برای پیوستن‌درنیم‌فصل سالانه 1.2 میلیون‌دلار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/28793" target="_blank">📅 13:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28792">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcBLmS8XxyJ7ObywkNSYmeYNdG2919u66BHgfmoHUvusHsTG-wvJrrsMbqOySumq5e0IEcGkKfUi5ehftXmzH9KwKrr7F5RAVECuVkVe-hmE9lbwHWsoAK_xCo1PGjTctUAoauiGfvPL0ykbc6hfO84oj3qIITlTOnsVUezxO0rhYa9DmUNS4z7TEOW9KyKf169-p0-B2DunVMK4KhRDg_nfGhj8JA9h7E9BlSGqKZH-BwLjoCl6odeJFjkV7KxKpRU6M9ivOIxoQnBtMVKdQTnn9ibI9YDSh9WONXEwudHfxVfflLR6Wop4BPO5nJhCKBgTKcv1x9-x-nA5EBwHKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ به احتمال فراوان موعود بنیادی فر هم بعنوان داور اتاق VAR شهراورد انتخاب میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/28792" target="_blank">📅 13:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28791">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/627b425286.mp4?token=DEHH4SZfYWhKWweS5N8ARRDc5mAwqEjiVqeTbinYsz34HljGZKLVhmdWjlbJkke9kivysAQaKOXbubc_J0JiHpv41VmSFRRsTVjwrvX7bLeYXfIdGut70qdgEeJPhr1EcSbztySIDkm7KrgIp06v-y41AK8GuUYOLZG4xgisGeF2R39ahYWv4iu0OZX_kHspXzxAdZI-DOU8SLlaXQqNHDqFeqPMLVe9x2XUBwXV2AIkRTR5K_udZvg3CbMsX0-qp1XHrjjwQtE9z3F_pkw8qL_Rtr1HUMou48SuSKO4u7cQTQaUBB9jmipOfAARAfEdGBdxrRDnjlT7wGlNDkMiJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/627b425286.mp4?token=DEHH4SZfYWhKWweS5N8ARRDc5mAwqEjiVqeTbinYsz34HljGZKLVhmdWjlbJkke9kivysAQaKOXbubc_J0JiHpv41VmSFRRsTVjwrvX7bLeYXfIdGut70qdgEeJPhr1EcSbztySIDkm7KrgIp06v-y41AK8GuUYOLZG4xgisGeF2R39ahYWv4iu0OZX_kHspXzxAdZI-DOU8SLlaXQqNHDqFeqPMLVe9x2XUBwXV2AIkRTR5K_udZvg3CbMsX0-qp1XHrjjwQtE9z3F_pkw8qL_Rtr1HUMou48SuSKO4u7cQTQaUBB9jmipOfAARAfEdGBdxrRDnjlT7wGlNDkMiJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
بااعلام فلورین‌پلتنبرگ: میکل بازا پسر خاله شانزده ساله یوناتان تاه مدافع آلمانی بایرن مونیخ با عقد قراردادی تا سال 2029 به بارسلونا پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28791" target="_blank">📅 13:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28790">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adbxt0TOnCdp1ccqbaDkTS3zcbKtQaKfJ7ccH3bJ7mcU32_w0yjczJO3DVVhiCTv-gGkEVrMu9bF1ECtQMa08Yi_ctqAxOJWApVtEaSGAGCNeA3ME_dF-yrIe5TWx3WpubYDwbRVq_g2pnmVjeO0f2db_5v-95gaYdZaOjg8KhDJk_KD5klmxd2km4wwNrdwVa2_TCkpRmV7rqpaDeQwxWRxptzubA-MpYOYv7z1gxXYP9dvd2R1-Irhe5Xem7HgbVh6mQ3RuONLoqoHvSWbaq9Vw2NdaipN8-HK6EpUfRbYTnE4EIf-puD9jL_AlVP23LguWWB4BEracf3A7v3bSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سایت فوتبال تیکت اعلام کرد که بلیت فروشی دربی از این‌سایت انجام نمیشود: بلیت فروشی رو از طریق باشگاه استقلال و سازمان لیگ پیگیری کنید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28790" target="_blank">📅 12:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28789">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXly2tzSMONZbkAE71SWVJcWLykvoS5ieZ5cEyc_k4sU4SzYJnXdqBlirokLy9jholflmGHELyutyh-4euqqZdAzGDUyO-Eq62K_Vo0uecQ0dt8RAcTwKLm53lUJoylwXrM40hEPemIns5p6cRgY1SbkXZ7o0I-Vk6RoAxsS9sOiLkHzHWp7s_GiWNHqkx4GnHi_LVDTkIgwmGKSVXGe58xmYrANOcZif1Cw9X6oOoKNEUXD-xygEFa37Z1dQbMit9uKF5meojTpe75pxxir8q2mc8jjV7Utu2jEIwUwlSO-cC4TL4ESxr96o_3Lmvhothlur3ylswa9qVeV31Tz_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفت خرید بارسلونا دراین پنجره که بابت جذب شون مبالغی بعنوان رضایت نامه پرداخت کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28789" target="_blank">📅 12:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28788">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIv4JSyJMcSjFBfENfbBZNJzrX42ThBlqlNyqyMxGWo6URNNIon_9ZuOdNlKevCtzZQz5gJGjTdewUn3wXKY0KjUbdObnkpqiFfHMGqQMf3IAi0QI8kmgmrgcC-7l--7AyIXv6GMMqU-M3m06fqKvxu798sslKCWcgN60zEQQ94-B2T3dQphL7-pb3oIpUMryCAuc98tX0SxXATwhyJtiC6BXQDWiJGScNx6xhfZMo_zHDvcx9SLx6Lhf21QTrhpc2B5tUssw0xanvtwApmNhfY-NVaUfVBNTWOHeuPruThNnykdByVjcLBbqRv9b5-M9xKG2UzZWrfn30mfAwyCYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛ درخصوص عزیز گانیف ستاره تیم ملی ازبکستان؛ پیشنهاد مالی باشگاه تراکتور بالاتر از پیشنهاد باشگاه استقلال است اما مدیر برنامه یاسر آسانی در حال تلاشه که گانیف 29 ساله استقلال رو انتخاب کنه و با آبی‌ها قراردادی سه ساله امضا کنه سپس بعنوان بازیکن‌قرضی‌راهی…</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28788" target="_blank">📅 12:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28787">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1bH1FTI8nlglMCIwnyr_41l6c2lCOd2HeJqdYxj7-3SwI-FK3Dfo4I0kR1UOv9SC2zWr7lVENJxVCnZ9_34Z_kg-iN-Ihuk4i2J9r6DYAGUH-xTHyuSB0M4jFj-is0qBZX6anu3PKX-E79aRaN2is5v9eUEGBBeYWHZBUwh0-87DPDTJKgS3r9e_c2EtZHltOgH-rcJ1IItPdqng6uydLMiMPy5eRVCJLBAngJnGAA9TLDImQih5d6C7BihcWy3Bi49wYqEs_0hYaYlZAmlNvXKauKtfDPdaJdP-__LkuAHcptirkbMBhC5wvJaJ-4Y6DbeH_jOO_Hr68xc0AdDdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
🔵
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ درصورتیکه‌هلدینگ‌خلیج‌فارس‌تاپایان این هفته 400 هزاردلارپیش‌پرداختی به عزیز گانیف ستاره تیم ملی ازبکستان پرداخت کنه این بازیکن قید حضور در تیم تراکتور تبریز رو خواهد زد و آبی پوش خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28787" target="_blank">📅 11:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28786">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmrVntSmeMIIciwt8aY6ed99T8kLIZYADZvdIG3a7_rRk6rnH7XXAS6GHs9Udrti3WGJUl-YVz08s5EdpSfLDpjWj_aOV9zoLzCAn5JT6O8JLiPDexdHecb9fkIOU3dAsIHz92RwVKTTM2HE6GUX6PHq3j1pLA-s7INjsfgk6yOGifnrZVyX7POpRZrEgTCmCcvBzw3hmRB-crkzNqy4k4aJNbRJJM1HVNymuywNWsAx4PXbfAaQDlS930K9BIcVZwBpXJLRA8UNEzXLI2m_32wi-dwvppTKda8GVdso2WgIX9L_aiNjEZ2pZYrYYLA2NpQaMFcNsHdBGy6RnkfKPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب جدید بارسا درفصل‌جدید بعد از پیوستن گابریل ژسوس ستاره سابق آرسنالی‌ها به این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28786" target="_blank">📅 11:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28785">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXhQ7AXu9mRLzZy8Kq44XVm-pIYuoYXOX-MM_l_5XFJfPwuhhyzyZv4jNJosrT9Se4a9bdgVeIwGBf5Pgp3oZRs2iwnP3GXKa5l2COB745tN53sJYQv2E7ohIa_Euc2AeCsFjwJPeZNdfm_0wIUbVlNH52eg1hNuEqceXf9YQgcXO_rl0boJ9vQ3xen8NpD7KuRHrAvi8lDtVaQro7YUdfJfwXMMm79kBzYCWzGttc9QRut50jHu0QnIAsMWx0JvsH58SHZNTv3Oj378sW_cHjOjZPZemTSGvHks4Uam-Wu8nYGQRkm1nxVscUi9LeV_coYRte2C6omwOJJmIyVSpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#فکت؛ 3107 روز بدون شکست در جریان بازی در دربی؛ پرسپولیس آخرین بار اسفند ۱۳۹۶ در دربی شکست‌خورد و از این‌بازی.تاحالا ۱۹ شهرآورد متوالی بدون باخت درجریان‌بازی‌را پشت سر گذاشته است.
‼️
سال1396:قیمت‌دلار 4500 بود، طلاگرمی 140 هزار بود، کرونایی‌وجودنداشت، پراید…</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28785" target="_blank">📅 11:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28783">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nV73HygUZ4xqg4Bf_vHNQJyVc-3Y3--CBSZYs-Ue8wfTiidhwba7OGf1SEn3-TpoM1F7X3Nc14dGGZNLIz6f7tbHvVCGQLPsOrEPjf2gZ59L_SKZh_Qe_qaxZuYuV048YI23HvuVauJToj7LukewfSzU-lZIgJgXeLrMEMH5r1RSt9WA632GKzdORHIJpAJqoY9-0tvBZxZnRbVtnNhaMa4kNV6IzOULMD2E8E3fC0Sbwshei3FmVq_nTE218JZp9GPGw2PWvYE_eJwxgoANpV5ukfPpLktmk3ZiWJnaXDs38Ar_bOeOVoXOQc0onVBKJTVNobS_UoiVGDdztI_tHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ قرارداد ژسوس با بارسلونا قطعی و دو ساله توافق‌شده. سران‌بارسا10 میلیون یورو بابت این انتقال به باشگاه ارسنال پرداخت خواهد کرد. تا کنون بارسلونا 174 میلیون یورو پول رضایت نامه داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28783" target="_blank">📅 11:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28782">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf70d43b37.mp4?token=AHuWz42QqAWQhaXxzAFRqjvUuXf03Y7hs64ptf_HJQtWo6IATUGqjnryYfnlCfifB4DNCJdE_Z2EedOzaqPacOIPS9CLlMDYDmttfOzTH2T49seUVO-B58EJz8QcWBv5ofiHZQlunOuVj8_Yep36HuYpqmzz2ZVt15-zwW6ijbZvaf82lkNH-59T6yyOyoVVg_z9iJQvRHnnigzI5ZpYEUE91jd8omDGfqMPoM1QaYAXJUORLYNzeb5s8IqKl6LQAbvPgweZmTNGB0YFi_dX8adJetL_X3ZaVlXdEsSO9kgnFj1wq2uR3pZHW4Y7pEdMt3Qz8j1u2tyaTY4Pk_toPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf70d43b37.mp4?token=AHuWz42QqAWQhaXxzAFRqjvUuXf03Y7hs64ptf_HJQtWo6IATUGqjnryYfnlCfifB4DNCJdE_Z2EedOzaqPacOIPS9CLlMDYDmttfOzTH2T49seUVO-B58EJz8QcWBv5ofiHZQlunOuVj8_Yep36HuYpqmzz2ZVt15-zwW6ijbZvaf82lkNH-59T6yyOyoVVg_z9iJQvRHnnigzI5ZpYEUE91jd8omDGfqMPoM1QaYAXJUORLYNzeb5s8IqKl6LQAbvPgweZmTNGB0YFi_dX8adJetL_X3ZaVlXdEsSO9kgnFj1wq2uR3pZHW4Y7pEdMt3Qz8j1u2tyaTY4Pk_toPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ویدیویی‌جالب‌از سبک بازی خارج مستطیل سبز کول پالمر ستاره انگلیسی 23 ساله چلسی انگلیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/28782" target="_blank">📅 10:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28781">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇺🇿
🇺🇿
هایلایتی‌کامل‌از عملکرد درخشان عزیز گانیف ستاره‌ازبکستانی مدنظر دوباشگاه تراکتور و استقلال؛ همانطور که شب‌گذشته‌گفتیم درصورتیکه آبی ها این هفته‌پیش پرداختی رو به او بدهند آبی پوش میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28781" target="_blank">📅 10:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28779">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‼️
هایلایتی‌ازعملکرد موسی‌چنپو وینگر مالیایی سابق استقلال در تیم جدیدش پانایتولیکوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28779" target="_blank">📅 10:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28778">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IyF9veoXAgwR80yq-iw5FTmkzcBOWU_dS2vUiPSyI3_2HwVUFx57ozvvijoxL7mmdS03C0ai437_4oOCCaWLUagojh7HvW3yjptZSkEbWXaLfgKgvDgXV27l4keFLQ4ZLEPyuudQIIFCIOWTt7KjxMujXVQpyWH4xs7_hNpO3IBiTJSTrmESVze8h9BeL0QBVl9bMYBvt95MttjBHKHu7wXtl-4zI2F85vtaFJ-BKjDFLOi7bilM5qSXMox7aZDGFwOtDX7ShlvRY8DfFvj7-9tGnBl9I264TLH-3nZULh5XP2SvbMk3JkMxGnuSWOjLFuGSJS-0_F20MxfDNM_img.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مصدومیت‌جدید مهدی ترابی ستاره 32 ساله تراکتور مشکوک به پارگی رباط صلیبیه و به احتمال زیاد ترابی 8 الی 10 ماه دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/28778" target="_blank">📅 09:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28777">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0edcdd5b47.mp4?token=iQHcliyrnhlAkej3Aj0npMHnyv7LUXgrfLBCZNVSBcm-sEoMcg7opotvpjbawRhfZvoFB9aOOa_pfMtLfz8eGUHlo_LrmAh2PhEy7M6Y80DF8qs2yn4p6ZNHTUj_ObZJqggziIfX0qEg9N9uaJ8PfmGaeRFTKLeavKL1itOAWw46gtBDSm699xcsaVbeADoF9IcLIXavK9MaStOEJeBm-dpHuZUQFXvz8j5u6L7l2tUMS_G1GIwTZw3Khee6veoFQO4pEuyb684RqIrLTTtb-pkEYnku1MlCiV5RQp-gvaXVoSXDFs74dVUOa5DT6scKgh-lw37bN8DL1g_pC7nTnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0edcdd5b47.mp4?token=iQHcliyrnhlAkej3Aj0npMHnyv7LUXgrfLBCZNVSBcm-sEoMcg7opotvpjbawRhfZvoFB9aOOa_pfMtLfz8eGUHlo_LrmAh2PhEy7M6Y80DF8qs2yn4p6ZNHTUj_ObZJqggziIfX0qEg9N9uaJ8PfmGaeRFTKLeavKL1itOAWw46gtBDSm699xcsaVbeADoF9IcLIXavK9MaStOEJeBm-dpHuZUQFXvz8j5u6L7l2tUMS_G1GIwTZw3Khee6veoFQO4pEuyb684RqIrLTTtb-pkEYnku1MlCiV5RQp-gvaXVoSXDFs74dVUOa5DT6scKgh-lw37bN8DL1g_pC7nTnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شباهت گل کیلیان امیاپه به مالاگا در بازی روز گذشته به گل دیدنی CR7 به یووه در سال 2017
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/28777" target="_blank">📅 08:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28776">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3785816e6f.mp4?token=FuWqooomwSHpS1PYXAqENowdxG5cK3LfzhpfkKIfjZ0uIJfl2eOdRqNBIZQHbP2fkfmJS8BdulGEmvlwufWLinSAYedNi5yzrERoelOeyE8BdKP_XD4HnuLwLFRSGzoX_ER9a_2gTkF6EkfbQ0p8pfkQhPT12xNrFp990PZBmRXbAx0AXZGsMXpjaHWxTL-lw3bKSr-Wm2niSYRiMGz_KL1fXDyRCivDvS3mw5mghelXCLH1SGy0Md1TKP4ST0n4HzwxiQ3ADsPq7H84PiXTgeqwxF2snFdkG_Jk34FNpiFEQEJ7Rm4e7jnhN4GYhvp4FJ1EbK2x0cmag-KYgSrEIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3785816e6f.mp4?token=FuWqooomwSHpS1PYXAqENowdxG5cK3LfzhpfkKIfjZ0uIJfl2eOdRqNBIZQHbP2fkfmJS8BdulGEmvlwufWLinSAYedNi5yzrERoelOeyE8BdKP_XD4HnuLwLFRSGzoX_ER9a_2gTkF6EkfbQ0p8pfkQhPT12xNrFp990PZBmRXbAx0AXZGsMXpjaHWxTL-lw3bKSr-Wm2niSYRiMGz_KL1fXDyRCivDvS3mw5mghelXCLH1SGy0Md1TKP4ST0n4HzwxiQ3ADsPq7H84PiXTgeqwxF2snFdkG_Jk34FNpiFEQEJ7Rm4e7jnhN4GYhvp4FJ1EbK2x0cmag-KYgSrEIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌بسیارزیباوارزشمند ازهیجان و استرس مادر برای پسرش حین کشتی گرفتن او در جشنواره کشتی امید سازان المپیک 2032. عالی بود واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/28776" target="_blank">📅 01:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28774">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5MOkmQGUqLI4tbdT4kHY_gSqbvgwiSFJeb_tbwBS5pLWKnDrXPkhTj-392C5HjPY-ZE9yZ8t6nGni5RmVTwFVJQLZPMD80yuOR8VLKJTmEKm13aVuC1HfmBXouo12SBkeA_gWIFchFr54xBU9--M8FDahYPbdopRGvhQw__xA-wCUgzZ8Y43i0RRrS_dGwvyseveUJZniFE1elnhKoywILto6xw14Lv1fpJ-7TpwMBdY-7iD0N-kyDdFxSRLf1JAtxj_3JnpkFaW6yS8TY7iZR44r8u4oazjSEvWl0T1rKRczL7ODgoswzRNekYnLcUS48jC1vQ6-ns9qXCIQO78w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛ درخصوص عزیز گانیف ستاره تیم ملی ازبکستان؛ پیشنهاد مالی باشگاه تراکتور بالاتر از پیشنهاد باشگاه استقلال است اما مدیر برنامه یاسر آسانی در حال تلاشه که گانیف 29 ساله استقلال رو انتخاب کنه و با آبی‌ها قراردادی سه ساله امضا کنه سپس بعنوان بازیکن‌قرضی‌راهی…</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/28774" target="_blank">📅 00:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28773">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjTqGM29JSaeqisnIMQaK621su7k3h-41BO2vV_mdAYL072bLfAR6qT8PD3Xcx5ODrWgffKmLReetddkWWOiVtwrorhc3YsShYTNo0eEwJM-Kuq9txHrMvNiMNtuUDzt2A87Q1DuwLz0ItAL2ZnxdLVBPD-kH2kHf6dNMoG3Axy4H_2J2zHuGpclCb7zvh7TYg2cto2zn27KXPmreIJVd2qSD2QtuQuQ7k7zMvrATeVhJ7X1pD3xbVvFn6d_K4hHHEBII3_r7sKxTazAz6sz1qkJaqBHhWqYe22oinAfHHsF9tTHH9UXTs6SX-Y1H8ttT8K1ELULH_5z6QS3JTheUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛دوئل‌شاگردان آرتتا و امری در ویلاپارک و جدال کاتالان‌ها مقابل رایو وایکانو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/28773" target="_blank">📅 00:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28772">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ci4zeJ33UrdNF1XstKenBtQBuccvsc4wcHaAHdfsNPzjrSwPozSmz1O8yfM3LX3Rtc-Cf4W3mnJhNPrJGFP9Om-SjU5IgQM7ZLeKN0z4WvXISNhHWwG-H5GTLVZIkDKL3A3HTkSleO0sL0Q_-Xujk9v72Jn6PLKOskCCJ39IrBa25wzMlBcdLghGWoxT96vFAW_N0aE35whkL0XkIA2wm_dM6xE_tf28kPoYBP1-SSIHnzHZjvPueLQF974atStXIrnIHINBR4AvKKoevQHILTQUkweJkOCBVlU9O1uhaf6e6IhAlysuHF7Y4VSKZ1n_xqVXKrOtlTHyt5vmmMrcPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌دیروز؛
از آتش‌بازی لئو مسی در MLS تا برد دلچسب یونایتدی‌ها مقابل ایپسویچ با هتریک برونو و ورژن آماده کهکشانی‌ها با ژوزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/28772" target="_blank">📅 00:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28771">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0YxUygUxBtF4-XvBm2fprf57X8A1Wxv_1aou8n6PY_v0PIis6aHQmR40qm6yIiv3ViAlML4FkzDpZpHC_Ps700hRzvZLoYI7WgorZTuTjXTyXnwoHSG1kqo8KneYfZQYYEvo9896-7Uv4KHViG83dqnSmgPhTFn95g3jiM0kDJCH-wUx8opFfe0lo2zKFCfi36OTbCuwsYFpdDwKSpr0JGClOWft10qG1RM5IX4FBmsvwcYR9JOjIsJ5zoCXl157w5coBbzweTaLKDT-ub3ZvjvSGpKwnMVQ7WcB9iCsCNXC_HAyc6YMBqjQiO_r33xZ7bpCuSdMtEWizSHiE8scA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛بعداز اینکه‌خبر از مذاکرات تراکتور با عزیز گانیف ستاره تیم ملی ازبکستان دادیم. حمید مریخ ایجنت‌یاسرآسانی و جلال‌الدین‌ماشاریپوف در تلاشند که این بازیکن رو از تراکتور هایجک کنند.
‼️
باتوجه به‌باز بودن پنجره نقل و انتقالاتی تراکتور فعلا شانس‌تی‌تی‌ها…</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/28771" target="_blank">📅 00:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28769">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbxB6fXjbLj4jTHQM2biruisveDqOWfKV5sZka8AIOREoy47fCL2-lfXJ7QWJqHiw8NrJuDkEZxSgQuEt2TmYMrBipwGWWbV9Cj-e0IzyFQHByXgnDpJ_ikg6OgptbnhrD8lW55x2diGrniAb1Y0JopdAbsHjd7CkhVU0ls75hZ1sZrxSSGr_Ps3x81Nr28RtyiGIQyoutmPXKjDJUSDfglQge1UfFjk48KFcyNa8LOiTrI1lYac9lmAktpHtIs5MheXNxkHbpUyXrald0WFD-g6vZKkCq3jyw3mDR33y425-Ty-2mInaN4jOTKm2RaCF1-PLtHLaokotrjO8JPLbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
🔵
سوپرگل‌استثنایی و برگ‌ریزون هاکان چالهان اوغلو در بازی امشب اینترمیلان در هفته اول سری‌‌آ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/28769" target="_blank">📅 00:18 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

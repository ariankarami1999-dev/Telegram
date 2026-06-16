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
<img src="https://cdn4.telesco.pe/file/ZST8GQZAuGoKIuxjVOLrbtnEh3uQLdxfuR56-qfImCCcl5kP7H3GM75I_bUzFX45dIVegsX43X38u2d2JKVKRcg9PsMgrhDv62q_X_yrgZfseSj-sJErCUdot1hhgdl8OLl7uFplRqAIE-0JE1mZJRQd7ssKNpVyLNghJv-KloKyDsSEbyndRQLbdGKDR1tGK_XTSU-kPk0xX9Iu-aoVtgWcWIfcvOVuFOBST6-7FWt9lQh2nepth3nZEFLIrZ6Y09LT-V6l82zQk5Y9GTMKO240WoMOxIi9OJYHeUQcFqc_-Lz74Denl17TwXLJiAexc2zS2a6paYGZOC24RAAerg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 301K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 16:53:27</div>
<hr>

<div class="tg-post" id="msg-23604">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/clSeeqG35B79nIJQTTm4mSx52ncPYLZ1rLptWNK7D8bCwC7to-TRVcU8eG_pmPRnqt2mYRd9f-s-j-ivRfX5bns59y3oJRT4P-5x7UyZsJ10Z_WSaImzbXe8hTty6r8KHQmrPW03Bs_ktD7k6k5aSP65W1RBybm5jjNo6q8GX77GMNQpFJjdKrKne-i0c3_pZSgKYQEH1hdiWLJHT4G7VZbR-kuqANvqGVS7Hl04auLjiZKSg6B83v5RnUKJT-bVCiR9vLwWmmKhT0erfRmLnNQTvsRwAT7fbUtUqmA3NIhggVMYtgOwy3eXl8YpApAPelzenYkKhKkLBAM2CHIVAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PnTH7T12lq9yKzUR6Yj_f7du13UDtN7QqwqlwOxxbEzgNks886RsCbuAGdDQfGFXi4jbBxL6heymrQzydK9x0FOJxIQiKklx5AxvDcZl-JC4cnbppVkudxFpM2Vqc7OSsT5pLVnOodwgeUCjywfEq-TKoPX18OJMulxoXKS8qZhPLlnel4j-9G6VCc3AQKpsrwKvsNa6C8sHqYCqWYnxxcE82Rwg-JjvTHOWA8_d9y98Q8iRtnlyNhtUsTFmGo8EdKHiehNNDyvUBbzbJ3OdtXAvGG_qtbUovZGi8DSXTOxKeCVC5ebcC7ox0MZBu2XN_aSFHJeieXBZqVjFdUC3Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
دو زوج ایرانی در حاشیه دیدار بامداد امروز دو تیم ملی ایران
🆚
نیوزیلند در جام جهانی که حسابی در فضای مجازی وایرال شده است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/persiana_Soccer/23604" target="_blank">📅 16:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23603">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzzitPFWJ2jZsv_f_s_HQ4Dr7V9bn1KHaMWOWVdBSJUOeW0ty9phcE3nRJ3LZO44mz7ady2newY9YEdzcq3yJrKiM-JVb2C3_6PnWIq68VBFNYzQQy8_3wOEHegPnDonC8tBRKFY-yDIx4syb2tgc_UNTXOI41xgdBleOpoHV-WXpTiYbie4bRpCa4MgIrpmrzeaX67VnJFUt_qj-i9HYBtY_PFrXXN305o1HXeUdKLosA7ZPC9Af5V4tDYfXBNJm89QvHdoK48M_AGDem2xu6IQeRELwCXScRdiZQV4vaKfgh3IIaGW2o0GMYvusonFpeIObjD6nrhlMcrM8eYgYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل‌هفته‌دوم‌رقابت‌های‌جام‌جهانی 2026؛ دیدارهای این هفته روز پنجشنبه استارت میخوره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/persiana_Soccer/23603" target="_blank">📅 16:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23602">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqX_hd88GHFrEnSADvNtlo5ytkAuwqJG7kP7UlHaYVSt4iMWj9oC3cgWEGpZZThgjGsegZfAiVThTF4ko7iIH_m90-cuN2OJAk0aH57qIM0bFRT76-E8B8CQnCUuEYrzKjpmQtC7CfMZzUbB77N2mqNFWxzgH1QAU640oib_JWOySwQgokLfDSnb0R6m0PIoZsw_HcG1GOBFk1EEb3rv4fOj6gERyq4S8fGmponRCnmK7wCJafVizZ7GpUe5ZsUGj9M5mcD1d1vPX_fyqFpM8iEa97GAmFd5l8TWIKaT72zA4kI5ypnCITr9xwEsW3U3R3USfQLi0EADWot8HuerVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
👤
علی رضا فغانی اسطوره داوری فوتبال ایران به عنوان‌ داور دیدارحساس‌دوتیم‌ فرانسه
🆚
سنگال انتخاب شد. این دیدار رور سه شنبه برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/persiana_Soccer/23602" target="_blank">📅 16:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23601">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b865e790d4.mp4?token=LiORZcSRDv03MpO3zrewi2Mt3OKTtKj1GV2wytCdaYCOffiwZRWVxLzUxYHYZrviP22U6Ryq0561fuG_IL-R6iE3hgiCSsAOjQo3_MzVtGI364xoOaApr3nwweCa6C2LlrQPIfWmW6A8Iz9ZUKMsmVEXXFMT8Ew0Lhag_-fr_FmojlLQo0c6J5lmj9BTG0MNzrbsb3sTNkAOZfY8LvCZ9i7BjqIQ_K0gqWrUXpxAVUa6J03-Bq1zFkapTIKMkOdngId8OC2SxOAoVOqGAcpuYGdaqgQfJOgM9PenVE4JbOYQiDHwKGTvw1xghPsr6MMc3HFFfencbf2Mv2XO_Fo5Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b865e790d4.mp4?token=LiORZcSRDv03MpO3zrewi2Mt3OKTtKj1GV2wytCdaYCOffiwZRWVxLzUxYHYZrviP22U6Ryq0561fuG_IL-R6iE3hgiCSsAOjQo3_MzVtGI364xoOaApr3nwweCa6C2LlrQPIfWmW6A8Iz9ZUKMsmVEXXFMT8Ew0Lhag_-fr_FmojlLQo0c6J5lmj9BTG0MNzrbsb3sTNkAOZfY8LvCZ9i7BjqIQ_K0gqWrUXpxAVUa6J03-Bq1zFkapTIKMkOdngId8OC2SxOAoVOqGAcpuYGdaqgQfJOgM9PenVE4JbOYQiDHwKGTvw1xghPsr6MMc3HFFfencbf2Mv2XO_Fo5Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جز‌ ترجمه‌های‌ماندگارتاریخ‌ ایران
؛ پیاتزا میگه به خلاقیت‌توحملات‌احتیاج داریم؛ حالا مترجم: سرویس خوب میزنیم تو دفاع باید عملکردمونو بهتر کنیم:)
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/23601" target="_blank">📅 16:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23600">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
#فوری؛ کسری‌طاهری امروز بین‌دوستانش گفته مذاکرات خیلی خوبی با باشگاه پرسپولیس داشته و بلافاصله بعدِ اینکه مدیریت این‌باشگاه‌رضایت‌نامه او رو از روبین کازان بگیره راهی این تیم خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/23600" target="_blank">📅 16:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23599">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDPjnkZNV2w8LNLiWNV5LCinz2RPa7qSDxbtYGWfueLM1VFU6C60Pj7mOUZNycNz-Z5e9cAjVsJW050U_gMoGBhGYO9hdS27kpzQFhsscxG2DK-FUPR7DU3ocwDFj4bRyiQ0C6Epqa6nKBojMbdNxJFt_wKIJ2aq824KEQ3aASr8_oWOZgdRikoofkgKzNQmM-IRMXAPH2i1kX8r7rVM5RZtnyjjD7VmC9DTtTJk_qfQz-2KimilVsCLEHPgIhafLb7Hq8kraYlpS3ysRCLxsz_HuTqKYoBrJGBD7HPrOCq6MLGqpOlp-nBM_9PrcAL9hORs7OcliqJO7VwA6C7OaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
تیم منتخب روز ششم جام جهانی با حضور رامین رضاییان و محمد محبی از نگاه سوفااسکور
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/23599" target="_blank">📅 15:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23598">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3yjOCZrxY_r3Yn8R3stn-vatjY8Em4STQzPzwCbHQFnwHIeJv8CIwvosKIvcK9RcIK89ZXTHfB11nnGWwNrIhXrQtNj8Xu9KuwHOcYJFP0__plpcUEZA7H0OEgRMXeA1u-Hi455hc_LbNpT69YALaOXojr815NyLldHSpaxf6M5W-5OvEgoK7dNHjRZj52Uh4y-ErvbmyXdZyGLk7bOsXctMQF0ZXkWYFVjRcvfenOFBg-zRY2gaxqopGtbTLEbFCHi8xAuT6EpmSPqsPHWelOU0H2sTvFSvwWcS1ivnniwzDweZ5_WrBi29Y_btkca55SYc76b5P9OmS6YV79o2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
روبن‌دیاز پس‌از ۱۸ ماه رابطه و زندگی در عمارتی مجلل از مایا جاما مجری‌معروف بریتانیایی جدا شد؛ بلافاصله پس از این جدایی، با حضور دانیلا ملچیور بازیگرپرتغالی فیلم‌های‌هالیوودی مثل‌جوخه انتحار و نگهبانان کهکشان ۳ درجایگاه‌ویژه‌بازی‌پرتغال و شیلی و تعاملات این دو در فضای مجازی، شایعات رابطه جدید دیاز دررسانه‌های‌بریتانیا و پرتغال بالا گرفته تا او علاوه بر فشار مسابقات، با حواشی سنگین زندگی شخصی‌اش هم دست‌وپنجه نرم کند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/23598" target="_blank">📅 15:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23597">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c17684a49a.mp4?token=ZQfcDMBO3pK7K2eFwGWmift0HEfEqjys00KgKgzIUt3f642H4YY3MNIiqWWyfANJN0igvgalxU7tHwwlVMe_b-RNWQpNz6DjoDLTATG0wp80Evmp7IaMsSuipkWbcHITkOSnZ59xgRqY5UAfzVFxLhp_8RXFLZ2xAyy_Aq3xdV0qYh-8arRLBdaNWURX7tKAi5NSSA0U8SEzuzl3cycJQyPxvfmn9fZQdH7feM2S72XGefwnh-yJNamedqIDkoFYky9WT9kh9omlWBSRIcR-kn8nXKr5UY9Gigb59Jz--rV6_PUtqMfdh1z90weXMbwRsHQ7if9Y8ekocGzDaYsJXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c17684a49a.mp4?token=ZQfcDMBO3pK7K2eFwGWmift0HEfEqjys00KgKgzIUt3f642H4YY3MNIiqWWyfANJN0igvgalxU7tHwwlVMe_b-RNWQpNz6DjoDLTATG0wp80Evmp7IaMsSuipkWbcHITkOSnZ59xgRqY5UAfzVFxLhp_8RXFLZ2xAyy_Aq3xdV0qYh-8arRLBdaNWURX7tKAi5NSSA0U8SEzuzl3cycJQyPxvfmn9fZQdH7feM2S72XGefwnh-yJNamedqIDkoFYky9WT9kh9omlWBSRIcR-kn8nXKr5UY9Gigb59Jz--rV6_PUtqMfdh1z90weXMbwRsHQ7if9Y8ekocGzDaYsJXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
یه عینک بزنم تو برنامه زنده جذاب‌ تر بشم کسی زیاد توجه‌نمیکنه‌بهم؛ همون‌لحظه عادل فردوسی‌پور:
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/23597" target="_blank">📅 15:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23596">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Te_-dfq5AWmVM1w5VGYSzDuCkUl6-BiDRYmnbAJcwKkvCCXJB6jXcCQMJFDxgNjDXsos7iNIy8h6VUa7IqmmJ12RmAG4vaNpbQmK_g_k6WpvfZYfSSV8uZGwx8wtZb1YnZ080UTYJvsDILZdDh1n78vBgUjcbzwhhv37XbOx2Y2A5Dj9nOL2PAhZmZ0Ixg_GTv0bV4ikGamhwRQnjceixto0S4peQW9S18rYBTsauuY17eXbew3Mn2_S1EypAu-esBlG5gwCuZbIRajCTe3GWu8_BLPEq87XAUaZfzZCzDBBbVaY3ifu32iwrwcpyANc2J53bQ8SUHzsmuo2PUXriQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌نشریه‌فرانسوی لکیپ:
دولت آمریکا ویزای مهدی طارمی و مهدی ترابی دوبازیکن ایران رو باطل کرد و نمیتونن تو بازی با بلژیک تیم رو همراهی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/23596" target="_blank">📅 15:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23595">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2AWj7iUGwUsF60AHg3OPD9JLqWpYpr5OFyUwleTuNXiRzMN_-SfM9C4AbnTZgxjsH0DAfHnL4UEmL51tsfosQepMRAAdysM2lziyavxObO8MZmFxDwRjCEJnSy8OWU-q4D4HnF6T8XrKT7igxwuGH_ldLPA7dJS9DBu2_oPg-Fxt4PsA3i1TnIy7Uy8l9Kg28pXAVQHviJAfBsFl6R4XgVaG-ROS0ptP9vKXor5xaAiuA0YzvJOGSPaeYc3H0NyZqrPL_VeX5pcHvcJjEyaEtO7sgnqeM2pHbmnmly0PdNdJv3b5kipOBZMhKleTmR6UMIoC2LjPlQdiI7FHMi0Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بااعلام‌استقلال؛ سهراب بختیاری‌زاده بعنوان سرمربی جدید آبی پوشان در فصل بعد انتخاب شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/23595" target="_blank">📅 14:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23594">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7FRQvmdlFjTldN5L22QsUNzqZgCBJ6A6EiFNNxGTgU4iP6Y58zvetYDgtZBXSfIuQMFaZIvn8lAeqizyDAzI_C0sThCzaneW5qovTN_XkQJZ5XXJT99I3-JqN7HCMwp8_jTb-ppZHjiYpV20vbFqzoIIUsD1Qcaf5h36I1WQUdI_GQS0_wyAiyc0jDlRFEHQRNMXKHuzZ5hjYJyrGeVV3wAOcWbNObf4UTVlFT1HC20cnpr5FaBsbto3dJJSobqk8b-X46NNLXPQ77YhVh2SI-sUk1aac_DrMnc5eB5co2n9r06ScF3j37i9qvA0I0s1CTqcv1N0ljfIte9WExbLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇳🇿
بازی که مساوی شد با اینکه نیوزیلند ضعیف‌ ترین تیم‌جام‌جهانیه؛ ولی کاش تو خارج از مستطیل سبز هم همه چیمون با نیوزیلند مساوی میبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/23594" target="_blank">📅 14:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23593">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mV9oq79nALSO_-tr5isIwxqDjkrv08tB4AJM3KPjOWKfsgJyY_UrG-NoBiutfUbHmOs2zcYzVH6O0rNz80i-8ALG9fAOnaueqEv9MB7Syv-tbhisj92EUESaIjSH7SZ1oYA5ZOSHhfaVdURZ32UtEG61P4xFefXl3nWxi_P0XEIc7OiCVKMGk4N5KPIdK_gyiT84bdRJnD71KCEIcirkveU52WsTYvyRXttFZCItfmoSPd5PxwY0P7iW1B3TJozMTObAexZogk0C7_SXd85uiRP2-B8iTjtyhw_GByid0cN5Lc1ivKbAa1SWhSBcNumzIzPINyUlmMl92rhLnExFug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
سانتر خط‌ کشی‌ شده رامین رضاییان ستاره استقلال در بازی بامداد امروز ایران مقابل نیوزیلند؛ خیلی باید روحیه‌جنگندگی داشته باشی که با وجود یک‌فصل‌درخشان دراستقلال به تیم‌ملی دعوت نشی و سکوت کنی و فصل‌بعد با اومدن ریکاردو ساپینتو نیمکت نشین بشی و بازم سکوت کنی…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/23593" target="_blank">📅 14:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23592">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHfoggr__XTKnCQpbM-uWr6zX1vuSivMtJkOcCAINkut9xzI7YvzXTn6Nf2SYv3pv5fSg3sYCjIn0Eo-nq0qfU7Bhlc4sAGnaPMWgCEbLNdtVKLXDqjvHjkMKvIQnxSC-FeaftxdahD70mbv6utnrGkzOwxE6roZ6qhk0rU6shgi4gj-ynJ05U9J7NfoT6XHbkIr5okykAyOz6a1SfxCmApjwEKltjWtjWEPEKmCwG7BeA0F_qS3PJ83vJ-zqeYCKAFxX7_0Y4PVgwJElRNy-3nsMabp74UTw0KgUamw96dFxkLPd-2qZE9CiMwatQzIX6s5Jb23N9F9FzAud-JoCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Aparat Sport [3.6.2].apk</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/23592" target="_blank">📅 14:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23591">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBTyapHCWSjB6GfaXJVsIwqMjcMStgZ8bQTjtGvjzeAZKW-g3oA82gtbEfPnjMUBGYD7uvtX3ikQzEerxynGrL32xbuVDDb2pkizkkdJq_ezBSs2RiHBjTRnPvQPcQoswuXzo44MekqekZWSmX4MFzpzQBrcOIjsJ5iXiijl37kOZvf-AbStPQY62eWyFy-RWn2uCvi4OHCy71HUdkipTZWExuBCDO-boENz2i92pj6I1FCsl4RQhDn97XhLWg48e_GhqlQqN9L0MmeTPjSsZqXGY61T5h88q4swBr6SA7u0EBf2I7EupE0liXg4v15UckmIlFDPU9YZXChVDyJ4HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
#تکمیلی؛ رومانو: نیکو پاز به مدیریت باشگاه رئال‌مادرید خواسته که اجازه‌بدهند یک فصل دیگر در کومو بازی کنه و تابستان 2027 با قراردادی پنج ساله به باشگاه رئال مادرید برگرده. نیکو پاز 21 سالشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/23591" target="_blank">📅 13:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23590">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1f5900223.mp4?token=c09b-6T-lBzC6V0EnjvRXubPZF-yKLtXQeSP1C1-Ak319ToiHdq7iZwiwAwviXEzPqrhZ2nlIh2JssQqEbXaSzBE2eaLg7pLrPf_0-oioy5G0ooxFCGVzl8JkRcFX7E6Y1Em-tTKCPcQyRUzXgmLfqWyFpyyk4UL_RJvjsoIcT82h2x9gap12GN2vK0F5JBgFO0Xq9MvHAyU__i31ssPLhwS-5WRNGs6USYY1RFMRM6d8GY3_myc3YQ55VwxZJ2D7PIZFJJ6LgVNNyM-sLd6AchdlCf6ew9wg6sgYFtNcI_b11dEo6KAKu350XWb519SaeRfbFOgBlrhGwQ-tWgtcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1f5900223.mp4?token=c09b-6T-lBzC6V0EnjvRXubPZF-yKLtXQeSP1C1-Ak319ToiHdq7iZwiwAwviXEzPqrhZ2nlIh2JssQqEbXaSzBE2eaLg7pLrPf_0-oioy5G0ooxFCGVzl8JkRcFX7E6Y1Em-tTKCPcQyRUzXgmLfqWyFpyyk4UL_RJvjsoIcT82h2x9gap12GN2vK0F5JBgFO0Xq9MvHAyU__i31ssPLhwS-5WRNGs6USYY1RFMRM6d8GY3_myc3YQ55VwxZJ2D7PIZFJJ6LgVNNyM-sLd6AchdlCf6ew9wg6sgYFtNcI_b11dEo6KAKu350XWb519SaeRfbFOgBlrhGwQ-tWgtcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
رامین رضاییان در گفتگو با میرر: شادی گل من سیاسی است اما اینجا نمی‌خواهم درباره آن صحبت کنم. گلم رو به تموم مردم عزیز ایران تقدیم میکنم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/23590" target="_blank">📅 13:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23589">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsrUFhlFvUiT-sZoOd6rvKdLdCgSmbc2gLSoxM5CCZKoxzs1juSN8Vx_t4Avbkkj20GGp0i_vVMWKdnmp0uqKxP8b0mJ7rJE-IeKxDNZSgxiuaQrjCeUT9MU_02aehXNlVej5U75SUExfydTQh3tAJB0kKH68Uf26XCCOSJxZYtBaOGRf9QYnRSf9pwhi1N8LJgTyn0pmSZlDJyHKjOPK55THJZ2HhDgt0AgMxULzsUPuCSmv3SPqMhwpJXznSko0m4iy8Gcdk9bSbfXVQin_QE8uhrC3TTIv-B3dymzlf9Gjj_PcLV4pJrRRdEI1xLXZNxU24gF_hvLt53Klh369A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
تعداد فالورهای وزینیا دروازه‌بان تیم کیپ ورد از 50 هزار به 3 میلیون رسید اونم تنها در 5 ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/23589" target="_blank">📅 13:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23588">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SscSBqA7jyOqo4AuxqmxMheNg1U17eIRQjp7TLiA_im54mkH7iu0j7LH_3HJC1FD_RjAOIOgC4g9wAJPr4C8IUtBJUZAuabShKMeKxkT8w1UyFk2skEf_1Uh_HQ7P4bAKR_af0wifKg6zyrbvsYWxDDfep11YNtYiRqUCh6w0TOtetbRsltJWhm79RwlZEUXqn5H1I_rg_hrzMBlV1G1JEj7ieC6pyFEWG94XkscjiKuhQPUi4wriVN7e1HuDjod-FDgOskN0YpHOp9As36m5NA0vPwg-hF-z580yE6PgkOTr3iWZpolf-z2ASwI8WGWOAXl5k9kxv8bHJ3kuNpdzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دهنت‌ سرویس پسر یه حرکتی زدی شدی سوژه همه؛ حالا تیری هانری اسطوره آرسنال دیگر کارشناس شبکه جام جهانیم درباره خوشحالی بعد گل محمد محبی گفته فکر نمی کنم منظور بدی داشته باشه. خودِ محمد محبیم گفته بخدا فقط یه خوشحالی ساده بود که اون لحظه به ذهنم رسید.…</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/23588" target="_blank">📅 12:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23587">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jcjs7R22rZ3ewRuoTP9fCGTt-lyqukOF-Ownbfu9FjC5AlnOb3g3nLEtrtRhJ4hHgXOwWdw2zZ1tYqMs7Km2dut1IdlA-CtL12Fc919pnRUJnL5yn45OIl8h73FXvNPXlzigVp_ybRZdyAr8P05KeUVAN0bGPu5Rfg5vL8Tp2x8kmo6CdZQzb6czvl4aFwdGSjl5_Blmh_pGpenfMXz4xgreQOCwjlTGrbDG9c4NcWflnreANAipQ3iw7pk1nV3zMHV84hCS34n2UgKXcTITwBtQdKFMXT5ka7KtlXT3ildd7dAGJwjlOlAu3j3f2ReUKHH2HK0V8SkawRjBtsIcnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو: آنتونیو رودیگر مدافع میانی رئال مادرید قرار داد خود را یک‌فصل دیگر با این تیم تمدید کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/23587" target="_blank">📅 12:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23586">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4mwIKVcUi7DB997TmxIx0WhUOk8w8rcMBhesSwA1nxFeUC-f6dbYX2yrss2jLL7kdxqxRwEckIK53V7iBB3RuA1GT3i1GlU6jVvYCiD2zpkckNgT_7BoKxUkkjtuR7RZesrlPsMB8sk18BIo1woP83cDf8-Ypgjjl0E0A7Ts9Z1hBjLmp9vZztnZnijf_gd-U7ZjTQilHb2dpEoPChSdFzVBRisUnRdp-lJM0yaVmGxhu0yNQeH9rJJBCuGSDG_4YESounTypHuaJghp-FtH3CYoG-1UYhPbtWAGBMdjGSBNc9bQyVDXJA-uJGeIpo9mPgcPb25U64PwITg8NZWxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
درباره وضعیت آریا یوسفی، محمد امین حزباوی و مهدی لیموچی که هرسه مدنظر باشگاه پرسپولیس است و مدیریت‌این‌باشگاه مذاکراتی‌نیز با مدیربرنامه آن‌ها داشته بزودی اخبار تکمیلی رو خواهم گفت.
‼️
آریا یوسفی جواب تماس‌های مدیران سپاهان رو نمیده و چند بار گفته یا لژیونر…</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/23586" target="_blank">📅 12:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23585">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vA5jrK_6lM0Ead20Byw646i3z4uf-cwDVjDRyDVsLJtB5OuK48HvFK5sdv6ayJ852SuNcAuI8sz0kqimVEK-I7LqPPJpJnJVIQeUqwHMBmFmTO0rt6Vn7dc56XESXpc7wf6fgOogmVJu4rwF1Yvtz26JID_ka7ITQLhc6lQ5_eOvquOnRx3FrkmMdw72CLkGv3cXtDziypjrwbCnbYWQcoFzxxuI5zui4kumTWKdjbjXOxUmTV5PloS62ptUPXnhW2lcMX3l75v4NZwz-TgaAxZTmeVBq8NlRtA787r4q0VXnvOI_RwP2hRTHLAqiunhBwT9WNrKqyqwUGz1sSXRzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
شادی گل محمد محبی که تو رسانه‌های خارجی جنجالی شده و میگن احتمال محرومیتش از رقابت های جام‌جهانی‌زیاد است! زلاتان ابراهیموویچ هم که کارشناس شبکه جام جهانیه ازش انتقاد کرده و گفته همینکه برای تیمت‌گل‌زدی کافیه دیگ این‌کارا چیه که تو خاک کشوری که رهبرت رو کشت…</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/23585" target="_blank">📅 11:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23584">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRdDC2AR5AwRUt6GPIs88PmgIs2AUFS73N90Wd1MIkx_TI3KF1DLY3pH4mtL4H20EGi6_PtLTPD7ySjXSefSs5LaguFG5Nb34Yds-uCVwIWz7KGnIq3rcdy24WAQ5zlym1NvrxBc5wlYGxuCRn4BXFf8wrI4az6UmRwD37fdO9zMev05i5pT0vl2h0SheRMI0GxxNQm-rY2yp0HMADIn88acUBpZPbQnXiYBldNzZ0T2_LuJgoY_VZx0xr_N6ZQ_EftQZvngIpQuutdqnbEu1Gx6sl8NEZKj3H2OtOxgFbd1uJJHzlxaSz0lwmYLznawp-AXw2ArAzy8L65UEfHAOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#نقل‌وانتقالات|رومانو: ژوزه موریینو شب گذشته درجلسه‌بامدیران رئال‌مادرید از علاقه خود به سبک‌بازی ماتئوس فرناندز ستاره پرتغالی وستهم خبر داد و درخواست جذب این بازیکن جوان رو کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/23584" target="_blank">📅 11:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23583">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">⚽️
خلاصه‌دیدار امروزصبح دو تیم ایران
🆚
نیوزیلند در هفته نخست رقابت های جام جهانی 2026.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/23583" target="_blank">📅 11:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23582">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7leCbhBCTMYVpioIJPwY4oJuhK9iPbnfJsGSwm1XyxTQBKSK-aXLwU3NOS419Oe7lLuqKyZz_6L3dg_0dvgz7Fb3CpnKoEUvEfoL0BEOG_t5NCOw8RWWi6hrew31r3C8wev2hlymwdd8iT1IxYoAMLsEJXJU06C2ZkvlChO8ahgyQ9Rr-edbuLnw1R7ktSiqIVVzC9lqhO2EwniJWVoEFYIQDuG6i9NmD5tr3h3IIpSGhqoixsTqwDGljtcEU_EFoLqmlRnF1YqJVZOJbHSVuny2eDqY3ClQiRpvy_SUjkdV_Ievqnh3v7nhe491XPNiY_TDR27AwrjMqAk1cEmiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد درخشان‌رامین‌رضاییان دربازی با نیوزلند درسن 35 سالگی: ۱گل، ۱پاس‌گل، ۴ از ۴ دوئل برنده،  ۲از ۲ دریبل‌موفق، ۲تکل، ۳ قطع توپ، ۴ بازپسگیری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/23582" target="_blank">📅 11:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23581">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmt5iyUvFcTBB4jRiNm5JBy8kFS8ht9w8P6G4HFAZCan4OB5-N9aQnSkkPt6wcvw6gDZTNXKgFjUHBPAoN33cSt_fpyNoRcn6a8qFoW3Y_X5agqp59wMdnpbCZ8pzQ4IP-NQXhApQoj7p5AyEdMaVn-UnRowZO5LPu_rYPnmS_4VvgAbXmy4GFVPiouJfRbHdih21VBQkyu7M7YB8wEijUoycHNF0baQjE7RrylBUk6v0BEvrJOEENsCn_TjlALgH7apAruy3kqPOCWSe7P8ExeyPUpkzeI81lgi_qqA3ripJNvFMlZ23INhW0HvdPV4SVy_-7wcoVoZha9FyeLbNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
امیرقلعه‌نویی‌سرمربی‌تیم‌ایران: میخواستیم دو شب قبل بازی بیایم آمریکا، گفتن نمی‌شه و فقط باید شب قبل‌بیاید. الان هم میخوایم برای ریکاوری بیشتر بمونیم لس‌ آنجلس ولی بازم گفتن باید همین امشب از آمریکا برید. ما مظلوم‌ترین تیم تاریخ جام جهانی هستیم. ساعتم هم…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/23581" target="_blank">📅 11:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23580">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28dc4a75ce.mp4?token=VYN8ywNFpQi4h5m270PFzhHFxlgwKJI8htaF6Gk0t8pRJkO9y9Tx_KfTLoT4C3ATfUt5LFHG9CxVDDFrN5WHJS6NVBiv1DEVKDxGaIa40kCeJL_5L7mEb7iswjPtelju-ksjjJzpI5H7gpRoSg6LxziJoxE2KGVRTAti5XPOjxoTKsmKA8lT44lJ9SsjhobD-PSLf56QKR3GDohh6F3OQc73s6HF3JtXfu_ydU_Ml5rti2ORUJ2t4HB2LdVe15XLw8pedJYxgb490mWKnexqfEmLaA8Fuc0zwKlJofSrYd7h1tU1KH--tCmqfqYhLABPSZYfq5lNoxTqXYRFqdmDYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28dc4a75ce.mp4?token=VYN8ywNFpQi4h5m270PFzhHFxlgwKJI8htaF6Gk0t8pRJkO9y9Tx_KfTLoT4C3ATfUt5LFHG9CxVDDFrN5WHJS6NVBiv1DEVKDxGaIa40kCeJL_5L7mEb7iswjPtelju-ksjjJzpI5H7gpRoSg6LxziJoxE2KGVRTAti5XPOjxoTKsmKA8lT44lJ9SsjhobD-PSLf56QKR3GDohh6F3OQc73s6HF3JtXfu_ydU_Ml5rti2ORUJ2t4HB2LdVe15XLw8pedJYxgb490mWKnexqfEmLaA8Fuc0zwKlJofSrYd7h1tU1KH--tCmqfqYhLABPSZYfq5lNoxTqXYRFqdmDYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
امیر علی اکبری در ویژه برنامه شب گذشته جام جهانی به این شکل انتقام همه رو از ابوطالب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/23580" target="_blank">📅 10:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23579">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwNOfMYac1iJrAsA_vjt45mxnbQojYkRx2uMxq1AkpKZ1wlU9LolqVbuKnNAFsnkAVQIVmyPXzuXLMPuo6UrANesa61a2yDMZqr4RnJxQMr0LLhHe1Kkw5FixMSgZP5xsSnuyQmyl0T2PzKxuNkAZeUCemTNfvjILZHEWRrrBMtNlTUweYYdFj_VWrKoCWYLyXiKIRJnqeu_5p-g0D-PYBaDTcWV8gnpCuhksE-8Qd3_iMdNnJZ2lqAmSi_0VTAvylGIwJu4_yas9FIsAOo3Ai3cK8ABxFaEPYLjbQ5TZ6YhLomlK6z6k2uex6B-9hTGtFmqPGMOTyxRIThrG_l-Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه سپاهان برای فروش محمد امین حزباوی، آریا یوسفی و مهدی لیموچی روی هم مبلغ 220 میلیارد تومان میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/23579" target="_blank">📅 10:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23578">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82ea73ae1d.mp4?token=FiE1uNYmSgCkTnZXwiKtp9TQ216eQ6GhFownwdUYoHSEO2Sr1_ZFsg-0xV7piur7wZzosBLS7scyizAJ_vcBlR4c44Zu7RGbnbIebO3HkjEg_BIezeQH1rNjb2qI2q3cUikGLHBbiDwGAfReDnkLXqKlo16Fx_P1SS9OZ7UX7SwFXfcDCsD8UzKRaUrBtDCZuuAWTzPZzUyy_wfSGoQ6yga1oRrrceiXjahSoSMPOJOXZ5Tneg7OW3HhqiEFUYF7UollRT6MEH7sfohfAioTC9qCmcPnTqEAwELbMyx1ZwVveQ6ltbD5GqNdMh0vZow_jKwcbEHTuomHNtoxf6kA9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82ea73ae1d.mp4?token=FiE1uNYmSgCkTnZXwiKtp9TQ216eQ6GhFownwdUYoHSEO2Sr1_ZFsg-0xV7piur7wZzosBLS7scyizAJ_vcBlR4c44Zu7RGbnbIebO3HkjEg_BIezeQH1rNjb2qI2q3cUikGLHBbiDwGAfReDnkLXqKlo16Fx_P1SS9OZ7UX7SwFXfcDCsD8UzKRaUrBtDCZuuAWTzPZzUyy_wfSGoQ6yga1oRrrceiXjahSoSMPOJOXZ5Tneg7OW3HhqiEFUYF7UollRT6MEH7sfohfAioTC9qCmcPnTqEAwELbMyx1ZwVveQ6ltbD5GqNdMh0vZow_jKwcbEHTuomHNtoxf6kA9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این گیف عالی بود؛ امیر قلعه نویی حین بازی با نیوزیلند بدنبال‌ساعت گرونقیمتش بود. مشخص نیس کی ازش دزدیدتش که اینجوری داره از هم میپرسه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/23578" target="_blank">📅 10:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23577">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3u0Xr3x6M1SGAj8sfTTR4ZGNX4ZVMDFQkjYKfyIi4fIUCH4zd1I8fLuSmGY7Zu_F8G6RCaYOjR5FOJDTe7jJmC_9GU4FpA56mWNGj33FSxXoi7bgqB0R4xSNXwJG5RHEwLZpBxGZKEMC96C48VKh2qpvjOcNdh49IH-bh92TgpQXz4K8vug9svX2IFHWzOd0oAar3a6jkHSyO8o3k5wKKYukaGDv34GoKaVae62cz0pBOwuA89fmW4l0ChjZNMYDjVQGlX3SEKQiusqBWOLTIgMsPoZa36iwYwrOxMTUvHqdK3FrcT8VLJDRy0LA1AwjlJkUPsWaAeJsPWh59paZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
شش تیم آسیایی حاضر درجام جهانی 2026 در دور اول مسابقات‌شکست‌ناپذیر بودند. ببینیم اردن و عراق امشب‌وفرداشب مقابل‌رقباشون چیکار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/23577" target="_blank">📅 10:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23576">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pzj7QE4Yxe_P0fWw748A0ccjYLny7TPDA_QN5PeTIs-VwRog0Zsr1ragsHdyxCdfxlbZPABwqlrrZGQGO7kIJEs0UgI0Z4VixouhT_4qH7EtooY6N0MjV5iZCWVU9iGKSFljV38zrEepwhSey2AI91_NQU0XaxTZXAFJsxZPCcHu8DDEHnU9VKN9nbkiMFSA-qeRkdOhSKXEKH5CMMgiUR1lWqx-kk-qa0soDCSs4aUehiyswwyslzcMHhl81A-b9iYts-F26CHWolZuZoO91M-sGtSriwV2K5EMqapRgnntARpk_H9g6vEib1xpJQ-mQCjik4upPJQkf0HGJRUBAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
شش تیم آسیایی حاضر درجام جهانی 2026 در دور اول مسابقات‌شکست‌ناپذیر بودند. ببینیم اردن و عراق امشب‌وفرداشب مقابل‌رقباشون چیکار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/23576" target="_blank">📅 10:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23575">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a244147c.mp4?token=sLnQKVXT0J0qKCTVi2I2enviAJFgYQM6_XJQppreonnJAiL2WcrztHn7OXojow2XaWD-YTBG_hiYMuhU48Pp6iNDrCin9B2BUtniTB_UhaFW3xRM_Q-1FHCnUulFGp9zSA1e37Q9XNZprV-0UJc5aWAbZ-3UEI3xSOcMKjoEXINFmBEK3ioo11f4wwzLmBm3juMn15oMWvrYWM4TY-H1lsb1iEJcoXIk1svJ4f8xr7yP_S-U9y6YnLIw4Hp1iVApgSpe6A0S-6KHhl9wKb7PQPkd2EN7rWPRczwpjbUmPitW0UP_YCRxyTKWaHi-YFxyLnj5KOlcA2fNW7I3MZQufw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a244147c.mp4?token=sLnQKVXT0J0qKCTVi2I2enviAJFgYQM6_XJQppreonnJAiL2WcrztHn7OXojow2XaWD-YTBG_hiYMuhU48Pp6iNDrCin9B2BUtniTB_UhaFW3xRM_Q-1FHCnUulFGp9zSA1e37Q9XNZprV-0UJc5aWAbZ-3UEI3xSOcMKjoEXINFmBEK3ioo11f4wwzLmBm3juMn15oMWvrYWM4TY-H1lsb1iEJcoXIk1svJ4f8xr7yP_S-U9y6YnLIw4Hp1iVApgSpe6A0S-6KHhl9wKb7PQPkd2EN7rWPRczwpjbUmPitW0UP_YCRxyTKWaHi-YFxyLnj5KOlcA2fNW7I3MZQufw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
سوپرگل‌دیدنی‌امام عاشور ستاره‌تیم‌ملی مصر در بازی روزگذشته مقابل بلژیک درهفته اول جام‌جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/23575" target="_blank">📅 10:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23574">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔺
بانس‌های فوق خفن مل‌بت
🔺
🫴
100 درصد پاداش اولین واریز
😀
100 درصد بانس یکشنبه ها
🎁
100 درصد بانس چهارشنبه ها
🔹
هر روز 1 چرخش گردونه 1 یورویی
😀
3 درصد باز پرداخت نقدی
😀
بانس شرط رایگان 30 دلاری
🎩
10 درصد باز پرداخت نقدی کازینو
🎆
بانس هدیه روز تولد
💵
و چندین بانس دیگر از جمله بانس خوش‌آمد گویی، بانس شرطبندی طولانی مدت، بانس 1750 یورویی کازینو و...
💰
هنگام ثبت‌نام با وارد کردن کد هدیه Sport100 بانس 100 دلاری رایگان دریافت کنید!
✈️
معرفی سایت و اپلیکیشن مل‌بت
🔄
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/23574" target="_blank">📅 10:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23573">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDROfBypq7Gotu8AG1S-bzq1CKMAHYMllNlJtRnYsYFIOeWH8SoXEsermU-r7q7TOdwNYSeTPSCgD5zvN5TKlrrWamnWNP9tvLYUlqM8xuCw44ca6r1ClYNT1FegBJcqhxKCotdGhEfP658DVwpGV1MnWv5CmqOF91oJDh_mqh6qpqm_bgQawIWTMFAa7wY1s9LmFKq-QKUzwXFDlfKNiUfDtP7b6aM4Ku5E544gcwuGpkCvTYUS32ahTX4BHpGiT5uKzKIlTnEXk6Gzcw9rAFKf_Rr_MCR1BYpGf_h5PNul0DP05EddDY-d4wlAblFCTYxFuJWLCuGCeTLzmLX1EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌ های پرشیانا؛ سیاست باشگاه استقلال در این پنجره نقل و انتقالات جذب بازیکنان جوان ایرانیه تا درصورت وقوع جنگ در وسط فصل اسکواد این تیم خالی نشود. در بین بازیکنان خارجی رستم آشورماتف، جلال ماشاریپوف، مونیر الحدادی، اندونگ و یاسر آسانی در تیم ماندنی…</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/23573" target="_blank">📅 09:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23572">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tV5ATugQCqoSm9eZ_y6N1_vH5r4ix3ZWeyOw1VkuPjYtPugwQTesITDV4m8SqVZxkLwAM5Erg0SIkEcGDf5k-CNE7PWjmR26DTmj6NgEr5sQRAyVXmsI2UO8553oG3OVBnGJqZkTd1bO6x-1RaB5bSp-50X9ySHnxR46FssLa1OlFXdTgEnwUBH1FJ4NKebmnNgq1IXM4NpnFCklEC48Qcou8bNWG8zZltmYrnf-tLXzglI7hRrM4Z7yhdh1ZDU3gzJe_-EZlU-pPBzScYoVnedShl5ZJVMOk-lbK4AJMhZjKSePZFQmVEGYEt03pDvCNH2khtoNjIOCVYj5fedUOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیران دو باشگاه مس رفسنجان و نساجی مازندران در روز های گذشته مذاکراتی‌باسهراب بختیاری زاده سرمربی فعلی آبی‌ها داشته‌اند و درصورتی که بختیاری‌زاده با تیم استقلال قطع همکاری کند با یکی‌از این دو تیم قرار داد رسمی خود را امضا خواهد…</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/23572" target="_blank">📅 09:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23571">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/607d3917ea.mp4?token=MFJqJzpTLsxUJqtFPqFc9wFqTpqavzjCFo-EVwu-WY5_ysISrS5If5KyxPVqNzEm7VWzOj01HFZpEk-apHhFjRmIssqctXHuUNX8wei6Nzvu16O1EK9UrbW8b2vpq1pMF9aiIwbt89nGgt5sCHk-c5fS28Esig1BYW8L0exMGTGLTjpjiyvOXliWDjc8h1-lfwD5GI-_I9NHqtL4gTNc318iHkrIp8520MYUolkeFaS8fmfdljCOlb66q5mPyU4_DFNtjV1xzlSP9jzzQctpHOMD7WlW-jsk1stmSBJEBvBmAYIDT-lG0j5sB09PYI-ESMmWv2v9U90rAZRYiJQPmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/607d3917ea.mp4?token=MFJqJzpTLsxUJqtFPqFc9wFqTpqavzjCFo-EVwu-WY5_ysISrS5If5KyxPVqNzEm7VWzOj01HFZpEk-apHhFjRmIssqctXHuUNX8wei6Nzvu16O1EK9UrbW8b2vpq1pMF9aiIwbt89nGgt5sCHk-c5fS28Esig1BYW8L0exMGTGLTjpjiyvOXliWDjc8h1-lfwD5GI-_I9NHqtL4gTNc318iHkrIp8520MYUolkeFaS8fmfdljCOlb66q5mPyU4_DFNtjV1xzlSP9jzzQctpHOMD7WlW-jsk1stmSBJEBvBmAYIDT-lG0j5sB09PYI-ESMmWv2v9U90rAZRYiJQPmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌های‌سنگین‌ولاتی امیر حسین قیاسی خطاب به محمدحسین میثاقی مجری سازمان صداوسیما
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/23571" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23570">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRkle1IlmrTAy61zhjTFWVAES0AMAQb_cO5iIPqU755KFR2i21OyHbFrJ2c0AX61tI4Zqlsm-SllDURdfNxWNFRnWkMZLzX0Shkj4-4nuFlF1u33dfyvzaT9p5_4JKEkFS4YDDU-Jt3bHgcPiW7y4hDfjcPDWVIilJCS5A81mdj-oM6oMnEYldlDJ65jvW3vjG1EUMy_I1zaM9zQKJnEWh-uL1IjfwxuDNlgsJgq-JLL0D6j-BxyzxF4BJvPgbrwtczTD32zFce94LV6SGJmz8sz4dXbbKPK-bSAVh1rzmy8PAljll2pC-ffR5FhYMZyLGyfe8usdeIxFXbBdvLnBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇯🇵
موریاسو سرمربی با تجربه تیم ملی ژاپن با شنیدن سرودملی‌کشورش‌اشک ریخت. یکی از تاثیر گذارترین عکس های جام جهانی تا اینجای کار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23570" target="_blank">📅 09:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23569">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3e9cf628c.mp4?token=R2wtp-7JdurpGy0XGWGQsp2O8og0CfRV-CzVrPXmR1jqxvbkvwTyp_1EGffKTNzejggxR4J8b86sm7W-d6Hf_QGOfkWpJC0D6npruWg7F-Es7HRNr2pggSPiIUwixm_wv0sMR18vXjVWM6GDSRV3wfEOaDPixvhog_EByuXtXnIJQ4kCLjkY46CQZxehbrIYZ6r3G9vl4Z3cr5Blz4e8etB4rY_2U2ea0toNzHleODraw1ZrcK0z2utAQKzGnJrnfn33JuPKC8chNoA9Kmsec6gx2PAxRCbzNxXOFRmi6gOHcEkx5fA8KBqckICWkj6rigBUBelwz2UGOLV1KihWCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3e9cf628c.mp4?token=R2wtp-7JdurpGy0XGWGQsp2O8og0CfRV-CzVrPXmR1jqxvbkvwTyp_1EGffKTNzejggxR4J8b86sm7W-d6Hf_QGOfkWpJC0D6npruWg7F-Es7HRNr2pggSPiIUwixm_wv0sMR18vXjVWM6GDSRV3wfEOaDPixvhog_EByuXtXnIJQ4kCLjkY46CQZxehbrIYZ6r3G9vl4Z3cr5Blz4e8etB4rY_2U2ea0toNzHleODraw1ZrcK0z2utAQKzGnJrnfn33JuPKC8chNoA9Kmsec6gx2PAxRCbzNxXOFRmi6gOHcEkx5fA8KBqckICWkj6rigBUBelwz2UGOLV1KihWCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه‌نویی در نشست خبری هم ولکن ساعت رولکسش نشد و به‌این‌شکل‌اون‌رو به نمایش گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23569" target="_blank">📅 08:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23568">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTYz06uHhpJB9xkzg29wLo9Oowz5WCVK7Qie5XcJhVLm5tToiyu7fpfJZh3KVB0Uj_yzaZzvOG7_TTgRX8uLzfcpbDegAgill2r6yJY4tSlKVpbOd3FrgquNEOY_NIPN1GOJh5agSU8q8XwYOe9BCeosWCL2IDvvjdepjhvqUCAMNkgCLxun8W638k7Bj8r8A2oWrKMCyf5h2sm0DLkJ_f_12fL9p-pTZxlDPwsw_FH4LM1sW3efROCSuRsxb73FfNeLlK06TodYSoVRo_EtpPUEyDwYwzsQDbx2xvDhImhOPYzOFiRPndKdV5lFKMDshWyW_SFm3327Ev0nJ1XPiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه‌ بنده‌خدا دیگه رو برد امشب بلژیک مقابل مصر 8.5 میلیون دلار شرط‌بسته‌بود که خیلی شیک باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23568" target="_blank">📅 08:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23566">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YFGXQSLwGhEMmfpVJRkRTKX7ldXdHk4jf6rkPYma3W_zGk6alcUIWkoebLuWwtPb3mshsTjr10SG6kswMfsPh_gWlh8MUUavImpJ_Dnxa78FQNBDqhizSsV2ffhNyBeW1gGofLx8jB66-B3Gw6-y_7MBpyL3v0pr94bfPTkZCe4y2K9-WPkq5WMSpJAzepoVQp_Vtifk-5mfjawDHTID2UzLjiuyq0Td1aGlAHMA0g3coHsIPO0ELL7bRlKie3ej0hWU4_ymzKRxtzlhrlA4vBJtEf-S612tvFQsuJXQW4pOIjyNCY12l4oXphEd_K9_TXkGxejsrU8L4c8JS8lX4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gT34gk2o--NlFiUwY3sGnfOOX6w4V-GqW4myXD2QCj_Wk4h92VfE2d9Z062ndhNhG4VZ-Bzb9L75KyQvwY2koiSBCpYzv_1LQV4sQbN5LDQ_FP3riby-V3OLbzpAK2NsaPZT9SK9OIBY31DTWFSmd6PBWdR69hiK6qm5Dvf6ZZmr1_e-YUwVkIFeeuraSUk8i4UAhuR_uMwwsb0cYkF5IkHO4anigmYVyXxDPGnyunUYk3AG_lpmy219L3zAMB3RnZ759hc_I7sK0zUgwMgwyrGxAZqPr2kbKThSfwllbFG0slzEEx-SilOO_HhInJBTRTQWUi5F6XUv8Jl3lAkVpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
نیمار جونیور اعلام کرد که پارتنرش بارداره و قراره یه دختر خوشکل دیگه براش بیاره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23566" target="_blank">📅 08:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23565">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVWkrwJLbT6Q1YalylSdhJAjJTDAi15Bq2UItHTeHul6tZIuAx8Ybh9VYWHeE1JE3_n2flrIyy7c-3fdmSOfSU27o4M-Y_LcQKz7rCtPgsw-eK5Ufj1TfIWctGcUgK70VQ-vANEcP1s6-FaKuBIWJprPs4HSoa3FexIdQW1BOWNqrBAS6c4mDitYtmoz1jweQjGal8kwxcuJFBA6wVnSFuj1Y5DuysZOijNSfihtJRA98u1X_wqASIxEFzlwvKdfdwh9fZrZRVrFGOXrZWAjOLbnUT24zwGAVdtr1e-gEoNddW5SC43KFhhbYFQqXu0XII59TrTIDHM-fA7QFhZ2hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد درخشان‌رامین‌رضاییان دربازی با نیوزلند درسن 35 سالگی: ۱گل، ۱پاس‌گل، ۴ از ۴ دوئل برنده،  ۲از ۲ دریبل‌موفق، ۲تکل، ۳ قطع توپ، ۴ بازپسگیری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23565" target="_blank">📅 07:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23564">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ae8867bbe.mp4?token=GzjK13gJI9vTvd9McTgFT5lqrnwkS9158pq7mKc10zbKLmlLuMrBaIDIxWb_rlkwZYiJuzmlWUxJjI0mJ6cqdvQJzSrjIbphGVBuU1my75RUhOIxPPtwv6jl9uMyHM8I-SWiuIXQFDBxGem9IeQKHxu03yzESY98e5vbIYBgvU3Go8LPW-N3cHiFWcAkyWgtsNwlBqhjVWttNlkh3p403ZuL-uCIb4tmdlD5bw7X2a2RiFeiuZGkUuvX0GiRsF3xdktMtIL313uZCYsUViVH8JLbslUBprjuuBQbmM3-_JObTkwMeqHXWXRfQMFkR9uGa9aOohe1s0YiNZjN1kvMAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ae8867bbe.mp4?token=GzjK13gJI9vTvd9McTgFT5lqrnwkS9158pq7mKc10zbKLmlLuMrBaIDIxWb_rlkwZYiJuzmlWUxJjI0mJ6cqdvQJzSrjIbphGVBuU1my75RUhOIxPPtwv6jl9uMyHM8I-SWiuIXQFDBxGem9IeQKHxu03yzESY98e5vbIYBgvU3Go8LPW-N3cHiFWcAkyWgtsNwlBqhjVWttNlkh3p403ZuL-uCIb4tmdlD5bw7X2a2RiFeiuZGkUuvX0GiRsF3xdktMtIL313uZCYsUViVH8JLbslUBprjuuBQbmM3-_JObTkwMeqHXWXRfQMFkR9uGa9aOohe1s0YiNZjN1kvMAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
گل‌های دیدار امروز صبح دو تیم ایران - نیوزیلند در گام نخست رقابت‌های جام جهانی؛ رامین رضاییان بعنوان بهترین بازیکن زمین مسابقه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23564" target="_blank">📅 07:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23563">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b16918ae52.mp4?token=aOdmEbxRaZqdANwOeiXZByBL4KKfJkoL_ny0_o6qruBqiHnD3m9hXGgNFv-NRmQg18aSP4XQgpUe1o-J5S7UXG546j_gRXHnl-8W3WZ6dN7vd7JQ-zbUXMiKNf6slEXfJSnPkxlKqIVnQqXydNG2vNkGLBt2P67s2X2mU1uuS-7LXL1WRnm8LbTETy3AJXeK4sWkTlTBZ06AH3trvy1RwRGshq_NVnnQxa74TI3F07Ew1H8tz8q9JlWXOv44-OWNeKbsxHSD5O-X0AGVntRNo0Hqp18nMOVomFrGRIOnxCPsvBLoNDT_dYYZiu7dVR5e04Oir-FVIs5f_g-0eXo9iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b16918ae52.mp4?token=aOdmEbxRaZqdANwOeiXZByBL4KKfJkoL_ny0_o6qruBqiHnD3m9hXGgNFv-NRmQg18aSP4XQgpUe1o-J5S7UXG546j_gRXHnl-8W3WZ6dN7vd7JQ-zbUXMiKNf6slEXfJSnPkxlKqIVnQqXydNG2vNkGLBt2P67s2X2mU1uuS-7LXL1WRnm8LbTETy3AJXeK4sWkTlTBZ06AH3trvy1RwRGshq_NVnnQxa74TI3F07Ew1H8tz8q9JlWXOv44-OWNeKbsxHSD5O-X0AGVntRNo0Hqp18nMOVomFrGRIOnxCPsvBLoNDT_dYYZiu7dVR5e04Oir-FVIs5f_g-0eXo9iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته اول جام جهانی|توقف شاگردان امیر قلعه نویی درگام‌نخست‌مقابل‌تیم کم نام و نشان نیوزیلند.
🇳🇿
نیوزیلند
2️⃣
-
2️⃣
ایران
🇮🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23563" target="_blank">📅 07:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23562">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✅
هفته اول جام جهانی|توقف شاگردان امیر قلعه نویی درگام‌نخست‌مقابل‌تیم کم نام و نشان نیوزیلند.
🇳🇿
نیوزیلند
2️⃣
-
2️⃣
ایران
🇮🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23562" target="_blank">📅 07:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23561">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVbVS0zesa9Qu_22wTEzgcGg879LD-ja9QWzOZNy5tw5qMw74psLZ8XTqE5yiake6aOW1Cx-rNsi79EoAEDv_ChV_i6JNa5pHCxxTDp0z7cOSdZliyqgmO56yYkFs_Vg8kUZVrdjzByWZchCquVsVv87cXwJPMqF4RG4GfcUE9rC77ZcuZqNBD0CYDNHvwpZOIG0P0YGTFbYBlotmln30vpxxhAfonGto8wTEsezUobGsxgnr0KMorWC-6PFzNZ3WC42yi5_IeqRz5yDyTd1g9lmVM1eNrHX-Y-xwyL-KwkpJ1DRGlA_Lc7VRqgw_1aQpNTTLlPJ7G3iO3ECtEngvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ از مصاف شاگردان قلعه‌ نویی با نیوزیلند تا اولین قضاوت علیرضا فغانی در تورنمنت در جدال حساس فرانسه و سنگال
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23561" target="_blank">📅 07:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23560">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXpgkJKaS6OfQavuL2dC_vBonx0HNeL9p7AHH9Q5Gc_P5sQY0CVV77m9ZP7y2GiqbKnsJVIiB_-UMH3iXg_7qI4HKNaw_yiF87EzFwIskgbCp_Knx00fheL_zcjbzN4jchU1S0zUJLrWfvtu1ZftV4Sm-fBwHpw4akZ0RwTT9GyDpqqYVMoYokmKq_NXFEtRzhhoraGdqIyhCXIqHhLwJD9zf8n_0C5qBcZcmCo6KBTPk5I_1Q9cZcUoHa7aMnOoiu0mujHLS2NZeuyK03HBZ0Zazs5jNnor7pqMH6ZwNgNKUYdNui9ZqUNlT8apZFJIwAN5ZoOhHJpRHL7nD4NgFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
احتمالا فرداعصر ازتیم‌جدیدکسری‌طاهری ستاره 19 ساله فصل گذشته پیکان رونمایی خواهیم کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/23560" target="_blank">📅 01:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23559">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5sdlkQFTUiSuOMIsFd9V3He13hZvasOS14OHVySpR56JsDJzqs_vN5VujYQEiVOKWsVztzNR9DcwpD5TfKdaIdwqCTuFxO5x3r32vq1u0_BeouG_LQpQby3d9aQXKtnb1XtgnnRVzZt9Jt1gBdyUda0he14AESyA_Brh9OezLWTQGYv8PVurr2ACS2eS2XUrZ7HmiVkcRa4cZkfJFmuSE_iaY12os3ZiRsffs_x1odsdRVE9mR5JLyvRhWttFgAPk0EOTdLlQh98XsN1qcTqrA5rSVm-DMVWNzdg83vvZx_3o66shs6on_US1iJIGG76NLFeUuwoSYejpI0W4tt0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وزینیا دروازه‌بان 40 ساله تیم کیپ‌ورد، قبل از بازی اسپانیا و کیپ‌ورد فقط 50 هزار دنبال‌کننده در اینستاگرام داشت و بعد از درخشش در این دیدار و انتخاب بعنوان بهترین بازیکن زمین؛ تنها چند دقیقه پس از سوت‌پایان بازی، آمار دنبال‌کنندگان او سر به فلک‌کشیده و به…</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/23559" target="_blank">📅 01:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23557">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NczLUzXn2I4e-ltrNms4d5fLwpAsCEy0QPfTcpaS9j4BYn_gLG5uPiCvOeixseRrCyQ_5yCuDsAgQsz3icXdE_zEuwBOBATzuoDI9t5Uplzbh711gFo5ojhrZHAa209SyFpEAi6duItofo6K51gNXh07OIXZmmPvNCeUD0f6doihwBUh_vzMLtxLWG8ETAfJcJWlkql7Clj4fKdSg4IOuHf-G1LLv4m2s5_6SaaYaoVm9TW6hEVtQiF3_OgDjR-vRcT73TnnIV1bjLG4e5rgod1WU0oNRnOQ1SOBd0Naxi88aN4w7wIePF1AuziPTZDVf4QjXdmS6vy6wac-hEAEFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
از مصاف شاگردان قلعه‌ نویی با نیوزیلند تا اولین قضاوت علیرضا فغانی در تورنمنت در جدال حساس فرانسه و سنگال
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/23557" target="_blank">📅 01:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23556">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hii02t00WKYavKBhJN5Cz_70pkd_SFdiEZO95NQKEJKr4dy9Ia0g2uv7a32lSLWiXetyu_HOgpxJ8maLYifOtnqg5-w7cNfHM_RY5pUEaY_hkdkLBbkr5eEivC-7loUpc3J5rbixURixNAE9Fo-IxmZ7WwmuluvVbL_-vTOjczmZ0XJ-5w98BUlXQQx1GZ4oKV1Ny9j6CFTFs2upQ-qR6famosNDcEryTkPjS-xrObAPSfDb2ZJmUKOQrt2Bz0R8D7FUnKGOq9BIJH1MrG98eS8BiMOnfGme_PUU16ShJsjKxqR23Ja1hsFf_C4gZdmLgZvuugutOxV_JNV6DPUVYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌‌ دیروز؛
از آتش‌ بازی سوئدی‌ ها بادرخشش ایساک و گیوکرش زوج خط حمله خود تا توقف‌غیرمنتظره‌اسپانیا و بلژیک مقابل حریفان خود
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23556" target="_blank">📅 01:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23555">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11adede3d.mp4?token=LPvMT6zUryHcD_lZ32hN1U97VECf9i4mU94nEcTonwKfrYzijDNZQeGv6TwjAzZ80zh31e62D3z-dTUBjXRXg-bvuibrNnHqfBDjCLykdwThEA6pgRDxXpt9VNwt7qikvS5-ocj7VFdcPWB6p8lheG6HAzNTcxA12xcPum9eWzsQIEyRoM6JA5-ySXxx7aQ4ndrl3zpZ7rPhOqxsfmfJwDB8nhWoLOirp_vC2wTKJwg-a1c9KD3iEKHEU0gqgSzbNgpJQIgEinsb0BmzmAJ5ZA31SoX4Jp8SjuqslE67FxZsE3urY_QxMHbzdZrJld8TCMqfUyuH-V-DLmw_xoFqYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11adede3d.mp4?token=LPvMT6zUryHcD_lZ32hN1U97VECf9i4mU94nEcTonwKfrYzijDNZQeGv6TwjAzZ80zh31e62D3z-dTUBjXRXg-bvuibrNnHqfBDjCLykdwThEA6pgRDxXpt9VNwt7qikvS5-ocj7VFdcPWB6p8lheG6HAzNTcxA12xcPum9eWzsQIEyRoM6JA5-ySXxx7aQ4ndrl3zpZ7rPhOqxsfmfJwDB8nhWoLOirp_vC2wTKJwg-a1c9KD3iEKHEU0gqgSzbNgpJQIgEinsb0BmzmAJ5ZA31SoX4Jp8SjuqslE67FxZsE3urY_QxMHbzdZrJld8TCMqfUyuH-V-DLmw_xoFqYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
نمایی‌ازاستادیوم‌سوفای‌درفاصله‌کمتر از ۴ ساعت تاشروع بازی دوتیم ایران
🆚
نیوزیلند در جام جهانی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23555" target="_blank">📅 01:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23554">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a904e7169f.mp4?token=bUwd1U5mAM4FekUn9wSV4Q1DyvcsM9OVjeL7GOgdTBm_TTkOLc5jhkf2kc4Rr7GFGrNilnsqynL2UjvYnOwJS3Vu3nLZ7tNj96NTpH6TC_hI9gS7sEoFxLxY4gnikwh2q5PDQ5ALBN8BygytfsQdeuZsrqJLlKzA0R3pP6MeJdTJJUvc4-Uzd-iYJQiTbODSC0Fn_G9pIkLTMpSZ73hoxxiHvcsX9p4E0e0bX7iqe3RyJzajh2rMsbsVVX0W86aMyDDtPJ9UCm7u8p0ufb4Vl6i0sr07frfUhW3ILL5RI9RbDEPlP72mhMPRQmMDbZRvnXTniOQSY9ZzAFqvFeZV7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a904e7169f.mp4?token=bUwd1U5mAM4FekUn9wSV4Q1DyvcsM9OVjeL7GOgdTBm_TTkOLc5jhkf2kc4Rr7GFGrNilnsqynL2UjvYnOwJS3Vu3nLZ7tNj96NTpH6TC_hI9gS7sEoFxLxY4gnikwh2q5PDQ5ALBN8BygytfsQdeuZsrqJLlKzA0R3pP6MeJdTJJUvc4-Uzd-iYJQiTbODSC0Fn_G9pIkLTMpSZ73hoxxiHvcsX9p4E0e0bX7iqe3RyJzajh2rMsbsVVX0W86aMyDDtPJ9UCm7u8p0ufb4Vl6i0sr07frfUhW3ILL5RI9RbDEPlP72mhMPRQmMDbZRvnXTniOQSY9ZzAFqvFeZV7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👤
🇪🇸
دین هویسن دفاع اسپانیایی باشگاه رئال مادرید و همبازی‌سابق‌سردار آزمون درتیم رم: سردار همیشه به من می‌گفت باید بیام ایران و ایران کشور قشنگیه. مطمئنم ناراحته که در جام جهانی نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23554" target="_blank">📅 00:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23553">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0ct5OekpXAyUTRjmvlqZMeUixTpX7Hwco1NErGaYxXyCxfnEWfMp5P-MY-2M6JYYCOl0w1s5qcw1MaXl30MxcDd-KBXv9JWJoERjaRgQD88QqO4OtMA9iWTIRhu4DnHrnvB2H4O6Qw29b9l3i9LJbFn1FPc-JaXkbj78ziXGUc8tvpruRzlpbwpe6oqw7PByFfAxRvozT_1dXSdWUYCXZ_7QmNKKBkQRgyzrqULkxWQJjerLGgrnfLPcqvSzhist0AKG3J9pkULiWaBYvCxWHRS5ol8LxQmthtKY06rJyt67m68mxRDdgsLSu1zk8n5NOb1x4oipR80Jt74R6d85w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه‌بنده‌خدایی امروز برای اینکه 85 هزار دلار ببره 1 میلیون دلار روی‌پیروزی‌اسپانیا مقابل کیپ‌ورد توی Polymarket شرط بست و الان همه‌ی پولشو باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23553" target="_blank">📅 00:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23552">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQqfb1-uceCvlrDJTRksvACiXS3WoUxwGWn3ie5eZsoOFWaGTxwhuenrVmgMoRi8TxFe82bkfbXj8WhHeS8tQAF7_sZTG-9Dvm5J0EXei0hogUfJLva0VEfCMs-xYHjh74Wg-5WiOFADvMjJWfaKVMkH3zdBm6419wjvWkS8YDgxVN-lQKqaLEfxWoIo5fmdBqyacej0C1avHP6l9vbfwwpA92CoiF_sf2Bdepp4AkPHTmNWlfvRDKqOHhtHPfIg1_Rf3-3ZLwOPa2CCr63hlETU6bxliQKvout9ob893Ws0bG_WHAyBbUoFRwDwLKPhPLkMzLRj0VTqlkj9Vlt8wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇬
🇧🇪
این‌هوادار تیم مصر پیش‌بینی کرده امشب مصر بانتیجه سه بر یک بلژیک رو میبره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23552" target="_blank">📅 00:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23551">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/auyRIkhTlif06WeArmZrOUv5M9cdJjmsUiYOnk6RCZeB44uGbSUBZd9-HXwnm5EFX-fc8yLEx1g7nahXit4OfcwVXzRKVbnva1vxzEJZt1LutwwviOfjxEP7_VySRx8-gicG7iAfchSZ11kUWeAd-7J5c_v1q5nqHdMz_PQgG0uXrsmAkmle-ma8C83UkRfJBWNCpKYvnhi5G3bIIeXb_ihUpIRYKKUXrPn8L-Jkqv2DtdQ3yxkLJvsR4GboCqH1-aA9ajSOuP5qXnUky-wlRhLq1tzqMCBHaefpUo16sRkSU0_eAytIEWNC1grzyEOE9DHu-aLRSjBRwa2xm9qinQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ همان طور که دیشب هم گفتیم؛ نماینده کسری طاهری مهاجم 19 ساله روبین کازان امروز صبح با باشگاه پرسپولیس جلسه داشت...اما طبق‌‌ استعلامی که از مدیر برنامه این بازیکن جوان گرفتیم هیچ قراردادی بین‌طرفین امضا نشده است.
🔵
جلسه‌نماینده طاهری بامدیریت استقلال…</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23551" target="_blank">📅 23:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23550">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqZvPffBElSBxgpHRyDvAPXW0g9DE0QXN3FDKi18gj2D_g9INV7BI-PiYCExFfzalvCw6bzRU8nN8Dx9K93qndQa142Az0MIxCZdoJZjNkEwPS7Ubpif2A6BsWA-tlUajyMHFz3K1s1RTir6_PYo47q_wiGmH4uXGKPUu9Yw8JC2aiB3Rj7Jj6BY0GQ2nVKEIOvIyf9OMD8CLHf6AC3SVG_W0T07UjaTOxmlptj0GTT-_7Z4AgacjKHVav0AlV_1dOqaV5BS0ea8P_7N0nGqtn64Q1Zcsky5At2FgYJNJFWnrVnPlS84eCI1cgxMxaJAaq7QudfRUMZq9WRhwOexYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇪🇸
تیم ملی اسپانیا در جام‌های جهانی اخیر:
2014
: تنها یک بردمقابل استرالیا و حذف در گروهی.
2018
: تنها یک بردمقابل ایران و حذف در یک هشتم نهایی.
2022
: تنها یک‌بردمقابل کاستاریکا و حذف در یک هشتم نهایی.
2026
: توقف‌در‌بازی‌اول مقابل کیپ ورد. دو بازی بعدی مقابل عربستان و اروگوئه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23550" target="_blank">📅 23:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23549">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSSxvnLPnMbyrrsvdvfajAFTxSBcqF6VrzcFoR2wm93NS7MoSEcCo2hS02spfphF_zxyT4SaOugrHtECX3afTQdtUAO6OTYsrNaLpzcQXSnm8OjsxKrLaVqdf1ryqCX7dLAOjq_KMGMJrJZZnP4QPH4Dd-uYxHzVCqw7Nk0PNjUSsvJBNT79MjkiamsMzYsw-vWkrhyL-LX36dHq9NOmffsqC0tN5sSafb1bNYLXOGtDHU0pNPV9cD2CudNoS2P-30l-QCncnAp6hI6GPyAGXJ_kmr9vGZDyTLNtT6tZdQBbSr8PVaIilAJSKpJ_q6qaiIsRE3BQISYKb0N7Sn_hGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
گل‌های دیدار امشب دو تیم هلند
🆚
ژاپن در هفته اول رقابت های داغ و جذاب جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23549" target="_blank">📅 23:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23547">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392bb7bb0d.mp4?token=TU0WzhiVoNoKH5boK7IeqBx-TeI4bAo3b0Wwq_g9g4pQnl7VLTM2pnpVCQ6ozc8P_Ppg3duYnQx17D0POitoYpqeyE-IY4QI2nAfhPnS15lF9r65lx1xwKwryytOr0Ok_59NW_zCk6q3hrrPJJ1AdToyR8XDTwZwFU2c5VPLoLYCuN_mIydQWUZoWWAVJGYZEjK1lH3prPG1MZYC0RzvlMSV_OmuWowd-c8XiEOFKjlB3dmbXJfCTIAh6GTgthvb8Twr9_Ti2feVP4GAxSKSPXetk2oNFVowezRvs1V5cQNuk8llUOhTE4zIinRHkNPmm28lATRCv75BB4WVRXoV74VuHtOP9qAhHIw5MYBWcsBzoZ4VZRotNekUk1rhgJb_b3LgF6vatC7vNKML6brn2aetAdvLH05is_Cs4m2WzmzxVW9M7Y35R29jPidyY37spTnm3H-CmYsQXZNv0SJLU2ps1jmwQiO-WKpqMsbvb2jFCxtiZrijkbA56yDQFq-crXDMm7AWaaWcM7L8BPuMfzgLZR1SVA_QfmL384n2nnSQ3Z5LaycRJrL6r4YQgk5bEPSc431F1EXblJteHo0AJbWL5m-hv8sdzxMmJaQB2c_OwYqV1uniVp20Wyrx0MuxbBp-wQmPflFHe8ypbtEyL8822MjE3oKKs07Mr9Y3qzI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392bb7bb0d.mp4?token=TU0WzhiVoNoKH5boK7IeqBx-TeI4bAo3b0Wwq_g9g4pQnl7VLTM2pnpVCQ6ozc8P_Ppg3duYnQx17D0POitoYpqeyE-IY4QI2nAfhPnS15lF9r65lx1xwKwryytOr0Ok_59NW_zCk6q3hrrPJJ1AdToyR8XDTwZwFU2c5VPLoLYCuN_mIydQWUZoWWAVJGYZEjK1lH3prPG1MZYC0RzvlMSV_OmuWowd-c8XiEOFKjlB3dmbXJfCTIAh6GTgthvb8Twr9_Ti2feVP4GAxSKSPXetk2oNFVowezRvs1V5cQNuk8llUOhTE4zIinRHkNPmm28lATRCv75BB4WVRXoV74VuHtOP9qAhHIw5MYBWcsBzoZ4VZRotNekUk1rhgJb_b3LgF6vatC7vNKML6brn2aetAdvLH05is_Cs4m2WzmzxVW9M7Y35R29jPidyY37spTnm3H-CmYsQXZNv0SJLU2ps1jmwQiO-WKpqMsbvb2jFCxtiZrijkbA56yDQFq-crXDMm7AWaaWcM7L8BPuMfzgLZR1SVA_QfmL384n2nnSQ3Z5LaycRJrL6r4YQgk5bEPSc431F1EXblJteHo0AJbWL5m-hv8sdzxMmJaQB2c_OwYqV1uniVp20Wyrx0MuxbBp-wQmPflFHe8ypbtEyL8822MjE3oKKs07Mr9Y3qzI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ماجرای شیر نگه داری علی اکبری قهرمان بوکس چهان در خونه از زبان خودش در گفتگو با ابوطالب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23547" target="_blank">📅 23:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23546">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d02367735.mp4?token=IX1yoDIfM_YcD_LtMfXuHjlxU0zfoUZxLA8g2XdvBjUbUpHG44ukclwKQWj5ckBmxbyRFvYULHymI9sLIToYYIsoPIxQaiIVKqJxzQvocV60nG461yQv5cZPNBVQwkj3oLrc8PuvKWL3gmA7Mwg7lfAX5K9riyeEjLF0hPvKKBH06XEn-_gnqkKC6DakE7ppbrhKzg0xP8G6mC21LURdByisXZLpcM5BliWCSI9Q4MevW8Tki18qCo3leqv2tVT4flMTZAvW1TcbQBNaXDEpbZGvfvbmlvE2JXlRV81EsXzV3t0IDzp2fQGE6CeSaMnRh_fEbyo6LwqYOvvgiADPcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d02367735.mp4?token=IX1yoDIfM_YcD_LtMfXuHjlxU0zfoUZxLA8g2XdvBjUbUpHG44ukclwKQWj5ckBmxbyRFvYULHymI9sLIToYYIsoPIxQaiIVKqJxzQvocV60nG461yQv5cZPNBVQwkj3oLrc8PuvKWL3gmA7Mwg7lfAX5K9riyeEjLF0hPvKKBH06XEn-_gnqkKC6DakE7ppbrhKzg0xP8G6mC21LURdByisXZLpcM5BliWCSI9Q4MevW8Tki18qCo3leqv2tVT4flMTZAvW1TcbQBNaXDEpbZGvfvbmlvE2JXlRV81EsXzV3t0IDzp2fQGE6CeSaMnRh_fEbyo6LwqYOvvgiADPcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
وزینیا دروازه‌بان 40 ساله تیم کیپ‌ورد، قبل از بازی اسپانیا و کیپ‌ورد فقط 50 هزار دنبال‌کننده در اینستاگرام داشت و بعد از درخشش در این دیدار و انتخاب بعنوان بهترین بازیکن زمین؛ تنها چند دقیقه پس از سوت‌پایان بازی، آمار دنبال‌کنندگان او سر به فلک‌کشیده و به نزدیک دومیلیون نفر رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23546" target="_blank">📅 22:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23545">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoUdT2fV8sCQJ2JxQACFxbnlV6JO-Xpw_GF494niNxUx6CXTS0KXbTaNPaZO7BFOCYOJ5glcwkH-xClXLfCRaF6M3UD3joV_RtM5cr4A7tjq6y55efMqKQtP87kQG-B0O7t3cNQXzvKkJrs8O5qczPKwVo3GiMg6NVgE6X5CgNPshXzZr0sPFCrTtYZgjfLwClvUmL4a3S2uhRrId4yWhLNJ9k_Gz41o38oFkOo2Cibiero5RPltP2gz1zP8_3MQU3XxLUj_J5JZrEpzfWjMCCRWnfYN3tYjOTk3tK4-kxzt5yYmT9vwsnOC-3Qxf1H44VvfJigTrK0EQNuujV5Tnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دریک رپر معروف کانادایی یک میلیون دلار روی قهرمانی آرسنال تو چمپیونزلیگ شرط‌بندی کرده.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23545" target="_blank">📅 22:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23544">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgHRI6m8Q1vFR-2ziPykNBxMTRWfr7FsFLjAS1BxkcTI9KN7EOI-2CzDOw1KQaCb6aozPU7f3eDXdV7KG0o92rAhN7Vmw_ftyyUHupJh2zEA7q2wNysEcLLWOZHPPj4GDhy6ViHphAhoGG9k_PoiRP57u1m32QLUv38S3JFRZQFGzpe-Q2cBNXfpnV_fEaeLErPkTCU0BPzuiZx3XDbzFXKz3bmrEgQ0QQfSOb6NfowTrSTiPa11n7avx1qWgRvWnOLXFscQNNxmdO_bsOPq_oWySytPLdSHvO-dArwVtvacGQ7zzTvHuM1ko_XBdn8cc3tpIhI0zesCt9BqvUfyIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
جلسه‌نماینده کسری طاهری با دوعضو هیات مدیره باشگاه پرسپولیس دقایقی‌قبل به پایان رسید؛ ایجنت طاهری به باشگاه پرسپولیس رقم مدنظر این بازیکن روبرای عقدقراردادی ‌چهار ساله اعلام کرده و منتظر پاسخ‌نهایی مدیران این تیمه. جلسه با تاجرنیا حدود دو ساعت دیگه درسعادت‌اباد…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23544" target="_blank">📅 21:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23543">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_wTO64MpQ0lD6obtc9YsNYYETs4dprbodT95Pp5mkrkxzJ2912-IC7TtIbo4LjiEmZ1z53Eb5jl_5WYeYZPs7zURlu5_w_cVP92ltcJ9V7-zEEjjr9mlj4dV-ZCCUnB70orrmCYMpf_b4Rs1Li54Xng4eau10UES4A7EH9fOqsbtPL3VY9cLkTgSQ3N4LZfDfkdmqkF9qJ8U0WuJohA0UtlDhUTU1YdhnGzfeVs60EGFv1AtwvtbEQRSosrdwuB2koLGwIFFZp3SlaVKHW9Tb4V-SqXEchvejwCS9GS2o74RY3HYpgjiiT9pUlL5l7_9DE49pk0ZOPFHU4rUjcATw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی 2026|توقف لاروخای پر ستاره مقابل کیپ ورد در شب درخشش خیره کننده و استثنایی دروازه بان 40 ساله این تیم گمنام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23543" target="_blank">📅 21:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23542">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCs5Us_dpq56nd1NyNW2wmwlpUeiQB7VAPi9sNbg8tj0s3OoGNZExYLnqQ-t9LL8r8i5gRjzOvz-G7SvrwBaeqJBER1X_may_mMaxer8IPNaZzdhgu_n4GUlQ_rmGIJUO7Jb5EL09ZnVnaRA5KfsAye6HBUP7EHjrL_hi1UN32bs2ddGeCrjJDCAcMIt_NHDYwNZ5D_9qp1oCq5ieWqsqSc6l3RunCqddpVGOY4EvDzzWEvdyd3B9gxlq4JaFdkm8dwoTmdS9QhSuMNxhcAnJq8DrLa9f2d5lx2LUUSHn5pP6gc0pom-Hp-6htwn3qVFWTKakrqPgbde1-5n-S5zwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی 2026|توقف لاروخای پر ستاره مقابل کیپ ورد در شب درخشش خیره کننده و استثنایی دروازه بان 40 ساله این تیم گمنام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23542" target="_blank">📅 21:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23541">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIP-0AR3uSJrmBVDoRKJB8xEr0oj4yxXlwsrEW-n7JYvwiDlK5CzHpDdru0ZE_6xWZrQjdliXablr1jPnxr5cvu3QBmLjrwwz7jEM55lI4B8-yN_souyffo83I_zuFHE1inO2VAZisOMJDqB6Yl9pQi85CVWNfgBzlhYifgtghaoC8WcqAUJUfZWQJOan3euf4vLJ8jZnVZM5rrmE_HiSyTZgHuQsAZJHtO0Lrsi0JFX69UB59496d_FAv9dksFG2T-PJ-nfSz6n48o0FFmu6RoDcE0vV7znZCSjhZo18m5jHnvhLAlUnlgqsY6Upr0692T20SEiciayBN-ct9FpSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درو‌ازه‌بان کیپ ورد در نیمه‌اول دیدار با اسپانیا 7 سیو موفق داشت و مانع باز شدن دروازه‌ اش شد 40 سالشه و ارزشش تو مارکت تنها 50 هزار دلاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23541" target="_blank">📅 21:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23540">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAhbmBQ_2aaI-2gNm5v973QnRpcqDBaEqh52IGe5Flj2SRJ9D-j2zTo6HMBC5s5fijmMMbnR-CmxSeNVpdpWoiwLQt6Eiyy7D-sVhy8XYSr49djCW1Abc7NVx9BlHSyzHV8f2gmeteG7n5nILFf6n6RttqHYT5uod6QNk05zexVAeqERR4Vnm6bGDKUhSScmUyB_tnti_CLXAYQ_rwPQy4Rgv_k5y1qe7rQLEgz9JMij_0EEoSFTVXbWCiDnoVYygVGFHIC79WxQLWyBcezzOKSlgPDf_XjDiCDIuF1OsHDkCL7ztU5MiCqKsAUqRVawERACJ_MewFSq8_33wya84g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
برنامه‌دیدارهای هفته‌دوم و سوم تیم ملی والیبال ایران در لیگ ملت‌های والیبال؛ هفته اول تموم شد که یک برد و سه باخت برای شاگردان پیاتزا حاصل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23540" target="_blank">📅 21:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23539">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAqX_Ump9UWUELoxZogciAkbuOA68kP85RSl4Vpv1OmUUlTlEKLzlLzXzMZ4khsCD9Vg4lkvOqSSZ48lAbUcKl4lQnOL74NwH3WCBZcaHDwYwpQUSg3v-dvqsc_0UKo1nzHkz1T47yp6yYZQ6mHyQtXcJZFcgYPQ_sI2XAXr50ttKrNxNEfDN9z1Zt1BwNZyrR7i8ue-sDXYo_ugGr_76UKZjYMBBrDeNG9BWxEDkeQQ3Q0IdUPQhyIBD_vlaGPZxSSTKpAb2W4LwUEZzKHbRGVBTECJcvIBIqkqgJiOVXFgF-f8YIUIS_Mrhz81YskFJVegZ7KQQZwrW9vNn_f14A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ویدیویی جالب و متفاوت‌از خرید مارک کوکوریا مدافع تیم جدید رئال مادرید توسط فلورنتینو پرز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23539" target="_blank">📅 21:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23538">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnapp | اسنپ</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMIOkGpkfjeiBwWtCOG7p5hwsG_52Nh2rshGjJDIwO4shwJi5B0ol_SkKhtgiaddL0iPdkdzdZ1zNQFN7oo5DiukuM8Xg_co9eNgz5jUiAIyzVCryn1XS398PEjhY4g-Q4ZVKUx3YXFzkdf2svnEsWAV-P_jFIVBRt9FeWn11p4XzL8rbwDOjRrg8Amjj8oKKI6Sn1AVUsajLRtfHPolfsk7mUR7rlNRArQm980I1fAkUm9nhcA6MMLs60e16hYXYohSq9jii5wTR5yvBDzEimCxaImeI3XRM3o5GqP_5ZX375VBhVIArxRWLbiby3wULTuCgF5S58iwNvwlHi8qzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥳
چیزی به شروع بازی
ایران - نیوزلند
نمونده.
🇮🇷
⚽️
🇳🇿
⭐️
با پیش‌بینی این بازی، هم
۲ برابر امتیاز
می‌گیری و هم وارد قرعه‌کشی
Apple Watch 11
می‌شی.
⌚️
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
روی
«
لینک
»
بزن!
@Snappofficial
🏆</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/23538" target="_blank">📅 21:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23537">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhhL3pqn5rNxV_qU4Avfg4qBaUetnNrtYNngKgL-lwgPKst18FDYq8zSaQ3nrVI8pi1cK2gBRqw1QDUQyvxBVC4bqBg97-8_VW7Zv90rLzrJbZ5SPzTmSXlHpqAxjld7_tH_PaIeUY-YbjlbVXumAwYTji1ODLqcknm0Ce9klyjofR2XjSpgbOgvGGkhrvq3Ibj_DD-kxaXPDV32S1S969S1QS8S35nzgo9CB_MmgzcbtgxfunV9El_v58pE_r1LMaSI2gGv-MkoujsTBl6BgxWqXHvuyqrFx2B5lnsi86CYMjIyDi6SZJlurZ7TITKTg_24AxHQCm5tT4hg-JPDXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی رسانه‌پرشیانا؛
فرهاد مجیدی سرمربی سابق استقلال پیشنهادی دو ساله از الغرافه قطر دریافت کرده و در حال برسی این آفره. احتمال اینکه گابریل پین به کادرش اضافه شود نیز زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23537" target="_blank">📅 20:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23536">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zw9qe-KhXe6eMHgxNvt0qAA6KqlHmZCgZ30RLRWh9FPFmigMMXXR7tGxlkTK96s0wtJfjXj5JsSk91cxx14qhii7mjXaPyu-yuL931bGovQnHz92nItI7NVsrDdB1VNc9dQHptqbSORNvikPNWirYfX8yAwagRnQ6mYSPkWRzCbkhhcbrlkAzOwUDEEKCEwB-khXtm1KTfdrelrklc6U4rSjF1NL62Rrh9K7OtmoT6YgusU6Kb3ix-oxUDM9wnk9nwvsahWDb1OhWMpK1qoUzoTqy7RpJy1ovCQakSNFd4DKSHZ67GmpxClgxT4sG_nR0evc6BSPxGUhF_-2LiG0lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ از آغاز کار ماتادورها در جام‌جهانی تا دوئل تماشایی یاران دیبروینه و صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23536" target="_blank">📅 20:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23535">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDgSSyAW7aP_rhJ8ootPTQoONcP1Cmzltx0n6Vqi0PXR-2tutU8dQ6Ptc4Oca6pLIeGb-qkn4UXffwgBN1wCpYoFpnZ7B6qZ8YLRS67RLvR1bA0gfrSVFUuEno8reb55pY2vfPWtp7E9J8zsDafA8yGp3pnyrhcZ4y-QrljMCmocrL544KcgN27cZVF5Jrs4m3JmOmALNK2qfcRMbvZtPDFLgQUHfEn_lSXQ2e0yFMbcmph7LUInERS02dkzZVbRlgNZt2-z95t8JQWc6DFd526knk7eCH1W0-ro0obpF8q2EPNAX8Zfh6YSvltsrqRZma7VH_URn4tWxT5A8Cwe_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نتایج‌اولین‌دیدارهای ایران در ادوار مختلف جام جهانی به‌بهانه‌دیدار بامداد فردا با تیم ملی نیوزیلند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23535" target="_blank">📅 20:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23534">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a3e86a106.mp4?token=SYOWOAYujvi8-nA1K-td73IFYytjWU4uK-DQjSPSKNdwSoG_wi0twhtk1ig1fL16LTGnkCQXBuqHO69RQVTDm4gaB2cJdmkKHhGkK8geWpvLNm1ygSMTpnTU84V7sw2IePiENNEW6ft_AXmOneWmd82IQHK_CGc7GiypUJjrRahl9tWHt3XoafoVzlSOfDuXAgFXveZGO11bPjPEoFvfcsFFz0BaFkNdJfuy6YeA-I5eJOzYhDvbdddMBwh7KGXDKCR3WOSaXBf57Wwovu5yqf1NFxlXXR68vAJGCoEZcWZ4zxDRIFw6qWSMdw9RI01Lb_bqaxyHJ2Hrf87rszFAJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a3e86a106.mp4?token=SYOWOAYujvi8-nA1K-td73IFYytjWU4uK-DQjSPSKNdwSoG_wi0twhtk1ig1fL16LTGnkCQXBuqHO69RQVTDm4gaB2cJdmkKHhGkK8geWpvLNm1ygSMTpnTU84V7sw2IePiENNEW6ft_AXmOneWmd82IQHK_CGc7GiypUJjrRahl9tWHt3XoafoVzlSOfDuXAgFXveZGO11bPjPEoFvfcsFFz0BaFkNdJfuy6YeA-I5eJOzYhDvbdddMBwh7KGXDKCR3WOSaXBf57Wwovu5yqf1NFxlXXR68vAJGCoEZcWZ4zxDRIFw6qWSMdw9RI01Lb_bqaxyHJ2Hrf87rszFAJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
بعداز پائولو دیبالا؛ دین‌هویسن دفاع رئال مادرید هم درویژه برنامه‌عادل‌فردوسی‌پور حضور پیدا کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23534" target="_blank">📅 20:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23533">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9uqUSo2qJ0lhTydBSvgYKeuZYeHzmkuirJlOTony3xgfajpMGa9IKD0cEgjlVuZUumTJsDieeg6PxJsP4YRnLxt4v2zgTZA5QL9PDWnIOhu7nzx2nKTECUU834Ry8_zrdHPyR0EcU6uwqtTgYKJ_pHHuGVbEKGLeMJh2V4JG4S_S-wb4Cnkan-gUoUuIbzN8jfIgDI7ynScLEVvn53nTpYtA_yf8vjWRr9dXlwkXU4wnhQr_6c1DUyf1dQIPQZVtZV3yY5z5H6JkGxpKEDwbFD2UnfpF64ljq19rHV7UmXgzYWJfDgNFl_lFQgIP_MiwA_UI4ORXPkjBEAl3t0ZZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عادل فردوسی‌پور: مشکل‌پرداخت مطالبات یاسر آسانی توسط مدیریت باشگاه استقلال برطرف شده و طبق اطلاعات دریافتی ما این بازیکن فصل اینده‌نیز با پیراهن استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23533" target="_blank">📅 19:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23532">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1O7tjZgrXFwWDigeA4FlmhdMceiGw_J249v6daFBmqmeXpOgqi_psNjRLXzjoLWst08RQ6iADgXzxbCD1noQ0rgwX-Ngff3fb1VmKFRuSb4slxnn4s3mh4znvN3IHenb_03neH7NrNojEAc8w9X6DXf6XPmjlcxfdw0kPFC5mLQI3YyIPdZEOC1hePgmtjudhYZR2ci89cUsC1fFFr6VweQeaxoxkgmyTUacPIyk5QmgEeNCVNVQRPq34dzOyMsV3Vs1bu5GKsm5xXyK0gtAsSF35XHJgEZejBdY4qFDgdd9QLVu8sZJFzGM5W7OBbZwT2lgVt5YWh1394ybCsMnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رفقای‌گل‌لطفا تو این نظرسنجی که تو کانال دوم گذاشتیم شرکت کنید. اگرم دوست داشتید اونور هم داشته باشید محتوای جذابی خواهیم گذاشت.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23532" target="_blank">📅 19:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23531">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0hHFE1kUk8jln_i95elG8ZUJhl-8_24J4oOwwfYRp1nXK5uMY6PO-zOrhAh0YiYwRkGmVwflGwpAmGO0LsfQGWkmgr04fAhM0Fk_SafJRMx8p4YAbJ3SJrRxYcT5SE8zeUtoHZra3ibUTvoeQuH7IB8z_iSuYTm4KTW8LBaVDTmB9Jqp4fuV_U5JD9bga4-nZHpBuZXe-SKC35UYY8-RF-7cErI0zJajbTchh-gfUZAZr3U46XOLwSPZGpz-ylvhhKFxgnp8d7-ZGhjtx_xooMrvSdxpWFa_C1qjy5Xrz6kGUVPVTIo0nSOhZmy231wd0fy0HkFkFmdM4SG_vEXpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد جواد حسین‌نژاد، محمدقربانی،احمد نوراللهی، کسری طاهری، رضا غندی پور، مهدی قایدی محمد محبی، محمد مهدی محبی بازیکنانین‌که‌احتمال به لیگ برتر برگردن بسیار زیاده. اللهیار صیادمنش هم آفر خوبی از اروپا نگیره احتمال بازگشت…</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23531" target="_blank">📅 19:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23530">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23b2efb67a.mp4?token=aAD2TyoXiyv3qGC5kGhL3iKwnVat2I6D9B5AmgiWMlmRCMoy_JYmXcuoSJpJG4qVXh5ozbDGNKyLP8q7iCSbBxEHKVLS8xya1eimskYbPfJTCFOz3dmvlDvlCP0NCCG7mW_rhiHgQYtSGqQ4G2T3gOTs5480y3AlUt-KjeoPMpidUmEe8ucSvKftZ6yxG6abizYVfAMJ3-_ePO-wEVG2bBFuyJ8mih0tY9ifVJ6W2xWuvQTAbuwdJ-DX-nh7VxFwEFuaiCqCsj7lGWRt-hL_IV0vCtCNYmumClkPYul1FmIyreuf9KH8jfM_CX-zIafQDdXwZCMSYlR1LolQ2nLOdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23b2efb67a.mp4?token=aAD2TyoXiyv3qGC5kGhL3iKwnVat2I6D9B5AmgiWMlmRCMoy_JYmXcuoSJpJG4qVXh5ozbDGNKyLP8q7iCSbBxEHKVLS8xya1eimskYbPfJTCFOz3dmvlDvlCP0NCCG7mW_rhiHgQYtSGqQ4G2T3gOTs5480y3AlUt-KjeoPMpidUmEe8ucSvKftZ6yxG6abizYVfAMJ3-_ePO-wEVG2bBFuyJ8mih0tY9ifVJ6W2xWuvQTAbuwdJ-DX-nh7VxFwEFuaiCqCsj7lGWRt-hL_IV0vCtCNYmumClkPYul1FmIyreuf9KH8jfM_CX-zIafQDdXwZCMSYlR1LolQ2nLOdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی جالب و متفاوت‌از خرید مارک کوکوریا مدافع تیم جدید رئال مادرید توسط فلورنتینو پرز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23530" target="_blank">📅 19:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23529">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBQPAbhoO9rj_vmfkEdBC8YDOu3VFqVwtKG4vKYSXeB0hHH6oLDYwHkeSmim_NgO5OLaO0c040BdtzRRhmY42x7FvDksigYj_8yd9hWAvOV0fW_uz1jwuntP39dFYx3WSQjORFcxtmLIEhaVzZSjNWn7sVe4K59dDtOomyksoKN6RbUdN3zAbGDLDrCC1OscE2DO2BvACiEQjVPK08Rp80HEyi9BdJPCTVtKg4P9l-Px_vMKK8EbRpTFWV9imv_gmPkFdRuHauUCQDNtfflqjI2rAU5FZSkCCIr-spojesxpPB_9FF_LS35E6S8X1gQS7LnKMA2c_U9sRSfIvWCo-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
تایید شد...باتاخیر چندروزه باشگاه استقلال امروز صبح مطالبات معوقه یاسر آسانی رو پرداخت کرد تا مشکلی برای ادامه فعالیت ستاره آلبانیایی ها آبی پوشان پایتخت برای فصل آینده بوجود نیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23529" target="_blank">📅 19:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23528">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JshTttFQmJ7pX4fzfXpXyIeFwNP3vDDweqv-KW9DpUv5SVq39k7KRqRxvFmSIDShIKHacElfoaNsBsu3gykU-_pzVUBjcEjN_6qGdBX6NzpGNW_90a5OoW9yOztaNxMmjEUCj_IEtvgjSlfsTDOVKN77L9hjA-yk_-nibHvzEcMO-SUI2qi3VafYzxw4cu7Ih0YjXxt927SLBCW9DT3KeQWMw02ozH46dzJ96nNcPYm1ofSD0kQN9k0GHClf5-O52U6cf9cmYay7J4ZC8uDDA7ua9RR3jTYq4cP9cNE0GuYpbDcK8yUem5uI7byx6Ev9k2ZycRDJQY5uaXoaABgF4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
بدن فوق العاده کریس رونالدو در سن 41 سالگی و آماده برای رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23528" target="_blank">📅 18:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23527">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fjjhpwmh14SkTd3osXPgj2edro_W-OhzJxqzGPQCkcnWFja7hYztVNyFr1uKGoJUcTWaCPgJy2KbLTF8wT_IdGil-Nunsh0sPl8mleL7kmopNOnDiyiyWHUtSiAapxdarY9IVL0wpZeNtTu2yimHDetBAkznCG0nb4fBe6XOAECSWkS4LPb-o7DQ4gyDHzQA6mL-S855vZRk5jGQJIO-hTsPmlgc7BMT5-KVEXUNnGM_2omELJ5zPVm340O1eXBIWcIOXLLkzC_NxnBwcSmFuCacDgCFBvKlbPeP3-AMmV-NbK4kxjtVo1oEHy7UnZSphBu-GsP4iZLcQjXkLKfWIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
#تکمیلی؛ال‌ناسیونال: یوشکو گواردیول مدافع کروات 24 ساله منچستر سیتی با رئال مادرید به‌توافق شخصی دست یافته و حالا توافق نهایی بین دو باشگاه رئال مادرید و سیتی باقی مونده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23527" target="_blank">📅 18:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23526">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2d57c883d.mp4?token=vjYNwMJNAfe6yUy5Hocy-UvBSvWEm1gyRqUK3aDImC84Kb7F9bHCUCsxZ6XOUOQiFKbRvZYooJNQoGJt794l6VY6YY2PmIgzYiLvAX3EB_HykpWmK0uHnOTmlT_vrgTVTEyA9iteIjlv2VaODQ6xATZPNvC-vhDYGSife7UKM1so1CvLFjnPz0MJD6sv2Fbg4pMhAarwyB0rLuwPK56gDJ9EmlR6ClGuZ6OdW-0VV26lwQsm7yYaDlikEfLlQUYs7nLXYfObSOjbiAl9ZGQCTOw-2SZSVIxT_JdhctCJg0aBKtfd7w4Pq84xOdpNo_ZC_5ZkHLn4nE2DE2MYwWTmVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2d57c883d.mp4?token=vjYNwMJNAfe6yUy5Hocy-UvBSvWEm1gyRqUK3aDImC84Kb7F9bHCUCsxZ6XOUOQiFKbRvZYooJNQoGJt794l6VY6YY2PmIgzYiLvAX3EB_HykpWmK0uHnOTmlT_vrgTVTEyA9iteIjlv2VaODQ6xATZPNvC-vhDYGSife7UKM1so1CvLFjnPz0MJD6sv2Fbg4pMhAarwyB0rLuwPK56gDJ9EmlR6ClGuZ6OdW-0VV26lwQsm7yYaDlikEfLlQUYs7nLXYfObSOjbiAl9ZGQCTOw-2SZSVIxT_JdhctCJg0aBKtfd7w4Pq84xOdpNo_ZC_5ZkHLn4nE2DE2MYwWTmVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
برادر از 4 سال‌پیش‌تاالان‌داره مینویسه؛ سرمربی تیم‌ملی‌ژاپن با همون‌استایل خاصش همچنان میتازد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23526" target="_blank">📅 18:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23525">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoG9xgt1EUb0gZwIdJnyiPX3graPJfSj55RTTaMfw0d7zJheG74c50GTFW0Pidn2JBAAlwC-aJkNbs6fGlNmJ5PLNtjmRaKdmwQQCCjZZcez4Xtcw-xfrhSUOSggr2RPWDeUtBWbeCi0esD6OVLD8jSy0WKiNkXgFWzZ7s23shc_Tfb_E07ZmtgjSfLBO7o9XP4u2D6fZitSa4BfVAc2T8IyDCJ8hd_gwcODijsYOWVmFJXPYHssXmLtBJyGbjlJOVfKY1dED9BhEntfvd5rFTRoGyr2qiZgDJpc2l6aF6XsrsfhWxsFEYudHaFezbYZ3jFNZwCKKuVPcqXGQ7GVbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بعداز پائولو دیبالا؛ دین‌هویسن دفاع رئال مادرید هم درویژه برنامه‌عادل‌فردوسی‌پور حضور پیدا کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23525" target="_blank">📅 18:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23524">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bca14044.mp4?token=KybI8Z_09tvpyeGevAVhRRPwoq2KdFPbW8lWMbK2p8ADwYvW7Vsu0OzNRieLJR5ghkqT5JCTLsADYP0y-5pKrQvpCEglKae9INoeOuJNJ28W0IRNFipnlRK9TyK_WSB--8DYNDLip-SPM4urnuUS9pxOX7CWNY1rELNoXxjiq5-fcBMBcVituMsFsiIbtx8DJ8B8PgDWN9nz4wiLItI6BitWK2M_Cpv0vF3cVuRLZ33os90MgqIVnfSZsv4PFZbHA0b8VGPyUHGQ5anw4zXRedAiKCRwPy3ScAzujTnJ0f07eTAjpMonFLhLDwzFowZ-oFQyd8zcU1xirlT6fM6sEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bca14044.mp4?token=KybI8Z_09tvpyeGevAVhRRPwoq2KdFPbW8lWMbK2p8ADwYvW7Vsu0OzNRieLJR5ghkqT5JCTLsADYP0y-5pKrQvpCEglKae9INoeOuJNJ28W0IRNFipnlRK9TyK_WSB--8DYNDLip-SPM4urnuUS9pxOX7CWNY1rELNoXxjiq5-fcBMBcVituMsFsiIbtx8DJ8B8PgDWN9nz4wiLItI6BitWK2M_Cpv0vF3cVuRLZ33os90MgqIVnfSZsv4PFZbHA0b8VGPyUHGQ5anw4zXRedAiKCRwPy3ScAzujTnJ0f07eTAjpMonFLhLDwzFowZ-oFQyd8zcU1xirlT6fM6sEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇹🇷
آردا گولر ستاره تیم ملی ترکیه پیش از آغاز بازی با استرالیا خطاب‌به‌هم‌تیمی‌هاش: یالا ما ازشون قویتریم؛ بیاید این رو از دقیقه 1 بهشون ثابت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23524" target="_blank">📅 17:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23523">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQ-7sxXkv5iM_bG8JuRbNON2LpHlB2Q9cNd8loQyBvWqMcqc9Q5gQB-_MEDiYDjqdXQ7ZKUeDel0PcE6LM0HONRdylq6D-fms3fYEXG8ZFVPSYzvE1oWAc9FUSQjeGOXEdgxL1iWQx5yJ1nbgiLl-gbs1M7ZDpcwJbMhAMXAxBpXOMH8ln1aicCKPZwxXf5FM0IQAlzbPOdw7Va5VOt_dbng3Nxf-ftFZLn8liHUSpo505OB8bFZfKhv5u2bwIVnk4cdgCUnMIYems4qLaRxxQQbdNVJjJitGgLH4Db-y_AfntMHmx1b1Bc4GqfbPinaeGIEvx1-Zv63KmW_gt_ljg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23523" target="_blank">📅 17:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23522">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZREqpvzCsa6dzvw0OODWMpW7Nct6XFCumH9MQt3gRAjaKIx12LQkfZNt26ST3I6Ltioz7gA394UJGND1IP8at-GHqMblBlYvJ28FuwbK1CMGA4XTUvAj4tUWzcF_Mmi_uUjxSifc3JrQV3Ttqs6Yg7hRhCIQJdS40eNJO5EbG307TbyH5_S9q_jGM9uf0VTfOcvYTng39rQHCjY2CGIuIFz7qT9SXygKRYGj0bQkyGcNsFFpKWb7hhT_a4p92cBzOocmQxiTgnvXE96Bp6uU4QSK8nrwlpEIwKwawe9RSA4G8t7SLjDpnXSeMssrNbGCe0cNvnlk4WM5jE6-r8-lww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23522" target="_blank">📅 17:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23521">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXqdVenlNl7zY6uGhaImiGa_od1UUZ_9YMWRQOQtIwhicyJdZDljhUSf8Ju57BDjPjOQucHwkVI9kcuL5pZb7AuzOUy4zs-gCVfXyVBX1MCc6l_SHISdZsf1-3Z4O3kj7JNTwIpmES78CbgpGTCvCVHTuie1o0K-GxnoK-XpKJHrIk2ul1jMZ9h3505Zs8FhhADlzhua-3S7IXoQ1IBur9apF7_d2RaqFKXqL29Luw2JMWd32GCU1bgCt493Td0ic0S4JfQWzJRLrjU8eSsRy_sV-7zhblPW2en6Ks_8CjIj_1ko12_tBSRQexzczS1-MINez_elHd8sSHsQ3TGXug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
گل‌های دیدار جذاب امشب دو تیم ملی آلمان
🆚
کوراسائو در هفته نخست رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23521" target="_blank">📅 17:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23520">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7870ebb64.mp4?token=Wm67PWwcK02YG9CumVbokLWRXJ0Pa66G9hJ-O4y4dvTueq74PGVGkiQeYkXpPzLY9_efxZ4ztz73Pw4BgI1I_jXyzEsLF_J6ELQCqfzMaU1hsDlqu0xciijbhPUFoXuvI0xdMXeY-erYB3oqjxMVTWwpPZHVXRO8rR7tGp8S-xABJDVoBFZ2QILUxufD9dVRO76-ymBXrhw522hN0tM2tGpoR_JDFjCN-9KrunwNHvYEI7K7-K8NfnajnTtsaLh7Sm3H2rpOzRD1m1NqUgHKhm4pt_6a3TT1D8x-I3EN6Yj-ymG607rEBD6NRkiUkiXKiGFFoFzLEZJoeexBE5xQ9SiMd5O7G1T0p7CwpYZwVbH8Ox1s7eo82NI5C1zAHNia1Jv6POFTAe3zo859SMb_9mdcHBcxK_jY9RWb07Apt7ISlew7POvkBQK60pFs2MLUgpXdR-Krhx7MAzchwMOkfcI6ZD6fJOt3IdetHEGTQlaRErdD8xhAU8k9WxH-lAldtow0ooAtoyj1o7CVHBFT_nk0oVGAiptOFRZCMSZC3cfq2hjKFr2hRlavffua6tuIJ5CI70ojVgaGNi-LaSoE7gYoDyqQyAZQhudDx5mJi24OH3d3IkXmOUEWM2F8sDY1Izh6vc26BU6l1J-XPgT2GE1vLIUYBmU3tZ6IRWrlEyk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7870ebb64.mp4?token=Wm67PWwcK02YG9CumVbokLWRXJ0Pa66G9hJ-O4y4dvTueq74PGVGkiQeYkXpPzLY9_efxZ4ztz73Pw4BgI1I_jXyzEsLF_J6ELQCqfzMaU1hsDlqu0xciijbhPUFoXuvI0xdMXeY-erYB3oqjxMVTWwpPZHVXRO8rR7tGp8S-xABJDVoBFZ2QILUxufD9dVRO76-ymBXrhw522hN0tM2tGpoR_JDFjCN-9KrunwNHvYEI7K7-K8NfnajnTtsaLh7Sm3H2rpOzRD1m1NqUgHKhm4pt_6a3TT1D8x-I3EN6Yj-ymG607rEBD6NRkiUkiXKiGFFoFzLEZJoeexBE5xQ9SiMd5O7G1T0p7CwpYZwVbH8Ox1s7eo82NI5C1zAHNia1Jv6POFTAe3zo859SMb_9mdcHBcxK_jY9RWb07Apt7ISlew7POvkBQK60pFs2MLUgpXdR-Krhx7MAzchwMOkfcI6ZD6fJOt3IdetHEGTQlaRErdD8xhAU8k9WxH-lAldtow0ooAtoyj1o7CVHBFT_nk0oVGAiptOFRZCMSZC3cfq2hjKFr2hRlavffua6tuIJ5CI70ojVgaGNi-LaSoE7gYoDyqQyAZQhudDx5mJi24OH3d3IkXmOUEWM2F8sDY1Izh6vc26BU6l1J-XPgT2GE1vLIUYBmU3tZ6IRWrlEyk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
پیش بینی 4 بازی امروز و بامداد فردا رقابت‌های جام جهانی؛ ببینیم چند تاش درست از آب درمیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23520" target="_blank">📅 17:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23519">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc271fde7.mp4?token=HEI3TP40gDjT-uM6T_6R5Xa4C3RY6wR4xQa3tG9NZDX9-5XSFnJiOsIUyaMmKXw72ZRiHRvfSxHH7wqXAoKgmeRL5QL-6rrJbRtIpIt5XyoJb-0RWbVHW3abCz223KcWlb5pyTSp7XK6tHCu_6HakL0zi986eiQsT4bmo3BNkKWZ7HvQI8WStfdCO5UCSJo_Caq2RMNNG4_nO1VGaMnWPIDC5s2ri5Urj1xJI-ZGFjbsg0nj9QGl2OWAmT2eX_2GJmYNVkTzdTm-lLhqceh57rDBxySXbUVkdSqjWSbiSY210wdvFDm7jLTIaObNuMizDkO6DLnuWfltbB0ue6QO_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc271fde7.mp4?token=HEI3TP40gDjT-uM6T_6R5Xa4C3RY6wR4xQa3tG9NZDX9-5XSFnJiOsIUyaMmKXw72ZRiHRvfSxHH7wqXAoKgmeRL5QL-6rrJbRtIpIt5XyoJb-0RWbVHW3abCz223KcWlb5pyTSp7XK6tHCu_6HakL0zi986eiQsT4bmo3BNkKWZ7HvQI8WStfdCO5UCSJo_Caq2RMNNG4_nO1VGaMnWPIDC5s2ri5Urj1xJI-ZGFjbsg0nj9QGl2OWAmT2eX_2GJmYNVkTzdTm-lLhqceh57rDBxySXbUVkdSqjWSbiSY210wdvFDm7jLTIaObNuMizDkO6DLnuWfltbB0ue6QO_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
تو نشست خبری شب گذشته ایران - نیوزیلند یه لحظه ارتباط مترجم با امیر قلعه نویی قطع میشه برگاش‌میریزه‌به‌مهدی‌طارمی میگه‌این داره چی میگه طارمی داره میمره از خنده‌فقط‌جلوخودش رو گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23519" target="_blank">📅 16:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23518">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9720dcdd27.mp4?token=dHZfgI--hd3Vj9JCj3jSkDn9sbO0oC78bDYZgz_XUvJEGb2chKn44q-a2ybYzI4udcM7psIt6Jr7UdwW9hjf-RRHKZnGamkUNa3figU1bJzN5imsqHRlnj6rAmLfwCMRYk9Iu9j_gaxkZ2OeIL1uLru8PfT43vurduWbTpDHPOjid00taJNp-_GABT_ih77tCrHCCTUAJhAf6g3H20kRciJ8pUkH1eq3Nt1U7EDgIRHSo2rwkMP9-clea8AyBFsmJ4S-sAzA6MVEbJHsgrGKYP4Uz07YBsjINCzNSSN2KCuZArua25BJM8FcxDMAlQI2kbKlomYr60tdPhdDq8DgQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9720dcdd27.mp4?token=dHZfgI--hd3Vj9JCj3jSkDn9sbO0oC78bDYZgz_XUvJEGb2chKn44q-a2ybYzI4udcM7psIt6Jr7UdwW9hjf-RRHKZnGamkUNa3figU1bJzN5imsqHRlnj6rAmLfwCMRYk9Iu9j_gaxkZ2OeIL1uLru8PfT43vurduWbTpDHPOjid00taJNp-_GABT_ih77tCrHCCTUAJhAf6g3H20kRciJ8pUkH1eq3Nt1U7EDgIRHSo2rwkMP9-clea8AyBFsmJ4S-sAzA6MVEbJHsgrGKYP4Uz07YBsjINCzNSSN2KCuZArua25BJM8FcxDMAlQI2kbKlomYr60tdPhdDq8DgQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روایت ژائو کانسلو ستاره32ساله تیم‌ملی پرتعال وباشگاه‌بارسلونا از تراژدی تلخ و سنگین زندگیش که در سال 2013 مادرش جونش رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23518" target="_blank">📅 16:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23517">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6VM098ze3tNujAW5zv0WKBJB7S2-hldTKqTv7cL1uZKSS0mGI69sdmK62T2KwEuwnBmaCAZMZPnGIOvpxV7r4yFKUeT2coWYWhVPDFXbHi5C4Jg1Dbbdq5883Yobtgnj9NDfXLOeq9IdLKXyV948skLZIuMDzY1__9ow8t1LR7QF53UFsusP_SWR27djlEO8OSqsIbcX5kgs99by_gv__9uCrPzpgXN0wGBl5yKYMdH4qO8Z8sLScjCVUTt8Zz-2jcKTTCUJy3YLfwHSmIoiV2BgMHR5QNhdycqUrJF6RlMpTy2_6GhEgbIe5yevW3zXmsNpSQ-j6FEkGmCsXik_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارک‌کوکوریابازیکن‌سابق‌چلسی‌ومحصول اکادمی بارسلونا به رئال پیوست؛ وضعیت باشگاه بارسلونا:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23517" target="_blank">📅 16:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23516">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSTh32xnkPSdENqmy6bFC1IE9IaQDQWtj3Whk_NkKp3Y4fShXWTl2rCVEk49yve3aEKTWBL4mnEnDGBSiTN15pdF43q2ZI41_j-mO8kZMSDhnu8kgD6tuv4JeN2e8eprP_tBMyn7ubbjT9hC4QGPydM9I5TE0BpxNn2E1s560TN1mZi9GIpsfivEo9msuJk0xXArTOFm8hfZOML6eSZ44_K1RQiFdxolHnJhSmKEsP_Lc6ZjhCaskJp9t7pYL01ZUGWuTgeNSsscvdDkbOCoVTqo4aRyudx-u5kxD7-ulmoVGxrnowJBcrUdFq1THAKsm9jsictA1Xk6dNmOWZkl2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی|توقف‌شاگردان کارلتو مقابل مراکشی‌ها درگام نخست؛ یاران حکیمی نشون دادند خیلی حرف‌ها برای گفتن در این جام جهانی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23516" target="_blank">📅 16:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23515">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4vZHzl1ky0sBQFnMcgFZKKDwUuUHrXtTwQDSNMN4ZTpIkXpHKTpo7aA0lxlgXRnBoUiG7mQXAHzlVyA4tVTQ8X01xnj4PbZO9wqGpW8vYLU7TCcGXRMAnQpUllddLoJHK-zCZgA6eHkpPWtrAx-it4IDS7muzxSrB5BHrvGURO0aZxj-LLiP7R7AwP6uT-0snpPpQevSnE8rMCKAOT9TwHTE9ijun0aGgh-eCWHdYmXzF5PsEGZePd5azb2BHAT5_2DHFaGDTC9aQqhB6t1MxcO3_hVUcpBnbLL2VijRCCI7nmIKmeG5uW_EoBRB8OEP2OemMn7_-Ykejg7hCJN_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23515" target="_blank">📅 16:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23514">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSwEy0NKLaVP-YMLBGhLUUo7NblIrEajfwHAjDRzyFUUKolUvue8qOooJVyEcv6VLy4nGj4oTkP7xA6ocGQM4IDgbiDl7ec0NAyA-HkQ_SvKRGNaHWlTLACi5__66_xii7kraF1jDNs2GpKYC9vfHeJufHLwp5sm1Oq9hdHEeiuFXGPUsbawOjj04kfeix4pSgTp1xxeBj0C3iUB5o1uZgJR6bYNd5jzLt0wiVbVzcKgBJv4apVLyHz31vqusDwczIdJiZOeuepL587xAOtSeh9v3QrI5v_7wV0TN7Rc9yJt5nSgxAPgrXOftvG0qTy2bopSD9JP21TIwXRwhbGyvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
اوسمار ویرا سرمربی پرسپولیس: بارها به مدیریت باشگاه گفتم‌که‌به‌قراردادم به این تیم پایبند هستم و به محض آروم شدن شرایط کشور به تهران برمیگردم. لیست بازیکنان‌مدنظرم‌رو‌به‌مدیریت‌دادم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23514" target="_blank">📅 16:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23513">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VC_p3oAN1MvukUYbYbm8nI6KppGUfOrtIVQHqgMMtkKKJod9-j8l8qV943foNyarkp8LgngOvXnnMrVJ-WENwgSIwXXnj7djSHBfWRL-OhrIRvDdVob5n38OY5XiHw79ThwjzTtYRRvqHUkMsAkYduiGOQGbEvR2Qw2N5WOANqNewFJFUczsBdLoL84-_uqDgb6cVqdp6PWc-utb6GqEceRvWFmWHVqwQ2uYZMiuaqFiplZR5cDoKGj0eqnE7w_gQcVF-WV-RQTdhQ1NbZ5iywS-9Q4R3EotWs4XqNwodYqS-Zs1HYw5MEBa5d-2Vz1mUdq8K5upAq6oWtpM4EoRFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دایانه تومازونی‌اعلام‌کرده به ازای هر گلی که برزیل توی جام جهانی بزنه، یه عکس کاملا برهنه از خودش میده بیرون و اگه برزیل قهرمان بشه، با همه بازیکنان تیم برزیل یه دور می‌خوابه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23513" target="_blank">📅 15:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23512">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6831beb90.mp4?token=oDnqJLjDtgUUY4pPR9fl5R_fVt1EfubiCNHYhZfl6gJSzU0MmSqepaobWHsM8jQGTdVz_nGvECYU9TlCpbtVGH82lRVio0NTmQI_crZtt0ZLh6MVPhKh_kL7bLqw5q-gVyfRv0n7Y5_GDFs4T-xNRifnaaeaYD0ip_jlbYphHci3hCMfmUjqf24N5-MvCakKo8or0QqLdZ6ICDKSUpjCspfenDbVPDEuvJiQGKxNLHHzgD0FI9JQ-WGNbdT7-pegu0ZfTd7LAFyXbDESdboAGp0ZRc1uSMAEAgbtGFzrwIm9pSW8ViN6za38k1TX9mlUh7BYHkAXNJ4S665XTGCDBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6831beb90.mp4?token=oDnqJLjDtgUUY4pPR9fl5R_fVt1EfubiCNHYhZfl6gJSzU0MmSqepaobWHsM8jQGTdVz_nGvECYU9TlCpbtVGH82lRVio0NTmQI_crZtt0ZLh6MVPhKh_kL7bLqw5q-gVyfRv0n7Y5_GDFs4T-xNRifnaaeaYD0ip_jlbYphHci3hCMfmUjqf24N5-MvCakKo8or0QqLdZ6ICDKSUpjCspfenDbVPDEuvJiQGKxNLHHzgD0FI9JQ-WGNbdT7-pegu0ZfTd7LAFyXbDESdboAGp0ZRc1uSMAEAgbtGFzrwIm9pSW8ViN6za38k1TX9mlUh7BYHkAXNJ4S665XTGCDBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
این بخش صحبت‌های ابوطالب در برنامه‌ دیشب درباره اظهارنظر رهبر کره شمالی که گفته بود عاشق لئو مسیه و دوست داره آرژانتین قهرمان شه عالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23512" target="_blank">📅 15:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23511">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea5e91b256.mp4?token=j3hOyFgSRlaKg8EZGHeGGVTs3SOW7HOTerBdijZQAX2XQCGWBFkJ1aZ4P2r8loRQr5CKlsaOsMuLcrscwOU5OEDFBaF4StUaaPxlUa2Uf-dBwmBLp8BhOjcd4MZHTZ3lxaw3FmiMO5TgRPYG228CfX4ZN0OZ6YnS3zLoF337i7UzmkKNc6vXU1yMh1koHk0eITsjGpItbpMzzhWheBZFSz6HVKsURV9iSzWOGEpYlv6ZG77B0eOAehX27axxeSx7pPJCqV5aO1TabU6Bmfx0Jhc2UULx_5YhPvuZXOi-1yG3byflNo4d7wzrhYtvkSJ9t7vjesyecfzxLi3qqjikyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea5e91b256.mp4?token=j3hOyFgSRlaKg8EZGHeGGVTs3SOW7HOTerBdijZQAX2XQCGWBFkJ1aZ4P2r8loRQr5CKlsaOsMuLcrscwOU5OEDFBaF4StUaaPxlUa2Uf-dBwmBLp8BhOjcd4MZHTZ3lxaw3FmiMO5TgRPYG228CfX4ZN0OZ6YnS3zLoF337i7UzmkKNc6vXU1yMh1koHk0eITsjGpItbpMzzhWheBZFSz6HVKsURV9iSzWOGEpYlv6ZG77B0eOAehX27axxeSx7pPJCqV5aO1TabU6Bmfx0Jhc2UULx_5YhPvuZXOi-1yG3byflNo4d7wzrhYtvkSJ9t7vjesyecfzxLi3qqjikyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
همسر کوکوریا مدافع‌چپ جدید تیم رئال مادرید هستن که در مصاحبه ای گفته سال‌ها رویای پیوستن شوهرش به رئال‌مادرید رو درسر داشته و حالا بسیار خوشحاله که این‌اتفاق مبارک براشون رخ داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23511" target="_blank">📅 15:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23510">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqUY9HcQ07hMs5J_eUE_y80CqYJY0YrJ_PNZoM0aAOxCFwZ29316W_eKsPS-GtE1__3foU_cyGhj6MeE4seHubNPFMAIJ19DrFVd5iMK6bYaNxVHrFfeBrQCXC6rEucWLZOF6HB5ma_kCMRrRmrTulJiBlG0JCdtF2WoobKbz-3UdKvmqVrAhsvYqm5NRsF5PCuCajU1-t3_oOV4eKJl5j0iCmW_CVeW6G05DHlchkWQINaqsg3Fvt4ewOwEau-IEGPrhc8cV3wZeZc_yCJ3PsiGZbtAV1DO5sQBDY9_S8HJhQ5wYyClKLGi-Kyw3igMwkeXY4M81bp0pQo6PkXxfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رتبه‌بندی‌شادترین‌کشورهای حاضر در جام جهانی ۲۰۲۶؛ مطابق معمول ایران اون پایین های لیسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23510" target="_blank">📅 15:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23509">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PR-j9NrCkDHbKDWQJvoA5LA8H2ZUZZqVymwzIAXSzR3kEiyqZa2T7Iugcn06ZYrClxC9qBvyuNaZp3zBgPGygKvRQ2mYb39jZGcloPTHgSP78prIE1i6L__ueL5k-kwX9eo6U3pE6WpzQ4YiHz1QSRlJTMDg22n273dZObsgHePqb3PNESQkQEPzkWF7ZYfN3m3-meGTKbn08MoFGCiPenxH_OPfwq8_TemZfWymNvruWD1gYvwzSCkHvBRx-J0xjYX6xb2XoOMJhi9cflml6mWJgTFaxu5QmlfwFll5N0JE-lh53JfVsrYV12D1ahl-dQsJuBaIlRgWwBQGrnCdTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ نیکو اشلوتربک مدافع ملی پوش 25 ساله بورسیا دورتموند آمادگی خود را برای عقد قرارداد پنج ساله باباشگاه رئال‌مادرید اعلام کرده و درصورت توافق دوباشگاه احتمال این انتقال زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23509" target="_blank">📅 15:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23508">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7ff7752d7.mp4?token=EUD5yajQRTHLOT1z_Ne7YryUMd9rB-kkdorTkEEFAYrBOPfsXf2sFz6fRafTBhVGBrvpBqYgmiZP425rKLH3qZ7M9-V717dN0X0oUjio5Xf84PHSMAfYK4u44ccZfyjupTVptzd6qMiihlRXinXQ_DSxDwsjL9hEcBPnPGKx1FhoD8S_2_qElZCSVDRq9BkYJDUD_01KlrfuZndJUHQe37NHrl8Jh2jQ4Q6-4URyqRlnUtIpmT2RZ9z2m3afq8P91SihAaJdRTg_Fwd1j96nao0_jRm1YdXAcmxnhjTqo1VkvdmCsw6E1jiDNBx34qoDc8-46hjnEapPp4_nwRgSuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7ff7752d7.mp4?token=EUD5yajQRTHLOT1z_Ne7YryUMd9rB-kkdorTkEEFAYrBOPfsXf2sFz6fRafTBhVGBrvpBqYgmiZP425rKLH3qZ7M9-V717dN0X0oUjio5Xf84PHSMAfYK4u44ccZfyjupTVptzd6qMiihlRXinXQ_DSxDwsjL9hEcBPnPGKx1FhoD8S_2_qElZCSVDRq9BkYJDUD_01KlrfuZndJUHQe37NHrl8Jh2jQ4Q6-4URyqRlnUtIpmT2RZ9z2m3afq8P91SihAaJdRTg_Fwd1j96nao0_jRm1YdXAcmxnhjTqo1VkvdmCsw6E1jiDNBx34qoDc8-46hjnEapPp4_nwRgSuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شیث‌رضایی درمصاحبه باابوطالب حسینی: همه روابطم باخانم‌هااسلامی بوده! دروغ تو کارم نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23508" target="_blank">📅 15:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23507">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0743550e2.mp4?token=jGHnFLLql1XgAKdw-1DTA2k8nZohc02VIFduVUaVVOML-9aS9FQZWaGCOFvmQ0Pxmc6f_5obBNmFZfN9GG495Hp6IlKUQPAynhKLKgDBUT1JOrA5QiV_wGoaAEF_L3UpDkWKR0dU8MIDx8QVhslvjSnkIhHPa9rsnLAvgl7Rm93uGROlIVnrt6i2VkG_ER2YA1ZAVt0xXadbKIZNgvI5ysPt0b9jsANf9eCcKoBHWD-KBywRtySbqRW-rsoTZWj83295Ngn_rl9V6-ozIbxrw47tuWZkJY7C84ZHN8TAoAxcBsrpmNbNwGKd-aCFLRtqnsLC3-kigWcQe3WOcHN-5makP0eClG1_8UXjGO5ryxCaciCt-GDRYrPGvc5Pd0-YKhGS4iTbAhAwR5JxDhd-NONUk8z16rKJQBzb_WBYwlDhbH4U2wDPHflxckMhiyarjOx4IdC13gb5H7EWR5f8wwWPr7wvrzRZjVxDATIAuagYHB6pzvyxoRvIXU1HE6J250PS_43q6S1rLMwikf6-ewEo_yfz6A2IPhCkftGyBoLf2raHMh1479WoAW85gXY2dWerkNaYVzP5yOsk-OLozdCUz_zZLYK3Mu0BYS22rUKHdYBHnq_gahUjQUzj1dyNO3aPVaPH-YmKycay7hnEzBj8lAMuMRhkje6akLl0QJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0743550e2.mp4?token=jGHnFLLql1XgAKdw-1DTA2k8nZohc02VIFduVUaVVOML-9aS9FQZWaGCOFvmQ0Pxmc6f_5obBNmFZfN9GG495Hp6IlKUQPAynhKLKgDBUT1JOrA5QiV_wGoaAEF_L3UpDkWKR0dU8MIDx8QVhslvjSnkIhHPa9rsnLAvgl7Rm93uGROlIVnrt6i2VkG_ER2YA1ZAVt0xXadbKIZNgvI5ysPt0b9jsANf9eCcKoBHWD-KBywRtySbqRW-rsoTZWj83295Ngn_rl9V6-ozIbxrw47tuWZkJY7C84ZHN8TAoAxcBsrpmNbNwGKd-aCFLRtqnsLC3-kigWcQe3WOcHN-5makP0eClG1_8UXjGO5ryxCaciCt-GDRYrPGvc5Pd0-YKhGS4iTbAhAwR5JxDhd-NONUk8z16rKJQBzb_WBYwlDhbH4U2wDPHflxckMhiyarjOx4IdC13gb5H7EWR5f8wwWPr7wvrzRZjVxDATIAuagYHB6pzvyxoRvIXU1HE6J250PS_43q6S1rLMwikf6-ewEo_yfz6A2IPhCkftGyBoLf2raHMh1479WoAW85gXY2dWerkNaYVzP5yOsk-OLozdCUz_zZLYK3Mu0BYS22rUKHdYBHnq_gahUjQUzj1dyNO3aPVaPH-YmKycay7hnEzBj8lAMuMRhkje6akLl0QJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی زلاتان و هانری، اسپید رو دست میندازند؛ این دلقک نمیدونه ایبرا خودش ختم این کاراست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23507" target="_blank">📅 14:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23506">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maA_mqiNAX00iB2Bkvhoa3smL1k0SjXaUnlVhaZnLsGnvU2cFPQ2Kb_fO2KISWCdM5eCfbCZSk_KjyZSKOKCDXpyFvl1V-f3xwMCKd1HYTPTSvykzDs8oL7IIJXjsK4NTzOVJJ5ih-zqi7nC54oK_8K5TrgKtJ0WlzTo8Kh6RUjM2kkTZe5tUkHnHhw0dX3xLT-eoQhKRwZ0dSG-hXh5auYkAeNj1Lmh7sWwgfhNkSTYOalR6NIsl9DezhUPRWnZaBJK8ny7jtjWsmSa5ziXbc68CLGFpyIBVVoVmGaMhhzFtpJ5YRw2BfaTwXwK-47_VE59Mn6tVxCw9hvjKSlR2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ نماینده کسری طاهری تا ساعتی دیگر بامدیریت باشگاه پرسپولیس در محلی خارج از ساختمان باشگاه‌جلسه‌ای برگزار خواهد کرد تا تکلیف نهایی این‌مهاجم‌با سرخپوشان‌پایتخت مشخص شود.
‼️
آخرشب نتیجه نهایی جلسه رو خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23506" target="_blank">📅 14:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23505">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8Xa3nU0w7dv5HPaGynMDbClXUezSnGBE-ZVRbk3AJ41NsnwHaGLrngZxEsDm4kwcgARstZSjaczlhxYCbKh1bBRF_XcZZS0vw62wd79aoVgwTUZCv-z9aqgpuVV_4A0c6ZFDwGmTipfUvMg-_byVw4tOCZV2mAJoCrSl2rkyuC0CkUdpzKJLGCuPZkn0Pq6U5zaHje4lGBodIYW0WwYSUxu6KszFR33HNOPwWc5knSjPh1WLSY5SiwhF0AkAn1NMQjcX51Yksbk-bSwJUBkctSbjdEeUoJmhdDn1JPCrSQAoJp2FWkqTzNAQS492MGs0WSaQE733aPisNRRW7cOtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خرید غافلگیر کننده کهکشانی‌ها؛ مارک کوکوریا مدافع چپ تیم ملی اسپانیا و باشگاه چلسی با عقد قرار دادی پنج ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23505" target="_blank">📅 14:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23504">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/358a407b96.mp4?token=MjNh4EO7N78o2j9aQvvl9IW9megsnz9rYmISxZ6KhK5jG7gzkatrjh43_NqF0r7d17sRrQIOQ0aUU_7M03xXhSAnYHcwKmzv9MOuboQJytFW5zYlzSEgQ1g1G8VDghH0EIx2tkitW2pVS7SVsS9XdA7jCUASoUw4UyIjVxRKuGvMS_krFtkjfGFvnXMKkhm1Y9UonehzmhJW6uliY5kNYXQ4LK57M249LaGHg8K5OHvgiFzG3voj8a1YSnyMieuMm3nkd8CgCbMp29Atn-JcwRcuhlscFTFQWH2pl6Q5rdv91aPoksv7hV1v4aETnKOKRKeX0rKt8GefLnZU8ZZyjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/358a407b96.mp4?token=MjNh4EO7N78o2j9aQvvl9IW9megsnz9rYmISxZ6KhK5jG7gzkatrjh43_NqF0r7d17sRrQIOQ0aUU_7M03xXhSAnYHcwKmzv9MOuboQJytFW5zYlzSEgQ1g1G8VDghH0EIx2tkitW2pVS7SVsS9XdA7jCUASoUw4UyIjVxRKuGvMS_krFtkjfGFvnXMKkhm1Y9UonehzmhJW6uliY5kNYXQ4LK57M249LaGHg8K5OHvgiFzG3voj8a1YSnyMieuMm3nkd8CgCbMp29Atn-JcwRcuhlscFTFQWH2pl6Q5rdv91aPoksv7hV1v4aETnKOKRKeX0rKt8GefLnZU8ZZyjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
احسان‌محمدی‌مدیرکمیته‌مسئولیت‌های اجتماعی می‌گوید بخاطر اتفاقات سال 1388؛ تیم ملی فوتبال ایران دیگر در هیچ مسابقه‌ای سبز نمی‌پوشد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23504" target="_blank">📅 14:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23502">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d283cc080.mp4?token=KS-opoQN_UG63jJmeOpJUU227i9ndrQbWC6SYkgo5FUINFCE5E4sAmrXSZpaCwTqdrlAiwSj3hLHX4oW0HcZpE9GlKEzZeRWMUH_WeH3DS0CTJ2AJaxcOhSIPPB1FlXWJkcd3RHFZoiJydVpoo_osRhMP0aR4BfhZwlPMJ6sTR2Wfo_MRtIyN0Yv8PFQE-pD-ZTtTDpCOS2hp1wj2CroVLqZH4jh8ya2XAMvE4PNCwayFsk4ALbTwtwooekn8982G47n6-tpZVU3-VPj2Gp6UEkz2qTS6DTFQGfN7IERewpHPXE1NWBHDNv2AoBfg63MLhCmaZUIT60NtXT3hdPZKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d283cc080.mp4?token=KS-opoQN_UG63jJmeOpJUU227i9ndrQbWC6SYkgo5FUINFCE5E4sAmrXSZpaCwTqdrlAiwSj3hLHX4oW0HcZpE9GlKEzZeRWMUH_WeH3DS0CTJ2AJaxcOhSIPPB1FlXWJkcd3RHFZoiJydVpoo_osRhMP0aR4BfhZwlPMJ6sTR2Wfo_MRtIyN0Yv8PFQE-pD-ZTtTDpCOS2hp1wj2CroVLqZH4jh8ya2XAMvE4PNCwayFsk4ALbTwtwooekn8982G47n6-tpZVU3-VPj2Gp6UEkz2qTS6DTFQGfN7IERewpHPXE1NWBHDNv2AoBfg63MLhCmaZUIT60NtXT3hdPZKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
فوتبال‌فراتر از یک‌ورزش؛
بازیکنان‌آلمان برای دل گرمی دادن به‌حریف‌به‌سمت آنهارفتند و از تلاششان قدردانی کردند. کوراسائو باوجود شکست، اولین گل تاریخ خود درجام‌جهانی را به ثمر رساند و حضورش دراین‌رقابت‌ها را به یک دستاورد تاریخی تبدیل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23502" target="_blank">📅 13:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23501">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PV1y-p6pBLrdt_yOKEGlgJdnXO3398ys1DLobduYFh1Ie_nY13tL4vh4c1vPVVVHwDX02YPzX-f1umQVJZITdU-qamhcIkRKcwps9uuliHkWJnRIuZr9O5NkDEu5Hdwgt5iPxFi3UtxhxUMt9n0M8IzwHHqyydf8UoQZWennGfcwDPHBh1qXDmJlo2loO-u8zveJ7yxZpouw6DvdxCnCL2lqOYmFmt3QOZKEERkIDCalW3q_KVqhDExf9nakY_a8m4yDuDx2QV_gMjck3c2wwc31E2G7ydXguCvbj8oQyAnBfk_wiY3Q0_q2DspQj6PrJ8RWpPRDAVaR0mvc8tto5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به‌بهانه‌عقدقرارداداحتمالی آموریم بامیلان یادی کنیم از این‌توییتر‌که نوشته:زنان باقاعدگی،بارداری و یائسگی دست و پنجه نرم می‌کنن، مردا چی؟ یکی از فن‌های یونایتد هم گفته: ترکیب 343 روبن آموریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23501" target="_blank">📅 13:21 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

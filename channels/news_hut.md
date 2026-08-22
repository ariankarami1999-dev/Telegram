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
<img src="https://cdn4.telesco.pe/file/dBApWbQoo74l1o6g1GhYt4i_OPV7r3b3pM28wOzJ9qXblXgwovzX95fc09avGOexECVRrmxjhedJGFnA1ro-TbJgwSZTDLPZNJqPAH2LM6w7tA9TBhH_T1tQhooy2X7kyawhMkcAwq0N2AJAnCac0jwYIbljDIVD3gsPszX57e3F3bOpboIozgGZW6t0Al2ykSz-7suTJrqwzOxxc0MzKee7h3a8eoJkb7_DZRhxBvWiRu9ifuAtISTnXdpmmjSKJeWR-djXvbaCI8VNJ2ut2kc_E_8TQKyac7GihR_W_rbiF65ucNCNTUnLWtBThmlm0Bv2BrlfUY4dUuXHNlna6A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 118K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-31 06:42:39</div>
<hr>

<div class="tg-post" id="msg-70391">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!  ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی…</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/news_hut/70391" target="_blank">📅 03:10 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70390">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=RXTgJNyi_d4aN3Bm6Tzii8cBfi4J2T_Dfx3Ezm61W3AGQ6GLl-FySLdxqR0hwprIgWzeAgSc540AnggwUPHgCmPU821orIuRe2H6wZq0z3loNGSfzBwEHwj7fgikkOeGpgHapCDrh2AW609hES9gfDJMLnjLy_OzecPvKKbmqPBhGj1LPn-cFlnfPSGl1NeMHmf003OJz-CauNDKk2yQh5sn34jJdw6lq3-cK5VzLSc84Iz-Gy2XfEtoHOU1zNMM8RvnS1Yt-DbwVxl9AXw5pjg1zeWTv7rFbaca85ehUUgRDMhP0wUSM5tDCPLBMzpxsti2vGmAveUsr6oqMw4S8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=RXTgJNyi_d4aN3Bm6Tzii8cBfi4J2T_Dfx3Ezm61W3AGQ6GLl-FySLdxqR0hwprIgWzeAgSc540AnggwUPHgCmPU821orIuRe2H6wZq0z3loNGSfzBwEHwj7fgikkOeGpgHapCDrh2AW609hES9gfDJMLnjLy_OzecPvKKbmqPBhGj1LPn-cFlnfPSGl1NeMHmf003OJz-CauNDKk2yQh5sn34jJdw6lq3-cK5VzLSc84Iz-Gy2XfEtoHOU1zNMM8RvnS1Yt-DbwVxl9AXw5pjg1zeWTv7rFbaca85ehUUgRDMhP0wUSM5tDCPLBMzpxsti2vGmAveUsr6oqMw4S8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!
ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی تخصصی بازی‌های دوستانه باشگاهی و تورنمنت‌های معتبر
➕
فرم‌های گلزنی (بله/خیر) و گل بالا/پایین با تحلیل آماری
اگر می‌خوای از روز اول چالش همراه ما باشی، همین الان وارد شو:
🔗
https://t.me/+UfR2NG4GjAMwNTQ0</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/news_hut/70390" target="_blank">📅 03:10 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70389">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoZEUKP_TsWGqMHmX-2-OeCNTDM9-0dBOLPoOIKF21Ip1MGmVal_qUJ442MJuQrdVnB78qWZt4RuSf0cQKIC5SfZNWQflLdnDykDCMF2dgrOQVIHkb0P3DP8M2bmgMF-tcfBoBsOYgy2a5LVWJhkIP4B3yMe2Bw3moMO0HS3Cc-4O1d8RRyz8xIhSC9T59bvcJa2-pBP7z8WneoNpfyNc4NyOOrurQKIyyqr-CwDtKWtHZLiMxqMVQrb2TeyzrANoMRPH7GnhtsxbQgD15IHg7uQPf_qwf4SpU_0afdm0E2fCqfqyYzBSDTZienPkosm_2ISvCsx3xw3XYO4zPCKaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
فعالیت پنج سوخت‌رسان و یک هواپیمای هشدار اولیه در اطراف تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/news_hut/70389" target="_blank">📅 02:10 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70388">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c253cab7c2.mp4?token=IM9hcvcpdzvNaR1lXyYSbc_AAtmHlicmS3vJLtYQcByN2u_abmUloUAgVcot-Sujk-_xZFSo-31Q0KOl4uarJhjGE3kAezOAW1VvwMRtwVfLs8xJEHy4Rd4v7aHJLBTrkznw-Xk6cWKeZ8AC5rAxZwjyEV1sXMnbay0bJd_72mQr7h_YSS2HqondSIBbw9zam6Pw-VHKrTJFrWhWmR8lnaiBbkws0MDK7xT490-76AsjSMx28_KZZdQzfIASC73Mq32ocrP2Ujggi5sGQBuvazo1S4qsRCe-JVTvoz12JORTWvUC25Vu5hDMQ1lKnh0xisHTT9x4dPZJN3BPSTGWJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c253cab7c2.mp4?token=IM9hcvcpdzvNaR1lXyYSbc_AAtmHlicmS3vJLtYQcByN2u_abmUloUAgVcot-Sujk-_xZFSo-31Q0KOl4uarJhjGE3kAezOAW1VvwMRtwVfLs8xJEHy4Rd4v7aHJLBTrkznw-Xk6cWKeZ8AC5rAxZwjyEV1sXMnbay0bJd_72mQr7h_YSS2HqondSIBbw9zam6Pw-VHKrTJFrWhWmR8lnaiBbkws0MDK7xT490-76AsjSMx28_KZZdQzfIASC73Mq32ocrP2Ujggi5sGQBuvazo1S4qsRCe-JVTvoz12JORTWvUC25Vu5hDMQ1lKnh0xisHTT9x4dPZJN3BPSTGWJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
〰️
سنتکام:
ملوانان نیروی دریایی ایالات متحده در حالی که ناو هواپیمابر «یو‌اس‌اس جورج واشنگتن» (CVN 73) در دریای عرب در حال حرکت است، عملیات پروازی شبانه را بر عرشه آن انجام می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/70388" target="_blank">📅 00:57 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70387">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4291f4458.mp4?token=uU-vydRWy1OVlrQhy2XjXGlja1WAXBHTRtTQool8_C9dtE7bEPlwqWnJ3xL1jXRUBzrLDX2AHa1ofLhkQ_ggMPbhVQzcKq1EScm9KkthpWneS6Ujb7YfxuutEETa7pda0U6JwIvXzXS4eOrIom2-_McRKyz6NwKlqfoqr9-SIAujGu3jdp4HHvWcyKXAM4liMPhu_1Xh6QhSY6T9u4pIOa0REz4GO_mAYZlqr97wPzA-RB4AMTtsGPjqdbYY38JetiMGzi67xqSGwqIJ5T2YyBLJinScg8o4zaUp8NvTiJMvIFmgO0LNZ0g49wGb2sxD59xxiVJj8jbjBzAuJVQUl71Ud2KE5itryQ7tr5QXNruyqrm7LztsndsNG15zqx5kJPYlOoWlupK8FgdIW7bwg-xFrN9TzeE-dQACaI8vRWPjnu2CDMd_NaFnFokYsXQ_0G6MpdtMEbcgXfvo4u4ICrZK_QY_eWthPTt38HAr-0n6E4ygobfK_CqxQQjD0TX4yQBVElI_M5cpB9nJHaj5bi72u2JcYHInyYGmAw35k85Zvmrkz0Hvhb9mGFCcvHkXQwNBqCmGoDvmpQpyhCu9A1hHUVAsvFTp1t_4WLbl02j-YRM0ZhHYYKgPM_3Ng5ZhRkcC8S4hC_OI7SX-vojIHxSzr59wAQ8Ce6evj3xRIp4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4291f4458.mp4?token=uU-vydRWy1OVlrQhy2XjXGlja1WAXBHTRtTQool8_C9dtE7bEPlwqWnJ3xL1jXRUBzrLDX2AHa1ofLhkQ_ggMPbhVQzcKq1EScm9KkthpWneS6Ujb7YfxuutEETa7pda0U6JwIvXzXS4eOrIom2-_McRKyz6NwKlqfoqr9-SIAujGu3jdp4HHvWcyKXAM4liMPhu_1Xh6QhSY6T9u4pIOa0REz4GO_mAYZlqr97wPzA-RB4AMTtsGPjqdbYY38JetiMGzi67xqSGwqIJ5T2YyBLJinScg8o4zaUp8NvTiJMvIFmgO0LNZ0g49wGb2sxD59xxiVJj8jbjBzAuJVQUl71Ud2KE5itryQ7tr5QXNruyqrm7LztsndsNG15zqx5kJPYlOoWlupK8FgdIW7bwg-xFrN9TzeE-dQACaI8vRWPjnu2CDMd_NaFnFokYsXQ_0G6MpdtMEbcgXfvo4u4ICrZK_QY_eWthPTt38HAr-0n6E4ygobfK_CqxQQjD0TX4yQBVElI_M5cpB9nJHaj5bi72u2JcYHInyYGmAw35k85Zvmrkz0Hvhb9mGFCcvHkXQwNBqCmGoDvmpQpyhCu9A1hHUVAsvFTp1t_4WLbl02j-YRM0ZhHYYKgPM_3Ng5ZhRkcC8S4hC_OI7SX-vojIHxSzr59wAQ8Ce6evj3xRIp4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی پشم‌ریزون از زلزله شدید چند روز قبل در کلمبیا که باعث شد ساختمونا برن رو ویبره:
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/70387" target="_blank">📅 00:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70386">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
⁉️
دقایقی پیش حوالی یوسف‌آباد و امیرآباد و فاطمی و... در تهران صدای فعالیت پدافند شنیده شده.
عده هم میگن صدای تیراندازی بوده و همه چی آرومه.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/70386" target="_blank">📅 23:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70385">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc11d1c4b.mp4?token=JwV2qT9f70wDyu7kr-lANkvksCu-yJ2eEbkTlKUuzHUgm7rBD83ose9l49Ui5P3T8cxOctDbCV5efnjOhu-BfztmR-tXIS6uVWbiEaDPy2E7RG3YvIyeLvRvEO1aEkw54qG6BkYwog_Xm-kC77557CHTCHWUizeRyaNG6lf-wXktDTD71biijHGpWCSzK6RGpD9nxUfFW_BRWcbBMVSbqHbWa8wLewaol_lKaKIrtQTnbulaUxDPHTGejS5P8YVaBccCSipXHgbukDfGrkKqjyu-0zkBfFM1uBIdkKkXnNWabl6clqQWHHeqeGdPBA2bK79GcC-C2aZbAoB2eTe5Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc11d1c4b.mp4?token=JwV2qT9f70wDyu7kr-lANkvksCu-yJ2eEbkTlKUuzHUgm7rBD83ose9l49Ui5P3T8cxOctDbCV5efnjOhu-BfztmR-tXIS6uVWbiEaDPy2E7RG3YvIyeLvRvEO1aEkw54qG6BkYwog_Xm-kC77557CHTCHWUizeRyaNG6lf-wXktDTD71biijHGpWCSzK6RGpD9nxUfFW_BRWcbBMVSbqHbWa8wLewaol_lKaKIrtQTnbulaUxDPHTGejS5P8YVaBccCSipXHgbukDfGrkKqjyu-0zkBfFM1uBIdkKkXnNWabl6clqQWHHeqeGdPBA2bK79GcC-C2aZbAoB2eTe5Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ظهوریان، نائب رئیس‌کمیسیون اقتصادی مجلس:
افزایش قیمت بنزین مثل چیپس و پفک نیست که راحت بتوان قیمت آن را تغییر داد
هیچ‌کدام از ۳ طرح مطرح شده، برای بنزین مناسب نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70385" target="_blank">📅 23:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70384">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9209031f2e.mp4?token=tWCKWv_ttISNRbswZCvDagFL_7Ta7iCZZYPsTVMPqF2cYypTsx7NxcJ_T5mqGOzDnf7F6zdz0a6EE8Dw7mS1Ji8ocv1x9QrfxfcDcmjTbH5kPpeKwPdLyWKNYocLd_t62G5tnuY7BMVWCG6aMlwjVpHLgEunKj5sWDK28T9Kt3CSk1bBMUVADVw7c-rdKAh7LFYn_L4zifxIl3vZyQQL5kB-7dAUfVoQCm14pB3rB0O8Ro0t9q5bUBSsEPBQG2RXBcgur1tSK4j0VWBcPdcAGvRuWm4x6DNB68UpwAnqelYI5X3eUsYRcxmwc3SUjYPn1CgurU9Km05qYDEkIgJvBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9209031f2e.mp4?token=tWCKWv_ttISNRbswZCvDagFL_7Ta7iCZZYPsTVMPqF2cYypTsx7NxcJ_T5mqGOzDnf7F6zdz0a6EE8Dw7mS1Ji8ocv1x9QrfxfcDcmjTbH5kPpeKwPdLyWKNYocLd_t62G5tnuY7BMVWCG6aMlwjVpHLgEunKj5sWDK28T9Kt3CSk1bBMUVADVw7c-rdKAh7LFYn_L4zifxIl3vZyQQL5kB-7dAUfVoQCm14pB3rB0O8Ro0t9q5bUBSsEPBQG2RXBcgur1tSK4j0VWBcPdcAGvRuWm4x6DNB68UpwAnqelYI5X3eUsYRcxmwc3SUjYPn1CgurU9Km05qYDEkIgJvBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
❌
🇮🇱
فرمانده سابق نیروهای ویژه ترکیه، زکای آکساکالی:
اسرائیل نمی‌تواند با ما رقابت کند، ما مانند سایر کشورها نیستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70384" target="_blank">📅 22:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70383">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kU1goLSNNg0FLx9y6kQ3OIepfitmHhO6g9MFSjvF8-XjBTyH233fTZHkF56snKyt1TWjFiQyS5XCzkB9qZsS0Vu0Ang6H3nyfoVHNnOMMvfxifBUBxvvqkKTXVG4f6YNwORGArotD1CqSfq0eBuK20747LbNXJnPqd_pU5e9oHbyvOJ-Q_UKsubFVjsiWUBUoWAZw6sR2FnbFHONPltFlVxdA-zi0BOKeI2d6BInJElyj0FnvC_OPKdpwfrIfZEfw5TE8R01QjgBVM-P9-GQVObo80sAEUqlPpS3p2rgIrU10pHTat_R6pk2HXdt1CSALvFMJh4lBx_CisHfBNMT5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ بازنشر کرد:
رئیس‌جمهور ما به ایران هر فرصت ممکنی را داد تا سرانجام رفتار خود را اصلاح کند، از نقش خود به‌عنوان بزرگ‌ترین حامی تروریسم در جهان دست بکشد و به کشورهای تولیدکننده بپیوندد. او درباره پیامدهای ادامه مسیر غیرقانونی و وحشیانه‌شان به آنها هشدار داد. اما «رهبران» آنها چیزی جز رفتار تروریستی و قانون‌شکنانه نمی‌دانند و اکنون رئیس‌جمهور ما به وعده‌های هشدارآمیز خود عمل می‌کند. این‌گونه است که رهبری واقعی عمل می‌کند!!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70383" target="_blank">📅 21:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70382">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7188f3aad0.mp4?token=PBC0y6c_sGm2nW0LAJZCUtvJ6ZEvfeCgCvWFb1vMIo_mPbC9t9bhScdOQbXiv_7IIWdeqP5d7bqPsgfW8asEE5HFxhuNInBHqBoiA48YLZqCYfzr2XvwTDYrzbFcJ8LAdKCF4bj5D8YQAUPSCC-XtICZgsfTVOVE_5S9OvnOltpKE69lh8B8ziPO_v2wF3hDJWUFa9arO0FKFSER5Ub_0QNyeG0s2lqg1cRFNEZznWlzbN5w_MOK7byqoG1Ia9uiRXrhdmOf1um-zb_8dzzZmD3DS38d7d92ErOt4Vuvd7SmEMeHcp_o_mOmdpEHzdAnUVzjZSjmXWRXRBY1ZxZCTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7188f3aad0.mp4?token=PBC0y6c_sGm2nW0LAJZCUtvJ6ZEvfeCgCvWFb1vMIo_mPbC9t9bhScdOQbXiv_7IIWdeqP5d7bqPsgfW8asEE5HFxhuNInBHqBoiA48YLZqCYfzr2XvwTDYrzbFcJ8LAdKCF4bj5D8YQAUPSCC-XtICZgsfTVOVE_5S9OvnOltpKE69lh8B8ziPO_v2wF3hDJWUFa9arO0FKFSER5Ub_0QNyeG0s2lqg1cRFNEZznWlzbN5w_MOK7byqoG1Ia9uiRXrhdmOf1um-zb_8dzzZmD3DS38d7d92ErOt4Vuvd7SmEMeHcp_o_mOmdpEHzdAnUVzjZSjmXWRXRBY1ZxZCTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇭
در شهر برن سوئیس در تابستان، خیلی از مردم، در مسیرهای مشخص بعد از پایان کار وارد رودخانه آره (Aare) می‌شوند و همراه جریان آب تا نزدیکی خانه‌شان شناور می‌شوند.
لباس و وسایلشان را داخل کیسه‌های ضدآب می‌گذارند و در نقطه مشخصی از آب خارج می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70382" target="_blank">📅 21:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70381">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpaB5yiqG4A4q6xQYgUGdiayC5qGI3IfCrbl9mLscD2aM4ltOxeVYstzt3z0UtgumcrJFnVRN7PjNpO6_olP_rO8VcpR_5gNhswXXYGRlML59IEuaX5j0LdIAx3K7-WP1diTdnyrCjCN5urND4BSt3jFOgjJDtgOqUwY8cGgMy_gX1MIhWiARhsMujWx56hah3Dc51ATuw1V4qJMYXNxzZGovALPPrVdkX6QFN2qMzpxj5dT5by8fnOe3dEkt27T_xP0Y9VSBLvbzz1N5r679saJoKZynh8-ILEOgqXlQcBBF1qFTrOO9g6axUlolPg00r2eEnnnGWNSz_sXZa55Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ابراهیم عزیزی رئیس کمیسیون امنیت ملی مجلس:
ایالات متحده ثابت کرده است که زبان دیپلماسی را نمی‌فهمد. آن‌ها نه تحریم‌ها را لغو می‌کنند، نه منابع ایران را آزاد می‌سازند و نه به دزدی دریایی پایان می‌دهند.
با این حال، تاریخ نشان خواهد داد که زبان قدرت، آن‌ها را وادار خواهد کرد تا نه‌تنها این اقدامات را انجام دهند، بلکه از ملت بزرگ ایران نیز عذرخواهی کرده و برای همیشه منطقه را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70381" target="_blank">📅 20:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70380">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eR82TW4FlsXG44Q2MK-Gj6NYbE_JI8ObRGuTFcfWDwHbwPx-Lco3RiAkPG_Zn8cEuS28djJXaWPjM7fIw5wSMUfc6NjdZYVj36Fx4fUOHT2L7fu7yDKkq7oDHluJz_eURHwBE46SWR2AQVoNg61FrncLlTdeaQANEN4WIqGFvxUzgzGb4G3UPIbgZfUcUzZIgswt0jh45yhRzirNdDgIGVnYg7ELmP4u-SJJFtlPGn_ogL7xbHcYO9AhoS7JRG78IsAS9PeKP13RJTuIIc__Dq8RUJFlYjcKaTyLMsHLxOC-xPDnBOIp9IMGmoLbLojmZBuQtqMxA5fNKg5a77rq4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی:
۱۴ سال پیش: «فلج‌کننده‌ترین تحریم‌های تاریخ.» شکست خورد.
۸ سال پیش: «فشار حداکثری.» شکست خورد.
۵ ماه پیش: «تسلیم بی‌قید و شرط.» شکست خورد.
امروز: «ویرانگرترین عملیات اقتصادی تاریخ.» محکوم به شکست است.
ما این فیلم را قبلاً دیده‌ایم. همان حرف‌های پوچ؛ همان قلدرها، اما با چهره‌هایی متفاوت.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/70380" target="_blank">📅 20:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70379">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/781f58184f.mp4?token=iUoG7VXsF7Gxxw59EUylGs2LDPzV5IThw53cDhFlGRyuRmgeOMiFp7UOeWcamjZx79lG2f8YHg-q3aHvoNI6RnJex_Ox08wFmzptXuBEboEcXSusuQbHXjnV9gvtywgbGYI9gnmt99VtBL6mmOWBF1cF0StsR0mdimJ5JKcyhR60qo2pVqIKxTLzNgWGQas-i4zRUP85YRzr8g8lV4YD6UbOLevUA3M91Rz-1GO1p5BuX0AzXR0K7fDBIZOqBMRpFu6RXHUkVPwO2x4fwJzY_bTWH4r0Dh8C-bKa858R5g3bkQoFtagQVYvL1HvXIJbAto5R5AUB_opHfYNsqnRc-WHj1lrazwoIU9CJCzMhBvg_iVtc8QmxhJ3yZyq99UQorGs0Kf8zq72xpEV7uda-LP9WBXsSaa1i2_0ZiOSqhGnzquTreu16fCkhqWq1E3kEb3Vjpf9G6z00IOJr2-bnbihrgrhxD-s7IFV9MYbhnpKtLvBICFJp5U5o4x2_op7eXtDV8L4ByUmJHvP24fi4JJQ31X75kX6iTRTngGnNznqOmaDBH2eDV4FUB8Q4J30CTvhMN3vjcOHfilzioEy9H-OmUEjroI6SPdimznxz70HJNB71Mjz1qBlmZhPo4Stb6EqA-A0wbRLozXc_ovkv6JuHlGh6rMb6Ol6a2MVq19Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/781f58184f.mp4?token=iUoG7VXsF7Gxxw59EUylGs2LDPzV5IThw53cDhFlGRyuRmgeOMiFp7UOeWcamjZx79lG2f8YHg-q3aHvoNI6RnJex_Ox08wFmzptXuBEboEcXSusuQbHXjnV9gvtywgbGYI9gnmt99VtBL6mmOWBF1cF0StsR0mdimJ5JKcyhR60qo2pVqIKxTLzNgWGQas-i4zRUP85YRzr8g8lV4YD6UbOLevUA3M91Rz-1GO1p5BuX0AzXR0K7fDBIZOqBMRpFu6RXHUkVPwO2x4fwJzY_bTWH4r0Dh8C-bKa858R5g3bkQoFtagQVYvL1HvXIJbAto5R5AUB_opHfYNsqnRc-WHj1lrazwoIU9CJCzMhBvg_iVtc8QmxhJ3yZyq99UQorGs0Kf8zq72xpEV7uda-LP9WBXsSaa1i2_0ZiOSqhGnzquTreu16fCkhqWq1E3kEb3Vjpf9G6z00IOJr2-bnbihrgrhxD-s7IFV9MYbhnpKtLvBICFJp5U5o4x2_op7eXtDV8L4ByUmJHvP24fi4JJQ31X75kX6iTRTngGnNznqOmaDBH2eDV4FUB8Q4J30CTvhMN3vjcOHfilzioEy9H-OmUEjroI6SPdimznxz70HJNB71Mjz1qBlmZhPo4Stb6EqA-A0wbRLozXc_ovkv6JuHlGh6rMb6Ol6a2MVq19Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یک آخوند در تجمعات شبانه:هنوزم از کنار بیت رد میشم بوی گوشت سوخته آقا میاد
🤣
🤣
یه روز یکی بهم‌گفت بیا بریم بیت هنوزم بوی گوشت سوخته حضرت آقا میاد
گفتم اغراق میکنی چنین چیزی ممکن نیست
خدا سر شاهده رفتم بیت دیدم هنوزم بوی گوشت سوخته آقا میاد
نامردا ۱۱۰ موشک سنگین به بیت آقا زدن
حضرت آقا بدن لطیفی داشت اصلا ایشون آرزوی کربلا داشتن هروقت میرفتیم‌کربلا میگفتن به نیت ایشون قدم بزنید
الان رهبر شهید شب جمعه ای کنار امام حسین نشسته و داره ما رو تماشا میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70379" target="_blank">📅 19:13 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70378">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IyNUP7Lmtep3uXSxc0MzqIViSV1hf3jhcKxm5IT_JCNvLKQuJtwXGt0Z4ssQBIxBbKAeaDM5Dn3cY890Cp0zgOoel_DFyFTbZsXiwe1jo739oRkFM7k-PRH6A-Z0HGqMUXcOF4TCwMazvP5c_tiecOO1sxtOjHWfZurDviHeIMsKkwsUlfmdJI-8QvX1xDvghkTXqG-mZocLLONf3hEQyTkOlhRF2i8KQHvitfyM2NhCtnRiw-rYn_PoJN1Kq7az8-9MibSzxupPBiejKkNepifDMFLhQXGcctrHTo7_eouhxcfKiuAisRJspHim5eAeG7g8CH8l9r9Xdge2r2VUlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
〰️
سنتکام:
تا تاریخ ۲۰ اوت، نیروهای آمریکایی مسیر ۶۷ کشتی تجاری را تغییر داده، ۳ کشتی را از کار انداخته و برای اطمینان از رعایت مقررات، وارد ۲ کشتی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/70378" target="_blank">📅 18:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70377">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb50540ec1.mp4?token=LyJ5Dkw15TsdRo2QlkhLkq3YJ7B4UKXzOuTwKtTAIFErNvznyfVZYtNCoABSKZzBh7teC3dAQF68Pwf1ypc6ImOA6Z6tCc63uS94sjLtIivZwrTvt_qczDt6dLPVqZ8rSgpdN2PSCjLYLON95Ig6yeNaHfN4n0KjLCb4E7JVe4wWh2HbKCcszZt_OTCJ2gIBu3_MkiFK4Ul3Jd4SRL1eQdGzvlYmzb2Rb0MdiO59cMYF3uQtHm7anW2QZ2qI844PfodGWl3Ze7Im9pEnoPzMhlp5iX4qa-VxxFmPkDuCpIKsKVWSitFod6IxkhtcotjKOnLbgr0hiSpipxSaaod54mF5i6M_ZkEtPzbaK7jEeFVvYPEGdfuHF-yF9vO-vGeor9PROHJvNlmRlxWNCw6VZLgyWaXZA4sr1nmXgzychHK1_PdL0vtDwuqC1m-hnc8PQNfrzgjiH60rYdMDGpmNEoF12sqVmHuaFISZHhhCEhsH_AIpEnTZP-TtnLJ7bjKv5LCbwywF-eevhL2b1CaHvebGaynnLc_H4c3QKjQGOTjFJs-EK7Ci_68yrp64yh-gTbw2zzVXQZjq__GRuv3aaOkP0yervnePjogUKmht4PqQdOkr9lhZXNqi8UjTeG_swMdjy3ASjY2LmXxSuxM8YVF3U3_3FLot6Bu3IcD8rOs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb50540ec1.mp4?token=LyJ5Dkw15TsdRo2QlkhLkq3YJ7B4UKXzOuTwKtTAIFErNvznyfVZYtNCoABSKZzBh7teC3dAQF68Pwf1ypc6ImOA6Z6tCc63uS94sjLtIivZwrTvt_qczDt6dLPVqZ8rSgpdN2PSCjLYLON95Ig6yeNaHfN4n0KjLCb4E7JVe4wWh2HbKCcszZt_OTCJ2gIBu3_MkiFK4Ul3Jd4SRL1eQdGzvlYmzb2Rb0MdiO59cMYF3uQtHm7anW2QZ2qI844PfodGWl3Ze7Im9pEnoPzMhlp5iX4qa-VxxFmPkDuCpIKsKVWSitFod6IxkhtcotjKOnLbgr0hiSpipxSaaod54mF5i6M_ZkEtPzbaK7jEeFVvYPEGdfuHF-yF9vO-vGeor9PROHJvNlmRlxWNCw6VZLgyWaXZA4sr1nmXgzychHK1_PdL0vtDwuqC1m-hnc8PQNfrzgjiH60rYdMDGpmNEoF12sqVmHuaFISZHhhCEhsH_AIpEnTZP-TtnLJ7bjKv5LCbwywF-eevhL2b1CaHvebGaynnLc_H4c3QKjQGOTjFJs-EK7Ci_68yrp64yh-gTbw2zzVXQZjq__GRuv3aaOkP0yervnePjogUKmht4PqQdOkr9lhZXNqi8UjTeG_swMdjy3ASjY2LmXxSuxM8YVF3U3_3FLot6Bu3IcD8rOs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این هواپیما پس از گرفتار شدن در تلاطم (توربولانس) شدید، ناگهان وارد یک وضعیت کاهش ارتفاع تند می‌شود؛ وضعیتی که با پر شدن فضای کابین از صدای جیغ مسافران، موجب وحشت آن‌ها می‌گردد.
تلاطم هوا می‌تواند باعث تغییرات ناگهانی و شدید در ارتفاع و سرعت عمودی شود. اگرچه این وضعیت از داخل کابین ممکن است بسیار هولناک به نظر برسد، اما هواپیما به گونه‌ای طراحی شده است که در برابر فشارهای ناشی از تلاطم‌های شدید مقاومت کند.
بزرگ‌ترین خطر معمولاً متوجه مسافران یا خدمه‌ای است که کمربند ایمنی خود را به درستی نبسته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70377" target="_blank">📅 18:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70374">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m6Ygw8MUazt6D3sgWjJkB3rYZyjIPIhQWKxhF8p6ASSkwB8eY1Zv9L-uS4qE0sxwDRgWCI8nLBLuzpw-ozoj5EDyl7J3aQpWr-vAx9W5SFu6sSKP3f1do2IdVbrmqgFq4189SIs_fsunWQfuVcpy-Y0c0OISgJaY8M1lIdjVE0t4dqKXAvQ-lGDsN99TRKMAGGZTZDJ9hPjnfXwvVYXDNTQMtsFRm-z_WMJcYl7F1T5lyI36HKZhnDrAf2P7oX8VD1yFYUIUPT-8jalJBYmAZAcqyGlVxNPTfpRY6dv4XnX8T30Oaw7NmM-DPjGQto9sWvjJ8MpHhSNpRRuWlB9P0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rqHN6F_WXJ3dBhAqS4vogxQoJrnX-NT9GXWF1rkWbFijG36G5ire5jJXfeQHckh86_c5E57Nie-bZIrM0P62kjBP8wleMOLDcArFECIxp2Cdi-I2H-lb0EBUVRQrktj6j6qBtzj-3kYPbYH5B88sDfx4nLBBpmKqoUuj-KykqUyEgMC87a-mTmDwygE_Nl1-iy7nvDQESuKJLtom3oc8Lkow3RfEt_-361sq0ANa-BE5Q8msdoc8Bg4QELP9vZUCTmX6c66hMOkyf6KCx5J5XVxGMW__YwhHTiTfZPWmE6XC4xJ2iFRTpMvqRvKRfe0EgW2EyKIASuJPHqGkl7QMCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee703d2eeb.mp4?token=Xtfct4ytzKvM1ttt25OTsHJ5VXZbUVuKNArJiEPwdreS2CfciOhvTFQVsfPmaE0wUNVLe2ie1Qt6ktrdwBT_2r1g80G86DI2OyKzKkdJo0U29qWmLXPdD_yepy7tiVwW8yriA2qGnVpvSuqA2iKRMoXkCnqqqw6YBKbOkxa0zlMdkLWFRwIvlsjuoBoyGxE7vJJY5EVZx6t4RJAPv5qScMwumwYYHh0vbVnxglC1Wvyz5kDaNlz5cE2hkDIa5tX281Ixw7O092RrR27JebmPkV59jy4mPgLGpy_SgqwkE1l4KAwN63TKZ0R7KCW5Wvif3r83uL6iASFWK8mGgGeS6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee703d2eeb.mp4?token=Xtfct4ytzKvM1ttt25OTsHJ5VXZbUVuKNArJiEPwdreS2CfciOhvTFQVsfPmaE0wUNVLe2ie1Qt6ktrdwBT_2r1g80G86DI2OyKzKkdJo0U29qWmLXPdD_yepy7tiVwW8yriA2qGnVpvSuqA2iKRMoXkCnqqqw6YBKbOkxa0zlMdkLWFRwIvlsjuoBoyGxE7vJJY5EVZx6t4RJAPv5qScMwumwYYHh0vbVnxglC1Wvyz5kDaNlz5cE2hkDIa5tX281Ixw7O092RrR27JebmPkV59jy4mPgLGpy_SgqwkE1l4KAwN63TKZ0R7KCW5Wvif3r83uL6iASFWK8mGgGeS6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دختر لب ساحل ، با این پوشش ساعت ۷ صبح رفته و از اون ور یه مرد با شرت هفتی اومده بهش گیر داده که تو چرا اینجایی پاشو برو تو قسمت زنونه...
دختر هم میگه داری بهم استرس وارد میکنی، مرد میگه استرست بیاد بره تو کونم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/70374" target="_blank">📅 18:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70373">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">امروز تو ویپاری رو برد آرسنال
⚽️
100 دلار بزارید 245 دلار (25.000.000تومان‌بونوس میده)  سود کنید.
✅
🎁
برای مبالغ بالاتر از ده هزار دلار بیمه شرطبندی ۳۵٪ داره‌
و مبالغ بالاتر از هزار دلار بیمه ۱۵٪ داره یعنی در صورت باخت مبالغ به حسابتون‌ دوباره واریز میشه.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/70373" target="_blank">📅 18:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70372">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari (3).apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/70372" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر WEPARI
😀
😃
😄
😁
🔥
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 120% اولین واریز
‼️
🔥
بونوس برای 4 واریز اول
‼️
⚽️
بونوس ورزشی هر دوشنبه و چهار شنبه
‼️
🎁
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :
Gift
🔥
دانلود مستقیم اپلیکشن اندروید
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
📌
آموزش نصب برای IOS
g39
✔
https://t.me/WePariFarsi</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/70372" target="_blank">📅 18:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70371">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea7209957.mp4?token=GrAgtKdcs11Uwujv8pkuMbNnY4mdom8YOB0gWyA-GYpc2-yzPZKOh8T7bpQIQrR1MlIsEbsp0encfoNEF23cIPeaYt1kUnMRfmWHGXjYnRMgZOUuLZG0g8elwaePHry2StUG2vjcahymFCy5ZrEvFFyM_Ex1wpjMZgqEm_08hfsnYPtnxJ8xIj6vPuJUukOLOSN9HrXhdzKAcy7Vx7ufjxeObQa4T_5C6ED-C3WA2PAVsPST00yjAKWY5Xr0FVvLeq-BQaGCss4DIP2L6fJqO79EZ1947CZMLOSWUL-CDP2uLiG5RPcBL9D1HBAHeuBrVx0SSdhV1UTNUlqT5U7WMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea7209957.mp4?token=GrAgtKdcs11Uwujv8pkuMbNnY4mdom8YOB0gWyA-GYpc2-yzPZKOh8T7bpQIQrR1MlIsEbsp0encfoNEF23cIPeaYt1kUnMRfmWHGXjYnRMgZOUuLZG0g8elwaePHry2StUG2vjcahymFCy5ZrEvFFyM_Ex1wpjMZgqEm_08hfsnYPtnxJ8xIj6vPuJUukOLOSN9HrXhdzKAcy7Vx7ufjxeObQa4T_5C6ED-C3WA2PAVsPST00yjAKWY5Xr0FVvLeq-BQaGCss4DIP2L6fJqO79EZ1947CZMLOSWUL-CDP2uLiG5RPcBL9D1HBAHeuBrVx0SSdhV1UTNUlqT5U7WMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه سری دخترا بخاطر اینکه امروز کنکور دادن، این شکلی از پدر، پارتنر و... کادو گرفتن:
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/70371" target="_blank">📅 18:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70370">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8650fb289.mp4?token=RQsUgz8dBgoOCZOAYXEzr9hcg6P54sdS4pdUfKdS-VHmqpEuDJXmNlQBj1Mdlnq4BaVl2Yu1FF8YVsLE4ehqp9eXfQx-n53y71BVpDyHJ-LSR0dLCHOtD9D0sK7cGTY1hVSb3WbTlPVUMJAm5G_JWaunhaqfSuISI9qRK92vdqtpzgVcoquGzK9pjVIVocB88BowBNq8Ts-a5uXYaP9QzL_LBMRJgBZtlcuikX1X5Gf2EOMdwtdCwRczMA4_Qm93bSeVRWkeFpDxH6T2VEvlFy2Cb-Et_LN3WG_9C-S8df3SnEcC_Ib970LUFG_pDkMznwBDKUDnL8n5cOxhyPG7Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8650fb289.mp4?token=RQsUgz8dBgoOCZOAYXEzr9hcg6P54sdS4pdUfKdS-VHmqpEuDJXmNlQBj1Mdlnq4BaVl2Yu1FF8YVsLE4ehqp9eXfQx-n53y71BVpDyHJ-LSR0dLCHOtD9D0sK7cGTY1hVSb3WbTlPVUMJAm5G_JWaunhaqfSuISI9qRK92vdqtpzgVcoquGzK9pjVIVocB88BowBNq8Ts-a5uXYaP9QzL_LBMRJgBZtlcuikX1X5Gf2EOMdwtdCwRczMA4_Qm93bSeVRWkeFpDxH6T2VEvlFy2Cb-Et_LN3WG_9C-S8df3SnEcC_Ib970LUFG_pDkMznwBDKUDnL8n5cOxhyPG7Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پسر به اسم امیر 850 میلیون برای دوس دخترش طلا خریده! حالا برا چی؟ دوس دخترش Pms بوده و میخواسته حالشو خوب کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70370" target="_blank">📅 17:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70368">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/600be60d87.mp4?token=daxGMhgX7o-CVraO3Pze9dH9xTV1Ekqg_0FZeDkDiRZ_wz2VTWdZ84c8kTOBbKsMj4n1HkzAEJ4klxsn8iyVA6ovXGPXpkJT8RXLcHiqS7uFR16VbbVcW63wXFyuC5YZ8aLUF51G3LP9ieCkFh4o21nCwe4Cx3ANjSBPY03iv7zKHPsZfQwkms-BaGbkHvTHL8IcNxXg8uwgZvXdDhoipGG4qAgtMsHuS0Z2HLozMLNScKtHki6E98q6eM9cfDud_POtMEA4itNmpcxbuPtqTrYrJsrnpUOrRNBloobUtsPAGhxqSBYmXPIpBs9yi4OXKuRt6ufasuojAk-Z_961mg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/600be60d87.mp4?token=daxGMhgX7o-CVraO3Pze9dH9xTV1Ekqg_0FZeDkDiRZ_wz2VTWdZ84c8kTOBbKsMj4n1HkzAEJ4klxsn8iyVA6ovXGPXpkJT8RXLcHiqS7uFR16VbbVcW63wXFyuC5YZ8aLUF51G3LP9ieCkFh4o21nCwe4Cx3ANjSBPY03iv7zKHPsZfQwkms-BaGbkHvTHL8IcNxXg8uwgZvXdDhoipGG4qAgtMsHuS0Z2HLozMLNScKtHki6E98q6eM9cfDud_POtMEA4itNmpcxbuPtqTrYrJsrnpUOrRNBloobUtsPAGhxqSBYmXPIpBs9yi4OXKuRt6ufasuojAk-Z_961mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ورود پسرای مجرد به سیتی سنتر خلیج فارس اهواز ممنوع شد!
بخاطر اینکه پسرای مجرد دختر بازی و دور دور نکنن، ورودشون به سیتی سنتر خلیج فارس ممنوع شد!
ورود دخترای مجرد هیچ مانعی نداره و میتونن وارد بشن، بزودی قراره در سیتی سنتر و مراکز خرید سراسر کشور طرحی اجرا بشه که؛
ورود پسرای مجرد ممنوع بشه که جلوی بساط دختر بازی گرفته بشه!
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70368" target="_blank">📅 17:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70367">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a5f935a3.mp4?token=pRS8c5svERAtziApgbldYljxnzgnptaGvclY3CgmKMVzl0fJbwUsc44EiQgBgK4RoVezv5wKrPdZNaWrKNeJC89_trQZjGxwl3DRj_DDikkKPf0Sh3hHCh-t6umn2l3ps37FzBz8j_NLMizCUVPJTz-Mh3Hp21lUd_8ThFdWeIepvFH1GMtrTZM35g3BA955ljztszjPT4l0Gw2hz7R3GQZqI3ewDJ545SVjkTvH1uNuwAXaWTMX1mMFvAE6ZDtzOeznKxJUxRsTYpP36oghlmXh9FX7ghK-GkeCf432bLrum_i6Y1pPCvuuXCYtOZ01GXTrsZw66HFmvpGpGdLOJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a5f935a3.mp4?token=pRS8c5svERAtziApgbldYljxnzgnptaGvclY3CgmKMVzl0fJbwUsc44EiQgBgK4RoVezv5wKrPdZNaWrKNeJC89_trQZjGxwl3DRj_DDikkKPf0Sh3hHCh-t6umn2l3ps37FzBz8j_NLMizCUVPJTz-Mh3Hp21lUd_8ThFdWeIepvFH1GMtrTZM35g3BA955ljztszjPT4l0Gw2hz7R3GQZqI3ewDJ545SVjkTvH1uNuwAXaWTMX1mMFvAE6ZDtzOeznKxJUxRsTYpP36oghlmXh9FX7ghK-GkeCf432bLrum_i6Y1pPCvuuXCYtOZ01GXTrsZw66HFmvpGpGdLOJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
کارشناس صداوسیما درباره نتانیاهو: نتانیاهو خیلی مرده؛
همین الان آماده ترین عنصر برای حمله‌ به ایران اسرائیل هس نه آتش بس میفهمه نه خستگی
نتانیاهو مرده واقعی هس نه پشیمونه نه خسته این همه زدیم سرش دوباره فکر حمله داره
با خودش میگه تا وقتی کله زرد توی قدرته باید ایران صد در صدی رو به زیر صفر برسونم
به هیچ قراردادی پایبند نیستن و چون ما براشون تهدید موجودیتی هستیم قطعا اقدام میکنه مجدد
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/70367" target="_blank">📅 16:33 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70366">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCo4wzzzatYVFcJ7s_IUz7YMyyGiLv8yopgQEJsTWtyYmQK28spyfVv69TT8d4WJilw8IKpv2WnjD8C6J3-ANm-x0pCt1Hr7AvcA1DFudO7oTU3V9JcJkIZwoLG0TrB1o-s918XbXEVzxZ03zBn9CHp6Li_Ly0TBjQbvPaNd5IBUPu7X6ezE1wrIwO6Hx6noWVBjX6dGt6R8x4p6uC-vwx9ykfBtNakq7Z7jTBy9MpuNmwW-w7fUNo3waoPIp_bRmqfLM7Rb9hjBkReIhtTqyUZi8qA_P0WA01eYsW_z0ewwvEJK5gMmW7f9Q8FMzEdYbcvsrA6JMeCCSPJuM09D-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
پزشکیان:   درباره هزینه تأمین سوخت، چه کسی گفته دولت باید بنزین ۱۳۰ هزار تومانی بخرد و بعد آن را ۱۵۰۰ تومان بفروشد؟ ادامه این روند، منابع دولت برای افزایش اعتبار کالابرگ و پرداخت تعهدات مربوط به گندم‌کاران، بیمه‌ها و معیشت کارگران، بازنشستگان و کارمندان…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70366" target="_blank">📅 15:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70365">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">⏺
🇮🇷
پزشکیان:
درباره هزینه تأمین سوخت، چه کسی گفته دولت باید بنزین ۱۳۰ هزار تومانی بخرد و بعد آن را ۱۵۰۰ تومان بفروشد؟
ادامه این روند، منابع دولت برای افزایش اعتبار کالابرگ و پرداخت تعهدات مربوط به گندم‌کاران، بیمه‌ها و معیشت کارگران، بازنشستگان و کارمندان را محدود می‌کند
.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70365" target="_blank">📅 15:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70364">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfcIEtr76ZHgiTi5nj6tZCplKerzxkt98EHoifOrWD36PPKCasCOllxT_DMihZns0ngASXXVzuU2mrzntqsSsqHB7YNERXs5Ln2swutwSDdztnKfOwuR189mLpcgPq98Ixe3xpxhxc4tK1__vgufbIZU-DLS1xtqKh3EQLxVEvA6kKrrSOD4A3MGxRKOpr50cRomj5To6L0qgYWx_4lP6VLFcWsujF8QC5V0KjIkD6WF0pVlqB7I_0-cAyIswLi8cOO84KEYdn4g3NB4VoOuVnT4tVttBYuXyicdmJHjE8BghkZPT0vE6jPVQMeN09Oepr04t_7jvEUdr2lJLYp7Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
مسعود پزشکیان:
بهتر است جنگ را امروز، در حالی که در موضع قدرت و عزت هستیم، پایان دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70364" target="_blank">📅 15:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70363">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/356ce94a67.mp4?token=IGFGKWx48UDRkPM2y5Tuh8VjY4Q5w7Qgl1mQG5PxuY6cPRIP2WNLxVNDKY7u02C7zSfj6CRb51eqYhG9hwDb7Ls_8RSGdcHw0JwL7k3bW5c86UFaiU19m4rEwy3aku0sYxtzoXjHVhVyIr_iA_aKBQSlarC-SUlrTqQs7SUIR1ltJZjun2zWG1mNf9umkGcd2ogmjVK2eF-r1jwXJRgyLqjX4Br3U3RW9seFwQnNqrIt5e4yzvIiNic3K8aZ7F7XM_k4P95ti2safxZAKp_qjKNVs01m5LjqRMG0_ahnjt--GjWDP2N5QkY3N5BzIJSWhItVi0q908z2YKzh6OzNvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/356ce94a67.mp4?token=IGFGKWx48UDRkPM2y5Tuh8VjY4Q5w7Qgl1mQG5PxuY6cPRIP2WNLxVNDKY7u02C7zSfj6CRb51eqYhG9hwDb7Ls_8RSGdcHw0JwL7k3bW5c86UFaiU19m4rEwy3aku0sYxtzoXjHVhVyIr_iA_aKBQSlarC-SUlrTqQs7SUIR1ltJZjun2zWG1mNf9umkGcd2ogmjVK2eF-r1jwXJRgyLqjX4Br3U3RW9seFwQnNqrIt5e4yzvIiNic3K8aZ7F7XM_k4P95ti2safxZAKp_qjKNVs01m5LjqRMG0_ahnjt--GjWDP2N5QkY3N5BzIJSWhItVi0q908z2YKzh6OzNvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وایرال شده از زنی که با اسپری عکس زنای بدحجاب تو لندن رو رنگی میکنه مردا تحریک نشن
😳
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70363" target="_blank">📅 14:16 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70360">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uc5EjcVgtx-SbpTngvGCggtKk3wh6gOeIr4uG6-YchOXlWQ6Rr5YUlL-WEEuuLdrnewdw-RqIGgSfOnOCYG9IiVia-8Mr5MjhWj_WGgIk7kS2j42IoIVXXvjVyCtgjRNm3lZ2IChXe4cPMd57cqhMhRkl_3Qebwa6o5_0swc4dSbKgg6ViMjuW8L-hzKXpg3sp-YVppZDbs1CDrA24GvC-BQPrxE1P3T-XgJbiweNoVZrB1ZXIkpwy58n_ryEx2WoGHDeV_pIsi1z9s5d4EvT_HsZNyFTAfdi2VxkM-BZVj5IyB3glDFQXpabTQgqnzVP0UA6r3d3xmupwmJgSM6Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aNCOr5rqSHaUOTcTbdBvPcndfshJCTf5AMp6grwuGzjRl-k6UAYMimpQUfLIIiM9UegM03EIOnPXs-vPsjAGrj4xp5gTZ9YWodWKh4h-weO2t2l65NgkgbO2vD70vfoIN4nHjVsw4N7mmiYVndRUUP4jLVJT2EBsg1aXCPdZhi2sIFuBz1d8sBmd1nPbp_4qUe4JRPTDcVKRfwDNiTjWxZxMN1RcsW2w97Fb6gpYe1WLu4lYchfhrEpGWgaHFqyHi7pjni95T-pLk9dfYZQSN-fLn-G9qqMyxAvIUYjtn_tBsiyjZ6_NcMdNwKAUtwdWJAK0Aqhlp1-sulFmZqDZhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GXUHiAZDy_3FZ8V9gTDIhdLmgpS8riexxPueJLg2v3Twh7SY-Osfz4idKSE_Xbo-vKnj6mL61qmqfgGwwfk-rpB5miSNeVeQrFe2Brr5zU_FcrkuA3HaCTpqfuPRl9MDrmg8DhIBlxblILkz9dmlU4R3ttPQ4A7LYnBg2FT-7qdjLhsKkQOfgVzeWG7OMGHgZU4Y7BSRKn55ZlCU-N2sDcxEXlVB6fKnSW0MTPXM0_Sm9paTLTWaEnWDSQVHhEjwNBIkpESrXw4zRFOqeQYJukx4-4KsgfRGEb2dOE0c9x4R-Z_WgXsiDiu5qnLSlSeuUAxeh-ZJJQ3n1FlMRCT_iA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💢
🇮🇱
حملات ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70360" target="_blank">📅 13:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70357">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D8lnjOKOGHHPgcv3S5JRJzbO3-wTyiP79VIh8OC2iLF9nxRlXws3wLRbQw6lRKtTP-v0f5U2AjTsFAAPmKkcDqPQLV-ravRSpMzVW014AfEY1q_2qvcnZNX-EJIdwWu8JTOI5mxb4RASynyVfBBnp76eYuKB7RGQjYX9bAo7jkWFH1u4hMkcPP7-6NVcO9f2CF9kHRHqOGNy5H1h5C-HKaP7ocS-J2waEGiI71rJ78qzLs2EZMxx3TAFzXlstK8iishs3C_4wc2iRVJDnqbsE7i4TtNBoLwDn5WN8yLDtxcILpsLcXdogn7t9U-7GFBbM7LVSVP2mUWO9rY5kYtAtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86f5f06d38.mp4?token=IhWIS4obkJvSKulxLBoybIa2EaWoB6iXE3JLTof38DAcWNe2WokC1UQnKTgWqVOU_wv7R6kaoNxcaeNLBwkyjKWBrbibYc2XBV34t1n84_meqGb5AKNCcKYAum1KwTWmQMVBe3YrAeOWCVMOm9HMHW3eh5pUeXU9IZ4VL-ppC4T7MdIWx5Sax1z4z00nib130U2IPRVLGKjqroufWH_LIlq5dNf9OE3yqGJcp5N-NMaLpyi1vVYCKl0yp3udtvS48i_RsD5FbxuKdHpl5Fg2-mOP7w1RAxl7awOXJGm_soSs0YQWWlruZTj204DiVwMB1ZOJllTR_jpMYr8NJzk8bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86f5f06d38.mp4?token=IhWIS4obkJvSKulxLBoybIa2EaWoB6iXE3JLTof38DAcWNe2WokC1UQnKTgWqVOU_wv7R6kaoNxcaeNLBwkyjKWBrbibYc2XBV34t1n84_meqGb5AKNCcKYAum1KwTWmQMVBe3YrAeOWCVMOm9HMHW3eh5pUeXU9IZ4VL-ppC4T7MdIWx5Sax1z4z00nib130U2IPRVLGKjqroufWH_LIlq5dNf9OE3yqGJcp5N-NMaLpyi1vVYCKl0yp3udtvS48i_RsD5FbxuKdHpl5Fg2-mOP7w1RAxl7awOXJGm_soSs0YQWWlruZTj204DiVwMB1ZOJllTR_jpMYr8NJzk8bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رضا گلزار تنها رولز رویس کولینان منصوری در ایران رو به قیمت 100 میلیارد خرید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70357" target="_blank">📅 13:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70355">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ee66c3b75.mp4?token=MGvgNNo3BvEHFrgkgpnRLJzeEeqssc0vRVrP4OYhUd1AWJxV8v1BXJgab8pKEdShr76_Leh7AwWVNx__5DXWHgS47AmEj0gkU9xu_yA5YTS0kp3x3A89ISDc6ZNz-zXhqORoA_XwaJJDJaFUFhTrCkk_gjVyvsc368mRAOndMw--vk9Zzoa7SS9YhuhXfFBm0gheEFXnEHR1bQhioB4B7iP1RbfB2yPyn3dStk7SPFSCr89xvtaq5oh4JccaA8JazXrimpeqAiWtINv5jKj184W6xuyon62RfzrcMidXp-iYg7h262B8-b4ZzvUKu2ojmDDXxhT1ENbQaw8Vnt729A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ee66c3b75.mp4?token=MGvgNNo3BvEHFrgkgpnRLJzeEeqssc0vRVrP4OYhUd1AWJxV8v1BXJgab8pKEdShr76_Leh7AwWVNx__5DXWHgS47AmEj0gkU9xu_yA5YTS0kp3x3A89ISDc6ZNz-zXhqORoA_XwaJJDJaFUFhTrCkk_gjVyvsc368mRAOndMw--vk9Zzoa7SS9YhuhXfFBm0gheEFXnEHR1bQhioB4B7iP1RbfB2yPyn3dStk7SPFSCr89xvtaq5oh4JccaA8JazXrimpeqAiWtINv5jKj184W6xuyon62RfzrcMidXp-iYg7h262B8-b4ZzvUKu2ojmDDXxhT1ENbQaw8Vnt729A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو تهران یه دختره بخاطر اینکه دوست‌پسرش باهاش قهر کرده؛
واسش مرسدس‌ بنز AMG GT 53 4MATIC+ چهاردر خریده که شاید آقایی آشتی کنه
😶
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/70355" target="_blank">📅 12:26 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70354">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/news_hut/70354" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/70354" target="_blank">📅 12:26 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70353">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6m9_EUqzYpThWfARGNhCIvwGqeS_FrLFFaq3xfGnUkojLVBY-oQjM1m1SNzORxWXkGXBYeE8Cg_rrDkndMDapG7uHcNS6aLydCB9Mme5GJli_sBT8HuEpk7KA_zubO_dEvUnvB6yRljlZLqN2gn-Xn5OvJSkdUip4hP8RpXQWLYVWF3Zsqt8X-Hj9YQPyC_Oy4AaDg2a1GefiLeYkKofSYDAtBduODTWXbKPFbblFTvco4uhgYS5x7NSdbX7JY6L9nxNpdSFLeNAx1n93G41rErcV20uZISOEEa35HU-ko-MO7_9FeA40ICbQcTSfuteSkEviK24aAfip9UmfmWsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
سایت جهانی  و معتبر
#Melbet
🔴
بازی های مهم 27 مرداد
🆗
ثبت نام آسان و سریع کلیک کنید
🆗
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
پخش زنده ی تمام مسابقات
✅
درگاه اختصاصی برای کاربران
👍
پشتیبانی 24 ساعته فارسی
🎟
Promo Code: MELBET90
🇩🇪
دانلود اپلیکیشن MELBET
📱
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r30
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/70353" target="_blank">📅 12:26 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70352">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3219c52e1.mp4?token=l_wvl0qvkCVV7bva2nHztL5WxKKY6-OLRtFwSuuTv-4V87tivLWOdbLN6i-psANSLoricVXvgL1bkYq7chidbraGIsHslkSZD9QMBl-Qb-825RRCeEhpssbiyHw4zdzfovMBlC8CGDcWrwCQ1DtOFL-2HFGTtMMRaLRyWa6KE2NVzkHW0QFaNIiGw10PJarDs0xs1EfAZ5kioU1-c2qRXhue8NtS6-QyAfifnzPQsGnO1jEvzZpJJILR1WTrK8aKcCctLXlKYEawCre3Ei6CyFKfPNeM-ThRnlVc3IS1xY9zEPF_awN1T1l9yq8hTzA_8otcsdf4JVdVq8EWga_efg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3219c52e1.mp4?token=l_wvl0qvkCVV7bva2nHztL5WxKKY6-OLRtFwSuuTv-4V87tivLWOdbLN6i-psANSLoricVXvgL1bkYq7chidbraGIsHslkSZD9QMBl-Qb-825RRCeEhpssbiyHw4zdzfovMBlC8CGDcWrwCQ1DtOFL-2HFGTtMMRaLRyWa6KE2NVzkHW0QFaNIiGw10PJarDs0xs1EfAZ5kioU1-c2qRXhue8NtS6-QyAfifnzPQsGnO1jEvzZpJJILR1WTrK8aKcCctLXlKYEawCre3Ei6CyFKfPNeM-ThRnlVc3IS1xY9zEPF_awN1T1l9yq8hTzA_8otcsdf4JVdVq8EWga_efg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اوه اوه اجرای بازی "نون بیار کباب ببر" بین دو نامحرم تو برنامه‌ای که مجوز وزارت‌ ارشاد رو داره!!!
همون طور که ملاحظه می‌کنید، چندين مرتبه دستِ این دو نامحرم حین بردن و آوردن نون و کباب به همدیگه برخورد کرد...
پس چیشد آرمان‌های امام؟!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70352" target="_blank">📅 12:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70351">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10c0b55713.mp4?token=PCKbSwRBy7arQx8BLReAy3NLXga8DRpaI7gMPlhRtYqUp7qQ3W2SbRpL80o6c9QA1U4IaQF5QJprvTx6L8B3CyuSgPd47eLjzMqJF0dE8Ue0QPynCZ6JIrz2B70L46P232A6LV193jElo56z5Keln39uGwC1uZZD3nyZQlb5sP3_t_YC6WT9QwjqdINm9dPZoSYRZYBk5e0HdN9EQjValtQgU5YYUYBPPUUmq04s4jEbloNk0ABz2oOCzCy2TqhwEbQmLHB8P4MwCKyagyr0zcSjADmcHtCpARX6UJJy4adzLrsyEDnUr-yP0yXvJJu7zmQog2d64K0ljrO2JU98MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10c0b55713.mp4?token=PCKbSwRBy7arQx8BLReAy3NLXga8DRpaI7gMPlhRtYqUp7qQ3W2SbRpL80o6c9QA1U4IaQF5QJprvTx6L8B3CyuSgPd47eLjzMqJF0dE8Ue0QPynCZ6JIrz2B70L46P232A6LV193jElo56z5Keln39uGwC1uZZD3nyZQlb5sP3_t_YC6WT9QwjqdINm9dPZoSYRZYBk5e0HdN9EQjValtQgU5YYUYBPPUUmq04s4jEbloNk0ABz2oOCzCy2TqhwEbQmLHB8P4MwCKyagyr0zcSjADmcHtCpARX6UJJy4adzLrsyEDnUr-yP0yXvJJu7zmQog2d64K0ljrO2JU98MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دیروز تو ابهر - زنجان ، دوتا دختر نوجوون اينجوری با موتور صاف رفتن تو دلِ تریلی که پارک شده بود!
جفتشون مصدوم شدن ولی خداروشکر آسیب‌ها خیلی جدی نیست...
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70351" target="_blank">📅 11:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70350">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab8c63c27e.mp4?token=f3WRbBd4h8MrEIIAzGInvT_Rd1tFVIXxRpI-h50bnnLewjtHBYWHuliSUMP1YiP5alrXjFbn3WV-_ozACpYhs197TqzAhp-Z1atCGA6lYtANFSADFBWQmsS6Gvde-t-tXW6HmftoOBYZerPk8pW2_7SRmpeU6ZPYd_I29IohicsLaVHx4E3bWsUNvYyWeCZVT73rgiZkek43EYNpNLsFHSj4-dZPa2iGTY1GlQa-Cqe1gQCVmn1KpWK0vGkHmI5EMwwVp6cxxAYEdSFLlEPWBNf7PXG9BiGAd6pikF6s0LbPF1dXJYGMsk58J0oY6DijwxFBRf2R9Y-RmyjVZg6UdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab8c63c27e.mp4?token=f3WRbBd4h8MrEIIAzGInvT_Rd1tFVIXxRpI-h50bnnLewjtHBYWHuliSUMP1YiP5alrXjFbn3WV-_ozACpYhs197TqzAhp-Z1atCGA6lYtANFSADFBWQmsS6Gvde-t-tXW6HmftoOBYZerPk8pW2_7SRmpeU6ZPYd_I29IohicsLaVHx4E3bWsUNvYyWeCZVT73rgiZkek43EYNpNLsFHSj4-dZPa2iGTY1GlQa-Cqe1gQCVmn1KpWK0vGkHmI5EMwwVp6cxxAYEdSFLlEPWBNf7PXG9BiGAd6pikF6s0LbPF1dXJYGMsk58J0oY6DijwxFBRf2R9Y-RmyjVZg6UdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بعد از تبرئه پژمان جمشیدی؛
حالا دختری که مدعی شد مورد تجـاوز قرار گرفته به برنامه‌ یوتیوبی ترانه علیدوستی دعوت شده و ادعاهای خودش رو مجدد تکرار کرد
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70350" target="_blank">📅 11:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70349">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f25ab02a82.mp4?token=tytDD9-_YErJ6DSPaLz0MBwTH4Ok--nwj_4Dd7W_I68jWfDv8fzTPw5nTb9PmqzVuUQe7-AXTnjBfR8iwcKMtujVsOocIxGXwCokO1kKrIe7hD30FuCDCVe9rP6sI2z1FJFF6xrsX4Qm7hZRz-xJ_fiK52N5Q8M92ok2HCbfk1zM9K4htIkg-K-MXiTA4Td0Mo06n0L2fxqpeL_VCA1jMYo6wFlRR2rSPxh3JzVORJKTaOoBdR6_djl8uQio8OQHMK-4PW_LqD3i3qybZodg9sBtp5dYpT7ifwRxGXDoc4N9rI25PNarH4AJKfyIX7OeTKC1rkJ9GoIbQko94AcHQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f25ab02a82.mp4?token=tytDD9-_YErJ6DSPaLz0MBwTH4Ok--nwj_4Dd7W_I68jWfDv8fzTPw5nTb9PmqzVuUQe7-AXTnjBfR8iwcKMtujVsOocIxGXwCokO1kKrIe7hD30FuCDCVe9rP6sI2z1FJFF6xrsX4Qm7hZRz-xJ_fiK52N5Q8M92ok2HCbfk1zM9K4htIkg-K-MXiTA4Td0Mo06n0L2fxqpeL_VCA1jMYo6wFlRR2rSPxh3JzVORJKTaOoBdR6_djl8uQio8OQHMK-4PW_LqD3i3qybZodg9sBtp5dYpT7ifwRxGXDoc4N9rI25PNarH4AJKfyIX7OeTKC1rkJ9GoIbQko94AcHQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
کارشناس صداوسیما درباره علی خامنه‌ای:
رهبر شهید یه پله از امام معصوم پایین تر بود هرحال هرکی نمیتونه نائب امام زمان بشه
خداوند متعال خامنه‌ای رو تو انفجار مسجد ابوذر برای ملت ایران نگه داشت
اما تو ۹ دی(منظورش ۹ اسفنده) اون همه موشک خورد به بیت آقا که خدا رهبر جدید رو به ما بخشید
اونجا هم خدا مجتبی رو از شر موشک ها نگه داشت
خدا خیلی حواسش به ما هستش اگه ما بهش حواسمون باشه
موقع جنگ رفتیم نماز با حضرت آقا یه آرامشی داشت یه جلالی داشت یه شکوهی داشت بی نظیر
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70349" target="_blank">📅 10:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70348">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ced1bea644.mp4?token=BXBBExVhNRqS4L_mPmbcmLj1wUBbCzXMro91QTfkIZPCpHivBriJyOf5MSOkhmj3LkQJpmOxsKCf3AAxHUmlKjZhA2GHPxEWMsEUagv9erHd_VQXW-y5wUBdtPCTA0BhTDUaH6sCV3xHF-vXJH_5zn3bHg7P_E_ZcyXkBfqo6w1w7aRex2-ipqSYWfVipjQzr7I0r5Ezo0vyIGPMOk-RcFpsouEY65u-_BOKLgNGgIvqjRB9_4ZXnH_uo0PYfvJHVGSni2nvsUw_nVJGUsJScd_0ZJTrsKX0LN__dHgtKUPIEOQIo-5wB-4AesCxZcbXYmbYoNfwrF3BzvFUPzUn0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ced1bea644.mp4?token=BXBBExVhNRqS4L_mPmbcmLj1wUBbCzXMro91QTfkIZPCpHivBriJyOf5MSOkhmj3LkQJpmOxsKCf3AAxHUmlKjZhA2GHPxEWMsEUagv9erHd_VQXW-y5wUBdtPCTA0BhTDUaH6sCV3xHF-vXJH_5zn3bHg7P_E_ZcyXkBfqo6w1w7aRex2-ipqSYWfVipjQzr7I0r5Ezo0vyIGPMOk-RcFpsouEY65u-_BOKLgNGgIvqjRB9_4ZXnH_uo0PYfvJHVGSni2nvsUw_nVJGUsJScd_0ZJTrsKX0LN__dHgtKUPIEOQIo-5wB-4AesCxZcbXYmbYoNfwrF3BzvFUPzUn0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلم وایرال شده از یه چوپان که توی پیجش منتشر کرده و میگه:
بنده مرتضی ریدم تو مملکتِ جمهوری اسلامی، ترامپ سر کیرتو میبوسم، بزن که خوب میزنی
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70348" target="_blank">📅 09:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70347">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ac295420e6.mp4?token=nS5YK9J6sTsk58TQjS102wPas1oofKroSJsArX57zYzLYp0G6MDG5zd6T2FZAf2NWnV6S29PoAnQTnXOO0H72ILIJQn4yP7ZVjMX-zhuL1Skl5lO9uZVN5Gz8jZNCm34As7yvo-VxvPXlST7XkkBnJlQ5yIn2iixhMPbqCzoPKyCr5i2Yu3tb87bS69bXf6thBNCb2G5z9mJkRvC209-tdXoPgPxIChVaFu_HmUOhxeMIPPRmIprJxGJctGCId9hbyOhS6ahv2WBs-3PZdMFy5bKIphOlCv3Z5MT4mJlFQn5j2xKrLSW_yPDGsebHr_iBIQuLZoLYZ5vj-ay1zDzbw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ac295420e6.mp4?token=nS5YK9J6sTsk58TQjS102wPas1oofKroSJsArX57zYzLYp0G6MDG5zd6T2FZAf2NWnV6S29PoAnQTnXOO0H72ILIJQn4yP7ZVjMX-zhuL1Skl5lO9uZVN5Gz8jZNCm34As7yvo-VxvPXlST7XkkBnJlQ5yIn2iixhMPbqCzoPKyCr5i2Yu3tb87bS69bXf6thBNCb2G5z9mJkRvC209-tdXoPgPxIChVaFu_HmUOhxeMIPPRmIprJxGJctGCId9hbyOhS6ahv2WBs-3PZdMFy5bKIphOlCv3Z5MT4mJlFQn5j2xKrLSW_yPDGsebHr_iBIQuLZoLYZ5vj-ay1zDzbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پسر بچه به زیباترین شکل، جواب اون مجری که گفت جنوب ایران فدای جنوب لبنان رو داد.
نسل جدید آگاه‌تر از چیزیه که فکرشو می کنید!
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/70347" target="_blank">📅 09:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70346">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">📊
تحلیل فوتبال فقط حدس نیست؛ آمار، ترکیب، انگیزه و فرم تیم‌ها مهمه.  در کانال ما بازی‌های مهم ملی، لیگ‌ها و دوستانه‌ها رو با بررسی دقیق منتشر می‌کنیم.
🎯
انتخاب‌های پیشنهادی روی گل، BTTS و بازارهای مطمئن‌تر  عضو شو و قبل از شروع بازی‌ها، تحلیل رو ببین.
⚠️
…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70346" target="_blank">📅 00:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70345">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=ivkY1acqj9j5Qj7iO3aZWTNdgRierTTmy1BusxfgYSOkHAP3fbnJF5z2CYVhm0DNpiumOdEOWH9pWbZC_8aYU1c9Q2xUktEE3YteH5dTNcMjeXUau1RmuvXgrO7ZYrksBKx0dzPEPbWDiAvLpUqZ0pCZ3lwOi7y4RLCZlVdGZnhgVVbhbFNY-UQhNHhT7itJVvYHeecrH_9qJtV5mmiFtZBarERXfSB32WZR6ZkZ4d4WNUbcCgBcVpnkCNEY2jR1BDZkSwE4X--gMv9NnQDBlS0t3IrCXTjNwE4DVzH0JPCCgoaPNeWU_nOECEWf0pdJSq_mKYDQFJxaZt2bprX7lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=ivkY1acqj9j5Qj7iO3aZWTNdgRierTTmy1BusxfgYSOkHAP3fbnJF5z2CYVhm0DNpiumOdEOWH9pWbZC_8aYU1c9Q2xUktEE3YteH5dTNcMjeXUau1RmuvXgrO7ZYrksBKx0dzPEPbWDiAvLpUqZ0pCZ3lwOi7y4RLCZlVdGZnhgVVbhbFNY-UQhNHhT7itJVvYHeecrH_9qJtV5mmiFtZBarERXfSB32WZR6ZkZ4d4WNUbcCgBcVpnkCNEY2jR1BDZkSwE4X--gMv9NnQDBlS0t3IrCXTjNwE4DVzH0JPCCgoaPNeWU_nOECEWf0pdJSq_mKYDQFJxaZt2bprX7lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
تحلیل فوتبال فقط حدس نیست؛ آمار، ترکیب، انگیزه و فرم تیم‌ها مهمه.
در کانال ما بازی‌های مهم ملی، لیگ‌ها و دوستانه‌ها رو با بررسی دقیق منتشر می‌کنیم.
🎯
انتخاب‌های پیشنهادی روی گل، BTTS و بازارهای مطمئن‌تر
عضو شو و قبل از شروع بازی‌ها، تحلیل رو ببین.
⚠️
شرط‌بندی باید با مدیریت سرمایه و مسئولیت‌پذیری باشد.
https://t.me/+nbm7Tb2pz8VjMDlk</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/70345" target="_blank">📅 00:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70344">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7469eeed2.mp4?token=v88ostxEANqwQ2HMFmERueW-z2RMDQyphKcerQsjh8IJ-H01KXtEaNNTI6_a1MG8kk9tFiy-Yz-lgJP9RT5HJWUm8Qc_oGBwbTxT-ZqR5d9v86xHxqrK4NBm4fJnrXG10n_3H-tdnW5NPNv-LRdjh2W2eSvyxZi_5YStcyLFUivsVLz_OHHq77VioU1Y7pW83sBt_3zqhfBb8w--sSfi3RVN8NBJ7FICBi5urTgFt8k7JoJodpluNQw4mG_AjyKJ_oLhPCcoBM82kwwNRzIBF2BqZJAm0BEY9IlKqdsLza6LuCScBYdv1G4LThfvdj0C5DbjdigNov_mKF_ykj1Bnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7469eeed2.mp4?token=v88ostxEANqwQ2HMFmERueW-z2RMDQyphKcerQsjh8IJ-H01KXtEaNNTI6_a1MG8kk9tFiy-Yz-lgJP9RT5HJWUm8Qc_oGBwbTxT-ZqR5d9v86xHxqrK4NBm4fJnrXG10n_3H-tdnW5NPNv-LRdjh2W2eSvyxZi_5YStcyLFUivsVLz_OHHq77VioU1Y7pW83sBt_3zqhfBb8w--sSfi3RVN8NBJ7FICBi5urTgFt8k7JoJodpluNQw4mG_AjyKJ_oLhPCcoBM82kwwNRzIBF2BqZJAm0BEY9IlKqdsLza6LuCScBYdv1G4LThfvdj0C5DbjdigNov_mKF_ykj1Bnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
آیت‌الله جی‌دی ونس:
تنگه هرمز اصلی ترین اهرم فشار تهران هستش
موثر ترین چیزی که فعلا داریم فشار اقتصادی هستش که به ایران اعمال کردیم
اونا هم به ما فشار اقتصادی وارد میکنن
بهترین راه راه فشار اقتصادی هس نظامی چاره ساز نبود و اونا الان زیر فشارن
ترامپ خیلی واضح گفته ایران نباید سلاح هسته‌ای داشته باشد
تاسیسات هسته‌ای اونا نابود شده ولی آیا دارن بازسازی میکنن؟؟
ما میخوایم یکاری انجام بدیم تاسیسات هسته‌ای اونا نابود بشه حتی شانس بازسازی نداشته باشه
افزایش قیمت نفت گاز تو آمریکا طبیعیه ولی به زودی پایین میاد
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/70344" target="_blank">📅 00:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70343">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
لحظاتی پیش صدای دو انفجار در سیریک شنیده شد.
احتمالا موشک شلیک کردن به سمت تنگه هرمز.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/70343" target="_blank">📅 23:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70342">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYleSyR9bb3Q8mMMYq6VZzJMXSm9-tVB0JjMoSs50c1aKHMFQSPofVT7IHbmQBlay28ZB8W95iJAqzLNFrgx9OjktpmZPW-rI8onHZXgkRO6i7EothzGHAf3J93vu6JfHFA-hcmGOE2zwErtd71vIVEONMcngNLqg8kaTAYVnExGbKfhZDzWpSyOYxGAcZispmNJQjIxPaeu4ubFIkgA8mKc1IXiCXUZK_o_nNAbvsNLA0gJ6xT2dmibKKcF4ms_hoxkyi0UsNldY7ygSeiQZjIU_edLC7AE4v3rYZee8T6JTIRLiTHJruWwL7bKpGQsgT95FnsnATUsi3Ve2vyjMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
پلتفرم X زیر توییت رئیس پارلمان عراق با عنوانی جعلی برای خلیج فارس، یادآوری کرده که «خلیج فارس »درسته
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/70342" target="_blank">📅 22:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70341">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/264b3e2171.mp4?token=OxuZ5TeOoFE5o8t0AX1tudu1isXw7a17YTC5j9AlC84EYkfiUKJeZsyLpcq3sEW9or3Kk4wKpD18UsJleUykjhR_Mh3_ul6uK4hPzBg9jAM9x14khC3jkj6KDEabB-WX7_mAGyuX2VkOR2XqSiydjllR85qQ0t7Rjc6X_8ds06FM0Wg3BKcJADEL8Pvibda6oNe_4vCNtxb3WhGyVYwKnW8oLyZpOpL9S-9VTfKzSN7Wg-Z5j7vFq22RD2K2er8UXhn1vCx40Hi4YPbOP3fiiETZ9dJwbQXs0lnmp2Ur-RsUdfzAFAEfMZLq0xb0OhPufs0oXZtCZTT0xQ2JNHTfMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/264b3e2171.mp4?token=OxuZ5TeOoFE5o8t0AX1tudu1isXw7a17YTC5j9AlC84EYkfiUKJeZsyLpcq3sEW9or3Kk4wKpD18UsJleUykjhR_Mh3_ul6uK4hPzBg9jAM9x14khC3jkj6KDEabB-WX7_mAGyuX2VkOR2XqSiydjllR85qQ0t7Rjc6X_8ds06FM0Wg3BKcJADEL8Pvibda6oNe_4vCNtxb3WhGyVYwKnW8oLyZpOpL9S-9VTfKzSN7Wg-Z5j7vFq22RD2K2er8UXhn1vCx40Hi4YPbOP3fiiETZ9dJwbQXs0lnmp2Ur-RsUdfzAFAEfMZLq0xb0OhPufs0oXZtCZTT0xQ2JNHTfMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف، اوایل تیرماه:
خودم رفتم قطر، با امیر قطر صحبت کردم و 12 میلیارد دلار از پول‌های بلوکه شده ایران، طی تفاهم‌نامه اسلام‌آباد آزاد شدن.
🇮🇷
همتی، رئیس کل بانک مرکزی، دیشب:
هیچ‌کدوم از پول‌های بلوکه شده‌ی ایران هنوز آزاد نشده و همش شایعه‌ست.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/70341" target="_blank">📅 21:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70340">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFlFiQB9nvH1qVFbGoLkjYkgmGckKfNJ5cF8dyCq4NucD_RUrVZfOWroyDv5CsnHYkVMrz2zVCt2K6HXVAVBO75PAM34rvMVC5uIzjopnIyNY1aSz-2HVs_QAuu9BpdFucOT7nTYfMJAvKicnflI-HjHnEKA8IamhmGtp1sr0Lb2oBFxLV0cQpMOlWIJOCeTOwVt1eYwOWgvseMG0glol9RS5XzbZCCzGW1KortVJfJ7r64Y1Bc1xE4soztiNwERxI3vQ82cW9zbVjfBDMTDZBrXV3fap_JHtmv93SbKSI31ytW5ZSu3w912f3-xKAWaW59IFJySs_DZtzrNQFv3Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بزرگسال‌ترین داوطلب کنکور ۱۴۰۵ با ۸۵ سال سن
😳
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/70340" target="_blank">📅 21:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70339">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7149fa402e.mp4?token=Im1GoiO6nqbeQtjKATtcMh7_ro1_F1aUGvxl5BdzMkFxHEq1w_io5Pc3MC7zBdVaK4f0m4YsB9UlxnFi6DRi8kDTLgpeavwl3p9kzOMCTiz-UkES8Du7YrqPZ7hKOHCWipZBxBUbyy33j8l2FGMuPm99eKQznPs37dfDo91ySgEorCAFJHoJVVX31ZRQQlDsNSgDtQeHzt1B8LM4F-0HrYvkMqN2sP_9h7Qci6OwUQe73WoBKy7TEeuWdkPu0KIcxGjEPMG020Wk0lluiXI6vkBqQHIW8cVJ47LPwoW4jcx_Nt5MZ47NlW-aE4Dmm6yLZuS30ifd4IjEDguYGu7mTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7149fa402e.mp4?token=Im1GoiO6nqbeQtjKATtcMh7_ro1_F1aUGvxl5BdzMkFxHEq1w_io5Pc3MC7zBdVaK4f0m4YsB9UlxnFi6DRi8kDTLgpeavwl3p9kzOMCTiz-UkES8Du7YrqPZ7hKOHCWipZBxBUbyy33j8l2FGMuPm99eKQznPs37dfDo91ySgEorCAFJHoJVVX31ZRQQlDsNSgDtQeHzt1B8LM4F-0HrYvkMqN2sP_9h7Qci6OwUQe73WoBKy7TEeuWdkPu0KIcxGjEPMG020Wk0lluiXI6vkBqQHIW8cVJ47LPwoW4jcx_Nt5MZ47NlW-aE4Dmm6yLZuS30ifd4IjEDguYGu7mTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
شهبازی مفعول :
نوید محمدزاده یه پست گذاشت زامبی ها ریختن سرش
فحش و ناسزا و تهدید و انفالو که چی ؟ حق نداری با این زامبی ها اختلاف نظر داشته باشی
این وضعیت زامبی هاست
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/70339" target="_blank">📅 20:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70338">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e91c8463bd.mp4?token=korKnjF7wOIUgkJKszaQsSNuDs34VkEWqg-IZJYCXeeP85AYelYd47nQW_7F0KrFj0rd7ym66MpsBc3Z48f0VKQCmRONoRozBP9rKWokIst9wNRKZs-cf32TV5Fq9jpfH-bLEiDNyLjjw8YZIjfSUE2uAsGHK6k9EYZnN6UPcuYB6rFOYHcPJROYJEcyKga1870qsUx7u-eEI4jCN2VpLlzjTt6IZGweB2ylQ6_aoR_WHUAVVk6YFbrAm6Md42DC8FBk3UOEox0-xRyaCu_Obc1siAeW_VpXMcUN0Jc2nTS8HBuPAO4TcmNsYEBw6bRs2aQo659F6xLDRkYJhjTLRSYso8-SSOqu0Wi_HWhN0FFIOruHGGonxxKAAnMMtrZQ6Ihdn9KvY5XxVsBzhExC5R1XvG2HjXYm7v9XO72bkhuFGsPJMm6_qp0ev36H1MTvWpg4GR4bpZhkSqXDr4OsrJeqkoEHdN64T1H1tGfX7Qsusc99TefDwYG0VZmkOlImSJHt_6B88kAMwEuxgl8dYf-5Y86ok5F-jDTK2iEqfXdXK2bBnZ3jbPnwtXF1IS18CDN2kF4TYZzMAmSbBhDA6ZpBuffP9mQqyQWl8MxVgychInTD4KbUOFS1NrPx1azRZsxaIXFiuVBeQ6O_DLTSCsb8ljJyXnUxi1BLdcEt4Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e91c8463bd.mp4?token=korKnjF7wOIUgkJKszaQsSNuDs34VkEWqg-IZJYCXeeP85AYelYd47nQW_7F0KrFj0rd7ym66MpsBc3Z48f0VKQCmRONoRozBP9rKWokIst9wNRKZs-cf32TV5Fq9jpfH-bLEiDNyLjjw8YZIjfSUE2uAsGHK6k9EYZnN6UPcuYB6rFOYHcPJROYJEcyKga1870qsUx7u-eEI4jCN2VpLlzjTt6IZGweB2ylQ6_aoR_WHUAVVk6YFbrAm6Md42DC8FBk3UOEox0-xRyaCu_Obc1siAeW_VpXMcUN0Jc2nTS8HBuPAO4TcmNsYEBw6bRs2aQo659F6xLDRkYJhjTLRSYso8-SSOqu0Wi_HWhN0FFIOruHGGonxxKAAnMMtrZQ6Ihdn9KvY5XxVsBzhExC5R1XvG2HjXYm7v9XO72bkhuFGsPJMm6_qp0ev36H1MTvWpg4GR4bpZhkSqXDr4OsrJeqkoEHdN64T1H1tGfX7Qsusc99TefDwYG0VZmkOlImSJHt_6B88kAMwEuxgl8dYf-5Y86ok5F-jDTK2iEqfXdXK2bBnZ3jbPnwtXF1IS18CDN2kF4TYZzMAmSbBhDA6ZpBuffP9mQqyQWl8MxVgychInTD4KbUOFS1NrPx1azRZsxaIXFiuVBeQ6O_DLTSCsb8ljJyXnUxi1BLdcEt4Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
#فوری
؛اسکات بسنت وزیر خزانه‌داری آمریکا درباره ایران:
این مناقشه با ایران؛ ما از آن عبور خواهیم کرد. نمی‌دانیم چه زمانی.
🎙
خبرنگار:
آیا کارزار اقتصادی علیه ایران، چین را هم شامل می‌شود؟ چرا که چین شریک اصلی اقتصادی ایران است.
🔴
بِسِنت:
بسیاری از گفتگوها بهتر است به‌صورت خصوصی انجام شوند.
🚨
🚨
⭕️
بسنت درباره ایران:
ما شدیدترین تحریم‌های تاریخ را اعمال خواهیم کرد و به شما می‌گویم که این کار نتیجه خواهد داد.
این روش در ونزوئلا، پس از آنکه دست به محاصره زدیم، مؤثر واقع شد؛
هم‌اکنون در کوبا نیز کارساز است و در مورد ایران هم نتیجه خواهد داد؛
ما این رژیم را ساقط خواهیم کرد
!
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/70338" target="_blank">📅 19:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70337">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">💎
میدونستین تو ویپاری
با شارژ بالاتر از ۱۰۰ دلار ۲۰٪ بیشتر حسابتون شارژ میشه
✅
🎁
برای مبالغ بالاتر از ده هزار دلار بیمه شرطبندی ۳۵٪ داره‌
و مبالغ بالاتر از هزار دلار بیمه ۱۵٪ داره یعنی در صورت باخت مبالغ به حسابتون‌ دوباره واریز میشه.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70337" target="_blank">📅 19:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70336">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari (3).apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/70336" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر WEPARI
😀
😃
😄
😁
🔥
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 120% اولین واریز
‼️
🔥
بونوس برای 4 واریز اول
‼️
⚽️
بونوس ورزشی هر دوشنبه و چهار شنبه
‼️
🎁
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :
Gift
🔥
دانلود مستقیم اپلیکشن اندروید
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
📌
آموزش نصب برای IOS
g29
✔
https://t.me/WePariFarsi</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/70336" target="_blank">📅 19:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70335">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47dcddfa33.mp4?token=DEy7Fm6RrT_oSCXySR5DTO-E3I5BDjj5jAxVAydy8l3QwaGtoDaTs8PWGWCkvHFhV439ix8CRr7hO9VzBqXqO3IDoiliLBFnaL7jdliUeTnFm1KEHuPyFcosKjF90Myzo_ieIEMmxXI2CeAO9NL8FDd96eo0ZxrXpz8FM9fOARqkDt7jqjk2lg7nyji9ytZre4aVAtdvOAYoNfbhm8x0TaX_ra2kFW3JzngZVo_n9rvoFVFdBwQofpTN5kjSHU_4wuAww8qx2qRAjyjlmHIOE9EP_aOAurzcl0Ekk-52yCsymwbISaEJIh-Earf8nVRwhqZgsRxj43v879jPFgKvZSWjlF5vTrB89N802cwDB01j2IAxrA546GJEq5YHwgCDyskmtpgZPuuiJunT6RX3T8n7jft3VbSgQSiX3snEuRMwCVUtKn-5Mn2TQ9U2gpJbZhaJTD_5QPJuyL1fQ6LHwiJFOmfmUDxqu7z_nyNEnQ0__9dux-vNlVsB8zfQES4aLDMQuwJPWZNBHIqL3unKhfAardU6NQOA0U4_uswxmEJOJLbyduFq_9kKFmNUbmZ55my9Kv2YTjXadWpSceGTgQB103jP8bQWA4_YZAMZ6G1hXMqJAzhFQvAqmlyCiuQIQD4cocF794dzNC-uIjvvnMii5DnXG_4xM959eYf38Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47dcddfa33.mp4?token=DEy7Fm6RrT_oSCXySR5DTO-E3I5BDjj5jAxVAydy8l3QwaGtoDaTs8PWGWCkvHFhV439ix8CRr7hO9VzBqXqO3IDoiliLBFnaL7jdliUeTnFm1KEHuPyFcosKjF90Myzo_ieIEMmxXI2CeAO9NL8FDd96eo0ZxrXpz8FM9fOARqkDt7jqjk2lg7nyji9ytZre4aVAtdvOAYoNfbhm8x0TaX_ra2kFW3JzngZVo_n9rvoFVFdBwQofpTN5kjSHU_4wuAww8qx2qRAjyjlmHIOE9EP_aOAurzcl0Ekk-52yCsymwbISaEJIh-Earf8nVRwhqZgsRxj43v879jPFgKvZSWjlF5vTrB89N802cwDB01j2IAxrA546GJEq5YHwgCDyskmtpgZPuuiJunT6RX3T8n7jft3VbSgQSiX3snEuRMwCVUtKn-5Mn2TQ9U2gpJbZhaJTD_5QPJuyL1fQ6LHwiJFOmfmUDxqu7z_nyNEnQ0__9dux-vNlVsB8zfQES4aLDMQuwJPWZNBHIqL3unKhfAardU6NQOA0U4_uswxmEJOJLbyduFq_9kKFmNUbmZ55my9Kv2YTjXadWpSceGTgQB103jP8bQWA4_YZAMZ6G1hXMqJAzhFQvAqmlyCiuQIQD4cocF794dzNC-uIjvvnMii5DnXG_4xM959eYf38Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از یکی زیباتر و حرفه ای تر:)
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70335" target="_blank">📅 19:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70334">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e96e27ffe3.mp4?token=v47gEkP3Oi4Hqr7bKIDd2cUd1w3hTcL7tpgNF-Ercw2EVEt8NtLYhiGlIWrJq0bP1udC3r5-sfO78aHPuCBzbVtvcKveYwUinqjwyQQ0DTHlicru2VTKMBQbHZ4usLjoLjMcAzOSRzWnMRF1FmTawnEG729vPf5A7W1euWymjx9myBOT-iLsXeSS7H_rKK9CMq0jf545AjDD7IENMWaYBq2SPsbNWmDAfhgMMyvZS8zh8F6Wji5PV5SrTWPTg1sYIb66MlFJ6UAVrC_oIF2h0iF0CV21GbXkpMOWT1mDA9AedyfpWv1ys7ege7Cwg7tgH7w8zaXUmbce4H40llTsuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e96e27ffe3.mp4?token=v47gEkP3Oi4Hqr7bKIDd2cUd1w3hTcL7tpgNF-Ercw2EVEt8NtLYhiGlIWrJq0bP1udC3r5-sfO78aHPuCBzbVtvcKveYwUinqjwyQQ0DTHlicru2VTKMBQbHZ4usLjoLjMcAzOSRzWnMRF1FmTawnEG729vPf5A7W1euWymjx9myBOT-iLsXeSS7H_rKK9CMq0jf545AjDD7IENMWaYBq2SPsbNWmDAfhgMMyvZS8zh8F6Wji5PV5SrTWPTg1sYIb66MlFJ6UAVrC_oIF2h0iF0CV21GbXkpMOWT1mDA9AedyfpWv1ys7ege7Cwg7tgH7w8zaXUmbce4H40llTsuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
یه پسر دانشجوی ۲۱ ساله آمریکایی به کمک هوش مصنوعی یه مدل اونلی فنز به اسم «مایا» درست کرده و تونسته تو یه ماه اخیر ازش ۴۳ هزار دلار(۸ میلیارد تومن) درآمد داشته باشه
مایا اصلا وجود خارجی نداره این پسر از خودش فیلم و عکس میگیره و به کمک هوش مصنوعی به دخترِ لخت تبدیلش میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70334" target="_blank">📅 18:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70333">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3764b3347.mp4?token=qmqZgmLpGK0X7COBWUyPsMpfhTy6dZIU-kWT3zQEF-Qh6zvIkeUsB7obrSK9PIsl8dknYXoFJSTfi954wauAqWfvRmJIfF9xg80KMXFtcfP3FK3ZsPvTOIO03WeJKY1MGB2fUAltwIZAJz3wxIEZWkQXpa1Pvu-Okh7lsSA5b_V01VTvNfn9t56yExE5MyIJrfR7O71Zk2JAEsUwYMYpSqFWQFZf2PjioBPIsNh3Nwr7BN7ZQj0__S4kzZwIdLQrfEqemhZ6uw7NXFyqfytJElULMP4Wl7wOpocnbJcFMmPkUjsGgG6m3XbL6_uwRpKVyv8-Bsdwqca4lLMIbOoZEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3764b3347.mp4?token=qmqZgmLpGK0X7COBWUyPsMpfhTy6dZIU-kWT3zQEF-Qh6zvIkeUsB7obrSK9PIsl8dknYXoFJSTfi954wauAqWfvRmJIfF9xg80KMXFtcfP3FK3ZsPvTOIO03WeJKY1MGB2fUAltwIZAJz3wxIEZWkQXpa1Pvu-Okh7lsSA5b_V01VTvNfn9t56yExE5MyIJrfR7O71Zk2JAEsUwYMYpSqFWQFZf2PjioBPIsNh3Nwr7BN7ZQj0__S4kzZwIdLQrfEqemhZ6uw7NXFyqfytJElULMP4Wl7wOpocnbJcFMmPkUjsGgG6m3XbL6_uwRpKVyv8-Bsdwqca4lLMIbOoZEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این پسر نقش ترامپو بهتر از خودش بازی میکنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70333" target="_blank">📅 18:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70332">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed854f2c03.mp4?token=QTH19PSbzGSAX21lyR4QZwd8ehD5H714nw-mtAT6t6WMpgTgsJCGksvCqOTiUqDx-0pix8N7JrEZc1csjI6MhoYpbZsUVoae7roTF4FVgRv4kmMDGhgcCSrFiGFBc8l76kKfR7bNdli95YdOAJ9S8mRcnWhxQWUcihRTnDvAWS4FMWDxTwq1HtD8cSrVmUZkkiQCnljO9CwKSyQaohZLs3E6qEHfmC-SvyRBDUrlqqlSBe-jmfaNsNpGVazdmBfo_09g5dnn-Tny0QEpx_ERdriu9j7ScY2pfvzS3V6rwuI-9NsynpKlZ2kOSTkbKP06bH_stqF9WTwQmdr5wDMnuSEG8Wg2G95d1moasFkd4__bq33LPjjrrAr9dpbeXbP0dbaZou689FqScT56r3H3Gy9W-SLH-KbIP8O34wEH4ARiiiQgA9kpY_xiJxCKHz_s55KlCy2Z0rD4tzFZa4eL1EUmdtlN2hvGL4eGFEWXVc16MbNye8cAs_IG0pOiKJfbyfa80htAcTbeGWm5SdCt394NSaDTcLA3vwcF3t4Ed__glNHWS4TyJxI5rVhTcTdNpNcnIM0VlIAno7NCMGk2oMeyB0bxhxS8L-bqZqkhhtlNQ4MKenrxuDu9JG16OKBEOlmf2y8pb3YWbZO6nn94iQs0y3tvZg_1iGS5xhy1SKk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed854f2c03.mp4?token=QTH19PSbzGSAX21lyR4QZwd8ehD5H714nw-mtAT6t6WMpgTgsJCGksvCqOTiUqDx-0pix8N7JrEZc1csjI6MhoYpbZsUVoae7roTF4FVgRv4kmMDGhgcCSrFiGFBc8l76kKfR7bNdli95YdOAJ9S8mRcnWhxQWUcihRTnDvAWS4FMWDxTwq1HtD8cSrVmUZkkiQCnljO9CwKSyQaohZLs3E6qEHfmC-SvyRBDUrlqqlSBe-jmfaNsNpGVazdmBfo_09g5dnn-Tny0QEpx_ERdriu9j7ScY2pfvzS3V6rwuI-9NsynpKlZ2kOSTkbKP06bH_stqF9WTwQmdr5wDMnuSEG8Wg2G95d1moasFkd4__bq33LPjjrrAr9dpbeXbP0dbaZou689FqScT56r3H3Gy9W-SLH-KbIP8O34wEH4ARiiiQgA9kpY_xiJxCKHz_s55KlCy2Z0rD4tzFZa4eL1EUmdtlN2hvGL4eGFEWXVc16MbNye8cAs_IG0pOiKJfbyfa80htAcTbeGWm5SdCt394NSaDTcLA3vwcF3t4Ed__glNHWS4TyJxI5rVhTcTdNpNcnIM0VlIAno7NCMGk2oMeyB0bxhxS8L-bqZqkhhtlNQ4MKenrxuDu9JG16OKBEOlmf2y8pb3YWbZO6nn94iQs0y3tvZg_1iGS5xhy1SKk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صنعت خودرو یه جوری داره پیشرفت میکنه که چین عملا داره سفینه می سازه
:
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70332" target="_blank">📅 17:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70331">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1219ed44a7.mp4?token=ukuELIRzlPJgcZegCyy4Du_XZF39O7cqKtbAe9p52VNhYgm4ZWB32PjknSEijdUj47P57D7fJxJYfDzsyu4NuHMjgz1z8ivTN55-HkYY5Nm-z79_0TCCYou_7Tim9-IS8aTvfNI0kpQX83DJfH-1KFqEtO23XHtyef_4bzccl807NHiCY_rkur2ssdlLHMq3-jwMIMnnRI4eieoZVNbVi9msUBewDJUWoH7h-xe3pXCrceIogxZd-m5qEZiDLdTHqvpBWZwVMiNsSL4N_G_9wzyG7m0RfK9oW24HC122KJoV7aSO6miTod9B6LVv8Hy9qagIyfjjHDf_QMZmxZyG2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1219ed44a7.mp4?token=ukuELIRzlPJgcZegCyy4Du_XZF39O7cqKtbAe9p52VNhYgm4ZWB32PjknSEijdUj47P57D7fJxJYfDzsyu4NuHMjgz1z8ivTN55-HkYY5Nm-z79_0TCCYou_7Tim9-IS8aTvfNI0kpQX83DJfH-1KFqEtO23XHtyef_4bzccl807NHiCY_rkur2ssdlLHMq3-jwMIMnnRI4eieoZVNbVi9msUBewDJUWoH7h-xe3pXCrceIogxZd-m5qEZiDLdTHqvpBWZwVMiNsSL4N_G_9wzyG7m0RfK9oW24HC122KJoV7aSO6miTod9B6LVv8Hy9qagIyfjjHDf_QMZmxZyG2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇬🇧
🇺🇦
🇷🇺
پهپادهای تهاجمی ۱۰۰۰ کیلومتری بریتانیا، جنگ را به عمق روسیه می‌برند، مسکو به خروش آمده است
بریتانیا پهپادهای تهاجمی دوربردی را که قادر به دستیابی به ۱۰۰۰ کیلومتر هستند، در اختیار اوکراین قرار داده است، در حالی که طبق گزارش‌ها، پهپادهای ساخت بریتانیا اکنون در حملات عمیق علیه اهداف در داخل روسیه استفاده می‌شوند.
از جمله آنها می‌توان به نیان، یک پهپاد تهاجمی دقیق با موتور جت که توسط کالن لنز از شرکت BAE Systems توسعه یافته و طول بال‌های آن ۲.۹ متر است، اشاره کرد.
طبق گزارش‌ها، سایر سیستم‌های ارائه شده توسط بریتانیا برد بسیار طولانی‌تری دارند و تا حدود ۱۰۰۰ کیلومتر برد دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70331" target="_blank">📅 16:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70330">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4669764466.mp4?token=EI-1WVd3zzWnAqxKlcjWwWb3wnxsERZW55prh7YAG2D3NW24sWUjI_fkC7h2krOR9E5FGwwPGDa5WEjFEzpvvbxgX7CDbE9X3G48wGtpbOrRfouHMXpV8sQruukTzOlmp-XFvMjcaV1kSxViWJUrOvAVDEMr_oSuD2YcdnHh7SDU2hkfxlNmTd-xrcnoX2QH6q3ApkAY9j9yir68A-jG36qtQh7BTfTnoPMLgXBLjPy9csY3qCwwMsH0hbpjvNCGvKT_XAShpSv44u0lhiBks0eJHqv4pvcQ04gHGHjrKnhkiGpkAnVWc-B-1vUyEE4dIOyjm0Td-XuaaPJQHD2RkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4669764466.mp4?token=EI-1WVd3zzWnAqxKlcjWwWb3wnxsERZW55prh7YAG2D3NW24sWUjI_fkC7h2krOR9E5FGwwPGDa5WEjFEzpvvbxgX7CDbE9X3G48wGtpbOrRfouHMXpV8sQruukTzOlmp-XFvMjcaV1kSxViWJUrOvAVDEMr_oSuD2YcdnHh7SDU2hkfxlNmTd-xrcnoX2QH6q3ApkAY9j9yir68A-jG36qtQh7BTfTnoPMLgXBLjPy9csY3qCwwMsH0hbpjvNCGvKT_XAShpSv44u0lhiBks0eJHqv4pvcQ04gHGHjrKnhkiGpkAnVWc-B-1vUyEE4dIOyjm0Td-XuaaPJQHD2RkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
جوابتون به صحبتای ترامپ درباره تنگه هرمز چیه؟
🇮🇷
حداد عادل:
باید بگیم تنگه، تنگه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70330" target="_blank">📅 16:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70329">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhVDvQ-baiGoROXv1Sx7al70M7cDulEhuAIHQDhnDXUHiTcRrr66hQGaD64nQsSU5lZ3doKVLoWzVMVU7tdsUV6SI4It8B6wiv2MIr1-SxCS6kDAcmhZASGm_3w2hdJkozM15ZvD6S9jt-sAV6oJRsDD6GxomzkhEPDBY3j22HdB4-kCydfFu7rubDLwQ4iW_ZEaAFI0z8BPFR2zNyd3n-Q4zKhsBljeRw6cqkq-CEMQ2BgUCkdA8vssaJ6rmF1BBLsQUSLV_1p9Clj_2-4u6I5cHIdLO4fcng1XJPtB2sCE5ybmc7Ek3mC974OQV8WNGnb9ZO0azWk-QdBJy63wVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
〰️
فرماندهی مرکزی ایالات متحده (سنتکام):ناوهواپیمابر جورج واشنگتن به منطقه عملیاتی سنت‌کام رسید.
ملوانان آمریکایی در تاریخ ۲۰ آگوست، همزمان با عبور ناو هواپیمابر جورج واشنگتن (CVN ۷۳)، بر روی عرشه پرواز آن کار می‌کنند. گروه ضربت ناو هواپیمابر جورج واشنگتن پس از ورود به صحنه فرماندهی مرکزی آمریکا (CENTCOM) دیروز، طبق برنامه در خاورمیانه فعالیت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70329" target="_blank">📅 15:13 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70328">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85771a2a65.mp4?token=XOtfgB6S5FVovud5h4Vma0Fgu1afpfOkQ0Mzj2mfLMrq09BGlkMB0R-YdMVmrwxtdAzLD1kGdsZ1svOR3waZUw8c3EapjQdyGR1VaKpn1scMN21jiWWNQzQUIuDe7Jk3kF8H_kbyKL1gt3bOmERoEVMaRNlsY2Hd_TslNlhrNRphzZXSTwbxUNaUGgvWpy3w4KtQCFMC-0eV2DMxjatgx50EkRwAINM52ZwM1AULxykSq3B_hDPP3A27fQ6RypwWDT-pafn1PHZgA-wLAeLqa6wkG1vWoZizW_c5gu76_qXp29C596JnxTa47z7H66Hhot4E7Q8J5yc5HNY5esDGAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85771a2a65.mp4?token=XOtfgB6S5FVovud5h4Vma0Fgu1afpfOkQ0Mzj2mfLMrq09BGlkMB0R-YdMVmrwxtdAzLD1kGdsZ1svOR3waZUw8c3EapjQdyGR1VaKpn1scMN21jiWWNQzQUIuDe7Jk3kF8H_kbyKL1gt3bOmERoEVMaRNlsY2Hd_TslNlhrNRphzZXSTwbxUNaUGgvWpy3w4KtQCFMC-0eV2DMxjatgx50EkRwAINM52ZwM1AULxykSq3B_hDPP3A27fQ6RypwWDT-pafn1PHZgA-wLAeLqa6wkG1vWoZizW_c5gu76_qXp29C596JnxTa47z7H66Hhot4E7Q8J5yc5HNY5esDGAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
‏همتی رئیس کل بانک مرکزی:
یکی از مسئولین رده بالا که نمی توانم اسمش را ببرم، چون ممکن است ناراحت شود در سفر خارجی به من گفت که آمریکایی ها فکر کردند ایران هم مثل ونزوئلا یا کشورهای آمریکای لاتین یا جاهای دیگر است.
ایشان به من گفت که شما در آینده نزدیک نقش جمهوری اسلامی را در منطقه خواهید دید، خواهیم دید که در واقع آن چیزی که آنها فکر می‌کردند نشد و یک چیز خلاف آن، عظمت ایران را خواهند دید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70328" target="_blank">📅 15:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70326">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d602fb7461.mp4?token=AmiVsLCMiFoqHkgRgNV7aR2rrMdv17E26X0s986g8XL5VdUJ9ZeZPR5_TAnq2-uc1Y50dc3XjbFTnl46foTZ73HdbeeYJr1ON1smM8pho61_47H7h4CBTb6LqniSRu6vIsVhI3NPsDBRhoPd8PNeLkpvCLIOFXON_5PiyqTDbS9X3UxP3F1W5o7d0QQ1t4BLZSn-4hWZryKkHrmDbVX6RWUmiq7Gg4pRPysZ4ZLG76UpubZuI57NnC7EkQ6vJulKjbhNRDiquf3ZVmnwFpyPei7ThmZ01nNhMEDM86zeNbUXoe0xqvs3qmFj4qpUwnJ0ibmXPIdOeeOGBgy1cAvYEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d602fb7461.mp4?token=AmiVsLCMiFoqHkgRgNV7aR2rrMdv17E26X0s986g8XL5VdUJ9ZeZPR5_TAnq2-uc1Y50dc3XjbFTnl46foTZ73HdbeeYJr1ON1smM8pho61_47H7h4CBTb6LqniSRu6vIsVhI3NPsDBRhoPd8PNeLkpvCLIOFXON_5PiyqTDbS9X3UxP3F1W5o7d0QQ1t4BLZSn-4hWZryKkHrmDbVX6RWUmiq7Gg4pRPysZ4ZLG76UpubZuI57NnC7EkQ6vJulKjbhNRDiquf3ZVmnwFpyPei7ThmZ01nNhMEDM86zeNbUXoe0xqvs3qmFj4qpUwnJ0ibmXPIdOeeOGBgy1cAvYEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
🤖
در جریان «کنفرانس جهانی رباتیک» در پکن، بر اثر نقص فنی در کنترل‌کننده‌های از راه دور، عملکرد برخی ربات‌ها مختل شد و از کنترل خارج شدند
😁
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70326" target="_blank">📅 14:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70322">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3V5kXg9YRk2tUviv9W5pMTvuuJbn8GtdAXc15-JFadNZHFmRFjRUUWfzEC1RT0RQc4PVteAl8v3lMI6NJvL6pMhgEh7cx-hsjyuw_4sOSn_KOo0JItnMk11AHsuyF2YM26cX6z74nP_AIZqBNuAIX6tndcg7DTidxNKKerUEh89DsFYGHTupNwiff4emRJ6Ga3b4Hw_xMMr7c1z6hkORebKs8V8fpIdhwyMFfQR18IHwYn5_mAWS-j20kigJt3RexS3egZc7bv9vh_nSAnQAGzi5UfAFCgAnwl3BHcKIa7H4yX-k5hsiS_tu09zhNEyTo2iCaW-BYpCHKPs-pdO9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e9d122dfe.mov?token=TajDKswjayWEoWsU9zgIks78NPJvlBxiJ57xkrg77oj77RCkZJRMHRfpfhcdousfHeYzcFIkkfseiV9SR9vWwq3OtoxdBrHdvVOob52-GBwQvTMyEWO4EPTR5blnuKEAmwJ0bOBXygw9Lt7ZFesu9TVe8_kXrt71UCGOVhy5LrrtDhoIlwItHtvDfgQLeMcJTLu4elOccgpjvUkozs7VY_hCywySGjSGNLsvHQ_3sS1aXja_3JjiKNvu8SnGCGXSGu32CxX-JANyr_hedBf3wmx84cI2WyyXSHt7RLqx5H1AYOXs75SZ-UMY_vHnr0-iIuGpmEFzxqCYLXBHUSflNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e9d122dfe.mov?token=TajDKswjayWEoWsU9zgIks78NPJvlBxiJ57xkrg77oj77RCkZJRMHRfpfhcdousfHeYzcFIkkfseiV9SR9vWwq3OtoxdBrHdvVOob52-GBwQvTMyEWO4EPTR5blnuKEAmwJ0bOBXygw9Lt7ZFesu9TVe8_kXrt71UCGOVhy5LrrtDhoIlwItHtvDfgQLeMcJTLu4elOccgpjvUkozs7VY_hCywySGjSGNLsvHQ_3sS1aXja_3JjiKNvu8SnGCGXSGu32CxX-JANyr_hedBf3wmx84cI2WyyXSHt7RLqx5H1AYOXs75SZ-UMY_vHnr0-iIuGpmEFzxqCYLXBHUSflNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
حمله موشکی شب گذشته روسیه به کی‌یف منجر به کشته شدن شش نفر و زخمی شدن ۳۳ نفر دیگر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70322" target="_blank">📅 13:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70321">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/it7bVzkhIDsDJb30GwbBH7O1PhoPaun-9lzyxjL87gAbLlGmCuNlfRTzlBk1jpfyNHxEyD_7HuzyIvS22JU78gO30VYIIhC-n0f40uxOZrE2fgeyV3ijcSJlpx569kFSOagfWhw76T7-7x0Tn7xKIRmnX5Y3cJQXeR2Xy53G7Ba6ah6wVZ4nU67D9lXChAhWYXwGHEKcSI7AOY86fBiCT79xc0FExPt2e46L0_yDCH_p2sGqFPaH0qALJ4xIGWDP3-2_1T5MszLR-ZqbmmgVfW4Yg4vHlryM0MgAcXHbthteCkn6UUYtnPeZ033tQ5Lg_wJNLGyG5ls33x3d9vqRNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ابراهیم عزیزی:
ما تمام تحرکات شما را زیر نظر داریم. هرگونه اشتباه یا محاسبات غلطِ دیگر، پیامدهایی به‌مراتب سنگین‌تر از گذشته در پی خواهد داشت.
پیش از آنکه دیر شود، فوراً به حضور خود در منطقه پایان دهید و نظم منطقه‌ای جدید ایران را بپذیرید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70321" target="_blank">📅 13:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70320">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/news_hut/70320" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/70320" target="_blank">📅 13:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70319">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yzmf3LT2lCebqH3o0QjB4SXtZemOi00kYe4wCz1mjZHzttLmMmFHYZmoRi2ssykPZtsAi5zb4X-IFfzAxjha3ZgAI3C4fJEPNOxN0Qho91zlko93UdVZybfEId6V7tQPxdZk26dB9GR2USWgEYmdUbhZPdkr-okMFQoKQUoGm-I9GhSIc66yjdHgdpOUISwJ8wWPgtuzS1wJfMLOWvsPjqjxyJyuw8wp7N4tS9bSVbzu8Bh5KPsaQjLwDQ7rrmR90iwGQTiFwsFvJOoWQnV2eUX74EDzRK1PjQHmjO9GJSnQlWDadtgbDfrUdxqwZbocfrHCQLWxhLPunRPgGKnBrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
سایت جهانی  و معتبر
#Melbet
🔴
بازی های مهم 27 مرداد
🆗
ثبت نام آسان و سریع کلیک کنید
🆗
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
پخش زنده ی تمام مسابقات
✅
درگاه اختصاصی برای کاربران
👍
پشتیبانی 24 ساعته فارسی
🎟
Promo Code: MELBET90
🇩🇪
دانلود اپلیکیشن MELBET
📱
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r29
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/70319" target="_blank">📅 13:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70318">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cp9UTlGGaos2P0EQcyjH8mHw7kkLXLceOzRWlkckbciK7RWYA7EriTTdNMpq4kX8fzFNLvNGRce9axhwRkXdfshbBYPWpxlXsX8aFT6mn7jPx9NpihMKVwjvjdA8GZoD3NKaOsueF-FT0VMt9-63XNE5qt0ky6Nv2aESlkLAyDBPKxNtl7oQfdFyemWu4uxokkxPuzKu-AzADiyubt_zWjHKpO55lSj8KvYGcW-nUfJleWrKzSXPlKdqLdkyrg61ttdp627hrEoH1dzBC7wvQR7d0e4wJUoA0wF_N_4jqmx8opdOhOSA7-mziU-Xxy9jl85RpIDUluEVEwDuR3byOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇮🇷
همتی رئیس بانک مرکزی:
درحال حاضر هیچگونه صادرات نفت نداریم
اما به حضرت آقا گفتم وسایل زیاده نگران نباشید
محاصره دریایی و تحریم ها شدیدا اقتصاد ما رو ضربه دار کرده
گرونی که بنظرم طبیعیه در شرایط جنگی هستیم
از مردم مبعوث شده درخواست همکاری داریم در این دوران سخت
این جنگ تموم بشه وضعیت آروم بشه خدا بخواد دلایل کاهش قدرت خرید مردم رو بررسی خواهیم کرد
ریالی از پول های بلوکه شده آزاد نشده
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70318" target="_blank">📅 12:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70317">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dcfbcfa9f.mp4?token=LoT57gNYLlDKgJGdMUhcvr7B4B0_8Se7EaYQtFPW28G3bTQOS8WE3PVORLidgqzxxF0vLaWa0plYDC3cFayt8Whb0FPxSgPMdpA5i_JMwm2rW6brPGxJfbWYbKuy7IzDAm3Dsv-hmE7GJsqs6u5gp2sEG3kxMDDxA-bjDY8lTCfgvn8OMp_0qk2D6SVsbYWjFaNePIYQBWLAabwELqxVcxbxWrX78VeDXb-uY6Cgy4t_9QAGGdpaaviBquQg5umE2P5UHXAZ1gBPlw8JUA8pMBGWt0F8KpTGGuwOEwADM73ylZFnpZTEfVlm6Hlq0JEYK4esHFm6L3HUAyuETMvC4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dcfbcfa9f.mp4?token=LoT57gNYLlDKgJGdMUhcvr7B4B0_8Se7EaYQtFPW28G3bTQOS8WE3PVORLidgqzxxF0vLaWa0plYDC3cFayt8Whb0FPxSgPMdpA5i_JMwm2rW6brPGxJfbWYbKuy7IzDAm3Dsv-hmE7GJsqs6u5gp2sEG3kxMDDxA-bjDY8lTCfgvn8OMp_0qk2D6SVsbYWjFaNePIYQBWLAabwELqxVcxbxWrX78VeDXb-uY6Cgy4t_9QAGGdpaaviBquQg5umE2P5UHXAZ1gBPlw8JUA8pMBGWt0F8KpTGGuwOEwADM73ylZFnpZTEfVlm6Hlq0JEYK4esHFm6L3HUAyuETMvC4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیشبینی زنده‌یاد مانوک خدابخشیان درباره ترکیه و اردوغان:
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70317" target="_blank">📅 12:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70316">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">⏺
🇮🇷
محمدرضا نقدی، فرمانده ارشد سپاه:
رئیس‌جمهور آمریکا خیلی کوته‌فکره و کاراش بچه‌گونس
بنظرم مشکل داره و برنامه‌ای برای آینده نداره و حرفایی میزنه که شاید ۲۴ ساعت بعد خودش هم یادش نباشه
حرفاش باعث شده قدرت آمریکا زیر سوال بره و ما دیگه روی حرفاش حساب نکنیم
به نظرم رسانه‌ها هم نباید زیاد وارد جزئیات حرفای رئیس‌جمهور فعلی آمریکا بشن، چون خیلی از این حرفا اساساً بی‌محتواست
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70316" target="_blank">📅 11:30 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70315">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d971ab84f7.mp4?token=s0yATDbNGKKJdAdyFs_BhUNHrmC2aqZdroxOmxxaq-aQJGW6C2ibhYDBJUKWf5eMRxiuTkj4WFiWQ8VMQtunUgSHEAEA-IcouddXaGpXUL6HhG6GhhaPRY8-ZTgq7khEIuxqqD38NGl_6LPFaCkeAV8xYL8vwgfVRqbGmmwmU7ekz968Q4nVhCpM_faiYPF1qJW92MZvJEUa2jhmG4vVhmifZbl2dkW-XpfTMO5Kdf-jrziDDMK10vbCa8x9BCyPro2RB_uHxoA3DKh7iRElTO8tN4scydCtnDjS-2YGiUBznHkoTBpnbjbWM0G2WEtA4HGq1tFiU8WvEjyG1665_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d971ab84f7.mp4?token=s0yATDbNGKKJdAdyFs_BhUNHrmC2aqZdroxOmxxaq-aQJGW6C2ibhYDBJUKWf5eMRxiuTkj4WFiWQ8VMQtunUgSHEAEA-IcouddXaGpXUL6HhG6GhhaPRY8-ZTgq7khEIuxqqD38NGl_6LPFaCkeAV8xYL8vwgfVRqbGmmwmU7ekz968Q4nVhCpM_faiYPF1qJW92MZvJEUa2jhmG4vVhmifZbl2dkW-XpfTMO5Kdf-jrziDDMK10vbCa8x9BCyPro2RB_uHxoA3DKh7iRElTO8tN4scydCtnDjS-2YGiUBznHkoTBpnbjbWM0G2WEtA4HGq1tFiU8WvEjyG1665_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
از دست هرکسی نوشیدنی نخورید
؛
فلونیترازپام که به «داروی تجاوز» معروف شده، یه آرام‌بخش بسیار قویه که مجرم‌ها واسه بی‌حال کردن قربانی‌ها ازش سوءاستفاده می‌کنن.
این ماده می‌تونه باعث گیجی شدید، خواب‌آلودگی، کاهش هوشیاری و حتی فراموشی موقت بشه.
ولی یه باور اشتباه توی فضای مجازی پخش شده؛
اینکه این دارو همیشه نوشیدنی رو شور می‌کنه!
شکل‌های جدیدتر و پنهانی‌تر این دارو میتونن بدون اینکه تغییری تو طعم و ظاهر نوشیدنی ایجاد کنن خورده بشن
پس به هیچ وجه از افرادی که بهشون اعتماد کافی ندارید نوشیدنی نگیرید مخصوصا دخترا بیشتر باید مواظب باشن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70315" target="_blank">📅 11:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70314">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41769ecb44.mp4?token=YKbot9ux5vf1JYXO4kMSxZ6_sYEQ6PT_F0qF7tSPG9OuylRTXZs0KsN5J6NKqjcGMsVwpBHCoU33mG0gK4ihr0LKHrs9euZazeKf5gHFyA7VKvKU1bV1OAUiJGqrqQltJLLIAbQW-BhJn04M8qale2h278G-Xm5xEuAP5aU--xbjCF7D32s_1FZoOuIxQMGogCsKfFzuXrIqIVLEWV-fhry2ig1xAj6s-E6jhQfT-7EcDn0tjmQt3GO2RypjV8MkZsovKN3mXyblcir69hqGqk1K7lWrVZmQh9XiSU_l26llfBqecP7Wtvy5qu9qyIzKm1Ulis9Oyt4jX4mzrs7zzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41769ecb44.mp4?token=YKbot9ux5vf1JYXO4kMSxZ6_sYEQ6PT_F0qF7tSPG9OuylRTXZs0KsN5J6NKqjcGMsVwpBHCoU33mG0gK4ihr0LKHrs9euZazeKf5gHFyA7VKvKU1bV1OAUiJGqrqQltJLLIAbQW-BhJn04M8qale2h278G-Xm5xEuAP5aU--xbjCF7D32s_1FZoOuIxQMGogCsKfFzuXrIqIVLEWV-fhry2ig1xAj6s-E6jhQfT-7EcDn0tjmQt3GO2RypjV8MkZsovKN3mXyblcir69hqGqk1K7lWrVZmQh9XiSU_l26llfBqecP7Wtvy5qu9qyIzKm1Ulis9Oyt4jX4mzrs7zzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تمسخر صحبت های خاتمی در صداوسیما
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70314" target="_blank">📅 10:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70313">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/670edf8121.mp4?token=FzSzT6nXkDHn8sjMdMQYjAR8vV91SH9yup-CsqzAxBkXXBdGaXs0EEHWqy8ELAl3BDv1ZJVbYEdXR_cNuhAaM9Ac_RWV1Il8pBuyXxiseKDWgsTOcjHr4MpYA2fsiLanVom6r6QCiAaRqGw8m64ZoDNNfNG65aOTZut2yNfH70iINGhhIqsaVljf9_lmp84_zG59M7DiPcIVPo7sP6i_ew42e1Fk3C9IIpv5GBDI5fGTDDXEbfKNX3mnWvMIU1hyQ8QM6Mv80S33x1W7mTIMIBjodcuGwltDdftRqgW343F3VJ2tHwl-cJ6SrVxpIS-ZOdi77YDzb0uq3-2-YjzH8w0uFQS3YFJdqzRfyUqe6uvjb7aUR1jlBQ4LiEL7AINAzvQ_NwGGqfP8O3iPRSX_MJ_EPJkl-N1XXpgkZV-bFcP9S_W-yX-OMMpJWHoe7M58amjihDl89b-fYY5rXSkHr83SgzxYRebhmaATmJR_-9v3LBmlvtDkMRgC_b1qHTFfoUmLmm3UFKEUS7EqEzKkDQPSiSodonjIr-ZV2BDOSxwWoJs0YFPu65iZ3s7quMJNNQuJ21VZGfFOgW4YSlYDRldMIdWZo0N7L8Y_-SqG0roDUDq9d9DPRl9lOEdHWrQ4XxdC_ByNz-jVTF7xyJjoMhYCL8O6zneiVrSEk0wFcug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/670edf8121.mp4?token=FzSzT6nXkDHn8sjMdMQYjAR8vV91SH9yup-CsqzAxBkXXBdGaXs0EEHWqy8ELAl3BDv1ZJVbYEdXR_cNuhAaM9Ac_RWV1Il8pBuyXxiseKDWgsTOcjHr4MpYA2fsiLanVom6r6QCiAaRqGw8m64ZoDNNfNG65aOTZut2yNfH70iINGhhIqsaVljf9_lmp84_zG59M7DiPcIVPo7sP6i_ew42e1Fk3C9IIpv5GBDI5fGTDDXEbfKNX3mnWvMIU1hyQ8QM6Mv80S33x1W7mTIMIBjodcuGwltDdftRqgW343F3VJ2tHwl-cJ6SrVxpIS-ZOdi77YDzb0uq3-2-YjzH8w0uFQS3YFJdqzRfyUqe6uvjb7aUR1jlBQ4LiEL7AINAzvQ_NwGGqfP8O3iPRSX_MJ_EPJkl-N1XXpgkZV-bFcP9S_W-yX-OMMpJWHoe7M58amjihDl89b-fYY5rXSkHr83SgzxYRebhmaATmJR_-9v3LBmlvtDkMRgC_b1qHTFfoUmLmm3UFKEUS7EqEzKkDQPSiSodonjIr-ZV2BDOSxwWoJs0YFPu65iZ3s7quMJNNQuJ21VZGfFOgW4YSlYDRldMIdWZo0N7L8Y_-SqG0roDUDq9d9DPRl9lOEdHWrQ4XxdC_ByNz-jVTF7xyJjoMhYCL8O6zneiVrSEk0wFcug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خانم دکتر از یکی دیگه از فانتزی‌های آقایونِ ایرانی پرده برداشت؛
یه خانم اومده دکتر و گفته همسرش 3 تا گوجه‌سبز رو همزمان کرده تو واژنش ولی متاسفانه دیر جنبیدن و واژن هر 3 تا رو قورت داده، ولی خوشبختانه همه رو تِخ کرده و عفونتی درکار نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70313" target="_blank">📅 10:04 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70312">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e03e1f6f01.mp4?token=bs_r1GqtA7HiLQ62R9bO5-2kfW7V81BqeT-tGiBi32Exh-vF1OTYbglqBJ8_8SCM9BB3ZRkrLKTUd6U7mLhMSQoy5Q14iTAOtas1AZ0-rOezG_-2pk7TtoX00ZCoLB0yt0itQyVZKrGe3ag4ss1DJFH4Rw6fwN9AqWb3jjaRYMWsPCdBzUlaFXU-J_3UN2TPQzeHg7uKxlWXXkzgIaJb3_ykdKAmzaPaROmCRD6bE7ZIU2p-CiQxeAHC0HGLtuNwzcR3Itpq1mZvcBP1DE6vaZGcGoxhjQ2QIy7B1F78vVb4hRu8nxGIgVZSC35qPZWNGcaqq6ZpHVFLhgMWFHjWWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e03e1f6f01.mp4?token=bs_r1GqtA7HiLQ62R9bO5-2kfW7V81BqeT-tGiBi32Exh-vF1OTYbglqBJ8_8SCM9BB3ZRkrLKTUd6U7mLhMSQoy5Q14iTAOtas1AZ0-rOezG_-2pk7TtoX00ZCoLB0yt0itQyVZKrGe3ag4ss1DJFH4Rw6fwN9AqWb3jjaRYMWsPCdBzUlaFXU-J_3UN2TPQzeHg7uKxlWXXkzgIaJb3_ykdKAmzaPaROmCRD6bE7ZIU2p-CiQxeAHC0HGLtuNwzcR3Itpq1mZvcBP1DE6vaZGcGoxhjQ2QIy7B1F78vVb4hRu8nxGIgVZSC35qPZWNGcaqq6ZpHVFLhgMWFHjWWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند شب پیش تو تبریز، یه پسره داشته مزاحم یه دختره می‌شده؛
کاسب‌های اونجا بهش تذکر میدن که نکن ولی پسره میگه به شما ربطی نداره!
اونا هم چند نفری می‌ریزن سرش و پسره رو میندازن تو سطل آشغال...
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70312" target="_blank">📅 09:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70309">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GHx2Exa2F_JcKvSdgG8SuKk9r3NgyjbWHE8cXeFz3aQms6QHYSQP2UjCc80MXVk1BqJtoM01qbL9RnTY0bNpu_Rbt0OxcaoMGdfuimmdj15qzHdhVr9Fj5VkqD0E_Y1vwG_mIDTPVlsKdUUc2Z9Gn8uu-uUqAThhZBABrYJSQr9eDeta4Qt5eCyYhan9ny5hqpf9GtB2cHFGMnm0dnbEKX3MgSXXpCXXpx6ZlFeHs7WzQgehI6KgLti7zdykVMwjY3l7ibG8v8KSQTvbUp6UigDlGgsbKc_0Uy0q91EAHaoE4F66gcFwlSFKsJbnvR1uGqneo91aBpWK3u9dg-uR_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VUipSO1hk8dKKQ44RGRyBfLs8djy6nsKBgPCLOwPkuotl29fohbM1W0A3jhiswdTn5W0Xk1C9lCYcH-VGjI5HkleohFveYTW3R9kyvHa8UfMYGwTbQcnkrtgJXAsmUBPiDRpztpVkSNNtQTjbvCSVuu-enXYsh-QAhVG1MgK1DnHceJ973SI6zBqbXGkOrhmE_bMAT8L3w4Ohv-J5vEw599XueHbDSMWCIzurHaKDBKE6dxdb6purzIkGnaqu61s6bZF_WFFqDmjM3tIcMQJIPMptuqJmzzJ46lQ0Ip2JnjPE0u5Ql7dtAGDX-cF4CyawvEHMkUE5Nq-t5gHdLOycQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e1fd6dc78.mp4?token=ufMEmP5qRW4OYwcjmnB6E3hzwiJPztv-hkfvwjSFuI933-yZQxsj16T0QPZqHQKUMpt5FICyNCMD7t2z07fPXZmibwYrvKxP3vb6AVlNNtG-n0nJtTQMFllTm2K45pQigHBJFwknzxMw6k8Y_IfimKWHh3zivUmc0uTj2OeWtiR24lxUxnFcJXhjFgZf3GA3Df5c47YzZc0OihCDj394QcbF4lWmA1mosxYIXCgFa_CeFGz6UPW5bvjfjl8xZn6ych5wtgF1sDdrD7jcahYr9xqXfR5C1rJZ1kLWC5JKhsorf9xfuYoqOTBBACXbVw6591lLA-2dpMTBDgkEwGODRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e1fd6dc78.mp4?token=ufMEmP5qRW4OYwcjmnB6E3hzwiJPztv-hkfvwjSFuI933-yZQxsj16T0QPZqHQKUMpt5FICyNCMD7t2z07fPXZmibwYrvKxP3vb6AVlNNtG-n0nJtTQMFllTm2K45pQigHBJFwknzxMw6k8Y_IfimKWHh3zivUmc0uTj2OeWtiR24lxUxnFcJXhjFgZf3GA3Df5c47YzZc0OihCDj394QcbF4lWmA1mosxYIXCgFa_CeFGz6UPW5bvjfjl8xZn6ych5wtgF1sDdrD7jcahYr9xqXfR5C1rJZ1kLWC5JKhsorf9xfuYoqOTBBACXbVw6591lLA-2dpMTBDgkEwGODRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ظاهرا علی خامنه‌ای به یه شاعر سفارش داده که یه شعر تولید کنه که خامنه‌ای بعنوان سروده‌ خودش منتشر کنه، شاعر هم یه شعر کرده تو پاچش که اگه حروف اول مصرع‌ها رو به هم بچسبونی میشه:
"من علی خامنه‌ای زاده شیطانم"
🔴
حالا رسانه های حکومتی تازه متوجه گاف شدن و دارن شعر رو از سایتا پاک میکنن
👅
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/70309" target="_blank">📅 09:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70308">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rqb0dMhoShZYhTtsGHf8AODwUx-GyUJUnZUSkVWSERPwYIrdJKbiWXgN9_UCH_UIT2n8zmOEWFRrHJNfXDcoT6_u3JWpYEf4wtwJcWWLjanWLMhOQG_yjg2ESO_0obc0CmxS0KG1DDD4BCrgrHveXt_tn-P-13SEcXJeyA92vRqFYZSHSbAOCWVaBna5WtmG7rDgGs7t7KJq3Py-AWzvTHe2SoJYuGit4J7gg9RQYFKpraZepJ1iTUnxLbZlhVTfBFfPGTB3M0APlzVcdxZxTPIiFt5AQ0ihmmCwYE-CBsjrRXj53wAJ9rrT4l66O8rqpj9a2ug5QLwuT9VjUwbMhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
🇺🇸
#فوری
؛ترامپ درباره‌ایران:هیچ‌کس به اندازه من به جمهوری اسلامی ایران فرصت دستیابی به توافق نداده است. اما متأسفانه برای آن‌ها، این فرصت از دست رفت.
از این رو، امروز من خبر از اجرای «ویرانگرترین عملیات اقتصادی تاریخ علیه یک کشور» می‌دهم!
این اقدام، مصداق جنگ اقتصادی و انزوا در ابعادی بی‌سابقه خواهد بود.
نیروی دریایی‌شان از میان رفته، نیروی هوایی‌شان نابود شده، کارخانه‌های نظامی‌شان به تلی از خاکستر بدل گشته، ارزش پول ملی‌شان از بین رفته و کشورشان در آستانه فروپاشی کامل قرار دارد.
همچنین امروز اعلام می‌کنم هر کشوری که به مؤسسات مالی، شرکت‌های تجاری، فرودگاه‌ها یا نهادهای دولتی خود اجازه دهد تا هرگونه شریان حیاتی برای ایران فراهم کنند، خود با پیامدهای اقتصادی سهمگینی روبرو خواهد شد.
قاچاق نفت، خطوط سوآپ (معاوضه)، انتقال پول نقد، صرافی‌ها، ثبت کشتی‌ها و شرکت‌های پوششی؛ همه این فعالیت‌ها باید همین حالا متوقف شوند. شما خود می‌دانید که چه کسانی هستید.
این یک «روز سرنوشت‌ساز اقتصادی» (D-Day اقتصادی) خواهد بود و ما نیازمند آنیم که تمامی متحدانمان در کنار ایالات متحده آمریکا بایستند تا تهدید ایران را منزوی و خنثی کنند.
این دیوانگان در تنگنا گرفتار شده‌اند و این اقدامات تاریخی، آن‌ها و توانایی‌شان در گسترش تروریسم در سراسر جهان را فلج خواهد کرد.
ایران هرگز به سلاح هسته‌ای دست نخواهد
یافت.
از توجه شما به این موضوع سپاسگزارم. رئیس‌جمهور دونالد جی. ترامپ.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70308" target="_blank">📅 08:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70307">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔥
امشب چه تیمی می‌درخشه؟
⚽
کدوم بازی گل‌دار می‌شه؟
📊
کدوم تیم ارزش اعتماد بیشتری داره؟  ما بازی‌ها رو قبل از شروع، با آمار و تحلیل بررسی می‌کنیم؛ نه با شانس و حدس!
📌
برای دنبال‌کردن تحلیل‌های روزانه فوتبال عضو شو:
🔗
https://t.me/+nbm7Tb2pz8VjMDlk</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70307" target="_blank">📅 02:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70306">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=Jz4NtWdpcxh2MPDBVZ90OiLERLJrxgEV1_AX2NvRHA-lO_Ph_qr8Bj3wCp_p8nNvNWhRnSV3jaz4Jf-ugMTqnT8aYGfEUipgCZ79Ah3z6yCbNhbcNyZSurzHUaJVG__XPy3Oogm1m-JyjK54kwSF6eSilKM7QKKzempt9odJuZ7lT_1fjS1zTYxFqAntoxZmgGd8om8pBxaoWXLCrGl01fGiAPHSXgH_Ajqvfq-_TFhO8uGE2aG4cG-aScBA5MZCWPTI9AXR8FWF_VjsIcqC71jZqQcQYMlou52PPlug_4BafdtLfuxMt70IsV9pBo_GB2idYkNEIjYqgnaOpWMImw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=Jz4NtWdpcxh2MPDBVZ90OiLERLJrxgEV1_AX2NvRHA-lO_Ph_qr8Bj3wCp_p8nNvNWhRnSV3jaz4Jf-ugMTqnT8aYGfEUipgCZ79Ah3z6yCbNhbcNyZSurzHUaJVG__XPy3Oogm1m-JyjK54kwSF6eSilKM7QKKzempt9odJuZ7lT_1fjS1zTYxFqAntoxZmgGd8om8pBxaoWXLCrGl01fGiAPHSXgH_Ajqvfq-_TFhO8uGE2aG4cG-aScBA5MZCWPTI9AXR8FWF_VjsIcqC71jZqQcQYMlou52PPlug_4BafdtLfuxMt70IsV9pBo_GB2idYkNEIjYqgnaOpWMImw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
امشب چه تیمی می‌درخشه؟
⚽
کدوم بازی گل‌دار می‌شه؟
📊
کدوم تیم ارزش اعتماد بیشتری داره؟
ما بازی‌ها رو قبل از شروع، با آمار و تحلیل بررسی می‌کنیم؛ نه با شانس و حدس!
📌
برای دنبال‌کردن تحلیل‌های روزانه فوتبال عضو شو:
🔗
https://t.me/+nbm7Tb2pz8VjMDlk</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70306" target="_blank">📅 02:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70302">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c25635056.mp4?token=gaRw3QFO4PcJO61fbYzWT9iDmZ5yidkJLKcPPCYy6fuMOy6VUsYx0H1e2LLt1MIpRgCJReJLmEQj7vMLmksfhF6oCYB7gWzLt5nDO_KEMUO862IdRCgyvF79i9N8HWomjpKYsy7KLPDJE9SRZKpT8rFVHZG_RQ5xCCoZbREvxmak3kdRGiZ3dnU4rVJEQNPC3zY1TWRZq6X3eG6B2yKuPxrqOIPWjXduu0xW2NSuGBb7cj30bleV9TDXz2LC1YVsvJ4Z8bAwf7mrFEiMsO81YrAe7KB_2eerAJIcmDepfwn1gcT8HuGINCZRmTd_P9kXQwUrrxor3qG3H_SJ1fpT3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c25635056.mp4?token=gaRw3QFO4PcJO61fbYzWT9iDmZ5yidkJLKcPPCYy6fuMOy6VUsYx0H1e2LLt1MIpRgCJReJLmEQj7vMLmksfhF6oCYB7gWzLt5nDO_KEMUO862IdRCgyvF79i9N8HWomjpKYsy7KLPDJE9SRZKpT8rFVHZG_RQ5xCCoZbREvxmak3kdRGiZ3dnU4rVJEQNPC3zY1TWRZq6X3eG6B2yKuPxrqOIPWjXduu0xW2NSuGBb7cj30bleV9TDXz2LC1YVsvJ4Z8bAwf7mrFEiMsO81YrAe7KB_2eerAJIcmDepfwn1gcT8HuGINCZRmTd_P9kXQwUrrxor3qG3H_SJ1fpT3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
حمله موشکی گسترده روسیه علیه کیف در حال انجام است
؛
بیش از ۲۵ موشک، از جمله موشک‌های اسکندر-ام، موشک‌های کره شمالی KN-۲۳ و زیرکون، به سمت کیف شلیک شده‌اند.
هفت بمب‌افکن استراتژیک Tu-۹۵MS و دو بمب‌افکن استراتژیک Tu-۱۶۰ در حال حاضر در هوا هستند و انتظار می‌رود به زودی موشک‌های Kh-۱۰۱ را شلیک کنند. همچنین انتظار می‌رود موشک‌های کروز کالیبر به زودی وارد حریم هوایی اوکراین شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70302" target="_blank">📅 01:17 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70301">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/443c91ecee.mp4?token=AMTt9o5l8jQyIlpHjcmaNarnVAEqieAPl5POsiLdpKY_W9aMCCKM5cBwL6me1UAkX0QQrCt-i0gN4Ap-gynuxYd_b90KRANLGZbZxYpr2dVgn86A6GzTzc4bYUdrDv7TcmQu3sHMlXXJWgcn-jQZFGj20yh1hy74iY3YqbwJ56hBranmSmGAlbNp7VgU09TMXQp7CptH_z4uGvbygk3N5NUOsTA8Lrcr-BLwNJflPLCQV-j2sLbbikoxE938oCuw8RoMdMPcAiPENxRjNLHIrFjdBQJ2scntd0i5hGTGVHUAwLNJaOR7wzbI4venGlbs-_Gerxao-yYLFLQFkDSdpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/443c91ecee.mp4?token=AMTt9o5l8jQyIlpHjcmaNarnVAEqieAPl5POsiLdpKY_W9aMCCKM5cBwL6me1UAkX0QQrCt-i0gN4Ap-gynuxYd_b90KRANLGZbZxYpr2dVgn86A6GzTzc4bYUdrDv7TcmQu3sHMlXXJWgcn-jQZFGj20yh1hy74iY3YqbwJ56hBranmSmGAlbNp7VgU09TMXQp7CptH_z4uGvbygk3N5NUOsTA8Lrcr-BLwNJflPLCQV-j2sLbbikoxE938oCuw8RoMdMPcAiPENxRjNLHIrFjdBQJ2scntd0i5hGTGVHUAwLNJaOR7wzbI4venGlbs-_Gerxao-yYLFLQFkDSdpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
تصاویری از یک سرباز اوکراینی که با استفاده از تیربار MG 3 (ارائه‌شده توسط آلمان)، یک پهپاد تهاجمی روسیِ در حال نزدیک‌شدن را از فاصله‌ای بسیار نزدیک سرنگون می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70301" target="_blank">📅 01:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70300">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVgSH741wk2Q5CQip830qKwiweq12EIo7seSOc4vwiJQU0UKhTpi_0FAycWXy2n-pQOyusjFWzr0qJDmVnynE5ItQ7S0Myv7sbuc43wvgFjRXn72-_vQ6QHhShkfCFU62Vu0s6VLiqP_d1GC2hahTL2QQe6D6Zhgo1_iVBVDLADWSpPbMBb3fUxRZbJq0BbK9rL2w8rCihCDNCEnaOJHd9PUs8BMOnECIgIdjAshaZ0YQqxOyfBln7AoyIDoh9o6ET-jDICzwmG7KAkW26BdLDAG3kdPz0kSzagtap1oATQtUtOVAeHZDWboC_2jVP42tblQAEYEKm2IAlSHKxv2Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
علی قلهکی:
اگر آمریکا بتواند مسیر جنوبی تنگه هرمز در آب‌های عمان را برای عبور کشتی‌ها آماده و امن کند و انتقال نفت را از این مسیر انجام دهد، اهرم فشار تنگه هرمز تا حد زیادی کم‌اثر خواهد شد.
در این صورت، به گفته قهلکی، آمریکا ممکن است دیگر نیازی به رفع محاصره، لغو تحریم‌ها یا آزادسازی منابع مالی ایران نداشته باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70300" target="_blank">📅 00:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70299">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVrpv3G7W36MPSVg-UH1fLSGkpNJ896DWFR3SnauX1HjHv8_Uox4X9zfEGoNxWEuBMMwiBa3Std_pTcK5Wjio7uZH16BSsIZEPJoSJwspk9F8LpTe6MGemOt8NuAdD3LUHTPImvdAZf9IlUAJdEyYR8Mm0Ia7zWZB4BEYkIM9iv8PHenXSQZ0veEpyXPaFwxDF-K6s967FAXIBCuAs4EtqFSaJNdcGykBpNUqWcWwllROR47Ubsqb6hSQwVkSdRsSBqOZ_6HhvwddEpTolEkQPG7f9VmTFt0_vNYHibBPrHT2fjoJ0rY9lG0-fV4ZB4PWNTY-dcSXiR6NGpd17m_Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هم قیمت بنزین تا ماه بعد و هم قیمت دلار و ماشین ایرانی رو تا اخر شهریور ماه گفته؛ این کانال تمام پیشبینی ها همراه تاریخ وقوع رو میگه:
👈
مشاهده بدون سانسور</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70299" target="_blank">📅 00:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70298">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYqdIA6aNVEf7BdhaI3l2xYGrugnBhignHNGi-udTrgvDugQ0fW4frrFihpIdT2qCYgxU-QSFYP_O_L0peoejexopNOjih3JxYMecpVVw9je-xZprGYMpdAbqzeKiCX5kvbZhqcYvI95usW_FnNhDP3izV9YHpwLYcjpPridZurmvVCTv16GH456Bh-CPGuyyRPUOV2t9GcIVdn8tG3_itj15zBaVArkE07WI9Gr03vGlQs0362VQCx0bp8nRZPvJurNzOJk_g2E7-W_ZaOUqatVCO98jtKav-iHGAmkoJX-MX9sSqF9F-MzQ-5Lm6aGy9wKP-zm02ybUU6QC3xpZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
📰
اکسیوس: ارتش ایالات متحده بی‌سروصدا یک کریدور کشتیرانی در بخش جنوبی تنگه هرمز ایجاد کرده است که به ۱۵ تا ۲۰ نفتکش اجازه می‌دهد هر شب در امتداد سواحل عمان وارد خلیج‌فارس شده و از آن خارج شوند.
مقامات آمریکایی می‌گویند که این عملیات اکنون امکان جابه‌جایی روزانه نزدیک به ۱۰ میلیون بشکه نفت را فراهم کرده است — که تقریباً معادل نیمی از حجم پیش از آغاز جنگ است — و در برخی شب‌ها میزان نفت منتقل‌شده به ۱۵ تا ۲۰ میلیون بشکه می‌رسد.
ایالات متحده هماهنگی‌های لازم را هم برای نفتکش‌های پر (در حال خروج از خلیج فارس) و هم برای شناورهای خالی (در حال ورود برای بارگیری نفت از امارات، بحرین و کویت) انجام می‌دهد. کشتی‌ها در قالب گروه‌های زمان‌بندی‌شده و تحت پوشش هوایی آمریکا حرکت می‌کنند و جنگنده‌ها برای رصد پهپادها و موشک‌های کروز ایران، عملیات پایش را انجام می‌دهند.
نیروهای آمریکایی تاکنون بارها حملات ایران را دفع کرده‌اند؛ از جمله در شامگاه دوشنبه که هشت پهپاد و دو موشک کروز را رهگیری و سرنگون کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/70298" target="_blank">📅 00:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70297">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a5dabd912.mp4?token=I4HMB52rXYu2-UN97DwVW5zWA_0pEPRQyPT80xSMpaycoP9Dhvr3jqELQ8w9K8T62GdrDFWtRw--fFyGb_ZBtL__lhxUqX7N2XtI40OzOpB2wCJjqUwulDYcMWZn3VR45nP_1PcmNE8EIPavw9cK4sH9lNUqw0CrYUEV3xfQj4rHEl6J0WBYG2tWIiBpsPacHapuavkxriBn2ZXwWFqa5kdXs80up-8CJYDH8Og-eTErVNYwQkZfmcEsE7PFb9lNHCt510lWga4fkCixFoTnwZtciaDJXFMaJRDEmSElkg8S4PMVO439-aA_epMyY40JH4-AiznOxPHXqU65-ZhYeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a5dabd912.mp4?token=I4HMB52rXYu2-UN97DwVW5zWA_0pEPRQyPT80xSMpaycoP9Dhvr3jqELQ8w9K8T62GdrDFWtRw--fFyGb_ZBtL__lhxUqX7N2XtI40OzOpB2wCJjqUwulDYcMWZn3VR45nP_1PcmNE8EIPavw9cK4sH9lNUqw0CrYUEV3xfQj4rHEl6J0WBYG2tWIiBpsPacHapuavkxriBn2ZXwWFqa5kdXs80up-8CJYDH8Og-eTErVNYwQkZfmcEsE7PFb9lNHCt510lWga4fkCixFoTnwZtciaDJXFMaJRDEmSElkg8S4PMVO439-aA_epMyY40JH4-AiznOxPHXqU65-ZhYeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ما مواردی داریم که می‌توانیم ایران را بابت آن‌ها تحریم کنیم. ما تحریم‌های بسیار سخت‌گیرانه‌ای در اختیار داریم و خواهیم دید چه میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70297" target="_blank">📅 23:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70296">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bf1eb3322.mp4?token=Sqo2W8TIvG3Uop3GzWJqf2FbCs_aR340NAkKkC1mA26dJ6nhxbIVLijrudlu64-dxVl2-hxO9Ic6Ac27ZR2dq0a34TewVhaFCU_6sYiuHb0RSg5Y7baf4ONounzpSsZvTf-WJ4z8SRmXzM8RbYfMc9GZeIM6Moi_2oE8GjDbEPtG1mdsaDa_xGfBbkFaA_dD5N4ftn52HJ7hQU_ycUnxcsJIV-Pa-09P1FIFdx9gfRC5ZZVNIFNmgOiTbC3mNj1vzBHe_Kq_aANB8AvUL5xq3BpeLR1tNcjWy9l19bG9OtP94-OOI1qOKqYUPirH8rOgkKnZZJBerQva5IBjpj753Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bf1eb3322.mp4?token=Sqo2W8TIvG3Uop3GzWJqf2FbCs_aR340NAkKkC1mA26dJ6nhxbIVLijrudlu64-dxVl2-hxO9Ic6Ac27ZR2dq0a34TewVhaFCU_6sYiuHb0RSg5Y7baf4ONounzpSsZvTf-WJ4z8SRmXzM8RbYfMc9GZeIM6Moi_2oE8GjDbEPtG1mdsaDa_xGfBbkFaA_dD5N4ftn52HJ7hQU_ycUnxcsJIV-Pa-09P1FIFdx9gfRC5ZZVNIFNmgOiTbC3mNj1vzBHe_Kq_aANB8AvUL5xq3BpeLR1tNcjWy9l19bG9OtP94-OOI1qOKqYUPirH8rOgkKnZZJBerQva5IBjpj753Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
سیدمحمد خاتمی:
فرصتی که در تفاهم‌نامه ایجاد شده اگر از دست بدهیم دچار مشکلات عجیب می‌شویم
تفاهم‌نامه نظیر ندارد
بعد از جنگ‌جهانی دوم هیچ سندی که به امضای رئیس جمهور آمریکا رسیده باشد اینقدر امتیاز به طرف مقابل نداده
ما در موضع عزت به این‌ تفاهم‌نامه رسیدیم
دست آقای پزشکیان را می‌بوسم که شجاعانه و فداکارانه این تفاهم‌نامه را امضا کرد
تقدیر می‌کنم از شعام که رای دادند و رهبری که تایید کردند
هر گامی که به سوی رفع جنگ و برداشتن محدودیت برای ایران و باز شدن راه به سوی آینده باشد را باید تایید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/70296" target="_blank">📅 23:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70295">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fR4qpz_QBtlQQYjPiis4tal3uOMkmhn919384hG8u9pcUuzEnRCQ7TtpcwUvF_CmjHWU49NW44It4IdvFMrRM_8gVCk0IKMOMZHWt7rS0YgoM65_aCztX5m2YJKSSeE2rLORfXjvApnPp0vi16UlUGSmxLFxmUczJS1KxWk7SpFawlAfZw0r4CCmNzbCrHjdo0DzExJIVwVjj7_R-oYMZMxzhu4s0YH1SQoxzwnwMUikDRELKqG3mVyJQ7svz5QT5Lg37jJjjIOkEa8aevos65ONDvGBH7TmKpcI1EzSl1RjIZ7sUEHpVom4RGcYkx3ue-cTlvXV07Uxx6r7F0UDoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
قالیباف در جواب ترامپ با کل‌ش تنگه هرمزو بست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70295" target="_blank">📅 22:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70294">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44e544df4f.mp4?token=XznKnSpa12syWxMy0s2vVC1djWyVosE0Wm-cUJGZ6Qn4crPGstSLFP_GvplWrW3ELs5zTK7HPq91-oVZahLQxwR03Q9wtXYgIyEms67BRsW1CF0eeE9nnhIfQ520n7uLmlIWIZz7E6n9-eMG_VzylcUQbCI2Z4k8j6THa_n7OjFIWdiEJxUhrn89emrXNWS1rEco0O8OvKLaJbPZHa1qEUtuG-1xbDEapfBauFNH-U56mHGJbktbXaR1tf2nT_kQDt3dYk_AJrGY-r6Bh_BOb6mRiHxqOwbL0RYF8fzJQwsvQ5vSDR34qXOGn6-5DKaKd_mKgS9XPzjReUCIpbOLYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44e544df4f.mp4?token=XznKnSpa12syWxMy0s2vVC1djWyVosE0Wm-cUJGZ6Qn4crPGstSLFP_GvplWrW3ELs5zTK7HPq91-oVZahLQxwR03Q9wtXYgIyEms67BRsW1CF0eeE9nnhIfQ520n7uLmlIWIZz7E6n9-eMG_VzylcUQbCI2Z4k8j6THa_n7OjFIWdiEJxUhrn89emrXNWS1rEco0O8OvKLaJbPZHa1qEUtuG-1xbDEapfBauFNH-U56mHGJbktbXaR1tf2nT_kQDt3dYk_AJrGY-r6Bh_BOb6mRiHxqOwbL0RYF8fzJQwsvQ5vSDR34qXOGn6-5DKaKd_mKgS9XPzjReUCIpbOLYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
قرار نیست بی‌نقص باشد، اما حجم عظیمی از نفت در حال عرضه است؛ خیلی زیاد.
همه شگفت‌زده‌اند.
🎙
خبرنگار: آیا مذاکرات با ایران را از سر خواهید گرفت؟
🇺🇸
ترامپ:
شاید زمانی این کار را بکنم، اما در حال حاضر وضعیت بسیار خوب است. با این حال، شاید زمانی این اتفاق بیفتد.
🇺🇸
ترامپ در ادامه:
ایران نمی‌تواند سلاح هسته‌ای داشته باشد. می‌دانید چرا؟ چون از آن استفاده خواهند کرد.
ما اجازه نخواهیم داد که از آن استفاده کنند.
مردم در حال یافتن جایگزین‌هایی برای هرمز هستند. شما این جایگزین‌ها را می‌شناسید: تگزاس، آلاسکا، لوئیزیانا.
مردم برای تأمین نفت به ایالات متحده روی می‌آورند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70294" target="_blank">📅 21:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70293">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f23583ef9.mp4?token=ockbQetVaDHQ6_7AuEW_ciF76RQF8tnhRiNgkluKm5lA_8rjG7BAwUwEw3_Sbl764qHHKhJKgO6I9HCYq-bQsl0Q88Lae8bHgg4k1y2PLBqyeq4607hyyOSDJNP4kMCDmuI7w6RBO_-LALcz5uDolmlP8phGqFfZejl58jFMY8kw0ui8Il2ZkFehhCUuYw_7kbd5VYx5dJAl9QaLsez8vX5R0gvMGJDnsJqACJ0fnMC64wDR0f7-oKWt-ceOAnyZfiExH1risgTxPlYuh5CTLPOmNKI48djv6aV0rzGNw0oZ2arRKJZLUMO4Rcyiyyok61raQGo3TU1-VqGkNzeR3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f23583ef9.mp4?token=ockbQetVaDHQ6_7AuEW_ciF76RQF8tnhRiNgkluKm5lA_8rjG7BAwUwEw3_Sbl764qHHKhJKgO6I9HCYq-bQsl0Q88Lae8bHgg4k1y2PLBqyeq4607hyyOSDJNP4kMCDmuI7w6RBO_-LALcz5uDolmlP8phGqFfZejl58jFMY8kw0ui8Il2ZkFehhCUuYw_7kbd5VYx5dJAl9QaLsez8vX5R0gvMGJDnsJqACJ0fnMC64wDR0f7-oKWt-ceOAnyZfiExH1risgTxPlYuh5CTLPOmNKI48djv6aV0rzGNw0oZ2arRKJZLUMO4Rcyiyyok61raQGo3TU1-VqGkNzeR3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عبدالملکی، وزیر اسبق کار در دولت سیزدهم:
به عنوان عضو تیم اقتصادی دولت رئیسی می‌گویم گرانی‌ها یک درصد هم به جنگ مربوط نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70293" target="_blank">📅 21:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70292">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0460292f9.mp4?token=o4dO8r-DJeUzBKWtG8uIOKb8NGlzeMS6TIhvx6d5SKzmQv_EnieGoU3p2lNyMBYUHDVbjvhCjc1uGVqMEHr2nqOqZZgeGzPwuBtGu0jmoRujFUPRxLE84wLvrWK4d9BrIpvY2y9sUs719Qu-vjne9nOPw5AID2iMvnNjMexARKS3GUHhu38aQM06f1csu1gP7SI3jnUm00-ySnnFfSONBnFrvKc3Ij3RooCcdhoHaeGQO5sSRJDG6NsbI3en9R1QaKEjNtfMCwh0oZ29qKCazyrIQOlrSNoe3zmdaekdTrgOOV0pUt77Iq7tWC0DbPFHdLOr1FmENiplncY0GZQZkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0460292f9.mp4?token=o4dO8r-DJeUzBKWtG8uIOKb8NGlzeMS6TIhvx6d5SKzmQv_EnieGoU3p2lNyMBYUHDVbjvhCjc1uGVqMEHr2nqOqZZgeGzPwuBtGu0jmoRujFUPRxLE84wLvrWK4d9BrIpvY2y9sUs719Qu-vjne9nOPw5AID2iMvnNjMexARKS3GUHhu38aQM06f1csu1gP7SI3jnUm00-ySnnFfSONBnFrvKc3Ij3RooCcdhoHaeGQO5sSRJDG6NsbI3en9R1QaKEjNtfMCwh0oZ29qKCazyrIQOlrSNoe3zmdaekdTrgOOV0pUt77Iq7tWC0DbPFHdLOr1FmENiplncY0GZQZkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بزرگترین هواپیمای برقی جهان برای اولین بار به پرواز درآمد
:
شرکت سوئدی-آمریکایی Heart Aerospace با موفقیت هواپیمای X1، یک هواپیمای تمام برقی با طول بال 32 متر و وزن بیش از 11 تن رو آزمایش کرد.
این پرواز در شهر نیویورک انجام شد، 27 دقیقه طول کشید و به ارتفاع تقریبی 335 متر رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70292" target="_blank">📅 20:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70289">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GJaHbvjnClKCnUGYvSvWZAkXCpOHNKneIFdrAYXHRwB2aIkShK063vau_73KNyCM1lXtPn4KJ5YqYNYWHmLHYYp2QQkXcF1gDS6lgOhsP8hToca_17ZnyokPdAkXh4m7bi618Z7Ik9WGlg1Hil2HQpYF9MxLOLjf3SI0ZywT3crQa-3nS0lzfVzddDtLDttHtvT5virk92e-_HwZQD8zW7S8kw25CqFchzezrCED4_lStlOvzgvqIE5okWKBIvcuBs5-1lKRsgcoXe7mJCpOj7VyFPZwua-yvtrPH2jKxkuZqZmZEEKbj8hMWl-lk1AW1y7-AuAy7b-YILtgsgidIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c6wIe_KvS-6V1nD4bcJDl_dhnPrsYyhbvui-R_afW8TcccJYjejRY07uV5SAPCDngVDPBj2RPYOTKSqEs78ed6P1q566NoI5XqYvrXM_cwWqQLG_1CcOg4fsUdKUgR7rxLj_fDgYGFf7gQcxSMz72jV1ZUWzMUfTmM_YYUbJx8gtBN7fiVXDnCkO9AncxBwfarUxdESTVjLowbBkcshxH7yMVRiMe_iLW2rfH6g4QhxJ68-rAP5aUc_ka1Cxzk9-i0x3zJFWR4uZ2nY_fcXZ5PGy3aekDsoD8PUqhwzUbn5ab_t53T2AJfnD-xSBzlpJF65KwZXYf3ERmEQUmtnPow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f8537b12e.mp4?token=rcu-tJH5TlWFrYDyppFyZ0SktDNuaZk4B-AGCdwmOG3U1kbFmMD3B44YUxw7YIeTmqooF_Oz3YjSBrKC7rdj7ONg5yPgdVbfh8OZDbzmalUV1JNptMIM2XpJIj7OmkThspYEIY1ssJJ6D4WzVsgzCqDCU1CZM6M1B9wBVAJpq7FR7aNWXtIb5B6vHVmWu1l0YZ2cJAocMWoANAd-Gzo-YLi4e3TULxlqfl5GQerW6PdNdmWeotbApGcrc-oVwjsH9HmshOAWNY2owbKpfNjGAWQM-dKwsldbUJ34A_BP68sEcLe_WsDapzr8SR3rWnHkxPAou1p0Zls7rteOWDmgVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f8537b12e.mp4?token=rcu-tJH5TlWFrYDyppFyZ0SktDNuaZk4B-AGCdwmOG3U1kbFmMD3B44YUxw7YIeTmqooF_Oz3YjSBrKC7rdj7ONg5yPgdVbfh8OZDbzmalUV1JNptMIM2XpJIj7OmkThspYEIY1ssJJ6D4WzVsgzCqDCU1CZM6M1B9wBVAJpq7FR7aNWXtIb5B6vHVmWu1l0YZ2cJAocMWoANAd-Gzo-YLi4e3TULxlqfl5GQerW6PdNdmWeotbApGcrc-oVwjsH9HmshOAWNY2owbKpfNjGAWQM-dKwsldbUJ34A_BP68sEcLe_WsDapzr8SR3rWnHkxPAou1p0Zls7rteOWDmgVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ پسر ایرانی برای سوپرایز کردن دوست دخترش، عکس چشاشو رو گردنش تتو کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70289" target="_blank">📅 19:53 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70288">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/322a5e809d.mp4?token=gDk6RoKqU4AgvmpL20nDu2AHig0TDHRQYuJWxYkMPe7xgOkGbcRztZiSAT4o5vN7h6F0kiPdoKYbtIpKo1UwL7qvk8jWhb4lPXI-5_VBeqf_fJnQRocoz6nthYPx-m-JHqfTEcw0BMofeEIdAEfjiBNUCl1Wne3XX9FBfq_SRF1KD4Yq4JsZgSWCJIOKWBxZni8rocNlT1hpzWEk2i0eUEzfUJQOIKwaqeObQkMs53W1SSwY_LvGoDpCERLWWfv8ix3RD48tjbQrwy-TicLExCAWBHv7sCrMWaj2OgrCUavtfS3rWANByWhsP_5h1Rj9oV7E82M4f-LLjFjys3_HiDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/322a5e809d.mp4?token=gDk6RoKqU4AgvmpL20nDu2AHig0TDHRQYuJWxYkMPe7xgOkGbcRztZiSAT4o5vN7h6F0kiPdoKYbtIpKo1UwL7qvk8jWhb4lPXI-5_VBeqf_fJnQRocoz6nthYPx-m-JHqfTEcw0BMofeEIdAEfjiBNUCl1Wne3XX9FBfq_SRF1KD4Yq4JsZgSWCJIOKWBxZni8rocNlT1hpzWEk2i0eUEzfUJQOIKwaqeObQkMs53W1SSwY_LvGoDpCERLWWfv8ix3RD48tjbQrwy-TicLExCAWBHv7sCrMWaj2OgrCUavtfS3rWANByWhsP_5h1Rj9oV7E82M4f-LLjFjys3_HiDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ماجرای پیشنهاد قرار گذاشتن از طرف‌ دونالد ترامپ به بازیگر هالیوودی سلماهایک از زبان بازیگر:
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70288" target="_blank">📅 19:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70287">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇷
قالیباف: مقاومت تنها راه پیروزی است و اگر آمادۀ جنگ نباشیم مذاکره هم ثمری نخواهد داشت
؛
از دولت و ملت عراق برای تشییع میلیونی رهبر شهید انقلاب کمال قدردانی را دارم همچنین از میزبانی شایسته ملت و دولت عراق از زائران اربعین حسینی تشکر می‌کنم.
مقصر تمامی مسائل و بحران‌های منطقه آمریکای جنایتکار و دخالت های آنهاست. همچنین غده سرطانی اسرائیل که توسط انگلیس در منطقه ما نهاده شد این خسارت‌ها را به بار آورد.
ملت ایران با مقاومت و وفاداری، با نیروهای نظامی و درایت فرماندهی کل قوا هیمنۀ آمریکا را شکسته و آنها را پشیمان کردند تا جایی که امروز آمریکا که در استیصال به سر می برد، هم با خروج از جنگ دچار بی اعتباری می‌شود و هم با ادامۀ آن ده‌ها مشکل برای خود ایجاد می کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70287" target="_blank">📅 18:30 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70286">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/680c5f174f.mp4?token=egUl-BMR-3vRB5EwKf6Dmj3FdqrB42Zd9ZjEVWnoWhhtasrGTGgmlyM3r0stQxljiBmQyinFSBPzitYBD3JyDPYEOgQAR5LSjt2gaXQf_ppPvaAYQTGwfWjfPz4FmuvksGW1T8iiDil-3xlm52OnGag7vsnBW7FulNmHt9CWG8pZbJ-2nLUN03saLQXVkkkZjyoRZVMUYXhFPEZgEOTGAOmZ0CvDvEPN2ZYlgjDxA1Rio2szBvUBnUhTJQOHX-lTYCsCAEM4g1FVWAOg3sk0rsDyufFj2oNm8r4_JMczTwSZi2NjwBbPwKMnSF3B_m-wF0kJ3MkFf7ZAxmN0484mNX1n9yDhMm4O7b_YO5lJIVv1ah6PnMjdETvfpij1JjSXLUDPr5dPjirhnnW8CJ4wzHYHkGsuhXrfe6XWUyAC0QLr49hcA0N3TaVOssQQNubQin-wyGniOxQZWw7BIc8NsWLOfvBfAEmSgZrx6IAC7KwV-vLB3r_82galTiCjSF5lck66EGDuAupHv-ihu5eHbGpYyHlGxpCsOxVAtdrEdrlOoykCuyQ3uq5MCxBnDJfdul1AccIfjEzOLTslG6FZyzrm0Ssi4SaNiMmwoom77TIQoje4T68GeR4Xo3bWFqLwxTfa0LSzNLfxbzGyzB2rL91xv1ElfunMlCAx7OpoGQY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/680c5f174f.mp4?token=egUl-BMR-3vRB5EwKf6Dmj3FdqrB42Zd9ZjEVWnoWhhtasrGTGgmlyM3r0stQxljiBmQyinFSBPzitYBD3JyDPYEOgQAR5LSjt2gaXQf_ppPvaAYQTGwfWjfPz4FmuvksGW1T8iiDil-3xlm52OnGag7vsnBW7FulNmHt9CWG8pZbJ-2nLUN03saLQXVkkkZjyoRZVMUYXhFPEZgEOTGAOmZ0CvDvEPN2ZYlgjDxA1Rio2szBvUBnUhTJQOHX-lTYCsCAEM4g1FVWAOg3sk0rsDyufFj2oNm8r4_JMczTwSZi2NjwBbPwKMnSF3B_m-wF0kJ3MkFf7ZAxmN0484mNX1n9yDhMm4O7b_YO5lJIVv1ah6PnMjdETvfpij1JjSXLUDPr5dPjirhnnW8CJ4wzHYHkGsuhXrfe6XWUyAC0QLr49hcA0N3TaVOssQQNubQin-wyGniOxQZWw7BIc8NsWLOfvBfAEmSgZrx6IAC7KwV-vLB3r_82galTiCjSF5lck66EGDuAupHv-ihu5eHbGpYyHlGxpCsOxVAtdrEdrlOoykCuyQ3uq5MCxBnDJfdul1AccIfjEzOLTslG6FZyzrm0Ssi4SaNiMmwoom77TIQoje4T68GeR4Xo3bWFqLwxTfa0LSzNLfxbzGyzB2rL91xv1ElfunMlCAx7OpoGQY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
چگونگی تولید برق با اورانیوم:
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70286" target="_blank">📅 18:30 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70285">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">💎
برداشت بدون محدودیت داره حتی ۱۰ میلیارد تومان هم برنده بشی بدون دردسر برداشت میکنی.
✅
🎁
برای مبالغ بالا ۱۰۰۰۰ دلار بیمه شرطبندی ۳۵٪ داره‌
و مبالغ ۱۰۰۰ دلار بیمه ۱۵٪ داره یعنی در صورت باخت مبالغ به حسابتون‌ دوباره واریز میشه.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/70285" target="_blank">📅 18:30 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70284">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari (3).apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/70284" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر WEPARI
😀
😃
😄
😁
🔥
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 120% اولین واریز
‼️
🔥
بونوس برای 4 واریز اول
‼️
⚽️
بونوس ورزشی هر دوشنبه و چهار شنبه
‼️
🎁
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :
Gift
🔥
دانلود مستقیم اپلیکشن اندروید
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
📌
آموزش نصب برای IOS
g28
✔
https://t.me/WePariFarsi</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/70284" target="_blank">📅 18:30 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70283">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇱
نفتالی بنت رقیب نتانیاهو:
باید مطمئن بشیم رژیم ایران قبل سقوط هسته ای نباشه
هرچی در اختیار داشته باشیم از جمله بمب برای فروپاشی آیت الله ها استفاده خواهم کرد
شوروی بدون بمباران سقوط کرد آمریکا فشار آورد و اونا سقوط کردن
رژیم ایران از درون پوسیده و به سقوطش سرعت خواهیم داد
حزب الله یعنی ایران حماس یعنی ایران تروریست یعنی ایران
هر بازوی تروریستی ایران اقدامی در خاک اسرائیل انجام بده جوابش در ایرانه
اقدامات موثری انجام خواهم داد
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70283" target="_blank">📅 18:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70282">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65db328cdd.mp4?token=VhMxsHBSwVkrtEd2Oy2dUL315F_cWLafQ5rGNzYvDAv-bflpGT-3dDZHjjtLFVoQn_SIdAYMrpUmYCsj469mmhJ2dycoU8puCx-g_KkTkpYg6ixF6MJy4nM33yKPHA9nluMcbSsMqAmF64TTv9p01VS0eZxbvovMWragX6jtvZ45a7ifsczjG4ePiZpbkkUcvAALqmVstStsOEnDor3OOE4Npgh9VWuh2edT0yCv3JUtNDf8oUk8nIeGCH_A37pJJCY8cYFEH7rPQyBbJYvTSoINCkPaJ7wrZo2CSdouA8UW4rD-SYfKFclPceOuOQZugiAqUEPpnKbcZaTqyTZbBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65db328cdd.mp4?token=VhMxsHBSwVkrtEd2Oy2dUL315F_cWLafQ5rGNzYvDAv-bflpGT-3dDZHjjtLFVoQn_SIdAYMrpUmYCsj469mmhJ2dycoU8puCx-g_KkTkpYg6ixF6MJy4nM33yKPHA9nluMcbSsMqAmF64TTv9p01VS0eZxbvovMWragX6jtvZ45a7ifsczjG4ePiZpbkkUcvAALqmVstStsOEnDor3OOE4Npgh9VWuh2edT0yCv3JUtNDf8oUk8nIeGCH_A37pJJCY8cYFEH7rPQyBbJYvTSoINCkPaJ7wrZo2CSdouA8UW4rD-SYfKFclPceOuOQZugiAqUEPpnKbcZaTqyTZbBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه نفر می‌خواسته از یه دختر دزدی کنه، وقتی دختره مقاومت کرده این بلا رو سرش آورده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70282" target="_blank">📅 17:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70280">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aGnG5uTE5mW8d8nX43rm8afzwCVvz0RaDpjAWFeBRtY_zXrGV0OnTeKA29m0AxpYl1m2DmqKEc5j0qmQe1cxk9aqJVP_p4mr7Mrtpkt-t9NSggBtowbyvx7-ViW41a89JD46DQSMPSx3XnmaM5_-QEaR4JyDSX1L5GC9Iy21OGBAksgtWwfsnfSCKMq3QreIbbPO8nhwwHNer32Aio8b4OMPTIzQzcfFDRHxq4H2fidkJPb08Ib7LFNj_jD85DCwVIPt87Kp9H8emprG5PQPU3l_vSeTxzh8wXARW7UebJVi-vUJO5bD65cT5DLy6aqOMnjVaQKHKcrCgyHbtP5FDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oW4nJ0SKEAGQ7Q-kk6u9T2dTzXa3BNnMvRlss048Yga75pPMzr-CRUs5lxlEyTYTLMsQfHHlDS8KymbEPuSPsLbsNpkwojTUjYgdVUnOj9AZD6RkR2T8cJVznlSD8zQjE8ufSGf3vxdDtqSkTXUU7txk6-fR5MpZlNOPuz9jB3IJPAleNhcKiyu1KyeIxOgSfFSWC46eLJeNlQ62fhkIGxa89mYxgmmf71_wx1JL9dt1k1z1egKmyJF0hN3NOMcj3wtzP9S8-o-XEubZa_9Zh1432APLEyR1GGWq1jertNyfxps0Z5Xc2Y-5S6lL6mYPgVlwU0FBGzCmduy6TBR8aA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
روبرتو کارلوس، اسطوره فوتبال برزیل مسلمان شد و با یه دختر به اسم سهیلا ازدواج کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70280" target="_blank">📅 17:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70279">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0a5de821a.mp4?token=oSX33jrssz31db64Z5B3d7_ecijaKUPGdkILp7WkVlxsKU7C4IhoOsvoF029hS8ziTpvoin_Sdha-Vi6pnMpEoQLgKa3nC86TOmHKu1Pmploi2eTY5l6xlV96veu_B7XHoh30-2BP5iHPP4uB6l0KvMEv56fZd0Yy9C3mu41DtWdVKmQ_vWZfEHXKKAdoOBCsYf0xFODyhJFXOgVf41JbsbAtbAWdoOqCSSUho7ghqOrv93JWcE4AttuKEcwYb-hB5fAMb2jxvRPSSafbnDYdsGPitp3VfKm4vBhecBQ6NSl56T-oD321wRLZj7KNEdzV_CMFLjJXR6yjwd6uwd2Oa7eWDM4_pCu_tBfSp_g0TDoV1I7ITsZkhhdQLBeWqs6WNium3-tQGfrZh_5CJjlRDaEfLaMLR-3czB26iCoxZ9pDVJn-w3Qz3lCV8iLXP_LpwmtmlHkvQ8zBbo1OztGDADYdTRVMgf9Ueza08vyVm7ovYO6vK32jM3-0Ud2CVWvQ8kSi802mmC-N5Z6cYd1mDDeqBrJLNHxhVAuX5ayhEpjBNbv7uKiybV07bEOc-VBxSX828MsDogAiQM1-8tqB6SoyBWK3AU92iJQFu3Sv-fJunzJiryGMxv68ICe1nwQ_jACqKvCK0q4g64zRrpakpsTSAp-ymLNPWCsqMZBHdY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0a5de821a.mp4?token=oSX33jrssz31db64Z5B3d7_ecijaKUPGdkILp7WkVlxsKU7C4IhoOsvoF029hS8ziTpvoin_Sdha-Vi6pnMpEoQLgKa3nC86TOmHKu1Pmploi2eTY5l6xlV96veu_B7XHoh30-2BP5iHPP4uB6l0KvMEv56fZd0Yy9C3mu41DtWdVKmQ_vWZfEHXKKAdoOBCsYf0xFODyhJFXOgVf41JbsbAtbAWdoOqCSSUho7ghqOrv93JWcE4AttuKEcwYb-hB5fAMb2jxvRPSSafbnDYdsGPitp3VfKm4vBhecBQ6NSl56T-oD321wRLZj7KNEdzV_CMFLjJXR6yjwd6uwd2Oa7eWDM4_pCu_tBfSp_g0TDoV1I7ITsZkhhdQLBeWqs6WNium3-tQGfrZh_5CJjlRDaEfLaMLR-3czB26iCoxZ9pDVJn-w3Qz3lCV8iLXP_LpwmtmlHkvQ8zBbo1OztGDADYdTRVMgf9Ueza08vyVm7ovYO6vK32jM3-0Ud2CVWvQ8kSi802mmC-N5Z6cYd1mDDeqBrJLNHxhVAuX5ayhEpjBNbv7uKiybV07bEOc-VBxSX828MsDogAiQM1-8tqB6SoyBWK3AU92iJQFu3Sv-fJunzJiryGMxv68ICe1nwQ_jACqKvCK0q4g64zRrpakpsTSAp-ymLNPWCsqMZBHdY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو بازار تهران مغازه نیم متری رو 15 میلیارد فروختن
😳
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70279" target="_blank">📅 16:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70278">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">⏸
نگاهی به تحلیل زنده‌یاد مانوک خدابخشیان درباره نتانیاهو(حدود ۸سال قبل)؛
از استراتژی‌های اطلاعاتی و ضد‌اطلاعاتی تا نفوذ در عمق برنامه هسته‌ای جمهوری اسلامی و دسترسی به اطلاعاتی که قرار بود محرمانه بمانند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70278" target="_blank">📅 16:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70277">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coEmQNJysMv5Z_WNFdvv9GAAKiMCWr5YNVxRJZot88oQC0LzFs-5xkL5plkzsv379ScuFeeliZi8ChLFSTnmhFf--atIZYNuxZOf7MyQB0qa6DSUgGeSRT1QTBZ5y_8qMhbDbof6vq-Jb5Vq3Pl7Zi6Iy1Il12pxYKQQPwqSO-VWIrIbTcGnVUCNhWLL3jRBkGZLnfOpS5WLxbxI3EsUbOEPfiTMkLB8PgLPBFzvzVNUQOHOBD0xi_bE37a_Tqk0bYyOCN46BSKOqm6Px2rOU5l2pl4kCFFjKctEFBqdQL4C9nuZm5diNJoz8MDfqrrnc8BXx7wnEk-AqZSKlTXoJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
یاسر جبرائیلی:
کرمان، عملیات فریب بود.
بنزین: فعلا ۳۰ هزار تومان!
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70277" target="_blank">📅 15:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70276">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029120d212.mp4?token=XKOqCluICKhqiU3cVDV8HahYV752BKF5ESgdmybL1eXzfkQZYx6s0s2wPEoyJHwdZc2EQMcTU2jggjkDlDzBg5M569Fczxl7dn7LaGY1tkGIcJcdaH2lPYceMGE8OLfhmTItGB7Kl3bcZ9xbWj7ujrrADn-nFBvV818MI_rQ5QS5gWXocSj29RN9Mwxzs6FVxE7lEB7chWX3vD9IONKJwMOKEgqqx4l2lUXLJMxdO55MkjMsMoVh1YJjm0m7P21M0-PufMqYUVPGwAP3vVEHEv5zb8by5nB_FHLzN2Hf24E_4M_ifJOfW4Qim4hY8RSfhJp5-i5tYKsFPo3sdZ809F2WTThEUn_-OkklVJtniqYgFfTITbW-f_Bng_HBGPWpimAb0UhN0a065Ya8WGc7JLNURg4pW0or5X522Hx2ZxJOHj8GJZ0UGuYw5JrFMvyQ4XN1-Pugd81TFdEKeYOPAMLETCvSyIucgm3zz3dZ5NYoRuiDjwqwOPNrPIo2RtVeFWKlGaQTy8sr0fUbhKarCxawC7SVXge89owkdUWcBRYGl8ebf3IPzRjYB9T6QP8vw-lKYXM_mfqPwR1a6PiN3_gXIHoNp-YE9MuVu3pSKotS4oU_TkEXOLpcFeEn0IdE49FjK1bFQNxxJ-08oyCPdT6-QdIudK_A3VPl9Lxr-fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029120d212.mp4?token=XKOqCluICKhqiU3cVDV8HahYV752BKF5ESgdmybL1eXzfkQZYx6s0s2wPEoyJHwdZc2EQMcTU2jggjkDlDzBg5M569Fczxl7dn7LaGY1tkGIcJcdaH2lPYceMGE8OLfhmTItGB7Kl3bcZ9xbWj7ujrrADn-nFBvV818MI_rQ5QS5gWXocSj29RN9Mwxzs6FVxE7lEB7chWX3vD9IONKJwMOKEgqqx4l2lUXLJMxdO55MkjMsMoVh1YJjm0m7P21M0-PufMqYUVPGwAP3vVEHEv5zb8by5nB_FHLzN2Hf24E_4M_ifJOfW4Qim4hY8RSfhJp5-i5tYKsFPo3sdZ809F2WTThEUn_-OkklVJtniqYgFfTITbW-f_Bng_HBGPWpimAb0UhN0a065Ya8WGc7JLNURg4pW0or5X522Hx2ZxJOHj8GJZ0UGuYw5JrFMvyQ4XN1-Pugd81TFdEKeYOPAMLETCvSyIucgm3zz3dZ5NYoRuiDjwqwOPNrPIo2RtVeFWKlGaQTy8sr0fUbhKarCxawC7SVXge89owkdUWcBRYGl8ebf3IPzRjYB9T6QP8vw-lKYXM_mfqPwR1a6PiN3_gXIHoNp-YE9MuVu3pSKotS4oU_TkEXOLpcFeEn0IdE49FjK1bFQNxxJ-08oyCPdT6-QdIudK_A3VPl9Lxr-fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند شب پیش تو یکی از محله‌های تهران یکی از هموطنامون یادش میره که آیفون خونشو درست بزاره سرجاش و الان یه محل بخاطر این حواس پرتیش خواب از سرشون پریده:
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70276" target="_blank">📅 15:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70275">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6a9c2f6f7.mp4?token=IgNH1ithPucHtZvSc-Y7VSIlnlA6oj_nF_K-e1WlEcPxBTKtN1y3lQ1Nk3cQL5OGEqZFTQHMe0AFeFaLP-IryU1OtIXuY7ibw5BGuFdr2kkSMgavFMVpq4aN_cUUZ-CotnPXDQzXqRvtKAFfhTI51udPCdnXdSdZ_9zUpThslZDjewdJHPiWZzlJl3YRGdreoQq2HBTn4S1dLRndAhsW2j3C7HodvNjQPtDz-VKFlZsiYhEFocs4HlzXBPN8w8_b37uoD_y6L1vep5B7Vg4bdxC7GW7_9kF_emlyIRWtKyZBR9P2E8S_AOBopC0jgc8dar5WKhlhnwzLHoXbbRZPJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6a9c2f6f7.mp4?token=IgNH1ithPucHtZvSc-Y7VSIlnlA6oj_nF_K-e1WlEcPxBTKtN1y3lQ1Nk3cQL5OGEqZFTQHMe0AFeFaLP-IryU1OtIXuY7ibw5BGuFdr2kkSMgavFMVpq4aN_cUUZ-CotnPXDQzXqRvtKAFfhTI51udPCdnXdSdZ_9zUpThslZDjewdJHPiWZzlJl3YRGdreoQq2HBTn4S1dLRndAhsW2j3C7HodvNjQPtDz-VKFlZsiYhEFocs4HlzXBPN8w8_b37uoD_y6L1vep5B7Vg4bdxC7GW7_9kF_emlyIRWtKyZBR9P2E8S_AOBopC0jgc8dar5WKhlhnwzLHoXbbRZPJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
واکنش سرهنگ سعید راستی به ویدیویی که از او در اعتراضات دی‌ماه منتشر شد:
تو جمهوری اسلامی اگه دیدید دارن یکی رو می‌زنن و تخریبش می‌کنن، بدونید اون طرف کارشو درست انجام داده؛
تو 32 سال گذشته کار من فقط مبارزه با ارازل و اوباش بوده و غیر ازاین نبوده.
تو فضای مجازی اومدن با استفاده از هوش مصنوعی یه کلیپ از من ساختن که توش با مردم درگیر هستم؛ در حالی که اون کلیپ اصلاً مربوط به من نیست و سر من رو با سر یه شخص دیگه جابه‌جا کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70275" target="_blank">📅 14:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70271">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nnIRITYZmVz3J6IrBEvo4t3fgNuYjdpMJYAvnEr-9OTLMZyFY2pAw_hc1T6vaQJEhWPjG9aa-CtTXIyv1trqWbTzTZ4iLsxcLRdpUnE9IUpkLhKSJYuoOSh8n8cK-MqEUJdNSpFoBBRxR_FHxnSHjrmfLRzRLzw23t9lZ7M3CBMBiAm31QtYp5hW7bpp4R-1SvqY1bHigPrJ7YQhjM9--_up-rO1cWvc5JjUBJIXJCY1ciZgTnTe93mXogkEsuUTXY_Eio8dLW_zEfePImAy9YKerJzkeW7vWWYMcoR7qJxteqvtSRGBbReZlu9-wcmlfLyp2e0io2IDEkhFj4vNhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rcrhMHY-kCPTiOe9fvfQ5mAbl0tNg7jkHjeZ7GwbRCAQlRvW5eMNz4m8Elzvq5_jUPdQlLbYF9VdOb-FNlNlnRzCo1KJrJPeWIHIeXqv8bMUc9LYeuwrK6Kn7RsbxHQ2Y--PA3t6n9z4pJeWduADJt1tmUpdWkV-We1KaiNLDZtZopjr7PdlmgibUvgJcNl8BQBvDd3X4WBTAaxpgvFq-Pe55vR1mdg2I_nuZAKM2Xgt_jS0vWDI6sRuoAZmKoJe-2W34aGuB28aq3wVr_3alkPsdSzxlgXSFoME0su1-EDy8WGTNoMaYzbr_7EWae-yr_AGjQILX2Vg1t5D63oKLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc313b331.mp4?token=H9vWb3LQmX6c3pJm3l2ZIxeFaU_NiLId7H3C-SKBIBdSe7ov8hMjiYbBy3LC5zP1A16M0_48yl1LE8hlzLI2HQ8YAwMTwMxG2GTMJ0QFjOfLLkbiKqLFpGKjDsRZZpeXNxEdO2tzdgRVGK2lspsoUbnal9Z-_EPIskKuLYpr1tlbVD2gsdrFs9Arc6QyarixQ_fs3Z3o5U_PYqudBQFLRSyZfVX1oHjiLf0eXUzNPuDg6FcqJ51FCaT9QUOhHvGxfjk5zBiwp83yzxGP71ntjfN_aflNJfaa6f0chHXxc76H9b_Mv6_iAuPf3kyPW0YRNukASJc4k2zCQ-sMlBQNyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc313b331.mp4?token=H9vWb3LQmX6c3pJm3l2ZIxeFaU_NiLId7H3C-SKBIBdSe7ov8hMjiYbBy3LC5zP1A16M0_48yl1LE8hlzLI2HQ8YAwMTwMxG2GTMJ0QFjOfLLkbiKqLFpGKjDsRZZpeXNxEdO2tzdgRVGK2lspsoUbnal9Z-_EPIskKuLYpr1tlbVD2gsdrFs9Arc6QyarixQ_fs3Z3o5U_PYqudBQFLRSyZfVX1oHjiLf0eXUzNPuDg6FcqJ51FCaT9QUOhHvGxfjk5zBiwp83yzxGP71ntjfN_aflNJfaa6f0chHXxc76H9b_Mv6_iAuPf3kyPW0YRNukASJc4k2zCQ-sMlBQNyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
امروز تولد جاویدنام مهرداد مشتاقی 27ساله‌ از اراک دانشجوی رشته معماری بود.
رتبه 200 کنکور سراسری
مهرداد 19دی تو اعتراضات اراک با گلوله جنگی از ناحیه سر مجروح و به بیمارستان منتقل میشه تو بیمارستان عمل میشه ولی به‌ دلیل مرگ مغزی جونشو از دست میده.
روحش شاد و یادش گرامی
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70271" target="_blank">📅 13:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70270">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9_XPZTRwE_JfuwhMBeYVBp_YJm9MOLqtzTCxFO5GieiRd-ngkzUds9goMH4ovWdFfBxDFm1o7G6E8HWGT6lekjC1FYT1F_z7_gwk7VWa6y9e13ToTl9KriI5r2M6MWI9JCIxGAa2EkOa8Ob7JyGGL0i6x5QiyGGeLJEDAGEWYAdML-XsWPs7e6Zf-dPS2bs8JuchItW2p2htsbUsZfziwvmvmRpsacQpXA3r4LucOjpmSk_2Win5r4VyzqtkB7vnAomu0sJtsU57vT3fzr11LJy0xm7aZMf4KK3HxANHgNpmqLpvaU7beVB4NUw9BrLurxWkt9reTzwp2KB-f_s9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری جدید رضا علیپور : جنوب لبنان که چیزی نیست تمام دنیا فدای یک وجب از خاک ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70270" target="_blank">📅 13:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70269">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WE1Aps_huKyhH88A33r46qwz5aHdMrxJVQLon-RImi4nkA41GsI5IJRcAaWcN5NYYTe-XvPkAWLiAAaSSNN9100q8P5PyRgHj8P2Z6Dy9EEwWL86VGmx139PgSrNd8xazOLwwaWXjsjo6glcBzt6LoUezYAOkR8mvnNPrmKRIiYUBYwTiKfbVIm8ReMY66P0ofgVPnyfZzUQcLLkiHZ2v0ilmfVmvfwMdAcnDvEWTPox3wBoP6598hKHlU9llkfoIx5QV8RdCKdB5uQi-ZCndmXsGMywB0UpJm4tU-kwTcdSW_JGCzY4kryqqlgTmhVeitiUDUEtLTWf3Tzo2sxynw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فایشنال تایمز:
ایران در صورت تشدید جنگ از سوی واشنگتن، حمله به تأسیسات نظامی آمریکا در اروپا را مد نظر دارد.
اهداف احتمالی شامل پایگاه‌هایی در بلغارستان و قبرس و همچنین کابل‌های زیردریایی در تنگه هرمز است.
مقامات ایرانی به‌طور فزاینده‌ای وقوع درگیری مجدد را اجتناب‌ناپذیر می‌دانند و هشدار می‌دهند که حمله به زیرساخت‌های حیاتی ایران می‌تواند دامنه جنگ را به فراتر از خاورمیانه بکشاند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70269" target="_blank">📅 12:34 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

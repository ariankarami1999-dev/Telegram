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
<img src="https://cdn4.telesco.pe/file/LXXJysPkfnr6ohUwwySTf_PLF1oj5fiy1NAp47WWeQrAWGddwEtwj3eNK5YwIALbs7BoLCSmD1bJmTPfxI42DsY_satgGzeZdVmBikov0lglnS2KyWOhsNScdJhTzhROVqcjuluSloIvWe_CyNrqTsxx3GL2hbA7GC3sXTZmu19eD8pP4ii5VTyLbo2FgzAaWVSCnX03CbuO607R14eWaBVCBxNy0aFFbQJ_UC097_t7zX-5tLnm_g62CqAo_J_3JtdOeDBqyQLMMIBtk167HLBHfe3BAs2jAV8oAGNLP6tDDStik_H1RtujevZxAwFCMw0kIO0ZKgeMWaJJhHnzGA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 966K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-25 09:54:26</div>
<hr>

<div class="tg-post" id="msg-141985">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rFKOolSfAqX45m2KK5bLnwaPp9DQsnIDk0t5EZft7LrPePFQ0ZeIUzwe6Lqeq-sKkYUNGMVvNiX4jjXmqS1R3TJmHvNf8fg2u7Um1pwVA4e8T086FdFECPN7LbBF6sroNJUNCMBvCSfYrCkxAjDSd-MWGY9KbXWR6TM49rjwdrVr65hKrluZqeBWa--l342bc79vgCQTJLmO4_EigBbzpSF6t6d0XClEVFTzqCVbRVw2Uqg-UVMfCmeDr9K_ZcfAaHRST8Pt0xrHv8zQWg-NXzKFM8sCiyGuxA8szX1MLBaHOpXkxSrSufKn2wNKhyfxciIWaWQP9ZIYNF-QPEMpcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rMNe_ZD7ng5NqquTRJjSUI9iK3JDt9839lZkKAznmRMq8briA8HhVzXXWrkL_DfUic41fYL_JbsuZErsQQozz_p1KNbcCbnaMr2oSGRePs_w7DWWjk2xR-IRyXWgUuBGLcxHWVD-59hNYsSrHxB9W6lmNcma56l8x2FtlOig2lZMd_flNcoBmKEXP2r5MU1DgYl7d6aCWrlO4dYq51zZAgA2xuIuz364GFPD1I3bXAjVVGaPiy54bvjuSOjqCLb9pUTaUU-gg6hRWAKJm11772G0RxFjU_FiMrMXHSIvmdl70wo6IZOqRnWKq1j9slWA6eqZ_phBor0iW55jheBIYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B9kssWs6aVbTaK19PKVG7xPu84aAUiNP7aKlWp2y1DHB2Sg6ffhvX5Lve9C7WUigHLvb7nIBTyHJgmyrY60BgfVK_TIBw6flirXmzPNHh6jDc_CT40FrdHgkG5pQnmca9KUe5-e-5NjtpyEP7XWxd7RpqMtBUY-L-Wm36Ay7sUnxyOsHHuGjttvkfL1m9rwpheDLn2jJuoMWPj0dc_F0S26jnd6nDjo8SjB-IG7FrLVQoJHlIAYh-_G6e8VFLursexmuLxg3RT61JtZSBDT6nhokp74PGYlhPuGb4vx9FjD0fzw7-8P32XDnSNc8Lj8l34Adi821GY2B00tsxaYScw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee38384b8.mp4?token=N9P56vlFdWLR2CMYLBJB8-iFUjVMnc2IQDlleLWtsoGPqY2IxZUFp_7gU4zdyXL8f3WK-RXvzWsVgF7YWXmWtU5AoGTozhko_Cc0bJrZ5bzQDYmg4ToFOiPkWhNgRqa08U57aqVmb_XR-q3THWshd9vBCv9tUmpAygPt50_fD4mlnwrMVZX8CrXZH4o6rd3dfPPtr0WdN1Cjo4-U9KPuhAF-R77SzmSol4nYodzfuz1OHFNEsqWiEuqd2MNHMa9cWII-pzPbJMfkTsU_qB3ZeYkBobgVbKUPV6SN0xmfke801WpQomt2I9Aw90bXHcrQ9LW5mVGGQ1pGuvHNm073Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee38384b8.mp4?token=N9P56vlFdWLR2CMYLBJB8-iFUjVMnc2IQDlleLWtsoGPqY2IxZUFp_7gU4zdyXL8f3WK-RXvzWsVgF7YWXmWtU5AoGTozhko_Cc0bJrZ5bzQDYmg4ToFOiPkWhNgRqa08U57aqVmb_XR-q3THWshd9vBCv9tUmpAygPt50_fD4mlnwrMVZX8CrXZH4o6rd3dfPPtr0WdN1Cjo4-U9KPuhAF-R77SzmSol4nYodzfuz1OHFNEsqWiEuqd2MNHMa9cWII-pzPbJMfkTsU_qB3ZeYkBobgVbKUPV6SN0xmfke801WpQomt2I9Aw90bXHcrQ9LW5mVGGQ1pGuvHNm073Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحنه‌های اضافی از آتش‌سوزی در انبار Wildberries در منطقه کولیدینو، منطقه مسکو روسیه، پس از حمله پهپاد اوکراینی
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/alonews/141985" target="_blank">📅 09:51 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141982">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpydTvONKk9rvinF7rFDHlyaeTMWhPYmql6UZ6UoDHR_4ONS6RkIMHQQpWH8bYW4SL7cDA49cZoZ1-R6F_ZcmF7fz6BNsuYrx1hYJ7kqZTo5x3N6k2yMZPGd56ish7atbYOhyWN0j9Qj_wP02_0Ozw_swXeIt0TI_37afw7DzmQOWfZp9hKOujZXYYYd8_7by56UqH4m4XQaWiyugviMRwxgT9XYkj0CtS0xZo541oIgME09bwQJZXQ3v4O9o3pjvyfmzQONGkFsUl8V5ymCJ5lY3AQpokE_74VqnSkyD0c3zSWe0T-Wf_EMi0koTmwjgLQP8tofD2z8lmj1kGvCyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3138a8e31.mp4?token=Rg0wB0m1fWVIRcqgbfgWp2BFf0LLh126KP2L9Wh9dZcspEpABiaFzlm2qA2M4OI96oU-l8amb3vh7MpQlXxQaD5ACqL4YOFl3w5Je-d26Gcsrb9hzvKhC9-ggiNn9NESPyKi-KVJmnzcwmHfqEG7lng-snppI-yD1lerRSdirF90_UjA-avSsPbbY90Q4CZfpbP1n5PJjxcbOzKWxTwfKFe2lh60jMhANpTPQMoWvl6T1SOtJ3UnY_qrBwTA272I8lm-FvHJ2Wds3AYbSNRLy1TOtjcS236dw4kVQykMUtDSEv35wemNkNF63C0RsioWFFzkfCkEVLW973Xvpbxokg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3138a8e31.mp4?token=Rg0wB0m1fWVIRcqgbfgWp2BFf0LLh126KP2L9Wh9dZcspEpABiaFzlm2qA2M4OI96oU-l8amb3vh7MpQlXxQaD5ACqL4YOFl3w5Je-d26Gcsrb9hzvKhC9-ggiNn9NESPyKi-KVJmnzcwmHfqEG7lng-snppI-yD1lerRSdirF90_UjA-avSsPbbY90Q4CZfpbP1n5PJjxcbOzKWxTwfKFe2lh60jMhANpTPQMoWvl6T1SOtJ3UnY_qrBwTA272I8lm-FvHJ2Wds3AYbSNRLy1TOtjcS236dw4kVQykMUtDSEv35wemNkNF63C0RsioWFFzkfCkEVLW973Xvpbxokg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای اوکراینی به یک مرکز لجستیک ویلدبری در کولدینو و انبار دیگری در دوموددوو حمله کردند که هر دو در منطقه مسکو روسیه واقع شده‌اند.
🔴
هر دو انبار در آتش سوخته‌اند و دود آسمان منطقه‌ای را که درست خارج از پایتخت روسیه قرار دارد، پر کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/alonews/141982" target="_blank">📅 09:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141981">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiQYf6ANv0FHMAfGW_y06S6VpHdc2u1SnpvFGGoCdvA2KY-tM0jTGZhCn6ArAubAo7TJ34uhmA6Xui0y0MRj_5dkL5iCp7K1n3yXBRhhvV6GOuvCe9HuiD2Rl6k2NeDIcZylXPQOC5djvF-lGZg8iClDFzqgecbmgn697bmGd4k9j1tILHP436JGIs32S5aX7sru2WkYCicpzpjKl1ai2o05WkuzOM7Jq-gXtYEmPdrnFUzEg6Mkc3us-JdURXoqLtnn4tf2YOSxBvcOW9gSwkfkz1DD4Nssy2SlsvcApV6KN8elh-vuZtOhUMAzu5VoAMR1_OJJc7d4QAjo0vdhtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری میزان وابسته به قوه قضاییه از اجرای حکم اعدام شهرام صادقی، از معترضان دی‌ماه، بامداد یکشنبه خبر داد.
🔴
صادقی از سوی دادگاه انقلاب کرج به اتهام «اقدام عملیاتی به نفع اسرائیل، آمریکا » به اعدام محکوم شده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/141981" target="_blank">📅 09:24 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141980">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
آغاز پروازهای مسافربری میان روسیه و سوریه پس از ۱۸ ماه
🔴
خبرگزاری تاس بامداد یکشنبه گزارش داد که پروازهای هفتگی مسافرتی میان دمشق و مسکو پس از بیش از ۱۸ ماه از امروز ( یکشنبه ) از سرگرفته می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/141980" target="_blank">📅 09:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141979">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
یسرائیل کاتس، وزیر جنگ اسرائیل: هیچ حساب باز در هیچ جبهه‌ای باز نخواهد ماند. ما با قدرت از سربازان و شهروندانمان دفاع می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/141979" target="_blank">📅 09:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141978">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4zDuDgc06bBYJFwqer1vrhEks36_2B1v9rpwJZjurXZ9d8BWujzPiv0Ilr9YwwFtJ7RzgGV_0POv86CbWsKmW0oaYvBB5QvlLbTw1C8GlYwsA-7vtAsgllsKGb4D6E2m4W16fTjxVI_MTBMZhQCzrc9iY4EzZGNtPJ3LCwAooTCJV2djmcOGh8Q_NnHVHTmWZJ_sHaUNbUph6FSEQpwJRk0R2Y5bSCwF2PZpM4_GFdpYT-xjay11Desfk1jdtyew3HN0nhGvk26r8n3c8vj4AaMEkdk58h55wUXiPuBoZDNyrU4BZEz5Lt--R_Q4CyzmrGScZ4q7_kjrLp1Hf8bDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه ایران، اسماعیل بقائی، با مقایسه انتقاد مارکو روبیو از اولویت دادن ایران به هزینه‌های نظامی به جای مردم، با اظهارات دونالد ترامپ مبنی بر اینکه ایالات متحده باید «حفاظت نظامی» را بر برنامه‌های داخلی برای مردم آمریکایی ترجیح دهد، از دولت ترامپ تمسخر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/141978" target="_blank">📅 09:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141977">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d33efc20a8.mp4?token=V9mhRtxUnyDAYupRrr8Lb1ynxmyZ7mBgZ4_LM5KCFg-u61-spKocFxRnQHXIu44oNcdzZK_IQu6gBDllLnGlGk7GccAf9zHMUi6amAPpZhXsIpFYBctmI65k7K--EKcyWaMD4oddIihfFcYTdUdViKjtR5se6RMNoZhZni7LzEkJU7qJifTpwLV15nyeKfgGeERGftIY3VC9vUUZFJ1N6-7R3soJ6xUonu4z8VaTJ4YwcSpQvr_kxNvbXfbceL1pw-zH041dLQoL-GTUIqPlKx80kp3CycQ0KNtQQfbjFwXJtKyLKtpZcLur_ieDkTcPbMuOLd6sWosvDKGCeLSCaw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d33efc20a8.mp4?token=V9mhRtxUnyDAYupRrr8Lb1ynxmyZ7mBgZ4_LM5KCFg-u61-spKocFxRnQHXIu44oNcdzZK_IQu6gBDllLnGlGk7GccAf9zHMUi6amAPpZhXsIpFYBctmI65k7K--EKcyWaMD4oddIihfFcYTdUdViKjtR5se6RMNoZhZni7LzEkJU7qJifTpwLV15nyeKfgGeERGftIY3VC9vUUZFJ1N6-7R3soJ6xUonu4z8VaTJ4YwcSpQvr_kxNvbXfbceL1pw-zH041dLQoL-GTUIqPlKx80kp3CycQ0KNtQQfbjFwXJtKyLKtpZcLur_ieDkTcPbMuOLd6sWosvDKGCeLSCaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تجمع و شعار قربانيان مهریه درب ساختمان مجلس: ما اشتباه کردیم که ازدواج کردیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/141977" target="_blank">📅 09:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141976">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
وزارت دفاع رومانی اعلام کرد که یک جت جنگنده اسپانیایی مدل F-18 که در ماموریت نظارت هوایی ناتو حضور داشت، یک پهپاد را که به طور غیرقانونی وارد فضای هوایی رومانی شده بود، سرنگون کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/141976" target="_blank">📅 08:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141975">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ارتش کره‌جنوبی ادعا کرده طی روزهای گذشته خط مرزی نظامی توسط سربازان کره‌شمالی نقض شده و با شلیک هشدار، سربازان کره شمالی عقب‌نشینی کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/141975" target="_blank">📅 08:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141974">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4860f711f.mp4?token=D3nZ_BIvXVlbvu-3Z4lkiX31FxZvuB2uh5NPH1mpnUtztZs4BALBhZ8s6LTktwtvz-HwSYeK1X0Itdcze8vv-phYy5VHK67jutiNL5vXwsDEXNwy4SENwtuQdJLxqQXKfTNsttmOJ5omhWKpbl0NtBA4-mOwIaj48Zgkw6dXKnkK0oW_TxfiC4oir87ingZGaJkx5Y_I1mCOa_rin_Dh3bua_VIyKQOBc-zF15tZsVkt5ULiAj69qHsnqpAHFR1YhXHIzwW8gh7XtxqqZ_NTdmVmfQOkZpLb9AJj0-Pt3IfQqpntpcLk5EtIRpQHnESYOSkrUOdTDa1QzIwT9XCnfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4860f711f.mp4?token=D3nZ_BIvXVlbvu-3Z4lkiX31FxZvuB2uh5NPH1mpnUtztZs4BALBhZ8s6LTktwtvz-HwSYeK1X0Itdcze8vv-phYy5VHK67jutiNL5vXwsDEXNwy4SENwtuQdJLxqQXKfTNsttmOJ5omhWKpbl0NtBA4-mOwIaj48Zgkw6dXKnkK0oW_TxfiC4oir87ingZGaJkx5Y_I1mCOa_rin_Dh3bua_VIyKQOBc-zF15tZsVkt5ULiAj69qHsnqpAHFR1YhXHIzwW8gh7XtxqqZ_NTdmVmfQOkZpLb9AJj0-Pt3IfQqpntpcLk5EtIRpQHnESYOSkrUOdTDa1QzIwT9XCnfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در پی وقوع تیراندازی در پارک «چارلز یانگ» شهر لکزینگتون ایالت کنتاکی، دست‌کم یک نفر جان خود را از دست داد و ۵ نفر دیگر مجروح شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/141974" target="_blank">📅 08:48 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141973">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-O--S_l9JhUERQxesM9wuOI6t-wZLRldFahrbyVlYm4DUavEmfL7x0FRGmngWG8FacWwNkhm-npCbGROFuyBVspez78Uj5gDVuKTJpHgkDkyvE-BNz9rJ61AdrblMiUU00DwC0OXFE0lOmYe6KPglPJk2Tad4S_6W89uV8qtMmyoiRoEwEgty7eHpurfL6lIqdX1ksEgzUd2DgdA1olQQpRLqBv7JbwdmQ75UplvEBBEld-g98lfk3QqUQOu9W88diGLL6WFSWXnOJsuMEfrcAfTM4WMOBJlOFFDseoLmCMxojuhjMdV-LYYe3bM5PHeRZGrifZVN5czP6E8C4kUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام نقشه‌ای منتشر کرده که در آن غزه و کرانه باختری به‌عنوان بخشی از قلمرو اسرائیل نشان داده شده‌اند و در ادامه نوشته: فرمانده سنتکام از بحرین، عراق، اسرائیل، اردن، عربستان سعودی و امارات متحده عربی بازدید کرد.
🔴
وی با مقامات ارشد غیرنظامی و نظامی دیدار و گفت‌وگو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/141973" target="_blank">📅 08:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141972">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZeQ6EeoIgYbgVsneT9kCEltJMIhnP65SIOmYDhyWSvp3skvhGl1IR76vqSVeql8akRSYlp4keMHblrnLON-u-77-6eHvXMp_FHJeRCwHodaFdD2b969MDiBom1lK3hPSRIyr38zo-fiYxJFqh77N_Evgad6NOeKgNRw_cT3XOQD4qcOHLhe4G6tDuZedg1r-QdBQSYT4kT9ZyCrihHPBy4kKpdT7_wvz9aA_2-FW_xVboNOPPX2p5qf3CFNmfEhIyhLbh_eSUq2XbFm5QrksRFNUELM7Y3c9UTCy7y9uU9IXoNlmMUlrJgp0VAkdrM8nbV-9cIu7PgzN9vg87AuGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی:
رئیس‌جمهور ایالات متحده باید به جای تهدیدهای بی‌پایان درباره تنگه هرمز، نگران امنیت خودش باشد.
🔴
او گفت ممکن است رئیس‌جمهور آمریکا مجبور شود «در یک کامیون حمل مواد غذایی پناه بگیرد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/141972" target="_blank">📅 08:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141971">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d324cd6a04.mp4?token=vWl-5Q_mwQ_DFVZKgkQeeMc1I7KA4aknytkRiFxFTs1lPahkUdbFwSiF15UW6nHoM1W7YWEfNJ_HTIECH4f16V65UPtx26ehKHqfRI9oVjixsSC65jD8G3V9Pj4P-zXBN0iGd4mHapxnlQd72bBtY8CacKQaL-WEs3-e8Tb5MVBvbMzMby6cgLRNvvgBj3SyCC2wtEQKztf1-N7Nq7KocJfRinRHwWpJx7-eUNV2Sdrh4DxuLwonZwQrtSruWkORrgXGXgjujjIPWDir7x-H88JigUo9W8mHrTZo6wIojUgZorJdyUyAWTgty-yiMzHoIwBT-U2nRCm6YffwN5Pz7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d324cd6a04.mp4?token=vWl-5Q_mwQ_DFVZKgkQeeMc1I7KA4aknytkRiFxFTs1lPahkUdbFwSiF15UW6nHoM1W7YWEfNJ_HTIECH4f16V65UPtx26ehKHqfRI9oVjixsSC65jD8G3V9Pj4P-zXBN0iGd4mHapxnlQd72bBtY8CacKQaL-WEs3-e8Tb5MVBvbMzMby6cgLRNvvgBj3SyCC2wtEQKztf1-N7Nq7KocJfRinRHwWpJx7-eUNV2Sdrh4DxuLwonZwQrtSruWkORrgXGXgjujjIPWDir7x-H88JigUo9W8mHrTZo6wIojUgZorJdyUyAWTgty-yiMzHoIwBT-U2nRCm6YffwN5Pz7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چینی صحبت کردن ممدانی، شهردار نیویورک با شهروندان چینی این شهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/alonews/141971" target="_blank">📅 08:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141970">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/911d977485.mp4?token=L3hMmOyUsecjsl8iFO4nCPJgbnTrJ6kTJxA5zkRT-hFQIJlAOkPtfR4UMVJ6Vyc2Ow8xStwYJoFkL9WbfEDT0aPjWB9MQckcsHrCV_9SMDPUxhIZOJdCzUt-Gv5cFhl9Y3YXQ3_uTwTWGHQFnnzQ-GNU7_3j09quRdbm-ev9Yq-GvDuW7WnWTdPlG1bwBJkWbmiF-yWo2Pngwi-3_F29KLuUWDbbAbiRiYOm-Z_s_r6DEtExaQEsPsdwJ4r67nUs3bZjolWc6iLcdPUEBLRSR_S4BMaIlPuq91WjW5rHoDR3UPex1TVAHfCGuaw2J0MDQyUExLQHsOBXK6orDKDaMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/911d977485.mp4?token=L3hMmOyUsecjsl8iFO4nCPJgbnTrJ6kTJxA5zkRT-hFQIJlAOkPtfR4UMVJ6Vyc2Ow8xStwYJoFkL9WbfEDT0aPjWB9MQckcsHrCV_9SMDPUxhIZOJdCzUt-Gv5cFhl9Y3YXQ3_uTwTWGHQFnnzQ-GNU7_3j09quRdbm-ev9Yq-GvDuW7WnWTdPlG1bwBJkWbmiF-yWo2Pngwi-3_F29KLuUWDbbAbiRiYOm-Z_s_r6DEtExaQEsPsdwJ4r67nUs3bZjolWc6iLcdPUEBLRSR_S4BMaIlPuq91WjW5rHoDR3UPex1TVAHfCGuaw2J0MDQyUExLQHsOBXK6orDKDaMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل برای بار Nام تفاهم نامه اسلام آباد رو نقض و به لبنان حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/141970" target="_blank">📅 01:48 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141969">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/494000c553.mp4?token=vYUWWiOMy2BOvQuGDvS622oEqT8TL6wS5_c4jSAWcjUGkN7me2anFZ-XcyP3PsWvmwQoI6cFsLxrE3C8_OLN3yzeVrJv1ENW91wm1wmayjW_VUYOoNOGMxVugX8xbaIzTOuK9ZnTnoc5sdoXloUhi9c7YAJb9vkdJCCP2DkzG3AZOjhEgvBsQyokdZz2lBd9apMFZ-A8y2mmZgIxrAzRfjtqRbQswil_9HumXPpgLVjf0OCxvLURs4U6dwr_A_oOCL5mwBYaZb3OfY6WPSqd9Ry6H6E70NW7JMHFMOuefV4AMXB87iM8wKkgUxF9zCOLzWG5utV2b2XNmlTnZ_6V7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/494000c553.mp4?token=vYUWWiOMy2BOvQuGDvS622oEqT8TL6wS5_c4jSAWcjUGkN7me2anFZ-XcyP3PsWvmwQoI6cFsLxrE3C8_OLN3yzeVrJv1ENW91wm1wmayjW_VUYOoNOGMxVugX8xbaIzTOuK9ZnTnoc5sdoXloUhi9c7YAJb9vkdJCCP2DkzG3AZOjhEgvBsQyokdZz2lBd9apMFZ-A8y2mmZgIxrAzRfjtqRbQswil_9HumXPpgLVjf0OCxvLURs4U6dwr_A_oOCL5mwBYaZb3OfY6WPSqd9Ry6H6E70NW7JMHFMOuefV4AMXB87iM8wKkgUxF9zCOLzWG5utV2b2XNmlTnZ_6V7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری: تا الان مردم فقط ۸۱میلیون تومن کمک کردن تا ترامپ رو بکشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/141969" target="_blank">📅 01:42 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141968">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
هم اکنون حملات به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/141968" target="_blank">📅 01:38 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141967">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
چند فروند موشک از سوی اسرائیل به منطقه "علی الطاهر" در جنوب لبنان شلیک شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/141967" target="_blank">📅 01:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141966">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKc5pH5i6hCRSKJtGv7_4XdtDv_w8A7SUeQukn010A6A2oB2p936RiaymWViFyYWaHUjOXfk-HUnstOYt0jZ9MFDpGVuz9wk6dC_MUgKj8zIIfNWeNxdMJmVO3W4lDZ_b5K-IDSDLmsAnN4Q2Ik6u4RAKgtqfw0hH9Ip4CTMkrCt19aWSx0xRP2n_PIdS3RZrHWU9tJT2F36iatc52_HqW5-6Mq3sPf6B2e4ydkSFbugti2GQSBKAVA_ySKALhROfQe836Qe4QuHGJoROMT6JVUx8nVQycYnObCexdOOhu9AOVQ9qCTMvO2Y8mK4iFhHohemNDRS9QhqB8uGv4UtVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ساشا سبحانی، پسر سفیر سابق تو ونزوئلا: حالا که انقدر بهم هِیت میدید اصلا خوب کاری کردم پول مردم رو خوردم و نوش جونم همینه که هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/141966" target="_blank">📅 01:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141965">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
اردوغان:
ترامپ به من قول داد که جنگنده‌های اف-35 را به ترکیه بفروشد. ما منتظر هستیم تا او به قول خود عمل کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/141965" target="_blank">📅 01:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141964">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIh8D5cEzt9Dvy5V_kefWO-VapMQ1xafRh20mcZctxQehwg7i-OO1PNFYzfHFrW63xJyZj_oYy7XrI_zJFStHLTH2QOWffuwFn-OGegwRb_cPQJKVVNVv9SWDO3_VKmkZJR3cZhJr0zdCNWx-d1j6I9eI1RW0iagrDmvyHTlYFHvucj4VWyInpB2iVtPXgC8h30-COfNrwR8VjBw7F2A2z5Tp4hYU-1ptEOXhaaTOPwMDtckuOjBzuTvbLmw64e_lLf5858jDwIvk3a9kyB94fMiiigJHrPztpSSymE3LsECbt5J30XlwSzn9AHClfbmkL_WjR0MNxOalLIpSiV5hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف:
دغدغه من از سال 64، لبنان هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/141964" target="_blank">📅 00:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141957">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vNb_e7DSN1KzeX9WJMmU-cG9DvUSl2sPtMN65RYkNME9-3f07g1Hrp0YG1Rwu6BjnAmHjtCFHECsSE1pq40S2M0xRjHkL4Zp9i5aff9QsVyClpSMsyBQJoa8ZbCF-EuDQeWg8E3EtLdxaUrX-l22_CsPDY1gQdWp5btb1CgnBgkvtDO1xjrNrqUYIYkmEoX3mLtF5Uoubvw12iCbdDIBNMHuWs-oAJSI_Hso70gwz8JLQrXuex0IPQPNDwxiIqyCh9LMRH9gYH0Z0THPOYTkBdkJd7mf3PmUoIhC0VICvz2IhKdGbyAa28IgK34lmi3tgFRT8w-Sw9ne9jNHFx1-gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oy5qD9bF184SBl9nLFZY6cnCJGyPcz9JHGqeHrKCT5dx7u2ZkhnK3Umhtm8azVy2Hy_uKUHtyGEBId-ZRDAn_9thG5gek6aalK2dL5J3E150BS9HW44vOxENQFZxOM-_g4yTjgVH4N3W8WABaJtbsiPqddmDmq_23Ju-bgCA50zybWCNTwS7VOmD0kcXARdQs4McPzg84II1g1CuuvnmPuwxgpPsNRQju5coulJZBQdUJJHpWCbll8BbEuomrYK77oFgiMwibx6J4X8Ojq9mCTWmEmpKrWYO5MagxvFlxQBj0l6SmOnDnZFv3D9-ksVcdclab6GYAQi3yMlfnBVieA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YKnkHmQ3yrtXVuvB2WDx2aCsSPqvWWGuJnaCGrMPtlOAsM2ROPs7aFppXmgDZ2kd-gmFyquhwBWaWytzkeJrcqA8MuA4Ru1uo6Sn7zQ1MrjLPsmNOzkiVwm0tvmvCm5JMmxY2ENNJS2kf7GPud0s-ORDoOVACgKdSoTLsoLDe46tjBKfGOPUdicF3jo6OapUTHpsx8JhaICSdEummfd9oJvKAy5_H9pzaAereM68TQ8dOjwvTvAXcehSEtgNcxzB5Bx7gcm3-rIQ0yyLboDZQEwyWgNZYqLJO7GuWrq_VU0re8NxXy9AR0NBD9YvU0AHFRz53kwUyalKxpjO03RYDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KbtP0GRekwEbOA37XFnUAM9saLu9tpRQxEQm7LeTwKHUwSuqjYZ1yD_nkD4J1RSkrNVFnJNIlUblJseH0-IZvyV3FUa93LGoAD3632E6Frkw38HEFHu6yvrgLZ4tU_r8J2LO3wWW7jkAAYHzSGjD3tkY8TEX0nKBS9_Da274uTPRxtKHe3aRP1Xvk3eJibU1UZ4i57WchIeuGANZdopkCPjfKvXVBHeQI_--BMpzl-7Nxeq3ztsZntQqsxGbKlw-wapSbnBujbD7dHm5sNglTXuVcIOr9TiCTQf0FEGzu0o5RVmtKtmyvv8_10qUxQ6FjxyQDr_Iis0HhJEqoQXBRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lF1BsgK3XSczC6D9hX4idiOEhXeluakOdB1JEtvma2ReAOke2bOM3oHw6dCuQkhviuoOR3TEt3apRjH0cmVpskCYRGXnMWsabFzpK41aW6OQK_pkXYLX22Rxp-ydJ6LPLrye5JrKVt2Fj-f2z2di6xkYbkeCpT-6lfc3ATW7GXROrvqeXHl6QF9asIYMdupa-JBlC4vJorbpqwenxluOrTT0uCb6PwtxNNQHWp_rNhNwkyqNlgAwtTCujcbH0INT4Co90SjBv465viIBcNIGGVEYbnvSJhPsklfxB5aEY9F6sKtL4At9AkbicyWgIdKmnAL9orbDRUffee83SmV2rw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f112eded0c.mp4?token=tK7dtQ_vREnGpha30DCnHwAkFVLIbHBuqCofcSp4PsnLk52TxHYyf_4KbgPlyCmfpFMS8LkgHX-pmhZtdNhJStP7wgnRIrK215Cxw2aA1og8uliQnyvE4tzXKBgJOGnP19Fvnvm0SnZMN56LvndyW_qfnQi0EQNj0h5PLBlxlOE4VmjWvTDFAstnKo4FFU4-rbR_LxEFz7K6ZRc1HGDY3CX6tBRnBCy2Z6Ecyyhl6jAJur8VsCEXWh7EKJkyTjpEz1BOblhL1tY2n9RHIrKm6hlkLyCkKqbUxHA0QTksLUCUOJlcTreHOiAEA8jPbke4wX9AZbiqiRNIynpQBRfkRYVwZrZ0cuZq9xrMxzmUU5ZbVDd1PDVSDFiof4YrUADGqDOTVrMVAQ07lRZDkWRroZ79Drk8MiP2y1qszMamCUqRoIOzji84bAMZj3Tl7exCwU0sEDRPa5Z5RDdyK4LQODkwBoFczqxamw1gNJLWDDIdmjU8-AsvY6hokQmB2saMWy2hLnggBcQQRQv750pqKHhNeMD8b2QHHk9D5O3T_7LwCDBFqpC_YVQt70LgpR-Ed0024YsdV8ol4o2JoqhcOKC9uBLiuYE1G3ZVzdjtL97EqDHYlHlfFROsPwocB04E8TrXI7STZdprjtuct5wsrN3T4heU2xIAh3lM64WWMvs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f112eded0c.mp4?token=tK7dtQ_vREnGpha30DCnHwAkFVLIbHBuqCofcSp4PsnLk52TxHYyf_4KbgPlyCmfpFMS8LkgHX-pmhZtdNhJStP7wgnRIrK215Cxw2aA1og8uliQnyvE4tzXKBgJOGnP19Fvnvm0SnZMN56LvndyW_qfnQi0EQNj0h5PLBlxlOE4VmjWvTDFAstnKo4FFU4-rbR_LxEFz7K6ZRc1HGDY3CX6tBRnBCy2Z6Ecyyhl6jAJur8VsCEXWh7EKJkyTjpEz1BOblhL1tY2n9RHIrKm6hlkLyCkKqbUxHA0QTksLUCUOJlcTreHOiAEA8jPbke4wX9AZbiqiRNIynpQBRfkRYVwZrZ0cuZq9xrMxzmUU5ZbVDd1PDVSDFiof4YrUADGqDOTVrMVAQ07lRZDkWRroZ79Drk8MiP2y1qszMamCUqRoIOzji84bAMZj3Tl7exCwU0sEDRPa5Z5RDdyK4LQODkwBoFczqxamw1gNJLWDDIdmjU8-AsvY6hokQmB2saMWy2hLnggBcQQRQv750pqKHhNeMD8b2QHHk9D5O3T_7LwCDBFqpC_YVQt70LgpR-Ed0024YsdV8ol4o2JoqhcOKC9uBLiuYE1G3ZVzdjtL97EqDHYlHlfFROsPwocB04E8TrXI7STZdprjtuct5wsrN3T4heU2xIAh3lM64WWMvs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اعتراض خانواده‌ها و بیماران مبتلا به سیستیک فیبروزیس(بیماری ژنتیکی
⬅️
Cf) در ایران به کمبود داروهای ضروری(حیاتی) مانند کرئون و پولموزایم و نبود تریکافتا در ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/141957" target="_blank">📅 00:51 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141956">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
۲۴ساعت تا پایان آتش بس
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/141956" target="_blank">📅 00:47 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141955">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AJzEtU7lXRGlx6rKe6meKVdlvCXjbNNIZAORPIQxuZiKdwvCYVAjtuOiY8KoEHa8LyeOwHzVu5ekdyeyy-YmwyAWJoBv0mnbnLBQotFXVLoYIncxeWBcWKg4Hggf01sxa6DzYLzK5b5x5g6iiyFTIRHa_rg-jVtiY-VxypZOcY8WfKZykCK-kSIblvwjND4H1mPW003cusoJJqgnGk0nu7auJ8UqKaVcB79weOrsR6FNjGp78kKSb_60KFRUJXOvPCfzN053vvqJBvwBSiHuI6JbLqWENxpoUdYfXZe90_z-ciEOMlgFMCENXTiTfD2Bg3Py5eDeLYNO7-j_X4H4fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا سپاه امروز یه کلیپ منتشر کرده که آره ما پدافند داریم، 20 دقیقه بعد لوکیشنی که پدافند بود لو رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/141955" target="_blank">📅 00:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141954">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🎙
‏روایت خداداد عزیزی از روزهای سخت زندگی‌اش  ‏ساندویچ نان و رب خالی می‌خوردم.. به‌همراه پدرم دم حرم دستفروشی و گچکاری کردم..  ‏برنج و مرغ تنها یک بار در سال و دم عید می‌خوردیم!  ‏چلوکباب نخورده بودم و نمی‌دانستم چیه  @AloSport</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/141954" target="_blank">📅 00:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141953">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOPS-MmWO38ZgdRKYwWd_tdI9IerGmhSktgAxA0PNHS-QcYS_t2BbipNQOKtXgeTW0RTp3GMM_bxKh5KKa9Sl4giPnzHoSiwQqXF-LF1jbjOx6FTtZfoh9nMkOH511I1gQ7ue7jQFaXL2jq495ZIH1RVD6DUg0-SYOxwNvul1SNY_AGN__liO7Gb9cFklW3WhAXgHlx506dhKOb4K1f1GiTYt3el3NiwQFZGnypmQjZUiJEeA9zJ_ZfX30jHB7LHI52LqRO5zLzLbaWPsdgsdbl24iBOo3caKBa6g_MRSLEWHPWK_caxfaRrDw3EmumcWip22xuDSVcPnB8DT8qiNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
پست جدید ترامپ:
سوار بر اسب با جرج واشینگتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/141953" target="_blank">📅 00:38 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141952">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9111f575b2.mp4?token=BcPqFvVw6kAULOhfCuue-DAY4y9gjhij3GLupySDedqUQLcg4hEXtwnDfxY8xZnwsn03awnktaZic0EFs6y_QJ50JPhRpq3Zjt1aHgAZt3chz_wasJuNRJxhnPGfmcN0_dWiDsLSt6LzmIeT3tU7nMxbinrdvDvrxyRQKOWH78UQZkUW8axZJKbmMmRWaYJZ9jU_OZI5SkRaBdYRG8I4XOKGsA5JBpwV4khCLeTHb4GO_a1U13fAFZQa3xBRIQK2rRo-pbulV8MVxII8d9Tk4aqSJt6FqhpsLw7Kik8pw5aa0Rr6VsT9pnM8G5aDXSXqnGGqYmm7xRfMOkLLfOAPVH0eBGFIywIryoR6fRkxVdMlhSTv5RfXOk9nylDIAKiJVhydeb3W7X8HsvHfcXNth2Os0UPTGVsgJtF4Q7X2T0vCr79ZOBbpSk84VHRF7UNrRVs9m5K5-EdO-F9PunizRsimu5xSYKSChsxVGggO08fYAzwXiUbLoMnYan2WnVlPIQJSb_0mw1QrIhSVs7S0icTs0P4Mh_SSYUO-SClpvBctNdggoocG3W2Qx8Qth3TrR15r2kF3e6H15kNC8MZXskr5jHDOHdwX0SWnKXVCplUyzcFXsFPBx2cmm8LGgCF84BRTGVKyRGFah24Z04WWl-Bv1jNldvuSvh3hslXo3sM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9111f575b2.mp4?token=BcPqFvVw6kAULOhfCuue-DAY4y9gjhij3GLupySDedqUQLcg4hEXtwnDfxY8xZnwsn03awnktaZic0EFs6y_QJ50JPhRpq3Zjt1aHgAZt3chz_wasJuNRJxhnPGfmcN0_dWiDsLSt6LzmIeT3tU7nMxbinrdvDvrxyRQKOWH78UQZkUW8axZJKbmMmRWaYJZ9jU_OZI5SkRaBdYRG8I4XOKGsA5JBpwV4khCLeTHb4GO_a1U13fAFZQa3xBRIQK2rRo-pbulV8MVxII8d9Tk4aqSJt6FqhpsLw7Kik8pw5aa0Rr6VsT9pnM8G5aDXSXqnGGqYmm7xRfMOkLLfOAPVH0eBGFIywIryoR6fRkxVdMlhSTv5RfXOk9nylDIAKiJVhydeb3W7X8HsvHfcXNth2Os0UPTGVsgJtF4Q7X2T0vCr79ZOBbpSk84VHRF7UNrRVs9m5K5-EdO-F9PunizRsimu5xSYKSChsxVGggO08fYAzwXiUbLoMnYan2WnVlPIQJSb_0mw1QrIhSVs7S0icTs0P4Mh_SSYUO-SClpvBctNdggoocG3W2Qx8Qth3TrR15r2kF3e6H15kNC8MZXskr5jHDOHdwX0SWnKXVCplUyzcFXsFPBx2cmm8LGgCF84BRTGVKyRGFah24Z04WWl-Bv1jNldvuSvh3hslXo3sM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
‏
روایت خداداد عزیزی از روزهای سخت زندگی‌اش
‏ساندویچ نان و رب خالی می‌خوردم.. به‌همراه پدرم دم حرم دستفروشی و گچکاری کردم..
‏برنج و مرغ تنها یک بار در سال و دم عید می‌خوردیم!
‏چلوکباب نخورده بودم و نمی‌دانستم چیه
@AloSport</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/141952" target="_blank">📅 00:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141951">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/refjf16OHST8l77FfbdiS_7erI-JBX6IzF9Pr5-hRbhobV-v4rDOfuR1-lKgBSgns7IQRb592foSFnAMxIUUaojNiIyXbia0lwQSdeUYaJ8bvycR-LCG3_w5DopR36ZwuMREIAti92_l4dBo-qo42lyYwBfpQ6JKgFGm5A9trcHiNLuhm74OEISXNLBliDvJ1griYaanjBx6ySagt2xWowRAvmakAPgJmUVpK1ycUiJpJ_kSlFgTMr5oBr0L26Ys-r4WcjOltDFJQFFmEJFiM6pRchf3TB7-ypsreNuzGyLO7EV0pXEZfUugdzYLnp67DTaZwgW1XUzO-SAAq7oqkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علم الهدی: بعد شهادت آقا دیگه نباید برنامه شادی رو اجرا کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/141951" target="_blank">📅 00:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141950">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f3644e74c.mp4?token=Cp8aKecpCp0YxekNdwb-Mxgev4uLbLu2qH1Ucv1x1uENVUso23_xZn29xbq-LkCMxPy-HDFdMezyj9K6KO-46Ueh1guiJ6J_Kl4XjCCAdz74GsD5oZ251iR4o40oUxKohz4HFbO5h_BixhGCv6PhoK6mXjw1cselOEX5LVOv2xtpC7m6K3OFG1900XPUx0IP9AQHu0sz3zlMC5HzElSIQjFW5iAKLOMKBj4v2OqHa6qxiURzq7jnPip7NUXXDaV4XHdlLgSE3SPJUv47nPc3AJmmefDJXI73RBt7RAmtowv-YFopc2uQWNDCXIB74z4LI31x7AYkhfz3PxTQ1AvRow" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f3644e74c.mp4?token=Cp8aKecpCp0YxekNdwb-Mxgev4uLbLu2qH1Ucv1x1uENVUso23_xZn29xbq-LkCMxPy-HDFdMezyj9K6KO-46Ueh1guiJ6J_Kl4XjCCAdz74GsD5oZ251iR4o40oUxKohz4HFbO5h_BixhGCv6PhoK6mXjw1cselOEX5LVOv2xtpC7m6K3OFG1900XPUx0IP9AQHu0sz3zlMC5HzElSIQjFW5iAKLOMKBj4v2OqHa6qxiURzq7jnPip7NUXXDaV4XHdlLgSE3SPJUv47nPc3AJmmefDJXI73RBt7RAmtowv-YFopc2uQWNDCXIB74z4LI31x7AYkhfz3PxTQ1AvRow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در پی اعتراضات به شرایط اعزام ناوهای هواپیمابر آمریکا شبکه CBS با جفرسون کلی که پسرش جکسون ۲۰ساله برای اولین مأموریت دریایی‌اش به ناو آبراهام لینکلن رفته است، مصاحبه‌ای داشته است. او در این مصاحبه اظهار داشته که «آن‌ها نباید این‌قدر طولانی در مأموریت باشند.»
🔴
او حتی نامه‌ای به سناتور برنی مورنو سناتور ایالتش نوشته و پیشنهاد داده که خودش به جای پسرش برود تا جکسون به خانه برگردد.  او تأکید کرده که این درخواست کاملاً از طرف خودش است و پسرش چیزی از او نخواسته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/141950" target="_blank">📅 00:29 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141949">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
تو بی صاحاب ترین کشور دنیا زندگی میکنیم.
🔴
مملکتی که سرتاپاش رو فساد گرفته و فاسدترین افراد کسایی هستن که خودشون رو مذهبی تر نشون میدن.
🤔
روزی که در به در دنبال ریش تراش بگردین تو بازار سیاه خیلی نزدیکه
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/141949" target="_blank">📅 00:24 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141946">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sy4eTpYYeFVahilK2JNljss5kGmsSF8660ZbrFRBMset13q6JKKU3oFeVvsDVRuTSPtzGUCnkf10-xDMLZnrMwG2YgWyMZV9y6KWH41k455B1J0CnutGb3yE-p2vAaBbmUrl8KIrZMAeRFLYceOHiedrwEGV3kfJlkSOgDrRujjf3hefipQ2tXfBbiCqt5Bouw8zastscIQM4So9CEdLR7zWzpfTiB20Bml7P9w_QiFSrQjM5DehtoNAdY0yJfPZD-xaKG-P54Am56RKW3MMGRNN92cCrBPJuCNBNJysQ-YL7v0SL7CtmsJP5Z03vWHulCkXJjAYXFTE5kyaOtNUwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/275828a58a.mp4?token=oXERktFq9R-mlAYvdVPH6clGR3azVcXp2RfZIW-aR_qHze2aDgzaJH2BVBcL8iya3416Z9WKBBBLLlvbJvcrQK2DS3Alvu-cK4CzTyOfsdTJersfKlgDzKsciyOyx5WNR14RWcYYAEAa7bkFNi4zbR1kC6n2cW3ukgiGcMa0WrqGvUzZI2YLBobrmq7Ueyr5jO8zMLeTWC5f3cfB8U_dRjIzoHcMLmZNSJW4nfqJDkTIZK2F39Fu8YTy0DDf8ruNDdI6BNFgxdcEbR33GmEKI21c2K6ADlKN-vjCY7uNzIoSz93a2FWWWk09Y2fyX8lvAC8SXKXloUY7urWwLqWMFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/275828a58a.mp4?token=oXERktFq9R-mlAYvdVPH6clGR3azVcXp2RfZIW-aR_qHze2aDgzaJH2BVBcL8iya3416Z9WKBBBLLlvbJvcrQK2DS3Alvu-cK4CzTyOfsdTJersfKlgDzKsciyOyx5WNR14RWcYYAEAa7bkFNi4zbR1kC6n2cW3ukgiGcMa0WrqGvUzZI2YLBobrmq7Ueyr5jO8zMLeTWC5f3cfB8U_dRjIzoHcMLmZNSJW4nfqJDkTIZK2F39Fu8YTy0DDf8ruNDdI6BNFgxdcEbR33GmEKI21c2K6ADlKN-vjCY7uNzIoSz93a2FWWWk09Y2fyX8lvAC8SXKXloUY7urWwLqWMFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
امیر علی‌اکبری، فایتر سنگین‌وزن ایران، امشب تو مسابقات ACA 206 واسه کسب کمربند قهرمانی سنگین‌وزن این سازمان، به مصاف علیخان واخائفِ روس، قهرمان فعلی این وزن، رفت؛
علی‌اکبری که تو چند روز اخیر حسابی واسه حریف کُری خونده بود، تو همون راند اول ناک اوت شد!
در ادامه گفت :
بعضی وقت‌ها میگن روز، روز تو نیست؛ شب، شب تو نیست، من خیلی واسه این فایت آماده بودم اما نشد، شرمنده مردم شدم
@AloSport</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/141946" target="_blank">📅 00:17 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141945">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMsroLVfJzugVCCT_Qsj8Qc_iL94Cg8Jw3dNGj5piFwSdh03gUjkX4V2KkPosoECjcENSKt3GeFKdxl5BvKh0RJkg1ftXQVu58lMnEUgMnRVVm1k4C4Q50AGi-38FJ0tr_KXSGQE39vshbI7fmc9EdsHrXEATwpThAS0z8VPQpBID4YGLRxZ3KWQCA_L8XgObex-jv3_hMok6fZ1vsFI0SPMnumDSdqQQ8UtmG0WOrQbrFf1U5_K95IPv_8YO98SSxUrAvR37MnX0B62qs2l4AhRm6_vpnq5R0tDVHpjLSgEbn2qt-rGd111xqr6QRiDL0q4JJorPHfaX3hWduqYXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ: پیروز خواهیم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/141945" target="_blank">📅 00:09 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141944">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
حالا عکسایی که این خانم به رامین فرستاده هم منتشر شده که منشوریه و گذاشتیم تو بات تا ببینید
😐
👇
⚠️
مشاهده عکس‌ها
⚠️</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/141944" target="_blank">📅 00:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141941">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UfU2tOYEggB2ZBucehMBloE0MBnOqNgajYYyC8qze-nzSlIbTwij4cvqsZcjMpcQCPTlhXWkeDxHFwd36GwgWE9Yx8IiJIVcmdNdXij78nQtDZKhckx3zIO4mMnXtwvm7FtfKuU9ecVJ6seKybXgjxMgyvD1u12lbqlNydZEHWTDPaM97N4VeZls2ck3fXE3uEYRead8IW2LP6c_57uG4ra7xcJQcwtjLiCMKzrPsWtG7R32btckvd1klUogQopYHGWWFWih_udLhN7Km52YC99z2r1RltXVsFV-V7W6OHls3iDc-hij7FZFnoB3Xxj_Di0k5CkykKb0X2xTfyD0-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/e0mrNBBTHUUCDkVbV5uY37sfc6C7xcT-5n6BkIcxkWlY98t9CyVVbFtrXLSLJnLxRboXz8mfzt3X6vN_C5aKdRTePwwfyoEoXbKhediN6WU5sEbxTLPXLheAoxo7JvJGi7H6FzQw2XC8PWLEg9UYMMZI4_FDioLSKP8r9atKqBsTUqo3YYZrdllSEWcK0EPSLrdL9KP4ELXV0qxUM9lUY2myVoM_KNvJtojzCrwDenTBTSETF0GAJ-zl7ZCxCZ6I5VF4FJr8qt01QuuMVbtXJz6pD9XciS3zTicbDgO1NDxxDkEr5-TwYUUUQpFBwh5hO2VovFCgnbgTWV6NujANJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
رامین رضاییان رفته دایرکت یه خانم دو رگه ایرانی-امریکایی که به اسم «جول فرشاد» که بازیگر سریال ایفوریا هم هست و ازش درخواست نود و عکسای سکسی کرده!
خوده جول این موضوع رو تایید کرده و گفته همزمان با اینکه تو جام جهانی بخاطر حذف شدن اشک میریخت، از من نود میخواست و این خانمم فرستاده
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/141941" target="_blank">📅 23:53 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141940">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
استانداری خوزستان: درپی افزایش دما و ضرورت مدیریت و پایداری شبکه برق، فعالیت ادارات استان روز دوشنبه ۲۶ مرداد ۱۴۰۵ به‌صورت دورکاری خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/141940" target="_blank">📅 23:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141939">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/8921c86a41.mp4?token=TN76rwZN98ukOjJO2C33IYQxV4njgffetcDrke4hQHPpkVblRSbHgwhVHWIZPNCihdV-aj3GiIp_22Sk2-NsBaaEoJOSnH1YToMRIBtyho4xdUCFFLaUFKzcCI2z0dTC_fg0_Uc-BWuN6yprPUeiCJ3k7bpveIdEJg0BcVOtADRh5ohBOhjmMyZflHrmmnk4XjhA5-ZMapu7xHdR0RTh-S49z0SdxLyW-ANk_bqSnM5Gw1sfl3uGLsLc_Ejs-33x2DnTPs1PfBRQxLnJ3OF4r8yDkBf15r59yi_V_pR97zP5dfxXitJNmjvK1miP_r6-nLZxwA7ABxQkfVlLzBsX82SCPIO4MveZF8iTDiw7wD81XiwzlrKL7CBH3Q2iRoABXmNYDrYe8a81opwhpSXsTzKHAlPp8Tn7hK5Jd5WCRQiJbCGG_eZRX2cdA0etLK7EgNKzHJUsKNOOwLygDB5dS8ELrxLFj3VFYj0sRT_1m9m2A42DtbFapiPW8yF49TN2xjX3EVdA8efaqrKRsViWMDdmVd1yF_mr8zOrJgiDgtHjq8it69YDg8OIi8MJcqu07LFR8JNiT6eFTdcG1P1jezP1tVHIZvztOj6aU4Xfkr9DF_L0bNxid7kLqTFp_USvx0ic7Or16ih9yJkuTQzAXlTvvxuzKMxbcHqdhURhXcs" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/8921c86a41.mp4?token=TN76rwZN98ukOjJO2C33IYQxV4njgffetcDrke4hQHPpkVblRSbHgwhVHWIZPNCihdV-aj3GiIp_22Sk2-NsBaaEoJOSnH1YToMRIBtyho4xdUCFFLaUFKzcCI2z0dTC_fg0_Uc-BWuN6yprPUeiCJ3k7bpveIdEJg0BcVOtADRh5ohBOhjmMyZflHrmmnk4XjhA5-ZMapu7xHdR0RTh-S49z0SdxLyW-ANk_bqSnM5Gw1sfl3uGLsLc_Ejs-33x2DnTPs1PfBRQxLnJ3OF4r8yDkBf15r59yi_V_pR97zP5dfxXitJNmjvK1miP_r6-nLZxwA7ABxQkfVlLzBsX82SCPIO4MveZF8iTDiw7wD81XiwzlrKL7CBH3Q2iRoABXmNYDrYe8a81opwhpSXsTzKHAlPp8Tn7hK5Jd5WCRQiJbCGG_eZRX2cdA0etLK7EgNKzHJUsKNOOwLygDB5dS8ELrxLFj3VFYj0sRT_1m9m2A42DtbFapiPW8yF49TN2xjX3EVdA8efaqrKRsViWMDdmVd1yF_mr8zOrJgiDgtHjq8it69YDg8OIi8MJcqu07LFR8JNiT6eFTdcG1P1jezP1tVHIZvztOj6aU4Xfkr9DF_L0bNxid7kLqTFp_USvx0ic7Or16ih9yJkuTQzAXlTvvxuzKMxbcHqdhURhXcs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رژه نیروهای طالبان با تجهیزات و خودروهای نظامی آمریکایی در خیابان های کابل، در سالروز خروج آمریکا از افغانستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/141939" target="_blank">📅 23:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141938">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/pgIIRpRTQ7_rJbA3Nbr75xuvtUfS9AY9bhQUOWOLHrvzgIKqlG5BJPjMUfY1yk6HP_KN8v1zXmvoy7Ue6vJoOkypTonZMe29pvy2pb1B04Iy1pU7hn33dlgYm_QlieKAgU0Y3saZF1sH_W97q-5mLgjrRwL7bpBE76JI-67BINrHee1NIQmheJq8tkVfmxatxcGaaWjqkc1rb-VAU0dX-zj1AQEIyTVIXgPXtR9nRPsdoMYtFGmygmvtT-MsrP836wA3ZcrnXbksAsMQfzFtptJne_uJazVA7dnx0W3jZ4TvS03Pz_WBL_D8Lp189bcEHL5PglW7AWH1aKjRRdbAAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرمانده ستاد ارتش اسرائیل: آماده بازگشت فوری به جنگ تمام‌ عیار هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/141938" target="_blank">📅 23:37 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141937">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4yAXefOdcT6W10NbCEFirL1c7s2ExXfwme3ASeFDXdq3Kmzc-xFLLXo7ZmW8ETp0whAkkpzoec7IhGqS4zmT22wsgKvKz2lyibVcXbfkYonBo9EoJc4bf1hpmHw0W95CQDTHurYKvp82RmhmAQaQxzxRnHdkLogHMj7aRKNqxUqNwo-wCsRmoWfGFT3H0Q_xlCN_rLjcTGcjMZU5VMlJnnLr8KTGqhwbLKoXEGPFiPgii5ixY7cJVMiKLhzsJ1-Qk4B-DNB4ZenpElBKd2-aoFEp3A__8bOxTEgX0dEl6yyHwAza7d67Ct3b5Tf3JKENIuPg_PaURKSZ4me_UQjpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همچنان جی دی ونس شانس اول برنده شدن در انتخابات ریاست جمهوری آمریکا در سال ۲۰۲۸ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/141937" target="_blank">📅 23:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141936">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1aa363cc6.mp4?token=sBGuQkjbB_JE9IPIOwIOFnjrCR9XfN7Jyh8nUKNdcpVbC34EXNpuqkLeOFLJBjprJYWY1CQCuv8O0k-V_LqiA95DLJo9U5YeVwrvPZDTKQjoUifzjfn2hqFLjoTtx3NoXtO694psfE4LR_b6D5SCf-7850zK_7K0Rzhw5ZwDG0EqYcMf6xCKzN8Y_68fZry5DzbQG2hT5bi1THHP-qJaedn4vqcPIy0c9Mpnojnf6lm5BlEz8r71iG1RW-JD1f4ZudffNVuTtjDX-WJlGZe3ZwpReau04LcAO3zwtVHgfgh8umOwpEyZlX_S2u82DoG5IIJXXCt6_GsufnQtCg5pWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1aa363cc6.mp4?token=sBGuQkjbB_JE9IPIOwIOFnjrCR9XfN7Jyh8nUKNdcpVbC34EXNpuqkLeOFLJBjprJYWY1CQCuv8O0k-V_LqiA95DLJo9U5YeVwrvPZDTKQjoUifzjfn2hqFLjoTtx3NoXtO694psfE4LR_b6D5SCf-7850zK_7K0Rzhw5ZwDG0EqYcMf6xCKzN8Y_68fZry5DzbQG2hT5bi1THHP-qJaedn4vqcPIy0c9Mpnojnf6lm5BlEz8r71iG1RW-JD1f4ZudffNVuTtjDX-WJlGZe3ZwpReau04LcAO3zwtVHgfgh8umOwpEyZlX_S2u82DoG5IIJXXCt6_GsufnQtCg5pWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سقاب اصفهانی
:
پولی که برای خرید اتوبوس داشتیم را در جیب قاچاقچیان سوخت ریختیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/141936" target="_blank">📅 23:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141935">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/580f35cabe.mp4?token=e5raVNd3gnMLClbXkpDeU0O6drhEWwNInCITtrH3cuty4n0ZKeJ8oS4QWgfXpTlVzOb_WzD-JTPvSGkLTgGYxOt79jl04A_uirZQOg7j98bvZ9gsjvgNyulF_QogZIxpyoEEvb1JoCYqjO_osjV7ZbLa-vDe6GIEvDKvCkTL0-WKhCAjofI6jhSCaY0KfZ6LN7J7Bv9C1xTfT9X4p01qw9Xi8Za7Tkd5GR4rg4VvLGqbMpPTJ8KMuNgwqunM1FVEF013bzHVUtGTG4-74DO5gguDJy2C8hzxRIt7FY4I75tS6sjs9YDYk07Nsy0ncF2ZyT7nrCR6V_lWRHW3c5KrxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/580f35cabe.mp4?token=e5raVNd3gnMLClbXkpDeU0O6drhEWwNInCITtrH3cuty4n0ZKeJ8oS4QWgfXpTlVzOb_WzD-JTPvSGkLTgGYxOt79jl04A_uirZQOg7j98bvZ9gsjvgNyulF_QogZIxpyoEEvb1JoCYqjO_osjV7ZbLa-vDe6GIEvDKvCkTL0-WKhCAjofI6jhSCaY0KfZ6LN7J7Bv9C1xTfT9X4p01qw9Xi8Za7Tkd5GR4rg4VvLGqbMpPTJ8KMuNgwqunM1FVEF013bzHVUtGTG4-74DO5gguDJy2C8hzxRIt7FY4I75tS6sjs9YDYk07Nsy0ncF2ZyT7nrCR6V_lWRHW3c5KrxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سقاب اصفهانی:
هیچ شگفتانه ای برای مردم در بنزین ایجاد نخواهیم کرد
🔴
در صورت انتخاب سناریو، چند هفته با مردم مشورت می کنیم و اصلاحاتی در صورت لزوم انجام خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/141935" target="_blank">📅 23:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141934">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
در پی حمله‌ای موشکی از سوی حوثی‌ها به نیروهای مورد حمایت عربستان سعودی در شهر مأرب، یمن، طی کمتر از یک ساعت، ۵ انفجار رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/alonews/141934" target="_blank">📅 23:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141933">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
سقاب اصفهانی: امکان ایجاد بازار صحیح برای فروش سهمیه افراد نیز می توان اجرا کرد/قیمت این بازار ها نباید توسط دولت یا رانت کنترل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/141933" target="_blank">📅 23:23 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141932">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da4e44162a.mp4?token=lSOWqaqaryxzhZ34KwXP-pdAItrN7QMKnQvQqYpqoUBf0ZyDKqb-bGmXfngNXRJCUNDLE9dK_KveIYRor4HslzMeSn7997WgU6GlPrjGJ9lnngozSqQkhVzEN731Ou-JSkPcocDdlzvPK1n5FrhDGjoFYt17Ci_8l-y9t4azQ44WS297y0_7LRgZCcoxjKF6SVfeSM2LAFa8SgTzp4AV2PvY0tzY3a3D1zeYxIoILn7kBY3hoKy6082aRAuSky3NxrsaHRRwc-UNJL2_VQxn8WG8WEkZvzoHrey52WhQwob7E0K3lbIrqW5p1yZdxsO2JxF3niiRZOubSzpEPBU-pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da4e44162a.mp4?token=lSOWqaqaryxzhZ34KwXP-pdAItrN7QMKnQvQqYpqoUBf0ZyDKqb-bGmXfngNXRJCUNDLE9dK_KveIYRor4HslzMeSn7997WgU6GlPrjGJ9lnngozSqQkhVzEN731Ou-JSkPcocDdlzvPK1n5FrhDGjoFYt17Ci_8l-y9t4azQ44WS297y0_7LRgZCcoxjKF6SVfeSM2LAFa8SgTzp4AV2PvY0tzY3a3D1zeYxIoILn7kBY3hoKy6082aRAuSky3NxrsaHRRwc-UNJL2_VQxn8WG8WEkZvzoHrey52WhQwob7E0K3lbIrqW5p1yZdxsO2JxF3niiRZOubSzpEPBU-pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هدف قرار گرفتن نیروگاه برق الزاویه در لیبی با یک پهپاد و قطع برق
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/141932" target="_blank">📅 23:22 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141931">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f7915012.mp4?token=jR34psS6IZ0rjEXnu9YpL4chKZq92cj7Th0ow6OMJs5uIxhrfyike2mnTFuN2ba1bLIpnE3AHhd5auE829ma7iFom58ICE-2PeMZWDwBJJqKsdyee3BZEoLQOH6tZKxAusXVZxFSy_LwBWCksrOUDsb0AAGdNwYoq1n9aGyVGXmPrfcgxfKxx8Px7-i08fygRyYROMDldl_GWQC0Hay87vXp9KR94LIfmQXVzvZXn2FDh8daClAtTOJ4dJ-Mv4nBpeCaO859Lxl6UU6mh1XtBiLskZaVwxTMbTp_odRJCa_zowlm6IdM7fj_Ah6NKRKirTYEu6PI0r9pPIOwi5rRhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f7915012.mp4?token=jR34psS6IZ0rjEXnu9YpL4chKZq92cj7Th0ow6OMJs5uIxhrfyike2mnTFuN2ba1bLIpnE3AHhd5auE829ma7iFom58ICE-2PeMZWDwBJJqKsdyee3BZEoLQOH6tZKxAusXVZxFSy_LwBWCksrOUDsb0AAGdNwYoq1n9aGyVGXmPrfcgxfKxx8Px7-i08fygRyYROMDldl_GWQC0Hay87vXp9KR94LIfmQXVzvZXn2FDh8daClAtTOJ4dJ-Mv4nBpeCaO859Lxl6UU6mh1XtBiLskZaVwxTMbTp_odRJCa_zowlm6IdM7fj_Ah6NKRKirTYEu6PI0r9pPIOwi5rRhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سقاب اصفهانی: امکان ایجاد بازار صحیح برای فروش سهمیه افراد نیز می توان اجرا کرد/قیمت این بازار ها نباید توسط دولت یا رانت کنترل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/141931" target="_blank">📅 23:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141930">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
رئیس سازمان بهینه‌سازی و مدیریت راهبردی انرژی در گفتگو ویژه خبری: حدودا به هر عضو خانوار ماهی 30 لیتر تعلق می‌گیرد حتی اگر صاحب خودرو نباشد.
🔴
قابلیت انتقال آن به هر فردی که بخواهید وجود دارد. دولت مدیریت سهمیه را به افراد می سپارد.
🔴
قیمت دوم و سوم در این…</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/141930" target="_blank">📅 23:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141929">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f05284b9d0.mp4?token=R3oYp6INMw0REIM_dFkVXiv-s4zVhiNO_iwHLuVMU5Tmk4SsTCtcMwBe643UBU2oDBUIA5TWmPrUA7ZjwKYpPSZ4-b4O4TFPvtaw9ecRDDkggGJMkq93gXo7coKPRYiWfSdvRb4ESswM5lkoq9N4_S9BKzssbbZ_3HM7pW9OMCnbAnmrUxng9fwLuD69nL0kinML_daEoc5Bs468wZzOMrydyYXIq41rSJHIUP0N9wmhZrUocnzQk_UnmwcrY9GwwmF6YooVm4gl960hcyDG0SlKc4mMdkzKKKjgx6nA-GwE6wwJY0hMgOR1tP_TFme84ZuWdnolpfz95kgEjBF8SR3aepEzFsbsy-8ncdq2tc41kane23Tsx5XYYNIC6hlDjrPg-RWIablIWZUuMVs9AVUTVSWV0POAeLQxHJYm2iek1lmLTWORfUW6sEFA6950fLhr4ZfIvhEUzMJZ0pBZ4WzdMV4yiV1lTx4SW1IlZEIhggS5yIll4HycEQ6FucygmOUAK_lutr-mtRkgfamDVd-6PZVsp2fZf76zQiT8s-Nhisr0dUiB3HzQ1sWKQ0XCVihAGBS9MVtB5HZFLJ95EQqTeIq8BI9SHzW7pObXkiRB8uMUyz9FyuKbTRxbY7qJCpPR-wkPWPGza0rDwaPkhv16t0ov-vcvpADfTKbLP-8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f05284b9d0.mp4?token=R3oYp6INMw0REIM_dFkVXiv-s4zVhiNO_iwHLuVMU5Tmk4SsTCtcMwBe643UBU2oDBUIA5TWmPrUA7ZjwKYpPSZ4-b4O4TFPvtaw9ecRDDkggGJMkq93gXo7coKPRYiWfSdvRb4ESswM5lkoq9N4_S9BKzssbbZ_3HM7pW9OMCnbAnmrUxng9fwLuD69nL0kinML_daEoc5Bs468wZzOMrydyYXIq41rSJHIUP0N9wmhZrUocnzQk_UnmwcrY9GwwmF6YooVm4gl960hcyDG0SlKc4mMdkzKKKjgx6nA-GwE6wwJY0hMgOR1tP_TFme84ZuWdnolpfz95kgEjBF8SR3aepEzFsbsy-8ncdq2tc41kane23Tsx5XYYNIC6hlDjrPg-RWIablIWZUuMVs9AVUTVSWV0POAeLQxHJYm2iek1lmLTWORfUW6sEFA6950fLhr4ZfIvhEUzMJZ0pBZ4WzdMV4yiV1lTx4SW1IlZEIhggS5yIll4HycEQ6FucygmOUAK_lutr-mtRkgfamDVd-6PZVsp2fZf76zQiT8s-Nhisr0dUiB3HzQ1sWKQ0XCVihAGBS9MVtB5HZFLJ95EQqTeIq8BI9SHzW7pObXkiRB8uMUyz9FyuKbTRxbY7qJCpPR-wkPWPGza0rDwaPkhv16t0ov-vcvpADfTKbLP-8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس سازمان بهینه‌سازی و مدیریت راهبردی انرژی در گفتگو ویژه خبری: حدودا به هر عضو خانوار ماهی 30 لیتر تعلق می‌گیرد حتی اگر صاحب خودرو نباشد.
🔴
قابلیت انتقال آن به هر فردی که بخواهید وجود دارد. دولت مدیریت سهمیه را به افراد می سپارد.
🔴
قیمت دوم و سوم در این طرح وجود ندارد و سهمیه در کارت بانکی افراد شارژ می شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/141929" target="_blank">📅 23:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141928">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c66d62c3d.mp4?token=O1OOfEkcSxLjdZKpfxOjlWXZi4ywY8SCkPrs6ZDbOjb3KHnJ_iiqO4nNLpVfxVs8kFAq2MdS4Bh3B6crkTgWOm28BMZuOG5AoQkiDNlibQcrLEgrtsqITGEdThisUHMnhpzDTLyG6mz-ERm2z7m-siJTxYomLlviDxD6aoLAFrZ8Z8DvkCUODHSdkaqMrqhcWrtHkqUc472io2WLz6O1KIL2A3KhFArxVLrRV0IcmLhBKEBa_B_0hPfs-LICzc-10lE9ecjVVQ6ubHmBN4JbYrGuI7LeChQfeqnqd74rlvs8UAkEX2B2vqaNMd_lTy04JsatszQ1pdc8r9EIF3X3oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c66d62c3d.mp4?token=O1OOfEkcSxLjdZKpfxOjlWXZi4ywY8SCkPrs6ZDbOjb3KHnJ_iiqO4nNLpVfxVs8kFAq2MdS4Bh3B6crkTgWOm28BMZuOG5AoQkiDNlibQcrLEgrtsqITGEdThisUHMnhpzDTLyG6mz-ERm2z7m-siJTxYomLlviDxD6aoLAFrZ8Z8DvkCUODHSdkaqMrqhcWrtHkqUc472io2WLz6O1KIL2A3KhFArxVLrRV0IcmLhBKEBa_B_0hPfs-LICzc-10lE9ecjVVQ6ubHmBN4JbYrGuI7LeChQfeqnqd74rlvs8UAkEX2B2vqaNMd_lTy04JsatszQ1pdc8r9EIF3X3oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی از شلیک اخیر موشک‌های "فلامینگو" اوکراین، به سمت روسیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/141928" target="_blank">📅 23:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141927">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
سقاب اصفهانی: بنزین در ایران لنگر اسمی تورم است/ مردم بلافاصله بعد از افزایش قیمت بنزین انتظار گرانی همه چیز را دارند
🔴
پ.ن : همیشه بعد گرونی بنزین همه چی گرونتر شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/141927" target="_blank">📅 23:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141926">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LS5If3yrfbs8UD07X1Y6D59YBDkx78nri3vmlPk2LLVygfMNuQifGASQA1XBSaqhWCtE5b6TwjaTk6LWJbz2EvEB3GP9SeWUDG6iuaUy8k37WznB_BFYKoaCaKwZZvJ6N5oWRoCFX6SAzEDHScm45iUA66drDsd9mYzo74KjJ1mGsTvcKq6Gi0aj0JUvP5hX7OgCc3_OEGSSSy8hSGZMikcne-xauZp5EBj8gdQFGAq1DZrWEcJnmhnf0HViiayWNp-edri62hVlyTn4MfbUyzMYfkMVaTDsgNM0us6Ue04FodMEs_JOPvPBaYxinkgi_yU7ZrSvl5-uE3b5_bTLjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت اقتصادی ترین مدل گوشی سامسونگ از ۵۰ میلیون تومن عبور کرد.
یعنی شما اگه ۵۰ میلیون تومن نداشته باشی؛ یه گوشی خیلی متوسط هم نمیتونی بخری.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/alonews/141926" target="_blank">📅 23:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141925">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jp8KV0EgiP74DwqOPUGRtEJkSbUMJST1yc7foH8LX1Jq2VQdDEbtV488p30Ff5Y5GQK8Lf7vK_qANpFbUrAmUEi7Sw6lZrBYU3F1xc4mtULJiUcko470VLctP1F1dtpp56E_5M5OBBNBL14-18SzUDg_-1to7sJf7WPKLg4YWra-9zY3h-8GaLTWqpoF8naEBUIH-gd31vS2R5l1p9sXsAUfkNfufmdJGWNO8xRkV_zV5tsfBtXgXDonRyxo6U_d4GTegPJbaGNKpNfMy1QjVsC5tHLbxPqkARzrxvca5e3BTleBJkOeYtcNwpu3st3gJ_PiZb4KCit3P7s4yDAR9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاهش سلامت روان در میان اعضای خدمه ایالات متحده فراتر از ناوچه آبراهام لینکلن به سایر کشتی‌های مستقر در منطقه برای حمایت از عملیات علیه ایران، از جمله ناوچه باکسر گزارش می‌شود.
یک مادر گفت پسرش از ماه مارس در ناوچه باکسر بوده و اگرچه شرایط «به بدی ناوچه لینکلن نیست»، اما این کشتی چندین ماه بدون توقف در بندر سپری کرده و سلامت روان به یک نگرانی جدی تبدیل شده است.
او گفت این کشتی پیر در ابتدا برای یک استقرار متفاوت برنامه‌ریزی شده بود اما به دلیل کمبودها به خاورمیانه تغییر مسیر داده شد، با وجود اینکه انتظار می‌رفت پس از استقرار دیگر بازنشسته شود، و با چندین مشکل مواجه شده است.
اعضای خانواده همچنین می‌گویند ملوانان زن در ناوچه باکسر به دلیل تمدیدهای طولانی‌مدت استقرار، از دست دادن تماس‌های بندری و عدم تأمین مجدد، از محصولات بهداشتی زنانه بی‌برگ مانده‌اند. ملوانان از بستگان خواستند پدها و تامپون‌های اضافی بفرستند تا بتوانند آن‌ها را بین خدمه توزیع کنند، اما بسته‌های کمک‌رسانی هرگز تحویل داده نشدند.
منبع:
آرون
پارناس
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/141925" target="_blank">📅 23:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141924">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8252e0d0e6.mp4?token=SoR8ZbeNNfIVvTEqj2MuueFcmGlgMLINA-lNK8Y8GGRv1275skrYVRdGwyzQt-nQg351maNIVLL5zQDlxTmTXwBODMXaFVAxOBZgW8_v3yfPB6sxDscDFPrILH-O3lLd_CrZLyt4Z8_tp-BuTMJqRLXEMi0seB767VMD83TjaTcC_6whFFlMU7qfvd1ymTgRXykkpiQ0kk5shl1McYgiiQmNYIRG5yO5H9cZ8VLQYJQKFnURM92QBi-TnPf4amImViuC6weJgMX1Fcd5qcglUJkZ1wlUg_yoiqzNnGuLLCgSpw7MGMd1YxuIxkV4DkMv_V0IAzQ_nPRRz125VBYTWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8252e0d0e6.mp4?token=SoR8ZbeNNfIVvTEqj2MuueFcmGlgMLINA-lNK8Y8GGRv1275skrYVRdGwyzQt-nQg351maNIVLL5zQDlxTmTXwBODMXaFVAxOBZgW8_v3yfPB6sxDscDFPrILH-O3lLd_CrZLyt4Z8_tp-BuTMJqRLXEMi0seB767VMD83TjaTcC_6whFFlMU7qfvd1ymTgRXykkpiQ0kk5shl1McYgiiQmNYIRG5yO5H9cZ8VLQYJQKFnURM92QBi-TnPf4amImViuC6weJgMX1Fcd5qcglUJkZ1wlUg_yoiqzNnGuLLCgSpw7MGMd1YxuIxkV4DkMv_V0IAzQ_nPRRz125VBYTWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
احمد آریایی نژاد نماینده چفیه به گردن مجلس:
مهسا امینی به درک واصل شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141924" target="_blank">📅 22:58 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141923">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bpv-K7SRi2I8t8lK3oWUB2HYfcOjM9RGDt01rSgsod-fHWDcJIAu5bkWDWTb7e-E8X49OqZzM319kt8dNYCv1opGdjmmAE3sKx2-gYhU4yUsI7SRjKvUiT3asOnjZbQM8ZkoEzsmobuQYr9Dl3JFQwQ97EwVfLEmKjWtYKFLqx0QRrxqiRTLuzKYNGIdRopAz_uR8EN8trYjBj1Nvixj6NNM9m75dJI6h186iOKmnu2KY_ZbughpAUvDCAdnhFeQZyRNyKjR_bPNchydpE6uwFGO1eBICkh2vhRP8JcQL0IdHAyKW1_oFQYTmwN9Po4xAZgw7laQuhakPrQkhRIyZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایرانی‌ها درمیان ۱۰ کشور پرکار جهان
🔴
مقایسه آمارهای سال ۲۰۲۴ نشان می‌دهد ایرانی‌ها به طور متوسط هفته‌ای ۴۶.۳ ساعت کار می‌کنند؛ رقمی که ایران را در میان ۱۷۰ کشور جهان در رتبه دهم قرار داده و افسانه کم‌کاری ایرانی‌ها را رد می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/141923" target="_blank">📅 22:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141919">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TO6qct8arNK8fvxqKq25A86npfTRmYX7MbWMwgz0c7HxZTI4luR_rBZkmyT1XDPYMH5q9v7wBlvPN2HH1ZMJP4iI1c5w_Ri8Dc3KeM4XcHzWBkx0fxKGrlCUFAfDG0rPOj0M7f-0iCNfCm4c54ZgiSxnIgZ3xa-ZLRjYaLc-SlduVYmR-yu3n2InjwdpSsdQoAq5a39fXdZ6YJxz-HZ4MTiL-19CYlphK7YHExJ8VCmzcVMR01BdvlHwGYgeqnlwJOCOez4BETg_DedXF5LGW-QEXE2LOtxLGC-FduaYLLI8-elytWB4N4QUH9mhrRMcGmmndAqdl-Qg6THFB4GGlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RrlOA3CF3TaZvCIXM2Ta3nALc2LDSh3mqYHYoz7u6qsadewL81jyIZnafB20On_brhr-mh07aPyV0q_Ji7joa6OEE75VvVZkH1713hWFr1W8gzbwhRsxyLTv3kFPDs4Vp1u_7BR-b9iOYdhWpwEzV8nLdqGdY8urnulKL-Unj-jSwFxNPzvLIM4MUK5FcHcmsRBP825n0qdDZbsrldznR8jIWbvGm3JZnXTjkTx71fZ5UJ7vNg7bK1-D2EjhYAMKcvSMVrMXhOY9zD6pHuEVVOH5KxPMgNYj4U-57bPBgm1KSF5TvGE4PRcrS6baHTdNiCc7eS_eaguR7qGVZlRWkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NM8dey-KYXoo_jyqd2XxbzQLaD86zbnsrke22dqcrqovGM11wZVP0O2bmJmg_XZklAyRCHbs5Du_9ekrF4hGJVZgM3fKynGoKfofB1Ttb6PGECQMemeCmTzuWIy7_7jgWLfVLUvSBMKpt4ATw9LD1tcJB8i4LmLMO_yw0QU9JX8PW5msOH6uOXqJzXxAMFV9UPQS5INsB3izEuAE0zBTCeVqnF9omYpz00hjb59yjMxeX3AtGBILafTy-Y1naLIiWqPs252fz3XQ6EEoZWp4z28v3Uey1YF6kue4VEVDpclBM-P1-OuqkUvhrOiDpmuGhUdEO-9VYDjfcwU4xj_D8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cNBod1ZueQ9rmQtIR3inlGZi_OE-TS7vtJKvnm8UxDQb_OGl7xsQIGgCCTNXCewkWO5UED1aCxcoF-SCQcHynCx1HUxdD4ugVTc_gtangoAmKgtjhMk76CPVnDVOz4VdDzEULDXai6aB1yPqME6DzQkQOABNEilHrAvd2q3CjjleONbHv0PLqEhjJY8S1PiZenP55UMx6RaYkC1ql78rBi5I_2hh4HUE1vPdctYuI5wNVhL-y33VA2BpbiO_JUutSl68qzKS6fOjR6RwISitM97maUTY2d_lwCbx3Vd6293m1OZCSalOUWTuChWbB8mT--6usV1NuiBmaVEjGX9yIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوشی‌های جدید سامسونگ با قیمتای فضایی وارد ایران شدن؛
⬆️
گلکسی زد فولد ۸ اولترا (Galaxy Z Fold 8 Ultra) با حافظه 256 گیگابایت و رم 12 گیگابایت که جزو گرونترین‌ها به حساب میاد، حدود 437 میلیون تومنه.
⬇️
ارزون‌ترین سری هم، گلکسی زد فلیپ ۸ (Galaxy Z Flip 8) با رم 12 گیگ و حافظه 256 گیگ، از حدودا 300 میلیون تومن شروع میشه.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/141919" target="_blank">📅 22:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141918">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e21c271cbb.mp4?token=QjczxxvMLaXAiaKh-skkwBpkpJQbzQHIJQSH9bk5Q3mfJdWewEkUNNSwCZfuLtOiWUtXWIdxxanL3deylq610c0Zymo-Y2fWHtlQN9yB-_zqv2F8YhRSSYdMToY75q5iGuYhuTCntb5RKjMhk5bH8azKZVMuWu_BuKu5FfD5VoUSmWiv-MMQpB8vFRKWOzqV0uxuttMTHx5pKJiji-dQBWJl4Jqfgyzo6QfZFM7Sq1sWvsO4u1zJpwFrNzeajvRKSB-iWWVPuQk89oEO3cOIib-2iLz2apoJ1lidgqbZk9UscweaHT2XYrEgBGt-SBJxpVabiVKL_cM5RP7SPpQENISZmUa43PSL63wj8EMFL4RzeJvLMd-Poevf1Z-N9sJhFV1FNCD7JJpAGWJzVaFnsuvmaQIaRutV9mZ3n7Q8g4Yz6xAT5AZqr1L8Fd0Ch9JgfnRNLS3gl0GR5DaABZ551uAughYk18A8RwqJ16G3vqJ9RHBXbuL_KN14EO2Wp7alokZJSkqPFiOcnttA7tAInl9DxatEQFX97f8F9G2DgIbgfZmwjqG9m-NaY5Nu5DFA8J8Nlule8pUIn9Ir81mT72To-upBcny4pblPu1zioULQq0Qcs5Vh4TDS6C-szs4TYHC47zPHm1NBwt2gLgoTvG3Q1eKNLprMXXelGYmKHS8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e21c271cbb.mp4?token=QjczxxvMLaXAiaKh-skkwBpkpJQbzQHIJQSH9bk5Q3mfJdWewEkUNNSwCZfuLtOiWUtXWIdxxanL3deylq610c0Zymo-Y2fWHtlQN9yB-_zqv2F8YhRSSYdMToY75q5iGuYhuTCntb5RKjMhk5bH8azKZVMuWu_BuKu5FfD5VoUSmWiv-MMQpB8vFRKWOzqV0uxuttMTHx5pKJiji-dQBWJl4Jqfgyzo6QfZFM7Sq1sWvsO4u1zJpwFrNzeajvRKSB-iWWVPuQk89oEO3cOIib-2iLz2apoJ1lidgqbZk9UscweaHT2XYrEgBGt-SBJxpVabiVKL_cM5RP7SPpQENISZmUa43PSL63wj8EMFL4RzeJvLMd-Poevf1Z-N9sJhFV1FNCD7JJpAGWJzVaFnsuvmaQIaRutV9mZ3n7Q8g4Yz6xAT5AZqr1L8Fd0Ch9JgfnRNLS3gl0GR5DaABZ551uAughYk18A8RwqJ16G3vqJ9RHBXbuL_KN14EO2Wp7alokZJSkqPFiOcnttA7tAInl9DxatEQFX97f8F9G2DgIbgfZmwjqG9m-NaY5Nu5DFA8J8Nlule8pUIn9Ir81mT72To-upBcny4pblPu1zioULQq0Qcs5Vh4TDS6C-szs4TYHC47zPHm1NBwt2gLgoTvG3Q1eKNLprMXXelGYmKHS8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حرام زاده بودن رژیم جمهوری اسلامی و طرفدارهاش رو بصورت ساده توضیح میده
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/141918" target="_blank">📅 22:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141917">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ugSOr5DlKxo_wOV6O_ueffSDZTsa3ByERBdpIUX_s6dudYIGo3eHrceyZ2ADxe-VEUWIvZ-WOzhh65xu4VQM_eCCOp5dXUCxjtNkzEZElcTG8lMzZxQFVwUvOVFTyF0unOV2UBy2ecN3592-PkKG8zqjur_ohUk1OfwzypQ14D2wdK3O84Cl-X0gmh6fbhC7Z-BRp0lRktrLm-xOTL0Ig4xpnhdOpY2ygRSWPQje7WBDBP1Yyjpks1PPaGHHagiuvqfdXPCpXeSZueuS6e-6p1m_SmbqrXAFgxHkDT20gdFRKZxeHgYnLkh3-NN_l8ybsKx0VpKHlI6U831FO4PWzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مدام از مصرف بنزین و صرفه جویی میگن ولی کسی اشاره نمیکنه چند ماهه شبانه تو کل کشور هر شب ،کاروان های موتوری و ماشینی تو خیابون ها دارن بنزین دود میکنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/alonews/141917" target="_blank">📅 22:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141916">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4ZghKHLDR8hw2Myj6mis-E5K5Q4r83FTnjjkM_bdGGq0YQbDyE1JvEFnLPoS8B1jGhVvgd4QONQmymVNEb_ngldDh5lveDVl0-hahWZUOA2mjUClW6GYB7o5yG3YZ1ThOX9YoahijpC5jf3RCpZYmD6ToHkHXbFst2VyzpiMVfxqoPvBAe0PUZJruKvf0UOupN_0lthkaDDm71TyzN-HbX4owcB1cUF0G8d560dc29jqisN7hdX67pr1j4SvNknoHEkGiscqfAy5R4TCIsCgPUDVIIgIvuEUWJ0IJZAt88kjBaf0yo5gEprt-8GGa6-HAR3Mu_iaEdttiGXkmFtpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک ملوان در ناوچه یو اس اس آبراهام لینکلن تصویری از غذای سرو شده در ناو به یکی از اعضای خانواده خود فرستاد و گفت که وعده غذایی شامل «یک قاشق از همه چیز» موجود بوده است، نه آیتم‌هایی که به صورت شخصی انتخاب کرده‌اند.
ملوان گفت که به خدمه گفته شده غذا «با هم مخلوط شده» است و اضافه کرد که لوبیاها از بدترین چیزهایی بودند که تا به حال چشیده‌اند.
منبع:
آرون پارناس
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/alonews/141916" target="_blank">📅 22:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141915">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114b809380.mp4?token=NBdpQ5ocb3inIRMFIBYqjldaKiVSGyQZELuTorWE2ktSaLflz21cZVyd5265CWjE8h8St7A25Qw3KkX2jh8FKqoWG8TYd-788VjWP83RNzP8XoCzihhNEq4bTJ9COSY6KbU4CYSm9xQ17xTJPLkoWqOVKGQprYrJZepPVBl9IsAC2GE8_0AGQ_LXtCKx3E90cCamikmc_m4bWsihrEiOWKaOFD0iZ-L507PkNfseOwpTG8zXZzEK0onYuha5taOmp7GqZ67T5KnXTXD_R3p_-rff5wrKulq8gC3Gm20ObsTn9FIPtBxxkLFD152hjWgLfKDfvdZ944DvIjSMcaDk4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114b809380.mp4?token=NBdpQ5ocb3inIRMFIBYqjldaKiVSGyQZELuTorWE2ktSaLflz21cZVyd5265CWjE8h8St7A25Qw3KkX2jh8FKqoWG8TYd-788VjWP83RNzP8XoCzihhNEq4bTJ9COSY6KbU4CYSm9xQ17xTJPLkoWqOVKGQprYrJZepPVBl9IsAC2GE8_0AGQ_LXtCKx3E90cCamikmc_m4bWsihrEiOWKaOFD0iZ-L507PkNfseOwpTG8zXZzEK0onYuha5taOmp7GqZ67T5KnXTXD_R3p_-rff5wrKulq8gC3Gm20ObsTn9FIPtBxxkLFD152hjWgLfKDfvdZ944DvIjSMcaDk4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس سازمان بهینه‌سازی: اگر به‌جای خودروهای بی‌کیفیت و مونتاژی چینی، کل یک خودروی ژاپنی را وارد کنیم ارزان‌تر درمی‌آید
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/alonews/141915" target="_blank">📅 22:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141913">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EXgv2KZiQCpvh5kLPSguX0DrsP9-hPPhe93aWtDI6nRZ__psjummyKoCOeLlg9YrqxHZ7qA3eucRCPxK86ZKLMLjYCRPkJI5S4ec39c4hIA9UUMT18vAMi4LmfXvIro51uQUkM5jBd3yZSAbHzjtuKG7A8TiB_GiDqI9uOcBqtj1JjMZPUtFqRhtVTFZ2S3DcKJZbWzCdlW1prcWx3nvwZXvCoq4f5ke3a7TgDqzFeTpfbbgjEUNtJlp5G94K4ngTasVDYSUpvztu_g6QeA2ZeSs3SVvUM03fjjXt1NmLymsTk3orv_QtfzEi-xlH35vxhpK5TXl2pBLQpPMJv5-8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MCHZFyn7Jc44SoBKN2B6-XaathlypH5HaD3lyVIKSD-vMV4HpcbGA18TINebP8lKca7arRnLWDvaj-Ph34MSm7QfMGVVtZcJjy6vvLQkSGmp5IbMnkConpkF3pc2J-XuHMvIZLF4O_B2UiHbhMXle0r8iLIHY_kIoOkPhwLLGutMdJ7oy5CBXgk80PIza721Sdzw2i6ALBHGRi32LnlYhthi4siSWcMHOGq4gGIML1re_QzbE0OdVsWeTH8txRtIEXIXFuK2hqMCOthiWn9c_SM9GwbudTNK1gua-saZ4s29eE0tj5QsiUGn4EffUn3clYmy9LexzPINlVnC9lVBBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
حرکت قشنگ هوادار خانوم استقلال بعداز بازی دیشب
👐
@AloSport</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/alonews/141913" target="_blank">📅 22:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141912">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9f363f7c8.mp4?token=bK-2rkVMdIs-gtmBEEPwnASgg_inX7_xfkdKU6ZmWfpiDkXTL3mMaKlV5WlwHG2gxEt3XKtZ9J7WMF0ov1IzS8yc6Ve6CclSvUaLHC_cG9BfZ1beNeCvUPFb7gJXT_bDdXOBIRu-vWT0An69KtoBwJPEi3ZCVnLAie3lG8uCPv6ZALTYjeD5Hm7XnBkdZ1xyHi99U6ZWbyn7uRhiK-1n0mRYLXyewNrTX7klbF7lC-9xwF1CtJSZZ6TmYMXPTma6NyqWNCv-HWKIitMW6VtkfAoU7Kiny_HF8FrlezACaEOrYrbtAmDrCyJlEDhdN63JyVq_9wTsrvTQQmGa-kG2WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9f363f7c8.mp4?token=bK-2rkVMdIs-gtmBEEPwnASgg_inX7_xfkdKU6ZmWfpiDkXTL3mMaKlV5WlwHG2gxEt3XKtZ9J7WMF0ov1IzS8yc6Ve6CclSvUaLHC_cG9BfZ1beNeCvUPFb7gJXT_bDdXOBIRu-vWT0An69KtoBwJPEi3ZCVnLAie3lG8uCPv6ZALTYjeD5Hm7XnBkdZ1xyHi99U6ZWbyn7uRhiK-1n0mRYLXyewNrTX7klbF7lC-9xwF1CtJSZZ6TmYMXPTma6NyqWNCv-HWKIitMW6VtkfAoU7Kiny_HF8FrlezACaEOrYrbtAmDrCyJlEDhdN63JyVq_9wTsrvTQQmGa-kG2WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس سازمان بهینه‌سازی: اگر میزان مصرف بنزین خودروهای داخلی مشابه خودروهای روز دنیا بود الان شاهد ناترازی در تولید و مصرف بنزین نبودیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/alonews/141912" target="_blank">📅 22:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141911">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6aabb4acf7.mp4?token=FfTk-1Wn2MTJ7rnVgbpdLrM-LVNxGp2j5mwirTbkQMhV6M0P1a64u-1fL1Z4IlRPMmBxwCkhM-uRXEQqJOAf_TzOp2xp61gXl8j-e4glJjsDX6d5chzT2pt2QhCDZMPLAsG8u9pz0953JMFDN0RUuFUoOF1ldzGnHSsXR7Tz8DoK45Ej_dd8NAOMi1tTNuCJDXvDfxL-nBI9LQ9PenhhiSotH707E1oh2vGCavOI_Sl2tqgBePdpz9WPZL1XCBNJjBnCqaizzOxAG9Zu4un35Ug2e0MgwMHCTwBoHSw9UlYiqwGEElP7dJBd_OULNxdtCTKOxctqgyQnQ6pL-kxaJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6aabb4acf7.mp4?token=FfTk-1Wn2MTJ7rnVgbpdLrM-LVNxGp2j5mwirTbkQMhV6M0P1a64u-1fL1Z4IlRPMmBxwCkhM-uRXEQqJOAf_TzOp2xp61gXl8j-e4glJjsDX6d5chzT2pt2QhCDZMPLAsG8u9pz0953JMFDN0RUuFUoOF1ldzGnHSsXR7Tz8DoK45Ej_dd8NAOMi1tTNuCJDXvDfxL-nBI9LQ9PenhhiSotH707E1oh2vGCavOI_Sl2tqgBePdpz9WPZL1XCBNJjBnCqaizzOxAG9Zu4un35Ug2e0MgwMHCTwBoHSw9UlYiqwGEElP7dJBd_OULNxdtCTKOxctqgyQnQ6pL-kxaJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سقاب اصفهانی، معاون رئیس‌جمهور و رئیس سازمان بهینه‌سازی و مدیریت راهبردی انرژی: نرخ مرگ و میر جاده‌ای ما ۳ برابر کشور همسایه ما ترکیه است، با اینکه جمعیت و تعداد خودروهایمان شبیه است.
🔴
در تصادفات هیچ‌وقت نمی‌گوییم خودرو بی‌کیفیت بود و هزینه‌ای برای خسارت او قائل نیستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/alonews/141911" target="_blank">📅 22:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141910">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
واشنگتن‌پست: متحدان آمریکا در خلیج فارس درباره اینکه آیا واشنگتن می‌تواند به یک پایان دیپلماتیک برای درگیری دست یابد یا نه، تردید دارند
🔴
مقام‌هایی از عربستان، امارات، قطر، کویت و بحرین پس از ماه‌ها حملات ایران در نارضایتی خود اتفاق‌نظر دارند؛ برخی از آنها درباره ارزش ادامه میزبانی از تأسیسات نظامی بزرگ آمریکا نیز بحث می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/alonews/141910" target="_blank">📅 22:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141909">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
طرح اول پیشنهادی دولت برای بنزین چه مزایا و معایبی دارد؟
🔴
در این روش قیمت بنزین تغییر نمی‌کند اما بنزین تا میزان تولید ۱۲۱ میلیون لیتری در پمپ‌بنزین‌ها توزیع شود و وقتی تمام شد، نازل‌ها خاموش می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/alonews/141909" target="_blank">📅 22:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141908">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-poll">
<h4>📊 🔴تو شهر شما هم عرزشی های حرام زاده موتور سوار، زن و بچه مردم رو بخاطر حجاب و پِت اذیت میکنن؟</h4>
<ul>
<li>✓ 👍بله</li>
<li>✓ 👎خیر</li>
</ul>
</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141908" target="_blank">📅 22:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141907">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
رئیس سازمان بهینه‌سازی: باید کلید اصلاح تولید خودرو را محکم بزنیم؛ نباید هزینۀ مصرف اضافی بنزین را از غیر از خودروساز بگیریم
🔴
باید شماره‌گذاری خودروها و واردات خودرو تعیین‌تکلیف شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/141907" target="_blank">📅 22:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141906">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
سقاب اصفهانی، معاون پزشکیان: تو خودرو سازی از اول انقلاب اشتباه راه رو رفتیم
🔴
پ.ن: تو ۹۵درصد زمینه‌ها اشتباه رفتید
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/141906" target="_blank">📅 22:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141905">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
گزارش صدای انفجار در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/141905" target="_blank">📅 22:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141904">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
گزارش صدای انفجار در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/141904" target="_blank">📅 22:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141903">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
سید عباس : آتش‌بسی وجود ندارد که بخواهیم آن را تمدید کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/141903" target="_blank">📅 22:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141902">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
سردار باقرزاده: 3 خلبان ایرانی پس از سقوط جنگنده‌های سوخو-۲۴ در جریان حملات اسفندماه، زنده توسط نیروهای قطری اسیر شده‌اند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/141902" target="_blank">📅 22:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141901">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
آنیتا آناند وزیر امورخارجه کانادا اعلام کرد ابراهیم عزیزی، رئیس کمیسیون امنیت ملی ایران به دلیل نقش داشتن در فعالیت های تنگه هرمز را در لیست تحریم های خود قرار داده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/141901" target="_blank">📅 22:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141900">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏
👈
الجزیره: کمتر از ۳۰ ساعت تا پایان صلح ۶۰ روزه بین ایران و آمریکا باقی مونده
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/141900" target="_blank">📅 22:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141898">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aGUrS6G9jOmswtB-hsBBRKLdriiZKvRmhB7d2EtrAHXqF5KNT92A6gaGBh8lzBQmUW74TJ2QEGj2h-0e3zKzIHaIld5YPZeZ4fZyrlNljg1WTFHHWHpaMUgJOePeEp-LJy7NXtCVowZuNYT-AciJAnnhp8hVwCzHZxR9uGr2UP1130LVjwC_vVAhVP43ixnsBeNZ1ggbr3qmcVroSTBLvEEYVxOpBudpHg3TW-NslaYZDleaym_wQjjYa3fMojjF83Y6FOWPF06OEivxhmvgN9CVS8oVqa3o5K0h_--Qw8yzCO-RqeP8V9VfTLnU3SDS8UqkRUGWUPli5dobFFvS2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vaO9BZuvA9PqmZbQAGrJH1eR04IJUodvRfTCpVvI0--qovcKuSPbiKRfB10xWLFUIxfSFWdcQ_r1zaGutySbiM56cpB6HgQwjzYcpiQgTlC2YyBTLwbFdkinPdqClKlwmLFKvgbpgI0a3m6XGmeIVQZFk_b4VJhe40rMhnuir3dfsLtVbWW5kSLQqy1rClNzyME_g5y1T6_et97PCW5tqbXy6ZQn56P081aepaI_msJ_aMW6YtCRh1F16o7J9U2y5SBNWZApGUmwxkXFi8gcGNKkJD5_6jDzTyiIlzB2JuWsy2BAkcIEgD-6F4RXpMCF3nFLOxAlT0cn7vdBwcekzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
در زمان قاجار دخترارو بر اساس سن طبقه بندی کرده بودن:
دختر بین ۹ تا ۱۰ سال : خانمچه
۱۲ تا ۱۳ ساله : نوچه
۱۳ تا ۱۵ : غنچه
۱۶ تا ۱۷ : گنده
دختر ۱۷ تا ۱۸ ساله:ترشیده
+بعد ۲۰ سال رو "پیردختر" حساب میکردن. و فقط مردای بالای ۶۰ سال به خواستگاریشون میرفن
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/alonews/141898" target="_blank">📅 22:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141897">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
این هم وطن
انزلی چی
ما حرف دل یه ایران رو زد.
🤔
قهرمان های ما همین مردمی هستن که با این رژیم سازش نکردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/alonews/141897" target="_blank">📅 22:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141896">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8994c2f3c6.mp4?token=oEDumC6KS6Gn-VVS0hLAE80Xn0TN0cm4_89r1PDAy7JNjljm-wNhT5GF4Rr1f61AIDQWpCyeYe7XM-5uMAjfXQAnvEKtCGoc1I59wJm5_UD9BZoSm-Tr92KaaPIfhTiul_KjX3D-wl15ub9CGy3yYLJtg28KTaXdqKFudsP7BhxWy_DOkesqBbu1kYXf1AbX8pyTxC9HaR3ewZUCDPtbghHsVSlgbpgvm4G_6F0v0QUUUz8JvchTQRsiBbm5GEPl4OBsGyM0lim7LMB19vfCZ7XG_4C98OdMo480wLWhrRhi6VYEYczbCQsxacYY7nRigO1Od2IL_6oW5BUgVksyJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8994c2f3c6.mp4?token=oEDumC6KS6Gn-VVS0hLAE80Xn0TN0cm4_89r1PDAy7JNjljm-wNhT5GF4Rr1f61AIDQWpCyeYe7XM-5uMAjfXQAnvEKtCGoc1I59wJm5_UD9BZoSm-Tr92KaaPIfhTiul_KjX3D-wl15ub9CGy3yYLJtg28KTaXdqKFudsP7BhxWy_DOkesqBbu1kYXf1AbX8pyTxC9HaR3ewZUCDPtbghHsVSlgbpgvm4G_6F0v0QUUUz8JvchTQRsiBbm5GEPl4OBsGyM0lim7LMB19vfCZ7XG_4C98OdMo480wLWhrRhi6VYEYczbCQsxacYY7nRigO1Od2IL_6oW5BUgVksyJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زندگی یک ایرانی در ۲۲ثانیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/141896" target="_blank">📅 22:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141895">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
طالبان هم فهمید برای پیشرفت باید دنبال رابطه با دنیا باشه و جهاد رو بزاره کنار اما جمهوری اسلامی نفهمید
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/141895" target="_blank">📅 21:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141894">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19a93bd565.mp4?token=IBtCPvuzRVLtKd-j8GqIBf9dkv2wmhk6uqTfi67ea4JOp5Eks_uS8XJ3Rp4DLYbWmpxf8BlT0MwG-q04kCszAzZN89AU-SyEE9OCTrecR3sGW2FSbWbITa7E6g6_T9gCKQgnQijAeSh5-AVw6QAxP9XzqBeN_UMJmjqcK-SGVwX9z9rmkzIQS8I20haIknKGiBZOaRM_GBUdzJi3K58zWtsD1TCHcVWxCLi14XUjYWBnFG51oildI3CMNrqOqNOjMQHKQnXLy96m5KaDahC0RjdKso5TiDC2Gfei-NRlkWW77ZOAJ6hAwJS-YswXEPm_-VhoL9Ar66QrLvJXMVheTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19a93bd565.mp4?token=IBtCPvuzRVLtKd-j8GqIBf9dkv2wmhk6uqTfi67ea4JOp5Eks_uS8XJ3Rp4DLYbWmpxf8BlT0MwG-q04kCszAzZN89AU-SyEE9OCTrecR3sGW2FSbWbITa7E6g6_T9gCKQgnQijAeSh5-AVw6QAxP9XzqBeN_UMJmjqcK-SGVwX9z9rmkzIQS8I20haIknKGiBZOaRM_GBUdzJi3K58zWtsD1TCHcVWxCLi14XUjYWBnFG51oildI3CMNrqOqNOjMQHKQnXLy96m5KaDahC0RjdKso5TiDC2Gfei-NRlkWW77ZOAJ6hAwJS-YswXEPm_-VhoL9Ar66QrLvJXMVheTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای یمنی مورد حمایت عربستان سعودی از یک پهپاد انتحاری (FPV) برای حمله به یک خودروی متعلق به گروه انصارالله/حوثی در خط مقدم جبهه استفاده کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/141894" target="_blank">📅 21:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141893">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e32c238411.mp4?token=gQgdcSkDKMK1OxAkCpKDX7lL0behGXyUREODHKamZp3Pk12CBOCS4u39Zprj998nBs4gihTlxdQ3QOn3WiqO7Ce3CtRqC_xH6eyHIgFRk1oKs06WFBhXzkd4Id80dAu9WETW4YYskK58rb3p9WP-mWAF76e3-pa2XrHGo_IV1pM38tJ-ghd0CCMK8_NLfteSfxg1eV8xPJ9pBx-HG0nGg2JBGThFqfqqPpEfg8Tbs9C0SwxKcSI7MPbhQwOzNC7Stt8H-OjaDfboCGwenML5INg_o6cI2Sy15iDvwPmRcDd0q-ANIvkWB1DsFKoIhRrMEibzJHzXZp2vOLdPoH4QJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e32c238411.mp4?token=gQgdcSkDKMK1OxAkCpKDX7lL0behGXyUREODHKamZp3Pk12CBOCS4u39Zprj998nBs4gihTlxdQ3QOn3WiqO7Ce3CtRqC_xH6eyHIgFRk1oKs06WFBhXzkd4Id80dAu9WETW4YYskK58rb3p9WP-mWAF76e3-pa2XrHGo_IV1pM38tJ-ghd0CCMK8_NLfteSfxg1eV8xPJ9pBx-HG0nGg2JBGThFqfqqPpEfg8Tbs9C0SwxKcSI7MPbhQwOzNC7Stt8H-OjaDfboCGwenML5INg_o6cI2Sy15iDvwPmRcDd0q-ANIvkWB1DsFKoIhRrMEibzJHzXZp2vOLdPoH4QJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهردار ایندیاناپولیس در آمریکا از ساکنان خواست که از راونزوود، راکی ریپل و سایر مناطق  به دلیل سیل شدید که بدترین مورد در حداقل ۳۰ سال گذشته است، تخلیه کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/141893" target="_blank">📅 21:37 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141892">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
پس از حدود پنج ماه توقف، پروازهای مسافری فرودگاه بین‌المللی لارستان با برقراری مسیر تهران–لار–تهران از سر گرفته شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/141892" target="_blank">📅 21:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141891">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gg7DPs158zvpCY9eAvEgN_ZL-VdUREFyel35ZjqPBgqlaR7pBEC9HWIlqZ7BnX7dQlQL3-EURjg2h0Egvrm5r8wbDWIBlLIRsjg83F-s94n85NXhZ5eKlPal3_bhp1uKZM8sh29lCVIP9-PtGaQeVl8JvA123XdEfZMJeqB63CInr88iiB6fNYAxFxIlgON0ogxNLCPubH3HFd3bmHNbYwQVgmx7GZD4mmYLC1pRkb0JjC4AEiUrVevVQI0mmAJCNbmGSa1wvNM_6bhrgpuk_GVCXUEXVnRmmwecZDxMnToZaFPeDDkRJe-4mRobd7y-4_Mv1ASWamMUmT1-ydiMLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور کلمبیا، اِس‌پریِلا
:
کلمبیا با اسرائیل، همیشه دوست و متحد بوده‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/alonews/141891" target="_blank">📅 21:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141890">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtaiXTvA8qmnqSPqrnqZSlEQFvDJtnlTRuNJmoASmbDrwSJWqB6QOFvdYWDdgUEgrR0kHse7lZEZblEdGWeXBxylny2GUZn0xIQKAJkhlFbaBXcT3yeiFCfEumw_3eImg1-1DzWzhgSMN7L-hXl2m4V3K9yCkUV_JVVd17As7yRc9EO4e2ZZqg7JP6fOBebxlxPjEO1W0q-Ba56SocK8iji45EnkT9dWiFLH7C4TxbQqCrTNi9Rv6-Mo-ch8kEa0-0c_gzCGyIQeDE38r3WUSdM87sBrlvwscwcxKkt7FVD6g7m9BCIvl_Q58F0goZFnP2pKHk7BAR_oYNz7LDP_xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبیه بری ، رئیس پارلمان لبنان : اسرائیل هیچ ارزشی برای هیچ‌گونه توافق یا قانونی قائل نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141890" target="_blank">📅 21:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141889">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eoyr4n37iOlNvUZq6TXtBbxZiQcKvLbnpbi_xzeG5mgYQNzVv85M6fOk7Fc4l8X3xdDPpWgBrJS4quccU6q7P6MyBj_xEOkJRmAAzhxcOYcjuQ_RCykPq7gkvC-vTOunhyp2pOQqWOQyGuNaaUoBGXKojXWHMZNmDAVYso7bdQZbeBeDV9H2BVAZYXdF2_xmPao_QQHC8MvHj4gp-T_BoKrAjBunz95V8AzNdHlu-06tYC-blbgZMo3prQ52EbpTdh3dHyt5V0Cd_rI8FaUBdycnF-P4x0KnJdfgUH2WAUXqjiLI1GO5cfmv8pDeQV68cbYgm9BN_15R3xLpJj5QbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در ساعات اخیر انصارالله یمن حملاتی به دو پایگاه نظامی صحن الجن و تداوین در استان مارب انجام داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/141889" target="_blank">📅 21:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141888">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بچه‌ها این گردونه صراف رو چک کنید، من الان شانسی زدم ۵ دلار بهم داد
😐
😂
انگار اصلاً پوچ نداره و به همه یه چیزی میده.
برید بچرخونید ببینید شانس شما چیه
👇
https://r.saraf.app/s/agrd309</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/alonews/141888" target="_blank">📅 21:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141887">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPt3O48LMG2-u5-iKjyU1C995miQCGVc_lHlkJ4QuxnxAwFK0Hbaqo5n2HNLw9Jdd0cHcIZVZjDwxyk0tRoUbjqgAbXwEq32k1eWLQbg07TtSb2D7miMyOlSnQilrqBwuQITAiXDxIFQgEhf_S6ivI9UaWH1xUyEo4MfrHyWL2Erv9Nhr6lvw8-jZq0A5nfD0tuCrY0yR2c5HQ0kHip-ObichFnON_yXAllo0QQqxKyQwpP62k5oUsGtDj88py7e4HxD8IdaG1sI5w53P4YuIm2zIHH390njByzvnYhzN8M_gVIFpCBIZx94o69PTLIKGPxqoLjgaFXOUhBaP4wBtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
اندی بیکر، مشاور ارشد امنیت ملی کاخ سفید و از افراد نزدیک به ونس از سمت خود کنار می‌رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141887" target="_blank">📅 21:07 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141886">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
آتشبار توپخانه اسرائیل به شهر عیترون در جنوب لبنان هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/alonews/141886" target="_blank">📅 21:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141885">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I40bByWKOF2fdlMkOXtX56jpvDa6T7tntzr5HUtX6F4o1uWLpZnY5ONPJG5RYv_D8L6DbomjwCoqQDqyL4weOKIcwbLidShB5xVCuG_68JLRW3Gh2ZVv_bAQfo8bY15T57jo_STsWNrIJida9ZTCH_-9KeNQ7zPZoFboWU4VmbARGe8UEpFt0DC8kmws9JeRCCrub_ghcqcZJutY0jPDsEXML2Iv7GwHWiiBvLPN1ra2XgcLkhXOPAOene7U2GyOpllO41XbFLaiQHGGiP0bXvFH9F9pwh1ZZYpRRmBM9_5QIIWdrSNZfDohwFAebSaTxPAndV1SwtkEvbCoonWfgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجاری در طلوسه، جنوب لبنان، به دنبال فعالیت‌های تخریبی اسرائیل مشاهده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141885" target="_blank">📅 20:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141884">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
زلزله‌ای به بزرگی 6 درجه در مقیاس ریشتر جزیره «میناهاسا» در اندونزی را لرزاند. این سومین زلزله بزرگ است که ظرف 24 ساعت گذشته در این کشور رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/141884" target="_blank">📅 20:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141883">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DS7qvOWA5y9gslBzDyf-XK7ZQy_IRBcnH6ZDHBD5GbL_bzU5Njp5Kngb0gpH3iTQXL2ul1Xpf_9U9diHBq-Ttbh2eH5WOHgAWqAaKTtvLR-7WfY3JgsBRyxxFgSyV6In7frVHpB6AHejfoFSNjcR0uIaZuJRwBTE-AzmThVBPjkkbhtAPPovPJJUGbvyCdhbjoG5zlfBBO23T5h7LWA2lAaNd-B4nU__YcQNGRSA61V1mxUxSma1j2gH5QJHBgCMFHVVTitVnIC506NYa88Ke4mOixRHN70KJNLnrrvaGXVaYL-wxsjIkeX7M3B7p-SZI3VB4oypTBu9hvQERl5zTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نورنیوز: ۲۶ خرداد، تفاهم تهران و واشنگتن شکل گرفت؛ ۲۷ خرداد، در منامه مقاماتی از آمریکا، اسرائیل و امارات دور یک میز نشستند
‏
🔴
موضوع فقط تنگه هرمز نبود؛ مسئله، جلوگیری از تثبیت تفاهم بود.چراغ «اتاق تخریب» درست یک روز پس از «میز تفاهم» روشن شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/141883" target="_blank">📅 20:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141882">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txT31zW3PMDX5b3S-4sF3hDryXa0bNBQo4uGlyX-zRHMKtiZBRczSsoyTD3kQfsJ7g6MSEBF0jOawcq9R6EmKh-M_BmIBpvjrsleArh2sx5UiPF8IYJuEqK951FVon4DFpKRm2q_nNj_iK-wPHQWjEM-f2UxMS7jCpM01HR1yhyqYn1S685aInCfyQ1YdVo3UgWaJARX8aBuN2DARRCC8wLayv93uLmTQzTaUSgs57vwwKPFXXH3hALrPFjxBT4kB1PzG9OCtk2CGoyqBcdnFTCuDa1AeAliFyvShRYnZf1TIsvbk2LlH22wuPqHmJdHQSdOrKdZXhhIMfxKcImmpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حماس اعلام کرد دفاتر خود را از قطر به ترکیه منتقل می کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/141882" target="_blank">📅 20:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141881">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9091137d97.mp4?token=uy32GdfhMJjeszCzwN0JbXTKNJHEB9j6SCkAXCUjvDU2C_abbwUk9U-tAdIQEvOt4S_REWa2kzLzgMeJyl6vtPwFKHwHaT_Or-d8gx1SIEGP3RJshU5PBZx-Vwid04jVRwD35vHRMr85FVYnk2DDlbQPPsTIRxwdT1koFZ7RlTsVDSZduQtJNr1ho-6H3B9AxY9LTB3P4ZYs2xzQxl36F3xI-ZkJaGiVlxl3btHctkf0VC_ltzMpdsjMQtA3hGJp6eitgvHLIKBPbZCtqoELySpqPnsVckplz40YWhmsdgnV2boe_KtG5jGyfHGCNV1l0DUQmPVOL5n1blnoVejXXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9091137d97.mp4?token=uy32GdfhMJjeszCzwN0JbXTKNJHEB9j6SCkAXCUjvDU2C_abbwUk9U-tAdIQEvOt4S_REWa2kzLzgMeJyl6vtPwFKHwHaT_Or-d8gx1SIEGP3RJshU5PBZx-Vwid04jVRwD35vHRMr85FVYnk2DDlbQPPsTIRxwdT1koFZ7RlTsVDSZduQtJNr1ho-6H3B9AxY9LTB3P4ZYs2xzQxl36F3xI-ZkJaGiVlxl3btHctkf0VC_ltzMpdsjMQtA3hGJp6eitgvHLIKBPbZCtqoELySpqPnsVckplz40YWhmsdgnV2boe_KtG5jGyfHGCNV1l0DUQmPVOL5n1blnoVejXXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کمین جالب FPV روس علیه نیروهای اوکراینی
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/141881" target="_blank">📅 20:33 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141880">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
نیویورک‌تایمز: اروپا که نگران است ترامپ بدون حضور کشورهای عضو این اتحادیه درباره جنگ اوکراین مذاکره کند، در تلاش است تا جایگاهی را پای میز مذاکرات کسب کند
🔴
فرانسه، آلمان و بریتانیا در حال تدوین موضعی مشترک هستند و انتظار می‌رود که کشورهای دیگری نیز در این روند مشارکت داشته باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/141880" target="_blank">📅 20:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141879">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-vD86uJR_YaJVVqrh6Eor2l2JrpijxLLOiQEeDebFOsNhh2H_pAYaDIcWmICjviNPuLus1f1wT3ga6I9c_SlKy4ugR84OzYcrot-bATvx2nHZ3oxn-2_FDrY_NbBC44H2dD55ogGKVhUqV9X7gyYPSCJI-Fa48xPO2BPC-TtJR3ZMgR64YN0kAf57AbTBuAz7J9Z_0xqVMNhMDJAKLug1HYc_SwHQV_nSvPKp2hGGS0mOmUdMKlXbmzlH4_iqQvZtt35kyzeGrGRH5OnDAXK6fklrT1x-vTke5UKX8F7R7MGwBJzYWgJ_jvxKjMuevGE8UEtICOF_mPZ0tk_T19mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مایک هاکبی، سفیر آمریکا در اسرائیل:
نیروهای نیابتی حکومت ایران شرارت محض هستند. حزب الله کودکان را جمع آوری می کند و به مناطق نظامی می فرستد. آنها نظامیان اسرائیل را می کشمد با اینکه می دانند این کار ها بی پاسخ نمی ماند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/alonews/141879" target="_blank">📅 20:22 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141878">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJJ2e6bwbb5_2bdBAOs9PJxdQTJp8Ns3wMtTKtJP9Dn2taY38j0IJPb0SUmn1UJdP9hfdBxLnpJ2nsavSFxOwX1RrG40IPeaqmmdWL1PZos2QBe-rPT-weeU2_s0OYVUl7GmT2L-AUYzP08m-PhZdG32tpQXo9z9Ui0JuDe1SCteFs_ozGifzMjIyIFgZ0Ku5Ba18AdGr04mPDz5pXrDDrhJJl8qyRYtoh6kaZ1w_-1Vo3ej2hF6coOexXalWmWx5JYcxiSD88J-MUM50vXATWWBPzEl2N4pDocWTxFyhTzEjt2FcI85c5m1tqmIcwLe_vSb9Ntxh0hycFYI8UoMRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نظرسنجی جدید شبکه CNN: محبوبیت ممدانی در شهر نیویورک در ۲ ماه اخیر ۱۱ درصد افزایش داشته و به ۶۹ درصد رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/141878" target="_blank">📅 20:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141877">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل: بر اساس اکثریت قریب به اتفاق نظرسنجی‌های فعلی، نتانیاهو در این انتخابات پیروز نخواهد شد، و آقای ترامپ و مشاورانش از این موضوع آگاه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/141877" target="_blank">📅 20:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141876">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
سوپر اپلیکیشن "بله" از پلتفرم های ایرانی بازار و مایکت و... حذف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/141876" target="_blank">📅 20:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141875">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">خبر عجیبی که دقایقی قبل اومد
😐
👇
https://t.me/+nCexQYLuuONhYzg0
https://t.me/+nCexQYLuuONhYzg0
دلار و طلا میریزه
⁉️</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/141875" target="_blank">📅 20:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141874">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7k3DY2SSDE9bVz2ppjYefy3CkEtCAZJghaDtX7VgkkgYGVZOZmzqm1_8lcCCUkAIUyonhng9QCE_Hs9yAHdCq3VJGLQwO-7R_IpZJqt4gExYWokAcsYidr8nYn1Hfp9vwK-bJBzT-6HBNwlaDDgYxencB7kaX7WIZT5bYTs85EDg9gt39IAskW4V_VGIcuCOvm6QAvIgcAdKkhXlmNQbIaU5L5K6aPb3TaIMRk-QyW5EKWKHV18zZKYasF-POnrBBwsk0wLyFPr3bxonEjVpNOaMvMtW9XAfOJ_4fOJOx31M7A65XgOfqtzFe9nO-b5EG5hfc6mgC_HGLcFp15Kpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری تابناک، سال ۱۳۸۷: خیز دلار برای گذر از ۱۰۰۰ تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/141874" target="_blank">📅 20:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141873">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
وال استریت ژورنال: کاخ سفید در هفته‌های اخیر بیش از پیش نسبت به دستیابی به یک توافق نهایی هسته‌ای با تهران بدبین شده
🔴
دستیاران ترامپ با ارائه داده‌های خسارات تحریم‌ها، او را مجاب به تشدید فشار اقتصادی به جای جنگ کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/141873" target="_blank">📅 19:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141872">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuYFUPTFISadT7MG_99X2sseMIBDaJQwebp5pP6A82X2baZk_8nLfih422sk9DVzVwK-F0QhybmZi4EhA-2C77i27U_2PVOXi_llTUeyfl080hc9mySyweXHegB3aevbYd6JPb8woZJtSmySXgVUiEiyFc1Z5MOqRbM5IO7OSmz8MeMdsenFhhSSlQlTvloc0OKIJI4Arjn1w9DbPB8tEG2Y1XICkJxaiA4NnXULx4oCB8tqbbN60a7ZgDnYWxLV5vJQh1uulxtTJcGi9N3wBGg8GjDbSFectTxr53_Wgq20P30G5aBVfOX_su3yN4W6j7PqmOi5q6oKr1OaXkAY2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: من و کیم جونگ اون خیلی خوب با هم کنار می‌آییم!
🔴
‏دونالد ترامپ درباره تصویری از خود و رهبر کره شمالی نوشت: با وجود نگاه غیردوستانه در این عکس خاص، عکس‌های زیادی هست که در آنها لبخند می‌زنیم؛ من و کیم جونگ اون خیلی خوب با هم کنار می‌آییم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/141872" target="_blank">📅 19:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141871">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okBkzBDNN-JsajLPk3sBBR_bHxZV49mG-owWy7J8lGLIykQVMwD8LnlCMvOVSXGNLEGwiTFgR_a4eSMjrt5_DP0TZJdA8qLrjz59Wf6gUChHXUWhpxMdZawIIwkjUXmdlbo0tajkRPq7Ao1PGNWsOc3kRvCaMtYr3laHdU6PQGRbNIWCKyN39m9eRNP6p_nbuL8nDeNg5S7O-cK9o9ctAq7z9HmoZl-TmkkSYO2VeyiLfC3rVwycw-NSkDiog9iiZdhndYgsY2LOvwLaITh08QYXIoZeia6DU0KP566f5GzfcOQsznw9sK2M8PWsW1LoNXUVrbpCDx1BeE2Hnou7UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حزب الله لبنان در بیانیه‌ای اعلام کرد پاسخ حملات سنگین اسرائیل به جنوب لبنان را خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/141871" target="_blank">📅 19:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141870">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/136da7e3a1.mp4?token=hHX4p2vnKwhnScbRRWnUNaboxS_7oUbbh_QIxzW2UDp8B5Kd3vJ6huHmj8lEUO3CEiya0b9la7X2Ngq_Epets6pQWlH1LfPtsqdmPx3U-b9Tso-_uiR_QEf6Sb5Ox0FZ76h5CdDChM1w3Ee3fv0qQtHheSXbH3lA0gmpx2AccQyg27fcZve6_6VN4vpgm0I_QNe3X-ub1YWHgdEICTV9epLIQYecB6ZGpgqtvCe-iqgz6WISajNHASWyGSjBSgC3_7QIHaU6xMY2MFj3M7XPc7Q8r-6-fkQCTtEcyMRrvtE2Jd5j03bkrK5KFB5ofx_Ge9qIjjyg8TxGgijm2JCMxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/136da7e3a1.mp4?token=hHX4p2vnKwhnScbRRWnUNaboxS_7oUbbh_QIxzW2UDp8B5Kd3vJ6huHmj8lEUO3CEiya0b9la7X2Ngq_Epets6pQWlH1LfPtsqdmPx3U-b9Tso-_uiR_QEf6Sb5Ox0FZ76h5CdDChM1w3Ee3fv0qQtHheSXbH3lA0gmpx2AccQyg27fcZve6_6VN4vpgm0I_QNe3X-ub1YWHgdEICTV9epLIQYecB6ZGpgqtvCe-iqgz6WISajNHASWyGSjBSgC3_7QIHaU6xMY2MFj3M7XPc7Q8r-6-fkQCTtEcyMRrvtE2Jd5j03bkrK5KFB5ofx_Ge9qIjjyg8TxGgijm2JCMxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سربازان گردان موتورزرهی 64، که بخشی از گروه نیروهای "وُستوک" هستند، به شناسایی و هدف قرار دادن نیروهای اوکراینی در منطقه زاپوریژیا ادامه می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/141870" target="_blank">📅 19:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141869">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
شجاع خلیل‌زاده: گل من به مصر درست بود؛ شاید ترامپ گل را دستکاری کرده باشد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/alonews/141869" target="_blank">📅 19:05 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/Z3Ch8Y_mxb-anIyJIR8PBMgI8u5-UGKPWkvQCO4lOV6FJjib6ZQRPAHMIcHj3V_iBPdm8-IpO5Iy_wl1WKkOt-qEjJNWPAtX-J1Yu-yz4WsfBDUK7iebyBfDN3KFs1jW8_7mOXGuAM-2Amx_K-aQO2NrZ8B8q5-Dfdjg7QGNsCOvvWF-NltI8nzsTCcUVATD9QYsCPVNlYoX1dtYkXejt75ldGGjW5Bnt-Z62iqvTQhz6ddS8Yc6OBN6NRgUeUe0J5Q_S8kCXKH-qXDOfpqvpHwuwDxKpJfZHfelfVUPxYXB2kibrO62yLtSdFHJmlVpM-aLou-uEkfevvKaeLT1CA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 613K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 21:31:29</div>
<hr>

<div class="tg-post" id="msg-26776">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWzOFoFdeadkCYEQBbuiMg2C-4Y2fAMF8BP7SQhpyZ7N7tubH4A3kZ9TqHEer3Yi-evVfK8-6drIARVWAzsCHAtUJSbJK-d3iSqOPSNDhgFGV4-4k9m01bRfqtOZxmWwlxIvP7pbGgXoNM974OnSw-0rXx9bdmIamEI5n63gWc7Dax7YMMau7XH-kZiXE1CqixXbssB_J8OXuZVf9ZLgq_JvRZUxW5BGjfmogLA3xBouuoU9fUoTgHPHXoDlOY-6f26ZnUa1a_DRzAbBWcsV8mnwl0O8nbGBzaWKSXpyiqiENUfhR2VmzZtmPcu6q4F3w-kPoENWU4Wk6w01d9ch5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/persiana_Soccer/26776" target="_blank">📅 21:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26775">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/762527d0f1.mp4?token=ANkwv7BWnrIBf0tv-infjyV76zmTEqi01www669_nk76SIu57Ubm4zvwqXczAO3M6tTofnqMmAwJ-EMqwXMigt_rWVzwLPQIn-T4ErtgF_g1mYqTDq9fzLlIJ2aP07lu-20LujymAOLN4PFLTItBf5A_W1CEn7-V_2--IBHCAyagakZ9F3rT7XJClCzMf7a65qC2LvCg3fI9FGIvBMIgnxlWn5qTA3nb9OOmhf__l5BwcThe8jHoNRUPC8hqtDZerRe7sPbGkXnSFcJ_1_v2x2v-ZYmsW9_lPBlaz_yVbkIWMyy4ZXEgFLP-cQZv0sfCQhJA3TWlqu1ox5VYp5hSqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/762527d0f1.mp4?token=ANkwv7BWnrIBf0tv-infjyV76zmTEqi01www669_nk76SIu57Ubm4zvwqXczAO3M6tTofnqMmAwJ-EMqwXMigt_rWVzwLPQIn-T4ErtgF_g1mYqTDq9fzLlIJ2aP07lu-20LujymAOLN4PFLTItBf5A_W1CEn7-V_2--IBHCAyagakZ9F3rT7XJClCzMf7a65qC2LvCg3fI9FGIvBMIgnxlWn5qTA3nb9OOmhf__l5BwcThe8jHoNRUPC8hqtDZerRe7sPbGkXnSFcJ_1_v2x2v-ZYmsW9_lPBlaz_yVbkIWMyy4ZXEgFLP-cQZv0sfCQhJA3TWlqu1ox5VYp5hSqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدشد...بااعلام‌باشگاه‌سپاهان؛قرارداد احسان حاج صفی با مدت یک فصل با این تیم تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/persiana_Soccer/26775" target="_blank">📅 21:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26774">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4063938cba.mp4?token=qO-TmDosqF87CAZUdEOrT_cMkRg_A1JWBinvqE1lONoNTP9BErHdMKVtnSpM5XZyIBoHlPHEaXHncBa7IKYpaO0Ro1FaKcHogvossbB4Xou4s0Sn9lAdOgffs5xopfGfxrHRKEVwpVJaMfMJymHBSsbOrt19Sib5BgZsfVK9CO3XVEJMm1hJla0TZhAD-EwKaN3a5Aasjv2ylYUYOnty240GZKENYiiX4pm48k8agW6yvt1N4DNr9wTStyApblqIleZjyloO2-9lJtpq2FvJj0iAL7qT1BJ3PkfIfNQl1P8n8q4xv0Kwcmbp8VZW9Jo4M3nCcepCFkOvSWShWcfSdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4063938cba.mp4?token=qO-TmDosqF87CAZUdEOrT_cMkRg_A1JWBinvqE1lONoNTP9BErHdMKVtnSpM5XZyIBoHlPHEaXHncBa7IKYpaO0Ro1FaKcHogvossbB4Xou4s0Sn9lAdOgffs5xopfGfxrHRKEVwpVJaMfMJymHBSsbOrt19Sib5BgZsfVK9CO3XVEJMm1hJla0TZhAD-EwKaN3a5Aasjv2ylYUYOnty240GZKENYiiX4pm48k8agW6yvt1N4DNr9wTStyApblqIleZjyloO2-9lJtpq2FvJj0iAL7qT1BJ3PkfIfNQl1P8n8q4xv0Kwcmbp8VZW9Jo4M3nCcepCFkOvSWShWcfSdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
استقبال‌فوق‌العاده مردم از علی‌آقا دایی اسطوره فوتبال ایران در مراسم ختم زنده‌ یاد اکبر عبدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/persiana_Soccer/26774" target="_blank">📅 21:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26772">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dhPEm4GfwBGNvOgC-cWcee2XiRZQFIaM2k_VJDa0PUt0PPunEfG0hFY4vpBZj7_7EhUBatX4PlkWCpam4rs_HKtuhrBzlwR5cfVFgOzZVpnWSVgbJ77-SLJ-3iqjlAV2ayKmxz4DssVEtNEia2pICH_zyuNTkqxAqsiz_lHesyKv22u52mAVp0ZdpyQgS-CI9J1YVDtshL2rjKdhBnqHYg8jlwERe51peSj2FdeASlGi0zyyiLFvVFIQXRMvWXk1uAhKnGZQclikKoMiVGmm5SwyD-_kzVzyIX65TG4mat5CA2zUxCFGz-js7G9Bfx58q29yd43ZU17_ppkMbJ-DeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W-_yEyu3UHNpDbgVpKGUoQNbTr3QiYDo7rQFYGgf0v8Ni-Gtr2LdEwH8Es9hs6LGMfySuZceKY3L355KeR3KG6dsdX2ixGk1Q9hUm-sUeuP3ttfdFn00U7mwvJCIT5ZnWuuXzEzxcI3btemFFsDFoNXVHewrMLsnHO3q0sC4qn8Nz4aPGN_vXXhGAI9ZZCnXT2wagPwA_ZHtC2T--jWA2xP2v35x60WCBF0iI3t31uWJO3XGiyrTfExVPtxSwc26qkeboB60sd-CS0qXlf2hNpwMEGNwjMIyJLgC_kQEQRBa6G1BA9dS8_TjKCMlc2tRsR52uDqXUrkq14zd_nMRxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
ویدیویی از مراسم عروسی شب گذشته گابریل مارتینلی ستاره برزیلی آرسنال با پارتنرش؛ مارتینلی حدود 8 ساله که با دوست دخترش بود و بالاخره دیشب باهم ازدواج کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/persiana_Soccer/26772" target="_blank">📅 20:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26771">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3befee8bbd.mp4?token=YNIegXpTOhkGOk6_wFaZ_zJxlQdw4djI7kgQM7YF-UcW21vkvxBI_QEw5EPuedFDZ6ZwhpUETgRNFmQeeyJZGZ2ORocCVYDVMjTx15rHolExjgzETjuJ118ii_ZdolRwdvOLvdI52l36GsDEekch7PKET0yyJp1vcosIoWz1AxIJFrZXlJh-TCYfnxaa8EmDOWBaPegCN3j0iBl6OsMAHyrADfyDDVF1GscsPoj3uZ2Dmj3QnYSI09p15Ag6-mZbIxL2hPTERWvFSt3DtFYyqF-w4qVZVNJWlQLiB1RURlJ8MSysUIyPxa8lVBY25yFytWMmfSwQQd7lqt1xphQTUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3befee8bbd.mp4?token=YNIegXpTOhkGOk6_wFaZ_zJxlQdw4djI7kgQM7YF-UcW21vkvxBI_QEw5EPuedFDZ6ZwhpUETgRNFmQeeyJZGZ2ORocCVYDVMjTx15rHolExjgzETjuJ118ii_ZdolRwdvOLvdI52l36GsDEekch7PKET0yyJp1vcosIoWz1AxIJFrZXlJh-TCYfnxaa8EmDOWBaPegCN3j0iBl6OsMAHyrADfyDDVF1GscsPoj3uZ2Dmj3QnYSI09p15Ag6-mZbIxL2hPTERWvFSt3DtFYyqF-w4qVZVNJWlQLiB1RURlJ8MSysUIyPxa8lVBY25yFytWMmfSwQQd7lqt1xphQTUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
حضور عادل درمراسم‌ختم زنده‌یاد اکبر عبدی که ساعاتی‌پیش درمسجد جامع شهرک غرب برگزار شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/26771" target="_blank">📅 20:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26770">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujiVCUmRHR50pJ5Pz4_-iCo--g_U-Y7zqjcN0V0pTjkM9Mo3Mum_IrqnDDtv0YwMjwHJX6GrY9pB2DVRjcVttnFmO9dlf7Qm_YxgnKLL_Uk3LGdqc2c2D2fpzdl82-tWJYVV1R3q68VEvRfkFVjBTwIZ8mYjCUaV2cfkbUSn6wIkKDxOL-hr_AcvWa-yLGRbpYxw7I77Q6_nfwc8IyyKq-18YUOjDiLz2xPlsKs5k6dfzmJgiby7mrvGzozTHm672xbwfa6obaa5AziOxFzrOIlOL7YjDsM3K31vXbuEuy8GqakFIbN-7-s0ciEsaocJY-5GDHf4nPaoLe6F_rxvxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇪🇸
🇪🇸
باشگاه رئال مادرید بعداز توافق کامل با رودری کاپیتان تیم ملی اسپانیا؛ ساعاتی قبل اولین پیشنهاد خود را به باشگاه منچسترسیتی ارائه کرد. انتظار میرود که سران سیتی آفر رو قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/26770" target="_blank">📅 19:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26769">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPu0WBbdhEffOdbCexdbnOYSlHhwury2RBeKNjtMiO_-Ix6byhE5iQz9o9yhB--zgKGrGMB3tnIiNCENhpHweJAl9CpyqXliQNNEAXHr_agtNfm_3nbd3YJmFkXHbBhe4nD38JQTSKshCFIZF5Viyq2mJ1ecNZ7GQPuhS85_A3I6byQ7mjnJd2DLA9rzP8Rb3ZshuzKoa-pMUOGdnO4xpF9eSu4lj9FUPt8DqKylKB34oouhmLMgYryZqsj3ZN-uIP5DociTEjCnhPpTSRtTVPCZTkT4_EPa3cFE5mW2WTD0-LPXd2MRdOrKk3mS9LDIWgVdh9f8JEnCT0KBDljzZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۱۰ بازیکن‌باارزش درمارکت؛
هالند و یامال هر دو با ۲۵۰,۶ میلیون دلار درصدرجدول ترانسفرمارکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/26769" target="_blank">📅 19:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26767">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee1553fa64.mp4?token=c6ZN0vfxEd3sqq5CDMgIrj0pgwZnoQCm3LG2rXaQ4H03ciSeBHQFVDO7CthTLKc0-bU8y53hdmZ9yTxBlhwtN930JMsknfJYmNjfg_TOXjjDSip5BAn8Z7w_o8fdP_4F6GgdsgXKCseDZ3VOc5j0ZcvA46ap_lMQI69YVs3NbMIKvcS1gzT5kFKfPc-hHyqSJ8AlRZjxgiI7LpU4stRmawjvREo9oH3UKRPZ9gMN00k1W2FiMqRJhiK_0kwZBWf7ZIRoKgrl78NGXm5ts5gWy0T72Du_WWRSH71JPZs1Iuyy12x9ipmagQ2ExIbiBqOXGAQdCOXOhDMVtKogkdbkKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee1553fa64.mp4?token=c6ZN0vfxEd3sqq5CDMgIrj0pgwZnoQCm3LG2rXaQ4H03ciSeBHQFVDO7CthTLKc0-bU8y53hdmZ9yTxBlhwtN930JMsknfJYmNjfg_TOXjjDSip5BAn8Z7w_o8fdP_4F6GgdsgXKCseDZ3VOc5j0ZcvA46ap_lMQI69YVs3NbMIKvcS1gzT5kFKfPc-hHyqSJ8AlRZjxgiI7LpU4stRmawjvREo9oH3UKRPZ9gMN00k1W2FiMqRJhiK_0kwZBWf7ZIRoKgrl78NGXm5ts5gWy0T72Du_WWRSH71JPZs1Iuyy12x9ipmagQ2ExIbiBqOXGAQdCOXOhDMVtKogkdbkKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوان‌رومن‌ریکلمه درباره‌ مسی و مارادونا:
«مسی و مارادونا دو نابغه‌ان. عادی نیستن. کاری که اونا می‌کنن، هیچکس دیگه نمی‌کنه. من عادی بازی میکردم اونا نه. حرف‌های فروتنانه و جالب از مردی که خودش هم هرگز معمولی نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/26767" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26766">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3lB2h8HXbW-gyZvzMR4nJhvaAI8g5kS1alWnvB0pDrgZrqTsA4wvBM_wbI8Cf_vlbtRmL_zgLfhq5eYJbxpSMOFzJkFJvuvsOcYvMxnTl0yP-DzD2ZETzIB_QDo9OCV_UCkfjTDo3VdJlzaCU417mFmoadZ47qTwLPTBRyItx4HcekWJWsVQLskL6WgGaIJ_1C2s_D2SYwmUHkDPfmKTh4wOxAZzsVO2rJLzBVbUkI0nD8yAl_JAF-VtYapq4q0koOaz5cdmewm6G4gje1azzTxHZN8lGFLLqrUzzYAtb1Q0dk9pTw2eVXjtvDbVO177E4_uhfQ-7vcHp0-a5wjzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امشب‌محمودرضابابایی ملقب به "بچه" به رفقای نزدیک جواد نکونام گفته "بی ناموس عالم هستم اگه اجازه‌بدم‌باشگاهی با جواد نکونام قرار داد امضا کند.
‼️
سرمربی‌سابق استقلال ظهرامروز با مدیران ایران خودرو برای قبول هدایت‌تیم‌پیکان به توافق رسیده و قرار شده فردا به…</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/26766" target="_blank">📅 18:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26765">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqpiTTot7-N2bcDHdN5ttwKoDvm4KTzNmDKYjQeF0iW2ZsMOjHkhC5ZzrY72bfeXByC88eLhiUdj_zt_DQhgEige8R-XUGA_FUhZ_GSnO_xKSWdXnWt2_Qwx_GuFSI2wBZpwaW09_YbldtLJahT6GbyPQmU69HrYiVBqeAppzzWYvWvQJILSH9mUn24ZJhFoup38ORIdTWhnLLzIfKiA9RwATk7Y7DT_aTC21K2Lx0738aopqh5JR5Kx0DyVYc-XaHap-04NCaZ6hiEX34RP8KYFnUcHdSgt2CNR0fvPNKRK43_az54nOI40PCrOUko2QxWld1GhJeMDOMN_E5-EZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
نگاهی به عملکرد کریستیانو رونالدو در چهار فصل حضورش درلیگ‌برتر عربستان و باشگاه النصر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/26765" target="_blank">📅 18:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26764">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97aa505010.mp4?token=uWKPxEQq-bjGr4FjW9q23ajGh-Vp1rDp10NXHNCxgR86Y58acY7M6-N7ji-yxKsh_w7yhZsux0A9rbOU2BbA6HTHDRl6QIrCiCIqELltP0QdHqTZbssq7_gFY8H693oJL_Ums4iaO2kjCZA5xmaYVAhTka2djXQ8pidUuwaeRiD_9WLWJ-gdNfBQ2E0DYvkq8YL4cAbFmLbPqeHGiVcdQ-4-HYCr1f7kO0FyRGLO3KAUV-TnhkUBcnMBy2IDdB1E1f4zDODwT9-iljLAHh-8jEgV82_jXhkOXhS3FiJNNjlR-v-5ASjUYGrOim-TY3PQecC4aHZfrbWkzx6sf0zpnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97aa505010.mp4?token=uWKPxEQq-bjGr4FjW9q23ajGh-Vp1rDp10NXHNCxgR86Y58acY7M6-N7ji-yxKsh_w7yhZsux0A9rbOU2BbA6HTHDRl6QIrCiCIqELltP0QdHqTZbssq7_gFY8H693oJL_Ums4iaO2kjCZA5xmaYVAhTka2djXQ8pidUuwaeRiD_9WLWJ-gdNfBQ2E0DYvkq8YL4cAbFmLbPqeHGiVcdQ-4-HYCr1f7kO0FyRGLO3KAUV-TnhkUBcnMBy2IDdB1E1f4zDODwT9-iljLAHh-8jEgV82_jXhkOXhS3FiJNNjlR-v-5ASjUYGrOim-TY3PQecC4aHZfrbWkzx6sf0zpnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛ گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/26764" target="_blank">📅 18:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26763">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivmS-FwcCJlK4nqwkDJPQoxMhNsgIAxWfvWI2k5lOXVtXdxKYRkTLumpSH7rCKRC6tCX1hdasGVn0igtjjvjy6RBG4WtuVxD67Hoa-0PLeyYd6-qqE2bSlVzjIM1PQHTI213Z42E78uZB33Edu9V7eIyHT7O7RbTlqaB3KFx_vGp3tFO_BBeN3aLCiS7hN_CbSAq1o-ySH-bE-OoGDRo9LoJM8MlK-dUgqFQtv9t-alFRWOqe8LFd5kUpZJidsvHF8LVv06hGQ4hY8_CcdtCoUnM9xSZa7wqwjw5fhA4TuZNI-bldZuZ2D93utOzSeOyr4dWsJP4uThOwNLNngBfvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌گفته وکیل‌ایتالیایی‌باشگاه استقلال؛ ظرف امروز و فردا دادگاه‌عالی‌ورزش CAS رای نهایی خود رادرباره پنجره‌آبی‌پوشان‌خواهدداد. یا پنجره رو بازی میکنه یا بسته میمونه تا نقل‌وانتقالات زمستون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/26763" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26761">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzfLErNOGS93aEHwdLuh8L37TZF89CGc9X2vczmvaynGlioOhbM9M7LANcFaBnf3Mu_N2MNJzEsFa2GgsChda2-QQdWlQY6rucFc6xzt4nfdzrhe2jW2ocRg89qhxz8Jwz3Z2ij-cV3tjF10t2QqPLFqEmJ2oOxth784asJNHfPaydCPXVx35r4k7_HV8p_LpVxwUYvOgagfuVuWBrtMvk0GEl5tFGMU7Yphh6qe49j5ZByEb6JwW00TMcVNQVHmoHFsd58T6YV-5xdD0iVdbGjI-Em_4v4gmVbh6q3qID-u89KHrQQCw61J76RZ9xRyy5IVomCm5y_uIkHr2H_I5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
دنی‌ولبک مهاجم35ساله سابق آرسنال با عقد قرار داد دوساله رسما به‌چلسی پیوست و شاگرد ژابی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/26761" target="_blank">📅 18:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26760">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mnb6Gxx3JVum60zVFvTjqiq70crjRrpEsq3Zv6NRn3FB9fi-I7f7Yw3jO_aup56umclhWVzPXXLqRTkoi0TIM0EawQ5131dMMDXfSVNrUwuh7Eq9awIrVamygVPhERnMxcD2l0xgS2loSYmmVTrP7iDPVSX5uCvz1yHn13i5LKRLhbEYZcfuScgZwBzhtQBe_taeL72ItGICfHk754KeDPctyGSfthKFnEQatAJUx6Hp4IPNo52lxSg05pxSkiRT5oH9chLhq0jS0kKRjmhfgqXajnvt1kRsfNpqEMyGixxVwuHYCvTUc5vjr72vzjlx1Pc765hSWqO33rLckVoHFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
امکان نداره هواداران رئال مادرید این ویدیو کوتاه رو ببینند و بغض نکنند؛ هایلایتی خاطره انگیز و دیدنی از مثلث وحشتناک BBC در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/26760" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26759">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcTZxAP5Xh4wyHQjos2URJARMyfYvyKkIOROyxrSQX1OB5zQwGBsV_wguccngDpXeSKMtigf28a5olXwWRv_eX_dIjK_jvSM-xpDf63sWDfCLojiIUyUoXoc44SdYegq44_wQsT26tkEG_Cu0smLdlYKoakg23i3hqZRWNbmCl55Z6wabDtNeUYbPkZYKUDxlUu57Cto7gaaK6_SlVjnvmEiG44V-_8pphfgQez7XPUxeYnSMn-D1qyoZW9A77XfKg5zhhWbd9iTkwR2ZYaN4p2YIYBkuk17YgNfFZA-SX4U8Irr8QVZmFBwZQbuzKBvgmutI2AkutLzTwKdaHrqTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇪🇸
🇪🇸
باشگاه رئال مادرید بعداز توافق کامل با رودری کاپیتان تیم ملی اسپانیا؛ ساعاتی قبل اولین پیشنهاد خود را به باشگاه منچسترسیتی ارائه کرد. انتظار میرود که سران سیتی آفر رو قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/26759" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26758">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnxBCZXOK1pnY2omkBJW5vH2ZeidUjsAhHLV8LBrgon3kLWvFhHzpXHdWYqxeKHX6KqJSUAPvOS7uXCNadoo6lO2Nwng6kG_9ui_68aeBLzLB6bw2-z4f1cL0ekkhxL7pwTOlidNsi1OhaDBAilsiNqigxpI7qBLAbNOqnM5bBJRt_9Obb7Kq5VqCImxz_cyO0va19Dd8-XzLunR9IE0cyPn-VInO6bYan1aQ9tMVGMcQ5RQRfq6yYR7UziUHZlWJiZQd4lo7OZWLMZ-7ttnJ9syTf1j9od5JNWySh-BW-56d3l4sMOl9l8A2jESSAb6FudZkDJmreaz0VAByOG-zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه همیشگی شما
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/26758" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26756">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QOSmWYz-tLMVaZRiZIPHoVKdzOMPaYpWjhqm0HTbFABpTpT2dPpHieHeWId1blBq8lMUl35x4w0vJ7FvONi0K0ISzyyFN6XmpgouJ03poFpCjfbww_474ocyyNL3LVT9R4xaZxBWwyXMmoKY57MlgxB634TJ_o4rtPJnSQvq90VqM2T7jm7Ba63pgLCgjh_byreEd7CTO9P_MHSy5RBTX0nCqgDUPoYsZTw_5s_ojyQ80imj9Hx20Z3Q_eV-dEQKJvxKi3WB4B9hMS_zqEEuwOAb4ey5Y4M2zWsl2NM0ssmR3BEIAkr07D93B5i3w5ITatp1P8j71u-NlY8HSuzi5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7YMMUfzTu2g5fvskE50DGJKUsnIOBmwpsTXxS0nmcPD7NR1wnTrZOFa5CQPp148I8Q4C-ruV6Dx9DsDso2z5btPmFoDq7rr3v_89AGgmOdHd5tMu55EBtHdNA2GBHBfhR36Da0ePwBzfo4u0NyT9eA8GZ32jgHo63rhYfWI_VsT10LprbEqtxbSZ0Dv0GmFpFueducmcixouerxJfMqdMXlsZNXtrJnyB7yZ_bOaBe5iTB5lIEmS6CcpEnBtDj3ryaJHxKAnbI1WebnYI8_yCpDfuNj-rfVLpl0ZMiYj3mESOszs-YTS6C5U6TbuqHZziwzm3jEpixopOnu9neuZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترکیب‌منتخب‌ستاره‌هایی که تا به امروز به هیچ باشگاهی قرارداد نبسته‌اند و بازیکن آزاد هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/26756" target="_blank">📅 17:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26755">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03d21e0c25.mp4?token=IE1kK04tUn2gm9jJKidvaeSWSSxNaCdVMtNOiHxhY8Ct3vaF_kzkHxn8kXCPh13YDf2YoIPI_m0YE9XhNSW2t6ArkSAbWsRymZa5sTUsmJ5uR9ppVMrXPoQIzhaUVWmNdS0h5eC-HGM-W3yrDayRa9XjZE1qBuzvOC0fB7OiHd_2KlYCzMZhYmjRXoPN8H86Datuo_t4zFA2SxNtIcXwYR7A19pGmugUG2QV9hf7gEyrStoEcPiQKCE-ePj7MiyVGq7i5jRmJpfsTnORfHfpp602cY4FvuNvA5LaxKhRkovgUYK_JTJmyVUIT5LyKtA9f5boTr_a1gVGtiHLJl3yEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03d21e0c25.mp4?token=IE1kK04tUn2gm9jJKidvaeSWSSxNaCdVMtNOiHxhY8Ct3vaF_kzkHxn8kXCPh13YDf2YoIPI_m0YE9XhNSW2t6ArkSAbWsRymZa5sTUsmJ5uR9ppVMrXPoQIzhaUVWmNdS0h5eC-HGM-W3yrDayRa9XjZE1qBuzvOC0fB7OiHd_2KlYCzMZhYmjRXoPN8H86Datuo_t4zFA2SxNtIcXwYR7A19pGmugUG2QV9hf7gEyrStoEcPiQKCE-ePj7MiyVGq7i5jRmJpfsTnORfHfpp602cY4FvuNvA5LaxKhRkovgUYK_JTJmyVUIT5LyKtA9f5boTr_a1gVGtiHLJl3yEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه‌ویدیو از الان‌وقبل یان‌کولر ستاره‌سابق تیم‌ملی چک و باشگاه‌دورتموندببینید؛فکرکنم کمتر کسی پیدا بشه که بازی‌های این فوق ستاره یادش مونده باشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/26755" target="_blank">📅 16:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26754">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3WjxLUR8ANyWMrTsGW5sqhcwsbcCJ1veo3yYbk3zCyxcr3FxDOAaZvab1-jmqvW1CQW4iqHZQIbxY68u17pCZw5iSHOusdEmYISOG3qBkfNWDit0tomdkogszFN3bN-GvodSZ3uNZtVJ9K1JDMVBXRayIuvLMzszBQqyZL_N4MbrYo0_0p3iI6sdGMEJ-kbTJKUQG2F8Uo_AIE6hBOVnQo58v3lg11PR1ws45OuQ0_VR54EpnryV_vCQnF4N1tYw1trQNe8kx0JxeG4IrCZfKq3UmchZB9Eiu5wLREGBRC-8e80jv3_tcuRZPq8p1gBOED_N8fxOc7PYHUycst0gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/26754" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26753">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇪🇸
👤
امکان نداره هواداران رئال مادرید این ویدیو کوتاه رو ببینند و بغض نکنند؛ هایلایتی خاطره انگیز و دیدنی از مثلث وحشتناک BBC در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/26753" target="_blank">📅 15:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26752">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BneAuHU406W6H8LXHJ2fEXrO39dP-7yqVcCvr9NUiuSQ4rXIqyh8fpYAiB2YF6f-ndj8KITWKjG-_9tlbl8g2BLn8m-jI5La9YqKAYQwVZ3m2HBMvh_v-gEEO0pjoct30NWusRb69SkyeWLBvKgUMShrTwRfgMAyl373JS7KGcfGHKYoB8rYMxyuXDVA5KHUZjg0L34Rc0Mbnb1b5reGwxWYpKxgd64b6CIxU_nu5yKNbpI_8eHtN_CFhqdM8TM-ZhTCjH5m6osbpiijawifC05xhYlw_2slbhFoK3dXmPK2PUiG46UiqCZYNyFdXULmGgTbCEO42xJZe0vDM-Z07g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/26752" target="_blank">📅 15:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26751">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c3851e11.mp4?token=e4Nqm2d9hHLsKJRblboK_64MMMGeLMJXGXfBpiJOyZhUpzLioe2Asfkx6ceBqOn9zJ6pauoNvCXbkOep2wD-tAI1hYrO2wj7lwRdRWZwQZvQgzV2P5Wpxoe-BCyPE2ftsrWzOXAq-Zm9ziwmSpfWoKRvQEcOG1_VsYxj_JsxZSn2Vrgfx0pcW06e7ovpNMY36RlrWZ23Ef0AO079d6TDGZDcBKyiMVxiSfhwrzBlQb6_BHgSFC9Xlnj5qn5j2UiopwKPTowh1IYIAXmbrzzNfuwbsSPJTesmCzhf8GNnCY-QDouBrSJGUnqUyZ2-eXl9ZikRlzQola-lQaVuD3bQkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c3851e11.mp4?token=e4Nqm2d9hHLsKJRblboK_64MMMGeLMJXGXfBpiJOyZhUpzLioe2Asfkx6ceBqOn9zJ6pauoNvCXbkOep2wD-tAI1hYrO2wj7lwRdRWZwQZvQgzV2P5Wpxoe-BCyPE2ftsrWzOXAq-Zm9ziwmSpfWoKRvQEcOG1_VsYxj_JsxZSn2Vrgfx0pcW06e7ovpNMY36RlrWZ23Ef0AO079d6TDGZDcBKyiMVxiSfhwrzBlQb6_BHgSFC9Xlnj5qn5j2UiopwKPTowh1IYIAXmbrzzNfuwbsSPJTesmCzhf8GNnCY-QDouBrSJGUnqUyZ2-eXl9ZikRlzQola-lQaVuD3bQkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تعدادی‌از سوپرگل‌های تماشایی سرخیو آگوئرو در دوران حضورش درتیم منچسترسیتی؛ آگوئرو در اوج فوتبالش به توصیه پزشکان فوتبال رو کنار گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/26751" target="_blank">📅 15:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26750">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_Ho4vjv9vB3TjASE8vHv9YHgIXZ0F1yYCnb-mB-zGdW_pFPhfzeV9xrsEXa7X_Fo1nAeog_ErVFTIhr3tVk09J8L9_7yEekUFoWv1fWiKj8_4lNj3kIG-CpUl1U_o3UX8ai84iQqivOQMV1LRwxFTXvfqcRSgX1ePdvxTOdYQqlZWg8RWSrNGOXPTK3ketYIDjRa0j9TE23kjgRBZ1TdMwpw3cUCiQcNJEd1iXqut3vvaxOdqfG_ZywOgZHK8ewbk9Yb-LT5RIkKGXtbJxsOEfgQTkDrQIHfw_CpJjacfrSWEYMyjLNhe3tXNdNTRilhCA4OztcxFxZvvPmaxo6GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های برزیلی مدعی‌شده‌اند که نیمار جونیور ستاره 34 ساله سابق بارسلونا تصمیم گرفته که برای همیشه از دنیای‌فوتبال خداحافظی‌کنه اما نزدیکانش میخوان او رو از این تصمیم عجیب منصرف کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/26750" target="_blank">📅 14:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26749">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aknC9ltuYi57cb0QG8CX0uhpd6aP_UTdz5baGB7YK2a7ahVgU2uQaPH0GzS0hxJ0U9zbefq12iu4tzgh1uDa8UfVm33c-Q17LodR4ayuBDkiDrytmeUbmGcdnPuk6__pnKdUQ2JiQ2wmZWHHCC0FnYcm9e_vp8a2SC83iK5lAleXYicUm7XbM-O2tqy4xJTQjFHZg8BVV3RqyqSv3Yac0z5pCbijr-voN75nqxgqPCusRwJwKt70S0x2GuUrnSN8xA6chACFqD4rZ2bHM84Or4hl874fSrN7LzTQXOoJNo8iw96R1k8xxNChBRC7OuxOtXaHTyT86BUg4XP5DpTGmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی روزگذشته‌پرشیانا به عنوان اولین رسانه؛ محمدرضا اخباری با عقد قرار دادی دو ساله رسما به باشگاه گل گهر سیرجان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/26749" target="_blank">📅 14:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26747">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jx07aEeIkAoCI58EOHj85eZF7h8S8-yIj6rTUldIs0P8fjmI9bbieUryERUkZa5qwfwkLHM6UltnCBQ7cx6LgoUF-k1h1Ur5woSuXPWsOeRulNJpUZJwsjo5O1I-6SKMUj0ZM3wkNyezmOsAtGux3TUu6FM86b9HoNslBLRQKXdAYMKlkIAaEGF8jQfIB0E8ROgzfWeSUID_rW2I5rUOSfvDWzjww7FUYTuGWsOoNj1fK2-QJ50gg53qpMjk_o6tIkimLIWFBeEmHowO9S23d_5kQR3ITNe8rfnKbD4gwbS0_jdh7yAawly1x1izASmDdYyZVT-jO6-9UzrecgohVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BN8F_N73Z4fq0wfB7HlRucDm9MoR_m2ehFczdSUCCGLWW8QNcF3CxyqRdZo9MyeNlWT3GpVXncqa1VK5U4L98XxP5DRZmR_j6XvgdjkqqBgU0By0SyJgoQW_DiQN2X9XuD8SsD36fjNkOADfqrQT2sgA4FzkCdxr5d16Z0WpwRmPZcJFQfy9Mmf2Sv5IKLx2YMaZpqff1QU84mGaVg2HEOBbN-FupxIveWpoXobDSiDEGgBkP_wsRYfrCln1ijsdFikOz5Z89ZyxEG8ufN1pN5JzfLU7lB83qDUkLfL4xtIEQnNa-wz0gLM4j3fdiU5Ga3gfNMX4RLk0Wx5tgAKpqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوست‌دخترنیکوویلیامز که‌درمراسم‌قهرمانی اسپانیا حضور داشت جدیدا نیکو رو با یه دختره روی قایق تفریحی دیده و تو شبکه‌های اجتماعی آنفالوش کرد و بعد از چند سال با او کات کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/26747" target="_blank">📅 13:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26746">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhCjIDt9twmOcctLL8h_dAM6V2CSRtiKHkiyOqgogge_AUMu2hk7a40bRZjZ0kVovsZJSJwMcYBZKuXNslWuDKg6HCt-jPak7v7Fk2eKB4RcquPYvLMeHr1XfQT4ZVkipR0gfulb-gGu1gmHzTzHHyncXvOJhDqm06-UMZ9d547NWKKtu-gd9IXhTvY2Kg8l-pW0_XYAY4BoFwYaprSPiHS6dCx2k5fc9RI3e4qoELfArJvvadH3xIw-5Q5Sd3WRsmLVnsRRwOmKyH0OyXmM6VG0LrcMhlCsxVaHcouiNhP7yE9q7UH1v7loWnb6BOCZGO6ZcM5lMPes-GCoC-of6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد لامین یامال، وینیسیوس جونیور و یان دیومانده در فصل گذشته لالیگا و بوندسلیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26746" target="_blank">📅 13:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26745">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/389ac26246.mp4?token=ll5FOOVFb1ETFkTaIWJk8L2wCvSDLaxuXVXNsYxMdTmCzyf3dG_yhPNvrRj59aqwXlu_fJTw7FdffVf9pdaPQx_Jb5XH_BRLI58wSQV-9etQP1r2m7Tb9IuitdeB1_xLE-He3pFty7zeD-_tj9xdqFHrOP8FVRdt-7ghAbAD1fd1OJ-Cks9RKlayMTrpwN_mYUkQwkMVWzyM2tel4xRRPxuYlcwKQYo51QkLXzjnD6TsywXMIhIbI2jipGTH9iBbLxLDjTO0Xhc1C4GlLEXYyJWssPAZKjTwqd8VeXQsyXQiprDk4X-_5X8qTj8zcDIa3y1yXOE1dji2QVlGKvPurg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/389ac26246.mp4?token=ll5FOOVFb1ETFkTaIWJk8L2wCvSDLaxuXVXNsYxMdTmCzyf3dG_yhPNvrRj59aqwXlu_fJTw7FdffVf9pdaPQx_Jb5XH_BRLI58wSQV-9etQP1r2m7Tb9IuitdeB1_xLE-He3pFty7zeD-_tj9xdqFHrOP8FVRdt-7ghAbAD1fd1OJ-Cks9RKlayMTrpwN_mYUkQwkMVWzyM2tel4xRRPxuYlcwKQYo51QkLXzjnD6TsywXMIhIbI2jipGTH9iBbLxLDjTO0Xhc1C4GlLEXYyJWssPAZKjTwqd8VeXQsyXQiprDk4X-_5X8qTj8zcDIa3y1yXOE1dji2QVlGKvPurg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛ درصورتی که پنجره استقلال امروز و فردا باز شود مهدی گودرزی، محمد جواد حسین نژاد، محمد محبی و یک مهاجم هدف اصلی‌ترین گزینه‌های آبی‌‌پوشان هستند و قصد ندارند بازیکنان پر شماری رو به خدمت بگیرند.
❌
باشگاه استقلال درکنار این‌ بازیکنان…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/26745" target="_blank">📅 13:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26744">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EH3BJGSWqYoutgI9r8-Otc4BI9IMj6rddID-Blw1cb6rj2ygSQJoxII5wxw2byz9mEzlhBwt1JSq8VvgBujvZ4lGi6UA8uQ0PwCx2EukAnL1ZyqJb0qWSoyNeFp-Y37jq2657BZsIP1odv5HjcyLXad67jjAkOMKxmFjiWG3BoZtlUx82Q4UjhQ8kcLQJ_tXXRh04V9RG358aiW5nRu2I3sjHLgogBS6gFh9k5F5LgHFhrmssZZSY8TyeXMNakeQrwmfvl5XTnmmz8nRovMoTgsKDVoGQt-NsNeLuXe3A9osWkTDMPG0JlBKg-0s5up_EZlM44-gmIB4DuQ45YRbnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رسانه‌های فرانسوی: رودری پیشنهاد باشگاه پاریسن ژرمن رو ردکرده و گفته هدفش تنها پیوستن به‌رئال‌مادریده. او به‌سران منچسترسیتی فشار میاره تا با انتقالش به باشگاه رئال مادرید موافقت کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26744" target="_blank">📅 12:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26743">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juPhyuGkucOn07p6S4xROgtIRoHs3_r1DiSgP_UXtPteZTFmT1YVbAYHl5TKSR5HlzlTj5Mwt4OXPKvtoOVWqKPbJJb8lijDiQdhKS5CMx7katpI17GxljxKrpqmWQtuIwpgAHJpUUTjbV0nrfrSilm1zGgnJky2Cl2K9DlN13sWUGya-1jPxeA_H-kpXKy63CKmboauthgCOiiR9muAqIn3wWaYbffgkXytxi6BQkFEvYmlMrIYxd1kxaM3le4dL-uTZG4zI-9s3X8m6maEy6MyBFB2dHZEV6y5sFDPaX-jC-q18HLdCXINyZw-HLo5hvoYCMeLE0ZMYCwqLsL5Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛ درصورتی که پنجره استقلال امروز و فردا باز شود مهدی گودرزی، محمد جواد حسین نژاد، محمد محبی و یک مهاجم هدف اصلی‌ترین گزینه‌های آبی‌‌پوشان هستند و قصد ندارند بازیکنان پر شماری رو به خدمت بگیرند.
❌
باشگاه استقلال درکنار این‌ بازیکنان…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26743" target="_blank">📅 12:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26742">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2cc2d700a.mp4?token=g3DwGNyBM4JRmL5XiwWrLndyWjELxINbJ6t8Y3b4Uy4f7mn8YxOYBO_qxnK-rblrv4bnSdwYT-VFf7KK3WoYduEHg7ZUJF2n7dRxzzhSLOomudOXNbIlZkGeUMsM2CsRozsoI5_U3WC74DNhjINOyC0wnnMY_qrEcztlbBIREF9w9f9EcDFd10ag2GcjyzFL2dhDi2G883ioznVTZuV3ySrnvt5b4zujuDr3tnz0SduWbwN26zf386BwgtOZYHJIE2lNqK-jyj2tbglGgaltmhFcJ351OqjjTJhSAW-mNIbQrWSqulcSfKA6Gvo7eYo4Zz6IVBIYnHMn9ZmjB5tnp6Z7g3la3uadKUXOJDCfGiEkzkGzOINp31W9JtUrle5P9u51HlICjmWAZ1voh1fYE3Cgoo59dzDMDKON0D-y-yufTZrOfWBtXjyDNIJn9CtOOeJeULZqgwNjXwRFvOl6h4a_nWvRIbljfbU7M0sojT6oxUTHktaKvclFU3z-iDf43HNYnh1pUwsn2GMNuwkaysR90sDllKqurNRvzVOsABxe70AwTMl_gBeiA5wPESv4ilpSOst__G63dCP6v4vc7z94vPAByNUsO2EfvKPjYJYv9KIpL7TQllb3QYvf8Jrg625I6ImMGwEmcDekbkczu4Pgperm-Lcnicxv58w7mzE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2cc2d700a.mp4?token=g3DwGNyBM4JRmL5XiwWrLndyWjELxINbJ6t8Y3b4Uy4f7mn8YxOYBO_qxnK-rblrv4bnSdwYT-VFf7KK3WoYduEHg7ZUJF2n7dRxzzhSLOomudOXNbIlZkGeUMsM2CsRozsoI5_U3WC74DNhjINOyC0wnnMY_qrEcztlbBIREF9w9f9EcDFd10ag2GcjyzFL2dhDi2G883ioznVTZuV3ySrnvt5b4zujuDr3tnz0SduWbwN26zf386BwgtOZYHJIE2lNqK-jyj2tbglGgaltmhFcJ351OqjjTJhSAW-mNIbQrWSqulcSfKA6Gvo7eYo4Zz6IVBIYnHMn9ZmjB5tnp6Z7g3la3uadKUXOJDCfGiEkzkGzOINp31W9JtUrle5P9u51HlICjmWAZ1voh1fYE3Cgoo59dzDMDKON0D-y-yufTZrOfWBtXjyDNIJn9CtOOeJeULZqgwNjXwRFvOl6h4a_nWvRIbljfbU7M0sojT6oxUTHktaKvclFU3z-iDf43HNYnh1pUwsn2GMNuwkaysR90sDllKqurNRvzVOsABxe70AwTMl_gBeiA5wPESv4ilpSOst__G63dCP6v4vc7z94vPAByNUsO2EfvKPjYJYv9KIpL7TQllb3QYvf8Jrg625I6ImMGwEmcDekbkczu4Pgperm-Lcnicxv58w7mzE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
پارتنر گابریل مارتینلی ستاره تیم ملی برزیل هستند که پزشک هستند و گفته دوست داره از بین برزیل و پرتغال یکیشون قهرمان جام جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26742" target="_blank">📅 11:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26741">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYqlXyBNhFmdq_oJpiHJz-54EWUZE0fSnZMFg-mKoN4iljeIO-eV7oNIia7bNjkAdqakEJxX4KR-8IYodTtWGr-BPYmhgHAkG0PAPXFJcl-G4V6BSJ8zEniORWT4de15shGfuShCKsCfeleWaXHCIgbl-onpfgPBmme9L2Wvb6ebnmHStccZtn1s0wL9DJ9Pnwm-_nhR05XpnTGw7Bq5nqJ8_jMP7vZ27GL1zDU35FerZrgTBIN5yJwQIXDbA42LENGSW3XmxOEeEg3uO5s1k3Qrrh64EAKFz4RcEamoBUlfqnLz3ZmvxHflq9zBpIy7zecUsdDpiJctIvlLsG8-mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیررسانه‌ای‌تیم‌پرسپولیس: اگه کسری طاهری و دانیال ایری رو‌جذب‌میکردیم بعد از هر بازی رقبا از ما شکایت‌ میکردند و ما هم‌ قید جذب این دو رو زدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26741" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26740">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gICxKefYIbtW0pQYauMQ1TkOhnm1jAP_--iO8r19NzHk1KOtyoXLYAQpmrNVqf03Vp-22p7Kifpy1MHmaawU3oX-DwxQSXpz8waz1bSzCUCjB08whVvZ6lcKWZgist5s_poD5fyI80slDqNaeK4WA5lokjuYQvcWBLF49IMUfk2dwO2LedQpI0q9Fao2SMV7D8tWToeQbBhFqly1QDMBcFsgpJpdRQILLoB7iOgAtzDZw7GPF5Kr2kcwZcdgA6HMko7leC13q6kelXplY4ST-S5D9OJuACFKVrdBovKKYVR9E9oLkhC2ZUh-N282dvkGK9mZiZNCCMDSGO3CnnSvJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26740" target="_blank">📅 11:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26739">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98e9665500.mp4?token=blsV_WXyELhwBhwdYKmnsG8cjBbdF9VV4jsY2YZxBC9R3r7Eu5jbTlKF9g0peATt2cOZR7WUa17fcAu_TKyZtdXXdErBK_OTyW16QgEkEUdlAWTpPhjXqmpj7MebhyfsCLz517WRRqgE2QUGrzVcyvaPLc-5vTDwPg9nH1XShxM47heqGTWH3W3NHR508Esn4qE_gcYaX1ZTjLlAmOIG05ze8x2gulDuLdKkxXjMDxXrS4ZH0SpYJzGwL5mYnXm_w3YHDNgyy2DkOpkcAQPvM_pBUKTPHF76r3A8i5gaigY5tvcBpELGD27PFD1IeUca-Wi9yvOvKzoySGEFYcwdkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98e9665500.mp4?token=blsV_WXyELhwBhwdYKmnsG8cjBbdF9VV4jsY2YZxBC9R3r7Eu5jbTlKF9g0peATt2cOZR7WUa17fcAu_TKyZtdXXdErBK_OTyW16QgEkEUdlAWTpPhjXqmpj7MebhyfsCLz517WRRqgE2QUGrzVcyvaPLc-5vTDwPg9nH1XShxM47heqGTWH3W3NHR508Esn4qE_gcYaX1ZTjLlAmOIG05ze8x2gulDuLdKkxXjMDxXrS4ZH0SpYJzGwL5mYnXm_w3YHDNgyy2DkOpkcAQPvM_pBUKTPHF76r3A8i5gaigY5tvcBpELGD27PFD1IeUca-Wi9yvOvKzoySGEFYcwdkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق پیگیری‌های پرشیانا؛ بانک شهر هیچ مبلغی به حساب باشگاه‌نساجی‌مازندران تا این لحظه که این خبر رو اعلام میکنیم واریز نکرده و باشگاه نساجی و مدیرعاملش فشرده در حال مذاکرات نهایی با باشگاه استقلال تهران هستند. علی تاجرنیا و هلدینگ اماده پرداخت پول رضایت نامه…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26739" target="_blank">📅 10:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26738">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96f6912da5.mp4?token=tmxiiD4tybqufyVNTrtxZy5jGWp1E78FyJqaDVJiImhlLL1pUewUDHSsDMfJ3WKy3OoumphXWNWwOPqWpHV57ypc8Q7QIM1xF34uNQFplENgJEczY14dsmt69jxe0Dh3HG79tcmPR670oVMcQsJo21Bc49vssJwGgjTzkrmVHkuMT2RJL9HgyPMWCFrjG8FjvkCjpflhjw-YBlRL_wfhKva6FJSpCRu0cQ_GTY1xXjir3HwGTRN_L9MMpI6QlJfHhyxHXfSGLJi_DINWnTE22O7HOKYoMOuNQGNZ5XGm9Hff1Ww7t5Vb1vz7fxMK8JD5jHN84gSEAv8gIxKHWFmZlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96f6912da5.mp4?token=tmxiiD4tybqufyVNTrtxZy5jGWp1E78FyJqaDVJiImhlLL1pUewUDHSsDMfJ3WKy3OoumphXWNWwOPqWpHV57ypc8Q7QIM1xF34uNQFplENgJEczY14dsmt69jxe0Dh3HG79tcmPR670oVMcQsJo21Bc49vssJwGgjTzkrmVHkuMT2RJL9HgyPMWCFrjG8FjvkCjpflhjw-YBlRL_wfhKva6FJSpCRu0cQ_GTY1xXjir3HwGTRN_L9MMpI6QlJfHhyxHXfSGLJi_DINWnTE22O7HOKYoMOuNQGNZ5XGm9Hff1Ww7t5Vb1vz7fxMK8JD5jHN84gSEAv8gIxKHWFmZlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شوخی‌های بامزه زنده یاد اکبر عبدی با همسرش درآخرین گفتگویی که با رسانه‌ها داشت: کسی به من زن نمی‌داد با دختر دایی ۱۴ ساله ام ازدواج کردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26738" target="_blank">📅 10:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26737">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6A-dc0G77Z3YzAIYcFVjhnqAby_RIG-RHw5oRwORuxGNqwPbj_ZMyCVXbcYoaOMZTPGpgi1sTWTjdmYwWhyro7SP3TI1RBby6KqqOftd0NphP6MUAKLwPlkZElREAM56XJ1RVOLZW2FVZYE5wZlgE8r3_tCjmgACR6UgRHm4VRGvkwswJ5j-FeZcdeqEzHJEFS11v-moxwk-V3C8sNLlt_66-1zOw8l1pippMqPaoUdN94CLP3blS37Rzuovk0n3f2pYcnsugHqfuGAIzIeJci_6MfLoUGidUMK3PA7hhhw6EK4S192ax2kePGbv3TEY2IVW7whJkhO3zf5gHYLrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26737" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26736">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfUmFK64sDuwksQnKD9yq91YOTK1X8Su5JWMSvIdCAFAmh4AXj0Tlj-BjCcoRkjNg3Ht11USFnqfhQrHK_nOouQT-UwOt1W9JqEuM4tVUn8BOPCkIO2Wn5ajrKnly_sMwdmblh-B6Kjdlz8Oj25YSSqSpKPwgHBSkUYM2m3y8udWxViL9Zh9ULf3Mhmqqr9GZUb7fkRO5lPqQpSsDD2KcIkLkWLFxgDBfRsuPBorZP_vD1hYtLZXwAtg77mPoWzazcK1sT2I2DN5W5IjGBku6w7KRCHpavVWimUrDWvXjpZXdYywBqy3Qp7lXpPZzJQTPau4mHF5LsMyMxOQwKmEwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
برخلاف شایعات مطرح شده؛ همانطور که گفتیم کادر فنی استقلال خواستار تمدید قرارداد جلال الدین ماشاریپوف شده و از مدیریت خواسته که قرارداد ستاره ازبکستانی آبی‌ها رو تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26736" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26735">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrgNRlRss1mIAtMgmEVPwG4ANe1aVHdOVWCvTqhp9fsKKMS6YAIBTt4laKvjpZeWKednQGFzvKsX7uf9JWhbY09vB_7tr0Pm0eny0J5HUfWwZnNzobrCBWTHO8m3kuoThBR2s0QGqiAs9kPw6iXdqwYTqPybkeBo9itQt1qT_WKY3sAFrLD6wgE6OXNpudCyyQJxSkc7qcvCeOw1ZH7P05skmskgyFHFW6c466rtEmRuWiEYXA-omx6yRoTgy2x-NWqWorr8-ifq3m0Sm9g2-GfAEiaYpBTMKOPlh3zbcfA54nCqvgjMqmxa-e8BRldOesDfvt8DdLvBYg-KM60MPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
توام میخوای به راحتی از فوتبال و باقی ورزش ها دلاری کسب درآمد کنی؟!
⭕️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
🔥
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
🔗
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26735" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26734">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oshNibq_rBML009NgHjFa1_9TeABco3rUOJy_doIm2aXx0qj37puZSbLq4z8Z7UGq5N3noQcegCdUt3OC5tH-oQWmtlwvIesNwpyJcn2UGjSmlexi2A5TNwJlxEtsQ9V9GMt6YGwehtxIbBx1TVKy4PBcalyvWdemOQ54iUSuxaASIMeQXrGk8ZTvO9N_zvyyPjW2-2nFso1hK0Eoj-lt6O5iTas2RmVjj4_hAhEhs5KeTh3HXZ4W9ZvxXW0Rf3pPSTAemVdyIRGlBSlOlwZMHKEgzJIE5cQXsKdqRcHdECY3noleiS9jCWxsEiN_Tse58PiuU-Ymz9RiY_X5lF6aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛ ایجنت ایرانی نزدیک به‌ عثمان‌ اندونگ به مهدی‌تارتار سرمربی تیم پرسپولیس گفته که اندونگ از سپاهان‌آفر دریافت کرده اما اگه او بخواد باپرداخت 600 هزار دلار میتواند رضایت نامه این بازیکن رو بگیرد و او رو به پرسپولیس بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26734" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26733">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59d676a359.mp4?token=ipAIEFn7B3UGiY14UibzVauvkqqkwV_7i6qB7BEdepDx4ntqCK8MTsaJjDdh0G7W4g-zpd3wVEMYvuSxo61xwSU7BLnQYV9yb5VyltitmBz0oGV4ZlNhwbixCxAw1QM89NmxbQmsgaosvfKZ2GSbZx8S_ooKmpJ11Rip1iJQCyWUe93YLT5H-Q91V6_O15EjTloDw-Fk_Yu3xjo1C0T3eoPZmiMeElFN7yVyAmo6WKxP4YcaTiekkC5P_pV5KI-csAsK6Az6nukH6fezkCxgghYLpf5SRtlGlFaTMea9oE3ByXE-loeQzeh2gugLWRCX9IoVUD5fS4sZ6sHci-kajw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59d676a359.mp4?token=ipAIEFn7B3UGiY14UibzVauvkqqkwV_7i6qB7BEdepDx4ntqCK8MTsaJjDdh0G7W4g-zpd3wVEMYvuSxo61xwSU7BLnQYV9yb5VyltitmBz0oGV4ZlNhwbixCxAw1QM89NmxbQmsgaosvfKZ2GSbZx8S_ooKmpJ11Rip1iJQCyWUe93YLT5H-Q91V6_O15EjTloDw-Fk_Yu3xjo1C0T3eoPZmiMeElFN7yVyAmo6WKxP4YcaTiekkC5P_pV5KI-csAsK6Az6nukH6fezkCxgghYLpf5SRtlGlFaTMea9oE3ByXE-loeQzeh2gugLWRCX9IoVUD5fS4sZ6sHci-kajw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
تیم فوتبال چلسی تو بازی دوستانه امروز 3 - 2 از حریف عقب‌ افتاد ژابی هم کل تیمو کشید بیرون و بعد ترکیب اصلی گذاشت تا بتونن کامبک بزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26733" target="_blank">📅 09:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26731">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01bf39426f.mp4?token=DroMWrAvOMgwqVPiexvEHl3-FafxtXBVCynaIki8nWmiK3Y4xJPrxYJ21CmyGbE3b5MPxYzud32YM6kvKMQdxCzyDTK0FcRuUwP8t2kFlwRswcB0hBp3S0EEYphjL_dtDCUZQ9giTjXfuIc9YKfm30X40BRXJihfdXMz3IZgZaSy6s2GJUeKDAlkCMPkkf1a2JYQrcNorloCE4ahjL9ljJDs1vMOd7m70Ouh7Rds_wlBKvIwr6MTIj6JBebM6dTLVxpSHsr3obd0hb0Z8aer8NWkZJcsE-5HHl3Jtz0w22g-33uN3Kp0ExTq1h_SXcRdwMgPpiFVF4BRjYUcmqIMhgbduXXe3zF9RJOmMoYf4Kyb_fLwKO3imukodMdUEzRMoBQoi29TZd-lDhU8BHJ6EpUv8vJW8yaiDe5ro_dU4Hjq2S7Ai6gRL3sqZ4OISi-Hv90RxhIDpc44poFWWZsKdho9Y-kodolVLMUnEGUwXHa4u0DhLB634PhOCBg-D3hw6ojZ-h6kS17IeJHVqPtPxnYEcluqNmqdklU7cYl0boUb80MybeNc6nXff1Kae_AVgOilh9YhKby6MbVkk6y14PK308Sfrfb1YgIwaQWblalrZk45kFSTBfzrfGqgvBggSUBSN-RN_Ji96kLNDkGPIy8JEU9bpYtRuJAZ3eiyYdY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01bf39426f.mp4?token=DroMWrAvOMgwqVPiexvEHl3-FafxtXBVCynaIki8nWmiK3Y4xJPrxYJ21CmyGbE3b5MPxYzud32YM6kvKMQdxCzyDTK0FcRuUwP8t2kFlwRswcB0hBp3S0EEYphjL_dtDCUZQ9giTjXfuIc9YKfm30X40BRXJihfdXMz3IZgZaSy6s2GJUeKDAlkCMPkkf1a2JYQrcNorloCE4ahjL9ljJDs1vMOd7m70Ouh7Rds_wlBKvIwr6MTIj6JBebM6dTLVxpSHsr3obd0hb0Z8aer8NWkZJcsE-5HHl3Jtz0w22g-33uN3Kp0ExTq1h_SXcRdwMgPpiFVF4BRjYUcmqIMhgbduXXe3zF9RJOmMoYf4Kyb_fLwKO3imukodMdUEzRMoBQoi29TZd-lDhU8BHJ6EpUv8vJW8yaiDe5ro_dU4Hjq2S7Ai6gRL3sqZ4OISi-Hv90RxhIDpc44poFWWZsKdho9Y-kodolVLMUnEGUwXHa4u0DhLB634PhOCBg-D3hw6ojZ-h6kS17IeJHVqPtPxnYEcluqNmqdklU7cYl0boUb80MybeNc6nXff1Kae_AVgOilh9YhKby6MbVkk6y14PK308Sfrfb1YgIwaQWblalrZk45kFSTBfzrfGqgvBggSUBSN-RN_Ji96kLNDkGPIy8JEU9bpYtRuJAZ3eiyYdY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علاقه بسیار شدید غزاله اکرمی بازیگر سینما و تلویزیون به مهاجم سابق استقلال: غلامرضا عنایتی ستاره سابق استقلال کراش دوران نوجوانی‌ام بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26731" target="_blank">📅 09:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26730">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1VCF0D89oZH9Z0rOs9aNXj0uSx9RBcWj6E0GiHdkJFyedFSrf3qEOOjT98ft75G9BuAhu0odyobfXKV-Ro17Q7Kh4VeK2hFqh6sh9ZHzSaLxog-PfeKEjkrHZjWTt0PYmRsiNc-sH4wscX-xIC0Ply3YevVEdjckyVXCD8Vq5E0Y2kF0CF3wfaFyeKxVJNjWXS5FNfwsV-U7Br8VVwxcTj5DBMzT6aAkTDuGH8HNWcuhtpOF_GDvgkkZOIQHPIGkz1KcTWOh4Wfj4ttiozt5tc5Zm7Hi_eTi1Io5NON1ckhBlXM7gnO31_Lu9FldBW68NZxIwrMTGEkl6dueMk3Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ: ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26730" target="_blank">📅 09:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26729">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1otSme51lcsgaACWbTmAMOaEDKeoFP41U-H2gyWINr9Rfjoc47EldmB4zcb1f_nJHnRkLW0ecAXr1ixioOFcIzGWlaOst5n7p_DcfMGCrZ63r_TC5Oy4he6Uo3803LQsHZyl4JS5PnAN_LG3PERPScQZXGibUqxqUDE6LEA-r8HX_UhhGizrpnXxrhYLyUDV-CGQy513752r8JWUqUL8Bmalq97SS-fvMUnRVCzubMDGP_hxw5sa_sdCAvF-dMiLps9kOBKKDF1MjbhanUO770kGazITKWoSRPRPHPnxn1aoHLlyrfkATPhU4RQnVUpN3miwvqJ8s3I5iwKVV5RiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
از مصاف دوتیم تاتنهام و دورتموند با تیم‌های آسیایی تا دیدار یاران صیادمنش در دور دوم پلی‌آف فصل آینده لیگ قهرمانان اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26729" target="_blank">📅 07:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26728">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCvOQDbEDfcx9QLHUbOSjzGhMkJtRVjkxAVztNGivD11aFn46aNkF9U8gvIcFGFKjoHHGqV55DhBWVriAEXeBrmhU_fdAAp2hIdM5qScoZRlqByLmKAvHknFzXpeF9Xhf0W3rfRWBWMgSJfTccqUr2La97s95-hxWccmMhQkoI_V6aMl7qnghlVBffb-ohWDzyEjK2iXghQkWuKG7guIfWs11Dawjx7Dv9ktFcigF9AkY0bZuKIIXJCXq3ibUs667-lBxyB-CBOkgBREGsdUv6Nd05Tr7h4IflCBoWadyHUcw_x6hOxVNJSH0u2La2ep6uucO1KD1rsB2yROwBK7qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدار های‌ دیروز؛
برتری شاگردان آلونسو بادرخشش‌ژوائو پدرو و بردآسان سفیدپوشان مادرید مقابل لگانس با ترکیب دوم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26728" target="_blank">📅 07:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26726">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nTfCLBXV-dh04TF5xO4Sn8SYrGcuC03qEoU_AAX6emM9L48bDmWiz5yWiuTjwyoeQq74OMqvZpVevFkZriMKm3netgikghXCwPVCCzf8FxvAKqTBsHncKpMQdmtHS4LUPnGygz6rTkbei4j01m_s_3mmRrRT0Gs77cWXNAcCQBeCBnLtxhSXkPaHMCTGP8MMSP-ybCoC4EOXln_aoRHcNDYJRfl8RaVGdSzIMIptd5HJwO59yDrFYAsirByLMOAp8-MgMSADSFajk3KR3DTs_rFBcA1QHPdLfgQCYbAicCB7yWOEUJeOqnd2tcDPTOfXkmUZ36hNyRYX4GqukZ_GGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LvO00pcNgDO-_A_tRL-w-t2af914k88-xdCCUC-oKP-KOHGS-QaoIav2WZxOlc2Lg0HFBqsghbpvkvHFjVLNOx1vjdl7F0At9U17u_6YhuZuIyFl0lQBaYa0gD_E7auPYBFVZ16zD4zaY9okMEL3OD1LetsGaAYNVj5jmqPGsNSKtZOIK4LZXepY3V10JQXXKTMDTQnSngII-zZLnKFmg1HtCh27IQ4MfOFIVhSY_VkigO4JEvoJwecBpTJAYbMsZ7l_SKog1ekjFOK_FxdYs5_zp7kMacUNJzAXt19TP1pBjigtjqzwh8owoLHczmwvDpTHvD1XsCKaq4Vk7m1MTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه مسابقات سپاهان
🆚
تراکتور تا پایان نیم فصل اول رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/persiana_Soccer/26726" target="_blank">📅 00:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26725">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQEUAjP4xXOzjk-fFMnPSxZnMbW2CyQ9EtYWBv-yapeofXIoh47Uk11QdshuT8Q7NnORtIL2OMT8Cl1ojZaPZB_mgXInn1NYDv4aKPyfgIwi1g1oHv9rr_ry8b2-ZfvkB-k0lgRur5B8nnR6Hau9QR0Ar_o61cyzUfWfgQTROHMjom7Es0sZQqZB3EP3CfIgSM-tOxmGPylUEedT7Y2gvYUQQ6upJb69lFBe7HDYv4Rdm6nTyJg0n4oB96dxdoUiCM426dYtS9lPturSldCleMCgkYtiFW3OhbMeYeYs9Iu1OCnHZZdTZ5s_CtW1zi2Nx127E1V1s2U4joKAHmUalw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن…</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/persiana_Soccer/26725" target="_blank">📅 00:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26724">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjOSUHO3MRA4cTn_4Ma4pAfkPFwsa2_FwVp1idcK-vBAP26tMowJcgUVwgb4hv0MVjS5KXoQQNzFWM2Qn5PzpffxYrJNPwNBrT-WA5fMPVesd5Z-sLosC4WAr5NlbS-X9hUIYr491Jy8ReWporUWe52_o1ZRZb0DZu_uWGARtVcsVwfWRW-WwLiJzXlGoCLc9GL-kJdUMNGklnwcP4Ilevek-x2JiDBVOZCdu3FFf4hfWlDDNH3Ibd1KPEW-V1JKVBV4FfTKrz32V5ooJN30OmOOilT7oYY-WIfheeDSZ2s-U1ka7zGYKnK5tLOnYgEHm0JZd1ktVyqY9TPZI5gBSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ قرار شد امشب‌دیگه سامان قدوس پاسخ نهایی خود را به آفرباشگاه پرسپولیس بدهد که تا روز شنبه زمان خواسته. طبق چیزی که از مدیریت پرسپولیس شنیدیم قدوس‌خودش‌اوکیه به ایران بیاد اما همسرش برای اومدن به ایران مردد است‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/persiana_Soccer/26724" target="_blank">📅 00:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26723">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb5d2d50b.mp4?token=upnT-ijgh4cJP_ab6YJ8PDABOXteRHHy13Fc_zLXY2ZL99g5ht1lN9PtytIiP-URdvBtoSEMtAd3dExptDkJuFvq4AFiMnvMcr8XtN1VAdhJJ5fU6FbYIhSIOtegvMNuyqQgWtwxub2qJCdYRtMtsfquNMa8aJkAPJWg9Gz25mNMt-8YDIrk0kpXMPyAUWoGBiHJ0r0i-a-vV_Fo7O6v3Ab5W3B-XyK1DtAwfCZw0wjD2ndXofOR3bPCXF2wg2wed9YPiYuT0OvamjYUuGhiSspv2yl_Ks15LqKE7KDaUr6h_cAIxW9pZL7ICy5Nsw6xps-9MjADHgDmOkkLmx_JpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb5d2d50b.mp4?token=upnT-ijgh4cJP_ab6YJ8PDABOXteRHHy13Fc_zLXY2ZL99g5ht1lN9PtytIiP-URdvBtoSEMtAd3dExptDkJuFvq4AFiMnvMcr8XtN1VAdhJJ5fU6FbYIhSIOtegvMNuyqQgWtwxub2qJCdYRtMtsfquNMa8aJkAPJWg9Gz25mNMt-8YDIrk0kpXMPyAUWoGBiHJ0r0i-a-vV_Fo7O6v3Ab5W3B-XyK1DtAwfCZw0wjD2ndXofOR3bPCXF2wg2wed9YPiYuT0OvamjYUuGhiSspv2yl_Ks15LqKE7KDaUr6h_cAIxW9pZL7ICy5Nsw6xps-9MjADHgDmOkkLmx_JpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇩🇪
یادی‌ کنیم‌ از شبی که جود بلینگهام بابت پاس تماشایی تونی کروس به وینیسیوس جونیور او رو تشویق کرد. بهداز خداحافظی تونی‌کروس نه تیم ملی آلمان روز خوش دید نه باشگاه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/persiana_Soccer/26723" target="_blank">📅 23:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26722">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9FWvwtUVAtMxYEqONN97EzDYjIZCxASjwDTTK9BMiuaCntuhJM2rOpRL0TjdWrmjxZRFLt9iNtY9DAdYaXvG33bhLdxN0anwOZD10VHY9vKaBVFV6qaTxGqVcq0xVVUSMZUbH2DfrrM5cG8ZOrRVLQ_Jmod1qtcyZg3NQU86HK_0zJ4Pfuz200jK0Vay1HqRtJbITd9GVplb5zbweOcCTsJ2StbtZ-TyunveVAAg7K0hkvYkw6SzhuXJiOVOafBpLrKmP9HRNr_jFTD9legHOWIfBvUFnY9HKnPRk12x2d2DGjJbjh_Ft9S70TOfhWQFyURYyYylKcLX1ZQuc3-Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/persiana_Soccer/26722" target="_blank">📅 23:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26721">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXjiJeTBzH34JNgzN1ogDjmvkUO94c9HNsOCy68PhP7Ia13bD5-Y1ptfEsgz5OtBK9w7wMTCS55QzrK6lTYWgaRQ-vYsHsaeRw1h4CGs7868gjcbDXhMJYy-FR2ikvLdHxjklpFL49HUZ8fn80wkpTJDMqZCyPOY52ZFLvZYzoLck7kOGJXj0gkTo3yl8otQw2hP_B_zG7E5s1bCkIo0S3itzegtDG6gHz5n5vfXb6ladqnOxLreHydg_oFd1mu189s_U4WJ_YJb0mADCcvP2h9ydAcOpuKpq2zNEzFsoWDniNDyfKK7GeyP9WrcvmGfZZggiZ7kpcchf22lxNbD6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
احمد گوهری دروازه‌بان سابق پرسپولیس اومده ویدیویی‌ازعملکردش‌رو توپرسپولیس رو پست کرده. تاجاییکه خبر داریم مذاکره شده. توافق هم شده اما تارتار باید تایید کنه. بین گوهری و عابدزاده یکی به احتمال فراوان گلر دوم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/persiana_Soccer/26721" target="_blank">📅 23:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26720">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZF_7xTmOOwCHDEZvPw2fB6FPOMly2Q2prYwCWj_2KOCUpJ40OuifdjkMfrknYyoMTh0vRjgtxW67kPlSWRE39s-MIWdRve_y1aC2xoFBkcyPXkfS-R1RTzkscnO1Wn9iVp0AiuF8FYAn9W51k-zeZ01lYofZzihMvsYozuslIs-uPXZUVaTeoAzVYoOyHwxr3oH1zv6kPk9SiBB7TxbRx9gtwE9Et8YQLp252QNZ3ZpT6wy_GZOBbfS0TjQxVJiFAcRckANEQorqiKMZusvM5o16lsaUjCGeMp-xSMt0oGteDBSpM4WXUmDAT3Z1XOAjzZ4GlzzfWO5vODd8mFnHeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/26720" target="_blank">📅 22:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26719">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9VTVwS46Bt0yEfQB08ecwdEchrvS4swyAA-5N0MUNFEZYTmJ7man7Csz8R7OHEyUufmTPv6a6ZEKMiwpPsFzfhp8lTSISuDAEUHlC9_-E7j8IMqpx6FWshdBxExTGWK98f4Qj_8y2I-0_pz-8y7WgO__qrn8pMdY_IXe654P49BRlwUhoPcoH6kvp0_eeCrU-HdnE6lfuukyxn_OsKgIGDU89UzEqIaSq-8V2e2-o3y_KAa9I-s45CTmdn-i3r0gmiszoIasAm-ZyksoYAByQD2zpuGKXFpncIwk-6s-5BU1d53WW-_I-2Is77vfrzuHEdZ-3l4ZTP6xMgB0wYFWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیکی‌نیکول:
یامال‌ التماس‌‌میکرد باهام باشه‌هفته ای ۲۰ هزار دلار بهم‌میدادکه باهام باشه‌. یه بار بهو ۲۵ هزار تا دادگفت‌نیکو ویلیامز منتظره برو باهاش وان نایت بزن که من‌قبول نکردم.میخوام‌از یامال شکایت کنم و به زودی اطلاعات بیشتری ازش افشا میکنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/26719" target="_blank">📅 22:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26718">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbedc9e3b3.mp4?token=aqBgdC60Cj-mVcEbbpd1xagno9kCGm5EuT4dStzaAWXss8Ze8i2rvyT4irbKMA5S1lO0x7B4kOjcM7QfjtiMJOzqQqVaKg6XW8qPjcJWNrtqieG6IBTBibvneKmwEt9_SW0d4AhOpoejb928GQvMLkowrBsV601POd9_aNxFxPP21yR4rFR-9qjfiLPcMZ2vIqbfVJ8Elpa3M_fwQd5BCxcvIhQHxwhiP8eYL_bfTZOfEI47K6LvVVmk_WZapaXqH6mUDSFfyYAsERXcyWvamJ_phMd-0Xw7j1rokvOMdhV74FbWfApkEX3Tg1y0KPpV01s_yYAJXMlX2F-tjsf5Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbedc9e3b3.mp4?token=aqBgdC60Cj-mVcEbbpd1xagno9kCGm5EuT4dStzaAWXss8Ze8i2rvyT4irbKMA5S1lO0x7B4kOjcM7QfjtiMJOzqQqVaKg6XW8qPjcJWNrtqieG6IBTBibvneKmwEt9_SW0d4AhOpoejb928GQvMLkowrBsV601POd9_aNxFxPP21yR4rFR-9qjfiLPcMZ2vIqbfVJ8Elpa3M_fwQd5BCxcvIhQHxwhiP8eYL_bfTZOfEI47K6LvVVmk_WZapaXqH6mUDSFfyYAsERXcyWvamJ_phMd-0Xw7j1rokvOMdhV74FbWfApkEX3Tg1y0KPpV01s_yYAJXMlX2F-tjsf5Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/26718" target="_blank">📅 22:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26717">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-0sxz-tTiJx1mrdgdMYqCzieU979tVTrjBr5qmbltAQtV3BIIJFNoPNbVb-U5Au0Axd_TYhlAUILyykOsiRCvm2iwsLTcLGeE3Eev7CKA5ZOWmdeF8iATT6yqY4-Bi4vC2QEN-mGnLhIgWAXHr2njEL4UGfIvFmp6cGRlQVxFEV5vaXMuVKDGWe-SGP13Fda3VigiJMtGXl1B9GoALQZ2HFe1_CXNcU5V6auKc9wLHviYrD0Vw-nhpmW59UzXvDeEQB8eHC0ovb2wsmU6D6knx5Ruj8YlsfJIX6Tk9VH2uA9IuuhzhtCyWq_7BRrZaYfk2Fk3SNh7tLw9oqb9-KwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه اوضاع کشور آروم باشه دیدارهای هفته اول لیگ برتر روزهای 23 و 24 مرداد برگزار میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/persiana_Soccer/26717" target="_blank">📅 21:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26716">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8DupcJgAPq0XKkpQL0jNs5MEIJGzvLzogboMfFntZH-U-dEfn-aFhja6P23SQsHH7VsUa9Q3BTELEoJ-WXP1QFkx5t9C1OlLAO4Kwi-WE9v2kVyG6a14H4LF_bixeZqtItA5-4I_4QTCS-z9Q2hpV_pWwneDgrp27w0Gh0GEuC1O8fXTWSzMApPIrWPdcXhrjLYW_w_kvcsHRDcqa9vjyGYLpGLcoN3OW4B3YTIA_lPF99pr3kZ-P1mh12V54a5m7FYZZY8cF0uvtahP9dzA6mrS1X_JM1O8YBGWI0SJP_yn_m-17TKHtDjav8RtPTbkIE5_n_ou5uos_olDOov-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه نساجی مازندران با انتشار این ویدیو از کسری طاهری از خرید جدید رسما رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/persiana_Soccer/26716" target="_blank">📅 21:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26715">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnd7Hyqrln_mPn3Vq_z0Ps0mVkacHnzmB8nDLh25RYPzRdGdHHReCu0BoXubgeKdj0_lWIq7pMAJfFsVZ0UcOjUXBer-LNJsSsbIxmBmGD8QsKF30bixQL37dhz0mY9leJCbiV7HBya_Kbhb48I6hT6btsTXXMyTndd2JX7trWlJJyNfRvfD2mLfkdoxEctpOewSlBNWwufUUW0NX6T98yK6ksJAuymzQMifmxOgKXNowO940ZWDZcXdX2u5mBRIjjIkZzGXjfrWfgrAQi9foNbifMJwLlceGO30DxBWNwDJSQtxGcc_XOaOE9Yl9sFQHwTJyOjt7JoKiCHICtzCXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟡
👤
#تکمیلی؛ امید عالیشاه کاپیتان سابق و با تجربه پرسپولیس ازطریق‌مدیر برنامه‌های به مدیریت سپاهان اعلام کرده 72 ساعت فرصت بدهند تا پاسخ نهایی‌خودرا به آفرطلایی‌پوشان بدهد. عالیشاه‌ امروز هم با مدیریت فولاد خوزستان جلسه داره درصورتی که‌پیشنهادمالی بهتری‌نسبت…</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26715" target="_blank">📅 21:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26714">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c8d48ffad.mp4?token=NcBJ1T4_HMHkJfNol9FlGnZnMrF-Xetjunm5IpEES82B1UWq6C92QXdiaMNKXFYbLx70i0kaRwjpzwNWQ130j5ThticDZopkewe0Kt2aYtA9UaJBqI-AdjlTSYleWb0Wo1MlFQsqYFzHREJBHRS2-OAYSdiD8puN_rhPW-3xtvQqlvEej1qd5BNFjEbSNuHfX5MVRZ48C4Z3JwcqlpPm2oq6yGJqWl6h0p-3-o_OeKFErXeriNB7RmqA_uRPzhtdIB5y8oQLeA4Dg_UPiAy6ktB4vh4Hp3a9pyKtlm1RV0RftWndYIZ6U1pbKdXe1pRwOKWiDMmLjsS2Qjb5h3M4GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c8d48ffad.mp4?token=NcBJ1T4_HMHkJfNol9FlGnZnMrF-Xetjunm5IpEES82B1UWq6C92QXdiaMNKXFYbLx70i0kaRwjpzwNWQ130j5ThticDZopkewe0Kt2aYtA9UaJBqI-AdjlTSYleWb0Wo1MlFQsqYFzHREJBHRS2-OAYSdiD8puN_rhPW-3xtvQqlvEej1qd5BNFjEbSNuHfX5MVRZ48C4Z3JwcqlpPm2oq6yGJqWl6h0p-3-o_OeKFErXeriNB7RmqA_uRPzhtdIB5y8oQLeA4Dg_UPiAy6ktB4vh4Hp3a9pyKtlm1RV0RftWndYIZ6U1pbKdXe1pRwOKWiDMmLjsS2Qjb5h3M4GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26714" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26713">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3548b140.mp4?token=bRP2QZMja7ebwtV7GVFmorO-3DomdG4zFtBKqSWTajCX9N80tqrKYzf65aA-i9Yw7p9KILKwQRq1LtxpBKhynjR1vB-bdAJ6TNSrR4ynUzO905VygXsJi-k09-wlJl5acsAi7AH1daZ2qjxeVCIXfYxiSjJrVvS-bwxBqTJ3BWYmyK7X5a1wFLo-95bzdSyhGqUHP-b-L2640k6GUrq0Z-U8lwa36g7SGgXT9A4yaCIsutyEkh0chspivU-TuP5gXOLviUkRaGatHc1IWqKII3CqGxU_vNBN1U1WqAuYdnHkSrV0VLfSrzbOjE0Xvy0N1WrzOwNKohEA8k5GF9HsmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3548b140.mp4?token=bRP2QZMja7ebwtV7GVFmorO-3DomdG4zFtBKqSWTajCX9N80tqrKYzf65aA-i9Yw7p9KILKwQRq1LtxpBKhynjR1vB-bdAJ6TNSrR4ynUzO905VygXsJi-k09-wlJl5acsAi7AH1daZ2qjxeVCIXfYxiSjJrVvS-bwxBqTJ3BWYmyK7X5a1wFLo-95bzdSyhGqUHP-b-L2640k6GUrq0Z-U8lwa36g7SGgXT9A4yaCIsutyEkh0chspivU-TuP5gXOLviUkRaGatHc1IWqKII3CqGxU_vNBN1U1WqAuYdnHkSrV0VLfSrzbOjE0Xvy0N1WrzOwNKohEA8k5GF9HsmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
پست‌جالب‌مجتبی و مصطفی بلاحبشی بازیگران نقش‌رحمان‌ورحیم‌پایتخت درصفحه اینساگرام‌شون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26713" target="_blank">📅 21:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26712">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X93D2CYD4Qx2ZDYoFc1fLJWVIo_20cMM_daGhaWM3u_BOyElboem4kwMnCVkp9ZIFDk8Iqb9bsS6qn0SmBy4UYyJOLzvpun3NreHovK7pGqarnLp7wj7GFVMisizyLOhUNhFPevzA8Ukf1Lh7S44FyMvuQa2JozXcyghFmTNKwwYmW0KLmv3sqb--asz9Bc1B94MMDf2kT5d1fDhFJoGEDNrBWPxofg1nDk3LyHtzCZ4k-2kB8Y9TnNL_MXLLbaWSgPBXOqF9qNTKRyQrFFuIUx3jSZbOr3CmYIynEC1Ol93PTh9u69MjBXSURSu3kfXp284jQHw9m-GAa6vJJXk_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اسکای اسپورت: وینیسیوس جونیور این تابستون در تیم رئال مادرید میمونه و قرار نیست که جایی بره. رئال مادرید به تمدید با بازیکن خوشبینه و هر دو طرف خواهان رسیدن به توافق نهایی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/persiana_Soccer/26712" target="_blank">📅 20:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26711">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSMz8orjY9RPu6ELxqMmuFyd2DF7S1BIyxZ7mvfgUnkCM0fO5qVtqZp6Z1aR4sUWv7c-1zEBlFvbPhm6sQEtq3u1HBFhbk7yV9kp0QnHNUUYfWIjAVRoJ4QPKMcbkhTRU4lPdldEiw32muu5Gm3H7rH84NIgea5oLz0Rjm0Uh_5W0K6mfALsrmSWNSpk2CWXLaIeJvaY9Or7pAZ-rmL_6piJTzOTps-RNawHQczzbNunyeOAEFStAquRpOzcApy_chPbWh97inT9IsQoJN7l4D4pLVt2PeSobvPaIV0gjmpA8lly59ut3LtFi4sS7LTEA4UI2HKopPedNzTE-MA3JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ باشگاه تراکتور رقم‌رضایت‌نامه‌صادق‌محرمی مدافع‌راست30 ساله این‌تیم روبرای رفتن به پرسپولیس 100 میلیارد اعلام کرده و از طریق مدیر برنامه های محرمی این موضوع رو به مدیریت سرخ ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/persiana_Soccer/26711" target="_blank">📅 20:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26710">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24d9dfad66.mp4?token=A0F2GopP2GsD1guV7LAMV0d0Y01p6ev7a9oRFwbqGbAPy7VGZXxxE60DFkw5xxGjTt8qEU5vhm9PJBSS8zDF_QNUnuEhna6cKUw9DtsKEYVjrJSVW7p0XFvmPxHCcF5EVxhaShjSQlz4pLYKY2TeE7CgoY1E8HcTTG5C0fkhjlbw2UtQUzuallvAts3eEwnJWBfkoTmec0YN3-pUo1OaOh7v_c3aoz_uaz1L9gvQGAQmgTbM1iyzaufgO0W8ImIYLoTBrwKx9h5YbaogEv-osnNQfprZNIzCc3eZ27ntbTPkV0bibQ3UtyirOAeaAstTC7n1IMpohsrQhshl5SOekw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24d9dfad66.mp4?token=A0F2GopP2GsD1guV7LAMV0d0Y01p6ev7a9oRFwbqGbAPy7VGZXxxE60DFkw5xxGjTt8qEU5vhm9PJBSS8zDF_QNUnuEhna6cKUw9DtsKEYVjrJSVW7p0XFvmPxHCcF5EVxhaShjSQlz4pLYKY2TeE7CgoY1E8HcTTG5C0fkhjlbw2UtQUzuallvAts3eEwnJWBfkoTmec0YN3-pUo1OaOh7v_c3aoz_uaz1L9gvQGAQmgTbM1iyzaufgO0W8ImIYLoTBrwKx9h5YbaogEv-osnNQfprZNIzCc3eZ27ntbTPkV0bibQ3UtyirOAeaAstTC7n1IMpohsrQhshl5SOekw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق پیگیری‌های پرشیانا؛ بانک شهر هیچ مبلغی به حساب باشگاه‌نساجی‌مازندران تا این لحظه که این خبر رو اعلام میکنیم واریز نکرده و باشگاه نساجی و مدیرعاملش فشرده در حال مذاکرات نهایی با باشگاه استقلال تهران هستند. علی تاجرنیا و هلدینگ اماده پرداخت پول رضایت نامه…</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26710" target="_blank">📅 19:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26709">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-nzUiTO8aKxLLip8Wcs4yXtmgKA0tVSJRM6GsVLHbJFURq8XpYGw8Q-k8cX18Y5VtOkyjRx9jo_7e3_H5pzsFSjHD2UEFI5hDxtqGvQJVwnmRAGyd5zTj8RRkBibt7Q32mhytjBs5-W7G8fB4hBSw0DSgT7jb3JPkiDb9si8jd-Cd386HNj74OUAetWlQkiIxRdtb15PMJ99cNWO-AIBBNNgObMUY1lF5GIAVJFOCL4ThiTdygPDSDdnWWb4ofaoNnRVQuQNGBN6VkRDH83d0B4ZkO09kG36y7OzKrynohzVq00mPKpwm1ZRhFOoXp12q9rrT3EFMM-5HAJDLbZyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ میکل آرتتا سرمربی آرسنال تماس های خود رابا وینیسیوس جونیور آغازکرده و در تلاشه که اوپیشنهاد تمدید قرار داد رئال مادرید رو رد کنه و به جمع توپچی‌ها بپیونده. نیمار هم به وینیسیوس گفته جدایی از رئال مادرید یعنی نابود کل دوران کریرت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26709" target="_blank">📅 19:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26708">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxN0dhdsWYlTy00oTWs6rLXRSSfijsMGgZ44g7eW_iln8L3gQRxsMKe4kwkTzuivwRp7pAnKZsrolN6XSIVPFivnX1-aVwpQ5hKzlYXGB08WRH6ZGH_iQEEIRi1lGPf_zimRIiulWeKL37b83aH8sTdahrmXhvsctmMyxmHR-DslI2-KTVualmp7iyHLY-R_lOZH8q3qgraPzX8myEW8dkJFWUnES6_5KO4tINWRNzdU_FAsUt3D7iQFoy9ic3GqsZlppB6BNIWQkyInH5ZD_oJYCJ7XFyYhPzi-Zog5aL3lj5bynhT6hfs15rYqzPOE_XLfihw8V-R_TUOa8L86oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام سازمان لیگ؛ لیگ برتر رسما از روز سه شنبه 23 مردادماه آغاز خواهدشد و روز 2 مرداد نیز قرعه کشی این رقابت‌ها انجام خواهد شد. البته همه اینا منوط به آروم بودن وضعیت کشوره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26708" target="_blank">📅 19:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26707">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfV407MgX279CoitlII8rU3LqMDtiKSl5i_pk7CHA4UqxShyqa6IMjrxV1t43OstQ7-umYaW_Avg3p-vnmzzc3hbBzD5k6V7ukPDS4kjn_Gzqkp6PzQlZ1AI2mHCGrH_Y7ArZ3UaVN2KfF07hd7o4kUYy5yz2YGgcGIzjwUI9h1NbiIfbMWTSOoG0XisLmLgQqiV6fceeJ_0YD_kScZOmYn925g41JY1lo85-BQuwqCoLL_bd8pgGEBWCO27Hx5rmARYq0SK56lVs50fYGmh4xvK8vlzcSdbDid1oW-TmT-gW1sdLvylobQXuTfTQR9ETr2zh7zLKUNMx5EROTPogg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ مهم‌ ترین دیدار ها‌ی‌‌ امروز؛ بازی دوستانه شاگردان ژوزه مورینیو مقابل لگانس در مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26707" target="_blank">📅 18:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26706">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c711337.mp4?token=YNe5ALQkLsvrx3SOlGyyt-I2i2JgSRE84DTtkrKyzlBLPAo1xFuY7z_itrof5d_ZWaMw1F_VNcq1eX_Q3Vx9J8YheKOp63UEn9Uz_rVlkBzh7dsuWbbWYvYEaIhVNJ2mabaJPEFjTpgVGvjDo99mjzVw2DHtQxstgXZr9zVDGpnLN04uURfp6eEcXAFnbW-eD-XCMAVNTXWwWZ5rUlZI8NrfkBCRl2Pwhu2hJFxHpFrgKnE6OnrjqYHxDtZW3ygnRvrAeJ_wDD4GxvwQrtkYWfGGEirO_5PlJOVh29n4_OhDfTsDoScgxwmzXZSmMyG0xFJKMqEw-VJcx33mjhbDn37prftz7Yr5exxSjxmCgSozEY8kiSvWOzF-AS_LBXbe8vSds-4aUSeCV6Py-h2fIfBx1vdWj9KTLN2oPqG0dB2FTLVCOmx-bXx0kc7_jc9zIx0O0Zc82IMHnnOP0MKEb98sWU9K2a3NFzuRIF436Kz5N5pARpBEiceusz39_hPP52Doorp9GXv7xSLmH95Tt79r5vPzB_XnedYvf9mcyyZNH_bE_em9It4oEkip6yZG5Zgij5mZh1POGi_P2WNeMW_sq3j-1HPn93I25-sAFTfny3kk27zR3KX-aHm9V9xpOg8HdrsYvjuqYhT_jcm37GmW7z5fyxOqATjjyEBzLMk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c711337.mp4?token=YNe5ALQkLsvrx3SOlGyyt-I2i2JgSRE84DTtkrKyzlBLPAo1xFuY7z_itrof5d_ZWaMw1F_VNcq1eX_Q3Vx9J8YheKOp63UEn9Uz_rVlkBzh7dsuWbbWYvYEaIhVNJ2mabaJPEFjTpgVGvjDo99mjzVw2DHtQxstgXZr9zVDGpnLN04uURfp6eEcXAFnbW-eD-XCMAVNTXWwWZ5rUlZI8NrfkBCRl2Pwhu2hJFxHpFrgKnE6OnrjqYHxDtZW3ygnRvrAeJ_wDD4GxvwQrtkYWfGGEirO_5PlJOVh29n4_OhDfTsDoScgxwmzXZSmMyG0xFJKMqEw-VJcx33mjhbDn37prftz7Yr5exxSjxmCgSozEY8kiSvWOzF-AS_LBXbe8vSds-4aUSeCV6Py-h2fIfBx1vdWj9KTLN2oPqG0dB2FTLVCOmx-bXx0kc7_jc9zIx0O0Zc82IMHnnOP0MKEb98sWU9K2a3NFzuRIF436Kz5N5pARpBEiceusz39_hPP52Doorp9GXv7xSLmH95Tt79r5vPzB_XnedYvf9mcyyZNH_bE_em9It4oEkip6yZG5Zgij5mZh1POGi_P2WNeMW_sq3j-1HPn93I25-sAFTfny3kk27zR3KX-aHm9V9xpOg8HdrsYvjuqYhT_jcm37GmW7z5fyxOqATjjyEBzLMk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آنتونی‌ جاشوآ بوکسور سرشناس‌ بریتانیایی و قهرمان سابق سنگین‌وزن بوکس جهان، در مسابقه چند شب پیش خود برابر کریستین پرنگا، با آهنگ مشهور «نقاب» از سیاوش قمیشی وارد سالن شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26706" target="_blank">📅 18:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26705">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGjh2H1novOuEb6ttSOFJdkvEXfiWJKhgS8IYuQlO8XQrz5qJ2DXmL7HR6O34dWN9qm6gRjVRiInf0XGRrUTw_at1dJBmG0BAG4qV0iElL1EGDUsKTzx0cgQpGvn2tK27wt5UeTPCPunFwFZ29RHUbRH11MOqkaEY6SqUpecW4uXiYP_09cDWUGdD798_ZIxQTyOMqoUarMXHOUZPqcpLzCxHg-aBTEOYGXLuziklxhosyR3okIURRE-YM4ILv7dfmoVSfYW8gmCFp0NYYZruTTAR1zYJMAaOuGC-Ie3RhHryoeg-WT1IFkO5oW0YmsFxyK2fHSQ0zo7YlU2FQAthQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
محمدمهدی محبی وینگرراست سابق سپاهان با عقد قراردادی 3 ساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26705" target="_blank">📅 18:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26704">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">برنامه کامل فصل جدید لیگ برتر.pdf</div>
  <div class="tg-doc-extra">34.2 KB</div>
</div>
<a href="https://t.me/persiana_Soccer/26704" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔹
این هم فایل برنامه کامل فصل جدید لیگ برتر؛ ذخیره کنید و برای دوستانتون هم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26704" target="_blank">📅 17:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26703">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3TksQNs1DEkTMpJQDblSyaPOVy7KUlUu0IWsyuC05DuDBJ0QyKwBDcoto-pJz5nA-gyZmeFt3vSIw3RCq4ThWyBbAKhYTkH3UJ_sb7lWsujzEVQW2OuujqKtRSL62ZWNEt5PjclTNffV081EMcjQ_m4uBfW0AJCEm6cX1O3VUXnTnrEaCLL1ra1-5yXtxuHZF442e434vBL03Oz67J15KbL36193q0y_YP9HgdTsWx1beoAgqpstNegkwnWiUo-2rH_7XASwOhJbshlmYr_8N8qJXIrFJlP3u_akGZhaWrL7LYva8Jte5Tmk5aPRidsPyh2bbqaduwoTQitFphX4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دوئل‌های جذاب 4 تیم مدعی لیگ‌ برتر
🗓
هفته دوم:
سپاهان اصفهان
🆚
تراکتور تبریز
🗓
هفته‌سوم:
استقلال تهران
🆚
سپاهان اصفهان
🗓
هفته‌سوم:
تراکتور تبریز
🆚
پرسپولیس تهران
🗓
هفته پنجم:
استقلال
🆚
پرسپولیس؛ شهرآورد
🗓
هفته هشتم:
تراکتور تبریز
🆚
استقلال تهران
🗓
هفته‌پانزدهم:
پرسپولیس
🆚
سپاهان اصفهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26703" target="_blank">📅 17:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26698">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mgT-HExm0iFWWmcqkLPMNnJHuuI7N1NTmShR05gBsxGA3anBcR7mRvn2Vc-eIARfi_Q4l5tXH1pWMN7wAk-BHvx6MwV9i8EqRrA20aKqV5UymyrQDe3MbXG_bnzsdlJoLEuXHQuJnYyoAX_DEhQPYBG16UydlKW-Uc67Uv9ylk_Swyw_Ni9mHT4cAQjQnKOpZTr61JpkBA2SbTjTCqw9iK4I3D_fB5WmsjVW5QbjmquSsxm-lUS113uN8qfUi2h7K8-e2Iwtlktb1Pzu9ESY9wQuK1ATkLRfGFye4xdpAU8V0SbF9DWtt0EHan56maXGdNFJWGz1O8YZv66d-fsXeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ddcy-CSiLEloFQ4SkIgo2CIUEQk2xtM1Z3o4VZWjozy-hfgmgW5YSvBkkeyVdTHSjeKWFimgDdBaruhf72btoZBHNBqVaaIVAdM4o3jLiIYs0o-PPipyuj2c5ikG--XvLDqh3G-186Q_fRpDdZnOv40d0NyE8a8uoP5KfVddbyQ1z5xZv0F_lnfHlqieGs2dkjnDAYnIf1F1h5RMi8Kh1-PWBsLIcUkW_AuPgmwRj8_gWYuBcI6tukULCHN_4mW8LF0FR7fIvoA58RFk-P-oxmIdtvXnYq5PUi2uweJpV36rMN4IPO4UJUvoQLDkMsKMSMtxWWLmkqQto7igafvjRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26698" target="_blank">📅 17:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26697">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ea6NtNiFAuuehOA56W1T0sOcQqPFKvfUOaoFYpSyOXDXdVm3it1FibAad2DU1yuyE2Ztlwesmk-cZZeLGW846EoGKYR6jLvteBmY6r7gTYX0H8K0W-FWt1FnFPPoRUYVmS45Q32xUXW9vWpe-gS2gutXyO6e9udCuXcIu6KM4fKuG5mPSSWQD6f1QlnTcmgSCsBl05n2sHCV9XDVo5vqYvrOXskE9lzAwOdUIbfvJMIhc9V1hetfeiZLDxw7r-kfbHGHZ4pBa5Y6meoa30jbyfz86gpti1YZd3pLNRj2K88x0FNWBmQH8sdqyLLFX238miI_iZdAKq3TLullCSgtVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26697" target="_blank">📅 17:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26696">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SigmECcyL3AwTlLELS9pIBthJeNR-9eR7-nrxqYq70Kz7C_2PP4TrkT9GWiz5QscWWjtTbioWkMKaPbTSa4xgFP03HpvpNunbWZ3VxWXB5GsQYKRbON4al-aQRS71-1rgv7W-A_uVZtX3pT68cWpdAAZ3QFsNjbnXGHusfMQ-Q2W_V5R5qw9WTCuG_eviRclTPSJawRhSinKLSIpxz_OOFucPgqc1lWc0FNcZkn6nkAykklSvS9zOb_eyYGxl3zkUpxT0Gc2zzmzyhxJyka57rN-mtMy7UsO8t96OhPmy6nfuQFfWjlOW5GNliEvQeErehH-wfVbKALFLX-I1tULIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26696" target="_blank">📅 17:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26695">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OyUMXU5i6fkOMZeRQMMCPfw2gZ6oJ8aHLGd08a0PTw_fq3j9CPEaF3UgNiWfvzRINFhgWfF2oiP8gzLOrOpZ0E4jELo78NF6DdB5LfFu1USU8Rg-a-1rrn85PKX7A76426y04UYtvOarjkxEM5KSOyNSADM7-awBiR8rWG-l1G3Cc1oPMb21aukM77RPXx9x6omACHt1DFAAgfMLy9KqjxVv88hSwLvmu85PfVoz0n093PmDP6C6vbwFD4h2LvfaMq2bVmMtroA4DkKpSzRGFO4lbAzhKOWCveNlAqGRN_MWGljzNAROUgxpABaNMXSryVzDeMRygXHEW2FBh8WIVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26695" target="_blank">📅 17:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26694">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31211ab420.mp4?token=OEaJ4uT66zlBjPhiRjIpXmd3FhJtpZxPWOHfwvrvPgyXsc83w2oSoY31-jT7qSNWyvMt7Ve2NP0WuoXJuMmc97Scp06KcSyCfUtyB5jHFXzh5g6WoTUoTRbXVnrXacN_ZJChJbMZWh0zZ2d50wLLFhkpI24IvRfjbz9b3_ljc3FMWn9IYRprk9WoLFWjSFv5VsgVc5F6MbZhpOJMD-8ujHd63bOAMpgHLMfb7wjt4T6VWZrGpeLulLyQs7EFCdc5REFiLYBYERQioFQeZExEHf-zPrv7hnarPXujMy9sEgahYeoQ7f0yz6-D1QHCFlh7QZnKqXjP0TU_zx1Hkz7OtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31211ab420.mp4?token=OEaJ4uT66zlBjPhiRjIpXmd3FhJtpZxPWOHfwvrvPgyXsc83w2oSoY31-jT7qSNWyvMt7Ve2NP0WuoXJuMmc97Scp06KcSyCfUtyB5jHFXzh5g6WoTUoTRbXVnrXacN_ZJChJbMZWh0zZ2d50wLLFhkpI24IvRfjbz9b3_ljc3FMWn9IYRprk9WoLFWjSFv5VsgVc5F6MbZhpOJMD-8ujHd63bOAMpgHLMfb7wjt4T6VWZrGpeLulLyQs7EFCdc5REFiLYBYERQioFQeZExEHf-zPrv7hnarPXujMy9sEgahYeoQ7f0yz6-D1QHCFlh7QZnKqXjP0TU_zx1Hkz7OtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
مسابقه بین دوتیم استقلال
🆚
پرسپولیس در هفته پنجم رقابت‌های لیگ برتر برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26694" target="_blank">📅 17:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26693">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PN95EiNa1lR9E-9Y0hAEByArenl9dz5pqQBYNwJYL6R-3hz91VIW214P_T8H-IQRvZ4ArC7YdXKvShTDvAzcDfdk5JK3yI3nUcC6AZb_ysFR7IU1ufrokDcpERK6fEGSgjCSjflMUcIgwIqsVIJJfNBE_GEodNNJC9dZv0FzkVuddwtcNqiXHURcPAKGIKUX_kwEhYqAspkrF9KrVef_OhbfglNMFQeWFtp7faan5q-kPaoZZGiXJ1cEDAqDiwhepPC4mjaMSRasTbsHNA8pn1D_jz77CUFE5wPyopZL4yxV3o1SOedoJmZdTTcbW_jTtiD3GiCMa_ZfcbCmExZPeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فرداشش‌مردادحوالی ساعت 16:00 قرعه کشی فصل جدید رقابت‌های لیگ برتر خلیج فارس انجام خواهد شد. مراسم از شبکه ورزش پخش میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26693" target="_blank">📅 16:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26691">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oiLEEU7nA6SoT70cUpCBO2747cBiXtmebYuIwWpj4xGxC6_oamK8JUuf0_pOAVxwxedh_7T2KJ4Oyl0JMAfxf4lXvCwczKdbp0GSOtbhRiYMUueX98mXm8B01CRbS6dKPzjSGgmkGR86mX89r62J154P9WRVXGlnoMsp_y7NBbY8P1DLkU0CNvvOh04QnN0d4oMUJMCyOeA5LaYXEsQh1SrYmQaLejsH0FNyfCZj_YjlfME9MbgbgMKEmyVKOUY4hr71kblGq0X4ZUX99TQdxc_0A6U1Plo7qKD0lzV1UcZlQp21dKPXyviPQW5GkVMmgDz7F_9B7xRiylIIr5to0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ محمد مهدی‌ محبی دقایقی قبل بالاخره قرار داد خود را به مدت سه فصل با‌ پرسپولیس امضا کرد. ممکن است باشگاه امشب یا فردا پوستر محبی رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26691" target="_blank">📅 16:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26690">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMA8L8JYj_sLoLGBhZD1CQgDRCgOEo4bMufvYNUj03Z_GsSVI5ZMxG5M0lp5n0B2YiVBA8Bo_2vsazSZ0dEBS8WoUi9x4_0O4pYp9BswLQwgQawjXd4plbVDKhdvhHkj0RF5_LwFocXHcPLWBiHX6bSObq74uoKRD-gafF9HYgaXOiW7HORqM7AYaItR4GPjgnrbMfl3LQqUUxOWdujvzgh9B7aGUasBXRg55u_-wlxTeYerc0iA8bmXfpAFT9L1xCgBgtSMAwfANK3mivlR769yNP4XZJnI8TO8qArQhOo0sEQazH5H3vVhMm1Uk3Pfneuozs-L4ZD3EtdFLdK1Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌عمو کسری‌طاهری ستاره تیم نساجی: مهدی تارتار به بانک‌شهر اعلام‌کرده با وجود علیپور، سرگیف و شهر آبادی نیازی به جذب طاهری ندارم. تارتار سر انتقال 150 میلیارد تومانی شهر آبادی به باشگاه پرسپولیس 35 میلیارد تومان به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26690" target="_blank">📅 16:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26689">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ccc06fbcc.mp4?token=EPewZvPVdfHu286TMXF4mdNPNDexJdB0PTCYTE-rMOahzlGXCSspsHXf_mj7yyY_Krp73SSR9V8gO-ZIiJ52c5XlASMZEpdZ3KvO-YY1w0aDnuOFCgsiIWLZhnL4P9xIza2kWWwRTr0wg2GrK0n8kDVAmzIF-9LHFLxUEZnLFTiYIwhIRMEBLa0ilzjgP1AMrpTaGXdt-lrJKruZYoQryfY5j9mbsck04CzpE8yYD8yeENvromTiw6fuBKFVv06QHlgPo2bhQ6Q__0YXM-gR2bGGqO9pHz-0AY2AreHggdcPZfGNHpDmhHSeAbPNFyQFKM10QZLgAsV8OnMrpKGOEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ccc06fbcc.mp4?token=EPewZvPVdfHu286TMXF4mdNPNDexJdB0PTCYTE-rMOahzlGXCSspsHXf_mj7yyY_Krp73SSR9V8gO-ZIiJ52c5XlASMZEpdZ3KvO-YY1w0aDnuOFCgsiIWLZhnL4P9xIza2kWWwRTr0wg2GrK0n8kDVAmzIF-9LHFLxUEZnLFTiYIwhIRMEBLa0ilzjgP1AMrpTaGXdt-lrJKruZYoQryfY5j9mbsck04CzpE8yYD8yeENvromTiw6fuBKFVv06QHlgPo2bhQ6Q__0YXM-gR2bGGqO9pHz-0AY2AreHggdcPZfGNHpDmhHSeAbPNFyQFKM10QZLgAsV8OnMrpKGOEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
هر اثری هنری دیدنی یک کپی بی ارزش داره؛ در نقاط سخت زندگی فردی به دادت خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/persiana_Soccer/26689" target="_blank">📅 16:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26688">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKeGT1sVN86vnaBvHgp5iYfU7MgjZV-Jr-gSfHISgxW_Ne--LLGi03pri59DdAKfm2bks6YHXFq4ZKsy_wK7jzUFd48Sqa3_UVHzew_OnzhIJTTHh2fj0hNkndnWU9jbGRoT-ZFhhrgY7-b8y8mobag4QoQCjNpr-u5chUoe3zpJ0EnU4K9fcdvDonv21JV_GICpUMiWjD5Xp0lalPMxvr6lCbQKQkAGmwNzi04T0Hdr5t3WDmpM3lWTe7jUalz3y4fSxUoofAtuqOhx9RhGFmeiYhWTFQRKhQWiYVOFIyWTah0rgWfLyWYVZcAW-HYlD4IU4h4CYzQmLsgy23rLxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
مارک‌کوکوریا مدافع‌تیم‌اسپانیا: اگه قهرمان جام‌ جهانی شویم و همسرم‌هم مشکلی نداشته باشه میخوام که عکس دلافوئنته رو روی قلبم تتو کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/26688" target="_blank">📅 16:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26687">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jd39oGHWHyCZJr9H6Gbz56x-l8CGIV4OEsAeMeg2VDTdhVU2Qw6ANxjxASNBS8GInQ8ifXqTGd4T0c0eEX047vLBt5158otJ16MEDYYB3GbyNqJuCcJYS0jwLmKCagDocXe4V7JF1b3o9AuvozvKR_efPum_TnC2Wf-gbpXwYIVEAEWMjvNqYT5A7NAP5TfzmJxY4cvIgdkhwI9Pmg90K5xpOUoWF6seHioUYMddlkRTbLzLYWfBwwwm4myH_2TTvmXNleHz690id9rhMHsOhTNMsBV_fGwfX60DuSuzEdkEhielR5rmExcd7SC7kPbVM2_yo15G3uIhekHI0P2wmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول مدافع 24 ساله منچسترسیتی قراردادش‌روتاسال 2032 تمدید کرد. سیتیزن ها اعلام‌کرده‌‌اند که هر باشگاهی یوشکو رو میخواهد باید 80 میلیون یورو به ما پرداخت کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/26687" target="_blank">📅 15:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26686">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/garpIwHNQ8LqV6UAQnivzEoj1ot4NOzd4sPNm6kxL_zRUz4M7L21yH3tr-fU281U8oJsqdtvoHa8hP34l7MUKCJLi7xvpm4U0-SZL89ZTY5croTjqw9-N0zSZRIDI1Lx549G5Azm8QKrh9fGkxxgZRIpdh89fIaEoHOY2A3hu56EUi_W6eXX-hWvEdcLDwWeZYlJbWNJuqIWBouhryQx0spw299nscOzEbav6RzBqkmhJovnSCKJgQNWXjyKBtR4ii7FPPLDgD4Rgb0ZcQvH-UycnwOWmR5f6y0pTuFtgYFvRV44g78fhCGZC7ikwaTyL1muh2kFuYL4QygTtq4xXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
#تکمیلی؛فیفا درروزهای‌اخیر رسما اعلام کرد که ازنظرحقوقی‌هیچ‌مشکلی‌برای پیوستن کسری طاهری از نساجی به تیم جدیدش نداره. هر باشگاهی پول رضایت نامه طاهری رو به نساجی پرداخت کنه باخیال راحت میتونه باهاش قرارداد امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/persiana_Soccer/26686" target="_blank">📅 15:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26685">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEYDbiWzl7pTeqxzWMjHQch3cVRdIXPBPzn9XmS1tbMqxF1V3g0jyO3ZnrpgrWXHlBzQzKwc7LerjPcNps_L7qdwoKSTtd0LKtW39ZxxzxN4ocqwcC2O5CgS6_gMA4Wwnj6cDIF1NLT6n8R64oCuhHy_ropYRY9lpcFLtYryF0mJyNKOjLr6ulu-QqyC4iK1ZWHBS__HVvcN1SSP5LTutgZOCESAFMCuzX18TmqI0-qDCsLxYF2j_S_hj-4ULubb_4YbyGoEH0PrZijwhBCTbwL_DxtgvNoQ95WBmLOdN5v6pACx_ShTajIfPOxElRMHPHpucEAbZtnziWU2fh7jfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرام‌جوینده همسر سپهر حیدری کاپیتان سابق پرسپولیس:
برای پیشرفت نیاز داشتم پارتنر بهتری پیدا کنم برای همین‌ازسپهر طلاق گرفت. دوس پسر جدیدم یکی‌ازخواننده‌های خوش صدا و خفن ایرانه که‌مردم خاطرات بسیار زیادی با آهنگ‌های او دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/persiana_Soccer/26685" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26684">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8Vc7fbiBMmKsw_qofn9-B01z0ZqsECVemDGa2X-hAJHMLWJbyU1viY4DVXfQ4I8hRaXeqCAlAVBoOxoFIYgAao6cXaDmFn5iJQT651g5xLDQEnwD7yeW1SM52oIj541VDsRPrJ5zHg5lQNbE8SwyKjIkZYIU4iyRH_se-vS_iOY2kLupYWzx_DpnpLOg4h4NIcDMVQY5l9ZCaLiqdoFSbqG3OuCerMdNuChRA0amiYIScJ8t6rlOprdRSBXKx75eL7BmMG7AzILHWfWtwAkf2EW2EhyAwAC1enuZZ5gN60VsRqH9HBpuej24nq3rVa7KtSNjWGkmVaKufp-B0tZ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
خبرنگاروگزارشگر معروف ایتالیایی: فدراسیون فوتبال ایتالیا به زودی روبرتو مانچینی رو بعنوان سر مربی جدید آتزوری در یورو 2028 انتخاب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/persiana_Soccer/26684" target="_blank">📅 14:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26683">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZitzHKK3C_jrB9aF0JoowJfZP_tKPv3UCGSZ0B4mFfWmGmQjt8ITHpYkuNxoeWaPFwQYhO2SWEnDP5NeOUJ5r6-7bsJ-zi1QusOSj-LswvPh23ovoeAVBeZn5JOpr161D6IsxLrfFmFYna_FeKRR8Dgk0VOATaIRKtflWvDOrF1ssZVD33iKkjEbig9SG9z0HypRgkotcOG7OmynzTMxBFKL4cG13VwgGvnD-9AALmF0xm6FDL-qa6WMEmMXw4Q7K0M5Q6tVPEb4INAvIDXssIM3v0uuK8or5ye6ppScmcxwVQh4ZVx2TiOIQ74V5lFZIetszAo4hG-znAiCEC0UTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ دقایقی قبل استعلام فیفا به دست مدیران باشگاه‌پرسپولیس رسید؛ فیفا رسما اعلام کرد که هیچ‌مشکلی‌برای‌عقدقرارداد کسری طاهری مهاجم جدید نساجی با باشگاه پرسپولیس وجود ندارد. حالا باشگاه با پرداخت زضایت نامه طاهری بزودی از او و دانیال ایری دیگر خرید خود…</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/persiana_Soccer/26683" target="_blank">📅 14:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26682">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4U_FGdjQNlWuf9tzyOqbX4XEZkscrUrNrMqKcjQAPI8uwMSe9R9Bbk9rI9CC-dK7q7SIN8DmOoBfvRzaeuvl_EPZ-zNdJ6kkHJ3D4YTT0RMz20Ztz9Jr_bdeFYH5gOrXg7BbiWpDHBe_6XPU1ABLxZMLay8Nzw0YJuB8ctn4vAJ7C1OMsdLrV7-0DIVXuWY_Rjapikl7ayU01gkaFzosc8aMRkk_zZ0gevMFu2QjLKlUGZksBu2KFVpa5F7Xgq4pc1slptFwjbw6SPHPK7QAHEiYJHmzczxaekcpVADb_IF1JIM373YehqjNo96QrhUTISO7bQD9do1KxxZ6eUD6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ ایجنت رضا غندی پور به مدیریت پرسپولیس گفته درصورتیکه درجذب این مهاجم 20 ساله شباب الاهلی مصمم باشند با 1.2 میلیون دلار حاضر است رضایت نامه رو از اماراتی‌ها بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/persiana_Soccer/26682" target="_blank">📅 14:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26681">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5bnSJUlGJXm-pCoJXgJGDHsHdu5f8ODw-AQipW2HblUr_0gN6dHXXF-a3u45YZeaxTHSyBc8MPoZnv1l4ahY00TwoLYmYnCg5UAOdWZYzDdRjH4m-40bnqs7Kt6l4WvU3S9h-_SAXpyG80On0HRfeo2sWDlUTdaYUrBpFTVCjieYC-8HxgO4NrJ4H-fjPdam6qlQfLQxwnhpMU7x12YPEEecPQEUkp2SBp5PI18c3NWhz7mYXm3RBIH2HvtSVA0vXZsSkiLMY2LkSreYDYHnoTIu0oufnLrRQ2-Zj6zgn5H4-qaRQJp2AjnZHLvaEIYUwpGe1a3pmUNrVKn93sdDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
مدیریت باشگاه پرسپولیس تا امروز ساعت 14:00 فرصت‌دارندبرای‌پرداخت رضایت‌نامه دانیال ایری و کسری‌طاهری بامدیریت‌باشگاه نساجی تماس بگیرند و گرنه تموم توافقات روی هوا میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/persiana_Soccer/26681" target="_blank">📅 14:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26680">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cy7k2q_PXQV0oHKnoEkY9UUtMdiSFfkelTSvkOem-YAL3DVGsMo2KGVJenaSbQWkrI2lgtYnMIRHgEb4JbpqKUJePDYeRwFkQOBTlJV1xGsN6j5wowNS5eTn3v_JMP7kVNwq8kX3DkZ1XbGKCXMoxOv6WK0_wplJJRXngKQWbJKWkvS365f6EXcRV9xGQYY8XXdb_RuhFUvBxQ6NeZv96mHMFhty3xr8H55zor2buBY6URdZBTllS2LQRNjmWwpwvW2ColG-NSlT6Dhk7y3mKK-b0Y1W2EQQRAXiAEONwVyEcRZ0Qwwo3b3nOkRvVA84I1m9o4SpdVB6pWpR1ZnW4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پوریا شهر آبادی، ابوالفضل جلالی و مهدی زارع سه‌خرید جدید پرسپولیس که سابق بازی در تیم‌های امید و بزرگسالان استقلال رو در کارنامه‌ داشته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/persiana_Soccer/26680" target="_blank">📅 13:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26679">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgyIIVqujzl75dyyWeU1VFWiaLgFh_ofP3P9prXH_hWt3c1zJAp-B2-ekk91Ri8Gf27ZXYeMsGZNDIPVxr_-v5zi0bosZuCBEL1UxTu0vAcInOsHlmP6GePShuEW_VRDWfdVFK9Htar7pm3NwPh2BdwZbTzkyX1VdCJOsMuHZFNE0XAbqkSp4B2Bxor5zIn8K_-5GUmHlZPAPS11JPIusqvpFLsDSTUTl9w7ooJXJraBudcyZFVG0-bAWc2LJG3Yt03SzBlOINx74TybR2BZ7nAhijn0ePJCEBQI75vJ-pt1tlWuT_r_VXpgLWMKRf_l5Whz7cc8Lybeo1GS3RjQdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/persiana_Soccer/26679" target="_blank">📅 13:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26678">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXslOQZzMNEM0JE8hFjmSuIEOWo0WwFzvdyH1kJG0rzaZoYfxOXndgd1LGWNOCrJRb-PHct5sD3xo-RmgjY_oMIKp6iLxOFmNHXMjxV6qEEiGzKTyX2ezcKwSl_bPS6KRaDw3Im-aLGxurhmBvovVeySp7BEqNI9M-Y4dRXrT3YsQLpVEoxK6ghISfCRSrNFxoSqzjmhKBZEj9iC725o38hYWCdJdw8chLrtyE2M2g4vw0X6bGgC2nhzkwtk7dmN8_Iml2VlnQ5OrJKQcHnOBR2A6-saGHWy7YAJar8LWKnLvC7B1SVs1Aefoylwxi7_bQ15_6yFIFge0Pp1MTVCQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمدمهدی محبی تا ساعات آینده قرارداد رسمی‌خود را به‌مدت سه فصل با پرسپولیس امضا خواهد کرد. تمام‌توافقات بین محبی، اتحاد کلبا و پرسپولیس برای این انتقال نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/26678" target="_blank">📅 13:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26677">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpgvVjksVS2kCVqog2A2yNtlGHYJFLONawIUdcwbyI4aIINhcMC92maebF1ryPb8quhFMG-Xf8zsq3V4WnACFPLQIboA8dlddfTuFplgx0JPMPhRNjDhzHAME2AI99xc2t3i_-9JifTcADarW64AYmfSEfjockpJZzsk2rAqxbqtKSAAVH6xvwu3ef9M3Q_S-l35ApshOOHG0-tLF6fKFV-gglypAiEmvTrOQn6bmEpWE064EhXJuequH8IAPTkfZFuiuEv3eYwFxGXdTgMVDy7fkyHjFXWLbvUuNNwalyiKbfOp7qVEWph-ZiOjA6Vek59Pa8KOsh2yPn05IJLN2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
اینستا یه آپدیت جدید داده؛ میتونین تو قسمت «یادبود» اینستا یک نفرو مشخص کنین که بتونه بعد مرگتون در پیجتون فعالیت کنه و توی بیوی پیجتون هم میزنه صفحه یادبود و یا کلا اکانتتون حذف بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26677" target="_blank">📅 13:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26676">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMYBxw1rw76dXiURv4qg8BdX3yaVISEkhNZRNqCmHKPn_bC7Hf9TFJYeLGPSmEoUJCinGOMY78ILwO54wycvHEPWzpQuwqf0CTuFmluhjyg7jVWfXsoDC6RWCfb2T0qnVXMRKECkFD5nlZy-jb65ghNNSUdchXDaRx0uqKhxVj-j_ixAHPgoE4NV-guVUZFy3S1xTOEHFQxLvSUkQFDJVzdGTCjr3SbqwBAoQ480r6As5AWwvR5vO1zxtSu2V3F-soM37vAU096hf-O9d2qZvta-94RIfGzSxYhPOiDh7WCTYoRfioF0La7DXRKc36bo3VTcija6oUi6NOlzpEymzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌بورسیادورتموند درطول‌سالای‌اخیر عثمان دمبله، جود بلینگهام، جیدون سانچو و ارلینگ هالند با ارقام پایین خریده و با رقم‌‌های نجومی به بارسا، رئال مادرید، منچستریونایتد و منچستر سیتی فروخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26676" target="_blank">📅 13:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26675">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kl9UB2Smi6ooVT91CWTVQZ_bF9DjBD2l9IuXeQMKnG2Qc3hr7bRfKW0X217mOsK1AUXNJI27X1pTRNQ6PqdWGeoIA17KJFa7R1jtqd21hu0_HnJvIqjS6YUl-Js9ek9nHN-uhdQvT-Z4lt1a4PhA39IgAU6lL3IKlgUEUxewrrq9trQi2HpZIMC3CH5VGs9jrAbxhGdc3beI_Izi8Ucyx6ibPNeJxPVmRyFMyKoF9WRB4EVxqBit4LKPQT4lJSZ-dDZNSGEu3hJQZfDgtH8SkEMTbAgpsT659LhK-OfiW4fA0DqC-tJLoWbp3f8qoejd9c0z9oHTDIiFeOcIKfrIKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو، توافق زیدان بافرانسه‌نهایی شد و این سرمربی جانشین دشان روی نیمکت فرانسه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26675" target="_blank">📅 12:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26674">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0DqrowR4497qUy-VCZ7-DoaY6670_YX5UHfTQ3qWztHYLGTyl6y0QvmcNpgaAJ48fw5BCDtag4SszY3XPEYMuzh0X9By7YiE6VZAwMbXhLAwjZY4D3QOYnuRR0McIeSIPw05hHWSXZBeaKhG_pqA1kON3L4dHfqdrOBokrhycbGJHLisF_IQn94Hho3ws0WlIgH6S_nj4w_Pp9filX4OMMy7tG1UyhSWlPc7wy0q-8vxZhJDrk7qzOd8BVniACED2IRYANXQSXuSznUkmrWHjkFQGE_lhDgYeTMcTyEuqT9b5ycGKtUpTtZXynFNxVPgus2ed0r8N526Lqz6dnJ1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عجیـب‌ترین‌تولد ۵/۵/۵؛ یک‌اتفاق باورنکردنی!
‼️
صبح دیروز یک نوزاد دختر در تاریخی خاص، ۵/۵/۵، چشم‌به‌جهان‌گشود؛شگفتی‌ماجرا فقط تاریخ‌ تولدش‌نبود! مادرنوزادمتولد ۱۳۸۸ و مادر بزرگش که برای مراقبت‌از دختر و نوه‌اش در بیمارستان حضور داشت، متولد ۱۳۷۰ و فقط و فقط…</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/persiana_Soccer/26674" target="_blank">📅 12:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26673">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUL5r93YyEaYPSbmzPumOcLcERTOgdzW6XDxDVDWauxRSlwCEbV1679pWQyQaAgG-p2v6kZ7hLqZ2EQ6PbTvMVEp-YiqpWsgIPgbYmE0aCHVUFlYIdoHV3QY8PoRd1UiMYemSvf2gZXrFzJ1bqUhnrmrGqyWfsTHcpbUkv0RREi5YUCsqsjvL3MpMG8KXn7PCs_L7GliXqRsBB0Z2yoIZaM31xW6s22k99lYl_aZvgFioU5bVM6ufzurN6TrQCSmN3ed7yhxldnndN2DkC6OgKnOuPOqcBYMLdd77Rzh9enucUYVcalr1-MQbHpo9dXQAoRlzIOdMtoqfrPCfbdVzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
«گونزالوتورس»پارتنرسابق«اینس گارسیا» یه استوری گذاشته و خطاب به لامین یامال گفته: او عاشقت نیست؛ فقط میخواهد از تو باردار شود و با گرفتن نفقه یا حمایت مالیِ فرزند، تو را گیر بیندازد. امیدوارم قبل از اینکه دیر شود، خودت متوجه این موضوع بشوی. گارسیا فقط بخاطر…</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26673" target="_blank">📅 11:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26672">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SX2701wKQP86b5bLG-OPHaDH-rqtWMaq2gMT2qeO71BSKQQ7ww5wfhgYinepvo_Zxq5MQh9lh-6m1UYTokuvc-lIndKqEzhwoL0tof4YGxAyOas_EKCoepkfqnBiHyT-maP9WnOMGPMgiQtaMiyMOFkk2_PTTC5-_OxhdDtCKw9k6oy3mPUCFHQkVyKPO79o-12Z4Gu_Em8G78KaWKdDRZ3hnRPurJxx3DDtyHoGy1fwL4xVBCPizgFHqp1EWaRhnDWiEUxS-Oht7F1RhFtEot_jqevCESAE6-3lk3im0XNW4j1CTHTPv_CngjcfuEQOksQsBVxe4bXSZ56VtYx39Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اکثر رسانه‌ های یونانی از جدایی قریب‌الوقع مهدی طارمی از المپیاکوس خبر میدهند. این‌تیم‌چهار مهاجم داره که گویا سرمربی این باشگاه تصمیم گرفته طارمی رو در لیست مازاد قرار بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26672" target="_blank">📅 11:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26671">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7fa18a77b.mp4?token=qbT7ZHAzcRAWdXeF8DJU8mXH4NggkENJwRwtRkeYlhOEm0jA-d-3gvuGstuHaE8pbPJ8T9k1ppiWym3kpp6cBGcQIROzcXrWERBISt7YnMqdED36oIVBwIshEE_1LUOCPKUwPU3gvod5eXfK50Etfapwp0MquI_aGb09p3kLsXi1GvTDUeQ4yn-HfeHpH0pZ31LwPJAny0mbzI50ZglSbsWd_j-CHAPVVtax4xU74ERhwX4vBb3iH0ALXlG0QsRzBS67_cWGcoSzCMvXwWwIaI3ANnbe-n5MvzoUy2KfjwcL2R749siLxh2N55i9gvnwKrXZKhLSIoMw2oVG98I-xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7fa18a77b.mp4?token=qbT7ZHAzcRAWdXeF8DJU8mXH4NggkENJwRwtRkeYlhOEm0jA-d-3gvuGstuHaE8pbPJ8T9k1ppiWym3kpp6cBGcQIROzcXrWERBISt7YnMqdED36oIVBwIshEE_1LUOCPKUwPU3gvod5eXfK50Etfapwp0MquI_aGb09p3kLsXi1GvTDUeQ4yn-HfeHpH0pZ31LwPJAny0mbzI50ZglSbsWd_j-CHAPVVtax4xU74ERhwX4vBb3iH0ALXlG0QsRzBS67_cWGcoSzCMvXwWwIaI3ANnbe-n5MvzoUy2KfjwcL2R749siLxh2N55i9gvnwKrXZKhLSIoMw2oVG98I-xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🇦🇷
پائولو دیبالا ستاره آرژانتینی آاس رم قرارداد خود را به مدت دو فصل با این باشگاه تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26671" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26669">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5tSH01Ie-ZtyH1V5IQ8bo5_ef8fG6j2okMbGDJS9_pCEGR56hk4lNG6DPDua0wIz7MFcQsMwXN5AoPEPioJD2TbNcOFejMYPsmxXr5nYEsEIk2zhIF0ncsFpsKhMKLo9-QHE_dmfEZ_ImVNiKLgM-2Z6jM5SseOseYM9XE6nZVlwdrMnJyOuapBx-v_28_Ghf2G7vF5uPv-Zsu2BCRzuRIpwMnDOOL4RiOSSs6KiDl7IwFbKphrWF7TexsjaJnLZU157zdxCFsPri-KO_DgkSA5EdSr5JbDMgMiQI6wYcLXK9YrwCDmdDFisi0AeV9meL1qYGWjk1vBEc5S9KB0pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وندا اکس مائورو ایکاردی: علت‌جدایی ما این بود که ایکاردی با شغل من مشکل داشت و شکاک بود که باعث میشد هرشب که برمیگشتم باهم دعوا کنیم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26669" target="_blank">📅 11:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26668">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrPSPl_e3QEaYSUggz2T12NjFu4I401oN_yfgGeb0jBkU77B-qaFHEF3OPsHmK5nyIONsdFJ0-mwtglPibEZb1SKENLu-aacXkWNLlHx_Ym8ubgWzxYxTh9_-gE45Tk5V0ENoh0nKKqY3_9NdMQb5zGLZfmKCw_2gxuhBJzhy_z2oVCNQrm6eUBlJ15wGe8Vh9UVdwg2Z4xMuHN8ffBS53CXsyPZkzr5pvfX5TXKbcwCFrf4Yeu7x9jkeRQIIzHHkuQb93T1D6sld_-962B9DZDyhwxjKTn8cqi6NR9esxBkNUX2IuS3Xz1-HUOSkmGRGrSxsD-PAM-9Zn-OObUulA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریس رونالدو قراره وارد دنیای سریال‌ها بشه!
طبق‌گزارش‌ها رونالدو توی‌سریال‌فوتبالی Day 1s که با همکاری متیو وان، کارگردان فیلم‌های Kingsman ساخته میشه حضور داره. جالب‌تر اینکه رونالدو فقط بازیگر این‌پروژه نیست؛ خودش یکی از تهیه‌کننده‌های سریال هم هست و در کنار دیمین لوئیس، تیری آنری و رپر معروف Dave ایفای نقش می‌کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26668" target="_blank">📅 11:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26667">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6lDgpxkmP_WyKp78iKexcZdv9xcPtGS_EJFlarx_khThEu1VaMZE_x5myjuqUUvDPRkYdndVV82uxDP9vlEEIZCwbRTcD7jznClgpgNYUqC7G_LGzNLPBIteU39skNaDc3vGafPmkrsQIWA9kOtgqFlXZOCqpguqM8nHxMyHTcWQ-dEfiT7V_fZQHvTehWDIUs9LV9wmAgv9fiK__R8w-Zk3u8_C9XG6_VC97fpJdC9OiYxSLoWAFIvSORpHXJptRptk4K6rTQjQrqK1UQYa3ARFL9U9bzVol-sUGfWmuzJD3q3K4jkWwWsq7adlv-M018_C8dkhVbt4MV1Id7mYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
مدیریت باشگاه پرسپولیس تا امروز ساعت 14:00 فرصت‌دارندبرای‌پرداخت رضایت‌نامه دانیال ایری و کسری‌طاهری بامدیریت‌باشگاه نساجی تماس بگیرند و گرنه تموم توافقات روی هوا میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26667" target="_blank">📅 11:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26666">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6387cL6oyKlZdr4-XIn2-l4aTCqxNoLumW8kZg3OSaFkBOX69UpsUSvf8DE5jBBV1oYLt-7SrtrKvrqPIUgn1bf-Va5RdIz6t1XycOv7aIxhUekEvRN90AmjCSFWEeX0GpctiEqCOcsLDbxpxn25wUKvreO6RjkBxkRP86ArHDeR71l7bJuz7infW5xAdK2Ix-26Ir7cieZKJFxziJUKJN0qOKPpEi3Vz6_KuiX4uAKttiOga9NtuWx6YVoOKe116ROA-ezkYp1SONPoCPsdf9a5t3nsFwjxw2rA1yzwu2fB5xXfWBdZrgVbHFOfInzhRXVOS301r_LXj3DdaQRsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26666" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26665">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIfcEXAZ8x3r55Z6QkX178GJTh15ooADCONGIzV2121kHvRpa-j3hHuE1ykW3c0AM2y0thGs74jVdWXItagU3tzCkgGy5mrNMaREOMYh08JfkVQyV2t4wiwmLZarLfJ915K_Sovifh2VbxnCyhHs2cJ5d167STaD-xxVbe_kwoPZEnp6VSXsdl_5QN87cRzYOSeKdxPlwL5Y_W3Q0hotWoUYWp4O2uYAE2IawiuT8dT8yB7Kf7LmwiAxTZWePc0hP22cW5td1WG3Fjvd_EXxCHJ-C8PWIjxOkLk7rKAIUJCVkR3SCMUPcgyNbpw-M4IPZHFCGLzLRsxKjhBRzdk2QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
#تکمیلی؛ محمد محبی هنوزآفر ارسالی باشگاه پرسپولیس روامضا نکرده و مدیریت باشگاه پرسپولیس نیز همچنان منتطر امضا قرارداد توسط ستاره سابق باشگاه سپاهانه. هرلحظه که امضا بشه سریعا توکانال پوشش میدیم. توافقات نهایی انجام شده و فقط امضای خودِ محبی باقی مونده…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26665" target="_blank">📅 10:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26664">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikDbz4ik1D0HCfuanmEtAV78w1q1OxpY-hvSFN3MpWCtDUqzRRDC9q_-NIMBT7-D2aOPcS_bBu2cmRLmQaX_11fHejNA779IP6onUehTsiEq-xDWnJvgsyFGvDm6lxI6c8t360BJSB21zQQ-5njoQ84v-TkCDuRg5a_XIahYVYsAIdDJLdZB7d_G2svBmBDu-WUfdJZE2cZz8jcHq6C7ChWjFmv8pRa1diskDWSmhtewUO-i4dMxT0HPhsvqniAlsZmhuhw97zurISzQdp0HAhVjTO73Y-TqiXsP_CIwGME-rk_OlelPrA49L0TEOP4azb8ru7MDPvmphkzhoe6uhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام رومانو؛ پائولو مالدینی اسطوره دوست داستنی باشگاه آث‌میلان از مدیرفنی تیم ملی ایتالیا استعفا داد! گویا قراره از بین مانچینی و کونته یکی بیاد بشه سرمربی و مالدینی باهاشون مشکل داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26664" target="_blank">📅 10:22 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

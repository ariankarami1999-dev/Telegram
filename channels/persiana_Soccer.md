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
<img src="https://cdn4.telesco.pe/file/hFKH2Nz-yflLidgTchok_cRdkvEConDCDdA348uGclv2P_bDvnS8eFCYGuTsSk2_IstKp3pUbmROw0I2-pBMCc0Rn3bca8zZvorWuBJdoSfKhDlswVy-RHEUiBfMAGPaZqjieuo_AjvEM9leLphhZQTkcwtvsaxF_Q1qlQECoakTm2je77zzhG4eukLFIsA9xMnfBMZ9lirbbzYgdBRVnL2Mt73AzR-gL5ox_JcjD6I5y13h0xL-uvysOWaK2t4PqrQu-YUYN-OOhlRcJq2MEVq3kRzf4Op-Gx_eElwTkmQscNkHVh8qNPfOsFVBxwl75z-SBqfdJpp0WgtvMKFSjQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 407K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 03:28:57</div>
<hr>

<div class="tg-post" id="msg-25055">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezbF-wfGTizc4k_nRacRBGv9vO28_em2XoIf65I3HwGAjD2uu2fB5V_xd3PhH8LkXbjP0HnnT5c0v_sJuxKBxDUfvIyhcCpIc85U4cJxplo95VDgHs-EAoBNJf8MLZ-Aupfm0MB0mDNrMmOB3m9EEUceMejj4N7uYFmlDlYC-3-wXd4GsoRaQ48Qy5KzgBdBca9OWrHwJBsYmLZsa_jGUZi5J7A8sqw-AFJ_wM35EkVuH06r-e4KZwb9aLIyAtYGTP0Jyp4_0QNmlUa8gAS7wRKyjKyoGtjHPnyI-UmY5y1Q7RoIJIPbW0SQK3swFJ7EQ1KgxzrUwI3-WVo9o1yLiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌ نهایی‌ جام‌جهانی؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
مکزیک؛ ساعت 03:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/persiana_Soccer/25055" target="_blank">📅 02:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25053">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XjCwyTkNznSDKuARCjAVaMLHtytHwA8wpS7fdwamWGiKGhMZsEcI36RPk1TCGNBX9YHKzZwHa0V73wYQN4wtJ9hJw6O0ZHcJ5TmKvN2uNWFNC6fk9LmUoHxWao4wOIHBqBMSEZBE6XPBMtAdvB4kN_4oaZBzoqgW8cE1yuXCcpxraNzcw-3afm3He8iykXf7hzABF_nY0XkJV4c7C9xu2qsIskQG8gedEtL1qk-RrG447oqfFVBUeVlgwyi5KOCJoPRZrdQYVw6Iyccto2r-SJsVTC3287-fBzgV7fLIbEU5uLlTQOQYxBXb9sYSEVdsUjdqMK1CD0vzZIev1cykNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OyifKWL6E2h6VxfCUKDOz7cu0hdxzQWy4TrM4_tToZM3rOe-zaIU53BVfvhDfgSK8yiLyLVSZKCdhFhRtUQ_lCOxi7ZhugvgdDMTHjvtjbgrhgypOI75f0JC9VreRdtAucmBG5oGAmsHerfKQStYHIwQKPjqT0HZKKqZKm0GFuKnhB0Cai4XFo3dMrgLrDp3b-QrUFtdSdjp_jJdeV3I_wJhQoWvkcXGKXZYuL7AY3pxHVvtPQxSdniWAowskuUOFR2hZgfAGGr10LwhoqIqPU0OuRn_f7MrpmeP7ZtFEHNc2TNdJ7V0Ekmrzqs0dCT0y3ulbij8HbnamgC8Kt1dzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛ از نبرد خانگی مکزیکی‌ها مقابل انگلیس باقضاوت علیرضا فغانی تا جدال فوق‌ العاده حساس و تماشایی یاران رونالدو برابر اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/25053" target="_blank">📅 02:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25050">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOwRadaQs68PdMnpznZ15xL3h-pLRQ77UUX84UcUNBC1CaI2Xpk7wwKgvatjIg3Kb72M_aZsVIEaRu6xgrysPxVDUol5wC0dItSsL7oRArEXfepThNIlTm7J7CuqmLdV15PnKrLULhkceuBWNuoIlWCN6Oelc5qtL-291dzKASCybkuSq5-me2fB0x4MyhuBju856-lGvF23hHx2ipVqrHBPU9v5KRKZ9W_frW0jUslkw_PtyW4QxulsCshtjO1t3zW8GqHUVZg0R668zNsK6FWix-gLNcpPKlBNypqWmwiLkQMDjy5O8DLB2EDG-YmpnKQJtwQbBvPvSG70zx-mRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باز هم ناکامی تیم ملی برزیل در مرحله حذفی جام جهانی؛ حذف سلسائو در مرحله حذفی شش دوره اخیر جام جهانی این بار با کارلو آنجلوتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/persiana_Soccer/25050" target="_blank">📅 02:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25049">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6DJnk2gxAVJTJQNMR2PuRzvMRt78mE6270QkWDnMz7meJobUlH4d5biC0UpUv8yk6LsuYhFkOuyForfWTazGkDH_gn-52yiNq-07p82Qaw4d_c6AN23OdYOHhwW3laNxukTMRDFf4d8QsJVz195le2s0nQYqrWZTHQ_hPrkbNQ40KvbxcFI6gTjwviU5npkOT7fsFmkMN191IIMQ9SY7E7Afp7aUEfG0pZxbQ4DxgWqKE5fl1z8Avpa464Z_NTc52vzcSg6CrS1DqbV45crM1rzwVt0YkX5hgCEuV_TLf8Mj4Q76XmQQ-DAu8OojzKbx14Z7lOl7-AoJJt47q3pUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای تقویت خط هافبک خود؛ احمد نوراللهی و محمد قربانی 23 ساله و ملی پوش رو رها کرد و قراردادی 2 ساله با پوریا پورعلی هافبک دفاعی30ساله‌ سابق گل گهر و تراکتور بست. پورعلی درتراکتورِ اسکوچیچ کامل‌نیمکت‌نشین بود.. پوریا پورعلی جانشین میلاد سرلک…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/25049" target="_blank">📅 01:55 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25047">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBasClq6XbwDz4j6oOT13lPl59dnCup1AyBtryA4YZ42TqUefvfJfzacvBEAxQx-NIYldaMuByh8aImxiXPjGmhdSS1Za9idWkNqdnZOlkML9_IElA_ebVdJesCBQfhkBxIUX07JK7C1wJdQi97s9SDUWU2Y-xxW8tlOvn0ujW5DAcZ3HX6dlco4lMEW6y2-G-iAltDRe_WQz5XSicYffgw5_lg0NZ8zT4u0BPZKQYyTg1HiDVqm0vMPQyBHKcVTxBYVzS-0BXygOdRaPijDQAZF0jb4zY3glSZQ2z_TCJGqWCSvU9ltgCNNBOzJ3twa9e9aRltnOYYvt06xRc5X2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
از نبرد خانگی مکزیکی‌ها مقابل انگلیس باقضاوت علیرضا فغانی تا جدال فوق‌ العاده حساس و تماشایی یاران رونالدو برابر اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/persiana_Soccer/25047" target="_blank">📅 01:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25046">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOuiX5F357n09IGptZGznhOlwtcTyU9XETNJOnOLF0Cc5P4OAThgoRntoQ50TmtgvcdX2qBLAkmcVeIL4AkWUFGR14V4TfmRZaNIHYWLh2FnOdffzw9KwZguZt4podeKWx3r60TzXdwWWewSo2Z6cvfc6AA1LKQBya9cpW2QYqauFdzWFeq_gBnXF2_kigZ_P4WDBRXXH6aq0DG6E8XLFrjeUEnwWyd0p8-QVjkdWEor9eF4Ave3jD8lgrpqLJRv_i6TWYjDYrdRwz48yMXk4oWdeDYgQHuNWCsVDoV0TGlFcY_IxUTBkpHILTHLqHFbICvLUVr2StJ73RgEogcj7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
صعود فرانسه و نروژ با درخشش‌ادامه‌دارامباپه و هالند و طلسم‌ادامه‌دار تیم برزیل مقابل‌تیم‌های‌اروپایی در دورحذفی جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/25046" target="_blank">📅 01:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25045">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLR3ZTR5S8AwUu7iOb0WNf2n_t1s8c_Q_xs0qLBGuDvWg1JmrFRdadYmMWqY53WVGDqSkdXsDncgw3GIZXcOHYMOmLGIdznt4yt7ePIaJk0ox7PtDhhgZus5D5TTjj_gyPnrUfMYMEDQy2R6NXvHozTvJEvl35EQN9QaFbdDEcqG1ShqpQRmbru4JqzoY9TE2aH8wh1eMDCR2XiUBOJWJhXnfHVGWDt3LfIt3TXF2RDnnlDw2XipfnXYcvhFl0HEEUeaPUND2WAO5toCuvmubie9zkuNnR4He0epHV-YP164ctwtcy17RZDD5WHrq5XSMiBOML4QgOm030WA6vasxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی2026؛حذف شاگردان کارلتو از جام جهانی با امضای هالند؛ دو موقعیت دو گل؛ هالند یه تنه نروژی‌ها رو به مرحله بعدی برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/persiana_Soccer/25045" target="_blank">📅 01:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25044">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇳🇴
خوشحالی هواداران تیم ملی نروژ از صعود این تیم به یک‌چهارم نهایی جام؛ نروژ به مصاف برنده مسابقه دو تیم انگلیس - مکزیک میره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/25044" target="_blank">📅 01:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25043">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6zB4CHwvHSeNbj1GHugnGlPjeSVJVtNiejdrSfxGx_rsduzPSKcbNn5beSX62kYxBUv7g3TbVwO6N9BdaF_SBgOmtaawEKM3XQ3cehlI0OoWf9S6sYoz0LWui8o3BRcLKy3HY89V154hcm6Tq0vpsa3n0S1wsrLO2_lbph_XC4vlKO05fWSEIOnAAGafi_mqobpgUzrhvyjV4AyleSY8dbgEOQM8SdISmfnxEivSDz-oflmS7XcpJ-sGabkVmiK2lNxpHka7mh33uWeqMNiqdjEgrMWNFCOGycQy-r2ELS-Wo8v8XnAyy7TT8wJkADFvq2g2rYRouywzFWPhKhyaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی2026؛حذف شاگردان کارلتو از جام جهانی با امضای هالند؛ دو موقعیت دو گل؛ هالند یه تنه نروژی‌ها رو به مرحله بعدی برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/persiana_Soccer/25043" target="_blank">📅 01:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25042">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2de979c355.mp4?token=dQI154Ao-2t2uP0abTAHUj7tXGIUsWr_ZBqCbIc7I2DI8Wlmb1mpqKaAOUIb661ydz8eD8kVEoQIJFWoiHVE4OvMyCDYGJnJHc1rdvYvbrKjhga7RRNJPaObs3b_P8GyCURxf2utyD3XpwuYI_hYjHnJWv5E5uurKgqrnBT-NtNA_1DQRlfdBkq91SPGjxgegd_lXch1Lap_VAkPb7EaaDA9jCWAngUMk6aMiTjM1IMh0PBYKXtYIHgCmhIez_GgogY8EmTeBLtdBPV-IP44osW8uZjKqcBWIzQZJUMaYTnGQAPtCXABS42klkSMeWwhiCTNNZopMeYGX-EAbeJeeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2de979c355.mp4?token=dQI154Ao-2t2uP0abTAHUj7tXGIUsWr_ZBqCbIc7I2DI8Wlmb1mpqKaAOUIb661ydz8eD8kVEoQIJFWoiHVE4OvMyCDYGJnJHc1rdvYvbrKjhga7RRNJPaObs3b_P8GyCURxf2utyD3XpwuYI_hYjHnJWv5E5uurKgqrnBT-NtNA_1DQRlfdBkq91SPGjxgegd_lXch1Lap_VAkPb7EaaDA9jCWAngUMk6aMiTjM1IMh0PBYKXtYIHgCmhIez_GgogY8EmTeBLtdBPV-IP44osW8uZjKqcBWIzQZJUMaYTnGQAPtCXABS42klkSMeWwhiCTNNZopMeYGX-EAbeJeeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی جام جهانی 2026؛ شماتیک ترکیب دوتیم‌ملی‌‌برزیل
🆚
نروژ؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/25042" target="_blank">📅 01:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25041">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae7cbb0612.mp4?token=ReWfvu945k0EcrKuNAb_RxpLxjSOhZ8-dMNGfQFaQsKohZmZjbPIvUOsK5-8cY1HqVrkHa9jlBnYPZWGskUSWGO9X7FF1lio49IM0hlp7q62gybbpQhwstlWIC-bSB1-GJxeoi0ZMc5Q7CkEDbrFM3QiYdFiJyzok_RTKzQlSUgwcESSqwcPmrBn5VDhLaEGwBYpcLz9-vJfC5Zy4WeJ44YigryGPzKNYj6gAy_FfJm6_I222mE9BuzqPSbbgivrltJWrR2GMWUdEBOwb7wf1nDpyEIM7ADnRMZbqAYf0I7__PRKnQjhwN4g-r8vtle47FeKmCk3jub0s5tACbaezg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae7cbb0612.mp4?token=ReWfvu945k0EcrKuNAb_RxpLxjSOhZ8-dMNGfQFaQsKohZmZjbPIvUOsK5-8cY1HqVrkHa9jlBnYPZWGskUSWGO9X7FF1lio49IM0hlp7q62gybbpQhwstlWIC-bSB1-GJxeoi0ZMc5Q7CkEDbrFM3QiYdFiJyzok_RTKzQlSUgwcESSqwcPmrBn5VDhLaEGwBYpcLz9-vJfC5Zy4WeJ44YigryGPzKNYj6gAy_FfJm6_I222mE9BuzqPSbbgivrltJWrR2GMWUdEBOwb7wf1nDpyEIM7ADnRMZbqAYf0I7__PRKnQjhwN4g-r8vtle47FeKmCk3jub0s5tACbaezg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تشکر دونالد ترامپ رئیس جمهور آمریکا از فیفا برای بخشش‌کارت‌قرمز بالوگان‌مهاجم‌تیم ملی آمریکا. بالوگان حالا می‌تواند مقابل بلژیک به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/25041" target="_blank">📅 01:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25040">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8897e8ba1a.mp4?token=tAVKVAEDXOtOZ891S1ZkQSLfR6OHy_fFVjy3d_Fq57U-6aUXeO2DZ4lWLWubEk6TMJ8MWWKqgICUtQs3spWjoFoWSfAWImNfS2-mPtlRPU0QfEScRKGb0KzRRVfPpIxehi9QW-ktW9WwxwknmDbSi5Q4GGv658lVYuNDYvdKBTDkw128b_ic5fL_H8Z5GIjb8PvRElobfwP30ExrRRJjfUnTz9Zo_76l7-Fiv72oR5s9BIRC2rzC74mUI2gnSNC40ex9aIN3M3U8n9m1imiYQ19B2kSB5rvMJtzE1meTiBEnLbdP-enhmfNvt2-Q45_1tYYBkSn0DuQox-Kzogx59g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8897e8ba1a.mp4?token=tAVKVAEDXOtOZ891S1ZkQSLfR6OHy_fFVjy3d_Fq57U-6aUXeO2DZ4lWLWubEk6TMJ8MWWKqgICUtQs3spWjoFoWSfAWImNfS2-mPtlRPU0QfEScRKGb0KzRRVfPpIxehi9QW-ktW9WwxwknmDbSi5Q4GGv658lVYuNDYvdKBTDkw128b_ic5fL_H8Z5GIjb8PvRElobfwP30ExrRRJjfUnTz9Zo_76l7-Fiv72oR5s9BIRC2rzC74mUI2gnSNC40ex9aIN3M3U8n9m1imiYQ19B2kSB5rvMJtzE1meTiBEnLbdP-enhmfNvt2-Q45_1tYYBkSn0DuQox-Kzogx59g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
کریستیانو رونالدو:
خدا کنه آخرین جام جهانیم نباشه، تا شماها بتونید بیشتر منو اذیت کنید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/25040" target="_blank">📅 00:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25039">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bN2QZDCldUxwwAKczOVMGN3hHuzqSlVb-47SmgHKws3yktCcWRmEXUrIOhZkarsiPk0C90IFdaulaMMwsieB9HmBc-iwuGI-g4bz0TF6JBJxGR5RcPljpC7nPsv8dl7vApXmN1OP7l1-fvmkHn9sKS8rycsUULFqYN8htKJhb3pWp3krxr8JBE2klbHzcDPgLNSUyjk5Emk2lZWyCtj3tX6OqyX7qD1ZAlaAYgUjT9q6vXNixm4GanXax9Rb491Dj2YxZiH8h_AXJEkAQtwJLeW20UjoRZ0VqFKa82jdmRSkpXd1B-lCOR7SEfh3flld6zMHMoJIEHgEg80U0hDYEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇳🇴
پدر ارلینگ‌هالند ستاره‌نروژی منچسترسیتی:
شاید روزی در آینده نچندان دور هالند رو در تیم رئال ببینیم. ممکن است اتفاقات هیجان انگیزی رخ بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/25039" target="_blank">📅 00:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25038">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_HbwJa9FJJd43b-bucxF6WymmUDlDSfNco6k-TlCYknOk5YuCtLkWYCqjkXYtTr1E2SDURlFaa1tdf6rFEIh5jPb4kL087VJJsTEWFPDOga0KsuvBEWlfqr4bMUricS0lhK09L3WO5D1AmZZpHQG_eoMC01jehnoJcuFyINhysNCReJ36z9SFYlkvJIS9D9lJS-b9BnjWLhsLsEtPtxzIhSDcXbRotpp9Nsp-RTMtOcScxDuZAQlsDKS1EbLsDk2HANdky0LqjKjyYxPqSAi5-2016NcsDIFzjv7EM56nUlpfbi4OX--iZKHjQgWG0l92aGUKzAHiQT0ruCYmovfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ کارلوس کی‌ روش در بخش دیگه‌ ای که از مصاحبه‌ اش به تعریف و تمجید از مردم ایران پرداخته و گفته من حدود 12 سال اونجا بودم. اگه روزی ازباشگاه‌های‌ایران‌پیشنهاد رسمی‌ دریافت‌ کنم ممکن است به‌آن‌پاسخ‌مثبت بدهم. من برنامه‌ای برای بازنشستگی ندارم و علاقه…</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/25038" target="_blank">📅 23:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25037">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhGuJltbDnlKiRqVBguHR60V4g5lbYYnEyTH3KvoiqLW3rrPQ0zkv90C-1TVpeg1Em5EokdHWo-IiMe97gzlidrA8It4u0ftfoxpX70c5tmIOQi7C6AH9rHOmxHiPDpRQpdbA3FsKNNHl33rFu7TX49OeinW6yIzUchfFyATzaNXNT-Euxev9eANYovRFsZALLWNLbt5oIaytKElrOPo-wXNAj-qlzHLLnxk1Rh7sFU4UEoKu53umOw4P2B7nYuQqchMHGcdeDYUj_wxVSseZXu8_NnkO89_QCNAlogP4lRS1paHAK7qVsJjyYMs2F6oKlrImPTk3Ns6KoGibhGb1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باحذف تیم‌ملی‌غنا از جام‌جهانی؛ به احتمال زیاد کارلوس کی‌روش به زودی قراردادش رو با فدراسیون فوتبال این کشور فسخ خواهد کرد و جدا میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/25037" target="_blank">📅 23:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25036">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81c1096e89.mp4?token=csQvaxO3mwPUWmNP6yaDUhGgiAX4oZMZ_-flNZPfCKBFkJUVC_gB0QpZEp2JcXEqXPKUBOMh6VuQDJeQFafOuCWEwzTaXyjolPwEpaV3FXeaJ7JfzwKNzncqLhaT9gGGoT3n-e15bahmyo4g1_TqLSf-RItGDIdGx1cF0zdtFG1mDgnjAEQDUnjPs7CDyal00yRVpHar_UujW4dEpX_ugi9D3nPuoub4qeFiTND_UiMh_Omjcs4Y4AMufRml1IGVmkVToBrJF1LT-uKWuV4qVHXhcciFbJ3YqsKoIbii4STbZW3-D2rD_q6OvcoWkHab4ZlmRySIyz17FmPc2wjuk21u1gskEiJw5POCoMDjcmPGgS6OR5QVNP0zyHQ6V51MJ0KzJzOINUTSiMAQoIRDJ3r9GE2u91juvge0E4zawHQjFC9FKPg4qWvlPYs2vcTu9-p-5m15mjh_9V7J4gd5g2-nGPZwuGva8jS4UKtwufIhcQQ88xX5xIl1CJZ2PHPDDYIueOm4m_DCmIleG2ROAn5QfvkYyQbu7SHwFCjOcHgZLaqt6sHnL1zeXB7YiebLMmFz0yU9-C0Fdo079krTp5mkWHBsuOlHhmFp1-YAfXrg9sciSUl-loj1pFhnnagpdRqD6-A9AI2bzHMj-UTGkFMDDAmc0gE8h0rBXmicJY0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81c1096e89.mp4?token=csQvaxO3mwPUWmNP6yaDUhGgiAX4oZMZ_-flNZPfCKBFkJUVC_gB0QpZEp2JcXEqXPKUBOMh6VuQDJeQFafOuCWEwzTaXyjolPwEpaV3FXeaJ7JfzwKNzncqLhaT9gGGoT3n-e15bahmyo4g1_TqLSf-RItGDIdGx1cF0zdtFG1mDgnjAEQDUnjPs7CDyal00yRVpHar_UujW4dEpX_ugi9D3nPuoub4qeFiTND_UiMh_Omjcs4Y4AMufRml1IGVmkVToBrJF1LT-uKWuV4qVHXhcciFbJ3YqsKoIbii4STbZW3-D2rD_q6OvcoWkHab4ZlmRySIyz17FmPc2wjuk21u1gskEiJw5POCoMDjcmPGgS6OR5QVNP0zyHQ6V51MJ0KzJzOINUTSiMAQoIRDJ3r9GE2u91juvge0E4zawHQjFC9FKPg4qWvlPYs2vcTu9-p-5m15mjh_9V7J4gd5g2-nGPZwuGva8jS4UKtwufIhcQQ88xX5xIl1CJZ2PHPDDYIueOm4m_DCmIleG2ROAn5QfvkYyQbu7SHwFCjOcHgZLaqt6sHnL1zeXB7YiebLMmFz0yU9-C0Fdo079krTp5mkWHBsuOlHhmFp1-YAfXrg9sciSUl-loj1pFhnnagpdRqD6-A9AI2bzHMj-UTGkFMDDAmc0gE8h0rBXmicJY0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
درگیری‌رونالدو بامارسلوبچلرخبرنگار برزیلی در کنفرانس مطبوعاتی پیشاز بازی پرتغال-اسپانیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/25036" target="_blank">📅 23:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25034">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWPrqp4fHRXz5Kj2YJ6UeZkkO6WIKR-kqToVY53GmPD0Nk0mzL-9Nbrx6jarp1Y40UiwVRC7Up3qkL1I5avA36spCZeJvj7SojlV_iwHIFqn1GsgyPLgfRDMil2jhdp5yyesBcHfWXEMpaH-GjyLaajRfLlL9qPjF2KIMoLSAzlRIRxXebPJvhSLa-Cq02rR3W2i4jjnnrOpLDOWp9o4yHsaymI85lpNAst65a1Ufc7tboNM6edWhfaMndKm7tlXu0iUdoW9a2CjhJQzOzIHl3BfvG6E7-eoSvAWe1kPXNIqpYC_Wj0wOXwaVpESUbRDBq4wsskerhs3uEUY10-J1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ علی نعمتی مدافع‌ ملی‌پوش سابق باشگاه فولاد برای عقد قراردادی دوساله‌باپرسپولیس خواستار دریافت مبلغ سالانه 75 میلیاردتومان‌‌شده‌است. درصورتی‌که بانک شهر با این رقم موافقت کند به زودی پوستر رونمایی از مدافع جدید سرخ‌ها…</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/25034" target="_blank">📅 22:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25033">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHHcjTpDYzkXUslbWD4YCSalGrGAxziDGRga0lxLvGUzCbdbX4wdo5SCYI_d6eFcWk9qmZv5a0x3Kptr-lNNU8IHjJ0iEZySaVkE7s4ocOgrxkmHuzJt4xFPpShAumrlRVlAVyUmVEFE2ziGh6VZVXKvmPO135qkCcghvP95FkDgA8QM0MpmU7xBasPKJCxcuJ3MQDmPkUM0dDi8JAVm4Lytls-vV8Lft0BYt-Cx75n7cyJ31XqdsY-xHrFRACf6XWYpIRaSQCSUcjD0iO4BF6sp4wT0ZBOxAfGUncKa2WfgV1gb6n6tYg8UC1hDrVvS9HdLF-GzWotkpUztEL48hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی جام جهانی 2026؛ شماتیک ترکیب دوتیم‌ملی‌‌برزیل
🆚
نروژ؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/25033" target="_blank">📅 22:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25032">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UB4OS9oYQ_TBSardgNxr6uQwd4Kbis2-n9LU8LsClg70zaFsy2CAZUClBsjOrG8Fhg3MDXkMjDCGUgqXBrVJkAMzqJbxksJg9ZhEm0oek7l0clo2yVyTFY1fFwPM6B9mw3Iq3JDMGCXV8Ju7PKC95ZysSld049uMYo24TyO05IE8eWMMfbQCroERiAmZhaP7RHsuMahXQJOAblpfhCqwSNgoDRCoSRYxRVBvMCYJW2iaKAV9l5I2xgLgKMErkGlNcJ8-Z0TLYIxot1AE2GJUdBwiJmjNGa8DEg5klXBPTUG3P_wnV0WCbVpkkwml3BuELKAuHixwCd69xpQB00pOcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
🔥
بلاخره انتظار ها به سر رسید
🚨
👤
نود جورجینا همسر کریس لو رفت
🔥
👇
🚨
👈
گزاشتم تو لینک زیر بگا نریم
👇
https://t.me/+wYDPG2ky70AwODU0</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/25032" target="_blank">📅 22:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25031">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsfiaf36fr0_5dLOzP2E3Pub_wZTotim-ro4kfPk0yDRbmbNL72JyMI2PJBSIrYgim3kUZoOzJYaIl-Wfp6w_KOeKGq7DCj4Gi_MNLajKqs3_XpaJlb6uCiZCqk8MJj4TMLJmDubuu9rQXCL3GeiLNPpvW3os2uGFd6BW9Jzcuxd2X6vud2fPmn3Lg4z2IBNj1BM1bPSk5cqJA7dlc7NtZWGGb4SBRqgYAofnmZIRmz58rDaPiNhb51_6PodyM8fxEtMB6nEiUUNplSmhp3m-k4y8b3MPyvl4lLw7U5uzZlxERp60CoxMAxQTeT3B7uFW37Z-wIVzUAVxs7CfruH1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای تقویت خط هافبک خود؛ احمد نوراللهی و محمد قربانی 23 ساله و ملی پوش رو رها کرد و قراردادی 2 ساله با پوریا پورعلی هافبک دفاعی30ساله‌ سابق گل گهر و تراکتور بست. پورعلی درتراکتورِ اسکوچیچ کامل‌نیمکت‌نشین بود.. پوریا پورعلی جانشین میلاد سرلک…</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/25031" target="_blank">📅 22:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25030">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDr2qSqbZ3yhciZGS9DicjioVS_5gSwy2nNqQNhL6J5QubOvJtdBnivAv4qA81fVjd1BIINgovDtOBlw8n7Asg6GkJFLEcngUh96odGSg7C0ZCHhDMvpviA-KeopLdrWDiDPQAARwrI2UabDmLooEHZ2LvD70qfDi2i-LlGudGf4r1Nb7CmDKb5gN4A27WCNrmCZNZ7lfxS0W2Vwuuh6FQoEUH6Baq5-z5SB9_X8O8n0r_gisqiOFyaptkmflYLlx6TCYbi6YU-EIZNsd51H2HojbNIrUtEf2GsuPUPZcjEbCUbd14Xh2LyviNO14zmV9qHfqaKnkxgWcL58qCNnFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#اختصاصی_پرشیانا #فوری؛دراگان اسکوچیچ سرمربی‌سابق‌تیم‌تراکتور و نماینده رسمی‌اش از شب گذشته بایک‌باشگاه‌لیگ‌برتری در حال انجام مذاکرات نهایی است و به‌احتمال بسیار زیاد فصل جدید او رو درلیگ‌برترایران خواهیم‌دید. مقصد جدید اسکوچیچ فوتبال ایران رو سورپرایز…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/25030" target="_blank">📅 22:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25028">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uQiXVQp-dAdY-cseqgXdrJirXhOsw2rL0o2XKN3qaUvcb0QxWz1kpvJ7kNWWZyzvoJ1JRKD03ai-Um-ow_A9bvMEjvsgSfFu3meBppUdWlNnj_u60zkLW2nhnB-bAikPk-1PHrftX7rfqJh69Co8SB3aULcsxjfbXWtLKNgrEw51ZqwUQ09TvEIfY7wqZEMh0n2iZ9MnuvZfqhxE3bckTK4KR96AFfDN1UGEuYRJcJx8s9SrSlEnPmEQD5oedRstk_b3RiSau4idN_AdknsaYSkelhcyFdm43zvP4JcpWhYmim7Cq_NdnOeuLPg8POKHssDUVJpic_yfzfkeI4suCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ALTWGg1Sg-37orXPTRTw-MK5HlDvxWxFqhoq5DVnkLOH-D1RA59hxheE7q1xb0TGhxhz-_xYTPjer1_HKtdvdt1Jnhj-XH5GV0dGiI39OSrRpiOdhKA483_F2lxvreZpvZjHQ51PUs2hYnA5tSgRGqzRkRNTKEXdxRb9TU5JNkHHjEKgdhy_NPPHThnghJMPSGqUbId0QYxXNROWg_pSf_vDp5l2Ztd3Z11XNqxW4CNhRERWomt9k_ee2GM7i5ZCweF-97mVoS-uZ2D1hQojxPaY5n-0bLi9mPFYTvrWSid1np6pRYpYkKhEw4u8Oxl94qnpVk6GrWdjICRBNogdEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی جام جهانی
2026
؛ شماتیک ترکیب دوتیم‌ملی‌‌برزیل
🆚
نروژ؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/25028" target="_blank">📅 22:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25027">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWbGRXdQNz_gWibiAp3oK4cAzfo_MU3vTyqxbD8S4Zkekg9YDWUdcTOigkN3-oYCXVamOgk8pou0O93EanwZmU0RiOcQ5nupcHWp3sOMGA3G3h6mc2cBwluTkf1omxi__UDt6sjNG6MWOj1D6seNIwiRe-oHilO57VH0qfWKr68O-y_LNLlkbfH4_0lWOHd2XiU_WECPUyW4AogpbLOGCvWSPpWsuwUpbeUwQ2AsmQXTFJl7bPVwiQOgiTHcHTc_spLyxcUJ-HG0OEOIqa9nzYcXrqckHMqP33yLyHBRtOZQuqoZ8nU-XxtWXj_EhVAiZTBNXBvYpcJbZaLNzzkgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
تشکر دونالد ترامپ رئیس جمهور آمریکا از فیفا برای بخشش‌کارت‌قرمز بالوگان‌مهاجم‌تیم ملی آمریکا. بالوگان حالا می‌تواند مقابل بلژیک به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/25027" target="_blank">📅 21:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25026">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ni4EqpumGxf_4WO6DHWETIWTXl-ixxMIHWbfh9K5yIzopLRq8m7Iel2B4R2XJ_YQkzDtzZVW7jmBrY8gcvqvkNe4rkIfv-wdY0keuX541CIzU0jaYoKPCeC5GIjchbWEmnaAqbQ2UfAh9X7JK3iF2yriOw-Ir3JMAvt0XY8YnljrKv3O4xfDNmtgtKjdvSIR3UafQCOtOOuIaMAa4wMwRQzl18tJQwjle2CjQVjDpaNnwQXb8vjW6gXGpidiTsYoycxApuivp9Y92jH_fZEOp14qQ4oMgoesWOZOBaJ5nIW4sLywCKqlpb67QPbPcGxp2we0HZ-AX4BvW1b8ldYV4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اقدام انسان دوستانه همسر رونالدو؛
جورجینا برای کمک‌به‌زلزله‌زده‌های‌ ونزوئلا پنج تخت اورژانس به یک بیمارستان اهدا کرد و ۵۰ هزار یورو  پرداخت کرد تا برای خونواده‌های آسیب‌دیده غذا تامین بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/25026" target="_blank">📅 21:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25025">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmxILp82VtwEiRvr_2I-93QhOy2cBdb-1bN0wdQVHeNyTcOtUWlihLf_KiJi3XoEOMdrYPLCbsliXh_JeJO5DwL8mqu_vX5l1MHFpv_zTcFD6-7hoPwQrIZ46FYSzyKlg0Y1sNvWks6qZVoqFoj6KLJrnQX742FdKdN46KarJc6i8SnkjXKEX5-9q-z9gZzxW0SQnaRCyUW5QiXqZ8OmTBcDvxxh2z2pkDEu6kuv0YIvxainnFrcGtrXNyjAAIORI8SPgCOtgo3hmng1iBLb1BRCoro8kd4CTTRsjsH0W48rqQ8cUBpQVKhljIq-jyYgk6vYkcyV7EpDMqKa3021jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوراللهی نامزد جایزه‌بهترین‌بازیکن ماه لیگ امارات شد؛ احمدنوراللهی‌بازیکن‌ایرانی تیم اتحادکلبا امارات بهمراه مهندعلی، تادیچ، کوجو و کریم البرکاوی نامزد دریافت جایزه بهترین بازیکن ماه ادنوک لیگ شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/25025" target="_blank">📅 21:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25024">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hn8GotJOuoA06MNofoTdGrcKO8z9M6-3-GOViPUmCdKWSAC_vAqHm2FdDU0J9zC5pHGCa3frZy08z5G7NqbKP6YWxDbGTypSeFwfSmSM-uN5YJ8XP7Vq8InF7pXUPEXKwJ6DL3up-MZ8kYf2ANqejX_lMajF8mQ924VDAEZw2_iygs0AghLIBriH_CcNrVXaO-hSEyraaLZvR9C6YjOu5YLYn68wnH-N7Yysj8hYHOxqRZU4sS62whMopp_Q6elboc4d5vrAULY4_AIAYmgA-TGOP4mlACE6H2gjRK9xWppeUa5LJ5w5fvuidr6AXTBeGR6OejDY1pFqPT2vlubzOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مهدی رحمتی سرمربی موفق فصل قبل خیبر خرم آباد با عقد قراردادی 3 ساله به گل گهر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/25024" target="_blank">📅 20:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25023">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lcc0t9k96vliflTKXIpVxoCqQCu1BB89jGCjs0pEvKpmlVbRwhbLy5PCPUfJFU4ZBJqh8U5vl9CstWz4oIXsGMr-3Zvq9dMEUEK--oFIe53ZyZMA9dpXW6Yu0BHOQmzu35s6sEvLelr7Z5uYpXMAYqmJ2jL7_R1BCsAWpIHSJ1fjNsxnnbKpx_qj9JZqtkxE5VslfVrXC2DWHQT_M7am_JDha5GMK1xvjf1-X3dbs07tw_B4PXDG0HUdVQGtkncc2hcFHTCdh8IOOoowsByQ4Zf7Uw8Vyo5mUuneAMEd7cri3f41KQs59EMgyI_p63IUIrHFugf8t4nxi_x9uh6PuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مهدی رحمتی سرمربی موفق فصل قبل خیبر خرم آباد با عقد قراردادی 3 ساله به گل گهر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/25023" target="_blank">📅 20:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25022">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9652d5ab0d.mp4?token=irfEk36vfg0kebpPfkuVUnibF25VbsGLjkBuFItMasl5QBmlhA8FH_GBN0HJ_0g9-TNa8ho7LAdwNkT_g5XNUdPktu4Cpn9TFTD7iwJGr8_uvO0xRjrFYkgkqLDpLrQFEeb3NhXK5LPWFa-YPY4bEvdc6lVtEbdHvUcN5uVypr-YvfMPD8s5IrXsdN9WkqYgYvY5iQDS3Gi9tF8xw28_JBWjieGa1C639O0DDEqARRfqrKNivtD7mEU7zXBb7wZFcc1bR55E8zgrXEgXgzAyk1l8hEAOFAE7YwqVouwqpoKxnBd1NtvreJP-H_y_rWT5tr5vjQMcMLkW-Gasamb5JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9652d5ab0d.mp4?token=irfEk36vfg0kebpPfkuVUnibF25VbsGLjkBuFItMasl5QBmlhA8FH_GBN0HJ_0g9-TNa8ho7LAdwNkT_g5XNUdPktu4Cpn9TFTD7iwJGr8_uvO0xRjrFYkgkqLDpLrQFEeb3NhXK5LPWFa-YPY4bEvdc6lVtEbdHvUcN5uVypr-YvfMPD8s5IrXsdN9WkqYgYvY5iQDS3Gi9tF8xw28_JBWjieGa1C639O0DDEqARRfqrKNivtD7mEU7zXBb7wZFcc1bR55E8zgrXEgXgzAyk1l8hEAOFAE7YwqVouwqpoKxnBd1NtvreJP-H_y_rWT5tr5vjQMcMLkW-Gasamb5JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تایید خبر اختصاصی روز گذشته پرشیانا
🔴
مهدی تارتار سرمربی سابق تیم گلگهر با عقد قرار دادی 2 دو ساله رسما سرمربی تیم پرسپولیس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/25022" target="_blank">📅 19:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25021">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89b613cca1.mp4?token=GP8xLQS8Xc32BZ9C_Y4dC5YfL7SWIxzeoh1YcgB8SyaAXMn36l6kH90_CKf3BGjabv0n1Z-uKVz16fgziKmh8hhH_TuEzk6vWnNT6DXcYPsm22PpXzWgN2ZMh7f2twvsyl6vm7avRhoGdRvzL6PQgaWz_VGfCwlAhxxTf4y0L5OorjprNxg5xGt3ADT3jFFpEs3TqEce8W0aQ4LAaI_Ks9I5B9EhfuqY1qcQieGopXcaix0iwzYD7w_ZAuss2CuAlMDMiOR3f6zrMFNWmrIReYTXc6E-_OSYUu0EOSzd2mFSWZEcY7Kqe16uCbsOqB42Br3oAipYgpdcRXI-d7zgdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89b613cca1.mp4?token=GP8xLQS8Xc32BZ9C_Y4dC5YfL7SWIxzeoh1YcgB8SyaAXMn36l6kH90_CKf3BGjabv0n1Z-uKVz16fgziKmh8hhH_TuEzk6vWnNT6DXcYPsm22PpXzWgN2ZMh7f2twvsyl6vm7avRhoGdRvzL6PQgaWz_VGfCwlAhxxTf4y0L5OorjprNxg5xGt3ADT3jFFpEs3TqEce8W0aQ4LAaI_Ks9I5B9EhfuqY1qcQieGopXcaix0iwzYD7w_ZAuss2CuAlMDMiOR3f6zrMFNWmrIReYTXc6E-_OSYUu0EOSzd2mFSWZEcY7Kqe16uCbsOqB42Br3oAipYgpdcRXI-d7zgdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
همراهی‌رایان‌شرکی باکیلیان‌امباپه در پایان بازی با پاراگوئه: لازم باشه توی کثافت، شیرجه میزنیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/25021" target="_blank">📅 19:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25020">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9rvhqerHs9W5BlXFndnVAtby3NSdjPRCR372kpijdxVz-zkqLcZQ2Y6aOK_d9cp3ZgfAEJ_8wM1B7R3Nml0k7nVb0xzk5LmLAhjG_8k4CHFi6eyf_Hu0q3WS8ppcf6z6NEI1m4m3esvc9jtC0Ks-F4b4f8HDQY5fzFl4OUfdEUBWNc8JMsLZ5xBHswZ0P8VlGV8fBhXuHroJOM912LUEZkOT2n18IJ47eqg-HCAaqd8IN_uQsbFN9wYJ4VTLkZfK_f-d6XAXf2H366ka0PZn2kwogGpbrAZLja2QNAzVkd2Bq8pE_hfpiTfVvd9QefhOYtbn8-30IZnoel4317sgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تیری هانری اسطوره آرسنال:
کیلیان امباپه در سن30سالگی‌به‌رکورد 1000 گل زده خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/25020" target="_blank">📅 19:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25019">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6_JuokBPc5EwEkYKZpqEa2Impx5FXdknnCfFlk03qA7U_u26ZZ_ZNa_B8g68eIdt3_zLnzVEtE4G0Bd_dO0Pw-f6qyEG9J0yUFwEmrnb7LdrbPqyvdY0DIxZyfMcdAoKKab_YpdJXisk5dshUDJA3b4JUDTl9NBnMql_7kTiAwvcXNd825I5TvJiAqfn-nXcyyVOrXbTnv1lXl7bfId-DVmyLAMx_Hf58cPckdtEUXKsOp7sGHTEi6HRbQcCFZFfJlUCj9vta5xeMsCGj2cLnMIMtGdOTq6fulaJC08kPAPdMJm9LFvFa2EWHEa4K294AoTvMUHKHaM7A2Jpn9vSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیدار فوق‌العاده‌حساس‌وجذاب فرداشب دو تیم پرتغال
🆚
اسپانیا رو عادل در آپارات گزارش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/25019" target="_blank">📅 19:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25017">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GL-r1WlFPHaZFaZq0eY6zueiJU-Yd7Fv89tKB0St93iNq_xCrpti0DNHdhsGmKBgifW-UQEIMTCmRwsN8SJAYMm7NIefGTclWv27rXGAkGszZ36fiRABqxtoB6peBV_vgFKpohY7AGngsclR2l2VXsr1_6fCPqh4yvyWwdQe3H5nnEGG923nVoPtJTX1Gugqloxtselrc1yj3m8NvPjpsPAgsXuRsgjz4mPeyPno_FZmiiTwvmeGG644ngIWJLcFWB-u42vel8kc2VJykK6LEoT-f6b_PEjOtkgqVhLxBvU_zz4oZz3gEsCGTzdcxfbvFW7W6maghqOz6BV3hb9R1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TQpdK6WwZlgHA1Q74alCtU6qzVspaR9dscqOUecnMQIN1a1fS2kuOWiFFeh2WyRaECQx9dD5afEexyR0A7PPl52eHumqMQ36lcur8xyUMyExpgNCc_ugRqZscZ3TZ0bPwhaui5TITfR4Akp7HXpTOdsAKVphQHcVwoOvEj4KEmMNAepmsWOYMjyrstgxyyDZCPneMuQaEvuoLrJfUpFXbXP8PYc3WClSnLxdxx81rgiPPLFhnrIFfkTR0M3QeSxPMPppkAwET9MU7CPPftpXMzgRjaNGbkKY2aM6o2Ws05raNUM_4GMtgcM4HHuqKpA6D9fL1XRNYsUT2kcr-CEVqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
🆚
🇳🇴
🗓️
۱۴ تیر
⏰
۲۳:۳۰
برزیل
🆚
نروژ
📌
صعود برزیل یا شگفتی نروژ؟
⚽
🔥
پرافتخارترین تیم تاریخ جام جهانی برای ادامه مسیر قهرمانی به میدان می‌آید، اما نروژِ آماده رویای حذف یکی از بزرگ‌ترین مدعیان را در سر دارد.
👀
⚡️
برزیل صعود می‌کند یا نروژ تاریخ‌سازی خواهد کرد؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/25017" target="_blank">📅 19:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25015">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tEbw4PS5PaeMkM0CiILrFtAQNIs5aaft2mXPNJ7bG7dj_WCk2p0DS1t2KcbBFgr-K-niYpBFfEA5K6VPuQUfxqtXaFOCDzARamATEnr6r2F2jgOpwYnsklVKkWF5J5vLVaFoFTTLU18bMf5w-gzD85DAc9FaNPqttCNc9aityqP1smtn5JNB-l7tYpYg0WD-tTpAFyWdjwz-u1yVCRM0c5UVKCTQatR3oTuaiTUte9iSWEbQVGM9epDJ48QHAIHYw6K0t-jU_N-FqkKUP68HCXzFQ4jnTmbeX0XZMyetxCan8Z_QYRVFApKaUiG1z6wFChQSf0V9hQMRohzUu1dHBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراگان اسکوچیچ: مدیریت‌ تیم پرسپولیس به شان‌وشخصیت بنده توهین‌کرد. تو عمرم ندیده بودم مدیران یک باشگاهی این‌چنینی با گزینه سرمربیگری خود برخورد‌کنند. اگر شرایط مهیا شود روزی دوباره بعنوان سرمربی یک باشگاه بزرگ به ایران برمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/25015" target="_blank">📅 19:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25014">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRizUKVIekKdzQ5XNQdGnahA2_5udmQ4AT8JPuzHWKtUQl4FcDQw_4DnKfutsXiwwyCBWCrftOYcpVlTSw0q9m0DhZEN4ZCwjbKBBky2WAzjUF_NT6kSuERWwIseyJTZReTTKntgiesZLjBR812uKm3V49_wenCzlWszyGewPixGVsQtkoOhySCwkv1OV8tZ32R4aDW15SWNJ-FMG9qjvZByQq1saLw8HaW2mRn9mGYvPNzLh8BnUD1qhPUeg2f9ZmCJ9sXsz0pWHojjpufI0BKIKOdoR2oQlgKAdL50wrr-MDwljfmf88-GKZuOPrnCJNY97ZELFyS6ImvGP3Qstg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Aparat Sport [3.6.2].apk</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/25014" target="_blank">📅 19:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25013">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUzfQZVh9DeHt4Zqq41m21n9XKP4o27yXG2jqw6H5li6UNkkWODjxUg-qEGM4gFxKKoHHhEER5N_XrtnpiKtlaZkM_1HNyZcEIJ8HyQd5VlnUwq7XGGjO44XoTB2F_-6BxPoDgKrFc4tuAtHD0D955D7BeMV5lWL38P3a_ZRGJj-buD99eYLYEXbcsZqZOUt7Yw6QpZ2AgTMHJ391bQdPBefaC78te0cX_13SCP7sXW1C0y1-Q-93pPeCceFUiEgx2aMJks6ivSHTvzu8Qtxs4rIVJc8RVdMO78-kSRAYzKpoBKikjl0_or4s00PxEVC0g_UHQjGICR09wKN1P0D-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد.. مهدی تیکدری، مدافع راست 29 ساله فصل گذشته گل‌گهر سیرجان، با امضای قراردادی دو ساله رسما به باشگاه پرسپولیس تهران پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/25013" target="_blank">📅 18:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25012">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hy1CW_IkeDot1irpxYRBvKRZTekM8VW59KTgBUTn0RS1NTcAgbTe8jg7OSXHOP7SKQmnIXESgEH2Ll8UbSB96HenBqEJzemMLrVnCSAHMhBX1Akuhx4jXHtu-DCskaikOcnR7WjzRwUMEMROVGzTFLIqZOvDd2QOLqf-hGElX7w1P7oTrFMvhDUJgwhBxImji83AnZ5mBiHmWJs7f_cjbY5bCdp8NcNLJcI5qO1NX2qCyXiGJvMjJubko5_4seTrZfYgsh8n30ex_ZbMFY8Ujf7Kd8JY8HxXOXVdUFJJV_LysFya3sgQOB3rw-jQ2seFhz7PC2AcLt6uy-bRwm-heQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/25012" target="_blank">📅 18:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25011">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ax4mweETrLinvRUm4DieXzDcOOJdJG08ds-eT0MmETgtXcFMf1LECk4oOAW4uS61U1H4raU7TaSYthWWXA1p98UWe28Ftoj6Z-JTHSINMoj4ZYoYLWQrsak41CkcnhP9NXgYMT7RwRfOOw57bSm7X6FCLUrWRgaRXgjzA61qdh9Jmi6hhYx5sxPF-n3pPypmciZ5MvoPudxDhALnLQw_qJKOETM8t3R8PefQEdW55dOrLuS-RWiuPEqXQWSAnF6IdfRMBQHFoBaGg1zPgdE8cCK6rEXIrPXC3XbEbTYsjDO08KneN62cTnEApqNxv13y9PaQFod0eeaKhglDdgjytA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌آلومینیوم رقم آخرفروش محمد خلیفه رو به باشگاه استقلال اعلام کرد: 60 میلیارد تومان. ایرالکو تخفیفی 10 میلیاردی به آبی‌ها داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/25011" target="_blank">📅 18:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25010">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V28hU1o1_VLYIszSELnIdQXAa94EiejRjsUOAAztKkWDMT5r7zy-rSuu7lzgQEF5Vvc6xveCOLeKvNN2DCVwmdCEdnghdNZ-uldCGsTIDZkx8BnFJWL61UxVi1yNCtZ0yvdO6kOKfgHhAce6_w46QxOH-SkgOjjaVuQ5HCe8ord3yj_Nw9V6OBy6nJIQLPzGfW134reX1CMm23JLszYcSdF-hKDBwVv1RVGzTsQDNhzrUO27K9cOeNFa2DC3XPk4BMJHmyZXBP2yON6pTbHGmJ7uVa-MYl18Yo8yetPISeVqQ2-f3Qdr7D9-FHbuXoHTnqWksh-oLpSH5RJeZPZnPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
14 روز و 14بازی دیگه‌از جام‌جهانی باقی مونده بعداز اون‌باید 1440 روز برای دوره بعدی صبر کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/25010" target="_blank">📅 17:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25009">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b051966bf.mp4?token=H455J6sN9N6YcYIM82V4Gx5LdVwOR7pJg7gJpuI3VA0FbkmGFDW-sOJd06j2UD7od366_OCkeN2P0Z2OUzb7WffDMtaWEWLC5VDcRt-AXb3mHvupNIIu_DKoyv5GwiN-ztELt-l4GjtfItG4bMeThJneDLduZDlQwA4H2RDHSSiz4DMKxzL6rCZS30cOTp7Ieg0LFT6vmGZvPJd_7AcXm7Zu95uJO_pNvXknqqJ7OPCv7BT1ahePDf-JqnhoWlYLUAQ_g40vQ94KEqdWkKy-qlhF7Yz6xRyKJZ4NsfqwF2uc_1PRXpf06S-1e3YWdIDnfv9yyg7w2fAIpWOeCFqLVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b051966bf.mp4?token=H455J6sN9N6YcYIM82V4Gx5LdVwOR7pJg7gJpuI3VA0FbkmGFDW-sOJd06j2UD7od366_OCkeN2P0Z2OUzb7WffDMtaWEWLC5VDcRt-AXb3mHvupNIIu_DKoyv5GwiN-ztELt-l4GjtfItG4bMeThJneDLduZDlQwA4H2RDHSSiz4DMKxzL6rCZS30cOTp7Ieg0LFT6vmGZvPJd_7AcXm7Zu95uJO_pNvXknqqJ7OPCv7BT1ahePDf-JqnhoWlYLUAQ_g40vQ94KEqdWkKy-qlhF7Yz6xRyKJZ4NsfqwF2uc_1PRXpf06S-1e3YWdIDnfv9yyg7w2fAIpWOeCFqLVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ریمیکس امیرقلعه‌نویی هم بالاخره منتشر شد؛
دهنتون سرویس این چه سماییه درست میکنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/25009" target="_blank">📅 17:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25008">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHhzGPggE0r6IgNlVSzkmP29VddAOoDW86h1OkYZpAANeq1kMWL4Jddc7DYrjyo2IJ0sWK_44XETedcIXR5n9vYjLt06rHsl26tX49k3QPE_kMwReXOo-f_JCdapt8I6usz102xcyBZuaK8hSLANOlINp1L_YaPX-Mzt1z93-jig6xKjx4cBW6rm7jH1qYoPkl7HnJSR7Sh_AogixfBEak1DZdYrHumw53bGEu1KOyaq9CjLZnBASQ1d4ShlqIRLv7KhFknjU-hgzKq1R9AI-O8Yc4oiyr-BkD3tPWe2Bsw2ZX3ye_zYC-PgdzNaJmHYKF0eUN4WWANCnS2QJCJBYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
سرمربی تیم‌های مدعی ایران در فصل جدید:
‼️
استقلال: سهراب بختیاری‌زاده، پرسپولیس: مهدی تارتار، تراکتور: محمد ربیعی، سپاهان: محرم نویدکیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/25008" target="_blank">📅 17:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25007">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeaaa6b3cd.mp4?token=VWDzjInIbLKlUv1p_Gmb3qprY-uhydfsETRXlhMZyayKQwTymow48U-S7TTeE0DttWKZ1RDfiCYkm-0_7uoknCQEGNkJmcCyumtxlkpn5x0AJzAGJ5a8r3yMZ2tqapFkMTbwZs6Crzpz4NExgM45KHZC3AOeNs-UpueKHtAELuYztf6a04NDTD6omUXii8uyMnpNg4Rq8wWXKPp6qKfAxcY0vIWbV2ZuEERV7MQ4WOq6BBWu8LNE5-dV7sf9SZj_eZUcAkdfBTBfQPUkBB9vvsPEt6EbHvpZMWESGOsiz1XfCBXKBhl6sV0Lw1QEwGhIojW78miiSR3yYN-d48B8vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeaaa6b3cd.mp4?token=VWDzjInIbLKlUv1p_Gmb3qprY-uhydfsETRXlhMZyayKQwTymow48U-S7TTeE0DttWKZ1RDfiCYkm-0_7uoknCQEGNkJmcCyumtxlkpn5x0AJzAGJ5a8r3yMZ2tqapFkMTbwZs6Crzpz4NExgM45KHZC3AOeNs-UpueKHtAELuYztf6a04NDTD6omUXii8uyMnpNg4Rq8wWXKPp6qKfAxcY0vIWbV2ZuEERV7MQ4WOq6BBWu8LNE5-dV7sf9SZj_eZUcAkdfBTBfQPUkBB9vvsPEt6EbHvpZMWESGOsiz1XfCBXKBhl6sV0Lw1QEwGhIojW78miiSR3yYN-d48B8vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی زیبا از تحلیل جذاب گل دیدنی لیونل مسی به کیپ ورد دریک‌شانردهم‌نهایی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/25007" target="_blank">📅 16:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25006">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWSQE-UGIamsXAzonE-rmOAzOqpn2UFKrBEmN-sEdH6xV4FBak9rna2o8Mt34YJ-IRGio-Evynk0cweHGcAnpoy6XtHfrwPNZrSuW9lk3Q5kfMaa6VjxJDGDzSJ6r44mowFoNyrvK2nMMAwDVezatj5JwnyA0kTtvuiGNVt2EKCj7Arqf__KBl4CRM1FJ_b9HO3du9NJZ69M5DBmkVx6VlDxUoKA62gIQOt9XR1zptrtGGQS8VzOAGz9TVu8bHQnKqCzBBBhVe7xc4zhNqLI5cMk9v1_2urJ7R2LmDeJoNaqTqHn6NWhBqcGQfHoUu9Tn2GJcHgTkJxm_ChqoL1-2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
باشگاه استقلال و تراکتورتبریز امروز صبح با ارسال نامه‌ای به فدراسیون فوتبال خواستار افزایش سهمیه خارجی تیم‌ها از عدد چهار به شش شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/25006" target="_blank">📅 16:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25005">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oya69wot-JT5biKEPk8oM8ykKi6blYHwdCZi39vnrnEsyqwbAAzyRMoRGC3zcCUd5i6Vwnc6kLSfnG0fqwjWtiwmQpSCjuUArB1opOk-76fxL4XbSW1W2Ml4yc10v4rYSiUHI9lxgt9Gja51h_egGAJp9K8NJwgpRdgY_6IVk5Ow1_HMq7QlmUvyIUrHZu3FXFDnUx2KwJITWXIdyAnxyDgvhcsNbD36NE2WSATl5jPdCL2rgkG_3mLm8QwywAuHsxYuFsn8KTnJwwp8wrVBOXDhS2JZEr84FAo61CSdOtSpMOM7DV9qhwBQw5zv6redxIH5g_B3emBPqx5cN57-oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
#نقل‌وانتقالات|پیغام پرز برای وینیسیوس جونیور: یا تاقبل‌از اتمام نیم‌فصل قراردادت رو طبق شرایط باشگاه تمدید کن یا قطعا تو رو میفروشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/25005" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25004">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa6c0365f.mp4?token=Iraf1ESqCHPrt5CDd3tAeygKnqXXBxP81lOof4cKUOxHnds0St7G_wA-hRZhNRggNKybAAKNl2-nNdCiSGGBcBwFxma1vS4KnUaBrf3c-umqlNE_yqHirhPfzdPfTmp5O_RL4zasRn6oPRfyJKVQFEFybengqoCDOL7EgWu0lG8KoNTnACTCSLgLney_Bn3fiV36vJK2Ed3aP89Vn_W-jvhyU8OKRBQevlXZRjJBDgIyrxgQ5HHaAfVHbGCGMkhFS2N9DHKd04jFBe3yzLCGV8-8TOChR_hhuNv3lRwsh2ewlqBNkOrTzH0vPqtSbFe0l7rTEvWLefklh51UVHzu0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa6c0365f.mp4?token=Iraf1ESqCHPrt5CDd3tAeygKnqXXBxP81lOof4cKUOxHnds0St7G_wA-hRZhNRggNKybAAKNl2-nNdCiSGGBcBwFxma1vS4KnUaBrf3c-umqlNE_yqHirhPfzdPfTmp5O_RL4zasRn6oPRfyJKVQFEFybengqoCDOL7EgWu0lG8KoNTnACTCSLgLney_Bn3fiV36vJK2Ed3aP89Vn_W-jvhyU8OKRBQevlXZRjJBDgIyrxgQ5HHaAfVHbGCGMkhFS2N9DHKd04jFBe3yzLCGV8-8TOChR_hhuNv3lRwsh2ewlqBNkOrTzH0vPqtSbFe0l7rTEvWLefklh51UVHzu0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌ازهواداران تیم‌ملی‌مکزیک رسیدن جلو هتل بازیکنای‌انگلیس‌که‌نتونن خوب استراحت بکنن: بامداد فردا ساعت 3:30 بازی مکزیک و انگلیسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/25004" target="_blank">📅 16:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25003">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‼️
یه‌ویدیو سه‌دقیقه‌ای‌جالب و تامل برانگیز درباره زندگی شخصی و فوتبالی مدافع تیم ملی کیپ ورد
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/25003" target="_blank">📅 16:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25002">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzFl2E3EPQ32cbnCu_si1_62DjbelZcuWsFBFi7dJiCTutIavksr5CZ70TGwS0hFZ76C770W6lk_m8iDY2m3yKe0IYXpoHXzQae4_ZdO-UdFwkUkYWVOLH39j8phN7sPVeZdWofCOzcDLZz_zzpZGGUKBTC2QvCjrvpQoInNKwRnCBhBGdpGBBAx1sPdPwcN6Fy4s1rf4h_-SDhwIgLYBunce5DPqc5aLVab_TmK3Mo-i_TOWrMe8emNjSGvCaneHbsfLNocp6Sp4nQkO_nWpih-0fl9qrla1mXZ4WI_MrwwC5z0zOc8gphRA0Jb93HtsUuSj-toVxc4APPE3-01rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی روز گذشته پرشیانا
🔴
مهدی تارتار سرمربی سابق تیم گلگهر با عقد قرار دادی 2 دو ساله رسما سرمربی تیم پرسپولیس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/25002" target="_blank">📅 15:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25001">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JytRM6E6x2XXVnpQHR0jyu_qZPJgeTMivuMOvOlcnJ1k-K2pJd-YexV8-IyAhILsHgl-NsRk60xTFbA7fu09eMhDwA5GfWVAnn551n7m91nmda3WQoJM1_iBXbE-i90ilR2q5yBldA9_d0ORwNaGUri0NNS0RJF6RV9pRhr9masKUNHHIa4wLn8N30cvS9j-nvRNynUBrzYHQ7e2dVBvq6wF1zF7UPqVSP4UrtKiwgyo8Ozh6VaeyRvPvcBp-8gVhjBnd-kCLsJOV6qaI1YFKMuCpBETcH6cHovP23xVLysVegmx9CcIqCelmU8M47ZUizX0rzHBEhNNcJV57KuL0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/25001" target="_blank">📅 15:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25000">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hf99gDrnw8hUqQ1TQLfpRe4Poqgae85yO6gl0B4TyR0Arvft4hfWfRVQZKWnvWI_NxF1YwO-iOsWGuCDAXFaNYinOoUmESyyW7ffS7f82Z4Wy4rxdGbPIk64lCo2Nl8wkOVy3DZp9ruuPiyP12WPpLIrlV2TcAgjTwdvj3yaGykx4uJAGhPYzNrhY3GbXeNu59KxdOAYMi2eU4TvNIR0SNcC4hOfaPI6RvG3fdtKp4FapZTObVVti94FgxGGMZ1sqx9J5qSq7Dc1SmVXRMU1gFYc2lBIhuLzDDgvQR2ER7UaM24eTh0OQRZgmzVH-yTk0PgPXiARK2u6wKCLy3r2Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه گلگهر سیرجان که اخیرا قرارداد مهدی تارتار رو تمدید کرد بندی در قراردادش گنجانده شده درصورتیکه باشگاه پرسپولیس این سرمربی رو بخواهد با پرداخت 20 میلیارد تومان رضایت نامه تارتار صادر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/25000" target="_blank">📅 15:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24998">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S50U1FlvoJwcdSbonwXGjCfDPvMkfiQ2APj-FPutijGpi5bPmYTq9-DcIQ4uJQu6_3lqShX5rWncc3wPCijj9tK2-ouU-JGat_Fdvz6YPzGFI6CKaZnQBazXUoAYNCfDtK4fuFP5zKZNFc3xgrDUfvMbGisu5FiX7jS-WaD1dXy_1AT7fPl_i6SFRWk7kt075tL_IzmDfZcISsCZ3oVFyMbZ3zuRDes5y44qfIRWdniaAifFQnYqcRG7HYBOWYpdmbirrQSVfMlbHEU3poquDzAeacFv6J-Diz5xy4DgsHMJXKgNdsWGt68grQb7r-6apOt5gmuNS2TU0ibraEdS5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uuZm2yWbykqKtGoJ8Bq06cJs6DeZqsrew44_XuZpLzlbMjF-yRzBtczAm4oUbMxxRJ8Hh9iIk2THAVq4Lx9ELdQk8kSlQxeub9spjyGrRs91cXK1evjJAC3sRo8QUom7c9GaKr509Bgyb4jnCbxCYppSn7Rgd8Re8GKxzSInDKLKBMsDe-M6PSNQPh31jMU3Ipfewu4Jibz8BJjfkMqVlCpj84DlXVUW_ShWcv6zPU_xPaO6Iz_KlKpHruMXiRPLAx1zK-HNPkmL00edbeYiSCQ06yS0L5uYk6DWxIVimmIP70zhdJIYE7A0TBjuU3m6C8rTqbu_3s8FbFKwwLOsoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
#تقویم
؛ سال2006 در چنین‌ روزی؛
جواد نکونام پس از جام‌جهانی 2006 به‌تیم اوساسونا پیوست و به نخستین بازیکن ایرانی لالیگا تبدیل شد. او طی هفت فصل حضور درتیم اوساسونا 197 بازی انجام داد و ۳۱ گل هم به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24998" target="_blank">📅 15:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24997">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEjSl4kdZtmJmmOICj3Ppzhrf_-w7rkemXGTIEGlNNLMI4k1xJDsf4W_MXJjjQmpwhcRJtDBOcQOAa0dCZfgsRIoD-ZYkoBHqQfrrs_mIpurBJFD_fkJIecqmD_sA3xT-cbwARGE7jK4nwfXRKVJrFCSl2wTLATPJ2a7qtu_eXoVVnrWj0pqGgdUJIMl2TKrF5z7D_sxY93Y0suVTIg08Jo2tQDjWoVD7p6dIiE1k5UgEuU_bibmrXmy1Wi-l5VTX-4CXPW_RNuUWTVqYM9D1hEhfhyMhdleht5ABSrQfWNap9jL75gUIBRe3LNGuKJNwS9sBEzIuD2MBPLlDEarLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔴
تایید خبر شب گذشته پرشیانا؛ با اعلام باشگاه‌گلگهر مهدی تارتار از این‌تیم جدا شد و بعنوان سرمربی‌جدید باشگاه پرسپولیس تهران انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24997" target="_blank">📅 15:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24996">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCv2AujI6kwa1-N0yH8I3gWNeKV_O0AeOB9ni6pcpF2Hbdc75toGF9jKpyz7vtvJnbK0DGHg_mvAdQhiLbvN6NFmqUH2lR6I-tNksuQWbed5NR3cwdxfUQke2zHeTUyDmAWRt0IxNkN1TYQSBjaMKlypIVFyDF-3bZs96RNOhsp1VNvNzZ1fsuXLzI2xfDulUGaTwUhglskCoEfe5FKcPyLphLR4XAbHuYcbkbN1PQZ2xxwQOvmUATiHQhgJ7FOTciZmERqlVCRC7FASjjJjMOKY6A-Lkp1wnU2Gg9DVzvr2svUKj4GMLZJr2ddu5GnzyuczOPpXkjOnYX1S8VtC7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24996" target="_blank">📅 14:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24995">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOInm0nXq3KFsklB06mClSxjpzMIh9p1ab9FRIdYf8W91G-c3cYcwv-npIj6I9aa9iZlHZjx2HGoOHH3yKvG09YZBZOL0RPQVVQ-e3lFjAhvpzx1MMdc6f-gZiPuER9FyvF-NWSaQw18LQHQAwg2vTemK-9JZ8nvCx2PsFauYOLYmGCwcxoT0P-JmReMsfSvbJ5LzMbi5gYFKSe4uj9WNzq4XgB42_INqiXtIEkN1RfjOZO16wA2RnbNx84x5mGOexF-5Bdz-Z6aaSf7Xqmv_Tw27z9rDaFb3KYHG9WzHaL5lIylo3I1AHUGGpU_x9Q5VU7wA9uEcZ6cOX3cvq0vvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارها‌ی‌‌ امروز؛ از مصاف فرانسوی‌ها با پاراگوئه تا نبرد تماشایی سلسائو برابر یاران هالند
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24995" target="_blank">📅 14:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24994">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIfULiPa5v8IS1bOMmsd0H6h872Nrs1w4dNL3tFpBm8EFTdrMV8n8wC2RbYMZuccX8tGgH1xQ1rLqn9F0IpPuCUH04RdndOW2KuEbuYBK72kheDalNcOsoRn8A6F-1q5HzwqUOfa6S1umRuKfr3z_N24jK8ZSqMOD3ukdFfkbmqC2phoUa10I6nEUDc3CPBLPmKIlGAmkhhn9jcJ3jJYQW5Bh-k9IhcJmycYte9DW7i9Te8HdRbvNC_vACCzPHZrrtcAu8YE5rH3TQNfgx_Le1BgkLSobxQIOtDexIYfnITQmY3LdbqAU1aopQJ1-7u5bz31DpS_ezVPan2RD1vH9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24994" target="_blank">📅 14:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24993">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSep8zaNXAszajhhtV-p0pIBxg7656AYot48o1OiYgqrh9a-GuecySce2BzjJxem6-x2__JNGCGIsQYRRQRo3qAGE7ocAwpaNIyT7WiHCZKTI2JcrBPFt8iRCYG8yTpMxKjPQETdbN6W-HIK5BrpqlTW4YNEkOAZMxTgGdWVjOMHuZt1t-UHtbffPf35Dfbn649TzqNYrknyMtz_kZ6e0eLPSBStDCFaFnn-5oA0SjvYe0pvb2wQ6gvqCcGe3u1MAsX6Tk-_oZH4--o7IUIrvNdUPeqKEoaIcHTDqwl3Tb38ppil6RFaCuNTxQQT83phCZxBstogdrV3If4ed357rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تارتار عصر امروز مبلغ 20 میلیارد تومان به حساب باشگاه گل گهر سیرجان واریز خواهد کرد و با عقدقراردادی1+1 ساله‌راهی پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/24993" target="_blank">📅 13:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24991">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mwa0tvIAxMEXrmni0mWnlT6BNm3FJ4HeJXo_uI5Qvg4Qh-wH0VDkv0kh4GslL9cGtZYXO6WEk7-jhjCU7zVFNNPvDx8OhvjK4By-KzsoXrAFva6Vu1DtDfHa8O-g_ddkjaj6aMCiDg1A78nAJOmQhpWl3xdF8A_Sf_N9R4P4c4sJn5YmlNhwGmo9skp3RKzYgfpF1v9bkmOXn09Ka6SnbI_mQK_dayI6lB0NkQjCSfu3CIHk4ZKY4A5uuQ_oC--z_qez8zDYwN0LnXqY4TAdbvEX_OAvLMu572eatxFM45SxXIyHiMYZMFSBYIEnEhbx-ZWJFcUSLlmUstVIBIn6cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/24991" target="_blank">📅 13:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24990">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLLImF3QgPDzVgq3QXV5KvIq8oHgEKG4bmi56vgbEs3WY4SUQ8RBUGNXL-CV0XikYan6cm6w-4P4_nWz2azsEo4vOr-Ny4AaL1GCO-WxJ1OI8FE_WkUZVDnUiToABfkpwdmP7E12r42xIBLchOq_2vkhnQQWaRymFX-zjDIN0JRhiV_UFa7N04e33fJY6DVhT9QapREzwzzD-9A22y4dqUhsH6obXWx45w92AmHIfvhC_H-r9WAzmfMntOXTrco-UVhWuHjCzZcuEvUQATX4q2AoS_MWaYqI0N2yHYvhYshs_ayOgURI8HiN25mBFcFTeoHQ635Z7y9Xzz04M1UamA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ گزینه دوم باشگاه پرسپولیس برای سکان هدایت سرخ پوشان مهدی مهدوی کیا اسطوره سرخ پوشانه که مدیریت باشگاه پیشنهادی سه ساله با دو دستیار خارجی به ایشان داده است. مهدی مهدوی‌کیا از مدیریت بانک شهر حدود یک هفته زمان خواسته تا پاسخ بدهد.…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/24990" target="_blank">📅 13:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24989">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVNRyIEqV6y0FSyYUu1qMLTGVZKPnjoC3AUFOOajCgGcLmqb2UVhrpoz7fYvCxS3q8I1_tV9rId1VkEGeLAT62mo4qBbPq0ygI3P08kcm6cWQSSyhdVYo9EM1YaikMUfFYrh-27aXUsIZug7_u-ta9PL_6l7aDAHuNzRHOgqNBHwCVJBKvux-g9OExoP2mkGmS_7EKL4BfZ939-i6a39TatlkkNpIFV9sb2vF8zRTfrTECG02vvyeuTLqqrYeb48R15VKLCL1tI3IwIPTYy8WKGjtzhEqm8Um7e72pBQGBEzz96PmiRh79HQOEQGvwfLgea53phK5V9gpq4_hA7Pfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌رومانو؛فدراسیون‌فوتبال‌آلمان با ناگلزمن سرمربی خود قطع همکاری کرد. یورگن کلوپ اصلی ترین گزینه سکان هدایت ژرمن‌ها در یورو بعدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/24989" target="_blank">📅 13:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24988">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/recaWzg9Gf-vqIYcrof0wdLKK9pFUB1gsPcRvjAemdODCMgISiG_ohmC6APiR7oLG0C1cPN8_O21MFwdmOvGhGxOJmdhB_c7RkSYlOmekB_5rwoJHAOfKjwEEqaBn4DcZizmYVA6cJ9Y2uTmZcIrdU5uZCh6q5q1GZwCpS21jGgII4p_Q4n_cqEhIDwKoNdeLnuOLsUqr2VSB-ukNqErSvvGK5oZ87Zxy8GIwIAE62ze-E4gR5bJ2tFFh-atq4qiatxg-KXylqEIdRhJi2crdCBJFbxqgaXENDmyhnkHF2guQCAu4VhnEFdOZ2C0tf0WumUPovDuMp7j6LLERMGvHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تارتار امروزاگه‌بتونه‌رضایت نامه‌اش رو از گل گهر بگیره سرمربی پرسپولیس میشه. در غیر این صورت مدیریت‌سرخهاسراغ مجبی حسینی میروند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/24988" target="_blank">📅 13:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24987">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgJSSH-x5CLd4OAUjeJXk0lBOJ3Bc2TlAcWlJst3CljQ02HB_ygQCr0BlHYFUl5wbl9TuLeKBS_Mxj4kCU-vCTRoiwueIHI1xL8FWfSUoGpnmS400MTaK4pnWaEeWvUk0Ta_OsyPAAf1dv2zRcaCtT_kbY6sURr8OOfTfODOiGos9xk2H5-ODyhXA7wBEQAbZBQRMF5Yq-N66R_hlcOGZwDMqdGak7VqcqXXzl_74G9mbN_x12ZE6cjSH7k_Jo4WG66OZ6-5Yz7KXuF4E6UWimT53tdGfCsQsVZ1e_tvOnNLY-02EnH1n3kbz8I2uEwWbWNrh0p0xx9A1zupoYumKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/24987" target="_blank">📅 12:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24986">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/occxG77KUPJCrT5NFd7bsMy35_3l_xpf_9Hcpms_zw7eRFdoeATNm-vpZCP9_qaBIXxbaHXGhrONa1E0T1w2NVCOjhUu1vge96_WT8C0z8CWYcIFoCkKYzIzSMs78ccAycY-CoFzAkxH3f3pwbmh-M4kmKXJ11y032Jeo3G6hE7pcTJOHjpHZ85UsU9bu59kxvZgb3sv5R8vObGSWO6E7ukYZHT3QEryJgxgIm1fsV5g350xS7DG_nE-tU4ybZaets2r-faMJdVyzQVPVtRhbGnVyckXtzPsmMvmnaPSywFQBiie2ms3d4CaOumZkUxHWQanoS-RPuR3XKfYbjvWOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#نوستالژی؛ یادی کنیم‌از مصاحبه قدیمی کارول سلیکو، همسر سابق کاکا و علت جدایی‌اش از او:
‼️
کاکا هرگز بهم خیانت نکرد او همیشه با من خوب رفتار میکرد و خانواده‌فوق‌العاده‌ای به من داد اما من خوشحال نبودم چون یک چیزی کم بود. مشکل این بود که او برای من خیلی کامل…</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/24986" target="_blank">📅 12:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24985">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mv7R876JPewhWWYc-vaAnudhA4vFIK70ojPkAZm63fMPaTgg_I6M4Y8mbrcGnizWCliTaYJXmdloxa9S2zYIgk3H82sD5FJtT-iDOCevn078lRfcLDPd5YLmm1s5grLk5gZdkExuihFD7IZyTQoREUeGXodX2yYufieDDkPVUbwQ4OZzj3yIqLsn6oM6-Is2r6JbAgRCY4oIA49Bvq55BW3a5dRoXfo0zNpq5IOA4ppBZhtjRXYBQ1sqExvN1HPAnz0rxVR8osjkL8AGnFfiV8JKe--1-TNCGP76pnJfJK-uA0sGjICwzK7uFtsGit-uZUQSqF41EvbGbrE6Cr6oPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ طبق‌آخرین اخبار دریافتی پرشیانا؛ عصر امروز جلسه نهایی بین مهدی تارتار و مدیران‌گلگهربرای‌فسخ قرارداد برگزار میشود. همانطور که شب گذشته نیز خبر داد مهدی تارتار به مدیریت تیم پرسپولیس اعلام کرده خودش رضایت نامه‌اش رو از باشگاه سیرجانی…</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/24985" target="_blank">📅 12:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24984">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpF3UUV81p5MPRKgBE4lGzfgltmfPTuscZges1GWZ0GrT_K7Bfm3FvOP9S1WndZmdy_A_Eetwgc-dfmIAj6wW_ktWIvMe59yK58FLgOjzD5SSiRT6BrVZBnVlGn5paj-B98t50qBr0aTRKQ0Ja8LCEAdfosK_zzOminY2W5LL8LiDTV116NHQE4dRKp1f6K1DbJSV-q7kB9uk7R5O6rMOwwRVmQTbjOwZil50LgaNl5b3B1eaPjeRZ0KLF3BUy_m1Khk5-5p-7C0UNGWPKnkOfuISIzv_Pw8d_nomrcIjuNaOTGkhg3St5vOnlmLnCEjxdjJR_tOg9uRIDJWD8iAjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/persiana_Soccer/24984" target="_blank">📅 11:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24983">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZ2cjWL_nTQGsWUIRMbD0KopwsxS8fj4PF7i05go4Fb94ZvLDgwa7MGfVB6bZj-fA5eMjxtHYC16smYm9RO-SJoAcl7l12SHyWfU9kVxWBv52TpRSt_TLpu6Q6qRQpUbWSvXVLzdsjqTxovd381VkxyhJWdfGOg58f10Nx6ZW142qesG-tQ3fQlwyTYmxAn1-UR21Cs8eDXS-cMnImdmF7mowGAO2Sqn6ql-F6PPDT1q1m-VN5yoadlLbToHyh3tKsnqAb5c4a0PGYaH4r787eqEp2cHZGfQyzi83hmVQrIuC--MhMejGtJGsw1WOhnygrAED-7xGwtijVnL8LrgkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌مرحله‌حذفی جام‌جهانی2026؛ فرانسه و مراکش در یک چهارم مقابل هم قرار میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/24983" target="_blank">📅 10:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24982">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCm99CdbEDsW9ZILsvGob98IDypphxBo3QxhbuFQJtk7nMfNG0B55bieLsQZJaKh8SEbJNX38rESC6F9zbkcqqjZ5gP4rZZsCSt8Mb_FI8q6psmiHlObzF_ysUR5rClaAgKoMdkZtqm_UG8pqU3g5vFQt2aY5l_HSE_A64Ee0QIcPfe0GclYH6ajCn6MsQk4FdmrDt9hS7ssJ40tv1Ouy32HXWwQbL63Hul9ZBH_13CyGF-2AXzDb-OOSbWCxYxlieR9cD1CKgEc4CS1gTi4ocTOPJISxOaAcf_Pugu63K4o4Le56RhhXAZ8A2TQDlFPMn2k-SlhinE6ATbSPrAf1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌داستان: امباپه‌‌کم‌عقل؛ رابطه‌ی کیلیان امپابه ستاره فرانسوی رئال مادرید با دوست دخترش، استر اکسپوزیتو باروشدن‌خیانت امباپه‌ کم عقل تموم شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/24982" target="_blank">📅 09:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24981">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDOULoLRhMFFU8IJDdKvf_3MEZn8BiAzBo2uq_vKGSJ-w2_Zp-CQtzYh0kA-OEpVNNGK7KI_ItrZ_WTALHfvBZJKutHB9MHIqT6-cgFw8J8b8ldZT4N2zu7RK7Ee8w0WHdcZkKMT4wt3Jx9Jd11iWudYImhWs2VkSL8pAg7PC2tQXEzgaxjMC2a5mm9DD9MnKhM18ScmbplxU2UAIo3vrVGrbBfAOC8XaANYiIOUWQYou__Kx30xNMBm3J4WfbvC3PLjqNe_G8Gxvph2Xrsc61qPEvmaVvwUU6nya3tnd8TdduM6QA1ZhXFzduUuKwFT6Qe2sdrf0feKFSNM4eUK3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌دهوک‌عراق به درخواست یحیی گل محمدی؛ با سینا اسدبیگی، حامد لک و محمدرضا سلیمانی سه بازیکن فصل گذشته فولاد وارد مذاکره شده‌اند تا درصورت توافقات نهایی این سه بازیکن با تجربه فصل آینده در لیگ برتر عراق به میدان بروند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/24981" target="_blank">📅 09:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24980">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=AX9VnPHuw1kUJwTm59QYF8-sKNOXZ-DlUfcOrLh9h84eaMM5IBD1mjXx44290LD--aO5zqO6p6xhTBzOFvmWcRHcGFm0nxslMZmK7SbF-48Z0B4NFwuFXIePHGAOEMYs2QiaA92YJlz9bAirQM_vYK1mlV5VtAiwDDH66MaxOb708wmjLar2cFGYV1MmRdNI-QBdTg4aTZCY5JsTxcIHIk1Mb2beCviZb2YVtjw2bUVar4KmxLBX-RzmT8ySybLXH5JpAz5bTDNbh2qXqRJS-KJTjVdmoD46_kOYHzJ9a-m5YslQcsY1o5KaDxIsdwP_60Z1Juf1UyEjzP7kzx3okA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=AX9VnPHuw1kUJwTm59QYF8-sKNOXZ-DlUfcOrLh9h84eaMM5IBD1mjXx44290LD--aO5zqO6p6xhTBzOFvmWcRHcGFm0nxslMZmK7SbF-48Z0B4NFwuFXIePHGAOEMYs2QiaA92YJlz9bAirQM_vYK1mlV5VtAiwDDH66MaxOb708wmjLar2cFGYV1MmRdNI-QBdTg4aTZCY5JsTxcIHIk1Mb2beCviZb2YVtjw2bUVar4KmxLBX-RzmT8ySybLXH5JpAz5bTDNbh2qXqRJS-KJTjVdmoD46_kOYHzJ9a-m5YslQcsY1o5KaDxIsdwP_60Z1Juf1UyEjzP7kzx3okA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/24980" target="_blank">📅 09:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24979">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWGxxuXl6UTkIF0Ht4_woQuoHC3MgUxL6LXP9OOzi_6rxkS-BVz6nru7GAabIPkCnoj5hPDAazW3dG1ythcY3sAlKWJy1fVkMKNvLH-rXMDBN-ht20HSSG8kBq1QPbY2Btj-vAutgz9UuH6dFgYIIG6OEWZ-hSIUXJciof15yHzgkYOVKB9-n9faFT3Uzp7fts-dKbHcCCWQY2J_P2tMrhb1Q0vHVjawn_Hy8kSWxRw53p2eWYvy_W3bLl5asV4dG1nCzprfHMeL1aDAcuygzDlQX9EGFvSgQ8A89F-VnG1b8w4ceeht5YkAHYYEji5j79Vu3zIfyTUp4tsttBgIfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گائل کاکوتا هافبک‌تهاجمی‌سابق‌چلسی و استقلال در سن 35 سالگی از دنیای فوتبال خداحافطی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/24979" target="_blank">📅 08:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24978">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd8c901fa.mp4?token=tRyCL1FwPiqMRyJTE2DixcKkiIt2c2WcHKMYzvIMRHhTDakTqOqaQnNs7lK6YMKWAyQM5vIca4LKgOv2U9ZKcuY4QuaIpuh3NxHZj7ETxx0Z83DrwWTPQkZY-T_FVOjKN2comcburXEjFOHBb1Z4C9Xy3TrpUFdHiYE_5yYg6cz0UHcjZNRAenqDgaPD2v8Li6f3fSmlJyolk3U1aPSE3AT8cW43FnU5IjPvqwyIcqCdCN3iHQCi1D3wQ0da62LAjQRruKtlVsORKqYfOv2Q_WnxOIskERnsEJHl_TO9NOx2nStGIAB9JcXODwiV0FjP5n5R2uwHcga0nEQ1c5DQCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd8c901fa.mp4?token=tRyCL1FwPiqMRyJTE2DixcKkiIt2c2WcHKMYzvIMRHhTDakTqOqaQnNs7lK6YMKWAyQM5vIca4LKgOv2U9ZKcuY4QuaIpuh3NxHZj7ETxx0Z83DrwWTPQkZY-T_FVOjKN2comcburXEjFOHBb1Z4C9Xy3TrpUFdHiYE_5yYg6cz0UHcjZNRAenqDgaPD2v8Li6f3fSmlJyolk3U1aPSE3AT8cW43FnU5IjPvqwyIcqCdCN3iHQCi1D3wQ0da62LAjQRruKtlVsORKqYfOv2Q_WnxOIskERnsEJHl_TO9NOx2nStGIAB9JcXODwiV0FjP5n5R2uwHcga0nEQ1c5DQCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه خطاب به تیم پاراگوئه:
اگه لازم باشه دستمون روکثیف‌کنیم و وارد جنگ‌های تن‌به‌تن بشیم، این کار رو هم میکنیم، ببخشید که این‌طوری میگم. ما اصلاً مشکلی با این قضیه نداریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/24978" target="_blank">📅 07:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24977">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WP94X8aTx_aLZa8SGEcDqdZ5FWikXiPOu2-j-r5XxyCWukKsXIpB4FK8-D2_Z9GPVY9b4NipVYEY3Oz3LtCEUjoJQst4m_CglNg0WKqzM_bLbfDO-dBq0Q42_xgMGOzhIDOWHGJOKZb0o4cWivo_LvD4yQHrWiPCADxxnNosFKZrjiw5j7XtHtZ0-NRdabzsvmdCPB1i-jI3MLb1dezUnhMHT9rN_5mrgSiDlyo4aCUaB6h358yBuIny5_gEyR18x3Ih0csFNNJ6sZmX0m81EDf7r4w8tL5WFCf76rMNOmWaibU0o2kBpjqP_x8Tcgjg1ry_B7w-WtIx6D_lMhYCuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌مرحله‌حذفی جام‌جهانی2026؛
فرانسه و مراکش در یک چهارم مقابل هم قرار میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/24977" target="_blank">📅 07:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24976">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5736be2a0.mp4?token=OG29UzBua1O_tU_rJJxrDv1MXveAifAIu0yHqzpvNn7D6xthMZO7NX9C2bjnCcZnuvblndRDLA77mGzjBUrzlMgNfRq98Yjo-ov_C9C_9vgRtNuURrjHDDoGj7W0TLFtH34-xCzLKCyE56G2_CiEmlW70CyTXEAoSpdjyVjxgbzppMSi0-a7W73xBZpg6-eFh2gQQ61dNk1DLp1n_FTN1MWq32lyafFL3BRf2bBkIWZYxODoSp7BbIbOVABign2Aw2DLerBp-Q80TeaYFjL3O1ZQZrr38qn_7Vu8WVLy_Ag4YAkNFZiFyxM3u5juK2km9oXppdYkqRhhwoY764yc1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5736be2a0.mp4?token=OG29UzBua1O_tU_rJJxrDv1MXveAifAIu0yHqzpvNn7D6xthMZO7NX9C2bjnCcZnuvblndRDLA77mGzjBUrzlMgNfRq98Yjo-ov_C9C_9vgRtNuURrjHDDoGj7W0TLFtH34-xCzLKCyE56G2_CiEmlW70CyTXEAoSpdjyVjxgbzppMSi0-a7W73xBZpg6-eFh2gQQ61dNk1DLp1n_FTN1MWq32lyafFL3BRf2bBkIWZYxODoSp7BbIbOVABign2Aw2DLerBp-Q80TeaYFjL3O1ZQZrr38qn_7Vu8WVLy_Ag4YAkNFZiFyxM3u5juK2km9oXppdYkqRhhwoY764yc1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
👤
این‌روزها ترکیب جواد خیابانی و خداداد عزیزی خیلی‌سمه‌خیلی؛ از دست‌ندید. این بار خداداد به جواد گیر داد ولی دهن سرویس کم نیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/24976" target="_blank">📅 00:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24974">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjD_60KHW_Mb3mRcogO_q8xazypITX-3vfhT5zB9IZ2Lv0gnjduzI_3T-cuTdm8burE30QJdf-8jQr9GzDJINGVapdQk8Qu69hg4tnrkLQBZdMSTDmy18EvFCJqrXKxIbYdHIjCR-1Pxx2x2ZAyNRfG5CvjqBy3ebOLVo2M2eCAEcmbPO6NpWc82rCr3SJ6rrB9yqi0R9fpVi5Q9ujdGwwo-cbQgNaa7RHW05H7NVaTcMJhxGEzQnO2_7dYXhv2j0HXfIntr5XiP8rQGXc2lGhs9pv9TinpTr7ei0PYQJDG1Ue5agw-wzzAOoQFvgTdBTLN0uJpoWkImZHyMdmDeaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ گزینه دوم باشگاه پرسپولیس برای سکان هدایت سرخ پوشان مهدی مهدوی کیا اسطوره سرخ پوشانه که مدیریت باشگاه پیشنهادی سه ساله با دو دستیار خارجی به ایشان داده است. مهدی مهدوی‌کیا از مدیریت بانک شهر حدود یک هفته زمان خواسته تا پاسخ بدهد.…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/24974" target="_blank">📅 00:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24973">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMLCBDp0k0tOgje43ynxVAaNvkEzl5pvNNO5xhYgX9a2GjjHHaPal_Tt5mmllfXWNeLdd-m-o5PVip5rprsnpcw-87TErc1rFYYHmrTAjezCm_OKzcxqW4Z8V7TObnjwIZYDD6c0Mhlvx2OGX2EpqytORCWgIYXQxHMdP2nLZY6pUE0zj3YovSYAeQJBNmOHcu356JYq9RsgVAj5YRgt4j6Chv1TykqfXfDMgGELjtP-dobZWAF07dVc0nHKxqEbN6hcNIEuD3JHalrvNnThUTKZCu0bo6QKcycDhM3RC7sYPSFwSEcLlJx9gJIMHpmtZTRK4Yft3gT8gYD5s44eBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارها‌ی‌‌ امروز؛
از مصاف فرانسوی‌ها با پاراگوئه تا نبرد تماشایی سلسائو برابر یاران هالند
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/24973" target="_blank">📅 00:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24972">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IA1Osky6ODwtFPSANu528Qj13AHRXFIxUhfFLqWk_ZWHAZSs2w4fvrDCABiAqQkmQM8rb2qmpk3jg_ZKBx5smQjXyd6QNE02o1M3razTio_ek1yAavKRETZm0CSLfaFnk_yQC3vzv1ZkikxHj8xsyoRwqIPdpg_R44y09POU3qxkF5FHIsWaOkX8bCfmL_dFuKjF4sJ4dXfXDypdbAIz6hwT68-IpFMcx98VucEYKXJsusz6bQxB-c5DLbL7mV9qWEPvkwk6ZLzsVxnZptT1EXNxNkz8VDud6D9GVYZKvvTPVTj4xl9jcD9CVH1Gq2ISITtO4ADh7fvD0lzrkFR9yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
صعود دشوار و نفس گیر یاران لیونل مسی در دیداری تماشایی مقابل کیپ‌ ورد و برد قاطعانه مراکشی‌ها برابر کانادا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/24972" target="_blank">📅 00:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24969">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZY3jupLC-0vZKc2PYdsjMrx0ZtYMcP0PdPYeBhI6_7Uiku6iJ6yX3tjPG6sOR04juaPykEStsbM7EU8Ub-SSoRb65dwGZh31-xnP_kxyO0zGNrOMyuzj_6WRWha1N3VYgzEkfK9bH9V5KmKXvgyha6BahGgxn8uOSWK4nuH8SrHQyGmJ6aPY3EjxpWp2Uj-JrXraiMxbpi_qk3VPuq6MWf26CeIpIFb8rjB_Cl63lSgNUEYstJvkvsmzEF9VurqBw38dmiR8GmxnPHkHlfJSwd2DNTROy3M2_lp5LxLMFUwg-YUFV4xERqHhghw8mQHEsXAarh-ZSv4cNA4t3LYvag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الاهلی عربستان؛
ریاض محرز ستاره 35 ساله تیم‌ملی الجزایر از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/24969" target="_blank">📅 00:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24968">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfpLu3thLj6tDIn76JtYBUVotaDbFI9h6EOKQC6SpZa9Kpz0xg8f6ehxPE6_WsGkfwhFlpCDxpVNDMX47WkWoYGYLymH1n41WN354nhmJP4yO8HpnQRO2ZcGplrscQDLQ8N72LsDnUDpIZVxfwrT2ZiYiIl_btpXBKRRdBNRVC1I6jU_XzvSUkqNxkeDH9jQCf7rLNMoDaxFH_6J7ywPulxj-3YJ2g0o6EpHFE2T7zdd3gDbnJ0BOlGHowQqK_lQCiesYPrltosmvWcFZT_CjFD4ZWwHdLZzFwNVkKQG-lwJ46OPIcJ47gWL32cUy3iaxVBVE9idgBu-Q8psqlr-Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌دوگزینه‌داخلی برای سکان هدایت سرخ‌ ها در فصل جدید مدنظر داره که سعی میکنیم اطلاعات دقیق و کامل درباره این دو گزینه بدست بیاریم و امشب یا فردا شب بهش بپردازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/24968" target="_blank">📅 00:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24966">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6Z7uhIQaroI5vITjYeTnWtbaR3NqEqC_YtiH0N9nWoEuZ7MrfeUuDvYRSGHstjbBsufgjqlBj5AGNOoTHqvH-WwlRRTY_ubgIdMNu3KNrZZOBXpM5vg87NfK80UFcKTW0PkdL4VABMyUnzDg7yK6vuxwbT6w3IzcPPsOpKK9BivJ8kJwbDE9exnnq0JwkxMYwwr3HTsL7FztpT3XH9Au3GEjghlc940e2uQ8GIDONbJ-XFvT4DstURvaadX79HZATiOyzF3PBnlp1rnoUQ56pl-kAyo_E0uSkHkFGS4QZJ88pxT1EC0onNW_0TE91ijKw8VxpH1EGwIMwNyXWQzBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه گلگهر سیرجان که اخیرا قرارداد مهدی تارتار رو تمدید کرد بندی در قراردادش گنجانده شده درصورتیکه باشگاه پرسپولیس این سرمربی رو بخواهد با پرداخت 20 میلیارد تومان رضایت نامه تارتار صادر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/24966" target="_blank">📅 00:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24965">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRUHhxXZxlJ8p5co5_p4E8Z9OJMU1Ige-am95NeyDqDly_RJJK-h03hWZHXnEd7fK5NBUVDJ1a64a4y2mEfjmA6hHfrkLfzNUHMUpVZUDTlMhqYVOy3SW-T4LW3pzjO7NOYNEGNC2lqJONw8olx_jDpWoEJcFrjXQWF6Llz2EY-bGduNNO665Y5LvD6FIUWC90-VJBwlmfvlIx54jqMuLF7Tj5Z5oL-EzLhHFqs5o1lgvKNKsV0QmEwLsKoBatcVHOFROT4ZuelFyOP8eCCg-WPnWNG9JW_HNKpHfZk7KYVPRtLcB-KBBPTxhJztX6EahhZJq7hDs0xVRCIj0AmznQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛باشگاه‌استقلال برای جذب دانیال ایری پیشنهاد فروش عارف غلامی، محمدرضاآزادی + 30 میلیارد تومان به نساجی داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/24965" target="_blank">📅 23:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24964">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0aei3YeQFYkMMSWxw4J_5-32KqurHNypHiJKU2w4Qys1Hkwq00e3L6TmNEOEGkjdD6Nxv-A1XA77y68rOjHSrUXqoMY5nEnXU_Ai51lw5IKKluEqjA3vmUF4Qfks1MXVoF-xCNJOARye2MPO38yYn9L8rdL55H55ABGmPYDJlkO67CayY2h05MNQ3tjVQEcRBG1tIbODKbUlDSsnPUZVzNtevqIRwyN5LUNwWMwN7CdHQTMrDYQivJl21tlXGLPdFn9qT7Bv7VyrjXG_MytMz8LlfUlAeAL_Whd7jXLCPiNdFkpG3sZAv7uKq8crOR9aSFWjoxC8v7cj7N0j6r1xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
💰
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس با ارسال نامه‌ای به باشگاه نساجی رسما خواستار جذب دانیال‌ایری مدافع‌ملی پوش 21 ساله این‌باشگاه‌شده‌است. سرخپوشان به مدیریت نساجی اعلام کرده که 90 میلیارد زیاده و تا 55 میلیارد ما حاضریم برای رضایت نامه ایری هزینه…</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/24964" target="_blank">📅 23:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24963">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NejeqjEgcZ7u9wQUOEPIlQ2TJgvhdP7mHL4BZ0p-nlbaExgyZwS4U_5xnpjHXI-wYl8WSG_3bNVKrPfpOEicnrIMiWBD9X4UMfmQySePL9NmwugSDirD1bZ59H5k0elMFzaD5lSaqG91z6lsG0TznLiYee3a2VG5R1jOGxo-Bb6a5TiISMmBP2ARElIDtfBbd_7roX16e3MaUSQDnV2haRA8pmnHrVM8Kzl7BRUN2V-Y1eypQBUbyCHd7LkFO4cA73589cRmD8GZk6e9PYN1RZONbstQXF4usISpk0lc6vLPYl2UYcJ3aYiv8qoij44tk8JBqo1bYd3gvdcgpcwWiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
در بازی شب گذشته؛ این هوادار آرژانتین کیتش رو میندازه برا لیساندرو مارتینز که براش امضا کنه، مارتینز هم کیت رو برمیداره و با خودش میبره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/24963" target="_blank">📅 22:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24962">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJdmk-mOEWuMojumFfEkrdfbyQsblqBi0N5qdmIRi200yIv4c0duhWl5gCLl3f1KvyvS4ccwk4q58XzgXIrkt8jWZjURe5RBB3Eagw6qvG-8QlfJTKWR-vBnx4xEb85OihpagDxFMS7alpa7tqbMB9F4z13Ir3EJCu0EmV6GyCUmbB3lp4R66NePXFbLwy9tU5h0k7MK9v9aw_YXk6uSl8sKNPRNRC_mopPlEQtVt8bnY0uS59Sx2S62ZYRiQNi3xVICZxoUIETpqg7uwlAbHv1aRVkifwBi8RJ9WFjxYXW1wGtMker_qt231RuNrtFf7tCyZGZxMXeSy78mQihw8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک هشتم نهایی جام‌جهانی؛
پیروزی ارزشمند و شیرین یاران اشرف حکیمی مقابل کانادای میزبان و صعود تاریخی به یک چهارم نهایی رقابت‌ها.
🇲🇦
مراکش
3️⃣
-
0️⃣
کانادا
🇨🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/24962" target="_blank">📅 22:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24961">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olDMPHCtKX_PUDuQyHKzciQ9AbdQgYp-kc6hks0fZ4ZPDPpK7JlId1Mg0wDVhOMbn8tPaRgYN_oz6NldZNls8VoCvLdO1xjHNV-dL_hpBR0dgmES3z8weDMNVaJZ2rA4_R2OPrZEMzarBDGSV6P0BIn5QoubwxmBmr4YjbaMnZaIV_X804VtmkDEzW_3LvGlPgSw1J1-05fvctpYi2yYwKm1KxoRoYzAPCSR3IXUpW-0wdyzE-uIxUwSqU6CvhcHCZZ48HbjX_ijXBeaB_v25atCfKvB5VFv550nQRFiVK2KceAcVaRbmixJEpxed1Swumcbj9PUh1MBLAiDpLOgxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/24961" target="_blank">📅 22:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24960">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xg5vO8lLH8MVMJKU0c0rgfhb22G149xXyKXTmo8aYXDDEbeFH_CiHL2xRu2VuOd1fVrUgq_g0_hL9OkXkHuXFjfxP77P36KYJJm2yQQaDF3eCh7walFWbRL0Sxld1Vc3IvpHwQrAdSJrarPu2Yn_nPXFdCItkEKPJgFkUv3WoM2kh5c2Rx3ZM7lIFVvM_hYhWpb8_OmYHvtFocQWeZ55Ci77jLaX5qEXQ2jTMD1vLJceMb6IMQneVqAisOALDwK6s2R94OawAnj3aZrmqym8qG3Ms-gMyy9NIg9hJD6_ZW_UqsBhOna0vLYTO7jofM-Yjqb6_cevi_JHQppCBQZ33Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هروه رنار سرمربی مراکشی تونس بعد از دوباره از عقد قراردادش از این تیم جداشد و در حال حاضر سرمربی آزاد بشمار می‌آید. کاش بشه ایران آوردش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/24960" target="_blank">📅 21:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24959">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbV6diytiukzR2Xfzh0NVcbi0DGoXUHKT70Z5geJAb13E6IOInxEvJlZb0MKdkHX3ZckXVBi5t6QQSCJHm1lbK9Eb3kw_nHccTmySz_bOqtCyTOt29fkGfmMdX9mg7diNP12UFsYqGaKbqr6igJDoWF6pdmQvGLQzu8boCiiNMq0kIjKbB4M2Vdw51tjeiaPod9Uf6Le49vwGpHKVqIj8coC_anKThDscknK7uULzzy_LonaYhtF6W4pFoL7fLsxg8-YrPlDfMWkvVPIWLEPfGEbu4aPKitL8lTPfTjGVOZqtbNRlesO4wOi9v9DxLDkRUqRHCixwMWjIwpxv_mZ6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇮🇹
🇧🇷
بااعلام رسانه‌های برزیلی؛
کارلو آنجلوتی تصمیم گرفته بجای پاکتا مصدوم نیمار جونیور رو در بازی‌فرداشب‌مقابل نروژ فیکس کنه. نیمار در تمرینات روزهای اخیر با انگیزه بسیار بالایی حضور داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/24959" target="_blank">📅 21:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24958">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GK9vlnLhAAYvyj1XPB8jPvid-p5RKRNUezSz10O-8Ro2s8w4oYYVjVSyX4fF470JTdCK-WlZsaKc8xLjGqlp-8W8Zp78_ba1tkSRSG-0YnVBM7Vg6IrJc-CpPSnlC53MEmmWQ7PeF7hdQmrga9tZK4TJAyXRzdd_eSvyeLK0nRG81niWpsRLDWhVxbAfP-X8QCV4FH7XpbLDD4cCCTf4UPZMvj5XmMizoY05nVXqd7OUXahH-sDoNGSnOZEeYx_xQXOkjlhovfBW-4RgV3gleSpwe9YrKOjcFd3cvZfuZR9bcnQHy3kRdPbFQzkuCX5mRkpyzkiSZ414TeVLSqN1sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
منیر الحدادی ستاره مراکشی استقلال امشب در تماس علی‌ تاجرنیا رئیس‌هیات مدیره استقلال اعلام کرده تا روز شنبه با خانواده‌اش به تهران باز خواهد گشت و به تمرینات آبی ها اضافه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/24958" target="_blank">📅 20:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24957">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2DGfM5caw9uFiF7sP6DySmA20FTlt9GjcswCB5FWAuITXIcdiZi4m1C0AQskW-OOZMTdZ2A2NGrKA_KbbiMe-CP8Z7vm6Z31vXTWy5wjs6l0DnuHYKoBhJZmHTZDXsgjSGRhWvO8_4qtbLJaFXQZjqdZIM7fIfDAAyHfC7lmQ4KMKbCmw1lQpo_x5gvTT6EDO-Qgx09SdvULPB_lly3YnofHE3kh91Ebjop5p1hkJ0Ej0QxYTAutiVSOeg3_MuO9qakOddsTLI-DzsFH1lR0P5FXtYCD7UgcR2k4_BzX8dktMLjnZojIOXQxwNJYD_EmwuPK6JKc4zILHQvveejVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/24957" target="_blank">📅 19:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24956">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAgsEotmpBpLH8iz5s_QfBpXyzucWwo6v1_yWkgGc3v135MD0hJJ_F9N7j6300uS9AM-YJYaujguwFQqUCrPMTjXNu3Ie_wm591-QoP9f-6lIKHyW1uVWgh8QHlCpLn7trqwZZNoAykaD_TVf5lV7DJ2G1fw0xpZRLHiyjz7mR-AYvEQvneMDFU9ngm1P9qAVp-uL6qLykJzWkuYB9lfCTvcdBPh5Z2-g9sX031FVPl53CQT_qyK_VrzeMlZa4Yxyq3HsjTrz-NFwmb_LqpQpmc2kWK2NamKxVjbgq2ctWTzJEJtgHdrkZtMjJQGYPa7_thldk6jyxAQy2Jdro3SfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گلزنان برتر جام‌جهانی در پایان مرحله یک شانزدهم این‌مسابقات؛ لئو مسی با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/24956" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24955">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‼️
خودزنی‌خداداد‌عزیزی روی برنامه زنده جام جهانی از دست جواد خیابانی ؛ میگه اگه زنوزی اینجا نمیبود همین‌الان برنامه رو ترک میکردم و به ارواح خاک پدرم دیگر به‌برنامه برنمیگشتم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/24955" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24954">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAZdR_BNYgYVAkiosLQQohyljk2rcEKyDik0_k9BCTQ5F4NdTwmAK_HiSMqeNURBTTdVhOqqVjdYCo1iq87CINp9tNhYbnGJdEVQ3tbe-KJ2fm1zwe5_AdVsjusBHMdMkvzQo6O7VH24mIedOoxEBtm7rVMpIoGsaVWoZpm-mOkvRRdcZ7j_l1Bfy-M7p-KYho1dRgtAj4RktaiNdMMX2Jt0md-gjJTd1NBJ4KPzOX5SQ7rODNGUFHihLePjcu5SH3nwmxvxrqz_xjgQLTspzQs5u5w7VxfKeEeKwaDfjAjbS3fF_VSQBQureEX3r2ZFiNey9qdUIqM74Pl2O4ZUtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
مراکش
🆚
کانادا
🇨🇦
فکر می‌کنید کدام تیم برنده این دیدار خواهد شد؟ رأی خود را ثبت کنید و اگر پیش‌بینی شما با نتیجه نهایی مسابقه مطابقت داشته باشد، در تقسیم جایزه
۱۰۰۰ دلاری
بین برندگان واجد شرایط شرکت خواهید کرد.
💰
جایزه به صورت مساوی و مطابق قوانین و شرایط سایت، بین تمامی شرکت‌کنندگانی که پیش‌بینی صحیح ثبت کرده باشند، توزیع خواهد شد.
⏰
مهلت ثبت پیش‌بینی: تا قبل از شروع مسابقه
👇
انتخاب شما چیست؟
🇲🇦
مراکش
🇨🇦
کانادا
شركت در قرعه كشي:
Https://t.me/betegramd
📺
پخش زنده بدون سانسور در کانال تلگرام
🚀
برای تماشای مسابقه و ثبت پیش‌بینی، به کانال تلگرام ما بپیوندید
عضويت در كانال
Https://t.me/betegram_official</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24954" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24953">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ie6j6pyeHmb4qyNfTz1gC-zzI2BaB8QG_nh8BHpns4qnB_q9EfF294CwetNQfc1jvGCt0ygkmPDv9ytJXz40_X44n2v8581zq6YgBtThVMfpSxU1OndCYeucaG7-W4P9iYK0hU_g2Jm9TEh21SRTf0hjm2dh5T6g_mq8Rjl7HTM740FLYSdq0XcOPlDE__ph-WVtuFmts7u4Lnrr50jge86ATSMsk4ymSDGo3jTXKvyPxdGIXA6m6yk_jZ7PBdy4g9U0MUXzky3TQfOdw4Lty7O6PPjTDdGeMop6muEC2NErvABW7hQtoS9QGTYXGYCsUZxeJYUNSby7vb1TsW5kYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/24953" target="_blank">📅 18:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24952">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/td3JxsWvd5O4D1qvFC6mNjNEut-9C3JURyuxorf7Uj3ra6Cf8VjZinTs7dFPhp-NH53vmNhyKMppxSOhK9tfT0KRAxMUU8A9Ep-Ab_LJFbJRRh46-fXMARQneLrNqY1bAxD6rcP2qV6xO82bT2q2tFkwTzzzlNn9TKy95t8_ju2erS75NDwEbN4l9boB42mjED6ID6y9-Z1xyErXHNisaNpDGCzcwNiKRyLjym71gv4f4u2YYUmAoDCmhUxvsRZcc9ZhBKa5bi-A9NmhTjrTIMAy7vJy66zQw0Yq587bgfne5J1pzYPUt5YPCHc1ghTSr_5vLANHX4c0F7PfNY7KFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/24952" target="_blank">📅 18:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24951">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZXM6djADl6DtB_fY6sb3UB-C5tnyASb7PD9jsvzLyPwH5sXl2EQAf5-mN-hX2uc1-dXom-Q_B7VbDxtGaxp1ibVXPMkAIfSy3oj3G4-LdxFrf82EbS2GH2vgv4PmcwnGZTDIjF0eRGRWwcIhlQ14Yc23y7FG188YdEaiyFaXLE1B-nEQyiYXsApncJ7mYW3RhGHqTTwJ-ZaBBSsIHJ7F2oCuJA-vp_taG25Oz-AThVXk_q__fh3e1Y0o_z4OCf-UFi6rjUJavtMjGxJQ6ZOCospXUcyCWIuY7lsxa8uk6Rl9iA-EquDJjMeEJyCpz24Io2XzPRghZYzDo3mUTBgXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا
؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/24951" target="_blank">📅 17:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24950">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BU7_6jhV3vjq-Di-KvWhLzchvSg7vWAHdhJeCxYi_1aBzwlR2YqwviCi9_ACekjBNT9KsVf7R5aW2YTD4wyXEQqp2bMiASERs-hFwg3wNMjtOmPvQ-dBQBPJJI64x1hyKOKxcbtRCQjl8Kxh72phgqIVZrhIg7y6SDn0I6672NHBJgC2ALiXRScXgkKqorUmPYc9KhrhL7cZ8SXaHXmf04do14wjUFU_0fb6PsRRJKv2xdPXinP4vIr7q9JIERQQuTQ7gjwvrKwWzR60y86oKumshQy3rVSqApka-9C-TyXtOprc8HIqCQW6O5bnUlaIOv8sGrxy44Of8hPDVfJJCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌دوگزینه‌داخلی برای سکان هدایت سرخ‌ ها در فصل جدید مدنظر داره که سعی میکنیم اطلاعات دقیق و کامل درباره این دو گزینه بدست بیاریم و امشب یا فردا شب بهش بپردازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/24950" target="_blank">📅 17:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24949">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWoRDsnN5OkrDp6FLTyNCRr29EBjrboZBhBzbqDZjRjECLmAats2fbNrtRt3RQiYmg-c6kKUjWB9y-sgkeLhpPZSJErf29pdcW8Vq1JI8riepx2trfdYqRRe9t91_B-hVJIJN6SKC7nH8J3H1T7pcEI41C8Ju9x7sZlFjpRWbA0nrAP_02bLRLLRnD310Ei4DT4kleIbkkW5Ekuk6gI87DaEw1RODLTXSa-6HAgc-b_uzkyAp_FAC1UTrJzUVfk7LCzEAmJYs_OYa9ePTZmrrG0NowTp5S1M50IMW7bEtBffesFCRCN2HcazNEy4KNZAhva-GBLMAQBZUCy9LLR5zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/24949" target="_blank">📅 17:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24948">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n48hllgCldtJZ1RAWYBwtHAfDnCr3m9ze6l4ti-2xAo0fr1BTO90oHao8HMKp0AGcI6ZQ7YKHLcHbQHDs4vEqa5OehtggXwtps_FxY2oDZNxpk02AfftJZQiYlLHR6WekNehgYIxiPAKw656Kltvb9UWnuU3DwBjoLxYVNanKYGc0Mj8c2sB5Q2ode0TU4f9GWRW0ymYPpGtCEjBIbRquy-4G2d1m5Z22qGnpknyEH2c9LifvgDddZmM04LovZ-2H74X5gDx5VrtVOD-ZfqWdxdo3lTBAMd6DNYtUqJUk8Mk46X6SskW6-3xGmnYatMELj22r5d3z-RXCJt65HefPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
15 تا سیو مقابل ستارگان اسپانیا و آرژانتین در جام جهانی سرنوشت یک بازیکن 40 ساله که تا قبل از جام جهانی تنها 50 هزار فالور داشت رو تغییر داد و به رکورد خارق العاده 20 میلیون فالور رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/24948" target="_blank">📅 16:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24946">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKP0AXTD3chVN__fRpGiInsuELPXO7VGS_0iqDsFvxhSR8WWrYJ8YchcbWsrF9A59_Um1LPFTWWSxm-nXCD1sb5odxkCX0XJV0T_7f5aVkK_l9LlTQYUWmkSqv1CeTNajqRZ_NKqpkFBgqtvGlemjE-7vZzFOqZj4M8uFNnE4TV3UeWHU2QP2kuX8ks-iph2kxjaYDckqBPN5x6BbmVnP_52nPMr6gmzzjzN1xxm7Vk3Qkp8Y2wjjCnkdYzjWL9AOw0i9LhhFi1awpfN9o_q0Pu2og4iuwUHXwHZDapzDjLgCXtNr2zqxwvxfhMI6Z4pmSjkReHtNgx2plyVtPidWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R-RsOcCuKT3X_sLPnHvDqUWXIhRQYyMFaTGuEpaGFoQ-Z7KZ4q7h2BkwF4iwKrI6w0DcUuLOliDZ904xeB5PmR2wmhzI8NOmmZgTvjAbhS4_uWVRFpfZrLZE1OhSGwQ9Uo5tx3ikNwpMQ9B_TC2VAY-XG8sx1hzgQel0Zp9kQRJHi2sk1kOpY41SYYRHrXnbwSE470ZdGQXoHQCzHtX6PuRg2IsiJk_WpmzFByTivq7fhksovOB23MBCxWOLIxusUenxkMIcQnhN4wlncHZfTy_tKsUMJiIxKlKq-2VkfpTANj2DbaPd5EHeaa-BUqFg2v3c0ZbPt36jFcD_CAzjKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/24946" target="_blank">📅 16:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24945">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOXDAnlrcHfGM4PBOLTpVHQDmZurQPbBGxX7wnnqnKqZW76k7mDWSlqJmnvv5chtSWB9Y5_DKSVgAtXwlezo-L9PLykN0G6bAUf9O2VFGzbZDDKIXl3-jWcn5RdEFJZ6slCCc_VdZQxZmz79lpixd6IYR3rlZq2BlEX1aMMHTgWnUbOryAL_vBKpZYx5uF28vhIh_ILMO1J1Y-tUJ6rfmqFbsUH5VYBl7jY-zwY39eZaV6D_3JfcKJ1Wwc-e0yKwsf2nScaS-jMZZ1D4enYTDTza-akv87rBHS9ydrxwdzUmIrLAZFLJPrV5ww3nabfY9lga5pt0RWq2ZMmllOKmLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مقایسه تعداد گل‌های لیونل مسی با پیراهن تیم‌ملی آرژانتین در دو جام جهانی 2022 و 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24945" target="_blank">📅 16:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24944">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDFdq5NqIOViGnyQoaiXYRXtLGKIgCP0FFupxiszSDDlSINeN6d8gp4j2RBeby8bcKvKcW5ix-YTr4O0ipw6LKiuKcVCb2mtZUnWMLT09eSbLobgMqB64qvMfEDaZVTLCa5gqAYgXM6HGUdUiUe61KYHWcWlXS1fjP7KEL5v5gozmyVxF4AOl_dZe3ogIkMRmHaHRLTKZxOH73FdR4Exx6c_7GQBkJWju0pxi-2O58DZa2G1vV4XZS7K2Ix477tglxkBK55_CRnw1453RnhE0wFH2ultkl7KusUL47mJlK4HiG2ttsxBRNyCv0ZyCcrLa6a-U1bn02p8TFuUt2DW5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24944" target="_blank">📅 15:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24942">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAdchw9ke8Nf2FuHjxgT4KOPB9AMr5qGlWD2cTnkQ7a9h8a4yWevBf9MtaKt02VSELDrYtZr7CQf1HMlvGQJHP-69nDmxdv_kVHcXCKGu_AtXogMnGqAQ0GwnRjwNwYEg2sRBDPaJ5fLywhmJwUMXtZbb-0XJsk_vEc3RfyVYNbxp-x1MgCgRgUJEh66S2ga8tHQENMGD0ncYDgkvPVkBBFcbzMtLvjpXUpQzuplEyyFMyzz5QsA47x3QR6AmDOEgZvmvCHOF_JZHnyqo0hxdOHPJsMPvDv9w1bhFvXnDQsPK4yVsSUe62HS276P9SAJFwjBvncCp8_ZRzVvIcGGKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات
|امیرحسین جلالی‌وند وینگر جوان فصل گذشته باشگاه استقلال خوزستان با عقد قراردادی به‌مدت ۳ فصل به باشگاه سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24942" target="_blank">📅 15:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24941">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMdT2jWYmYqy0fXeVCLzh1ir2Cpibe8Ell8e4QhicA_xFx_1t3s37i4n9XoVjOQgJAw_J-8ZaB9N_8ukuDISCFGpGJ82xu3cOsLGoQT3VugcEb_TTKK3UYXNUI1dGDwt62NYDg-Q6d9SDqRjFq03xLMxPweoSnsC8_3bRdqSPAGrD9JntXSxwMFsLyzxlF0SC3SUQhu7yZfqt7z3iI4uUdb7M9KH-EtKdQldhZ6LhEgISa_No9dIhpzpQdIcxn9Lkl763LylWqtT0kfk6kWvdnBz4EPd5GnPt8OK1sDUzSBa67dx9Nx1FUXSrNmIFQF0FRLs452p9xnsPefFqtcMrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مقایسه تیم های حاضر در ⅛ جام جهانی 2026 با تیم های حاضر در ⅛ نهایی جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24941" target="_blank">📅 15:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24940">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nn8XWuzN_udvJBIAZ0Xxm2M_UGRs1ihossxkkiYcKp36duSfZmmuv0rYZOUS8PgD6t4oqiZpMq9KnBoeOft5JT70k-eejwojWQAe4uAN8QnBPI0qIYlVsUZv1n70IIwcK8k6HKUP_P6r3zzIUs8fQnQqHfKkeCtNIMNr0e47Z0jCrQJfEQ_nO-Ptz92kQgGDGGe-40YZmHXT6-sg3yhkE_g9bHcWIM7HDQs3vOq8jCXnAVeFnw9arNlxOWhfRZIF5Vc6RiCT4XIfkgMAdob4NCsNKGqljghheXVyMF0Mx5LSYwYwSZRS26vUD1D4e6Oh4fuQqcpJhpZG1r7yDwnWmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
همه از عملکرد نه چندان درخشان بازیکنان تیم بارسلونا تو تیم‌ملی‌درجام‌جهانی2026 حرف میزنن ولی کسی از این حرف نمیزنه که این نبوغ فلیک رو نشون میده که با این بازیکنان تو دو سال اخیر ۵ تا جام‌برده و تو سال اولشم تا نیمه نهایی چمپ رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24940" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

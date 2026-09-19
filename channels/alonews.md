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
<img src="https://cdn4.telesco.pe/file/qLhLmHA8OLXraenVcJUmytpExJKMH8newebthXSX8tIjEnzP6QW2pU2pOHXKeYM_l8-IbnaqMArVnH779FbVc-358vSHVVto8dXiOJpE9FiHoUiHC8mLwHnct6KT1x9GnwGogZBTHXIBjGi0qHDQtdcKq0-VKRjbgMJgs7u6Oj-SYmp-nSvQT6Pn11h2Dfx_QS8y-Er9pPr_Oi2-cIDz9vQAgH2iPa0byVHs9H0xgTAv8TCNybYDNNhQhMagss1hK810mOOzMJr09dChbMSpVcBmGJc51nzAPTlN8lTg5ol9IijeO9rP-exxzT6c_Hs3vk-2KJ7555Xl7Mwb-DgWng.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 966K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 15:29:19</div>
<hr>

<div class="tg-post" id="msg-148191">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
یاشار سلطانی: کشور صاحاب نداره! رئیس جمهور و رئیس مجلس یه توافق رو انجام دادن اما عده ای خودسر موشک شلیک کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/alonews/148191" target="_blank">📅 15:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148190">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
مکرون: خواهان بازگشایی تنگه هرمز از طریق دیپلماسی هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/alonews/148190" target="_blank">📅 15:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148189">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
واردات خودرو مدل ۲۰۲۳ آزاد شد
🔴
تا پیش از این، تنها خودروهای مدل ۲۰۲۱ و ۲۰۲۲ در این رویه امکان ثبت سفارش داشتند، اما مدل‌های ۲۰۲۳ نیز اکنون به این فهرست اضافه شده‌اند. جزئیات شرایط جدید و الزامات قانونی، همچنان اهمیت زیادی برای متقاضیان دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/alonews/148189" target="_blank">📅 15:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148186">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Na3IE3hV-dioG2DJDj1d2Yn1aNCq8xtEiN4cgTSxf0MSQvuDE_gyKsyTa33VcKDHprGT40149XhWRxnkAMN46jWTFAa1PSfMTESrdbSVhaz8u3Sf6MFSMTSPAakB6ZsVmhgTavf4w65lQ7cGluRenRDzcq0AHHoxl_pnbU3fBGieRM6yR-sAA0m5Ams0wvIzVBR0rwTOnW2Ufqh_Q92JbysOfShErvTWq8xyWnk6QCpBDNllzzMUhPoRFL8RxELNX2WlHaPaGM8MtBI0ZSsRMKW84ll-dStmBjW-zIU4IUOKQt0cC4d2sxs9FphcweyLzk9iMmYb7aHPZ5DLUM8hDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a4c429f9.mp4?token=aD03XEajy-a6-9u_uEu0n9aUQmwh4VRAIjWzzN-3wHLvO8lB4rskYYMgxFk6sHVqiA2vg2pChY4v2sBnBII_72Aap53E0itzZH4OaW9395ncKepPLtqZ0WwowWl3MS5-NTmJLAJcsl62odnPnLnYdJYeZv4I86Vj-fyDoPj9S787skHEvCYLgM3hohRx81RdQ6JWIMi6ic0lcWBBliSUJmtlkuYSzY1cntRp7irrha-hZ5PelxhUipVM7tYpzilr2q_nmO4WjYJYfXZ2fP9NFZl_PhSJJgf4XxIwbJZQ7COAZ_YGWp_MXnJUIpyuwCcFh8IOk9jkRtzfkQf4BoPTvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a4c429f9.mp4?token=aD03XEajy-a6-9u_uEu0n9aUQmwh4VRAIjWzzN-3wHLvO8lB4rskYYMgxFk6sHVqiA2vg2pChY4v2sBnBII_72Aap53E0itzZH4OaW9395ncKepPLtqZ0WwowWl3MS5-NTmJLAJcsl62odnPnLnYdJYeZv4I86Vj-fyDoPj9S787skHEvCYLgM3hohRx81RdQ6JWIMi6ic0lcWBBliSUJmtlkuYSzY1cntRp7irrha-hZ5PelxhUipVM7tYpzilr2q_nmO4WjYJYfXZ2fP9NFZl_PhSJJgf4XxIwbJZQ7COAZ_YGWp_MXnJUIpyuwCcFh8IOk9jkRtzfkQf4BoPTvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر دیگر از انبار ذخیره سوخت در فرودگاه بین‌المللی شاه خالد در ریاض، عربستان سعودی که در حال سوختن است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/148186" target="_blank">📅 15:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148185">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bd3300290.mp4?token=t-ejjACXnsSyyHKDCyEncZAqgYUe2ycHUL4cygvXQ7p2S6LvvFQsT-sOfvE2Ea78-B8yaxXP2yCrJsb8eRrjAVtYu6iIodxCLWW2y5Qoi5Z6buknOOuRUnzWD18iKspLoDF6lz2RH7gZWa5t6VuoufavU2xRjgZ3XaRfChf2Ajzg9XE10kP6oqtwgjPx7Sn2Bfbo1urtexxhDJnW0bPLLFA1ASPSPRSrvnq8n24_K9wqyOiitZ5x2VnATIWPCtOUs506W05u7_z-H6lyZcctDzEJxOflW9IY79bExB4jkuCrSUBL7bAerB7lUEpI3ahWm1jlES7bd6n9ydyrG1X5rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bd3300290.mp4?token=t-ejjACXnsSyyHKDCyEncZAqgYUe2ycHUL4cygvXQ7p2S6LvvFQsT-sOfvE2Ea78-B8yaxXP2yCrJsb8eRrjAVtYu6iIodxCLWW2y5Qoi5Z6buknOOuRUnzWD18iKspLoDF6lz2RH7gZWa5t6VuoufavU2xRjgZ3XaRfChf2Ajzg9XE10kP6oqtwgjPx7Sn2Bfbo1urtexxhDJnW0bPLLFA1ASPSPRSrvnq8n24_K9wqyOiitZ5x2VnATIWPCtOUs506W05u7_z-H6lyZcctDzEJxOflW9IY79bExB4jkuCrSUBL7bAerB7lUEpI3ahWm1jlES7bd6n9ydyrG1X5rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زین واکر بازیگر ایرانی هالیوود با انتشار این ویدیو از جمهوری اسلامی حمایت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/148185" target="_blank">📅 15:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148184">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
امام جمعه دزفول: دختری که تا پاسی از شب در کافی‌شاپ‌ها و فروشگاه‌ها حضور دارد، نه فرزند خوب نه مادر مناسب و نه همسر موفقی خواهد بود.
🔴
پ.ن: این یکیو راست میگن
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/148184" target="_blank">📅 15:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148183">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
معاون پزشکیان: شرایط اقتصادی خوب نیست؛ مجبوریم پول چاپ کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/148183" target="_blank">📅 15:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148182">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
دود از شهر ریاض در عربستان سعودی به هوا برده می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/148182" target="_blank">📅 14:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148181">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d0c461c6.mp4?token=YYe7CAtB3cUYkzlFAJa-nGRpqpV1hsDiB2E2xGqSXRR9wA0M-RTMSUKUUlXyox6uJo6NSDaO85heRonzlAw3MUpAZPVMHb_p5Yt-AS29_zuyywjdXqmkpnqm6xoSmqKb1iaJYQL_pDOKElFRGBm3yZiNQU58lIeMXW0gpKFXjJVy96Yj53rYnLPgl048gDGy0ByFZ0j3IzPPS-KDI3GOUKZRyAl4GlQ4OBQgWht5WAhudF0g_7ftKT1JOgLEunQX1xNjNQ0x87gS-ZLjn8g_nq3mhc0cqYI6Uz7OzQnPA58p_JD4B_59cJO_wldwpphUKOWPodbx3XrYd4mFC09vLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d0c461c6.mp4?token=YYe7CAtB3cUYkzlFAJa-nGRpqpV1hsDiB2E2xGqSXRR9wA0M-RTMSUKUUlXyox6uJo6NSDaO85heRonzlAw3MUpAZPVMHb_p5Yt-AS29_zuyywjdXqmkpnqm6xoSmqKb1iaJYQL_pDOKElFRGBm3yZiNQU58lIeMXW0gpKFXjJVy96Yj53rYnLPgl048gDGy0ByFZ0j3IzPPS-KDI3GOUKZRyAl4GlQ4OBQgWht5WAhudF0g_7ftKT1JOgLEunQX1xNjNQ0x87gS-ZLjn8g_nq3mhc0cqYI6Uz7OzQnPA58p_JD4B_59cJO_wldwpphUKOWPodbx3XrYd4mFC09vLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دود از شهر ریاض در عربستان سعودی به هوا برده می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/148181" target="_blank">📅 14:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148180">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
مکرون دیروز  صبح تمام سران سیاسی فرانسه (حتی احزاب مخالف) را به جلسه‌ای محرمانه دعوت کرده بود. موضوع جلسه امنیت اروپا، احتمال گسترش جنگ در اروپا و خاورمیانه بوده است. جلساتی مشابه در آلمان و لهستان هم برگزار شده بود. گویا احتمال وقوع جنگ بین کشورهای اروپای…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/148180" target="_blank">📅 14:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148179">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
رسانه‌های عربی: پروازهای فرودگاه ملک خالد ریاض پس‌از اصابت پهپاد یمنی متوقف شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/148179" target="_blank">📅 14:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148178">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b27b34a2bb.mp4?token=aH0ZhN4bqfn_IxdGnUTLTOZFn91jZzhX2dRsLZteuOGfLwXPQBBGjuY_PFPRaopzCxQ0ebaWVwy5_23237kcc6-JlZW4qTuSlxRNrVtxsHDXqPapAhhFlDGa5wOhxRpINYihMGXcgsEAOOmt3DPXK_EU-jz3AMB0hpLzRJum17uwNc-H9ftT7aG7fIkq_mUPtl2UnfvC_pGMy1hqT3pOt2_tNSYdxjzAfxH0XmiPGcecivHOKOG_g9PI65i3_waFrr2hiBPwGwCzebXCjthc-8XR4DIwUYITnpoV7UmvF8sNUo5w25rhYK66boQN8Qp4v4_GcfcTwnMjAevl1T0XNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b27b34a2bb.mp4?token=aH0ZhN4bqfn_IxdGnUTLTOZFn91jZzhX2dRsLZteuOGfLwXPQBBGjuY_PFPRaopzCxQ0ebaWVwy5_23237kcc6-JlZW4qTuSlxRNrVtxsHDXqPapAhhFlDGa5wOhxRpINYihMGXcgsEAOOmt3DPXK_EU-jz3AMB0hpLzRJum17uwNc-H9ftT7aG7fIkq_mUPtl2UnfvC_pGMy1hqT3pOt2_tNSYdxjzAfxH0XmiPGcecivHOKOG_g9PI65i3_waFrr2hiBPwGwCzebXCjthc-8XR4DIwUYITnpoV7UmvF8sNUo5w25rhYK66boQN8Qp4v4_GcfcTwnMjAevl1T0XNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امام جمعه دزفول: دختری که تا پاسی از شب در کافه‌ها وقت می‌گذراند نه می‌تواند مادر خوبی باشد و نه همسر خوبی
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/148178" target="_blank">📅 14:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148177">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4n7eVKqJH2J2LK5WbxYZ40EnUjjJsEj52BPr-3ahZ4RiQ-kGu7j-Akb7CeNWKg_8ayCBvkyDvM64QGbXKRgSETcO1xh8rH5vo5k02D6crInlje06yNouA8ETk35XVFm7vaRZRQWfNXvoINMqywpyOQk8oA-U-ELZ2jvNFlrYy9AzUI-0yw_pXeHS7GvwhXMHAPiUHxWSanLa4XWdLwiRhhAkOga7F5UAAO1ijrEAY3DWfxHHHDs9AAPSzn0ZhuKTWHWz1aLe59gXPre6o6xUITnPqMr6yrvU4jTyojeUz35xyofH0rCnSve0mk-Z3XzrD1SQBnN5CAcnx8fq8hCTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرودگاه‌های عربستان سعودی با مشکلاتی روبرو هستند...
🔴
تقریباً ۹ فروند هواپیمای مسافربری قادر به فرود در فرودگاه ملک خالد در پایتخت عربستان، ریاض، نیستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/148177" target="_blank">📅 14:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148176">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
رویترز: شعله‌های آتش و ستون بزرگی از دود سیاه در نزدیکی فرودگاه بین‌المللی ملک خالد در ریاض مشاهده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/148176" target="_blank">📅 14:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148175">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
وزیر امور خارجه پاکستان به همتای ایرانی خود:ما بر لزوم تضمین عبور ایمن کشتی‌ها تأکید می‌کنیم، زیرا این امر به نفع زنجیره‌های تأمین انرژی جهانی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/148175" target="_blank">📅 14:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148174">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bcf4947eb.mp4?token=WVUZiAwUtUI7hf5TMqL1Mb8p4mgpq9xLlbb_pS3Awl3BfTj7wxVFmxfRNws184N-6sBJHvjCC1IcYgsBHO88EwMz7TTAswEn2Kcv8b9oR9B3lA8eePdYeVSuW71ArsecNtJLlvk82G-gepn9VdU-uY9rbJeNDJnbQYjw5zfFi4hk0UXpd4f7_ISXzAsmkZatP2nv0jpKxGIkx2ssoHLv7tDMOzMT4rf2lLS3wePvEPrlDGb3LP1muu9zdOQXls1MxrcH_d3D7VjF3FA7eHeJT5j6qGnqBMqz_8ty1QHqAEY_MA3kLygf6aUFo9PuDfW6eva_tzIGhDOlivyH2Uszrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bcf4947eb.mp4?token=WVUZiAwUtUI7hf5TMqL1Mb8p4mgpq9xLlbb_pS3Awl3BfTj7wxVFmxfRNws184N-6sBJHvjCC1IcYgsBHO88EwMz7TTAswEn2Kcv8b9oR9B3lA8eePdYeVSuW71ArsecNtJLlvk82G-gepn9VdU-uY9rbJeNDJnbQYjw5zfFi4hk0UXpd4f7_ISXzAsmkZatP2nv0jpKxGIkx2ssoHLv7tDMOzMT4rf2lLS3wePvEPrlDGb3LP1muu9zdOQXls1MxrcH_d3D7VjF3FA7eHeJT5j6qGnqBMqz_8ty1QHqAEY_MA3kLygf6aUFo9PuDfW6eva_tzIGhDOlivyH2Uszrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو صدا و سیما مجریا‌ با تراکتور اومدن وسط برنامه میگن با همین میخواییم اسرائیل رو شخم بزنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/148174" target="_blank">📅 13:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148173">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
وزارت دفاع روسیه:«ما یک نفتکش در بندر اودسا و یک کشتی باری در دریای سیاه را که برای پشتیبانی از نیروهای مسلح اوکراین مورد استفاده قرار می‌گرفتند، هدف قرار دادیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/148173" target="_blank">📅 13:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148172">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
مذاکرات پکن و آمریکا در حوزه انرژی /  بازگشت چین به بازار LNG در بسته ۳۰ میلیارد دلاری
🔴
آمریکا و چین برای کاهش یا حذف تعرفه ۱۵ درصدی پکن بر گاز طبیعی مایع آمریکا مذاکره می‌کنند؛ توافقی که می‌تواند هم‌زمان با سفر رئیس‌جمهور چین به واشنگتن و در قالب بسته گسترده‌تری از قرارداد‌های انرژی و کشاورزی اعلام شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/148172" target="_blank">📅 13:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148171">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZHKTOdDw_0X0_remkeBjrr1pMZVY9Rj4dkKmE4vimW0u0Huh589-zOQWJg8bKxX5IIoJJIrE8NBGoTZG4SKnj1wI5gfgD_oE5Cs8HWcvC6vHhpsbmFhN_fz2sOZcsyDOQ1zZgMwBdVpMSc-zjMzg59zRb15sH37lcpzH0zf2sE7ovf1NV95X4c6kIw66SVh8WS6i86gjx3O4iCQKP7v1rxhe_7U-uoKPn_b_U7wYVOwyMVGF_4UYj4UhvxYHt2U9ea_tpf8ajNTSZvzrrzfFzTflte0Ev3-6Zbb-c9Ki465KHXcNphCGUe39IdRYwEXOzdvv4WtiPyqvazUf9KBkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاسخ ایران به پیشنهاد جدید آمریکا احتمالا منفی است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/148171" target="_blank">📅 13:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148170">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
سخنگوی ناتو: از اعلام توافق بین ایالات متحده، گرینلند و دانمارک استقبال می‌کنیم. این توافق، امنیت و ثبات در اقیانوس اطلس شمالی را تقویت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/148170" target="_blank">📅 13:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148169">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ان بی‌سی: روبیو، وزیر خارجه آمریکا برخلاف ونس، از قرار گرفتن در کانون توجهات درباره جنگ نامحبوب ایران اجتناب کرده؛ این فاصله ممکن است از نظر سیاسی به سود او باشد
🔴
روبیو در تمام مدت این جنگ، یک «دست پنهان» بوده؛ او به تدوین راهبرد دولت ترامپ کمک کرده
🔴
به گفته افراد نزدیک به وی، نامزدی احتمالی او برای ریاست‌جمهوری می‌تواند روی میز باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/148169" target="_blank">📅 13:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148168">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
سفیر آمریکا در سازمان ملل: محور سخنرانی ترامپ در نشست سالانه مجمع عمومی سازمان ملل در هفته آینده، ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/148168" target="_blank">📅 13:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148167">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16b3ec86ff.mp4?token=Ds58dXSaPf9vHC2wGTDlUNF0dkDavZ_A6rlnVs0teMntP2NXEgGs3_CgGSvqbziVAuoEvCSQJEGkngnuqbmXwlNZrSBMN3Y5IwkVKz_fqCoxKWOEfrfrjkaUeAfzhtLEOqPhQXoNUPGT3yjzCEk76Q8E09kzRxJeiCDZzu41JYr_o2s30wvq3llI1ld4A1EhyRQ_GAyomBSqrVEaEERXw9PbK_pjUJ0-191Y1us6RsBKUmZ-b011gpDnzVWD6PxGhFI6O-TjU1JuJ8Gkfo3o02ALh724jQGHCKmnr-SontZoIl8XJ1t3_ABQSnVVG9NbhlTLqRaxApj5GIBWs_3__A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16b3ec86ff.mp4?token=Ds58dXSaPf9vHC2wGTDlUNF0dkDavZ_A6rlnVs0teMntP2NXEgGs3_CgGSvqbziVAuoEvCSQJEGkngnuqbmXwlNZrSBMN3Y5IwkVKz_fqCoxKWOEfrfrjkaUeAfzhtLEOqPhQXoNUPGT3yjzCEk76Q8E09kzRxJeiCDZzu41JYr_o2s30wvq3llI1ld4A1EhyRQ_GAyomBSqrVEaEERXw9PbK_pjUJ0-191Y1us6RsBKUmZ-b011gpDnzVWD6PxGhFI6O-TjU1JuJ8Gkfo3o02ALh724jQGHCKmnr-SontZoIl8XJ1t3_ABQSnVVG9NbhlTLqRaxApj5GIBWs_3__A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دختر پزشکیان: من هم جان‌فدای ایران هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/148167" target="_blank">📅 13:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148166">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_KWvp9YsCErzJDf-r8wpjUvT9kG3FDsfKjY0QS5cVvqv4TUi1CdDcTS1BM_J7-5g5anqeeecNX-q_UV6Tm0uutJR2h-Iz7yQtA3a-YZqRst6rxwMphXWK4OOzbfQmZ3YMg__2XG0lGmowQLdQDRYSrWT_GHlevbBZaGj5y0lfLLbsBltf_lRig16-ZMALiU9qp7AieuWZeRbBYR7TYdB-quuYmZ5JE9633spNt_xs1QG7n1Yz9hEhY5xE1WpFuun1UXKC-Fwy3WbqnR4qt824MuZAczxS-tmcErthBqaXncIG3KPd6zhJfWu0-bsTIwurifcVZDssme6GZNMnNXGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرودگاه‌های عربستان سعودی با مشکلاتی روبرو هستند...
🔴
تقریباً ۹ فروند هواپیمای مسافربری قادر به فرود در فرودگاه ملک خالد در پایتخت عربستان، ریاض، نیستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/148166" target="_blank">📅 12:56 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148165">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
النشره: حزب‌الله برای سناریوی شکست مذاکرات ایران و آمریکا آماده می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/148165" target="_blank">📅 12:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148164">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QY__8TtGRkaXVF0jEU711p_m6HjeVc_bKFfkH5aGENTcj9a29f7uN3S_8TiWB69I6irYUxJVGyYJJEkxqoH_pCZRX6Ftejam4-pI9538cZQcZGw_o5ljdFAykj-FuO-FlwrRBKNwkYKqfm4JV_K2Y41huA8KR4OnQEuZVYsiSAE69kt5RE0MoHFtadK2qHdceOcRsjF61V9g7Xr8RmYp9Elzy3toO9T2MkX0r8d28a1hi4SWZpsFMZMlel_1qRPuOzzsGI0BEIHJny_ThinXPssJtiBj_r4PtWDjYjo7teUTJIlcqyC2FKTX1t0oTlUHarIwP-FTGruvRU4u5i5GeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری پر بازدید از یک جانفدا
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/148164" target="_blank">📅 12:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148163">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
تا ماه بعد وضعیت طلا چجوریه؟</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/148163" target="_blank">📅 12:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148162">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
هواشناسی: بارش پاییزی هم خشکسالی تهران را جبران نمی‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/148162" target="_blank">📅 12:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148161">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnNB2Jhm-fik6u7Nl0h51g0e2JEoSXmQvsyb1Q2WUVoLwsMxKKkN0sw4iqx0BtTiqNU18QmFioaDU9cCOHt6-NUIC5Ipt_nSK2Ohy_VMSETW5qhZ7Uj2lvECAOjx4G93t3jCc2LjZOVjvgqK1WPktJW7SKOVQzK9kUxB5DIqGXdbZduUSRV-_yAEvakSlssBjre9R_Jm4YSCKLE7HDlJQmPtC2PBansY7ScKnemxSkjOPyjyeViw13p5JOhIHa7seMf2td9LrxggDptCoYnrt-InX8JQCbp2ZT7FVyODjhDUh1K5vsDz6BOr1mJ_lEWxv9hRACKCMtSsmCYDWHWe9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مکرون دیروز  صبح تمام سران سیاسی فرانسه (حتی احزاب مخالف) را به جلسه‌ای محرمانه دعوت کرده بود. موضوع جلسه امنیت اروپا، احتمال گسترش جنگ در اروپا و خاورمیانه بوده است. جلساتی مشابه در آلمان و لهستان هم برگزار شده بود. گویا احتمال وقوع جنگ بین کشورهای اروپای غربی و روسیه بالاست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/148161" target="_blank">📅 12:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148160">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
جبهه اصلاحات: رأی مردم باید بر سیاست‌ها و جهت‌گیری کشور اثر بگذارد
🔴
جواد امام، سخنگوی جبهه اصلاحات ایران، با تأکید بر شایسته‌سالاری و اصلاح شیوه حکمرانی گفت انتخابات زمانی معنای واقعی دارد که رأی مردم بر سیاست‌ها، اولویت‌ها و جهت‌گیری عمومی کشور اثرگذار باشد و تنها به جابه‌جایی افراد در مناصب محدود نشود.
🔴
او با انتقاد از آنچه «بازار مشترک قدرت» خواند، گفت حضور مدیران در دولت‌های مختلف به‌خودی‌خود ایرادی ندارد و تجربه، تخصص و کارآمدی می‌تواند ادامه مسئولیت آنها را توجیه کند؛ اما روابط سیاسی، قومی، خانوادگی یا حلقه‌های قدرت نباید جایگزین شایستگی شود.
🔴
امام همچنین بر تفکیک مناصب سیاسی از بدنه کارشناسی تأکید کرد و کنار گذاشتن نیروهای متخصص با تغییر دولت‌ها را آسیب‌زا دانست.
🔴
به گفته او، حکمرانی سالم باید بر رأی مردم، شایستگی مدیران، حفظ تخصص در نظام اداری و تعیین مرز روشن میان سیاست و اداره کشور استوار باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/148160" target="_blank">📅 12:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148159">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d462dd9ba9.mp4?token=gY0ShplykAQRutx9pEn4vAMwe6cIoUrpiW830GeoblmQXFZSbfsorN4eruWUwmUMLbjFCbDLrylnsVuhXzlFkLuVTMl_0gUsS3oC2TI0s9tGKYge74Q18PUz0-MdC3qiUvNXhnQ8iZVoG2E5gP1O5-XC7VDrS-_T28VUW93cjfI9VfPsmtaRf1OJ1dGAj6OCLFzrNaNuikrA53gCB03Vvxuc8OLBWn1yyB9JCGNqyYGjq5ywjIrvFfyvVt-F_o8HsrCpFOePFR-rl4WPUx-3ivVTN9A8gIzWrJrUnZtrkidM1CWccEZRmFxP770vHx_ZbQEfXUES7maZL_-QZG5vHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d462dd9ba9.mp4?token=gY0ShplykAQRutx9pEn4vAMwe6cIoUrpiW830GeoblmQXFZSbfsorN4eruWUwmUMLbjFCbDLrylnsVuhXzlFkLuVTMl_0gUsS3oC2TI0s9tGKYge74Q18PUz0-MdC3qiUvNXhnQ8iZVoG2E5gP1O5-XC7VDrS-_T28VUW93cjfI9VfPsmtaRf1OJ1dGAj6OCLFzrNaNuikrA53gCB03Vvxuc8OLBWn1yyB9JCGNqyYGjq5ywjIrvFfyvVt-F_o8HsrCpFOePFR-rl4WPUx-3ivVTN9A8gIzWrJrUnZtrkidM1CWccEZRmFxP770vHx_ZbQEfXUES7maZL_-QZG5vHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک پهپاد بدون سرنشین سعودی در حال پرواز بر فراز استان صعده در یمن است و شهروندان محلی تلاش می‌کنند با سلاح‌های سبک آن را سرنگون کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/148159" target="_blank">📅 12:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148158">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
گفتگوی تلفنی عراقچی و وزیر خارجه پاکستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/148158" target="_blank">📅 12:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148157">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aa0bfc25e.mp4?token=k6twz1crtKKINDUiltInpXhTe4AZi4bB6oBjEOF2B3oRVej1oVJT6FGRWy8zgNjMn65FFjqBAISxTF-QyieUt7sYCPIwevx34rcWHiBqLmpulit9V0wRLnqbxNlECmYsTu1iI3cMNv8JBE1wy1p54FpOpfd6_jp6ovYRm4F02jrLAl_RsqEy4Cv0pTK0KECOyJOKinjWcq6cHt8Adl8UDB-RjfQ9qf2mQvuYh2mbjOjHsRhcjFT49zmKxKh1MAgYdM_fhs0o7n3RXLyotFOApEYf9_DBd7P-ewWGwV4AsBp3rVUhPgZd4XyxYRTj2ZSUVnOBK8nn1DiukBESeGgZdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aa0bfc25e.mp4?token=k6twz1crtKKINDUiltInpXhTe4AZi4bB6oBjEOF2B3oRVej1oVJT6FGRWy8zgNjMn65FFjqBAISxTF-QyieUt7sYCPIwevx34rcWHiBqLmpulit9V0wRLnqbxNlECmYsTu1iI3cMNv8JBE1wy1p54FpOpfd6_jp6ovYRm4F02jrLAl_RsqEy4Cv0pTK0KECOyJOKinjWcq6cHt8Adl8UDB-RjfQ9qf2mQvuYh2mbjOjHsRhcjFT49zmKxKh1MAgYdM_fhs0o7n3RXLyotFOApEYf9_DBd7P-ewWGwV4AsBp3rVUhPgZd4XyxYRTj2ZSUVnOBK8nn1DiukBESeGgZdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: هرکس پلیس بکُشد باید اعـدام شود
🔴
ترامپ: "مدت کوتاهی پس از آغاز به کارم، یک فرمان اجرایی تاریخی امضا کردم که بر اساس آن، هر کسی که به جرم کشتن یک افسر پلیس محکوم شود باید با مجازات اعدام روبه‌رو شود؛ و سال گذشته، کشته های پلیس حین خدمت به پایین‌ترین سطح در ۸٠ سال گذشته رسید."
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/148157" target="_blank">📅 12:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148156">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKV0MfvlFYqBbm_kauokdRNXCAaihPhcIIgU_FH_A72Pg33Bwj4asj0c-UYKLfOYRQfLMmAN0T_kJ8txGTrnbF8XPRq6IZdQmgglipwDWvOJE21OJ60iKtal8S2H2muyrFOeH98sVKSCTvBwmjiMNnj7sc_5fkFt3C1AEWOoSO6KSzXCM8PjuXZxkL7aq9glgcZRF8xgSkui9wOti3OIvEjEB1cxxL3pMCbkR8c8x7Uqdwq-1_KQHoGr3HnCX7bAB3v7u9eSIIJ9Slq9FGQrMm81q5pYQ3KFR2juHoWQPVyBlYLiLwf4wPZzGyDu_HS9tiSd0WUKE-vx6auY9J_eIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تعدادی از هواپیماهای مسافربری که قصد فرود در فرودگاه جده در عربستان سعودی را داشتند، به دلیل احتمال وقوع حمله، قادر به فرود در این فرودگاه نبودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/148156" target="_blank">📅 12:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148155">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
دادستانی تهران علیه عوامل برگزاری «دو مارتن تهران» اعلام جرم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148155" target="_blank">📅 11:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148154">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
وزیر خارجه کره‌جنوبی در دیدار با وزیر خارجه آمریکا، از آمادگی کشورش برای ارائه سهم قابل‌ توجه در تلاش‌ها برای بازگرداندن آزادی کشتیرانی در تنگه هرمز خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/148154" target="_blank">📅 11:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148153">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
پیمان اکبری مجری صدا سیما : به تجمعات عادت کنید، دیگه هم شب میاییم هم صبح
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/148153" target="_blank">📅 11:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148152">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
شورای امنیت سازمان ملل حملات حوثی‌ها به عربستان سعودی، از جمله حملات علیه زیرساخت‌های غیرنظامی و انرژی را به‌شدت محکوم کرد و خواستار توقف فوری تشدید تنش‌های نظامی شد.
🔴
شورای امنیت همچنین تهدیدها علیه کشتیرانی در دریای سرخ و باب‌المندب را محکوم کرد، حق عربستان برای دفاع از خود بر اساس قوانین بین‌المللی را به رسمیت شناخت و بر تعهد خود به حاکمیت و تمامیت ارضی یمن تأکید کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/148152" target="_blank">📅 11:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148151">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
نیروی هوایی اوکراین اعلام کرد که در جریان حملات شبانه، ۱۴۱ پهپاد روسی را در مناطق مختلف این کشور سرنگون کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148151" target="_blank">📅 11:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148150">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
الجزیره: قانون جدید تحریم‌های ترامپ، اختیارات کلیدی تحریمی علیه ایران را تا سال ۲۰۳۱ حفظ می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/148150" target="_blank">📅 11:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148149">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fafde8acd9.mp4?token=d1XZ1V6_5Hl_CPpDz1LDgI7o4YwHY12QZMFFo3_c1udwYhCKLbnnXCMWmZwgPRIfQ0DXl-_7giljixClWtrRlat4H0ot36pJknNEXLq11aKI8gPzmzS69jGapHBUWUUt1W1nzrVQ1sKcdCJFOI69Wg1AdylxNJRRJahyU0_8lcVdT8_AbfQDLQI31n4ofcW0ChcEFELxITFGtGc8XmoKX2NqXcGz16JT2TTocsSeXXSbp-zZl83n1H6jGBKDyo_klLU_Vvo2MQV5Qzta6EIfCIccxKH2mWfsFYe4v8XFlUNG8f8RcsoNHrW_upYwzeupiSWPclYxdt760C5nRVYN4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fafde8acd9.mp4?token=d1XZ1V6_5Hl_CPpDz1LDgI7o4YwHY12QZMFFo3_c1udwYhCKLbnnXCMWmZwgPRIfQ0DXl-_7giljixClWtrRlat4H0ot36pJknNEXLq11aKI8gPzmzS69jGapHBUWUUt1W1nzrVQ1sKcdCJFOI69Wg1AdylxNJRRJahyU0_8lcVdT8_AbfQDLQI31n4ofcW0ChcEFELxITFGtGc8XmoKX2NqXcGz16JT2TTocsSeXXSbp-zZl83n1H6jGBKDyo_klLU_Vvo2MQV5Qzta6EIfCIccxKH2mWfsFYe4v8XFlUNG8f8RcsoNHrW_upYwzeupiSWPclYxdt760C5nRVYN4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
هم اکنون ، ویدئویی از آتش سوزی یک رستوران در خیابان دولت
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/148149" target="_blank">📅 11:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148148">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
قیمت بیت کوین پس از افزایش نرخ بهره در ژاپن به بالای ۸۱ هزار دلار جهش کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/148148" target="_blank">📅 11:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148147">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
شبکه خبری سی‌ان‌ان: یک گزارش اطلاعاتی نادرست که با کمک هوش مصنوعی تهیه شده بود، در جریان جنگ آمریکا علیه ایران، ارتش این کشور را تا آستانه یک عملیات علیه یک کشتی چینی در خاورمیانه پیش برد و خطر درگیری نظامی میان واشنگتن و پکن را افزایش داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/148147" target="_blank">📅 10:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148146">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
نماینده آمریکا در سازمان ملل: ترامپ در سخنرانی خود در سازمان ملل، به موضوع جلوگیری از دستیابی ایران به سلاح هسته‌ای می‌پردازد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/148146" target="_blank">📅 10:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148144">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGESPDTBcuOjsdstBNh1gbg83_EvLLiUiubd1_CCJn0iprnwmUSuD5byMMofp_4JFAsHiz1yW9It3ZJnUdElH7RUJ2Syp7D_QzR6-tGXSMrHydXCZZzy79c3rCrWkQsPi9er1OYtHdmO-rA98UOibT9fzBWB2G5XUT8IxhmX7FfmgsX7_BGaRlqpKisQimYB8EqR2VQdZ9usJLcFoJozcphu5Q3zv1mMHhF-4QIrDRzBaILW2JtJr10zdj6rFAaqtgXVrNeA4BpcS1dfL5Sxn76W3TUWFfdI2xuhjITWWMf6d-qHkaDzMSVAlTrxOzyNdTnF_xZLPw5s5n_NY8NJCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53e84c2629.mp4?token=DVd9zzWhyswJsHDprG98W0p7d-FtalenYOXEkL3PaTy9riZv-NPXnlIDDAvDecoiuFyIohzmYd-fqLDvDhPH7Dyt0IVsIKgWnU4f3msVTV7z4e1U1ffGM_SrQ8vc7m8ulOtJhW5QsJDe1wiMbwq23MwjgqKQsQreUmYvFtoYhLJ7HkMShi6UJLLNbsOJWrNvbh2S6zgzCzuoEE4L72VK_oSG65D3rP72BLmkutLKY0nPlIyXCWLmvIoyuaZM-5QDfKu4zJqRB4Eyqs3seCz5KX90R88AAGrLb3_YRzL6cNwlkWhPr9K_SLUU3_yM06bGjereP2EoDlIOkn5VWCroXnfzs1lrg7SL6XhQ-4a_isNQirTc7k14UdNVy2TZQvKSmagD7iXMUY_T_oLyhgz7nwTBlB8m0Bboug60DjmtzVaKo8SgOOh3AWOB-k_N_n05QQA24V194OkLftv_4w3_Q88ff8HjS5wfGs0Yn59g8SvdLZoI7T2q_tjrUU3IK0kRPSJVNql2EakOa5pbxT6nJ3qHF6F5oV9oLosQWaUC6lbCKjieQLHpP1uReJ3DndYTxRt4vFiH_vbZbxy3Y9SYIednxojc0yVhXoataqV-J44deuSr2tPzUhuMqE1HyB_B_FrNC81T-HmZZLc336YRST2a9HmAkAqPs6JFc6j1tEM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53e84c2629.mp4?token=DVd9zzWhyswJsHDprG98W0p7d-FtalenYOXEkL3PaTy9riZv-NPXnlIDDAvDecoiuFyIohzmYd-fqLDvDhPH7Dyt0IVsIKgWnU4f3msVTV7z4e1U1ffGM_SrQ8vc7m8ulOtJhW5QsJDe1wiMbwq23MwjgqKQsQreUmYvFtoYhLJ7HkMShi6UJLLNbsOJWrNvbh2S6zgzCzuoEE4L72VK_oSG65D3rP72BLmkutLKY0nPlIyXCWLmvIoyuaZM-5QDfKu4zJqRB4Eyqs3seCz5KX90R88AAGrLb3_YRzL6cNwlkWhPr9K_SLUU3_yM06bGjereP2EoDlIOkn5VWCroXnfzs1lrg7SL6XhQ-4a_isNQirTc7k14UdNVy2TZQvKSmagD7iXMUY_T_oLyhgz7nwTBlB8m0Bboug60DjmtzVaKo8SgOOh3AWOB-k_N_n05QQA24V194OkLftv_4w3_Q88ff8HjS5wfGs0Yn59g8SvdLZoI7T2q_tjrUU3IK0kRPSJVNql2EakOa5pbxT6nJ3qHF6F5oV9oLosQWaUC6lbCKjieQLHpP1uReJ3DndYTxRt4vFiH_vbZbxy3Y9SYIednxojc0yVhXoataqV-J44deuSr2tPzUhuMqE1HyB_B_FrNC81T-HmZZLc336YRST2a9HmAkAqPs6JFc6j1tEM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
از روز گذشته ظاهرا حملات نیروهای تحت‌الحمایه عربستان با پهپادهای سری نقم و عیبان (معادل شاهد-۱۳۶ ایرانی) به اهدافی در اطراف صنعا آغاز شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148144" target="_blank">📅 10:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148143">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
مولوی عبدالحمید: اگه حکومت حرف مردمو گوش میداد شرایط اینجوری نمیشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/148143" target="_blank">📅 10:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148142">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
مقامات ارشد دولت ترامپ می‌گویند که رئیس‌جمهور در جریان نشست مجمع عمومی سازمان ملل در نیویورک، با بنیامین نتانیاهو، دیدار نخواهد کرد!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148142" target="_blank">📅 10:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148141">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
عضو دفتر سیاسی جنبش انصارالله: ملت یمن با هرگونه آتش‌بس یا کاهش تنش، تا زمانی که عربستان محاصره یمن را رفع نکند، موافقت نخواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148141" target="_blank">📅 10:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148140">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
الجزیره: نهاد ناظر بانک‌های ترکیه، مجوز فعالیت شعبه «بانک ملت ایران» در استانبول را لغو کرد
🔴
بر اساس اطلاعیه‌ای که در روزنامه رسمی منتشر شد، نهاد تنظیم‌گر و ناظر بانک‌های ترکیه، مجوز فعالیت شعبه بانک ملت ایران در استانبول را لغو کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148140" target="_blank">📅 09:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148139">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
وزیر امور خارجه آمریکا: توافق با دانمارک و گرینلند «تاریخی» است و بر اساس آن، منافع امنیتی ما در قطب شمال به طور دائمی و بدون هیچ هزینه‌ای تضمین می‌شود
🔴
مارکو روبیو، وزیر امور خارجه آمریکا در مورد توافق با دانمارک و گریلند گفت: این توافق تاریخی، یک پیروزی بزرگ برای ایالات متحده و مردم آمریکا است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148139" target="_blank">📅 09:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148138">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc3cc6058d.mp4?token=PoVDuKLF3pcvR_qWK2eSMDcWkC0UMXkgY_ImVQeijutX0EYAXDhfezhPCIvW9vw10ONMk5S7HhhdjroY8hI7oBwApn9wgPKo8bk6ARmI6RtXQPvG7_nz1DDmu5IsGOJOAkkqtJ-426PXl0cuiVCy-dw-zORcVKxopFmoERvB6VSih42On6CEF0wfyOR_TzyS0WAQFDhFlvPl3-P7uD1gULisK6sOFf0hOCM0NH7tMSQuUz7lLajZ2QfNHprEPzh__2PDcajPoDJGho88EXhXdi9NhwXkqt7j3ZnrK6JBBkM5aTXuQWkVuBFsc9xX9IDPWr0qfy_4FDMUpWf2M6MkTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc3cc6058d.mp4?token=PoVDuKLF3pcvR_qWK2eSMDcWkC0UMXkgY_ImVQeijutX0EYAXDhfezhPCIvW9vw10ONMk5S7HhhdjroY8hI7oBwApn9wgPKo8bk6ARmI6RtXQPvG7_nz1DDmu5IsGOJOAkkqtJ-426PXl0cuiVCy-dw-zORcVKxopFmoERvB6VSih42On6CEF0wfyOR_TzyS0WAQFDhFlvPl3-P7uD1gULisK6sOFf0hOCM0NH7tMSQuUz7lLajZ2QfNHprEPzh__2PDcajPoDJGho88EXhXdi9NhwXkqt7j3ZnrK6JBBkM5aTXuQWkVuBFsc9xX9IDPWr0qfy_4FDMUpWf2M6MkTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: هفته آینده در سازمان ملل سخنرانی می‌کنید. پیام شما چیست؟
🔴
ترامپ: خب، سال گذشته اپراتور تله‌پرامپتر من را از ورود به سالن منع کردند. بنابراین من بدون تله‌پرامپتر آنجا ایستاده بودم. جالب نیست؟
🔴
خبرنگار : پیام شما چیست؟
🔴
ترامپ: یادتان هست؟ آن‌ها پله‌برقی را خاموش کردند.
🔴
خوشبختانه بانوی اول من خیلی محکم بود و من توانستم پشت او یا بخش دیگری از بدنش را بگیرم. در واقع، دستم کمی پایین‌تر از پشت او قرار گرفت و محکم گرفتمش.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148138" target="_blank">📅 09:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148137">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
هزینه یک دست لاستیک ایرانی تا بیش از ۳۵ میلیون تومان رسید
🔴
آوش در گزارشی نوشته قیمت شش سایز پرمصرف لاستیک ایرانی اکنون بین ۴.۵ میلیون تا ۸ میلیون و ۷۵۰ هزار تومان برای هر حلقه قرار دارد.
🔴
بر این اساس، خرید یک دست چهارحلقه‌ای لاستیک برای بسیاری از خودروهای داخلی بین ۱۸ میلیون تا بیش از ۳۵ میلیون تومان هزینه دارد.
🔴
رقمی که نشان می‌دهد تعویض لاستیک، برای بخش بزرگی از رانندگان دیگر یک هزینه عادی نگهداری خودرو نیست و می‌تواند فشار قابل‌توجهی به بودجه خانوار وارد کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148137" target="_blank">📅 09:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148135">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GWlwYjQC_swj1GkypFmvWZIUQHZp2swz8IMcHN_koSfCkT5ZsWG7OR5iNaacjMNBuvPVNUV4nWLmI-FYZjREiieprdHXIXNA_-dxl7rHeoOxMd5pdPe6_MsC3-2Wby3DGJxDhBPtBLwfx-hFzeJpPGzuN-xcd6-ejegUXZR63LIvmIb7eg7yUZn_EnXYpWrvygM931ocW-3K_AUBP9UgAJcHizIft1XxPVhkjUCgIYbTjIVKrdCBptyQOwysddLu3eCpXS7_1WwwN_KdKkyh_ZAEihCU9oV0-YGNmuSbgGgW6QbzEj9jPrSEt4WKCJTmcqg1hrqhVyBWf93K9t22nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XZv8pJG3uG6oak9kYpc_nsoy1ZUBkYMW8T8M3BKy9DR9yQfzPWHqL32PwjmWK1EcQTdWtxQvseblUrWllAwEk1s0mITTjJbdEwIOHhOqv8hc6YVf6z5_hmG1pzEKJyxYV0Yr-NAgmKIxYl09oCmUnLCzqoaPWb5E3h7z3dJqLmea1MaPgNEy-A3niK0MF9exJQ7NC6ddQPdEGe44q1sWD62B_qv57xW6i-6Ov9gz5sHFuwwIMTDKDW_SWbhfgoXkZsOhPGraZ7ScH0ensAP8TgjnZyY5kpaDHgJDBxSkCfNm2EM_mseLRrQd6j2oklU-TsLhdZtLlWXduAG6fjur2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا،
فهرست «
۲۵ دستاورد برتر ترامپ در دوره سوم
» را در شبکه اجتماعی
Truth Social
منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148135" target="_blank">📅 09:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148134">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
پروازهای هوایی در ریاض به دلیل موشک‌ها و پهپادهای حوثی ها متوقف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/148134" target="_blank">📅 09:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148133">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bB8MTteiJ7v-sLhZbGf3INWB-pQ-MT2hjb0o-_gtF9PNjSOuc5mf4PPSAsD9BXPzEwsutFMr9Ow0XeaPAkYzX2Ivx_YOKPhDFk8vJHvSmIzr4-sLhJggdpCOQ5Fp_ItPLC-tUTDoKN27eDxH057ooB0_cndju6wySLl8n3YWhTCG9Knkj76dOYeQmNzJlnxEhiP9q_EhTihPdxnemrWzuJTd561lNLIgP0jbw56eKlN923M5TpySoNOmtddcof8YJ1vSeaPCx1LCcQi-1nG0bWta12grQenRuSoBNAkqHxR-jhLW5O6ZNaTu-Wncb4-8VI_k3qobJz9vhMs1aK-4bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به نظر من، هدف حمله موشک بالستیک انصارالله به ریاض، احتمالاً پایگاه هوایی ملک سلمان در جنوب ریاض بوده است
🔴
اگر هدف پایگاه هوایی شاهزاده سلطان بود، احتمالاً هشدارهای اولیه برای ریاض صادر نمی‌شد؛ زیرا این پایگاه در فاصله حدود ۸۰ کیلومتری ریاض قرار دارد. همچنین در حمله ایران به پایگاه هوایی شاهزاده سلطان در اوایل سال جاری، معمولاً هشدارهای اولیه در ریاض فعال نمی‌شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148133" target="_blank">📅 09:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148132">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
انتظار می‌رود شی جین پینگ، رئیس جمهور چین، هفته آینده در واشینگتن با دونالد ترامپ درباره آتش‌بس تجاری رو به پایان، معافیت میلیاردی تعرفه‌ها و هوش مصنوعی گفت‌وگو کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/148132" target="_blank">📅 08:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148131">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
پنتاگون در تازه‌ترین برآورد خود اعتراف کرد جنگ با ایران تاکنون ۴۳.۶ میلیارد دلار برای آمریکا هزینه داشته است؛ رقمی که هنوز خسارت‌های واردشده به تأسیسات نظامی آمریکا در ۸ کشور غرب آسیا را شامل نمی‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/148131" target="_blank">📅 08:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148130">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxhPn8N7Etvf8ddc6GjPYJ9Vr5zP3Cnz3oVH9V91qYdaa9onWNaVdZq6JPeC3eLOLEHABRB-4Y1QgcG9EQOs21QxMsuvP6je3o3Q69ShDVZHZE51acsFhtgNBYskItBsatI23gf4spCGU1MDSkZmoZaWvyDqFhA7U1NIIBjQGz0B208KC894OV1uSh7-SvnCv1xvwhqz2985U5go50skN-RY0eur9yuoTvWHY6YvZJ8Bp7rUB6lTc2T7iKEryDcWaSAH4y5m9FhGkuNUOTEaIAhxBMj1Euc12rLJCFyfctRE1JtLwUm5H69bLjcsPr1Sgpe1lRxdREWcvlkI2HfSgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر جنگ آمریکا: شرم بر واشنگتن پست. این اطلاعات جعلی و دروغ است. آنها از رسانه دولتی ایران بدتر هستند.
‏
🔴
واشنگتن پست: بر ادعای خود باقی میمانیم. ۶ کشته بیش از آنچه اعلام کردید وجود دارد. واشنگتن پست اعلام کرده که تعداد کشته شدگان نظامی آمریکا در جنگ علیه ایران بیشتر از اعلام پنتاگون است
‏
🔴
به گفته ۶ مقام آمریکایی آشنا با داده‌های حسابداری تلفات داخلی وزارت جنگ، شمار نظامیان آمریکایی که در جنگ علیه ایران در کشته شده‌اند، بیشتر از آن است که پنتاگون اعلام کرده است.
‏
🔴
این مقامات تعداد کشته شدگان را دستکم  ۲۲ تا ۲۳ نفر اعلام کردند، پنتاگون در حال حاضر ۱۸ کشته را فهرست کرده است..
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/148130" target="_blank">📅 08:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148129">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ترامپ: با دانمارک و گرینلند به توافقی دست یافته‌ایم که به آمریکا کنترل دائمی بر امنیت و نیازهای دیگر در گرینلند را می‌دهد
🔴
این توافق کاملا به همه نگرانی‌های متعدد واشنگتن رسیدگی می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/148129" target="_blank">📅 08:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148128">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZwCQtCNdziiyV9eJt9DlJea4mR-14b5RjoCqcmUS7eaQNAVjR5HsZ7s1RIYAwuscZyaccT7LVQwIjCVCosy5FYriR3qgfR7R6MqVOalkxIAvBUI2o6jrhTxZmlSE--7ZerR0ewowrvTlOVE1SsdocTmxIZFKQBOu7ev__e_kH1bhvpBS-55PyCrWVaF9zt-Q9YBcIBqfYiExYADanWKSH1vVqtiYI5Ye3Hodgy6uRpKbi4zRrWRIrbQwNQrLkIUz7MePBvrSuEi9l5_vqhpDziP2Gxg18I-JSR4J_4p9Tve2O14JFQpBCa70z-KNyFdsKbCdUIKLx7n8g26AoswoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترکیه مجوز فعالیت شعبه بانک ملت در استانبول را لغو کرد!
🔴
نهاد ناظر بانکی ترکیه مجوز فعالیت شعبه استانبول بانک ملت، بانک کاملاً دولتی ایران، را لغو کرد
🔴
این نهاد دلیل تصمیم خود را «تهدید علیه ثبات نظام مالی» اعلام کرده است
🔴
شعبه بانک ملت از سال ۱۹۸۲ در ترکیه فعال بود، اما پس از تحریم‌های آمریکا عملاً از سوئیفت و سامانه انتقال بانکی EFT ترکیه کنار گذاشته شده بود.
🔴
لغو مجوز، پایان رسمی فعالیت این شعبه در ترکیه محسوب می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/148128" target="_blank">📅 08:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148127">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
حوثی‌های یمن (انصارالله) از کشته شدن ژنرال فرق العصار، فرمانده تیپ اول کماندویی، در نتیجه حمله هوایی عربستان سعودی در جبهه کهبوب در نزدیکی تنگه باب المندب خبر دادند.
🔴
گزارش‌ها حاکی از آن است که شش نفر از محافظان العصار نیز در این حمله کشته شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/148127" target="_blank">📅 08:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148126">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFdztp5eOCsLlyOF5srjZslis8gT6e7uoB9cFmbacLEAVda7F_0n63rLNFCXhoxb1ImTOiHyHaQP65KMtreS2qEZpe_bSITs1Z5XFqMBDAWtmNQadTawbgKu8yl8s4-Cw1uBaf85q7_GCqV46yCxZxXSZ8beeN7iuj4ljB_FF5tdpZzbYGsN5fS_BhDtsQ76xiwIQfqvOJa3kCgtsPt2HzG0dj50Y5RcIkuRQOeuIzzEwZQf3J81RFEhXY_aWpzme0Ccx9_HvZ1PMxSGuHX2UoF0w0Itv_LxXLEf_a8viuspbXw_D1N5GNUtiNa6ZNhQdehMt2cqaY-HZHJ4_RATHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای نظامی آمریکا به ABC News گفته‌اند که بیشتر پایگاه‌های نظامی آمریکا در خاورمیانه به‌طور غیرقابل‌جبرانی آسیب دیده‌اند و ترمیم آن‌ها ممکن است دهه‌ها طول بکشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/148126" target="_blank">📅 01:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148125">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا، قانون «تحریم روسیه و ایران، لیندسی او. گراهام» در سال ۲۰۲۶ را امضا و آن را به قانون تبدیل کرد.
🔴
بر اساس این قانون، تحریم‌های قانونی، تعرفه‌ها و محدودیت‌های اعمال‌شده علیه روسیه گسترش می‌یابد و تحریم‌های موجود علیه ایران نیز…</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/alonews/148125" target="_blank">📅 01:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148124">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtaMiAs4PzxievIzAtx7KhAcOcyVElggB0Cf1dDu_O7PAeG-Cf-gYGhx2OkCz0ytfHIBxtGd8d3qliZHdMjvESaHdcvx6e-iMS8Sy_1IXtulHLvbUg8DXGHo_yo0lkrk9Gp_oZZDEnMs5pqRe5cv7zne82atDNqGdycMnV4PsnQf3ljKDE77ZF9VZlG0_ZJvv5jRf3PG1m6kLkEoLUHWvrvhf8Bn2X_usfx-hZOHDvQ3jmRVK_AN5-QQczLYjYSCCPifUPbSKTdXFlLig_hqWd-jyNJoPCfgar82vBhNpTFUS-uNv8RIGkoGYTy89tZoiENQFP6JscDzpLabQ7FFLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا،
قانون «تحریم روسیه و ایران، لیندسی او. گراهام» در سال ۲۰۲۶
را امضا و آن را به قانون تبدیل کرد.
🔴
بر اساس این قانون،
تحریم‌های قانونی، تعرفه‌ها و محدودیت‌های اعمال‌شده علیه روسیه گسترش می‌یابد
و
تحریم‌های موجود علیه ایران نیز تمدید می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/148124" target="_blank">📅 01:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148123">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f1eeaeb95.mp4?token=QmhfcKdf_97E17OnolTd4xiUnnMMNE-BSM10uNPKRW2J6GhrmreLtPW8Z9r_BP769v2fjWX759VexqdRH3Un8OQ4aJzwNJlnNcBzrZ8fbDEIoQ2PWgwj0Rlm4LfDX5B8FkGQxqbNBZZ8InAvH82dsRjRe-SYaAcEgJD9EGIoXBUJGEtpaUThewKnaIR1wc1r336DwFuJIWwlr6y9-6bIg41-m6HE3J4TC_FBS_d3xQCvfPRVBd49GNjRCV4mtJbCSra4Qw8GxnlLjvQBlwKnz7m5LmjlGYp4HaIOxbVGU5Ol5TwM98yhkzSfYgS3DzOQlkbzvyi5uem2Ub35lswyTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f1eeaeb95.mp4?token=QmhfcKdf_97E17OnolTd4xiUnnMMNE-BSM10uNPKRW2J6GhrmreLtPW8Z9r_BP769v2fjWX759VexqdRH3Un8OQ4aJzwNJlnNcBzrZ8fbDEIoQ2PWgwj0Rlm4LfDX5B8FkGQxqbNBZZ8InAvH82dsRjRe-SYaAcEgJD9EGIoXBUJGEtpaUThewKnaIR1wc1r336DwFuJIWwlr6y9-6bIg41-m6HE3J4TC_FBS_d3xQCvfPRVBd49GNjRCV4mtJbCSra4Qw8GxnlLjvQBlwKnz7m5LmjlGYp4HaIOxbVGU5Ol5TwM98yhkzSfYgS3DzOQlkbzvyi5uem2Ub35lswyTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگست:
«تنها رسانه‌ای که بهتر از ایران پروپاگاندای جعلی تولید می‌کند، رسانه‌های دچار جنون ترامپ در کشور خودمان هستند.
🔴
جدی می‌گویم. واقعاً تأسف‌بار است.
»
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/148123" target="_blank">📅 01:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148122">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
پیت هگست : خسارات و تخریب‌هایی که ارتش ما به جمهوری اسلامی وارد کرده، بی‌سابقه بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/alonews/148122" target="_blank">📅 00:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148121">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ترامپ میگوید سازمان ملل متحد عمداً دستگاه پله برقی و دستگاه نمایش متن مورد استفاده او را در سخنرانی‌اش در مجمع عمومی سازمان ملل سال گذشته، از کار انداخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/alonews/148121" target="_blank">📅 00:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148120">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYtaKYMdTicT0_kU4mF9oqWdEyznZwRZRR8MbX7wvh3SoN3NCXRJisQ2ZOrfQ4n3TxE0kKHBwBAdyCRKEicCS75H7L-dik2oK3Wsn9gUxmSBE3_SsxbeZv5g-HQXXKQcHQLotqTzRgWrR0mj5P2Uza24fqhRryke5Bk4QNsTT72ObA4B1P643mkqmID4e29hlzMTNP6xVG7Dq3PfPADJBGBtFSqzlsfZ-gRTcO71rLQlXQUfMc4czqME1us0bZZyrMVlWBaXF9-hVprjcSoZfHOfn2RF_M0r94UuOEUt5GQiB9i2dCdpAALJ283HGxJ81di6bt0NT1TPEp9p1Gj5Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علم الهدی: ریشه تمام مشکلات بی حجابیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/alonews/148120" target="_blank">📅 00:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148119">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ترامپ : روزنامه نیویورک تایمز بسیار دروغگو است.
🔴
واشنگتن پست بسیار زننده است. من می‌گویم، آن‌ها زننده هستند.
🔴
من نمی‌فهمم. چرا باید این‌گونه باشند؟ ما بسیار خوب پیش می‌رویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/148119" target="_blank">📅 00:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148118">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
هشدار های در غرب عربستان سعودی دوباره فعال شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/148118" target="_blank">📅 00:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148117">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
فوری /  هشدارها در جیزان، جنوب غربی عربستان سعودی
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/alonews/148117" target="_blank">📅 00:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148116">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ترامپ : شبکه فاکس بدترین نظرسنجی‌ها را در کل این صنعت دارد. به نظر من، آن‌ها سال‌ها پیش باید کارشناسان نظرسنجی خود را اخراج می‌کردند.
🔴
آن‌ها به مدت ۱۰ سال، پیش‌بینی‌های نادرستی درباره من داشته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/alonews/148116" target="_blank">📅 23:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148115">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
خبرنگار: آزادی مطبوعات در متمم اول قانون اساسی تضمین شده است.
🔴
ترامپ: ممنونم که این را به من یادآوری کردید.
🔴
خبرنگار: آیا شما در تلاش هستید تا با اعمال فشار، رسانه‌ها را از انجام وظیفه‌شان باز دارید؟
🔴
ترامپ: نه، نه، نه. من از رسانه‌هایی که دروغ می‌گویند،…</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/148115" target="_blank">📅 23:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148114">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
خبرنگار: آزادی مطبوعات در متمم اول قانون اساسی تضمین شده است.
🔴
ترامپ: ممنونم که این را به من یادآوری کردید.
🔴
خبرنگار: آیا شما در تلاش هستید تا با اعمال فشار، رسانه‌ها را از انجام وظیفه‌شان باز دارید؟
🔴
ترامپ: نه، نه، نه. من از رسانه‌هایی که دروغ می‌گویند، مثل شما، خوشم نمی‌آید. من فکر می‌کنم شماها خیلی بد هستید
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/148114" target="_blank">📅 23:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148113">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d63f668795.mp4?token=PMaWLaA_5C_LSmh9nk6VlYu-GZ4RuU_KtlOBmuzOMee-zxC7qfd3RkeLYN0zzkDnA_mmxyvSiBYDHvyVCEJ_ZCTKDog2G9ehzzOw52_I2JsUaTYlqNeTJRClMQ64yg4E7m_vcpcyxjBCNeFrYqE6gRr4U19FQDeq6jbBJhBS45IhSK2Vtb3Sjok6B8_Ul4HWwd2CI-OxmGl1hfdMZ9fOLqVw9WFjrRGS2Zsw8hXmEZBDIs0jc8DQ9UcJSH8Yb3pBgVjH6tzj0g6FDCEWH1OdsrSji1ya1NerfYzzEbbjrFwRB64njAGbpKH6onowLniCcdx0Urg2idR9tlM-9EtsKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d63f668795.mp4?token=PMaWLaA_5C_LSmh9nk6VlYu-GZ4RuU_KtlOBmuzOMee-zxC7qfd3RkeLYN0zzkDnA_mmxyvSiBYDHvyVCEJ_ZCTKDog2G9ehzzOw52_I2JsUaTYlqNeTJRClMQ64yg4E7m_vcpcyxjBCNeFrYqE6gRr4U19FQDeq6jbBJhBS45IhSK2Vtb3Sjok6B8_Ul4HWwd2CI-OxmGl1hfdMZ9fOLqVw9WFjrRGS2Zsw8hXmEZBDIs0jc8DQ9UcJSH8Yb3pBgVjH6tzj0g6FDCEWH1OdsrSji1ya1NerfYzzEbbjrFwRB64njAGbpKH6onowLniCcdx0Urg2idR9tlM-9EtsKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره اروپا: روسیه از قبل به متحدان اوکراین حمله کرده است. این کشور حدود پنج سال است که به متحدان اوکراین حمله می‌کند.
🔴
به نظر من، همه با این موضوع موافق هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/148113" target="_blank">📅 23:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148112">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c2567a538.mp4?token=om6nd0daWmvUe1NnR5-TyElsemc53BnDLmPM8hltLF0_Bnzc8q0kiq2YGwUBdDjWi7dZ8MDkp335GxlTlKwAnStJ1DPdoUd7uqbAgYgmNJaPp8nA4ZYViMZIR3aC1CXnl6l3SpU5lcZqqCeSjVTr0NWkLOuQjFo0dt1ottNqC7MztjbonHgybbwCyattn3AVlaydGcHmFmvzHVhhHKzSYg3_urx1DiNDFlkFvGOn6oexmtmxwepYN7v1rb4CZJoQbgzlLUeymrXzjyr4J8V8OWOuht9hZFYWM4_JozLsYWf-ONXOTRrOt89McEjbXgRQBpSoAXYLChVAJS0k1MjObgzzmykuHkynEOGV93JTZsapxG4aAO2G2eKLPqoSwPh7P7dY5rQAWz7tR5qqZWj2uIFv8jgzAHQzrjwW5OBGoz3E5ISwkhXCTv6Xl6ZaLcrRtDFLkfohCNnbib4oKuHgI8Qo_NB5OEycM_rKXPcGRPACyB1IkdFFRXIy9UIEiR664o7pO-3_wjM90mk0yBUzTJp_TzxVfoTmhjooVhU-TH9DRoMFCkxLbe3u7JbXT0G22_Dr7hwMKYWqhF9_Z2CykTyZpe-p9wSajhPAMOe67UOWm4nYE2mdddYF2eVX_cw91LXwofyvHTl7divTJOqW1r3pTx7-arkdEOKal0khWwE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c2567a538.mp4?token=om6nd0daWmvUe1NnR5-TyElsemc53BnDLmPM8hltLF0_Bnzc8q0kiq2YGwUBdDjWi7dZ8MDkp335GxlTlKwAnStJ1DPdoUd7uqbAgYgmNJaPp8nA4ZYViMZIR3aC1CXnl6l3SpU5lcZqqCeSjVTr0NWkLOuQjFo0dt1ottNqC7MztjbonHgybbwCyattn3AVlaydGcHmFmvzHVhhHKzSYg3_urx1DiNDFlkFvGOn6oexmtmxwepYN7v1rb4CZJoQbgzlLUeymrXzjyr4J8V8OWOuht9hZFYWM4_JozLsYWf-ONXOTRrOt89McEjbXgRQBpSoAXYLChVAJS0k1MjObgzzmykuHkynEOGV93JTZsapxG4aAO2G2eKLPqoSwPh7P7dY5rQAWz7tR5qqZWj2uIFv8jgzAHQzrjwW5OBGoz3E5ISwkhXCTv6Xl6ZaLcrRtDFLkfohCNnbib4oKuHgI8Qo_NB5OEycM_rKXPcGRPACyB1IkdFFRXIy9UIEiR664o7pO-3_wjM90mk0yBUzTJp_TzxVfoTmhjooVhU-TH9DRoMFCkxLbe3u7JbXT0G22_Dr7hwMKYWqhF9_Z2CykTyZpe-p9wSajhPAMOe67UOWm4nYE2mdddYF2eVX_cw91LXwofyvHTl7divTJOqW1r3pTx7-arkdEOKal0khWwE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: در دنیایی که بر پایه منطق استوار است، غیرممکن است که فردی که یهودی است یا فردی که سیاهپوست است، برای یک دموکرات رای دهد.
🔴
اظهارت شگفت‌انگیزی که آن‌ها درباره گروه‌های مختلف مردم کرده‌اند، باورنکردنی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/148112" target="_blank">📅 23:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148111">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae9633a2e0.mp4?token=fg90IRtTaJIVODBNG_T21ehFjmd1nddh0mXN9OomOjjstgsEryS1LW00OqHhpIIIwTU_NW4x8izKTZXpsuy3wU3FOsnIzczZg7kIjcOXd9farBTTwO-73TGwia1CimTGMSoXKXfKXhHHxkDVeZlDA7THYCf5PuCmqy2LVWWRFn2RVBxp__Z9ybvxZtlVG8vWLz8BT3i0sOfBZrofHnPbhc16K2GMTXO1iIvVs7veSslcchscZvVQNNly0WcQMxtgBTXXjgKrZ-bcdQz-rT_9oRiWj0xGu55WhMuzU9Ek2VcboyXjCa5JYcOuCDecuurnzFmY-nOMhvCdIAyVvxjMWp36-CkgG05hGzEvZ_y2jgSYoFUbWI6wGCJtSe2xXKGh4ALLmcGkHCqG3o3EAq0G_wWhrtgbyO1RSRlrWS3ze54O859Pn6b2KHc09ue6u60thJD7yJWQhnLH3r7NnJMcxOJ3YMRLquW2lO4qNsqrRluA_mKrJsr_VokdeZO1K-34JpesDOWwkxtKp1sjdcPaTXPNMZwQxpo4uA0NjBUdnf8Mcb9M4TO3zhc27d-_czlAtIkUTE7cIvVpNRCr5czCi-01NmKzwa7a7AmRrCXG901Q0BvoFLiDZWFkq3MPx9EGiDaXzPpwNNes4XspjKyMvza5HQoKlAT-PpaoLDl9TNc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae9633a2e0.mp4?token=fg90IRtTaJIVODBNG_T21ehFjmd1nddh0mXN9OomOjjstgsEryS1LW00OqHhpIIIwTU_NW4x8izKTZXpsuy3wU3FOsnIzczZg7kIjcOXd9farBTTwO-73TGwia1CimTGMSoXKXfKXhHHxkDVeZlDA7THYCf5PuCmqy2LVWWRFn2RVBxp__Z9ybvxZtlVG8vWLz8BT3i0sOfBZrofHnPbhc16K2GMTXO1iIvVs7veSslcchscZvVQNNly0WcQMxtgBTXXjgKrZ-bcdQz-rT_9oRiWj0xGu55WhMuzU9Ek2VcboyXjCa5JYcOuCDecuurnzFmY-nOMhvCdIAyVvxjMWp36-CkgG05hGzEvZ_y2jgSYoFUbWI6wGCJtSe2xXKGh4ALLmcGkHCqG3o3EAq0G_wWhrtgbyO1RSRlrWS3ze54O859Pn6b2KHc09ue6u60thJD7yJWQhnLH3r7NnJMcxOJ3YMRLquW2lO4qNsqrRluA_mKrJsr_VokdeZO1K-34JpesDOWwkxtKp1sjdcPaTXPNMZwQxpo4uA0NjBUdnf8Mcb9M4TO3zhc27d-_czlAtIkUTE7cIvVpNRCr5czCi-01NmKzwa7a7AmRrCXG901Q0BvoFLiDZWFkq3MPx9EGiDaXzPpwNNes4XspjKyMvza5HQoKlAT-PpaoLDl9TNc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره حسن پیکر: به نظر من، او یک ضرر بزرگ برای حزب دموکرات است.
🔴
او یک کمونیست است - و در این مورد هیچ شکی وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/148111" target="_blank">📅 23:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148110">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
فوری / شنیده شدن چندین انفجار در عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/148110" target="_blank">📅 23:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148109">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c79171cb8.mp4?token=ircQOExTV7AjynAACtRuCwUEmfup1XvLWalOTmFxQoZJa-AkwMfhy5HnI_tWpTm2KIuOxkWF-SjeRVWfET6O9o56bfpZqHkwJImbdGWNgJSH961mFXsxVK8O_AgvR9QcsompkLjNceazq4yjF7YkOpYUqjZ9AnupFOF0e1FfPmHDubZo5MPkmqXyqO4ldKzOSoUsZnryi8VNOuaxyEyFIhX_9HAIiEmfDRHDjmtcrBh1QayUz5kioGOl0EWiCIRzz92tKFkz4TLMxag9FIXFif3mQITq4mqNsRm_Epf4ry1FiFCSf0uF-gPpo5mhI-clWrbgjHemkBp9NRQfG0pV5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c79171cb8.mp4?token=ircQOExTV7AjynAACtRuCwUEmfup1XvLWalOTmFxQoZJa-AkwMfhy5HnI_tWpTm2KIuOxkWF-SjeRVWfET6O9o56bfpZqHkwJImbdGWNgJSH961mFXsxVK8O_AgvR9QcsompkLjNceazq4yjF7YkOpYUqjZ9AnupFOF0e1FfPmHDubZo5MPkmqXyqO4ldKzOSoUsZnryi8VNOuaxyEyFIhX_9HAIiEmfDRHDjmtcrBh1QayUz5kioGOl0EWiCIRzz92tKFkz4TLMxag9FIXFif3mQITq4mqNsRm_Epf4ry1FiFCSf0uF-gPpo5mhI-clWrbgjHemkBp9NRQfG0pV5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: به نظر من، اگر مردم می‌توانستند در مورد کاهش قیمت بنزین یا اجازه دادن به ایران برای داشتن سلاح هسته‌ای رأی دهند، نتیجه به شدت به نفع گزینه اول خواهد بود.
🔴
مردم نمی‌خواهند ایران سلاح هسته‌ای داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/148109" target="_blank">📅 23:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148108">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097ecbb4d7.mp4?token=hCxpdbdVQ6NjFOLvTTpVAfDzFwbGmhTcxzdZqMw-Uzi9_CBDOOd1V7oeXoVu_misIJz9b3E6qNC1qQe67ZKWcTOak_uYsCgZ6G16U-gum9wbDscORZcSAme4HkdxqyUf9ti8y7dpcxnPHfEn50reRjeEDO-mh-iqNp8bjsNX8yz3Vf6rxL_4KcpkZU_SNiF_jc0lmDSQlp5M3AINjdk1nc7A6H6h8kpKJ7s2-bjTf2ikkXHWObRPOdj5zxI6jFzKtho0lXW_tyo91G9xazImEYlOiz14VWnw2vRUNAvISM6KkfoQojZ6TzAQcGfxoMro5FCKtd0AOpL_daSF2S1teg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097ecbb4d7.mp4?token=hCxpdbdVQ6NjFOLvTTpVAfDzFwbGmhTcxzdZqMw-Uzi9_CBDOOd1V7oeXoVu_misIJz9b3E6qNC1qQe67ZKWcTOak_uYsCgZ6G16U-gum9wbDscORZcSAme4HkdxqyUf9ti8y7dpcxnPHfEn50reRjeEDO-mh-iqNp8bjsNX8yz3Vf6rxL_4KcpkZU_SNiF_jc0lmDSQlp5M3AINjdk1nc7A6H6h8kpKJ7s2-bjTf2ikkXHWObRPOdj5zxI6jFzKtho0lXW_tyo91G9xazImEYlOiz14VWnw2vRUNAvISM6KkfoQojZ6TzAQcGfxoMro5FCKtd0AOpL_daSF2S1teg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: جنگ به زودی به پایان خواهد رسید و وقتی این اتفاق بیفتد، قیمت بنزین شما به سطحی که قبل از آن داشت، کاهش خواهد یافت، شاید حتی کمتر از آن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/148108" target="_blank">📅 23:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148107">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ترامپ: جنگ با ایران به‌زودی پایان می‌یابد؛ قیمت بنزین کاهش خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/148107" target="_blank">📅 23:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148106">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gThynslLRINg8OJuHa61zQBLkR5uIbRWeZitvYSRdkGeZjsS5b6HZSJNZhMxCA9leIQ4FD27f3heL5I_ToD8f6sJjr8ww7io-cWnqw13BDMJjMvporFDRYDDoB8gkHCBdd2_pZPyoxwKlNiaXQAzQOvw6EaJLHyRlYVDsoQCT_KAA60_M3Dw7PKXuZNgO84vonJcSicYfbkjp21XKjLKTnrW7FmQKtWt2BVAp07WRJ4ssfIGi-cs4Ian0H3QZpn8IKJkCttIqnBjhazu9BK8ykBeN8d4wOgWC6LMQQz2DDHLlma_uoyuqXmv78quFKGekjTOEFGbnP1utDtWhCPsCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه برق کشور کوبا تحت تاثیر تحریم و محاصره آمریکا دچار فروپاشی کامل و سراسری شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/148106" target="_blank">📅 23:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148105">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClAM0Ckh0Jj65UBJ4FwjlwiO_7QkMyEjNjRTAqZLlSdevKXWNsv_pUr7ebSmZj2UVH7mjYSy59MfYfMtLp9InWzbDrP32-e8Ag7_MHvhqVsvYwzEnZFVuQaCiI43HpQjUPqmOcnmJcPx5tgciAyPvGDuAWTLVqZg8Ginm8pbWDFd9GMqJzjzP5OLVDva5bq3_0W_S0-99XDkIE8b8gLsDLQ82VHyTxUKHSdfbTkobj1Lk7dmyxql0Krv6QRG12i4tj0wmuauSHqdMhoXUCFfWmdyzfFI62wQiGTOBX12oG_fxPlNmn99sLmtDx6SwVgL8BsQOPwjdLAx348ysH5o-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: ایالات متحده به متحدان خود درباره تأخیر در تحویل موشک‌های رهگیر هشدار داده است؛ تأخیرهایی که ممکن است تا پنج سال طول بکشد، زیرا واشنگتن پس از مصرف گسترده تسلیحات در جنگ ایران، در حال بازسازی ذخایر تسلیحاتی خود است.
🔴
آلمان و کشورهای اروپای شرقی با تأخیر در دریافت تسلیحات مواجه هستند و درخواست‌های اوکراین برای دریافت سامانه‌های پاتریوت نیز تحت تأثیر تلاش آمریکا برای بازسازی ذخایر داخلی خود قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/148105" target="_blank">📅 23:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148104">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tv8m-LZ2ZDNdD2dwTEV66qTlyuzRCEK7XtL-ZVjYlMIogdZ_NagvMLYaUF-mqALPSt7zmx41145KxGT_tiM0F49KTbMlQwFQqI0SGA-XcfrX7aqqGcSHsdN9zKxGepWpo9pRvpmPZUyP_db6yGwN4Zl2d0GPYzryNQ1P7IqJP1F9OY6rMz2BMwycXaOL50115KmHXXydfAuRKR9Vs4Da8scF1kgg_ztVSI8eN6AbLjg-tevDGTagwOhJ-hKtxv1UVa5YIiKdbg2RsHmjtAVPpDeNqpFJU7oM7a9JGbkvfpAodd9sJAVzETnJk6HtxSsvorOCWAMQ5KLXJTfWOibmHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمایت خبرگزاری فارس از پورن استار حامی حکومت
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/148104" target="_blank">📅 23:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148103">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
️نشریهٔ پولیتیکو: این تابستان، قطعات حساس هواپیمای جنگندهٔ F-35 به‌طور غیرمنتظره‌ای به هنگ‌کنگ منتقل شدند؛ درحالی‌که قرار بود از استرالیا به ایالات متحده برای تعمیرات ارسال شوند.
‏
🔴
این موضوع باعث ایجاد تحقیقاتی در کنگره شد؛ زیرا نگرانی‌هایی وجود داشت که ممکن است فناوری‌های طبقه‌بندی‌شده در اختیار چین قرار گرفته باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/148103" target="_blank">📅 23:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148102">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/040b6f8928.mp4?token=HmHkxs7KsgH5_KgFhXLgRwu7e0vZpPAOSkdRiKZ2kEo4y_RFA4YaY0ceAE1tSvDH4ZfAJMpe-e2PG4qlEt_-hoM9-XCKBjtGEGkGXbyU7Sh2ul26PbOEvPSarmm0Exd3kjl5fNrhpV-26i8EWeBDxXHk2K6PcRr4gfheCA5TP3GsXeNZIoCQAOkoiiRZc-cPts-bgoM5srXOfeQOp9v1g3ZWk11s-_-SUCFRCB9nWYi5gDxUj2HHSEHx4IZPyHvcUi6exqqglOWUXw3lBfMUvQl_vCvuc4ITbN77DItcaEHuoKacQicuAzh8ssNZshhMZzOv3WwwUgEee7pmo1B3bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/040b6f8928.mp4?token=HmHkxs7KsgH5_KgFhXLgRwu7e0vZpPAOSkdRiKZ2kEo4y_RFA4YaY0ceAE1tSvDH4ZfAJMpe-e2PG4qlEt_-hoM9-XCKBjtGEGkGXbyU7Sh2ul26PbOEvPSarmm0Exd3kjl5fNrhpV-26i8EWeBDxXHk2K6PcRr4gfheCA5TP3GsXeNZIoCQAOkoiiRZc-cPts-bgoM5srXOfeQOp9v1g3ZWk11s-_-SUCFRCB9nWYi5gDxUj2HHSEHx4IZPyHvcUi6exqqglOWUXw3lBfMUvQl_vCvuc4ITbN77DItcaEHuoKacQicuAzh8ssNZshhMZzOv3WwwUgEee7pmo1B3bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما در جنگ با ایران، به طور قابل توجهی پیروز می‌شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/148102" target="_blank">📅 23:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148101">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
رویترز: داده‌ها نشان می‌دهند که حجم حمل‌ونقل از طریق تنگه هرمز همچنان کمتر از میانگین ۱۰ روز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/148101" target="_blank">📅 23:16 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148100">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deace85529.mp4?token=UxjW8VUXkhRBvfadDcUGtGNf7slp5Y0dDf54hBn8Ij9xrlqFrUxUvEScn6bTGUikAg55iPxnsZ4jhAtRzQe9XkYG7do-HF2ofEFhNWKcqGAXeYGVVCXnZHp0oaspGadrQyfmllVYuqxO6RsxSuzldODuZutW1edFUsP_eAkYPjVF5yjuThXlzb5uxl7UeVg-yN1sqJmgVERhJhLZHwqJXKdQmRUo9BZtiN5oo6qbHfJRZN1ZRUJLnfqRyKL6Pp1LnSWHmMJxP5Yj9wUTG2RpQclCN-iwHo_R6YxuOclM3MGXHH5pM-mKS6e5xAo8FHSaBvKnWfJEGIEgkGDe8mZLSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deace85529.mp4?token=UxjW8VUXkhRBvfadDcUGtGNf7slp5Y0dDf54hBn8Ij9xrlqFrUxUvEScn6bTGUikAg55iPxnsZ4jhAtRzQe9XkYG7do-HF2ofEFhNWKcqGAXeYGVVCXnZHp0oaspGadrQyfmllVYuqxO6RsxSuzldODuZutW1edFUsP_eAkYPjVF5yjuThXlzb5uxl7UeVg-yN1sqJmgVERhJhLZHwqJXKdQmRUo9BZtiN5oo6qbHfJRZN1ZRUJLnfqRyKL6Pp1LnSWHmMJxP5Yj9wUTG2RpQclCN-iwHo_R6YxuOclM3MGXHH5pM-mKS6e5xAo8FHSaBvKnWfJEGIEgkGDe8mZLSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دعای عجیب روحانی عربستانی: خدایا به حساب دو شاخ شیطان برس، اسرائیل و ایران!
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/148100" target="_blank">📅 23:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148099">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
رویترز: ایالات متحده و ایران همچنان در مورد مسائل اصلی اختلاف نظر دارند، اما هر دو طرف گزارش‌هایی مبنی بر پیشرفت‌هایی را منتشر کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/148099" target="_blank">📅 22:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148098">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTNGtTAmtEcSbRj0j5nV_P4pDWnFxQEmY4uyZ_GiVT27W8aPc6xNs-GqB6SgK_qegN5ZIHWuR0Bu5xFv43CAO_u_xYZHSnCdA-YOEtL7knnuOz6kn-00XGcueMgxU1Vq2q4w-osWQMC72ONOF8b8TPhAX2Yzo-Yz7TLvVuLy0FwEEip6R9icCxc7tTVgYXXDSzwMK80WEY0vPVapO8Wqked5k653ZtlNVRib2QoMnBVjX8PZy5deAGj7bpPzOcvbTHGOkx_0BlMLG3t1vpaPQ_v5Afa77TMH0Q6B3w0_x3n0iwS3CrDoBqEzLSjbuh-oy4rIfR8AOCCknIHTHwnL2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / ترامپ اعلام کرد که کانال‌های CNN، MSNBC و نشریه Politico از این لحظه به بعد از ورود به کاخ سفید منع می‌شوند. او این رسانه‌ها را به انتشار مکرر "اخبار دروغ" متهم کرد.
🔴
او گفت که سازمان‌های رسانه‌ای نباید بتوانند به طور مکرر آنچه را که او "خرافات و دروغ" درباره دولت خود یا ایالات متحده می‌داند، منتشر کنند، و هشدار داد که "سایر رسانه‌های خبری منتشرکننده اخبار دروغ" نیز ممکن است با اقدامات مشابهی روبرو شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/148098" target="_blank">📅 22:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148097">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بیت کوین منفجر میشه
‼️
‼️
‼️
اگه توام نمیدونی بخری یا نه حتما ببین
👇
https://t.me/+4jOgodAq96dmYzY0
https://t.me/+4jOgodAq96dmYzY0</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/148097" target="_blank">📅 22:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148096">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buihgDIYRn2Tq4Ml0DQIGHpOSNC_fc0HyGqDlXC5WAAUUJe5fhqsYlEfxIENjg2D0oYVgNal-XpDY8BPbpxUgCvl0oZ2ijA2IhBJTvwN8RTtXUAh_GMSanpoR1BLei5Aq4CE8J5jKY-2gboNfZmYpw5bguqw3S2qHx5sHkYyKq08kbRk6uOzs4FivO_bCKFkdMHdwBvsqZJI41fBr6sqRXlNFSbAYInsB5dL4a7eSKTMlL5mElhVeFfik6C9hyCL85wbfD8uPgsds8QRxLheI06A33r5ZGeO078bCV_76fVtVUo0sFwC5ZVF6t76p-xMMF9MkbiBxLD3IiGEy5sNLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حدود ۳۰ دقیقه پیش، دست‌کم چهار موشک کروز ضدکشتی از منطقه سیریک در جنوب ایران شلیک شد.
‏
🔴
صدای چندین انفجار از سمت تنگه هرمز شنیده شد؛ جایی که پیش‌تر در همین روز، دو نفتکش هدف قرار گرفته بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/148096" target="_blank">📅 22:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148095">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
پوتین: روسیه هیچ برنامه تهاجمی علیه اروپا ندارد و آماده همکاری و احیای روابط با همسایگان اروپایی خود است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/148095" target="_blank">📅 22:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148094">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDoNo9NtMzj6nIRCj7aWIlQ6n4wJ1GVR50PhH_gIZhbN2vopYsOUO5m6uT9NM3sgfn3-ibpexwhDOnrB5BvTEv4w4m-tavSX1nrudeU-EczTw4eWhhjlNRpVjb0m5CNMvF3DsPH6bZC5uQiAB3ElRUSqWyZXNXuVxLrJJK78ZvwLvwfzQ2GgUzHuPMH_3Ex1yZibTTOOLt6NFYuX1zi5m0MudZlNk7WQU28A8qRMJLc9fxJ_IdTeVoX2q6ekckEU50CmQpNXPJN57BR137UeVrazmNjjQNKTdTlu4Ir_h8JqymJZ0eMypZTigoHmRU5ldk9CsV3bBWcHf36XUVhgAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واشنگتن پست: تعداد پرسنل نظامی آمریکایی که در جریان درگیری جاری با ایران در خاورمیانه کشته شده‌اند، بیشتر از آن چیزی است که وزارت دفاع اذعان کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/148094" target="_blank">📅 22:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148093">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
کارشناس صداوسیما: الحمدالله وضع مردم ما از مردم آمریکا خیلی بهتره
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/148093" target="_blank">📅 22:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148092">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
نخست وزیر لهستان: روسیه ممکن است به زودی به لهستان حمله موشکی و پهپادی کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/148092" target="_blank">📅 22:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148091">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a967d061c9.mp4?token=K0ZdUhOF22q2E3wgJnEFH-1OMFGjufKx84sKtAGl-Dc3auywvJnYNm3pXxZGqGKU7WwiDeDvLlLVv7jFPIYOOCk4x--va2cImRlpRFWWT1nWA6rfPfuBL1w4S4uIdtdZlihIo5tJi-vLt23lHY8MbJ453jczpBTx_TkflK3x6oZH82-sscMHzwrUjo1B54F-fDGrITHYxkABM6ybYGjmHwuBM4WJKJmKge_K7ide70OISbXlV0VfIGnIoVm_b_I3I7y-zGyfzlr__C5qzySUKCqXsxetG0BH__dEr22CXsNLW5be9Py_zgKCcxLqQVqbZUXdIc3QDICP1w9bRCxIOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a967d061c9.mp4?token=K0ZdUhOF22q2E3wgJnEFH-1OMFGjufKx84sKtAGl-Dc3auywvJnYNm3pXxZGqGKU7WwiDeDvLlLVv7jFPIYOOCk4x--va2cImRlpRFWWT1nWA6rfPfuBL1w4S4uIdtdZlihIo5tJi-vLt23lHY8MbJ453jczpBTx_TkflK3x6oZH82-sscMHzwrUjo1B54F-fDGrITHYxkABM6ybYGjmHwuBM4WJKJmKge_K7ide70OISbXlV0VfIGnIoVm_b_I3I7y-zGyfzlr__C5qzySUKCqXsxetG0BH__dEr22CXsNLW5be9Py_zgKCcxLqQVqbZUXdIc3QDICP1w9bRCxIOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ستاد اطلاع‌رسانی نیروهای مسلح یمن جمعه 27 شهریور، صحنه‌هایی ویدیویی از حملات پهپادی انجام شده به تجمعات شبه‌نظامیان حوثی در جبهه شمال استان مأرب منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/148091" target="_blank">📅 22:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148090">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
حوثی‌ها (انصارالله) اعلام کردند که جنگنده‌های اف-۱۵ عربستان سعودی از پایگاه هوایی خمیس مشیت، در ۲۴ ساعت گذشته، ۲۶ حمله هوایی به استان تعز انجام داده‌اند.
🔴
آنها همچنین مدعی شدند که نیروهای سعودی در طول هفته گذشته، ۳۰۰ حمله هوایی انجام داده‌اند که در آن از جنگنده‌های اف-۱۵ و تایفون مستقر در پایگاه‌های خمیس مشیت و طائف استفاده شده و اهداف این حملات، استان‌های تعز، حجه، مأرب، الجوف، البیضا، عمران، الحدیده و صعدا بوده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/148090" target="_blank">📅 21:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148089">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRaHSFJbBcYi00Fo8vEt3h2pi02lJtfqbJ5LczDAr_NvCNFshzDFSoVbFlHEZLIWrWjXQUZhobRo06Tz4oP4FMd6rcnKCuUaHTSNOyycThwuAjXU06tzfGfLQ9WBZpuBILeamePOKw0kTCaFdDHGMAxneWsrb0rlS3_Z89vpHI5No2w876gj704FeqeCDWJ1Ta-2cXm00MsYVp2MYxN-G0-Y29b6fdIjH0492vcg4AdjSqHR7MvaHczPwamTBLJMyXzmdmjSzLwi4KDFS3VArOEYE_WkmOTQnUGHTIZNWxIz0d-ZJ99tt9N0r4oNiyTCdlGDFT-S9poQGQh7rFmLsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ
:
روند محبوبیت ترامپ در حزب جمهوری‌خواه اکنون به ۹۵٪ رسیده است، که یک رکورد محسوب می‌شود.
🔴
رتبه‌ی دوم، رونالد ریگان با نرخ محبوبیت ۸۶٪ است. از شما سپاسگزارم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/148089" target="_blank">📅 21:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148088">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
احمد الشرع،رئيس جمهور سوریه درخواست عربستان سعودی برای اعزام جنگجویان سوری به یمن برای جنگ علیه انصارالله را رد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/148088" target="_blank">📅 21:43 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

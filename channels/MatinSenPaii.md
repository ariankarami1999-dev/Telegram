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
<img src="https://cdn1.telesco.pe/file/d5dwh2Vl6g_D2RrA7DLMvaWSntG1vCE93d4Kr7zN3m44lQuOWf5cvaOWjf-MuHN7TzKYgpAOlk-YsSKssBdj7gSEameCi-FAlTDMlgyjA0xx5E9yWA3OLU8DtEHhTdha-Bdb4LNZr0FQsCVoNRq7uvn-eoXvgbhVVq2g5FbNYQ0rL0Bg0VyWrmijq1L8IiuGQV7JGjQhovEHdkRPxUkDh8E5QGPyg9Hkuv3i6HnwvMDxdlVH6-NzXYOS9EvSK3cPP8XMRp9ERoqZTynA1B6RpAqq7xdFzL_YyYECywEQ8KpTcJy12e-l8ZJo_Y4EJUy2bHdLGy8cazcEiU8303ikDg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 156K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-05 20:40:41</div>
<hr>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a2386a8b3.mp4?token=aziPDMHV9eEAKPC3jiCMZNpoulcOvRyjVTUiMZ04rDXdFSEgOT8DkE6ppgoxEtP7xMhghvjLybgmEa1aL7ieo4wbemLruS-jIyERMoXKSkgAQ1ROV25jk7VV_56r1v5bss73RjyIN76px7gou1Yh-vFgvXAqhGge1vmb4tEjAlJsmppucQBFLt9f4N_nfDkPbAFvTkOM05yHQ4F55cECjxHaZ-jJe_cCzAos2CYbOOiwxXLyiHHdgwxwGI8NoTd72hCr9LafikkKt38qIfg4hJjobHQcU3w2U6V5urXKRZMPO3jV4sbKzppPIhjhQsqFbcK-QvA4QdvTA2wotw8N2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a2386a8b3.mp4?token=aziPDMHV9eEAKPC3jiCMZNpoulcOvRyjVTUiMZ04rDXdFSEgOT8DkE6ppgoxEtP7xMhghvjLybgmEa1aL7ieo4wbemLruS-jIyERMoXKSkgAQ1ROV25jk7VV_56r1v5bss73RjyIN76px7gou1Yh-vFgvXAqhGge1vmb4tEjAlJsmppucQBFLt9f4N_nfDkPbAFvTkOM05yHQ4F55cECjxHaZ-jJe_cCzAos2CYbOOiwxXLyiHHdgwxwGI8NoTd72hCr9LafikkKt38qIfg4hJjobHQcU3w2U6V5urXKRZMPO3jV4sbKzppPIhjhQsqFbcK-QvA4QdvTA2wotw8N2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این لودینگ ها هم جدیدن و خلاقانه خوبیش اینه که SVG هستن و توی سایت و اپلیکیشن و هرجایی می‌تونید ازش استفاده کنید:
circleloaders.dominikakissi.com
@Linuxor</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/MatinSenPaii/5071" target="_blank">📅 18:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B3nJjLp0CSS8LYCVVVETMpjd9hyoHBkxjPd3LpULzo7ZoArAFcgXQOPC6yOAXaJlcL9_7aRwhNsUXTmmwO7YZXQKH0qGckFx5jm-yQtwtEJAbpRjD4KTYPFD9hYXZFdHgheK7sL9wuif6nm1JvXEg6gWFMTTgjvZH0W6Qysk0cJxpPNdMNykehGXIOUzsZbGKhoPy5soYXQ7d4vASlAtFKPCvXQ52djRtc3rmy2_v80JL7RHbZQhQDaCjd1_MweMCY7X0DIWvI76IGMio6coki1fgshyzSu1XbnMD948ZtpCsHz6VWzOdKE6EHQdFgg6rftLmXcal4SBNPqExhDjnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچقدر از هوشمندیش هم بگم کم گفتم</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/MatinSenPaii/5070" target="_blank">📅 13:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ECq9d48K-971gW0t4qLFmHz6TExluWyyO2YIY1zA8pDGdRFg9MBHeGnHM_Fm__bSDHBzU_5-t5V2p4ZpY2suxS37DdpKtdhnoCMimH0vdlkNOHGXhx_R0o-ocgum2rlAedU-CWyskSdJFQBwfHl4vOEHWyzNW7jzIFzPqBcBVssKZiqjW_6Q1M_mhqUzr30oDM0oXWql2uqBdq-vYenN4IMyPR-QtnQMb5SC_zhQQLFpCKBfRvl9wLJsZW6uvqx9oISYz6wFOq40HPsizAfUuoGLiYcrD8L7ZjSKDjMzqioyDv9rlZ0BOWR6woFTS-GB1BOQi42d3XpXPEqdbpPiGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ Input Cache اش خارق‌العادست
روی خود هارنس OpenCode</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/MatinSenPaii/5069" target="_blank">📅 13:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5068">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JNfgSXvYWO4znS3Or--vQ4hlQRBIzG1658h2Uz8VA1qMAoKXniNDYPbZrlSttBqWFIoH3pg0pv2_48sLlk-tzIBdI2FEXP5-8xOj4iC1avbdDVOsC3vMb5l8GphSFV93Qa0OrlZq4mxIcTFGKmIIiZrVcn8NXphaxYhOIQ1doBmCG5vcrP0phxgGY_W8YMAT5fMDAxok5WOus5YO2JecyHLlrkhtAUUi24vGs3CngQ86HlrnluJE-R7pzCvQnM7eWBGBX18EsgOLlzbLnrUUdIVsZJNxWpMGQ-2OOEGWoc-1gWljXaG8QV7sN9UUg0zNeRitj6xHgqeE5q6uLor67Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصرفش خییییییییییییلی نسبت به GLM 5.3 اوکی تره
و راجب هوشمند بودنش هم که دیگه یه ویدئو کامل دادم نیازی نیست بیشتر صحبت کنم. باز ما میگیم درود بر مدل‌های چینی به یه سریا بر میخوره</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/MatinSenPaii/5068" target="_blank">📅 13:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5067">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZP82fVLi1TRlNICh9CcSg0Wixnan2eXaVyaZaYE8S2fEGEJnc3-oWLkjYAVj3Uj_KKm5LA-R7Pr1iEpc00sSyevg0pF1VpzotBurBlwrX2oqj5RiLA1-yaUk4nYdqI_QyEmCNQcvJG3sKgtzL7GQjqbWuV4oRRQtVicpx4mOSatHN3mlDcY66FwOr6MhCqG53WfRQDLJM4yMQkoIARgpxrk2p59_TbMtN7kFaJdlrduhu_gFIrRjBsNnzNDVC5RJS9WKFIx_G-2HRhFBu6xNw89Z9-RMH_3Hr_4R8ibh0NA_bEgVtB-bfCSbwZEwsEpXGsJ7NMtKfJc_cmp6MKX7Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی درد داشت که Ox Alpha رو عوض کردم روی GLM 5.3 Flash و الان دارم واسش پول میدم روی OpenCode Go
😭</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/MatinSenPaii/5067" target="_blank">📅 13:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5066">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">خیلی درد داشت که Ox Alpha رو عوض کردم روی GLM 5.3 Flash و الان دارم واسش پول میدم روی OpenCode Go
😭</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/MatinSenPaii/5066" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/MatinSenPaii/5065" target="_blank">📅 12:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rQeUxZ4FGTdMZeC0p2NCQ6U1rka-bIICcD0YIpx0qb34KY8bEe8dsUi2cxPSP3pmK9KQN1af_zPN8g4_nM10jlIxUAfcfv4cDJl0fLHYB-zT1J2Yfg-viny5xFYoL9huJgzSWW3bma8YbM0bgZ_TZUsabf3Gy82jYU_e4FrJ-gE0_5TSOhiKeIBlyHbC4l4PGrpLx6LgRnzMLWf9egW4TFSmWlIBW6aDovHrLOa5v63ukKBx51XQc1yGP8SuLHKeX_b1aV0Mn8Qqxph3XlfkLXjJx9oZUK9VsiTkPSIZnlV0_Oh_Z1LP-5IPq_9WpTe8auS5BpekRX1wyGkeoKHf9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM 5.3 Flash یا همون Ox Alpha، به صورت رایگان روی Cline قرار داره. Cline هم اکستنشن Vs Code داره هم می‌تونید با
npm i -g cline
خودش رو نصب کنید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/MatinSenPaii/5064" target="_blank">📅 02:26 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bcWdIfFaEgXJ6QSuBgHHTkYGbG90SEQ3JykcRQIohayzQXk56Wy8yLBT8-SGkhZH4uZRqlutylEjy9WSd0JATpw_7B-GCF8RJR0BQOKKxYY_QKbqO-xCJ35Xac7OtP4Fjr9Euc2_3-xz9uY2gEGlQCV6cWPLP9XiWN-IUZOwxx_rxkptzLGfqZ6xrhx_aOLKCcoLqgSSH0CWcmw47bgM8tNTwqzpOCJQcH07nceDoSLTQ4DhSqk57ClB-ReUpEw6tkmUWOyzXfPrCYpRsP3M-FywbtlVmVB4EhP_okt7iCn5MkfZZkbcH_zJ97a41fkbWL9YMIsIQeL0GeYIUkXngQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی این بنچمارکا همه‌اش GLM 5.3-Flash رو با GLM 5.2 مقایسه میکنن سؤالم اینه که چرا با خود GLM 5.3 مقایسه نمی‌کنن؟</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/MatinSenPaii/5063" target="_blank">📅 21:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">توی این بنچمارکا همه‌اش GLM 5.3-Flash رو با GLM 5.2 مقایسه میکنن
سؤالم اینه که چرا با خود GLM 5.3 مقایسه نمی‌کنن؟</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/MatinSenPaii/5062" target="_blank">📅 21:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eIIInpEFOfPOWpaQBUexsk0FUSGM4K1P02ylxvQhect44DB4uFNo5dDHdkhrFxOy-upz7GqzLApNNmxjyCTHlJm-OTeKy0wkz5Clve_YEFxyNgjddS6VcXzRAbAtEsWSg_jRGqGe7ObNONxXPirDPNjR7-BbZKRpGvVFRtUPaIJCTBB7L-SGQA_g3TE5_Sz-YQVr8yKpbpy1o0uGKEY5DPY_-gOogBTTj8xCiDM64Tym2F1GPPBazTe1KZAOftgU43ZD8MhzlhC3v6ju8rP3-tf6hGw04-XtA55QhxIIoepX1WnquqyUp0q862Jic2fQqKC-6WhnOxY_uCTVfZb-4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/q9JNTcP1c2saEW0xG2d1EOMPUAuOc4B3FO6ngVrte9q5F9pNVkUxlbLmTXpILual-Zw1VuqHY0DJSAXch9t-slWNA8xe-tbll_H9OgBA0rWxsWPg8hlXAHlljoAqEz-hdAPhQ5DSyazzqJN5oqDWjs4RaB9NsaGpd2syfbDJKW2Kt7UELSq-vY-Wd-UVO7fSKAoUEg7tylG5oUo0Dj1DwRDaXvkEKexd5xPMKno5fCeTfAIDvMVCarLCHm47PJfTp9t-Yf68-LcstYzsL67xz3rBZMchzIV8Y262uHi4iC7K4JQW95o0X8mgrcxuCWswNgm8F5_Vdpd6aPq_WvYqHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DnmzGVxjnexBJaTtMge3mM00j38QqIgWcWW4667izXQAVUDgrHfn5BgsllnKI6X9YTPjObtJUGpIgAoNPv-2elj7YyXDqggA0KX4P22lnFBVwbeLe2izsAjbBM8no4P3TxTuTSdc9DUgExozWUi66mzBVUXx43nAHKWXOCmCfkifYBgmA9hZofc1RU3hPkx0lHR5170mwX48NMti-YepjT2plhQhIn41cT6wBTh_pD4iyzhJJz3E880kRj8BE5Z9ok2hHROBMbeL0TOyGO6muJnFUTDOT-CbxxvN4iY0Z_It8n_zc9DvF0hvyA9rlcxQqS7pQoqoP6erv0iTeFL55Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q0y7OEIQh3MpKxBbKrtM3mL_ozeYzc85PUaFKylai5c9T5MGi8usiLR6FW_WnaYUu288RrrT1AEwNAnlpy6PqDSLx28jecLbVgAhBdgDxSAfAiyizNE1km_uEBhS5PVEKF6qvunCzanovC1iAKLj3NyHzvxWX2fiwTGhS_UnKTgT_VqleI86d3QOgFeI8WHr8l04_RAcXaYgifm71Or9DtBN9FTOnZVe8Ul6CzCnRCKlIiPF77YsPzdOKQUIRTvZM8TVUOGvHPCYgrxCK3sKk1r-H9TvhIFPkeyabH9qpXl7YHSJua3pcDpRkZLDo9Nn_NpsXBO2eX8L6Ofy14UYVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معرفی GLM-5.3-Flash و ماجرای Ox Alpha
شرکت چینی
Z.ai
بالاخره مدل GLM-5.3-Flash را رسماً معرفی کرد؛ مدلی با ۳۲۰ میلیارد پارامتر (معماری ۳۲۰B-A18B)، لایسنس کاملا متن‌باز MIT، کانتکست یک میلیون توکنی و قابلیت چندوجهی (multimodal)، که به‌طور کامل روی تراشه‌های هوش مصنوعی داخلی چین اجرا می‌شود.
نکته جالب ماجرا، پیشینه‌ی این مدل است. حدود یک هفته قبل از رونمایی رسمی، یک مدل ناشناس با نام Ox Alpha به‌صورت رایگان روی پلتفرم‌هایی مثل OpenRouter ظاهر شد و به‌سرعت بین توسعه‌دهندگان وایرال شد؛ در عرض چند روز، حجم مصرف توکن آن به رقم نجومی ۴۲ تریلیون توکن در شش روز رسید و صدر جدول‌های استفاده را قبضه کرد. جامعه‌ی فنی با تحلیل نشانه‌های تکنیکال (مثل نوع توکنایزر و کدهای خطای مشخص API) به این نتیجه رسیدند که Ox Alpha احتمالاً نسخه‌ی آزمایشی همین مدل GLM است، تا اینکه بلومبرگ گزارش داد
Z.ai
این حدس را تأیید کرده و وعده‌ی انتشار رسمی وزن‌های مدل را داد. جالب است که Ox Alpha پنجمین مدل ناشناسی بود که طی شش ماه اخیر همین الگو را تکرار کرد (قبلاً Pony Alpha از GLM-5 و Hunter Alpha از Xiaomi هم به همین شکل رونمایی شده بودند).
از نظر قیمت، GLM-5.3-Flash بسیار رقابتی است: ۰.۱۵ دلار برای هر یک‌میلیون توکن ورودی، ۰.۵۰ دلار برای خروجی و ۰.۰۳ دلار برای ورودی کش‌شده. روی بنچمارک کدنویسی واقعی (Code Bench) در همه‌ی سطوح تلاش از نسخه‌ی قبلی (GLM-5.2) بهتر عمل کرده و با Claude Opus 4.8 برابری می‌کند!
از نظر معماری هم ترکیبی از MoE، Sparse Attention، Linear Attention و لایه MTP به‌کار رفته که باعث شده حافظه KV-Cache به ازای هر لایه حدود ۴.۴۴ برابر و محاسبات attention به ازای هر توکن حدود ۳ برابر کاهش پیدا کند؛
خلاصه: هوش وحشتناک بیشتر با محاسبات بسیار کمتر.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/MatinSenPaii/5058" target="_blank">📅 18:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ODeTKGiV-HFc-wDEw9haEvPPoLCsicBcD3MIkmFqj-YH5c5zxzVMWdMIsWdDe3XZT3wLv4LopGtLTbZ-lj8dibficPPAKVXD1VIaZvF9YJbKkjwmQYoiUARnHGv4fls74Lg8Xcei9BKGpiVfko5j18JHrgePT25R8RiFKbFm1Hhle3dmxBkfTEFnDwvRNw6znlsflQlnRNdZ0QyFQG1T9ScDd7ULOHjUmR_nx385g7VF9Xe0nMDBeD2uUnJ_trH0Ly1jf6tskc6z5Ceneyg8fkT1D7dbdyAmB6WHhxTlow3gYDhKzG4rSjtn--hNN4dwtnlgFRUcLwlRAeTri9zwOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LbeIx_AWRfQeYFg_Y8Oe2S8NGIPBXR2LzRBE3775qiaJ7uyRHZbjMVzFBa59gKxacRS_fmuJASMe8PfEydzK_4mkKWusCOxdGTLa1VVr8n52z9E7COTDw6g2MeFLZ4Ko1KDh2zl6lDqF7ksE4vmV4wLD35wbeoZh6adI71YUBCl4yxhFq8kZ9UUTaahxvf18a3kEO94KVQeK_-ruGfxgcTfRdniwTroIlBulXpO6Z1FAwo62Uff5gqIkMk6OKb4EdvXk62suczAJy0vSAf5HkAP01q3yIJmwD09TMwPSZOiX69bxwBUDDOH4Fi3HtGotK8CepcAZiRvjvSGZ2cnIjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rdxmBcVUFQb36yTQlDzs-5Yx3KgtmO3k1aIBGTQeEZIKH6cEyYEfV_LRLYnXAq8Z0eo9guAYLdYll6b7CGP78x25QDMZjaBngPj7PuTck8Vxs3HT9VykR22l75-Xa4Y5UKh6JEi0JmAXCNEVzu6CAItUDmMUaJLLKcgc_MpHRfaJhBrqIIb-OJ6ROQkzY36kt5vmFVgIstE5K6TZHHUTvxiKYcPJBLgZwPe8AcXPVxang5NuSTYxqJ1Svnoa_YKWDfDFG48EcoORrI50LzV-NHWAPG0sf6iTaquxT3MkjDa-UZ45HOYTG6fzYpJ6L_VRaw_sEyJrYP-2o7nYagt_1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">باورم نمیشه
running Entirely on Chinese AI Chips
😐</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/MatinSenPaii/5055" target="_blank">📅 18:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5054">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">خبر:
مدل Ox Alpha در واقع GLM 5.3 Flaah بود و گویا حدس همه درست بود و جمنای نبود
🥲
اما....
مگه میشهههههه
مدل فلش از مدل اصلی انقدر قوی‌تر
😭
😭
برم تحقیق کنم ببینم چی شد این دو ساعت که خواب بودم</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/MatinSenPaii/5054" target="_blank">📅 18:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5053">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DT3vYH2_zVbA_OuWqJ2_pHddjoRQyzaMeF13Y086Z8adlHx1eg1uQ7Buq7vdCjD1BVc93b9HEUeLxyFSCwIihI6jnrRN7mZ4R3dAHcdUG9GqMv2YGyjpsHLqEDmQ84ACOOPpc2-viYU8k88ptZAMQsL4Lb36xKYylJ_-O7bYZI_ZwtDGFtdv3UfpTWH8xJabBJlmBexrTs4FGlNrEvcy3CEn7PpqBx4lO4TRikuBdVTBiLwx1yi9Ymg_IYcccoKV210fuGR4RzoiK_k_ZVce244DkNV18hBCivWIdvKIN7Ya4FsdEzYHRDORHccWRy1pyvyYNNogLEk6czYWAdWi0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو ساعت خوابیدما
😂
😂
😂</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/MatinSenPaii/5053" target="_blank">📅 18:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/5052" target="_blank">📅 10:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iK5rAR2VIxvV-fyOrJjG7FhnBSYK1n-I0vOGN-2B5yceVyhjs9KK83pH2eTlGfHt7GPefgC-A9YGYmuErrlGjUNe5yHvMiEp_XlgDbUxVxFnC0lMXrj5OAV3CsrXWi6oyN4n8IuY-Zo_6tqz4s1cVCsL7OqmaIJXEK4G8DBCit3lQhjhWsLfOWPjOP1x-uJHKt-9MDKqhZqo24difEIDBuqp5kSOSt9I52zhZKNNzOWoEpqOdb49DidgwwRoa7rXfGQxvKgnYOnb1jobIvBmp-MxDNPtL7evgWYSAl60APZsQyguOA0Ujv76cFoANEbDc3h3w_wGmDwyST9v_vNZtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐂
چالش Ox Alpha
با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.
هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha:
https://youtu.be/FIhoccZtpZQ
برای شرکت در چالش:
1- ابزار یا پروژه‌ای که ساختید رو همراه با یه توضیح کوتاه و ترجیحاً عکس/ویدئو ازش توییت کنید.
2- من رو توی توییت تگ کنید:
@MatinSenPai
3- عضو کانال اسپانسر چالش، Lira Candles باشید:
https://t.me/liracandles
من پروژه‌هایی که برام جالب باشن رو ری‌توییت می‌کنم و در نهایت از بین شرکت‌کننده‌ها ۵ پروژه برتر رو انتخاب می‌کنم.
🔥
🎁
جایزه هرکدوم از ۵ برنده: یک
شمع صدف
و
توت‌فرنگی
از Lira
🕯️
🍓
معیار انتخابم بیشتر روی خلاقیت ایده، کاربردی بودن و کیفیت چیزی که با Ox Alpha ساختید خواهد بود.
تا فردا همین ساعت می‌تونید توی چالش شرکت کنید! چون احتمالا آخرین مهلت استفاده‌ی رایگان از مدل Ox Alpha خواهد بود طبق گفته‌ی OpenCode</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5051" target="_blank">📅 05:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">به زودی آموزش ویدئویی این ویزا کارت مجازی و روش گرفتن آفرهای رایگان و اینکه چطوری وصلش کنید به Google Pay و... رو می‌ذارم
🎨</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5050" target="_blank">📅 01:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gDPMhkorfBeXeNtgIZaBj_VztytWHqg9e9spzuaoYaPZSYekUF4lcivTeB9dfhyKj4ecKdLS2_MGLufoo_CT7adACFpR9IO0cOlv-UJhG6IjCVQW7O2yZCig1njcfu6fSDAhGrjHrNTw3p1GyxgZ-UEdbhY-7Fu26c2a2_T9Ools3r7j0rjqSUHr3K8KYeFV5p1s56ER4v8tv0-ItWsqtJrtaFmEOZC6G0fi8DWnUUZD3FVwFa2Cn6QrdDPsc_csNtspGAkiqx-RzrAOsoAQbHNkOV-gw3uSvwcLnrhSvAEs93w0Tfv1ze0i_KYtGLn0xKmaQaSBWOkGiQ3hy1lPbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قدرتمندتر از Fable 5 ولی رایگان! مدل مرموز Ox Alpha
توی این ویدئو رفتیم سراغ مدل مرموز Ox Alpha و اون پروژه‌ای که توی ویدئوی قبلی زدیم رو ارتقا میدیم باهاش! این مدل، به تازگی اومده و یه مدل مرموزه که هنوز اعلام نشده مال کدوم شرکته، اما بررسی و تحلیل می‌کنیم که مال کجا می‌تونه باشه. و همینطور بهتون میگم که چطور می‌تونید رایگان ازش استفاده کنید و کد بزنید
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5049" target="_blank">📅 00:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دوستان من کمی از لحاظ جسمی مشکل برام به وجود اومده بود. الان رو به راهم
سعی می‌کنم ویدئوی x alpha رو زودتر بذارم
❤️</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5048" target="_blank">📅 22:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5047">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">و خب من نظرم اینه که، Train بشه که بشه:)) مدل‌های قوی‌تر، ارزونتری که الان هستن و داریم ازشون استفاده می‌کنیم، بخشیش از همین طریق قدرتمندتر شدن
ولی خب شما باز اگر نگران «حریم خصوصی» هستید، دور چین و مدل رایگان و contributer رو خط بکشید</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5047" target="_blank">📅 11:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5046">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">به خاطر جالب بودن این پیشرفتش فرستادم. وگرنه به نظرم این نگرانی تا حدودی بی‌مورده.
زمانی که از مدل چینی/رایگان استفاده می‌کنیم، عملا داریم امضا میکنیم که از دیتامون استفاده بشه واسه‌ی Train کردن مدل.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5046" target="_blank">📅 11:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5045">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6f33bcf78a.mp4?token=lrFm90E3aFKEqT_Oa86niPjKKGaOruAWrSkWY7srwaVlyXcUpETM88v3TiL_V0Eosd933wPPq_2odCDaGNDPJSgldoHi9-TVyk96PuRE_BJOeGWflZjX7DarcnUTO3mjoywujZl-RTQM-JPqTGMXblvqVgmnruD_OenhaKFIcFoN2tjhIh5o6WmXS7d3hVpJ_6l2d3TEtzwFKjBIcxpBeq8CB4el3JUb5LhqIXU8qz9bUSdFTRCF8fvnoXjBYjbZfmKmpG_4KZmR1ObL4YxFYp4cGsx5xYm5zR5PRO5HYMPwdgTU4SojfnppbmZg1_8D5tdi8Dbn3zvxn9dUH8Uz_nrKQYp8BXfzbBZZVmLFEf9vZ1SgUm9cK1IZgNcvESGZRJH8AvkZ2twhRfnK7U75f05qFAWbQrJXB2NVNYlggQyQVxOZEnYq9w1VmISW7R0mk0Rb0Osc-eDY0rUJSPguwvDGEQcqDLrRBrW1OU_fRS0csmk7JkdE8_8Y-qlPMYr0KMcirAg6D_2v30nZxJMjw_rf6uG6b6FgLJFxb0pgpTTdWERPjbeZFe5KglPtFy7-32iGW6xrYeTNbgOPA0GApFfFnagf8wyOsjoEBUtbEQTVq5wV_qIBg8tiskmC8PIAm6WimRCyIWqvnpLFXesnuhisHlAgm5b4uim7CzMpdjI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6f33bcf78a.mp4?token=lrFm90E3aFKEqT_Oa86niPjKKGaOruAWrSkWY7srwaVlyXcUpETM88v3TiL_V0Eosd933wPPq_2odCDaGNDPJSgldoHi9-TVyk96PuRE_BJOeGWflZjX7DarcnUTO3mjoywujZl-RTQM-JPqTGMXblvqVgmnruD_OenhaKFIcFoN2tjhIh5o6WmXS7d3hVpJ_6l2d3TEtzwFKjBIcxpBeq8CB4el3JUb5LhqIXU8qz9bUSdFTRCF8fvnoXjBYjbZfmKmpG_4KZmR1ObL4YxFYp4cGsx5xYm5zR5PRO5HYMPwdgTU4SojfnppbmZg1_8D5tdi8Dbn3zvxn9dUH8Uz_nrKQYp8BXfzbBZZVmLFEf9vZ1SgUm9cK1IZgNcvESGZRJH8AvkZ2twhRfnK7U75f05qFAWbQrJXB2NVNYlggQyQVxOZEnYq9w1VmISW7R0mk0Rb0Osc-eDY0rUJSPguwvDGEQcqDLrRBrW1OU_fRS0csmk7JkdE8_8Y-qlPMYr0KMcirAg6D_2v30nZxJMjw_rf6uG6b6FgLJFxb0pgpTTdWERPjbeZFe5KglPtFy7-32iGW6xrYeTNbgOPA0GApFfFnagf8wyOsjoEBUtbEQTVq5wV_qIBg8tiskmC8PIAm6WimRCyIWqvnpLFXesnuhisHlAgm5b4uim7CzMpdjI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نکته عجیب در تست‌های اخیر کاربران از مدل Ox Alpha دیده شده که واقعاً سؤال‌برانگیز است.
همان پرامپت روز اول، بدون حتی یک کلمه تغییر، حالا خروجی بسیار دقیق‌تر و جزئی‌تری تولید می‌کند؛ مخصوصاً در مدل‌سازی سه‌بعدی موتور Raptor که اختلاف کیفیت با خروجی قبلی کاملاً محسوس است.
اما سؤال اصلی اینجاست:
اگر پرامپت همان است و آپدیت رسمی هم اعلام نشده، این جهش کیفیت دقیقاً از کجا آمده؟
آیا مدل در سکوت روی داده‌های جدید Fine-tune شده؟
آیا وزن‌های مدل یا پایپ‌لاین رندرینگ پشت صحنه تغییر کرده؟
یا Ox Alpha واقعاً نوعی یادگیری مداوم دارد؟
اگر این تغییرات بدون اطلاع‌رسانی رسمی در حال رخ دادن باشد، ما فقط با یک مدل بهتر طرف نیستیم؛ بلکه با مدلی مواجهیم که رفتار و توانایی‌هایش می‌تواند بدون انتشار نسخه جدید تغییر کند.
و این، از خودِ افزایش کیفیت جالب‌تر و البته نگران‌کننده‌تر است.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5045" target="_blank">📅 11:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5044">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">راجب یه پادکست جالب شنیدم در مورد یه تیم نرم‌افزار نروژی که 4 ماه کامل از کلاد استفاده کردن و بعدش کلا بیخیال شدن برگشتن روی روش سنتی خودشون
فردا خلاصه‌اش رو واستون می‌ذارم</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5044" target="_blank">📅 00:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5043">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نمیدونم واقعا چی بگم راجب اقتصاد
برق
...
می‌خواستم امشب استریم بذارم و بریم سراغ اخبار ai، برق رفت کلا تمرکز و انگیزه‌ام پودر شد.
کلا همیشه ترجیح میدم کمتر صحبت کنم راجب بدبختیامون چون همه جا میشنوید. و بیشتر تمرکز رو بذارم روی کار که کمی از این فضای حال به هم زن اقتصادی کشور دور بشیم...</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5043" target="_blank">📅 22:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5042">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ما الان داریم دقیقا مسیر ونزوئلا رو میریم.</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/5042" target="_blank">📅 20:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5041">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">راستی بچه‌ها پلن 5 دلاری OpenCode Go رو من با همین روش گرفتم. اگر که خواستید بگیرید میتونید به GLM 5.3 و اینها دسترسی داشته باشید به ارزش 60 دلار مجموعا: https://t.me/MatinSenPaii/4915</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5041" target="_blank">📅 19:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5040" target="_blank">📅 18:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5039" target="_blank">📅 18:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5038">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">☠️
آموزش OpenCode، رقیب رایگان Claude Code
☀️
⭐️
توی این ویدئو: 1- با همدیگه OpenCode رو نصب می‌کنیم(کاملا رایگانه امکاناتش و اوپن سورسه) 2- طرز استفاده ازش رو یاد میگیریم و بهتون میگم کجاها خوبه ازش استفاده کنید 3- یه چیز مسخره با میمو می‌نویسیم(توی ویدئوی…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5038" target="_blank">📅 18:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5037">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u7od4jcXe8EeOHGF7xkbmq7cJOa0i9T-zsEiLEIG4Ml90bhGbB5FOX_GAL66BeTgf5-ZfsfbF1TPYS_0ZUev0zKI49_HHBphW8X8vs37Dlzp3RQaIqjVwIr6oUD1JTVplVVXMpJo1D4mDTZDnDnyPwQO9PevBswic_XF7ffmQhdqdDlugEAzGC7cQedum7hkijpQfprCbGSNBZWRG2BYPXxkmQ7Rc0ogNIbAZe6ntePYs8z6ig5UdKb1GZm_FUcgD9CBvckp8404GtASU8hgYS3sc5gZZD5SH3Mrr0V2eZ8a9OU5bIa4v9TQZl7dJQ-ENfuzLjOYNUcj-x1xsWAaYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش OpenCode، رقیب رایگان Claude Code
☀️
⭐️
توی این ویدئو: 1- با همدیگه OpenCode رو نصب می‌کنیم(کاملا رایگانه امکاناتش و اوپن سورسه) 2- طرز استفاده ازش رو یاد میگیریم و بهتون میگم کجاها خوبه ازش استفاده کنید 3- یه چیز مسخره با میمو می‌نویسیم(توی ویدئوی…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5037" target="_blank">📅 18:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5036">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UqQXvK0OI_2ioRMRRgq0KG39Efy1m8PiqD88otMKqUkDDnGmVArtXted_yH9nAitY5G36eaPrQgyKVUEGLYrzZCkq9LAF5XIEFuGLcozIzefYkrz9yS0UQHMXnoz7r2CMQsVGRAdIvPbRg_IUCC3XEWSsbxORH5tMlwjclGTBUkYAXWnDeBp2dUGFDaOp6wErbAOef25-fuySZRzvWzdNwJJ6g2uv7TLl3m86GXh3B6rKy6KvgK0Evy6sj69M0rsDHDS_MikD-GZwlboSThgUJcyHcC2qJtfVqYg7DLhJA8qrL4qoQzXw_L4ca7_emhAfVo_zRbrP6Eix9lS6kIrMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش OpenCode، رقیب رایگان Claude Code
☀️
⭐️
توی این ویدئو:
1- با همدیگه OpenCode رو نصب می‌کنیم(کاملا رایگانه امکاناتش و اوپن سورسه)
2- طرز استفاده ازش رو یاد میگیریم و بهتون میگم کجاها خوبه ازش استفاده کنید
3- یه چیز مسخره با میمو می‌نویسیم(توی ویدئوی بعدی که پشت این میاد فردا، قراره حسابی ارتقاش بدیم)
4- آخر ویدئو هم توی ثانیه‌های آخر یه چیز جادویی هست. اولین نفر برید ببینیدش
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به هیچ دانش شبکه یا کامپیوتری نداره
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5036" target="_blank">📅 17:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5035">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تموم نشو x alpha
💔</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5035" target="_blank">📅 17:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5034">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تموم نشو x alpha
💔</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5034" target="_blank">📅 17:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5033">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">آموزش مدل‌های AI روی کتاب‌های کپی‌رایت‌دار؛ قانونی یا نه؟
خبر:
اکثر نویسنده‌ها بدون اطلاع و رضایت خودشون عملاً توی ساخت همین ابزارهایی که شغلشون رو تهدید می‌کنه سهیم شدن. TechCrunch یه تحلیل مفصل نوشته که چرا قضیه از نظر حقوقی خیلی پیچیده‌تر از یه «دزدی!» ساده‌ست و Fair Use وسط این ماجراجویی نقش تعیین‌کننده‌ای داره
🔗
https://techcrunch.com/2026/08/23/is-it-legal-to-train-ai-models-on-copyrighted-books-its-complicated/
نظر من اینه که حتی کاری هم از دستشون بر بیاد که انجام بدن، دیگه به چه درد میخوره
😂
مثلا فکر کردن OpenAI یا علی‌بابا با Qwen که خودش دزدی و دیستیلیشن از کلاد هست(
🤣
) و... تره خورد می‌کنن واسشون؟ =)) یا مثلا میان بگن آقا بیا این قسمت از کتاب شما رو قیچی کردیم از LLM چند تریلیون پارامتریمون؟</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5033" target="_blank">📅 02:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5032">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">خب انگار قسمت نبود
👍</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5032" target="_blank">📅 01:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5031">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یه ویدئو داریم واسه Open Code
داخلش یه پلنر ساده می‌نویسیم با Mimo
توی ویدئوی بعدی که پشت سرش میاد، میدم به X Alpha و اصلا یه چیز عجیب غریبی زد.
موندم که واقعا این مدل مال کیه</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5031" target="_blank">📅 23:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5030">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5030" target="_blank">📅 20:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5029">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دلار 200 رو هم رد کرد
ولی نکته‌ی دردناک اینجاست که هرچی جنس می‌خریدیم تا الان با دلار بالای 200 بوده قیمتش
الان قراره حتی بدتر هم بشه</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5029" target="_blank">📅 20:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5028">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QfuNcolp1C3X5sNpwB_Ijhm_poClSRu-NncVEcRI5nsRukpbVyiALYk6JU8iybBVCjylpny9bUQeMEaPdl2g_bxGri1sZsPDn-6nVeaO5RuVvfdUxxiqz31QnRo9PrxHTxi2VYSB7X0RAaXV9-qzCSGEUs-4MMuv-csURTVKK3qR8usCfmbwrrbdrJiTuouGzlJP2NL4V9WGfwDYG8Rc2-xRQm83X9vIbvF-LB2JjGCQAl72pAlZB3P5ep9vTLxu5J58fLeaR3-C8jbNxvBAdKuQcpXS9Vy176f3BoTHSo6IUWremNbKkdKVc80lDtevNjFf0fZwc5AekvnALHsFtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسیدم ۲۰۰۰
تا الان ۳۰۰ هزارتا امتیاز
دو برابر بشه میفتیم زیر ۱۰۰۰
❤️</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5028" target="_blank">📅 19:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5026">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Vb1A093T6F-O34fhpyNqSDQLGFYENtFxlNNuwcKleZv3iuBfDCG1NPTyfpuUl0Vtb69dIO3RnbjVv8gLo4uBCCM8ZubFs5PWL3dSyEu3d6pG4rOrakT98qd_nlpMjcA57MnE1EVtSQgXZ15CAMKde1dt4wtls1BBSQPqIiJsBLptL9Zp-XucZOQvd7gAPf_Id759AZFSV3j7GewZjJmb6BWjPwmId1741IurHuaDrM0KOqzK4ZYzR3Uu3bvhBTnM9M8pR-VGUomJLa6_4FVh2pcacXmtmWMFkQ5CEB6O1G46m4E2b1wwEXerwSbFyJqMSQJgASCJ9t6G1g6CeGV-iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RRDESeJbmkmhgaFzRPqjAXLD1WONuUlQ8fVljQ0cXQnp018w5hzTlprxgzwG0bzcuBpI7N2xeZkqmiuLJyrwOdR7RFBmq4UjR3SEeTGWkKVlLHFUlqPfofDa138ssVdQcVDQtaim5OvQyZe0rD6pQHdOKy0LlhxBuj_qSFdejcxjVgl7WV2oasdKbmGwRkc7CHkCvH2ISc6ePr8W8DKpCsINipEoRDFjpblD0IKUvzHHM1HOszmVf0ZaalIWHAxuHAE0gdk9UbXSBLE-K2UZeGS7Wz1CG05dyOQMxdU-RA8nj5wwu4UYbp3GgKIZL9VpWLhmTSeukE8HdN2Vam-zQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه چیزی دیدم تازگی ترند شده توی توییتر، یاد همستر افتادم
😂
😭
گویا اسمش ووچ(VOUCH) هست و طبق گفته‌ی دوستان کریپتویی، یه کمپین پولساز هستش و فقط هم یه روز ازش مونده.
اگر که تونستم جزو 1000 نفر اول بشم و جایزه‌اش رو بگیرم، یه اشتراک Claude Max میگیریم و روی استریم میریم میفتیم به جون ایده‌هایی که می‌دید. بازی سه بعدی چرت و پرت هم می‌سازیم
😂
فکر می‌کنم نهایتا 5-6 دقیقه زمان ببره انجام دادن این کارها واسه‌تون اما اگر که انجام دادید، هم به من ووچ میده هم به شما:
الف- برید توی سایت
commonsmade.com/vouch
و روی Claim With X بزنید
ب- جوین که شدید بعدش روی پروفایلتون رو بزنید. اینجا باید دوتا کار بکنید:
1- گیتهابتون رو وصل کنید
( گیتهاب ندارید هم راحت بزنید Continue with google )
2- مجددا توی همون بخش پروفایل، یه جای کد تخفیف داره به اسم gift code. کلیک میکنید روش و کد "love" رو میزنید، باعث میشه ضریب 2 بده بهتون.
بعدش بالا، سمت راست صفحه براتون 7 تا قلب ووچ میاد و میتونید به دیگران به شکل زیر ووچ بدید توی توییتر:
Hey @commonsmade, vouch @MatinSenPai
زیر این توییت من می‌تونید همین جمله بالا رو بنویسید:
https://x.com/MatinSenPai/status/2091522197537919325</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5026" target="_blank">📅 17:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5025">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uiTYbnprhEkcjbD21jEPO6pwatuKBFsdyYoc9QjQojwoM5ZFw9dgnOlSiZkpCAtxuLxVlnTPkZYSypk8VSE8Fl2bBuQGZ6MKwEmhgTlM3eOb5_B2hWrjT7eO8KHgxhpI4iWflDqAPP0T6rANnTYrHGt9bokOYPzRworOZ_jVS3Qubu2ONKpRMZOXPvU_ZsXitNrlt8lnC9CkW0NXeU0LqklIsAMbNsfSZzeN9Wypv-PG8Lql2EwLFFEZ5TAOxamTb9NJFAq5lSdms4oFvcyc-XLV519TIiAHYj0GJmHgg8_CWxtzYV3dC8enULbDPJKcyJ88BzSZM-dJx8oqhpSVyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خدا چند ساعت خوابیدما دلار کی شد ۱۹۷</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5025" target="_blank">📅 16:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5024">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1357719d90.webm?token=P6_C_mijj_ah5Vaw1GeZ7bHWTNvP7bA0D4lMXYI3fWHWHrOI9dLwnoRZMQL1N2U3kYWlBdPFIMXlcrFu5Uoq0PPYytunioY37kB4JIE01Ae3xy-UYQrPfr0xjPlijBnjtg2wUX6mAXk32g3xZOMRgAJ7Jk2aV1gCkf7TtzzLrrgPPJRx3-Eqdzvw0-zR_4vfoC0sIgAKasCX4Nn38-jVyEO31-2VxodJJLFupQc-5-RFm5OY6aip_XfXngkClKkzHx6a8pS5ZZdF1r1puHSSuqQOkfOHoSvs5RtM-D4EQ8ybpJK6kRinjshGclbyUjWijuEHMNiO-wMRC_fBZ7CGRg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1357719d90.webm?token=P6_C_mijj_ah5Vaw1GeZ7bHWTNvP7bA0D4lMXYI3fWHWHrOI9dLwnoRZMQL1N2U3kYWlBdPFIMXlcrFu5Uoq0PPYytunioY37kB4JIE01Ae3xy-UYQrPfr0xjPlijBnjtg2wUX6mAXk32g3xZOMRgAJ7Jk2aV1gCkf7TtzzLrrgPPJRx3-Eqdzvw0-zR_4vfoC0sIgAKasCX4Nn38-jVyEO31-2VxodJJLFupQc-5-RFm5OY6aip_XfXngkClKkzHx6a8pS5ZZdF1r1puHSSuqQOkfOHoSvs5RtM-D4EQ8ybpJK6kRinjshGclbyUjWijuEHMNiO-wMRC_fBZ7CGRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5024" target="_blank">📅 16:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5023">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">به خدا چند ساعت خوابیدما
دلار کی شد ۱۹۷</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5023" target="_blank">📅 16:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5022">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حدودا 20 روز هست که دارم با ابزارهای مختلف و AIهای مختلف کار می‌کنم و خودم رو آپدیت می‌کنم و چیزهای جدید یاد می‌گیرم، و ویدئوی جدیدی ندادم در مورد AIها تا هم دانشم بیشتر بشه هم محتوا باکیفیت‌تر. اما طی روزهای آینده، کلی ویدئوی جدید راجب تجربیات این بیست روزم می‌سازم و می‌ذارم توی کانال.
(آرک سولو لولینگ مخفی به پایان رسید
✨
)</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5022" target="_blank">📅 06:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5020">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KbOW_qkNeGihJ2PzyHTOWDPNBUb_xjRQ-slltb4iGFY6rkMTv7vmfRmauiXy22-dlTQszzEkF_wENaGgzW-obzVCw63MXZLyGusUR3g7_n30sBW1alCVBafSPhcqaT_uGZqRjTvNoCG2ihVyXuGct55X7bddswjLCz8En1cnrtzoEY6DD8s7jp---k8qjmjriVer-Hbr0F9f7QGxunVp1o89ekyR1msXQulVBkUhMpLxtc9EtbD02top2WRa1K_1ez8FjNi9V65JZdjih9fAS_Y9ktKLziYlqt4JTldn7ke3HyIM4z3IlERoZ4LW8063hFCl2KnaNY21QUB8j9hAeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/usjQCienVULqIh9ABS6qUZ5OXtCC7SWz0B5jXBOma7BEF5QrhYGCPbgkkJD3Y5rTDZlyDuC5uIqe7ogNA0ILcoHJG_kACB7e2zBoeIl-DYFNXwOtiXxRqZVJzpQ51tOuXFDTQQmB1mVtI2lLhX-ONaF3X787O62cW_TRkNqyO8QKp_5zaWA7zK3bpsA_-GhjX4tstWaBURLRVihzIVL9_DeJtfV7YJn7HKYfHzb4CeWzzVsyUpkMlGKfgQJ9UPF3Ol5sW3GeBIu_085VxsBTKpNlGgqYw9aGcl-Z6S9uQRdK9rT946-dQrt6FcSO6nInV9-9YeKZJAY46d70-bu2sw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خیلی خوشحال شدم امشب از پیام‌های محبت‌آمیزتون و از اینکه آموزش‌ها چقدر کاربردی بوده واستون
❤️</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/5020" target="_blank">📅 05:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5019">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iNzKipatJd3G1BSLSUC5QuNo-3Av00Eb1gnopoFB3skNAy65c0hiO9law-FolSOVsM0vvotLMc4zFnSUkDZhp8feFjJL_hQ3871RhvDHdBORmDX5_gdtraA94UJyxUPAbfN3zMxQobHxdvGlZMgtUPQs5qNPhcvk4LHPN_DfpmtQ93pdq407INL9aNFjltIpH0gADPJId86MpW3wP-8uwa-Kmvz2TWUW42IORlanrl5kcb7c3ONVeXcrTkIqeVUYDWovIt5equxauPv_-3mwZn8QnjK3wcZcOFas7VwU1EdiC_3s3uNAQBThgNjasXdfhe_PANzxQ9W8az15HDaQzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم یا مدل جدید شیائومی Mimo هست یا به قول یکی از بچه‌های توییتر مدل جدید خود Google(جمنای ۳.۵ پرو). گوگل هم ماشالا ید طولایی داره توی این ناشناس مدل ریلیز کردنه
😂
خواهیم دید چه خواهد شد اما تا الان خیلی خفن بوده</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/5019" target="_blank">📅 17:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5018">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خیلی توی کامیونیتی خارجی بحث و جدل شده سر اینکه حدس بزنن این مدل جدیده مال کدوم شرکته، چینیه یا آمریکایی و OpenCode هم اعلام کرده که دسترسی بهش نامحدود هستش تا هفته‌ی آینده و روزی 100 تریلیون توکن تمام کاربرا می‌تونن استفاده کنن مجموعا و ظرفیتشو دارن
😂
همینطور…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5018" target="_blank">📅 16:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5017">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خب من این آفر سه ماهه رایگان اسپاتیفای رو تونستم بگیرم با همین روشی که اینجا یاد دادم  مزیت بسیار بسیار بزرگی که داره اینه که میشه به گوگل پلی وصلش کرد و عملا توی هـــر بازی‌ای خرید کرد. البته من با VPN آمریکا chain شده رفتم که ساخت این رو هم یاد میدم بهتون…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/5017" target="_blank">📅 08:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5015">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i5eCZeyYKJasa5KzDgP5jJ-Xe8wwNXcM1yio3uNiBB8wN-z-1Rf0Cy1AoXtt_vDaKpzquM3m1fACgA7QxloTp2kjyGUwTdgd5AQirCHWUNOp7ZHvYciTxtW8QY7QDc9Qucn7ZaE2A2XJV7R9Fz5U1zK_myWPLt6zegA7kdqNmt22sz8yAoqwhjzCysBtVweEsmpVSEfKJEBVic8P4G6mxN7qHd0cTLvlI-k19-c9nLHLf8fB63Y1KE0v1Vf5mCQgJKjZnPl8In1qNqj-sixujFJ9K9jBZDxOn0sQ5LqQIPlePhKGaecdOj7zpLL8FgwnIRmzVarxvt1hZXds0A1EVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/R_s1w0kUFALVIZBxdWolceHdNy1IIdHvzHT4Qfd15K7WjwRIbU5URuxalCmhu9kJWc1xEHx-pyBTUu8Bux7GrY836UOwlj8DdwPhs9gJiPUFPRZsU5YgHjsnuKQ-71rh7lGwaf6RysibKygZ94ySlZUc_Ro6l1ggkN-EUIP452evjp-IwCYGaxNOzXV_vfSHcH43hTgBsBx1tL85CZh60tiJebbpEMFj2yXpleEpLXdqtE5mPmgeNHuyqSpbKZCYnAGj90C5CqFPtyLRzbt3qo8B5fx1RH5yS4qzbVym44j6j6kNxbHlWtg1zkDYJ4h2qAO_ktRpOKFapzEVy5Nvxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب من این آفر سه ماهه رایگان اسپاتیفای رو تونستم بگیرم
با همین روشی که اینجا یاد دادم
مزیت بسیار بسیار بزرگی که داره اینه که میشه به گوگل پلی وصلش کرد و عملا توی هـــر بازی‌ای خرید کرد. البته من با VPN آمریکا chain شده رفتم که ساخت این رو هم یاد میدم بهتون
تا الان اینها رو تونستم بگیرم باهاش:
1- اشتراک ChatGPT(بیست دلاری)
2- توی کلش رویال کلی آفر گرفتم(رایگان)
3- توییتر پریمیوم(فکر کنم ۹ دلار ماهانه بودش)
4- پلن رایگان Hermes Nous Research
5- همه‌ی پرداخت‌های گوگل پلی(با آیپی آمریکا زدم. و یه سری آفرها رایگان)
6- اشتراک OpenCode Go(5 دلار)
7- آفر سه ماهه رایگان اسپاتیفای پریمیوم(با گوگل پلی. هزینه یه ماه بعدش رو هم کم کرد یعنی ماهی ۳ دلار. حواستون باشه)
و در کل اکثر جاها میشد خرید کرد، تنها چیزی که نشد بگیرم آفر رایگان GPT بود که انگار واسه‌ی خیلیا خارج از کشور هم قبول نمیکنه کلا.
و مجددا همینجا آموزشش و مابقی مزایا و معایبش رو گفتم:
https://t.me/MatinSenPaii/4917</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/5015" target="_blank">📅 08:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5014">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nH5NoP7TyvLrsgcp_E_1eJkMe83Czx9jz1bqxRw9996hv9ywFSi4bjQVHlXQMrJYHl5ouCJ29qn2oppN9ybPHCPN6hKbimh4_eqrOvQi_cBji-71qT-HCrxAhhW0VjHPnb59ImhbXTPK1OPppshIxNE6ehfiabHbC0SCiQ0yPgzrWwR4K5QvAou9MEWbi52C_K8myt-OnLJdxhcEZZRv29yJvECwSykwso9wHGO0X5wPex5KeFdK-YF6ozItTPkffz7SHe6SS5oA_NAanIVkBwAxhpugcowUsRx_OYoOWOQtADgCEdvUwPK0e2Dv8YwEPx-e7Po9KvRoJLXuIXaKQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل جدید و مرموز x alpha که روی اوپن کد اومده به تازگی رو می‌تونید این شکلی تست کنید روی 9router: https://x.com/MatinSenPai/status/2090856359117902053</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5014" target="_blank">📅 08:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5013">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فکر کنم وقتشه کم کم یه لیست از چیز میزای رایگان و آفر و... هایی که با این سایت تونستم بگیرم بذارم</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5013" target="_blank">📅 07:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5012">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sdIUUnaniPOF_jRreU36MZRRRwPlR8QHGS1N0ubtjonPnzbz5sX1I_0cPu4uLFy_SnxOqI4jVn05gBj3i8DOKdIag3FVQvQUOyEGfw2aEnzN_DtIV4ayP8WISk67qN7_aS30sDOmlkC-QLErlkDJXoBtytix6KlVAr6qiUZabh3IJtRW0jxFQIdQRdzJXsjAXBCtO4SrXTcfKyh4GVXK_sTxk93iKL00La_wIxW8DKVEuCZY2xq1dAkD2B3-uODxNmMjzs_QdJMoE-KGdqTFadEpgvnlLrdH7CG7fkd6s3BM2Nw4q74rVt7LPZpxsYzMPUS_4cqiRncv5cIyCsi9iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سریا هم یه جوری شبیه دی‌کاپریو میگن «اوه این پروژه وایب‌کد شده» انگار مچ معلم مدرسه‌شون رو وقتی دستش توی دماغش بوده گرفتن.
همونقد معصومانه و مهدکودکی</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5012" target="_blank">📅 07:39 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5011">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مدل جدید و مرموز x alpha که روی اوپن کد اومده به تازگی رو می‌تونید این شکلی تست کنید روی 9router:
https://x.com/MatinSenPai/status/2090856359117902053</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5011" target="_blank">📅 23:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5010">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/qplbmQS3k4YxH5w61RbQD5HvGEb-xkjo9M0PPRqUaNM2LQb7CYRNmvFMiE1h0ODC6caXC6F8K3U_eGFdbK3fOZNnGhSLd1x7NQdyp3O5p3sj3wTy9zyap4yUAQu1QTQoq5G-8_xJKDyStOuZcdqN7-Z3yvGuuumsJeaJtHLTQ_9E75G_quWj4o6UyRylDCXUu9avOYRQsELl0KyUBTZCqelBHMYQ8fS3y1Ih833A2sofNyEBlaOspTil373HvOIzk8cYgw1vKvcbqpGyqygCeY_v4nu38jOR_8tr6ueUy3jjKd_tABSx_CVsFBUslQah6Xih1xv4cqSnh9lF5MEofA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔗
WhiteAesther Android ورژن جدید
🔥
🔥
🔥
🔥
🔥
نسخه ۱.۲.۱ — رفع سه مشکل اتصال
این نسخه قابلیت بزرگ جدیدی نداره؛ سه تا مشکل رو رفع می‌کنه که باعث می‌شد اپ روی خیلی از گوشی‌ها اصلاً وصل نشه. اگه ۱.۲.۰ داری حتماً آپدیت کن.
🛠
چی رفع شد
1
.پروتکل های wireguard و warp in warp برای خیلی از دوستان اصلاً وصل نمی‌شدن
توی ۱.۲.۰ «ثبت‌نام مشترک بین پروتکل‌ها» رو به‌عنوان یک بهبود اعلام کردیم. اون کار اشتباه بود: وقتی MASQUE هویت رو ثبت می‌کرد، کلید WireGuard روی سرور Cloudflare پاک می‌شد. بعدش هیچ اندپوینتی جواب نمی‌داد و اپ می‌گفت شبکه بسته‌ست — در حالی که مشکل از هویت بود، نه از شبکه.
حالا هر پروتکل هویت خودش رو داره. اگه از ۱.۲.۰ آپدیت کنی حسابت از دست نمی‌ره.
⚠️
در عوض، اون کاهش سه‌برابری احتمال rate limit هم برگشت. اگه زیاد نصب و حذف می‌کنی، حتماً از
Settings ← Identity & access
یک بار بکاپ هویت بگیر.
۲
. عوض کردن پروتکل وسط اتصال، همه‌چیز رو خراب می‌کرد
اگه بدون قطع کردن اتصال پروتکل رو عوض می‌کردی، جستجوی اندپوینت از داخل همون تونل قبلی رد می‌شد — یعنی هزاران درخواست دقیقاً به جایی می‌رفت که قرار بود جایگزینش کنه. نتیجه: هیچی وصل نمی‌شد.
۳
. گیر کردن روی پروتکلی که شبکه‌ات بسته
پیش‌فرض قبلی H3 بود که روی UDP کار می‌کنه. اگه شبکه UDP رو بسته بود تلاش اول شکست می‌خورد و اپ دوباره همون رو امتحان می‌کرد. تا نوبت MASQUE H2 برسه چهار دقیقه و نیم گذشته بود، و عملاً هیچ‌کس این‌قدر صبر نمی‌کنه.
✨
چی جدیده
حالت Automatic — از
Routes ← Manual ← Protocol
گزینه اول حالا Automatic هست و پیش‌فرض هم شده. خودش سریع امتحان می‌کنه ببینه شبکه‌ات چی رو اجازه می‌ده، از H2 شروع می‌کنه (چون TCP روی پورت ۴۴۳ هست و شبیه HTTPS معمولی دیده می‌شه)، و هرچی جواب داد رو یادش می‌مونه تا دفعه بعد از همون شروع کنه.
روی نصب تازه: ۱۴ ثانیه تا اتصال، جایی که قبلاً چند دقیقه طول می‌کشید.
گزارش خطای واقعی — قبلاً اگه جستجو نتیجه نمی‌داد فقط می‌نوشت «اندپوینتی پیدا نشد». حالا می‌گه چرا: بسته‌ها از گوشی خارج شدن و جوابی نیومد (مشکل از شبکه‌ست)، یا اصلاً خارج نشدن (مشکل از مسیریابی خود گوشیه). لاگ خود موتور تونل هم از این نسخه داخل
Settings ← Diagnostics
هست — اگه مشکلی خوردی همون گزارش رو بفرست.
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5010" target="_blank">📅 21:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5008">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vH-1Ka-WvqeIGlZA3J3IRWj_s6ocEsmp0SVfgMkH_JCL_VlSMDirsRIhR-qAVVrOIDDmDmxcmwxI2lVcbwHqVr4-c5X7o6j5t9nyc_HiwDdnkVRvV6ZhAvYTkbJ_LSAen1OaFeWruEO5fueDPYmydmE3ArW_4Nx9rwoPmb04YOOVuhjsYsn9HdHibOK_gp6c7Pi2I0a12Voyyv7GCAFxn-xdjkMc1kQFA_GEw5rq66QN9hv90_tMypIcq5q4WuhBpXvOzq80OFfpY_oyk4bCwTZ-3j7630uU3Lp9jDYpeb2KBxuh8p8EUK7CSSIQ4q9sBT_CwR_iwpyEuv8GtbuLCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IDk19QkY22D5AopqjgOOJziTliPoIUgRYMo4pAo_qgE33Uj3bEVoJu20r7LcCdW72p3JFd-Rbaw1wnPWOvsfSHDuitmavBhr57ChEE8IPnzeUkn-CCv2x5dXCyL6mgdA5TlcVmjELCA0U2dl9PNAGCS8wQI2i113cMgbZeByu6aciIYy9pJrKGQ1a4dSAIuFOzKNCY5C3bdjqedQq5J3cv6wzMpkgtfq-rKJQB60_qZOSC4KQ052GWjsZg1UhCjsT8BdF05DFud62dkiKoOIAeV5MfG8-Ow8ZhoTC2lPvH-Kqptp_1PpOKzuVUmvyNC37zuyK5u2CsTtzllEyaupiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  چند تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5008" target="_blank">📅 15:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5007">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد
PattNG
کرده و لذت ببرید !
https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt
ساب هر ۲۴ ساعت آپدیت میشود.
///
توضیحات:
چند تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری و تست میکنند و سپس کانفیگهای سالم را فیلتر و در اختیار قرار میدهند پروژه‌ها‌ی
https://github.com/0xRadikal/Free-v2ray-Configs
و
https://github.com/itsyebekhe/PSG
و
https://github.com/Delta-Kronecker/V2ray-Config
هستند.
اما این پروژه‌ها دو مشکل اساسی دارند، اول اینکه تست کانفیگها باید از طریق اینترنت و فایروال ایران انجام شود ولی در حال حاضر تست کانفیگها در این پروژه‌ها از طریق گیتهاب انجام میشود، دوم اینکه روی نت‌های آپلود محدود (ایرانسل و ...) عملا اکثر کانفیگهای این پروژه‌ها آپلود محدود هستند و کیفیت بسیار پایینی دارند.
از آنجا که با روشهای زیادی میتوان محدودیت آپلود را روی کلودفلر دور زد، من در پروژه‌ی خودم اومدم کانفیگهای کلودفلر سالم را از پروژه‌ها‌ی اصلی جدا کردم و تغییراتی را برای دور زدن محدودیت آپلود (و همچنین دور زدن فیلتر دامنه) اعمال کردم (در حال حاضر متد fragment+fingerprint اعمال شده). بنابراین کانفیگهای نهایی سالم و با حداکثر سرعت در تمامی نتها قابل استفاده هستند.
برای دور زدن محدودیت آپلود در نتهای آپلود محدود در حال حاضر فقط باید از کلاینت
PattNG
استفاده کنید، بزودی در سایر کلاینتها نیز این مورد پشتیبانی میشود.
https://github.com/patterniha/Free-Configs</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/5007" target="_blank">📅 15:09 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5006">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NDd1WfTcnj31Ku1SOfNNCFWwrjpwKDh8VEmeWt0PcZqSIlw7xOfXKaRgtVjMshMpRQZz2gV9douDS2CJLbMPOfJp240WEZuzLHMremIv84tCco7wcVisJ1ZIHZTfNU3nzBWEdBYxDvDzPknfTPSDFamxUhLSGa7cfg1HIaLbff-TMW623wA9zp53TGHzR7DY8u-UrtOm-O7Rc7gd6JMpd7Di8LcqcnVxl0mIUPN67_vf4KjMRKxvhKPoxUi3OQ9k-YV3pkYWY61rz8lrPQj537J3lao-I_zJSEwoY0FkR7D1H_IID__n_cY98L6CEIZi8RwnQ5j43wimiKMe4q4m2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه مقایسه‌ای دارم انجام میدم</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/5006" target="_blank">📅 03:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5005">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">آقا این Muse Spark هم عجب چیزیه:) روی هارنس درست به نظرم شاهکار میکنه. فعلا روی OpenCode به شدت سریع و اوکیه</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/5005" target="_blank">📅 03:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5004">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بیاید بریم Rust یاد بگیریم لایو هستیم روی
🟩
: https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/5004" target="_blank">📅 21:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5003">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بچه ها بازی Rust نه. زبان Rust:))</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/MatinSenPaii/5003" target="_blank">📅 19:11 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5002">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بیاید بریم Rust یاد بگیریم
لایو هستیم روی
🟩
:
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/MatinSenPaii/5002" target="_blank">📅 19:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5001">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">آپدیت جدید Aether:
توی این آپدیت روی مسیریابی (روتینگ) و اتصال از پشت پروکسی کار شده</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/MatinSenPaii/5001" target="_blank">📅 03:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4999">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">هوش مصنوعی و برنامه نویسی | آینده این شغل
لایو هستیم روی کیک:
🟩
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/4999" target="_blank">📅 21:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4998">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">حس می‌کنم شدم هوش طبیعی متین سنپای که پول توکنش رو نمیده
😂</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/4998" target="_blank">📅 20:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4997">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بچه‌ها شرمنده می‌کنید با استار هایی که میزنید. ممنونم
❤️</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/4997" target="_blank">📅 20:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4996">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/co_Ym0AtaTLVkgyjEU8K86EHAvX88fKtrNBH9lE9ditwUHajWHlE6e9A5lFr_Ce3sQ9BXyHTF-X1XHMYW9rFg81v2mu-Oeuq7N98UwY81uikEzdIQkeoTYEoVZMVrJiv21prIy9ieT6XDxwKBlk4J5pMWdI6zr1itcM524L58wcPb9IP3AnluGbLKj0vKbiP11RJFmP8jHW0Nn6PFseCYHMdJm4Lx9iAU1FVoeuLHyETe6yFKx6v-t0TmIxbB7mRstQ3KkIUGPHA_HJYSLbpXia5z4gSStEhmID5XigIbygvC_eyJhr2R_8WscwGUZztj0H78cBGg_QvPb8YQULxaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نصب هرمس وب یوآی با یک کلیک
متین سنپای
بهم گفت که Hermes WebUi نصبش سخته و بهتره با یک کلیک بشه نصبش کرد برای همین روی پروژه اصلی PR زدم که اگر تایید بشه از این به بعد میتونید راحت این پنل رو نصب کنید و ازش استفاده کنید.
لینک PR:
https://github.com/nesquena/hermes-webui/pull/7152
میتونید روش ری اکت بدید شاید تاثیری داشته باشه.
اگر هم تایید نکردن مهم نیست
یک پروژه جدید روی گیت هاب خودم اوردم بالا
لینک پروژه:
https://github.com/nesquena/hermes-webui
میتونید به هرمس بدید و بگید براتون نصبش کنه
خیلی ساده همون پروژه اصلی رو میاد براتون نصب میکنه
حس می‌کنم شدم هوش طبیعی متین سنپای که پول توکنش رو نمیده
😂</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/MatinSenPaii/4996" target="_blank">📅 20:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4994">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/USyGW52VN7kLN32LUxHSogIRC1_-EM7Oz3MKBMMJjIVj5yPNjN0AMB5ojkKMwzQpL_9eyq_SggXcP3n0GubhMu0V8WVD6rx4oqG4Wa8GMAVl0zb7FZuQccmMFso5Drsasocn7K2hTU_XnsMQAm4_lqjXFLAE9iz6xi5stHIACFTSWKQBLNAQVh_q25DMZHjE0tCfBI9vKAxKFQB8ckVUuZozvpBrLxP1-2AtXnPnIXBPZRlrLu6mNdvzKNZzXBPUyicKqIHXzsjjD7vCVBlipCHufQx_3I6OOeupad3NLMtCmNrOlT0wmnkUuGiq3hQCGu-4b6mOhgkHzpGH0HyIOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gX9WeoxEfipRma2XdZRcz43D48Rm-ltub0c3T-UOZePqHGQZqhGWAyRTIbZGwrDqlAsQIvH1fKDfC_dpv76sEDJOeohblQLaJYjD_8YXZbjAsiaGV22UXdFTxSiEYOt0pwLJR1oM2_yIqjclePVMDIzTegl9MoWndeOHdV5dany2qyKPjy1rkFQYDx_N5z_AVD7kh0nE9B-q0Xxh1NSLEB9nXZOdQP_z9sNXNJo4Ch547_JtfT9gmX20UKJ-xZJhPco556XG3yxVbbeOkFIPTKe2DxDuyL8--wjaupmmYOYXsCCqpcWv---pu5GFbYSXySREQNSnlXQCta2YtBLrqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4994" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4993">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qQQrpWNOz3r20z-Fvx6AORIGsKYja_56IU5z1EO6ePbJKFfTTpYvHhSXdxf6G9PF6zJzEdxYN5RFfCEAiXjVr4_nFJlJdKku9OhivPygaDNHRMcrSFMei0Fisdo-q8OgSbNpW-hcJ26IXBYJYdWAch1C8-bNaUHRoTwX_W5RNhEchPNSNEZi5s6f7B0ZYVugrJKQS6o7Vt0p4Cw_zXq2L7uQ4SRZR2zRoPuTKsqlZzC27_j-at2jxG2zMHfVGpqKk_TnKRr8yQ2bnVdURsQzfVrvWjV08q8ecfIfmGnNogitA1W4NUyKw2KAZxFqHqEpN_2jxUcoaNdzI99YUsy4rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرویس استریم شخصی هم نوشتم واسه خودم که با نت داخلی بیام روی Kick
(تانل rathole
😂
)
هاهاها
به من خندیدین؟
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/4993" target="_blank">📅 08:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4992">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q2Daz_HGWzDkhky8rc203nMgc4TmNcoBpj80H3vUbTD1mrOUrIcppY4KXoq2vZ3h-BiMhusOVYBjIlCS7PJ-R6w44bHszwIn6oDthRyloK_Wu1c8wAJ6V4YdRMGPC0den_gngAVjVwOfmCIMAnM7V-ZAaW6aRy9opgrknYXCAJvk9Evl0kbl3WCTQYkxFmg1xbdODMZIdb6vlKtro2tOFQi_OvGZQkLWwMU9Zyd-sbEkoJRBnvKvThltfDWZ-Ucak-LW6NwzF1l4x9RAN5rdMyxQul67ihmmDdP3dSN3WkdI24Ye7YnXuzCBxsPBk2cZuS_7lJTt50nmntt0gHwMNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجربه من از 5 روز کار با OpenCode Go
https://x.com/MatinSenPai/status/2089928470801318139?s=20</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/4992" target="_blank">📅 07:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4991">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T50GPsoAA7I3LVBEKHJXeaar75y0o1597etAWvJsECVDyUbZhW2le_6-VMv7fNbfafPuHmN7UIPTMq_jogj_IXnM4q9T5CzHlkPqZ2YgdNStboEPOwB7IaEn_tmqvgcG1_XUeKNP7rd1WJeH34CoWBRAry8YY0M-4ZK6JGXEg91msg2KObVfteRWisoGbRoF3Kuy-3yXmTY3qfLUMI6JxXHHX18RY7nib6JvHo7Z-ui4IAvyNZfpmUwLboOcBLNr3VrjvmGVG7f_Qp2-BkOHdqr2Q__eJrwQ4nLU4CjyC1smlOc-S4GcIJprjd9xVOtUbZq2Y5KJ7L8H1B_QK9Dviw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب پنل BPB + متد پترنیها + Chain Proxy داره بهم سرعت آپلود خوبی روی آیپی ثابت میده</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/4991" target="_blank">📅 23:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4990">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">لینک داشبورد کلودفلر:
dash.cloudflare.com
لینک ویزارد تحت وب BPB جهت راه‌اندازی:
https://wizard.bpb-panel.workers.dev/</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/MatinSenPaii/4990" target="_blank">📅 20:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4989">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mbjS3__iqcRdqAo_rWGc9NvweW9B0sC1ihKGYVPaYATrUk6R84vqdndwPaEQ1wcNLHD_SjW6Y0ENJdUyMkNZD5B_0hPYSKoOYDRJt_BMi8o7KsQxNrxAKXF-MDD5p16WLJeVEUWKJEgKYpDB0QjGKAOnDCsMWwrs20WF9dtvTD_c_TdTcBmdWK1IjG7ib1mhCjWae-6Qi7uoNXscNHI5maPI-3gYRcJxTc5ZQ6VpSZdugEGMD6jIFbZbqNbpg4BahacW5fxAQuMVC024zN9_acWYCB-1odtrnDpZ9aLFdMBwUhZz7PJ2UQFXrUKJYK-oRZsmDBiLR8nXuyscl4xhNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت VPN رایگان بدون سرور با پنل BPB! ورژن 5
🌊
⚡️
لینک‌های استفاده شده توی ویدئو:
https://t.me/MatinSenPaii/4990
⭐️
توی این ویدئو بهتون یاد میدم که:
1- چطوری با پنل BPB برای خودتون VPN رایگان بسازید
2- روی گوشی و سیستم چطوری ستاپش کنید
3- و برای خودتون و خانوادتون، از یه VPN امن استفاده کنید
ویدئوی آموزش تنظیمات:
https://youtu.be/7G9Fjhe_NxM
ویدئوی بالا بردن سرعت آپلود:
https://youtu.be/dQKfkXnThCE
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/MatinSenPaii/4989" target="_blank">📅 20:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4988">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ویدئوی BPB دیرتر میرسه و می‌تونید اداره برق رو سرزنش کنید
😭
😭</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/4988" target="_blank">📅 19:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4987">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/reF5mCjTsAs9iIqSmJrbTgg0AhPErEh9b_Jz-C1eklKnv8risOL8Z1_0TFy7wiYRUBm6j5Z9nZ38mJwTotXIwhXmnHipF8DIQ-RVzZKCiF4qOSNh3FsgR53V4_r-DO1eqxwoQnEZnCO_gYEi-zjJBLfWQmfWVUwRu_pS3XgnaODnhgkxWEdt-YtqWkPU_q6igdNxJ-ybduCd8YV2vJMyV8UNZi7LqS0LtLf_uUblflmkEkaAZw33YXGP0lbzfYmWug5msvKZgwC2uqT9AGqGGqawADH9lAqlgsY-QAf_RYvQDhmZxym97thnaK8dt5GxCE3UwNNx9EyFfUYELzQvmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteVPN دسکتاپ هم سرعتش عالیه. تازه با ساب خودش هم دارم یوتوب می‌بینم</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/4987" target="_blank">📅 13:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4982">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.5.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4982" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">WhiteVPN V1.5.0</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4982" target="_blank">📅 13:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4981">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsFZrhB4bKQdfxRuhvbpPK91csyWCYUrJYAKN8g_7bNE0jwTqTFTPFenKckfh84vsBMW9eUUZkngWVPBDihiV800CXVUdU7VjNlJ2UPMBTqxIbUnMrwdCAaagjv5gEnSYzDJr3TOr-GQ-gvtNUQwF9k5R3KIIslxI3l3zMSSb8SEAYMgYWV3121BsJ8FnUX7RuaUH91dRexW__zhRZr-ArZIcde99ROFIaN7GYYg0EdMVNnHZcLM0tt5LWNOa6se9lxIZfhieNPJ9Yfiqf18u6JrvPorHb3NHYKEJA4BZ-WNvOf79OZ5RVt8OrClbybqlnN_dbQKcb_TmTXQufPpQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید WhiteVPN v1.5.0
توی این نسخه سعی کردیم پیدا کردن یک اتصال خوب و سریع خیلی راحت‌تر بشه. اول همهٔ اتصال‌ها بررسی می‌شن و بعد، اگر دوست داشته باشید، می‌تونید سرعت هرکدوم رو جداگانه تست کنید.
حالا می‌تونید زمان، تعداد و حجم تست‌ها رو هم خودتون تنظیم کنید تا هم کمتر منتظر بمونید و هم مصرف اینترنت دست خودتون باشه. ظاهر و بخش‌های مختلف برنامه هم مرتب‌تر شدن تا انتخاب اتصال، عوض کردن سابسکریپشن و پیدا کردن تنظیمات راحت‌تر باشه.
⚡️
تست اتصال‌ها سریع‌تر، دقیق‌تر و مطمئن‌تر شده.
⚡️
برای گرفتن نتیجهٔ بهتر، تست تأخیر حالا از سرویس پایدار گوگل استفاده می‌کنه.
⚡️
تعداد اتصال‌های هم‌زمان، زمان انتظار و حجم تست سرعت قابل تنظیمه.
⚡️
تست سرعت دیگه خودکار انجام نمی‌شه و فقط برای اتصال‌هایی که خودتون بخواید اجرا می‌شه.
⚡️
تست تأخیر و سرعت از هم جدا شدن تا خطا و تداخل کمتری پیش بیاد.
⚡️
می‌تونید چند کشور و چند نوع اتصال رو هم‌زمان برای تست انتخاب کنید.
⚡️
انتخاب و مدیریت سابسکریپشن‌ها راحت‌تر شده و از صفحهٔ اصلی هم قابل تغییره.
⚡️
صفحهٔ تنظیمات، تونل تفکیکی، اطلاعات اتصال و چیدمان فارسی مرتب‌تر و ساده‌تر شده.
دانلود آخرین نسخه از گیت‌هاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/4981" target="_blank">📅 13:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4980">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">امروز ویدئوی پنل BPB جدید رو داریم</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/4980" target="_blank">📅 12:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4979">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dgbDhvwiA5XvVUfkkhh1PfWx6nzu2t4BDYc1DaPWRxLHc1-kRwDAyvrp7R7ro1ixBlpVbOdMLnOH9NTxKT9Q_Fx7LrtjW1YDsO-cKZinAY1a1JA51TERmqzTJgaTP4jvdtK4OJyG6oCo5KuT-c1W0-RZbR79FFHJWWUk5NHW8it-MuGVJzcpVHByrWFXJsp09qy9rW2iTiqUGff4XNjvc3B5WVsvNaZE6EIUZAogwpGrBjaxP2XLkCfd7Mijh7x7ehdhmA-qwCKVkdT3EFR4lrSou77VT770ogm8R7yWCflYiqmY8brwn_Dp7l3D66YwOlweMNtXA7muhtqviatNiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دمتون گرم بچه‌ها
مرسی از همه‌ی کسایی که اومدید
شبتون کانفیگی
😂</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/4979" target="_blank">📅 01:36 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4978">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بفرمایید لایو
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/4978" target="_blank">📅 01:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4977">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اگر دوست دارید استریم‌ها رو دنبال کنید، جوین بشید:
https://t.me/matinsdungeon
امشب یه لایو کوچیک خواهیم داشت که کمی گپ بزنیم و صحبت کنیم راجب اینکه قراره چیکارا بکنیم</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4977" target="_blank">📅 23:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4976">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iLicg2jvCIrIZOt1z_n1OqTLZt_mPVK31-AlKu-J9bwPNzfv0A67F2A5DHNPMwT3OTAwBEgD7nERHD_RoqAXdoW3ySDrl8Or3nlN8XJKC1a8xSg9szSY4JMDvJGs5XkaEHRc_vQZyEo12bNOm38gAHTrSmY32CGOXCodXR5qrOHqtThjg_w4cVohe0CT9leXN-SvynhEeTWtPoZol08R_Hov8QcI6yq9Mws3vw5s2d-8w9SNAT4SIvw5AQtFoh4EKKhhUzptPVtG0CJM7m5WtnqrW6o3ayfA1TqUiB1xSbTEDrzNkWgR4EVq_1srVnh_n12ACGGPPIm6eKUHUYWkyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ریپو رو یکی از بچه‌ها واسم فرستاد که دوستش نوشتتش و جالب و کاربردیه، برای گرفتن کانفیگ رایگان
فرقش با بقیه ریپوهای «کانفیگ رایگان» اینه که فقط کانفیگ جمع نمی‌کنه. کانفیگ‌ها وارد یه
pipeline چندمرحله‌ای
می‌شن:
1- اول duplicateها حذف می‌شن و ساختار و endpoint هر کانفیگ چک می‌شه
🧹
2- بعد اتصال TCP سرورها تست می‌شه (سرورهای بی‌راه حذف می‌شن)
🔴
3- در نهایت هر کانفیگ با یه درخواست HTTP واقعی از طریق خود proxy توی
۳ دور مستقل
تست می‌شه
✅
یعنی چیزی که توی خروجی
verified
می‌بینید، ۳ بار واقعا کار کرده. نه فقط روی کاغذ.
🛡
اعداد و ارقامِ آخرین اجرا ( که خودم از روی index.json چک کردم):
- تغذیه از
۲۱ منبع
(۱۶ تاشون الان live هستن)
-
۱۰٬۵۵۲ کانفیگ یکتای
جمع‌آوری شده
-
۲٬۳۶۲ تا
هر ۳ دور تست رو رد کردن و وارد لیست verified شدن
- خروجی‌های
verified
،
fast
،
secure
و
top100
(۱۰۰ تا از سریع‌ترین‌ها)
- خروجی برای
V2Ray/Xray، Clash و sing-box
— اپ‌هایی مثل v2rayNG، Hiddify، NekoBox، Clash Meta پشتیبانی می‌شن
- کل سیستم هر
۱۵ دقیقه
خودکار آپدیت می‌شه
- فیلتر
secure
شامل forward secrecy هم هست و لینک‌های بدون اعتبارسنجی گواهی رو رد می‌کنه
🔐
لینک پروژه:
https://github.com/0xRadikal/Free-v2ray-Configs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/MatinSenPaii/4976" target="_blank">📅 23:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4975">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZZ23Xe3f3lSeiJAGf8b84u-t_w-33AeI3lvImBPbAuh6-edVKUs_JNutCADbk7NTXh0Ne1M8gs21U8izNSyggQPty41VTXmXrVhRdoWjCy7rRhDW-B-vrPdFHREuW4V_TkqXrW5lbIhauxGPe-lmWrQqY3-r-XTVtY7yi9GdvS9dCIS_f1Nn4oAqH6Id4Uwrw4xgCNvLEocOpQerSznWF2STkArbmAavVMpVd9-iVnUvJMOUNi_iWUxMS6-8XjzgrjqVTH-9SbijK6efFNYxR81c48jbOyVl4KPEbNGglIWAB3cV5Mvn8jpbnKsHjSPhfybzwL_29LZNj73fdD4jMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته‌ای که من فراموش کرده بودم توی ویدئو بگم، این بودش که برای حل مشکل آپلود حتما باید Fingerprint رو روی Unsafe بذارید
عذرخواهی می‌کنم از همه بابت بی‌دقتیم
❤️</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/4975" target="_blank">📅 17:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4974">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SrFBs7zn6v78Fnw9iNP430s_tjdD8e4VyJfosemff0bKXVQ9rnp19xei012ocwkYZLWbGyBIZ4GV9PrkRoZq1QVCRrFI0p2RaGinj7Dxy3bbBxO2xfmETyMo7BcYtQ-fVbd5Gze7Lg5iDWGbu2hyMfZy9fAkSRqprL2Djyvdy0hLnrJeILtYN0RQ296ViF-mcbFpEFo0R1zyk4fOgVt0hvZ4mVIxh2jJmS3qGeElI1NqcM4gVi45PJoPzNb8ZZmw6Ies3rFiADHB8LJW8-sKjVIzR2PC9uDEEf4lp_WCw9M0ZPE0qHVSof5B1TIoq_LTS6vEEYsx_DN3SN-x1XlDXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب به سلامتی تا ما ویدئو رو ساختیم رفع فیلتر شد Worker اما هنوزم ویدئو رو می‌تونید ببینید سر سرعت آپلود خدایی که این متد پترنیها میده
🥰
که وقتی ویس می‌دید دو ساعت صبر نکنید آپلود شه
و متاسفانه ممکنه بعدا دوباره بزنن ورکر رو فیلتر کنن</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/4974" target="_blank">📅 11:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4973">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">فایل و نکات مربوط به ویندوز:
https://t.me/patt_channel_x/101
مطالب اندروید:
https://t.me/patt_channel_x/91
اسکنر من:
https://github.com/MatinSenPai/SenPaiScanner
آخرین نسخه V2rayN دسکتاپ:
https://github.com/2dust/v2rayN/releases/tag/7.24.4
اپ PattNG ویژه اندروید:
https://github.com/patterniha/PattNG/releases</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/4973" target="_blank">📅 03:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4972">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hzBmDbJufP0lXxyak7QZPLqpZy8UJngr7nA2my3jIQ5hhSxz73rYT9StrFdlaWpD5W9w8PsswQ1Ds-cVo7MDO8Z9lwoJLAyPNszKR7fBovyphQhiWB3j8EuoZ_zjEA0P0_e38nPE4Lh9AEZaKpHcrlweXNzo8h5ebXCGGXnH0LQY5NS8l4GrBz7vL2SdBj_wmwC-PnbklKMnoakW6_kM6_buignofxUk8AvJYv9CyToYfa8tk8e_Lpmsf25277CXva8Hwpp30b-1zf3XZifqz1kwBBSSp92CUIOlXT5aH7dCVQgO9yO18WsIwpVIinuvlphI_wr2IBBuKIzrtXD0Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
رفع فیلتر کانفیگ های کلودفلر + حل سرعت آپلود
⚡️
لینک‌های مورد نیاز:
https://t.me/MatinSenPaii/4973
⭐️
توی این ویدئو بهتون اینها رو یاد میدم:
1- آموزش دور زدن فیلترینگ
Workers‌.dev
با متد پترنیها
2- از بین بردن کامل مشکل سرعت آپلود روی کانفیگ‌های کلودفلر
3- استفاده درست از اسکنر من توی این شرایط
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/4972" target="_blank">📅 03:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4971">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ویدئوی رفع مشکل آپلود کانفیگ‌های کلودفلر و دور زدن فیلترینگ
Workers.dev
در حال ادیت توسط ادیتور عزیزه و به محض اینکه تموم بشه، آپلود می‌کنم واستون</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/4971" target="_blank">📅 23:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4970">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/trLw8WliVi-NiyE8hiM7t36e_izARxbHE8II7-ky4TqENRtsTodIActlbAiQouZOPKyxAiiUi5RNF-w0jqitcfFkXsv2jFq481lF1GoEJj3QcA6KLksD6bNmQGx42KGX60XLTFllF-sqBz9tS3Bx_IvO8w_7aMBJVo3xpGYfuaA8ZbV4psFs6khuiq83BlQ1OwhY954KeWvA3UtGrEVdXP18g__veyJKQD4MTqKtyae0RDxxy11UrY2ocjAXuzRVpDMdYuhRNU1aH8ap_38OiLkf1U4bFUY4PMUMSmyn4elbWLeP_G5ttyBD-_bVtqFhjZ8hwvg8-CvWHaWpLFynlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیزهای باحالی قراره داشته باشیم به زودی
🔫
از
🟩
می‌تونید فالو کنید اگه دوست داشتید:
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/4970" target="_blank">📅 19:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4969">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">با این آموزش، نه تنها محدودیت سرعت آپلودی دیگه وجود نداره، پلکه پایداری خیلی خیلی بیشتره روی همراه اول هم هستم</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/MatinSenPaii/4969" target="_blank">📅 15:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4968">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/syyhsZeFV2teAv-1bHA6vfWhtE3sMe2-6UhrS9M1-EwCJpU52jhRjIEaFDVU63p0OqY5xrTpcHAfYn3CznoVaSFd8U4yZ3iugo_QPWldAZzk8_wafll8yYraieEujeIrR_1YmM-tP4bp2ZM80RfKVPGKrNaDGsmKO2uAkkrLWGFitX898MHw5W37MtIGcFC5oZL3SaTMhhgFzMauNy-8P_TbONiXgZunMMCxCYiApAGaCEGEsVpljDHEwe10qGeuB1ZhT05zvWzhQ4q93rkz0LNOE9hAPM21Xej22bKvkDtgrk0nQbubKblplLMwB0gU-hvvV6nP-452iFDniVPWbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش fragment+fingerprint برای رفع فیلتر دامنه و رفع محدودیت آپلود بر روی کلودفلر (ورکر/cdn) حتی روی نت‌های محدود:  Android: https://t.me/patt_channel_x/91?single  Windows: https://t.me/patt_channel_x/101?single  Android/Windows/Mac/iOS/Linux: Use Xray-core…</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/MatinSenPaii/4968" target="_blank">📅 15:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4967">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/knUuaEsebRV81jx12FCKvTqn5y5K34maFkGZOreVkXiSDfQio41cle8zipuBXeYrKl-6G3uRGKOSayfKrI_nj4y4MoeWSie-nx7KkNUCp6XZ3vX7Ua_0MguihOCySy4hXIZFxOH9tYVKzEObXPOI1Sk5cCyXH7JbJhMa0EpaxSJaTDjkyTHexPvGADx6k7aP-i9YIU0ploUmecinvhh1G7Q-VTW4xHmWunI4qZlYMmhy_k6ADZzfbds7zSgIFCTqUTr0TSkNuYv32jMsZR9etCnYPHMMTsfrcNgY83ijWmt6mCQ8PNkllik6xeMppjHYZOl9eiN5f-b-lW7n8pojrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کلاینت WhiteAesther
(دانلود همزمان برای اندروید و ویندوز / دسکتاپ)
اگر به دنبال یک اتصال فوق‌العاده پایدار، سریع و امن با پروتکل نوین MASQUE H2 هستید، نرم‌افزار WhiteAesther در دو نسخه دسکتاپ و موبایل در دسترس شماست.
✨
قابلیت‌ها و ویژگی‌های کلیدی:
🔹
مبتنی بر پروتکل پرسرعت و مدرن MASQUE H2
🔹
اتصال سریع با یک کلیک (Zero-Config)
🔹
پایداری بالا و پینگ عالی مناسب وب‌گردی، گیمینگ و استریم
🔹
سیستم محافظت از کل ترافیک دستگاه (IPv4 + IPv6)
🔹
قابلیت Reconnect خودکار و Killswitch داخلی
🔹
رابط کاربری بسیار روان، تاریک (Dark Mode) و مدرن
━━━━━━━━━━━━━━━━━━━━
📥
لینک‌های دانلود مستقیم آخرین نسخه از گیت‌هاب:
📱
دانلود نسخه اندروید (Android APK):
🔗
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
💻
دانلود نسخه دسکتاپ (Windows / PC):
🔗
https://github.com/WhiteDNS/WhiteAesther/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
پیشنهاد: این پست را برای دسترسی سریع به هر دو نسخه ذخیره (Save) یا پین کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4967" target="_blank">📅 07:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4966">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">آموزش fragment+fingerprint برای رفع فیلتر دامنه و رفع محدودیت آپلود بر روی کلودفلر (ورکر/cdn) حتی روی نت‌های محدود:  Android: https://t.me/patt_channel_x/91?single  Windows: https://t.me/patt_channel_x/101?single  Android/Windows/Mac/iOS/Linux: Use Xray-core…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4966" target="_blank">📅 05:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4965">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">آموزش fragment+fingerprint برای رفع فیلتر دامنه و رفع محدودیت آپلود بر روی کلودفلر (ورکر/cdn) حتی روی نت‌های محدود:
Android
:
https://t.me/patt_channel_x/91?single
Windows
:
https://t.me/patt_channel_x/101?single
Android/Windows/Mac/iOS/Linux
: Use Xray-core custom-json-config and change/add --> address, finalMask, fingerprint, cipherSuites</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4965" target="_blank">📅 05:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4964">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گویا روی سامانتل و رایتل و نت مخابرات و خیلی از اینترنت‌های خونگی هنوز فیلتر نشده Workers و بیشترین اختلال، طبق معمول روی همراه اول، ایرانسل و شاتل هست</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/4964" target="_blank">📅 00:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4963">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گویا روی سامانتل و رایتل و نت مخابرات و خیلی از اینترنت‌های خونگی هنوز فیلتر نشده Workers و بیشترین اختلال، طبق معمول روی همراه اول، ایرانسل و شاتل هست</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/4963" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4962">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تمام #نکات واسه مشکل فیلتر شدن worker رو داخل این پست میگم:</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/4962" target="_blank">📅 22:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4961">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">حل مشکل اتصال به کانفیگ‌های BPB و تمام پنل‌های Worker کلودفلر:  1- آخرین نسخه‌ی Pre-Release نرم‌افزار V2rayNG رو نصب کنید(۲.۳.۴): https://github.com/2dust/v2rayNG/releases/tag/2.3.4 یا V2rayN نسخه‌ی 7.24.7 رو از گیتهاب بگیرید برای آیفون هم Sterisand آخرین…</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/MatinSenPaii/4961" target="_blank">📅 22:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4960">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZDiUCC74GfIoL4VNlG7MONjNxDNEKuYCSfmlqjfY4MsXuasTlAFeTnfXRXJKeVgb-eHo8ojY_n20UWsvs9VKQrhr1_6E8nziJSm-RgQbd8Zkw1Ftk0st37wcgG57DtS5xKRS8gZiVNTaz9rwMcZx-zVBwBd7YFLp9YXnF8OndszbdnmkQ61PiuyYnSmqiPYVFmx0S6Eh7VLkUiIGazzPzC_OPR_7REEZXOYjARwBsO-R3lG90hSn2ji00MoM2za01jJwiXs6ONN6sBBH4LhNdf0Eue8PXJPxuW_Ts_XnAMeaDhMCvu_AzHuOVmMIDPIr5Nx7CM2FfU_j26U6QmZqwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حل مشکل اتصال به کانفیگ‌های BPB و تمام پنل‌های Worker کلودفلر:
1- آخرین نسخه‌ی Pre-Release نرم‌افزار V2rayNG رو نصب کنید(۲.۳.۴):
https://github.com/2dust/v2rayNG/releases/tag/2.3.4
یا V2rayN نسخه‌ی 7.24.7 رو از گیتهاب بگیرید
برای آیفون هم Sterisand آخرین نسخه کار می‌کنه
2-
این پروژه
از دوست عزیزمون Hidden-Node با الهام گرفتن از نکته‌ای که Patterniha
اینجا
گفته بود، نوشته شده و اوپن سورسه و کانفیگتون هم جایی ذخیره نمیشه:
http://hidden-node.github.io/proxy-builder
3- وارد سایت بالا که شدید، روی بخش Fragment + Fingerprint کلیک کنید
4- کانفیگتون رو کپی، و اینجا Paste کنید
5- پایین، روی Enhance بزنید و بعدش کانفیگ جدید رو کپی و توی
v2rayNG  2.3.4
v2rayN   7.24.7
برای آیفون هم Sterisand نسخه آخر
پیست کنید و به راحتی کار می‌کنه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/MatinSenPaii/4960" target="_blank">📅 21:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4959">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aCdBX-9d15UTK7PNczRZ85-TuokewnNt6rQcRbbgDnr0fQuY4ogafrFzz8H1kfidpR8Y3nHBnJg3uzZRK78z23ElJMIYWEvY3FUmgiSHtM50_8fqP1zQ_1Phzc-dtvtWEL4sde57J5n_pC3BLke7VzqTsM58vbbVRFHL6361Vv2Y-nM1MPXq1wLsKALmMdHTnX1poExG6TiAbvGL7SlltTjnTHKyCi_3g1YJ5By6bRqPDqGzHKB3fjvOc2BNyPOi9GxdGiJHLxqYsRJR5uCwHkyIeu0mzfxHm22ucXMMImmZUUWgzmX6wt5WVpIMcXyLaW_xPgjlAnLMnNBP775k7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست پترن عیان شد
پنل ما جوان شد
مشکل رو حل کردم با کمک Hidden-Node عزیز. الان آموزششو می‌ذارم</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4959" target="_blank">📅 21:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4958">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIkehKdU0QjExPr68UoBOydVWqxcwaLiYfIT0alLw4CK5sg5EpIDLl1-RBVoJnwKySMPL1g0rRIRx0BvdQH2oetk7fEpa-R9Kb7FgQWYgbzOdoUl1crRRQKLwsWXJp76tI4XeZOTZdYv1ocIQPhN0SOMfol1Vd9c1rXS35aUE7ZQz8YENmXZZ6Mr5U7X_SukmbxloMyPSnvEzs5opbOeEvPf6l_pouCv6-hA-sxciCEZ6c4VLgeqmLCpQVaOqrab-vCOmvUgAWbp-VgaCneJdidDVkdshdQ2kbX_1K0BCV0j8IUF8sUPBCrl-l4-yf5YDB3NT1frjFwJ3jZQUxCHXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
چطوری فیلتر شدن BPB و Workers رو دور بزنید؟
میتونید با رفتن به منو تنطیمات، فعال کردن گزینه Amnezia Noise فیلترینگ ورکر رو دور بزنید و به کانفیگ های ساب BPB Warp Pro وصل بشید.
این مشابه گزینه فرگمنت هست برای Warp pro و Wireguard داخل اپ WhiteVPN</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4958" target="_blank">📅 20:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4957">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=k0kd4PyZ1MNgB1cqYLbrrZ4607At0ZMCo0QNxOYCUk8VEZIcrkij1a_IdXMIBayAuQJIhvCw-aPPHQGZlhuzZzp7O8Fto-PAtCyG547H-CmtpwfQugwQzYpg1bZkOh_q1v_y_7g1vvUxvYOSAJjebU2kGQavJ6tbCK0uY_Ku6-Z0J_Bzp3APO9EY9jAwXzfbdmH-824q9rFfH5zD2moedP098QSIcr2Bfbtt9axBEspb3taZ0uw3z9stEVzgE8AdwymA_qWqiZqmGCqGVRCS1XFLNGs_UnmTihRoW4UBRSJDEKuv-JBHZI6kRn_Nz9c30UCup18vF5D5kYkKmY6t8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=k0kd4PyZ1MNgB1cqYLbrrZ4607At0ZMCo0QNxOYCUk8VEZIcrkij1a_IdXMIBayAuQJIhvCw-aPPHQGZlhuzZzp7O8Fto-PAtCyG547H-CmtpwfQugwQzYpg1bZkOh_q1v_y_7g1vvUxvYOSAJjebU2kGQavJ6tbCK0uY_Ku6-Z0J_Bzp3APO9EY9jAwXzfbdmH-824q9rFfH5zD2moedP098QSIcr2Bfbtt9axBEspb3taZ0uw3z9stEVzgE8AdwymA_qWqiZqmGCqGVRCS1XFLNGs_UnmTihRoW4UBRSJDEKuv-JBHZI6kRn_Nz9c30UCup18vF5D5kYkKmY6t8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💬
دوستانی که فقط با فشار دادن دکمه کانکت براتون وصل نمیشه یا سرعت کمی دارید، از این روش میتونید تست سرعت بگیرید و بهترین کانفیگ بسته به اینترنت خودتون وصل بشید.
توجه کنید، هر تست سرعت ۱مگابایت از حجم شما استفاده خواهد کرد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/4957" target="_blank">📅 20:35 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn5.telesco.pe/file/g_T0J-9oMiFcHbOwG-iYQulyaeUCybY1nE82xIt_tUkMj_r4eHzPazEr5xgPkYhn1JLFqjMeDo9Eh0n-sw_E8QlSzveSa2Pilm6Q3sCLlNv7CJbh6s5TkOWCOWhefuJ2nwET6MnhNfxLvikj61SWjECDsYynS1wrBcJeDCzUCTkBDsAWC3DUO3m24YubEyb3Q066zMIL2_O_n1rWI8xieTMgkIc9s44oIihAJ2Xqvp-TSWpTr-avHQsbrHoJ-832feQcRYHdUMwANZvLsIeQ6yFPRCaLEc-q68gypUo8-L1LniEHwREvxG1i2rYRoh2RkYa2FUvuHyba1_UNo-JG0A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 417K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 02:56:55</div>
<hr>

<div class="tg-post" id="msg-106257">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/Futball180TV/106257" target="_blank">📅 01:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106256">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHXr-DNmb26V-Frol3AQFWFPu9f_KodnRLbWr_mo1WJ8Zd_ZdoZw0JrHdqWzuVe9fQB8hRtdgsP8b1kDUhWiZVwq6qJM4D8zKipfEPugcktMnq0LiPJVUUeLltsqo507847VGwkBIaXt0sZtGNHRRWWIlzYu2IvSnwYppLX5yWVfqRha7liCk8jM4bRUCNAafGiVPxQaCVQeZ4-VYc7IkSIhjFn57zEwJYToHEwIAM0yZn0fmuvoZTrGOno-qWC7aFC-jgkUL1EvlNQa1AgpDtheRNMUuh3p3MPheufZ1qDqSyD-g6wU5bN0IZIeoK2vcDAsFN2Y9Ij569_RrZIJjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در
TrexBet
، بین
۲ تا ۴ عکس چالشی
منتشر می‌کنیم که داخل هرکدوم یک
Promo Code یک‌دلاری
مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.
18:30 → اولین شکار
20:00 → شکار دوم
🦖
•
شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت نره...
ممکنه کدی که دنبالش هستی، فقط چند ثانیه با تو فاصله داشته باشه.
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/Futball180TV/106256" target="_blank">📅 01:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106255">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/Futball180TV/106255" target="_blank">📅 01:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106254">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPG734juzKSpOoYgSL2FYxZOzYNpRjnD4pVZ5eQGVZOvFFW2FDrzDTGZDCY9s62z-hb2kzxpWM-TvSS9Znv-LpmocwmTyn-8iVdrG3j3z4w09WC63uuf8k6ZJfuNjAJVQuSI7jbx0g_WuUcULUUggBKz-z5ldy1SgbH4rrPEloSCEMn_EEgF-eW8mmUl2LNXNtqLmpTDIxDhLuUY-Rmx9OKSFahSSMLkk9q1KDmeLwcL7XwhJ3Vug_v-5xgV8CMrZXvZbAcYVBunhK9qNXvtAmHu0BpWjfkFsBR7_AhWBBgBlIswF4N4NpGgO5lOuFjC3a7NG-eOUGKwudQq6-Gilg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
✅
🚨
کیلیان‌امباپه:
🔻
من سال‌هاست که خودم را بهترین بازیکن جهان می‌دانم اما اگر در مراسمی توپ‌طلا به مسی یا رونالدو می‌رسید، اصلا ناراحت نمی‌شدم چون می‌دانستم آنها چه بازیکنانی هستند. اما درباره سایر بازیکنان و کسب جوایز کمی تعجب میکردم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/Futball180TV/106254" target="_blank">📅 01:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106253">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egB80Nhyh4qciCZbQqyfqu07irIi6uyWILRdpCqCXidhhGA2KzqL4CAJqVwtq-Y7Z8p2hk1v7abSkLWgNYmC6-EjMtbmOZhcfn1JeKS3MuO563aUaivdjTP-rGeyLoI0V7ZgMeqRKWZPaQSNGj8a5tXFxGp6jmmT9xYQTilqFBtBu7bKK_m1scNAANK_-xxHmfJseNStOZjfox06FdX6NU33UayqmlkGIUfClE0ZU5T5XI1pkOfBB4glvpRvKxBiDTv5w9Q7gHZ4YUKOotkM86OeztnILQDAZd4j5O6pp5-i3Z2seDZ04Q1dH4HGBNF0aeoXUI22eE809EX4alN83Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
آیا فکر می‌کنید می‌توانید مانند لیونل مسی تا سن 39 سالگی بازی کنید؟
🚨
🎙
کیلیان امباپه:  اگر لازم باشد، تا صد سال هم بازی می‌کنم! (می‌خندد).
🔻
آیا کیفیت من هم به همین اندازه خواهد بود؟ این به هوش بستگی دارد: اینکه بدانید چه زمانی دیگر نمی‌توانید ادامه دهید.…</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/Futball180TV/106253" target="_blank">📅 01:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106252">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwlCufMp5r9NEjGnD_baXlRt9FmYmziJtkJyrny7d59Cd5YuAViYPJJig9cPHgyHo1hVcZQ_pFtYotQ00fZWfzsNarzK58NdUei-I90MFnRQxFTR2Kt3WtEIYJFm4_2B7cGMqNvGFT8Ni5nHjdNl5_ntbnFrsOWiBN5tFlwQwnAdbI0Gfb1-oZ9L6LHMgFouCT0uyS4O2JmJQ8CATlsDfFG9f2fd-uuobEtJUTB4GKRpOuGxQwq9_7oXsmOwbLX5oPm3RT5C2ntJtWp_Bb305zaUya-3OOGXgdlLA9vdLq2xCqptE4i9oTGn-FKwzSlOW_qPcztnB6KoVX8680GfSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
آیا فکر می‌کنید می‌توانید مانند لیونل مسی تا سن 39 سالگی بازی کنید؟
🚨
🎙
کیلیان امباپه:
اگر لازم باشد، تا صد سال هم بازی می‌کنم! (می‌خندد).
🔻
آیا کیفیت من هم به همین اندازه خواهد بود؟ این به هوش بستگی دارد: اینکه بدانید چه زمانی دیگر نمی‌توانید ادامه دهید.
🔻
او نیازی به فکر کردن در این مورد ندارد، چون هنوز می‌تواند این کار را انجام دهد. ضمن اینکه، مسی خودش یک بازیکن فوق‌العاده‌ خاص است.
🔻
من خودم را یک بازیکن متفاوت می‌دانم. اما او هم یک بازیکن متفاوت، در بین نسل‌های مختلف بازیکنان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/Futball180TV/106252" target="_blank">📅 01:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106251">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAq1h7WKBtXOjfoTGrEHERbEkrrYSTLxYuG7FxzMhMzP5liVs76_EVvJ204775MKs19FAGnUBUhYjqhhYIcF-QqjxCA4u0MaiyUQA4tZyl8c7KbWPP7KqLBnEntc_wgslL5WisojyJBKfXMTlw669ZKruD0iyduf-rcfQ3imOjDIiw21gEE3Ebcj2nkAoGarF_3Bx_WV6tn8aP0gdWBrIbA6ZD97plceB1tbFGsGaXAW6IchLMjYMFaWhYXyAlAb-NcGeK_yhWK4ABtaSwZSA5aE8Lf8ZNCOE_yUaViNDqKLv9tHiSRYp2MO73ZikEq27Fb626BwW22UbeGOB0__xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😆
📱
استوری ابوطالب‌حسینی: ما نبودیم دیگه تو فوتبال حاشیه نبود و همه پاها موازی بود دیگه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/Futball180TV/106251" target="_blank">📅 00:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106250">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b4f3dd673.mp4?token=ol59WqiYzSSF0MGUNBrht6gUSvo9OkAiSQJ22b9XyIPJ9jE1LCPJ9Vy2-4BxVdvoid7Y-w2WIBM9d67jFY8AdPe1lyqz6pG3FSWyUFyx1n0zom_N4bDAWwQeKf_eAnxMSDcUBZs86jcD1xGGVU054hnfgYSbxeYXRKpBxT9FSheOiQ_j_z625NqD4IjoDdLOqSv0h-6jy5Ye2VvQ74uw3Ll9oZB_9etVoziwk6t87VNaIhal9D4Y8u0bPQ99pI42id3dKIVU90LlcX58NWu76p3tbKphBdP_rrb6KIV5ZX8LQMfmxcJ8q2pt4l2y9hLOyWpjZgSh8PURJyK69MaScQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b4f3dd673.mp4?token=ol59WqiYzSSF0MGUNBrht6gUSvo9OkAiSQJ22b9XyIPJ9jE1LCPJ9Vy2-4BxVdvoid7Y-w2WIBM9d67jFY8AdPe1lyqz6pG3FSWyUFyx1n0zom_N4bDAWwQeKf_eAnxMSDcUBZs86jcD1xGGVU054hnfgYSbxeYXRKpBxT9FSheOiQ_j_z625NqD4IjoDdLOqSv0h-6jy5Ye2VvQ74uw3Ll9oZB_9etVoziwk6t87VNaIhal9D4Y8u0bPQ99pI42id3dKIVU90LlcX58NWu76p3tbKphBdP_rrb6KIV5ZX8LQMfmxcJ8q2pt4l2y9hLOyWpjZgSh8PURJyK69MaScQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇮🇷
🇮🇷
آنالیز بازی استقلال و پیکان توسط تقوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/Futball180TV/106250" target="_blank">📅 00:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106249">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ki6c9qgAj0H2rpDsdJEHeXPxgEbNjYmf93wwkSsCKbtmbOZbIwMczr9WwwDhQuOfW-e_cCxzJEDXFH46CW82v1_iYadEWmRLpkwob89I2q1NJM7nPVIVJCUbCJ512B2P8sJT-drjtCpIvjDCqPslp2QZTp4l7wOQZJJl3ABfZ3wGZuSzLMaUGG7feCeYMWE-VDG-zRBqr8s6zfqIStLUKfDIddLw7Mn880pLL_9PMTL1s8PXGrEwzVvVqJiRNK1YR1EupmD4HFhfMQp-lzeqqkRKqVm_mpEcGjc0NNdriVeXOZBrL1T9izMLwxfsnCf1dCWwFJ0AJm0dultlX8guvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
⭕️
🇮🇷
با اعلام باشگاه استقلال، مشکل مصدومیت یاسر‌آسانی جدی نیست و این بازیکن برای بازی روز دوشنبه مقابل السد در دسترس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/106249" target="_blank">📅 23:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106248">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOuwTmJzYe4rzbVQlspnKHvt-sMB8QQh9sqXOgu8HDr9LB-0uwJxcUPsTg_tckpHBedbyB2KioIL_GarM5oeeTJnH_MISRBL0lqrTmY1amK6AL7kJhHM1scB-cDg1i_Ja6g_2SX6N_qCdux_lGU2kh_YnqhRQUdpV0enGMK9DZRLC5OjKwYpHCBAGgNnV0J_GMmf1RFibX6g-fEmDQYF1VAlWf31mjZd0h9kK8-_Nip6tqanbCoaM5GASXrE-1ox-W-M-Ozo_R1YMwnxsque-fneDx1Nfl7Dbn1xVIJqoeemWFSBFJaw4-XlHzTxZlpvThPJB7jRpWbYXOlbqV6n_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🙂
🇮🇷
نحوه برخورد شجاع خلیل‌زاده با مدافعان تراکتور: حمال‌های بی‌خاصیت
❗️
❗️
❗️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/106248" target="_blank">📅 23:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106247">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63b0b11397.mp4?token=fEDKzYoL8GrkjGh8NUnVUTrO0ZyF-0j15v99M-wJC9D0vMG6gXopDlbcFC48IO73XGVg81sqBNBGcghfZ27jPRmsJayutJie1JGN1Cju5yRercxS6NWVJ7XKmWw5EPbFyiIzmWIUQbheZM814T-aRNTSIYW3J3ZTUCi342cFeCl4UVuSPCJOdP02Fv3neBVPKrkUPW1N6pAl6Mqr3nfWPcWKUW2mzrYutgnYChS4T9-IorrM8Ov3bfcFttDgmfwquDUNaiHsT8BBpM0Fbr_JbgRmnfkMf8dvUTC-oA1tEoS0Wo63RbX1eKDoB44er3hu8uPSFxOemZ9O8IJrH4zONwagBmkBpaAgWEUoDhal_7A1HWbz5I4IrZxHNihuuiPuPdItH3gVWJy8V44ShMG09hnM5ppoCAUT64a4Y2f6lxfFy1xI0EZ0_19vifJWrXTf93PA-HKobB91DBalqyp9QZwsnIsbBCK0H6aVxcKDgAhvflDRhooig6V0fLj5FmZdA2awzi5jvMbMBwcmyo_MtdgPS8Xq6gecADT5ZmUCqpO1OnYxTJTSJK-poxsoef8Ewr1UOjyZiAoW7_yU_Zob-WjtZB8jj8rmpZDWLO07JSd1l3t_LecH2HryJyDru_gAQXnIIT2cjVZPhwR0_BgSwp-yer39U3CFtiIBSgRdw6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63b0b11397.mp4?token=fEDKzYoL8GrkjGh8NUnVUTrO0ZyF-0j15v99M-wJC9D0vMG6gXopDlbcFC48IO73XGVg81sqBNBGcghfZ27jPRmsJayutJie1JGN1Cju5yRercxS6NWVJ7XKmWw5EPbFyiIzmWIUQbheZM814T-aRNTSIYW3J3ZTUCi342cFeCl4UVuSPCJOdP02Fv3neBVPKrkUPW1N6pAl6Mqr3nfWPcWKUW2mzrYutgnYChS4T9-IorrM8Ov3bfcFttDgmfwquDUNaiHsT8BBpM0Fbr_JbgRmnfkMf8dvUTC-oA1tEoS0Wo63RbX1eKDoB44er3hu8uPSFxOemZ9O8IJrH4zONwagBmkBpaAgWEUoDhal_7A1HWbz5I4IrZxHNihuuiPuPdItH3gVWJy8V44ShMG09hnM5ppoCAUT64a4Y2f6lxfFy1xI0EZ0_19vifJWrXTf93PA-HKobB91DBalqyp9QZwsnIsbBCK0H6aVxcKDgAhvflDRhooig6V0fLj5FmZdA2awzi5jvMbMBwcmyo_MtdgPS8Xq6gecADT5ZmUCqpO1OnYxTJTSJK-poxsoef8Ewr1UOjyZiAoW7_yU_Zob-WjtZB8jj8rmpZDWLO07JSd1l3t_LecH2HryJyDru_gAQXnIIT2cjVZPhwR0_BgSwp-yer39U3CFtiIBSgRdw6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
کنایه‌های تند وحید هاشمیان به حدادی:
🔻
حداقل درویش از مدیریت الان مرام بیشتری داشت و به نظرم برکنار شد چون من را برکنار نکرد. چطور برای اوسمار این چنین مراسم بدرقه ای انجام دادید ولی با من این گونه برخورد شد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/106247" target="_blank">📅 23:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106246">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa1d2ea919.mp4?token=dhrOo1Z86rrTK9Trs_jZ8JUJEOrO0L5KWLfLAqUpbFirOWmDnRqPURi6g9c41Dx2WmA3Hxl4fPAb26lfMvige6Qjcd-NZD0xjQjfUIadT1K2cFettPNrVh1LmBC8l44UE3tf8qGd1a9yNEC9X1r7wl6GG_6IZrXGyfAK8m3wq394Oj0reCFjFEyzu8U88FJNnnlyzbBZTmgBgHQ5WkJpuJivdXqNDU8eW1nMTYfOAWeQ7ZSOcrofuoPlsxmDfkOeYecAOHXDJJezMoxmq1QdZIz6BxmkXxJj1X3JHkEQtO4gKMQ2wz_Ui_i6O3BuwVkbdOsNjG9Kmx6PExwq9sE1Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa1d2ea919.mp4?token=dhrOo1Z86rrTK9Trs_jZ8JUJEOrO0L5KWLfLAqUpbFirOWmDnRqPURi6g9c41Dx2WmA3Hxl4fPAb26lfMvige6Qjcd-NZD0xjQjfUIadT1K2cFettPNrVh1LmBC8l44UE3tf8qGd1a9yNEC9X1r7wl6GG_6IZrXGyfAK8m3wq394Oj0reCFjFEyzu8U88FJNnnlyzbBZTmgBgHQ5WkJpuJivdXqNDU8eW1nMTYfOAWeQ7ZSOcrofuoPlsxmDfkOeYecAOHXDJJezMoxmq1QdZIz6BxmkXxJj1X3JHkEQtO4gKMQ2wz_Ui_i6O3BuwVkbdOsNjG9Kmx6PExwq9sE1Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
محمد تقوی، درباره پیروزی استقلال برابر پیکان در هفته هفتم لیگ برتر گفت: «استقلال نمایش خوبی در این بازی نداشت اما باید این بازی را می‌برد. خط دفاعی استقلال آشفته است و با این شرایط در بازی‌های آسیایی مشکل بزرگی خواهند داشت.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/106246" target="_blank">📅 23:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106245">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/657c84dea6.mp4?token=hSj_OZoBlEnKxrIVT1yT2la3mYWtmTSNIlpD2_y9BF6H4H4c_8agbprWlMpMdW8lJA4u-BCrDjffRIV68NbRrDhyuYgmnHqqHDkeqT3hegDyzaSyTqSM_yzyuCkHUSQFN8gpBeyIrN-iXOaiAFSomM3x7bkPCHD3x3RonD2IuHQilP5SvOqP-hLzWCKlFuUaf94INeWBUgrEXnBwTC5yd4dePlLLYqNV3NnTfpb7XWP-pEJ6bh3t9SLgzkTvXFlNaI2YSEplRi6xXOSGYsvMZmm9FZEop9GJhbItYKXJ8e-e6X5z5Ypg98xKoEpN12RUFFeh3iDFzR7y1Oi2nGcW7gnFuQ-Sk8LLZ6bIRTebgTHzEcxOVBw8PQt4Yb7QcjkG1L84jxPzJXta_iLQdUmpDQ2xpX0IZ2XIp0DPa9rAgh58RVJYc0wbE4T9d2u7_eEzA15DgHw4MEWKqoaHu8MrbDaJhUygT3rKQvzHXwJ3agIJWVzwNSClWjfwjizBOI5_hGUD6IjGfD8nhZ6gf01kHZ8T9iuopJeHJatX1r_5_5KCXCdB3BXWMIcKAgHW2d4M0U-G5EEsjhv8apPHacbHrnzdq13_J7Mg8rfEr9Jk8AlzTvohb8Vchnoijn2Gaxkp6ha4FzMtYXGwm-0iWyNvTHI8t2kGmMx_W5aKYvT40VU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/657c84dea6.mp4?token=hSj_OZoBlEnKxrIVT1yT2la3mYWtmTSNIlpD2_y9BF6H4H4c_8agbprWlMpMdW8lJA4u-BCrDjffRIV68NbRrDhyuYgmnHqqHDkeqT3hegDyzaSyTqSM_yzyuCkHUSQFN8gpBeyIrN-iXOaiAFSomM3x7bkPCHD3x3RonD2IuHQilP5SvOqP-hLzWCKlFuUaf94INeWBUgrEXnBwTC5yd4dePlLLYqNV3NnTfpb7XWP-pEJ6bh3t9SLgzkTvXFlNaI2YSEplRi6xXOSGYsvMZmm9FZEop9GJhbItYKXJ8e-e6X5z5Ypg98xKoEpN12RUFFeh3iDFzR7y1Oi2nGcW7gnFuQ-Sk8LLZ6bIRTebgTHzEcxOVBw8PQt4Yb7QcjkG1L84jxPzJXta_iLQdUmpDQ2xpX0IZ2XIp0DPa9rAgh58RVJYc0wbE4T9d2u7_eEzA15DgHw4MEWKqoaHu8MrbDaJhUygT3rKQvzHXwJ3agIJWVzwNSClWjfwjizBOI5_hGUD6IjGfD8nhZ6gf01kHZ8T9iuopJeHJatX1r_5_5KCXCdB3BXWMIcKAgHW2d4M0U-G5EEsjhv8apPHacbHrnzdq13_J7Mg8rfEr9Jk8AlzTvohb8Vchnoijn2Gaxkp6ha4FzMtYXGwm-0iWyNvTHI8t2kGmMx_W5aKYvT40VU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇶🇦
کامنت‌ هواداران پرسپولیس زیر پست‌های السد: قرارداد آسانی غیرقانونی است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106245" target="_blank">📅 22:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106244">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9444ed9ae1.mp4?token=YEllYRrhSxkfTvqb8sDuwHkCulTrk_JpUc7M_CNaQpYuUpnZ_zXQwRGdLu0I2_BG8ZphLIfCMi7lVOdETr1QA6i7My55Mmy9Puv2aHbFehMFD2FgCrS2bQw3WE1ackHswetZK7h2W4O_0EN7SV6nl_NW9vUCqa7KT84EWWvCNMloKDOmDD2k0jBFUL2q9jldCnPWIvyXqJQrX2ADpvh91c3BpXd27imZ0oOpeonzqtpUa0UJOGyCYEcj1j0BTYZqVPXVuNsX1HBibfQ_qDmb-fwAulHz_bnxPlC-VN7xLHxK9VHeaCZWZNBc8tBO3jZn5Jri3M20WEiTFhdUmKTbfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9444ed9ae1.mp4?token=YEllYRrhSxkfTvqb8sDuwHkCulTrk_JpUc7M_CNaQpYuUpnZ_zXQwRGdLu0I2_BG8ZphLIfCMi7lVOdETr1QA6i7My55Mmy9Puv2aHbFehMFD2FgCrS2bQw3WE1ackHswetZK7h2W4O_0EN7SV6nl_NW9vUCqa7KT84EWWvCNMloKDOmDD2k0jBFUL2q9jldCnPWIvyXqJQrX2ADpvh91c3BpXd27imZ0oOpeonzqtpUa0UJOGyCYEcj1j0BTYZqVPXVuNsX1HBibfQ_qDmb-fwAulHz_bnxPlC-VN7xLHxK9VHeaCZWZNBc8tBO3jZn5Jri3M20WEiTFhdUmKTbfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💙
سعید فتاحی رئیس سازمان فوتبال استقلال: به غیر از خلیفه و گودرزی در نیم فصل هربازیکنی سهراب بختیاری زاده بخواهد باشگاه استقلال جذب خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106244" target="_blank">📅 22:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106243">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dab1b117ec.mp4?token=SSLESN-LdGJZbbPhJbgP_gRuoUpknf8W-m2g2KrVWKUbPwC77eU36-8m796iEByY6ZPB23ZfbBY7hxEgrLmwXXP8ay4YNnGLPt-OoISMwkN8rjxZpAobN2C29xrKo55lkHMJrISJ0JfB3XW2284sOvaAEGde15tJeiiIr4NX8ZuCzYwVnkRFQqKKtFX_sHleo4XMPGT6yu0Uz2GCXyhe55GqfFSA18cqthRMg6cIcNVIm3bHKuiardgHIMK0v4WthwWh6XmSTsPdUtEpah9jTgoon-PNiQ8OAgz5lICBjWE9PJM-XqOZw_hAneyzve1-vGwNM6u-y0wHdfFDEJg_Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dab1b117ec.mp4?token=SSLESN-LdGJZbbPhJbgP_gRuoUpknf8W-m2g2KrVWKUbPwC77eU36-8m796iEByY6ZPB23ZfbBY7hxEgrLmwXXP8ay4YNnGLPt-OoISMwkN8rjxZpAobN2C29xrKo55lkHMJrISJ0JfB3XW2284sOvaAEGde15tJeiiIr4NX8ZuCzYwVnkRFQqKKtFX_sHleo4XMPGT6yu0Uz2GCXyhe55GqfFSA18cqthRMg6cIcNVIm3bHKuiardgHIMK0v4WthwWh6XmSTsPdUtEpah9jTgoon-PNiQ8OAgz5lICBjWE9PJM-XqOZw_hAneyzve1-vGwNM6u-y0wHdfFDEJg_Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
🎙
نادر محمدی منجنیق: به صورت اتفاقی این نوع پرتاب رو یاد گرفتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106243" target="_blank">📅 22:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106242">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
⭕️
⭕️
🇮🇷
با اعلام باشگاه استقلال، مشکل مصدومیت یاسر‌آسانی جدی نیست و این بازیکن برای بازی روز دوشنبه مقابل السد در دسترس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106242" target="_blank">📅 22:24 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106241">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3e40e30b.mp4?token=e9N57IRG-Y_8Mh0sfkfvfZC47_WuQGVOF5ef7Jowk4QIM0UFQRzks-I0pEnXi6thSS_W_xPd19A4GcA4z5y5bEN9GdM_PNWIQm_buCSLwPubXPZ6j_gVoW8DUZDt-m_jzX-xU_N4eLM_gVjAQWGEgKZL3XsW_Gyo9OhD6eF0LuIkPC7gJvj1K6G4etCJ6MfvUYG0V6YbJqTZIB0KlwK3TvF7oU5YB-o_WZOR1LDgbWh9Oo3gH5-YZX7WJmnyFtjBE6WG_uxY3Tiwsts6lxVyCAUyl3VZ48y4UhUeRxnTHKVyAIHxdNAf09d3xTQOqVfZtmXZtNNQ50wWhzw6U7ThGliFEx0Yf_rBNYLdthJILhi7lUG1JNYppXgC-RE0u5l1elwZIkD3tfYerii6X4etGGPAlA_ilRQHd2Aa0QxyQ7jDh048PtQUZl8Vv2ZtTQbLOhFMS458DcEpQbiHcaFFwXiI_to94SjkwCb6B-XdXbfKo3RrsdXYK-5QVvvbAotUvdOsMEvLB_6MFaKrVoyEote5ZUGgRYnr3ZJ2p6KggigGzxFeFDLMjse23_avhsNgC28E4RZ8SjN7MncMyuJgwMG4LDGUBhuHRwL6XIqKCZ0UmFPBkXo-y8wLKOfJz3f4C1ltCZmFtQ34Y8AYAlyqi6o0MBST0_VND23Z8dHe7Zc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3e40e30b.mp4?token=e9N57IRG-Y_8Mh0sfkfvfZC47_WuQGVOF5ef7Jowk4QIM0UFQRzks-I0pEnXi6thSS_W_xPd19A4GcA4z5y5bEN9GdM_PNWIQm_buCSLwPubXPZ6j_gVoW8DUZDt-m_jzX-xU_N4eLM_gVjAQWGEgKZL3XsW_Gyo9OhD6eF0LuIkPC7gJvj1K6G4etCJ6MfvUYG0V6YbJqTZIB0KlwK3TvF7oU5YB-o_WZOR1LDgbWh9Oo3gH5-YZX7WJmnyFtjBE6WG_uxY3Tiwsts6lxVyCAUyl3VZ48y4UhUeRxnTHKVyAIHxdNAf09d3xTQOqVfZtmXZtNNQ50wWhzw6U7ThGliFEx0Yf_rBNYLdthJILhi7lUG1JNYppXgC-RE0u5l1elwZIkD3tfYerii6X4etGGPAlA_ilRQHd2Aa0QxyQ7jDh048PtQUZl8Vv2ZtTQbLOhFMS458DcEpQbiHcaFFwXiI_to94SjkwCb6B-XdXbfKo3RrsdXYK-5QVvvbAotUvdOsMEvLB_6MFaKrVoyEote5ZUGgRYnr3ZJ2p6KggigGzxFeFDLMjse23_avhsNgC28E4RZ8SjN7MncMyuJgwMG4LDGUBhuHRwL6XIqKCZ0UmFPBkXo-y8wLKOfJz3f4C1ltCZmFtQ34Y8AYAlyqi6o0MBST0_VND23Z8dHe7Zc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
✅
🇺🇲
بررسی حادثه ۱۱ سپتامبر از این زاویه؛ برای دوستانی که اطلاعات کمی دارن دیدنش توصیه میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106241" target="_blank">📅 22:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106240">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16ebf2050a.mp4?token=VQICLhFztAjowQkj7UKIpq6aywK0g6PfHax4ZT12WMYYzYADOVJ9Pr9wVLfv2t1YYOopt4FUa_l2M0SEtw7r1yxHhXoPb-oJ0QaUzefOyYmRgla02hniPhyCoK-tUbBNmCirpPi9WavJPItbpoImCQfL2nByXFOIcOiqYpqEOVVIKBtTokoUpzlNPvEVUtLVEXShGsIhrBY6cNavqFY62SuJdwggUgVPLMzXhMg6g4hgyEVXGMI6Syc-VoORFvcfAzaQbGVLe6S7xf_se13EHh399R5ynqrroJW0f2eSmJYs4dW5jOQiBxy38d9PD-es7FskA5qSjK3Jp3mlAuPIDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16ebf2050a.mp4?token=VQICLhFztAjowQkj7UKIpq6aywK0g6PfHax4ZT12WMYYzYADOVJ9Pr9wVLfv2t1YYOopt4FUa_l2M0SEtw7r1yxHhXoPb-oJ0QaUzefOyYmRgla02hniPhyCoK-tUbBNmCirpPi9WavJPItbpoImCQfL2nByXFOIcOiqYpqEOVVIKBtTokoUpzlNPvEVUtLVEXShGsIhrBY6cNavqFY62SuJdwggUgVPLMzXhMg6g4hgyEVXGMI6Syc-VoORFvcfAzaQbGVLe6S7xf_se13EHh399R5ynqrroJW0f2eSmJYs4dW5jOQiBxy38d9PD-es7FskA5qSjK3Jp3mlAuPIDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❤️
محسن خلیلی مدیر پرسپولیس: چرا می خواهند ترمز پرسپولیس را بکشند؟ چرا می خواهند حق پرسپولیس را بخورند واقعا این شائبه برانگیز است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106240" target="_blank">📅 22:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106239">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/febf5e7a8e.mp4?token=KvG8a5am65pd2UCvYTpPlUc422jnBaG_LqYH_yO6n0beJihLmhlNTWA7MZofVGuG5LeMI2DX92j85jzE6N7EerQbP_i1i-xb5RrJl6ziSqeP14pxBb7bf0_qaIVSpDEA4OQ8KVuAWcp4jg6Nrw9tr4pGdICXx8L4srSvyHsoenV3tpUnEg9N1A8q2ESpMmD8xypXJRzvoltF75NwDM0n8VNSN37Qvza5dxFX9-U41OwRZdM5TddCnPeLdnTvaNGZmduZbb43rmqJy4ewwMVdiDdD-nAMvnegHQJsHHVp0-Qtpa3oSqDwyNdGVx3R2DqRqs-kJjLTwlbx__wMC1WHkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/febf5e7a8e.mp4?token=KvG8a5am65pd2UCvYTpPlUc422jnBaG_LqYH_yO6n0beJihLmhlNTWA7MZofVGuG5LeMI2DX92j85jzE6N7EerQbP_i1i-xb5RrJl6ziSqeP14pxBb7bf0_qaIVSpDEA4OQ8KVuAWcp4jg6Nrw9tr4pGdICXx8L4srSvyHsoenV3tpUnEg9N1A8q2ESpMmD8xypXJRzvoltF75NwDM0n8VNSN37Qvza5dxFX9-U41OwRZdM5TddCnPeLdnTvaNGZmduZbb43rmqJy4ewwMVdiDdD-nAMvnegHQJsHHVp0-Qtpa3oSqDwyNdGVx3R2DqRqs-kJjLTwlbx__wMC1WHkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❤️
محسن خلیلی مدیر پرسپولیس:  2 تیم ( استقلال و تراکتور) با تیم ملی امید همکاری نکردند و بازیکن ندادند چرا کمیته انضباطی با آنها برخورد نکرد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106239" target="_blank">📅 21:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106238">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a557a62450.mp4?token=H5yg1GtssXxTE8IRdM-JUA7Y71WTd1uhhzbvQhToahtNK07KHTdaSpVob01CIKf4VfduVZjK-4oxa9sDTrKthbUETMz8e0UzjsG554OjvhZ1hiqcHBgZYBPMPBjYrQK2Dh_3ZFOgzBafRYON_xEIJbUkvuDk7a0UDmWxUR_kh2k2vL60Arbm37XNtYIkGXRuq_WIKHg5A2LOOaJKwtxIuHeZRzThyPYIvFdgYzur22d36rEYyIuQJgexbDnMDmj6ebvuiOPWKQGMtq80G1bXMLEJXcqRlu7ACM4g5Cr4XZwnGW-LwDKu0HS3onQXavXebdV33R-DAOFYS_R5I8aYjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a557a62450.mp4?token=H5yg1GtssXxTE8IRdM-JUA7Y71WTd1uhhzbvQhToahtNK07KHTdaSpVob01CIKf4VfduVZjK-4oxa9sDTrKthbUETMz8e0UzjsG554OjvhZ1hiqcHBgZYBPMPBjYrQK2Dh_3ZFOgzBafRYON_xEIJbUkvuDk7a0UDmWxUR_kh2k2vL60Arbm37XNtYIkGXRuq_WIKHg5A2LOOaJKwtxIuHeZRzThyPYIvFdgYzur22d36rEYyIuQJgexbDnMDmj6ebvuiOPWKQGMtq80G1bXMLEJXcqRlu7ACM4g5Cr4XZwnGW-LwDKu0HS3onQXavXebdV33R-DAOFYS_R5I8aYjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببینیم دیشب در لیگ قهرمانان چه خبر بوده.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106238" target="_blank">📅 21:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106237">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dtq6rKVsXQGTGqE1S09Svb4-TzQNWQefROmVCkDXaboczIXHn37fvqnYgN0fD-6LmX3Ept4iPUHXqowbO1qKaS7iB9JFLV8SVKVUw2ynoD_Oz6TtzJ_zPBKE6DcDf8Wsvj_eo5-zCv3UrL2YnVaIbyVfwCIMwvt-UkN4riA_l9CA5P344n1jauGG81Z64RdnNEbXM30VPuqdeNLDDOLjFZm_xKBO6QfmdHn2CIQP1Q67we1oKwsiMbm5AkXin8Qy7VsD_bOure9MGsQJhRqjBOzj0EnVzPlYoH8el88EfTNudsnrjpe4K56Kg8YL1VwV9PZxM4C1ffSzxf_1OCRieg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇮🇹
🇪🇸
سسک فابرگاس، سرمربی کومو:
🔻
«بارسلونا ترسناک شده. سطحی که تیم در حال حاضر داره واقعا ترسناکه. بازی دیشب رو دیدم. فاینورد تیم خیلی خوبیه، ولی بارسلونا کاری می‌کنه که حریف ضعیف به نظر برسه، چون در هر لحظه راه‌حل پیدا می‌کنن.»
🔻
«می‌تونی مقابلشون نفر به نفر دفاع کنی؛ همون‌طور که فاینورد سعی کرد این کار رو مقابل رودری یا پدری انجام بده، اما بارسا از هر نقطه‌ای راه‌حل پیدا می‌کنه. فرقی نمی‌کنه چه بازیکنی وارد زمین بشه؛ سطح تیم همچنان خیلی بالاست.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106237" target="_blank">📅 21:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106236">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/525ed46310.mp4?token=BnPvImjLhsRH2wmLlBgOL-adYIQbLDF-3Ro2rFCTWc51YTeGKuaLOCzMpAiVt1K9doi42DKT0ohM7l22QbLSG6mReS1rd0UpqBpcfUPXm7mFkpQpPvU1mSxj6W7dFjSWRAil2CbJ8rCaU7Im-za-FTuBkzruNjYFHcrMl42ELU8C040ypMumekAaDr2jeLlsKGKtJ2B1VDTWCbpoiAHMd2fjJcRFYPhRXg6Z4ETubOBGhe7j0LADhj5rSWPb49FpCuQtLw-ncIeHHMOrv5gaq2WYLi2p0CM2K5AWfuxklipL3Hxza291FVZwA6xa_cUjGwYAd_PvqCH2dzSP08PQbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/525ed46310.mp4?token=BnPvImjLhsRH2wmLlBgOL-adYIQbLDF-3Ro2rFCTWc51YTeGKuaLOCzMpAiVt1K9doi42DKT0ohM7l22QbLSG6mReS1rd0UpqBpcfUPXm7mFkpQpPvU1mSxj6W7dFjSWRAil2CbJ8rCaU7Im-za-FTuBkzruNjYFHcrMl42ELU8C040ypMumekAaDr2jeLlsKGKtJ2B1VDTWCbpoiAHMd2fjJcRFYPhRXg6Z4ETubOBGhe7j0LADhj5rSWPb49FpCuQtLw-ncIeHHMOrv5gaq2WYLi2p0CM2K5AWfuxklipL3Hxza291FVZwA6xa_cUjGwYAd_PvqCH2dzSP08PQbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😳
😳
😳
اینارو از کجا پیدا می‌کنن
😂
- کارشناس صداوسیما می‌گوید ذخایر طلای بانک مرکزی ایران ۵۰۰ میلیون تن است!
یک ۵۰۰ میلیون تن و یک ۸۰۰ میلیون تن دیگه هم گفت تازه
😂
حالا جالبه بدونید که کل طلای کشف شده توسط بشر در طول تاریخ ۲۲۲ هزار تن بوده
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106236" target="_blank">📅 20:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106235">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e059f4f8a8.mp4?token=ZWriskzAXy_1DRrewILDzEJNqHoFo1AB3ingdbxU6FjCQrnMENm4QvZmSRH192s6hjozuJURbXsP2dEg1eD4lvgcpVfKOBD4xl3ENPX9qNlRdHe7aijQHHhbfU5gUCQWQA-UOXgWwO36HDpSTdprLq-lyUxb_hlycdyNdCGOgg6OIz9cJhnqGc5MkxyIdonMjMEaweMf6IRnJOnuv3L2pSx6CA9lg6VMoKuijONOHUA7COsjxLKnk32M8nuN-1XBA7xLODMhbdWHvCzxUOvMPmMRQB9Q3V97gNUII8j8AXqeDcLGabrzW6TUzIQR7ypL36OEgilMF8UVLXxORHptTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e059f4f8a8.mp4?token=ZWriskzAXy_1DRrewILDzEJNqHoFo1AB3ingdbxU6FjCQrnMENm4QvZmSRH192s6hjozuJURbXsP2dEg1eD4lvgcpVfKOBD4xl3ENPX9qNlRdHe7aijQHHhbfU5gUCQWQA-UOXgWwO36HDpSTdprLq-lyUxb_hlycdyNdCGOgg6OIz9cJhnqGc5MkxyIdonMjMEaweMf6IRnJOnuv3L2pSx6CA9lg6VMoKuijONOHUA7COsjxLKnk32M8nuN-1XBA7xLODMhbdWHvCzxUOvMPmMRQB9Q3V97gNUII8j8AXqeDcLGabrzW6TUzIQR7ypL36OEgilMF8UVLXxORHptTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
فراز کمالوند سرمربی خیبر: الان که پرسپولیسی‌ها مخالف هستند 3 ماه پیش هم که پرسپولیس اصرار داشت تورنمنت 3 جانبه برگزار شود همه مخالف بودند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106235" target="_blank">📅 20:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106234">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmFtdxztLJKPir9DKFgBliy8PK7tGUEixPp8E6lUemmq3YzTQ3fFoT3tGR_4qxEx8DqBZU3apm5KpMd8TgzHQAhbVgY1YxfNp3_lgbRcNXLn0CvRolX3l-vD4fksGpeqr7-W2iEIDnHbVM7l8rYxUJ2ygCRmufu62Grj5N8q5mn6sHYjZmywbvlf1xjfO3U1NPx6VMtsL4xHJKc43OTP1O1ywWnc0R_WkpjjV9DahwCYDpDbO5ZkIOFI7b6SZ-PKo4JM-uYm6okK4HZW4k3D-GVPMR2pp-sqrZDwchoGFaA0WodTAawkC4nHSO2_kUxzuiQ3ww2VaL0w9Sr3Ny4ktA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین‌ماهینی عزیز و همسرش
✅
🔥
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106234" target="_blank">📅 20:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106233">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d8215d3c.mp4?token=R_SBVVIsqdyUzYIfjUCL0kMBm2pIdIT-_sKbBQ72oUK5PjjH0BKw39onV_1hu44JX59ZW1OrsGXwwIMRACARXU7w6QFmvWyxmU-XeSkdOFTxJZeoZTCuG0m4U6ibtGmTeAlrjZnD81GjYNS_eQk-hkl3pwznxHKeL64CumbWtDvI9ydVQPrWUVu5qDgJ2dO_UkJpZuaH4pKDHwCYs_Y1o8fjfTNcfafJiBQ-o8vUYMZNpyIfqEMi4U00FoOzf04tjjDX9gsRF0fcxyz9J-t_u5yK2n2AClWIGzwLn99_m4iVdVR2tvC5-TL-eCUAfImwVNutiP8DvR24NtX8Y0YlGyLqPjGcX8820DM6uGwN3hCTrA2NfMx76Nihem-MDMI8ZB4j-v78mFNHXtD06Ljr9yFXpa0Mg7syfDN72cYk6vormEXeNu6nfikNZJLSofD_IeRhWf6TAf6K9Zb-uGfyrxTbFSU2HFpesUBwggN1hajpILsBSGfo7jgeVkjYRBg6Vp6lMiCUDymw8a5HjxoiLpfMygMQl3vMVwItcuWZs59IJMIxd9Xmd8wKkCFb070AEy-smMzgj_9ZCoVXm232va4rO_q99YP8W4X9qd-6ZGqZV8uMFeNT0p0-CKiboR1ulHYtao3OWNuRa8G4W2w01PgFQY0JOxXA_RT62wYD0bE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d8215d3c.mp4?token=R_SBVVIsqdyUzYIfjUCL0kMBm2pIdIT-_sKbBQ72oUK5PjjH0BKw39onV_1hu44JX59ZW1OrsGXwwIMRACARXU7w6QFmvWyxmU-XeSkdOFTxJZeoZTCuG0m4U6ibtGmTeAlrjZnD81GjYNS_eQk-hkl3pwznxHKeL64CumbWtDvI9ydVQPrWUVu5qDgJ2dO_UkJpZuaH4pKDHwCYs_Y1o8fjfTNcfafJiBQ-o8vUYMZNpyIfqEMi4U00FoOzf04tjjDX9gsRF0fcxyz9J-t_u5yK2n2AClWIGzwLn99_m4iVdVR2tvC5-TL-eCUAfImwVNutiP8DvR24NtX8Y0YlGyLqPjGcX8820DM6uGwN3hCTrA2NfMx76Nihem-MDMI8ZB4j-v78mFNHXtD06Ljr9yFXpa0Mg7syfDN72cYk6vormEXeNu6nfikNZJLSofD_IeRhWf6TAf6K9Zb-uGfyrxTbFSU2HFpesUBwggN1hajpILsBSGfo7jgeVkjYRBg6Vp6lMiCUDymw8a5HjxoiLpfMygMQl3vMVwItcuWZs59IJMIxd9Xmd8wKkCFb070AEy-smMzgj_9ZCoVXm232va4rO_q99YP8W4X9qd-6ZGqZV8uMFeNT0p0-CKiboR1ulHYtao3OWNuRa8G4W2w01PgFQY0JOxXA_RT62wYD0bE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
آشتی جالب هواداران نساجی با مجتبی حسینی سرمربی تیمشون بعد از فحاشی اخیر به وی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106233" target="_blank">📅 19:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106232">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gp6gJhtgz1OVdwwFt22Gx7hepGogV7dM6JAGOEYyLQ5tqUChXWrXaelAMh3SMuLki_IRN8uOyZ0typ68fUCk1McKNrzLEq4wqmjromWC1CSpuuFleBJoUkShm2A86s-qiIMrHFaZxv-1KrWTecNRVWmENI-ksYC2DuECxXfM_rD5BJGWgZDZcme-2vP5pFasWxmya3qvBI96lytHRcGmLBpgNuDfx7DHwi_5IhRpyAZnijQHrcMUXa-ZPlRdwwzJwacQR7UM0wW1PGlL0stiJ-QHj7_Dmixtdkqv-ePxANFQdi2KbtN57o15NBpT0q9VyT01iRdsLqAilt2LfNtZcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🇮🇷
طبق پیش‌بینی‌ها، یکی از پربارش‌ترین پاییزها برای ایران در راه است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106232" target="_blank">📅 19:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106231">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be84e2f3d7.mp4?token=KVjhAoV715oLQ4q85fmlMHqX9F701dZZwTD_OYH7NiCv9e6WAheAsDB2kpWP8BnwI1tMQO2YceTsAq_0JXUoSuzNvXczj19Il79_U-c3gUU2w36ljmF146yI60BpFKuezM9QqRoL-TrZDbu06BKQ6pYpkdlAKJme4ks_x6LAoqtpf20hy4tRuRArwwSwf0q_VisYKkMPGNVDiDic73Hw6m9wMnGtwtHOsLNMoSWMIAgVl_Js7bN4vutdDf2K3yIaeX4L91iqhmdYugqwN65zsRu3cjMGEERAq7aS2I8aJFs3moULk21HXXl8IfJLOJ4h4t383SnHPxmqhVLWFFOlLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be84e2f3d7.mp4?token=KVjhAoV715oLQ4q85fmlMHqX9F701dZZwTD_OYH7NiCv9e6WAheAsDB2kpWP8BnwI1tMQO2YceTsAq_0JXUoSuzNvXczj19Il79_U-c3gUU2w36ljmF146yI60BpFKuezM9QqRoL-TrZDbu06BKQ6pYpkdlAKJme4ks_x6LAoqtpf20hy4tRuRArwwSwf0q_VisYKkMPGNVDiDic73Hw6m9wMnGtwtHOsLNMoSWMIAgVl_Js7bN4vutdDf2K3yIaeX4L91iqhmdYugqwN65zsRu3cjMGEERAq7aS2I8aJFs3moULk21HXXl8IfJLOJ4h4t383SnHPxmqhVLWFFOlLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
به مناسبت سالروز واقعه ۱۱ سپتامبر یادی کنیم از همدردی مردم شریف ایران با آمریکایی‌ها؛ این درحالیه که کشورهایی نظیر عراق جشن و سرور به پا کرده بودن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106231" target="_blank">📅 19:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106230">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URm56nhe7ooyqOZbhauxqi5Mc-cGW8Ayj9PCf1-p3w2ZSJ4m3ROj8Oa3gph1c-GMc6MK9i6hyaWiSl8__Cdl9VzzEFiha6--WkksYahMCQjjnTGlHLJfKJau-ZvlOksl9b0RcFoCoDzXaVQ_hKhD189AH0AhGWBJlEibRcd8kfGOstJfvQdn4cgKnPYbgKgfkV9gp1DDo63NrF_kQsjy51rMAKid263y-lCmE34xqc4Jg_GR_82ogwmhgHC2_Ge8n8OKGGAYgbL5wyYytZBVnDX7uOEQQIBGkyAWvCG827Y9L8UixdWI16wnV8hriYIcIEkLKeXXS5zSCNyCJZrH4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
👋
گئورگی گولسیانی مدافع سابق پرسپولیس ‌و سپاهان از فوتبال خداحافظی کرد. گولسیانی زننده گل قهرمانی پرسپولیس در لیگ بیست‌وسوم بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106230" target="_blank">📅 19:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106229">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNJEJ_5LpyraOn7FouifJ8BNnuXgHTnUyOx6gJIgk-4-wjRi20VLO3gWVVaVq-PP8_y8fur-G4VfcETC4gSRcWnGSVD8xJxg-k6ysvria9mrvGc461TOnjfxEEr4uSYewYTFHXnOQcCfYCGlcRXCPogl3pahLHeCgNRlHJEutaN0ydRjxBZskrb_tUBPoPdm1f_Jxo52O2yMGUQYQW0g613lHerba_UBJa9ST6-EqWnZa_Jcl1nYLdhMChjoFpO1VYHnVaNJ2_FUTlKiW1IZuwmI-ldIdNlc4SdqKUVWt7btQ4YsEc_z1lII_r9mx4JEERln3x1OvrP2bDPvTPguEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🔥
🔥
🔥
اکتبر خونین که در پیش‌داریم!
🗓
🇪🇸
🇫🇷
20 اکتبر/بارسلونا - پاری‌سن‌ژرمن
🗓
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇩🇪
21اکتبر/آرسنال - بایرن‌مونیخ
🗓
🇪🇸
🇪🇸
25اکتبر/بارسلونا - رئال‌مادرید
🗓
🏆
26 اکتبر/اعلام رسمی برنده توپ‌طلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106229" target="_blank">📅 18:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106228">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106228" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/106228" target="_blank">📅 18:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106227">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VliDEZCNJZXcgt5wC_bpFUo72XloO4sOwIHDSq74PULqnRY1-PPeiuckX7MqBcVe4Ti-a-1CEdcjE7ECdwzXt1qwg9BcUTEteos4B6qjmDBOrnRRwsppgpKiHAWcD-7NGIrjZLxx1xGNZwP2QQ-c02aiW003wTSTOoYYuHFp8wRIgd6HeqhlTueny8R_gY1WFePNvQHsmJhCTXAuHV_GRfDaCUlWPzLd3LgDTWamp3sNEUL-YMt2ZW63ibWZx1LRKmegoF7d8-I_h_maAzOe6B5lsdFsjS0yAQaYy9kQ4iCWTh-WEN6E7dL3BRSSqmwKkUPnaNcT1VFV_UL7kkaEug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106227" target="_blank">📅 18:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106226">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2YLmWotD85HHpPyghyeHUl2U7sRkYAevwbU4S5LG6_HZaFz2dySck2ZbjExxy8m3ol_gwaeihPywi78JSZWhtLmU7v__HbeK-Uc11H4W5Q01WGva-P-map65V4rvXpYUc5rLJzvHpvDIo605QNdR3rHQQyj1rv95x8IUeySoJkBm_k5pnMjqyiUfdc2nkM2i6K6S6B-q4zgV_SHrsFxd7Wv3_AxULVxPI69idXUgItWpCr8U3ip2r0LuHK8ANGE7cHTVlM2GnN7MUTQaC5-PR6wqSNYwyfcNoxnqUQoxqInfaDQcxaM_bVQ1VHewbNfOIy4BoKz3sRoZj3Sihnw1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇺
تیم‌منتخب هفته‌اول لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106226" target="_blank">📅 18:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106225">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e1c6bb479.mp4?token=JNKlsV_E_reZvEglkT8wprxJkYvGXKQ68q7lW-3i7DshqyJzWHd_Rk0spzVnuR3gSkSxqupFxF8WbIHYwVt9Gf6D_XjjbGl_oUSgoPcnAaWPPZM9Zv1JPPOUKbkrycB8b0jrbMRyQ9dRapxlsCeFWK9Kdjm3MWhH3NM1zmMZe0JGsj4dO3gh15ELeq0WTmWc4ZdMZObNVSYzJt023qhZmF8tTXfYheQJnXTFQ4P8diVpZVq45Op5jlNO8V7LEx-ZeP-lRHZ8ZsArXFchXu7DwudiZRE5DC-Vj4Tho2vO3vHHI4yu-LKmD6elWjwjTw6ESgtTE2xzX1Nbb8aYaAXYaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e1c6bb479.mp4?token=JNKlsV_E_reZvEglkT8wprxJkYvGXKQ68q7lW-3i7DshqyJzWHd_Rk0spzVnuR3gSkSxqupFxF8WbIHYwVt9Gf6D_XjjbGl_oUSgoPcnAaWPPZM9Zv1JPPOUKbkrycB8b0jrbMRyQ9dRapxlsCeFWK9Kdjm3MWhH3NM1zmMZe0JGsj4dO3gh15ELeq0WTmWc4ZdMZObNVSYzJt023qhZmF8tTXfYheQJnXTFQ4P8diVpZVq45Op5jlNO8V7LEx-ZeP-lRHZ8ZsArXFchXu7DwudiZRE5DC-Vj4Tho2vO3vHHI4yu-LKmD6elWjwjTw6ESgtTE2xzX1Nbb8aYaAXYaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
پخش‌صدای بانو هایده در مراسم هفته‌مد در نیویورک آمریکا؛ روحش شاد اسطوره
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106225" target="_blank">📅 18:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106224">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8904bfcc25.mp4?token=X7BxrVAcK9HF989Wt_cvUicgAxZRT46kGipQzpW99tqhwWrgheE0cQ1ML6NpC8IXUQ-WFHW-_8OIuRf-5auF02kFUbowYn9sgE0EzMu1QwslA952lvZeIKdL7sEimRNxgFfSFyViEIn85s8VJ8j2auHfFoF5WtW3jU6MNLG2fp3vTH_wzsSw8dxM9RsKO0s4fkiwyCHgmxYUqfEUjmC4EbxptDtueGXEOZCN61SQs_Q52UHMLdPk4GijcmnUbCz-7nZ0vfitpa-_6kmbavi3eawk3JK8WBrtriwyYaw93MEsw833HM77R_xV2Qe8tP0zv07OpvdBdmH4xxkye5jMEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8904bfcc25.mp4?token=X7BxrVAcK9HF989Wt_cvUicgAxZRT46kGipQzpW99tqhwWrgheE0cQ1ML6NpC8IXUQ-WFHW-_8OIuRf-5auF02kFUbowYn9sgE0EzMu1QwslA952lvZeIKdL7sEimRNxgFfSFyViEIn85s8VJ8j2auHfFoF5WtW3jU6MNLG2fp3vTH_wzsSw8dxM9RsKO0s4fkiwyCHgmxYUqfEUjmC4EbxptDtueGXEOZCN61SQs_Q52UHMLdPk4GijcmnUbCz-7nZ0vfitpa-_6kmbavi3eawk3JK8WBrtriwyYaw93MEsw833HM77R_xV2Qe8tP0zv07OpvdBdmH4xxkye5jMEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇺
برخی از اتفاقات هفته‌اول لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106224" target="_blank">📅 17:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106223">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3be86e9eb1.mp4?token=pvoCg3sOJVORth8l0UNvt-ecDd770BqHobxnOkSyYjXHdrKhoTD3805gk0PRsZIJYPY0OmPo1urY8L7QMREMHsrW1JBZYu87YGEiYE-Yrxamk-E1-OO67x6slmhBLxkkGDcJIRiRtVGnwTUP3ZT9w22y57Z-kya5yF5mDi74OA9SvgPDcLFnxp-TvhUunU72M_KbHz7OPS4ql4ojSdCSzwh9t4ORudFFj-Q2zpbRwHYbIEk7ExtCX-nmPbSlNQjORTNlsowNagOwL0pVhCuyP0kgkcDub2LeZeRJ-eSZjQdDgAR_ob9p7zuWlyB5DytVXa123aScqBfwqcd-BrQA9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3be86e9eb1.mp4?token=pvoCg3sOJVORth8l0UNvt-ecDd770BqHobxnOkSyYjXHdrKhoTD3805gk0PRsZIJYPY0OmPo1urY8L7QMREMHsrW1JBZYu87YGEiYE-Yrxamk-E1-OO67x6slmhBLxkkGDcJIRiRtVGnwTUP3ZT9w22y57Z-kya5yF5mDi74OA9SvgPDcLFnxp-TvhUunU72M_KbHz7OPS4ql4ojSdCSzwh9t4ORudFFj-Q2zpbRwHYbIEk7ExtCX-nmPbSlNQjORTNlsowNagOwL0pVhCuyP0kgkcDub2LeZeRJ-eSZjQdDgAR_ob9p7zuWlyB5DytVXa123aScqBfwqcd-BrQA9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراسم تشیع جنازه بابای مسی با علی‌آقا دایی
😂
🚫
با صدای کم‌گوش بدید فقط
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106223" target="_blank">📅 17:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106222">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8jduY8N4wIVfp_Co9301ycYNCYHDp0ztMsGvOxIjTl_0FLD72mCmdjtDVd0sYerhs6snw7qPetsS5iX_Ge9m3lNI3o_6hn7CR6oC2UsJA6fXGNQPnxY6C0p3aSOFeunpm915Ze9EcbLEM_y5UVKuhJp7Fl4favTwAXq51YvBx_T73m-sVCpKSLsz-lYPa2_Dz1I2PJ8izfsJ9G8b_P4r5usKwr-fwNfhAP6DwW308-7VplgHbGC21xG7fqsJJcS_zW2XhLoX9RH9jnPR77Ljs7_xYfi130OwPChKZyF0Q7it7SPjRGC9lIj4nGQWhYTaBSxe8r45xWhU8CIjuwBcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
واکنش علی تاجرنیا به بخشیده شدن صالح‌حردانی توسط بختیاری‌زاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106222" target="_blank">📅 17:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106221">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d24125c19.mp4?token=RDs_PAWMpxuu25pcW5AS5Q-MeosjQgqmltsWUo7Tx0YwC-dkHJnY6CFRDTNyFs6TuASwr6dSH0yYSbe3nqKlZUxzW61iHyGxGlC10QZAXCdZmdBOXDncMZW5ihNLDMypUMGIl8pOLxldhCMtVKFViG_ii0Gi3D9Z0aeoOqCgOTd8wJQwQHsLQgl8ir0iOgbBVyXHaD_oMK2Cjg0Bzg5U9QYkL-XfEGbMTytUIC4sRMNhVzKDIrnsTrIDVafelQUClU-0Ou-EieusO1P-OG_BNNoH1MrpgDFwzuVKSuGNKYOZWD9LngFFd2yIwcVj_jJ0qw_zjVmiTGoADcciGQ1sEHj84RPrL-omVmcQwhiL1gSgUWTXNN5WWd_HvaoeznxTKnSiAIEFCMtyZiHhl6eE3E6IrSKvGmu9bOUK4h3EdGwo-7Pe2E0tqNsjrJ3j0PjKHDMBCYmspl2Ae8NWTB8jy21-bFyhfIP5Uvvwka6lv4rVP7GOsSYVwDLzshVLmeCU27TAksYhpp6P6_LBtjcvJrsCkr3up_19Nsg7cpn7CiXc38k0PeqvuFBMBGKKhuhDZeqO4jkXE79yziGPJAvmP17fwHTpsesM88ehpCmDKf1lDawgQiIrKLcVWr-EqKEUzyySYQRxeSnm13h0TewwN9f9a2KKiZhINXlx-OCN2Kc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d24125c19.mp4?token=RDs_PAWMpxuu25pcW5AS5Q-MeosjQgqmltsWUo7Tx0YwC-dkHJnY6CFRDTNyFs6TuASwr6dSH0yYSbe3nqKlZUxzW61iHyGxGlC10QZAXCdZmdBOXDncMZW5ihNLDMypUMGIl8pOLxldhCMtVKFViG_ii0Gi3D9Z0aeoOqCgOTd8wJQwQHsLQgl8ir0iOgbBVyXHaD_oMK2Cjg0Bzg5U9QYkL-XfEGbMTytUIC4sRMNhVzKDIrnsTrIDVafelQUClU-0Ou-EieusO1P-OG_BNNoH1MrpgDFwzuVKSuGNKYOZWD9LngFFd2yIwcVj_jJ0qw_zjVmiTGoADcciGQ1sEHj84RPrL-omVmcQwhiL1gSgUWTXNN5WWd_HvaoeznxTKnSiAIEFCMtyZiHhl6eE3E6IrSKvGmu9bOUK4h3EdGwo-7Pe2E0tqNsjrJ3j0PjKHDMBCYmspl2Ae8NWTB8jy21-bFyhfIP5Uvvwka6lv4rVP7GOsSYVwDLzshVLmeCU27TAksYhpp6P6_LBtjcvJrsCkr3up_19Nsg7cpn7CiXc38k0PeqvuFBMBGKKhuhDZeqO4jkXE79yziGPJAvmP17fwHTpsesM88ehpCmDKf1lDawgQiIrKLcVWr-EqKEUzyySYQRxeSnm13h0TewwN9f9a2KKiZhINXlx-OCN2Kc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
یک‌دقیقه با کورتوا بهترین گلر فعلی اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106221" target="_blank">📅 16:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106220">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0df98090f.mp4?token=psw00VhHxpJ_Aw0GzA3tb6ocpNDgMEcRoN3nxMI3SaueavD_KK_7lmgsRl0250sNO_NWu5yAMwyPODjGnoUYwOO1vmOtQeBh5dWE8CPJarPSuE-9rG8PxkMKl4YiXtVIcu3RgNtXJoS43_5x2jKcbEQiDD1rtttU8Bt2g_pIIg7H5zRgB3MnWnISnATIqRqq39IYAoHHmJcknKbKB2OEFLWr6ZNDkWVgAI60GS0-wbO7aAtX1uwai9QXzo-zW0uvoj3PKpHRACWY1RAvxjfjJNuTgzTGnAjh3m5mrZSo9U8EQQ8EJ56_zOMj3cg-qpsh1mIpw6CEuWEFZOy7_BJAwAGHy0bsosiYtQMRMxzGI8J0rPpPilQ3aUMCbflEg4OsG8Mx6hCqVVRe7p9VwNytzxk8CYYmrpPL8UcMPDuXA_a4P6XuyQm-yC7zZ6hWscIeuOgUoKKeaVMJIpZAW6bNmun0l70jyWcwi6FNZv3aoPMMY46G9Qju2dEALWLqzVWfywIYp1WeBl_lPObpvfQ1-m3bmAgBlpFelIyFgq1fnbD9-7LhRhbIekGKrQ5qIld4UkCgW_4Bz4mKJrMiL1Lzqu1AB89M-sry3aUL-1Z-gXqaaUzRQ9SCYiAe3hEU3OQQbv2FF_YwaKjlpwc77IsLggwBC47p4iOopxB3LOEpXTE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0df98090f.mp4?token=psw00VhHxpJ_Aw0GzA3tb6ocpNDgMEcRoN3nxMI3SaueavD_KK_7lmgsRl0250sNO_NWu5yAMwyPODjGnoUYwOO1vmOtQeBh5dWE8CPJarPSuE-9rG8PxkMKl4YiXtVIcu3RgNtXJoS43_5x2jKcbEQiDD1rtttU8Bt2g_pIIg7H5zRgB3MnWnISnATIqRqq39IYAoHHmJcknKbKB2OEFLWr6ZNDkWVgAI60GS0-wbO7aAtX1uwai9QXzo-zW0uvoj3PKpHRACWY1RAvxjfjJNuTgzTGnAjh3m5mrZSo9U8EQQ8EJ56_zOMj3cg-qpsh1mIpw6CEuWEFZOy7_BJAwAGHy0bsosiYtQMRMxzGI8J0rPpPilQ3aUMCbflEg4OsG8Mx6hCqVVRe7p9VwNytzxk8CYYmrpPL8UcMPDuXA_a4P6XuyQm-yC7zZ6hWscIeuOgUoKKeaVMJIpZAW6bNmun0l70jyWcwi6FNZv3aoPMMY46G9Qju2dEALWLqzVWfywIYp1WeBl_lPObpvfQ1-m3bmAgBlpFelIyFgq1fnbD9-7LhRhbIekGKrQ5qIld4UkCgW_4Bz4mKJrMiL1Lzqu1AB89M-sry3aUL-1Z-gXqaaUzRQ9SCYiAe3hEU3OQQbv2FF_YwaKjlpwc77IsLggwBC47p4iOopxB3LOEpXTE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇮🇷
واکنش مجتبی‌پوربخش و علیرضا مرزبان به تصویر تلخ دستفروشی یک‌دختر خردسال در استادیوم اراک!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106220" target="_blank">📅 16:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106219">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6ANU2-kyxp-oxUVoGEpntamnWrdqSZok76D2u92h84R8oo09qa92TSZVXDj1TfpWrl3ccTiepWGTE-tljB2Ii_Cnz0zPYvsRoxW3EZ8bqi7f4S4MSUInSdrKhLz7QfzhDxLciOOdonpenZSnJIGJus6RccERcnUU3SE3HAqrvN0lCQpx1FUoHcL8qoD_lELA-barf-pQVeYabE2vMgeW0qv_Xm5mC7S1Q8bhM_kQeQ3mrzkCeWzuV7Rh6JfhS87UkDqsG_jnC2S5Fq8bkc7t_6WRYUUR-yqMjyfi8tXTkQassd4jbdWIf_R219TTVSs6k5-povPXWiiLaIUvCqLaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
‼️
📊
🏆
سوفا اسکور: مقایسه میانگین نمره رافینیا با نامزدهای توپ طلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106219" target="_blank">📅 16:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106218">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kth7B57sV-h_kMvnKBBJ6ghtlqmcPeHc9BLQW2dZmn224572_yK0NiGol_RMVYzFal6hP3GvfHNrsubnVCtHEaT-wBJzyA3uvY5yPsundCwM-d2LW8w-bXMF1LxyP3MzievyX6bEj6Envc0ZQDQIoYH7yr1E8v6JhOvanJSmb9ecH5VAcZ6_dMvCEc7P_v7w3g_-ti8Y0n3UqC4aPFVNNccSJeIS39VpaLRzokS8I8rsKyu6t5qszLhyRk7uzH2h-eVy-Sd32Uf8SpzUAEhfKRuVIikUzad-_6Y3CMXbAiykP2YWr5z5nmV6H3EGtBkKMKWwZZu0ckc8KSKIPLnW8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🤯
امار و ارقام لامین یامال در کریرش
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106218" target="_blank">📅 15:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106217">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88e638c5ef.mp4?token=c7-ozvUJ9uR9ZmQpL07alevuQstbMoD15Juq2QooF1GfGgFO9G_4nSK20PoX0qh9t1qZA1aP5Uvw7rviTVJAT0vjAoOP9969H03gj_FSoH2bEiO4sLnohTSK4f-rtwbR9WRc1IrhxTySm2N-7KbXdwI0NPCHeYI9god8GnTlPHF9qwY4rOS-UjnufpKqmi-fW5PqiMSezzzWeZyY8vWzJGmxAmuyB6VlRu1mkDFmbxR7X3POO9NuCFekSV84XLwybksa8vsl_Kg2gKn0cx00caiCfoniPv3M2jg0JNndO8xau-OF6L1nxZgBWpEVIHLpIKyH3_ShgJaoBDXOL6rt_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88e638c5ef.mp4?token=c7-ozvUJ9uR9ZmQpL07alevuQstbMoD15Juq2QooF1GfGgFO9G_4nSK20PoX0qh9t1qZA1aP5Uvw7rviTVJAT0vjAoOP9969H03gj_FSoH2bEiO4sLnohTSK4f-rtwbR9WRc1IrhxTySm2N-7KbXdwI0NPCHeYI9god8GnTlPHF9qwY4rOS-UjnufpKqmi-fW5PqiMSezzzWeZyY8vWzJGmxAmuyB6VlRu1mkDFmbxR7X3POO9NuCFekSV84XLwybksa8vsl_Kg2gKn0cx00caiCfoniPv3M2jg0JNndO8xau-OF6L1nxZgBWpEVIHLpIKyH3_ShgJaoBDXOL6rt_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
از مالیدن روی آنتن‌زنده و صحبت از قناعت تا عروسی سوپرلاکچری سامان گوران مجری صداوسیما
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106217" target="_blank">📅 15:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106216">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/225d461ea8.mp4?token=AnBTAfQKYgwMxVI6rYOWJy2nfyPlXPRO5HM_gPhjZ7qf6Lbit1vzIMXyRbEGlUC9z2ADOEdx0FuIrP2JtAzJ2BXY20ycak4q9jBOzTm41M_3LEbt0CqOrR58u9oqrZ2Y0rFch2oHxcOTgDkRF8156LOtqiS_q6h__7E-xu0c49am_CWz2xA0exST7-G1kwMZRfR1H05JK-XsSPWip2saD8mKAiXp1M-jKWZc_9q4Shzp8Nkr5g-_4evUKdxJysZPA61VmiCvRhcjZmVsto8jfPt24ytSmZKpzH-ZszfWiOTieQF4Brk0-Ojx9QioJTn3rdNSTWobgTnB8yIZkGVNSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/225d461ea8.mp4?token=AnBTAfQKYgwMxVI6rYOWJy2nfyPlXPRO5HM_gPhjZ7qf6Lbit1vzIMXyRbEGlUC9z2ADOEdx0FuIrP2JtAzJ2BXY20ycak4q9jBOzTm41M_3LEbt0CqOrR58u9oqrZ2Y0rFch2oHxcOTgDkRF8156LOtqiS_q6h__7E-xu0c49am_CWz2xA0exST7-G1kwMZRfR1H05JK-XsSPWip2saD8mKAiXp1M-jKWZc_9q4Shzp8Nkr5g-_4evUKdxJysZPA61VmiCvRhcjZmVsto8jfPt24ytSmZKpzH-ZszfWiOTieQF4Brk0-Ojx9QioJTn3rdNSTWobgTnB8yIZkGVNSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
▶️
حس‌واقعی هنر در ایام‌قبل از انقلاب با حضور ستارگانی نظیر بانو گوگوش...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106216" target="_blank">📅 14:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106215">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2irbqJ6dm3V7E3l8atHQxS8u3FK44Zmc6uYwm5AoAt9b89S2TWIct7pWogFSQFJ7znxvlGw5xJYe3GFyuUUs5eLr-7qSBSXLuJnJk1vKRnpQbKJyXcKHsu5Tt6P1V5M6yRn6o5S98vegCLL4vp0Yot8KS2uGUzWLo_FbuCRD1BOY4vXULoL2kRXYkVaiaV6KEqXhmjFzRct9iSa_jTQlG4o90Wl3APWsFeoL21LyIeBweg6zRMRNJef5Yt07G5eFAzloWYativaIud8qSgKQ3Iod7kfR-I6go93UNtsZaKQJDTbsYcyed9vdwsoRlBVHADJWr_dsdQELcpGgCs8ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💥
🇪🇸
عملکرد فوق‌العاده رافینیا از شروع‌فصل:
🇪🇸
الچه
⚽️
⚽️
🔴
🇪🇸
بیلبائو
⚽️
🇪🇸
رایووایکانو
⚽️
⚽️
🇪🇸
والنسیا
⚽️
🇳🇱
فاینورد
⚽️
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106215" target="_blank">📅 14:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106214">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e2cd36180.mp4?token=dwgjocTWZsMoMigas1p44snyxg8v6zgpdYXnLa6fiwAXG_nn-CT1M_GttIpLB15i-PUf9Axl-NigizARuy_mD7r9roKfV1iSDIRJH8BRUeta13toJEeNdBdoyCwJzk82i7iKl6VINOdSgZ6lwKCXryeBwdFxXx0_Ox9IxLAHxdRM3D7PdJJ_k_M3fCxVh7z_Ue4061DDbti9dnLw1tRhU7xQ_1c631s-s8ZeyXrQBwP8c5zdsAX85gz846sVCCss3jxvDNQ71L4c3U0MDi9i7W_vVBGCNaiygsubhNQ4TInDgBh_5RwGDCcvQypebIzGjANoG3elweJep0L-2A_SIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e2cd36180.mp4?token=dwgjocTWZsMoMigas1p44snyxg8v6zgpdYXnLa6fiwAXG_nn-CT1M_GttIpLB15i-PUf9Axl-NigizARuy_mD7r9roKfV1iSDIRJH8BRUeta13toJEeNdBdoyCwJzk82i7iKl6VINOdSgZ6lwKCXryeBwdFxXx0_Ox9IxLAHxdRM3D7PdJJ_k_M3fCxVh7z_Ue4061DDbti9dnLw1tRhU7xQ_1c631s-s8ZeyXrQBwP8c5zdsAX85gz846sVCCss3jxvDNQ71L4c3U0MDi9i7W_vVBGCNaiygsubhNQ4TInDgBh_5RwGDCcvQypebIzGjANoG3elweJep0L-2A_SIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرمین یا بلینگام؟‌ کی بهتره؟
👀
⁉️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106214" target="_blank">📅 14:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106213">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ol_imBX8xhehwAP0lBc3jyH0i8uPicsqny9mBLQCEgolEE1ASqOCWZDFJZKBbaniaiDUrMkVcFw2PYVc-0p8c8w4yaIek6BzH15dOxLcCaoselbt6NCu_y6MrcZ5E9dkJpJMJGWj8IYSBgL4UJINAp5Be0TOzADWFiie0KcngxnJsGMKjoPW_HeZqcV0_TvVdwWaCiwC1nh4YnHIttRWm6HxEQAhDv2RXbRm4QWijzShldtR45I-m_pyCuzfI-BisuTU2n914dn_2TC52gv6hapczimcOE5YRz4VVm8afixrrT9nPSiL09iBbU7tnZm7sctY6-Uj2IFd8yQtc-8z5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد درخشان مورگان راجرز در چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106213" target="_blank">📅 13:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106212">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4258e2b29.mp4?token=ZpDi6BcNhv6m4JN8YfUOOQu8Q4Wh6GcxqQ_Pp2BBOFSQWzvpp4rLlJsabcvQs3_bQo_A_aLx6X_U45WGVFZDTwcFNrBwhpA4iGT2BdhJAh-iQ2BGJ6IxUaMqio7ChIUQtGR0YYwqaE9sY9igpaA-dftMiNq6CG9TqWVRE6sum6svTD3WNwOD7GtcYONhCQv47DbtURV5XCs9ibsHBEXplLpIYIB_XSL2Qq7kvYQZG4ZjUBJA7rtZTDAIws6dXjVBb_dikDNgX3F42bfMO2zwpF63RL6EYHQsTWf2Z9pjX-phli4qduGdfYbwjop880v4cXITv96fa8PlBinBnj4jlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4258e2b29.mp4?token=ZpDi6BcNhv6m4JN8YfUOOQu8Q4Wh6GcxqQ_Pp2BBOFSQWzvpp4rLlJsabcvQs3_bQo_A_aLx6X_U45WGVFZDTwcFNrBwhpA4iGT2BdhJAh-iQ2BGJ6IxUaMqio7ChIUQtGR0YYwqaE9sY9igpaA-dftMiNq6CG9TqWVRE6sum6svTD3WNwOD7GtcYONhCQv47DbtURV5XCs9ibsHBEXplLpIYIB_XSL2Qq7kvYQZG4ZjUBJA7rtZTDAIws6dXjVBb_dikDNgX3F42bfMO2zwpF63RL6EYHQsTWf2Z9pjX-phli4qduGdfYbwjop880v4cXITv96fa8PlBinBnj4jlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
ویدیوی وایرال شده از تجمعات شبانه:
«تو تاریکی می‌شینیم، ذلت نمی‌پذیریم
بنزین رو کم میگیریم، ذلت نمی‌پذیریم
دلاری گوشت میگیریم، ذلت نمی‌پذیریم
مهریه کم میگیریم، ذلت نمی پذیریم»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106212" target="_blank">📅 13:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106211">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62e4095a95.mp4?token=UEpOxMc-W9__mcy5xi0EHVoJjhBzxVlyC0GAM0gGRq2TY2pr7fKfHcuxwI3ClcxFxltkG-IBVuXjFL36c0VLS56t_iaRI4NRS2dP_CMVJ28qADi9Fx34BXqcxItKDmRl4NJFmp63vK55XezTVoa_mREHvieDvmv_yX_0jkd5Tg2JlonGji2pguMMUH6saIgloqUBVxsWj3zyDJskBTCI03h5JlYMCmNC48Qk0hu4Or7PWhRUzWyrdL6psU8chEeqPtGWwTgw3qu6dNqGK7AxlUFONt77q31B0YpsHG_xScZLF6coSzSuuk1QbnTXTmB-rEW6WDnLeKK4N1UnZDDr7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62e4095a95.mp4?token=UEpOxMc-W9__mcy5xi0EHVoJjhBzxVlyC0GAM0gGRq2TY2pr7fKfHcuxwI3ClcxFxltkG-IBVuXjFL36c0VLS56t_iaRI4NRS2dP_CMVJ28qADi9Fx34BXqcxItKDmRl4NJFmp63vK55XezTVoa_mREHvieDvmv_yX_0jkd5Tg2JlonGji2pguMMUH6saIgloqUBVxsWj3zyDJskBTCI03h5JlYMCmNC48Qk0hu4Or7PWhRUzWyrdL6psU8chEeqPtGWwTgw3qu6dNqGK7AxlUFONt77q31B0YpsHG_xScZLF6coSzSuuk1QbnTXTmB-rEW6WDnLeKK4N1UnZDDr7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🙂
🇮🇷
نحوه برخورد شجاع خلیل‌زاده با مدافعان تراکتور: حمال‌های بی‌خاصیت
❗️
❗️
❗️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106211" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106210">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106210" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106210" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106209">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vss3qEKxMZ10tHJFlc3a4q0PSEMrZd8iUL2G5tajARj5hpq-0C11xG_8yzd6GawvnSpSjgWJ6bi5WqGoHL-1Qy9R0pHwjNnZjOLldGDbFqfLpu881Z6R9_PgR3ROIDtTuMu_59ah1Jx22wcKYssmMigVPvCZ4fFNHxQbadpFvMI7ClHX4itRLrymfcr2bIeV9v9LroNQ79puCM6QAhc3O9lzrwoV6-JIb3u52FlfOA-n2QHxt9034a_foKQJ0e3uySiUaa-BXziMdzcHzJMxHcgN66sHjbLaLRtRcTd6ov9DZ0xObpQWh0G0nvEX6p58vRyJpJ9pDtlo7G_fCFn-Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
والنسیا
🆚
سویا
فیورنتینا
🆚
ونزیا
شالکه
🆚
انیون برلین
مارسی
🆚
رن
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106209" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106207">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👀
🎙
🇹🇷
اسماعیل کارتال: بمولا از ۵ تا بازی اخیر تنها یکی باختم اونم جلو بشیکتاش بوده. تو پلی‌آف اروپا هم لیون رو بردم و به مرحله گروهی رسیدیم. نمیدونم مردم دیگه از یه سرمربی چی میخوان. دهنم سرویس شده و قصد استعفا دارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106207" target="_blank">📅 12:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106206">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46400b9012.mp4?token=TwA5iCpMvTb6tYCp7F_0C-FeU0HzN_L1x7ri-18Dgf-eImdy6iTOyaS3lMXanZj3wDf8iTbrCuFBUCY-QziNKWnpVFA8CI1GZMHjDBgeYkB2WTgSI55We53IxTE6DFBCfy5i7pqk1PT6XH3kkHy5l_h6d4EJkTcuA066tuRde7_API8-IgQoOTFLFJAjbydd2OAT8u6rV0Gov1KiGmSEbKjr6z-zkaV9zjAmyoHg0SvKf-SforA02BtPwlKn8XGDkpbyGH1teFOjvs3CWaVji4ybaACzb-UfU5M6tLTrZvx8v5IWWUX4SJZyi4CnCf3Fqir6pMKTv0ITXoGdUIUq3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46400b9012.mp4?token=TwA5iCpMvTb6tYCp7F_0C-FeU0HzN_L1x7ri-18Dgf-eImdy6iTOyaS3lMXanZj3wDf8iTbrCuFBUCY-QziNKWnpVFA8CI1GZMHjDBgeYkB2WTgSI55We53IxTE6DFBCfy5i7pqk1PT6XH3kkHy5l_h6d4EJkTcuA066tuRde7_API8-IgQoOTFLFJAjbydd2OAT8u6rV0Gov1KiGmSEbKjr6z-zkaV9zjAmyoHg0SvKf-SforA02BtPwlKn8XGDkpbyGH1teFOjvs3CWaVji4ybaACzb-UfU5M6tLTrZvx8v5IWWUX4SJZyi4CnCf3Fqir6pMKTv0ITXoGdUIUq3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
محسن افشانی: اون شورت و کرستی که استوری کردم برای خریدن آبروی یک بازیکن فوتبال بود!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106206" target="_blank">📅 12:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106205">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abdf4b56cc.mp4?token=IIhWBVmeaxKyO8J1MejPwNsxiZCVjZEUc-D07Q_40h4WbhuJi5sFeP1JP3T1DgFd4l0RbospVdYOUVYtrjMEDKo0W0oiWSoIqg3BEDwlv57U04mnKjYZMY3pEfYGS51TrmRMwUsIaF5bsg2a9F1wFcLleqXl9G7r13PhaaeUhqFEFWY0vm3URPL619Z1WvEyMc5q1Cv5dNnFWw64_pvc454qhZThICpyGUzfkkTZ8ENHFlfD9rprPr9pB8axujDPOjbc4T8gypiMplLhlMUVLuMRdvBxOkuJMWXuCYv9M9BD4eu0VGZn_PRrSFQNerQG1kna9wpw4xOxZ2AEj8ayrlkJRW3gPEMjJVfJTrrcGP2UI1mO57sVwIMi0XTrVVSrpEkb4VqPhpRZahDwXodx9-u7DuN_9GVCcpndqBZGNA5V8bZYrVNW1LCl9ycUW5mJ-4PJcWlKaztZJDIYv0ekE8ZCRb_YLK9ak4jG0573VpaAmf4sCo7crGsTp2aRFQPhrwTpBOWYjTh9xqk7HvHRImqedquJsITPuTBOgqk_SxIjSjtxot3IFzi5Fh1UHUPWUBjUq2f0IXQRjj-hN5ST3UGbx1F5KXj9RI86K5MJTi9yb8faf0emw_jYtmFWMkbDaNvAVBq5EBm1q_CZgjwBA_dX8kCiX3WcwYbjtEuT3nI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abdf4b56cc.mp4?token=IIhWBVmeaxKyO8J1MejPwNsxiZCVjZEUc-D07Q_40h4WbhuJi5sFeP1JP3T1DgFd4l0RbospVdYOUVYtrjMEDKo0W0oiWSoIqg3BEDwlv57U04mnKjYZMY3pEfYGS51TrmRMwUsIaF5bsg2a9F1wFcLleqXl9G7r13PhaaeUhqFEFWY0vm3URPL619Z1WvEyMc5q1Cv5dNnFWw64_pvc454qhZThICpyGUzfkkTZ8ENHFlfD9rprPr9pB8axujDPOjbc4T8gypiMplLhlMUVLuMRdvBxOkuJMWXuCYv9M9BD4eu0VGZn_PRrSFQNerQG1kna9wpw4xOxZ2AEj8ayrlkJRW3gPEMjJVfJTrrcGP2UI1mO57sVwIMi0XTrVVSrpEkb4VqPhpRZahDwXodx9-u7DuN_9GVCcpndqBZGNA5V8bZYrVNW1LCl9ycUW5mJ-4PJcWlKaztZJDIYv0ekE8ZCRb_YLK9ak4jG0573VpaAmf4sCo7crGsTp2aRFQPhrwTpBOWYjTh9xqk7HvHRImqedquJsITPuTBOgqk_SxIjSjtxot3IFzi5Fh1UHUPWUBjUq2f0IXQRjj-hN5ST3UGbx1F5KXj9RI86K5MJTi9yb8faf0emw_jYtmFWMkbDaNvAVBq5EBm1q_CZgjwBA_dX8kCiX3WcwYbjtEuT3nI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
روش‌های نوین تیم‌ساکت‌الهامی برای وقت‌کشی! الحق که رو دستش کارکشته‌باز نیومده
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106205" target="_blank">📅 11:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106204">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/249d50f161.mp4?token=VFW4Yuxkc9jr0RSW_uum_bpQHalbYOjeyOmVabPfqtrQ1OS1BVYXra_1ML8_OpfQ3VH1eslytV2gCuKkiNx7hLBPYRKefWsqOntJUyADGa5aXE74w_N94Ig2okI8Vh2qzisEqNvDok1vY9FaogtUOzQHDHNTpyLhSNBN6LHL5-9J-ZES_wafvlEdVnSNIIX28-32dCQ7NAWL9YsX4RU9YPz4kVghUTzb-eyDjULlXyCc2XwYDk1J6YuFBWTu0UMx73Lh-KyYfrIeN2GFSNWEu2m6YmOC4jzUq7V_6XBCASrm5WYMzqUj9eEz0syGAfFHHV66XYgx_Ejp7w34igJiww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/249d50f161.mp4?token=VFW4Yuxkc9jr0RSW_uum_bpQHalbYOjeyOmVabPfqtrQ1OS1BVYXra_1ML8_OpfQ3VH1eslytV2gCuKkiNx7hLBPYRKefWsqOntJUyADGa5aXE74w_N94Ig2okI8Vh2qzisEqNvDok1vY9FaogtUOzQHDHNTpyLhSNBN6LHL5-9J-ZES_wafvlEdVnSNIIX28-32dCQ7NAWL9YsX4RU9YPz4kVghUTzb-eyDjULlXyCc2XwYDk1J6YuFBWTu0UMx73Lh-KyYfrIeN2GFSNWEu2m6YmOC4jzUq7V_6XBCASrm5WYMzqUj9eEz0syGAfFHHV66XYgx_Ejp7w34igJiww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇪🇺
پس از ۱۰ سال ایران در UCL نماینده نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106204" target="_blank">📅 11:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106203">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c7627bb5d.mp4?token=UT7qyqnnJLfcpIxl2oG4lOtHy52_05Fr12CjJi66_QmTZQw6pSZE6SBna7ndReAvDVNUUA7wxS3wLrmoLyj2L5AcA2Cfyo8vdavwtJA3H5X54jj2ldUq0_pGjlkBhqshuL9UGtaHkes7-EhmEbs8Sm9oLCnzHkXobBwaDdTaDQ6DG71h4kYkCQOVc7cErn5HA2soMHdut8z918JkzL0pqbiJo92vPJJKNfLMuMm08ZUu5rvaeuWRqWn81rpcYBg-97qxq1h099y4pgEUlE7by5aSJHMEL7hv09rS_hgZGaGcB44rI9yH5XMWQbcjfCII4i-ovWTgIWot4JOnY69qSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c7627bb5d.mp4?token=UT7qyqnnJLfcpIxl2oG4lOtHy52_05Fr12CjJi66_QmTZQw6pSZE6SBna7ndReAvDVNUUA7wxS3wLrmoLyj2L5AcA2Cfyo8vdavwtJA3H5X54jj2ldUq0_pGjlkBhqshuL9UGtaHkes7-EhmEbs8Sm9oLCnzHkXobBwaDdTaDQ6DG71h4kYkCQOVc7cErn5HA2soMHdut8z918JkzL0pqbiJo92vPJJKNfLMuMm08ZUu5rvaeuWRqWn81rpcYBg-97qxq1h099y4pgEUlE7by5aSJHMEL7hv09rS_hgZGaGcB44rI9yH5XMWQbcjfCII4i-ovWTgIWot4JOnY69qSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
⚠️
ادموند اختر :لويى ويتون هزار دلارى رامين رو با دو تومن تو منيريه مى تونى بخرى
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106203" target="_blank">📅 11:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106202">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/629b78a14c.mp4?token=ScI6sr2-dIE-QE_sCRahq2yWPzK6RKemT-u3Nzle9NpG6UF6ObNRHokkhgw9FQmSg7L0gLn-YoD7aOIUMrqLZM11imzk78SDkle9RUrKFGegByFtDdzScitPYyNBhr_CzjGOAMKzef8QPHH8N6veZlP9sMQYscyEXxFbWV0b3prIYh3LnJ639uda7dHmSjAnqHoUDn2Y7anEUh58b7-6CSHrjFeMkKQ873_x-HDHTR6Ut461ihwZ8eynnqMyhAdQvf06puRK4dBa18h0rWeS9NMKJ5_Wjy6_H9_ZHo1AXstbha9IraY9WdgimogXw2o7yukr6-QYPpHBDlY7xqZQIU7r2WqbzVsKFX9Qj3VyhbTHfZGxBydW1y3C7dD6BUT5woNBwn4r1hVrQqYGsjQnCq9S9G9FkCkK2DujENjJ_EU1ugRpPg_X0XMBdV9qiSTfbJseEQeJU4ociU7smmpvHyZ7K-w0mENNoOOeRW2ocjXsAQ8jzIcvLAu2SVJ3PNxIcd56F4pFT9S8XLFDidRjfrASl29WUNVuTZxJ3mq0NJaTD4ShWaUNWoa76hW18gFhNdVserYaEcDcIZpTZX5g0JRwK0kEZLfUs7w5g1pMkrVYCDXymRH-MEGUma8mYy_bdK_v5o487iGXvDVsU1wi5IADgQXDhfs_Kwg_PX__c7E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/629b78a14c.mp4?token=ScI6sr2-dIE-QE_sCRahq2yWPzK6RKemT-u3Nzle9NpG6UF6ObNRHokkhgw9FQmSg7L0gLn-YoD7aOIUMrqLZM11imzk78SDkle9RUrKFGegByFtDdzScitPYyNBhr_CzjGOAMKzef8QPHH8N6veZlP9sMQYscyEXxFbWV0b3prIYh3LnJ639uda7dHmSjAnqHoUDn2Y7anEUh58b7-6CSHrjFeMkKQ873_x-HDHTR6Ut461ihwZ8eynnqMyhAdQvf06puRK4dBa18h0rWeS9NMKJ5_Wjy6_H9_ZHo1AXstbha9IraY9WdgimogXw2o7yukr6-QYPpHBDlY7xqZQIU7r2WqbzVsKFX9Qj3VyhbTHfZGxBydW1y3C7dD6BUT5woNBwn4r1hVrQqYGsjQnCq9S9G9FkCkK2DujENjJ_EU1ugRpPg_X0XMBdV9qiSTfbJseEQeJU4ociU7smmpvHyZ7K-w0mENNoOOeRW2ocjXsAQ8jzIcvLAu2SVJ3PNxIcd56F4pFT9S8XLFDidRjfrASl29WUNVuTZxJ3mq0NJaTD4ShWaUNWoa76hW18gFhNdVserYaEcDcIZpTZX5g0JRwK0kEZLfUs7w5g1pMkrVYCDXymRH-MEGUma8mYy_bdK_v5o487iGXvDVsU1wi5IADgQXDhfs_Kwg_PX__c7E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
💥
یک‌دقیقه خاطره‌بازی با اسطوره آرین‌روبن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106202" target="_blank">📅 10:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106201">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c278d8437.mp4?token=bEDUYVC6rsG3XnAY1pSeWAhSBvtfxJ8N30FoyYQKjEAM3AOLsqU6-L7DlEpf-FS8mFD4jqjDygvagTNjUovqvKLYNB2FAvqvtA7jEcs3xp8sA77C_nbz9ZD507v2lfUxYA19ycwpCCoTVz8b6bi-PIyS4QmaI_UDpbASt3a0PCtcQAS7mpBU2OFr4RG_QcaeycQd-AhDqriyZxAHdDsQZI2clA_lRYHpD_6u_wCDAGOMKhlwbb9M7XP4oK0EejYFyx3Ptb10xcbVQGfOSyLlSWnT5QMY5Xa8LHSaWZ14Dhf_6C6nOkQQbG35oQJ4V2PxzTB9qrb_OEzm2Tn3sEy65w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c278d8437.mp4?token=bEDUYVC6rsG3XnAY1pSeWAhSBvtfxJ8N30FoyYQKjEAM3AOLsqU6-L7DlEpf-FS8mFD4jqjDygvagTNjUovqvKLYNB2FAvqvtA7jEcs3xp8sA77C_nbz9ZD507v2lfUxYA19ycwpCCoTVz8b6bi-PIyS4QmaI_UDpbASt3a0PCtcQAS7mpBU2OFr4RG_QcaeycQd-AhDqriyZxAHdDsQZI2clA_lRYHpD_6u_wCDAGOMKhlwbb9M7XP4oK0EejYFyx3Ptb10xcbVQGfOSyLlSWnT5QMY5Xa8LHSaWZ14Dhf_6C6nOkQQbG35oQJ4V2PxzTB9qrb_OEzm2Tn3sEy65w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💥
نیروی دفاعی اسرائیل (IDF) دیشب با انتشار این ویدیو از انهدام کامل تونل‌های متعلق به سپاه و حزب‌الله در منطقه استراتژیک علی‌الطاهر در جنوب لبنان خبر داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106201" target="_blank">📅 10:24 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106200">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsM2A3b3_Kl1LRXdp06bUqxhWB5W-Ab5Y6llQoVwLkXMjjyytEXgE73SsFBYgPLqYQ2yAgKziFM52Qs57tSANXAULx_vgBFpjKYRd6Ich1mW3GZ8w6kHGGtOQwdxSQy9R1jlJ3_hu9cvNbO09GGe7p-snYACeBn5bO42iVQv1gChFNQqynURVX5WlwzWH0ixweck_ohYaNbmkoY-DHveaTu_5C2jbJO0XDHJehXwXWVPgFUj567qaWTdn8VFJWZyPVm0SWvzyTK9XZspX81GhVWlgJSh42HXjjkiNyjgzN9ZCFkI9QQklMisgOV1_Oab0u6lCJODJsOrMQSIIk5paQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نامزدهای بهترین بازیکن هفته اول UCL
🔸
فران تورس
🔸
رافینیا
🔸
ارمدین دمیروویچ
🔸
مارک بارترا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106200" target="_blank">📅 10:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106199">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c20f0a6e3.mp4?token=c4giJN8Ikme2l-jTDOuqGer1pJXnDxmf4cd4ctcRvCyXZ6HlBVmrzIW7lZpfZbzDcwWxqrqYkdyvDp0e5Er5CP4J_MdyTsgQgfMhA9RT_Q7pwquDzbTN_2LGdd1C9MGjrtZXe5OW9ln1qPypaNYe08tEWaR0r8DMPMX_1WvrGRqpc4moK6gNtja1NBQP5zpVR5-RQMU_D_3bdBv2YvtrsiUuyDZ-qFCftu_jhnlmglBZCPJEFTc8hcJmBGNZSwqZ96Af58HtwBqnoFvtPaQFrpdyJ6_nKypC3M73fUaQwNPQpPTm8ZNHmAphu3LYpyhsS2Zl6Lb7ZzzO8drGs779uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c20f0a6e3.mp4?token=c4giJN8Ikme2l-jTDOuqGer1pJXnDxmf4cd4ctcRvCyXZ6HlBVmrzIW7lZpfZbzDcwWxqrqYkdyvDp0e5Er5CP4J_MdyTsgQgfMhA9RT_Q7pwquDzbTN_2LGdd1C9MGjrtZXe5OW9ln1qPypaNYe08tEWaR0r8DMPMX_1WvrGRqpc4moK6gNtja1NBQP5zpVR5-RQMU_D_3bdBv2YvtrsiUuyDZ-qFCftu_jhnlmglBZCPJEFTc8hcJmBGNZSwqZ96Af58HtwBqnoFvtPaQFrpdyJ6_nKypC3M73fUaQwNPQpPTm8ZNHmAphu3LYpyhsS2Zl6Lb7ZzzO8drGs779uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
ویدیو وایرال شده و دلهره آور از جنگ اوکراین ؛ سربازی که شانس میاره و از زیر تانک سالم بیرون میاد ...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106199" target="_blank">📅 09:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106198">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc5454d366.mp4?token=OUUmelOj-8GlY8PLkItun6Hw2pDVQFlsI1ex06H65TbvsB1WLcNFiU35PG1yXvMfaxl8gY1pEfKz8kK2Z--pWGhd0lBBLE7f0hFSAMHibrViF0lfItpDtFlaAg1Z1chWQ65J2f9DAYSOOFIAq7AbIthb8rtGLZE-cDGza8TGgT-H9-Gt35G5vKyMlv7OAj0iuNgr6LWmpWQjIGDsvqq7lgVtVn7eWesU0_mKTYJ0_xn7V8x8aEf4ANQbGawvrkuZxfB0jE7c6shcqXbo207vwuULIIE_1RTLl7B_L8Hi8CdZ4SOgYajIfApkV_jc1w8wlLCMdHlYJDoAnTAlJeLIAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc5454d366.mp4?token=OUUmelOj-8GlY8PLkItun6Hw2pDVQFlsI1ex06H65TbvsB1WLcNFiU35PG1yXvMfaxl8gY1pEfKz8kK2Z--pWGhd0lBBLE7f0hFSAMHibrViF0lfItpDtFlaAg1Z1chWQ65J2f9DAYSOOFIAq7AbIthb8rtGLZE-cDGza8TGgT-H9-Gt35G5vKyMlv7OAj0iuNgr6LWmpWQjIGDsvqq7lgVtVn7eWesU0_mKTYJ0_xn7V8x8aEf4ANQbGawvrkuZxfB0jE7c6shcqXbo207vwuULIIE_1RTLl7B_L8Hi8CdZ4SOgYajIfApkV_jc1w8wlLCMdHlYJDoAnTAlJeLIAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🎙
🇪🇸
تعریف و‌ تمجید جالب تیری‌آنری از رودری خرید جدید بارسلونا و تشبیه‌ش به سرخیو بوسکتس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106198" target="_blank">📅 09:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106197">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf8721a346.mp4?token=Lt58hE4X7llrMQcc5KMuV1l7edomcgAZFEr_K8RIisvv__SIJszSoRgUQ7YtUpHhbpnwg1An_2wRlLxWRDdQI9CXPChQPuGLsC2bwiN9c5sSk3Qyput4PKQGo2KLLoAw9nWVBqWsWHvgIX9gjAdhNdvOPYnCEZ4pTT5oHddBmLM7JkypcZZq7DXkYcL_xaqwtYEDUD_JjK6imgaxj6wDpkFM1m86WokH2yM1ReZj9i_A1y8MJn4vx5wev1tZtzhdI3lBTf70ynha-V3XCrSll9YGO7KnW9HUkaa5tUDGufcfpdacudJAv_e8ZphqgCAZg7kJh_qZnlyDc6I-X7isfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf8721a346.mp4?token=Lt58hE4X7llrMQcc5KMuV1l7edomcgAZFEr_K8RIisvv__SIJszSoRgUQ7YtUpHhbpnwg1An_2wRlLxWRDdQI9CXPChQPuGLsC2bwiN9c5sSk3Qyput4PKQGo2KLLoAw9nWVBqWsWHvgIX9gjAdhNdvOPYnCEZ4pTT5oHddBmLM7JkypcZZq7DXkYcL_xaqwtYEDUD_JjK6imgaxj6wDpkFM1m86WokH2yM1ReZj9i_A1y8MJn4vx5wev1tZtzhdI3lBTf70ynha-V3XCrSll9YGO7KnW9HUkaa5tUDGufcfpdacudJAv_e8ZphqgCAZg7kJh_qZnlyDc6I-X7isfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
اینبار کنایه تاجرنیا به پیمان حدادی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106197" target="_blank">📅 09:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106196">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8kU9m3BGgO1-tFQJ5KxB_A1MQ5-ZQ8HXiE6c3pRiUKldFe6mlZbYyTWdyjOyA9i2CNX7AdOUB5aBi4WDZq0u3e9qLQKvSk_5gkHBJNayj35HMFhweMYpKqusb7hPo7He23PgJpuz3LRuJDVKKU_WciX7zZlOROeJg7yW9dpXMYBZBV6qU4H1wg_a3viKDl97KKno9mWZpBtvNRqcRJXKwIYwRG3iGCZgi1ph561wSGBPc86jeJmtHu37twAIf6ACgN03YhvVeaGKUpLV14TmUgd4k7c8kXqPA4cr1kVoets6D_OFhDkzn5rBEdqFcSNLTWeAahPBDngT4Od1foisA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔻
🇪🇺
کمترین تعداد بازی برای به ثمر رساندن 55 گل در لیگ قهرمانان اروپا:
◎
🥇
🥶
ارلینگ هالند — 49 بازی
⚽️
◎
🥈
رود فن نیستلروی — 70 بازی
⚽️
◉
🥉
هری کین — 71 بازی
⚽️
🆕
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106196" target="_blank">📅 08:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106192">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fcya1R4DbStm6DXtHQSSAhRvjXMrloKIhrPx1OmofoFds9dM0f0aXfpDN3XvHiDhzEI0gCjI6Ui9319hxJkE_Cb4I2y5Ay5Aw56HN7BZU5c8V97q56u5z8Ig4TCuj1-k7VczIDjbxDLcMIAADXh_T3p3pDCtwouDFqiVxnfNQGzIo2Q_wnkOPOXk1xnNXCWCG3sFoOR3hHGuE0VBQfP7rVkzVyYGOc2eqBhdngbQS0EC1cvyvwYpovosajV5cJo2zbJ2zgG6qIw-a2x0Lsunu0BevyESYutDsdX8ift2PZK7bH-8mK0sjq9INhprvoxRI-u9yafrzvkGELzPFaKORg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🥶
مقایسه آمار السد قطر و بارسلونا در لیگ:
🇪🇸
بارسلونا ۴ برد و ۱۷ گل‌زده و ۱۲ امتیاز
🇶🇦
السد ۴ برد و ۱۹ گل‌زده و ۱۲ امتیاز
❌
پ‌ن: دوشنبه هفته‌آینده ساعت ۲۱:۴۵ قراره استقلال ایران از السد قطر میزبانی کنه. ایشالا خیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/106192" target="_blank">📅 01:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106191">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHd3W8nv_Iwq2cjftAr7RmBokgdA0wcz9a6NuhdRssUx4SJJczIVXrNh1PG34tqvudzfAhkV6Af4_AI1ji2AVcbsaxEvAqTYvFUBYuH-MVRzO1vQtUC1g4JkTz2kqXQq1lSG1QMchWH67NkzMh2_fuiLmmvZT8Z5Aiw31VFZSu9_AAci7UwZPqKW5bJvVUc-iVqQLkBiq-ZgvdseYk6wC0IC_76tNMeSGnpvwhH_KCJNgrYPrEe80QhxSJi0suxCTH0FZb_vfLsRmoR0S6-kWFpBVMCDrVtzjitlNFiSMLwLutHhYjalgNL3koEd8grTWKYWg6-ro3Z0GWbyf12L1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🔥
🔥
🔥
سوپرگل چهارم بایرن‌مونیخ توسط اولیسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106191" target="_blank">📅 00:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106190">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYnNCxDVoNgU28yp9-jEJ2Dp6IYqgdr0NhSTo40D2yHhVSjRh4BtqS25QwNRGQjJWbkh-4e87gC9GtRkTjYOi1fgHGJUkukC_Iwy0J_BwBSkzd-fB35AVSfXFqHqyo8o4tH5xPN0_Jsy1s8m9bTel-HjIVClVTvSwk79VL4IVnlSYSJfgB0yFOl6smNLiNAZmExa6iHHDCM6CZLTPcE6Ab7gtBQqlJgZWkTJZvqgT84hQnyDNe4Yhz62-H7ZQTzLDIZ1MP9Q9WnI6GBkAAacGt15VfbJoqwURqNs3hyJ4G7S_YophG3JwOT3_1ADPSAXo84H-gl7tw0J5vmb5-Obfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
نتایج بازی‌های امشب لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106190" target="_blank">📅 00:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106189">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇿
هایلایت بازی منچستر یونایتد 4-0 صباح
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106189" target="_blank">📅 00:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106188">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSomEmoVWc5Rz7vy7YtVVVsGOARJTTE_Ri3HQC8yUbiH1qGVpj-_XnPmeRNZG3xyDCivsH4N_OG2Xzm9DRqI09ecduXlE1cKkVVE-7kqdKOH5KdjzWu-W6L2C_bopVYtwJmCFrkq79abQD9vAQ4G0Kuf86VtBSX5YZMc2ZLxVINPUqVk8HFi-Ye4I1BF_KjcBN6IXa7scWbWNwogulDmym_nyiW7FELR1Ufc10sW4nWSmLpCzaP68jdETiUc4nf0Wtcpm4n0mMzgE8r0bhuaXLk__nJ4tDert3mWNfm3e8hYr3c5SKuhOcFynkltRlLpbPo6iQ3EMfN2hEQ5PEb9Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
نتایج بازی‌های امشب لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/106188" target="_blank">📅 00:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106187">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3993269f13.mp4?token=WzfDxKSUyBJcVfUjGTG96H4BTY0BqnR_NF0pYCitKy4jbIJ2oP9IruYyNlXFXJ3EAa7Ark0pc3EcP5P1tP8UKeKm6eSF1SzJVnKnJj0UmL9Z7PeiAOuZ7Ma6wmT5P3TxHtV9-OAstWtQvxrd8paLe6SNSJXOLU5E80WZ6AJIukg4DR20p8cguLtU8xAEEse7-07yTZ-1KmaNG0s-FR0LRwwx2mlZoYBUbZlWzKoXrjSLXpRh3NPvtKmQGkavo11PjzGjDgxT60I0zsRxUSFZXxWtT9geBnlcmT_t9hF5XiRP3GEft8TvUvw_gajSaatzHX0Ou0s-SGwsxMHDyFfcx7Ehvs1Dz_mrH5Pio3k6im4Gboceo4Cbkqi2GBd4a4pmSjxX4lcLyntP_lp9P8A-6j3EMvsUDIWmrlMHr3euY8JW7bJwa1CNnTBrV6v7JMYIcrh98v1QXUH1umczch-3ruPErLWcCu5-S6DonC7xgkSt3uplGXr1zluVytLYfj4ih-3mHigtG8smeCMy-BG89axw4B4HCpAhSbJ_D789nLZXVW2yaCTvOH83wPIrrCDN2Rg6cmlfesvluN8KZYT4-B1TjX1uzZ8aB3-C16MHd5cpdZ8U2_rmy5m-QyDhH6AOc8eByF5SODQRshLpx_tfOxWUTc1YxL6Mp0v7udofyO8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3993269f13.mp4?token=WzfDxKSUyBJcVfUjGTG96H4BTY0BqnR_NF0pYCitKy4jbIJ2oP9IruYyNlXFXJ3EAa7Ark0pc3EcP5P1tP8UKeKm6eSF1SzJVnKnJj0UmL9Z7PeiAOuZ7Ma6wmT5P3TxHtV9-OAstWtQvxrd8paLe6SNSJXOLU5E80WZ6AJIukg4DR20p8cguLtU8xAEEse7-07yTZ-1KmaNG0s-FR0LRwwx2mlZoYBUbZlWzKoXrjSLXpRh3NPvtKmQGkavo11PjzGjDgxT60I0zsRxUSFZXxWtT9geBnlcmT_t9hF5XiRP3GEft8TvUvw_gajSaatzHX0Ou0s-SGwsxMHDyFfcx7Ehvs1Dz_mrH5Pio3k6im4Gboceo4Cbkqi2GBd4a4pmSjxX4lcLyntP_lp9P8A-6j3EMvsUDIWmrlMHr3euY8JW7bJwa1CNnTBrV6v7JMYIcrh98v1QXUH1umczch-3ruPErLWcCu5-S6DonC7xgkSt3uplGXr1zluVytLYfj4ih-3mHigtG8smeCMy-BG89axw4B4HCpAhSbJ_D789nLZXVW2yaCTvOH83wPIrrCDN2Rg6cmlfesvluN8KZYT4-B1TjX1uzZ8aB3-C16MHd5cpdZ8U2_rmy5m-QyDhH6AOc8eByF5SODQRshLpx_tfOxWUTc1YxL6Mp0v7udofyO8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🔥
🔥
🔥
سوپرگل چهارم بایرن‌مونیخ توسط اولیسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106187" target="_blank">📅 00:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106186">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a3837ef974.mp4?token=GXv504CUYzWpqGXkAIfeDZOSDVvurjZGKGU3sdpSgw1gyui7dp3ojoZ5QBESSjsU0blXLssEGNbmE-9hVGBvfVDTu5XyxDWefVwlwFmT85QS2TFgAkuS5_3BxCXoOpS0z9z7UUfLIuwQvXrwnPHPl8fHJz4tz2Eh_vQ_tJxORbbq5OLarTfuIe2rifqF-xQZvm_8mOUq9p_xpBKonHSqZHfIAHiZcLbAHETxlq4DbSsvNE7_R4ioxf4_U_qZkmBBHthj2xeBex9axMYqj6sKPFUNVp1HzE1EGjHcj8Pl7DTiMyzNlGV0-pFeEroJaHFiA2R_AuCk3RgkCQv072rb6qH2TIQmM01HS98dQ_t0QrXOUHbvOZo0PM-AOU0MzAF4WBeeiRJe0ir7Ix_QW3bHI0KujvoE2PTTeGgPPWvr_Pz54wR60mrIOtNEiDyJWe8IAcrFO29PL-MXGIFAxly40Hkv339zXu3Yzv1R_vXWXS6Cks6x6Vd274Q0Nv4fQE0lwoZMGh69uhndrnx--vseUuBou5rUfXzxCqpO7-0YRPv_8tgiO-0aPyoGCFzqvmhC-0VIvH2SIycJ-gdgZ3GD3x4svqvEpXyVANaS9SSz_VoW5dvUdHGw57VNAHyEDZQAiHG5AgAlnmrysMRnJ5mevsIb2CFiGseInzcS-2dx0v4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a3837ef974.mp4?token=GXv504CUYzWpqGXkAIfeDZOSDVvurjZGKGU3sdpSgw1gyui7dp3ojoZ5QBESSjsU0blXLssEGNbmE-9hVGBvfVDTu5XyxDWefVwlwFmT85QS2TFgAkuS5_3BxCXoOpS0z9z7UUfLIuwQvXrwnPHPl8fHJz4tz2Eh_vQ_tJxORbbq5OLarTfuIe2rifqF-xQZvm_8mOUq9p_xpBKonHSqZHfIAHiZcLbAHETxlq4DbSsvNE7_R4ioxf4_U_qZkmBBHthj2xeBex9axMYqj6sKPFUNVp1HzE1EGjHcj8Pl7DTiMyzNlGV0-pFeEroJaHFiA2R_AuCk3RgkCQv072rb6qH2TIQmM01HS98dQ_t0QrXOUHbvOZo0PM-AOU0MzAF4WBeeiRJe0ir7Ix_QW3bHI0KujvoE2PTTeGgPPWvr_Pz54wR60mrIOtNEiDyJWe8IAcrFO29PL-MXGIFAxly40Hkv339zXu3Yzv1R_vXWXS6Cks6x6Vd274Q0Nv4fQE0lwoZMGh69uhndrnx--vseUuBou5rUfXzxCqpO7-0YRPv_8tgiO-0aPyoGCFzqvmhC-0VIvH2SIycJ-gdgZ3GD3x4svqvEpXyVANaS9SSz_VoW5dvUdHGw57VNAHyEDZQAiHG5AgAlnmrysMRnJ5mevsIb2CFiGseInzcS-2dx0v4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
گل‌سوم بایرن‌مونیخ توسط آلفونسو دیویس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106186" target="_blank">📅 00:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106185">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/29ed472619.mp4?token=MpPg_tawl2Q7BFKmnNpt1csLB2CAyYoYQ554_K2b_ft_gnWXV8KgbYYbFuME0_Y6uVJkw14dvOdozErmmt4Z31jqxTsyaNt8-bA26bsYAvAi132YvYDUA_ATWiAY26rSe8rIVJzBawbk93LdJuNFZZpjpTOsuHCLmzz_daOyuhLcFhvw2B0jbWYC4ZEarW9XNU4Sm9aZMdcTjscZr39lzogm9-bGs_OPf7BcciQ0P5_Pdy35qCBMJDwqS-cyMKV1NozkTwK0Q8R1gCp2nLA5JuXmOHvVLn0GiYy_LGlN-kGiX-bfWs_bkl9X5lKKm_Z_xC2wilHsJm5GqXDbTJO2Z2yOpSVCXhn5zuJOmccE17qlDoFzvWbLM3TJK4gDM57TdszPb5Ajsd3OViOec3I3KmVbKpNvWbccG5TnWuL-X-_7sVfOSmseYoxrAOiksRLJ_5U37ImRI7INoyZ3_qP9i3AFWClw8sCP6Z9OrsVBgOLMatkiFzKgbWuJxtOvC2Qd8zV_x3hg43xCD4tnVtnpX0i0TXWVssgQ2o_m8o1UfsoNGHfQvm-bYddic41GOR8jDx6Har3Q2YsNt1JPhkPOwSair4g7xpOktY7nv1YxHb5F1R7kzPFRlZUU03gvkZAWzfrlHlLwbRydjbCX5FL0os5_BybG8pf6bmCwuK3hfTk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/29ed472619.mp4?token=MpPg_tawl2Q7BFKmnNpt1csLB2CAyYoYQ554_K2b_ft_gnWXV8KgbYYbFuME0_Y6uVJkw14dvOdozErmmt4Z31jqxTsyaNt8-bA26bsYAvAi132YvYDUA_ATWiAY26rSe8rIVJzBawbk93LdJuNFZZpjpTOsuHCLmzz_daOyuhLcFhvw2B0jbWYC4ZEarW9XNU4Sm9aZMdcTjscZr39lzogm9-bGs_OPf7BcciQ0P5_Pdy35qCBMJDwqS-cyMKV1NozkTwK0Q8R1gCp2nLA5JuXmOHvVLn0GiYy_LGlN-kGiX-bfWs_bkl9X5lKKm_Z_xC2wilHsJm5GqXDbTJO2Z2yOpSVCXhn5zuJOmccE17qlDoFzvWbLM3TJK4gDM57TdszPb5Ajsd3OViOec3I3KmVbKpNvWbccG5TnWuL-X-_7sVfOSmseYoxrAOiksRLJ_5U37ImRI7INoyZ3_qP9i3AFWClw8sCP6Z9OrsVBgOLMatkiFzKgbWuJxtOvC2Qd8zV_x3hg43xCD4tnVtnpX0i0TXWVssgQ2o_m8o1UfsoNGHfQvm-bYddic41GOR8jDx6Har3Q2YsNt1JPhkPOwSair4g7xpOktY7nv1YxHb5F1R7kzPFRlZUU03gvkZAWzfrlHlLwbRydjbCX5FL0os5_BybG8pf6bmCwuK3hfTk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇩🇪
گل دوم بایرن‌مونیخ توسط هری‌کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106185" target="_blank">📅 00:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106184">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/469ae1834b.mp4?token=elp1bR0xFMGAs3p6xyJOVGX4hdgI7-QcCTiKghYXjw8ypQ6nNheYBB7T_mqwm9KmKj2xdDEwfPpVKLXpfg34Z7kdg_t98sviH2kjSCUm9RWn--VsLp_1VytFPSSECR8nEBfjUHA_TYlvJi-u3rC5NihZ76ny0EgmTwcNNu2AFw2CLQLnuEmrXf8ah10f022SxskmivzULRP2X_MqtJfsZII6cy-63ZDY7lQH6i95MUkchx1N_BpSXwzSEWcqjkxVlzg0d-mOXbCYbZjfqm1YLs6B2Bwzq-dryDtLv5QLm474Cb4uV8ePC_u5bUDMHXvzfhNZyhyjTZxmLVi_Xgv8tl0GiyktpWRMfbAs5qzFUGnMx1PLMt4rZ9Qr7wDbEyP-8i1We6tplsun85Lpjpe_-QiBWHfx0DotTY_h-cljcllzYAYOtXsvWpMK07FfvrVI1kLUgDE-xwQtZrqNwlvskunWEbjerSYVxxZ6OdyXB5U4FBbkH_hPziwlpQwGL8lWcVfboVpf99SavLF_MhFm0JjPBQVoFAofeFCezABAcIFag3NlQyMG3hfD3zeZcx2bT1QRbVOGUOoISBp-xwYe3xzPqKGqQ0-0QRww0vwh8e7p-rXSUpVBSMt0KLR-ju14s_7CSxuGdHF-OJ5b-yqQV6ypqSJ1oeNEcBJu7fOwAEc" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/469ae1834b.mp4?token=elp1bR0xFMGAs3p6xyJOVGX4hdgI7-QcCTiKghYXjw8ypQ6nNheYBB7T_mqwm9KmKj2xdDEwfPpVKLXpfg34Z7kdg_t98sviH2kjSCUm9RWn--VsLp_1VytFPSSECR8nEBfjUHA_TYlvJi-u3rC5NihZ76ny0EgmTwcNNu2AFw2CLQLnuEmrXf8ah10f022SxskmivzULRP2X_MqtJfsZII6cy-63ZDY7lQH6i95MUkchx1N_BpSXwzSEWcqjkxVlzg0d-mOXbCYbZjfqm1YLs6B2Bwzq-dryDtLv5QLm474Cb4uV8ePC_u5bUDMHXvzfhNZyhyjTZxmLVi_Xgv8tl0GiyktpWRMfbAs5qzFUGnMx1PLMt4rZ9Qr7wDbEyP-8i1We6tplsun85Lpjpe_-QiBWHfx0DotTY_h-cljcllzYAYOtXsvWpMK07FfvrVI1kLUgDE-xwQtZrqNwlvskunWEbjerSYVxxZ6OdyXB5U4FBbkH_hPziwlpQwGL8lWcVfboVpf99SavLF_MhFm0JjPBQVoFAofeFCezABAcIFag3NlQyMG3hfD3zeZcx2bT1QRbVOGUOoISBp-xwYe3xzPqKGqQ0-0QRww0vwh8e7p-rXSUpVBSMt0KLR-ju14s_7CSxuGdHF-OJ5b-yqQV6ypqSJ1oeNEcBJu7fOwAEc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌چهارم منچستریونایتد توسط لیساندرو مارتینز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106184" target="_blank">📅 00:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106183">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6a73af6ae7.mp4?token=BgrLCQE4BajnIVvWkomCCGOLCk6PaTpkkpOn9-Yxp0GFmSuSdaoZoQ5N9nDDMVr0zcRwFBddVE9fRvOInH-mMCd7V4dVW_R_wAFZvas_QmucUzZ7rESPKC7uQolx-8_Y4anQFbycOpVhHnmnPWcdbOT7kwZYMn9NfCupenfVBYi0oBgWVkhxuAtL7h0BcM6YdHsO4TAaILUwe-z2pXKib3SUjkHuOqEM2ao7GtZN6CkxX8bB2L4Iwgf83-SxCRSQF_O09nUxKhSapKbCzDtMOolg2u6rMurIhj_22J-SejmDxuF8GvZLPZsCgvDnzLtvrEYi1ZWTCktTixxA_tKLWhFVOtraclKeYr6a7amHzklyNvhe2BWWNMxp4OOlWOTaPADKbQBDvAJjxIdynHKg7M2QViudZkhGhE4kzoEBOgFroUzCkvFOyxdEUFy4L-BsTZGC3IppQn34VXY4ZUgSaNqrLQEpzjNEG0GZJzbhX-5sftGjFoxBbhSuEbPQaMq7--muJAL3v8EN7njAwQcJ2_u5x6b9E6TraiEafy7Mi4QgASMUHp7TjEl0qNJwkyxv4_I8oKsbIKBTDmszbknE3Depi8VT2Uc2-Sd1Dbm4vvUu0h5LgQz5vw-abRWi39NstHZcpMhA67-G4ZoKS_r-pNKHzz4oosr8QBC1264CepE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6a73af6ae7.mp4?token=BgrLCQE4BajnIVvWkomCCGOLCk6PaTpkkpOn9-Yxp0GFmSuSdaoZoQ5N9nDDMVr0zcRwFBddVE9fRvOInH-mMCd7V4dVW_R_wAFZvas_QmucUzZ7rESPKC7uQolx-8_Y4anQFbycOpVhHnmnPWcdbOT7kwZYMn9NfCupenfVBYi0oBgWVkhxuAtL7h0BcM6YdHsO4TAaILUwe-z2pXKib3SUjkHuOqEM2ao7GtZN6CkxX8bB2L4Iwgf83-SxCRSQF_O09nUxKhSapKbCzDtMOolg2u6rMurIhj_22J-SejmDxuF8GvZLPZsCgvDnzLtvrEYi1ZWTCktTixxA_tKLWhFVOtraclKeYr6a7amHzklyNvhe2BWWNMxp4OOlWOTaPADKbQBDvAJjxIdynHKg7M2QViudZkhGhE4kzoEBOgFroUzCkvFOyxdEUFy4L-BsTZGC3IppQn34VXY4ZUgSaNqrLQEpzjNEG0GZJzbhX-5sftGjFoxBbhSuEbPQaMq7--muJAL3v8EN7njAwQcJ2_u5x6b9E6TraiEafy7Mi4QgASMUHp7TjEl0qNJwkyxv4_I8oKsbIKBTDmszbknE3Depi8VT2Uc2-Sd1Dbm4vvUu0h5LgQz5vw-abRWi39NstHZcpMhA67-G4ZoKS_r-pNKHzz4oosr8QBC1264CepE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
گل‌اول بایرن‌مونیخ به بودوگلیمت توسط موسیالا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106183" target="_blank">📅 23:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106182">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hugUcjo9jutQ-gS96QotdcjZqI3qeLb_Saozw69JPH1_JEC1_x1i3KA1znil4g5xCpXC-CQUeFcqUnDHn8sl3WG0TJnyfmdcAlBVqF244QkojYx8FfJKTiVtUD__Jp5bZbyjO7EzZubO58auC7Y051LlEsikQwhqpzoRGa7-aESW2JoE13glSXZDE5xl2OWoVbCKCy51GRdtzF8HA9myF2PtasQiN31E62Hdz2UJzPx0Nkzmd67ICGbHrYxxNJfDgg0i15C5IZLkUSuJsahAiWEjuFVSZlPJ-1EuElh97Wk5tKx77EznUuKRTyk13Rk00fyJb1gFXp1tCiq9lDImoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔥
🗞
رومانو: فیلیپه کوتینیو با قراردادی آزاد به سانتوس پیوست و هم‌بازی نیمار شد، هیر وی گو!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106182" target="_blank">📅 23:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106181">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
‼️
🇹🇷
اسماعیل‌کارتال پس از تساوی جلو رم در لیگ‌قهرمانان اروپا از هدایت فنرباغچه استعفا داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106181" target="_blank">📅 23:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106180">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kD01DWIDw_gm4SIEPDJUasNW8cO2F126lOtpkqXpKo5OgyuDkEvzOESleLnEd26PHk8_LC8gVsV1NY8HzJTTqmjPxmWjJId8zVHVZnkCH4pZAGZZlr6TP7VuaIICaShep9N8iio8qsExSvMlOJCf1jL5RAguWMcFzY3Aj18MAkgYqmfyAn00Ue9QMGVCfhP2ktvTigitrFnNrGzb2NQRsgGHZ1ZYEVWtc4fmub5Is9nIVoG9MXpjokvi0MdXH-1WuhC_oSeqVHM4krXcvV0pBD-Tw0f1scPscPAZnTHCfyJabMAdAZ8_mX0hUXCEY6wle_lGfLnvr3YFE-hsK-_ifA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇹🇷
اسماعیل‌کارتال پس از تساوی جلو رم در لیگ‌قهرمانان اروپا از هدایت فنرباغچه استعفا داد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106180" target="_blank">📅 23:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106179">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f2197035aa.mp4?token=LxTEz2PjqrVl4-EmESY8U9h50LeA6_sNV594doK8I62coY1VuBmBsCTzWmaw6a0Mv_lKuETLhJq_NmN4PsRdL2KPAMyhVMyPydYADpnFw5T9Cr62bp_RfT-qJVA0-1UC47IkOFVnAso1znCeR2h3pCSQxiHm3oRgaLX81movaWDX1kjR_l6Np7wP7CkFHA_JfDohW36A4VFemhydsGDZzCxLW8aFREeH-19tMsCk53YzWzjpWM73IJo-VrjXb1LXYl91J5GzPgDAno9wTusD8NACMWbvQ1QDC1bUZ5uH5kNSZZV6IA3GtytElup5Joo26X51TooQKp2ftFlH5aAKax7UnOQ_cLxzBZYwTBRDpuZA3P-wGWZaCKfZlsNFMv5fSh6kN5QrYxTkQDuSximOPx2q4jgsWD1EkmQXfxTuPNQTK6-6Zqfdx8joPmNawinQcOytQpBy1p1YKbyDkcbdsGa2HJfDrCOfT4FMaz2c69Yys76nIdTRpnbSWETqkQSuaiCelRcGvGcLpiplpc2ZuhYgErBSC8iSepzBKU_1DdWvMfn9_3RQ6MH1KlIsvGVQbb5vrD0CslJJ53YyD38nRZU2NdoCqCt_fwQGSAX_A5XhSD1MY14GY-UW9ZjjZHNHy4p6Lm6zg4RKKnStba2roPO9D5ZAzFq2S7X7pjVt0Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f2197035aa.mp4?token=LxTEz2PjqrVl4-EmESY8U9h50LeA6_sNV594doK8I62coY1VuBmBsCTzWmaw6a0Mv_lKuETLhJq_NmN4PsRdL2KPAMyhVMyPydYADpnFw5T9Cr62bp_RfT-qJVA0-1UC47IkOFVnAso1znCeR2h3pCSQxiHm3oRgaLX81movaWDX1kjR_l6Np7wP7CkFHA_JfDohW36A4VFemhydsGDZzCxLW8aFREeH-19tMsCk53YzWzjpWM73IJo-VrjXb1LXYl91J5GzPgDAno9wTusD8NACMWbvQ1QDC1bUZ5uH5kNSZZV6IA3GtytElup5Joo26X51TooQKp2ftFlH5aAKax7UnOQ_cLxzBZYwTBRDpuZA3P-wGWZaCKfZlsNFMv5fSh6kN5QrYxTkQDuSximOPx2q4jgsWD1EkmQXfxTuPNQTK6-6Zqfdx8joPmNawinQcOytQpBy1p1YKbyDkcbdsGa2HJfDrCOfT4FMaz2c69Yys76nIdTRpnbSWETqkQSuaiCelRcGvGcLpiplpc2ZuhYgErBSC8iSepzBKU_1DdWvMfn9_3RQ6MH1KlIsvGVQbb5vrD0CslJJ53YyD38nRZU2NdoCqCt_fwQGSAX_A5XhSD1MY14GY-UW9ZjjZHNHy4p6Lm6zg4RKKnStba2roPO9D5ZAzFq2S7X7pjVt0Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇺
گل‌سوم منچستریونایتد توسط ششکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106179" target="_blank">📅 23:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106178">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c7c2e2ba0e.mp4?token=YuQ1Oxe5jPhkikNj3a1hF9RmDXfJMdzRvqEjQwsOQ_g0iGDzzP4kbI1Ahq5O1WRmkuZkJl7Li1pny0S5AI4oU7tFy63wCuRfD4UEa-GLawFrcli3ARMSPcRRcOL3EdwvSbofX7UJBgJY7GzhoxyN_kjoLZ52F9vUziCTXaJH49VDJd03_NhxOql3cvYXp1O8Ui6bRDck24TDJFVAh19KK0OkX0U-hLXUjh8SjGxugjatSTyafv6EIXHmy3JdisAoxgm_YvLT52x56aKjztHsZa5GSG4T38Q1M4rMJh7HglAGlgzwmDH5PG9QVo9oE9PbRI5wQn1rPzZWHGVlfHHEMYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c7c2e2ba0e.mp4?token=YuQ1Oxe5jPhkikNj3a1hF9RmDXfJMdzRvqEjQwsOQ_g0iGDzzP4kbI1Ahq5O1WRmkuZkJl7Li1pny0S5AI4oU7tFy63wCuRfD4UEa-GLawFrcli3ARMSPcRRcOL3EdwvSbofX7UJBgJY7GzhoxyN_kjoLZ52F9vUziCTXaJH49VDJd03_NhxOql3cvYXp1O8Ui6bRDck24TDJFVAh19KK0OkX0U-hLXUjh8SjGxugjatSTyafv6EIXHmy3JdisAoxgm_YvLT52x56aKjztHsZa5GSG4T38Q1M4rMJh7HglAGlgzwmDH5PG9QVo9oE9PbRI5wQn1rPzZWHGVlfHHEMYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم منچستریونایتد توسط برونو فرناندز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106178" target="_blank">📅 23:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106177">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7a2f3527a0.mp4?token=lvvJYDNSa11CxgeMDLPNMVS6Sn6cuSbffQLpJY7hR7YHpid4mlc5iXMf9bQrKoPUwgBcJ73HBNiceGVcOBLSBVZLyVKXh7S8EqIapL502KAC6CljPk2VvsHGVsqMNmwkD95fMLBE_2CbIjNfHJV_0K_iTCUnjvPdsoagjsJWIy-bQNvYHkE2d_kXUhCdMXDcr12VS4NgB2sokY7XFrGS4haThiMIl2juoJZFa0FPW5Ghjoy5h7HUxJsR9VA12DeoNA6Y5pAPtvReLqI-wXy53LiU1hRBTZJMMwwrYnqOMbOcKiwJKhS1VwbU0q_S1kgrOyz-AlGqFxykE2SYvef-FHo2AI98G9mg8RbIZqCHdTHUQZatmiT-JRInueeIDf_MD95ITnVZ9BEEM-fIeBoEHaW2Rao4at2G5xt6XzfFvfohWhpZfRy3y6sC0kMu6VtGp4V2qdvkT9YZsMRY5gtrkpIv_xNgz91F6IrSLHl4ytfJ8V0ojI31rSKGVMvTSEvtldAW2a3AfhX8oDS0nHV115hqTTRuPH3B8rHCQfgwlTfnhSsLqtTw84g32m51wJnCeheR_Ork5bCdrhKZgka4c6B5Je_N1IVFtihkKB6boMdB6S5EwYqeterEQjfPKs80cfP9gjnHZbDcVC-Wu8HEWH21QkgOw11jJrZrkA121to" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7a2f3527a0.mp4?token=lvvJYDNSa11CxgeMDLPNMVS6Sn6cuSbffQLpJY7hR7YHpid4mlc5iXMf9bQrKoPUwgBcJ73HBNiceGVcOBLSBVZLyVKXh7S8EqIapL502KAC6CljPk2VvsHGVsqMNmwkD95fMLBE_2CbIjNfHJV_0K_iTCUnjvPdsoagjsJWIy-bQNvYHkE2d_kXUhCdMXDcr12VS4NgB2sokY7XFrGS4haThiMIl2juoJZFa0FPW5Ghjoy5h7HUxJsR9VA12DeoNA6Y5pAPtvReLqI-wXy53LiU1hRBTZJMMwwrYnqOMbOcKiwJKhS1VwbU0q_S1kgrOyz-AlGqFxykE2SYvef-FHo2AI98G9mg8RbIZqCHdTHUQZatmiT-JRInueeIDf_MD95ITnVZ9BEEM-fIeBoEHaW2Rao4at2G5xt6XzfFvfohWhpZfRy3y6sC0kMu6VtGp4V2qdvkT9YZsMRY5gtrkpIv_xNgz91F6IrSLHl4ytfJ8V0ojI31rSKGVMvTSEvtldAW2a3AfhX8oDS0nHV115hqTTRuPH3B8rHCQfgwlTfnhSsLqtTw84g32m51wJnCeheR_Ork5bCdrhKZgka4c6B5Je_N1IVFtihkKB6boMdB6S5EwYqeterEQjfPKs80cfP9gjnHZbDcVC-Wu8HEWH21QkgOw11jJrZrkA121to" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول منچستریونایتد به صباح توسط کونیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106177" target="_blank">📅 23:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106176">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8476aaa93.mp4?token=XcDBDeOaUB8b-dAOAPWN9wl_LlTe3KPelq68IJJUgzGyWrR0qNN-nk7GX6cPkuSCjNq0nrmz_Ra94v3iwxeQvQwG9gek02lRjDZBve3u9QhHBVL4ULwu_8Fvg_EtS5MFzQ1nEeCtWqfnmE9zTNjj7kqBznZXD4T4MoXztgFktUrmnnEAOG90JrpYRoYm-r2i9-DZeVqKw95Qdh6yOnIdZj-AwSxgNCm4stFIiJmaQfvky24FW7hICz33Mbis7Kyod2hiO7za5QOzHu8W7IfPvR_uOY3g4eRCdytG9NtdyvRWVXZA1LHVTIWF8uk8-ywOXC7n3l3FQkg88UcgyzA5Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8476aaa93.mp4?token=XcDBDeOaUB8b-dAOAPWN9wl_LlTe3KPelq68IJJUgzGyWrR0qNN-nk7GX6cPkuSCjNq0nrmz_Ra94v3iwxeQvQwG9gek02lRjDZBve3u9QhHBVL4ULwu_8Fvg_EtS5MFzQ1nEeCtWqfnmE9zTNjj7kqBznZXD4T4MoXztgFktUrmnnEAOG90JrpYRoYm-r2i9-DZeVqKw95Qdh6yOnIdZj-AwSxgNCm4stFIiJmaQfvky24FW7hICz33Mbis7Kyod2hiO7za5QOzHu8W7IfPvR_uOY3g4eRCdytG9NtdyvRWVXZA1LHVTIWF8uk8-ywOXC7n3l3FQkg88UcgyzA5Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
بازی استقلال ـ پیکان، داغ ذوبی‌ها در دیدار با پرسپولیس را تازه کرد؛ باشگاه ذوب‌آهن نوشت: دلیل مصونیت تیم پرسپولیس چیست؟
❌
⚠️
باشگاه ذوب آهن: دو صحنه در یک نقطه از محوطه جریمه و در یک ورزشگاه
🟢
یکی امشب، چک شدن صحنه توسط وار و اعلام پنالتی به دلیل بی احتیاطی مدافع. دیگری سه شب پیش، خاموش کردن VAR و چک نشدن صحنه به بهانه پایان بازی و اعلام نشدن پنالتی و دقیقا همان بی احتیاطی مدافع پرسپولیس و ضایع شدن حق ذوب‌آهن برای بار چندم تا هفته ششم لیگ برتر
🟢
⁉️
قضاوت با شما؛ چه کسی پاسخگوی حقوق از دست رفته ذوب‌آهن است؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106176" target="_blank">📅 23:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106175">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
‼️
🇮🇷
اظهارات خداداد عزیزی علیه فدراسیون فوتبال: پول ندادند، VAR آفساید را تشخیص نمی‌دهد
🔴
فدراسیون پول شرکتی که VAR را آورده نداده و VAR اصلا آفساید لاینشون کار نمی‌کند و نمی‌توانند سر صحنه های آفساید تشخیص بدهند.
🔴
آقای فدراسیون چرا خط کشی نکردی صحنه رو؟ شما وجود ندارید اگه راست میگید بیایید خط کشی کنید و نشون بدید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106175" target="_blank">📅 22:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106174">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ge4LT1pMA7WFf38aeG1kfgkngQAOUIzrhcAeUwagVMY1D1eZG10jsGljCNhnZxxeOff7ca-hmet59zsc7uFWx10nzrNQpy8mYzxBwmgSPSpvtJyMJPqtyoC_AU4-TGoMznUcnd7yubnM00RkbJkLmCAM1_BVm9B3sfDICGsZL2BQsc_WIsgjCzACRf1mCo66-oqASA9d90L_BNb9YWHE5RPy3W8O2uOyNlGAzer9LATg0Wtt3CwnQ7bFeuMPgSSXVa5nR1CMOAoo0nlBbZ4VjfHTK2pvbD-sChJcJaOLJf-Jv5_BzhRk1Vu3iIt1SKFVzvT9pxkX32DoaBf795Po0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🇮🇷
‼️
واکنش خداداد به داوری بازی تراکتور و اس.خوزستان: تبریک به فدراسیون و کمیته داوران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/106174" target="_blank">📅 22:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106173">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‼️
❌
🇮🇷
🇮🇷
بیزاتی مربی استقلال:  دلیل لغو بازی رقبا را نمی‌دانم؛ شاید چون بازیکنان پرسپولیس قرار است بروند تیم ملی، بازی آن‌ها لغو شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106173" target="_blank">📅 22:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106172">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/588203f560.mp4?token=GdLaATi1Sh4FfUjvPhMFAFwTzqZJYatsCwX71oZ7Yac0y-cL9X-7uQ8rsms_B3-dXrl9sUdc7nRs8Oe4A4EQoJouo2t1g3MhzPOQMw14EaWI7RIBxbpCCGPN4JRvgznOJqnzv-1MhyhI9ayrZ_0okMhuOIHRPfFfgNTwA4UPoHJY52-ujZAcXfJO6qsRMZmuk4OYEXroQGdGz1hQ5EBUyf-NucOJH7ZgE87BP0b22NtUcwxshHr8U5Hgb5-GGuSAUv2_6UBsCJDfYb_z66s6TKsc-dNSxXt0V0Xxbtanqev3jwD5uWfhdJuTY10ecMIdTP-pgLB71w_jH2BaeupRAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/588203f560.mp4?token=GdLaATi1Sh4FfUjvPhMFAFwTzqZJYatsCwX71oZ7Yac0y-cL9X-7uQ8rsms_B3-dXrl9sUdc7nRs8Oe4A4EQoJouo2t1g3MhzPOQMw14EaWI7RIBxbpCCGPN4JRvgznOJqnzv-1MhyhI9ayrZ_0okMhuOIHRPfFfgNTwA4UPoHJY52-ujZAcXfJO6qsRMZmuk4OYEXroQGdGz1hQ5EBUyf-NucOJH7ZgE87BP0b22NtUcwxshHr8U5Hgb5-GGuSAUv2_6UBsCJDfYb_z66s6TKsc-dNSxXt0V0Xxbtanqev3jwD5uWfhdJuTY10ecMIdTP-pgLB71w_jH2BaeupRAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
وضعیت یاسر‌آسانی حین خروج از ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/106172" target="_blank">📅 21:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106171">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBN1at9-7DD4PY1sAIHC5FflTQD4UEWpG09Hbbs3f6JR2EzKoA8_eOIMJpj8LnK9Bhz4SxHNjfzwr0OqjZz4NLjucSC2X_EXdg2h9FVjSaHja8HPpmk4_MwfL2OnTMNP4fuAmoqoAUt3QR3mQzg7wvonFpQaReM2LfLKAEhCMlQW3OuV7k6BNU056eXzezAqyiSNi1cWy1dZTzt8N8zXvFk9DBqxJa5oN14FELl1Q8wa3CS93ADsEwwsOsFl0ol0i3v0oLY8z3NKAPh_y5VCWio9y11tMSgqHQR4pL7VBR4Fb6fb_OKqdyBpLBEr26ngVwWYK9AAC9RPAH2MrA7rAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
⭕️
❌
🇮🇷
پزشک استقلال در حین خروج از ورزشگاه: یاسر‌آسانی شرایط مطلوبی نداره و حضورش مقابل السد تقریبا منتفی هست هرچند باید تا روز شنبه منتظر بمونیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/106171" target="_blank">📅 21:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106170">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
‼️
🚑
🇮🇷
مصدومیت ستاره استقلال در آستانه بازی با السد؛ آسانی لنگ‌لنگان از زمین خارج شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/106170" target="_blank">📅 21:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106169">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df1846b0f6.mp4?token=qKA7V1mJ46c-gmsWfjMqrcDI_JJaSg9Bm_VT4OKssrmlGWJ-4kDwd7s3mwD518QHExP7zTs1UORD9hgRFoOj3RzTXFTEAxL2AJgp4BgF5vNSKnHBYwL5XPVN8U9YFUCQ6bpSADeqxgXp9Y9YD_kQt34kFuwufsMTNjan0o5aELQLpbvje3QLJG5LrQTJ0JvrrzDOuQfnor2LYpwQqpO2O4UzzLU0fNOPHC8RSNMTpJY6R86xS87-fg6NqM2bmwmMqq55h2JS74wK6JGN4iHL5aj_NmieMqBQB0Siq5oXg6dV_6LS9NJDwv1QkCpIX_lN2d55K5UTmMPaQBCmdHpjHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df1846b0f6.mp4?token=qKA7V1mJ46c-gmsWfjMqrcDI_JJaSg9Bm_VT4OKssrmlGWJ-4kDwd7s3mwD518QHExP7zTs1UORD9hgRFoOj3RzTXFTEAxL2AJgp4BgF5vNSKnHBYwL5XPVN8U9YFUCQ6bpSADeqxgXp9Y9YD_kQt34kFuwufsMTNjan0o5aELQLpbvje3QLJG5LrQTJ0JvrrzDOuQfnor2LYpwQqpO2O4UzzLU0fNOPHC8RSNMTpJY6R86xS87-fg6NqM2bmwmMqq55h2JS74wK6JGN4iHL5aj_NmieMqBQB0Siq5oXg6dV_6LS9NJDwv1QkCpIX_lN2d55K5UTmMPaQBCmdHpjHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚑
⭕️
🇮🇷
سعید سحرخیزان نیز لنگ لنگان استادیوم شهدای شهر قدس را ترک کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/106169" target="_blank">📅 21:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106168">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/020d7e0eea.mp4?token=pnnXc2oUjoZ805GUSrSDmg5mWisar2Ucbtvw6mKQCiO4aoQtwW_CpO4dMYFG7_-xvnXJfRewkAt45EK_9rCYWkhNwgYxejeLi0tfJRbMEjVxBkX1Sd_dOwOObOA2aG0Tld5SL_d2h2qBMplRfzQyRRJt21Pd4tCx_ht6ftn7qpULpyD3hjibS2RqgOt-e0HA4jl8_W-ebSRZfkWl19NzjrgFFtcYLSSxm1rL-3bEF8TjNlFMFbVOXcXrCK4WpCNgbfKln0LHTtGD5mu2it4SkzkQdPUttvJFlwRbxNvz1sZJV7IEjcPc-ZHaNK2Qzq5C_zElzc4j8t4F1gGzLwVPMS8iXp4tp0G0cuf9hE_a_vt02-5PSIPwbIzIHmV7SxNC-y4ecsgeTyEyjPeRUYSvNXxh49eDNo1rySaS87axfNlEvL2Vu7yt9Wa8wwqMk4wRut5URwu8ww9Ox3yqflZTLpthF9_LIebQAb6sMi1nzjU7rEcwaXS4efDjUupvOVZK4gTgiyrx-67EBxM631tKO6Eb86zcisVlPsSbhJyTVnUrkeufATYmZUshvVfMdLJs3VaeB2bMAmd6_zE5U67l_fVaCHFrNwrtV_VjyfvgrX1te0hW7WJZHgNVLV2rl5YQVEDuHNH2MVC65EBk2IAvuwAt-K_YBcSwuNVm7grYm_Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/020d7e0eea.mp4?token=pnnXc2oUjoZ805GUSrSDmg5mWisar2Ucbtvw6mKQCiO4aoQtwW_CpO4dMYFG7_-xvnXJfRewkAt45EK_9rCYWkhNwgYxejeLi0tfJRbMEjVxBkX1Sd_dOwOObOA2aG0Tld5SL_d2h2qBMplRfzQyRRJt21Pd4tCx_ht6ftn7qpULpyD3hjibS2RqgOt-e0HA4jl8_W-ebSRZfkWl19NzjrgFFtcYLSSxm1rL-3bEF8TjNlFMFbVOXcXrCK4WpCNgbfKln0LHTtGD5mu2it4SkzkQdPUttvJFlwRbxNvz1sZJV7IEjcPc-ZHaNK2Qzq5C_zElzc4j8t4F1gGzLwVPMS8iXp4tp0G0cuf9hE_a_vt02-5PSIPwbIzIHmV7SxNC-y4ecsgeTyEyjPeRUYSvNXxh49eDNo1rySaS87axfNlEvL2Vu7yt9Wa8wwqMk4wRut5URwu8ww9Ox3yqflZTLpthF9_LIebQAb6sMi1nzjU7rEcwaXS4efDjUupvOVZK4gTgiyrx-67EBxM631tKO6Eb86zcisVlPsSbhJyTVnUrkeufATYmZUshvVfMdLJs3VaeB2bMAmd6_zE5U67l_fVaCHFrNwrtV_VjyfvgrX1te0hW7WJZHgNVLV2rl5YQVEDuHNH2MVC65EBk2IAvuwAt-K_YBcSwuNVm7grYm_Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
ساکت الهامی، سرمربی پیکان: این برد را به استقلال تبریک می‌گویم؛ ان‌شاءالله در آسیا موفق باشند/ در نیمه اول تیم برتر میدان ما بودیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/106168" target="_blank">📅 21:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106167">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4fb8db538.mp4?token=ag8ljdJ1vcRnu-VVPH2u2PGHsKKv63I0AfnyMNJlldw7RNEUX4ZL0ti3Ws-_yJZHiG8w105podClSREFeWSaCu3vPqFUqIo4MFs0rcDU8DXabIOHNJbrRREgs4RChXkqUzTv4DRzm9gsgqN7b_0tNWIzASY20cBVkYWl0UCBDhKy599LnLk9ROAj1ZbaPeSADmzo2ucE-TywANJpCXqOFFW10OTYT60mBRlSxSY_uWlHLf0Knr-LJGnv8ivY4PMJKAiuzIPDzJgA9LS5wAqp5Fxqs__6gmNNvHOCcAD4PoM_9F-6GC8yFPX255dDGuzD_6KX2LD4SLfWbKyzN-GRGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4fb8db538.mp4?token=ag8ljdJ1vcRnu-VVPH2u2PGHsKKv63I0AfnyMNJlldw7RNEUX4ZL0ti3Ws-_yJZHiG8w105podClSREFeWSaCu3vPqFUqIo4MFs0rcDU8DXabIOHNJbrRREgs4RChXkqUzTv4DRzm9gsgqN7b_0tNWIzASY20cBVkYWl0UCBDhKy599LnLk9ROAj1ZbaPeSADmzo2ucE-TywANJpCXqOFFW10OTYT60mBRlSxSY_uWlHLf0Knr-LJGnv8ivY4PMJKAiuzIPDzJgA9LS5wAqp5Fxqs__6gmNNvHOCcAD4PoM_9F-6GC8yFPX255dDGuzD_6KX2LD4SLfWbKyzN-GRGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
هوادار تیم‌ فوتبال استقلال: تا قبل از ورود ماشاریپوف چیزی از تیم ندیدیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/106167" target="_blank">📅 21:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106166">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c788208205.mp4?token=HsqR74F7kPrf5Jw7A4Ie4hDmWSKaQmSJEMMCxAEf78NRd8wsnfa68p5bLoVCcqnDVAAcJasMn7goIyxWjAAEkSuVbxZLE2J9HBdbctBCdNWc4zPY4RTt28ttZJeLnuIhZZDBd7k2rG_UZQaQ7EBziJT2bCxo5HykJRb4TRzZiSPD-QNaKkXFdlJqU-KnYUSj8kJKwxy8rEqiB7pWLbR1in440ev9yBtM6RhknPFgR-EnqiC7NAFCf46eQnJkJH5UJtSCFeUXRBGbKClCBhglNADuy8zbtraI6itNZEUsCW1tKBECv2vWX36RiBuNfCWG7QECsyEOpoP4us7TX7HoVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c788208205.mp4?token=HsqR74F7kPrf5Jw7A4Ie4hDmWSKaQmSJEMMCxAEf78NRd8wsnfa68p5bLoVCcqnDVAAcJasMn7goIyxWjAAEkSuVbxZLE2J9HBdbctBCdNWc4zPY4RTt28ttZJeLnuIhZZDBd7k2rG_UZQaQ7EBziJT2bCxo5HykJRb4TRzZiSPD-QNaKkXFdlJqU-KnYUSj8kJKwxy8rEqiB7pWLbR1in440ev9yBtM6RhknPFgR-EnqiC7NAFCf46eQnJkJH5UJtSCFeUXRBGbKClCBhglNADuy8zbtraI6itNZEUsCW1tKBECv2vWX36RiBuNfCWG7QECsyEOpoP4us7TX7HoVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
‼️
هوادار استقلال: به زور بردیم؛ آقا سهراب دست از لجبازی بردار!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/106166" target="_blank">📅 21:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106165">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
صالح‌حردانی مدافع استقلال: از آقای سهراب بختیاری‌زاده عزیز عذرخواهی می‌کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/106165" target="_blank">📅 21:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106164">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e33ed4a004.mp4?token=mg71T6FDIgC6849ZesPbfy_kNT1TdJ6IbZikyQGjW1GOFRNfwFcV_O7F15H5oOrnJuEMGmyXDVyhcmy3qi9w9gD5n1St8rWhmF6Y4nIDldzNpZmOGExsdVnv7fHWk1U56cqklCeZ5lsE8qItsgQU_vGLE2yeWrtdaGVqiC61cV9NUEqMs5cr7yQWU5V8zuAUmJM_J8vCccXVwnx4QQ0sMOde8syRKW-uAAlsQyzfUBmsGBS5ZaxH8vyDRiWIN998FhcYri8GWHJD25Ko0o_CZXps8YupdmfQHoYyDfeYDRFFFnhxa6UJn4w5O6E3TGk5ovidB8hcSLZ1HrxwSjOolIu-fY_NVctHAUMsvgk12_cnMkiE5CgFPOJfTdnZdDwPjjA3AlSPKX1FCdS7Zts1njvksBNcZe4_4pU0L0fZ72H729P2MS06S6PnWDziHpOp63yvflf4LXHl0EADBKeVuv40p1wkyQoXV9eFeXzvAB6s86rIIVCCMQe53Harre_73ErXnSAR78ZpValyb9zSPuS5NVKOBtt2jUiJMmGoOFfbn_KXN8VjxcCzAzgObjua3eeHVIN2DXPJkUUQdkmOTAUU09kcKroQW3jQpF5vicXllZX8vAkYGR53gkJ-keWl8CDQ5Q_fDWl-iXgET65JQqzATTHd5q_9M-u4GWpCRbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e33ed4a004.mp4?token=mg71T6FDIgC6849ZesPbfy_kNT1TdJ6IbZikyQGjW1GOFRNfwFcV_O7F15H5oOrnJuEMGmyXDVyhcmy3qi9w9gD5n1St8rWhmF6Y4nIDldzNpZmOGExsdVnv7fHWk1U56cqklCeZ5lsE8qItsgQU_vGLE2yeWrtdaGVqiC61cV9NUEqMs5cr7yQWU5V8zuAUmJM_J8vCccXVwnx4QQ0sMOde8syRKW-uAAlsQyzfUBmsGBS5ZaxH8vyDRiWIN998FhcYri8GWHJD25Ko0o_CZXps8YupdmfQHoYyDfeYDRFFFnhxa6UJn4w5O6E3TGk5ovidB8hcSLZ1HrxwSjOolIu-fY_NVctHAUMsvgk12_cnMkiE5CgFPOJfTdnZdDwPjjA3AlSPKX1FCdS7Zts1njvksBNcZe4_4pU0L0fZ72H729P2MS06S6PnWDziHpOp63yvflf4LXHl0EADBKeVuv40p1wkyQoXV9eFeXzvAB6s86rIIVCCMQe53Harre_73ErXnSAR78ZpValyb9zSPuS5NVKOBtt2jUiJMmGoOFfbn_KXN8VjxcCzAzgObjua3eeHVIN2DXPJkUUQdkmOTAUU09kcKroQW3jQpF5vicXllZX8vAkYGR53gkJ-keWl8CDQ5Q_fDWl-iXgET65JQqzATTHd5q_9M-u4GWpCRbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تاجرنیا: امیدوار به حل مشکل صالح هستیم. جام قهرمانی استقلال؟ خبر موثقی ندارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/106164" target="_blank">📅 21:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106163">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAWD0eIt2Ba5p4mis5AWE5-N43SSadhRVB8l_wvVa_ESUVHVSfmTkA7MQ_5GA-yg1U6WQaX3FprNeTTyzlqKfGPgdC2Z6tj0wN2iyCp8JiG9tz0NYY3OxIJNzOHTXGk1ll0AQMbOYaNh8RcxuD32-c4hmGMl-RVEaVgYJv2a6Wui1AZbkxlRwqlmQjzsZYHKl2pl778usgGnH0iUMSV58dushkwUsZ86mKFQtXX7Sjg2bVK_D-bBDWJge9n77BLXjZXDZs8Ov8-FdjqQSklhyeSCqZBOKeHnSSHuPpF7zrhAX9A3wis9lICmRYpYpySRSqDWvq5KK1xb7IDWGMjQXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
هفته‌هفتم لیگ‌برتر فوتبال؛ خارجی‌ها عصای دست سهراب بختیاری‌زاده شدند؛ استقلال با برتری سخت و دشوار به استقبال بازی السد رفت!
🇮🇷
استقلال
😃
-
😏
پیکان
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/106163" target="_blank">📅 21:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106162">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b6bc94122.mp4?token=DdyqT8m6u0y9IVXPiGEshW7XsM7wbaDXKO_ctecYI24TtnGP1MLRu9BRTujdrt8PibErxhGZYfatBnE8VIPaKHiuPAJRQDvEd40_CGC85_w02KRFBiA5LvTfyz5wizsGSR3FSg7vwZozO1XwHYnKUVQ7TsfuAaHgjGX6wn5rxZnCUQP0ef2-ATZ89UHKMgCQmAj_9YvH9moxb1RszNy9cWpb50x7vTkKLBxppi6TOdtgMnEw_T3Bf-y2Gun8IyuV0jYgiHqKMqnfzfJiiteopITH2XOSuISzO0EWJQb2x1Wq9Rp-keit6C6rHWgaf7p1_ngVIV1F5rn2VBSsUIaq3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b6bc94122.mp4?token=DdyqT8m6u0y9IVXPiGEshW7XsM7wbaDXKO_ctecYI24TtnGP1MLRu9BRTujdrt8PibErxhGZYfatBnE8VIPaKHiuPAJRQDvEd40_CGC85_w02KRFBiA5LvTfyz5wizsGSR3FSg7vwZozO1XwHYnKUVQ7TsfuAaHgjGX6wn5rxZnCUQP0ef2-ATZ89UHKMgCQmAj_9YvH9moxb1RszNy9cWpb50x7vTkKLBxppi6TOdtgMnEw_T3Bf-y2Gun8IyuV0jYgiHqKMqnfzfJiiteopITH2XOSuISzO0EWJQb2x1Wq9Rp-keit6C6rHWgaf7p1_ngVIV1F5rn2VBSsUIaq3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🚑
🇮🇷
مصدومیت ستاره استقلال در آستانه بازی با السد؛
آسانی لنگ‌لنگان از زمین خارج شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/106162" target="_blank">📅 20:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106161">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇮🇷
🇮🇷
خلاصه بازی استقلال یک پیکان صفر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/106161" target="_blank">📅 20:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106160">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qik6N2dkovqBMm-Ym3CtLp6QRLYmq9uUmRWsU9LpY-4ij_ONZX7knSsGO8prniCqIInMCX7LMmrJkE7qBDTRttO8A4N2mAm4NH4RqkOBlID7q4a8EVvk2hr5OGW3Lz_NK4r3NzWN-S89cjBCIHnxmBNSTJ-DmHpHOeb4jud9mH99WITIRDSDGxr8C-xi-qZlsLWYqD-UI3pTLg6ymka7YW5JdWZDP9SwXTXmeyUcIiDgMDnqQyIWPUxa13WQRnLxpl2OWStkKfDu0Qb094aflNn7IORTo_xGKUJoYwoWPzViIerNkL-9bhfepQo4gmL1ttuKNDUO_RfrWjwK9fFhzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
هفته‌هفتم لیگ‌برتر فوتبال؛ خارجی‌ها عصای دست سهراب بختیاری‌زاده شدند؛ استقلال با برتری سخت و دشوار به استقبال بازی السد رفت!
🇮🇷
استقلال
😃
-
😏
پیکان
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/106160" target="_blank">📅 20:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106159">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f33ea76eac.mp4?token=EQGCSe09oGhdtHdIzRhZbOiF0oWJx0lsplun9AIvVuMoSn-AxVXC6c8gH3Syv9X3k6nEGIv6RcomGNJ_tpUqhBYAknooUcwDF28nwb1GxjGfs56HCRVpqwpOMbYTnIYDBbvKBaozBO71IP5XxzKLLitfJVFBWUIPHBJm0vbRm7RogxCDDCZoMewbhgObUiH2ViTfacm4Ilrm31yh1LFfe3OkwjJRumECsO2S2NqajTEv7QfTmCWneiqlaU_xsfWKHAxoVdVnrGTlEqxUUnaUdPvVJDIUKbmv46sNsFJzB6sBiKSjQSGypx3aoAjbdAxuCVYYMAfIOMiieexToMszJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f33ea76eac.mp4?token=EQGCSe09oGhdtHdIzRhZbOiF0oWJx0lsplun9AIvVuMoSn-AxVXC6c8gH3Syv9X3k6nEGIv6RcomGNJ_tpUqhBYAknooUcwDF28nwb1GxjGfs56HCRVpqwpOMbYTnIYDBbvKBaozBO71IP5XxzKLLitfJVFBWUIPHBJm0vbRm7RogxCDDCZoMewbhgObUiH2ViTfacm4Ilrm31yh1LFfe3OkwjJRumECsO2S2NqajTEv7QfTmCWneiqlaU_xsfWKHAxoVdVnrGTlEqxUUnaUdPvVJDIUKbmv46sNsFJzB6sBiKSjQSGypx3aoAjbdAxuCVYYMAfIOMiieexToMszJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آزادی چه توپایی گل نمیزنه و ۱۰۰ میلیارد پول میگیره از استقلال
🤣
🤣
🤣
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106159" target="_blank">📅 20:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106158">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c661b28aa.mp4?token=GhLJ3gIeqfx6KBvk036c54j75l6AG_lx3SKSj0Jl9wcU3hOMuD5GM53gON6Z90pNFch3g42epuj3k4Tx2QryyOFpbIBfwY0GoQYG0JFF9NOspAs1PptPiWvjhDsZC6Z4PK8ps-_XHx32s4O9-cItjtCJuE7yS1JIzv2EoTZzaBJmzulVovoP0QXXGbHgv4C8KmK3NU9mU8gsnVX-tsKI5xpu1BltigkFYvWr58NlzXSIVlmAQUAEcsAD-B07_jnn0tl0g6IR32Pu1TKbpH1qLa9UPD8jI2x1B7cEeAussXF8IKiZ5mh1uBbuKP1jaHDbgJNtSiZKA6EDR_Dys8K4Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c661b28aa.mp4?token=GhLJ3gIeqfx6KBvk036c54j75l6AG_lx3SKSj0Jl9wcU3hOMuD5GM53gON6Z90pNFch3g42epuj3k4Tx2QryyOFpbIBfwY0GoQYG0JFF9NOspAs1PptPiWvjhDsZC6Z4PK8ps-_XHx32s4O9-cItjtCJuE7yS1JIzv2EoTZzaBJmzulVovoP0QXXGbHgv4C8KmK3NU9mU8gsnVX-tsKI5xpu1BltigkFYvWr58NlzXSIVlmAQUAEcsAD-B07_jnn0tl0g6IR32Pu1TKbpH1qLa9UPD8jI2x1B7cEeAussXF8IKiZ5mh1uBbuKP1jaHDbgJNtSiZKA6EDR_Dys8K4Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گل اول استقلال به پیکان توسط آسانی(76)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106158" target="_blank">📅 20:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106157">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
✅
گل اول استقلال توسط یاسر‌آسانی</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106157" target="_blank">📅 20:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106156">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d01d6e5347.mp4?token=JGYHT6bVKHOpY4Eo2CyWWop_qifzZL9wGRq0rf7wek7ie3NnAfTy49xBQrwRvT3C4qd-dx-aQ7nmjlDGOXtVKLDwgFYvAeXXso1y3Fy_NyIwR05I6kk1oZddRho2mxjKEXkhoVRriAZYUm2hVg7T6o_jQsw-0OtY5xe_yZt1WqLUSjJVb0A-zwH8NDXrwAR1Xyh5vjfHbq5ThaLjp2Q8AQs05i2pKGdnHZKZFTeoSBmlwRnCdX68-pX2AL-Wpy3yqW8eADEP26bNyyUjBt0ShVsvP2gn_i8mgYxpzZI_OkF-mjc1itHmbutWzosx4I681pEz0nGjZtewqaucya8Ogw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d01d6e5347.mp4?token=JGYHT6bVKHOpY4Eo2CyWWop_qifzZL9wGRq0rf7wek7ie3NnAfTy49xBQrwRvT3C4qd-dx-aQ7nmjlDGOXtVKLDwgFYvAeXXso1y3Fy_NyIwR05I6kk1oZddRho2mxjKEXkhoVRriAZYUm2hVg7T6o_jQsw-0OtY5xe_yZt1WqLUSjJVb0A-zwH8NDXrwAR1Xyh5vjfHbq5ThaLjp2Q8AQs05i2pKGdnHZKZFTeoSBmlwRnCdX68-pX2AL-Wpy3yqW8eADEP26bNyyUjBt0ShVsvP2gn_i8mgYxpzZI_OkF-mjc1itHmbutWzosx4I681pEz0nGjZtewqaucya8Ogw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✅
🇮🇷
لحظه اعلام پنالتی به سود تیم استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106156" target="_blank">📅 20:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106155">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
احتمالا پنالتی برای استقلال گرفته بشه</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106155" target="_blank">📅 20:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106154">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
احتمالا پنالتی برای استقلال گرفته بشه</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106154" target="_blank">📅 20:31 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

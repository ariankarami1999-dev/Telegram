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
<img src="https://cdn5.telesco.pe/file/Yaaioy3-UDqBCk7s4tO3E9ewiMdgWfCc9iQxWU9z7MHKIUiN-AVimL0JU4zJQqxw2yzYACJUeucjostgr_PkYt-zmzoJxbP9pIDFtVtNp7Dotzl4TiCCbaxpY_HSEKfbeB7zu0WO5u0DKTZGc9tD65EWBXepATbPcvtMmIjAsYPolVHa0eCn7XH_DyxPkl_UAgwEHRU1JlKD9GGOLqUTYYF3qgUBoSKIHGVUEVkv0cbX_Db6TF7UanQEN46O6haNaAbteKs5AOjA9sU7deAehfR4LJNvZSehtvGRfXo8QMKXEbRQoA6DxkjCrJWhPuPbSZVlVR0VBQT-lEaUlZqxXw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 422K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 13:27:39</div>
<hr>

<div class="tg-post" id="msg-105865">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRsr1NDlP1MkOizfQCkQZzEwLcAtaAZLn13Is_2D3X1KpwejI_C0gvO6EzRDclHcv-17zxzVD4gbxXjMO-5hZuf3lLDLWbLTpmTc2PrpQR-JBdQVNgf8TiOARgPeriWsikksBhgD17Dqb_aigMG043PjzjbotZb2hJWVKKozihSmslWkUrm6bYrGBaXGvlgPO27irP6WqL5DGFMj2OLDs7S5oIlLHEwqtz7XygV9Ov9ohqyZnCVMFTsoxfotcqoFA1xkmbeAexnIw48klMD7kNWWZ1JK3exR-3WdQGVvnj3PQgQ8Etl6j5tsnHMm0994nOcYzi5h-fQv4MRsBedAlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
نامزدهای بهترین تیم‌مردان فصل‌گذشته:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
🇩🇪
بایرن‌مونیخ
🇳🇴
بودگلیمت نروژ
🇧🇷
فلامینگو برزیل
🇫🇷
پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/Futball180TV/105865" target="_blank">📅 12:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105864">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🇮🇷
جلسه کمیته‌انضباطی باشگاه استقلال برای رسیدگی به تخلفات صالح‌حردانی فردا برگزار می‌شود. حردانی در بازی مقابل پیکان غایب بوده و احتمالا مقابل السد هم شانسی برای بازگشت به تمرینات استقلال ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/Futball180TV/105864" target="_blank">📅 12:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105863">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubyFpayDrNhtS1Hl1Ht2xaZUtyOIqN_KZFoOGzwf0v5upUFxnX_VaPfgizStmctKg6BmPEdQMy_Q_mwyyuMwekGa4o7f6bBXkg4eYYgHNlALv8MXY6s87MNu_42v20oeu57-VfFjg6a_MonE7heQkMPxWOX_Q7-s-Ie4WZ1Xmf9QjSTc1xLl5OUXCWz-Fg-5AXWX72KPT-0Isj2jGmRLgBOtu7arXsfCPUovjTy6G79LuAoIPJiA0jKAF3ZeDb-uANH-nx3qxf6DlJRwE7If1qR3CwKTwYSg9pK2xEtAX6JOHfndPT5lS2V6yXCA2oULuVjTs7JfrfuYTqU47saWRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نامزهای کسب‌عنوان بهترین تیم زنان فصل‌گذشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/Futball180TV/105863" target="_blank">📅 12:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105862">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🏆
آغاز اعلام اسامی نامزدهای نهایی جایزه توپ‌طلا؛ ابتدا بخش زنان معرفی میشه بعدش مردان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/Futball180TV/105862" target="_blank">📅 12:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105861">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hfeoz0AJJqB0UP4JP7-p7bJUBZ0H508xaw7lggg4WX60pXDk-0x9RJet7vbfzpeVz6a5-diQV3e86LODykX-gSBmkAQv22gf3PdqBMuluWe-ooDveKlTqSF8CetfAPIpKwtSHL0UKXk7UjAcdHSJxrfM9WR6LDZem4mMq1O3gnc0mDsC79p-W8u0UXqfyQVgQ0cL-rA7vFXhrMKfaL_FrJkheznidnGz7XczsCAHEFGCmIupLlKjzervbzC64B2OH-wqP6f_MOwTxDs2UbVioDtbTMHo9P-1A7CSfcHKSTm3HW-CltOFdFYvn9kg1OQT0Mu3OVl86e87njT0TWG_ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
آرش قادری مدافع ذوب‌آهن ۶ زندانی جرائم مالی و غیرعمد رو با پرداخت بدهیشون آزاد کرد. با این ۶ نفر تعداد نفراتی که این بازیکن طی دو سال اخیر آزاد کرده به ۲۰ نفر رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/Futball180TV/105861" target="_blank">📅 12:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105860">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3601cd12ba.mp4?token=rYCi6ZbZ3saB3iULPWufC-J77YCcM9U68x2DmUpRiDXVdRu5m9wIDsM4EEZ8OTXCLMON95Qu5HhAbk_Bn1eqZ9HbATAqcFwqojWoUAw31DBZYB9JfAPCHNDMA8ZOoL3zd_IYjK1Yc6_7TuWHCRwC0kxdM7bPZDTqsq1ZRvswMzOhbK2NGXp3441mowUBD1i8mwI_nlDRrTwZmIBUQQvpJL-_Acob8Wl_UIc0tobDZ4Knyb9q2YPpCTZXGWs0NwZ8FdLWW558zy88WqoAAByKNrcgvfz_uovrSKkbkmKZreYjY1ByTCn2p0OchwfXbfW9JNXDuSKwSYJiZEREKT3nFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3601cd12ba.mp4?token=rYCi6ZbZ3saB3iULPWufC-J77YCcM9U68x2DmUpRiDXVdRu5m9wIDsM4EEZ8OTXCLMON95Qu5HhAbk_Bn1eqZ9HbATAqcFwqojWoUAw31DBZYB9JfAPCHNDMA8ZOoL3zd_IYjK1Yc6_7TuWHCRwC0kxdM7bPZDTqsq1ZRvswMzOhbK2NGXp3441mowUBD1i8mwI_nlDRrTwZmIBUQQvpJL-_Acob8Wl_UIc0tobDZ4Knyb9q2YPpCTZXGWs0NwZ8FdLWW558zy88WqoAAByKNrcgvfz_uovrSKkbkmKZreYjY1ByTCn2p0OchwfXbfW9JNXDuSKwSYJiZEREKT3nFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سون هیونگ مین در مقایسه مسی و رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/Futball180TV/105860" target="_blank">📅 12:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105859">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105859" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/Futball180TV/105859" target="_blank">📅 12:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105858">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHPiucW3hqXUFEwQ2SkrHOS7003hKm2MlCpGG5Oo3YAdO4MpqJpTf6yACf5aaONrcTHZMt2fxurGZNojN0WaJI9tnxJdevlJwac7zDmO2P8KZRsRwb3ksrzXzCjIcSscLvE9xu8sMzExU0ylmqmPahqjOb0Pj_NrJUA2cfI7Hd0Hy1ZIrT7vON9URVAdCLPKxSPlnwjNnlrsL9kG1sQCBply890G-drBOmU-n52tSaKxTwivB6DlPyjKrCOsGd6hG8io24Q5GBZ80e6u4BlCvMqtQohnXJJ5kGGKuz1YgvODgPEuH-aXY83kMT9E8fW_2Y_yTyfw8A2V_gIy9af5yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شبِ بزرگ فوتبال اروپا فرا رسید!
⚽️
رئال مادرید
🆚
اینتر
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در ۵ تقابل اخیر:
⚽️
رئال مادرید: ۵ بازی ۵ برد و ۱۱ گل زده
⚽️
اینتر: ۵ بازی ۵ شکست و ۲ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/Futball180TV/105858" target="_blank">📅 12:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105857">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hae78R3ZA1CPU0wRfWW_DZ1FUndFxqQaBxewGLquVD4pFETibnpY5H5izmy5IYHogI02KWVuweG4lYT7mC1IPvYlXt5NcdZ2_8KJ0YXUXEdz4TW0V47-vzYQh6Ul93SbW6pX2BX1qPSIAYmTbsB36T0_6OvzEe4vybTBjfQm8pcJvdnOmkEtRQFWMAkqzfFUn6RoWK3_-jzz5aOAqvbH4S2dd-MX4JKlHtoxNgUvz7tTSoSWIMFDh-mxK6EWs3ACg8eEL3QYcg5VRxthg9Wz5WPvxor1s3G_Qp6gfk8Emdy84fBJZ7NhQXW7FJMuy3HiSOEbw80wba_BVeZtI6O96A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👀
🇶🇦
🇮🇷
نتایج بازی‌های اخیر السد حریف هفته‌بعدی استقلال در لیگ‌نخبگان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/105857" target="_blank">📅 11:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105856">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSIVCqwi-hqYt-1cjuJmIKVvZTpWe0T3qfoYwiV5iTVgf10TvDdHPFce7e5N_DXKeH7PBUdSYghhz-bQn104ohucIhdUoAftPLYvNLG7A3-xu7Be-nz9oqXcbiHD9hTRw4w7aIHOmI9TwO-6sMpjiZrGnpedRV5rAsI_jViQ8Fm6X7zY4nLbTVrC--CwAdcxCYVCdlDtiXdzvnvaBMzcJ90NrFZ6fLXGNGTftoAUr3vgD0rzBDoswN-OM3_zISz4xHbKqmyBkqZfLBcusdi531t9S_3oZLOmZUJCFc-ifQnBAb2mi1E1BegbaJGTkD6Z36cwVt2chuqkgcT4LZSIFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇺
لیست اتلتیکومادرید مقابل لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/Futball180TV/105856" target="_blank">📅 11:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105855">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5465076b4d.mp4?token=uM9kPeooTBell81V5zaYKCpumBD_6HBHcklt2qM1UumFdA4qwU7fhCnfG_OC9XKrb957T3lqj_vrIKSTQPvJpibCp_JQuFdENLv3d3ELy7AnFDzfPtfYYDXjs474IYxdzTBfj033Lpf99f7quiTgASBmHR4F5XuqkggIoo3X5ierQDk7ic274huBy-kyZZuAMRFs7R7Yc5sOGn2gVF9xm071hd5IyYQnw1oEUOcqCluZ0_B0NSn31pyb5cHOJzwCFaycP5JbkCFUzl_duz8Zojw7t00brJjtO9mWLkcc3EBKnlN89suSF0zdhKMy97t88FnPSavMgaalENjlJkpGjpmZVB-dDWt2UQu5t5UGWf9_SBEqjmasfRyAb6i2TTXyGfGyiLwOIuMckOvt8lqOl7hDCjvNbOAsmu50mZltIF74GqW3YEOJLBv4m6plZd9jEABIYd0zIZXxPSne6udGTAQT_boVVkp7KqxyHAqm1O-RyGdRkhxgfMXMe3ealP3iIW_DlTVkzH5NBjnPx1NIR8dvL64tSl7JF1MP465JXyCz7Nd7RWnjAgnaG1XHdyE0u6Cmwan_Gt-L1hwvXQCXIgDDK-pcooATvb93refBG1YtrBMqb3ATG_RzDPcP1Xsi4TMlD_N-l2r39o0mTrPZRf0xDcHb9lpXLz7pM4jvE7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5465076b4d.mp4?token=uM9kPeooTBell81V5zaYKCpumBD_6HBHcklt2qM1UumFdA4qwU7fhCnfG_OC9XKrb957T3lqj_vrIKSTQPvJpibCp_JQuFdENLv3d3ELy7AnFDzfPtfYYDXjs474IYxdzTBfj033Lpf99f7quiTgASBmHR4F5XuqkggIoo3X5ierQDk7ic274huBy-kyZZuAMRFs7R7Yc5sOGn2gVF9xm071hd5IyYQnw1oEUOcqCluZ0_B0NSn31pyb5cHOJzwCFaycP5JbkCFUzl_duz8Zojw7t00brJjtO9mWLkcc3EBKnlN89suSF0zdhKMy97t88FnPSavMgaalENjlJkpGjpmZVB-dDWt2UQu5t5UGWf9_SBEqjmasfRyAb6i2TTXyGfGyiLwOIuMckOvt8lqOl7hDCjvNbOAsmu50mZltIF74GqW3YEOJLBv4m6plZd9jEABIYd0zIZXxPSne6udGTAQT_boVVkp7KqxyHAqm1O-RyGdRkhxgfMXMe3ealP3iIW_DlTVkzH5NBjnPx1NIR8dvL64tSl7JF1MP465JXyCz7Nd7RWnjAgnaG1XHdyE0u6Cmwan_Gt-L1hwvXQCXIgDDK-pcooATvb93refBG1YtrBMqb3ATG_RzDPcP1Xsi4TMlD_N-l2r39o0mTrPZRf0xDcHb9lpXLz7pM4jvE7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
فرشید اسماعیلی: داور باید شهامت داشته باشد و از هواداران ذوب آهن عذرخواهی کند
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/Futball180TV/105855" target="_blank">📅 11:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105854">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97326bc667.mp4?token=INDgq7TXn3EM6nDt7UW1QUX3FplQ3AdV9G4ws3n8CPJwavxEo-DkCn47eoIRAg1vwKI3byV3UckLywiJzLfBteLOvD6gSHqniGL0x84MHi7kKWpSYB4ZAvY2pcLHx7UIZaaK1M-q3-jK8Zpwg3dNze42j7clbLL1pDO4pSQRPmOojbSydTb4LnnX3H5NWcp_YOFSYoua6WgIbrkfJnmqEU01UxWQK5CyBWZH9Iap1qZ4zwH_f3R7y-EpN6C9Wh7lq1AB6skonR2CQAdPly2ybWwSYLIAHU7d97YXKFd4NalbTfdSV_EX4jEHHgBKdEBZEymqdwuzZaJUfMP9HU6MKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97326bc667.mp4?token=INDgq7TXn3EM6nDt7UW1QUX3FplQ3AdV9G4ws3n8CPJwavxEo-DkCn47eoIRAg1vwKI3byV3UckLywiJzLfBteLOvD6gSHqniGL0x84MHi7kKWpSYB4ZAvY2pcLHx7UIZaaK1M-q3-jK8Zpwg3dNze42j7clbLL1pDO4pSQRPmOojbSydTb4LnnX3H5NWcp_YOFSYoua6WgIbrkfJnmqEU01UxWQK5CyBWZH9Iap1qZ4zwH_f3R7y-EpN6C9Wh7lq1AB6skonR2CQAdPly2ybWwSYLIAHU7d97YXKFd4NalbTfdSV_EX4jEHHgBKdEBZEymqdwuzZaJUfMP9HU6MKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🧕
مارک‌کلاتنبرگ: گل‌اول پرسپولیس مقابل ذوب‌آهن باید آفساید گرفته می‌شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/Futball180TV/105854" target="_blank">📅 11:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105853">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
‼️
⚠️
واکنش اینستاگرامی خداداد عزیزی به محرومیت ۴ماهه از حضور در ورزشگاه‌ها
:
چهار ماه محروم شدم و الان دارم میرم مشهد به یه زمین چمن سر بزنم. خواستم اطلاع بدم فردا کسی ویس صدای قدم‌های من در چمن را نگیرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/105853" target="_blank">📅 10:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105852">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a688084072.mp4?token=S_SP7uzGrGcezSsxDt6v2XqUWzy4nWJG3n2pETfdiWrbj6PKE6c1jvQjTivDA7HSNzBemL6bLQ3gchMWBc7hqI4sfALIY026O_PZ8gyOrVjuBjgY4taieH_ntLvXU183_tlPpQQu0KFuFhbJdGvKimzX-keR0wgOY8xKttzyWWfAUX3jTcruUyK2RFmxgq-DtChtqdxKhsmPEotT7JXLIJc01034bNftWYzrRWXiNdGYEHtZVuHw86yIqTAMF-Do2a2aniyCBoKrCIYR2LAvqrkI9DUvFtdRL9baVYVyMzy16ngDu0Xd_6lA62wBe2v3l-p3JGlDIpHQLf0v8z5uBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a688084072.mp4?token=S_SP7uzGrGcezSsxDt6v2XqUWzy4nWJG3n2pETfdiWrbj6PKE6c1jvQjTivDA7HSNzBemL6bLQ3gchMWBc7hqI4sfALIY026O_PZ8gyOrVjuBjgY4taieH_ntLvXU183_tlPpQQu0KFuFhbJdGvKimzX-keR0wgOY8xKttzyWWfAUX3jTcruUyK2RFmxgq-DtChtqdxKhsmPEotT7JXLIJc01034bNftWYzrRWXiNdGYEHtZVuHw86yIqTAMF-Do2a2aniyCBoKrCIYR2LAvqrkI9DUvFtdRL9baVYVyMzy16ngDu0Xd_6lA62wBe2v3l-p3JGlDIpHQLf0v8z5uBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🇪🇸
پست باشگاه بدبخت و خار آلاوس بعد دوم شدن در لالیگا پس از هفته‌چهارم
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/105852" target="_blank">📅 10:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105851">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gc1-PlnUL3ANpS8t9Qxdm7NZE9UktnWdWc2-cnn3_4Q35qVnvK_GpC2hjCEF_F5VOO3tPYMUxyNCLsBNVpqJqYVWzNioG-IMKHcXVCu6f4snFzCLvq59OJzVJo9xDEpTgXEpwYZi4aFaX3IsenetGZJ_fGlU_djFXfu6ZKbWcwkpMRrP57OPvAfymNM1m_UxeartfpHvFAS1kfsByu9j9PCk8xRpkkTNXZernIyY9YNvHq4OuD5Zf0kvfxduHeS0zy3N7O5mieGbMkr-5jbF6HIzO6nN07-XdWVQ32_OpMHGG3D8iddwvMby4Q9EY7hOzH5gwmUGXXzHumzGfsmyVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرویز برومند پیشکسوت شریف فوتبال ایران و همسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/105851" target="_blank">📅 10:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105850">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dffcc1103.mp4?token=n7a2gKmHR6EU42SDBpgaBswYnDxRGN83SeqsQQx_bzDAUl4YeNgukO3woYoggscFs3YwEd9FXM340YlqGFVXntb1hN5A5gA8VqDsOrQxNkeeH6MnAqV_75x04XkIu7WGyNVAcATUCaRwLSU-j9s_UW31G3rBk6i28vcisXaac4M7OqmnenJv4rjcEkEDmX6gg3Q9B1Jp01SFCHNI8sd4PBucJuRnoAN8LYjGjqdO8Jc-iYrYie9h1LZzffvna8ms3O2w7ZN01YTqsdvwPQG7WuZ1xwAeaHGqHjCs7zKmIQE0MSPaw8iWgJ5OT_fWEuln-_HYsn7RlJb92vzNllTcZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dffcc1103.mp4?token=n7a2gKmHR6EU42SDBpgaBswYnDxRGN83SeqsQQx_bzDAUl4YeNgukO3woYoggscFs3YwEd9FXM340YlqGFVXntb1hN5A5gA8VqDsOrQxNkeeH6MnAqV_75x04XkIu7WGyNVAcATUCaRwLSU-j9s_UW31G3rBk6i28vcisXaac4M7OqmnenJv4rjcEkEDmX6gg3Q9B1Jp01SFCHNI8sd4PBucJuRnoAN8LYjGjqdO8Jc-iYrYie9h1LZzffvna8ms3O2w7ZN01YTqsdvwPQG7WuZ1xwAeaHGqHjCs7zKmIQE0MSPaw8iWgJ5OT_fWEuln-_HYsn7RlJb92vzNllTcZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
کنایه تندادموند اختر بازیکن سابق استقلال به رامین‌رضاییان: فاميل‌هاى ما سه تا جت دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/105850" target="_blank">📅 09:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105849">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7e0021bd.mp4?token=EO-U_LR_aABUbpSL0rg57HXVP8mqA0P4bgCRNwElVJz_IjXD5LC9_N4F_oM-jMWQiAL9MK-gQR8u_oQCJvPwKxKJ49uuCcAe3NsB5v4Tm3__sej-YIN0xyURH-_lEVV-0ILp8jaq4dCRzR2wLmBdYW7kUGh9oxz9u_2fr4ekNDHKiphx4l7vkh3fbSAXfUJgQJTTmtm-KeF85WuU7_oOIQeEWGiBmaeyU8YPPWyVfjsG5x7vML4SPxMkB6ugKLwH0E1ASn0w7dL9_PAwykydzKttJUkDfI2aYVA9uWDqCwWZ1GnpDhDKSl9KocXCPNhTbW3gLymmf2Xrfew13Ksusg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7e0021bd.mp4?token=EO-U_LR_aABUbpSL0rg57HXVP8mqA0P4bgCRNwElVJz_IjXD5LC9_N4F_oM-jMWQiAL9MK-gQR8u_oQCJvPwKxKJ49uuCcAe3NsB5v4Tm3__sej-YIN0xyURH-_lEVV-0ILp8jaq4dCRzR2wLmBdYW7kUGh9oxz9u_2fr4ekNDHKiphx4l7vkh3fbSAXfUJgQJTTmtm-KeF85WuU7_oOIQeEWGiBmaeyU8YPPWyVfjsG5x7vML4SPxMkB6ugKLwH0E1ASn0w7dL9_PAwykydzKttJUkDfI2aYVA9uWDqCwWZ1GnpDhDKSl9KocXCPNhTbW3gLymmf2Xrfew13Ksusg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
ماندگاری مدیر رسانه‌ای استقلال: اگه کنعانی بتونه با شستش گیتار بزنه، واقعاً از نوادر موسیقیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/105849" target="_blank">📅 09:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105848">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63a78b6b32.mp4?token=pqZwN06nzHVq70wUwgB6gE1nuxy2r7dtE1FwotjT-X-Sd1IHQHSr-6Tpi2p1dSQT6_XZ3hV8GFK4cSPN5Wt0e-jzTLKFLlQN4hDQ_0pcudfmuXuvIi7EFLipDaUA1O5G4pQl9m9gOVxiw_LI7SlA-F6MdPIEg0w6D7pVXr7zlA4NMhbUxNBzXeEW9hjvlsWbyRHzFQpAHQob4PoXtpCfP-UciDYlGVwPn2tmCxG7PC3HHvpXYStxe6nCJX_QkaERZwPf2tXkYfjIsyoVEfd0PglI1uaZoTko9NQzUF_gzIseHgRItiTkIaYIaJyVfXONdSNCg_W15O67LEzwuRw7sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63a78b6b32.mp4?token=pqZwN06nzHVq70wUwgB6gE1nuxy2r7dtE1FwotjT-X-Sd1IHQHSr-6Tpi2p1dSQT6_XZ3hV8GFK4cSPN5Wt0e-jzTLKFLlQN4hDQ_0pcudfmuXuvIi7EFLipDaUA1O5G4pQl9m9gOVxiw_LI7SlA-F6MdPIEg0w6D7pVXr7zlA4NMhbUxNBzXeEW9hjvlsWbyRHzFQpAHQob4PoXtpCfP-UciDYlGVwPn2tmCxG7PC3HHvpXYStxe6nCJX_QkaERZwPf2tXkYfjIsyoVEfd0PglI1uaZoTko9NQzUF_gzIseHgRItiTkIaYIaJyVfXONdSNCg_W15O67LEzwuRw7sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
تصویری از کنایه امید عالیشاه به داور دیدار تراکتور و گل‌گهر: میخوای بهشون جام بدی
؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/105848" target="_blank">📅 09:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105847">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12456da477.mp4?token=kb2EC5JJtuTw88X7Q0jD7FnSTogxDN_EGXSGXIkE-1Ltjo594KJPb2WG59Ep2gx8Dfz_XB_jD9on_kOmQfzltI8-oAVrfpcD24Tl6S3gq_y94qDzmRZtjrIu7w61dsJUHfVsLm_eoSfRdT1EhZAontjBVD2ZUh6-c2vhw7iOLvn-2LT3IlY13qBAxlZXiW_6gsl5-RqitymuJWVSyjH9FUYGztzaVqK_W32xxQzZwL3mOEZJjG64RzD90ijnnyEtgkz-9cZr7DBi7nJjEifgfhwl329VRWCYWvDgDFzDO_ZZbmglGNPxU0F2Fw0eHK7T35ZH_YB3BXqypUiOhkdjIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12456da477.mp4?token=kb2EC5JJtuTw88X7Q0jD7FnSTogxDN_EGXSGXIkE-1Ltjo594KJPb2WG59Ep2gx8Dfz_XB_jD9on_kOmQfzltI8-oAVrfpcD24Tl6S3gq_y94qDzmRZtjrIu7w61dsJUHfVsLm_eoSfRdT1EhZAontjBVD2ZUh6-c2vhw7iOLvn-2LT3IlY13qBAxlZXiW_6gsl5-RqitymuJWVSyjH9FUYGztzaVqK_W32xxQzZwL3mOEZJjG64RzD90ijnnyEtgkz-9cZr7DBi7nJjEifgfhwl329VRWCYWvDgDFzDO_ZZbmglGNPxU0F2Fw0eHK7T35ZH_YB3BXqypUiOhkdjIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
پیام جدید وحید قلیچ به خداداد عزیزی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/105847" target="_blank">📅 08:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105846">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105846" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105846" target="_blank">📅 01:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105845">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBRkW8NH3gEwvPPnN-y0oifw07R2GMwa0rWLEX2HcNFletbrxtFP_q_DaZ9vh0hXaptSNN2dDiD18qfxofLrhNbpkGiPd7TKiejIHB0O2g3XfLgUF_3tmG5pCl87JrvIu7qo0-je7wCC2SOSng6fqlS3oSuf5d_K597KvNdqKyiRHC4SMnRokOLoco762M7nTVDAvIakys_VahocAmGWKCZwz45iNcFj8sksJeMMGoutouEiti-73QkjpMOOoYz3c7XTwrMmC8V1lMQ6X765RS6hPGrv-VGealY1zJWzQRt1bC-6nsy_7npUQkR7Ts7W3rbW5mI6m86vYMmvxDaiyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان
US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105845" target="_blank">📅 01:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105844">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105844" target="_blank">📅 01:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105843">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94a89c6058.mp4?token=h7XnrwFM5AVDbHF1-KDJpeeuIyVt_rJNez7hzsVWZPwXq-piBap6BJNjxQFH1EYZG_eU-0vhgX1_ZpkEjUtdhVy2CM7gsA1TiY5o-mX7n_m9vHeDGYjFcANZXwqvI-Y6lGZOMyNiXfOtb6V9BekfLFxZRL1ohNLDkvstcPZ7KDcm7JJG4q4Ga4C27xaevOqPIURP6D0C9FgJj5mynzwvDyxqua-qopf4rubCPXTUbUBw_qepx9ejsD-LtQ7VEh0v-xW_hv5nAdaGwdAHyc3r14DahLlF7_y1rmbpWabuJEKvghQr4NBpdSStKdHFJn0f-OGJnG-OOfSglpx62ElNzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94a89c6058.mp4?token=h7XnrwFM5AVDbHF1-KDJpeeuIyVt_rJNez7hzsVWZPwXq-piBap6BJNjxQFH1EYZG_eU-0vhgX1_ZpkEjUtdhVy2CM7gsA1TiY5o-mX7n_m9vHeDGYjFcANZXwqvI-Y6lGZOMyNiXfOtb6V9BekfLFxZRL1ohNLDkvstcPZ7KDcm7JJG4q4Ga4C27xaevOqPIURP6D0C9FgJj5mynzwvDyxqua-qopf4rubCPXTUbUBw_qepx9ejsD-LtQ7VEh0v-xW_hv5nAdaGwdAHyc3r14DahLlF7_y1rmbpWabuJEKvghQr4NBpdSStKdHFJn0f-OGJnG-OOfSglpx62ElNzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
💙
میثاقی: با صالح حردانی صحبت کردم او توضیح داد که اصلا قصد حاشیه سازی نداشتم و هیچ قصدی هم برای حاشیه سازی ندارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105843" target="_blank">📅 01:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105842">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ee6a8989.mp4?token=tLz-u9q4hGUcG2XtbRA0Mel2c19nhw0XYRydJyjsIUGAujwVscAYrp__Zf18nNqcOyP4dLFwmuRPA73o2_AuTESCKF4AWqg_QNEGsCZOgt-CfGNesiUMXrOEwBcILX8cKq2PVnmDbVKe-l3xYSIHq5KVTdMBvxzwaRUkRccJB5MPI8Z1YgXQKv_NiQ9aYXVGwt-dV4-LesQ0o-6sDxwnfjEiRkB3CgNNnjm31ncELuZqdVvhVXgWRGmRdCr5-H5-0m1M7dItaI90PStCU3ASezZF_ClcZRdJzte8o9D6BP3Kp2lgF6LrFY6CLAugvRXgPKfQvgiBjCt4QNr73H803A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ee6a8989.mp4?token=tLz-u9q4hGUcG2XtbRA0Mel2c19nhw0XYRydJyjsIUGAujwVscAYrp__Zf18nNqcOyP4dLFwmuRPA73o2_AuTESCKF4AWqg_QNEGsCZOgt-CfGNesiUMXrOEwBcILX8cKq2PVnmDbVKe-l3xYSIHq5KVTdMBvxzwaRUkRccJB5MPI8Z1YgXQKv_NiQ9aYXVGwt-dV4-LesQ0o-6sDxwnfjEiRkB3CgNNnjm31ncELuZqdVvhVXgWRGmRdCr5-H5-0m1M7dItaI90PStCU3ASezZF_ClcZRdJzte8o9D6BP3Kp2lgF6LrFY6CLAugvRXgPKfQvgiBjCt4QNr73H803A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
💙
اسفندیارپور مدیرعامل گل‌گهر: سندی بیرون آمده که یک نفر از آن طرف فحش داده ولی از طرف ما اتفاقی نیفتاده است!
💙
میثاقی: پس چطور عالیشاه 4 جلسه محروم شده است؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105842" target="_blank">📅 00:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105841">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1e01e106d.mp4?token=eVFXHbDBYexT-LLu9Lp_dWODt0qhAB1vrfMd8Lg-PSjZhfCJLHEUpi2s7M7icl6hBvRGrhXquP27_b0NlU9T-XXFhmgaYxvkvW06ocLDVbnd1iwGPm7MyLj7mA4YXE_RpaG9Me2VHloRzHDykRgGyW_Ct1YR0mIBO49U-HsdF-LCkj_QkkJKVzGAOo0IhVQ5HzeXdxNLhB_PuLpVSKM1AvUEFzDf-_0igyQW40mBqLxNl8oFa5eufYNsRtLE0rpLrdsyZPr3rCH45dYltj4NoCkwPhMRbCDXy1VzWgW3jZydYqNtcegSea600bxToLefsjrki55DTVIJfHbWJPao8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1e01e106d.mp4?token=eVFXHbDBYexT-LLu9Lp_dWODt0qhAB1vrfMd8Lg-PSjZhfCJLHEUpi2s7M7icl6hBvRGrhXquP27_b0NlU9T-XXFhmgaYxvkvW06ocLDVbnd1iwGPm7MyLj7mA4YXE_RpaG9Me2VHloRzHDykRgGyW_Ct1YR0mIBO49U-HsdF-LCkj_QkkJKVzGAOo0IhVQ5HzeXdxNLhB_PuLpVSKM1AvUEFzDf-_0igyQW40mBqLxNl8oFa5eufYNsRtLE0rpLrdsyZPr3rCH45dYltj4NoCkwPhMRbCDXy1VzWgW3jZydYqNtcegSea600bxToLefsjrki55DTVIJfHbWJPao8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
❤️
حجت کریمی مدیرعامل تراکتور: حالا حکم کمیته انضباطی آمده است آیا واقعا باید خداداد عزیزی را در استادیوم‌ها راه ندهیم؟ آیا این درست است؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105841" target="_blank">📅 00:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105840">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fca1acab48.mp4?token=AH997B_BMIDYc7vbfa_VCVxphXiJbRuq6cknSXY1Gne5W7oTdZVyk5RxW3rZs2rUB9YcwWErQnHP8IJAgVRkcCj2lNT1h4qKrO4g_EkGTUCF77nBGI453aT_4sU6UUT4Q-KVW2W25CK-cdGIOMMs8gP1yy4dMR97JIFointerJaOYK-PTyP8GWCIAeECTNIF07evO7N-spKfC_V1TCfsY_N35Z-kIDGtRZjvNaL11-T_O9VK5xLbm7k3PSQHigCcxDuvH_JiuvFRpjlWesF3HWLjC7uIbqoyzBBg1-ScEk0Y6mjFAxq-L3vmbJVGEGhM2t8OrGtqCSL9h1S8TXLKsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fca1acab48.mp4?token=AH997B_BMIDYc7vbfa_VCVxphXiJbRuq6cknSXY1Gne5W7oTdZVyk5RxW3rZs2rUB9YcwWErQnHP8IJAgVRkcCj2lNT1h4qKrO4g_EkGTUCF77nBGI453aT_4sU6UUT4Q-KVW2W25CK-cdGIOMMs8gP1yy4dMR97JIFointerJaOYK-PTyP8GWCIAeECTNIF07evO7N-spKfC_V1TCfsY_N35Z-kIDGtRZjvNaL11-T_O9VK5xLbm7k3PSQHigCcxDuvH_JiuvFRpjlWesF3HWLjC7uIbqoyzBBg1-ScEk0Y6mjFAxq-L3vmbJVGEGhM2t8OrGtqCSL9h1S8TXLKsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😳
😳
😳
گلایه عجیب خلیل‌زاده از حجت کریمی؛
🚨
‼️
چرا به تماشاگرانمان گفتی فحش ندهند!
؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105840" target="_blank">📅 00:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105839">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d780e6da8.mp4?token=b4X2GyS0ZN_al94AlQYHCHMpkbHcFiMukKmhwMnJvWSEAsSRH8iRhCv2RHzS3LxHrzawp_BeUNKNPkR64sd3fFauBeHdxfzoUI8rk3QzcDapkeR8CBMDFmSR-3sVcZeCpteD_FZNyvra5B4QB4ae8Nk3C-oAl7UxxxzCOfa2mj5aUOFSIbv8bYis4Rm8LW02QlqxALTVmkGZNoqqFyfmUzbKfpfWP1QCU7Ywm3IkCFWtNyN8YeGDjRXIkNJxIcFAr8kt1Kc31rSL-y4LYpag7sZ3cYayH01ZglHhVKZzdFofMlyxMXsM4Fk7aDG6qrn7x8Sz9_LJbrwflT9XTuCq3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d780e6da8.mp4?token=b4X2GyS0ZN_al94AlQYHCHMpkbHcFiMukKmhwMnJvWSEAsSRH8iRhCv2RHzS3LxHrzawp_BeUNKNPkR64sd3fFauBeHdxfzoUI8rk3QzcDapkeR8CBMDFmSR-3sVcZeCpteD_FZNyvra5B4QB4ae8Nk3C-oAl7UxxxzCOfa2mj5aUOFSIbv8bYis4Rm8LW02QlqxALTVmkGZNoqqFyfmUzbKfpfWP1QCU7Ywm3IkCFWtNyN8YeGDjRXIkNJxIcFAr8kt1Kc31rSL-y4LYpag7sZ3cYayH01ZglHhVKZzdFofMlyxMXsM4Fk7aDG6qrn7x8Sz9_LJbrwflT9XTuCq3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
به‌به آقا مبارک باشه. اولین لحظات بنزین ۱۰ هزار تومانی در ساحت مقدس جمهوری اسلامی
🙏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105839" target="_blank">📅 00:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105838">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cab995b804.mp4?token=GmqKDmuxGmoV6J_CQXESn9B-pwjMxJM3nYQvZPS045bfcOELMn4XPZiHehGbrku5H-z_UO0FPfwDhwirvRKZwBIicRDOU6Zq6Zcywp_HacLelIAwoHf_SfjPAOxaEJXx-oMbOijtrdu_mY7kGpaqsBxYiatBwNuOzvFazURmoP9y8tXhosOmKffNOUsYSRtHU6dB36kwW0Bw7ZsyNNTOpZksy3QSzlgKo-ujYlf9YRX9nMe0y1fcgSRGpY3MgNByd4weuQIvgXZIwPbDr38TXaFvntfYGIGSJLHfpTAyZdIvrXXNH6cAKgB6KGXL0SxFOrzSJ8kWmpIGtHXO9BZ99A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cab995b804.mp4?token=GmqKDmuxGmoV6J_CQXESn9B-pwjMxJM3nYQvZPS045bfcOELMn4XPZiHehGbrku5H-z_UO0FPfwDhwirvRKZwBIicRDOU6Zq6Zcywp_HacLelIAwoHf_SfjPAOxaEJXx-oMbOijtrdu_mY7kGpaqsBxYiatBwNuOzvFazURmoP9y8tXhosOmKffNOUsYSRtHU6dB36kwW0Bw7ZsyNNTOpZksy3QSzlgKo-ujYlf9YRX9nMe0y1fcgSRGpY3MgNByd4weuQIvgXZIwPbDr38TXaFvntfYGIGSJLHfpTAyZdIvrXXNH6cAKgB6KGXL0SxFOrzSJ8kWmpIGtHXO9BZ99A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❤️
حجت کریمی مدیرعامل تراکتور: آن کسی که ویس را ضبط کرده است چرا به آبروی طرف مقابل( خداداد) فکر نکرده است؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105838" target="_blank">📅 00:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105837">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac4ad57568.mp4?token=CLelqLTzDvWNK31M4bvD4KRKuvgz9lVxohasxSShEz-PcJtNK2PI3pp3y8NRv8d7kh1HNqr7GwaWlQJ_-YBFs3YnYPOcb6iAjQj0BrY8FIqjAXgzIxKdt-vWSxluNl1k1hGxdHOY-JtyOP2JXX0sUk6oGFEjuWR2lzsfmNT6VusjjdrWhbhTfedp1Pa7mtrKfSDG3TOeck_YVmo0STqfm6IwrfXyhgfZytjJrtZgIRBSmo5omnS2RyHGF7SpN186EfAo1PB_9OIBWS6cpvHlZ3KRvgrNPI80M9LtMyBNc2-E5I4ocTlR654XiI-ELmrcY_lzGyaiSJjXdzLDRsoogQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac4ad57568.mp4?token=CLelqLTzDvWNK31M4bvD4KRKuvgz9lVxohasxSShEz-PcJtNK2PI3pp3y8NRv8d7kh1HNqr7GwaWlQJ_-YBFs3YnYPOcb6iAjQj0BrY8FIqjAXgzIxKdt-vWSxluNl1k1hGxdHOY-JtyOP2JXX0sUk6oGFEjuWR2lzsfmNT6VusjjdrWhbhTfedp1Pa7mtrKfSDG3TOeck_YVmo0STqfm6IwrfXyhgfZytjJrtZgIRBSmo5omnS2RyHGF7SpN186EfAo1PB_9OIBWS6cpvHlZ3KRvgrNPI80M9LtMyBNc2-E5I4ocTlR654XiI-ELmrcY_lzGyaiSJjXdzLDRsoogQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❌
حجت کریمی مدیرعامل تراکتور:  دیشب بچه ام از من می پرسید بابا قضیه خداداد چیه؟ من نتوانستم جوابش را بدهم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105837" target="_blank">📅 00:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105836">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd890b34ee.mp4?token=vbd9LVWagl6N-BXKMrY6MW9zYo_z99haac_TBhNNiM0aWsk1UjEpGTGBlD3eHy4dnR63MYlWAhrfFMOUL57YX2CFYs6kbZ2fE8kxkNCoS2Tx6s20_CLYdCN5ugXeqDyuqDPfBWJ83PRJtn9Dlf5qFD57LWUU49sXp0GD7tt6N0k5ngW5W6sSwBculh9aoKr8lkb9rtxS24nbKyDwOFO0NkeTmqE9Xgdis_FOYnobL4Oy6DCvHCtehLyDcLF3kEnAaNA4-KPJ4sjDeYwnU24EXXIjKAurK2EiEBfuVvSAap6REecyWGox2pQZ-E9GUPZArUlMQWFxoY0XAlD62WzRrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd890b34ee.mp4?token=vbd9LVWagl6N-BXKMrY6MW9zYo_z99haac_TBhNNiM0aWsk1UjEpGTGBlD3eHy4dnR63MYlWAhrfFMOUL57YX2CFYs6kbZ2fE8kxkNCoS2Tx6s20_CLYdCN5ugXeqDyuqDPfBWJ83PRJtn9Dlf5qFD57LWUU49sXp0GD7tt6N0k5ngW5W6sSwBculh9aoKr8lkb9rtxS24nbKyDwOFO0NkeTmqE9Xgdis_FOYnobL4Oy6DCvHCtehLyDcLF3kEnAaNA4-KPJ4sjDeYwnU24EXXIjKAurK2EiEBfuVvSAap6REecyWGox2pQZ-E9GUPZArUlMQWFxoY0XAlD62WzRrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
❤️
حجت کریمی مدیرعامل تراکتور: حق نداشتند که آن ویس (فحش های خداداد عزیزی) را پخش و جامعه را ناراحت کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105836" target="_blank">📅 00:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105835">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a288bb9015.mp4?token=cTp1T_7qbKpFCX11F9DSSe8UVb1qGz8QGqrGrlZAiZ-YLbE-QA9z8nIAYrqN0_nWsdBQ6KCd3m_9JHDbont5ZEjxeiv1lsV_BzwExM9qqn8nJT3sCDqbXHf12UG3UEVfuzW7uIDgTuHPihYiq8KcGO52SirjvPI6dLVArB7UcIHeQ-fd9fN3Ii3tn7nwzYD_uqN3uHninq25XiurfDkFJCGXdmzfKepkoP92U_hkVVkQB-XqwxXtZHT4CyxL-rJX1ZlezNERHzxLNmONnF4TH36MxsXSfb4GcUxZsAsiFgDx0vOvqBM7mJIjA-z8wz9vYhRDhZvyVU8JTSLh3dUCXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a288bb9015.mp4?token=cTp1T_7qbKpFCX11F9DSSe8UVb1qGz8QGqrGrlZAiZ-YLbE-QA9z8nIAYrqN0_nWsdBQ6KCd3m_9JHDbont5ZEjxeiv1lsV_BzwExM9qqn8nJT3sCDqbXHf12UG3UEVfuzW7uIDgTuHPihYiq8KcGO52SirjvPI6dLVArB7UcIHeQ-fd9fN3Ii3tn7nwzYD_uqN3uHninq25XiurfDkFJCGXdmzfKepkoP92U_hkVVkQB-XqwxXtZHT4CyxL-rJX1ZlezNERHzxLNmONnF4TH36MxsXSfb4GcUxZsAsiFgDx0vOvqBM7mJIjA-z8wz9vYhRDhZvyVU8JTSLh3dUCXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😆
😆
😆
😆
عادل خودشو جر که فحاشی خداداد رو تکرار نکنه بعد همون لحظه واکنش سخنگوی گلگهر:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105835" target="_blank">📅 00:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105834">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/670edf11a2.mp4?token=fLtyj0-A6qLMNE_bqt-_BdUayH8Az49hrztSjuX6gRTc0eEArcvXTp9RtjJHhRbRLlNzFXvEKqyyLTfIpoiM4pfP0CIcmMomNt5Q2NCllN90ifiUhAgGxzCG-aj3XbxNkVXgxL2yjQWgmDALdZR-TbzCeXJT_NeBPTVkBHxTFtTq18TcGiDal0OwI278H_tw4RIsRg8B6vfbd7zG6htx2J5noWmMiNdM50ultSBM1Ed8y3ZqVQfDIK0yjzcch8S1peHADFArdqa1NsqzG1Yg9lWnSHWZP9OPkOyyjALWKJuAfFHBGQ-vue668FnQjqvV2NcwtY-Gf1e2eFDhu5WBfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/670edf11a2.mp4?token=fLtyj0-A6qLMNE_bqt-_BdUayH8Az49hrztSjuX6gRTc0eEArcvXTp9RtjJHhRbRLlNzFXvEKqyyLTfIpoiM4pfP0CIcmMomNt5Q2NCllN90ifiUhAgGxzCG-aj3XbxNkVXgxL2yjQWgmDALdZR-TbzCeXJT_NeBPTVkBHxTFtTq18TcGiDal0OwI278H_tw4RIsRg8B6vfbd7zG6htx2J5noWmMiNdM50ultSBM1Ed8y3ZqVQfDIK0yjzcch8S1peHADFArdqa1NsqzG1Yg9lWnSHWZP9OPkOyyjALWKJuAfFHBGQ-vue668FnQjqvV2NcwtY-Gf1e2eFDhu5WBfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
‼️
❤️
حجت کریمی: اگر خداداد عزیزی فحش داده است حتما یک نفر یک کاری کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105834" target="_blank">📅 00:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105833">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9428c43ae.mp4?token=mJZ5qnUu4pCqXQOOUAQVpVNvRiF4KQMsYBH59et2RZK7NQvApOGjMkx5lh-YqKgjvy_4VIIGSN8f-W-TluLqKDCI62-nRO7opQmqMdb2arcYifeHI6gT5ud5vQflXR0Yvyslbsshj-2iRicgtWbiF9aOQg0jrO8_DYUjK456PITdfZ_nYivr9zXdTvK6Fkhz6NgNub4AOiGmMcP5WqYFD-hHgAbGgXL-Zuvb_kYllkmLCVCAywgPJijvH9warMTaY_Qp8S49WfI73eiS8K5cAp7e54WjkBTehhVGhg6orREHZ93uXcRs9GZTGh2D7-Nlxodq7DGi_eCJXt_Zg5EcoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9428c43ae.mp4?token=mJZ5qnUu4pCqXQOOUAQVpVNvRiF4KQMsYBH59et2RZK7NQvApOGjMkx5lh-YqKgjvy_4VIIGSN8f-W-TluLqKDCI62-nRO7opQmqMdb2arcYifeHI6gT5ud5vQflXR0Yvyslbsshj-2iRicgtWbiF9aOQg0jrO8_DYUjK456PITdfZ_nYivr9zXdTvK6Fkhz6NgNub4AOiGmMcP5WqYFD-hHgAbGgXL-Zuvb_kYllkmLCVCAywgPJijvH9warMTaY_Qp8S49WfI73eiS8K5cAp7e54WjkBTehhVGhg6orREHZ93uXcRs9GZTGh2D7-Nlxodq7DGi_eCJXt_Zg5EcoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❤️
حجت کریمی مدیرعامل تراکتور: به دلیل اتفاقاتی که در تبریز و در بازی با گل گهر افتاد از تمام مردم ایران عذرخواهی می کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105833" target="_blank">📅 00:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105832">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8340864e3b.mp4?token=VN1b836N35o-qINQL0_tQulGSPD6ksuCd92D_x5YzBW8ziF4gGu9_1NDB00uOTFsQKpOLMh4EW4REzYVjr2Ow7t27_NSPqX55RDuE205k1ECTO8LuK2c-cqq4a9Kq3LoDpIveYUXYr8o7fYxEskN2ZolavKn5YqCVWxUirXbdqVUWkRBD3qp5ApN5aY9RTXdV1Tg9zSc5XavpP9bZuClc--5SsKcB1coyTb2Kl4duwSXANy6Gr9yD_AXM2UHT7b9ojjD-csWiRUCH2OBlFbbdQyEQkpX3GVKbiQliRhBLVVTWTfBK3bFrIQP7CcWxp0TjLNQeymo2hcL83v_Z9oiRDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8340864e3b.mp4?token=VN1b836N35o-qINQL0_tQulGSPD6ksuCd92D_x5YzBW8ziF4gGu9_1NDB00uOTFsQKpOLMh4EW4REzYVjr2Ow7t27_NSPqX55RDuE205k1ECTO8LuK2c-cqq4a9Kq3LoDpIveYUXYr8o7fYxEskN2ZolavKn5YqCVWxUirXbdqVUWkRBD3qp5ApN5aY9RTXdV1Tg9zSc5XavpP9bZuClc--5SsKcB1coyTb2Kl4duwSXANy6Gr9yD_AXM2UHT7b9ojjD-csWiRUCH2OBlFbbdQyEQkpX3GVKbiQliRhBLVVTWTfBK3bFrIQP7CcWxp0TjLNQeymo2hcL83v_Z9oiRDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
با استقلال تفاهم‌نامه امضا کرده‌ایم
🇮🇷
چیزی ۱۰۰ درصدی نیست!/ توضیح محمد خلیفه درباره جزئیات تفاهم آلومینیوم با استقلال؛ که حتی خود از بندهایش خبر ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105832" target="_blank">📅 23:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105831">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
‼️
🇮🇷
صحبت‌های سخنگوی باشگاه گل‌گهر در خصوص فایل صوتی جنجالی خداداد عزیزی؛ با صدای بلند فحش می‌داد اما کسی از رختکن گل‌گهر بیرون نیامد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105831" target="_blank">📅 23:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105830">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
‼️
آدم عارش میاد بگه به فوتبال علاقه‌منده!
مقدمه عادل فردوسی‌پور قبل از مرور پرونده بازی جنجالی ترا‌کتور - گل‌گهر؛ این‌قدر از ترسشان برخورد نکردند که کار به این‌جا کشیده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/105830" target="_blank">📅 23:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105829">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a84e3855.mp4?token=YKKdjzHZEWsl_3ItqsuLB7ZpoPFNV0M2ESzYJWH3wc_a8LhP-rYZ2rQKa_8mZNEO98oxeN_W-g_oaPsU2gWzv4_9lJGOAFwKlj_MzOqaTwi3TyFCsXUB8sgL-DGEIf1AHTqCkpPei28DKsO9J3tN8mnLJPtAjawV3tioX_zffGe3F6gcg1NbgPB95z1y9zj-zjpJfBZrIay8NlYypZYvKOiriCLPKnL7LkGMT1W4-6G407tRpAGlihAiuf67iL2VXjrEs48zbJQLw1FTHzTO_NuxT2w0orIid9DLrdyyo13djykBmz1U9eU86FnDEsuAd_6yzqRWwtUmXGd5LCiCAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a84e3855.mp4?token=YKKdjzHZEWsl_3ItqsuLB7ZpoPFNV0M2ESzYJWH3wc_a8LhP-rYZ2rQKa_8mZNEO98oxeN_W-g_oaPsU2gWzv4_9lJGOAFwKlj_MzOqaTwi3TyFCsXUB8sgL-DGEIf1AHTqCkpPei28DKsO9J3tN8mnLJPtAjawV3tioX_zffGe3F6gcg1NbgPB95z1y9zj-zjpJfBZrIay8NlYypZYvKOiriCLPKnL7LkGMT1W4-6G407tRpAGlihAiuf67iL2VXjrEs48zbJQLw1FTHzTO_NuxT2w0orIid9DLrdyyo13djykBmz1U9eU86FnDEsuAd_6yzqRWwtUmXGd5LCiCAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇷
فولاد خوزستان با گل دقیقه ۹۲ احسان محروقی مقابل فجرسپاسی به برتری رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/105829" target="_blank">📅 22:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105828">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc6f987e3d.mp4?token=DP4wT7EJYB_H_SuRQhA2DHPakoqFKMJCYXEDAlEvjv6Wbemr-xIlw5D8PUwLLL2YuVxfLi39xH_xZiQmQGJwk69Caj82R3K4O8D6jk8tnHPDg6Mv3dBvPfy82a7ReS9cUMs18QBuR7ITXjJnDiaivvi6NCUbLFDcESGHef3PUMgpKM6sITID7t8X54eT1ZWw_ItwcWhrlop-ASxOoHifLa_h7yk5NKZIMw4bntGlIlzc7slIMCUTFqpzo8JrbWZcq58dVKJ3ZTf4-NGQ3VbVOF1gU5XAGVfIRc8-VOpW6Pyibsmx8XmhzorAencBZt0P3x3fA-3ZRGC2IVdgH5YWEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc6f987e3d.mp4?token=DP4wT7EJYB_H_SuRQhA2DHPakoqFKMJCYXEDAlEvjv6Wbemr-xIlw5D8PUwLLL2YuVxfLi39xH_xZiQmQGJwk69Caj82R3K4O8D6jk8tnHPDg6Mv3dBvPfy82a7ReS9cUMs18QBuR7ITXjJnDiaivvi6NCUbLFDcESGHef3PUMgpKM6sITID7t8X54eT1ZWw_ItwcWhrlop-ASxOoHifLa_h7yk5NKZIMw4bntGlIlzc7slIMCUTFqpzo8JrbWZcq58dVKJ3ZTf4-NGQ3VbVOF1gU5XAGVfIRc8-VOpW6Pyibsmx8XmhzorAencBZt0P3x3fA-3ZRGC2IVdgH5YWEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
واکنش کنعانی زادگان، بازیکن پرسپولیس در مورد حواشی دربی و ضربه اش به عارف آقاسی:
در فوتبال اتفاقات زیاد می افتد/ نمی خواهم به کسی توهین کنم و یا ضربه بزنم/ شما دنبال این هستید که حرفی زده شود/ هیچ کسی مشکلی ندارد و همه را دوست داریم و به همه احترام می گذاریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/105828" target="_blank">📅 21:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105827">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d82451c129.mp4?token=vEZTjiaEMMEZA4oXWIO3xxrC0ivTvo0cyzLsWclPmJAFCIc_qF1H-aMNQBO2nNpCUDEDLbR_P1CJroMRHjYwGdHsBqgCqphwEHOt6FGAkDBtZxFgu-s8V3-9tMOBK_e33B0XTT2Nr7ILWHc4eFpXhnZQkh5HCl2Q0h6f3a9zA7xJeaC2dvov5bCE5eBognxehyipg7bfjJJCY05Kxd5GVcSOGZQ5e1SHL7JJjZvyQnxD6YBtb4gqKffxAtJMP0zN4Zavoyu_51bvOb1ACayt-VPBxrbqSCxrnvWW5FtEeYYWOu_JX40rW3Dwr-5vFjBHttooqBT1Xoy7VQQXPlCf1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d82451c129.mp4?token=vEZTjiaEMMEZA4oXWIO3xxrC0ivTvo0cyzLsWclPmJAFCIc_qF1H-aMNQBO2nNpCUDEDLbR_P1CJroMRHjYwGdHsBqgCqphwEHOt6FGAkDBtZxFgu-s8V3-9tMOBK_e33B0XTT2Nr7ILWHc4eFpXhnZQkh5HCl2Q0h6f3a9zA7xJeaC2dvov5bCE5eBognxehyipg7bfjJJCY05Kxd5GVcSOGZQ5e1SHL7JJjZvyQnxD6YBtb4gqKffxAtJMP0zN4Zavoyu_51bvOb1ACayt-VPBxrbqSCxrnvWW5FtEeYYWOu_JX40rW3Dwr-5vFjBHttooqBT1Xoy7VQQXPlCf1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
❤️
کنعانی زادگان: بازی امروز خیلی سخت تر از بازی با استقلال بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105827" target="_blank">📅 21:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105826">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7963e99b5d.mp4?token=rTBouJKM9dn2B6hie7bmJKo4B_gw7MZ8i0Ylx4OM5aGIJYvUz1LW6fp2mYvyzUIqVYX66-Toq26r7Ur4R8fu0LIfbWZg-bDUNexFhLMUz2BapoQL8uVnxlO5MXrmrK62vMhYfzpVg8QYZQWHvGtBf3WGH57ruywIgLTIQacUeuZqzQRUG6XjqlMpS1lQffy3E9znOJ1JwUsGqoNrzwwd4ZssdXpBU_zcIc71l_wtWo0hYuluSMSo_p0LZD_6yHW93mEOF1r7E5PbCeHi5htNXyei90MaVAOIek3pybSGsTL3JPQq34bo3cZecCqzWM_wdbnV94g-le1aFgc4YzUisw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7963e99b5d.mp4?token=rTBouJKM9dn2B6hie7bmJKo4B_gw7MZ8i0Ylx4OM5aGIJYvUz1LW6fp2mYvyzUIqVYX66-Toq26r7Ur4R8fu0LIfbWZg-bDUNexFhLMUz2BapoQL8uVnxlO5MXrmrK62vMhYfzpVg8QYZQWHvGtBf3WGH57ruywIgLTIQacUeuZqzQRUG6XjqlMpS1lQffy3E9znOJ1JwUsGqoNrzwwd4ZssdXpBU_zcIc71l_wtWo0hYuluSMSo_p0LZD_6yHW93mEOF1r7E5PbCeHi5htNXyei90MaVAOIek3pybSGsTL3JPQq34bo3cZecCqzWM_wdbnV94g-le1aFgc4YzUisw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
😢
🇮🇷
واکنش جالب هوادار پرسپولیس به عملکرد تیم
:
بارسلونا هم بیاید در این زمین شکستش می دهیم؛ 2 تا به بارسا گل می زنیم 3 تا به رئال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/105826" target="_blank">📅 21:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105825">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
پیمان حدادی، مدیرعامل پرسپولیس:
🔴
با توجه به مستنداتی که در اختیار داریم، درخصوص پرونده آسانی از باشگاه استقلال شکایت کرده‌ایم و در صورت حاصل نشدن نتیجه، حتما پیگیری‌های خود برای احقاق حق باشگاه را از طریق دادگاه CAS ادامه خواهیم داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/105825" target="_blank">📅 21:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105824">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQYGPyAiIHUojxRgAi-_U5JKltmlt79ikgmW3z_eVTkYuI5DNSoJTjYO--a9ZIV562P1QCcxUJdwS42nVTsYIKLFDLdA5d557KvN8tqsagJ4RSBP8RtgWsLUQhNJs5hr_DKN9SqvN8YQP7RJKoKnKIHU2LPN9mL1kvIu73t3E0-3wwWD0Sq29y1Tl9e8yiU9XueeY0ewoDmxbcZD3A2dD7QsLshQoczu4okNo0WRl4bztSBaG2N-HtneZ-7wiP9JocNYkFMvYaTO4DZAKwtxwQT1ek2f4kB8o3goZpCpOlycdYcZouQhaCHh2XJYzLP__4NoDefRbtBjmVxfelRSCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
عبدالله ویسی، سرمربی ذوب‌آهن پس از دیدار امروز مقابل پرسپولیس از سمت خود استعفا کرد. ذوب‌آهن با کسب ۶ امتیاز از ۶ بازی در رده سیزدهم جدول لیگ برتر قرار دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/105824" target="_blank">📅 21:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105823">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRS_D6YPhEiOYZN_Vc2NwDUaAYq8gQW5-cGIQffjN2Iil9UDXK-EBBqdEVnKTznk2GqTCJgrlQCkwYdT2LkXFeBW079LAHg6VGz_FxIgmymS9n4Kn8rYEaUVS64cvdwYhO1nAMcmYQlagTDN-Q9s1APXRqYeLAmriMhCiO4IZCYMa9G2AoZCEIeneYg0jB3ae1zHTI5O0tW02Dhq3Eg9kmf7Ju0M7c0JhLlyefGQHDXujKRppA1HGfmUdQm7gN9jvEcDlhQrA8UJbCSWKpaka0OGQva3VfBKCv2tesDvPilS18bvEltf1wgwWZwdhRhLtZGni_GsZdKKgsAhGX47bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
هفته‌ششم لیگ‌برتر؛ شهرقدس قتل‌گاه رقبای تارتار و تیمش؛ پرسپولیس با یک نمایش زیبای دیگر دوباره از استقلال پیشی گرفت
🇮🇷
پرسپولیس
😀
😏
ذوب‌آهن
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/105823" target="_blank">📅 21:13 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105822">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjLZmDXrDd8Sn8vPVCtvGeZUO-RdIzDUzcdAF78UFVvExbm_JgKMx5OyEjIn8OuQ1gMO0HUkpp_wsIy1ynx6Uu9ePaLuGpogK7w0XS_2l35qY5VEbktzt9nDB85hyg_hqd4HzsgFMYeSn8DZeEpvgGLLyzuNZ1ilJF9ZtOO0xe_jfLI5qIGm_BpP0DRGz6E5J4w_iPYr0jRxQipfGpIh7tVelcNphThEySqeFTefg8SfsitEDHZUTxJzUTyM1z185Gh2yxU79GLuvcdPKiMwGG-9CL-oZM_X121vPRVmIvrx-jl3kk_wXquRGqehSDPTcD9RoELZb6Qb6Wl59-_7bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
هفته‌ششم لیگ‌برتر؛ شهرقدس قتل‌گاه رقبای تارتار و تیمش؛ پرسپولیس با یک نمایش زیبای دیگر دوباره از استقلال پیشی گرفت
🇮🇷
پرسپولیس
😀
😏
ذوب‌آهن
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105822" target="_blank">📅 20:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105821">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca306a134d.mp4?token=R1zYEWhTW68J0QjJHx2ehVZZaoA9oCtVp5yW5FXAHWoPJliIHO7D36s6jatxqznUambO9ZFNwnQsuSOfHDh8TMpbFxeyHQZ8n2fQTDmpPfeLayNwmFEnmcVqSq9YuMXrK7In3NagnLOKszp0DVOTwf76WttVh9ZdRlyLIVPm4XeDxUIHWazYrp0td5RvJ3pnS1pZ3GVIWHnDeqY-ZJc_oonTl-PFEIoWGO9AQvd9ek-nwXCLhP4P6qxUx-iNNAO9d9TJal6xymPFH552V24yDemE1re7ALsmCCjz1HzeCfJts2K3_qYLYcQ8wmLr1WgF7Cl-ZRuQuuY9U_-qNFxisw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca306a134d.mp4?token=R1zYEWhTW68J0QjJHx2ehVZZaoA9oCtVp5yW5FXAHWoPJliIHO7D36s6jatxqznUambO9ZFNwnQsuSOfHDh8TMpbFxeyHQZ8n2fQTDmpPfeLayNwmFEnmcVqSq9YuMXrK7In3NagnLOKszp0DVOTwf76WttVh9ZdRlyLIVPm4XeDxUIHWazYrp0td5RvJ3pnS1pZ3GVIWHnDeqY-ZJc_oonTl-PFEIoWGO9AQvd9ek-nwXCLhP4P6qxUx-iNNAO9d9TJal6xymPFH552V24yDemE1re7ALsmCCjz1HzeCfJts2K3_qYLYcQ8wmLr1WgF7Cl-ZRuQuuY9U_-qNFxisw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از مشخص شدن محرومیت 4 ماهه خداداد عزیزی، پرسپولیسیا این شکلی عالیشاه رو تشویق کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/105821" target="_blank">📅 20:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105820">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/656ef71eba.mp4?token=KkJUG9G2HRJgVbeSizc24nBRWF-UvvqV0UdjAVLEcXzaYvH3dEcscDKXxReH2xKeTyvx0RcosNKj-wpABCu2j0plS73rfeh8bXRY01soi9uIYtoQVgWf8uLTZGIsX-Acly4WK4KlDHIhIhe__fSfuPKMCglHKv7a3H6ZTO_Nc2sjSG_Tyz6H1Y1rnJpiAO7KiBbp1mFBowaHqt5_0bkThdAZft4Oi7TN7GLdHUNkZCH4_7V9Jne_GWEwIfAOLyakx6tnkAApjhfPJShi-R9DzEdMG1h1F9gRYd5AdkasQjQCSf3glv_rneDsIJrdOcYkeWG4uXpUrzphy3XKVK0I7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/656ef71eba.mp4?token=KkJUG9G2HRJgVbeSizc24nBRWF-UvvqV0UdjAVLEcXzaYvH3dEcscDKXxReH2xKeTyvx0RcosNKj-wpABCu2j0plS73rfeh8bXRY01soi9uIYtoQVgWf8uLTZGIsX-Acly4WK4KlDHIhIhe__fSfuPKMCglHKv7a3H6ZTO_Nc2sjSG_Tyz6H1Y1rnJpiAO7KiBbp1mFBowaHqt5_0bkThdAZft4Oi7TN7GLdHUNkZCH4_7V9Jne_GWEwIfAOLyakx6tnkAApjhfPJShi-R9DzEdMG1h1F9gRYd5AdkasQjQCSf3glv_rneDsIJrdOcYkeWG4uXpUrzphy3XKVK0I7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
گل دوم پرسپولیس به ذوب آهن توسط پوریا شهرآبادی
64
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/105820" target="_blank">📅 20:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105819">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔞
⭕️
⭕️
⭕️
⭕️
‼️
‼️
‼️
‼️
🇮🇷
🇮🇷
صدای منتسب به فحاشی زشت و زننده و ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/105819" target="_blank">📅 20:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105818">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lbll0s23YWJGK0bh0waaToW5xaxgSgNDLwiXKuA3m4CS8I-4okLLUY16mKueTfHecnaRm79NV-Elz1-5WcblOP5BKw2XDEFe_tMfoOKFBuhZP_zHrmlCtwXLNhuROSzotJSVPj7S7wBIecLEuktLh2A6mZaARF5ABzJBxEL7iWcgH1H7GXYZuQy3wmgVProQNlJ-mSHLI3EcZwosGaFoqHsY4KpXtH_h4Hx4rsmj97u5DBOlIw8WYynDzk9Sh_E2ZlkpdPSxLLdzX8iYTeHBQgoIlsUSWEYM1rRl7M51hQexrpeUhW475afWe9szcAjjzisZ5DMxbKhNZadoHAm7xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔞
⭕️
⭕️
⭕️
⭕️
‼️
‼️
‼️
‼️
🇮🇷
🇮🇷
صدای منتسب به فحاشی زشت و زننده و ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/105818" target="_blank">📅 20:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105817">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b10d894fc.mp4?token=KlNw6YP9RXnuQUWFz_arBzJNCdY_9u9cRaY1yaLYX0n6svjb1ERIorYY9DLwoxO447YP-aLy92Cv3rUOfxuJk4QE6D5NT50RLEEfe8CKafNr1y_4v60xi5JlPjdjhSYtGL74Pdkca0yZ8QWyFMY4602V3hRwbTcHBtwtVkwa-bXc03vzr3wh6a2uJk6A_idYoXgSuZDIsojSpKQi2_IdL7SGnzGeV9UCG8nsq-7TLii9Oio0FLKFQe2iKQYQbphmLsVUopFvkY0Uq4pMGN2qtt6qfRYAZzDh6o8hjWbUw8887gNWea8omx5vRKrpXyOw5W0CdFpjdhWpEoVyZ9g1XwWaRVyLVmKKca5XVkxt0aRX1-KI8pQ6y3_TpVqP4DNPG_WneKY9SO1EKWn8cDfDqBzr4PkmHyS23AyV4oROPq3TRfAIetjyr75ZquyUmtu958lIrYB57jwL53OSYhacICrpmrjQnsYBVzFq66xhgTxsXttako99FM6BSajByPcVQJonm8jtlEqtg4q6bg5I0kKYL_PXpO4Zd03bvWE8xr6Ky0ix9D14yUqdY2YaIZDdEZ0G8JzkWZ3Wvy9OcmxbIXYOrdjOz14L1Gc4KD99XE6YzjNSwx_Ns1FSMxIyfZ3YjKBfn3Rwq2So9Nl4p_lmEr5d1QzVx88D5kpY_HX2k-E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b10d894fc.mp4?token=KlNw6YP9RXnuQUWFz_arBzJNCdY_9u9cRaY1yaLYX0n6svjb1ERIorYY9DLwoxO447YP-aLy92Cv3rUOfxuJk4QE6D5NT50RLEEfe8CKafNr1y_4v60xi5JlPjdjhSYtGL74Pdkca0yZ8QWyFMY4602V3hRwbTcHBtwtVkwa-bXc03vzr3wh6a2uJk6A_idYoXgSuZDIsojSpKQi2_IdL7SGnzGeV9UCG8nsq-7TLii9Oio0FLKFQe2iKQYQbphmLsVUopFvkY0Uq4pMGN2qtt6qfRYAZzDh6o8hjWbUw8887gNWea8omx5vRKrpXyOw5W0CdFpjdhWpEoVyZ9g1XwWaRVyLVmKKca5XVkxt0aRX1-KI8pQ6y3_TpVqP4DNPG_WneKY9SO1EKWn8cDfDqBzr4PkmHyS23AyV4oROPq3TRfAIetjyr75ZquyUmtu958lIrYB57jwL53OSYhacICrpmrjQnsYBVzFq66xhgTxsXttako99FM6BSajByPcVQJonm8jtlEqtg4q6bg5I0kKYL_PXpO4Zd03bvWE8xr6Ky0ix9D14yUqdY2YaIZDdEZ0G8JzkWZ3Wvy9OcmxbIXYOrdjOz14L1Gc4KD99XE6YzjNSwx_Ns1FSMxIyfZ3YjKBfn3Rwq2So9Nl4p_lmEr5d1QzVx88D5kpY_HX2k-E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گل اول پرسپولیس به ذوب آهن توسط علیپور(43)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/105817" target="_blank">📅 19:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105816">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بالاخره پرسپولیس زدددددددد</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/105816" target="_blank">📅 19:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105815">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">علیپووووووووور</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105815" target="_blank">📅 19:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105814">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گلگلگگلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105814" target="_blank">📅 19:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105813">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd555c5d54.mp4?token=Ic4rU9CKooaXU1yW19uIrfTz39rsr6Phj813DuLnwgLJb-Joz07GU2md9TIqYDgS8qsPidDaHFsBaniIizKH3dRBjB_moex0bVLGnG19YbmEZh4v1OedHB6MxwYAl4GCj7-Rkieoy2PicQdYl2F4KWukluxgHJEc7zCAr_KXEizDbAOlu0udpko1gRR99VnNSkGpS1RUcwYDNSpxtoLbLHkDtgPymrO0rHfm7i04OdLI6QXaX96U-mKd7D0Ox6IyDOhm0JTJJlyC4BtQum18Wq2kxkH33yMR9z6SWatsaRGPSS1-oC82kqwtcenoVwyrIXVIHqAohm34kTpeHMoyFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd555c5d54.mp4?token=Ic4rU9CKooaXU1yW19uIrfTz39rsr6Phj813DuLnwgLJb-Joz07GU2md9TIqYDgS8qsPidDaHFsBaniIizKH3dRBjB_moex0bVLGnG19YbmEZh4v1OedHB6MxwYAl4GCj7-Rkieoy2PicQdYl2F4KWukluxgHJEc7zCAr_KXEizDbAOlu0udpko1gRR99VnNSkGpS1RUcwYDNSpxtoLbLHkDtgPymrO0rHfm7i04OdLI6QXaX96U-mKd7D0Ox6IyDOhm0JTJJlyC4BtQum18Wq2kxkH33yMR9z6SWatsaRGPSS1-oC82kqwtcenoVwyrIXVIHqAohm34kTpeHMoyFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
واکنش جالب عبدالله ویسی به خراب شدن موقعیت گلزنی تیمش مقابل پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105813" target="_blank">📅 19:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105812">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a21d11818e.mp4?token=O-kzBmCV8Asm1ZJcmmeXOyPsPNl-YQokiKK03x8M2L3VKbgtqcMZ9KxGT9AeSWJgbDZh9SfFCwZak1S6uCixW6EvjG26HTHF66esDx5SU-F6qiq5wjTUMrXb0vZ4uKpyWHzsN0OJ6ik3TNp5B9QERHgmUotLAluiLgpXAaS1owcIsqtmR1oUwg54iQYX33pLS5Oe6HuJtV91_Jgw0ZMD1De3SrwyN3ILy7yL9oC8ZGfjj6klWZFyH3FVVV44m8loQB0ce_r45Z7xh8ozyLhII0sx1X0S7UdjxrZOB40t_MGD3Bhki-HiuiGmOIw3Z1E-N9PVbjjJIbpuZZKwdu7XiBBy3I2bacNzHTdaekQD00iXyVxu4RtXmQOs0qeiOD3Mz2uyzD-INzp7IaCxsaHQh_GlaxIvr9jD3CPCYQI416IS0zhSkkhn_JxrjDayQ2G8tTysb1r2yZFu_HqwYChAM_Krx6H-b4t2d-LImL60VD-VbiMKeWvHrDjtGcKAz43Oh81SmeIa4aqAZXcXqp9jeA8gANbGPJVJmbIJu1vipZaCpEk219XCa_oP9S71qkB5CDZRpNU0ReQCMnSIaD334BClSvjigVPc5Eb6xiP_4Xma-qL16B5N92MRLzVrHplqIMBA5gAzdf6LPUJnxQKGwgEAFiUnP2ZMAIYXWBTzCO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a21d11818e.mp4?token=O-kzBmCV8Asm1ZJcmmeXOyPsPNl-YQokiKK03x8M2L3VKbgtqcMZ9KxGT9AeSWJgbDZh9SfFCwZak1S6uCixW6EvjG26HTHF66esDx5SU-F6qiq5wjTUMrXb0vZ4uKpyWHzsN0OJ6ik3TNp5B9QERHgmUotLAluiLgpXAaS1owcIsqtmR1oUwg54iQYX33pLS5Oe6HuJtV91_Jgw0ZMD1De3SrwyN3ILy7yL9oC8ZGfjj6klWZFyH3FVVV44m8loQB0ce_r45Z7xh8ozyLhII0sx1X0S7UdjxrZOB40t_MGD3Bhki-HiuiGmOIw3Z1E-N9PVbjjJIbpuZZKwdu7XiBBy3I2bacNzHTdaekQD00iXyVxu4RtXmQOs0qeiOD3Mz2uyzD-INzp7IaCxsaHQh_GlaxIvr9jD3CPCYQI416IS0zhSkkhn_JxrjDayQ2G8tTysb1r2yZFu_HqwYChAM_Krx6H-b4t2d-LImL60VD-VbiMKeWvHrDjtGcKAz43Oh81SmeIa4aqAZXcXqp9jeA8gANbGPJVJmbIJu1vipZaCpEk219XCa_oP9S71qkB5CDZRpNU0ReQCMnSIaD334BClSvjigVPc5Eb6xiP_4Xma-qL16B5N92MRLzVrHplqIMBA5gAzdf6LPUJnxQKGwgEAFiUnP2ZMAIYXWBTzCO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرصت سوزی عجیب رحمان جعفری مقابل دروازه پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105812" target="_blank">📅 19:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105811">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8676bf1957.mp4?token=HW_JumWO6gcAW7rVCqWsgw_adCOcwW5lZ3cyiduP0d5dAYQHObwG2hHsgKo-AJ_xQ1jnWooSorstEvM8qOKvZ_PGEH6dslBp0J7-_9zIklvBETWMztmtzEhnT5r7ATOqHudBYJ8z_NO11VB7Cdu8fHXUij1Lcv2TRtBPZvdZwuQaTZ2gLLwj7e9fN8I3t55h79LV-kk5zvcuQRFkZtPw1SMQWrPX1fAK70deyCauPeLMfRxLeKhu_L2JiwbXpXVQefRinYX4Dhuo_YE8GsGyo4r3tKIX4-tTUSFnmRAY_0xcUA6shyGmZLM7dLTyjg3hdjXG5WAGGZq79WSaLz18dZNtCPRxk1bgmr0_mPevP7Kul0DO4g2a_uaX9MAl5d4T-kOfwa9TmUHqQqOwe7-l_-uhNFUKpMyLx_sb5nv7BW8lbV7j-U6LxyHhMWPic2tKhl7O1aPFaCt4BtNrOZl8zzJDnA68SpiEHBvBdVtj6xtiUItcnzhuTQRq-Xrf-uMNMju0EHhqqy3gPo5WII0gdFnfoHl-HekSL251P4ehFYr7Al0IvyNxIXb0yB8IPFXgz1c3-d2t6gWFxN7zfGqdgRDV2ik-1A8ERqhAXuiezjjnrFwF3lsKbrTOU6jYFUfPzKoj5ngllnivj0aYZECalHZF1GjFTJIwBaqeH5sjHT0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8676bf1957.mp4?token=HW_JumWO6gcAW7rVCqWsgw_adCOcwW5lZ3cyiduP0d5dAYQHObwG2hHsgKo-AJ_xQ1jnWooSorstEvM8qOKvZ_PGEH6dslBp0J7-_9zIklvBETWMztmtzEhnT5r7ATOqHudBYJ8z_NO11VB7Cdu8fHXUij1Lcv2TRtBPZvdZwuQaTZ2gLLwj7e9fN8I3t55h79LV-kk5zvcuQRFkZtPw1SMQWrPX1fAK70deyCauPeLMfRxLeKhu_L2JiwbXpXVQefRinYX4Dhuo_YE8GsGyo4r3tKIX4-tTUSFnmRAY_0xcUA6shyGmZLM7dLTyjg3hdjXG5WAGGZq79WSaLz18dZNtCPRxk1bgmr0_mPevP7Kul0DO4g2a_uaX9MAl5d4T-kOfwa9TmUHqQqOwe7-l_-uhNFUKpMyLx_sb5nv7BW8lbV7j-U6LxyHhMWPic2tKhl7O1aPFaCt4BtNrOZl8zzJDnA68SpiEHBvBdVtj6xtiUItcnzhuTQRq-Xrf-uMNMju0EHhqqy3gPo5WII0gdFnfoHl-HekSL251P4ehFYr7Al0IvyNxIXb0yB8IPFXgz1c3-d2t6gWFxN7zfGqdgRDV2ik-1A8ERqhAXuiezjjnrFwF3lsKbrTOU6jYFUfPzKoj5ngllnivj0aYZECalHZF1GjFTJIwBaqeH5sjHT0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🎙
عایشه‌گل جوشکن، بازیگر و خواننده ترک، در گفت‌وگو با مجید واشقانی در برنامه «رُک» از ماجرای آشنایی و ازدواجش با همسر ایرانی‌اش گفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105811" target="_blank">📅 19:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105810">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZ0Gh6rzJWFxxT5u5qYT-JsFEsesnjqmWlVypnGSr1UjoG5Kb-eKm50TwnwVeC6h1XMADROBtvpwl39TDB_Z2JR-OBl_YMm4NgkUxN73BxuozC2enz0Z34T43KmWLHD2xur2ttZGveB7qy6btvcDqttrBoObDXAtwfR3ywmDzlLeVKeVh75EoX5C77_YFsH0EaX-ZaLl3AtbKx_jI3p87lgmjV3eXZwlXJ_tpBvTn26FASiyySQrxV1cO3QUZSVcPiPyy597y_lw3g626RgnS3T9o8RDJKBYyLBeMSOyIom53brLQBuWkBmKEox8bJ2EN9PMZh6GERbRUjdL4m02rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه موضوعی هست که فکر می‌کنم تقریباً همه ما به‌نوعی باهاش درگیریم؛ هزینه و شرایط بنزین.
شاید خیلی‌هامون هر روز درباره‌ش صحبت کنیم، غر بزنیم یا فقط سعی کنیم با شرایط جدید کنار بیایم، ولی در نهایت چیزی تغییر نمی‌کنه مگر اینکه صدای تعداد زیادی از مردم شنیده بشه.
برای همین این کارزار راه افتاده تا نظر و درخواست مردم درباره این موضوع جمع‌آوری بشه.
من خودم اینو امضا کردم و فکر می‌کنم اگر شما هم با موضوعش موافقید، چند دقیقه وقت بذارید و امضاش کنید. حتی اگر فکر می‌کنید یک امضا تأثیری نداره، همین امضاها وقتی تعدادشون زیاد بشه می‌تونن نشون بدن که این موضوع برای تعداد زیادی از مردم مهمه.
اگر دوست داشتید، لینک کارزار رو برای چند نفر دیگه هم بفرستید. شاید همین کار ساده باعث بشه افراد بیشتری از وجودش باخبر بشن.
🔗
https://www.karzar.net/346254</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105810" target="_blank">📅 19:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105809">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZ7sDUS6sKJuCjo_harl7wGl-eVae0kvM0RizmpbhhQ2NC34ou_ZeStF6p-1LbS8h_4rQjMpLflqGv9raD5rl8vP8q9uYZkXFLuM2D0X6YEacEeX-ODo6gCte5J-ENnePNRmdxXv2BCSa1NQ-DbQkMx9pne-gpO0YCnoxwE9rxCuKz7iYT2pj5mecDldPunEEe3OCFQZDe9Pq5VO9M4tHNxiiTtUuxL6m6kf4QzmIGBUTUhyqNO54NEUEOzxiy8zqlm0AXAk_ojEqbJai-n_oH82Bxggd1QZLKMTeMb6E2I7eOmGeTyS0cONreb1fnxvA4jvvAiD-EEIWqX77j49lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🏆
اگر حق رای دادن را داشتید، به چه کسی برای جایزه توپ طلایی رای می‌دادید؟
🎙
کیلیان امباپه:
🔴
من برای خودم برای جایزه توپ طلایی رای می‌دهم. این یک جایزه فردی است و باید دید که بازیکن در سطح فردی چه دستاوردهایی داشته است.
🔴
برخی می‌گویند که من یک فصل بی‌نتیجه داشتم، اما من هرگز برنده توپ طلایی را ندیده‌ام که تمام معیارها را داشته باشد. آیا بازیکنی وجود داشته که به طور یکپارچه توپ طلایی را برنده شده باشد؟ نه. این بدان معناست که همیشه کسانی هستند که فکر می‌کنند بازیکن شایسته آن نیست.
🔴
اینکه من بهترین گلزن تاریخ جام جهانی هستم، چیزی است که در ذهن مردم باقی می‌ماند. اینکه من بهترین گلزن تمام تورنمنت‌های بزرگ هستم، جایی که بهترین بازیکنان بازی می‌کنند، لیگ قهرمانان اروپا، جام جهانی، نمی‌دانم آیا کسی قبلاً این کار را انجام داده است یا خیر.
🔴
من کسانی را که با من مخالف هستند درک می‌کنم، زیرا این یک دیکتاتوری نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105809" target="_blank">📅 19:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105808">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32837e6be8.mp4?token=cI2rgbKxTonIdp22QEAUcpo9-QriJ7InDVMNWe--SMlLnED4COeCeC5pNTLQyJQJ-QZkBIQCixHmUVzha1HFJ_y1Y2Xq1HMG0J8en1fuxAQ0Yc1wB4Wk8seR1vSktiPmH_4EXLnaR9ff6Ja1WWB2vASu7pRRJ0wYtU65WZrPqcGK041l5oYAKItD6JwxOyzpxpqBcYWb-pFtx9VBMPhpC44FVyw1Wa4eUn0OQROgqjcZTBax53wy6RkjLaYrmOfjAJa9NzswfY-I8pcDqgSYR9upwm2-CSopHvZniJqvH_IA7_1ORYkXAD70J-FgfkXgH4fhvQYMQiuTKn28Hb2-zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32837e6be8.mp4?token=cI2rgbKxTonIdp22QEAUcpo9-QriJ7InDVMNWe--SMlLnED4COeCeC5pNTLQyJQJ-QZkBIQCixHmUVzha1HFJ_y1Y2Xq1HMG0J8en1fuxAQ0Yc1wB4Wk8seR1vSktiPmH_4EXLnaR9ff6Ja1WWB2vASu7pRRJ0wYtU65WZrPqcGK041l5oYAKItD6JwxOyzpxpqBcYWb-pFtx9VBMPhpC44FVyw1Wa4eUn0OQROgqjcZTBax53wy6RkjLaYrmOfjAJa9NzswfY-I8pcDqgSYR9upwm2-CSopHvZniJqvH_IA7_1ORYkXAD70J-FgfkXgH4fhvQYMQiuTKn28Hb2-zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
بازشدن پرچم 6 از سوی هواداران پرسپولیس و کری برای استقلالی ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105808" target="_blank">📅 19:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105807">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3392d48f0.mp4?token=OBLXf3P-jrh5pADKrlXbBuhNqSfuptC9Al8Ko_7DZ3KqQw2fUZ0FjqbR9n5H_YunQ93tk8z2yLOd5l6JVHZZ5b5EoBC3JTBGo5uyMTfXg6fxYZ8bscWXM8XNCnLWk24v5hzrst7ExCTqzHOqgVCBYu58tkCml86_0Da1NLWnsc83oul0rXgjAsULqJBnBSkrIZSrHvxUx8pd9cYjqJK15KlY7tj3TXpuoEENo-v-DOxLybo62LPzxozE0mV4m2rPg95j-uezlTpUHjtoBfOdF6EO5cbhWVa0VZ16e6WMDuSFeIoaTKJXVPqGmta-QOKElWjQNADNtfgz0SJwAph5ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3392d48f0.mp4?token=OBLXf3P-jrh5pADKrlXbBuhNqSfuptC9Al8Ko_7DZ3KqQw2fUZ0FjqbR9n5H_YunQ93tk8z2yLOd5l6JVHZZ5b5EoBC3JTBGo5uyMTfXg6fxYZ8bscWXM8XNCnLWk24v5hzrst7ExCTqzHOqgVCBYu58tkCml86_0Da1NLWnsc83oul0rXgjAsULqJBnBSkrIZSrHvxUx8pd9cYjqJK15KlY7tj3TXpuoEENo-v-DOxLybo62LPzxozE0mV4m2rPg95j-uezlTpUHjtoBfOdF6EO5cbhWVa0VZ16e6WMDuSFeIoaTKJXVPqGmta-QOKElWjQNADNtfgz0SJwAph5ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
هواداران پرسپولیس در پاسخ به فحاشی خداداد عزیزی به امید عالیشاه، کاپیتان سابق خود را تشویق کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105807" target="_blank">📅 18:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105806">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105806" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105806" target="_blank">📅 18:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105805">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4au16FRUIpVzLDDVRZRo9WrPuJnRDq2OGDzUD_54dWENce3dYgjtQaVY5L85g-yYgqwtA8a6iMWkt3C5otJNdD6Hrijs7jcl8BsDXrYCWq7h9B8SNYUyUtUlhZYmtHQKg4M7JSkAG6ULWZ9B8dwf6yDLatEgpHAc7FlL1w_zIXQcjYhHIsSWZukajQlEOd16JFJYMlZvsjAe-rm2uzjHdrifxjISd4jk6iMGyGT1xEDv9cm2BEaY0tq0J54bakdhLeX1LefCoCgrq6infbdkWfYTb8XCYMghvfRqjNaEn2iFh2T4r8eMifJ3zWOlausina6VUWCsDsukeT-A-qxpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105805" target="_blank">📅 18:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105804">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeAIjcaPSDb4z7Sx1d_0bdEl3GazV1_yWbWT2qkUxsdYdXyspSXrQ2A-gORq6B3IQj4kO07aD8eQ_dSFJ4mYtRFphGUiZ33f8cu9o1v6YqcZDL4yYDZjtjKmiOHibTl2l1TH6UVv647Ja5-0Oj1mSah68R93NNr6WYPusqPeidGCl8WO-5k-LsvymeFnyFyMnY9ziZQJDb6wa9qK96E5FWK8hu3rexXTtnpMKBJcmTEoJ1NoQFXEAmENUczBiPEzanoy-v2KeuEiMyuCTl5AXZVPUhXfafP5c197cTlezPmfmjkk4Ick9C78hNQu5PPbz6sx1wAeE3o6jnwuA0QCgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔴
شماتیک ترکیب پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105804" target="_blank">📅 18:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105803">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b66914acac.mp4?token=aRFmDZmb2lXdExf1uH7W4xncv_eALs7ugalpoZ4Yt3Uo11GhEIQoe-EPpvNIaSFNVz6AyWdJ8la-4T0kne4u-16vfLEIum39CmROdvNnuR4_oxfTcR6P4xFl4V7c4qXQTqNfW_evcYKJ4ldBw10t7gWlzqKLD4sZlJqW_EX8golY_itN_b1dCy1S0VPsY4e53OTtRmDdooVXQizwX45dnquZAxHnYKzgy7AHjba5cbYmMTwxPawxsDfnFz7DSam9IPdDgtOQ3Zxexds-sdDTi9XPjMSuEVDbw7EnDoqXKVKf7N135Ucd558m3MsPuGyXLOfUYNfYqZe968IhbIja6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b66914acac.mp4?token=aRFmDZmb2lXdExf1uH7W4xncv_eALs7ugalpoZ4Yt3Uo11GhEIQoe-EPpvNIaSFNVz6AyWdJ8la-4T0kne4u-16vfLEIum39CmROdvNnuR4_oxfTcR6P4xFl4V7c4qXQTqNfW_evcYKJ4ldBw10t7gWlzqKLD4sZlJqW_EX8golY_itN_b1dCy1S0VPsY4e53OTtRmDdooVXQizwX45dnquZAxHnYKzgy7AHjba5cbYmMTwxPawxsDfnFz7DSam9IPdDgtOQ3Zxexds-sdDTi9XPjMSuEVDbw7EnDoqXKVKf7N135Ucd558m3MsPuGyXLOfUYNfYqZe968IhbIja6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇺
🇪🇸
خولیان آلوارز در مراسم عکاسی UCL
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105803" target="_blank">📅 17:39 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105802">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdea9220e8.mp4?token=CsisuHAoNrZyEirsKQdYno_40xdYTPAqnFYSRDHt-8zC2YpU65sPGgA5XUXZrVesBeD9iSXxuh4r_aKxBcPny8uzQBI-I7353ktwfWKb7V97p7POYW4eZj5Psf_ACpOMXeb1Kx4B4N6IYP41TU4et36YqdHElMJGsBBNlUjz-4ER5w5bwZOTfT_cuZWvTPiLVKlIgEvGqtHhETV6Yr_glZWGCRkyfgD3GEeEyhKv2IEBcNv7qP3q45dZL7Kyc3Rq5unugs-cO72-cqWXdeowa5lFyy1inpliiXzUTXPYqJ0F6MtMRCIaJk7ksz1ZDjDP0la7IgTV_zRNAe9_Yyjc4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdea9220e8.mp4?token=CsisuHAoNrZyEirsKQdYno_40xdYTPAqnFYSRDHt-8zC2YpU65sPGgA5XUXZrVesBeD9iSXxuh4r_aKxBcPny8uzQBI-I7353ktwfWKb7V97p7POYW4eZj5Psf_ACpOMXeb1Kx4B4N6IYP41TU4et36YqdHElMJGsBBNlUjz-4ER5w5bwZOTfT_cuZWvTPiLVKlIgEvGqtHhETV6Yr_glZWGCRkyfgD3GEeEyhKv2IEBcNv7qP3q45dZL7Kyc3Rq5unugs-cO72-cqWXdeowa5lFyy1inpliiXzUTXPYqJ0F6MtMRCIaJk7ksz1ZDjDP0la7IgTV_zRNAe9_Yyjc4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
💙
پژمان ماندگاری مدیر رسانه ای استقلال: با صالح حردانی در ارتباط هستیم هم من هم باشگاه، ولی باید زمان بگذرد تا اتفاقی که بین باشگاه و حردانی افتاده است حل شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105802" target="_blank">📅 17:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105801">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e983fd5a.mp4?token=EM4TLBeEMQn-1E0panmcW4eZ-IYx1Mabukbj6Okng5H_u431QCyVuHnaMWT1UypJeUijZpfwEZe3MUc_4bD5VxA2lQxVr72KFGFxC9DdVAcjUfphQib8zqXPd1YVnWDes04e9IE_5hOtO1aIg2bViTTsKX07EbxdjyssDir6-xKP1JIMKpgRmKMD-3ivb739XdJi9EEARbHjSgeQU0oqlAYYn2LAzCehN3-KC5Nxx_QCa6AOetsDZW_o2SRS9pzHfNWlaAjRIniKrQKrHWi4m9TDypem39mChSKv19Iqxj_yngcSciRX1oWGB3N91kGBcDweJzoGGDZsLINbK3MkGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e983fd5a.mp4?token=EM4TLBeEMQn-1E0panmcW4eZ-IYx1Mabukbj6Okng5H_u431QCyVuHnaMWT1UypJeUijZpfwEZe3MUc_4bD5VxA2lQxVr72KFGFxC9DdVAcjUfphQib8zqXPd1YVnWDes04e9IE_5hOtO1aIg2bViTTsKX07EbxdjyssDir6-xKP1JIMKpgRmKMD-3ivb739XdJi9EEARbHjSgeQU0oqlAYYn2LAzCehN3-KC5Nxx_QCa6AOetsDZW_o2SRS9pzHfNWlaAjRIniKrQKrHWi4m9TDypem39mChSKv19Iqxj_yngcSciRX1oWGB3N91kGBcDweJzoGGDZsLINbK3MkGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
💙
پژمان ماندگاری مدیر رسانه ای استقلال: در خصوص ماندن یا بازگشت صالح حردانی جلساتی در حال برگزاری است اجازه دهید خود سهراب بختیاری زاده در این خصوص تصمیم نهایی را بگیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105801" target="_blank">📅 17:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105800">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533e25adb5.mp4?token=P2-HON9MhJ32qGhMRMffskdayOqNuIZPTzogvmIKgee6qD7k7MwWNUGH1VamMxXY4x8xW-zHmcPsLiuDbCBNteBsrjCXyAV4RfG9YCaLhmXoLl6zSEVHyZ3GHuTf3aB5u3Dr19kCKHJZVE1QqcFrG7CnTL5k4oDElXKBVi4AQrb9razmc7QGM15p-cKCnRMAfcjpQXQR8yNuSb3uECv3ueSudBLHYicN9ElpjRXe4RaV7nxlHIqLubhY61oPS-F3OPXK-8VZ0tbSsnhLzh6dkhguzpSSwphDh8q_cDfbpL8gaELVCroZUYttUPWREi09m6eonkzoXDWRgeOLFsd7Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533e25adb5.mp4?token=P2-HON9MhJ32qGhMRMffskdayOqNuIZPTzogvmIKgee6qD7k7MwWNUGH1VamMxXY4x8xW-zHmcPsLiuDbCBNteBsrjCXyAV4RfG9YCaLhmXoLl6zSEVHyZ3GHuTf3aB5u3Dr19kCKHJZVE1QqcFrG7CnTL5k4oDElXKBVi4AQrb9razmc7QGM15p-cKCnRMAfcjpQXQR8yNuSb3uECv3ueSudBLHYicN9ElpjRXe4RaV7nxlHIqLubhY61oPS-F3OPXK-8VZ0tbSsnhLzh6dkhguzpSSwphDh8q_cDfbpL8gaELVCroZUYttUPWREi09m6eonkzoXDWRgeOLFsd7Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
پژمان ماندگاری مدیر رسانه ای استقلال:
🔺
مصاحبه پخش شده از بهاروند در خصوص قهرمان لیگ تقطیع شده بود/ آخر مصاحبه می گوید که هیئت رئیسه فدراسیون فوتبال می تواند دوباره در خصوص موضوع قهرمانی لیگ بررسی های لازم را به عمل آورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105800" target="_blank">📅 17:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105799">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b75db3430f.mp4?token=CCBPyMk66kYdDQK_IJ9tAALuKWMyAC-jWb3w6-1nQm5t9Bv8lOGLJpv8X5GOYf7fXc0E1d_p6jON7bmeFix67Ee42shv_wQlEa_vw_h5dPoSGTk1oo9EJovy4cYF5t8qwNuMwo4SY6e0ZK0Mt6ChTqWQ89N5EOIdCdPpfxy_6N1rFk7aJG5NbEGVv0rbc_T__gSsFlx4ZzRrbBYPKpFgeS_W7GHIWGldNIFhsXrjWxCP21UBtOWlJAMozJcN8ccKohPihthsavhdvBnDnUkQALgNS95f8BxL-gJcTrUl4T13G1USKNQuA7OrST-4x1iqsSqQgigbFJ6wbuPEgcedsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b75db3430f.mp4?token=CCBPyMk66kYdDQK_IJ9tAALuKWMyAC-jWb3w6-1nQm5t9Bv8lOGLJpv8X5GOYf7fXc0E1d_p6jON7bmeFix67Ee42shv_wQlEa_vw_h5dPoSGTk1oo9EJovy4cYF5t8qwNuMwo4SY6e0ZK0Mt6ChTqWQ89N5EOIdCdPpfxy_6N1rFk7aJG5NbEGVv0rbc_T__gSsFlx4ZzRrbBYPKpFgeS_W7GHIWGldNIFhsXrjWxCP21UBtOWlJAMozJcN8ccKohPihthsavhdvBnDnUkQALgNS95f8BxL-gJcTrUl4T13G1USKNQuA7OrST-4x1iqsSqQgigbFJ6wbuPEgcedsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
هوادار پرسپولیس
: ای کاش خداداد عزیزی سُر می‌خورد و آن گل را نمی‌زد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105799" target="_blank">📅 17:26 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105798">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a65105bf5a.mp4?token=RIz0g9GR5U6fs0JmXAgRLUhGhp78iMeDSjQ56FgBUBllXspoMM129D9Ifgaz7W2vu2AA9gQ9eIYmFRHRYlVcavp8agoAkxgCiqVJZLhhz08z7NP9NP6A-gJouxElrJBZ9o0L3NIIFv0bZ8r2jC8SPq9lnkPFZwvcRjaqzDAgrY0fYpqLoIss0tQOy-lszsvnZ9OX1LDdSr2bL-HxJde6yiBBy2fI0KV-o6nDBQ4bpKZk4Zh8CAmIi6Hp2qqus4q86Th3D_SGbl7hXu4Ejo1rnsereQNeqGGTuKWtBdtYjiwZwh28GE0_nPCgPspwYtCnyXhzC-jbHyvyLgtZLSjvOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a65105bf5a.mp4?token=RIz0g9GR5U6fs0JmXAgRLUhGhp78iMeDSjQ56FgBUBllXspoMM129D9Ifgaz7W2vu2AA9gQ9eIYmFRHRYlVcavp8agoAkxgCiqVJZLhhz08z7NP9NP6A-gJouxElrJBZ9o0L3NIIFv0bZ8r2jC8SPq9lnkPFZwvcRjaqzDAgrY0fYpqLoIss0tQOy-lszsvnZ9OX1LDdSr2bL-HxJde6yiBBy2fI0KV-o6nDBQ4bpKZk4Zh8CAmIi6Hp2qqus4q86Th3D_SGbl7hXu4Ejo1rnsereQNeqGGTuKWtBdtYjiwZwh28GE0_nPCgPspwYtCnyXhzC-jbHyvyLgtZLSjvOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدون‌شرح :)))))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105798" target="_blank">📅 17:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105797">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce531ef9e.mp4?token=WC70BD_FUEeQyMf_yk8rzbA510to-y1aAImnqAH-BjnnihBpN0m-qgxt9I6TqZUuPDKEV7KF20JrTOLiZvSK0iEQrch2b-nRUgNjVoJM7BZRGAgXBAsNDZnGQL69xds0fiywycs-ViC8X0o6pp_iwK5kRc68cxgQk1OsDP3yJT4gygPSxvJVeHaYQSoQcLKXNPz_92y8lm2FIVMnrZt_kQN_tl8h9ahv2xniHEq3-2L4abXsiYsng24unVUS9azgSSN4miqnmRJMrMJdQCs9yKSyXBPPg4kauqeoMgaSrPikabsVfUURJn6RBmkZuOP1exlo6JaX2QJ78qGXLbbryw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce531ef9e.mp4?token=WC70BD_FUEeQyMf_yk8rzbA510to-y1aAImnqAH-BjnnihBpN0m-qgxt9I6TqZUuPDKEV7KF20JrTOLiZvSK0iEQrch2b-nRUgNjVoJM7BZRGAgXBAsNDZnGQL69xds0fiywycs-ViC8X0o6pp_iwK5kRc68cxgQk1OsDP3yJT4gygPSxvJVeHaYQSoQcLKXNPz_92y8lm2FIVMnrZt_kQN_tl8h9ahv2xniHEq3-2L4abXsiYsng24unVUS9azgSSN4miqnmRJMrMJdQCs9yKSyXBPPg4kauqeoMgaSrPikabsVfUURJn6RBmkZuOP1exlo6JaX2QJ78qGXLbbryw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
بعد از دعوای خداداد عزیزی و عالیشاه آدم ناخودآگاه یاد این صحبت‌های اسطوره علی‌دایی میفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105797" target="_blank">📅 16:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105796">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc7d165fd0.mp4?token=idxTSOrbrC-9ugVWC2k7Cb01-a-iKYh8CjiNuy2RFjLWbnyz5XN3qmjuBHVYcqyvnxCOkVxMJzbDUDjNBHoR2nWsPmKCvpQBmq4jISREmjtXp3B6Ao3Lxm-xar2Lxid4MbiarwpHonwiiqmOeVWx7K0QUGNN94KZFAM6KAKUrUdEV9rXFFyRAgZU3oc1mDXdrUzH5ohn_EKgeSuHdP2GostTzJl_C4LdiTDmcuurOd0Rt-DBXCjRL98JdfiyYm-Q0Gyat8bRiYRVdTho64hgU5Q1i219a8z_jBs9YXD7j1qQTH9wJu9pO6e0ljWH55wq0tLDAMIWO9XbbBZwJ4Qlwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc7d165fd0.mp4?token=idxTSOrbrC-9ugVWC2k7Cb01-a-iKYh8CjiNuy2RFjLWbnyz5XN3qmjuBHVYcqyvnxCOkVxMJzbDUDjNBHoR2nWsPmKCvpQBmq4jISREmjtXp3B6Ao3Lxm-xar2Lxid4MbiarwpHonwiiqmOeVWx7K0QUGNN94KZFAM6KAKUrUdEV9rXFFyRAgZU3oc1mDXdrUzH5ohn_EKgeSuHdP2GostTzJl_C4LdiTDmcuurOd0Rt-DBXCjRL98JdfiyYm-Q0Gyat8bRiYRVdTho64hgU5Q1i219a8z_jBs9YXD7j1qQTH9wJu9pO6e0ljWH55wq0tLDAMIWO9XbbBZwJ4Qlwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
بزرگی و مردانگی یک بزرگ‌مرد، با حرف‌های پوچ و توهین‌آمیز یک آدم بی‌سواد زیر سؤال نمی‌رود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105796" target="_blank">📅 16:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105795">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/608b5b0627.mp4?token=BWEPw6-wyHpkMsPMOyrYdVn5WxFcQcplTcwKPHrVtgf8QEm84xtYcDiVI3Pi-93FII1bS8Ab_6F0zKaScFJAF3aYwhnJNQ7tL25C9-Qdv_Yw9nQ6vg1QQMKxG4K0k9M4DWqaUGrZlLPr1wnaUBYYTFZCHz_4_QdmWRJZ6bsvJz9m77UTssUkNf3y2c0mQ4Y6G7HNasDlKoQwaS2regfPMdFOskRu5cWQZi2r_iM_txujk3Pd8MbazJ33fvaGGncznMUZljDGd42Wn-UIkMyxWwV3QpNdIRn04z6zkTo5TKEgm124jZXwM7pCYsK9efAGZIIl8EQqwgNKnrZ0AHI2aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/608b5b0627.mp4?token=BWEPw6-wyHpkMsPMOyrYdVn5WxFcQcplTcwKPHrVtgf8QEm84xtYcDiVI3Pi-93FII1bS8Ab_6F0zKaScFJAF3aYwhnJNQ7tL25C9-Qdv_Yw9nQ6vg1QQMKxG4K0k9M4DWqaUGrZlLPr1wnaUBYYTFZCHz_4_QdmWRJZ6bsvJz9m77UTssUkNf3y2c0mQ4Y6G7HNasDlKoQwaS2regfPMdFOskRu5cWQZi2r_iM_txujk3Pd8MbazJ33fvaGGncznMUZljDGd42Wn-UIkMyxWwV3QpNdIRn04z6zkTo5TKEgm124jZXwM7pCYsK9efAGZIIl8EQqwgNKnrZ0AHI2aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دعوای خداداد عزیزی و امید عالیشاه از این زاویه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105795" target="_blank">📅 16:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105794">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCLpJ1Bo0_gdDRvp_nhJhRZa4ik5zi0FadlLe2JhW-5V0r3_32WukpkFqb-wjlg-oSeimD2tUOFtNDfDs9q9KV9FH6Sxwu1XYI0PiqrAcu5EYWMeoWTlmD9K70RaTaZ5OZCUpmnrnw58KdRymYQOEtW_S5AdZUgKdQO7iWxsagVKRCoF_piCGOC-HP2ceVJlkfn7LNYcybHc90EQ1kfOcF2WAXB2ciWNmsujCXE1g_J3CxuEFP9wgLcGsVWHnWTk-0S8igmOlFAuV7nr3qRFRdA2PPMRgenNWklzPbwVxDrNBcDQsBgq4nqgjGIZp4zkk1I41S23K3wy8twxxdpL3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔵
هوادار جذاب و شیک تیم‌الهلال عربستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105794" target="_blank">📅 15:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105793">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72559f2230.mp4?token=hqPwtHSwuzqUUsf3TSOi_hkwltRBvkpEdCemLVwvzPWu-Fi27k1wWy4OxfABSZkCgHqEwqIJkrtQsQQ2YwLXAxq2RLQHjcE67QPMrWhbIOpJRnXP9uT_mB_0Xa6jhpXTlYl4bmr1UItAesMRLATjwVDzLotYXB6b0CVPJzvA7F9c8nX_RK8UyiO4ZMZeCseaR5tndqiUEz-7mBiI2SlsfNxT34SzMNwsenwvP_7coydSKogrFfkGcNMAHKrYFE-dWcRV6fdV9sNfswVKX8BI_YOYUt-lYMrJDzBgvCR3NIqxwFzeVsA7-BF5xA7ZSrMaYaBlO8FrXjaBTiO7T6Gpcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72559f2230.mp4?token=hqPwtHSwuzqUUsf3TSOi_hkwltRBvkpEdCemLVwvzPWu-Fi27k1wWy4OxfABSZkCgHqEwqIJkrtQsQQ2YwLXAxq2RLQHjcE67QPMrWhbIOpJRnXP9uT_mB_0Xa6jhpXTlYl4bmr1UItAesMRLATjwVDzLotYXB6b0CVPJzvA7F9c8nX_RK8UyiO4ZMZeCseaR5tndqiUEz-7mBiI2SlsfNxT34SzMNwsenwvP_7coydSKogrFfkGcNMAHKrYFE-dWcRV6fdV9sNfswVKX8BI_YOYUt-lYMrJDzBgvCR3NIqxwFzeVsA7-BF5xA7ZSrMaYaBlO8FrXjaBTiO7T6Gpcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
جوری که دیشب هواداران والنسیا هنگام تعویض شدن پدری ستاره بارسلونا تشویقش کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105793" target="_blank">📅 15:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105792">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2073e1633f.mp4?token=ApgOskQhJ73cndw7DOeAsGOanB4kU4SmvPte4EjiMJsnVWEtTO2teKdy8aMo1U_5iIHd1IWu9XWFfkOFwGiVV2Yrn_ZF5OG72TCF1iKNkHkiEo6a6mYkTCoSIG6KhC8QEeQTSQvkM5W8_L9XXZwNMP0YqIPMblkMVEsocXebFik5cW4mFnDWuHKwEWcNdZvPMdnVhZQNlCeeROL1F_9G9pjxCCgLWEljgpjmVgdA_TJmEGal42SuJ6VuMynNsSVw56EctyTdaBunNbMnNEVlA-E3J5Fqi9BdI-7RqQmSeOnktlW_kGFojZpaapWJ-6EPv0qZfuhZs0OjmOwDJuUmOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2073e1633f.mp4?token=ApgOskQhJ73cndw7DOeAsGOanB4kU4SmvPte4EjiMJsnVWEtTO2teKdy8aMo1U_5iIHd1IWu9XWFfkOFwGiVV2Yrn_ZF5OG72TCF1iKNkHkiEo6a6mYkTCoSIG6KhC8QEeQTSQvkM5W8_L9XXZwNMP0YqIPMblkMVEsocXebFik5cW4mFnDWuHKwEWcNdZvPMdnVhZQNlCeeROL1F_9G9pjxCCgLWEljgpjmVgdA_TJmEGal42SuJ6VuMynNsSVw56EctyTdaBunNbMnNEVlA-E3J5Fqi9BdI-7RqQmSeOnktlW_kGFojZpaapWJ-6EPv0qZfuhZs0OjmOwDJuUmOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🇪🇸
وضعیت شاهکار این‌هفته بارساییا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105792" target="_blank">📅 14:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105791">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miGeGHKDoMXRwcODz4Bgco0sruJOrEN-ROuDoL5rsAOA3qwe5UWpwHoyjsshuueXW1KwJqB54tfQwSTdTA5ZXPszaYEH29bxFc32tEt2f-1Uue1Ur68piXgftLjrt5ueloN1etd0kWkDSnx0x9AF_YlHDtlOwvVVBBJW88h9jAA63ZvkTUxujr-wFqA-MxhvTuoxN65uBF-vpNHJp9mStggmzg7LgFXJf4DFSSWc6TZxOOlQMcewDyWMcBspdcKU1MZjB1yTvnEOexzLLiI1yFaVXYQyWYUmE2LoVskJC2Qo32TZmvlKVArmXae8zl3ScDc4jdhOnrinO6Qf6gec7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تعداد بازی‌های لازم برای رسیدن به 300 گل
:
🇦🇷
مسی: 365 بازی، 300 گل
🇳🇴
هالاند: 384 بازی، 300 گل
🇫🇷
امباپه: 398 بازی، 300 گل
🇵🇹
رونالدو: 499 بازی، 300 گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105791" target="_blank">📅 14:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105790">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7j1rB590KW0zz2ODRRTCdLfEjrpL1un8u_d7NcHsX0Fm5HrANGHqBQz13vZaLK0tGwY5YVNKpJLAYC0ct_e3vo2RXw5MbRHOtdV5ZT71-XaYVEnc6k-kxjKNENtyMiQ2sawZ46BTEvuLnB00wkoF5Qs6dnr-7t5iYuSLVpud5YqLMUkpUD122Mx57e6ZxPQnqNU2DIfO2Uf36T-BQRakhZOseHeUyz6g3ZtXH3zLqBLrk38sZjQaWHHYoZddS0gP6ayxE479QwHSZmFWrt-mRrQGixOScLPWi0vCgbJBfeB9nm-Jn9wDIqbWVOlLvhQnwS7-MHR2-yK-NFdHqJk0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇭🇷
🎼
لیست تیم‌ملی کرواسی برای فیفادی با حضور لوکا مودریچ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105790" target="_blank">📅 14:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105789">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJ91y3WvgMKNsEpjsc-oeAHag9uuGSe_Ot53oxcd6R0__TYi5-V7zncfDA2X6EA-to1j9siCBp2sKWZUXSdg9bP4IxIjUUXQyLpI8Tz-Z54WP0ipMWl1yMvL-AUGnjhxVNZNbp4XmsVXXcrkEn0c7SW4wzLGem6qKDTp7iHzZgMXmExmaI5qj2_yn2v3yVgAXoub6LzxRpuOzAbMEht1jsWvocm3WFWqY8opBYfOk9llgvXaIFirAPitycgaSO6xMogC_vc4055OoE7tk6yVNh7l94viyKVF1URkDAVJrbi-ADO38bsSv5LGYut8y9VqTh_6E0O9e_V-odPB8SmJ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🇪🇸
این تنها سومین بار در دوران حرفه‌ای امباپه است که این بازیکن هم موفق‌به گلزنی نمی‌شود  و هم چهار موقعیت گلزنی بزرگ را در یک بازی از دست می‌دهد.
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105789" target="_blank">📅 13:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105788">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51d2063588.mp4?token=l2e2_zSPz2T6Nkd9Z1gkzarFb6tABe3FtCgIhNl-jQYGLseFUmHb-DPFquqMM3rWcz-7OFpqgTlwkkvconr1V1TU7hksTcMGXAbL17SJBhx2bGZeoDUc4mE29_Il1WyIuUfQ0nJcQ0j2uF319fUx0p23gpa-wYFw32fn4y5zGC4ZiOesi_wzL4mFzyx0zdanKVzHw6_Agt2HRjTRdfXddba4l9bTnTguZ0gwCjk-clXVBV5uV8hLPXesrEThEvxzCqTX-fdnXz6Flp1zi2iAbdYHyZOX5R2Ob4QeD0bg_jt5ycuZXidDoBxHISxThW-ql3PtXzcVdBFnYYe6BMRB8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51d2063588.mp4?token=l2e2_zSPz2T6Nkd9Z1gkzarFb6tABe3FtCgIhNl-jQYGLseFUmHb-DPFquqMM3rWcz-7OFpqgTlwkkvconr1V1TU7hksTcMGXAbL17SJBhx2bGZeoDUc4mE29_Il1WyIuUfQ0nJcQ0j2uF319fUx0p23gpa-wYFw32fn4y5zGC4ZiOesi_wzL4mFzyx0zdanKVzHw6_Agt2HRjTRdfXddba4l9bTnTguZ0gwCjk-clXVBV5uV8hLPXesrEThEvxzCqTX-fdnXz6Flp1zi2iAbdYHyZOX5R2Ob4QeD0bg_jt5ycuZXidDoBxHISxThW-ql3PtXzcVdBFnYYe6BMRB8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
😂
امین‌رضایی یکی از اساطیر سندروم‌داون در دیدار با علیرضا منصوریان در بغداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/105788" target="_blank">📅 13:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105787">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/737dc646bf.mp4?token=Er91YxPHumBguwWUF5Qvhui-UvHi8FhgvuEQdylHXPi4Q4OBVYeFKi1PhT4NrWHR4MFYIhyUaJ9jxYVq0D6HaL-69BIoiL5HmnRTLAI4cmUYAYIzyv0ZeMOoGK32r9ugVE6vvYxOlEemBtjATLdV3MjMnwmJ0ejCI5ZX0fiV7qL7l7ZMTAs7f5ns62doCM4Y9LYuPb-xsd_LDt16v0kYRFJXYFsuterdJz7uozWjHL82XR8ZLfvbybrUOVA-Ye7THi5tr8OSgbQ79lJR7oj5eBazZUfq1DyG1EYRokkjTSOHlY4YY4_gGThOBcj1uYISmQ3rnKXKe6MSq721NLh6IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/737dc646bf.mp4?token=Er91YxPHumBguwWUF5Qvhui-UvHi8FhgvuEQdylHXPi4Q4OBVYeFKi1PhT4NrWHR4MFYIhyUaJ9jxYVq0D6HaL-69BIoiL5HmnRTLAI4cmUYAYIzyv0ZeMOoGK32r9ugVE6vvYxOlEemBtjATLdV3MjMnwmJ0ejCI5ZX0fiV7qL7l7ZMTAs7f5ns62doCM4Y9LYuPb-xsd_LDt16v0kYRFJXYFsuterdJz7uozWjHL82XR8ZLfvbybrUOVA-Ye7THi5tr8OSgbQ79lJR7oj5eBazZUfq1DyG1EYRokkjTSOHlY4YY4_gGThOBcj1uYISmQ3rnKXKe6MSq721NLh6IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🇮🇷
حمایت جالب هوادار استقلال از امید عالیشاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105787" target="_blank">📅 13:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105786">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ca5c3fb8.mp4?token=V_pfN-wTnk6P1fJNbScmePSvjfqLFBt_nppe2Ncl9dlL144XqkkSxuq_ugx2V8RPjyZ-cwIc64WdEYGgmUiLTO0WhvEdvFWOPF4UXJ7f3LIVlHGKVphwlNeC3rTZH-OIdo37azy8M0EteJTCvsyZmwzfOjFp-tt136htnTjx8XMoMtbJ96STYbqnUXmvDbASVDfTtFcP4ixaX6vMjRq54AopGUZiYXBDz9JbKVNd2rscfzvBkVvzTu2OueTaZZScav74k4OlIc_XcH-Heh3GAKMmHgMw_Wm7rm517f1_uts9HIc07BW_pJltjjlYnLdKx3om0rw1PjXfKbZDipIk2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ca5c3fb8.mp4?token=V_pfN-wTnk6P1fJNbScmePSvjfqLFBt_nppe2Ncl9dlL144XqkkSxuq_ugx2V8RPjyZ-cwIc64WdEYGgmUiLTO0WhvEdvFWOPF4UXJ7f3LIVlHGKVphwlNeC3rTZH-OIdo37azy8M0EteJTCvsyZmwzfOjFp-tt136htnTjx8XMoMtbJ96STYbqnUXmvDbASVDfTtFcP4ixaX6vMjRq54AopGUZiYXBDz9JbKVNd2rscfzvBkVvzTu2OueTaZZScav74k4OlIc_XcH-Heh3GAKMmHgMw_Wm7rm517f1_uts9HIc07BW_pJltjjlYnLdKx3om0rw1PjXfKbZDipIk2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شوخی سمی همسر دیوید بکام با ظاهر عجیب محصول کشاورزی شوهرش
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105786" target="_blank">📅 13:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105785">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4072bbde8.mp4?token=v_p3uhT1VJRAVc4nMFEmhft3PeFyPK1qZssCxDYsIycrd7G2tUQN62J-j7PUvcL4glwq7SICB8oaNmJSRIjeZ1k2HY84G52LOsn_yL1NzOI2ovjVn7B8n28lvICKdGLkKJg0mxfcxCndisyy3JGIvujuOylBqAADA_6Gn8RM0Q2K6ZCW60L4fEm-wpicT46Vh-pSvcpLqZ9sQjDhfueDmEuQmb-KWu4SrDI_bNdm39SdgtLWv4FSR3_FpJEeETOJdre0hOCCbN-6VjQOQjZuu2QCqxb_qs7iU9A-jlbOjwCqxSUi9_Z-umeaT1aCP6QakzJdfcyuTn_-VWAc9d0tQjaVA30uvf9TZJhRoKVq8E57d_HFoTKrOnaaJm99XpYiR5MthxQS4MKEZ63QegF52lBmSGY165_qANigpgKekgYAhIhPNyCTmXGuKoQpgMyHX33MOlg-i8C-Vf0_Va_HyruowwXahrr8z1S2PkOP9bQFvk0o5yB1Qo4O-EKMy2zftHipzNVhky7gyDPehgCkfNzHGrvNYY8CdcCP3vJdSK_hJ2eOFB6CWfWq8LuTr6l0v5f13hQIeg_PyciDx765vulK8VrhuR4yNT53SvoqzdjL-a-DY3naMzbqAIifIAJR3gZShnZgY0YrQlcJGAYdoKiI7pfTntroVg4ZwTqq_i4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4072bbde8.mp4?token=v_p3uhT1VJRAVc4nMFEmhft3PeFyPK1qZssCxDYsIycrd7G2tUQN62J-j7PUvcL4glwq7SICB8oaNmJSRIjeZ1k2HY84G52LOsn_yL1NzOI2ovjVn7B8n28lvICKdGLkKJg0mxfcxCndisyy3JGIvujuOylBqAADA_6Gn8RM0Q2K6ZCW60L4fEm-wpicT46Vh-pSvcpLqZ9sQjDhfueDmEuQmb-KWu4SrDI_bNdm39SdgtLWv4FSR3_FpJEeETOJdre0hOCCbN-6VjQOQjZuu2QCqxb_qs7iU9A-jlbOjwCqxSUi9_Z-umeaT1aCP6QakzJdfcyuTn_-VWAc9d0tQjaVA30uvf9TZJhRoKVq8E57d_HFoTKrOnaaJm99XpYiR5MthxQS4MKEZ63QegF52lBmSGY165_qANigpgKekgYAhIhPNyCTmXGuKoQpgMyHX33MOlg-i8C-Vf0_Va_HyruowwXahrr8z1S2PkOP9bQFvk0o5yB1Qo4O-EKMy2zftHipzNVhky7gyDPehgCkfNzHGrvNYY8CdcCP3vJdSK_hJ2eOFB6CWfWq8LuTr6l0v5f13hQIeg_PyciDx765vulK8VrhuR4yNT53SvoqzdjL-a-DY3naMzbqAIifIAJR3gZShnZgY0YrQlcJGAYdoKiI7pfTntroVg4ZwTqq_i4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
فرشید باقری، بازیکن پیکان: خوشحالم در پرسپولیس شاگرد گل‌محمدی و مطهری نشدم. اینکه بعد از جدایی به همه جا زنگ بزنند و من را خراب کنند، حرکت درستی نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105785" target="_blank">📅 12:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105784">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfgLZkIdyt0mui7VLjMTug4jmgRdlFZKEA5cBDx6sK4aMTg6mHBJgyiuxYlZhtnTxCrgh4FMwbL6tj-AIATuBKLtP7dG6995OjJxorfUwnffKc-jH_W0_kHeR7JeHuORKKGIl2w_u1ParuvD-iPvF-TRl6tn-BuJt8RGQzhU_GmlC7CNeTeer8KNC4pfkOeT5txcHdhQZEJ877PLO1YZCKrzKLDl35LYr39IHNQXLq4owJAJzqQoPzWbY9O2psKqq9C6ipP8RfQQE2sATG7BTpmIQc5XlipkrhARf0_QCCclEA2mMi47J7jgFIgea2r5QkWu4UatkfyPiRuJt96T4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
👩‍💻
💡
یه راهنمای فوق‌العاده کاربردی برای دوستانی که با برنامه‌های آفیس سروکار دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105784" target="_blank">📅 12:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105783">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4331728b0.mp4?token=eagh5kyMnqr1F641Pmvt3eRxG1FSls6zxBqLzkAVaIFRoYkk5jC8I5vfzfx677Nf8d9qwGPpSps6ewVC1Qw1KKKllRLa9hqzg48GywfD_XfkRgmKs03eiznZrcixRqWxzYs5W85-bQfO5B-xnRR7ynVt__XYdAB1gm42cgnDoAhhKGWG1TQTiligKcZXYNJHmLP4YKlTNawF0ZfDz8WPc7sEfgtZm7jwQPrwdO2OgOMou4I5lspFyaUmUE-nWmNPsqWjycAM4F2bCsguSIHFdJhWIRbUdYR5KRUyrRS2Q-9XNUR_eeQuhab1jRZozvNeyTzNgOfOqGcCkRmqsXFDKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4331728b0.mp4?token=eagh5kyMnqr1F641Pmvt3eRxG1FSls6zxBqLzkAVaIFRoYkk5jC8I5vfzfx677Nf8d9qwGPpSps6ewVC1Qw1KKKllRLa9hqzg48GywfD_XfkRgmKs03eiznZrcixRqWxzYs5W85-bQfO5B-xnRR7ynVt__XYdAB1gm42cgnDoAhhKGWG1TQTiligKcZXYNJHmLP4YKlTNawF0ZfDz8WPc7sEfgtZm7jwQPrwdO2OgOMou4I5lspFyaUmUE-nWmNPsqWjycAM4F2bCsguSIHFdJhWIRbUdYR5KRUyrRS2Q-9XNUR_eeQuhab1jRZozvNeyTzNgOfOqGcCkRmqsXFDKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرد آلمانی بعد از شروع فوق‌العاده در لالیگا و ۴ برد متوالی و ۱۷ گل زده: تقرببا بی‌نقص بود، چون هیچی بی‌نقص نیست و همیشه جا برای بهبود هست!
بارسای تقریبا بی‌نقص هانسی فلیک در صدر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105783" target="_blank">📅 12:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105782">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105782" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105782" target="_blank">📅 12:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105781">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYb4_rO5sMc7bT5jHZZSIJQnV9WZMPJkSEK63aqHXMc5KIEm-iuVXf9AdbfNAal5kJeyX9wnUJBxd5UPY5jKr4n0VfF_xs-ghZDLySqQi1JMFk4p5ix28aIrdF87wdX5BdDugfVktlAYN3c6k4ikUbI89ZZQP01Te6mT_0o7gkNRGWYsyKLgucvQpFmGZ_xu6-0O0wdTCuduIdC6uW9HZfkN9ug_1XonQCrtbA2a47PsRWdWSHkzSdM-oRhO1HJXYD19eFfOqlBbB-JAtzchfx68nNE_tP9OAGOkE7juWDhemsferZ7PWtke77-OGgn4MHE4mpUC75e3II7I0Vs5ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
ذوب‌آهن
🆚
پرسپولیس
⚽️
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی
به آمار ۲ تیم در در این فصل
ذوب‌آهن: ۵ بازی ۱ برد, ۳ تساوی، ۱ شکست
پرسپولیس: ۵ بازی ۳ برد، ۱ تساوی، ۱ شکست
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105781" target="_blank">📅 12:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105780">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1732fa7bfa.mp4?token=W0kZNMEP1Ss0OUvj2jStqd1auFkJxUK-acUXPHTinqIN-CnEsyV6h35iXR0pQesoG8fpbzxPwR0nZtNj6NlwcAEATVIB6uWv6pcpbSAsGZd3xD6ELqXHVDdMqmIbDyX_jPFVAOE2fvOKnr7HlGYalA-PEh2K-6fVbL30CU_9nC7B85JTHBAugyTWaN5ScsuZByCIVBVxayIukockhWK8Z65_ap2rZbqkUGWwpAiOOfMB7Ipszmp76_59e5owAPT9u1DaKmJHyMIu2oZtTkT3c_Mz_-iBPLw6Hd4tL_euxR8sQA7cgWeYi6sYO3mpXGXBS4_jWLUYlE7q1YV4v7lKgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1732fa7bfa.mp4?token=W0kZNMEP1Ss0OUvj2jStqd1auFkJxUK-acUXPHTinqIN-CnEsyV6h35iXR0pQesoG8fpbzxPwR0nZtNj6NlwcAEATVIB6uWv6pcpbSAsGZd3xD6ELqXHVDdMqmIbDyX_jPFVAOE2fvOKnr7HlGYalA-PEh2K-6fVbL30CU_9nC7B85JTHBAugyTWaN5ScsuZByCIVBVxayIukockhWK8Z65_ap2rZbqkUGWwpAiOOfMB7Ipszmp76_59e5owAPT9u1DaKmJHyMIu2oZtTkT3c_Mz_-iBPLw6Hd4tL_euxR8sQA7cgWeYi6sYO3mpXGXBS4_jWLUYlE7q1YV4v7lKgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لندن مطابق سالیان اخیر قرمزه
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105780" target="_blank">📅 11:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105779">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be20a40432.mp4?token=FKDoAtRkpV9irDhi02IcqUb7_rO4pf30RdYx6tcX5DGAg6EuBefPwmlKbwuYEDTs8xvE1rIoHpcXPW1Ag1z4blq9mONWu0crkL-iX6X2UI0agy1cNZOXtMTbyzkF47wgkraRpYGTcjx9tLSj50ynZl5J4S5lalXK_cPwC_rng9TcBTW_gynYhglAvGYCxK3QwRDALQUaumQUjQinEYGisAHLc2GwGFh4PB0l-ZCfWDc_SDZ7KfK5hTChxS2mx4Gf7H-y7woU0JYCxl0Q43c9Xz9eH8heXGQiNYz0iHnMZ4oNpyxYQdA4F-wbcOCzmSRHbg_6R0MDNtgLpAoivY4HYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be20a40432.mp4?token=FKDoAtRkpV9irDhi02IcqUb7_rO4pf30RdYx6tcX5DGAg6EuBefPwmlKbwuYEDTs8xvE1rIoHpcXPW1Ag1z4blq9mONWu0crkL-iX6X2UI0agy1cNZOXtMTbyzkF47wgkraRpYGTcjx9tLSj50ynZl5J4S5lalXK_cPwC_rng9TcBTW_gynYhglAvGYCxK3QwRDALQUaumQUjQinEYGisAHLc2GwGFh4PB0l-ZCfWDc_SDZ7KfK5hTChxS2mx4Gf7H-y7woU0JYCxl0Q43c9Xz9eH8heXGQiNYz0iHnMZ4oNpyxYQdA4F-wbcOCzmSRHbg_6R0MDNtgLpAoivY4HYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
⚡️
ویدیو بسیار‌کاربردی از بات‌های جذاب تلگرام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105779" target="_blank">📅 11:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105778">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/872be66f89.mp4?token=f-HNanAWzgHbOYDDA9jsczFgW4rqlaxY5ewtdICBzav79M2icJWLTszM8aLXHS_uf224JgLuSdLK1VDA6WliZbNhpE_84hc0LpvJqHg_aSWfq-HjHDa89k6vdlZuZkoOXs3Pbl2nQXF9yoK_ugjNgvKDyudy3rn-7Vk2knaCntAZyMVDx7kpi_MJpbuMZti4d1-vTC87TkpUpRLbzwdbZmaFdtFZVor4LseqrK454TRh0e127iYs0jCwdf_Qgylwhsfvxtk6yTubf6gXOuaACwZ0lss0H5QOWB4iasbpdVfAehpczaOewkaVs3y_q-nLNR-RQfps4Wkx6_dgTnuUooWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/872be66f89.mp4?token=f-HNanAWzgHbOYDDA9jsczFgW4rqlaxY5ewtdICBzav79M2icJWLTszM8aLXHS_uf224JgLuSdLK1VDA6WliZbNhpE_84hc0LpvJqHg_aSWfq-HjHDa89k6vdlZuZkoOXs3Pbl2nQXF9yoK_ugjNgvKDyudy3rn-7Vk2knaCntAZyMVDx7kpi_MJpbuMZti4d1-vTC87TkpUpRLbzwdbZmaFdtFZVor4LseqrK454TRh0e127iYs0jCwdf_Qgylwhsfvxtk6yTubf6gXOuaACwZ0lss0H5QOWB4iasbpdVfAehpczaOewkaVs3y_q-nLNR-RQfps4Wkx6_dgTnuUooWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
هایلایت‌درخشش دیشب لامین‌یامال برای بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105778" target="_blank">📅 11:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105777">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pR1bqfxt6uLOM8at_q6s6hXTN3bFFH7N8Qhcn5DGL-R4XY1vyngKrfWvyCRLWYJSKy8XK-BT_kHCiyRY7j4FzcebsN1d1uKyZvqc3GvDH5IJ1qJe9ZYpH-JMm8B6JQQdDsry2w2plBAvqprUKISgKwszXjrcn5-bO47k8NI5OeqxwnrkvGqp2mfiBhc9glg9yYE6havt8WArC2pPbVdAA3srd7x-cPYs_6HbUeHxj6D__FL1FGL9mtESEP-IbHW4ET1YC5Tnx77iwNB2OpMvubXTRpGqv8hxHBwi_3f3jWVndZO5jo3lqMhrE82pBCL3dZ4TSpPWV_jsVVXDBGy4pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💸
بالاترین میزان حقوق در بین سرمربیان جهان؛ هانسی‌فلیک بهترین سرمربی فعلی جهان در بین ۱۵ مربی اول لیست قرار نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105777" target="_blank">📅 10:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105776">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
⭕️
با اعلام سازمان‌لیگ ایران، فصل‌گذشته لیگ‌برتر بدون معرفی قهرمان به پایان رسیده و جامی به استقلال تعلق نمی‌گیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/105776" target="_blank">📅 10:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105775">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e60f25ffc.mp4?token=dcXPyMjI9fnTLsiBVPmAMkQkd9a0xPjuSCsOar6Dw1rvtJsaxpnDY6Ah9VkfLVpNLxrcuRgnzqwpR14XDoNS-m1jvp9R7PqJywGZ6JUw9TimEj0-ecC87BmxJisHNgPrEss05i8ZQ7S_MUMTHhX4G2iVsoiHBQELpFgwEyT353LTMB-m7NfFNyFGO5UtcEKLJlBF3v9_NGhN4hi3wax97OOsEKa_IJpurvCAxXf6bKkbMoOI4p9SrkGI88DmLkTidxMvBePtcuMuHi3bP4NcwS3QOiUnu1HlA_daFz62cuc6vjFjF0xc6QrIl5m7bndcwvTNPAOKmIfeS7i43wo_FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e60f25ffc.mp4?token=dcXPyMjI9fnTLsiBVPmAMkQkd9a0xPjuSCsOar6Dw1rvtJsaxpnDY6Ah9VkfLVpNLxrcuRgnzqwpR14XDoNS-m1jvp9R7PqJywGZ6JUw9TimEj0-ecC87BmxJisHNgPrEss05i8ZQ7S_MUMTHhX4G2iVsoiHBQELpFgwEyT353LTMB-m7NfFNyFGO5UtcEKLJlBF3v9_NGhN4hi3wax97OOsEKa_IJpurvCAxXf6bKkbMoOI4p9SrkGI88DmLkTidxMvBePtcuMuHi3bP4NcwS3QOiUnu1HlA_daFz62cuc6vjFjF0xc6QrIl5m7bndcwvTNPAOKmIfeS7i43wo_FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😢
🇮🇷
هوادار روشن‌دل تراکتور خطاب به شجاع خلیل‌زاده: به قرآن خیلی جدی میگم راموس ناخن پاته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105775" target="_blank">📅 10:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105774">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ab9d20b35.mp4?token=hdaWhfU_7j2ZYoQC-TBHb7B8JTEUEgNIleHP66jlpCcXPawZkPcd365smS7FrQxyGrmojBhumvRcxjC-u-JQ4TQRM-5CmBf7eIC6K6YXWY_IUhhC4MsL-4qL_N8a6WBKiZZKhVx_jpP6ui9ClqxC8YVJl2H8ihjH6Jk76eeEUz_sgniH3_cDR_aArOUZhWNK41kexmJbuTTmPkeO_rHYm5-E8vyxWwTgaNnsKYZR1VAj_uONA8DBKdAt7MAmsrU4laa2_PtPLEN7rxkXJdk3ReLvVOUYoPKc2LTXR03bV0NeGSzWGfTWuT_-DVAK7FW54QJ2FN8S_KlsIBzGofv6GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ab9d20b35.mp4?token=hdaWhfU_7j2ZYoQC-TBHb7B8JTEUEgNIleHP66jlpCcXPawZkPcd365smS7FrQxyGrmojBhumvRcxjC-u-JQ4TQRM-5CmBf7eIC6K6YXWY_IUhhC4MsL-4qL_N8a6WBKiZZKhVx_jpP6ui9ClqxC8YVJl2H8ihjH6Jk76eeEUz_sgniH3_cDR_aArOUZhWNK41kexmJbuTTmPkeO_rHYm5-E8vyxWwTgaNnsKYZR1VAj_uONA8DBKdAt7MAmsrU4laa2_PtPLEN7rxkXJdk3ReLvVOUYoPKc2LTXR03bV0NeGSzWGfTWuT_-DVAK7FW54QJ2FN8S_KlsIBzGofv6GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
کنایه تند رسول مجیدی به فحاشی خداداد عزیزی: والله اینطوریا هم نیست که همه جامعه فحاشی کنن
…
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105774" target="_blank">📅 09:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105773">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfbdf6e4f5.mp4?token=T24YdyaPPZjnUIQygC-4ypQD80rw_TpOxKYucz0rC1KP0hp4ceLUoJiboq03kFkwfM3xm3E5CEDuRiQBL280kqoOUtpiQP58kQIvWvm59r3etyXyLua3mIwLBErrdMYQlhjhdTzUhAfprLoxPr3BXdCUs_MB4UwKZYENlvkjxSSkFQ6X6c1-DyyROX3A1khHylYzwe3jRXbJ_fUw9iaB-HQgy1wPBSa_zz5sKnzdDkx1Kb-9nA4kRpMRtj9TSDu4Ow6mzxxjlYp7GISoZLW9egkhYwPfJi1LbRDrdSXoSXLbLnDNedHbrH5E4SwSjyMluGopOj1q7x3EzA-lHsJegw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfbdf6e4f5.mp4?token=T24YdyaPPZjnUIQygC-4ypQD80rw_TpOxKYucz0rC1KP0hp4ceLUoJiboq03kFkwfM3xm3E5CEDuRiQBL280kqoOUtpiQP58kQIvWvm59r3etyXyLua3mIwLBErrdMYQlhjhdTzUhAfprLoxPr3BXdCUs_MB4UwKZYENlvkjxSSkFQ6X6c1-DyyROX3A1khHylYzwe3jRXbJ_fUw9iaB-HQgy1wPBSa_zz5sKnzdDkx1Kb-9nA4kRpMRtj9TSDu4Ow6mzxxjlYp7GISoZLW9egkhYwPfJi1LbRDrdSXoSXLbLnDNedHbrH5E4SwSjyMluGopOj1q7x3EzA-lHsJegw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکت تماشایی دیشب رودری در بازی بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/105773" target="_blank">📅 09:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105772">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Em22KgpL1gscoeX7MQYcKWOnIemwsWPuRVrElzq1PASkIlhKkx48U0cRGhzri1kptBR9eTc-74vZEiZvWYOmheD0O0AA-eapiUv58h_feWi8u7J5DnKd2P2vKlzLVbW6I9dIApJIRzig6R4UxTXrN17inZHYslcKkQC-J_El868P6tf_w4X0lKAPlGIdZh15PtHqZaT-vnYNpMTnYag6lh7zTUwU50gW1kM-QUwHaR1fN9M-etgfG5FoCy4tBy-wumyK8CTii5w81TjhUezcm9oQCHToOvRr8wy3DPLg5oa5Fdj1A4LrXQ1pBLswhwIEwuqZ83aOfyLg1Z8YbGB-ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105772" target="_blank">📅 09:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105771">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf5650c1b3.mp4?token=u9vAH33kXkUCmm1FiKXNu-nYwlN7Io7jp9tOhxExoRb3X0qtCnANgigzKb1f6IYh59nRy7RdzRN5OQSY0YfOiWU05cT0c5sMTeoIzhF1jb0sXJBIsd8aWx8aesY0lkU_U9ciiyPDAURLsrtAhOqp_qsixyUlY_ejfk5bO_Dbt3xcPDVNGtUprgf_2IxRQ-u0jfPL1zLPiN4-Tnh2_mt7n-mf7YDaBCHLoNuczTUPT69Z_Xlqzshwgk5A-tAyrt3c1-mXzTJto5tBqXeRJ8k4EQuqg6CMM3bX2_s_vr9GoApHEGx1gq-E63lXM07uIHwNjxTWNx5FRyMNS4noDkSQWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf5650c1b3.mp4?token=u9vAH33kXkUCmm1FiKXNu-nYwlN7Io7jp9tOhxExoRb3X0qtCnANgigzKb1f6IYh59nRy7RdzRN5OQSY0YfOiWU05cT0c5sMTeoIzhF1jb0sXJBIsd8aWx8aesY0lkU_U9ciiyPDAURLsrtAhOqp_qsixyUlY_ejfk5bO_Dbt3xcPDVNGtUprgf_2IxRQ-u0jfPL1zLPiN4-Tnh2_mt7n-mf7YDaBCHLoNuczTUPT69Z_Xlqzshwgk5A-tAyrt3c1-mXzTJto5tBqXeRJ8k4EQuqg6CMM3bX2_s_vr9GoApHEGx1gq-E63lXM07uIHwNjxTWNx5FRyMNS4noDkSQWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هواداران آرسنال دیشب حسابی از خجالت مورگان راجرز بابت عقد قرارداد با چلسی بجای آرسنال دراومدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/105771" target="_blank">📅 09:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105770">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99e6028a7c.mp4?token=jkAwXxGME6zyeckfuE7Awq6xlACOJ-YYAEyijX2zfIA1VJa5RUnSYTSSRoWE1Dd8U9QiXuSMcWHOTi04ad9T9iF7yeYgPGx7rQlhRtfDTOPD5zLPZ9L8WB0eKP0we6cDJ2Kn9fkaBfezMy_ZRin8e1CuFALX5ZL4XyqFMDPv7LXfQhaoO9WKaUkjTv8ZbTWn1f8Ts4_5rcWLzJztG5CUIyXNR2LnrFrSuKtP5nnT7TvhD3lhqSo3f_eJVpJtjVd52WsPZyhCZ4VZ9FjH3W7UWU9a3Y-tv3KkXDtbCpRdoeb_HXXCspV3WmQ-doS_62yhSgEosiydzW2ih_AT74KJrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99e6028a7c.mp4?token=jkAwXxGME6zyeckfuE7Awq6xlACOJ-YYAEyijX2zfIA1VJa5RUnSYTSSRoWE1Dd8U9QiXuSMcWHOTi04ad9T9iF7yeYgPGx7rQlhRtfDTOPD5zLPZ9L8WB0eKP0we6cDJ2Kn9fkaBfezMy_ZRin8e1CuFALX5ZL4XyqFMDPv7LXfQhaoO9WKaUkjTv8ZbTWn1f8Ts4_5rcWLzJztG5CUIyXNR2LnrFrSuKtP5nnT7TvhD3lhqSo3f_eJVpJtjVd52WsPZyhCZ4VZ9FjH3W7UWU9a3Y-tv3KkXDtbCpRdoeb_HXXCspV3WmQ-doS_62yhSgEosiydzW2ih_AT74KJrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حمله شدید وحید قلیچ به خداداد عزیزی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/105770" target="_blank">📅 08:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105767">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105767" target="_blank">📅 00:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105766">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e26f7c6c2.mp4?token=E3O_Jf9cq3DwyipljfSsCbiDFxQzEaB4R88dfTDzbV6KAWWZLWdz-XD-d7WqXkqS3kUuPZduk-nU8TR9s5l3iLXdGXYnlolEEhRM9IL3CUdK2nD_yN1KmqG6-IPHWSdaEH9Dqb5f6qzyNMOGuebjmkGiY7V9WdIjRIi4bidtaEbuNxHHm68ELfPIFZSGcwVdriLwxLUrbCBpaMy-RujGxJ0Jytizj45wcrnSihzAOWdxGwrG1Gk1bS42vAJ1hZvCfYS3jWF5j77nlQVnEgwko1XJk2bBPddW4HrtKAXywJyUXL4Zr4rZAt_WNy7nk5lTza7MQ_zCdfC_uRohkyczlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e26f7c6c2.mp4?token=E3O_Jf9cq3DwyipljfSsCbiDFxQzEaB4R88dfTDzbV6KAWWZLWdz-XD-d7WqXkqS3kUuPZduk-nU8TR9s5l3iLXdGXYnlolEEhRM9IL3CUdK2nD_yN1KmqG6-IPHWSdaEH9Dqb5f6qzyNMOGuebjmkGiY7V9WdIjRIi4bidtaEbuNxHHm68ELfPIFZSGcwVdriLwxLUrbCBpaMy-RujGxJ0Jytizj45wcrnSihzAOWdxGwrG1Gk1bS42vAJ1hZvCfYS3jWF5j77nlQVnEgwko1XJk2bBPddW4HrtKAXywJyUXL4Zr4rZAt_WNy7nk5lTza7MQ_zCdfC_uRohkyczlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
🇮🇷
🇮🇷
سجده جیمی‌جامپ امشب نقش‌جهان با پرچم استقلال مقابل سیدحسین‌حسینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/105766" target="_blank">📅 00:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105765">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqQbr8BvUsIEAfOWijZM-qyiAGP4B7QoPH6ZZhjhrFtQlzu0AJMrIGXHrX_rfL7gLZ0Zzu5_uEupdHijiRpt-_dGBGsl2-9IIrvYOUoQkhV7RvjW-EWfrXsx5hXAIlEyFjTWvTfuDWh1jcQs5mz406Cb5fq_Wbp5tfpgD3_vXmoL3ZhbkUg5XkHaBOtmI8NcRMlwPAhq_IHjrCJXRYrACyv1_b8gobj3tFcDaYlaq-CydVQ4Y24VzkHxZZ-HcU2-k7QJXjbv6f1OvLQuvxCGWyuB6-xXQGVpQtFunRVpRbvU21X9RVAGBiE8kBGN6Mx9S3hckVVvL8ek84vks_L6EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇮🇹
پایان‌بازی|
🇮🇹
میلان
😃
-
😃
یوونتوس
🇮🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/105765" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105762">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
پیروز قربانی: من به توافقات قبلی کاری ندارم، خلیفه و گودرزی رو نیم فصل به استقلال نمی‌دم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/105762" target="_blank">📅 23:45 · 15 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

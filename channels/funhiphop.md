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
<img src="https://cdn4.telesco.pe/file/hic4xkmOPKwxa3V5-oIRDLHCh045aKoLuPkSDls6Mtq65WRF4T0gIBiq9KwYxczY4yZGYsVAk0LygSSc_AXFn5e-2Lj62Yhjpwa9ZZNZZqfCDZXJNIgJ_3KFjYqFky46ldtBq2w_jmwhHkQAw3iKAOojpzZXAuJ4EspVZAwBCRs2X34Q1PoW0dGKG6yPPzlzjwehCS22TCqYQ6ePZUNYIYYCY4bUi97MmU5uMoIgtb8Y6Vdd9_kt280nwG4wJboahP4dU2Sl4_Hwf4L2-KiPzJxQl1ERUV2kviOx60rKqr_nhSL27BFfwutGEjZtejNtSM_uTTcaDDGiR52kmOxscQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 254K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 12:14:42</div>
<hr>

<div class="tg-post" id="msg-84315">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e0832652.mp4?token=BKiPWpTw-JZ3KdfBd2vohH3QJlPlkNOlPYh4_9hCATbEqI096tdibDZRJN0a7BL5ns9Wbo7dJpdTmA1R9YN4lk6_F_korE1z3TwEVIPKInScU-TqeUc2Ek1rED3T0kKbRr-XJSJ4PsdAqqkw9N63IotPooouRvqCklRWUYFGTLt1DVqvJ6sTgV3Lnh_vnplGz2gs42EfFQrLU8r1ei6SFm45w5EQaEu3CPL3WhaptaLx0mUkzCwVPznw4q0FCgG_fZQem_bLThzu_fle8LknL8-smR8dJjK841uA2UW8QzeFyU48_5gdtOnanSsW1q3bj49kb9NsJgSYQ5bowNjxCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e0832652.mp4?token=BKiPWpTw-JZ3KdfBd2vohH3QJlPlkNOlPYh4_9hCATbEqI096tdibDZRJN0a7BL5ns9Wbo7dJpdTmA1R9YN4lk6_F_korE1z3TwEVIPKInScU-TqeUc2Ek1rED3T0kKbRr-XJSJ4PsdAqqkw9N63IotPooouRvqCklRWUYFGTLt1DVqvJ6sTgV3Lnh_vnplGz2gs42EfFQrLU8r1ei6SFm45w5EQaEu3CPL3WhaptaLx0mUkzCwVPznw4q0FCgG_fZQem_bLThzu_fle8LknL8-smR8dJjK841uA2UW8QzeFyU48_5gdtOnanSsW1q3bj49kb9NsJgSYQ5bowNjxCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پورعلی : مجتبی خامنه ای شبا به صورت ناشناس تو تجمعات شرکت میکنه. دوشب قبل نیم ساعت اینجا بود.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/funhiphop/84315" target="_blank">📅 11:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84314">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d8bb7d42b5.mp4?token=PjutR6ykm2cSN59qAftrIVbFeVslC8ul8UgwyIg2AGDhTWWeNUc4jTficZy29som74W6dOD8KnH2-yGjm7yEfHus75Mef6IIz6oxNInLPOzAjuZ8hWRKXgL2H5ZUHC03Jp4tFitnonfThqfX6lS90IsZdxFax2XlvsS0mOVjqciMkBolX-tHq8AFKugyWPtgMpQD6o2mK6SxQqtPOQGa5Rf2yQaoqasgU87EthBsUFfb4brNQs4gcjvzvUoNyWa9UI_ws7Huc02VhCFyeVYWpno8vXWOlc9zRvp2CyWGqyB7ECBWgHtMU84l43kOX3s5Bzj13L4sKikUfy5oax_NNg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d8bb7d42b5.mp4?token=PjutR6ykm2cSN59qAftrIVbFeVslC8ul8UgwyIg2AGDhTWWeNUc4jTficZy29som74W6dOD8KnH2-yGjm7yEfHus75Mef6IIz6oxNInLPOzAjuZ8hWRKXgL2H5ZUHC03Jp4tFitnonfThqfX6lS90IsZdxFax2XlvsS0mOVjqciMkBolX-tHq8AFKugyWPtgMpQD6o2mK6SxQqtPOQGa5Rf2yQaoqasgU87EthBsUFfb4brNQs4gcjvzvUoNyWa9UI_ws7Huc02VhCFyeVYWpno8vXWOlc9zRvp2CyWGqyB7ECBWgHtMU84l43kOX3s5Bzj13L4sKikUfy5oax_NNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
یه توریست و بلاگر خارجی اومده بود ایران و با دوچرخه میخواست بره یه شهر دیگه.
دو تا خانم دیدن شبه و خطرناک و تاریکه، برای همین تا مقصد، دو ساعت تمام اسکورتش کردن!
حالا این بلاگر پستشو گذاشته اینستا و تمام دنیا به مردم ایران افتخار میکنن!
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/funhiphop/84314" target="_blank">📅 11:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84313">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⚽️
مسابقات ورزشی را با بری بت پیشبینی کنید
⚽️</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/funhiphop/84313" target="_blank">📅 11:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84312">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEPn08ArRLugTxBp_yeVerMdsM-nTYpOtmgZX1hNW1N_Mgp8a4haLqPRcEPAa_23mHexOFTl0aQodPFncaMfDGSmoSaw7uuEau0UhepFc4S7ZC61OkiwrBQZtQqEgb8_owB6s5H9VRp7TB5r7TGnbwjz1Y-rjv_3c0Gvp3N0CVZy0yYw0j9X2syNj4O2L6whLnaHU81pJ3HKRLfti16hMHS9gMKWTXTUjN6HxWWNBAnNEPMZd-lIdxh0NLnVjQCN5NgpM7AKUW-9PW7CDXgX8PRs7_9TXIRbQyhFHaGEl9PDm-Kf2VvdK8BX9Wayc1zAROk-k5OcJYTTB63-3vWw0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
فرانسه - ایتالیا
⏰
ساعت ۲۲:۱۵
🌎
📲
لهستان - رومانی
😀
ساعت ۲۲:۱۵
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R10
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://ewreioxko.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/funhiphop/84312" target="_blank">📅 11:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84311">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea0a9e79fa.mp4?token=dulCzvptCOs6mknwVF7AT8gn6grKFrVPMdQLvmmCSNL3NDjn44IYbgwETeIreymGyhg7MYSe5RuaUJU1X5DG5I94-jIYWurWuicNw2rMIAq8bZATPYv41P_Xj8D-U6WWkVXhOmE_T1IO7-ZVLfGxLfDw1iHTmBSZvNlM97KbP-ec9PB1AEtRVncihWCknNtQgjHzV36T3sp1oP5ZS29OD477t2HfR4qAgzUKj3RKdgnwSKPK-Jl71r2kGXsMHs1mdbagOVDulp6G8HWWInbPML2f4YrEO99a0PVNkZwgitTHX26kSPwsBQMvz2Xw0C-GUThM2ik70THoEvYVVF2Nfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea0a9e79fa.mp4?token=dulCzvptCOs6mknwVF7AT8gn6grKFrVPMdQLvmmCSNL3NDjn44IYbgwETeIreymGyhg7MYSe5RuaUJU1X5DG5I94-jIYWurWuicNw2rMIAq8bZATPYv41P_Xj8D-U6WWkVXhOmE_T1IO7-ZVLfGxLfDw1iHTmBSZvNlM97KbP-ec9PB1AEtRVncihWCknNtQgjHzV36T3sp1oP5ZS29OD477t2HfR4qAgzUKj3RKdgnwSKPK-Jl71r2kGXsMHs1mdbagOVDulp6G8HWWInbPML2f4YrEO99a0PVNkZwgitTHX26kSPwsBQMvz2Xw0C-GUThM2ik70THoEvYVVF2Nfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رپرای جدید تا حالا واسه زلزله های مخرب تاریخ مملکت خوندن؟ نه.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/funhiphop/84311" target="_blank">📅 09:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84310">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e286f8be43.mp4?token=trhzI-jFyBPAfrQb6HEtJnSsZW3wuK8dPN84gizuvweo8EIw5t0VItNgGn9mbnnTRUKulIUhssba_VtQV6YbGn2_qaNGPgGidCdYa4mIHc5mtJzbEWLDyhG7dTXaYIPerJNKQT63wAmtYX6t71searu-HgigGeR0vxKwBRIor8Hoq2xg_LmnMdNH0BQ9RZdKgkOon8Eq4bgYXJUO5LisVrY4oJ9RIBO4I91zKWFOjakKg3vZSjdUT5u9vMPSTYGGyR7Oi_Anwd4eYICltTjpMAdqX0NCsPcNRGgd1vbaYhbF0irBXcVjk8LLoj9LnebjoSEv3Ajiu97Ca27Ds8TZIDYZe1Vd2u_DQRjWXshbz-3VMUjhwlWS7_1320y0To8W7bGxx94Q6litUuTLlo2T0gckgk3f-JvgVTbQlBBGOT4APhTcyrbnvqXjuxrSSSt8NGnr71o0pTqHuRkJvXoUV7cAOaUW25fjPSU3IK53IYEUInmy_RpZOBWwF_2GjhFpWd3G9ndpVmIsDSJfUl06y-OPFyTmKx8iaNP4k4AhLjLQ5UoC1vp5U78v2duGMCsWE1ld03gakbxDJU9Rt6WzAx5g0v_eV5xXl6ewWSxIOTgA-aQegMAn3dFSbGfWDLhIQ9Kk7GHVJ564n5DJRQkzAxj2opCnt_Io-nG6038K3BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e286f8be43.mp4?token=trhzI-jFyBPAfrQb6HEtJnSsZW3wuK8dPN84gizuvweo8EIw5t0VItNgGn9mbnnTRUKulIUhssba_VtQV6YbGn2_qaNGPgGidCdYa4mIHc5mtJzbEWLDyhG7dTXaYIPerJNKQT63wAmtYX6t71searu-HgigGeR0vxKwBRIor8Hoq2xg_LmnMdNH0BQ9RZdKgkOon8Eq4bgYXJUO5LisVrY4oJ9RIBO4I91zKWFOjakKg3vZSjdUT5u9vMPSTYGGyR7Oi_Anwd4eYICltTjpMAdqX0NCsPcNRGgd1vbaYhbF0irBXcVjk8LLoj9LnebjoSEv3Ajiu97Ca27Ds8TZIDYZe1Vd2u_DQRjWXshbz-3VMUjhwlWS7_1320y0To8W7bGxx94Q6litUuTLlo2T0gckgk3f-JvgVTbQlBBGOT4APhTcyrbnvqXjuxrSSSt8NGnr71o0pTqHuRkJvXoUV7cAOaUW25fjPSU3IK53IYEUInmy_RpZOBWwF_2GjhFpWd3G9ndpVmIsDSJfUl06y-OPFyTmKx8iaNP4k4AhLjLQ5UoC1vp5U78v2duGMCsWE1ld03gakbxDJU9Rt6WzAx5g0v_eV5xXl6ewWSxIOTgA-aQegMAn3dFSbGfWDLhIQ9Kk7GHVJ564n5DJRQkzAxj2opCnt_Io-nG6038K3BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا لحظه آخر منتظر بودم بزنن زیر خنده بگن جدی این کصشرا رو میپوشید؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/funhiphop/84310" target="_blank">📅 09:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84309">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/337199248a.mp4?token=EScSnBlg_RtqbDEnHMbD236PqC_Xmk6RThk6gkb4r-QMgsKDUj4oW21MWFLk-j6DOCmGqFwuWdueVW9glZxk_EIpDvTtMlsIkgb3lstI-FEDOqJX3lj9IW3dG-nIM-2Rjfwxk0Ia2l7-Cngc2AUSUaubPrZ9LZCpC9K5G_EdJ28znIlmhSZ4_z4fghBnaA__yDu78JyYgVmbzfJ2m3O6M3Vhv9YW_1Bi78U5oEGei4d2obzIU2g5PyUiNy_VMq2tEhDVc_lcJYwR8uzKsMhPJpB0TWvDnn2yP53mSkyo6i3YuVhCD7uTRnjmkQrQoncf2_tNTPGJ2m-90W_hl3YPMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/337199248a.mp4?token=EScSnBlg_RtqbDEnHMbD236PqC_Xmk6RThk6gkb4r-QMgsKDUj4oW21MWFLk-j6DOCmGqFwuWdueVW9glZxk_EIpDvTtMlsIkgb3lstI-FEDOqJX3lj9IW3dG-nIM-2Rjfwxk0Ia2l7-Cngc2AUSUaubPrZ9LZCpC9K5G_EdJ28znIlmhSZ4_z4fghBnaA__yDu78JyYgVmbzfJ2m3O6M3Vhv9YW_1Bi78U5oEGei4d2obzIU2g5PyUiNy_VMq2tEhDVc_lcJYwR8uzKsMhPJpB0TWvDnn2yP53mSkyo6i3YuVhCD7uTRnjmkQrQoncf2_tNTPGJ2m-90W_hl3YPMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کمدی شاخر : (شاهکار+فاخر)
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/funhiphop/84309" target="_blank">📅 08:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84308">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خسته نشدی این همه پول VPN دادی و آخرشم فقط یه روز درست کار کرد؟
😕
لومس نت اومده تا نهایت سرعت و پایداری واقعی رو بهت بده. نه وعده الکی، نه حرف بی‌خود!
👌
🎁
تست رایگان
💵
تضمین بازگشت وجه
🌐
اتصال پایدار و پر سرعت
🤖
همین حالا ربات رو استارت کن و تست رایگان…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/84308" target="_blank">📅 02:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84307">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ka1aLnDxzPabQ2aW10HZ51YXqO6n702or6M-26xxQpqeF8eF3bnmdWAM2ROFQrbf9l5-CelNagLvDTQDgScr79_tICNVMoxMPz-aoXCFZoGbAUKeSJ2-kOTLwmnPiIYbDJnjcoVSOKEz4z8KmiLWBJqmjAT7n9tL9K1WKr6mGB55Oyc4yAzDgzGs1TNuettzPz7YUWcFnOzfbkB34yrj1lBNxUZEh_3MHujohYoGu36FmvzrUA3CrIf98j2CAr27Czq4XZo1qKkwU8E4FvZr96fE-cmsXhxcHJLgOVTCx0nZEttbqemimitfrYU7bQgXfPx5TYVc-iJKzrY5AxAg5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته نشدی این همه پول VPN دادی و آخرشم فقط یه روز درست کار کرد؟
😕
لومس نت اومده تا نهایت سرعت و پایداری واقعی رو بهت بده. نه وعده الکی، نه حرف بی‌خود!
👌
🎁
تست رایگان
💵
تضمین بازگشت وجه
🌐
اتصال پایدار و پر سرعت
🤖
همین حالا ربات رو استارت کن و تست رایگان بگیر:
👉
@LomesNetBot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/84307" target="_blank">📅 01:14 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84306">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a90438c76b.mp4?token=mAyK_Ra6D3_BYLN8tioCKjgd_CiDrEmpgz7NTE9eVBvn-vVStQVDabHsB55muEEOo8UVyTWHH484wDOzlYPlWrPwlePGE-q0zCdZyTwoS-HXx0GcI9d45h9NWLgdvayfmHVsyAg-QR5_hcVWDX0mUry5dhsmqGEFUCZck67Kjo7iS6oAt0nSqpynEpfdvFwatSCT-Jcl2I8x_Svd0b9ngUX0Np_UkXmrYVZQUlZO6kYzdTyNO9DsjK8RjqAHG5bvCRlGukKB4G527HUTInubQkVBCpR1QjN2rBGEomwmR7ZoVhtDjywdeVHodUqQB3yYipJJRjDD2FpZxamSrxUfVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a90438c76b.mp4?token=mAyK_Ra6D3_BYLN8tioCKjgd_CiDrEmpgz7NTE9eVBvn-vVStQVDabHsB55muEEOo8UVyTWHH484wDOzlYPlWrPwlePGE-q0zCdZyTwoS-HXx0GcI9d45h9NWLgdvayfmHVsyAg-QR5_hcVWDX0mUry5dhsmqGEFUCZck67Kjo7iS6oAt0nSqpynEpfdvFwatSCT-Jcl2I8x_Svd0b9ngUX0Np_UkXmrYVZQUlZO6kYzdTyNO9DsjK8RjqAHG5bvCRlGukKB4G527HUTInubQkVBCpR1QjN2rBGEomwmR7ZoVhtDjywdeVHodUqQB3yYipJJRjDD2FpZxamSrxUfVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو حاجی  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/84306" target="_blank">📅 00:28 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84305">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed8253be66.mp4?token=EWmkQgu_QNF2OB_I-tHTHLPB7TlplF7-EvYTWaiXf57zOmtYYZ9epolLvwmkG-myoDheC-88PWfSmoVkUwKFU3Ji4Bal7N7QmNYTQtfKe2VCezpERKeMvNPy5kglSUsFUcaIGqVJ302aiHDkoRPV8Vqghs-eBAIhGZw8_hPD9lTD6c4-KiUAaemHmONq33Wbwvr9ODYcRra2yn8Bg8bQiqzVMxHd03_SUU0cyY3WRZjlciBLWUmpU24Hh7KaiEUjMnNl2fuoDJFf_VQtsp_wYbcNl3IJGYntfdXqCO1E4cW2WsM2G3kFgyVtP5IZv-2CWeXipuqPu9I8DxwB-FlzwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed8253be66.mp4?token=EWmkQgu_QNF2OB_I-tHTHLPB7TlplF7-EvYTWaiXf57zOmtYYZ9epolLvwmkG-myoDheC-88PWfSmoVkUwKFU3Ji4Bal7N7QmNYTQtfKe2VCezpERKeMvNPy5kglSUsFUcaIGqVJ302aiHDkoRPV8Vqghs-eBAIhGZw8_hPD9lTD6c4-KiUAaemHmONq33Wbwvr9ODYcRra2yn8Bg8bQiqzVMxHd03_SUU0cyY3WRZjlciBLWUmpU24Hh7KaiEUjMnNl2fuoDJFf_VQtsp_wYbcNl3IJGYntfdXqCO1E4cW2WsM2G3kFgyVtP5IZv-2CWeXipuqPu9I8DxwB-FlzwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو حاجی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/84305" target="_blank">📅 00:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84304">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aunxO-5JKYDim1R64chmxeIAf_qy75dUim19WZT8vhdxgiBbvPvWubzgnadh82v_xVfcR3F3WnqV1rtZGiKpI6Z7F3zrZEC9qtFuhSrJf7QaWJXtAsC64sGTC1Ar3H7C-FERWHCkbrTlDU5TiCar62jGJ9tMAjA2KHLlPacXSfkuRX2nSMIinivwMIpHUFX53W31OhVlBl-0nWBhNrNiLznGsWsh2d_feW72usjXn0LEKEnGB6BYuAxFLM5uHdAxdTMoK6sojAg_RHzLfsYTKUk4v86lDaRFxfYEjPMbmJqhocfewmEbx0zYrvAUuaxqVu5sWzPBOpKoq4V9mqS8Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصکشا دیدید بدون رونالدو هیچی نیستید؟ رونالدو بود دفاع میکرد دوتا نخورید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/84304" target="_blank">📅 00:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84302">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دقایقی پیش وزارت خزانه‌داری آمریکا شرکت های ایران‌خودرو، ایران‌خودرو دیزل، سایپا، پارس‌خودرو، زامیاد، هپکو، راه‌آهن ملی ایران و شرکت قطارهای مسافری رجا را در فهرست تحریم های سراسری خود قرار داد و اعلام کرد بیش از 30 درصد درآمد صادراتی ایران را هدف قرار داده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84302" target="_blank">📅 22:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84298">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43faf33322.mp4?token=ibhJjQeE9evCxflg-WIKdvO3AC2RqaU80Ixy5_aG47cQRE7A7FoWFE7L9bXA_FRvchIP4fBNtK1SltFxD_2nLeegsSA7XXBIEr43ShmZst0SkozbHAUy5dTufjJMr7INMbzOJEWuaHnyfDCw6oUqkDxrXDxsc-fsvQRZMq78vZKlLIry2QEgjqY1Ar1IsdwTsxBJGIxNfbgsarpmWZFskE-WWDigd7WYUYrwW_HOAuHilqDspcVW7V4VZjpDy1VLsLAinybXayc7o1zyK4XbKtRNb9cxjulIyVbyCIFbh1tgSe3XTJ5BkHadFpUUtGVhx8vgp90O_i6GIy15LkwNsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43faf33322.mp4?token=ibhJjQeE9evCxflg-WIKdvO3AC2RqaU80Ixy5_aG47cQRE7A7FoWFE7L9bXA_FRvchIP4fBNtK1SltFxD_2nLeegsSA7XXBIEr43ShmZst0SkozbHAUy5dTufjJMr7INMbzOJEWuaHnyfDCw6oUqkDxrXDxsc-fsvQRZMq78vZKlLIry2QEgjqY1Ar1IsdwTsxBJGIxNfbgsarpmWZFskE-WWDigd7WYUYrwW_HOAuHilqDspcVW7V4VZjpDy1VLsLAinybXayc7o1zyK4XbKtRNb9cxjulIyVbyCIFbh1tgSe3XTJ5BkHadFpUUtGVhx8vgp90O_i6GIy15LkwNsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید میلی گلد بعد از حواشی و شکایت های متعدد مردم با کپشن: این طلا، بخشی از طلای میلی است که خارج شده و حالا با آن، تسویه کاربران در حال انجام است.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/84298" target="_blank">📅 21:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84297">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">لیائو کصکشو تا ۱۰۰ سال پیش ۷ دلار میخریدن الان شاخ شده شماره ۷ رونالدو رو میپوشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/84297" target="_blank">📅 21:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84295">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sw7BbeL60sW7sDyyN6Occc1ylDWZ7ZuK4Sv4OyX7UJKlqrcrE5H6OkfmAzZInmeKW1AmLuFabAiHhQysJ3G-6bT4SyLv7iAnm6k4tt9FEXwQbHJAjbr-r4R_hGTN08Y-VSSg0416DZUCPI8JhJX2ATd7bgJO0WUxDoRh64DC4FfaIkbG3ZkthjlrsE5teMsl4dqzcYYmxUfZ4S-mzIpZAFPFHTiME-QxcvhFP3MGBz4on_B5cmpvsYns2vJoGcrecBRPBQnu11Z0yQAbEQFkVwUveYKsmH1-srCXu4juVCLQmYwlYLMpK6NqV0mg15bOy1zk3CAgDKlk_Okt09zl0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا جای این کصشرا یه شیر چای تریاک نمیزنن این شرکتا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/84295" target="_blank">📅 21:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84294">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پوتین رسما ناتو رو به حمله اتمی تهدید کرد، ورژن ۲۰۲۷ کره زمین قراره هیجان انگیز تر باشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/84294" target="_blank">📅 21:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84293">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پوتین: کسمادر هر کی که به ما حمله کنه نقض هم نداریم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/84293" target="_blank">📅 20:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84292">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مهدی چند ماه اینده این ناوی که زدن چند میلیارد دلاره
یک مقام آمریکایی به الجزیره: تا پایان نوامبر آینده، ۳ ناو هواپیمابر و دو گروه آبی‌خاکی در اطراف ایران مستقر میشن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84292" target="_blank">📅 20:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84291">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝖕𝖆𝖐𝖍𝖆𝖜</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aochIbWIZPaPPkKaxATl4behlVnoAoD9IKY3yVYhKnokI6meUGzPH2ekDvnJZ1NdbJe7XuFE64bykLM1xEeAZKL64RgmHiKZxMSghFonJtdUZGQ7H4_spfSd0adM9hEGdc1tYjNNescQVNQgTv6qVMTUUBBpZODXvNAPngnXgefZpLdx6b_EvBFdPvg8UKEorvF9UpyVznGJn10R7nljg1Km4OU7qXxdxn60SLp3lfC0Qjd9TsMdbvQwAnto3mK_oku_WYOjCgn3zLzCFGKm6P35F3ZDSduw0UwuhUN3OpNxPr_RAtjytzqwUObHH_i7QGd5QkVPQ47aU1CdJ4MsZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیه</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/84291" target="_blank">📅 19:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84290">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPnp0C9WHLTa0i7NpEnmxLurMKQKKtedCaZao-7YwLpIEcDpYsmcqkLXRi2LKBQyM1BqjEuB1izmvPMowOeWRmgJe5zJtA2vIXAODI8dgoYEpKBTCAW0ZxkaNiIayT0w4rAYkIm-nf8z751V-qpIZd8P-xDIliRtYUKHB793T7-V-_lXcXTVclhh6CdaJEEEUvclFmgT1veGE99CIUQLgCcvhw-iJeDXe1DYPd1fo0gaJgqipIWm1KYoiySlmR3m6v7mWYKCCXG7y9ARqEbMXKtIYxypUXFLmNkR-kr10-ZXxpv-w-l2Q4ybZKR5IfMQ5y0xm-2RjoDULz0_YcMv9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به این فکر کردید امیرمحمد هرچی دلش بخواد میتونه بخوره بدون این که نگران چاق شدنش باشه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/84290" target="_blank">📅 19:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84287">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eiDyvp4kWlo2ty8oGYlyoZ-WrKaZGfuJSjZfE-7B5nzCM9LxPcx3vYV6cHS-jz7h3Bk55DnxhWXgl3KHmuHLg_3q8I47CQFF5NkS3ASHfSptS2X_RKvGCpnMrbnhlgSM5VQgO-vVVGvETHCfsceFmiOsOd_DaDw1Sd1fYnoklSlrJYR1nB-jwPmYsE-N21_5dj4vwwy1avYz9y1pDLHI0M-jn7897mPSnbtiDY0W1ptm8sfDPMeAPcaDzOwP9ll2lrmf_Ng6WQBUC4eQFftTEHxjtY5q7XT6BgizfPzxlth81nAS-uCZ9QmlGw5UDXKxRN6KzUr9uvjXrLxD-mcf0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bY-ZvNYloWksL0EWA7jwCQGx6R9iwoNXueQepi_CuuIe75Tb7Jz7lnyd3eFELPJJCCAeWw-6P2WWQFHSoYQ2BCcNg0zpjx0O9jm6AtDSStscClJYLKBKvW4FYmnHENYOKx_Aj11Bbni32shgIpYfhokalDTsZ3dWtKIuU8neqskFllQcs3Fkbxq-HJmFjMlZFARcVTAf2S-dqPA1pw3RM6Ab2fZoKcWofkWerD8RpHHZnbVivqLheoLEA7USagGWrcAoolkuot8GJjugnZKNaIk4am65DCgxy_11-MnlOSsj4-VjSNCMnaY5OAGkz5y_rSvDwcWhBXRrrn2gg9jg2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NE91RClQDYOOSkQjABOeHnBkSIP8fyFSYDGAyg-R2eajdQCaiO_3Sq75u55foECF1bqtQrBh0JNgd3R_6UiNnslzCWfSZTviFC5wdr1jIbrMcVObVHfHvXrJoeGgZ9dF8tmh23_myM2EZfYxSWCfTsogx7PRtudrZ7Qmv0NiyIn5gPHNCr42i-g-qsJzbcnKk9A2ayk89uppjDZYzOK49NLQMv2bRsbk_nBvDEuuqmg__pYI9O16__uh1SuW7kowmH3pFNoYCzgibaklaUR-EnhGt94LreekFLPPiz2aqxdVuvwp5u0i_443jndk0cLNO1X99eXmVQV06gkM4bVd7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ریری یه جزیره رفته، ۹۲۹۱۹۹۱ تا ازش پست گذاشته اینستاگرامش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/84287" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84286">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ritzobet.apk</div>
  <div class="tg-doc-extra">45.3 MB</div>
</div>
<a href="https://t.me/funhiphop/84286" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/84286" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84285">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E66dxv0lCwN0JHEO3tAXDvvHqwjeINniQwZkRkgW7LS7xGI9P4OWMIJ4lGzzhQZF5jLvAupBplXsEiclowYSthEIgiwTmLsUtvwpG5iuEc8bcuzIz5wea_KOhINsIRW7J1Z5OCnS7ge6qc8OQ1gIFHMIqNqvSxc7V_LNrRn1BoJ3TFRafSKSDgqHJZ-Q0VudrybByqCDmWsHIKBdVH-ImzSWvZpMs4LnJ7DjxsHeE2VN-rod3TDCsQkbUD0DkBAcMPTxfmYoz28vLR7aEfLziJNY6QIu7lTp_GiMDNxIch8wP8yA-FNAtHSLL0OFNw3DC5AYE_dUJ1q8kx0q9KxMKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
⭕️
⭕️
⭕️
⭕️
اولیتت برای انتخاب سایت چیه
❓
امنیت مالی مهم ترین چیزیه که یه سایت پیشبینی باید داشته باشه
⚡️
ریتزوبت با انواع  درگاه های شارژ و‌ در گاه مخصوص و اختصاصی کارت به کارت امنیت مالی رو به کاربراش عرضه میکنه
⚡️
از همه‌مهم‌تر واریز و برداشت در ریتزوبت کاملا خودکار و اتوماتیک انجام میشه تمام پرداخت جوایز زیر 15 دقیقه س
🚀
همین حالا ثبت‌نام کن و تجربه‌ای متفاوت از شرط‌بندی آنلاین رو شروع کن.
📲
اپلیکیشن موبایل برای اندروید
🌐
https://RitzoBet.com
پشتیبان فارسی سایت ریتزوبت
👇
🅰
g9
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/84285" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84284">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ناو هواپیمابر تئودور روزولت آمریکا هم پس از نهایی شدن مراحل آماده‌سازی راهی خاورمیانه شد تا نشون بده دکتر عراقچی حتی تو نیویورک هم با تعهد کاری و تکنیکال عمل می‌کنه.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/84284" target="_blank">📅 18:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84282">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">جدی باورم نمیشه یسری آدم هستن که موزیکای قدیمی گوش نمیدن و پاپ جدید یا رپ گوش میدن فقط.
فک کن حس فاز گرفتن با موزیکای سیاوش قمیشی رو درک نکنی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/84282" target="_blank">📅 17:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84281">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترک جدید ویناک به نام "سرت میاد" منتشر شد.  YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/84281" target="_blank">📅 17:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84280">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R90WhbHV3VhxxFujewAahQgMxgmhPh2uq6O-LPCFrWa4sGOE0hTA0WWv9euYnZu7Rqf69wh7zjl0zF07KGeDApTlHoxl64QY-FgTotoyLBsAUksrVfS_Xs_eadvQPaTZU67Et_2K1_gQApNlL7dCkPulTk38bxKJCMqbNi8gfQ3_sJmskH49ONYolsaOzKv0-8AmD_Pzu2zCc7f50jc3Ay0x8Y71fIQLVpG_D8geYw3m3Qt-dzWcrC-rywLJERmSF62CZ3JBc1-Hsqu2p7ZDa5UWGNVP1TJCShvdIE7-IDPj5uSPABIyLaVAgpMWGLe2_XTQIljgKFrfZCfwSLZgCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به نام "سرت میاد" منتشر شد.
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/84280" target="_blank">📅 17:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84279">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEPv6bJcuZ7vbKZEhubjFQG5AVI2oZ95F2hB0NtWb33t1RIKuodKeu-HDFHgFYzvt9az7dpeiqSJxV87Aer_VseSKNPIPDoRAKdtaCb_YtrVsmGM2vcMR-JtMegZPO-HGBLJav6cvBd2rbfUJA1_XSCWbssUy2qXHxoMB3eOG4xgGRFtLpiXI4TAWNsPf-vRNAHloKJyk-53QfyISZytuE2oLv04dkktV-dDzHh3MtwQqiz0ajYv89682GdOrOEaz-kZu0fREaYGenR-UTW_At-s0KMFlVC_crvaxFRQgKbGfgr9yD94Y6FahszGgz4v7QoST-Lyuo9LZYxOJPfeNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی انقد شاهکار شوخی کردی که مردم با شماره ناشناس زنگ میزنن ازت تشکر کنن:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84279" target="_blank">📅 17:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84277">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzU3qmmh6WpCE36F4brIVwTBWiO6U9YYnS11t3mN_B4yBHV1YdOv4ojbUW-ZNRvVdWCaMsdwmpL06rEvgd7iuO85ma6dz3DBh-cmGM1XIVETbtPwlxeblQ_u0Kt6r1PTa5r02SnxXerByOfb8BvPPyVnntyzhMO6BbVGmQ0a1vSyo9O1CRamfLBeyZp2Kn5K-ZrGa8hn9qUSv1ie-9hHor2M_Qr_l0dspvTkBe0hoNWVNXmu4QO4mJkqoEgS5b-CxE0ohrlvQJZlEalpzWNlQjPzkgjISoMVb1iTz-UFoAltLljvld7jUbjIvFMOZSNtrCu3DpgTvm68OFvBWEfe8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f25717c9e4.mp4?token=MWpItvlKN0cdHmbdQ9aLp8qWAycWUuUHaVASi2IDOzjngR_O6AQ-QFAkgHKu7yOThhnNSxVzKpfS2qdV9P0kIx2HrrMG3_tboO4W_Q6hy_MBm-5akq583EwNjpbLHtmYGqVNdPXtGWeg9LX5HN8v5xVBMnwDkVDZ8fliArVHIyD4f5c4efIIQm1Xc91DTP5KEk_dXmdfIeldMd03jyF0TjZw1PEGy_fK7r53b03n5Xs5GwBluNt_RW1xquuL-rYuSbEoRodzH0GbUGRrrH6PZZzLqP_Fy328y2dguO9g7C0RGaK3gYc5hAem5LwOQwgjGdltlc8gjTszudig39H5qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f25717c9e4.mp4?token=MWpItvlKN0cdHmbdQ9aLp8qWAycWUuUHaVASi2IDOzjngR_O6AQ-QFAkgHKu7yOThhnNSxVzKpfS2qdV9P0kIx2HrrMG3_tboO4W_Q6hy_MBm-5akq583EwNjpbLHtmYGqVNdPXtGWeg9LX5HN8v5xVBMnwDkVDZ8fliArVHIyD4f5c4efIIQm1Xc91DTP5KEk_dXmdfIeldMd03jyF0TjZw1PEGy_fK7r53b03n5Xs5GwBluNt_RW1xquuL-rYuSbEoRodzH0GbUGRrrH6PZZzLqP_Fy328y2dguO9g7C0RGaK3gYc5hAem5LwOQwgjGdltlc8gjTszudig39H5qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحید جان ناموسا تو یکی دیگه بیا برو کونتو بده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84277" target="_blank">📅 16:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84276">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مارکو روبیو، دیشب هیئت ایرانی که احتمالا برای مذاکره مونده بودن تو آمریکا رو از خاک این کشور اخراج کرد  @FunHipHop | Mehrdad</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84276" target="_blank">📅 16:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84275">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">واقعا فید کردن موها یه کلک مارکتینگی بود که آرایشگرا پیاده کردن، مجبوری هر هفته بری پول بدی بهشون وگرنه شبیه جنگلیا میشی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84275" target="_blank">📅 15:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84274">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">کصکشا انقد به پر و پای بلو بانک نپیچید و نگید بزودی اونم پول مردم رو میدزده، یهو عصبی میشن فیلمای ثبت ناممون رو پخش میکنن بدبخت میشیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84274" target="_blank">📅 14:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84273">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4XmltXoFCCQ6pi3wY1eVQQuGLE2kZdnE98auO9eVeYeK9EwmzgCycjTKlRYddX4gYWMBrgyi3FpP7zxaEbSGzcyqfmr-jbW5qwrGg0nfGGlsxA6nq0IjuuqG18QNjtTBFnXSAmozohEGFNLeZMgwAI-5yYhnqNXpyRT4w_8tPIkDaixsFJZBodBOS_O_oGkEQSiphEuK1DIu2Am3JJLZwPjNGLp9cpoRkC_KUmn3IoXcLpoQCT7-8Qj5xMxUKKBS_wI3SaAseBGufG8I8DHtlEAwRJ7is_9v2C-2YFUtS7GBCUf5TXKeUSJ0UOAMRjo0wRc_pMyqAUHUZ_SmCD6BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو بازی دوستانه دیروز کونیا اسپور و تیم ملی فلسطین بازی رو دقیقه 89:59 متوقف کردن و گفتن ادامه بازی زمانی برگزار میشه که فلسطین آزاد بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84273" target="_blank">📅 13:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84272">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e053e973a0.mp4?token=eb5_OuvDdDKVYZ3pKNaYgVRgp610TIOP_Lnx7_8MPh5KVWqRuYKhnCA64YvLhQb0Y3SBEx0y3qpcj5d6Z91pm_2xgdgEdzRSQjZ_7qzI4W0YnshLvCwGcP9wSK7iMN37YamQioz4NyPsxDx2P062tbKwQiFMSqgQUpQc9Xq9SensS3K4EW4ZmCEVi0BY3Z2sxZEKNmVJ1TizhAY9fMb2RNvBbdKpl97d9A9WAgbFnv01IE-Trq7O2xy5yYAjPYqOQEzIjRYLm3G-vFzyUkyU4pCrFzAYB1HydOmHJu0PgqccTTJ4w5TBsHNnFmGXF5ZrJgSq-hQ0mgqaWHqJNoJ4SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e053e973a0.mp4?token=eb5_OuvDdDKVYZ3pKNaYgVRgp610TIOP_Lnx7_8MPh5KVWqRuYKhnCA64YvLhQb0Y3SBEx0y3qpcj5d6Z91pm_2xgdgEdzRSQjZ_7qzI4W0YnshLvCwGcP9wSK7iMN37YamQioz4NyPsxDx2P062tbKwQiFMSqgQUpQc9Xq9SensS3K4EW4ZmCEVi0BY3Z2sxZEKNmVJ1TizhAY9fMb2RNvBbdKpl97d9A9WAgbFnv01IE-Trq7O2xy5yYAjPYqOQEzIjRYLm3G-vFzyUkyU4pCrFzAYB1HydOmHJu0PgqccTTJ4w5TBsHNnFmGXF5ZrJgSq-hQ0mgqaWHqJNoJ4SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آ
مریکای جنایتکار با انتشار این کلیپ و نحوه شناسایی و منفجر کردن آدما با پهپاد، ایران رو به جنگ زمینی تهدید کرد
.
تو این کلیپ سربازای آمریکایی وارد خاک ایران میشن، و دو نفرو با پهپاد میکشن!
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84272" target="_blank">📅 12:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84271">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مارکو روبیو، دیشب هیئت ایرانی که احتمالا برای مذاکره مونده بودن تو آمریکا رو از خاک این کشور اخراج کرد
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84271" target="_blank">📅 12:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84270">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">محسن رضایی: قبل از اینکه انتقام آقا را بگیرم شهید نمیشوم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84270" target="_blank">📅 11:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84269">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
خبرنگار حوادث : دیشب تو تهران یه مرد جوون بخاطر اینکه زنش قصد داشته ازش طلاق بگیره با یه گالن بنزین وارد پاگرد طبقه اول شده و آتیش بپا کرده
تو این اتیش سوزی، خودش و خانمش و مادر زنش کشته شدن.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84269" target="_blank">📅 11:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84268">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIzIupHTc8u43giwJwGTKImlx-2pABRRB3W3R7ZFKYBlGWu8-_z975ikItB-eiJ_guRJkec0LwDQbZt0bRotx5B8hUKhAl0jdnN-3_cXwSGuci0ZQjbUR72VMnA73j5iwKcniMfuVa6slAFI5T3e58Uf1O6CecAbqIeEnLR2cKxNaTcFBYJ6LRZL1xbwlEeajt4XZ_pVV-AXUurE5B2rIkhS2pVol7Sd0Wv5YfqYkVWzmPQAPRDb5tssWneAAmP6rthRiCBZB8tOYlLIijpjtgsBJrDRbc1OMFHHW5mreDUxg8V_D274EfxFXM50sdtzepnPPMy81bIpxyQZnc_z0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط بوراک میتونه نجاتش بده
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84268" target="_blank">📅 10:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84264">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rrKyG2ruSjbgV3ndZ4BpfaCT3mY7wFiYTas92D0YGb23qdyKRebsP9n5nfSwfyt4r51PxOxaifmNrICau6QZ8YVGarWNplPA_0a1fkKSoRt2RSGqWrqT6L2b6qIvSbY6yLkQsfgecefUHzeE_dIdK6SqEOz8BiHy6ifk_0BgrwCHBLL4H09oHcJss9yfjMe4G0SoJQuBYnsLOp-PgsE8WgDeziV6FTyuZxA5xUIJzd8Yl3kGOjtKLM2IKcYl9GUBzTQNF5lYnPCvAnZMnGvOkcAiDhq_R-tEB1DKe3UZK1rhr65u42AUKGE_pOLYnfDsybim9MGz6mAu4x4KV1EU9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZTUAAk40t-p4ovHvP1ZlYyXys9yJJT1vyEECpfIBPJbD-YvOPnP4Uyiiya9NC-lQFOLOd4AfEtTMyfIC2N2UwwMqhihx87CvUy3WKxWwGuH22X2l1V0jQbkmE2tOyG05xMxcQedtaxGxX6tI_FW_uaJYKG4w8vpKzIoZn33s5OT3LG2Y0_jCNl97MCZdJwjgmisNyrm1POAMdPyhPKtPsx8lbLE9gGy4kr5hjuIxXBImZ7VfPnUKzPWVmxQcj_sWpOaFZgpRVsXzoGmAqxifE001kh_ooUzaKVtg57V1FmLHGFYmRZiRd_S4EDMTFDEHIQ1K28bZHYMHzOnWS-E5UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ha0lseNJ-DcY6L6CFotF_V7EcM4fV4aJI5ditQ3OjjZpGQWp2fL1sONi-2wHAAl69XBVnAmAXiOPMoUSgsiwXoeJjlpjVPSeBMWObfFRGaZWZ3mC-Fd6KS73QFgHabscJNs87c5CduEz_hIXjyDzgCPXKS4KJzuzH0lvU-9HMDdjYfizX0HYNJyYoMrVpVWNmpinJRVdC3ERKuD1KTYbmJN-IDnNOQBZQo_DfD3q8KeUFZg-4LDpgmG7_8pAlBr8mERiLql6kRwDa8ro-BgcgrEkng3p2ItMNkBNHsmBE-PAMUHt-ovZNI9pEvzxqdZj_8X3GtIAZlu40bm_0K21Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LWU09gIFirCXkdPlgIdUSagAKfOWioHrAZJftajRQUol1d3UQPthNE9MQrexOLyTFGuqAUoobmE5NrKxEmr1JBiiiRJMSHn4-0aj1_CsunaAbMAse25Ke3bDMo4m_qnjhTfcFdk6zHjUhpUD6Yxp_DKD4U-cW-FHpmP3qcjJuCU0VSVvWMgMb21ZchBzUKSKoWgg5eFHs-Ox1EEainVMONPQhb_3Rc8IhGyMIdfFDOpZRucE1ZJv5kvtb8BK0UWMheom0EoPb9DQ5iDb0ZkRM_A-EHFRM2ah4U8O_Nh05Sx51WZd6YmINpLkW_-juWLGKjEpHOKeYSMteSIXLBHd2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های جدید بوراک
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84264" target="_blank">📅 10:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84263">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ritzobet.apk</div>
  <div class="tg-doc-extra">45.3 MB</div>
</div>
<a href="https://t.me/funhiphop/84263" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/84263" target="_blank">📅 10:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84262">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLKRvCwxo-RDD25VN9cng_Hc5fQsPpSxZU5KPfuqrl77JIUq24VCsSOsUlvLepHalXr6nwH6mzveRwogbufLXZXlO9ONbxquv8i6tWo7RnTmU7MoAWr8sU_hhkroqV4FLMc2EA08hp9n8hiEEzTPK832m7pooOdE4oD1IUsoIdbpFcoTTWgR2Lit2yqObEsnFP3vaPQZFw0xckr3KnWwt8eiS7ODFpz-tGlLS0ID5dlEP0wuFuSTJ3neQ1nyIYZeB4ewe0Kl7UVx7NnSiVmkD9oQyBs6eaNHU5eJ-n5JB9obOwsiiU_xxgE-LeCQNjq9-Yq-p_2gMHcUSdovwLhabQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👏
یک بار شارژ کن ، دوبار شارژشو‌ این طرح اختصاصی ریتزوبت برای کاربرای فارسی زبان خودش رو از دست نده
🔵
اولین پلتفرم جهانی و اسپانسر لیگ هلند محیط امن و حرفه ای برای عاشقان شرط بندی فوتبال
⚡️
واریز آنی با کریپتو
⚡️
تسویه‌حساب سریع و مطمئن
⚡️
دسترسی آسان و بدون دردسر
⚡️
محیط حرفه‌ای برای شرط‌بندی و کازینو
🚀
همین حالا ثبت‌نام کن و تجربه‌ای متفاوت از شرط‌بندی آنلاین رو شروع کن.
📲
اپلیکیشن موبایل برای اندروید
🌐
https://RitzoBet.com
پشتیبان فارسی سایت ریتزوبت
👇
🅰
r9
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84262" target="_blank">📅 10:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84261">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">در بازگشایی مدارس امسال جای خالی یک نفر شدیداً حس میشد، شهید رییسی اگر زنده بود امروز بعد از انتخاب رشته مشغول به تحصیل در دبیرستان میشد
💔
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84261" target="_blank">📅 08:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84260">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49c29e72a9.mp4?token=FgU8jGALX6lq2Vmrc34xAh-IBo1qOxPUNtErqzc0aNWRHs9WIfJ5ZZP_V80ZaBd_B2Px1R5kv1WF5LrRC3vGNBGcQS9I3DYBGRHmpv5KXhxYEbEqcYQ7lN2PLqcUUJ98wzdrOOLMqiB_MSpcaPL19cSNlbqTLAzmNVM1_WKrLf6tC8gWmlZ1rl03q2TQeJzqZtWXnIZhfcVCZTFiuEBv1n4nIKc1EQ7MlEx1KZ8EmpqCKawaq2teV1kiV7jECRBezbnEfxDilLzFKZrbfOMlCtxGMQXaFpfd7486eodkDR0l4GM36JFhxEUr7JDEFdINEPTXrBe7M-TgjpVyhegZ_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49c29e72a9.mp4?token=FgU8jGALX6lq2Vmrc34xAh-IBo1qOxPUNtErqzc0aNWRHs9WIfJ5ZZP_V80ZaBd_B2Px1R5kv1WF5LrRC3vGNBGcQS9I3DYBGRHmpv5KXhxYEbEqcYQ7lN2PLqcUUJ98wzdrOOLMqiB_MSpcaPL19cSNlbqTLAzmNVM1_WKrLf6tC8gWmlZ1rl03q2TQeJzqZtWXnIZhfcVCZTFiuEBv1n4nIKc1EQ7MlEx1KZ8EmpqCKawaq2teV1kiV7jECRBezbnEfxDilLzFKZrbfOMlCtxGMQXaFpfd7486eodkDR0l4GM36JFhxEUr7JDEFdINEPTXrBe7M-TgjpVyhegZ_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده امارات در سازمان ملل: «تنب بزرگ، تنب کوچک و ابوموسی، جزایری هستند که بخشی از امارات محسوب می‌شوند و تحت اشغال ایران قرار دارند»
پ‌ن: بیا برو کونتو بده ناموسا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84260" target="_blank">📅 01:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84259">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ: میخایم بزنیم ،بزودی تصمیم میگیریم
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84259" target="_blank">📅 00:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84257">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85208a1d9e.mp4?token=enoUYoBy-mPK36cCuH3717LS5TtsPhU3zmLWU7IR7-H2Poovrf062vobZ4FcS2H3NTzr2f4nDVOnwJVlvQ-oBOuw5WbHkLjusOfYliC30hhWhjgkG7jg1GEVhDirz0N7OGRVeTyi0WW0QOqi0HWZc2PuJqnV-6LCYTkIMTUHWpCHBbAFQmydtBW7FE5z-yVHsRry2TQugtvBctYBAp3Xb1zpTlTbzWPtRypLx6HZraVnWGF-gpm9sTNK-HwXihoIxkz-x23rCmRimz_TF8BUVwEdbBMK5k6M-gB8uHEI1xeA30mZXfVFqbus5qByIOgMWRDG2NVu10eJQEUuuUHQzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85208a1d9e.mp4?token=enoUYoBy-mPK36cCuH3717LS5TtsPhU3zmLWU7IR7-H2Poovrf062vobZ4FcS2H3NTzr2f4nDVOnwJVlvQ-oBOuw5WbHkLjusOfYliC30hhWhjgkG7jg1GEVhDirz0N7OGRVeTyi0WW0QOqi0HWZc2PuJqnV-6LCYTkIMTUHWpCHBbAFQmydtBW7FE5z-yVHsRry2TQugtvBctYBAp3Xb1zpTlTbzWPtRypLx6HZraVnWGF-gpm9sTNK-HwXihoIxkz-x23rCmRimz_TF8BUVwEdbBMK5k6M-gB8uHEI1xeA30mZXfVFqbus5qByIOgMWRDG2NVu10eJQEUuuUHQzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یجور هرکی که فکرشو بکنی خایمال داره فک کنم اگه استالین هم زنده بود خایمال داشت، یسری بودن که میگفتن قضاوتش نکنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84257" target="_blank">📅 00:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84256">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">وقتی از زندگی خسته شدید به این فکر کنید یسری هستن که بصورت جدی موزیکی که توش میگه "بِچه ارچره من بربر" گوش میدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84256" target="_blank">📅 23:36 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84255">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9caab26da7.mp4?token=iiH3ouOgA7CiGGC-ojS3zKduzsnJECoX5jAnrmKkJmlRWO1xf4PfIBkQNl-MZWhprjDuH0j_sbE5FkPm4DRJZ6gTFXw8LF4TE1iXFlBCY5drPf4j4z_VQ4Ns04HKXJsL6jUB8pCu82cPdtVcLvtPDUh39EbN_NsSg9g5FYKRpIapT9nbbdpsnnOgfYWYAtpBddzaN5RNKnovDKaM7proL2bnBvS5z06uUOgi0Dk1adym3tnMAQU3B2HPotAhzK40eolFuLnLWJ_i0TYtcKp2MW3MoGa3PBCFKIsDeafhL5Vb697xmRbvAjNihjVTa8TfIoTzbvCYx5Oi8aiZpdjJIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9caab26da7.mp4?token=iiH3ouOgA7CiGGC-ojS3zKduzsnJECoX5jAnrmKkJmlRWO1xf4PfIBkQNl-MZWhprjDuH0j_sbE5FkPm4DRJZ6gTFXw8LF4TE1iXFlBCY5drPf4j4z_VQ4Ns04HKXJsL6jUB8pCu82cPdtVcLvtPDUh39EbN_NsSg9g5FYKRpIapT9nbbdpsnnOgfYWYAtpBddzaN5RNKnovDKaM7proL2bnBvS5z06uUOgi0Dk1adym3tnMAQU3B2HPotAhzK40eolFuLnLWJ_i0TYtcKp2MW3MoGa3PBCFKIsDeafhL5Vb697xmRbvAjNihjVTa8TfIoTzbvCYx5Oi8aiZpdjJIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این رفتار ها در شان مردمی که چهارم جهان هستن نیست
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/84255" target="_blank">📅 23:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84254">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کاش شرکتی جز دلپذیر سس فرانسوی تولید نکنه، خر میشم میخرم بعد پشیمون میشم</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84254" target="_blank">📅 22:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84253">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBK3Be58fXCvZb1Z-5cLNSHaNupKSvPk64dRI-lRLz2bMqmLUPee4K9RqAJTgOjKz6LNKPrjCrjUU36vxw0ts7Ha_9nYW5O3-ZWapyROJdJS7obJSrMPiyCp3ViIGaSQMK4xzX1XH3xsiwKBVM5Pxku4qsQpplx6iiGQna9g_Jug2FL0jKpzmok7K_QqH2NHFLCE1MtxcG0ngWAERwdCbxl2Zaw0oXmenC_D2pPNWDBNe3UVbErVjfvepMl5Zw4e2uSUXoCFhGoWCpR8xf0Xd6wwn8ufDtcHS9r5Tme6vrbSoyb0TPqxMxE7k53GVUH0eNmDlfb8wxBwMujRmhkNrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین موسوی مگه مجبورت کردن آخه؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84253" target="_blank">📅 22:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84252">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">شاید همه اینا امتحانه خدا داره رونالدو رو میکنه</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84252" target="_blank">📅 22:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84251">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رونالدو رسما خودش اعلام کرد که کمپ تیم ملی پرتغالو ترک کرده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84251" target="_blank">📅 22:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84250">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">رونالدو رسما خودش اعلام کرد که کمپ تیم ملی پرتغالو ترک کرده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84250" target="_blank">📅 22:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84249">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IL2AIl7UKjk9vrcvarzVMw_3V_SicDgFs8pC414y7yUY-VNd0r-lymU4n6ejjyPP5i1Rrjut5TKUuCC_oF5mn0L76eThVbfIzQFdyY6XLrxvKHp50SHHo6EnkreolPqkjkKkN9sm5Fe22CMgI75K_1Yr0YEu5TytxeDLA_v5KYhEhoXCDqJFe7Q6xjyGzVsdmhsj6lbbwWgp2xdBrxwRiqb_4F3j2UbYPIZKBCsOcv7HbFLeGgF-0YswIAHs4iEYfCyDZd3B9kNHCe1uDFMHaPceIoIhY7KEtHKMI_7L0T0zy3AXmimKaFb6qusQy9a1mIZ-kkU_ctEeUWITrXw1Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
🤣
🤣
🤣
🤣
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84249" target="_blank">📅 22:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84248">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzq4EdimixthXDlOxePWPYDw0YmwqEXhA6a8xHy57VLsHui8vaKZyBUwLYmhjal_rsg-BEV0HjiOex6NNGt19iiHe0I1ZHr9N9NGwTlWydGvhdPW8L0goNv6EbIt3eMCWeQ-oPCgkwh49IWzJrSzVUWFYpwZWNZ7uOzMfWNqKh7Hg4iIPZbCG9yx7tefRLRPWyVb45beaPbLD_Hb3af6AUdjOeG8lGraydWp4Vq1ySjxwv6PW2e3n5GqxQRH6GPMqupU69x5A1xRGnfGt8AYCxSUBlPpTF-IulPR29Cb0YpLGOWeV9MnSx-vSAqHaeVaAKVIsBjbdOCoRLRWkrncXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعی که من پذیرش گرفتم با دلار اون موقع شد ۳۰۰ تومن که رفیقمم میخواست بیاد نیومد الان بخواد پذیرش بگیره باید ۲ میلیارد بده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84248" target="_blank">📅 21:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84247">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2qOW1heKKaAozNC_290LqHM54JxNFKYYQCd8i5Lj6J1EFTAa05JT8GyJZSck4z062PPkYcNgjhGhml5n-sVfonPtgStmjWeRgn2ykXNey_Ixl1Qp1mdglVUvN-pt_G9FGjAcTQDvn3Hv71oU21px5H6EjT1ppOBy1J9i_3h4q9EjEkYIruhX1ATJMPt0v9y3kKzaCJXrQf15rJdMQ1MJWQcAizcNMCpqMgW2Hdx1Gr-rgFu9XNtCdQSylBTDQnXdJJrTcuco0MS4mZARHDwOh42Lb3fA7-t0q-7o37ZQecgipqpWBGsKPnMLGJJio7RbcbhEdY0QzuTXUTZASMhYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلار میخواد بشه 420000 حالا اپلای کن ببینم چاقال.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84247" target="_blank">📅 21:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84243">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">رونالدو چون تو بازی قبلی بازیش ندادن قهر کرد و از کمپ تیم ملی پرتغال زد بیرون  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84243" target="_blank">📅 21:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84242">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">رونالدو چون تو بازی قبلی بازیش ندادن قهر کرد و از کمپ تیم ملی پرتغال زد بیرون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84242" target="_blank">📅 21:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84241">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPueTeDfKqcwwx3LyJIvCjuG9SOqOixZ5WpDFO-mg1pkwKQIHFDqzWJRBARD8r2H7JUnypz4kvu9ScPIiqJ8sUEMur9A-lyrJZglhOaGcb_16ey0Ixumh7-iYSLagZGvcN9j_pmhnFfJ39jKXb4LdBhZx0SGEotb20w8OzoV8v9A0kAUxNwuGQ_JyARfTHhWfdXOXBZMPhvpM7lj1xqHbaCIJj9tfTqz_e8VkybSrSOVaaMt7Ue2Uwn_RImfTqqH2-liTkm7gdGZjajdb4OvHyYiIG1PjSJgeYVFTR3ER8yGTJ8JhDJOZzobcoMDDb1dPZjPbC5n3HslMosqS7-afw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش تا حالا شده تو آینه نگاه کنی و از خودت خجالت بکشی؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84241" target="_blank">📅 20:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84240">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بادوم زمینی کیلو یتومن کجای دلم بزارم</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84240" target="_blank">📅 20:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84238">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mf_h2ntwqAdjBvh804xUxvLTeQ9GysCN1omX3wj5FR67TUMzwkb18dqSfh2wD--x4a9LZ879BJQxMkeU-0JN8NlkEr9EzueLQh-CbDrpfSEok7U4nva9xeTUK7AKvyjtHpetLXJ0RNUvTOWn3GZn2I4lAm8vqdcqbcETQdoXuEo9rluIGFkxBLG80w5dapzgu57-fUDynrirXa7asFcneZ2wn9RpqRmlBcbReMHf8BtFxn1PHrfEENMoTluBwbQjOf42Fr2GjgZCcjkPZzuRPa7Ea6xOzAQ-OS2CQavVmNoSHDq_oe5cKm9g7KP4152eI4OwDrdHahPQROt9em339w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدونم اتفاقی عادی تو خاورمیانه اس ولی خب تعداد بیشماری پهپاد جاسوسی تو آسمون تهران مشاهده شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84238" target="_blank">📅 19:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84236">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jK_JjcqAhBVa09JlIMGcH-Ql5DgHXNjUKbiTwjHxawYUQaDmQJOKJQ7c6tPKRQv0mJHgOI_GkQu6yz70RZZ-x9eplCix7CmnzdrDU5-PRixRd4G1Lq94ROydX0RWn6lSpX-v8ZffZpw5HyfXQjZez33fDYvb12p6HEqqLomCjYznTU_kW_c2beuDPGq23e6y8RC-hM1Umlv_boSezORC8NnMCxJUemWqeJuQ7sXBp3HkiEwnCcQypCdH8FHo_dxMr5c5FRxkr6rTBWnfPA4cCWoiaGImTDMyn66GdgygIIzq52y6CZIU4a9Uh0dmJHvcifnuGfNgoUkfpmrY_K7LMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی خیلی بیشعورید
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84236" target="_blank">📅 19:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84234">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgpeC6sTRESF3iUNkbTV9HCCnsKd82X0_l4_ykht1Tv4bn8ce1_K2b3PZhyofy1usaxBnZzx7iiWzw77OR9HKH1p5XSR8yDLCkAcFDrGGaZbJQgdj7KIlXA1UncQdxJjWf9Y7i0SEiWeDyZ8Khi7v9aUlLyDqjsuldR4wsFgT8taMXRuXjSkvyGR7ny5UOBX6sr3sw64O_l7QL6vdf_MJ6eqRrMRfmYnEArl694wXr1lhK_SQoM20j-jZBjj1XIUppr74RzAFcXE05JNw3l5BBxMWnanFIvtv9QxlPzZJ4qeA4wdyXjpkiJqtCL4i47SAZbh8JNcBeVH118WFP2C3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدای همه دلقک بازیا واقعا دلم برا این بچه میسوزه، شده بازیچه دست چهارتا حرومزاده منفعت طلب.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84234" target="_blank">📅 18:36 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84233">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/142f9f8326.mp4?token=HGgweySKJG3ekly8S_P_yccMe_72kMD3pbaHhjjtOIVFqJwedQyWN6XaRCYZBpr8ZDqvfOZOI4tr71uEYfMkCJjmQWP1Xzq1ugVXGoveal-TaWh6B0pGYO-ymNoMSCsvEv7-S5bOmlV3DNIOi0p0VsgoTC4M8I3u5ApgjPDD55U5lQTFxGPcBuVyYl1mpkrE0CzRqQkbaTin0JqmAVjl2VKAxzzwlpJ75V52xQ5sLkXXZphXoo_HpXKOeajIiL75is3qYFWD270fgy6mBK-RVkKeUCUxDICcTUhdia4CtRFLQpe-2dWbjTG-Q5uyXw70PRlHeUIVKJeKZc5XADnagoZLvzlHQnLx6pl4d0EfLoqXXUw8r2Pkm6Cb20fAEIAbYlqekPZJlHe6fJSF0Nx7q_kgps7fbLRa_CZIwXPZKebEW6PqhkK0DFfZRofm24GBaHrcDyGrT12t6DfpKPQm--YuPMGycccgDFPmmWyJqIWSUZyVy24GqF7ZlspWgiL8WryvspRNHF3WlJlqUPG0jRrIA1nJL4SVvOVgu9DiF0sKgFKCjjx2eqmf4Ma9gygblpdvsQD8qjhAq8SKaHDXVMbUxvmS0wQp1EoQnrgxD1vFlmhx-V4h9yMAQS_gBOiAax2-vX8QkNCr6PVM8NRtVGvFMlWpABK4xE_g3MAtq4I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/142f9f8326.mp4?token=HGgweySKJG3ekly8S_P_yccMe_72kMD3pbaHhjjtOIVFqJwedQyWN6XaRCYZBpr8ZDqvfOZOI4tr71uEYfMkCJjmQWP1Xzq1ugVXGoveal-TaWh6B0pGYO-ymNoMSCsvEv7-S5bOmlV3DNIOi0p0VsgoTC4M8I3u5ApgjPDD55U5lQTFxGPcBuVyYl1mpkrE0CzRqQkbaTin0JqmAVjl2VKAxzzwlpJ75V52xQ5sLkXXZphXoo_HpXKOeajIiL75is3qYFWD270fgy6mBK-RVkKeUCUxDICcTUhdia4CtRFLQpe-2dWbjTG-Q5uyXw70PRlHeUIVKJeKZc5XADnagoZLvzlHQnLx6pl4d0EfLoqXXUw8r2Pkm6Cb20fAEIAbYlqekPZJlHe6fJSF0Nx7q_kgps7fbLRa_CZIwXPZKebEW6PqhkK0DFfZRofm24GBaHrcDyGrT12t6DfpKPQm--YuPMGycccgDFPmmWyJqIWSUZyVy24GqF7ZlspWgiL8WryvspRNHF3WlJlqUPG0jRrIA1nJL4SVvOVgu9DiF0sKgFKCjjx2eqmf4Ma9gygblpdvsQD8qjhAq8SKaHDXVMbUxvmS0wQp1EoQnrgxD1vFlmhx-V4h9yMAQS_gBOiAax2-vX8QkNCr6PVM8NRtVGvFMlWpABK4xE_g3MAtq4I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جانی دپ
❌
محمود احمدی‌نژاد
✅
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84233" target="_blank">📅 18:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84229">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">میگن میرحسین موسوی مرد.
@Funhiphop
| Mehrdad</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/84229" target="_blank">📅 17:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84228">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بابا حداقل یه خبر از رشید مظاهری بدید بدونیم زندس این بدبخت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84228" target="_blank">📅 17:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84227">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgdRXmSRdteFqtj0yO_BsYD_kKs2o6Wpx-sfYNaQuLivrNHYO7yy3M6VpTx25w9XT2ch8OltDdmdSjrKPyOhO476aAXMGCqO261StGsFkUy4isiEI5w1ZDY_X4vPeIEkETFSHPmAY2djhT7kf2emlmMJCSWuYNkP2la0xSHK4P8vn9kuo9y1NupT6XmuDJVe1A0dz-QAQ5tHyLDFdL6b7Y0NKwZLXFTHE9Xv4DGXjRdA92SrWv9kT68SgtpxRJ6ZJgnz1Yw3waLkUupeIpU2G5RdQmzvr_clA-PcpQyJg4pnRnKowzX1ThEjJNYxOCN-CMuQHOy4fsX434iufzA0tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبریک به پسر بچه های عشق گوز
برای سریال ترکی "اشرف رویا" یه اسپین اف ساختن که اتفاقات قبل از سریال اصلی رو نشون میده و بزودی منتشر میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84227" target="_blank">📅 17:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84226">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">زن بیژن مرتضوی: بیژن برگشت ایران تو این شرایط سخت جنگی کنار مردمش باشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84226" target="_blank">📅 17:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84225">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvDFJcqzIbTO7WS-OjyTCkCqAvvSqHJWpUmfSZI4Qk7usSvJ0BRjLW7pZLigr5hD4PQuyXx9KutPIf8skrcswT4SgkxSKR--OCrifS1WwOr-QwRSe_xvnLtRkLEN8bIJN1TgSohiKdA6H-4CkyMFKNSQtRDr2N3t7OwKLhN3pNQdZ2xfACVJEop8OuYlRND2RrIBjWqhJhU1YZlaviYkUZBL7lOhmsGsseOAHFefCMrzTNK_oyrAclS16nK9yYDLEGP8DJpVdX5qfnDSI9w_s0zh1O51Yevo1a7SaZ6ofgpigIwwFYF7dtykaG2blowA-rWA3uDtdLkNr25_1ABHOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84225" target="_blank">📅 17:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84224">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بیژن مرتضوی که چند روز پیش می‌گفت میخوان منو بدنام کنن و برام شایعه درست کردن که ایرانم و با شرایط فعلی ایران نمیام امروز برای اثبات حرفش اومد فرودگاه امام و لایو گرفت.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84224" target="_blank">📅 16:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84223">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بیژن مرتضوی که چند روز پیش می‌گفت میخوان منو بدنام کنن و برام شایعه درست کردن که ایرانم و با شرایط فعلی ایران نمیام امروز برای اثبات حرفش اومد فرودگاه امام و لایو گرفت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84223" target="_blank">📅 16:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84222">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آتش‌نشانا دیگه شغل دومشون آتش نشانیه، شغل اولشون بلاگریه
از در و دیوار داره بلاگر آتش‌نشان می‌ریزه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84222" target="_blank">📅 14:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84221">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">یک فروند هواپیمای مسافربری که از دبی به مقصد تلاویو درحال پرواز بود. اول از مسیر تل آویو دور شد بعد از کد اضطراری ۷۵۰۰ که نشون دهنده دزدیده شدن هواپیما هست استفاده کرد  @Funhiphop  | Mehrdad</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/84221" target="_blank">📅 13:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84218">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb2003caf7.mp4?token=roz_1PMv8arw4Un9fKJG3T_H12t1rdsInadafYDuBr_DeEFIX_WkdIoD6fi4g4b-DdPYrHRLtDvI-GebfnHBnJTOT8F39sLv5jE9lc9-JyjKJqLYGfUqh5BFDhMlVTAbwi26yvPePJpyKGwMqdW1yUpCIkq18N7jTEMhP4ZeYzfn3pkSpdLw9mQc4XnexjGwJ2CxMMQ0-APwSfsjs8LBro7SPpGhpjkDX12HblPYdnWIvgMR2tYE1f9SfkRpAcZ-N4_YDAjdhpyUu-bKDjdYVYRPbxB6VYkCEOA4UlWj_5zO5Xe2YY8Clkj_voYjAmWtKeoFww-DdOUzjub6hCdeoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb2003caf7.mp4?token=roz_1PMv8arw4Un9fKJG3T_H12t1rdsInadafYDuBr_DeEFIX_WkdIoD6fi4g4b-DdPYrHRLtDvI-GebfnHBnJTOT8F39sLv5jE9lc9-JyjKJqLYGfUqh5BFDhMlVTAbwi26yvPePJpyKGwMqdW1yUpCIkq18N7jTEMhP4ZeYzfn3pkSpdLw9mQc4XnexjGwJ2CxMMQ0-APwSfsjs8LBro7SPpGhpjkDX12HblPYdnWIvgMR2tYE1f9SfkRpAcZ-N4_YDAjdhpyUu-bKDjdYVYRPbxB6VYkCEOA4UlWj_5zO5Xe2YY8Clkj_voYjAmWtKeoFww-DdOUzjub6hCdeoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میخوام برم استانبول کنسرت.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/84218" target="_blank">📅 11:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84217">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1244f53d60.mp4?token=WwuOpRV6sTggSKpXtFsGPEAzG_Qj9mYTz2SZJuY5foqPmy5VS3qaeI2_OuhM53bBvnaF8XSX5WeoBGluI-oQnAFT8D1GDF7UzworMdbjWn4KRih-smlkDnqwH-i4uauhyB7Fy2izEUSoWSnz8SSzmpWCYm8HuzRtl95yZ0hOEd5sO9lN47L-Bs7d99ypNvInzCAyXbzzqbSha5ObUtU2o1BBJkG4Q2C1ZStjotosRQ47kTPwoR7NWJ87nO5XNbiupp_DWfgH8wPFqM2NP2VA7jVnOB8EezSmoMy0PuSHwKjTUWh8b3ZCWET4I_5afwao8nItItfuuB5t5mZzBoLT9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1244f53d60.mp4?token=WwuOpRV6sTggSKpXtFsGPEAzG_Qj9mYTz2SZJuY5foqPmy5VS3qaeI2_OuhM53bBvnaF8XSX5WeoBGluI-oQnAFT8D1GDF7UzworMdbjWn4KRih-smlkDnqwH-i4uauhyB7Fy2izEUSoWSnz8SSzmpWCYm8HuzRtl95yZ0hOEd5sO9lN47L-Bs7d99ypNvInzCAyXbzzqbSha5ObUtU2o1BBJkG4Q2C1ZStjotosRQ47kTPwoR7NWJ87nO5XNbiupp_DWfgH8wPFqM2NP2VA7jVnOB8EezSmoMy0PuSHwKjTUWh8b3ZCWET4I_5afwao8nItItfuuB5t5mZzBoLT9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پسره برای اینکه علاقشو به دوس دخترش ثابت کنه، رو گردنش تتو زده و نوشته: من سگ دوست دخترمم.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84217" target="_blank">📅 10:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84214">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یک فروند هواپیمای مسافربری که از دبی به مقصد تلاویو درحال پرواز بود. اول از مسیر تل آویو دور شد بعد از کد اضطراری ۷۵۰۰ که نشون دهنده دزدیده شدن هواپیما هست استفاده کرد  @Funhiphop  | Mehrdad</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84214" target="_blank">📅 10:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84213">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">یک فروند هواپیمای مسافربری که از دبی به مقصد تلاویو درحال پرواز بود. اول از مسیر تل آویو دور شد بعد از کد اضطراری ۷۵۰۰ که نشون دهنده دزدیده شدن هواپیما هست استفاده کرد
@Funhiphop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84213" target="_blank">📅 10:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84211">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4Nj0D1bxN5c3EEjmcCMKnJKyzB0QXrVMPLExxzHDizj2aOCiZSo2X-C5GqIiVkfkhH0HoH_dHTG3__fGGKAsRSwi9vpaB-jXzfVXUwI1jrOpjrZYtH8rlXYq0jQOVxzUMY4Om62w6Qelz0zMg1Y53BOSZm1mOHBBSt6kpd-m2NE7JbDep6X2QYqdiSSGedlUekYkH6BWn8FTNg2lFt-DfNbeNyaiDOMmetvUUgSGpRwPm39APsOSEihwURG1RXEcB_SaIPzp9sVomRFVwOKWpbUWO0TcBWrlCqvupJCLx6OFWAq4TJeyyjIioapsi_iUd7qQ3cyfHpO4I5ePckmtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dacdc1485a.mp4?token=Kswd7DQfaQ4KUHW85UlLKjqS24Ua14RyxdViWjK4zLweveHz0DK-e3NKN0dub1zEa0ysxv1R5WeTtgoKwNwIpD3nNW4ZyF9pYkmI7V4UlZ1hWk49LR8vrVEL71qYQ--p1IU6BMrCixuu1UeEbpDVdF0h6Alh_4nynuzBUqDkbytpYf_6wdq-tnLtQRAGFKczUUbZWlM7yl5gsMFUFT4jzVp1H0D8t9muYuWaatM2pSUOA0C1MUG_rtsYVIr5vXJ8zBtL6qUnaJZKrQ_t3iB9BBTFLEkepJU2RwOYQiBZwIUxe9XN_Fwv61Eu7PctA3A_aPPFXzzP5JPMCr_hyNRys1zFHZnE85EvdwoKcGQc0ZVG0li4eZ0psESHuwAKcMH9BH71PDCRg7sy3GiauRfmcnI9LeNDJbpDoPNNrSJF2XY204niAcXvPJ5CTe3yV7b16HauOEQnS4rKCq_pkGp4WKPyE4Bn3CW42s8RkiTBfDSktJuNkOJtCjEGphoLguAL92QW2DnKHufkpl64dXMP1LBBBxGXyL4Ar2H9ToMydrOu-AUmMTFLngoTv5IjwTU96uN4mHhi1XugYVnXGI5pn3UkaHcgM1CR3QrZiUZP-J25ig4ioCE83bpIeatjxPCqpVakLXFEZQtTdeRFcDBe8XRMMEMdhNGi1dKXG4mhLKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dacdc1485a.mp4?token=Kswd7DQfaQ4KUHW85UlLKjqS24Ua14RyxdViWjK4zLweveHz0DK-e3NKN0dub1zEa0ysxv1R5WeTtgoKwNwIpD3nNW4ZyF9pYkmI7V4UlZ1hWk49LR8vrVEL71qYQ--p1IU6BMrCixuu1UeEbpDVdF0h6Alh_4nynuzBUqDkbytpYf_6wdq-tnLtQRAGFKczUUbZWlM7yl5gsMFUFT4jzVp1H0D8t9muYuWaatM2pSUOA0C1MUG_rtsYVIr5vXJ8zBtL6qUnaJZKrQ_t3iB9BBTFLEkepJU2RwOYQiBZwIUxe9XN_Fwv61Eu7PctA3A_aPPFXzzP5JPMCr_hyNRys1zFHZnE85EvdwoKcGQc0ZVG0li4eZ0psESHuwAKcMH9BH71PDCRg7sy3GiauRfmcnI9LeNDJbpDoPNNrSJF2XY204niAcXvPJ5CTe3yV7b16HauOEQnS4rKCq_pkGp4WKPyE4Bn3CW42s8RkiTBfDSktJuNkOJtCjEGphoLguAL92QW2DnKHufkpl64dXMP1LBBBxGXyL4Ar2H9ToMydrOu-AUmMTFLngoTv5IjwTU96uN4mHhi1XugYVnXGI5pn3UkaHcgM1CR3QrZiUZP-J25ig4ioCE83bpIeatjxPCqpVakLXFEZQtTdeRFcDBe8XRMMEMdhNGi1dKXG4mhLKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی اومده یه سکانس از برنامه فان ۳۶۰ که ژوله اجرا میکنه گذاشته و گفته خیلی خفنه و اینا کاش قیاسی و ابوطالب اینا جای جلف بازی ازش یاد بگیرن و همچین شوخیایی بکنن
حالا قیاسی اومده کامنت گذاشته کصخل چی میگی این شوخی رو خود من نوشتم برا ژوله
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84211" target="_blank">📅 10:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84210">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/64cf794cfa.mp4?token=iqFthqfD62XrWtVQ7E618Gt6vymQwfStZFvWfgn4l6_oDVVOE88gP7-Ha7NuCx9ol3_orSKkHlX9GuE3bzWc45QzQ_MoREHcD4FGCTU_lodo5zS7NDNOm_qPLRA7qQOVmJCU9LvKbSW7Jd3pllYG9Nzav_wMIPcOmNvGfE4PYCzzX-3w0uYxACWgjrF_QFHyFWsdoEDS01qkqOevjnwrGl3yD1s7cH2K6DrKQ_kWissWaSzjGJW7rvItD3aLDKOBgh0wGzjbcN_N9HExKZbBUEZLKYjkRY95yV72JEMN-vcsFVdNFp3uWh4LD9gbizOZiLfIZMLPsZ2EOHtLdveNmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/64cf794cfa.mp4?token=iqFthqfD62XrWtVQ7E618Gt6vymQwfStZFvWfgn4l6_oDVVOE88gP7-Ha7NuCx9ol3_orSKkHlX9GuE3bzWc45QzQ_MoREHcD4FGCTU_lodo5zS7NDNOm_qPLRA7qQOVmJCU9LvKbSW7Jd3pllYG9Nzav_wMIPcOmNvGfE4PYCzzX-3w0uYxACWgjrF_QFHyFWsdoEDS01qkqOevjnwrGl3yD1s7cH2K6DrKQ_kWissWaSzjGJW7rvItD3aLDKOBgh0wGzjbcN_N9HExKZbBUEZLKYjkRY95yV72JEMN-vcsFVdNFp3uWh4LD9gbizOZiLfIZMLPsZ2EOHtLdveNmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه بلاگر ایرانی تو خارج که اتفاقا فن کوروش وانتونز هم بوده، می‌ره یه ویدیو می‌سازه که توش نظر خارجی‌ها رو درمورد ظاهر سلبریتی‌های ایرانی می‌پرسه و عکس پارتنر کوروش وانتونز هم اون لابه‌لا بوده که کوروش برمی‌گرده به این بلاگره فحاشی خیلی سنگینی می‌کنه.
بلاگره هم برمی‌گرده می‌گه زنت ۹۰۰ کا فالوور داره هر روز از خودش عکس می‌ذاره بعد حالا من عکسشو به چهار نفر نشون دادم اینجوری فحاشی می‌کنی؟
به نظرتون بلاگره مقصره یا کوروش زیاده‌روی کرده؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84210" target="_blank">📅 03:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84209">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eR9p8PaVcHiMnSWnNTjcUNBE9an7xCaNhW2abFB-PIPot7r7QasyenL2ziLf7oWLJxiyzRrf3A77qPjIiSAkvVXkYHtZ0Wq1vwN5ffvFJjXXgP2JYueyvy0vDpBjFj99IdogQoZ1ZHatEin5S2BDEjUTHeEWhCsrHVNqhoVqvRIubSs9ai2Ef7VDDLT3VFRMcyZJVTMMEQ_RgnIgYIWWtSwWNfklzIOda5rMxYDL9FBuw7i-23qhGFvFuD_xKkTOmPJtvvRrY7evu5Z4Z_BnKJAaX8SJ23YscBUZ0NyxvgO0xOSyaGkvARzwCF0jT9ODQrgNm3iFZeA-b47DKzm30w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواب از کلم پرید
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/84209" target="_blank">📅 00:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84208">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOLhSw3CVaR7bV4zLMMeDMtOsfUAcoV5IGpsPNnJtc57CiyTZFJrodRrpOLlwa45PNINA73bKAhd1bImRQJHgbxpyPO_wHnieGfVSzPIYJ0y5hHQiQ3xVDVaSuqX4cLtR5mgRQ2ycn6wKbSyeDhyeu1YloMtp-Mlqn31jGkFMnAx0DMMylmyKBSD0DHiXJHaMBrBvDg_0ySJTFpi4LCARM6aK17EJGQzbCrk_UhPsO5CA5qaoZbAwpL7VWClRucv2RCpuw3D3AfDnGHweUGV_AFzlCo1SOmQPr3awk0fH5C4h85Pe9_1CskGJWM4-33FLW_FdUU0jQI4I1oSmFiDrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بیانیه میلی‌گلد: بعد از پیگیری‌های میلی دستور آزادسازی طلاهای میلی از بانک کارگشایی صادر شد
خدمت تسویه و تحویل که به علت مسدودی دارایی‌های میلی در بانک کارگشایی مختل شده بود، فردا عصر پس از دریافت طلا از بانک کارگشایی به روال طبیعی بازخواهد گشت.
همچنین طبق دستور دادستان، محدودیت‌های اعمال شده بر درگاه میلی رفع خواهد شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/84208" target="_blank">📅 00:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84207">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">رسام سهرابی جان مادرت وقتایی که جیحونی پنجره کیریو ببند بعد داد و بیداد کن سری بعد زنگ میزنم 110 میگم پرونده هم داری
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84207" target="_blank">📅 00:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84205">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">به وقت سم های عشق ابدی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/84205" target="_blank">📅 23:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84204">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">فرمین لوپز تو کیر شانسی میتونه با ما ایرانیا رقابت پایاپایی داشته باشه واقعا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/84204" target="_blank">📅 23:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84203">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پشمام از یامال</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/84203" target="_blank">📅 22:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84202">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8ZR_AF95bATsn0O9_4WpXZ0ZcnU6XtBCf7zjmvdJAAWaDw1RjOy58zldpAf35R1Fy8WsVbgssp4ejRzlA21p6yyFyWq-t5fAehscf59cajPvsWNtAjOwypqX1gkeZc49ouDUhVCIgCJvU_WWC1T361Ary1SL8XwJrtggnGfjqHgHL_iwYbxWluZW9wdcDVmxGjVUqQJh9wZC1bg-_VWMIJgnPKF-vrYFswlu8y_nFntQeeleNN0DTMJB4K5yI-5TjAc35Y5z4wF_2A4AMyeBM_YFIDrhp-JbpDtP7A6nkHkOyalSuq8gr-ihqic5ogPg0YUsho16_5gYXKNo73fdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز همزمان با پلمپ شدن مغازه های ربکا عکس دوس پسر جدیدشم لیک شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/84202" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84198">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">یاسر بختیاری در یک لایو ۴ نفره اعلام کرد فیت سه نفره او با رضا پیشرو و tech 9 قطعا در کمتر از ۱۲ سال آینده منتشر خواهد شد.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84198" target="_blank">📅 20:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84196">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">بر جرعت میتونم بگم رضا پیشرو درحال حاضر رپر هایپ تریه تا تک ناین
و رضا پیشرو انقد هایپه سه روز آلبوم داده و بعنوان یه ادمین رسانه رپی هنوز گوشش نکردم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84196" target="_blank">📅 20:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84195">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یاسر بختیاری در یک لایو ۴ نفره اعلام کرد فیت سه نفره او با رضا پیشرو و tech 9 قطعا در کمتر از ۱۲ سال آینده منتشر خواهد شد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84195" target="_blank">📅 20:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84193">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Or2dmDpZ5R2Y8tayx5tqevcZxaKNSStTG1GJy7kOJ5uM6RjhvY4UhzOAE4Qc1gjHHzYcG2qNxbBaMcfY9MJozi1tKlKQzHdlzNIZx87ZHyTkhqPZDQtHvm6n0WJP0Uc7G_J2BUG5ExresUSMbd1zqiAUaEALrxz6Pz8tO2O-z_shWkqPrsNI1GHUyWcGgN9THsEJKVCHuuWew2wcWJsmY1oOjy8yIOmFpGCMYkNjUU1Ny3ogV3Xfx7BdElV2jqjRZhWO8arn3AREtCSMbVAgVx3MW9elnAvze9vD6uQNieaFUaGeCnF6NdA30fIxppY61M_SnLc-_nyQnqsFdNfMbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا باید صبح بیدار شیم از شیک زدن زنمون فیلم بگیریم بزاریم توییتر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84193" target="_blank">📅 20:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84190">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سیتی محکوم شد و بزودی حکمش میاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84190" target="_blank">📅 19:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84189">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzqkboMn2-2NebntvBMxLg8KMIYDFeTU0Asrx4ANfZ9wuyGxiDIuij26KRlxuOAYaSBugJNXepyjW338zr4yVsJU9nyiyWVXssBXW_2yG5ITrhaucyDWRfMSoSR-AuygJAfDT5-e-elCH_yNc5ozGS4iTq8DbZhvwXYFEKW5y0WyyT2cmJhWg1Skf9mUjGIKvUVkVTTZF5HzH3f8-01vQf6BTDkvACWNK1CFB1JuuKiIMX1wH-HBZUbuxr-Wg9N5BHvHreBgUtzbUqMPLJVQsh38zqPVk1GvDOn3C6IsQavUiAOclRv2MHRl7CMXvHY5_dYl79eo6nyYP73i7ZfCFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید آرون و کاگان به نام "انکار" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84189" target="_blank">📅 18:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84188">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترک جدید بهزاد لیتو و بیگ شگی به نام "1.6" منتشر شد.  SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84188" target="_blank">📅 18:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84187">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9Yu3N69L8Ncuu8Rr7Z5B7mAVj68XHeuBrXy2rb59J8zi0gPyQscFHXguGEDUdN9JTxab3osh0dHchUuLYyu3QTzzMVOOzVzjAM0nkzXEATOdX9z5LzVcIH40hFzoF2pvHYPA9PTJVLwQahvtYFuiuGW0uUQx9RYR6TTzBi6Ch3KHYOGqra4kreCHel81pG_CtNIbPstQmB8lYwUCTDS89Dyg_G05o2eW89lRlfgOnpylTwzJeEjqtSN4vxU0INj-yDrXqI24pd_qeQTkCXzjDEebAwBZ7vmieOHDzxHJg9lJMfNREmc7otLMPB52krLtwlZN2-KCXIxsYwsVnit4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید بهزاد لیتو و بیگ شگی به نام "1.6" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84187" target="_blank">📅 18:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84186">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpXTtCrezvvydg90jYQz3KysBwEyBe0c6Maegvp8fwJx30hEdzsVD3kkasbB7izMvFhA-94fSyAPjoDyuS76dvUNL7-J0zoIuLpPzfQ7K0vmSkU28BtlAVprEoj1M0Fshl_KBFQNNIEo8ERlHTZ_KHhawFIdHh5DSYVA-TkIV0TyvWsq0KF4THRvbjQPSsdssDZLW7l9t5JuO9GEvJ1D6Jo28L-hHWgIJkYFs8TQbEChF9jfxzHS5sBhf2V5MTLMRq9q4CDTL_zClHVec5fpd9YAoU587_v9qCVUdoImaervPpGKxDsixm8EBqTu8HRbtA_Udw4b5XUpRBz6wc7sBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاره شدم این چرا اینجوریهههه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84186" target="_blank">📅 18:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84185">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862ec698b.mp4?token=gG-ffSV6Wt_vlWyf2YCcbsHKI9mPffo4L6xSIxNgZsp15W8rvZAJNIJOFKTi40NOC9XWXCPUOzyt7UXXZeHhXohKf467fOHDtoUaUDDA7inQvzQlP7fGyHjtQ72Pao0TTjlEFqUBKhpJ4kLCL44QLOgtG5WCoCDaKMG-2YxGnIgMH6tOFSsCE24S5c2MddDh15VDdUA0n4I-7F6TWsItdbRi4ozHQE17fYrkL9cwDyRDuvvxsxf62QmxvL-AAKYikhw9LczUVdCxeT2ZibLoeQT6JWa-WQNkm1QmR3K7sUI78WMbUxHFLjOw4sp6KMhgi7koeoQ4mWLb8srW6mY1sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862ec698b.mp4?token=gG-ffSV6Wt_vlWyf2YCcbsHKI9mPffo4L6xSIxNgZsp15W8rvZAJNIJOFKTi40NOC9XWXCPUOzyt7UXXZeHhXohKf467fOHDtoUaUDDA7inQvzQlP7fGyHjtQ72Pao0TTjlEFqUBKhpJ4kLCL44QLOgtG5WCoCDaKMG-2YxGnIgMH6tOFSsCE24S5c2MddDh15VDdUA0n4I-7F6TWsItdbRi4ozHQE17fYrkL9cwDyRDuvvxsxf62QmxvL-AAKYikhw9LczUVdCxeT2ZibLoeQT6JWa-WQNkm1QmR3K7sUI78WMbUxHFLjOw4sp6KMhgi7koeoQ4mWLb8srW6mY1sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هادی چوپان: یه ساله دارم کابوس میبینم؛ باورم نمیشه دیگه محبوبیت قبلو ندارم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/84185" target="_blank">📅 18:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84182">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ادم اخه طلا رو مجازی میخره</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84182" target="_blank">📅 17:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84181">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">معلوم نیست کی خورده ولی نزدیک ۲۰۰ میلیون دلار اموال مردم تو میلی گلد بگا رفته و هیشکی پاسخگو نیست.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84181" target="_blank">📅 17:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84179">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adf73bf24d.mp4?token=JHoFAFcomXL-lTQo_NHhH596-uKasxKwv3odF08PGcVZqKYx_VF2p2CXbnKpkw-CAzVSSbmIVR7tkLObxpYMpsMOppfx_XuYrPYSe6jfmBuWdP17TFF0Me9c9afj-Z4q1idpVwr6f-hq4y18geG3Nn8TWoXUeEVF90H2kbTWeR9n2zrydbjpae6UFjt_ivI4CGf49X4dxxY7PWKOBvSyT05LTtLzR9_SC_vF-soc4tdMq9po2FzJ8Hqur7JZ_LluisDyqful87zOcIHmMswqpEQ2XLovtvW7Zc08p4Alprki5q1gl6ntglpuqnfoEnRr2hWhFq2LnmeXHPY4gfCPGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adf73bf24d.mp4?token=JHoFAFcomXL-lTQo_NHhH596-uKasxKwv3odF08PGcVZqKYx_VF2p2CXbnKpkw-CAzVSSbmIVR7tkLObxpYMpsMOppfx_XuYrPYSe6jfmBuWdP17TFF0Me9c9afj-Z4q1idpVwr6f-hq4y18geG3Nn8TWoXUeEVF90H2kbTWeR9n2zrydbjpae6UFjt_ivI4CGf49X4dxxY7PWKOBvSyT05LTtLzR9_SC_vF-soc4tdMq9po2FzJ8Hqur7JZ_LluisDyqful87zOcIHmMswqpEQ2XLovtvW7Zc08p4Alprki5q1gl6ntglpuqnfoEnRr2hWhFq2LnmeXHPY4gfCPGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خارکسه حداقل بدون لهجه فارسی حرف بزن بعد بحث وطن و وطن پرستی بکن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84179" target="_blank">📅 16:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84178">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یه زمانی خارجی ها مسخرمون  میکردن بخاطر کالا برگ ۷ دلاری الان چطوری بگیم  شده ۱.۱۷ دلار
سخنگوی دولت: خبر خوش دارم اونم اینه که الحمدالله بحث کالابرگ حل شد و از نیمه دوم مهر کالابرگ رقمش میره بالاتر
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84178" target="_blank">📅 16:34 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn5.telesco.pe/file/uy0pCmQWRcQAFmCkJzS_9MQyl9edPLLnk2gDfpjAW6YUQc1tXX_7z-J6tV8DNxB8ghogv8YowAMGCLJOehYVmVhTwjyOS8xZ8HBd4fA0_eBblHYUrli2Lqnz4EsItRKvRPz9A2jOkcE7LcjK7EkaX1P0rQGsIN5ACh7uIYSvRBawlEqQa8pHn8GDp5luzKlbjiDGIeVLC5oEMitpOfJoj9WFyalq4_e23gYTIUR6e9_Ez9dRqm6GtxNXSmGWpBsvuE7VVif-rci4Qxyn5vc5H8Att5GF2O9iNeBcvFlST4MgHH8dWQRHZlAtKQOVU5MsUOAJ5O9h0in9NyTJRGPi_w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 444K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-03 23:48:21</div>
<hr>

<div class="tg-post" id="msg-104675">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmXtvoZQtIlHgorfkRcogJ5LIbcixsuwNelS2nuUJi1jQqwriFjgu1D8aPoUQBfFoal1nm_e7rQzkLhtuh8-gOXdjTvIlSEDz--EKpnKM1qOAKZQk68IoVV28qSOBm7kLGRd_ZzphUDCdNDJnaY4N8F5DXD3grH5ZKqcxFZ_7qLxBNfoaQ4hQ0oHlWUQc3MsOu1M1-2QZu9uprILqnvlT6j0FY8bNN91q2LXYzveNLetlolwTiHyLCR06K0iOKZ8Uw5aH93FTN37aqIMZGU9M5MOfmo8U0YdbEXx8tsE0eLSq2-cO4Puzetwdwn2R6Cz-3o1SfSE5eIwX-Dpp8WdNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚑
🇮🇷
#فوووووری؛ اوستون اورونوف در بازی امروز دوستانه پرسپولیس مصدوم شده و تا فردا وضعیت دوری احتمالی‌ش مشخص خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/Futball180TV/104675" target="_blank">📅 23:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104674">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41704fa8fe.mp4?token=mHHHDv2Iq8Nbqdk3s_cvvKYpZBUcU48MLZ0aloefqjsdhEWmEbSqSGAh3py6Xxk5NoA6b-WacnMSt_xAm3ZuS325XDmGkA1dF3SAjajtX127dgbciyLE-dnR-riWKVALCQrTkTsqlb08d-Ke7kCSqKhXcf2wWccOIqy80eCPvJZRoSAVrQR1FsC3oHq3kR0QscnP_B-22WqCVjKT9NVciq2NSbg4t2HXzb_28U5zb3l7uY7JEuH17bCfEXa0bQPWFNVAX7DM9hXYz616Y7ifAqTPLNJxL3fhTTvx27HCYyIlMKVk3QAYyaqbv90Jp56q4iLu9J6iH9OCZHAcJiDsNW0gF4pla3hw9LOFXBu7xJmF38hT6Yfv9ONGfSW4f_xIjp2TlBej9ME41GgY7fabB3IbpGUib860623XEEqTuVofDSxkyjfSMOOjnICXZGu8-z3_rBpcqEYeDQ1g9P4z_SJ_3kShQQtfe924jd9vkt-XsoA_tlLrmQjJ-66VOLo__1YZDQSxrYMUVwAFHKVMvHo0e7n9Vk48CCO2rZpP7eE0kYKaMDvfpvk9v_bSPA5KrDNBD8xRtp0P2RJbcZrJd2NemdhRicTVouoklPO1DJWxySUYHYqEffZI0wkA_i329cvTHbxXhNjsh1kW1jq4B5cJjXhEszEalkXl2612jo0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41704fa8fe.mp4?token=mHHHDv2Iq8Nbqdk3s_cvvKYpZBUcU48MLZ0aloefqjsdhEWmEbSqSGAh3py6Xxk5NoA6b-WacnMSt_xAm3ZuS325XDmGkA1dF3SAjajtX127dgbciyLE-dnR-riWKVALCQrTkTsqlb08d-Ke7kCSqKhXcf2wWccOIqy80eCPvJZRoSAVrQR1FsC3oHq3kR0QscnP_B-22WqCVjKT9NVciq2NSbg4t2HXzb_28U5zb3l7uY7JEuH17bCfEXa0bQPWFNVAX7DM9hXYz616Y7ifAqTPLNJxL3fhTTvx27HCYyIlMKVk3QAYyaqbv90Jp56q4iLu9J6iH9OCZHAcJiDsNW0gF4pla3hw9LOFXBu7xJmF38hT6Yfv9ONGfSW4f_xIjp2TlBej9ME41GgY7fabB3IbpGUib860623XEEqTuVofDSxkyjfSMOOjnICXZGu8-z3_rBpcqEYeDQ1g9P4z_SJ_3kShQQtfe924jd9vkt-XsoA_tlLrmQjJ-66VOLo__1YZDQSxrYMUVwAFHKVMvHo0e7n9Vk48CCO2rZpP7eE0kYKaMDvfpvk9v_bSPA5KrDNBD8xRtp0P2RJbcZrJd2NemdhRicTVouoklPO1DJWxySUYHYqEffZI0wkA_i329cvTHbxXhNjsh1kW1jq4B5cJjXhEszEalkXl2612jo0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
ویدیو وایرال شده از دعوای خیابونی عجیب در گیلان که یک مرد در دفاع از همسرش دست به کتک‌زدن دوتا خانم دیگه زده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/Futball180TV/104674" target="_blank">📅 23:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104672">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPgKD_YPWxZfT0mHKEOQbBtlL7gIB3nwZ7NY66BOO0HXHSHMMJGh8dZVerODTxGDc0gkk6JA5blXqyizRARN3WboHaFJFBAJ8G6Mx8cRqplsMY2-1yoBhQ803B1_sCu9YWKUW5mK1jUTho6YPOgLJwd9PxzzexEIMvvuf21MIONExeN0rmtUorOY4KfSheHJwzE3mxiB8R6IE6OziSFvcGEprUl_dRX4MMWir_mZyyiotwno1BmB2Bmb0J2HwsbG0dGJolWHPTOw-xXg9LY5YCdT2pO_RO4a1w9RNM4o8Zb3skCj612OM8pKb6X-OKz2ucni2FulOS5S-n82UZ76qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برونو فرناندز، برنده جایزه بهترین بازیکن لیگ انگلیس برای فصل 2025/26، بر اساس رای اتحادیه بازیکنان حرفه‌ای.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/Futball180TV/104672" target="_blank">📅 23:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104671">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-IUV-zrkjXx5vD8hvZSHru7u9cWzR0LM8i3pAnJrDSLUQekq9wDFIbv3xEp7frVVjX8nY8BZ785AY9foc4N8JgspgEVs49GKN1pvZGeMhrpzUyK1yOsuMl8fIAUq4aseoKoeLNssBifcXaYUFEwjTTHyeje0geVGZ7ZRNObzhx2UiNwEmxTY20_5uU-I0EWmW8X7m5vosZULQAm4PEaFZ1CjAH8DzFGeM5LX-Nc7wiLBcHp-0FlGg-Us9FqP9K5TSWrjWjbRBkMxR3UkowM82TJUoc_r7Xh5BmN30MnFjI8ozR87Jyi5Y_y_eI3IgycpzmhbZAzetbh2_mFiGINEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب منتخب فصل‌گذشته پریمیرلیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/Futball180TV/104671" target="_blank">📅 22:44 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104670">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/090cee5ae0.mp4?token=YajBG8Kk2tx5k__VNbu_9kNM7EyTVKFRIaW5Kjl-wdn6npz-BFnecjw2uO-_L5KV2ec5oeg0emcnA-11sMy_q9gw_nZEzAKam2txNK1Mj_m-zODKGRf8EgS2VSiGAK44BXqgmGmsLzm19HYstowC0LMGmi9xfd38z1YE0IvUDMZxm4h0w1ScDy8Cp-F92PGPTYw6ERiCqeFykqPZ6ZxRFaxlam8WtYHMo3mSedLY8_axbUMiJJeLNrUnlTlEN8DBzaSzRGEAnJ4UJ4LU1Sv9hI8720tzJLByJwB-drYkMa6jngaRTiVbzdhawtdminKkD7qYiZU7fdm9pDGfBXDjxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/090cee5ae0.mp4?token=YajBG8Kk2tx5k__VNbu_9kNM7EyTVKFRIaW5Kjl-wdn6npz-BFnecjw2uO-_L5KV2ec5oeg0emcnA-11sMy_q9gw_nZEzAKam2txNK1Mj_m-zODKGRf8EgS2VSiGAK44BXqgmGmsLzm19HYstowC0LMGmi9xfd38z1YE0IvUDMZxm4h0w1ScDy8Cp-F92PGPTYw6ERiCqeFykqPZ6ZxRFaxlam8WtYHMo3mSedLY8_axbUMiJJeLNrUnlTlEN8DBzaSzRGEAnJ4UJ4LU1Sv9hI8720tzJLByJwB-drYkMa6jngaRTiVbzdhawtdminKkD7qYiZU7fdm9pDGfBXDjxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🎙
سخنگوی دولت پزشکیان: احتمالا قیمت آزاد بنزین به حوالی ۱۰ هزار تومان میرسه و ارقام بالایی که مطرح شده صحت نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/Futball180TV/104670" target="_blank">📅 22:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104669">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NkIdq8kzk-yR94lC_aw0MGvGB07lXsOx7T-ZTpQUCvx0P33CQ-AQJk537CLMVCTlwxIh9McVVmAYE_M9SVypo0vv5dqjPpo5RBymO-BUgdtfum7xdwxMN5m8X_adPCpFv7Wz9ry0nvDbDwreYpMZY6-IOTsDHYkQYUM04qMOie8lBiqebGCeo-eQvsna4rkE8IU3_Tgl-37BfHfM8bqfFmPsv0QRpo-ZmrDZ8onBC5KVO5pt5YSbldJL-3AFwxpyFmHdurFQaKflZrMu_EYntZjBCzusq9DdDTGAtivoIu155o93vkbFveWzoSPWaaikRPvHPQ8foGDuIH18Javs2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گستون‌ایدول خبرنگار مطرح آرژانتین: مذاکرات سیتی و چلسی درباره انزو فرناندز آغاز شده. ژابی‌آلونسو در جریان این انتقال هست و در صورت توافق مشکلی با جدایی این بازیکن نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/104669" target="_blank">📅 22:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104668">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2063216dff.mp4?token=qPn1YJbN8kBir1t-AZj07fMdBh4BxNWr7zNJmupolQ0ZP_KbtHSqqNlt3v3J78EuMT_CCrZUoWmJVn-dYpNSkRl4U1rF1ik5cZZiN970bVHdItwrVC7ae-QXEANMkEmXALPh_FttsP1FNK9h-4n8LIuNMf5J_fHiO9pDdRg5y3xf9rDdzkN_eo8q2xETGedP-oiXOO1hPPgfVuW6jWjF5Uodk0QFqWKyju-coFQFdVepxKzCdEAbmJqPTFKgm5eGz0fAmRHEeu_KvZJOvltN7VbdU8lrMD_kN3qln3-kINhTUskcbkYvjcYqzeyUGvt0d1WIHUlBCUkCK_BR-txmzodiaJbl6V_-2hgYtC4cPiK07NBreZ3c2K21Uq1IZOZoXJ88qJVa9fGn4Acb87GoAXELhFRzlJCbB5Krq79BeP1-iSoVY-AqanPCG50qaVw8D_M7FHrfvfbxX0BI-66KlE3dUhtJX6j3FgV4_3Hp0sy69VAPE2iw0A9l0-3ArPQy1AU3N_yqKDfbUlZ67oE802T1FZeYBb5eBXjsUT3JFE2Ja0sJ9egtWbTy6zEu68NlcbxerWlw10jI5A1adoWmF4EIDSfjYEv5b65dXUyzbaOUUO7quunFaRyKytg4RQW5aDh60UHF1eGesjnEKkRXib4--tqatAHQAB2ytan_KN4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2063216dff.mp4?token=qPn1YJbN8kBir1t-AZj07fMdBh4BxNWr7zNJmupolQ0ZP_KbtHSqqNlt3v3J78EuMT_CCrZUoWmJVn-dYpNSkRl4U1rF1ik5cZZiN970bVHdItwrVC7ae-QXEANMkEmXALPh_FttsP1FNK9h-4n8LIuNMf5J_fHiO9pDdRg5y3xf9rDdzkN_eo8q2xETGedP-oiXOO1hPPgfVuW6jWjF5Uodk0QFqWKyju-coFQFdVepxKzCdEAbmJqPTFKgm5eGz0fAmRHEeu_KvZJOvltN7VbdU8lrMD_kN3qln3-kINhTUskcbkYvjcYqzeyUGvt0d1WIHUlBCUkCK_BR-txmzodiaJbl6V_-2hgYtC4cPiK07NBreZ3c2K21Uq1IZOZoXJ88qJVa9fGn4Acb87GoAXELhFRzlJCbB5Krq79BeP1-iSoVY-AqanPCG50qaVw8D_M7FHrfvfbxX0BI-66KlE3dUhtJX6j3FgV4_3Hp0sy69VAPE2iw0A9l0-3ArPQy1AU3N_yqKDfbUlZ67oE802T1FZeYBb5eBXjsUT3JFE2Ja0sJ9egtWbTy6zEu68NlcbxerWlw10jI5A1adoWmF4EIDSfjYEv5b65dXUyzbaOUUO7quunFaRyKytg4RQW5aDh60UHF1eGesjnEKkRXib4--tqatAHQAB2ytan_KN4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🥶
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ماتیاس‌یاسله بعد ترک عربستان و بازگشت به اروپا؛ عجب حرارت و شوقی داره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/104668" target="_blank">📅 22:04 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104667">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufPKx0pe1tfloX-9rHpZaajypWye5GvHifwFDytHw2Twvgmle-jHBfqHSdBtcPgLuSVCD_mEKtw7c7mMS4TgdNv5wfmmT5sldlNXcjtjhlZeKHV6dZxVwHKmfSRuXkZ4b9uIKTvNr1vAcgCwmJQiRTSfVUDYo9u58uFgF96-L3x1fdvoBmkMCuaA75_7iBZ5CGa-yWfFz2wSe8kfmiCoREb-cny_2iDuMTAbO0NwGmd1pXfNHD9i2lf-ZDgJNoP4Xafs47XwX_ygvb8OrLbraev-QhV2uNZw28IYmPD59pI1HuMjW5PjQl9bQBeYmXzrLzmnt1chBc5e4D4gXngKHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نیکو اورایلی جایزه بهترین بازیکن جوان لیگ برتر انگلیس را برای فصل 2025/26 از آن خود کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/104667" target="_blank">📅 21:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104666">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INxxEOueIh2wigXmARUWgXzaXDw114aFaS2iyyJ8F521lM1Fv49h3F9mT2FukEJeZfAv_W7FcrbbyLq2iTqcpS7r54Hg-mcwDYjgTAui5ySv_YPBcQiF6WG_A7QtHGhgFOrv2bx9VpiTG1CSQtbHIy_twLmD7xQ076beMtiLxwOXaPgpOtSamYLFDVyIRif93Fce1gTN6sdmcsYVTY-Qvhh-gz9hQIRquJYfDrsA3eNxIj0N-TnUZbqCVWT-MeuTth36xx3MaLIW773TJdlrqBgvNFZIsk57WIf3jiClqu9GedA32pHtWr751WTNAzg5pvPyDPm7JmWIMBTmU1P2rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفته اول لالیگا اسپانیا
🇪🇸
والنسیا
🆚
رئال بتیس
🇪🇸
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۲۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/Futball180TV/104666" target="_blank">📅 21:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104665">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccff2e7a05.mp4?token=Fkd7m3x14qTWNX5TqdWy_pjfFZlH_ycLDOsWB7hZr7GM8183ADv8PO9zAOdU3uunx30eZnxbPEGGG3lhJAV2QF85Gup5xUEz507QcQrKhL6K_1HGwTOBRxObz7w89nRg2pb-ZX-Jubn1ClyaykEijbWuOSxBwKamlV7WGjuo3njNweFpypEq1YCRBu6dbHUcWNNZdQT7z1luqFpl4I2oKqxKgzYJXsuHtafwdJvSHE_aWy0Sxlv_YvbaM0QNDJUN3TWMmVCvIQ2i8ZOtFf99wESvnu7csp3cqAvIfcojeWVYK2EbIOxvy3OKeIibXqU3nqFwFmoGnUimIV85iORK4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccff2e7a05.mp4?token=Fkd7m3x14qTWNX5TqdWy_pjfFZlH_ycLDOsWB7hZr7GM8183ADv8PO9zAOdU3uunx30eZnxbPEGGG3lhJAV2QF85Gup5xUEz507QcQrKhL6K_1HGwTOBRxObz7w89nRg2pb-ZX-Jubn1ClyaykEijbWuOSxBwKamlV7WGjuo3njNweFpypEq1YCRBu6dbHUcWNNZdQT7z1luqFpl4I2oKqxKgzYJXsuHtafwdJvSHE_aWy0Sxlv_YvbaM0QNDJUN3TWMmVCvIQ2i8ZOtFf99wESvnu7csp3cqAvIfcojeWVYK2EbIOxvy3OKeIibXqU3nqFwFmoGnUimIV85iORK4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⚪️
ممبینی دبیرکل فدراسیون فوتبال: قبل از جلسه فردای هیئت رئیسه  تقریبا به این نتیجه رسیدیم که قلعه نویی سرمربی تیم ملی در جام ملتهای آسیا باشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/104665" target="_blank">📅 21:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104664">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/az_modGAQEjKo7EHG5ogsfyq6ZJIWZ2NPEpmdO7cDQEmptW-OqL0FeP0HhlqoBvxwrzWKgxmQkfdzGPbELTDADA887dWE3kKwtcsxUDVymcL0el82oee1Zor-EhNoxQcmy4izcYDxxGk0MokMIiMvDcPjY1fDzuOkW8BqBt4CkKnXMEWLEglYRelJUVuwYZosHKOzPlmVNiuBghhGXnZJr7lYW1UPd341nfrg8eWw0L093xiuGI0HcuoED0UN7LgAAa0gyNrx3b6ZbwpPMZJ-yOpP8k4EWLfAlLMXyUpflCgWkDn5HDdUZLRZ15Q1BYpNmZnfhZWlYeM1WUjhbVmNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚑
🇮🇷
#فوووووری
؛ اوستون اورونوف در بازی امروز دوستانه پرسپولیس مصدوم شده و تا فردا وضعیت دوری احتمالی‌ش مشخص خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/104664" target="_blank">📅 21:17 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104663">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db2b316284.mp4?token=qXZAnRBfxL32uZOA2VC1UWuLRiIT64MBc82hRA4W6nJ9hMvljersqHX5X9nC8n3tGGJuxLAPQ89xmSOm3sT0G3xTr6FLQwcS9B-T1E0zmbVLFdl5BcQyogtn_STOIpRVuTB-fUgYkz983tcJC5-ivQDbjldzoiawgyz-Ol9e8q6U2SoLKUVtzVL6qqwpMZlNqKx4JvGjDeSVekXeI-sa5B5i5x2pIoT-JTX2KeO6KNJ57OPJNUNYFwdMmmFuaV80A6G9MCxaxhiTsON9pRnsVeIL47xvMslp8IXGeMbNFdYO2xeA0ypSFVRGLXPClH4TOpPG0tpBLZwIWsruISKeRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db2b316284.mp4?token=qXZAnRBfxL32uZOA2VC1UWuLRiIT64MBc82hRA4W6nJ9hMvljersqHX5X9nC8n3tGGJuxLAPQ89xmSOm3sT0G3xTr6FLQwcS9B-T1E0zmbVLFdl5BcQyogtn_STOIpRVuTB-fUgYkz983tcJC5-ivQDbjldzoiawgyz-Ol9e8q6U2SoLKUVtzVL6qqwpMZlNqKx4JvGjDeSVekXeI-sa5B5i5x2pIoT-JTX2KeO6KNJ57OPJNUNYFwdMmmFuaV80A6G9MCxaxhiTsON9pRnsVeIL47xvMslp8IXGeMbNFdYO2xeA0ypSFVRGLXPClH4TOpPG0tpBLZwIWsruISKeRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇮🇷
اشک ریختن هوادار فولاد خوزستان در بازی دیشب در آرزوی دیدار با رامین رضاییان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/104663" target="_blank">📅 21:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104662">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7BYaw66mZjuArE8zBTW6SEgePcW1ir6dYDzLzBrL7G9DMWMrmxSW-52yf56aqHwrvzHsEVhb2y3DfR1FtcqCI5aV0ZBBXfkidg4X38-m9eg4by1N49VmNqBFCtc9rm5FHJhcp0EzQACvaPC0sAW2cYvyqUwXTYz-z28E2cGz2uFEQHEd72QC2DLw8p5Wm148PUhyb1zZGIZ_m6ykGVPbIReq2YIRgacRrGkIPPQGBPtZ0k0HJ9tH-4y_udIiMr79joRS_xKEOp0QGTYxPg1mYX16jWPQeLtutrWnTxIsyCkUD26WGxUa6KCtNJS3kmohqZuprO0pOs2jy-0QiyfHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فابریزیو رومانو: لیام دلاپ با 50 میلیون یورو از چلسی به ناتینگهام
HERE WE GO
✅
✅
✅
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/104662" target="_blank">📅 20:39 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104661">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r2WhKSwmWdGkikdndUKTuGycmTY2xfApadti52xGZrEZYdA1c8GH5f5swJG_iJbnH3Y27g9iWeWoplmGgPaaARRs8jLmMf69iiTpMw3oxwV8KtK6FTOQkMOp5TqIZby5JZkMiNrsFrqx3e9gueaH85qiz8XwfXS42FNHSGorBJNhXh5tOKCvL-VNNONSy8JGIwIsaivz4AfsvHUZWtAk8wHPYr_gblzObgSE6rFd3OruuKrTp_gSD0C2_0G38ydpvZf52oA8hqUGqhYOp4FMjPE6jFz9vyvHc03uTTcGCq-FjGw11E7QvZdezVj8TOlHvvnku42k8eEgN9wEPJ9Z8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
رونالدو در ترکیب فیکس النصر مقابل الاتفاق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/104661" target="_blank">📅 20:11 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104660">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELC1B9N8wm9dL3t3nDhCFdYr_ZftJ805twFGWbha6XBuxhGM0R4SdKqZoNWBhIvtoqaFYEjN0RGJWuJNIsyzAUJYiQtGtB9_LT807NNkf0HFJwO2dyfK0qiKkwzQNeRIWHQgC-uA3VIA3kA36BDJoZWhJIoIaCbytKAv-EnJfrXX5iZ2ZxpEz43ytgVWn-27gMGVHE8fthj3mLsLr5sSBtbP5C1Vz92vpARqsNZO2ksKbiF-_hfk9JIUXZW3zaqpWLvDZU-QmCdg595PROC2zETOhJCVIozh5LEBw_eb178gkhYi9HqCizU63smVEYwT406o9bs7Hdir0JY-Aes5yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✅
🇮🇷
🇮🇷
بیانیه باشگاه سپاهان: رفتار عارف حاج‌عیدی مصداق بارز رفتار غیراخلاقی بوده و از تمام هواداران استقلال عذرخواهی میکنیم و تنبیه‌انضباطی متناسب برای این بازیکن در نظر گرفته خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/104660" target="_blank">📅 20:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104659">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1H448Hn49_iHW_mX-m0st_TLsjCzuVdwu81Mo5EwS3tKzNp3BeMbUF1iIqo4_kRLGxOc37TGyuxeTNAU5hgPFki0OTFcltWL9ewSyQ8sNITmOOIW96krW6iwzZev7sONLJ1ozGbZY219g7DrczorlIejCXOkBLBgwbbx_lGi28qmJWjHzuj2nq-QokPp8N3LBxB_apPludXGqFz4ai6p28nOF9Z0hBmwGdm85PO-51jMjw9MyqxuYFY22LflQiVFLlFsi6Sr7oim5ntJbTYWZV078TjpBU0E5n_G5Q3F2UzEeW04iANOaGf4K9wBbYemJxupan5aS6vAaiCX0bL1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
دیوید اورنشتین؛
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
لیورپول و پاریسن‌ ژرمن امروز در حال انجام مذاکرات کلیدی بر سر یک توافق احتمالی برای بردلی بارکولا هستن.
🔻
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بارکولا میخواد به لیورپول بره و نمی‌خواد قرارداد جدیدی با پاریسن‌ ژرمن امضا کنه.
🔻
🇫🇷
پاریس این بازیکن رو حدود 145 میلیون پوند ارزش‌گذاری کرده، در حالی که لیورپول می‌خواد معامله‌ای نزدیک به 100 میلیون پوند انجام بده.
🔻
✅
مذاکرات امروز دو تیم گامی مهم در جهت مشخص کردن اینکه آیا میشه به توافقی دست یافت یا نه، تلقی میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/104659" target="_blank">📅 19:49 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104658">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48bb1d2255.mp4?token=aLjuZmoOyrNqftjpLRC0B26_S0yR0N8WVoFXxFpXeB-ebZ60-hQLAxHAVnbVx8x3eveVZSolF4JkFv2fqx33tv2Usd7IvDlbLf1zWk7OVbqwXSDKJptorxCfm7Bv3E2fjqio-X55zlFyIBb-jpDNvDruHY8ODOGdv6BU2tcKUBVaZ9-efebmh8Z_PuQpA1_ZpVo3Xr0BZTpKvugQXw9WlqCYaHi3bTr6mBIRyZUTh7mCfaC6EdKmqpb4hKurFoPa46zC8m7AXYotR06CFowHrbqtZfyIl2jVvFyIAMVw8PtvII2dVQ8_aVHcurR9_tTPVX7s4sAS4YJlqrlVI2nQZov6dngxCbxDLV0phHLykvKNKXdrpQsKzhyQDvSHgpJHhrJyjtapgAogJmjjTdpEPZuU5cKfDVOlKvBt9hH0socFuYAahMsNvUqLj4xd34ws9GbbOSZPYyjoLIcDTSQAZ1nu92dMxozSM6dr-RqIi2NEDs3OEpgU9GGXemZtWqMtF6PoNpe5lWKabfKB5nBuz5yCVg52NrWpOZkIxcfWmfR-FsY53d8PLv5xXWj_exLMN3OIDh0ntoInNq7k1B3j7yUSuS-Fe1Tryl4EeevgUeRIYnQZzMgQZbf4Hj6XzxemUMnIjvcKXua1dYnuxERyjgLlmSKfcxFg37vE2aUjnYc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48bb1d2255.mp4?token=aLjuZmoOyrNqftjpLRC0B26_S0yR0N8WVoFXxFpXeB-ebZ60-hQLAxHAVnbVx8x3eveVZSolF4JkFv2fqx33tv2Usd7IvDlbLf1zWk7OVbqwXSDKJptorxCfm7Bv3E2fjqio-X55zlFyIBb-jpDNvDruHY8ODOGdv6BU2tcKUBVaZ9-efebmh8Z_PuQpA1_ZpVo3Xr0BZTpKvugQXw9WlqCYaHi3bTr6mBIRyZUTh7mCfaC6EdKmqpb4hKurFoPa46zC8m7AXYotR06CFowHrbqtZfyIl2jVvFyIAMVw8PtvII2dVQ8_aVHcurR9_tTPVX7s4sAS4YJlqrlVI2nQZov6dngxCbxDLV0phHLykvKNKXdrpQsKzhyQDvSHgpJHhrJyjtapgAogJmjjTdpEPZuU5cKfDVOlKvBt9hH0socFuYAahMsNvUqLj4xd34ws9GbbOSZPYyjoLIcDTSQAZ1nu92dMxozSM6dr-RqIi2NEDs3OEpgU9GGXemZtWqMtF6PoNpe5lWKabfKB5nBuz5yCVg52NrWpOZkIxcfWmfR-FsY53d8PLv5xXWj_exLMN3OIDh0ntoInNq7k1B3j7yUSuS-Fe1Tryl4EeevgUeRIYnQZzMgQZbf4Hj6XzxemUMnIjvcKXua1dYnuxERyjgLlmSKfcxFg37vE2aUjnYc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💥
ستاره استقلال رکورد جهان را شکست
🏋️‍♀️
عبدالله بیرانوند از تیم استقلال در جریان لیگ برتر وزنه برداری با مهار وزنه ۱۷۲ کیلوگرمی رکورد یکضرب دسته ۸۵ کیلوگرم جهان را یک کیلو جابجا کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/104658" target="_blank">📅 19:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104657">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c5505a725.mp4?token=TGSOXFY-5EqISWS4yXPk8jr7Jg2J_YWiWqVwRV2NjkGC_ggyAUlkwFlVcZng-859xnUemBnEM8YHX_fIkZUJ-vYQPK_diZaOmqLPakZ-JOEIMgwhApiBcBaZouQ7_2zI7htyQVA9fSgJeOAjNiHvtC35ivvOYTZso10xYvYxykFhoqp6ZGRY4MX72cOqrtYhhmmlRQ3jKbEBhJurewnM2F5D0wKWZm7T1BVid2l4ng0_iqJd_bSrNdjGJshbbr5HnHCVtjbsCtnmGAvTdFjx6g9MYB3_Ul6t1F0vnqvvMWWR0DWxjvsVJ02d66y1gKcd0tw-ANsIEDd06I25CHpPjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c5505a725.mp4?token=TGSOXFY-5EqISWS4yXPk8jr7Jg2J_YWiWqVwRV2NjkGC_ggyAUlkwFlVcZng-859xnUemBnEM8YHX_fIkZUJ-vYQPK_diZaOmqLPakZ-JOEIMgwhApiBcBaZouQ7_2zI7htyQVA9fSgJeOAjNiHvtC35ivvOYTZso10xYvYxykFhoqp6ZGRY4MX72cOqrtYhhmmlRQ3jKbEBhJurewnM2F5D0wKWZm7T1BVid2l4ng0_iqJd_bSrNdjGJshbbr5HnHCVtjbsCtnmGAvTdFjx6g9MYB3_Ul6t1F0vnqvvMWWR0DWxjvsVJ02d66y1gKcd0tw-ANsIEDd06I25CHpPjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
❌
⚠️
علی‌محمدزاده: پژمان جمشیدی از اتهام رابطه جنسی عادی هم تبرئه شد
!
💬
محمدزاده وکیل پژمان جمشیدی بازیکن اسبق سایپا و پرسپولیس و تیم ملی فوتبال ایران: قبلا هم پیش‌بینی کرده بودم که رای پرونده پژمان جمشیدی چه خواهد شد. خوشبختانه، متهم یعنی پژمان جمشیدی از اتهام تجاوز به عنف و حتی از اتهام رابطه جنسی عادی هم برائت گرفته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/104657" target="_blank">📅 19:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104656">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
؛ کارلوس‌بالبا هافبک باشگاه برایتون با عقد قراردادی به ارزش ۷۰ میلیون پوند به تیم منچستریونایتد پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/104656" target="_blank">📅 19:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104655">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icdicnOApzqDy5NNXP4jujg8KlHy_h5T_0TTk9HPixey1A81SkE5XQiV_5VbxYBiRyseHk66NkgI_34JwFEaUTwN-JLIvmt3TlzW2LCbxU7dJFVoqRjS8EuHZhIbjxGUHazuWUf01qTiR2ttsWHD5lqwsCP7Z865WRptmuKDsGOo3ZmJNqnbdBouhwxolm3Y5LFhww181OKiyZAz9uZZpTaX4TJMsmQUcOzJWE4-lCF_KvyDgvT43Q8brN2SPqOYAtWVpDvydajwFQnVVutPfrpH0q-sCEja86Clz4XbXJDDvo23mbNLUzsCoOxNa-L7SE_Vzy5eptFG4DRk7cgBWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔴
پرسپولیس در دیداری تدارکاتی با نتیجه 2-0  تیم امید این باشگاه را شکست داد.
⚽️
شهرآبادی و ایگور سرگیف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/104655" target="_blank">📅 19:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104654">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuYiM-OCiEYGIbPiUapPJ32x4NxFa_8Z3SvIgGpmPW2T5bNMKvSni4s0mUkDXK7xZh2iPNhQ6AUxsjSOOKzQS_Xki3xZz5NIOr3xz5Gpv_Ti52aFPU1kII8rBJs_ATG2FmWzxdC4IidOSD_XQRhxfMm8cWY-mEBdBTsojKzD83eiukA9aohhYfmqcE791e9ktjuTVXYpdl_AFUkPEiNWvd24I5lUr5eVSvXyCjUW1vXpIZBwXFuznoZ225RFg3mr5K96LDAfml90nsqxsMZseryLoZeGAP93GZTLjFgc4nh-lS6RWxC0Xz60yv3zg_bagJvvskTAuA6SU3eRqHOaOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
حرکت منشوری و عجیب عارف حاجی‌عیدی هافبک سپاهان پس از بازی دیشب خطاب به هواداران استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/104654" target="_blank">📅 18:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104653">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33e507f396.mp4?token=R_HPgxSD3Taew2fLM9zVTbUGg6zRdYS74Wez2C1cytnR9fNJt_To1NHxkpNjO1CpvVTNBtdJJx9yz4rwYDjVfq5Q9cEjK5ZtGiBBAqVhsVtXT_6bGQEqtFZqCq3aXnEFZ_hKt5N4XkWZikKto88dDlL2q-pL0pjLyd6F1027lNNRWAD7o4zIqD8ZCx65akTtImbXPPQafc5cCbu3EJNumeKV1heo-T6rumrkVSOepUnMkZbRuFeWyBcfSvVwTRHyXji2w73tye5yo5PbC6GeWTbJ3I29c8xKWzqhpnbrCBmV6FWpJ-gieIvcgWpA99G4WNKmRzG84lcwdlutnFJYCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33e507f396.mp4?token=R_HPgxSD3Taew2fLM9zVTbUGg6zRdYS74Wez2C1cytnR9fNJt_To1NHxkpNjO1CpvVTNBtdJJx9yz4rwYDjVfq5Q9cEjK5ZtGiBBAqVhsVtXT_6bGQEqtFZqCq3aXnEFZ_hKt5N4XkWZikKto88dDlL2q-pL0pjLyd6F1027lNNRWAD7o4zIqD8ZCx65akTtImbXPPQafc5cCbu3EJNumeKV1heo-T6rumrkVSOepUnMkZbRuFeWyBcfSvVwTRHyXji2w73tye5yo5PbC6GeWTbJ3I29c8xKWzqhpnbrCBmV6FWpJ-gieIvcgWpA99G4WNKmRzG84lcwdlutnFJYCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
واکنش محمدحسین میثاقی به تصمیم سهراب بختیاری‌زاده برای نیمکت‌نشین شدن علیرضا کوشکی: با تصمیم سهراب حال کردم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/104653" target="_blank">📅 18:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104652">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">بازی شکار مرغ این روزا خیلی پرطرفدار
😍
توم میتونی بازی کنی و پولت چند برابر کنی
👌
از دستش نده
✅
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/104652" target="_blank">📅 18:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104651">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOAreygZXCiYr2iyv2zAxoWseEBQAT4_uQj5gKQRaKm5wUNZDJotNzDm7B-XaebtKjdoI7axseny37S2fWEgmkaVDAIlJhE0GQiamo8k6ACeiJU6FksMPEDRGxA-icRtHl6qdQe5utuvGZuUSwPNl8X-DM9RUTAWs2JM0W328N2MB42IJ9e6gE4YTUvDsPNbzWyH3Gk5I8Zi3aVEF_YC5uGaGkx4oY2D7d9YAKtt4xZkzDWapAzaLgpYgUp8nIgw2QbiNM1XNo-U2GB47i21XnvQIPg02oT_Szu0AGHBi2r5uDpmycbo8-1hCaEJL7TTQ8inXfc0T83cQ3pAjsYlU8uwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOAreygZXCiYr2iyv2zAxoWseEBQAT4_uQj5gKQRaKm5wUNZDJotNzDm7B-XaebtKjdoI7axseny37S2fWEgmkaVDAIlJhE0GQiamo8k6ACeiJU6FksMPEDRGxA-icRtHl6qdQe5utuvGZuUSwPNl8X-DM9RUTAWs2JM0W328N2MB42IJ9e6gE4YTUvDsPNbzWyH3Gk5I8Zi3aVEF_YC5uGaGkx4oY2D7d9YAKtt4xZkzDWapAzaLgpYgUp8nIgw2QbiNM1XNo-U2GB47i21XnvQIPg02oT_Szu0AGHBi2r5uDpmycbo8-1hCaEJL7TTQ8inXfc0T83cQ3pAjsYlU8uwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙋
ویدئو بازی پرطرفدار Chicken shot
🙋
فقط کافیه شکارچی خوبی باشی و مرغ هارو شکار کنی و پولت چند برابر کنی
😍
💵
💖
توی سایت بت اینجا بازی کن و پیش بینی کن و پول در بیار
😍
⬅️
امکان شارژ با کارت بانکی راحت و امن
⬅️
تسویه حساب سریع بدون احراز
🎁
هربار شارژ کنی 12% بیشتر شارژ میشی
✅
🎁
اگ باختی هم 10% باختت سایت بهت برگشت میده
✅
🚨
ادرس ورود به سایت:
💠
http://betinja.bet/affiliates/?btag=2760677
💖
فیلترشکن خود را روشن کنید و روی کشور مناسب قرار دهید مانند المان،کانادا،امریکا،ترکیه،سنگاپور،فنلاند و...
g3
⭐
کانال اطلاع رسانی سایت:
👇
💠
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/104651" target="_blank">📅 18:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104650">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9040b715e4.mp4?token=ksSdX30cJazwUegkqMWZalzY_EbuGNQKnnuN4B7BhLevDHKPRbKIirStVee-J5T7BjbR4NFLFG31ASdfyRMj65dwaR3PUoecpQnPNijTQK8lGmdESbY2yu1_2YGedMjEPbTZuhWYk8qqW_R5eq72D4AWg5ZFyOaLsQjcgmaRUP3VE8fYc7fVLcp8MxLjgRtc7x0iXDkmLUPMaeEuOloOP1zOzsCTne9bRSRBkZIDXpCFsJHw9MYCQyC0DHm6etS8VR3cLPwuq7EXqf51_U2EZ2S-dGxEI4DYegOajVtLp8TbWtayrrNeN6lGGlP3w0ASvqlLgC1Mds4H5ibmBGRZVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9040b715e4.mp4?token=ksSdX30cJazwUegkqMWZalzY_EbuGNQKnnuN4B7BhLevDHKPRbKIirStVee-J5T7BjbR4NFLFG31ASdfyRMj65dwaR3PUoecpQnPNijTQK8lGmdESbY2yu1_2YGedMjEPbTZuhWYk8qqW_R5eq72D4AWg5ZFyOaLsQjcgmaRUP3VE8fYc7fVLcp8MxLjgRtc7x0iXDkmLUPMaeEuOloOP1zOzsCTne9bRSRBkZIDXpCFsJHw9MYCQyC0DHm6etS8VR3cLPwuq7EXqf51_U2EZ2S-dGxEI4DYegOajVtLp8TbWtayrrNeN6lGGlP3w0ASvqlLgC1Mds4H5ibmBGRZVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
نباید هم بترسید؛ آقایان مسئول می‌گویند از تحریم و تهدید و محاصره اقتصادی نمی‌ترسند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/104650" target="_blank">📅 18:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104649">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‼️
⚠️
بخش دیگر از مسابقات جهانی ربات‌های انسان‌نما اینبار در رشته وزنه‌برداری!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/104649" target="_blank">📅 18:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104648">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47d29aa087.mp4?token=JFbA7xaJvCOYOMjplSXKloyWPBLk9rc2JlpDDMSfWIb3hGdQlTRJ1DLQFIcD_CnfuMyDHdVL313_9Eu3tH16jrI9cHAErKt7IlknmofjLTdduwTdzHbt985mTM_1jqlK59V9JvwZtUremqTtTLnynmrHU-keJBZ4p3K1-bYdpWraLOr4QIzB8VD3MIP3ArhJLQ7vHU9rNjapPwTJOLTRjUqFLcD3WzK7cvSib6hkD8HCVKcI5GcHwAB02fb-4J5t5su62Koyr02SzPN2HfII2w07S0cIYRR-mjcxr1FkaDGEGsL2moOLxt8x3KTSs7co5fCP22ffOU8vceBfh75pNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47d29aa087.mp4?token=JFbA7xaJvCOYOMjplSXKloyWPBLk9rc2JlpDDMSfWIb3hGdQlTRJ1DLQFIcD_CnfuMyDHdVL313_9Eu3tH16jrI9cHAErKt7IlknmofjLTdduwTdzHbt985mTM_1jqlK59V9JvwZtUremqTtTLnynmrHU-keJBZ4p3K1-bYdpWraLOr4QIzB8VD3MIP3ArhJLQ7vHU9rNjapPwTJOLTRjUqFLcD3WzK7cvSib6hkD8HCVKcI5GcHwAB02fb-4J5t5su62Koyr02SzPN2HfII2w07S0cIYRR-mjcxr1FkaDGEGsL2moOLxt8x3KTSs7co5fCP22ffOU8vceBfh75pNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای تارتار والا دیشب پرسپولیسیا نه پرس کلوپ، نه‌پاسکاری گواردیولا و نه سانترهای آرتتا رو ازت ندیدن برادر. قبل حرف زدن دقت کن استاد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/104648" target="_blank">📅 17:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104647">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f287b16532.mp4?token=pU_zkF4DSII4B6u3CLd92qpuZJjTSBU8sy13t2nRe_lHe2Rs6djS45azxBv1syTAO9CIGKN4I6mJWgfKqOT6LDhs_b3RdHTyIf4nt2qTXIp3m_bJMSIgaYzKiTIYAQDM687asOh2g5pn6R_E1WD92Q7eWaOxYrYG-Ab-tpG-ndHCtubnmiB2IPFiWgkK-9nHloFVOpRM-5lba5qNTF67lE23Px8TG57fB_I57P4c88wcM7_flDVQv2BEkWy0g0cSwC7MaG_hqLL8e5MkLOsoRUjk1VJftbi_ChXDlFNJSAYX4U6ICYGLy_lN1CGc5OvOC2dUh0ZN4xFlZG_xP9mTzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f287b16532.mp4?token=pU_zkF4DSII4B6u3CLd92qpuZJjTSBU8sy13t2nRe_lHe2Rs6djS45azxBv1syTAO9CIGKN4I6mJWgfKqOT6LDhs_b3RdHTyIf4nt2qTXIp3m_bJMSIgaYzKiTIYAQDM687asOh2g5pn6R_E1WD92Q7eWaOxYrYG-Ab-tpG-ndHCtubnmiB2IPFiWgkK-9nHloFVOpRM-5lba5qNTF67lE23Px8TG57fB_I57P4c88wcM7_flDVQv2BEkWy0g0cSwC7MaG_hqLL8e5MkLOsoRUjk1VJftbi_ChXDlFNJSAYX4U6ICYGLy_lN1CGc5OvOC2dUh0ZN4xFlZG_xP9mTzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
😃
رونمایی از ربات رونالدو در مسابقات جهانی ربات‌های انسان‌نما در پکن چین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/104647" target="_blank">📅 17:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104646">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xw3LpqSfVczRoNE15DFayvB2-OKaGvcINWNPdKTi2OJwD0sIDHKnuHrXe9AGKBj0NCVwS5CMJ6HPuE6uijDEnzyZ8hYcuP4x4KSo8ndTX4I6s2DAcI_Xoqov5aCMGCXyO9e-KIwYJbF9_QcWwkQ2fDGGLgNxTleJi_Fb_SXlCmTjUKpu7xzNEwTt1QDWhWwAcu46zQLznS5rhvo2A6-DGbQnYhNg_3Qi7h75qndYhu8qrwKQlMbH24-q9whU_-Vv9gJIT2zuBtPjVLszzPVghsZzdwP77KWU2BZNatSvwMfmb5x2ZtCQgJPg0YKIxqlo3NQdBzAVhk8sTdeUH9w5mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
روزنامه RAC1: بالده اگ پیشنهاد خوب نرسه به موندن فکر میکنه و فک میکنه میتونه فلیک رو متقاعد کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/104646" target="_blank">📅 17:17 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104645">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2f481f1fe.mp4?token=NQ9-IkU33mLTtJDCxpL-MEddl7J3UIVxc36xA2vFQDi_DdC6hnIA7koQ-rTLcTRCbBQ3V3SYUkkRKxtceOTukjcCC1vK5IFWudiRzofSYvTEeOXvkcl2M-LA49gjpn966f-I_vWxvMbZWnp5XgwDIysgk5jsiPsODXXRaWtSQJSK9E9s9SWdsO8hKC2sa9FpjbtlIL0mxcOIA_h24iHp7wkMEs4OY1AmtB1HscB48zVw6gs2ZnQlYU7ytblgAJEe1ZZ7k8E5_3tfzxLth32UzuC1fuEBLqOywh_yWYEUKYyuSM162V0Q4uRePDg5GNqjh2Nv4Hk1lXTzX43IyfV3zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2f481f1fe.mp4?token=NQ9-IkU33mLTtJDCxpL-MEddl7J3UIVxc36xA2vFQDi_DdC6hnIA7koQ-rTLcTRCbBQ3V3SYUkkRKxtceOTukjcCC1vK5IFWudiRzofSYvTEeOXvkcl2M-LA49gjpn966f-I_vWxvMbZWnp5XgwDIysgk5jsiPsODXXRaWtSQJSK9E9s9SWdsO8hKC2sa9FpjbtlIL0mxcOIA_h24iHp7wkMEs4OY1AmtB1HscB48zVw6gs2ZnQlYU7ytblgAJEe1ZZ7k8E5_3tfzxLth32UzuC1fuEBLqOywh_yWYEUKYyuSM162V0Q4uRePDg5GNqjh2Nv4Hk1lXTzX43IyfV3zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتایج اینترمیامی با حضور کاسمیرو:
4 باخت،  2برد،  2مساوی.
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/104645" target="_blank">📅 16:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104644">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29f38711d1.mp4?token=lJdcqrFCiQMe99Qq2LSJKq-a4x4a-ViYMT7NSt_HFxbiNCWhBeon7H4NgvSMX4t6HfiF1Exx8KTNUgwEMoTAPuWDDxQ8p9S_GDtinCaN65a1ulofRBGcLDGTvzf4h0ZffBTEupmmM-KsVlKshfR-TlCaN35qHnP61ocxOlAhewWPilLmq5FFf1y77RC9N9eenFjQvqZc4Ta0QoDGngNZT8Z-Seo25tKBlWc8SUIVsiC6fL36Tw9Y08nSgHbH9pi2FyFbDKUhjbrOswu3gRhP4H9irqpa9pNnJNJw2wlYSL2v0gPOJVzFgFZ619edU7_ODMIFYuvTyz9qHxBxKFp-Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29f38711d1.mp4?token=lJdcqrFCiQMe99Qq2LSJKq-a4x4a-ViYMT7NSt_HFxbiNCWhBeon7H4NgvSMX4t6HfiF1Exx8KTNUgwEMoTAPuWDDxQ8p9S_GDtinCaN65a1ulofRBGcLDGTvzf4h0ZffBTEupmmM-KsVlKshfR-TlCaN35qHnP61ocxOlAhewWPilLmq5FFf1y77RC9N9eenFjQvqZc4Ta0QoDGngNZT8Z-Seo25tKBlWc8SUIVsiC6fL36Tw9Y08nSgHbH9pi2FyFbDKUhjbrOswu3gRhP4H9irqpa9pNnJNJw2wlYSL2v0gPOJVzFgFZ619edU7_ODMIFYuvTyz9qHxBxKFp-Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هری‌کین در نقش هافبک در بایرن‌مونیخ
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/104644" target="_blank">📅 16:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104643">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88cac48e79.mp4?token=MMdiCgg6fUXh9YUUQCUO5-CY-tplY9RpblVPY_fL1gSJk4jrE63-TEn7u6vDgsQQeaWFEOpcsxCMORCx2QBWgNAs3qVl7VzpmY9sAM9o7ftK1SNcF5f3yTPh8i7cXJ1BU90X8gyV2UcsLgPfjlS5wmNaqyxxsyi0XI_Rs4CCuJ9eFFl9X42oD2Wl0jGTCryt1qgjN96tja2SxX8Xa67XnnZBTDFEG6VFv-F_nylIEy39UrNynvT8JjUyt1YuYLY64GKMEztNz4t_JlEJBqFOWTsJnxJnNt75kmK4hj9QfpZXX5aOtekJgW5MOmuJHoWozPGzr13MLcPUOKhtZfjOTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88cac48e79.mp4?token=MMdiCgg6fUXh9YUUQCUO5-CY-tplY9RpblVPY_fL1gSJk4jrE63-TEn7u6vDgsQQeaWFEOpcsxCMORCx2QBWgNAs3qVl7VzpmY9sAM9o7ftK1SNcF5f3yTPh8i7cXJ1BU90X8gyV2UcsLgPfjlS5wmNaqyxxsyi0XI_Rs4CCuJ9eFFl9X42oD2Wl0jGTCryt1qgjN96tja2SxX8Xa67XnnZBTDFEG6VFv-F_nylIEy39UrNynvT8JjUyt1YuYLY64GKMEztNz4t_JlEJBqFOWTsJnxJnNt75kmK4hj9QfpZXX5aOtekJgW5MOmuJHoWozPGzr13MLcPUOKhtZfjOTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😞
وضعیت روانی خولیان آلوارز در اتلتیکو دقیقا با این موزیک میشه شرح داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/104643" target="_blank">📅 16:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104642">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed5ac9e8f.mp4?token=ED2diYvwzsBnCyn4oNIrIlRvSu1xcV4FeAVrvoJvbCrBMPW1yCQYpSsXpt__CQlEoL4CoBEqR35fQTPMIy5Uw0bjlvXqgt7qPSvza1_D8QNDsdaXPbVVe8QaAYREpAIq3ASAF0wWB9TK6j5Op9VSAKXBk77w4mvzSHj_s2XqtfG2wwqPCPYuXEPtjSlu0baj_9zm0ykhpcu4qj-9_qTecLprRIjDQTpaOPP5HlbF4inc8LaovzRF2XAX0MbDXIiIrQoQkbf8yeOcmCccF7-bISGJReodtbbtF0C9FC7pFFhaV4aJJf69NZPS4_WroJGa3W0PivTborJVpmbt9um4JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed5ac9e8f.mp4?token=ED2diYvwzsBnCyn4oNIrIlRvSu1xcV4FeAVrvoJvbCrBMPW1yCQYpSsXpt__CQlEoL4CoBEqR35fQTPMIy5Uw0bjlvXqgt7qPSvza1_D8QNDsdaXPbVVe8QaAYREpAIq3ASAF0wWB9TK6j5Op9VSAKXBk77w4mvzSHj_s2XqtfG2wwqPCPYuXEPtjSlu0baj_9zm0ykhpcu4qj-9_qTecLprRIjDQTpaOPP5HlbF4inc8LaovzRF2XAX0MbDXIiIrQoQkbf8yeOcmCccF7-bISGJReodtbbtF0C9FC7pFFhaV4aJJf69NZPS4_WroJGa3W0PivTborJVpmbt9um4JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چلسی که بوی قهرمانی لیگ‌برتر به مشامش خورده
👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/104642" target="_blank">📅 15:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104641">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
▶️
❗️
صحبت کنایه‌آمیز و جالب امیرمحمد زند درباره‌ وضعیت فوق‌العاده فاجعه‌بار مملکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/104641" target="_blank">📅 15:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104640">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61023bc5f8.mp4?token=dWwWieqdB08D_YkMmkFSYAM1vqYu7FyjVt8a78NcG7eAAlYpBQOKaEOgPlxd3mIXg5yZE1RTlsK7Wz2q3XVMPQMIDqAJ9r7qhrmd_w3VChCak3vgNZ_Rdd4Pcju7L1eDgQz2Vgp1rcAjCK_uPR2BPxWWJJn1Xt9G4_C2I8hNy-5mUbVq1mkoMVTVDxVvYIFmtNkSoSqGjNKWYNWA_TBcJEFvvd9H_sy9vwX20CPKSqd0PvyHovgxztPKcIdpoSXtiYH2sQTbYCpfCqW-wULOquqP9yNuhSVEpXoMTLbCejNKUEnT1qZ5wMr1Ngg8-guiHqjNGxeYwGbhO_hU8Oz74g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61023bc5f8.mp4?token=dWwWieqdB08D_YkMmkFSYAM1vqYu7FyjVt8a78NcG7eAAlYpBQOKaEOgPlxd3mIXg5yZE1RTlsK7Wz2q3XVMPQMIDqAJ9r7qhrmd_w3VChCak3vgNZ_Rdd4Pcju7L1eDgQz2Vgp1rcAjCK_uPR2BPxWWJJn1Xt9G4_C2I8hNy-5mUbVq1mkoMVTVDxVvYIFmtNkSoSqGjNKWYNWA_TBcJEFvvd9H_sy9vwX20CPKSqd0PvyHovgxztPKcIdpoSXtiYH2sQTbYCpfCqW-wULOquqP9yNuhSVEpXoMTLbCejNKUEnT1qZ5wMr1Ngg8-guiHqjNGxeYwGbhO_hU8Oz74g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک خبرنگار اینفانتینو را گیر انداخت و مستقیم از او پرسید:
«به فوتبال خیانت کردی؟ چرا استعفا نمی‌دی؟»
اینفانتینو اما هیچ جوابی به سؤال‌ها نداد؛ فقط نگاهی به خبرنگار انداخت و گفت:
«چه مدل مویی! آرایشگاه می‌بینمت.»
وقتی جواب سؤال‌ها رو نداری، حداقل درباره مدل مو حرف بزن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/104640" target="_blank">📅 14:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104639">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_8fAOKISaWXwGEHN0tq2ns4mnMs6dKDIpaaXSlAVNglLLj4YcR-prSmVQOXXlV1Hy39WERqyjw899a41Ombuf86ygiutqQOO2pEDEprdvM1ndsx5rwowCFqMxfkretZnsyWEUo87ZCjqELR8IENSJracY89nCFHCLjryViVmUDLT-P_ruAeIaD1HVa7HHo-nLtV2_ZrlH9pBzGWTMblx2OUGR2C75AAI4M6mfh__vRayTp4gv4d659398Q1SXqJWsxw-tim7FUo07s_Imxuoj4bs5HB0ECH0Xf9gZUrXcxTvnXBLS-rOF1s3kuUeHGzGOeWZLGqYUmbxu6I1N7nqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
اسطوره آرتتا چیز ببخشید تارتار دیشب گفت که بازی دادن به جوونا تاوان داره. حالا عکسو باز کنید ببینید سن بازیکنان ترکیب اصلی دیشب پرسپولیس چند بوده
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/104639" target="_blank">📅 14:19 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104638">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKOAjzCd_ZxrAgoqHwZdFAMLmoOo94ndCaDJiKhGNTWHEdQ1TBSqUI_8sgyGQt1_bk7gSfHNjtYlybedjQ_WzqK_aP6BX5CWXgPX9MdhgWvgWNpuZ7SxkUzarQu0kXrJSZ4ZAY3ahFyf2pdvhWCoPbUE1tpYcKm_r23XPTitFuMIrO449URmlSQvK8YYaWJBtOHgV10kXqQLlfVwfEhIApxTWJ-kS6f_C1RHSgVNi_-2Ukoa8uK7efIKoIK49FF3LB8KmOg2Q8A2cpjmGzjiyKtdl4mbffIByDSnof7y7Ltn00Fedi8Y7BrzfMIGEO6RNa5Hl5p1cmXjNZRt4b-4yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
منتخب هفته‌دوم لالیگا؛ پنج بازیکن از بارسا
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/104638" target="_blank">📅 14:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104637">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f029f12cc.mp4?token=OAWe5T0nhOoYH_wuUEVgY1T_eSksL9mzwqqcHi0nfGYVyZP0QCf9k5cMry8LmRQSrlxJ-UA4kVbQYdWE4PF8Yg_08V2eYU12yBpXZ8knlKuuQ5rJ8ID-RnkNiY07YQfIpxfwe5Qf53l5Jw61wBlHFXlUlNPv_Z_p55cQsdjgJSIzfW4JQXzIImOQnZvQdT4PKOgmVJCknBE9IjsrNYXZfbkZU3zCWFOBLFHRJCn-_oDA7Wcomzy_tsCNGlSEet3zcqs1kHP8Zun6b0ilBCPMNtbmnlo8b2PYEkM0Z_piIXyrtTXwdLpVcbjaIq8Ebqrk2LJfkOoSwq2b8e8DMUPxMghb467yJpUZwwG69LpDY8Z00DTjkroROsAbucIe2Mu5O0leJq5GTf_IRR_jm4RgImU5-_PMgcKVNwFMG15-FXhcW-Wc0ygFgYGDlztRVOG3TfX0Xtar8AXj1Yibvy0TngKZ-xNSTfmqru2EjSqIULAdw-bsDuPDDOgLCn6cQHuvM0wOwBdGcC--AtpwMmuEwe4YGyDt1WfgQbAI6OLzminQJch8j4AAj5yzUxnqw0-5QeMakTzoDLN8sbRAYQVesw5AVEjYRabv5BE97vT8NRrQ2q1BNqtr9y1q-LHnyGxvDWLbOcJ6bMDKpq2n3gZ97xSpU9NFkDKOX-05MvATPHE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f029f12cc.mp4?token=OAWe5T0nhOoYH_wuUEVgY1T_eSksL9mzwqqcHi0nfGYVyZP0QCf9k5cMry8LmRQSrlxJ-UA4kVbQYdWE4PF8Yg_08V2eYU12yBpXZ8knlKuuQ5rJ8ID-RnkNiY07YQfIpxfwe5Qf53l5Jw61wBlHFXlUlNPv_Z_p55cQsdjgJSIzfW4JQXzIImOQnZvQdT4PKOgmVJCknBE9IjsrNYXZfbkZU3zCWFOBLFHRJCn-_oDA7Wcomzy_tsCNGlSEet3zcqs1kHP8Zun6b0ilBCPMNtbmnlo8b2PYEkM0Z_piIXyrtTXwdLpVcbjaIq8Ebqrk2LJfkOoSwq2b8e8DMUPxMghb467yJpUZwwG69LpDY8Z00DTjkroROsAbucIe2Mu5O0leJq5GTf_IRR_jm4RgImU5-_PMgcKVNwFMG15-FXhcW-Wc0ygFgYGDlztRVOG3TfX0Xtar8AXj1Yibvy0TngKZ-xNSTfmqru2EjSqIULAdw-bsDuPDDOgLCn6cQHuvM0wOwBdGcC--AtpwMmuEwe4YGyDt1WfgQbAI6OLzminQJch8j4AAj5yzUxnqw0-5QeMakTzoDLN8sbRAYQVesw5AVEjYRabv5BE97vT8NRrQ2q1BNqtr9y1q-LHnyGxvDWLbOcJ6bMDKpq2n3gZ97xSpU9NFkDKOX-05MvATPHE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
یه پسر حدودا ۲۲ ۲۳ ساله با گل رفته بود ورزشگاه رامین رضاییان رو ببینه، رامین پیداش نشد و ایشون هم نشست یه گوشه گریه کرد:)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/104637" target="_blank">📅 13:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104636">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c97e761449.mp4?token=SKKjOWolGaTyDjmtTVtfKtEpFL4HSadu5oStZVYIV8XjHAxPWOT_pDVUwPF3giJfl_ebx40Orpbw4Sr9nbbmofi4yfuRDQoe1uwwqM5prOzJWlrtraBGRqq-07eEnF51qGy0G8koRxFKF2BHkJbSXRQ8ghDODtrlq1RStmuxARNXWnECm1Ouz3C1Mm4D1gm0-BSnLL4mvLcWm8Z8wPHeYIDb0iH0A7ED2VbQa8n8iWMba9s4vjEe3uAk0o2wENvW_2uKFYTpw45I_fnrVqlMUlq6nV49CERdVA1ArBXeiIq_AfGz1FmZRhyGM13CaxiviM6dT8eVVYCvJW-68LOZlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c97e761449.mp4?token=SKKjOWolGaTyDjmtTVtfKtEpFL4HSadu5oStZVYIV8XjHAxPWOT_pDVUwPF3giJfl_ebx40Orpbw4Sr9nbbmofi4yfuRDQoe1uwwqM5prOzJWlrtraBGRqq-07eEnF51qGy0G8koRxFKF2BHkJbSXRQ8ghDODtrlq1RStmuxARNXWnECm1Ouz3C1Mm4D1gm0-BSnLL4mvLcWm8Z8wPHeYIDb0iH0A7ED2VbQa8n8iWMba9s4vjEe3uAk0o2wENvW_2uKFYTpw45I_fnrVqlMUlq6nV49CERdVA1ArBXeiIq_AfGz1FmZRhyGM13CaxiviM6dT8eVVYCvJW-68LOZlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حسن‌روشن: بنظرم تارتار امسال موفق نمیشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/104636" target="_blank">📅 13:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104635">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTJwtyzrXkSO4wvRXkMYE9YNGJSWZU8Mqo-SJFuAwJkrfJVIlw-NwwUppUVkrXKw0wzJl1woYpGNd_voHtAoTruHrfUdBIz83SCt1fTXvqJSgwSi2a1d_oRq8XKK6CF05QySvl4ZstEdh826PNXf4eIRNuRlak8JA3-xqgMbYHqPXTn-w-wzGso7bHUmr8Z0BNfBPgcKacL15mCNjHM44MdAWUZzdaUaQ7g_W--3fV54mfljkpZGTOA_ZPowtXm3koEvEMabPsKNbLW2VZW1uUvXvFX04QrrE4Ck99z64Iv8MrrQTPeNOxHTXKWrSVt7NzlmfqKVPG4eNf1jdm8RkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
☑️
منتخب هفته‌اول لیگ‌برتر انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/104635" target="_blank">📅 13:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104634">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffcea03907.mp4?token=Vdiq517ajECmY0DDHTi_1wKI-9aUjXVB5Jjs9JLdOgwHUvLASzwfMnjaQLZWpCr7ucNZM-eedQYY0exU90F9dfLZ1Jbok0C1Jt06H7W0twh4QuNUf0Goqx1YQlUJ4mJpZvRqzX3aPNbwqyHCDOR58SJUMwOw3zO1K1gvOJIN53KbQSHQR0-9az9_RUPsrUOQNQgipb670vUpxq4oU2-qJTsl0hzkDOdtLmnDq1lEVFAKZ6tRDzqF1B5HaZpOunzQWcrJPoIVDG9GYK-e6H2t_IKtA5Zro6S2OMomuceFc247fuegNpLtrUKdqq1Ox1ze5zgFsExOWi4UXHgjypgIWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffcea03907.mp4?token=Vdiq517ajECmY0DDHTi_1wKI-9aUjXVB5Jjs9JLdOgwHUvLASzwfMnjaQLZWpCr7ucNZM-eedQYY0exU90F9dfLZ1Jbok0C1Jt06H7W0twh4QuNUf0Goqx1YQlUJ4mJpZvRqzX3aPNbwqyHCDOR58SJUMwOw3zO1K1gvOJIN53KbQSHQR0-9az9_RUPsrUOQNQgipb670vUpxq4oU2-qJTsl0hzkDOdtLmnDq1lEVFAKZ6tRDzqF1B5HaZpOunzQWcrJPoIVDG9GYK-e6H2t_IKtA5Zro6S2OMomuceFc247fuegNpLtrUKdqq1Ox1ze5zgFsExOWi4UXHgjypgIWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
سعید دقیقی: دوست داشتم سرمربی استقلال بشوم اما نشد و بوژوویچ را انتخاب کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/104634" target="_blank">📅 12:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104633">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15b0b27abd.mp4?token=XAWpcGcxQxQO61AraFvhKCDhhEstrOEooqqnZehcaAcEIQET1uvxmrm4t6B89759U5R54p2yvEO7CTuHJY26SjeqJwPCY7btI8l_ivwJjo-kG0IOC8ojyRSQQZLlHVZ-Jsgcu7UD8y_So1TKy1dj27kk0g4b2q9fbPJQoZKToCHKbn9UykwWfblzf8TlZ4zY-lTnsVTIOzEAn0rOb9ldJR4xXEo5YoaTpndf2O75CVsOYtyhxBb-IGvLHNU-del4j5h6o4WY6zEiAOHV8PClmvqiAQDzYzD9L0p7kvgR4ay9BhDKgx1fxYxb79NnVk6GsqrvjxlbkysKGQrYIW7eLIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15b0b27abd.mp4?token=XAWpcGcxQxQO61AraFvhKCDhhEstrOEooqqnZehcaAcEIQET1uvxmrm4t6B89759U5R54p2yvEO7CTuHJY26SjeqJwPCY7btI8l_ivwJjo-kG0IOC8ojyRSQQZLlHVZ-Jsgcu7UD8y_So1TKy1dj27kk0g4b2q9fbPJQoZKToCHKbn9UykwWfblzf8TlZ4zY-lTnsVTIOzEAn0rOb9ldJR4xXEo5YoaTpndf2O75CVsOYtyhxBb-IGvLHNU-del4j5h6o4WY6zEiAOHV8PClmvqiAQDzYzD9L0p7kvgR4ay9BhDKgx1fxYxb79NnVk6GsqrvjxlbkysKGQrYIW7eLIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
🇪🇸
گوشه‌ای از عملکرد درخشان لیواکوویچ سنگربان جدید بارسلونا در فصل‌آینده فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/104633" target="_blank">📅 12:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104632">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c053ee6d8.mp4?token=khjTiRmrEmjAVSN5w2GikCSo4YjvNg7rZq2ABmj9NKJ6Qe7y-V70N4yQUcvNgATM1RxRJKDJjdxGuE6QUncbncgKMane8ADoEaSt1LJlrq3brfvQo92uT974BIHVB_qbH5Rm5Ai6WrrmSsBotTX7vScA8PN9j-rXNLxbKzXwzt_e6QVTsL4vGHs-UR7DoCo3weoprmJfmgxmdE_ZXmElj6AQGMAG31a8dOQV-Jw9h0lyQmli2nfJIRdCrfaDSs2LUxF8RBDnxMjiXfZp_YL6rSe_mobSIpl0EJ-_HwgBYs5_PWpWTdIgLx0iHxekJMNyZPTdtXIT-4C1vcG8ESjKbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c053ee6d8.mp4?token=khjTiRmrEmjAVSN5w2GikCSo4YjvNg7rZq2ABmj9NKJ6Qe7y-V70N4yQUcvNgATM1RxRJKDJjdxGuE6QUncbncgKMane8ADoEaSt1LJlrq3brfvQo92uT974BIHVB_qbH5Rm5Ai6WrrmSsBotTX7vScA8PN9j-rXNLxbKzXwzt_e6QVTsL4vGHs-UR7DoCo3weoprmJfmgxmdE_ZXmElj6AQGMAG31a8dOQV-Jw9h0lyQmli2nfJIRdCrfaDSs2LUxF8RBDnxMjiXfZp_YL6rSe_mobSIpl0EJ-_HwgBYs5_PWpWTdIgLx0iHxekJMNyZPTdtXIT-4C1vcG8ESjKbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
امیرحسین اصلانیان بازیکن سابق پرسپولیس: عکس من خیلی طرفدار داشت. به پژمان جمشیدی جواب تندی دادم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/104632" target="_blank">📅 11:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104631">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7472fb85f9.mp4?token=nv9cdpA4t0jm8u4C6M0gKwSkHzwxLzW_9kghy5nmdDeJySK793zJH1hgYL0eiqMYhLevC2dUen5WolT5ZPwRdzPAmnBjJH6JAEb3wjsBj9LVD2TwPnjiIanFO0IVl6gOJGaqRIkoEPLAu1wR9fDY67RTK_3dja-Pb2oIV1bDuFWK2muYMyTgJK1ZsTWAQiAmcLv3QSRfIqmJr_HMS2ysXqb8Ir11axnEKosancgAA0BLY-1kYWbqLCe03UcklMuDhhpGAUmSjT6yUxlxDAsgSUqoTA2UQr-JjfDL5g49LlJLCzXwPHLRU-_lIuK4vAKCVefn_ij2_wOF4bVL2MRllg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7472fb85f9.mp4?token=nv9cdpA4t0jm8u4C6M0gKwSkHzwxLzW_9kghy5nmdDeJySK793zJH1hgYL0eiqMYhLevC2dUen5WolT5ZPwRdzPAmnBjJH6JAEb3wjsBj9LVD2TwPnjiIanFO0IVl6gOJGaqRIkoEPLAu1wR9fDY67RTK_3dja-Pb2oIV1bDuFWK2muYMyTgJK1ZsTWAQiAmcLv3QSRfIqmJr_HMS2ysXqb8Ir11axnEKosancgAA0BLY-1kYWbqLCe03UcklMuDhhpGAUmSjT6yUxlxDAsgSUqoTA2UQr-JjfDL5g49LlJLCzXwPHLRU-_lIuK4vAKCVefn_ij2_wOF4bVL2MRllg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
شهربانو منصوریان: میخواهم پناهنده شوم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/104631" target="_blank">📅 11:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104630">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ya9BgY8r04HWPBvweOjfmPPEsy9C4rwB4jpOqTE_Pb2KzUK8qMv6R6n6fwonsiq3pUHm7e9aJnudvlfNv-GpuV1_f3HUeiT1Ib3PZyPIMzC0hq6Mk_4SuCDL0UU298WyVCc6llZCF1EKtW01VMKHeOc7ZfI4Tvfba-3RWVRdhWWtjr_-ZbZjdnTPhNqQjoKJkIH40PD30O7SJ9mEnArCmM9x76qxYFK8nHlruzH-hRjBa_rKgopuJ7doDCYHUiw_0dTlp2yeMOPo9k_3QxlXnblFDjWoS16E6aNgW94Z3wetnVxl2Ko01GYXuchkquD3fdaHXeSn5Gos41eQmihVaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⚽️
بول بالوس (روزنامه‌نگار تخصصی در اخبار بارسلونا در نشریه The Athletic):
✅
جذب یک مهاجم شماره 9 همچنان اولویت اصلی بارسلونا است.
⚠️
بارسلونا نسبت به احتمال جذب خولیان آلوارز بدبین شده است، زیرا اتلتیکو مادرید هیچ نشانه‌ای از آمادگی برای تغییر موضع خود نشان نداده است.
⬅
بارسلونا تا پایان دوره نقل و انتقالات، تلاش خود را برای جذب خولیان متوقف نخواهد کرد.
⬅
اگر هرگونه نشانه‌ای از سوی اتلتیکو مبنی بر امکان انجام این انتقال به دست بارسلونا برسد، بارسلونا بلافاصله اقدام خواهد کرد.
👀
❌
احتمال زیادی وجود دارد که بارسلونا در صورت عدم موفقیت در جذب خولیان، هیچ مهاجم جدیدی جذب نکند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/104630" target="_blank">📅 10:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104629">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_Q3D_X63_S8_g5JOYPQiyBmMmRp8fJocuJkPPqNGiSSGcoqc460ZZQrot6SU2d2gdK9Ksx5HZF_znXhMXQPJleTv1fcBZd5LhAriOHNT1YF16Uwfk7-17Bx3F1H_4vU_Ev20bsk_ULVei9_JjxSAzy0gAJFVo8lpdHKCp8z-6gZ2fWbdnyAec96wXy9hmPX2uumXvvGX_U0V0gLPDNfopwKi5waxtmMVJoZsKL_WDSBJ1hIryLKDf-2MLLQ9l63zCS6Cs708w4zvK2QmUtCxh4EPr5tiUFtL6Qe_RUSzSnpNJkXGGHXkXk_RX-1x89SysM-OX5fSA5sE4VdWR9Xkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گستون‌ایدول خبرنگار مطرح آرژانتین: مذاکرات سیتی و چلسی درباره انزو فرناندز آغاز شده. ژابی‌آلونسو در جریان این انتقال هست و در صورت توافق مشکلی با جدایی این بازیکن نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/104629" target="_blank">📅 10:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104628">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CH0opuGUBdCOHYGJieN8bZHNUA9hzyVP5zRw4cZC8pJj7eY2UNUJ1J_VS-Z8R_2cOcgstLuwcMXnmkZieNOVv2gixgWuTJYZ9bicz-mj6qlbvTVRxSDq7x0Q8Ew719UCik9q7Oq3owIkCGCuKIO3BE-zuWrgOI-_smr8PdmDg3hBADGB_y-pKh3P9jVzGeeJipY7L39v66l_tPc6HS83j8IhowSgpJ74U_GY81KxaMlb7gsXwFsAzp4hjQcFkr44tAVCjU0uikbQENHf8ZAKhGpSBNqkpJNDHXb-LO3SG536SZ3C7C6jOpaIApMFQrUFpbPuBDaZQ5HKGkCSE2mQ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
نشریه The Athletic: بارسلونا با نظر مثبت هانسی‌فلیک، لوکبا مدافع لایپزیگ رو زیر نظر گرفته اما جذب این بازیکن در روزهای پایانی نقل‌وانتقالات به خروج بالده گره‌خورده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/104628" target="_blank">📅 10:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104627">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZZs5uRbfr89txd_BdIy5-7hluMmUdBoTvtIXvXpOk8hqTa4js8Wr24SfNP8-XgGpvS9K5bxtnBQWicY-f76ffby80oEucGqq4T3J3UsvkeLhSegSdf0QdWXmcwvco6ZEDR5kV00YVQLw8kgTYiWxydJnwOETZMVKHEJibEtItxh13sU-SMmZEvOY8ThzbIRecIosAhwGbakJ5ZwzEOUuhW_Ap24d2L2ZbEYJn0O1HwIH3cOoZzKHGWxWn3FTfp4WJW6GqDLFVnr7e8Ste4eI2JgIWF73OVDc66mWbc7Wt370qSK8nlEqUWPh9OYg_LZNAqChDLa1ig9fQuFxUV2lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
‼️
انیس مارتی: بارسا بعد بازی اتلتیکو - ویارئال تصمیم گرفت که خولیان رو تنها نذاره و قراره تا اخرین لحظه منتظر بمونن و اگ این تابستون نشد ، ژانویه و تابستون بعدی براش تلاش کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/104627" target="_blank">📅 10:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104626">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/Futball180TV/104626" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/104626" target="_blank">📅 10:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104625">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtzSsbDt5OwPRUU9Jd08ILgybeZfPpMlpHHxrukdgq3afBCJkswWep1qt1nsKCR4dMTtg1WQKYQ_GOvhflN6WBEcfsb-g_qYyCYckXfcGfVz2kYiWuPuFrUwiQIXtJ4DaaLjmnCLSomukpsPcGYKu9E05lNJPs9gWDiU7OHdZhuq0NAK66VCipSx_tBu_nM52Bth2S46OAMW_l1p1QrBGqFakd5cghhzKO9gUiwWV7xHLmzgUfuQ1U45M8veZUOHiVgX-_Ev0eiHg6oFSCTXE6u0a2jFMJZgnCu0abJWTgKWcKc5yjLtRMoa6MOi9pF0RxkD3x3mw_snfxJs-rGy4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️برای دانلود اپلکیشن کلیک کنید
👉
r3
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/104625" target="_blank">📅 10:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104624">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/638bfc01fb.mp4?token=hUecdxwjGmugapexbixWUBaDIucHwF2yG5KARqikorPLlqNfQBKyNeq7Lg_wwMTE_Kjw6U1R-6Wl3ix4pvK88aaFbWKThENRLE8xLJPGkbQJSwWeYl1OGHz4aim1f7OWE_2FqWz0PV5h8yNdVWiu5inLsceCMtH5P4ACHlR_K35VYuNaihmP4Z37y11REjFaL95DKhD3XhIJYqbpq__G-GJkEQh08cxJY0bpD_Sz2ACnshTamyQgXUVhjrG5BloEsrX2qPgU46eis4iU06lr9CcTaPQqz19u0_ef2MxoB4pqeh1VbBzE7B4h1_8mTDzO1WgTyyd6QN7HYX5JKh_Hxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/638bfc01fb.mp4?token=hUecdxwjGmugapexbixWUBaDIucHwF2yG5KARqikorPLlqNfQBKyNeq7Lg_wwMTE_Kjw6U1R-6Wl3ix4pvK88aaFbWKThENRLE8xLJPGkbQJSwWeYl1OGHz4aim1f7OWE_2FqWz0PV5h8yNdVWiu5inLsceCMtH5P4ACHlR_K35VYuNaihmP4Z37y11REjFaL95DKhD3XhIJYqbpq__G-GJkEQh08cxJY0bpD_Sz2ACnshTamyQgXUVhjrG5BloEsrX2qPgU46eis4iU06lr9CcTaPQqz19u0_ef2MxoB4pqeh1VbBzE7B4h1_8mTDzO1WgTyyd6QN7HYX5JKh_Hxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
روایت بامزه داودسیدعباسی از اولین روز حضورش در تیم‌فوتبال استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/104624" target="_blank">📅 10:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104623">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a51e8569ef.mp4?token=jIN3d2oudFfiIz682XxEEUJ-ctybjHhXFsrPW063q6fx-k-IvVuw417zR-SAfdKMGptY2Gx6yQq1lKflKVSE3W_UeQ_T_LYTQolslUBsKouThbxaJkbO0n81LNX-b1KSVNXktQ4eS7DelR5cKllnG23Bv1-3lOH9RCLVt79M3yJ6stVYB-Uz2abQwa87GVUQStp6can-rRfcxbLxE3JFkC4AIo72QCO-Yu5bRqagly2eS32yc742r_-MGi2MtGSdlUBlWWLyQKLEeZwHLNz_7nJPf_G4J3sQAdsV0wse8FqykgDepiWnwCiTCsMLIm4ccsM0ILEhVIz6x-qWgLeZhoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a51e8569ef.mp4?token=jIN3d2oudFfiIz682XxEEUJ-ctybjHhXFsrPW063q6fx-k-IvVuw417zR-SAfdKMGptY2Gx6yQq1lKflKVSE3W_UeQ_T_LYTQolslUBsKouThbxaJkbO0n81LNX-b1KSVNXktQ4eS7DelR5cKllnG23Bv1-3lOH9RCLVt79M3yJ6stVYB-Uz2abQwa87GVUQStp6can-rRfcxbLxE3JFkC4AIo72QCO-Yu5bRqagly2eS32yc742r_-MGi2MtGSdlUBlWWLyQKLEeZwHLNz_7nJPf_G4J3sQAdsV0wse8FqykgDepiWnwCiTCsMLIm4ccsM0ILEhVIz6x-qWgLeZhoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صفر تا صد قهر سیدحسین و روزبه از زبان میثاقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/104623" target="_blank">📅 10:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104622">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rENKBdiZKBs6oCqB_Z2io-_HsVDzgvzdE3a5fWwFReWzQukFUuEnIahh-SlibbCI_IX4TWm6vV9RPEW9k_XW-wg5mYSXKdwfU0m54uKfXASmuL8dZckzEUVj244bfusmMOT1iMoJDD8p66OiLV-KDERE3H1P8RjNQ7pSmJAYuvNLB28HBn9SJ2TjXhK_GgdrS8pqJqLlvuGVIAooShGS0195tz5eLQ9XzzWwtJzC6n9b4sRxq3iX5QizcgLkstPQRZ2RXT3OmC1XEJxwADfi9ZdI5amnYdo5-_ZQYuKx5cqOiqE3UKEYQK63MT2PlYFSmEoMazrW5K8Q3pUuKajeNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
⚽️
امشب و فرداشب بازی‌های پلی‌آف لیگ‌قهرمانان اروپا برگزار میشه و قرعه‌کشی دور گروهی روز پنجشنبه انجام خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/104622" target="_blank">📅 10:04 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104621">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/288552d3bc.mp4?token=OFIEX2nrt5H1h9OiTKlZCyiF1I7KlCFDrbJn4dD2Kwb05KSISlpI7fetXn92TLnkatTbWEQtsuoG6DFSN5_C84WjGHEyIzscNR6kgytAWN7q5c7xmivYBNetYQH6iBPs6cLltpiDg2sagMOCqMtcxdtVlMYEDx9hEGrnNN7O51R41dUJjv03cGiKyvNuLIz3KwzU2a1UphpGosVDsJ8pfqmGCfZc8L2hmWgKVY7gshDCtoHxFjWPUeDnZl6bLNBGysC_R7c0BZKrZTEep8InLynHw2tX93OC8goTnkNtrN7oV8PMXIXNoxou2f2AqC1sTtgVw7OWBUnzitrTe-JH0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/288552d3bc.mp4?token=OFIEX2nrt5H1h9OiTKlZCyiF1I7KlCFDrbJn4dD2Kwb05KSISlpI7fetXn92TLnkatTbWEQtsuoG6DFSN5_C84WjGHEyIzscNR6kgytAWN7q5c7xmivYBNetYQH6iBPs6cLltpiDg2sagMOCqMtcxdtVlMYEDx9hEGrnNN7O51R41dUJjv03cGiKyvNuLIz3KwzU2a1UphpGosVDsJ8pfqmGCfZc8L2hmWgKVY7gshDCtoHxFjWPUeDnZl6bLNBGysC_R7c0BZKrZTEep8InLynHw2tX93OC8goTnkNtrN7oV8PMXIXNoxou2f2AqC1sTtgVw7OWBUnzitrTe-JH0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🎙
الهه منصوریان: همان‌طور که با علی دایی بد هستند، با ما هم بد هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/104621" target="_blank">📅 09:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104620">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9080d9bf87.mp4?token=vz85Jq7uOdDyu_YIjc2Tld5fuKe6MivdA_2I3hAqonmpjkJeeNdr_j6Kog5fa7WysBpxbWrxvQKfCAl3Lw1RLkkZ_nGfHdSUU2n0KoQZYjBGO86T_rOuT8Fmvv7hDIDfvMmp1CGeoZ9VRL0ZTrdoItBlPPULmpETvMzlATZiyN-TbKy0xd1ZqCLN-SKJgjAfij5tr5BC6gexd9FLUjq6sXxRus9m1jkDUAgzCy_17HpYbLTegUTfY1hUA9xicpPbqa-ECUR3Vgp12itG_YE5db1utk6yCFqelDnrNqiKHHBE6G4Nnq-5btJolHzknmLjCtIPp0tnKgBDSnMhKShe5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9080d9bf87.mp4?token=vz85Jq7uOdDyu_YIjc2Tld5fuKe6MivdA_2I3hAqonmpjkJeeNdr_j6Kog5fa7WysBpxbWrxvQKfCAl3Lw1RLkkZ_nGfHdSUU2n0KoQZYjBGO86T_rOuT8Fmvv7hDIDfvMmp1CGeoZ9VRL0ZTrdoItBlPPULmpETvMzlATZiyN-TbKy0xd1ZqCLN-SKJgjAfij5tr5BC6gexd9FLUjq6sXxRus9m1jkDUAgzCy_17HpYbLTegUTfY1hUA9xicpPbqa-ECUR3Vgp12itG_YE5db1utk6yCFqelDnrNqiKHHBE6G4Nnq-5btJolHzknmLjCtIPp0tnKgBDSnMhKShe5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محرم نوید کیا مربی سپاهان در برنامه عادل فردوسی پور گفتن که باید به عقل کسی که حسین نژاد نبرده جام جهانی شک کرد ، منظورش با آقای قلعه نوعی بوده ، در اینجا جواب هاشم بیک زاده بازیکن سابق تیم ملی ، و استقلال و سپاهان بشنویم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/104620" target="_blank">📅 09:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104619">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66e469197b.mp4?token=kaElJlbFM-jdyo4Lue5dz_Y_qPBpqjdUUH6avLyhogwB-RluZ5CCAyvRPbIVoVMq8VFp4IW4kA61Sxbpnr93VHVb91FbdH1THioD5Fn_--NP_o6XSb5yw125oHLj0lhWVM6uNOrXneQfT5vy5nJ3MPMsJiixF84N_R3sR97N0j-ddRyQIrzn858zm67vWjJ5pu2j7JFT5Ukm0eaNi3w6c4HoH03IUNcX6eLQAkqYDrBhdSio6ZqvsgD5IEwGdP-8iIqigmGRNuA7mqsdGFfzJ0DzjvrqCKApHM44HSpxJfD1FWjjnwOgSj56CS0QPNWucUyV10qOScDFAG9237fqwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66e469197b.mp4?token=kaElJlbFM-jdyo4Lue5dz_Y_qPBpqjdUUH6avLyhogwB-RluZ5CCAyvRPbIVoVMq8VFp4IW4kA61Sxbpnr93VHVb91FbdH1THioD5Fn_--NP_o6XSb5yw125oHLj0lhWVM6uNOrXneQfT5vy5nJ3MPMsJiixF84N_R3sR97N0j-ddRyQIrzn858zm67vWjJ5pu2j7JFT5Ukm0eaNi3w6c4HoH03IUNcX6eLQAkqYDrBhdSio6ZqvsgD5IEwGdP-8iIqigmGRNuA7mqsdGFfzJ0DzjvrqCKApHM44HSpxJfD1FWjjnwOgSj56CS0QPNWucUyV10qOScDFAG9237fqwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
واکنش کورتوا به انتقال رودری به بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/104619" target="_blank">📅 09:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104618">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/431f50241e.mp4?token=gYz-SKpzH1DqxW4u0H6ax07UJ38wiAIUW7zSizkTtgTAPwjiRyZ2MxcBcuRMhabe5MesWSNg9LWI7Z0Q97t3oLV6CmvlIK0s0ecdNuocUqp_ZJgHj6tTEmVJichj4D9S1VtpODI6fHIKjMZ4kHtfd1OetRx6_LRDLUgFu1qMmRwYONSS85a68j7AynOYvbS4rF8sxBor-B7Ro4nhg81rhPqmrrVWvUxY8ZhhKkTUEMkTR-WbFOtbbDU5Hc1u3STx6s5uhXMo-weOECq-5va8p6Ln0Bwmmo1NjXkfTxFy3TfxaGwqN96LmUaiMWdbhc6VBfWPDGZyfqwhmI4BUqYRiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/431f50241e.mp4?token=gYz-SKpzH1DqxW4u0H6ax07UJ38wiAIUW7zSizkTtgTAPwjiRyZ2MxcBcuRMhabe5MesWSNg9LWI7Z0Q97t3oLV6CmvlIK0s0ecdNuocUqp_ZJgHj6tTEmVJichj4D9S1VtpODI6fHIKjMZ4kHtfd1OetRx6_LRDLUgFu1qMmRwYONSS85a68j7AynOYvbS4rF8sxBor-B7Ro4nhg81rhPqmrrVWvUxY8ZhhKkTUEMkTR-WbFOtbbDU5Hc1u3STx6s5uhXMo-weOECq-5va8p6Ln0Bwmmo1NjXkfTxFy3TfxaGwqN96LmUaiMWdbhc6VBfWPDGZyfqwhmI4BUqYRiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
▶️
آهنگ‌ خاطره‌انگیز جناب سندی به نام "حلیمه" که این‌روزها مجددا بین مردم جنوب کشور حسابی وایرال شده. به امید سرافرازی میهن بزرگ ایران و ریشه‌کن شدن تمامی ظالمان...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/104618" target="_blank">📅 02:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104617">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8e39602d0.mp4?token=VJFKl82nGfVqbOgiaxDmlmEujGb34XTeQY6OIf9gbvEdzSU_ZKnrFpjxwLtyhNvacBt0Y9yneVjPcDmAQLkCnhhGK_MPrNuqPCchx590HEIRFkOVXa8nGWvyr8WoSGfEd6LktiJy9E-49z2xBd1qViKlW6PAQ_dwEEnEuMugP7EJB9PGZB_XJer50shdPErOy-uJRMLUu3-SBSau6AStkaLhofN__FcD813dX_CxDhWitWWm76XhTQkz17AvWuO6M_3_kBz8q-Z--atSmjOohhSyO1d8wIL8x30i_sK0033SsOy2zwqSdQT7rYzPc761anJUfd812ZybhWx0IINkpYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8e39602d0.mp4?token=VJFKl82nGfVqbOgiaxDmlmEujGb34XTeQY6OIf9gbvEdzSU_ZKnrFpjxwLtyhNvacBt0Y9yneVjPcDmAQLkCnhhGK_MPrNuqPCchx590HEIRFkOVXa8nGWvyr8WoSGfEd6LktiJy9E-49z2xBd1qViKlW6PAQ_dwEEnEuMugP7EJB9PGZB_XJer50shdPErOy-uJRMLUu3-SBSau6AStkaLhofN__FcD813dX_CxDhWitWWm76XhTQkz17AvWuO6M_3_kBz8q-Z--atSmjOohhSyO1d8wIL8x30i_sK0033SsOy2zwqSdQT7rYzPc761anJUfd812ZybhWx0IINkpYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
سخنگوی سازمان‌لیگ: بحث قهرمانی فصل‌گذشته استقلال هنوز مطرح نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/104617" target="_blank">📅 01:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104616">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc8c7133cd.mp4?token=hW-nD3LRgx3skabaslsFPVf-aPfQAnaNPefR-TfJM8JkVGLStJcIrMEb0q5yl0WsG-NOEQ2lqizuiqTzxcD1CBtACOGkcQhpizGw-NMGEQY9nGqZj0NdNkkbSP7Lx23kBuR-LfTZr_VI66McSbECDWLHKXMMY20_2rsgp8QXZelxB4W_ZSz0bVjm9DCp_omsia5aC4OUp93Ff6A-S0mraokUAdSo2XfExwrN-bWw5oO8HtqN0yoOgLskvS2CyNdJGl9uWf_41PCUkmIZHuQzhAdx-2Lag_hKYw_ScnjafayZDlIQb9xjBqV0ZzQbZVwoHbvcViLnt-rtBMtY48NeVoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc8c7133cd.mp4?token=hW-nD3LRgx3skabaslsFPVf-aPfQAnaNPefR-TfJM8JkVGLStJcIrMEb0q5yl0WsG-NOEQ2lqizuiqTzxcD1CBtACOGkcQhpizGw-NMGEQY9nGqZj0NdNkkbSP7Lx23kBuR-LfTZr_VI66McSbECDWLHKXMMY20_2rsgp8QXZelxB4W_ZSz0bVjm9DCp_omsia5aC4OUp93Ff6A-S0mraokUAdSo2XfExwrN-bWw5oO8HtqN0yoOgLskvS2CyNdJGl9uWf_41PCUkmIZHuQzhAdx-2Lag_hKYw_ScnjafayZDlIQb9xjBqV0ZzQbZVwoHbvcViLnt-rtBMtY48NeVoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
از حواشی بازی استقلال و سپاهان که حسینی حاضر به خوش‌وبش با روزبه‌چشمی نشد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/104616" target="_blank">📅 00:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104615">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGCO1S6wOPev_MbUuzbO3nNFGG-6mATYWGlpotuDxpwjAahHU6XlKXZfNdCh7jGdyvUf7Rtg8-GI_IsVyJTxbCShyLZEzchpdnCWXDwo7Me-UViqkW9MGXQfN2w2BymZnZYy-VCeTvd2qw_X2yds4S7FH7p2UFBNvTTqsSiGmPF3EeZyAJEy7uyHlTvXxtUfPSxNF4QQ74LuqdRS6Zqtb5mHxAwsO4gfhhsEws4Ig8w8XzC8UKbU7rRQ2bcrrlGGoybFbsa9BHPYKOGoLPPpZqGSBL7FPyRNTCJyIksxaTT0rQQPEUg_VHI3odLWcx_u_B0T77fkJKinEmWOFS4O8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌اول لیگ‌برتر فوتبال انگلیس؛ غرش شیرهای لندن در خارج از خانه؛ جدال سرمربیان فصل‌گذشته رئال‌مادرید به سود ژابی‌آلونسو خاتمه یافت
🏴󠁧󠁢󠁥󠁮󠁧󠁿
چلسی
😆
-
😀
فولام
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/104615" target="_blank">📅 00:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104612">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d62852b4d.mp4?token=Khu8sixfh78AghYvbbHl52jXW6mvkmyJwLvCpxIl1pRkgB7dbr-joHffi4U-lpk4Np6Syzpm2-HDFtHKcEaGtwz_0PSbhzNYuBGe9sxBgIJgBLbTtWOvPIEH-xTtdqN4Zc-FKmsPenpd84ka35P3wtyrqukUWLwC9pF05jdyYnKZjfsdfJIXqfOU0vBsTTYL61na2kzV1e9GRtUwfADRwSFz_u6l8mgR63Xw8OwGh5GtcVNgsQ_QzoSkc35IOPiImPeJ-1OTwElQVeF1aiCzjCZ_ioffvJNDx_mvQohT4myp3xFwHPLmwEqqrnsPY-M9RVM6cChAW9pNWgN2ze39ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d62852b4d.mp4?token=Khu8sixfh78AghYvbbHl52jXW6mvkmyJwLvCpxIl1pRkgB7dbr-joHffi4U-lpk4Np6Syzpm2-HDFtHKcEaGtwz_0PSbhzNYuBGe9sxBgIJgBLbTtWOvPIEH-xTtdqN4Zc-FKmsPenpd84ka35P3wtyrqukUWLwC9pF05jdyYnKZjfsdfJIXqfOU0vBsTTYL61na2kzV1e9GRtUwfADRwSFz_u6l8mgR63Xw8OwGh5GtcVNgsQ_QzoSkc35IOPiImPeJ-1OTwElQVeF1aiCzjCZ_ioffvJNDx_mvQohT4myp3xFwHPLmwEqqrnsPY-M9RVM6cChAW9pNWgN2ze39ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
👤
🇮🇷
#فوووووری
از علوی سخنگوی فدراسیون فوتبال:
🔴
سرباز شدن علیرضا بیرانوند؟ تاریخ بازی کردن بیرانوند تا 31 شهریور در کارتش که در اختیار سازمان لیگ است درج شده است و بعد از آن سرباز خواهد شد اما اگر نامه دیگری بیاید این تاریخ می تواند آپدیت شود و بیرانوند تا جام ملتها می تواند در تراکتور بازی کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/104612" target="_blank">📅 00:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104611">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5U5rD_aalZeJUVFTDVisxs1dNAycfpCAJVBOO15t_-F5uDSF7gKAUyJIMA9dnD-_pSNCwFO2uy1XCU9ja_a9dQQmAXAleBSInvfEfjNU1w00-og83GSzjGiMyWrOTpxbKARygpgMmAb668PcYfFPzl2cEUobXO7gfXeFVjXMTe5oLUFJT1DIca7Ex-tQ6O4cJWRScNUwCZesLfRQZYLCdKeVfotUjVMmHhyZnub02DH2s5ioqWrpSjhrGPXO0ain2UrzG0kgZnAjBgo7gL1961ibsGmqHkQdDso-ogSMiY1vjkKhgXK1woAjyIupUQh30JqahXsvWELBJf4GXebgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
📱
انتقاد شدید جواد کاظمیان به عملکرد تارتار در بازی امشب: کمر پرسپولیس رو شکستی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/104611" target="_blank">📅 00:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104610">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5710ee96dc.mp4?token=ItQYsFL-BdCKod-FZK15udzBr4zhsVlNqw6XtkSm902NspLI-aXY19u9x0PH-HfdHnmiq-NoSZ3Owr1XT8HrLDvcvSdaQQtltlQPCmev4fqoUMw5qFx3rA5NyBi2OYol5-loZKOIKjQQc2F0zNmsDrtwAeVaR3GXwB4amBI2XU8laL5rL9hft9qjBdnFXocXX9SPUh5bd6XF5SUFxcf7r2JjMKsbDFq_zJbQ6uY_XhEYH6SKRfIwFlkCQ1BhsgniG9-htdMx5Yl4dxKFMSGm2u2Bb4QYHH8FDhiKivc_0g4Dcji8jbQMqvWoZZet9V8EFZ2im_EmGxMdhlYtktAYFglHXnBNuY9sqkiKeP1vskr8qQCTvh0-Nka9NF0Kbsd2nRTjBzjRZBnLjtRkcQRL9IyNgbE1x1RNHM68CnpHxUfgthR2D0qj7yVARdmLEfskgGhNli1_p8l1vastdzvbIIHbgNUK7W5ge0IO4I5ByFmsQ_ovsSNmRULzSLn0gFSa2nYd-8NlPItb7b7bgIBk9Hmgc0dcBkuVyfWuoA52HhqbQfV53mSxRcwL92_vSrMgOnySPg5WYu53wQcOYMSKCOTS-CgyadenUqJ0aGS4PA_2WjpqdmxVf_CHcVOYM2Oib47X7IqgnwhSfZLK_EqbOHwzJl4ijBRtyoz7remYKls" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5710ee96dc.mp4?token=ItQYsFL-BdCKod-FZK15udzBr4zhsVlNqw6XtkSm902NspLI-aXY19u9x0PH-HfdHnmiq-NoSZ3Owr1XT8HrLDvcvSdaQQtltlQPCmev4fqoUMw5qFx3rA5NyBi2OYol5-loZKOIKjQQc2F0zNmsDrtwAeVaR3GXwB4amBI2XU8laL5rL9hft9qjBdnFXocXX9SPUh5bd6XF5SUFxcf7r2JjMKsbDFq_zJbQ6uY_XhEYH6SKRfIwFlkCQ1BhsgniG9-htdMx5Yl4dxKFMSGm2u2Bb4QYHH8FDhiKivc_0g4Dcji8jbQMqvWoZZet9V8EFZ2im_EmGxMdhlYtktAYFglHXnBNuY9sqkiKeP1vskr8qQCTvh0-Nka9NF0Kbsd2nRTjBzjRZBnLjtRkcQRL9IyNgbE1x1RNHM68CnpHxUfgthR2D0qj7yVARdmLEfskgGhNli1_p8l1vastdzvbIIHbgNUK7W5ge0IO4I5ByFmsQ_ovsSNmRULzSLn0gFSa2nYd-8NlPItb7b7bgIBk9Hmgc0dcBkuVyfWuoA52HhqbQfV53mSxRcwL92_vSrMgOnySPg5WYu53wQcOYMSKCOTS-CgyadenUqJ0aGS4PA_2WjpqdmxVf_CHcVOYM2Oib47X7IqgnwhSfZLK_EqbOHwzJl4ijBRtyoz7remYKls" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌سوم چلسی به فولام توسط کول‌پالمر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/104610" target="_blank">📅 23:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104609">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f61c2bb38.mp4?token=gYuDWroX3q245HZMg__en58ekYsnkcw1vjEaHyzGukb_k6MrTDgQwa42n-u1QRFo-p2Fc_Bf_yBczoaNGzb97d3vx1rxZDpM3iXZCdr5zyyUB0nsmVvn0PUFSX9GV51KPP-Pk7uE9Kq3j9vPi6cK7TF11qP_mI2KLfrTmKCGTPN6dB1zPdNEv7dzDHc7X898L0EcaPUO1YYymObHixy01pZy9LRQGPzmcRX5mvLmZur1V4QaocuypEiXOhVCaj_JvZ9KNGzcVNYaNVUpO0EusOWfj_se3MxoOd--3xC_SXbVIvs-64Qa7Px82oPgkc6ujoRH2sDHuPAWpUolLJXJ0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f61c2bb38.mp4?token=gYuDWroX3q245HZMg__en58ekYsnkcw1vjEaHyzGukb_k6MrTDgQwa42n-u1QRFo-p2Fc_Bf_yBczoaNGzb97d3vx1rxZDpM3iXZCdr5zyyUB0nsmVvn0PUFSX9GV51KPP-Pk7uE9Kq3j9vPi6cK7TF11qP_mI2KLfrTmKCGTPN6dB1zPdNEv7dzDHc7X898L0EcaPUO1YYymObHixy01pZy9LRQGPzmcRX5mvLmZur1V4QaocuypEiXOhVCaj_JvZ9KNGzcVNYaNVUpO0EusOWfj_se3MxoOd--3xC_SXbVIvs-64Qa7Px82oPgkc6ujoRH2sDHuPAWpUolLJXJ0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
🇮🇷
🇮🇷
استوری طعنه‌آمیز و فوق‌جنجالی علیرضا بیرانوند
پس از برتری در بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/104609" target="_blank">📅 23:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104608">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/19774d8b5c.mp4?token=Ue8wbCYBXeFnsZJcCUWe0hemJLRIZvaQLcZ0LWSIBtTqMuHEFxDKNVJfeREK7H20470dsW8zFtYz4PPhlo9kVh6GQuL0NJzR9kyyKtnf1RJX_O1r2L3TSTdUeV1VPZNWfqYAmmd1Nz_1Wet8Q9KVr-90DTR3dxtpE_TNhSYQ3GB5OBLbYe5KjYXPLvj0Pk1awvoLkY_oAEY0CJbFJyOxPEQE95oMBTqUy1fwHbQeGwzjNWHqASl8Q9Mb2xERcmGorh4q3LRGj4eM675FB-zCSIkOFKLOTiBXa9Tlti2oG1i6n_8ujO_PcHdMmMjcBQnD00s-95fSwkd5ohpVXZmiQgrqF_IveQtKO1GIoeHnfey6GfjqsTphso2AWsm3JkGyVECf1JYUDTJ5MTaBhBFPHfwJx8v4PRHDpYmy3IsQFwqlgWDePasjZNzdGsM22uUkfsvgEuq0j2js5V5MyV4rryZDjklbMG3XiBkRfVaNeW7mWgK5wPBf5SNCxIVDjGrH7OUje5bDRbqwYc5Ua4eOEzrHYQrg3Tl0ar8Xa_iV4t_gyTcIOwCXEzBT_yng5m9QpMoDjhjqnhEf6NObLRAqdO9irgLnERTmBWwKfYLy7AhGQ0UdxNU_VfPuZtullrAG6TXAO_zJQo2MwOGP7B2cFLahSKP1D_D4DqF3dQjcfX0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/19774d8b5c.mp4?token=Ue8wbCYBXeFnsZJcCUWe0hemJLRIZvaQLcZ0LWSIBtTqMuHEFxDKNVJfeREK7H20470dsW8zFtYz4PPhlo9kVh6GQuL0NJzR9kyyKtnf1RJX_O1r2L3TSTdUeV1VPZNWfqYAmmd1Nz_1Wet8Q9KVr-90DTR3dxtpE_TNhSYQ3GB5OBLbYe5KjYXPLvj0Pk1awvoLkY_oAEY0CJbFJyOxPEQE95oMBTqUy1fwHbQeGwzjNWHqASl8Q9Mb2xERcmGorh4q3LRGj4eM675FB-zCSIkOFKLOTiBXa9Tlti2oG1i6n_8ujO_PcHdMmMjcBQnD00s-95fSwkd5ohpVXZmiQgrqF_IveQtKO1GIoeHnfey6GfjqsTphso2AWsm3JkGyVECf1JYUDTJ5MTaBhBFPHfwJx8v4PRHDpYmy3IsQFwqlgWDePasjZNzdGsM22uUkfsvgEuq0j2js5V5MyV4rryZDjklbMG3XiBkRfVaNeW7mWgK5wPBf5SNCxIVDjGrH7OUje5bDRbqwYc5Ua4eOEzrHYQrg3Tl0ar8Xa_iV4t_gyTcIOwCXEzBT_yng5m9QpMoDjhjqnhEf6NObLRAqdO9irgLnERTmBWwKfYLy7AhGQ0UdxNU_VfPuZtullrAG6TXAO_zJQo2MwOGP7B2cFLahSKP1D_D4DqF3dQjcfX0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم چلسی به فولام توسط مورگان راجرز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/104608" target="_blank">📅 23:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104607">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a39f5d717.mp4?token=ScOT2NLrspDLhyCC0IH0Lr5aXZaeK3K2tFV62Qy-P5aot6gXFaBdJUgwKRKl0Fp44R-LVbeaUeguT632-3ljPG8-3iD2g9HMxqwI2Q3xkMHpLG70ZW_R_xhnNd23BPoDiHKEfX4-t7uEa47HncNLcs11s29AqO9aWKh00Y5t9pQSJB5KdIzLds8_4oAmv6OYGl88BvIwvZRL90cG5KUh5Th6C8Iy1Ul_zIxOexEppMukiVWlFaLkSNPRW0VAapOFjZ3ee-v1sMvmbGlmJSbkvyH-RqfLMTsR8956bXje3bOExjk-7g9uJS11EvLW_0oXBEc4I-KvRBJuOXVBQtF0mKGw5SE8AqSiqGc1uDWlwMvGwzxmUm2J7atxEHO16sj1YsenCVSP2msulG8QRcaL8VDM1_Xg3LnHavmiT0ggsbmif4uJn_Kcb37YWJW22pRQPQ0AzZUtEEGXhx3vkKBHkvPMuxUkmKhRbtMib60tAcp8xl9sbb2F4Jx5Ih4wAt4QHqcGHE5L4PUR3xA3BG7hUHTFEMVItc7LPJANrqOBRy-_Vt7haektmsMA5aBBDOpuZB2gWKqPI0eOBY7JoPUgY1eSCLtfKwRYPy9nF3vMZy99YWeOI3uAHebJI6OtpZr7LFs5J-FzUTUf2neN74R8ExhqhTEjs3aF1_t2XWdXZ6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a39f5d717.mp4?token=ScOT2NLrspDLhyCC0IH0Lr5aXZaeK3K2tFV62Qy-P5aot6gXFaBdJUgwKRKl0Fp44R-LVbeaUeguT632-3ljPG8-3iD2g9HMxqwI2Q3xkMHpLG70ZW_R_xhnNd23BPoDiHKEfX4-t7uEa47HncNLcs11s29AqO9aWKh00Y5t9pQSJB5KdIzLds8_4oAmv6OYGl88BvIwvZRL90cG5KUh5Th6C8Iy1Ul_zIxOexEppMukiVWlFaLkSNPRW0VAapOFjZ3ee-v1sMvmbGlmJSbkvyH-RqfLMTsR8956bXje3bOExjk-7g9uJS11EvLW_0oXBEc4I-KvRBJuOXVBQtF0mKGw5SE8AqSiqGc1uDWlwMvGwzxmUm2J7atxEHO16sj1YsenCVSP2msulG8QRcaL8VDM1_Xg3LnHavmiT0ggsbmif4uJn_Kcb37YWJW22pRQPQ0AzZUtEEGXhx3vkKBHkvPMuxUkmKhRbtMib60tAcp8xl9sbb2F4Jx5Ih4wAt4QHqcGHE5L4PUR3xA3BG7hUHTFEMVItc7LPJANrqOBRy-_Vt7haektmsMA5aBBDOpuZB2gWKqPI0eOBY7JoPUgY1eSCLtfKwRYPy9nF3vMZy99YWeOI3uAHebJI6OtpZr7LFs5J-FzUTUf2neN74R8ExhqhTEjs3aF1_t2XWdXZ6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
🇮🇷
❗️
درگیری شدید هواداران در دربی خوزستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/104607" target="_blank">📅 23:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104606">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5e7c831cb3.mp4?token=YZSYe054L888Cn-_KMFE-4q4sFHlfDWMHkBCGzQB5XI69fbJt_VSQ16ojSvfwTVCKD1X6ctpkO1BfzY3qO-CJjsCR9uLAolRa2nqhj36QBAWpFgE9xnVtg5yYIAkDk1p77ZQ7XasY4PH5C5A3YT62N-x3rqkY5qj4cJYCrwYEXOJBOZ0KoIqkRUzjTySKMoFJWrxSK8w3HYlXrMQGlQ35HSh8icj2Q5RGIazdPem3XOf-xiDdLSfgIQXnX8OcGaVglDg0vwqb6eaxIy9YdE3IpBubV2gMWPOGRnbd8X4k_hrtjF8kYfIBD_wveEiKccWTVNFnj11vnT1rpPgAInbfg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5e7c831cb3.mp4?token=YZSYe054L888Cn-_KMFE-4q4sFHlfDWMHkBCGzQB5XI69fbJt_VSQ16ojSvfwTVCKD1X6ctpkO1BfzY3qO-CJjsCR9uLAolRa2nqhj36QBAWpFgE9xnVtg5yYIAkDk1p77ZQ7XasY4PH5C5A3YT62N-x3rqkY5qj4cJYCrwYEXOJBOZ0KoIqkRUzjTySKMoFJWrxSK8w3HYlXrMQGlQ35HSh8icj2Q5RGIazdPem3XOf-xiDdLSfgIQXnX8OcGaVglDg0vwqb6eaxIy9YdE3IpBubV2gMWPOGRnbd8X4k_hrtjF8kYfIBD_wveEiKccWTVNFnj11vnT1rpPgAInbfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول فولام به چلسی توسط جاشوآ کینگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/104606" target="_blank">📅 23:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104605">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/49528cc115.mp4?token=eV07gTCZHjTPipSn3Udck2_HcgMyQKnVbJam3oGCYaSnBzHFB_w61e-a-OcZjUI9OFh5cO3lZliXioKj-R1Gpm8xZbhIQfWRiQd906ErzRcUyBPwCYGXlBr1gJDIgVwwAzOjPf4vAkRMOeWsB4c2ea9_euxmaZNWZK-VoquNGMYSrgjfFemm6p1-nKuPaoKj59NaRgBBzinfUzZD8KGHfRSIIBYFfcNPvpH_ATDLOMbBU61Bbgv5Y_PBmOVrZIb580b_m1_ZQdqHsPI0J6uKXupSBPxEPY_1jcIVG9vsWqpPjWrc0606fhevOPo0i9-ygMJvidurZC_8GWGdMF8xoFqCcVvGRdQaQ6OeczakKbi-KgTWi82Etjf7VHuOeDMKJu_Tkrwd2vq6xSiPDvXOLQr6r4wA33XQGc11tzgxhNYCFfTIyqi5qnYjSTzTp9E8vXiqkQuxIDgPddgOliZ2XQKQeFW2Rfvec8SkGKOzH5iSA_HOtkvL9LpHxYd4Nn8muvwmWhuG15HDZoTsEEkqW-Nry5Ty7me64JVRLTTCM2jPk4CkaayExaxyJk3TsSo4tIjU9Jz1YwHyoDZci0wAq_gni-aPapEOD5vdV7OfJJtQJkqrfHXRaE4720IyV1JK0ABkCtaarobqvPkFnP_hb_VW7upn_qtcdlbNZb8hEpw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/49528cc115.mp4?token=eV07gTCZHjTPipSn3Udck2_HcgMyQKnVbJam3oGCYaSnBzHFB_w61e-a-OcZjUI9OFh5cO3lZliXioKj-R1Gpm8xZbhIQfWRiQd906ErzRcUyBPwCYGXlBr1gJDIgVwwAzOjPf4vAkRMOeWsB4c2ea9_euxmaZNWZK-VoquNGMYSrgjfFemm6p1-nKuPaoKj59NaRgBBzinfUzZD8KGHfRSIIBYFfcNPvpH_ATDLOMbBU61Bbgv5Y_PBmOVrZIb580b_m1_ZQdqHsPI0J6uKXupSBPxEPY_1jcIVG9vsWqpPjWrc0606fhevOPo0i9-ygMJvidurZC_8GWGdMF8xoFqCcVvGRdQaQ6OeczakKbi-KgTWi82Etjf7VHuOeDMKJu_Tkrwd2vq6xSiPDvXOLQr6r4wA33XQGc11tzgxhNYCFfTIyqi5qnYjSTzTp9E8vXiqkQuxIDgPddgOliZ2XQKQeFW2Rfvec8SkGKOzH5iSA_HOtkvL9LpHxYd4Nn8muvwmWhuG15HDZoTsEEkqW-Nry5Ty7me64JVRLTTCM2jPk4CkaayExaxyJk3TsSo4tIjU9Jz1YwHyoDZci0wAq_gni-aPapEOD5vdV7OfJJtQJkqrfHXRaE4720IyV1JK0ABkCtaarobqvPkFnP_hb_VW7upn_qtcdlbNZb8hEpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول چلسی به فولام توسط ژائو پدرو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/104605" target="_blank">📅 22:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104604">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L57WPhhabREphklyFAJgcMdbAwAEvS1aMfhPmyt6AVZj7k3xW_NTlDynkb0vlTr74EEnv7KHgJO-lFrQeob2U9ZZBf5PF667ltHF1I0QuTYrc7v7KFR-a-vPsEP0uSUPeOEEqpdllzkmhEbFF17EaG2BdXOtMeetX_ZlRjr21vqg0FTzH2CwJ1VH3gYh9KhQ-Yq5k7n8Bw9nBhmNFwbd_eO5dSm3x-yP5sfbeoSmjGyXJsn51cu7RlAD5zqVOC9EIOKdrGijyKQ9tRDjIlYNI7zGjDGjGNoTcDnYxStDmpCJanIbJcv6zxMCiufQdnCb4pptkVB6cWIPBXbIiL8WQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
نتایج‌‌بازی‌های این‌هفته لیگ‌برتر فوتبال ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/104604" target="_blank">📅 22:35 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104603">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b217109864.mp4?token=mRb9wTf8xR6TbXQ8rNCWsGPVvX5deU41Y99JQXvNY-j5-m3r6__ZXbvC7rU8PBeygompVN_hkQVIyJp2e1XTt1FfFEer6UZliqDW3Nj-86rd6dIZW4lCOtx8H-CXS76iDCX4KVOR3I_x2kaEcGAMGhhspPIUxH6iqf8sD_8UMCl240PyMIyf94gAChPOhDb2TfpHE33Dsl-WAx-QOLuws-KF7CCIt3UofeBlQNDBED7bA9CYyZqhCEfjA6I0IXRKgy8wo428HE6acc9g9ypD__cgpXenn-2ZfluzsL4uUOPqzsgLHEYD0kwyw_Gs5YnNU_Lb7ntQZV-xTigLTHXYj1170HNS4CNkI0Bqin9q3siAbMrHYuVPN5gMJ9ke9kAhFS9bDkDNjXppF1o9ow863fLdvOpxxFJrkKN0JGwj7BGa7V0X7cmISCaAKnB_Qz7m9lbawL_iA6Vm-EQG6kZYaLLVu74nsyTLK8DjYFvmRUr7O88ta9T7rMD8ulgcd___xs_bPjmOUGR5IILfkEos8OB5B9URghEtnG6P0p1Fq0bu7azhz3j-lFi_xHQYJegCriwxf9GO2MEUUrT7jP7vGkw5-8SIX6UHuvSblDA3zx0eOKz5PCbSWYR6IaqO6ipRClWQDPffOeOWX1tSVG2HNad97BJNQzMCB2iG1oajIXM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b217109864.mp4?token=mRb9wTf8xR6TbXQ8rNCWsGPVvX5deU41Y99JQXvNY-j5-m3r6__ZXbvC7rU8PBeygompVN_hkQVIyJp2e1XTt1FfFEer6UZliqDW3Nj-86rd6dIZW4lCOtx8H-CXS76iDCX4KVOR3I_x2kaEcGAMGhhspPIUxH6iqf8sD_8UMCl240PyMIyf94gAChPOhDb2TfpHE33Dsl-WAx-QOLuws-KF7CCIt3UofeBlQNDBED7bA9CYyZqhCEfjA6I0IXRKgy8wo428HE6acc9g9ypD__cgpXenn-2ZfluzsL4uUOPqzsgLHEYD0kwyw_Gs5YnNU_Lb7ntQZV-xTigLTHXYj1170HNS4CNkI0Bqin9q3siAbMrHYuVPN5gMJ9ke9kAhFS9bDkDNjXppF1o9ow863fLdvOpxxFJrkKN0JGwj7BGa7V0X7cmISCaAKnB_Qz7m9lbawL_iA6Vm-EQG6kZYaLLVu74nsyTLK8DjYFvmRUr7O88ta9T7rMD8ulgcd___xs_bPjmOUGR5IILfkEos8OB5B9URghEtnG6P0p1Fq0bu7azhz3j-lFi_xHQYJegCriwxf9GO2MEUUrT7jP7vGkw5-8SIX6UHuvSblDA3zx0eOKz5PCbSWYR6IaqO6ipRClWQDPffOeOWX1tSVG2HNad97BJNQzMCB2iG1oajIXM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
‼️
مهدی ترابی: قهرمان آخرین دوره لیگ برتر ما
هستیم؛ حق تراکتور کسب سه امتیاز بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/104603" target="_blank">📅 22:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104602">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pibfcs0bzbImMN1zu-mT9UaCrhkS5SJnd3PZXkDghpPjvBQmJhdQweyKddPgV8kXuqDos0DpYFlcqj6mUK_TyjEz_lJ_2rS3x3woW6IJw2MHZAbn0LiyNBR6Or_uvFm4PeOtvbsyT9feabUteyu4r-sdCypeQQH8XZJm2f7mDrqvPhZeL1--IDA14jmSo9pwjFReCZ947gIAex8njINHg0jh5R6R66G6SOvt1A50zwD5mU87ilPM9fAzwouY6zrPk8ah_K9p4vBiL7_xYLEcJYEeDy9GeYTcAsE6xrDlaxUP1bD_SV7zrHYMMcY3y2MEVZuPVAKxwRrygzQPd1Z3_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
کری‌خوانی صفحه تراکتور برای پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/104602" target="_blank">📅 21:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104601">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/723487d9b9.mp4?token=oCKPa-wqjUWXMAxcaDG_yUNx_QOFDzJyq-l9a6hsoglQejWgXVfQegSm2r8Q1k3jrq95Rf7xWit2o5hTY03MWuKAhj_jC1qXHJD6AgwH7gTKFZWV4jOFdsch2uAOsBPmqNziJecIDgUaDUe0k4l3gR6X0T7YGDlkB4ZFxk6RFP73F0ZdlbGlssyYT_vugb1_qxZhyMevwk3eO-Qtx7jRi6_-AHYbzB8al9qIIhfoHkU7yOHXhbd-R4OVUq2pT4S5GUrC4Xgzh2zwlaw2Y0CZOPTaRncI4ZZjZ-f6LPvagMvoa-r06mHItKgJ4JnxSsrUC6OT8_frPFPV_lm9A9rZDYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/723487d9b9.mp4?token=oCKPa-wqjUWXMAxcaDG_yUNx_QOFDzJyq-l9a6hsoglQejWgXVfQegSm2r8Q1k3jrq95Rf7xWit2o5hTY03MWuKAhj_jC1qXHJD6AgwH7gTKFZWV4jOFdsch2uAOsBPmqNziJecIDgUaDUe0k4l3gR6X0T7YGDlkB4ZFxk6RFP73F0ZdlbGlssyYT_vugb1_qxZhyMevwk3eO-Qtx7jRi6_-AHYbzB8al9qIIhfoHkU7yOHXhbd-R4OVUq2pT4S5GUrC4Xgzh2zwlaw2Y0CZOPTaRncI4ZZjZ-f6LPvagMvoa-r06mHItKgJ4JnxSsrUC6OT8_frPFPV_lm9A9rZDYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
پاس گل رامین‌رضاییان در بازی امشب فولاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/104601" target="_blank">📅 21:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104600">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f291196ab1.mp4?token=QeWDY1aBc5_lVH1bfOaGesyuAnBrjA0_O4jJgwRpqFwG3hOTjFBNB_jiUwnGKCasINc6k0KYDaU8F1kiA71UMAjQisGV28ls-iTqh2Zd0Tw_X204yT5Jaz8ErkBE9Zy-3ORXsPK9LHodQzrATmrFg7RTO80LSQYrDsv5ax-0L6e9iP1mw63TC5cHwdQRLaAFUJc6giaXd1iIErPx-iKoBXcYI2hzMhzFPdSVBXuy_7Ip63QZxciykvPW7uJxZ1JwNDDxCsPtrpemiu1Fp3suBMGyNIyXF5PNpJksXPxTgMsya90t7VBFs2DM237sP76DtSOxXvkzio0S1YSqBrUTpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f291196ab1.mp4?token=QeWDY1aBc5_lVH1bfOaGesyuAnBrjA0_O4jJgwRpqFwG3hOTjFBNB_jiUwnGKCasINc6k0KYDaU8F1kiA71UMAjQisGV28ls-iTqh2Zd0Tw_X204yT5Jaz8ErkBE9Zy-3ORXsPK9LHodQzrATmrFg7RTO80LSQYrDsv5ax-0L6e9iP1mw63TC5cHwdQRLaAFUJc6giaXd1iIErPx-iKoBXcYI2hzMhzFPdSVBXuy_7Ip63QZxciykvPW7uJxZ1JwNDDxCsPtrpemiu1Fp3suBMGyNIyXF5PNpJksXPxTgMsya90t7VBFs2DM237sP76DtSOxXvkzio0S1YSqBrUTpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❤️
خداداد عزیزی: بیرانوند از مهرماه سرباز است؟ قسم می خورم خبر ندارم/ ما علی بیرو را خواهیم داشت به امید خدا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/104600" target="_blank">📅 21:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104599">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEHhBifo0NAXgVnvQg3vYhzS-TK3IJcvUX7pG52OQ4k25DhkHzmn2-l1FlxqVoGgMUG2mjNkQtJSN-JVSZua4ex7HyaPrntboCMi34I52G4la5tdtEMTkfHMvpoNqenKcJ5k-EuEyb0OW6G6i7JAlkz4Uf5kEVcFsOVXq-60Wbh5_xtagx2rbg-FqQi9KFXt3uClIDqJ0M4PKe9BGBVSlRK8ZTPVW5clPUuWdVNJ3CYjoAn109RLzheeplxOt_EnjoTl5DacsQ1slsIKmqm9Zq0qPAUnV6eCL3aEbhIJkMa7aq4nrJBssyVaEE2pD4w5qdmIHxN7CR8iwXbAw91JRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌اول پریمیرلیگ؛ ترکیب چلسی مقابل فولام؛ ساعت ۲۲:۳۰ شبکه‌ورزش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/104599" target="_blank">📅 21:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104598">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1eaa4d7c9.mp4?token=YGWv17qz2r-FXldF4nOX32IomTQHYQIRHx0xjcXV9mhafWLFwXv3Bt1rNskgrTmqC-ltkHuco2A0-NtVrQInFaxX2mZH-kkHR2dTQH1VAwN76f55gloGOoBgWfWpJyPLKLDEiIqJkA4MzS2vaby5SYjXDd64LjM_n-8MktOOmHu5lR1X61y7d9BmJuhz9eOmfKvN4Pi2CzOJzVzodBEB0xmMyHuY8E0r8HPCWxbPnHATwGU_kfeTlI11kI4F_ZSuSL_Ucif4-Zkhfo_jfHPFQwyDwMb3Y1fL0g6lSZ4oR1yIyypZpNMcor4jTNr6FQSCfDlN4H1KEFJPzRAj2xKh_kvu0dyp-xO1oC-F4migQu332t9S9rfM7UtBG_8D4pMwv1RrMSLglOlmD5SusHhCn2J-8gEHbt6u8cPesEfMpdAFp5-JlZSnAWMI_Ny8CE1U3sk1AgrFhlSujnCiVDB__lw62jSkJEAKcPe4tGde772VUM-UUtoK1P1BEQoeKGnN7rZPrbqdbjw-ZJSNcqFCr79ORbX9tpldaVg9UvY9wcV98RFvZQ1uF5N4kJ-U_ahKBWm9_rooaYVfu7tpZ6uylAnUjFO3ic9TCjPErL_A1VhVE8sS13Yw2wXKwwrwAAlHZIjQal09dlS6u5I44eOU-x9Cu5maNvU-cZ7-EDU6ce0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1eaa4d7c9.mp4?token=YGWv17qz2r-FXldF4nOX32IomTQHYQIRHx0xjcXV9mhafWLFwXv3Bt1rNskgrTmqC-ltkHuco2A0-NtVrQInFaxX2mZH-kkHR2dTQH1VAwN76f55gloGOoBgWfWpJyPLKLDEiIqJkA4MzS2vaby5SYjXDd64LjM_n-8MktOOmHu5lR1X61y7d9BmJuhz9eOmfKvN4Pi2CzOJzVzodBEB0xmMyHuY8E0r8HPCWxbPnHATwGU_kfeTlI11kI4F_ZSuSL_Ucif4-Zkhfo_jfHPFQwyDwMb3Y1fL0g6lSZ4oR1yIyypZpNMcor4jTNr6FQSCfDlN4H1KEFJPzRAj2xKh_kvu0dyp-xO1oC-F4migQu332t9S9rfM7UtBG_8D4pMwv1RrMSLglOlmD5SusHhCn2J-8gEHbt6u8cPesEfMpdAFp5-JlZSnAWMI_Ny8CE1U3sk1AgrFhlSujnCiVDB__lw62jSkJEAKcPe4tGde772VUM-UUtoK1P1BEQoeKGnN7rZPrbqdbjw-ZJSNcqFCr79ORbX9tpldaVg9UvY9wcV98RFvZQ1uF5N4kJ-U_ahKBWm9_rooaYVfu7tpZ6uylAnUjFO3ic9TCjPErL_A1VhVE8sS13Yw2wXKwwrwAAlHZIjQal09dlS6u5I44eOU-x9Cu5maNvU-cZ7-EDU6ce0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
تارتار سرمربی پرسپولیس:
دلیل بازی نکردن ارونوف و سرگیف؟ این به کادر فنی مربوط است و دلایل فنی داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/104598" target="_blank">📅 21:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104597">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c69ee8ec9.mp4?token=BO2PkvTN6_smvbbL655Pac3Po4SXjYmf1_7pYtnS6VGOlE3lUT5XZjGOVVopB5PnqbhBwXiQ1HuBPv8vp-jg5U3du1GirBTfwENywZgrQjxpEAmTswrMRmvYnFdwMDGQdWFxHZP74vwK9qkzKdwHwObsj1DCiOrjoror6wzWJChQ5ofa6dnduIOsDsdwm41lbs-wZARY_g7JNdN3SxL7P7yi0kOGQe9CGFe06MBrLNDJ9tvURnB8a0e3W6I_1RJGXoII7jvW_xRdS8oVq-NNkTMTK22Wc-MaVkIX8X3FNUEwcmtW2dDxFyZwgNQx_pBmW5FDE4D-uNeGyVthKDyBBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c69ee8ec9.mp4?token=BO2PkvTN6_smvbbL655Pac3Po4SXjYmf1_7pYtnS6VGOlE3lUT5XZjGOVVopB5PnqbhBwXiQ1HuBPv8vp-jg5U3du1GirBTfwENywZgrQjxpEAmTswrMRmvYnFdwMDGQdWFxHZP74vwK9qkzKdwHwObsj1DCiOrjoror6wzWJChQ5ofa6dnduIOsDsdwm41lbs-wZARY_g7JNdN3SxL7P7yi0kOGQe9CGFe06MBrLNDJ9tvURnB8a0e3W6I_1RJGXoII7jvW_xRdS8oVq-NNkTMTK22Wc-MaVkIX8X3FNUEwcmtW2dDxFyZwgNQx_pBmW5FDE4D-uNeGyVthKDyBBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
❤️
تارتار: به خاطر شکست امروز از هواداران عذرخواهی می کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/104597" target="_blank">📅 21:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104596">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbcc283cc3.mp4?token=k3bx0l-cURdssUkR9KgsKYArcjOd0VnLjhJjWHql5T8-xX8HVq-yq2YqMMa_Zdtd0GnDxVvChkD_829dknZfx0g2G9UBBUtgzQRsnyz5ZdOCrmA70z33Z9LkgNQJb6WtdargfxAGnvp4h6sOUfB-tVfkGZ0RBK9lvCIRzDDtZ3qwxb5B1TZgr5W4nNUHtzYMu1J8DwXi127j7GEvF7scufN3f8JskN4RlTc6xs7w_pUFrnPL-yRmypwSYdE_tXhtblRkzip0U0pKbbKmXt4zrn0aPMQzaJWiKETDMiB2_1_bqmyATqI2XCl6abky3UwgKn85K_Jopj2u36Dftj8yXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbcc283cc3.mp4?token=k3bx0l-cURdssUkR9KgsKYArcjOd0VnLjhJjWHql5T8-xX8HVq-yq2YqMMa_Zdtd0GnDxVvChkD_829dknZfx0g2G9UBBUtgzQRsnyz5ZdOCrmA70z33Z9LkgNQJb6WtdargfxAGnvp4h6sOUfB-tVfkGZ0RBK9lvCIRzDDtZ3qwxb5B1TZgr5W4nNUHtzYMu1J8DwXi127j7GEvF7scufN3f8JskN4RlTc6xs7w_pUFrnPL-yRmypwSYdE_tXhtblRkzip0U0pKbbKmXt4zrn0aPMQzaJWiKETDMiB2_1_bqmyATqI2XCl6abky3UwgKn85K_Jopj2u36Dftj8yXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
اسکات بِسِنت وزیر خزانه داری آمریکا:
🔴
«می‌خواهیم امروز به‌روشنی اعلام کنیم که هیچ‌کس خارج از دسترس تحریم‌های آمریکا نیست.
🔴
اگر کسی معاملات ایران را تسهیل کند و بخشی از شبکه‌ای باشد که نفت ایران را به پول و سپس ابزاری برای سرکوب تبدیل می‌کند، هدف تحریم‌ها قرار خواهد گرفت.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/104596" target="_blank">📅 20:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104595">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d42d6444d6.mp4?token=owV_S0gpMOzREruoQ5zjZByTci-oF74BAZP5XAPFDR-PLUsR-5jbtssf0AJdTAnzBBnZNUS70m9Ox9b3aZdmYLN7Fvx0ZuZ_EP8iBYdlS8QST3BtcquFoQkBvbC4_rCrJsSCbUYJq0lI1hyJLqHNDzN1dpkW8RdmIXxoI6c590xWNQVYvaCJKk0tPkwEutuZoflcOQe4HEkrYA3NZ6-nrKqnA5RawIBv9eYHYxgAyXuaB01vfkaM0c9_I9TtyRPvJbGurx3_maOT7Yi9ORHlXiAsLsyRBJ3R6llnrDrpTMZS49cKQm6cwFRmikoS7rNuzBP3Ew5OnDajiPzol2gm5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d42d6444d6.mp4?token=owV_S0gpMOzREruoQ5zjZByTci-oF74BAZP5XAPFDR-PLUsR-5jbtssf0AJdTAnzBBnZNUS70m9Ox9b3aZdmYLN7Fvx0ZuZ_EP8iBYdlS8QST3BtcquFoQkBvbC4_rCrJsSCbUYJq0lI1hyJLqHNDzN1dpkW8RdmIXxoI6c590xWNQVYvaCJKk0tPkwEutuZoflcOQe4HEkrYA3NZ6-nrKqnA5RawIBv9eYHYxgAyXuaB01vfkaM0c9_I9TtyRPvJbGurx3_maOT7Yi9ORHlXiAsLsyRBJ3R6llnrDrpTMZS49cKQm6cwFRmikoS7rNuzBP3Ew5OnDajiPzol2gm5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
اسکات بِسِنت وزیر خزانه‌داری آمریکا:
🔴
«خطاب به سربازان عادی که از این حکومت حمایت می‌کنند:
🔴
وقتی پرداخت حقوق‌تان یکی پس از دیگری متوقف می‌شود یا به‌ظاهر فقط به تأخیر می‌افتد، از خود بپرسید آیا فرماندهان‌تان کشور را به سوی پیروزی می‌برند یا ویرانی.
🔴
به یاد داشته باشید که دیوار برلین زمانی فرو ریخت که سربازان عادی تصمیم گرفتند به مردم خود شلیک نکنند.
🔴
و خطاب به کسانی که به تهران کمک کرده‌اند: هزینه آزمودن عزم واشنگتن را دست‌کم نگیرید.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/104595" target="_blank">📅 20:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104594">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b198e5e16.mp4?token=Ug5F7RKCypieF1mU53nQ2rDwDGuoy15wdy3fVtnwKR1dIpj6OWOpfcosUTbgtYigdwpfvK4BeJJUEvgkaaOFFbXyvfJyeYaaHkeYRMqMIoMzJ6bXPsOpa4d5WNUQ-o0_q31RMXiyZF0XIyrTETBfRc4JpWSrjyxjuT-7KN-FY4EFuoXmlJkBGMdM_1jYDrpfgKD0j2_sMJrRc0nf5D2hsgiOcbAEHytvXytZ40K50uMDmgXh6NsakuvUkHoOiOhwqbAo92e9QKknWyGgpg_jqVWpxUsFK_YuFjgxmFLJnZmmxpwcfqLn6LHbYxl0L4LWch71X3qmn91EdQbuQECIEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b198e5e16.mp4?token=Ug5F7RKCypieF1mU53nQ2rDwDGuoy15wdy3fVtnwKR1dIpj6OWOpfcosUTbgtYigdwpfvK4BeJJUEvgkaaOFFbXyvfJyeYaaHkeYRMqMIoMzJ6bXPsOpa4d5WNUQ-o0_q31RMXiyZF0XIyrTETBfRc4JpWSrjyxjuT-7KN-FY4EFuoXmlJkBGMdM_1jYDrpfgKD0j2_sMJrRc0nf5D2hsgiOcbAEHytvXytZ40K50uMDmgXh6NsakuvUkHoOiOhwqbAo92e9QKknWyGgpg_jqVWpxUsFK_YuFjgxmFLJnZmmxpwcfqLn6LHbYxl0L4LWch71X3qmn91EdQbuQECIEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🇮🇷
گل‌تماشایی گل‌گهر در بازی با چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/104594" target="_blank">📅 20:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104593">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHfNPuvsBZcuN7NAmOSfh3HSz3aZjeg1S2SAWWNujUp5eWEQ-ZDW6T2xPYxRbyAbnWRGvo0YtvFFuZH1XUpc5A2jjiU1lRTIfz3mteyOwX5qmy-ijd9OtHh20Y_erjMTgGQCBsnwdaG0hdoGVOnIZ1zb93tAzrFs5QpT7fQnynass8Go-XWYUOPpXUjGD25qKahopUV8kuflFC8sKfA1fEN_TG_liFYVZ50hUFNuzr-J1cOeL1afym4wYXfQ9P9jbA_MkEM79A2Ec41p_F5einY9tFRbFcAyxn8FmYD9UxxdI4bItTdOuA5QDVKcv6iqfVHbpmI4ReQR5J91w0GwWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
توییت کنایه‌آمیز استقلال بعد از باخت امشب تیم‌فوتبال پرسپولیس در تبریز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/104593" target="_blank">📅 20:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104592">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c54496137.mp4?token=tBm0Jq2YyWsEqm4W4WeBMu2CG71T0CZdeMaU-egAXnEw7S_6_G7HzTiTjG_ibzvSKktK1LvWu0xQtgbClNAof-CuPQvfk7ck2opl5tQu6CTGDa5KC2e53JwumWayugyrtrvB11hKPf9l_vu5R5O2R_QPN2185uhgW0BkbMH9e1WCNh1aZLP9cpyh3QNpxgPDK_hED4DcSved2MvBW8_udj7G73rJEIIWw1f1ZEtf38sV-bBSJ1Rm_bfJjr_Wo8osU5Suvh98Yc63-YwXEY-IriPHoxdZZOxT9skMkOkx1HoxysR47_Qy0KXMYy2ZdZmVgYDyryBgkPqq7It7cpMomQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c54496137.mp4?token=tBm0Jq2YyWsEqm4W4WeBMu2CG71T0CZdeMaU-egAXnEw7S_6_G7HzTiTjG_ibzvSKktK1LvWu0xQtgbClNAof-CuPQvfk7ck2opl5tQu6CTGDa5KC2e53JwumWayugyrtrvB11hKPf9l_vu5R5O2R_QPN2185uhgW0BkbMH9e1WCNh1aZLP9cpyh3QNpxgPDK_hED4DcSved2MvBW8_udj7G73rJEIIWw1f1ZEtf38sV-bBSJ1Rm_bfJjr_Wo8osU5Suvh98Yc63-YwXEY-IriPHoxdZZOxT9skMkOkx1HoxysR47_Qy0KXMYy2ZdZmVgYDyryBgkPqq7It7cpMomQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🤯
🤯
سوپرگل‌بخودی پشم‌ریزون ذوب‌آهن در بازی امشب مقابل ذوب‌آهن اصفهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/104592" target="_blank">📅 20:46 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104591">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGuGouSte89HDzKviMeWGsUuyU5aQWXofpogZCKAbiv1SmhirzZ4fZdhg8JVTrNQp-Azx5o-hpaQBkgzps_xOpTwFiNtFI7Mp3OLRqttXlcMU5qHJ7PIlQYm6HesCLiuRD3owZTMbDMpCzdtcxTje3xfLpsw4IhwASd87VKLKI9r_ThUKVGscqqQWPXh4SL-_gjEzkBbykSg3ZumTW5tcnjepf3c4I7XKhTo1m5O20sen7hRfG9qN5Ptu3Xcdni4Vs-jDyfn_ZOsWeB1eFWqV7U-2UNXGtYdYVZ5ZL7Azldt1bbsDy1w9KuWwNaoeV5ToNerH7IpuHKALmRYjy34Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✅
🇮🇷
هفته‌سوم لیگ‌برتر فوتبال ایران؛ نکونام با سبک خاص خودش در تبریز برنده شد؛ تارتار و ستاره‌هایش در اولین محک جدی با یک تیم نامدار ناکام ماندند!
🇮🇷
پرسپولیس
😏
-
😃
تراکتور
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/104591" target="_blank">📅 20:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104590">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4XpVimprpN5rzr20g0pM78zRsqTW0jrDBujYJCFCyvjUAPm3zHfcVs5N-YTpipWkV2IK98F3PzCM8yV345v9BpJlnw7rBFDzeGyzffFyM2aebqPPfPolIkl9eATdyiP7IsakAP5W-UiVaTn7DqFQBqjlTM-5B9uAL0Up8Po-_aQZe26xBMDug_XMeEN5lExn_-h7ilKf1rX6by8nY7mqQOmeZsDJ_f0QO1Jzha6ny3ymUY7YopG0pjj0rg0eaxeCjy_Xna4vZbI_kwdyvEiyqilm9ePkUPlAuSl-ospEMfIDEg8SNqeeX9WG8-sGXZTmMl5fjtcsofIX6TW0CI2fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✅
🇮🇷
هفته‌سوم لیگ‌برتر فوتبال ایران؛ نکونام با سبک خاص خودش در تبریز برنده شد؛ تارتار و ستاره‌هایش در اولین محک جدی با یک تیم نامدار ناکام ماندند!
🇮🇷
پرسپولیس
😏
-
😃
تراکتور
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/104590" target="_blank">📅 20:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104589">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
گل اول تراکتور به پرسپولیس توسط اشترکالی روی اشتباه دانیال ایری(89)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/104589" target="_blank">📅 20:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104588">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1adda802a.mp4?token=tfnA79oAT2sQrteGGjfm9-HoMTG5qWx0cA2iIRXqlPBtyaiqHJAvuEpLF-dQQ2uVGvZ5tsI9ve0ZCmQMciAH_J4l6AKjwVvvBcRwtZXJc4DQcv90uUtLTK-WYpEKKd2kOLalhPRGhGAksjazVkJGGlw2H7mAVzgklsK6KRAO4245osidw3Z_quPV2i_yaIXBSa_96NvNAYi7DWeNMCrRsyyHz5kItM9pxUIxNLHA9P6U9JVkwnDPS4tF0vGLb6cAipl_x9FcLLoJ5sGE96IYLEUfNdGiBmOlAESRKjB3yARq6znier8UpwdyBe8KtLt_LELMeK8VoTCm2cLHiUYhyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1adda802a.mp4?token=tfnA79oAT2sQrteGGjfm9-HoMTG5qWx0cA2iIRXqlPBtyaiqHJAvuEpLF-dQQ2uVGvZ5tsI9ve0ZCmQMciAH_J4l6AKjwVvvBcRwtZXJc4DQcv90uUtLTK-WYpEKKd2kOLalhPRGhGAksjazVkJGGlw2H7mAVzgklsK6KRAO4245osidw3Z_quPV2i_yaIXBSa_96NvNAYi7DWeNMCrRsyyHz5kItM9pxUIxNLHA9P6U9JVkwnDPS4tF0vGLb6cAipl_x9FcLLoJ5sGE96IYLEUfNdGiBmOlAESRKjB3yARq6znier8UpwdyBe8KtLt_LELMeK8VoTCm2cLHiUYhyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
گل اول تراکتور به پرسپولیس توسط اشترکالی روی اشتباه دانیال ایری(89)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/104588" target="_blank">📅 20:27 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104587">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تراکتور زدددد</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/104587" target="_blank">📅 20:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104586">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گلگلگلگلگلگگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/104586" target="_blank">📅 20:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104585">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmCiYD0qswjT8ANTs5PgDGxP8ZMf_Ibkcs54AqZW77C8U8IkPs24qgPhVWFBZb30_8vqo8mL5GFGgUL_iiUtRqwUkx3QK_8RnBDm2qgGKPZSKZTT8NLgULxahGi9sT521NHp3GDkyrfm-FBCkHb9LUy3qrVpOZnQgt8hkc06DCZbnljNMdhEnXyymLhd3gU7aPJkMyShBQP76xOmhealm4XBcjG82CTnFrqM7vQA27BE_MaJdWFRZrf8fHbI8vp4BP9oAGiKBkaOAAxNMzV8FWPvujSsTvwXxVY5bpzhvw2_mTfInkDMi8FsE0SCyu2K611nsUhXHSkgUQhq0kp6Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از رومانو: کودی‌گاکپو ستاره هلندی لیورپول در تیررس منچسترسیتی قرار گرفته و مذاکرات جدی در حال انجامه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/104585" target="_blank">📅 20:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104584">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">حداقل تماشاگرا راه میدادن بازی جذاب میشد
😐
۷۰ دقیقه کسشر خالص از صداوسیما پخش شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/104584" target="_blank">📅 20:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104583">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇱
بنیامین‌نتانیاهو: در روزهای اخیر ایران تلاش کرد که یکی از اعضای خانواده‌ام را ترور کند که در نهایت ناموفق بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/104583" target="_blank">📅 19:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104582">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cef14eb37a.mp4?token=As8FDrgSjVe8nrYg85pJyKsf-37AntJXP70EoOGy0q6MVYIsRXVlJZ9BNHbrnBBwCDpPTXOBNYWBylmgo0kI7QVqAZU6o6TkrfgEOnO1OhouXg5o4F7Qw95vDI16bP5evtkqll0tfOfppPdTvJdZLlh9tveYboMDLeckuY-2PQaun_sjbIof3sD4PTJ_tSWougKueKH1rqRZwZAzNBKk90_dp_xKZDXBHt1qiiJl0dw3ikdydBGq9MxGb59PL1aEsB1ThOcCjUAbNXn98e3Z3oqKn5g3rL2o17OTofhygIr3G3tGS5TsYXq07WkO_ojzbCJdPWqp-PTWC0duGay9Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cef14eb37a.mp4?token=As8FDrgSjVe8nrYg85pJyKsf-37AntJXP70EoOGy0q6MVYIsRXVlJZ9BNHbrnBBwCDpPTXOBNYWBylmgo0kI7QVqAZU6o6TkrfgEOnO1OhouXg5o4F7Qw95vDI16bP5evtkqll0tfOfppPdTvJdZLlh9tveYboMDLeckuY-2PQaun_sjbIof3sD4PTJ_tSWougKueKH1rqRZwZAzNBKk90_dp_xKZDXBHt1qiiJl0dw3ikdydBGq9MxGb59PL1aEsB1ThOcCjUAbNXn98e3Z3oqKn5g3rL2o17OTofhygIr3G3tGS5TsYXq07WkO_ojzbCJdPWqp-PTWC0duGay9Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
فرصت‌سوزی پشم‌ریزون امیرحسین حسین‌زاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/104582" target="_blank">📅 19:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104581">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f81fa46cd.mp4?token=GoX1EPKmktCZ3ecoMadZmBzj0p_6xvidMRaGx6Oa1fPw65G8H0iGf87khf7hvMTyuX3h3bHHOpVu3_68WZJUFnh264L2wRIhDPTlRHLTDIqgxX-kWs6v-lmC4EGwpDlGOKfb3vE0UEkWAK3TJupjg5dxCk7Hd_q26bOjQ_FyUPK8RDdNq_OmZmkAEmwGvb-09z7fh-FXdK_B5hbqY3jM1_vrrCeL5PZlvSsKxPjnuWwmAISelTC06kM4LwPi26jkdyvN4fW_lurDi4D-O_GE6HLQENfv5wT440eEY8DydRbXNRoIMHptpjz38wMWkhOwnP2f0tEpaRHv7v6eOKlnCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f81fa46cd.mp4?token=GoX1EPKmktCZ3ecoMadZmBzj0p_6xvidMRaGx6Oa1fPw65G8H0iGf87khf7hvMTyuX3h3bHHOpVu3_68WZJUFnh264L2wRIhDPTlRHLTDIqgxX-kWs6v-lmC4EGwpDlGOKfb3vE0UEkWAK3TJupjg5dxCk7Hd_q26bOjQ_FyUPK8RDdNq_OmZmkAEmwGvb-09z7fh-FXdK_B5hbqY3jM1_vrrCeL5PZlvSsKxPjnuWwmAISelTC06kM4LwPi26jkdyvN4fW_lurDi4D-O_GE6HLQENfv5wT440eEY8DydRbXNRoIMHptpjz38wMWkhOwnP2f0tEpaRHv7v6eOKlnCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
فرصت‌سوزی پشم‌ریزون علی‌علیپور
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/104581" target="_blank">📅 19:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104580">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRxH5sCPs7IOnaHQY7um3qsQx865s-6neWy7MEnHc1gLnSnB-gnPxZU8gz0ywmTOf7WonFbF-joH9emk9gu3Z5lqNTAaPKwsrW2oCZsrK2mxpk8i5izCwdLZ8A3uYsgL1Af1b0gRGi2U5IpjAz_tFX3_692qpcMAmui-4GeHtNvDwromHqn_uSmMLZNCcWEhqK7QiTiG2SbvQIeA3Qa7-lNzcABMJejHEz3e6v1guNWKDv3WngQIJM4V5mRHrr-HZbOeyWFYiOcn0xdkeWqwSio499RkjRT7NCHMaRWcwCgBcNCzZRvevQfH9AVGzx8Ep2PTYpIX7pYPx1-wZLcGLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
رامین‌رضاییان در ترکیب فولاد خوزستان مقابل نفت‌آبادان با شماره پیراهن 69
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/104580" target="_blank">📅 19:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104579">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/701c8571d2.mp4?token=szKcEdZXqNol_N4T3AJrttHEmR58dXg86lCdPmHrRcWvWW6-_KI5Euxj5you8zJg5iaNOplBDtHVfb_9rlQruuSM8gELmHDnQfCVx3pynjWyVZtUhGqLaNzXxNGgUW4jnblriDcRhg66x6tgiP_1XiazvGJZIwB5HhDqD0eRAG0CcsW3vOaJyUeTIsNHlVsSpVXuO66hy6-Mtc6b3f-PMMhmUn3TaA1R71_iPfiLLVYgwNWt4c8mnKYMX7JvOq-goMBfua3XJfINAp9xLw6QSD3RXp6Txt5Oh5j89Q4T-Oht8tUqjOM0aFvGrKVXparo4c9d3Ye7CBUE63yoC6U0ygI-QKLDWqN-TTjRMxhpmyOIROnqElM4A3ecpqJbKczrJej11JvjzzGdHCvqLLZRkCFS209vKzPlmaRRs9KvX2GwXyJIxQh2OjTXFHk_c9vC_SU51ymVMu4yDnyuE5tuWR4NmM6G4ZgyXIYXJe4IQEGv0kVTw8Xr_hqmE_kYvZmeEY5oMpPZj_RtGhCXvEgmKEWq_byXgC0ndSDt-m250TKkbSTIYRKDbIHGZHQhVwwx-oI2DGvEDxqDHbH3YO0LJnYujyympyvhfy0x_5qjGcIpARoNKEaQtWOvpb8e_cv1o2G4qxdZ8wR-afoIR-7l1tcj3gghntyb6Aieglmk6vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/701c8571d2.mp4?token=szKcEdZXqNol_N4T3AJrttHEmR58dXg86lCdPmHrRcWvWW6-_KI5Euxj5you8zJg5iaNOplBDtHVfb_9rlQruuSM8gELmHDnQfCVx3pynjWyVZtUhGqLaNzXxNGgUW4jnblriDcRhg66x6tgiP_1XiazvGJZIwB5HhDqD0eRAG0CcsW3vOaJyUeTIsNHlVsSpVXuO66hy6-Mtc6b3f-PMMhmUn3TaA1R71_iPfiLLVYgwNWt4c8mnKYMX7JvOq-goMBfua3XJfINAp9xLw6QSD3RXp6Txt5Oh5j89Q4T-Oht8tUqjOM0aFvGrKVXparo4c9d3Ye7CBUE63yoC6U0ygI-QKLDWqN-TTjRMxhpmyOIROnqElM4A3ecpqJbKczrJej11JvjzzGdHCvqLLZRkCFS209vKzPlmaRRs9KvX2GwXyJIxQh2OjTXFHk_c9vC_SU51ymVMu4yDnyuE5tuWR4NmM6G4ZgyXIYXJe4IQEGv0kVTw8Xr_hqmE_kYvZmeEY5oMpPZj_RtGhCXvEgmKEWq_byXgC0ndSDt-m250TKkbSTIYRKDbIHGZHQhVwwx-oI2DGvEDxqDHbH3YO0LJnYujyympyvhfy0x_5qjGcIpARoNKEaQtWOvpb8e_cv1o2G4qxdZ8wR-afoIR-7l1tcj3gghntyb6Aieglmk6vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😢
🇮🇷
🇮🇷
خلاصه نیمه اول مسابقه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/104579" target="_blank">📅 19:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104578">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07cabf9572.mp4?token=UkFdxISi_9ir6kNvCvNZ4jdWZ6oRRRdaNhIXMY2qz7sx7fbwTig7Obyi3MWdyxtoLjzNVPhxU6XNGf9GshL-e_OmW_JoaC8ZbFYlb4fe7PAf8xI7Yj-Dv5Md60WeWmo9CZZ0DfpIf7rOZkgaIpVPnikl_bzBjHSoIieEniwGWlO4-g59FmT0fYjUiS5kTzdQb0R0900ha5PzZuzKXMiCbr-P4XDJwI5s-i9S8JQzoYKs0GtkcrdHpcHmGn4_xugViKZH4HCtCjfeOv5vpZkDZRWAK2CVruHgEa7qNxyfM_i5OuAP1Qo-Jw_XOXh8S58gTn9PmYZhBLKjGnC8K7_IVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07cabf9572.mp4?token=UkFdxISi_9ir6kNvCvNZ4jdWZ6oRRRdaNhIXMY2qz7sx7fbwTig7Obyi3MWdyxtoLjzNVPhxU6XNGf9GshL-e_OmW_JoaC8ZbFYlb4fe7PAf8xI7Yj-Dv5Md60WeWmo9CZZ0DfpIf7rOZkgaIpVPnikl_bzBjHSoIieEniwGWlO4-g59FmT0fYjUiS5kTzdQb0R0900ha5PzZuzKXMiCbr-P4XDJwI5s-i9S8JQzoYKs0GtkcrdHpcHmGn4_xugViKZH4HCtCjfeOv5vpZkDZRWAK2CVruHgEa7qNxyfM_i5OuAP1Qo-Jw_XOXh8S58gTn9PmYZhBLKjGnC8K7_IVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
مهدی تارتار، سرمربی پرسپولیس پیش از بازی با تراکتور در استادیوم خالی از تماشاگر سهند تبریز، مشغول مترکردن زمین و بررسی چمن استادیوم بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/104578" target="_blank">📅 19:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104577">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QnMrb03g1a2I6BtKLNvk7mfd11sIruLTcvhwpfCL5tsY3dxYild5WR535Y4y9y2TGqvi_UkLtubO96KrBGwc__JwbkoYtFnqyGP3BXrMqwH9D225t6qyDB8ZLl8o6sybRDs5icixKvyRIkrEBOmShZU1YynGIqW70J8fA7KLF5yKk9zbPZIOAdC8W2AkRtJEpjV9AY1ensbIMIbBW6lgTB03_U1paRAPQcz9SMZndBIGp1qQES7Zz17bMcyPG2apZ3ugz-k9gQ4UkJPJ85mEp0d2zKx-606UNr0YKEByWy2CQfKV3S-mjdgJeMVPAeGzTVqExS_4_qCi_Aas-Z7XZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
از ESPN :
⚽️
منچستریونایتد فقط به دنبال جذب بالده به صورت قرضی با بند خرید است اما بارسلونا می‌خواهد بالده را با مبلغی حدود ۳۰ تا ۴۰ میلیون یورو به فروش برساند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/104577" target="_blank">📅 18:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104576">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a390435aa.mp4?token=BIY1gB_oDVAqrAmdnVedNK9QLCsL4Y01meyNqY24W5VnI33xVAE3rYgbmWZCpOEDa1pId2WLVoIaN3s4LIigRBZF4w4YFEVeFDDe6fui0IHrMjV_X3br6a6-IriR28SI4CdK4c6X4c5MMO4AsbMlHECNKbgZoEXynTcGUltHofoIcX9Wd6z-4I2H0t4kPMXZXSK1C6MH16RnicLYLYxOg-m7262a1ZzaMDO4C94FrtvJbrbYHKVeSB-X6gFS4IwuinmpGPXpjhD8Nv3J0Hg_Mn_tQO_yxt9EYcne7ejiV7YZmcSC_Ab4ng9cqM68P6spWWNQwQFDVmEvJOGIYvf8qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a390435aa.mp4?token=BIY1gB_oDVAqrAmdnVedNK9QLCsL4Y01meyNqY24W5VnI33xVAE3rYgbmWZCpOEDa1pId2WLVoIaN3s4LIigRBZF4w4YFEVeFDDe6fui0IHrMjV_X3br6a6-IriR28SI4CdK4c6X4c5MMO4AsbMlHECNKbgZoEXynTcGUltHofoIcX9Wd6z-4I2H0t4kPMXZXSK1C6MH16RnicLYLYxOg-m7262a1ZzaMDO4C94FrtvJbrbYHKVeSB-X6gFS4IwuinmpGPXpjhD8Nv3J0Hg_Mn_tQO_yxt9EYcne7ejiV7YZmcSC_Ab4ng9cqM68P6spWWNQwQFDVmEvJOGIYvf8qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
❤️
خوش و بش گرم بازیکنان پرسپولیس و تراکتور در تونل ورزشگاه یادگار امام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/104576" target="_blank">📅 18:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104575">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c210be91e5.mp4?token=Rqf_WZdkPDcZaD5hbiRX2gJg_Q_53fyJp55s_GReEEGjppHdsRZf_rRX70ePTtt6u8T0IYZ0Vjl1vmcmwz6Jg14WULzfbN6UKIqi1HifnQgg8CEBFIWA-JjuZJrgwJzIS5pqP-ENDizT9TXsIWeCjX2iNZ3GSmNzIe12qnnyIuAs1JzWUPEyMJuB-Hc59ilKCg_F4O700usG9tJO0EjKYZxUFsJnnyJxf-23JxluEDY7v4DxVPifez27MmNkKq_JYGQe1-FG979G2H_35wO9t5nhkub8VkBMSL6ld_ScZ1pmv4zQIi2I85Vs0kMXb4QhvSmwoqtBtUtM5OqpogRChA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c210be91e5.mp4?token=Rqf_WZdkPDcZaD5hbiRX2gJg_Q_53fyJp55s_GReEEGjppHdsRZf_rRX70ePTtt6u8T0IYZ0Vjl1vmcmwz6Jg14WULzfbN6UKIqi1HifnQgg8CEBFIWA-JjuZJrgwJzIS5pqP-ENDizT9TXsIWeCjX2iNZ3GSmNzIe12qnnyIuAs1JzWUPEyMJuB-Hc59ilKCg_F4O700usG9tJO0EjKYZxUFsJnnyJxf-23JxluEDY7v4DxVPifez27MmNkKq_JYGQe1-FG979G2H_35wO9t5nhkub8VkBMSL6ld_ScZ1pmv4zQIi2I85Vs0kMXb4QhvSmwoqtBtUtM5OqpogRChA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
باشگاه پرسپولیس با انتشار این کلیپ در آستانه دیدار با تراکتور نوشت: «ماموریت بعدی کسب سه امتیاز سوم
»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/104575" target="_blank">📅 18:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104574">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/631497f3c1.mp4?token=XuOhPieq_Wvm4bV5Ds2-iVgsiVt2oSlSiPP3j4_bTOGWT4SftMk3V3fiMaJq96xU19Bm94CKaM7NFvd1Q6NGqxe56emFhlACUZG82HjJxHy2uggKB63-d8mJrQUQ_4BPc2Enw2DgQd7qwTg5rzIqIgPQELkS9yJZ1EnXsaNsTqFOzJ14lW9WbSsKrnnu7Mist60tMK3lUTx_cWpjdcvWM-mE7iKzYA0G9txNYpY9KMvgIQNyGoKwoTjiq7pkrTqHSKn-qgO-Nk9Lg3mzOVpxlo0O60SEPxl4j3olRUl7RgUZHcIKUi8R1OjzZWK_8wD0mFcJklVxga28_oTBtA_TgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/631497f3c1.mp4?token=XuOhPieq_Wvm4bV5Ds2-iVgsiVt2oSlSiPP3j4_bTOGWT4SftMk3V3fiMaJq96xU19Bm94CKaM7NFvd1Q6NGqxe56emFhlACUZG82HjJxHy2uggKB63-d8mJrQUQ_4BPc2Enw2DgQd7qwTg5rzIqIgPQELkS9yJZ1EnXsaNsTqFOzJ14lW9WbSsKrnnu7Mist60tMK3lUTx_cWpjdcvWM-mE7iKzYA0G9txNYpY9KMvgIQNyGoKwoTjiq7pkrTqHSKn-qgO-Nk9Lg3mzOVpxlo0O60SEPxl4j3olRUl7RgUZHcIKUi8R1OjzZWK_8wD0mFcJklVxga28_oTBtA_TgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
کمال کامیابی نیا: تراکتور، پرسپولیس ب است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/104574" target="_blank">📅 17:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104573">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">⏸
🇮🇷
ویدیو باشگاه استقلال از تقابل دیشب با سپاهان و برتری قاطع آبی‌پوشان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/104573" target="_blank">📅 17:56 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/iv3EvOwhabNKqQNzrE-bZyuzblLB216nD98c8-EDgDyXtL2-9e40AlTv1sNT4WBhO4yVP14BAUcm2ycMxrlM2_CXDcmM78befFUl-u2kqLZa7zFrHBfVUeqE1h0LSx4Y-cp5jWgBIWsgp8HAPcDfUx1b_z6E3OltQ1xWLCm_Ig0RNinTtFKs5U5VbSID5Xznj9OGl8h3_0JMpZWcJ3PpB7sVMnHAub7C7wdgXJAjsn8YRkdHbdus4loXnBwCMLIndPXo15qVRt7Goizq6GWM0CQGnZyFTb15uSt6j95RoRQZewfikxPc9M3eCMBLAXtmUH6o806DXE-0EoKC9UPoUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 225K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 18:04:58</div>
<hr>

<div class="tg-post" id="msg-66010">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_RBDjLTBAjdhYpzW10wBx5JVhf4M2nqU5NKZfT3eNUGU0lFi9ly4Db9ObEeCMgFkYx9laM7bNU5DZG0k5Wl-9pkDcop_kL4JjG9thLsQW3oUC3vudElsGVvMIi0y7a2BAyUo8vV9wQ30IAHYgYsba06lJKNfQ32JyjNuoc07wHeS5QRRYabU5tYBaJPZii-Nac_aStTTcMPlvfhqLcLiaaQAmWOnRN3oFbGpIeSZXXUtxuJTL-nvgQU7Fu69VZ8LLC_OwAL-y5rasQpE2VlpdzElMUFzbMdIiS1hNlinLZPwUQ2dkSAgFaf7WFGc4erf1jc2hfATC_sgkKTzwgsJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ توییت شهباز شریف نخست وزیر پاکستان درباره احتمال توافق تا ۲۴ ساعت آینده را در صفحه خود بازنشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/news_hut/66010" target="_blank">📅 17:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66006">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fq38QXVV1aN8wYbVUI-xpzB_EAf4Y4x4nv8ju01tTWXnN3CcNRfEuXVd1oRAKz4ytdttX8iXOyXbKXUuKpZT4AnMY0i-U5NyopylBjS54PzrThiC1zp2othpmX5P_MAWhp8j5kxkuRpvzujqYshEJKsZATPXc4CXuEFxUogQ2IMLyassqCLWt56b4wNZq4RQ_9FF9Z3XYavIM4hjmybZv9ueKt2hgDVn1wnal-vKn6URTeAW0ESSivdNuofgG40RX9qbb6qxsUu1ETndMdOWMKKmbpe9iM3PtVG0PaX6Iv1k0nAhEVDWG5rMOdkmabGK-D_FndqQmFXr2E-tTTePwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R0b4wAChLNbqMsqchXZwxY54nLcgeBoGXw9c3gXu9gDYisX0pu_H-MjhjMVWhCVbe2DuzcQGzYKQEwXqWbX3WYDe5IdZlapHTqlZeXEdGzSIu9yhNTqbUGkJW67nTXgLNCL5nbVms8pSt3RsipExEu6mK2UHheV9tl1Ogie1RVmWDhEU8N2Kh0N03CeoqwRJ7wUN0xqg7t1K3RhRStVBm7kut0IqxMeRo2B8BAdFq2GrN0Y6w3FXYA6BkAQTm_0XmkLs5gPrYm8FASSGtyAtaCWV0uajApROkSF08Lqr7KiGFkE7PhifLpTff8QracW8YedIF-10Vqanwc4rvsnlqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MlGCCsxJyHF0lxNnB6QbXpd4SpMP6D6RYqf_bPqbhSGtdBuI81LiBpoRTu46tXudNQAy2DDmLZx4gHMpUEP3vjn8gAIPgaa34o84bsBeup7LEZNsWgxx_U44fLnjGaX7NwgV4ezNNwFP1AGh2c9tQ1Y5C0CQdNzgg0OPr8_7TIOn6lf2cEAmbtm-xUeuSjbKSvB3CimgTlEVwb8Rae1mw79g3BlMR3-q_cR-SSwndon2fIdvlHcF0-iR2wJa2nTFBxQWyKqMuf8gn86oCp35r8mRVefRD47f4N1SobaSi46Eb5pW2_DyY-F_UvR-HP1R5OXwBYi3aFGhhbKnGmPPbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u6ZnSrZDfurIy-blOf7vAuJ-5jgO4Gd3_qDfQ1IZ_gjY7q3VLMx60E1_ZEFLOysLbiX_UX3Or0XcAHoNjCi5RPit_gQUdCmjRjihTOv400yDMwDQzbxrAXCYXdenUOKoXrWKcdGlvfLuyzyqU9IS0T80lzgKO5cWBpFxue-XCnjoUVPt8eSADwPaL_VnBiPnKjulE4C8LFWmUJLcrbXuUdf7k4iwJxUDPwqE3i7-hVkZ2E0y8lWjdfWX0qX7qaqyq_i-0FIKgxOIxAvN2PKNXBhA8K7oPNaWSe91XGUCl8uJc001LoBSu-HXCN2uKlbX1ZnYI3IWI4pWZkfemHXLxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
جت‌های جنگنده نیروی دریایی ایالات متحده و هواپیماهای فرماندهی و کنترل آماده می‌شوند تا همزمان با عبور ناو هواپیمابر آبراهام لینکلن (CVN 72) از دریای عرب، از روی آن بلند شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/news_hut/66006" target="_blank">📅 17:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66005">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">از جام جهانی تا لیگ ملت های والیبال ! هیچ فوتبال و ورزشی و از دست گروه انالیز حرفه ای ما در بت ویژن در نمیره ! فقط کافیه یه شب از گلچین فرم های بت ویژن تا استفاده کنی تا ببینی چرا سایتا دنبال ترور ادمین این چنلن بیا اینجا تا ببینی فرق ما با بقیه چیه
💸
💸
💸
💸
…</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/news_hut/66005" target="_blank">📅 17:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66004">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJC66rm8tZJTFlTzlL3TLZCOXPKhT8854SnD0s_dl0OR67VDxVu735mnlrEy41xUvcWijy4cuQauGMHI4QEp_nmvtN7XkOob2DPtuvc4BjRLEfdh0dt-Q0exRG6GKq_hQNQ_aItk6Dh7cLO_MyBGOZp14wQye3-8WywnA89h1ACG006Y1iddnETVqBKs1XcQegqnfeWF7s1T7SoE0kaJUbGn19NqBIs1mJVfpvQ7RRCN5zRH-PR_OlLCUC97R9rGdAfeFdQrsgwa1zyPU9yNq2hfPGrk1BDyHodgDpxBOiqnttEYp7qadXbgo-ejdNC_tzZegiobR-AftWiWk6eSZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از
جام جهانی
تا لیگ ملت های والیبال !
هیچ فوتبال و ورزشی و از دست گروه انالیز حرفه ای ما در بت ویژن در نمیره !
فقط کافیه یه شب از گلچین فرم های بت ویژن تا استفاده کنی تا ببینی چرا سایتا دنبال ترور ادمین این چنلن
بیا اینجا تا ببینی فرق ما با بقیه چیه
💸
💸
💸
💸
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/news_hut/66004" target="_blank">📅 17:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66003">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgNssTpGmiu6n_BNM62lLGwCuYQlXHithwktfSPl5GpMAkQx2eDeIwTO5o35meac9HUvw_NILz96SMXeefikaTD7k3QBbDKxnUqau2qI6id22gQZQx0oyOz3L7V_w8K3eTUOBg56FgSnKb-NFKim_-hbN7Tqe8hsTLlT6H2EBfLrhzX-vStCNh5oRVOyMZImOiL-GSkbXA51KQS6dy3P_oXopozZsV2r9DA7Q8OtvHjrLqQM2tG5nslWeh63fM1PJAuGFCI8I3YzJV0zdeWgdmZ0Zj-mqWqkaqcvqM-AnZwPgbxXfZHvHrgF_l6_2qHhMEMNOlU5H8xFosmN9xcNuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعدادی از نمایندگان مجلس به همراه قشر تندرو امشب جلوی وزارت خارجه تجمع اعتراضی برگزار میکنن و به روند مذاکرات اعتراض میکنن‌
@News_Hut</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/news_hut/66003" target="_blank">📅 17:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66002">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHNQ182bOW3CLRIQE4Vxo-3A2s69qqknI7VcemMVDNTDRoh4DeTnIkt8GFS0HkDPx3_OfhB6f2t5enGmsuIVHt2H83YTr3k7W7FT4SShjveFSA-lI26d3ub5uL1qto3tTn_cCFQc9wdPHiUTd5t1BOyRhlrOCTpikOGlgmqhE016TEKlBIzHhqDO5JM7MlnvKSliVp9vIVyYLeZVtMGT694RE_WpU5hF3MIuxwXDj2HuBUCWzOc6JJi1NwV_fDqXHyVuEUkW2dEcJ1-N0QlGMfFw56vbE_ryjvtlNQlpQIjYmt1Yc_a33c5zeKxGXddqb94EM-09ys4PUxdnakTdPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اواخر بهمن ماه پارسال، ترامپ مصاحبه شمخانی که گفته بود «اگه آمریکایی ها سر حرفاشون باشن میتونیم رابطه خوبی داشته باشیم» رو بازنشر کرد ولی هفته بعد کشتش ، حالا دیشب هم صحبت های عراقچی که گفته به «توافق نزدیکیم» رو بازنشر کرده
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/66002" target="_blank">📅 16:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66001">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41b2c6552b.mp4?token=NGPp7t2K9gBSnKSjGjVcHraTP4JEK-WNm6Adn6uv6wxce9QTgcwg3Cvmptatip-aMvu0wfhfH9FYQLxrDiMH3QzvAO2A2pX2A-60yvMfQZz6GIJWZxF1xuot0nwJA0vA64Ehj8H9zJIHv_hKi2lgIOow4q1i911e-I0aWCgEZsqwiEkGJgBL4-QPbh94fzsHImSiQ__D2R9mNw-UyFRBmmcEughtO56HLY1oN3C33YmIY6Sg53hVU-tJM9ypcnsMIg-dEM1MRHcSVkAORWZnaYjXuT4gKL5qCNRqv3mDyFebCJUPiRAsmR5pUiKV7X7ZA_WDzRg5JEIvAusjgJFhRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41b2c6552b.mp4?token=NGPp7t2K9gBSnKSjGjVcHraTP4JEK-WNm6Adn6uv6wxce9QTgcwg3Cvmptatip-aMvu0wfhfH9FYQLxrDiMH3QzvAO2A2pX2A-60yvMfQZz6GIJWZxF1xuot0nwJA0vA64Ehj8H9zJIHv_hKi2lgIOow4q1i911e-I0aWCgEZsqwiEkGJgBL4-QPbh94fzsHImSiQ__D2R9mNw-UyFRBmmcEughtO56HLY1oN3C33YmIY6Sg53hVU-tJM9ypcnsMIg-dEM1MRHcSVkAORWZnaYjXuT4gKL5qCNRqv3mDyFebCJUPiRAsmR5pUiKV7X7ZA_WDzRg5JEIvAusjgJFhRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه هدف قرار گرفتن راکت انداز Tos-1A روسی توسط پرتابه FPV اوکراینی
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/66001" target="_blank">📅 15:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66000">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSUJzjjDvwcO2TXPgBuDba25NmklK0gStI-hgnChz-hfoIgzNp_Zu1VyE3PZKVM5oIT8aPZmBR2YDAPZI1dQrYwXiabjLJ-SsbywpzWKzjJ5zElIZMNY3T3BweAQOJp6Qfmdx0zZ57U2HhoYgN3kF2QsPBxRcxyJaxgCdlQ933ZE1mX9LAXkvZRc_OdtZfh5EQMaWz1blpTcs761bh005f06IJcI-hW6M0-P3jLvSTfGiTvzt87uUq7usxo3kHxI1EdxBsx1gvLr51pNH7fV_Vc8yZleNWyhW0ZVIgZBnZJ3Hlu17xsj75xN5-WyJWcLBiFntx92gjcqZ0yoiL96qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقایقی قبل سازمان حمل و نقل دریایی بریتانیا (UKMTO) گزارشی از حادثه‌ای در ۶ مایل دریایی شرق عمان دریافت کرده است.
گزارش شده است که یک نفتکش توسط یک پرتابه ناشناخته در دماغه بندر مورد اصابت قرار گرفته است.
خدمه در سلامت هستند و هیچ گونه آسیب زیست‌محیطی گزارش نشده است. نفتکش در حال حرکت به سمت بندر بعدی خود است.
@News_Hut
﻿</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/66000" target="_blank">📅 14:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65999">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
شهباز شریف:
من مطمئنم که توافق تاریخی بین واشنگتن و تهران، پایه و اساس صلح پایدار را بنا خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/65999" target="_blank">📅 14:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65998">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
شهباز شریف:
مذاکرات فنی هفته آینده پس از امضای الکترونیکی توافق آمریکا و ایران برگزار می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/65998" target="_blank">📅 14:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65997">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
شهباز شریف:
پاکستان در حال آماده شدن برای امضای الکترونیکی توافقنامه صلح آمریکا و ایران ظرف ۲۴ ساعت است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/65997" target="_blank">📅 14:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65996">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر پاکستان:
ایالات متحده و ایران بر سر چارچوبی برای یک توافق صلح که به ماه‌ها درگیری در خاورمیانه پایان می‌دهد، به توافق رسیده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/65996" target="_blank">📅 14:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65995">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوری
؛نخست وزیر پاکستان:
ما بیش از هر زمان دیگری به توافق صلح نزدیک شده‌ایم و احتمالاً ظرف ۲۴ ساعت آینده نهایی خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/65995" target="_blank">📅 14:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65994">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">شهر عجیبیه! تریسام بروبچ دهه نودی  @sammfoott</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/65994" target="_blank">📅 14:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65993">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
⭕️
مراسم خاکسپاری علی‌خامنه‌ای روز ۱۸ تیرماه در مشهد برگزار خواهد شد. از روزهای ۱۳ تا ۱۷ تیر هم مراسم‌هایی برای رهبر دوم جمهوری اسلامی در تهران و قم برگزار می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/65993" target="_blank">📅 14:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65992">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
از امروز صبح خدمات الکترونیکی برخی بانک های کشور از جمله ،تجارت،ملی،صادرات و توسعه صادرات با اختلال مواجه شده است.
خبرگزاری فارس اعلام کرد برخی منابع از احتمال وقوع حمله سایبری خبر داده اند اماهنوز منابع رسمی این موضوع را تایید یا رد نکرده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65992" target="_blank">📅 13:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65991">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/65991" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/65991" target="_blank">📅 13:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65990">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsFiWYFUkZzGYUeMamjg_p8bzGZALCGhJ8ELobWaB9Hk7aleosRTVIIhZqon3CNdtVjD8P-Fac89H6aXwlvwDuBGz--8vahsGEHekQ4JpirmSjJtnQCgl-XWGe63WvnM1p9y5zDpWl7BTpVB7kDyYnlNmU-eOTeuQ6Pt4OEzvLxYZqi61ipWtCrlLzKStC7Hriuk-yNjDbe1Jqlto94aObcebnnWfNh_-G12bjlIZcdHDVTFMU1Oez89K8tBPpH0QuzqCO2g2N_Mp5oDN6AVk0Kb6BGDBfmak8QYAEAllIHlo5uSQcfYI0X7PXfATbC0sw_yAhCkFc70JX6e3DTFQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/65990" target="_blank">📅 13:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65989">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFekwfsq22cIWPjisapT-ehg6FkkP3OWWFOc7cCJSzTsPJSOf3lS3jN9_3QooISM_cAUPvwztdBrQTQgk-PQoEXqUlLEBBf9hZyme-0lB2PwMx_iiqLn2IoYilYSp6vsnf_VVstzUJ_OoGsCp07grm-jmsFUQECcoWL7xrW_-ZhRVuaPPWGoy6SI0avel3Nk_4WxCufmgukYOehBbYh6H-HT3sJq8goNDoqJL-1D-B5QL_unzs7JK3KhtRVACRPFfYAQH1QgfSZkpLYQr_Ertk9FWDnbNqMABraNsRods67uUNzVn1kdXFeBKHgSy-ths9kPdasj_jn9lSQzaebBtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
جنوب لبنان؛ارتش اسرائیل پرچم این کشور رو روی تپه العویدات و کنار سازه یا حسین نصب کرده
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/65989" target="_blank">📅 13:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65988">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkBTYLLAnriA00R--DvIV1WqbQnapJPmRF8yDcCnws_rTtI0YiZa-yWlX5cRBFB1tyGVTlpX_2XfwrqfpVgXtI1np1QpE1sx-TOpyD67hWCDkD28PtaKTKiWMOU4ZuK23fuZOF3sPRJENC1AWwf2z_QfcB7Rv7EfYrR-wWDDtpPFITC9z41dbCNTB3bdydn-YLe786sacGMMvYVBxOtF_GqiF13ktqmkQYaUiNrcd3_BnVhE-weydujzK0t3ESpVfpTeNCsy-EtnZLTy91wd1-0j2N3-ECGiZ-H5jMJ0Deme81aTNYLr9nkl-c0NBns-mWmwp5XherT7wO5OWB-pew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ایران تو هفته‌های اخیر حسابی دسترسی به انبارهای اورانیوم غنی‌شده رو سخت‌تر کرده
- طبق گفته چند منبع اطلاعاتی آمریکا؛
- ایران بعضی از تونل‌ها رو عمداً ریزش داده و ورودی‌هاشون رو با مواد منفجره مین‌گذاری کرده
به گفته این منابع؛
- الان رسیدن به این انبارها نسبت به یک ماه پیش خیلی سخت‌تر، خطرناک‌تر و زمان‌برتر شده -
CNN
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/65988" target="_blank">📅 12:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65987">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85b34abe01.mp4?token=TrwIjwSi85cVKlxqCQeZI0tjBRYE8pgKMCi1x4DgAuwVnki7HNUrDJSDKOu3W3-3-pqAF3FawqPHRHsRZJc1Hs3K-iSDOfjASZhLVAvm0-G1AAdTYel_4350nW3ef_aytk5wJJp5QcW0viuN8wgXLyJNAamLOfAmkwyI-l5u12rZskCZXwK6VqsbYnYbALEulcoADyRqUDeEnw9e-4L6ILVXExW9fcr9aVtRAiFS6Wm2LEpwqrOGsimoVj9-F22qq6n4PiAj-f6Sg1yjkOy-IU5ffYPpQGvO_Xj8jZVGHCdWlzEcv7b8w-6sc5Hk2wU2C958x_1R62a26XYBybGXmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85b34abe01.mp4?token=TrwIjwSi85cVKlxqCQeZI0tjBRYE8pgKMCi1x4DgAuwVnki7HNUrDJSDKOu3W3-3-pqAF3FawqPHRHsRZJc1Hs3K-iSDOfjASZhLVAvm0-G1AAdTYel_4350nW3ef_aytk5wJJp5QcW0viuN8wgXLyJNAamLOfAmkwyI-l5u12rZskCZXwK6VqsbYnYbALEulcoADyRqUDeEnw9e-4L6ILVXExW9fcr9aVtRAiFS6Wm2LEpwqrOGsimoVj9-F22qq6n4PiAj-f6Sg1yjkOy-IU5ffYPpQGvO_Xj8jZVGHCdWlzEcv7b8w-6sc5Hk2wU2C958x_1R62a26XYBybGXmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انفجار شدید تانکر حامل سوخت در مکزیک
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65987" target="_blank">📅 12:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65986">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a45e16c46.mp4?token=JvZuBpucNs58jEtSg0oUCKZEhmiqrvdgWmn_i2X1FE2E_Q75mjLFB3KA6pbEjw9wsq32LrdGutMTipqpubXu_LYRHSFzPL3TmtFqsMk6PgumACGlGnUH7jl4fGl-x9kGlxKbVjuknbgCkjEOyYrwQUU6w3e7Y2kFWMn0zL_h0vCwIFxoQDtnHtndmgRu-Wi8qmrLUYKrW5RbF1uVglxjXuismYXNOTsrKIKXR3MGv5o-LiDTZ77Kc1bACuKGaTaL8hLdCayv2SnwX2V08srWZDIua3-zpsYS7DBgX5_YLUm3mLvkHynetY7h83u5qoRSNQmlAlqvuj2P--acoC0oEiNWEvWv1mcG1aaghHZCJWSO_PUgDWacZOxr3bfQO2JacMymgePufhulFdo7yZ4qFhtJ-ZBfwx0qzmNl3Ghb3IIKKK5wED9Ayk3x4Vj3jZQBiQfDX8UfrB7ZghDb8rqOE3dpEjcpaxVT0DTeuIwZrJ1Iami6jy5D64nN3e5xO08b995VHYVADddUwCmhp2xpS8AOGdIcykn6fr9sd34RcjOZWRj5R0u0-0Dg9jmFVB65ArXSj5Oi4G6yn-pgrVhLikWnFr0-BF7chw4nnNcGKn_w-S706hUnBq_rJ6WjhOewoDR3qBoLDIvhxk5lM800QZV2lk6aIeuzgKVjWO_IgUo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a45e16c46.mp4?token=JvZuBpucNs58jEtSg0oUCKZEhmiqrvdgWmn_i2X1FE2E_Q75mjLFB3KA6pbEjw9wsq32LrdGutMTipqpubXu_LYRHSFzPL3TmtFqsMk6PgumACGlGnUH7jl4fGl-x9kGlxKbVjuknbgCkjEOyYrwQUU6w3e7Y2kFWMn0zL_h0vCwIFxoQDtnHtndmgRu-Wi8qmrLUYKrW5RbF1uVglxjXuismYXNOTsrKIKXR3MGv5o-LiDTZ77Kc1bACuKGaTaL8hLdCayv2SnwX2V08srWZDIua3-zpsYS7DBgX5_YLUm3mLvkHynetY7h83u5qoRSNQmlAlqvuj2P--acoC0oEiNWEvWv1mcG1aaghHZCJWSO_PUgDWacZOxr3bfQO2JacMymgePufhulFdo7yZ4qFhtJ-ZBfwx0qzmNl3Ghb3IIKKK5wED9Ayk3x4Vj3jZQBiQfDX8UfrB7ZghDb8rqOE3dpEjcpaxVT0DTeuIwZrJ1Iami6jy5D64nN3e5xO08b995VHYVADddUwCmhp2xpS8AOGdIcykn6fr9sd34RcjOZWRj5R0u0-0Dg9jmFVB65ArXSj5Oi4G6yn-pgrVhLikWnFr0-BF7chw4nnNcGKn_w-S706hUnBq_rJ6WjhOewoDR3qBoLDIvhxk5lM800QZV2lk6aIeuzgKVjWO_IgUo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
خبرگزاری فرانسه:
روز جمعه، از کشف یک جسد در صندوق‌عقب خودرویی در مجاورت محل تمرینات تیم ملی فوتبال ایران در جریان مسابقات جام جهانی ۲۰۲۶ خبر داد. بر اساس این گزارش، بازرسان و کارشناسان پزشکی قانونی مکزیک در حال بررسی جسدی هستند که در یک خودروی متوقف‌شده در پارکینگ بیرونی استادیوم «کالینته» در شهر تیخوانا پیدا شده است؛ استادیومی که به عنوان اردوی تمرینی تیم ملی فوتبال ایران در این دوره از رقابت‌ها استفاده می‌شود. این حادثه تکان‌دهنده تنها یک روز پس از افتتاحیه و آغاز رسمی مسابقات جام جهانی ۲۰۲۶ رخ داده و پلیس محلی هنوز جزئیات بیشتری درباره هویت مقتول یا انگیزه احتمالی این جنایت منتشر نکرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/65986" target="_blank">📅 11:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65985">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1ac66f6c0.mp4?token=IIV2IFU4s_o_OLy4ZMPOZwBZM9DKuL0L6N0AZRQivwE7guQN75K6eQCDmQ9kar0oUeZYl5VslWCUGfU3K1JY4VIUt_CAwMToCtMRiX2GocrR9WvN8xnLYov2pS6PVH2GMlEajHh9_Jfn4eFIurJxjYlp43HwnWI_4_PAOSkruoHytxKT4O3QKF0QY3z2tJarxmTSzaQKboUAx_GYXdfFtgoR8c0KNJ8CnNrCoWWV2LqvldmROxuZt72MVUA4C5Gejm8t0Y-f5gLELnEK0Pwiaw8c_gKRVn0auv0nUAcJ4iCdASTCkLq1FULQEiGrlzeszbNCypEqcoTQe8lvcIi_9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1ac66f6c0.mp4?token=IIV2IFU4s_o_OLy4ZMPOZwBZM9DKuL0L6N0AZRQivwE7guQN75K6eQCDmQ9kar0oUeZYl5VslWCUGfU3K1JY4VIUt_CAwMToCtMRiX2GocrR9WvN8xnLYov2pS6PVH2GMlEajHh9_Jfn4eFIurJxjYlp43HwnWI_4_PAOSkruoHytxKT4O3QKF0QY3z2tJarxmTSzaQKboUAx_GYXdfFtgoR8c0KNJ8CnNrCoWWV2LqvldmROxuZt72MVUA4C5Gejm8t0Y-f5gLELnEK0Pwiaw8c_gKRVn0auv0nUAcJ4iCdASTCkLq1FULQEiGrlzeszbNCypEqcoTQe8lvcIi_9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند تا پسر اهوازی وسط جنگ وقتی رفیقشون خواب بود این شاهکار رو خلق کردن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65985" target="_blank">📅 11:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65984">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11109e09bd.mp4?token=nK8CCkhzTaFQpk_kDGLHwHUEIWrsvIFunDMI_bIe-yZi_rG8exVGoqCSzgH-GsrQqz7b-H8eSidXwIiUjzxSGkd1cNLyJHUSn7BsiFngTrSkDFPOBcLFWcUU9-gEy8_89Z72zyz8DLKF1HlML671dfkqxiJ19jMXMsVVnxQ_dE9GGa9aKKs7kxmxKl4uUO26lBPahtcbRgTNNqbyoofTLfDK30VA_YZMdbfh3gvdx1VBqZ-1c2Gx7M2MlpBDKlaXOZCCo4pbiHgDGUbnKgrpyiFMmRTbafbL8Z5fguPs9va3nETApcXKVSlwCG5AEZVOdFChGNENlsdfHZ8DuqmGNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11109e09bd.mp4?token=nK8CCkhzTaFQpk_kDGLHwHUEIWrsvIFunDMI_bIe-yZi_rG8exVGoqCSzgH-GsrQqz7b-H8eSidXwIiUjzxSGkd1cNLyJHUSn7BsiFngTrSkDFPOBcLFWcUU9-gEy8_89Z72zyz8DLKF1HlML671dfkqxiJ19jMXMsVVnxQ_dE9GGa9aKKs7kxmxKl4uUO26lBPahtcbRgTNNqbyoofTLfDK30VA_YZMdbfh3gvdx1VBqZ-1c2Gx7M2MlpBDKlaXOZCCo4pbiHgDGUbnKgrpyiFMmRTbafbL8Z5fguPs9va3nETApcXKVSlwCG5AEZVOdFChGNENlsdfHZ8DuqmGNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ربات گدا در چین دیده شد
یک ربات انسان‌نما که از چندین روز بدون شارژ ماندن شکایت می‌کرد تا همدردی رهگذران را جلب کند، در شبکه‌های اجتماعی چین مشهور شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65984" target="_blank">📅 10:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65983">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a77f6aacbc.mp4?token=bV9hsTp_fKYwcSQeBemFTFs2n8MmRBdEETyMgyzeTmCy4u2Ze7a61Z9cDTYAtx71OKPPkXVQ4ZEvBViE5AXB-Byq-GEUTMdo5HcLw01n-vatRyLeUieugn7ZydIh2KF_e77N7fcFBPbgdNj2QzYs7lmr52V1UHgj3-fvFwIm144NS0czeFlpFCDMt6pGMGPovdhXORomckOu1gPbGTdx6gHa6KEaI_yMgSOTGjMqdb9jGAjnwppWzA8ovfnmRcrDCoXmBMy3RYmett-AOfcIl_SMSKmxIhtNfzlGeD_hoPlZrm94c2NZmsY6Uwqk0KT1ZiGMlONaXdxXrulIDPPJDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a77f6aacbc.mp4?token=bV9hsTp_fKYwcSQeBemFTFs2n8MmRBdEETyMgyzeTmCy4u2Ze7a61Z9cDTYAtx71OKPPkXVQ4ZEvBViE5AXB-Byq-GEUTMdo5HcLw01n-vatRyLeUieugn7ZydIh2KF_e77N7fcFBPbgdNj2QzYs7lmr52V1UHgj3-fvFwIm144NS0czeFlpFCDMt6pGMGPovdhXORomckOu1gPbGTdx6gHa6KEaI_yMgSOTGjMqdb9jGAjnwppWzA8ovfnmRcrDCoXmBMy3RYmett-AOfcIl_SMSKmxIhtNfzlGeD_hoPlZrm94c2NZmsY6Uwqk0KT1ZiGMlONaXdxXrulIDPPJDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ بعد دیدن این ویدیو از مسعود فهمید جز توافق راهی نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/65983" target="_blank">📅 10:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65982">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKdP5IkNGCern6J5ZWxtzacNYJs2ERoK5KXSYWu4VvEW9Mv5P1shdtD0OPImfQ-yIrBcL8pemp-TaZl4qtxvhIaIVURX0QaHgc0KizdOBwbzLP4hLHKc0CW2-A6K-Xh7ku0zIASDVgLdFeib1UF54Imyf0xaf9Kc7uUyh_rRVaKWbO0t2YKZ2lb-k6xoHP2FlxmCPRVDJIeSOqpKGbf-8KrHd_aKe6ve_8SU4XcYwu7jyBvCcBRqFoeryp88LcbDjejTurdKV1tEC0bffQ7JBYBig6MP6KxhHDX4_myCNq1U9sjYNHwTHHuFrtqdB1d9QYISdprMwn-Vs7xXf28unA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سنتکام:
ایران چندین پهپاد تهاجمی یک‌طرفه را در تلاش برای حمله به کشتی‌های تجاری در حال عبور از تنگه هرمز به پرواز درآورد. نیروهای آمریکایی در ساعات اخیر همه آنها را سرنگون کرده‌اند، در حالی که جریان ترافیک از طریق تنگه بدون مانع ادامه دارد. این کریدور تجاری بین‌المللی همچنان برای ترانزیت باز است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/65982" target="_blank">📅 10:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65981">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/65981" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/65981" target="_blank">📅 10:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65980">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=bAq0aA1CxMQ1Oey-nWGuAwpet_3FrfDwGgLi6wuFsXkgbcl_IMjof6I5cnmX-_BU-m2QQx9B_oNIoViTaUl_zBzayAQ6J5NCZWmq6MJ_liArYOCuzDGH0OwjKPoufTcVAk4x9gVyoNsNbwiKpbfYCyfblihPBl2v_9XskHizlHn-g4FxHhKkoiitWLLC2MzHnwnbqGRc5p4q5zax5vZ9oJy4pRhRB54kxKMy7I0I4Hc6d9Ix7nVoYC7ViXSTtlzYfzLh-RKLkmdB4fr6C6ny9b43G6Weknlt3nRiBPshZBxLtcomdN2IOiBL4L2RWv-XrGzMTYI_F0z1eHDYhiCz9Scv_hd4wosgUqciCsLfIfFi7TaBTJ1w7VD_g-_Zq8XKLUOMJUJT1VuIRPU4wO7spcXtBzeux0_i2DGo7_55Zs0NlClAkoHExHye02UCy7EMyykQzYXHtnynAnf8eLu54YWPGMAjh-vOEvrDkRXhcdhbJKJrarskB6mlA5kDf8ro5vNReAynPXqIS1mt8zTyiW_m1ztLC-WSwmGfmp5AefgnVJ2-sUWY8FzYpMVnTO6Dd97BfklRwijQBvXzJ-lIHgy3LZ0nzjGKZyJ2HHtXYomuyqG_w8nBdAdkhAJYu94x0QfQE_uWscag0aZXM9Ghu_ebpfDXpqgUblHrLFk2QJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=bAq0aA1CxMQ1Oey-nWGuAwpet_3FrfDwGgLi6wuFsXkgbcl_IMjof6I5cnmX-_BU-m2QQx9B_oNIoViTaUl_zBzayAQ6J5NCZWmq6MJ_liArYOCuzDGH0OwjKPoufTcVAk4x9gVyoNsNbwiKpbfYCyfblihPBl2v_9XskHizlHn-g4FxHhKkoiitWLLC2MzHnwnbqGRc5p4q5zax5vZ9oJy4pRhRB54kxKMy7I0I4Hc6d9Ix7nVoYC7ViXSTtlzYfzLh-RKLkmdB4fr6C6ny9b43G6Weknlt3nRiBPshZBxLtcomdN2IOiBL4L2RWv-XrGzMTYI_F0z1eHDYhiCz9Scv_hd4wosgUqciCsLfIfFi7TaBTJ1w7VD_g-_Zq8XKLUOMJUJT1VuIRPU4wO7spcXtBzeux0_i2DGo7_55Zs0NlClAkoHExHye02UCy7EMyykQzYXHtnynAnf8eLu54YWPGMAjh-vOEvrDkRXhcdhbJKJrarskB6mlA5kDf8ro5vNReAynPXqIS1mt8zTyiW_m1ztLC-WSwmGfmp5AefgnVJ2-sUWY8FzYpMVnTO6Dd97BfklRwijQBvXzJ-lIHgy3LZ0nzjGKZyJ2HHtXYomuyqG_w8nBdAdkhAJYu94x0QfQE_uWscag0aZXM9Ghu_ebpfDXpqgUblHrLFk2QJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/65980" target="_blank">📅 10:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65979">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEKuz6c-w2VYiBC_W9cV9SXWimKsVg7Rb0iouA-6UnU77OaAZaLASI2dGex73HM9mhrtEq2YnngBq4jDgPtN7Pn-ht1xAWd1hsBfQzhszOl7NBzm_yZf_dY5tSjsxD8FRQlYYb3RzS3mXGT3hzhTvl5xviF6ASbhSoRBJu-RgG52Qzs__vyIa3FF-3-IfLZa1-0R9dBZaLFoqRdw8OwBSfCCadtoasStiyrzbT-al9X0V4jlYXBhnL9PKKJPCBsNMz-fINHd3BMUH8IiGC9GDxU4A_Qz2t3_I7nhOhYAisnb812YzoasZzPOKp2GoRzCblHpveFe_3ohSSe_14CpDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روح الله خمینی:
اگر آمریکا و اسرائیل «لا اله الا الله»بگویند ما قبول نداریم چون که آنها میخواهند سر ما کلاه بگذارند
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65979" target="_blank">📅 09:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65978">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b92693abb1.mp4?token=IiUaZgHqoZ1V8kYlyajdk5cDr6yxzomW7q5k91Z1hCx_nbKOqNkjT8cE7IE8PXSL3xb3tPe29RNQ61ZvsLtUltPqFCK7S_D1WsaOivTVL2SOAWRdAxx86Iwp3NYtfkkKZ9MkKraRERB5WrIioiZm4cTDcbzy5Ftw40QNn7e-cjT_lcjIwxL7_Mo3SJm3_KEEKKPoAv_nx6IQ55FeAGkCFAcKlTLWOezO_GxWCRfQvKvN2Js_3rml-ib9ueqKdXtaYJyzk2azynYnI3K7jQK998EijKJAslTWMWz1leiCZivYqLv81hPnDfgJFCLm28H1kl5IyUsQJUh7GRNyYqMC4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b92693abb1.mp4?token=IiUaZgHqoZ1V8kYlyajdk5cDr6yxzomW7q5k91Z1hCx_nbKOqNkjT8cE7IE8PXSL3xb3tPe29RNQ61ZvsLtUltPqFCK7S_D1WsaOivTVL2SOAWRdAxx86Iwp3NYtfkkKZ9MkKraRERB5WrIioiZm4cTDcbzy5Ftw40QNn7e-cjT_lcjIwxL7_Mo3SJm3_KEEKKPoAv_nx6IQ55FeAGkCFAcKlTLWOezO_GxWCRfQvKvN2Js_3rml-ib9ueqKdXtaYJyzk2azynYnI3K7jQK998EijKJAslTWMWz1leiCZivYqLv81hPnDfgJFCLm28H1kl5IyUsQJUh7GRNyYqMC4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مراد ویسی تحلیلگر ارشد اینترنشنال:
جمهوری اسلامی خامنه ایش رو میکشن، مقاماتشو میکشن وتحقیرش میکنن بعد میزنن تو سرش میگن بیا بشین سر میز امضا کن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65978" target="_blank">📅 09:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65977">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/65977" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65977" target="_blank">📅 01:17 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65976">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v40moqvDum03zP1sf_FbmkGfu5JVDQ9ccbXCthljkUPkD10MyY7ejKA9Dgkazxh8Th0_hHrgaHk-PGR4iq5GtwAJlbA24Ih3AZokPbGa_H1dkcCBM_HiRgDYrSCM37ioAZKannMGaDebb30jZ8Hng8hx2p9bUaBFyt9CaKPQbwvAuWBVkH0r6ecewES99vz93XVf6fTHg3_Be1vnNRHTD4nB3vP9vAYXE8gDNc7FGtsKfcjQUCTfvgoqnX0tXSJr3BcmJNvQEl7f8XdkSqPy0H5eB4NQTw4aA3CzwgUu1IQLkJdWEmkB62FKXpCMnYAzLSR4wwpiTzSrcQixXK-35Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65976" target="_blank">📅 01:17 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65975">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cV7sDxW7d73X9bVQik1oAN8PPeAyKzlh1kdI97T0njUMTOg4c1VvWWBd1nGWl7V8FaqxLKw-RrzZa_kOL4nvcTnPVvGhz8NVzhrD7Gfm8CQNwSgKjLkpxQAQ665xlH4lOurgyAWcQU21D5Ks11ge2d2Px8S6p7R8jhngMZHGzTJJ_IsVCfAZBKYkgGZpkO4MlxVfZLp9ly-rqjPZOz85VLEizzYy74S1R6rH31TEMq6orjJANGJMKwUQE8iyaolS9vjLUucdQjtaAWFtEKnoMCwHbRlhSrWOwGcurkmD-yCRpRquMWxmpv18j_MtindKwEEBHtOlBGXtDz6poT5qdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تندروها گرفتن رو قالیباف
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65975" target="_blank">📅 01:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65974">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
سپاه:
کشتی هایی سعی کردند بدون مجوز از تنگه هرمز عبور کنند و مورد هدف قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65974" target="_blank">📅 01:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65973">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ER72uDbu5sYLZz342yFbOMX96ADg4qq2J86rexQKH5TSnYuVKh0iyoLyuf9Vmhwxwdivk4UkIRAM_Mo0RHqRwLhXbpgbs76y2P_XImbw3QvjlxMyTGJ4AmlvFSNZo343PoOLAXsetaXQsC8ZKennuZg85ANzP-nO2wceiNTLHIE0lCg4BAp8c1ROpRvTdmPwMniEUlZTVEFf93uj2RQMP257Lk1ZZ4w5MeJxwd37ktIGS3QgDfuQikyKq06DRNRFU0GYdIdcULmVuicApOzoZQcgyTSsUKTwsr-7f_gRfWUWx8NpXS92iv2FYe1zThxiXrkOU02jnUJ1_fZ8eS-V-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برزیل
🇧🇷
-
🇲🇦
مراکش
🏆
جام جهانی ۲۰۲۶ - گروه C
⏰
بامداد یکشنبه ساعت ۰۱:۳۰
🏟
ورزشگاه متلایف
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
- برزیل پرافتخارترین تیم جام جهانی با
۵
قهرمانی است و در همه ادوار جام حضور داشته است.
- برزیل در جام جهانی ۲۰۲۲ از گروه خود صعود کرد و در مرحله
یک‌چهارم‌نهایی
در مقابل کرواسی شکست خورد.
- مراکش در شش دوره جام جهانی حضور داشته و بهترین عملکرد این تیم کسب مقام
چهارمی
در ۲۰۲۲ می‌باشد.
- مراکش در جام جهانی ۲۰۲۲ با حذف اسپانیا و پرتغال به
نیمه‌نهایی
رسید و یک شگفتی بزرگ خلق کرد.
🧠
اگر دنبال جبرانید، یعنی از مسیر تحلیل خارج شده‌اید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65973" target="_blank">📅 01:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65972">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
نایا خبرگزاری عراق: شنیده شدن صدای انفجار در قشم و سیریک  @News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65972" target="_blank">📅 00:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65971">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
نایا خبرگزاری عراق: شنیده شدن صدای انفجار در قشم و سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65971" target="_blank">📅 00:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65970">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f73bf5f98.mp4?token=ip9KTEWbNIztWSlnTw8T_IMlq8mhGULgZ-LlTy1ezgi-2rews321VM_H2zCpH_pMggJETbgYvOVEj2tIfB-7ANZBgzOc2gkzmOFfyuvhQH5Dwn-smnW9mEcOopYyuD8FV9_h6ECGa_aL9UAanU-gnB29c7JrSFmG8LrbWQWy0AwKRc8jimOIMKdAGaYgajWkOswSOZA30cMcbQNZF09P5X023Nw2NNOq55dQAcow4g-1L3-xh5ywgWveku_U6fTjx5abcQMZcykFuan35YvQ3OOQchztVzkQZh6UNasyVKc6qATypTYGBzhu-Q8UCp7L2TYuuI2DeR3qLRIXc92CKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f73bf5f98.mp4?token=ip9KTEWbNIztWSlnTw8T_IMlq8mhGULgZ-LlTy1ezgi-2rews321VM_H2zCpH_pMggJETbgYvOVEj2tIfB-7ANZBgzOc2gkzmOFfyuvhQH5Dwn-smnW9mEcOopYyuD8FV9_h6ECGa_aL9UAanU-gnB29c7JrSFmG8LrbWQWy0AwKRc8jimOIMKdAGaYgajWkOswSOZA30cMcbQNZF09P5X023Nw2NNOq55dQAcow4g-1L3-xh5ywgWveku_U6fTjx5abcQMZcykFuan35YvQ3OOQchztVzkQZh6UNasyVKc6qATypTYGBzhu-Q8UCp7L2TYuuI2DeR3qLRIXc92CKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صدا سیما: هک تصویر انفجار اتمی در تلویزیون، سیگنال آمریکا بود
!
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65970" target="_blank">📅 00:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65969">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/060800d75a.mp4?token=mgRlcc5QvEsSPP_LRNIq9a4cSrDWJrCb0WzD6qml536ObmTNxfcBgq8A0QrAgNf-gCtTfBSTSpv9y36K8QKPTA8MOYPxO6ozULgmRxZvS4B1d16WZQZSWve5rpIcY9IN6lNs6ag3HuNeJK47wBsJnxDy7fO_lBQjWz6wcrJv8TFQ94kd2JDJa9_tHwc-7psi96XUoGKEbwFuCjYM__BzfJ2jVc-frv3qL6IUw9W9MG6l-eh_bIhcuy5jJglT2Sz9G-50AvrCGN92WB8EN99DJ7pYHn3lHAMLqK-vyDFeuqWc6HegVlvfuacaz6J5PSyzhndi_7goYHjkwPZikMGfNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/060800d75a.mp4?token=mgRlcc5QvEsSPP_LRNIq9a4cSrDWJrCb0WzD6qml536ObmTNxfcBgq8A0QrAgNf-gCtTfBSTSpv9y36K8QKPTA8MOYPxO6ozULgmRxZvS4B1d16WZQZSWve5rpIcY9IN6lNs6ag3HuNeJK47wBsJnxDy7fO_lBQjWz6wcrJv8TFQ94kd2JDJa9_tHwc-7psi96XUoGKEbwFuCjYM__BzfJ2jVc-frv3qL6IUw9W9MG6l-eh_bIhcuy5jJglT2Sz9G-50AvrCGN92WB8EN99DJ7pYHn3lHAMLqK-vyDFeuqWc6HegVlvfuacaz6J5PSyzhndi_7goYHjkwPZikMGfNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
گفتگوی عراقچی هم اکنون شروع شد.  @News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65969" target="_blank">📅 23:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65968">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
عراقچی:
محاصره دریایی آمریکا اولین چیزی است که در این توافق به آن اشاره و تاکید شده است که باید رفع شود
دارایی‌های مسدود شده طبق یادداشت تفاهم اگر امضا شود، آزاد خواهد شد
هیچ‌یک از دارایی‌های ما نمی‌تواند مجددا مسدود بماند
برای جبران خسارت ایران طرح بازسازی در نظر گرفته شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65968" target="_blank">📅 23:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65967">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
عراقچی:
به زودی ایران و عمان بیانیه ای مشترک در رابطه با تنگه هرمز منتشر خواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65967" target="_blank">📅 23:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65966">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
عراقچی:
به طور قطع تنگه هرمز به شرایط قبل از جنگ باز نخواهد گشت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65966" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65965">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
عراقچی:
پایان جنگ در توافق همچنین به معنای خروج اسرائیل از مناطق اشغالی در جنوب لبنان است و ما این موضوع را صراحتاً به طرف مقابل اعلام کرده‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65965" target="_blank">📅 23:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65964">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZltb-k9mIX0UBlCMH67leDrEP27cYU81VT3oFGnd7gYsbeD-UwJgNwmJYY6xc19rnahhz72BWeD8c0N3obSopBaLHeDiyO6DN17LdRKcXhBIBLmYHvFNSNu_bGH0rX8zLtZVrJP2dWzm4LDRlE19lB9hhtYswMyp_yrv5AXHNfodtsM4ScR5GG5CEetJmj-e_cMjfxETm98w-e6ltGUdGthjdmUDtiQdNDhbGCsFO8OiIHa4_I8G5Lk4uNRLW48TXlM4tx9MCt9fPqNlbflEjaMSiCQBLwd9asI_TUz1nlrdRx_xMBWU_d_TOxnNuPpRSETBpHtdGRzOsGD55blhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
تعهداتی که داده شده باید حفظ شود. نه اگر و نه اما و نه بهانه‌ای. برای معامله نزدیک پیش رو، راه دیگری وجود ندارد.
هر چه بکاری، همان را درو می‌کنی.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65964" target="_blank">📅 22:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65963">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‌
🚨
🚨
عراقچی:
نتیجهٔ تفاهم یک یادداشت ۱۴ ماده‌ای است و وقتی نهایی شد تک‌تک آن را به مردم می‌گوییم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65963" target="_blank">📅 22:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65962">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
عراقچی:
ما پیروز میدان هستیم؛ مقامات خارجی به من می‌گویند که ایران را این‌گونه نشناخته بودند و ایرانی‌ها شگفتی آفریدند و با قدرت بیشتری از جنگ بیرون آمدند
من می‌توانم اسم ببرم که کدام مقامات این حرف‌ها را زدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65962" target="_blank">📅 22:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65961">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‌
🚨
🚨
عراقچی:
هیچ دوگانگی بین میدان و دیپلماسی وجود ندارد و هردو در یک‌راستا حرکت می‌کنند
به این ۲ رکن، رسانه و خیابان‌ هم این‌بار اضافه شد و ۴ رکن باهم در یک‌سو حرکت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65961" target="_blank">📅 22:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65960">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‌
🚨
🚨
عراقچی:
همهٔ ما مدیون تک‌تک نیروهای مسلح هستیم.
همین‌طور ما مدیون مردمی هستیم که ما را تنها نگذاشتند و هرشب در خیابان‌ها هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65960" target="_blank">📅 22:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65959">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
عراقچی:
دشمن تصور می‌کرد که بعد از جنگ ۱۲ روزه، در جنگ ۴۰ روزه می‌تواند ایران را تسلیم کند اما با مقاومت جانانهٔ مردم و نیروهای مسلح ایران مواجه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65959" target="_blank">📅 22:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65958">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
#فوری: طبق اعلام زیرنویس شبکه خبر ، عراقچی تا دقایقی دیگر مهمان این شبکه خواهد بود  @News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65958" target="_blank">📅 22:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65957">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
خبرگزاری تسنیم وابسته به سپاه؛
حزب‌الله: لبنان نیز شامل آتش بس میان ایران و آمریکا است
«حسین الحاج حسن» نماینده فراکسیون حزب‌الله:
بر اساس آنچه از سوی مقامات ایرانی به روشنی به ما ابلاغ شده، لبنان نیز شامل آتش بس است.
بر اساس آنچه مقامات ایرانی به ما ابلاغ کرده اند، اسرائیل از خاک لبنان بر اساس این توافق عقب نشینی خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65957" target="_blank">📅 22:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65956">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 450 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری عالی
✅
مناسب برای گیم و استفاده روزمره
✅
تحویل فوری
✅
تست رایگان قبل از خرید
❗️
پشتیبانی 24 ساعته
📣
کانال رضایت مشتری @kavianivpn  جهت خرید اشتراک پیام بدید
⬇️
…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65956" target="_blank">📅 22:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65955">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrgIBwUusuhaUOfSbkwORsh2MYGBxOeKgeJF7U-6sCpaLLtIQ8ebHStZH34gckUEpFotwSEAHbYj0xQipMRRdg7g1KRlLkDQZLD-kfDEBGzxQDZm4OyLBbVkXBXTCY3nCVIFkLkc7OfRlBmV4Ghcae_pfuSVbpGPOdCj6Sz_SR7M9uJJ23ojnBCVNB9OKRA5eXj3QWH91LuvolGB-JqQoS_QcspOPRkquFguBDfT46LYpoIGKkK6Skmkj4dffHV4ahqKm6k4lWP9BLMmxls2xEbg3IMV6ak2Vypetfh_s3qWn0KdJzy_W2FupUeIEmA4g6ZPq70JUDYtVgB5U3_tuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 450 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری عالی
✅
مناسب برای گیم و استفاده روزمره
✅
تحویل فوری
✅
تست رایگان قبل از خرید
❗️
پشتیبانی 24 ساعته
📣
کانال رضایت مشتری
@kavianivpn
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65955" target="_blank">📅 22:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65954">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
کانال 12 اسرائیل :
توافق قطعی است و این به نتانیاهو اعلام شده.
ترامپ از ایران خواسته به صورت علنی درباره توافق شفاف سازی کنه و هشدار داده انجام ندادن این کار پیامد هایی رو به همراه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65954" target="_blank">📅 22:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65953">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
رویترز: امارات ۳ میلیارد دلار از دارایی های ایران را آزاد و به آنها تحویل داده، این اقدام تضمینی بوده در ازای اینکه دیگر به این کشور حمله نشود
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65953" target="_blank">📅 22:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65952">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3a3YuMhrttbJTqkIg7oIEM7Dxg8etB9dVoo0Rc3B7BIsoAPpLpVty7uilIeobsbrOt33K5_AXNf2VX7XlNRqA9SnZyOWUBem-IISmur7XuQGayK6BK3-tCQVBrT_s8lQz3QiV1oTFiauLg5B1QBfXmifX9YEDXtftTF5Vmajt1oQmsrSpzDqUmCoaKvkCkGzl_kkymAzn1d9He-GyvQ7-jEezG-BzDB2E4reA0Am2rH2WsQuhg3_rCnRulyGzs0xbafw4j4DsvjCrIQkfVWZAEvWnBrOjQ6XRV-P7CRTnBKlBeS8Fsv_cllwGk5l7blCBx5vLwrRt-nKq-HyTDtYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#
فوری
: طبق اعلام زیرنویس شبکه خبر ، عراقچی تا دقایقی دیگر مهمان این شبکه خواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65952" target="_blank">📅 22:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65951">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itk82fceMTCicY6bAIFjah-YhCCdn-w-axAwKBobA4K7nlEirb3vYCoDvQFMAFpUAiaZdNW8Hid53z3lvd_eA3q4KzUf8FI7Yx2nfaeUvCaLPAsPIbHw9g0YRwPanV4F94T-9iTzWB_HgYuUGTXn2KGUYLcEWv9KL3klKH2cUyW8hQEJsK7rfbO_JylJDb6kjWwL989xLroz7l1bHxgiwUuxS6oukBsvozlRHR9Hxdav69u6CTZM4NUR0O6PJ4CMdQdaLxe-eLPv_fIV0RrVw5bU7ltE6RRDBNurm7HdvKKCMaMJyKmZG4G1SoFwCqZDmCx5Vno-2h443mWkSj3dDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشالا به شیرمردان سپاه اسلام و حضرت آیت‌الله العظمی سید شیرمردان حاج آقا مجتبی حسینی خامنه‌ای، خوب دارین کیر می‌کنید ترامپ زن کصه‌رو #hjAly‌</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65951" target="_blank">📅 21:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65950">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJ-KSti4VnoSkEl-kymVBZEla--6fTAFpJkpfW4kJUic-774OW8z0yxNDYOmYbYTXa_kSa2n4Z71agkYLxfiGcZPFfl8ZSy1yFQi_QOQdPZGbn7rWqVdtvKEHndiYkH8m4JbUcxzg87qtiwbGBmXmWdD6arPWusGIn1hM0SwRCcKNBZQxKt8_cs5INWQCVnts5TbUY7A7nfi9ZVgeViAtF5baIoJXTWmBQjuweZ9Cf0Gkbe3-jbQGGB6OWk4LgmrmMJlbw-G_wmLNKAvTVGlQx74IKqBV5EEUzQrwRGkJxzKWXnDnieU3d82avGZAZSqyiRdcK7wgzFZ4_30aCo7Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ثابتی نماینده مجلس:
طبق اطلاعاتی که به دستم رسیده توافق احتمالی بدتر از برجام است.
نه احتمال جنگ را از بین میبرد و نه گشایش اقتصادی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65950" target="_blank">📅 21:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65949">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
الحدث:
وزیر خارجه پاکستان امشب عازم ژنو میشود
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65949" target="_blank">📅 21:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65948">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🤖
رایگان پیشبینی کن؛ جایزه ببر
🍸
درسته! کاملاً رایگان می‌تونید برنده بشید؛ فقط با پیش‌بینی بازی‌های فوتبال، بصورت کاملاااااا رایگان میتونید برنده جوایز ما باشید
💸
جوایز هفتگی پیشبینی رایگان
🥇
نفر اول ۱۵ میلیون
🥈
نفر دوم ۱۰ میلیون
🥉
نفر سوم ۵ میلیون
🛫
…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65948" target="_blank">📅 21:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65946">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2x9eoQMuhIgJBHvYvWcqh3nLHSjY4QHkgvNUfHzloNTrjsAxpn7ctImTJq9Fmxove7TN_U-aAvKb9H7Obbb9ykrEsLmmDpvtegANJzOy823jVdQSRkno6qkLq0sDFAl5iLoNzn6y1PK_cqhZFhhE5k2l1wgs1M2PFKwvv6G9_iTF-qDJFhWpsMf3peglnAYVeA2-Mlm-AtR5lUSbBIzwr5TlKCdZjXMohghj0yFdSkwP0dBLrq4oxfDyszz0t3kkbxYFJH6BEWgsVruOz0BnHLbzriBVhcENF_73prwo6SW4MWpBSIYoCLT_ApOgkYs3HOGIHm08EEdYFEN-ruP0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
رایگان پیشبینی کن؛ جایزه ببر
🍸
درسته! کاملاً رایگان می‌تونید برنده بشید؛ فقط با پیش‌بینی بازی‌های فوتبال، بصورت کاملاااااا رایگان میتونید برنده جوایز ما باشید
💸
جوایز
هفتگی
پیشبینی رایگان
🥇
نفر اول ۱۵ میلیون
🥈
نفر دوم ۱۰ میلیون
🥉
نفر سوم ۵ میلیون
🛫
نفر چهارم تا هشتم ۲ میلیون میلیون
📈
۵ نفر از اعضا به قید قرعه ۲ میلیون
🏆
فقط پیش‌بینی کن و برنده شو
👇
➡️
@PishWin_Bot
➡️
@PishWin_Bot</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65946" target="_blank">📅 21:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65945">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e7da6863b.mp4?token=ZcdjxmGo3sOy3toEPDgz5sqYnwYDqeJOS7LamXukZ7MSUMxRo5MFNvFCqHdnPqEyAtXt6xZmuyz4j3ZM5VInHIi2KrZS2TYUrDf4C3MYrFGHP6urUCALRtTKWwiHxvYEoqfA3M_eqtvHX6lYi0KuvGElXl7zQbV7VtOb2I7Ce_WDwLPPZDllT8vH0IdLXAXaBhSAqx6XVJML61RPuS5X1VHSkt6A82cdaUePYeHrV_CF9U57mQ6BsmxU9x6-Un21T5cUhSf1l6KpI3s36-zJCP8RDc2DAqw_wMuozVa-kc31HEoBvJgV39SyiBmaY-dIw6JjmLWFSsS0fCB44Pl57Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e7da6863b.mp4?token=ZcdjxmGo3sOy3toEPDgz5sqYnwYDqeJOS7LamXukZ7MSUMxRo5MFNvFCqHdnPqEyAtXt6xZmuyz4j3ZM5VInHIi2KrZS2TYUrDf4C3MYrFGHP6urUCALRtTKWwiHxvYEoqfA3M_eqtvHX6lYi0KuvGElXl7zQbV7VtOb2I7Ce_WDwLPPZDllT8vH0IdLXAXaBhSAqx6XVJML61RPuS5X1VHSkt6A82cdaUePYeHrV_CF9U57mQ6BsmxU9x6-Un21T5cUhSf1l6KpI3s36-zJCP8RDc2DAqw_wMuozVa-kc31HEoBvJgV39SyiBmaY-dIw6JjmLWFSsS0fCB44Pl57Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شهباز شریف:   در بحبوحه تلاش‌های میانجیگری فشرده پاکستان، ما کاملاً از کمپین بی‌وقفه اطلاعات نادرست که توسط کسانی که می‌خواهند توافق صلح را خراب کنند، به راه افتاده است، آگاه هستیم. گذشته از این سر و صداها، می‌توانیم تأیید کنیم که متن نهایی و مورد توافق…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/65945" target="_blank">📅 20:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65944">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJQWaqxALB95Ne9yd2hbxhzQ1xWgeX0Rk6EqqJycJ_rbHVzvSRPm3s7Nkj2Srtp5I-mmbxr3cwXt2J9TwEsVx1djeVdToUuoz_KX5WpFCVnz-LdROoKTOtvLgcMglpuQLOjvA1ZnknnKjJJvVVqRuXS-smoS8vViFSHcG-xFGuNaNgKCy_9xEfaYKvxrP0_IwwnxTUEr7s4QF-mkvds7OfIhGdLh9lGxJ__AMv7-qpacNH1Wd2ZIzjZ-NhPkCT7QFPowFD60YsRsFeUFc9D8SXjd53VH-1m3bUfdZBXDXrkY8YUPWiA3W5ywPiaXTmLfnPp_LL5qGPmOlM-5JSIfdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شهباز شریف:
در بحبوحه تلاش‌های میانجیگری فشرده پاکستان، ما کاملاً از کمپین بی‌وقفه اطلاعات نادرست که توسط کسانی که می‌خواهند توافق صلح را خراب کنند، به راه افتاده است، آگاه هستیم. گذشته از این سر و صداها، می‌توانیم تأیید کنیم که متن نهایی و مورد توافق توافق صلح حاصل شده است و پاکستان اکنون از نزدیک با هر دو طرف برای نهایی کردن مراحل بعدی همکاری می‌کند. صلح هرگز تا این حد نزدیک نبوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65944" target="_blank">📅 20:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65943">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58b6a7c560.mp4?token=e5acVJByRyEilXg91gAFt9yieciSoZINJdO07UI_DU44Yfj88PsHfZRtTEez9CsX0wnh2CFz1vb1Zyouz6DFtPkAQJbOtS-V2ItWBQhDGcfy1LtbR51hO6zzdpFsoaUPvzOABfxE1nZVKS1XVO2XaT0meR8H4bywZipREHX76DtHIS2q_LAwTsY-bs4dlyEW2WneGnxdlFv813K1o2AoXZuxtinmN8JActTvR_bTydRR8dW4sNcki6vqek-ucKWXDMgSDF5-jxZE9yDkPmd4vQLiKvrS8UVPa1RSb8VzUmmTuusea5_CFgGoO-PgLeMJrlvnqZiKKvs5kdbmYDWQmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58b6a7c560.mp4?token=e5acVJByRyEilXg91gAFt9yieciSoZINJdO07UI_DU44Yfj88PsHfZRtTEez9CsX0wnh2CFz1vb1Zyouz6DFtPkAQJbOtS-V2ItWBQhDGcfy1LtbR51hO6zzdpFsoaUPvzOABfxE1nZVKS1XVO2XaT0meR8H4bywZipREHX76DtHIS2q_LAwTsY-bs4dlyEW2WneGnxdlFv813K1o2AoXZuxtinmN8JActTvR_bTydRR8dW4sNcki6vqek-ucKWXDMgSDF5-jxZE9yDkPmd4vQLiKvrS8UVPa1RSb8VzUmmTuusea5_CFgGoO-PgLeMJrlvnqZiKKvs5kdbmYDWQmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از مراسم دیشب افتتاحیه جام جهانی
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/65943" target="_blank">📅 20:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65942">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qb66NkEUMiFWyIZswHyfmkhCNS1jJOZU4kiXxnTTrK9MTWQXloNxwOVwTen_dectFGjWw3RZIjbHBKIZWgYX0VZsmOFx-FN5Hvz2GxqPnm0OchiUuUm7MgweWNITGJ3rIEBcVQUCIHaGoCKM7SsFfhhrl4g7a2PgvW_icDpPxH37Bvq4bi9KiP-a4N07WHO1EMjgVwCq8V4fpk8VZaZ_Mt7NnvIGz9nbdxxFIfz40bnmQNaXeTvyq4XGr2jfjeYsROyfiv0gbGBc1GAugLHbYuKJBpC9b0fkYKMHC7I3tLgXOFHyn3hxZtPJfUOEPMLYg5vMLXNq1bWQg1550oLpMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندزی گراهام:
ایده یک صندوق بازسازی ۳۰۰ میلیارد دلاری، با توجه به اینکه چه کسی مسئول ایران است، به نظر می‌رسد بی‌معنی باشد. این شبیه طرح مارشال برای آلمان با وجود نازی‌ها در قدرت خواهد بود. آن زمان این ایده خوبی نبود و هر صندوق بازسازی که به نفع این رژیم تروریستی باشد، اکنون ایده خوبی نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/65942" target="_blank">📅 20:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65941">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/65941" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/65941" target="_blank">📅 20:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65940">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBjeM_JsodClPklXX4WKZz7qDMdtFdjkHj8hcUQ_OxDordso0DbgzvMsciZZpw_oi9cgBa6fapBTJ4w6ZOC4cpufSDJeYhmu2OwKT6cW8gu8yDb1yg6rtcDs8jfR_tXR43Qvfq-0rM2jMjZnjUBc84JSu1jjGXJMjJUMNo87MhyW6pfELbJhO77Ld1mT-CLiRTdDV0_BfqgIet05yu7JtnkasS25DKWj5hzKkVKUAuBvIqmYBXhOO2TkXOFeyx1tOsJeOKQl7U1d6nNZhhws_PoH396ybKsfC39c2AOV3B7SrIqc0nJSjmiZ6fMY8QYE-T7wrK_Wao2W_YDIh3Xrqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/65940" target="_blank">📅 20:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65939">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiTIBSgs1NtZ4QASZfZcM5f9qp2VcWxN2yIClI9Ue6tzQEt9k7jGyboK4dQD2kD3yMaCeOggX3837M0NNtP847UCWyHZpEKaA0OVX5xOoy_sgpgSewZ1kfbfYdiCkDaemA339sAjM41fH0Azo6j4JbbN6HmMbwpwRtrfLJseQ1yzxZ0YWlacavV9jUsdOvZsbOPguFAwYMmKgiMiOPtzeI1xRT1FaL1YXmKj62StqDoSVRy1Np9GD-91HDe8w_985gC6-hGqgVqVNYQYqGR9tHVeB9GnZYMm_ntBf708fhQaMr-zpBuwss-nzCsf6hP5SaTnasdzcZ3L3qe5H7WDgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سنتکام:
ناوهای جنگی و دارایی های هوایی نیروی دریایی ایالات متحده همچنان به گشت زنی در آب های منطقه ای ادامه میدهند و محاصره علیه ایران را اجرا میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65939" target="_blank">📅 19:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65937">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f3347ca6.mp4?token=m_zFyUl2bgcoEUja93ADhuQPrVvNGXYU68e5UqG2k5_q8qSHdqHHMIkAysmisFdMfIlkGOmJumc3hm8xAcBRXmVLdlTlWYDYWyjl_GslULDm-ZeHs9XGae9cbtGgnjpYIBdGsuvSKhM505XQlFCNzUR9bjgvEYc7dQyx8gLNGaDI56v4SHPITdndFHhHjVl6yDXdotxwKRljNPHeIuzNGBiTJ0rMex0Mrw1eqUT9whXcvodQieRbSsei2jTMHZMO58i9-uZEpv4H2Kv41qjoYQybjeT7j6UwNbSpmGksCEe33lXpL9Cn59ERkHuRErDaIBjjjhOPmTSlilkPcIe8Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f3347ca6.mp4?token=m_zFyUl2bgcoEUja93ADhuQPrVvNGXYU68e5UqG2k5_q8qSHdqHHMIkAysmisFdMfIlkGOmJumc3hm8xAcBRXmVLdlTlWYDYWyjl_GslULDm-ZeHs9XGae9cbtGgnjpYIBdGsuvSKhM505XQlFCNzUR9bjgvEYc7dQyx8gLNGaDI56v4SHPITdndFHhHjVl6yDXdotxwKRljNPHeIuzNGBiTJ0rMex0Mrw1eqUT9whXcvodQieRbSsei2jTMHZMO58i9-uZEpv4H2Kv41qjoYQybjeT7j6UwNbSpmGksCEe33lXpL9Cn59ERkHuRErDaIBjjjhOPmTSlilkPcIe8Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی قبل از جنگ ۱۲ روزه و ۴۰ روزه:
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65937" target="_blank">📅 19:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65936">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3QqWVhBGr2TVjh_Hzqr1cltWW8kjwGyn4WpSHnLB5uN7DRIjHN0qKgB1h1dW4-dUgqSc5w9CJVlwM_nXbQX9rw49TKu5VlV-gO7V-YoE21DMksK4pqDAzfBNdupLk6rRts9OOwfpBzvmJ7lZ-zCFol72OwwT-24yzebqo2uS9Jnzw43NytGpJkEZGjSKupm10JF4WNUhBnIxD3v_wgziG0aL4DKHXpGWsVSzhtBP1Np5JKI7JZTJyFVUVRoNgDeMJ3tsqYYYvERMc4OS8JuBYhuNxnj39bQDac6No5LyHuBgxDTAhYb_pOTg16kklqU_RWUt4pBZApvoCTspNTQNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: تفاهم‌نامه اسلام‌آباد هرگز تا این حد نزدیک نبوده است. تا زمان نهایی شدن آن، رسانه‌ها باید از گمانه‌زنی در مورد محتوای آن خودداری کنند  @News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65936" target="_blank">📅 19:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65935">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
جی‌دی ونس:
اولاً، ایرانیان هیچ وجه نقدی دریافت نمی‌کنند و هیچ وجهی صرفاً برای امضای یک توافق یا حضور در یک جلسه آزاد نمی‌شود. این توافق به گونه‌ای طراحی شده است که نگرانی‌های ایالات متحده و متحدانش اولویت داشته باشد، و اگر جمهوری اسلامی ایران تعهدات خود را انجام دهد، فواید اقتصادی به آن‌ها و کل منطقه سرازیر خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65935" target="_blank">📅 18:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65934">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">تا دیدن اعصاب ترامپ تخمی شده عراقچی یه توییت زد گفت رسانه ها چیزی در مورد جزئیات توافق نگید :)))) #hjAly‌</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65934" target="_blank">📅 18:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65933">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
ترامپ:   شرایطی که ایران به رسانه‌های دروغگو فاش کرده است هیچ ارتباطی با شرایط توافق شده کتبی ندارد. آنچه گفتند، از جمله بیانیه ضعیف و تأسف‌بارشان درباره وجود توافق، هیچ ربطی به حقیقت ندارد. افرادی بسیار ناصادق در برخورد با آنها هستند. هیچ چیزی به نام…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65933" target="_blank">📅 18:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65931">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rTwjfhTb_PhLWxWVRpj90uLnBNDOVqko7QMxr4Xc4K-9gtd5E9hsNYPhRUYRZmuyeIl2kYKDBkx7K-FhreblW6uTpv4ZVx4W4zGYnGQrajB87g2EGyTslEs4WwwiujgwK0Xt210LcDkEOjvxklMQ87ZiCchQn0UvUQbiUvWaz2wHhx1R0zb__G4dL4TYj9TH4suYSUXhzmzcHtlO2igrbk32lWA9ltTxc938CBvLt02_R3SBQu5iSEDkD0E6HkDUyqkr6wEFPkjdEkucgmV-b9_83JxSJNk583Q36X8jS_FCgD7gR_eG8_hTVavQLjop_COslmqASqw9Plis8lKqZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IFPYGwowfR3K3Sfa5eeoxB22GBMCd6kVhor4CMpLF7MWTEcZoegIFLVrarBegOpJynV113cxbBoYijlNdL3DXLf62hN-Rak1UebP1Ept7-f538NWulLTDCu0Cj1TgiWb333UyNVvMEwCc_csO6AFxljZdnSFeFGUQxJsRI1XepVbOlP0i7hx7xmdl7v-2iKwLtlx_ixkWHH5T-S3NLo8ssu9rXDz9DyoHLJx-7YvJZAaHzvBYhZGmzNJzoDHKoLbVuh3woc9U8eHlsfvZWlyFnfz4li8DxzbfWumkeuCObzf1P81RFtsX2NyF_9-vWemJoQWzk2y__9d5wkRd6rVtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
برنامه امتحانات نهایی پایه های یازدهم و دوازدهم منتشر شد.
شروع امتحانات از ۱۳و۱۴تیر
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65931" target="_blank">📅 17:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65930">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81c65a1f96.mp4?token=rnoFg-lHlndpnSOM85pYVpqhoEHQ6LqRszExx_EGOA-oZ5-oMbAN_PN2RSJuowI8_-gHGF1g6wj6D2teF89Hjcl8O8bX2a8g8WMBEPUsrGrWHDV4JUPSse3alTaps4Xq2ZQfHsyu6JWS1ELl-1bM1ot8qsQFXazw7vUDxuwsMnhk7c3M03K9GCWfgVU0ObmmA1G_ujN7GB5jd4S-T6QuAaMDvBn1MND8WIIZZPI_rFvYlos0Kvq8OhQUAudod6HoRff6M2mG8ZZBGHCbuLPhFfksq3KKgnaHj6gCQE7HqU9GCoEdDiybQG53WRuM_D5Fh3tqPGTmpjEBeZchTDl2XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81c65a1f96.mp4?token=rnoFg-lHlndpnSOM85pYVpqhoEHQ6LqRszExx_EGOA-oZ5-oMbAN_PN2RSJuowI8_-gHGF1g6wj6D2teF89Hjcl8O8bX2a8g8WMBEPUsrGrWHDV4JUPSse3alTaps4Xq2ZQfHsyu6JWS1ELl-1bM1ot8qsQFXazw7vUDxuwsMnhk7c3M03K9GCWfgVU0ObmmA1G_ujN7GB5jd4S-T6QuAaMDvBn1MND8WIIZZPI_rFvYlos0Kvq8OhQUAudod6HoRff6M2mG8ZZBGHCbuLPhFfksq3KKgnaHj6gCQE7HqU9GCoEdDiybQG53WRuM_D5Fh3tqPGTmpjEBeZchTDl2XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین طهلیل ویدیویی بنده از شرایط خاص منطقه برای عزیزایی که تو دایرکت درخواست داشتن
🙏
🙏
🙏
#hjAly‌</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65930" target="_blank">📅 17:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65929">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6007e01a82.mp4?token=WZhfGncFnYvCCqeicy4ihoAVp1Ck1C7-Kjwuo1FhiX5et3rPThlxArCuENMAUNKFXrcafDI4TJTFt3IrEA08ooQmzY2bR4NT7Cde4KTu5cJ0MpIXnTvZiXVD0-cZxKMIsF6ny_017LaqCw7h5RX3yv5b_DU5psvkOQeuMEZcs-YM8uSVMoo7SMV-rDLFbvU33Z_EWyGr6Rdj0J3vJtr_6Rs4dCGBEgd5tJBbREzHutxUDOzLYWUrMil4v45C8UO4iqLipxsOa3SvF9wqFj7ROekCWLnukw0GUU5McVaxnrXejbIYEBzLL5s5Byd-CKUU4siqyXNuPiPbQhdYFm1i6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6007e01a82.mp4?token=WZhfGncFnYvCCqeicy4ihoAVp1Ck1C7-Kjwuo1FhiX5et3rPThlxArCuENMAUNKFXrcafDI4TJTFt3IrEA08ooQmzY2bR4NT7Cde4KTu5cJ0MpIXnTvZiXVD0-cZxKMIsF6ny_017LaqCw7h5RX3yv5b_DU5psvkOQeuMEZcs-YM8uSVMoo7SMV-rDLFbvU33Z_EWyGr6Rdj0J3vJtr_6Rs4dCGBEgd5tJBbREzHutxUDOzLYWUrMil4v45C8UO4iqLipxsOa3SvF9wqFj7ROekCWLnukw0GUU5McVaxnrXejbIYEBzLL5s5Byd-CKUU4siqyXNuPiPbQhdYFm1i6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی خامنه ای ۶سال قبل:
هیچ پیام مستقیمی برای ترامپ ندارم چون اون رو شایسته مبادله پیام هم نمیدونم.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65929" target="_blank">📅 17:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65928">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
ترامپ:   شرایطی که ایران به رسانه‌های دروغگو فاش کرده است هیچ ارتباطی با شرایط توافق شده کتبی ندارد. آنچه گفتند، از جمله بیانیه ضعیف و تأسف‌بارشان درباره وجود توافق، هیچ ربطی به حقیقت ندارد. افرادی بسیار ناصادق در برخورد با آنها هستند. هیچ چیزی به نام…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65928" target="_blank">📅 17:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65927">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‼️
ایرنامتنی رو منتشر کرده و گفته تفاهم نامه پایان جنگ دربرگیرنده این مسائل و موضوعات است:  ۱. موضوع هسته‌ای دست‌نخورده باقی می‌ماند هیچ توافقی در مورد پرونده هسته‌ای در تفاهم‌نامه فعلی انجام نمی‌شود و ایران هیچ تعهد جدیدی نمی‌دهد. گفت‌وگوهای هسته‌ای در مهلت…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65927" target="_blank">📅 17:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65926">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgAEHlkMtMQSiO5GjtRRiphqNZAJu328S9dy3cmWqWFcN73nnd-iA23vu0ApesNHweyivudqKoqqnzmp3UtTMlsJMM66ptYFK6LZP2T5abUWMyxSHmS802DWwhe1ezYncUQkbegGm9uwWjnNbKsUWLRUvXlaedbrgULhitbQaZ17p-JvSwDxNWryJTNqiHQh-I4Uh1sglxITJiHf1V-NSKNmPQ9HNL1qp8oRNWICyLvaqS_p7DYcClQcDh0QzEo9oXyggJLtxnwrHL5eOv027I5_DDNSiSXtGemtfmGPPxWP1pyoXwDNLuLT_PhcLcJyGUZol_F8Vdw1e3Jr_wc34A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پلاکاردی عجیب در تجمعات شبانه
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65926" target="_blank">📅 17:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65925">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzK8ulQZjBjIowIuykk5gYPtvuX91ykyZ3E16ExWieK98ulbdg2SPVYQTXBH23dIZRHwN5Aojcek-5nhu-0ftGKomt-Ac-m_NhFHWbKwQWphsPt3q9cau5X_gTBSotxM5fW3j_gVILa7UbkbDM7cuFn8OzWMCt8fPk4oE_-72bVBlU1zlEm3z6bE1n9SZdLMe4fhFSveK55MAvQ9vTq9X5JAZoirF7TaN5-zHV4PxubFstq3TuxpEC0U64CZYAAURSRtXOJwcZmFZO2xj-IzHz8ofreABxtENtXe6XvxyTXiy5XYV9CejfwlFXqI1A0ap1i0V2mqWB4RBc0sd-o9tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤡
ترامپ در سال 2049:
ایرانی‌ها هر لحظه ممکن است توافقی را امضا کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65925" target="_blank">📅 17:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65924">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCUmGU-MDbqY1izm5kEf5G5_dHJ9oIrtPRB7YFIQiJlUMXRgP-T7l41TXD9RCqEZKzSJurbgsM_kXG3Tb3HYUAGXPt1Fcv-6xm_uX_V5o5_AyD4QHcxOI-08unIeovKFSCCt6M3XXhh2E3i7LxeS5e6ZQ6z7Qhs7X96yEU75gVSRh7-1e41baCp8OhfByNai-kmKASixULboUhgs4_LGMnRBvBlbqe3yr1LdxBZ_nUaXpuJeGb5nj31uqa65nmkmonP8mQ92DrSyHxD98qKEly1A71HCYsJFUGtfn8rj_NzhPCkkrsj3iCKTSvCRMCygxbL-1fbmBZfD-621rbu8Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
مرندی، عضو تیم مذاکره‌کننده: یکشنبه در ژنو اتفاقی نمی‌افتد
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65924" target="_blank">📅 16:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65923">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f5e54d8d.mp4?token=pvDdPBgriB_r_Lm1wGpI-P7vaP-1llWhqbFigDXjJU2FGdiCmUZ7jjqTytGCEYPk6EB5PJu5Oamh8xeOhhvIkDO8migqTIRMreNxLcw-gfxoIH8boM5OMAOd4x-hbo0yQctkl2oBloNc2JX7n0XBKglib9uoilwZwGPiaBOjJtAi9dS2_pBHaPBJwbNM4L7ypX0QJXxLcebn_1oEpKgrrG4xLQFbI384jjkzKCPpf9zqIpn0nXhOp7sfnXVRDOqCJte-lVec0XGDz4JW72HMPjjtFEH6BXMUXMKmAs9yx9kIWxnAzlXRMiVnj9JtftNNwMYNxotfpzFUsiRZFLD7vXQexjd-zey967BwlzBDvXexusTYL-MUtdncCUpR4aiNEoN8JPs1L3sVLJvIOJRRqQ4dKD5tdmuC9dwRAvS6STHQXSNz6bhw-Bf92nfP2MP_rKKjGcCZ194R5QSLv9MFpQDx58aPQkvoBW2wkERznk9lI1_700XeDeaGHUzj7qqNPMmoaJQa0LFX7KU7soGFbsgOKYLFDxWDTrqrgy7jRUU16l0WqNhvrp4xPPjozmiEghKx1nve7KyAJhj-lOAXcPzUG9HIlaVW7y2o8LSRWBjYER_rkhMwDLa9jtgyJxijJ__wwtlAXnQXar3p3LH0iUXXOR1G0nBWTvHvuuTxrTc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f5e54d8d.mp4?token=pvDdPBgriB_r_Lm1wGpI-P7vaP-1llWhqbFigDXjJU2FGdiCmUZ7jjqTytGCEYPk6EB5PJu5Oamh8xeOhhvIkDO8migqTIRMreNxLcw-gfxoIH8boM5OMAOd4x-hbo0yQctkl2oBloNc2JX7n0XBKglib9uoilwZwGPiaBOjJtAi9dS2_pBHaPBJwbNM4L7ypX0QJXxLcebn_1oEpKgrrG4xLQFbI384jjkzKCPpf9zqIpn0nXhOp7sfnXVRDOqCJte-lVec0XGDz4JW72HMPjjtFEH6BXMUXMKmAs9yx9kIWxnAzlXRMiVnj9JtftNNwMYNxotfpzFUsiRZFLD7vXQexjd-zey967BwlzBDvXexusTYL-MUtdncCUpR4aiNEoN8JPs1L3sVLJvIOJRRqQ4dKD5tdmuC9dwRAvS6STHQXSNz6bhw-Bf92nfP2MP_rKKjGcCZ194R5QSLv9MFpQDx58aPQkvoBW2wkERznk9lI1_700XeDeaGHUzj7qqNPMmoaJQa0LFX7KU7soGFbsgOKYLFDxWDTrqrgy7jRUU16l0WqNhvrp4xPPjozmiEghKx1nve7KyAJhj-lOAXcPzUG9HIlaVW7y2o8LSRWBjYER_rkhMwDLa9jtgyJxijJ__wwtlAXnQXar3p3LH0iUXXOR1G0nBWTvHvuuTxrTc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هگست وزیر جنگ آمریکا امروز ۴۴تا پرس سینه زد
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65923" target="_blank">📅 15:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65922">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‼️
خاورمیانه در این مدت
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65922" target="_blank">📅 15:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65921">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‼️
ایرنامتنی رو منتشر کرده و گفته تفاهم نامه پایان جنگ دربرگیرنده این مسائل و موضوعات است:
۱. موضوع هسته‌ای دست‌نخورده باقی می‌ماند
هیچ توافقی در مورد پرونده هسته‌ای در تفاهم‌نامه فعلی انجام نمی‌شود و ایران هیچ تعهد جدیدی نمی‌دهد. گفت‌وگوهای هسته‌ای در مهلت ۶۰ روزه پس از امضا انجام خواهد شد.
۲. تنگه هرمز؛ نه واگذاری، نه نقش آمریکا
ایران هیچ تعهدی در مورد واگذاری مدیریت تنگه هرمز نمی‌دهد. آینده اداره تنگه در چارچوب یک امر منطقه‌ای و از طریق گفت‌وگو و تصمیم گیری مشترک تهران با عمان حل و فصل می‌شود.
۳. پایان قاطع جنگ در تمام جبهه‌ها، از جمله لبنان
هدف اصلی تفاهم‌نامه، پایان جنگ در تمامی جبهه‌های منطقه است. آمریکا تعهد می‌دهد که اسرائیل را وادار به پایان جنگ در لبنان کند و عبارت «تمدید آتش‌بس» در متن جایی ندارد.
۴. آزادی دارایی‌های مسدودشده با ساز و کار مشخص
بخشی از دارایی‌های مسدودشده بلافاصله پس از امضا و بقیه به تدریج در طول مذاکرات آزاد خواهند شد. تهران تضمین‌های روشنی بر اساس ساز و کارهای مورد نظر خود دریافت کرده است.
۵. غرامت جنگ در دستور کار
خسارات وارده به ایران در تجاوز آمریکا و اسرائیل از جمله موارد مورد اشاره در تفاهم‌نامه است. ساز و کار اجرایی دریافت غرامت در مذاکرات ۶۰ روزه پس از امضا مورد توافق قرار خواهد گرفت.
۶. جزییات رفع تحریم‌های اولیه و ثانویه؛
موضوع مورد بحث در توافق نهایی
رفع تمامی تحریم‌های آمریکا و قطعنامه‌های بین‌المللی در مهلت ۶۰ روزه مذاکرات هسته‌ای بررسی می‌شود.
۷. سه موضوع و ۶۰ روز برای توافق نهایی
در مذاکرات ۶۰ روزه تنها سه موضوع بررسی می‌شود: استمرار برنامه صلح‌آمیز هسته‌ای، رفع تحریم‌های یکجانبه آمریکا، و ساز و کار جبران خسارات. هیچ موضوع دیگری در از جمله توانمندی موشکی ایران، دستور کار نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65921" target="_blank">📅 14:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65920">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
سخنگوی وزارت خارجه:
متن توافق پایان درگیری میان ایران و آمریکا تقریبا نهایی شده و منتظر تایید نهادهای مربوطه هستیم.
متن نهایی تا زمان پذیرش قطعی آن توسط دو طرف منتشر نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65920" target="_blank">📅 14:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65918">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qcb0xse40QorFq4N2iHJ5HQ5ieZTWFBfvRmwaKLcFbHSmlhZM6upF8k7bspi2gkLvZgJS9nxzOOLORvyUYndKIxAIuE1B5xmz6HtpP2JXEzaUKLC3vqml1sTGnciBaamCLMYFuCCcJUMIrgOu1tj-VmK3lHJ9KujkgxSjtBsbiFeZYDGpwtKacayHnxQfXcuXgWaRvyVIpEoLDZEb7XQ4C7mwf5EZKQpbG8ek3msGOcYNiKHLB56joaIR07lOUhKCE66rTs4P6CeSNqfHM4znvU02z0Qx1nH7Vx6xYKBeh8K4JTcIIzWU6TorZfPk_h7Vw98biMMAsbVL0wVV3aWWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D_Cm5q5RuU0atMk1k6K38oYTDZ3NIwnpL3cwtcpG5nFBPkJrOsRMj-amPFjFy1cVGCxTszI7Rwn-kFmIaGmSw6eEKS20da3ZlHEin3tSM-zbv9nXTogV_rFNoXv1QFXfUT9ihWfQ3JJqNO_FtNcNAWFi9FnOvYDJ_N-4OnFI6UibQOChfg0XjeRCIWqs9-Blw16k2Zge21NuDgR1ZcsmLJIMzV17bbcoBhiS48Bxi52cEMCPqMtUEqqxBHxXzDM_q2mlU3k4Il5ZJ3l0m41Hh2oW4SXcstOwyeWtfdF2SXIwEv1_QdMHfpx-X8oAzb-nl_pHhXgRtUzaNPp81E-08A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تصویری که یک پرستوی نظام در تجمعات شبانه از خودش منتشر کرده درحالی که چاک سینش پیداست.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65918" target="_blank">📅 14:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65917">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5aed65f61d.mp4?token=VOlEfMrXts9LIqoMY1VP9TeJFkoTRO67JRd4pLSXCh2SU4WxVpw87wwqwMBV0j7jVSMsegd5XovOwWHNJzSVxrbMP8lds8QLQIUowQ6lmRh5g7OvqSC_mL7nA4SLlmyK0yN6eQ_ljlegw90l2q80gN-1v5yeutfh_tfLztGw1N-D-e2JwVoIPmmhwN7x99tN3ZHL4Jrq-71kTv9LpC3RxDRfQh6YI-kzoNEPKQeaKp4sWAroTpKa3_TOu2yiSeY_e1VPWr4W44AloWu96X-JBUozNo5w0iTEA1AjCIaJMKOMkT-DTldnJzxEFY8i-sDgZlYA2ff77aoyARD8VXZ4Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5aed65f61d.mp4?token=VOlEfMrXts9LIqoMY1VP9TeJFkoTRO67JRd4pLSXCh2SU4WxVpw87wwqwMBV0j7jVSMsegd5XovOwWHNJzSVxrbMP8lds8QLQIUowQ6lmRh5g7OvqSC_mL7nA4SLlmyK0yN6eQ_ljlegw90l2q80gN-1v5yeutfh_tfLztGw1N-D-e2JwVoIPmmhwN7x99tN3ZHL4Jrq-71kTv9LpC3RxDRfQh6YI-kzoNEPKQeaKp4sWAroTpKa3_TOu2yiSeY_e1VPWr4W44AloWu96X-JBUozNo5w0iTEA1AjCIaJMKOMkT-DTldnJzxEFY8i-sDgZlYA2ff77aoyARD8VXZ4Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
وزیر ارتباطات: بستن اینترنت امنیت نمی‌آورد. وقتی اینترنت قطع بود، وزیر اطلاعات، لاریجانی، رییس اطلاعات سپاه و بقیه ترور شدند. با بستن اینترنت، جوانان نخبه مهاجرت می‌کنند و این ضد امنیتی است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65917" target="_blank">📅 13:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65916">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‼️
ترامپ از زمان شروع جنگ ۳۹بار گفته با جمهوری اسلامی به توافق میرسه
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65916" target="_blank">📅 13:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65915">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30551bbbff.mp4?token=n7W_PfrhbwAhrv8uS6dLCqsjGo6g-KrVNLVK8eE_9Jf3npBZ_CwZ-BxMEB6XgAl3EhntM5PK2tEFcyv_RfGpI0BRnhRXoHAjp1ahTgaRmM2DCA0AUfwbacF7FQSUtkG50UaMpkGxbA5QepAibm2xEYVSRw0LUYGbvsQ1zKJXLCSrJrtYurYZZaLNOFNGNWJQoByRXIfERfV5D41IFE-4TXaBzTqMXXQo5YIqy5qUbM9HvFNLKd8ZxINTQo23-F5ZBDlSuwtNY_rSskI5H-OOaEZKd-4M4oBDGVSBBILCJu9fjvtGszUSU1SLPT-29ar1eyANUlgmP4s4r0LWbbeTaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30551bbbff.mp4?token=n7W_PfrhbwAhrv8uS6dLCqsjGo6g-KrVNLVK8eE_9Jf3npBZ_CwZ-BxMEB6XgAl3EhntM5PK2tEFcyv_RfGpI0BRnhRXoHAjp1ahTgaRmM2DCA0AUfwbacF7FQSUtkG50UaMpkGxbA5QepAibm2xEYVSRw0LUYGbvsQ1zKJXLCSrJrtYurYZZaLNOFNGNWJQoByRXIfERfV5D41IFE-4TXaBzTqMXXQo5YIqy5qUbM9HvFNLKd8ZxINTQo23-F5ZBDlSuwtNY_rSskI5H-OOaEZKd-4M4oBDGVSBBILCJu9fjvtGszUSU1SLPT-29ar1eyANUlgmP4s4r0LWbbeTaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت آتش بس در خاورمیانه:
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65915" target="_blank">📅 13:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65914">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/65914" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65914" target="_blank">📅 13:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65913">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=nd7M_plJKc-He49yhCKRLen0TBk2h77ZKgu6MBXULTrc9YzmRE1LuVXLxq31__I5Pn_9oKnWTuWrLVJUINpjrRMrDGh4jjXgreSvulluPt0dsToFpHiXpNgpSBDz6EAtGr8cy1UYDJ-b6Y1EBcDs7bkqBEBpRamBYcrqAC2H3KmFRstxE9BpZIRwIU--nCVcIsw_I0BeVvBAEzA0gX-xN7m6v6YD5gkJIhzfL5xnYkK4Ib6IcnAsZ-1MlJfs5QoC7Et8HO8JZAkMeFYCINNwN6TPH1L4op-jCaBFpjwOXUYTbF9NerRT5oCOJtf5kHgWQipIKvdfJTXMvbyL4OXjwWn6em5RmY7hdwfbtULhByWCoP3qDPX0gyI782ijApXrZx-wwpVG4GEc54AHeTejOjITbIYApGj6xrBKcRU-I7ou1Ekh51e3ykbJeY8NmWRvL1ILHLDvLJEQH2xnyyzCIZE8bkjQd94qWAa-rdqQsEdHoLjS7HWtxkrz07GcbWpS5RXKeHH5-Po-PWPJVKcV0H6bEKemlsB0j9IbjpEWtRLFQ_WDKSCCxBdBtSt3rgcEh9o0pZPN5cvBkqm-6-0tYLSp8Kr2GXWE5kEwzz2geE-GgV2WUP1JRs8XgURVws7Pqa2RUZhYKnp25B7hShHFjYVOpwJHfRbzln8aZCH_9gI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=nd7M_plJKc-He49yhCKRLen0TBk2h77ZKgu6MBXULTrc9YzmRE1LuVXLxq31__I5Pn_9oKnWTuWrLVJUINpjrRMrDGh4jjXgreSvulluPt0dsToFpHiXpNgpSBDz6EAtGr8cy1UYDJ-b6Y1EBcDs7bkqBEBpRamBYcrqAC2H3KmFRstxE9BpZIRwIU--nCVcIsw_I0BeVvBAEzA0gX-xN7m6v6YD5gkJIhzfL5xnYkK4Ib6IcnAsZ-1MlJfs5QoC7Et8HO8JZAkMeFYCINNwN6TPH1L4op-jCaBFpjwOXUYTbF9NerRT5oCOJtf5kHgWQipIKvdfJTXMvbyL4OXjwWn6em5RmY7hdwfbtULhByWCoP3qDPX0gyI782ijApXrZx-wwpVG4GEc54AHeTejOjITbIYApGj6xrBKcRU-I7ou1Ekh51e3ykbJeY8NmWRvL1ILHLDvLJEQH2xnyyzCIZE8bkjQd94qWAa-rdqQsEdHoLjS7HWtxkrz07GcbWpS5RXKeHH5-Po-PWPJVKcV0H6bEKemlsB0j9IbjpEWtRLFQ_WDKSCCxBdBtSt3rgcEh9o0pZPN5cvBkqm-6-0tYLSp8Kr2GXWE5kEwzz2geE-GgV2WUP1JRs8XgURVws7Pqa2RUZhYKnp25B7hShHFjYVOpwJHfRbzln8aZCH_9gI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65913" target="_blank">📅 13:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65912">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
کانال۱۲اسرائیل:
مذاکرات نهایی آمریکا و جمهوری اسلامی در مورد برنامه هسته ای و مسائل اقتصادی است و برنامه موشکی در آن جایی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65912" target="_blank">📅 12:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65911">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
یه‌یارو بیکاری بلند شده تمام اسکناس‌های کشورای مختلف دنیا رو جمع کرده و باهاش ویدیو ساخته.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65911" target="_blank">📅 12:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65910">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
رهبران قطر،امارات و پاکستان کسانی بودند که مانع حمله دیروز ترامپ به ایران شدند.
سران این کشور ها به ترامپ وعده دادند که توافقی اولیه با جمهوری اسلامی دردسترس است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65910" target="_blank">📅 12:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65909">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9247426e69.mp4?token=Lz4uKp6jLNeaViExsHsFoj4gtc570XvZpq6ddbAYQDDmEBI7wK9ycrVoMqen22cvG3UFKCxOqKuo-aMbm_e46GjiSz5g8ko2PwwYcPK8TJS-AiekBqwKEKLzHXpnv6MO4CHbZQPnnK_DrYsvIXDrTJr5mrIgVTcVhe6Mje4rtN0GHmTCnmquALyvf2uPF--pIm1kvsT38qkX3l-C-iA91el7XHrZZpVi4r41Wd_HW1pmAAQbySmgQsmIiIqV5Dz6jSHInB8txXHrsEjFVVMREevfp3KzIMPzSog-Tx6npPTjLiNnCm1id2xAdRYiBTvEuGWMC52b796UVoe1VIgavQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9247426e69.mp4?token=Lz4uKp6jLNeaViExsHsFoj4gtc570XvZpq6ddbAYQDDmEBI7wK9ycrVoMqen22cvG3UFKCxOqKuo-aMbm_e46GjiSz5g8ko2PwwYcPK8TJS-AiekBqwKEKLzHXpnv6MO4CHbZQPnnK_DrYsvIXDrTJr5mrIgVTcVhe6Mje4rtN0GHmTCnmquALyvf2uPF--pIm1kvsT38qkX3l-C-iA91el7XHrZZpVi4r41Wd_HW1pmAAQbySmgQsmIiIqV5Dz6jSHInB8txXHrsEjFVVMREevfp3KzIMPzSog-Tx6npPTjLiNnCm1id2xAdRYiBTvEuGWMC52b796UVoe1VIgavQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو یکی از کشورهای آمریکایی پلیس به یه زن مشکوک میشه که ازش اسلحه بگیره. تهش طی تحقیقات زیاد متوجه میشن اسلحه رو تو واژن خودش مخفی کرده و با تهدید پلیس مجبور‌ به تحویل میشه
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65909" target="_blank">📅 11:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65908">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
خبرگزاری حکومتی مهر:
جزئیات جدید از پیش‌نویس تفاهمنامه ۱۴ ماده ای ایران و آمریکا
جزئیات جدید از پیش‌نویس تفاهمنامه ۱۴ ماده ای ایران و آمریکا منتشر شد. این تفاهم شامل تعهد آمریکا به رفع تحریم ها، خروج نیروهایش از اطراف ایران، رفع محاصره دریایی، بازگشایی تنگه هرمز، لغو تحریم های نفتی، و پول های بلوکه شده ایران است.  آمریکا موظف است طرح بازسازی اقتصاد ایران را ارائه دهد و در حالی مذاکره نهایی میان دو کشور باید در مسایل هسته ای و اقتصادی انجام شود، بدون بحث درباره برنامه موشکی ایران. این پیش‌نویس نیازمند نهایی شدن در نهادهای مربوطه است
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65908" target="_blank">📅 11:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65907">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
باراک راوید:
یک دیپلمات از یکی از کشورهای میانجی که بندهای متن فعلی را با من بررسی کرد، گفت که «ایالات متحده و ایران در مورد متن توافق به توافق رسیده‌اند»، اما اذعان کرد که هنوز تأیید نهایی لازم است. با این حال، هواپیماهای نیروی هوایی ایالات متحده دیشب با تجهیزاتی به مقصد اروپا به پرواز درآمدند تا برای احتمال سفر معاون رئیس جمهور ونس به مراسم امضای توافق در ژنو در روزهای آینده آماده شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65907" target="_blank">📅 10:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65906">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
⭕️
توافق قریب‌الوقوع جمهوری اسلامی و آمریکا بزودی در ژنو امضا خواهد شد و به‌نام توافق "اسلام‌آباد" نامگذاری می‌شود. طی این توافق یک آتش‌بس ۶۰ روزه که لبنان هم شامل شود، شکل گرفته و ایران می‌تواند با پول‌های بلوکه‌شده خود کالاهای بشردوستانه تهیه کند
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65906" target="_blank">📅 10:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65905">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/215d29fff2.mp4?token=Ugi3HOQAasdoyjLy04bKQ7PhorJPGlcv3csCHKcPy5tnTJBui24fCAOLklnjYLNsMH7bE_Vl1YQFpm46UV9iQ9d695sKQauRH58MsE9S9ghGkuifF-BflFkicPxPt0yGWSwmc7eE1-jZ-_A8j5XDdxV8U0qj-8L2CfNQc1RBtK4e3es2zqscWS5NmnL42lCPvYh5a-97WnZP6dc7lRSEHDglkVm5E4z4CpBlxgqqgTbHW2Y8YUh231iJwFVf7dCme5wIYgjp1mZYWgSP9ERTdpk6oe_Ee1h7Q0db8vLUPcSwJquDnAQZObU3EIGSFUnqrgy7Pqtk1GT7xZiUbgl8nFItSCSApHnxDinxsMoLzvZQhD0oV5amRgiRCfE3c2n0004HLoAqkVGRdVi2JJfK3CFAsaNIUuPlMelYkGq1rLgj37UFCu4a5YHjWEA-hgJW8eiwN9xalXfdT3mw3_Z_TxDbuTlWew8g1T73sRo_FgusujbeeBX8G7e1mFKyT4-RuYIOsk0OgsiFsmLHXopkRPr2iRDYZWaErWW_B19jryxdN4LVIPdpd5sewt0nBAcvytRR3rR9IehUIRGbNK7p4eMWZrl3_6mXNQFlcaRqWsn8SPgeELO8RvfOAqouzg6mQYsdB2UK7ZAtmlgmlISd-XFaIQu-hynJGaBMr5QoLJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/215d29fff2.mp4?token=Ugi3HOQAasdoyjLy04bKQ7PhorJPGlcv3csCHKcPy5tnTJBui24fCAOLklnjYLNsMH7bE_Vl1YQFpm46UV9iQ9d695sKQauRH58MsE9S9ghGkuifF-BflFkicPxPt0yGWSwmc7eE1-jZ-_A8j5XDdxV8U0qj-8L2CfNQc1RBtK4e3es2zqscWS5NmnL42lCPvYh5a-97WnZP6dc7lRSEHDglkVm5E4z4CpBlxgqqgTbHW2Y8YUh231iJwFVf7dCme5wIYgjp1mZYWgSP9ERTdpk6oe_Ee1h7Q0db8vLUPcSwJquDnAQZObU3EIGSFUnqrgy7Pqtk1GT7xZiUbgl8nFItSCSApHnxDinxsMoLzvZQhD0oV5amRgiRCfE3c2n0004HLoAqkVGRdVi2JJfK3CFAsaNIUuPlMelYkGq1rLgj37UFCu4a5YHjWEA-hgJW8eiwN9xalXfdT3mw3_Z_TxDbuTlWew8g1T73sRo_FgusujbeeBX8G7e1mFKyT4-RuYIOsk0OgsiFsmLHXopkRPr2iRDYZWaErWW_B19jryxdN4LVIPdpd5sewt0nBAcvytRR3rR9IehUIRGbNK7p4eMWZrl3_6mXNQFlcaRqWsn8SPgeELO8RvfOAqouzg6mQYsdB2UK7ZAtmlgmlISd-XFaIQu-hynJGaBMr5QoLJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس شبکه خبر:
با صراحت میگویم بخش عمده ای از شروط ده‌گانه در توافق وجود ندارد
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65905" target="_blank">📅 09:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65904">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e6afe375b.mp4?token=ioKyXKhdQnRzHg0V2gGcbv91R83YqSRuUZmyUNx_mJDv5vaxGaH23hy-tZZLSIIJzWbkVzA3cxgIzxugKW-UtoCEfXRnzVxUzN_sRwiwu9rAYyf44VNN6DuS75D8FcG_j9oKkEUhzBSbdc55uoMIPdl8A2HrKDMYfCX8cd0EKpBHinHWmIXdUOgnvy_2pJ_mm-4ONxcNepW7x6DN9-IW_4V0CaMTjF91ciBL15D3NEpIreBg6AsGT4QUZn3VnYcVDFTzxy7EaO1HD0OoFxlignLj-c3pseU_rV25KuUkFGHwYvulnbNfINCUpxhSkKQoCp9e4OigCiiuax7FCSJ2Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e6afe375b.mp4?token=ioKyXKhdQnRzHg0V2gGcbv91R83YqSRuUZmyUNx_mJDv5vaxGaH23hy-tZZLSIIJzWbkVzA3cxgIzxugKW-UtoCEfXRnzVxUzN_sRwiwu9rAYyf44VNN6DuS75D8FcG_j9oKkEUhzBSbdc55uoMIPdl8A2HrKDMYfCX8cd0EKpBHinHWmIXdUOgnvy_2pJ_mm-4ONxcNepW7x6DN9-IW_4V0CaMTjF91ciBL15D3NEpIreBg6AsGT4QUZn3VnYcVDFTzxy7EaO1HD0OoFxlignLj-c3pseU_rV25KuUkFGHwYvulnbNfINCUpxhSkKQoCp9e4OigCiiuax7FCSJ2Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گفته شده ترامپ بعد دیدن این ویدیو تصمیم گرفته که توافق کنه
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65904" target="_blank">📅 09:02 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

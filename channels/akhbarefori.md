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
<img src="https://cdn4.telesco.pe/file/hEaXEPqc5wZqFPvjE-PWQZLCCoG971HU_uIZWBgIUvSaPQjXfSfxd5voGELwPsmwWUBUcD2_qNDlDUMA_BVxF1d4_DapZzp3o4OHNIKClJlyO2oAa-lrDaEnQxxs6KP7mBd6_n6zsdadpu0RqxfdjlO1IbwABunwyIkzEw57FQu0F2s2-6gc3wTOMT0YF6MvT-H3kQUifopxsWE3qli7sjwn3-49C89Y1sxyBnbIY4qBcXW0yjOZUM6FSD3wmxIYsYmMwWdRaUhcA59ERwoyO2ArOAegUNk0O-oJ9JUSwA07KNuvdjDbaY2sEiyaGBC6shcGJ1m_eZ_EdSwHMTDKXQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.11M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 19:04:48</div>
<hr>

<div class="tg-post" id="msg-677030">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e611bb25cf.mp4?token=fByaTUE8us2H4Vost_mGhpKS5uhBTvOEKxJLr5I6rtDUi2SIeh4gI-PL_p8TE0wO_pWKAm3fC1IrU8GRKlBgZiDF2PkMEEgyevWCyOIwQM0w8VbDyLNb1LhZEBo2H7lX7QHfM6-mfLlO5tOCliX0RMKsR-fr0It6HRJrzl5V3jiAmiOs1UmRssoM7WsjabiqGhdPvxWW43dbPqbvGHeEeM3r1P3pHzsXNI7SxnWuwo4eYu5cvYR1PbAu5lXP4c8NpH3npkXrFSF7f_f6grh4VdHAv0feBHlnYxQysKYvM6irP7ncZunJGm_xgn5LHMg7cWlb6S1IEIY4AHMbDSxHBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e611bb25cf.mp4?token=fByaTUE8us2H4Vost_mGhpKS5uhBTvOEKxJLr5I6rtDUi2SIeh4gI-PL_p8TE0wO_pWKAm3fC1IrU8GRKlBgZiDF2PkMEEgyevWCyOIwQM0w8VbDyLNb1LhZEBo2H7lX7QHfM6-mfLlO5tOCliX0RMKsR-fr0It6HRJrzl5V3jiAmiOs1UmRssoM7WsjabiqGhdPvxWW43dbPqbvGHeEeM3r1P3pHzsXNI7SxnWuwo4eYu5cvYR1PbAu5lXP4c8NpH3npkXrFSF7f_f6grh4VdHAv0feBHlnYxQysKYvM6irP7ncZunJGm_xgn5LHMg7cWlb6S1IEIY4AHMbDSxHBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای بین‌الحرمین در ایام باقی مانده به اربعین حسینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/677030" target="_blank">📅 19:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677029">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQE1Tol6quSA5AS43C8pOEk2kta0NUYTFXt1K7zjIY3RK6cTIZ2eoKVsN12--gixlL9xIPinJOvHvVnHpNVpvSRuqdSr3G5uAyo8mcHfcFgcSVZHCq_-oDBZgsK1FfGplGOchY5HAZFwBmm3bgKoGolcKFIq2XG_tiyrbB-r8tyP0v6QBNime2hY7gwkTgoJKyw3BlDcCMZVInQBWd6DoPCP90oYSzgY6j4g-9fVKnmF8YOwXHpsDT05uFyN_ejFQJHyMHiFterhoGgmMXoIgwNiw5DklJKB5YnGXmgeVQLJToYjuBqaUogiCMfpWn7J_VKIo4IZlr59CoXfdSWOHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ذخایر موشک‌های رهگیر پاتریوت آمریکا در طول جنگ ایران حدود ۶۵ درصد کاهش یافت
ادعای ای‌بی‌سی نیوز:
🔹
ذخایر رهگیرهای پاتریوت آمریکا که پیش از این ۵۵ درصد کاهش یافته بود، حالا ۱۰ درصد دیگر هم کاهش یافته است.
🔹
طبق گزارش CSIS، آمریکا سالانه ۱۸۳ فروند از این موشک‌های رهگیر تولید می‌کند و حدود ۳.۵ سال از زمان می‌برد تا دوباره آنها را بسازد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/akhbarefori/677029" target="_blank">📅 19:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677028">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزرای خارجه ایران و انگلیس بصورت تلفنی گفتگو کردند.
🔹
هادی العامری: قطعا انتقام خون شهدایمان را می‌گیریم.
🔹
مسئول سیاست خارجی اروپا: اسرائیل مجبور به عقب‌نشینی از غزه خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/akhbarefori/677028" target="_blank">📅 18:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677021">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RybMGNqpYhHxuFWxKrBjcZzr3QvwrDgaOFSEWXaJ8yS41mA8PaPoeFDoZY2XaXJ7OkHAn-K4V3myfTzby9n1_cdfr6AhgVJUb_5EE8B4zyNxliK1n5Kzr6lqfz0TsLlDwyZwXhwyHbaIJPR2xocLG4T5OqWRaKiYyAUNCwHtivEM0niegxfDYMt5DQP_Z0LiDhtqYYouLbYCB_3rMHaMOko-ndxGS63agozTwPO5VC-7WsEzdB8jAqWwCf0o5Ej8VNKxFdss8FEdLQUUO_Rre-1t-l8VRqxVbuZ8RFSdHG7tvucpcGTT5Mn-aqfcBbRZDiMu5mJzZjZBIqlyiuzXPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BmDSA_EQTkfUCXpOAGdQTCFl7CtslZf8dcyx9K3j3TnBpyE9RNPQMRtGqEzcvxNFnZU0M4AwaNPHq07bfFUz3-ZRZLKG2MMy3n24YwmpHg18EMg5M9wfwMQOMxBSi_o7DJoZEF34tsiPoWxwJpf-ilUIjispZpsAPGWhyHNqwW7xTjcGnbIvkGYPRicHG4cqDTVU9jTH2L6Dfue3l5f-otBxRUlIEGMvr5l4GwClDNavfuyhI574933IFNArXo_LguCGcd-XLnKAM7Prx4ulS4v7dPigQFhN8g4G909lqoYJofOgtCJJKsZT_fNNa2LF1y4f-GKnaUWNL-VZGfrwlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/avk6PhC96YJ1_k1suQLPL6pGkOwbDMZCkDdrENBFliSZg-9Y4zARp2NqA_3n8L0Kfs8iUYD3Cw5Mgd7A-xYFY6YRbMFp2Rht5gApPgYiecxRaKsTBIB-ODfh32XoifqUjLTmgKqfbMOHcNUOMsh_Xwf-XG7VEZ2XPXPNZ-NmMCf_TCWH5aFCD2LOaZ4DBfooFo-Nhkpxgw68Ux0mK5wUqmbHbMdfkVXbc0_RADEA9bfsJeeLCP9RY6PK_uQ3QyKZZ2yyIIcpcpZMYTBjeveY8H7alrcHth8SMDJ6cP3n1Q8Glq_yUhuyLZrhuH2qCOGZ020afEGnEKnfmVnmZcHNqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gWMWFdQ0ZJ87EeLRLGaD2ACZG8hnFhkLEMoMwttslkERsCaN5-HoGJjdVEvd5bfOWupVevQ0kwljXVI26ikJqg46v2T4wLpXfg_5r45cfsJWAlvN9wRbNDuVeb-egcU3wE1QBtQnCEYGXX3O7aIwVc29CFBW0qRNmMzLQHH_u82xe5MOjWsDxS38X6R4D8T4epVqWYMXZfIj1xcFU5hTateGp-ynkJkm1VEOMVbXQOqwbghC09Y7YAZK-Oc8FqWqg5ELD4To51qXG6Cek5pShEDAid_EXyVIyLOE9cw5WxaUXC636e3gZIFbej3D-2Rwya4Rp_JvgGJaaxhq09wkTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VwzxEVIvxZfJEdmNfrUNz2dVbkjosN-HJ7EhDQfiOSy2tOO8DZH93p3WouUPY9kYxO-DkAjLrh_yJfQ7mPLXhZV6bmieL6iwYGSzUZ3hD4ctDs8Oa4SI20A64_-BR5LvA0EqPkLuydIt64hOjteiPresvD2qb6FxS3m6TfoWI9WEGx_SvFfWrxkuZxigW3iOVSpwZF5UA7-GXO5VN3_68Dh4YfpNvfOGEaunGELv7Ur7LY6z_cu-stsozTLJypL7N42MoPA8IQtb-SKDmWIn0jyuZe6xJ9WGNtSUvNn_WEh1xmPHeYazR3gomuxeZMNHDOx_wvPu79smOyJz8vQCyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TaRjVfNuGZ_whw3vGHxnYZzWvwqbNNzvxYoXzWP6LRzehZmFkEA3ywDy69LQr3v-HeDG4kWG03RHNvMGhFje2VLhTW5gNMnfRUzQnJIWkNJ8VW5FHmc3CoG5CtNhPTy51nFHfIdXxTcZwGU4tIOFjX_vaCmVZFYLPboCHNRWUMuH4QPbf6Td-CcfP44To7H55CD_drAWKaEGcugZhLQTDYW4YzIFCy1hkkO1RQGB1g2JK1zU5M1FKHyGOwV3PJzoU7553n7fA47XrgIrS-a87LmwrNxfCXYL8vAGKsR4r-yVLxrNyChYD9u2FZgAAOBBzo0Ypd1enYiWv87pNkkH1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kNpMXqKxIP1Ycpqz11CT-twQPmN2F2cjzLhyn7iwHOT6qf3rZABCmnfb6x5AkXugZEtG7tERo8eCDeG_ohUmKF6LIRUr9_q0Q_KFoRJGywq-NeSugmpVkPw6MpSHUdLDW1HhEtxsmUasNke8UIUfmFFrYmPj-hUOqasx8sY-jig2GWX8GV_deCnDuj1xQTe0gdNlr64zh-tq2jFTLq0dm-U-wQh8OQhdYWUJwnJt3e9vsuIURCBm55teDl_MQD8WoyqMfJ2RIRZmPy56v7Er-dCScONX_qNvQHL6oFiDR2dU6xC3y5f63x3wPR8Y8H4O6LaC7KJtiJADuVGg-FYCZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
اربعین یعنی کنار هم بودن…
یعنی حواسمان به آدم‌های اطرافمان هم باشد
یک قدم برای تمیزی مسیر، یک جرعه آب برای یک خسته، یک کمک کوچک برای یک زائر…
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/akhbarefori/677021" target="_blank">📅 18:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677020">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
اوکراین: علاقه‌ای به جنگ با ایران نداریم
اولگا استفانیشین سفیر اوکراین در آمریکا در گفتگو با یو‌اس‌ای تودی:
🔹
رهبران کیف با حمله پهپادی اخیر خود به یک کشتی ایرانی «شطرنج» بازی نمی‌کنند
ما هیچ علاقه‌ای به تبدیل مناقشه خود با روسیه به یک جنگ جهانی گسترده‌تر در خاورمیانه نداریم.
🔹
‌«رئیس‌جمهور من، فقط به توقف جنگ در کشورم اهمیت می‌دهد.»/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/akhbarefori/677020" target="_blank">📅 18:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677015">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gp1dpDEXVWnnbMAa-MiJhi8hHmEKhJLoU670w8TPIcRwf0zGggYTxY2o6P0pBufL997A_UuAOwf0bi3cWTvR09Waa5Tf_61pXw2EKK9dc1wMI5nd8cI3iGO-7ftcjFEYmscBTrCAoTKalqlBH7hiGcbig0ATIJCmyznUB5AmGAbvfE2Te4tPEndofNYXd5eMwaVhQTjwqGqNAwTmte7nziD9ZPTE5l0TrguAzHGb10qMWoWSNMRFicVvDzIF1vLsRdSMdJEWHHZsMtxissTMMbGNGVDS0SYpgmB29VWALAH-9QxnCLLMnlWMlETfSqjnhsJwLuJI9oXRQCcFAiniWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YCXDyIioQIueWjbEa-GjZEsVOBGecgl7TAWy6H1PSTgb4LxGFPrW7aO-oRyYzhJTXhJOsT7fKgfGHzLWAQaTgkvQsXMa4qzthsdiRKRq559zQ7e0Sz7VZOb1Likzh-Y8PpcUE7XxsTPg6eVqRebImPZUwGaTTBvxV9u3t-bDw9ESoDyrzj4f1N68Tk57TlluiSqy7lw-rBg5vQHAJay4W0p-jorEEfOo3Xd0s8QOD7T6ybRo_ygB3LlJCzX-u_m4eggkVwJ19hQ3iBse7O9QQKRg1n_upP-8YsEWGDFj_MtYAsTkYQx6HP2CA5hWMGRXyXQkwWRvXgNpkE2XCIqtlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tc9eu7m2dp_es4xKqnIENkxuOElzxElWBw0WVpiL3HuTrCHJMy9XU0rs8-Fj4g-JSF7nkLvZZP8Wv1S42Tcup1xRGK9PTa7TQUudX3N_eBydSR-06iSmRzgKPigcdvN95pblnEtSFunmhWevoLJhJbBb1fCnYoKk0lWDfIsj1jxkIk82H45Y5iJt1H3lpat_CpmIQVD6rpzrEHZjnxTyEhdM4p2G4HyecR4FXO7kaDHjXlb8cGTR9mPMqu-7bfZ_83FBOrlUeoejq33B1wXL32UA7aS0D1V825gdQY6lRuVcAm5Sv6XzzEn5LBtxaTT34SanUNDZTV7PiOnI0My8aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gkjnVqvFpp5-7E57b5L74iHGEbeXCRQNRAV7RyAaAhb36KXlHirddv9bRurhCCip1l2VMUVOORVpLXmSm_TmE0VAFrlzHpg34SMp__34RhuSKtvkI2mqgRt2f5L_92ht9ZrQImzed6_PYFvoj1LTne1vWGlvLhkaQnG73tUqFL3TGxVeCiT3L7t3wmEeMTOLmBmV2BFLWAewjhMtBTObVhaLrc3OuikiVp03BYobdWG766fWbY4wVxV8UaU7LgXvWDlG-BfDhzPU87MbPMdzqh0-3oVDpmUkrT8PEcLDT6LW1nRYwVgMYYQrLsW5kjWHwoAuD2yJpQbPg0bO46g92A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VBZEm3xoZGtYIpMh78Hbbbu_1peXkwMb0oCRRRTkFf53uQ7OOaPzoW4hd0ZJ8snpSliFfPiOkvFdHgi_NE1O0sPL-kc-mYASLc-Rq3r5hfHLXtngwS3D5k94jef28auOAXyAzR7Op1cHlZJxXXGZlGwEH1JAj4gsUjatJdOXRxLqojtKsSCQW_XT07U-o4Nt10lPv7-6QYxB66Sn7WAmJgCNC7a1q-dWSDI37SPmI_CCYGdWOiF7NwJsvk90j6rGbBCjecaR5WC19ntGmvbedyFLZ1NDLtEriDyQS3Rb9rIGRRkUZ_6pLr4ws25OchEcc9MZhFLMsw8SRyNehq94-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۵ نوع پاستیل خونگی و خوشمزه
🍡
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/akhbarefori/677015" target="_blank">📅 18:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677014">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0efd09904.mp4?token=BL_hoPme2lwF86spVsghxKRAFZuzLBvjGEKnkFIVhWyVp7OwKc-tqip_2RBNSBlBF_t9HQhZX-ugXUuR26bXD4ldb1yksPkkFtsyCqOs15IXW_7gzlGEyvIhQGvvoThWLYINFCmDMLOfcgoBq6Emu2XINjLKzmyKOrXcw9qOKgrOYorvsSW8N--W6hQkoKLXfAi06L5eHOchsb5tLus_DiU4pBGz-egJpHIMf6Qf6_MnI8wYqEEotE6fQEtxqZKIkGzx4HwRlUAetJkyJll2guOBeoYwsDZWhw3ZUulFfkbqPj-1okWE7qHopqjQoyVWSK3LNJiK47P6qVv_HfWGdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0efd09904.mp4?token=BL_hoPme2lwF86spVsghxKRAFZuzLBvjGEKnkFIVhWyVp7OwKc-tqip_2RBNSBlBF_t9HQhZX-ugXUuR26bXD4ldb1yksPkkFtsyCqOs15IXW_7gzlGEyvIhQGvvoThWLYINFCmDMLOfcgoBq6Emu2XINjLKzmyKOrXcw9qOKgrOYorvsSW8N--W6hQkoKLXfAi06L5eHOchsb5tLus_DiU4pBGz-egJpHIMf6Qf6_MnI8wYqEEotE6fQEtxqZKIkGzx4HwRlUAetJkyJll2guOBeoYwsDZWhw3ZUulFfkbqPj-1okWE7qHopqjQoyVWSK3LNJiK47P6qVv_HfWGdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎦
ایمنی سفر زائران، از جاده آغاز می‌شود
🔹
در آستانه اربعین حسینی، راهداران کشور با اجرای عملیات گسترده بهسازی، نگهداری و پایش شبانه‌روزی محورهای مواصلاتی، مسیرهای منتهی به مرزهای اربعینی را برای تردد ایمن زائران آماده کرده‌اند.
🔹
این موشن گرافیک را ببینید و با دیگران به اشتراک بگذارید.
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/akhbarefori/677014" target="_blank">📅 18:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677013">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
منابع عربی: ۴ انفجار در جزیره بوبیان در کویت رخ داده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/677013" target="_blank">📅 18:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677012">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
الحدث به نقل از منابع آگاه: واشنگتن به حماس قول داده است که نتانیاهو را ملزم به عقب‌نشینی از غزه و اجرای توافقنامه خواهد کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/677012" target="_blank">📅 18:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677011">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ادامه سرقت اموال ایران از سوی دولت تروریست آمریکا
🔹
وزیر خزانه‌داری دولت تروریست آمریکا با کمال پررویی گفت: دارایی‌های ایران را در سراسر جهان تحت تعقیب قرار خواهیم داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/677011" target="_blank">📅 17:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677010">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17770649ea.mp4?token=GuwZ360Ha5RcLEwFwnxg2Fp1IG0Mv0grDqJ4oOM_nools4FV-ff38mgSNDRu3FVbq8IMhrSde6vOjiy8A0-ETI8jHmNZOSB9po8XR2xRLMuQV1AMOSVfamT8aWvDxTBKTuURGuF72p72kIAPdQITWe0-CeriMGwIVXBMxslTn_21qikr-iuJ7-MrRTAJPZ9n-xt-QDZ6NvrUF0lfYsf4IcWvaiXNuARYkP0l_uE_8GlkrKnt-8JQoltO3CUA-nR1RWnMDg8KbqaBw2S3hn0rr_cq4xJC1qv3fLZeyGSv04D5D13qBnPQJyhsNGJGKtNjIZcieWmVq19ophbBQYoJ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17770649ea.mp4?token=GuwZ360Ha5RcLEwFwnxg2Fp1IG0Mv0grDqJ4oOM_nools4FV-ff38mgSNDRu3FVbq8IMhrSde6vOjiy8A0-ETI8jHmNZOSB9po8XR2xRLMuQV1AMOSVfamT8aWvDxTBKTuURGuF72p72kIAPdQITWe0-CeriMGwIVXBMxslTn_21qikr-iuJ7-MrRTAJPZ9n-xt-QDZ6NvrUF0lfYsf4IcWvaiXNuARYkP0l_uE_8GlkrKnt-8JQoltO3CUA-nR1RWnMDg8KbqaBw2S3hn0rr_cq4xJC1qv3fLZeyGSv04D5D13qBnPQJyhsNGJGKtNjIZcieWmVq19ophbBQYoJ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نحوه شستن روغن و سینک از زبون خودشون
😀
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/677010" target="_blank">📅 17:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677009">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
نیویورک‌پست: ترامپ مایل به انجام مذاکرات در صورت موافقت ایران با آتش‌بس است
نیویورک‌پست به نقل از یک مقام آمریکایی:
🔹
دونالد ترامپ مایل است به روند مذاکرات فرصت دهد، به شرط آنکه ایران با آتش‌بس موافقت کند. این مقام افزوده که ترامپ خواهان توافق است، اما هشدار داده در صورت ادامه حملات ایران، هزینه‌هایی متوجه تهران خواهد بود.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/677009" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677007">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مارین ترافیک: همه ترددهای ثبت‌شده از تنگه هرمز از مسیر ایرانی بوده است
🔹
پس از تصویب پارلمان بلغارستان، هواپیماهای سوخت‌رسان آمریکایی وارد پایگاه هوایی بزمر شدند.
🔹
حزب‌الله لبنان: تجاوز آمریکا به عراق، آغازگر پیامدهای خطرناکی برای منطقه است
🔹
نماینده حماس در ایران: مقاومت هرگز سلاح خود را کنار نمی‌گذارد
🔹
وزیر امنیت داخلی اسرائیل: پیش‌نویس توافقی که توسط شورای صلح منتشر شده، برای اسرائیل غیرقابل قبول است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/677007" target="_blank">📅 17:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677005">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1efb3a2f0.mp4?token=B1yG8RgMorx6RDXqVgcuFG9vHkyNQH2Ef3xjNAYLzM4dKoTIAn8guCRhlMlPKc-2Z9CdvRgOkUp6hnZMvMDSjwZCa1htLXcyEFUL3RtupLi0rmzo_QclS72kH0BEoUlHt8ousO3KwYR7JKcM7YGbFGKuZwrUeo9Y0Lt-l-vD9nJ_hDrR-4FzQ5perWM6-uXs_4X_yPOTa6VAS6EOnufGBX9-Tc5Z8HGYS0R4Lk6FHN8J-uq47o1ZwkPTE9FatD8k3GQMVWNWmdhfzf6TgcDpB1LF-e7dKzQiPtrv7avOt2vS8gfF3A2_yRxtigrU2Uz9xwTSQJeoyiYdzVXWiU27Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1efb3a2f0.mp4?token=B1yG8RgMorx6RDXqVgcuFG9vHkyNQH2Ef3xjNAYLzM4dKoTIAn8guCRhlMlPKc-2Z9CdvRgOkUp6hnZMvMDSjwZCa1htLXcyEFUL3RtupLi0rmzo_QclS72kH0BEoUlHt8ousO3KwYR7JKcM7YGbFGKuZwrUeo9Y0Lt-l-vD9nJ_hDrR-4FzQ5perWM6-uXs_4X_yPOTa6VAS6EOnufGBX9-Tc5Z8HGYS0R4Lk6FHN8J-uq47o1ZwkPTE9FatD8k3GQMVWNWmdhfzf6TgcDpB1LF-e7dKzQiPtrv7avOt2vS8gfF3A2_yRxtigrU2Uz9xwTSQJeoyiYdzVXWiU27Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آئودی دیگر فقط ظاهر جذاب ندارد، بلکه حالا پیشرفت و کارایی هم به بخشی از هویت آن تبدیل شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/677005" target="_blank">📅 17:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677003">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
استقرار تجهیزات هوایی ایتالیا در عربستان
اویشنیست:
🔹
جت‌های یوروفایتر، یک هواپیمای هشدار زودهنگام، سامانه‌های راداری و ضدپهپادی ایتالیا در عربستان و برخی کشورهای منطقه مستقر شده‌اند. همچنین ۷۰۰ نیروی ارتش ایتالیا در عربستان، کویت و بحرین حضور دارند.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عربی دنبال کنید
👇
@AkhbareFori_Ar</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/677003" target="_blank">📅 17:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677002">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دعای خاص امام زمان علیه‌السلام در عصر جمعه
✨
گفته شده هرکس صلوات ابوالحسن ضراب اصفهانی را بفرستد، حضرت حجت ارواحنافداه برای او دعا می‌کند.
✨
بیایید در این جمعه‌ نورانی، با فرستادن این صلوات، دل‌های‌مان را به عطر یاد امام زمان ارواحنافداه معطر کنیم و مشمول دعای حضرت شویم.
#گنج_پنهان
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/677002" target="_blank">📅 17:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677000">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_b39yhVg2EWaCYud-I1Ud88gG1pRDbJuxEUGYvaG6yZ08K3VXq4x6f9xAemsQZZimsSCFJQBknMv_T8jbFQbv4SEPB3CLR0GVABAz8tS_I6Pi1JEx4WA2Bmvmq8791y7kWw14C3V1G8o84rO3coG2DSuRW23nxY-FoKPWWajuJgCZjkrDUwK0wGK5tlrGy9gtQMpBmt9a3AKOHF53P05wUxiWkAcGLAeQE2lZZAfNPIdT2mxUbQbT7oSd65_m3sBJT5lMI82NHYZMOuH2x_RdZflcrbqoOYa24izdLDxog_NLz8SEbf4L7vHN9r1TJMgh9720fl4PaDWSyYpgRbRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵۰ درصد برنج دنیا را این دو‌کشور تولید می‌کنند
🔹
بیش از نیمی از برنج جهان تنها در چین و هند تولید می‌شود؛ دو کشوری که نقش تعیین‌کننده‌ای در تأمین غذای میلیاردها نفر دارند.
🔹
برنج یکی از اصلی‌ترین مواد غذایی در حدود ۳۵ درصد کشورهای جهان است و غذای اصلی بیش از نیمی از جمعیت کره زمین به شمار می‌رود.
@amarfact</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/677000" target="_blank">📅 17:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676999">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
سگ متوهم: حملات ادامه دارد و اوضاع به نفع ما پیش می‌رود
🔹
دونالد ترامپ درباره جنگ علیه ایران مدعی شد روند تحولات به نفع آمریکا پیش می‌رود و این کشور با ادامه حملات، طرف مقابل را تحت فشار قرار داده است؛ او همچنین گفت این روند ادامه خواهد یافت تا شرایط به نفع واشنگتن تغییر کند.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/676999" target="_blank">📅 16:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676997">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a9d671d57.mp4?token=ia8H-_LPzYbMmS-FB6P1eb9Um4viqqwA2go_fgDycaxn7Iu9KhpEt0c0Ig2ofjS1PHkua0hceAUxnu3WCMYXIA0twh-gVR0eCeg-WIUwabclsGXB_rn2a8nvKvQn4fVoNajYpxwp6N9HM07yR5tO27tpVIEGayxrfYTOJMz9i1ZjPKF13Ja_0b2i9ntUZ0j5yVgL-03T2DpX0yKzBQpDuQ473g9ktSSaLbo-Dg6dcfsfKP_ghZi9YJ6EFU5kUNmf6cJ4d2QNVF9zU7VV8XdRg7JhPzh9USHO2lFRTcUmsPkCMOZeRECI3Xc3Gc4ZFedCRVSXsUCZq01DB5zKVReFww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a9d671d57.mp4?token=ia8H-_LPzYbMmS-FB6P1eb9Um4viqqwA2go_fgDycaxn7Iu9KhpEt0c0Ig2ofjS1PHkua0hceAUxnu3WCMYXIA0twh-gVR0eCeg-WIUwabclsGXB_rn2a8nvKvQn4fVoNajYpxwp6N9HM07yR5tO27tpVIEGayxrfYTOJMz9i1ZjPKF13Ja_0b2i9ntUZ0j5yVgL-03T2DpX0yKzBQpDuQ473g9ktSSaLbo-Dg6dcfsfKP_ghZi9YJ6EFU5kUNmf6cJ4d2QNVF9zU7VV8XdRg7JhPzh9USHO2lFRTcUmsPkCMOZeRECI3Xc3Gc4ZFedCRVSXsUCZq01DB5zKVReFww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تنگه هرمز قدرتی است که کم‌کم از بین می‌رود؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/676997" target="_blank">📅 16:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676996">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7mTfXGq1QO_AHzNKHr3OMTEDsCuMyhnVLjm7Pix3E8FUk87fByiwiMNAi7r6Z1_Xd5YfbzN4zdbpVoE6DcbZksxl0GPnOeFIdWGL0Puu3CLsn6BqOZUTtKswEy3c91GPSC4jZQ6DUHom3JSDfbMf9Wf8lQSrFTuSO3aWEO6-Sn1SZaWJbHcs_oeIGQt8XC52wvfa6Hyl1An9rJXf4VCBH6frdK3yHkJ0_Q1U-gMjUhymp3H63TT9GkPMWycdXqxJBXZRTvj9-DxnWh9J88QmcQzvuI1-GPijNKhWlxWuS5ByiK3GPbsRFikV7Z3hedaWJmIY-dIHxnAX0_qjQ40KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به علت اقدامات تجاوزکارانه ایالات متحده، تردد از تنگه هرمز امکان‌پذیر نمی‌باشد
نهاد مدیریت آبراهه خلیج فارس:
🔹
به علت تداوم اقدامات تجاوزکارانه نیروهای نظامی ایالات متحده در منطقه، تردد از تنگه هرمز امکان‌پذیر نمی‌باشد. به محض برقراری ثبات و آرامش، کلیه درخواستها بر اساس ترتیب و زمان‌بندی بررسی و مجوزها به مرور صادر خواهند شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/676996" target="_blank">📅 16:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676995">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مرشایمر: هرچه جنگ با ایران طولانی‌تر شود، موقعیت آمریکا ضعیف‌تر می‌شود
🔹
عفو بین‌الملل: هند تأمین‌کننده سلاح رژیم صهیونیستی در جنگ غزه بود
🔹
افزایش مجدد تورم در منطقه یورو به‌دلیل جنگ علیه ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/676995" target="_blank">📅 16:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676994">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gld0LvNdc07QBBF6MODKC9QE_4D8xaNb9XZI-DxcvhpL8rOhXN2s7Y6RPjUj4f0GhdE0QpHH53oFP6nKKx1r5kgTGVojLdUdzb8LxvzUb0g408PPyVuzTuC06QVgvpU-JbH3WJOEqL19Fi9jxpGL1i2luuXumJbAuzvAoDaUV9XUJ6s1ToWXThJgmivIF0N_Pcjhv1jvpV0-S3yU47KBfnhAJPmNLPmId0LkmdidttUimSZDsqmcTszl5aYsw-amwHYig_DqrB648n6sGBSMLrv8_g_bhj_kv1ACQcbc2Y9Ma534A2bSE3wNFnEMFdCjhYH0G0D-gTlmVPTtT1vYlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت یک فعال رسانه درباره‌ تاثیر هوش مصنوعی بر کلاس‌های دانشگاه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/676994" target="_blank">📅 16:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676993">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbb1198ee1.mp4?token=NfqAIh6rK-OoI4cl831zFX2DTTEWHJFjSyfKFrXuAghT9B11JvQLKPl32NJycaEKvqK52ebbCy8GsgkXVmGB0DQa4E5FG97j2ZCbk3yzgdcOx6zXfQQT3rzfy4ziwyfwKsP40LIeulSgLRjvoMfTpNOQ8b7ps2TQld7j24Q-9xJqlqH19b_DrNYOoy4FfFUL5pOUO6gLVs8h4MilAgDubwU6BdPIYMGHm_SvfHgb9ddncsD0_EAiKjpPvu5FfGkOCyBBope2SU0CL4VDhJK-9BACnuiCa11lq1yfbbLRNQE_F3ss8xQSfmbXndxGbstIm8zHHIihFlC01itC1o2TmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbb1198ee1.mp4?token=NfqAIh6rK-OoI4cl831zFX2DTTEWHJFjSyfKFrXuAghT9B11JvQLKPl32NJycaEKvqK52ebbCy8GsgkXVmGB0DQa4E5FG97j2ZCbk3yzgdcOx6zXfQQT3rzfy4ziwyfwKsP40LIeulSgLRjvoMfTpNOQ8b7ps2TQld7j24Q-9xJqlqH19b_DrNYOoy4FfFUL5pOUO6gLVs8h4MilAgDubwU6BdPIYMGHm_SvfHgb9ddncsD0_EAiKjpPvu5FfGkOCyBBope2SU0CL4VDhJK-9BACnuiCa11lq1yfbbLRNQE_F3ss8xQSfmbXndxGbstIm8zHHIihFlC01itC1o2TmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مراکش با هدایت مهاجران به مرز اسپانیا، سناریوی آمریکایی-صهیونیستی را اجرا می‌کند
🔹
ویدئویی بحث‌برانگیز از مرز اسپانیا منتشر شده که گفته می‌شود انتقال مهاجران از سوی مراکش را به تصویر می‌کشد و واکنش‌های گسترده‌ای به دنبال داشته است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/676993" target="_blank">📅 16:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676992">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
تیزر قسمت هفدهم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای سید سبحان حسینی‌نژاد که در اثر سانحه‌ای ضربه مغزی شده و بخاطر شدت بسیار زیاد ضربه، امیدی به زنده ماندنش وجود نداشته اما ایشان بعد از مشاهدات اموری در برزخ و همراهی های مادر در هنگام دعا در حرم مطهر امام رضا(ع) توسط یک شخص سبزپوش در برزخ، ۳ نکته برای زندگی دنیایی آموخته و به دنیا بازگردانده می‌شود را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: سید سبحان حسینی نژاد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/676992" target="_blank">📅 16:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676991">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/206c453fcd.mp4?token=wBD56B_oILE63rG2pcdC-hD7qFXAijvtmx3epwQx8AoIIuXBXzBQXtU24Kx-3HNFqiA-lYsFvlnVKEmawiuo_xddQ80Ow1A0DL7qy3V42mq1_nh6q1Rm63MHKKwxW5UftiYbd73b5Kv6S5VRO3v9JJa-HreT6XgkcLUlViI4CLpscHEHNG6nfpX0eAZhGuTZXI8LOpB9-oiGig31kXnNPcGfYK0dd-CXYHZsmO5YgOO7AdPR31HvjScfyjpWBBJz936Fu4lWshWp1gaS5WzIBOQcj02gtjqURZHOYc6K2DbVnv3tq9Q49ucmal4Tok4R5QaoOiS0wrLVdFEtNZzWSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/206c453fcd.mp4?token=wBD56B_oILE63rG2pcdC-hD7qFXAijvtmx3epwQx8AoIIuXBXzBQXtU24Kx-3HNFqiA-lYsFvlnVKEmawiuo_xddQ80Ow1A0DL7qy3V42mq1_nh6q1Rm63MHKKwxW5UftiYbd73b5Kv6S5VRO3v9JJa-HreT6XgkcLUlViI4CLpscHEHNG6nfpX0eAZhGuTZXI8LOpB9-oiGig31kXnNPcGfYK0dd-CXYHZsmO5YgOO7AdPR31HvjScfyjpWBBJz936Fu4lWshWp1gaS5WzIBOQcj02gtjqURZHOYc6K2DbVnv3tq9Q49ucmal4Tok4R5QaoOiS0wrLVdFEtNZzWSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برنامه تعاملی تلویزیون اینترنتی مدار آغاز به کار کرد
🔹
«شهروندمدار» عنوان برنامه تعاملی تلویزیون اینترنتی مدار است که هر روز به انعکاس پیام های مردم و پیگیری آن‌ها از مسئولان اختصاص دارد. دغدغه‌های معیشتی، گرانی، مسکن، اشتغال، حقوق کارگران، تولید، خدمات عمومی و مشکلات روزمره تا هر مطالبه‌ای که نیازمند پاسخگویی مسئولان است.
شهروندمدار و سایر برنامه ها را اینجا ببینید
👇
https://youtube.com/@madaar_tv?si=e1sVJ4219UwoCUzD
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/676991" target="_blank">📅 16:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676989">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BY-oaMnKYekXWQ_HuYdwORVr5YK5KRUBWGFXknvN3X2WuVJo8Svu9cOMjq1kivQFT9Iy57iz67mpLbFXAeCaouZLefQMavCTmYPQU876zt5nIXZc_FJixtFTzrT5d1acVMxFoTXx69Fmhcl5mxPGi88C5QEfLdEVNgpCsw3Smz3YBrepEULPs6JqC9hv7Pj4UVQ_RHVCW0T1ZwepaGKDZQ76rJiF81mVr7hlVWlK46z7-3_T4H0YeZKVoLFRdHVVWiDCfM0RQKgZDHHIUOb3ZsjiY89JsRDBBXrhQ_b8rWREGtglHg1GuV0BK4ZoZqzLnVPDud5jdrYojtCcGf63fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
آیا آماده‌اید تا به کربلا سفر کنید؟
✨
▫️
با پویش «زیارت به نیابت»، شما می‌توانید یکی از ۱۰۰۱ نفری باشید که به  کربلا سفر میکنند .فقط کافیست عدد ۲ را به ۳۰۰۰۱۱۵۲ پیامک کنید و در این راه نورانی شریک شوید.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/676989" target="_blank">📅 16:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676988">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
حماس: فقط سلاح‌های سنگین را تحویل می‌دهیم؛ آن هم با این شروط
🔹
حماس اعلام کرد با مرحله دوم چارچوب آتش‌بس موافق است، اما تأکید کرد تحویل سلاح‌های سنگین تنها در صورت خروج کامل اسرائیل از غزه، تشکیل کشور مستقل فلسطین، بازسازی غزه و پایان تجاوزها انجام خواهد شد./ صابرین‌نیوز
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/676988" target="_blank">📅 15:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676984">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8719c4f62a.mp4?token=pLEibZaRp8t3LaEeZW72sfnv313VLRQ1qP3Awk4HWiXNBdpw5mBc1G_FndMWeDWWchgbQ5AYjL6ggQbnPqyDMNrfjNrC9IlIlcrPrmdwmB8adLzT6mCqQVbfXU1mZQLkIpUDr6X66Xc5NO7fhuKGbPc3AffLD436N3e1uhlexVPeJ-w5A7PSPbwQohx24GkqbxELyrMRId2M9ZPbhi3yYb_greso1rx75TSG5wDGUF1NfpFlJCDZf56KURyGP6kbr9buE_t85vOr0faPayi-hBARVon9ElsBH1j7gNwbf_SdWc9SyvDqTWdPNBPN5qcZCXg1SAXFZ95T6SF91XobsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8719c4f62a.mp4?token=pLEibZaRp8t3LaEeZW72sfnv313VLRQ1qP3Awk4HWiXNBdpw5mBc1G_FndMWeDWWchgbQ5AYjL6ggQbnPqyDMNrfjNrC9IlIlcrPrmdwmB8adLzT6mCqQVbfXU1mZQLkIpUDr6X66Xc5NO7fhuKGbPc3AffLD436N3e1uhlexVPeJ-w5A7PSPbwQohx24GkqbxELyrMRId2M9ZPbhi3yYb_greso1rx75TSG5wDGUF1NfpFlJCDZf56KURyGP6kbr9buE_t85vOr0faPayi-hBARVon9ElsBH1j7gNwbf_SdWc9SyvDqTWdPNBPN5qcZCXg1SAXFZ95T6SF91XobsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فوران قدرتمند اتنا؛ شکاف جدید در کوه آتشفشانی
🔹
فوران قدرتمندی از کوه اتنا در ایتالیا طی شب آغاز شد و شکافی جدید در ارتفاع حدود ۲۷۰۰ متری این آتشفشان ایجاد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/676984" target="_blank">📅 15:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676983">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
لحظاتی منتشر نشده از دیدارهای صمیمانه خانواده‌های معظم شهدا با رهبر شهید مسلمانان جهان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/676983" target="_blank">📅 15:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676978">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc07cde495.mp4?token=Cqr19pd8rxCrzFCQKIIwm5Paz8x-PpOLzWVPps-EDmBK9Pj-ygun2zjoAORxvR4Nc4Q6L8riIayEhlycneKlBrM9_BTcEfm7_jkScuaYqieWwvt0rWO6XcteKT5iYmHDTOqXhA1QAs-1bInr7tIourkoVP4KM1BvhKtU_OTNP0Rlk3HNEI-PwisN3nJzj4buulArHg5YJZf-4H6aL7amqgKaPbxfLVcpBVhhspMCRrg-JYtdAeTLiBKYGQ6SkTdrkWpj8NF7EzDVJ_jZOYV5lrvhRm3BCh5v-rl8e_gvl4k71IYzeUrWPQNT3NQDGgTv9j68QcjPNIz3lpJ81xW9Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc07cde495.mp4?token=Cqr19pd8rxCrzFCQKIIwm5Paz8x-PpOLzWVPps-EDmBK9Pj-ygun2zjoAORxvR4Nc4Q6L8riIayEhlycneKlBrM9_BTcEfm7_jkScuaYqieWwvt0rWO6XcteKT5iYmHDTOqXhA1QAs-1bInr7tIourkoVP4KM1BvhKtU_OTNP0Rlk3HNEI-PwisN3nJzj4buulArHg5YJZf-4H6aL7amqgKaPbxfLVcpBVhhspMCRrg-JYtdAeTLiBKYGQ6SkTdrkWpj8NF7EzDVJ_jZOYV5lrvhRm3BCh5v-rl8e_gvl4k71IYzeUrWPQNT3NQDGgTv9j68QcjPNIz3lpJ81xW9Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میدونستید پشه‌ها اینطوری به دنیا میان؟!
🔹
چرخه زندگی پشه چهار مرحله هست؛ تخم، لارو، شفیره و پشه بالغ که همه این مراحل ۷ تا ۱۴ روز طول میکشه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/676978" target="_blank">📅 15:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676977">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7979329654.mp4?token=fxFsFiSusDt37IIClT9cGZdGIqTsNuXt8ErYBJBtZkdGDikBGcZSuxki3RnFE7cmrky9aiYrNW8KHq_qcUVrdkg7osojfGQ4qeYO4U6kbPeQtPEVprz6X73iTj9r3xf2lIH-LAgIYAZtUxrbhClQTiFClsacU0t03jHoH-5GwT5dyTXYGpciUPERTVG2zMdpmH6RZjOzoZxa-kmAiXVcrY0z1v1O-U0wYTAEq5O9aDjkJSRPXwEWplF-VUXpBYa9eMk36apNqdY751IPDmgSBg23wtWDSNixOT4_wTBP-2xmWqMn3PNCCO64rpuAYKPRL0kbt1Um5AAVWBjuN0TJAiwrIAj43dQMee7JQKLfKfUOj4mgBQ2Mq8rl74j2hfpH6CZFDsy4h_ytVTMtZArBoXdKv41fYkWUcrK89YNET3moc_Vtt5dXZ4QKaSvvApM2Z2_d-sErEqH75SZTex-eareWfVPgHNpzdpESGYNIOrtmco5XXRSk38gLVxm-yHZ3S1b4GT97JSU6cqvLcCOQAsF3p29kvINjLKZtsxdd1RFcIj78fAFhKrDKG5r72hjlOvTvJlNfJXwOybhY5AoWt686zqWACejPaNvA08809MuO8MBbX8ksnxs6hfnW54Ws7ly2tWjSGr2hz8qJwe75P0HBb--hdWiRpcSz7NB-wf0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7979329654.mp4?token=fxFsFiSusDt37IIClT9cGZdGIqTsNuXt8ErYBJBtZkdGDikBGcZSuxki3RnFE7cmrky9aiYrNW8KHq_qcUVrdkg7osojfGQ4qeYO4U6kbPeQtPEVprz6X73iTj9r3xf2lIH-LAgIYAZtUxrbhClQTiFClsacU0t03jHoH-5GwT5dyTXYGpciUPERTVG2zMdpmH6RZjOzoZxa-kmAiXVcrY0z1v1O-U0wYTAEq5O9aDjkJSRPXwEWplF-VUXpBYa9eMk36apNqdY751IPDmgSBg23wtWDSNixOT4_wTBP-2xmWqMn3PNCCO64rpuAYKPRL0kbt1Um5AAVWBjuN0TJAiwrIAj43dQMee7JQKLfKfUOj4mgBQ2Mq8rl74j2hfpH6CZFDsy4h_ytVTMtZArBoXdKv41fYkWUcrK89YNET3moc_Vtt5dXZ4QKaSvvApM2Z2_d-sErEqH75SZTex-eareWfVPgHNpzdpESGYNIOrtmco5XXRSk38gLVxm-yHZ3S1b4GT97JSU6cqvLcCOQAsF3p29kvINjLKZtsxdd1RFcIj78fAFhKrDKG5r72hjlOvTvJlNfJXwOybhY5AoWt686zqWACejPaNvA08809MuO8MBbX8ksnxs6hfnW54Ws7ly2tWjSGr2hz8qJwe75P0HBb--hdWiRpcSz7NB-wf0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منافق کسیه که پشت شعاراش قائم میشه!
🔹
بریده‌ای از فیلم سینمایی «لباس شخصی» که در سینماها به نمایش درآمده است</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/676977" target="_blank">📅 15:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676976">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f935398a4c.mp4?token=QXVyA2E4WSfPGkeiMw8tLYTrnB1WJHuhmTYssF3crvbpjhGA_ys8CWurQjoEHd4C0YrRvC4NTYrlzoBVHdcObL79ixrOg0NDSUa2HujS2cp9SQqVQI37u-G8TrD2DgYQFetKRkwMyYtx3n3Bqsu4PyKsDjBRWqk2WnYg6dhQii02jBPL0hvx9vRawjyePSD1K7c1KNgkc-4tbklayxzkNh7imUcDKAM2np6sG91VhJ1rkLtpcmz-Eht1VTcCgj76mybhL15VHnKbxOKvJ3ROQqKAEc6Lljz2CWKUwFpzfryj8AJ1yPYiFk21qNOGYBn76cJlFGAgeGuJgbqo8hUArg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f935398a4c.mp4?token=QXVyA2E4WSfPGkeiMw8tLYTrnB1WJHuhmTYssF3crvbpjhGA_ys8CWurQjoEHd4C0YrRvC4NTYrlzoBVHdcObL79ixrOg0NDSUa2HujS2cp9SQqVQI37u-G8TrD2DgYQFetKRkwMyYtx3n3Bqsu4PyKsDjBRWqk2WnYg6dhQii02jBPL0hvx9vRawjyePSD1K7c1KNgkc-4tbklayxzkNh7imUcDKAM2np6sG91VhJ1rkLtpcmz-Eht1VTcCgj76mybhL15VHnKbxOKvJ3ROQqKAEc6Lljz2CWKUwFpzfryj8AJ1yPYiFk21qNOGYBn76cJlFGAgeGuJgbqo8hUArg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی تازه منتشرشده که گفته می‌شود مربوط به لحظه حملات پی‌درپی دشمن آمریکایی به دبستان شجره طیبه میناب
است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/676976" target="_blank">📅 15:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676975">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/676975" target="_blank">📅 15:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676974">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8225375f0.mp4?token=X_NVhdmJ2me-PmuRC5PfwM5TsulV4hh5ywokaYltwk_Qu_o6XK_vsJDLwYceoWSbFwvqEWC3Il7Xovw5LAS07Lw8jSt2k4_Crulb6EYPYyYFCC76sUNwswsqtg5tMFyL5irDtIftLXiU-Rkt9NfSWuyvLYOVXnfz5xS68mp4Fw2rYloh3Jfr8_SP3kBlR_YJG_USdVN7kYNnnQAwTTb1U1XPO5374TPNGB6PlexmlSRfPiSRQ__JVGZYs_CUfKMnFPBw8aKHQ8rzbe5xKUIyoCyQvRObUNpb0Cs1OOcyzoOp9ufQTbnSSgpDUcI-4QnmWF49N3a2fTryY6hAgQCf8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8225375f0.mp4?token=X_NVhdmJ2me-PmuRC5PfwM5TsulV4hh5ywokaYltwk_Qu_o6XK_vsJDLwYceoWSbFwvqEWC3Il7Xovw5LAS07Lw8jSt2k4_Crulb6EYPYyYFCC76sUNwswsqtg5tMFyL5irDtIftLXiU-Rkt9NfSWuyvLYOVXnfz5xS68mp4Fw2rYloh3Jfr8_SP3kBlR_YJG_USdVN7kYNnnQAwTTb1U1XPO5374TPNGB6PlexmlSRfPiSRQ__JVGZYs_CUfKMnFPBw8aKHQ8rzbe5xKUIyoCyQvRObUNpb0Cs1OOcyzoOp9ufQTbnSSgpDUcI-4QnmWF49N3a2fTryY6hAgQCf8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی روحانی عراقی به دلیل شباهت ظاهری به رهبر شهید آزادگان جهان در فضای مجازی پربازدید شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/676974" target="_blank">📅 15:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676973">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/064113fb7c.mp4?token=pJ5a2d2IH9KxeL4oYYtASatjYO3McEXT19PoZqs40ufM9K1_UjHSCqZn6YDpmDAwPcZUOojIwfMmgbVJ_SF_OoMVpYEwhACdUwiMTRaXuAxrpVYPxLZ6DWXKaSS5jC4jMW5v5hnoYu3vTE3FQkRMKanf8pdqI-g42lh_6HrdSNn4vLABOfAt9vhjcEJNWYYqbwWpvCoNF0Bna1golnFPoAOYqRC_oq5YwzE-AJFOWG_vT1wqLjgdpXhgzMNDu2SESor6Q_QD9s7ZUaUq_FgmGwJ_Ozm1W5xb6274NQ26ZEWkRkicezzQ_ysWpwDaqA5TxCWD4HO_B7utqquBlU6o4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/064113fb7c.mp4?token=pJ5a2d2IH9KxeL4oYYtASatjYO3McEXT19PoZqs40ufM9K1_UjHSCqZn6YDpmDAwPcZUOojIwfMmgbVJ_SF_OoMVpYEwhACdUwiMTRaXuAxrpVYPxLZ6DWXKaSS5jC4jMW5v5hnoYu3vTE3FQkRMKanf8pdqI-g42lh_6HrdSNn4vLABOfAt9vhjcEJNWYYqbwWpvCoNF0Bna1golnFPoAOYqRC_oq5YwzE-AJFOWG_vT1wqLjgdpXhgzMNDu2SESor6Q_QD9s7ZUaUq_FgmGwJ_Ozm1W5xb6274NQ26ZEWkRkicezzQ_ysWpwDaqA5TxCWD4HO_B7utqquBlU6o4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار درباره یک سناریوی خطرناک/تلاش برای ایجاد جنگ میان ایران و کشورهای مسلمان
مایکل یان، عضو سابق ارتش آمریکا:
🔹
رژیم صهیونیستی با حملات پرچم دروغین به زیرساخت‌های کشورهای مسلمان خاورمیانه، به‌دنبال شعله‌ور کردن جنگ میان ایران و دیگر کشورهای مسلمان است.در لبنان هم سعی دارد جنگ فرقه ای ایجاد کند
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/676973" target="_blank">📅 15:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676972">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb384c4485.mp4?token=hW2eMzD990EHuvvSvmNN5J660zmKICRBkWe6EExDT6U6qRcWWnX23dRKoQ5NlxpauJOMpJ2ZNpg1py4Ha16BtiOebTIRkN2xEyp6qnbyrR1xfp9-clvkgRvNoJl5P6DksK-YIffd1eOH86_N_5C09bQS1vjjtV3O7Q3xsooFty0uF4XBd_Pd4xevfjPp_nUOm_vCs5lPM3hAIDD46mIElBQr98H3W8lzeUbV966ALkNT06GFUB4z_5l9itFAs97wsrFRjWdOEr7Qfu1hCXfNw0zLt7cQDYj1tYpV8xaRzIG5KS4GwGdwlNYe9IYfbVhZichr6_2kCCQRh1qhMTMjLbmEIB34sfHE3L_ZhEwX5oX1gY6fufUrBUtzYHD_B9iu3UlQaaXo5AJsJeB_NWpnckPSPLLMb6BSsz1jBxamCPOtX0GDt0J4pW7AzDLA2h7K7BcoBsDzE0bJzO19wGZ0EsijV8kknVVcwNp0_uAzty9LhtANdd1DS6Utw-NtTVMHyKPsvgd7NWW1hq0iyHLD2cDKXuY0wkRVhnoCrneceRcFynVygSg-hQIc56hKXlhYsTH0xo_Ku768BF5ahbw37Vn-mBQIcS7661wJNHupkiPZcuiRjdcdzNoEF8jxQ6c-cRmXO7si1gaEJqJfHLb-NlluBreu2_fG8tBFNUuSb24" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb384c4485.mp4?token=hW2eMzD990EHuvvSvmNN5J660zmKICRBkWe6EExDT6U6qRcWWnX23dRKoQ5NlxpauJOMpJ2ZNpg1py4Ha16BtiOebTIRkN2xEyp6qnbyrR1xfp9-clvkgRvNoJl5P6DksK-YIffd1eOH86_N_5C09bQS1vjjtV3O7Q3xsooFty0uF4XBd_Pd4xevfjPp_nUOm_vCs5lPM3hAIDD46mIElBQr98H3W8lzeUbV966ALkNT06GFUB4z_5l9itFAs97wsrFRjWdOEr7Qfu1hCXfNw0zLt7cQDYj1tYpV8xaRzIG5KS4GwGdwlNYe9IYfbVhZichr6_2kCCQRh1qhMTMjLbmEIB34sfHE3L_ZhEwX5oX1gY6fufUrBUtzYHD_B9iu3UlQaaXo5AJsJeB_NWpnckPSPLLMb6BSsz1jBxamCPOtX0GDt0J4pW7AzDLA2h7K7BcoBsDzE0bJzO19wGZ0EsijV8kknVVcwNp0_uAzty9LhtANdd1DS6Utw-NtTVMHyKPsvgd7NWW1hq0iyHLD2cDKXuY0wkRVhnoCrneceRcFynVygSg-hQIc56hKXlhYsTH0xo_Ku768BF5ahbw37Vn-mBQIcS7661wJNHupkiPZcuiRjdcdzNoEF8jxQ6c-cRmXO7si1gaEJqJfHLb-NlluBreu2_fG8tBFNUuSb24" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سید بشیر حسینی: آمریکا با ترور رهبری، پدر ایرانی‌ها را به شهادت رسانده و ما با آمریکایی‌ها پدر کشتگی داریم/ به کمتر از محو اسرائیل و آمریکا راضی نمی‌شویم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/676972" target="_blank">📅 15:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676970">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDydsd6GJhoEv7h_plC8tGhT4B0rCci3qQaRfZvCzyV4Oj_-oxFyvEWTzat49UfnODCdzQgipiTDiscj8RyA4VvbClfmRksvdUI2cKcfRrSzP2vs_Y6NgTnMhFf94GFo7hFKLftvZCCAQOj_orDZl-TrbQ58BEiBHp0arIveOII7wUbSRokCd5pATNNRcU5TOeHmS87aW1Q1-7PngDeQcxdU130U01Tykya9Lp94Q6uM7EIrxKsGnCYrorHKGHV-aZd5xb12FbWrCp7Jw-KiT2gkPqrtI0fMaPAjoNHir7fW4TgHKkfaef2Yg4y5U2CdlxYDlap9PpFJZWGt1SM1Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بدن آماده رونالدو در ۴۱ سالگی؛ قاب پدر و پسری کریستیانو
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/676970" target="_blank">📅 14:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676969">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuHq9e1ii8V2InJhjywdq94Pntz-GSbwANOXN_ryoDNgrJVBGU41vOFUhxI0psat2Rgz5qDjFMPqsl4frZkhRvXVuL7-X83prkfU9tdZc9EIM0YvTBnDVCSOJ78fIAcEGHES8VRDJB0n05A90k8f0thynJxYx22nOget9o0TUIv6TOmxWOL3vZZKffqn6EbSFSkK1xyn1ZmXpy8lQwlDqVRdZiMAXGFrYiufj81GQopmSEQj3pvazQzD-Iw9Brd4wG7_uog9PZhq84gMYlJPfuESVV_ckl2nevvRgg897vWfP__dErk3IVuJQMBJsqSuPpdpvAokOpJG0E54_SPB2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محاصره زمینی ایران؛ طرح جدید آمریکا و رژیم صهیونیستی؟   تلگراف مدعی شد:
🔹
آمریکا و اسرائیل در حال بررسی طرحی برای محدودسازی مرزهای زمینی ایران با همکاری کشورهای همسایه و افزایش فشار اقتصادی بر تهران هستند. اجرای این طرح، به‌گفته تحلیلگران، با چالش‌های جدی…</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/676969" target="_blank">📅 14:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676968">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBJFcFJt3_L-mUEtZN3J-DhNRKDTu8mL4tPuMyCshsPTHUhl7tMjwi8NkXvAncQ6qjS6N1aykOmiVkuY4hiFbVmntq4SeTzjdYdR7UirhhZr_4Mw54ornj8JIbwady1-2zMDNoWdDvkITShbrKQZwmKAfl1Mg-kaVEUXrHqkjy10nvei5s442YrEKP9f_3CNFvQql4qXwUQQ5XpYV0urnPXUvMLfyyfQJ2fzIpCeP0EmwEPAHesN7dGm-LtZraBYgWkHSN8Ny10Q3Njp60UcLNO4ouLivX74ic3sujd16W_vOgBMxETZZBIqCgPaaqDTbcPRpBC_1kRqQG7ZnJ5ZLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قطعی گسترده اینترنت در ترکیه
نت‌بلاکس:
🔹
داده‌های شبکه از وقوع یک اختلال سراسری در سرویس‌دهنده اینترنت «ترک‌نت» در ترکیه حکایت دارد؛ رخدادی که همزمان با گزارش‌های گسترده کاربران از قطع یا اختلال در دسترسی به اینترنت رخ داده است./ سیتنا
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان ترکی دنبال کنید
👇
@AkhbareFori_TR</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/676968" target="_blank">📅 14:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676966">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7e0b93dc5.mp4?token=B_LdCewGuuTK61Hhwsut1D8ptvCYM0DQJqUrpCjiiTvKCCvbPqfMfhRB_C5RIyQygFJnlXn_9Y10HIwze0YFo5lnBgX6_HhbQOeUWKpzawsdK2dafyv1DNyEo8W5jrZrOr2shb7DTfUuD1BqPsP00sevKFaV_K9-PEu74bmeaTvnj2vj-xyZAAxHExcsM2BIEyTKjKjpuimD7bBGMI5I1c0bHjgMo8e1iqipoIZjjikCmNwYo4wsnzK25olfg-E7t70ADIcrojUafgp-DIpU2aWQ62ynhvghqtKlFhs52yLzzN18ckzHqmXBaGau30SJD2SYcLiE7W87CsS_w5I1uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7e0b93dc5.mp4?token=B_LdCewGuuTK61Hhwsut1D8ptvCYM0DQJqUrpCjiiTvKCCvbPqfMfhRB_C5RIyQygFJnlXn_9Y10HIwze0YFo5lnBgX6_HhbQOeUWKpzawsdK2dafyv1DNyEo8W5jrZrOr2shb7DTfUuD1BqPsP00sevKFaV_K9-PEu74bmeaTvnj2vj-xyZAAxHExcsM2BIEyTKjKjpuimD7bBGMI5I1c0bHjgMo8e1iqipoIZjjikCmNwYo4wsnzK25olfg-E7t70ADIcrojUafgp-DIpU2aWQ62ynhvghqtKlFhs52yLzzN18ckzHqmXBaGau30SJD2SYcLiE7W87CsS_w5I1uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کامیون‌های حامل مهاجران در مرز اسپانیا؛ ژاندارمری مراکش فقط نظاره‌گر؟
🔹
ویدئویی منتشر شده که نیروهای ژاندارمری سلطنتی مراکش، در حال تخلیه کامیون‌های حامل مهاجران در نزدیکی مرز اسپانیا، تنها نظاره‌گرند.
🔹
اسپانیا هدف طرح صهیونیستی-آمریکایی به‌خاطر حمایت…</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/676966" target="_blank">📅 14:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676965">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvdrJCZRU0q25Cl7GeihXRIc2jVRB-FXumzAGnoXNGb-3I_u1xKdNxIEga3Q-jfqVbNIAXGgatt7Np0pumIg96-6UJqBqud2MScnv4aT6u864t3H5OC5iaFVvOl-Gp0eE7eby9jT_1l1f5Sk77ONhET3YqKUsFXB2g6ofQr-eDSC3KecWEjrYuHEb7GRz0fBBOBo3Hu7TDnXg5L4JalOgdBVdgHrsPrKFMavcsXB597EMLCM0SwSWFMufdELQkrVK3CijQtdcemEvMPFPIyKVaoh5UGwzGy65vu75cH4ADeKKuxWKV5UyIC1y6UgG8sybi82ZJsLQPDpRul8djVvJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنامه ویژه و متفاوت شهرداری تهران برای اربعین/ از توسعه زیرساخت‌ها تا توجه به نیازهای فرهنگی و اجتماعی
توکلی‌زاده، رئیس ستاد اربعین شهرداری تهران:
🔹
برنامه‌ریزی امسال بر پایه مردمی‌سازی، توسعه فعالیت‌های فرهنگی و رسانه‌ای، ارتقای کیفیت خدمت‌رسانی، مدیریت هوشمند، تقویت مشارکت اجتماعی و حرکت از خدمات صرفاً زیرساختی به سمت تمدن‌سازی انجام شده و تمامی ظرفیت‌های مدیریت شهری برای خدمت به زائران حضرت اباعبدالله الحسین (ع) بسیج شده است.
🔹
امروز در کنار توسعه زیرساخت‌ها، توجه به نیاز‌های فرهنگی، معرفتی و اجتماعی زائران اهمیت بیشتری یافته است؛ از این رو، علاوه بر استمرار خدمات عمرانی و پشتیبانی، استقرار ایستگاه‌های فرهنگی و مذهبی، اجرای برنامه‌های معرفتی، تولید محتوای فرهنگی و پاسخ‌گویی به نیاز‌های نرم‌افزاری زائران نیز در دستور کار قرار گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/676965" target="_blank">📅 14:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676962">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eacdd6360e.mp4?token=rR-dCuptc_Lkp2bp7g996BzLC5jdqIM9wuxtUf7BQxeBXc1LURWinust6HauS0ij5FA7u6V4aTfB4Qk1o_WPYS4AZeyPwla4NMz8kP26o0UaWyFORn3dhAaOci9x-ooAZhk74ZQv3Foyz5VOLpdnacXHnN1HQsJXEZYBmDo6h0FCehrrG9CWAHAGg_2LfLZX5VSvnqCikHp8V_hY64B-7bEhdIQEBvvKRs6ZEx5f8xglQuj29O221aPLTIqH82ETBqQ5aWCb1h9kmn1oYnF7RLZWNq5ULDQ_ow-NM6BpTAKchRuXgq9VcsLpOMZ-X03G6KI-eCWs2OrUmoA4BCiBhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eacdd6360e.mp4?token=rR-dCuptc_Lkp2bp7g996BzLC5jdqIM9wuxtUf7BQxeBXc1LURWinust6HauS0ij5FA7u6V4aTfB4Qk1o_WPYS4AZeyPwla4NMz8kP26o0UaWyFORn3dhAaOci9x-ooAZhk74ZQv3Foyz5VOLpdnacXHnN1HQsJXEZYBmDo6h0FCehrrG9CWAHAGg_2LfLZX5VSvnqCikHp8V_hY64B-7bEhdIQEBvvKRs6ZEx5f8xglQuj29O221aPLTIqH82ETBqQ5aWCb1h9kmn1oYnF7RLZWNq5ULDQ_ow-NM6BpTAKchRuXgq9VcsLpOMZ-X03G6KI-eCWs2OrUmoA4BCiBhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایتی متفاوت از اربعین با ابتکار یک زائر ایرانی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/676962" target="_blank">📅 14:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676960">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a00a5bc9.mp4?token=mx-26vQWY7ueRxQFDNIP9MfQyknHzGftzSvCQZ8Hy5urw8CrxBAIWkxD_dFI9QN1zn1B0-wPrF2QKOh_9b37nvI-a5shtRE34Vwg9mWUWT3WTZsHTYpwPfPOqRYmzm43m03dN6WRVVcboPau7dv5n57lkL83psUZf1HT9n0ocPbxb9xNMsVU8scVVhpdTWd5sGHIFV_E2RQ8EcgRI2n98Ook8WHvSpBvY1WLUXEjxz6ScoTGoyMOxduIjliapAKx8s4HQwwVaKKYbCQiAORske-NZP8j605RV6n_Pn99SXLX2TZc5Q-QeDT3V_Rp-vKV8uLbe2e8ut4ciXvDXxZagg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a00a5bc9.mp4?token=mx-26vQWY7ueRxQFDNIP9MfQyknHzGftzSvCQZ8Hy5urw8CrxBAIWkxD_dFI9QN1zn1B0-wPrF2QKOh_9b37nvI-a5shtRE34Vwg9mWUWT3WTZsHTYpwPfPOqRYmzm43m03dN6WRVVcboPau7dv5n57lkL83psUZf1HT9n0ocPbxb9xNMsVU8scVVhpdTWd5sGHIFV_E2RQ8EcgRI2n98Ook8WHvSpBvY1WLUXEjxz6ScoTGoyMOxduIjliapAKx8s4HQwwVaKKYbCQiAORske-NZP8j605RV6n_Pn99SXLX2TZc5Q-QeDT3V_Rp-vKV8uLbe2e8ut4ciXvDXxZagg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بمباران محل تجمع نیروهای اوکراینی توسط روسیه
🔹
وزارت دفاع روسیه با انتشار ویدئویی از هدف قرار دادن محل تجمع نیروهای اوکراینی در مناطق زاپروژیا و دونتسک با استفاده از بمب‌های «فاب-۱۵۰۰» خبر داد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان روسی دنبال کنید
👇
@AkhbareFori_RU</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/676960" target="_blank">📅 14:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676959">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad9a3c862.mp4?token=lwCK9m9UpZrjypdKXLU2IShOODp7mB_4BrNT2Xl85OD6U2pAS9zvXUkHECxUS0dP3crdU8CnCwejGyGNJyGJx_nV6KOZvnGa4MxxDz8MeHN61xFYHzkAUHddY9tt3GQJ1FiINSwlAbHt55GpWTZp8ORKPgTxCCwLepB1eejUuvTHJ_yiXcOhH0EUQmGpzUu7sa72gNeLY1knOY9rg2AycJSAS9A8TUeOSKVz1ZVDHvYy-iBJWj4-WZRNohkRagLUzONjzYIuEUid4rZz8H7BSMMWKms5G7zQNIJyoNwyQAnnkUkdNh9o9OhMji4zn2yk4hstHioFcZzQEadcGVb8RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad9a3c862.mp4?token=lwCK9m9UpZrjypdKXLU2IShOODp7mB_4BrNT2Xl85OD6U2pAS9zvXUkHECxUS0dP3crdU8CnCwejGyGNJyGJx_nV6KOZvnGa4MxxDz8MeHN61xFYHzkAUHddY9tt3GQJ1FiINSwlAbHt55GpWTZp8ORKPgTxCCwLepB1eejUuvTHJ_yiXcOhH0EUQmGpzUu7sa72gNeLY1knOY9rg2AycJSAS9A8TUeOSKVz1ZVDHvYy-iBJWj4-WZRNohkRagLUzONjzYIuEUid4rZz8H7BSMMWKms5G7zQNIJyoNwyQAnnkUkdNh9o9OhMji4zn2yk4hstHioFcZzQEadcGVb8RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دوربین وایرلس مگنتی A9؛ کوچیک، کاربردی و همیشه همراه!
با این دوربین جمع‌وجور، هر زمان و هر جا که بخوای از طریق موبایل محیط رو زیر نظر داشته باش.
✅
اتصال وای‌فای و مشاهده آنلاین
✅
دید در شب
✅
تشخیص حرکت
✅
نصب آسان با مگنت قوی
✅
مناسب منزل، محل کار، خودرو و مراقبت از کودک یا حیوان خانگی
❌
قیمت قبل: 1,598
🔥
قیمت ویژه: 1,298
⏳
فرصت خرید با تخفیف محدود، قبل از اتمام موجودی سفارش خودت رو ثبت کن.
https://memarket24.ir/product/brief/35151/180124/</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/676959" target="_blank">📅 14:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676958">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3c52b50ba.mp4?token=jlEbegbKmXZZ20CIJErxj6CFKVQ8P0gJoQIWlfyuO1UNzFdbTa-cORyC202BYfqvgqH7LzKuntW1sGPT-b4CLbdsTwRHE4FBuulkclkLF6Efr6herLYNiHJlL9As8FBv0QclUq-rh8BbM0PMhPqnOCsXRA_nB9ZuVT1io4zp3Kl-2sTuoRkiNp8rQw_lP1SWPpTEPMJZ7bF2P26S3TToilnIc210-4w8p1adODoG9xbrkXUVmq-wLc8LAbUfTvxVYRxWD5xlPqq8lbyWGiwewk-pKrdb5BQ9alI2EZ5oweVb6LCmU6xV47ANXoy1FowWl7kXD4gaxxgvhCIuEclvlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3c52b50ba.mp4?token=jlEbegbKmXZZ20CIJErxj6CFKVQ8P0gJoQIWlfyuO1UNzFdbTa-cORyC202BYfqvgqH7LzKuntW1sGPT-b4CLbdsTwRHE4FBuulkclkLF6Efr6herLYNiHJlL9As8FBv0QclUq-rh8BbM0PMhPqnOCsXRA_nB9ZuVT1io4zp3Kl-2sTuoRkiNp8rQw_lP1SWPpTEPMJZ7bF2P26S3TToilnIc210-4w8p1adODoG9xbrkXUVmq-wLc8LAbUfTvxVYRxWD5xlPqq8lbyWGiwewk-pKrdb5BQ9alI2EZ5oweVb6LCmU6xV47ANXoy1FowWl7kXD4gaxxgvhCIuEclvlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی میراث اشکانیان به دست امریکا نابود شد!
🔹
شهر باستانی هترا، یادگار دوره اشکانی، پس از قرن‌ها مقاومت در برابر جنگ‌ها، در سال ۲۰۱۵ به دست داعش آسیب دید.
داعشی که پیش.تر ترامپ نیز، اوباما و کلینتون را به نقش در شکل‌گیری داعش متهم کرده بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/676958" target="_blank">📅 14:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676957">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a77b8a7a73.mp4?token=DCiaKIAGZskF0QBDLr_ZMXL9KFwvxU4eneEII8C6hH9QemXle1yo_SLXk6K3TBdmkY2nMaWRs_LIPunpb5Zw3GKYs32nr7pUqV6coAlAb_yfBrtcZQjUW9jr0BoRVvCaOURzarADKHn9I6Wl53XbWGNVLho0pgb32cuUnIfDqpRvZ81FC204x5se6HXq7NvpQc43h_sx4X2P_ocUDxw5ccten0pGbf1dXy89uM5Zat4jtO6iNpUhb-zbd5HK_7lRuXvx5ackBSAGLs4T-kzf90zLx0dcZJfTmARxVqisjxBHuTXpcCQzMgaU3J7hqMnIpYZ5sAjfap789QpbwxWpUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a77b8a7a73.mp4?token=DCiaKIAGZskF0QBDLr_ZMXL9KFwvxU4eneEII8C6hH9QemXle1yo_SLXk6K3TBdmkY2nMaWRs_LIPunpb5Zw3GKYs32nr7pUqV6coAlAb_yfBrtcZQjUW9jr0BoRVvCaOURzarADKHn9I6Wl53XbWGNVLho0pgb32cuUnIfDqpRvZ81FC204x5se6HXq7NvpQc43h_sx4X2P_ocUDxw5ccten0pGbf1dXy89uM5Zat4jtO6iNpUhb-zbd5HK_7lRuXvx5ackBSAGLs4T-kzf90zLx0dcZJfTmARxVqisjxBHuTXpcCQzMgaU3J7hqMnIpYZ5sAjfap789QpbwxWpUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روز دوم تهاجم مراکشی‌ها به اسپانیا
🔹
این ناآرامی‌ها بدلیل مواضع حمایتی دولت اسپانیا از فلسطین، لبنان، ایران و محور مقاومت بوده و این پروژه با هدایت صهیونیست‌ها در این کشور کلید خورده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/676957" target="_blank">📅 13:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676955">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
محاصره زمینی ایران؛ طرح جدید آمریکا و رژیم صهیونیستی؟
تلگراف مدعی شد:
🔹
آمریکا و اسرائیل در حال بررسی طرحی برای محدودسازی مرزهای زمینی ایران با همکاری کشورهای همسایه و افزایش فشار اقتصادی بر تهران هستند. اجرای این طرح، به‌گفته تحلیلگران، با چالش‌های جدی روبه‌رو است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/676955" target="_blank">📅 13:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676954">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/007cb2fb94.mp4?token=mP3nUPKvPGo73TUbHJzpbL0NLAsYmGvKTJhJIJOEvZgOq0Rx049ChgQBculchgF7iE00xLNjOSQsCnTLI6aIaZxySrDZy2sZcTjpVUdPP4sID32VzSDQeJTlX4lAIO1md6g8772IY6nv2VJf5-UEgy3GlcxYA6H_x8sA2gVzG38vbqhPqLYGKnl4CWh0Qb3vTtUvHtD-xXeee8IueIjGuHq7R7WHJC0wK4ikGOnCe8ZEKJ6g39TGOqVQ5IhKvqkYv_rfPWmX7K0cH0dJkWiBOj1SEka2zsI-poj_6_XUINQQxNMdK_cH_88vo7S9VeEui_k_l58tMB-41YeLqovxuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/007cb2fb94.mp4?token=mP3nUPKvPGo73TUbHJzpbL0NLAsYmGvKTJhJIJOEvZgOq0Rx049ChgQBculchgF7iE00xLNjOSQsCnTLI6aIaZxySrDZy2sZcTjpVUdPP4sID32VzSDQeJTlX4lAIO1md6g8772IY6nv2VJf5-UEgy3GlcxYA6H_x8sA2gVzG38vbqhPqLYGKnl4CWh0Qb3vTtUvHtD-xXeee8IueIjGuHq7R7WHJC0wK4ikGOnCe8ZEKJ6g39TGOqVQ5IhKvqkYv_rfPWmX7K0cH0dJkWiBOj1SEka2zsI-poj_6_XUINQQxNMdK_cH_88vo7S9VeEui_k_l58tMB-41YeLqovxuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرنوشت، محصول تکرارهای روزانه ماست
🔹
هرچه یک رفتار بیشتر تکرار شود، اتصالات نورونی مرتبط با آن قوی‌تر و آن رفتار خودکارتر می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/676954" target="_blank">📅 13:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676950">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BlD7zaSRSDI3lL0j3w_iqMuPQRTRrEpKuN86GyYTuVeSnLk1Gu5p_vW5KQbRrDlGzn91MVPJpBr8geFUvNzh7X3Z8iwSLIdtGmJGiJnb12O34EFAwUr9MC1ePyRrKURVfOJG9ciYgByOFtJ69lDxNHez3oZK2-1gdIAfD9z72kptECFilm-8vEeoxFfOaxjvQs7YsVTkSBjEJTWDodTrtsk0y23wFDY6sDRKoFqfhjJMx0B7ECmIuTjidjIKDkZFKsIdPlDXYjIPG7-eY_qrW_R7txJBxyIO9mxdKNUI5tPknTnSdbZ5ENBvqAJSfEHqjEQArtcE5Vb-t5EJklZ3gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توقف کشتی قطری در مسیر پاکستان به‌دلیل عبور از مسیر ایران
🔹
آمریکا مانع رسیدن یک کشتی قطری حامل LNG به پاکستان شده، زیرا این کشتی به‌جای مسیر موردنظر واشنگتن از مسیر ایران عبور می‌کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/676950" target="_blank">📅 13:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676949">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOvddG_qYcANbV3B5S8XaVrAKE5mVk_0-IQ8toGfwKBRW17yRhy1PY4M3vxlLuuDPTAZkXmPvGnzC99GWRGyJtyqT3c8Fs6l5ltvAZJTUuT9ZTrCrZVL4rzfrIWZLTbDDSnidOZ37Re7CR3CdXfEqHJgg4RB2gbilSmhrEWOY-Zxl_isbCMd0Ynyw4khhsqbkS--YKBPVUgDefrU02eDtN0vPYPVHjLgtoq10kpmX1cljmyPiIPRj-SxQndTCzgeCHBl2_Bs5hMQXxAATNUMj2Us11Wu0llYC3FBT1xRU7oHtS-l-rHqPaDt2ZwpQpogYP2TaSjzeT9Rb3Lhd24DvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر وایرال شده از حاجی گیرینوف و همسرش در اخراجی‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/676949" target="_blank">📅 13:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676948">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ii5Wgdl8cidqvPkZrt_5X7ThBbThJIe0GF_ERK2ckeuSk2snhT7Yz__B-X9QvMwPa1KjJWFmiZNKoFkR_jBsQr4S8MHXaba19KkP8_Bg_SH4hsr1mx23gYKJlpZenLkcMTKsqbcZ07tFPi1LKV1RgpXejBrhMzFamxDvpwmgdHHK6qZpdLL3NvfgaXbJrYu5lCsgXpoEMVt1YtJsItGNY2HZW9eoy0a5TxGybnuBQyBcjlMEWwYEM1uIxg1fMNI4y9tFSo92bsbURodqk8ae2acacOUa0kRMm8i9kel7kGSU5CsMGtoShx6gnZXzoZNrs-EoQH-X4XKFuZrmuV716g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕌
برج ساعت حرم امام رضا (ع)
حرم همیشه نزدیک‌تر از آن چیزی‌ست که فکر می‌کنی...
یادگاری ماندگار از بارگاه امام مهربانی برای خانه یا هدیه‌ای ارزشمند.
💰
۵,۷۵۳,۰۰۰ تومان
🛍
ثبت سفارش:
@gharar_order
👁
مشاهده محصولات:
@ghararshop
🌐
ghararshop.com</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/676948" target="_blank">📅 13:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676947">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeOHi-9ESgH1Hzwl4vATnf3-7OtAeCsztDGCauubmOmPwXY77tJp007OjAxB8ht8mir9sND5LCMlzQ482KMnR22Za0jwgHa0-cGAs8J8hb0LJswsgZEroKobNmsKUtzfcNlIfCwy4k8Jh8YZcAh7nejCxCe0UUxV30KJsWGVeSRdPZAbbVHhzHautxbTWRy8YC3IsRXMXKF9hTEkKMX67HibTLBEl6VNHSYdpcwvBT5oBkAaDCnFF0_QBsoJymo13PSteVi_BZeQOcN1ydy_PI2uNylCeogBVD_pezwH2oJZonsMu4g-HSzOajJ4M7qILrze6dYMz66z_rheHLQwcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شگفتی‌های ناشناخته از دنیای حیوانات
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/676947" target="_blank">📅 13:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676946">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشهاب پارسا</strong></div>
<div class="tg-text">مجتبی شکوری
یه ویدئو از خودش گذاشته توی اینستاگرامش و گفته امسال برای اولین‌بار اومدم پیاده‌روی اربعین و در این مسیر چیزهایی رو متوجه شدم که تا قبل از این نبودم؛ بین صحبتاش میگه عاشورا، مسیر اربعین و حال‌وهوای آدمای اینجا ترس از دوست داشته نشدن و قضاوت شدن بخاطر بیان حقیقت رو از من گرفت.
خلاصه‌ی تمام حرفش این بود:
اهریمن برای ایران عزیز ما خواب‌های بدی دیده و ما باید پشت هم باشیم
. البته که ریختن سرش و دارن بهش توهین میکنن به‌خاطر سفر اربعین و حرفای دلسوزانه‌ش اما به قول خودش مسیر اربعین باعث شد قوی باشه و دیگه از دوست داشته نشدن نترسه. ان‌شاءالله همیشه امام حسینی باشی آقای شکوری...</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/676946" target="_blank">📅 13:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676945">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fed29aef9b.mp4?token=ZBmZ_jeuTuCPjO_cjmSyOUqYVwOIwDwWUtrijo5rN8r6_NFTlU7R7imLPp3fLoQo5Yi3vO9T6x2Vri5X0MBKaeuwSrXZyN1vizIfgRpzzeNN2-lT4DbhpGOFXST4UkUJkgdjwc61N7jLFxE_wdapceTErSYy9xlgwnyr2KE-Q005JMYTCxe6FM38_9IfHYLbaEuRBd53WXLllKU1rNWA-5VbANfhBbsKk4bZUKNbyQe9nioRU3Y280VXgspw_dDk6oyu7RISY-v_zFcNT8KZMIs2F-36GM_k_CYQNwo9YMOrGN1tI_ait8LBUHUp8_SZyNOlNFdtAA341zDCDM37sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fed29aef9b.mp4?token=ZBmZ_jeuTuCPjO_cjmSyOUqYVwOIwDwWUtrijo5rN8r6_NFTlU7R7imLPp3fLoQo5Yi3vO9T6x2Vri5X0MBKaeuwSrXZyN1vizIfgRpzzeNN2-lT4DbhpGOFXST4UkUJkgdjwc61N7jLFxE_wdapceTErSYy9xlgwnyr2KE-Q005JMYTCxe6FM38_9IfHYLbaEuRBd53WXLllKU1rNWA-5VbANfhBbsKk4bZUKNbyQe9nioRU3Y280VXgspw_dDk6oyu7RISY-v_zFcNT8KZMIs2F-36GM_k_CYQNwo9YMOrGN1tI_ait8LBUHUp8_SZyNOlNFdtAA341zDCDM37sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایلان ماسک هجوم پناهندگان مراکشی به سئوتا، اسپانیا را به آخرالزمان زامبی‌ها تشبیه کرد و تصاویری از فیلم "جنگ جهانی زد" را منتشر کرد
🔹
وزارت کشور اسپانیا اعلام کرد طی ۲۴ ساعت، ۴۹ هزار مهاجر وارد شهر خودمختار سئوتا شده‌اند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/676945" target="_blank">📅 13:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676944">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
تصاویری از عملیات سپاه پاسداران علیه کشتی‌های متخلف در آب‌های خلیج همیشه فارس؛ عاقبت عدم توجه به هشدارهای نیروی دریایی سپاه و حرکت به اعتماد سنتکام
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/676944" target="_blank">📅 12:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676943">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38ffdd7aa1.mp4?token=USslQpS75XwIsnEOjnem6dDELwe-NqiZfgx34y6zuAAsYdnelWavOq676cIEoM_A1YLgmvKQ-VcFxcJUTO93zlO5k7fnYGmd1__OvFKAw8IqkBvrqSM7sX9BAdYxRzccPbY05GYuqykwp49_4QWW9Uh4EuW8NXiYBc9c5YJz4j_281g7PEGVer_0yro5WIfyke4W9q41N5E5s4v7Cvz3IKiKwq3r_TAwY6r7YPBYqcm48SpCnKusXxw8osp-ON7yUNxqav3x4MmUJhYWSYCQyeDwvB64NsAI9omCgtJ4_-5AWX9n8LNucQMVO_xMdfqnCdRPcQiP_QW0jB4JHX4QaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38ffdd7aa1.mp4?token=USslQpS75XwIsnEOjnem6dDELwe-NqiZfgx34y6zuAAsYdnelWavOq676cIEoM_A1YLgmvKQ-VcFxcJUTO93zlO5k7fnYGmd1__OvFKAw8IqkBvrqSM7sX9BAdYxRzccPbY05GYuqykwp49_4QWW9Uh4EuW8NXiYBc9c5YJz4j_281g7PEGVer_0yro5WIfyke4W9q41N5E5s4v7Cvz3IKiKwq3r_TAwY6r7YPBYqcm48SpCnKusXxw8osp-ON7yUNxqav3x4MmUJhYWSYCQyeDwvB64NsAI9omCgtJ4_-5AWX9n8LNucQMVO_xMdfqnCdRPcQiP_QW0jB4JHX4QaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سپاه: دو نفتکش متخلف مورد اصابت قرار گرفته و متوقف شدند و ۴ نفتکش متخلف به سرعت برگشتند  روابط عمومی سپاه:
🔹
ساعات ابتدایی امروز دو نفتکش متخلف تحت تاثیر اغواگری‌های سنتکام به خیال اینکه می‌توانند از مسیر غیر اعلامی تحت اسکورت هوایی ارتش کودک‌کش و تروریست…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/676943" target="_blank">📅 12:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676942">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
سپاه: دو نفتکش متخلف مورد اصابت قرار گرفته و متوقف شدند و ۴ نفتکش متخلف به سرعت برگشتند
روابط عمومی سپاه:
🔹
ساعات ابتدایی امروز دو نفتکش متخلف تحت تاثیر اغواگری‌های سنتکام به خیال اینکه می‌توانند از مسیر غیر اعلامی تحت اسکورت هوایی ارتش کودک‌کش و تروریست امریکا بدون توجه به اخطارهای ما، در مسیر ناامن و غیرقانونی حرکت کرده و از تنگه هرمز عبور کنند، مورد اصابت قرار گرفته و متوقف شدند و ۴ نفتکش دیگر به سرعت تغییر مسیر داده و به محل خود بازگشتند.
🔹
شب گذشته در پاسخ به بیانیه کذب سنتکام به اطلاع همه مالکان شرکت‌های کشتیرانی و بیمه رساندیم که به اطلاعیه های سنتکام توجه نکنید و از کسانی که فریب خورده اند و دچار حادثه شده اند سوال کنید.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/676942" target="_blank">📅 12:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676941">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6lwVe-88Zp94O2DP0AYB45VFjy3-mL763fbYK0-RiEUORLklX8a7Nykp8qrvK2d3YJ0K3_Q0UCdhbhZeL8kVcChP2B8iKSCXCdFZp9Cii7YtijpdFMWUE95HaAcnUJO4N9wGKjbfhFvmSgi691k88ha9F0FeRu5ESybxOkXRLniPVFIGGFds8lqW7HEmXwdLer9mqwfBDLBT-Qr_v3UVb6l4GoaH7XYwz7z0a3cDUTh-yaMNG5gQzEbIzcAqD8POPIf9kIOgKqRrA24VwWY6nQAI2EnaZrIf4JaGWbtTbwXpsLhK3JnAIrvhNZ6pqSvx7dUMrhIdwaXQqZGpIlljA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری | حضور به نیابت از رهبر شهید در مسیر اربعین
🔹
اگر در مسیر اربعین هستید و یادی از رهبر شهید در دل دارید، یک پیام صوتی حداکثر ۱۵ ثانیه ای برای خبرفوری ارسال کنید تا صدای ارادت شما نیز در این مسیر ماندگار شود.
🔹
در پیام صوتی خود این جمله را بیان کنید:
«من ... هستم از ... و در این مسیر به نیابت از رهبر شهید قدم برمی‌دارم.»
🔹
منتخبی از پیام های صوتی شما در خبرفوری منتشر خواهد شد.
🔸
پیام صوتی  خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/676941" target="_blank">📅 12:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676936">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7rDweW0MJXaBrA9iLCpgpb4D2IKeJvMdgwiNWKjf_M6Nav0hRdlSau3HUWG0G_f6xTdVoOxBhV2uEFtqo_eGbwbOJtNyvOQCvMz7S8ZR7B_p74zBXpPuO34CMpy3ar8ojGzJA4BrnAJ6CjD6xUF5mCDoCOBEUIQ3cKymkPdji63e7cw1RokQ9eRDDf_iSkplsbHfeGMVAjm8a6XQMDLSZp4l2UivFffDXBTR1yF8tmDq8wdMT69TnxHNzlsk1mIBOtgQ5IWCIcdCbFksSY1LykCLFiJh26D3_CalMXX1d7CAIyFhMm3zP0oILdJigRO4MDZNhP0vlVp4SY51_iLeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنی بیست‌ساله که به هنگام زایمان جان سپرده است
🔹
این استخوانِگان ۴۰۰۰ساله در کاوش اسماعیل یغمایی در تپه حصار دامغان کشف شد و بنا به سنت خاکسپاری به پهلو و رو به طلوع خورشید دفن شده و در کنارش کاسه خوراک و بر انگشت و مچش، زیوری مفرغین دیده می‌شود و سر جنین او در تصویر پیداست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/676936" target="_blank">📅 12:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676935">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-zBN7e9t4wA1WLhJL30U2F49KmzTAcR_jzqp5BOQ3nypvSeRd-kLZvW6mxzmj6Z2hO5j-hO1q8fqHGYFqKnUaeiurkabHycItKq09k2wqP8rRoF8wXRESSqfdLbFFxq9HrsQf8B5iHuKdOla1A9bT4ARd6mOUV_zAFnfTSJN4qCphooc6pn-fdJfuqNAWehKwCkxJHu8pJwY0XFRhPiV2XjtxyyqnIPtXkRjU7CLrpzNwJ0ON0T82H1tNj-mWPFC9VMmEDJbEMmB9_ZY0xzDqbQxgezz1oKldIxV7Og2EgDPHXjlAap7Oxw6abl7OrC4VHgRBx_0a9SQg_UiToSkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایلان ماسک هجوم پناهندگان مراکشی به سئوتا، اسپانیا را به آخرالزمان زامبی‌ها تشبیه کرد و تصاویری از فیلم "جنگ جهانی زد" را منتشر کرد
🔹
وزارت کشور اسپانیا اعلام کرد طی ۲۴ ساعت، ۴۹ هزار مهاجر وارد شهر خودمختار سئوتا شده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/676935" target="_blank">📅 12:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676934">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V137SyVs-8O1HccH4oRLRUfC4r-7vdbInOBNae9m3k9iugiCcUGv42HmE_vvdZ0DTQoehSU2-YVjDdkbfPB4HQu33-isoOerNfXtAFqG8x6xqlrS8Zt-b5X_I87BvtTMuNbpTF73598UMgFtINixITwB3yE-FV1a9a42kBIyOX8Ax7P6TzBgtP1_e2PxYMT3PWq-4dsimekLqY0cFFPOnLhB597CKXJ8rw8l2suH_yuXhcVaHFWvXWT60RtIWcYLiSTjuUyplJaWuigBykOW2wj_KX-Un2d9jE_K5AMA5ySSw_rwNGLjTRKIGLi1zj3EDIbPUK0k1Ci0V-tH8sx6rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرنوشت جوان مفقود فلسطینی در تصویر سربازان اسرائیلی
🔹
خانواده «محمود الدریملی» پس از دو سال جست‌وجو، سرنوشت فرزند مفقود خود را از طریق تصویری که سربازان اسرائیلی در حال تحقیر و آزار او با دستان بسته و چشمان پوشیده منتشر کرده بودند، یافتند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/676934" target="_blank">📅 12:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676932">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59d85e4810.mp4?token=CV-Al6dMNklv6ueyjh8lM40tlNZ4Zj3Eb8sEFP5RkK4tJpg3b0gGBOQyTew1KLKQletkmghPmWDgD2bbjACQn-YlmK5ueqv4iRDXN5lBRCxNmGBQE5Y3Z4ogE_RDz5BgV93fQXEKjASbvBqpAN9wNAn1YqcIoaKfRTNca1MfgJdF7S3F_hz70wbcNY68455N85zBklfD0OVBM36Kbf0jR-HyXa4NdeT5AnjmOo-gzegqWQy0MiaTc0Qi76b3tHh6tOXdd-FDzCXlqIltqKO_M-4A2bBern4_M1TpTVjulLXOrYwaBf5vuUg4lsTbWKhqj7S4wnalaGdGAo8TWyvJ2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59d85e4810.mp4?token=CV-Al6dMNklv6ueyjh8lM40tlNZ4Zj3Eb8sEFP5RkK4tJpg3b0gGBOQyTew1KLKQletkmghPmWDgD2bbjACQn-YlmK5ueqv4iRDXN5lBRCxNmGBQE5Y3Z4ogE_RDz5BgV93fQXEKjASbvBqpAN9wNAn1YqcIoaKfRTNca1MfgJdF7S3F_hz70wbcNY68455N85zBklfD0OVBM36Kbf0jR-HyXa4NdeT5AnjmOo-gzegqWQy0MiaTc0Qi76b3tHh6tOXdd-FDzCXlqIltqKO_M-4A2bBern4_M1TpTVjulLXOrYwaBf5vuUg4lsTbWKhqj7S4wnalaGdGAo8TWyvJ2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎦
عشق رانندگان به آقا امام حسین
🔹
موکب به موکب، قدم به قدم، اشک به اشک می‌آیم آقا، نه با پای سالم که با دل مشتاق، اگر لایق باشم این قدم‌ها را به‌حساب زیارتت بنویس.
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/676932" target="_blank">📅 11:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676927">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78f2d8ddf.mp4?token=uLwb910FeoGzu7p8RXOUrmXudWTqPphnI9AEBUJfYGO9XLNNjGYLInxljE3fLtz_dAh2Ohb_w-4nOR68jWPKD0Yn1DFJwRekxzcJGStHNuyXg-nW-2LePJkzn1fPieOcQrhIYIq_tL_1Ju5OK8b5oDbWRVAs2cxn6iKSMHdAXbKHzUrNFd8F8xFjvIy3fzgV0hX-x3LJxMbU_JY6cQMU4uxRdjSM4GRlOSpjKQ1phCN9OuiQW-G90D4O82coQH0zgeR9NZFBld_ZZW5jwsTIdwfhZoZUtf6lTGivXm-eZ6-MDD4M7HnyJkyo_uDoorPIf72VtTYP4DjhoegOxA-qWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78f2d8ddf.mp4?token=uLwb910FeoGzu7p8RXOUrmXudWTqPphnI9AEBUJfYGO9XLNNjGYLInxljE3fLtz_dAh2Ohb_w-4nOR68jWPKD0Yn1DFJwRekxzcJGStHNuyXg-nW-2LePJkzn1fPieOcQrhIYIq_tL_1Ju5OK8b5oDbWRVAs2cxn6iKSMHdAXbKHzUrNFd8F8xFjvIy3fzgV0hX-x3LJxMbU_JY6cQMU4uxRdjSM4GRlOSpjKQ1phCN9OuiQW-G90D4O82coQH0zgeR9NZFBld_ZZW5jwsTIdwfhZoZUtf6lTGivXm-eZ6-MDD4M7HnyJkyo_uDoorPIf72VtTYP4DjhoegOxA-qWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از ورود مهاجران به قلمروی اسپانیا
🔹
همزمان با تداوم بحران مهاجرت، گزارش‌ها حاکی از آن است که بیش از ۲۰ هزار مهاجر بدون مواجهه با مقاومت نیروهای امنیتی مراکش، از مرز زمینی وارد شهر خودمختار سئوتا در شمال آفریقا شده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/676927" target="_blank">📅 11:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676925">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3d9857e6.mp4?token=KsGN9E18kQ946btoMgS1EUEQAaba8Rl2pWirPqiDsUwMa7cbBFSWUIRW59UIUX4DGAGNhZXo2QF7vVi48IJh2rP9MxncxXe8ugeFpKvQ2I8bZtXk3_Jo3dTneytBrZgn3Esc5LOmNEA2gFlRr_M6NemdiJmQB04QAjta0QMked7n5n9zN-4ZV6Xlz1SSetpMtTKW0d1btTc1u7rtE9SyyuTDz1sV3teIjUROYUoAoi1QKS0Aed9rwB-CnGx5uXQauxR3fw5K0Z4oSGVvbOfO3PnqANC3UHEkS2rzaciKKLFiaUevIqNx0p_eRNAYFfjCHn2bHnIzPUTjGGAz-B41bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3d9857e6.mp4?token=KsGN9E18kQ946btoMgS1EUEQAaba8Rl2pWirPqiDsUwMa7cbBFSWUIRW59UIUX4DGAGNhZXo2QF7vVi48IJh2rP9MxncxXe8ugeFpKvQ2I8bZtXk3_Jo3dTneytBrZgn3Esc5LOmNEA2gFlRr_M6NemdiJmQB04QAjta0QMked7n5n9zN-4ZV6Xlz1SSetpMtTKW0d1btTc1u7rtE9SyyuTDz1sV3teIjUROYUoAoi1QKS0Aed9rwB-CnGx5uXQauxR3fw5K0Z4oSGVvbOfO3PnqANC3UHEkS2rzaciKKLFiaUevIqNx0p_eRNAYFfjCHn2bHnIzPUTjGGAz-B41bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مایباخ S۵۸۰؛ ماشین جدید بنز
🏎
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/676925" target="_blank">📅 11:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676924">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/TuMODDt__9T7BVHc49u37DvY71ZXnwq_IRzsxAkkhO0qSCWR9PDr0sk0oK7PMq1Fsw5mVFzoJcRepLW95R4BVUhpn-EDekx0g5GBVoxMoA680cE771a_rhPYKYl5NiZX3roqQW_I_BTVJvSFQvtgxrFDEBbpg_AlumfnXI4N3X_DkUKeosw2LDMihngbVMfvbnJTEIryNfLE2SgeZZYEpej1CvpBB7E257JVE8j5YSJjRckq76RwCy1Zr_3AtDOUuBbwMXioNqDE9i29yKyHj8id7wQjuQGadeMp7uNGO40sTM7Upuh0BXPEJfAvNybw1nbyS-KpoCZEPcks2qJX3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور حجت‌الاسلام محمدجواد محمدی گلپایگانی داماد رهبر شهید انقلاب و سید پرویز فتاح رئیس ستاد اجرایی فرمان امام در موکب امام رضا(ع) در عمود ۲۸۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/676924" target="_blank">📅 11:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676923">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8a5326a9c.mp4?token=WqZh5AbeKzd8uUkJnz0OgslLr2fOHFRhWHy2uMsIMdFtkUD3y67Rp4JpN0Y9yWgOPIaAnSUGWQvAYTQQAeDRBlSjt968CSIArldiTuKl1sktaqKErUwv8Q0Pgzsz-uo_62sqkiJPcMqCZvBS-AeEQGwWtKS61OtvKc8ZLjsdTUX7FxSb03whzRXoQVEyjxz3BDIC6dudM-SexVda7lWGIxd-GJ2s-B_YjHtGns1s3MeBW0nDMv_HiQROHphjtUhnRkkNYYMEEsjpShjMfVrOnsFibfF0CiLl4P44Hqs_BdbR6MF3aaVvqV66_b6V0omjAp9lxntxwFJyYCP2i_mEx3qdHHt5KpLoyrXLQVLu_psreIiVvFjpxZU1qeCJhbvY7dTc5_8UvQWXaFRcqjfr0-jtKoKwUqeearqAa6193bPRmoDZz_CML5Icc6p5hX837lDfSqYGsBK-nwS3wDrTORPsfPMEiRnV3IJmm8RkgpPYaOzDAmeGKfyyjI_zT21qdwGXJ7pY-SVrO-aXB3TtXd3JVqgxo2Dly_1Edv6wO6fJNN8bkzplCe3a4gR1YoTmyEQ9DnpcZj6zjyZz3vkix9J12oPhadMQud6GxfGQzz3B9WydFklW5dmxhelDnJUYUJtHnQmOaYhIomMeXDFspMaZAuRrVJUvNz1Cv5FZFW0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8a5326a9c.mp4?token=WqZh5AbeKzd8uUkJnz0OgslLr2fOHFRhWHy2uMsIMdFtkUD3y67Rp4JpN0Y9yWgOPIaAnSUGWQvAYTQQAeDRBlSjt968CSIArldiTuKl1sktaqKErUwv8Q0Pgzsz-uo_62sqkiJPcMqCZvBS-AeEQGwWtKS61OtvKc8ZLjsdTUX7FxSb03whzRXoQVEyjxz3BDIC6dudM-SexVda7lWGIxd-GJ2s-B_YjHtGns1s3MeBW0nDMv_HiQROHphjtUhnRkkNYYMEEsjpShjMfVrOnsFibfF0CiLl4P44Hqs_BdbR6MF3aaVvqV66_b6V0omjAp9lxntxwFJyYCP2i_mEx3qdHHt5KpLoyrXLQVLu_psreIiVvFjpxZU1qeCJhbvY7dTc5_8UvQWXaFRcqjfr0-jtKoKwUqeearqAa6193bPRmoDZz_CML5Icc6p5hX837lDfSqYGsBK-nwS3wDrTORPsfPMEiRnV3IJmm8RkgpPYaOzDAmeGKfyyjI_zT21qdwGXJ7pY-SVrO-aXB3TtXd3JVqgxo2Dly_1Edv6wO6fJNN8bkzplCe3a4gR1YoTmyEQ9DnpcZj6zjyZz3vkix9J12oPhadMQud6GxfGQzz3B9WydFklW5dmxhelDnJUYUJtHnQmOaYhIomMeXDFspMaZAuRrVJUvNz1Cv5FZFW0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نور طبیعی به‌جای قهوه صبحگاهی
☕️
🔹
استاد عصب‌شناسی استنفورد توصیه می‌کند برای افزایش انرژی و هوشیاری، بلافاصله پس از بیداری به‌جای قهوه در معرض نور خورشید قرار بگیرید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/676923" target="_blank">📅 10:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676922">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/059f1d5219.mp4?token=VXmq-6awRbghjpyqClIKbqnEMtoi1cnVMYBC1H76k2Eq70HuYyfyTYskY5t_8ObGby7BCu7BUxBIF8WttKDJo1ZJwm4jYPBM8nnsPThMQDdgk5kDES72rjTMh_bQO14X0liDouz3eYuSTZbIwZNrILJkqI4D6xa85yntsg8In9BCzZsa4eZFa8ZfOEpAvHhTfmHmAjAVrh2V35LIJVk34CkHgGoKZWTRbGKpwvDhG-gmjbxBgv47hWoTdtLGDiGFkpGmj36ARugsgD3BW_RO9NDUki82f6Oahic4M5EDBxPpKlxGiuYf-AUh1zHH56StLxpxZCnSsOsc-XbV8zwZYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/059f1d5219.mp4?token=VXmq-6awRbghjpyqClIKbqnEMtoi1cnVMYBC1H76k2Eq70HuYyfyTYskY5t_8ObGby7BCu7BUxBIF8WttKDJo1ZJwm4jYPBM8nnsPThMQDdgk5kDES72rjTMh_bQO14X0liDouz3eYuSTZbIwZNrILJkqI4D6xa85yntsg8In9BCzZsa4eZFa8ZfOEpAvHhTfmHmAjAVrh2V35LIJVk34CkHgGoKZWTRbGKpwvDhG-gmjbxBgv47hWoTdtLGDiGFkpGmj36ARugsgD3BW_RO9NDUki82f6Oahic4M5EDBxPpKlxGiuYf-AUh1zHH56StLxpxZCnSsOsc-XbV8zwZYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به‌ اندازه نیاز خرید کنیم؛ از خرید و انبار کردن بیش از نیاز خودداری کنیم #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/676922" target="_blank">📅 10:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676911">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PojrETwmlylAx-LAh5iWniZtA0DHXKWNT5L5QGj_8YWzmgGr5v-fEBGiAKpo1aMGazeMpUG5njl7aqBKtxCulzX61fF0FZ-QLYQJ0u9jbOTBG4kPXHemonazfm1Q9JF_71PeEGanCkh5sKQ5Pgtfa_hkC1ppsWQGqQ0amXucHp_Hhh7piD4ulO-jq12o0F1dHBT28Li3jxLhr1wVNt2p8-EA94HMkno_wvW277OhWakyck8UZzAhUhkvSrhnPMnc4Jp40-NXflGrYVonRI8VgBpPWtGIrOd6r75-pBNWCL9NfCfHc7Bp5n9UjAR1CObEYKPgn7484TfEUaSdTjQB7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PD-KkHq8cOr4lRGyOZgwXuQTZYWpG-ZapBaXOB8cKI45DD6jroe_xBPzA2DxFu8MiwcEw2RNYUfBpoSgwOXJ3l0jKXPwtH4SBojANKYvXqxCHTOHYz8ZqfCLCVMcK97k9Xalm0HNGgQV8V-fvX2WxWNZZn1VsIIi2L2aoKzzbLbSSESEW9QYILL4HpWHWdP00tpt8qWxOug-UPP398VfV43vBVMlzXkb-_R3pPIjvNs-w_1sBXV59IU6UUdHAnXtY8EXHiEtbT36y9u6xFVegEo-dzMZdF-9_rkB6RuU_IarnqAR2FBl5OEx1kXhRRVUrhT86UdcVd6UN_iGDoPfag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LOiMkzrIMBFEnjvdnPpgefTXojxmI6MiGRctkC7t0Xj56FuyXTA1JhRLsldLQA7XQ6yZ-nmv_xg7Z0vrHpsK0nnmX38MHIYcGJr4Iz7FjstBbxovhqa3wdmvDtcMj49Srwkw2_Y7WKJrR5vH59WqPJ6sl7ah_P5Rqpwfr7nHpP91ugU7m39-b3oLkuGKOuhMsRQydePRD6Evhgma1jRlYG1bc_02w2OAq5aQvA4lEeRjUnnqwsHnlGbNOpoqufeHMNa3hTfYn4eKAIaM---VBlRSSHLaD88JHqKxczlRSEKSNN1TlyD3xnY_y77FfXl2OK5cm_6h6JbK4bsdqWMv_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ati2kYWK6it0BKFzbCdeFin9h09Az6iWY1GbHBM2FOnZa7hX3HqwfE_dxHquF93moB-JdAMi41EFSnkJW_VJlhNo9J0RYvmsbBP5giLAqCKQAWjP2qO-fXOFGLzfZ7tadnTnszqR7Uk5wuzF3KSlfnyWaIoRcRZUz51MqzhmbS05_FrOV3Fv5f1mRgYa5ViJmCxitpUCks6oIsVCBky8vyKp7f-AiCuWmLKxC6Z_KmlsHQ5B-7AVm4rbLl1350FUYtonM2DBGSWVCe-ilAlxPCTzXyMF0SNQcZqJdP44wprrYMw116hm8SycS1ptjs0vWRHi7RowVT1Nlwla8y5eyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BJv9Z-qjQQe-9IKJLKobA4I-nb9z51lSJYQFz0iicXBJkTMgqYQ4AnkYt7mX7xZXrfRzrGhIifXaFF96m643CSONm6z2P6V_9SpGMz0edJ62dq4O432ytTovTUQDGiL55AHLMFluYUvmHHP9bN9enWtfDr_ilW5oJ00QnIRMVRGb4ARFIU2kC9SS5UEo5PAhKV9S7hWu6Q9uoNImI5t9l4Jg-THndjtDY-nYSLbJpIWMlN7A1_0p0iJt1vLGS2PSyuWbA8SaYEu68J6rAZabuvNFAtF4bvexLBqFlpK2wj7xJ9gQ6fs2YdHt78s8o1VmuwzwylkA9OKyYwKeoNE09w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kmbxSBiROCb8pD3nszNj74Ykgq9mQYMhc_iwiJMFwlzcvRWgsFSv3KFkrcqfDokyCN5e0gZk2PDdO2cjmnjVx730Kt0x-HZ29Q6LM-kZ_oVexSOtxu_uQJCoMGlcmLSTfqU47Kn0i-H6aYUBfqaSjNFoQYPuWM-9-1m0t6lBT1U08f8n7Wsy-1CIqvngkrQ_9yVBbktScTlnWkkeWlp8lqB-iJb44MciJP7DSbebgDJdN9TxBI7P1XsBvzcyUhkqd8tnlPGnOMlVhumwFMIHMOeM3t7f3lzAHnG3I0eXW8k-SKsV1MU7pKIxhcQ-Av_33oQqBLirCB0lU8K8Q51FzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VWvhSFwLTopxUI3ZGfd6vV5xPkcL7DmHtz0ZEP-ZtMZZXua7BGtkzIqL59xPiB_akp8tQc57tblYvvEhFEeR5EUBx1d_T3J13I_s6zNb8wJUgxM5V50kgqRulTqTa6F1wdn_DGoXUlXhRP6TATVKpvxVk6gKF9mcBFvyRQmXX6mgfy0ozKPCMT4vnYC6RV7uNVsQ5bV9I4m-g0mWHmuo4VwzxZd3bxysSt8upUjBAuX-yOzMJZznvOCUoMGOzbFDznn0-NlBfACSlBXs1z-77Ila9bxA6epIivHw93432cA4ZcdUcRotYSWz7GwF9NJo2i72vIP9tAXk2I0J0vS7_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qhl4mIudyq4FBaq6y9deryV79uT7XOADtku-pQWzbtvsUz0rkwPPRkdXkS0AdirlkMbr4aulQibr6Y9l0NrboJlhoxEK-4P3MCc-r2yR2i2nyVkssjr5UBXHYmf8F7ej83Hw-9rJdJw8tPtBGC8IEV-lJASbOQk0MVQvCYIpQRc7yKdsJ6KdaZOaKb07YICXOPFpY5NpHrSZbhKgKwEjxqiRG7lRHPAqTQE8v32KtzxyzZas2RHU26JstTC35m7XJcbE4esa7pq02kU2O3e0WwnQc-0hfKYvEpgg31xGDWAWOj43dpKAPdnmWgSmIZ-8jfaUymsaubdB8czT-SVlwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/keaOAh0jayiCeFdM-LDn7MKkjrLvHew48CF15pqu3uCK7SmMRi6DeCyuTK8DuPZ-GhT1WZmofsFNZ2qkjQ3GijWCz6ibBOGxkOsj-qeiY1jL1kzFsPBMhRaBL2uVMyhRX6b6qdLwSHzMtSbX84fVdSAgrzE03Of4gkXUuQpo_Xe9B7nOEZKD5Y9pKjMO9XHbzw1rgnyJDfDiy29jGX2hvTWSoDJNWRQlV4JvpVsWVsI12GL-GiUsEaDwKkSZ0ZtDT3o4uM3uVSAkRqONelnHXMnVvLyPwHaw-b2MfKiBuYV9hyjWMGY1YKCpJL28EIP5bqQhS56zzdvCGTD9ZIJjrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cx6fgXgeqJK2mdgxhT8CGc8gjKo34021TJ4F1WI9I62S_vudxlhkEK17KpSPN0r2Z60PnCZzSrFQqfvvJ1oMK2HXi-t9771CVP6Eyqr9dPKzJhyqx9b2Gg9uJLLNqvJ1JjEyMhzYjHhruEkVvpk0uHwfUW3DyPsu6t_jXXtNDUOiUPQ5c3Wt9n0khE68cb7LCLdhBn51B1FZwXlyeiuMqbdZQgpkhLIiXeAVfDj7CzTMpY7b-c_nR44sTOVRp1ogHsM-PHFL_rBG8HAQrF3Zknh2DZZyIlp9nUCibqepMWUCMvxgLKI41t0_twjc3PEWiBFzaa8Eo4J-aCxdW9Q1lA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
از روش‌های قدیمی تا ترفندهای جدید؛ ۱۰ نکته کاربردی خانه‌داری
😍
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/676911" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676909">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-bQy7PlkzUa6y5G0Y2jIc9bY1OxP0uaLZzG2yJGaLVaEAWmAqQTuUUbgA50uQCmbUzh-g1BY8JKaAMDdXz0KyB5wvC62M8XeDw78yHH6fhsLA7s8M3sisSNbVkMkOsYKABY_e1NXTUNzVCHMocSRUFEua4c0CoDQTDUizhfDL38ElH9n5IXAA5cRmzRsErbAaj1hygaVr77q5N-i6nZ-KRLVkVmxz-6QuhjYpZWbNFVrhRdeOuOsicx_3uxX4TN33aY3m7JdGE45UDxUoe671gL2wLNYgHXYEDU7tUSsJ78CV2Dfq_8fZADIVf4IzuW-onwVpB4OUNJanJZho9LuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/676909" target="_blank">📅 10:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676908">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b780c515.mp4?token=Fcy4NkzCV1H-02Ygxmx4qzU4bTy-8AJy4kGklbG9Fph7k0e3qmyqJdWsPZ18Q3NYpoldkf0rfqMQcXYXtafc5h2sn8FY5ilRwC1CJYCC5DlVjzsD5vGGXLAVc3zBTvraTy41vn3lYr6T_tQrOBOEMLTAMy3aGc9YJ3AMsTE7gefq1aYAM7IYO4efeXKYqGd3kVtpTPfLs7EhY2h0QntkL3CQE3z2o4xq_38YAB5OzIonYAO9yRQse6YxdF0qvXqq44UBTDNxBdSZxrz01WFTng_OXUAQ456sxifLZwfzOHUlvq7kmkCYUKO7QuE14IECy4OeUeZepEvKWocyY6cmKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b780c515.mp4?token=Fcy4NkzCV1H-02Ygxmx4qzU4bTy-8AJy4kGklbG9Fph7k0e3qmyqJdWsPZ18Q3NYpoldkf0rfqMQcXYXtafc5h2sn8FY5ilRwC1CJYCC5DlVjzsD5vGGXLAVc3zBTvraTy41vn3lYr6T_tQrOBOEMLTAMy3aGc9YJ3AMsTE7gefq1aYAM7IYO4efeXKYqGd3kVtpTPfLs7EhY2h0QntkL3CQE3z2o4xq_38YAB5OzIonYAO9yRQse6YxdF0qvXqq44UBTDNxBdSZxrz01WFTng_OXUAQ456sxifLZwfzOHUlvq7kmkCYUKO7QuE14IECy4OeUeZepEvKWocyY6cmKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عزیزهای عراقی چه دلبری کردید
برای مردم ایران برادری کردید
آهای اهل عراق، آبروی شیعه شدید
🔹
شعر تازۀ احمد بابایی در وصف حماسۀ مردم عراق در حمایت از ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/676908" target="_blank">📅 10:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676904">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3548ced87.mp4?token=PLWxuU7XgUVzlYLTX-icZCucyFMmrbcM2spBq40d4XE2Qugk2GRMfraluDorZebSuNzz_uXX_T5bM9zz9JGhNx33-47pfuaW_06ZN--y32uuqGvqLXIWWap3_8E9eaqOJW1dgVobqyY5lWgxcGePBdoo9by5V4ul2kl5_jfconzcrjs-qenCOIPONJErG3O0jx09dJ8u9HTGi1yAFyuzrF6fHJ2XAbJWfnJkRa_yZ7eiWj0yN_7OdUcZEkaVQ3WUve1aLovbShlE8qGBfwlrdTPjgIr1pxvSzyJc0gTb6Ovw2KUkYCJNSXzPllCSgLIzCyNWQG9zNYfZiOOjPZrzTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3548ced87.mp4?token=PLWxuU7XgUVzlYLTX-icZCucyFMmrbcM2spBq40d4XE2Qugk2GRMfraluDorZebSuNzz_uXX_T5bM9zz9JGhNx33-47pfuaW_06ZN--y32uuqGvqLXIWWap3_8E9eaqOJW1dgVobqyY5lWgxcGePBdoo9by5V4ul2kl5_jfconzcrjs-qenCOIPONJErG3O0jx09dJ8u9HTGi1yAFyuzrF6fHJ2XAbJWfnJkRa_yZ7eiWj0yN_7OdUcZEkaVQ3WUve1aLovbShlE8qGBfwlrdTPjgIr1pxvSzyJc0gTb6Ovw2KUkYCJNSXzPllCSgLIzCyNWQG9zNYfZiOOjPZrzTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی شدید در نزدیکی نیروگاه هسته‌ای انگلیس
🔹
صدها نفر در پی وقوع آتش‌سوزی گسترده در منطقه ساحلی سافک در شرق انگلیس تخلیه شدند و مقام‌های محلی وضعیت اضطراری اعلام کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/676904" target="_blank">📅 09:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676903">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
پاکستان: مذاکرات میان تهران و واشنگتن ادامه دارد
سخنگوی وزارت امور خارجه پاکستان:
🔹
اسلام‌آباد نهایت تلاش خود را برای بازگرداندن ایران و آمریکا به اجرای تعهدات‌شان در یادداشت تفاهم پایان جنگ به کار می‌گیرد.
🔹
مذاکرات میان طرفین با وجود درگیری‌های اخیر ادامه دارد. پاکستان از طرفین می‌خواهد که حداکثر خویشتنداری را به کار گیرند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/676903" target="_blank">📅 09:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676902">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3224fc1b2.mp4?token=Q3_F0WetKN-1fiebGs55op2FL5g4YWaf-O6ObKpT4pKLmiBdgxkJTQIRFFbtnB2sDc7zDT2hZNLLion4dSkP1UIlbxN0rjQ2V4AvnZr0_Tgr0g3Rn8CjxeZzbDYK7wH-EyRlhaGgVbxble3IHxxudf08M1oFGGaZ-1JANDd_Hf8U7JkN8XTQsAiG0nf-hhzwueVGoWGRIrSW4dKNPt8zc2kyMu27u5VyhgK08yqxW_2DhQ1xMgl3-g-HkfoIWD962053r59capGxphUQusrD5gxwFzsJJbEENnB__w9X4NMrsfVwBnArtYylVjs9XWag1Pq3lzDMzxoGG5oN_tpu2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3224fc1b2.mp4?token=Q3_F0WetKN-1fiebGs55op2FL5g4YWaf-O6ObKpT4pKLmiBdgxkJTQIRFFbtnB2sDc7zDT2hZNLLion4dSkP1UIlbxN0rjQ2V4AvnZr0_Tgr0g3Rn8CjxeZzbDYK7wH-EyRlhaGgVbxble3IHxxudf08M1oFGGaZ-1JANDd_Hf8U7JkN8XTQsAiG0nf-hhzwueVGoWGRIrSW4dKNPt8zc2kyMu27u5VyhgK08yqxW_2DhQ1xMgl3-g-HkfoIWD962053r59capGxphUQusrD5gxwFzsJJbEENnB__w9X4NMrsfVwBnArtYylVjs9XWag1Pq3lzDMzxoGG5oN_tpu2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی نزدیک از فلامینگوهای تالاب میانکاله
🦩
🔹
مهدی محبی پور ، مرداد ۱۴۰۵
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/676902" target="_blank">📅 09:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676900">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqzohLgVMS_VX3U_p3QUYCFyMsL4XwSaAXWnHTuEe3Zbh70Pu3NZ53PBnRr4CGWqhrumH90WLY2F2_403vwK5bfViT77tEZy8FCL7hi12fknjOxMrKK3z1r0UvtXmQMpWFktDwENEXnQD8PnqOc9rL8mHidjw4eq-WVXUAwBZ-LwK8I-VmN5sUfCzXnhHTEAptZLJ06dofewYtof9ijHcPRk66mY0AgPDmX5YBoCd9xvvCef1S1oFHUfRaBb1aykxVHtrYJoV6scDJh7AdfsjdIL-cF0Xvz762-nrqJSh2yfsl6i_6-Skd5DB0Tv4lshCx2BvNm9C8Jy1CgKMJovDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لحظاتی پیش، فرانکو بارسی، اسطوره فوتبال ایتالیا، در سن ۶۶ سالگی درگذشت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/akhbarefori/676900" target="_blank">📅 09:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676891">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E4T8q4wa-JfLEwBYooEuCCxVCWiWw_Km3N5Fg0uUfnabP8KDZQC-rMd2jNb_ENuvGx9uWKcPHYcDPWqlp2wnDhvF6cKXAzG6oD3fjZQBIdJ66jFJXcCo7_tnbeRJsewMQ6ykTOYjjULTtpyLft5sfwOzmuD6Ph2oQFG9ro28U9OG5TdzE96VkmxpcYlXzlt5hedlmoFWDAPVjbmAqQMVp3_p5QqYnpjye3_ljZ1FiUzt848KgBVq4_ghKmmlOLW4yD05fN44UP_FchHS8Xq6tnSMdOLPlZ8x1JkeD9dUy5LjBcyeqhljLQS0DH3ThHp1puZiI4sSl0_0Wr1oiZiQdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sEaUAPENAl2ZV59I-vaxI1sPJHeNcDCTaJAgVXxrYYv8vPeEhbWQVsNpxMw342ecJfxk1u3VaAGiSLVyxQDG5yg-fghW-zyCrxDZnVaclCs-ALX7z8XBkeFoivB50yhcZNQEruqkKlDojK9wSxxkbszZ4-f5xoJgkWLf2Z0zuLxBZ_CysK-U-HirSYHT3ZVkhMJ4sm55e3soEvIRokISkb5wLK7itFOu0P_vncLvYWOgIogRyjYSX_VmQuAde-6PECOe79Jt3hKKOiFUQFnqhdvv_v9MVa3VVNBTtd7JcwKjvWdFTrcAkNgcIQh96tlBPaTk4y1H81OoseLdo_tz_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZiODNAOphy4DZVflhqnvj5EDyTB1zZJTDOmM_y33bmd2_19rAHSyrog9_Bts9tDZaHesZWl9O6RRz3ErEkYHENtCyqxQaVzFwv5VK3IO1dDJhq7xtItZtKS_7jqxeWfe5wgvyf79ydFuP0kqaaZdznS6u505iqiKP1rk2fEpULa1fk8Mc_nWG_aQv9peE7XSztMEFXql-06TkNr_t1jasfCLm3T1EDJGOEvrqUdSlPvYqifhh0Nid-0myJecdg2DP1K8ymhZ-eYKkF24eQ2ADGDhwDn04nEAN8J2ZE8GHa6f-4JLvMPpdMAzoYtgXM5FunfTl9gvRocqzrONQvF1rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HJ-nCQ5JWLNgLvNDCsW4vtwQcn3SZQayE8kf_mRtR0V6NHQOWJcjECVzGI-_TmzNy6uHdthcSnyNZIGo4ce1XeB3mnoc3IZCPR9ZVAe8cGEbNYxxXD7XYz-HfY4AOZieVT_dbXq8U3BbYVqxjWNdsG1caNoXOHhEW_rJBU2irYwNLHtOyzVMmeDIgR7n0rLTN3gBfMTfMPxRvRvsBORcK0deELHzhzVwZkUAdOpLG7Wep87Mx6gT3FRWYJ7Q_n7naxsc3XA15fgwVIJigLEQ4g2DdpHPWSLTEKcXkIAirT32ifUD8O-3sZxM_eNTAEte82wStmknYiugtgUwph2X4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3nVGjbyTlC9jZ0iCqdUEms8LmJ7TKZu9SzhDkc64Ijrc-rd6qgGhjRim_ljdoZVETJfVKO2kHHopkE2ts7qn0A5c47yYVCfxLkNkew3I51MQvL8B2jegO3nXjiP4YHkfMKGTDVJBE7lejffmzEYuaSyBKGtKGQpBxufzMsfocqk4ZoGEXvjNFL2-akFSua-HfbueZfiJgICkca5kp21gJOEh9LHISN5Qq61RHx0FGED6gNh05-RHlQPQeJTntNpOF5n_8b_KgvogfOD9CMmTlG0JcwdpM45u7A-f_wD184MoHfBBLRAWNgFixwfVa1yvmWyd-jYjjUlEk5m9cr4Jg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۵
دستور محبوب برای تهیه سوسیس و کالباس خانگی
🍖
🍖
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/676891" target="_blank">📅 09:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676890">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhAjeE6soeP3qZmH9JDy39N92_oH4AV1f8tdXL8AcL1ydG7wHSCQd30T5XSg5YMFiijLDuEF-aVkX7VYz9pRwtnj_JSxMY0WfyIzKx-OH-a4wD7NnszM512dMOU3fCCa76fy0PjSCjMna7Ema95_CGT-gmylBuq8_lN_31X0COvAUFPQMkzvti4vvRHR8s6og8t1u2A2t0Vdgv3FH6k1fAV7LudWWrZVDb9I3h_VCL67i5i-PL-gcbCFbF9xflC4oa5_8vcZk0869TNN2idDdwkgcxZA8fHs-GkVYE-y4K22yMGrDQVqUfwNQWkRti5fMXYfZJtnPvvH7X2wzsTwrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خوک هار: حماس خلع سلاح شد
ترامپ:
🔹
امروز، شورای صلح به یک توافق تاریخی در مورد خلع سلاح کامل حماس و تمام گروه‌های مسلح دیگر در غزه دست یافت. این یک گام بزرگ به سوی صلح و امنیت پایدار است.
🔹
این توافق، یک گام حیاتی برای این است که دولت فلسطینی جدید، که با شورای صلح برای کمک به مردم فلسطین همکاری نزدیکی خواهد داشت، سرانجام بر غزه حکومت کند. در عین حال، اسرائیل امنیت مورد نیاز خود را به دست خواهد آورد، زیرا غزه دیگر به عنوان پایگاهی برای حملات تروریستی مورد استفاده قرار نخواهد گرفت.
🔹
این یک نقطه عطف مهم در اجرای طرح ۲۰ ماده ترامپ است. این توافق به صورت مرحله‌ای و با ساختاری مشخص اجرا خواهد شد. با تکمیل فرآیند خلع سلاح، نیروهای اسرائیلی عقب‌نشینی خواهند کرد و نیروهای بین‌المللی حفظ صلح با پلیس فلسطینی جدید همکاری خواهند کرد تا امنیت غزه را برای ساکنان و همسایگان آن تضمین کنند.
🔹
یک سال پیش، جنگ وحشتناکی در جریان بود، بحران انسانی وجود داشت و افراد به عنوان گروگان در اسارت وحشیانه نگهداری می‌شدند. ما به پیشرفت تاریخی دست یافته‌ایم و هنوز کارهای زیادی باید انجام شود.
🔹
می‌خواهم از میانجی‌ها - مصر، قطر و ترکیه - به خاطر تلاش‌های مهمشان تشکر کنم، و به ویژه از تیم برجسته‌ام که تلاش‌های بی‌وقفه آنها، این پیشرفت تاریخی را ممکن ساخت.
🔹
تهدیدی که از غزه در ۷ اکتبر ایجاد شد، دیگر فرصتی برای بازگشت نخواهد داشت. در چارچوب این توافق، غزه سرانجام به دست دولت فلسطینی جدیدی خواهد افتاد که به مردم خود خدمت خواهد کرد.
🔹
به همه تبریک می‌گویم برای این دستاورد شگفت‌انگیز که، همانطور که همه می‌گفتند، هرگز قابل تحقق نبود
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/akhbarefori/676890" target="_blank">📅 09:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676888">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d04c147610.mp4?token=ecg67hVoCW9lT9cgCA7YjeADk2ncDFNBVKj0OuBSQARg2AINMlWAJ4GFzObIj92IA18BdhEhtlViZAOznGCEMcu9grHaX2wwSbF0QGBx4kINudfssZITAbtVKSzA11hNZfzZBPad0M8zFoCMsYJOil9nxZs86Xdb7K9rftXfVoEi-MeyIGfLn2ELV460x0zafsQtnwsHhOo9oovHCiGUXSOpVWHGhUNC0H05bxnFnUTRV9QDN6l0qdnjgOaRWt_0bH8oKDrVFaPVOQjyVidnNAwdjKXxgkSyRqF0cJye_O_COF72tZVoA95aWBm-U2s-569CtYXyOcG-6fVf8I0Mo0hAFjg8zKaPXfyLt9LqCd1aF2y6fHdJ8YTxGKmRBVMj8Ngz_YKuv9A5LBt0dXLv-ZRaUseXoe2bjx5oh3uponU_sHYD4m281GGFx42V8nrrEn7afd6H0Qg6Lo6P54uBgPxw2czIZ0JBJJrlqHfkWa9gicKDJK97a9Z6qe6yNLy1Azt03ez00OJj21QizRNYR_9AhtIHHTN51HbPUpvnRH8nE2JLy6W9GVQIMtZx3VL2rlloqXhRtKrKfw3WZ6iymZdYtdH-xSNHVlUr04mhhJKdBtbu9VcjtVnbEvujDrpQcQQ2w-kkZmzW6iOERKgSfpMLYVKgHnZXSiWRBPEWgys" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d04c147610.mp4?token=ecg67hVoCW9lT9cgCA7YjeADk2ncDFNBVKj0OuBSQARg2AINMlWAJ4GFzObIj92IA18BdhEhtlViZAOznGCEMcu9grHaX2wwSbF0QGBx4kINudfssZITAbtVKSzA11hNZfzZBPad0M8zFoCMsYJOil9nxZs86Xdb7K9rftXfVoEi-MeyIGfLn2ELV460x0zafsQtnwsHhOo9oovHCiGUXSOpVWHGhUNC0H05bxnFnUTRV9QDN6l0qdnjgOaRWt_0bH8oKDrVFaPVOQjyVidnNAwdjKXxgkSyRqF0cJye_O_COF72tZVoA95aWBm-U2s-569CtYXyOcG-6fVf8I0Mo0hAFjg8zKaPXfyLt9LqCd1aF2y6fHdJ8YTxGKmRBVMj8Ngz_YKuv9A5LBt0dXLv-ZRaUseXoe2bjx5oh3uponU_sHYD4m281GGFx42V8nrrEn7afd6H0Qg6Lo6P54uBgPxw2czIZ0JBJJrlqHfkWa9gicKDJK97a9Z6qe6yNLy1Azt03ez00OJj21QizRNYR_9AhtIHHTN51HbPUpvnRH8nE2JLy6W9GVQIMtZx3VL2rlloqXhRtKrKfw3WZ6iymZdYtdH-xSNHVlUr04mhhJKdBtbu9VcjtVnbEvujDrpQcQQ2w-kkZmzW6iOERKgSfpMLYVKgHnZXSiWRBPEWgys" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خط و نشان تحلیلگر عمانی برای دشمنان؛ رژیم صهیونیستی نابودی‌اش قطعی است؛ ایران تا ابد می‌ماند و هرگز شکست نمی‌خورد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/676888" target="_blank">📅 08:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676882">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cbb6ca0bd.mp4?token=CobBhiiuN_OPI6ysH8zi7Ot2H5-oeAyc5p4xbq2QX-0w5d25UTiYB7RYyh9ZVOvIlWSNT9DvdArP4M7eLgOYSUo7hoNrO0mOp9DF1dGM6WhbMNBvdeTPvwFRPpYB5m0OulIB_H3flzJxeW8ZrU_GH3qO8tSwwi40QPwXpVN-YlNu1XytrG-nzFK27wT4t6JlK9KlBdLaYmM83hlaw2-VTG87V_AWlmagvrWFatTIEQHlSQ7I5b8KOZQp-x-p-BBeoa-pCZG0gad_JO1KmwpJN0vgYJLLdxJQ67CSdHXjKqKJJqIlzH2_hnbdvvPlMtjxojAEhvf7EP23HhG_iy-vEoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cbb6ca0bd.mp4?token=CobBhiiuN_OPI6ysH8zi7Ot2H5-oeAyc5p4xbq2QX-0w5d25UTiYB7RYyh9ZVOvIlWSNT9DvdArP4M7eLgOYSUo7hoNrO0mOp9DF1dGM6WhbMNBvdeTPvwFRPpYB5m0OulIB_H3flzJxeW8ZrU_GH3qO8tSwwi40QPwXpVN-YlNu1XytrG-nzFK27wT4t6JlK9KlBdLaYmM83hlaw2-VTG87V_AWlmagvrWFatTIEQHlSQ7I5b8KOZQp-x-p-BBeoa-pCZG0gad_JO1KmwpJN0vgYJLLdxJQ67CSdHXjKqKJJqIlzH2_hnbdvvPlMtjxojAEhvf7EP23HhG_iy-vEoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به‌ اندازه نیاز خرید کنیم؛ از خرید و انبار کردن بیش از نیاز خودداری کنیم
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/akhbarefori/676882" target="_blank">📅 08:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676880">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7544b67e8d.mp4?token=FZNEMRJkyrEVkCgEe9ir3y7DUhaQe4xama8LYqF5IbO6PjKsvO0UZvKCqb8UVGicUI2qPZW5N_BalkwC1Ep4GjpqcVPPoPGLIJ7lVUZW0CAoE0SWGpr8DDeW_G8L_8ifbjpte71RsH5Y7Gm8b0dYtzcANz8PCao91sulMm7MX0TrCx9Yd1RNwL4HAdgZ2LLnFdemNlw7I2edIs4cwTrnlI_4yaloUnalhHZfCqIhp1HQTVqXsg_dQY_tbYbr47YTU5citbc2zG3T-jZbg8tdWgdLzMa_O2FG4ZlIfcWoYjfH_uwTKZ_EPnLKDZhpx4_qQiO1QhllTKtNLgbFFbc5Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7544b67e8d.mp4?token=FZNEMRJkyrEVkCgEe9ir3y7DUhaQe4xama8LYqF5IbO6PjKsvO0UZvKCqb8UVGicUI2qPZW5N_BalkwC1Ep4GjpqcVPPoPGLIJ7lVUZW0CAoE0SWGpr8DDeW_G8L_8ifbjpte71RsH5Y7Gm8b0dYtzcANz8PCao91sulMm7MX0TrCx9Yd1RNwL4HAdgZ2LLnFdemNlw7I2edIs4cwTrnlI_4yaloUnalhHZfCqIhp1HQTVqXsg_dQY_tbYbr47YTU5citbc2zG3T-jZbg8tdWgdLzMa_O2FG4ZlIfcWoYjfH_uwTKZ_EPnLKDZhpx4_qQiO1QhllTKtNLgbFFbc5Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشای رایزنی گراهام و نتانیاهو برای تعویق حکم بازداشت لاهه
🔹
تصاویر تازه منتشرشده از گفتگوی سناتور افراطی و جنگ‌طلب گراهام، با نتانیاهو نشان می‌دهد دو طرف درباره راهکارهای به تأخیر انداختن روند صدور و اجرای حکم بازداشت او از سوی دیوان کیفری بین‌المللی (ICC) رایزنی کرده‌اند.
🔹
بر اساس این گزارش، گراهام در این گفتگو بر جلب حمایت دوحزبی در کنگره آمریکا و افزایش فشار سیاسی بر دادستان دیوان تأکید کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/akhbarefori/676880" target="_blank">📅 07:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676879">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHcLfTjDls7K150yirFccCvD8yxbwChp8mPTqYz6f5mmLZnlQnuHCOGZt8Z8g5nF8QrLC33QQ8iSbofdCOZjGkZlI1EDGQPhuyhpBenkXh60I-Ubycgm6vYyyZjIIEaZB-r-WftanceQSNoZWY_XAdC03Sk6MS09WZdeBcDb-5X6mXYeeryGMqXy2wMZV24SBBkJVmNuWOwy6sc-WXrgjrxT8F5sE5ypSvW30ShkwIQ2uosElCt-HfSbCbwxBDhFxRnJ6T1scScienZ38Y_HN9WjwwxKS2UNQUZbgVF97uDt8kNUaggMN3eGHB_8_2RnZKyU8rMaeATk8JJm_CMbqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۹ مرداد ماه
۱۶ صفر ۱۴۴۸
۳۱ جولای ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/akhbarefori/676879" target="_blank">📅 07:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676871">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4bbc91c80.mp4?token=dCs0HIVf_Cv-GvkLnPqnlx-HXMFnH-G_VjUzRg2P79ZTxugwUzYxD4saYa7J6A1xRnsrNFBs_Z0tk1Zl4FXcXIBSauRofF3Of3EOMnAjteSRLQEUOTZsgCh2FRVdSudbXJCu4Ps1BJnFqWqXo6MOTZXq8y3njmTh-ucKDshqoN0sCFH39tfLbwR43-_i6x3dLI690H6WSGp3OPOvbdFwdKO1ZI5PEHWYWI1s3298JP0HyMcrQg9cp0YO3TdBU9vY5XrUWA2_NPy-NhvgtuwSCUmaGz4EdAHwrE7Qk2Sk25bTt_wxFBdrI1bD-7xFevVT0tKpzBF53hIoB9AWNToYoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4bbc91c80.mp4?token=dCs0HIVf_Cv-GvkLnPqnlx-HXMFnH-G_VjUzRg2P79ZTxugwUzYxD4saYa7J6A1xRnsrNFBs_Z0tk1Zl4FXcXIBSauRofF3Of3EOMnAjteSRLQEUOTZsgCh2FRVdSudbXJCu4Ps1BJnFqWqXo6MOTZXq8y3njmTh-ucKDshqoN0sCFH39tfLbwR43-_i6x3dLI690H6WSGp3OPOvbdFwdKO1ZI5PEHWYWI1s3298JP0HyMcrQg9cp0YO3TdBU9vY5XrUWA2_NPy-NhvgtuwSCUmaGz4EdAHwrE7Qk2Sk25bTt_wxFBdrI1bD-7xFevVT0tKpzBF53hIoB9AWNToYoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش در اسپانیا
🔹
ده‌ها هزار مهاجر مراکشی با هماهنگی  صهیونیست‌ها، وارد اسپانیا شدند و حالا امشب تعدادی از شهرهای اسپانیا رو به آشوب کشیدن و ماشین‌ها رو آتش زدن و مغازه‌ها رو غارت کردن.
🔹
این آشوب‌ها بخاطر حمایت محکم دولت اسپانیا از فلسطین، لبنان، ایران و…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/akhbarefori/676871" target="_blank">📅 06:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676870">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
ادعای اکسیوس: کاخ سفید و «هیئت صلح» دونالد ترامپ بر این باورند که حماس ممکن است طی روزهای آینده توافقی را امضا کند که آغازگر روند خلع سلاح و غیرنظامی‌سازی نوار غزه باشد. چهار منبع آگاه از این مذاکرات این موضوع را به آکسیوس گفته‌اند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/akhbarefori/676870" target="_blank">📅 04:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676867">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac84668d0b.mp4?token=F00UAQ8vHjcnlzacaoJYYFPyYFV_shKHMS1LT1u4GJV8pXYQaobyaHrloueI0X8Y6AbCtDv2MV27uzTAue9VzHgFBroMqoXW3tQEn3vOTRa1yTx67lJbophe27QnCHAzHKdSQz5mn25vXIP0qQ3UjjOdd2ISObrN0NuBmGoQeG_e5_k43E1yivoo-aEvhR1V-vYNc2DiJl0eqvJ0AbmCNy6Uxh3oZWa5NzqbxxyDEM9wVo-O5Sutprpjh3ESWDz9FX9agnYkVcNAiLRCCpW5Ixiv9dT1Rm3M3gKS8g2QdWDfq_DabT7cHbpiyfSrwsBgmcDBk7KwTmHQkbE0VcK8dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac84668d0b.mp4?token=F00UAQ8vHjcnlzacaoJYYFPyYFV_shKHMS1LT1u4GJV8pXYQaobyaHrloueI0X8Y6AbCtDv2MV27uzTAue9VzHgFBroMqoXW3tQEn3vOTRa1yTx67lJbophe27QnCHAzHKdSQz5mn25vXIP0qQ3UjjOdd2ISObrN0NuBmGoQeG_e5_k43E1yivoo-aEvhR1V-vYNc2DiJl0eqvJ0AbmCNy6Uxh3oZWa5NzqbxxyDEM9wVo-O5Sutprpjh3ESWDz9FX9agnYkVcNAiLRCCpW5Ixiv9dT1Rm3M3gKS8g2QdWDfq_DabT7cHbpiyfSrwsBgmcDBk7KwTmHQkbE0VcK8dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش در اسپانیا
🔹
ده‌ها هزار مهاجر مراکشی با هماهنگی  صهیونیست‌ها، وارد اسپانیا شدند و حالا امشب تعدادی از شهرهای اسپانیا رو به آشوب کشیدن و ماشین‌ها رو آتش زدن و مغازه‌ها رو غارت کردن.
🔹
این آشوب‌ها بخاطر حمایت محکم دولت اسپانیا از فلسطین، لبنان، ایران و محور مقاومت است که پروژه آشوب‌ها توسط صهیونیست‌ها در این کشور استارت خورده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/akhbarefori/676867" target="_blank">📅 04:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676865">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oN_vXyF_XOVLfMiPh3yEF9VErx4nH2Mp8pX4Q7nyTJ-lp4bP2MqCNAMYR6VD7q_4z0lyl9UT0K_lBo53tODiDpTlI-6krlwJg05gbkdOErxdBXVIWCIOyd7h0beXaQ3TRTcl3GZXvFuNUV3KsyNH4PAZ0pWAhoBU-plEzjMwZkCTdMgHFyX8JxMsyTkAIo8uZzRwfesWRXGpmbHWs3USTvkN4OrEkzHZsv5jKImLsKi1UBEepbFVsCpjszwVBijQaBPradeqqld-LoyUa7HEnYAYOlZLXHxsm4lkanjGEF18c1h7-xNK2KCycXd5E2bapi4r4MRstO0HfGUJGpbqRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هواپیمای هشدار دهنده E-3G همزمان با حرکت تعدادی از هواپیماهای سوخت‌رسان آمریکایی که از تل‌آویو و ریاض می‌آیند، به پرواز در نزدیکی کویت ادامه می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/akhbarefori/676865" target="_blank">📅 02:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676864">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0PXIq6hybZmGpQT6-YgNgB6MeR1Wt1DisuH3YCT2OVnMLwsElBl2AbtF3RdA0wdqH9PoshiFGgaZJfhax3WRoKecD9V96Q2JzBhuND7xjiAA-s51Cqr7X4uRJ17e1lv1mk0Fq1QnSu8so3LHwTolMMxwVgZof8oFWPDxgy5mCr9wnuUry5Q4N6sPgYPSKIF0tCstyJO9vB157hqcnlyjvr8wblSnjmJ7qKxZkjl7tkC788jNyQyHaJkl1NH3wziEY4pmKDwsdd7ltGpJkaU_H0s0DUqaeWi9_fVVD0V7OD9JTADCPNwwP6E2GObdyCENsqzcvmP5m8UrmWFPKuGwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پس از حملات تروریستی عربستان سعودی به عراق، ملت عراق تصویر ولیعهد این رژیم خبیث را روی سطل آشغال ها نصب کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/akhbarefori/676864" target="_blank">📅 02:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676863">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
ادعای اکسیوس: کاخ سفید و «هیئت صلح» دونالد ترامپ بر این باورند که حماس ممکن است طی روزهای آینده توافقی را امضا کند که آغازگر روند خلع سلاح و غیرنظامی‌سازی نوار غزه باشد. چهار منبع آگاه از این مذاکرات این موضوع را به آکسیوس گفته‌اند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/akhbarefori/676863" target="_blank">📅 02:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676862">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
انفجارهای سنگین در مقر گروه‌های تجزیه‌طلب اقلیم کردستان عراق
🔹
منابع خبری از وقوع انفجارهای سنگین در مقر گروه‌های تروریستی کُرد تجریه‌طلب مخالف جمهوری اسلامی ایران در اربیل واقع در اقلیم کردستان عراق خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/akhbarefori/676862" target="_blank">📅 01:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676861">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
ادعای اکسیوس: کاخ سفید و «هیئت صلح» دونالد ترامپ بر این باورند که حماس ممکن است طی روزهای آینده توافقی را امضا کند که آغازگر روند خلع سلاح و غیرنظامی‌سازی نوار غزه باشد. چهار منبع آگاه از این مذاکرات این موضوع را به آکسیوس گفته‌اند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/akhbarefori/676861" target="_blank">📅 01:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676857">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a48c959043.mp4?token=Sgv013d-JfenihorM5g3BA9NUpkQE-vZAYlw0Kj2P6vCo37VRA68z47HFM5bsyEpw8wHAzmbC8OT1MODdoc4i7mO7y4sAaH4embyLCWlS2xrdpn4cijZUxJ_U1jtLiTrWhZ5LMfPsN2V-XfrGkjx31ud4hLiRAb9r9j65hQv07Ca9IS9ncCu5BH45Q8m-_x8fd-htwW6daBeMuRQuEzjFjttXJq73d4Nocu0nEkie8lIEhan32beQKOqz8IiQhtCV2NNtFbAj-ZwiXwqaQfhkDQIeFeoSli1RBLm1Ufyj_hiBXGypZNJBMQfm7tHPbgzrGjg2hZNRuyiQFcCJdIIUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a48c959043.mp4?token=Sgv013d-JfenihorM5g3BA9NUpkQE-vZAYlw0Kj2P6vCo37VRA68z47HFM5bsyEpw8wHAzmbC8OT1MODdoc4i7mO7y4sAaH4embyLCWlS2xrdpn4cijZUxJ_U1jtLiTrWhZ5LMfPsN2V-XfrGkjx31ud4hLiRAb9r9j65hQv07Ca9IS9ncCu5BH45Q8m-_x8fd-htwW6daBeMuRQuEzjFjttXJq73d4Nocu0nEkie8lIEhan32beQKOqz8IiQhtCV2NNtFbAj-ZwiXwqaQfhkDQIeFeoSli1RBLm1Ufyj_hiBXGypZNJBMQfm7tHPbgzrGjg2hZNRuyiQFcCJdIIUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بحران در اسپانیا به خاطر سیل پناهجویان از مراکش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/akhbarefori/676857" target="_blank">📅 01:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676853">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339d6a9891.mp4?token=h5hRYZX7YxlzID75d5rE82GtwTXhwNOOszQbgEFsJ1R62OG7yre7MA0DP2b2E8zWyCbUVT62ohOshmbEGc_yAAYDNHyT9f21LCDRwTrPrguVmv_ZCw4GWGJ-5EGbEyGpkqrrxDhn2e9AX6s2gHUfKCWRDz1zbtlK1dMNhU1BFKoXe2zeZndBW4L-gGoYjGJDrtsT11BkV4xeEqNw1OUJ63ste4LisFHPOW_DRBhanEejk3ZyPZVWgKEyU1-I5UCvPyUzdFPhw2yuYMn4EVlvg4MiozQdp0mEZTlu8BHUerlAPVQrv4oHvIofFx6oQp1cFzqDLyN8ewWSaOb_3V6fsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339d6a9891.mp4?token=h5hRYZX7YxlzID75d5rE82GtwTXhwNOOszQbgEFsJ1R62OG7yre7MA0DP2b2E8zWyCbUVT62ohOshmbEGc_yAAYDNHyT9f21LCDRwTrPrguVmv_ZCw4GWGJ-5EGbEyGpkqrrxDhn2e9AX6s2gHUfKCWRDz1zbtlK1dMNhU1BFKoXe2zeZndBW4L-gGoYjGJDrtsT11BkV4xeEqNw1OUJ63ste4LisFHPOW_DRBhanEejk3ZyPZVWgKEyU1-I5UCvPyUzdFPhw2yuYMn4EVlvg4MiozQdp0mEZTlu8BHUerlAPVQrv4oHvIofFx6oQp1cFzqDLyN8ewWSaOb_3V6fsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی پربازدید از عادل فردوسی پور و وزیر ارشاد در حاشیه مراسم یادبود اکبر عبدی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/akhbarefori/676853" target="_blank">📅 01:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676851">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f579c094.mp4?token=AOQuc56XXQcAhEpgpHytTtz1vQSDOQLMj1Ts5SYTwSKZc9HkWB3Q9P2FWrKRQtGCNejBRCZkh2GZlMzDH6F3WNQKyth8EBdYjCfWzBHAibqVIL4b1jpJD1VYP_d44U6XCvr_WeqTDZ7Sq8ZviCbRRuL-KYgdhNUTkRJ2Gzbw8LqzhveL9hFzZhLyDmPzQIoJ-vuS6Pbv443F1sKjzGwn-DsW3dBNz4X-ycEzCU30EK1kmX4JjWAzP2lGCqqqxQkd81gnfeX02j4ddzGc0PswXFgx-__guW199O8umPCT4i26IMtNK8J9h4Q8RTvwCXu9VtMlUggqpwNHMkv22G6r_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f579c094.mp4?token=AOQuc56XXQcAhEpgpHytTtz1vQSDOQLMj1Ts5SYTwSKZc9HkWB3Q9P2FWrKRQtGCNejBRCZkh2GZlMzDH6F3WNQKyth8EBdYjCfWzBHAibqVIL4b1jpJD1VYP_d44U6XCvr_WeqTDZ7Sq8ZviCbRRuL-KYgdhNUTkRJ2Gzbw8LqzhveL9hFzZhLyDmPzQIoJ-vuS6Pbv443F1sKjzGwn-DsW3dBNz4X-ycEzCU30EK1kmX4JjWAzP2lGCqqqxQkd81gnfeX02j4ddzGc0PswXFgx-__guW199O8umPCT4i26IMtNK8J9h4Q8RTvwCXu9VtMlUggqpwNHMkv22G6r_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکر شهدای حمله آمریکایی-سعودی به نجف اشرف رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/akhbarefori/676851" target="_blank">📅 01:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676850">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2544901f6.mp4?token=GZBrYJImeDm-tfXW-vhIBW7QpDjg7T_XbITvovkIlRxgFhcMwRTu-kjFcsMa8N1md02lkdF6qiBGBzkZ8wxGXdUC80jThUWAziGyiPYhGYcx9slE3EwuAsSAORtzmszG-yNGzZjVqF-cQ-eZVTGJIUfHxxxkm31Uie_4-2LpwTxoSkyNdxnRSO4OGKFJAmBj-puQtesuQXOdLP3CtkpqSFevZn4qQ46sFGbLO2DLcWzKnG9DrYtjFGKpJISj1ouyd2BAZEFWvwTnbR_S21OjdLomCme5-tmvW1Cl3kq_MQWdQicDXhB5f9yTtlsxMnNCBRhTqpfylbCswKtHlam7dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2544901f6.mp4?token=GZBrYJImeDm-tfXW-vhIBW7QpDjg7T_XbITvovkIlRxgFhcMwRTu-kjFcsMa8N1md02lkdF6qiBGBzkZ8wxGXdUC80jThUWAziGyiPYhGYcx9slE3EwuAsSAORtzmszG-yNGzZjVqF-cQ-eZVTGJIUfHxxxkm31Uie_4-2LpwTxoSkyNdxnRSO4OGKFJAmBj-puQtesuQXOdLP3CtkpqSFevZn4qQ46sFGbLO2DLcWzKnG9DrYtjFGKpJISj1ouyd2BAZEFWvwTnbR_S21OjdLomCme5-tmvW1Cl3kq_MQWdQicDXhB5f9yTtlsxMnNCBRhTqpfylbCswKtHlam7dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هواپیماهای جنگی آمریکایی در آسمان استان نینوا عراق پرسه می زنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/akhbarefori/676850" target="_blank">📅 01:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676844">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/igbQAcQQ0GyIt8Myc8Sj8bjk53BhpOIdSSpQrfz1w7axbQ2qOCHrG-DSiNOV36Eh0DgmviWMBBzcnRIpZqiV3fLpBgnTqxwStwGblP8MZjstr7Dm4Nvb9704yOci6R4hA-ZI5WPCLnM8FykSxAXCPFa2PZKCbP0jLYBAi0tRBM0Yg7t63H9ClVglFPRrBqA3OTL9CDwvTgaGeTZpDQjC6lEx_li-qumEDbZIfUfuMTLgLPnkbEA5ulkIM8xc2qNLn70iq2vZxG12W-uz58NKTBv1Yx3Tzvbgb22X_2OFbpxtq8vC4wUXpNrvL_8UPSU1lO1ZBpiZR1jnb5ROzjJ1FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/svhxwxrTwWm1D2sL4EfMxSUJ__lZp-hIKcpliYnD1v_K_mm9Iewle49qTUhgmAV9Ubf82sVgwsclmKViNjD49UoDSAsBL7egMSmxgE0O6VtOQ1tKLXhMZa62w2NHNvbuIgdV23p7kRj7-eQ9wmNqx30oBqL85Xnu23HmM6WOKnDZ162tXFcQk8VEFetqmw8JIjefipLw4vFATxIV0w50-gG88mLi8aprP0K_11-li2vDdXqQ4odA6hTMcmSDgiBsBvyJTSfXzQDEcfczL1wCawfzAYtNsJe16-fBRVlV2MbeATKA_gXsfdAg0wP-jXcbpjUYoFkGw-znttFoL-pVhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cx8Fa8uqePLjFGDfv0A98A_3xJCLcws6bheBgd8fg7OqazpUs4_QUsIX5cufjVPQXd9FufYRtoTE23KetIzYoGH1pMxPnnQlW5ubZLDVz39c9bFIog5IXrfWFuM3fxEBVaV3if4Z_dnDXNlAM9GclNHSoOVvBrKTLZ8P9R_EenliklR96VRSosud3sX8Q3sbe56ozzFW11RlTHR99XQggFpgvhx3AbLGqtK3MiUd1jdA6m6JKrP5mp3cs1iwwLTZYvtVtLf0UZN_bsOCngKpDF0SzIIlLlWPYT6Qc7tsUNOAUoS0_CyB7esyI2uYbuGJ8WdBeFT8P_Zh5lfxGxBWng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eIIolyPKkWGC1IGKzxG9TM2cRIcNhfs2SeVCJG4w1fbaXpU5U7ThzegYbvfbRxsfbeqISrQWl4XkcLAh8T2IDwcj4F64tb7-H-oHB69UhYUHc3oI92UYG0lG8LEJTK89p4Nu7nTv0SHmW9R29AGnv8VU9300ZqZUAndxomlK72LvPovWXLGeyq6p0cHtpdFh2nJJV8QEzkRHY6Kckoq26OGkLLdg5OLXODfyExTAahpesX9RAAanQwfDnDPqXlp2RFJv8F_-6TjEM1MyA3U-y-gRFplRLTEfBtJPEzR3l5BuC1WJDgGFIdpMqCJvPjQvSI48yR_rk9MKPBzKTspp-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SApfhH2oWPhYbF_i19nZuvW_aE5LMqbpsBT3mbhXiZMJHj1mZsqatUzmZ7ol-Hen5kvtPL1M2rTj-XXyrfsUUGbFhwBq_X9px34x_J1Rwup5XdcuQP0U2ioZDeW5M1jfR8K7VQIUNhFxQ8M9-gFMUKtr0cychALiN7kqfUyL5WpnLuzrSLT_JIxR6ldf5gwCdEtWTrZMcLS4OO7rjV5alWSbuQsFz3KOOvIeeoEBN1tvBoaCi399mF6xiAmecDabbOyDemlbhF2B6PDhZl6i1KHY6jB3yFYuedGnYf1tfd6hpgKPqH2AhWUUb15McahoUEUGKdCkFwQL7x1aZhnaew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
غروب زیبای مسیر طریق‌العلما به کربلا
🔹
عکاس: نسترن کرمانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/akhbarefori/676844" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676842">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCNqHHV3n-qF8eHLG5Qm6-4kQ7WgBhQ3pIl7xl3Rzlzye9adLuLcHDt0NGDfPOBuO8zpvPRWIRjXfuEI23KMFQADnlHVhym5Ydp8LJ8uThAZw5GCMllznuQ-ZOQ7Ol7PCXrsJqTONh35HNTYNNw4raWy5CK1Ie20uh15t4ZbtrsoHkEqAHssno9e_gOV3EfQuKCPOeM7ewPZncIH3_9QRP5xL9MyyOkE-IRdnizj5-sXYDIb9SjCxe1IdktT8tI6yxsng_1KHfLFKO1PzItcwnfyLY4g7eOVtsuzMfNAAipMDKoxdz1xaFMuIYi4PNx7ZiArccyka08hCCrmv0V0VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صبح انتقام
🔹
شب گذشته حمله هوایی آمریکا با استفاده از بمب های سنگر شکن دو منزل مسکونی در جزیره قشم را هدف قرار داد که در پی آن پدر، مادر و یکی از فرزندان یک خانواده به شهادت رسیدند و دو کودک دیگر مجروح شدند. نیروی هوافضای سپاه در پاسخ به این جنایت رمپ استقرار و سوله تعمیراتی جنگنده های f۳۵ آمریکا در پایگاه هوایی الازرق را با چند فروند موشک بالستیک هدف قرار داد که سه فروند f۳۵ به طور کامل منهدم و سه فروند دیگر آسیب جدی دیدند و شماری از نیروهای فنی و نظامی مستقر در این پایگاه نیز کشته شدند
🔹
هشتصدوبیست‌وچهارمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/akhbarefori/676842" target="_blank">📅 00:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676841">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d06e1b886.mp4?token=fuVzT2pc-U22eSiDrONH6JNQ-j_4rSzXMfOy4UQYZ5f25MY08d4Dbk7TOrrYxA8g5VQoLjXvhMTyQye89g9pMEnU5roWace_lSUgoFeGa7P9WePj2tuCAum9T-BoOvhizsCUw6IT93KaP2cYD_pjmjuK2ynJMjWV_hCOtkEARkopgtLpzxPlpK8NjG5lunLhzi7QQp7tDi6Se4SMFOaeugAW5tA9Sd-0kHdyFmGDznS_XiM_P4PyevHZHS0sP9CvB2CRSDqQhy4jNw0QYba7qbd7bZ9L14tDXtCDFD4QuNVdQQ1iTXfuR3zNeRdJQwQF45-30gRGszFmgVvS26O3pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d06e1b886.mp4?token=fuVzT2pc-U22eSiDrONH6JNQ-j_4rSzXMfOy4UQYZ5f25MY08d4Dbk7TOrrYxA8g5VQoLjXvhMTyQye89g9pMEnU5roWace_lSUgoFeGa7P9WePj2tuCAum9T-BoOvhizsCUw6IT93KaP2cYD_pjmjuK2ynJMjWV_hCOtkEARkopgtLpzxPlpK8NjG5lunLhzi7QQp7tDi6Se4SMFOaeugAW5tA9Sd-0kHdyFmGDznS_XiM_P4PyevHZHS0sP9CvB2CRSDqQhy4jNw0QYba7qbd7bZ9L14tDXtCDFD4QuNVdQQ1iTXfuR3zNeRdJQwQF45-30gRGszFmgVvS26O3pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علت سختی‌ دور شد شدن از فضای مجازی به روایت تصویر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/akhbarefori/676841" target="_blank">📅 00:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676839">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/921eea2f4c.mp4?token=F6VNE7H7yUOb05xMxzUpRclSgYkvRVTNPIZh0Q3dh6xreyStSQvllXnhosiFW9TncUWhIatnnN8tFwHUlnosRWfDppogGA0eipg39Ku3UvD0eNaF0Gzq01JJ-nCbRp4c9P8lVje5on5hSvhpxstfPAq9TAEeLdTAjZq1WAB5oj4YGYhKb7jVsbtsKgIk3qheLjhf4xNdIsCLoq8qnLvPhYybvMhj8TFrgAtPnDcDLjhHVy2RAFX3CCHSsU6sQa42M69gmIBkx04vxwnZ8d9ch_Hid-4DS4JkfMvQXNLd8YnDTSWSLl-Ng930GKQle6yQTqVLgbkEMCAfe4AaBsXp0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/921eea2f4c.mp4?token=F6VNE7H7yUOb05xMxzUpRclSgYkvRVTNPIZh0Q3dh6xreyStSQvllXnhosiFW9TncUWhIatnnN8tFwHUlnosRWfDppogGA0eipg39Ku3UvD0eNaF0Gzq01JJ-nCbRp4c9P8lVje5on5hSvhpxstfPAq9TAEeLdTAjZq1WAB5oj4YGYhKb7jVsbtsKgIk3qheLjhf4xNdIsCLoq8qnLvPhYybvMhj8TFrgAtPnDcDLjhHVy2RAFX3CCHSsU6sQa42M69gmIBkx04vxwnZ8d9ch_Hid-4DS4JkfMvQXNLd8YnDTSWSLl-Ng930GKQle6yQTqVLgbkEMCAfe4AaBsXp0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استقبال جالب مامور مرزبانی عراق از زوار ایرانی اربعین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/akhbarefori/676839" target="_blank">📅 00:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676838">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hicfS2T_OruIghrm6dXaW5o4LqSSeSC7p5L0ZVVXWwrZvxVjdCiggnbdirXPFiwe4uZsTCGqjr-MmIhlCZMUFN-TqeM78NHfD4BQBbdc7VXeUuCOsCHfVd-Y7xaGR3a9zXtRpeuNM8F1AYicXcZLPwSHWgk6f25l2JDDPzQ96Zf16aQ45XyyfApyynpSxnn8Rjo0iTaccvP0fznkDexjUtpUtDE6kwQgmNl-ztvGk9gO3loqXas0GtviPAHX0GjETh-KBNG4c6P6hvsAssqV17If7QVmlTGicJmI858WeHGpijAzhjwqO9lEP2si6Ld78vJxT8dlGgEGn4lhYxXWcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مکمل ترک اعتیاد
‼️
‼️
✅️
کاملا محرمانه برای اولین بار در ایران
بدون نیاز به بستری بدون درد خماری 100%گیاهی دارای نشان
سیب سلامت و تائیدیه سازمان غذا و دارو
🔻
اطلاعات بیشتر جهت ثبت نام
🔻
📝
برای اقدام به درمان فرم سامانه زیر را جهت مشاوره پر کنید
👇
👇
https://app.epoll.ir/80475925
https://app.epoll.ir/80475925
در داخل کشور تولید شده
😍
😍
✅️
حتما تا ۹ام شب اقدام کنید تخفیف ۳۰ درصدی و از دست ندین
خدارو شکر در این اوضاع و شرایط
برای همچین اتفاق بزرگی
🙏
☎️
جهت مشاوره سریعتر عدد ۵ را به شماره تماس زیر ارسال کنید
👇
📞
09379940040
📞
09379940040</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/akhbarefori/676838" target="_blank">📅 00:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676837">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
جدید‌ترین تصاویر از حمله به بندر دمیاط در مصر
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/akhbarefori/676837" target="_blank">📅 00:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676836">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPUBGjJO-6ATVveUAZ0Bll0GEbldLBeWeiHn8G-TdYa8Xc57tvTSYdfW8p6xUDv2vZB45ekewShmoumjuOcNUbMvczs0_lZN83w9Lu6cZGt-xs0w2BtGdTaet4j4ts0k7x5fANV5HvO3Ds0-tQK7UHwlztce9DBxJwLfZ2uDp7dd7lfRc3XeDyXMYPGk31VIXdL3y5cTFziWugN1giB3EM0lLBpPaLRLYozoJ65nAEs9gJno87TgzJAjb3gTZcxhYjWyZiZyM03GgDaEdohCWwPlfSYFBsJxIIYZTdaeZCFLPqj2opkWsJF2h72tbtThf7JUZ8Gw_mWp9YgEdubcPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با این تکنیک ها از هوش مصنوعی پاسخ حرفه ای بگیر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/akhbarefori/676836" target="_blank">📅 00:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676834">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWsm87bPNlx7J5ohc0u9hfa6-fSVCB83E5Ffp-Gea9UHHRgNPlcBMQfFX7TMC6t2_QnIw18mTQGhGTDhsZ8ErmvqizKgFVC-rJBS9Lx5PxmRnbIP5dsGbj7MUsoglG4eF90XT8rGEO2Oq2XMpOy-x-d_GFb_7__ZntfxScoYLEUbri4795nfjwmKbJakj2SCFrD56p4vkTl0TaXNuS6m6jtv7_IBAB9Bo8M1-Lrolu2Ag-s4YRMgvMENUs0CCtT5ixDYFKd77uATpbEZSEfLkzX5euXNbZr7vhl8Xk7mkRp1wTm3HFBsHSMXOqQ0MixyeAx_2Fjmv3t0YQwjnb-5_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک موشک بالستیک روسی، کارخانه تولید پهپاد در کیف متعلق به یک شرکت ثبت‌شده در ایالات متحده را منهدم کرد
🔹
این کارخانه، پهپادهای تهاجمی هدایت‌شونده با هوش مصنوعی تولید می‌کرد و گزارش شده که کسی در این حمله کشته نشده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/akhbarefori/676834" target="_blank">📅 00:08 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

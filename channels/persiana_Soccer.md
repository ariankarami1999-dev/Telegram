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
<img src="https://cdn4.telesco.pe/file/fKMnCr9Q6qCGF6vrgSyQ65ICG454TEJGbfmQT9z9-LFkyDsyxQ3YoHiaEUomy1vOduTewkxiR3eoPwgUv6JuWffdDRPw5BjoyOY1zk76UN9wAHHxkQo4O8p9iAKINl9tnAKMWCT4rZcJxInxY2f-t1epCRYtvk5rZo_LiXeNXkEQRQKIEG2oMWBVEORrh8ORYywZeiah5BcZ9Asu7ORfoyhHzJ2ZQ9ATTZk_A7s_cZzUEbyCzpDbymzAqgYLngMSoLuwApwzFfFkRgYejeeypBGRywRIdeF-SU-l2FU32N9BQuAhyZ7tRmhZ3nUgRyPWPjCl-ZfEIBCdcBbziccfsg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 423K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 22:35:41</div>
<hr>

<div class="tg-post" id="msg-25303">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxfK14LyCWj9xZ0O0_yNeksymMnzVde7uZVENjG5uq1vROR4lk0poY7IzuqHz7UMLYJwlPHvO-lfo1DoyDSg7huHRepzPlVFI0qe3NFvBrlNShX5Jnh7b8tg97q7HCib51G24Dc3yxaKH9WQ4ntPXv7kIPAvVo2zueAzHuCf3x0R6ZnzmbYLzcT0UCV1e_IETJNPfNvenUQovVoS8kgG8MJyC7I9X3dPgBy341Eb_lQy0Olg53NjONObYARQhO3V_R7NdbxMKS_lWMUAlEfEpD_Gln5efa5VRtG22yeg_gjF5Udpc7O2f-iJ8W13BVBxw6kDBIgBtj5HJMhY1Ws2uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/25303" target="_blank">📅 22:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25302">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZjg-bepTUOBdNybqIBPyh0r9CB07lBEpN7vO7mF4q0dv8daKIIcYlhrHXZ_GNy5GV3PkUPPWY_bsxjKlX-cG6cOU4KAspWBo0761VuwN6qPLjJ3DVPW-lfNVVBRCrSxu5fSotLTYSiZdbX4na06C23HmLaiAtpZYx79IRbwJSsqnb3ceE7ptcoSx4wJPa-kG3_yZ9MAVz6Bkf0A9UipWItdRCTO77IkaVjVQ0NHK20EhgCGdUIJ_WJmVsdJZ-MtrkVqgthWFZCbk9lU9YYOA3JwUa9po691I6dkTMGWqyRxZYbBes0pi1kF_4i5HzJeUHj9D67ddmcr4BPx6WDizQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جلسه‌مدیران باشگاه پرسپولیس با مهدی ترابی و نماینده اش شروع شده است. تا ساعات آینده تکلیف ترابی با مدیران باشگاه پرسپولیس مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/25302" target="_blank">📅 22:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25301">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJ6zhttKK9k0v2r6KUDd_HVDl0FbgEZ6ySjesXfUL2Njx2TL2GMMCP4TyWWdDUxxa1gawCoXYAhfSQ8m7LSQOQUf_zXvoORzAID6DqJ73Ne-EfdC1M16aG4aQRmNjPUfv84mAFjsrjLZ6WUeUb0B7_nYW5d8mK2KX97R58-TlPpS23LPiSm7L3x7mOt-ASIhv2JCIsirfX0e5-dtbKzViIdRxn-YKd8yShkUqwxU5UqR5DLEJdQKUCS-4d8HISugZDQvdE68HVpxwT8Jo1f-wehAzVwyo-x41igIYksNlYpbfyC5WddMtiyofuDR7Uw48bv1moHlRQZBOrl7A7nmzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دیدارامشب‌ دوتیم‌‌ ملی‌ مراکش
🆚
فرانسه در ¼ نهایی جام جهانی رو عادل در آپارات گزارش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/25301" target="_blank">📅 22:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25300">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxkjPg3ijis11g27MYenI-XglC70WSRUdRmvlDhX_MeOBCoxB3ASsYmCW7sdlhWpae9Y_arQ-K0hoc-uGsSuT2P1ERtd2pnCjyVLdaxldGa1ePWKkuB6Ovygi9U79Z9g41Q5CyMmSxbCJ4dcDJIkSXNHJYzLc9DMDGTHatDTAJE6WOx-K8-nZNhdHPbgna_Kfd0WGkRmS32ClchDo1OF7jxzcyBAQMbX6fUL25K-N7kEoqLRQgr02PuQBNzpL1irLSZJtdcoiGHooembfd60gswtMZ1_uLNbYByWZzRWAdpwmVyuxqy_kG6bKwNPrEkKcKJhiCwOTBw4BwRh9T216A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تقویم؛ بیست سال پیش همچین روزی ایتالیا با غلبه بر فرانسه در ضربات پنالتی قهرمان جهان شد. با این حال، این مسابقه همیشه به خاطر اشتباه فاحش زیدان و ضربه‌ سرش‌به‌ماتراتزی تو یادها باقی مونده.
‼️
زیدان: از همهٔ کودکانی که اون صحنه رو دیدند عذرخواهی میکنم. هیچ…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/persiana_Soccer/25300" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25299">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bb2pG7iZEzqYAvzj-g_C0CSwGHBQ3aqueK8qO73k2M655S_ZtahGFSVgz4-96KJPmF5PW2TDta3oERZy5A6XDh9aZByujWMEVyvJRR6OnBcN3aZVpi1CNh9zQsD_AMXGshTSdgf-9CE2gU2V4KW_obGUezpoFAsfhPVA0lkfCP8Aahn289wbCmfapcf-Q_ZXmL2_5TUgO9xT495GCEq3PX9l3c6Tu1KgE-oOhXr_2kN7Po-f9qDTCYnCqRu5od8Sf72idM_XktgdXdt_OOhM0KesYrtqMN8hJ6W9A6YEDh5jTNl0YSmdLH-p34db0KKi0ddNN-O9guJJxJHlZRQMdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
باشگاه یوونتوس برای عقدقرارداد دو ساله با امیلیانو مارتینز دروازه‌بان تیم ملی آرژانتین به توافق کامل رسید و تنها توافق با آستون ویلا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/persiana_Soccer/25299" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25298">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKnKHpX-Ez0o1GJH3PyfAVOWTs5b16TFeyWS3AQ1oMGbtund922Fh_0TlN1QLv0PdXRUqf82NKFfigi516x8oxK1wT26O2ZM0k75JpMLXoLt-y1tkjuc_vNJwwe1UIN-tq3-bZPjVJoz9xaAiV2AMNzAa8XeD4BuC82oOOslXed3Z2mmXteBEZebch27dPejHRndzp8z5cytAPDbxkKkQKmwo5omseHsw3a0o8W4v7e9zJ4ldcaSnxY1LAP78zZkKbqy624BT9h_Yx4i99SBotm2V2aOdQtK9YiFDFcr3PIc8E9DZ8eIQaw8CrRU1vzZ940MoMtHA3DKTsZDPLVo1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
مراکش
🆚
🇫🇷
فرانسه
فکر می‌کنی کدوم تیم برنده می‌شه؟
👀
🎁
۵۰۰ دلار جایزه
بین تمام افرادی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، طبق قوانین سایت تقسیم می‌شود.
👇
همین حالا پیش‌بینی‌ات را ثبت کن:
https://t.me/betegram_bot?start=p4_r4EF37DCE
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/persiana_Soccer/25298" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25297">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYpcqdD6ByE2owceYe1wNzOxdzz444wBctYch08YV0HCGWUvRf8ThqzWaQ8kskHyIYiwTuMc4P978FaDP8GZxhtkHT2ZEyzNprm7A0SKsBfkGDbHyA_RHgxdWiXLQEfh6pWchlmEOCS7fXdpWuYOmowRFceLXo5AYznldtZogceyJCkOvewidk4DhoSZ5sP6ERQi7sSDeNgKiyUIvp5RZ5tcOaRRe_7g7ResM4GlpDVdIx6CtGxyvtquML4ZApQ8fTnpZOoI5CSvrLlWJozNXyh8hv-dAYu3c34uaTLn8xA5JFrzjB5ABGc9Qg5aYFHrg-39LDWDsFBI-jUCxYCNYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
طبق شنیده‌های رسانه پرشیانا؛ هفته آینده جلسه‌‌ای بین ایگور سرگیف و مدیریت باشگاه پرسپولیس برگزار خواهد شد تا مدیریت‌سرخ‌ها این بازیکن رو برای‌موندن دراین باشگاه برای فصل آینده متقاعد کنند. سرگیف بخاطر مسائل خانوادگی قصد داره فصل جدید رو در لیگ برتر ازبکستان…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/25297" target="_blank">📅 21:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25296">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJ_ynT7dHsY1H_jPrZHJmTGp40vv7kJxXS94y2Rv3bA0N2hDGjvudy-TT3oPgbZf1HAKvXAsf_o0VzgwnJmcR9mpow1F-Os9DTxBGtJy-w69wMyXU2zhdbtMiUK05XULeweG0nUOKgh72mDZ9B4ZynTa4E9c9iEuZmwN2jwHIqeuJEPK-bQoUsQbosgcjWzAB20Oz9_B2y0TY0515idxU5A3n6w03q0mTrAWLOCT0KNstgZ4WgeA2LKly_P6BoHOjgGgJG5yFOFh45OBwxqRAFQxXIHkNPTX_dX2-R5oSXRUZu5bg5iyNPDXCx3gqTfz2-73Xse3rfb9uUcsWY6-iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
بنیامین تانیاهو
: راستش‌روکه بخواین لیونل مسی 39 سالشه و اون قبلاً هر چیزی که میخواست توی فوتبال به دست بیاره رو به دست آورده و بارها شجاعت و بزرگی‌خودش‌رو ثابت کرده. ولی واضحه که هنوز حرف‌های زیادی برای گفتن داره. من در جام جهانی طرفدار آرژانتین هستم؛ حالا از فردا بازی های آرژانتین از صداوسیما پخش نشد تعجب نکنید:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/25296" target="_blank">📅 20:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25295">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECd2-Pof3kcXpG-i23OY2bvcjPl3FbAQj0_5QxHpCep4qDI-Z_Kx-u8i9M3FA2ro33s5_oGNE53P60ORzjbz7Kio_wExNQjevN_ntnQssSMmfo-MIpNGCaYtegdiewnfj2ij0mBqgc2QCZ1molzjPgfMHnC3yFVJ1Pdd3wI3nXBCVYbsZ-RFdKJvh_wJQ5et1BE3t10MLQzNP6xHtFjGp274BQkpFX_BQVw6v4-5rJJoiK1mgdamm2qJ0ZlK46b6ZW9Efp6D0MxgeM6E9gniGlgy-WO7YRFGqzI63V6S7CavU4yufo0R5v2wlmXWJVisdm4mCjLONiCOklrsHtXojw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|داوید دخیا سنگربان اسپانیایی 35 ساله فصل‌گذشته فیورنتینا آمادگی خود را برای بازگشت‌به‌باشگاه منچستر یونایتد اعلام کرده‌. دخیا میخواد دو فصل در منچستر یونایتد بازی کنه و با پیراهن این تیم از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/25295" target="_blank">📅 20:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25294">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwJtQXhRUnaxSviHcTJX03SkE_yNj5BZso64tzdBD2NVYRlTJ7XovnQ_BIahzVGET2GPPhXc_FiY1SVBHhoW_qfqZcqxxWFHnuFTp8kL8Fv_gXrpFIFb1U2DUhOvt0JKHLUITEqd3xBiAa65JqNPlaeNTmyeSZDejwHuiRHlMOisIkKc7g6CMhnLQ6nEJZqDGd2nyRA0_aq0RDheq2sZEgHXLAgtnVNVMtU7VPMyBA8CctWX8D10Qht2H8cjZj3d3Z2J8zDc0_Ta2YA_QhYB7t6viYE4TfQks8LkUdXkHzdm9a4upKLLSY_9oDtAtDIKiez1QybxdoAvQ6CCoR06SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ طبق اخبار دریافتی پرشیانا؛فرداشب‌حوالی‌ساعت 21:00 مدیر عامل باشگاه پرسپولیس در منزل مهدی ترابی جلسه مهم و سرنوشت‌سازی خواهد داشت و احتمال اینکه قرارداد 2+1 ساله امضا شود بسیار زیاد است.
‼️
پ.ن: دیگه داریم لحظه تمام اخبار داغ نقل…</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/25294" target="_blank">📅 20:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25293">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Twp7h1DuVPA6pLVwCcMJjOrm1MExBxmKWcwMFDh-vJS4v3bw7X0RAU-qPXQR2nS7OYHD3k6G3nENhGD-lgJ-xSryw0GtXeDt5dFuBQPYEQmVO905Qm144yDfB3uPR23Pecd1AHGgaXJS2yRcuEKLAP06I3jIxv376y4OOUZwXCiKNT1D3YiMoJYPw2gyGVMKguBpYGvnZQh-MqVY14iUQyq_LBS2IS_Z7s33OPE-m0zQsRdfiiOEBrYvNUhTHbBxRYXLqbvZ7Ky6n9BbrOm04YqwIETbM9K-b0ClbcLAforuFLhJSAFQlbdBI45YKs0b2JLFbL-LLNv_D-fH_qZNjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/25293" target="_blank">📅 20:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25292">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XG3lpBbPg5Eabq7dm82zdkMHcsf9I1hijuCJCHVtCNu48oIZcKlc95jokyaybFV1wRFW50osw2bjLwV0DZA6sx9gDSHUTPQYTVbyafqbjF0qst5Nn-39N32k8B9VfNvzxJlkpRenRdSLWmd0cpuXm24fHCoXwfFghQj-b3bsWC1uN_20HT2KO026l9cpPTSWKRIGXmfyJMnA5mq3bLK5emWL9Fr0C9G4Z_t7nV0XSPZgmk8KBE6zW3J4PjmWg4wHIIyadSnZjs4_Swl8vk3braVMeCHiHgtS7SpXztVkt8Bqwv5fF6tp-FlS84vVWUQg8LOJDhDniujw9MdbnOy1Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هادی حبیبی نژاد قبل از اومدن تارتار مذاکرات مثبتی باسران‌پرسپولیس‌داشت امابعد اومدن تارتار و درخواست جذب مهدی‌ترابی دیگر قید این بازیکن رو زدند و او با قراردادی دو ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/25292" target="_blank">📅 19:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25291">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HavWvbD-7j9z9nBFSi3S1GUfKLXcTp2jRECb2gGfE7ZaS_v4I9lXp1bOsS73b23X2QkU29GQeN5otSSo1tpLnQWZ-2j5vGzMjQpMjYragn2ovRryt6fA9V__twAv-psD2TryLnEFwFp7NBV0AIQ-eqJr2jSEnLc1ToiGHrS89lSDaoCdBXEjaPl8zbJlUUOEVM9P3EmX_CNrSyn7xQJD3dAsP6RDbxTxlZVzpn4giE7gARYNJPe9LtqarZr8okUZ4gUW-vILGqD_emudcUpYsABgswDhe7mB-o6TzqBX60QcccS0rtJBo0RTbRPqlfWLAJJyr4Hf2fDcuK0mTWulYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیرورزشی باشگاه‌الوحده به محمد قربانی گفته هرباشگاه ایرانی دو میلیون دلار پرداخت کنه رضایت نامه ات رو براشون صادر میکنیم. همانطور که دیروز گفتیم باشگاه پرسپولیس گفته ما تا 1.5 میلیون دلار حاضریم بابت رضایت نامه پرداخت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/25291" target="_blank">📅 19:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25290">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrGefmGesUiEcK49O9w7IJBkqFLp3qX_4lxmqh_7sfpHUsP8SEh773lcDLgCT_9uh3TTSt3IuAZ2tp-WpR0EXduqP0t-elk6EfGRC-uHX4j0BJuUq2YsPZPBPxyADVzVyfKIrAPxztCFIOwlOVYTL4l65L2FWfNufa9VXXZSj9UsD7lFUZ3UQfaErqZD4FmHKsr5Tu5Tc5EMmPkPstEXuu5YfH_vrfavGuJjc4B0NyM483N8E95IXKhrUrvH0xXL3D2KWYz6_tng8XfL4u0XMCnp2rm2h6K9c53qqZDKfCAmKiHM9mnmvH565bIJ8Vlh53JxzJbNeOY7WgeuBXzy5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
تونی‌کروس اسطوره باشگاه رئال مادرید:
مردم همیشه دنبال‌بهانه‌اند. تکلیف‌فوتبال‌در ۹۰ دقیقه تعیین می‌شود، نه یک‌لحظه. مصر نیمه‌اول عالی بود اما بعد از اینکه ۲-۰ پیش‌افتاد کنترل‌را از دست‌داد و آرژانتین استفاده کرد. این تخصص تیم‌های نخبه است.
🔵
مردم مدام درمورد داور و VAR صحبت می‌کنند، اما دلیل‌بازگشت‌آرژانتینی‌ها کیفیت و ذهنیت‌شان بود. مصر نتوانست‌سطحی‌که ابتدا نشان داده بود را حفظ کند. اینکه مسابقه "دزدیده شده" یا به آرژانتین هدیه داده شده تئوری‌ توطئه است.
🔵
بخش‌سخت‌فوتبال پس از باخت، پذیرفتن اینه که حریف بهتربوده. آرژانتین‌شایسته تقدیره. مصر باید به عملکردش افتخارکند اما از اشتباهاتی که برایش گران تمام شد، درس بگیرد. فوتبال همین است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/25290" target="_blank">📅 18:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25289">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXQw1D0zfdhMqPoFIhM9L8bCxtQyYVioWs5YzbjQRNbsYUGxLiYSJn166HRMXc8KlKJtm-kwHlviPIFH8pNbVtjAH1HO_nRRVFKZzBiHEOAD74N2vSbxYAxO-U28LCLVN1TSjGSGoOWqSIZRqn1JKUe-BOKPoSujsmi9Knw3xr52kBkLkOK9N5GqB06RVLXc8pbgM0V3Fu9_d2aoa2177tjzdbU_O3v_CNiQ17KlN6faT3__o7qwshiezpmbLxoOWz5bAPGOs8OCXUOHXsUWIe5DfdktS0MLSeU759yIZKcKu6XsbRgIlZbcRLM6o-SuQfxNEY-5Hq2b4wyXIDgyVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/25289" target="_blank">📅 18:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25288">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgDGydNJCcvO4ErEBejToy4PiqyKecJXxdjbSDb2hpP2NmOO0fmbfKbaluBFKxFDcw27o-341mvyWsdKaFcC_qGRBGuB3Fakpy8oTiku3Nh6XA2w_CBuU0CdT1gUqqBCZmZMeTofckcgUEm4Zehizaq1IPEAAcBVJTx1mui0UIeRfdEuVHEXShkGF12bY5TfJt3XpgAiQSqokno3Hy5A-818BHWBwTju8wMPhPjnsCJT0jIy68CAufsqKvi4qGDheEt4IrAq8rRq4yUiagxTO1OCOfutG56dqZ4_5aayMVIsNlqFNm0ybxlOztpqKocou7xqnth7Q6qK0wqih-QAAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تقویم
؛ بیست سال پیش همچین روزی ایتالیا با غلبه بر فرانسه در ضربات پنالتی قهرمان جهان شد. با این حال، این مسابقه همیشه به خاطر اشتباه فاحش زیدان و ضربه‌ سرش‌به‌ماتراتزی تو یادها باقی مونده.
‼️
زیدان: از همهٔ کودکانی که اون صحنه رو دیدند عذرخواهی میکنم. هیچ توجیهی برای اون کار ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/25288" target="_blank">📅 18:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25287">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAj-l2Bt2FkSorCP7NLtlgscKiK8riFh20ItJQ4GMyTbmpvNPG_av77G52qcPPSBr5da-HLG-T1wrw0dKczP95Kyk-0UM8GFq3c1GXq5bW3S-1K8koloij-3eYCOjAnF71sn3rJYA-QTN1OsVpLQjVafdE0HyV5X8eJs3Z4ImBkw9gsgmD7hcFKjqLWJKsQnfSmUp-w-_8JJ5_EeThm5J9APdIGHQcZjw2Zv2bL0bcWeM9Geda0Yeq12yQa5OOVaOJCBRXNNHI-XuK4fBp1s7nAE7-pLlkawvUpTEC920UkA2YwOWk_DG0Tdr7214h4NsrBjOKpUnTmbKtrEGU1u6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ طبق‌شنیده‌های پرشیانا؛ مدیریت باشگاه سپاهان درتماس بامدبربرنامه های علی نعمتی خواستار جذب این‌مدافع ملی پوش شده و به نعمتی اعلام‌کرده‌حاضره‌برای دوفصل‌حضور دراین تیم رقم مدنظرش که 150میلیاردتومانه روبه‌او پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/25287" target="_blank">📅 17:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25286">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4Btb80ne3590zhoMtVqwpiELq_oeSdFhrMCBiPINbAHut_KA8WAcL6trl6ZZ7ai33aVr0DwUw9NGAEzZ1v0LLeInzIw_u1DIAGWXS5CM0fqEO7X5UAjveVD4-Qpu0Uo7VfkuBDdEp3RmtWMDfmGVTVQMMzrT7tVTJptLjh9uG-z-efwLQ8aW4MEnYvfuTse5fH080jmcD3WBe2eSSVH_WmpXlrU4sSyEzhBTwzlkBpio3MbEs2uZYh5n2kIVNwxg_ceogb8YBJ8myR5gY0OiuRwL4hFPe73GmUu_h0gEeRMDa9iLu5DpsX4HwW62tXz4IpJQfayIiCAE9nx93ZvEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
درخصوص اوستون اورونوف هم پنج روز پیش خبردادیم که چندپیشنهاد از جمله پیشنهاد الشمال رو‌ی‌میز مدیریت‌سرخ‌ها قرار داره و با توجه به‌ چراغ سبز مهدی تارتار برای فروش ستاره ازبکی درصورت پیشنهاد مالی مناسب؛ احتمال جدایی اوستون اورونوف از جمع سرخ ها وجود داره.…</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/25286" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25285">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCdkOmd_Q3Z5bKvsEUmANVAvzHQ3SbTKRZd1zAm5f9jcCyVgSW76Ohn8o1mWnPLvT98fOh_687u2pAp8-Wwz5vPZt2x633dWIvVTDf6llv-xjQsV9cmaSZmg0M6SUJsxvRfAkRChRVdc0GT7Pe071uvTGJLlozlv39H_22uDNRIXul4RyG3Kk2OeYt05umIxdbWT6_9uXVa9ewAD3ufAcqE_fSho99K9zLhOafePZWFGrp4ybTohnSS398ayTLV_vwJlLY5-mUYbT2hgq2MS_G-CbEZ2qOANSOzCePE1CG16TmNNW6WzRtoltQOg_05A5mWKk4Ag7k1Q7-uMZPE9KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
ارلینگ هالند روزانه 6 وعده‌غذا میخوره و حدود 6000 کالری مصرف‌میکنه معادل 24 چیزبرگر. هالند عمدتاً به‌مرغ،پاستا، استیک، ماهی، سبزیجات و عسل علاقه داره و بیشتر آب مینوشه و ازتمام خوراکی‌‌های شکردار اجتناب می‌کنه. جاشوا کینگ هم تیمی سابق هالند گفت اون مثل یه خرس غذا می خوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/25285" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25284">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/25284" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25283">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LC00z27goK4g5gf7FI7reJlntqrY-rxGq4Mh0QzkZvDW2wKalxwFh82DpdPpG5PQY4EjR9iu1d8PTTWiCuxowG1d62iHJ2PK4mEGdQbLujhcbc-pjvdwRHGbK2wHLmzXAKWaGpwhssiEgzZWrXMAnIr1ruCNAg1URejjz62EanAramLFkON9JQwNeSAeO6_YllKqxEoPzFj3ccCxSjRZNCxV69GH9VLFjUYM9ALzsJjsXVxb_KDK7ED3VDq7Jfe7CWBpYhT5iwHriTLfF8qYBtYqjWQWiZdac0Bw-mTm8DmcBdC7548UoGLfmq85R5mDYnHrF-psMAxuAOF9oUk5aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
جواب‌ فوق‌ العاده رونالدو به‌ سوال خبرنگاری که گفته بود میتونی‌ اسپانیا رو ببری: من تموم تلاشم رو بکار میبرم تاوجدانم‌راحت باشه حالا هرچی شد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/25283" target="_blank">📅 17:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25282">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aT1YkV4P330oq4-9mvtHyevIii-tObMBEn9hPoTC8ApXfgNzZkvRZDlopHZsLDIkbWtcdnOX79OzkfsTuPHZyxezHu-H3Z5H6VBCBFzb1uZZpcKTATjnMy-EmeKBhc6L_FmZxb7twwH9yaYN3yNchVhFr9pDFPUUs3_wJEuY1-I7K-rhovv-8DvDmF_MaIqh2hJ43xUgME-rVj8e7Z5oAA7wErhnAXsEbOC5t4jvgCR5qhUmpGmmik51GQG7YILDDYaO5Jn0EsRoOerJnCidxf2UQjB2D5jeQkTLhHCdg_LsV3nV_MKTDqRClJh2OLXob0z_k8gUkM4AbBVVP8puvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی دو روز پیش پرشیانا
🔴
پوریا شهرآبادی مهاجم جوان گل‌گهر با عقد قرار دادی چهار ساله رسما به‌باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/25282" target="_blank">📅 16:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25281">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUNpWBKwecjFe1m4_AyHp7umMEz2eaA2RFRmPxZ3bShTh2IASqrHvYZ2zRchlM6z8AyQ6JUT2fiHz3QcKmrIfxYfBYaEsBgpHKA_fIcOx764Sx66u6i0zLhNaGHZXKoUMEzg0UOuPYGZctM7HMsPoOZzW6rAn0nybWTaJbs-0sc_L3j1t0qFNvCjni_4OdedatyzcG7D3fPP494iT5azie8zAB6ML2od-vR5WHhG_ghMx0VUib9SG6sBEWJexKOvIkoK-jkFPW86hVM_ExrT8rLGauqXBFd62uP2D1ompA6srzNyUP7HffLmya5VOHvIJ-mnIEGFAqTtfaibWGGCgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ پیرو خبر روز گذشته پرشیانا؛ پوریا شهرآبادی مهاجم 20 ساله تیم گل گهر سیرجان دقایقی‌قبل درتماس با مهدی تارتار اعلام کرده که قید حضور در تیم استقلال رو زده و اماده عقد قرارداد با باشگاه پرسپولیسه. بدین ترتیب شهر آبادی ظرف 48 ساعت آینده با حضور درساختمان‌باشگاه…</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/25281" target="_blank">📅 16:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25280">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‼️
رونمایی‌از تاکتیک‌اصلی تیم قلعه نویی در رقابت های جام جهانی 2026 که سه مساوی بدست آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/25280" target="_blank">📅 16:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25279">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7QHzCOVmH2YzFvNggK-Piyi8ZPfuqfKYErPxnbjSsKVwF0_LdFI3wYLI4NosCS7PVfSN7ar56yiRIV9IATPmPK0aI2__EVHB_ONep5BP8duiwZui3dNZTXytvUDwjjFOLRvQbE4gqwTSjqrJRu9EhaPRvpGxI9jNaVlH2MPPZjptZ4XI8tqlkMfAMLREqLshUaoHCqwPKi_YAPoNAPZ0mWT0R0-RyvbXIbkCwI8DQrVEd3ag6VHTs_VT5puOvCQ5XaUZJBTFcS-kXajBYOxbg0eFrpa448astT6fsAcXTDR0GXP5r4OkAxaKxYW9abCGm4LXgpX5sisx71yKf53bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیو لو رفته از کلاس‌درس‌محرمانه امیر قلعه نویی برای سرمربیان آلمان، هلند، ژاپن و برزیل در خانه‌اش بعد از حذف این تیم‌ها از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/25279" target="_blank">📅 15:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25278">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_liKjs4iGyhWa_apgo91ofu6HR2Ru8MCz8DnT7NCGm0A6n4ZZS7AVx1FMY-Qr2KK0peciwXIuj7W1evKBpURbFUTeHR7ipM-h6faSfnCqYNdn--v0X1OlayaLHI8COsLmg9ehCFEcXxdaMlFHn9Ubx5ny33HWO6bnbR4OsxSjNO9QIJXAsqVcFADgRjJUe2vMee1jPQvUCDI0qLWCbEdEqogum3YAn8SBL53P7dz-ak6cPxOY7IGobnV99iVlnmUn2KSvJJEthbr0NjG7jHdojQuGPux1-HXDCWEADZbSRLyovq8ffMtuHKuG47lm_2m9WG8Z3JyPO-qkGZFey5Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛مدیریت‌باشگاه‌استقلال میخواد بعد از تمدیدقرارداد یاسر آسانی قرارداد رستم آشورماتف مدافع 28 ساله خود را نیز تا سال 2029 تمدید کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/25278" target="_blank">📅 15:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25277">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2IQ7kcaah02utE5G9PQ2YYxXxXauN-uPEIDLpEnnjq8aySMuDEViF1lruZzW4y41hjhVK-Hl64AolcTzNJkKPEAzPYConU9herP7oie0DLbEqt8y6PD3XvMYDT3ltgOxj00yqMk3xInY700IIhC0d8nP5qzoRNvewfwU4uuQL0n9mAUqpx27PfChY18eLAW27gMQjxCPklYcpurnMuyfwFESsLFq9_7dtIj7cTitYUKY4cUie9EmKb2vRJfqtPRNd3QQ79XmjkdgpWHC55nv4AQ6QhfJjL_TnvtC5Y5K-kbg3ahl0XzhsGfKcLkHqIp418Nu1lLUd6GwOp-g-LSlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛ کریم آدیمی ستاره23ساله بورسیا دورتموند برای عقدقرارداد پنج‌ساله با سران بارسا به توافق نهایی رسیده و تنها توافق با مدیران دورتموند باقی مونده که باتوجه به علاقه آدیمی برای پیوستن به بارسا بزودی بند فسخ او رو فعال خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/25277" target="_blank">📅 15:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25276">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/en8okEzYzqUA1fabbnwDh4Hmup3yEyg8ol3No8uAsRZE9ktMvSfgBtEnYvqRzkvRBcnNi7Yyj72QdrwLdmxBUCbwJi5WUcRth2ErX4d87XnKrbioUBLFFA2CEV16X6w1DZnZQk_H3P-fVZs0teXBrjzCzpMimKfgM7rfUYz9dye35o7KLxBtGK9xHdK96H9xTiJNSRvOuyvKS2LUh1YE4dB6oX6Rky0DOVSOS8Yb1c8pzx3rP3trA1GER1s9mnPkSeTDuTgOk6utb3M9tLB-U1wEvy0Oo9R3Anjcq_W5_1h2oyPPNayeZo33OqKUAhI9si7F6v_pZ0i8CLiRpKdctA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/25276" target="_blank">📅 15:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25275">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbK-bwRdWWlykPv1PC9NYBp8YU0hNcOhfDoLbKeE27KgYHRCVbcsPdPKLIa3kjXrAiUxZBJ86yejPFrw5r7yUBUYvFAehZCn7sGh92hEHsvU3lySgF5_kojIB--7wRgdZG6kvxvrQsHaytZ5X15XvzMLW-GzmvZfzKqTY1zhJ0P53D-hRJz9j6pbXaL-5em5YPc1NYwEVdokxlA1OBekMsIiAxAXECY34iiS0f3ABdzyho9pOIcCTRW7vWiWZgjWZcNbzK4Ylp_cKNWhQeNzSEyfNC4yLQSrJcE6Wb8joGmr7yAgbc3dq5XCG3db7IwsWS1dagxnTxMdQd8sp9wHPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ ایگور سرگیف مهاجم ازبکستانی تیم پرسپولیس‌نیز درگفتگوبارسانه‌های ازبکستانی اعلام کرد که به قراردادش با سرخ‌ها پایبند خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/25275" target="_blank">📅 15:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25274">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M48fgnvBdjidgtLH2TjaRZQYlI5itVPwkji9xa5tnVVEREb0T0Ij_hlRBYZEkf8WoD-C9n6t7jw-tPvx9N5Z7ONpUx8IpbGh3mWmfM4bnZLQFSJlbPDcJBRQ70doOqrLRuY5ULPdN2vbXO2-oPcR3aE5jn0omYpRmkJmQlvVHa_knE6HfvxraGptTHFieyY1eEa1cPKYVnglLz0uoXo4q5ttaSHQz_zGxErPgreLOu6pOJDhq62gVDPoatb3q5ct3P6phOWnWmgsXItMYcIpzT7ygwroJTMWW_eQmUKZ50mRhXf2Z0lGpdEbFHQ6xDl7LeCzdqdiwfMU_D5gcGg87A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
آمار فینیشینگ و ایجاد موقعیت بازیکنان جام جهانی؛
همه چیز خوبه تا زمانی که گوشه راست بالا رونگاه‌نکنید. رامین‌رضاییان هم تو این لیست هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/25274" target="_blank">📅 14:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25273">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmfSUaDa6a1eCp_e4TJU0evMISd4Op2uBl9t21BnhwZA3z60wYKVRWN0ArLECNAYjaDQN7qmCdrLTfsWeivWfdqzGLm1QgRNm1rYKvqi7BDl8s1ekmgW-vMFrCN1rTTcJinjQAQX0NbN2uDTuB5zhALGaTmQA5dSl9m8aCMHSRsyEX2YSL-6JoWF7_s4-wMi6jsjlMX6veSqMazL6tBkjhCYzfKSAlgKPdvb4pjA4q5nte-DUNCebwJL4YjAdnwrSsPKbHHMIGug8NHxULkjExacnNF7JStIgeZKvs0KC5nudSFaw_7ChDSkyyJ7l4uI4lgeBIahS9kLO49pSLiAow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/25273" target="_blank">📅 14:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25272">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAjDERw7wD6QipExwmGnvu8S50eIIz5LM1NbFj2QK2Cefo80IzWanKpPul2-aw_3v8skYEzeJ7ybSsjO4fKD_fdYcxFZ-3Nu_AM3fqR-vOE44MC4mefz5EbGBIyn0oDFHOEPkjIex7OIG7WJ_WACBjOhgCp-hT9MmyypIbMOF70hfVJogEqlCwlul1mk9Vxj7oNzWaiOAYLla64TAuks1KO_WTgPdn_72uhIsjHuIi-h-3Oqmf34h4kVbKP2awZQKWuGYgRNwPRP0vjXn9ZY_6jaC688N1uN5tInyy9RFhEaN1CtU4wAZ9ift6o874RhiJ_d9IjRCv_CJESI26ROPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا؛ علیرضا کوشکی فصل آینده در استقلال خواهد بود. تمام‌توافقات برای تمدید قراردادش‌ انجام‌ شده و بزودی‌راهی ساختمان باشگاه خواهد شد تا قراردادش رو سه ساله تمدید کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25272" target="_blank">📅 13:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25271">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjeIafOZdOI3ceAleeXj1dDyyHWmIIAobo6lJuxdC7kGwRek8bySvtQS3wSUExDGOEmEb-ATIp73iCrOj-xaZUV-YgL0AqJq_qM9_yPmr7ljOdT79IPbKPa9Ek3qHEbJf0d0BUWsuPVhkXDqyL2cCkkavIYZJSEd1LjXXbPoInb5pYfqPHXyQeJrDn5eieZuZ9zlCHeepPzyH5bkAb6sJyTuUehfDssMbOJ64102HcMI-6pTR-4or_KjLk_xYQ717HHzdWDNy8fViEolV6ZJhNQRaYSGAMEQhM1fPNSBMty2FaoAk_BFzIDPFexsRw8Sz43jh9c4qoQgegl4s9VgNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه استقلال باشخص امید نورافکن برای عقد قراردادی 3 ساله به توافق کامل رسیده و هافبک سابق استقلالی‌ ها برای بازگشت به این تیم منتطربازشدن پنجره آبی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25271" target="_blank">📅 13:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25270">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VoAjLDDJYre0AycLK7tMMbhvbjne9RkRHc0Jz4Wf47gGeFzLSWD2qpYxLrwN6_s0WIJ_vXWfb0hTVaVcvmRJK8i-J7UlhG3iyqD48yugluI_33SLcqlq-5Z_gcSCXTVVf-tB7C_kkp-FfMPRv3xUP2LJyVX9PLvueRy6rqafGVP9kZXgsRX1GzVSeKwxlspLMu6METyovKV6j4WOq1G4gh67ZDfqSAQNd6Kj4bgVboy_llr0RC68muByxmyKeCEtEiISxW0Ed2jlDZFqgueVq5Arf3LdkLVNOYnC4exfuy_9ziu3vlcUiV08sRH8A_9ZLw91Mtk_V3MzkDHb9Kn4pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
باشگاه یوونتوس برای عقدقرارداد دو ساله با امیلیانو مارتینز دروازه‌بان تیم ملی آرژانتین به توافق کامل رسید و تنها توافق با آستون ویلا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25270" target="_blank">📅 13:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25269">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrKTp8b37KP7FJ5J2_bjfH5uGAFfJAPzkSCMePU-3COs1AMhK781gZkVM-y3PmoCjn_X1WCf9vXjhbzFI0FuXCtqzbtJEcAAQ5OqEMVb08WypClTNSIv0KxKATo0kgtX9aqXiHbzrpyeJwecL9VhnASO2y818mAc5TklnSF5JP4gNvsZq0PyCR28VYjNybqfRjcNa9LEdNdJlCmqc-2je32GTrHH6cYWnr6fjnsxA9mPDGVJ4wmYUPc5tTu44RFdwPI2qSJltrKWvFSIa-6wuA6fo2Wjs4lonhgkeqRZ-wvVPKrSY9RraHw2fmWZck9BTjdVP8XoZXDl1mrNoTs5Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
کریم آدیمی‌درسال۲۰۲۱: بارسلونا یکی‌از بهترین باشگاه‌های جهان است و برای من مایه افتخار است که‌آن‌ها خواهان جذب من هستند. در خودم میبینم روزی به این باشگاه بزرگ بپیوندم و بدرخشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25269" target="_blank">📅 12:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25268">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUTQPTD6XUAF-WdpVV44qgEcsgrEIEWXExxPd_YDHpri2lVvBc-S0K5ga8UZ7DnsHj2beNQZFuJ8ZmplvW7jvqmvtDw1EqXb_r6e2hYOdCGCEOJStoc0hbTpiohOJ7iH2ImVI3JevgkLZfkT_8KFwnMNBfGvaV5k8XnE46uM4bdBTnT2w5A-KdGs0BoVMgJBI21d2Zjq_VpdE36YgKwhm6Zm2laEWama6zYy9yPr6rMFYlQF6uzMAYXd_qWf7Pjx9m0CLWNJFNk2jKsvs6W32vZJ1yMDkgm9k85bAq_DsflvNGVR2aNhRi2cJk-fRIYQHvyJnhdKynyxrtaeV9ChwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آپدیت‌عملکردکلی لئو مسی فوق‌ستاره آرژانتینی 39 ساله فوتبال جهان در کل دوران حرفه ای خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25268" target="_blank">📅 12:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25267">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30af4fbd6d.mp4?token=MAHVbl1tb825s7bVYlQNWxCbGHVpNdyuMf_Q865ClEI8n4Iqw9zmugIFmCbpQWWz8u7V7SNiDdC1yGTIra6pAFmDpalgs7Dtc1MGcf0i6wNHXKbNwxCWoHj035jfgI4hM9JQh00RvFZVvu7k3qMPjnec__7kc5VMZ090apF13L1oHZKFfJFNhFMQVronJi9LBosBv8eLovg1QVAwrTMYwthN5utVB-slACCK_gbeHRSzKDC5bUQ_r-MX8y5OHgbPU-V6pIEZlPXxc-TdD-p3czAtpEpbkgRmd_HOLKhHkJdYMbAKb1q81pUVNDzAHxyo3AFkSlYA22-K6tMiPMuGQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30af4fbd6d.mp4?token=MAHVbl1tb825s7bVYlQNWxCbGHVpNdyuMf_Q865ClEI8n4Iqw9zmugIFmCbpQWWz8u7V7SNiDdC1yGTIra6pAFmDpalgs7Dtc1MGcf0i6wNHXKbNwxCWoHj035jfgI4hM9JQh00RvFZVvu7k3qMPjnec__7kc5VMZ090apF13L1oHZKFfJFNhFMQVronJi9LBosBv8eLovg1QVAwrTMYwthN5utVB-slACCK_gbeHRSzKDC5bUQ_r-MX8y5OHgbPU-V6pIEZlPXxc-TdD-p3czAtpEpbkgRmd_HOLKhHkJdYMbAKb1q81pUVNDzAHxyo3AFkSlYA22-K6tMiPMuGQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
جواب‌ فوق‌ العاده رونالدو به‌ سوال خبرنگاری که گفته بود میتونی‌ اسپانیا رو ببری: من تموم تلاشم رو بکار میبرم تاوجدانم‌راحت باشه حالا هرچی شد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25267" target="_blank">📅 12:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25266">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Au0rJlWohLOBjcUZWiTwJzjmnKYTmJUmiRHeJfsh9pDJqe9d7ObHcz9XwouIqJWvrbkn4VzQVZJHzYTmugHCRT32degn3PdwjXuQbR6o92jXEvKuKHh5VjgJW-ZQSmFgUcyXfpiPReAL0Q64nEF8kZODiyUWhGEA1PC6oX2En6zR_RX4G-oqlO28USnNwJIcqCpvdkZfFmMYq1Z025ufOL1KiXWyrM_J4Yn9MGVynj2QROBU3shOZJJajGxohCXijJaiyj0qbXIEmhS_aqoDR-Dv8JSSLpw6pRZ4EFcPlUcJxAX7ne5QVwV1hRsCpYr-ijbAhHfYFx_ObEBy6TVCHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛آمادگی پرسپولیسی‌ها برای‌ پرداخت رضایت نامه قربانی ستاره الوحده.
🔴
باشگاه پرسپولیس ساعاتی‌قبل‌باارسال‌نامه ای به باشگاه الوحده امارات اعلام کرده تا 1.5 میلیون دلار حاضر است برای رضایت نامه محمد قربانی پرداخت کند. اماراتی‌ها 2 میلیون دلاربرای…</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25266" target="_blank">📅 11:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25265">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0zsvMYdkgMLUUabWwrqIUXGteTWc_S-Cz1WiqQgMjxfy4WUjy62L0kFdTpeq8bgZGe1A4VmcPJeAfUCd5ULf-dSvoHIAjDRFo0PDfV3KGRV2Nq7ytNkEWd0KRnjVlnMYt1jrNxeW_epIitlrRTqpRrFNZDHiWez5Y4Z6uSD80rgFlc8j4sChPZ0ShhYb46Wd9KqNvk4xEVYsvoySkw-GbKTh8s4wIRges7sZU-DXupg8zg-eJ43nFg368wCS8etIWVqlT_wtRdMOty4uh91QjKbYyyqXNccLvu6iczWTNHR0iLutl58AoAJJeeAEEyAldLaNjWmSn1fWNcnx_Eg-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇳🇴
پدر ارلینگ‌هالند ستاره‌نروژی منچسترسیتی: شاید روزی در آینده نچندان دور هالند رو در تیم رئال ببینیم. ممکن است اتفاقات هیجان انگیزی رخ بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25265" target="_blank">📅 11:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25264">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZ9ewhx3vXd_pkdtZeNicUSO00w5_BtYRypIlTuQF3fBKkB3vcJw524Omelo6immMBiuLeZz4fYe4fF664BMCYEiqfnAxPpxwQR1fQS0h5UiVQl2NZmjYmFPxj0Ei549StSxrykGvqEfAFeyiiYm4jqnDgdqwz6--T7DZEtqrtF3yTMu1fWWQIhJAfGGlY9h5nP-T767VGOHdSvG8UUcnbUM2Jf7R2rB2P4t7f_0D-pkebcdiFCyP4ae9XpmEuS_ILRhcTgyLNkdFbfgSIpabPaIaMTh3usiW0u13LGibfgvjtNINGIosG8trI9dMr1MgR_AlzXigfJUQLuKpi--yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی_پرشیانا #فوری؛ پیغام‌جدید محمد قربانی به پیمان‌حدادی مدیرعامل باشگاه پرسپولیس: پیشنهاد مالی شما رو پذیرفته‌ام، رضایت نامه ام رو بگیرید روز شنبه قراردادم رو امضا خواهد کرد.
‼️
پیشنهادمالی‌پرسپولیس: سه ساله بوده. سال اول 80، سال دوم 110 و سال سوم 150…</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25264" target="_blank">📅 10:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25263">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94e6448be0.mp4?token=LoD4dOf-m5JANaTEvsG-oCLdHONVBWZ5Znk0TeDL1t8HaB_ez1zNRSOLQd-WjZtpV2ygoyyfRsI-y2dXD39IjayX2G7ivecwPIPZ8NUiUT0r68F5JpOc1ph1J8fljZwVlPUoOPiaeiFj0VVH1QHHfdm-8YVCOgP60s8YGlMYp058nfvYbK52kGLU3VVEFHU7blqY-8bzY4Ihz1JO94Dtr81Lz_f1WjhiwMF8s1UeRTGrn2Ga8vdEcXzObW40Xw6IS_mJpMltjI-la0eeRhh9yiApDdPzXSVFMC_YBmGQLrXJCqtZ583DGhB35JPwdCX8nan7f1SFuQIuSfiWP1mKAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94e6448be0.mp4?token=LoD4dOf-m5JANaTEvsG-oCLdHONVBWZ5Znk0TeDL1t8HaB_ez1zNRSOLQd-WjZtpV2ygoyyfRsI-y2dXD39IjayX2G7ivecwPIPZ8NUiUT0r68F5JpOc1ph1J8fljZwVlPUoOPiaeiFj0VVH1QHHfdm-8YVCOgP60s8YGlMYp058nfvYbK52kGLU3VVEFHU7blqY-8bzY4Ihz1JO94Dtr81Lz_f1WjhiwMF8s1UeRTGrn2Ga8vdEcXzObW40Xw6IS_mJpMltjI-la0eeRhh9yiApDdPzXSVFMC_YBmGQLrXJCqtZ583DGhB35JPwdCX8nan7f1SFuQIuSfiWP1mKAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عکس‌خاص‌وعجیب‌وغریب از 18 سالگی جواد خیابانی؛ خیابانی به خداداد میگه تعجب کن ببینم چطوری میشی. زنوزی‌هم به خداداد گفته بعد جام جهانی اول باید یه ماه تو تیمارستان بستریت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25263" target="_blank">📅 10:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25262">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzrawqlgyEg_stcT6Xgr4oCfNL433nJkokqf0ltC5en7W1yBdZpcmEQtHBASHnE6hA5sYrc-iXX4692SrWQsLGaQJyLwZmm-aDPLUeADk4J3yoEnQKP94jPL3pmcAm1h80l7-OCoWhKhq-kZUg5Uzo2kvwxqF7nhAoyb0g_y34qDpwybZDvkFRB3opz5Y8CiR1bNTBMZHLLjuCj5wsHoxw83eQS-IrDSIpv0mm0sbHtIgK3QjiDihRc54rJV6ysQ7rMxxL_0Qp_kUE4uVvVF1arZEDheqKKXWLLKOeHdb-ARs76OMkjxGO7ezDwQa3FM7bwQr2wCkWsWnSO63B5Xng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نوع‌حکومت در ۱۰ کشور برتر و ۱۰ کشور پایین جهان از نظر شادی و کیفیت زندگی؛ منبع: گزارش جهانی شادی ۲۰۲۴ و شاخص کیفیت زندگی ۲۰۲۴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25262" target="_blank">📅 10:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25261">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGtq6tuqP3tkztzMSfC1f7ZXzlvpYaDttLw_gfu6hDmp97B-Jf0dKV28jtIAL_SZysNsoQruw3u3CeFU-sMEJZsBE1-6NEOlIr208bCO4SrO6RQKblnuJVgslJzBUOZSx97dEqqmV9arc4EB4dw6y5pb8rp7sHyRtaxcW_1kbzIt9u8dHVYLLuON6Ie3X3Cq-lr_FvwHkz5QwT0acaP4uRHowUlCY-gCI6ZHJ8W9hiPiG3bMj7YwbmLlegkrQJqGLvpAbzmfESMY4sLlW6XnYGE02fE_06vDHroOaEnJz6Nc-TtqBDYjd7s8I1JtkPspJbtXAB925X_xt3zNsBMZww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیو لو رفته از کلاس‌درس‌محرمانه امیر قلعه نویی برای سرمربیان آلمان، هلند، ژاپن و برزیل در خانه‌اش بعد از حذف این تیم‌ها از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25261" target="_blank">📅 10:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25260">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3YiSJGgC7j27GfvH8rts2lTuNt09YewK3qL7ML2GqNqkaVrOwRU5vzMlux3maJ1tDf6634DAFltmR_-jupWVBaDEQD4kgBzXw0eyNnYW38p7SVXBVSQxbdOG3ITWhpOkbBQKdbSwuoqM3PL-kLYjCSQ963aXO_9p0WXBxU-oxWCtaQdAmEWwO1fb3TpizJcOXgyHcozWQPnpjwnBZ60VsHHsVgmbl5_c1qfYIRPuGi3aKs2mZAWs97B7FdwjJD1D9T_jZzxnSinYZWlwKRWGlm8zwLbu1p0NqLR-P1avRVZ2b0FC9g5mmMv9N7eDZIuDFDbftmAtTkm4w0VWFhajw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
تصویری دیدنی از لئو مسی هنگام زدن کرنر دربازی شب‌گذشته آرژانتین مقابل مصر؛ آلبی سلسته شب گذشته با جادوی اعجوبه آرژانتینی خود سه بر دو از سد یاران محمد صلاح در مصر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25260" target="_blank">📅 10:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25259">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqZQThgapSutlmDyC9_OmvtCqPlwtNwRYM30yynlnx5Zk5ai9yqpy2h33_DGH5NP8iceXP6k0-mLI4l-wXspQGnWyRcbrLZz88RFkRy6isZd0wnl_KmNwFe6o4Qj3PFdnit3wyZX3-3Vfo-hoK_aTqhA2Rc0NL9FO_AJ9n2vTwdRiCjtfehrFVH092dIHaGilvBfkGR6iwc4itpMLZ0F2R45uYTAm5UjLDtSqk_3xCrPmEy3lffS6aNiBvIcyFs9TKzY2b_lYzXg4Q3CGW46sBiEZAuHTOh7rrncEYNP8TbTgOmwKhEece-JyDooCpJbVnhKRsOmtSWjPQlae2pPHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ علی نعمتی مدافع‌ ملی‌پوش سابق باشگاه فولاد برای عقد قراردادی دوساله‌باپرسپولیس خواستار دریافت مبلغ سالانه 75 میلیاردتومان‌‌شده‌است. درصورتی‌که بانک شهر با این رقم موافقت کند به زودی پوستر رونمایی از مدافع جدید سرخ‌ها…</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25259" target="_blank">📅 09:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25258">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRUqyx46r-fVLU7x2x0oBv7_S6jwWyLNyRPLtHk1AQopy6Hx2aKU4P4XRG-4g31v0b4PMfawuamOOQGmw6xCGAgaB4f9OTb7AfbgG0F_xWkWo8bHnvKcquMcYwAFuKQatgWGzHZCrelyySVGi_rp9G7j_hUYUgBJOmv6D7lQkaA-lZ4O8ViazU1hlkji2kNkAXLBCHYCUqEqwv6shwyuKK6qCH1Z7zEVi5_ZcAvgnVEFIwyiko6VdF0Tb2UzwfXSq-_75hcyHmU44RP0GBhUKHM1VJ8TOGVeMt5FIZMEO2bXf-jdbU_WFCgCPoTZdyNCGDtnjXKZr5jS6J0auysVTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/25258" target="_blank">📅 09:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25257">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzMYdUAlNkHl0IE2e_glL0_TzVdVUVQi54nmryDbg8-he2MyOMb2VxezJbG4x9X127vJsTxt1DlKGj1oAZW0DqX6tz0hj0bb8_ve8is3UO38acLVT4AZpNXxzUGrHdI9pC60mT0oSd_j761Mt-c8NKaih_-Co3lZ8Gb7DoEpPh4KIKMt1ZRzyrXz2iiCTdfyoppZ49tKLvG86SN1G5ptyq_5u_mFV00zjnDE-3O0XXuLvn4HwpdEyMlNOZhT8TS1c2SiWDjt11BlVQ4RFK4hJUEN1pTB5TaVulEE8SXx5nIDqfRK0zwNlcMU_9sWcnaZ-phhh8lyKzX6V_xIz5RJNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25257" target="_blank">📅 09:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25256">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaBvaTCIyP7mfMlrzjxG0hhq7_koswkj9c8-ZP5LPuOrXkxovfcdz1Q8ahsuPFiq-wUdoorLsfgsX1y3pl6_SBHEzpNcl2q1nxx6sNTmiLopjbUHmW75yfzNf-xW6r2IJ6KebMYo8nYKzLTZzydf7iXlx4C7odt1dTL3B_muovWXQMakEm-yo2dpTfYKLJeqoJmG2SEn8JqrXlqPhZLAmUephdWcQLrNHIRdOznfDwiLOTUwCN-B7qPrKnDn1h-s3rv5qm83TwYhy4Yh6SEc_k64OyAN3UDI6xn3_j5VBvBAEpsBdlw2Ies8S2ZGG1hucEZvBcz2i2bxaGZU4Xsftg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ باصلاحدید کادرفنی استقلال؛ آرمین سهرابیان دیگر مدافع میانی استقلال در لیست مازاد آبی‌ ها قرار گرفته و بزودی از جمع شاگردان سهراب بختیاری زاده جدا خواهد شد. پیش تر عارف غلامی نیز در لیست خروج استقلالی‌ها قرار گرفته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25256" target="_blank">📅 09:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25255">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8869652ba6.mp4?token=Yfeq_k6vWazoLFOwCgYctfAnNU55_T5bY5WPbQboxsLwBWGBMTuc6v8IQmNDNcLmjlqIpqajC_IePghNrotD4jqGwiXqawLnxI-47sHTXcU2fppoCnmrBVMsSEKzSIcHrfGfpETA5h6QiH7ebnqHrCBAdyuxXt9g1vnOQET1MWDNxk_7PQU0seziTnIxfGo_Bdxn-TBr1yuAfjmd5MzwVEpDerTct9fDOyVOQijV-ku1oe4ay5XI9Akp9uL0TVDuHE6Qo5AyYzyKG3pQGVBEjMLvdAciUY3vasyIhaX0H6IQ_8fC85XJiBlQza3PrMgMKzKMClWI3xlOqbA3-p0s6hu9VUXOumDyoT_dJ8rxL_SIXZyCgyWnCKqaY6XYnzQxWtDitYZfzMTFl6KAyOZKwrMrvH_qQdNZWQRtgRFqm1shR58uEdhRz1UyEkH4l9HDcrzx_j75Oz_gsZ2nyyk3BB_-EkRhso540Buoenn8Qz7MK6ZPjSmXqiugBnw4ItZlHzEldU9FypIS1XTuwJ2VgV4yvmizfFVd15iI9nQlx-SUMyE3goZLEp0SZ4TULAheOVxZHGr-PekLDDNtMVCIqUzt2pP08mhKeQ6qGvFfU_1vCj1kYeC3205curOFcF6mZjl3UWQl0lqDA23oNyedX7rdUhEDke_N7bh1bPZvWuM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8869652ba6.mp4?token=Yfeq_k6vWazoLFOwCgYctfAnNU55_T5bY5WPbQboxsLwBWGBMTuc6v8IQmNDNcLmjlqIpqajC_IePghNrotD4jqGwiXqawLnxI-47sHTXcU2fppoCnmrBVMsSEKzSIcHrfGfpETA5h6QiH7ebnqHrCBAdyuxXt9g1vnOQET1MWDNxk_7PQU0seziTnIxfGo_Bdxn-TBr1yuAfjmd5MzwVEpDerTct9fDOyVOQijV-ku1oe4ay5XI9Akp9uL0TVDuHE6Qo5AyYzyKG3pQGVBEjMLvdAciUY3vasyIhaX0H6IQ_8fC85XJiBlQza3PrMgMKzKMClWI3xlOqbA3-p0s6hu9VUXOumDyoT_dJ8rxL_SIXZyCgyWnCKqaY6XYnzQxWtDitYZfzMTFl6KAyOZKwrMrvH_qQdNZWQRtgRFqm1shR58uEdhRz1UyEkH4l9HDcrzx_j75Oz_gsZ2nyyk3BB_-EkRhso540Buoenn8Qz7MK6ZPjSmXqiugBnw4ItZlHzEldU9FypIS1XTuwJ2VgV4yvmizfFVd15iI9nQlx-SUMyE3goZLEp0SZ4TULAheOVxZHGr-PekLDDNtMVCIqUzt2pP08mhKeQ6qGvFfU_1vCj1kYeC3205curOFcF6mZjl3UWQl0lqDA23oNyedX7rdUhEDke_N7bh1bPZvWuM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
علی رضا فغانی:
دوست داشتم هرجا داری کنم نماینده ایران باشم اماخودشون‌گفتن ما نمیخوایمت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25255" target="_blank">📅 08:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25253">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vi1PqMyLknSGsFKmYh1R1qWidbLyEA3VSQgUSmB6VCXFQPIGZ4lxhI0zbErEgfP9snFbF7i-Wd75_24W5NrhLBuImcf80tiN9oJ7BxlLIey23ljloIGMcuwpn8BAP2xSGL5GbzsrjJpeKjJVQKtJ5Xp7scMuhUdCwYYwvb0Y2ra5f4yMIaFZp0nMJ3hn4DTr3kcRAd1Mj39I_Pw1l2S3XENSYv4G4fBV3zzZbIPp7-04PCJX8voStWRPXiUG737F2Aq8fqxY_1G7ZmsYkNH34ehxYMgGqqWV9LPw4enV5d2eshzTnMZ5qdJq0vfW1ebA6AOzOriZAWdxRIUdFnzpCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امشب؛ آغاز مرحله حساس یک‌ چهارم نهایی بارویارویی‌مجدد فرانسه و مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25253" target="_blank">📅 08:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25252">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQDd2EwYhYFUsSddw-c72ZTDRk91gKhlwAE-CjtfwUi3CizVp6AlvwBpKrcypamiH_dZ-2B6_bkJPz8fX2MT8asdWItfOiHTUp9k56TZ5Lpd8cJ_rO2pBqMwcOo3hOEkBt1DxQR5BvbMa_NLx88pu282j6wNLPJEbKx2fERWa_xugrDKkaiY1MORSMRNQuvgvOZWv3cnjolhI4zOgyy6DZ7fywJzuRAIzhcGUtZ9azXjCU67Z84C0mgt5hYPc8fwV-UgIgJFULV4tT_uKXvkYeeAq2MrWWjWjqNRCllwDMnsma8iQiy0_Rctuf5HB4wsGbzXSrjVvvqxjBQvOBkx8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
جرارد رومرو: ممکنه‌ طی‌ روزهای آینده کریم آدیمی ستاره جوان دورتموند با عقد قراردادی 5 ساله به بارسلونا بپیوندد. مذاکرات مثبتی صورت کرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25252" target="_blank">📅 01:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25251">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkbdqXNjBsEzisANaReWry-PgGSoPTfkAOj0Q5mFyft7-B59JOOVLoE2TaHl0hGgCuHelpa5PCqJzHv_ZYy9qbd0qZlvabawG0L8DJdCCTPQfeKMFNsSpORaftKN95wuEKrBmMqqqWmX7UJaSRk_edOH7vbERDWyn4Jn32RPX9-sS_lu4Rlc1j801X9mj_q_8S-b5WSkzKAVnrv_zoCL7po0m2w5vfr4ksBoKryV67FMNa3gl9K7QhyHzQDmQdg2HlBs9QIezjrp1KboX-wwNFvGlrxD3dgUx25q4GlKXiVUhUl2tKd0-y4La3vw42F_KApS9zM7IddqoVt9raqlZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
نشریه‌بیلد: کریم آدیمی ستاره 23 ساله تیم دورتموند به مدیران این باشگاه اعلام کرده که قصد داره از این تیم جدا بشه. منچستریونایتد و بارسلونا به شدت دنبال این ستاره آلمانی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25251" target="_blank">📅 01:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25250">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6798637471.mp4?token=kX9n1eJ__vzlKgx14YpQmJw1aAR6_qhZ-rAPjUGTseiVly3x3i66mEzPT5yOe4ZJ-56Pnp69X5Edfw7zYWWXHWPHsZ2NNOA6f2Su6gu_-sOxdSko7G3unYzQrG7sOGXO40SCplivQ4_Uy73clVnPExuf12CCk2MDM_pkxhbQKFf_p06Ott_O5nkSL6Wh6WK8-HsjOPkXEJPfHa_SKePc22jPlVQO1hoauvdvZtBGHrchdN1YxoiD_BeiurrJ97IVemij2lVP3PEdGi5ebNbqFiQ7Qa7xW_-sAg0C2RRokfbQ2RmASwIbjBYb0xqMr7UoGGnreYEKEWcBdL_gy5r8DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6798637471.mp4?token=kX9n1eJ__vzlKgx14YpQmJw1aAR6_qhZ-rAPjUGTseiVly3x3i66mEzPT5yOe4ZJ-56Pnp69X5Edfw7zYWWXHWPHsZ2NNOA6f2Su6gu_-sOxdSko7G3unYzQrG7sOGXO40SCplivQ4_Uy73clVnPExuf12CCk2MDM_pkxhbQKFf_p06Ott_O5nkSL6Wh6WK8-HsjOPkXEJPfHa_SKePc22jPlVQO1hoauvdvZtBGHrchdN1YxoiD_BeiurrJ97IVemij2lVP3PEdGi5ebNbqFiQ7Qa7xW_-sAg0C2RRokfbQ2RmASwIbjBYb0xqMr7UoGGnreYEKEWcBdL_gy5r8DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جوادخیابانی‌ تو ویژه‌ برنامه‌امشب جمله معروف
"گشتم نبود نگرد نیست رو گفت" خداداد هنگ کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25250" target="_blank">📅 01:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25249">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v13KqYdg8chraH4XaMXO-mi3sJmZ_OXuBwI-OEX4mBiYEswrPvzQcbOCgH3RWbNW1boT0nQR2fRwNjtoOUPZIIm29QDbLP0zs8mRBnJAP1mY4xwGpEyuxYRK7_BwPl8liBNyb7xgvyt7durz6COqiCgSwcsUWTSXciHAUEoCSGsTmmZvE2a53RKgTvXf8JnfVppztHbBvs89t2JtxTCQvX7L_FLwF4MZ111dl9xcAL9cumKts4IZVzZtncFM4gzQ5GwggV0yR2Xohi4kz8hBVJ0JNCVVgsYpHJPAgoq3UNPcAByzT_wcBgX0OQuzWJwfgB-pUliwEy9oQpkzQkjIDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
خوزه‌فلیکس‌دیاز:باشگاه‌منچستریونایتد برای‌ جذب‌اورلین شوامنی هافبک26 ساله تیم ملی فرانسه به باشگاه‌رئال‌مادرید نامه زد. کهکشانی‌ها برای فروش شوامنی ملی پوش 100 میلیون یورو میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25249" target="_blank">📅 01:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25248">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMsWs74hGqBf_j0lrzIxY5YL0JYrXTmDgL1xtAv-MKA0S1t5Utv2rTZPtW1cTFAbJ4Ie-aHQXACsVeoIQ4Tazru_O_opAQu2q572hZ6SYXiYJz1b2r2y5-pvJrq1FL8YBhtGgxXIdCvE03OXOSfKhVBj-LRnFY5en1NEU7RFMJ3z-_iK06oYPfixBzPr_ogffXRJfHW0u-HNWdsgc5q7nCYeHMj6JdB7ibF5fGcolpyksfzQjg7qRjXkIRY_Uauy8rgqCgGQrNoQJiITNn5alEfGCT0hYQO1u0N8eSSZgya3ccHOTSByZUKriSUkMOY1c46jAT56JeAP_4kZAsrntg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امشب؛
آغاز مرحله حساس یک‌ چهارم نهایی بارویارویی‌مجدد فرانسه و مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25248" target="_blank">📅 00:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25247">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfHb4Sbh3wF4KkJLWmMnBm-ckFCRnIRtGp5naXt3FEQYxAih8EWCNGewntRtemaYqU_LFnGJ0opwFwYdP3wBPsg3NOUESyMffSKW2ynGOF9CbzyDzKSUL5ZFvG92lHv-88yqIupzjRz6BFp4XEa27KpSXvrQrgIYYc__vX16X-wohHAZFrA_igiwaVomkgWOYHspHlVH7l3bMeQPEXYB8P_3WHteHoLLqglsGPrdoXSqhZGcfcKv3t-71DFYamj3dagaARqT_5zYh2uBB3v5XAhMuNP8jZlMUZGXpXZzzK14ZAspOaeJmokj4I9P0_8ylWwr_iQJTClAmAcxdUeuMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عکس‌هایی‌که از وضعيت امشب بوشهر داره دست به دست میشه: یکی به این ترامپ احمق بگه هنوزجام‌جهانی‌تموم‌نشده دهنت سرویس.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25247" target="_blank">📅 00:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25246">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmx236cgc02DieRlv-LoS44dBUzIQY8y75wo3tQJf8_TmxhxnkDYyLaXZ6vDB_scyEb1CMzctnG0t0hZGShvmGQT-aBVUhcCISqmrHwsAqp1pSEHcTvWd-AkOvCadzAQY8OvpHtidf_Waja2yQ6AKAjtg1Mit83Yi_I4JB8fG3HWDn3kcBUeuC89UW6uhldRHowZlvxcg7nKwFzLYKrfD6NmrlERg4sFm0L6W8GTE3eB78AYdRy_HvLboQ-P9lz8-CQR1vAigyutkDe5MfcluOK_Frbaf-Wtk3G6nvG8fmaOmaO4vLn9KfRkX562NCH1EHGC5n69UR2N4PSK0tMugg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه دهوک عراق بعداز جذب سینا اسدبیگی؛ حالا محمدرضا سلیمانی مهاجم فصل گذشته فولاد خوزستان هم با قراردادی دو ساله جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25246" target="_blank">📅 00:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25245">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfIqce67GNl8d81htt23c84D8xFpW0eQFcEKlAxkQ3VEpXdSluz8cceHaa6PnWNCjK255ehCXaDeqyUc5GM-0X2mdeZELRLMQdC3qPcjPBKZrjt9YKWOWrycQ_olYIzvHHfJT15eOnBLaLdo5kaZMDoQwl5c44rZjnh_g96-1-3eX64JEI9LDmxF7Aw6YONZCRbB1A8JQ_wrFPz1xSD3Noqfaeyh2oPT678ILQcsxnNz4K2KhueQVlCE2lRIzFq6pcHisx3IYwvDNzAMXLwEYAhW2QLRcvJZKFcgz9l9mE-G83NV5GZUyvYqLA5Na6MDcE1D_6W0y0gakLYh7AY-5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25245" target="_blank">📅 23:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25244">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHaRFcsu96n6rgFDA7ljbk3wep5dzoL-vLCtckf5vCjxZj33dBJsfZe6s_XeF7OmcJjAhfb9Bg-IambUAQAmPFaZisJU30qaGh8Kex202YgVQGYYnYgkm0khgXogGMPSSiWiCdT4wyvTsxJCeGtqBc0cV-h7d7mRF-MUFJf990xdqApmwyqHMFRZEV8g2VHS3vXzyzFZZ5iUtePxlHaa47g0_c06SuUy0TD6ow34ukFZ2DpH1euAOCLUT9KAU4_22PhbaL8f1MsB9JDfkFNzleLihDLVhBBrBBeMrac_w4Nb_9lDGdInRbcmEFv8eX9PbGeqexSIN8TRlkdcxyUj2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25244" target="_blank">📅 23:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25243">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFEI2gKlpSBtqysOHJDznbHQg-4G1OKENDSP3KDgWx8PUWhU90ftkHozEZAYw5fTm-S3VpeYbESEiqfKl-oA5DwOhHUIzNt2nx1cDin9bQx5faDA1vOmgBa_7kiF7aD1FLWIdhd8K00YOQ3WAvpq5h7J3A_y2AwJFIS6YNesLyQsJBZ49cPsL9QOOOwe30QVr447Jj1fGbHXQmnSs0AYr1zOYAWSz4bXNTzVFAjSxAZBGKFvnUwz6j1K8Br8RAVzeeRROHcqZ9cQ_OCEil58G_StIqA03pLCN7_3FzP_KprM1t70rhghiG9RpGQDgdLMitwNhvjo0cLkB1sbo4966w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
تصویری دیدنی از لئو مسی هنگام زدن کرنر دربازی شب‌گذشته آرژانتین مقابل مصر؛ آلبی سلسته شب گذشته با جادوی اعجوبه آرژانتینی خود سه بر دو از سد یاران محمد صلاح در مصر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25243" target="_blank">📅 22:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25241">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T9eYwMj0SaIG1FQPPojZyB6r0Knj3G6Z73M0p4Ah3TSvcEsA1I7sciSXSBpCTtXW0_B5CPWryI455Ek1TSTSIYUeYuKn7BX1qZfKImAxNvUXD3t0w6lYEVFUYLNJPR7YKVtiHQ5lDubqzy8RNGhHt4NnbFk-PKrwtNt0ls5kOgas-cZEoSTf-7drDllDdsj0q7JFZVOEJgfzsENJjrTz8KuIXNSyxv-p3Y0-GfN8xHrj8Xxcc68-APRsjZmB9BjctbRcokewwW8QXaLfp3Tf1zbTUt2mF5tkwZfYspd3rAbkg1isHPln1HvcE3yQZjFXCPPCpnbz1ctgf8TcJMtYtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FOpdvyGMX4iR5doqKe6cXzl9opKi1I5gNVKlc68vl_OalHBIjecgarh96D8ZD3TbCE5k7IOx1IDFd-MlCFj8ps_6gzO25Dadmv3Zz5OMR6s46a6YlPiVBQzXVi2MW5xmTzoLFeJFu8EG-7cB-v61ZXG-ty4A5funADxTU0ruo1--DD3-f1YjFjzEGcYi20o6REty4TwjwLzPiCTyOTCuhPbhRP895ruSfTbEGRJojxubsrB23t7-6Ot-C2ZYdbURbiEjnzZu3JnV54oqHA4cylRf7YTgxUl0aRdk4WzmcEcSfSNRLoG8zuFJaku1FPu12FVEfMat5fhWLv1TnaMrcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🤩
مجری شبکه رسمی باشگاه رئال مادرید که مدعیه‌کار انتقال انزو فرناندز به این‌تیم تموم شده و بلافاصله بعدازاتمام‌جام‌جهانی2026 انزو کهکشانی میشود. گفته با انزو در ارتباطه و انزو گفته به زودی به رئال مادرید خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25241" target="_blank">📅 22:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25240">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d23ff97317.mp4?token=Fj9THE7CyyhfTTcrNLWTL3j7sjaCEzs8tc_xvyl4iTokIJfMtluSaOA6lYtgkUuAXCHH0mi_ZZe628Y7EJTFLBzY9ALa7RV9IbPxFO12O1fBD0zCk0BygYihpWR1Q_pprJQDq_cXo3tpzhIwSu_UgbwV_7-xdcur6626may9wxiphjQPMhYauRd7Kz4hMCeyOuYRPTxCD_tDvxnJGyt6g9mJ4qS_QOO_gnRD-y-ZGJAR67p0H9aZVPciyvlBBn3yDk_usNpHcN8Tp-wUPssB8H_QYDp9QOQd-FexUl1zyuy-egw-AjWYTNXpYfcIjdYF_6-3wInkmolGjzSp5fcYAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d23ff97317.mp4?token=Fj9THE7CyyhfTTcrNLWTL3j7sjaCEzs8tc_xvyl4iTokIJfMtluSaOA6lYtgkUuAXCHH0mi_ZZe628Y7EJTFLBzY9ALa7RV9IbPxFO12O1fBD0zCk0BygYihpWR1Q_pprJQDq_cXo3tpzhIwSu_UgbwV_7-xdcur6626may9wxiphjQPMhYauRd7Kz4hMCeyOuYRPTxCD_tDvxnJGyt6g9mJ4qS_QOO_gnRD-y-ZGJAR67p0H9aZVPciyvlBBn3yDk_usNpHcN8Tp-wUPssB8H_QYDp9QOQd-FexUl1zyuy-egw-AjWYTNXpYfcIjdYF_6-3wInkmolGjzSp5fcYAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
امیر قلعه نویی سرمربی تیم ایران: کاش قدرتی داشتم که بعداز گل شجاع زمان رو متوقف میکردم تا شادی واسه همیشه رو صورت مردم ایران بمونه. باور کنید این تیم شایسته به مرحله حذفی صعود بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25240" target="_blank">📅 22:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25239">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-b-pKA_hsG6zZM20Z9Kg8JyHNIPsbkL5pz6mt4H1_r2stzOnptGyv6H2RBzTVbtw7FccZMuhKdaZQsOWlrgGu_dx0j1etzY6sWOnNP9dSBaENvyo-kFttF02Zl8qx8eEjUYpBCdfbo2Gy3W6GT3iF6KwK8FvF9O9Hd4FcVofeNHwGSvcHC_xVZ08NaTLao8oHqMJSV5YTzgQXdG-ut0NS8oxEAcgk8Zqy4jAgoiTmvj3zQIQCpLUJtzToeh3ASxtCIASyBu_k1Tz3t4CDW7OLDonRJAGH9AI94eCIqdGfxIYRO-USpP34F6lTUK1SUj3t-maN4M5i5Mquo9JNAL-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25239" target="_blank">📅 22:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25237">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFTijEnEi0pC3apHFGbO6LplMinpi3aYt46wWunY5AuSVLNvaR6-U_nxuoHGgzJkML7w01JO_lXSZpjeVL3jWXVZOuTKAL53UiOCFqIEzvUmhJJdSbS1RGnmKPztPyjOTjbnmaYxNhQ-qGviDcTsWx8gWp270j0co_ZIBjlNC_n_ElpKZya22DcPsn3UPCkRF9FhyU11Zp73AHaN-IWDIBFE6hhVrJo8aYb1erFJfRJZcvxfTFB7mSwtBBFzW_NSYYQSH-IUeDEs-lmO3KOeQyGzLTndIGZeK7uvA2vmXamq1rjAYtVLwpi1e03mWhCSRNV2MhjTa5air70-1mQEkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ورزشکارانیکه درحمایت‌از مردم از تیم ملی کناره‌ گیری کردند: یخچالی‌بسکتبال، محمد امینی بسکتبال، زهرا علی زاده فوتبال، موسی اسماعیل‌پور فیتنس و محمدرضا اورعی هندبال؛ بزودی شاهد خداحافظی جندین ستاره تیم ملی فوتبال نیز خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25237" target="_blank">📅 21:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25236">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RP-Dcz4LDCl8_DtFloaczD1bEDTzLhUMm7G0y8OucDi4hvCSpn7W-8vAxEbLQ_elTjmMqc8vdx1rWZq77DQqesUiuQJmU4PnGzCPKVQm81Y2_VRhO-Z04NGN4I580LZiDqt0McPXXLhxrnca6R1H4YWGJtVQYY_yk3JPdqGRYSXdx-2bKYM3hBQa5xQY7y1yITTZTLuWonq_ivZ-VgkSZweecYmColG_2PBdCih3FeWacayhWwTs2J026MBKyvmgexNEh7PLLl5WIMj1_sngCJAyjs9fU5Yjlj94f-YMgntwEyDtUphxpuzInr3tQ2GB15T7o3YglQ5seKkc9_pM1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🟡
بااعلام مدیریت باشگاه سپاهان؛ گابریل پین دستیار ایتالیایی محرم نویدکیو از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25236" target="_blank">📅 21:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25235">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_0lVzkl0XvVlUE5lDkuD6YhrQv12rnQDC6Oz5m-RoeCPxw6B5q97GL4EC7HxDXfXPB-ZhKRGJg_r7poJPET1yjE1mA4xgsBiVzWSlWocjJoVoZZDsbKRwE40kMRpgTb_2ifUzanR3IpxOHvJLflt7sCcDUCVjEGi3CpI2sBSn_0s4sBBgNb9lRRU_CIyS7GNqCLvtuSdCcCuAomuGg7vQpuZ6dVqqTumJQIrIcB3zNw80vjwvL0jmvjV3JVOrh6iCP2o32urM1I4GhJmxmSKHgGUgYKt5VwZ7yOULLb9dN-NehriHjJNfoE0BUD5t8c7H8mTX1Rm0uRf3g0Fyin5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌پرشیانا؛ مدیریت پرسپولیس پیش از انتخاب مهدی تارتار بعنوان سرمربی خود؛ با ایجنت هادی‌حبیبی‌نژاد مذاکرات‌مثبتی داشت و حالا درصورتیکه‌تارتار تاییدکنه هادی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25235" target="_blank">📅 21:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25234">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvWzeB9CbGyLHnT2sKts5EQhuTNvh3abPMEj0MGDnRVf4ae0siEE92Dq9-Foc0oeHn_OsbBheAvSqKQya3_HDGdBDuJvmPV5id1Np40zkazUQDted4AckNJWXSy7fQ7jEDvutcGsE0WJwnrCOgKlXFrKWSnzEFHR4Iqn_uwRb1JQY_budzGo4rEfVnSiaIZbKEQEyyQsOPTztAcWQtyOkylFN4TVS33oO7JGreGgc-3brvRSh8PhSKmE8_sdQ9RknerbT1vM7zZf1mR0H3XtQXi4p9eLexq1A4CHubV5aa1tLePOdYvxgtN66M-ZLvl3nWIUg32YjnakgXZC3JUPKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امیر قلعه نویی سرمربی تیم ایران:
کاش قدرتی داشتم که بعداز گل شجاع زمان رو متوقف میکردم تا شادی واسه همیشه رو صورت مردم ایران بمونه. باور کنید این تیم شایسته به مرحله حذفی صعود بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25234" target="_blank">📅 21:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25233">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hlame8-sHjj_zEdn9lSGBFH8_hBH_JTI7_qprCpWlkO5SPkc45bPztNZqXZ3O2rxhPLSbNZZkptoHZX4cJItw5etN3m5cNkW1GCoD--hD6o6pw_1Ukh1imUANscvM6nfS3wKfX66lpEuVZQqE-C8PYxpw39S3awFGBHU3LwfBct3S3DaaPnIbaSBH5Cdwih3togtAcjvwRN_mBN2bvqn9ST60eItra5HAMfIKRg_-KjhlYyWr_wceb4Onz90S8Y7YzrQMRX8JQMuVF6tgbOoePpcq7kzSxYqMq9pymEGzzQGiKcwbHD4vFOBvXSRZ_RGS-MneFzCo8y9ZJy61raZCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
غلامرضا ثابت ایمانی هافبک‌میانی‌سابق ملوان با عقد قراردادی سه ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25233" target="_blank">📅 20:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25232">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgDOU2R5Qx5-hOJzrc-s_AvspAVe-CTTzSpWeanMDChv-QSYLUvCiZQI4UUI4Udqw-rriYPolFBRKhJvMkzDXgIt625zbh2muUjjtdvKiRI2tNikFtyRymDWHbO25IlzZzKoHVWDWcYV6rq1bKag-Wk7DlH_D3GipdD00fFjZMAWob0EEhfNj0If0P_jWNoMxyKOcEuAQHou6fQ7HK7ufuHU5nQsOZxwjUsKSjYN4JylkYZ6buTaY1Ju_0-Jlv6Bqpd-1sPlILETWOX1Cfv0ArTr9RBUvLZ0lplHzIFMLQNmiqIm4TkezunROGSxM3qkMeiEV_7G5gGABe0rDzlyrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کنایه‌مربی‌مصربه‌مسی‌ولیگMLS؛ابراهیم حسن: فیفا میخواهد مسی توپ طلا را ببرد، در حالی که او درلیگی بازی میکندکه‌فقط 3 نفر آن را تماشا میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25232" target="_blank">📅 20:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25231">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXXajHbjZ-t6-moVDsliVTUqLcmO2NCsNXsb0ELcn5fiACbE0fiziV9Al8focZogqB7PQEbEPBv-yvRmTOApNvYSqrwXzOjTl6Ssk6FphYdpF9hUIJrq1g45JNkfpj1CqdB3YEjSaLw8vLl9RJuz0hLR7s1Fcaq3Jk-KfHx0fxssqI0Zl8C0V3pp0ZIs953QPHyYuAWeQh5rpH9pcHnfW8fraumkEmARFAv_G7kkpQo0d_Oxa57-OFRdl3wDsS7LiOFYQ4L773mXjg4zQK3NLvkT92CuV6PaBTzGAuornV3-f5Dx0mjOKRyaOC8JQn9_kEGsnpZh5_FisXBfcPBRYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
یکی‌اینطوری هم‌تیمیاش خوشحالن براش و بهس احترام میزارند. یکی‌بعدبازی از تیم رقیب میاد دلداری‌بده‌بهش. خلاصه که یارخوب تمام ماجراست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25231" target="_blank">📅 20:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25230">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2AZ1pWV0k7nK-8B43HFJl5WeLAAHISqKxAIaAboeUrwH4ss01UO4WkeusuET3KPnIYx4tnBBYoB54MqI7Fuk-uV6eMSEOaiqiKyTLtJExNa0jM_GxC21AIwbWovoRNuw7X8AFtMNVWdbfDSc1CjOjUpnTzQ8Hy7_BYGRpldTH5aRLyLwfhHoF0I2iz4VytfwXyiCTzUFdsPdheQk4PmJgtlfs62DoNVSZaAHq3YbMWpc3hIeVxk1V6aBqZh0CPE_oczDk9U81kurAyfySb81dIRSJFCNzbQYRKRgWhsI_T_VtHzCSqO5IYAlnH5lFOpTP64FzlArqf13WNH9mHVBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/25230" target="_blank">📅 19:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25229">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSKvMuqrm65nlDRhoz5FPlgXbymevOiJMOoFvceVgo6DyaDZTY80rT97HBjGB2JC3BKfs_fGefhFSMpdYV41LpT9A3zV7K7uwLXGGsunUSyfyYs20N4TjmGVFL-q4aQUcb55okEEy_YSbYKeUI_Wihu6ErdpF-r-OtDs6zShobOOwtHzSRotJ5WKDNEzEy9YmmMAJa4TCnE-vdsGJfwpxVgA_BTvyifeLU8JiPuZfD0-lW11oGjz3tl67CLEIuwSOJI4JLvTYea5l7pS4UQARDYg_ujHGq_sF7aUF-qgsqXHtAvMqtRq9Urepk5k9Z9DflPw206MzFoQsvvNIIldcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا
#فوری
؛
مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/25229" target="_blank">📅 19:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25228">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7acbde92f2.mp4?token=TAq82aYOqL2XhXm4BU0cMw-fyeVCUJNd4hIrHBcIKI7oVTFvNk5JcBHs9hjr6P8YMvBqZftiw4OFJGr3Cbs_Ht4xD5_lkh3g2Eb7cx7BQWNlRcblt3L786ycoeoPWQ5ocj12RzRl6yHU4DJofkqXoNv3ek0yR0dKHKf_mP8vtVZ5f-2rYI3tAoOZX7jfQGbhTgmVE4e6jYkfwmMHbnI3anv77SAQDnMNJU-575yOFByP6XGHBeAeiZXHurzfHYLajTO74Z8oBJgCk9bnJEunh0TUWcVFQOl4Hc9hKSgCXJ62CdRsE1x6sFQx2Qmv0drjDfB6g1Z__cWkltlG0-6jRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7acbde92f2.mp4?token=TAq82aYOqL2XhXm4BU0cMw-fyeVCUJNd4hIrHBcIKI7oVTFvNk5JcBHs9hjr6P8YMvBqZftiw4OFJGr3Cbs_Ht4xD5_lkh3g2Eb7cx7BQWNlRcblt3L786ycoeoPWQ5ocj12RzRl6yHU4DJofkqXoNv3ek0yR0dKHKf_mP8vtVZ5f-2rYI3tAoOZX7jfQGbhTgmVE4e6jYkfwmMHbnI3anv77SAQDnMNJU-575yOFByP6XGHBeAeiZXHurzfHYLajTO74Z8oBJgCk9bnJEunh0TUWcVFQOl4Hc9hKSgCXJ62CdRsE1x6sFQx2Qmv0drjDfB6g1Z__cWkltlG0-6jRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
👤
طبق پیگیری‌های پرشیانا از ایجنت منیر الحدادی؛ خبری‌که رسانه‌های‌آفریقایی مبنی بر توافق اوبا یک‌تیم‌مراکشی منتشر کردند کذب محض است. این بازیکن اواسط هفته آینده به تهران برمیگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/25228" target="_blank">📅 18:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25227">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9aAPHgCn7TeLOyC6lzlVfJx4B_Ov90IxUux5GmD0Ytqef_NV1hIziymrO3xHyWWNZ4a5txpcLmFGWkZhhiAtSwv1vx3CeMN6Z6pXrQjkX71k19VEb8OKQh06X1iVBjuTH4KfQ4zONduZiTzZBybFlZCLtIzGwN_4ygVndTgkWlaahaQosvzfwBrcgbtuqlR_MmIZ3vla_JvYMO5eHmoeW0j6bwe_DsP8-WPG3e5u2LNmBsczyUakrhsJuyUaPZ6yfI-S5RK4u9a0RZiVqSxDZx5vaecnZjt8O2oFuj1Ixwch684oP7MOg2klHP7EUXT6iylIlMTaKFK2JRZZ5AhKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
تو این عکس لیونل مسی با نصفه بالایی صورتش داره گریه میکنه بانصفه‌پایینی داره میخنده، آلپاچینو نسخه عمودی‌این‌عکسوداره؛ لیونل مسی بعد از بازی: من گریه کردم، چون احساس کردم که هم تیمی‌هامو بخاطر پنالتی که خراب کردم ناامید کردم. اما خداوند برام سوپرایز داشت.…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25227" target="_blank">📅 18:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25226">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qv5ykGB_eur-1Ph2262ho77J_ie3Dzy76rJ50Sa5dAUTNtsK3b5dLXJHt0mwoXOD8OsTgZFyxFQa6zKj6DbI-_IodZn1CeoqjPQKVjzBFn96UQbe-1d5o_MmqNeuWYwpLSHmYz7baomeTcPNNQj0goe15EZddFk3Oof5gLMkO6rQSTy8dC72unA1vRug3jcEEnxHSbc8ZxGL3SpyDO8xybzTK63FUoyz3wKF0zRnk2VVabX0ipm4IBEnCw-joRpquWi8ObuM7zgw6mzjRKnhHhxKzKlkclCMvDGhx7gl8iw-1JGE6M_hSQJQeG7jaaJCd_lZ5r894ahVhtJjNYb3Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بمب اصلی پرسپولیس که امروز رسانه‌ها تازه دارند روش مانور میدهند سه روز پیش به عنوان اولین رسانه ازش‌ رونمایی‌ کردیم؛ بله مهدی ترابی بدنبال‌بازگشت‌به‌پرسپولیسه و صحبت‌هایی با مهدی تارتار سرمربی‌ سرخپوشان نیز انجام‌ داده. تارتار بعدِ اومدن به پرسپولیس‌بلافاصله‌نامه‌جذب…</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/25226" target="_blank">📅 17:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25224">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLZR6daj2CWN4pg44FU7qu7ocpaQn_D2vEhsldc5fkyKyVMXAPWvFw_7c8DCxlZ2HXt2AsSJq2_vIJZbCuUcBDHvfejb6C7vhnUNabWg3ZNDMVRXAEK9ten9yADNTf0ArlsommVmaCbFx9qbG0XCQggTWibA2fz_vHBqikz5q3bFTcKAPdrHfQaeUNcf35GMrJyPimF8WZfa-4ZV41UNZuEqJZfaT8ExlsQp_WSHJjdPinuCr8XERltc2tdCdVYoypzV6x3U5pP-i1tM03vFLvDZRTs2mxktfu6d-RZohVHYNypgSKsvBqWgLdHmhbh8PCRs24EuSH9-UuU89M4zbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
در‌اقدامی‌عجیب‌ازسوی‌فدراسیون‌فوتبال؛ درحالی که روز گذشته چادر ملو با برتری مقابل گل گهر جواز حضور در سطح دوم آسیا رو بدست آورد اما مدیران فدراسیون پیش‌تر نام گل گهر سیرجان رد بعنوان نماینده ایران در سطح دو آسیا معرفی کرده اند.
‼️
همون موقع‌ای که AFC خودش…</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/25224" target="_blank">📅 17:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25223">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfEcwmdV0CFTB_n7ZRrjhlvmo3jsD8bvWgXz2iHe1XP57S7VVFoP_xHnI77cCFob198jUMBJ3cu3ZpPT2bxz2JferDgGXkKTTlqizBHkD1LsDlqeAeV26TMwraR3xi5mCwaWSh9V2qBY6GTXKpeo79TV2zv_-CiT7eQBhu8WbF25PsbfnwsnCk1qgkc9YPfk3h_b0NVk4y4nDweYd381wMF01pFdRoYLF9_xgzDutcNnGYcpUcSHfIWoYTtgqlvjhnYOl8cPguj58dHUJ3PJJ-P_9fSvH2NGkl1Fa6NHn971s9SsLoSMH2x3Q_vTwca4noHTr6_Yl4rCQhhzh8sqMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی در صدر موثرترین بازیکنان هجومی مرحله ⅛ نهایی جام جهانی 2026 + توصیفات زیبای عباس قانع درباره لئو مسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/persiana_Soccer/25223" target="_blank">📅 17:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25222">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/th-oie8t2B2u_VDw84tBkKheNoTlHsHgBPJQX0SDCH_9q0PtKU1DaQs4sxjvPd29elAFRsdY0zOlkrX-yDa2TlukpDpmVEPQynQIpfia0GYR1otsjjBiAHoQLzjXbGANrt7TCq7effO97Sq1iZ8vfCotC7TY5EDBZ4Gn27Aaf4PchEOLVOe6nCGKR0VpxqytogYGj8G88lrhH-K8XZ2xPMCe0GHB2jlAzK9LPx5KdmuCCoCAvcua-57ylQxARumFjk5uSblr7eHuq5nr654_-d87BUgqtoRTJAFe9cSSbOasp12QIsmMhmrea8VGy_J7f4iaOKsNviusTbDfNGztCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی پرسپولیس ساعتی‌قبل‌خواستارجذب مهدی ترابی و برگردون این بازیکن به پرسپولیس شده و از مدیریت باشگاه خواسته  با تراکتوری‌ها مذاکره کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/persiana_Soccer/25222" target="_blank">📅 17:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25221">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpL2mx5hqzpqCqDPQRjap3DqXxYoMCQNYQjJ_9-11zb7Ce-qMFUrppnpUTFpx49LFpB8Vp2XGv3mnExZBVwXkk3ur_etIxqy6fHfDsNWg3vntpTINU5TCpJdGYsv8ziPWKitmUPAeHL9wa_uczantRl6Hnrlvf1bpnpwK0tS-mQ--WR0s6v_x7lwDCiykca6sq6mkYIjOMNMIHRAxRlSNJWRw5rf7B6gbjyqkpVzImKu_4Vjmtko1jIlRabB6Rq5HxuXIwESZJJyKD5zTyHhxcqEQ3l8u2ZyXBlofG0nH5XIzVNfunyEjvyTvx4AD69NVemMZnN_DbwpyvWssVh5Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/25221" target="_blank">📅 16:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25220">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCyxH89rS8P0_9mISntMGxdmhnxi7jfDtz7xnr8btt6GQXao7OGiXYLKrqFl7Pe9FTYfdcXiuTln9EiWZafmC4y9OfVt0T3fUgCNd-cTVAONGJPFp8uIXpglq3q4Vs_9sZFrcIrGzE4QXBAYYpuJTSOdn4B57vefLwN9WVKYVnh0Z5LO5or08u4o5GQ80w6Jhh7yOW3wC7Z73jznXX4R5mesAyFxxJqsf5-MY9Trl7C89np43GRMBCKbRTeJFYEValUbIecuQDtEum3HDaeVr6UtG7dbl5-1JPYykOimeMTwosNlCG3z07lXiMAUBv-7YRpNr1UdHT-LB7lVujB0FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر…</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/25220" target="_blank">📅 16:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25219">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqNm5UrBvVRI_bYue692B8CF3J3L5OG1nMpjL981R0zJXr7uh3gbCi25sRsmwwQgKWfWSL7UWKEieZTjTzT7oFMYL-zVpQd6RcuX7ZX_pH6ED4iH1PahpOI5vE7xJjZ9DM4ltOQP-h0lp7uinX1B_ikp5M1ME1GxtE5kwaWPWz5slVivMe9DSy1AWWPjpzdQSWHi6ER-b4Jk_OMMK6d7o2w6sj-3c2WI8uWVY6ZmUT05xWDm25UWkL8Rzz8kiuccQkDk9gihPi9KUZrgF1Fq00N_2gO7TcmTO4OyuQw25wxJp3twV1eh8dwFpobpMslCGUalk1Vx6qRdlpJ8BKF7Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
👤
#اختصاصی_پرشیانا #فوری؛ طبق جدیدترین‌اخباردریافتی‌رسانه پرشیانا ساکر؛ محمد قربانی ستاره23ساله‌الوحده امارات ازطریق نزدیکان خود درباشگاه پرسپولیس اعلام‌کرده درصورتیکه این باشگاه بتواند بر سر رقم رضایت نامه با اماراتی‌ها به توافق برسد حاضر است به این تیم…</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/25219" target="_blank">📅 16:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25218">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f158271b54.mp4?token=aekbU0VdEUrtTNvLj8YVO4WGbIlAHRnIr2yEXNqM6lspLCrTBx-ihihc_r6TCbikJEEqAYcTB_R92jhW7JF8pIliLrTaA5xpz32_lFruDMWMLWoLkeQCLktRlglAFRAvj3S4ppIMgo9xsJW80q-Nw6E-TicFYYVjFuYZ48_SXUbtIhDjF7q7w0tZaDwHL2x_uI4DvUtmimvMr2a6_iA21fVwDm3plOiNMargGk3KvcxB0BSrs9rUbPrlvD0_zKVKY2oFyGwCpJCKIt-KhRU7XpbPEaNGIaWMgHsq6bim4xA938QpRggcx25cahkJ_IO3QLZbcOSrFf7M8BSRMd4j3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f158271b54.mp4?token=aekbU0VdEUrtTNvLj8YVO4WGbIlAHRnIr2yEXNqM6lspLCrTBx-ihihc_r6TCbikJEEqAYcTB_R92jhW7JF8pIliLrTaA5xpz32_lFruDMWMLWoLkeQCLktRlglAFRAvj3S4ppIMgo9xsJW80q-Nw6E-TicFYYVjFuYZ48_SXUbtIhDjF7q7w0tZaDwHL2x_uI4DvUtmimvMr2a6_iA21fVwDm3plOiNMargGk3KvcxB0BSrs9rUbPrlvD0_zKVKY2oFyGwCpJCKIt-KhRU7XpbPEaNGIaWMgHsq6bim4xA938QpRggcx25cahkJ_IO3QLZbcOSrFf7M8BSRMd4j3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعجب‌مهران‌مدیری‌ازدرآمدفغانی؛
علیرضا فغانی سال ۹۹ وقتی‌ایران‌ بود: به من برای قضاوت هر بازی ۶۵۰ هزار میدادن که ۵۰ تومن هم مالیات می‌گرفتن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/persiana_Soccer/25218" target="_blank">📅 16:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25217">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fe_nQpdDaZGYRUfRe15yYPiu6MMaz1i0XP9zEHqqqPsW8CJWVE-WNG7lOGMiAFDTNYi1rvwCD2ZhYY0Df4ZTRB-wAeZQjgYea23qaNOVVwDO2KKdPUZSdEKnFdy5CRw6fXgtI3FgLum30oFmdvJkKLpOF3TG4ScWlLN5iUVcoQJ6J4-5yz1EHp45-z5qff7s1XXA40klm9kNN4BFihCTctloD7MXCzKLkWu63049mzACuJKCb7WrgCOtNwnwHFOwZ1U-zKaV9TEs-41RzmpFdYfA6fkLqyUAPRWhG-Hlju8IS07JB51UJDJjag0ZGJaOeJLl-HJXgVkUAXD6pvLRmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌آخرین‌اخباردریافتی پرشیانا؛ علی رقم پیشنهاد خوبی که از لیگ برتر لهستان برای علیرضا کوشکی ستاره استقلالی‌ها اومده این بازیکن بعد از مشورت بااعضای خانواده‌اش به باشگاه اعلام کرده به توافقش با آبی‌ها متعهده و بزودی با حضور درساختمان باشگاه قراردادش…</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/persiana_Soccer/25217" target="_blank">📅 16:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25216">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMcg8UnebSf82hdoypk77qSsWoNVxzj93munzmwIcyPinMxyYGCfZH9vhEgOkijO5pVkeSw9n2ZQmg94rJH4kJcCJpQusH0e2D4bkRHwQoJie66Ugs7vEAbrv1vPM_lgP4LVPPwElal2su3dkrZrklDiAktTt_23bedVP6RORctSYOaoiUFvJduqNKLzi0a3ZIQvuJRru6MVMTzOpyrB6BfJnYxsqU0WqCpiFXiQkR2P3w5hU1EcSK8-x6AccIGzgRH8VTgPqEauYqjN4Ii2KSaHlI8p8_yrumFhbqTgpud3mJvA3gAIHCrVbGs0019FFToKbKNQiGRYqTryUV9F1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی #اختصاصی_پرشیانا؛پرسپولیسی‌ها به محمد قربانی پیشنهادی سه ساله با رقم‌فوق‌العاده بالا داده اند تا این بازیکن رو به هر شکلی‌ که شده در این پنجره جذب کند: سال‌اول80میلیارد تومان، سال دوم 110 میلیارد تومان، سال سوم 150 میلیارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/persiana_Soccer/25216" target="_blank">📅 16:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25215">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcdA82QqRbM_YMTF8hZsxDnThT2hZvmh3Y9xddVHnA6nb_qrc9EviMk2Y9dEdFjKTfzs68XxShR0440IMnEjmgnt4_z4DZaydo1OPwSELk3iGwz-pjYSfZmbeMPI_XZDT9SNOLFa351Py44l5yvT9x8Ad9XKWboaEpF2x--KLCZ-J7hTIDNwFUTfacl6qnATMH9gj7qVkjpkIJQEhrK0jFrihWoabvxGRsv-8C_dZyn3MKdHGKy8oxyAOS5C1AVWt4R3sjLZ8oK88bcADfSNmc0bf_wC7Kc1TAa7PLal5SVS7BYjeod6S07-BpcQCqRT3L8o5Yt4GhtEiXteVTorhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ آرمان اکوان باانتشار این پست در اینستاگرام باهواداران‌گلگهر خداحافظی کرد و رسما ازاین تیم‌جداشد. همانطورکه‌گفتیم اکوان از سپاهان پرسپولیس و فولاد پیشنهاد دریافت کرده و ظرف 48 ساعت آینده از تیم جدید خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/persiana_Soccer/25215" target="_blank">📅 15:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25214">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWF6qTelxdqMqEcYkS13S5V8N0rWvsFsh3bjTFGkIp5GuPyJURvhjttWYVlrgUTe0KbAkLw-nswh5lGPHU1jTE4Xo6J0d8ZHUB6I88osW4FbWt0fYXVgyQhQ6MfR9nPvWBKsKzsdgUpMFC83-2eq9HXjQdQ8-TC-QwN2D7yjELVwmgiQl3U_SqwD7pC4urNC47lsgQY5uGJ-4x5kluzBxBsWlkCXiqsPB4FhGa2EdwE-rvJVs7talzYsKmtjDrto2Z9VK1tIbcDTiAh5y44lDTdmFo-FeNZg73RQOUIflFwXu28YCpskcELfvIGEl87jKctw6BGKGZpVOdHr13LtjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/persiana_Soccer/25214" target="_blank">📅 15:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25213">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e22c0f699.mp4?token=Spla3hJVa5857NBK37JosMTvb7JPsHYNkjeiNT_yTQzfeuRz3wgfw6Y_-kxkVhPuHmPrTHxigrZEnR-CLGFtU0atL5VGg1Ig9qYl-Ik5XO8RkoueBC0ks4wKiqFNoew1m6UyFLKlPIXsGZMSF43vQxWSZ4T2TmVI6oTnjT71jGtnK5Bdk9UvKm5Rb-_FELOpNX01eDTDdO3Ic49CRtUlWIJirJdFBD6tEY-Ejh5jcoa3IiaTnE5BdncEecIibouajwBDlWURC5AiSNbaIREOldRQdHSzIhkEP05_TUhSlDTv8hv9nbdtPqPkc4eeznAk1lq6u6kgnLRWg3VM6VBFcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e22c0f699.mp4?token=Spla3hJVa5857NBK37JosMTvb7JPsHYNkjeiNT_yTQzfeuRz3wgfw6Y_-kxkVhPuHmPrTHxigrZEnR-CLGFtU0atL5VGg1Ig9qYl-Ik5XO8RkoueBC0ks4wKiqFNoew1m6UyFLKlPIXsGZMSF43vQxWSZ4T2TmVI6oTnjT71jGtnK5Bdk9UvKm5Rb-_FELOpNX01eDTDdO3Ic49CRtUlWIJirJdFBD6tEY-Ejh5jcoa3IiaTnE5BdncEecIibouajwBDlWURC5AiSNbaIREOldRQdHSzIhkEP05_TUhSlDTv8hv9nbdtPqPkc4eeznAk1lq6u6kgnLRWg3VM6VBFcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#اختصاصی_پرشیانا #فوری؛آرمان‌اکوان مدافع میانی گل‌گهر سیرجان علاوه برسپاهان از پرسپولیس نیز پیشنهاد رسمی دریافت کرده است. مهدی تارتار از مدیریت پرسپولیس خواسته‌اگه‌باعلی نعمتی سر مبلغ به توافق نرسیدند با ارمان اکوان قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/25213" target="_blank">📅 15:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25212">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwZykcbVEhdsRjcsnD6jbrsvze9ydMlH7dfpC7E6bi0dFQJ057CNhdzCHYCy3GLwthh9xOFEbzndK8t_2XJ3ETiCUFeFeT9XtEb36fNYhlBR98ZkfokklaxRo7699c2JVtDQfDtU6Qa1UG5Rj4Qo3dKEnQxnsaGM2n4r3vV6mrtr6p0kAVzpr8kn9NURdOchCvACd_40RNneKzTgdQoWQpJBd1_8jdw3oYJPfz4KT9SibTR9rLCG0JpKhjw93096yi4Kd36KEq1tAaJLcXGpAIQpMkN6DcGFkNqgTfqEpQu91wEM8JQKe3HdWeC821YQJzJWfYV5SE4evFxggZLswQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
«
وزینا»همبازی مسی میشود؟
براساس گزارش روزنامه مارکا، باشگاه اینترمیامی قصد دارد ووزینا دروازه‌ بان 40 ساله تیم ملی کیپ ورد را به خدمت بگیرد. او پس از پایان قراردادش با تیم چاوس در لیگ دسته دوم پرتغال بازیکن آزاد شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25212" target="_blank">📅 15:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25211">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUmKM84LZtCxVJJwr1Lc8Ttlqhi2xxgsYJlPDZ3I7Xxl7hA_eijar6IU5lbNbfW-IfHICUEkZqpWaPjtVnUwb4bFHuQxRr86_Rs00ynIEVQqYJXlXBMWwu4lXsvtfpLgE0l-KUr4hfIjFs5BGEj465KHChpEn_xFLnUx08KJ2RXOMWjctjbkTF7Uo4hcFiDmD0c26ahY1tpcVSAErLonwt_sHhs73cn1PuaIUbK7jV-L7OzLGFEMbFqjzF9BVr77s28pUz8W69i9BfGTqb7UPsREju8P4DAezZw3-wexXs_PMTWZbWnvorZfV5J42xrGNW7hGXBiuXfVQ4GGGWK_Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون فوتبال کرواسی رسما جدایی زلاتکو دالیچ از سمت‌سرمربیگری‌این‌تیم رااعلام کرد. دالیچ سال 97 دریکقدمی‌پیوستن به استقلال قرار داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25211" target="_blank">📅 14:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25210">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrZ-tfSf_mOyNnJh3meVhXHBDeboY9oVFXRcHdsVbNAiLjjqVh9pw8x_yfgPBLMy7KcpRYbnv4RmUMYwr-Zflcm4VQ1VmUvYNJLd2g8KfB2GKAQO7I89X_HuRdubTjhjXvZnGHS2O0ht3W0sRhsYchPO4FDLQABvSGOr-HK0bRY9C_OSJ8JgQ3a1-FcJiXvsXy_oNaPxSRbAbjZxbrD6A9i9nTtoz_ORpCFbriIw7Ng7vaf1tlvFpkPoH2gUM1X0jelb2YohZrHn3O3a0NKYlLvLMxFh7p4d-vxio7K1JQvx3O5H8zwRgkYX9VPI6dM_wFOrhs34fqVlxfN2Zuw2mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ابوالفضل‌ جلالی بعداز امضای قرارداد خود با تیم پرسپولیس ساختمان این باشگاه رو ترک کرد؛ یه عده میگفتن تازه الان میخواد بره داخل ساختمان باشگاه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25210" target="_blank">📅 14:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25208">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baD1CedZHGI5JR36a-opSuc9qXcWGOO0XV03k4r3kokBQQR2sKBoZ1YcBRuBnFVb6suOZt_K794eV4DEHtUsjUbpZlxVXvs9IPUO0J81m1NUOzMDHDS8yPHAhQaJ5u6BkJOpTJwKha_n0flboEqMJQPcqXvyvT-NcJGP80M9Y5qhthZlvTVvhehWnlzjP74hiTEa0iEov_-fqS5JYLI3HKgEckLEXRg7RM3HBp53aE7Yr20yDoZhnZLWtegmfkHwoQniN9-aelEzkmVA0fUxibQpqcJQ5CnrU9qrVEVvSfjXVbBCkrniPM3eG5YBklUao-SOo-7m-A_0C0ViM6mZWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbd67803a1.mp4?token=cdqGJit7wmIhGfuQuEiid1_l-9QIOeSqDK6lBWutcoZLqszIOPSYMevKKecZWsu8XL_aQ3tPYI9Y9lgqF5Kv2avI-g578QRw9IJCASJcg2NggGZsold7hQlD1GiKFfigPkTdtySgU_HyeFivnTPVFS5fgXOBYRpz9tVkEX9HQa2bbspcTq2JOYRon34v_0yI4s2_82Y_1Fd-dcm5ztKXAobYKWmeZez9rCiz0A9my0dxf6a2YifD3915qEM0ih6BUozpEMwRlwqmHn9a1_rDNUdEJaI-RgCzsgnolcFfbjHeqrcRKHLTiNEsaPa9MFGQ2ERZKMiHceL-juJ3oHjOVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbd67803a1.mp4?token=cdqGJit7wmIhGfuQuEiid1_l-9QIOeSqDK6lBWutcoZLqszIOPSYMevKKecZWsu8XL_aQ3tPYI9Y9lgqF5Kv2avI-g578QRw9IJCASJcg2NggGZsold7hQlD1GiKFfigPkTdtySgU_HyeFivnTPVFS5fgXOBYRpz9tVkEX9HQa2bbspcTq2JOYRon34v_0yI4s2_82Y_1Fd-dcm5ztKXAobYKWmeZez9rCiz0A9my0dxf6a2YifD3915qEM0ih6BUozpEMwRlwqmHn9a1_rDNUdEJaI-RgCzsgnolcFfbjHeqrcRKHLTiNEsaPa9MFGQ2ERZKMiHceL-juJ3oHjOVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
اسکالونی‌قهرمانِ‌جهان‌شد، شادی نکرد، وقتی قهرمانِ کوپاآمریکاشد خوشحالی نکرد وقتی قهرمانِ دومین‌کوپاآمریکا شد خوشحالی نکرد، وقتی بهترین مربیِ سال شد خوشحالی نکرد، ولی وقتی مسی گلِ دوم رو به مصر زد روح از تنش کامل جدا شد. الحق که تمام لذت و هیجان فوتبال تو…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25208" target="_blank">📅 14:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25206">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e403b418.mp4?token=Mc3_cQImvuciSv_2aVcxNhFK02YtsHOn1Bx6X5OoGVWvYkkwQaNh_YksM9B5elzyfWHr_VLB3uM92Lx8fIxuLiRc2xNuqr2J5iQg-cb98lkvGs-Uka5iusBn148W6MCw4kmDRLwxOg8xTDwnvxeDcAjqvHHZHkGyg6wAFIrSWcjBxSEeGR8y8O4h1eg15jkoICFn9P6V6HlsCmQsVwmoS92ayj4r3Z8LDM_a6OrOS3g5Ox2jCaI4-BYyhlBfK8FVTEB6V7ZP3D6UyNeBMZPeZTBTumo_szGj6816RoacHt4ne_ThsW63EMF7aMQ-XxJcwLV-uNGn0JNBZM6fBrl2IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e403b418.mp4?token=Mc3_cQImvuciSv_2aVcxNhFK02YtsHOn1Bx6X5OoGVWvYkkwQaNh_YksM9B5elzyfWHr_VLB3uM92Lx8fIxuLiRc2xNuqr2J5iQg-cb98lkvGs-Uka5iusBn148W6MCw4kmDRLwxOg8xTDwnvxeDcAjqvHHZHkGyg6wAFIrSWcjBxSEeGR8y8O4h1eg15jkoICFn9P6V6HlsCmQsVwmoS92ayj4r3Z8LDM_a6OrOS3g5Ox2jCaI4-BYyhlBfK8FVTEB6V7ZP3D6UyNeBMZPeZTBTumo_szGj6816RoacHt4ne_ThsW63EMF7aMQ-XxJcwLV-uNGn0JNBZM6fBrl2IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#فوری؛ابوالفضل‌جلالی مدافع‌سابق استقلال برای عقدقرارداد با باشگاه پرسپولیس وارد ساختمان این باشگاه شد. قرارداد 2+1 ساله توافق شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25206" target="_blank">📅 14:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25205">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbhTgCP1LezE9wMmDjG-mPbw4bmvLP4CVnfaoN7S6AmmloOVhBLY-utyVrPUnqWhTZG-IPJTrlPHo7-Vl94cFBGSsTP6VyVT5U4GcsyRNbiSW7V7iRSu4acG1933oMUhEmfly9najvGo15O5VTh1PHtoqLzLssFWcM8GRpl6jcd_QpRLfjVM1XZu5r8o6H0hOdCeUywajOmcPy8EdyILVmj08FYLuTdzficiw6VnQR5hzQGQtm1-SzfqrK255WdtPBmiabpKXDYxxAYDI0vjBpuUNMPyhpGBVM0VM5x_xVvvPgZiCAJeoPn292M9WXd7QLt_LQP_W4zuQVRh-OZeUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25205" target="_blank">📅 13:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25204">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZjHkhunrPfQSeXJtd0wVczKwbW_jLZ00p6-Z-CPc2wk_vc1biFkei3Q2Vbp3e6FUFjLrG3yphRxDZW0NhLz3HrRRbd4y4WZXe4Z4ejxcxj7iOTUIfDo-rUFBitT-bc42JReifEonKatuMPqOxVt64-fHRpKk3Xc0frwU6YDLVX417HP9dkJntnXAdbaY6ETfb0SGKzZDIpN4DYDHydy8P1kpIfFInitr1UVorquWoSY3r32lgdKt8h3n_qyzsEmPo08H7Xol45SMfmNfQ8OGbx11gjBu8SSs4G50n5MJuXVTjTunjJolePPkBnwhD6wgUhDoQU8bq_uWIH5WDdk6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25204" target="_blank">📅 13:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25203">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8123ef735.mp4?token=Wh3c3lOIz4CX_OCBMelF6HTgZbb2i3Cy4TA16v6pWZM9Phnb2Cc1Io1ab4_nJQhdD4OVrVlTtWPZCiV-CjHlpACMmeXWjRO_SFxhTWW0Q9Qr7yLQVrbPloiKFDq21tpnFHzQ0YDeztVKBgTSUIsacyUQSXMRUX81iv6rbPjGjT9rz9J_xWeHYDFA1KU8WuhpnWFR07kplQlJGwwNtUNRFAFTJwLI3RcBxJx88qAhIGSWQK8KHNAL3D-KoLH1DYJrPjDtrw_4bZLTgFOk_5LzrNIN4bQoJmmT-Uf2AHnOZUQ_Q5l48xVJsG5XiRuJDLvKI76xB1repK0809tgAyZi6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8123ef735.mp4?token=Wh3c3lOIz4CX_OCBMelF6HTgZbb2i3Cy4TA16v6pWZM9Phnb2Cc1Io1ab4_nJQhdD4OVrVlTtWPZCiV-CjHlpACMmeXWjRO_SFxhTWW0Q9Qr7yLQVrbPloiKFDq21tpnFHzQ0YDeztVKBgTSUIsacyUQSXMRUX81iv6rbPjGjT9rz9J_xWeHYDFA1KU8WuhpnWFR07kplQlJGwwNtUNRFAFTJwLI3RcBxJx88qAhIGSWQK8KHNAL3D-KoLH1DYJrPjDtrw_4bZLTgFOk_5LzrNIN4bQoJmmT-Uf2AHnOZUQ_Q5l48xVJsG5XiRuJDLvKI76xB1repK0809tgAyZi6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
اسکالونی‌قهرمانِ‌جهان‌شد، شادی نکرد، وقتی قهرمانِ کوپاآمریکاشد خوشحالی نکرد وقتی قهرمانِ دومین‌کوپاآمریکا شد خوشحالی نکرد، وقتی بهترین مربیِ سال شد خوشحالی نکرد، ولی وقتی مسی گلِ دوم رو به مصر زد روح از تنش کامل جدا شد. الحق که تمام لذت و هیجان فوتبال تو ساق پاهای مسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25203" target="_blank">📅 13:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25202">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/867fd1f608.mp4?token=fAUp5hQL-EcRNmwcOkZwtasm8otTiZ-ccWXLtuVSqXTlaB9dlvIHhKJqlKJl1To4mBqvZpyAwfYN59TOS3AwUsKjAr3uffAM1MdJMIGU04Vi4QtnDx8YftnxMHn85g5JFgY2_zWbDtxJK8qYQ3hPgxngygbFdCo4it8yW0OL_7SbEgKc-EJhozsfLyrqXw3HbWdX8oMGBzE8ho4pe8G2iWX-CFdUf86_w86CO07qqsaVkmUuu0c9w8BIhCu17umqS9BzCclMxxEhgnhu5GjFpdXn9oabRrQBGUsBs4gDZ5UlE4VGXcyVKArer4DdVy0BUwkeu5IyoNEohYcdPmvy4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/867fd1f608.mp4?token=fAUp5hQL-EcRNmwcOkZwtasm8otTiZ-ccWXLtuVSqXTlaB9dlvIHhKJqlKJl1To4mBqvZpyAwfYN59TOS3AwUsKjAr3uffAM1MdJMIGU04Vi4QtnDx8YftnxMHn85g5JFgY2_zWbDtxJK8qYQ3hPgxngygbFdCo4it8yW0OL_7SbEgKc-EJhozsfLyrqXw3HbWdX8oMGBzE8ho4pe8G2iWX-CFdUf86_w86CO07qqsaVkmUuu0c9w8BIhCu17umqS9BzCclMxxEhgnhu5GjFpdXn9oabRrQBGUsBs4gDZ5UlE4VGXcyVKArer4DdVy0BUwkeu5IyoNEohYcdPmvy4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇬
محمد صلاح فوق ستاره 34 ساله مصر در پایان دیدار با آرژانتین از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/25202" target="_blank">📅 13:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25201">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMdig6QmfuDKKQbpFCqZlNi23NKN12CQBviYpUSIH1L-5nepw8WqgG8g1YeFa89xihzkk70yxBjU7il_N7Ln6PjzUREpRIIy7_kfGfwRKZ6nMUKX_73ueOhBkZHC3njPkSKUyseYHUuynyrs9O4iP4ruHwGdGHFqXlDcWS3TlNEXOOqJFhMgbi0uqw0kxLBpIFz6SSC_r87addZyqjJh1e4ZlYJyf93u4o1pfdoGcOK9NXQBpMFrg1fmmjuiM6vtljJQIy8qr63OtP3Dssw4Q6OSjk_WZLrzQD-52Eo7L2Yyon2PtZi8_d0nQ4zBaRg9OmeZxT-Fa4C2eC73FJ_Zfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
فدراسیون فوتبال برزیل ساعاتی پیش قرار داد کارلو آنجلوتی سرمریی ایتالیایی و کهنه کار خود را تا پایان جام جهانی 2030 رسما تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25201" target="_blank">📅 13:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25200">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADNQiOVEAGiZtQLWaW4mVwZxrQtmSapvhqrfhdeSxxJt-4EQZHDDvDWN-tW-OnnYBWjHiUfVMC82idNy28rMWPjvRLiMvTfY9c1ORCn5qrG9plABd8FLmLJzCZg6tYLoo_NzAHzyiax411BSDZs99EiXjZ5ZoEMXaYPkiJG7rRhAu6k28eSl0Da2T19G_5SHDxZS-iX0akhChpWjC6Wr5HY7SmOGzmmQQ79q41td89fev5im_EHv7Xtaf1yqW5wfLCF4_dWFf3F50CWly18QIKR4_F663jV-CYZSd44pD3VhyYPokDyCc0sJsDdLpWtd51kXtpht9UCrvFUy93WNSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25200" target="_blank">📅 12:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25199">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBNmgzgqXe_yu_vMkMYp2I-fNtc69u6uTEYdw8s3B3MCPlWE_JGXs1C9jhekJLVCu6JLX4hUtLSQpu2n_OhM7bKsJrljJFBWoZ6Hs_J3QV4xlrKcvMoEqxjVn3Sk6_kcKQlx19yky770hCvpY-Eupe24ataJbOcnI4qFsIjMHkGLeEFKxvGdFnbZYKaRLn59cjhPdxkGl--ebxpuxuBcGWHy0AIp2-GRUryS01Zo2oRywopc2KXshCuvRyGYCujhKge8CNZOX9wLjt4V0zWKxG4wwJdM2wfRzbJH-Fe2i-oAslxIf0nbUFNZM5NKjGk__Zscqc7PWJ6PpgwC_uVo5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛سیدابوالفضل‌جلالی شب گذشته به صالح حردانی گفته‌بود وقتی‌باشگاه هیچ تماسی برای تمدید قرار داد من نگرفته و کادر فنی هم هیچ تمایلی برای موندن من در استقلال نداره باشگاه پرسپولیس بشدت تمایل به جذب من دارند و فردا ظهرم قرارداد 2+1 ساله‌ام رو با این باشگاه…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25199" target="_blank">📅 12:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25197">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32700e30e8.mp4?token=HPgUU5aqvpVwisJot-XD9R3Vjp0CM2a-HvdJI8gIa0DHg0OONOWVVC-cuKh4O0s8PgB1iIgLvplmDIt10Wo3a6IZ-U7qUtB-B3NV7wUGzL0haBkiuwB5LjgBDwU3mkm3erKYC7l5dIm2I0TlKdI9Gc2YVpSOCMfRULGVuzkHPREhnUIRhycdgEoHpGWhPhEIlFsNk0Jr1YoQykulC-fuw2BPBEiKL1aUerrA7HHAEuiC1gGojyLe3EVKQ-cFAvAePDctKdn8rf27zAqbvAy9RqSAzPJYU-KUscAsyFyfxZIDQLLM7akew_2OoEfkEwcNH7cUnvFvOXVAJIui1TnaUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32700e30e8.mp4?token=HPgUU5aqvpVwisJot-XD9R3Vjp0CM2a-HvdJI8gIa0DHg0OONOWVVC-cuKh4O0s8PgB1iIgLvplmDIt10Wo3a6IZ-U7qUtB-B3NV7wUGzL0haBkiuwB5LjgBDwU3mkm3erKYC7l5dIm2I0TlKdI9Gc2YVpSOCMfRULGVuzkHPREhnUIRhycdgEoHpGWhPhEIlFsNk0Jr1YoQykulC-fuw2BPBEiKL1aUerrA7HHAEuiC1gGojyLe3EVKQ-cFAvAePDctKdn8rf27zAqbvAy9RqSAzPJYU-KUscAsyFyfxZIDQLLM7akew_2OoEfkEwcNH7cUnvFvOXVAJIui1TnaUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇦🇷
یکی‌اینطوری هم‌تیمیاش خوشحالن براش و بهس احترام میزارند. یکی‌بعدبازی از تیم رقیب میاد دلداری‌بده‌بهش. خلاصه که یارخوب تمام ماجراست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25197" target="_blank">📅 12:28 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

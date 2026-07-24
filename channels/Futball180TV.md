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
<img src="https://cdn5.telesco.pe/file/oCRfMHctDv52afti7MeH-h-_cA5m1j7NwspSUXMNMLQHQNSGkUCnqtozIL96feFaNMHLkUjV3vtRkwoiG_8aVaO3nWjHSxeGYPQEfjXaNu6wyK5FgncfrifKt_lWrIAeKyJufjuGv13meGpcxED2491AgyrReStQjt9OZuP1CwJN7XKEUSHe9HTaKnv-zMzkf07atj89DgXUoOn627D7vDAle6Jme-wGCe2XOxi2Iq2rXY8EInYSyOan2lZ54Ex9XfC7Wy8EQMBv9zfNdO28hpNz4wxk9azZa_59zuiCFud_zkzEWDt0oxQgGe9Npxj6PSt73zQ7WYzDMH_2wBGAzw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 534K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 18:50:40</div>
<hr>

<div class="tg-post" id="msg-101795">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrDyMCxWa_MXZ32hykJ3kGDrLWXHGOUeIZlhXbQki0rrBXTixQbgq9IEtlr_lfUN9iYg3KAJaXnmnMh-fpvjISR2QUSULRv6f0dSbcHF33gUgZgIbz-iDhcFLR6DH7i1aMm5P_jWEXNNIIOBa454Z2Tq7fHqPaJl11ULO-V6vGRaakt7KeTSMTHuo6kTC1jHc3Oihibw58WHcKtOHEYlejBnFewcTwpCSo77tEL9wMRJG0YsKTu1Sdhystl1r1vtCnv6ZzBFnoCUxFnz91A5SIXh-Xo50itJY9Rql88SmtC9xu6lncI4-Uf8tfhSkFuUc5v9imiiOF_gLdnIzqT0jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
⚽️
بیشترین دستمزد هفتگی در سیتیزن‌ها.
💰
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/Futball180TV/101795" target="_blank">📅 18:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101794">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1da4d2bb8.mp4?token=pOq796Rh80xnJeArCobaPZhNobOP7uZpOKANCReScw2_J47PqoeDPjen8TPPT_DnbB2H-1KO5P1epbbNuk5f9WUTsZV7vneapyiuIAVIIsUTGuPDuMrNYLH5oj1R3DMF1vsPXgo9fDLnrmXJNxWOpA8AkXyEoqjk7CJK-V_XaGxNTxWy1hc-Ot6KeBvrCR_cZxeOIoKl8Hy4kw8jIP9oqMo9-a1m2W06XJo7SLeVwUVClcCaLM0daeLLRF6n2u2O0mqZ3LV9ORNIb0gu-L5-j9RPzGj7qmgQPTXX2g9BRKCZ3H3_RmQRMTbk9P8pP338dvS2P9iJ4u4lm-FafLeyc2g5ULSZ_xvSJ3WGvJThB4eUPchVlR8LK9PEakV74iaHRntQVFB6AM6A3pjDXbuOQ66ONMtb5hfRN6oJSPOlXrXIITaS2iEKLAN2o5aDrtyTBvjetghk6FL44q45U0otP4bvoaqPHlutrUgPv-UnlLJFBaBQr_QiGbgZksAlj9kqVCAsSSovN7cDR4aKqZeVHnDNULq5SY8XD6yoRs9cgsfTHL96toe_022CRN7F1SJUjSbTI2rXkZ6BJ-ho1Ip1-rVX0fTXcRG2u-byoBQMm1VYfdMNK5yFKWMAbvwjDzulFh7NAnIHu_hNndcQ_SAqRYrEV0kTk0QFnKjjETQbtNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1da4d2bb8.mp4?token=pOq796Rh80xnJeArCobaPZhNobOP7uZpOKANCReScw2_J47PqoeDPjen8TPPT_DnbB2H-1KO5P1epbbNuk5f9WUTsZV7vneapyiuIAVIIsUTGuPDuMrNYLH5oj1R3DMF1vsPXgo9fDLnrmXJNxWOpA8AkXyEoqjk7CJK-V_XaGxNTxWy1hc-Ot6KeBvrCR_cZxeOIoKl8Hy4kw8jIP9oqMo9-a1m2W06XJo7SLeVwUVClcCaLM0daeLLRF6n2u2O0mqZ3LV9ORNIb0gu-L5-j9RPzGj7qmgQPTXX2g9BRKCZ3H3_RmQRMTbk9P8pP338dvS2P9iJ4u4lm-FafLeyc2g5ULSZ_xvSJ3WGvJThB4eUPchVlR8LK9PEakV74iaHRntQVFB6AM6A3pjDXbuOQ66ONMtb5hfRN6oJSPOlXrXIITaS2iEKLAN2o5aDrtyTBvjetghk6FL44q45U0otP4bvoaqPHlutrUgPv-UnlLJFBaBQr_QiGbgZksAlj9kqVCAsSSovN7cDR4aKqZeVHnDNULq5SY8XD6yoRs9cgsfTHL96toe_022CRN7F1SJUjSbTI2rXkZ6BJ-ho1Ip1-rVX0fTXcRG2u-byoBQMm1VYfdMNK5yFKWMAbvwjDzulFh7NAnIHu_hNndcQ_SAqRYrEV0kTk0QFnKjjETQbtNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
▶️
اشرف‌حکیمی و امباپه در کنسرت بد‌بانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/101794" target="_blank">📅 18:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101793">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b632e2b27.mp4?token=l4vh2cTPdYkcSNqoRql7WBLFiJ9PVr4UA7CnglN5IxzxRxvAkEGwSQ_Fooq7fbWvoJxoLUwcC4OCrgUdgTMqgEXxrxWJ9ES-9AV4tOuOvZoIgGrSOnPw3HvMCcjHz78Uykc3GJryM3IRCyt6YTGAuyisNwkTauaZG_Gv-hvM2u3UpqtgbSBmy_bnz0p3s88AJnoh7bxleBB2iDOplOSgyH-G59PUlU-fjZ1I9ER2pYEgP6cON3MPCa4u3oCtMaKKPYpKEjhHlWdq3uCq_plMNUoZPMG5Mk97XknHkgn9VQPA-0ApO2wi19kBZOULnLmnZervfrWSt0HGawHEvbOJyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b632e2b27.mp4?token=l4vh2cTPdYkcSNqoRql7WBLFiJ9PVr4UA7CnglN5IxzxRxvAkEGwSQ_Fooq7fbWvoJxoLUwcC4OCrgUdgTMqgEXxrxWJ9ES-9AV4tOuOvZoIgGrSOnPw3HvMCcjHz78Uykc3GJryM3IRCyt6YTGAuyisNwkTauaZG_Gv-hvM2u3UpqtgbSBmy_bnz0p3s88AJnoh7bxleBB2iDOplOSgyH-G59PUlU-fjZ1I9ER2pYEgP6cON3MPCa4u3oCtMaKKPYpKEjhHlWdq3uCq_plMNUoZPMG5Mk97XknHkgn9VQPA-0ApO2wi19kBZOULnLmnZervfrWSt0HGawHEvbOJyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسی همه چیش بهترینه، حتی میم‌ شدنش.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/Futball180TV/101793" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101792">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e74ccace70.mp4?token=d4EVW9-I23FNzzx5qKU2lA7-gBnvkbKtArYroSytc5ouHntWB7EA6wvf6BeYnGzrPoRSU6YRtppAHXX0ROEiR5VhE07pA626Y35rEMuY0PPb8cDoY7RzxqCVLpPVpiLTVukf6zkq6qGy1OtkQ9tANoz3Qtg_vPFpXKaSTpwCpicA_xHCtF9K0LrkCdAsM7B11Ei8j4D-QzHUAJAVHrgXq25t-_5jqAL9UXaFb69Xue85yOmg33Bt_rUHzGVmzPzzgyWjYq7K20IACkNSP0NTJ6fg6rt1qV3BroRPCSPYXIXKarkSe39ILnvUjlA1LZosAIayY2dY9pNhkJCfOEB1JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e74ccace70.mp4?token=d4EVW9-I23FNzzx5qKU2lA7-gBnvkbKtArYroSytc5ouHntWB7EA6wvf6BeYnGzrPoRSU6YRtppAHXX0ROEiR5VhE07pA626Y35rEMuY0PPb8cDoY7RzxqCVLpPVpiLTVukf6zkq6qGy1OtkQ9tANoz3Qtg_vPFpXKaSTpwCpicA_xHCtF9K0LrkCdAsM7B11Ei8j4D-QzHUAJAVHrgXq25t-_5jqAL9UXaFb69Xue85yOmg33Bt_rUHzGVmzPzzgyWjYq7K20IACkNSP0NTJ6fg6rt1qV3BroRPCSPYXIXKarkSe39ILnvUjlA1LZosAIayY2dY9pNhkJCfOEB1JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🇮🇷
عباس‌عراقچی وزیر خارجه پزشکیان: توافق با آمریکا بهترین توافق ممکن بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/Futball180TV/101792" target="_blank">📅 18:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101791">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYT-e6E-u-MQjy5jlesN6aYjZUy7UV7dLQpMyZfNtlAiikbDHp1BDBrnt4WT8pD2SjnCK3Ezxtg3T0iB2S48B6gZ8PjuSV2Z9yRz7curEit_doV1m_FWcUZoAorl_B6A86fjyO6VzcuYshyVj1tuy2-XST8_xPwDjU1qFG3U6KEdakusTuD24iFwRJ5sCR0gth06buRh3WOkxjA1aiboyWbDebDijPWp5dcbru8lHjtqlas87rOldCwYxBPwhcAAIvr5k3AytPy8U_L4h8uXE7-9u2nHMupPXJS-EhsOtwppPJK69OmalaQHp3d6u4l1O8dQCeBrIVQ2fEGhbZkKFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
💣
💣
💣
💣
💣
🇪🇸
خبر فوری: فلوریان پلتنبرگ: رودری اکنون به طور رسمی یکی از مهم‌ترین اهداف فلورنتینو پِرز در بازار نقل و انتقالات است. مذاکرات با نمایندگان این بازیکن آغاز شده و پِرز با این انتقال موافقت کرده است.
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/Futball180TV/101791" target="_blank">📅 17:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101790">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👀
یک استعداد دیگه در کارخانه لاماسیا درحال ساخته شدنه؛ سال‌ها بعد اسمشو قراره زیاد بشنوید..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/101790" target="_blank">📅 17:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101789">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeTRckbG8rf501Apoe_jADIbMkPG5k6Jua-PY-EnkCDOs6HHk6CY3qoCpZ6zYHWE7IJldiBkxwDrOBqKEBPVE9ir_22wb7uAsYlivdRCyv7Ihfz5Sx3gkHavJFG9K7yvH10AzPG3IBO-cerMq2qk6XjtFiEd6U0A7Il1TM5au_ehYPJzeWyYrYuCcbA_wyt5CuLYkyskDcrhieguou3z9mWveARJwh7NtqjHNMKAyye2zDYYa02617uDVw9Chqp7vPovzDkvp30PgPoNKoE41i6ToDuvIW3TMfVIGGw_6_RriLu9y1BmOY5Yacux49jszUU-BDREAPFQ3JYA90PDeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
✅
رئال‌مادرید به رودری اعلام کرده که مشکلی با عمل جراحی مربوط به مصدومیت غضروفی این بازیکن و غیبت برای چند هفته ندارد و تصمیم نهایی برای عقد قرارداد به این بازیکن واگذار شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/101789" target="_blank">📅 17:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101787">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vFu2W1LxLl_tyNaYbEjhCnmc_PvM5h1NNvzARypqy6mlPA8uBJ-8Ea1eZ6Sa5WJUVqxL8ofGUVAXgjE7CR2mZFlHo2UUweNy0gIB0UOYWR2B2QZTkN-8pd94OS5sRqcwrzlmclHfAFRQa7MmBbL9_10KVcn0_xCjgeDQRrFf7R0A70KpDd8i6-Pn9A41GWMWHsTFXf707klsOGlXD9i1c5BMKJFIfyNvkCZiTWRbpzxvz_9oH5mdiUgOf_zE6G3SPJ2Uzj_iCxI7VbmXzu3HWGSkr-ZU6HtiM2BjBMM1DzRkicZkDlEN2DVDJ4kUF4QRK-CbJVjQ6yRW3mQ1AluPIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UoLvPhfTBXH8cDlqwfcz8vaanrVkQHHSMT0rynRp7kx_ZDQgN01gnRty_xhdz_ACvHDZX9VCNnMb19dWEVRsM5VrvqnXMUYAwO1-BKDPxr8OxDIacXOoiaZU50S3H3igIwanC9d_hwegItgh6DCRXku8kDLjWMTdTATSFF0SoZ6Tb-4hdcXa7i-cQqOoKUiOlQgrDcyAlD1_P-H3mUhVYiv5HuOXOMr8TfWY5gPmYjFQBlYciJ3X75k1fSPVm6l8Ym6Sf8WwNPwjl6qSBH5uFS8KCcOJGzU-a3TBxtLn7XHiwettTWfhqBvmpZyBGJ_hUJtY-jfy6fAdNnXOoCW8hQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
مشکوک به نظر میرسی هالندعلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/101787" target="_blank">📅 17:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101786">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzLDowtEaEwmYu3s6WFGqSZfioBM-EK6Cx7NMSri2YxyoBPqrWV6E9bXkM3oWdc7Ik2cGsWSUb1_bwFz3gLHLEqEXYPSjQtIF444adA_CgBBEtakfQWXiDSIvK6N8RprY2v6gSwKUb-pIS3hIyXqXv3OoJi2nxOOcitCz4DDnTsZNRQQMcacAEfKlCGV0vtZgEiL9cZX2y-q2Dcn6NhSBlyimeAzOBVJxb4mEgFxTNsG0--VHSj0hqjqh1QYNFPVC82c8NYJziPfd2ilLDlpzt-i6y35f8A0l1IqS7JBwXLDCXC4GZvI_8ItS9OIL3yhTRs24QfxSeZugBdJSzviag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اسپورت: منچسترسیتی با توجه به شایعات جدایی رودری، مارک‌برنال ستاره جوان بارسلونا رو زیر نظر گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/101786" target="_blank">📅 17:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101785">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
⭕️
🔵
براساس شایعات منتشر شده، قرار است یاسر‌آسانی تا فردا به تهران برگردد و در تمرینات استقلال حاضر شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/101785" target="_blank">📅 17:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101784">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnoKGlEEvvZ5NJFspNoAQjhWZrDLmQ0UtXD8-pauxgeiwt3bOBCyD-ju3orc08yW7d3AL5Z4ZUG7mCry7MK_7etdT9Z5raYcVxQGVM8ovKWp-VN2CaSVKbwwTQ-grSdo_OX2YImWoKwx3LquG2v_yyG-lQiqPhOljFqpuQPF1-lrOs9cZk-zvXGIVsYOXSnVL2e5Ov4uq7W5XYlUWO9AFzsCsjZsVmo9eHBOGM5zxqHEfm2-bCI0EK22v6rMX-H6tGxj7hQBoRzBeIsTGoy3JsaQ22wGIkBZlY-tzp2DGDYZpV91kJPX9YOM1RqYwFlL6N9tRMRSUKBHnLJTxvfx5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇹
✔️
به نقل از گاتزتا دلواسپورت، آندره‌آ پیرلو سرمربی جدید تیم ملی ایتالیا خواهد بود و این قرارداد به زودی نهایی می‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/101784" target="_blank">📅 17:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101783">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e1ed1b860.mp4?token=J4QWih09MHfgPTyYr-n9u9BKOZMSTHSIYTeOrZ9HIc6CS6Kg6pJ5DmQp-rLjDKfNhlefaAXW4WwTLkn7-oE1nMySypOzKlLbJ3kIIXPhCTzrqDtkb2Od_sV9VQVPkwWF-wq4qK-DLU4id1FLsyhcPgpWRwoNEjtQk6UFWrWCMLDoi9hyIynjlA1i4oWlNM_7A0MpprLRG5jLBogHpBQKqro-GAm3rVqKbIbDh8PdiJv2dn9TKa2nGq7FlreaM_sm_x8B6ZObctOAZHUJGo3TVX7gWoASXR5wKlafqjTbuT7IN9s0hT6oaVPXJClWY5tB0J9faN4VebO5u5eDsQZ1aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e1ed1b860.mp4?token=J4QWih09MHfgPTyYr-n9u9BKOZMSTHSIYTeOrZ9HIc6CS6Kg6pJ5DmQp-rLjDKfNhlefaAXW4WwTLkn7-oE1nMySypOzKlLbJ3kIIXPhCTzrqDtkb2Od_sV9VQVPkwWF-wq4qK-DLU4id1FLsyhcPgpWRwoNEjtQk6UFWrWCMLDoi9hyIynjlA1i4oWlNM_7A0MpprLRG5jLBogHpBQKqro-GAm3rVqKbIbDh8PdiJv2dn9TKa2nGq7FlreaM_sm_x8B6ZObctOAZHUJGo3TVX7gWoASXR5wKlafqjTbuT7IN9s0hT6oaVPXJClWY5tB0J9faN4VebO5u5eDsQZ1aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
مهدی‌قایدی ستاره تیم‌ملی ایران: اگر میخواید عاقبت بخیر بشید، بچه‌دار بشید
😔
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/101783" target="_blank">📅 16:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101781">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WTBsOkQ3od8OpQnPP1ReSA57N_P4zA3cvX6E4_47rWgDICUfeLa7aJrbZNsGNP7IhEFkjc2m8YI0jyblU7GZ5ZEPEYJNP67esFSiLH80IQQoxE8xh_Lu62c7a758Bchakh0hSIhSjnsHWm9nlPtfhXKhn07a7U5gPF8p-dkmHqbMgzJP1MxvIhzXl3H6-XpB6D_qyLdKjwvKBhG9MjOILTj9d76UC9INFTLOLEXx_G9Z-xp7uXZQOVx039tgOrkVF1wx7ykvg1fu0v-T672sw-ebn9nPQZ9toxoRE87TdmSDX3YXe8s93BW-SSExcOmEJetoy7j2XXHRt4I-6C37WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/avuIHVUerGqT3mSBMqqFQ2qNcGXUK0jQ9y8RZ-cE2Ml-6M3feHXBNZoN6SRInCGz8gouE5OFDMdbXrG9w-wWwx39akZszjcEWwcmkW5wC7AcwNEwsR8tDIj2G71UDUnFbPWO2wsSWnU1H-9SXlENDSFZHtHwOiJnVxAYtz7JjljRF_wpuJ1LNu4wN2S4OHP7ZKGB_Nl9-K0ifnC5fPgxg7TMiqheqrFqgEKX7TAEmeK9QcfMtbpq6RO3mujyzDWIg-BTgCm-6Jy_Ygyxohmt0hSV5wWQEovHjw-gAhrGSnY1a_tpJrCWB04ESEQ2ssMrFZtIddTqQbsWPiSImF9zow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
⚪️
امروز، ۲۶ سال از جنجالی‌ترین انتقال تاریخ فوتبال می‌گذرد؛ لوئیس فیگو، کاپیتان و ستاره بارسلونا، با فعال شدن بند فسخ ۶۲ میلیون یورویی‌اش توسط فلورنتینو پرز راهی رئال مادرید شد. این انتقال رکورد جهان را شکست و بازگشت او به نیوکمپ با استقبال شدید هواداران بارسا، از جمله پرتاب سرِ خوک به سمتش، همراه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/101781" target="_blank">📅 16:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101780">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnAkUc-nThOo_Ybm71LUIaP_S2Z8WbRq8UfLzEq_OirViGJ9XR06foOk8uc1PAzIZtH0T18fxhGusli-_ErHw9k974m70MAz8o2umKBohhGMkTlDtdrIzHcqKdh0D8ANGJmppAaZ1R2BnK39RN7qU_-9ZlQ1C_oGRz2c9u6kWHbcx5ImRwpjqvt0WyZIAU2uzem6b9OTIVpO_U0KBW2HOUf8qYpzPlPJd3ezlNLuT4pZFbmgkoaawOwd1Jo9IbaKr65LHIzS8cH2-RvmV5LMSxVpwtJAhSzob-8qQKMDhR0tqiKgjiqxpgZvSqY5J6b7mPIalsjymUzjuH3_rKizgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینتر دید کسی حواسش نیست رفت به یه تیم از دسته 5 آلمان 16 تا گل زد. دوستانه نیست این دشمنانه‌ست بیشتر.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/101780" target="_blank">📅 16:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101779">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56f574b376.mp4?token=T-PHeDxvqe-N1-ysGLI6GTbSkqq3KrBJUyzlLiBOrSN_6R_l08oDEpKQZzbyzQplXyakoQV1IpjejStcsCFYb8laXZZ2ZVnC7rNwJT19t4WQAoYCnc1GOX9QxquEVwzU6P8BJis8kvd-VDRPjPAfWAmj3E1QfEkmX-vB3AZK-DSJrUOQWFW62t30__T6PPPslV4lLbDRdd-hDL18eDjuBXqrN3D0A6GnirJDTFygAodgnADkviALfYxyLG40spNXWs53JRADDb9SYf21yFZRq66Hael1iJw2qLJBVmpSRRrBcoW4HS_sAfvi-To5nZ2JN97YHl8GCvP2ByJmT8qfqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56f574b376.mp4?token=T-PHeDxvqe-N1-ysGLI6GTbSkqq3KrBJUyzlLiBOrSN_6R_l08oDEpKQZzbyzQplXyakoQV1IpjejStcsCFYb8laXZZ2ZVnC7rNwJT19t4WQAoYCnc1GOX9QxquEVwzU6P8BJis8kvd-VDRPjPAfWAmj3E1QfEkmX-vB3AZK-DSJrUOQWFW62t30__T6PPPslV4lLbDRdd-hDL18eDjuBXqrN3D0A6GnirJDTFygAodgnADkviALfYxyLG40spNXWs53JRADDb9SYf21yFZRq66Hael1iJw2qLJBVmpSRRrBcoW4HS_sAfvi-To5nZ2JN97YHl8GCvP2ByJmT8qfqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
برخی از سوپرگل‌های لوئیز سوارز در بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/101779" target="_blank">📅 16:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101778">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3068c762cc.mp4?token=WhgJV2xcVNmNCvh6dbPDlWbwRCR7NGQiomw891BE9Hs01JUd1_XqthrGDcSXfE7SbkOoAs_G0g83DIbIuTmIHXeMLOgClZzd1KR1AEd9v8NBe7EdBuIrUPwVXHO0RhCKhFc2D04C3dJbP_L7sOE9h4z4EW9NI4IAqDzzL3ynoEgKdecfLSn5hPDdJH4Z1DgpSRs9OvkAAIRjSG-8voL785cGuH7MfR2-o-_aKOYKz6q9rhv3Ot6MVUTyunE1PoDOTLcfJAABiF2qYKTYsCQtFNLTkXvLq2FHUMMXABnDUKpyg5iuRBOsyww5ST34go0yEngBYRWEKbIU3mlyrGo5TDOD6wexGj-0mOcKbhf7U5qksx-PWkX_eZRPyQh3s5X4MNfKVaeY13HvyvTu2Rt6P_dsys3tQ5AWLP7cx5Mt0FLG8_zzxNoIaIZx91HYs2Bq-fZ_Zi5h6imYLC5732i_l1bbRAkqwIiOkDrH16fo297plfAnyikTgehRVD646SZEmcauXYawE8TzSe_rCEMpogBxFGpo3fZ04sO4wx4lqOJ7iw3Kq6wo6NhE0KsXULxNptkDHf_Pjg3x34h4ZGQRasMdhUObzeneNbbyC3oC6Jj9BaGu1zuWVZnOFxrUBxBcaYFzYIyStjJ_4FWUaNmCqw5L5j2fqVMg2_CCrTP8aik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3068c762cc.mp4?token=WhgJV2xcVNmNCvh6dbPDlWbwRCR7NGQiomw891BE9Hs01JUd1_XqthrGDcSXfE7SbkOoAs_G0g83DIbIuTmIHXeMLOgClZzd1KR1AEd9v8NBe7EdBuIrUPwVXHO0RhCKhFc2D04C3dJbP_L7sOE9h4z4EW9NI4IAqDzzL3ynoEgKdecfLSn5hPDdJH4Z1DgpSRs9OvkAAIRjSG-8voL785cGuH7MfR2-o-_aKOYKz6q9rhv3Ot6MVUTyunE1PoDOTLcfJAABiF2qYKTYsCQtFNLTkXvLq2FHUMMXABnDUKpyg5iuRBOsyww5ST34go0yEngBYRWEKbIU3mlyrGo5TDOD6wexGj-0mOcKbhf7U5qksx-PWkX_eZRPyQh3s5X4MNfKVaeY13HvyvTu2Rt6P_dsys3tQ5AWLP7cx5Mt0FLG8_zzxNoIaIZx91HYs2Bq-fZ_Zi5h6imYLC5732i_l1bbRAkqwIiOkDrH16fo297plfAnyikTgehRVD646SZEmcauXYawE8TzSe_rCEMpogBxFGpo3fZ04sO4wx4lqOJ7iw3Kq6wo6NhE0KsXULxNptkDHf_Pjg3x34h4ZGQRasMdhUObzeneNbbyC3oC6Jj9BaGu1zuWVZnOFxrUBxBcaYFzYIyStjJ_4FWUaNmCqw5L5j2fqVMg2_CCrTP8aik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چطور در لاماسیا، مسی و اینیستا می‌سازند؟  اینیستا و تشریح سازوکار خاص‌ترین آکادمی فوتبال جهان؛ استعدادیابی در سرتاسر دنیا، مطابق با استانداردهای بارسا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/101778" target="_blank">📅 15:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101777">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">▶️
👤
به بهانه تولد 49 سالگی مهدی مهدوی‌کیا ستاره سابق پرسپولیس؛ تمام گلهایی که در در تیم ملی به ثمر رسانده را در این ویدیو می‌توانید ببینید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/101777" target="_blank">📅 15:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101776">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfurPxkr3b3GGrFzNcrw5UewEl_jYP9757ujNvUnLRV2hbQD6PnvKtS11LXsRaRyrI82sZYc-tLWOG6CrFXTdM3eSD9qfRmMD5p8Ka7OXDwbRa4vPlpYvtdRKHUTQg9TcH4krxXTEG2Nhdro54r2YL-jx3or2-hI_GzOXDArFsUXHm_ZDGP8bLZtNAxOyjBSCpgZ2uWZ8TS0hN2-i8IxpOoqKJVNuyUxrhSf3fwDGQ4I6MeMBqUDsoPyloh37i4YvknNagheTB9T1ndAk2fkEmEuJvbIpwPJxr5KLCsf0orN0Iu2VFR1ERMkCeVZ7IWqKUF2PFDVg2MFzszi2cqY5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇩🇪
یورگن کلوپ:
با چیزی که خیلی مخالفم فحش به خانوادست! اگر به خانواده‌ام توهین کنید، من می‌روم. اگر روزی فکر کردید من مربی بدی هستم، مستقیم به خودم بگویید؛ همان لحظه بدون اینکه حتی غرامتی بخواهم، کنار می‌روم. من این کار را برای خودم انجام نمی‌دهم، برای شما انجام می‌دهم. با وجود اینکه دیدم با ناگلزمان و توخل چه رفتاری شد، این مسئولیت را پذیرفتم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/101776" target="_blank">📅 15:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101775">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cz2sQB_9XbpS2IFCYHNB4glIn5QlaxpZCTvZd1hID2IVMohFsprEopYm8RhotiOvIYQeTe-9kDWqwtzpXRgx7cb2UwCif4imS8vSdLiKwXj3XX7I2PqYl5nnd2VNjoEzdDVh_yLD2o_LA0O0MddM45z-E9KsifxJFVvL732Z2ADvh0OEIH_AXk9UVDx_XGVP_zaT4na2FS4T4t32P3pHw-qULSlqlE9Hi5ePz7-JLwdz0Tw_XGutHeKAERDs1rjVLacWoIMRH1_uvzd7kzkqcvivj0mcI5BpIEJrBmPrUa15qqsoB6-OLx7xIHwl4oZ27AC-QjdMJc5lTUfcbmp5dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
دنیله دروسی:
عشق من فوتبال و رمه! اگه بازیکن رم نبودم، حاضر بودم همیشه 10 ساعت با ماشینم سفر کنم تا برم استادیوم و تشویقشون کنم. هیچکسی هیچوقت نمیتونه رم رو بیشتر از من دوست داشته باشه.
تولدت مبارک آخرین گلادیاتور رم
🎉
🎊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/101775" target="_blank">📅 15:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101774">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfxP8gb1t-vA6Eah-xdhVtumuSv18iS7aiaj4EaxyvPFnBmj6hsOuHmcyIYdtKqDXQeSTOJ0wNwC31stTxLIeiYz2d2Hcawik5-RW4wizrYNYroWfj7IPDo4wJEIPsjJXauHVCwBlWr4LBAH_2XcNWKEp1CiYhAfD4ceaL9d9BeVHUnBDgp7fSOuh6qzgg4ezptuIS5jKPONFYrzTD0tjMgGO4blns7HZfGgaWqA3iohK1tHqhGK4m_gTLexZJZOAKA4FdDi-lBkPrVSGXhvkyrtmsSpodq_zx3viASj9npCeSaCYBAsCHCU0_FcdXN1bTvN-1VoqQ_yihMdr1ycfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
قرعه کشی مرحله گروهی لیگ قهرمانان اروپا 27 مرداد ماه برگزار میشود.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/101774" target="_blank">📅 15:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101773">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clueHMXRwImuQOT7jECUiS2sSI9KyajBws4zMzuOU7di_HH-zTfgV1VsNMegsGf71CVq2lGRN95e0c9dmq7_RGCxg6RvBKImR5JpMwKW3-cSSpsnFTecwn2fR_7LlfvZi7pgTzy3gt0ZHmsMUgvtNjvx4y3Kx6vfo4niPMe9UWb_DaLIAH2zjozplrNHHrgwZZtgr-iks7fA_COGUEL2ADoutHs8msj95dakRBgL08FsXJJhMttJNAKccJQ3rmlyw3UFNTxWQ5LH4e3gpw-NH3Mnt3tMQZ4VbDasH6xUyvDV1wk1wBEVoD5ZYDB-eWlwKBTHfcQJrR4axd1uAKrqjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
📊
مقایسه عملکرد نیمار‌‌ و امباپه برای پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/101773" target="_blank">📅 15:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101772">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZk2dWg-5cR5S753TyFKFgrwh1sSjlX1UGvi63GZFkcvNy92DOoHaigoC_ay7M4_LMGH_4Nb4jKpU0nszgoJInh4OGOk0PcEEmniUuvoHWi3FLtIYzuS8XewzQTCbDw5WF84gLVvz1roGAjxzoZF9PTplVWfPB4H0H18-xZUrQb5ATPyXmrNvvAuGQSkMJt_YqokQXD0ZS_xaRhqwBZ5vnlqEUVibizDTm8Su6iGMLyhRF-ZHdKHhy6fMhxSRkixbO_j7-x7vYrr6jOSJ0zmlFXOHoXOk2T9dUHKJoPtniufH-F6YFvkYko2WWSZr3ZVQdEoE4zI18zEoQ4epvvzDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوریییییی از فابريزيو رومانو
🚨
🚨
🇮🇹
🔺
پپ گواردیولا پیشنهاد سرمربیگری تیم‌ملی ایتالیا رو رد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/101772" target="_blank">📅 15:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101771">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVk1rew7ouBTwZkJHy2bdPCBeOd7wU4Se9eu95wc6dLuZk7lzD8Fo34DzmOrUWpArsTFBE7v5TOqy6eQVSCRUWgYVC8gUiliwecVkH7YjqEJObMlgJ6SYoNSca_yLlcptn2204WVCbbtozaUl4k4wkN2R8VznE8BFJCpjuT53_PRfLjnSqRxmNj4KItr44ikIvO9wCm4xTryzico5e7SX1KfCIBdNGC5jHS38va5o0bwqGWQhvKrgWvTH6OLMzo2OTGmvNHWQOLU5hts9SPDGjrulMriR_GM6n1VAZ20Vv8YUBcvjeOQsszlAku7612UbuZcKCd-m0LLNSAjqlJoxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
اندریک و خانومش و بچه‌ای که خانومش بارداره به اسم کندریک!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/101771" target="_blank">📅 14:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101770">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmaI17uaAk7T7jxuNTe-cegAhxTm9iCQL2hjrebPTMGtF-ihqiopGy0D0gy4Ree05S5QPSZQUHP6eyXtAtKMP3nt_dfznwjdMGzDhIha1dCHBhls_90GZ3ycQi_KhgibUwnba1Gdnb9gj-GXL_uI7M-r_udMTGpC1boWEScFYoHQ9xRGNMNkgmFAccR660-mwYStyoulgniEMeyosGAri-KyJsyWPPHhVlii9LqTDHuNrggLCXIuYAwCML-4GDz0W_ZV5on63AKKje1Vpl-7hE6Y6LOVJjZgvkJzpuzexJ6kAyvQj8stcIl6gGHWUYj3b2BvDO91k-og19aza23iPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚑
🔴
از زمان پیوستن به بارسلونا، فرنکی دی‌یونگ 416 روز رو به علت مصدومیت از دست داده که با این مصدومیت جدیدش احتمالا به 566 روز هم برسه
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/101770" target="_blank">📅 14:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101769">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/accd9e1667.mp4?token=RFsmCP2SwT8lF1giaNRU62B-VM6PdNLr5dH55JbfRxdL47zPeK6qhbDH_vyHzm2dpPKVbq_Qnb3mi6-ZtdH-B2jz3ECWcS27nRt2KUwpSJTQhUDkkceqmnfpnOK8M0nKGFKU9Q2B6S5Jwon3GxRvow8ChAivf76rdlyhSle7N01hAtUz2liXfLjZwtgTsbUrcZ-2EVYt2DruRR4j4bFV_fm0VjvgF_TXoHRbKkBn6UbzkUj7XXPtt7XREyKYsovaPMKPwvtSbWaS5dAG3w_djFaylCHQrOqiJ9tfr_BVdpbxxRavd8sUX9j87zDoXTWRa-59yVJIrXI2BUQfO4k0YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/accd9e1667.mp4?token=RFsmCP2SwT8lF1giaNRU62B-VM6PdNLr5dH55JbfRxdL47zPeK6qhbDH_vyHzm2dpPKVbq_Qnb3mi6-ZtdH-B2jz3ECWcS27nRt2KUwpSJTQhUDkkceqmnfpnOK8M0nKGFKU9Q2B6S5Jwon3GxRvow8ChAivf76rdlyhSle7N01hAtUz2liXfLjZwtgTsbUrcZ-2EVYt2DruRR4j4bFV_fm0VjvgF_TXoHRbKkBn6UbzkUj7XXPtt7XREyKYsovaPMKPwvtSbWaS5dAG3w_djFaylCHQrOqiJ9tfr_BVdpbxxRavd8sUX9j87zDoXTWRa-59yVJIrXI2BUQfO4k0YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
در چنین روزی، ۱۶ سال پیش، ماریو بالوتلی در جریان یکی از بازی‌های دوستانه پیش‌فصل منچسترسیتی این حرکت عجیب را انجام داد. روبرتو مانچینی آن‌قدر از این اتفاق عصبانی شد که بلافاصله بالوتلی را تعویض کرد..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/101769" target="_blank">📅 14:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101768">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33b6580c49.mp4?token=rhyyiYW5TwZG_7FwBZm0_Z6WbLBvgmYZnGPDsqTGkgcsdtc8l9y8qYriRBCeOfbyjZqaRU1gL2ejKKDG3SqSUU-KUflGhGeMPBDadxG8VS46L9nVUTIzagIgf2fG_m40b6e8awaz5pZ9fdcMqVkio4af5n_pbyOYIiwHQRnwQEUZLvGicjQkZXAbOkiBDpISfagJPixmH_u5Nr3ZLG10-eRIjlXIMCcLc0D2-pUsycZhrMyMStuv9PKGztOcImnVDtLOPAfaSpXd9j3u0Kddy1hrUpwu5wO8tBzDSnj8_zUFk-FdMdV5KPbIPtfDId4nWkeFdgMaGEqWqb6MNdQbEDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33b6580c49.mp4?token=rhyyiYW5TwZG_7FwBZm0_Z6WbLBvgmYZnGPDsqTGkgcsdtc8l9y8qYriRBCeOfbyjZqaRU1gL2ejKKDG3SqSUU-KUflGhGeMPBDadxG8VS46L9nVUTIzagIgf2fG_m40b6e8awaz5pZ9fdcMqVkio4af5n_pbyOYIiwHQRnwQEUZLvGicjQkZXAbOkiBDpISfagJPixmH_u5Nr3ZLG10-eRIjlXIMCcLc0D2-pUsycZhrMyMStuv9PKGztOcImnVDtLOPAfaSpXd9j3u0Kddy1hrUpwu5wO8tBzDSnj8_zUFk-FdMdV5KPbIPtfDId4nWkeFdgMaGEqWqb6MNdQbEDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
کدگذاری به سبک قلعه‌نویی؛ واکنش قائدی به حرکات عجیب قلعه‌نویی کنار زمین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/101768" target="_blank">📅 14:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101767">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhpcgCfdosoUdpGnn2bEYJNnZk6ySyBKPZu11x_Gb19UC6KEAix9Ms8EaTfm7tiwEBjgxBpBewze_khKr_ZSZF481uhpx77ULGpghpipRn2Dac8EeokLmxbZYoMrnjbpjp0ug-_lVDuu-nJp0DILoWhfGUZkaA2v84ib7bdzNP9VRr0wzsD91rE9vYk0PR3c4KZ38EU-DZquMSX5jQ7LGZ_UGLdcXrPg8UXUvDGXVm79QWc2YNtSLDyIsoM1Qr7QJQwMIrTS6gcjfllzSWs_WGRHyon85apCPxd-RJ9JcsebrSz_agZFwu_Uv7gUwrIVvrOEGDj6wpJ5fHepB7qRlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نفرات چلسی برای اردوی استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/101767" target="_blank">📅 14:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101766">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f65adaacf.mp4?token=ltonaENLPwoTnRjhq7MWU7hwv6DlqhbcKYXK8SlWEtCugMn5YOzw9bDavLr9ICJSdcKvNuGESxtqW3-iEQmZMaRFORIwB9EY8xCFBZJYPqiSvtzwZR1RZmJcuw_FbGKkG5oc-WwmcgEICgtMk8NWb2WMT2LlHMf75opI3AI7y_b0kuj6rFrrJ_OiShNR980dVBA9kOmB2LsC3IpvNI4gn7TDCtIpVE6RaPoLLMobkXAA4-Si-uC9VQyVCm3Tu06AlINbdFSS2K45jRv-VJImC7Ry4blM1bw62Heiycywq7NNdGXfedZ6nRzfamZHGHgNYEI2DhJONKC-YTmUPCxX6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f65adaacf.mp4?token=ltonaENLPwoTnRjhq7MWU7hwv6DlqhbcKYXK8SlWEtCugMn5YOzw9bDavLr9ICJSdcKvNuGESxtqW3-iEQmZMaRFORIwB9EY8xCFBZJYPqiSvtzwZR1RZmJcuw_FbGKkG5oc-WwmcgEICgtMk8NWb2WMT2LlHMf75opI3AI7y_b0kuj6rFrrJ_OiShNR980dVBA9kOmB2LsC3IpvNI4gn7TDCtIpVE6RaPoLLMobkXAA4-Si-uC9VQyVCm3Tu06AlINbdFSS2K45jRv-VJImC7Ry4blM1bw62Heiycywq7NNdGXfedZ6nRzfamZHGHgNYEI2DhJONKC-YTmUPCxX6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❌
مصدومیت شدید یک ورزشکار در جریان مسابقات مردان‌آهنین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/101766" target="_blank">📅 14:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101765">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ea14c8f5.mp4?token=sFnRmRh1xmYOvJ7JYBWAdFILhexNPVhvcQ-HxSYG8rUzKAv1eDrWV-dxYJhH-whWUYbnk0ZX1au-ALdwGZTUjJ0JjzeTYaXW0sAlAc_494Ew-96CoqMj4UmVgVT8QpRPLYbISJKAr6pb8Z1s43aX0dqAxiI3_NrqMI2-_YIiT8SKmnWDffz7ir66sOBT1Cxj8P2idWNpG-Yn4lLOoucossj0YLDH_pxJKOaXbxdi4QfmEqfL_t5nWvI68R5f2pu7TlbUWgHGADGxFCrzkLqJkjQex_kOuDG7yPoR1V6NcbVl3Gtd0iwpmXSxy-K_wYjDwxJGZU3Do8MtKGlHKJcT2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ea14c8f5.mp4?token=sFnRmRh1xmYOvJ7JYBWAdFILhexNPVhvcQ-HxSYG8rUzKAv1eDrWV-dxYJhH-whWUYbnk0ZX1au-ALdwGZTUjJ0JjzeTYaXW0sAlAc_494Ew-96CoqMj4UmVgVT8QpRPLYbISJKAr6pb8Z1s43aX0dqAxiI3_NrqMI2-_YIiT8SKmnWDffz7ir66sOBT1Cxj8P2idWNpG-Yn4lLOoucossj0YLDH_pxJKOaXbxdi4QfmEqfL_t5nWvI68R5f2pu7TlbUWgHGADGxFCrzkLqJkjQex_kOuDG7yPoR1V6NcbVl3Gtd0iwpmXSxy-K_wYjDwxJGZU3Do8MtKGlHKJcT2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
😐
افشاگری پشم‌ریزون اوجی وزیرنفت‌ دولت ابراهیم رئیسی: موساد به من زنگ زد گفت ۳+۵ چند می شود و سپس خط لوله هشتم انتقال گاز به شمال کشور را منفجر کرد!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/101765" target="_blank">📅 13:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101764">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a128d814cf.mp4?token=Y3s-6xbjrIvS5F_KqhqFcf02JvvNvav4QADN4HEAOC-Z1baBwl291AyO_9oQHSKXllM7A_TS4GMU4SIj48fjGnk8gwABiiFhhBZrp9t7L5DdwpVPWyLp7os7CdGSzpLSDIFWXPXdYKKXNZH1IvehjXUET5Ij4twq8GEY0WJ61inMYKQrCvkvppltK1y15crZoq8OHQJlrtKpvSlhGdn4YpticxE_8WjZ70smBwGo1ZlBxamn4hyjfzNtPb5gBvrkl5FWD9t4bqiVNBPwvqrZCjhVSOR6AsVJMXHPTXdKHnX-kOg_b_L3B1Yr8j0sIkQ5fe3tvwXa6OCDCP3GQekXfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a128d814cf.mp4?token=Y3s-6xbjrIvS5F_KqhqFcf02JvvNvav4QADN4HEAOC-Z1baBwl291AyO_9oQHSKXllM7A_TS4GMU4SIj48fjGnk8gwABiiFhhBZrp9t7L5DdwpVPWyLp7os7CdGSzpLSDIFWXPXdYKKXNZH1IvehjXUET5Ij4twq8GEY0WJ61inMYKQrCvkvppltK1y15crZoq8OHQJlrtKpvSlhGdn4YpticxE_8WjZ70smBwGo1ZlBxamn4hyjfzNtPb5gBvrkl5FWD9t4bqiVNBPwvqrZCjhVSOR6AsVJMXHPTXdKHnX-kOg_b_L3B1Yr8j0sIkQ5fe3tvwXa6OCDCP3GQekXfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🎙
پیرس مورگان، مجری معروف تلویزیونی انگلیس، بعد از باخت آرژانتین به اسپانیا تو فینال جام جهانی ۲۰۲۶، دوباره رفت سراغ انتقاد از لیونل مسی.
گفت: مسی فوراً دوید سمت داور، مثل یه بچه مدرسه‌ای که می‌خواد یکی رو لو بده، تا باعث اخراجش بشه. به نظرم این واقعاً چندش‌آور بود.
این‌همه از «سن‌لئو» حرف می‌زنن؛ همون کسی که می‌گن قراره بهترین بازیکن تاریخ فوتبال باشه. ولی توی فینال کاملاً محو شده بود؛ انقدر که اصلاً حس نکردم توی زمین حضور داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101764" target="_blank">📅 13:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101763">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uo7dPkxJHJExPnczQqFzZDSBXrlNZfvtHOB468fihtHcDVVgzb3lGDiEUaVZnq6LNPn8btUabfNCtJLc1zV5kbXpDpblqs0tr7tCUu9BxEGxuH3sar0gCET1s4rQCoVtrtvs_5pYrxnCWZL9xbMghTgk082eimqQzqb6lsnaEPC1w74PkkCeQVeLF7p4z9z_S4BHO0QBO318M9v3FR4dTOAvAzEwa1QWzgBxyYIP1975xV2RjTYdZxkCOaYc5EC2lBV-YI2jhcu1ZgmENmoS8dikFqD2IFbp-bVUFg2zy2P4SaofvbgCL6W8vt4c_JWdmhfKK9Z6V7wLpkHGAodQKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🔵
براساس شایعات منتشر شده، قرار است یاسر‌آسانی تا فردا به تهران برگردد و در تمرینات استقلال حاضر شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101763" target="_blank">📅 13:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101762">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/632f699042.mp4?token=B5PtDtVGmiaX4EzxzWXSqU9ekpidDAy1dwLO-odKdQu3QYzRBUXn2mtD4hX33hfGQ3yLm9pHR3tfjefIiW3QKtE6eK_gqIu6rNzC0O-leIDQ91N4O__b4GQMIavaTzdM0tn1oH8pXHKdKLA59xsx4QXCri06wv6PxZPDK9WGK4NlF1sCgxqIx8QPSHmzU90_Jo9EUBoOmmj6sBXbxXF6UQ9L1sfkvNNOrzR4nX2Fs7DC0acmZtEy50uxSkdDxPDMusNdZtrGHYwFLzg0m91_qjr2f0V9DoRdhRtnBLmD-gDaUpISD5n1-6t23MIqUh7ip53KTH69hB0-aBYED128Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/632f699042.mp4?token=B5PtDtVGmiaX4EzxzWXSqU9ekpidDAy1dwLO-odKdQu3QYzRBUXn2mtD4hX33hfGQ3yLm9pHR3tfjefIiW3QKtE6eK_gqIu6rNzC0O-leIDQ91N4O__b4GQMIavaTzdM0tn1oH8pXHKdKLA59xsx4QXCri06wv6PxZPDK9WGK4NlF1sCgxqIx8QPSHmzU90_Jo9EUBoOmmj6sBXbxXF6UQ9L1sfkvNNOrzR4nX2Fs7DC0acmZtEy50uxSkdDxPDMusNdZtrGHYwFLzg0m91_qjr2f0V9DoRdhRtnBLmD-gDaUpISD5n1-6t23MIqUh7ip53KTH69hB0-aBYED128Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
خبرنگار: ارزیابیت از عملکرد مسی در جام‌جهانی؟⁣
🎙
لوئیس سوارر: با سنی که اون داره، میتونست بشینه توی خونه، اما با انگیزه تمام رفت تا دومین جام‌جهانی رو برای کشورش کسب کنه و تیم ملیش رو هم تا بالاترین سطح بالا آورد اما نشد. فکر نکنم کسی گله و انتقادی ازش داشته باشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101762" target="_blank">📅 13:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101761">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a535e73d0.mp4?token=EMPcfzSSFpOIX3BRp5D1Iuh2TfuFHS6Fhh1-p-oU2gxPvetolk66kQVydo57KxbKJYYCHV7ixJf2HuLkXcchm8J2ejcVkGDgDgXoQ_RCI6g34MaLNaVWqOpcLeFqsztVCUXIbhph38-pZ5wp7L3-g6Gxl7m3aHXBP0xSEJChR0BKPHp2IcvMq-vY_t4IhI2gJjJbWVxsAcJk4GMlnuqM4qyiLNZ2GcsTxkrLVOcszeWFhoR3mxuhh_BHRW_eYzeZxaDqgQ3xHSDAEQgngqVWhMPSjFXbw3u457shrVzdWrwXJgdT_QJAyHaBaJE4G0eN3w_Dlk3V2vI7eMFnyR70fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a535e73d0.mp4?token=EMPcfzSSFpOIX3BRp5D1Iuh2TfuFHS6Fhh1-p-oU2gxPvetolk66kQVydo57KxbKJYYCHV7ixJf2HuLkXcchm8J2ejcVkGDgDgXoQ_RCI6g34MaLNaVWqOpcLeFqsztVCUXIbhph38-pZ5wp7L3-g6Gxl7m3aHXBP0xSEJChR0BKPHp2IcvMq-vY_t4IhI2gJjJbWVxsAcJk4GMlnuqM4qyiLNZ2GcsTxkrLVOcszeWFhoR3mxuhh_BHRW_eYzeZxaDqgQ3xHSDAEQgngqVWhMPSjFXbw3u457shrVzdWrwXJgdT_QJAyHaBaJE4G0eN3w_Dlk3V2vI7eMFnyR70fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇫🇷
هوگو لوریس درباره برنامه فرانسه برای مهار مسی: "یه دستور ویژه از طرف دشان به انگولو کانته داده شده بود. کانته همیشه باید سایه‌به‌سایه و تو شعاع حرکتیِ لئو مسی میموند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101761" target="_blank">📅 13:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101760">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adad22d87c.mp4?token=H6ZZUWMFhIIN3VlPquU0RVs-rz-RyUBjOGaJV-S58ISBLiW5Sc-6n7qtFKAIW_0A6f_WLVxadqSIVaoxoOY6a2ewqiOJSkRiSYwyvMB05o2J68DTcR4-Y6dMkLxGI4-XorCbVYPy8re557QfTcOcOgte-pi_o58eFvqYO0vYoxcpfJvmOhVwHTyP8xp0sG3fvdQnh3ylDNCTOkOzvCwzco_D5rCDJ6lXVz069ibYF-jYYHALkdpdpJ2bA34KO_zI-au3zO2zIILh_z2KUFXukyWN_L6kQ1JT7xxt841-Y5W0hYUk4GCeIU784ArGz5Ky96zwBqSyfcpxAzMpdpUcD4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adad22d87c.mp4?token=H6ZZUWMFhIIN3VlPquU0RVs-rz-RyUBjOGaJV-S58ISBLiW5Sc-6n7qtFKAIW_0A6f_WLVxadqSIVaoxoOY6a2ewqiOJSkRiSYwyvMB05o2J68DTcR4-Y6dMkLxGI4-XorCbVYPy8re557QfTcOcOgte-pi_o58eFvqYO0vYoxcpfJvmOhVwHTyP8xp0sG3fvdQnh3ylDNCTOkOzvCwzco_D5rCDJ6lXVz069ibYF-jYYHALkdpdpJ2bA34KO_zI-au3zO2zIILh_z2KUFXukyWN_L6kQ1JT7xxt841-Y5W0hYUk4GCeIU784ArGz5Ky96zwBqSyfcpxAzMpdpUcD4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
وضعیت استادیوم فینال جام‌جهانی که درحال کندن چمن و بازسازی برای مسابقات فوتبال آمریکایی هست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101760" target="_blank">📅 12:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101759">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHavaanr95a53tSubLZaaEMUmhbHP_Lkuyf-KL4bOIbi0CNRlBcTsxoYDqqyJ4vbQQnV9juRKIX9vwxA4YlMF31wpzLaaEdw3Q0zB4q0okpWFzfddeGI4gwvFVYNEBf6hdQtev6dFf16fIuxzceKjXqkPmY98ORqfjJ7u3vtTdF23sQf7xnzaKVclGZILTujmVrT0SKYs-LcR4D3YpV1BVxCH3471ubIKAK7sfRN0R7M_vMVzTp98O0mpP1O2ttAZnA_Jn-mgBVCo2lExUFqQr5ErLWN9jo3DwfcI2oOVSXR3X6o7YJ8dWocUAlE_LvX7Fz3Oyi0LcsWOI6aJFf4dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فدراسیون فوتبال آلمان از انتصاب یورگن کلوپ به عنوان سرمربی تیم ملی با قراردادی تا سال 2030 خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101759" target="_blank">📅 12:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101758">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMg_vVJY5hwsUHX2GQ5ThU_IOiB45O6h3WLg_CM8StWZsNGzT8MoQniCD8kKrFouOi2v1fU3BpfcCGxbZnFFs_TRzfn2NWEunMz8kW_CCstIl-GMPQBil2InKMJALXJmrnt4lB-i1lMWWFvPOsZGgTy5O0Spp77JGTx6_qSFyALfqN7APmWvrM8a76u7ngyvIjfezc8PS9DQOOjbIexknCu7YyNAUDnwAIa-cA6DETih5rXbXRXG8qAa7RMqmkQd6zxYeyAD0uKOVES4yPBnLusHRjAmmvQJ9nVcgeDkTZgFwO6nUAPZrCPswhC72voPmdHKdgMLtIck6wqgd6xXrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوریییییی از فابريزيو رومانو
🚨
🚨
🇮🇹
🔺
پپ گواردیولا پیشنهاد سرمربیگری تیم‌ملی ایتالیا رو رد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101758" target="_blank">📅 12:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101757">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d513714e20.mp4?token=Abzt3iJ-NGrTj_rDnye3RKOTVT2Ym5Kvjh8bvYVS2eJeOA5wgEpS3aOG2H7Jof76EdclXaSp8a-HMfUYbX7wJhBG3ZA1eDztYwq5hNCpi6YNCBl_D3-KO8cpECVbOzjTHtAC496uajHn6L2EB_uCDOTKM_mQe5i2n8JDyogKkp1uGEiPrZqrK5fNGRJLOz8Yw0YQ3bO9SB8VyTsJtIvq9iktkeLbDsCe11E9y7b54nlT-68OBCzdE_T-iVr2WWHVGwKmbrInyeuVc289lt7n9dhus-Rb5iO7sKI8RqInWzfYW1x0YYF_ohujpa7SbGm63liDiZpAJ2Gr5zd0Bph2sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d513714e20.mp4?token=Abzt3iJ-NGrTj_rDnye3RKOTVT2Ym5Kvjh8bvYVS2eJeOA5wgEpS3aOG2H7Jof76EdclXaSp8a-HMfUYbX7wJhBG3ZA1eDztYwq5hNCpi6YNCBl_D3-KO8cpECVbOzjTHtAC496uajHn6L2EB_uCDOTKM_mQe5i2n8JDyogKkp1uGEiPrZqrK5fNGRJLOz8Yw0YQ3bO9SB8VyTsJtIvq9iktkeLbDsCe11E9y7b54nlT-68OBCzdE_T-iVr2WWHVGwKmbrInyeuVc289lt7n9dhus-Rb5iO7sKI8RqInWzfYW1x0YYF_ohujpa7SbGm63liDiZpAJ2Gr5zd0Bph2sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇹
⭐
فوری از فابریزیو رومانو:
⚽️
ماکسین لاکرو از کریستال پالاس به چلسی پیوست. 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/101757" target="_blank">📅 12:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101756">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47d5bde5ed.mp4?token=NJwwebh4JO8Ps82XeWLsNXT-G7a6UdyFMrqHnEGpw2NGwVMvI3ql5ZVb8l7ewufoOcBZdFo0YGon4I9laptK6I91g3h1Wa9O2GKb2uMgjZiBb1z0-GIGhZolI0P1E6bfEn-Zj1pkGjaGzbNEMSd2zruph2LHPnlmAvohQg77Vt5d2FuBbB-4lC6-gnLuLQzdJ3AToecZITxLgtRcLdC_qH6gRYYCHZipgKLCVOUsStlia1DQhgUW2KKgfXsLr1TR00jn4-ZN19S--2phG2sbPZotG0XWZRXBI7k5oBmSa6y87QbO2yDUO_keip0bx28uhp7WrIvra5p80PbLshqe9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47d5bde5ed.mp4?token=NJwwebh4JO8Ps82XeWLsNXT-G7a6UdyFMrqHnEGpw2NGwVMvI3ql5ZVb8l7ewufoOcBZdFo0YGon4I9laptK6I91g3h1Wa9O2GKb2uMgjZiBb1z0-GIGhZolI0P1E6bfEn-Zj1pkGjaGzbNEMSd2zruph2LHPnlmAvohQg77Vt5d2FuBbB-4lC6-gnLuLQzdJ3AToecZITxLgtRcLdC_qH6gRYYCHZipgKLCVOUsStlia1DQhgUW2KKgfXsLr1TR00jn4-ZN19S--2phG2sbPZotG0XWZRXBI7k5oBmSa6y87QbO2yDUO_keip0bx28uhp7WrIvra5p80PbLshqe9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
🤯
«لی میژن»، دونده ۲۵ ساله چینی، در حالی که تنها ۸ کیلومتر تا خط پایان ماراتن دریاچه هنگ‌شویی فاصله داشت، دچار قاعدگی شد. با وجود خونریزی و شرایط دشوار، از مسابقه انصراف نداد و با اراده‌ای مثال‌زدنی به دویدن ادامه داد. او سرانجام مسابقه را در زمان ۲ ساعت و ۳۵ دقیقه به پایان رساند و موفق شد حدنصاب لازم برای حضور در رقابت‌های قهرمانی را کسب کند؛ عملکردی که تحسین گسترده کاربران فضای مجازی را به دنبال داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101756" target="_blank">📅 12:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101754">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2O9vEwDrGP7GHrc3hkkhvoau5uTr07Jykao-JgOJIz32i1mNaYOlzKDWaKnNnV7XPyaIxlm2X9iL4FtLbSWHJCcplPkUyqr2gkBcc9yWUrmV2bFr5KHX97f_e13JhdyN0u9muBQzCg1FTLRrKDE4YH2-R1spJMkVwibfFqhluQFLFtLLLIlgqZTe70FTXc6lvqmJV5LecuoNNisq00DKViultKY3JIbWSAjT2mSJ6V-DLgibyLHWmG_UaBwseku_ThPTvtqQloLUZFNqNrauuXfi62S5vGjScxYLTWbDyFuzJE6gZG58jfWfCLhZS4-NC2Tf69AB2YdQab9cKY7LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بن جیکوبز:
🔺
چلسی به احتمال زیاد قرارداد با ماکسین لاکرو مدافع تیم کریستال پالاس را با مبلغی در حدود 52 میلیون دلار نهایی خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/101754" target="_blank">📅 12:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101753">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60409e4f3e.mp4?token=NcbUNbukg3LBsMLrUqceL0R7nIDs6-sZjmMKlYiGdEtrtAwxIih4hnb5Hp1_Iwn7MeQuGT4GtN0znVk6e2M5WHPzgLieDICVclsFOhNOa5sMFegUIf0jcYEckxo-c1FQRmlQpO390xB2RbWwmUg27BFMhGIbzEkgTQqf1yaY9OS2oEJm8sWpjrP9AHoIecwfXeTT_La6txMyAFxbumpfh-HivbV9LxnSySs7Ba4Vd_RhHpGfoSjoypD4B-vy1_iQ5zNl3CcVwI4z3S6jtglebjmcytgnDruK1x6qMVIECcB72XrEGS5wjPWUi-kVz6oVrYQDbdVKTW5KCbnkMBfoUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60409e4f3e.mp4?token=NcbUNbukg3LBsMLrUqceL0R7nIDs6-sZjmMKlYiGdEtrtAwxIih4hnb5Hp1_Iwn7MeQuGT4GtN0znVk6e2M5WHPzgLieDICVclsFOhNOa5sMFegUIf0jcYEckxo-c1FQRmlQpO390xB2RbWwmUg27BFMhGIbzEkgTQqf1yaY9OS2oEJm8sWpjrP9AHoIecwfXeTT_La6txMyAFxbumpfh-HivbV9LxnSySs7Ba4Vd_RhHpGfoSjoypD4B-vy1_iQ5zNl3CcVwI4z3S6jtglebjmcytgnDruK1x6qMVIECcB72XrEGS5wjPWUi-kVz6oVrYQDbdVKTW5KCbnkMBfoUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
انتقاد شدید عباس عراقچی از صداوسیما: صداوسیما مصاحبه‌های بین‌المللی من و استقبال مردم عراق را پخش نمی‌کند، اما شعار «مرگ بر سازشگر» و روایت‌های منفی را برجسته می‌کند؛ گاهی با خود می‌گویم شاید اسرائیلی‌ها در این روند نفوذ کرده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/101753" target="_blank">📅 12:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101752">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-65pl8uMQ7Pv2FL5cjKJ_wtj3RPGru9vba4KGN4L1KYUyYLhkS5-K8tpwpNXIBNffStJiYYrO1xcetrMxb4IREuGZ5AXVUOmCUFybuspohEPNpiEdvPZ4lvum7wKRjiy9_NhybRaP0QOY8xH0Utk5QWcsowOjlyJhxKooRnzgXv_Alh7HPaYccPvFkKaSOB-3pS0OvpkQzpdALIKX-ifghmdsLwI24mautfnZ7Ulfc81lihmvt_gXYfmYIHIcr7P2PU0H0StqniNt551d-rrpXcx7GLbOn9QPSUTPbDwssCXNPQtCAsiZuNH_hismHkjM4JTVemH70f4Q9dz3kTRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
اینترمیلان تماس اولیه با نمایندگان کریستین رومرو برقرار کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/101752" target="_blank">📅 12:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101749">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fb93Z-bbGx1HOMtozJkZvjATUBSxmCp2Co267nspnyTGYAdfqTRIAH7tYszWRCRmlVn3a4-bUu2l4Bqzvu7mFCMgKc_0wCZZmHkTlVG51y4rI225dJ5MQ5Lr0FEDcsHDiQc4wH_J9hcv6NgNvRuIgCL5aUOqKxMLvzhglMk4YG5sbY8L-dKb_T-GbfLO1qlqU-4H5BHHYTgSYSxw_wGXLuiHfG85qj8cO8pfBy1LRrgH9njFavw6gdSZicGKO1hOEb4HJxoY8GBYj-KtbRRUGbzSGficbdPp2TWP32ho695cYfB5wX89v1xIKfeWUBexlmCnN0_e0MWsMnhloNVc8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mHbBrssoWVhhv6D8mW2QBTXGD1IxPE6i6SteKmfB6uvw8j6RLOdqUycw53dP8o3WUJPMvqVTr2gcZpze4ASgeScfiudsLc60RC2bGggXy5jfgS8MZf_qjgIdbwatzepF1QPiSVP64jW1YqzizISiPJQ8X3A-yzpoTdWAql-bN9u8A2cqhPyEq3sfjh4A9MlusdTFehXdfYaWva2AFr9zJDeQTUFvYnQj-4wI_wuZn5QdLl2PMKspM3vvNe5Zf-a_EeD0XKwL5v6QNmzi3LXQGrOG2h_tudomOneErhzG-6G2EXYPiGxF1kYnUuS06sJlAPKw0KS3VFYb0Bh5ZKwHgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OcnpPsBeyiSsZ_YcUnn9ypIs3vLD5UYgIysqc7fRwIAEZWBYg0LI2AvS6hF2RcoT0a39PeB-X5PwxVYLO3bWcHI4ZNPfMnI34H0jaxQW4ZntfMWKS_NWyLwbkNmEbcKvZSOYlrtnNB5JhYan2OdfEYSct8QhKba29xifUCsvuV-FP4Uie3d4FIbuuiTW6aTklk9IWhkxhCUYtGJHklOonL8uNeYP0MKZu-Z8NUFpudtXWSg2RMi4Nr1tnB3W8Q3wfoTmkaMBqNaY4Z-kSOvwayS59-52wEJEB6pWsgk-hWQ-BtHb5SSPxKRdCYwdTMZmHos5mEYNw0eHDLjA4kbMQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
⚫️
کیت‌دوم فصل‌آینده باشگاه نیوکاسل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/101749" target="_blank">📅 12:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101748">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXHraIypG60UJV2mma5PX3YfTxmv1Yzl5dPsMkekACW9KM7qa5xymIuaNX5Q0zVQVzY9RFNZKjyC59hKj9wK0to_QNGDoN6g3ubqKLPxi7-BPI0jc5cWDRkNDiyXOxdhrSqDXq8lvw0QxxpEu9nTyndlvBJAE1Hou8zyCzveX5BTm_iA4i1D0993mmd5031qQ7276IGuP4SRC8LFzjM_cjxXGqWm6rcknqU3NWT0ep2ef1kdfJ8xAbtB3DsTVTq4DTQMapwR_OPL8va5VeE_lkmmnFCm7DEpVKYnHuofMAyvl9Psx-uHg6tQKeNg2KJoNeT5i1fvxr9w1m96cINNWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
لاگاتزتا: فنرباغچه ترکیه با ارائه پیشنهادی به ارزش ۴۰ میلیون یورو بدنبال جذب رافائل‌لیائو ستاره میلان است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/101748" target="_blank">📅 11:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101744">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tza--ZDT7lsGycKmWj76pHW-r6zVrBT-yUri5yHWzmAkd5rOr6LC0-Amu6VQjXdS5MloYRJI4pCe61fhfWrpaZjTp5HJWnCfFINqDaImJgdwEoswGl69zx2pQdqsmDKteZN9eO6B6b6COkLBZ1Bvf-1M325biuTkPCG6dpoJJ2ledfx28bhiDfykeKXSs-HPSDMu7zLRaRG2jcT0ZRHUl1SNHbOXMuLZpFxXEzqj9RldzGkVzkldOHQN56VIzVuFXSW-7FCBPv1tnWazcFM8OPbT8jEJ1JqIePfvLTC9VV-h5FskZP0R4Gf5bd3SAlBdz4_IQO7WaIoURNcQ2Jn-Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q9pUUYzLjbmvmi1lROAuExOMgaGZQh2AY92G_wIS05QIyuM9GoqWI-iOfS5-kKn9zXDVmkmYGFKnwxq1XchGB_89s2YczGuA4roRLy7r5bcXrXLQ3LJbf5ATw8Xc7iERjdboKnzF7n3q3LIQgAVb-GbMZnfzvBCsdbNO04-_WNDewAmj4fGaYcMtAoeyNQCjBDc8McLtIaWWbBXy6fKyQZA_1C_I0vsg5aSqugygYr0VlXKFEFf7TdT8dG1od8uSQR6ibxUoJ2BUHvddt901CAslI0o60K7fZmbMNSOYiMjWJDQoFfQ2jXPAIInBVTIdSv4s0DDZKOo1C6BegSkaUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PfJKT4oWPWDhcGNh_HSkfM4bp7k-26v2gvjP87CB5RXgPKXOBaKYvY05PfZOwmWFon58lx-qOU1h0JTeAR-WwHl4t588iTd3lGStWqjSg-vyNwsl9382l0eY-edZF_5I2mzC-DEF8c3fumY6PKf8DBzfb1P9Xipd4RWtExzMNH4LQAjvhsH0Xdu4LiUFZ0xAwR62RAZVHu8HJNfbYgO5C60KBSTayecgL0st5vXF2vXVJdMfMS9rHKvxnFR3MnJB0m-krEBD4JctfeX1W6KbrUOOjy088BcVXq27bOznyTy6YPf6fcBzd15H-EWFoSKhY6U_eXG_uafaXMd4N3Bd_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌دوم فصل‌آینده باشگاه آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/101744" target="_blank">📅 11:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101743">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a0b08e15d.mp4?token=LGHGtPCj9CRtKjtTTFYZKKSMxiZlAbuqGxZoL73u6dl8aGvbeptl073LEuf6YvNwsnNQzVVkeIPfDIfhMQ9c2ddGRvLnwLsGA-lcSUqgcljwQ08XaJJPCBFIe54-FgVBVZt0F5ya_tfMHBDoeuDP_bjiZX_8TyhIHxH-UUA9kiVafoUQUJkOpWnLunhmUzKH1FBcdpxF8ZiPKeiDfHdYhUwkxIaZOGfOo-ONFcVLlE_TX-0rN3HysXJL5h9AmN4ht74m5qtQ12dS8z2g0Bp8oUXMGuzn097Ir26Tc-e_VGTgfwxZ3HfKayFjs1t84k_my0pa4EOX9SIgQVMf4-vR3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a0b08e15d.mp4?token=LGHGtPCj9CRtKjtTTFYZKKSMxiZlAbuqGxZoL73u6dl8aGvbeptl073LEuf6YvNwsnNQzVVkeIPfDIfhMQ9c2ddGRvLnwLsGA-lcSUqgcljwQ08XaJJPCBFIe54-FgVBVZt0F5ya_tfMHBDoeuDP_bjiZX_8TyhIHxH-UUA9kiVafoUQUJkOpWnLunhmUzKH1FBcdpxF8ZiPKeiDfHdYhUwkxIaZOGfOo-ONFcVLlE_TX-0rN3HysXJL5h9AmN4ht74m5qtQ12dS8z2g0Bp8oUXMGuzn097Ir26Tc-e_VGTgfwxZ3HfKayFjs1t84k_my0pa4EOX9SIgQVMf4-vR3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
کاپیتانِ اسپانیا در رویای پیوستن به رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/101743" target="_blank">📅 11:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101742">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc95b900a9.mp4?token=bIBiLS5Qdt8e3Pzb_h1REWM5oRBfULqfb3nRiDMJ9I--ngPEhCcCndh-hQZS2ikfriNvcHg49TqTmvIos4oID_nl3OJiVS29FT4korWoX3qDgJWpf-0Vp-JT1tjITIRtKnWmk5Ybus4k5y15PzJeRzyOKftneBE2_MwSqph7On2XGydWW30UoGPxdMpRrEpCCViALtREw3BGs4GcTjgf9bDsRrqTweovzcGa2EUEBA3l-pDPr9XFDljIWpfFI5dORJS4i05C4eGnvqsw6LaLUx1uBupICVt718uUSHfSJ_De9uYgFgGXWbpJOvXmU4ZpxeHFX5hIbzWHgpOHuY9mnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc95b900a9.mp4?token=bIBiLS5Qdt8e3Pzb_h1REWM5oRBfULqfb3nRiDMJ9I--ngPEhCcCndh-hQZS2ikfriNvcHg49TqTmvIos4oID_nl3OJiVS29FT4korWoX3qDgJWpf-0Vp-JT1tjITIRtKnWmk5Ybus4k5y15PzJeRzyOKftneBE2_MwSqph7On2XGydWW30UoGPxdMpRrEpCCViALtREw3BGs4GcTjgf9bDsRrqTweovzcGa2EUEBA3l-pDPr9XFDljIWpfFI5dORJS4i05C4eGnvqsw6LaLUx1uBupICVt718uUSHfSJ_De9uYgFgGXWbpJOvXmU4ZpxeHFX5hIbzWHgpOHuY9mnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⭐️
🇪🇸
زوج طلایی اینیستا و لیونل‌مسی که از بهترین ترکیب‌های تاریخ فوتبال یاد میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/101742" target="_blank">📅 11:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101734">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mh9hyEzZoK6DkU7uHnmPqwZzzAJso8ujWYOCkchSzmfB69heDk3IHzZyglZJGC7iAR3e7TLlWUmTKREou48wqWqhT5QNkBr1-faMi6OtVaThMhRwez-hS4gOvckSQJ-imzFzfaCJGCwZlHR83U7Ku8FFmJvf4Uk2AtK2fyzkH0FzbBXWmQ27E2mwzPVImbFr7VxJxQP7Y-dWyirO1cuLuZa6BWkZbgJu1QBLg9y4113OQQMckKu7KVtv6UtvRozc2z2I92oP0ol0J64CQv5QwGXQo0nEyDJzBNqBgjfqpd5icg-M8O08cKAvLGAoIucaMh3VY7xXtWHxSHQLCDSeuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ho8GSJojYmHbaxpDqdpujhSn960MEKzhlXkP8MGApwFpaJj6rHY5U_JsXevMzHO9YRGGI_8o-1qVJ7iEquHxWEVKF0vtQK9CkL-37jvtDphnIDdwqaeE1nHj1nL1yAJO61R9RfJKpBA9Ou_STFqyTH_D0897IDDENxRVCuJwiflwyOJjybjwZYaq0xkihOIYomtNLnCMtCnfuf0iE_kOevfG_XO7vvgHxATn4u0e6OWuV_bZqxtCOJH1aAVoOHc-brPVvrp5UhQ_glt9lETzBtEQp7uUccpj6qG5LfGRg2aj6zon4U_JU-EcT3rx1ph76jo5eT5jmjZ0gRRyOmF34w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p-lNsM-Adkjw7M_a2P90yrWe8aAa5GFPPW7NP3kn-bN4eiYDGj0RRArpZy_WCHOXTmNWrLH5qXDO7x9EWxbvQC_w7enDvXquxuKeh0t9-wWRSKm1FqRdVVDlS-Z8C6sH3hUyA-irrFadfdoOqlUSpn-OWRL83FqxNyyZ3pRVnt_9aOfosw6ktJTm3yUuSc5HBl-1rNySaGf7UKNMdRvNRUFANhtG6Wjt7KXcDJRBcE0OeMZ6Ig2DFwqnm9O7r-uIXzlVpqCTKlv3xAa6eUSsKL0QuGFFzNYqo6LeoCGos0P3KKE-c9z1-c14YBf_E8XI9S42hiFdBg_ZtaISf30H8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nJffoNMyL9gwqHSZRp-5EfYkv7Ci4geB_4ser8aXrsJk2MGWY88zcad_9eWx3QtZTu4gb3IRN0jJNW8fSIBi6Zd-l2oGEBRSU-JmEab2H2oEVzLe_WTMRxcbF5B_RPw_dImuK2N4wi9cNRI1j8-MKz_zxOjaqp_mWW_E89Xc6rERWEDby59MW4vDZO0FmMi9yRhz2OEOqwWeG-_NuE0CM7-sLGJ08NxstlEPoqx4yjRU69gaUTk-O2Pg0iSrpnxzZEpJAyLN_zVzq37gFFnmUOaiMgNbozuO4GczIyyV-kGhvLOHMVBrI0hjswnfIHg7JDhi0dlovsgwsyBoh5rqcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vbiCkPrT29di3jZuclRDvyiwRA0_9CHenN3InJ6uaJAQepUdm_96fxuy-bsag5mdcG5Pc15UpmnZtxmgyAegrJv9PbO3K3gpB1UUnKs6OeoM5DDfmI5CYV1HdNvgZwxsruTHvdMYnsYSz80RAhK7tR58X0jlhcKDNNnPMYFwrbYmxvxtcN4dnklRGvbNmZZXtP9VlX-Mu1f6LFzOI6wc278OwODaTm7DIC7jK6Lu7Jhjacu6dQNp2HFQO4py4azppnqei9uiU_MqOesbpLiNPlIeFUGgM4ySFbKU4jumDHZIStWARaEix7xoFb1W9Z6TlgbYf-Aa62lPt72v5pa7Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NeTqv4FXr31EsCdi8KcfP_MOaBhZe51Rftq9GLaUD2kdDBpwzV-35YL_DQxlGOWxpmOTrrS0GZ-zhmGDcAhPeify79h9sfllU9okoG7i4iJDhKY0fZ6jDriv9klxxtvQiJYh35k1NrdvzzXAQdZH7gIoPGyJUEZJ_VQrKE2XgV2Kgk2Awo4DMdtGuXF8A7bl1cMrVyrHpLXQxl43vFQX02fkdCMf5P7CZ2eV2afuI9b0PFbpbu9hB0RuzKlQ9_gHPeEopCvsO2RpeK3QMVVmaGZNzv8IKHQKBd23JcmU-Ti3KIiIk00VRDBW_JJIPJWRF5jt2QLJxIGaX0M6hczN4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ppM2Lnhl3CEtjq8VdrmBzYXigAeCEDzfM7cGakzXO9lX4q92aVE63LPiVs5QclSrkVnqR6NBkwWDIZ6vW58bxEMYasODJ8_NLR9EdJJofDW_2genE13KM7OQdleou8d6k36G5U_SDoxk_IT6olFDU5GOscAUvaKxOYjx2YK61H0MWtUW5pLcDiphoO1AfZw0LHvprzfM1aIot8vyrLcOZBW5r6S_FqD8tJ6yJ0YZPMMga__1YRwl58MgIx0PPqGJeGV-qIJ43qzTZVF0aNhmwP4B3qz1Z1Zu6DZ82-cEli2I9CYjbbCbJSUeReUDB1B7fkL9eaMLs0XU9d9mtFF2Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XLXiaX1BU7BxXFeqPwbs-Eankxn4fcER_1ASlQOvLZw5Y4j6KvgW81dtuPpM1Fk89tC69Kzesn2LnfMEm3psmsSm87fFURy5YE1Kv3h0hrgHU6rqeL9v71Kf86l6tQto7Zf3KyQRhOkfW_edD0PmgI-ObDm9UGYYKc7htVZGLLeNx5f9YPe7QI_neSo5ZPjSVxIjVMIsuKeV39w_iMHCAycXgd1pc29MZ1SiqYWzMid_e0yXSF0-9lZbdTEwU_pGcniUlAu4ONdGZxQOuYThNtrsndD_RlSBmAnFK7oxnz81c6Z37kkffQQ39ZqneY8z_KZhuXriVKVOu8AW4BujmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔥
کیت دوم فصل ۲۰۲۶/۲۷ بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/101734" target="_blank">📅 10:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101733">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae0f2a4c9d.mp4?token=UBJ8fhsz7CJkwnzThRUSlRiiZxw1OYVz4o6otyvjpoSz5oeT9NnCO172lU4zQEqicK14YQkz5l-2HZj_0Ll7DvabGN6cLb1XlkYGmP4QzVDIe2Ou9F3iDibFhT4_udeITJ6rTLjrMlpptOCCpBrQuRfSPl2BL7UD2DdFVrNhV-plDhxm8ljDtGJEGjvpVU2uMkSVePgxAxgU1PhQgV-NsH8SsosM9yhGwVBlCxcN01X_Pn3-rHrPqJs8td2BexjoiyoR8wAOZWyP78otxLf-G4KQYzwI077Pj2vu8jdVFQUQ_APu8D-s0J5rYf8QabhltQNZbYr6UllWa9XzVtrt4htaHbCsq71cHLCn4qUezDbKHa8GOrlXqtXDXX60NeBtCr5XR-KlXEAJku7z176LyBdVOsQtesdyLGT-N2-Jn_gla7xrHkEE6fOOksP50I_L58N9FjCEh_Ak1tedgBNgWoSaX0iaoilch1bZHYwaxGI8y-PAB5ReWJZ-uNhixPPtoOVp-ElYCdWvzR3mqt_arwkgbPFUh9z3XmwbP0WDmcLncHSr3_wrKD_ZwPfrdLDZXmVvVR_8CBPEtWyjD2S2BhWWy3Qioa3xVYaG77XC8QlWgfvDA6cwJEDie9_gEvaU82eqe3nQYhdkjfZffhxXY1FCuuR0vsgEafmubLb-SQk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae0f2a4c9d.mp4?token=UBJ8fhsz7CJkwnzThRUSlRiiZxw1OYVz4o6otyvjpoSz5oeT9NnCO172lU4zQEqicK14YQkz5l-2HZj_0Ll7DvabGN6cLb1XlkYGmP4QzVDIe2Ou9F3iDibFhT4_udeITJ6rTLjrMlpptOCCpBrQuRfSPl2BL7UD2DdFVrNhV-plDhxm8ljDtGJEGjvpVU2uMkSVePgxAxgU1PhQgV-NsH8SsosM9yhGwVBlCxcN01X_Pn3-rHrPqJs8td2BexjoiyoR8wAOZWyP78otxLf-G4KQYzwI077Pj2vu8jdVFQUQ_APu8D-s0J5rYf8QabhltQNZbYr6UllWa9XzVtrt4htaHbCsq71cHLCn4qUezDbKHa8GOrlXqtXDXX60NeBtCr5XR-KlXEAJku7z176LyBdVOsQtesdyLGT-N2-Jn_gla7xrHkEE6fOOksP50I_L58N9FjCEh_Ak1tedgBNgWoSaX0iaoilch1bZHYwaxGI8y-PAB5ReWJZ-uNhixPPtoOVp-ElYCdWvzR3mqt_arwkgbPFUh9z3XmwbP0WDmcLncHSr3_wrKD_ZwPfrdLDZXmVvVR_8CBPEtWyjD2S2BhWWy3Qioa3xVYaG77XC8QlWgfvDA6cwJEDie9_gEvaU82eqe3nQYhdkjfZffhxXY1FCuuR0vsgEafmubLb-SQk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🏆
تمامی‌گل‌های کیلیان امباپه در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/101733" target="_blank">📅 10:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101732">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eabdc39afc.mp4?token=ZRSOaYJouaDTPujeqYkxNDEd4q5MWZ2NtiFzvFUC_yXYE7nnBUeFiW09atLbICn59kCzszC8DoH0yk_2mjRMuDidhfHpqvwCdIyfLEOWmMQe3gJjfUi3r5VatrE9nCgUcuvYxukoUtDXfEC6hSk3NtqN3bmbZryUUpzyI-qYLyg92POljHi6WybXrAnq6mqUzyHxRUwhEJMyN2cT7xx6_gwlsypHkv7SAQVDcipgiT500u7IOrwbLmVWNHBYmYTtkB5l0sD667BcF1mbLSfFWaTd1Sv8EKLfQJusxbRAfX7eOrX3mPkyGu1P9GHyhqTipIelIC3OhbTSjeS2mYh16w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eabdc39afc.mp4?token=ZRSOaYJouaDTPujeqYkxNDEd4q5MWZ2NtiFzvFUC_yXYE7nnBUeFiW09atLbICn59kCzszC8DoH0yk_2mjRMuDidhfHpqvwCdIyfLEOWmMQe3gJjfUi3r5VatrE9nCgUcuvYxukoUtDXfEC6hSk3NtqN3bmbZryUUpzyI-qYLyg92POljHi6WybXrAnq6mqUzyHxRUwhEJMyN2cT7xx6_gwlsypHkv7SAQVDcipgiT500u7IOrwbLmVWNHBYmYTtkB5l0sD667BcF1mbLSfFWaTd1Sv8EKLfQJusxbRAfX7eOrX3mPkyGu1P9GHyhqTipIelIC3OhbTSjeS2mYh16w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
تفسیر نام اتحاد کلبا توسط مهدی‌قایدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/101732" target="_blank">📅 10:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101731">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e10a696be7.mp4?token=BSGqqbnJJALEMig8Vystga0I4Z9nYv3v-JRWXlp3gMT0kajGjczoY5L2Wifa5usrlTF7a7VGMeN1ErEmLVP605eKsw1UxfCnqH5LrUQBwuCvC82ZViqpK6fAWYXfVsIw1EtyTxnb2x7kFeQdxQ4-YFe9MIs-RBoagxeX0WXw3EW9nm2FUfZIdpVJOZOJqyof30f77grOtCsUbiM5z-S1B95eFSzVjBWW-pdoSKmueGhQvroO7dDOIkS9oJtSLmWU4mqYS1LpnCvXS1MmWpyyyBGCxDdSFs1FmTYssQTEldtstfEwOaSMN4IZnqTq2Gyhum3php3GLA8El4jHsl4sig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e10a696be7.mp4?token=BSGqqbnJJALEMig8Vystga0I4Z9nYv3v-JRWXlp3gMT0kajGjczoY5L2Wifa5usrlTF7a7VGMeN1ErEmLVP605eKsw1UxfCnqH5LrUQBwuCvC82ZViqpK6fAWYXfVsIw1EtyTxnb2x7kFeQdxQ4-YFe9MIs-RBoagxeX0WXw3EW9nm2FUfZIdpVJOZOJqyof30f77grOtCsUbiM5z-S1B95eFSzVjBWW-pdoSKmueGhQvroO7dDOIkS9oJtSLmWU4mqYS1LpnCvXS1MmWpyyyBGCxDdSFs1FmTYssQTEldtstfEwOaSMN4IZnqTq2Gyhum3php3GLA8El4jHsl4sig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇦🇷
صحبت‌های یک‌آخوند حکومتی درباره عدم‌قهرمانی آرژانتین در جام‌جهانی!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101731" target="_blank">📅 10:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101729">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C9szXYxVWTDrNNSQK61hX8LEg3-viJCKmESllGlmuPycAa7Ha8pL7_ulux9wW7ge_m7t39LweIyjgglsFvNSPglLf1LMucJbmH9-az_8f98HycHScISEdmsNBWOo_mSmfryK-9aH-kUbsLy73wFV845zJk6GVbAlRBB9GpY90xSTJcB7kt-Ywzw8gE12kBU0eRDJtIR738teKjBVRFo26bdbzUv0angndus0nTIbWvLzLOMczna-_s2FDRWtU2Zvlu1v6Nasmce7n5URFuYKK6MHemvRZdZmmpXUH1KewG5vF-E5YQev-9BOIkO2uREFD3pxOH2zYdUAbjZA2Hxkhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T-SOGi2h_KVWzHpM4BHcVV6i-mBxNmfXqWQHTyRGBOwwMB5_phm5tK0b641_-Kefab6GHAW0DPUdFj55F1hz8qesJJ1zh6i9xLPicTe2YGw_YAg4Ty3m-Fr4wcLY30s3nwGWl0SjG91cf4EpfUuzS9cV9baamX8wRitD9i1Rcm9VJwA_XYNdpuoaEBst3BUofR2D_9T_oov628oSuE_-utBWGRzZScupcYlHgGRAjOXEuz__faA88VQ1_hQQmta18blnDlNEi8kuVrvcS-PR7OyqXbb25KGKj8ZibxL_Bzfz1IVDLMniu7Vc4LI8oaKu6pWqkteshhC50jGPVP5hpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گفته میشه لامین یامال، دو هفته پیش به دوست دخترش یک خودروی مرسدس کابریو به ارزش ۹۰۰,۰۰۰ دلار هدیه داده
‼️
این دو نفر در حین خرید خودرو با هم دیده شدند و عجیبه که این هدیه در ابتدای رابطه اونا داده شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101729" target="_blank">📅 09:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101728">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMHtpcnCXOzC69Kl45ez6BYQ9Q8aH06JpqBmkwd1cu91qxhG4zQcEX0JOltpERu18cBgUmB2QfDa3-nPBIH5jAhWe-PmhxdScNr_IGMRpzt-xaq83ZQlndYReKfSc9hwFrxQfL2kl918sAp6DcaopqTggB6wTTA3v-uTnjX3-PqTua3hjYikhvx5ESiaFi7EEhY331AjLGLqd2CCCqSHeZio2vA5ParObvy0wKQTaA9owhLnsUv_KVEHic83rq1n8Ryy9yHBJ0ByAvnRBsqySVexVuNYFN4M4P4fRAlzHKXqgQjvqmxqOXH9TytgDWzLwB5uGWeWz1Q5a8474H1Z9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇦🇷
پاردس: آخرین بازی ملی لیونل‌مسی مقابل اسپانیا بود و این بازیکن قصدی برای ادامه دادن نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101728" target="_blank">📅 09:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101727">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ct3SUCFPoQPWUmvfBHdGlO-na4qDU3Q49x-_sWDFNPlRItOcsUV9aGyFVBFsuuhmdYyE2tZLJLo-aWRcvaTGIT1hZnyd3jLvSObLzj1SEs1DzJHcNbeAjWxxGoirHpSG8y-T5LGijNWwR4Jl4Yr0RfXUWBNZR7Oqo9HrTvJtssQSokiL2BPlV9C5y4Yo7yNs7k2gBC86i5PFl8QkrV7kUWv3lh0ryoDpKE0TLwlbIXn5mafVqLKF1l5GH-EeJGqU2By79k0EiNUpNmZgi5W1tzGwSjSo36nYCbFxYAblyzMBxYqK_vLJtiWcHGsB0upD_YD0lR8235lardd8RF4Zvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔻
الکس فرگوسن: "آیا منچسترسیتی از منچستریونایتد پیشی خواهد گرفت؟ در طول عمر من، این اتفاق هرگز نخواهد افتاد."
🔵
🔺
منچسترسیتی از زمان بازنشستگی او در سال 2013، در هر فصل، جایگاه بهتری نسبت به منچستریونایتد کسب کرده است
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/101727" target="_blank">📅 09:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101726">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvfsJrrnVN-Qng2IJSPcZKf5pE2KByN4sLWefBGiwN1oyDPJm5oYSMkIQ_1POEpgxGMlY3EPepCOHX7m19jzfjRq2jy0zcYjIvcufCIV76VpSi2AOiIyY7xrl5C_zcVTiQy-I1M8LiWXJyNNrKvKuaRJxkJUPwSI6KoKxGpUl5AOFf3m_4rNE1zK5MJ-JVxezg6g-qgr67cobz30yKpu2dxfHNB5rWDTrEY04p47fg_7stGBjO2TW2VsEkoGu49Coj-HAVyBGH_5r1ZMG_fNI4lY1QgZDOVo8xxzfb24r5izNFY5ZRYpYgEpdWVUm1_U_4s-KI092eLETvJfCeuisg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏟
✅
تمامی ورزشگاه‌های میزبان یورو ۲۰۲۸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101726" target="_blank">📅 09:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101725">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbbM6PyTkdWNLqqHArDO2wJpA3PH7SXEFA8QVQwYnhC5m7WXhC8fTqxxBXkkvg7MviAvw4za_JW5W4qtWuUwo7qsi4kyENXH50_RXukNWYtBgVeo5DFFwfKteDrJIN7UYmPrvHunPE9Vnn83Mi4qM9ICsUn2s2D6WO8ulb6tRwn4hnVJHkBkOLFYFSJ8x5W4EAy5h-5SEmwimRd-97ZXbO-fadjXkq_RxnWqatpbBICKke17XznRHi49rjgJiw8Q2PWYmAeFE7m-HzitpASxXokhBMvL4Dc91UvWtAWMxO-BiRWYnUWfx9KvpKoxDSDAqp8MbWXF3zxQYaDpOghWzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
👀
کیپ ورد در بازی مرحله گروهی خودش مقابل اسپانیا، 0.28 موقعیت گلزنی (xG) ثبت کرد.
‼️
جالبه بدونید، فرانسه و آرژانتین هم در مرحله نیمه‌نهایی و فینال مقابل اسپانیا به صورت میانگین (Xg) 0.28 رو ثبت کردند.
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101725" target="_blank">📅 08:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101724">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekdBCmrI1Rtj8t-FaSuM_FpEeqOzy__OP1cCnlZUi_dVIZ_QQhQa-3Lhrp3fQ8-ixIZ3MGyoznKVxnMB5ho5MJZC0PMFWNbb0mNHrViAt1DlChoIDTsIwOhQ7qbNHwf5sxqWlOWOfobl1b1rsekbpfW6OFkHD7eI6Df4r6rwYgEal187LPPL4UQ8FXbsDJQ2mLVAiKqqff1AJQ5Pb2iOelaohDn-zhUeQAlzQG85Jq7E7x8A0KVAKZa-jaZAuzF0Rc3VdQrqByoKr0mSsQKa1K8N0V0r-B4o66LcHBzhiq-AdX7yqE82EdDJNzGzJxfrBvz7GKTLeOg_xwmYXuAhSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
🇫🇷
آلمان و فرانسه میخوان درخواست میزبانی مشترک جام جهانی ۲۰۳۸ رو ارائه کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101724" target="_blank">📅 08:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101723">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXCAcLjn6HIGGmaW6VghdXADSsCCL8jtyq_YATOw1Fgl37cp7RXzUj-jA0SvM81LPO3sifsZDCnV8E65l3VNu9Qp93CB9k6HYmf2EsUcXmgSYNX2Yl8bo0rTyPVrNJSwUKUHfcVpOo3D2cG38BJWARKDbWo8teScTd_YRCwCjHqvdrcN7iw4sz2yntPy3ItPup2bE2-pifyFsEKOrLf2y9e6CmMeaml_XNU0FraX8euY4iF9vvTuuRLn9cp9tiDLer_kqBlS07hfX1a1cPlMByjYu-uEYw9N1T0KVu1gYlWzHXwyCdJRx93I4eWZv_6dYGS9gBB4oZ2edD-O44McSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#
فکت
؛
پشماتون بریزه که بیشترین مبلغی که آرسنال از فروش یک بازیکن تو تاریخش درآمدزایی کرده 35 میلیون یورو بوده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/101723" target="_blank">📅 03:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101722">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729338e3ee.mp4?token=DRmXKzTr1ugyoqiFsovo3XlCtk6GmMm0tDRBg5WbzdvIOl3Hi520pQk3hXx7u3tMadlKO83OWrz_BpHHyrSuTkF0Ay1sStGgLIPDN0o99Xyz01Y0jDEYruu8qdbye2o1WUbqMyZ7bMfh57RifSWyPTI3U1bRCP7UbdJKZ39fksY31XnWJp7M6547tAbxs57NHlFpwEYpnD5g1B0ql6PXwwP_oi8fUFWw1U_t1_4lzDmzJijV7FRDsnC7hkgUjQ0EhPE4aDr_6FW9WctLVX7jjB89r3GBTbXanhy8U2THOAGZxcopplwQvwRYFF0-UYwC_3kFELNF4ISSMxHI4sTsNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729338e3ee.mp4?token=DRmXKzTr1ugyoqiFsovo3XlCtk6GmMm0tDRBg5WbzdvIOl3Hi520pQk3hXx7u3tMadlKO83OWrz_BpHHyrSuTkF0Ay1sStGgLIPDN0o99Xyz01Y0jDEYruu8qdbye2o1WUbqMyZ7bMfh57RifSWyPTI3U1bRCP7UbdJKZ39fksY31XnWJp7M6547tAbxs57NHlFpwEYpnD5g1B0ql6PXwwP_oi8fUFWw1U_t1_4lzDmzJijV7FRDsnC7hkgUjQ0EhPE4aDr_6FW9WctLVX7jjB89r3GBTbXanhy8U2THOAGZxcopplwQvwRYFF0-UYwC_3kFELNF4ISSMxHI4sTsNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اهواز از این زاویه
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/101722" target="_blank">📅 02:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101721">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb56b99a1d.mp4?token=gTus49tgBRFs-qjqGR3ehmK6jI8Rv21KAebHsUCxxMSVQPDksf-j2FkGLGFY0VA5lxqoLvxop38B78lZTnxXBZXzPy5A7ZYMj8ethGuKNn-gy-DUg4lPk5asv1lGC_q4LJVmC5idrwKs9q4g3NE4gCv6iQpR5FQ_x-jRsT7K8dD4-7edwNxro7E2EbP0PXvaDZeh7dix2L5KXgmE2QilxyX4Uwe2724p2gtpcSDx6R-oMDmfnnkE-t1JGI9dk57BbdX2z6BkNfZ6cnLXSL-O-qWWsteuAsjdKbNf4grdwvmB-ATS4oHrjPC3Yzm4KNu_NCLPQQToPGJ3-rrmJ7heu00V8RjQgA0AtFtdpFoYZdrNBa22XFN63LSiNrg8OxkZfVOGBhDmpFMk6SEx1czipvf5eoO8qiN3FganrgJ3l777oM_iy6T_z8GN2NhR7PjxhN93SfnroJ3Kf4rj0j-aJQxIGzYZdRRIJfesua4GItq-ENGyYjfYhtS_6y4gnWelbNJSjW94uizQcoo29yXuHtHs78q7CvkcOBuIzuFOulvUchnimaScOy-ZzGVfyyPh-FR0y56mZRnzp9dkQtGDIO73XLuZsb6QfrKx7Nt_R90ctMyUby5m2CN_DJylNkVic8tEj6qae2CBepwXB4wn42Xuv_9Esfc9U5tSSxBtCzk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb56b99a1d.mp4?token=gTus49tgBRFs-qjqGR3ehmK6jI8Rv21KAebHsUCxxMSVQPDksf-j2FkGLGFY0VA5lxqoLvxop38B78lZTnxXBZXzPy5A7ZYMj8ethGuKNn-gy-DUg4lPk5asv1lGC_q4LJVmC5idrwKs9q4g3NE4gCv6iQpR5FQ_x-jRsT7K8dD4-7edwNxro7E2EbP0PXvaDZeh7dix2L5KXgmE2QilxyX4Uwe2724p2gtpcSDx6R-oMDmfnnkE-t1JGI9dk57BbdX2z6BkNfZ6cnLXSL-O-qWWsteuAsjdKbNf4grdwvmB-ATS4oHrjPC3Yzm4KNu_NCLPQQToPGJ3-rrmJ7heu00V8RjQgA0AtFtdpFoYZdrNBa22XFN63LSiNrg8OxkZfVOGBhDmpFMk6SEx1czipvf5eoO8qiN3FganrgJ3l777oM_iy6T_z8GN2NhR7PjxhN93SfnroJ3Kf4rj0j-aJQxIGzYZdRRIJfesua4GItq-ENGyYjfYhtS_6y4gnWelbNJSjW94uizQcoo29yXuHtHs78q7CvkcOBuIzuFOulvUchnimaScOy-ZzGVfyyPh-FR0y56mZRnzp9dkQtGDIO73XLuZsb6QfrKx7Nt_R90ctMyUby5m2CN_DJylNkVic8tEj6qae2CBepwXB4wn42Xuv_9Esfc9U5tSSxBtCzk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو جدید از حملات سنگین به اهواز
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/101721" target="_blank">📅 02:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101720">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/213a7b9392.mp4?token=spzoU1z3HcCtpLqJbr1ecF4jJOdeB88k2tHTD3dUGf90-wtnN6sA5WjrjnBVVcmKYZOJDkP_fHB7LAtu8OK0o1202EsNwQ0x4nMPXZQ9DV9aFKY_L3U6yl0lj-aSiK3r3NCRRaiu6-d-eII1je4BllTLor0TsPKTDOVqwK8mZjWo-Oop0ClJQ3nRn0TutBTec00Oxb5NCFVO3EEcr0kor0Bk_o3da-6HlQECtLjzrpT5xPVqMFaj8qO39mlFQUFnHMG09gzaM0DnjXbbEgLQy4TWvaRNbBtvpfx4-fsrXCq1EiD5g73u_RBuHlj9cmLsaOpQanofbjp6YVxUG8Vi_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/213a7b9392.mp4?token=spzoU1z3HcCtpLqJbr1ecF4jJOdeB88k2tHTD3dUGf90-wtnN6sA5WjrjnBVVcmKYZOJDkP_fHB7LAtu8OK0o1202EsNwQ0x4nMPXZQ9DV9aFKY_L3U6yl0lj-aSiK3r3NCRRaiu6-d-eII1je4BllTLor0TsPKTDOVqwK8mZjWo-Oop0ClJQ3nRn0TutBTec00Oxb5NCFVO3EEcr0kor0Bk_o3da-6HlQECtLjzrpT5xPVqMFaj8qO39mlFQUFnHMG09gzaM0DnjXbbEgLQy4TWvaRNbBtvpfx4-fsrXCq1EiD5g73u_RBuHlj9cmLsaOpQanofbjp6YVxUG8Vi_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پشماممممم صدای انفجار اهواز بشنویدددد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/101720" target="_blank">📅 02:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101719">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
‼️
انفجارهای سنگین در نقاط مختلف اهواز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101719" target="_blank">📅 02:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101718">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a6c0f6a9.mp4?token=vDJPQiisOc_pwi6OH_IQkgS00LmCNIAreyTZZ-E8fwo2RHmJ9xL5ylLmbq7fpZKyMjyNgFsapvRuhYk7x1YlzrhJ99f5MmJxiCt8YIYRGhNwPgtVs9a8gt9mpM5uWoyqYMNgrfS9UyXhOrASKMEjnZyt7z6e3dZO9nRzcF8VwDfFVvpZ9KQKAHQ3HNog1CFcyRTvT7Kvl0aHL7-Qeq9jpv4WTSYmqWAfO1xnHDHFdb0Saw8KuH9YorJ40nBuvX7O9y56pvPo66CwsT196iVGVosnTmdHwUd-JTRPIvWmXzjy2Z0Bbvar82MuUsWxpISNX9VSesIuRZX_uuLLG4hpig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a6c0f6a9.mp4?token=vDJPQiisOc_pwi6OH_IQkgS00LmCNIAreyTZZ-E8fwo2RHmJ9xL5ylLmbq7fpZKyMjyNgFsapvRuhYk7x1YlzrhJ99f5MmJxiCt8YIYRGhNwPgtVs9a8gt9mpM5uWoyqYMNgrfS9UyXhOrASKMEjnZyt7z6e3dZO9nRzcF8VwDfFVvpZ9KQKAHQ3HNog1CFcyRTvT7Kvl0aHL7-Qeq9jpv4WTSYmqWAfO1xnHDHFdb0Saw8KuH9YorJ40nBuvX7O9y56pvPo66CwsT196iVGVosnTmdHwUd-JTRPIvWmXzjy2Z0Bbvar82MuUsWxpISNX9VSesIuRZX_uuLLG4hpig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
انفجارهای سنگین در نقاط مختلف اهواز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/101718" target="_blank">📅 02:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101717">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i100BpoonHNLE9I-j9bx7XPo9UKIrMbNv02oyPE_48JXNusMP11hP46C7FHTh8ru8CFOFN5fMiTlp31PENZiM-Oxd6TdXMK_FX9O8DD2Dzm2ce1FtwpaYN2A6ihoZu_iCKdTIYqIOgXlELk_D9cGbgf0hkjEu1HRy_jmfrqjDCydINqvv5F88bFdiCWVzHJ8vnV5SbCq8D8WbshkrKq36dfUmHRcwRJS9VLk5KhRirTw4fpqRxeleBEf9vsCNuRe3jGdEqkuqi6xDDIJY2GnTZ-M6IQnk-t5DhTGkr8fowayBUHon83yhSkC6eZAkQkxdZSMoNy3FVc8UDeONhnjqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
✅
کریم‌آدیمی ستاره بارسلونا و خانواده‌اش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101717" target="_blank">📅 02:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101716">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9db91c85c7.mp4?token=Hut2ZW2878FY875rzgximEELNflUhSszY2YBa8s8HC-XjDOohw73AqihKL-GoOY61CEsMw2zID0GO9Z8M_2dnKtahoXPKtIW25LQTSiMU_tl2Jth80dkn7VuxQm6U-pBcNI2d29p0EKqqtK9nDHkqdTGq4QljP7kLPHhOqc4n4VM6Dr1dqK0mG2OV4egX1TfmKfZBcNUGcFqxG7ziBMuo5mkCiyOcssg6-cdfvP4CKIE9UltHIp6Hr8DUTEQ-E1a5Yq2RSc3jJTNegH9HDG0GoJDR3agfz0DyeUD6xMdLRoz7oTNOa4rL-9hYkYel4Q_B8Xet3tL1PyL9JX_vQTqJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9db91c85c7.mp4?token=Hut2ZW2878FY875rzgximEELNflUhSszY2YBa8s8HC-XjDOohw73AqihKL-GoOY61CEsMw2zID0GO9Z8M_2dnKtahoXPKtIW25LQTSiMU_tl2Jth80dkn7VuxQm6U-pBcNI2d29p0EKqqtK9nDHkqdTGq4QljP7kLPHhOqc4n4VM6Dr1dqK0mG2OV4egX1TfmKfZBcNUGcFqxG7ziBMuo5mkCiyOcssg6-cdfvP4CKIE9UltHIp6Hr8DUTEQ-E1a5Yq2RSc3jJTNegH9HDG0GoJDR3agfz0DyeUD6xMdLRoz7oTNOa4rL-9hYkYel4Q_B8Xet3tL1PyL9JX_vQTqJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت تلخ کودکان در‌ جنوب کشور‌ بدلیل قطعی مکرر و گسترده برق...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101716" target="_blank">📅 02:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101715">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDqU6jt3xRntYj1WcBjiUGElTtHs2xttkEIp6G10nykjco7luFjQsqI0LT1PiZ5-GNIPEorIYpKr5QoLKxOzlRfzL1rnA1nnK5FhCtf8DX_q-Etn3h8Itv8IX0K2Km2oNKBi_gOTYHSONQiRlfJkoB4RVuICijLBtm-LplJngMOYZMJxqaGcLJvyiKHqtSvKq3J_2tz8uC7SWbkj_nuIxIiBWtX0BdcwHfH53aIeNv5f6tkeN7cACKT4-v2dgW15whesvdQ3IF_Bta6Su0P6Cbap07IMLSOyypE_DJNrCKIblqg2DLFKz6MCgDDmtgJJ2jQlJHu5a4VvHrL62Erb_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
❌
اوتامندی رسما از مسابقات ملی برای آرژانتین خداحافظی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101715" target="_blank">📅 02:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101714">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xcxvz00C4pU04sJtHNCcIkKpkTmfa-1jEopT4L8A4gUN5kIcrzom4Fel9YyYAXxwHXDWhRKpRVd6Q_7uf1ceC6bwoLPdFTH11iKAWDyTGWXid8bUh-0kLzeG1DnRZ0vevVQQFhzDS3nqlOnNxrcW_WTuyC9kmkrfGWxOuuyi1VC4o0xTBD6lKYiwiwXwOZPUXQivODMYgV6vT9_o84GyJi-cZy9FE4AaSQunxRdmUXVOs01-J_g7Ym0Isepu7WC9NXmvteLw3BrnKWskxK1Re29bin23c-V82xGLUo4cQPkJvYN9IpbuDetLp681WRkXv47GUZjHfdzibFCUH5JSzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101714" target="_blank">📅 02:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101713">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5f7d69dd9.mp4?token=kqkwmFEG99gM00gD93H-DPq4Gs5lnB4rBtBedg235mxEUYtOWEPyeyNV2f46oPrAiHN2p2kASYjkg28HefhM2jc5cLJr-XWNFs3vgjR_As3n12DwS2T43ZTX_ohKuR-8G95FmTV4HbFKl7CTJNrRSyn15YbY5Y3m6JpAlfNlkP5lNuvqCF7Od1v5aH-yLFly55LonHlaRTVGgCjE1hThBStMwsK-36gyyoFO0NF3iJ3W1OrevMwbkkBCuQ0-FV7nEkHLpY1YlAVfRztN3FBRX9Gz_X4lWdlbAMK-_X0WXLU7jv2wTVgdScW1BrZaLRow5-kfa31ghnC57sDqEU7OJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5f7d69dd9.mp4?token=kqkwmFEG99gM00gD93H-DPq4Gs5lnB4rBtBedg235mxEUYtOWEPyeyNV2f46oPrAiHN2p2kASYjkg28HefhM2jc5cLJr-XWNFs3vgjR_As3n12DwS2T43ZTX_ohKuR-8G95FmTV4HbFKl7CTJNrRSyn15YbY5Y3m6JpAlfNlkP5lNuvqCF7Od1v5aH-yLFly55LonHlaRTVGgCjE1hThBStMwsK-36gyyoFO0NF3iJ3W1OrevMwbkkBCuQ0-FV7nEkHLpY1YlAVfRztN3FBRX9Gz_X4lWdlbAMK-_X0WXLU7jv2wTVgdScW1BrZaLRow5-kfa31ghnC57sDqEU7OJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
نیمار دوباره در برزیل جنجال به پا کرد! باشگاه سانتوس اعلام کرد نیمار به‌جای سفر با تیم برای دیدار کوپاسودامریکانا، در برزیل ماند تا روی آمادگی بدنی‌اش کار کند. اما ساعاتی بعد، او در یک تورنمنت پوکر با مبلغ بالا در سائوپائولو دیده شد! این اتفاق باعث شد خیلی…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101713" target="_blank">📅 00:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101712">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24deb1c503.mp4?token=tcmUvX0w48Xn3zbMZrod1ogRdr4oLu0dMxa01Iqp0eNVxHBcIuhszJFEmYCCtOYg1VpWLd7J3XOQs-99pKfvfgkxOQ8JcU6HfhygPi-klnfQD_hoq6Pqzc-udm-RXcmlOckde_X_0y-7MWu8qLPD1lcPjsKhdlEAGkglxpGsATo90WxGmV_6qXTwUF1K0D7AgTlz7mGhgJeaHx8HedfaGOuZWlHG3Xo4hNjKgUEpPx569thXIdOrqBrIgWD1u9nh0ASZZ9OgzcAaHuADW2CqT2oy-g6BkG-PAB0o-MUlwlxYg57E9WFtvCxKMlcep1Ol_vz5Bcl9fBuTKxmZHb57DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24deb1c503.mp4?token=tcmUvX0w48Xn3zbMZrod1ogRdr4oLu0dMxa01Iqp0eNVxHBcIuhszJFEmYCCtOYg1VpWLd7J3XOQs-99pKfvfgkxOQ8JcU6HfhygPi-klnfQD_hoq6Pqzc-udm-RXcmlOckde_X_0y-7MWu8qLPD1lcPjsKhdlEAGkglxpGsATo90WxGmV_6qXTwUF1K0D7AgTlz7mGhgJeaHx8HedfaGOuZWlHG3Xo4hNjKgUEpPx569thXIdOrqBrIgWD1u9nh0ASZZ9OgzcAaHuADW2CqT2oy-g6BkG-PAB0o-MUlwlxYg57E9WFtvCxKMlcep1Ol_vz5Bcl9fBuTKxmZHb57DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇸
‼️
🇪🇸
یه فرد فلسطینی رفته وسط اسپانیایی هایی که قهرمانی تیم ملی کشورشون در جام جهانی رو جشن گرفتن، پرچم فلسطین رو بلند کرده و اسپانیایی ها هم پرچم رو میارن پایین و پاره میکنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/101712" target="_blank">📅 00:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101711">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nm7uFFvQLaO7G3YWMChehDIuThR6UPPVYyHQ9b58Vz3MiFnmX1f5wesLe6IRaS6vhrduItPo7ONHFv5SInTWJW07XVdeBJKxmVyOWdluG2EXc9xEJ1v_8ztfUzuT9QFiQPFI92RYaHMpgUAu09TGX5PFqlcqQfoKSoNsF0QZssGDI7UAilszJppDHwouT3vickMH3Xb50Ih7Ed3DII7eiA25hwdZpiyRVAFB6ItZrc4DEoxqvH9ow_Xwi7W00bFOBJdFtiB7Jy3o87C1akwEVweYtxGtUCEKDczOVQw07kXmiShorz9_Gd9UsKuKCM-YOM6pPvhArRODOQ-MqgPq_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
رامون آلوارز:
لیورپول قصد دارد وینیسیوس جونیور را در تابستان آینده پس از پایان قراردادش با رئال مادرید به عنوان بازیکن آزاد جذب کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/101711" target="_blank">📅 00:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101710">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTRkCIa8UyZnq0hAQRlHZlJEKr5Za9N41JZzDJRRH2yfGJXAOeosGmpEwlLHu-4lVDKDDwDhn62wgdbruAMFsUbloa-VRCLXKTIx9a2Fp8yWexRXgJ_lLCICvvyfTXKVoRxDy39UF3_7_4d7Qye1wZf-3I7mHtaDJP1ysCXkaYfDApfoivllDde-ZFjMeRBRyW4JRaOOUUf9r-GFGiWjVsSYUPJA3f2Xs8Sk1Bil16EOPo2ImGUKMr5FWWpGVElmJqKm-1Y9azsd3d6gDv7rRXAw8Y5e0AzVzRaK3SgsHWGVCd7zBqTIZwGtg-_kcl2-2q7mwQwVGx58yAP0Y6uOXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
ارزشمندترین بازیکنای دنیا تو ترانسفرمارکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101710" target="_blank">📅 23:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101709">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5766dd6b60.mp4?token=SBa1dIZsokwqItbRh_-GqZtf7YYfBr4wIHCVUHduGaY4uEotOphcvUbZg6cIegoVPzWR8gCaa46xEi_jQATUW1pr47PZ-E-pr7pFoL6G3MRZtP1yXqPU-f7cpnDZb7Rjubo8EupDMFNyBPKuflWcNOGWD07iGpo4xbl2I2ABeiPDuVamShYHQT1akuDbGFobY4HsCWIG-FPfmdGz1AJhJHzzP1CQPRMOCY7PnTTKXBGSD-4dFzTTVei1JDLczP0xo5dun2ONMqY24AxEN6e22n1v2xOlVCZDvjmgcuJkspWXeNQSjZDZplH-y4hcJ9XgJDC3voFJ7FrNsMgOjgFe7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5766dd6b60.mp4?token=SBa1dIZsokwqItbRh_-GqZtf7YYfBr4wIHCVUHduGaY4uEotOphcvUbZg6cIegoVPzWR8gCaa46xEi_jQATUW1pr47PZ-E-pr7pFoL6G3MRZtP1yXqPU-f7cpnDZb7Rjubo8EupDMFNyBPKuflWcNOGWD07iGpo4xbl2I2ABeiPDuVamShYHQT1akuDbGFobY4HsCWIG-FPfmdGz1AJhJHzzP1CQPRMOCY7PnTTKXBGSD-4dFzTTVei1JDLczP0xo5dun2ONMqY24AxEN6e22n1v2xOlVCZDvjmgcuJkspWXeNQSjZDZplH-y4hcJ9XgJDC3voFJ7FrNsMgOjgFe7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
▶️
در سال ۲۰۱۶، مرتضی احمدی، پسربچه افغان که توان خرید پیراهن مسی را نداشت، با یک کیسه پلاستیکی پیراهنی شبیه لباس ستاره آرژانتینی ساخت. تصویر او در شبکه‌های اجتماعی جهانی شد و به گوش لیونل مسی رسید. مسی تحت تأثیر داستانش، مرتضی را به قطر دعوت کرد و در آنجا با او دیدار کرد؛ لحظه‌ای که رؤیای یک کودک عاشق فوتبال را به واقعیت تبدیل کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/101709" target="_blank">📅 23:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101708">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b758c8add.mp4?token=DM-BelDlhnigO9t6UVK1Bz7ozsB72PW-OyTWN55eF2yT6OqK_611CSBqi4kUCKIv9iozJUoBCtsadHSEduz8WUQCNIQLU5jrOuedmvWBm4jpPVh-zCXLsr2Tou2ot-rMotx_7ZKtYVlgdvGXqf8vCNYW6_uCBogsbg9rm81KomuK44feAkYJwuQioIEf22bIQRpHGvttZGCX4foBOD9krl5U2bb5k3lqrh_8EyW2h8Gv2xLOOMcgTgbFZltA8d238sIBC0a7TM0wAE19UTtbF3DbKEIBv6mrbOqRLUo-WwIlWXtlfH6_FBr0o0i8diG8C9xx0cltFwMRqiKw9IBXNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b758c8add.mp4?token=DM-BelDlhnigO9t6UVK1Bz7ozsB72PW-OyTWN55eF2yT6OqK_611CSBqi4kUCKIv9iozJUoBCtsadHSEduz8WUQCNIQLU5jrOuedmvWBm4jpPVh-zCXLsr2Tou2ot-rMotx_7ZKtYVlgdvGXqf8vCNYW6_uCBogsbg9rm81KomuK44feAkYJwuQioIEf22bIQRpHGvttZGCX4foBOD9krl5U2bb5k3lqrh_8EyW2h8Gv2xLOOMcgTgbFZltA8d238sIBC0a7TM0wAE19UTtbF3DbKEIBv6mrbOqRLUo-WwIlWXtlfH6_FBr0o0i8diG8C9xx0cltFwMRqiKw9IBXNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لطفا هوش مصنوعی رو متوقف کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101708" target="_blank">📅 23:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101707">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rn_BPKQNlih_ms5gxiY-2cmZeuvnuQEY8VCfYBcCsQQlpP5sq-GcASyY6liZpV5JU_pv4tL5_DYaBmtv41JJY_2vB1mDKGKdS4SwlR9PxYxp1ervLbFHm2by8aUnRuFVSVpdsmKmYMMihVwVGFfeUoXStAfhenzgH4JB2F05RdlrdQrSphyZ-HwyRIFn5UfvYyxf7-pZFsu13aNS17ScCXhjed_taFiRHJ_FOZIKyKHw9W4lbujpKnZMRinPUNngOT4HBjCmePGZvVrgTlaZduvtlfceMPPvjSxo3_-Gpu87pWweoTfHNl5sgTyhwWJZJUA4StWAzyOJkw2yPLnI5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ال‌کلاسیکو فقط یک روز قبل از مراسم توپ طلا برگزار می‌شه :
🔵
⚪️
۳ آبان ۱۴۰۵ : بارسلونا × رئال مادرید
📝
۴ آبان ۱۴۰۵ : مراسم توپ طلا ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101707" target="_blank">📅 22:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101706">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jh00173R8gy2PEQI8PABohDChg7fGvc8Cqu4X32yPRkfX3bfipks79bInkQt6cWbJWvxNFgaJPP7I8ry3Ms9zFPZId3XG3SZ_6mcVbn8pJ1_Px0a5bqISWZps3qOSvUoEEeuaYQfO2RuauLfu-h6vO09K6iqKTka8ihDY_WmtH3_iextRU8YWLhcCGqHyTjhMH4lKm8In6eO1-Kvwvy8rFSLC4hZzbbYW1xr0jg009U9JkZMrSUhmOhQeIc4igS34Df6mWZALkSKQ4vTx7zz5iJ2g6PQTkwR2grL_LXiGfgfH4JbCneAAW6AryG63OD7i6adxuAWfdkHa_Tskf3K-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنخل دی‌ماریا درباره اینکه چرا همه بازیکنان کارلو آنچلوتی رو دوست دارن:
از نظر تاکتیکی دقیقا میدونست باید چه کاری انجام بده، اما چیزی که واقعا اون رو خاص می‌کرد، توانایی بالاش در مدیریت آدم‌ها بود. همه رو کنار هم نگه می‌داشت. هیچ‌کس از نیمکت‌نشینی ناراضی نبود، چون با همه عادلانه رفتار میکرد.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101706" target="_blank">📅 22:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101705">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X02zvWrI2si_Dwl2FQg7In_pzJH1UMxDaF5Lwi5wuHRxUJhQAs5HrMaXnerpzvZD5EcON07tYKaql7he22tU-6lpzW0M46FGK5NSRetl8aw7q8nF6mHEzCi1Jeo8pMSM5-DtXKQhHqCyBmdaiBJDG4BDtljEnZ-WvZ24TQS2yltRS_zIo7az8aRG-AiRbvYWz0LP5c0znbLl8NDi7dma1H_Pj9aJqHk2Zyq4-qwyoAR2pPa20L-W5_SocsKeRiDE4EVPqSQ6bB0XpzzoQsW4f7oBvHRdI58IlPoQRb1SZqMcU8EODvPLVFotiDY4z1hm_LUpSXTxFhglqgqZLPPJrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
به پرتغال هشدار داده شده بعد از خداحافظی رونالدو ممکنه بخش زیادی از توجه و درآمدش رو از دست بده. کارشناسان میگن فدراسیون باید از الان برای دوران بدون کریستیانو آماده بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101705" target="_blank">📅 22:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101704">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
🔵
پنجره نقل و انتقالاتی استقلال باز میشود؟
🔵
💣
همانطور که ۱۱ روز پیش اعلام کردیم، باز هم دقایقی پیش که از محسن ابراهیمی هم ( ایجنت و معرف وکیل ایتالیایی همه کاره پنجره استقلال) پرسیدیم ایشان اعلام کردند پنجره استقلال به قطع باز می‌شود.
✈️
🏆
@abitajsport</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101704" target="_blank">📅 22:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101703">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0GRtTNIFyTx33WdclxNlph7cDXA42OoER4khwL2ZUMsi7myizFdnsEca8AprTbmYF-JgxAktYxKYgL743KzPRQO1NkiEAlvsnCOgDOQPCnpqbQ44IVtPxeUFJISPOtG3eWkEORFFtruy79Q0GJoVhXAV_CVubifJfphfFl863RKxf-H1XegUPKwcRiiY5QiMG-FWU8MsYWjxMqktH-aFk9b53hbpvOxysB-q6MCttU4gQFsf8xxFLEQei-CFdugt4KdqOZQcdjJG6FHL5mrpvqp7smrIbWwMOOSAO30Y5Qcdoz68ImqvIUGjTjd0wHGMpDuxebNO8CkoQagOONz3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کیلیان امباپه هنوز شانس بردن توپ طلای ۲۰۲۶ رو داره.
نشریه اکیپ یادآوری کرده که چند بازیکن قبلا بدون کسب هیچ جام تیمی هم توپ طلا رو بردن.
✅
کریستیانو رونالدو در سال ۲۰۱۳ بدون بردن جامی با تیمش، توپ طلا رو گرفت.
🇵🇹
✅
لوئیس فیگو در سال ۲۰۰۰ هم در سالی که جام ملت‌های اروپا برگزار شد و فصل رو بدون جام تموم کرد، برنده توپ طلا شد.
🇵🇹
✅
گرد مولر در سال ۱۹۷۰ بعد از زدن ۱۰ گل در جام جهانی (مثل امباپه)، با اینکه به فینال نرسید و فصل بدون جامی داشت، توپ طلا رو برد.
🇩🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101703" target="_blank">📅 22:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101702">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtVJnVm5-Laj4WQTCpeBi65Mw7klKdYL4CHSSOAc2YWZhT114lApwYmgaGdtCBkVLbWzBJwajuy8vX-sUMtrucmLuVP1Hb-qsWELvNBSyhxo9peinfInOvUISEHcTF2WEXgtyUkSkZUvSZgQ_LQEJ0mhk6qRJ5D0Lu5-bKK0CrEuNSyu-q2286zNyHlK4hJlpPKHJ2lovniJ8-IwqIqO5jTTaSTUppi5yQdYAkDntvyfx35dfITNi6qRpVJ1LkN9GZ5QjcS1tIPdFqA0yMqLSIM9RAX-s0xcAfJ8JTCY2Gj7acWiVDgDiRlaNN2SVCkVpe39r-HViKRIkKCrUUpzkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
ترکیب منتخب جام‌جهانی از نگاه فیفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101702" target="_blank">📅 21:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101701">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_Af2FutYW2wl2KaYcFSZmZrFY4GkC9ppBadsyFdNeMTyYYZT_mshMsQ3qY0_w6qRMeNp4SmE0-dpTocDhwa_n2TYRFYCZe8xUA57BDbtYkRpntQX9_0Q_B1S_F8PGXJ55IeiPiwCdzd651RPyQOyF-Qrg4hpG4v87wHdh-neTWhor8PA17wT0mdG_xzeRPoLgAnvFC7eH_nKycvCGQlvtKv39Gn2pgMiMf0LZxiqGsBq1HOevDNBeNclIY6gCs0nADCpGkTQTgAJVDvJXNKlJIj9f9sfCYSetdBW7hYMhfjROSg5lizRfbv7aZASXxV4MdtP_oaM9vtDISG-MWQjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنخل دی‌ماریا:
رئال مادرید شبیه یک تیم ملی بود؛ چون در هر پست، یکی از بهترین بازیکنان دنیا حضور داشت. هم‌تیمی بودن با کریستیانو رونالدو، بیل، بنزما، مودریچ، کاکا، کاسیاس، سرخیو راموس و په‌په واقعاً چیزی خاص و فراموش‌نشدنی بود. هیچ‌وقت کامل متوجه نشدم که برای بزرگ‌ترین باشگاه دنیا بازی میکنم، چون فقط داشتم از فوتبال لذت میبردم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101701" target="_blank">📅 21:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101700">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfGmX6WK9CaNupbc1hM7Yepg5Xq13L5PsRWwTxUxUov4g6l3sbKPmb4vSlt-eTJy0nkmoRjdChqa_h0SO6q1hizbFRG9C_hGDwpoG438YboQeXfBPNHAHvncVsv6E7WModlTdfcoTOfafdME3gTpprhkK5YYFyjv8hWHNHbWNYxKuy77Vjy5A2c9Qdfg8r1RrsPS19VYyxsQj3WT9rSKXe-UmfueRRRKUXQPYCgBEihgBOkz1DV9sTNpPpw4L-afnpokee_-f4XAF8Yaiurflc7Snrm42pRYOjHa0br5GwSOfpN7zXGSO9e31U0sh568-fM3_TQFhyXRaiXvRrwNTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بن جیکوبز:
🔺
چلسی به احتمال زیاد قرارداد با ماکسین لاکرو مدافع تیم کریستال پالاس را با مبلغی در حدود 52 میلیون دلار نهایی خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101700" target="_blank">📅 21:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101699">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gc1D_vgkWN4uKlArvdiUj813oD0gZPKbh9SNJKyuq0iLYs5Fq14qkUY0fHFw6DUfxOU80TzgAqfbn0v3buuWdmgy-sP14ea5N2padtiEW9_sOfeI2K3CJLqYgvEc_1f96Pl8OSBpgcJIPcWAU9K6UvSklIoZ0P0MsScBJf8vF94z39abJtBvsHghEDCpPgPLFwmR1AuEfs_BbRQZRm4lHP41eozJzcMGl0FxYZ0fDvEZ_1Ozt-7r5SjAFE1C3lM-QqCLeonQgaIa_XnfBkTPdhMsWlUYyYjs1rCjk_O9vY9FnWy65dFZ_uDrP2MvRH1jxccgyasLzMJiqS08lteq4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇴
فدراسیون فوتبال نروژ قصد دارد بعد از دخالت دونالد ترامپ در ماجرای فولارین بالوگون، یک شکایت رسمی به فیفا ارائه کند. این فدراسیون نمی‌خواهد این دخالت بدون عواقب باقی بماند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101699" target="_blank">📅 21:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101698">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCvYIHWOxPOCfJ2kN2VKLrZQqN9T2XWKmOxf_n-pwTUazZGGNAiMe6HjujVZpaWgjIl9y55G8f5djbatzWkgRipcT61psYCfoXCfAbeZR7Yz5Tg7G2pbnLh2vK2Sy5EgKOk7BYT0B0ofdwSSXKIZkp2LuwFQMlPHNLIJFk4KScRGwFuQiSkEY6gF3IhNF36z68nuJC-Mye3rP0cGev9AdfKdRK9sC0nagMRjGTnq6OoYH7KtxXiMnOP0bPnagP1zaraqxPtT39nYVFN37X8EXPnKO3W1dxPWml2hFEGMmBc9V_L_Av0dIaNTWlx9bdbp1mIyFe3MxsTB0JaDQ-Iwzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
آنجلوتی پیشنهاد فدراسیون فوتبال ایتالیا برای هدایت کشورش را رد کرده و گفته که میخواد در برزیل بمونه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101698" target="_blank">📅 20:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101697">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpvEEvzgmEwaygUg4ZuSCWaIPyCZGm6rlFUTvE4-GDQ7sMlQmOmhYAHLol-0W3TQFUrxUwS0fx3i4Ts_TmUih05N9JNpmcmlidWqhYjQUyYga-IFR9nx0XugBvPizGaFneZNMW88-buXSwrvxN3lqUcEOir0kIWGiXjCt99a8nihj4F9r1nHbbihmCaIbApvvOxKsYk5m-3joM-QiBXMgxPvI6S9h4Mb6xFITYmZ4mgWThvZHUkfhKoE63wEqywRWRCcus2d-kq-elHPeEHE6wFaGC1jOSkMD6LfKadSZ7OIGqHtOzgyxbZ7Gj-_I5KID1weTL13AXykJx4lTyElUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇪🇸
لوئیس دلافوئنته بعد از قهرمانی اسپانیا در جام جهانی:
بعد از بازی، بازیکن‌هام به من گفتن: ما همه‌چی رو بردیم، در تمام رده‌ها. حالا دیگه چی مونده که ببریم؟
🚨
🔻
یادآوری:
این نسل از اسپانیا قهرمانی در یورو زیر ۱۷ سال، یورو زیر ۱۹ سال، جام ملت‌های اروپا، لیگ ملت‌ها و جام جهانی رو به دست آورده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101697" target="_blank">📅 20:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101696">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIUwqzfDWjKwfzlE6ixVjqonIsWd3_deky5SdzFW9cb4njS38i5X_g-6mptKSCvEOH6jCPrtYOE79ic-RfLS4xiGfTaqAefJnj1l16XIQiriCvvLzXVw-hQ46cbpKMieLdv1geBcXakwND6kC62vB9oxMO1uaadtdKZ7BzbheM6efBiGvjspaL69_zwhm6qBqKRJtpxOzUXBPefCa2sOWHBQ2oJ5snqus2yF2qTrUwnF5XxDtGNT9xk8iawSkLhjeQRzVSlF5RCEK72Ll2EwCUdFLgk34EIdB0YA_AXfhVBJrGS5EoDMweRz3tGHJB3GQNV_uJ7TwLz48GtsY7iSyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیمار در کنار بتموبیل و هلیکوپتر و جتش :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101696" target="_blank">📅 20:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101695">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PK3oJqiE7p-BME095F3or-3EgK5UvNLP03eHIXIhNWMimJBw1ue3aAb2_FZUrKB_1f-eJ03vgbIP2-iOGjpcX56gUJPdXHdUXAk1cV4Uv67-wcVupnJQTgzKpC7mXcKq5QEpNBPF8zkkZdw4jHiGrtI3ouUkHo_CCr9zYWlQZ1xApyfVLVdmEqLZmT8g_L_XhzjlS9-KAgC_oNGF_vxQ9QGRlIZbU9Qy5s_fuX4IxFjWOXmKHwltKWEpLrajk6uw0tyuekl9rHT_-QNila0gwRZ2aIKThmj4RfXqZP5_QAw0rbISIf0kMUMYhjkcnH-cPfugl7t_r23pJCps8QJyRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
❌
#رسمیییییی؛ باشگاه بارسلونا اعلام کرد که رباط جانبی داخلی زانو راست فرنکی‌ دی‌یونگ دچار پارگی شده و ماه‌ها شرایط بازی برای کاتالان‌ها رو نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101695" target="_blank">📅 20:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101694">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSQYrDrdwueSUY4PgwPLqY2mWEq-Fi_eTIzQA15apDUxxTrg_plObYectEvjU9sJ7O0vM4R5FUZKXhGRgbizIbz92wyQlh4o3IOrRMFxWZkh2QWmVi1TKPfEWt47YJ6OGHaoh-3FSOmSo45ZN76IqrdZDO_yF7r2kqvcV-xWrnwSzVKNFkpOams-viYkGYxVlyxNq6FnjukPIfEx-OPJJsbyUVNbDbNBOKJxQEFKvL1itv6dqQYm_ruAA2XoChKNo-I06rH5UCyRwvQf8e91k_Vo2lMBI8UYaZoC5AwZBzz9gnDj_1ZElpNQ_mgfWcS0k01WyM26uy8sBMcJx8EPdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔴
سامی مقبل خبرنگار معتبر BBC:
🔻
باشگاه آرسنال قصد داره پیشنهادی به ارزش 70 میلیون پوند برای جذب برونو گیمارش به نیوکاسل ارائه بده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101694" target="_blank">📅 20:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101693">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d00c416b26.mp4?token=CKVuMhDu7VZ64NRGcBnssWWwE65XrrRAAqedjnrQW6nAzl1Cng6fswVsTopBeobtE2lbJeIRrdiMKskkPp6c1G5IG2YZhwo0RdLy6sVFbhPMLiHtTrN_vBz6yx9b_oF6tJBv2nycoUxlu6I6cH66Pq20xByrWSHMR9aiOcFfgx2kQZmSCnkf1jNW-3M45ui-X0W8IpJ3TOX1fBRrH7eo7q1PyWOtj7Y1-4tbuNCcMjGtGWt3O-4cpABDmu7rqc4Gz1SfewfYTNntVBL2v2sqYLwZ4TEmRhiklUuCVU7DyLxPTs52F_jcFtIxZGHcozv2NnQzFX2wBIHZtk_c7bRUSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d00c416b26.mp4?token=CKVuMhDu7VZ64NRGcBnssWWwE65XrrRAAqedjnrQW6nAzl1Cng6fswVsTopBeobtE2lbJeIRrdiMKskkPp6c1G5IG2YZhwo0RdLy6sVFbhPMLiHtTrN_vBz6yx9b_oF6tJBv2nycoUxlu6I6cH66Pq20xByrWSHMR9aiOcFfgx2kQZmSCnkf1jNW-3M45ui-X0W8IpJ3TOX1fBRrH7eo7q1PyWOtj7Y1-4tbuNCcMjGtGWt3O-4cpABDmu7rqc4Gz1SfewfYTNntVBL2v2sqYLwZ4TEmRhiklUuCVU7DyLxPTs52F_jcFtIxZGHcozv2NnQzFX2wBIHZtk_c7bRUSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از اون دکتراهایی که دکتر علیرضا بیرانوند گرفته
😀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101693" target="_blank">📅 20:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101692">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dm9Q7vTIfacdpCxw1Z5qkGrl5H1bodyVJ0DEZzNRi_hXPnpW5d1OKpAdbbew6xtOwJS_-knsnMQLNeJLkAJ0MF30BOUtZ03BndFk57JjWioWwMvxnT2ar3N7TUOLHa5VBH4RjuLmx5BVuXHSK8tbYP6JzuoXw7Sz64-KyKMMrdTpasLhKW_q625PAVMFltjMJ0Pyz0D8felojb1KSs_NonFkjD4bgIfxfTvDIok97ouS3B5od1vTHVtWf2CrNvp4c2HugOnOzJkeK79PCkJXC-ZCjmCJk-PMxum7hbO53fJCepu8hGQvsW-leD7eKew9FmcPgyIoptZfxnbnDf0YgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیتی که همه رئالیا رو برد به سال 2013 و اون کیت معروف..
⚪️
😃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101692" target="_blank">📅 20:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101691">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZs2ZG12tfHX3QbF3rf0rYDMSvNZf2GMzv2fkaDZMZ_fLgRnEXkxbVvLJhUdhs-6Yh4EmMHaY7V9Y5bFCqvc06wVh3zDfKHk0UvpGMzwV6uZWXfBwNKe_xOynsMoqVZ_OSCFHQcr_Qvkc55TrW2cLzcurCR22CW3gmoovK28rCHL5VonOW6mSpqHx46ATRjzrfEqMUmmrbyECaxM5D-kqdn4Iho7NmfEbpFsPMUbqwM0a_hKDm9lF3fTgAJgAxkKfh1gZ197Kx7bww2K-qGzusZh0eROeX4RiP4bzew9sFSwRQAjGtrgMLXx1ZAigOaprXp8Ew27LEpbXAxfKtGpjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کاسمیرو درباره پیوستن به اینتر میامی:
بی‌صبرانه منتظرم به لئو مسی کمک کنم؛ بازیکنی که یکی از بزرگ‌ترین بازیکنان تاریخ فوتبال است.
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/101691" target="_blank">📅 20:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101690">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfsaoRrkzEnTol1GRtEa6OjF2O0smUHlgjiDOsGstxLrLs4JUJEpnq58EqSE-YTRADXxG7EVb-ft6HSL2K5hCPFVWrSJlwS1lwgeSB_RhY6zMrGlwb5ED491phmVp8e0ym4pm7JPIgvRFmhczThPXQwNnWMmGnmiusX6CeCwOScNtfe8Og350vLNBdaKZjWuj8sGnc5f06bxul6VJnwr2iqUEcGsvCkoJOWWH-Wz5fGETkjSifeQ7kZizra7OBFInzVTTYsWMWvLHJrppRzRWnlmgAHaT9tZ2eDHey6iSqFyjk4o9WkOt6lYvHvZoSEJ2DOvtRTahXJKYJjy7ldSbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇳
فوت‌مرتکاتو: پاتریک‌ویرا اسطوره فوتبال جهان بزودی سرمربی تیم‌ملی سنگال می‌شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101690" target="_blank">📅 20:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101689">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQMzkvg9lzxiwF25-fPXi2FPodzm7v3q3FWbRBUPPzSlrSs1F2KnH_6PxL_sU1BYJv2TnyBH3gHqKZemAj2nvzVzetKAA9UmGcnECHdyBZ8gUwj7rxHU8BQIKRwi5mcmet1RV8VDWigQGzg9MSjo2mKDt07IW5DZhPKhdca0pzyiIfBlLA_Wf8rg2reOW39I52kZJRw1OVtBmj1B8_yQK47flDiPKEOhZnCrSYOV6Vx2pGENNjv-mSnmHXKtQyAUG70LO39eEQmv1-aum2EI1mdqeO3l00oPZGkG6Lyja8HCz61LdKwR2v_hOEtIfcVkbTIZuYDtx-IWGXLrYazphw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
❌
#رسمیییییی
؛ باشگاه بارسلونا اعلام کرد که رباط جانبی داخلی زانو راست فرنکی‌ دی‌یونگ دچار پارگی شده و ماه‌ها شرایط بازی برای کاتالان‌ها رو نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/101689" target="_blank">📅 20:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101688">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZhNfkLl1bFbcxX64T8mlmwByzT1wcOQbjpX_kpN3rVSOry9qQWEdTx2cBBkXK1FeJcHMeS149uGft5hcOyX-0I_wFdJKgAjkcT3COXHN2jTZ7ybiYl4n_O8SMTl9M30UXFOHZ1U6ACeYg-aYWO4WMjfts9n8UvgqdOLdv7kG5y8Y2k8RbQNm8Irt--ehAQdgdNXMZXU3q_jU1XgvbOrqUEbmYEkx5nXrS3XijvtZq7yss_BfgXKznSTCiyQYGohfJOR35CiV1tkpPHQbBJA1fXbIuzE1kQTxqda3Qu46Sv08nLse9QXp6oFcRbIOI4_WK3dlc68_UmzX53Ppm34NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
توماس مولر در مورد ادعاهایی مبنی بر اینکه داوران به لیونل مسی در زمین امتیاز می‌دهند:
🔺
"در مرحله یک‌چهارم نهایی جام جهانی 2010، ما مقابل آرژانتین پیش بودیم و مسی دقیقاً کنار من ایستاده بود.
🔺
توپ به سمت بالا پرتاب شد و به دست من برخورد کرد. داور بلافاصله کارت زرد به من نشان داد. من مطمئنم که این فقط به این دلیل بود که مسی آنجا حضور داشت. ما 2 بر 0 جلو بودیم، بنابراین احساس می‌کردم که داور فکر می‌کرد:  بیایید کمی به مسی و آرژانتین کمک کنیم.'"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101688" target="_blank">📅 19:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101687">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
فوووری و رسمی؛ تریلر FC 27 منتشر شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/101687" target="_blank">📅 19:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101686">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hr1XdfLHnnxppBOL6-7ItsZ7RW1eTXf8SmkGFm1e2FM-tn510-mIqQSIbJZ1i1BcL1iLoLfUGRw9GM-lKBE-EzCcScxpACDVde5imi5Z4eOn9Tvb4T_wTE8M1orTXTgUxXFpz24o1hwxRbkASQjHEzMnA5CuVt0v9WbfZkmYAGFSrvkUU2EaMuuoH_BnHzw6Cf-eqbdiQbKdK4Ua8tRQG3rbTeXXkJxwXcAHiVOmzBQZAowoJEr_4IVKstRtG4Jd5L2xFx-QlncPFnpPA611WOgI_fAzwNsJt4-L-t7kuZk3o5pZZuNA0CTZ92foyez5XuDHyHd-qS41mAHni5eSJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی: الیوت اندرسون ستاره تیم‌ملی انگلیس به منچسترسیتی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/101686" target="_blank">📅 19:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101685">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vW0BagKFuIB8nCwW_N0TkpKbuV7tjnhK_tTwZIRZw5e3oxIyGma-EqykBizvfFTmlbOQFqaqULWSVtx4Caf3HR5CvivtX6NHvdex4OoFBiMzOfhmJEow1C3mV6iubpK0lYoyBKPHCu3fjR7N5RJjLKlCpn7MPfqGdOf-o4sHsZ81ointXU821HiLiRbrB_nZ_In1ZfwXsol4_XeH8-KEhRjz03_ev8DDl2hu1F1fEOL2i1yJrru-F-PoM9Xb82WTosWD7nBO9MfS9m82EFrQhdgSxRpL07bQJ4XMxrZsuLSJxEJEyG2yznrye4ivVFtG0F--4pokUICvpDIRZwf8IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
: الیوت اندرسون ستاره تیم‌ملی انگلیس به منچسترسیتی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/101685" target="_blank">📅 19:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101684">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAdSKs62lMswGxfSIYLXs6N4CV-5WsmmS3PHirxAlH7z0XAj6X6oU05WbXnWqB7Kno4XFoFxYBiE4jXOv0n8x1709N7lnes2IcrVynxVWS_hm3GUPoUAbAz32Q0GTaXy4jP5iIq-O2DddPcUXjBiRLzOQrUW24ldYxodC8ahjsoGTBwZWq_M2_ADOnAfxnq19FwWnKDHHsh_2f-2j_I9mf8YbGcYKptgKLVPAZv-8HlTKVtYY6Wsb8Zpy4b0b1SvXcW1Lxm5wz0XON6hGoUgbn3Xzt7Pjy5Bs1OyQjNCBxK6tC7OqJ9LxY8k8664ep80CznnS_N2j83AM53BqxTktQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاسمیرو رویاهای همتونو داره زندگی میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/101684" target="_blank">📅 19:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101683">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYivN-G824ceC0oxFWmTteyPDrr7i6xNng94gFrDd3wcYBKOkw6KT4Z47sKVVMLkz9WCfT1ereVZRU_R-EqseYIOTFrmKOltJejmUeQuoSyYF_4YcCA3RzxdwERv0NWcuB2AERz3YsCiKi6hN_h5kS18TNFYsptJ2GO8vc-D2BuLz_UdoBi6X0l2_nyJC7zK1UtfB7nUPcWvsbkh_p-fbUrlt-GbyGn4Pg9Gmh0Qzewgwk4SPy5rxAntZcJWvTeDYguUswrWz5hTdcaFCDPXP5IQTAJN7eHXqebLChmpN95OjYAmEO9ynnxfSDuvk251w8oOLdC444T6B7xqtyEiTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#رسمیییییی
: قرارداد لوکا مودریچ با میلان به مدت یک‌فصل دیگر تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101683" target="_blank">📅 19:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101682">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyIWlaw16-PSAMMLZopPf-kHp-f_PbuIMF2kCx2BgxvqikcxW04cxNQAqjZ8moDogSPREPR0Tt74AdTmvc4St9OoVahNa-PiL-y97O8vmY3uPR7O8jXMiK4Xt6OtFiiK5jgLxM2bjywYRH-lSc27sZj1xMr0EkVROUA2Phswtu4Y21pgsko2TvhsvcYyAdFM4pkxlXGhNJdayB7oClolTn_Onst3F4zpUHr5KJ6Ct-MZ_2tW3DgO-GlE5qWFv7IWmxDdV_Ukj4FKYuG35VBXjQKIWHoTqTKSrTBMd6TxjfFaXy5nOODq8a-GKXFmQXy27mbf8rXRUk4fqypSV2wzqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/101682" target="_blank">📅 19:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101681">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4befd2a6b8.mp4?token=gY3PcubZx33CGWzIFaADSGnN0S8MnR5sSppBO9IGxguV6bq1nNwFkuQt1PwiOaLBS3dMDEYBlDBTGOOILgERXFjjuAXdr5zN5k0wcTAm24MPfwiuUILdqISt_8pRY5vtV-wDsaxLn4W3pz741TtNjGygOdd_SY4WDcpqoAuz3PDe0EhpcPgzu01TN-yExYxD0Zj-S2tPkwh1t7ooVVbDbxzpprxdxMscT1lnouyiAqxibpGOMCabQZXYtyZXXZVdp8mD4-8u7slyxs57b5UIBW4MN7xVn3aszcrLcCPHfU6R5ghGYBM8IXOyvMi_EoCuOBfAGdxR_lGlVbQi5stUAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4befd2a6b8.mp4?token=gY3PcubZx33CGWzIFaADSGnN0S8MnR5sSppBO9IGxguV6bq1nNwFkuQt1PwiOaLBS3dMDEYBlDBTGOOILgERXFjjuAXdr5zN5k0wcTAm24MPfwiuUILdqISt_8pRY5vtV-wDsaxLn4W3pz741TtNjGygOdd_SY4WDcpqoAuz3PDe0EhpcPgzu01TN-yExYxD0Zj-S2tPkwh1t7ooVVbDbxzpprxdxMscT1lnouyiAqxibpGOMCabQZXYtyZXXZVdp8mD4-8u7slyxs57b5UIBW4MN7xVn3aszcrLcCPHfU6R5ghGYBM8IXOyvMi_EoCuOBfAGdxR_lGlVbQi5stUAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
سوال: آیا مسی بهترین بازیکن تاریخ است؟
🇮🇱
نتانیاهو: باید بگویم، در کنار پله. اما در دوران ما و در دهه‌های اخیر قطعا مسی. او چند سال پیش به اسرائیل سفر کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/101681" target="_blank">📅 19:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101680">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
فوووری ترامپ: من در حال بررسی یک حمله گسترده هستم؛ بزرگ‌تر از هر حمله‌ای که تاکنون انجام داده‌ایم. به تصمیم‌گیری نزدیک شده‌ام. ما برای انجام آن کاملاً آماده هستیم.
اگر از اسرائیل بخواهم، ظرف دو دقیقه به این عملیات ملحق خواهد شد. ایران به اندازه کافی احساس درد نکرده است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/101680" target="_blank">📅 19:20 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

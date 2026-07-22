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
<img src="https://cdn4.telesco.pe/file/poSPcI5yPdJdgU3hrGWzQ8eNlNE3zapgCh-p1KY9EzWFshZrrmk6g8xv_jMz-lhmpSyZdgVhD96EHbQiIylh6-Bwd9mBM_kB3yOweKYxrHTPobLrvL_8U-ytcw3NjalGhISMqmKXBIqv1jTAiCzuTQkO_J1nsIYUqcpCwS_yLrudASTBEtKh1kC7fW68qXIpZshIMQLuPVh-glr5Bru6M-W0_R3wK2bckl5dJVscMkdk_HhOKeFxve6XW0VkbzPAViy-a_52UxoQOBpAMwnSqqC-b79L0UOn2o6CdmcpLuPMI9F5ffHC1egyLumEt46PMdoKSbNdP-qD50Dyt8KtQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 544K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 23:41:22</div>
<hr>

<div class="tg-post" id="msg-26318">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rwu5L_IszwIcMwcL7q68HkFtctbYuSyM6ia3IyluQ98_kTuVehJlUe09z3H4UKYfAX39wcdk7tAPlPyT7ghroiHDIVkZAwa3Bmhv2T0g0E_-SKX9e6S6GsUVIVPNFz5ABpFc8dkDCZ_6OU3zoHcMj786hc49D-riW1z_QA-JDln9seULUKafU-r7YBVxoCswsYomxFqsfWNiTG6kBG-1H7P_srLsVaG0x_tQS2eNmlZpZrCpcmpQFMb4q_qWPjSUcWEWB0c1hY2OXH_EEdDn1eQOIq2qmw3B4o4xPHxriIIWG5bjNab3F0O1WTCNT5nc-Co9PPXq1fYJ7acx169WXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
#تکمیلی؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مهدی گودرزی رو 500 هزاردلار اعلام‌ کرده. این مبلغ از سوی استقلالی‌ ها پرداخت شود گودرزی 22 ساله با عقد قراردادی 4 ساله راهی استقلال میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/26318" target="_blank">📅 23:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26317">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjMdbhSYQEWjQUmy0VvoCtrSuHypGsVJ8GJjEXv-yQvAbIFV5NfDjBKkdC4CvUHwLoRPhGuibHtEluMVRuxufUZ_nd7K-MYW9nLeUSeJ-HRuKgpZFqg8ga5rT6MqZ55Vv5bI_Y6RUdbTg3FdknBa6_huii772iL9Iq5dylG7wde_BfMmWl-LhCYaOuZyb0RD-6kGsFKmvdlBedWZ9h_2RU_r8116qCgzwIkMOcQK4X0y1J2KTxzS9uvWNsuHJ8dz-l6Ic6uJgHsEMWzJxmSzj9wnGdhJV6hx5bSzQT00cT4FesVZKlsOm4fQYaUpFAQygfw1L_CYkul7r_aaM99yzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
آخرین وضعیت دو خرید جدید پرسپولیس؛ محمد رضا اخباری صبح امروز به پیمان حدادی قول داده امروزعصر یا فرداصبح برای بستن قرارداد خود راهی ساختمان‌ باشگاه شود. دانیال ایری هم دو شب پیش‌باشگاه پرسپولیس‌باهاش‌قرارداد داخلی بست و به‌محض پرداخت رضایت نامه از او رونمایی…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/persiana_Soccer/26317" target="_blank">📅 23:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26316">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqVFtM3NniFHa5J4RseXNmyMGrZo5HFKlLOIc6V17ihBOhdAg1-su2zDR7FTWR1V4T1zcnjHtkMSW_23nhnpIcWUqUWU9V0Mg9WOcMnELfX_gbNTrCDrrYmUTP6-hlpmj9-SkpHqnMZLfPNE8bK9aqPXx2_sQvEQtCPKr21FWng1cQ7GJ6bt3oxyX9O0TFd3O32dceq5-xFn26pGyXDWS462iN1FBABU0zjN8_cn-GCjePLYWVf_RUlMuaOvhBz-TiRMktIAUY6zv4S2Fn5dCywhrnHNwm_itYML_N7lsIPUlWakPSN2gIWL7EsdPNYmx2T9cMyJw8GjZyQExo4bNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق اطلاعات بدست آمده؛ قراره امشب یا نهایتا فردا سامان قدوس پاسخ نهایی خود را به آفر باشگاه پرسپولیس بدهد. مدیریت سرخ ها پیشنهاد مالی سه ساله بالایی رو به قدوس داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/26316" target="_blank">📅 22:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26315">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gH-fL3kUYiuQSKyh1HbE2Zh8ZUGlUmiPpLn6fH3TxDbCIngRwRtSJ0JOP5HbApmhV9ePRX4c-9PCwi_20A9Z5QWKWgTmdFWdG7my7wwwfCiKnF6V9_IzFOfXxW2HavCztdxHX2xxiNKytnfnq-XUezVm6kmV9eEC0yqJs7Ud_BXBBkiDfEI5BbC5qrev6CHWqav6EU4Fln8QOKykA_P5hUZyguExTv4wGCVsoZZK42K9PrmDVto-RrJAJEpsYMoPsN7-D2mG8zkoxncq6yU7_CTAxYSK4UuVJSWG5zLet8edRcEQHqVgeg5VAh_9iJSgsVcP3jHDkRfqAOcjxVYFow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
زین‌الدین‌زیدان‌سرمربی‌جدید تیم‌ملی فرانسه روز به روز بیشتر داره شبیه بهنام تشکر خودمون میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/26315" target="_blank">📅 22:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26314">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kximxwa1xSeOGT5EhPtdRmGBA8AnZ5XlycBuPLj3apMswUNnmEBVAj0cxJMYIonDL3X-iG6GfxQGUAzLM7kZJUns8TjYOEkHU0djHtVhoI7n_lyLz18abFk1flfyAODGaZB4g4p7r-yaSIgFUGM_vRt37RoFaaRx7ZiytgL_h-PWgYTRyzJ-FYFWJF-Aj1AGF4lcRMIvowzPgM3A6O4nQR2e1JsvpLSXvzhUh70zu02hOv1NKcsQQjybTgELhgflErpSnKg0kDzpv_CUsBib-LodrVTjrEk-OmRWDMWScOgJVgWzZS9iHE4vib8DjQ6NKX65N662h4HakPFnE2cGVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: سه هدف اصلی فلورنتینو پرز در این تابستون که قولشو به مورینیو داده: تمدید قرار داد وینیسیوس جونیور، عقد قرارداد با انزو فرناندز و مایکل اولیسه دو فوق ستاره چلسی و بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/26314" target="_blank">📅 22:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26313">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCDQ53dVRSVLigWPOWQioIONilyG8qyKOqzB0JikvX4OqovCjmzVk7DrhLEKo21yZpv45r_gzvl_cLUXxRAl8IUiPoVC2t0bxqLjXQ3g9zoepr-CHPAuG-BsAioQnYZtNeML3vmAOe7VoZGSPGRmQAwVJTY8kFaFSAVVTK4PKJEq2gGtkyJWXVise7Ftu9X713qtl2VrgM-oLhM2KsEhLljDsCxLyfwrii_q3v-DgmJj6H_C08JGVw2T8BNRJapg9_APcDQ8vStxjwcbO2OPaAhrWIw7jjVvMtamU8KE-VBG-rCD0t-1qJl6Dd-Uxgf6FPVd3pbFS4sXXdJtO1GQMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👍
#تکمیلی؛ تو 1500 تا فالور داری. دختر مورد علاقه‌ات باهاته. 5 سال روباهاش گذروندی. اما ستاره فوتبال کشورت با 50 میلیون‌فالور، یهو دوس دخترتو میخواد. دختره تو رو درعرض 2 هفته به خاطر لامین یامال ول میکنه. حالا در کنار یامال جام جهانی برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/26313" target="_blank">📅 22:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26312">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plEyJ4c3D_tK9Xst36asfQ1kkjS2ydDTgo68ed8d06Pg99POE0mOko03hzNdVKC2settf9OCE64jQqtIk8SooNchm8gU1khGU-XYr7uxiMVJzKXX-1EmlyhYCz3tOPQMG5M3AVgKbGfS1Njz6dtpkIMiKuL4Nay4Hg9kkzIBpx3sjEu8Uj0cxNtlsZBI8pufB-RKaYsuisw7C6WMgnifrSKHcGumwIyXjg865W-iIpkBCxxHcemjyFLE_VNTc1Txr2LVIu7HFwzuYU7sp92D1WAcXp4eKt5wRTm5fC91OsziDLhgrvOkilcK1KnXT4WCUF4evKSgsOEfXhJ8gu93pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فابریتزیو رومانو خبر داد:
کریسنسیو سامرویل، مهاجم 24 ساله و هلندی تیم وستهم با قراردادی به ارزش 55+10 میلیون پوند به الهلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/26312" target="_blank">📅 21:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26311">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xuzg5Un35W2yUu9F6gQcKtq-6u2Ed6s1WjeP_Z9PkIImX9A2f5rRk8blZvgFT8jNTKGcfACuIfaNLkGw5dNYxf_w27E41Kfz7avMO9IY_dVLg3Bftjmm25ij4K686u0OCvJ-udRHM9DHNyonTbPR2KncLXETYLmNMCK9l6SYTfC8SjpnYwHIVqVKKTJ6bKpO_R54-6Ao1pDlW-0UVpOR5QNcMSuqEGt9eeE4LQzfbqtVqU2BuVRLYmYvdPLjrxPytvsMB5SvhcoXqL5SYjO8-xqctmnyqvXCUgbxloOajxZidnSjrhWT_EvsOvFVtaGvQPuFY9uwcrUVNHGVPjQ2tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد خلیفه امروز عصر با حضور در ساختمان باشگاه استقلال عکس‌های‌رونمایی رو گرفت و بخش رسانه‌ای باشگاه استقلال پوسترش رو آماده کرده و فردا در کانال و پیج باشگاه منتشر خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/26311" target="_blank">📅 21:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26310">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQ0HJqAh26asGcJZtmV9ucW08X73JdSHIZIsMiOACeqjBtfQV0s6fr_sVNSQANf2Mk1vOODnrfZMLP2jxOmmEtWskNPpsJVvWozhYW3ZKfKHDnL_3bzo5Ug5518eP9jm8gF96GW41dvEuG3N43Z2tnFh3GvIM1cBSyXWq_7ffFmX70zpWs2CJpTsHDZ5yitJGCpv5En2h9m79XtnOQlDIT6SrmRrBjnLxmUDSB0fvwuL7qf7bEEF1VBdvOhReWUQFVwIEEh_vVOuExDfrc4YzciI9x7LC56AhMhvZ-bpF80T9U4udlUv28378PWCYiJCnUZ_bG_Q3LSaUDUm4SLf3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول و نتایج رقابت‌های لیگ آزادگان در پایان هفته سی‌وسوم؛ صنعت‌نفت بازی پایانی مقابل نیرو زمینی رو ببره‌میره‌پلی‌آف اما اگه تبره و سایپا بتونه پالایش نفت روببره سایپا میره‌پلی‌اف. اون سر بازی پلی آف شاگردان مجتبی جباری در مس رفسنجان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/26310" target="_blank">📅 21:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26309">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u52p_3XRjDB66XHHcd3eXrPxCsAO_1p7_ZKI7xv3NvEtdSASDAqkjsC2pBB6nxZGQ9ZdNh25WO7QCwSIxbBrp5w_o01kz8FZ5LZkEuwWwkDTBwnARJRRe2qq4JChcNFDjyUWW0s2M9TqyIJ9RNrQ-OltY8ZX2dsJkqEeG1h45SaBsRGm5NYXcMnCqixUPSbeQGYfR0SlVMoUO8XvDylSamyWOq6-xd7RXhxm9R_yL6VJGeFOnTSP0vOdU3AF550NsMKW3XakkuPy3XbJ3YU8KPWdC01soY9m7hCpz01EVX-oE18tA3yYA32CX6C2dbbC57EoQNRLpzyFtH5I6zVUNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛درباره کسری طاهری ازمدیریت باشگاه پرسپولیس پرسیدیم که گفتن امشب یا فردا استعلام فیفا به باشگاه ارسال میشه. اگه منعی وجود نداشته باشه طاهری فردا شب با حضور در ساحتمان باشگاه قراردادش رو چهارساله با پرسپولیس امضا میکنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/26309" target="_blank">📅 20:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26308">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a142133503.mp4?token=jX6v9fGnE1w9T-mO-xMpLax8dq07_tmR_8h1klGe4f0qRRiF8Y2DIroN5zvpQMqN-C0LsOVcq4nuvPcB_SK78hwReO7JM6m2MbDaGdmNzLWyD-2alQzr0cjhrKFGN_0Nn--yKXAW81BqNe_bJP2KgCNODWnTJ5A1_Q2pfeWnN-v5K-8bq1ni8yveo8dA__zERCcrFR45VYtsr4yFKATW-LbXMO7Nm-mecZ-N4TvBHnpb88HTlJ23bfMLyioZZRqtmoPRIPpO25zJqyj5jcNCZaZnX_2rNn8ckp3SpophYT2EhtNOATrDUxKj8r51pjBFrChAsg9uJ9HorLQXB5iljQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a142133503.mp4?token=jX6v9fGnE1w9T-mO-xMpLax8dq07_tmR_8h1klGe4f0qRRiF8Y2DIroN5zvpQMqN-C0LsOVcq4nuvPcB_SK78hwReO7JM6m2MbDaGdmNzLWyD-2alQzr0cjhrKFGN_0Nn--yKXAW81BqNe_bJP2KgCNODWnTJ5A1_Q2pfeWnN-v5K-8bq1ni8yveo8dA__zERCcrFR45VYtsr4yFKATW-LbXMO7Nm-mecZ-N4TvBHnpb88HTlJ23bfMLyioZZRqtmoPRIPpO25zJqyj5jcNCZaZnX_2rNn8ckp3SpophYT2EhtNOATrDUxKj8r51pjBFrChAsg9uJ9HorLQXB5iljQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پاسخ متفاوت و معنادار پیمان یوسفی به سوالی درباره گزارش نکردن بازی های جام جهانی این دوره
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/26308" target="_blank">📅 20:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26307">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a6a22a0f.mp4?token=adP7pPJc-vXZiBZiGtPskDGPfCxyNWMbFnwAU42R0sEd3B7bwc6jgOiqE4buP1JzmtKd6ly31njubTohgsYKxu4NvyLHwcgds1Yg1CUtt6B5g65g2WFH2fnR2R7tBeSjC2gY2pEKDnP867t0OkO7yqaivZsq704mqUAyI4e3E1nO2cyaJZhpjt20WHlw0FWBIzZBxdVSYG2wytazvRST4Qmn-sDqoVXf4wQSRIZFzlRFy67Fy6zwTNhtAzmSPExw5BgBHF-YSGXEUI1qlcWKK16EOjTOotqt6sKJHfPbY0RZIwTkvLY7nW0ER0Y3kEbDZYj-h2qyAMeBu3H5ybyqog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a6a22a0f.mp4?token=adP7pPJc-vXZiBZiGtPskDGPfCxyNWMbFnwAU42R0sEd3B7bwc6jgOiqE4buP1JzmtKd6ly31njubTohgsYKxu4NvyLHwcgds1Yg1CUtt6B5g65g2WFH2fnR2R7tBeSjC2gY2pEKDnP867t0OkO7yqaivZsq704mqUAyI4e3E1nO2cyaJZhpjt20WHlw0FWBIzZBxdVSYG2wytazvRST4Qmn-sDqoVXf4wQSRIZFzlRFy67Fy6zwTNhtAzmSPExw5BgBHF-YSGXEUI1qlcWKK16EOjTOotqt6sKJHfPbY0RZIwTkvLY7nW0ER0Y3kEbDZYj-h2qyAMeBu3H5ybyqog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
بادستورمسعود پزشکیان؛ مشکل پلتفرم و سایت عادل فردوسی پور در حال برطرف شدنه و عادل پر قدرت تر از قبل برنامه اش رو ادامه میده. مصاحبه مسعود پزشکیان رو تو کانال دوم گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/26307" target="_blank">📅 20:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26306">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1W6pJlD1zYMdlHA3BL78qOA08yY2Qj4oJvjkI1JzjmxkZV_ceS2qvc8e45HlU097LMMMOBOjEzZsGITbF48vLHPNrDx6E9wfcmrUcQus2K5MiAU4RDsLMmC2ejZIpEnWD3ET2Nn8oP-20rNTSsOQ7MN7UQ9qsKB4TvD_OFFo6QSA34Mm7LqXNW1UYsRu6gHR4R-ZAjcoGUtRbdeSGgalJpwQXx-e0dUUMgf4ksUOshhc0DwW8Rj0BGpP1VIY-o6JX5l0LJ7b9FTQHIjTRoDOQWy07dPaPkL2x6DAp0QWU6BF-HE_XHQnPyWshqIPaZL3eK968xPfZdRjj8EQ_PPwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇧🇷
رسمی شد؛ کاسمیرو ستاره برزیلی سابق دو باشگاه رئال‌مارید و منچستریونایتد با عقد قراردادی دوساله به اینترمیامی پیوست و هم‌تیمی مسی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/26306" target="_blank">📅 19:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26305">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDp-387yjF39QLIM8YF3Gk9ELwtzT4_4_6B-h8-qbngUZ2fBgrQE3DAGsVxHI6oXG-A06kAD5tUcoL68owOc2otqB5LCsW9SLqvFN05AzZRPlPjiV6QTj4jPE1rta93hrZI7sD7noXFOuBKA4VOIAF2OyPxwr4N9oYY67rqjUUM4wzh_OkRFlNy-a3UmkK6H3vdPJ1DPLuSTqv7_aESMFyRNpBWN7hgQdVpPhnzWmI16lJdDz7tGMiDjVEy02ncjes_-sceYyTGZW1on9h_Sr6YJ8TY2qkBTz_xsiMCfHU3xLzSan0jMac9vzYfgDGmPPOUVxTy_8dnUSt9tHvr5NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های اسپانیایی: دوست‌ دختر یامال رابطه 5 ساله خودش رو با دوست‌ پسر سابقش به خاطر یه درخواست مسافرت از طرف یامال تموم کرد. گویا قرار بوده ازدواج هم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/26305" target="_blank">📅 19:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26304">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoVDrE2BZcH5fTLEdGoGuK1NkMf5CSSYE0Dw_w67gE1WdzZVeLSMWiPWepAfSIr6CNUsiMDQf19i7cQ9_ObLEGnpO4rLK5NEq6DJS8msQAyAv7cia03V5xjEszX3nE_l2Re66vO1CRGxiTC5_GA6BStNBJGxQVR6vf7i03eceBhSTaTrlDqDXinMnCmXQZh-Y7hdpCLAP0EnnmOYjElwUc4ueWAAzu4dlI3LXNa0wm0eR0QjdWO7J8al8KvWFz_SqGd4m_P3q71RZE48-er-zY62_lHvFd8nrUTC5MYMToqBodijIsAqViacHLKbEpU9pwwJNRzCPPG8xJWADIdgBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب جام جهانی 2026 از نگاه فیفا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/26304" target="_blank">📅 19:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26303">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgPedxORJXwDG9JfYk7d-GB75b8JOe9BwA0JX-lw-t6gjp_eZ_tJQoGHDq3USBi79JzDBI5-MweLEonR7WJyAKyiDK3tDT_3_xE8E4_KG4jhpfJWeaFQ84eZJAtyWvNZUcdWyHohgipMlN1V59zxVgz70gYLEh4w7PODBjQGr00h63WJj1CtaE2ZtiEaUOEY6gbDE21tUCsi379ggO3V3f1pQavWAIykre7PXg21AoM60B5hEJ7E3enK5yfIsXcr8BEAYE_xepQGfm-xC4UKx35T8-diB0xY79ji4TrI2jPDeOi3mDhsUwxzPztXVxju4V7gK2therWAjFspnTF4Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/26303" target="_blank">📅 19:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26302">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMXFxXOvcoWSARqD8t6JkM4YxYM5Yq2eBYz89Bc_Hk9iB-i-RWLeuKoOjjMwfyr4pRDyAyv_hSggP8hR_iLOuBSa2T-BNH4QYxI0PdEZjkopRGpDy5o_rbci4WtZlCIQyeag6CQ0vUfgS3UIYdc8vVvRuobF9G7p_WQEEd790-J5Xv4M-ePdKZuRRP06RyYVZ7-2_dH9zxIw72kL10vB4AyCAfoFZFc6Qz0zKmB1SkYHnjALd9sdKEH8pigHyW9r__jGhjJY4-1UVbxK2ZvYVDBDigGw2WrKADiWAaCaKaDl231lCZuaThNF_OCeRcJoLIXjt6QlrpFkM9voGkNA9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: کدوم‌پلشتی‌خایه‌اینو داشته سایت داداشم عادل فردوسی رو ببنده؟ ناموسا من در جریان نبودم و امروز صبح دستور دادم سایت عادل رو باز کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/26302" target="_blank">📅 19:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26301">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_pV1ROFZ2gQ220_2ya6NYHWwuqYT5T_TXsplIjniRPDopBiewOyssEA2KRvfOYO_mhwAgB2bLFQbqSZO9rxC502So23jk97JUMiTrtY3Eocnsa-dR0vLtQEMOigVVVzEL7DpoAqSNIjqeSfZUi1pOXyGLo-yWCHVM-IwuIFcnitc2WzSaXOcHVKkh-aFh1YIIdMDj7NQ05X0yWFF1ghQUOfSCHFRrLOtZb_KwKF_K_4ogsCfxzXXLIAVPKtCvFR5dTfIMLQ5amcSZxqxnGLuh-Czu6ZdyJp4rCVD9U_dD7bHuAYA_0-c_9dMxsDOfMj1qlc8TTKDIUr37YXiC9xjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌استقلال بجای محمدرضا آزادی خواستارجذب حجت احمدی مهاجم‌تکنیکی 22 ساله سابق استقلال خوزستان و پیکان شده. درصورتی که باشگاه با این بازیکن قرارداد ببندد و پنجره باز شود محمدرضا آزادی از باشگاه استقلال…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/26301" target="_blank">📅 18:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26300">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tx9LXdV1H2SKcYt-WsvjNAOwgnaIVozCBFIZDSOHc918-g9sRfXsCnOG5eKpeXlJ8MP50OCpuoIGEy_IWXLcl_vh0NQxGLC0VR4192fLAZCKthgZPoVTTyPE6Y1oJOoRnGvs1gtE3tsNg4tEiR2w7aRGkFKQlOrFeHB2BcderLEnaWuQhUl8-XL98x-F2yOOXgfZ5aODfpTId2pCLcvoqxLHDIZ3tFIFEL1k2TL2UdggokekCH40vgkRd3JLOKN-xq-yqaYu9OwiKMLr3I4Zow88bhhOoAj_gGA6emrqZxWt8RpbiL1MRK83aE0DNCB7UTw2LxkJkWtzfL1vCu9aYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمال کامیابی نیا هافبک‌سابق تیم پرسپولیس در 37 سالگی از دنیای فوتبال خداحافظی کرد. کامیابی نیا قصد داشت باپیراهن پرسپولیس از دنیای فوتبال خداحافظی کنه اما باندکاپیتان سابق که خودش این پنجره مازاد شد باعث که کمال کامیابی نیا در اوج فوتبالش از باشگاه پرسپولیس کنار گذاشته بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/26300" target="_blank">📅 18:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26299">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQ1rHbkMoBOmHlPgc_lt-JrSLNZECPCIftHu18-DyybZ0uWGb1N-g5Jv2vp18Jj6UQXP38GRK5fYV8u-lNlHkgasyw9i408yUAiIfCsdBEsdLs55DCHZibxdbHiXNgnHfImeihYth5EEaUicAHIg5vyPSbAeIrfGPa_5GNTFEt6ZFuSBDRvf-gm2pZHrgNJQ1iFPb-GhBZ9lExNYklMjsY6eLIPwfuKtimzpnfRLcTU-AayGF9l4qHMc8dCIQXNRoceWGC9A4KkOzH9bkt5NWgcvZBvtMon2PYkRR0sJ_owJYZOzhNx6UE-CGx9rI3_-odELKJohzsLDqvfbYBfZ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ فیفا ظرف72ساعت آینده استعلام باشگاه‌پرسپولیس‌ونساجی رومیدهد. اگه پاسخ مثبت باشه کسری طاهری بزودی با عقدقراردادی چهار ساله رسما به عضویت باشگاه پرسپولیس درخواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/26299" target="_blank">📅 17:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26298">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OemgJYU3j0XvuRE6JrISGeYLvj99pf8sOMMWJh7VFxxdw9Lf6dqQhL-1PtWv6LPqYdrvdDTOoiY1xCIf60V44PaTioIrLPCpD3KVQuUOvYBuwOUFofqjixsXX00w2nqGr0_BhPGNOu6OLoe5hqnvv2pfMclt3I19lj9InBP8fRM43v68SYEmvH7lKsOJCXm6596BeljD5sF9N5_98mYopXsEy4Bri5LoZpo7VQejrpPshZWqx9JydWOzPnArqg3URX_YXDzxt28l6NX1FVDoYOxstDPsfDb_x4ldALc-AhTHtV0UUvtIHl51WsWKoagLVEsh7fRyfvG1ovWOcp7wSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/26298" target="_blank">📅 16:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26297">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1Lx0u1mLBx76hVLN1jM0V0n-6U0J5H5JG2MzkKlGXwRxZZJM_5naeoJdNoLc2E83RoCteNBq38maEMxHoU0K1wNCoCJ9urYUo4dcBfch-OfzUUilPDU6t__cDTRLF8Q0N15dM7i5PDG6HDNm1adHKgtsQyfwp9lQLzrife77SVwTlJ9vaYYRJY7-BqyIlObuckenffcq-1xkfFxBe8Ons-YwUaWwGIRVx3QcIQAQDa8p2FKTuKurxFFx1AeOICQNIZU4RzJeh_oQ12XDNShGbYCM3IwvDul7pIQVVI-QwHKmh5qC-ylZqRx1G1ALTFL6GndfwWpI3qrJsUGQ2LbnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط 7 بازیکن در تاریخ موفق به کسب قهرمانی درجام‌جهانی، توپ طلا و لیگ قهرمانان اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/26297" target="_blank">📅 15:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26296">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUjuyaV4yXw6UFmpuUkZtGOEUB3prV_gqndkMXM5U3Pe-GzNC1eLJIrBWb9gbeWO7Oshvn5bLQBmldPDR5nB3csXniBvQhJkjq0jyhHQlwC9L1xcWnb9Hma0UR0yp18sOS67oOPqBhLJ3Fikeurx5FyuvM49cDN91dICgZ9fabcpv3wjFEg7BzAqvxRdcstV_ugzSUFo4NVP-jLKjF6rJak6mtaVj8tsV02qbziNTiD-1bMeqXv4zpLK_Viqk9BJeU-5nDKSgs9Bvs3kME-ZZbGeo207EsX1QtQnfGjNfdtOh6SrRI_GOAxIDcHEMaNzAUEp5-kDMVIKfMwUTKmEew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#نقل‌انتقالات
؛رضا جعفری وینگرچپ‌سابق ملوان وگل‌گهر با عقد قراردادی دو ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/26296" target="_blank">📅 15:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26295">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwvOzMokkoLYNAotFP2S7_AZBkYVoZs1bDiDefzSnC9FwEiEt71aCSvEbrt0fmYM9RY8veF5kbm3NJkj8CqDKOYVPlHteuoDhrMzi2VVNWYIo92QLQ71dRd_7nQBoAyrZMIwg_RfIVB5pvmcyJTMhb5zN7shGS1XUR-cdf18pRABzmrc2RJd2AHdD2ynDwSqcghpsxvSlPHc810-hwm8IaqrIZN4ML8kubFtX3UqaseiIgkGlObpR0agkOUcgwSnnUgtW6VbrV-NH9du5twx53PqLkY481C0cjG1FU3lgLlhOEW-D0FJaFjxWMI5aU6pZVo60TL0jrmlvB_mlY1MIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رسانه‌ های عربستانی مدعی شدند؛ باشگاه الهلال پیشنهاد مالی بسیار سنگینی رو به فیل فودن ستاره26ساله باشگاه منچسترسیتی داده‌اند و قصد دارند این فوق ستاره انگلیسی رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/26295" target="_blank">📅 15:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26294">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvEr5QPWrew8lrEJpc95xgK-9DryBZmMVF0EIXwETBLudX5Oeztl3qTZlZcdl8jqYNQe2RVAsyVzS6DGPXQ5qD3jJF4OKaJDrKevZqlTDQyfSCeHD4eaMON_e-jsxq_wXvpPQe3TolTXp6u1LVrvvnGTAfa34bP13CsMo_4hReALLALTvfDm9Dl36AKtF5PlA-C5h52XBXnWM_4YoQhIm-r6x2x5f6LJAjl5AjrTzK4i86cykM9tW5fLByY4xMYQKPLI2nt3FaJuvbA6wBzWpyBaTtcoyaUX9auvrUjAxCj4n-v1Tbm-NUJBuY8jA0SKxZdkST-SB45IPzweVdk7Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اگر اتفاق عجیبی رخ ندهد؛ باشگاه پرسپولیس ظرف 24 ساعت آینده از محمدرضا اخباری و دانیال ایری دو خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/26294" target="_blank">📅 15:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26293">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olteHfHhY6FAGPyNwYPVpjyNozzi1-b3pQhxs0CNhfKf95ngvEx7XDfWulWNJz9GPEYUDRZN9ogw-xZkhNCXIYVWOY2ckts0SlonmYlBoKa85ajFlEgbrspQ4bI6MYPpdLXxqTA2aSFnNoAjTRFhXaF1tAmOkdKyWesraXweIV5dhEDE-HwKgaROIDUYHtL2mCpmrlvzz2ehGJta0PVpuzePRfxBOe37fV_PZl1yVwYRM48NwuMlt75eBl1EqX6RQ8pcMj-QZrIADsPvWpL1k8If4tzRV5-atp_Ap-1Y73_Ie5h25ygNiGnXsUPOTplelVnJou-Sdz7afHBrr7nLvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌قوانین‌فیفا؛ درصورتیکه پنجره استقلال باز نشود این تیم درپایان نقل و انتقالات نمیتواند سه بازیکن آزاد جذب کند و تا نیم فصل حق عقدقرارداد در سازمان‌لیگ‌رو نخواهدداشت. این‌درحالیه‌که رئیس هیات‌مدیره آبی ها امروز عصر گفته بود که حتی اگه پنجره باز نشود ما…</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/26293" target="_blank">📅 15:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26291">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D0F2hCZWzazsyCu-F5KGXkjlmCkR6NOvd9fO8f-rQqTBLWqjYBnroHbqDbteYu0b_2gtmu7UIXHzW502-UBj9PhDehMa542M8rbaZNLbMa4_HLtZPheOCe6FWkeyYV6WdBY4CX71KRATXkths2jXAIMnMo_zj2FdToctS3FGQWaChQwBU_tuTKDysjcPsw-1WEbzwayt3xycCZG0_YWto0NQ_FVFw_vwg-1kEqvapi9KfDVb37lnqVDxOO5zPABggnZACAyq8Jhh7iBvCSZroWWGBBxJ6z5W7cgGo9DgqOVYx5k4lJbD7KgN6GIJQs8GZ7dUPH36eaBw-TnsZPHXzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4PgX-FlcV-_-wihCwlTbrQ5IrHNrA6VsDg8HNH123FdXmhrffNXINdXKzwYEob-oBdk7w34p5xPySSfQzYirOjVMEoqJl-QXF7I2Zxam69wkX0kbmj984FlnMcSz2UJIaAUi3B9xIk1yij7JrmUunE95H1bcX5hwR5aI1xtFZ9tDB2f9A1sMeQh9QyfnDqGBMpjqJS3xPFVzTTxX7zrzEUQrJeVxEXWp_bJQhONbVaIBTlnaWz7EfeU5LaI5-K0_Bok8CZ8bnWwATtJ-Sxva8ecbfG-ps4hucPZk-zSG5oINd4m8H0Sg5nS5jM12lUyBnwo7zXX4v3SN0x6uN7nBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇪🇸
ملکه‌های‌آینده اسپانیا فعلا دارند با کاپ جام چهانی که بروبچ تیم ملی این کشور گرفتن عشق و حال میکنن هرجامیرن‌اونم با خودشون میبرن و چند شات یادگاری باهاش میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/26291" target="_blank">📅 15:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26290">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gy2-tY8LzaIU7AwiORYqmPh8Wy0bYwdD_6GWhDMgT-8m1oa-QhyvFHTf5ZBrl7DQZ_SnQJk19pySOE-DINIHtxkTZ-EqoDjxoMEoTxmCiMxDavflu-1STKMCsCvsWnMVKncWx9Bm4lGpJ-6q6Ufgit7hikbvP58WSS444LI-VF0wMQzIOYws6b0dZP3QdFBqfMOAES8ip4Hcr-oS1SHp-In2pznaRviNgi-Nbt8rlWExlFN3CtcR45fIyjB5tRO_0zYOysz6Z70kGQXLQUPpgDF2wtw7yF_Ek3FE7PEdnt8L7_fLJzxD9TWsUjEMRZTkNFB6qJcK3hrnA7fCYhWygQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
خریدهای لیگ‌برتری پرسپولیس تا به امروز: مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/26290" target="_blank">📅 14:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26289">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKqFDAKniYAtGC5HhYFlo8SqWZFsdT8PvEpjD2w9sEf82o0hcc9zGXtFuZIASHO-69PRyvISzz9iyfwpkKqPboKkfTnADCZq-pTCzzW8oXZgQq69I5k1Gy2mZZX_c7781u0vlSXLzU5EzxWT79XEnd7CNxtfIXd2trElQXCB49TGphWw3eDFyh-uSLdC8MvHvRdAGOh17Kl0THrQ-veIwEqFE6aeNMaRJ5lZRIL3qfmFJ7wzDZ3yhdyS1S_TCl8eRevoUfTiAVEfolNW1FLljPyXQdBw2Ogy-WExtUmivEcleWDtTIiqJMDyfTMflU5_iNoPyxhbvyNFAbGtmSHItg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیمایی‌که تو جام‌های‌جهانی اخیر تو جریان بازی نباختن؛ ایران 2026 و نیوزلند 2010 با 3 مساوی از جام جهانی حذف شدند و شکست رو چپشیدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26289" target="_blank">📅 14:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26288">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KiPG8U9e8N2vJtvDdbgndUG6EQaR-lBiT-cllWuH09CX_rAOI3C75KP66xvHf4dwBEHBUqYm0Ylg1-j0QJnaF3QT3kQikB9otqKaIzRZXtpHCiMuYQEYk5eSDs5JieJ7popBggiXqR4nehBzR2MnGP0bKLz4dU6eUwnCzsmI8RR8CPxxbuI_giH4SBAg9yINswuef6p__cQyTdt-RwTo5ydmcv_K37qYjC40t66U9xW2PpfPz_KYMHj2nSabVOgNLQhe2uybLKGgkAUsUfMLO3yXiTGU78gs8VklRa6WsmkZr6ILN4_4OM1BqDiIdrXBVZbyJTh04QFAhVGi7GQloQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط 7 بازیکن در تاریخ موفق به کسب قهرمانی درجام‌جهانی، توپ طلا و لیگ قهرمانان اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26288" target="_blank">📅 13:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26287">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eT77gQuzeTLN56X5pdBpJw10ZzRu4kKByKWBiojAbBdIFLiOJMCSGeYki18JCAWreFgEMOhSavXNcEV9AvFuUgs7Ws1CUkLN2ufUBwmLs0wEoJKvdb6-C5gLUHAeWCc26zE5rA98aCxrGlOFf3Evs5G6LdP5nyt_6IFWHTX7gnrDe8X5mJZs-zRobzbPGPFGiCMKoFgyzwU72Am_S4V610AfeJaycvUPAsemL_QJF9LHv4FfeezVDk1bLydtPPp_c26wk8WUYYJ0p7BA3eLFJxFgl_Qtbj8a7KVQyT4_emDj2rJ31aaKAS4tUv1zuyV2_qIYviDxV-VDGtwWWVQuBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ بعد از رفتن محمود بابایی و مجتبی‌فریدونی؛ بزودی علی نظری جویباری نیز از هیات‌مدیره‌باشگاه استقلال برکنار خواهد شد.
❌
علی فتح الله‌زاده یکی از گزینه های علی تاجرنیا برای مدیر عاملی تیم استقلال بشمار می آید. تاجرنیا نیم نگاهی به حل کردن مشکل…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26287" target="_blank">📅 13:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26286">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_mEq1vqWJDq_5P5rL7WKYIqL4eEb29_AgAyqmahjJhEh9OF0fgKtCApQ6L43KyqxjiiWhrKL6fEJwh8JtzNqS6Y3dVHpa6v6lsXR32AQ-Cn519CBOoRDoWlSfrkLrJ13G298cCArBMtd6VLnbuU5w3XReqWkavLsYYIgyfhj7MsAcUZTm4Rvu9MNhw5d1BgzRZX9aLdeiYej0TBkXMT3jwR3RhSKXKuL8-NmQrMZ4mK3eIaQQBI0HbUTysZoassAMOBuRingouziY6QEHtj8mSwf7oNydC7GdCk8Q37PX9JMHXsI2VZr6OhFFgbC479t-TchuZ9bcG75oJmHqOaKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
رسانه‌های‌آرژانتینی
: لئو مسی بعدِشکست مقابل اسپانیا در فینال جام‌جهانی به هم‌تیمی‌های آرژانتینی خود در رختکن گفت که این آخرین بازی او برای تیم ملی بود. و شاید پایان دوران یک اسطوره در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26286" target="_blank">📅 13:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26285">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCJ7aZ1iHSqAzpXx92OWTd5attlf7FbOYuHgtAo0z6X_j4u5CjcNO03DAYsU8t59zLHpgIPU8dB-uhf2OymT0-XT0hgC8tDSKimynQFPSB3q6yoS01uJGR7qS9Z10i85kauIUmcH656B2wb9BQbfbxcA6zKwL2OUPdtnpnlkO4EttvQ6W3Xm-Oj3i3L0YD5OwHHN9siNDplqz3oBkoBIKPIFkVTa4W1pq2RsZKTCtP5sBV8IiG4-YPhmue8RYu4WPUcNNho2yihVxMFGJYbw-sagNedSlqgmBOIGSheSE0fM8y8HrbX1AAQFgFz4IEnG_mMlWdJJzOVkcKoJO4DOkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسپید، یوتیوبر معروف که بشدت فن کریس رونالدو هست‌ شب‌گذشته حین اجرا در اختتامیه جام جهانی مقابل‌چشم‌ میلیاردها بیننده رو کُتش "فروهر" نماد ایران باستان و آیین زرتشتی داشت و به شدت مورد استقبال ایرانی‌ ها قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26285" target="_blank">📅 12:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26284">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDtsH3C5EN8Cj0I6fLuj5fdysxR1wwRicqc01GPGV5Rhc_W2GvS4b92nlABCUDsq_hs9Tg_5CT_3jtaAHqdADqnuPwN0jUWd94wDLGPCZECBz6CU_UQ3KtU5wGsXtbEAbrlPM7aF-n8GEYtkarCKASo78f5aX1_1NYlbosEXQwjIaL3SrnuxBMl41CA4K82wX1c3uFjgXebX3oYUquhs5zWKLjm_hj2qkVXEfft32oegF-Y2S9nuSiCO-LHf_h2DQdlxgAGxizDHboINQGP49Dq7KN4PU0FzhGvZwmofbAF1Sa1aUsIy4HX-NVp_36mnEbbBGSwoClQuPZq-NjQcBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
با اعلام باشگاه منچستریونایتد آندری سانتوس هافبک برزیلی سابق چلسی با قراردادی پنج ساله تا 2031 به جمع شاگردان مایکل کریک ملحق شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26284" target="_blank">📅 11:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26283">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIMOQgb-xoP1x01zB2niuU3dEc7xnLE4B_jrCPitOeD0l8KdKKhgNJXtilYnQN4iSLAOU2z6fSSCT3MHiBIbbCmxwgAMpqjk-WDmTkD9HxwCv17NY6Q2BtD6ZC3x3rQz_-yVp1ex9yy2XgLoFBxSZBZW_tkiSREZjjDq33YbhZPpZL_NK3_NHWpY0mb7Bmi9oizQpFAI0e7mEKESH_bJIhZvg0Fsof8QzNfJHQkKS15Yea5LPwab384QdH-Bw-MfQ97HZgiFQjg5RJ2QB7O8l5vryuCEsc1WoqbOHRwk-KnvVVt3cICdM2Ch1K_0gWxYcLugAP5f3ydrAwJqW6QqBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پوستر رسمی باشگاه چلسی برای مورگان راجرز فوق‌ستاره‌ انگلیسی‌جدیدخود؛ چلسی برای این انتقال 137 میلیون‌یورو به باشگاه آستون‌ویلا پرداخت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/26283" target="_blank">📅 11:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26282">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWA_uaRT4XznNO9q5d37Lj0JxfRAUa_kJNG0QEo9IT182KvFOKHwnLzL23iZB4AyjiSWzgSFxYPc18psRfMG4fL0UX1l43YlIwlpniuIhkGRIyc6VqybjDs8-ksSpEwYIsF3DK0fQKVKoIjC4L2xyVyGAHyvwbx9t36isg5mr5AEXINI5LziKUQQ8NykVoySi7etKg1dsAa0ZlhYMMIU3Di-aWFzzTS0AyNLDGPlZYt0TBnjxfK7JyvrGA6yTJGTfBXo4aq40BAfvnA39_0X0SnqXpbYtCyIGVsccKpW4R5K6qT2g7Uuro1dwQI0fcwdoWSfzNlPITX9Cw9RREoD6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب‌کهکشانی‌وبرگ‌ریزون رئال مادرید در فصل جدید درصورت‌قطعی‌شدن حضور اولیسه و رودری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26282" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26281">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJiAx5r-lsF2bqa7nK6YQADfmAAv_EjysTlCDsrmWCAsATFW37hDM328cFPd4PNQ7zy2yd37OrHMeCJBWvCtoyrr4461UKUw6iXCRMzyBTbK3bzwZqM6icFt3mbYlj_YrEU8HH_wl0XpBUg1_FK87RsQdl4Sn-ObTNxXtCUh_k8EY4ZPvXuHr4Ue1FWvH-OdbpIhSnmFkkOsBHZ050A4HcevwBoxwQNwGtUWFlxAwdIV6AIXk_qgiTc-ULZ0O9249HCFbj8u2OU85MmOOLXUM8UCqkLvZsxzQbZ7QaD9LnknhRTNhP_dvNxwecrznRTBrD-MtJdJDxWFlzb7OC6cNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ دیمارتزیو: مالدینی مدیرورزشی تیم ملی ایتالیا مامورشده‌‌که پپ‌گواردیولا رو راضی کنه باقراردادی چهار ساله سکان هدایت آتزوری رو قبول کنه. بایستی صبر کرد و دید پپ قبول میکنه یا خیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/26281" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26279">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgNfzF0NR4_r3zkmb4CRnAnKEsZ9QMYa5vNrE810htOIK6O5n2AONofqE_eDy1GZ_NmVUEOBUhD0E1goYwMxewOodMAiBv_Nomt_RTXMmEtB-4GV_xOrYCEkKGCnpE4Hvk2FVHVZKCQho9KFyk51uVDG94cT5j5Ghua017JKQlCDyC5vokpHRV6pKWotbSeyukx16Po7joQlHH7eVlSeeTQsBFTx2OYeOd3UEmasytq-JQLR3pRmR-k8JeSCQgJV7q1_EDfEeqSBIuPnojc05DEBI6KR5khPHZBd8Ez_98NgZ3x-wb6qhBq3AKuYSWV-mi2Ci1AOvYbk0KiYcmnDIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ بعد از رفتن محمود بابایی و مجتبی‌فریدونی؛ بزودی علی نظری جویباری نیز از هیات‌مدیره‌باشگاه استقلال برکنار خواهد شد.
❌
علی فتح الله‌زاده یکی از گزینه های علی تاجرنیا برای مدیر عاملی تیم استقلال بشمار می آید. تاجرنیا نیم نگاهی به حل کردن مشکل…</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/26279" target="_blank">📅 10:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26278">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cq3KPB4dWEq2SA9_O_GdN1dcVdzMOtqLAjytktXh6viEYqUJSrEdEAoDdwT5DqMiG3NV6NTOh1s68yo-V491M4SRrCV3xlfZ2y7EV6weNAO8DogFRicUFjZE4V4mcpJnOnwkh8iwPQf5CqpVi-BaP2YbOE48G0oZ0wDH71uTaeULqxBVo70D8xjfMqGYM-gV69plRfM-v1twPpUYcz3fUCySK4LXJQWHyizBdYMRqYwMFiCdPi0wJLXvs0Y3M9asog00R9E_c9_WLi1Yn1Mau885eUVZjfdTsaHccJjb7G96IgydUDwMPJJP_Lkg3oD0kVmAu16saeRupYW2_m0c8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/26278" target="_blank">📅 10:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26277">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2fwQEkDyLVzJCxMXqJVrgoXOr1JZN8wdH5eoVbmVExLp4vUnPZMUhjyFbPKDUp4aTqa9YJT7Mxwir8EzfuKU3R99VghS6DlkYsZcU5fwooaJB8E6o8G-aTGXUm4wyq_ICUTn2xDa1daRLFnJT9Ml6Aqm-69mfJC6QHjz6BufnqePkRLKhkUxrJ7FWtZ4A7ZDajKg9CuSRewC0m3CefYR2BAQhIcuv7mbmfgwd58BBuKbabkWXwTXIr7zW9uUlQ-NexarlQvsq6_GjfOwqA-7b4aBVTijjfMo-9idfdzl7JGxTIH-5n3Ko3PxAMet2EjTS7c1vMpPgfzE0y9OUAwmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
شمارش معکوس برای بازگشت فوتبال باشگاهی اروپا آغاز شد؛ یک ماه تا آغاز رقابت‌های لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/26277" target="_blank">📅 10:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26276">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmJiy_A6k6ucVxXUUzYVlXXfzEEXSOBq1vDZz17eNcmJvjiLYIWl1qp2nVopPLWrWdpOeD3Sspf4x_0so6NDq-dS53INzCuVkapag302wG1N_UXkcSolQl7g8h2vCwFQD5LwNgecXETHpL20j-TmqdhH7Vmv9N7RR_gGfSKerSG8Uqw__b1VO_emhlXNWpPJs7ys2FA8CM2qo6WN_GhTrDDheeEUMx0sJ3MiaOxw4QwyD9JvNBG_BIPpmUC_NEAJ_eHskliqh-kjfG7RHBiCzUpv_Q3G72K5yCTXUuj9eNUn5VIygu9tNm0p88MO4cStbGsQYr584cE5cHH6IHR8qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
#تکمیلی؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مهدی گودرزی رو 500 هزاردلار اعلام‌ کرده. این مبلغ از سوی استقلالی‌ ها پرداخت شود گودرزی 22 ساله با عقد قراردادی 4 ساله راهی استقلال میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/26276" target="_blank">📅 10:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26275">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFVjye_P7S8Yv0mUrn0qiaDyQshWwjFVibp1G4GkO-rE1dR_y6KcjQM49aqtkvPmtIwNTYW6_tS1UJRTaYH_hT7D9TjHl_EHc5ougtcyu_w09FCfPLFH--gjo-tHDGodXkIoT7nnAMXd9BZP3canA4B9wZ756H6_H6j13J99nwcoZhFZpaZLNl4p2sS7tAdENB6wURImUtbxOMs2Z0HaBNc3AkoPvmw4jce5a-AecaI83lgdU-RCZL38vWboP2LH4guncPgUUltPo7vsKPBtDzYvQiH-DnYdIuQK6aHoNcJfGgQGMldTNTY3s2oA98yxTFTz20IuO_In4N7MZlCggQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد خلیفه امروز عصر با حضور در ساختمان باشگاه استقلال عکس‌های‌رونمایی رو گرفت و بخش رسانه‌ای باشگاه استقلال پوسترش رو آماده کرده و فردا در کانال و پیج باشگاه منتشر خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26275" target="_blank">📅 09:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26273">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrQ4cTwCgyJr5cZNFd7VsZgiJohtXnB9rgRto1ASzxRgeZbLAxutwMUb9DUBIiOltPbfDVF94cN_kzsHq3J7nnZJxsWTr-E_IjSSGGNAeAwIchUkPxICv2Qu4cmNk-GqVhpRNYHreezcG1KzdJriqCr9qmIm2qrPCbmm-yaMS_XPzOyNZnrVq_z2YVTOfaIrpH4lG9KqjZ5JHIuirPLCL0IcnMqmHwm7_sWUFe73q_1kwKIzE8teRiXnbJIJ3GrHv1-kkCGFurGsLMPh_ngMeHAZ6E0zoYWdtW6IN0JLe7-_8n9XhCi6okwjRu5PYkjIHSzPDkkgqFjDRh6FHPipmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
رومانو:رودری ستاره‌اسپانیایی منچستر سیتی تمام تلاشش روبکاربرده تا در این پنجره راهی رئال‌مادرید بشه. رودری حتی دستمزدش رو به شکل قابل توجهی کاهش داده تا این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/26273" target="_blank">📅 09:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26272">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/955b39f6d5.mp4?token=cC_UTRrmfVACmOsPadkbvfwiqIF3Unaq84nlxmslHuzXdb0XZjhWSUaTdhmsj9-Dpdrl533b9587GC6wLrYLyxhc-3vWqiwPMBbPVVcmo9MgS8UOirQnPLnc3eaUFq7q1oEfEBCuWfGRMTajJ_DLLkHwpZTiFC-D_4IEBYEIhvQjJQoff45_Z12FQgD3WeR639q1meGXMbUpNFx9PAV-BqYpZT4_p5NJ3QKTGmqnKk4Kkd8euqfsyK7r-rIvwREySW_mnuA9iyiKPByIk6ArIb4Tx7Eix3jObsw8JMddYZ2Y-vDm68h7AXTQgy_cgD1-0hVfqZNJq2J8Lo775LqjdIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/955b39f6d5.mp4?token=cC_UTRrmfVACmOsPadkbvfwiqIF3Unaq84nlxmslHuzXdb0XZjhWSUaTdhmsj9-Dpdrl533b9587GC6wLrYLyxhc-3vWqiwPMBbPVVcmo9MgS8UOirQnPLnc3eaUFq7q1oEfEBCuWfGRMTajJ_DLLkHwpZTiFC-D_4IEBYEIhvQjJQoff45_Z12FQgD3WeR639q1meGXMbUpNFx9PAV-BqYpZT4_p5NJ3QKTGmqnKk4Kkd8euqfsyK7r-rIvwREySW_mnuA9iyiKPByIk6ArIb4Tx7Eix3jObsw8JMddYZ2Y-vDm68h7AXTQgy_cgD1-0hVfqZNJq2J8Lo775LqjdIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
پاسخ معنادار و جالب جواد کاظمیان به ادعای «بدشانس‌‌ترین‌نسل‌تاریخ» توسط بازیکنان تیم ملی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26272" target="_blank">📅 09:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26271">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzXg061jodvdt3zSFcRgdaNVdqDmcxPLOv_Y_joajJiNCQzNpWfpoaO4FByLQdx5mDOm62sPpVS20Q_LnB9_ixGTCnoiSvCSLAhaMPzYik1mrAK6xih7wQwC5zXs01sTlbbqMweqodi9MV0TsAoNXTJD6Z8Qswdg5otvpTsGPC3onDmlYXwqnpgrbzUQL_xAXLK7x3hL5JsropRsC9eSnLDnOks7ctFOrof5KdcmKX54Vdv1hgMWfaK7yr9CP0I2ObQEsIi84z20xBlfZ0snfrLIpzpQfoDMySQOyXZ09_SGb7aN8uKSWGlmCTyqtdgTYj3RYOvx43b16z3cCMyc5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال در روز های گذشته مذاکرات مثبتی‌روبا مهدی گودرزی ستاره‌ جوان خیبر خرم آباد داشته و حتی‌ توافقاتی‌نیز بانماینده‌او برای آبی پوش کردن این‌ستاره‌داشته و حالاتنها توافق باباشگاه خیبر خرم آباد مونده. درصورتیکه‌ برای‌گرفتن رضایت نامه با‌خرم آبادی‌…</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26271" target="_blank">📅 08:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26270">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab82c054c.mp4?token=vLotpyIDmmXq1mHl97Y-5GNfav8kPTfI_olhn1AR2zBMSbnu6Pj6gKASFZ3A2iEm_iUzFkqDGqoDWZjXAJ59OtNEAeIw38vIrwyU84l0rM89CWh6ussoZXLyuEVGtV7PntiWwTey1HlzEDAYa3Lh3OzI0Wx39nk3ZaKw0qtll-v2ivJRknCgsI8D3S0zuMY4Z2pczwGP0ypZgFZwRhY7YawrSawye1UiD6BbGgpdyyN_8O5qU0bpvUEd96lbVJtHLLlZY9gTzKql6S6u3e3SNXGIYB61mN_bbmH0aTLMGem_3ooM7rRuXUo2VqiKaxlrP4I2O6MFZi5V8sffxT-XzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab82c054c.mp4?token=vLotpyIDmmXq1mHl97Y-5GNfav8kPTfI_olhn1AR2zBMSbnu6Pj6gKASFZ3A2iEm_iUzFkqDGqoDWZjXAJ59OtNEAeIw38vIrwyU84l0rM89CWh6ussoZXLyuEVGtV7PntiWwTey1HlzEDAYa3Lh3OzI0Wx39nk3ZaKw0qtll-v2ivJRknCgsI8D3S0zuMY4Z2pczwGP0ypZgFZwRhY7YawrSawye1UiD6BbGgpdyyN_8O5qU0bpvUEd96lbVJtHLLlZY9gTzKql6S6u3e3SNXGIYB61mN_bbmH0aTLMGem_3ooM7rRuXUo2VqiKaxlrP4I2O6MFZi5V8sffxT-XzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
پیش‌بینی پپ در مورد شرایط رودری در مهر ماه ۱۴۰۴ که در ۲۸ تیر ۱۴۰۵ به حقیقت پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26270" target="_blank">📅 08:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26269">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRBdu4B6YuR2z7EK_NWsWE4GUGqEsOZqn3CmquAj5qvYVk6HzGNdWmjILDuTPcX0eYAwAe0CYevfqIqgzIfPfGnk5s8b6VUyjpt89zZra4ROWtLk1pogCRdi2Z6bhfRIYW6LJ4toLssdlHH0RYuTWvVeQNVCn0JI12BZKehjYyHBI2wOdKFlczkuWtQqcYyROPSlFaaKU1_ZWyVRJbzKeGTYeQ5HwkW1uO8v8_Ia3uExu7-OLZXvkm6WMnjrm1x4_MFPvdkfrO9LtM_oOP_s3FLU-9t74Ad-kobufUtJQTfaX99shzLUTf5TGIC5Nx0J3blzMwfcMdhXcNkxFNIWYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ رودری تموم‌پیشنهادات منچسترسیتی برای تمدیدقرارداد ردکرده و منتظر آفر رسمی باشگاه رئال مادریده تابلافاصله پاسخ مثبت‌بدهد. پرز بزودی آفر رسمی میده... قرار داد فعلی رودری تابستان سال 2027 رسما به‌پایان‌میرسه و سیتی میخواد اگه قرار دادش رو نمدید نکنه…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26269" target="_blank">📅 08:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26268">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBo0cxXm2eO4MP7A98-4M2pf5eRb3Wj3PfPtkw7vS5S36tiaaVjzIw8vTYPw6Nu7x4A5aSY-7LxcDlgKBy6kbG4FwNGXMI3aMxObsOOLYRKz3eWkNAlbpdUy155OoB0wHCvZWfS_z9dyWBPN7Pe5d-rsUCrRfphDE6JTObRKS9xSmyHVstToP1NklCk9UxFv7JFu_mvBjD76anrVqQMOieK7A-g1WoE2IdppRlc9R0FdbRjUQviFg3tLrOx8HET9jlPjYgDDgSAK0sJpDe8pSTQGMnTjzdBYZQeNeov_-IronT_7bg7slWgSGXHze4Wg12RlEejbFWzC1mRSaFmIIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ به‌ احتمال‌فراوان بعداز رونمایی از محمد خلیفه؛ باشگاه‌استقلال از مهدی گودرزی نیز در صورت‌توافق‌نهایی رونمایی خواهدکرد. گودرزی فصل گذشته یکی از موثرترین بازیکنان خیبر خرم آباد بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26268" target="_blank">📅 07:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26267">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c41630a748.mp4?token=MeiAM34zuDNxApDM6-6frDULqgoBD0JvrUmu3ub26NzPhaAfGl9cOpwrQF7vzffJPU456OPCAvns0dJotPko2UY29XFV6nk2zuBLGH6yZos4paAXwj80JULxp7KsZMWgLnR-7iY5HkJSqxdJl-I5997FMaFkZqKO1fobampUn3DmMyOwR_4eV-ljWOXWF8zD6P04odl7a6YKLAwBY-o8pGkF1E9rdUUrTkObOQlIfNIIywIZgLC6Ds20_Kg9kaU6re-NsbfgQdjEJNsoMsQpfP_rQPDUduwGyD2EvPfTNY0tuGtFxNPCCAiojIbDWGKcvOgdGZ9wddktV9osNbXVuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c41630a748.mp4?token=MeiAM34zuDNxApDM6-6frDULqgoBD0JvrUmu3ub26NzPhaAfGl9cOpwrQF7vzffJPU456OPCAvns0dJotPko2UY29XFV6nk2zuBLGH6yZos4paAXwj80JULxp7KsZMWgLnR-7iY5HkJSqxdJl-I5997FMaFkZqKO1fobampUn3DmMyOwR_4eV-ljWOXWF8zD6P04odl7a6YKLAwBY-o8pGkF1E9rdUUrTkObOQlIfNIIywIZgLC6Ds20_Kg9kaU6re-NsbfgQdjEJNsoMsQpfP_rQPDUduwGyD2EvPfTNY0tuGtFxNPCCAiojIbDWGKcvOgdGZ9wddktV9osNbXVuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های رضارشیدپور مجری‌سابق صداوسیما در حمایت از عادل‌فردوسی‌پور در پی حواشی اخیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26267" target="_blank">📅 07:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26265">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nsh-Bd3nkfk1-E3nDNMlkj_AQiLGwLSKH8uTIglAxaRmWJeesRYFTijnBpuV8HwSBT4ZokSpM5l1TaA2bMHKhydFGo537X0rgYF9SzDOFJ7pRWPaLbAF6oHGkVPe7cEIBUuQtzId7Gm6LJl4t5GYj0bY0L80jsT3ZcsiKm51WvhXnnYVNGOIHYUY3kCi_d2FeyY5OQNmQjylaYEuzXMO2sa2Gtu9wsQv6stiT3BTznni9_99UfB6jW3U8RXtBdKZY4UAZWSXwtNMxNfHD7Tsx8rrkMo3JRAUg9bo1e6v4xQzpeIFrSwTgL4L4IOM7R8-Y7CtuposOIll0mPgZJYU3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VRE7Y2adTTevcXmAYJ8IulcTg-LlFdXzgEZFsWVgOZOdfPjQXahVPIs9K2NTt4XArhsD8FHIjpyniJUYCtEtOKLKcIrLrEsgLG-G5bK349wS2fqzFIymSHedsL9RzXTKid8qM7TfdN5sdhJFvslTZhglYWSUGiYKgD0bVVplv61nHsMjX2saOF4DFh3bQc3zWahoD0Z1a1nf3kx-POna4t9iuGkSkLa7kmF4OJ8ideHEe2pOsGb8ke2-Cd0CNHeErpzhFjB0FzRMQXE8wyOnCD9sM0hTv2j84d0enyOJSdupIwpKw6bLRq5gCsIWNJVcHEjCsvX485VirkI3zve8ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اگه بخوام یه آماری از لیگ ملت‌های والیبال بدم بهتون؛ ایران بابازی‌که امروزجلوی ترکیه 3 -1 باخت درمجموع بین 12 بازی 9 بار باخت و 3 بار بُرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26265" target="_blank">📅 01:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26264">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zx3diKAJ8EIg8qJtwpatuq0IPn8R6159hnJ1P_BBEk7bDFD-UjZTcD2j6BlVaes4tPROLaZMY5xhihbSg__4-8k1Ac-uU3Ij26NGf4GYdnhgp4mulmMPXORUJ54m_xgIAiAcZWU5f50li6vPHxmRXlvjRYxf9Kp_1865jYkI7co9TFwsHs5m8g3J1JiXw97BhYHYmdy6r5rpAdmexrGeUFojadbJmfSvCVx-ew2YKlk402sOVQM0u51s4gTdBAWyu9nqQWCvm72P69Q1HgC2cilybam_b-P5OYR05YN0TfXyFPVj9Uwe6BiJOk2H0x6alngWSfvOVZz_I2PGiVEKVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رامون آلوارز: بعد از ابراز تمایل شدید رودری به پیوستن به رئال‌مادرید؛ حالا پرز هم بعد از مشورت با مورینیو علاقمند به جذب این ستاره 30 ساله شده و بزودی آفر رسمی خود را برای او ارسال خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26264" target="_blank">📅 01:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26263">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6052d2abc7.mp4?token=V72mJlRBULjNgpIJ19jiYeWfhMkG1ztv1zrQSQPDGN8XmvxaQPzOvMlPb_84t2Qe3BmVFZM-FnTV8SzZs4c9k8_DfGCFzF3gIwoN39WaXi5Myj7frYWyaV1VmsbSFf4HYJYNs8fGOg_uuoqTfXpldG6d32uf_yzsb7fJDMFPtPaAG__9418SpsXg5ye9pP-MJTQ_c0mBExod0IiUSVxMH1PVxWoFr4MlRSlncEMKGZzoCHv4TJweduVl7lEtqU-e1TjEI5CiWS6OpzEXZ7aNanTmzyzLTxSho8Y60xLBKgKTepxa3bIoIZtCaRoWov8XBKX23Y9ZFLyDEeop6fYYJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6052d2abc7.mp4?token=V72mJlRBULjNgpIJ19jiYeWfhMkG1ztv1zrQSQPDGN8XmvxaQPzOvMlPb_84t2Qe3BmVFZM-FnTV8SzZs4c9k8_DfGCFzF3gIwoN39WaXi5Myj7frYWyaV1VmsbSFf4HYJYNs8fGOg_uuoqTfXpldG6d32uf_yzsb7fJDMFPtPaAG__9418SpsXg5ye9pP-MJTQ_c0mBExod0IiUSVxMH1PVxWoFr4MlRSlncEMKGZzoCHv4TJweduVl7lEtqU-e1TjEI5CiWS6OpzEXZ7aNanTmzyzLTxSho8Y60xLBKgKTepxa3bIoIZtCaRoWov8XBKX23Y9ZFLyDEeop6fYYJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26263" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26262">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea272dc59.mp4?token=NP0jgiwW7xhhU1ZnBQ-nqblm6TwGun8d7K40wPc7Pi6koKKCygZOVRBlUxU6byMz0b9kNgOkABUiZilFgOhNxqqBz5iw_tBFQMuQsBjltUEa8Zd5ifF52u1Ix2SEWvhphCJQICqE0HB8_OT-B4z79NpycdHBq2coAMavRhu9HN2DOlhqPEBi7oHPudUsuFwjRDB8MJliSEUZRBPuccFmSdb1jXmJydnI8tksfftG-vMGXCb3kDYD285yCl4vKGL0m2bYK2SkuSxXcS8zgJD4OxnVQKPJfH3ayuaqPKzW5O6qcxA2AvWbudvIbhRvmWZtKvEI49hSUK5TkhCMwrHlIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea272dc59.mp4?token=NP0jgiwW7xhhU1ZnBQ-nqblm6TwGun8d7K40wPc7Pi6koKKCygZOVRBlUxU6byMz0b9kNgOkABUiZilFgOhNxqqBz5iw_tBFQMuQsBjltUEa8Zd5ifF52u1Ix2SEWvhphCJQICqE0HB8_OT-B4z79NpycdHBq2coAMavRhu9HN2DOlhqPEBi7oHPudUsuFwjRDB8MJliSEUZRBPuccFmSdb1jXmJydnI8tksfftG-vMGXCb3kDYD285yCl4vKGL0m2bYK2SkuSxXcS8zgJD4OxnVQKPJfH3ayuaqPKzW5O6qcxA2AvWbudvIbhRvmWZtKvEI49hSUK5TkhCMwrHlIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بجای مانده از مسابقه فینال جام جهانی؛
لحظه بلند شدن کاپ نمادین این رقابت‌ها در وسط زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26262" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26260">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQdqI49SVLnjEdLN5_ufPVq8_1KdrKY122DEwDNwydPlDVHY39GRB378_22ccUixIrWbBFbBc7vT83pQlSCaiPBGtQ_-bou2s5Kinn5TuZAWbuFUF0rGnXP88zSBRMiByqEfbwABkXZY591NepV86uwyL9JCCB8mLmisiv4nYbXPa149meyeIS4g8YHaIMxVaASJuWPa72bnxap0yIHpXabPBriCnerpfwp_SCrATKIR_FiypG0wm3eFfk-iQjCDxacsL_hSN9Ja9YEDdc2i8Qky_RthegQhckIYJjWYTpSajuEy2D6i73b2uCt7U97bNkc0ef94riUFsXEouV8xzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری؛ رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26260" target="_blank">📅 00:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26259">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c47a31e55.mp4?token=C0vUxMbBti-P-onlrnutorbQojywm8GGwyMOESCbv2f4azaqdKlfT_lh-EQQp6Kl1C-oNmnEq9Uyz0IU5zS1Lfe7Bi05DPt1HDZjFyC9WzLwMtNKU5TNyHET9aa39cVcvQJ3sqNdtvyDIIlvBqFDSxGyl44tEO9g5wbFfRp4sxNvbBq3eqNIjbdxL3j7RHIOU468YZdSpaX91S7_jxGUsR38q0dRxbv41QTJapA-Ky-eu6aKJVWD5y-s-yXIOzQq1LgreUzFcuFtLVcHAuyw6BVQ-SDcV4Rc_ZODFqb-mjI5NQUaZN4RJlpVbJdnhAG8hpyXW7GsPn_rVE3ln30Kjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c47a31e55.mp4?token=C0vUxMbBti-P-onlrnutorbQojywm8GGwyMOESCbv2f4azaqdKlfT_lh-EQQp6Kl1C-oNmnEq9Uyz0IU5zS1Lfe7Bi05DPt1HDZjFyC9WzLwMtNKU5TNyHET9aa39cVcvQJ3sqNdtvyDIIlvBqFDSxGyl44tEO9g5wbFfRp4sxNvbBq3eqNIjbdxL3j7RHIOU468YZdSpaX91S7_jxGUsR38q0dRxbv41QTJapA-Ky-eu6aKJVWD5y-s-yXIOzQq1LgreUzFcuFtLVcHAuyw6BVQ-SDcV4Rc_ZODFqb-mjI5NQUaZN4RJlpVbJdnhAG8hpyXW7GsPn_rVE3ln30Kjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏این‌چجوری‌هرروزکل‌بازیارومیبینه‌اصلا میخوابه چیزی میخوره؟ چجوری به‌این‌سرعت جابجا میشه؟ منی‌که‌میدونم از اینفانتینو دو تا هست ولی نمیتونم ثابت کنم‌. مگه‌میشه‌به‌این سرعت استادیوما رو بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26259" target="_blank">📅 00:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26258">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O28_7FohRGnvnZflTCsOofS5SvB6yrRAiLTi1Y3sR962oKNm4TKWTNr3oXYRmgFImAxSp0n6g9AEm7uAtb2_kyTf0_rQjBwkzJCHQ0jdasfAA1LhsVIZoBgfAm5UGqS-CZHVT5Pg5g1IbCOqfNpjcVTgzVht4gYEV_gvMCs2PsDPThhBCtHMxN0Qkp_wrDQJVaUNHUP-t3rIEIfSmOs9rkyIDXMhLn21tuiJ5pZh8PX9_H0SgutGp7vKqT8jgQ5c-c0YUj4sfLbFH6wNW7aq04PQyt9dE7zFc38E5HTSdvk4vWGyQaDaIzU1uodMMEKc7xjUXNmZIUB79JCec3SMgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سیدبندی فصل جدید لیگ‌نخبگان آسیا اعلام شد که در آن استقلال در سید نخست و تراکتور در سید سوم قراردارند. هر تیم با ۲ تیم هرسبد بازی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26258" target="_blank">📅 00:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26257">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxjQBOzVyOqJ5dVCBznf_Z0qUqUuG0JH7m3ZiXssyf3zmez6OWEynd6VGczs-TWC5rrwXqk-UI_3AhcZFPrDQ3kEkstFB_tTmJfUpAlcIVzTvfsWNYdR1SFndpoTWWSMFQdKkeNehuBScB1UEz5Q926x16JK4PzBtRskBH9f9kQJ_19IHaIdW_VsugyeSY1bppQAHV_ATM7uesUa2B6gHGsC9vRDTqAlZKOE7fmUTBgScuQJzOZS_zXR3sOtO-kNiWLI4qX9SzuX8cvsOlrATP83SBFRMVBFMI_xKU1LzY78el_EAAnANHwXM9yGIjuO6s4pHpPilJExfkLhr8F7Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعداز اورنشتاین؛ رومانو هم تایید کرد؛ مورگان راجرز ستاره آستون ویلا رسما به چلسی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26257" target="_blank">📅 00:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26256">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJwRnXIn-5W7eAWnF2AcEFsjjYhJG2vtENXzk8NNHqGa6Ump13Av2RDUMU25WWcX28MmEHlfLfJMgKM2clTDJr-4cCWM_1n39qs92ZQu2FYx3tL2DstECx8o8Q-q2MZmAgIVepLzuVPzqUtp4taoxZargTU8KL2k6CuLbV1L1mKwXnCwICQWB98L754SovQtKjv32iUZzF5KwufR8aZl26pkqqvh0g6a7rq4g8yXHBbr0StRRECCpVzTF96C-hece0iHPLZfOZW7OdTtnHR5Ex0JY_aHVeI748oXP7Wy03omaOGyI8yNJB7nFwVJMolxXITESCFNgU7ci-d7uy-gKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ محمد رضا آزادی که یک‌فصل‌دیگر با استقلال قرارداد داره برای جدایی‌‌ازتیم‌ خواستاردریافت 20 میلیاردتومان شده. آزادی درلیست‌‌خروج بختیاری‌زاده قرارگرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26256" target="_blank">📅 23:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26255">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbsV8aTbnZ02egcDhUM6ezF7nQm61KiKoXQddd1eIozEU1qomay68iVIEWHiyugVRrQknmVBJVCK97sUxgxUHrSMbc7Q7uYehIyo_yiv9UcSj7PHymQiKdWmB13woqOsyMTYpN-cum8FdUNFQV-LDs_KGZicjh8t2kNjGNDU4sTjZW92wWWGRuChx2UPQuGzyr4ryoS4EV0v1CNURg-9qxmFwwxKO5CN8JUGLOfV9O_PgVREwifJX9Jvj04_KCnE4HwOYL8eKuyxUoVK0Ok_JNOKPwEJvlm0WTwUbuvnJfkLmRmXUxY1PqQNVov2U6ZSmw898OXgBparQyMfJROKzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیلیان امباپه کاور EA FC27
؛ نوجوان و جوان ایرانی باید ۱۱۰ تا دلار ۱۹۰ هزار تومنی برای خرید این بازی خرج‌کنه. تازه‌اگه‌فقط بخواد آفلاین بازیش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26255" target="_blank">📅 23:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26254">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AiIa-0UhNAAULJaqJfjL_4IfZAfINbq-gMHJFAF-CAyQOM6ziaJMhCB2zLYAuAJsSOWm5O0pm6vy2C_63jHD2rwZ5842ufPJxL9pwvGLNv9ib2EKGIMv_vLX2ylGtUB4DIYgu9gQULscFqaCDExc5ls-GH_Qv7-ZjDI4mW4y38FikryTV1l207UUv9VjHVKIgMNMc_p76n7vEzRKu4Vb3-IujqZFgZDjkU8uFx2lzlqFlgyZnBbVoY-mEG6xRD7cN5khRdSYUwAlxXVI_g4xwU3SDIrNpI68-ZXwHA1Fi8Me2ZNbWfYDibSDKp38lhSgGu8f7Cc0nIzA-rFLjYYJ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26254" target="_blank">📅 23:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26252">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42bce1c0ee.mp4?token=s97fva2xGtXcTuAZ9TLBHhanp-amXs1MyYCSNQKgNLizr0Px030aEJe_SG9BKWmlLoGtnop9nDAVQB8Tywx_nlDT9tsqlP1-3sBRNZ78EARzmJCxQt4Bqhd_oM_MVJ930sKLFGVrKxmvoyBRCJA1a_oFAkyggT5I3sm5O3vKTjNc6H2gsTpsUsJL-Pr4-W8FM0SUNh-dxCMK6Bqdqo3IX9swiLUfSQR_3E_4A35GC3ujCrOZkhO8BVwWjPqyLQvddKrUPaNA0u5E3aDxXgiuLf68_cxkSccpzV0YKVyJZ-Y98LqAHmZWsF7MZ-dhJ5_V8K-E1ufZioPXsjWM9N4Qcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42bce1c0ee.mp4?token=s97fva2xGtXcTuAZ9TLBHhanp-amXs1MyYCSNQKgNLizr0Px030aEJe_SG9BKWmlLoGtnop9nDAVQB8Tywx_nlDT9tsqlP1-3sBRNZ78EARzmJCxQt4Bqhd_oM_MVJ930sKLFGVrKxmvoyBRCJA1a_oFAkyggT5I3sm5O3vKTjNc6H2gsTpsUsJL-Pr4-W8FM0SUNh-dxCMK6Bqdqo3IX9swiLUfSQR_3E_4A35GC3ujCrOZkhO8BVwWjPqyLQvddKrUPaNA0u5E3aDxXgiuLf68_cxkSccpzV0YKVyJZ-Y98LqAHmZWsF7MZ-dhJ5_V8K-E1ufZioPXsjWM9N4Qcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیوجذاب ساخته‌شده از هوش مصنوعی؛ خوندن عو عو برای عمو ها این بار با حضور لئو مسی فوف ستاره آرژانتینی فوتبال جهان.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26252" target="_blank">📅 23:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26251">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b149394bb5.mp4?token=m5t36FdwqKAsmwVoAfltoeidEna6Uu8xcZaJ6FRCxVl9KTDPR1wIC1YsaZnvr5WefXWH0tPK4BpoxhFB9jQxWRWGBbjHmuZQ3aK4lT1me6rQ8tJw8EKemEdU4YI6YTdePohmUAJpH2xuIAJz5xenV5luQxbXnLauVpubgVVnWa9B53QMEozcBDs-s5Ozwpr9GPB_FEkQ9_Y59_U4vuzWBf1YpjDfDujCg5dBuc4YXbuMC95g-xtvtYrqg6gkZH-UyraLcWVZBTIpfeayc2ERUARIlD4RR7Uhc2P5ZB312z_5qt9oh5AvU78v57gba7wO0rZW2RD94fLV-9GitCOgyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b149394bb5.mp4?token=m5t36FdwqKAsmwVoAfltoeidEna6Uu8xcZaJ6FRCxVl9KTDPR1wIC1YsaZnvr5WefXWH0tPK4BpoxhFB9jQxWRWGBbjHmuZQ3aK4lT1me6rQ8tJw8EKemEdU4YI6YTdePohmUAJpH2xuIAJz5xenV5luQxbXnLauVpubgVVnWa9B53QMEozcBDs-s5Ozwpr9GPB_FEkQ9_Y59_U4vuzWBf1YpjDfDujCg5dBuc4YXbuMC95g-xtvtYrqg6gkZH-UyraLcWVZBTIpfeayc2ERUARIlD4RR7Uhc2P5ZB312z_5qt9oh5AvU78v57gba7wO0rZW2RD94fLV-9GitCOgyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو آخرین قسمت‌ویژه برنامه جام؛ خداداد عزیزی وسط عذرخواهی از خیابانی با خیابانی دعواش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26251" target="_blank">📅 22:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26250">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cV7pvVH9UUsX2O-qKZJQ_O-jkfPcafl0pEmmJJDu4HtzzlOQmr8nyn_WSK5bOIT6cMAl_BPDdJFZpLsgOb_5VIyyrPKp83UzJdkarcDwE74fe2zZKk7biHXQ_KpPG2TMLLW9RvWVrEuA-5qYwSRePVlW9lX9rjIUtrFi8IKb5k8m-32fdU4jBvKOqUVi6Jjk7OCwQrCruxixpIDKU0kidZkJAHp3r14LRJKvVMgVuSlL1drJpXo43JDsNe-yum539R-jw4hfZ6a2k4pEXTjQYBnFAqSZlKAtZoqFYaBYrFN_Rwz3nBcdcNLyUeoefHhy_DdiUuSR1S8SqMQkcKSpeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ویدیو باشگاه استقلال که به استقبال رونمایی از محمد خلیفه گلر شماره یک جدید خود میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26250" target="_blank">📅 22:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26249">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2d1e4b083.mp4?token=ITm44qlFgte4lW3HLIMuTnxNLFBLbQhy0IACReHy8fUqiov8QHo9VPAmgAWiJS4T8AjvGq6kSoQwfFEatAVEtWZ3CK8GMx1fMMXiwESGoI_4skzr3vAxl401AHxYlfJ8M_mxCZunVbk7VEH5sfwOpM23HAebLjE14G8r_Plz1zre_IPHag1I_dCo1Xe8XkpENr8z-FR0flY3HzlSyK2jgkMfaGnuknOprUQTitpXXOqZbmBBwEB9zs8rASH0XCaxa2LvXbMedZ601ykf_sVjHH2ww69nB45dVrcws_QAISe2qNysO7uDy9K_KjcC3YE7CgITY-8HipS8X7nj3clgsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2d1e4b083.mp4?token=ITm44qlFgte4lW3HLIMuTnxNLFBLbQhy0IACReHy8fUqiov8QHo9VPAmgAWiJS4T8AjvGq6kSoQwfFEatAVEtWZ3CK8GMx1fMMXiwESGoI_4skzr3vAxl401AHxYlfJ8M_mxCZunVbk7VEH5sfwOpM23HAebLjE14G8r_Plz1zre_IPHag1I_dCo1Xe8XkpENr8z-FR0flY3HzlSyK2jgkMfaGnuknOprUQTitpXXOqZbmBBwEB9zs8rASH0XCaxa2LvXbMedZ601ykf_sVjHH2ww69nB45dVrcws_QAISe2qNysO7uDy9K_KjcC3YE7CgITY-8HipS8X7nj3clgsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌ نویی‌ گفته بد کردم ایثار کردم!
آقای قلعه نویی‌محض‌اطلاعتون؛ «ایثار» رو سربازی کرد که تو اوج درگیری و جنگ، با وجود همه خطـ..ـراتش پست نگهـ..ـبانی خودشوترک‌نکرد تا شما الان راحت بشینی پز ایثارگری‌بدی! «ایثار» رو اون پرستاری‌کرد که توی اوج دوران کـ..ـرونا با وجود خطـ..ـر ابتلا، دو شیفت دوشیفت توی بیمارستان‌میموندکه‌انسان‌های بیشتری رو نجات بده.. «ایثار» رواون‌آتش‌نشانی کرد که برای نجات آدما وارد پلاسکوی درحال‌سوختن شد و دیگه هیچوقت برنگشت‌ آره برادر؛ نه تویی که ۱۴۰ میلیارد تومان فقط پاداش گرفتی. حرف نزنی نمیگن لاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26249" target="_blank">📅 22:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26248">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8899308b74.mp4?token=LijbD7UQjg7ZmMG6SHxOl_LaZiFgLDPSisR8WSF5ZFt0kRVs8PBGdDPkApDMTtciOruHGd2kPpiYAGxwKINc-RTivVxXgZrj3KC4iOXFT9i7Y_YUXoOlVoP0ytJLZf2yKRus8BQPB4Gv27x5_PKAthvzhVVfWmqt3DRUb9beFCO7UoJhf9LM4c6PBQNYVAldbE-L6P8aiQGYjpyvcuSvEHIpvLE5hBAWYYeeo2OEIKr9cWtyeeHnXyU9ia74Ofkt1txpEiF0VONrx52m30H2NxgoYCwGVUW9p8E4P3pQRTO_LqbayvINMPd3HS8ztAOfOG__SiRrbArwUwUYSSGeOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8899308b74.mp4?token=LijbD7UQjg7ZmMG6SHxOl_LaZiFgLDPSisR8WSF5ZFt0kRVs8PBGdDPkApDMTtciOruHGd2kPpiYAGxwKINc-RTivVxXgZrj3KC4iOXFT9i7Y_YUXoOlVoP0ytJLZf2yKRus8BQPB4Gv27x5_PKAthvzhVVfWmqt3DRUb9beFCO7UoJhf9LM4c6PBQNYVAldbE-L6P8aiQGYjpyvcuSvEHIpvLE5hBAWYYeeo2OEIKr9cWtyeeHnXyU9ia74Ofkt1txpEiF0VONrx52m30H2NxgoYCwGVUW9p8E4P3pQRTO_LqbayvINMPd3HS8ztAOfOG__SiRrbArwUwUYSSGeOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26248" target="_blank">📅 22:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26247">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-lNypCN9BJkTO2abKXfFio2J7a_-rkLgyu442yGdIthrAWjNSNUv-c12QTw9zyXgro9CXWLrZH3RTTB-JJ6o8mkYjLpsXAH41_fYwq4QSs3qqoUJ4WboARPq78xhZ-WTKB_v8mrJyC1mnGnlQCr9TJuyiylHoGwDORnZ8uKWFFRCT4bYKeDcFeT5ad-pbL-ZbdMJXEAKjlugF2QhC6UbgLXDsO3DTNhcDP4YIIcgMapXA1oNMOhkjnSTh0UJ7VehCMkDrPHhWyqAyu8kBMU_lUYeaA6jemNNpcptKrYL9_RrOg3QLrac8CN89k44zan7vX2QBnvir1ehyEe7SkYuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛
برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26247" target="_blank">📅 21:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26246">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chbFagi1cO8Kl5onFicI91ruqt-GF-YM0fFlsR7-kUzBU0lF4KpFphJK5990WT8kDVd-CgS7-bhdE5-sxJldXu5Ax6XvUXcr3MCQzjbfqTraNTw8fClvd6-ZtzDgEgto3HPxRras_zXumvfQ5VUgXWcKdpv38263Nu2Dw8reoAXZc2mBef7gNY3rkhLGTx0BirnWy00nrOqflel3gQtD2X0EBwGebKdgRc1pG7-f2zoKID_UP9V7jzB5rrq_RPNmVBR5rbXyRASN5yiKZxmr2Y9RWa_JLjjCFs38DSmno5YpeU6fpoHAhGQLF34SrAWwRqoFHyK3HIfJi5oojkwZxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
متاسفانه توی همدان بعداز شکست لیونل مسی و آرژانتین توی فینال جام جهانی، یه پسر نوجوون نتونست طاقت دیدن اشکای لئو مسی رو بیاره و از شدت ناراحتی ایست قلبی کرد و درجا فوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26246" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26245">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfbn-ROZusr7gJ9CAAx8BHi8eKQG0ITSDRbrvhysftRii6cmz2L35WKdwDaFy31OnA7zldmLwg2TjTpV8xqYdkWTOn5B7Sb6TbpNwEl9sUrrUTqkzwpaEEtSJBP_-I50lzBBb1pN1PMBORKF9-8KiNuMYGMvJ7HhtJdUr2FKeArWTAIF29Zgobkwf_blKpI_JSxve4qzvEGufB4JRCTcsOY-QIGSBm617XR5V3x5tKYovBLu4QQ-E73Xs6frsELGRxsU566zDAKjwFKfuaKHllJNpw3ZBUB8-HII4UJ1RaYcDRTNHncU1JmhlQ2cjvEcHKKurzZSfhh3elu6oC54Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
نشریه گاتزتا در خبری فوری؛ لوکا مودریچ فوق ستاره 40 ساله‌کروات‌سابق رئال مادرید و آث میلان تصمیم به خداحافظی از دنیای فوتبال گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26245" target="_blank">📅 20:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26244">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/512d886ac4.mp4?token=oUn6EA5MIB8U6h0Jw029lbTH0D9MqdA7J8hpXou0XHDtxv-_oU-p5GwyDjUCDoPAJghh4CuYRY5Uk-XhnxQLhU0l3-AUxyEME12m0KPxhOeBivb60L0n3h39doffdzwk_WOCkw9mwZsBytrL1GnVevPPGRAGoIwySZjNCsCyMMFrYpNCoh2hKRMgF2CKIqeG12kN1kaUDXfBeWFRPyNA9mUTLJzIpv3sAjJ1p95cg0xaf1RS_SstqLbTla8xsV7cfdWKvtOtz1bxpVDHCeAVkz6aCu-uxskQC6u1Dnur-ayjr9GMQdVm6Dqb8vv1F5UAWp4AIwCZ3caki3j8kxKXKzcibDBBqGHEU-aeS2BD5HKepHr8K8sCLs9lYQjm2AboMkXWeOW1h8fdU7yeoae1RjYK0cLyFd3v6jP8G8gycSTkxfQA9ga41J9Yg7CnkduhVlIngCLrl2C6d_YglXsgMaL89hnZ3jBX41_L6bcOgsrH1BW4coamnMOkVgLE21qdphCRDhgHZu1uLrpVrrr6vX7C4klq6mAUPd-uQC7tluhkjCu1LMjGjijQnzqpoo5Re79Ah83pg00TEu9-T0eSybUl6Kmibzm3INANL1HZ0UalfVPqtYl-6T-N5eX1qY746oQ8VmUQ6G9RUXmyk9Oo2-bwDycR9ZTnh_pL1iqQKu4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/512d886ac4.mp4?token=oUn6EA5MIB8U6h0Jw029lbTH0D9MqdA7J8hpXou0XHDtxv-_oU-p5GwyDjUCDoPAJghh4CuYRY5Uk-XhnxQLhU0l3-AUxyEME12m0KPxhOeBivb60L0n3h39doffdzwk_WOCkw9mwZsBytrL1GnVevPPGRAGoIwySZjNCsCyMMFrYpNCoh2hKRMgF2CKIqeG12kN1kaUDXfBeWFRPyNA9mUTLJzIpv3sAjJ1p95cg0xaf1RS_SstqLbTla8xsV7cfdWKvtOtz1bxpVDHCeAVkz6aCu-uxskQC6u1Dnur-ayjr9GMQdVm6Dqb8vv1F5UAWp4AIwCZ3caki3j8kxKXKzcibDBBqGHEU-aeS2BD5HKepHr8K8sCLs9lYQjm2AboMkXWeOW1h8fdU7yeoae1RjYK0cLyFd3v6jP8G8gycSTkxfQA9ga41J9Yg7CnkduhVlIngCLrl2C6d_YglXsgMaL89hnZ3jBX41_L6bcOgsrH1BW4coamnMOkVgLE21qdphCRDhgHZu1uLrpVrrr6vX7C4klq6mAUPd-uQC7tluhkjCu1LMjGjijQnzqpoo5Re79Ah83pg00TEu9-T0eSybUl6Kmibzm3INANL1HZ0UalfVPqtYl-6T-N5eX1qY746oQ8VmUQ6G9RUXmyk9Oo2-bwDycR9ZTnh_pL1iqQKu4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26244" target="_blank">📅 20:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26243">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogTTWV5Nd8rPMYXux78euwvp3tbEz37zKwzkiz0PWjjwy-m-3RDfxtGTDWSE_diQzTTxjxdf4xZkFVIpTku37ELtQzwwXz0vl91FJPxRTQmMZqIBFF3RMefQNtcRSSGv8FlPG2TpFw8lVeveUwkjcuVo9cyOINv9f8kvuiG5dyRJzYwLG4WiCic_M4dSVgD3vSFvoMRW5_pe2jZAh2gTkyqsNVTFPNZq0WC-WqxXc0TrR8kW523JQdain6rDsbgbHvwCQle6ZuqyzyfRdzWzqvn2ZUkYW3VvOCAJ6rnCdKb6RkiQhqMEsJxR7p997jGTNBdtoJXkZh1shJmZY4iSRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26243" target="_blank">📅 20:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26242">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKrtyx0aHmyyYUQsOQsP89CEzhfAQNr6WxfjKc0NJ96TKnPqSxGYGCjyRdqTF54UC1ZI9ZDISLPAOiwRriM3H1S0kFhGITJDtORUNQEj1JUBAluTiC0BixR3j8pYbqixpVKqojos19Re3loxOst4WJvcGSYqeDgXtJ6Fru4sMsi9S4RiGHvtYJKZQfExLKuq3tLMOe53bQ-sKWRIv5ZCExURxdveR1EbDbZC8hnmAcA7j8LgTNTEtC7IBw3qr2qjNhogrGFObdS6x8wkGaEr_TFV_i-0a6QfNOw91YbANXS_Q41beKQ8pjK-GvxG8QfrerMPEZ9RHqEo5uYm9T_Wvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ رامین رضاییان ستاره آبی‌ها ظرف امروز یا فردا راهی‌ساختمان‌باشگاه استقلال تا تکلیف نهایی‌اش مشخص شود. اختلاف مالی بین طرفین بر طرف شود رضاییان در استقلال ماندنی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/26242" target="_blank">📅 20:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26241">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2or-pA7-PiEQqfk-Vd6BgYDtOQW3XHaS_VQ9fsFUo0jUouxAyBndqD1fyazIeQZRjTr_MPFKq1qTqC7gUZ2krkNjfMC4AUqcobUZWh3uA5av9ZNKia1099LnUswAJibykrfUT0uqrBsLq95Qd3d04Gx9-Gt1l5nFrOCi-Q_OpEwvIvj8aGnbgqV0fYmotybEEWHHQYZpj0FbNPOEvl0wp_NZtx11AnkH8oQMpToFkqdGZxg5qf3st4w_79Ekhz9mo-oQGNyPynWrDwTYnD9gYkCJyLK2RH6-ZAkq-5RplRUzcKDPT1y0KVYIsB2yAyq6aASxqOmL6c30lJhz6ilmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26241" target="_blank">📅 19:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26240">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tcuo8xZD2I6jSr79f_M1pTR3ZGYwEyMVWaGv18nZf7WM6Flpu4QQa6x-GwN0_4_R7b659cCO2uxB_L0UGcY9gKBsq_f6bXEMEOHZ4Yo0YX7kDlOB_pyZPeiH3NWc81mkB1CCrIgb-LEVcXTC56PDiLpsYdbD2OkmKDsUpico0Gjqgz3QV6CdvADsDe9ptpHBtkla73t5s-Z6tpGe1wDAWt-LsVSYQlZ03HrBLN80B_dcw48BvJfIrZjIw6ceISHmmbIG5ELlqXLCOKJ3GR07t9AwqgXNBLkS1rl23eVXzV8fQD1NRNhOfONnReKKjpl8vnJOCtNA2kb8yyQaeeCOIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26240" target="_blank">📅 19:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26239">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWvIf8kMNWXzCMoftFSzBg_QICjr9LYVTHnAZe5YDyhM3cQctVZeM1xdCSUmUf83gDeuFJwdbmBbyS3tFSzcI-ghy9Hfxz1MKcNgFM2MSSFoGx5ulECibb4IOpBYD5Yp5YMUM_nnQdGY1RsEufKs_1W2TpJiuwi5kX-CQuFqTJLF2LaGn1D8arZ2_PYJZx4AX5ezPPhmD15EnWXNOYcz8mwY9Kw3HA-gPZD_q4aThyKB63U_mgOSE5l3LAbmGJVUB88T6BZR73AjnLmz2SWFCEyPhHsarwyu8lSkGQSdrx16R8Le9k0w1cmdi6K8Zl4uRb-jjRpsA4om-2NA7XH6fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
تیم پرسپولیس امروز عصر در بازی دوستانه بادرخشش مهدی تیکدری 2 بر 0 از سد خیبر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26239" target="_blank">📅 19:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26238">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fe98fee7a.mp4?token=OE5KC40RTkgYfR7JvvEY1JibLjXxamawM6uH-poTz3fhmhWyjevHV7F3VruJ1s1JdbIuHkcm7q7r20BqLIO8cwm1dJ9wXGNIzIb3GWZLkRHJ09Qu1j_FX64KT0J8iiOb4WtcYSKjp8uVCWAFG2iKx56n1k38kjrEJ2Sr6uU2RNVkBkkQawae7MjbTZspYaESIbF2Div0QHprH8XAGdqpq2sYXvXjICZzsAb2z5T37_SWMBPPh_FYoFnRN4j9-i0VQyHN4m77LIBBLlLHzQuIhYPMsSQyWnhE37eiuerRrE-9Fx8jUSvs1h-Kl02e2cvkUFV38Zi1M57zn55UueJx7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fe98fee7a.mp4?token=OE5KC40RTkgYfR7JvvEY1JibLjXxamawM6uH-poTz3fhmhWyjevHV7F3VruJ1s1JdbIuHkcm7q7r20BqLIO8cwm1dJ9wXGNIzIb3GWZLkRHJ09Qu1j_FX64KT0J8iiOb4WtcYSKjp8uVCWAFG2iKx56n1k38kjrEJ2Sr6uU2RNVkBkkQawae7MjbTZspYaESIbF2Div0QHprH8XAGdqpq2sYXvXjICZzsAb2z5T37_SWMBPPh_FYoFnRN4j9-i0VQyHN4m77LIBBLlLHzQuIhYPMsSQyWnhE37eiuerRrE-9Fx8jUSvs1h-Kl02e2cvkUFV38Zi1M57zn55UueJx7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
🤩
انزو فرناندز ستاره تیم ملی آرژانتین: بعضی‌وقت‌ها واقعا خودمون هم از خونسردی لیونل اسکالونی متعجب میشیم اما او میگه من یقین دارم که‌دوباره قهرمان میشیم. همدل شده‌ایم که قهرمان شیم و لیونل مسی هم نهمین توپ طلایش رو ببره. حقیقتا لیونل مسی رو بیشترازخودم دوست…</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/26238" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26237">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ks0FWwwoTx4g0LRq1bB8rC28NIJ90btuj28pEY2qNr_ooMsqfsZPk-X3bVGg_UOnfHDS0mOWmiOB0F5MQKTP5rShgK4nSTa0s6A6y30iMtv1QL7C0Gqeh314GTIsnGy9ovGqmab53iLxvRf0HjZLQVAREU59jyxjDCTrtjKrlV1JQcGAGAbjcSBaW9OqodK1pYA4xJhdWUyta4IzyqwqJn9XXsUmUECrZXYQOhUOd7bQL2dyb7iCHK2L2JIm1okBZLzY9SCZohcXU8jubfL8QFzcN82SISZABwYGlTy7PWvgGx8zW3PFLirSsP7eexlHEcA2hX1yDlq5hhb00IEvmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/26237" target="_blank">📅 19:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26236">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aE8oSwlldAGTnWGpXHZfogPFKHe73EXhpHFgBBYwvQ5nr9PMJ8tND7pJIM-qbTZltH4lG7SrATn2o0UsPbewVFxtj8ueu7nNCefxkH0-QHz7_sS3WiQb7oLsxGyNpShEOk4bJPWkrJHJShEvF7M_El3aPaP5ctCPcq4AZZRwsSKAA7fhXxiuBs8WZiRHb2gZLaYCWK8lcd4HSHIpxloYj1lgLxNwVdtAKDe5OfsyH-9PO-JEh39ZXtm_QbktAGAuOk3AHsx6yU71wqNaYOszQ9iTtoOf2YATRwgV_bwE0-4MJlLN1BGtBVs5faHLeR4qv64W7AdfiUBrmS6GqVCHXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/persiana_Soccer/26236" target="_blank">📅 19:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26235">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aX156REVE7fr2MY7pW61x0BpyuIXrGQ14PX7QRhKWvXuQFg5MgNvHXDlpAvlFxBU7by2E5WZTfNajMgYzRqwd20skO3eTmVY-yqNPPEKOkBkAE2V-YmMzxvHljPmmlzxa8sheIG1JhkOO98Lq7mQbLAjEmPVCkeQBKstfSRBkAKvi4SAMUcwRoj8GgGEe99TUoSxuU88j32V-DN7JuBxm94IGCneGS8lrAD8vIpV7IG-n5J4zdRBrwuHaRGc31J2giQcuqX2n-POjqRO_HJQRyGh9oWebbHo0rTU_VO9llaIIFp9duUsKHWCf1aV11b9eKmelM2jPZxCOmLRpJvZbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه پرسپولیس دو هفته پیش با ارسال نامه ای خواستار جذب فرهان جعفری هافبک تهاجمی 20 ساله ملوان‌انزلی‌شد که‌درکانال گفتیم. باشگاه با خودِ جعفری به‌ توافق رسیده و توافق با ملوان باقی مانده که باتوجه به‌فشار بازیکن به باشگاه در روزهای آینده رضایت‌نامه این…</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/persiana_Soccer/26235" target="_blank">📅 19:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26234">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59137224b2.mp4?token=tbL4z0s3-GCbV1vT3QO0s1LKBv-Insy9ssu4IAV1PRRyqSSerbdOzU5W3xhFFA_YFJMr2WYUpoyRUe78zC_mdjHjqRi1-MLTZLRT7-kJC5wqzPxkq9f3FW7I_07MLWsS0ueqNf7wZTrQ8WOHmadpKCbICAtE0YEYP6vnp4UD-nP6laM0ZjYJNOk-ITgA1UDd5cKIMpbN-Ar1CuIGk0xxCE6g0oaoJqAqv0onMnW2DNDGfMMF0M5IokVSWB5d_hwrURxXxpr3BQQNb9IFcj8tFimeFGjYpUsyyfyu9vv5N-zuK_xcUtdFcaERIiai_xjRsqr1IFORiiyXBfV9eklVCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59137224b2.mp4?token=tbL4z0s3-GCbV1vT3QO0s1LKBv-Insy9ssu4IAV1PRRyqSSerbdOzU5W3xhFFA_YFJMr2WYUpoyRUe78zC_mdjHjqRi1-MLTZLRT7-kJC5wqzPxkq9f3FW7I_07MLWsS0ueqNf7wZTrQ8WOHmadpKCbICAtE0YEYP6vnp4UD-nP6laM0ZjYJNOk-ITgA1UDd5cKIMpbN-Ar1CuIGk0xxCE6g0oaoJqAqv0onMnW2DNDGfMMF0M5IokVSWB5d_hwrURxXxpr3BQQNb9IFcj8tFimeFGjYpUsyyfyu9vv5N-zuK_xcUtdFcaERIiai_xjRsqr1IFORiiyXBfV9eklVCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
راز ساده‌ داشتن بدن خوب در کنار ورزش کردن مستمر؛ به‌هیچ‌عنوان سمت آمپول زدن نرید تا دلتون بخوادعوارض‌‌داره. مستمرتمرینت روبکن تغذیت هم خوب باشه بدن خودش یواش یواش میاد بالا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/persiana_Soccer/26234" target="_blank">📅 18:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26232">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uo2soC9HaSJs8HGq95h0PmMsLpz8Tcag781uWEaZvh23DBPSSIseyAXi15oEyFdWGZnoyi0xg_WTgielj5vbPWKrs7vi45m7FqIOuvdn1N7zHCcT_AOeK7zKFL3IAvVCEDwLSkdfEfE5SE1unV_6pr02JWyqwwPrmUqkqj2Ez7_gOEBi0zPE8vsuew69qnbWy4EzkFPlzkUgnHoeyf0AuOqlJy0VYTExsAs5SM-648firce3zlylQXX_RHy3wPvkvm9x1702BbPb61FZtAh-_pHRYENeCZqI2TTXyaecaa_F56EhIszyDFJyv7tx_fMFpbYGnVl5X6sl_-etp8bbNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WcKeVDC8plMQxllTX4N9tKXlCe5o41Z8GRvBiIfiufTV57jb4bwgXzM-6K7_uQgQmIxeUY6dAmFkQ83Xc2uBWelz7olUSCNFdib1SQJtF9t_gb4oGVcUN8oIIvgGPBeEO9Uho-0IMiBjKMfXmskTcM1xHecgpjO7D8140PNFx1FkHPUR7iEafnfKeZ4u4WarNuEm_l59YmjewXr-Ki2onzpKt5N6sdadSP_63mhJPGMf1xCj6P7JagXKdLpNVc7-UCJJa88oONdRzqruzYyOUzponBoU1CpER4o2jSyBda7tqsddr0Afgt2MlRxZdQqMMvcYuMfmH6pybYXJQRKRZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
نیوفیس وینیسیوس‌جونیورستاره برزیلی رئال مادرید درکنار پارتنرش؛ بعد از ترزیق ژل زاویه فک و چونه‌ اش خیلی خوب شده، اون غبغب‌های زیر چونش برداشته شده. فقط این ریشی که گذاشته‌ قیافش‌رو تغییر داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26232" target="_blank">📅 18:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26231">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6aFArK_JWDddE4SbUd30qglqGB-9LKGGnUQc0_mwgrBuNmzOjcfMxRzhedik2pRxdwOxB3Nz_-CduFARTEZXkYDvstzsarFp-f-VK2Z4M-lExOvag4LMK_26iEvHKTyzl7C2emmM_qnGyMTljmBcHss76CYA1kBW4WBcuomEb_D71N7T-fxmI2pM4nqNQS4RoQ3rSE3GIAUfjzJxae3HwZPNuN5DXsnhl8Q9fRvX8ZFtFCgqRcYmxqvpU8oeO5v7DaxWY3A02y2I0dAPa3RNJY4yE-42wDvzam8neskAsYaGqv2jlcWPW-ouVg8VgI7WLHW9J5xQAsQ08KlhtNEVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
تایید شد؛ با دستور مسئولان هلدینگ خلیج فارس؛ علاوه بر مجتبی فریدونی، محمود رضا بابایی نیز از هیات مدیره باشگاه استقلال رفتنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26231" target="_blank">📅 18:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26230">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNcogTY6BDuIeY1_y6o-o3fufF9BbhVVoXLeU2IvbwCCNhK7CIrLPy6q4T2wfT0_tWYi2RW0FhMlkMi2n7Rx2V5fLr_eV04TMPpkQrEVL8bLtBnA4xsvxDaTTkK0bg9B-jRQTBnuMx0qxm4OaVpXhX1wjMM5kFtn219grhWKvDU8TgmM8a8XWGNZCWtMnI4FgVoPq4gdz4m0HdxjShWCg6zPLSbbRLeFH1FOiMsjUOmYEENWK5BBQJrrFYlM28VXbazkTRTte9ykzDJ9BT_LrV1A0xRcBjR4V0JQotJTSin-ETopwXnKFazhGHzfxagFRUkGVkhUvZCLiSWIUkspHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین گلر شش دوره‌اخیر جام جهانی؛ بوفون، کاسیاس، نویر، تیبو کورتوا، مارتینز و اونای سیمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26230" target="_blank">📅 17:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26229">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2xXr6pG_ojDWfvQMnmP3RYu3ipOkznBVwEx3glWohreHmruK96Ge6VSDhVgbkUpVoJR182dY9gYEp9OQpPm_-_XxFfD5P3vTsanwvH8ej31-iwY6VyBhofA8q4fZ7Pv04VzR1kMbLi_MiZwQrN1iFY6jgE1LkDIkcTpjjwIfUO9q8XJbWHg-v9Ieod6rQpRbaSFKfv7wqrAi_uetqflqS6D2v0fSFwoAFqc5yLBGmll1pBvxsjzPSVkkjjqqSit_csOzCF-QJ9aqdCfBvp_DLO1QMCWfqZ5NJ1J23xTgHAEzsr48xxHpP_uDyHAFUK6oLst_ddFYnhjuV5lTmv76w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت رده‌بندی فیفا پس از جام جهانی؛ سقوط ایران و صعود اسپانیایی‌ها در رنکینگ بندی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26229" target="_blank">📅 17:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26228">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3639cfb2fe.mp4?token=DEyZxhhUYIcoAtn4Q0WwBQ9Po5tD0jTIbAho9K9AhtDN1EHn8jhZ0zM5iS1cGl5ian0dJAXQ905bk660QZzgj5TuKjdTN1FxP_orC1Ko1ZxjvCQTEFoMEoN43Ne9Oob0bb9Asdk1Lv8ElMSrD7TzsFv32muxQCjQc9rbFKqoAHGVrylu585Kx8r4mnQlI7ggXKbnwfL6Bax3sUKglw2lYpp4NNN-ygkDtk7GMFxQyGnPrYhp5evIVKGiqbbNSHX-ljeGd3AKsUxNQbx1QvGiA5VfdgAJ4AS4GbTSLhEu8yJBS1hX5vq6UdENR19A4QkZac_T_PaOaWEROmOwhI3sDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3639cfb2fe.mp4?token=DEyZxhhUYIcoAtn4Q0WwBQ9Po5tD0jTIbAho9K9AhtDN1EHn8jhZ0zM5iS1cGl5ian0dJAXQ905bk660QZzgj5TuKjdTN1FxP_orC1Ko1ZxjvCQTEFoMEoN43Ne9Oob0bb9Asdk1Lv8ElMSrD7TzsFv32muxQCjQc9rbFKqoAHGVrylu585Kx8r4mnQlI7ggXKbnwfL6Bax3sUKglw2lYpp4NNN-ygkDtk7GMFxQyGnPrYhp5evIVKGiqbbNSHX-ljeGd3AKsUxNQbx1QvGiA5VfdgAJ4AS4GbTSLhEu8yJBS1hX5vq6UdENR19A4QkZac_T_PaOaWEROmOwhI3sDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بعضی‌صحنه‌هاگل‌نیستن امابه‌اندازه یه قهرمانی ارزش دارن. دفع‌توپ‌کوبارسی تو دقیقه ۱۲۰ از همون لحظه‌ها بود؛ جایی که با یه اشتباه می‌تونست گل به خودی بزنه یا پنالتی بده، اما با خونسردی کامل توپ رو بیرون کشید. این فقط دفاع نیست، یه اثر هنریه.
و یادمون نره؛ فقط ۱۹ سالشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26228" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26227">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ec8c45572.mp4?token=RRUDOXV26rdkDd3ft1mJrYEpnIZdObdShjuU-a3kVxcrqTFQDZvfsILVbvREOie5oD5LTvAwWeHU6m2nww114ptBd8wNOoQTHvmo0KSmfB3LmJgIK3mJQZQhW8TRmZpb1DE-mzuoC-wkcMyH760FnOUuE5qrzIOoBUXEjqEGyly0RB-LkAuytit9IyWl-dafB4-qOUIHf9_HONU51l-8Se34QuO_ZlnPQvVSuHLBt_uaE6LK_nPLNbBi6AzuQLPSpGJnMA2-6yn9Ozhih-QP5gMx8hO_fPV6CefHRhWWXViScaURgaotD5ZBaEtKGuqEnBIvUFgkO46480UHP9pHfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ec8c45572.mp4?token=RRUDOXV26rdkDd3ft1mJrYEpnIZdObdShjuU-a3kVxcrqTFQDZvfsILVbvREOie5oD5LTvAwWeHU6m2nww114ptBd8wNOoQTHvmo0KSmfB3LmJgIK3mJQZQhW8TRmZpb1DE-mzuoC-wkcMyH760FnOUuE5qrzIOoBUXEjqEGyly0RB-LkAuytit9IyWl-dafB4-qOUIHf9_HONU51l-8Se34QuO_ZlnPQvVSuHLBt_uaE6LK_nPLNbBi6AzuQLPSpGJnMA2-6yn9Ozhih-QP5gMx8hO_fPV6CefHRhWWXViScaURgaotD5ZBaEtKGuqEnBIvUFgkO46480UHP9pHfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حرکات عجیب لامین یامال ستاره 19 ساله تیم اسپانیا درجشن‌قهرمانی‌شب‌گذشته؛ چرا یهو کشیدی پایین؟ یه‌درصدتوپ‌طلابگیری میخوای چیکار کنی؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26227" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26225">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8b008c54e.mp4?token=hF6L5iMuVIAHmOMzA4YJnHeQrIwZ0G2rksAawfvNliSkKIGECBn9FEiMbMNukdl0P3U4-VR9tRTHE2fb3YNJDdJiIqXQK5SeVeb8uhIssz5F9n9DyVMOYG6CxjNPFd4lY1dX_v7KqcsoQWH_nT7D5nhqTpw7HlfW_FO63uw2t67s2etIlR3952bb2OmZ9u0aOTh42LZClc3FygTu_QDgLbgSYcxnrB51rSWKS_xSqNE8Z2Z69KUNAzwY-HUaYeKfk0mNkUKNWugrB7iPqlZIoe75mjuuWW8VCj1AJanIouIAUbnh9iEehzJ2dDy3k-Xc5q--zRBMijRgc4gNodZEqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8b008c54e.mp4?token=hF6L5iMuVIAHmOMzA4YJnHeQrIwZ0G2rksAawfvNliSkKIGECBn9FEiMbMNukdl0P3U4-VR9tRTHE2fb3YNJDdJiIqXQK5SeVeb8uhIssz5F9n9DyVMOYG6CxjNPFd4lY1dX_v7KqcsoQWH_nT7D5nhqTpw7HlfW_FO63uw2t67s2etIlR3952bb2OmZ9u0aOTh42LZClc3FygTu_QDgLbgSYcxnrB51rSWKS_xSqNE8Z2Z69KUNAzwY-HUaYeKfk0mNkUKNWugrB7iPqlZIoe75mjuuWW8VCj1AJanIouIAUbnh9iEehzJ2dDy3k-Xc5q--zRBMijRgc4gNodZEqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی؛قرارداد محمد خلیفه دروازه‌بان 21 ساله جدید استقلال پنج‌ساله امضا شده است. باشگاه بزودی پوستر رونمایی از خلیفه رو منتشر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26225" target="_blank">📅 17:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26224">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDj7P2FzO5M5zUMPDfBzy8FPv8uyw8LnCWUnGv7trAi5j98R88SMX_xn_dF00EXcBcMp5OIFcGuMlCDjylF9znWtUGxY9g-dvTodsEE7_anFlLSOl0bkfBToydsvXxnxVLxYwq6mhgXFy-HaJyax4bJ5PDFLKRMd4ZBnQBUcxY39xp_j0pAmchUddbQFoLg9YxyZKJI-KPg0kQ0gvp9OWPVgIXGhUtJ2wi0yF9YzV-QolP8jNmLYUggi9D3Pqt62pK2ddGMDFAQBpR99qcamnjMyaFj4TVLvVwPNGB978wo1lasxgxMJhKBOJCHAI21Z1QT422sI3ikbZt-Wb42wwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
◽️
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه پرشیانا؛ مجتبی حسینی سرمربی سابق‌تیم آلومینیوم اراک که در روزهای گذشته مذاکرات مثبتی رو با مدیران فجر سپاسی داشت. امشب بعد از جدایی رضا عنایتی از نساجی مدیریت این تیم با او تماس گرفته و صحبت‌ های مفصلی رو با او داشته. حسینی…</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26224" target="_blank">📅 16:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26222">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/llfdyVWeLnahi6Cu2kIVtJqhSdz9-3kqC4nXCKIIqkjoIVX2KdfWU_AWHPyTlbh9cDSb574J8sedQVOrm7JexzRjih6zl8FCJIQNeFQbxioYIWKv2Gn5nNBVtzt6jpGEMmqUQ-2nPEWvTuVjRZfMemC6HptVIb5HOHueDuFQUTDLZgvgqEiCxwZenCS3QRiEJg7Sr5Iyx1xpdgmYqjBNdUkjJOfmgucdVqxXvC0WPo_aICX2G9FNLk7CBI0ND171y1IypMGM0v6l0rkvnbDaJP03OuL-BvGLNotPhHtJ6KKj2XxAWVdIqDzzKNYvUOt5H_RKeh-xZ7IZ7TGdQnYlaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ukKkM7kuHWea09F188DIPuJVp5S_1u2neVX3goCdq_I5X7m21suaLDPsEZLGRWFoE_M7PYdZrmSOhD9QcKCQQJSQrnfKH88ZiyWtjzMvFYTHaBOsouHDt9o8_R_RH9WZuAZ45WkJ_nmmSBq3Ixs4s95CvNDGjfisNIRIkUdGGAyKpdyrniGW1p7RJS4I6UFMQ6Xh5hVC0eIlMO9Ql0IWO1QQNLjL8QNjfmxy3TerbSGktaitZnpngTMgD7AMc-KfcmKemDJKSrK34pBjqicyg6X50-6XCA2AAqoNiScLzgClxhkccOTKgHgZiB12yoybBpQxM6nH40xwWtzy_uiWag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
خواننده‌های جشن قهرمانی تیم ملی اسپانیا بعد از موفقیت در تورنمنت بزرگ و ارزشمند جام جهانی.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26222" target="_blank">📅 16:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26221">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8LwtgUXV8tkVg9gW0AKtIg0apyORpoMXjO484hb4iIFignDgTIgEIxRiAgypu5JEnlNooB0OReYTH6enfStvhk9RcywvlirL0a_KF87uO41rdaHD6Q97-r5-j3YlWZaY0ZOOmmocUnVRcBqQwBjEmRbKivRbpSjD1V51E2rryq5lAaSkrvyD4wYb6tUXZt9vJ9MlymKM6SYtzT2Z4tGlVVXXkS9wyAJh7cHqBL4e61rXfP5trK7AqA9S0NvwklTI3jm_r3pKcP7NvVcnvwiVbWYflU4fxfriLfd-zRpT_Cn7n4EkGXyU6Zqp_3Uu7lVcnzL-MLd6aVhDzQmoVuvDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26221" target="_blank">📅 16:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26220">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rknv2DwiBcb_67j4fG6Nz7-Iw1ICEFrdKKDERxwDmfIbeoYE6EGiY-UYhoC0Auj2BfvxqWPXyx3rkZ_HT6biGX81fWYuBPZ4cVc1y_11biUWZzswdcoaiNaDGawdgfuKDSivT9m8AgnkChrnAu_KgehTmCpBs3GMylq0D8gYdXjosk8b8OpAdwVBdyalo379oqBOrwmpa_tZG81IAdQkNN--FC5rPiXFYtlYFJbmfn4V5eLmp2pI03kvlr-4y6Sv6b6bXMFk004_rflf359PZyQobO5KgI0mTkj_H-rWq1N4mgONpr25n3Zkh-Byo4htYBv2jLjW-lc3OMfapfDPCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
درحالی که با قهرمانی اسپانیا هیچ گزینه قاطعی برای کسب توپ طلا دیده نمیشود ، فرانس فوتبال در آخرین‌آپدیت‌خود درماه آپریل "عملکرد فردی در تمام مسابقات بزرگ و مهم" را جزو ملاک‌های مهم انتخاب برنده توپ طلا در سال جاری اعلام کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26220" target="_blank">📅 16:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26219">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H54TkMbvHWY3KwYuROhk4GkXqWYK8Q9g9my5G3EJDUgU5VfflkpN6MrnoEKB2QaPMODdpTjF_fUDuVztyudB0cEjyUqSoKuyP08G1REi-O84JzfclEBYzaYd21qipwOjD4e_5oVsxdnogIYr95Slu5YyrNuEVaWX0afNg-PEcUQMuFzhHycZ6EhOgoZnL5-HPt7_d0k54whoFbZPtTtEbKUpTblCqEh5MFn7eZyQOzh1h4VpTVs7GeBye5mmkVLNWHOT7MUD2qy-0XT7NQQFmTpq_BZk0uWng52TAuP5tYp4m87DQZMVk9tYusYvf-Ngt6YwnjJVg7DbnwAauw5IOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت‌های‌جام‌جهانی 2026 با 655 میلیون دلار جایزه نقدی، گران‌ترین دوره درتاریخ‌فوتبال شد. 50 میلیون دلار از این جایزه روفقط اسپانیایی‌ها بردن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26219" target="_blank">📅 16:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26218">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSuHFqUP9cY417JKgylmxJ52X9QDWP2sEY6GWtu9GxQVHcoIrgkZyBmVv5Dbi5vLfA6ZsYrSYS5JqGsGQgloYcoSZpdJp2zFBGz0fH1H-i8BrcARS2iOsPsI8WPbhMqtqnVZ8X7qcNWgYJflobLAmHMm4Q4sRNw31Wxikgb8Maz_BOItbOh_zH6Fo0bZZwwd342Pylit7jeACMM0dSo6UIzn_k2faO_vpmx5hZtJ2GLWqv01Co95hJWMcUacQhRO2cer10l9rwGvvXYVW1VJRJYBj-EQIN2opiH42RwGXvhgSGITL7vK7c7TucWeYVNRIDwuz9gNGkshc73rN9nBCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
محرم نوید کیا سرمربی سپاهان؛ علی کریمی هافبک 32 ساله طلایی‌پوشان زاینده‌رود رو در لیست مازاد این تیم قرار داد و کریمی به زودی با حضور در ساختمان باشگاه قراردادش رو فسخ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26218" target="_blank">📅 15:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26214">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ND29bHgjiq6n3kSBX_JkPBdrodaKXGXaFkhYZx7I4NXkDDu2wqOl_z9bW3o_Roqwpp6yw7-V5eLFEoyBUnNFbMo93bMRVrLRVpHqbc6Rim1EwYjlLOzg0Kw5JCn8QMmjJy739X2kEUnR5gzL_te12132jtj4CujJuv_KtMsUHWC1HbU163UrHJaLZVvUrIqDOCWyhti4C-dULl1-4EzmmiaNnSnjds69sflfZi97mHKbYC6LpadZLYBxpoBWkC8tC2jeILyA8SXf5bdG2Ej3ZaS8kgXvRtEnzrhBo3vsXyQiw17-bmhK8UFi7s-VNneL69-mADBk9umY8tF13A8UZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری؛ رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26214" target="_blank">📅 15:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26213">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTlFgLkHpUoILnM6A3pOqJpIP46JeB2raaIB_rsvGLuhvms8R5QvQtm-paiSCnSJt4Au2HFEm29AeBpFw_-V26rIKXxt62MR83yQgQfSmhXL8huDtF-MLwjt6-sPDLHOR5xn0cs5r7PJ7EStqikS56IwPfd2lkMQPJZ_qsosDUVzKI7dx-qE2VE6yEnDEVoKcYnmTjkCVB62yPjgwvFJ3AxnBElb-XO8KQeyzQm7d6UyXv1G5f449_QsjXqYsI4GXNAXfgttuItryiYKw2_GPkd3yBU-ycDiSTIBaS6l9Jaa0PKPv7BGEZLuWsmbz24fEydDlTLVdHFgRd8QIXVybw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26213" target="_blank">📅 15:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26212">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvSL5reE6TPsJutj7bE6vH8d5Z-MlGGmIKYwMUqKI-d_Vxm23yLJOYXI12HThjrprE3qa4Tx4wTjHsw0K--pCIhdTkZHEI5RPfEK5RVfrETUR0weds7nw-5KJh6vWv8_itb5gLKiYtPpUirO_NRCui_FdXO7nOGJhvdwF2nyYMR_NX2qK2M9Jr3DD7TEKm8vlLAevXDiBgb-9FGCOXI6-l05Rwfvm8crjAATSPGjs5hKGeh8MHb7lx_9UoAf0DKh5E-9OMZoQu7nuu_FHGG0VfU-yIPYJoMiy9pabUyKhvnCIHv79aA8omi63w14T3zV2TjMTKjdWp6dhX_KiMT8ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26212" target="_blank">📅 14:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26211">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ywl5gPmykNYT4sORep_BqV4w08_vdZPeD6i9rIH6Dj83dL2yr3v6LYQP_z1xQlR9O4pS65yKYbWDmYIFX6uBhauNxw5wZHnZq3wZQu1TN2A81UWAgBNKJ8ehfNNRBYj5XXS-diOaCo5MxLBS4rDOwx2HEl-CVgkjsvGh_aRnMn-IJVXgpKaLSgIRATM2N9Z6tIx1mM0JNZGSx8Delo_mtaTxKfU32RRrwMW3JjJJf1OWNpuHmDAv2Xi8E4HcGhtVA4P992VWjfFw4WAMN7OrXh0MOlaAYniNeUULFZpw86crJFENqDuIXNryaUOQyHNhYomtSstAK8jSL6MDbjjE6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا؛ علیرضا کوشکی فصل آینده در استقلال خواهد بود. تمام‌توافقات برای تمدید قراردادش‌ انجام‌ شده و بزودی‌راهی ساختمان باشگاه خواهد شد تا قراردادش رو سه ساله تمدید کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26211" target="_blank">📅 14:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26210">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXvKyne_ST0qoe2dFHxjuLeqr4CTJoY_RD3z4vvQSkotAADH8Xcl8j7ZAZQe0D9myKSUS1cjbwh6xaY3R0HkhEZE00ya2ensvQWdhaWiHfrwskgVzCaQqFV3b4IR-0lj84FNHieKmwFXLkpHEQEhNAQIkTYmRv6jnnh3-OR6ZjO6tMeJALIBYtyDgi0aA1QM8dwGIsf_eur93WmHmV962CkTbLb8xymzX0rHvLsHi0cC_idKlCTOYrDGuXl1KpeD_hBdjqNCRROY_PC_ee_ySbs1jYsn_gBUla30mSDQsJuLN1vBUUC5kb0DRJs5EDySqW1qAiZrJVkLmOYc28WvRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
جسی بیسیوو وینگر 18 ساله کلوب‌بروژ با عقد قراردادی 5 ساله‌رسما بارسلونا پیوست. آبی اناری‌ها برای این انتقال 8.5 میلیون یورو هزینه کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26210" target="_blank">📅 13:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26209">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcDi9gWXpvauahuWRgJNvQjvmQzeOYnMqxy_TuE6_RA4j4LT7Ki7gBwCgS-sF48F_6OMnedSU6VcT2Xu2juiFu_Qx3yELjX4kVwLoDiVJBVcnP1HDwsImDBBn_mJfqg_MUewCwvSa-pZlUM9TM-EN64E5AQ4ka2akrJ6ONdbcczM5iB7mgE_LO141CCs9SRuo1dIeSwjnZeJNrqTXz8DdxrdCxYv1fULFy7nwcf91A7T3TesLUSAbZijoNfaGQ2R8XbJ6uRBKomkDqHK41BG8GnsHe7XwrewzS-5PezI0pgHUMubvNyJLx8r0PLH7mHRi4iyU1ouPUZj9Uu0DAA2rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری
؛
رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26209" target="_blank">📅 13:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26208">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeQr4i1g0p8xEPlo9mO4dqnu8vWZ5Wgal7vuIHHXl9Os_Mo4SH3baKSuSRG8UtOLm_shHnNoYpR955upAI8RWky4fMuKkgmNauMA2zG933sgrgFdZm5VAXAn7HtA0BmaoOQs4K12tbzks6fyWGuS9ZJxuewwlpx_khrFM1arXmWysF8oCUqu4lfn8BcbvFN8KpcqYPuvoe_jNPCHZEh8SoWGuF5qOwSA4m8e3GeOCafrsIhE5Y4Qz7XOorGICNDXY9niUYF3saljH1rQeHXjtOrHh7DL1K_-qKuOAYdZL1ab8o-VrARZlC3mJ-IxfdkxpY6LL6yf50l2nqKEP8aVQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 10 روز پیش پرشیانا
🔵
بهرام گودرزی مدافع‌چپ‌فصل‌قبل آلومینیوم اراک باعقد قراردادی پنج ساله رسما به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26208" target="_blank">📅 13:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26207">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLi4oNg131gtCLJ_4-NqTYsZrKHh0wICrvpCvw7Y51wMSr-NKXnue2F0DRD_2ZmT6S5gwZqPYI7n9sjYuW7F49cMVp7rfXHURdBmD6R2dKcnHUjtomXdE3BnEWobfYHZBB-BnFtIxgKq4luqkxSxBk_waHsvgpNRfvBOFlKOHbM-UbhBG6czWgsgnaiU6FmuxyehUO30olfi4X7kLIKOU_-MpPT0lp1vdSU7tokNOztKOHnSgwgTL2YUZngrkVjT8jRlyTEYk_gFwEC2Bj2KEfLEB5TyY1ZOA_zruvUJwuqjOihaqG16GbnWR2TefplaD9Ds9P2gpFzuMy16BnPhxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق شنیده‌های رسانه پرشیانا؛ مدیران هلدینگ خلیج فارس از عملکرد مدیریت‌فعلی باشگاه استقلال به هیچ‌عنوان رضایت ندارد و در هفته پیش تغییرات گسترده‌ای که مدیریت آبی پوشان رخ خواهد داد.
❌
علت نارضایتی هلدینگ بابت هزیته هنگفت برای جذب ستاره های خارجی استقلال در…</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26207" target="_blank">📅 13:03 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/A7T-A-rN4FjCOsiK2q5g2jjVdYUh8gKrbIg7EkhcwRuVn449tgbDPToGiYYXRCc8FQNOeztntzN4ye9nJkMU_Tc_gLcUtWf6HSFCkOQ67t9OZRBthTRNspFKmMh9SKteK5yyqYazfSNDZeMiZ8vFAzD-KI0vZe4nC-vtUL0zloDrT-5eEK5j9xaBq1RJ5__85zr685LxXAIEts9htrYiguPynkqot-Uk3380SU-1LHYQMKwjYOCMCR8zNjU_SIHH68a__9DGTPUxEHUNGKEgO6UJwuQn0kv3okfkFu6PSvPqCJ6kz13l5pFpYi-zXN4bcMzowcj9KQY10yl4i9jCKw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 419K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 21:34:41</div>
<hr>

<div class="tg-post" id="msg-30930">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyFSJu2grsxegrDploQKLirqWarQEy77VQmXUaDfb1kDaGvgBvPhBUwfwcH0j3TOJmf-cd5-LenL3K0NAH-Zfd-5xZwHTiTO7AQWD8d8u6E3xTdQlsZool7uSct7V8UFgWYNsQZF-4pr6wt6IE4BRuBgYtoq6NNsx7xjK6_HL-lxJ7snd9LVuHyi13xEjvIVXHY_1AnfYnJR0nK96dt0a11jY7n3h2poZYEIEuJ-wj9itPi--qYyf_Aci14eBS1pp1oah93BDTrRVOzha6dIFp6MZVkRDkeZZGP-cPTSv416M2ePOGmSpiTJjfwUPVplb31W_rVQTT_Q57nAk4Dalw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خبرگزاری‌تابناک:گلشیفته‌فراهانی‌بازیگر سابق به زودی برمیگرده ایران‌وکارای اداریش هم انجام شده.
‼️
درروزهای‌گذشته‌آهنگساز بیژن مرتضوی به ایران بازگشته بود و رسانه‌هامدعی‌شدن که شادمهر عقیلی و معین نیز بزودی به ایران باز خواهند گشت.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/persiana_Soccer/30930" target="_blank">📅 21:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30928">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SSp9l6ktlurAldlk9-RXf-M_RGmBnbJ5VfvN85yCvKov89_FndmtexnFXjKyIP8-8_COJQFWdWAY_0SfXex2dhHim-1nwElLwCoHLsDqXHBe4yc0NVVUngBve-zozI4namUzCHuLnBB3DBrGn8-_lXCSebjAV8lwqkURVd_R30eKxPPoF37ZAmBn6Wwqp4P7rFGHW3g8ekAxAhuq46v6jD8ZvL5UGfQFlGNn1nvhVA2lj1jWAZMYO5V0L1ShPFAHqhrwu2W5v8giKvXj0wpzc9FrhjubeXsOLxRhbGhakOtVyFPlWzuEv2kifcJsmF26rRBkEllZZNZtx1U3XArPBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P89Amd-70BI5B8wRDKqV3XzqAo3ZbPUHBlctUSXrLG7i_TK_nk9BJP1zloTDqbwUyeFowymhk8HVJD1S7eHPi6_OVHJylZCdUmxAzLy_L5zODWC4G9Ow9MHCTcZ5iEsFkdj-o92ASMQHt7Qg1bxyQLeV6oyXEYMTcz9DtqUAAulRt5_XUT-dJDnTMaEPxiDFVzQfk--rGS2cMZ9tRwWehVw9cPv2EQKiPwy9S0v0vYxqmbtI-iDumkHa8XTSFMug3LO_OMD4tml1FVaRTKnfkcB5P5INaBfHYUJVGQu8hRDRO_iZKAtZtM4-CVNvWuXC_dfeBzmPgg62NatAjPJZhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
خبرنگار شبکه اسپورت اسپانیا و هانده ارچل بازیگر معروف ترکیه و فن شدید منچستریونایند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/30928" target="_blank">📅 21:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30927">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/470c5a8148.mp4?token=eCUMHPnggWjvUNBJuHRNFrWxZ4VETf47_vTcnMVErw87FagAJADxm12SngKZBVoU-Tq-KZ59-cl4Nk6tLfk9kYLKx7RaYJp5DQh5p6WbE6aKjh16Oz-qxlW2K6Y6Eu3mBvYt4fyGzKAAXNynv_zk6Rh8bLaCOCwwhWt6uWDLed4hhjHQH3PN7L8QVBLqYOP9pLVdRurKMvY1fEJV-52Wzgl3smDHiBdrRE_UeKA2fDdSw0b0X8_6mzvchqNsLvhBkEpnsnKGtj2Q3qQkpoepkIxdqp_-cYSFknRFOIccMrQengqedUFbGs3gl2RxFdH_TGmfbFORxny6kk52OI3SZzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/470c5a8148.mp4?token=eCUMHPnggWjvUNBJuHRNFrWxZ4VETf47_vTcnMVErw87FagAJADxm12SngKZBVoU-Tq-KZ59-cl4Nk6tLfk9kYLKx7RaYJp5DQh5p6WbE6aKjh16Oz-qxlW2K6Y6Eu3mBvYt4fyGzKAAXNynv_zk6Rh8bLaCOCwwhWt6uWDLed4hhjHQH3PN7L8QVBLqYOP9pLVdRurKMvY1fEJV-52Wzgl3smDHiBdrRE_UeKA2fDdSw0b0X8_6mzvchqNsLvhBkEpnsnKGtj2Q3qQkpoepkIxdqp_-cYSFknRFOIccMrQengqedUFbGs3gl2RxFdH_TGmfbFORxny6kk52OI3SZzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
کریستیانو رونالدو یا لیونل مسی؟⁣ جواب توماس مولر اسطوره باشگاه بایرن‌مونیخ به دو گانه تاریخی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/30927" target="_blank">📅 20:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30926">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00c9ed1281.mp4?token=AIRN-abnXRsf9E3-uMCl-xpabhqdL96D6CIATNOx3jpydIautmFtyZlsQY2Su8J9fSiJq_EBhPaiC4kFWujRBeSuwCdmyBVZ7Im_MNA3iSYkJJb9W-HRxGYyOZjgP86Q8lqVeiSWZhr51eaFVfuvsAg1nnZQ16tQ24W19dR5WEtRhUpw7loow7fe_lj0XvXHwjhm4eH2jtVnooao4A5zLsEegE2HX5vHaZIuJ2qNAjALJVwbfTYnym14cAElitZKK54RCVZuyZ1h1W2AI4ICyqnIXn8TNAhAvz20TjEYiWhmcZzlT73L3aI-jul1nNZDyvd1XCVbSztjkPFKzL0OIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00c9ed1281.mp4?token=AIRN-abnXRsf9E3-uMCl-xpabhqdL96D6CIATNOx3jpydIautmFtyZlsQY2Su8J9fSiJq_EBhPaiC4kFWujRBeSuwCdmyBVZ7Im_MNA3iSYkJJb9W-HRxGYyOZjgP86Q8lqVeiSWZhr51eaFVfuvsAg1nnZQ16tQ24W19dR5WEtRhUpw7loow7fe_lj0XvXHwjhm4eH2jtVnooao4A5zLsEegE2HX5vHaZIuJ2qNAjALJVwbfTYnym14cAElitZKK54RCVZuyZ1h1W2AI4ICyqnIXn8TNAhAvz20TjEYiWhmcZzlT73L3aI-jul1nNZDyvd1XCVbSztjkPFKzL0OIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
حمایت جانانه و قاطعانه فیلیپه ملو ستاره سابق تیم‌ملی از رونالدو:
یه‌تفاوت خیلی فاحش بین رفتاربازیکنان با رونالدو و رفتار بازیکنای آرژانتینی با لیونل مسی وجود داره. من‌میبینم که وقتی بازیکنان حریف مقابل رونالدو بازی می‌کنن، خیلی بیشتر بهش احترام می‌ذارن. تو پرتغال هیچ‌کس حتی به گرد پای کریستیانو رونالدو هم نمی رسه! تو نمی‌تونی بذاری بهترین بازیکن تاریخ همین‌جوری بذاره بره، انگار نه انگار که اتفاقی افتاده؛ واقعا اصلاً راه نداره!"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/30926" target="_blank">📅 20:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30925">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز؛ رویارویی دوباره انگلیس و کرواسی پس از تقابل جذاب جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/30925" target="_blank">📅 20:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30924">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORvVWx51ubthJSkE3Ic0emhjjhcFV5nZGZnQH3amke8wwc1DLEq1hAhqnFslS0DzTzNDMRF5DtXVzmU_DK4EvmN0zbAqb6DFKBSlXx6UmTR4Mr2PQtIT7RucDSrlDN6TehhIEHS-MPjuy0DS6R4b1IeUVBiE2ZgTv4FphTlK4y_jKlY7W6c8U6Yz5SOYXbbB-Fb5x1QZQSOIXxU0qYUZDNL87qqUuod8A9-5rNubv0qtYxu98osxHvhr12wB96qaM55nD7mSK601zRQnm9CGZAyWz1ouZUZ0ZE2TD9EDuSSdvQKs1zzx8aTwZVlGL77nhv1BTQ_dvkerqd-RPeS6IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برندگان مدال طلا، نقره و برنز فوتبال بازی‌ های آسیایی در 20 سال‌اخیر؛ ناکامی مطلق امید ایران!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/persiana_Soccer/30924" target="_blank">📅 20:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30923">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_0Tvv2EEBfferDoubDjDJiZ5lqwiSQCp3xOyRK1h5dlKzUr_Roz2AEJ_fNr-iEymn-8yS7h0R8DG4X-ZkJhUbFl2-omGY7iZzT1ZxpfFBmcj5drJ_6SkdZTJYchI1FUfTpyoYGeqz3ZWD_DNclOa_dEMLqf5VoFMniB5-rfqKM-3CCmllhrlW9MA2K9yydxCh9UWCPik2YtYENSn8IHFinAhHx4Wl_iQwKDkosLJsDM0tll1YOXlBqNlaFwFvHpuZLkUxFpODFFqcJonkzTOVJsWwQJaj0BFFo_5F2_l_O38S5d6N8wjOCwlX73ZbiSmWyVrBf52_ThR0WRyoqsag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ضربه بزرگ فیفادی به تارتار؛ علاوه بر دانیال ایری،محمدحسین کنعانی زادگان و علی علیپور دو کاپیتان‌اول و دوم پرسپولیس به دلیل مصدومیت به احتمال‌زیاد بازی با صنعت‌نفت‌رو از دست میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/30923" target="_blank">📅 19:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30922">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggtQzkOn0kv1u7NnYBTTxqkrWeDNkH8Rl6OG2KoOTW84ERth-ERt8Bd-notL1lswBeEPvAuUpoSaPjLtTnNu2kVqLMUcnwUZChbRNQehr_7iTLJc22wn95-ME1ozgIxvJCe-w3qqAVvoknZxGh-RU6Kplf_tc91kKgGIjtt_P7DvrPsRd9QVxo_zcsrVoyuNaFtGXjIskvIObNSDbFbC00xSLmJ4mjmPL83paulOTXzdq5mfMTDkpqeui1cQjUwHnNYjC28FJbRYA4dMJhHzCoPo_y_iFwAMJaBiGkOrt7X6cVW_yqFlrftY1UGs4931NNwI-11TqntPnRwPGaRrZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه افتخارات کریس رونالدو
🆚
لیونل مسی دو اسطوره تاریخ فوتبال در کل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/30922" target="_blank">📅 19:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30920">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RGU3fLx2jZzU2B5sYK4hMbJCnTGljNAtddJMnPrikhpyJ8P6g0fKzGm8nFF-28wU1ms0QuMZ6JSoc_w-i6PXU3_be1SGHDv--SqwPWCDPM3SjA-8cjZBQVYbXex48Y_T3ZxieduvqMrVg547TBda_CtzzX_Wjy2Di-jTjzOc3GqWVWs-7UOJzhptuJP7w-0u7lNvfCrJewQo_OLCs7pYAIIybWbNDpzGp0fSVGlG6V--sOiv0in_JWC-cpYaiMRBn15YBpic4dKbwZY9KpTt-MLqzGYfMw7sWdG8Uh2_hvCLW4-YmrbwdGAu9frEgfcgdzveYTY6Qxe5Fy-sOf_z1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ueEBMx1bTehqLms7Jjrq3lrdNoq4H7u_Mgozd-PaAUDkAlEO5XnpVzU6G-ax2T-V0S6fYTNc_hpGcZ_7-vcWAshNx0iswnTwQsjuWPs812kJ375T2xc8Q2FqPdjuTqjLgh2bsqFkoRyAOzmk0h7wuaxPHxDb3kXtgz3BdwOlxSFkeTCFt7zgKVrJNUXG7palmt4hNnlYFYM0ToIfAMm1yA-TT0kLP2Xjbf1uDYM1uYNur2vAUylD7wVTS5WXUUBn4Y3SMc-OOUyb4jD7oi5ZKp7Z64-jKgsMPMECqZwzMfbThWd7mLxMNuCXMr7dMIIeQ2QTSlRuH4q7yEvTpmKFWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشک و فیزیوتراپیست تیم‌ملی‌بانوان‌ایران؛ روز فیزیوتراپی رو هم به‌همه‌فیزیوتراپ عزیز تبریک میگیم که‌مشکل‌بازیکنان‌روسریع‌برطرف میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/30920" target="_blank">📅 18:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30919">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcZKhSMZp-Zyk6bdRBVFFKw5NDex2ABt5YW8bZFK5Lr0wlJ_hETvJRQj5y-RCzhIAT_YAOqRdLf0bUx4lXjQ7JeZDrBJpLWFit5-RFJNVEepcujn2aSJgX6b8veD8s66K1GbW_Ehvhs_bQkvEd31Ca4GsqCs4bblelm8_ax9a2050bjBRyMBRuiSt4FGszGHJu-ubBeqal6H7pSR1CknRJBYuBUQ_oVh4MuSqPKzrN7ddxOkXSTZj1JPcic2KBvjuYlSX9lP9dKvx3xC-UPdtsQ85G5VUphvhhwasfcc8GHKqTZkr6rp9WUk9KX9owMAU19a5HCs_LIAHSrRPG7Prg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
عملکرد خیره‌کننده و فوق العاده لیونل مسی در دو نیمه دوران حرفه‌ای خود در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/30919" target="_blank">📅 18:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30918">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSLvWB4jG3tUmvG2I8mogyKPtF1jIGk_tFEkcpGCs8f64lrF54tjRV3an60P9f73k_Wnema807CE2U4mW4P4vWOdTLjSLXJ3kgH0ndAIrHpzUey8H_V2ZfZzFncOa9IfZ-Hs80uJsu0s8WWftnpQansIqKeoMeUkB-Cc0XTVg9UjBNxLn3bW0Cfen9JFe39Oq2Q_FzUz7xpa1_OP6dc922w1jBRLkjQ3QLoPz7MHHnS5tk-VibL351MR37tw1Z4dFChin6a8_tUeILq4-UNRQLropjJroMgdZg1XtV1FfWov47aX999KKYbhiy6Z6EqKrrQKt8Sx7ngbueDfFK8TWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم ملی کره جنوبی در فینال مسابقات فوتبال بازی‌های آسیایی ناگویا یک بر صفر ژاپن رو شکست دادند و قهرمان این‌دوره از رقابت‌ها شد. دولت کره بازیکنان رو بابت قهرمانی از خدمت معاف کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/30918" target="_blank">📅 18:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30917">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4oM3n7ewSpnQ0MM8ER9V_YHO1liX02HZmJlVdsX8E1vZlHyznu-2WDM3hjoxasoYXykvPrDYgcBViDFCvalyHZmkngIvoagDMZSSC0bOxZwYiQwVPmEBEsOgUYyC30hN1Is71675fgUyzEmuLm36X1MvbPXoJCH2vGue3-sGHhFzCehRJQGR7Oy7T0lvQ89J1bSidG7CqvJ2AMOBLF39QyZg9wDfp2vnbphY4G6HygwuvvZKdHmHlgVEQL-Ke_NBY_lZo6gWQp-Jv5YnDOb4lOxgRupQoCCEZOrXnw5IRFe6RHEkGmYXdAzpeEWdGLzhWbOz95JN0hNJ4cnE0zxcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/30917" target="_blank">📅 18:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30916">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aizJZ5_fDjI-fG7Xfv8LQP5vKRobjVSX2zJ-UDM7RplVEy2zmUimnDQvaxIpBblv63GSby_OKurGt6H35FC96ImxqGjQMrD_okFjLiBJLHGVxOGxoMpO6swc7aP-sFMDxRXoBF_P8ajhR11OYeCutldFU-G4ZB1dEbSyE0YbR-F45i3DyoD9M5wj36nVYlu2KVUFVozG3ftOqCMNlLggn1TI9CcaOlFxLKHC5XTnYMXfZwGmvNkQxxL_3tW8_WSAGmWnlhvP7pHbaCI_-4tyuRWGhCRmAWNOYgzk1O7dbJiNaITw9A1r-7pthYAcYWGQe2FnWAwWH0m2LEwxMpao1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
فیفا باشگاه کایسری اسپور رو به دلیل فسخ قرارداد یکطرفه علی کریمی محکوم به پرداخت یک میلیون یورو به هافبک ایرانی سابق خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/30916" target="_blank">📅 18:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30915">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-6cI5rvw_0rnSinnoIOK_lH7ksa450nkTVumOHt8_ulOlAnpwTaUT18VmLzjK-TZLZbOeTo-yyH5d1S4leGdMXOe9mtcLUqaJ_C-0sD8Hau4JCBCXFTu8fMr6yF_2A-OHMWlQ7urOee6FEKv1aUy0KxfrkyGOtEIMs1m4MX2WDU9lIwktLrK4NVjuVsqo-Z-O2uxHFaTUiLaz4DXJ7HQrr22GPrkMaL7p3CtzuyftkVwV-3TwC6HuCruZ618bMWOnkeeCCo1clFtIQLOKH-rOy074L3nR8_9tE6wLTa5SqN5sMZW8_QybXxhl_Tq9OxAET4dj9WlKMTOmMxmonk1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ رائول آسنسیو مدافع رئال مادرید بدلیل مصدومیت تمام مسابقات رئال مادرید در سال 2026 رو از دست داد و از ابتدای سال 2027 به تمرینات گروهی شاگردان ژوزه مورینیو باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/30915" target="_blank">📅 18:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30914">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_dEsuExqTADbOsfir7HQLGoEeXCiw0Tl6p_PWZj8Kqwi7Ibfnb7O4y6S2ulF0NZNxjNgkfgR6B9lxGYhydczs7oObETLHdOfw1Su-_2Z8DJtjBpjMi6UPjQOinhrFLFfs6HqcflTArOpZFznEx4lV4NMJcW_to0AETlclsN1YC9xzinthvTOTvi_Mg5-k6iZxo6BpCIVNgP5MY5QY7_9JY_91xa26jHZWlYDKDz_g2LnZ8Uf-V4qsa5zak5wfsLqnkoNkOGD0kyvsllBVmz7pSkeX6ae6Y-qEbtZow83nLgRZrwAXYI_6B0nBP7KNkjbcTG3xxg47GyxJNDrGTQfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دنیس اکرت مهاجم 28 ساله تیم ملی ایران از طریق مدیر برنامه‌ ایرانی خود علاقه‌اش رو برای عقدقرارداد با استقلال در نیم فصل اعلام کرده و درصورت تاییدیه سهراب بختیاری‌زاده احتمال آبی پوش شدن این مهاجم ایرانی الاصل بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/30914" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30913">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETI8vOQ-R7fA-_lqCPr0plthxD6mh8nblXfdGue19gQ6iwTrV2vvja75hIqoQGZLT80ijFP4CUyRzlFTlTmdFKr48TMaVZqfzPy3OcMZE66sm_3NWllMp4ZWbH2FRr_9nPTC6j55smCZFNhpy7lG957U7kNHy_e54iSk8w1OW9BkqhJwCccg2ZHINa1G6pAfs6wgue-3WaflkaZO2PinK8FXj2OH-DdukFS3G4ezhlN6k93YUd__xL7OJTa71oNeqdMxECP-vh7DtlNw3upQROA3yn3CT5yKV-FzRPTafZ5nqs0kyq67Vyh271_ud9j_viaWRFetEobsVDZhbLfLnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه فلش بزنیم به این صحبت‌های تلخ ابوطالب حسینی درخصوص قیمت دلار در آذر 1404 یعنی کمتر از یکسال پیش + دیس به امیر مهدی ژوله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/30913" target="_blank">📅 17:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30912">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyK4QxKNzE8ifPKcPdBZ_A76_CN1X0r--amyfRlJBWFvYliW8m951GhMjbTZy7dUk_LzKntMygjLYDtyeZ2dS796WjNHBJ7QJUycxLnmLLTLwVAqqWIL0CcauS7j7PPQ41wwsQ0ToCW57fikJSrjjpgvUC-mcG4jWrkcyO97tE7ySMnl0Z1BamM0fW2OdmhNboSYXWVGOWZTz_4y2MlCuhmhosurCKEKwDBpUJPPHwUstdsBatOWEuOQjDuUie1TtN2qj383UADF-r-WrwyfMNDc2CBg_7vIbmlVMApzu4KjWLmEpRuN-AuwfD61nXiyeP-uWE4qotCyqRyo3Nu55A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
هر ۳ جام‌جهانی‌که مسی فینالیست شده تو گل، پاس‌گل، دریبل، خلق‌موقعیت و پاس کلیدی نفر اول تیمش بوده.‌ توتاریخ فوتبال حتی یک بارش رو هم کسی نتونسته انجام بده چه برسه به سه بار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/30912" target="_blank">📅 17:01 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30911">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfXsLfL7swFE1mVgn08Gf4pNkTzhjOgvPIIgDlDtE-KJTa1RyIqT6yTussmEcF7z7ni_juMqd9xYqlekYhiC0DOc-VSKR5lM5UiXRy5iKTA5k3tSsIIoRiC6lkpmo8KGF15z3ifA-7xN9FoAHTQpOFzR_GBshALON7sbQdtdid1P6q1HtZbf7pHyYIiVmYfUjTvhz5OsZVtKQlapl3ieArdUy9FvxzMYgzG4TFBWQb4MCEGx-gDuxoIMt72crayDsEV9XZGJVRV9J8DQTd20W5pTcmfG3JuaCq1cGfz753pkJZZtZfAk0Q-KE7was56veIJptXLizoEyK7Pxv7wYSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
انتقام قهرمانی آسیایی از ژاپن گرفته شد! تیم ملی والیبال ایران امروز بابرتری سه بر یک مقابل تیم ملی ژاپن قهرمان بازی‌های آسیا شد و نوزدهمین مدال طلای کاروان ایران روبدست آوردند. البته گفتی است ژاپن با تیم دوم خود به این مسابقات اومده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/30911" target="_blank">📅 16:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30910">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8339ec657.mp4?token=jVQxuro4WasO7H1qynQupDlULkMOCTC-X4x14P13Vf_8BiwC54iy6lTt6F1N8oF3pAgA6LwZhAEdoQIXrNQ62B4iGyowgCjgMueqPjLcs9g9ERs-PzJSIGU1BXgfyuPAW8_cV15Vk3O-S6lptfVbUpHu1Jb-2uItlx7yz6CB049IzHNybf8xoB-YOp1Ulfwz9E_HT5V_0rDVJ5JfNavbOPAbULN2KQx2EAO7alduQZvDa7TyFFkt4xT0yj-ReBWelKvb4pPbHfAycVjYd1UkHYphkEutNRRgP4VvuLjgJW-CVa2Cl36DlDBS8jhiWcJ28ymifTj8CTDcXxNkKmvpPBMNa8zEQrA8ynR0Q5JDq8EegZ-3AV1Ug3gQWUt0ki4vIvAhk7Rc_u9G4AA-VjxOaXz-pHGrXj9FXLOG_WFVNk4Ob-jxQbK6JY9AVwNZDyNTfFuzuzJSBMuSJOwKvn_rS1fW5BmOXzRTEysDHsJNf5KVtsO08MjERbBjknBqLlFcwYAYkJqx5NiKVbxQJHAYd3gflHq-tUpegqtwZtNBA6-gd2aW5Fq3itGmXSpXtE6do2NWEvvkHyRrPut_wRTsWNegJbTtT40hSLy1CZoyS4RyO3iAymUYhN8FxveIfpSwFVtI5gaPROfOAKuI7eFMT-6-k1xha4EsSQJ0OET-H4E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8339ec657.mp4?token=jVQxuro4WasO7H1qynQupDlULkMOCTC-X4x14P13Vf_8BiwC54iy6lTt6F1N8oF3pAgA6LwZhAEdoQIXrNQ62B4iGyowgCjgMueqPjLcs9g9ERs-PzJSIGU1BXgfyuPAW8_cV15Vk3O-S6lptfVbUpHu1Jb-2uItlx7yz6CB049IzHNybf8xoB-YOp1Ulfwz9E_HT5V_0rDVJ5JfNavbOPAbULN2KQx2EAO7alduQZvDa7TyFFkt4xT0yj-ReBWelKvb4pPbHfAycVjYd1UkHYphkEutNRRgP4VvuLjgJW-CVa2Cl36DlDBS8jhiWcJ28ymifTj8CTDcXxNkKmvpPBMNa8zEQrA8ynR0Q5JDq8EegZ-3AV1Ug3gQWUt0ki4vIvAhk7Rc_u9G4AA-VjxOaXz-pHGrXj9FXLOG_WFVNk4Ob-jxQbK6JY9AVwNZDyNTfFuzuzJSBMuSJOwKvn_rS1fW5BmOXzRTEysDHsJNf5KVtsO08MjERbBjknBqLlFcwYAYkJqx5NiKVbxQJHAYd3gflHq-tUpegqtwZtNBA6-gd2aW5Fq3itGmXSpXtE6do2NWEvvkHyRrPut_wRTsWNegJbTtT40hSLy1CZoyS4RyO3iAymUYhN8FxveIfpSwFVtI5gaPROfOAKuI7eFMT-6-k1xha4EsSQJ0OET-H4E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ امیر قلعه نویی به فدراسیون فوتبال تاکیدکرده که افشین‌قطبی بعنوان سرمربی تیم امید انتخاب بشه. درحالیکه جایگاه خودِقلعه‌نویی محکم نیست و ممکنه هر لحظه کودتا علیه او آغاز شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/30910" target="_blank">📅 16:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30909">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7722f37ae4.mp4?token=gMalPQaWLG1TjUmlENadyZXgxqwJZRe2xEo3cOIUxZYOP5W9rg43UIzEMPyY3pKdmBtpX7E_bDzCbGr2SaoYZ9KVg8LFUvyjuP-S0vwmA8v6L_ae_h4q9sx8EusU9OG2Yi7F7JFr5onjzM330hfKWzUcRJWdNmaAqS2embwLoM4hRoDRfX0J0rwIUEbbVQE3jeX4SSet12rSdUzuI52yPD4ARRTKuhLcRVBYrrgtYTWoBaQbUouOp1m_xtOUfraunOvZQCd7Q0-Pv-A_2WUUd0CDZs_8pbUKlDrcofq6WplftbyhchNhR_XDrHi2Ul2w2bQtTuLLZyNmgPXU1deQsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7722f37ae4.mp4?token=gMalPQaWLG1TjUmlENadyZXgxqwJZRe2xEo3cOIUxZYOP5W9rg43UIzEMPyY3pKdmBtpX7E_bDzCbGr2SaoYZ9KVg8LFUvyjuP-S0vwmA8v6L_ae_h4q9sx8EusU9OG2Yi7F7JFr5onjzM330hfKWzUcRJWdNmaAqS2embwLoM4hRoDRfX0J0rwIUEbbVQE3jeX4SSet12rSdUzuI52yPD4ARRTKuhLcRVBYrrgtYTWoBaQbUouOp1m_xtOUfraunOvZQCd7Q0-Pv-A_2WUUd0CDZs_8pbUKlDrcofq6WplftbyhchNhR_XDrHi2Ul2w2bQtTuLLZyNmgPXU1deQsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
فینال‌قهرمانی‌آسیا؛ شاگردان روبرتو پیاتزا سه بر صفر از ژاپن شکست خوردند و قهرمانی ارزشمند این رقابت‌هارو و کسب سهمیه المپیک رو از دست دادند. یه زمانی همین ژاپن آرزوش بود یه ست از ما ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/30909" target="_blank">📅 15:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30908">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5YK9UsCTHIXfV70VqYNgvnXybzf2CRosT7JzESqerVEG2Qbdzwi9Jm4XijLKFR2IBmRCXgNR9CVCZwCo2DZryppctnaPGlICoq2xxO9IKjsIPQ865kHq90HuhcytS34uQ5_mncclfwrgSISB7SzciNA3_Cmh8uzAkfUcuX4MobNqc90Kt-CvxUuLlVZBaL4QmdwXiKlTaT6Xdo4uducoz-fcbF5un8jxQ3eNTt4TKu6FNaKFrvfCropQwASpEL84P7RHWtKfR59tVy3tgc0Y2aWwymhhw8Q5iSl9MTP0ng8e89-VnzthkOBmJfv_M296zzPVSvMg6otAx1LOtKU0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باصلاحدید سهراب بختیاری‌زاده سرمربی تیم استقلال؛عماد زارعی وینگرچپ 18ساله‌آکادمی آبی‌ها به تیم بزرگسالان پیوست و در فصل جدید با شماره 99 برای تیم استقلال به میدان خواهد رفت.‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/30908" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30907">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhBdqkxEEktanFJLiQOlnWWHRL_Yh3PFj0h8YorS8_4AvGkW9DaojxG9QWNmutkoEggyCpR35qnno0HGm1LfVEM7u4vONDiq0d_1dEn8tvJ0i-26iPa-Agm8YfHeUJoJoMGe5yfklEIW-GncVmNOvZlmGlKMMKWWx5MVqlMTgCs3d9zreew57aoTvCWUvnVdaw0unpEiMmBp2y2OAHjAfXk2vr3PTfyagNL78ikI3Y1Z1Upa-jKvuYBGaD5FXWvujHIRes_c-xEAzDSbPMhTjtTvWq3Lx9u_lz9QndGXV-A3UjbrAoOAFhaavmCCtXUVi9YPi5T2mIo4FGQT_vVVew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درفوق‌العاده‌بودن رابرت لواندوفسکی همین بس که تعداد گل‌های ملی‌اش از تعداد گل های ملی کریم بنزما، لوئیزسوارز، نیمارجونیور و هری کین بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/30907" target="_blank">📅 15:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30906">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyLmh0U6-uQBQMRbOBXg8_fQu602c564UaJEJpHtmXCLPIxifMM7RDhDcQ7-boGvvfiDBrrexXyuyVuKmNKgOy-gG3Dz15jy7cgxwxWMx8UaDqKnG-j8ex5ZkuHGIyUFpbsMH3Jeosj1NloESzsdrZkO_K1PXuGmquiHmrHE96YZ-u1q8VUlzfJZ-bXXiE8lFzA4QJ9FatpNjvz_ZdWdGQD95c_ZobAQPhG-VpYiCV6PTz_earQRrXT4zKROhaLm3ViAk98tJIT8abH4V7TSaO0t6aNnIxpYF7w8FQWvbWvzE7LADzu2QvLtYuxX74BiGL4zhMVfMbrH7svSkyQ3tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#تکمیلی؛ 10 گلزن برتر تاریخ مسابقات ملی؛ کریس‌رونالدو و لئومسی اول و دوم، علی‌آقا سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/30906" target="_blank">📅 15:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30905">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36e69e0420.mp4?token=APeZnW9DsEQKjgZbR3Jh4LGn_-hgVBnK2MhdOv07JQRh72uBd3jRlp2BL1Z8LfTKbLD-SDuBedaijC8VvpGRT0DBYR-NaQRP-vx8f2k7JIfFX_raauMyM9LVSMvfSuR29wZKlD2hi9gp0qNaju92QXCEYt0tsjkQ36LCdeiNJ5bzGRRwy2awwJCvuwGC_aKOhMlFx4G-cl2JmSPSpo8RWA42zf_TmMY8P98KubbRmy-3rk2Z_KwRr6pdM6oOjl7Zsj-YVsCyb3CsuncaRarFHLKr-1MDuoR3i58lCQHfIEirUEkjDm5DZZEgC2V4DA5hL6AmQeulxTgyQXZGjUOdIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36e69e0420.mp4?token=APeZnW9DsEQKjgZbR3Jh4LGn_-hgVBnK2MhdOv07JQRh72uBd3jRlp2BL1Z8LfTKbLD-SDuBedaijC8VvpGRT0DBYR-NaQRP-vx8f2k7JIfFX_raauMyM9LVSMvfSuR29wZKlD2hi9gp0qNaju92QXCEYt0tsjkQ36LCdeiNJ5bzGRRwy2awwJCvuwGC_aKOhMlFx4G-cl2JmSPSpo8RWA42zf_TmMY8P98KubbRmy-3rk2Z_KwRr6pdM6oOjl7Zsj-YVsCyb3CsuncaRarFHLKr-1MDuoR3i58lCQHfIEirUEkjDm5DZZEgC2V4DA5hL6AmQeulxTgyQXZGjUOdIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز صبح بعد از پیروزی مهم آذر پیرا مقابل یوشیدا از ژاپن‌هادی‌عامل‌حواسش‌نبود میکروفونش بازه و گفت: ببین یوشیدا با همین خستگیش حسن یزدانی رو چیکار بکنه تو جهانی اگه بخوره بهش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/30905" target="_blank">📅 14:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30903">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMuol1bzq4Dbbmr6Cf6K-nDJV8MwmIYFduZm9q8wJQcTXJoUSJe_UEr49alWrTbAJ-ftHixdhVn8F4nkyXGy7nb7Jg9figAaCV8nYZWNNn6r4bt_8jHacqPM32dxMpF_DqXf4MAQHBuBCddoQ-BM_VuBy10KodqfVGGBoWNNjczyF9GQ6ILkdIkl4pUhcY3msZlX7qd5GpSuuw30A6NF7jmUhjGTsFVbwapTDVLae0hhc2T980vnX--enU_kHSrMH-bqiKOZUCQITC1VDjFAOg0fLgFbjdTexcfTkTbVf4_vAlWhBcZnqkeAj4IrmgCszzgCmF5f0musLgx21dz_Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌‌های خارجی معتبر پنج گلزن تاریخ رقابت‌ های ملی رو اعلام کرده‌اند که علی آقا دایی اسطوره فوتبال ایران در رتبه‌سوم این لیست قرار داره و تنها کریس رونالدو و لئو مسی بالاتر از او قرار گرفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/30903" target="_blank">📅 14:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30902">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPoh6nTTcNumjx6gFsdG5o64mwTX55ZisSyYQaGisPrhKHn26BGXTtyt68mRE0jWo2aV0fPnqgcN6i9wIleI2IhFZDk4NXRBbhwPj33eyPlfdLv8nQMyqdAoXBvvWfP9iTb_DSyMS51MnqKIrSdD0-UwXDn51HPS5A0jvO37RyVPMNNgc4fsRnHoGq1tfY8XNRmHCByEhMH4L6gaDmMroYXIvGlp8325wTK6lu9bRglhVSazSvUTyojhONBhibiqhmtClMXy4jMBABwKybTmbJpfkcMK1eY3EZad8q8rGxcaR4sbbOUyXMP3St23hhaXon61lD237H7EDWewqLDAjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طلای آرین پایان تکواندو ایران در ناگویا؛ سلیمی در فینال وزن 80+ کیلوگرم تکواندو بازی‌‌های آسیایی ناگویا طی‌دو راندمقابل‌مارات ماولونوف از ازبکستان به پیروزی رسید و مدال طلا را بر گردن آویخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/30902" target="_blank">📅 13:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30901">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOwJODr09uN-wbQDDUEwVmqfOEh5GAMbcRJdFfdS9qtj_bdLDYSpA_HEMYn7QaX8XdguDSulSnVgqi43PboQatnYRTg6mn1UKr8_pSRzSeQLl866r23LGaICCGWDgQ8q6ZhyRMy17spgjIZTnjt6QatHuNQ5K0PlxzQsDkDSykzzdkQUd8ViznaQgb6NrA9KvfN8duPTJ_nOY6aDyBKnGaZEUX9NH0U6xK-kbKXgVZpMvl88KuRDCwFKxRXCZfryimULhRPihb34V1MP5fGOvJl2Z3jTVoVlP2mUJkxlz7yx0_6_lZbKz-JfvsDndrW_aeQGKITcOQLANhim4_RiJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون فوتبال سرمربیگری تیم ملی امید رو به افشین قطبی سرمربی سابق پرسپولیس و فولاد خوزستان پیشنهاد داده و درصورت موافقت قطبی ایشان بعدِ سال‌ها دوباره به ایران باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/30901" target="_blank">📅 13:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30900">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlN4spphox9hAYhKjEldzyuSH_XkmHtTbP7ywZr2nWosgXQk4tS6FauBVP-WBrutYVU8jjyUbG08sHYDiOMAiuuWaeMBiX8EpEnbsGaFpxOYolirNjgXnK8TivuRkibpAxlqfXmFCNrVoJAq5rNvJI8kmf8m6w0bfM4eZ_7BBV6LbSvbPkZMR-IbM0lxLmL0QdcuCs9vrdq_meMuVE1NJsHHq5K1erGSoGkXKuLyYxrY3IyLf7dNCwzQLpY-GrXndcMM5YO1qpII3415xXXtDRraCIAETJqe177IsKIFc5JNS8hJc_cErdYdcRG23JWAWtcTt0rhAYB8QbiRKQsY9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ قیمت‌پلی‌استیشن‌پنج پرو تو دیجیکالا به 345 میلیون تومن ناقابل رسید. خرید یه کنسول بازی هم برای خیلی از جوانان ایرانی آرزو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/30900" target="_blank">📅 12:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30899">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOryZfh0RIDAYMVqMzr1PVtfTNfv1rBqTQOzJbqGy-O3Nsf4YfGPqnmk5YdR-2xp0Jeht2ySwwz8YWikyz5Bp8aNy3VPm8AyrWYfY_yriFfoqQByrIqo2DacwTn6zUDcydz4zjcvD7mwwGXX8uUnxFKXFmLIaYkAKXSMVe3grtWHEgHwsX-hPHrv7dcGggOaZp5D7y2g5Mlej2ocXRJ0_4x74YBWgesAcloKy_aWbn1CmTBtcNBzwbSJHFTDeOkKXejOXCEZRcUy9nGg8mUHpOwENx8An5OmkWAFqcFN4lf9YctJCEB4mvS_3dC_r3mqMk8DKkEFJrsTrhmLfuhTzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
گل خاطره انگیز و تماشایی زلاتان ابراهیمووویچ ستاره سابق تیم ملی سوئد به ایتالیا در یورو 2004
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/30899" target="_blank">📅 12:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30897">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
حسین ابرقویی نژاد بازیکن جدید پرسپولیس: باعث‌افتخارم‌است که هم در لیست کارتال بودم و هم هاشمیان. تلاش میکنم بهترین عماکردم را نشان دهد.
🔴
از بچگی پرسپولیسی بودم. مثل آرین سلیمی که همه اهدافش را نوشته بود سال 98 تمام آرزوهایم را نوشتم که آخرینش پوشیدن پیراهن…</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/30897" target="_blank">📅 12:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30896">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plSgy1NKUpJWHTAS4TVgJq-km8KGTEh8dnWWrMBrVuwk4i98ZQYX2o49bYrUeXsZyKF8cjk6stwIRGEZN5hULe9uPVmpAfKP1IbUbz8xqXXjeOb4325UNOJO673BmvjytczwrGYKjG7G00TBDWLUN1uOo0dgwCa11Ub43NIq8Pcy_JQOZpGvZRm364qcp6P-dorsZy8sjgT13Z3Ho7any47cV_VoAAl_YqLIWaBsn0QdWCOggspVEX4GFTi5lZ_eOt62oFjKRqd-hneltG3VgmJJL_dZu1yqrTe73yx71yW1K8xftZh6eS2eaFK2D6ZSb9ZyXTq2hiP-WxVbAlrjtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیرعامل باشگاه تراکتورتبریز عصرامروز با علی‌ کریمی برای‌پیوستن به این تیم جلسه خواهد داشت تا درصورت توافق نهایی هافبک سابق سپاهان و استقلال شاگرد نکونام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/30896" target="_blank">📅 11:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30895">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a63af919e.mp4?token=pe8SZDvjMgJ6W6_ZsPNR9q0PnBwpB76feIxnTmbZuzaT5rEAcF2LSnlp55mA3Kxjxq_mfa5ADs8wAMY5j8TtlEYr4H0Y7sVJmAgAPziO6SrwyY-aEWtTf6-P9yM-33MeoO8dcx7jWLym8VuJVKazDXCS6l7mYD7I00hPO0Fp626Q8em0rPtfAm2xKR3Ff42Mb1uaWD2YOJO9wxns77khBa3ETZnmq42kC3xf54mPJiRakefKANK-WXPKlfHNkfN57e1TqKQM8SZt5wCbon7JQ4ancKJVy3-0GOZ2Rl1XKouwfegIcxK51Ya4lPZGiM8qajQNhKUBQWwoNIjiIom3YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a63af919e.mp4?token=pe8SZDvjMgJ6W6_ZsPNR9q0PnBwpB76feIxnTmbZuzaT5rEAcF2LSnlp55mA3Kxjxq_mfa5ADs8wAMY5j8TtlEYr4H0Y7sVJmAgAPziO6SrwyY-aEWtTf6-P9yM-33MeoO8dcx7jWLym8VuJVKazDXCS6l7mYD7I00hPO0Fp626Q8em0rPtfAm2xKR3Ff42Mb1uaWD2YOJO9wxns77khBa3ETZnmq42kC3xf54mPJiRakefKANK-WXPKlfHNkfN57e1TqKQM8SZt5wCbon7JQ4ancKJVy3-0GOZ2Rl1XKouwfegIcxK51Ya4lPZGiM8qajQNhKUBQWwoNIjiIom3YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زلاتان ابراهیموویچ درواکنش به‌خروج کریستیانو رونالدو از اردوی تیم‌ملی‌پرتغال از رفتار او انتقاد کرد و گفت: نباید میراثی را که ساخته‌ای با غرورت خراب کنی. اینکه بدون صحبت با هم‌تیمی‌هایت اردوی تیم ملی پرتغال را ترک کنی، بی‌احترامی بزرگ است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/30895" target="_blank">📅 10:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30894">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gR8veUEvbEVBz9qm9plTEXnGCMoIgqC8ZK8V5_xNz9U2fDT85ehN39mTB-DXd1-i-vo6pmrOrDBpfUE7MCZ3EkG1oWNryotA6vmt0DawyIttdG6bsdSrzIoGD1xh0DXBlrttAe_-ijzKtl2Z-cLG4kLpkQPT7mlyTVqateKLfOWKyYgLf58gp2FSGZTM_7Wt60Wo3IVeeXx6878MIyUr7bbsME7Im0LhrY_xGg87bfPoui36J5ghFakm4-5o_ZY6Vc_iluqZNML3h7IeK7-1S98LhLBTWSIruM4zcqXjwMNIykdvkG7DOQcdopd_VvLf26KSQHsfV32uG3NHVv8-DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شنیده میشود که فدراسیون فوتبال میخواد که یه مسابقه دوستانه دیگه برگزار کنه تو اردوی ترکیه. اگه قطعی بشه دیدارهای هفته هشتم که قرار بود تو بازه زمانی 15 تا 17 ام مهرماه برگزار بشه به تعویق می‌افته. یجوری دنبال‌بازی‌دوستانه میگردن انگار این دو بازی چشم‌نواز…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/30894" target="_blank">📅 10:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30893">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgQrWhqTsrrDo1lUp3TQvGJ04z_Ss-1uKWOiOEQLcbIDu7qcIq1II_gkstYeoiXmROv3fz6yGkYcRdKf7za4pOIydD9iNL_wWHOG5e5sa84sodQJz5nY7h0HksFf_1TQdS7aUFO_clkdqST7JOEZmxPcNBQu9FOJyq9yAQUaA-sK2kduMg_Ila1kvFpQwnRI5ddoF5fct5PYfcsdo-QGPE6UT1BVVQ4-z90uluDXk49yzpw-fvmo2HE4ithFJvAzJHa85GBAudjQs51segqjDc1Sg9qpMD7Ojr8YWGM4iQSinH7n2MXv0Y3b87BEWUhTMVaZXNjoZSZmfwgoTqA8Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه
آاس:
رئال مادرید توگزارش شکایت‌اش از بارسا به یوفاگفته بایدتمام جام هاشون از سال 2001 تا 2018 ازشون گرفته بشه. بارسا تواین‌مدت 9 لالیگا برده که تو همشون‌رئال دوم‌شده و اگه این پرونده به نتیجه برسه 9 قهرمانی لیگ به رئال اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/30893" target="_blank">📅 10:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30892">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from؛</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6Lp9KJIkWkk5hGhdLQhWS1Vd86Mdo8WlEmCMkFtWJib6OBY5OTVErc1xrlRII1_t0YQUJlNeXF4FYJEwoTyfCYmpgaSHzOnPLCGRaBoG1l0K96arXzI5b970LehqjMHQAMAj6qFujPOzAlxI0H1dOPiTMQ9UyGztz-kpjI_TMTtveXl0jY1Cm1BUoN37N-5ltwi-lewA01ELCMSXd-m5N3yw8zw97aDwJmXIGip_vVL3tHnJcU9I4GnsXq_3zyd9lf6pc1tR6GZ9Kgd5WweJZPAVvfhQ1FP4Plun3FV1lEqbQiumMKrCwr9DjCbsHfGWTd3QQlo7ZxSrxaxwlY9Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لایو ضریب 2.0 دیشب که به راحتی برد شد
✔️
✈️
@best_form</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/persiana_Soccer/30892" target="_blank">📅 10:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30891">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9ae1_N2aBm6bFSQwlmokTK4A3mneNmGpC9tAARo3rSBdQzREQHTg_1O9V0ATzhz8lGnlBLsXCMfuGKyrCpfMiUdg3hLS0FyPDjn_u0chicMuMKRBzZWS8-GHvn6eCkphSjrvtk4nFVhQLED4CPdFPpA4dqnfbJl3pBF8iY12DEuJpdgjIw9sWzjfd6k7eHu108-6O_VrECkUrtWtNPBoeUbcKCen3n9lOgQVEk5MJOppi0SB2spZvu8h2bnmIy77uWrwoj3dn_R-ya7LHF-UVJ1Uepd5ST3gbR5Kt8zli7OkQoFL-SxsSg9wWKAiSiC09vpsyhnsUrKwkT3Bt-29Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
10 بازیکن‌ایرانیکه سابقه بیشترین تعداد بازی در تیم ملی ایران رو در کارنامه خود دارند؛ احسان حاج صفی شب گذشته در صدر این رکورد قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/30891" target="_blank">📅 10:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30890">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kn0tZbq5XfiyVqYWdjuzFOILPKWV79-f0IZDRTb9GMrZrINbC8VJVGm2o9UiCMKxLLIn7luDB5-gBvcbQGVYl7RtuGe6CgYMNGZp0Vte9rSTDOT5NF-tzVBXUuZCqNXc0TygwGSZ5ysHK8JpWd23Rup_Jn9Q-gMzGK1cfSgcBqu7uAt7Svt0W1XInNyZUNLq0TUdZxtTcl2T2Iisj6WxqzcWZU4FNqiqXdRb7LyTmkydHHtIJDy7HGHXKgdl_9Cwj94nzEdrtHxVlXbos9aaG76BVGaouZxkpOtP-YOjWpwFpsaQGKlWn3-xYRO2E9UC3ckEqbBwyPLbbMNGwkSzug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ترکیب‌منتخب‌فوق‌ستاره‌هایی که تا به امروز با هییچ باشگاهی قرارداد امضا نکرده‌ اند و در مارکت‌بازیکن آزادند. محرز یه مدت با باشگاه الوصل در حال انجام مذاکره بود اما به توافق مالی نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/30890" target="_blank">📅 09:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30889">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8CRi_8Q2ydX3dornaFvrQWkyp-EZM8P0GrnW7Izo-UxxeBGBpVfUDjzLnl9Sw1yNSdAq3s13_RbNDHmdrbPn5k4qAuanji-pC1QpsxbYr-oyzKCeAF2DicMNz28Y5yIir-IGZu1Oqjg6-Bg_L9dZOCtGLJb7lGwgvZWZ8DY0T4Il2HG5-Ri5TFPFHJeeAEQ24LrHlJkm6qJZtovmMkprtKWPIuWggYeZwKql95TIhFm7EAidVEMzQ7RTyoqOLBibJbJTYhthdiaq0TSl_9q-KbOx84NIyOK8updnT9SPJWx54GUaVgE9k7HLvUum6HEoZbV-OuTrpNLX-mlLyVubw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین رضاییان که‌چندروزپیش در اردوی تیم ملی جوانان گفته‌بود که من اونقدر حرفه‌ای تمرین کردم که هیچوقت مصدوم نشدم تو بازی با روسیه مصدوم شد و ممکن است که چند هفته‌ای دور از میادین باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/30889" target="_blank">📅 09:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30888">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7fabc89fd.mp4?token=aR4bgY4u7QqSyHjHb0zvey4YEzMlx0R5G73Er-1A_o8eFUFP882hTTGPgHqqTKTT0kpS1mxwV-XFLEUAqu3ij4luR68XEZ2AO_GQVRb4MWluDwvmkKlvq-j4qL8zJ7MjiBLrQdSlMOxWH0021UzUqhkybEyj0_58q4cqIsDPEThvoYQO26-9vkzEbDHPTVup5sGK5aWWsEIga8zxT7R3pd0nNoNFoIv_a9r422bx2g1sO5PlxjdakyBnIliRKDRrTk3OVnzbO5d2tEQ8O1phJgYosp1U1ykMF-rR5PWLBPsUs0Wx5IOGgPbNMCE1fdI0ktdtwszug1NEUEpSgN6Lqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7fabc89fd.mp4?token=aR4bgY4u7QqSyHjHb0zvey4YEzMlx0R5G73Er-1A_o8eFUFP882hTTGPgHqqTKTT0kpS1mxwV-XFLEUAqu3ij4luR68XEZ2AO_GQVRb4MWluDwvmkKlvq-j4qL8zJ7MjiBLrQdSlMOxWH0021UzUqhkybEyj0_58q4cqIsDPEThvoYQO26-9vkzEbDHPTVup5sGK5aWWsEIga8zxT7R3pd0nNoNFoIv_a9r422bx2g1sO5PlxjdakyBnIliRKDRrTk3OVnzbO5d2tEQ8O1phJgYosp1U1ykMF-rR5PWLBPsUs0Wx5IOGgPbNMCE1fdI0ktdtwszug1NEUEpSgN6Lqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
صحبت‌های جالب عادل فردوسی پور درباره مدل ماشین اونای‌سیمون دروازه‌بان تیم‌ملی اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30888" target="_blank">📅 09:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30887">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryAlVSTH8KJTWZYc-FzFVbbru0VKQQlU6bbzPueIJfeLB2grxl-Off626BnAmQBYzk_xKYJmeanv324tnzAjJCdo7nTQTaIHk2zAmICVtRvUnWLxttRvfbnrJ-qUkgbUUJjOSgeu956mKrpK_QvdQJl0x5Vt6idlNZFEpsSy2OYieiwehAhp5BJ2hWwCdAnRcuATWEEjyWLUPds_WLZfW_ilRI6V4Fy13PCNgaG3T9U1-e6CNA6SVOgA_Uj2SoCs0Uyftbc-jw2FyGiy4yZOl112tp2pjxulmnIDAemtaQ41QXiRR5PTXTG-hMfrJe2nxW6Ao3U42p3b8fuhxmSTeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
ولی کریس رونالدو با خدافظی از تیم پرتغال درس خیلی خوبی به‌ما هم داد؛ جایی که نخواستنت نمان؛ حتی اگر تمام خواستنت هم همان جا باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30887" target="_blank">📅 08:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30886">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZ5fIVKWQ7ohelv2pM_igEO-yb-73txTXM4KiEjq5zmp0hlYJG_16cutDptKykv8Dz6tw3gTTG_Jm9dOfRvBf1kp6c_TxcciPNhh-9NKdtwp2igMsat1fSgaMnwWtaqAbRtqyn_tTjXqpz88ynAwr_jbClS8X5B62QKvlbTAkmeFD3o6eLXJM584roKnTftkfUxf3TGS-bK7mFMeYZ19TjFOCF2xGp4kqGr-hBDOYE0GkAB--Rd0xkbR6JlNmbVb8Uo7HmCVoHsDjye38o1ATZdgPWeeGft8IGCg7qo460_wXCvyj83_N4-xJje2hr6rZjzvestcVz_h5Nre8Wt5Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
🔴
معین توی کنسرت آخرش اجازه ورود پرچم شیر و خورشید رو نداده؛ وقتی تماشاگر شعار دادن وسطش آهنگ خونه، ترانه «بی‌بی گل» رو هم اجرا نکرده.
🔺
این اقدامات زمزمه برگشتنش به ایران رو جدی‌تر کرده و احتمالاً خواننده بعدی که باید تو ایران منتظرش باشیم معین.
🆔
@Persiana_Newss</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30886" target="_blank">📅 01:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30885">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇧🇪
🇧🇪
ویدیویی‌زیبااز دوسوپرگل استثنایی و محشر کوین دیبروینه 35 ساله در مسابقه امشب تیم بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30885" target="_blank">📅 01:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30883">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JS62KTtZyEkKm_mD67KDzgSIr8rYjHdP2oWfnrcHjxdrnwg82QxGptIP8LWHbdR58S9H_N-1N03aT6GD_fP22rFM2jdrkRC-5ejZKr1PJYgQGzUoyATXepYUsgTjHgR2_bfyf-PIZVtmyWRFbEgrkvMn0s4B4tlbVtzBAAMCPlAigffmD7YmXC9CWOt8S7EisCxFOxgwzzJBzkBJo9uIvTSZ-uulbWo2ftNSkXd2cOX0Ix62CuoDVBT81JqkjgualuBjoFn2UrU24cPyA01UfIFspjJkSNyYvlvv9bb3zIq4ybb09TwNLuvtdVKQ3WyiFnrst3H3wvkEtDecUv1HAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ رویارویی دوباره انگلیس و کرواسی پس از تقابل جذاب جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30883" target="_blank">📅 01:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30882">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFcZag2JX-3OmFmxEWFfVFYN1Aezr9COHlBLz7wtDNu9JZtM4ynsRzLmCeaeWSsX1YSgUA4XoQlVoKp01nFefEdpOZxmhqkLy_RQQWHLN__hbJRlqlT3r-XK_CFQZh9vgVZGrSEBKJdSrknyNHEziQwjac5v0BJJhFdIUYvD98XCL42TFQXfXWVNTkLp3EABfEdH4lb7ZyoFKo6RbdJZcNjYUOAYIsiYckv8fi87ZwOmXsbtFpZfFrP4CnObxiOukxX7Av2eSfGi1ML6CNSzQRZP3zX26VH-IxERSKWrKisQdVo3MMAojzoQ3UGitvb6W5_t1vLEppFQuLHBwJC1UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌ دیروز؛
توقف‌ خانگی‌ فرانسه ده‌ نفره‌ برابر آتزوری در شب درخشش جی‌جی دوناروما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30882" target="_blank">📅 01:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30880">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇪🇺
گل‌های دیدار امشب ایتالیا - فرانسه، بلژیک - ترکیه و هتریک دیدنی رابرت لواندوفسکی؛ لوا با این هتریک در تاریخ مسابقات ملی 92 گله شد. گل‌هارو اصلا از دست ندید فوق العاده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30880" target="_blank">📅 01:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30879">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZehNYwCI7ouXk1eXpdReM9fct8gMRfjRKoFPW4hJ_K14qhtunYY0WJPHtQBuJslAltCf5iMuD6VIt0QEwZI8-haxbmrPwDS5qm9Z0Olvx85HQ0dqaWrlzpIuep_cX4yCfDYcvBPhEmCvQuMPUYCVnNv6cItCXepcuKOs_Zl20oJh_Zkub2-0eWEO5iFM1eHb9QfFOXrcTPeOd9tcVdhD-zMgNbMtgtVBPlN-a-EPAQtWVPaHggWsJ8nI-H_12OBpVEfyuQa92RPf9FXwSaquZKrf2rmrkl_aLPWz2dzVrB3zXALCdyJEiZc0K2JhRQEcSddYEACiIr6ZMn0K-kxsjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔴
پوستر رسمی باشگاه پرسپولیس برای زهرا خواجوی گلرسرخ‌ها: 2 بازی، 2 کلین شیت، 8 سیو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/30879" target="_blank">📅 01:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30876">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sd5Lv0RcEt7mjK6-H0qyRYjfq6eDmtkJrcqsX4Y3QuPVnwhcCykAlmKD3Qb9j71yxsuRPfYdpfpmQ7NkOJs7cLa76wyouXbgd3-Sej8d_camEUmPm273TNlootd-Vq-51sxEiqHcTa48zhS5j4WJWGYaXEqM7bQgm9Nxsa28bA776BMTsL4THeefn_lLVE3y9oucD2E_kgWiuOWxApNm7E0Jn1ydvByZobEV1KrcTuTQUPzy8Lfoc45LDva5NQDTTTmLgLwwqyHY2SBMVQxjdepqhqRsJyrebT_0czSEmTlwtCc5AvAJiwyPcdWEWzkUH7Xm8yCos5FTS2ssU9eoiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه A لیگ ملت‌های اروپا در پایان دیدار های امشب هفته سوم؛ فرانسه با ایتالیا مساوی کرد. بلژیک سه بر صفر یاران آردا گولر رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30876" target="_blank">📅 00:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30875">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W28mVLqOI4QiNmXKexHNR2ZWkZXNTm--ocZK1ItxmVu3Z9xlZU7WnjHEk1v_WhnNNT4SKK3INtLV5CUhrWqK7oGy58MAvXLOwblARwQ28uv6qBhZl_I8j93WQKiER-KQdxWKtfC7edyER4uVjy4nw1K6lfKyHQU9wLNTdmjwYtQfw5lMNZ6rZ0MKnSALHFu2mRYh_xxj7oIfkHqBV3Tilng7hPlxOaKNJ3MVCRUOKtymTuPLrO4SDWJzkJMip2w9Ns09V-m4cbf8QL-UgfVwNQfT76LopHeJJtXzcibRy-p8w9T8ljU5vhOsOz_Sf43Mpt3kQj58yt3LMMoWL73kkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از نگاه بیشتر بنگاه‌های شرط‌بندی؛ لامین یامال فوق‌ستاره‌اسپانیایی بارسلونا بالاتر از هری کین و لئو مسی بیشترین شانس گرفتن توپ طلا رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30875" target="_blank">📅 00:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30874">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pH2sNJaz8Vilzy7Pq8MTRKYBQEdf7zfFnmpd4MrkAmxYkwON-U65nGW-KlkLIuLBpICxSGsPG-RGvGDm2K6_Fk_p4yW7KWXaS6vJvmRVz_mcaJDbCYvC7g-TAQc0grLxgL6k_E15DewVotgYPP1WIDMr4BGuscYaCZDKEZCTjg81ghr5xKi6-jL_dGXE9-oGy7nyMEpkYb4hzxa2hmz6DTtqIYUyEdfeu_EdYIwZrGvoYUT-Xt-undtov0M6vXhKDwQM5vqxWer-cS_DHkQOqxtcuua8hEBIKZ-SYuxtTWzUf83Ub8Duhg571XsqivFx8kX2w0FdlC8klq_IeGNSPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز؛ رویارویی مجدد و دیدنی زین‌الدین زیدان و ایتالیا پس از فینال 2006 برلین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30874" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30873">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9Sjrb9TPaotancjOeNA3xjk-qFaGAFTf0DPiohvBCnuzxnXXji9NFvYSJdE18qgg5LjVzFtFvuYlm_qwkoEhhI0Mf77_LLrzEU-DdRobghtMWPxludBUqZgCqi6DZk02rGOj1E_dX2-yv8ZOFfoY0eMlv01aURANgh2hBiVBinbmd4aAZtkg8P2Z9PKwACro4tgJuy9wQwBAFyiRroWTz5BhYepHL8ymNXWEuyzISyFonzaFxf3-30oWAwFComOKF8omJlWbD4xN2lIsZ-jVGmT6Ixbo6cVx7rnVb6hZHwoj5cNMgzrAw8ZyLARKvLjaJhr9g6Zh9gSaBy64zICMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال فوق ستاره تیم ملی اسپانیا برای دومین هفته‌پیاپی بعنوان بهترین باریکن لیگ ملت‌های اروپا انتخاب شد. اسپانیا در دو هفته ابتدایی تونست بادرخشش یامال انگلیس و کرواسی رو شکست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30873" target="_blank">📅 23:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30872">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGYWAeKlvwR7ic6joG7qx9mr2-H4RteQdi_M6iH3nOIZ1CUE9_2HzbKRDNwwGOETAAF80j2o7ZxpH1kGBIK6pnx_gAMPbNTgr4r1jjkVnt3zerndD3vvY54niX1PM4oRp6V7HpnL-3JDiaIlLHlVpcj4kqSuoiKJBjwsv96rBIX2zQ8hbXBzgNSUNbJH3CisVvrsZ2SglpfKQpITl5Hw-oKXPlUAptk5livLH-E4U4YQmuwYJMdzpGhhvZfHugIHQTlnmrOlfKpg8SbfcUP5VyEHulZB56KdW-J-voNTfGmwB5pS2UFpHiZ7Mz0AIvk-jUKYtkyAUwqHekf-ewca7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
ویدیویی زیبا و ساخته شده هوش مصنوعی از علی آقا دایی اسطوره تاریخی فوتبال ایران و آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30872" target="_blank">📅 23:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30871">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6GTU21ZnLkfrolzjlndqKHwUmY8NwE38aaSDFRV8HTzMDygFIQPhmWG2yEHcOd089nxLHD9ccGghqHh4ApZhGqBU6rw0y9WXIisVMgS1TWVnhUSyefrLgsxaPzY0FuwS7J8ZZBhqdwYIIyPDVpprAh3HPIWRWc-PtHZDF3M8nKRl6caqz1CBibtXtEc04gThcFFD6--fTLsn-UjWxJAa_BkHJdz0MJ997uKzT-nU2ITbH_-UxIB-UpvE-kAmYi5dJPY1Z33LYtzknhTfS_VEMOEuAhDdyMYu9L-HCfvDSHt2oCODV2vvqN4UYZqPzjDHPtJ_LVPNBxFVQRrWxSqFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل کریستیانو رونالدو
🆚
لیونل مسی در سال 2026 در تموم مسابقات ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30871" target="_blank">📅 23:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30869">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RNEQ8aSvJ6wdpEfXQztuzU29A6QuiD-9xIPCSjSAPRlAkDuRV49eADvqGvfU9Kg-wuKMtCrvjiRl6r3IoOTonbSEpPg46K92O82K9Eiw_Z8OJBuVc3AAyoFUXnE5Na6oELtGV2GYLUakMDx6tQWZ4M_JsSS-A2cAnbliIOSZpct3VGkayyWVMEerBh9M6WZeZfJYlEbrFrSaLy6xS729xBx8UZnTLBOVLfFnrky_g4oL7zzkdpkwmKqbR6KzcnbksSwGB2Ltq4meW2_WGvrO4BPoN105Q18aN4ibibvKL5LIlRdcXtqvAZtdTBzMgG7gyk0tv_hautxrAJoNQbXnLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G8BIm67cEyp8GqISPhSA-6wAa4InmagT3SnSTzVuAcDtoJkkdEhtakemosBGd5CiVlx6jjLKzAIzqE1f0v5uHEug6rFqF_OFKuDvlLFvyfOWUlB7r6f_KC8glZNwdLX7S3oR0ZvXN5-tcByfc5P1zdgF7LwcSPwLvi20RZvlDAcRqfA8J97TTVTXXcudLHdIvBJoUfcS2TYNbzS8icNjZAZJTjdDGe5jn_f2G9U1BaPxKKm2xhbx-XJZPROoAP0XLjFfQqcvLpI8W_qP111eAr0uDjKbWlwMymQvYU3_6OcwDX0NrUlJtPNkPRQeIxi_e_02Ytd0BV7MkaoozifMRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تعطیلی مطلق استقلالِ سهراب بختیاری زاده درفیفادی؛ ۱۷ تیم بازی‌کردند استقلال تمرین کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30869" target="_blank">📅 22:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30868">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab82ee522d.mp4?token=PRzdC2GAjpy5ERlbraA_EvvjD8P0hHl3k8PfoJeSk6_AyeoD8_rvqbSEYQvbnx4y39Av7Py8Wk-eUrfHv_qqtvl81Zib-8o0LPzj1NfW4XEzs8Vq5gTCBRSRXIgwneqhqCqeBY97_OniBp02arB4dvU56kXI8RW7SuXNXvTL8AsuCZvQo1PLcSZXHMPwbgVBIu8o-YrEZeVx-prnRS1ZhL9yKgjxBu-1cS1vzrshkqXC3urpQj03zgHmDlSWgWL7ODj5N2bFqDP-1m09FSPCmX3pGYx0EVjBM2qlq5PZNz-PN8j-lArjR6HKwazIwHIkfKuBYoh69KGNPyzq9ppDS6GbNc-kSm_rI0trk4SPQduCzl7C-fgS2xMpkOKK6sZdbHA1NBn_IIdowawiAiCSYp-tEgO1zQ7t38bRKPGcmHYtVRktwuGPhRvo2vq7s3wT1K_OxBEyQ1n_Qwl3oMD6l8brztKVsTB6gAKk-OYfHDoGgJ9e4dR1S0hbGl1YlJd2_Ay-zHFoK9zvqgUhGkURd-WQMMh7uw4cn1JCN4i5RinQ88m6uzemwqUhGMh3ND4Wdpgi0a1ABx3MDxc-niEfQ34fFPDQxHzpBNP7mGT5VM66zKYCNlgzmGLeP5Sc85ndig942N9kPz1i4dXy3OGzATuzBcSSaYvI7EfPlRwvP9Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab82ee522d.mp4?token=PRzdC2GAjpy5ERlbraA_EvvjD8P0hHl3k8PfoJeSk6_AyeoD8_rvqbSEYQvbnx4y39Av7Py8Wk-eUrfHv_qqtvl81Zib-8o0LPzj1NfW4XEzs8Vq5gTCBRSRXIgwneqhqCqeBY97_OniBp02arB4dvU56kXI8RW7SuXNXvTL8AsuCZvQo1PLcSZXHMPwbgVBIu8o-YrEZeVx-prnRS1ZhL9yKgjxBu-1cS1vzrshkqXC3urpQj03zgHmDlSWgWL7ODj5N2bFqDP-1m09FSPCmX3pGYx0EVjBM2qlq5PZNz-PN8j-lArjR6HKwazIwHIkfKuBYoh69KGNPyzq9ppDS6GbNc-kSm_rI0trk4SPQduCzl7C-fgS2xMpkOKK6sZdbHA1NBn_IIdowawiAiCSYp-tEgO1zQ7t38bRKPGcmHYtVRktwuGPhRvo2vq7s3wT1K_OxBEyQ1n_Qwl3oMD6l8brztKVsTB6gAKk-OYfHDoGgJ9e4dR1S0hbGl1YlJd2_Ay-zHFoK9zvqgUhGkURd-WQMMh7uw4cn1JCN4i5RinQ88m6uzemwqUhGMh3ND4Wdpgi0a1ABx3MDxc-niEfQ34fFPDQxHzpBNP7mGT5VM66zKYCNlgzmGLeP5Sc85ndig942N9kPz1i4dXy3OGzATuzBcSSaYvI7EfPlRwvP9Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ صحبت‌های جنجالی و عجیب و غریب حسن‌روشن‌پیشکسوت‌آبی‌ها درباره ریکاردو ساپینتو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30868" target="_blank">📅 22:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30867">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrJzoqis2-WsBo9UuT_JalajpJfmqCHv_X-Ihy1-vJ_2D6UzSBTgriGe558e4ZkF4VBHo9Ek_-XeVnH_nUfRysdVQ_srJ7xLSM4UyUrzdk3gSdq4TMlLI1QdF-uLL087fRobcXvwBkhu0F5qv-Z4xn7zIzpEiD9whNmnm7unUngIYqxIikTR_HbtmpTMYRvJioTkRK2PO9vnLzRuwqhNIl63lCrw3XdhF1Ds9b36y-PxnXWdnZH9xnwoZ4SbL_cyHtZW70_I-6X__U--yjkb1i1qpAVyNV8vbBKAl72PgdTkKg4PE74KNLXHV_ZSEvXkC4GvmzqOGRwDTB3sobG1uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌ های رسانه پرشیانا از نزدیکان اوستون اورونوف؛ برخلاف ادعای رسانه‌ های ازبکی باشگاه تراکتور تبریز هیچ گونه مذاکره‌ای با اوستون اورونوف ستاره‌ازبکستانی‌سرخپوشان نداشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30867" target="_blank">📅 22:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30866">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atzRA2ItAQGHZqxG-eoOPGzKYK8tz4HWR-HQk6lHbD7VD0A6cVFz7VOaMjLhnqU1SG0vSVizMxNfHl6ueoInqKiHIaNBhx3O5O7cDasLDVmb4M1zE0XYZ0JaSNIHZ8c7KgFqtAtohzc-3QSXk-A8e7phTXaekIVZF4sw_-zNkgULcj6MFTMcUZ5PzeA6az9875GIPqAzsHrlSY76LAshJTXlQtbPM6UnwGESMegAOMSLdrK9m9bSVLXTmAD-v4ZAk_dhPtVYW61lb98FeAZml0jsW5p0d9wFxV16M3Wp2E8DaT4evKm5cXIJ7UjtgW2cbKeaUlF8qiDoBiw8wRN-iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج دیدار مهم امشب هفته سوم لیگ ملت‌های اروپا؛ پیروزی پرتغال در غیاب اسطوره‌اش و شکست‌ دور ازانتظاریاران‌ارلینگ هالند مقابل تیمی‌که کارلوس کی‌روش در جام جهانی 2022 اون رو برده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30866" target="_blank">📅 22:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30865">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/va_iKYt1r5lpjk_hU7eQTUfKZtjFmG95Yq6Z0vmMBI-FfD9AxqC3hGRvw0rTSqnhxES4iSh5wHDkDA7eJMbcYN4lsIiygsPuopH_qYhkEqHR3Hz2gY5ere0xABxXkCn-PpgYbq14wGE8knb0lq8xoaOkqdiRRcb3RVqLyuPL0IYhfMtmH5PEpQdwL9-TQEOsU5e7jcPC7xY2-lsDXy1bwb03jMA5TRYyOYT2C5WUF-jAooNE-0Ysaa-HJbXh-WP3_l4uste07d5jiXiSzf7jynVgQbyahhZlM0aBA9uVR1ItqQSvr-9Srs9eXO2x2_kICYYOeEQftM_o-dp9l7FwhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ به‌احتمال‌زیاد رقابت‌های این فصل جام حذفی بانام یادواره شهدای میناب برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30865" target="_blank">📅 21:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30864">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwRtcwynYR_wY5Tw5PIXj3-tQtlxyD6byU4Ozab8WE1BcE36kMJGKgb8_iZ7ByXK1sSwtNrOLhPoitM-MwczfbTCZT5UwLpvaDaOP-wduQcw3j1uYY4H8P72pxLWlH5HwidgeW0qX1vTW3DE57M3cgMjvkKg71J_k9Js5hltvjBFfKGE_7x7Gu8I50AuLnvkmxi4KqqRWJB4p_OdKH_LR4JoShZSX7iEouqiL95qDbwpHVbQDWdW5wjPywgQxHuhyR06YW2Pm5X97FeOfPhN4zHmNCi7MUTdj-3bYOKGqmePq9fXL2a73Ren91-dDD5p5lUsg8mWz4syv1VvLUUonw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔵
#تکمیلی؛ درصورتی که حکم نهایی منجر به محکومیت منچستر سینی بشود؛ ارلینگ هالند، انزو فرناندز، رایان‌چرکی، دوناروما و دوکو بازیکنان‌مهم این تیم از جمع شاگردان انزو مارسکا جدا میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30864" target="_blank">📅 21:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30863">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIb95jgf8ZzB20oRvgrBNtfxAhXCPVE-UKh09b4e5QGh_cENdOnm9QH3rAAy-o5pGqwAVkBqnTbG6jv4wBPyfVfkuZlN2gPiN-7E-ZjNvnnCm5hwEFtahIgDAbedDCWeDtovDf67MwTesmEAuklXG6bongIGYoDzSFz-6KIkhU8F3xUiknxZF9TDjK0jf5DwKraxpNz4gKfYCGOOBiV2lc_4_TBFM93-gmhGBk1onUBApghwsAfyJOE29Oo50PO3voucdvoKlymWvHmqdHrPsaJUit_3pYDFuWwI4x_yVsWgOnwpWulnXOUzlPzPLCiNHy6V4vxds_Bm98IVxVdWPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بهترین و خفن ترین ترکیب منتخب تاریخ فوتبال از نگاه دنی کارواخال کاپیتان سابق تیم رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30863" target="_blank">📅 20:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30862">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxhwSXmjUYTQrZQ9G0pY56UtoQkHTXOCkl0q0DNiWHbeGFg-IeB7Mz6IEge57058OY2ecD_7GEGs--7cenHSnGibVdtehSJnyIEnCMB5B5dzYnzYq_OKxP7QHXkOdVdys8pcHbpCGDBlmYl_N9WRaeNFH5Mp6MevYBYBpQfao_FfXnLqsSNk0hWYxiyKDcvA-FiATGl33x9c6YZTv2Btd2fjaa7bKFibEVSG0gqmepMPPpEF8QIMsFHQlLp1mM_ofR9Vwc7WQejjFvlclkSDU73-viGAFzIut5rmkX4jGgdzRATXkorZedpCAQ76kFSV9-W36dZJl_bU2NGSu0Eubg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛نشریه‌بیلد: باشگاه بایرن مونیخ امادگی خود را برای‌ تمدیدقرارداد مایکل اولیسه همراه با بند فسخ200میلیون‌یورویی‌اعلام کرده. سران باواریایی‌ ها حاضر نیستند با رقم زیر 200 میلیون یورو فوق ستاره فرانسوی خود را بفروشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30862" target="_blank">📅 20:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30861">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v83SDlyHOnOTZ1FPRdADFOKfUBwKWs7VpzWcT41jW3EH9d8wgJqgGTLXKQIa09gXjsvc16oPBSGR2IqGd51cAjSkTyFEiexNTngnt4HYMhX49-bpTEDR313wqG3H54_nA2EqIpK4dGPoe1LfL5a_ESX11Y3z9a-HEo25d7ELNJbIqZj93uXq9jr5RDzc2FGQDQx85sNYZ46sahSJBQhas5bfqlrVaH_OLONxFhWTHza18pb46Xg9hoSI36sR2W0FRqnbozC3dWrbVJOWvcFsXD-Hkwk4Z8HZBbhm-U1boU4zlif94ugBSxlVDmRwildiN5owvEMil1jQ_96r7lHc6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج نهایی و جدول رده بندی رقابت های لیگ برتر بانوان در پایان مسابقات هفته دوم رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30861" target="_blank">📅 20:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30860">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1GgkGQO_6c9MBHi1UlhowgXg6d2lPJbJbgNTxkVn6FSbuPFoBwkUQXdkY6Co_73Dw92JYqPpI0t-JimNOzMDmRQExBJPwUD6uHg1wGqIGK4UYPRfDOY8pbF1XUL3PRz_27sFOGGXkKCrpGV0cuXAFJPpBgVpPXYjUUJ8jwvZJIFnu6afA939ac_hAxpfy2yc1RdEHkGp2l01EHbXVFn2fEHtsX3MPin9PDyOjd2SRmpVPQawcvaLG4A4utameOyLI61aPx2oZSLqFEkbsvc4wUS-l2oVX2i4UEeD-OOJx53ECG0u0K84wQeeR42uTNAeAFLFsZyaNHVGHVrlSnDKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
هانسی فلیک سرمربی آلمانی بارسلونا بعنوان بهترین سرمربی‌ماه‌رقابت‌های‌لالیگا انتخاب شد. چهار مسابقه، چهار پیروزی، صدرنشینی مطلق لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30860" target="_blank">📅 20:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30858">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24f9f9a87d.mp4?token=IY9TNvtgqK4cSBpUF73g32f4GqNDCuo6tIh4quzztgVNd8CRKlfPKGgx9aYj_P9-v-YGEOG9b7oZwKQ1sftfUllnQSHApIeJ8lhJ1d_4IJYUWvfVaqPdU2TR2mWnqLEssndJo0zdlLgwAK4bzp7KI3CkkIZadaBpOaa2-3daqvjCwOZJy_FpB9GmVpmMkSWSkAJNsOF8pbGaGRChBI9hPIiXy1Zo20hlhM_a_gEyCvk2kjhy2fufmzUXhcPilIZKFa1_QxkYr-b_05r7Lbht2ryMYR9y3OYCztzbejxVNYw5eMrfy-1JsPuF8NytHwphESHlt4gwhORz7uLTY-d8-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24f9f9a87d.mp4?token=IY9TNvtgqK4cSBpUF73g32f4GqNDCuo6tIh4quzztgVNd8CRKlfPKGgx9aYj_P9-v-YGEOG9b7oZwKQ1sftfUllnQSHApIeJ8lhJ1d_4IJYUWvfVaqPdU2TR2mWnqLEssndJo0zdlLgwAK4bzp7KI3CkkIZadaBpOaa2-3daqvjCwOZJy_FpB9GmVpmMkSWSkAJNsOF8pbGaGRChBI9hPIiXy1Zo20hlhM_a_gEyCvk2kjhy2fufmzUXhcPilIZKFa1_QxkYr-b_05r7Lbht2ryMYR9y3OYCztzbejxVNYw5eMrfy-1JsPuF8NytHwphESHlt4gwhORz7uLTY-d8-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
حسن روشن پیشکسوت باشگاه استقلال: ریکاردو ساپینتو تو اردوی کیش هر شب دختر میاورد تو هتل و ترتیبشون رومیداد. تو سعادت آباد هم خونه گرفته بود مکان کرده بود. بعد از تمرینات میاورد تو خونه و شب رو تا خودِ صبح با اونا سر میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30858" target="_blank">📅 19:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30857">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHiLA4q5cilUcm-gvH6olU2AnTR6V4wa4K-oJE7YYF7O-CzrUu1bFp5WgJMYwHwOu0X-WX0J-0hLgh3fTvLHBeQWg8Xx1ML3CfF1PAntN9nZZe5iaRSJNoLsDMXh1WH93i-t8f-pqZMnyKtCIptv4UKTgsrjI-cj1nfPlAbn4fC2QxM6-_NP94XB6JsiQ4EM3zbzHiXcT4vCSQl8mKKXeOMlOqgmbTImEHTxG_jwxLTTBYFuT0xymJyqG6hZbSEIZbfW0qzy3d6wQiWqmueZejEGr5FO8itHAakWwQjKdAfeULV4waKNgXNmkOydVzzIpJUOll9EBSQXprKiw7yt5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل کریستیانو رونالدو
🆚
لیونل مسی در سال 2026 در تموم مسابقات ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30857" target="_blank">📅 19:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30856">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JggO-qSOGXS83mJ9SQEC-QFgnaGLDUwnbm-cDumBiIhtPaYy-sK7ry9kIRyVxAfWz1ASi3fJHd117BvxG95SMlUBg4VFw8ykWNuiab3ZcKVlthtEIKNNPu3G3bApAwe6MkF2ktYGxFYZxq4NYw3-MGW4_3RERexoQWyXHcddOE5SYYeu8aaNo2m0uYLbXfZhw2FHZyr4GrqZefV98mEZMsjsR26OitvcPoTKIM5Bo38ljZ1tWyLjUmiVoKK_jmIRDosAPBy7l6VcW9ZlqaJWdpxdKB5CU_9CA8UUj3NNXc85u5iZXI_LFoOLGOn0QoO5X3x_8i9IOkRYeT8eFNTNhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ رضایت‌نامه ابوالفضل‌رزاق‌پور و یوسف مزرعه رو هم300میلیاردتومان خواهد بود که باشگاه فولاد خوزستان درنیم‌فصل با فروش این دو این رقم برگ ریزون و سنگین رو به جیب خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30856" target="_blank">📅 18:54 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30855">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYMVIw7vAhR_McsZUwZ7cHO7bINVGgJVbR-J-V5qsJ5gxtg49ZUxlrO1RQYdENhPb7_GU4mXxPnZziz1dyn_xQv5j8sqGhbcqCde9U1n0uxF0mv_zV5PAndEtUcH2ibZZJgL91HL4y0A3zvBYqe9SsNP1zMeUzANY-8zp-7QhHUR676NaTo5c-8tOFmk2mw1tX6fVxmjhuqLBmrMtKa5HZuJYAhtIiiNOXwbAQjaWFm5Dl2DT1tHchlqOhwhJwkA7eh9LmPTIjNd50sdllRMHNKsLR36CtsfB-M0uo3psjkX1esXjqypGL_yMta7r_pfD1T3xEryniSWCNecR-S7Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
هانگ کانگ در شمال نروژ، با جمعیت 2484 نفر، جایی که خیلی سرده و یک زمین فوتبال زیبا داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30855" target="_blank">📅 18:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30854">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMBIyCkIHpDKkltVKjU1qTMOw9YK9_sewnsNDOy-FvRns6stKxbEjipovR28-Ooa10FBRidQyvkrReJCwVNyF5nrvG9NogQPOZFDIpwwiBfuHv8chrHeH90NeCQ2nfSi_UTZsTU3QNwphNzMsBzWEZaMy-gWOD_m7tfmuov--PJ9lE1yhnDbS1m_NxRJwi_u0ku8N6iNBX2CcakHwTq10nA9ZK__4Jf7mzfQObmAOKTg-fynNSjBYkTWS9JR7trJClx7hcqWYodP58tlEPWnYQfO1cm3QDatLUPyomGOmdM90RqU-Ggb04Kx_qOnLzA0NxpNZtkZFbYRoJ9kvL1NTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ بعد از خبر اینکه رونالدو به تیم ملیش دیگر برنخواهد گشت پسر اسطوره از تیم ملی زیر ۱۶ ساله های پرتغال حذف شد و اسطوره تصمیم گرفته جونیور برای تیم ملی فوتبال اسپانیا بازی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/30854" target="_blank">📅 17:48 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30853">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6rL4jDCelKXKwnoOtLTI7FtHBg8r8SbFwqp5BMw6-F9n7cLMSnb1zAmRBdiZPu1M1-p2LkZ-FpP75ybiezvlF_nXn0NrySXITD3Eiz4UQuoXwZBn2m_1ir_fwOAYDWxAwB61SSfHMUmexm6BhhvUR7HqyS4vevI-oJYtE--_7bhrBYu7Xk1YCHj9gljHD7iOiLKJku3-GMDHLfKoDtpwPLptHtUfXoJZpM4Q6uHuNs65le7gowlg4IPPdvKiiBtX7b7df9kf7hFSXggr9wZsZ1Ynv5nef4hapq4Hxyje0LLpuPJMsSQfu2Qa3FBYyTKqzfpQQg4ClI6O9b8Jz32lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز؛ رویارویی مجدد و دیدنی زین‌الدین زیدان و ایتالیا پس از فینال 2006 برلین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30853" target="_blank">📅 17:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30852">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VY__eWSKpjkAcIAiwaRJta9qF4287VlQW70j8Tk7Hh5A4sRG-Yyg8UQLRLvb0ivFeIau57H6K9bxReqImWqFbRoiPPEN8Bm9b7iq8q2BhA919FfRXlXu8PIGWnefMgW_U_XYOj8xsekhIs2ADVfMssy2EXjrXv6YW3_pLQzUeeHHZDLR41LWyNGVMVQCMSCnD-Czy1ASvRXY1_LjgY-DKwlNGNwHhVAOO-V8IXaXDdxxgvaT99bTylW0j8T1oWzgBfurWbA6VoAWNLKqFB8RiAXZd5z0UoEFF2IWPelveHIL9at3d25NnlEp0DraYr1F1PVnZHtDnikAke5QCvPz1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توماس‌مولر درباره‌بازی‌معروف ۷-۱ برابر برزیل:
بین دونیمه تورختکن‌ما به هم نگاه میکردیم میگفتیم چی شد اصلا؟ یواخیم لو بهمون گفت نیمه‌دوم کارای عجیب و غریب نکنین. نه برگردون نه دریبلای اضافی نه هیچی. باید به حریف احترام زیادی بذاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30852" target="_blank">📅 16:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30851">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmpOnHEfLoaEXIqAWPGSdCQKJbZ0-lLeRMQSnUYGBeKXaegUq3AgH4BeClm7YabvemDv0YizH0TAej0QB5yL7_UyHguR1JrIjjwl1xdCG3fMlzWrPZzS9QDeCVAYVt-_VfW52lRws2kNt-PVWwtoPn3zyQyM6cWIou5RQ_7ywBWZYqc9myO9DLlOGxABzetpUf5Ebqo5ynyIgqkaGfbuyhXEuI9cx8vyCKhRo1ptPKjR70Zyh-iWW8RIEVGEqhIHessNPp47toX929PWcFdDgN5cK-MmtAi07rLVfTd3rvLkuDzLJ3phW4v9YaL2ctzLxrlTgwne3IAdODmIl2kTQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحالی که گفته میشد خورخه ژسوس در پایان بازی‌امشب‌برابر دانمارک درباره کریس رونالدو خواهد گفت و از او بابت‌ این‌همه‌سال حضور دراین تیم تشکر خواهد کرد اما او از هر سوالی راجب‌ این فوق ستاره پرتغالی طفره میره و جوابی به خبرنگاران نمیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30851" target="_blank">📅 16:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30850">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyPmsG_ZncUAOd6jxm5mP_dsFWqwixp4a_C-2pHMIzvOCorExTJsGw1zps5dYUHBPu13QIPKUlEaKRItjmvOP0bwvdFb5b-CCRuhJmziVRwxnSp-CQg3W3yUKauGPwyJ6a6UvGmAL3Wih893d-gGfEfzC2flz6EB8sSOAL6_ecPA2nCVHKy0nm-qFdDv0fu1FkctyM_0r8zR0gCeQreJdWi-4j4IQmQP-8pJjLnia9YW2DLWgxMrWuurrghDcg_RmpliVTcJIxDNFcWdo9qtC0YPU8q6JCC3KD_UZRZSNf8oodon9sqR9ww6zQqjJ7tMEzhltMJ3bDbi_lx85KKWVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت‌ جدید ایلان‌ماسک:
اینستاگرام فقط واسه دختراست اگه‌پسرید بایداینستاگرامتون رو پاک کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30850" target="_blank">📅 16:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30849">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEIZkP07468ZSQD7HIrGW6EFEaH7oOce2wVOdUi_3YxPF-ZsusgoIv7s0u-35j5DHLEoQgNnBiEoDpppcEDdebtNPD2AgxWlguXTlEfroJ1y9jN3Yt4w22W_uRw8eGruT6nEKPsW77acQ-sAxgwo2grrw62OAVQO6yQFG6lgYXMAhvHTfMWwVzYaVgdngbA2GQOB__123uEEQdqJc5TI3r27e-ymilrWeDbrq8Q66TUUNOyifegtF-xN3C2KktkGb-m7pTW6CPO1RPauMjJYQ8n2-gFfj7VLNamvYdAs5WLMQQU83CgpA5fIp1ZLsmCpNVI2U7z6f5-BZGPAZpPxeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب‌فوق‌ستاره‌هایی‌که درفیفادی مهر ماه مصدوم شدند. حالا مصدومیت امباپه و رافینیا زیادی جدی نیست و از هفته بعد به تمرینات رئال مادرید و بارسا برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30849" target="_blank">📅 15:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30848">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1IlNDY4MHJlJZdBuGa8oRAli87tRS9Kz155ZLrBNyqsTZJeHjbTol8l_tLegHGtROGEssWUEOjWmjWqUAYMTDfxesougoVgFIH9_2xjcQ0_hY9slQEAsImmlXIa6UpamRHAM6pRwCPD8Dhen-uqoYLIt68IVdwc7QOnhi_8ou-FDtq3jXKlckfQOLIW0m5kSA0gxIE_kbbb4U4i61_o0edeSfpGR_JJvsiSh16NYAX-sLKOtBeWE7RPTWwWealuXvbOLnB1WaPKyrj_XKBzTwKiYD8eyQO6vtbRsdy4EScp1CF_fq703zdHtq_UEjF9WxeIpyhgBYBnbUMhPEGXnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇭
روزنامه AS: باشگاه‌رئال‌مادرید گرگور کوبل دروازه‌بان 28 ساله تیم بورسیا دورتموند رو به ژوزه مورینیو برای جانشینی تیبو کورتوا پیشنهاد داده‌اند. درصورتیه ژوزه نظرش مثبت باشد فلورنتینو پرز با دروازه‌بان سوئیسی دورتموند قرارداد امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/30848" target="_blank">📅 15:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30847">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obgzD2sM5DGGH3Bttz9_jX53lLdB9BBQQgszF4vO-mSWrOWohZOb18hTrFxpEy_4L5-SPps1K1UM_Cybv-Ekhtyyg-vQUGU3Sl4cdi-zEX_gph8Z-EpP93_83GXhXpqj6INpzWTMq4OKE6ak9aUyQXiSh6Nd1r8aunSLod5mKk8mXw5wZL8ebNloMfPMR6LJIwxP7YfIAvA9uo4qfTKJu3Vpfu8wHUUIQtziqVklAqF2U9oHidNPUusEVcrdwZxVH77oKhgIdULEfnAUb-khBYCw991alctPJzUvguYs3KS6imTqtdBRWWxxDWgXJuVW2K-25MKPisCkROK-Yru03Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دانیال ایری مدافع‌میانی پرسپولیس به دلیل مصدومیت از ناحیه‌کشاله ران در بازی اخیر تیم ملی امید سه هفته دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30847" target="_blank">📅 15:17 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30846">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSNPqEEfTOwWGjDmDSlISa8lUVyxfhJxU083EfuIDyf5b6Yp6qtRv2mxssXz5qMSBrhtjC3PmrG0Wa_QgV6ia2PvpzQEborzBfZ5qs9m9Q4utXwbdxD9UUAY2_o_t2jScJqJBLijlNvU-QCigkXHaR8dNtblldlGuA6JFmi6TMrPnx0cfkF5pGOTp9d-tH3sg6TTBYXKQa1ioj1S9Ku4GFYHV-vSxwKTxTmpTanAG5t-w9I9yZ6uk5pBGvC0hm7HU4PfxDiVBJ-zfzsNLuTSweQkahg_s6--RZSEIrZJ15Zr5dZzo0LiVkMOIlqk_llQc9kA5Js6F4s2Q0Nf1pXo3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رافائل لیائو: پوشیدن‌پیراهن‌شماره هفت تیم ملی برای من خیلی خاص بود چون رونالدو از دوران کودکی الگوی من بوده. فرزندام هم در روز هفتم ماه به دنیا اومدن و به همین دلیل از این موضوع بسیار خوشحالم.  تمام تلاشم روکردم تابه‌این شماره و این پیراهن احترام بذارم.…</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30846" target="_blank">📅 14:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30845">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f21V5iAlvjLK9Hk6YXNW9lXCE-TJZtfvdkZBW3t_4xl9Pf41q02v2Rtnl-eF4JFSj6rW6Da5RV6vmqoIrJPTJfR3mxbQiZFql3X8OKMQ4oGtFrrVKqW2LQ0pCNURukHPdBze2g93MSWy19LDb4zSurDrnW2VNeqak8G4lOKrKKG-a3sHeQ7o4Z-yv0552XPaVJ8nxECR6bSLrHlFSxH9ufcTEQCBnIKC2MiKzJgrIWDO4quX4yQJn6vfkZzLMuUTrmh1hRYOgmX1g4Hd6r7fMo6uW4u9Gz4Ta0PfMRj2pGDe-wQ2lk-9a3r17fUqRjqxQUccJiyY0prcHbCBzF0fMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه پرسپولیس؛ دانیال ایری مدافع جوان سرخ‌ها در اردوی تیم امید دچار مصدومیت از ناحیه کشاله ران شده و چند هفته دور از میادینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30845" target="_blank">📅 14:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30844">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e6e601e1.mp4?token=l3QzzTbzkQ9MS2X6t6kjdAWuaWUBYcfPSfk1JIULSvxzFNZBfuYKnJXipCHHBOvlFltz8AIkBgDf9PuhOyfpjMRv2CJHis75Rs4bxfepGXANEDYvda8B61SMhUfyZ0YkzbK6UqFFWLPfRAFMTYr4312G0sc-1U4ymQYNr86j_AEXmiEQ49hwaqt08M9aOD6zIHFC1cQ55SlDfoEbvkDYOCyLTtwvf2m_ddmpkdH4_itmcfF4lXaaxPEqgbD-_iXjMcI9FT_p-sCYd59DG4GGZAa-gkHxO905Bwi6CAQeFvxvI6FXhBNQvE2NTxBppaCULG_uoOpH3PhpLnhdrPRu8WSmGkvvLBErIw2eqzYySlHf-ts25BL3dPIH8gRu7vWG7zKVsgeeCuAPD5py2IKgng_q6Q3Kz742ZHXm1r_57lbgSMphgvsyFaxNMaWZve91QFN4VcC27FOcGQrIy1_lXQOzjmk6-UjF84sDwYV2TAKdAUg72dqWEhss8NpDgsOATppOpgqHrjLvtZF3wPuhS-G9jCSHLQa9iyOO8MBv5WlZx4bBcOX1ymNYtNbbigwGFSPrhIRWFV_eQh35egaZLiK1Af5GLsPq2slrlAhzrYNbwDbowB5oUlXVg4s51cATSCJm1o1roQlYpWv1ZGndC3tTssqfDQmHezoabDFLe4o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e6e601e1.mp4?token=l3QzzTbzkQ9MS2X6t6kjdAWuaWUBYcfPSfk1JIULSvxzFNZBfuYKnJXipCHHBOvlFltz8AIkBgDf9PuhOyfpjMRv2CJHis75Rs4bxfepGXANEDYvda8B61SMhUfyZ0YkzbK6UqFFWLPfRAFMTYr4312G0sc-1U4ymQYNr86j_AEXmiEQ49hwaqt08M9aOD6zIHFC1cQ55SlDfoEbvkDYOCyLTtwvf2m_ddmpkdH4_itmcfF4lXaaxPEqgbD-_iXjMcI9FT_p-sCYd59DG4GGZAa-gkHxO905Bwi6CAQeFvxvI6FXhBNQvE2NTxBppaCULG_uoOpH3PhpLnhdrPRu8WSmGkvvLBErIw2eqzYySlHf-ts25BL3dPIH8gRu7vWG7zKVsgeeCuAPD5py2IKgng_q6Q3Kz742ZHXm1r_57lbgSMphgvsyFaxNMaWZve91QFN4VcC27FOcGQrIy1_lXQOzjmk6-UjF84sDwYV2TAKdAUg72dqWEhss8NpDgsOATppOpgqHrjLvtZF3wPuhS-G9jCSHLQa9iyOO8MBv5WlZx4bBcOX1ymNYtNbbigwGFSPrhIRWFV_eQh35egaZLiK1Af5GLsPq2slrlAhzrYNbwDbowB5oUlXVg4s51cATSCJm1o1roQlYpWv1ZGndC3tTssqfDQmHezoabDFLe4o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسابقات‌فینال کشتی آزاد بازی‌های آسیایی هنوز برگزار نشده اما صدا و سیما به‌استقبال فینال رفت و مدال طلا محمد نخودی و امیرحسین زارع رو مردم تبریک گفت. "جلو جلو ذوق کنی کنسل میشه آیا"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30844" target="_blank">📅 14:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30843">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6Gjtfw1Ye_UFpUToWvULcuL_INlW1jcrwJ3OGIxw_88c3OYfTkNmJ1pixY5kwwxx5tEjfKwrub3gXeNL2RhcOrKk_OLzf8tMVG_armb7nHhfqCABuxaND5T2LLadGxMafHlj40w_sy3wg1kW3nKq0UrpJuRav7tWb85IYCaBb_2bEn4AquTiL71esO48j9y6E181VWLZtHwAlXj2mlToKkGIgbU6mpYH4HZ7XvYihBWlbX14voaKWmiLY_Dfn6s9KTAPodrWBvu5Ug9vOwoUW8z5bdOL2RXAn0lle3HIURp3JGslCw66rN6RovJbEziLu_5zHrJNfH2qtWsNLhJCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نرخ‌امروزمدل‌های‌مختلف‌ کنسول پلی‌استیشن 5؛ قیمت PS5 Pro درعرض‌تنها کمتر از یک سال از 40 میلیون تومان به 315 میلیون تومان ناقابل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/30843" target="_blank">📅 13:49 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30842">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkUWdPSb6GYWyrNusW_thDyufpd1XBnWualKmsqlODmqPieJfekM0fFBipP1OjASlo61qCsjBReg0IIsINhgA5K6YgMfXod67XwBm_V9jlP8SCj55RkFzqObAkc6_HSWlGSOMJtAUzczhllUDOIfV4Q9SWfFDtPIVnHzTDnU23qRuBV7zo3KKtcT2597C6F0nfr0WwIdIg4KwPVYKg15-swxFPNERz4W-eNRudp3NzFjP7GyVc3Lv25VVSfb9bXPGdDPj5I8biTJ8FEqUFdblCTZqed7mZV1c_e4thqC1UhHsMrGaL1xqEoPX0oDTBS_52kMqT6mbJp_cATMEpVzOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رافائل لیائو:
پوشیدن‌پیراهن‌شماره هفت تیم ملی برای من خیلی خاص بود چون رونالدو از دوران کودکی الگوی من بوده. فرزندام هم در روز هفتم ماه به دنیا اومدن و به همین دلیل از این موضوع بسیار خوشحالم.  تمام تلاشم روکردم تابه‌این شماره و این پیراهن احترام بذارم. از این پیروزی خوشحالم.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30842" target="_blank">📅 13:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30841">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxT5cascU64Jqa-87IeFIxClECR8M_xrV7yZaFFpiQF6EIhJt7hLaIDeJ3SyK8oPPpSfXosyW1Ek4K6IIF6mQjJkmM2ABfCPN98u6ON2v7NDb843RhP0nPbWDc_IN3gXTOMV_nb8aKi4zDa7HPMQjF3XDMj5IcA4bw8BEXEEPYXkCA02ZxgPOTAhT0uvBqkOggN55qIMFsFCIc7QPpFYzvQrFDK9PeB9rw7jSkLzc00ulWunscEr7WESYAnZ-yh6XOYYQk7I8_KJja4RyzST-ZnrzYZN-jvefvJ_Ug3GB2kwYVb32J3LPJtHM4003TUEJeQgpXjqyP6yIEvwhKIZPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بهترین‌شماره‌هفت،هشت، نُه و ده تاریخ مستطیل سبز با اختلاف بسیار زیاد این چهار نفر هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30841" target="_blank">📅 12:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30840">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaNIqRG2Bmd8FvEzj0njNCtR1HCba581NUPkOftCHV55PB0Zu4D1mXET1JoeZYTsA2gYSsoe5DSxpF2Pf641-pIItSBPhoxPUT6q1W0u7pukG-lbn3KUPRkCWg9Zdig34DoCfogf4MANkgLP-Kjj8Ub_FHzeXdvH09b2j5rOnDDNoJiH55OSiBTktZSrlvn6dskUNzsRrrceBMdyy_KGeWJDHVySsXN45kJtYodDmpBiVUyKyNr-FLqaNGwiuM09X6DEkm7CjviZJpdxctvFWiaUz06TQLNO2iWHclzCPy720UnUqa6jCzf-DSp9-kmUF7ar-jh_4UtNtJlV4uK0dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه افتخارات لیونل مسی، کریم بنزما، نیمار جونیور، کیلیان امباپه و وینیسیوس جونیور!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30840" target="_blank">📅 12:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30838">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdKiS0qBd5YzrfEbdKSNcyy2Q1duWl3vUKE87lAMb1iaahRHy3qxDnxucr45HsCGfw-yoj80vw-l8QUwPcDR1i4HPY12gwzmZWA6I79DQntf4Na5HoZTF_279gmx9gSyA0coVf-5idkLL6kwHRyb38JNrS4MXir0pohQYmexoB7kye_fiQ2w8WecL-C9oYFOnQ1vs23dNjXEzYVevdakBoLFbdy4xrpCV9Y08Z5DhwLQQ5Pytx8uYfxP_KdGyxazDRtEQ5wNUsSov1-bX5sUPp2KwVehIIu8R3YnteIr6BoTECH0F4yTQEFq9c0qXsCaf7s7D99rVerZ0cA1gI7D7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه بیلد: سران بایرن مونیخ از موندن مایکل اولیسه دراین تیم مطمئن نیستن به همین خاطر دارن تلاش میکنن که فلورین ویرتز ستاره آلمانی لیورپول رو جذب کنند و جانشین اولیسه در این تیم بکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30838" target="_blank">📅 12:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30837">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0rxQ-wZaFAgrLErADjPf_0_MUB_pqXY5PvHGQlNqQtsB9VCfDE2ogp-XAUC04vdaorYckUzT2eDnXzlIgfNFCDch5pcocm8IWjdmnvUk4dQn5B5R4IWzZyMTdAoiEI4MaDH5aC2t4QMLSduwuAu6PJxXxDhjoZzT81gEEwcx46RI5H-Sqt9c2u3DVkBNwwLDycMuK5gAXa-ZPI39rwBX6f7JNJpVNvxfbIXS1d3CN0SIJYMQcO51bpFY2aMMyeDZ4jzqwbeSeC1eyDDJ8TtjmxpTwVz20WQpEcbngKloBbhhCmy-7NqKrqRk5aS_vDGtLXCmgGSxiI6Fc1A3_8psA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسابقات‌فینال کشتی آزاد بازی‌های آسیایی هنوز برگزار نشده اما صدا و سیما به‌استقبال فینال رفت و مدال طلا محمد نخودی و امیرحسین زارع رو مردم تبریک گفت. "جلو جلو ذوق کنی کنسل میشه آیا"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30837" target="_blank">📅 12:14 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30836">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dc2bf5c9a.mp4?token=vv8sK2vXhnjtVwp0kqPomVeWdsV1oyOd2GmvH_6kDxj2bxGBh6xUa336lRyh710T_7Xq8Ht8XJrXPeXULAD42AON--VL48v9akZznbY-gLFam4KutiE6tFjKgzh42wFOcC38Rx9RmGFjnSCY_V-TVZG24R_4OeEo6sNfxkwA4zYuZyXs98ydJ0Y_PFx8fc6Np8CuhRDyyXj2ZlwZDj73yZ6EezpW5bf2bPecbal0sMly_aN94dS81QzTVpu4etZ_ltsb-hXaufjgtGwe__yTV9-pN8zQkuM71uktgS9ePEoPLm6WgLjNP6UfiqT1tlKjXJZ4pEEzVQBpKkHc6KguUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dc2bf5c9a.mp4?token=vv8sK2vXhnjtVwp0kqPomVeWdsV1oyOd2GmvH_6kDxj2bxGBh6xUa336lRyh710T_7Xq8Ht8XJrXPeXULAD42AON--VL48v9akZznbY-gLFam4KutiE6tFjKgzh42wFOcC38Rx9RmGFjnSCY_V-TVZG24R_4OeEo6sNfxkwA4zYuZyXs98ydJ0Y_PFx8fc6Np8CuhRDyyXj2ZlwZDj73yZ6EezpW5bf2bPecbal0sMly_aN94dS81QzTVpu4etZ_ltsb-hXaufjgtGwe__yTV9-pN8zQkuM71uktgS9ePEoPLm6WgLjNP6UfiqT1tlKjXJZ4pEEzVQBpKkHc6KguUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طوریکه‌قراره‌علیرضابیرانوند دروازه‌بان ملی پوش تراکتور بعداز اتمام‌معافیت‌اش به خدمت سربازی بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/30836" target="_blank">📅 11:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30835">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✅
نتایج دیدار مهم امشب هفته سوم لیگ ملت‌های اروپا؛ پیروزی پرتغال در غیاب اسطوره‌اش و شکست‌ دور ازانتظاریاران‌ارلینگ هالند مقابل تیمی‌که کارلوس کی‌روش در جام جهانی 2022 اون رو برده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/30835" target="_blank">📅 11:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30834">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9446cc89ef.mp4?token=b9TIJ967jBmXwy0M2hhV5LoFaPyQA1dQUBk-iksNHHMmWGxQwv-bLGmYrKa6DUNni7kzNNAGWta2fRvLG85gF6AvVuaTqH4sp4mYr2i_qmfAJm484byEslEOywJ0yevSt-BYbPWpY42bYSWWces7ZkPw8GjqFt-7rlZQ5akF73slDhqGwMyW3RgNtTHE93VtrP95xoIz-_gB_COFFjHUuK9o9UdWXVppYC--I9KVI8U6CF7nMc-Cko9sSDIzOeiE23xOZDid1y1mbg1o4UFuvectUutFmQck0mQT5q-Cc3W19jbVl85aR4_caWfnpFLzUooQRJGZTtJOlLUqdSYvzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9446cc89ef.mp4?token=b9TIJ967jBmXwy0M2hhV5LoFaPyQA1dQUBk-iksNHHMmWGxQwv-bLGmYrKa6DUNni7kzNNAGWta2fRvLG85gF6AvVuaTqH4sp4mYr2i_qmfAJm484byEslEOywJ0yevSt-BYbPWpY42bYSWWces7ZkPw8GjqFt-7rlZQ5akF73slDhqGwMyW3RgNtTHE93VtrP95xoIz-_gB_COFFjHUuK9o9UdWXVppYC--I9KVI8U6CF7nMc-Cko9sSDIzOeiE23xOZDid1y1mbg1o4UFuvectUutFmQck0mQT5q-Cc3W19jbVl85aR4_caWfnpFLzUooQRJGZTtJOlLUqdSYvzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
راسموند هویلند مهاجم تیم ملی دانمارک دیشب بعد از گلزنی به پرتغال خوشحالی بعد از گل معروف کریس رونالدو روانجام داد و درپایان‌بازی هم وقتی خورخه ژسوس اومد باهاش دست بده هولش داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/30834" target="_blank">📅 10:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30833">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rV4aEb_5ulL8GXujUNPRHwaqj8juUUhG-YP6LddcJswoSOPjan3QPi4C3iy0GkzqV-_B5DEsfDG2dZYJRj-ZvglMGVE0VK8Cnzehl61kx5qlWFpDId_FaPUywMV2RvXgtBtVqmQpCwKFIO9Y1mK2iPqwu6x0g28QQrwfkwhPKK_2VZq2nrwObo8Jm66yHoGB-XmZkrbBdoxSWH0owyOYXGAUq6Vo_aEc08VGKagt9Ys9bNaPnVKsABr79qHv1zd4uMbxsxwaPPVCGCKQDfFmE0s7qlPekCkBkZNIbNxaP2sb_tNpzsHJXwVxHTgRxEttQelJiM3jXG76fV-OHhg7Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
👤
#تکمیلی؛ مدیرعامل باشگاه ماخاچ قلعه روسیه رسما مبلغ فروش محمد جواد حسین نژاد در نیم‌فصل رو به رسانه‌ها اعلام کرد: یک میلیون دلار با 15 درصد از انتقال بعدی محمد جواد حسین نژاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/30833" target="_blank">📅 09:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30831">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1cd6a61cf.mp4?token=ZQl_F2-WemuQu77Vfc1_j58Xb30nSHNwFTK2ZRCH_ARnPC8bPKnkX_w-dTsHeqfHj6u7j8KvsPiZdGeA4kZluQh1xYq2o2u-smGK46BCTWKQHg702A9ee2zPRPUWwPXP2Sk5I5FmpUL5E6wVaGPit2u5iubDQJob_hC9rUDkpspX-oUzO2p4PbMF2VfHfHoJL-DcTkRO-51xxfwvzjm8czZSmjjimesWm1U8YDRMpHDGYaei46OLsikoRs5DDhm798ZDAazBqgEw7ASZyacoQtENXIPgufdqVK2I2yjfXUqEWnC8B3XM8TfqYFx4QtHWSH9OnBg2gv5vjdq7Py9xPbn26gkmmCEIXdMD8V2fxcGpFDkS6FTMKQzMZHL0Yechu-0oMPdtv5JX5UOSj3BRxlNrv_isR_7Vgg5b_icTbVqWVbEyjAUsEWCT2D9ih475GiT8JFZ8I8qeCUFtTLiDcrWiLjU00anQTVBKJGT5TVuEzGmS89CIjMdMh2IY8QxpoS-PD15Mya1TVAj5BTsrnidTk3tj3QyZZ-yCfkMvC0z0_GTr4xSK2z08zy4GB0-rPGHqzKymsYAW4T4umtf8_gigU7BwL7dph6Cavy6lSXMKb5e29-LTVvPXsMR7N6XONRgDTLsEjGzEycfHXQm20qNv4kDYV3zFNsYtn_xrKA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1cd6a61cf.mp4?token=ZQl_F2-WemuQu77Vfc1_j58Xb30nSHNwFTK2ZRCH_ARnPC8bPKnkX_w-dTsHeqfHj6u7j8KvsPiZdGeA4kZluQh1xYq2o2u-smGK46BCTWKQHg702A9ee2zPRPUWwPXP2Sk5I5FmpUL5E6wVaGPit2u5iubDQJob_hC9rUDkpspX-oUzO2p4PbMF2VfHfHoJL-DcTkRO-51xxfwvzjm8czZSmjjimesWm1U8YDRMpHDGYaei46OLsikoRs5DDhm798ZDAazBqgEw7ASZyacoQtENXIPgufdqVK2I2yjfXUqEWnC8B3XM8TfqYFx4QtHWSH9OnBg2gv5vjdq7Py9xPbn26gkmmCEIXdMD8V2fxcGpFDkS6FTMKQzMZHL0Yechu-0oMPdtv5JX5UOSj3BRxlNrv_isR_7Vgg5b_icTbVqWVbEyjAUsEWCT2D9ih475GiT8JFZ8I8qeCUFtTLiDcrWiLjU00anQTVBKJGT5TVuEzGmS89CIjMdMh2IY8QxpoS-PD15Mya1TVAj5BTsrnidTk3tj3QyZZ-yCfkMvC0z0_GTr4xSK2z08zy4GB0-rPGHqzKymsYAW4T4umtf8_gigU7BwL7dph6Cavy6lSXMKb5e29-LTVvPXsMR7N6XONRgDTLsEjGzEycfHXQm20qNv4kDYV3zFNsYtn_xrKA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
راسموند هویلند مهاجم تیم ملی دانمارک دیشب بعد از گلزنی به پرتغال خوشحالی بعد از گل معروف کریس رونالدو روانجام داد و درپایان‌بازی هم وقتی خورخه ژسوس اومد باهاش دست بده هولش داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/30831" target="_blank">📅 09:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30830">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drPD4z9jlF_mpOYhM21MJAcTdAPUbbt2jg0Mb3bxRzZQPH3JMgyykdcL1hHNJbxtlHyeCP5aacn5PjrwQW0qbecLWKc8EmCkk8P9POQDpaXMml4alRgUlIcPjkcaJXfPULAsoneHP2HS1llgvqbZfVZ5J9aSHMvbxQUDU7LPeU6ZZ-dcO5MZA7facEoBG6msHZtX3vJKi6QIRGg1pLQbuxDbI9Bd47WrOrZhMZtNJ4zg1Fr3T1qvfTOBR9GK7eji5IQKMEbzzhI901RuQZx8XXVsRk4RtCBsK_26_IedycQZ0nVKhs3dm63gki6xBoQr7FJURmI4FfH9NtPpB8KsEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
راسموند هویلند مهاجم تیم ملی دانمارک دیشب بعد از گلزنی به پرتغال خوشحالی بعد از گل معروف کریس رونالدو روانجام داد و درپایان‌بازی هم وقتی خورخه ژسوس اومد باهاش دست بده هولش داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/30830" target="_blank">📅 09:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30829">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEta5N-wf0ct2GGMxjrnzeo2_86hFAQXzG6HtbtVrkxh-dSX-vWLA0VXO2UHKUJ94G5uzadQPJ1sfChWXHMxpysD4V84Z235GuDGqpasf97KSTQS3lHDXMCnqN6AwroQpKzjDjJoZCec2f-BvhLHQCjOA9g5Tnadc27epLpfGoEV8gbgf8Hh1iN7F3-4lr2MUzAAZ2uL7kpHXGvykNijW1OGChUx700kGQE1yPnpV0GrXGC4g6ECiHZxxfAMSTK2GLFnr0XVppfekLzPDIFgojS0N2RRDwJHExe876h8j0qYjyo5z4doOC9f9Jg8EBePrEZ79slESKHgW8j4xV7qMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌خورخه‌ژسوس‌سرمربی‌تیم‌ملی پرتغال؛ کریس رونالدو فوق ستاره 41 ساله این تیم در بازی فردا شب مقابل دانمارک بازی نخواهد کرد. ژسوس اعلام کرد مشکلی با کریستیانو رونالدو نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/30829" target="_blank">📅 01:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30827">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POlpMs04wSNQrc6vkXP9N9u9mKWIjwPpVax1gxqtSOJ0HJLJYhgkSDUiRpD1l4goUU_yjDis_142RaL_k20D18_ddVDGUeoVLrrNbihFW9HJu-sTjRSbrOHjNBKtzi5QEnhNaOVdhIt_ooFh9BJqvlxve5lxGPwZ3TxkF1UF5sMGon2hI_vFQGZnhnOu9E4OiHtbbtckWR5f_p-KVNqOe8VkPEH3JAAH51DdcwL5IVXIxMECpy_j8rs7Nv3fULlRPQ68eKrdyVb2sjt2gD-tu7KwgxMjr32n7GqBu2LpwFyVEASG_4lpUNXD-NJyCKmjYiZ5EfnPIG1ounGQ3K5xtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ رویارویی مجدد و دیدنی زین‌الدین زیدان و ایتالیا پس از فینال 2006 برلین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/30827" target="_blank">📅 01:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30826">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1P509fgeZcL_cdqVRoqkesxtWNcNWz-21fnA1ZPkkREqQCHflsq5p3FimOkH4g37v8Mf0avcermFkL1o5KJyb9JG1_cBBtZKUAMtRacYyX8BK8C9UonYtFTfhzhgLHG-pZBHRIz0NAisApxqJet2YKwBh5hocLU22a7ThdIPYiV5UVEC0dluFjjSD46tbfRyrnw1__DH4uMrgV7W0_Ct2Jm2mKnOCfeA0wbC5peHI2qgkqAEipO1IvxIlPKxcdYmOJALT5aCpSUCTQ3B0E0IQ8IPHizzupA96zgFAZfIGf3EVm-SH2Okjwh1p5JFTYZrfh3DLfakX4VyzXm-FH6HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
از اولین طعم برد ژرمن‌ها باکلوپ تا سومین برد پیاپی شاگردان ژرژ ژسوس!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/30826" target="_blank">📅 01:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30824">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/leCKKZTIBrFhbiZb0Qi22JMJZQH2qDe9VL4Dk657iy889qRGB5PoroWmeT1Z-ehBeYTBxTNkukCbCd28WJbO-ppkoK4kz9z5rYDkwkYmQZyGKKwCQnBH3QJce_6R5o-JTYBnUcaLRsnSnsLgkBVTKeveMi8M-oocgoYFKRdRbkmLebbIAXPsXFsroSA9LiR0RWOSfKMbiDjSOGC3louZ8_3uleZp5T0YXEMw0lUXZrUDMGgfl55pc7a8T9iwvjsvVZ4nUur3ejQx9ZfUior3Gek9YJtohxsE9vyoqiI8PVLULmMJzJw6QJIKIePGACtrk4ltuWKpNY0U7kWu6yk4pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رکورداران بیشترین تعداد گل زده در بازی‌ های ملی؛ کریس رونالدو با اختلاف در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30824" target="_blank">📅 00:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30823">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2U8uRHFWH-tF3FKRLDWAAfr6BALoKEQEuW-At6SLfnEdDzmmBESlPOXWTXVhnesppxdBjwbMGpMEatsQIIG64J3sYO9UU_mibO-9Op90aqNYKb2trpsPeJe6pBh172LTzFpPQiFhwmaBSpsTvl8ugb9HsubytyhgyitmvuYeXHM-ODKSz_S46LJUcouqLMMXdAiwIBFWms1HVqf06UdeJs3ScKkbxCQJBYamHS_AtlzEH3X7_cGDb6oefVhw4P9fx5h772HGMUCBdd1YC73-zAZOt3Ji8vv8VyxQWGgHiWNp_kD6xHIWFi4OtgQJN67TXbqgkqZ2CG8b4dKkOpVoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ابوالفضل رزاق‌پور و یوسف مزرعه دو ستاره 29 و 21 ساله تیم فولاد خوزستان به احتمال قریب به یقین در پنجره نیم‌فصل به ترتیب راهی دو باشگاه پرسپولیس و استقلال خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/30823" target="_blank">📅 00:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30822">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1JUqkBNqJHQ6-yMDkNTy4lbHAk8gZZ3Wq53MhQjCt8XJOw-5px_2qOUx3lQ9pXyZebJKXu2OA6GnWSzL9Glmta87OIzUD_WP9TBM1Rl5LmQbAOkXLPuSvWc8vpihWchKkSaa_6bLZwGkMfD_j3eJoqaL8AYIrgzvBbkiYSSYvFGnYB2sOAGDDoKVdULUu55ZuXTmUpwcHBtbg0Rjffr89LVwHZwIvn7VBx9Gu6C2cSaPeolTu3FopQwqeJnEOqJfoAQx00bYJnxsA1FI4CMdXkfOcNEEp2qg5PoOSsIPDnJrFcz8_IDkpSzOxN6tOwk0A0pty3f3k92DyKCfeEqiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛ برخلاف پیش فصل؛ حمید مطهری موافقتش رابافروش‌ابوالفضل رزاق پور به پرسپولیس در نیم‌فصل بادریافت 150 میلیارد تومان به مدیریت فولاد اعلام کرده. بدین ترتیب با پرداخت این رقم از سوی بانک شهر رزاق پور پرسپولیسی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/30822" target="_blank">📅 23:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30821">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBZxEvYekMeI8z6L_7vyOxIQo3Gkxtfusk3e6odzHBFwGyvwOAVxfl4OhvU4POHyoTTMiaQPi3FyBp07eChM-fJCBO5GovjG-ul_rgWiyZ8o9qM10xI9zZFJBsxiCsf1XhyLk1AJiQnP7O1VCX15KS4KDFDtViKN6wRd9V-xNh7CNOtqv2c3jo6Zf3B3MBJGoNowyzAQBqdD3lFEocyqBtnFn4xUMRc20W9XhAxqXOYo1C3BZ_wCSbKCjh1s8bp0u_Xap6DHauICWwTe6TpLgp4ummaAlDI2Z6C4jQaJkKUKQqxBSmMghEi7vXvO3e4jPFPumPCzcvrRxC9gaaqb7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب‌فوق‌ستاره‌هایی‌که درفیفادی مهر ماه مصدوم شدند. حالا مصدومیت امباپه و رافینیا زیادی جدی نیست و از هفته بعد به تمرینات رئال مادرید و بارسا برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/30821" target="_blank">📅 23:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30820">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nx5-IPkQMmQ74h29LMTg06NzE4Q4UBkyQchkKCQ941jb70e53lRpUU3M5y7cHa6HBODrAs_hDEtKqryke46uMSanzE9Ebl785KtwAp8PW9GCiQQN8brzMMNmty6nSziRwNIRKQ3NcevnUgQ-nZVY34nIi0Qr97aoBhZMoDihMdXbw3foJxCA2kRht2jY2dosmbJl49P-mFq2kv3kgThbwFZVxVOl-nDh5LtsvtfYhN85gOYoA26Guykl1F1QRC3LUmq3i98fBX1KsSuyeE297Hjefdyn-xiUncNOA3z77e76AZvB-fkDdI1kjlhCg175eaSAObRG53W0oEx8ll6V1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#تکمیلی؛طبق‌اخبار دریافتی پرشیانا؛ باشگاه استاندارد لیژ و دنیس اکرت برای جدایی توافقی در ژانویه به توافق‌رسیده‌اند و این بازیکن درنیم‌فصل به احتمال‌فراوان بعنوان بازیکن آزاد به لیگ برتر خواهد آمد. استقلال مقصد احتمالی این بازیکن خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/30820" target="_blank">📅 23:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30819">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twkZ-dxXcevZpjWpT0Kt79zguOP6fNnQ_sziLlmXHILWNsZUCOtcNh8guIHXqnHz_82cf8dnL_uHahYtbC4I3Rzob9i81GuRIDE7XG60GpCbTVANNDlcdlbAt3Ajz2W5P3Lsl27uxBsNNM_Gif8niODGcnzihComc67KGImMBNXgjHGVSbAz-YpjF1JzK_tdfh-thkUgAFZoeYCPcUzCQRwTLQ3QPl4pVOCPbkG5-bu5dzkL8exRVK-9pKEfLt8ItT-F2fl4sdu511scJexcWeXHrGDGU0j45sbK8SQRFR5AtCdsodwUWtVFgnxOT5rv_pRTQBDaMMJgQs3alWp-Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#فکت؛ پرتغال درتاریخ چهار بار به فینال یک تورنمنت‌بزرگ‌رسیده‌که کریس رونالدو در مرحله نیمه نهایی هر چهار تورنمنت عملکرد درخشانی از خودش به‌ثبت رسانده که منجر به صعود تیمش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/30819" target="_blank">📅 22:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30818">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWR-nGQu-FsfWu2QpjBuxZKXRVWHjsSDB0qYL0RLy1H2k7MdTbjEwAJGUNRNYnPu3qh8MomV1ZFpC2IhXEiNjKYqzHuX6yJ0ULZ5sPlT-ypyVW9PHXOyNYuHiQJnwGGEAMT1x3FAnwREavmtXdwXLrMoXfdtM_bACBMrEOsYlsC9oRqzq0FgQS6tjbhcRJfuhhp0CByaaf3KvDiBJtUH5AByAuu1wJ1znnKZH7v2RP6T9jwYl3U-V-xkkMl49KSauGNMK321Ol2TQ9j2VtJCiYBhCvLsRAgLiLVLFbRd5Pahg7WFrZM97NTkranVZzrbOj3GTOqMAkMOzOtZ6fVyGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تفکیک 146 گل کریس رونالدو در بازی‌های ملی برای تیم‌ ملی پرتغال به همراه تیم‌های ملی که بیشترین‌تعدادگل‌رو ازCR7دریافت کرده‌اند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/30818" target="_blank">📅 22:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30817">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZV9Ma5lB6Xh7J3lkMcxA_HnK22emPntvx9B1rgif5N_fE93R-8KRcNnL2g3nBkdUf_STySIRgN68lXsflwxdPwt1Oi43h0W9j_ScO6x1UjEumptAt_rITMHaaFqbI9X9qy06K09iQQFgRAzHr2M7UFbqGeR-MMWhsQLfQlANq8eOMEe3ZuinUpRn3FeKikROeg5MC-zVK1RVJQnjuGDLQr0O3dxhHq1GgKhQaxKtVX1vQxMddq90PsCE9KAazKsz6BjC-iuYJKytOTaaBzJR3hVq-XccUb4hbCK7_XM5T5zfQloUpijSWfv98-CSEDBtS9W-TLs7JfAK551WphOCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رکوردزنی‌تاریخی‌حاج‌صفی!احسان حاج‌صفی با حضور مقابل روسیه به ۱۵۰ بازی ملی رسید و با عبور از رکورد نکونام، به رکورددار بازی ملی تبدیل شد.
‼️
جالبه بدونید اصلی‌ ترین دلیل دعوت حاج صفی توسط قلعه نویی؛ این‌بودکه احسان رکورد بیشترین تعداد بازی علی آقا دایی و جواد…</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/30817" target="_blank">📅 22:41 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

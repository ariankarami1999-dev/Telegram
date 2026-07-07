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
<img src="https://cdn4.telesco.pe/file/jv5RsXZJTwr-9OF_Sc2Swus_8lRIF-IoUdzF4bGTNCYz-u_wHC_F9u8OL5bjhwOiTWCRvGfgm-B7S-nmT1BbdFXuCfBnOg6zKwTE3zfGr3lAiEPIPl71TrPf7crJNoMozh01qUdA3kmu1fB-rkHaT9BUfwnDPgDyan6u5MOnMP7rogXpChHq9A90XohYWbkZOnAeqD_5Q20Yxxe0Rd0ubBz4_K8JVAO4U0frii41EKUmZ6COrUc8Vlckn7WVgeQEWrldttbjQBXQfjJL_XKL7VktX5wXjlUMpjFNRNzRkXyHLE2hgfxINVYQ7ntvmJoZ1eQEMu3kVvlrxwsE_OVK6A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 422K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 19:49:56</div>
<hr>

<div class="tg-post" id="msg-25163">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyDeGUTAgeSvXlsqqP1762C7XozoPjbg79NUcS9eAzdgBehXp27BAxNlZ07ha_J_o0ToooSvGrmp6f4_v8FmkkXo6YcWoIGHoA0EfpwP7eq_dvEC-WJ9S6XtHV50FbBv-LKc1fF5b2heiSgu8xitZ4rmsgyK1ku8XPAR4bkReEIn84TPGbWjhZPpvx-Q3hYn_lMRp2lWEkJwZ-OYnWgqDnXCaz-dz_hgpLVnxn6qf0_Baethe3jcwDEDrZ34vlQXj_0DBM5D6ifb-UzRGt5YedV7Fr_Qj5l50By57SD0nF0BseSbhE_at0RkXQtZLDISFitTqmYBzdD4mAjn5IMCfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/persiana_Soccer/25163" target="_blank">📅 19:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25162">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnBMyirs-eJR9rAec7KbmUtMjj5t-4TaXBGecmAd8S3aQdYENueQuTNF-TENTrsDoSnoKpMohFdmGL227Naf4zFHDrPtoPD4ckKaXueSINVl41EO_d0QTSwPz1mccI4YE_OTjHYHVxa-nvmz-yv3uBejeks5mEKKdj1osrp8vtgYNtmwhSnGQubBdLcFfgAgXBVPN3nXmOcH4_oQlxynbGSPJJOK7gzQryGv2OOzjlTb8AdV9a8NFsOB3lfUL8jB27-JPKZk6xhzDSufOjuvYIG12FZXzS54XA5K00bns_h3cJhhNx0NQ84nntwZ-M8FS5crw3LLRxKPJFtH_ukCrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مدیرعامل‌‌تیم‌ نساجی: برای‌جذب دانیال ایری از سپاهان، استقلال و پرسپولیس آفر بدستمون‌ رسیده اماتا این لحظه باهیچ باشگاهی به توافق نرسیده‌ایم. رقم دقیق رضایت نامه دانیال ایری رو به باشگاه‌های خواهان این بازیکن گفته‌ایم و هر باشگاهی اون مبلغ رو پرداخت‌ کنه…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/persiana_Soccer/25162" target="_blank">📅 19:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25161">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rl8xIxNC0Lkx4rcE6oSu-QJ5LLI_AfT3qYmfX3ek38cRjmw7rZGmPdSSrF4w7XTASGnjPXtoWA0oYaUjrZ3FyfIGKHQGSZkxUHoDTZpkRIpGfFDR_gM5ABo3U0x6P4EXHNPENAxPl5jksZz3V_C2aJEoat2LgaOdzbc0Tl9opMK5no7zS-32dSBY_eG_tY_jeqxrTk6Rev345FHxJfA0GgI4wxBv5iBL6fGsRHq86Rsj5xcuRZ50olCQ6LywRvh6R5rIz24RdF5V3YHNlRGQIPfPIAQQSi8WR2chVxfWXRTSRsHPkshaebTg79rgyqH6QQJ9IerTe7EV7RWsXUq5gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودارکامل‌مرحله حذفی جام جهانی 2026 بعد از صعود اسپانیا و بلژیک به جمع هشت تیم برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/25161" target="_blank">📅 19:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25160">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d97c61ff.mp4?token=ZGtWPrTp5-YeGhmEpFGUzXyAmIJQ8uOLtnmkhV3bOsishEPP_95Cr8gatcZTk-OUJA_wjc733EBkGlLMuAY8C6MWgbZXRLcF5_tUXKLQkMzxdIzt2rszii2VgiERqXm6UPuwkxTwcx97jsKvErp3UcfPtZAoQ2FtW9UC9pmXknBw4zE6m_cAX-8mPH2AxOTF1GZV3wziPvDRxcD8bu8Un8qzwJw8SzS-gXH-oDIJmedui-CEAHWPBKsUtNw_zRwZgsF85hMMR50nH6nwLF8s6MwqjyJV5pnzDyDgrNVWgpmbT_sUdD-1DYi2ry4r7GI-DoQGg1kuNgq0i-UrECiP6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d97c61ff.mp4?token=ZGtWPrTp5-YeGhmEpFGUzXyAmIJQ8uOLtnmkhV3bOsishEPP_95Cr8gatcZTk-OUJA_wjc733EBkGlLMuAY8C6MWgbZXRLcF5_tUXKLQkMzxdIzt2rszii2VgiERqXm6UPuwkxTwcx97jsKvErp3UcfPtZAoQ2FtW9UC9pmXknBw4zE6m_cAX-8mPH2AxOTF1GZV3wziPvDRxcD8bu8Un8qzwJw8SzS-gXH-oDIJmedui-CEAHWPBKsUtNw_zRwZgsF85hMMR50nH6nwLF8s6MwqjyJV5pnzDyDgrNVWgpmbT_sUdD-1DYi2ry4r7GI-DoQGg1kuNgq0i-UrECiP6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت‌شب‌گذشته فن‌های کریس رونالدو بعد از شکست تلخ مقابل تیم ملی اسپانیا در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/persiana_Soccer/25160" target="_blank">📅 18:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25159">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99da3bbab0.mp4?token=nfPYHGEsIPDbY0yDhY6aWozDhoCkUHzmkDtWEGabCrO0OMQI1tHxaUM2DAu4UOSTSkze4jk8o0yhVzcvR2XHrDBGdodhv-u0yRc1ld0VUO0EtTMOC0de9aisMp7nxDERwq-oaVB7dU9LYnWtM6ua8pMaL3_n6jgjODkCCKwrys2bBx0x3YK4FngCdsrPX7d73MXM__AfXUP3zLl0AApWCjpAwyNwDLRBS-I0L3Va3Cm60iNJbIndadFBFzXGV51JqPz-GNwUxD5-IBEOrA8cc8V0D_AhPtbQWpmBvpPbze7Uhru3lch9L49jgFwoWQ-IAJDo26kH5IFZQrOCZrpZmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99da3bbab0.mp4?token=nfPYHGEsIPDbY0yDhY6aWozDhoCkUHzmkDtWEGabCrO0OMQI1tHxaUM2DAu4UOSTSkze4jk8o0yhVzcvR2XHrDBGdodhv-u0yRc1ld0VUO0EtTMOC0de9aisMp7nxDERwq-oaVB7dU9LYnWtM6ua8pMaL3_n6jgjODkCCKwrys2bBx0x3YK4FngCdsrPX7d73MXM__AfXUP3zLl0AApWCjpAwyNwDLRBS-I0L3Va3Cm60iNJbIndadFBFzXGV51JqPz-GNwUxD5-IBEOrA8cc8V0D_AhPtbQWpmBvpPbze7Uhru3lch9L49jgFwoWQ-IAJDo26kH5IFZQrOCZrpZmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت‌شب‌گذشته فن‌های کریس رونالدو بعد از شکست تلخ مقابل تیم ملی اسپانیا در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/persiana_Soccer/25159" target="_blank">📅 18:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25157">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B5loZ70G-xM_A9SqhA2H1OeTDXJBMSDTuKZzd6kI4uQC_PHEu5FT8mVQJADKRFbimzfWn5oVCDCxQhSfpdIkrJKKXyT_UoXKQr_G7ajth424F2kVKm62wde5ruO1DsMiHKRvNWGPOq9g7ENCsaVcYv7inL50G5a40L95k80nRm5lJswdyzRqkePuXgMyXLydz5wO5hHzSwYn9E0PQPR34Rdu-TllFUxOfGxj8_IdMDBbT0v6w46mwyNPr0AD1nygJQn30iNNrZaDDtUc6-bPlmdxoHedgZyOgbkLPFIpIw7_I1OWosYkAsT0FBwit8Ah_c5SNpzbrZr7VD9ikO6V1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ci2eRtTDgwz7OeCC45fuXPSNc99vpNUQXfUSivEYHMENorscxIGw5ya3YY_xEBQQSQQoI_22_mRKq3OSozJWJCPIj3jzOM4d5o-GA7gTFFv5WOmmleFWOYREHjBEp2_sE1w98EGfhXU8_gh7oypDq8wG58GA_PkjUDEc4VxtKYJM9QtDlrStu7Xs1wcxLgfp6ralCGlv6x8-Kayp3s5PipZHBq3EpIHTKhpmOYZz4kid-QtsYaIFfxndkkc89hgtqgMUZPCgmbOT6fsTPxrscfA3z-MenCAJbUQyXZrPcBaQ1ALplBS30yQyLjWfuna_3y8RlYnL5QFHOUJwLDeifA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نتایج کامل دیدارهای مرحله ⅛ نهایی+برنامه دو دیدار باقی‌مونده این مرحله از رقابت‌های‌جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/25157" target="_blank">📅 18:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25156">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWMJjmWZ81wNp4-z16n86RmAfbDKMsVTlIpJg3nGKmZWzniW6noasm9cblYDdjfe8CWkWSX6fgGM2gZCCBhaPWRF1ZPV3olnyYQ5OJOX0zRi0z8I_M9S_LhqFApNtZV1IYUx4GKUNsqNChhgVEnMVImMryw-olRX8UbwNIq7Ppzz723ZjiLa25COi85YAhM88vG_x8QngDu4rOrhjk-WKB-Er6SwLad5fCpFOpYk9Kre5f3hIF8_PabxLfSq0Mg9BdHR4qCNDxnD7LRcAWe9490h8Zsf2_6nC6q1f_GrEm2l3FxNH4sJQWxP7-zTXM5cMhkZH-By9gLssSOOVoNVfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس باارسال‌ایمیلی به باشگاه ملوان انزالی خواستار جذب فرهان حعفری هافبک تهاجمی 20 ساله این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/25156" target="_blank">📅 18:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25155">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6llFZw3zUjIeNr8UWLqwyOF2pFtxvWq6aFhfaatReuGhMOrA1kRwdsDv5YC1b_iPc4eJy5rEu4vdqJt9vGwfCl8od4zJL1OlK53_1sDPFPd3CliR7l28sPIe3IBYR9_6K7R-e7Vdk2ka71GVLpejMLJFk2B6XG0rW1Tymht7bN8XY-vWEbAR2PXZ0bWmIx6e52MB0h05BBofSNF3Vs_68YNa7NZ4Y4t0p6YQhqVv34sY1DFsFE2Jwd3B16psYTvYHktlN9LPLPKr3fV9vGNkFFR1910NxJhdJ9oYV6S_Lt20xswAj7ZIS8h2UtN95wlaz0M1Zrt7VqOQAmwra4o0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
👤
#اختصاصی_پرشیانا #فوری؛ طبق جدیدترین‌اخباردریافتی‌رسانه پرشیانا ساکر؛ محمد قربانی ستاره23ساله‌الوحده امارات ازطریق نزدیکان خود درباشگاه پرسپولیس اعلام‌کرده درصورتیکه این باشگاه بتواند بر سر رقم رضایت نامه با اماراتی‌ها به توافق برسد حاضر است به این تیم…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/25155" target="_blank">📅 17:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25154">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVINSLVCnHlNkyS10b-Dyax2lbwdmq1uZIu4bXFJsY4lx45lk2tck7HGjQHwY-5j1D4Ka5gaSzKE-veizqLPtWKFewo26JASwzkBX1gBQ21xeXq5SjLssFka1Suld38gwTUJasq4H0yYN4UMqrNQHBncuTRmmOo2QEZMjjAHHyeRHJ28v3jlaTyWH4k6qdBVedgej3yGd7pn4yzwyFZHSoKFzMHx2c_m2l7J564V_fuMWszyDLebZnKH974mI08idhnN2CG18ukCWdqvJ9iJDNy3QiQc9u5b-JYqNLngAdhLM2slgwBjOZ7gbdQCZZ8l8-ZG7pUYWf8NIQA-_By9UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/25154" target="_blank">📅 17:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25153">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fem9yK052MkTHKyfxCwtbng8brItZgt7KxhYe-J3TV68wE6D9Izjuy9zFUsl-N8fs2-E5f5V398LVrPdtcRMqrUCgC1haLHGv5jmOUy6EwbnQB_SaTakG9tPbaklxe05EZifo1mtBhB1supsaK3Fe3Pk9HXRO2hIuxGSeq4jMBwTIIQfs8iqOF4IQFO_eDOBmu0IFiof7p6orUvT4pef0vWNZbd2sQCycpNGgwdezZKwq8V9etwDBpwFFcC9hU1dhskLwIFB2zP0OYQVtQi3hxVO8oZDD3Jqm5ZOzVrwRbhd4DWBHkzRoViHOwNKjsSakD0_8FUovC3a6Y0z-qnDGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛ ازجدال‌شاگردان پوچتینو برابر بلژیک تادوئل‌تماشایی یاران لئو مسی
🆚
صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/25153" target="_blank">📅 17:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25152">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2fRq9w6Ue5zW2lf3yYqyCQptvsm_vUYQrhIg16HJsS-eYi9io0661BiaUIWkrSi_pLkw7vuyYJhQXDo2ubOF4QPjNup374FhWTfVFZtbnFwW9QnLXLxVhWqT5X_Cg7km2w7G0F8-wbouVIYE3U1xAVinEOC0VgaDLuwMw13Hxpk_nMqdCx3LW7Hzdr6TMZG4LTPZ-_Q1-me-68-c6nZlRyFK-EwQkUPM4C1rt0GLImtLBs7nZZ2NEOXTQl_z5pBwvBTv_k4eZrMfFONKMpY24GUYEMV0I32N72kmCoK910j1p3QduNongt2hNju4ft7KurUmaB4318X4zNyjMX9Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا
#فوری
؛ امیررضا رفیعی سنگربان24ساله‌پرسپولیس مذاکرات‌خود را با باشگاه تراکتور آغاز کرده تا درصورت توافق‌نهایی بین طرفین با عقد قراردادی سه ساله راهی این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/25152" target="_blank">📅 17:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25151">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FaErQR-wB2DRuJllxriBNRKOPNuBey_IohJH0hR79EXp2ib45FkzY0L3T3Oke2KcDc49EFkOD52lPEaGnl7myBghyIHrjFtU2JUgrIJXniSfUhleBFxO1cZuXzjO5e9k2gio3lBxlHKk-dZgKy-P-exwIgz5mjp2ydZvw2q8MsuyNGymm-SUcPYo4ldAlcEnwVCGIjSYQ65GRc7ItxE0Tcb_xxOpndn5cFugevthTeikn_-jy0s7LI6zNAdvD7fln-gSO8Ki7Br_dns9RC2iejcnjBS7K9bwBD644MUlzi2kzemA2o9ch2wumGNCPiYn4rTbA8-S3yJA9bNxv_qvtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
👤
#تکمیلی؛باشگاه‌پرسپولیس قصد داره که یه بار دیگه برای‌جذب محمد قربانی یا احمد نوراللهی تلاش خود را بکنه و به زودی با ارسال نامه‌ای رسمی به باشگاه الوحده‌امارات و اتحادکلبا خواستار شرایط جذب این دوستاره ایرانی این دو باشگاه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/25151" target="_blank">📅 16:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25150">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_vmA6PrJ286NKfC47fTG9ulDrBXjRkvupbfKcGGTBJ5sYtN5LXvtzuEBNPKhlDFQb60BV5sMW2pUTPUzEnZoR9vdVnQAITKUm6Ac7Te2GiCYuZhXMQFVPAHTefpGGGDr_n3udU7xSEN7L-LnqrRoFFpXUO29i0Oa2IJRiiS1cESw1jgm0z4uzZ9Hd6pldQXCH-J5KhCKVJnOoMtCngqGiUzQA0pH4cec9kOWoNw5UHdUrjFXqbUpB31Xaa-ysSXpttlLlCSuwLOC9i4EQZoXRm4IlYbEF3iy57OadrDjZxTLQmfB33wHzKtQbFU6OLthxClEwzKNen-DW7_UU8Kog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
همانطور که دقایقی قبل در کانال دوم پرشیانا هم گفتیم؛ مدیربرنامه‌های ابوالفضل جلالی شب گذشته مذاکرات‌مثبتی رو با پیمان حدادی برای انتقال ابوالفضل جلالی به جمع سرخپوشان پایتخت انجام داده اما به عقدقرارداد منجر نشده است.
🔴
نکته‌مهم‌اینجاس؛ حدادی به‌ایجنت…</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/25150" target="_blank">📅 16:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25149">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8-IdXEqDqfydr9zLTrtVXJP6w4j8U6SDvUFGScO-FnUbQJ_k1QllGvlOx2eHVld9ww-pMAAIM7DReFngMh5fNKkZZQzTpRXUQrwFJFufE1GgYhq0Ofa4_O4Q5LA_9rYkHQKfDuRIAp4hLy0xgMBp6vOfx1dvxpNMSVmTQGg4Ku5ZAhf8Nnznh8ZYvlms0bKOKqQiLUBeHfQsoeazKsJtjSFxRYAAwOI-HVnr9tdRz9fuKHGjq4AalEarQhBo0rN_U8vNZn0ZDMbKpDslfmKi7txHWA2dzKpF-WKom15QvP-URpcik9MBlRz_H__QhVGmNhadHnrO3g6oijahUk_Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
امیرهوشنگ‌سعادتی ایجنت ابوالفضل جلالی با باشگاه پرسپولیس مذاکرات‌مثبتی داشته و احتمال اینکه ابوالفضل‌جلالی‌مدافع چپ 28 ساله استقلال با عقد قراردادی سه ساله به پرسپولیس بپیونده زیاده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/25149" target="_blank">📅 16:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25148">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djYsLswt4nM5g3Rorvg3vjroXa5XUE_310JbupsidKVwrWbD3Hr5nRSZOCuUMI3rKxakJdTtraSADSft57uyPbW1DNjWzS5NwdCvP0TkNN2l2E7cJmaRXuyzser7svK5hUGnvtW6yQHh1Xw6JuZTIcRQyLRN7QpI-F6b3_GwrMwQW7FTCs9ATzGhZm1bhBSgJGq5hWBEDJMbEvH1_UiBJ9rKfqjESpXo-ugY_bS64v_fRsvk7rB7v2x5QXXQSLP-1YbCGPbYBZQkZW-43GoGsK9Si-M5A4t5_pDRJH7CrzofbFYKA-fMzEQitnMWg9HAru47V-3ZdFeJhp-LRs0sgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
ستاره الجزایری فصل قبل تیم بانوان الاهلی عربستان که بهترین‌بازیکن این تیم شناخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/25148" target="_blank">📅 16:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25147">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7eJZIkrsDNBhzLFRcHiwxwmyGycsNPqKfKGUUo2XiNr0gYtCRP9Zl1R7LMWV87U1B9VSZEJWNGYz7BI84Hx-yg6j8d67GmQ1avWMJJykUnfZK_7a3neZVMHDyWsfZn9idjNOrDhJ-K6B8IXtk3sKLU3rHliZC10qBpiK_Q6QlI5q06UxtOKOrOzcmSosb5qKmcHPElOtMn9_kDnYrjr6CWGcHFuSwaGoIvSFUsXSE7REC68dGEYvmmajy0AVn7dkKiqVugmfGYxIdn-IlEQYvqqzgMxYZh7QDx6aLP5tzOHnuBaum6-Y-moIvOtnclTTAz7DuCcgx1oa0mna1aaLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/25147" target="_blank">📅 16:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25145">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLWWa1ZrGx1ZtBYn_Cc3zKTmdTt5dN0VE46u_eHkn9jxc--XrHvvwpsUSiSyQmMJ00D70rNGYyA_3J7VeGN5FLjhP8ug5hC6Ld-SEIxzsv9UlYD0QdegwCrfDbKbEeTBvKGhQHHQ4WNlEsKISAw1ngIrfm__V1JsVzaxSxLkfDZ_8yvdtWnlj3hXo4fWGgwE2cSuz3RLBf4eM4O1lmprioKouc3E0l-LpsAGdn--fxi14WhmndWEm0k4HE8ptF1p8Dgl8tZ2zgxdoHOhqcjQ91h1uimlVg4zBGAbRU40Up8UXbn8-bsCutJPOiazqRznuoWEakQ_mISQUT8pgrLquA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جعفر سلمانی مدافع‌سابق‌باشگاه استقلال با عقد قراردادی دو ساله به ارزش 300 هزار دلار به الطلبه عراق پیوست و شاگرد علیرضا منصوریان شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/25145" target="_blank">📅 15:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25144">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuONBInsU742iA8ghGUvcgmJnCPOkXJZ9p-Y0X2UvLw-SCXS3OMyhPG-RtpgeSftbi9DDUEdQcdhjFv3ob6svpV8EpZZgLZHrHkN1Xfa2yH2Zt1gSONJZWDeADJAaWIRm6mzWI3h_SGgSjr3JcTrVWcqW4iEZkeqj18G6F0uCn5W8-4RDWsZS4wNe5rK9kRFA4A-E96jcVynDkV0OKi9L24JM2-hac5McPKjhmiqevcZlNGYfDjRok6oodXGzoXeHM26WANh_0RDQBb5e9_eU826sjmZu5cfXDV6Y2DDUuqxBoKb2rWXZcW2kszf6nLpyA8OougLdG0mmxKjD9RJHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
#اختصاصی_پرشیانا #فوری؛ مدیریت‌ باشگاه‌ پرسپولیس روز گذشته با‌ارسال نامه‌ای رسمی به باشگاه الوحده خواستار جذب مبین دهقان هافبک دفاعی جوان و آینده دار این باشگاه اماراتی شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/25144" target="_blank">📅 15:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25143">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cImh8t_lHvrLUM9eZ6ofg9jbKCacP1-wsx60u9T2mOXh5GZvi7FR_omKAtQhz_ahuWPhyk6F7-AOfWGR6Z6AEdVOfgFB0rlubzMN6IZl0_WtrutyDwTfnvaHKZyZebV2Ep9RWIwvLAL0d2dxv7Qpk2U4iHyTeX75WXKtuDI4hctlPXm0GDQ5O8AOo4T2uuImCHy8zebKkpOUN35ChjyOKTcpUOmxCv5BYGMIxjOKkz7PB1ZCVeTf73UzEg8MpdCv6dglgBcKwSo7TguNAcYySdt0u_P2yF-IA_IxoWlNtuUHwbwAsFO3R5sVEnUEXR_2UeF0_XPWBxYQ0Jmbh-hmVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
پوریا شهرآبادی مهاجم جوان‌گلگهر که مدنظر باشگاه استقلال بود و حتی‌‌مذاکراتی با مدیران گلگهر برسر این‌انتقال انجام‌شد حالا مهدی تارتار با او تماس گرفته و ازش خواسته که قید حضور در استقلال رو بزنه و به پرسپولیس بیاد. شهر آبادی بزودی تصمیم نهایی خود را در این…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/25143" target="_blank">📅 15:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25142">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYgZx5nP34gq23xcuVNjLWhFcPV7cytFjPNVut6FeqanMZKDVbGWCH93LmOZDmhLazI0hsXXN1YYW0e5mhTo_58WlHcSN57NMkXIY31Aen2bYf5UZ5K6zS8VolB0WjJukwsj1iFGyLVKxNvVFU-vfj0GvDcz90fuHK983hucbzd4GiGggB1sDR_lrqAxSlR0iEto7siKw4OMTPF1j1dV-oEW3zlTXArAoafiF7VBpsi8bZo0QNBkSa5uiISXtrDUg49b-9EOc_x8uMwZxH6lTd9f-eJ1XxzSMMK0pi9fP1mPae0fuHvsZkCTySI1QKnDBTNeeA37jOGgqdKCpWlv3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی جدید پرسپولیس برای جانشینی دنیل گرا در پست‌دفاع راست مجید عیدی مدافع راست گلگهر رو در لیست خود قرار داده و از مدیریت باشگاه خواسته با او مذاکره و جذبش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/25142" target="_blank">📅 15:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25141">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtrSciN_tBtuYLFijUuQJg0Bmew-y237ZMsf_F6gF39U3ZhyE7Xax6ezNtfpUFOptY27glfhI5k5GEhuLyK7vcXIMc_pXf9WtK04M_xO9IpZGE0i3q28MtGDdc856mx5C9Bs0CYCn5o7lI65-NvfRPoQhQfNrbwgfo0DQXcurg5BmqSiLsQCYytCgQrPhutGBOgyE1HrHZ15e4pukk6JE4xOYOC2TROwnjYsC1nrm5u4kl2w3N6PZmgPopQ4q1d4z64K5VktpqGTlX4jvrS6m-CBbgcdZ7kc_aYWUpmIHacC-kL-y8W4dqvsb2wPse2QFHqjjWRWQTN6UmUE-iA-4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
قضاوت‌های‌علیرضافغانی در جام جهانی؛ دیدار شب گذشته تیم‌های‌ملی مکزیک و انگلیس در مرحله ⅛ نهایی رقابت‌های جام جهانی ۲۰۲۶، نهمین قضاوت علیرضا فغانی در تاریخ رقابت‌های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/25141" target="_blank">📅 15:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25139">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B70jGDGmCrj9tcGOaxwEUUZnNEczgx6TOLkwVCE4ktW3f7xIg0HDwiaeFDox2xYQZArs1qikunuf4KzgVRRH-pd52cTUrB8bz_SEkFd8OqvshBTRdpsh444liD0J0MYBq9qwZedYMj9JEp95tc1lHlwd3PryOIyTGwST6G3PNc8_pWNacSEbjMa_kwuZ93dUr2RjSo2Wh5cIvklIjj4G221eSw2eEpDDVDLhNdyGgHjPONEHgKEZGUje3LmlGqlvgZnyGI9S-Qd45rfSzH4VAsJPF0fzwasXkZwcICTUFmPxyZD2VB5Vi3gFGGv92qUoD-DaX76ixWXlmbcN0F6EDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MoZEebTd9UIODGQNbacR-_52Us3EV6RprmgGS4WqFrA9CYedkQFPyQOYR9GRbCKIbJ4GKEPjptkYP0UBAf4w1kcBS_QB5ZTyHwP_oRjMqBIgw2QrAIqLYOKA18F4xfuqILFmuzxXwifNwomftDDt-H1nka9O5lCiQcqlhsZdj9iF0lfZfqIPPXHzjp2o77Aa0S-TwsKwEvWmHcBh1t7avoefoKJgF0rR7LF8UqHbV0-5BcbQHE95Bp_OLgvxJanqB3bA3wJ2rOFDuWuYGQrjAyIAVMA_VP3iUmvDbtIcrO5bt_l5ghfDsREm8PObP6xnMwIGLRqcqkX3CQjKs7odDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
تمجید کاربران خارجی از علیرضا فغانی: او لیاقت سوت زدن فینال جام جهانی را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/25139" target="_blank">📅 15:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25138">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0HBGEcACQuiC9-bTIJ2Szb-RxNwGwWgntOSLXlz4Hdvl8WPFZHcuAqo8RJ3pbOMrc3hNKSB6NuCQ-IfiObFXovKFB_xHkRQXFBxv3KDsPdnfvF6xwVqZJb71UKK1hRPFCOfslukfSW3ZEVCqe4mlyDz1EIJ3W-p6jNC3L6Nhp-nBA7agSWsm6-4f3P8hzy4cV0BmWwNwNYGVUnJEJHnAZYgwO2o4_lQ1khH5tC7_ldcDVls8FMoY06kWCa_clbcYO8Eng4YlabdQvvh7NwPvxVjLzCCLZH1K1CYtFrihRl-djyvsFMZ16ELH-BMG51uTKYjlxq3kg1v_jTJlA3IXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#اختصاصی_پرشیانا؛ یه‌خبرمهمی که باید بهتون بگم اینه؛ تمام بازیکنان خارجی حاضر در لیگ برتر که حمید مریخ مدیربرنامه آن‌هاست قبل از عقد قرارداد باباشگاه‌های‌مدنظرتمام شرایط‌فعلی ایران رو براشون توضیخ داده و حتی‌اگه‌یه‌درصدهم جنگ بشه بازیکنانی که با حمید کار…</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/25138" target="_blank">📅 14:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25136">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCHOmSLI7R9YXJF1UykCOxsE26b3kwbhchXfWXtZdbc3BSTzb3FdSE9LQ7lnBfMNqZzwGSQe3qLhInZlno8ehKAKYUD8DZ2BPxmK2apx-ZxRXWWePJRBcfaTT8MYLTTXgfK4biB8EoelyawtgBTl_NzuMmuvANA4FMjO9W3nKdmBqQZPOL1D-vFINxXRtZFRQSl_N08OWF4XNr6j_xJerXCZsvDdcVo_GbTV5ay4-N3H4mLd8_F8Dm5hpw8I-wXkt9rz--gG-Rp7ax8dNxSaYX_DVNO0zidRrAnCJvsNvBsKVS-s4NuwPH6rHDkxvb_wSnny72588KvAGaauO59kOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c18c66aa.mp4?token=LCB0qXgXl6081pOyNswFRlaj9FgikTCiYnx_uv5rCjh6ajfguJsx4FCLZL2v51DI4r_rUpN6X3O8fjXw8Y1-ACrrDUYNlwVfYRLmleEJaaI75ji8QUhAGnl4-tQmA2wscouirsvVWfq5e59l14kByAIoXWkRs3h462BvgkWvev69GhBPKtjRvszUlxa4DDpi01Tu6jQHnCjhunhYWrumf0Z7X48_PYc52m-zurLzuR3_I-polBbbVYyBRJCmL8FDjeGHa80BhACC-I7rXp57hh_1rogjoizudsl3Qc_lbQNJ7gsIDepNZZdrh7bAPollIZW3ChZCXRf9IYU91wwVZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c18c66aa.mp4?token=LCB0qXgXl6081pOyNswFRlaj9FgikTCiYnx_uv5rCjh6ajfguJsx4FCLZL2v51DI4r_rUpN6X3O8fjXw8Y1-ACrrDUYNlwVfYRLmleEJaaI75ji8QUhAGnl4-tQmA2wscouirsvVWfq5e59l14kByAIoXWkRs3h462BvgkWvev69GhBPKtjRvszUlxa4DDpi01Tu6jQHnCjhunhYWrumf0Z7X48_PYc52m-zurLzuR3_I-polBbbVYyBRJCmL8FDjeGHa80BhACC-I7rXp57hh_1rogjoizudsl3Qc_lbQNJ7gsIDepNZZdrh7bAPollIZW3ChZCXRf9IYU91wwVZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/25136" target="_blank">📅 13:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25135">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cu7-SR0xjKA4MOPRBRhYLL99iS3D56ZdELu5P3MIOqqAKJAkB8CR-v0vcUaajiO7wbhNj6w8FLV3YRLpe2RUTH9rG_SDTEcE0WIyCm6e5909tn3AO1a73mhFbnZhXwZ7hNL3vktXboUD36Pz_Y8bJjsiWcAlhDSJagDPE3mmWlxqiuxoOnOpPSQuQnugM7pw0-t8IbbM-cR_QKWFLQS2lVvASOBewoMMhfgbBlWjmRecfkWxG961_Yr0sg8bnl4ry-ZbbmzwU0rscxplqMJSrJ8ypj6_Pi4OA6eXMHlZ_ftHW7NrhWKMio-yCGNevs3dr-2fzTHPckM1gDA5g7VWIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی؛حذف‌تلخ‌یاران کریس رونالدو از جام جهانی با قبول شکست مقابل لاروخا؛ اسپانیا به مصاف برنده بلژیک - آمریکا خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/25135" target="_blank">📅 13:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25134">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPe3SCJTSOVyHBqf0ZudSvBTk7Tt9_G-HhzTaZnHcYb0j8OdXnDkyFqtUhikElBIWY6R0j_hr77joI-yFbw7ZzE-jQBv8qvqwLbyvZjhrbXqRDyAFsLJx4xS2F2A5sLP-jTAUm2SWUmIRQCRVZng82269P2_gZARC0VQyL9vwbra4Zr9k5b8hMhKvRpgo5BtCh8O_Hrns2qb10BIHahJ1o5fQdYDP_qJvmN5d9yxGBx-gPNZJ-ug5pKzpUyqa60Qha7tDQGZZ9oxGj3RIYVsUL_bDqYLtzfbvzZcomFDNWU_s8V1t3z3vzkj6rwzHsCgb58U5Zd-vjoD4tmJYis7pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علی نعمتی به باشگاه پرسپولیس گفته که از لیگ‌های حوزه خلیج‌فارس رسمی دریافت کرده اما اگه مدیریت باشگاه پرسپولیس رقم مدنظر او رو پرداخت کنند به تیم پرسپولیس باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/25134" target="_blank">📅 13:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25133">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dyp8pAOm3Yx9woFQyVB_DhVMKmD7xfopgn25-GItP-TtNy-I2OfWBdIUSDGcLmVV1ivxLcpLSNONv1EzR9VQ5dspLI1BmfyNzYlhxoV2iAWAu7aZd3Jf7UBlEhKTOxR1ALFQrGzBw7SJfuU4UnO4ilp7Pm1k-2mL2MbDbMbGPej5l4-plhjI3sFcaG1NrlJlCE5FKMvtZDf4XAEiIY_SepDtI4iuk0YLxVxoyShC2meaeJJv_xv-kn4X6bbRKJk43Tw7usjQ-cXk8zF7OLmt1J0OhuioXvgv-JXv3ecZPBYx74r8_B6ciAb0Ti2H5nxU8WtrS-deeLILwRbmDkIUdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/25133" target="_blank">📅 12:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25132">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQMzUZYnN3nTH0h0v2KFTNRuJzqN0E0RvFf1q5QRgpd75LeQq1B-NTC6HsRPRaDPCh46WpZyb7FtFuWZ-GaVndRoIVl_CRUGOscgQ8VWeDCH2Nev2qbLgPPO-Farq5ZTJLzcIv-Df-JdC0gItYpS1GyPTXoCegeSHDAfRRn87AnGvvPywFrXAEkMi-MzHXdcLMYg8T5F7s12cTCvbl65oYOF3Gq5wl36dWaN43_C1zJSGlDPlR10OBESFfWX0AmrHErcnnIvyoLwWAtBBZfgH9KtLFpUdag4wCdmkB8EE6ySiMgG9y1gnasraLO6iO2TlWRJPHdcuQgZ_B_cHfsO7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیر الحدادی ستاره آبی‌ها: آماده بازگشت به میادینم. بزودی در تمرینات استقلال شرکت میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/25132" target="_blank">📅 12:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25131">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4AC56xwCT8bto4K8rQ4-xpgqXQF5SAjR5f-tXxZa5QTlPWHBxEN6RKxlzbcYC2Aywf3azmdsZz8Cy_AcW2m-Wvk5xxR8yDYWAWb1bTTk_dPFiHOjaBBpebR40mqt9gX2D9hX58vHHQOZRWEUUnfNb6qUwu3EhvfiBCY_PVKo8zZKbF439LMTgfjLo6G9KDdLB25Z3-inNfDYuxHrfZBQ_SsuaCcXpI_Nr_HBEcKhk50R4ttBd0SrDgcIZj687Nq5J41zd0ftZdJvy7vLghBPhBbl6aCdfy3kngkgjmqpaisPb_3BH7WT4VuNuK9rX5BQDmCqiEKsmrVjT3Ubbimhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
مقایسه تعداد جام‌ های گرفته شده تیم ملی پرتغال قبل‌وبعداز حضور کریس رونالدو در این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/25131" target="_blank">📅 11:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25130">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPOomZfO3hp60JvTGbEiNwFg0A8yTFKZS6NOrcvFyDcOT7hX1T9sgmp4Eqxzld9pVf_UxISqXBbZ-I8Tf4rtfjlOcasnDdTFMl3-Kf1Ja8d7odhTWWOt_F2KSoRJGk2fMSrwjgm1IWPTnb87DInUOqfniznOhOaYisgxHrHqkWChEJgxNi6OXcxPUhf9vqKhAF6EVzimxHj-uDcB_fDG3QAJvJa4whk5PTsyS3d93f_Nq79FxchHZA0nbBD_2zCUqCwEop1IQCslDpb52WeXdUpYNi1oKDrgKhcXEgjY-5D1mc6fB3up2XLKFc4UqVAnHHZtgmmjR5GjjZQtqRYgHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره آبی‌ها به کادرفنی تیم استقلال خبر داده بعد از بازگشت به تهران 72 ساعت استراحت خواهد کرد و سپس به تمرینات استقلال برای فصل جدید مسابقات اضافه‌میشود. این درحالیه به تموم‌ بازیکنان ملی پوش 14 روز استراحت…</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/25130" target="_blank">📅 11:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25129">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARs44koGttuSo44ondrOl7uLtP2c59EceIqshGFHDT6pcmdwc1rzV860ObR9r31GCz4bN0X5rib9CydEk9IGOEmeJnk-TuTQYR77lhwEJ7HQlrUJFk9jmVRIe2lZJz9PwiaIq0rkXXabr-qtyCge_rU7IWiAdsUo-ztzYnA9ky29t4Uv9AkjT1EcUgXgyN7kegCVLK4Q6u41RGIFgIosvKElgJ8s9_wZuehbfr21eEVZ2Xu0H7_V1KqvOdBzHhBTgOxge9on5a79xfoa4sS9UNeRdQh15Owxv4BS4GtK2OPyl900177cgnBSpBCAgdyWg02kXheHqLdUr4p5U8bLjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ باشگاه گل‌گهر با محمدرضا اخباری گلرسابق خود وارد مذاکره شده تادرصورت توافق بار دیگر قرارداد ۲ ساله با او امضا شود. برین ترتیب حسینی در سپاهان موندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/25129" target="_blank">📅 11:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25128">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGXWe6JrvDIKfZXJoD1VGDn2zs-CZplTv5pPiSk-fZTeEs0BIUaLqtWskMUjAs0h96YSk_uhBqK3a0-lgfP5IbNfya4jM8Igl8YPnKm83QbkjVmhSOssLKPSBVmACBQGVsgxB9u5Geunnxva_cmJnTac0TZWSv9yJsYT7RVj2Ytt0gU-jHEKQT9O6xUOPRB-0eyQzDB5Ah6o68EcqmL5BW2OTPq_40g_zquwAI70A1CHngx1G6Nqo0ssoCTudmn3JIl3WXBiQSdESTFrXC70SlfF42jcG6HxXSxYDtRJ5teXebvAacNr9IFv8YxM4fjAkBlLyeOnrzCPTiQF4fnLcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌ایجنت محمدقربانی قرارداد این ستاره 23 ساله به‌مدت‌یک‌فصل‌دیگر با الوحده امارات تمدید شد و این‌بازیکن‌تابستون‌سال بعد بازیکن آزاد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/25128" target="_blank">📅 11:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25127">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6dc32dceb.mp4?token=J9XRNlv8Pjdkl5vs95e-OPiD4RsxBzI_n2svhMKlNNVOqPimP-KaLuJARadDm6HWlfxlZfjXDh91eLjvtEX1NUaqiwDW5Q1iYPRlW8Kd1B594SNUBamWvZw2niu5Be3PE2aGXYd5jLIfhnGeXLcQSxLA1Qf8FK3qf6X-VoSNQLo0MarSKALle1vvRANRq0a3PIaMHWS4tcCThHnGVsVVyamcdkeM9iaViQjwZSbmHQY9EZX-_vDAKZxUMy0_C_UHuvw_VygbOTCIdArogJyKOOgkJuBkOHWbQUGktMchftAMbTLoDnaY9sduaEadpqwCJn0afdA3WeGdWpwQdkdxDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6dc32dceb.mp4?token=J9XRNlv8Pjdkl5vs95e-OPiD4RsxBzI_n2svhMKlNNVOqPimP-KaLuJARadDm6HWlfxlZfjXDh91eLjvtEX1NUaqiwDW5Q1iYPRlW8Kd1B594SNUBamWvZw2niu5Be3PE2aGXYd5jLIfhnGeXLcQSxLA1Qf8FK3qf6X-VoSNQLo0MarSKALle1vvRANRq0a3PIaMHWS4tcCThHnGVsVVyamcdkeM9iaViQjwZSbmHQY9EZX-_vDAKZxUMy0_C_UHuvw_VygbOTCIdArogJyKOOgkJuBkOHWbQUGktMchftAMbTLoDnaY9sduaEadpqwCJn0afdA3WeGdWpwQdkdxDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
از داوری در زمین‌های خاکی هاشم‌آباد تا رویای قضاوت در فینال جام‌جهانی با علیرضا فعانی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/25127" target="_blank">📅 10:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25126">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3cbyrBTebXDYoTpMLNmTKCIubaUcIyZnTyQpPWmLEsFHfZO5qW2ss8hBQ1GFBZZS5dlJGpS-EXYD6idsfxGvEQ94TjpfWyl4Z0ld4RKmfV3mxRRVqaaKdFu77SWUOreEX6Rk9FZygGnCLc0IJy5WEPQNX4M11oZHehZ3q5VgJ3Mv3CQ2edC6RswJFOqhEX8LJDbXdfcQb4tOrfhf_sNxrlKy-TpNCrf1KVWm2MMg5HPQYZD0ER-WUYGW4X-nguZSYTNLva5mDhAV64wA0lX8jeiNyq5qORTdgR5-HME4vtgFw1-p2VO9WKFeiJ9p-PwS_vnAWHu2jIwA7XTtI2PAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلاتی‌از دیداربامداد امروز بلژیک
🆚
آمریکا در مرحله یک‌هشتم‌نهایی رقابت‌های جام جهانی 2026؛ حالا هر سه تیم میزبان تورنمنت از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25126" target="_blank">📅 10:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25125">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58bc836c41.mp4?token=CfyNX_BOX43oHRMZeFtAtPqt9W63APcXbDxVvxeC4qGg62N9g19N7vNaat-TlNv5qAB-_KNjmAyWeHdpqSGs2PoKayfpiQmk05vEzli_GxlA7kzapqJWlaJAIlSfl_Ytgg8diqhEaHsgmT0qTRfUp8uiK3KdU0y6l5I9Ko7VrBVFSG4bT7IUYugQ6bsDHh8_32CrILbDKdGOMblng0z_CZJptinLfznNTvLWURO-RthUAQbsTKDxCLy4VDlGXNLoztiRWRWXFeUrAaE71_XJSbllPKGpbFegcJqMfg6qKpXCMePDsWY2CqMIFJmQ_s8TOdG7DJHofltSCxDC9TAWyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58bc836c41.mp4?token=CfyNX_BOX43oHRMZeFtAtPqt9W63APcXbDxVvxeC4qGg62N9g19N7vNaat-TlNv5qAB-_KNjmAyWeHdpqSGs2PoKayfpiQmk05vEzli_GxlA7kzapqJWlaJAIlSfl_Ytgg8diqhEaHsgmT0qTRfUp8uiK3KdU0y6l5I9Ko7VrBVFSG4bT7IUYugQ6bsDHh8_32CrILbDKdGOMblng0z_CZJptinLfznNTvLWURO-RthUAQbsTKDxCLy4VDlGXNLoztiRWRWXFeUrAaE71_XJSbllPKGpbFegcJqMfg6qKpXCMePDsWY2CqMIFJmQ_s8TOdG7DJHofltSCxDC9TAWyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نمودارکامل‌مرحله حذفی جام جهانی 2026 بعد از صعود اسپانیا و بلژیک به جمع هشت تیم برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/25125" target="_blank">📅 10:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25124">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b3a80979e.mp4?token=QTtzg9AyXQK3CFLAyKDIWztE3im6V2N0MmANZOtbCe2adBTWkumaLCB7VLtl8fARcZY--tVHwZzTu4NTg6PdITL9dim4nOJugyeTGWEkY6bC8ipp1N_iBcMNIndtFPCPJyi0np_V6MOgPdDbNmPFKw0fsDibhAqnPvJ9hXXQhvqPbxUwP8UHj59tuLlUT7j-WYN5GywteuiuEqPLxE_ymuhbF9O3AZvtQAYoLbP1r96QdgmDY2o6ZskVzPbjS9LVVAdMueXi__J57sQpy_gv9wsaLB4Qpu40fKDDGaZeR_c_G7rHnrrfGpwiW1SDFu7TtcVknl_bvpW47j5_8oABUjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b3a80979e.mp4?token=QTtzg9AyXQK3CFLAyKDIWztE3im6V2N0MmANZOtbCe2adBTWkumaLCB7VLtl8fARcZY--tVHwZzTu4NTg6PdITL9dim4nOJugyeTGWEkY6bC8ipp1N_iBcMNIndtFPCPJyi0np_V6MOgPdDbNmPFKw0fsDibhAqnPvJ9hXXQhvqPbxUwP8UHj59tuLlUT7j-WYN5GywteuiuEqPLxE_ymuhbF9O3AZvtQAYoLbP1r96QdgmDY2o6ZskVzPbjS9LVVAdMueXi__J57sQpy_gv9wsaLB4Qpu40fKDDGaZeR_c_G7rHnrrfGpwiW1SDFu7TtcVknl_bvpW47j5_8oABUjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های‌تامل‌برانگیز امیر مهدی ژوله در ویژه برنامه دو سال گذشته عادل خان برای یورو 2024
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/25124" target="_blank">📅 09:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25123">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2fe49d1dd.mp4?token=PGrmGWOF1kydO0Cexvbu5BmvNrY_S51qzDVdEks__7P8B6khdISfn7Tv6Y1325ocTk2ajqnSvVyEaczlPz97i1_eUAfwR2KhlI3-YUyNXrv9rawbrWhEJfvSnhBKRNNA0CvODFrRetufS03ut9dc9b73-VwtaOem88W4U0rMUnadWa0nePnAbdXyeko6UHDzGjl-ibXKRtH03bjia4tEOt_GizNuLXbudtG16fSxM3tWA1y2CrxG61MwU0SqIFF0_FnS9BgvHLWfvlFzZ4qFuwia7Kc4yRk-4JPJEDgxfwOeoEWxP5obf4YhzOhCSrdDuwAHpurCBDk1rbXANxijIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2fe49d1dd.mp4?token=PGrmGWOF1kydO0Cexvbu5BmvNrY_S51qzDVdEks__7P8B6khdISfn7Tv6Y1325ocTk2ajqnSvVyEaczlPz97i1_eUAfwR2KhlI3-YUyNXrv9rawbrWhEJfvSnhBKRNNA0CvODFrRetufS03ut9dc9b73-VwtaOem88W4U0rMUnadWa0nePnAbdXyeko6UHDzGjl-ibXKRtH03bjia4tEOt_GizNuLXbudtG16fSxM3tWA1y2CrxG61MwU0SqIFF0_FnS9BgvHLWfvlFzZ4qFuwia7Kc4yRk-4JPJEDgxfwOeoEWxP5obf4YhzOhCSrdDuwAHpurCBDk1rbXANxijIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
داداش دوست دخترم فوتبالی و عاشق فوتبال تماشا کردنه؛ حالا دوست دخترش حین فوتبال:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/25123" target="_blank">📅 09:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25122">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIGy4JCubmhD9qicrQtFCvzIaXlpN6CobKJU8wG4_ddztqiDmPo_Oil9VbK-xrXf393de723qb9z38nE2y91-9TPvq9VW-CL5VfX3EYYC9t9Y1Oxi0zuxQyr-EaGP0LAkkY0yXvZYlArf48QRzmrUv71aEtKhJeZosyA0LcClSOwuoLiv4klcf00Mdsz7bZ1m8LbycCAY9yHcQJbcrn-XotR--24vddHETesKoG7P2pKzm6UBnBuJ6Auayl4FrEB41uJ-IUzHTq6MycuYBY4lHTRu6qMSxFGBqbyJPcYOZczLNAMw9SMTAtd5jgQpLvD5rHRovIgkAidAJ8ZuJuDzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/25122" target="_blank">📅 09:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25121">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdQYUkwTvhCJTjbYba1DzWRYexNPsppfFgyvLKHoV8kILYdaCsFmOVxNw6AiEH6rRKfsOPH8HmsR0v_D6vzW6fylf5b7VNCER8VyxaPf4G7kOWz0YWWgiPo9XQO_l8ujEnobnj7m4KfVWL199ncNj1EZs4qZ1Rp0jRwlbC6Rw4k9QjCTjM3pcrZX2ph7FnSXm6IzoT0JDjY1zKHkQzzJjpVp7QNSfdVmbpKcs4lAdewRlaRoxIOve-e8vH5bvoPgGGQqC9EFBx2S44BaeoiZaw9MmH0I6aaqT6uJVYNw8zQnx1DHEwKvhK0dAcIDi7pQKMIY8FKPBlSNj8YdCjV31g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی جدید پرسپولیس برای جانشینی دنیل گرا در پست‌دفاع راست مجید عیدی مدافع راست گلگهر رو در لیست خود قرار داده و از مدیریت باشگاه خواسته با او مذاکره و جذبش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/25121" target="_blank">📅 08:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25120">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psHrTiXJr1kvjGvEPpIR7jCPE8qjlaj1NaI_JHEVCg7fd-9D7TEBe2PZW8hZFAtrl4wKfS0_jB_6ytaVdfhZ0tnckkzlQ0Tr_fvJvTJeqpOnzZW_5wdoqcM5YJfAVh2qkfAX3eUqxUih4_Cs5gBKXhtxrP94iLZE_s1huqGjFJGti6TGfO9F2BdL-A22PD43KnZUhwL2tRs3KvUP70gQqXO5mN0XcpAERDyn-0tiBLjMuDW1TnGYeVDpZdTkPE6ZkVAXQadaVRMGMzafXPB2ZENSxyOFppw0vPK61dPal7JCS_ZQrw8QpcxLoKp2PNvg5-tyjVteXSRBFlPRmSyuWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25120" target="_blank">📅 07:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25119">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pch2NwWSpSFZaC1UJAFRB2ShCPsSqlIvvgaYW3r6zTGkMP0hQZgChKlFTmXsr_mWIBtYcEMh_jYJJ5vXKuTANyt76BEtVbAFUR-yk4UIk55_E4wu-W-C0X9TkWDwXkYMkbQf_Fw0Ht06HidKKj7Hs6axAFJSpZxBJwg5nk4hLV-JXdJBi1gxsQqz6hRRigGjcKeks2egibUX6p_hrFmrpvlfL8PCwpbsG5iwVXPS7p_jjg3N_PBJSikpM1Y7fT9PlOGbsjjFxRL1wfOSvIJTUFPE_wntHgIjRDqmyr4hcvv5f0yp8ikb2FYBfQCQBqVvp_SO_DCqpAtAOyad9fXnQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
دو ویدیو از کریس رونالدو و صحبت هاش در پایان‌بازی امشب: در این سال‌ها تموم تلاشم برای موفقیت تیم ملی کشورم به‌کار بردم و سه قهرمانی به ارمغان آوردم‌. وجدانم دیگه راحته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25119" target="_blank">📅 03:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25117">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e026475ce9.mp4?token=ZwCx0q4GtA8kqSzfXULj5SoJHK93d-Qv87EJAn1WgxqdF9CgtLX-lfAqkSe_BfJ67DNmbTthDqrDe_2OtQDGqLfNL1b-MybEF2NiaKt02PkTj6B_9MzVI5LLNo2lcEyS9Blw3VNBi58T6pZ-le1vo-a62bAOzZyTucwGQmAm1FJNW3sMr4xnyNu1EerLHOiyKxrsJSK6UScl_y9kKNZ4e86AsHQ8XjGrrxtyuVul4x-TUvEPCXbsA9UF8Wz5-NewfUTjqELpL_6zD1-Q7gFlpLlwmGqaX1eVZ_zJvg0rWDS9k0sj3Km8z_3W3XqrNPwVB1uVRp_ZlvvMBcbLm3VoTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e026475ce9.mp4?token=ZwCx0q4GtA8kqSzfXULj5SoJHK93d-Qv87EJAn1WgxqdF9CgtLX-lfAqkSe_BfJ67DNmbTthDqrDe_2OtQDGqLfNL1b-MybEF2NiaKt02PkTj6B_9MzVI5LLNo2lcEyS9Blw3VNBi58T6pZ-le1vo-a62bAOzZyTucwGQmAm1FJNW3sMr4xnyNu1EerLHOiyKxrsJSK6UScl_y9kKNZ4e86AsHQ8XjGrrxtyuVul4x-TUvEPCXbsA9UF8Wz5-NewfUTjqELpL_6zD1-Q7gFlpLlwmGqaX1eVZ_zJvg0rWDS9k0sj3Km8z_3W3XqrNPwVB1uVRp_ZlvvMBcbLm3VoTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: من تموم تلاشم رو کردم اما خب نشد که بشه... زندگی ادامه داره. من یه قهرمانی تاریخی دریورو 2016 دارم که ارزشش برابری میکنه باقهرمانی درجام‌جهانی. این آخرین جام جهانیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25117" target="_blank">📅 02:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25116">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwDMhLQ6Ftu1Sj4wguUkz7eVwaR7GqTFkj2E38VbFK3AaKO9E0omFO-4qN8fHMPmCISBcRJ-6L3vr-qe6bTH-4x_c9kaepD203Ogqv0BFLChRS-s5vPxXAMc39MYQYov7KC6dEnAgL1rT8vSl8g9o7hdFxmkALGIQau2bPh-Sl8-hACpcGLLAf-y3e1diWhkcJgaQ2uERCVyfB7My4oyeJ3RQIdBniV0PIyiSBO1CTYk_bkzzZ7A_6xh7K6iohKOCbAgKXIO4ze05Jkn25WyEwtUU6LHVg34qtkH1Jx0MiRVwuOycAxTjB6LGOgpzODdQ1au7Sl5ECKZyKjxtG-NoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25116" target="_blank">📅 02:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25115">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FipDmaM6u6YWUoNM80-Oxbh8ahfu0yp5xk4yk9VuIq4kqebCXiSPH8DCA5mF78hodPkHmWhoGoylDwQryKOJZpXz7p9PBQCIFeEmEfuO3wI2v0dlYOCn9oV5c97j2vQSf051wzTTJih8-WFqd8a1-ogAVQwdaO6YOQGM4PtHoJvsno_auznJzNqjY7RJReUeEBJo-uO557sWgKhQ3XUm8lhNJeV43tz-H6Tbh0FdhZrf21ImQQvEmj0poT0g-InilSbTiY2CVBKmodFD-X4t9834s1CdC1PrkGhMc1GhwPjcAyLoLTU2YJykLyMDBChmXlZhqOW2f70NqJSRYXQa9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال ستاره تیم‌ملی‌اسپانیا درپایان مسابقه به این شکل رفت کریس رونالدو رو در آغوش گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25115" target="_blank">📅 01:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25113">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8xYnSGs9_JQ2cHp0OgJrsNM-rs0v_3BR3fQRw1AvikizW_ndeHxBWANXHqjqi80YN3DV1yCxvS3BCv4UQ710z8JjOPqOdtQ62qAi_GwvY5QWZHi9efF7i5drdgY8D77fqdnkgEXePx3mfUfFLnHKPLRsvmYzfh5Vc3LhIMrm8cS0RYgkAC0V3HiN76o8RYPzsz1LEwx1jua0btGsWboJ83UvmUyAsWhLio4lRgzmRW4z3nZ4uMXwOAFQhwMVInMbzB6cgeQfTiiCjky16L-xqIAGH01MTkxTd2xS6PzdM32ka7I8rcewhi-hHL8zPIh9TEfUxC2o3KBt4LadH5M8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوتبال درعین‌ زیبایی، می‌تونه همینقدر بی رحم باشه... در آوردن اشک دو فوق ستاره محبوب فوتبال جهان درکمتراز 24 ساعت؛ روبرتو مارتینز هم بعد از عملکرد افتضاحش ازسرمربیگری پرتعال استعفا داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/25113" target="_blank">📅 01:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25112">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTUsHfCl9mE9Un9PuLxtpT0wLgTnW8-h8KB2bjI5ZglaYSXlI402nWs2BxxO5sdwvLyod5IZSG9tlbEPjuFALBTh7grtXDfOcyyHqcDYx-fnq_hOJD-PzVPUsBzqS2T45Z8dIwJbV_0vJg6mNjiOZtIuBtnp1K5yv1bQzQnD6xVgjuxaNP4q4Z0YHhOdVDnRlmUGBPhZSqSCgWLKnfPDzgCD8TYon1lKyxR6KWJkm97TpVk8MdFd1wIS7-CZJtZVMusB9bUDbqag33eJpgp_1_b-LGMzMl_0fEUk6CLrmddQ1Uy9wMoH6GvDKCcFWtM-R71kKtomuy1rZS5Z_PB4mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/25112" target="_blank">📅 01:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25111">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHBPps8pKJNZK8KqDO2VN1jcjMcjvpe1snChFj4pBB8xRoDgFPnrcEIDjFuiMZq45PXMZ5Z8AC9zVTMAgpXVkmOK9DLnZX0A3cEpkAeCqj2XfgrAssdsaTafSYwKaRY9JzTRCGsex1GT0PXUwGOYiH5jnCZrEUhZkES-tEacA3I7p_r4wvFafDP3MdRZzQMuXmcNlQouGxJv-N9Gi_1L9okYDHKNjn0dIE0fk3eG6303AJ6j6Pic1IzQdOKaPIQG8jIv-lLEFzfODx5dGmbRM4ycjnfFUVvbTfTlwpqOXi1fB-ReWaKlYgyFrn3jt3rK69htqu9yXRfFQHXBUB6Tbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
ازجدال‌شاگردان پوچتینو برابر بلژیک تادوئل‌تماشایی یاران لئو مسی
🆚
صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/25111" target="_blank">📅 01:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25110">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVTZNj_72RZeDlzogymZ9o_xHcKLn712NoNPB4GipFQZVS7XKZwooR6boaPVN0fF5hIcUCJY9HR7KA1TgFwzLEGmhGvJqCL-PXiEtNVTjfOCwPo8wdJuhbhdhvWESEzgjcc4nb3RUmNBn2mnn_Mrq8y4YQJk8HfrQnwFyUUAfKzz4kBnGv0nCiWnXA69FiHpyHdPJAx9RCcYY71iAUcgrbeJqainLAsPMiVRnYI6uuEdBQt3X4YN-qQGh92wKW1BaklGjwGmsIVWcFR-f5eEB0V4ararf2E_XBue3yT2dk8_w_ILhXCYNTKl3wuDCFeSZLsQ0sZpyrbZhfnDhvFpvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
صعوددشوارماتادورها با گل دیرهنگام مرینو و برتری انگلیس با درخشش بلینگهام
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25110" target="_blank">📅 01:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25109">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ec0bc9761.mp4?token=R4yN_BqoG_tkPpVujuNJ8kOKV6sdYT44VRgEOfJbCUS59hhQh9U61r8BryppURbzYWbsIF_DOuYoDWPKXtb6zK48iPf79L9-h59N8ev118VPQZdflDM3-Q-SwwmIeYrbhJY5y-4KTjljS584Hk5YnLRIPCIhf-uYQBiuOXRzWycd2PX2jckqpUE2_yc_HLLaWPFDH9Bq4DpC1fmc-LWyeO-SJddl7kgbQtcYe9C3xUM96IW27xH2xtQpwjC6k4mdDZ7lr7aYRckJ06XYr1B-lzJz5wIR_vYRyfR2eAAqpUWXMlVxPicGEbudju3iBX4xsVjfpdzTXCSwQc7EHSjROikv3ss7wV_YNWMQaDWKvnjqCDvCH2VQmBgB2EOoUvJU6rbW_Z8uQ08PJCd9AmXXk3I7gMcW-3PilxCcKjxTYBuekQr5yyc1ra1eZzzKPpdqRqZzluQBNe92LE9seiVWKJFsZNm3-L-tEtpzAT6CVO9ryimOjmKu2JD-jHfBwMQc7mJDUqzD9-DfWpPkIpE8tk4mU8RC758LMguCN_KfeDU7S99PVrnADjwvG83OhqZLxz6_kLSgEl--VS1VP79tbt7qvQH3DOZ7eq2_COdeXujdng8PJkUcQh6haf3Rk2NDxwjXKnnQCDAP-t6ZyHUT6Di5wzuMAYRNEKf-SVke7uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ec0bc9761.mp4?token=R4yN_BqoG_tkPpVujuNJ8kOKV6sdYT44VRgEOfJbCUS59hhQh9U61r8BryppURbzYWbsIF_DOuYoDWPKXtb6zK48iPf79L9-h59N8ev118VPQZdflDM3-Q-SwwmIeYrbhJY5y-4KTjljS584Hk5YnLRIPCIhf-uYQBiuOXRzWycd2PX2jckqpUE2_yc_HLLaWPFDH9Bq4DpC1fmc-LWyeO-SJddl7kgbQtcYe9C3xUM96IW27xH2xtQpwjC6k4mdDZ7lr7aYRckJ06XYr1B-lzJz5wIR_vYRyfR2eAAqpUWXMlVxPicGEbudju3iBX4xsVjfpdzTXCSwQc7EHSjROikv3ss7wV_YNWMQaDWKvnjqCDvCH2VQmBgB2EOoUvJU6rbW_Z8uQ08PJCd9AmXXk3I7gMcW-3PilxCcKjxTYBuekQr5yyc1ra1eZzzKPpdqRqZzluQBNe92LE9seiVWKJFsZNm3-L-tEtpzAT6CVO9ryimOjmKu2JD-jHfBwMQc7mJDUqzD9-DfWpPkIpE8tk4mU8RC758LMguCN_KfeDU7S99PVrnADjwvG83OhqZLxz6_kLSgEl--VS1VP79tbt7qvQH3DOZ7eq2_COdeXujdng8PJkUcQh6haf3Rk2NDxwjXKnnQCDAP-t6ZyHUT6Di5wzuMAYRNEKf-SVke7uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25109" target="_blank">📅 00:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25108">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a9ae9f6e2.mp4?token=bCQNKopoI_pX8pgw1WKlbUb9QL_hydHciL-hkZViLbne7O_w0Ija1UjmmhnnTg62l1ReonrXhivb_1DVV6it6WIPQtRhczC91m1z0cSQ-DhBRAOZesZCjxW6BMaD2kRK8lM-Suft14qX5Mg8ZEiz30eG4b2ieaash7XS2Kz9YIHZ61jdAbey00sgRJDJuGM1X5g9S6VBCTJ6LbUStrTPhx0zlWX-elfKtKohB5rH1m7fRgff5sc8BRRzsyJJuYp20EP5GAm6kMYfh08j86MyxE9La-1oAOMLaqKkAusyPL6GApjvzntAUIinH_xJtmWX8U8uqwgDRjzVbbRX9C7Cloi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a9ae9f6e2.mp4?token=bCQNKopoI_pX8pgw1WKlbUb9QL_hydHciL-hkZViLbne7O_w0Ija1UjmmhnnTg62l1ReonrXhivb_1DVV6it6WIPQtRhczC91m1z0cSQ-DhBRAOZesZCjxW6BMaD2kRK8lM-Suft14qX5Mg8ZEiz30eG4b2ieaash7XS2Kz9YIHZ61jdAbey00sgRJDJuGM1X5g9S6VBCTJ6LbUStrTPhx0zlWX-elfKtKohB5rH1m7fRgff5sc8BRRzsyJJuYp20EP5GAm6kMYfh08j86MyxE9La-1oAOMLaqKkAusyPL6GApjvzntAUIinH_xJtmWX8U8uqwgDRjzVbbRX9C7Cloi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
مرسی کریس‌رونالدو بابت‌تمام‌لحظه‌هایی که برای ما فوتبال دوستان‌ساختی تو مرد تموم نشدنی فوتبال هستی دهه‌هفتاد-هشتاد باتو خاطرات‌زیادی دارن
💔
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25108" target="_blank">📅 00:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25107">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYMOta1iImltFxpUkPI6KQxmhIM1jI_GlsQS245EHfY25bUIoNPrkdt5OuiIV9kHZKzjEOKop4XFI6pN6T1BMnzRjzUlQ7RB1Wt8wVNuqH4vtnt6krRAkgYEvQunma_HrP3X4AgbkrlsXOK6aATOriIBPJtNE-qefhCW8gIKm-hJ1UAgUK3YQJhCNzmiTfxKyOF7U5293hOoBRzrzkWhv75QsseK7IWUUXdsRA8uwo3ec_JwdJq1TO4X_CEz92LCAKFjKuXlfUbXJJ3ttW7WsMJsdAbtjh63p5P9K9GaUqIN440b4R7jJQ_2NeteCqZCo5xb7q-_hSpMlYd6zp6ZjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
اشک‌های‌تلخ و دردناک کریس‌رونالدو اسطوره تاریخ فوتبال جهان پس از باخت مفت مقابل اسپانیا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25107" target="_blank">📅 00:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25105">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXZnegAkfLtB8fZxYmsJLoJmu6XYdnHfo2ynGWb7DAZWh6wEXXOTzXB12y-WQj6WW0pU8zXokaF31OO5UcKHbRj6pkz44ucsC8e_13M1gdhy67CCUg53lUhfJHD6h4RTNjiM-KayI5Aes66nbYmQXaVoE9wu_itm6V5mRza5GnhBL9l5hKd8udYg8Iv12fOsKnSKtGsRwGzk1zSgeCSXLPZEF7bBLJQ0KQiVtxnnU0xIqWJaIE_wKhH8K0D4hmX7XQltILVBTT_23BHsHV8cTWSiLAeDWjdBENEh7mxjjlcLbF9fn492jH1d1jVq13Gl26lLDVojuo__tHGeDd7-Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
پایان رویای تاریخی قهرمانی در جام جهانی برای کریستیانو رونالدو 41 ساله؛ نشد که بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25105" target="_blank">📅 00:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25104">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Siz_OC0RpS4IdD2r806_BbA9Nyp_MV-QPgbjhFBDr-iAlpsKKYSPFTYGl90Q6ThknFImhXfpywu-DJQeTcU-3lraKyPXLGH2jGA7f-ipSrvyGUHy26tkeToPVXROMGYz-WdSl23wBP9-XVtNKEQt0WxW7Zdp3ZR0tP5sdz8nefO8Af-gPOSTqwl-YZA617vzNVhfkMegENwGwo-9SHNjWXg3Yssg51RCt99D8kTY2IG7sV0hGoPTi0lTJmvBuFGAb2qV1_yfsVWuf3CG6TvNCSU2gwPFLngeyQzufsmjjFblnaNsv5y6tRVLXJZhstdQl-YxJOCJfSWFwJQsnyMTtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی؛حذف‌تلخ‌یاران کریس رونالدو از جام جهانی با قبول شکست مقابل لاروخا؛ اسپانیا به مصاف برنده بلژیک - آمریکا خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25104" target="_blank">📅 00:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25103">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DC4lvj5qosf4BjW9ae5yhuY3KPZv9rfZm2g_OJp9oqfP1BeW2APwalbfHGagUtjnBUSbvYE5cw24AHDMJIpXn6iE5M_eGXnijdNU9TcLNGF22xGtz6lLYW6crXPZmiy-g2ExRt28sKiFH5r-r_QfI2sUmfH_okDQjHvtiN-ehY--McZbvbfbT-01N1Znmgy0oM_bh_NoTny9Gy357-cA6W6oj8EUwOBZFYIQ5N9S7a3-RB5NK5oxssoQatwBQVchphK1pJa-OboJdmzPEbRw24iHqLjVKogv8efqJilb6rgMmIdk8Kb6VCTh8L3TcAJt_OM6Gr-UgK7MM-lPD8q1yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇪🇸
آخرین تقابل دوتیم ملی اسپانیا
🆚
پرتغال با شاهکارکریس‌رونالدو اسطوره پرتغالی فوتبال جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25103" target="_blank">📅 00:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25102">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZse2xw3-MVPOfokAByKbZv-leJeyQf2MccEwgCSTXRd1x9hILCipddEmLL3-mZNVLrr7b3THvexWQNKpYV1AQfB993_AhtXaJ_bQxYhUa8XhOnLeB89yML9K_--wPgk4KuaTnhXN15DsyfkUH5lmQc9nbNtpmNksb7s9IRELE-UesX1yssnQy4y_t_HDOQAGpw0Twdig8bcvhvHGaiKIouy1AmPCFetyVFgH4lyQCtZlPLN3Vrj2ojghSL151lq3OU7eoKP1OPCc4ZAJJ3MKpDUgJRS69pwz6bRHkb1TPAASHcShc4LM1-sFaTaI3ETp3ixnAyVAKjlAORjg2MHDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
#تکمیلی؛ به احتمال‌بسیارزیاد مدیریت بانک شهر با رقم 65تا باعلی‌نعمتی و نماینده‌اش به توافق خواهد رسید. مهدی تارتار بجای امین حزباوی که در لیست اوسمار بود خواستار جذب نعمتی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25102" target="_blank">📅 00:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25101">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOJdA9F8w-gUhXC4COF1S8qIshgWI3ckBUFKJMZ-wQmWSBfaliyvcwwYdKmFOu_LAxNw37mMTO9E99k4RvHVYdtk4-67RZPJ8m0w6NUK7RWkPVXhAEWWDamwqt0UFBtDRHOMs6NOhivdrkRQ7-ZostCvKVtk9SDAv159dLzu3JcXwdWh1Cu6vTzVT3VE_QY9cXxJpxXe-qJP51VY-oW3SBYH0tlwzhhDXaDpbZWHVU_qos9sAwYJ4d8mv0JSyqOEzP4rh11b3R1us_ja2zuRcw0Wb51oeXVwGjeyuwyiTavhvYyA4VcTyngzeWffdZymCRediIIlg3mAWn3kgMUCJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه نساجی برای فروش دانیال ایری به باشگاه استقلال دوهفته زمان خواسته تا درصورتیکه پیشنهاد بهتری برای‌فروش این‌ مدافع‌‌جوان‌ملی پوش دریافت نکند این بازیکن با قراردادی چهار ساله آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25101" target="_blank">📅 23:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25100">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nverbOocemB41732mfWXNHdEG8jcWLrE6K1QzjkQKbWRGIw2x5XwLYS8OAVPtwI3q3H7ZDdEb46nXiLRWQ9Yy8xDqm-_PesAM1JYspCaUPcYN-opcvh5eKLVkMNXSfAuP3jc8-fZZIEh8Vtrty2UIbuuLm-4tj-4GKVEX4_ZQgQnPvfajwwD1QcDm3SyB5xYvWKZe_Az3UhCTWDDuHuCra57cICHdD4C-QVTKhh6c4hv5vaR4hqKv6kiL8JaQAHHduUMd3rH9TGJoJQ8btNMR5ZizeLnJB137KKCXPMIClgKi2OEQgdZJnoYVVOJsEhjn2a5i6UZt_oLXRUNQ9vnDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ آرمان اکوان برای عقدقراردادی دو ساله با باشگاه‌پرسپولیس 80 میلیارد تومان خواسته که نسبت‌علی‌نعمتی رقم بسیار معقولیه و پایین‌تریه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25100" target="_blank">📅 22:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25099">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmGECv4liac5pVAAeQFTQlOISTQkFExokrmDItst4LRY-XvLGRgXsFSmQOLacQnJycLIL-wGGEjfmke0RU7aIPjg-y2fG3CuoyambA69bF3cXxKI79PxprDzEsl7KT6oNbio5zVTc1ivKScL8SgI0GP5SkfnXhXuHEBSM7JiiPl1oeIwHaVHHI13IKGLcGLaEPaBMhu3-DKOLtyql5S1SNlnAASDa1xosw8kqsDvGSUHEYDUC3IeVdGDYyTNmhXKSEmZ7Utzfeo1VAJFnGWac8AXC6xxOZY2GW9fIzTaSgaBcGtFgao9U-edP--SSwiQm00co_hXsabQEevNKxPeSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیو جدید تاتیانا کائر پارتنر ویکتور فورت بعد از عمل کتف این بازیکن و جشن سال جدید 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25099" target="_blank">📅 21:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25098">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHkcGVAJLZ4tDge138D_fU27puJxHVFpQl2OGz-DjW1Si2nxWfrSFQ8YaD2v9yOx0DVWGVtTXR4ly5w71sVRi-ZZrNKh502sISiSag0cMEYvfM65Qu6RUm87bRPBP9Z_vWW8vm1tEsc2tL-uqAmQDleSq97X3agbW2QscJFU396zvs3lIEGnkwTDIT7XDJJqTlJRTdhU2uM0SBHTTkwVs7fiayUoQFDdT57qT2EEAc3LiZzk3Zs4l4ZevL1nblZIs9iFZenBLgeObQhGIBOZaMKXATVxKFe6WnCXTT16yCoQT0Ko2rCgRJlsymg88lE4BpeyiqQcr3OD5ik0zpJVjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه عملکرد کریس رونالدو با لامین یامال ستاره جوان اسپانیا در مسابقات تیم های ملی خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25098" target="_blank">📅 21:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25097">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWT-ECLe_vbSpnvCe58xkMDIPC9gaF7JG43r9J-U7GCJZqJtjeo2B-ZNaaheVEblt-esHwI1nkjDX-acpDWt_nOkwu86BD4ZBt89XeCv-Hc2perqQtAN7rRgyDJNDc_zDm2ZEF4y-WzE-ifuX14q8b_owXsKUSY9hAwafJ_7g8FVFp5Y7QKa4eKlaMEcJ8a0mmcn5OjWKXaa7pJNaZB6IPgYGA4pv28exKsJ0f9Fxo8ZsNJchmFo8cdnqMZggvEhM3TeGYx-tWfevhn4M1EFl2ecrhf7I-GzbTCAxD5IDVhRVy9oFs-Gf_-LKkvW60yk7u5VB98tUBUo91xkvtFLFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🇳🇴
‏چهار بازی هفت گل؛ اندازه کیلیان امباپه گل زده با یه‌بازی‌کمتر؛هم‌‌تیمی‌های امباپه با ارلینگ هالند مقایسه کنیدوببینید چه شاهکاری‌خلق‌کرده این بشر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/25097" target="_blank">📅 21:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25096">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onNARV46gnc5GWDhMB9hTpXbHZ5Q3Lm2e3QAsc3iwFSK6PLNlH3kk5DyAXNds5VSH90ks9o4tAAuiHdGBa_SFm-fRVOZMU8Wv3BGPdWJQYJ_KcmWuoKxgi569CgPftHIPQys3AL3scwoyDLWTEvqvEIZ7ZPTME7fWRxHbVpCzAIxGg-bRHMoMamdIPDLvngpGR64zmklEEFVz_4PQh9W5DAsxQd6EcAVwVbOwYcyzm8fVrXZ3LNa0qE5eknrtbcIgDz9jdcufqoEv7wsKbRFHeYmwn48tkiPW6TeYA7PJ7VU9krS4vodTzNfdrtuwGLTWW8A-NBiQi8K9DaL3fzUjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
پیش‌بینی خودت رو ثبت کن!
🇵🇹
پرتغال
🆚
🇪🇸
اسپانیا
🎁
جایزه ۱۰۰۰ دلاری بین تمام کاربرانی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، تقسیم خواهد شد.
⏳
فرصت شرکت فقط تا قبل از شروع مسابقه
👇
انتخاب شما کدام است؟
🇵🇹
پرتغال
یا
🇪🇸
اسپانیا؟
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود.
https://t.me/betegram_bot?start=p2_r4EF37DCE</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/25096" target="_blank">📅 21:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25095">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjYgi2H_ikkm0K9lXHsjYS3ZsFk5icQcl_0xTxidk7cDMbUUyzY4BXvXSFjRkp54IMW0UizvJtPLKOgLdSkgt5qKGxpZlIefYSuob2t7p2G9NUupzwI4hITby3Y4jwNzS622HVwWWNu8bCUq51KOD0ysmnepcco_90SBUuGEAmDJT2HKeZ9hkL008JuRfBq-zi9yghKCPwBV09mUC6IM23SOfoty3ivHJPVR6cf5f4jinnA7dGHQbGsaJiz2zXjXF2dkEF5BSI0m-5I0j-Kk-6MPAopSPSpLPtpOMZICCcjVVdSwvupR9gbLG_Zb2QJyCCKM-XlV-6O7A0smApM7OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه عملکرد کریس رونالدو با لامین یامال ستاره جوان اسپانیا در مسابقات تیم های ملی خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/25095" target="_blank">📅 21:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25094">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLOh6Af5D4iuB3X2EWWrk17SmYMlNHMbzYZuODq_6yHVVJwX_JtooyANMQBu3hPN-sWvD3RrEtyNJeg7FDf66djcFlG5RyGtGNSN593paySV-jvId1Xv_qgTvXXCL9RlEKVk5d4Drup90mQWRkDXF9Hl7I4Qa6Zl0mSYrVVTDc2vgUFh42WRACKU2deFyxnCTTCvD95q58914GL9-K2CJfKtpoYcGzzrf6SpToz8b1u1pyhu2K4Gpv0Xy6ko82D0RKp39kuPCieBa-b2cCj-iq0DyFi5avLw9gMIrsCntNgpmjgkrqwMFq2R78eTA-sxTpx4u_P7lYPvf4cvzG6S1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌هشتم‌نهایی جام‌جهانی 2026؛ شماتیک ترکیب دوتیم اسپانیا
🆚
پرتغال؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/25094" target="_blank">📅 21:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25092">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GzSKuG3pGzvWntKswzskKCPI-qa9BJ7qekUvHXbJUJWl4--ZBnN2vVI0sH7vdK3wjJgut_iK7_15iQ9AYVjMuPEdh5cUW_ZY12fj2jC_3FN4cBZVN2JrxteYxbZIm67aqThFllCbXPMEUxdHZmvaOMCENRm-vIopyGHh0F6IzJupT5m09bGQ_touX2JyKI5N5neagssHx3Lv4-B1_ZG3vfOCctGaMummRY_oWNizN9RRozb3ucqeJHNHNpwzY7gsQi4yQB31cjBEc3f-U1WRDQdluiXvydEfqaWF_gHtiWWdI6hGV4jXdwlFs4BTC5CbdvEvMCzuEAvWM5pQ7GrOvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BOXQYQU7p6H40nMGnpbP9mlH0Sc_8DSFsXHvZWoOcNWr2kDiml7AxTMmZEByEsQ6DFyIfqy10rYJr8DbBFJLOoFh37vPRCo3UA256XRqdJJCu_ZFKWzqIJD5zy465une44pr-zz-cscoqnuGk94OTDQZyN4HlRUqMSYAhR8sXhm0Ua31JIXI6gp6ZTPgybALRXkVLGHB1bqjsogIbOBy9mng1UCzfsa34qCTem8SbNFlBrYBr6qa0od7D9vCPAgC2Np6ndhdfP4O3o9J91RdCKVgGCAZOyieavTH04icv05XnoNptWu4tNe9JFAdy83bYiKCQUeqVS8m59NS6NOulw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
یک‌هشتم‌نهایی جام‌جهانی 2026
؛ شماتیک ترکیب دوتیم اسپانیا
🆚
پرتغال؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25092" target="_blank">📅 20:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25091">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNS115l8iEu9-pRp5IxNc2VXjlgYXXzMD7YeUasGNDeWAdGM1XRVnV94LEA0rjXFnaYpHKcQIXvwkTmo2E5nC83IZw4WoVv0bvZZ-oTYawpe2WC6yE3zIh-cpzDW3DSBZeu34wbrQHzTfhIIBPCGfRmqHw4anXEa9GfEL_3rAPp7gTv6NyT_wiDw6fwIh4NMDutiw8nJ6u2UmkXle9ITtfZ9f57PYxlvfUzLW734IFqzxiEtakILMQ1RtnYF1c3gzK0Zlm_K3JwCnYZwUZ15AqZfu9-ufp7hSZm26sWMhK62kPETtQEmBiR933daUT3e_wMzvuYrvAQYo1rky2WCZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ مهدی تاررتار نام سه مهاجم خارجی رو به مدیریت پرسپولیس داده تا شرایط جذب یکی از آن‌ها رو فراهم کنند. بزودی اطلاعات دقیق‌تری درباره این سه مهاجم میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25091" target="_blank">📅 20:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25090">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGaS5lBSrHx4CN0w7rzFjZrCb4Tb1c0QUGHCEW1hJIiW2lipHuh1HyUK4dSUj2RrXiHhMQfrPM6j-G3ZN5uxf5X7aBY3leLL0hu4HNSvYAWU5xMzfueWs6r2o8X0k6-PiKWHaJi4iRJUPHikL1DtXddhGf6KtKRU7T20OQzJ3FFlLVeoVbtum4gcjJVm4GSSZNbaG3JouCpXxi0NHokTOo__ZfOIS_F4xRHw3DH0mwKAq02g-nIQ2CvuZGD1foGI6QDWB88x7uwLCxP0bmH-uMz4jt0fNkHSMrx7-nkaa3MRC5QB0NQCL2S_ejL4Hw2vy20OyUBsCFbjVrW_ZtgQiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛سهراب‌بختیاری‌زاده امروز به عارف غلامی مدافع میانی‌تیم‌استقلال گفته دیگر نیاز نیست در تمرینات این تیم حضور پیدا کنه و او رو در لیست مازاد آبی ها قرار داده تا دنبال تیم جدید باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25090" target="_blank">📅 19:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25089">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24c947b2fe.mp4?token=MlIHgXPh4qP7Kxr3EB5gd4-tYWRwbTVzFqgHUh8YLm6FuRGZyZNt_lI4G7Zvo0qIcTfniTN8Z7FbsrOoVHm1eysJYuAqcGygQCXWRjhcz6Gaxx3644ulENv4FNbn7IGFPYmCIWw5mE3_Yh_YjdeBMEu0O4RDIyQ4PZin9x0PTFz7ecLLFBzlD9LI94Xamgy4AUvzJiXsFL8fSAsH6xV0_-eyY0iM9hMLc5hZU4pOBNcorU-MVk0t4n9IuvWk92LmQ92gJwg5NwMytsIVYOmpevwAZMmA1JAXpkcxcl2FxNsPXbwAtPLnk5KuFsYdmBXT6TrJUe8eywG5XXd7S9f_GpmCbuIS88cDztuIV5SBtMb7Dl6dUoEDhMCjFIfJgr4YFt7qBnBdYp4azEn3igBxdMNn6vJehbOvomG2Ww3vN2_6coYQGa_uFhhdyaLwoue9FsUT013nI-Sr51EeHw12fcYN47Bn7--BOUcKVCXBxVDMaB0zjy4rERQVNBJySljl5w8E7rOj3jvppeL0fTWGENY19gqF8Yp1yRKc5dftx-Myr7Pz2iXBKboM_q5bgmYEE3vmVUPcBeZ3wTGYCh8o3ZP2AYxMPnSMG_qwUSJr495uuIaxtW95osUu3VcrcRtvGh5jfLoWSjVm2tZpRqv40GldWRJT3xRg9hyhvAFkmL0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24c947b2fe.mp4?token=MlIHgXPh4qP7Kxr3EB5gd4-tYWRwbTVzFqgHUh8YLm6FuRGZyZNt_lI4G7Zvo0qIcTfniTN8Z7FbsrOoVHm1eysJYuAqcGygQCXWRjhcz6Gaxx3644ulENv4FNbn7IGFPYmCIWw5mE3_Yh_YjdeBMEu0O4RDIyQ4PZin9x0PTFz7ecLLFBzlD9LI94Xamgy4AUvzJiXsFL8fSAsH6xV0_-eyY0iM9hMLc5hZU4pOBNcorU-MVk0t4n9IuvWk92LmQ92gJwg5NwMytsIVYOmpevwAZMmA1JAXpkcxcl2FxNsPXbwAtPLnk5KuFsYdmBXT6TrJUe8eywG5XXd7S9f_GpmCbuIS88cDztuIV5SBtMb7Dl6dUoEDhMCjFIfJgr4YFt7qBnBdYp4azEn3igBxdMNn6vJehbOvomG2Ww3vN2_6coYQGa_uFhhdyaLwoue9FsUT013nI-Sr51EeHw12fcYN47Bn7--BOUcKVCXBxVDMaB0zjy4rERQVNBJySljl5w8E7rOj3jvppeL0fTWGENY19gqF8Yp1yRKc5dftx-Myr7Pz2iXBKboM_q5bgmYEE3vmVUPcBeZ3wTGYCh8o3ZP2AYxMPnSMG_qwUSJr495uuIaxtW95osUu3VcrcRtvGh5jfLoWSjVm2tZpRqv40GldWRJT3xRg9hyhvAFkmL0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دونالد
ترامپ رئیس جمهور آمریکا:
نمیدونستم که‌ کارت قرمز گرفتن به چه معنایی هست، اما وقتی شنیدم که به‌این‌معنیه که شما نمیتونید در بازی بعدی بازی کنیدگفتم‌این بسیارناعادلانست. چطوربازیکن رو واسه بازی‌ای که هنوز برگزار نشده جریمه می‌کنید؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25089" target="_blank">📅 19:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25088">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ts0CSB-M5HK_4zDkNv-IIM61iMX_6K9P70gOfJkhl4Caj17o6z-vCrxjxvHguZvlQBD17nlxuia-8Ze8Zmv4xeNLMm3iISLJYHtNqywX84zk-9onEQCxOpoXYJqaYxYaX9T2DOFFwJTdO7bsdbEOpEvMs0I-097y0oAi82BaS4kywbE-HUWbOhW0cdCsRPuER2MJbZoQgZaMBgLB-B139ylfzWxf373JIk3PFOqhmPDeBRd2NIRveLVVt2e-pGEJu4sgucierqin_kcmAW8pqHAEfqzkTGt-BP1kesWOMvIpuIio-eRwlLHtkb7gqCQU88CHZfYLU5DIEumM5DG6AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
طبق‌اخبار دریافتی پرشیانا از مدیریت باشگاه پرسپولیس؛ مدیریت باشگاه ملوان رقم فروش فرهان جعفری ستاره خود را 35 میلیارد تومان اعلام کرده‌!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25088" target="_blank">📅 19:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25087">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZI7UK0lBifjnqQrRFsWQyNdOoisCpDSrGQ4s42aTzZETActHdMjF5Hs3UQBaPJA3mlWdxpEySFxNtg8OL0r9WD091fndT62uar_6Lb0lPDRDRrSuMlAcNcXDAQCajLRLs_8i7pBUme4OPlNCiGmV3dW97QOUlRAX-d_dGT9TukpYLyMTAy1Jo1RTD7dHzxG-5JC1HMjNIBrCtkwm1pD7pZp3Z5tFH-N0v68-6RO7qvm53ikHBv4ZthCFtfSW-WySLhihQCexUNOC4ElFr3u_oOn_QoTzVB9dJCR5FVXWBNbo0lpVHDDFvBlCwbm3V9eycJCBSptS-0EmBVpbVlACA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#اختصاصی_پرشیانا #فوری؛آرمان‌اکوان مدافع میانی گل‌گهر سیرجان علاوه برسپاهان از پرسپولیس نیز پیشنهاد رسمی دریافت کرده است. مهدی تارتار از مدیریت پرسپولیس خواسته‌اگه‌باعلی نعمتی سر مبلغ به توافق نرسیدند با ارمان اکوان قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25087" target="_blank">📅 18:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25086">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZoR_EBW0KnRxYjyyuVPENz3rdb75O5Z89LnPMKJR_c7t5Fofr6RnITFHmGN_kaQIliEgNUoYcpDVAcAHx9PvjSNTD2DgnAYAQrgBvslUaj6ls6tJyuo8sQU3qR3kxuS0CFlQ6q9mX678hvK8STFXk3wx6DjZ78Y80l6pgf9RkSReMBKqCAVx33Vyi-8f0Zn9sxS6hMf4GaAYAbZKJXbzrHgSv1eUCn3d-zUHM1mcP8eO16orsIKQNGOxhAzLrbD6na9j5xVxY2FBmJC1oo4cO3F19F51Tv-sYse3IKnv866FAk3YypWHSpxTev5Xw81eqswxbt-5nJTg37hZ8bZRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ علی نعمتی مدافع‌ ملی‌پوش سابق باشگاه فولاد برای عقد قراردادی دوساله‌باپرسپولیس خواستار دریافت مبلغ سالانه 75 میلیاردتومان‌‌شده‌است. درصورتی‌که بانک شهر با این رقم موافقت کند به زودی پوستر رونمایی از مدافع جدید سرخ‌ها…</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25086" target="_blank">📅 18:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25085">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cttdhCoiZs14XPc4PaDOiMMS4QUs5tKzYpBmhifnw9I3Kl1oYa2-qEoYuCtr8wO189yJ5RqSajglbi6KGrgnhrTXP2nowbUNOhvvoSl7N-JSGu1XC2PC0nH3cWAk9OyvLVJQnc_OZs0sSQzNn8CZnujzIVArHOAgElRs11r8rsDdX0Cp1JA_4TowTde5tsp75wjn0EYpVBr9Njkn61PctnO1XtuHQ_006qFN34mDQcha19_jii9elXLNV9UNoqADEUQE_lQe4CzRk2fdgx29W5OFtJ1ElU2Eb7OeUdK8of2_Gv-TyV9PSuWvngiCxQJIfQVtsJTGQyu0W60k6SZWeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25085" target="_blank">📅 17:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25084">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aacoukSY8ErkRFvOETih2mjJ8sI7TKLMIXX_7T5LoNcFPQM_Gkgxc0ftZm2SvKf570VSksqnqccdqC6AgZT-fqB9-HYjpwvvaNB7GL_1mX77URTzgxfnKl0dGkBlOR1z0rzQJcXq2Ms_mRrAdz-CoHvYzvhKXF4whh-4AI1P8pTDQ2NNuAualxBIGUZ1XXWbhMO6PXImGMtekV2nHhtv3Hg_RqOzVvRX7Mj2qV2MJBeYPur-MFb6LvHMXCJP_olanigCIWGTtWWvPKAVW2shc3SbRoGgpvjS5fYC8phfQs7n1wWfZbMTcYWE7yz-EF3D4SwHpAaX4jLzz60LR8CIXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ مایکل کریک سرمربی جوان منچستر یونایتد به سران این باشگاه انگلیسی خبر داده از بین کاماوینگا و شوامنی دو هافبک فرانسوی رئال مادرید یکی رو در این تابستون براش به خدمت بگیرند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25084" target="_blank">📅 17:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25083">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbTo6ZU-fJSQ9FPPdyBW8-DelWqiVYnfczCEQZVWl41HSu9ODuXlx5Ob3CLrGx-eFMehNU-DDf-oNcl0jOg865CDhHSC2oF6sbqst4iO3su13DDuSs8nEB-dylMFF1kq4wMRRMz0Ohd5l-5kC1k5D27Dv9D3RPKVpHgrqgIPJ8vs2toJB7MoX37Gdx017c9pTa0V89qt-fslPcGVTj7QBjAo77NOeaD4QZFia3ZoKLtLZBUX3jrzjHtGpp74SOac8E9qJGlv374DtHiyO9f1eVcssYOMZxHsvRVFU9Vi1aICqubPYfPJZ4-2pe99JEePx_6LG_dpYdnwYKPTfT2ShA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🇳🇴
‏چهار بازی هفت گل؛ اندازه کیلیان امباپه گل زده با یه‌بازی‌کمتر؛هم‌‌تیمی‌های امباپه با ارلینگ هالند مقایسه کنیدوببینید چه شاهکاری‌خلق‌کرده این بشر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25083" target="_blank">📅 17:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25082">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HaJei_kKXLUWQqja66RzeDNURn47WGPTOdrO7FeKJ9FO_OeMD9TVNLcg_Uimd0oAP-iPVnyWtRKnz35y_9EO81Dx6LTmacGqdEzw-hsR3JMWXaEUJmL4KPp9MRrI5xya_h1tKhWGzlQDhaM7FA6DyO2d02NzpNso60g8yOh2K7kjeKF5RfzbRK_LnKzFkntFavrumERddrJ7FlZkfPRFB-UCU3MrdhpNb9KH8XuupyOLqiCJMjWy58vOKEdzeo_FBVoQ6WuKn_dZ5QV2BXEZiXfJpYeJuDf98MJJF3HJ0cgPb4Khi9cBmKNCXpOvM4hTIej3mG6N6bCOoI_G22d3RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
رستم‌آشورماتف مدافع‌ملی‌پوش ازبکستانی تیم استقلال:
ما از مرحله گروهی جام صعود نکردیم و حتی موفق‌به‌کسب یک برد هم نشدیم، اما با مراسمی بسیار بزرگ از ما استقبال شد. نه فقط من، بلکه سایر بازیکنان هم در این فضا احساس راحتی نمی‌کردند و باخود می‌گفتیم چرا تا این حد از ما تجلیل می‌شود؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25082" target="_blank">📅 16:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25081">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWcX6xkrB8AkkAB7wQhX93OVCgtOQkW3wXdP8PsrMC1-Xf6yH1p3khzW8_Bsb3zimv2SiZAb-OZsr8fWsyDGlsoBc5z7tOymLv6cqDIl_PezhxrHDrX4T6OThbZYPrxEDWpeapJVbtQ_7sLlrAHXzEJEHuIH9-XoKlYIUVId_ZaGJlAVWWIDlBVwKDPko_yVpmTR6d7c_CT_HTbkerGSSXnAO_laxmmOHlM9VpfWfueuDeDw49d_dhfjD_OKKGETSffQN5tnTF32SkPu4ZNn-KX6iVALIhB-2TYfg-Sp5V7IF2ojnfG93ThCh_2of5jHDiT2uqYQCHwrrUFfrbAerg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لی کانگ‌ این هافبک هجومی کره‌ای فصل پیش پاری‌سن‌ژرمن، با قراردادی به ارزش ۴۰ میلیون یورو راهی‌اتلتیکومادریدشد.کانگ‌این در پاریس ۱۲۴ بار به میدان رفت و۱۶گل و۱۶پاس گل به نامش ثبت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25081" target="_blank">📅 16:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25080">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSZxgU8oj3iPbFPYmtFAQPxM_4GvsgJQ6a4ZUUklb1jOo3wASvAMfirj2fej3Z5KVJt0AVuXRCtkhEzZyRshlcjskmw63YidRpBbDDxlFE6oiP-bGhkLLIiL5SD5DPKe4POe-Vi4CdhiEPr0I-pVnue527Kcl7V-w-5metzOuQtY-ex7AJbZCFFN7zkotlhakGRfyx9biOFnDWKbJibc0FxQD1uu2NyE5axyVMrq5IqW90hKRx1beyO6J8gxrLC8tAdsMLh-n4Xs3X77GgPXHXNthomvHk1rbEXMl4-MP0x7ebwHkJT-E6uwSdR6NXomcIwXvgt8a7OButObDiIyZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عارف‌غلامی مدافع‌استقلال‌تابستان سال قبل قراردادی دو ساله با آبی‌ها امضا کرد اما کادر فنی به تاجرنیا اعلام‌کرده‌اند درصورت عقدقرارداد رسمی با سید مجید حسینی دیگر نیازی به غلامی ندارد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25080" target="_blank">📅 16:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25079">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmHb9exj0jBO6HawF4i68onhHbhLNFOFSitd3o7cSeZeEtNQ2yQSpZ08YydNKQifZ4-b2tJd0r8C7R7IMUNrEKmkOYEzDvq9vN1N5nZ-L4HKAvxbJQJn2zSYO4rcetylQwbLh5QmdVI4pW_Gh10KcrHkwDtRtBpvcEWZ12ciFqaBCRWts7HyNMPqWMvD2XY-2mE-g5QreYi-QIo1A6hGOj_8SstV3y2JHrNRGCQ9COUIQiiQIDUJj1hPEBA8ebyqwn9PC7PwahNSN39Qo2zCYqt0Mu5_z4RYjuYK1rafv5J6GxcotU682Tqfc-FH1jifgzbiYs3pPENMqxwyIdieiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی تارتار سرمربی تیم پرسپولیس درجدید ترین اقدام خود تیوی بیفوما و دنیل گرا رو درلیست مازاد سرخوشان قرار داده است و این دو بازیکن نیز بزودی از جمع سرخ‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25079" target="_blank">📅 16:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25078">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7cm32w5yc8Q8FDY9YEsynliUgRKiAqIesUCQE5kcRu1oqY1KQ_XynrynVf7TzoBvSJzm5Qgi-6p576WpBykmAEo2kItvwiw1-hWzukgkIMco3mhkJYEHQqZqL3Kd_d5keP3nQMqGoEBzXvKLis8WMyYcZA8vouA807xduZw53NxJNBtBhhm5V9y3cSofYWhr7cvSibAY-wRpl4yCxXdDqPEJXNyWxnarOFaBYFxo4FteRuD7v5zzRBwHNxWFxz9P8dVyQDimiFCSYd353ax-ko6PufhftUKHvJpsmX5xkSO7ShS3A-3zZDuJXTh_tmt3jOYm-0cS3qf3Tr4zCpp0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس در تلاش است که در نقل و انتقالات تابستانی یکی رو از بین‌احمدنوراللهی و محمد قربانی جذب‌کنه و تماس های اولیه رو با ایجنت این دو شروع کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25078" target="_blank">📅 16:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25077">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNIBj0F80zE9et4nVq3yi2P70YsgZI0gFYZeIGvbz4U-niwque6DmkUvexmpsJwrJGWFDwm6h7NvT_BAhRXg1MS5lLw-NobIFXlfCVfi5DL0HNynA7JnFXJMjvvltPPPyRoVYAeQEj4bNKIObBD54Eje_rTRc9OsIxzz1AICwtfcfgPhpfPSZzvxX0uwIuZzmNdtq1rpTqsQhLe9e70KJ4Bf1l7YxcyOzaZQtyzQ0z-trvcC2kRtbGqE_en8XwfWnIIl39glFNKgvmEgtHYRAwtfAu6srbaqxxHQFm92pM3FETA9z9jnsV_6qaqiJgYS4AUiONhsr48QPGEh6Di4SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇧🇷
ویدیویی‌ازهایلایتی نیمار جونیور در تیم ملی برزیل به مناسب خداحافظی او از بازی‌های ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25077" target="_blank">📅 16:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25076">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEW3gB0Z7UWQzWu3bLVrrLR5UaScwrUiSh8c9WXy3ZTYlRieDCdwS0OhbyxosMA7I6KBYrCdTDSTXGfD1MDNKcJDLpm0gEb8glvJMSj58uNPyTi8zgdPRIHP90px5ExEBAQn_JSd401GlJ85FplkA4OXUevJxMCA-BmdcAtJDnv2w1XUnBfffu4_6i1KzGqeC-xXm1Bv09h0mjoxHG5p_rw2eewLlvqsQor_eirSv4jQUVgw_U0K2fPcV4E_s3IWPMcNY3gg8zNQ64VGZ_rns2bExtJxW_mKM9SGi7lNSEjGZkvCyvHuofL7ZdZx71MtDF4yKZNUgiDy77CEZqCPnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی2026؛حذف شاگردان کارلتو از جام جهانی با امضای هالند؛ دو موقعیت دو گل؛ هالند یه تنه نروژی‌ها رو به مرحله بعدی برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25076" target="_blank">📅 14:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25075">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e147ba88a9.mp4?token=Z9w2g7UO_psQ-K6x6Ojm7tdMfjEWucbAMP42rGbGt8Vd4rrMCSLQ7mBHnRolOplEH1FYdsDVf4sY3R3QoEhkj2ulftWjY8qtDS0eLawdS-uWiGdg2RmHF3c-6VwdnoRRI7QfPgyl8-InRGVZGv7dKFrabRjcMXILdczAVafZQtqCGRxuaJcrH2EpefCz5bYmAOZIzyTI3WnIE9dK8VF5m3ALTnsgiJto70op44A2Ppgc3np04EtgpDLp-_tLcnHvglbnFfilYKopjTGcG16uwQc_FwdCNuDWLyVog-sBmdNB8xMRaHePnR7r848huQX4U_OnlJ2pqTAJ2ApvFuRbnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e147ba88a9.mp4?token=Z9w2g7UO_psQ-K6x6Ojm7tdMfjEWucbAMP42rGbGt8Vd4rrMCSLQ7mBHnRolOplEH1FYdsDVf4sY3R3QoEhkj2ulftWjY8qtDS0eLawdS-uWiGdg2RmHF3c-6VwdnoRRI7QfPgyl8-InRGVZGv7dKFrabRjcMXILdczAVafZQtqCGRxuaJcrH2EpefCz5bYmAOZIzyTI3WnIE9dK8VF5m3ALTnsgiJto70op44A2Ppgc3np04EtgpDLp-_tLcnHvglbnFfilYKopjTGcG16uwQc_FwdCNuDWLyVog-sBmdNB8xMRaHePnR7r848huQX4U_OnlJ2pqTAJ2ApvFuRbnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
درس‌بزرگ‌کیلیان‌امباپه و هم‌تیمی‌هایش در بازی مقابل پاراگوئه: تو زندگی ازاین‌آدمای چرک و بیهوده زیاد هستن مهم اینه تو زندگی کنی و تسلیم نشی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25075" target="_blank">📅 14:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25073">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RDaMGr5_TYPdMkR8KtiByNSmwdAjJy6Bfg5PE9tXKMA9L-1_y3udUF7oAQ2kSF0yxJyCq1zipnMMoBM7wC8gvKLyc3PE8bkC22318golyJHP3P892d1quTOsax5b2MHc9dX8LFHtvgSOWvMVcqitXV3pztLqkGpEGCqRHLurn7UjvtX8upEDr270KlSOi0pjbWVqvY_KMH0OqnBwxwnEl8kppWUoQRoLLNC0B4GldFqyjKX_-kdZUklGoj17vH5KUivEbyUpHdbFvCB5jlLwZ03tol8s7lH1zV2whdWkYxDesCigUxeNkFbUEUnp7I3-CJyqtl_ztOSHRbtVkHg4ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jRmErTnEcg5hG7_lTAcn5E0a8XpgSB9MlB1S2Bn-KZ5cKzVb2fYzjZNySYoyzGYsgk-sXRp8LRwzvEehXEfk736JKo6xdV08_pUnbyVLneZu0FmFOTm7MsP1xmpZJcMrOGfyD_Ra0Yr67LOqCrxePAEdmxDtFIgiIFL41qFZqIBjfKIDZM00oOCkyyOQqcRUZ-oz2ecaevUt-WR-eZ7sURgci3_erSMPLonDNACqV0ie4nmlVUhy6Jcd8Xm_Y0bDBed2tco2NnW1xi3xkgbRJDpILvN0xZcP48veP09rB2o8d5QVIC4iWWb_S38fEYztl_vHFpATJleug7knN5m-CA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
🇧🇷
ویدیویی‌ازهایلایتی نیمار جونیور در تیم ملی برزیل به مناسب خداحافظی او از بازی‌های ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25073" target="_blank">📅 13:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25072">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_Gu1Rjs7iOCt9giSGwYttqH9BDjDfeikMZ3sLuE5C2xBtKDn1FCTwUlCH6luCuclbIGJU8W7xL_rFsjWWj46A_RFONQbhTJJp3ORdo9Ka9diCiVG6Yv5XD6aDYq2_oU0_hPmHReIUbLbacqojOyRpFleylE_MDZ3hsr_r_cOnABLTa1XG_sjA1Xj9EpNE5k-67VrZ3aSvp65CrHftqHB5Qqi5stJgZNnUDIhuPc5GlvN_S1lRavWG6dpuQXqANALK1wg8TPpIOjk0lpgjBwptQOF8328_GBWigye2sGbmyBn44G7buKalOxbkJxbKnT1YqZGb7WNRJrJUJ1t3XXzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌ عملکرد کسری‌ طاهری
🆚
پوریا شهرآبادی مهاجم جوان سال آتی پرسپولیس و احتمالا استقلال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25072" target="_blank">📅 13:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25071">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZzquo1RmCM_CEmxjGQJHFB38RkjR0w2p64GLIWTf9zJstw3jCyH4_OT4-6K8X6i4dRVnCsukWlnUYke9x4B3rHbHlUqj8Zp0AKzzGl_ue7YQOUs0J5mDrmDFEwfzTXaCmB-h7Uxu8fi_QSpKRlQSqHcq6obsOpBvJaDhqfV3Nhlmmacos-vL-5pQOw898Zs5TBiiKapr_bxO7bYTHNqRheBMlEQ35UyH-qZByF-G49G0Lz8AaV96ChM6wEv7wzUbnNm5FuX3_MfvI_T3S0wA1l7o2KemMAPYWSajt_LVJ1nJ-efQLzESwFsXQd8gDCgt0N2oUAr1cQm_1OeIweKVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کارشناس‌داوری‌ دیدار انگلیس
🆚
مکزیک توسط مارک کلاتنبرگ: تمام تصمیمات فغانی درست بود. او بشدت روی بازی‌تسلط داشت. علی فغانی نشون داد لیاقت این‌رو داره‌که مسابقه‌فینال‌رو هم سوت بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25071" target="_blank">📅 13:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25070">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4fFFcxvdIeGlUIhLsVubRazEB1Z38Kfmap_quXSGYJdjyZdiLR3hCCRrzwOYY34c4mv0iKaSn0D8Q4jhqRSt8LF3nzuukM1YXq200qtyZq4s8j0eUJ4nKwYgs9Eff72snS9rVHKOdTAQ0mXD9_717sCAC6NR3wiEgJpM2EzGFXUYTsohY6rNN0u0uuhEK8nViK-m5iOBm4FoJGvAC8QYDv5808Fv1xKVjUZL7QNHojT8GvjvoPKrwzT6o-ROcSo8_EcM_NBZ2ibbEsmpNZTN8NExhwWMgJMaPLKsaj5KsDXHIwK2p0NoBfNHpLFKnJNy_KzWu-FmLScYClWs8Z8zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25070" target="_blank">📅 12:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25069">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ax_qHu8Uj1iXU5piMS-dB1epeQinNEGlEcQAILfLZkcxnjLYpBAiNRTRxyczPYQ5c_Zv8DT5EgUjP2SjehfXKBgpZnx1jPdUSzde78fLn8nCPdkO8tke7H4nui1PW_CAwzpCRnU3y5JqpG8HuPiOaJNDWGf9pCLYxkjhOJJe3q-9RLGx3P4HoFmNBk5UbNuHMiEO6yR9rO0gLiY2OHh84WT2j187-BnmIMo6OSGnAQhWArNtCuIKvJBXCvBqvIoDoWjOWy8RWTY4Db9banFGLq34RCnlXsAQ_aV36lRS6a3NGJ0cOXYyRWUK-UgGNDwgRtAp9iytmSWpZA2PnBwfEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
هایلایتی از عملکرد علیرضا فعانی عزیز در بازی بامداد امروز انگلیس-مکزیک؛ چه کیفی داره خدایی یه‌مرد ایرانی‌ الاصل تو بالاترین سطح فوتبال جهان به‌این شکل میدرخشه. تنت سلامت علی آقای عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25069" target="_blank">📅 12:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25068">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6Ym_dmRrR2lqE-4si2d7fepeapx1T2YDUTv4RoA5zL0oQjIHzEYeFx2qAUg7mb_XhR5MB7qlA8zB9k6fWwp7i3B1diqVfywPrqIVeousgrQwCya5ZmUnbe4Ja8-vVQC0nn1JeO1acOpVWOI2GoK52tUHLq-BSqNzwi9rnSQYCY8jlza9afwn5VWYd8BTXlsgKndmBXESceGkuLPl9M9fA29otHun6417UG0jk9uNlueuLalZSGCddhCDBVuMpCZ4mV0AdKDwK1jb75sr6emHazBG8ukEX-CUcNXibmQfNTV1OdgYFda22EYE1wvP-qNX25VWRX-PZcHYK03u-s5ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟠
🔴
طبق آخرین شنیده‌های رسانه پرشیانا؛
باشگاه پرسپولیس با احسان محروقی مهاجم گلزن فولاد خوزستان واردمذاکره‌شده تا درصورت توافق نهایی با این مهاجم قراردادی سه ساله امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25068" target="_blank">📅 12:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25067">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19dbd7ccdd.mp4?token=j1J_BwgqRV7Jl3Cieur4OimJgdpVCl4kDW2R-guvREOqgJj_hzw1lebqvlvLG_20fDntP4NuA21THi0UDqCcj8UTxAczrvbIWJmeHh2vCMTgBacuK15Mi9Muz6Az4IspzaWtXA4Qc92Ah3qRi9zvegDj0ssP_CUdg8-ozsegkg3BSlZV45ezedh94dTN7spHxKGu4h3ErS7BGhyLtfIxg_UYwLvJrHOoGSK7mijaHDEgzPysUXpFVa7FaXMYh_A9JsF3JMbLPjJtu4FPMXYeNCyZ8DkVpFQsaVEdHeWcvIdmMETrkoUSooBqUAP0mqCMWlVohdZT1ADQgE0-M25BJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19dbd7ccdd.mp4?token=j1J_BwgqRV7Jl3Cieur4OimJgdpVCl4kDW2R-guvREOqgJj_hzw1lebqvlvLG_20fDntP4NuA21THi0UDqCcj8UTxAczrvbIWJmeHh2vCMTgBacuK15Mi9Muz6Az4IspzaWtXA4Qc92Ah3qRi9zvegDj0ssP_CUdg8-ozsegkg3BSlZV45ezedh94dTN7spHxKGu4h3ErS7BGhyLtfIxg_UYwLvJrHOoGSK7mijaHDEgzPysUXpFVa7FaXMYh_A9JsF3JMbLPjJtu4FPMXYeNCyZ8DkVpFQsaVEdHeWcvIdmMETrkoUSooBqUAP0mqCMWlVohdZT1ADQgE0-M25BJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
ویدیویی‌ازهایلایتی نیمار جونیور در تیم ملی برزیل به مناسب خداحافظی او از بازی‌های ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25067" target="_blank">📅 11:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25066">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZnhoqG3dOPqb3RQSi6j1YBUixCYENjNa9W4lnts_57HLZO-j8Bv3cYJbg7eiRV3OKybRwQL1wUUJWkmx4o5UGvWi0120bsfc52mExnWlEb6doj7Ss51lh6fDVbpDm16hDUMVvhMRcY8pgSPyUdgRDSR3Q6V4cyz_hwmRQXvHbSnHcP0UftBzKBtM5y5cmdXv-QULNQM9bvzaWOnSknSRHmuFwIsAvKDfCY82GvEwafquoV_Oti5cVhdlAdAcIb9GYRhKYRPnm0HCqO6zpxnB0mKOFelNMhEchR4X6Ao6NANmZRPhFgY0qSj6G6qjrnq1_Kzv6VE81fGvorE8xLWLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛باشگاه‌استقلال برای جذب دانیال ایری پیشنهاد فروش عارف غلامی، محمدرضاآزادی + 30 میلیارد تومان به نساجی داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25066" target="_blank">📅 11:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25065">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/expsDEmhjTM-17m7PaHzuv8oKz6AVaj6mLo61VcKSBCVrDzz1IbbvNyM7wQLI2OeK8ZO7lEE9j6X74BvOKcDOKRtddnj5BjXUYPFq7fh7Oqaui7FgngEgY8TsuxsqAvLfqKVTkCsgcn9gInNATQhSbznbrxdYhHsO_WHErm8GcdhexjNOAkVbM8fk0A0d_Ym0eokLFpryqmDXZPyjDp63xEFDWTZ5R2vTk78nGjv00M7g65shkOcjkIJXyOTuWhJ6HWUwOEnhG26jk2rbzBBVilYMB4aCWmVCSt3a8_Fp1in3lYX_STtRVXEkqQ-bLlxnA4BcDQP5mQs44A0XiKwhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25065" target="_blank">📅 11:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25064">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9398d6a28e.mp4?token=YcRW4iVBbaPqTJyTz_hWcI1Dx_6wwf1j79gR2j72l2TFmB1DrQ2Xs_nm2dlcSZRHPwrJNq8fykG5egHpZqyOlBvRx-Ty3W4SgzsobNFvV10iXgZSNuwIl9tCuvw_h-9YbGT_5vsWrOgHLsZw8nGhfV9XkN1Eh9rT7HecFXZANTTXLN_uSfR5OhgFZmlbJGPZkJWEQVA0JbPn7kI-1An3MshhpshLtGguRYxVhE5wZAOmilfCvX3vShYE2OhqCQ_Y3QLzqF2Q_oKEfKfuFsMfYv9pW-bDqDefvWHa9A2ItUu5yk-S4AymO_e_OHBbaQs-6M_FxqlFp_HfCrdvXhh0uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9398d6a28e.mp4?token=YcRW4iVBbaPqTJyTz_hWcI1Dx_6wwf1j79gR2j72l2TFmB1DrQ2Xs_nm2dlcSZRHPwrJNq8fykG5egHpZqyOlBvRx-Ty3W4SgzsobNFvV10iXgZSNuwIl9tCuvw_h-9YbGT_5vsWrOgHLsZw8nGhfV9XkN1Eh9rT7HecFXZANTTXLN_uSfR5OhgFZmlbJGPZkJWEQVA0JbPn7kI-1An3MshhpshLtGguRYxVhE5wZAOmilfCvX3vShYE2OhqCQ_Y3QLzqF2Q_oKEfKfuFsMfYv9pW-bDqDefvWHa9A2ItUu5yk-S4AymO_e_OHBbaQs-6M_FxqlFp_HfCrdvXhh0uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
هایلایتی از عملکرد علیرضا فعانی عزیز در بازی بامداد امروز انگلیس-مکزیک؛ چه کیفی داره خدایی یه‌مرد ایرانی‌ الاصل تو بالاترین سطح فوتبال جهان به‌این شکل میدرخشه. تنت سلامت علی آقای عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25064" target="_blank">📅 10:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25063">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2866a16ef2.mp4?token=H2jDKrW0yc4Oxon53sVzw8hQ_IG-cKDGs6bWGBxb4vv9eLvYUkEophINS7HjjDIsBiLlG01S_ufs0xQu6zLwdSOaB4rfgyjyyzyhfcAZFmecJmmPswXLtbTGwNCd0U8zeZccIACdZ8L--Dg3-vV0_v09Ed8y3HyKtPtiKV0MZAypILMzuuMzJG4D-5y-uP4T7UaoJCmRGG4MRCq7Sj7ux7TNqLq2ti6clP3TYRoDMbiSrsbS6Qnz11JAHBQETwvNkCGwK1WnKL8ZfiZc8mEqGALK87doczyqxpudXrFM0n8cFc53L7-8lcYhNmzHHBuSpqo2uc8v4TQUA9IPJ4Sz_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2866a16ef2.mp4?token=H2jDKrW0yc4Oxon53sVzw8hQ_IG-cKDGs6bWGBxb4vv9eLvYUkEophINS7HjjDIsBiLlG01S_ufs0xQu6zLwdSOaB4rfgyjyyzyhfcAZFmecJmmPswXLtbTGwNCd0U8zeZccIACdZ8L--Dg3-vV0_v09Ed8y3HyKtPtiKV0MZAypILMzuuMzJG4D-5y-uP4T7UaoJCmRGG4MRCq7Sj7ux7TNqLq2ti6clP3TYRoDMbiSrsbS6Qnz11JAHBQETwvNkCGwK1WnKL8ZfiZc8mEqGALK87doczyqxpudXrFM0n8cFc53L7-8lcYhNmzHHBuSpqo2uc8v4TQUA9IPJ4Sz_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌ های جالب دکتر انوشه از دلایل علاقه شدید بسیاری از مردان به فوتبال و مستطیل سبز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25063" target="_blank">📅 10:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25062">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c09d93bfad.mp4?token=D48NqPo6HdMZfnlIsyuV6iXZbp70w3fHAI862RlnXu90C41z4mSyUrPR8APgO2t40l9bl10iO17up3doHgkhPhi0TITJlBNE-rDiESDscGq_PT8uUxAGxPfnZYxMZgOle6UxWVz4gzT3xs_G6moUZFvV58ADVdO-ZQ_vRoAU7xYYRPO_SktEYlpja7kN586u2BRbm3EPrA2a9yO6g5c7jZ3CO1tj8qUwU-32Bcrdy2daIq2W3EmmmfKFFHxbB4KBmFMGGRilnaG0r4H5nsUMtaBRFoQ7ZbrwsJf53kybHoND4RBYpEEXkKuEOLPcRcS4_wSxNEvj1u-MlZ6azzKAEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c09d93bfad.mp4?token=D48NqPo6HdMZfnlIsyuV6iXZbp70w3fHAI862RlnXu90C41z4mSyUrPR8APgO2t40l9bl10iO17up3doHgkhPhi0TITJlBNE-rDiESDscGq_PT8uUxAGxPfnZYxMZgOle6UxWVz4gzT3xs_G6moUZFvV58ADVdO-ZQ_vRoAU7xYYRPO_SktEYlpja7kN586u2BRbm3EPrA2a9yO6g5c7jZ3CO1tj8qUwU-32Bcrdy2daIq2W3EmmmfKFFHxbB4KBmFMGGRilnaG0r4H5nsUMtaBRFoQ7ZbrwsJf53kybHoND4RBYpEEXkKuEOLPcRcS4_wSxNEvj1u-MlZ6azzKAEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
حسادت عادل‌به‌حال‌خوب‌نروژی‌ها بعداز پیروزی ارزشمند و تاریخی‌مقابل برزیل و صعود به ¼ نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/25062" target="_blank">📅 10:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25061">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daac7485e4.mp4?token=RizC0xkjPJn0CmXvJXZX7-a-jRtBVvvuGFPCI-cf6UzumZFArzeQVmXl4cvwQeZEafPnWN94BgBqV6Plro7bjl2-bhNJGC8Q0hszOOrIa5110v1lHHH8ovFJ1Pfc7pbiPGPzRgqk7bqylkoGPgFa5cCa0SiJvPTruw0Llo6khBr9rTZQMJcbd05lVqBT4ZT2tbhECYI71aVX1K3N5HNhkT-7GLcf2Z-XvnvUQDQwskjuIyziBvztWfTdsxNeoxQRk0aQ2Wwrq8X65oO8QCQ7VPqB_kTW0LQlVb7XyJbexC-BdOC20SNnLiKWTXcyggOajGA4Sq7KIAPZ7OKwSbINsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daac7485e4.mp4?token=RizC0xkjPJn0CmXvJXZX7-a-jRtBVvvuGFPCI-cf6UzumZFArzeQVmXl4cvwQeZEafPnWN94BgBqV6Plro7bjl2-bhNJGC8Q0hszOOrIa5110v1lHHH8ovFJ1Pfc7pbiPGPzRgqk7bqylkoGPgFa5cCa0SiJvPTruw0Llo6khBr9rTZQMJcbd05lVqBT4ZT2tbhECYI71aVX1K3N5HNhkT-7GLcf2Z-XvnvUQDQwskjuIyziBvztWfTdsxNeoxQRk0aQ2Wwrq8X65oO8QCQ7VPqB_kTW0LQlVb7XyJbexC-BdOC20SNnLiKWTXcyggOajGA4Sq7KIAPZ7OKwSbINsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی از صحبت‌های جواد خیابانی دیگ رد داده میگه باید در پایان جام جهانی بستری شم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25061" target="_blank">📅 09:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25060">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🏆
ویدیویی جالب از نظر دختران خارجی درباره بازیکنان ایرانی و نمره دادن به قیافه ملی پوشان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25060" target="_blank">📅 09:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25059">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/529bb11b1c.mp4?token=cSdqbkT6JVU6CXUISPMlJHD3JMU7Upj-0Kp_i7diuh6OLv2PHMuBscYXb2kusxCReBw08eBsMvP0ulwErVc0Mhax4LmiQe6xBIJkT2p4hgiNHbR5JV7iL_tF_WDCQA8loL9V_OX_AQoI5WBN4U7OR2E5HA4dLZF_pySjofNkUX7Pm_i-oc_fdj_fOwVe7ndqLhOGw5XgznsDIqGpBpbeRzUwJ8W-KT7Hah8giMXXsOu63z0u7Mxgs-pRX9MXuNUmSTAbd2q2Ejbt1qqH9zd0XZrCUYX79Q2FhiCPV-MQniGDr7wsP2hSh4EeIknAoEkglyQv4U_6K1eWxkx1CD4ejzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/529bb11b1c.mp4?token=cSdqbkT6JVU6CXUISPMlJHD3JMU7Upj-0Kp_i7diuh6OLv2PHMuBscYXb2kusxCReBw08eBsMvP0ulwErVc0Mhax4LmiQe6xBIJkT2p4hgiNHbR5JV7iL_tF_WDCQA8loL9V_OX_AQoI5WBN4U7OR2E5HA4dLZF_pySjofNkUX7Pm_i-oc_fdj_fOwVe7ndqLhOGw5XgznsDIqGpBpbeRzUwJ8W-KT7Hah8giMXXsOu63z0u7Mxgs-pRX9MXuNUmSTAbd2q2Ejbt1qqH9zd0XZrCUYX79Q2FhiCPV-MQniGDr7wsP2hSh4EeIknAoEkglyQv4U_6K1eWxkx1CD4ejzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هری‌کین بنده‌خدا درپایان بازی با مکزیک صداش بالا نمیاد خبرنگاره‌جلوش رو گرفته میگه حرف بزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25059" target="_blank">📅 08:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25058">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WScW-CwaruBs1pRyCKa6HeEf5zpdV1ZYQ5mKW6MGdWJDoOyVo1Lm6GLKRDnY_jX-ShlwaJh2eztO6I4K-kMcdEZKqRcgg9MAbUTCRKqgN_gdfBV9sN-dWufwjU6X6rLnqlZdo445_OQOL2w60d62JWz2AQos8RAtCXdWWBc83r-d-OtI_vA8tWulVfHztutG8OvTdDWbvoJkWmFJufyTfn_Wh4X29PFZItoFYmrSw3TwteKzFe1sKVfKgijt0qG947Ih3aG4kXvz4_FyCh7EB10BX4wVjaN1KgP4EIgnb6qEyC5g0duCEekyUh98yXGZergtLKoi2NhQtPWdzPVVDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مرحله یک‌ هشتم نهایی جام جهانی 2026؛ پیروزی‌ارزشمند و البته نفسگیر سه شیرها مقابل مکزیک میزبان و صعود به ¼ نهایی رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/25058" target="_blank">📅 07:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25056">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JilntOZIPkafKbyY1qRgsfurkTVgPU-txfIXfmevVjjuvF7Y3DAqj1bUj1_s67zT7678B4P7M1xAFBhvUnnya9I9fMtVEHr4GwWQZtjm5IkY1A9uOnThZ29HgJMRx4rnPO9_IbSqzJikCr3KLvXxLNQFzUeKVqlJGiEoVsA8T1yEpbw8ihvA0QrHPYDPBPDAtVm0Ia3CyO39nTuLa4HlmxX9FKiqWVGtmxblBRHEJhIgxUm2xkRfs4czxD6NXDJhyqiu8GYkQVfLmBxqivdjWZgkCWvF5rHhmefTtc--kXQC0qcFj8rF6pRd9rfF9z_Z5Yi2vMkK9WvXpU1218_1Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kAyp3O75WIF2W9OY-RxIG0OdJnkqiGFDrSiiNO4kdBoDpue9Dni28MdbBoLy6uNdhU23_3Uq07xFAKeuNZlxeY2XXanHRTNcv0-1Sjzfo0Hned5dCAsdbwBmSNAwtyC_SvYt-hanfQjm5DkPyi0A7_rXRWis4No99nVT1V56sGZfqrFLEeAigGj-ADoP7WggdIGMZoCFPlCTCFLzdx-SZhWTOEJ-J_OY9jwr2MOxXkisUKhFNdCh9wq_R4K4JmkMqvNoAcM779DwwEhnoSK6FjaO450Od3l56xEFQh_fEIN6XBk8VZetjA2Mku5ChlO1oYrl86SnVgQS_JFVrMoDPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌هشتم‌ نهایی‌ جام‌جهانی؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
مکزیک؛ ساعت 03:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/25056" target="_blank">📅 07:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25055">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8FhMDGNIppXXRh9EUs7pKFrMXd_Ow2rka3t_lbv53n0OqcS1PW5sxdT-vWyMZg0l_iA2taUTYd2GkkPPaVZetHzJKuOS0aYYuWbu2-ACOxdSH139P4BO3gK6q40H8pTv3diG61QWvchhVv9c7opIu2zV4SDrjlKKW_r4HzSvJtx9luPiUzHQKIxMpVT6uSopkHc5K3PZW0J-obXAtoqt0RH3UbkCB6hXEyH5tUZak5zNAYqUe9WT-y61MYioGKoAyemJCXF5IcgmBc-8JuoKtB8mL6DLbFxWPs3PNtxeDYYDSBtXVHXaXywUkcS9ihcTkEfGWSO4XKjvUp6BPlJ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌ نهایی‌ جام‌جهانی؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
مکزیک؛ ساعت 03:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/25055" target="_blank">📅 02:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25053">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IUHZCEEuTW0y54NZtFKML_S9H-0XgFfvVTYJGEZrdP4OvpAZIC3Qq9DO2F4x1DS6wVqBI0UimRJOPG_At1aG6uWs5f2gNPQENmrkL7_ee3VUjEJ-JyT5LrLdRTVIB5MImLzCXCOS9REmNDOlx4NMaI8KHxS_8NmJgvT7kCW85lrOkHgLoH7ascdCdl_wP1cjX6Y8BC4fNz-3QJOgE_sET_DVS7DeG58LvXoDHCFPzKpStOrJ0qN4y4iaIv95yXL_K_T-Ioz3WxYCAzQxMVamLXk0UGItzrJYysRcb3GK9A8EsCoQU9QafIp15BfgVM7EVsssOrqeL4EicWk59Oos9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L5bkKBxa9P8FBZnMoEdUwwPwrBSDw_9aWr1jGAS_SW6VM3oiqdhsXSv5bmgpEeOosV8u4HWOyMtvtBfoTEFiGn8Gh2VvmMvgQG-iCa1S0MQefB27cl2eL85RHXGEaQp6CdFrvwh76Fwjn8U3RpVzJ__llK1_47FnLUwmFn4T2dFAli8ZjS88RGzhf8Et2uaBd8CK4rv_oIjGBj58SGa1eSlRvdATMrs_7jbyM0Lm2O0vpSR9kn3KpeWZH0PBW9nCEa6a58o4pSD70lOVLiO45Hq7kznSSql6LJ8sevD19o-k7zxn6gk8U_QV6GTenxxwY-VOcnkoKSSinTak0UFqkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛ از نبرد خانگی مکزیکی‌ها مقابل انگلیس باقضاوت علیرضا فغانی تا جدال فوق‌ العاده حساس و تماشایی یاران رونالدو برابر اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/25053" target="_blank">📅 02:25 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

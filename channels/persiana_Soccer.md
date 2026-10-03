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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 01:05:37</div>
<hr>

<div class="tg-post" id="msg-30942">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2df8fe53e9.mp4?token=TWapO7IBtaLCTCz52MgDnwbChLRh5Y7b2ebryr3VVPF-QpYUiPYEJtuNiljtFqifG32Cnia0BvS-qwtx2-tFsZweSBkxaggmPP6ALfATT10xm-9zCvZO8mbEjY1Hpn_CxxL4TdwYF0rdB9dCz5QqhBNS5tBdRDh-X8DNCDtIE6dA9rcRWAI5QbV6AsZiY0hMBl0T57yh8rVZ7Z1Vooy9h9guVhUF5LtbVQxNaC53LRE4CiyouCCnnsw0BmmcGXkzaVITqsqAn1xZmTRR3U4Ctpo4kQyGDPbBMG56kfAN4wqy1gR1ft3PUs4PYoWJ6SAeO_p3DPvqsR7Y6LMlQRLpowlVU3kBH5by2wQGqoGijtfIqqzBZBESN2WyBEFuU8VoCd4xOXlVmcb7WsU1TQPG7RnJCpFeXzHPTuTSGhGZY9r69VIynfNPvuEBqlyKC25ynuPFdPenuE_Nz0IgwiK8nHH1UJukSzhmSfHXsUvB_t_MGUQWLTZHp64dOpcADtxLkxrFTBuOuc9E5XCnssc8_b8VBAxoi-68nIUB2Suvwd-H4Ag1K0uTykf7f5nOcT7Vz4vucxX_cristFYfLx9d4PuLgtHs9XIzr2BNeCXzxQthx6RmfxXpgiZ73E5TJUCnvP7mYOXri5vIKedDRt-XiXNkRSo6AAkFb_zdLDR9W1M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2df8fe53e9.mp4?token=TWapO7IBtaLCTCz52MgDnwbChLRh5Y7b2ebryr3VVPF-QpYUiPYEJtuNiljtFqifG32Cnia0BvS-qwtx2-tFsZweSBkxaggmPP6ALfATT10xm-9zCvZO8mbEjY1Hpn_CxxL4TdwYF0rdB9dCz5QqhBNS5tBdRDh-X8DNCDtIE6dA9rcRWAI5QbV6AsZiY0hMBl0T57yh8rVZ7Z1Vooy9h9guVhUF5LtbVQxNaC53LRE4CiyouCCnnsw0BmmcGXkzaVITqsqAn1xZmTRR3U4Ctpo4kQyGDPbBMG56kfAN4wqy1gR1ft3PUs4PYoWJ6SAeO_p3DPvqsR7Y6LMlQRLpowlVU3kBH5by2wQGqoGijtfIqqzBZBESN2WyBEFuU8VoCd4xOXlVmcb7WsU1TQPG7RnJCpFeXzHPTuTSGhGZY9r69VIynfNPvuEBqlyKC25ynuPFdPenuE_Nz0IgwiK8nHH1UJukSzhmSfHXsUvB_t_MGUQWLTZHp64dOpcADtxLkxrFTBuOuc9E5XCnssc8_b8VBAxoi-68nIUB2Suvwd-H4Ag1K0uTykf7f5nOcT7Vz4vucxX_cristFYfLx9d4PuLgtHs9XIzr2BNeCXzxQthx6RmfxXpgiZ73E5TJUCnvP7mYOXri5vIKedDRt-XiXNkRSo6AAkFb_zdLDR9W1M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتایج نهایی و جدول رده بندی رقابت های لیگ برتر بانوان در پایان مسابقات هفته دوم رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/persiana_Soccer/30942" target="_blank">📅 00:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30941">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rG3r4EPMM_AwUoZ4mnkkKoxBB-p3c_en7jWZp9gYR2YgzcGQDsHPdX2ph9YbKa_Ss_93YQ7Dihpd-O0bRGGYLRsiBibEs2EfLuiW3ruVRjTdD0Zjp5oWgUYQH2vji-b506-sj7UanrIjTKT9wUJHFWYXJucyAYufrn-e15lb2XfqsPxAicKec3E4oDT22ylH3TVI-AsgXOtKyT5l_en0APavpSYg060J_UL4-o1mXGahn34L-3njxS2lTQcz-wa_YesQ-i2-ddJS-srq7qL6r1y-E3JpPM_WeI-2KEBX0db7qkzW_PGY4FkzTYK7F86_PmDXtDfTQTNUolVT64-ocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
درهفته‌‌سوم لیگ ملت‌های اروپا؛ لاروخا در شب درخشش‌لامین‌یامال و گلزنی‌رودری با نتیجه قاطعانه سه بر یک از سد تیم ملی جمهوری چک گذشت.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/persiana_Soccer/30941" target="_blank">📅 00:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30940">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‼️
وقتی‌اوس‌جواد لامین یامال را یامال سیبیلو خطاب کرد؛ جواد خیابانی: به خونه ام برگشتم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/30940" target="_blank">📅 00:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30939">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ov5rhXuDa0L-HkqK5f6-j8YB1koBcEBd4SayhPQkywZnV6Np338Tx5n4Ob81fQQp5gmZzz0Wo5PQt93_8WSg-d21Ogjxd6qBW1jO4ILUF7rKsRotxBN1qfwMpHrpjw5G_zdSk7L_SItMhAZD9_9IjiQrdniYfaK6p9ohHx9ARgZCW0XI1IyB-SW2m5eWJet5ONEz-1sKoU9umVcHUEPXIrKTt4G-fMB2Waynh4YX2JdPxua7DuvO3z8ShvT_W2kaiV3BuBy7uZ9yVhMIFwjpomssh0IIGZPp3MQnvJFmEK6lFQ58MBkv_5FCrHPeWnvWIGGIOJ-vYrb9oqZ8uPApjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ نشریه العربی امارات: رضا غندی پور و مهدی قایدی دو ستاره جوان ایرانی شباب الاهلی و النصر از شرایط خود در تیم‌هاشون راضی نیستند و به فکر جدایی از تیم‌هاشون در نیم فصل هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/persiana_Soccer/30939" target="_blank">📅 00:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30938">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5SiukSwaM6EN8dAD9kWg_Oe7JFaUMqMGZLVc5qoS94sp-e4X8Qexsv9-RWZrT_Dhz4l7b8qYToUjxn8SK-eaQQ8QdMATVsWVYmiHUt6UevkwrudAEG3DxVSYuF9o0DG_dzOwrHMGFovnF-4jj7pBnaS11KnTU8mgVUXZ2kQMGKluGB41DHbSxRw1REzAU1MxwXbwayG7KtdNXUOV_Dq6gSbnCP_WciPPhAsdrZtipKS1j4xQCS17u-ynCFy2JBnnY1KAzdvHWRUAYaoShO7FVbsuKUoXEY5EvnEaibVeuJHJrg65-B73KCQtzp952g9csRt7Qf3QpL_bDAVVhR4pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا از نزدیکان مهدی‌قایدی؛باشگاه‌النصر در روزهای گذشته قصد داشته که قرار داد این بازیکن رو تا سال 2029 تمدید کنه که قایدی از طریق مدیر برنامه های ایرانی خود به این درخواست‌پاسخ منفی داده است. قرارداد فعلی قایدی با النصر…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/30938" target="_blank">📅 23:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30937">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwzJIByrqqMInfxq6AbsbowRAI25uu4X5EmLE6ZYtMBXZ751bGuDpjOa1-fwi_LCBVlmpGgkRe-t7lPlpJdKAqo7L_4-YvFDkAGUBmWv0irb2sEs065hNCyE9ev9dHL-B96IBfwQzRBRLDOw7eMPOsQNwJRpmrj7TLygXiXTkrCV7I_Q3HnYQY-_M5n5hNxkNpFok4hiapHoY2OvxZLkCB6STLfxqufcC2dMHjeuTojMtKdaUil0thhm5lHeDn2cSCJJEQOhE3T3ylKD2fCYkap_0akwO2eNsvLknFKCiE2GRUnLgwUHJX84NPx4ujYuBIHVoJTIiF1Qr-XrXMrjWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
درهفته‌سوم‌لیگ‌ملت‌های اروپا؛ شاگردان توماس توخل درشب‌درخشش هری‌کین و جود بلینگهام آتش بازی به پا کردند و با گل کل یاران مودریچ رو بردند.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/30937" target="_blank">📅 23:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30936">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmBBODg5l7Mfb83tfNzlyACQakXiFB7GT0eLoUk8nyuLwdnzGzmlDkoJH-RkIELbc98yEBNMVMRivAwwFDDR1IRl030wNtkYt5EyMM9pGWtsaxsDEXqgv1JDOsqTECnFdkuFUboxaQf-LV-t__15-xUftY_hJtGniEXeLRzgq12gQT_KA78y0OksVBu8mBjfShHld02i6atqQh63_QF6XSvYzpYZmwQKzoEwdYIdzLaTW6ideGa8QVgAd0_dPxO3sBetew_WIb14ksVFpr8lbKRsWHhbpWosTtvormee7AvvlGVbD8zTCUlGmUC6BGTiD0Hq7He79knBzfj7AQwNVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر مارک کوکوریا از خودش خوشحالتره بابت پیوستن شوهرش‌به‌رئال و تو اینستاگرامش عکس‌های قدیمیشوشیرکرده و نوشته:«ازبچگی‌رویای‌این رنگ‌ها رو داشتم و امروز زندگی‌این‌هدیه رو بهم داده که این لحظه رو کنار تو تجربه‌کنم. رویایی که همیشه وجود داشت به واقعیت تبدیل…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/30936" target="_blank">📅 23:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30934">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f069d8eb.mp4?token=Nfe8bhf8BAAJI1beyn_CMg1cZc96kVFO1LT3mMotOgpP56RLXY7QQwA7gQc_nL5rgGiv5zOxF7mWioRw3oKdCigQgjOreCPQ2b06S7D9W3JSPOV_IaBJXgJ-VzbDIkeC0BLgK6diCRdRl5RVmIfqU8hk2gTbYcGp21q7OZKCcDqexED31AUB76kgYp7ogLqEw9d6D2e99vwPGE1kcrHS1sM6fYVmJ3Bn8tOWcoJvDMiI8uXK4bacSxXci9lPRQFfxSZVL8Zsf8a473X8i4PRGw60n8BAG0nh5yR_p4_UFwZjGsWeF40LdL8J0jZR4Hl7QjIL4wYBcTnCJ-fPGsM0eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f069d8eb.mp4?token=Nfe8bhf8BAAJI1beyn_CMg1cZc96kVFO1LT3mMotOgpP56RLXY7QQwA7gQc_nL5rgGiv5zOxF7mWioRw3oKdCigQgjOreCPQ2b06S7D9W3JSPOV_IaBJXgJ-VzbDIkeC0BLgK6diCRdRl5RVmIfqU8hk2gTbYcGp21q7OZKCcDqexED31AUB76kgYp7ogLqEw9d6D2e99vwPGE1kcrHS1sM6fYVmJ3Bn8tOWcoJvDMiI8uXK4bacSxXci9lPRQFfxSZVL8Zsf8a473X8i4PRGw60n8BAG0nh5yR_p4_UFwZjGsWeF40LdL8J0jZR4Hl7QjIL4wYBcTnCJ-fPGsM0eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جواد خیابانی که قبل‌شروع جام‌جهانی بازنشسته شده بود و از صداوسیما خدافظی کرده بود امشب بار دیگر بعنوان مجری به شبکه ورزش بازگشت.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/30934" target="_blank">📅 22:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30933">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8329d169bd.mp4?token=Fs6EIxHxh_LtViJ_aTedZbWN8oTIp5c1Z4hfDa4Kxmq3Z-BstzeLolS6DKxHIQVIQT1hhG4E2tTxmzjh2yh1kbh65tvy7GVghAMq5eYt6A7JdGBH1OvIn5HprhzoPGtJaR6DaoDgLLASj8yxQtxdffQU6UdewIK8E22Vloi24qVC-8FUQi2ah4MGoQ9YeEXX_dw8TVpZNwwPTxIOmykqVEorR6VhklAfSQuZXd1bs4hF2Ju2zidyPNo4MBY4qa-kCheezlLjB1j8DOnZAOVyEmaaoABSqeCVn9uSq3iMeVo_2ag3QVEbW1QeBp7X6gUjBWuw2qOrVnb02Jc_ZngzaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8329d169bd.mp4?token=Fs6EIxHxh_LtViJ_aTedZbWN8oTIp5c1Z4hfDa4Kxmq3Z-BstzeLolS6DKxHIQVIQT1hhG4E2tTxmzjh2yh1kbh65tvy7GVghAMq5eYt6A7JdGBH1OvIn5HprhzoPGtJaR6DaoDgLLASj8yxQtxdffQU6UdewIK8E22Vloi24qVC-8FUQi2ah4MGoQ9YeEXX_dw8TVpZNwwPTxIOmykqVEorR6VhklAfSQuZXd1bs4hF2Ju2zidyPNo4MBY4qa-kCheezlLjB1j8DOnZAOVyEmaaoABSqeCVn9uSq3iMeVo_2ag3QVEbW1QeBp7X6gUjBWuw2qOrVnb02Jc_ZngzaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
در آستانه شروع رقابت‌های جام جهانی 2026؛ جواد خیابانی رسما از صداوسیما خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/30933" target="_blank">📅 22:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30932">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vguPZy5IuYNo3Q7Y3LDrHhQGU5AKpQQZCINrozOBM7UVGMhyYIoI3jIQbpVazyBgH3Z5NlNDU8J529Wik9eHrdIXe4FTSq3qxW_iySU3AOT3977Myo5vHi0OisdX-A4R54GfLwvwuoWf7l1OW5__tkobrIR7z8JDoANd9aPx09WLj8g11Hh2wp3fS-KYSrphj9ZOtpImkdaugOmLy-R947NilBK0nx0JetCfiTlWOn2Kbl8kg_cCGrrrcPZ9_ulaUfeX69DPchhrI1rvF63r74QexeL8PaA2QBvjuPNvoyCiu_jq-zQaeAQl0lulx3wYSMnZVlYRKOKMqxaWf1R2sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
ولی کریس رونالدو با خدافظی از تیم پرتغال درس خیلی خوبی به‌ما هم داد؛ جایی که نخواستنت نمان؛ حتی اگر تمام خواستنت هم همان جا باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/30932" target="_blank">📅 22:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30931">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇧🇷
🇧🇷
تیم‌ملی برزیل در سومین بازی دوستانه خود درفیفادی ساعتی قبل بانتیجه‌پرگل چهار بر صفر هند رو شکست داد. یه‌زمانی‌همه میگفتن که هند هم مگه فوتبال داره اما حالا فوق ستاره‌ها دنیا این تیم رو در فیفادی انتخاب میکنند. اینور هم حتی تیم گینه بی صحاب هم حاضر نیست…</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/30931" target="_blank">📅 21:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30930">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyFSJu2grsxegrDploQKLirqWarQEy77VQmXUaDfb1kDaGvgBvPhBUwfwcH0j3TOJmf-cd5-LenL3K0NAH-Zfd-5xZwHTiTO7AQWD8d8u6E3xTdQlsZool7uSct7V8UFgWYNsQZF-4pr6wt6IE4BRuBgYtoq6NNsx7xjK6_HL-lxJ7snd9LVuHyi13xEjvIVXHY_1AnfYnJR0nK96dt0a11jY7n3h2poZYEIEuJ-wj9itPi--qYyf_Aci14eBS1pp1oah93BDTrRVOzha6dIFp6MZVkRDkeZZGP-cPTSv416M2ePOGmSpiTJjfwUPVplb31W_rVQTT_Q57nAk4Dalw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خبرگزاری‌تابناک:گلشیفته‌فراهانی‌بازیگر سابق به زودی برمیگرده ایران‌وکارای اداریش هم انجام شده.
‼️
درروزهای‌گذشته‌آهنگساز بیژن مرتضوی به ایران بازگشته بود و رسانه‌هامدعی‌شدن که شادمهر عقیلی و معین نیز بزودی به ایران باز خواهند گشت.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/30930" target="_blank">📅 21:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30928">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SSp9l6ktlurAldlk9-RXf-M_RGmBnbJ5VfvN85yCvKov89_FndmtexnFXjKyIP8-8_COJQFWdWAY_0SfXex2dhHim-1nwElLwCoHLsDqXHBe4yc0NVVUngBve-zozI4namUzCHuLnBB3DBrGn8-_lXCSebjAV8lwqkURVd_R30eKxPPoF37ZAmBn6Wwqp4P7rFGHW3g8ekAxAhuq46v6jD8ZvL5UGfQFlGNn1nvhVA2lj1jWAZMYO5V0L1ShPFAHqhrwu2W5v8giKvXj0wpzc9FrhjubeXsOLxRhbGhakOtVyFPlWzuEv2kifcJsmF26rRBkEllZZNZtx1U3XArPBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P89Amd-70BI5B8wRDKqV3XzqAo3ZbPUHBlctUSXrLG7i_TK_nk9BJP1zloTDqbwUyeFowymhk8HVJD1S7eHPi6_OVHJylZCdUmxAzLy_L5zODWC4G9Ow9MHCTcZ5iEsFkdj-o92ASMQHt7Qg1bxyQLeV6oyXEYMTcz9DtqUAAulRt5_XUT-dJDnTMaEPxiDFVzQfk--rGS2cMZ9tRwWehVw9cPv2EQKiPwy9S0v0vYxqmbtI-iDumkHa8XTSFMug3LO_OMD4tml1FVaRTKnfkcB5P5INaBfHYUJVGQu8hRDRO_iZKAtZtM4-CVNvWuXC_dfeBzmPgg62NatAjPJZhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
خبرنگار شبکه اسپورت اسپانیا و هانده ارچل بازیگر معروف ترکیه و فن شدید منچستریونایند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/30928" target="_blank">📅 21:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30927">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/30927" target="_blank">📅 20:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30926">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/30926" target="_blank">📅 20:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30925">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز؛ رویارویی دوباره انگلیس و کرواسی پس از تقابل جذاب جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/30925" target="_blank">📅 20:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30924">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORvVWx51ubthJSkE3Ic0emhjjhcFV5nZGZnQH3amke8wwc1DLEq1hAhqnFslS0DzTzNDMRF5DtXVzmU_DK4EvmN0zbAqb6DFKBSlXx6UmTR4Mr2PQtIT7RucDSrlDN6TehhIEHS-MPjuy0DS6R4b1IeUVBiE2ZgTv4FphTlK4y_jKlY7W6c8U6Yz5SOYXbbB-Fb5x1QZQSOIXxU0qYUZDNL87qqUuod8A9-5rNubv0qtYxu98osxHvhr12wB96qaM55nD7mSK601zRQnm9CGZAyWz1ouZUZ0ZE2TD9EDuSSdvQKs1zzx8aTwZVlGL77nhv1BTQ_dvkerqd-RPeS6IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برندگان مدال طلا، نقره و برنز فوتبال بازی‌ های آسیایی در 20 سال‌اخیر؛ ناکامی مطلق امید ایران!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/30924" target="_blank">📅 20:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30923">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_0Tvv2EEBfferDoubDjDJiZ5lqwiSQCp3xOyRK1h5dlKzUr_Roz2AEJ_fNr-iEymn-8yS7h0R8DG4X-ZkJhUbFl2-omGY7iZzT1ZxpfFBmcj5drJ_6SkdZTJYchI1FUfTpyoYGeqz3ZWD_DNclOa_dEMLqf5VoFMniB5-rfqKM-3CCmllhrlW9MA2K9yydxCh9UWCPik2YtYENSn8IHFinAhHx4Wl_iQwKDkosLJsDM0tll1YOXlBqNlaFwFvHpuZLkUxFpODFFqcJonkzTOVJsWwQJaj0BFFo_5F2_l_O38S5d6N8wjOCwlX73ZbiSmWyVrBf52_ThR0WRyoqsag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ضربه بزرگ فیفادی به تارتار؛ علاوه بر دانیال ایری،محمدحسین کنعانی زادگان و علی علیپور دو کاپیتان‌اول و دوم پرسپولیس به دلیل مصدومیت به احتمال‌زیاد بازی با صنعت‌نفت‌رو از دست میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/30923" target="_blank">📅 19:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30922">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggtQzkOn0kv1u7NnYBTTxqkrWeDNkH8Rl6OG2KoOTW84ERth-ERt8Bd-notL1lswBeEPvAuUpoSaPjLtTnNu2kVqLMUcnwUZChbRNQehr_7iTLJc22wn95-ME1ozgIxvJCe-w3qqAVvoknZxGh-RU6Kplf_tc91kKgGIjtt_P7DvrPsRd9QVxo_zcsrVoyuNaFtGXjIskvIObNSDbFbC00xSLmJ4mjmPL83paulOTXzdq5mfMTDkpqeui1cQjUwHnNYjC28FJbRYA4dMJhHzCoPo_y_iFwAMJaBiGkOrt7X6cVW_yqFlrftY1UGs4931NNwI-11TqntPnRwPGaRrZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه افتخارات کریس رونالدو
🆚
لیونل مسی دو اسطوره تاریخ فوتبال در کل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/30922" target="_blank">📅 19:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30920">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RGU3fLx2jZzU2B5sYK4hMbJCnTGljNAtddJMnPrikhpyJ8P6g0fKzGm8nFF-28wU1ms0QuMZ6JSoc_w-i6PXU3_be1SGHDv--SqwPWCDPM3SjA-8cjZBQVYbXex48Y_T3ZxieduvqMrVg547TBda_CtzzX_Wjy2Di-jTjzOc3GqWVWs-7UOJzhptuJP7w-0u7lNvfCrJewQo_OLCs7pYAIIybWbNDpzGp0fSVGlG6V--sOiv0in_JWC-cpYaiMRBn15YBpic4dKbwZY9KpTt-MLqzGYfMw7sWdG8Uh2_hvCLW4-YmrbwdGAu9frEgfcgdzveYTY6Qxe5Fy-sOf_z1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ueEBMx1bTehqLms7Jjrq3lrdNoq4H7u_Mgozd-PaAUDkAlEO5XnpVzU6G-ax2T-V0S6fYTNc_hpGcZ_7-vcWAshNx0iswnTwQsjuWPs812kJ375T2xc8Q2FqPdjuTqjLgh2bsqFkoRyAOzmk0h7wuaxPHxDb3kXtgz3BdwOlxSFkeTCFt7zgKVrJNUXG7palmt4hNnlYFYM0ToIfAMm1yA-TT0kLP2Xjbf1uDYM1uYNur2vAUylD7wVTS5WXUUBn4Y3SMc-OOUyb4jD7oi5ZKp7Z64-jKgsMPMECqZwzMfbThWd7mLxMNuCXMr7dMIIeQ2QTSlRuH4q7yEvTpmKFWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشک و فیزیوتراپیست تیم‌ملی‌بانوان‌ایران؛ روز فیزیوتراپی رو هم به‌همه‌فیزیوتراپ عزیز تبریک میگیم که‌مشکل‌بازیکنان‌روسریع‌برطرف میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/30920" target="_blank">📅 18:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30919">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcZKhSMZp-Zyk6bdRBVFFKw5NDex2ABt5YW8bZFK5Lr0wlJ_hETvJRQj5y-RCzhIAT_YAOqRdLf0bUx4lXjQ7JeZDrBJpLWFit5-RFJNVEepcujn2aSJgX6b8veD8s66K1GbW_Ehvhs_bQkvEd31Ca4GsqCs4bblelm8_ax9a2050bjBRyMBRuiSt4FGszGHJu-ubBeqal6H7pSR1CknRJBYuBUQ_oVh4MuSqPKzrN7ddxOkXSTZj1JPcic2KBvjuYlSX9lP9dKvx3xC-UPdtsQ85G5VUphvhhwasfcc8GHKqTZkr6rp9WUk9KX9owMAU19a5HCs_LIAHSrRPG7Prg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
عملکرد خیره‌کننده و فوق العاده لیونل مسی در دو نیمه دوران حرفه‌ای خود در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/30919" target="_blank">📅 18:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30918">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSLvWB4jG3tUmvG2I8mogyKPtF1jIGk_tFEkcpGCs8f64lrF54tjRV3an60P9f73k_Wnema807CE2U4mW4P4vWOdTLjSLXJ3kgH0ndAIrHpzUey8H_V2ZfZzFncOa9IfZ-Hs80uJsu0s8WWftnpQansIqKeoMeUkB-Cc0XTVg9UjBNxLn3bW0Cfen9JFe39Oq2Q_FzUz7xpa1_OP6dc922w1jBRLkjQ3QLoPz7MHHnS5tk-VibL351MR37tw1Z4dFChin6a8_tUeILq4-UNRQLropjJroMgdZg1XtV1FfWov47aX999KKYbhiy6Z6EqKrrQKt8Sx7ngbueDfFK8TWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم ملی کره جنوبی در فینال مسابقات فوتبال بازی‌های آسیایی ناگویا یک بر صفر ژاپن رو شکست دادند و قهرمان این‌دوره از رقابت‌ها شد. دولت کره بازیکنان رو بابت قهرمانی از خدمت معاف کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/30918" target="_blank">📅 18:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30917">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/30917" target="_blank">📅 18:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30916">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aizJZ5_fDjI-fG7Xfv8LQP5vKRobjVSX2zJ-UDM7RplVEy2zmUimnDQvaxIpBblv63GSby_OKurGt6H35FC96ImxqGjQMrD_okFjLiBJLHGVxOGxoMpO6swc7aP-sFMDxRXoBF_P8ajhR11OYeCutldFU-G4ZB1dEbSyE0YbR-F45i3DyoD9M5wj36nVYlu2KVUFVozG3ftOqCMNlLggn1TI9CcaOlFxLKHC5XTnYMXfZwGmvNkQxxL_3tW8_WSAGmWnlhvP7pHbaCI_-4tyuRWGhCRmAWNOYgzk1O7dbJiNaITw9A1r-7pthYAcYWGQe2FnWAwWH0m2LEwxMpao1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
فیفا باشگاه کایسری اسپور رو به دلیل فسخ قرارداد یکطرفه علی کریمی محکوم به پرداخت یک میلیون یورو به هافبک ایرانی سابق خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/30916" target="_blank">📅 18:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30915">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-6cI5rvw_0rnSinnoIOK_lH7ksa450nkTVumOHt8_ulOlAnpwTaUT18VmLzjK-TZLZbOeTo-yyH5d1S4leGdMXOe9mtcLUqaJ_C-0sD8Hau4JCBCXFTu8fMr6yF_2A-OHMWlQ7urOee6FEKv1aUy0KxfrkyGOtEIMs1m4MX2WDU9lIwktLrK4NVjuVsqo-Z-O2uxHFaTUiLaz4DXJ7HQrr22GPrkMaL7p3CtzuyftkVwV-3TwC6HuCruZ618bMWOnkeeCCo1clFtIQLOKH-rOy074L3nR8_9tE6wLTa5SqN5sMZW8_QybXxhl_Tq9OxAET4dj9WlKMTOmMxmonk1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ رائول آسنسیو مدافع رئال مادرید بدلیل مصدومیت تمام مسابقات رئال مادرید در سال 2026 رو از دست داد و از ابتدای سال 2027 به تمرینات گروهی شاگردان ژوزه مورینیو باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/30915" target="_blank">📅 18:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30914">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFI3Y7x97vKNRLd9IPA0FXc8R_VrdJ99JCL-3eCnl1iwrJRflfw-KKq_hpuqyDmNy2B1gDpBdmr0T78tehxff_1ipMHZXA4ZtajL6mYwuI2b7Jb8q_8sttBWKGm5mC95z75fwupXlfmuiqQcudngsMgsIumN6YrgHNgD4fzDPxo1pHhwS69SIbBwd5zqKjLE3XeqHV2zWDA2gLlQ4-Bb6WlWMwItH8IZULRiM2jz0cScLwr7m20mLLOkqvFrs1qoYcJ9N6lqCPyvWntfNmSVmWjnG0Rpfkr-6Dx2QEIvI7SdSpWcbE0AbuxhnfTpTh5D9X4xVlf73XqasMEGyxTCOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دنیس اکرت مهاجم 28 ساله تیم ملی ایران از طریق مدیر برنامه‌ ایرانی خود علاقه‌اش رو برای عقدقرارداد با استقلال در نیم فصل اعلام کرده و درصورت تاییدیه سهراب بختیاری‌زاده احتمال آبی پوش شدن این مهاجم ایرانی الاصل بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/30914" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30913">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETI8vOQ-R7fA-_lqCPr0plthxD6mh8nblXfdGue19gQ6iwTrV2vvja75hIqoQGZLT80ijFP4CUyRzlFTlTmdFKr48TMaVZqfzPy3OcMZE66sm_3NWllMp4ZWbH2FRr_9nPTC6j55smCZFNhpy7lG957U7kNHy_e54iSk8w1OW9BkqhJwCccg2ZHINa1G6pAfs6wgue-3WaflkaZO2PinK8FXj2OH-DdukFS3G4ezhlN6k93YUd__xL7OJTa71oNeqdMxECP-vh7DtlNw3upQROA3yn3CT5yKV-FzRPTafZ5nqs0kyq67Vyh271_ud9j_viaWRFetEobsVDZhbLfLnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه فلش بزنیم به این صحبت‌های تلخ ابوطالب حسینی درخصوص قیمت دلار در آذر 1404 یعنی کمتر از یکسال پیش + دیس به امیر مهدی ژوله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/30913" target="_blank">📅 17:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30912">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIShV4mRId2BxOcr72SGEB9rHcsQEf6_aSq5QhyHSYkpaS8La2HtISdiXgGgu2AuJGj4-qCeV6lMN7Yo-on9KFUCS6cU6YnmL_2-KysW2h2zZ6PZsogHOl3vGTbbcFljBdo8C28w431Fs_pY0dh0UyNHYLty-ZLkzHs2ISnk9vYidn9wlwD0Rz69uQp5LYFiw-jDSssXsvpo6WH9tKsqRADI_gmcMEF2xLtfzmmQF91g7pkKuqXsg7sYEm7X1OT66uezITgWXmwD495zwAROYfvhPYIQydpo04gqzzT7BDn5qq4VefFbduP3HI6yWI8vpdpCF5dmF_BqS11axtGYXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
هر ۳ جام‌جهانی‌که مسی فینالیست شده تو گل، پاس‌گل، دریبل، خلق‌موقعیت و پاس کلیدی نفر اول تیمش بوده.‌ توتاریخ فوتبال حتی یک بارش رو هم کسی نتونسته انجام بده چه برسه به سه بار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/30912" target="_blank">📅 17:01 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30911">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfXsLfL7swFE1mVgn08Gf4pNkTzhjOgvPIIgDlDtE-KJTa1RyIqT6yTussmEcF7z7ni_juMqd9xYqlekYhiC0DOc-VSKR5lM5UiXRy5iKTA5k3tSsIIoRiC6lkpmo8KGF15z3ifA-7xN9FoAHTQpOFzR_GBshALON7sbQdtdid1P6q1HtZbf7pHyYIiVmYfUjTvhz5OsZVtKQlapl3ieArdUy9FvxzMYgzG4TFBWQb4MCEGx-gDuxoIMt72crayDsEV9XZGJVRV9J8DQTd20W5pTcmfG3JuaCq1cGfz753pkJZZtZfAk0Q-KE7was56veIJptXLizoEyK7Pxv7wYSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
انتقام قهرمانی آسیایی از ژاپن گرفته شد! تیم ملی والیبال ایران امروز بابرتری سه بر یک مقابل تیم ملی ژاپن قهرمان بازی‌های آسیا شد و نوزدهمین مدال طلای کاروان ایران روبدست آوردند. البته گفتی است ژاپن با تیم دوم خود به این مسابقات اومده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/30911" target="_blank">📅 16:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30910">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/30910" target="_blank">📅 16:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30909">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7722f37ae4.mp4?token=WmxDbSJLq1d1tn9ixX9J7DjyESfXT-QWXrVhymYb-IYazvfoIkV_-CfghAxeDe7olGYiAOV9b4Uk3JnAZV1exPazJHCNa3m7McXUasX-3PNz-Ks3FJP6VI8uRYEBPF_LBCDMeQaqXphfs-DAExs4A0AyKNN-BrLB24n70pnwsqgS_D5MqhDuvO0AeEMM89Zd0y0F7rWzsKZk1gVXGWDX3jin2NpcZabpb6BfpxXIXoNW_LC7UEFFdB2v0PjPfJHhhB7I_JDdcdDuU-GNet_HIMpQyL-bJ8HspYhAq82rpxv_17F13KsesQRfK77Sz_83s9jgcqC8CTkqvAmEnEO0HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7722f37ae4.mp4?token=WmxDbSJLq1d1tn9ixX9J7DjyESfXT-QWXrVhymYb-IYazvfoIkV_-CfghAxeDe7olGYiAOV9b4Uk3JnAZV1exPazJHCNa3m7McXUasX-3PNz-Ks3FJP6VI8uRYEBPF_LBCDMeQaqXphfs-DAExs4A0AyKNN-BrLB24n70pnwsqgS_D5MqhDuvO0AeEMM89Zd0y0F7rWzsKZk1gVXGWDX3jin2NpcZabpb6BfpxXIXoNW_LC7UEFFdB2v0PjPfJHhhB7I_JDdcdDuU-GNet_HIMpQyL-bJ8HspYhAq82rpxv_17F13KsesQRfK77Sz_83s9jgcqC8CTkqvAmEnEO0HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
فینال‌قهرمانی‌آسیا؛ شاگردان روبرتو پیاتزا سه بر صفر از ژاپن شکست خوردند و قهرمانی ارزشمند این رقابت‌هارو و کسب سهمیه المپیک رو از دست دادند. یه زمانی همین ژاپن آرزوش بود یه ست از ما ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/30909" target="_blank">📅 15:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30908">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5YK9UsCTHIXfV70VqYNgvnXybzf2CRosT7JzESqerVEG2Qbdzwi9Jm4XijLKFR2IBmRCXgNR9CVCZwCo2DZryppctnaPGlICoq2xxO9IKjsIPQ865kHq90HuhcytS34uQ5_mncclfwrgSISB7SzciNA3_Cmh8uzAkfUcuX4MobNqc90Kt-CvxUuLlVZBaL4QmdwXiKlTaT6Xdo4uducoz-fcbF5un8jxQ3eNTt4TKu6FNaKFrvfCropQwASpEL84P7RHWtKfR59tVy3tgc0Y2aWwymhhw8Q5iSl9MTP0ng8e89-VnzthkOBmJfv_M296zzPVSvMg6otAx1LOtKU0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باصلاحدید سهراب بختیاری‌زاده سرمربی تیم استقلال؛عماد زارعی وینگرچپ 18ساله‌آکادمی آبی‌ها به تیم بزرگسالان پیوست و در فصل جدید با شماره 99 برای تیم استقلال به میدان خواهد رفت.‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/30908" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30907">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhBdqkxEEktanFJLiQOlnWWHRL_Yh3PFj0h8YorS8_4AvGkW9DaojxG9QWNmutkoEggyCpR35qnno0HGm1LfVEM7u4vONDiq0d_1dEn8tvJ0i-26iPa-Agm8YfHeUJoJoMGe5yfklEIW-GncVmNOvZlmGlKMMKWWx5MVqlMTgCs3d9zreew57aoTvCWUvnVdaw0unpEiMmBp2y2OAHjAfXk2vr3PTfyagNL78ikI3Y1Z1Upa-jKvuYBGaD5FXWvujHIRes_c-xEAzDSbPMhTjtTvWq3Lx9u_lz9QndGXV-A3UjbrAoOAFhaavmCCtXUVi9YPi5T2mIo4FGQT_vVVew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درفوق‌العاده‌بودن رابرت لواندوفسکی همین بس که تعداد گل‌های ملی‌اش از تعداد گل های ملی کریم بنزما، لوئیزسوارز، نیمارجونیور و هری کین بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/30907" target="_blank">📅 15:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30906">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyLmh0U6-uQBQMRbOBXg8_fQu602c564UaJEJpHtmXCLPIxifMM7RDhDcQ7-boGvvfiDBrrexXyuyVuKmNKgOy-gG3Dz15jy7cgxwxWMx8UaDqKnG-j8ex5ZkuHGIyUFpbsMH3Jeosj1NloESzsdrZkO_K1PXuGmquiHmrHE96YZ-u1q8VUlzfJZ-bXXiE8lFzA4QJ9FatpNjvz_ZdWdGQD95c_ZobAQPhG-VpYiCV6PTz_earQRrXT4zKROhaLm3ViAk98tJIT8abH4V7TSaO0t6aNnIxpYF7w8FQWvbWvzE7LADzu2QvLtYuxX74BiGL4zhMVfMbrH7svSkyQ3tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#تکمیلی؛ 10 گلزن برتر تاریخ مسابقات ملی؛ کریس‌رونالدو و لئومسی اول و دوم، علی‌آقا سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/30906" target="_blank">📅 15:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30905">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/30905" target="_blank">📅 14:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30903">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMuol1bzq4Dbbmr6Cf6K-nDJV8MwmIYFduZm9q8wJQcTXJoUSJe_UEr49alWrTbAJ-ftHixdhVn8F4nkyXGy7nb7Jg9figAaCV8nYZWNNn6r4bt_8jHacqPM32dxMpF_DqXf4MAQHBuBCddoQ-BM_VuBy10KodqfVGGBoWNNjczyF9GQ6ILkdIkl4pUhcY3msZlX7qd5GpSuuw30A6NF7jmUhjGTsFVbwapTDVLae0hhc2T980vnX--enU_kHSrMH-bqiKOZUCQITC1VDjFAOg0fLgFbjdTexcfTkTbVf4_vAlWhBcZnqkeAj4IrmgCszzgCmF5f0musLgx21dz_Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌‌های خارجی معتبر پنج گلزن تاریخ رقابت‌ های ملی رو اعلام کرده‌اند که علی آقا دایی اسطوره فوتبال ایران در رتبه‌سوم این لیست قرار داره و تنها کریس رونالدو و لئو مسی بالاتر از او قرار گرفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30903" target="_blank">📅 14:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30902">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPoh6nTTcNumjx6gFsdG5o64mwTX55ZisSyYQaGisPrhKHn26BGXTtyt68mRE0jWo2aV0fPnqgcN6i9wIleI2IhFZDk4NXRBbhwPj33eyPlfdLv8nQMyqdAoXBvvWfP9iTb_DSyMS51MnqKIrSdD0-UwXDn51HPS5A0jvO37RyVPMNNgc4fsRnHoGq1tfY8XNRmHCByEhMH4L6gaDmMroYXIvGlp8325wTK6lu9bRglhVSazSvUTyojhONBhibiqhmtClMXy4jMBABwKybTmbJpfkcMK1eY3EZad8q8rGxcaR4sbbOUyXMP3St23hhaXon61lD237H7EDWewqLDAjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طلای آرین پایان تکواندو ایران در ناگویا؛ سلیمی در فینال وزن 80+ کیلوگرم تکواندو بازی‌‌های آسیایی ناگویا طی‌دو راندمقابل‌مارات ماولونوف از ازبکستان به پیروزی رسید و مدال طلا را بر گردن آویخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30902" target="_blank">📅 13:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30901">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJGqLZEmXZiivu6GeygknTzuxLnTdMzb-YVYS7bDaoNfT4RLX2b7ndz0U8c8xkwoS6nLAStdqFEw0tGJV3_gNTQFbHR8pFPWljGNsvV8TlVcVefgrqpVvHMKY5zTPfOoSmFZoNvscBdQRsVk44WSOQyzacrONI3BnW4xLgOIQujU_cUawaXhWnplUtJklXFFilFdrw0qkdeAZZmv8vT62XzqeawcSmGhJqOfYTlAJD1y7T9UBMpCB5NhPcWCNhDsvhv7TubdDLuCrTvoZ1fproMk2vVB4MZAZhiwbxjJxeCZJMCB6kc2Ujq-aSWolp5ucMCcTfcKFeXe6V7RtjxHjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون فوتبال سرمربیگری تیم ملی امید رو به افشین قطبی سرمربی سابق پرسپولیس و فولاد خوزستان پیشنهاد داده و درصورت موافقت قطبی ایشان بعدِ سال‌ها دوباره به ایران باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30901" target="_blank">📅 13:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30900">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlN4spphox9hAYhKjEldzyuSH_XkmHtTbP7ywZr2nWosgXQk4tS6FauBVP-WBrutYVU8jjyUbG08sHYDiOMAiuuWaeMBiX8EpEnbsGaFpxOYolirNjgXnK8TivuRkibpAxlqfXmFCNrVoJAq5rNvJI8kmf8m6w0bfM4eZ_7BBV6LbSvbPkZMR-IbM0lxLmL0QdcuCs9vrdq_meMuVE1NJsHHq5K1erGSoGkXKuLyYxrY3IyLf7dNCwzQLpY-GrXndcMM5YO1qpII3415xXXtDRraCIAETJqe177IsKIFc5JNS8hJc_cErdYdcRG23JWAWtcTt0rhAYB8QbiRKQsY9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ قیمت‌پلی‌استیشن‌پنج پرو تو دیجیکالا به 345 میلیون تومن ناقابل رسید. خرید یه کنسول بازی هم برای خیلی از جوانان ایرانی آرزو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30900" target="_blank">📅 12:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30899">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8WGeZrgzDYKrHw40KJYqjU_hY161DGuyhjPob1s8RSwuzkibZ7GmUktbhyzD0LH5M3pLnGUWGSFimmxKDtRbreDb89aLnmwIk7d9nhij8WUQ633Z_jG4vSmXTfpd3LUdeWLi8QfBu73zfF83l-zJYGdCZEpJ6flry1-na-915UgInZN5neefcyr8YBfI87icmcWOuqfgKpsik_5y13xcm0tXQs18wk_ij71RrM3fcOHtG83fZfAOyafGKCy4MTQBAPBjPeFGEp-xTCkvMwokIvYWYvMoQuznnGxgfAGw1BYtQU1_OHBDV_Uw-3sgxyiwiM9mIA5g1OXYdSrrHqJJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
گل خاطره انگیز و تماشایی زلاتان ابراهیمووویچ ستاره سابق تیم ملی سوئد به ایتالیا در یورو 2004
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30899" target="_blank">📅 12:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30897">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
حسین ابرقویی نژاد بازیکن جدید پرسپولیس: باعث‌افتخارم‌است که هم در لیست کارتال بودم و هم هاشمیان. تلاش میکنم بهترین عماکردم را نشان دهد.
🔴
از بچگی پرسپولیسی بودم. مثل آرین سلیمی که همه اهدافش را نوشته بود سال 98 تمام آرزوهایم را نوشتم که آخرینش پوشیدن پیراهن…</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30897" target="_blank">📅 12:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30896">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plSgy1NKUpJWHTAS4TVgJq-km8KGTEh8dnWWrMBrVuwk4i98ZQYX2o49bYrUeXsZyKF8cjk6stwIRGEZN5hULe9uPVmpAfKP1IbUbz8xqXXjeOb4325UNOJO673BmvjytczwrGYKjG7G00TBDWLUN1uOo0dgwCa11Ub43NIq8Pcy_JQOZpGvZRm364qcp6P-dorsZy8sjgT13Z3Ho7any47cV_VoAAl_YqLIWaBsn0QdWCOggspVEX4GFTi5lZ_eOt62oFjKRqd-hneltG3VgmJJL_dZu1yqrTe73yx71yW1K8xftZh6eS2eaFK2D6ZSb9ZyXTq2hiP-WxVbAlrjtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیرعامل باشگاه تراکتورتبریز عصرامروز با علی‌ کریمی برای‌پیوستن به این تیم جلسه خواهد داشت تا درصورت توافق نهایی هافبک سابق سپاهان و استقلال شاگرد نکونام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30896" target="_blank">📅 11:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30895">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30895" target="_blank">📅 10:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30894">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gR8veUEvbEVBz9qm9plTEXnGCMoIgqC8ZK8V5_xNz9U2fDT85ehN39mTB-DXd1-i-vo6pmrOrDBpfUE7MCZ3EkG1oWNryotA6vmt0DawyIttdG6bsdSrzIoGD1xh0DXBlrttAe_-ijzKtl2Z-cLG4kLpkQPT7mlyTVqateKLfOWKyYgLf58gp2FSGZTM_7Wt60Wo3IVeeXx6878MIyUr7bbsME7Im0LhrY_xGg87bfPoui36J5ghFakm4-5o_ZY6Vc_iluqZNML3h7IeK7-1S98LhLBTWSIruM4zcqXjwMNIykdvkG7DOQcdopd_VvLf26KSQHsfV32uG3NHVv8-DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شنیده میشود که فدراسیون فوتبال میخواد که یه مسابقه دوستانه دیگه برگزار کنه تو اردوی ترکیه. اگه قطعی بشه دیدارهای هفته هشتم که قرار بود تو بازه زمانی 15 تا 17 ام مهرماه برگزار بشه به تعویق می‌افته. یجوری دنبال‌بازی‌دوستانه میگردن انگار این دو بازی چشم‌نواز…</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30894" target="_blank">📅 10:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30893">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGv6A3M2lHtUyFjHPF5VZFUjEjO3jkp3fDANUYjjXD37vr1hN3uyvDGc9ogox-tzt9LZNMRGEPNqAznq1qY2chJhwEvjx9_k-mNmUG3cyFh60H_kxmBr3zKYgQWHc5nxP6XD3S4NApFI4Oho94USjUO84KqSt1MsuoigSkYR-reFdPEPSdB-hdmK8uAsE7E7bnw9SrL7imDoOQHf0uAo2p8KnvJtpAbfNhJntOYwdaCYc2oivPoW0gZMyfG8TCaOt39pW3g0-gcaTi74-YPCWRcdFOy20lURrSiEBRzqHf673UOOetO-JzazYufKjou7E0Dxe4rDc84fn84p88ostA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه
آاس:
رئال مادرید توگزارش شکایت‌اش از بارسا به یوفاگفته بایدتمام جام هاشون از سال 2001 تا 2018 ازشون گرفته بشه. بارسا تواین‌مدت 9 لالیگا برده که تو همشون‌رئال دوم‌شده و اگه این پرونده به نتیجه برسه 9 قهرمانی لیگ به رئال اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30893" target="_blank">📅 10:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30892">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from؛</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uzm9GuDRxQYGie64EPfdnjwb6muBOTNCkG-ZBfwVEpNMlhG0uFmdKs6PRUacRlJiHpeLZCv29Kav6r8kLSh6IXzdm1-h5DBRpt8FL0zIRW0_68f0zCemdq5TQqcNaeHWOY_oVZ0lFKY6qt1tP5-47YxxhlyeuMZkBVxQhshcp9wFtc9ybeAsoeKC9tYzfqzxjn0df4nghfRSllmk2XFv00tCR_Tq-AWD_VdzDQdRtpX7enwVlkvqmfW9A3deSLqO9nRxxTNY5ZNyEca85kgjAzoEa-eO7NKVPu-UPkdS5gUiM_3IDITP1_bHUfur2l7VOLpQGvXB78sRBD_1oIpN0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لایو ضریب 2.0 دیشب که به راحتی برد شد
✔️
✈️
@best_form</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/persiana_Soccer/30892" target="_blank">📅 10:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30891">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQT2T5Ruxbyq5d8u81E7gtztJ1qFCdEG2k2ODj9mrgJxwCgNK2OokavPmLxZk5nWyaz0UlHBizP4rZ06nh-K8dXl-ClgFkeaOC9wqOUMkkI3EMGqswNXvp332iFSbBnzNSUA_56bEUNDvgZqL9cFN1BwHhrdquspKjWYBDIDYbX-i-aZ6cuhGgUS0rj0WtZn1W21Yw1UDqe-2z4lVIVL9JLHC-5YEQEfJasEZ9HW2VZw2Cik4bfhs6Rfal30A_KoecgUH8KBdyGDP7Ggw9Wx5SG_343q1qP5YS4sX-XC5Bh8WBHYMPLUqQM7vhPmCDM3M7s3DucgxWKNlIKl-NHdnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
10 بازیکن‌ایرانیکه سابقه بیشترین تعداد بازی در تیم ملی ایران رو در کارنامه خود دارند؛ احسان حاج صفی شب گذشته در صدر این رکورد قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30891" target="_blank">📅 10:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30890">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2IKnSWqSTIUXrJDV9r0DrVe924-_n7Ene8ovoGllal2TIkL3y-ITMDieJYPx76pPUL3VUvFUzhcSOn53X6lKf6TWiG8K2o0GfkE9qJC9FKemm0X6gnmqmNqmjhHjgrQ5t-kmupSvH0gTEA_Z8mhDFYMnIakb2hI_oNJ_5PkEpZYgTf2PTu5roiOA2EGY9BxuNezRsZEhjG1WuwG6umHWxftlFQniy7Gl3kS8IVA3pYbifkTE_TGr_ard4ZsC1pKZH1GGqMs2mJBLUDFu1oTsEdUqFxfaiWs58pw10n4QWS6ZXYKgflxHq1aoVqtHgoZmimpzk6YytYx7Eu_fDdzSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ترکیب‌منتخب‌فوق‌ستاره‌هایی که تا به امروز با هییچ باشگاهی قرارداد امضا نکرده‌ اند و در مارکت‌بازیکن آزادند. محرز یه مدت با باشگاه الوصل در حال انجام مذاکره بود اما به توافق مالی نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/30890" target="_blank">📅 09:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30889">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mn3MC4oX01EcIQQBZhtSuP_WVdx_J2MPD3J4iYRBB06bYad9JlEupYU_bQhRqhKsyX5jkgZZNYR4r1_eJWhP2YNXzUZIQ1HqjGMSkVYSoX9ydEXkpaJzNk3_UX6Djg_Sm-f9eaQPwBYuebGYzsq52C7OnDlVlJl7bcRVPVIBrrtWXGS5y8S6c65hUwKnmBbTLL3mj27o3-TK_im-zHGCimQHOc1lRN9GqRJdYHHx4FadiQ7o5EYuAXh4egr17tzTROUvyFstvHE-tg65KSOVtcP8z_idQM3DDjhjuZDvaM3sPA5xE4tJBVKJjVtlmo9sdmctnZK47Sc5DeTIfE3iCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین رضاییان که‌چندروزپیش در اردوی تیم ملی جوانان گفته‌بود که من اونقدر حرفه‌ای تمرین کردم که هیچوقت مصدوم نشدم تو بازی با روسیه مصدوم شد و ممکن است که چند هفته‌ای دور از میادین باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30889" target="_blank">📅 09:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30888">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7fabc89fd.mp4?token=guCdF2lPOuMmioEQpeP1U9orP18nG62jXkZCZYvD42KDjuu0q4euJJPtWwD1pu81v0cIfXfq64-h3PLZ-kd9O54pchHADChy6CuszFCXucLnKIFVaWAvI1tsPxE7NRqRdplWZspZXb7GO8Vuy7QfrpzesV6JRyKoqFb8DdEnWtrV0ODWDt_MIxUf7M6nZHlm3JBlovrLuzoFHlD_4R_Ka20xt-nW7LgCmvfW_VUX84IaUjkRi72PyF7HXmTz-c17NIOYaFY8O-V2qXM5ktZG74ofGyAReG2TSn8eWuZ72OX-VENOon6OEJyRildVF7sek3W4voQ4_290KYiUCBy65A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7fabc89fd.mp4?token=guCdF2lPOuMmioEQpeP1U9orP18nG62jXkZCZYvD42KDjuu0q4euJJPtWwD1pu81v0cIfXfq64-h3PLZ-kd9O54pchHADChy6CuszFCXucLnKIFVaWAvI1tsPxE7NRqRdplWZspZXb7GO8Vuy7QfrpzesV6JRyKoqFb8DdEnWtrV0ODWDt_MIxUf7M6nZHlm3JBlovrLuzoFHlD_4R_Ka20xt-nW7LgCmvfW_VUX84IaUjkRi72PyF7HXmTz-c17NIOYaFY8O-V2qXM5ktZG74ofGyAReG2TSn8eWuZ72OX-VENOon6OEJyRildVF7sek3W4voQ4_290KYiUCBy65A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
صحبت‌های جالب عادل فردوسی پور درباره مدل ماشین اونای‌سیمون دروازه‌بان تیم‌ملی اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30888" target="_blank">📅 09:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30887">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkgKiq6CO_b7vS2_0Dx-732xcP0Orztgme6nSVmxnAQcES4gSgglKZa3_Z1KCKe1T7vfj58zolrqt0zMOKEdX-D-e5FjY_fQPkUzIXGKrXlg7nP1M_sEQHfcgCtdbPeEVa9gfBBhEnvbbLBH7pPxtLmk-wnBAr5cojSx9ydX0qpI70EkN1CpDJ4amL8UxVTbYNfduAIbGugWU3b50ydrx51UP_0-azf_LeIAwoz1pzuKONl6nnf1vEXfI9NYW2rxpdSYfpvHsAWHw3lop6AAXrWUg0YQOT-n3C9BktB3hrJEPvpQEZSsJ44WCXV12EfotLyBBmPGYkAJA5ktDGfkSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
ولی کریس رونالدو با خدافظی از تیم پرتغال درس خیلی خوبی به‌ما هم داد؛ جایی که نخواستنت نمان؛ حتی اگر تمام خواستنت هم همان جا باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30887" target="_blank">📅 08:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30886">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4LEs0t7T9bYpRuEcs8pc9xBno8agzRMf3eDVn8bc6oXWIvSmbLb7bw3fTzJiP6j7qEpqGOK5yK06kKpRp2NhAMmAdG26MMF7oDN2i7zozaPXksCsr4zEi5OCfNatudAgyXtuSEdQca85KGRSK4N2YrTaw0PBYBpPXMCTLToBocRTMws4BfS50H134Vz0oYhEeZ2olSOPxYoRheSx0i99tPwLg5RhG7zcfiSCNEmWHTshdl1a3UThxrmCoITgCVH76c1ZyYnCzvJmAI4xJ3pvhYFionSWvoraf_iL76C2aujVOTS1N2LnrOX5cDDk0sV-XPSlnDUl_FaIbJWs7S1Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
🔴
معین توی کنسرت آخرش اجازه ورود پرچم شیر و خورشید رو نداده؛ وقتی تماشاگر شعار دادن وسطش آهنگ خونه، ترانه «بی‌بی گل» رو هم اجرا نکرده.
🔺
این اقدامات زمزمه برگشتنش به ایران رو جدی‌تر کرده و احتمالاً خواننده بعدی که باید تو ایران منتظرش باشیم معین.
🆔
@Persiana_Newss</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/30886" target="_blank">📅 01:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30885">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇧🇪
🇧🇪
ویدیویی‌زیبااز دوسوپرگل استثنایی و محشر کوین دیبروینه 35 ساله در مسابقه امشب تیم بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30885" target="_blank">📅 01:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30883">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbmCoP2PED4chQ4gkd93sZfFs0vmSt_lz-NSBWGpbY3TDOUfKvDxvrJ6-4PM1930-k1iAaTASJlVL4846FfAFtTaTQpvxmh63NN5Jbv0LiIj2dRx7T-ALGJcB4aJHzNzHRPt6L4XQOqitjwzjIsX677McmlbHli9qmAmLYcbdBjeONmpjtyTb6CRaam9_SgKE_yOruK8akBRZ_rLjRm3tGsQHlpOR_JZq3YqCjJyrjCzAviI3g6sAXqPinXdKZtDWrkR5rUe6nGmXlh2FvdsQvcHsN4ZNVDqDCJsg3251TPupE6nvHhc4-xRhKfRsipjdkyplR2chLzvGfsEIQUEMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ رویارویی دوباره انگلیس و کرواسی پس از تقابل جذاب جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30883" target="_blank">📅 01:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30882">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOW_PynKz-o2yQW01zqQQhTmfYmvwMl8ixXQIl6FshB9hfc5XIOcp0Eq3ElFSGicwnnzvC1PywohI1Pm8QoxJT75zRLe-Cg9LESmyI_PCna7XYCJbLf63xuia37RtD43ucdscO8-C7OAh_vaeyx1Vr5fsEpvkp3CycvEs1FNYs4ZH34-rdEbnktaMAv07Ak-ai4rZ9SQ33ppl45bRwDnt38YqNmiqk8XaSnLJAawGg9564dD73xrN1cF2JmkfvnjSywe9Xea3yYBNdkjNYKqGaUVK_e3_mJ-f48LBgtUmWkHHlOPQ4JaTfSSGIMqxiDqu4CF-fbyWkv_YdnyJsOBog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌ دیروز؛
توقف‌ خانگی‌ فرانسه ده‌ نفره‌ برابر آتزوری در شب درخشش جی‌جی دوناروما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30882" target="_blank">📅 01:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30880">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇪🇺
گل‌های دیدار امشب ایتالیا - فرانسه، بلژیک - ترکیه و هتریک دیدنی رابرت لواندوفسکی؛ لوا با این هتریک در تاریخ مسابقات ملی 92 گله شد. گل‌هارو اصلا از دست ندید فوق العاده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30880" target="_blank">📅 01:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30879">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-NvquSGBLYf2Cr3LEccQ4vVmJk6wsB2qCDlOlR_7-3pQ23cd7msP98sfCd2WHpb3am-kuCpS73iNV-ItHatFOqOIK1E8XDSKTQ-w7QhQNGwNzNcY7l4sYgS7guTDWMH7CQh-RHqOMMd3c4K6Vi9wL7zIZe0V39bXT90qD8j2wAThVzL5GPlZ417YasPf-7Vv0-EWNaHxFEZCdk1WSI_F_Sw8qMjJ_WLisd-rLPmG2KjTbzjMY2h20BDTuzqNo45Jsw9hfZrRZMHBYn04SpMdxOGF6N2jUbw3IpypObD8N-tPb_5aDJO81Xtigx94UHGlxq0v3ohTv6mD5B9CriQpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔴
پوستر رسمی باشگاه پرسپولیس برای زهرا خواجوی گلرسرخ‌ها: 2 بازی، 2 کلین شیت، 8 سیو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30879" target="_blank">📅 01:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30876">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d21gbNzLngCNDkLX0XOIxA1ufUMKXQT6n_Fez1_XqDFWUiNf2e45p9Bg5PIytXR7zx_YKywEhDh0-J-7nLDkPLSRSyY95puSIsi_z95DlibMZNqWSR9y3vfH-3avlKoabhti1TOgF-z2tjD9N-VIvemaCQqLsCuudJ5yVTeAuQM_smVKAt245ZD7kz8hVEP56NZFA16OEcE3znMZUDUGe9-gSIWoWAcv-ZJeXezpEc-PKAEXRmRB0LdFGEKgs3Pxjmk89HhiZAsuPkDDYEO4OvoqHB5QWn8eYxAwSswEQIgJyIiCTjahltnwTXq8I3UD8ooloTI6tOYiShS-m25IEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه A لیگ ملت‌های اروپا در پایان دیدار های امشب هفته سوم؛ فرانسه با ایتالیا مساوی کرد. بلژیک سه بر صفر یاران آردا گولر رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30876" target="_blank">📅 00:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30875">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0PZthgTmd1FVyulvfOaESrRSXkNp9qqteFLSKh9ezJ2yGxTZDOsRxfLeNQaRdl3nWTlitfzVzaFrI6Sw9uy8BP9WcoevgWv0eiDBaBLUCjTV3aZYFdl7bzSFnEki1tFEc9e7XLWnxso9m2zvytfnpse1mU6Njgiy52LQ0Q29zY944efKzoNppvYjEkSNEqGsPzcjpDYqRXd2sJ-NzL7Ux6LLseK4aydV-6EO_8Dw4eZoVw2CVTdFoegVYq3tYvpgKKchcXphMeM0liRqCF0ynYoEJhK8C0N5N5LQlNuALuUXurZUa9HZ-LYvNw-PquyRRDPtlOoH-8ctKzRSaKpWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از نگاه بیشتر بنگاه‌های شرط‌بندی؛ لامین یامال فوق‌ستاره‌اسپانیایی بارسلونا بالاتر از هری کین و لئو مسی بیشترین شانس گرفتن توپ طلا رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30875" target="_blank">📅 00:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30874">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NryWHrPUKPLNxW888l_iLlBheeM_RUxa25jjxu068uEGMiVjQPEHamWlgWeijzMW4yHi4anF59n6j3HUl5j6oX1WnbgEZoYnAhw3afyBkJ-9_9hvvlEGLIgDzGZ3CJEbCyMncsU0XaBK2eMCx512SNdi0SR5NMBeAwaOhL8XGAZ0m367-zzCNtg1m-j1amr_TvphzWONN6q-Ns7JFdGSLKYB1BnT0W3rJnGly1cjsdiHcy036idiNoLml6wcPjoyXJlGiQ0SmX6jXininecRDVEe6U43I3W07W1njXlyMJ6Lcoa2IpsF4gRAbwu6Xrlcm08_6cFz7eehVkwCI87g-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز؛ رویارویی مجدد و دیدنی زین‌الدین زیدان و ایتالیا پس از فینال 2006 برلین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30874" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30873">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0I4RfsRZQmIKDgRPG3yJmSDQJdDNMGWhZhKCdCL8gFAtfFCfpRn7bppVWYO4wKAXZ_2ydXr_YGoBo78LjFvG_RRMMiyLwUUbnmZoW7LHV3fHNnIa8pZexuPH4Dr4dfI8xXxX36iiR47ACUWAq9b3PzCM9IFZEl_5kKLpyAIJVUAkoPkVxPM_nLLSKA3jlEK5SjTjOj9RUFoFKTyPrxZ9Ye7zM2wJovOKoLcVCG6zid9FSJbOf5dTUfOL9iDJtjNIEmZPqNAtTEyQ8G_JM0oSipAz_iIRvDV2Y7Sw6_Pvo8oJ7eTw2x4mrY6JJMt5aojUXM0QbTMhSu6u5RMTt7Inw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال فوق ستاره تیم ملی اسپانیا برای دومین هفته‌پیاپی بعنوان بهترین باریکن لیگ ملت‌های اروپا انتخاب شد. اسپانیا در دو هفته ابتدایی تونست بادرخشش یامال انگلیس و کرواسی رو شکست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30873" target="_blank">📅 23:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30872">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpuBTcMCKNUSkd68EhRXOG8lDuIznFNK7qY5gvczqXXGg1UzxHQdTMa_6c8FSq0voosUNn20bPBQdOMkDMQid5-M3OfOwZ1-KY50xPNt7fdyscAEbvbl9xbgQPtBBkRojM0wzaWGdngN7w_CqXkoDDEwB956I-rgcRXFWF1Gai8d9xtWpoE8YgMwpjlwKf8mYlLqXDSfJjVx__ekG9uQcDILxar_FSMFrGR52UUqSbFDd35iRDMHlFcbUW7-GxnPKq_PEtjz33VgvSnK6RrpC5MjAfcAVZCpbW2S52UNOMVbGkUnZDSvMfEvmTz14Q0dFJzzs5fi4XfVkszrOf7jPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
ویدیویی زیبا و ساخته شده هوش مصنوعی از علی آقا دایی اسطوره تاریخی فوتبال ایران و آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30872" target="_blank">📅 23:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30871">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8LTzLWoGGmHqn-uthFqXZmSKvOtnPoKpOfBEbQlAccDPezouiX21vX-5IlEEVWWuHIwp_KSlQ8BFuoHNMt-GxllemAUDwocw1rPl6-PtNvLh3AjJWb5H5g2RxgnWV4re6qJrYJCrWCdigvsw6GP1QiJdHxAyJHOr7OOUSuMVlTq2RgChcaAU_OksGMolG0yPeLF6R2Ze8u0FaRvs8Rp1twhNMb2QJco_o6WHfiV_Y7N615bxPXzxmd9Zis2AR6gjve7q43Cygcs0t9AL7rkk0JIOOYlql0uK4R6W6By27gSqfy2EUbeF_O-OYf0s0cGchKEgdR0LfeNRkK6U6sSOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل کریستیانو رونالدو
🆚
لیونل مسی در سال 2026 در تموم مسابقات ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30871" target="_blank">📅 23:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30869">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oGMRWsH3PaKqu1k9Xw4u4QbXyYFmvOH-fcvXYbAfuXRbqbmHHJOfSCJROIRMJ15LgnpwHFyGDJLECP54bZjLiXYXmmHgVjM-jByliaSSYyYh69N2-V8RTTeHXOzVtHXnJrMoUfbSp0C_eA2ZzDna7LboYkkG-32We3_bP_rcD45vHjYzbGKr2NgLVzez1IDPAkBYkeGGz7TyXWpt6U5vCTSAn8CRsJQyoGBGvziffHSwxO_7V8a7FMBamJE-HjpA95X5qbGRK5TZILVEX_BiJQUfo7nVn5xWgg3hGl29UxmzyEdJqVLdIJXeX4mmfW9pn6M_E9ktqztUWYYDqpqacg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e28D9LCecrccJw1ogUsqQIIdMha9Ke2F8muE9g4I9lTLeDdpagSaTtN5Z7RTghYA_l3Nl8RQCD_zG2OcKMxi1BnA2DINdkVyBjc23YUvgNsLJtoIsewcH_J59KFKl4y0n6Y3JzL_b-rq5jTLeBdufypcRwq7UUJxXdSGtrMFpNgFc0BsNDjwKSC9-s_EXoBoUsepSv2nE0eSXPOnKiUeOwX3BlM6WBbexa7hWgJidAc4SdbnfuOP5FdyU5n_1z1Vtde5M2yCxYcKOHvCS1HRqpOHSZmOxL4_fykV7kjiKSVWlZljBAwew7SmlYgHftr_ds9Laahc3xQZW-c5dHiohQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تعطیلی مطلق استقلالِ سهراب بختیاری زاده درفیفادی؛ ۱۷ تیم بازی‌کردند استقلال تمرین کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30869" target="_blank">📅 22:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30868">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab82ee522d.mp4?token=PJ4dRUQjW5AQHmiCV9opfW3ANkWct145A-WEF2WdYstkcD7BVLxDXUyc6q4ZfLEswOHodnM2n1bL0Pi7lLFk6T6yUrLhU5wBhgsMuoH8ZebrjJy4hYAySjuRYMqmyL2I5LYN6vlI3TMWbANoGt1LuvL01D7TR5zvvp3NE7wL1K2mdEIAOEVepqE5qdpFe4iK89qETR-faM_ajkzFUYeROzhT7TXyi4TSz-QIgYpWSqrYj723EG92UzhMBqWDRuepmMKQLAWS0x0kw7QY1XgvHVViTmXPgbXKxS5inCX8putHtyTTVRR8MFxJY31P7XpZ5AMEb-CvUnL3oEIRoWYVcyYsLoXSOjiRVWskhU5iSYPI_l2cglhkXnb5h_BvLJXSSd0y3cud_Zv-vLU-z96cWyI4uiAYYpH_Ctk4s9M9D3dqx43QrH7kosMMqJDKO5GN5RDoN4Ppy8KX2oqH3eVEsEYGlD32tv03d7Mcj-C31MjZVqWDOQSUjhpjCGHsYSRQfovLjOoY_tGj2xomSSutmIEDUajMF3ld-24TXZR3JWUqGEY1Yqaii_Lb-c8TgvFlsmqAXZZ40gAbf5m6P0VHFs1oNCUB0LlNHCBmAWzS2WMhn_DwRxBzuZ7x2HXNnSoO3Bp7NJw5EajS7icQMo10RECN6orq0r3hdMnGINH3tWM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab82ee522d.mp4?token=PJ4dRUQjW5AQHmiCV9opfW3ANkWct145A-WEF2WdYstkcD7BVLxDXUyc6q4ZfLEswOHodnM2n1bL0Pi7lLFk6T6yUrLhU5wBhgsMuoH8ZebrjJy4hYAySjuRYMqmyL2I5LYN6vlI3TMWbANoGt1LuvL01D7TR5zvvp3NE7wL1K2mdEIAOEVepqE5qdpFe4iK89qETR-faM_ajkzFUYeROzhT7TXyi4TSz-QIgYpWSqrYj723EG92UzhMBqWDRuepmMKQLAWS0x0kw7QY1XgvHVViTmXPgbXKxS5inCX8putHtyTTVRR8MFxJY31P7XpZ5AMEb-CvUnL3oEIRoWYVcyYsLoXSOjiRVWskhU5iSYPI_l2cglhkXnb5h_BvLJXSSd0y3cud_Zv-vLU-z96cWyI4uiAYYpH_Ctk4s9M9D3dqx43QrH7kosMMqJDKO5GN5RDoN4Ppy8KX2oqH3eVEsEYGlD32tv03d7Mcj-C31MjZVqWDOQSUjhpjCGHsYSRQfovLjOoY_tGj2xomSSutmIEDUajMF3ld-24TXZR3JWUqGEY1Yqaii_Lb-c8TgvFlsmqAXZZ40gAbf5m6P0VHFs1oNCUB0LlNHCBmAWzS2WMhn_DwRxBzuZ7x2HXNnSoO3Bp7NJw5EajS7icQMo10RECN6orq0r3hdMnGINH3tWM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ صحبت‌های جنجالی و عجیب و غریب حسن‌روشن‌پیشکسوت‌آبی‌ها درباره ریکاردو ساپینتو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30868" target="_blank">📅 22:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30867">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6EnRlSIdGYEv9O97KPCT8WCBslIqhk_rQleRS-Evl3ZydXlS_uA2AXqhN8bVJPfmCTKfNHqStWh49XrhfmYswXJ82KXBBoNQMBGHPf5hAVje0X6cIi2pTaqfVecNoMvSJZhVYsB6lgJK8W5N_OFXtaSPAQ10JyrxVQMKE5sCIZhb6BK45vBUumHc4Vk6uVY7PUWRttTkuOsbO02q7BR_AUlWPsFzX4cpCvsL2bKhxobznc_7OdE-hg15FZpyMPC8dMeB0HJc0--AX9Ez6ui4bjEPsa5OGpoy-Q6vPTVquqA_LyqiwYxhnjJLWfPwjmPMJ44Ju5dBGzMMw8BRpao-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌ های رسانه پرشیانا از نزدیکان اوستون اورونوف؛ برخلاف ادعای رسانه‌ های ازبکی باشگاه تراکتور تبریز هیچ گونه مذاکره‌ای با اوستون اورونوف ستاره‌ازبکستانی‌سرخپوشان نداشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/30867" target="_blank">📅 22:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30866">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3d9WSXmvrg30CtV62GTivviJdusYRLoX1Wx_GsaZaTix9NQh3aL8pX4Xo96xL1lR5RqwhyVHVj5lfS-9GL9JZnkNsGXEXAmlbMmKii02X-cp2JPwb0OekG1g2WqhQVXW5m0-ZR0hxazS1oVhS9waPlnm42O5OoiXn7rahEI4P4iGcQFiVcz3s_Sr2lFsxMDADn11dlkmRh6P0hpIW_SFUsJydaN_lQEVBnOkK8tIHrGhTgZOFEwexWEAK_qbVG1cVAAsDD27J8mzP_mMMATeiUm-9lpFxyueiDOlY1adqeYcmGMRU5nZ8ky45Li6JK3TvYtlpPSZYjVlJxfe9SnzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج دیدار مهم امشب هفته سوم لیگ ملت‌های اروپا؛ پیروزی پرتغال در غیاب اسطوره‌اش و شکست‌ دور ازانتظاریاران‌ارلینگ هالند مقابل تیمی‌که کارلوس کی‌روش در جام جهانی 2022 اون رو برده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30866" target="_blank">📅 22:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30865">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqBd_x1KyXbGMgjxyq031k-a_OVyy25OCPP93OiTf8NOJswizdRG7r06RhyvJu_kW6ATGZl21x16avU0gEItQTswiBcDMlSe8aC6Yz5Uv-f-YyPIqyTiRIO-323h0FpS71aaujWwD-EOSFeXc5ZNWvlvD8ixYFJZYodpoKgEbgV02LPUZHXu4I1ttL-Ny0Cm3oK3m2d4nRu5TWf1E2F6wEqW9MM_hy5dnsA4L1l2AsDCbEqOPKZx8suGFCa2R_r5xglK03tsuSTrnb3CxhugZNiOGOcpl6sX3_1lC_849Vt7E82YRs3Xf9WeY8Lii7K_UEdjz9To4RhyotrJpPUGlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ به‌احتمال‌زیاد رقابت‌های این فصل جام حذفی بانام یادواره شهدای میناب برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/30865" target="_blank">📅 21:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30864">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOS9yf8uCbxVjaXeK9bp0Htt7x_UI9IyYvK69ZJnrF8YCQKeC3-S3Rlxcpk3muxIDv6wzp6akY_N0GxZI3R4pguYgag-VVsyHsUdQ0mjT9DQNOATIMoO63CcHooic3gtz2o8mo8_-yleE_4OpAihBn3aYiN5ukxDYBLIwqmmovmut6BVfALyM_u_YmSjo3BB6QofTEZ8VUlVY4UutIfme0HHSA7YwyNo00d7bOkgyIXxBxtiLPqw4n6v84FKHRnMUsUbSniKFvplsJs0mEZ6zmhVIFzBx4huIIyeCHtZ-5m8vtC8esbIVANHg4LTyAPBjGpjbwn-lX4c8T9BxmiwhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔵
#تکمیلی؛ درصورتی که حکم نهایی منجر به محکومیت منچستر سینی بشود؛ ارلینگ هالند، انزو فرناندز، رایان‌چرکی، دوناروما و دوکو بازیکنان‌مهم این تیم از جمع شاگردان انزو مارسکا جدا میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30864" target="_blank">📅 21:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30863">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ywaaf3Yku7PGmFBjiiXHbFJfWlbkxx5d5TxFJlz0tdJnsUi_td6ZxWEhNCFyp3et11GwjZ2_5nZnmpoCFe4Nq7aCZ4Hr7241prcyqSYFk0pxAc4RM9mCoby86IR_lNt0YU6d8Pbk0S4ng5Y8YaPfUfVv7xxfvumyWB3tqy4DDWeDPFDM94W9b8lJQcfaEz4MSsw_CL4e8ZWolGRdm-fESf4Hxnzjvdyu9MO6c3xj1sf40qrworZqzEshNWqftFGmVIh_nuvJlW0tsbZnvDtcUDA4p8pHnGy4KqX8NE3XC08ZtukrHOhHtoWqZuNP1n9xvpp-WfokDQcWdBEdUtUc3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بهترین و خفن ترین ترکیب منتخب تاریخ فوتبال از نگاه دنی کارواخال کاپیتان سابق تیم رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30863" target="_blank">📅 20:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30862">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogvd6_G2KQAyi7GzixE-dWRTN0GCTJu1hXz-R9fAki4f8RcZVLW92LFRlRz1dsCQ0GzVjHkRg3ZnGWlt3YsG5dA44Z9I6pUTfQ8SXdQRkaHXfl2ayOhp3bgt0Zg9IaJQIDLlX9D32xl0as4YQtjI5CuZLW1KuDNT_Yujei_RmeqJv5ERLqO8q2vr-JzD-3wtkgR0XcXKxNVyNt5SREJ6UQ3JpDDppwUDEO9VnLa9pb_RuaXtF1SrZNjVT94IEmne3p0n9l9VmZuH_9sst0lV7FahLyG6PW0EBkt3vDGwmckvCvK0mUXn3Wc8nWdFNk43EaoQxNEDFtrPxX9j5xxK7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛نشریه‌بیلد: باشگاه بایرن مونیخ امادگی خود را برای‌ تمدیدقرارداد مایکل اولیسه همراه با بند فسخ200میلیون‌یورویی‌اعلام کرده. سران باواریایی‌ ها حاضر نیستند با رقم زیر 200 میلیون یورو فوق ستاره فرانسوی خود را بفروشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30862" target="_blank">📅 20:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30861">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSSdHWo9vscOUQShM7dAep8dPX_mOfbvAGZd7gfSGMxIKAFj0-4tA2CXl-PUYgmGVMX5m3h-GDIOiGrVUdxMgPrhfz8ivnV-TzPIrORlWa7mK4mQQxPNZfl1i-qCeKnnASi8m-qRdyz3y7SSOo5V4HQvUDdnvufVkBIExUE_VDAXOC2CHoT6voLvU8czGguiKIsYcvJi0ylNoMEdS3N-rfma83MXUHylKVMMNYiO9KWMf9z3v703GNOem1Ic5R_7J_IfRARMIjFfwYaTKIHGcTUr2EnWtrZFMESF0rmsuzsa_W7MSjbRf9E60DqHVg6GXx960fsQF3DQTl0ucriGpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج نهایی و جدول رده بندی رقابت های لیگ برتر بانوان در پایان مسابقات هفته دوم رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30861" target="_blank">📅 20:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30860">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-CMccCMvEVNhbeeTnqL6huWaXCRoRlGqxwaNz_PGysKBIgBcR4MlaUwr9ZPfTnKukfbfjTVhUtTuBX0cFirb7mT5n0KHmcFxzKC3Z9kjyzpk72r1zM7-Hsm1G73zW6NhTBUWQ5qJfnxE7M3VfVpN17lPciMXH6laeGH2c4MxsYFotIbG-7IIOefKjbkOXYPngoiGK2CX9c0EaohRXl4wKm2ZFNNZkZfWX-vZGRZd1_pccB92Hcx2RItN_hzw56mtz4tC9ZZIxFgXGkH3porfy6bBNZbirBoktaYx-9NSBMwCihX-hatnuLFuoYCWp3ulMGr4iqdGTfOG51hms1cbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
هانسی فلیک سرمربی آلمانی بارسلونا بعنوان بهترین سرمربی‌ماه‌رقابت‌های‌لالیگا انتخاب شد. چهار مسابقه، چهار پیروزی، صدرنشینی مطلق لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30860" target="_blank">📅 20:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30858">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24f9f9a87d.mp4?token=Vb6BQiA69UKxPGh1-7eN9JMr9i3m4veWIQaT1OJF0GHrMNvKR8JFYDDfz5_ZrOF81QzQZ8k456jJW5FEMqCVAO7f-sDbdhoblcS_woAXKYV64lHsOwFFB5IyOlEVYyApoMh91jKYMIFk03TomJM6VucegWu1n6KuMfOLwett_bqLLdsjtiOMo-DBC6-1H7_Yft098UE20cTjGiruJchgk6Dcocyjiqgh4e44FU8p9NyaUnaKIlwK91yDdmdQ6ojKBIw8tAQMO5Up5T8kY5UZn7EuX-dZY4paqj-_geSqmoo1UTJkeL6BusD4hE8cv3GJqOjRrbmDIE26UFyNM0WOLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24f9f9a87d.mp4?token=Vb6BQiA69UKxPGh1-7eN9JMr9i3m4veWIQaT1OJF0GHrMNvKR8JFYDDfz5_ZrOF81QzQZ8k456jJW5FEMqCVAO7f-sDbdhoblcS_woAXKYV64lHsOwFFB5IyOlEVYyApoMh91jKYMIFk03TomJM6VucegWu1n6KuMfOLwett_bqLLdsjtiOMo-DBC6-1H7_Yft098UE20cTjGiruJchgk6Dcocyjiqgh4e44FU8p9NyaUnaKIlwK91yDdmdQ6ojKBIw8tAQMO5Up5T8kY5UZn7EuX-dZY4paqj-_geSqmoo1UTJkeL6BusD4hE8cv3GJqOjRrbmDIE26UFyNM0WOLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
حسن روشن پیشکسوت باشگاه استقلال: ریکاردو ساپینتو تو اردوی کیش هر شب دختر میاورد تو هتل و ترتیبشون رومیداد. تو سعادت آباد هم خونه گرفته بود مکان کرده بود. بعد از تمرینات میاورد تو خونه و شب رو تا خودِ صبح با اونا سر میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30858" target="_blank">📅 19:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30857">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYGMMMq--CUELYiXI6B3FN2HyXkpsYIH-BVGzBqW7nvV-RzwpUszKUciCqJaZJ7yie0wIZvCbLgOjo7lL6PCRTQjKj69Jm_6dD700GYOeE-jVuWJEIBCzr1xw3Ra3eS_8TAvH5ziP__K4fRZ-Ewo2FgiFhBUnt5QeJ-BZOHfqu8By6vpOqpbDmeTRMrb6LxS1yiA0Hi8VTTX0I5IagUz57JayTLPuiv4yEiNGspZEe6oUfFrKSp747w6Ayd4mYZoj2C95C1F74RKoTJFQu7FNA2paD7wBADJyw42IDB2rzJqojwFJ1zvs8-dVWWTDuSM3MDuP6GJ6GTyLqK8QHsFlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل کریستیانو رونالدو
🆚
لیونل مسی در سال 2026 در تموم مسابقات ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30857" target="_blank">📅 19:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30856">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W73VlAznn8uH4XEsOtc3aQ2F4J28Jem5wUWJxfZdh9b79daJt_qNVCJkq3fvrDUddHB1LnbRzuDwyMWcDA4pBO-fUukXcuTtAG1uyfG9SohL9wmGvtc_6e2PIDpd4JVmVC6pyLKs9P1guTYGTVdQR9PbRU587_QJXJK2eIpU7B5KHIdw5owUJiioD50IS6-puiy8Q6mEhZxmpsdu9deCuNZ3Lc5A-bIeSHaTvJOWy384gCz4w2k9w1pt_lv4NQvTo99rDS1IjaGKh0SF92kWdbTMvLtXJpcccU-_q21joY60Ctnh44KkMbbDV7Sc9zFOVogGcQQa0quVC5FRAJJyRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ رضایت‌نامه ابوالفضل‌رزاق‌پور و یوسف مزرعه رو هم300میلیاردتومان خواهد بود که باشگاه فولاد خوزستان درنیم‌فصل با فروش این دو این رقم برگ ریزون و سنگین رو به جیب خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30856" target="_blank">📅 18:54 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30855">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1Cdf9B8pkCziaDYJOm4Ioq_EZcEHEV4wqm5Cgw7AAVvC0ksVFuWTVn5WJo7yKSjslRQNH3qm5puBpUTbD_RZJyeadlGExAUBdJ0VR2tKH3_JywvLGSCOKbXGHH2wvnGa8kUw_4pucTlknPPku6PAdGVD9w4mTMUOe9veSoASDQDRYCv7mAeJChgRMp4px72rI-Fbgr42V2ZkE85_dGi_zVRyGUHcGf9teIFPh4_GfbWsG4YfmI6WSAdrIZI5OIKB9_as3go5NB0ICE8leK5me6G_jQhLLiktxWs88y0SLZ6tFqerLetDpTtpXwmhiTsWf_-fh42XVgMJJVNd9MkPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
هانگ کانگ در شمال نروژ، با جمعیت 2484 نفر، جایی که خیلی سرده و یک زمین فوتبال زیبا داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30855" target="_blank">📅 18:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30854">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdJd2akzbSEcXeHc7c79QLkvxnvBaKr8faotM-CPd112yfDvrQzqWru75kyJgH8zAZLOL5mGStWNd1-WPZOPI5SiEpZL1NY1Z5ATO5c_GfKltyZpcfX76W0yfXyRpafLh4cV4kQlbKfi2LLazuhdmW-NBDb6F6g7TgSo3FnJ4Q1y-4tcLmaJHVNcSYRWz2Yv2Py6SCqRL5fky6Bakm-qERFMZ5kqN8a_pnmJvr5g12tm2Af0eAvI3WYN7Y7oJFx-NMzQVvB42btbLFRqIlzPVBCT0rLioSJLWSsNm26UUuGYFYBc6ZeZdSy4Kdumqji4OxdYSMvGNtMCD2eeErhf7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ بعد از خبر اینکه رونالدو به تیم ملیش دیگر برنخواهد گشت پسر اسطوره از تیم ملی زیر ۱۶ ساله های پرتغال حذف شد و اسطوره تصمیم گرفته جونیور برای تیم ملی فوتبال اسپانیا بازی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/30854" target="_blank">📅 17:48 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30853">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfjLQqKpixstrJQjwm66I5KwIn4nImlXe1PNEyFsktST_rTByY-GoouB4jZ17hGvZIALUglWlUhpzXlVcpy0R1Lc-soNxJWreHMQmeEQ3yKD5MmKdf2NA-KmC0vn84sYIFRlYTb85bAoQ61C5UdTIxVyRDFkj5Yyzfs5YpXmj2s_vNuj6KwKw7f-SBrJbkwfcCFxMVdTHgw87TXOnlNYvSGSrTjJMFu_8McupjzwncLtO1S96ImXr02DxLi06MIOdT2nN_RHAfQ94w2QoGmKcEzswb3DptRNZQrxjs0wxcQwCv5re6iyogS82iL0sjlbwjs4fg6Cti7yxQi8We97pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز؛ رویارویی مجدد و دیدنی زین‌الدین زیدان و ایتالیا پس از فینال 2006 برلین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30853" target="_blank">📅 17:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30852">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXg3IrW8r7rP-y3l1fEwo9_dHl7_syALDiphWL_dBhUIe_2Te-A-KUNf76VkvxEQeZR5PJ7SgWnAgT7SgBL6U2rQSVzICELVjZIaRkavP_auUyOPsO1OCwvH0aH7ThN9G-WoRui3ePEm-iVWgIflced-Qv5hPUwqftvztDLuue6WSYB3dB0wF_svwqn-JUpJa7-8R_D1QaaSilWitTyA7saOkPZa6hZ-z2pAcWmvSjzA0VboNFw4qWrib6prTvN6cQw6pmy05kLrsMrRyrrvq1-0JOLlylIgt81AeKHgpqUjvif_rASkhKPR8-cepfNTZzACoWjXo997Yq9c9rjBiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توماس‌مولر درباره‌بازی‌معروف ۷-۱ برابر برزیل:
بین دونیمه تورختکن‌ما به هم نگاه میکردیم میگفتیم چی شد اصلا؟ یواخیم لو بهمون گفت نیمه‌دوم کارای عجیب و غریب نکنین. نه برگردون نه دریبلای اضافی نه هیچی. باید به حریف احترام زیادی بذاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30852" target="_blank">📅 16:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30851">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROoTXPCcNkfztmgzttJyag4OeAIvHY6r1Wob_TaBXk-Kk6dRaV95Ff7fLTtBy8k1EpGG3qnTgRUnLc4lYjN9fmNbK7mW0gfb2tzYBa8sZ2omrwjVeb6EEcmspr6ds7hFkpe5csRBYdzBdrbiHNdQb864t-op9W8HekcvK20nmkqhtaTIiUXBYVYUMGTRqiR0eLPKS4AF8OMNHR274N4CfINAm_-vcJuhZSdo3zgcyYAFKi7OW8Qm4O6bz5VR1ha7l6vGFFw9TqKaAW3qgSU33qiNFCQnaQ9Keqt-pM81pZKW5moN2P_BH4yc42XB_yEgP7LSvuq4syoynH-KA2-86A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحالی که گفته میشد خورخه ژسوس در پایان بازی‌امشب‌برابر دانمارک درباره کریس رونالدو خواهد گفت و از او بابت‌ این‌همه‌سال حضور دراین تیم تشکر خواهد کرد اما او از هر سوالی راجب‌ این فوق ستاره پرتغالی طفره میره و جوابی به خبرنگاران نمیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30851" target="_blank">📅 16:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30850">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scNHkAxkgRJuRG-RYfJL8pFf3P4PAfOPKlGsk8prMVsg8nwfh8JBGlh8jIskLEagfXLqozcRI6YCMjAX0Vh_zgmFqQVWBqpuCUYE9cI4_nYYAi5nApZjs-IIDoOZAZ1fwC2srOM99JuV2SoxPk72ARK-WvLle_F4p-BSPo32S-cW6F4Ei1ogUejcUwS4lD_qLjZCjnu6MDwGktWrVe6f_1tzEIw2T3z6bHfa3tPmIOxc52hZ-5MQIEmwi06hn6cpeKrJJ8mjdwJOn0cnOYD6vQJ_vd-7TKGiDlItDEKsAdnrBUJaY-LlomHuRsj8GicKHGRr1ZW-851v6nqB5UIo7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت‌ جدید ایلان‌ماسک:
اینستاگرام فقط واسه دختراست اگه‌پسرید بایداینستاگرامتون رو پاک کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30850" target="_blank">📅 16:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30849">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCgUsEggNgg1s05k8aw4J2ZlylaiZple--Z8nVpp6LwjYXLdgfvnon7TLEJ-40_axL6fte5tOwAvLdJiUtSr0Gxd4WmnF7NDNemz3J4_wlyoVhdCG_ugYHhLuxpzxyf9wRCWiW54qwI4qw_8MupviXdTnvGkdnS385QBReZGZTfODAit96OuJjv-8a0K4jlpZezT9NxGhdwkjjyOqvN18ijl5W-bfaosO5_6qZ6AxHyRW6fVnEI6DfuldpfVDgjOR1Vn-d73RRPBQ1ruFl9Cne6xiwjqAfjcphjbM9atv_Asdi005Q84Wx9ere4Uh3UVn0IsDm1DAwaQNLqiiFjRaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب‌فوق‌ستاره‌هایی‌که درفیفادی مهر ماه مصدوم شدند. حالا مصدومیت امباپه و رافینیا زیادی جدی نیست و از هفته بعد به تمرینات رئال مادرید و بارسا برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30849" target="_blank">📅 15:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30848">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReIMrWBvqXHcfF--Nn8pogCgIoiTHRH81AclvFKb55eXMbVlBRela4ADuu3mMkv3oGSJJjizQiyUmBNeJmaHn3F-KCc-qRBmx6k4X1gQ6C85JQYe0ermuG7088sa4DNIBgUoOJlwUwI9PT6buExJiwGCSDGrWeRTflWjJzzSd7TeaeNGDoOKVH9ZXYXynVJkbDApUUvPN9NWQlsB3N8bVJCyKxAvpxBo5cKBC9nMOglx6LCdHOlmTq0xtp81_x3T0xtcvwoMYx8kaOXPpRQ-XDX8Qq6_5FxQjolYyQGEkGXr67S9_1ZOF4nU8FdzUfp7C8ixeTP7pvNElD21d7wLVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇭
روزنامه AS: باشگاه‌رئال‌مادرید گرگور کوبل دروازه‌بان 28 ساله تیم بورسیا دورتموند رو به ژوزه مورینیو برای جانشینی تیبو کورتوا پیشنهاد داده‌اند. درصورتیه ژوزه نظرش مثبت باشد فلورنتینو پرز با دروازه‌بان سوئیسی دورتموند قرارداد امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30848" target="_blank">📅 15:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30847">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSgcFrQyHOW3y4cNrlHFZ0jNS81jFA668NuDgHPhjOzt0QwiTTLWNM2TVzLqpmJtR2hs19NzZBeWU9tIhs9COMQ88GZHzl6VNbSNoeFnhn1h5NhxoAqFRmFfhCyvOewtIIRoat_rWAHdJkm_pcQRFmFVZYU0j3sHf8Vvn0MSERA3a2xksgUbXMQq8SCxYULB26e22JmtsxrUuIEg2RpvIttF4-ThdnbE136ngXlhCfajCsxQSNPidbJZnOLAln2WDLE6Fo7XmRsZpODUDr2dvHmsgCpzB6QRJvWHi47byOmrfh7vg0iV5vI-qfv1EN2Bx6jyU7wKx8--cxS6znpEmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دانیال ایری مدافع‌میانی پرسپولیس به دلیل مصدومیت از ناحیه‌کشاله ران در بازی اخیر تیم ملی امید سه هفته دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/30847" target="_blank">📅 15:17 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30846">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXMosSByvkPvqwXDxg_rbjca5wI_vtlp1a5v82plvx7a8LPYBAQ3xQ9RB_oVe3VN0XH218TW013MpDTccXdAAlVIcqCjmfVPXmfe-2D8YU9kcjIMISUdDbTBYJDgimHiStVmuhfCA7i50FIq7gUeAnz9O9v3MuKIFNW4Hp6KyHgMA7RkRgsZjWVUpGPmAlmCGOH-SagaNsNiB5z-a5HA4rTWRsUg4xVZROpFV2_1Lnq9MT7vxi9rpIFG84YkCMn3r4RLZ49149dDmVwew5cigBdC9FTraNZKZqSG3a1_H8Wn5F-wx22fJ2OXf0J8hAkNyoAWmkluPn1nAx77pEslSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رافائل لیائو: پوشیدن‌پیراهن‌شماره هفت تیم ملی برای من خیلی خاص بود چون رونالدو از دوران کودکی الگوی من بوده. فرزندام هم در روز هفتم ماه به دنیا اومدن و به همین دلیل از این موضوع بسیار خوشحالم.  تمام تلاشم روکردم تابه‌این شماره و این پیراهن احترام بذارم.…</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/30846" target="_blank">📅 14:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30845">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tq-QXwssCqlIo1YnzyRidM3ippkzYTx1yx0VpLDsB6Otrr8xIpAS1fB-ipMzmF7mrFXv1xFGQYss1MxdBaL_DCbqbiWwOEM6jay9iyopg8GuLGoC8fpG6JZ0iyvXarzywkpgcR6YnXryDdSBhAnVyjg_6ibX47_XPOvqIBaHg2iaKTAZYvcw63SiEmhcdD_J6j7S09GeaaJ0g_8eay0UFaOCfqpjaUMJeXAwme4GoRq4svTOGBgEem-wnxnb9V5uOAerOUNPBoQefj5Sl2UfIYlr9dTdwwIcOhyltT29RoGHNxbdL2CXg2GzKCWfiTjDyTSjFL5qgBdSwjRxdV06Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه پرسپولیس؛ دانیال ایری مدافع جوان سرخ‌ها در اردوی تیم امید دچار مصدومیت از ناحیه کشاله ران شده و چند هفته دور از میادینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/30845" target="_blank">📅 14:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30844">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e6e601e1.mp4?token=h0Ee-nn8DwhKPLlYeSscdihmKE6tekRWRO2fcY5fuPmMqr5Tt1YTz3btYf-9H0Kybl8ZbQ4kmVwpmnmvhyu9TeB2_DlWY0JpHeBmSi_X1cDd8nW8uMKEGCYiS0eN-k32B47AL8RAhlAPElSyr4BSKV9iHPESJO_Bf12Kg3auWE6GKTbthyuFfaL9EHU0L8M1X2W64GdR1duPsDn1GoH4jHLW5u6_hMcE0LGs3mGLSWr31xse0NJKQcjHXg-buEAkOsYi_EPin28RlIX7OzR8egmCMmiZ7ilTG72-zxNliCoIBuMUIiIns7BvNLBBsRFzrpSAKDPT2JVkEdCTNqjzF7h_yTurk_wtKykiGnJW2vMxa9YLBD4HzulImVWTfsXC46IyJg77ypLbmmmw_hgG7Hu5SR4Ct7limZpmIUQ_0c_tM1eiVDgPQPh1yafYHdAq9O8IOf0ovo7gp0pxqr5lcpAYm0a-XkcseaLShudX1Y3yLqco2elZ8qfUz7aODxU5AKubZGrGGDoepg0riD0S3dCQFZ5KOKC_WTu6Tnl2ehOMrJa2coBHl1YJ5u62J60YjsdcxgFt6bVhjaj2b7khWAASWeAwQgZA9hY12tB5ifA7v7YbbGh4WdlqqwYl4D4w5_4mmJx7Q5WCzobKhpkKl5GGGZoUbWVo4r3-2dB68ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e6e601e1.mp4?token=h0Ee-nn8DwhKPLlYeSscdihmKE6tekRWRO2fcY5fuPmMqr5Tt1YTz3btYf-9H0Kybl8ZbQ4kmVwpmnmvhyu9TeB2_DlWY0JpHeBmSi_X1cDd8nW8uMKEGCYiS0eN-k32B47AL8RAhlAPElSyr4BSKV9iHPESJO_Bf12Kg3auWE6GKTbthyuFfaL9EHU0L8M1X2W64GdR1duPsDn1GoH4jHLW5u6_hMcE0LGs3mGLSWr31xse0NJKQcjHXg-buEAkOsYi_EPin28RlIX7OzR8egmCMmiZ7ilTG72-zxNliCoIBuMUIiIns7BvNLBBsRFzrpSAKDPT2JVkEdCTNqjzF7h_yTurk_wtKykiGnJW2vMxa9YLBD4HzulImVWTfsXC46IyJg77ypLbmmmw_hgG7Hu5SR4Ct7limZpmIUQ_0c_tM1eiVDgPQPh1yafYHdAq9O8IOf0ovo7gp0pxqr5lcpAYm0a-XkcseaLShudX1Y3yLqco2elZ8qfUz7aODxU5AKubZGrGGDoepg0riD0S3dCQFZ5KOKC_WTu6Tnl2ehOMrJa2coBHl1YJ5u62J60YjsdcxgFt6bVhjaj2b7khWAASWeAwQgZA9hY12tB5ifA7v7YbbGh4WdlqqwYl4D4w5_4mmJx7Q5WCzobKhpkKl5GGGZoUbWVo4r3-2dB68ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسابقات‌فینال کشتی آزاد بازی‌های آسیایی هنوز برگزار نشده اما صدا و سیما به‌استقبال فینال رفت و مدال طلا محمد نخودی و امیرحسین زارع رو مردم تبریک گفت. "جلو جلو ذوق کنی کنسل میشه آیا"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/30844" target="_blank">📅 14:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30843">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0MW9MLLLyb3nXGNcYE_08Fi6TIcvRy4aR7CyU3tpTgRgCc1hjiULiPsoEww37hZAcfhUA_fAMTkyaQ_-57u-qs8fXSXydeTQDIFqLlPt5MpO0h32wzphPhx3GsyzvV-9r9lu60VXgMvXe9MLr0GqKRIYnaK7U5j6xM30A7fKpSv8UB4XY6f6vRvHfXiGDgHPTh4IdiE9yDp3illIzhsVpIoI7jSrdbKE1OZtlWA9r8RO0OG_3lwXDghR5tm4pzf1nCvhcRO6dFP6awqsfWKiR7Ew2moJ9NxAEbUViJfhD3u3mVS8Mfy1Bm8TdEJmvm7dmro1ySUAqeIW_bM0YBBKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نرخ‌امروزمدل‌های‌مختلف‌ کنسول پلی‌استیشن 5؛ قیمت PS5 Pro درعرض‌تنها کمتر از یک سال از 40 میلیون تومان به 315 میلیون تومان ناقابل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/30843" target="_blank">📅 13:49 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30842">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXRRzqyVCtS0pw_5PJfxZduwI-_SMIFwAW0zKKRcl_RDCtjl8mQMGZaFUMdxlEWi-1YESTnmw4t2WlUttrRc_oMX9JIiCXHMqL2jvq6S1FPHZBy5NUsQjRjPsW50l-HuXL2eGXMpg9jnWoSp60XtjrcjfqaIr8tNW5ywiGrO8VS-GQF_OANPvHlnyocPjX7scsAN5NQV3j41zErw8z7Owd1RQrED0Y1FfbeczQoVtfEZIr0M5W8Pu_sjq6B-DDBAg8Fp2P_yMtFLcce8birNPKvo9ODMYsrJ5ksQUSMEIZ2q6OhhFilOpa0OWgKONZyy1aH6Ny-ae258RZXxepiILQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رافائل لیائو:
پوشیدن‌پیراهن‌شماره هفت تیم ملی برای من خیلی خاص بود چون رونالدو از دوران کودکی الگوی من بوده. فرزندام هم در روز هفتم ماه به دنیا اومدن و به همین دلیل از این موضوع بسیار خوشحالم.  تمام تلاشم روکردم تابه‌این شماره و این پیراهن احترام بذارم. از این پیروزی خوشحالم.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30842" target="_blank">📅 13:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30841">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkiiIhmC5F8TbjdjNqIe76lNvK98EEmbhVDAzB2ULhHodZXNn6gEnNV8fdLLnk9n5f4DtpgGhTtsnJwwgitDEyCjnEVaaCwlJLwWgOHF59_XOechFn759yUWw0L0mLBS_QTGFRA1dWBZsKbIYVazbxK_rxQpIlMUQjtnko5gIYW0Itr7lqwh92JNtlerkyBBZcnORm9IfIYTt-HWkMmZxQubZ5UBip_fRMIeTHtKPk63xcLHC11Y6WckpvYWxBYf0mMevymA_hLr5i8d1fd7WvjmCqIQZxt_hyfWOgSgB1jgKzb-Au3_TuNBF-YEfekKKiv0EsOrfXjwsU39Yiyc2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بهترین‌شماره‌هفت،هشت، نُه و ده تاریخ مستطیل سبز با اختلاف بسیار زیاد این چهار نفر هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30841" target="_blank">📅 12:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30840">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBMu8AA0Gmy1pxLINXKFZl5mzGx_L4MH0RDKYR4P4oPNxwJ5F49IM_k4VpnWDtJlrwIZP44-v9tLG4_4_TYSOA_daxpNF25k94COaA81cw7gUQeM5CgP0f5iCTDX_BOoqsplqTHEwMW1uRz6r8mYNCCtRqcHgP2w6TC-k2ZMahl4eFgLiXeuSPvNjVId3aV37i_8yjVt4w1RojUUQt7mpJrVMumQVIYhZncK-yR-GAqyr0uYZdp0AyPj4NoxZ9v95jGu853UxaASE3hKOKAnrbPtYMIiBio_ZQdEVWp5yhCKsnWryj3IkHq2P7DoJ2cI-6AMUMBD00yk9WxR-1Detg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه افتخارات لیونل مسی، کریم بنزما، نیمار جونیور، کیلیان امباپه و وینیسیوس جونیور!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/30840" target="_blank">📅 12:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30838">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJ6_I3R-k7lSOISqH2TJU3bXz4CnPDtuZ0JgJR6jYoO8Y9M1hzSELDX8R0d9lPbzvTYQExd3wZxstJzfaKDJvgiRTB6SEN9nJWbHu978vUdt2Udy0yjnmolzWQNBo2Qrjl1ptR5lIbVh0pqCB4rz-r17U8gieIML1zwVcL6cFLAZq0Qtb0URgL_aF0ycMBG3XfWgfFUZ1GxvoUe8E0Z1dF8IKhFv49fnDEAQnJrsJf9cHrIfeEsOfHG35lmjT1oMLI7t_Zxp1-eH7KF-FkfGyyBh9w1kAZQKZ2A7qoFwTqPFJdO0IuAWDU9qcMB15ME_76aY-4Ivr50dw8ofGtKYfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه بیلد: سران بایرن مونیخ از موندن مایکل اولیسه دراین تیم مطمئن نیستن به همین خاطر دارن تلاش میکنن که فلورین ویرتز ستاره آلمانی لیورپول رو جذب کنند و جانشین اولیسه در این تیم بکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30838" target="_blank">📅 12:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30837">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ze6e4jjGbF3q5EffyEc_RYCep5XeFEr-dPEmnme8FNee2yDqQx-LmULf5dqpafJIJp9uTLgxrqJbr0QstyRC34Xd3AswE9uyx-Js_NKCuUMxlhLkIG5oQsNV1lfA56yYs32yPOUdChR8JSFqkg8fDBJrFIXaRFMuXMF9pl9BL0nglXUdfHlGaBEyJWqLjNNEso_RVKhFcG-ou25Ot9J6pGf4vBu1j2ueMvDGZlX_uJW4plafSCVr_DKOE-8rRZz0Rp53656az3jS5PBhTePtapcdtNjEUe8EaRYNcZOR5uom9wIvbbzNdDoGGci51IT5C8V_KzJksLuVd0cOqqQ2hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسابقات‌فینال کشتی آزاد بازی‌های آسیایی هنوز برگزار نشده اما صدا و سیما به‌استقبال فینال رفت و مدال طلا محمد نخودی و امیرحسین زارع رو مردم تبریک گفت. "جلو جلو ذوق کنی کنسل میشه آیا"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30837" target="_blank">📅 12:14 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30836">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dc2bf5c9a.mp4?token=BfcF9epKEze87CsnltPqoXnMx8iy_23QsUXiVOfH9KACIO167nOvzoWBv_x6MHafRTI34B_uUM0D16Fp5TjfC2Jkj3aCkuyGaxmpEjMhEHXdTeKyqy981VuQ9RtKdqccsLcKf7oAm_5CD4Ayr6WwMljq7f1QMzLKACWakeAUGkUklho78gAcVVdUPQOVantpKH-me6auYqPnhDBQSCvwTTuokT3joODSHsQI5GEhvGkEl9N75Zy1ZvyQuiBaTF18DN5O5tQTK0XlA_wSGbjxCN3aNjDan6Jlxu2-37DYeYAa2btTruyBwOxbocURciHjST2aAXgTZ6BAEit1HLc_Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dc2bf5c9a.mp4?token=BfcF9epKEze87CsnltPqoXnMx8iy_23QsUXiVOfH9KACIO167nOvzoWBv_x6MHafRTI34B_uUM0D16Fp5TjfC2Jkj3aCkuyGaxmpEjMhEHXdTeKyqy981VuQ9RtKdqccsLcKf7oAm_5CD4Ayr6WwMljq7f1QMzLKACWakeAUGkUklho78gAcVVdUPQOVantpKH-me6auYqPnhDBQSCvwTTuokT3joODSHsQI5GEhvGkEl9N75Zy1ZvyQuiBaTF18DN5O5tQTK0XlA_wSGbjxCN3aNjDan6Jlxu2-37DYeYAa2btTruyBwOxbocURciHjST2aAXgTZ6BAEit1HLc_Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طوریکه‌قراره‌علیرضابیرانوند دروازه‌بان ملی پوش تراکتور بعداز اتمام‌معافیت‌اش به خدمت سربازی بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/30836" target="_blank">📅 11:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30835">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✅
نتایج دیدار مهم امشب هفته سوم لیگ ملت‌های اروپا؛ پیروزی پرتغال در غیاب اسطوره‌اش و شکست‌ دور ازانتظاریاران‌ارلینگ هالند مقابل تیمی‌که کارلوس کی‌روش در جام جهانی 2022 اون رو برده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/30835" target="_blank">📅 11:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30834">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9446cc89ef.mp4?token=XSAHdddRp4BNft9jD_5d5e3uySBCQaKS6dv2sTl39kNIA6CgxtX-vpS1-80oC0zXEnWwI5wsPeIIASb6F16h5SORV_3OtzbW7y6YdlOUMfMvQbvOssu9NG95gB7wDKWdgRtmewREyc_hUtv3Ph3-4-4I7VGwZwZswRi1OlsQZTIzVdop_mD_1ducS5HepmFFETu1wrLeGQcy0zf4OTMO7T4tBuoyxRcdJtyciGR4nhGvH4OOdeV-YNp7CtINq_j4ps0iqFVsFC7fL37pkrVv_DW46yfZLrtZNRscYlddWRIHCx9lyXERk5LKBk36aCCdg17ZFYq1q-x8cFhfiQ5b1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9446cc89ef.mp4?token=XSAHdddRp4BNft9jD_5d5e3uySBCQaKS6dv2sTl39kNIA6CgxtX-vpS1-80oC0zXEnWwI5wsPeIIASb6F16h5SORV_3OtzbW7y6YdlOUMfMvQbvOssu9NG95gB7wDKWdgRtmewREyc_hUtv3Ph3-4-4I7VGwZwZswRi1OlsQZTIzVdop_mD_1ducS5HepmFFETu1wrLeGQcy0zf4OTMO7T4tBuoyxRcdJtyciGR4nhGvH4OOdeV-YNp7CtINq_j4ps0iqFVsFC7fL37pkrVv_DW46yfZLrtZNRscYlddWRIHCx9lyXERk5LKBk36aCCdg17ZFYq1q-x8cFhfiQ5b1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
راسموند هویلند مهاجم تیم ملی دانمارک دیشب بعد از گلزنی به پرتغال خوشحالی بعد از گل معروف کریس رونالدو روانجام داد و درپایان‌بازی هم وقتی خورخه ژسوس اومد باهاش دست بده هولش داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/30834" target="_blank">📅 10:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30833">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxiiRisr-LSr3GiRLSO-V2xEFexumwt_ie1AKj4OD1ruEIh14yHeQEb5IEZiKVjah_t4YZYVdcT1JgZgaZrGScL3kC2degf8ptELNfeeNOF4IAidFbsXSjD4tRBtfckq_MMypQCPkuzz_srSYy3_BwV5ZH4zJ0FmVJFSZ6-uPJsItAyMtr1k6SC3_pFaWCwfZOYNu17DHyh-fnkhbMiOLI7TxM06LxKJ36PZS2WpAwpOe_J8ClNwXbVI2jCY4LDcDBxK_xag09c64odpiuf6_JJi1C-l_bdqfiKIx8MEwS4immB4g2eu26zQCEatEDcaY4ZSniLKUdIE-S-vtgICHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
👤
#تکمیلی؛ مدیرعامل باشگاه ماخاچ قلعه روسیه رسما مبلغ فروش محمد جواد حسین نژاد در نیم‌فصل رو به رسانه‌ها اعلام کرد: یک میلیون دلار با 15 درصد از انتقال بعدی محمد جواد حسین نژاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/30833" target="_blank">📅 09:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30831">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1cd6a61cf.mp4?token=G0Pac9qk_HzEBHh3boERW4zRPE7pMbwZ_TynO_FfgzbyhdB8A_zfXGVBDm4CnOOLmlzmgbDfJapUPiEjR7VhEY1ozzpaEU6tw8eSx2v33xIc8rHhTBvhXznxYPpakbSlg7dz1Cc19UfObQRZpd1MjXFJvGc18FJX_FurTN77hNFJC0pueXbCY52lS3g1QZbFMlfhfRwI2s9mwg0XiBw0BjP7ZxR_xXRHUs37cR2heYCC2J7eIxLAiUBHdKqMECC8MsqNYgSTMFF04wzNeMRWgPK2EW5_ScfMQCNCuTRlQ6WKtnKSMr4PY4grRhESmaUciipMwaMCecMUzs5PeUpNiZGhi9g93b5fU_yu1pk0SNhNwW_rc4C0L56lRPRQIGCmWxKQX4rUM4z9qXdqgHvuNG4___tW2xFG1GyRUyZmF1fKxbWaISj-iDsr7bVyCnrTyrHfa1SkJ8Q4BDcisLOaiyfU27-BUWY52DEfuHigjiAxE8zUq3qz2ETxtLvnCKXoewzbR3ABTQGwKOybQNSA4Uvx8nyQ7GbmS4FkUczGCCmcta1UkhKWMHDmknziC8BhkeHI_mrx5CrrQ4V9H0uxXVP8Qtxb_60ntcXapw-S77qfSbkHsTGv_WudwfFYFSslpS1wyWSsd-3dSyXwiMr1iyihHPSI4zY4jR4Zp8RQ-Zs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1cd6a61cf.mp4?token=G0Pac9qk_HzEBHh3boERW4zRPE7pMbwZ_TynO_FfgzbyhdB8A_zfXGVBDm4CnOOLmlzmgbDfJapUPiEjR7VhEY1ozzpaEU6tw8eSx2v33xIc8rHhTBvhXznxYPpakbSlg7dz1Cc19UfObQRZpd1MjXFJvGc18FJX_FurTN77hNFJC0pueXbCY52lS3g1QZbFMlfhfRwI2s9mwg0XiBw0BjP7ZxR_xXRHUs37cR2heYCC2J7eIxLAiUBHdKqMECC8MsqNYgSTMFF04wzNeMRWgPK2EW5_ScfMQCNCuTRlQ6WKtnKSMr4PY4grRhESmaUciipMwaMCecMUzs5PeUpNiZGhi9g93b5fU_yu1pk0SNhNwW_rc4C0L56lRPRQIGCmWxKQX4rUM4z9qXdqgHvuNG4___tW2xFG1GyRUyZmF1fKxbWaISj-iDsr7bVyCnrTyrHfa1SkJ8Q4BDcisLOaiyfU27-BUWY52DEfuHigjiAxE8zUq3qz2ETxtLvnCKXoewzbR3ABTQGwKOybQNSA4Uvx8nyQ7GbmS4FkUczGCCmcta1UkhKWMHDmknziC8BhkeHI_mrx5CrrQ4V9H0uxXVP8Qtxb_60ntcXapw-S77qfSbkHsTGv_WudwfFYFSslpS1wyWSsd-3dSyXwiMr1iyihHPSI4zY4jR4Zp8RQ-Zs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
راسموند هویلند مهاجم تیم ملی دانمارک دیشب بعد از گلزنی به پرتغال خوشحالی بعد از گل معروف کریس رونالدو روانجام داد و درپایان‌بازی هم وقتی خورخه ژسوس اومد باهاش دست بده هولش داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/30831" target="_blank">📅 09:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30830">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DClDsa52JDds51RDC9lqZecjzpbeRgZbAs0TsBOnH2_slclxctcB8k226GGRHZOAYkdVgJhQTZLbefHULw5REtT0eJ9sBQfY-l28bZE3jl4Yr-uOmKBIRoVtsZKzHH1JMxxip1Q8AEfOMONb7HaxpLBlFDjmahLMNmaugEisyDH_1bssmsv25gVnOy85mzdSIqQWUYKcJ1DCRWj6QH0oTPlevpJdtLPnLHt-RW8IeJTQXMT2_V6Jxvy6cKkebQdyU6GfiH2klOPJj5_5UH8lXQVjkI8pyPL8T43619THtjNJ_N8TR6S1UFh1Z0lI-TxC2qweRIoGt0L5cxHn10XN_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
راسموند هویلند مهاجم تیم ملی دانمارک دیشب بعد از گلزنی به پرتغال خوشحالی بعد از گل معروف کریس رونالدو روانجام داد و درپایان‌بازی هم وقتی خورخه ژسوس اومد باهاش دست بده هولش داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/30830" target="_blank">📅 09:22 · 10 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

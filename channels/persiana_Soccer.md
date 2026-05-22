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
<img src="https://cdn4.telesco.pe/file/jGZBntk1z7E9aoCPAGexeVORjF1OgpiRDnmi9an5NVlvj_2YTlnKEfG2-puF8Nnmmb1ISvj_aer-nWmNIj4k0HgFdGJ5qet8kuzSSJrLAEscalST4fAPoj78qbivSdnPxIeS67weF9XmDDdNlupnrafQDd_O9MsIKrkmuPHbIrHDlVzYi9JQxY7ukWc-NL3CzQJpoWA9NZvcviGxhgtNHhWc3BEGYYW_20su04k9ENODig_S7FWj-6eFqi91sS03xwF3Q6ayY1guSARyrqhPN5x9k8gdLC-hSJ4aN6HuJtLC5v9NKAVDnX8RWVzXDbn7bex14gpML7rIbRYS06mDNw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 199K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 19:15:28</div>
<hr>

<div class="tg-post" id="msg-22246">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfyto_CWiqKMnlqFVzm9kKGRRQgdX12Zn0RPKY3AuZUEFDhexXbJZa6ox25TT2Xbj6UzZn1202C2YMohvUpEKOmV1uj2UpB0feMyoHWPLZXzLNRqqy0PPv25M98stV-fBtKvH9IW0DhBe3tUmAbeI5pYBEZQRqb822hcHgepNqdqtRJXgQPYG8zE-9MNKu6MlhoYza1YKdfHUcGMx1yPIEs-qJF9IGJlo-hSp5chtuNJ8-03Jq8iO0vGMSuwuv3NuqXTIrR0w-E5lkdWswrN05qAMbKEuirggRH_nbw3IPdl4pB1RdpG6r5NbuvVTR4CPwcV99rPPhJBxbcaM_Ao7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
ایوان سانچز وینگر اسپانیایی سپاهان بعد از دیدار آسیایی این‌تیم به‌احتمال‌فراوان از جمع طلایی پوشان زاینده رود جداخواهدشد. سانچز از شرایطش در ایران بعد از کشتار مردم بی گناه راضی نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/persiana_Soccer/22246" target="_blank">📅 17:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22245">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cdb0d3e03.mp4?token=u-O9-01EtuxYh1oiLIqHjglRTJ2djDgGuucFieeccJoQ_D1kTsI8xTw425zEuwohSZqlh2ztrHHddwFDFgjBY9psTn4fBgB2DFFqQdmdxVh673JEHqGH7bX4IT2GD0FsEgCviaOROUTbQcp1VJds-a1yjLYlKD1NhO_EECJsU4qMmQxMSl-GkvcBF6WQ3Z7eeYrgGOgGcLW7qcxMOcUCy2kdZGmUC4NEDGYDYpA6C6v-16qbppFtNQ0MKO-6g8WnovvniGZyqVEqHkisacu85Xdk6V3V36vUWFBngD5dhul8Jf2aIzRBqFuBZsX_bcyhaG8g0a9tk5JJ3lci3crm-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cdb0d3e03.mp4?token=u-O9-01EtuxYh1oiLIqHjglRTJ2djDgGuucFieeccJoQ_D1kTsI8xTw425zEuwohSZqlh2ztrHHddwFDFgjBY9psTn4fBgB2DFFqQdmdxVh673JEHqGH7bX4IT2GD0FsEgCviaOROUTbQcp1VJds-a1yjLYlKD1NhO_EECJsU4qMmQxMSl-GkvcBF6WQ3Z7eeYrgGOgGcLW7qcxMOcUCy2kdZGmUC4NEDGYDYpA6C6v-16qbppFtNQ0MKO-6g8WnovvniGZyqVEqHkisacu85Xdk6V3V36vUWFBngD5dhul8Jf2aIzRBqFuBZsX_bcyhaG8g0a9tk5JJ3lci3crm-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش‌بینی‌جذاب و جالب از فینال لیگ قهرمانان اروپا امسال؛سال‌رویایی و تاریخی آرسنال تکمیل میشود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/persiana_Soccer/22245" target="_blank">📅 16:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22244">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuWK_MJGyya90dKu9jl4xK337fVPM4EGIUlg_HjjD9MpA4uSF-5trAYexxah79NaMItmjpeQpwXxSPB5FF9bQPZOnWgyA7tYaOE3DKVdKv4D-4-1ado9KxpZn3z0ubnZ6jEjxqtFnTk1z6WQ2orCHlk4fSp590DBxzeRyFIvn6CxEU9I3yv7Kug_yIrsDRXgL_YzM2fS5tAlXHKOkGPC7v4aPR5rF0g-9_zTr5CcqPqycOlX-j2U0E8nFDAlceS_W-dih-MmK6Kj2uW-RToMBlbFKBMLpP4TyLH2UrrqlNGTKqdyJWWOvIcWV3D7kwjYRkpcRKamc61L1XJX9_4Siw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شانس قهرمانی تمام تیم‌های ملی در رقابت های جام‌جهانی2026همه‌تیم‌هاباصدر؛
اسپانیا در صدر.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/persiana_Soccer/22244" target="_blank">📅 15:42 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22243">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1vD6B6GkeaK62DLDfOgWB3_20YtnP_cnFCscG95Tb5x5Q7t0ZpArKExp5BCwjMs6TCMwujWtniulm2rUlmOVjD9od2qEEnRwMi9nKJQeF4jC1-z8A2ffcKjU1SPJVhNx2tzfqbUQRDkZN9-MxNFYk-RnzZM0HIbWqhP7gBjZfJ7TABYNhXl_dJ0b-7XHsUqWye8qeg29sMqDJTG2sW4Jk-gD-IzcR6Y_LV4CdnStc1w70zHPfy5rKyhOp9Fmp9hgdsbthoS83Xiq_5WD6D1fKF-y3sPCc5Soh3YjhGP9IUQzKttcVi34fsD55ySfo1gV0suZdAHDQMO14UmPYSQzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ علی تاجرنیا صحبت هایی با وکیل علیرضا بیرانوند انجام داده تا درصورتیکه پنجره آبی‌ها در تابستان باز شود بیرو پس‌از کش و قوس های فراوان آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/persiana_Soccer/22243" target="_blank">📅 15:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22242">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENVP1cJbcN47mhh1YBHzPPzyh3Ny2UL0QybGdQaXGwiF9-UA66FJNZPuO76UAplslcZCT2uDIFFheF082pApEmakAtKn97iRTmPetqmti4aV955vvVhGg1OJh4JMwu5aGj9kPLvpmnfK5436MxGPtNY0rgQpmNdK-rhi-mmJHhGo7PrcaSvf71k_9iEQPBUO_Q8pGVTU4RbMmdzRzVraxsE8ojJZDwsbCNV75yFc77lbFpYRJCfM9DWE8KZsqrY_lJXC5P8M2y16sSaZ-c9MjvCQNB2b-eerlqfK48Rsa7mBMsI-HkKrjvP3yg8bP0iwNWq3bBwjMWmTsyetQsxNlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/persiana_Soccer/22242" target="_blank">📅 14:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22241">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEyKeJebEgefFkaCxtgEkA1lpV37SDo1xrDTTL0zzDSZaZf1k1K6E5BdzkBNtld2KlPq4WFr3N8UhDhigSUsxqqMjn1_HGQnR9kxNKeJRF2-N7t90rt3chT8c4B3ALEDr7bLXctscaDyzm-Za6NX_c72GR8DaNoubSj2Xybk_plyWlKkLRyD0t181PU9C0Gty2lsOW6yCx-ChtFNM8cShWIeAHZqbJTQDGGcuEn5Pr8Hrt9UWlx3MmM2UJVosGkFnJv9SpMFNZUzLclAw7o3SokiZ5qOKGVJ-e0bZbN_Q_R5ZrnRCyKyxU19THud73h5imB0NyrosI-S64XAAB3Xeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
با‌ اعلام رسمی باشگاه منچسترسیتی، پپ‌ گواردیولا پس از ۱۰ سال درخشش در قامت سرمربی این‌تیم از جمع‌ سیتیزن‌ها جدا شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/persiana_Soccer/22241" target="_blank">📅 14:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22240">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uu8-0UGjhbkaLewHhvfUnByqwL9qby5wZfbWlotfuSU9fdOjVGTCtVERGPeTcoprF2rgAPYtBbgezVTYjY3-0L7wzde-dqlIiRDlSk5o_ReGrDoV3H9Eqbt-HujyYbNyqFhKuq-2_SrqbHSYXoLgicsbl_7VPLv-nXpSO9hoWN6KiOw3G_XPNQ-Ibp0VliSE_dQza4wvfeTEEDz-DT8HuTby6m04K4C7TgczmJUH3QU9mWEv96RLx0v26__lDd1yCuYkQVTo0SAA73lJ7-09r_N_Jg5ZELr0QbhCj3LzGE3og8TDYvlxngPlWVweFprdgOYEb3VHr3mBR-gsTODciQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
مایکل‌کریک با عقد قراردادی تا سال 2028 رسما به عنوان سرمربی دائم منچستریونایتد منصوب شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/persiana_Soccer/22240" target="_blank">📅 14:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22239">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gg1qOpK1HQCpFgFC5ch8R0EeWM3aC1Jj5nekXDTk-oQhFFmkbn4JJYTITKO727sb_4iftPyeG2bxNmFY1Qoxhc3PZagTLc3Piq-0uoeKfcE6MpK9UgAzAIuNuLvCMJJ9l6LrR-me2JHjq0mBit19Kx0wGSrm-l1VgLGGc7v0prX5cgdLu2QtyOOowrs6qMMENmBrDPr6C7T0KJCO-aDMKM98X6L2R3eDjNejuAEOrv0cdvRafyI9rG61UG8YzwMHm0qk-T30Mkhx3U9SIBpYQsQEyTqn66y4HgTvTXmyCpPljis9WsK1I-PvI83C5YJ8Tyb5M7b4ounOsM8aq8sbwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
با‌ اعلام رسمی باشگاه منچسترسیتی، پپ‌ گواردیولا پس از ۱۰ سال درخشش در قامت سرمربی این‌تیم از جمع‌ سیتیزن‌ها جدا شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/persiana_Soccer/22239" target="_blank">📅 14:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22238">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-EpLWKuf0SXX5Q9g639JYCYs2WMVjLbHIzS4jIrFdhVGsG4UieZ_CQS1qrSpVzUJXByneCTRTp5rEZwMVT8bcL9_XmUheYC_ztvkeLUzG4CLMuMM9lIDRm4kFhru2-v2gO5RTgxNk-cF-GnXZimYky_6VwoqFeD5U66vSAyhHYrjkWRRA7in11fL_UgyVY-FD8c0rO7dTTPhg0KWo19BpSbhKghc-XeQ8M1O5NXFQNh58MncBuziN2QC9_wYUtNpP1LaKnxl1j3gVZWMPFWc9MhQyltPorTbHuQH_GLIgVdpN2DR1mspXcjac_F-YgQiX9JrKd7EQUSj7E-fet76w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نهایی تیم‌ملی انگلیس برای جام‌جهانی؛ نفرات سرشناسی مثل کول‌پالمر، آرنولد و فودن از فهرست‌نهایی توماس‌توخل خط خوردند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/persiana_Soccer/22238" target="_blank">📅 12:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22237">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6iTacoSV1zuwQsabZSp7cWK4BrheeDLmto6NSLyl_eitLDy9FxG7jxjTFTyGaMsCR6pqfB7TTvnIcTfGBx-YGyJWndoawxmyS-K2OYy6qd1i4S36cUz3csGhgxQhfq1ikPQKmeKlTObejnpHxSEtad-uw0BP02q5Y6CGpFIWuLAlftJ_Rf0PD5Y8rElctU5mkhO5nGURL5F9G2cbg2yprOtPADC7mRioXoTFKRPfNCkrD9F7ayF9WYojeZ4dxf8IcOFOWJNkrRO-_ZK4fuvC-yfQQWrIPapqQp7o20TwjJi1_tXkLdlMHHd6ygd8oKxUW_UJU_W3MLbkkZuz6FY4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/persiana_Soccer/22237" target="_blank">📅 11:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22236">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpdEk8RIsUUp4mbJJ8n2NVWRUvFWBO5HVxl2oL5c99cKxjtDuQNfupxZkMjBunVulf8t76P7GGTLl10fBhmskln8jqURMQdd2BY2w0tn7CSHlSmSUP7mH9xPMfnaAo5bhda1WoKXeoc2QT4ya7mijQLlMnDyqX50yyyj9KogdLAt-Dy6RmgyaCahEXrBvy8fI8XIT2jE_Az9yUXTotxPn4gzJiDIvhrO_x92Nf3IX06PjaYRLSXyjxB6KX594tmgW1HuixbIedO_qejaqs2i37utBRnkJ3GmcqTQbSdQvmsAdd2ShIJ6QF3tJKUqRmg55pTL6Gb4171OyCQYiATbrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/persiana_Soccer/22236" target="_blank">📅 10:58 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22235">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/De8xmqfelYtdE7kAU27yM3upHLGRuIAVu59wPDEBEnjINldTeK1oMdOKl3pkTMToDZSm8OT2rjl1RLFRLmk9n_wcHL8OsECbcaQqcn4BOMKN68OK1kjHb4KCH2ZvFl64aGfx4_UUIpo4-ScdBhUYowIf5DCJvm3C3LAnze9vkStEmbvglIS-vWQwFR27usI05W3BAxiJ8OZDte4jFRcKw3_5FkdI7pto5zUkwMT0DgH3Q5Trt2LGKskP8JyKxp7x_xuFnrNSGEyHhyPhFigNRHnzptFkvpGSLqd86EygEKgW_D_gVrwmaCmvc6YRndFTZLWYDSjJD6yODHty3Y5dZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بعد از باشگاه استقلال؛ مجوز رسمی دو باشگاه تراکتور و پرسپولیس نیز صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/persiana_Soccer/22235" target="_blank">📅 10:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22233">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gA6KKRUXJsVzi1aexljtT9b1dyuuES9fI31Wo_RewXu-HJ-5MQpLOupKZZRaaw_8ZEvcfRzpgkPNIGrbw5yMKg98mndSLP2WTcKBwYgXbfUoL7qeaG2_eXf5VaMQ4_d-Z8fo9HH7iU6PyzZNF1u9M-qtlYjkwzriLKCVhb3I4RNTGreMOeRixL8_SsQUyxqr6GkjEKaGCfaOnsfukpAirF6JrjlKIo7-HZ4Z8P7bRaMQCs4V4qJeoRhj2xKlk6uf6GA_qSDnVW7Ufn5FttpvAxfqM6OitjF_msmU8BNp-fMHrS0yEOyhnmiXV9m5Gt9ZVsN5KIX844hHB0pepobqtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HqicYASW9B9T3Ua0z-s9Q3VVLnasml1uorRuw7W5nJ0QuiCLQTQC8K8aRF12PYIr-cXIM_l8kq1TIcGrQ53b-QJK5NnVPBrBW1QWF6z511HEqnOpVm_SJ8eABnameckWqNk88Z96LAnHKFXWoRLhVO4JUNDiR2rURqGCVbbNRJAOe2mznxJp1vaz93x_NrLNUqj3LEBKrn2m4Q3M_J5zZ8HyHaSOZPfrL5Iu_L7EUNXa2TlNIM7FSq_CiSWnBkPV3IJJ8rmnZ-gxNlg6o6LLwKzEgKnmhWFLuJeYiQFJ1JuNPYs1ppYLRdLJUN87dF9AklKbDhgv_Wkh5K0JD4YhXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/persiana_Soccer/22233" target="_blank">📅 00:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22232">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/persiana_Soccer/22232" target="_blank">📅 00:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22230">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jRrckIYxNaYfaa4JXCJDqIXmYIshKnxbSpRaRcY2SqN227CUrQFHogFEVG14CAj9dTpe0Ua_QdnZeYXqwy8-F6-wS5WDD2FTT-wK8TDgN0WuhpoI--JwM68O04KEEmBZjNtMN1QDuigskpnXeiz0vCfSE9yPnapbVjXqSNbG7oTMQZrI6sA3rqupW_B1wiiqOiGSZTsO8PJjs4WAZMwpi5LsTUvbS0kMuj46ee5w5cET-xYE7UwSGlqrO0wH3VjYZJd-9DgvQ0DMUF9IJ0RwqjVUYXX6nP8hy5pBZo8M04XLCmvLowvsF8YcsJRP3NjX0EPaDaBufzVB9nNebO7ZLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZIZK7PMtCq1XDO3-vpzC3d9WMQjWa3m9UXCRA4Md47dVr7ZfSear9DrVXIoH2m-Me0MSNvfSOAL1JdsifWUxPz1B15g3uO9rKh7Kd9lnd589MRveCbcXHLyDxtbZBNdUujkLbmvgRJtFXlOk-RVdQdHRjj4_OHETkGkWJQtTD_jlQap5LUZbd7WByueGx42WO8l7Rngbds1EWISKdMT-bR_7SlbfV6PzICEkoUtjewUQXMquZTHkhvf1Wyloe7WzxnZxmrDN1XiaItmGwEJR80AeMEh_bzw_zr9oclqFqucxybj8uUehsqXjM1d1hYcXBft4PDYbYlGaMQgZb9HLAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
هواداران پرسپولیس امشب پیش از دیدار با ملوان انزلی به این شکل ازدواج امیررضا رفیعی دروازه بان جوان این تیم رو تبریک گفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/persiana_Soccer/22230" target="_blank">📅 00:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22229">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bg4IOQy0Kd1_9mlj_lfwQpqnrprn0od0z3bqfhZZWs4kB--kCw-bUZSPI0YILtLI01Rz4_Io5d_wqSPBvYay6BBvCRA1QuLBNuGmzE8VMBsBQaajK9DiVxIq7xUCZGM10LIP7FFAi-dry2U8i3oro-MFSmR76tU95tzdrMb3IBgMsxipgcBaHvG8yrEfeVdM6tY4p0PFEO1amSmRe3frBU9WXvC1AeCo_AgqgqbYI4eYcbOgUMmtcmmPerzEP9Hvsg6uFkOxwtxhvQv99wGX7t0l1ihrQjSJ8LLMqagaEg3KgX4Fbj_DAPtX1C4P_7ISAl7n-_zB38zrEdZxGY6zKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوپرگل دیدنی کریس رونالدو در بازی امشب النصر مقابل ضمک؛ النصر با رونالدو به قهرمانی رسید.
🔥
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/persiana_Soccer/22229" target="_blank">📅 00:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22228">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlnjSF0k2tsgKbT2I5qzdoW64vdbAmAIH9yCV_xV9iy-WPTtXEzCiuw179FBsRladpF2dYF5r2BPxW_pJ-iEWYJiq__Mre-YWmst-HXqsL0HXpfaXr8g4nGgpVjO8ETwhAu1s5kRpNJmdBk9DTck876_8dzM8iN7OoR6BaQ8VvdyvhMu_BDHFtQ1pZXsSm_yi6M0OPfmfPE-b8gQ3CQ-Df932tDHzCc00DqTPfygLkp28e9HNsalU6BYYHkTRprXou37c4M19iJn6edZ4lUouHZRzgaMF9gSnWLGocjGBfT8IVa8ocdDGONaTOT6PINT6x7cpNIuww0glrfpBTWrvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
والتر ماتزاری سرمربی سابق اینتر و ناپولی که در دو بازه زمانی تا آستانه عقد قرارداد با دو باشگاه ایرانی پرسپولیس و استقلال پیش با عقدقراردادی دوساله رسما به باشگاه یونانی تسالونیکی پیوست‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/persiana_Soccer/22228" target="_blank">📅 00:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22227">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JimHe9JIaMYKOTnZvCI8MfEeoXoMtoiIRcDfkX8N1_Y0xKXlxOOX0F-_SQPKM72njRkWXN45E9puydiWHp-SsaKbPPMvYQq2wivRDk40Zgi0qM7OwE0dNKZPcgNyDWy0gZ9gTcPllhZ2t_y-VTNixw_iFSH4Y4jZt4xtzeKTVY0pTdsUC0bmVVEjXDlR6ggXfDqJaEU1xHe8-7XxFwNFg8AzIzfIU1wf7aLQMNLYhVjrjru07oM54WC6SdDrLl_y1WLjax6ci95y0j701NUh3nxNWadI3GObLk1mAuCMmZZSElg_EyPMw1rbxdUYoCwrjhbRdKbE1n8U-FIaZj5oWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
چنل ما برای اوناییه که فوتبالو نفس میکشن
📹
خبرای لحظه‌ای تحلیل، حاشیه، نقل‌وانتقالات
🟨
مهم‌ترین اتفاقای ورزشی پوشش داده می‌شه
🥅
یه منبع‌کامل و قابل‌اعتماد دقیقا همین‌جاست
▫️
https://t.me/+XdSZ8OmU62QwYTU0</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/persiana_Soccer/22227" target="_blank">📅 00:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22226">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYXb2qaeHjZCkfZCX6ux_uYGsr5IAM_GzoR4Ydxoncwy7zBGg_qaPKkaU1qKWUBw8qWh9uXBdmeTQyxWb1g64g6zYzzxHKlZbg6jNTfMGTriGyuNuRX8poscqIFISc8UjJXfiH7Yn-D_5mNgXMm5TywAF8X_MeIuEUqzVulGqYwWfNHfYmHziQL6hKlds7HwYa-2My0NBHgxTOoeir3woaUbN7mDFx7WHNltQ8vlEAXSRVcoA_DpZoUhq5Sed5yjWWKd95TC5Mf7p2k14SHH6aRR8sKl1-tjuws0X_3w_0MVH8qjFDALntB4OrRChl_Lv0MVt7sN9Tvdtybzg6cfwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ النصر عربستان بعد از هفت سال با کریس رونالدو قهرمان رقابت‌ های لیگ برتر عربستان شد. قهرمانی که با درخشش کریس رونالدو رقم خورد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/persiana_Soccer/22226" target="_blank">📅 23:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22225">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfQ3fHrwdAwA7ID9ojM92JvHzuhT4bAVFOXpkKmJls4NombMD2vXcKEQ-GxKiSMdBovAj3HzertCMsWSpzrdt4v27_QIlLIPrfKXXE67ej8ZnBcreENOGDaebEYlbFfJbcikIIo8Xr3VNUSQQGryv4dNu3nxtcYXHpktT6DkWKjbWuZWSxAb8KHu1WXJJJO-KgMUbiW_FVXP9FSjGaFYrCVh2boSdjpLgdiqxY4wczNAfxlOtgf2nbfdNidgRDW9HIk8lp0TwNU7uR0H_2eqRlzCUhrgYaK-doOdezuQzAjh5vEvddqEJJoqa5BV3EGMCGG_VDsRG9Aonoc_uete9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خط و نشان CR7 برای رقبا برای جام جهانی؛ دبل دیدنی کریس رونالدو 41 ساله در بازی قهرمانی ارزشمند النصر در لیگ عربستان؛ این 973 امین گل تاریخ دوران حرفه‌ای فوق ستاره پرتغالی بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/persiana_Soccer/22225" target="_blank">📅 23:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22224">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d569523e34.mp4?token=fxq8cCUzCXEN8KqEuwAikAckESdhuwLLcwfOmA2_-JYPvR0bLOO8HxFSTUGZdwvXW4LPT6m-ervpBsEgR9gT27LJJiyu45H_AOX_y7ONRHX__NOPnYfRXmryE_I72d38wA6e4dG1UuJkzvtivUCUEL-nlyEnSWwp8UwfZseUXDlHGUTEAq2gY05TbJqRWoMzvcGGeNdVnXGkcURbpCbp5N8nkK0TiSaE49XL8fMNF0oDIPAWr_mKj8Kno2vs5IhTrW5KFsC6aZivPIr-2-_JwXFQF7eUhrr3ufOW1lY-kaY8HBTevP0hI2b7vejnb3zNDnc6IYWNLH_BDDtL6ejbqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d569523e34.mp4?token=fxq8cCUzCXEN8KqEuwAikAckESdhuwLLcwfOmA2_-JYPvR0bLOO8HxFSTUGZdwvXW4LPT6m-ervpBsEgR9gT27LJJiyu45H_AOX_y7ONRHX__NOPnYfRXmryE_I72d38wA6e4dG1UuJkzvtivUCUEL-nlyEnSWwp8UwfZseUXDlHGUTEAq2gY05TbJqRWoMzvcGGeNdVnXGkcURbpCbp5N8nkK0TiSaE49XL8fMNF0oDIPAWr_mKj8Kno2vs5IhTrW5KFsC6aZivPIr-2-_JwXFQF7eUhrr3ufOW1lY-kaY8HBTevP0hI2b7vejnb3zNDnc6IYWNLH_BDDtL6ejbqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپرگل دیدنی کریس رونالدو در بازی امشب النصر مقابل ضمک؛ النصر با رونالدو به قهرمانی رسید.
🔥
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/persiana_Soccer/22224" target="_blank">📅 23:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22223">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/908ff057fc.mp4?token=U3JNWoDuDTTayX8AZkq4YboJGAA1cnWQRMNc6j-maTc6W3HDK5WQxtpal-V_SzJbGMAfCDb6PZ_Kcu5hpaMqLHrqZg25WpFFhRHW7QLK4xswmJe0CkenH42nA6jjOAkF0KJqtNBkrozkFU1_uT_TbFDIuMBgc0F_8kd_UFy7YbLL__VSV94gYIhCbBbrwG-VIguLStdtE3IKn_SrEayqLQjA6yYDcuUaX5S3_ekZe_Il2TA6IM0I4pX5yjFhbET45ExZq0XIlu0pK8e4etTwb-6-cGuxvGAg6X5DxBFkHNSaMuIuuY2PTyOigdXO48t4fUSMxjaYhmslSMtKf-0NjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/908ff057fc.mp4?token=U3JNWoDuDTTayX8AZkq4YboJGAA1cnWQRMNc6j-maTc6W3HDK5WQxtpal-V_SzJbGMAfCDb6PZ_Kcu5hpaMqLHrqZg25WpFFhRHW7QLK4xswmJe0CkenH42nA6jjOAkF0KJqtNBkrozkFU1_uT_TbFDIuMBgc0F_8kd_UFy7YbLL__VSV94gYIhCbBbrwG-VIguLStdtE3IKn_SrEayqLQjA6yYDcuUaX5S3_ekZe_Il2TA6IM0I4pX5yjFhbET45ExZq0XIlu0pK8e4etTwb-6-cGuxvGAg6X5DxBFkHNSaMuIuuY2PTyOigdXO48t4fUSMxjaYhmslSMtKf-0NjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درصورت پیروزی النصر در بازی امشب مقابل ضمک؛ این تیم با کریس رونالدو قهرمان لیگ خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/persiana_Soccer/22223" target="_blank">📅 23:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22222">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YK4yGsyvptFLNMWGOl4v9acUO6qHC-hpSPttlwkQV2kTNVejJ-RveOkEWWjxp0PPnIupEnyRoZEkWDU7qZvPUnCNVee0BD8CzjKeVbybwF4GahjqyxesuitIzJ1tuZqgcjtYB2EJVk6jxjxD9h_aeAtGouJ8JKtQ6UvPS6fD1SLbRrhnVsW8xxGRypKtvWq3TF_N_Wq0bIekeE8yEzCSsjx4zrDs_asB4CIkZpsCveBPuW3l8zOXpq-WjtMi3dzlbuzs_3Lqi-wpD-elMWGkE5cmSxErD22IzMX_jyszM7epnppfcMtrdotxl3zxqw0vRGcFux9GllPKNeVvgYNBWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22222" target="_blank">📅 20:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22221">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
آفر مجموعه سوآن وی پی ان: ( علیرضا )
⭕️
مخاطبینی که 10 گیگ کانفیگ از ما تهیه کنند گیگی 185 هزار تومان براشون حساب خواهد شد.
⭕️
و مخاطبینی که 20 گیگ تهیه کنند، گیگی 177 تومن براشون حساب خواهد شد.
جهت خرید به آیدی زیر پیام بدین
👇
(
@alireza_mosve
. )
⚡️
𝑪𝒉𝒂𝒏𝒏𝒆𝒍
➡️
@vpnswan</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22221" target="_blank">📅 20:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22220">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtlVm1QYfhNa3KWryIxcrc9NmTACIHB4-IO1Se7TnR3CuJQZRyvim9uHtWmEwlTOBYWdhkukBAkQCTr2vdJbDaiTS9Vzrlqww551k2zhXlbeqlJoswjkOdxDSUUV5ZAQMJ5NNsSDVIjXIl4JgjjVI5h0wVr86nVK6HBjbWdF2aXapGvyXjWUO-FA2MvL3Qm7Luj6qAYKmTWh-Tj1O8awszQYMciPJVn74szDD3f3keT_Ar7TS4IcqenGJpN93U1DoNPaytpFNBSULh_qK4SLC8fD53sMdqPjbCfBJT3vgryngv7IFu7Wt54xcxkc2Bpr21LHuBRhGq45sWfICjY4yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام فدراسیون فوتبال؛ باشگاه استقلال مجوز حرفه‌ای خود را از AFC گرفت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22220" target="_blank">📅 19:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22219">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYks4UkYvi-xSil3K6Hb80jV-hH7h9__1PGF2CRPfSEgSNHD31zZiMdvgH7D5yiiidsOEHxb9vnl4lA_XqK6NGFPpe4mNPnzVZALF1wxti4EQmYVhp6hdy1nK3zUzcseqUyYgCP3doUxMNuWuGsyEhzmhxUDRAzn9u4cJ2VDXklWtT48HenLJpgtWgl5J9r7ml_UwsHbl4-c0O2KcY3qlBcEq_Yd7QUpb-LtIO-wiFdW_c4n_VC33_b42kl0P74SZypZtzBLRfFBLZZs-pgivokVfp7Zt0--0JpBkge4o4qtDCzK43eVuzFHaBRtQsTQkazhpS-s7aEo4VX8rCP9sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باتاییدیه رسمی کنفدراسیون‌فوتبال آسیا؛ مجوز حرفه ای باشگاه استقلال برای حضور در فصل اینده رقابت‌های لیگ نخبگان آسیا 2027 رسما صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22219" target="_blank">📅 16:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22218">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hv5YpdoUclf2DLsVguk6fNwwkPRC2Es3TGKhTiOND4c5OLZyh6ZiiDyn8iXaEPlijU3nutHhepGemT5s-392f0YaQhlNsYo7nZi2Jl8lLRDlysv39E99_ZAOMwGDAo8l9y6L1yqphZo4zKcMaCsk3iSOVrpB3RuJKAM1AjyP1EO_rjDLnz5M4n-FZEu9Glwx8iq6S8RLakXWgXZXdNzRCdDFA6fP6g1oVPZv_ZWJ0BhHei9E3epRB1ayJS4jHxjgJZ7dF-yeVgSvJB4LVwSTxWpdsNVa8z4mOm5tIxpfaY2zDXYic22jjHkdClC93IFnVnvf7Q-A0UC2OVOU5jDpaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22218" target="_blank">📅 15:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22217">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0RDDxpbUBcacsDEXWGZXW-tc7fXr1Jpgu4sOENaCNELFrCCAnpRtF70z3CKeqSAN9dxNp3l2IU19oMh2_2hzziBELzhi5K3qPaFVVkc-EkmQN5hm94JOnqHNqNfNX8LWECPs6TH17x3eKWv4UIIy84XqnkJ6-HHaV8JYOs_OPh7-Pwx2VZ4vWZgL7beX8K1cJvEiaWcUYXqN-7fD8GI-nndnUNHsIW4_oFMNUd2hR_75qE39gF6hVuIHWljYOiP8ewYxruX_b5k28oZLsrRY7WAIPStIvq1JC3Y212cqUZziRVViXSjECkt3Hs4V6D63icBTK8h5n9DapGUSMopSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قهرمانان 22 دوره اخیر رقابت های جام جهانی به مناسبت چند هفته تا شروع جام جهانی 2026  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22217" target="_blank">📅 15:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22216">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3vMFgAmKsYAIsaeFYMFh1KRISsW_xVaVk_IwcEPB770zusdv1tXQY-pXtfHxsNXZL57yXAOOXtWMsJ8tisoGrOFWyHgsTUD3b35v29KOo3Z9acUNSil8qI1u1fGWazwOiXeVeFajER7nC6ezfbvuKr2uwzevqQ8Za0gPsWN6MdH1pPFrHm_r3W6HZJtnUhnSYPfH4FIhp3FuWNOW0cgw3mR0i28TEKEBrWQsefiB0hX9SZ3MXgW-UdnG0Esd_TCecy7vLEkoL84-zfWhOzxYFNsznq91B7_YELmWi0kbDXoO8Dy9kgs_EAMR0D8u4G9jtH11Bey9OeuuU94gn5UgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بیشترین حضور درادوار جام‌های‌جهانی؛ تیم ملی برزیل با 23 بار حضور در جام جهانی رکورد داره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22216" target="_blank">📅 13:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22214">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nEnTV2O0z4KZ5MulsXJQ-nXCN_52z1MuErezVn5uMmk1K7vVdD3jb-M3s8e-D0AJ7U-OGxBoFnasqRxITwYcgCNCeN_Cg32isNSGa9SMFPDOixLXUeeVlIxkyH55CXsr2sjGFZLk_Tvtcu5MUNhhyvVTef_SFxBUReHPlSHaFbaqbPngucE3qx-ywrmG5FJU4n0fUp8I9HtIk_PptKoxJi1RFmhqmKX1LTIDAPRd2mIdzaILb8mw10r6n9YAKXMzbeR0jP27fV4Zr_HKTGicpRbZU9A-zmaiov2tbRHeiJv84xYxQAVPhB4nyIvBDJTrU1ikpwm71xA5yfoBGTQP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TEb2SoDRVWaWCOX0J5SRnBgG2_QW6AUWX1bVJYg12829DwgZlu-VtTV4bGKHZYxMqXTD7jdhszgq613-6PonLolCKQ-S2jO0yLiZ_KC9pqNBrNor9JO_0Vb6N6ML63i0y_nWk8o7nn2RWy3r9rvdZh7WQfOAOp3mFaX5bKktKT4JSMQ0iItAlvzpOci1uyuYK6xMl1Iga2ByeOGQC5XF8SkPx21RCv96xOQCvBF2i_wHrfngpPjnbzySQ6pRo-tunBEss1Fwa9zE1RSbznSaLHkhMKySRNWnTL8GbRynO8h1e0pNNVjO5PDRWpJlMNZSfz4sIqxkfx8SqjZO_OIvXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
🇧🇷
همسر مارتینلی ستاره‌برزیلی‌آرسنال: رویایم قهرمانی آرسنال در UCL امسال با گل مارتینلی‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22214" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22213">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBX0LEFz7weFXZSgLiOjC16E2Flq2UuLo1sKhgO7TIp82j7lC7Ca1CjBwfTjNT55ncYxRZiTDjLADT1Mpeoh5YBT8thwNP3-pUMsNPuEm5lpKcwot3s00IqJMzjMQsl6dZzpCn61Tpwb_a2662jzJjIHTr1Zcr4AqPlcUXoCCnjoCwrzvTvdmoW9YljzCWw3beS8KqKh_bYUvljJEveoMsktE8cNKNz4IOipF-ZQpOG1OSlO28Hbj7vrsZBmm1BOVP6465zvab9DLdPJsgT7IkDuEibjLKfshQLiyAvDubfGg-C7utRA8qfkxV859YEvtkHnSCGUhZkY7-OBv6O4Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزبه چشمی هافبک ملی پوش استقلال نیز در تمرین روزگذشته‌شاگردان‌قلعه‌نویی دچار مصدومیت شدید شده و ممکن‌است به دلیل پارگی رباط صلیبی رقابت های جام جهانی 2026 رو از دست بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22213" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22211">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOU1qMbPZDydHn9kB6BVyRWOHEJ1ao-urnb4NcKsKSy2S0qt3aIwI09tE9_B8yWGarbuipu8_fvpH--YMLZBNnH1TpQMbEr85G5E0C2X7CI5IBHPaDUS4XpIZrIEpCrikxaRiKB8MLEJvbNFC8jGZo8gvatdC5j8ROKLqEPhBnKssnrAWBDX5QxOh6Kflc4Nir5QzhBQV78uA_Q6q4Fyy7P4HeqaKNJk2hrna12ub9ty69IaLljda-TuymEwwo1X38IzgB32J6_q5cINA4dXH7AonZTP-tcD8vy2TCi2MoWFHdODe7ccPMljIOEnAN2oYg15q-PDsJaj0ikbfqnPsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بزرگ‌ ترین کشور های جهان براساس مساحت؛
روسیه با اختلاف در صدر، ایران در رتبه هفدهم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/persiana_Soccer/22211" target="_blank">📅 12:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22210">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1hMJKNeV93V2Ao4XfzZ12PbvxjTnnmOYm6gA94gg-Ll6R8VYBvAkOGv_Uf9koqHrIIoSXamOWv63NEc_J6EtFQVH78CgxfFRgOK3ZeEHqofVHyQ6rhamJl0g1qW6qUX8C92rjGZ14T4FNkGEnsLq5D66B2djknxR8dx0ZLy9np4YrZ7djwudstxRbhKQxUlSCCmWwh3o7fRbzITvxn1tAPupF82idUoDWHHcDrFjULnPJYyXK0pLeTGI9DOgG0kT8vbkZ44lWxdcEjz2pfPiHft7FsyiWtTw4ChvOMWBKsORJ7iw7JjevUH6GnOw5ZDC-aGlHqf3tl0LZHu1Ei0jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/persiana_Soccer/22210" target="_blank">📅 12:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22209">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lClAbhLtfVDqJb81WP6LFp2cipbVGbRz-whM4ZrZ_zosjstN62rXfeYpWyaWhGsAo9y--b-IVRgPgJ7Uhmw7ItnqKZp3CIuo0hRbYsAdVmfU-T-X5gzN9XxoevoWlzME9FSHsHr5RScnuK_icLENb_m3YaU_rwrRTu4PBBUcxhnJzMBlPZFYGKtfpKxHHqtr9Fv12bmL_dPGdvwbklkWs34svJVqMzn95nxRVtTuBzQWZ94O-sAJNVblZcfhyz9TzWvRvhc0qC95xM1-BJexTX9pssltqpTK4aiT5WhEyqQgZyC3iwNN-lU8LInAnyRgIorWht46MZK8ro1orsGNqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوستون اورونوف ستاره ازبکستانی پرسپولیس در پایان تمرینات روز گذشته تیم ملی کشور از ناحیه قدیمی‌کشاله‌ران دچار مصدومیت‌شده و ممکن است رقابت های جام جهانی 2026 رو از دست بدهد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22209" target="_blank">📅 12:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22208">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kX1E48H6q6NUk4Fd3n8avhiT04RpLCKMU43YIdKEM-ycQHTZVUB9U5ssmK6_0ZR4rPDcr3gq0mg8i6yeN_iL9VEih66QAIMzHUgkvyWOOdKODUHtSd3MGos_UEIGcdzAIDC2T2fifONDFAg0H3BI1xAEdCT0qde_5yxyx9NSqlyfUIMEG8X5KtNPq9Hk-TA7i7gnSI49lgJIImXcsdnHVbzZu8AB4nR9Mm4kV9D3EvjFExZET1sGRqS-JeJaOpe8IDiRqk9ccWJG5SbqDAT7cN58RKEGP3IsF3DcOr4mo0UdoMfNvO_OtJiqnftjwv2XPHBHwT03eBlebVfSBnUq1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22208" target="_blank">📅 12:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22207">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-JauixGHvpFMKFXECPThDbat3wj1w1UtUbU1CyS6GbaiCrLgcVXxww1QGjDCDoR9pyEFDVjdz6dlgFobxuFmrCSg8-qR4WEZl-PYRrfEMH8y6heKoAVl9H6RySmrD7uJJ-MSz_eXG-Csu0UKDwGrhNojOv6STvgHVl3bgTicvzKqkBC3sXQCO17JNCR8uLE7rVCLYro7KRmE4kKI2SO_S2n9y_1IVdu9j5jZ0YDd7E8kXYAheDLviKIG3tg0mprcFCiiG4dxWpylF8oYm4jduKGdm3cVjOhtS7LB4qRlQsw_SBoC6o5B1f5aXsKBdZGyQ9I-KdKsiFFY9_uMicMsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22207" target="_blank">📅 00:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22206">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDlUk6rvoW0CXQkGz8tiNI3_P0m_gJCLTtiB60EL7m1D8T_dx5l37CBNkkp7gHYkutgsWzu9F5jt-AvVKKegMjsbuIlQ0Z3NerXpAkZ024qki78TePMlrKkVKcjmk2XH69qQHDdxlDFDQnNQAPfi0aLGaQ6VYsBshq7TCEG4xaQ1rdBkjy31QAgX6fWsGGAeltUa7hVzRrVb8U7xiRemBd-ZeBu4xkiFC0MnMFevkme5BSLt_MiJbXtS1wJ3bJSjSKNcbSQ889sJ8J8Zk64UklumFFlClE6qwDE-QEvy8jbuNUQjHNVvGY5Tuw9UD7YBZlVFc5IHKC_AdGZLMlbyfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22206" target="_blank">📅 23:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22205">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGePQt4zW9xPGNUa9k_V-DM6zGh5Rr-fC71N-i0sQAgbIGwGneNM4HZePcp12aIlnCI571hzYVXjC3nXONI5uQ8d4x5XvLhC9SOXsVpNXoN8FHFwMTijl0U7Eet1TLAr1Hv_4m4hYfL2I1B2i63q1vBvgy34J2Qo5RkXUxnTwwTU_H0R-_xvLUU6TdzSEQT-ud8POCdKY9JBaitc1-h1zVwQXWFR7Fu1XE1d_jk3Mz62XH8R2K95FTq3Ff3PXW0pEpP7CFdskQD8lLneDY53hpmrmzrSvhEXFjt4EwA6PzTbaw1zVln1XoT0qmV3jjHMG5bGiOf05BmcScaQrBJCHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخبار دریافتی‌رسانه پرشیانا؛
دوباشگاه سپاهان و تراکتور بشدت‌دنبال عقدقراردادی دو ساله با سردار دورسون مهاجم‌سابق‌پرسپولیس هستند و صحبتهای اولیه با ایجنت او نیز انجام شده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22205" target="_blank">📅 23:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22204">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OeSHCyiY7JxnzCs_2payCcdaXWJUKzMtVRhDXEstzvwZVChvCSTOurhtqpa6fMNEllrdHAlmLu-GWyLTGtTO9njaPNRhYXVDWQz4vzqVo4NdP7OdIbV9zVO98QM_QV2j58ExDvYgoNJrgxvgh9RrQ2PCCMKww3rcLlWiEq41Ci1WIr7Nud_LpBLuOzs943LrFhqMMn1_Jd2ynxbLH8FT_R-Eu-H8xpyUYk9YpogJv10Q19-FmWS5ZPq5bm0cI6xEQVzoJ1klJohmY0ffbUTw9rcMtwzFOcV3tIpXu1up2GUKL6qlwINzSdHydSnVU-LCiT-FOymsJCzo9P1FFqsDcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22204" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22202">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4IvX6Ya_w9VaCxHuMHBe2JFexMYJ0VlcXFBE33uR-tXkuZcV6c8JYzDgYEtKoPE3sacLA2Dsc5LSx287NQsiGlYTQ1NcS6BDwImlgz75tSk4XA52COiNmMzz8Wue9S0WWpdaLA161dZEr685xYA1cbZm2rQsO4uGdChUZNHMy9kAbNCLoofaJpxzfZx3NhzZFc-l83dMINFE1QfZW3CbzHmGpEyMvZ0rs8VqR3NIKzBq2q-QPSvYsYku0cVz5UsmqlHlToq1xyDdlpcoVMK9PTOD1wn5nNsHqlnxb6UvBF0sgxFJq3gpc1XyH1tEY8fYTQNNrFPLNQW2UWs4uxDzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22202" target="_blank">📅 20:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22200">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O9cYc8HQhDfwz7vqn0NoNbk0j8e50Gj1-UBrfnilyYKvoQFzGLJmIiDYR4_Acbxk3nNYhZNTVz1e-q67caVeEKqx2d6T0-Wcn9bzTgeVFHJbR-wzRqoxBoz_QgWLlhEKO2BJQS9muJcLwH1OAm4_qbhjv1-7FJWceBxWJBZFXW3MaaHJVWkWMqaKsZx-7vl7WcIQhjE6_kgm0FLg0Qsah1w19lZgdRcxZdSWbThy_ciwO5uA_8mWcejZ0towWVBNjwwFepMCCJ0MXPp-XPn0Y_vZoXmieVe5JqBTUXfw5DU3D_x2dsvkylERGbufwbOiSQhIfwU3YpAfSTQmR507Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HfcnvzeMMWWGguyeIRdWn9vTWQYhHV6FCKhOEUbopKtayMTDyP2sHTEPzoX4UWkJh-kUmJNL0R6mdKYb5EZ0rlB5_5a7YT-OHpybvhECWpaTC33ywMkLpNFbDaMzSBPdwbnQbiGLhor8M4k2-Lo1pxATNQ7SLI2dVrDWpSQRm8W34_LzwxNZyoFTT8EpZmfEGFynKY4PUWOFKu9NdpjkP3N6acyUfADlRHkDBut0cHTcU0_HzzQ6MHYzljCfh481dQwTRgoNqzwy8gwODFdXT-2Ce7bHpF4ugcp3tSJV5uUX-rRASe5Q5e9UqteTb73d8sPpPrLL1hJPg_OHMrlnFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22200" target="_blank">📅 16:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22199">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dc475c66e.mp4?token=B57Fnb8YG6r_3w6okrRvIQjSCW1oOpqOzy1_xEvRv7oH0N54k74F3_O73DCibA61YhNwXaNr2fhRHDJkBRa5X6QjwFwQfr2fq8KQwqx2B1yASaUzwdKoxLZyecbi8kwYad1UEBqMUrMR3Kzfmn9TRdGpMucxv6E0qkfQJVCtDQLoYzq77IrjRvIPwBswoqlc-3Lq9qcPFoYyD6Q6qcLfXSi_5dvbV17aoHqoUV8LJjs7a9vTlrjHeL4LyrksaSfUYMmOMSPhXQtYlsIQaLQe7jcAxwCJetz29GhtT2s1lGfKIodNsKy40-Yiuh0H086sDWcwCpD9yKDh60E2wTsaDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dc475c66e.mp4?token=B57Fnb8YG6r_3w6okrRvIQjSCW1oOpqOzy1_xEvRv7oH0N54k74F3_O73DCibA61YhNwXaNr2fhRHDJkBRa5X6QjwFwQfr2fq8KQwqx2B1yASaUzwdKoxLZyecbi8kwYad1UEBqMUrMR3Kzfmn9TRdGpMucxv6E0qkfQJVCtDQLoYzq77IrjRvIPwBswoqlc-3Lq9qcPFoYyD6Q6qcLfXSi_5dvbV17aoHqoUV8LJjs7a9vTlrjHeL4LyrksaSfUYMmOMSPhXQtYlsIQaLQe7jcAxwCJetz29GhtT2s1lGfKIodNsKy40-Yiuh0H086sDWcwCpD9yKDh60E2wTsaDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22199" target="_blank">📅 16:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22198">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntNsieEHlq8vvjmK76WwNLsrIr6IclxNcWaqM2dbUPuTQD7I4wUzO7pwG4STJ4njrXWZi1ulzXHQlIvV4RzH8JT8jM2ayjR5s7I5-gYU97lPk6s0DwgSh7WA8-20u8GQqUYlZRUU6z2DL2Ysd1W-sF9w1aHT0aIgSMAr1grwQmEUcc5nBbkjn1bWee-GrOQmyCDwxkKK8IR7_dhNvIri-_jOVL86wexF8pHcjE95zlSnobSrlBXjl7FW_fj5E0LHuI4yYwdPM22YBtb87p7VaoXUabyniS_0St2PNeoFnTlppXPIoRq-DKYYEqXDqWhVb7LrDGNOy6I3GKShBYuUkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22198" target="_blank">📅 15:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22197">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">▶️
واکنش‌جالب‌نیمارجونیور و همسرش بعداز اعلام رسمی دعوت‌ او به تیم ملی برزیل توسط کارلتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22197" target="_blank">📅 15:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22196">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">▶️
مهار پنالتی سیدمهدی‌رحمتی گلر سابق استقلال توسط پسرش در تمرینات تیم اماراتی در دوبی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22196" target="_blank">📅 15:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22195">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oy2wWDJZ8WA1zeZLfYdrcdkzKasVPakWTk2kedGMtnvve-11LHxTtbO9oH9C2VvhK8RyXBnIeDjG0BIgKwrvv8CpOr3Hkza1xSKIKe5UIww0Gt4U0QrKOikWJw93EeumaK7Ixulm96VhwbszcwvgUFQ8VU5jG5MWVNJ0gGWTn3FeshMsTf0kMbagGKuKKTV2jAuzNzo0_9kvdZK1DorkOfY-69zp75TS32goHzf8Ms9LwcXCaojw0zRcVQ7JlEWt4Kpbx5aY1Miif41WyySLYgua-9M7yTWRvL_D3tiEh7N6SYZlHXvrvTsMKxwSy0A14j2x3_ad-N9A6wQNYv-YiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک‌ترکیب‌احتمالی و پرستاره تیم ملی برزیل در رقابت های پیش رو جام جهانی 2026 آمریکا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22195" target="_blank">📅 11:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22194">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLzlwFVs5CGAxt9wqjAKLar0caLlz9Uuv58_M0wEbsbkibiD1jLhAMAXM_-ZEsAJMuFsRqI431Y7nTv2cMth_KROlnwlXKARyK_NOihpHqUVa76sYPOg4PcfHQGUXG3nDPtU14O6J3rhSHiByCLLcbKONsoiy1wFw5kwMJRl5EURl-0ErlFUER7WjustdBLIfByNa9n0sW5usfTadw9jw_j5UBJd8-yUWolz6y7kLfaJwDob8WsLc22CG0ppiBhg9uDBiRwRx726byp3UWsDNQwUAr0wcxG4kVARZJzbD44vdnm3OVeVM1VC8JRBJSQR-8es71eZgIbCVuXBycvhZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22194" target="_blank">📅 11:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22193">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/La32mngOKLG0Oy_vWH7Z4LAmrX9JDtZnA8g3ik-WRmkny8Nu9np4ks9Q7CDZXjCIU2Uoxhv_D8HwjHAxdrmMC4VOE3t-m1bug9ZWxpWnfTHObMNhjJn7nIDUJlDrygFQqsDx8V9GQJP9mxbg-gwlfUFfsoPtyrZrDk1aSpMUUyMDsRhBSSHNd8j2quvIrt_RyTGnOWjEcBEZ6ZSLk7ESo6C3LYyyUoZ_BdEqxwZXS08hdC-9GtA1sD_QwAyQo9AoklcSZ-2VVcw7w7G8GK59ORRE_hSFvg1ARHoT9DdxKhnsMJ6KZK6CeA_sOas1g1Iazmbl1J82XnNqXo61iZjRDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردفوق‌العادهCR7: حضور در6امین جام جهانی؛ لیست پر ستاره تیم ملی پرتغال برای جام جهانی.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22193" target="_blank">📅 11:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22191">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YKSdOwvx0APKYgtQ5hQNs-XIj9Jubpc8JK4HVQz6nxym7ewQzGhULiwi0Xq6Lg9h2rxM6TfwcsojCVbq5c-zxERWj8aL7cxhOS3dnoNIvQbm0tMc2SS-y9CUE6yaVaU_GHrxE0fd3W0vn7En6QSLh1zD0m3wxulvs1F6YFKiNwxjTbJHRLipfC9nVJR7bZQuxGsrIOFhLtUYDDNHcAuyYtvcFr9w6kC0ggfxgyE7MS4D8g30oyNYpBrQpKZOD3dNx5WuNvgVW9RDh-pSfeOWlF3ZK7-t_sCVSxvxPAPflmIBzhInE0RLtbSEx8aWr5OR_6ueV41qOAq9e5XRUurLtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q5eL06af3yzAvJoP-LwUsy4fEklmh0KfjrBgTKlPEsRsuF-06xI4D_-k1KZZTgq7AwBWjprO3oHo5eMjUprJ55HyruQbzbSDJEIUMfOyVNcURXyf9PKyVxBIxet8Vhi9VjPSKOjdmzAkT5Yn0TalD5wRmwJkkgY0Pgw_uAU17spU9OrmgOvAsbYeHJCLEYl5k4PJAMFz1O6h3pGVugtAWaBp2okfp5kikmWPGuWTZ0nm6cpkrV18yK6yTM5Cn3UzGWTsnMpr48-9Br_pkXszx8Nqq-zluFuZNT3TW6Qzrgy36ACQzTeFaHD6EoId_3OnbLmcP5oFbd8gNYZt3xCddQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند.  با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22191" target="_blank">📅 00:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22190">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzYqyC1vL8pUZdxr7XvzK8-VoALVFmv472emVhhjHxeyoXz5Q24EMW-wGwiUbpdQ3_Bih8j-gabgtPFUWgfpigOJvmokvnFXV4Xq8fuXoPU_gFcnvWcFwap1ytrwQAm5K91hOdDMktFTXgchwcXX2snanXaY7DPbWz0BjAc1n6VoUonkdhligucIMUTvwfU_ceC79GgS0_RI0XCDEhmTkVQ9PVU6UpveKCaAoK-6VB3Sp_-bPAFglFvQXfQzgD_Z4zSFOiBgA1y0FnEkjqCOjUe-4bBMfmkfO1FmvT8MSW-A1IFdO-MNUf5QWTGnMZb2ZGAm9FJX6HzD2wL19vnKjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند
.
با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22190" target="_blank">📅 00:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22189">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✅
متفاوت نه اما همچنان‌چشم‌نواز؛ رونمایی از کیت فصل بعد اینترمیلان: لباسی در قامت فاتح اسکودتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22189" target="_blank">📅 16:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22188">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDAD1cXE9kJYGVbpDSWIzHobiReaJLohdWQWjgKCI94zXM1-C203zc_67SmKhjgdoPKf6iuf97W0CL4E0VhqHLIJKjGBmcJxGbmuYXMFX7wH9mdNvqoMaXjWW3A0TvyBMZ2gor-EqW-Rs85wGka00CejlpWgUDZXuWYGx_jNNpRdisfBw89EOmw-iMAT8PhA94ThLLqU4kk69XiqRFfnH1LQ4HKItnRieHwama2-ryX_Njtbwpm64q7mxbRAhFUU4H84PNOuCyjMPwEfmxiQDSbHrBYWegUOu0UM2JYTVITQp_SufAWsIs2r0lifYyINW8yv9TdpHy5YZ4zphst-3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22188" target="_blank">📅 16:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22186">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFgBLNrq8jOJ1tUKaXQvA-oLg-jFxCWvG0eFWKWzWDNRORAZcRsOrvhpT582qoESYLoDeatx_bwWSRN_IZ6jKB40O2pTcysyaL3Ut5bs_fJu3CjfrCcoz-0s0HzInPXBanGxjWcl57inRJc7vP7CvgyweaHl72rw5SCFXWaiB7nV4YoGDmltTs-Trostz8IDrQLNOXwGux1BF_P2g3z1tXIIJOt1q48oeA5kKGrhez8w3OEaB53zjyToEbhIZ8uHLLBPhWePV6zY-_AMAFVK14tkwpbSoOR3z1wmowFaU2eytZKMWXpieLFy6zG79dgsTNjuICGv_cDVYMNDb4PluA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا
؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22186" target="_blank">📅 16:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22185">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rI2-dNu_9yZG8Ce5nuSNFS5eS7BOgHnNUi5Ym5t-Bo-olg8539EHK5g8u9EvmgBKnL6HHosZzhR5AH54uTulYak2LEJRj8Lj2i5ekFJMdHF4Bk34G8EvkbH_mOv0Ynv0qW2BN-kcdffqSIlS8oD10nIN4EUSLRU3H0A4masfH1z4qXQs6mqlPuvcJ0QbEKKDccpd0QWzHeSDd-flbt7x-YX8D5tJHExTAEiVFzeKMKt5apDmlH5O1GbdBVbOIJfMkzQUCeB9XxT7dqA44fPanJDg-7NMudUEX7rAXDSB78b4zBRZtZf8OOnAy_C3GSyjDLy2TxaJoeVR5419wQfBTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22185" target="_blank">📅 12:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22184">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7duaZpbJboOAuNwBIxRHMb_rO-A4g0oMcYCBXODvx4M0nzLP0s-Pb31YIVZTT3AWOZGVtfIH5p-780yo58ZImMo_7BPuAK5JSqAdph3O76-YxrFvTsYTAUAZFb-EEtmu1vijtnx6Urr8zUWGXFugux9Ga8uzS9uO3YoMhQ-qdEp4xL7docCUsGMptV595MvuTewJHAYaH8V6fxBQ1sgbUyIzHTj3W-RuG5XhapyDAh-bXrgTR5XsXxb3KihLSjkBZYoN3C3DLN4o6TlQ01TwF6-9MzFOkH3Rl8ndi8yJpVd0ID9PVvvM6NaQ4HplA4J-Dd1QSeBpPtD_r4E6UeJ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22184" target="_blank">📅 12:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22183">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7621338636.mp4?token=cU0OZX41T19gMRRZLzf3JacOmq_1lyxtCXj1UEbeB1nhrR44uWR3ch4-qTge1EQ94DtpZQyCNB4PVYmIja0Q--IIzMWeF6EHJG0Fi_a1aawQ-2woNs8BH1Viy-qVxkkx1nFM59YTkS8BmvzZ0KX7WKOotRWYFlceIQAe8IcdHgd1ouVecDaroddwb_jKqwGHsU6d_10FE6zLdhwEyoKZfbEZJ4WZBjwEOYUJy05a_gV47VjUGXJgDYren79mYd0aPke7aBvrQQyA98K-q3_6NVBs47PCiD3sIE4HvKyv4hkTqTs1R9HZP2AbpgVQ_cUQkOToGAhxrGk3FKdYH2-A2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7621338636.mp4?token=cU0OZX41T19gMRRZLzf3JacOmq_1lyxtCXj1UEbeB1nhrR44uWR3ch4-qTge1EQ94DtpZQyCNB4PVYmIja0Q--IIzMWeF6EHJG0Fi_a1aawQ-2woNs8BH1Viy-qVxkkx1nFM59YTkS8BmvzZ0KX7WKOotRWYFlceIQAe8IcdHgd1ouVecDaroddwb_jKqwGHsU6d_10FE6zLdhwEyoKZfbEZJ4WZBjwEOYUJy05a_gV47VjUGXJgDYren79mYd0aPke7aBvrQQyA98K-q3_6NVBs47PCiD3sIE4HvKyv4hkTqTs1R9HZP2AbpgVQ_cUQkOToGAhxrGk3FKdYH2-A2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22183" target="_blank">📅 11:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22182">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hd4YIE5l2XSDOLv0kQJOoZoPxPzGXNU3CssKBwT1vXI2n7Sv8EjlCVhBRzS0qV9WlecJvRVlAhlxHI-KnvgG29I0xN8eVXG2jy2x8vTD0AXWX6wZsluVZ481EpMdWCCHZR8B1LJqoOt2sl40eILJljTwTTwjoxw9MuEEv8Kk59EqH5W15v_932py2JquWCDDGdUw4IVFHIjY45V7sSHyxGL_5V9zC2ibK_wIoEDIMeX3Fv9WSP9Wbv63s5k349TEe8ezI_Kss7B02lcNrxOlZtiJ4pbEUNt-RDopkdh47W5O1S9PX3VQFOnIu3oUAeuCXC0FVnZ5R5_9k0rzxPpbSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ پپ گواردیولا سرمربی سیتیزن‌ها در پایان فصل ازمنچسترسیتی جدا خواهدشد و انزو مارسکا دستیار سابق او در من سیتی جانشینش خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22182" target="_blank">📅 10:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22181">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSjUw1oSayBGTPlehubFGVjaoKLjntChijreZwN58c_nuVylM0sOvgmMD_VY3q9apN6ahnJF1jKqW5qaWpoPgzjqaYm5kISjIgjb_zUy1WrLCRkcDithNydXC5rb-Py08GvamG2v2CMRUBvzfoFyYHPNrdtxj4dwUBludJVm-5LeIhrTbDMOfzKgmDWHLVy1Q9fu0JrNof2Ytl179eukPwxOD6vBaBBLJYtC02-7eL3cMfaAyZq1fqzGnQz0zOHeSc5rnfS3i-2A5rAlylj0or16lzqevi7aJTmMoURDAA4MlARFrUofqWN9xNWcK43WdGFfusD80th0i7Pby0iLUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریهESPN: کارلوآنجلوتی به نیمار اعلام کرده که او کاپیتان اول برزیل در جام جهانی خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22181" target="_blank">📅 00:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22180">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6ReqmwegtHe4Xyvro5GOGpSFxdi5ckyvFC2CJEuUrfnT8qAMXLy7sRdzNI2Jpd1mnJBwhx1_XVLbXxtDdOFCOwU2wiHi3WyIZYsDC3lHJW3G62WsLp39UaKazIy6aC8rlly9cScdmadn57WvcKRSyXhLZoTyoddnfyw4gJaUUgX8blH5-JomGq7ZKP_nm7L44vvWuwukSm7RLj_hTDkc4zqyxil8iTcFD65uBAx54CHVJlpv5IM8ktq2hyibQFfWpfhxl-B3EhuHpGZitKan5JLd002jGTZCw0GRGp4qJYJV8KO090IKwDyXd_i0G57UqdbLVlclal8m3kGxboF1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22180" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22179">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9FmWIAl7csxgetH35QK92-4YF8NYH3AkDL4RB2vg8pwUFvhLvGgNpLXY6y_ai53wg2EN_efNRyjE6wYVphjaFTASvSSW1fAZf1zsO9D1bSwvFcqoyT1EQzotC4-2nPG3X4qcwA9Sw2PwaRXumSRQzRI_-c2EKIQUhGXh-HWOEzLL5GJS1Cbj4dY7RqwCDDwJKldC6CR35eCGzvInhu4Vdm6Buajw1gGdtdCbFNiVuu5tk1UOTnYGZZI5zWusHA65eJRlmm9qxpeINmOGV-8QmFN7BjScROiaV4HCG6tzW42lb4rIotURtUJpEKf9qKm7hAB95G-l9Twl3qnOajMMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه جذاب افتخارات پپ گواردیولا و ژوزه مورینیو همراه با هزینه های هنگفت این دو سرمربی محبوب در پنجره های نقل و انتقالاتی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22179" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22175">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jo-X0HCtkacR1vfCCbtyCaG5V4Fby8aQ2P1EUWcLeorxzXP0ZJQDHjQGsZjct0VQfQ7zTOv_6G0DuGuhN-A6xU247FFMK8JNVFmD6qemGQVzGkMD5xdym53eShEs5JbfMuYWHTUnbeH4d2ji_ZJ-YehDJNgHTB8IwoYH25N5ZT597jc9Vl9IIjBtVTWLRvcsvsjR2VdV99GIoOxjYDtO7VZXwN2TZEZKkhVeN5ViD2s1GMpmBPn1JS-Zzp-7hm7dUSOap3x6bUP1gFDDaF6DZeSfTNuInmj7SSvE4qKQOjkvbf9LpUlnLYCP71n8EeHLuCy-deyAyQoxcpvceclVGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ROeJCgg-QiVYhw5i6zCMh28qeaaoScK5oaVCuWams5JLwlmV6i0xDwBl73qiKoeFIvIHY1xAvOtN1CbsB2T5FPio7NTjz_G3Oz8UMoxygr6x1hKOZkuS4Nmk49VhFhiiPQFB8IC90VKYqucA8YXUfAQI_NIYZFHKVD-pQdpkhJxhr4M5vf3Mr4lRrclrumg_6Qm3LAh27hIHtCyWWkKXOCya5riG7ZM4zrdmqM8s2f69JqEPWcDBBFGKBln11ehA-9JBwsEZUteGk7QzQ0-xe0Kxl4vqE1jdxDKBJL2h7njDY_R5cDapUAPv5xg-C_kp2jAl1q-rTBSmyvPQxRcz0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
مهدی قایدی ستاره 27 ساله ایرانی سابق باشگاه استقلال در کنار پسرش میلان قایدی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22175" target="_blank">📅 20:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22174">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8Y8Y9_wZt53BDaUeeE62td7psJaYASvWbpsQs_7U-jFa5LyRgBxrTPUC0fnu928D--vMhuJ9ilmOeSDhOjrG5iTffjagHsHyKF0VWx_m-_y-_YUdDkjECJs5pxGuIthIZjgksKGqkknUd5dEL7l_aBjZhzKk2kru_VhE6llAQGq3qCco3lxk69sVl-YPIgla3lcBtsVAghd7lMssKZ_yAYtP2fl8no_MnQu6K5PJrE5Jlgq8hxRT1HrkCz-LYSGzzRQuo31Xv-PBNvBCNP0JF5bcq4r4jS_DQ7KEXyz5JtdrOdErgut0VDjATBYjt8vNXl4oHyUMbNQXdu-ickfcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22174" target="_blank">📅 20:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22173">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPK78K0MkWcZQ-9hXoTVD2YEanFiOs9uk-rzKM2xVSZKXM3tIHedx7e7K34CXkgn-88DzVaZWY-pl3xizrt2xhjvqI8A61RF9eHe86bWVgpMnfwZsLUtSqDiPTK1l9lQXkk5bAsu65JR8cT0Ypg3jYtcNMFHpUxwPYTK1NTv-Rlfv-jPen_FCWczmU4pHmYmruPaB9VPLuoUM0D5xft7LchMGx72SZxdCQ_JueGJoyXrBHCVZTYl3P1W5MkX6vSEYdbP67fI27uBOqhjEpApssmcPUeZYxqvYsdgxCy4boTUUZxfit9hDmNs1BVP64uNT3Hc6H9x9xSR3D28_fSOhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22173" target="_blank">📅 20:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22171">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKWgVadkWm8y6cFN_W5CiMgmsKILGOeP5P3x23_vf-YWEybzSkOqAtSYBUJXDqtyUiSXw8jfMnUSsXWbU_uuHs4uwD7Wlxp_kmSIEdkXp3f7CtselGR8TIpFgpFkNCDsNocs_ofQVaZQ-mthrxHByMX7oIo3Xzjfkb0tMZG0cPHTeAB1FMLoGokFtn4EFkhnIaV5VXUkiXVf4Fw2j4JsJiHAx5bGY8BTfhxxFvnR8QnzgQ8o0wjKeUKJ5BozFtQXAWzU_OnDCi4Fe571wAPHvfnH4fU6_UguJQKst0IbXCNQTHDL84R3_zVlIRIqtzj1pNACiYNDbWtyTPfOuxzbhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#تکمیلی؛ سردار آزمون به نزدیکان خود اعلام کرده خودش‌هیچ‌علاقه‌ای به حضور در تیم جمهوری اسلامی نداشته و برنامه ریزی شده پست دیدار با حاکم دوبی رو در صفحه اش استوری کرده.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22171" target="_blank">📅 10:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22170">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841076b140.mp4?token=Dw99tOnH9uXHs2PXAH0E622pqnqYMvMgNiYXSLJ1jbQzaJZ67DN-GjMleapocSgieyr_ySuyfZY8XgDfEyxv161OdLJpEknMH-1iihiPhrmZhCNa53A5f2TMFV0hVtZckDUhXHXKDABMfOXwK3TMrOP9E6dyDh-jqZna_TvZm7YSsCubVimDjCG-H9Wle8G6gsB02e1BHizysD_E1PnN0TJMS8pSxaE1ZTnJhMdCNmI5qdkdwmG1OCB-ASqKuSHl_DAiLy6AE-Ni04DWyDpqBVaznL0dlc8Rmwn29BQRxvM0hJigqONuSd5MhsMMEbVlhfKI66cvA2BKDDpvZk70Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841076b140.mp4?token=Dw99tOnH9uXHs2PXAH0E622pqnqYMvMgNiYXSLJ1jbQzaJZ67DN-GjMleapocSgieyr_ySuyfZY8XgDfEyxv161OdLJpEknMH-1iihiPhrmZhCNa53A5f2TMFV0hVtZckDUhXHXKDABMfOXwK3TMrOP9E6dyDh-jqZna_TvZm7YSsCubVimDjCG-H9Wle8G6gsB02e1BHizysD_E1PnN0TJMS8pSxaE1ZTnJhMdCNmI5qdkdwmG1OCB-ASqKuSHl_DAiLy6AE-Ni04DWyDpqBVaznL0dlc8Rmwn29BQRxvM0hJigqONuSd5MhsMMEbVlhfKI66cvA2BKDDpvZk70Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#تقویم
؛ 13سال‌قبل‌درچنین‌روزی
؛ دیوید بکام آخرین بازی دوران حرفه‌ای خود را با پیراهن پاری‌سن‌ژرمن انجام داد و از مستطیل سبز خداحافظی کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22170" target="_blank">📅 10:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22169">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=eSrsiVKI45lEicU3oOx8CzV_XPaunKKCu5sr-cg-TaSyCL_5IgQsURhwbHyI742DbErLKTFQdb3IgOGNoOla7sXVKeCfvxmsmug91uEmmCARninw5DnVJkIAFDTd_GQ9KBLTnVu6FTniaVv4J_QtJkX_IIqIpe9jB-fGGjXhs7S0gUnipjRHxyqfrUWAhLFnDzSl5Z7PHFLiNMMIRQp21X3NCIuAOWGgzAin_rLof7tHGVMn0Wt3Oyc8EHrnazFzz9IupNrw0zqRF0_I_Qcm8CJ2lqDQb06pmTJNa9YAUwTnTnPUPArwUJvi_QeBrHd7NvTim6-QKisncMXIlxWUOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=eSrsiVKI45lEicU3oOx8CzV_XPaunKKCu5sr-cg-TaSyCL_5IgQsURhwbHyI742DbErLKTFQdb3IgOGNoOla7sXVKeCfvxmsmug91uEmmCARninw5DnVJkIAFDTd_GQ9KBLTnVu6FTniaVv4J_QtJkX_IIqIpe9jB-fGGjXhs7S0gUnipjRHxyqfrUWAhLFnDzSl5Z7PHFLiNMMIRQp21X3NCIuAOWGgzAin_rLof7tHGVMn0Wt3Oyc8EHrnazFzz9IupNrw0zqRF0_I_Qcm8CJ2lqDQb06pmTJNa9YAUwTnTnPUPArwUJvi_QeBrHd7NvTim6-QKisncMXIlxWUOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
لئو مسی آرژانتینی در صدر بازیکنان با بیشترین تعداد بازی درادوار رقابت‌های جام جهانی در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22169" target="_blank">📅 08:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22168">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txC-HlII2km74Wyx_E-qGCfyJf0hMCjU5HVjNAq-9dgpANWap0oy4ooBg9ZbsOOkVbKKI01zvtNHgaXvmI-c_5N3dAunwtWxWIvrhx8aY1MSMTUyFSeF_6CGl6oIVl2noG4-TChZbNZWXZs3Ggx_MuMmaTqwjuWIKd1JbxWTHYdxIE_REneuLUjgAHW5hy_rKwLIGn8ZAqOgQBnlNGfr2QRx-KtjcRBSI5MiiPA8RlO_Cp4vLeuKLAgt2c5SfuIOGuw1bZe8Wb59Hsd56d01TFh_FaUVFT7_OMT965xCCAEMiBf2kOYe1utoLEXdyOkOxLE6d-18EyQo5Zc2vO6eJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#لژیونرها؛شکست‌ تیم مجیدی و شاهکار منتظری درقطر؛ البطائح تحت‌هدایت فرهاد مجیدی در دیداری خانگی برابربنی‌یاس با یک‌گل شکست‌خورد. شاگردان پژمان منتظری درالشحانیه‌برابرالاهلی‌قطر که سپاهان را از آسیا حذف کرده بود، به برتری ۲ بر یک رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/persiana_Soccer/22168" target="_blank">📅 00:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22167">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N70viX_q1fHbnqxm4IbLZWDonZgspF3pKga5auizXWiVGxOLZCrUZY09NNVKJXYrWRh3wDnjC5U2M_B8O-i_ye016iGZT2IYCDbEkzdonmBYySUJT5FIXlnsXLtymLXWPn4in9JrsNoHmZsE9TkixiGRW3GjZ16BmjQQk1xC_9JiWKE4zLFq58dA6SXaa84u2CJG1Z8rX_esbZHayDQU8NJdcciCkiVns0EFtp9WEK8bDW7NnN-zexfLEJv_faIk_ZQZ8_P-AI7kwghQtrYM1mMsX2c7YeiF8WvndMyTBJ9_DsoarlKiJGCtLoe-eclffu1d1auXXnXZ3RkzBnMosQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22167" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22165">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwXH8fdalGNso-LLVQ0slU5cJICUyWEPRMB6e6FKDSoAAy8Zu2XYJJVELvNVlm19s1Wo4jvZE732RVkyoAwRhFyrfgbPLJbiUYsN9wJjvQLdw7Vlx8J_qPEPXG60vbsZ5eENqyDlaa4ycRJSEPv-aN2I4wILfdBnwTrh_RR7RkP_3e9fUJEG8sPwbRj5cXhq8wRiR5PBbw3dbtFgX8Qna5klnsmO91p9kGvV-m3OIPUQ6iETV4QG2X6pKr5xwKSQo3K3xkIQGSt2DkjSKzmfrqMkZip91jSvm9Ka_XIadQiw6rZVTLG5XcnAmeomJKYVMWm5o6YBLNilE4wilQx5gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در جدول نهایی رنکینگ منطقه غرب، عربستان در رتبه اول ایستاده، امارات‌دوم شد و ایران‌بالاتر ازقطر رتبه سوم غرب‌آسیا راحفظ‌کرد.براساس‌سهمیه‌بندی نهایی فصل ۲۰۲۷–۲۰۲۸، ایران صاحب سه سهمیه مستقیم در لیگ نخبگان آسیا و یک سهمیه مستقیم در سطح دوم لیگ قهرمانان آسیا خواهد شد. این در حالی‌ست که‌ طبق اعلام کنفدراسیون‌آسیا سهمیه‌ایران در فصل آینده ۲ سهمیه مستقیم درلیگ نخبگان و یک سهمیه درلیگ‌قهرمانان ۲ عه. باید دید با این تغییر امتیازی، وضعیت سهمیه‌های ایران به چه شکل خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22165" target="_blank">📅 20:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22164">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXCEs-3G6_falQ3nXBrp93AapTsuhgZfGLcTpbVtpC-klq3353QCZpycauwB43eLmvwCKRj8OjBAEkyzpzIC__fJSk7ODwTJte2hADAFUAlAlgvvKOMm2FnD7hUJ3F2gFfegTSOW3WX4PMEl0zoU5FsaaQPlWZMdd-V_mrIOexsi76xT1Szlyi4P-bcO5M7vAiMkGF6bEkmG9ucwsLUKMdAeDqLqyE0SgSBQgOJA089o3JfMPEYuSjeBy82m9GuVsyz46VBwONByujQZv4pk79KKf6O5Ah_vJ6tAyjOLg_eG0NNEnTicnXVgJVkOHDdkj4YnGDfRQLsfWm13lSWcpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22164" target="_blank">📅 18:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22163">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNitFkMbEcxSv71HoMsRecySfam1PbD1GanriU-Ghtb90g8BG3mBwyw6IIGfO0A0emeLfgQm46ucGfQdyaAvPrc9Z5uXntpKh7kdg7-vV_llX0IF3Sf5FYqgUVPg9g0eX_gNFUhQbISk05n7EWXfKFmqbBTE1z0HYV8UTEqPPXwBHJ6JdCEK6lIctgGJZlFPWPimi6EoB8AhR0qWLfy3J108_r7Gv-B-d4xemm3EubsZQ8gE4sfgZMXF036_Poh9LaELYHgYpybQdPPZjddjISXFQx0X3UCM_WoR8WUjSfLFJjXgrI9E0i5p9bJ22-_Vfee9XBRTNRWuMc4petNG2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
متئوس‌کونیا و کاسمیرو دو ستاره منچستر یونایتد و خانواده‌هاشون درتعطیلات کریسمس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22163" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22162">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwJLXtUoe-WeIaZnKl282WrxIEZMNcZBEG2wqS21Ny_9OT-XjNo8O5HnOU8iv4-QTrOWmQv_6qiOdOgVNOzstMsEzekBYf93WRXdQI-6R9um_QHjRA2JpROy6vGasplH1W1EcmBzg4YBDv0pEdVUT648jIlQkSPSj9ZcX9n6TUKy1oGMPFrQkAHo89llf4FrgRVVq8FP7XcBBMS7jrOJVe1ELE0PtZ82yMfKCdTl50lle8K_YdoDUVGMQ_wnyAwHFKIIRaXLwLl6Gc9HAtP-L0BmI7q80TyqWNB9wH5BASUHdx9DtP-Xh5GMUv-rl2aCBMffD59pHMufjs46L4Ugtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم‌ جمهوری اسلامی برای رقابت های جام‌ جهانی 2026 به‌ تفکیک تیم‌ های باشگاهی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22162" target="_blank">📅 18:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22160">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wo29QzNo9Jmos3jdOp9kdgKtXFjLbfSoSY45hJeAB0hSTgY_cPokQ6zfg5jjzaVpygQd9i4L7uwd9-SC57VXiT4mh6TiVEH8Y6_FFMmAN3UK9n0knLdNmnq0Eok1z-Tdu3UhccqHIHTsYwUUeiVI4d1p5NpYaLrCkbLstSaUS_DGeWW0SOSzfXewMmfVkSA6eCk-GcL_s4lob74ODGEP38NVeTfSxuuwhVlIiOTkz0ldoL9a_yffjXRLIaVFbPsyG3JcnpZIr2BwyyJLp5FpKL4SetXH_2qQqC0v_zZR3Shc7Znd5xH7VOeGdxHmNTaLC5mqexC8QxQ07ID0u2un0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22160" target="_blank">📅 13:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22159">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kl5RJpGe24AM3z8IhL9T_HJ-kD8aiJKCTd0T2J9VP6DQTfByAmA5P4iblXr5TZNjSc41gKJfZxSkF_lSgknqxu1qmg7tkiWb45g_1A_6lgEVsb_3cGJWZoQfWrgJVtp0cDc9ZF1_YjZ36Q2GB9ZpMN0x88gU4w0l9mBjPqJMSCIGMj0At_5BjgJHReTy6XMEV6GRcf--bU90Ro2iekrjPHmX0qAzmntwoY6WKWEQAfZC0_pcdiZMBRQ_rqSV_V_NF2bSQLQVNBkRWn1QQ96A8cjUVDS3ocv0Y-lo8YoKxttI_8A8nCdJCkZaZMEhrksh7syEaacL01oXNLVxK5Hviw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22159" target="_blank">📅 11:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22158">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFgGobxVFDFW4k7hQtyPacq1V7wQfvETiXLH9IEhx9cWWcZQ80zdEoR4Kv_VNdSPeCmyGND7Qi-nijrUloDoYU68I-J3FljYvuaf2-gzto8n28xIoCwYYcOcMfevhWzs2KYmwjCbes9ay2naCYhMcPuj7dEMlEqBfBNvamden4DHhH4qonffZXTreVrKcAh3fpQICN1q22mFJVmUXDqtTQUwVwQoeOI8HT3UuLV_mI3yLhrbn6O6IBh49fEMcXLamQAJTMYkk_8wRnBEVpSVBYsDYgTy9-T5Dh8t6pWEFXpkryYNFaLzgfLLv7NRBFcBzbSKYwRDhcyQcAZyK54W8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22158" target="_blank">📅 00:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22157">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGqniC0HtB_N0TeD3rR9lZ-gmr6dFzM_tFdqsVUKNyDMth6DZkKQvhOkwf4VL6w0Ivx7ob7Y9vqo4iEurCKfW44mjV4Nzh-qX2_uAMnmrnNJzqAjzZnp0A49J4Gjib6_Lk2vUX8yEHUs0W5LkORIUzSCaFqZnt-5dcCXz4sSempdrqPSFuLFcOP4HtynHXDysQj8e0fsGfx_wUmAHvNddsXx5TIyn_sG8uQYBFVyDuxeSCBrNKG_VqslnVj6OT2ffkexnR20Z8HCIibwHNFFk0sgNXqOIxE7ikxZEtxqLmRRi8VQcYq-uQdZ4cmwwiRYetyha40MHoAJNfxfouXy9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22157" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22156">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksvvnbPLrvgJCdxrdGaHBF4oPmlGWRpaCVEncpObYGeRCQLo6aXwzhojOuVxGmI0LGbOfNUnptkHT72PtrtkQL_9kSFfPnEXOgzhVeyJTqu7H9Js9C6sJo5_rQAPOz9ibex6Bu1_QkYV-IiT0xrksnH4UV45VzhsuFd0J7j3W84kXUiDXmbP72ZM9eJAeRp4_9AcDLIxtVjcPUThJo5vZoA7M3yXQxQkG9zhoky5WFPq58fC2vnixLsaYsdiaG6xQ1pLmRO2TzSSzoap8LN-Akk6dQvIZ829qA3VUKXQU3zErSON2bjlbVdaA_Eyd6-RWsCL7ckIQVyDFSLAWX_yKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی: باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22156" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8z7SPU4Sv6eTNVeI5GKf3F2GVaB5fHAjFZ0Tr0C2ls077bhhWnuX5imdEAFU54uJrVOB-YQ0PWY5QuEaUjUNzX7gTKmAlADCat-HNXYr3uV7XYGK49kRsrtzQq2Vfb7Z8aflgzZeWJ-O0k8iH0tmgNJtAzAeAvKOfk12nTrs71YOJPSepFc2w4HywnqjGYtWzz0I_CYWWVxEhn2F0a61JUVjwdMqe4gSGZo4o2JO8WaCHnElTHKGgSe8LPtkv9aTVrWA8lSdRBXm6tMTYHU21hR3rXAFW1fES-pFYsX9NnpV-B7NGLplXWt7fD4_fYm-_rxwMqL42yr1lc_a-r_Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم منچسترسیتی با تک گل سمینو چلسی رو در فینال جام‌حذفی انگلیس برد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22154" target="_blank">📅 20:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6yEOlI5RflJsH_hGMGoY7dBsZpPvU5Ezrk1prbCmTHISRc-fDH1rqYYoGMUjs3H72q8ILUbpJLRCT3RXf1YBL08oVuD8mkhSzAIhNpGUFlrBwb0AfPA--qELQdHri03JirSGvsCgRQKQPGw5E24UDgy3b-gfnCIwimHLGsu9xSbT6L5sT3BWn4V8Z2FcAsUpmv3cNJAGRJ2FueME393XOPw70_sY6EoMXOeTnJYjxHc69Mji33gsI6lcLo1jSXbpcYVJJpIlEukBHkXfpGxMVGWMak1wXyKKn1kw28FaeaQdKeKXkUuIHdPm-FRRrUS83SRt6FTBWoyVaA08W2NbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاکا اسطوره‌فوتبال‌برزیل: اگه‌اتفاق‌خاصی برای نیمار جونیور پیش‌نیاید اوقطعا درجام جهانی 2026 بعنوان کاپیتان اول کشور ما به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22153" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22152">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qP3e_gVshMtvxrwKZOruK6Iif8eNWKr8xobAAGugw6sunWnnlXF2v7q_VJaxd8F4jYcn-2Wyrx0yYg8BTU8ZdfJPPKXAtnbLAQ4JQugPcZ03LuoCQiFUDkG2roSWCALJ6SLm4l-9FSgR6BuI-ec5ycUPwI5owNdFhQXDNBhurZPl_jwaKQ8ZK5UohAe__s3q-EuSrWUZouJHwSccjHaOntQDZSuc8d1UDWgM6r8WfFaTdp9AFqmyOtqGjlwXl7oHWyUlR7S19Jjr5o4K5YfH6U1FPB9wKAOfhDDUw5OqHdpgWrEvlsg64wyKYnBR53GegojhXeON6m_WlkhNJprx3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22152" target="_blank">📅 16:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22151">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uk5_wXy96DxTcnm6SSnMiH8EG7NtgK7aIhNJz0_7YUjour8anUO6TN6nFmX9fcVcsqmdrJHYthAhYez63iAsLZsiuFUHzIMxlcL57Yg-SjR7hFvFqFsz5rD5L2ylNxu95B48mULtNT-IpI-ZvkuggtawNpEwxz21QSc-tU3sHd48Esrs8FjOY8wLc7FGlRZmTbxpgAGlcK16KO4IE48jlqMvx7t3yBgafllhC6-WSe9SxlYw3kM7riJDgVKEOB68YnbLzDYdxHq1oNtmBkdcfmwFd67YZpcU1ubwmIt1Ib4MflNVXqkQCwO9wh10MafXZx2vKI2sllHMmw9tFDIVDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رویای‌فوتبال‌دوستان:خداحافظی کریس رونالدو و لیونل مسی باپیراهن‌دوتیم رئال مادرید و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22151" target="_blank">📅 15:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22149">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjaldY-uOUGpeZKE9ZcvOAnkPkxUMLE1PTey3-LjCyBa7TqkTo564gRkC1RpfHmqM7MhmJHRuPO97qDDa2XHfyrByyoS1rHmFFeE071MGEAdwNHgngXNTwnn7A285IkYk7mrUgqvE_doPOqs6Y2ipZFYI_qrR0nqTXjDbN0G2KEtgDXUTELUAw1N50LHHgBQkXuL3UBVENLKdljX2liAeV3KNlvQISe4yvIjajMq0NHC8bpsLPOJXYdGMYEZVLbI25pJZSl9B1hdbPne1NgFhBlLXnuDUpquTMhOOkSzjwEfdabvKXSZX80Z2gWus2msZM6ZgHqdY__ft6SnMYvrnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رابرت لواندوفسکی ستاره لهستانی تیم بارسلونا اعلام کرد که بزودی از جمع آبی اناری‌ها جدا خواهد شد و فصل اینده در این باشگاه نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22149" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22148">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdJKmsQwyhdskiOAUKySlG0ImvLgfXb6VV9by-Ow2381n-H5GETrmf2acZG0lKs4feii7PzilrKqeHxh3E5cFUwVxeEH_7RKBvjDgzhGhvsS5wjwn42lvG0Vw6AdMrkPGOnrrqsEZ39w-oNttY2erLaXx8G02vqDhAZVgYePURcrWDvjUctRXHkVrFrI-y-CD2KGnf7y-I_IBe_4YViYxoPOYDk7Ic93r34cIz8l8Qz_vG8UuStul1cUUK_L-jc6fgoBYoLhhdvrUQYlH6rBivx3vCaAf1mGuyCsT4-A-F3VwKn-eYO_l61L2lZ1L9_bsIfMIZagTNegtZIwLB4Olg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22148" target="_blank">📅 15:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22147">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsdXtj6AMHVZKhTrK-NFIIZ3VagjY38DClIOhX00xfkp0TQHBdPkENUjvgQYxTbNdv8Cnsc8hEAc3Suex0oGYZR8mCJNEQes6Usjos2W157mtp17jNKL7QluYasNr7UfHbG-j9ytG2LHJC695ssQKjNPSBI9-sotodVHivIrD0R4Y2HIA1cLwO2nbU9m2HkjWV7ayw70nrkSPlylxLtO3jzYKe_zFO7EbAQdct_wLk23h2Z0bhlh-Tj2Z53_CwFaCz8B_jtV5525D29k-opBWAMzJZghz4kjPhKsSQGneU-XGR3wNb2us3v0c1CYHeQkytIRMiS9AChS0Sm7BlzepQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22147" target="_blank">📅 12:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22146">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0YR8vOFrf-lGKa_lEoEnZXNOi0lLJ5Y1Jx7j5c4W77bGLKMtl4_Y0rXNfAAHzEBa8QUHV1jk9oW5X9sQS5QXrzTcOOOx0--mvJHs7HirykouATwChCiT_vQ33lyCkyYIS7fvlGYMctRdWw78XrV3csZlohWaMVUGwL1vaRLTpnAm4UBencSHj9Zn7Xt4HRZ_169M0QgRxko9btMCNwMgwhITvDuviEZ2S1b51YxXLJ5hk6nK2OnJqU9t-F0x8JNgrX-nmDaqvzHfNX6spbQiUMqxr6Xvg8oA-ija_AQ2iY-5wU8BuePq8LblB4pokxj4pmHoDR1PRWf6a8u3l2kkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/persiana_Soccer/22146" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLisvWiAx70zvkCUmW1rDAZYhV9bQDLB0tINWZYDZoYZ9bBpFy0rhu56cmBJW68Cjp3ZgBlbV83kfkOu3g5MZ7bD9IiJv6gLdjnctjnn0Do64Cz_sq20PP1PQyyFtFx5CY2Lje7ZnX-_CVIae5nSkQU9ptoR5dbzM3B8YJ4jOHOAeqDjFFFIJqMih1fbRkDCLzf4tleytKyempJ2zN9csVy5xp077FL5Gh4XG-070lJjX7JsbhyRSv-LDTBOSjnbCysXNbG0s48m5Lf7REkkJWPb2bnGC115HHg0v3sUyTbSAzp5JQL1okmMk5O5nSBfFTo2t4Lbx9v1fZhW6blNuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛اوسمار ویرا سرمربی برزیلی باشگاه پرسپولیس بزودی لیست ورودی و خروجی مدنظرش رو به مدیران باشگاه پرسپولیس تهران خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22145" target="_blank">📅 00:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22143">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⚽️
معرفی تیم های حاضر در جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22143" target="_blank">📅 20:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22142">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESBy3u-5doTlMWLkwE0dCM18cpjWurXyYiB5T_1tUT1yYstER-di_Imh2zqFkFHWi2mleJPuVHZLtWp9Se0JXYUJyQ2iumvSNt_Gt119VXOJzi754-n48ITu-vU_cbHoNHqH8KAMhhgnEjl1a2PzAwygqPwWv-B_-mTqUIh1uJB4wUxN5PbrKWyXRtaLqkoHh-6TwQ5huSmwOI3uzFQa1pf9UxVP91ZD_eudl1cAMjAFQDdWLUzQaja6xBOtS2C_kgm_zq2AgrmZTTKGzVAyM8bRzuoSlBbcRZuEhV7CM8Ac0omtWtcOP6R0ikgUoSAltTzH-XTq2bG9eI1FjeNbHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
مانوئل نویر، گلر ۴۰ سالۀ تیم بایرن‌ مونیخ قرار دادش را برای یک فصل دیگر با این تیم تمدید کرد.
📊
آمار:
✅
۵۹۷ بازی برای بایرن
✅
۱۳ قهرمانی بوندس‌لیگا
✅
۵ قهرمانی جام حذفی
✅
دو قهرمانی لیگ قهرمانان
✅
دو قهرمانی جام جهانی باشگاه‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22142" target="_blank">📅 20:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22141">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyIsLZWMPsbzhANABC5iZ20QQ6WEMkUUt6MapS51FgOqQM8jfOQ_176h9Ms53WidRA0jbYge_tHbT7006B6lsNBPuOlzu2t3zQqocsXm7sZ8y8iPm276SMDLuMJE2wT237_51blMzSudF1OxJlSxhkFo0ectnf693l_Xvri1DHoHxq4py-nh37AL-TrvYGkSeLKK-TlS7Qkn7g2I_Lkd_zdTAZiJtlfxpeqNEAqSkfksMjPBw1dhWCl8p3VYAk3Cw7lBz4c25rkBhqZIBJVycPbU3j-zsUd4jIBqEFwXoC0aUmh3r6uB2fXSXz3iAU_Oe5lao9QgDbo53hrU4cSrsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-WqyhsjXabO-I-LPJ_OF__wr9M6lbJGn716TNY9CXkzSdybbDwCaudFDFhouR80FTyNMIXaXBOgnVra3cVXCr0C9scTck3RaGaeVCdmMapYIl-ho7-4Zh8wZrYo8nZlNzARN4uCkNIpcWqCjtJBw-v7vHX6lPLnnG70DROxDXMmHETLXGXEVBcirONwRI8YHfgVcTt9eKOIGPmD8iYsauEG9rSqspEqkIpoVctsyBfvRfHU46QmJgpAGb_1J-ccwo0Jt3Krb_90sqYFh1EE4zXMHyngrvb6JdwpxEwJfNk1z7JutZKkuHdr_v1Llx4kyOuHbAyR_PM7say1RURShg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدیدترین رنکینگ بندی جایزه توپ طلا فوتبال جهان در سال 2026 بعد از حذف بایرن در UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22140" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcHjrh57rj243OnALBsiw4M8hvYlYyYOXKBADCjPqV4hYp4V3mWo2CDIUjqhDwXRcvWx8C9iw5oel2R90UPFbzHj6gxm-3fd0M5CdSm_qpbzs8bosvsCcCWXpUtpTRDys--IKosH7JVGX4WKjt3PlbhNSPE1JnU1vd5KseD1ouECSmkHw6upaNYHu0042ZQmT3903de9UtXaa7ekybHee2tgorrLECpX6mMPZZHkNQ-Ho6OC-tY5x--jVGTKetP5z8dmkphvWE4h5nl_O_ytv010FBdpbj_-5Y2WTKGTcjIaFkX_Gvm8vPKSIq4j12zUGJtdS72Yat1mmUNZ7ooj3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0T8skXCvnMgc8QTLnSl5e3wjfLGGYI_s0WOhy-zPjqu0OdB3ghlyOpabLzZjQIwmLlnz_J1kstOu5PczlwWaWQ0Kw5Wt3BufcNctnppDGlQZ1E3r2ZPsKDkviVaZwzJuiVas22D5KO31oJe3STCDU58tsA-OyyCDEtvZVfSRj1xSwckyB4PH8OmKOB6G0IjQcmb3q707PxZZp5OxKc2I-Uk122zDQrwU7LkSbF0arq0ZohTfN2i3SVbM5ZUThAvyzVe-pXCdP6LzBr_DVDCT5rZrr6q93SKrQz2wn0aEiumpp9P3du0FkDjJCnv-JVit09gwMUT-V1EPweWfLqi_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⚽️
اسپورت ‌کاتالونیا: هانسی فلیک سرمربی باشگاه بارسلونا درپایان فصل جاری قراردادی جدید با این تیم امضا خواهد کرد که به موجب آن تا پایان ماه ژوئن سال 2027 به آبی‌و‌اناری‌ها متعهد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22137" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22136">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0JYR5ngf3_sZF8qV7V2WLqYp1Vu8kvl16xqkqIu0vYhtVj6sj-lnV3eWHTCs2EPP9IJWAFZfk1TT-LlJdKdc7OKema96URxPW2krub9PiWWpCNGHgbZp5W9mSHwhjG7zhm0AysY4RyrxrSOxMNqyPKHWfIcfhS9oCCgtuSGiUmn7azS61qcv557Wl0c34kFDL4fYrs_kHWMzTxvWvJgb9FkCCIG2qasQyUSOHoLupMZkSU6GSFxsWhZw93Cxf6kQbG6IbPN_yN_F99M2Ili9HpGS8EYpu_m7nemkGx_xw2fcLqbv5OrEMa7F4vs7oUhKDAU5kFdRp8VjaTPzJzopQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22136" target="_blank">📅 00:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22135">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OS0CE77EOOsUbHtQMUsPLMU4tMHwokyHPqjUz1O6piLP5s3Cdi7514xPICSzc4bhbKVAhFyDmkTxohwpPBOHhSGhmOh5C0Icm34EXx0Yo3UuJINRTYlqI4BXFlbB9NpZIuwjTFgBBXoj4Jrr9xk2-mQQBEaTD8NLhF-9dhOqGlBiqx3f3M1PJfQX2r7DM9Ctcypz7dGz2DkzF7urV0a0_NlO4IesE3rdOEHbElsgbOnQ2yGrzwaDIHdO69fYbkSK2jDX4xcNZr45qP_OCMVDXzPkZxwXJFtPesNogIOlBgq4A2UPzOFL-MF6c82Gq0m6KxRDTckBW-kCxL9sXV74uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-kCGYV5CK5biMZl0QRJGGVXUTtlw7_TPKlEsQFdupM7nbpID7he7Z5Jha4Cco_ABEyjrGq--nSvwtsQNozycrSGtqAs6lPwclCs7hf183P7Z61u8aFA_RlsLUtIEGm29hMT8UveMoUwZ3uBbpmQVffzWjlsFY39tTej3IpWg6iekRQllsWWnZxHK_9PMg5RLF-5vSEZIltu8PKOK9aKJcpsTM53Mq_LrK9Pl3XxHhKBQj-pRD3AKp1Tt5RpJCY0aAvrB_XCoIMrOkcHDVUKKByFh3xMW3QBLm2rIoRF3xc7kBc6I5FZcGZxJsTI86clfC0OXYYJ-MV_bP6wPH3GWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22133" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22132">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=mGBCnlMrGVlrV1VV3K6zH7VqmzOdh0N0uJhCSWYfwNAOg3-asGa6eJ4Kf1O1guCuCPwe47uWQyhoOfdzx65e6dxoYjkEmBvDoUi4U4zBWa8-31sVgD4XtjoUZhkjK1c7q5AUVTwHr5ipNOrVS14W3zgOtaRZMx2Lhy1q1yHW602aSZRZTog-IbCFd4AP2jV6pA3wR1v-Q-H3cK4HTZRPnpCRifSiMjqeqUGr_pT7JZNmADKbuviJnnGmOxe97cBXCE7Du8vfWj-ARYZHMmZEjs2fr3Yt036LZ3TF-OfOyVY64J_6dJ1pDzZqZCs4rbNsfxk8Dd1prwYFPLesgo0jbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=mGBCnlMrGVlrV1VV3K6zH7VqmzOdh0N0uJhCSWYfwNAOg3-asGa6eJ4Kf1O1guCuCPwe47uWQyhoOfdzx65e6dxoYjkEmBvDoUi4U4zBWa8-31sVgD4XtjoUZhkjK1c7q5AUVTwHr5ipNOrVS14W3zgOtaRZMx2Lhy1q1yHW602aSZRZTog-IbCFd4AP2jV6pA3wR1v-Q-H3cK4HTZRPnpCRifSiMjqeqUGr_pT7JZNmADKbuviJnnGmOxe97cBXCE7Du8vfWj-ARYZHMmZEjs2fr3Yt036LZ3TF-OfOyVY64J_6dJ1pDzZqZCs4rbNsfxk8Dd1prwYFPLesgo0jbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
👤
در شب درخشان لیونل مسی؛
پیروزی پرگل و ارزش مند اینترمیامی برابر سینسیناتی
اینترمیامی درشبی‌که‌مهمان‌سینسیناتی بود توانست با نتیجه 5-3 به پیروزی برسد. لیونل مسی در این دیدار موفق شد دو گل و 1 پاس گل به ثبت رساند تا نقش اول پیروزی تیمش باشد. با این عملکرد لیونل مسی به آمار 11 گل و 4 پاس‌گل در12 مسابقه فصل جدید ام ال اس رسید تا صدرنشین جدول اثرگذاری لیگ باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22132" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22129">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIysP0miO2p-QFh9EN0crLOmfzllO_JyoTzzWbJJl6sOxSZaLsE8yJR0HdzssLbaLFscJze-Qvv5i09jfd9uYAE1w1Cf1zGpvCs6oXpwOXw3Nq-JFNl66fagJp8jxl-LxvAmoh7RNWhJ42c0pTkmpYLUdYlRmnTRHqA1I-DP80A69JMBk11YW5EUNoBoq32McgayVFHu_JERt9mpjBJaoerXqOZM05UjPHRv6Sc-4BLtmqawnCyPL2GwBIAoBQqlwfmvgM2x4loyRgBMLIzZ38mPukE1UP9CgPYkEtTXiD2LPV6pvBuQMjIeXIXvNTCWqcLgZ8B7nnL0CQf3DxUR5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ham1DMWufWl8ZRDxNIxmLYSD69FaYMtaOPXnICKRx_jM-FL5j9EV6UzPZiCBJQuo3YA4BKGZEtkS04K8Iv7_ELdbjMcLzVvPDSW5c0u0YK1td29pwR8rLWhaSPRYdMrit387koGiaoh6_A8pbtFCIEa7kpLUSGgPd39yvIq2KaQPCQ0TvMlzhgYk7YAsg11zkI2ZNgwiYpfi_3drEADkCEJjrnDzmuYIOT2gDvDKdv_y5DnaepTZlMVhLej_DyM0dT2okq2I0MbDOFeNeYlsyNMdP9rU2e0glzS1weFMOUdnyGatxM9mFvEp2YFKKsxejz_yz62cBh7tJVVGvzG8pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22127">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5mBn8dH2ncss1jDe958Qfq_bSsnhD0z8WbdDEgzIebbgOg2p2pzPtS0gz2YgfgM4RbZQo41xdVAt4zBlRZogDBSpT_EO5Zpvaxgn8_ReGSgIW900DVMrQHK49Xa0WUFrRYK0IQ0fTGOKEt7gcq5nUMabfpbvAhap4kkAeKH264xABMrfYrqT9cHo8W-xq5pTGZ0yK4vfJR0ERtQCUuLnM3hbH1hLlVF5zFVUFiUgmOm9_KX1sGj0hi4cybauwFRkzk1iWeRNkfL50dcvWrDk--qmwMyptkxSOJtv7gWcMi_2HRiYoLYsjGvM2m0PLNlAuRxvcOVeSEwyNIMEX7XIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا؛ مدیریت باشگاه پرسپولیس قصد داره قرارداد علی علیپور رو تا قبل از اتمام نیم‌فصل به‌مدت دو فصل دیگر تمدید کنه و صحبت‌هایی با‌مدیربرنامه‌های‌او نیز داشته. قرارداد فعلی علیپور تا پایان فصل اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22127" target="_blank">📅 07:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBrEnBFUQ947TAjBDIGgxfYNpK4_prNBmXPv-R9gvCD_0WSVib86Zx8oYX9dsg0MUyrOgHLbrCNogWQR_aTGdZvspCRZYiBgwAp2xWHBN5FFdwnLse36k05ArspEK4dLSlmhsCSeSHVASq4BYyL06MQyI_WkFtmIKN4rVaijQ6ysrUf-IYYTn1FXTNNurNGptpbFt-muSjPNtHIVWOTIPziuU8nA2sltKot8yeJmVyjVEViA4_wGmvzm_lbjt0tNTAxxfbdXSFvus_DScESYuSgY6CGzfLL1BpEktbK4CR4AxX2tvioScF_pfQzwHIh2CXcXZQvF9ySCgPV_nde7_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

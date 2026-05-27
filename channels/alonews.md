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
<img src="https://cdn4.telesco.pe/file/jgbFB-Eiw6AhjbiKjitEwtcqtuInrvqg76cb5mGF7hxvuKYkXhcEkMplmptFXPCmkw63_I_DPxu6fLdrX8w3iIx63J9mrxTBu-ZS5TkzGeZqr1gDyEHNUMiBBAceV_9ITI5KZh_TfGV-jJQDkbazdm1MljtdykuzqzFNqpeWtTIzGuQni5GpVm7viA-XMboTMbqz_wNXTKwP1kyphCyV6cxzvq1u0zySVeImvi5eJSl-TKJNaRVIH62oWMJMoqsxvTZAMcFrIWjmXY90-tIvB9KigdXZF-QogN5s-WzFbHw623-EfNt-FU40x4mwAJSQCDNfOmfscyOXASRN1JVkrg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 927K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 21:09:14</div>
<hr>

<div class="tg-post" id="msg-123123">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
ترامپ: اوباما کشور اشتباهی را انتخاب کرد. او باید کشور دیگری را انتخاب می‌کرد. به شما نمی‌گویم که آن چه بود. او وقتی ایران را انتخاب کرد، کشور اشتباهی را انتخاب کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/alonews/123123" target="_blank">📅 20:59 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123122">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ترامپ درباره ایران: آنها شروع به دادن چیزهایی می کنند که باید به ما بدهند. اگر این کار را انجام دهند، عالی است.
🔴
اگر این کار را نکنند، هگست آنها را تمام خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/alonews/123122" target="_blank">📅 20:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123121">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a286aadd.mp4?token=VM7Dz_sVauEbsZGFe16RsT9rxoNczNvkJI_HSSxHv41xnUhBS852NpOUzdu37s2FhFI3sG702U_U2CjmYtG51xBiRELjX_tx9xnKjgYU2aog1-10XE6qHR0z9jkE4kkJ_p5FExxvqJ_uR35SFiRtHGM1ASan2i7tOHhGH1X-HVHswZcnxlyKXdCsTLTSFS9qz67NrVsZKC72F72eVAdDCCwU8TJMMXZPCS6VgPL21Sprp8FcniqbF3YsYE633WmLbY5d9XOIc7zZ39tonyUdCT_gnDh4D3kK8UCnC_q36PQ2gHQ5HnSDM3Dnlwfnv7erEcZmGiBRTiCw2zHbCvPVDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a286aadd.mp4?token=VM7Dz_sVauEbsZGFe16RsT9rxoNczNvkJI_HSSxHv41xnUhBS852NpOUzdu37s2FhFI3sG702U_U2CjmYtG51xBiRELjX_tx9xnKjgYU2aog1-10XE6qHR0z9jkE4kkJ_p5FExxvqJ_uR35SFiRtHGM1ASan2i7tOHhGH1X-HVHswZcnxlyKXdCsTLTSFS9qz67NrVsZKC72F72eVAdDCCwU8TJMMXZPCS6VgPL21Sprp8FcniqbF3YsYE633WmLbY5d9XOIc7zZ39tonyUdCT_gnDh4D3kK8UCnC_q36PQ2gHQ5HnSDM3Dnlwfnv7erEcZmGiBRTiCw2zHbCvPVDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: این تغییر رژیم است. یک رژیم از بین رفته، رژیم دیگری از بین رفته، و ما با بخش‌هایی از رژیم سوم سروکار داریم.
🔴
پ.ن : تنها چیزی که تغییر کرد مارک سیگار من بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/123121" target="_blank">📅 20:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123120">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
فوری / ترامپ: می‌خواهم عربستان سعودی، امارات، قطر و دیگران به توافقنامه‌های ابراهیم بپیوندند
🔴
آنها «به ما بدهکارند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/alonews/123120" target="_blank">📅 20:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123119">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: آنها ممکن است موشک داشته باشند، اما در حال حاضر نمی‌توانند موشک‌های بیشتری بسازند. نمی‌توانند پهپادهای بیشتری بسازند. نمی‌توانند کشتی‌های بیشتری بسازند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/alonews/123119" target="_blank">📅 20:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123118">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ترامپ: به درخواست نخست وزیر و فرمانده ارتش پاکستان، به ایران فرصت کوتاهی خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/123118" target="_blank">📅 20:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123117">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a107aa436.mp4?token=WKPk5QqfZFxMcY7onc6ktq1ObLH5A7XGQn8aYd8hyiMx8Z2uXnWWexgvnavhdSfR2HfzHkDRfZGsxPUP-kexZzBlKD-PP4DEMXZzgJPxw3KFz94GRuoqNQ3oJAPdc-yW6nvRm6tTiVXS48mLLjf1UFM54y5C86tPm9gTEf_nDOe59cm1K3pVIlrAgjy1o656-z8Z9tfMgFAjvRVxVmPCjGM3itczuv9ceQtt416ZPTLkwssy771GOY8jLQDpyz8UETjSGOb6Ykvn4jVvBpMjL6b3yIaQy5wPJi52nVaKRFH97EZkXA9Nm9xqC2PAdau2RzkanX4-ge6NM_Hx4i24KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a107aa436.mp4?token=WKPk5QqfZFxMcY7onc6ktq1ObLH5A7XGQn8aYd8hyiMx8Z2uXnWWexgvnavhdSfR2HfzHkDRfZGsxPUP-kexZzBlKD-PP4DEMXZzgJPxw3KFz94GRuoqNQ3oJAPdc-yW6nvRm6tTiVXS48mLLjf1UFM54y5C86tPm9gTEf_nDOe59cm1K3pVIlrAgjy1o656-z8Z9tfMgFAjvRVxVmPCjGM3itczuv9ceQtt416ZPTLkwssy771GOY8jLQDpyz8UETjSGOb6Ykvn4jVvBpMjL6b3yIaQy5wPJi52nVaKRFH97EZkXA9Nm9xqC2PAdau2RzkanX4-ge6NM_Hx4i24KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ما چند ماهه داریم این کار رو انجام می‌دیم
🔴
جنگ ویتنام ۱۹ سال طول کشید،بین دو جنگ، ما ۱۳ نفر رو از دست دادیم
🔴
این خیلی چیز وحشتناکیه، ولی اگر به تلفات جنگ ویتنام و جنگ‌های دیگه نگاه کنید، اون‌ها صدها هزار نفر از دست دادن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/123117" target="_blank">📅 20:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123116">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
فوری / ترامپ: ما در مورد کاهش تحریم‌ها علیه ایران صحبت نمی‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/123116" target="_blank">📅 20:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123115">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ترامپ: اگر ایران آنچه را که می‌خواهیم به ما ندهد، وزیر دفاع کار را تمام خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/123115" target="_blank">📅 20:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123114">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ترامپ: با این‌که روسیه یا چین اورانیوم ایرانی را بگیرند راحت نخواهم بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/123114" target="_blank">📅 20:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123113">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ترامپ: تا زمانی که ایرانی‌ها رفتارشان را اصلاح نکنند، هیچ پولی را به آنها برنمی‌گردانیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/123113" target="_blank">📅 20:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123112">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ترامپ درباره منفجر کردن عمان صحبت می‌کند : تنگه‌ها برای همه باز خواهند بود و تحت کنترل هیچ‌کس نخواهند بود. ما مراقب آن‌ها خواهیم بود.
🔴
عمان مثل همه رفتار خواهد کرد، وگرنه مجبوریم آن‌ها را منفجر کنیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/123112" target="_blank">📅 20:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123111">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa3da0b6f4.mp4?token=LU7l5LW1-yVXsoElmOe8lEpnWjtPCoTP3dYdf63_1AK1iK9kFB6jp_wxWmyAbqv2qnjUEc7D5cMpOaqb6dAFt3HhC3dHMu0VB28L-IVbPIGix_iNx0SbLyXHB2zq2SSk_ntADpJfP8zFULtFYftQ2fej8MyNxqf8ELFTgv7W8yaAof0bOo5xSjCMbVB7sx8ezBXaWks85QYrSPA4wGxRuXi5XKGZfE-svT5Ijhoy37LFszh_BbrcghjoC0m-V5WViTi6FhTN0WTOK9gbWL_JzKa3hnLd4n0DJJBM3pC7QqNNALblBQ2_ye03eUgTSLglci8h7HT6BTJWMtYM8VCB4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa3da0b6f4.mp4?token=LU7l5LW1-yVXsoElmOe8lEpnWjtPCoTP3dYdf63_1AK1iK9kFB6jp_wxWmyAbqv2qnjUEc7D5cMpOaqb6dAFt3HhC3dHMu0VB28L-IVbPIGix_iNx0SbLyXHB2zq2SSk_ntADpJfP8zFULtFYftQ2fej8MyNxqf8ELFTgv7W8yaAof0bOo5xSjCMbVB7sx8ezBXaWks85QYrSPA4wGxRuXi5XKGZfE-svT5Ijhoy37LFszh_BbrcghjoC0m-V5WViTi6FhTN0WTOK9gbWL_JzKa3hnLd4n0DJJBM3pC7QqNNALblBQ2_ye03eUgTSLglci8h7HT6BTJWMtYM8VCB4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : تنگه هرمز برای همه باز خواهد بود. این آبراه بین‌المللیه و هیچ‌کس نباید کنترلش کنه
🔴
ما نظارت می‌کنیم، اما هیچ کشوری حق کنترل کاملش رو نداره، این هم بخشی از مذاکرات ماست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/123111" target="_blank">📅 20:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123110">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
پیت هگست، وزیر جنگ آمریکا:
ما توانایی موشکی، دریایی و نظامی ایران را نابود کردیم.
🔴
ایران ۴۷ سال علیه ما جنگ به راه انداخت.
🔴
یکی از افتخارات ترامپ ترور قاسم سلیمانی است.
🔴
اگر در میز مذاکره به نتیجه نرسیم بر می‌گردیم و کار را تمام خواهیم کرد.
هم اکنون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/123110" target="_blank">📅 20:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123109">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔥
حجم‌های بالا با قیمت‌های باورنکردنی
🔥
⚡
سرعت بالا
🌐
پایداری عالی
🚀
کیفیتی که حسش میکنی  همین الان جوین شو که جا نمونی
😍
@NetAazaadVPN  @NetAazaadVPN</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/123109" target="_blank">📅 20:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123108">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P-kRq6_zMxNqExmNvKVoMERtQWFmwIHzu3QPLsB4Mmsunt5euVqhxbfifi1jfDkzqJtoJlcFmNOGOTjqyxq_6tFPEZXB9FlvQr3rTN8ris2h5PXcfEMNwyArO16HwpzlJq_5fyed3UDHYhKok_QWi3YEzTMfsdbIFA3vroYyssfCV65V94hpR-F2Rcu4_8esg4mBE3Xm_bNC8t8E5eVrz096CFunrKlXoSKY-tNS_E4j963P4BgrV1DzjfJ4jJlyMaPQA8emG9-fGFZXrUh_vUNJyOlUuTTw97w7qVUpUlS61QX9hGegfQgYfmDCQMFQ7MucXMPiOjz5sDy8AnMCrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
حجم‌های بالا با قیمت‌های باورنکردنی
🔥
⚡
سرعت بالا
🌐
پایداری عالی
🚀
کیفیتی که حسش میکنی
همین الان جوین شو که جا نمونی
😍
@NetAazaadVPN
@NetAazaadVPN</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/123108" target="_blank">📅 20:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123107">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) کل منطقه جنوب رودخانه زهرانی در لبنان را به عنوان «منطقه جنگی» اعلام کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/123107" target="_blank">📅 20:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123106">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
وزیر جنگ ایالات متحده: ترامپ شرایطی را ایجاد کرد که مردم آمریکا و جهان را از تهدید دستیابی ایران به سلاح هسته‌ای محافظت کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/123106" target="_blank">📅 20:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123105">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b162738c9.mp4?token=CFdn25VsASM2vDjprLMeYjzDI3rwKhdB_cy2v7JqbJOZNr6C5EBnQGaxhIuAtcyzQvTxhYS0Lir5eTijGq7RRewkfkWbGVsy-tijGTXPJIYyO6NHneFj_JyimxbtxVeSIY1IdN5JVswBYpV2wmIkDe-W7UazlDoo9sjJVjfBaw5ziZ3Rpsi5zTlRHAlmF8drNzee7_zjiiLw3RVfHt1fatAHiOLkAFCXp2MpupymeH7EDxsXZzV03W7OYmHiSsc8RAqOjcC6k1AYgBS0mZq6qDNKJ3xOhGZhiy-6wcML89TWTq7b5rR1CCU6B6ZDYNhgwgTCjLYX1gCJOpi9sh5TEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b162738c9.mp4?token=CFdn25VsASM2vDjprLMeYjzDI3rwKhdB_cy2v7JqbJOZNr6C5EBnQGaxhIuAtcyzQvTxhYS0Lir5eTijGq7RRewkfkWbGVsy-tijGTXPJIYyO6NHneFj_JyimxbtxVeSIY1IdN5JVswBYpV2wmIkDe-W7UazlDoo9sjJVjfBaw5ziZ3Rpsi5zTlRHAlmF8drNzee7_zjiiLw3RVfHt1fatAHiOLkAFCXp2MpupymeH7EDxsXZzV03W7OYmHiSsc8RAqOjcC6k1AYgBS0mZq6qDNKJ3xOhGZhiy-6wcML89TWTq7b5rR1CCU6B6ZDYNhgwgTCjLYX1gCJOpi9sh5TEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : الان داریم به فواره مربوط به جنگ جهانی دوم نگاه می‌کنیم، چون اون هم واقعاً تو وضعیت خوبی نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/123105" target="_blank">📅 20:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123104">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
سی‌ان‌ان ایالات متحده و ایران در حال نزدیک شدن به یک توافق آتش‌بس هستند.
🔴
هر دو طرف در حال کار بر روی یک «حفظه تفاهم» هستند که نقشه راهی برای حل تمام مسائل باقی‌مانده تعیین می‌کند — روبیو آن را یک «کار در حال پیشرفت» نامید.
🔴
نقاط کلیدی اختلاف: بازگشایی تنگه هرمز، برنامه هسته‌ای ایران و ۲۴ میلیارد دلار دارایی‌های منجمد شده ایران — با اختلافات عمده بر سر زمان‌بندی تسکین تحریم‌ها.
🔴
ایالات متحده یک توقف ۲۰ ساله هسته‌ای را پیشنهاد داد؛ ایران با ۵ سال پاسخ داد — که واشنگتن آن را رد کرد. ایران همچنین در برابر درخواست‌های ایالات متحده برای ارسال اورانیوم غنی‌سازی شده خود به خارج مقاومت می‌کند.
🔴
پاکستان و قطر به عنوان میانجی‌گران کلیدی ظاهر شده‌اند و پیشنهادات و پیشنهادات متقابل را بین دو طرف منتقل می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/123104" target="_blank">📅 20:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123103">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
دولت پاکستان: شهباز شریف در گفتگو با پزشکیان تأکید کرد که امیدوار است به‌زودی به یک توافق صلح دست یابد.
🔴
شهباز شریف به پزشکیان تأکید کرد که عاصم منیر تلاش‌های جدی و مستمری برای برقراری صلح انجام می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/123103" target="_blank">📅 20:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123102">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31be1e9e76.mp4?token=lMjOyTcf9fwDhF50ntIQBrjhx8WKPT_E9S_Vv7_5aR_WQWRh-jV4_cqWvqQLiH03cuTXh1pJk0JGGbFlID0Mc3ENxfg5LveadRaWv8trBdlECvz5jgGfjF88jg_vwD5WJK8gUsjxHbse2aVPJ_ApGPe281ci-eMIQBLneVoMOVt4cOmQVDEiHnp-mESLSaChSqhDj9YxyIT910Hg5tLuPRKYJw8emTQw1yfaJKaAol4_Gi451LcCjprUsPhUUN1S8vJ4O2s9SRmk2-Ccn4-7xv-RWdEJYqRtr0DDfz4uQxmCJ96VCkkoc7DiAassXnYHY_gMY-m0ms5UWZ2eYwEBRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31be1e9e76.mp4?token=lMjOyTcf9fwDhF50ntIQBrjhx8WKPT_E9S_Vv7_5aR_WQWRh-jV4_cqWvqQLiH03cuTXh1pJk0JGGbFlID0Mc3ENxfg5LveadRaWv8trBdlECvz5jgGfjF88jg_vwD5WJK8gUsjxHbse2aVPJ_ApGPe281ci-eMIQBLneVoMOVt4cOmQVDEiHnp-mESLSaChSqhDj9YxyIT910Hg5tLuPRKYJw8emTQw1yfaJKaAol4_Gi451LcCjprUsPhUUN1S8vJ4O2s9SRmk2-Ccn4-7xv-RWdEJYqRtr0DDfz4uQxmCJ96VCkkoc7DiAassXnYHY_gMY-m0ms5UWZ2eYwEBRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو : کوبا وضعیت خیلی بدی داره چون توسط یه عده کمونیست ناتوان اداره می‌شه،
🔴
و کمونیسم کلاً بده، کمونیسم ناتوان دیگه بدترین حالتشه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/123102" target="_blank">📅 20:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123101">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/086c5a05eb.mp4?token=L9JUW9Sa1CqwhAUnhSzRXlDUd89b14TDppd10dweTnxtisAKhb8EmQ74V7Ge7X4LFCOmYIcn6Cp_JAveJSFq8bARYub0LDIDsMNenFTDdytTe_O4ruZcCoJb3cQnEti_lEiOjuWDvoyp3iw8HRgXW_sZHK5W2VJpdRJJlrD11L5-lGM9zzm-n8mZVgCV810evisEZ4M6ru7KzUzMsCnhZYdxVfK2GpQq1liPplIrmZlIS-SwHKXpWG9NPNx7ySxt_HkKQV-arpTvib6B6ne3guNr6FEs0kCOxkiu1sxwdymGDd_TWkMcxzQFDkEdmF6LYFMETPq1mY2Qq6oVgorG7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/086c5a05eb.mp4?token=L9JUW9Sa1CqwhAUnhSzRXlDUd89b14TDppd10dweTnxtisAKhb8EmQ74V7Ge7X4LFCOmYIcn6Cp_JAveJSFq8bARYub0LDIDsMNenFTDdytTe_O4ruZcCoJb3cQnEti_lEiOjuWDvoyp3iw8HRgXW_sZHK5W2VJpdRJJlrD11L5-lGM9zzm-n8mZVgCV810evisEZ4M6ru7KzUzMsCnhZYdxVfK2GpQq1liPplIrmZlIS-SwHKXpWG9NPNx7ySxt_HkKQV-arpTvib6B6ne3guNr6FEs0kCOxkiu1sxwdymGDd_TWkMcxzQFDkEdmF6LYFMETPq1mY2Qq6oVgorG7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ :  ما به نفت احتیاج نداریم، به تنگه هم احتیاجی نداریم، به هیچ‌چیزشون احتیاج نداریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/123101" target="_blank">📅 20:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123100">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
روبیو: دیپلماسی اولین گزینه ماست، اما گزینه‌های دیگری هم در مورد ایران وجود دارد
🔴
من معتقدم پیشرفت‌هایی در جهت دستیابی به توافق با ایران حاصل شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/123100" target="_blank">📅 19:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123099">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
ترامپ: ایران نمی‌تواند سلاح هسته‌ای داشته باشد و من به خاطر جهان جلوی آن را می‌گیرم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/123099" target="_blank">📅 19:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123098">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/082192b8a1.mp4?token=q3Bz0glEb6g3dLlSheZbPvScz4AjXqm2JOHeBrggadsBxRtavTX_r6T45nYG6Twyl9207L1fAjvMpM_QDA66ajZMQvTiKFY-jTR5d8neQJXYOwLU8wJoU-d0DLhNnCs2pLfKQj1QdQ_4tbMJVYizgI7qzfTqm6p-gzqKZsEhB7Cs98e1uPqDz25rps1dcGUFd9fdP4yFsrHEY9xn3BCr-bQSw-w2SudH7lLr5QNycnw6Hb1jR1-b0RvcPa909EEMUvwED2saFUfxcbSfb_DFJRq7Ymsg0QtOmRLm1w38SA7rVRw5H9QBNPuwjCrvbxSoq8RaNgah4HZrgI_YxiAQ3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/082192b8a1.mp4?token=q3Bz0glEb6g3dLlSheZbPvScz4AjXqm2JOHeBrggadsBxRtavTX_r6T45nYG6Twyl9207L1fAjvMpM_QDA66ajZMQvTiKFY-jTR5d8neQJXYOwLU8wJoU-d0DLhNnCs2pLfKQj1QdQ_4tbMJVYizgI7qzfTqm6p-gzqKZsEhB7Cs98e1uPqDz25rps1dcGUFd9fdP4yFsrHEY9xn3BCr-bQSw-w2SudH7lLr5QNycnw6Hb1jR1-b0RvcPa909EEMUvwED2saFUfxcbSfb_DFJRq7Ymsg0QtOmRLm1w38SA7rVRw5H9QBNPuwjCrvbxSoq8RaNgah4HZrgI_YxiAQ3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : وزیر جنگ، پیت هگست، انگار از دل فیلم‌ها دراومده! عاشق
جنگه
! ولی آدم خوبیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/123098" target="_blank">📅 19:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123097">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
ترامپ : با وجود درگیری با ونزوئلا، کشوری که دیگه نیروی دریایی نداره
🔴
نیروی هوایی نداره، و خیلی از آدم‌هایی که کشور رو به جاهای بد کشونده بودن کنار رفتن و دیگه خبری از رهبری قبلی نیست...
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/123097" target="_blank">📅 19:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123096">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45c44fd22f.mp4?token=qH6PfRu9SLi0UduGn0ZaJu-KI9kKADKtgVigZ0T7fqKOel9JCx9QYPGdwrCqBW78PODoJY7PJ7N1Tnq1k4gn8SZ9u8oLN91YxZVCt1oR_M3iRZQR2ZWoiyHOefZpE3lDfvH2T0hSYllgiCQ7IL6LqpgRfSOq3As9ZgcN0fa2F0s6JEUzFbxGrXwSJuq5iolwv6kRvF-A8yIFY-6cJ86E4lLonWtaWa4eV60zDqa4p6ZRmvJnOC_QNVsDc3eJV2lI6ayrAJmmU4tciRX4vxvpxYxnh9Jq7yOMswP_aiBXFzIFSz_imp7B8D34ULFEMlo7BghhctmDk2UG0oQ54mdBkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45c44fd22f.mp4?token=qH6PfRu9SLi0UduGn0ZaJu-KI9kKADKtgVigZ0T7fqKOel9JCx9QYPGdwrCqBW78PODoJY7PJ7N1Tnq1k4gn8SZ9u8oLN91YxZVCt1oR_M3iRZQR2ZWoiyHOefZpE3lDfvH2T0hSYllgiCQ7IL6LqpgRfSOq3As9ZgcN0fa2F0s6JEUzFbxGrXwSJuq5iolwv6kRvF-A8yIFY-6cJ86E4lLonWtaWa4eV60zDqa4p6ZRmvJnOC_QNVsDc3eJV2lI6ayrAJmmU4tciRX4vxvpxYxnh9Jq7yOMswP_aiBXFzIFSz_imp7B8D34ULFEMlo7BghhctmDk2UG0oQ54mdBkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : سومالیایی‌ها، همه‌شون کلاهبردارن، خیلی هم خرابن، ماگرفتیمشون و داریم روشون فشار می‌ذاریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/123096" target="_blank">📅 19:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123095">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ترامپ: ما هنوز در مورد ایران به توافق نرسیده‌ایم و از این موضوع راضی نیستیم.
🔴
ایران فکر می‌کرد می‌تواند صبر کند تا من را خسته کند
🔴
به انتخابات میان دوره اهمیتی نمیدهم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/123095" target="_blank">📅 19:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123094">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dbdd434b1.mp4?token=c1_MhzABZadDXpp8wq4UoL_MGJFqXUFf2qYsyrjf1yMa8IvBuye-XlbGNF3mxlCAOiY05uBPiWRoh5WtCd9dK394d8V6frBrxOyGaKeaPZOHovI4RAvCUHY2HLoVGxWQavoqfy_dA0b2x0sSPki_vTI_shT50GdDiPfBKCgTvcHmniCZrZjTWEdNX8Yq0a-LfnNkju6e8q94c3qoLCYwMZut5CBQhT9oTaUMTaUxsepXR56--tCWZvb0cvK-YdDJyEGKVNULyev6qnipfTEVbxpmKimL8xihqnZfPHCbJNinCInJDGNvrkExC6svEljykF_MIJei7xK2iQsdCh7pDzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dbdd434b1.mp4?token=c1_MhzABZadDXpp8wq4UoL_MGJFqXUFf2qYsyrjf1yMa8IvBuye-XlbGNF3mxlCAOiY05uBPiWRoh5WtCd9dK394d8V6frBrxOyGaKeaPZOHovI4RAvCUHY2HLoVGxWQavoqfy_dA0b2x0sSPki_vTI_shT50GdDiPfBKCgTvcHmniCZrZjTWEdNX8Yq0a-LfnNkju6e8q94c3qoLCYwMZut5CBQhT9oTaUMTaUxsepXR56--tCWZvb0cvK-YdDJyEGKVNULyev6qnipfTEVbxpmKimL8xihqnZfPHCbJNinCInJDGNvrkExC6svEljykF_MIJei7xK2iQsdCh7pDzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : الان داریم با رویکرد «اول آمریکا» جلو می‌ریم درباره ایران. یا باید با شرایط من کنار بیان، یا کار رو تموم می‌کنیم.
🔴
می‌گن «صبر می‌کنیم تا انتخابات میان‌دوره‌ای». دیشب دیدید چی شد؟ اون فقط شروع ماجرا بود برای انتخابات!
🔴
هر کسی گفته من دارم کوتاه میام، اشتباه کرده
🔴
الان به نظر میاد خودشون دنبال توافقن. فکر نمی‌کنم حق انتخاب زیادی داشته باشن
🔴
اینترنتشون تازه دوباره وصل شده، اقتصادشون هم داغونه، تورم هم خیلی بالاست!
🔴
شاید مجبور بشیم برگردیم و کار رو یک‌سره کنیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/123094" target="_blank">📅 19:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123093">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ترامپ: ایران می‌خواهد توافقی منعقد کند و ما با آن توافق می‌کنیم یا به ماموریت پایان می‌دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/123093" target="_blank">📅 19:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123092">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cc219101d.mp4?token=l2igRpb7eGUDbdGXzI99Cq_m3Ioxfg29dfutczQQeq7S4NmhMzFTfrgpeKdZ7lSqDIahddPRnzd5CCU38kD8JRO02NIa_oVbqYSdwRV3jqCXLCv_u16qJwh5SsILGYZ919xFe1Nh-XlZdaKjrrEylAgZPSxTjU7EGU2c-KFd5JgpWEuNNOwXjMz432ttNpdbLB-FZoIa27WOh_zAQhuEVX_8ZqWREM5gyz3TQsx9oZOWH1m1335c1gbtDX0pD82TQYhlVvSoyVIl4hJqHFq3ykACIJyvE2DJK-TtR5kXt45TRWJ4O7LGgnvg83wTIaNjPW39S-yUuQYZREqNQWa9QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cc219101d.mp4?token=l2igRpb7eGUDbdGXzI99Cq_m3Ioxfg29dfutczQQeq7S4NmhMzFTfrgpeKdZ7lSqDIahddPRnzd5CCU38kD8JRO02NIa_oVbqYSdwRV3jqCXLCv_u16qJwh5SsILGYZ919xFe1Nh-XlZdaKjrrEylAgZPSxTjU7EGU2c-KFd5JgpWEuNNOwXjMz432ttNpdbLB-FZoIa27WOh_zAQhuEVX_8ZqWREM5gyz3TQsx9oZOWH1m1335c1gbtDX0pD82TQYhlVvSoyVIl4hJqHFq3ykACIJyvE2DJK-TtR5kXt45TRWJ4O7LGgnvg83wTIaNjPW39S-yUuQYZREqNQWa9QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : با وجود درگیری با ونزوئلا، کشوری که دیگه نیروی دریایی نداره
🔴
نیروی هوایی نداره، و خیلی از آدم‌هایی که کشور رو به جاهای بد کشونده بودن کنار رفتن و دیگه خبری از رهبری قبلی نیست...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/alonews/123092" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123091">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
تلگراف: ایران فقط در صورت آزادسازی ۲۴ میلیارد دلار از دارایی‌های مسدودشده‌اش، توافق با آمریکا را امضا می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/alonews/123091" target="_blank">📅 19:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123090">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ترامپ به PBS : اگه ایران اورانیوم خیلی غنی‌شده رو تحویل بده، در مقابلش هیچ تخفیف یا کاهش تحریم‌ها بهش داده نمی‌شه
🔴
عربستان سعودی باید به توافق‌های ابراهیم بپیونده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/123090" target="_blank">📅 19:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123089">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNILe_dwGEKzuTdUX_v7X07Es_EdTW_vDh8ZUBCvWFQPmR935w28LvEXUpTxMAnsbtAPeNe5S3XYaiubbK_TcufJpbLZyBbAKdzt1jthwc_zqFNwKSpzkdYMLDe34NgPMHVGy0Fs7wxq-ISaiBSf80tlak6G5F2BIaI5V_7LaIskmoTxx8NR47ZVEMxzUBdN2elcAWYw0cHPV1OXNRprb1NZiPzH4y_QJf5PpHmf8Uu-Pc8vqPSGwKjqc8T1SQF7ycgH4OmpTm_TLlqCErbXZTzvVw7JsdEepnDwxgO5Urdse6tw0YTDfCbVsXp_cImy9EgsH0sR8RLPDbf_jb7pHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در ایتا و روبیکا چه میگذرد؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/123089" target="_blank">📅 19:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123088">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
فارس: منابع آگاه می‌گویند احتمال دارد ترامپ طی ساعات آینده به صورت یک‌طرفه اعلام کند توافق ایران و آمریکا نهایی شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/123088" target="_blank">📅 19:16 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123087">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
جلسه کابینه ترامپ قرار بود ۴۰ دقیقه پیش شروع شه، ولی شروع نشده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/123087" target="_blank">📅 19:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123086">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17eead82df.mp4?token=a9kOM9eL2gRSVdTSpJSd3DZAkPm30pIgsUcPvsRkXumvijR4N-6X_EEWCIDaM2De55HAGV3rzRweQMfhfMP_gG2PLxE380A25WPHlmYNP69-HlR4D6e2EWXzj_9MGfmwsxcts9rban9kC92dJbkgdbT-TU8OwcpsEHaI6dc_tuCZm8Xp046O3itKHqKn8PlYdokDUsrzccO-gPL41LBjMKZ3SPDpxkkgS4g-GkdhVfiXvZ_hih4jT1pPMp47t-mNDcMsLVf27_s4sOxfQz4yQo487cL0X_67TyLXnKg4mF2uwitiDCwkCUlY1M52Tcu3FAW9DE9MsZsm0vgjtygFPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17eead82df.mp4?token=a9kOM9eL2gRSVdTSpJSd3DZAkPm30pIgsUcPvsRkXumvijR4N-6X_EEWCIDaM2De55HAGV3rzRweQMfhfMP_gG2PLxE380A25WPHlmYNP69-HlR4D6e2EWXzj_9MGfmwsxcts9rban9kC92dJbkgdbT-TU8OwcpsEHaI6dc_tuCZm8Xp046O3itKHqKn8PlYdokDUsrzccO-gPL41LBjMKZ3SPDpxkkgS4g-GkdhVfiXvZ_hih4jT1pPMp47t-mNDcMsLVf27_s4sOxfQz4yQo487cL0X_67TyLXnKg4mF2uwitiDCwkCUlY1M52Tcu3FAW9DE9MsZsm0vgjtygFPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
به ساکنان‌های صور تو لبنان زنگ میزنن و میگن اونجارو تخلیه کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/alonews/123086" target="_blank">📅 19:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123085">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7909417a98.mp4?token=hzJ6Xuh9v-N-qb6CMEU9yfZl5iVlkH_dps86QWZaA09lb6uXnJNwyW9Hjc1kZyddfwdpAeUSOdTPLouUoI53DUU4hu80-EhZoLhcFlY-6F0kKK5eF1GAQ-dxJ4gIVcmExOcWL-NLo_QOl-CjuITkiaVJyICy4dTlrpi_uQWJYLtY-pd9w6Kg9gvEBaBJTzWlERDpWTNEX4KPjC3eRrWN5UQ2MJcpPm4y16d7hYygoknb_XZdQz_D4ubIJlc0uA1q8gTVNYWJrVvTDTkOsBSSw7sJW7SnALgMfeXsS4R1LKUUKUdNmDcKE7wC988Tv1f5iSrHOY_8Ad_hEqO8J_6Jjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7909417a98.mp4?token=hzJ6Xuh9v-N-qb6CMEU9yfZl5iVlkH_dps86QWZaA09lb6uXnJNwyW9Hjc1kZyddfwdpAeUSOdTPLouUoI53DUU4hu80-EhZoLhcFlY-6F0kKK5eF1GAQ-dxJ4gIVcmExOcWL-NLo_QOl-CjuITkiaVJyICy4dTlrpi_uQWJYLtY-pd9w6Kg9gvEBaBJTzWlERDpWTNEX4KPjC3eRrWN5UQ2MJcpPm4y16d7hYygoknb_XZdQz_D4ubIJlc0uA1q8gTVNYWJrVvTDTkOsBSSw7sJW7SnALgMfeXsS4R1LKUUKUdNmDcKE7wC988Tv1f5iSrHOY_8Ad_hEqO8J_6Jjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش زدن ماکت جواد ظریف در میدان اتحاد گرگان!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/alonews/123085" target="_blank">📅 19:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123084">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyZaIbY2IgPpfDtHLFKOZOLAEhDgRJQMsHrsGM-4NrRVYm8Osj22jwsJwAVOCT0EGHwqjGiqQhcEf-SPRLSwLWDmzITK7RzNOWA2ZJvrzwBttYlW4j1L_Xg67dqIw926s1VYYCxdosE8uzxEUBvV6UiwsfVrNR-7FKku9mNZN76BruIS6Yn8bzLgevu9Z_kzAzmyhpPNz-JmIkRT-c9U5HUTi0KxJlUpjrQ1XaQ9FyA5AaL6U6CxtY8AMtpjcIO-g2DBV-_oHtMNFGSgbM0yBe5Ne_ZRYuhgFAX4B0m_FQvyuuGqibckGKDQZrjbW-zgOykduHkr2I1IBK8mk8AVzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابوالفضل ابوترابی، نماینده مجلس: مردم عزیز(اون ۴درصد) اخباری که در خصوص مذاکرات به گوش ما می‌رسد، خسرانی است که از برجام هم بدتر است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/123084" target="_blank">📅 19:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123083">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/78f3edcfce.mp4?token=GKSbnAsl6l0sKdDOk0FmzHci3pl0L8ah8TLQOU4NW0jc6zx9h6Ir3f7gdyixPaEQY4OMncsZmUBkitqjfINpKPZgXXrOnIp6efnDTUZDInHT0xT0L0ij-fR00bwSGzB57zcl6pHEDw30RlmvMTr5to0Y9AYFBdgkiZQbQyzGolqUpCvkUbOai8oPjVIZiHYheVaTv65dF4mPy_T-Fb-8x8jQaUpECglc31sXYPgzGuKfPSG4RhJ7V5yz9_vJcp6jzhK9JG3lCLYPIsFYCp5fCgyQsT1sGnnO6vlL_VTpXsX2n1EOsjTjCkv2DyDx-Y5qFt7LJCprNhPxyI6YNYqFq5HJBxkP1X7Cxs02T7Obkby1K8AwdxduI5fuh41ajSDQwYDUwf7GnS-rRggWvWNpTW1Ed1IGU0iy_9sfro-187ETIdAZuERjA5Fbs6wgsMH3l3Re-mucOn-WgLSlokyjBs8i3SXtAAhGptJZrp4bpsBlF0EEm8spgkyy3c8nZhJUetRXs4Kak1263lXzpqO-bY8rTENyyQM8qHfjlmGnmio11sVxUnjmFJ1cmVNcwp7WxvahUHoaTRdT9LHhi4lsNUEikHln7dpZg1rAlao6lEdisRnCO61RuVSgR41JI8TxC_PJ-7wggIyVpgjASt4m51HiKN6wQvci1R6PGAUJ3hA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/78f3edcfce.mp4?token=GKSbnAsl6l0sKdDOk0FmzHci3pl0L8ah8TLQOU4NW0jc6zx9h6Ir3f7gdyixPaEQY4OMncsZmUBkitqjfINpKPZgXXrOnIp6efnDTUZDInHT0xT0L0ij-fR00bwSGzB57zcl6pHEDw30RlmvMTr5to0Y9AYFBdgkiZQbQyzGolqUpCvkUbOai8oPjVIZiHYheVaTv65dF4mPy_T-Fb-8x8jQaUpECglc31sXYPgzGuKfPSG4RhJ7V5yz9_vJcp6jzhK9JG3lCLYPIsFYCp5fCgyQsT1sGnnO6vlL_VTpXsX2n1EOsjTjCkv2DyDx-Y5qFt7LJCprNhPxyI6YNYqFq5HJBxkP1X7Cxs02T7Obkby1K8AwdxduI5fuh41ajSDQwYDUwf7GnS-rRggWvWNpTW1Ed1IGU0iy_9sfro-187ETIdAZuERjA5Fbs6wgsMH3l3Re-mucOn-WgLSlokyjBs8i3SXtAAhGptJZrp4bpsBlF0EEm8spgkyy3c8nZhJUetRXs4Kak1263lXzpqO-bY8rTENyyQM8qHfjlmGnmio11sVxUnjmFJ1cmVNcwp7WxvahUHoaTRdT9LHhi4lsNUEikHln7dpZg1rAlao6lEdisRnCO61RuVSgR41JI8TxC_PJ-7wggIyVpgjASt4m51HiKN6wQvci1R6PGAUJ3hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تعجب یک گردشگر خارجی از تعداد پولی که در ازای دو دلار بهش دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/alonews/123083" target="_blank">📅 19:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123082">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e28ebfd303.mp4?token=sCf4GpThEwI1MQiVMX0sZPKbWb2AQHd9qX9cqHCf2MbUd10-jm4cdIh__Z45PksZW8dTXLEwaZFlMiiMXa_dC8JHPgrBt9oXtkQrPXXgh4EzB9ePhYyI88p_ZPxax33fiStoFaY7caX0bFp2Y9ttVLWWDzdD0McFIs_QGU-BnN5D3dM7Zx10dyyriJwYlTdatL_5phHwtB31hb1fe20yrKk4quevZJDKOhFQVhCtZXss1YfWl_FCb57rL76bai3ptwCt-9uS8JIecpaM_0Qj4vGSe2lUH5iTqcSx8JCwVb13ShjNZ6xJQuzXWhzeTNsLN2iEYbWiz3wztF-HRFEBCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e28ebfd303.mp4?token=sCf4GpThEwI1MQiVMX0sZPKbWb2AQHd9qX9cqHCf2MbUd10-jm4cdIh__Z45PksZW8dTXLEwaZFlMiiMXa_dC8JHPgrBt9oXtkQrPXXgh4EzB9ePhYyI88p_ZPxax33fiStoFaY7caX0bFp2Y9ttVLWWDzdD0McFIs_QGU-BnN5D3dM7Zx10dyyriJwYlTdatL_5phHwtB31hb1fe20yrKk4quevZJDKOhFQVhCtZXss1YfWl_FCb57rL76bai3ptwCt-9uS8JIecpaM_0Qj4vGSe2lUH5iTqcSx8JCwVb13ShjNZ6xJQuzXWhzeTNsLN2iEYbWiz3wztF-HRFEBCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل اولین هواپیمای سوخت‌رسان هوایی بوئینگ KC-46 پگاسوس «جیدئون» را از ایالات متحده دریافت کرده است.
این هواپیما امروز زودتر در پایگاه هوایی نوواتیم، یکی از بزرگ‌ترین پایگاه‌های اسرائیل، به زمین نشست و رئیس ستاد کل ارتش اسرائیل، ایال زامیر، نیز حضور داشت.
KC-46 می‌تواند سوخت بیشتری حمل کند و تعداد بیشتری از هواپیماها را نسبت به ناوگان سوخت‌رسان قدیمی‌تر اسرائیل سوخت‌رسانی کند.
قرار است اسرائیل حداقل شش فروند هواپیمای KC-46 دریافت کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/alonews/123082" target="_blank">📅 18:46 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123081">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
رسایی،از رهبران بولشویک‌ها: از وقتی اینترنت وصل شده قلبم درد گرفته، یه لحظه‌ام نتونستم بخوابم.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/alonews/123081" target="_blank">📅 18:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123080">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuEsdl6c-lHwY3-zlKSgLisQiQyGJC9FT6erHx9UHR41-6NAQAfyVpJLUM69oGHn2hHDixhuCDGV_icSFRdLMAfykr0FuzJqO91xHxwD2FRVArCMU5B5W-pR4O1t-KgnlBNmqPFsurkExejXs832y0yi6pdn-RFU0GF5h3wIgLGaZaxAx6bq7brM7LzbKO7RN5agcXZB9A-kGuoRnRgTP_mYmEKxBbei5jNQjGojZUnfGEVQEPOnQMEJ49CK_kMqVo3A8UOk_fXBPQNiXSK81x-ODnVeFQTWI2aovgq29neFHGNlOLBEhzWL54eYWYUfdxBvDaV-iQzLY4BEBCm0iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی،از رهبران بولشویک‌ها: از وقتی اینترنت وصل شده قلبم درد گرفته، یه لحظه‌ام نتونستم بخوابم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/alonews/123080" target="_blank">📅 18:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123079">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHsOZc9UKawuD-6yAhSSo8mXSOwTQtdYh4BOuyaViCmJoW6gOm22x3ST062fGmfoZbRLAZNM-_w27YZS6PyrjsXRn0oN2_MXC9h28clhzS8vwkTuVVNCH6VHEnXmMWhLJWAGgwKMP_HCEQMOUuRs3eNbzW6O1CG9xHBmU-C9ynndAlzujFmf8su23L88ekSAahzcmkSW42MjKXJWpem7YYao2TFU6LBMp6myJlplzJInCC3DtPcQjGKPrW0WLc1-qQMsdYCM8F0TD6tnF1LBFcUl1vKx8x8IcbvwqS4SHYlwHv-1ManAouefAYLglBlMCls3GSs0qjleBjVJXRyUhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل :
ترامپ اجازه حمله به بیروت رو داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/alonews/123079" target="_blank">📅 18:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123077">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E5l7c74Qwx4MJ7bvugOMVkVRYyzCkHUByd-CF5KyUOoSchEO4VdjeKziKZF4TLst5XV1QteeniMlwmuQBVDniprJJJJKgPW99sgGH47rcJ02aWgb2quLzsrEta6S84NsdsjrteWURe8dBi9IkNGxvV9wVmZrC0MtntxQWVk-dlRnN2KJMRYChZVYC_iB9SSxmUaU-7s6FkiiXnSfJ14Z6ZKmMqBCfdStHXEtgwQgLA4_-RsfHqMoN1S9cPOvb5cIvMkArodDXKfofkHGDrjpV9NeEhARL3_bbNL0H82sz5EeOFY9PgV6owg8EWSF0XfXWWDZFxtZvS6Tc0kRCrRYHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PGmTaV112uO5Yw7NPscF-40zLjd-zmy54r_RAwkc1vtDbBhyO0TSjfEJviJLAu9Q1CwFhfZaysaRgmfVdkohZ3gxSom7wmIMnIWD7KTOvC2PsBBgcZOWBaIeM4HFkq6V7_nJ2OzdrVMl_a4Xj5Vou1bOfGNe0YpfxahwIDcJl1G4ZSUOHPLJ14NhMZWv5e8396mM4ea4m2qxabEkCmdoAkuwmT08Ga0qyHyvvf99qzZVbFQZDMuo8GCsNRd1-Y92nAjLjBKq9uKecRV6Yh3SrsWjwDjIOCY7z-MjQu7x_6pgbkpDbKJxkPTUC65cCZaNj65bYadgrVEZztQZhHJkNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات اسرائیل به حزب الله ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/alonews/123077" target="_blank">📅 18:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123076">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
صداوسیما: سند غیر رسمی اولیه از چارچوب‌بندی یادداشت تفاهم ایران و آمریکا منتشر شد
🔴
آمریکا متعهد به رفع محاصره دریایی ایران شده است.
🔴
در مقابل، ایران متعهد شده است تعداد کشتی‌های عبوری تجاری را طی یک ماه به سطح پیش از تنش‌ها بازگرداند که شناورهای نظامی مشمول…</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/alonews/123076" target="_blank">📅 18:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123075">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
کاخ سفید: ترامپ گفته است «
مذاکرات به خوبی پیش می‌رود
» و خطوط قرمز خود را به وضوح مشخص کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/alonews/123075" target="_blank">📅 18:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123074">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbKRgFQ94ZN0mVKqLax4L0gx_EFo5FzEIcQnxBZXVNafl9Iz4UDvbW_m_k6RfIGjX9jVdWV-MQ8FkLkJHtOZeSwPMxct-miukzSKGvaHb58MP4UAC21speEKHxrKFh5a9QsBkRkiOy8lOOcF21pdHJw-KlF-vDrD7y3hEXAQF9zj3YLw-FXj4-nsHCUPWlIy8Kdwss1i2xPCAPpXkMUVw5y1b7nGgRf_JOK6R9DeiKzYs6p7bW_-i5i3SenCz-YYhDTef2Bhp4P_sg3ADjbYqI4Vo3nEdcIPVYtlelzHGZFbajMh6Ni-ZAizYqe4Z6mVWJF8F-_rL9g-bvwwO8eGuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ برای بار هزارم این عکس رو توئیت کرد و نوشت نیروی دریایی ایران‌نابود شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/alonews/123074" target="_blank">📅 17:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123073">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
صداوسیما:
سند غیر رسمی اولیه از چارچوب‌بندی یادداشت تفاهم ایران و آمریکا منتشر شد
🔴
آمریکا متعهد به رفع محاصره دریایی ایران شده است.
🔴
در مقابل،
ایران متعهد شده است تعداد کشتی‌های عبوری تجاری را طی یک ماه به سطح پیش از تنش‌ها بازگرداند
که شناورهای نظامی مشمول این توافق نیستند.
🔴
مدیریت و مسیر عبور و مرور کشتی‌ها با ایران و همکاری عمان انجام خواهد شد.
🔴
آمریکا تعهد داده نیروهای نظامی این کشور از محیط پیرامونی ایران خارج شوند؛
این‌که نیروهای اعزامی به منطقه را شامل می شود یا نیروهای مقیم در پایگاه‌ها نیاز به مذاکره دارد.
🔴
در صورت دستیابی به توافق نهایی در بازه زمانی ۶۰ روزه، این توافق در قالب یک قطعنامه الزام‌آور شورای امنیت سازمان ملل تایید خواهد شد.
🔴
چارچوب تفاهم اسلام آباد هنوز نهایی نیست؛ هیچ قدمی از سوی ایران بدون  «راستی‌آزمایی ملموس» برداشته نخواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/alonews/123073" target="_blank">📅 17:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123072">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
کاخ سفید به الجزیره گفت: رئیس جمهور ترامپ تنها توافقی را امضا خواهد کرد که به طور قطعی تضمین کند ایران هیچ سلاح هسته‌ای نخواهد داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/alonews/123072" target="_blank">📅 17:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123071">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
فارس: آواربرداری، تعمیر و ساخت بخش‌های آسیب‌دیده واحدهای پتروشیمی به پایان رسیده و اکنون تمامی پتروشیمی‌ها می‌توانند با ظرفیت قبل از جنگ تولید داشته باشند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/alonews/123071" target="_blank">📅 17:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123070">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8f80cb944.mp4?token=v15d-QLDy_wIgkZSCJfPG6YJFnwTlkJXD1LjgaGfOiFiwliaUOjDv0aATowYIdZnbuXNl_y9gYk_ciXo2B-yMv4LcugdPh-AM3TGigoO5XfCSf9aYxr9yOZiTCZjEL7bmuCjc4dxlj03jNBa-xu7lZwP7pnPfMMNpko75S6ucjBms5kLA08fMaT-LpQWVU62luR28B02HDb14foFRtwx_zbusYmifWKRN6LO6flKmeiGDrQ3i4n4v9q1aUoDZWMiAbJPOxS8NiQ-EqphkVGeyOhKl0qUwD0bldSaJVW4ZoBVvtcGvsDrtIeABsLAPcc8yv569VpOHXuHGEQXx1GY9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8f80cb944.mp4?token=v15d-QLDy_wIgkZSCJfPG6YJFnwTlkJXD1LjgaGfOiFiwliaUOjDv0aATowYIdZnbuXNl_y9gYk_ciXo2B-yMv4LcugdPh-AM3TGigoO5XfCSf9aYxr9yOZiTCZjEL7bmuCjc4dxlj03jNBa-xu7lZwP7pnPfMMNpko75S6ucjBms5kLA08fMaT-LpQWVU62luR28B02HDb14foFRtwx_zbusYmifWKRN6LO6flKmeiGDrQ3i4n4v9q1aUoDZWMiAbJPOxS8NiQ-EqphkVGeyOhKl0qUwD0bldSaJVW4ZoBVvtcGvsDrtIeABsLAPcc8yv569VpOHXuHGEQXx1GY9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ثبت لحظه‌ی حمله به لانچرهای موشکی (یا پدافندی) هوافضا در اتوبان بستان‌آباد-تبریز توسط یک راننده‌ی تریلی ترکیه‌ای
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/123070" target="_blank">📅 17:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123069">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff9d4354c.mp4?token=khfiiGaf_qUngX19Nh7WzsH2-rI3WPBkD66rHvpZgHsMUTGmy7lq0lugvPqbzq9EnV-4WPgILWXVNtfeROHFaL0a-B1-c4MmShcDyUza8l69QU8u5_x4vq39Pw2CqnxI-A4sgLJjPpB2cdg2jLOlotxwB6b6PdvrXzFguN0WS8N9hu6PxGiDiMrV0ckWov2rDcLfuVHkSJEUiTNI-JtxcRWpm191sutgIIxI6E1ItyI4eAiC4npeVY95wAc9vby-9Pr738wUd_Mi1ZzNIGUIuIzps_BxKxElW6_H51KZmeYARxcEz-Z6vTGWfySH892YIhdfRjpl7g88QZxak64I8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff9d4354c.mp4?token=khfiiGaf_qUngX19Nh7WzsH2-rI3WPBkD66rHvpZgHsMUTGmy7lq0lugvPqbzq9EnV-4WPgILWXVNtfeROHFaL0a-B1-c4MmShcDyUza8l69QU8u5_x4vq39Pw2CqnxI-A4sgLJjPpB2cdg2jLOlotxwB6b6PdvrXzFguN0WS8N9hu6PxGiDiMrV0ckWov2rDcLfuVHkSJEUiTNI-JtxcRWpm191sutgIIxI6E1ItyI4eAiC4npeVY95wAc9vby-9Pr738wUd_Mi1ZzNIGUIuIzps_BxKxElW6_H51KZmeYARxcEz-Z6vTGWfySH892YIhdfRjpl7g88QZxak64I8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آغاز تخلیه شهر صور پس از هشدار ارتش اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/alonews/123069" target="_blank">📅 17:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123068">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fQDvIrfX_CVrXXrBcCp9QE7Ka0tCcdf-PjNNYvz8vQqqbEs01BF2s3aGED3j90h3N9onj731bEInl_g2l69ve1q3-Oc_OgjojO5zbQ0ZTStIuj5-lftTVpkfGlzAnk2xpGbwnq33bvRytqMAT4dbrGeqSTmG6ku3GI6tjmHgl49uqihqOWTIe2miIEXYLLiMer_QQwPdrJCVcRS_DZUrEQjF8Jzl9XJb8eJ2bxWh1rUmGaWsOm76rO2JZzLbjwH2mvBcBa9nd3LSDQODedHpZjdo4wQbJFKGVPSHowWUe2-P5RyMveuRUSWr9evgdiOxtPz06fEQTSRvEGvIwMe41A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک ایرانی رفته جلوی کلیسای پروتستان که اصلا پاپ کاتولیک رو قبول ندارند که به اون ها بگه پاپ طرف جمهوری اسلامی رو گرفته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/alonews/123068" target="_blank">📅 17:18 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123067">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ترامپ امروز ساعت ۱۱ به وقت محلی (حوالی ساعت ۱۹ به وقت تهران) برای بررسی مذاکرات با ایران، جلسه‌ای با اعضای کابینه و دستیاران ارشد خود خواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/123067" target="_blank">📅 17:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123066">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eloAes96SnE-cEugZgeJ-Od7LUApq50mYa5hHmUvLiQa7gXdXOqyleoFx-lcZ8g9O-P8PhEBnWCm7OyJHrDEfNZXWvwE_-1mOGpRRNB0Ks5FV2kP6fabPhorq_xYzhcFika_JH2086nqolYXvmN1-rus7lI2SHqaVfRhM1gwcYbNKZ_-Q8jzwNPvN-rB3zineTtcP9_03DPKlNoCykxBLzKnxpW0-cZ1OjMq9o4x1XLi1XMuWKnynxM7sb1g_x51ctZXl0xILKW6XmMO4NyUw-HHGNsvjhbaJ3_oMVhRuajSlbE2qJccS3eFOpaSMtcMwrfXii7F_pJZ_0tuDyCCWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل در اقدامی بسیار غیر عادی و عجیب دستور تخلیه کامل شهر بندری صور، بزرگ ترین شهر جنوب لبنان به همراه تمام روستاهای اطراف آن را صادر کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/alonews/123066" target="_blank">📅 16:52 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123063">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g8asDcMHgetcBW6LL7vHubVoqPgL0WqxAXCPaz_S8-iYFBc-NMHtqMO9KGX5LJudGzctEytAEofV-jhajOJD5hKoeN3AIvZlFbMGVizGGMO06RIfU8XNw_V5vbi23G9UxngU64UPwyuolOoFaghJOmxPddHVUbEL4bCdI--P7RZ0pJ7I4jrOtCEH0jfDPMfW-ZF8AQe_-dddxqB8z4Slzyxv2PI47vUCVNApBmLeUItq0JhHKWHiLM7sopt5NO0g221ntEwxtLAP0ksAcl_RV1d6RdUwJDAFEWJ3ULBCrCkABqSrlDnspL6GbV8ny-j6hzXUfPz48Pzx-n6OhZUi5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V5CcgIboI4HTGpYLsB19Ok8GgRyB5tGD2QLmvvGIEwnPr-YtxBfXgPwBxaYm7-dKpTdLp7umgH48yL0szvxU8_asjVqd3vQkAh6OH-jNG7eUl-9kAasQsG357bzYIFPHlyi5U5N-v8JahlBJYZ1aJw-68PTPALn5303_iZHPtTYtmnLSQRrXesV1Us-9IXUewA0GBctfK7YRts1oVI4dW33MMOMqGo_QJPJTEOlV5EBJwkJhbB1yeZpNGP3txbTff7cL4Z7hIzJvQ_qjdwXlK1G8rz6FYL8Qn2fj7xict6Yh2UNqFN6CpGEMCJ5iH1b9hbjraq-CG4Co2sQe3EBRbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xng0yy5BvWgeCNiVvp19cWyjw6RQ7-93C_QShsOXBRd-pjEXrPdQUqK4tK5I3wH9uoN4sJwmAxB9GotYYbM8-evwchHV2z7LKBTkjQRPKlF4v4--TJhvSHzMUfQDQSQm-dIW0yTh6D9u5giCsSipua-cBSdkX5agQwXX9xnnVdORJDjb31im_I82JTI_9HbHTKYetNQJGGcb5E2YrJ0C_SUDWNisSK3FErOs8GAuwHrD3nDu9jCJ1Ei59YOEAoEyuDiSUgfmeAHuPKRZ__LJtcsw8QHSbbzikoEKtXclp_nH70i3u1WXapwA-JwB66eVFRymS7sRYYUbe4ZSs9RzuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی حملات هوایی به بریتال، کفر حونه و ملیخ در لبنان انجام داده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/alonews/123063" target="_blank">📅 16:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123062">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
اسرائیل شدید داره به حزب الله حمله میکنه از وزارت خارجه گفتن امکان توقف مذاکره اولیه و انسداد کامل هرمز هست
🔴
یعنی نتم ممکنه دوباره قطع کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/alonews/123062" target="_blank">📅 16:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123061">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyF4gbzXbP9p9v0Y6FsYEYAHdr8jMwFQRMj05akxrswE3b7OLaFaHhNYzdmNdiKc0WsGl2CJ5rU9QQmS9JhxBLJZSjS06W3epgF3demQv9EtDpzT96945JPDLId_O6ZmHmMiwc514Sxfx4S9Hcz4NgQ7LANn0eW9EcloIriU9xWngXJtV3cjY7w0H_r_vZiryrJ2MZN7R7yfpklVwcKP8wajjIJVZRnjkxcLb8f_r_4A9mZscb8DfXsS6Ns9KT5AE921zr0pLLVpOfhdNguEetIowgTk1Pi7QNhNW7Ujx9H51SXRuKaBvNwzDAMjhkFJdJITTKw4F1025wXm8QLWGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۵.۱۰ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/123061" target="_blank">📅 16:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123060">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TfImbSyMgWj1jmbcS9JPL6pGtMtBfhyZF6D3PcTRigFK5_aeJeBYyie3K_-SkwolwHKiO6Gs0oHXHHlpUFCoMiSS-KEEhHz1lrg3M9BEZupBguU0nqxIYZ4aU8ouzeLOmWydO2gQqg_IywvGsNPno8zRbo6N0iI33ufUzvJsfYkSaAPvdSBBEN_4_twmankZ_8toziC8YO9qPI5AKdagsCrsD8Rm3ze1kLQNGCDtu631cPSbgVS52niej6Uv3ZqKk4S2YsTZlIRzI-wVRZJ4Fku1se4JY8oIK6Ehy-hn9BXym5lhBB0ubIGWE-KgK-rJ2c0Qzxt_EeIm1bB8PWhAVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان وقتی میبینه همه جا نوشتن با دستور رییس‌جمهور اینترنت بین الملل متصل شد:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/alonews/123060" target="_blank">📅 16:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123059">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
یسرائیل کاتس، وزیر جنگ اسرائیل در جلسه کابینه امنیتی: ما در حال حاضر با ایالات متحده در مورد حملات به منطقه الضاحیه در بیروت وضعیت پیچیده‌ای داریم. در عین حال، ما متعهد به دفاع از خود با تمام وسایل لازم هستیم. هیچ‌کس ما را متوقف نمی‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/alonews/123059" target="_blank">📅 16:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123058">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔥
حجم‌های بالا با قیمت‌های باورنکردنی
🔥
⚡
سرعت بالا
🌐
پایداری عالی
🚀
کیفیتی که حسش میکنی  همین الان جوین شو که جا نمونی
😍
@NetAazaadVPN  @NetAazaadVPN</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/alonews/123058" target="_blank">📅 16:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123057">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EtgDbpi8m7FyZKBnmTrr4tVJOUMB3GmuJe8DQrlUJ3-8ZJsECk2XRNfNbt5Nd5u7daiekWIyYF5DipIs3gdiD10S5mCje0sbCSUxyO8F3MGW08tUWMcEuplaIad9n_p1NF8K01niCWZ0zR2o1Ux96Tw_G8h9OHA14OffPM_1GoWJw86JvmsunGmzONVbNOrIKsjsKFhAnwg1MgANOrIY6JjMvBpEGzjRS_aT2amoz49WlKAj0QQe009E330dFfl9AbqzTKl6lQOtyixsPIeKtex4ll1UvQN_MFULh7hHZE5KeCP4TKCdlRznomTmV53q5NscYlRxAvCkSX_9uvQNww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
حجم‌های بالا با قیمت‌های باورنکردنی
🔥
⚡
سرعت بالا
🌐
پایداری عالی
🚀
کیفیتی که حسش میکنی
همین الان جوین شو که جا نمونی
😍
@NetAazaadVPN
@NetAazaadVPN</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/123057" target="_blank">📅 16:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123056">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5Mu6DalWwScB1diWiIDSPRtgHssufpuKR8hnLn924-uVut4Q3uEq_isXUKzK2rOd_IhN8f2L3lbSBeuxmWpmtRI5ZS-a3MLHvfxbNwbifOvleWDczn0FlbO99q6DDJC6vTf6F1uqLJXIyGf9HHEOFHxYF__hR1PaCyIqxUvCgUmxU1GwYLxs2sSXPQes5sGueMI0wh75ijQqKRfopDTJjWBsixRJzK7h1c4mAcehVnRBeOsS_w55FLlyIjh9HGyxU9dio_4OiZUZ_-sa7tnozDbrNcb3u8sLgAOmHcyrOB3vu2s6eRgf7kc5XLczu4K9nbY4pKHCYqFrXS418eEog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جو بایدن، رئیس‌جمهور سابق [آمریکا]، با ثبت شکایتی علیه وزارت دادگستری، تلاش دارد مانع از آن شود که دولت ترامپ فایل‌های صوتی و متن مکتوب مصاحبه‌های خصوصی او را منتشر کند؛ مصاحبه‌هایی که با یک نویسنده در سایه (نویسنده همکار) انجام شده بود که در نگارش کتاب خاطراتش به او کمک می‌کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/alonews/123056" target="_blank">📅 16:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123055">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سی‌ان‌ان: هزینه‌های جنگ ایران، بودجه نظامی آمریکا را به شدت کاهش داده است
🔴
پنتاگون فشار مالی را احساس می‌کند و در برخی موارد برای انجام آموزش‌های روتین و تعمیر و نگهداری در بحبوحه عملیات‌های جاری خود علیه ایران با مشکل مواجه است و رهبران نظامی یونیفرم‌پوش کنگره را برای حمایت از بودجه اضافی تحت فشار قرار می‌دهند.
🔴
بر اساس یک سند داخلی، سپاه سوم زرهی ارتش، ستادی مستقر در تگزاس که بر تقریباً ۷۰ هزار سرباز و صدها تانک نظارت دارد، در اواخر آوریل شاهد کاهش تقریباً ۲۹۲ میلیون دلاری بودجه آموزشی خود بود.
🔴
سرپرست حسابرسی پنتاگون، در ۱۲ مه به زیرگروه دفاعی کمیته تخصیص بودجه مجلس نمایندگان گفت که آخرین برآورد پنتاگون از هزینه این درگیری تقریباً ۲۹ میلیارد دلار بوده است.
🔴
هرست اذعان کرد که این تخمین بر اساس هزینه مهمات و هواپیماهای منهدم شده بوده و هزینه‌های ساخت و ساز برای بازسازی پایگاه‌ها را شامل نمی‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/alonews/123055" target="_blank">📅 16:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123054">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
لیندسی گراهام، سناتور جمهوری‌خواه کارولینای جنوبی : مدتی است که برای من آشکار شده پاکستان به عنوان یک میانجی، بیش از حد مشکل‌ساز است. دشمنی آنها با اسرائیل دیرینه است.
🔴
غیرقابل انکار است که هواپیماهای نظامی ایران در پایگاه‌های هوایی پاکستان مستقر هستند و لفاظی‌های گذشته مقامات ارشد پاکستان علیه اسرائیل نگران‌کننده است.
🔴
وزیر دفاع پاکستان گفته بود این کشور هرگز به توافق‌نامه‌های ابراهیم ملحق نخواهد شد زیرا به اسرائیل اعتماد ندارد. این کلیپ ممکن است یک سال قدمت داشته باشد، اما من می‌ترسم این احساسات تازه باشد.
🔴
در این راستا، ضروری است پاکستان اکنون به درخواست رئیس‌جمهور ترامپ برای پیوستن به توافق‌نامه‌های ابراهیم پاسخ دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/alonews/123054" target="_blank">📅 15:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123053">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltaN5PKMfIuFFTLcwgoSjtNkDIDn7It8hR-e7Asmhazm8y3Ds3oB9xxue9_Zf8_YwZ0TO5IeOCj8dQ016nlFj2r7nCXP0LRZgrzzMdjDPZqpm4qh-bZPsrwivXVRYhXRalrQeY_ot0lH4BuJ5ybo5z_d56HmLwISGL5h7ne5kJ1AR_UGMu_o5XsUcSuKviTCfp3nNQ8YpCasqGgXcsiu_ODEw_EG3YSLExgI2jGxyM229FIuAVrIEpzRJpd4Fx-lmIylSJiqXmifEUOP1bmadhd3WNeMshUxktXdQmrDGH7Un5GAgtGHfAh5SHYnR4Czo5KJOcxPew9lVpd5r-_ZKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات هوایی اسرائیل به شهر کفر حونه در بقیعه غربی لبنان هدف قرار گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/123053" target="_blank">📅 15:52 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123052">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران: برخی از بندهای یادداشت تفاهم بین تهران و واشنگتن
🔴
واشنگتن محاصره دریایی ایران را لغو کرده و نیروهای خود را از پیرامون ایران خارج می‌کند.
🔴
ایران متعهد می‌شود ظرف مدت یک ماه، تعداد کشتی‌های تجاری عبوری را (به استثنای کشتی‌های نظامی) به سطح پیش از تنش‌ها بازگرداند.
🔴
هماهنگی در خصوص مدیریت مسیر کشتی‌ها با ایران و عمان انجام خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/alonews/123052" target="_blank">📅 15:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123051">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
زنگنه، نماینده مجلس: احتمالا عید غدیر جشن پیروزی ایران بر آمریکارو میگیریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/alonews/123051" target="_blank">📅 15:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123050">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXOOHefzVdKhcyIHhI0c3yan8eM2eViqafEVeIjIl8T_2uF37qf2JB5AyuCqvleQzw25UVsH99OHbqgeoFjNaH8GY5tE-p0ttj69JgvWX_t9m4-F9vtUa0Qh9-NNSbmTFnb4b-_MTdOdloDZo3KxiXn2CSNf1s0qmeqWAb1SM0XuQ87IE_sm0Kcl8qmZ1Ja3f_bepVm6vcAZkmVkZbvjogvliSIRUjzOpXgWzUTOliEP_YlNHQlZ5IQRrma5yzUkL7SgDKqYA0IuoRV6klZk7EAUUlIzNtK35p_hJ__Xyura25aEiwcTStBfiLR18pSt-53Jqblm-f51gpHFrX_INw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر نشان می‌دهد که هواپیمای سوخت‌رسانی جدید نیروی هوایی اسرائیل، KC-46A Pegasus "Gideon" (301)، اندکی پیش در اسرائیل فرود آمد و ایال زمیر، رئیس ستاد کل ارتش اسرائیل، در مراسم استقبال حضور داشت. این هواپیما اولین فروند از شش فروند سفارش داده شده است و امکان سفارش دو فروند دیگر نیز وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/123050" target="_blank">📅 15:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123049">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dff2f7cb6.mp4?token=C19_QM85BP7uih-PPoBBcNyiOy54sf_o_fPafz6iqqIWB3CkweX_7hXEBDog245MrZVbxdcQporjE5ha6FC11puT3Fe-ysNI2tnDk7XH4aC9TCuFFJMzYK6Z55VzL1n8CXlkVJ-KIq0y8wog12xpcCI8RXvOrAARYJ_gDx9vNb08fujKpSXxvuW9iVDzqTSQ8jalPuW2z_Mlw6lI7T_fIycNGMrDSRMs1AQxPLsRBK1rUDjogFjDJhplzhC5H_Vdghaj_S8oYf7WvtF3JDSAa77ThPgAY5PiYul-iyqx8yu6y7-YJfz0mAKM5n7CXIk-HaW23wwNaA2y643MeM2TUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dff2f7cb6.mp4?token=C19_QM85BP7uih-PPoBBcNyiOy54sf_o_fPafz6iqqIWB3CkweX_7hXEBDog245MrZVbxdcQporjE5ha6FC11puT3Fe-ysNI2tnDk7XH4aC9TCuFFJMzYK6Z55VzL1n8CXlkVJ-KIq0y8wog12xpcCI8RXvOrAARYJ_gDx9vNb08fujKpSXxvuW9iVDzqTSQ8jalPuW2z_Mlw6lI7T_fIycNGMrDSRMs1AQxPLsRBK1rUDjogFjDJhplzhC5H_Vdghaj_S8oYf7WvtF3JDSAa77ThPgAY5PiYul-iyqx8yu6y7-YJfz0mAKM5n7CXIk-HaW23wwNaA2y643MeM2TUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم دوربین مداربسته لحظه‌ای را نشان می‌دهد که جنگنده‌های اسرائیلی حملات هوایی به نبطیه در جنوب لبنان را انجام دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/alonews/123049" target="_blank">📅 15:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123048">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFKYahq9kMfI1HRjPusWXE8sNA0H-85qkXhlOxWmQR_5jib7ydN903IR8sEfvIbE_dKbK5t6G5iEQXk6B2lkjTWTrDs07CVKWtP-jjB0dm08-LtjrzRFxdINno9ORiy5kwhugYEt297TjqGpBygzU7YK3dpkLca053qr3a8EVfVkSJPGFWRZHbtMlGZT-BQTVRmgImhTwCnEyAB_Fo743eBU8IfUUuFWSGTi08FbMETeNZWJFbi1XRSMH4kaurzcrMb-IoGce7gjrcSELHXR6HobGzF7bdJ4RZvejB6Wi9eIbA0UZZ2wGBGZq7w3DTZaGLrudHR8TF6uLXfR97GtHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده درباره محاصره
:
تا امروز، ۱۰۹ کشتی تجاری برای اطمینان از رعایت قوانین محاصره به سوی مسیر دیگر هدایت شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/123048" target="_blank">📅 15:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123047">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_uYRwlAPfCNOAF1gS8aBNVfyNwWelDspE6yvSeu21OtOVBaM3BmGRASvvpxuWTJAbKXnfEek6FpUKaT5IwFswDExVfccc7hMX239OpyIUs3KCJRAO_kLBDdWm4wOwm4WuF5IY7RZTt1jSjvxWEYqcURGHhwChg1wc4-AF8o6jds-0ANLwsiur8-bV-BKUL1KJJOC5hohg-1HkKgZH4a6TV6nawuKxMPGuf8-K1z3K7-k3eHpukq_7gSj7H1Dov6bUCI1KlFn8VwLy0_SXKFlaBbhN8yEEvJRY58J5em9sPZaaaETQXCv8x8W2P8TcR_hJEXfmi8iXjmZtAq8O-Ahw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت امروز اینترنت بین الملل ایران از نگاه نت بلاکس
🔴
اینترنت هنوز به وضعیت ۱۰۰ درصدی بازنگشته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/123047" target="_blank">📅 15:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123046">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
العربیه: به گفته منابع، احتمال دارد طی چند هفته یک توافق میان آمریکا و ایران حاصل شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/123046" target="_blank">📅 15:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123045">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
باقری،معاون دبیر شورای عالی امنیت ملی: ایران و عمان در حال مذاکره درباره سازوکار مدیریت تنگه هرمز هستند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/123045" target="_blank">📅 15:16 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123044">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
نیروی دریایی سپاه: ۲۳ شناور تا این لحظه از تنگه هرمز عبور کرده‌اند و عبور شناورهای دیگر نیز تا ساعات آینده ادامه دارد.
🔴
عبور شناورهای کشورهای متخاصم از تنگه هرمز همچنان ممنوع است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/alonews/123044" target="_blank">📅 15:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123043">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfPHzwyaBzqhE6Ory73sWAigTjOh5DAiVsWiF5mTc25Vw5t7N5eSrtH_0hz7y_X0r-taFopxGQiawMT5ec963UdPcqhB5Y_1eDjpIqZqQ3962j8jnfySa5CTkdbkT0DDDoKtmg-L4Fw63T3A7hWdrOHUL-jyXvZYDcAXSahWxDipph7M8aWW4P4HFYqoIOZtaJ8hlINKXe0GUv62_hNY7s9JyPrgSKMozrL2gFpX6tKTjZQQJaDHMwHKF0Z2C-oCkJw5xazvjVId8o3zfUELnxQihivgU8lvT5IzbR4OnU3pVHoO5yK8MC2tNz_8bgQR4gy2Y9YjJdVRhuG8lh23nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس ستاد کل ارتش اسرائیل، ایال زامیر، امروز ارقام جدیدی را به کابینه امنیتی اسرائیل ارائه داد که نشان می‌دهد از اکتبر ۲۰۲۳، نیروهای اسرائیلی حدود ۸۰۰۰ مبارز مظنون حزب‌الله را کشته‌اند، طبق گزارش ینت.
🔴
تقریباً ۲۵۰۰ نفر در جریان «عملیات شیر غران» کشته شدند، در حالی که ۷۰۰ مبارز دیگر پس از اجرای آتش‌بس کشته شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/alonews/123043" target="_blank">📅 15:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123042">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyIsb22xPWIyQfJ-e2b6s0lh1rc8vH9-n48Pw85ZZudUyPYxjBgAueVzbkRL2JdtkZt8K1iS6s4buEA8p0bHhuMIEcAbLW3PdtxDZi5-bJ9a8KtRTvxIes-li0aMyDXwCbKjRG_QJ1G2tHcNrYgEQvgN4Q4K2WN6sN5fvyMurnOd7XicbWiGRRuv1HWp5Zp7_UyB5BZkgtvSoR3Kqu4j60g_CxBcsRMP_Zez8eSBY4hgFnDeRX8jPeb1UdiFjYLqKmEbrm6Hp9-Ek6fHzcn81M47Gk2iNiwysTvgerYB05ehu9iNZLY2s2fhejCGWbwNTQ2GhKtvMll13dENY7qx6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر دفاع اسرائیل کاتز: اگر به شهرک‌های ما شلیک کنند، طبق وضعیتی که در گذشته به آنها عادت داده‌ایم، باید ساکنان ضاحیه را تخلیه کنیم، حمله کنیم و آن را ویران کنیم.
🔴
اگر پهپاد باشد — دیگر کسی نخواهد بود.
🔴
در حال حاضر در این زمینه با آمریکا در وضعیت پیچیده‌ای هستیم. در عین حال، ما متعهد به دفاع از خود به هر طریق هستیم؛ هیچ‌کس ما را متوقف نمی‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/alonews/123042" target="_blank">📅 15:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123041">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
عضو هیئت‌مدیره اتحادیه مشاوران املاک:پس از جنگ ۴۰ روزه، قیمت‌های پیشنهادی مسکن در مناطق مختلف تهران به طور میانگین ۷۰ تا ۸۰ درصد رشد داشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/alonews/123041" target="_blank">📅 14:52 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123038">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eziDnir3JK-8mHmAEGb5lzJxzV6j7ZaDjSI4-XM02FsHdLDAm8772ODikj-GrOP6WTo49yWCnSfdbfLdCNVdALpiTIkaesRwXek6I_4FZ4mB00jS0VboQFF7XIrfU139sgbyXDl-coff7SYQEaeEXHJYtKvpLf6kv1uv3us8bLKGCOai66doX7xN2LCcOy2fer3tluSEae8ZAGYBD1Hib5xUVxyAIJFkX3msVKfAaLyGR5-6F10wqHk0ZzI2G9sOxE3FUR-lMhZvoFtqHr3WFTbkGJjhbV-t9lFCvWp5QOnbti6KxaAZ52MeGS8tPRHZVKXwX2YSyLetPKgwKY1cTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WzR9M87tLX8vY6hMFwV4-zCYgSOWtBOzWrD-oHr_tklAjEghlHzrjcca260UEzoeaDTibJjqFh7bIgMZiHaNxkFgmQQXZltTSNWYKDBosdxPF5jc39_a2ak4RmpLbO-IKt5PPE-XBGKINvzQmdeLFAL0XDcq-aeDV0AfKWbt3SPYurYpxspagJCVHqMC75B6dxU8863ZF_5aMELwnNaCuQt4zYP4NytGc_icVP7b61cFVVyY6Lia3rkryLl39C1DQo1_Mnrf_vu9UOu63AQFOQeH--tfc0lvXcoOrO_PElhKTnZ2PgXu_P2z27HR2Z7arj-2f23lbcbNPEX6OjizXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mIj0ZB2MKm8l7JzFcWShtwxZGIuBTKTFDdCOv8gjP8aW7X9JM-QDEN5V_XltN7ZaGGyVlB1x-4b4UI2CG37GgdV0_EX1SnkxO_-cGxHvKAYgH9tOdTVpvzj-pY5DBLoBLQpgvbnV5R9_BddAWyt1NjUyxMzMrsKhrElyz5ZqwsvT_BLsNCXK_gVBdY_xdcbsI-GJF1iSfWVqloCLc45ahTlbJa5_l2fMw6brxWFNTbKh34UvQY_RccKAuagjJm_4LWjjdVO3wUaXoS7uyrmAkp3RQdWBvjPcZlZ9unVGReRWNlzcJTfguufHhiKxkunF_gNNuNPYLb1qbuqDLC9lBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی لحظاتی پیش حمله هوایی به حبوش و نبطیه الفوقا در جنوب لبنان انجام دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/123038" target="_blank">📅 14:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123037">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
علی باقری، معاون دبیر شورای عالی امنیت ملی ایران، امروز در حاشیه چهاردهمین نشست بین‌المللی امنیت در مسکو با مشاور امنیت ملی سوئیس دیدار کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/alonews/123037" target="_blank">📅 14:46 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123036">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
العربیه:  رئیس‌جمهور ایران و نخست‌وزیر پاکستان امروز به صورت تلفنی گفتگو کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/123036" target="_blank">📅 14:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123030">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BCeV8pUJtPbod4JyF2x22rh2qpRZRO-ZbHu2NlS5fY7K-LCIiHqiTgchAZ9Xa1y7fp24HgZcnOurKx4QZLuowGwkcLis1gGe9MbFLqfBI4G7MZ7ovpcCGwRekCX1AbuhjZVgJzencDkhgGmsj5ITP2RtvwFTSlQDQPr4xCpXmns8os7YjRgLGGE4xNsQAwUn2RwErw5MTtxJa2CY0mNIi0a7d_BNLzA9VuMQf9FHVdWmavdvq_IHZfV2G5BAtRyoxZVRwK9n5eKZHYsH9UEXSGwYa8VFvefaTofkMczytnJwBB-srht-ghNgqonv1svogNxgxaDtg3JT8t2rTbmKnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oa_OVQL7RuSbZ_E3yS-R4ql9sQIH-vv00Yz0yyr0BFPDdV-JxB5hL52XjTaddHxDw_bgdKwZLDnKfDl4Rg1xDSGgvTNwvBAB6TRX0CCXdgyojiu7oHI9ymVMfbg-XOdJEHcn0piBNNcNlLspgc4DTAtYL0XZf_V1AQdpvSWFgYvIdrsz7Q6H4aAhVEwNW-xYw_HxXJpGYezkObpgJF0zGbwtlILmKofjUjEa8dqHrW3YWW2_-qBgyWFeFiTxxK7YM0M20ij0mMnRAwDidiPQTITTil0Lpul_5WOjlYqeI3FrMQ4pok8-cBnbcqUM3mkSUHDFmM9KVyy2CWXPCb7k3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p7xLgHK2R5Gyb720Wg-VC5oZmvx8w046HjbGBGckgZbQv2r2e9yQVGkcyoNETbVwlL9y9MAkOdwDeX6Ai-BDbpik1gko4u5tEwlY50r7MsbKG9jUVKg6WkKZIelaeKG0JkWqGLHr6fD0n59kCIhmtCT44Y3oGdKR6UtXNVnt6HAaMYEC7FiTISzbrVoztIzvCYrrDc1fNXA8_u2weyIxhUxpInx3G2m7Vr_5vCA-Mkzq1wnYhUanxaf6Bb9kgwBiYdF3PDdzD-vXnoHdCz4tmsJb9ar7gnSfbQmfkXlshhIs38NilL8Rmb6n3iJSQ5zSDv2S80A30-sYQ_mPZ9_kIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hTDuOHUwyi-UIM2vgxoNN6t4pF1R_XA81ItqEQb1xnVznxi_NwmzBMIWddfTSnEOiiZP0FQrbZ9P6JEPutJpSWXBskGaiABi82lyLOIc8sgblMeeQY7iXVrlS4pNDk1VPa0xLu6rko5JzkAqP0yi7-lEBMLtMpUPy4YFnPv1XzJc86FwRAujH4QeGPOx4LMueeh1SdXmFO4iEx7Yn8xJWlHDF7BdIa-ncO6JICEEVvtnjJ2LU59fghXQxfda4HPQy9T4ylCK29XBVo9UeZkytAotszftTaXQ95C5hZ9jtU7J1iR1P4J-p-1vqfM-3Y8XZrDJsno90pvWndT_82vekQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aH-8hrFxCyk1npcWs-I99Gpmv_MzGoPBAv88lHYT3ZWYIFl8U3vAgQjpHVFLIBkRV6NXEiCoCMSNmGV7Z3_mHPBiAkVXSfi5QHekVHe3PX2OMA-gmcW8wjr2xnOpQXT41hP2_h_pigf3qgHg_Wlz2watbFdaH3aFGPXdfUBhAFB7CswzLFEh_ozxA3v24nOueLGH6f9BqM-Smar4FGkM7K68m3pPZ5LsIGnwjG3eRyu_DgotGlZ-Y5RXs8LVMXp95sivOtkAkIy56Xg1awUqhl5QzZqPodJvMqAS1jyKhxY6MpNTCwvWLB_a8o22IHF55sLn15G2mlasledXxyy1ow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24df64f5f1.mp4?token=rGljknLxaRdbXoo9zdivkbU7RwIcigA4GWV2V1dQQFvGxUbtc6nFPJ2pwhPSfukJ-axf6Un0FYAjDaV-a7oiIVp4vJ8HDlfybiND0tV4XBAGA9vTEKCbK1qR0iOdIKDEAW4B3_fYIJYGDyRu7Ty61fiN_kBtR-QTv6l5YhvupS-ONsiRUZRUfjEhaTI3AgGZ9sGU2pe1gXYm7SFuTO7zwCGkk30nuOHALJidI1eXSptpYTR7a81L0Ap2WsPbaTSx8q0Kk2_2rI73F8FLFX349HSuZ9OKiYfCzi4EAMc8xFr0DuysuHmthJyjlRHvv4DTQxKB0iu2BeIzd7k6TA8Pig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24df64f5f1.mp4?token=rGljknLxaRdbXoo9zdivkbU7RwIcigA4GWV2V1dQQFvGxUbtc6nFPJ2pwhPSfukJ-axf6Un0FYAjDaV-a7oiIVp4vJ8HDlfybiND0tV4XBAGA9vTEKCbK1qR0iOdIKDEAW4B3_fYIJYGDyRu7Ty61fiN_kBtR-QTv6l5YhvupS-ONsiRUZRUfjEhaTI3AgGZ9sGU2pe1gXYm7SFuTO7zwCGkk30nuOHALJidI1eXSptpYTR7a81L0Ap2WsPbaTSx8q0Kk2_2rI73F8FLFX349HSuZ9OKiYfCzi4EAMc8xFr0DuysuHmthJyjlRHvv4DTQxKB0iu2BeIzd7k6TA8Pig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات سنگین ارتش اسرائیل به مواضع حزب‌الله در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/123030" target="_blank">📅 14:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123029">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udyDYKI3GIKN9fydUWyn5R6MAcJQGJpOA2jocu4tKrMQ2cbhXSLWloBGfl_e3PgFgHq20TdUa9WCpgqJxenma_D7r60XOpxDJs2wNx9mnrcHciEzphi9VKOzNWc1C8ZP0Wsbfgp6mF4Cdkng1UPDj-J2xynac8cTtT6xL5jpHLDrZwfxJISaE8Fts2qUl39lf_h1KIDXbi0F3RWGOwX55SKsrHqQRB94h1gkTW5Ts788yZNgGD2VRRMi-Z_QoUfTWjce6dkeRS6FHG9FvCeb-oldbI_JiobO1uV4IpU-v-FNBGpKA7fe8R3fGQkVpaC9t2lEcOT1mK7P_Q1bNcs9Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش کانال ۱۲ اسرائیل، زمانی که توافقی برای پایان جنگ ایران امضا شود، تمام هواپیماهای نظامی آمریکا ظرف ۷۲ ساعت از فرودگاه بن گوریون اسرائیل تخلیه شده و به پایگاه‌هایی در اروپا منتقل خواهند شد، در حالی که در حالت آماده‌باش باقی می‌مانند تا در صورت از سرگیری درگیری با ایران، وارد عمل شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/123029" target="_blank">📅 14:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123028">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aded17f1da.mp4?token=txEmZdMAveJD0TTvzIe2j8gwr81YoLrsoAG__UOf0npQ7XuTWwyANi9U5BiCMiYasjdVgXclbD-vQCaLx6VWBjC2axm9SZyfhB2zsWu8YwUu38CbaNC39YX8xAAEYTHLDjBTZc_zk1Nn3CYS2dQ8-KyeSnD8Tub1MjoSfwmd6puIs5Ybu7uMSkYTz3iV8fKxvYWikrIVgZBiesp-uk6S05K0Ycz1YkqAxiwqGtEx_bzYURXe6n62s4tUeweimY4odRGF88ktUyp2zYNYpaDKAhPYg7x25AXrvYhOfwptsPa41IruReruI6tUtGFo-olId1oQKG_Pe6wn6xTjY6aWWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aded17f1da.mp4?token=txEmZdMAveJD0TTvzIe2j8gwr81YoLrsoAG__UOf0npQ7XuTWwyANi9U5BiCMiYasjdVgXclbD-vQCaLx6VWBjC2axm9SZyfhB2zsWu8YwUu38CbaNC39YX8xAAEYTHLDjBTZc_zk1Nn3CYS2dQ8-KyeSnD8Tub1MjoSfwmd6puIs5Ybu7uMSkYTz3iV8fKxvYWikrIVgZBiesp-uk6S05K0Ycz1YkqAxiwqGtEx_bzYURXe6n62s4tUeweimY4odRGF88ktUyp2zYNYpaDKAhPYg7x25AXrvYhOfwptsPa41IruReruI6tUtGFo-olId1oQKG_Pe6wn6xTjY6aWWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرگزاری فاکس نیوز: جزئیات نهایی یک توافق احتمالی بین ایالات متحده و ایران همچنان در حال مذاکره است، در حالی که تنش‌های منطقه‌ای با امید به اینکه یک توافق می‌تواند از بازگشت به جنگ جلوگیری کند، کاهش یافته است، برنامه هسته‌ای ایران و تنگه هرمز را مورد توجه قرار می‌دهد.
🔴
مسئولان منطقه‌ای می‌گویند اجرای توافق مهم‌تر از کلمات خود توافق خواهد بود، هرچند مذاکره‌کنندگان همچنان در حال بحث درباره زبان خاص و جزئیات کلیدی هستند.
🔴
مسئولان درگیر در مذاکرات می‌گویند همسویی گسترده‌ای در چارچوب پیش‌نویس مقدماتی وجود دارد، اما تأکید می‌کنند که هر توافق نهایی یا یک «توافق خوب» خواهد بود یا اصلاً توافقی وجود نخواهد داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/123028" target="_blank">📅 14:31 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123027">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63369dc297.mp4?token=qhTqSGWrHPDQthxGjGCxAuD7QZKDe_K15Ov_FwgxZlIEpozcaUHgnGilu9T2Dqiu5yMEz3K9Zj_mpAstSp9RM6l7wD953mPfAPhKmEG4eJuz0V-joFOMt5tZM197NhuzP7y0U_uaA_rvUkq0e_D5qyZ8KV9mYtkPB7SpdG51iFfgeNTPHjaQObjO0UaBZNLFDIei1NWBX-zOCcwsA-MDKnTfuCxKeYdsnhFbTsIhiaFGYrI-EaDGYte0gjWApWB57b1aMbcTs77-rfYRCoGjIHlt1uILhk-B0mItMqKRJ9OdllWoe_4VDTCzHv3kpQJXuRJPCNnNezFil3LMtQSkBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63369dc297.mp4?token=qhTqSGWrHPDQthxGjGCxAuD7QZKDe_K15Ov_FwgxZlIEpozcaUHgnGilu9T2Dqiu5yMEz3K9Zj_mpAstSp9RM6l7wD953mPfAPhKmEG4eJuz0V-joFOMt5tZM197NhuzP7y0U_uaA_rvUkq0e_D5qyZ8KV9mYtkPB7SpdG51iFfgeNTPHjaQObjO0UaBZNLFDIei1NWBX-zOCcwsA-MDKnTfuCxKeYdsnhFbTsIhiaFGYrI-EaDGYte0gjWApWB57b1aMbcTs77-rfYRCoGjIHlt1uILhk-B0mItMqKRJ9OdllWoe_4VDTCzHv3kpQJXuRJPCNnNezFil3LMtQSkBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک مرد آفریقایی به همراه چند تن از دوستانش قصد داشت تا معجزه حضرت موسی را تکرار کند اما ظاهراً موفق نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/123027" target="_blank">📅 14:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123026">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNylDxjtJUdBYcMTtsEDpE3jLkBZ1uXi2B32dp62ACgctYm9S-JvnW4j6NXYmVhU8JDJs70VaPrMhtc32DGCKIa-q6xfZHx1OSuS0d1ZjL2uSMsnR7kbsouSVggg-T0Ixv0KzPgJb_yif4-1FaM-IacMo8Kt5t6ekfG4Qv9T3qbyEQPCRi1Fg0sMqSEpfGP_mnoMNtoHvvxWW0pjnaWqJ6Cw6PoC9bM27Y2EITwkfv-9k70QMsWYqS9rhZV2Hu_vSfeDcHDK2tFZhdrfwtp4OmsUgs9HjxxyO7z_EM07HQOPYpAFbsaXNFGyzo4Js5IFGHRTsM4U966AlYu0nGE-5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/alonews/123026" target="_blank">📅 14:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123025">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a909976f6.mp4?token=JOl2SbI033NNZDR4f6F572u0JFEqZYaOVllzwKfOep0beJk3v86WGzFyaiRdPJiM9ZGXf1yCnEaQ-9R2N6QgvCWxDcYlc1bh2Cfnwi-Ucie56cuRm26qxLlMamMrt2QafeBRmagyfIxTYCJKhSBmcB45U2jzUaeRKL71UvqclXq3ErPYTxJTVaU7NiaFRWhkgwLTlkVb4iysqxX0CXkOr1AN5D-1b0aVp4d2U65LCgt0sOsomr_MgrWbvdhiqrwszmgzk6CiFQim-nq7MyzgzpHKbelcOfb4s_OmIJmcPWUNMq9rs5ZfvHcFEBzLZqRYEA4GH2nMtXIpCXZUyogV2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a909976f6.mp4?token=JOl2SbI033NNZDR4f6F572u0JFEqZYaOVllzwKfOep0beJk3v86WGzFyaiRdPJiM9ZGXf1yCnEaQ-9R2N6QgvCWxDcYlc1bh2Cfnwi-Ucie56cuRm26qxLlMamMrt2QafeBRmagyfIxTYCJKhSBmcB45U2jzUaeRKL71UvqclXq3ErPYTxJTVaU7NiaFRWhkgwLTlkVb4iysqxX0CXkOr1AN5D-1b0aVp4d2U65LCgt0sOsomr_MgrWbvdhiqrwszmgzk6CiFQim-nq7MyzgzpHKbelcOfb4s_OmIJmcPWUNMq9rs5ZfvHcFEBzLZqRYEA4GH2nMtXIpCXZUyogV2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش سوزی پشت بام مجتمع تجاری در شوش تهران
🔴
سخنگوی سازمان آتش نشانی و خدمات ایمنی شهرداری تهران از آتش سوزی بر روی پشت بام یک مجتمع تجاری در خیابان شوش خبر داد.
🔴
با تلاش به موقع آتش نشانان این حادثه بدون سرایت به انبارها مهار شد و افراد نیز در همان لحظات اولیه از ساختمان تخلیه شدند و این حادثه بدون مصدومیت به پایان رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/123025" target="_blank">📅 14:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123024">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c4d523ec4.mp4?token=v1dethEPWc0LHbpg69SMP42fZHys5D_aE92P01sJ-IpgtoFypaU0pFlLnbZU3t_ygWszC3EZ0uZCOJv7cSKXWe430YNgQFhyu_Iij9Vm3RIu3asLo3xrkNaWFYshJu-ThSk18eF9wNTIqzKqSeOvakdu_0yjgjm1nTyVU-uGgGqpDU25W1RW4HBp2SIejWvTnkBIG1ntvbBLLAyFo5nNCephlRx-ZcTfCPyjUxbt-boaO654bs1G9-ZmbiAMCvwuxxiQd3o9PkDfVsfU1Siz7xAXert_p2VV7grs8luOaKb_Cxz3bFjMvPJ95araqc1gWqK_4aLEEXK2t130fkQdfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c4d523ec4.mp4?token=v1dethEPWc0LHbpg69SMP42fZHys5D_aE92P01sJ-IpgtoFypaU0pFlLnbZU3t_ygWszC3EZ0uZCOJv7cSKXWe430YNgQFhyu_Iij9Vm3RIu3asLo3xrkNaWFYshJu-ThSk18eF9wNTIqzKqSeOvakdu_0yjgjm1nTyVU-uGgGqpDU25W1RW4HBp2SIejWvTnkBIG1ntvbBLLAyFo5nNCephlRx-ZcTfCPyjUxbt-boaO654bs1G9-ZmbiAMCvwuxxiQd3o9PkDfVsfU1Siz7xAXert_p2VV7grs8luOaKb_Cxz3bFjMvPJ95araqc1gWqK_4aLEEXK2t130fkQdfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
70 میلیارد نخ سیگار در طول یک سال در کشور مصرف می‌شود
...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/alonews/123024" target="_blank">📅 14:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123023">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QktVVmteaww19QT7CAE_60I6nEX8EP_WpO5NY8-iq_4qS_LtcbGekcrrBrE7wnorYhbJlDpKuCJCJwaWkJqIzLITZ6fjj1YEOVMCvCGL2YPIfnsSgeMOQ4kYY0gbkrMj3JNewUFL_319Xq3Ju9e8cuFsrf6keyWKslNGSEq5pi9VKT_6WN9hoZjtUYBFk4Iz26oNZ80Gp9tLfCItz7zpIjbJnEWCHy5GR4Qi-4fp6iiHIgTZ60Su6Rxmg8YrMZkyfZas5Po3PMA3aXYYG_aQd17Eq3wzgyxC56J8ambB9YgtPzfLzJDZZaSCwhnvS5ju7Yv44f_rxMiP92Q203g3XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همراه اول امروز در پیامی به کاربران اینترنت پرو اعلام کرد در صورت تمایل می‌توانید اینترنت خود را به حالت قبل برگردانید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/123023" target="_blank">📅 13:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123022">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCesn2Wh-rwaERF9hPqPDBwj9pGpEsE8w7SwPB2sTP6jdsCrPsljysrnrQQY1PgrCKH_xXdVfhpacepgU7Fu_rYxpNPlGS6JObeu7Me8DqomKNr9jYwgOXWeon50A1bcJkMzc88y4KlUW7hbRcNBOJF7cG5xa63bl3F_q31qpRWDfl03bRHdmPP98f1EezOfwKSh2znsTnXx9ES6f_ZN6Cb-Fjle4FgbpUq73wVi2c1BA-gFxkR29c2vrG-3RIQxrVzYQiDTFHOWIsRhsnYsX16wOdXsOoE97Ei-ARBgmxvEfIjQO6Wga9ckxozx_yanXmkzMVWGyqobpFT4jUGq8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایالات متحده در حال کاهش حجم نیروهایی است که برای اعزام به اروپا در مواقع بحران برنامه‌ریزی کرده بود؛ این اقدام، گام جدیدی از سوی دولت ترامپ در راستای کاهش حمایت‌های نظامی خود از متحدان ناتو محسوب می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/123022" target="_blank">📅 13:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123021">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
رسانه I24 NEWS: نیروهای دفاعی اسرائیل (IDF) و فرماندهی مرکزی ارتش آمریکا (سنتکام) در حالت آماده‌باش بالا باقی مانده‌اند، در شرایطی که احتمال شکست مذاکرات میان واشنگتن و تهران و صدور دستور اقدام نظامی از سوی رئیس‌جمهور دونالد ترامپ وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/alonews/123021" target="_blank">📅 13:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123020">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8bxCd6NEMal6TZFuPfoTI0X7ghJpVG61iCiDSP7oFPOZcKfIqDYxkQc6lIc-BlNWeZKcPoJC3yQ5cYSwwIfFWLW-E-krXqem1Vc8NFDdqj-iLLZcSaB68TlG7TdeeliXxVltWXB6aqtf47hDyyNrPAAJfnD0Cnogd822AuZLPsCJvEltL-XmVsvLbyfPP2fXZQW5Re2Bf4Y9cDxONE2Vk-g-RkllQWc8jV7PJ2XnZ2b4PZJ6s86BE9PojDM6sWGTAXA5vvMUEG582XX7QtXxhIew40tAPxdxO3o1X15NCrVjVbNO5Swfmct7_-4pCNBMymFAmkQsyZ2n8oN3mcpeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با تصاویر ماهواره‌ای سنتینل-۲ ناو آبی‌خاکی تریپولی آمریکا رو تو دریای عرب دیده شده
🔴
الانم با اسکورت یه ناوشکن داره حرکت می‌کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/123020" target="_blank">📅 13:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123019">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
پارلمان مجارستان امروز قانونی را تصویب کرد که عضویت این کشور در دادگاه کیفری بین‌المللی را حفظ می‌کند، و بدین ترتیب تصمیم دولت سابق اوربان در سال ۲۰۲۵ برای خروج از این دادگاه را معکوس کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/123019" target="_blank">📅 13:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123018">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
نتانیاهو دیشب در جلسه کابینه: محدودیتی برای حملات در بیروت نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/123018" target="_blank">📅 13:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123017">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
امتحانات پایه‌های هفتم تا دهم به صورت غیرحضوری و از طریق سامانه جدید شاد برگزار می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/123017" target="_blank">📅 13:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123016">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6fda00612.mp4?token=u-9eQ2fqBrQPJIHFVTdeU58K767kHp6jXJn_kWRiDwPQsEkR2CLDRjvO-P9aXaF8PyNGfEBJP0SxYpVN86fzZ3EcPpKmQca1tYmmZO8HFjvPBAYpmkvjvOPIhMD5109a3LFA3pmMWpQvF0DwuihIcDhGVBNJ5pw8iRICstPDYcldCxGTaaGOxO5yzKOunV0dUKSkJhHYCt3C4xMW21rdPMTjje3hjW3dm68U3Nrb6IENpWxf1sc4KsjUpiVhX48B7URdWbREiGwwJTenFGxb1o2cBSveQ-3iqSYLpJ5-v0pywT6B4hzs9-G1yC9o-V81uQ8S9I0Oq-rY1zE6zJwrXqc9HpzgfJL5p5Ohu2lcjJg_8Psbl_IXT9x4TF6363nzUhKkIhPdHfwktkwjrLzpOaA-cQwwww2PEmKV45ixWKvqK_7mC1EJ2RMgSjk0Ebzsn-dMRhbzW6plIPVcAzp6IlTGQKmhmc4As8384Mq0uNDnS6MB9xiBI2hvcj1Xd8MXxx-XGHI_BRiM0Wzyz2sM6jfiaB4Zkrah24xnwEZeJDCscKdLjSSxZ4wND13feJBwYld6oiWSju1DIZyox63ciagoRPNO2ZcUXfw_Pe0Jd-0tvg4oEafc8CPS-zL5qUUCReJ_Obd8zLxcd1drQwHryLUfOm9Gj6nA4h-a49T-K5E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6fda00612.mp4?token=u-9eQ2fqBrQPJIHFVTdeU58K767kHp6jXJn_kWRiDwPQsEkR2CLDRjvO-P9aXaF8PyNGfEBJP0SxYpVN86fzZ3EcPpKmQca1tYmmZO8HFjvPBAYpmkvjvOPIhMD5109a3LFA3pmMWpQvF0DwuihIcDhGVBNJ5pw8iRICstPDYcldCxGTaaGOxO5yzKOunV0dUKSkJhHYCt3C4xMW21rdPMTjje3hjW3dm68U3Nrb6IENpWxf1sc4KsjUpiVhX48B7URdWbREiGwwJTenFGxb1o2cBSveQ-3iqSYLpJ5-v0pywT6B4hzs9-G1yC9o-V81uQ8S9I0Oq-rY1zE6zJwrXqc9HpzgfJL5p5Ohu2lcjJg_8Psbl_IXT9x4TF6363nzUhKkIhPdHfwktkwjrLzpOaA-cQwwww2PEmKV45ixWKvqK_7mC1EJ2RMgSjk0Ebzsn-dMRhbzW6plIPVcAzp6IlTGQKmhmc4As8384Mq0uNDnS6MB9xiBI2hvcj1Xd8MXxx-XGHI_BRiM0Wzyz2sM6jfiaB4Zkrah24xnwEZeJDCscKdLjSSxZ4wND13feJBwYld6oiWSju1DIZyox63ciagoRPNO2ZcUXfw_Pe0Jd-0tvg4oEafc8CPS-zL5qUUCReJ_Obd8zLxcd1drQwHryLUfOm9Gj6nA4h-a49T-K5E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور ترکیه اردوغان: ان‌شاءالله این دیکتاتور به نام نتانیاهو، درسی که شایسته‌اش است را از مسلمانان جهان خواهد گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/123016" target="_blank">📅 13:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123015">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1ecf0a6d3.mp4?token=Zoqj2r310_Uh-IddWghzZt32iKtTlWHjup-mCqnsxB95foRAjFBMJebcYINNqQ5Kzf-0zkzUmaWXm-UaMqtG9_5r6d9j02KrAYxZSp6QWW1klM2E3jz_ffjqSGpNi4Ol0496JvD3m53gl14U6-vpgQY4DvmdD8NnabYmDnDO8nna7xfZP6WywWLzBQGRwFoyPKVjFA0J_nfVIk5ycBm2mcd0jZLmUAuCvPByfgpg_WFvyW9WTYzffiTRF1FeBCL4kV_iL7DTElj8sgH7VZmWJO25WJg-QW-vVY72mVP0uvHHeq9v1DPPPWuNOrEosHX8yvfLskoUvJ9TUzdgh7pQCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1ecf0a6d3.mp4?token=Zoqj2r310_Uh-IddWghzZt32iKtTlWHjup-mCqnsxB95foRAjFBMJebcYINNqQ5Kzf-0zkzUmaWXm-UaMqtG9_5r6d9j02KrAYxZSp6QWW1klM2E3jz_ffjqSGpNi4Ol0496JvD3m53gl14U6-vpgQY4DvmdD8NnabYmDnDO8nna7xfZP6WywWLzBQGRwFoyPKVjFA0J_nfVIk5ycBm2mcd0jZLmUAuCvPByfgpg_WFvyW9WTYzffiTRF1FeBCL4kV_iL7DTElj8sgH7VZmWJO25WJg-QW-vVY72mVP0uvHHeq9v1DPPPWuNOrEosHX8yvfLskoUvJ9TUzdgh7pQCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه هدف قرار گرفتن انبار تسلیحاتی پایگاه شکاری دزفول در ایام جنگ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/alonews/123015" target="_blank">📅 13:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123014">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhjG_DOoiVuhL9sm8QSoWd0abis_B81xyRiGkyczU-p-K5RlBBTGYl2FDXEGvkO9nurW3KFg_C_su5-Iu1blcclGc_IJZN2TBDAiYXi6u3fJJJp9uECrxV5xxH4mFteV4fRYxbd4rhBHpvxem2l8kMm0tR0JrMPFaEpGc5oG-PgpB5Ov8zdNr2no6xvd5ZShaV6_mTJbXcC3dRbd1P6oFVaM6-fncZWOVQiqXWHGtmWn2Lk-1rdsZ3awF3OFoqZM8j_6pscGoe_WIpgs5jSE3OvSqOKZj7BOZnFIxxcuZHsJ4Xq_EgKZlhBSpADC8hNMAhRStk1Iysia88G5Uan8dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سالود کارباجال، نماینده کنگره با انتشار نظرسنجی مبنی بر اینکه ۷۷٪ آمریکایی‌ها معتقدند سیاست‌های ترامپ زندگی را گران‌تر کرده نوشت:
🔴
«مردم آمریکا به‌حق از این موضوع ناراضی‌اند که قیمت خواربار، بنزین و دیگر کالاهای ضروری به دلیل جنگ غیرقانونی ترامپ سر به فلک کشیده است. این دولت خانواده‌ها را زیر فشار گذاشته بدون اینکه پایانی برای آن در چشم باشد، و جمهوری‌خواهان هم دارند اجازه می‌دهند این اتفاق بیفتد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/123014" target="_blank">📅 13:01 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

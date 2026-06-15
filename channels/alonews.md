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
<img src="https://cdn4.telesco.pe/file/gpgC7JP2ulAj13MLrXj5_iMYk0R6E2sfXqQmrBryg-Moud7_cW5P-adcM1F2PovnVR2fkS9QSNIzK7nNWCJRt1H4vBg4luNd7PxbbfwEmse8AlwHjbOZepFM_Uxw7qK02po_2PCnZcnFu9NDnGtwiXTBV2KRrn7TFnymmrokhtSimxXYwPxeGml6XxbXLPcZM3ouOXjzrlIYIXF-d4gN6C4em_vCwoC81tNBaJ_O3-bDfEY4x9iKkRU8U2J_lvymcr_QL6cbBTPLzoaULpDaMWjQGoueFhYKkSCL0h5X_d5BARCvexvZJU5FoWdXBcyxFdwk91UCL_7sZ5U4fmRxQg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 975K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 18:28:11</div>
<hr>

<div class="tg-post" id="msg-128248">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
کمیسیون اروپا: توافق تفاهم نشان می‌دهد دیپلماسی نتیجه می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18 · <a href="https://t.me/alonews/128248" target="_blank">📅 18:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128247">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
بحرین از یادداشت تفاهم میان واشنگتن و تهران استقبال کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/alonews/128247" target="_blank">📅 18:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128246">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
عراقچی: جمعه تفاهمنامه ایران و آمریکا امضا می‌شود
🔴
اقتصاد ما نباید خود را متکی و موکول به این قبیل توافقات اقتصادی از طریق مذاکره با آمریکا بکند
🔴
در راستای منافع کشور، نیمی دیگر از راه مانده که باید طی کنیم که نیمه سختی خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/alonews/128246" target="_blank">📅 18:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128245">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
بدر البوسعیدی، وزیر خارجه عمان، در پستی در شبکه «ایکس» گفت که جامعه جهانی باید از تفاهم حاصل‌شده میان ایالات متحده و ایران استقبال کند و از همه کسانی که در تحقق آن نقش داشتند تشکر کرد.
🔴
او این توافق میان واشنگتن و تهران را پیروزی دیپلماسی و منطق سلیم توصیف کرد و تأکید کرد که در زمان مناسبی به دست آمده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/alonews/128245" target="_blank">📅 18:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128244">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
یک حمله پهپادی اسرائیلی خودرویی را در کفر تبنیط، جنوب لبنان هدف قرار داد و راننده را کشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/alonews/128244" target="_blank">📅 18:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128243">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3UcdbDWbMXl7VTBAbDUNQZ9NtC2ErIW-rO-FqQU8zbd37b_oMiEshqlu-5YD7DP79bw9cWwp6YedvWwKy2Mhp3aCHhwNYAs1pLro6W2WY_APFfIatfkF9f2IEj5MRXajBP0364it9uUQEPcwJPJjr6xkoInDXOFCQBTF5UN2Yg9yS2YlScunRA3_zOz7EyWeEsGn6FQC_XeeBm9i4o2ilC99fHCh0rgPkum1Fu65WczroXc1kbqJvgsKpnWwdx7akI6Adhamd3OODxJspwmxE7rwsjyBFLLM_XGmtNz12CXcCMCof0kZ4xej1ieEJ3C92kK5yr8vLseLsTxer6alg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: متأسفانه، اگر افراد را از کشورهای جهان سوم وارد کنید، به سرعت خودتان تبدیل به یک کشور جهان سوم می‌شوید و هیچ کاری نمی‌توانید در این باره انجام دهید
🔴
آمریکا را دوباره بزرگ کنیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/128243" target="_blank">📅 18:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128242">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
رویترز به نقل از ارتش آمریکا: محاصره بنادر ایران همچنان ادامه داره و در انتظار تکمیل توافق با ایرانه که قراره روز جمعه انجام بشه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/128242" target="_blank">📅 18:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128241">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1QIcq_4wlnXkrGBEIWwNW9xkF59nsAvA_D-8xM_9FHhLA-eyRO88i8_CD3nGwFdmuLq0ClEpswJzSOU5DngcviqIBVcD-SrUGlahJ3zZqPq3cxdezlmSXIOWwifPZozTYuaZZ5ngKxtPoG_AoEqLqIeo3CN3SHrRzGb3-fOzN7aOFsKCIrzobtwZXjjaei-nz4_SOpsowiw_1BuSfbU0KtZ4K3vZ2QqlS-ERXmLV_qW7Nd9H7ZJWlG922oO3_bNp8Eb92KpsLwVvyvkIjEoGmYPOeFGHJ-yKc9tCkFyDs3gW3rdHxclUhhmQIm9ojL0ahBmBBrpiUbJOeIL25D9sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لهستان هنوز جنگنده‌های میگ-۲۹ باقی‌مانده خود را به اوکراین تحویل نداده است، زیرا مذاکرات در مورد انتقال فناوری پهپاد اوکراین هنوز ناتمام مانده است.
🔴
سزاری تومچیک، معاون وزیر دفاع، گفت که لهستان به عنوان بخشی از توافق، خواهان دسترسی به تخصص پهپادهای میدان نبرد اوکراین است.
🔴
در صورت نهایی شدن انتقال فناوری، ورشو آماده ارسال این هواپیما است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/128241" target="_blank">📅 18:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128240">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c73cb88b33.mp4?token=pMopZAWV8DSb1jTgyoPfgG-nbZmdbUqr2nnuqtDOcKWLzVzldALo3pFMnCd1cMYhpaBiPCyn1qMRgRtIc69IAOaGSQPD_ORyVP049-FX1j3mThNiR_Mc3A_HqnHXP33aHqO3WMCd5l1PMlW6hBUBiVhURitq-qBhShAJQg_C4m-8-ukecncrRIvidOHko7qr62k2Y-COP8A7R3BD2ojn8nc7KtjPZJx7YntbdxbvRjV34M2RTLg-j_2VQ_3jNDhjo3UA8Uop13AF-oBfNf_fowKjk_DsmYAQxtkrZTgyQHa-LGh4msJpiyyLeVroD0_d6V7oXgD_JMYoUk1y1BGBNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c73cb88b33.mp4?token=pMopZAWV8DSb1jTgyoPfgG-nbZmdbUqr2nnuqtDOcKWLzVzldALo3pFMnCd1cMYhpaBiPCyn1qMRgRtIc69IAOaGSQPD_ORyVP049-FX1j3mThNiR_Mc3A_HqnHXP33aHqO3WMCd5l1PMlW6hBUBiVhURitq-qBhShAJQg_C4m-8-ukecncrRIvidOHko7qr62k2Y-COP8A7R3BD2ojn8nc7KtjPZJx7YntbdxbvRjV34M2RTLg-j_2VQ_3jNDhjo3UA8Uop13AF-oBfNf_fowKjk_DsmYAQxtkrZTgyQHa-LGh4msJpiyyLeVroD0_d6V7oXgD_JMYoUk1y1BGBNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس کمیسیون اروپا اورزولا فون در لاین: تا زمانی که لبنان در آتش می‌سوزد، صلح پایدار امکان‌پذیر نیست
🔴
ما خواستار آتش‌بس واقعی و احترام کامل به حاکمیت لبنان هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/128240" target="_blank">📅 18:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128239">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cc712a5cb.mp4?token=tfsa_IZ_rT9tl5iHjqp12sK39Suw_9iQrHfVXVN8u8XjMS3FRAgcQXcYu3xp5ujCoe_NuqucJQ7Im3Wdx2BYtXbv5aaV0zZd2U_iPCvolhaxv0kHKnTWyrHxAaeQdCPoFQSQeKEKGc7KURdf5K_SlZDdWKLyjkO4Wc_v8lUCi4GjqxbySaTgtnTPQh2E82sGAFEC2f4Z2fIe64th7s2I-MlMLcKNyPM8rbQUjFAU1IfU7_mkRSr6XwberAQvTXDmChRxeR9g2GE4i1WfX8baU4srjEfuA3ixAmQXmET58XBJz9NUmN_zrRvEN9QA9Mv_FwOQdEfHOSodHSWCmZToag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cc712a5cb.mp4?token=tfsa_IZ_rT9tl5iHjqp12sK39Suw_9iQrHfVXVN8u8XjMS3FRAgcQXcYu3xp5ujCoe_NuqucJQ7Im3Wdx2BYtXbv5aaV0zZd2U_iPCvolhaxv0kHKnTWyrHxAaeQdCPoFQSQeKEKGc7KURdf5K_SlZDdWKLyjkO4Wc_v8lUCi4GjqxbySaTgtnTPQh2E82sGAFEC2f4Z2fIe64th7s2I-MlMLcKNyPM8rbQUjFAU1IfU7_mkRSr6XwberAQvTXDmChRxeR9g2GE4i1WfX8baU4srjEfuA3ixAmQXmET58XBJz9NUmN_zrRvEN9QA9Mv_FwOQdEfHOSodHSWCmZToag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس درباره رسانه های ایران: رسانه‌های ایران، به ویژه رسانه‌های تندرو، بدون اینکه درباره آنچه می‌دهند صحبت کنند، درباره آنچه به دست می‌آورند صحبت خواهند کرد.
🔴
برای همه ما مهم است که این سابقه را اصلاح کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/128239" target="_blank">📅 18:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128238">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
محسنی اژه ای : خداروشکر در جنگ سوم هم مثل دو جنگ قبلی پیروز شدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/128238" target="_blank">📅 18:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128237">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5a403944.mp4?token=WcFLuVsuxyRPNb9-NNsEm6euF1_zI7IGvPUge8NeOLjnhloeAapTv41_aujRmJAIJbx0dgvA18RMtabjJmfBAMJYlN-GkY1Lx1SMefWjdNrLsfljl-92j0y31hD5YlcfI7QCidYsPCHN8AxMd5PsON4AJZK95iDBFDUd60Jy3GZ2iacafYFa9_ACeN1UINcNNv4R7YG-7WavqWG0ctGdOMRvgZNgeWxeVtnp0oBN42aoGU2EAMuPFQXYlK0cZ6agPUdpITNQWNL0UnsTU-hdTPjy-m860xkIGkSrSnp34Nso7ZDyddBKE5Y0n1XY0jCKW3Wm5kLZLTw-fRNuo1gSrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5a403944.mp4?token=WcFLuVsuxyRPNb9-NNsEm6euF1_zI7IGvPUge8NeOLjnhloeAapTv41_aujRmJAIJbx0dgvA18RMtabjJmfBAMJYlN-GkY1Lx1SMefWjdNrLsfljl-92j0y31hD5YlcfI7QCidYsPCHN8AxMd5PsON4AJZK95iDBFDUd60Jy3GZ2iacafYFa9_ACeN1UINcNNv4R7YG-7WavqWG0ctGdOMRvgZNgeWxeVtnp0oBN42aoGU2EAMuPFQXYlK0cZ6agPUdpITNQWNL0UnsTU-hdTPjy-m860xkIGkSrSnp34Nso7ZDyddBKE5Y0n1XY0jCKW3Wm5kLZLTw-fRNuo1gSrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دکتر جی‌دی ونس درباره ایران:
ما کاملاً آماده‌ایم که کشورهای خلیج فارس در بازسازی ایران سرمایه‌گذاری هنگفتی کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/128237" target="_blank">📅 17:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128236">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b083f878.mp4?token=AAD92v3WTqNsS9X0kzLf-ZLeWIxsy63hLmHpFa_KRxkrDDVViJEKYqTMXYl9jDt-V6qO0i4UbKPjVoj3JqE4bu4greOeZvFHI47R3RA8yCFxzsjQzPNaBb5ZyDXkNscCXeucWQhRW_bnNvSGyCGTBbJ5V0qWGVJqRRUYejo_0MKi_f_cM0ZfbkgOmcb0Rc4cPXwUmsIC1YB_ZQfk41sVKUcyrrCyUGcYjKmDfz6NYVlk9paNorKCPKNtPO5onzd-dTTkm-GaOG9QJKG1ehjEHRnMszdaAcqmS1LEuNWoSUqrIjM6do9l3o97hYjV54rcJfUmc5EhB_GDsezUuN5bPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b083f878.mp4?token=AAD92v3WTqNsS9X0kzLf-ZLeWIxsy63hLmHpFa_KRxkrDDVViJEKYqTMXYl9jDt-V6qO0i4UbKPjVoj3JqE4bu4greOeZvFHI47R3RA8yCFxzsjQzPNaBb5ZyDXkNscCXeucWQhRW_bnNvSGyCGTBbJ5V0qWGVJqRRUYejo_0MKi_f_cM0ZfbkgOmcb0Rc4cPXwUmsIC1YB_ZQfk41sVKUcyrrCyUGcYjKmDfz6NYVlk9paNorKCPKNtPO5onzd-dTTkm-GaOG9QJKG1ehjEHRnMszdaAcqmS1LEuNWoSUqrIjM6do9l3o97hYjV54rcJfUmc5EhB_GDsezUuN5bPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ به اجلاس
G7
وارد ژنو شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/128236" target="_blank">📅 17:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128235">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
جی‌دی ونس درباره ایران:
ما دیروز به صورت دیجیتالی قرارداد را امضا کردیم و هیچ پولی آزاد نشده است. این موضوع تغییر نخواهد کرد،
این یک مسئله مبتنی بر عملکرد است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/128235" target="_blank">📅 17:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128234">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
خبرنگار: قبلاً ترامپ گفته بود «هیچ توافقی با ایران جز تسلیم بی‌قید و شرط وجود نخواهد داشت.» چرا مسیر خود را تغییر داد و اکنون با این توافق موافقت کرد؟
🔴
دکتر جی‌دی ونس: فکر نمی‌کنم مسیرش را تغییر داده باشد. اساساً استدلال ترامپ این بود که ما از نیروی نظامی برای فشار آوردن به ایران استفاده خواهیم کرد و چیزی خوب برای مردم آمریکا به دست خواهیم آورد. و اکنون ما آن را داریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/128234" target="_blank">📅 17:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128233">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
پرزیدنت پزشکیان:
تفاهم ایران و آمریکا جمعه امضا می شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/128233" target="_blank">📅 17:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128232">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRB29UTl_iEz3NaXYG18r7T2U4f8GH2mfDfI9GAe_psj2MlUGlPLzGbekzZTpMFNOH0BgxmrK7pNAIJyTHCKuZInFAhzj-In6P-HNrrE4_2DYKoHiA1cDMc7kLfOsZOeqFW8_81dDwR9WmpfbTGuR21eLhCRnXWkba7KQccdCtCPDmwRR2cMVbEWmPI-nk_OJwp4kJCgCASZs-org0Ne8hlxuHgWkztW47gO19bUeGH_F3WnBS-g4V6nTUAG6ap7ns58GTAbjzz2VS7Umsvq8ZPU2udkHgo9QRsv8XB50346RgWgt4V0dZQ3nzp34VVyKmjR85DbNN1ZQiKuxrfsIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرزیدنت م. پزشکیان: فقط یک نفر از اعضای شورای عالی امنیت ملی مخالف توافق بود
🔴
پ.ن: جلیلی بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/128232" target="_blank">📅 17:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128231">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AG4gqpFmLO6DgfNqDVVrqq_3u2u3_3WMAbqHMSDZQCed1gVqlL0H3iphpERdiyZi8ljFQOnbDON-Vib1dUu8I6ugqYg67bpo1Uys6hkv1EEy5VMDQRgVIfofcTjZkIIqbCKQaInimsa4XBfFUdYkrLYX_38AHQwUG-eiPdi-K-vxH4lJDZavBqj_l813igo1x6q78w-ooFJdYLnwDorIkb7JA5OBIWq5bQNuqMgCMlxeYTjuwEYgnkkTAUQRpjYe8bEahYLEi39UoQG77d8FSa2KXuhBeaqm18SEUpKSrv0l-uCAUoISAq2BF0tWG3N5kL_ck-DuRkBeEQe6XysQmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آیت الله محمد خاتمی:
از تیم مذاکره کننده بابت رشادت‌ها تشکر میکنم
💚
💚
💚
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/128231" target="_blank">📅 17:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128230">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ونس: رهبران جدید ایران از ۴۷سال مسیر اشتباه برگشته‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/128230" target="_blank">📅 17:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128229">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fb6d0af85.mp4?token=ugS1VbfhRbNXAegG077zSOeCDHM2__1NSx4yyehd8-0ZmopDo-pxueVfeYVNUg2D3mONRspnPi5nVoN5h_kgMzlI6EzM9yhbh9uCX3HkcX-QUCXw4p1Ra3kryh-mE_g8BiPpr1iTZcqRoQWSIk6HNPc_JAHCYswybXGEyyRavexOV-TPxoPIvfqROMq6aiALmA7ag8OcctZ1IIbA4CXamjGvZl_iyHPeDQD0L6SGXOsxvGAlNx0WssMNXigecneYrtLaz6qWTPuR6SoSY9Rk5xWpY9Xq2HV7HBuxzM9iR1fr7GvKfYfcMDkZjvfVp8--i6ikRqW935jd3iIxzSkn0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fb6d0af85.mp4?token=ugS1VbfhRbNXAegG077zSOeCDHM2__1NSx4yyehd8-0ZmopDo-pxueVfeYVNUg2D3mONRspnPi5nVoN5h_kgMzlI6EzM9yhbh9uCX3HkcX-QUCXw4p1Ra3kryh-mE_g8BiPpr1iTZcqRoQWSIk6HNPc_JAHCYswybXGEyyRavexOV-TPxoPIvfqROMq6aiALmA7ag8OcctZ1IIbA4CXamjGvZl_iyHPeDQD0L6SGXOsxvGAlNx0WssMNXigecneYrtLaz6qWTPuR6SoSY9Rk5xWpY9Xq2HV7HBuxzM9iR1fr7GvKfYfcMDkZjvfVp8--i6ikRqW935jd3iIxzSkn0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری: ایرانی‌ها می‌گویند قرار است به یک صندوق ۳۰۰ میلیارد دلاری برای بازسازی دسترسی داشته باشند. درست است یا نادرست؟
🔴
جی‌دی ونس: چنین چیزی می‌تواند در دسترس آن‌ها قرار بگیرد، مشروط بر اینکه به تعهدات خود در این توافق پایبند باشند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/128229" target="_blank">📅 17:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128228">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کصاخیل درحال جهاد ری اکشنی
😂
میان ری اکت فیک میزنن و اونو جهاد میدونن و میگن ثواب آخرت داره
با همین تفکر هم همیشه.... خوردن</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/128228" target="_blank">📅 17:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128227">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f90b6b743a.mp4?token=mXtG0TrSVjvCiPMYGAfKtCChPNsBRhvyo0LJKk1S3YDGqJKVtQxBqXxdPjR_48MWpD4PY-2WVxq56M8rdiT9Na6DbccELZufizTQdNZQ_dZv0hzfRolxyXNIF-MoEXy3379CK7wXjxDhxXEl2JCiqMJVsPfN7w38Je1IEU4MnjUo41ScVIdDfRurLO8uiTZp4o8N7uy9C-doohjfPJRLj8eIS--I8SWliP_44vs_HwQyHcMBUb9pc2yDDDCpqVwe0lxyyLGd7zTbeHMFlUldqEe_xwYmcsEqaQrgAFYkTacoKT6XOdx5pC2YF73d3QTk8SxZluNYVbiWTONifreH6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f90b6b743a.mp4?token=mXtG0TrSVjvCiPMYGAfKtCChPNsBRhvyo0LJKk1S3YDGqJKVtQxBqXxdPjR_48MWpD4PY-2WVxq56M8rdiT9Na6DbccELZufizTQdNZQ_dZv0hzfRolxyXNIF-MoEXy3379CK7wXjxDhxXEl2JCiqMJVsPfN7w38Je1IEU4MnjUo41ScVIdDfRurLO8uiTZp4o8N7uy9C-doohjfPJRLj8eIS--I8SWliP_44vs_HwQyHcMBUb9pc2yDDDCpqVwe0lxyyLGd7zTbeHMFlUldqEe_xwYmcsEqaQrgAFYkTacoKT6XOdx5pC2YF73d3QTk8SxZluNYVbiWTONifreH6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس درباره ایران:
ما دست دوستی به سوی ایران دراز کرده‌ایم. اگر آن‌ها بخواهند رابطه‌شان با ما را تغییر دهند، ما نیز رابطه‌مان با ایران را تغییر خواهیم داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/128227" target="_blank">📅 17:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128226">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87eb24a096.mp4?token=Usr0ebaBpgiuHxPgX2osxMjYx4lljAUVKDVUQVjc1QLKnbVp5O9e1zHGyEZjJezJg2DXK7NNaemzAcihlwAX0lLEtrQqRZJ8YkoPBTFTHYylVtq7btQp1c0WAAcw9JRTYfuSAjHyocOLQCBUouh_OWieb3Tc5A-a36F3YaqM5D1zW1rz4QA8aGw9JY-AkwXqqPcmTBobyfCTweMrE07lYdwBec41XJNdZTFBKD3EwkfL-5Azb-OSKJUm4ToXuLc8_4dYO6C8-FNgu5nhxA4y0GRDw4WyIQHmUk_mI2syz0NAGoXPlkAHcPqi84-VX6UOwz_QBqnjNTDGrFG00chhAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87eb24a096.mp4?token=Usr0ebaBpgiuHxPgX2osxMjYx4lljAUVKDVUQVjc1QLKnbVp5O9e1zHGyEZjJezJg2DXK7NNaemzAcihlwAX0lLEtrQqRZJ8YkoPBTFTHYylVtq7btQp1c0WAAcw9JRTYfuSAjHyocOLQCBUouh_OWieb3Tc5A-a36F3YaqM5D1zW1rz4QA8aGw9JY-AkwXqqPcmTBobyfCTweMrE07lYdwBec41XJNdZTFBKD3EwkfL-5Azb-OSKJUm4ToXuLc8_4dYO6C8-FNgu5nhxA4y0GRDw4WyIQHmUk_mI2syz0NAGoXPlkAHcPqi84-VX6UOwz_QBqnjNTDGrFG00chhAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس: تعهد دادن که ذخایر مواد بسیار غنی‌شده‌شون رو نابود و جمع‌آوری کنن
🔴
همون اورانیوم بسیار غنی‌شده‌ای که در دوران دولت اوباما و دولت بایدن جمع کرده بودن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/128226" target="_blank">📅 17:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128225">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
جی‌دی ونس، معاون ترامپ:
ما شاهدیم که هم تندروها و هم رهبران سیاسی ایران میگن: رابطه ما با آمریکا در 47 سال گذشته یک اشتباه بوده، بیایید ورق جدیدی رو برگردونیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/128225" target="_blank">📅 17:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128224">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a52eea38a.mp4?token=exCl9__W2w43Uc6WYd2YFUlyCMUuwHnirAlw7iwcXm2kPAULamZOxREih7Am1wlW--cr0L3omeea4GwmcUl3Ezf3ROKh3jUAxpHlHWHVoYZ1DZVfPY9nNjntcKxVPjx5wdCga9j4ZDEuwVfwD2qtCBg10-Kx6XCnzPPrLnnbqFPvNA37ZoAOyIGqv9LUFANaoSip1EEChVmC7XuMwUggUymdONvupnhvTC89OrtkOiNRzjpKXfpIKvKJx6nO5verCqY4KgCZHfTS4yylUiHhv-u1pS1EIW2TvPsDJ9ueDZtNTYJwXHSDxuKv2DjEJm3KbG65c4GZd0Q_z-FX0hRbcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a52eea38a.mp4?token=exCl9__W2w43Uc6WYd2YFUlyCMUuwHnirAlw7iwcXm2kPAULamZOxREih7Am1wlW--cr0L3omeea4GwmcUl3Ezf3ROKh3jUAxpHlHWHVoYZ1DZVfPY9nNjntcKxVPjx5wdCga9j4ZDEuwVfwD2qtCBg10-Kx6XCnzPPrLnnbqFPvNA37ZoAOyIGqv9LUFANaoSip1EEChVmC7XuMwUggUymdONvupnhvTC89OrtkOiNRzjpKXfpIKvKJx6nO5verCqY4KgCZHfTS4yylUiHhv-u1pS1EIW2TvPsDJ9ueDZtNTYJwXHSDxuKv2DjEJm3KbG65c4GZd0Q_z-FX0hRbcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تیزر وایرال شده از دکتر قالیباف
#مرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/128224" target="_blank">📅 17:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128223">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9226ba657c.mp4?token=ehY6XYs-cO3gy90NrG-92QuMV433KggvLtDlw3d-aP9y98Zq8UpyvI3A_JrIRwg9dVakvizSN4Nsf9hUD1LZ-WjwKKjJxO_DY0RvQNqgvmPeDa80a-LbBRGyoYTVdoEXnxiEGLoADc7GuSBKRMmg3Nym8qnoij5HIDpq1wN4qLTlPvZwP-FrdKHT3Vcxz4kO9LSNP8CEYPEtz1EDdV-9cw85LMMb7ALraSSBKNVBTr71V-UGBkhtdrDdgkiPzGPRRPW07OPtoEe9ukxQshERNyFKA-IX3qltUKaMya5YytXSEylCpCg9oufsCKCII3kcRcKxMDLRqVILUnMmxnC03aCio0qNaordWxae51P6FeWNq3-u74uA3cPLZUEOJyw3AYanWklDfWXiTMMHBI5iZ_bX8ZAyP2bUjEG4p7u4J4IOMG7oq3wvfd-uXMwir_A3-c2Kea8J_4Bq7p3m1UXFTdrEOsI9OnvQjtKWFanfmW2UA8ft9Cn6-1LlR2s5xg1o0rssh666dk-UZPytGti_gvDSrFl7_P-kksElABktys2JG7CgP86xpKVuUZTvKAbbAYkaeeP7nDc7BT7f9ZQExOGbf_GhoT60a0L3vyHS-5pJLHm3uR9MfNCg-Xhs3AkYiFq5y6w3dLIxRS3SLZ51_R0VzjcyeT1tabjTc0GYnHk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9226ba657c.mp4?token=ehY6XYs-cO3gy90NrG-92QuMV433KggvLtDlw3d-aP9y98Zq8UpyvI3A_JrIRwg9dVakvizSN4Nsf9hUD1LZ-WjwKKjJxO_DY0RvQNqgvmPeDa80a-LbBRGyoYTVdoEXnxiEGLoADc7GuSBKRMmg3Nym8qnoij5HIDpq1wN4qLTlPvZwP-FrdKHT3Vcxz4kO9LSNP8CEYPEtz1EDdV-9cw85LMMb7ALraSSBKNVBTr71V-UGBkhtdrDdgkiPzGPRRPW07OPtoEe9ukxQshERNyFKA-IX3qltUKaMya5YytXSEylCpCg9oufsCKCII3kcRcKxMDLRqVILUnMmxnC03aCio0qNaordWxae51P6FeWNq3-u74uA3cPLZUEOJyw3AYanWklDfWXiTMMHBI5iZ_bX8ZAyP2bUjEG4p7u4J4IOMG7oq3wvfd-uXMwir_A3-c2Kea8J_4Bq7p3m1UXFTdrEOsI9OnvQjtKWFanfmW2UA8ft9Cn6-1LlR2s5xg1o0rssh666dk-UZPytGti_gvDSrFl7_P-kksElABktys2JG7CgP86xpKVuUZTvKAbbAYkaeeP7nDc7BT7f9ZQExOGbf_GhoT60a0L3vyHS-5pJLHm3uR9MfNCg-Xhs3AkYiFq5y6w3dLIxRS3SLZ51_R0VzjcyeT1tabjTc0GYnHk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس : می‌تونید دوباره به یه اقتصاد بدون تحریم دسترسی داشته باشید و به اقتصاد جهانی برگردید، اما فقط در صورتی که به تعهداتی که تو این توافق می‌دید پایبند باشید
🔴
پس این هم نقطه فشار ماست و هم‌زمان هم ابزار اجرای توافقیه که تو اختیار داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/128223" target="_blank">📅 17:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128222">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
رئیس کمیسیون اروپا: ایران قبل از لغو تحریم ها باید رفتار خود را تغییر دهد‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/128222" target="_blank">📅 17:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128221">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
جی. دی. ونس درباره ایران:
«تمام ائتلاف کشورهای حاشیهٔ خلیج فارس از توافق هسته‌ای اوباما با ایران متنفر بودند، چون احساس می‌کردند این توافق به ایران قدرت می‌دهد که نقش یک بازیگر بد را ایفا کند.
🔴
حالا ائتلاف خلیج فارس دربارهٔ توافق صلح ترامپ چه می‌گوید؟ آنها عاشق این توافق هستند، چون آن را فرصتی برای ساختن و آفریدن خاورمیانه‌ای جدید می‌بینند.
🔴
ترامپ می‌خواهد ایران کشوری موفق باشد اگر در مورد ورق زدن برگی جدید جدی باشد.
🔴
ما با همه طرف‌های درون رژیم ایران در حال تعامل هستیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/128221" target="_blank">📅 16:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128220">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpsCrFCVL1Zcif_vSeAkgA6Yddd-hUzA6K8qyMIqkgAFbHdb0C9J4JrqPoVnrTE15ec_79DmvAxj_oefjE9UC7wy4ZtNT0-t3suiGB_hgTQ-ZD1oj48IkcUR7obVPRfIIGYiIr7z_bYYAfjqpJVaGbJKwWiA681zWGMusS0hYYEgU64WfQdHoLENEU4qkiXjW0vaisvwROl02qOOBwadPSMIf3AQVNl3K8CPZgj_zD9z9EvaI1RPFv_befGvnsgo2hRe_Wmh90ZngM4K3dmYvjiXVrRnkLdDcMiIIVz6oobWDjIpO_pqDV9ALLtEXJPgM-YRBYS_to5hNUOKqKwDjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: کشتی‌ها شروع به حرکت کرده‌اند، بسیاری از آنها با نفت بارگیری شده‌اند، از تنگه هرمز خارج می‌شوند
🔴
آنها در امتداد «بزرگراه» جنوبی حرکت می‌کنند که کاملاً امن، مطمئن و بکر است. مناطق دیگری نیز برای سفر وجود دارد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/128220" target="_blank">📅 16:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128219">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ونس: مستقیم با رهبران ایران در ارتباطیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128219" target="_blank">📅 16:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128218">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ونس: برنامه هسته‌ای برچیده خواهد شد و تنها در آن زمان درباره اموال بلوکه شده مذاکره خواهیم کرد.
🔴
با آژانس و ایران درباره چگونگی نابودی اورانیوم غنی‌شده صحبت خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128218" target="_blank">📅 16:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128217">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
بعضیا یجور مردم‌ مردم میکنن انگار مردم اون ۳۰ الی ۴۰هزار نفری هستن که تو میدون‌ها هستن
🔴
مثلا تو تهران ۱۲میلیونی ۴۰هزار نفر عددی نی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/128217" target="_blank">📅 16:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128216">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H14NdMcmss7bZPe9uAhIYi18lLK3cAv6PRZguHGF3eUCpiESbgkjgDm5dh0Rw-IeGNcw4wSO7cX1xBqOTNd7TVaWbX1RjnCmjc1YVIhZnzd6-cwmEhRRBO5Nn2BmcPyadhqAdxE-ZpUXaxTBaBtPGTzVoX0Kui_kxaxTooVKMMAuOUHVRQdnyJgXdSuHg_GF4XULTQ_wz0kN4Pu0UCFDEBehLR8DsyECr8wXbWSPGPZBY42zSGTk7fV35ywwNqVtYIRm-PC211g6fZCvhSxdh0EHYjnF0OLTWYzdOu8BYJrk3Q7iKYqBxCAlkdCeZVglPdcJhlfY-i54nDbvGaxxMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات اسرائیل به لبنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/128216" target="_blank">📅 16:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128215">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e6aee63ae.mp4?token=uTLQzBoLPYKSmlDK-hXKWg9WhOer67Br3bgkbA1lTRjL6M_sUehqQB6ib3_bFRGu_-Pyf5F5kWUXXjJG0sLf2_KqESq_W17PQ1NYIM9FIGZceMpnCC7_wxriRhd0VR7uatVgZR1zYslZSZR-kdCmVO0d9VragtsyJOYHK6syuF7fP_L-OW8n2sdUr9IU1vJCu42lzSGk6kUkvliBW7IpuBnGGN9WOVBszirEJMrfSjtp4yjhe_HBev7JaKDYnyTv19GWDC_OnoVoPL2JssBeWrcuV4qSoI9FWev1dwG-l_NzuYVH8PIkfn9-Ibo73jvKygWQJCHz5zNQQf0vnR9X1mWCC8e_cExVyscmJ8KM46LKVVtWaLK3vZsgipTznC_ur1KMTlZMw9wYIwZIT0Cy0NPolCcJ8TM3wnuOB3dX9qwAUR5qLC98-e95Bavj0cYgWC7giL8LkXghFT9C6GCXNX3FPGnfU5ldwZx0WW_pP333LeCLRNUYxRshoQ8Q5mfeM3w4x8ZzN2f9OSf84qd4ddDkyBCUcD21_ldxHIjBdcM6JYO5nSIabAq3GHxsHmveZjzqswZSK9zgAQiayTPE3xxft15IAjn2B9QDO0S7V7jFfCVh0nGnaCW5nXMnLjLDPqv8aeR1wpU8rhQe27fB4G3Z1gRSG3rVx0WaxVkK9FI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e6aee63ae.mp4?token=uTLQzBoLPYKSmlDK-hXKWg9WhOer67Br3bgkbA1lTRjL6M_sUehqQB6ib3_bFRGu_-Pyf5F5kWUXXjJG0sLf2_KqESq_W17PQ1NYIM9FIGZceMpnCC7_wxriRhd0VR7uatVgZR1zYslZSZR-kdCmVO0d9VragtsyJOYHK6syuF7fP_L-OW8n2sdUr9IU1vJCu42lzSGk6kUkvliBW7IpuBnGGN9WOVBszirEJMrfSjtp4yjhe_HBev7JaKDYnyTv19GWDC_OnoVoPL2JssBeWrcuV4qSoI9FWev1dwG-l_NzuYVH8PIkfn9-Ibo73jvKygWQJCHz5zNQQf0vnR9X1mWCC8e_cExVyscmJ8KM46LKVVtWaLK3vZsgipTznC_ur1KMTlZMw9wYIwZIT0Cy0NPolCcJ8TM3wnuOB3dX9qwAUR5qLC98-e95Bavj0cYgWC7giL8LkXghFT9C6GCXNX3FPGnfU5ldwZx0WW_pP333LeCLRNUYxRshoQ8Q5mfeM3w4x8ZzN2f9OSf84qd4ddDkyBCUcD21_ldxHIjBdcM6JYO5nSIabAq3GHxsHmveZjzqswZSK9zgAQiayTPE3xxft15IAjn2B9QDO0S7V7jFfCVh0nGnaCW5nXMnLjLDPqv8aeR1wpU8rhQe27fB4G3Z1gRSG3rVx0WaxVkK9FI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دقایقی قبل در مینی تجمعات
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/128215" target="_blank">📅 16:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128214">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ونس: امیدواریم متن توافق با ایران این هفته منتشر شود/ خواهیم دید که آیا تهران حاضر به امتیازدهی است یا خیر
جی دی ونس، معاون رئیس جمهور آمریکا در مصاحبه با سی‌ان‌بی‌سی مدعی شد:
🔴
روند راستی‌آزمایی دو مرحله‌ای در مورد ایران وجود خواهد داشت
🔴
ما انتظار داریم تنگه هرمز برای مدت طولانی باز و بدون عوارض باقی بماند.
🔴
هنوز جزئیات زیادی در مورد این توافق وجود دارد که نیاز به توضیح دارد
🔴
فکر می‌کنم کسانی در اسرائیل هستند که این توافق را می‌پذیرند
🔴
ما انتظار داریم که رئیس مجلس، وزیر امور خارجه و دیگران، نمایندگانی از ایران را در مراسم امضای توافق‌نامه حضور داشته باشند.
🔴
تعهد بلندمدتی وجود دارد تا اطمینان حاصل شود که ایران هرگز سلاح هسته‌ای تولید یا به آن دست نمی‌یابد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128214" target="_blank">📅 16:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128213">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ ضربه آخرو بزن</div>
  <div class="tg-doc-extra">علیرضا طاهری</div>
</div>
<a href="https://t.me/alonews/128213" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128213" target="_blank">📅 16:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128212">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127a682588.mp4?token=oi2KhKjEpz2cHv9m5qM-76GVncxSLwP7Y7dCVe0P6sAbDbgxC3x0d2C0HNIBeXjDUmC411UHJgFrh4X36CoKS7SbSUzj_Kv8v_ruZKlodTRCKr6yCuA624mi_86x2vdWUm2tISn2mDWS3UluLqQ5rBD_AAEIuyKiSUpno0ONkoTfZeBlOjfvzjXiqgU9aEPw4MY8wzvDQN_9yPAdTwli-eZE4DL1VGpdjNIh4fXPgDXXDSBSS9BsUk3XKNoHC6GDYmQRqH8upf_zsiUBwG4MfREZ5oSFdh-1tlB_RE7xQhVhOXBgAhqsnWI4FkQPBEuHztGxxOdiHqBhwhL-Lwwtcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127a682588.mp4?token=oi2KhKjEpz2cHv9m5qM-76GVncxSLwP7Y7dCVe0P6sAbDbgxC3x0d2C0HNIBeXjDUmC411UHJgFrh4X36CoKS7SbSUzj_Kv8v_ruZKlodTRCKr6yCuA624mi_86x2vdWUm2tISn2mDWS3UluLqQ5rBD_AAEIuyKiSUpno0ONkoTfZeBlOjfvzjXiqgU9aEPw4MY8wzvDQN_9yPAdTwli-eZE4DL1VGpdjNIh4fXPgDXXDSBSS9BsUk3XKNoHC6GDYmQRqH8upf_zsiUBwG4MfREZ5oSFdh-1tlB_RE7xQhVhOXBgAhqsnWI4FkQPBEuHztGxxOdiHqBhwhL-Lwwtcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آخرین شاهکار عوستاد خوش چشم ۱۰ثانیه قبل از اعلام توافق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/128212" target="_blank">📅 16:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128211">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ونس: انتظار می‌رود طیف کاملی از نمایندگان ایران در مراسم امضای روز جمعه حضور داشته باشند
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128211" target="_blank">📅 16:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128210">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
ونس: انتظار می‌رود طیف کاملی از نمایندگان ایران در مراسم امضای روز جمعه حضور داشته باشند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/128210" target="_blank">📅 16:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128209">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: مباحث مربوط به اسقاطی‌های مرتبط با فروش نفت ایران، مشتقات نفتی و پتروشیمی که به محض امضای یادداشت تفاهم، که قرار است روز جمعه انجام شود، باید این اتفاق بیفتد و ایران بتواند بدون هیچ مانع و مشکلی، کار فروش نفت و محصولات پتروشیمی و مشتقات نفتی را انجام بدهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128209" target="_blank">📅 15:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128208">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
بقایی : به اسرائیل اصلاً اعتمادی نیست
🔴
همون‌طور که به آمریکا هم اعتماد نداریم تجربه هم نشون داده اینها در عمل به تعهداتشان هیچ‌وقت صداقت نداشتند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128208" target="_blank">📅 15:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128207">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
بقائی: مذاکرات هسته‌ای و رفع تحریم‌ها ظرف ۶۰ روز آغاز می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128207" target="_blank">📅 15:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128206">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/699a79d84c.mp4?token=eP8o3rxJwIklGVnRGbYcwJXce9joBumzsnZ4NgpjJPbK6BOb_H7A6zBZkzV-Rg5s-U2A5IjWxVN9XQM4HUHvtKNE8VpjblflcLHaRUIOR8641gKmEz_Q-KYmdqhZwT75k1VwpEGr4HqmpivDWYOZxwR7-Fotm4V-t_fURXfbqESNeNz06ACaWZ5vtNgO0CitnkhMjSCl8G2dxjrmnYRRH-wG-vYf-w8LwEzvfu7HObtzVtmvI_9SLDfS4EdNp-yEW7jrIZj1-UOAhtt11f3ho0yl8lDSP6eVru9AAYe7Lvomy3GtdoHCVJlWL9EnuM-rgJdbKa3W5PWrvLu-eyokPZoTjr1m74VImUITVGoi0NUyYN2RoALqxNFoJ9EhmDZ0N09hk3JGVhsD_euUZMYPccH_mhLdaXpHJBX9BoAzE9X8ZgujS0y8AbyIcZzDQfZdvv73JZquz_ypsShF6GwkbF_MFDzN98sCAKo5hFlZURjzvBTjYaVggG-1bCXWYkNEREoYpt3cY4t7DrwJD9ACYmtrPppKcukb_hIrFMa6SxXcny0CBkiwrSHRVsaBb4C4tMh8pp3jIw3AJ0sfpCjm_OsJMscz57RG8UEO3KJEBk2eFBuWYzXPtVLAFKed78jRZwEXv4DgAlO0eQVQesE4lcpZTeXynzXak0_4RksXcJc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/699a79d84c.mp4?token=eP8o3rxJwIklGVnRGbYcwJXce9joBumzsnZ4NgpjJPbK6BOb_H7A6zBZkzV-Rg5s-U2A5IjWxVN9XQM4HUHvtKNE8VpjblflcLHaRUIOR8641gKmEz_Q-KYmdqhZwT75k1VwpEGr4HqmpivDWYOZxwR7-Fotm4V-t_fURXfbqESNeNz06ACaWZ5vtNgO0CitnkhMjSCl8G2dxjrmnYRRH-wG-vYf-w8LwEzvfu7HObtzVtmvI_9SLDfS4EdNp-yEW7jrIZj1-UOAhtt11f3ho0yl8lDSP6eVru9AAYe7Lvomy3GtdoHCVJlWL9EnuM-rgJdbKa3W5PWrvLu-eyokPZoTjr1m74VImUITVGoi0NUyYN2RoALqxNFoJ9EhmDZ0N09hk3JGVhsD_euUZMYPccH_mhLdaXpHJBX9BoAzE9X8ZgujS0y8AbyIcZzDQfZdvv73JZquz_ypsShF6GwkbF_MFDzN98sCAKo5hFlZURjzvBTjYaVggG-1bCXWYkNEREoYpt3cY4t7DrwJD9ACYmtrPppKcukb_hIrFMa6SxXcny0CBkiwrSHRVsaBb4C4tMh8pp3jIw3AJ0sfpCjm_OsJMscz57RG8UEO3KJEBk2eFBuWYzXPtVLAFKed78jRZwEXv4DgAlO0eQVQesE4lcpZTeXynzXak0_4RksXcJc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقائی: ایران و عمان امنیت تردد در تنگه هرمز را تأمین می‌کنند
🔴
هزینه‌های خدمات ناوبری و بیمه کشتی‌ها طراحی و دریافت می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128206" target="_blank">📅 15:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128205">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db36eff319.mp4?token=ueZlOLzfG37CcdZyLOgEbaeQ1eVEx7dEebqVqMjm_uVAcENC26PQuaaRuMNa0IpCOtcqJCbfuHVw7mOeKXrVn11h04A_31j3RQ9Nh56CdIp2SXP6bqqIcGKJ_ObLeeqjTP-b8sLcGV5Ebpv-bjanpNfS7GYvru2eLM6L9II2wAQf2EgjEcHQupfnWce_LTFckkzcCu6EAudzZXNkiz_khxof9BdDy2tRQHPvD6SEs_dm9Eqj_fsMe0Q337HPbQzJAVPwdg5giXBiQmi09pWxaXksTzUinxKJRAws-lrOeDcDN-q-LFe5jTFHej7N2ON-_U11M2YUxzmR4PF89taqGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db36eff319.mp4?token=ueZlOLzfG37CcdZyLOgEbaeQ1eVEx7dEebqVqMjm_uVAcENC26PQuaaRuMNa0IpCOtcqJCbfuHVw7mOeKXrVn11h04A_31j3RQ9Nh56CdIp2SXP6bqqIcGKJ_ObLeeqjTP-b8sLcGV5Ebpv-bjanpNfS7GYvru2eLM6L9II2wAQf2EgjEcHQupfnWce_LTFckkzcCu6EAudzZXNkiz_khxof9BdDy2tRQHPvD6SEs_dm9Eqj_fsMe0Q337HPbQzJAVPwdg5giXBiQmi09pWxaXksTzUinxKJRAws-lrOeDcDN-q-LFe5jTFHej7N2ON-_U11M2YUxzmR4PF89taqGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقائی: یادداشت تفاهم ایران و آمریکا توافق برای خاتمه جنگ را نهایی کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128205" target="_blank">📅 15:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128204">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
سخنگوی‌ وزارت خارجه : دو تا موضوع اقتصادی مهم مطرحه؛ یکی آزاد شدن پول‌ها و دارایی‌های بلوکه‌شده ایران و یکی هم جبران خسارت‌ها
🔴
آمریکا قول داده برای هر دو مورد اقدام کنه
🔴
نکته مهم اینه که بحث بر سر پس گرفتن پول‌های خود ایران هست، نه اینکه آمریکا بخواد پول جدیدی به ایران بده
🔴
بقایی : قراره درباره برداشته شدن همه تحریم‌ها؛ چه تحریم‌های آمریکا (اولیه و ثانویه) و چه تحریم‌های شورای امنیت و حتی قطعنامه‌ها و محدودیت‌های آژانس صحبت بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128204" target="_blank">📅 15:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128203">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
مکرون، رئیس‌جمهور فرانسه: مهم است که برنامه موشک‌های بالستیک ایران در مذاکرات آینده مورد بحث قرار گیرد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/128203" target="_blank">📅 15:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128202">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb5948c916.mp4?token=nn2tludkynzAhqWU004t6jt7rrYtwqqBxQC5dTy6obT30d_Ud9S5u8YILU6fWqPUP3or84mXfi1O7m_rA-En-wGiXM2_DvfyTQ-NQQtmPYH7rmcpFYQfU0hDz6H_8pOTo7L4RVAR_cc0TvBrM7u4BjSddKcKo_6zJZRhdenfdfRgooPYv85rhtH6OjDHqvqdlnEUHM-GBHlczeuzq-i0Ntob3FF8p9iEM8qwlqIDxztcbdiTDjpzk8_TOioIY9KiLwwwkxcWW1WudVDOQmn06tdF0XPgtLWpSmWxdKWWNeBlyDKC-E2n22Tr5jYVD-37Q7YXNdPQWdERJUcy3D6N7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb5948c916.mp4?token=nn2tludkynzAhqWU004t6jt7rrYtwqqBxQC5dTy6obT30d_Ud9S5u8YILU6fWqPUP3or84mXfi1O7m_rA-En-wGiXM2_DvfyTQ-NQQtmPYH7rmcpFYQfU0hDz6H_8pOTo7L4RVAR_cc0TvBrM7u4BjSddKcKo_6zJZRhdenfdfRgooPYv85rhtH6OjDHqvqdlnEUHM-GBHlczeuzq-i0Ntob3FF8p9iEM8qwlqIDxztcbdiTDjpzk8_TOioIY9KiLwwwkxcWW1WudVDOQmn06tdF0XPgtLWpSmWxdKWWNeBlyDKC-E2n22Tr5jYVD-37Q7YXNdPQWdERJUcy3D6N7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقائی: جزئیات ابعاد دیپلماتیک توافق به‌زودی رسانه‌ای خواهد شد
🔴
در خصوص نحوه و سازوکار امضای یادداشت تفاهم، تصمیم‌گیری نهایی ظرف امروز و فردا صورت می‌گیرد و نتایج آن به‌صورت رسمی اعلام می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/128202" target="_blank">📅 15:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128201">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f31afa1dfe.mp4?token=DdNl6-lMQ2ymEMNJM5UdaAc85BpyvxghpMaNNDAdHFDiCHMf6mgN7WmQrGlJsjINVvcgB4uc4Ucd-LXbGeIfEc2kiZkwgkgAxBN-As0A7OpxpXOIVyhQcKzZyW_qNHZ52tZi0QvQPRCJaJr-lRADIRZrhHlxiCrN_qgvp9Epeit3OoDyBQr04mrRLFGtUGXJ3ZQSUi503dGo5wjJ3bWL7N3F0TBoZXxdVQ0Na06wXsKS-11nVTqpFJzCnK1_jf93chhpzDU_I57iRDToA81valdrQIRVKZdXrA0fiPaLiicXKpo0MoxXCfdn4fMP2j0CWuNDqMm2jP5_irhXrniAVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f31afa1dfe.mp4?token=DdNl6-lMQ2ymEMNJM5UdaAc85BpyvxghpMaNNDAdHFDiCHMf6mgN7WmQrGlJsjINVvcgB4uc4Ucd-LXbGeIfEc2kiZkwgkgAxBN-As0A7OpxpXOIVyhQcKzZyW_qNHZ52tZi0QvQPRCJaJr-lRADIRZrhHlxiCrN_qgvp9Epeit3OoDyBQr04mrRLFGtUGXJ3ZQSUi503dGo5wjJ3bWL7N3F0TBoZXxdVQ0Na06wXsKS-11nVTqpFJzCnK1_jf93chhpzDU_I57iRDToA81valdrQIRVKZdXrA0fiPaLiicXKpo0MoxXCfdn4fMP2j0CWuNDqMm2jP5_irhXrniAVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: لبنان و خاتمۀ جنگ در لبنان بخش لاینفک تفاهم خاتمۀ جنگ است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/128201" target="_blank">📅 15:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128200">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e979bbc34.mp4?token=ivfdwtF7KAaXsobva8y13213jDfdg7BmavhQxG2sEfEcplCBvgcm2kGVBMoCBhcgkgOMfCf7CTd8TfpP8IdtXls43PdbmKKAJ4JPivJYvz7-3Lg10Tz4zaDiyHabXAodRFueieojH9C0ImUys9PBA479cly_YoL59l8U1wux-eZcgJgEUiaWBvEEto-Rbb4acPKqcL_93Y5CYL2MDSlcJBwUrGWd1NdTxjt4vmT4P_29qD6B47RptuBsc6QWAFGMlygrBhGpHp2CbfUwbLIF9_Y-o2_u1xdNxAC5h4bzrPLlTygMfA95rENMrKu70_SoJprv9PDpr_BEHRm9-DXwdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e979bbc34.mp4?token=ivfdwtF7KAaXsobva8y13213jDfdg7BmavhQxG2sEfEcplCBvgcm2kGVBMoCBhcgkgOMfCf7CTd8TfpP8IdtXls43PdbmKKAJ4JPivJYvz7-3Lg10Tz4zaDiyHabXAodRFueieojH9C0ImUys9PBA479cly_YoL59l8U1wux-eZcgJgEUiaWBvEEto-Rbb4acPKqcL_93Y5CYL2MDSlcJBwUrGWd1NdTxjt4vmT4P_29qD6B47RptuBsc6QWAFGMlygrBhGpHp2CbfUwbLIF9_Y-o2_u1xdNxAC5h4bzrPLlTygMfA95rENMrKu70_SoJprv9PDpr_BEHRm9-DXwdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عوستاد
خوش‌چشم: تحت هیچ شرایطی مردم خیابان را ترک نکنند/ترامپ برای ایران برنامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128200" target="_blank">📅 15:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128199">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14602c7b1f.mp4?token=DGZ1-dmL2WZ-6unpJNdT4-EpApZyEkIlFpyqtAc3hyu9ZeVGtaaas106DTn0gXHu9rTO_JbGb4OA_xXMuL0BV4V3g_IHhz-5tsG8picALaotwEEMqtQGTdvIlHlq2E9ZvdiS_Ic8YGviyC9AVKsazR_SafVH-B2CqKpHUKUPEJq3o463TAjNqVPySkkXJ4g3Oc2vzNV0IbbZEfqk7GcZY-mWthvaUd9UUbnfCqcS6pAWBBv5NgSFJLKeXKAx-4CwEJxu8BvqqALuWdn8soYRqbvY6TxTAr54tJwMjkx6cz143c9poGIYGJ6itH2GR5QsqaZnMfe5pvhUKZ93pz8fQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14602c7b1f.mp4?token=DGZ1-dmL2WZ-6unpJNdT4-EpApZyEkIlFpyqtAc3hyu9ZeVGtaaas106DTn0gXHu9rTO_JbGb4OA_xXMuL0BV4V3g_IHhz-5tsG8picALaotwEEMqtQGTdvIlHlq2E9ZvdiS_Ic8YGviyC9AVKsazR_SafVH-B2CqKpHUKUPEJq3o463TAjNqVPySkkXJ4g3Oc2vzNV0IbbZEfqk7GcZY-mWthvaUd9UUbnfCqcS6pAWBBv5NgSFJLKeXKAx-4CwEJxu8BvqqALuWdn8soYRqbvY6TxTAr54tJwMjkx6cz143c9poGIYGJ6itH2GR5QsqaZnMfe5pvhUKZ93pz8fQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی از تمرینات نیروی هوابرد ارتش آمریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/128199" target="_blank">📅 15:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128198">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سازمان هدفمندسازی یارانه ها: یارانه نقدی مرحله ۱۸۴ خرداد‌ماه به حساب سرپرستان دهک‌های اول تا سوم واریز شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/128198" target="_blank">📅 15:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128197">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWxjLkUCL3VD734uS5wDx4kYvAu7Cn4XGCLVuvTwGvBNDW2jD-sezCASOw_CBuSj2KSmbKWz8bDSH6cra2msLAwTJ4-smeadXKNcywHiMJ_kC6yha8NSLMFLMb6MP4-74-DI8UAUiSEgyan4JUXIZkNNlz7cqrRoK8vwZ-CJD2MW5phh8E93GEGlo7cVhG7d5-EEiFEUKX5-Pox1LdxFSUIRhe5rpuFjyq5_LrqENzCKE6UhfTlD4oU-AuVci8s11VpQHZY48QnCFawds1gtdYAqXrVOWvJyClO_H8C7_Zu4UcaMifGQNstuyrQ198dSazw0_JblEBvCtCwcO1jk4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت صفحه اسرائیل به فارسی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/128197" target="_blank">📅 14:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128196">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
صدا و سیما: تنگه هرمز تا اطلاع ثانوی بسته است و بیش از ۹۶ ساعت است نیروی دریایی سپاه اجازه عبور هیچ شناوری را نداده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/128196" target="_blank">📅 14:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128195">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jG8H9XRdKIxAkr-pfgKZ8loZRlqhl4Orw-SofAtgliTyM4kxzY19wsHivWBHnC4-Xxym7SWYlM0CQRKG3_IaQW4fFGVaahBiYV0s4ukaEN6Ve4BB-FVL8fs6j1DA73Lb9u-EDFq_OGJesQECnb4C50WR0rzlgzGliF6H9jzSt-xuquGf4R65x_kPhQ7rRw-vMuIqn2uLVW4jaIdcobWgmpp_CHr6s-GsV_A1MyAb4coXaLDeLVlc-6JQxnD-5YkmG2uPxVlBRocicbOZHinTmDxoRlLrjmZQeaeOpHIjj--J6gbIPD6Hx5gkdBZFE2kMjsHBjXyL9qNrlUfUo0G8QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش مارک دوبوویتز، مدیر بنیاد دفاع از دموکراسی (FDD) به توافق: بازارهای انرژی را دوباره آرام و ذخایر را پر کنید.
🔴
به ارتش آمریکا استراحت دهید و آن را دوباره مسلح کنید.
🔴
طرحی برای حمایت از ایرانیان مخالف برای فلج کردن حکومت تدوین کنید.
🔴
تحریم‌ها را با فشار بی‌وقفه اجرا کنید.
🔴
پای میز مذاکره بازی نخورید.
🔴
اراده تهران را زود آزمایش کنید.
🔴
امتیاز کم بدهید.
🔴
نتیجه بخواهید.
🔴
سریع (از میز مذاکره) کنار بروید.
🔴
محکم‌تر ضربه بزنید و حمله کنید.
🔴
محاصره دریایی ایران از طرح‌های قدیمی پیشنهادی بنیاد دفاع از دموکراسی (FDD) بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/128195" target="_blank">📅 14:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128194">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
خبرگزاری سعودی: وزیر خارجه عربستان سعودی تماس تلفنی‌ای از همتای ایرانی خود دریافت کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/128194" target="_blank">📅 14:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128193">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
بنی گانتز، رهبر اپوزیسیون اسرائیل هشدار می‌دهد که اسرائیل نباید با محدودیت‌هایی در آزادی عمل خود در لبنان یا هرگونه عقب‌نشینی که ساکنان شمال را به خطر می‌اندازد، موافقت کند.
🔴
توافق در حال ظهور با ایران به نظر می‌رسد یک شکست استراتژیک باشد که اسرائیل را ملزم به درگیری در یک مبارزه سیاسی، نظامی و حقوقی در سال‌های آینده می‌کند، مبارزه‌ای که تنها می‌تواند توسط یک دولت وسیع صهیونیستی رهبری شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/128193" target="_blank">📅 14:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128192">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
سازمان ملل: توافق امریکا و ایران مارو خیلی دلگرم کرد و فعلا نگران نیستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/128192" target="_blank">📅 14:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128191">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0848ff20aa.mp4?token=XGN9iPhoMl3tkCASpBGTXh9Cc7-Rb5pZ2zw8CLuM_x-LPRMJzWrJp1wKbY823xe1qYSvYnHTSB90kdKEKn4jnAFKOip22ZJgBpcMQhYBpInW884nqTQYV9qao7Q2XFBRLtjI3RxLVBPttdEuu5pJUYMn_7yyEAsjnwDVmD8rzhgBxvT9l89LbQSAhibeOERagPf_-w5uKy61L82JfreI4ZEQlzecR2rPK2i_3sURXXnlNFvTI-SAsyw7c3PkqgX_GipcW6o92svQiDQ3nu0rmhXy5080OPDYIPRyuF3uuUc2AR7WaCrJyKaBcvbsyaGFouU3MiET1PEt0Deh7N8GckkY_qJLYJSQfIrixK_fKNVZoJE4SzOYVIpLmUihPt-UbKkyZSlHxDZmU5jOEDo3O4jUX0Ce_YxQqzYsdDSax7tgOpF8W0I4eZkMP8O8qoBx6ZlwWvD-1JInnCSs6-weDx6aFrFcTP5CQTJOM7wHj8H8nuFG49dbrareq5hhhnplMkswdPnC7TV9Dxyc26Vuui-u700zrmG6o1tLlLQszLennv0zE0J8Af5QRIJaw5mtwmzWXqkVwcgaPzPKEbLCLorwacb2ht0E1gg2G98QtgjgfExfHeA1vti9mUFtY2PTnkAMPAlUoRQAQBwkdmQR_9htK-y3ov4J1bJaH-J_YsU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0848ff20aa.mp4?token=XGN9iPhoMl3tkCASpBGTXh9Cc7-Rb5pZ2zw8CLuM_x-LPRMJzWrJp1wKbY823xe1qYSvYnHTSB90kdKEKn4jnAFKOip22ZJgBpcMQhYBpInW884nqTQYV9qao7Q2XFBRLtjI3RxLVBPttdEuu5pJUYMn_7yyEAsjnwDVmD8rzhgBxvT9l89LbQSAhibeOERagPf_-w5uKy61L82JfreI4ZEQlzecR2rPK2i_3sURXXnlNFvTI-SAsyw7c3PkqgX_GipcW6o92svQiDQ3nu0rmhXy5080OPDYIPRyuF3uuUc2AR7WaCrJyKaBcvbsyaGFouU3MiET1PEt0Deh7N8GckkY_qJLYJSQfIrixK_fKNVZoJE4SzOYVIpLmUihPt-UbKkyZSlHxDZmU5jOEDo3O4jUX0Ce_YxQqzYsdDSax7tgOpF8W0I4eZkMP8O8qoBx6ZlwWvD-1JInnCSs6-weDx6aFrFcTP5CQTJOM7wHj8H8nuFG49dbrareq5hhhnplMkswdPnC7TV9Dxyc26Vuui-u700zrmG6o1tLlLQszLennv0zE0J8Af5QRIJaw5mtwmzWXqkVwcgaPzPKEbLCLorwacb2ht0E1gg2G98QtgjgfExfHeA1vti9mUFtY2PTnkAMPAlUoRQAQBwkdmQR_9htK-y3ov4J1bJaH-J_YsU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه غرق شدن سه نوجوان آملی، دیروز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/128191" target="_blank">📅 14:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128190">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SameagVIzSQSmojpE4z_o0X578hpBceUa4f2fnnDyeb8Ha2NcNp8SWnVOMWRVbmENoeO0AdcrBfXOWPXyzKp912wdX3RPiMQmxd6QvQdPGJgaJgcI7eq2MgREjdshYMN5qtZSJpjEJWw0zNtFTAA1OPGvzLgeEON3x8u6kWBRXs866x5oeQ-kWkIfA3QO6chZ0LYOCpwwjGDCMlqkbRWe8siZFYPg3t3hCnzc_y7JSP7hspqV9790BO4p-HgDCxa-L3qCclbk7p_CwpR6B-rYncXPw2Mb4IDVswqe3h8PBqrctjAWR2fi9nxGb1xFyXSog7_y8RgoedafdN0gIT5Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش جواد ظریف به توافق ایران و آمریکا
🔴
هوشمندی رهبری و ایثار رییس جمهور، رییس و اعضای هیأت مذاکره‌کننده برای تثبیت پیروزی تاریخی مردم و سربازان وطن، شایسته پشتیبانی ملی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/128190" target="_blank">📅 14:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128189">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
سودهای اولیه در بورس تل‌آویو به زیان تبدیل شده‌اند، به طوری که شاخص‌های اصلی حدود ۱.۵٪ در خلاف روند جهانی سقوط کرده‌اند، گزارش کانال ۱۲ اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/128189" target="_blank">📅 14:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128188">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
خبرگزاری فرانسه: جلسات مقدماتی پیش از امضای توافق‌نامه ایران-آمریکا در دوحه برگزار می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/128188" target="_blank">📅 14:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128187">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
توکیو آماده پیوستن به بیانیه اروپا درباره کاهش تحریم‌های ایران هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/128187" target="_blank">📅 13:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128186">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
والانیوز عبری: تاکنون هیچ درخواستی از جانب امریکا برای خروج اسرائیل از لبنان وجود ندارد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/128186" target="_blank">📅 13:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128185">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
خوش‌چشم تحلیلگر صداوسیما: من تعهد می‌دم ترامپ به شهباز شریف گفته حرف من دیگه خریدار نداره، بیا توییت بزن بگو توافق نهایی شده!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/128185" target="_blank">📅 13:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128184">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
خبرگزاری واس: وزیر خارجه عربستان سعودی تماس تلفنی‌ای از همتای ایرانی خود دریافت کرد.
🔴
فیصل بن فرحان در گفت‌وگو با عباس عراقچی،  از توافق برای پایان دادن به عملیات نظامی ابراز خرسندی کرد.
🔴
فیصل بن فرحان همچنین از آغاز مذاکرات تفصیلی با هدف دستیابی به یک توافق دائمی استقبال کرد.
🔴
وزیر امور خارجه عربستان سعودی ابراز امیدواری کرد که صلحی محقق شود که امنیت منطقه و جهان را تقویت کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/128184" target="_blank">📅 13:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128183">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e8f740c4d.mp4?token=kGY9pjDmdb9XYK8slo8kFINjzKtuejtouf2_QgVdYKpDhhBwQYgWJod8zfhP7kubOju4HpyUjhfxNzxKcXscOqXAtu-vvFro1OylL8gRuoEupaPgpEJE6iT4Obq-Lr4d8dZd98Yo-9TrqDkUeHDWFK6p4taPrSky2nsgH_Ju8gxwRcQZVMTu2QxOKpJFCaAS2uwTH2u0cIeQheqaMNIB1MM1JmF6M6zXWfp2fX5lb2hXgobPBezw_DN2GezmM2JJNvy8V4o0b3owpVNQIwQgHZJW306c-R7bR5mujQgX7UamaiyOBInUzMahCloIpBm3kwPq7mCwfI9_6rkfdJtBsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e8f740c4d.mp4?token=kGY9pjDmdb9XYK8slo8kFINjzKtuejtouf2_QgVdYKpDhhBwQYgWJod8zfhP7kubOju4HpyUjhfxNzxKcXscOqXAtu-vvFro1OylL8gRuoEupaPgpEJE6iT4Obq-Lr4d8dZd98Yo-9TrqDkUeHDWFK6p4taPrSky2nsgH_Ju8gxwRcQZVMTu2QxOKpJFCaAS2uwTH2u0cIeQheqaMNIB1MM1JmF6M6zXWfp2fX5lb2hXgobPBezw_DN2GezmM2JJNvy8V4o0b3owpVNQIwQgHZJW306c-R7bR5mujQgX7UamaiyOBInUzMahCloIpBm3kwPq7mCwfI9_6rkfdJtBsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ برای شرکت تو اجلاس گروه ۷ به فرانسه پرواز کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/128183" target="_blank">📅 13:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128182">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
شورای عالی مناطق ازاد تجاری اعلام کرده که صدور مجوز نصب پلاک ملی روی خودروهای لوکس مناطق آزاد درحال انجامه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/128182" target="_blank">📅 13:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128181">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0Mf6LOr6kIH-jjl7IOKGkSSmiGEmHIJxCpl-teZapbV5BcgNhYT419cv-9SF4zaV2VB67ttzFNU4TlcClesk52cf4rMAQ7xgF5IQJ-lPli9VGgfyqd7vF4nrnrTkZWLtiKGRzHhmIl4mhSIe_evR-onyddXtd9-T0PBDVSPFmgBTvWvRmtte4NdkUjt3KXsVu0VpGdUcxDV7cmrz6x5P-T64XR-KaL8KIsRtGqj12heTmyfHoow_c_0heL8Ka0JIiYBbV7L0NnwokvmytMqmcqE7-vdhr9rEn5u_8v438OGQwYkfI-vtFWLI1rfS1jCxyuFXFY6V50uj_LXF3LvJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
داده‌های هواشناسی جهانی نشان می‌دهد زابل در ۲۴ ساعت منتهی به صبح ۲۵ خرداد با ثبت دمای ۴۷.۶ درجه، گرم‌ترین نقطه جهان بوده است.
🔴
شهرهای الاحساء عربستان با ۴۷.۴ و سبی پاکستان و ینبع عربستان با ۴۷ درجه در رتبه‌های بعدی قرار گرفتند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/128181" target="_blank">📅 13:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128180">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPWABIFlbUTYmbuvfGiq4PfObd8wbg82VORcJdzddZQ6EUW49ZN6mrH4IfCh_tIso3JfujvohqJ5JCIq3cOwpPl7Gc8xROKZaPX-wLNVUh_VxkUHW-_doUY2EwF4jeG0rA7ZDQ0sJ9KHak6PMGOE0S8VAoEK18Aaq9Xd1cdWYS_L0UsNJe0h4PECwEwbIMtWB4oFvKZCPvYuLFHxtjcTbKoWaxIteOV4bnDas-E_x2JaPq1AOaK4j5ziVCmYl-XSWPRWZTq242-AJ0bUJNzog93sE-upA1WAsnlHGbO-JI8DYoei4zpg__GkftAJfXyQvV4ruRZjCIdhQhKU7SGzsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شرط بندی روی پیروزی گادی آیزنکوت و شکست بنیامین نتانیاهو، در انتخابات اسرائیل افزایش یافته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/128180" target="_blank">📅 13:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128179">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
یورونیوز : توافق کنونی راه را برای مذاکرات ۶۰ روزه درباره مسائل هسته‌ای هموار می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/128179" target="_blank">📅 13:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128178">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
رویترز این توافق را بزرگ‌ترین پیشرفت دیپلماتیک از زمان آغاز جنگ توصیف کرد و نوشت: توافق ایران و آمریکا به کاهش قیمت نفت و امیدواری بازارهای جهانی منجر شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/128178" target="_blank">📅 13:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128177">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
رئیس‌جمهور لبنان، عون : از اینکه امنیت و ثبات لبنان تو توافق آمریکا و ایران برای پایان دادن به جنگ لحاظ شده، قدردانی می‌کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/128177" target="_blank">📅 13:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128176">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640febd296.mp4?token=LXna58be0QgVPZa0d4HQ9P7w2E9lETXF2s8Vromi7aUfb6nZaqhThmBIduRBcmTyvmuzpOAePo-aUqqs4x4eEqQuS2AMBkJIOvjXNqnPKrfWBTBWjQFX7DhtIx4bMtkxLGPRHdzowUvnkLgPctJOhvHe6zogU1hSPYwz-AjSR9U26_8_DulwrCWtqSafBpxnZ59_0Cql5GBDio79cIbbIKQDJD-hkj0DToIgAA9-joglHwQ5rzMyjhGnIsQQNDs21E7T13mnhEIEqKOEnMKyspS_zBnpSA6KddQOAZEXqHH-99HeF5ozTDZgDYYosU4zz_KPA1E1ulPsD-r1B1d4NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640febd296.mp4?token=LXna58be0QgVPZa0d4HQ9P7w2E9lETXF2s8Vromi7aUfb6nZaqhThmBIduRBcmTyvmuzpOAePo-aUqqs4x4eEqQuS2AMBkJIOvjXNqnPKrfWBTBWjQFX7DhtIx4bMtkxLGPRHdzowUvnkLgPctJOhvHe6zogU1hSPYwz-AjSR9U26_8_DulwrCWtqSafBpxnZ59_0Cql5GBDio79cIbbIKQDJD-hkj0DToIgAA9-joglHwQ5rzMyjhGnIsQQNDs21E7T13mnhEIEqKOEnMKyspS_zBnpSA6KddQOAZEXqHH-99HeF5ozTDZgDYYosU4zz_KPA1E1ulPsD-r1B1d4NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات اسرائیل تو مناطقی از جنوب لبنان ادامه داره!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/128176" target="_blank">📅 13:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128175">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RejY1VapEEiM9WW3JQEyPBlyt__mFJO71r84u1j1JmuUX-i6GxhrvbMA32sBbGCWLH2WYsMaA6XmCDizYC9CzzMqgj_WBkgqdWXMf2mEEUOd_ax4GKEwHA2yN46mMQB-4NZOCpn7_YlqhUIMRUhJnuPhD8nnE-GrcNx4qAd80DLXe4LNmbrtIhLuYJ0oboTK1kgo08ihugTpftB0MCw1sOeNeO3EJ3PL1EOrRErYIcZmXIt7okWmOw5kGb4LiHUIN_P97ufkHqN0bOy-MtyqEg5TKZi5Hwit7Gom_wjYja79Jx5CUSl3Il0djlM03a8MHyixHpT9Nlf_Em-mlHn-tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت هر بشکه نفت خام برنت بعد از توافق بین ایران و آمریکا :
۸۳
دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/128175" target="_blank">📅 12:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128174">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Y8t8xLkVvxIt-3SOeDJTOBWDeJ0Q2jlXyt23Dvmvg3tYFol3vSDwkqaHgKnY5_DXQR16t9oEHZTK89XDNtcbrU9vJD_lLpbTgpbsHzH3J1P68rXZFsY-wkMa4ah4d6fdV7A_fiU8fY_rc8mzZJ1ytq716aJBUofJTQwwDw_igwmaDZhGvir3OB2UD7jpoGUUb8SklNfyXNKE_R8b-28SoAlrlKo-SMTAMW1flMtjjXuAvi-dB5k0DQ8rN7pAugt-8PEZieHzdbx2hrqhfcT-j-pqBiAuzsI2axupW5Sr0bOFSPSmrQrMjapNADP_3nn6dCmOKvQuGaHvCB9t5QKsmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آتش توپخانه اسرائیل تپه علی الطاهر در منطقه نبطیه، جنوب لبنان را هدف قرار می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/128174" target="_blank">📅 12:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128173">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
وزارت خارجه امارات: ما بر اهمیت اولویت دادن به گفت‌وگو و دیپلماسی و پایبندی به قوانین بین‌المللی تأکید می‌کنیم، به‌گونه‌ای که امنیت و ثبات در منطقه تقویت شود.
🔴
ما بر اهمیت پایبندی کامل به مفاد توافق تأکید می‌کنیم، به‌گونه‌ای که توقف فوری و کامل اقدامات تجاوزکارانه در منطقه تضمین شود.
🔴
ما از مشارکت کشورها و طرف‌های ذی‌ربط در فراهم‌سازی شرایط مناسب برای دستیابی به این توافق قدردانی می‌کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/128173" target="_blank">📅 12:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128172">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
نفتالی بنت، نخست وزیر پیشین اسرائیل درباره توافق با ایران:  «این یک نقطه عطف خطرناک برای امنیت اسرائیل است. نتانیاهو ما را به جنگ‌های فرسایشی کشانده است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/128172" target="_blank">📅 12:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128171">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
در جریان معاملات امروز شاخص کل بورس با جهش ۱۶۱ هزار و ۵۹۸ واحد در سطح ۴ میلیون و ۹۸۰ هزار واحدی ایستاد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/128171" target="_blank">📅 12:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128170">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
اسموتریچ، وزیر دارایی اسرائیل:
توافق با ایران برای اسرائیل بد است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/128170" target="_blank">📅 12:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128169">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
مقامات اسرائیلی خواسته نشده‌اند که از جنوب لبنان عقب‌نشینی کنند، گزارش کانال ۱۲
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/128169" target="_blank">📅 12:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128168">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyPkPW_GFwz0SYXDErLlqYh433L_m8Fg75CxA3bbfm0Y2A4frczLFtbqHJZPRYw3f3zo3-Msz25EKT_Ejj6Redwvc-MdRxZX3LHN6IJZmuZ5Q6HG9fw1JOdrFAj-dSxqiUebz3fKA_cKFLRJ1YQVZ7fqi7xXscwMTCIKWeUgzJnoq65tlS57N8B0SpgOWLfPLmUHx1V5kkQHVpHuR4ljLAxBi9lNUCYfnYSl8GUA-CgZHJKuLeTyGECydyTexYdQcdbolG1NHyhCFvKHxzvInak5tF7OrMwg-FpKtlYoVPJc5oRvR4U3FMQscFH1f58dgNCFlagxc3GCNjkVUSLRSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش UKMTO از حادثه‌ای در ۱۴ مایل دریایی جنوب ساحل یمن ارائه داد.
🔴
یک کشتی کانتینری توسط یک قایق کوچک که خدمه‌اش آتش گشودند و تلاش کردند به کشتی سوار شوند، مورد حمله قرار گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/128168" target="_blank">📅 12:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128167">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8545eb45f.mp4?token=MTk6igoFw5ruAqf0I2N7T3mmOkJyI_W99cKCqERelpccAU2Q5JoRcSXN_oA46NqS0XdhdEJWhjB2EYxddvp05SDPHildAqAzM5fbAWttt6vl2yURYCLObigIbu602cim9-V1B6ggCkVHDPp-6nzEk7TWPzecmXBqjmnJdwmNIrDktf3L7MSPPDRccoimqvy8p8-ZsjOP-ZN58RiiBI165F0nNjE2EgErWfPqcbQNgroHLPUnTxzpTbPqtzLRh76MhMv5yV7EkbSuONhXbmvQlYk_-eYrj4CzWFfUoiaYuG9aOItN1eqKv6toEEZZRXjBwrtS_VV0WwGE_Fvo39cHjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8545eb45f.mp4?token=MTk6igoFw5ruAqf0I2N7T3mmOkJyI_W99cKCqERelpccAU2Q5JoRcSXN_oA46NqS0XdhdEJWhjB2EYxddvp05SDPHildAqAzM5fbAWttt6vl2yURYCLObigIbu602cim9-V1B6ggCkVHDPp-6nzEk7TWPzecmXBqjmnJdwmNIrDktf3L7MSPPDRccoimqvy8p8-ZsjOP-ZN58RiiBI165F0nNjE2EgErWfPqcbQNgroHLPUnTxzpTbPqtzLRh76MhMv5yV7EkbSuONhXbmvQlYk_-eYrj4CzWFfUoiaYuG9aOItN1eqKv6toEEZZRXjBwrtS_VV0WwGE_Fvo39cHjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برگشت مردمِ به لُبنان بعد آتش‌بس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/128167" target="_blank">📅 12:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128166">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
گزارش ها از حمله به یک کشتی در نزدیکی یمن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/128166" target="_blank">📅 12:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128165">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from112222</strong></div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/128165" target="_blank">📅 12:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128164">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVarzesh+plus | جام جهانی با ورزش پلاس(K_B9)</strong></div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/128164" target="_blank">📅 12:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128163">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
پزشکیان: زیر بار زور نمیریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/128163" target="_blank">📅 12:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128162">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل، کاتز : قرار نیست از لُبنان عقب‌نشینی کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/128162" target="_blank">📅 12:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128161">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
العربیه به نقل از منابع آگاه: آمریکا بر اساس این توافق متعهد می‌شود عملیات نظامی را در تمامی جبهه‌ها متوقف کند.
🔴
تعهد آمریکا به توقف عملیات نظامی شامل جبهه لبنان نیز می‌شود.
🔴
آمریکا بر اساس این توافق متعهد به رفع محاصره ایران است.
🔴
توافق بر رفع تدریجی تحریم‌های آمریکا و سازمان ملل علیه ایران انجام شده است.
🔴
ایران بر اساس این توافق متعهد می‌شود تنگه هرمز را ظرف ۳۰ روز باز کند.
🔴
ایران بر اساس این توافق متعهد می‌شود از تولید یا دستیابی به سلاح‌های هسته‌ای خودداری کند.
🔴
مذاکرات [اتمی] طی ۶۰ روز انجام خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/128161" target="_blank">📅 11:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128160">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d904eacc8.mp4?token=VyIDvtEY54_bg4pCOBi_092nbP9NXgmVvmg1e3r2XmW319cU5Tck-0IakdANVUBR4NtVHtawCuFSxvXfODgArKh2etzTe-hPzvtw_0OSfvarEXTpkzLfD263_O_M7gGjMIsJPsFuMZH0cfCYdK_imgWW3FQRUAWpp2vVMnt-lQdaAY7CdRrVVkPryLaoTFoN9F6mbDsSE6eLymArnzgq7FyImOucQiap6QcWjHCSB968KZQTe7HHpp2H17NRFB3GiquBieTisEfFPftaI4CmOsBZM0O5ciFbNAwR3Jh-9IagWTcP5YCMttxw5MU4Wx0tNB1MheL8eis-zRaK-c6djg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d904eacc8.mp4?token=VyIDvtEY54_bg4pCOBi_092nbP9NXgmVvmg1e3r2XmW319cU5Tck-0IakdANVUBR4NtVHtawCuFSxvXfODgArKh2etzTe-hPzvtw_0OSfvarEXTpkzLfD263_O_M7gGjMIsJPsFuMZH0cfCYdK_imgWW3FQRUAWpp2vVMnt-lQdaAY7CdRrVVkPryLaoTFoN9F6mbDsSE6eLymArnzgq7FyImOucQiap6QcWjHCSB968KZQTe7HHpp2H17NRFB3GiquBieTisEfFPftaI4CmOsBZM0O5ciFbNAwR3Jh-9IagWTcP5YCMttxw5MU4Wx0tNB1MheL8eis-zRaK-c6djg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آخرشم هچی که هچی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/128160" target="_blank">📅 11:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128159">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
الجزیره: شهباز شریف شخصاً در مراسم امضای توافق شرکت خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/128159" target="_blank">📅 11:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128158">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
یه سریا باید از امشب شام درست کنن دیگه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/128158" target="_blank">📅 11:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128157">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">میدان با تو خیابان با ما</div>
  <div class="tg-doc-extra">کربلایی حسین طاهری</div>
</div>
<a href="https://t.me/alonews/128157" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">😐
😐
😐
😐
🖋
🖋
🖋
🖋
🖋
🔖
🔖</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/128157" target="_blank">📅 11:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128156">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
قیمت دلار 163,500
🔴
طلای ۱۸ عیار 17,000,000
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/128156" target="_blank">📅 11:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128155">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3880986582.mp4?token=AJSmrC00n2egliaTC6rUtmDJiKOXx7_Ce3Lgpq4seI0gacnvUzkoIUO3FFBKj01BGKmayjHSsDTmIhixpSZ3Xp9x4t5haIhp7EXT4cD8KGBMWn0gBC7Eau9y8MlQhFLtf2nGSDCjbmMNxbVh1F3OxKIhWyN_aXg9WxMayTtCEccissm6bLHOo23s1cFMVRSxUasyZXQsSUQvSpx1YLVnPfsK-gf_CUdL1LadQf8swqB89jE20yhGnf5kfd78bOa_2A6I7aXdZTvOt2KwpJkJyCJGoX8WfQDGv0IE0YDcFvRp5WquNGOc4q_Gy36rXDm7vnKrYz_eeMwe2xiO5eoVGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3880986582.mp4?token=AJSmrC00n2egliaTC6rUtmDJiKOXx7_Ce3Lgpq4seI0gacnvUzkoIUO3FFBKj01BGKmayjHSsDTmIhixpSZ3Xp9x4t5haIhp7EXT4cD8KGBMWn0gBC7Eau9y8MlQhFLtf2nGSDCjbmMNxbVh1F3OxKIhWyN_aXg9WxMayTtCEccissm6bLHOo23s1cFMVRSxUasyZXQsSUQvSpx1YLVnPfsK-gf_CUdL1LadQf8swqB89jE20yhGnf5kfd78bOa_2A6I7aXdZTvOt2KwpJkJyCJGoX8WfQDGv0IE0YDcFvRp5WquNGOc4q_Gy36rXDm7vnKrYz_eeMwe2xiO5eoVGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صداوسیما سرود پیروزی پخش کرد :
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/128155" target="_blank">📅 11:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128154">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: حدود ۱۰ ساعت از اعلام توافق بین واشنگتن و تهران می‌گذرد اما نتانیاهو هنوز در سکوت به سر می برد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/128154" target="_blank">📅 11:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128153">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
وزارت خارجه کویت: از توافق میان ایالات متحده و ایران استقبال می‌کنیم و از نقش پاکستان و قطر که در دستیابی به آن نقش داشته‌اند، قدردانی می‌کنیم.
🔴
امیدواریم این تفاهم، حسن همجواری و عدم مداخله در امور داخلی کشورها را تقویت کند.
🔴
از همه طرف‌ها می‌خواهیم با روحیه‌ای مثبت و سازنده در مذاکرات آینده مشارکت کنند تا ثبات تقویت شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/128153" target="_blank">📅 11:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128152">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39f0972d8b.mp4?token=YoRpK11b_XlXo2dtvqsvsCSNP0bFnBKalyjVD-4lzm-LscVSdt9-CamYrAEzQ8u4sJDa-b7525NLYU_uDePPnrGbvSXhpTldidXCmEyb-LotO4qqmkVrhB20CnZacqRzMhkTxlZK2ibaVOJ-rL2dbVuKZKVu2-AO0-A8WdKr6Qp81SMN0wyeoSaL2zWJMVO2fcrVsriLzrxunC7vxQvrAyhoNpUoarrKjL5Rl3zUjR9_2qtKTJs0D12b709WZxDRnWsfW4ZUeGD3f5wiWnXVbc9XQG3RvgWZlPCn4CZ7YjvndPNnazmyBtEjenK9iNQbzYm8z5o0diMfx4lRj-NoBzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39f0972d8b.mp4?token=YoRpK11b_XlXo2dtvqsvsCSNP0bFnBKalyjVD-4lzm-LscVSdt9-CamYrAEzQ8u4sJDa-b7525NLYU_uDePPnrGbvSXhpTldidXCmEyb-LotO4qqmkVrhB20CnZacqRzMhkTxlZK2ibaVOJ-rL2dbVuKZKVu2-AO0-A8WdKr6Qp81SMN0wyeoSaL2zWJMVO2fcrVsriLzrxunC7vxQvrAyhoNpUoarrKjL5Rl3zUjR9_2qtKTJs0D12b709WZxDRnWsfW4ZUeGD3f5wiWnXVbc9XQG3RvgWZlPCn4CZ7YjvndPNnazmyBtEjenK9iNQbzYm8z5o0diMfx4lRj-NoBzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خوش‌چشم تحلیلگر ارشد صداوسیما:
من تعهد می‌دم ترامپ به شهباز شریف گفته حرف من دیگه خریدار نداره، بیا توییت بزن بگو توافق نهایی شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/128152" target="_blank">📅 11:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128151">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
رسایی: اینترنت رو قطع کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/128151" target="_blank">📅 11:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128149">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
خوارج برای امشب فراخوان دادن که همگی بریزن تو خیابون، تازه میگن مجتبی زنده نیست!
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/128149" target="_blank">📅 11:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128148">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dVB33-UNjSIbBA5wBkcj5JwekYnhUiorOTCEh8GNYSNydxkoKX3Iv5UJWOvCjuji3XgPUsrUR9nRNG5rXnwEDkKxYvMjkqlQx_L-YVXBTGkUBymGgCeZXEJUZmvg9ydWRVdcG7uoqGlyDGKbnua720jRHCOdl9FkFt8MLbIfOgaofWr1bR19kHcUf4eqvjLr1XgkDmMZ_4dGuHEvI5PYO9XLDXVxO0jwnKYN6BvMSKF_doULN3rP9QzI9_JhgDSf3TF77xclYqfCbnpY9KLCx_tBwFRF5silTIvQsTd6ayIuSSm4YIC3NVxjIxAfWwKXYt8mRkMMq4i8g1dwwa269g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خوارج برای امشب فراخوان دادن که همگی بریزن تو خیابون، تازه میگن مجتبی زنده نیست!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/128148" target="_blank">📅 11:29 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

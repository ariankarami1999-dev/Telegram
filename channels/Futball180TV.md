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
<img src="https://cdn5.telesco.pe/file/ZW7l5BbdOaRH2QaHB2PDZQKTk7RmrJ9NYhtmm-3fC-xQItcinGT9ReVJ2OgEOXRyH44yccQMG1clTkUhSqe1qNNNIwpR6EZRTWHuT1Ry0a8XMnKsFmGr0CYg0v_yUAd1d3JDl9zM9WAaG-dMmiAPy5EJupkrr_UFmVvGumBlDv0va1Q0fOmgHxQ_LRJOWk1ZCKh5UZ9vVRCv58rJwNyWtCIBQZ85WbF_xO0HgGZgBuJ7kdEZeLZxrvfY0KAG0Pe-c7NNXUynGrwf6HHBVeHsCvSlhplCoV5bgJLBWWW0MzO4bw5SpnFZE1TUYLkyV4sFxqXvg_vxE9HuNwHAShKj6Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 397K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 18:44:52</div>
<hr>

<div class="tg-post" id="msg-107498">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68583cf71d.mp4?token=SNs-ftRhrUcxhvHqFhQp9QZDWIMOByRy3zHPKt-LEjoEMILUlo7jrNoYNdhAxpfDMXREYEAGS0Wc1Pl4nRaIFqWLOM3Hb1ckkQF-CGPv_Q9e_Fea_NhRkpOjjQxiD9iPJulLoDtKhTH-hYlnubBODx-Ri03tS0z_yIpAxFYeWh1Y_sHj5Eyak0BHv_yNaJZTDlHSOpJkcwGWK9kcIRYsH64SqHMNFRHctCZNMAS2m44cFYpL8-eLImIIE35GbxNRM9Q8vRwiyWm-A55Bfv68jyipLjfekxtmBgnKQCckKXmXSSZ9MfTVvVoyLSUMpoPvljgwkGvDw54f_imOTVB6TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68583cf71d.mp4?token=SNs-ftRhrUcxhvHqFhQp9QZDWIMOByRy3zHPKt-LEjoEMILUlo7jrNoYNdhAxpfDMXREYEAGS0Wc1Pl4nRaIFqWLOM3Hb1ckkQF-CGPv_Q9e_Fea_NhRkpOjjQxiD9iPJulLoDtKhTH-hYlnubBODx-Ri03tS0z_yIpAxFYeWh1Y_sHj5Eyak0BHv_yNaJZTDlHSOpJkcwGWK9kcIRYsH64SqHMNFRHctCZNMAS2m44cFYpL8-eLImIIE35GbxNRM9Q8vRwiyWm-A55Bfv68jyipLjfekxtmBgnKQCckKXmXSSZ9MfTVvVoyLSUMpoPvljgwkGvDw54f_imOTVB6TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
صداوسیما والیبال را هم از روی آپارات پخش کرد/ بودجه ۴۰ همتی برای مخفی‌کردن لوگو!
📺
سازمان صداوسیما که به‌خاطر پخش قسمتی از یک سریال تلویزیونی در کانال آپارات کاربری عادی به نام نفیسه‌جون، از این سایت شکایت کرده و دنبال جریمه ۳٫۵ همتی است، بازهم برای پخش مسابقات ناگویا تصویر زنده آپارات را بدون رعایت حقوق ناشر تحویل مردم داد.
🤯
جالب این‌که همچنان سانسورچی به‌دنبال محو لوگوی آپارات است و مجری تلویزیون قطع پخش را به ارتباط با مرکز(!) مربوط می‌داند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/Futball180TV/107498" target="_blank">📅 18:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107497">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKeOcU2kHSJxP3tTDuyqx_PZxC-c-HJ7u48jAVf01AlBHWuJce8pH-J8j5Q8KyK6yha9QI3g5xOJdSmn89e7Yd5-kymshKRfDguCFV3K0zhXctPMajWM8z5vgM8z3_omMvc-KuFxTgLBpYQFhyzgg8_W1NgVXtZ3VEo8mkSOsHEqG4kvviAgmynT2d96lqOCFG1E9q0x_l9sgKeG-t5aVrAWBkFijiH8N9LBz6T2AV0VrFvgn6upWqYqDZOEcLUenZ0wiBaB9Mb9qOwkPtjI8P3bvep6dyZ4pSZSSrM1nFfOEpai710UfI2hUWdGHPLkRt5oRHH1oNRkRgAqCr2InA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب تیم ملی ایران مقابل روسیه
سید حسین حسینی، شجاع خلیل‌زاده، علی نعمتی، صالح حردانی، آریا یوسفی، رامین رضاییان، سعید عزت‌اللهی، محمد قربانی، محمد مهدی محبی، سردار آزمون و مهدی طارمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/Futball180TV/107497" target="_blank">📅 18:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107496">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlHfq9eIKjUsFN2XgtcgBIlgU8AUCvSi-kLhXzHQKyTCofmVjY1dat9kLSKzncxfDsP_pusRq32BLYxv9RWMRnEtKIjT2rLvkUVINwxDBC9eoVEAciH7WWFLys7B6H7zHENzKgeXGVGuVW-TAEz7JtR9YbqXsq1LL5UMrEMeSYHWKovJEmHO887SKQi-z37awaq0HbQlWRgcZ1uz09GFVEYpVPtHYUFTWU5ssKi2xFPHK7rd7Id5_FVKsR748G7lZN7Ck2ddrzAbpDDPJzLoqsLJ8bj-tLAE2RUhmc1y6NNu7_auV41dU5djzHMIKlgew6qM_gcWU4ok0HTo-m50Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚑
مصدومیت های کریر رافینیا
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/Futball180TV/107496" target="_blank">📅 17:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107495">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30660fe341.mp4?token=oKTsmbcKBBImvdyqaN0mu89ZVs46b2px5gjNciZiwT4R8bVSZjsGUb5GI8n__SEf6oMl7u347yqYUr-twnh96LgZYZhsraZ9msLOVI6wEDDdlcoo9FrA6pHC6STACCiZVQoAqa2SbTqAmNwcTnJLqahv66Hbbmv1FImOXoZuVryZPbEiQXgWlHTHYiMZywJTYmwbnkXHztzkn8GNfnIxfqGsieTDk4-hk5YT-zW6VNPLooRpZ1T5Q482tyDwmtP40Eyr2PqqKT2H-CAWpySTP1PPHe2xeV9qbQzidd_f2uUS-Et1jNi-UAew4UNL3HM13lUE8d9Ga8fTxqllqYb_2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30660fe341.mp4?token=oKTsmbcKBBImvdyqaN0mu89ZVs46b2px5gjNciZiwT4R8bVSZjsGUb5GI8n__SEf6oMl7u347yqYUr-twnh96LgZYZhsraZ9msLOVI6wEDDdlcoo9FrA6pHC6STACCiZVQoAqa2SbTqAmNwcTnJLqahv66Hbbmv1FImOXoZuVryZPbEiQXgWlHTHYiMZywJTYmwbnkXHztzkn8GNfnIxfqGsieTDk4-hk5YT-zW6VNPLooRpZ1T5Q482tyDwmtP40Eyr2PqqKT2H-CAWpySTP1PPHe2xeV9qbQzidd_f2uUS-Et1jNi-UAew4UNL3HM13lUE8d9Ga8fTxqllqYb_2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
على تاجرنيا: با والتر ماتزاری به دُمش رسیده بودیم اما پیام های داخلی برخی هواداران پرسپولیس باعث شد قراردادمان امضا نشود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/Futball180TV/107495" target="_blank">📅 16:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107494">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa385d1d9b.mp4?token=I-RmjWlAN138wQvcvx-p87TnKKwe3DHADPeFYptHklNpfHdMYP9w00gq4tfgk79zeuB9iBwAuy2XSms3EKkqfl_LZbRLvKLpyEn0I6bAjcRm2BgI58DEy8yBfeEE_OdsHqJNDSEbrsRYEm8ujeMQI2CriwtD9uJtocoBcfXc_CB_-90S32bgNRB-3VL4byvRzJbZfX3T8j4gKUV-qEcAmpwLBi8S_oPE_R9JJCuE27GUGHqc5SKtGR5x13_fNYYDy4kgwuS5joUygACanCDqx8H1HlRXJXxu1TazhO14cPae2vnCqaKy3WrptEgjxDlLQVajIO7xEqraYbUfCtbpEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa385d1d9b.mp4?token=I-RmjWlAN138wQvcvx-p87TnKKwe3DHADPeFYptHklNpfHdMYP9w00gq4tfgk79zeuB9iBwAuy2XSms3EKkqfl_LZbRLvKLpyEn0I6bAjcRm2BgI58DEy8yBfeEE_OdsHqJNDSEbrsRYEm8ujeMQI2CriwtD9uJtocoBcfXc_CB_-90S32bgNRB-3VL4byvRzJbZfX3T8j4gKUV-qEcAmpwLBi8S_oPE_R9JJCuE27GUGHqc5SKtGR5x13_fNYYDy4kgwuS5joUygACanCDqx8H1HlRXJXxu1TazhO14cPae2vnCqaKy3WrptEgjxDlLQVajIO7xEqraYbUfCtbpEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
وقتی امیرحسین‌قیاسی با چندین یوتیوبر مصاحبه و از درآمد عجیبشون سوال میپرسه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/107494" target="_blank">📅 16:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107493">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39b949da6c.mp4?token=aWIuIYQLiE4QLZSwbjuaLvCXW-PjaFLK_bn_PN_3V6-P0cNsbz28P_sNbv7RRzpZFIvdjoozYOtg-t7Zzre0U_dxskzB9Pw2Z8qt7kYA-KsH-tu_3gerrJDOc4ZPKMTt9AhWrsqYH4_dq3PmSps9Hbj3rg4LXFylf84St3ko2L6JeBVZuV-UQzfnTu351MEJyjA9TzZp_GjTQInklcaZg1dAwQ5V0rgIg3E74C72evgf1hWOJ3HpHIiCf6uAriT5fm6pqbQJkJoY7hQBQWX5i9cBUtV_Q1K5F0K2Ng0larDvnCCssDb-x9INrQA49ZEJTQAq51mJA8fQk8joGjYsaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39b949da6c.mp4?token=aWIuIYQLiE4QLZSwbjuaLvCXW-PjaFLK_bn_PN_3V6-P0cNsbz28P_sNbv7RRzpZFIvdjoozYOtg-t7Zzre0U_dxskzB9Pw2Z8qt7kYA-KsH-tu_3gerrJDOc4ZPKMTt9AhWrsqYH4_dq3PmSps9Hbj3rg4LXFylf84St3ko2L6JeBVZuV-UQzfnTu351MEJyjA9TzZp_GjTQInklcaZg1dAwQ5V0rgIg3E74C72evgf1hWOJ3HpHIiCf6uAriT5fm6pqbQJkJoY7hQBQWX5i9cBUtV_Q1K5F0K2Ng0larDvnCCssDb-x9INrQA49ZEJTQAq51mJA8fQk8joGjYsaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
#
نوستالژی
؛ درگیری تاریخی علی‌دایی و محمود فکری درباره تیم‌ملی در دهه هشتاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/107493" target="_blank">📅 16:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107492">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/St_nzex2VJ6-6n1HnqeKCfh_Yl9SyPpr9cct2qUOSgqDQK1TPPpgdXprZujGrw5io00SaP51FKJuNufQ2Ni8XpmeHsZcigWAuCg7ZOZp59uhx6I3YSU27tJHQ0wPxxUuf58l_pH89J-v0j2komyu30d0wgVNIoNb2pqCYVVY-7yEZrdCWfrn2ayQaJj1JOgLVw-AX3RXfYzam01Y95c7vDDPuGVKLOLRbHHl_tQjmPzauFtZYX4fIEDseX6aZ7VH9PhB5B1G3pEL6Gr0yfNN8j87BqcANm3aUB4aVUerevYKmDB3q8m8UvtVzK9dzuE2oeD7ryvej07jcPhVJejcNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🇪🇸
میزان دوندگی تیم‌های لالیگایی با رتبه فعلی آنها در جدول مسابقات این‌فصل!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/107492" target="_blank">📅 15:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107491">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بررسی پرونده فساد مالی منچسترسیتی به روایت دقیق رسول‌مجیدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/107491" target="_blank">📅 15:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107490">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚑
#فوووووری
؛ رافینیا در بازی امروز برزیل از ناحیه ران دچار مصدومیت شده و از زمین خارج شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/107490" target="_blank">📅 15:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107489">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11af8c0994.mp4?token=lRR1c72iqYa_5rZXVlKCxg9ACSbsu8YwY8wEc7Hha1YhUOdG_x3BiKXrGbhp5PKyU449Gi0dvJpb1yUIGXRT-KRVpfgZfudAK8iGh_So3BMCy4quWHYdIdMXCyO6bE5-wxvgvh9uGA4fY9ziqRmrdWYxzjoTQM2gskSGRZ7ydlNEsV5k0C3iuTm-D9Sl1rIZHoQLrf4n5QThiiB3q-_9XxpAOcOx7GwBFzHmUvMMkZsmH3I0JamtPPmvNp5ofW9Ao32FC0uC49j7TWx2WoiC-P_UoqLEwH90Ff5nrLmwbo8g5AB0SSzDhxcrHzk36xAuva0LW_DDjDkYLadbs_mPNoUwm9q4eAmJ0rINpyD54PHOueo0kUkE-RSiy8Vjx48A618JTNq2SrhQ7zJsSJ5ZKcXJVOF2o18VCywo60ixANufMVnYowxf58FLmjykH6I4gAV_p6ImOoseLmdqAFDAZu7U3wnJSaUhuuUuq5LCBY7mEake1kah71wtOP5HaoPMpsBWHcCoRt3lG444_JmEe7PczQI8xzHGLHCLp4641n2KzZy1x7H9isIqb-pce6LKkyCUCuU_UspCAc-Ti-L4DLKh_1UQf1xzaWHRwQPeGdzWbYXw87SoRRZ0MsQYEUJB7wd60a47i-NKzy9KaptVcODa90QDhp4bP_au_MLBCg0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11af8c0994.mp4?token=lRR1c72iqYa_5rZXVlKCxg9ACSbsu8YwY8wEc7Hha1YhUOdG_x3BiKXrGbhp5PKyU449Gi0dvJpb1yUIGXRT-KRVpfgZfudAK8iGh_So3BMCy4quWHYdIdMXCyO6bE5-wxvgvh9uGA4fY9ziqRmrdWYxzjoTQM2gskSGRZ7ydlNEsV5k0C3iuTm-D9Sl1rIZHoQLrf4n5QThiiB3q-_9XxpAOcOx7GwBFzHmUvMMkZsmH3I0JamtPPmvNp5ofW9Ao32FC0uC49j7TWx2WoiC-P_UoqLEwH90Ff5nrLmwbo8g5AB0SSzDhxcrHzk36xAuva0LW_DDjDkYLadbs_mPNoUwm9q4eAmJ0rINpyD54PHOueo0kUkE-RSiy8Vjx48A618JTNq2SrhQ7zJsSJ5ZKcXJVOF2o18VCywo60ixANufMVnYowxf58FLmjykH6I4gAV_p6ImOoseLmdqAFDAZu7U3wnJSaUhuuUuq5LCBY7mEake1kah71wtOP5HaoPMpsBWHcCoRt3lG444_JmEe7PczQI8xzHGLHCLp4641n2KzZy1x7H9isIqb-pce6LKkyCUCuU_UspCAc-Ti-L4DLKh_1UQf1xzaWHRwQPeGdzWbYXw87SoRRZ0MsQYEUJB7wd60a47i-NKzy9KaptVcODa90QDhp4bP_au_MLBCg0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
اگه‌یه فرد سیگاری هستی حتما این ویدیو رو ببین و برای دوستات بفرست؛ تاثیر مخرب سیگار روی سلامتی از زبان دکتر رهبری...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/107489" target="_blank">📅 14:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107488">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd91aee857.mp4?token=SjjW7lhWyea4RVJ66PkalTabTPWEDN0SWyVsRLb5CrTQC8ayfPjU-DTspt1wbvaeoAU5HECptaQWhsORyWe-eJIjXTcjw61PahevQ5Y-ALw1G6BfoW16NSpYprTmCzpxeuZvIPVSRodC0SMXryxce7PS2X6pVkDfVD_4hKNKhW8jN3OCsiRllWMnMIqWrWf9XyLu4qvivK9nKTJzGbQ9aTqbeRjob2sDpOV4Gy6pq-WAhHkJN1A4ei1ETCHreR4ClHA4lNlitLXyPdky4a8sbgX30ddzG4uuqP-voGzKs6et0yrFuYiUeOX33jZFFC1BbgTcIOXhKyP37p00kWXzxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd91aee857.mp4?token=SjjW7lhWyea4RVJ66PkalTabTPWEDN0SWyVsRLb5CrTQC8ayfPjU-DTspt1wbvaeoAU5HECptaQWhsORyWe-eJIjXTcjw61PahevQ5Y-ALw1G6BfoW16NSpYprTmCzpxeuZvIPVSRodC0SMXryxce7PS2X6pVkDfVD_4hKNKhW8jN3OCsiRllWMnMIqWrWf9XyLu4qvivK9nKTJzGbQ9aTqbeRjob2sDpOV4Gy6pq-WAhHkJN1A4ei1ETCHreR4ClHA4lNlitLXyPdky4a8sbgX30ddzG4uuqP-voGzKs6et0yrFuYiUeOX33jZFFC1BbgTcIOXhKyP37p00kWXzxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇵🇹
پیام‌واضح ژسوس به رونالدو پس از نیمکت‌ نشینی در آخرین بازی پرتغال مقابل نروژ!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/107488" target="_blank">📅 14:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107487">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bf450995b.mp4?token=FUvgq-FTbOTdLldlU_7D8AyTe-o38DXyaj21ukOzY5nP0HE7g4X_XHndWzU6NEQ14XWpyz7A8Iz2AZ6ZQaSVtc6C2A5YXonRUWiHGA56GuuIkCVc3hZWprB56FiY0S5-IwpvEnKperGZZWPxotTYp7aUB3fMUn20Pv46YgjWME9WyV3-lFZ1e39ZDRvX53rWV30O6VV-lGXCCI3ZPd-D0XRSwdJ-rnZYF06IYtmCDSAoDZ1SLw1adWvX6R8j848asBjk1P4yTu4UgSUDlBYDKQxdgkO2QnDys3Gwq06WwL-F0xav1OdND24OqWnzgrJu5SCLtFTcLTsCRJPif7uz6rp1K__-xMZlkhL5QXPyGey7_1P95S8FP53Nzn1oEqnYj9NnzGiAXh_Cbvnr5ruuccX9b4q9s3wgBeS9uJfrVfYEpAfRZzlXnPnVVQHrS5xBAW_vFp6mdtzDuF3uEStXP8ZrDg5d6m3qnRMYCEtyN5jAP-wLxdGWEA5CWDdgEIB6pREA7KRcCl_H3zVkdC1iizm6ndv_ouOxiGccmzdMxIvJr2eH_C3-RrUSgWFkJF4PRKF1cns1PEIpCS28yzm41nz607i-AMLxnm_JZwewRpwyYBB3Xld2UmgtLh4kFq6fnX16wXGNN7ii5w9qBufKOD0rQCI2Xc8GoSrssvrI_yM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bf450995b.mp4?token=FUvgq-FTbOTdLldlU_7D8AyTe-o38DXyaj21ukOzY5nP0HE7g4X_XHndWzU6NEQ14XWpyz7A8Iz2AZ6ZQaSVtc6C2A5YXonRUWiHGA56GuuIkCVc3hZWprB56FiY0S5-IwpvEnKperGZZWPxotTYp7aUB3fMUn20Pv46YgjWME9WyV3-lFZ1e39ZDRvX53rWV30O6VV-lGXCCI3ZPd-D0XRSwdJ-rnZYF06IYtmCDSAoDZ1SLw1adWvX6R8j848asBjk1P4yTu4UgSUDlBYDKQxdgkO2QnDys3Gwq06WwL-F0xav1OdND24OqWnzgrJu5SCLtFTcLTsCRJPif7uz6rp1K__-xMZlkhL5QXPyGey7_1P95S8FP53Nzn1oEqnYj9NnzGiAXh_Cbvnr5ruuccX9b4q9s3wgBeS9uJfrVfYEpAfRZzlXnPnVVQHrS5xBAW_vFp6mdtzDuF3uEStXP8ZrDg5d6m3qnRMYCEtyN5jAP-wLxdGWEA5CWDdgEIB6pREA7KRcCl_H3zVkdC1iizm6ndv_ouOxiGccmzdMxIvJr2eH_C3-RrUSgWFkJF4PRKF1cns1PEIpCS28yzm41nz607i-AMLxnm_JZwewRpwyYBB3Xld2UmgtLh4kFq6fnX16wXGNN7ii5w9qBufKOD0rQCI2Xc8GoSrssvrI_yM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
دیس دکتر ابوطالب‌حسینی به دکتر بیرانوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/107487" target="_blank">📅 14:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107486">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09a02722eb.mp4?token=FNi1qzGTMtPbcbDyzycVl8LpIZb6BzGmKyZv0Iuy9x18itj8zlF7TR-J3V8ZaYGTybG2y7dr234wGaV3t6in9Zdi41Vz4PeRf2NrQKIwDb3cqaPbfaFAScaz4VI_So0TOuvHLUF-aoxwP0lKIhf9wLdNSiMWv9HySIJief3VnQZWHDQ2kAPij_gXhVpfEDFSY3CLpOo9v4yVbHi1rx_4P7AUHn5m6fGVZNQ9klExaiwWd68fw7gbjajMXohEY7ZCK7G_5x5YvmixQ73zbWLIv_2utNgiyETt9mIZ_Rid8g7oPL8VYG3DHNaRKmGIO3uodYz3JFPWNHmtlSs36GqekA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09a02722eb.mp4?token=FNi1qzGTMtPbcbDyzycVl8LpIZb6BzGmKyZv0Iuy9x18itj8zlF7TR-J3V8ZaYGTybG2y7dr234wGaV3t6in9Zdi41Vz4PeRf2NrQKIwDb3cqaPbfaFAScaz4VI_So0TOuvHLUF-aoxwP0lKIhf9wLdNSiMWv9HySIJief3VnQZWHDQ2kAPij_gXhVpfEDFSY3CLpOo9v4yVbHi1rx_4P7AUHn5m6fGVZNQ9klExaiwWd68fw7gbjajMXohEY7ZCK7G_5x5YvmixQ73zbWLIv_2utNgiyETt9mIZ_Rid8g7oPL8VYG3DHNaRKmGIO3uodYz3JFPWNHmtlSs36GqekA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
عادل: ناکامی تیم ملی مثل داستان تورم شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/107486" target="_blank">📅 13:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107485">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ee940a4.mp4?token=ZgP8g1n8_zg6jx223gPvGOw5Xne6ZsEhKTnS8QBYC4BXIIDi5pYDYfLMKhyK3Rzp620-rsnhVNE6OTkuUvNSwUL8esg_6kaWCcVTsrySk481PNAQPkqblV3ClvuKaOutwZTVOaF-b7E0gVdQSmCfYIHAHBqhLF12gZFbDpqP-wrEzAKsHvDyO2fpaMIPOSUVXe0bFl9QVBffUTODJD_-NBMua5jkHds6hmxbVkIaLYQeEO6orCm-9rDszgpi66-fbDs_rC9etQO2wGdUHIeMYU7PB4JwdejgTTjTlGvOtmy47hJErCMxaJ_cZuZ84f-sBVizLdeNJ3XPhwDSvt6m_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ee940a4.mp4?token=ZgP8g1n8_zg6jx223gPvGOw5Xne6ZsEhKTnS8QBYC4BXIIDi5pYDYfLMKhyK3Rzp620-rsnhVNE6OTkuUvNSwUL8esg_6kaWCcVTsrySk481PNAQPkqblV3ClvuKaOutwZTVOaF-b7E0gVdQSmCfYIHAHBqhLF12gZFbDpqP-wrEzAKsHvDyO2fpaMIPOSUVXe0bFl9QVBffUTODJD_-NBMua5jkHds6hmxbVkIaLYQeEO6orCm-9rDszgpi66-fbDs_rC9etQO2wGdUHIeMYU7PB4JwdejgTTjTlGvOtmy47hJErCMxaJ_cZuZ84f-sBVizLdeNJ3XPhwDSvt6m_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
📱
پست‌جدید سعید صادقی بازیکن سابق پرسپولیس که خبر از ازدواج‌خود می‌دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/107485" target="_blank">📅 13:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107484">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‼️
نیکولاس‌سوله مدافع سابق بایرن و دورتمند این روزها مشغول دروازه‌بانی در لیگ‌های پایین آلمانه
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/107484" target="_blank">📅 13:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107483">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0bf7aaba1.mp4?token=sXdo2GWA72FPoWLTqX6u9TdEncAKtAbjwzQZUD_N-Yq8c46KySTWWWjmY9PspE1FT9dc0GcFH9gei29AAkQo9K2hQbMz7t2Wy7obTqc2xqzaLpfMjVPkbkO3Js-JKv-ErCuA4r2JfZr5wVnOEOmUrk8WytX4NwB7G5bjf4L4q_rJg9ruYNME7B3k5vcxGatiobgathm59PbAmRzeQ8IKn6on6lY0x2By1kKU46bL8CgqWxVnLuToA0bRYB7FdiTbxDTbpDlgWhVzOkkL_MGkbB8umFPrEsSLzXEDOH5RI36nd0MybApZQTdzwJFD2e2n7L7mDUbwEXzgRPxvOat8Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0bf7aaba1.mp4?token=sXdo2GWA72FPoWLTqX6u9TdEncAKtAbjwzQZUD_N-Yq8c46KySTWWWjmY9PspE1FT9dc0GcFH9gei29AAkQo9K2hQbMz7t2Wy7obTqc2xqzaLpfMjVPkbkO3Js-JKv-ErCuA4r2JfZr5wVnOEOmUrk8WytX4NwB7G5bjf4L4q_rJg9ruYNME7B3k5vcxGatiobgathm59PbAmRzeQ8IKn6on6lY0x2By1kKU46bL8CgqWxVnLuToA0bRYB7FdiTbxDTbpDlgWhVzOkkL_MGkbB8umFPrEsSLzXEDOH5RI36nd0MybApZQTdzwJFD2e2n7L7mDUbwEXzgRPxvOat8Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
👀
وضعیت وینیسیوس در بازی با استرالیا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/107483" target="_blank">📅 12:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107482">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgixkyLK6Y9_Dp-sBmfSHgUyNaXYfs4SDho92IM0T9QDqY-Bozmldm3TkxB1E5fozjliZSaJOPQn8W5Zv9ZhV3-koYMdWeq6Ubn8LTN7bLfW9GmwRPeB7V6Q8xn_bpTdyjhIXZD24Fe4tZ11_ly6_6IjOgje8FtALSzLgOa1TVafQWlxY3vnr9LUqTPWo7yJPMYjuS0kYlQxOB6n-DnXCC3WsmGlOKfcH2iLm1PET3GOUYI_fhE3gIYlitttAJRRnSc4nDbAz-qbPB98Nu5B0W0h8hf24iHek7naysAry2RwMmq5UGIbAwxTohY68x2P-HriNHVB0CBPC9GavzkVHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
علیرضا بیرانوند به دلیل تاهل، داشتن دو فرزند و شش سال فعالیت مستمر در بسیج، ۱۵ ماه کسر از خدمت دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/107482" target="_blank">📅 12:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107481">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2592f7770.mp4?token=VLJiKy9CQR8-poSMuyq4WJttc26mIk-1pDFX6ORiARK2l3hAGj7qnad2JxE2Pj0Oq2chFgQrjKIuA501gXB2QD3exqcKl7TrB8N_CTCqjAhvNPuTuAl_N3MWMDHbNZloDhlmbYZ58bs4moJI1iqtaAw1eT-dD2gr8IxeOeF4InW4xtZmV2tKUBTG_KHfNpRn2osFyJ8nTl487T6YtW_DZ0H0y7TJQIMzfRg3USf7i6xGyv8VdZu5FJPD8JnFLkyeiwT3hGjMG_HAhHz9fkPyK3NU8R3r8GRCevYD8Kh8gLh-sc94alrwbjKPbIHcTCXUyjMPad6oiMSNjSlQzEY7jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2592f7770.mp4?token=VLJiKy9CQR8-poSMuyq4WJttc26mIk-1pDFX6ORiARK2l3hAGj7qnad2JxE2Pj0Oq2chFgQrjKIuA501gXB2QD3exqcKl7TrB8N_CTCqjAhvNPuTuAl_N3MWMDHbNZloDhlmbYZ58bs4moJI1iqtaAw1eT-dD2gr8IxeOeF4InW4xtZmV2tKUBTG_KHfNpRn2osFyJ8nTl487T6YtW_DZ0H0y7TJQIMzfRg3USf7i6xGyv8VdZu5FJPD8JnFLkyeiwT3hGjMG_HAhHz9fkPyK3NU8R3r8GRCevYD8Kh8gLh-sc94alrwbjKPbIHcTCXUyjMPad6oiMSNjSlQzEY7jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
خاطره خنده‌دار امیرحسین صادقی از سوتی وحشتناک حنیف عمران‌زاده مدافع سابق استقلال وسط مکه
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/107481" target="_blank">📅 12:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107480">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OA4eVSwz4kCQcw7blEtO92Wmg4bjmUWx5LMNv5DquGxazsGa7pOxUk0rfkg5WjQviP02SILnzhZBVJB0YmJyQ5yv0u170fdH5DuLBnL0xJXiNslTSWNmesADfsWb3Pi5j2J_AgFaRKKXKP8RqzIdZUmfpAq6payzo7ueOg7gjS7ZYlPXpjmI3cPQxyONs7rd10qttUFGB-kvLkreA47235QjJxSwk36YHlMHXTFE0r6vPLHLqKJO12Di_Xd-li3hKrgcLvpzESJOCssqN_V2od-fTS846SFwPPaqyJ8MCojf15aRJgbId8GMxDlKT942BeE7cntNuBNBVBM5f2puJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
ترکیب‌رسمی برزیل مقابل استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/107480" target="_blank">📅 12:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107479">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e6f4de836.mp4?token=LebN8hIEF8d6NJoQX7C_OPhgm7WocEvaSSfXmGS8F91wu74kRm5jP_yWpjYagAZx9UaDERDdJqjz5NKTqEN70i7cDUu5HmzKbx1Wj31tDkH0AeZ3umDNHhOG5XEAtobcQy5VgEX9wo0JgWyzzREr_bgDTQguOB6YRnbkkoG3EjbweZS09Fan0bNmAtI1VURaMseoH4TwWz8wh3K_W_KJa2PnZIZDQlC1vmGU763og1RTotWAqZGHi5QyEybYCSW2NxX-oajIJ2DMW3Iuf3dbAiqijc6ORz6FNk0lu9ypDqhV6smNbWO1XxfrdqztbP9iVxLS5B3RXjMZF_lWtpWqvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e6f4de836.mp4?token=LebN8hIEF8d6NJoQX7C_OPhgm7WocEvaSSfXmGS8F91wu74kRm5jP_yWpjYagAZx9UaDERDdJqjz5NKTqEN70i7cDUu5HmzKbx1Wj31tDkH0AeZ3umDNHhOG5XEAtobcQy5VgEX9wo0JgWyzzREr_bgDTQguOB6YRnbkkoG3EjbweZS09Fan0bNmAtI1VURaMseoH4TwWz8wh3K_W_KJa2PnZIZDQlC1vmGU763og1RTotWAqZGHi5QyEybYCSW2NxX-oajIJ2DMW3Iuf3dbAiqijc6ORz6FNk0lu9ypDqhV6smNbWO1XxfrdqztbP9iVxLS5B3RXjMZF_lWtpWqvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
تشکر عادل فردوسی‌پور از ابوطالب‌حسینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/107479" target="_blank">📅 11:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107478">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evl2uDL9fuPycLsSgxfMmXPfTtvgBSUhSl7i3kHNN3335bayp712zggeb37pHPCrL-y4bD-cJTAHTty-1oxrG7IexdQ7KNRRQkzhLiF4K1bFwdPBWDrha7oJqTYOc44d7qSlLAsjHCsfrxXpOqTQqxGW4D1Mx9-pobS9kNmSmk2jDXyGOdlRIVR2yo4HzSRO4abUKv_DOH30vZrklHhkJfcTyHEuXNN5NFs3s2AmX-oWAR0Ks9QdNpJ_cPYqBFrVElLBDhkUK5AjYhBGWG7gPNQkxP8OadxXxC7WvPh9whEgmO-bJeiQYPcA3L5p_pL--K-6naPVFE_p6EErzMsgfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💵
وضعیت دلار تا این لحظه: ۲۵۰ هزار تومان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/107478" target="_blank">📅 11:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107477">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRv7TvVpFO_1Ov9Q2oPoirgLomsp-BPnW8oacR1OUKdMETntVH3Xme2JfSNsdfVO05qzJcxHns2IvhLeRR6KZAsdNqUrfmRbVVby5hKv3kuCWe6_egFde1W2ef-e9H2UT7_zKpCanrYDB3N-g0x_ZA14JyPyOJoheVgdP8EJYqfzrrAA1UBXKMZPoGR7DKOEarMg2CmmbwFQuwghzBWKJj-BJxO4HlFulV4eE-Qh5sSUvLaxUE_rbbtmp5aptfCY20c0_zO-ONdXN24147r0aZijHTLUCXFuW4VEJAYfgmmab0SREsseMhfeaHt6i--crGS_DtPlyTezBn5CpsPF8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
‼️
🇪🇸
مقایسه آمار رافینیا زیر نظر فلیک‌و ژاوی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/107477" target="_blank">📅 11:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107476">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OrgmKHRi41wI4DAFhV55eGzLZbpkcvrCMWJwhbeoXoavbD-OM1-2zTEn8MghuYGR4574lI9IpdRelNLLeHHlYiv0FtHv6xRzarqBcac-aqYKNZE4EA36Tg6VVP_Fxudvs80FtOpVfWiorciyN-3fCvDzN7TsseGzOuaknaPWGBIR-8nYg35aLHeZyxASE9Th1EqqV_xmbMQl00myEnLKQtkU_r7iCQL0x6DpcnGNxNoDwqgGgybMqcqw4jViNvD9yfwjHxwDDOV0OapsL5f2mDNDofYK5ME8nUXpOcWNUSE7VhfyaPOdU4Fxb_mcwE-gAtwWmFA4Z5WNIy5rnzBhbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐐
بازیکنانی با بیشترین گل‌زده از روی ضربه آزاد در تاریخ فوتبال؛ لیونل‌مسی تنها دو گل تا تاریخ‌سازی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/107476" target="_blank">📅 11:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107475">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107475" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/107475" target="_blank">📅 11:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107474">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dh1ypW7yiKyRwgKtlXHIbcFFTa-coCACGpJwT5eodkG0QsugZ0djof3ktK9PDeczzzQu9LersSq1sys9nkZcs6u29lCq62HQl15HZ-tEHe1mdTNuNrR7qoElyoSUHO9tjXjFFbqSfnUJel3rfLEIKGrkERxuRBdnRtCuSFmp5eBMI4qIWnK6MypjdVWShYq1ohuLdULX0GV42qXgCGo3QJ0GmJo5qKnFgB-p13Vc5eWO9P3MOzAFK2lbCbnp4JKjgOAKFMZKKDqxIw2Z_XwF9Xb7s7CdGUN9YKeXFQ68mSQNx628HRhblAkcZCjO2P6e3qmU1j2FLpXw5CQed-BDXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
انگلیس
🆚
چک
کرواسی
🆚
اسپانیا
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/107474" target="_blank">📅 11:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107473">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3862876082.mp4?token=k_eA22j8H2rwaTQjn8SYD6VpP-vBoExWzfNT3kil9V5zlq1z5INqYkFIpjw_gzCrEqMiz3p33JK0etLNE9ofaN1imNB-AP5ZvvUjzvC7OVd0kENa6_7AoY6IieU4S9gLNRVXIzGFHi0p1hKZFsPLFyCOu5yAThth55ro1EYw-YQ8tsYW9K95OXh2FCJ9zGbkptWyU8O67oNjuNE_1GkY1bz-mxclfTZP9ZG1aocOTZK6nmNr3NEWRuYh5uHvpJJPtkeO15Cb3z9zhP-iafDTYjzdVitxN00yyHbLgAGbssan3iC-ziENDB4HJGwmt_OWrQNw96l9wijeoY2Y7R1Rmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3862876082.mp4?token=k_eA22j8H2rwaTQjn8SYD6VpP-vBoExWzfNT3kil9V5zlq1z5INqYkFIpjw_gzCrEqMiz3p33JK0etLNE9ofaN1imNB-AP5ZvvUjzvC7OVd0kENa6_7AoY6IieU4S9gLNRVXIzGFHi0p1hKZFsPLFyCOu5yAThth55ro1EYw-YQ8tsYW9K95OXh2FCJ9zGbkptWyU8O67oNjuNE_1GkY1bz-mxclfTZP9ZG1aocOTZK6nmNr3NEWRuYh5uHvpJJPtkeO15Cb3z9zhP-iafDTYjzdVitxN00yyHbLgAGbssan3iC-ziENDB4HJGwmt_OWrQNw96l9wijeoY2Y7R1Rmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😐
انجام پدیکور فرشاد احمدزاده بازیکن فولاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/107473" target="_blank">📅 11:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107472">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
‼️
⚠️
ضرب و شتم دو نوجوان سنندجی بدون گواهینامه توسط نیروی انتظامی که‌در فضای مجازی حسابی جنجالی شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/107472" target="_blank">📅 10:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107471">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae822cab56.mp4?token=h5_6c1MgxHsPktNNuT52HzRsyiWsCc2hsQNxJERRr0nB54l-B6IMmEJg6lyBLdfbYwrWczwXXlCi3IrRkb6izM3Z1Y-RtGClMHff-mMAvyi-AzkijS_Id_HNbezR9axuJKMDToG0QREwfi5EZDUF1uaQ9ptCfqxHWLu32PLJyq3g1FCfBXJB6DJlfspny0eePeVyPuGdqmsy3lq5HJRpwf3zEkpNjv_bS7Huf5Ri_DSb3fnVCLV1LNDH7ADMP80W3dkVXMwy3cDVM0VWk6563feDxO67JsTlgnuzmI3JNFDeS5TmXjhooVTaDQ_74hyBp9RlICfiNRXqJGedzxsjvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae822cab56.mp4?token=h5_6c1MgxHsPktNNuT52HzRsyiWsCc2hsQNxJERRr0nB54l-B6IMmEJg6lyBLdfbYwrWczwXXlCi3IrRkb6izM3Z1Y-RtGClMHff-mMAvyi-AzkijS_Id_HNbezR9axuJKMDToG0QREwfi5EZDUF1uaQ9ptCfqxHWLu32PLJyq3g1FCfBXJB6DJlfspny0eePeVyPuGdqmsy3lq5HJRpwf3zEkpNjv_bS7Huf5Ri_DSb3fnVCLV1LNDH7ADMP80W3dkVXMwy3cDVM0VWk6563feDxO67JsTlgnuzmI3JNFDeS5TmXjhooVTaDQ_74hyBp9RlICfiNRXqJGedzxsjvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یکی از عجیب‌ترین مصاحبه‌های امیرحسین قیاسی که پس از یکسال مجدد وایرال شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/107471" target="_blank">📅 10:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107470">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a5a16dba.mp4?token=C4Dhw_yqARJVS7XDFJXdZUDmY4o0otoWi1SSWZgKlA6XGaIkKosj1LJ0jMdexnPRjgU_AUfThQsq5_k54SZMacyghmv1Arlx9D2QxmM7_lALDSJ4iMBLVSV-8-ZPjXLVYAWCpHOMj7SZvhC6Bl9NBGalyW9fyB_B4dCiXbKDg7AhJuXdhiPo1ONMzuFo3StcKDaVtEVxFJ41ysk-q3rZtijSfwglUTCZxYL-G7L_GqjreCRHgkAub8WpshiqHAGFYlsCMK2FtRilb8T4hXRr7Gmul78jwFMoYCrpHSu_K1od1NMYJANDRDl5lWSuGdd-13sIoECwmfmtYv2E5-qk-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a5a16dba.mp4?token=C4Dhw_yqARJVS7XDFJXdZUDmY4o0otoWi1SSWZgKlA6XGaIkKosj1LJ0jMdexnPRjgU_AUfThQsq5_k54SZMacyghmv1Arlx9D2QxmM7_lALDSJ4iMBLVSV-8-ZPjXLVYAWCpHOMj7SZvhC6Bl9NBGalyW9fyB_B4dCiXbKDg7AhJuXdhiPo1ONMzuFo3StcKDaVtEVxFJ41ysk-q3rZtijSfwglUTCZxYL-G7L_GqjreCRHgkAub8WpshiqHAGFYlsCMK2FtRilb8T4hXRr7Gmul78jwFMoYCrpHSu_K1od1NMYJANDRDl5lWSuGdd-13sIoECwmfmtYv2E5-qk-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
محمد نصرتی بازیکن سابق تیم‌ملی: آقای قلعه‌نویی آن مصاحبه مهدی‌قایدی را نادیده بگیر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/107470" target="_blank">📅 09:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107469">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e0c6152c5.mp4?token=RF2vxL5xxJ0NrSpBAcEQWBnBWQ02YZPkyp43RUFpXp6Srm9kxiAZm_PO346Lue6Gg20KhjtM4nn5bnR2lgPJE92T2XfhmeP9PXrM_M7jYRKHA2LYaAHa_wbDx3m7Hunw2YxYZB4QQUeZa1l9o4S_K9cVyUKC887xiJXC-Hobn_9KlwrI2hTfjTXM7pVQjhu6AfreKv9pMASJAmj6lSYoRgAQVZgBi4FL9Dsn-wo4TxqJJ0b2JNTUiKl8WvIo-vbVk1xI3oYADZV9dgew_WKuMH9LlJvmhm1sstW7cKOH1elGL97QfoZPXgWP-B5sY20IEkmB9iqKQXy6Yq8NH7qMJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e0c6152c5.mp4?token=RF2vxL5xxJ0NrSpBAcEQWBnBWQ02YZPkyp43RUFpXp6Srm9kxiAZm_PO346Lue6Gg20KhjtM4nn5bnR2lgPJE92T2XfhmeP9PXrM_M7jYRKHA2LYaAHa_wbDx3m7Hunw2YxYZB4QQUeZa1l9o4S_K9cVyUKC887xiJXC-Hobn_9KlwrI2hTfjTXM7pVQjhu6AfreKv9pMASJAmj6lSYoRgAQVZgBi4FL9Dsn-wo4TxqJJ0b2JNTUiKl8WvIo-vbVk1xI3oYADZV9dgew_WKuMH9LlJvmhm1sstW7cKOH1elGL97QfoZPXgWP-B5sY20IEkmB9iqKQXy6Yq8NH7qMJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
🎙
تشکر هانی رامبد از مردم ایران بابت‌ حواشی اخیر: مرسی از حمایتتون!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/107469" target="_blank">📅 09:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107468">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/capaLf0LO-lhBemUNRPKEbC_atPeUVCeh1KhdBePE7vBfJ5qOKXYT2zVgzgHYtgF2u9eGkaHnHLud9bSXiQgO1ENvhOSAqWAzX05ZbvF9VJWuHnB4NJhyjYCU71KaTPNGNjMtCeYobQ3D_NP3CbHeDiddOKXBJvee_EBp6XvybhtKTTJ6bT0cQUcDHw61fYIPxMKFjeMLGaVeN5TfcqhjSVeDIojk4jh3DmUUKxVyv5vhi5Ol0VzwbhgoPv8fAWk3sP0d8EFxfuxIwUkiIK8YvV0qdz_ARIeCpRZT3aKx03PVA_7AUEIO9kEvZTiUssHl_6MSJvcrWtRhi9pncdwxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
‼️
تیم ملی اسپانیا هیچ‌گاه در دیدارهایی که لامین یامال را در ترکیب اصلی داشته، شکست نخورده :
🔴
۲۹ بازی؛ ۲۳ برد؛ ۶ تساوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/107468" target="_blank">📅 09:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107467">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bd2d848cb.mp4?token=DSiijoyV2yFYRVLV9rY-hBkq67bC9V0zSu-hytffCzvDJKtVLu-ECsXnJaSkgp3OvQ8T1HKmLuMe3OrIrsrw6Lh74Oj4jO6teOVFZ5F-4E6fRHLzWa_VLPR1-_1pKB0kx6GdllOkKkWRLImEuIFhobPBeJQDdK8M_hJMA2VJG4vBjW9tGFc0fA6narC3jBmm_oAV2-QNTt8678lR56xLYl2BCoO6eRg7-RdWAgNykSm03X0_vNh72xmoZF_FwYDvczosdvTkS3YdB_vQxYOLspnymQMmJrzX5L-UkZfy_-r4mk-etiKcRQ8cari7Phk5gPFDrj0MUTB3fnrz-TULazzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bd2d848cb.mp4?token=DSiijoyV2yFYRVLV9rY-hBkq67bC9V0zSu-hytffCzvDJKtVLu-ECsXnJaSkgp3OvQ8T1HKmLuMe3OrIrsrw6Lh74Oj4jO6teOVFZ5F-4E6fRHLzWa_VLPR1-_1pKB0kx6GdllOkKkWRLImEuIFhobPBeJQDdK8M_hJMA2VJG4vBjW9tGFc0fA6narC3jBmm_oAV2-QNTt8678lR56xLYl2BCoO6eRg7-RdWAgNykSm03X0_vNh72xmoZF_FwYDvczosdvTkS3YdB_vQxYOLspnymQMmJrzX5L-UkZfy_-r4mk-etiKcRQ8cari7Phk5gPFDrj0MUTB3fnrz-TULazzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇮🇷
پرونده قهرمان فصل نیمه تمام؛
جنگ بر سر جام نامرئی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107467" target="_blank">📅 08:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107464">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107464" target="_blank">📅 01:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107463">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYB-d8jMOXMJB8lR5kd36tUSQ9EyhrCmUytf9qw9C9s4B2uYg2zToFvfvaewy_czhRJSjhYNcz7BHZXysbJG9dzLlcBfA96377MzAAUd_oOZKAG4VgzblC9jbPswPLA-2WR4dS-_lnC66ijWO_iCN04d4fcPDEZFGONdK1guGpYANtqD7WyzVaHObGGhdbOGu3u2j_nHDLpyzCZbQbDgdpWp6giz-xsYqrKnRTtgt94EZgVjNjJG7gy84iBu7HzKbxFgr2hV72GyMP7yM7T6qAvvkSIViwcXIMUyAiEqbTfvSr2Vp7Jjb5QWycNl8YRdRiO8AG81AfbQYs04MWJo-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
❌
⭕️
🇮🇷
با اعلام سخنگوی فدراسیون، قراره جام فصل گذشته لیگ برتر به شهدای میناب تقدیم بشه و استقلال یه لوح یادگاری بگیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107463" target="_blank">📅 00:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107462">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/950f5d5e0b.mp4?token=Ruvr_vOsNFfkF1BW3YnttU_DEbxv7eNtVZtL0Vb7sxobjcpGtLnrJgJX9ERFLgrfmGgysq9Sd_kRp02wlVRLYPfrJXNjPqfB2huO_r2UDLGX3bjjc7M1f-E2QLSmk1hiD3_FoLMhuf8bkeu2_SruEUoa6uFQUpR3xJcFDD8MDBGJTpcoO4n5d4cACGJEQspH_thk3KH96V2bg0jK2-KeaOggQKLEQh4xSFDW3o_xPGrNQ75oBk9WIDPSn9cdrg1uIw5akfjau8uKbUxlB5VpIzVNoPzYy2QSESh9fw1_2B1sSI7Pgi41Havu37I0zMhsAuRnODD6uZR_2Wk3Dp8yA19Hxvxr0fiR0zwvBL9L8QhtT8J5GpA-_4ZRIe67nVn_AyAEuSWsMyvuZDwMul8mzTuemXAhVwAZCEzSqpwF_5EDv2fqg5IMN1SV0wzuKElRYldl3UdG1mi66cWRfF6GjZl1uLVL-zu35OvlQPqZhkjn1ziKc4u7YogZESsrNS402p4K0w8BpKteV5sKQ2UAb4vwkyZAMkbVk87zIVL6ZLBP_hxYjJvqDwPbju_ykq9bETYkgkBa7-PJ8tTcRR9JSDlpS7nK16UFAQ9lqPvd-yxy0zFKlMuolMSt2sH193_YwKwK6sk38MFNipqylCLbDKuk4fK6LaPLSaOVYZwcgq0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/950f5d5e0b.mp4?token=Ruvr_vOsNFfkF1BW3YnttU_DEbxv7eNtVZtL0Vb7sxobjcpGtLnrJgJX9ERFLgrfmGgysq9Sd_kRp02wlVRLYPfrJXNjPqfB2huO_r2UDLGX3bjjc7M1f-E2QLSmk1hiD3_FoLMhuf8bkeu2_SruEUoa6uFQUpR3xJcFDD8MDBGJTpcoO4n5d4cACGJEQspH_thk3KH96V2bg0jK2-KeaOggQKLEQh4xSFDW3o_xPGrNQ75oBk9WIDPSn9cdrg1uIw5akfjau8uKbUxlB5VpIzVNoPzYy2QSESh9fw1_2B1sSI7Pgi41Havu37I0zMhsAuRnODD6uZR_2Wk3Dp8yA19Hxvxr0fiR0zwvBL9L8QhtT8J5GpA-_4ZRIe67nVn_AyAEuSWsMyvuZDwMul8mzTuemXAhVwAZCEzSqpwF_5EDv2fqg5IMN1SV0wzuKElRYldl3UdG1mi66cWRfF6GjZl1uLVL-zu35OvlQPqZhkjn1ziKc4u7YogZESsrNS402p4K0w8BpKteV5sKQ2UAb4vwkyZAMkbVk87zIVL6ZLBP_hxYjJvqDwPbju_ykq9bETYkgkBa7-PJ8tTcRR9JSDlpS7nK16UFAQ9lqPvd-yxy0zFKlMuolMSt2sH193_YwKwK6sk38MFNipqylCLbDKuk4fK6LaPLSaOVYZwcgq0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
تاجرنیا، سرپرست مدیرعاملی استقلال: ترجیح می‌دهم به خاطر بازی حساس مقابل تراکتور فعلا درباره مسائل قهرمانی فصل‌گذشته سکوت کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107462" target="_blank">📅 00:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107461">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe4b115fa.mp4?token=mEFCwD9NvZLGO0XesPi_eowSiAoq1-tqalG2pKHKkgKAcKuypNu00J0MmOkYElCUK7FcB9AjWmdCCUl68lVFw9emk1DqnwePI2ci8Ron7Eib3IXEJHcGC9ttbHVoCBpCFK4Se0N2_3LZJI8x-SUYPxH7krin4RxGucYI5DebwuhtOcvwxXGOdbwehsBdMJlyaZb0rtIZEl4MN_CmkpeIZUJ_pmT8tz7KnThIcEfIPndlbkgsFYLVVri6JzHSwRzgdstqbcZdX6DIkOOMqyeDs4-1Zcus6i-GhdRaemzX_jL-N6mtJT7qKnij5XZcmZo8ks2ZttQVv3-cpw0pOgUd0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe4b115fa.mp4?token=mEFCwD9NvZLGO0XesPi_eowSiAoq1-tqalG2pKHKkgKAcKuypNu00J0MmOkYElCUK7FcB9AjWmdCCUl68lVFw9emk1DqnwePI2ci8Ron7Eib3IXEJHcGC9ttbHVoCBpCFK4Se0N2_3LZJI8x-SUYPxH7krin4RxGucYI5DebwuhtOcvwxXGOdbwehsBdMJlyaZb0rtIZEl4MN_CmkpeIZUJ_pmT8tz7KnThIcEfIPndlbkgsFYLVVri6JzHSwRzgdstqbcZdX6DIkOOMqyeDs4-1Zcus6i-GhdRaemzX_jL-N6mtJT7qKnij5XZcmZo8ks2ZttQVv3-cpw0pOgUd0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
علیرضا بیرانوند: اصلا دنبال معافیت پزشکی نیستم/ دوست ندارم به خاطر پرونده سربازی من، نظام‌وظیفه روی خیلی از بازیکنان دارای معافیت پزشکی لیگ زوم کند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107461" target="_blank">📅 00:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107460">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
💵
⚪️
🔵
افشاگری عادل فردوسی‌پور از ماجرای پول گرفتن ۷۵۰ هزار دلاری فدراسیون از باشگاه استقلال، قبل از اردوی ترکیه تیم ملی بزرگسالان؛ نامه شریعتمداری به تاج برای برگرداندن پول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107460" target="_blank">📅 00:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107459">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/373e4ffb08.mp4?token=Qw7qcCqUpgATGIaa8Uo47Kw66SURPWbVoi3XDZrIolyIBW-42b7H0nlczTs0G6cRF3aR0LO_uCtDOl8lLtLD_ESKhs8mCXzIqZrgRRdJTu-Mly6o30eURVn0tGSJnQ1ymBI8C6KVZKbUqkWAD_8dwjvr9i8WLKReztSN55Z9YPGTB9Nh0KxsJDWhiInVOK08c1rblK2m_kM8ThAM9WZeWIuy87vI2Vv44v6x7C3BXhRDMx43OhHKfDDiTGhAzu7GLTRXJ7-mmwasDQfiSEyPeKPULQQcEiofbC26snkhulOA0IX7KqbyiGKLm5A2NtiaeisK3HsS8yXrnuOy-eaRoitx2L4xbkZIlLavygx_nVnBcO07ZiKGHsA4Rwm0WILKUomTtZ62Z2J8_61wSppGz_1ycJ7SOrnt7eDr5-zJYq3fsFjNPvXlFkaXPPWVfyTlnlOOK5WYGzLCYKm_-sgUdzKPCx_N7AUXKoj2LZ7CmO_gI56VoUq23ydGR4woo0pOY9UxHOOCgHKL72uJiH8PpIBA9ESFE4VBGnVWstSwZdX5IbQpdfUXEKiSwDg3llYoun7hHPpMN5x_JErONW5Abzmf7OjYyAHwk9j6lCWmYXqfcNEHHpp-e4G-lxYwBnZcCZvCXAZhV4vrZmIIEhX5xNmJTP5Qrt0Vd1nZa-1kpv8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/373e4ffb08.mp4?token=Qw7qcCqUpgATGIaa8Uo47Kw66SURPWbVoi3XDZrIolyIBW-42b7H0nlczTs0G6cRF3aR0LO_uCtDOl8lLtLD_ESKhs8mCXzIqZrgRRdJTu-Mly6o30eURVn0tGSJnQ1ymBI8C6KVZKbUqkWAD_8dwjvr9i8WLKReztSN55Z9YPGTB9Nh0KxsJDWhiInVOK08c1rblK2m_kM8ThAM9WZeWIuy87vI2Vv44v6x7C3BXhRDMx43OhHKfDDiTGhAzu7GLTRXJ7-mmwasDQfiSEyPeKPULQQcEiofbC26snkhulOA0IX7KqbyiGKLm5A2NtiaeisK3HsS8yXrnuOy-eaRoitx2L4xbkZIlLavygx_nVnBcO07ZiKGHsA4Rwm0WILKUomTtZ62Z2J8_61wSppGz_1ycJ7SOrnt7eDr5-zJYq3fsFjNPvXlFkaXPPWVfyTlnlOOK5WYGzLCYKm_-sgUdzKPCx_N7AUXKoj2LZ7CmO_gI56VoUq23ydGR4woo0pOY9UxHOOCgHKL72uJiH8PpIBA9ESFE4VBGnVWstSwZdX5IbQpdfUXEKiSwDg3llYoun7hHPpMN5x_JErONW5Abzmf7OjYyAHwk9j6lCWmYXqfcNEHHpp-e4G-lxYwBnZcCZvCXAZhV4vrZmIIEhX5xNmJTP5Qrt0Vd1nZa-1kpv8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
توضیحات میثاقی درباره شکایت اندونگ و کاریله از باشگاه استقلال
⚪️
محمدحسین میثاقی: در این هلدینگ خلیج فارس یک نفر نیست بپرسد که اندونگ کجاست؟ چه کسی قرارداد کاریله را امضا کرد؟ آقای تاجرنیا الان وقت آن است که مطب و آپارتمان خودت را بفروشی تا سهم خودت از این اشتباه را پرداخت کنی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107459" target="_blank">📅 00:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107458">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ed66f5dc3.mp4?token=irWFA2yx66bsWYsO1pmPq_cR_YxoafZLXGQhfsUAovAz0FlWl071PdTi3UYhtFRKorj0yAmBQyWhgItHwqcZadJCzo29rO-eDJMQf6rjQxcVd2TcRvw-DdaqTnBvQSUBQZ9JumZ_lWgzu8SJ4E8SXZ9prNgU4NjSpxI1GnjMmf8AUfzN3_mzqHkUWVwY4FbvIBT3cBR60CL7UvQw_uAkN18VAHvZXWc5i8z2zz4lpsz2IcMUbABekxHbqRPO2-yQuiaCkQwMUJVnV_vIUo9E2Av6WlT8VUpi18p6JO1ZytoBJMMarcVZUEL3rHa7RItKDbgngLhYhJ401FY6Sys0XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ed66f5dc3.mp4?token=irWFA2yx66bsWYsO1pmPq_cR_YxoafZLXGQhfsUAovAz0FlWl071PdTi3UYhtFRKorj0yAmBQyWhgItHwqcZadJCzo29rO-eDJMQf6rjQxcVd2TcRvw-DdaqTnBvQSUBQZ9JumZ_lWgzu8SJ4E8SXZ9prNgU4NjSpxI1GnjMmf8AUfzN3_mzqHkUWVwY4FbvIBT3cBR60CL7UvQw_uAkN18VAHvZXWc5i8z2zz4lpsz2IcMUbABekxHbqRPO2-yQuiaCkQwMUJVnV_vIUo9E2Av6WlT8VUpi18p6JO1ZytoBJMMarcVZUEL3rHa7RItKDbgngLhYhJ401FY6Sys0XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
⚽️
خوشحالی فوق‌العاده زیدان پس از گل پیروزی بخش فرانسه مقابل بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107458" target="_blank">📅 00:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107457">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3190d23c56.mp4?token=Sg2FgvBk5gwJKZwPEMsNoPdJIDcnAus-xbuzboI6rxFn02J1f4GDQyQdP9BOzLf4Z8R56dfSFGizxkscjAw5dvzxnLwJLzZ7-z2-T6KMHLhjZ9URrhAsi5lweSZtpt8BI3gvI98iHK4PfI4RdaUy0RIDtyw0oX3H4rMC98ju6XmLUsnIWOz_HVPrJSv-8aonkEyeb4gF6aNBCHdJjpsLNiMM6IBUoSikkxZaoSnUYFY9N81SGSjT-s3MrRdU1l8DaCtE6XgkuLxPNgJMKuF7j7kQKGC2Wk0ElDi1GfivnOBlIvt4yrU4SS9IDNRrKdx85kSmjYh_Kf_lIcisvwPCbjqFQAzyN9cTNlqX3fyQFD2p0mWXYwM5i0gv_8fa4LZGp6snTmrQibN4YE40YfC-9bapgTRzzzsquQb4h-_SxcmLr2trwiLeoXaySibc5O9Dv28eOd7-LDEx1WK-yBlNj4rGTJ88bosdFkzKdluyNhERTBfmlX0BpatGYACkSdnghFGO8kY9sMQesTr74-00IDB50mhWavs9QCKnzwox-XgbEOFbBgLupzFedp42l5aHYrhoAFmBB0fPWw8oaIlyajNpuSE1N6GKL-3cHGeCyFcuLZLYVwm7NaI0pFNMPFHC00CKiRyy1dfYqkF8ZNQASPX9RFjNmc1pXwzZ-tlBPcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3190d23c56.mp4?token=Sg2FgvBk5gwJKZwPEMsNoPdJIDcnAus-xbuzboI6rxFn02J1f4GDQyQdP9BOzLf4Z8R56dfSFGizxkscjAw5dvzxnLwJLzZ7-z2-T6KMHLhjZ9URrhAsi5lweSZtpt8BI3gvI98iHK4PfI4RdaUy0RIDtyw0oX3H4rMC98ju6XmLUsnIWOz_HVPrJSv-8aonkEyeb4gF6aNBCHdJjpsLNiMM6IBUoSikkxZaoSnUYFY9N81SGSjT-s3MrRdU1l8DaCtE6XgkuLxPNgJMKuF7j7kQKGC2Wk0ElDi1GfivnOBlIvt4yrU4SS9IDNRrKdx85kSmjYh_Kf_lIcisvwPCbjqFQAzyN9cTNlqX3fyQFD2p0mWXYwM5i0gv_8fa4LZGp6snTmrQibN4YE40YfC-9bapgTRzzzsquQb4h-_SxcmLr2trwiLeoXaySibc5O9Dv28eOd7-LDEx1WK-yBlNj4rGTJ88bosdFkzKdluyNhERTBfmlX0BpatGYACkSdnghFGO8kY9sMQesTr74-00IDB50mhWavs9QCKnzwox-XgbEOFbBgLupzFedp42l5aHYrhoAFmBB0fPWw8oaIlyajNpuSE1N6GKL-3cHGeCyFcuLZLYVwm7NaI0pFNMPFHC00CKiRyy1dfYqkF8ZNQASPX9RFjNmc1pXwzZ-tlBPcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇮🇷
افشاگری
باورنکردنی میثاقی از یک ایجنت، عارف آقاسی، پرسپولیس و پیش قرارداد برای یاسر آسانی!
محمد
حسین‌میثاقی: پرسپولیس به یک ایجنت ۱۰۰ هزار دلار پول داده بود که عارف آقاسی را به پرسپولیس ببرد ولی این بازیکن را به استقلال برد و الان باشگاه از این ایجنت شکایت کرده است
در همین راستا این ایجنت قرار شده است مدارکی به پرسپولیس درباره فسخ آسانی بدهد و همچنین این بازیکن به پرسپولیس ملحق شود و مذاکرات حتی تا پیش قرارداد هم جلو رفته بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107457" target="_blank">📅 00:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107456">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13b959785a.mp4?token=gdqEr6eGmy80kXMEV7dCulUNaRSfNgAPSVGp3dVcdIZHc8e5GX_DmF2MbL_3lWJYSLknwgSC2ROq4p-hkK_DcwuuHHlPNdY4OauZv2l0pkvC8uSwv_CHa8UzXcgDyMQYrYGUtfSHoeqzsNXyPZbqO7RmoJzsya_BCS3HGhmJQpPIoNAmsAz4CQ0gS69yohRFl0xnmMjruikZ0nmsiRdx67ZXVhzwBJeY4dlnqaqyxXhgeuwsrvXeK3ywocYc0m74oHskyvnnJDLZBwMiBlkg2-tD97_ywcVxodvf5xy1g7Z_nMIdbmvoTAWpaN-rehBhoa5ooYdkOsFSeb4t5z9ZFz513v9QcsddX34ZM6NIizknjoaQOfSVtBc265FnPRmTQF14EhKU47_RubXyFSlDeAFjpqZV8QQBPhvylNRtf-cNr-jGvkBSMhcYT5KTTN6OjL1mjoQe0WalZR-HqBsZmg6UYWMz4WHgHOYSsuG4DbKVp8xgD7aGaVjHvAIuq4R8vRyG6c3L2EZjZSpx5qTu7uJqzKBgTw4sVopZeNpFncMGtuKwlQZXxSnY73pwK9X1ylydmyZx9MM2LQumhHq5Tb_6G8grL1UenhQcrrx8MvMIbi49HkIR9WNyjQedR1_A5sG_evjtxM83fAlPzkZLgNEq9oBvO7vTNF4y9bUMrxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13b959785a.mp4?token=gdqEr6eGmy80kXMEV7dCulUNaRSfNgAPSVGp3dVcdIZHc8e5GX_DmF2MbL_3lWJYSLknwgSC2ROq4p-hkK_DcwuuHHlPNdY4OauZv2l0pkvC8uSwv_CHa8UzXcgDyMQYrYGUtfSHoeqzsNXyPZbqO7RmoJzsya_BCS3HGhmJQpPIoNAmsAz4CQ0gS69yohRFl0xnmMjruikZ0nmsiRdx67ZXVhzwBJeY4dlnqaqyxXhgeuwsrvXeK3ywocYc0m74oHskyvnnJDLZBwMiBlkg2-tD97_ywcVxodvf5xy1g7Z_nMIdbmvoTAWpaN-rehBhoa5ooYdkOsFSeb4t5z9ZFz513v9QcsddX34ZM6NIizknjoaQOfSVtBc265FnPRmTQF14EhKU47_RubXyFSlDeAFjpqZV8QQBPhvylNRtf-cNr-jGvkBSMhcYT5KTTN6OjL1mjoQe0WalZR-HqBsZmg6UYWMz4WHgHOYSsuG4DbKVp8xgD7aGaVjHvAIuq4R8vRyG6c3L2EZjZSpx5qTu7uJqzKBgTw4sVopZeNpFncMGtuKwlQZXxSnY73pwK9X1ylydmyZx9MM2LQumhHq5Tb_6G8grL1UenhQcrrx8MvMIbi49HkIR9WNyjQedR1_A5sG_evjtxM83fAlPzkZLgNEq9oBvO7vTNF4y9bUMrxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇫🇷
گل‌تماشایی مایکل‌اولیسه مقابل بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107456" target="_blank">📅 00:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107455">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aba31d6094.mp4?token=voCJq5mh83FVfUMl5zgq48vCJorUxlVN_S0uhfsSs4nTgcHhGdne7C8Naspd0ggS9WMcHeteNfvPI1EFaEv7LoF3vjkfKFgOaw-NOeSU3t--smqhlxnjUDqUC8X3ZrLr06WTA8l5hz6SMQckld0dWpeD7PDY1SlOzosiybxDecPM319kl9qfg-zx2kg72ek2528shukO7RdsVdOPoQ0WM0OjnFE4ZYcLifx0_AcatmfpbNNWD7U-bE5m-ynA_Oz1LjRW8mlzF9r81EVsTMKGG4usG12f630a3bxaDqnKkOZKN4Ib1UazpQnNgMRSGJMbNsitajLZdpVNIlkYbcLCew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aba31d6094.mp4?token=voCJq5mh83FVfUMl5zgq48vCJorUxlVN_S0uhfsSs4nTgcHhGdne7C8Naspd0ggS9WMcHeteNfvPI1EFaEv7LoF3vjkfKFgOaw-NOeSU3t--smqhlxnjUDqUC8X3ZrLr06WTA8l5hz6SMQckld0dWpeD7PDY1SlOzosiybxDecPM319kl9qfg-zx2kg72ek2528shukO7RdsVdOPoQ0WM0OjnFE4ZYcLifx0_AcatmfpbNNWD7U-bE5m-ynA_Oz1LjRW8mlzF9r81EVsTMKGG4usG12f630a3bxaDqnKkOZKN4Ib1UazpQnNgMRSGJMbNsitajLZdpVNIlkYbcLCew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
‼️
امیرمهدی ژوله جایگزین ابوطالب حسینی شد و برنامه فان فوتبال 360 رو اجرا خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107455" target="_blank">📅 00:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107454">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9beb68432a.mp4?token=t0vpzMlgRFN-rybwtDCGs0mQEWPEDv_K50AtTPOl8vzfqdenp1xFv-i9WXKdPatmnbo7tI6Vyqt_Bu_PQMLuJNEOdVx7d-GPI3-oQ-ggtUbV2l3yIHRxPVMLxluisJRU8BFjPysmzOCsGWtSL7_m7siff2Drugz_srRTZDEA4K6e7HwcD8W7qa2tpQDa_79qKADVwYxwTUv_MqJwhe2i2u_Tb_pb-e05WChFFba8J9SklAWlTL0lYHVCsDQ6eJaN12JzLdn64DYjCzC-kxmloqn93kPfpLUI8vz7qczLYZMyTOy47S6Gx2eDIqjjVKguyI--E0G9baGASqoBEQ6PPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9beb68432a.mp4?token=t0vpzMlgRFN-rybwtDCGs0mQEWPEDv_K50AtTPOl8vzfqdenp1xFv-i9WXKdPatmnbo7tI6Vyqt_Bu_PQMLuJNEOdVx7d-GPI3-oQ-ggtUbV2l3yIHRxPVMLxluisJRU8BFjPysmzOCsGWtSL7_m7siff2Drugz_srRTZDEA4K6e7HwcD8W7qa2tpQDa_79qKADVwYxwTUv_MqJwhe2i2u_Tb_pb-e05WChFFba8J9SklAWlTL0lYHVCsDQ6eJaN12JzLdn64DYjCzC-kxmloqn93kPfpLUI8vz7qczLYZMyTOy47S6Gx2eDIqjjVKguyI--E0G9baGASqoBEQ6PPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
‼️
سوتی سمی عادل فردوسی‌پور و ریختن لیوان آب روی میز که با خنده‌های آسانی همراه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107454" target="_blank">📅 23:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107453">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5937fb4be6.mp4?token=WNxariIQuzilP3LpL_b-Ey7dCdG_qFEMPX50Fwpaq7cD0SIYdikkAJkKrruQxAjp6VtjVA42IrDlkNwWA9wdHrEAdpli2SWlrZc2fiQnfb4ry7hzgq06kIMDQEnkCHfstWFIpSpZxaV5ga8_A0DJkdZIsmMqpxQbwFWt3bm-CpmCy4Pb8yA5ERxTmFkU6aJ_JcDkUtDsJggOPK-XGzUCvA5qG9Yf4YChq5xNoJcJ_iNr-lR-YubLN1oGREQBEanaXacQayhzaAypFFW1guVpVZL5LjTEoEQ06uO9CIJiCfj34GejZ2MTIWmM9j_aM0n3JbzCVWvfvagCvmwrmN6gFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5937fb4be6.mp4?token=WNxariIQuzilP3LpL_b-Ey7dCdG_qFEMPX50Fwpaq7cD0SIYdikkAJkKrruQxAjp6VtjVA42IrDlkNwWA9wdHrEAdpli2SWlrZc2fiQnfb4ry7hzgq06kIMDQEnkCHfstWFIpSpZxaV5ga8_A0DJkdZIsmMqpxQbwFWt3bm-CpmCy4Pb8yA5ERxTmFkU6aJ_JcDkUtDsJggOPK-XGzUCvA5qG9Yf4YChq5xNoJcJ_iNr-lR-YubLN1oGREQBEanaXacQayhzaAypFFW1guVpVZL5LjTEoEQ06uO9CIJiCfj34GejZ2MTIWmM9j_aM0n3JbzCVWvfvagCvmwrmN6gFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
سردار آزمون: دیروز به زنوزی زنگ زدم و گفتم یه وقت نکند من را گردن نگیری/ انتخابم برای بازی در ایران تراکتور است مگر اینکه خودشان نخواهند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107453" target="_blank">📅 23:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107452">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07eddda0fb.mp4?token=efkRMM9veafsnCYIOUQjSuyas-aB4AkOoGiKt5FYzS91BsFJrlocGeVIp8TaGihoQgvw690e-o4HllDDIf5NnzddXS7twUTtosvo1p8bdwixF3NUFfH8K1t_GEpFHhUD786mKOevGso8bGm0Ft9_G-amx5ehtGsXyV-j4RxsXhxI4XofD8CdRpwRErj7PqF1KdShCfQKbkNDayr350tG99hBV-SAr21VxZgYSf9KqR08d3PyO7e5D7b5MZMrRHBrrtr2Xj9bBz1d9GEOnw1Q-QvdviKChNN4m0pMnihAWnBiixG7EjB1B8tbkDNetwDrxKioG9I500prispUSWxQZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07eddda0fb.mp4?token=efkRMM9veafsnCYIOUQjSuyas-aB4AkOoGiKt5FYzS91BsFJrlocGeVIp8TaGihoQgvw690e-o4HllDDIf5NnzddXS7twUTtosvo1p8bdwixF3NUFfH8K1t_GEpFHhUD786mKOevGso8bGm0Ft9_G-amx5ehtGsXyV-j4RxsXhxI4XofD8CdRpwRErj7PqF1KdShCfQKbkNDayr350tG99hBV-SAr21VxZgYSf9KqR08d3PyO7e5D7b5MZMrRHBrrtr2Xj9bBz1d9GEOnw1Q-QvdviKChNN4m0pMnihAWnBiixG7EjB1B8tbkDNetwDrxKioG9I500prispUSWxQZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شوخی‌های سردار آزمون با بیرانوند درمورد رنگ مو و سربازی‌اش
🟠
همسر بیرانوند باز برایش حنا گذاشته ولی اصلا بهش نمیاد. یکی اکرم خانم (همسرش) و یکی اکرم عفیف او را در زندگی بدبخت کرده‌اند!
🟠
خدا کند علی در فجر مویش را نزند...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107452" target="_blank">📅 23:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107451">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✔️
جنس متفاوت غافلگیرکردن یاسر آسانی!
👍
🇮🇷
خوش‌قلب و خیرخواه، مثل ستاره آلبانیایی استقلال؛ وقتی یاسر تصمیم گرفت برای اعضای نیازمند باشگاه، موتور و خانه تهیه کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107451" target="_blank">📅 22:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107450">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‼️
از ختافه، ژاپن و عربستان پیشنهاد داشتم
🇮🇷
واکنش آسانی به پیشنهادهایی که بعد از فصل اولش در جمع استقلالی‌ها دریافت کرد؛ بهشان گفتم فقط وقتی پیشنهاد استقلال آمد به من زنگ بزنید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107450" target="_blank">📅 22:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107449">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‼️
درباره رامین با ساپینتو حرف زدم؛ گفت برش می‌گردونم!
صحبت‌های یاسر آسانی درباره رابطه‌اش با رضاییان، اتفاقات جنجالی بعد از بازی با الوصل و پادرمیانی بین او و سرمربی سابق!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107449" target="_blank">📅 22:36 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107448">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🎙
🇮🇷
توضیح آسانی درباره تکنیک‌های کری خواندن، از بازی مقابل پادیاب تا داربی برابر پرسپولیس!/ در استقلال، از تمام لحظات لذت می‌برم و خیلی خوشحالم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107448" target="_blank">📅 22:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107447">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/133f025096.mp4?token=iUg6fKJLH3JWHhxRLbMxXdmcx_6-nZnuX3MH7ARVMD5PQEjcwBMtM6sSkceHsn1A1f6-BVznJWAKJBYk2W1oVrAS9sP2EJi77WmueJwVq3yFZPC8DnPSbVpaIta8v3Rw7KxPGxQnnanCrE5VLkEANjtJQXsc3Vjl1Qf1ntOK0HyFgcKM14RUpjobaZ-L9GH5Dy_nr3aSBkFm5Kh-D5s2fG20XLuSsOKsf3GtiTguCtveEp-rWxYB4pZHcg8CNFUNH14abV-XdjAHpG7W8iShiTdtvkNhbWIMBxoCoAZ3Z5T8Sc15dFP8R1YLcBpBr2n9wU9s2YJvXX_g7JAVh8yj4L8kik-xTXw4dYb-7O42yxSWJ7cY5RsiVXXfbwJRNiWQZyK7ia_o7sLKCEDBA0ai8016T_fjHLXsVwfiQ6IMLyJ11C291WepVLyAHXYM-Ho9YiHmYz_6wpb98cuFMjHQsxcYmrYs2nzzhyEjHZq5L5SxV3zegQ5Lj8HxlESsS1s34vAGvOCOUU9sIRGotr0M70ujuKf_i22XMDqhrzjiQIpWV-ma3SZKBJ_8H65QnfhzEBmCqSqyvd9akrgXxH5jiHkk94HMxcp_2TQa17ZjkHGM2m-M6PJ8CKhYbhS7NgxV-wWPCLJIQo4sar4uzt9sFtH2A3pV3wuGk5je57FyUQs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/133f025096.mp4?token=iUg6fKJLH3JWHhxRLbMxXdmcx_6-nZnuX3MH7ARVMD5PQEjcwBMtM6sSkceHsn1A1f6-BVznJWAKJBYk2W1oVrAS9sP2EJi77WmueJwVq3yFZPC8DnPSbVpaIta8v3Rw7KxPGxQnnanCrE5VLkEANjtJQXsc3Vjl1Qf1ntOK0HyFgcKM14RUpjobaZ-L9GH5Dy_nr3aSBkFm5Kh-D5s2fG20XLuSsOKsf3GtiTguCtveEp-rWxYB4pZHcg8CNFUNH14abV-XdjAHpG7W8iShiTdtvkNhbWIMBxoCoAZ3Z5T8Sc15dFP8R1YLcBpBr2n9wU9s2YJvXX_g7JAVh8yj4L8kik-xTXw4dYb-7O42yxSWJ7cY5RsiVXXfbwJRNiWQZyK7ia_o7sLKCEDBA0ai8016T_fjHLXsVwfiQ6IMLyJ11C291WepVLyAHXYM-Ho9YiHmYz_6wpb98cuFMjHQsxcYmrYs2nzzhyEjHZq5L5SxV3zegQ5Lj8HxlESsS1s34vAGvOCOUU9sIRGotr0M70ujuKf_i22XMDqhrzjiQIpWV-ma3SZKBJ_8H65QnfhzEBmCqSqyvd9akrgXxH5jiHkk94HMxcp_2TQa17ZjkHGM2m-M6PJ8CKhYbhS7NgxV-wWPCLJIQo4sar4uzt9sFtH2A3pV3wuGk5je57FyUQs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
گفت‌‌وگو با یاسر آسانی، درباره واکنش عجیبش به دعوت‌نشدن به تیم ملی آلبانی: حالا می‌توانم برای استقلال بهترین بازی‌هایم را انجام دهم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107447" target="_blank">📅 22:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107446">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1d5953f9f.mp4?token=D6m9Nx7uX28I6H0DPhzVoVNTF7lsvmclDNM1_rFtUABWvp0h-r77ZOmGIWtSPrsOBq252snx__kunob4VI3x_Ip_iOwlk5DVeyR_i8RSLCai6H8_VBCMdQRtWGrv94qdnDDWXEZyNWevJAqAmTGonvQuuBg04mM0lhPhL7EyPwKQBM7IvQKo4jT6IN2u693G4o1p_tPyE77x5ZQAzsuSFSG8NXInqdrLMXdVWAhS355Zr3oFdv2xxxqKD6Fn4zcaNENH08rxoTa6WDiM3SLVKbcTYNtWUJjda9JdxdrnGYgXDPDV4UkVtAX-SymGP7C1sO3HXQC9Oqf_M9cTPx1AHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1d5953f9f.mp4?token=D6m9Nx7uX28I6H0DPhzVoVNTF7lsvmclDNM1_rFtUABWvp0h-r77ZOmGIWtSPrsOBq252snx__kunob4VI3x_Ip_iOwlk5DVeyR_i8RSLCai6H8_VBCMdQRtWGrv94qdnDDWXEZyNWevJAqAmTGonvQuuBg04mM0lhPhL7EyPwKQBM7IvQKo4jT6IN2u693G4o1p_tPyE77x5ZQAzsuSFSG8NXInqdrLMXdVWAhS355Zr3oFdv2xxxqKD6Fn4zcaNENH08rxoTa6WDiM3SLVKbcTYNtWUJjda9JdxdrnGYgXDPDV4UkVtAX-SymGP7C1sO3HXQC9Oqf_M9cTPx1AHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
حسین‌
عبدی: رفتن به المپیک ربطی به سرمربی ندارد!
‼️
خیابانی: پس گواردیولا هم بیاید همین است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107446" target="_blank">📅 21:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107445">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uysxGBWmO2YOjkEN8dWtoDaKaCCu79b5mZtj_xZvNhq2A89B-K6gzLjNLr1rQK-zgDXpNSgEvuau4ScKcc_R2XHXuepOGQ_HQQ-wLIiz5V_WbuPfQUchYYnfMraEqZkWHR6VaFFoyFmdlWyMClGm8g_4A9tTcqw27AJ8rWRLCTy8cnci6192GRoWUNC5U_2RVrqR_opAR26sCh9-ZrUBh7oQz684-odlFun2wHNlPADNnuen31_tNuOzs7g4SYpOGedPCRZbLIT_sC6dq7HCGUyFCiTR_i6nNaw6ZUpnOgffNuYDScdOlc2vKrB_fuY0KgpaUK7itHqzyGrpvQpEaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
یاسر‌آسانی تا دقایقی‌دیگر با حضور در برنامه عادل فردوسی‌پور با وی مصاحبه خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107445" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107444">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0794b34067.mp4?token=WduRxH_Ak24JfZsTd84gDJ6oyNcA6y9bpbYcvOZgePFUk7wusm1NZ6QtKR1yI7asKqPIr2nkBKuRDoni9LdI-s_ylBpbnef2aXbm2XM1cdMlwMa67rrTBsCg0YBf_xG_tu6-bsgsWdrUhsVwKG_soxAHZ2njNS-4qoLUYPa2wRfLAZE18JOxkjJBbIDjdrEdD9WG8FY_wMaD8lV7HisPIVhUqmw9uyX20vp6TszTFNOO4XzipJWn0jV_KJ70Q9f2kbfh09RtJLXbGPnzISYKFNzyckUNDxXB5PJ7ag4wk2dMk1IX5ChqMSIwYhGFMDFIfe_-WAl3Tw-b2AU4NJJXfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0794b34067.mp4?token=WduRxH_Ak24JfZsTd84gDJ6oyNcA6y9bpbYcvOZgePFUk7wusm1NZ6QtKR1yI7asKqPIr2nkBKuRDoni9LdI-s_ylBpbnef2aXbm2XM1cdMlwMa67rrTBsCg0YBf_xG_tu6-bsgsWdrUhsVwKG_soxAHZ2njNS-4qoLUYPa2wRfLAZE18JOxkjJBbIDjdrEdD9WG8FY_wMaD8lV7HisPIVhUqmw9uyX20vp6TszTFNOO4XzipJWn0jV_KJ70Q9f2kbfh09RtJLXbGPnzISYKFNzyckUNDxXB5PJ7ag4wk2dMk1IX5ChqMSIwYhGFMDFIfe_-WAl3Tw-b2AU4NJJXfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
مطابق گزارش خبرنگار شبکه الحدث در پاکستان، به گفته منابع، ایران با توقف فعالیت‌های غنی‌سازی موافقت کرده است، در ازای آن، تحریم‌های ایالات متحده علیه ایران کاهش خواهد یافت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107444" target="_blank">📅 21:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107442">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pL4eLpqewipl27sl28kLfiMussXa0LDkjYwKuDPz-y4W8qH8bef8jvSWxe5ipcOjUlfYHlUR9Rh7qMXfJSMhXGcvP2wwIcziKTCMU57G62opJ2PBcpiKeseiOYhVqIx-14Dqs3nJPO8iK6Pp6C9EDVtpkSDAm1z3AKhwQokbMcwRFanay4M7TIz4-I6Kj0O2BJfRzslqZ-S-hZNC7v-JWf3tB85uB6BqQIy4PcKU6h6JsVTm9zjyHrMSdyTu1ozhqzGhUEjqyJliZYB7jL8Hyp_Dy6Da0TWLoeDCNsuH79CqRTp9aieGZ2tCZaMtNrwJ8RJDTaoZxLL5icm4NX665A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UxvBSEQf3jIveGQLgLy8jVq3ioSz9M7RRhr0AjKJnWgJImumj7LeTJsVhsE1P-J6ErJrrUDxXanM2nj-MQpDjvtErNMnShB4YJoGUok3RvM5MQcxsP_Rd1cUg4hIyBg8YLyjbAz7anUBxIkHC8guNTUrYk126WvEnDWXAJu6ht3fWUh-j0EAR78_h8LhG2Um_F7miW7v_6OBL5dAuLW1UHzrpq7RmG6Mc_ub2P7xKu5_zDuoREaeI8RW1gd5_6d52FP7NKdzyc6pTFh_G4kOAaBJKomZm3YXO1UOPE0jrmSj2b3U0EA3FVxA9iXGIOPhEckw1E-fGdzK8G5QOV0YYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇫🇷
🇧🇪
ترکیب‌تیم‌های بلژیک x فرانسه
ساعت 22:15
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107442" target="_blank">📅 21:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107441">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
🇮🇷
🇮🇷
على تاجرنيا : از هواداران پرسپولیس گله دارم و ناراحتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107441" target="_blank">📅 20:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107440">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd0094f85.mp4?token=sl9aAROWE7fZLvltSFartBg0VN2P019o_REmqqT-FP9r6sKepvSF656T-LvySVVUVwgFu9fLTNZPJxmCaKw0JMHnybXCvv9Mrz8YrorQubrWjJv1TA0N1lwqpredU9aMy-A1R9w50rLHOQ4yHv9C3Ao4e_aSE8xOHXCEiVFC1LtOjxwUAGBiNSU-z7MDshxx43p-mtppwwmUumI1NghCRNpV0KWz-Z-J7kcjykaSAxIu5XnGpcmX9qtHYr2uiGXPrCLCjQMz-UvdL9MqmrHys8wNqtl-ZBTnkp8BJD9-u30fEFmvfhqorePx9aLfPilhldU_nN34Zy0vkNXhQWSFKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd0094f85.mp4?token=sl9aAROWE7fZLvltSFartBg0VN2P019o_REmqqT-FP9r6sKepvSF656T-LvySVVUVwgFu9fLTNZPJxmCaKw0JMHnybXCvv9Mrz8YrorQubrWjJv1TA0N1lwqpredU9aMy-A1R9w50rLHOQ4yHv9C3Ao4e_aSE8xOHXCEiVFC1LtOjxwUAGBiNSU-z7MDshxx43p-mtppwwmUumI1NghCRNpV0KWz-Z-J7kcjykaSAxIu5XnGpcmX9qtHYr2uiGXPrCLCjQMz-UvdL9MqmrHys8wNqtl-ZBTnkp8BJD9-u30fEFmvfhqorePx9aLfPilhldU_nN34Zy0vkNXhQWSFKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
کنایه مجری تلویزیون به زنوزی: باید از هواداران استقلال عذرخواهی کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107440" target="_blank">📅 20:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107439">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd102e93c.mp4?token=JE_nWkIp487ORsN8UnoWg1tuwaooHaVhAbT-fEBUh8dXJy3GuAMCQDwSVYKg3a7a1XW3c0hbPg4IkyQWEgS4kHtTpK3LyZ6b-wGAWlyhss1rXVAV_VC_42mJebpGjNKkFjCOxnZzY-4payRoQBjrOzaW-A9s2y8MT8c2G8mY_iN2DZ8NL3bzy4iG9wIu9JSWhCgliDRzr6e6RzDx8wTAyA5ugfO2Er16AlmwkHYtZI76SecgOZlhF4xZ71kcTO_namHPodsCpueafxKkkzu7FKpFAlPVe3S07uOxGCxosuYMG4uzyhgD7yhroFbuJkA27GJzj93zgHT8boV31NUL4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd102e93c.mp4?token=JE_nWkIp487ORsN8UnoWg1tuwaooHaVhAbT-fEBUh8dXJy3GuAMCQDwSVYKg3a7a1XW3c0hbPg4IkyQWEgS4kHtTpK3LyZ6b-wGAWlyhss1rXVAV_VC_42mJebpGjNKkFjCOxnZzY-4payRoQBjrOzaW-A9s2y8MT8c2G8mY_iN2DZ8NL3bzy4iG9wIu9JSWhCgliDRzr6e6RzDx8wTAyA5ugfO2Er16AlmwkHYtZI76SecgOZlhF4xZ71kcTO_namHPodsCpueafxKkkzu7FKpFAlPVe3S07uOxGCxosuYMG4uzyhgD7yhroFbuJkA27GJzj93zgHT8boV31NUL4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
📱
یامال دیوث اومده از عرق زیر بغل نیکو ویلیامز استوری گرفته و مسخرش میکنه
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107439" target="_blank">📅 19:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107438">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee7cdbb4e.mp4?token=LWJOqZ0vzKgx7Rna2mPXacRNVm5ZY3xohw2F0T9erk0T-m3XbXAgRaud6jdkwwrjj8Li0DVVGOfTD2rCBQ7bcgqqab0ugJplVZJDmanV9kWe9k-6Sz2ChB8Bvr7We95GUPqexggjZi0JLHHASjYTxJvgaqnHxY_GwXLe6bt4Sam7H3AtB8xloLBEdeO0mpx9ZX30TCHyfRLsvRyvlXMdzyBpbFr7PQQaF_9VPA6tgi5EZGsIHmlH9Krt1HuNmwbgZJXnzIUxNDqNJo9WzEhki7BVx5X9kUnL9n70FZj2I1wDOuRSbwt1LZwMUPQxt1oDEGhQ4duVHAciL3DPJbj_qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee7cdbb4e.mp4?token=LWJOqZ0vzKgx7Rna2mPXacRNVm5ZY3xohw2F0T9erk0T-m3XbXAgRaud6jdkwwrjj8Li0DVVGOfTD2rCBQ7bcgqqab0ugJplVZJDmanV9kWe9k-6Sz2ChB8Bvr7We95GUPqexggjZi0JLHHASjYTxJvgaqnHxY_GwXLe6bt4Sam7H3AtB8xloLBEdeO0mpx9ZX30TCHyfRLsvRyvlXMdzyBpbFr7PQQaF_9VPA6tgi5EZGsIHmlH9Krt1HuNmwbgZJXnzIUxNDqNJo9WzEhki7BVx5X9kUnL9n70FZj2I1wDOuRSbwt1LZwMUPQxt1oDEGhQ4duVHAciL3DPJbj_qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇮🇷
❌
فرزین دبیری عضو هیات رییسه فدراسیون فوتبال : علی تاجرنیا به اعضای هیات‌رییسه نامه زده که جام فصل گذشته به استقلال اهدا شود اما هنوز هیچ‌چیز قطعی نشده و هیچ کس هم به تاجرنیا قولی نداده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107438" target="_blank">📅 19:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107437">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vA3RfyQEIMreHFMmZLp9dSTAjJeP4OnXKqvWjvjjei2DqZWRgr27q3NxqM8m__qT3pI3bcpFIDjQyWuibns9OJJcDkz-goIE_9o_Mj3mVJAOj2IqvFTooRCfq_KJosjQTF8-0uBUF6u0E2zQ1zeThYKchS4DQ1gCeavVPEh9YtsEfL263ve5tV6uape0lHc0m0CDyRm63Ln0yX83MiH2a7Wc5mjI1PLFCtriJsJvuRlCAsCM4Njhr-EI53OGpN3bK5zeKskbV6IS_xU2774yVyDEupz74tEj5WlMF1YTImHofIwrXkiHgBSXnYJjYaxLsQEVe5QYhGcrEhd50y0cuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
افشین‌قطبی، پیروز قربانی و رسول خطیبی سه گزینه نهایی فدراسیون فوتبال برای سرمربیگری تیم‌ملی امید هستند که بزودی یک نفر معرفی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107437" target="_blank">📅 19:23 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107436">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0d622742.mp4?token=hvGmq0wHg5iEv6GeMaHEd1O4T8RqOIXEMDUed9IRTv_-HRRcZ9m_IfT7Ir7ybb3-umBqMd5aW6Kmm-Lr_1KtjQV7IkXwATu7ckM4fpb-IaawgVKQq2uV5QUmGPaSYnjisU5NDhVy-zZJdBWR5aycDo1aEIYcPY-a1U1rVS8TxIkKCe08i2ng9s0Is710f5wfCc7vAEWn76ei37FO8NlM3E29gi7bSNNchJfICGVyy1AHM4xjR8Zhwq5_o-HL5JaE-XFcCWrM553kuNn6xMEk51p3NkV2kPTzOZA765Eb8_La9hXogJ2D4ep8Mpfr3MBrGsG93fKhPp3O9GfKXnkHf4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0d622742.mp4?token=hvGmq0wHg5iEv6GeMaHEd1O4T8RqOIXEMDUed9IRTv_-HRRcZ9m_IfT7Ir7ybb3-umBqMd5aW6Kmm-Lr_1KtjQV7IkXwATu7ckM4fpb-IaawgVKQq2uV5QUmGPaSYnjisU5NDhVy-zZJdBWR5aycDo1aEIYcPY-a1U1rVS8TxIkKCe08i2ng9s0Is710f5wfCc7vAEWn76ei37FO8NlM3E29gi7bSNNchJfICGVyy1AHM4xjR8Zhwq5_o-HL5JaE-XFcCWrM553kuNn6xMEk51p3NkV2kPTzOZA765Eb8_La9hXogJ2D4ep8Mpfr3MBrGsG93fKhPp3O9GfKXnkHf4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
👍
ویدیو‌دیدنی از حرکات بانوی ژیمناستیک ایران در بازی‌های آسیایی که حسابی وایرال شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107436" target="_blank">📅 19:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107435">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2iFtxahzISBygrYbUBVgUc50GhHDYjK2HF6JtoXESOandB2Rz-D_nWbrDZKl0Lr7MMRcZ3CqEbvnNIUynSJtg-JJNze0g2ScMsdNMDJUn_xSOUxlAYpUnpKHuwdC6N44FioK3hPJEnZVNc-9eFdi0bz1Nnh0GgiAWGVy-ymSZSePmoFUH5hp0rpsk636-fHrd8zfCw1-xPhs7mM9yFgqhMKisPLmqee-KC1YM_WNC_kWNlNBbp2hqD6CFpFnZiMQrrbg8ZQ0-QitvCOwii5bjG_Wr7y_L1wUQ1ZG2EX6Jlvr39aRUME-YxCIS_e0YOU8rTwtoL_0hOmH9wuEPu7RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
دوایت باکس، گارد باتجربه آمریکایی، با تیم بسکتبال استقلال پیوست. این بازیکن آمریکای سابقه حضور در NBA تورنتو رپتورز، لس‌آنجلس لیکرز و دیترویت پیستونز را دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107435" target="_blank">📅 18:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107434">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3874fb3e78.mp4?token=E_a69lC4Hc_HsK2KP3KsUmRcSbe5ek-DeMY9_20bUqJ3HanuVouxsIfTY4gdJFPvLlDkMXtwIV8x7Au5NCaXy_YqLKJ5mgP972Xe_uBEviJqJq-fH-r_In_rjSyOue7HfSlyIXuuUE0OFOfCjEx2pKDEcDpWyvxoCQyVrJjivqDsZXp4p2rf-GHng35S5WmLfUNgVNmfwnqWWUt2GaER3D9FV7SiHFxDm8On4SmQGFnPdNGA-f_EyqLTLSK69R3rjjTTL2nArrY2ilJr9ky5BkJ44nRMbjoHp7L-RfGnIanhQekpbt74Gx6rPnraxvUpMK9gQk9pIoFHeBnhbWQ2Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3874fb3e78.mp4?token=E_a69lC4Hc_HsK2KP3KsUmRcSbe5ek-DeMY9_20bUqJ3HanuVouxsIfTY4gdJFPvLlDkMXtwIV8x7Au5NCaXy_YqLKJ5mgP972Xe_uBEviJqJq-fH-r_In_rjSyOue7HfSlyIXuuUE0OFOfCjEx2pKDEcDpWyvxoCQyVrJjivqDsZXp4p2rf-GHng35S5WmLfUNgVNmfwnqWWUt2GaER3D9FV7SiHFxDm8On4SmQGFnPdNGA-f_EyqLTLSK69R3rjjTTL2nArrY2ilJr9ky5BkJ44nRMbjoHp7L-RfGnIanhQekpbt74Gx6rPnraxvUpMK9gQk9pIoFHeBnhbWQ2Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
تاجرنيا: خیلی ها من را سرزنش کردن که چرا موضع علیه سه جانبه نگرفتیم اما در نهایت دیدید که چه افتضاحی برایشان رقم خورد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107434" target="_blank">📅 18:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107433">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbe27Nt5OQdlYLPVwgOWG-u4I8UoEz5cvM6hVnwofyD5GDRKu703QCgq2agkSBINHvDs8VgUjg2c-tNBhg7vdtEagndRAzhB7P6LuqNuEKedkDqLm34UG7N2cxZXi12GvlwC6XdGaUNAMKm_I4Da6hC7Ma_v5pynds4nV-ZhWYV4XAEFgsM7NA4q8Q9xdUWqbnQbkrPIoib5RgCHqcalV4KiuAux240QYg5XDmAewF1HT7fyfqdmRfeB_EhwkfnRgAbEXxAZTTelh3uJfa4PG1h49hhiU3XNl-SUdSFLCGami6xm8q4-CkTqdUvfsRqIubC1-4j4j_wBACxPF-a6RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
عملکرد اسپانیا در ۵ بازی اخیر خودش
🔥
🇵🇹
برتری مقابل پرتغال —  رنکینگ 7 فیفا
🇧🇪
برتری مقابل بلژیک —  رنکینگ 8 فیفا
🇫🇷
برتری مقابل فرانسه — رنکینگ 3 فیفا
🇦🇷
برتری مقابل آرژانتین—  رنکینگ 2 فیفا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برتری مقابل انگلیس —  رنکینگ 4 فیفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107433" target="_blank">📅 17:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107430">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387378bb2a.mp4?token=HGVifblMimUA69OiWdWVpgE9sPz_Vp5LksGH-monCprjzaPf9PEpsMNvmGAH-qT2LIOmoKGyoCNrN1ccKwb5V5kJXdeoJ11OLliTLDcDjr2FvL8FMMkfoUkD-liBbCrKL3iCNZhtZ5WyWmeQhPSYoRlEY6-rBJgW21hbg76S8eOmKq7gi3nzeeXgRsVeKl7DvAhQBqX8WJdrfgNBM_fOcf5cuPKqa_XYTRDPeuuJqr4xUUtWgOwFv_95oj5F_u2Fw0fB2LFcqO_tLBknet94RE7QnaNx9AZOwSlhBZI-d5OchhGLm7I3SXUxftOkdbGW3md_z-_WUkUo-kn4BkL0nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387378bb2a.mp4?token=HGVifblMimUA69OiWdWVpgE9sPz_Vp5LksGH-monCprjzaPf9PEpsMNvmGAH-qT2LIOmoKGyoCNrN1ccKwb5V5kJXdeoJ11OLliTLDcDjr2FvL8FMMkfoUkD-liBbCrKL3iCNZhtZ5WyWmeQhPSYoRlEY6-rBJgW21hbg76S8eOmKq7gi3nzeeXgRsVeKl7DvAhQBqX8WJdrfgNBM_fOcf5cuPKqa_XYTRDPeuuJqr4xUUtWgOwFv_95oj5F_u2Fw0fB2LFcqO_tLBknet94RE7QnaNx9AZOwSlhBZI-d5OchhGLm7I3SXUxftOkdbGW3md_z-_WUkUo-kn4BkL0nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیروزی پرتغال در خانه ی نروژ، در شب نیمکت نشینی رونالدو.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107430" target="_blank">📅 17:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107429">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jljMyCR6zZrIxy-oflVM7lvFv9xz2rzML90I9B_JZT3EUy27z575KbteS0jllqBjz_S6PrFb8rc45C_Xct5AE0Bbf-VmkAY_blFN4Lu2QEH6YBP6FyEJYxjBqmJVxscQmp0yQ08KKZ3Jgpm5OoG8TJQIk1LN-4JXJfaMRtOO3hy7g1MZ8-mpIaq5KPhxi1ZmGI3Xi3NHojYuFEKYj2vqzRGgQp7-tnBAKCESLkKpY_5WFE2cp0TzhR7WRKB-bHuGnmyyqy3YpzJcXm9IZvE7_vPPCX3LJQ9Vm8AfQJ_ASBaNWqjcfPIsmOFwJHlQl733ClOwqnOx0NzB4fx_muC6eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
عکس فوق العاده زیبا از برج میلاد و ماه که دیشب گرفته شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107429" target="_blank">📅 17:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107428">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/302c2a5126.mp4?token=Nzob2BWMz84GN-0XsZSt_sBxg5JiipQfoR7KU9XFgz5zTzRCCTPgcx2-gOhd4-017MKUuEDsvhpfLBR4cLGVviYRorhLXqXCnKfFzJKA-DsPVKT96YqxKh9GbG8fA2bg93zIlBCtxpDk8C-FVXpaF7yzg7ogGfwea6iIL5ksn_sgO6brjsA-O22tkMwcHB1rxHbjTnXuec8B2qZqItAtt4ntPbZkOhnhRhRIR4-HmPcd91cK1wMpYEecb-l_xCvQDEe3jvk7LUID_raYx6rrafp8G-EEINVvs_8Ge75vrKu6U8SPhdkQx6PmWPCtSckjTBavIQ3G1Up9APW-8XdzrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/302c2a5126.mp4?token=Nzob2BWMz84GN-0XsZSt_sBxg5JiipQfoR7KU9XFgz5zTzRCCTPgcx2-gOhd4-017MKUuEDsvhpfLBR4cLGVviYRorhLXqXCnKfFzJKA-DsPVKT96YqxKh9GbG8fA2bg93zIlBCtxpDk8C-FVXpaF7yzg7ogGfwea6iIL5ksn_sgO6brjsA-O22tkMwcHB1rxHbjTnXuec8B2qZqItAtt4ntPbZkOhnhRhRIR4-HmPcd91cK1wMpYEecb-l_xCvQDEe3jvk7LUID_raYx6rrafp8G-EEINVvs_8Ge75vrKu6U8SPhdkQx6PmWPCtSckjTBavIQ3G1Up9APW-8XdzrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دکتر بیرانوند روز اول خدمت
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107428" target="_blank">📅 17:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107427">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">📊
🇳🇱
🇩🇪
آنالیز تاکتیک جذاب ژاوی در دیدار اخیر خود مقابل آلمان یورگن‌کلوپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107427" target="_blank">📅 16:55 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107426">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a6242b00b.mp4?token=hjEz-sAIsjPASJ12xQWLbVQJeZdBc8xEabHgj1Iok5kjtlo4xClUe5Y-RH3Ao8DvA9ltl6KAl9Qx4WM6Pc4E3EDgyHAJ1fbLCUrAP80W4uLwooPWzDpHYwHO7-QhtQV3lXdJKn4-3Reqmjea8_Mzb9XGHsHB-PqoHMdzIm0yjbtUmXhsZLhbl1BqDatUatCtWB9QIFe-rFexWAjvfl9upGpQbxzALpo9yHxbwGDEUb6Qa_b8hV2nYnZr1BPTqYQ4Fjpk95ZYtIOaM8Qo5V9VDrvY2VtCNfwGQJjtbbtaKjVNWkmw0kE7vRhJNWFMorbSkflotN5QvaP93rgM1-n_Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a6242b00b.mp4?token=hjEz-sAIsjPASJ12xQWLbVQJeZdBc8xEabHgj1Iok5kjtlo4xClUe5Y-RH3Ao8DvA9ltl6KAl9Qx4WM6Pc4E3EDgyHAJ1fbLCUrAP80W4uLwooPWzDpHYwHO7-QhtQV3lXdJKn4-3Reqmjea8_Mzb9XGHsHB-PqoHMdzIm0yjbtUmXhsZLhbl1BqDatUatCtWB9QIFe-rFexWAjvfl9upGpQbxzALpo9yHxbwGDEUb6Qa_b8hV2nYnZr1BPTqYQ4Fjpk95ZYtIOaM8Qo5V9VDrvY2VtCNfwGQJjtbbtaKjVNWkmw0kE7vRhJNWFMorbSkflotN5QvaP93rgM1-n_Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مهدی‌مهدوی‌کیا: عدد فوتبال ایران پول خرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107426" target="_blank">📅 16:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107425">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63162a7ef0.mp4?token=Vx9WNVwMGgg1uOzozT7MtH8OLNAu1vFeiLSFBpilwZlEEpxQgsXwOdKMLsQu1PyfNG_T0cBhvtaPaEjC34DQvMkAoa4gGNUxIfH7KYEHAny6VQwVx16uBNSIW7PpHQNGoYT0on7F6vxjPZ_Olofjjz8dSUgZfbrPhi4k4wST54K_AUpbq4SB9v6agET9o5nD9ePzMF_-H-IaLrgeX5EUYXuOIVN5oCTBGOy4a3Uxb1XPKCzQN2VGIMnmblvAtLfY1UBANB8mMt4oa__9FxHROUEgsqg0mTMXapUdRjxclZPnm8Dc7wPVcvOxYUxEq0IHI1_2VeocqOewFL22M-7w3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63162a7ef0.mp4?token=Vx9WNVwMGgg1uOzozT7MtH8OLNAu1vFeiLSFBpilwZlEEpxQgsXwOdKMLsQu1PyfNG_T0cBhvtaPaEjC34DQvMkAoa4gGNUxIfH7KYEHAny6VQwVx16uBNSIW7PpHQNGoYT0on7F6vxjPZ_Olofjjz8dSUgZfbrPhi4k4wST54K_AUpbq4SB9v6agET9o5nD9ePzMF_-H-IaLrgeX5EUYXuOIVN5oCTBGOy4a3Uxb1XPKCzQN2VGIMnmblvAtLfY1UBANB8mMt4oa__9FxHROUEgsqg0mTMXapUdRjxclZPnm8Dc7wPVcvOxYUxEq0IHI1_2VeocqOewFL22M-7w3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇪
نحوه برخورد بازیکنان ایرلند با اسرائیل در بازی دیشب که حسابی جنجالی شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107425" target="_blank">📅 16:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107424">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6d3f57825.mp4?token=ZbwQrdeGNT6ianXruvUV_EgbO9mdGvRDOIGcHh9KWncFz7tMqxHGxF-5f6UhbHV223FMvOl5_eHZdzeOhym96vLvyi-f9viRKqQreM26ibanjO1h2_K-XHX0z7Bgz5Lk--xFFN2TyA9StCexhk5GnUdItynJjcmx0N1qxN6QtK5T2xhL37Wrfq-JMlKzzO4uoRJQy2AsYdGQIECIR4rN5_Yi0JG7JVUhrq_ZyiacirgvbY4GdIXKztoIUhrUpkVSTiyketNaN3vht6nJMVjFmja0mz10zn39gP11iFsxuQrmr4RZslQdZr7tNSeoWOAnw1CQsMvBuo4ZcLshzbFtoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6d3f57825.mp4?token=ZbwQrdeGNT6ianXruvUV_EgbO9mdGvRDOIGcHh9KWncFz7tMqxHGxF-5f6UhbHV223FMvOl5_eHZdzeOhym96vLvyi-f9viRKqQreM26ibanjO1h2_K-XHX0z7Bgz5Lk--xFFN2TyA9StCexhk5GnUdItynJjcmx0N1qxN6QtK5T2xhL37Wrfq-JMlKzzO4uoRJQy2AsYdGQIECIR4rN5_Yi0JG7JVUhrq_ZyiacirgvbY4GdIXKztoIUhrUpkVSTiyketNaN3vht6nJMVjFmja0mz10zn39gP11iFsxuQrmr4RZslQdZr7tNSeoWOAnw1CQsMvBuo4ZcLshzbFtoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیتِ ناراحت کننده ی سرخیو آگوئرو.
🙁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107424" target="_blank">📅 15:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107423">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSTeqZBwOUIkRXWxKzvCUwYP6qb2-ilzh51rP1IX4nRQa_gGXODFdEu0VDsMddO46vEIIwfgF1siO8EFRg_tuqaLKzE3g9xx09u2HVNlkVyS8qqQaPu1vFYFeEd4BgBocURTOq11RTQe55qKWl0CPIaeqE1odQXWSEcYZ7XG4OswAWnwNXw5t0YzIZxrMQ2oxKCFJlwRlundBs9sUjAGUPZk8NSubX9rV25nhdX_IoBojrZ061ExJUS1yaR4p6LuiLw0o3aZ-hJzd-e3SSd01swyUao-1yoJDqkOkLEOZO-cTQCUCQ8_yjTVlJ9wdCacI9C0kvXQPWOzozA591Mzhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🤯
مقایسه آمار هالند و رونالدو تا ۲۶ سالگی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107423" target="_blank">📅 15:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107422">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42ff849b11.mp4?token=nk34mqOT4n3NVfpkV1jquoLapH6Hxrv3fWPw6qLNjr5I3gjrODGPppHn-YupyZBZincMbEF0u8ENHX3U4-XJsKwVApPh_5V5weABJ6E2KcqbVA10I2JykZHG4PzxVC3VNkF_SMGLEKIadpT8LyThvdc3BIGDDG6Nq0G6Oz1w_lzgv-FY3Hs5qVbab0PcRQqA1go9J6syQ-6n_EyvfrdS5zxPFWoL4pZTFbwpnnl1oOZmdIJS4iikdia2TOl4n9_f8lB3ADG3iaRNwnklEZCjAABNaPfnfQ34cZxHckkRhyBpnycwoplsj2s20Q6v3daYNIC6unpfME0VF9ioz2btvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42ff849b11.mp4?token=nk34mqOT4n3NVfpkV1jquoLapH6Hxrv3fWPw6qLNjr5I3gjrODGPppHn-YupyZBZincMbEF0u8ENHX3U4-XJsKwVApPh_5V5weABJ6E2KcqbVA10I2JykZHG4PzxVC3VNkF_SMGLEKIadpT8LyThvdc3BIGDDG6Nq0G6Oz1w_lzgv-FY3Hs5qVbab0PcRQqA1go9J6syQ-6n_EyvfrdS5zxPFWoL4pZTFbwpnnl1oOZmdIJS4iikdia2TOl4n9_f8lB3ADG3iaRNwnklEZCjAABNaPfnfQ34cZxHckkRhyBpnycwoplsj2s20Q6v3daYNIC6unpfME0VF9ioz2btvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
بیژن مرتضوی به ایران بازگشت  بیژن مرتضوی، خواننده و آهنگساز، دو روز پیش وارد ایران و روز گذشته در منطقه نیاوران مستقر شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107422" target="_blank">📅 14:59 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107421">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1947c53917.mp4?token=SD12AV5DX9DkBBsAa5M0HTgwugGAou-bVpxICr0o7vdJIhkgGudWeq-qWHSUQ-miu0-gALaosDl1uBdYJyGCneQV9geprkunkQiofrIgqEjsoQ8Gv4GZnTmCoPSekfC_ve42B20wOXgKeoXIzldwFQyDasPwTdaAmZgf9fwD5ezAZcB63I-yUGgihh5Q0Ixrbf5Glhxvwk8aLfLabYZIVlLYAQz_7AuuJE5CDwicGMMi1OHxPIDJZBnuq4fccUD6mcfYoaC-wfFztyCIh3-ng2JbcEZf1VJc6dbY-SyynNk79oTrYgE-K0vmzbI4TLx0KRHmMvKa3D5fgInFGKVfM2eFgK6hlDX4jEY89olNeIM7NQcdd3-xahrJABFdQFlvapbau60GAssfJ0_AukYXwKNJIOk6IqQdJuW1TFd45zVpfiW5g77N78yWTXDSrByiZoPrFFIBEmO2h-2Z92m2QhE6g9IxygKkspKbPkRbTDnTVYic8EG9_dvMGQvndah3OrqCcfHgXjGzry_kNm8VJnR444sF8ZwfHLGkJ47-wMNzyhZ3DVpXYBMqngW94Fc2ZBgSOuQZgHKcJl-NqT4RPAf2GwVYpl25yVoDfU7sk9IMEVCIzAZzlSY-Wnf3hnONBlekQWBBuXz0Tbt_K2nKPLiBf6bMqBNRC-SkgZPqvWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1947c53917.mp4?token=SD12AV5DX9DkBBsAa5M0HTgwugGAou-bVpxICr0o7vdJIhkgGudWeq-qWHSUQ-miu0-gALaosDl1uBdYJyGCneQV9geprkunkQiofrIgqEjsoQ8Gv4GZnTmCoPSekfC_ve42B20wOXgKeoXIzldwFQyDasPwTdaAmZgf9fwD5ezAZcB63I-yUGgihh5Q0Ixrbf5Glhxvwk8aLfLabYZIVlLYAQz_7AuuJE5CDwicGMMi1OHxPIDJZBnuq4fccUD6mcfYoaC-wfFztyCIh3-ng2JbcEZf1VJc6dbY-SyynNk79oTrYgE-K0vmzbI4TLx0KRHmMvKa3D5fgInFGKVfM2eFgK6hlDX4jEY89olNeIM7NQcdd3-xahrJABFdQFlvapbau60GAssfJ0_AukYXwKNJIOk6IqQdJuW1TFd45zVpfiW5g77N78yWTXDSrByiZoPrFFIBEmO2h-2Z92m2QhE6g9IxygKkspKbPkRbTDnTVYic8EG9_dvMGQvndah3OrqCcfHgXjGzry_kNm8VJnR444sF8ZwfHLGkJ47-wMNzyhZ3DVpXYBMqngW94Fc2ZBgSOuQZgHKcJl-NqT4RPAf2GwVYpl25yVoDfU7sk9IMEVCIzAZzlSY-Wnf3hnONBlekQWBBuXz0Tbt_K2nKPLiBf6bMqBNRC-SkgZPqvWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
على تاجرنيا مدیرعامل استقلال: پاى حرفم هستم ؛ پول كاريله رو ميدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107421" target="_blank">📅 14:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107420">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdc8f323f.mp4?token=h4lXNlPEox2aq7j__nXoccmecrZPMCFnmYK9cM78Eaw3Kmsabsh-Jkr6pNvk9_ZpGV8WMDpc2bUJGxY7ZSMg8WetNxAyKGn9g4K10TITmX-QWsdqPopc8Vh1TAG8x0megtqVHmBtxN5OY-iLNwKZpL6DhBozI6Fw_BcQyjLlM2VbXpqM7Ib68s_0Cg0MA4alsNKUXNttePmV6qdJwlmIMS071_lwsTne3MrKCBe4TLfkfqOXHqymVPwHjcyd4YpXwcGCRMru3XEqTUF6wAHRWG9xKbrsOIwZT4_TH7OYzp7DMpnZ2VMox-GIX1iNRWWE9h0cP6LmFK_ezxIkZhJTtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdc8f323f.mp4?token=h4lXNlPEox2aq7j__nXoccmecrZPMCFnmYK9cM78Eaw3Kmsabsh-Jkr6pNvk9_ZpGV8WMDpc2bUJGxY7ZSMg8WetNxAyKGn9g4K10TITmX-QWsdqPopc8Vh1TAG8x0megtqVHmBtxN5OY-iLNwKZpL6DhBozI6Fw_BcQyjLlM2VbXpqM7Ib68s_0Cg0MA4alsNKUXNttePmV6qdJwlmIMS071_lwsTne3MrKCBe4TLfkfqOXHqymVPwHjcyd4YpXwcGCRMru3XEqTUF6wAHRWG9xKbrsOIwZT4_TH7OYzp7DMpnZ2VMox-GIX1iNRWWE9h0cP6LmFK_ezxIkZhJTtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بیرانوند از خیابانی تو خدمت مرخصی میخواد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107420" target="_blank">📅 14:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107419">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39074d4c05.mp4?token=FU97KexHEmxJcMIj0v9TjnrOBq7JvXgA_wszzbz1296Hp6MLYCE0znfcEZAitOyhC7FEUUR-6FrCw8_M6emG6Nfz-e6vvvsCRYi3xF4TbLA638-rFnehD-1DYYRcYNE-9_WzSCUVfvlWP11UBwRYlQuv1lkB_4Dj6h5QwZx7ipQLuHqFxDlCxnt1W-k6QGLYIDEHsQDHEtk0Nk0sClrN0GwaBl4zS_DssgqSfJ-9PdRHiC4r8uT4cg6CDjANurG9l7N1WSYEYRwPaW-jKEWd5D3Bh9KCMND5MgA5goobX4A4v_yxHgozBiYzXR0sepLF4_RHwp0jK-4-REBODlmGwqr8iXfJ_Ih8TH9_HeIRqlsNecWHTG0whrcsFfJuEG7_SVt4Sn7sHt0LqyKCBV79hRMf_rGtTQ_lFzAB7_3M9uXqaGr3Q_QWw5W0NoRlElWDTOEbrYByy0VYXJHoKUj54b9b-Vfp_YvQLdNP3MyH6bi3I1aBUWudQSFuUlI0mNd2zsaSCwVEJl7j5igHzcfgR76eNoqBrs16Q1Pg5q8QD1eHiOo9rZkWaNAs3abn6oU1wH8ZNhlcjJBFCmosq4YvJBCYu11O9bZe-4W9NjGL_QANk5BiLNctTGKVZkNZb3bMKHHRawkg3ty5tWg8uSSjKeNtuM_BzfJ9HG-eilfg40A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39074d4c05.mp4?token=FU97KexHEmxJcMIj0v9TjnrOBq7JvXgA_wszzbz1296Hp6MLYCE0znfcEZAitOyhC7FEUUR-6FrCw8_M6emG6Nfz-e6vvvsCRYi3xF4TbLA638-rFnehD-1DYYRcYNE-9_WzSCUVfvlWP11UBwRYlQuv1lkB_4Dj6h5QwZx7ipQLuHqFxDlCxnt1W-k6QGLYIDEHsQDHEtk0Nk0sClrN0GwaBl4zS_DssgqSfJ-9PdRHiC4r8uT4cg6CDjANurG9l7N1WSYEYRwPaW-jKEWd5D3Bh9KCMND5MgA5goobX4A4v_yxHgozBiYzXR0sepLF4_RHwp0jK-4-REBODlmGwqr8iXfJ_Ih8TH9_HeIRqlsNecWHTG0whrcsFfJuEG7_SVt4Sn7sHt0LqyKCBV79hRMf_rGtTQ_lFzAB7_3M9uXqaGr3Q_QWw5W0NoRlElWDTOEbrYByy0VYXJHoKUj54b9b-Vfp_YvQLdNP3MyH6bi3I1aBUWudQSFuUlI0mNd2zsaSCwVEJl7j5igHzcfgR76eNoqBrs16Q1Pg5q8QD1eHiOo9rZkWaNAs3abn6oU1wH8ZNhlcjJBFCmosq4YvJBCYu11O9bZe-4W9NjGL_QANk5BiLNctTGKVZkNZb3bMKHHRawkg3ty5tWg8uSSjKeNtuM_BzfJ9HG-eilfg40A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔺
آنخل دی‌ماریا پس از به ثمر رساندن گلی شبیه گل مسی:⁣ قبل از بازی استرس داشتم و سعی می‌کردم با موبایلم خودم رو مشغول کنم و به بازی فکر نکنم که یهو گل ضربه آزاد مسب جلوی آمریکا روی صفحه گوشیم ظاهر شد. وقتی توی بازی صاحب کاشته شدیم، با خودم گفتم امتحان کنم؛ درسته من مسی نیستم، اما شاید جواب بده. و واقعاً جواب داد!⁣
🥇
روزاریو سنترال در فینال سوپرکوپا اینترنشنال آرژانتین با دبل دی‌ماریا ۳ بر ۱ استودیانتس رو برد و قهرمان شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107419" target="_blank">📅 14:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107418">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb4774088c.mp4?token=sR4mpT46BCqhP2oj3fMxqTiTAMgZ5AqlQ7n-0m5C9xUXf8vANK-gxaMu-HFBnzUc9JETZ_TiE7cCPXLWnhzltZsXey2f9kk5suesxOEovk5VXxnVWK5dq8g3IwaE4oUOUhpZxaPRwdXJKNj34Y8x4AyvjKCEvw2CRURGvAQRl5pgu1WCc64Xg5pmkQAiT_O9XLaMYbAa_NVBNzXzODucP_-Gamlnbjb5ugAQrgkgRVunu8Vp_HC92Uk5z9ic4ONTveQInArqnfzgA6yzwK5INQGQglKpTPzWl4thzXfshfExNE2jqcibAw252-IzPbt1f9mUnIpddIabHe3cbDGGjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb4774088c.mp4?token=sR4mpT46BCqhP2oj3fMxqTiTAMgZ5AqlQ7n-0m5C9xUXf8vANK-gxaMu-HFBnzUc9JETZ_TiE7cCPXLWnhzltZsXey2f9kk5suesxOEovk5VXxnVWK5dq8g3IwaE4oUOUhpZxaPRwdXJKNj34Y8x4AyvjKCEvw2CRURGvAQRl5pgu1WCc64Xg5pmkQAiT_O9XLaMYbAa_NVBNzXzODucP_-Gamlnbjb5ugAQrgkgRVunu8Vp_HC92Uk5z9ic4ONTveQInArqnfzgA6yzwK5INQGQglKpTPzWl4thzXfshfExNE2jqcibAw252-IzPbt1f9mUnIpddIabHe3cbDGGjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🐐
سوپرگل دیشب لیونل‌مسی از نماهای مختلف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107418" target="_blank">📅 13:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107417">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a5b80ac0.mp4?token=vO-F-s_Kz4B2xBKnOCgI7zhy2f3Ho6NgNGGsulsa8xASzzYy6VpKIyRUvTHvjP4h72uwJYPBL91UPo-5NfiRAx72xt6Vx4kOiLwIHUebsdyAZCFjUqLC8COHUAH7QG1MCpszUlDZ_idyKSu75w-9AQz6Re4KFuZbaWwOFov4XYheXYxJagNw40LJ1HbQHN5qLKg4WHH-DXZocr9HkT4mnOE7GZqFQaJ_6lizgeifbZ3GX5s9ij74Oif-0zhfbO0rzngCIIoGsOO9EdgwLvFB1PR-naKkwrR3ecIgcXE_AizD97g6NShwYawbQIfmbz6ubhnghA6EYg4k6PQuXwO1oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a5b80ac0.mp4?token=vO-F-s_Kz4B2xBKnOCgI7zhy2f3Ho6NgNGGsulsa8xASzzYy6VpKIyRUvTHvjP4h72uwJYPBL91UPo-5NfiRAx72xt6Vx4kOiLwIHUebsdyAZCFjUqLC8COHUAH7QG1MCpszUlDZ_idyKSu75w-9AQz6Re4KFuZbaWwOFov4XYheXYxJagNw40LJ1HbQHN5qLKg4WHH-DXZocr9HkT4mnOE7GZqFQaJ_6lizgeifbZ3GX5s9ij74Oif-0zhfbO0rzngCIIoGsOO9EdgwLvFB1PR-naKkwrR3ecIgcXE_AizD97g6NShwYawbQIfmbz6ubhnghA6EYg4k6PQuXwO1oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
ویدویی از درگیری بلینگهام و کوکوریا دو بازیکن رئال در بازی اخیر اسپانیا و انگلیس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107417" target="_blank">📅 13:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107415">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55f2619929.mp4?token=bZgkP2tOlZe7oWe2eh-CwIucYd_OkJQzs3-UUDW9GSqcadHj30T5TRMKR_aU8RreXiEEhL7XFyNRvFCgfT_WsIEbpBlyxGD5-qLNV87aa9tBGCxo6Bx5UVh4h9sGu5kS6UVqoV3lqCeTf2c-eTNjmc6trxZ8b-B169Kp3ObVevvTO59TUYy1BMpenzS-sA0I56NfX5TXNx6o1mJUnMGgYzGvdXNV7kaH2R02R_azX6acH38xsKDXkGlpJKL0ZDt3n4RmVhrq_3J2nu13VeBa8mRhxwNg-hPzupjKnbLipMW6vSQN0dW8XoiEQAeqNZeLEr4sQDY8x6FdDc_RMggVJTxK26TKwNMmr8m7qIMZxPBpmkewUii4qL1XTwL2Pwcvnba8z-xy4_9yj_DQ9jQPthSLki1UB_2Cuy_cyMMbP6xh5s9lf4ZSdCH59HdvuPDP3vdiFdOyZN555PGYKYHu9leMGwmsu9iG7_wvpkMGrgyQtJp9krPfUItwI49bDtW7zDbazCudbg52NdcwASbGP3GxYUf8oOrFa9eKtcdM4qVNy91UsIXFTOcC-fOIUiS2USSY5jfMjac4Fb43ZydsDiUkT46iJZdHh09KKyZTGztU_JAx7N8cAMrG3g_hTl7zgt9oeuS-78HFpzPL-6snskNXwwCPH00ZAdU1ccKFZIc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55f2619929.mp4?token=bZgkP2tOlZe7oWe2eh-CwIucYd_OkJQzs3-UUDW9GSqcadHj30T5TRMKR_aU8RreXiEEhL7XFyNRvFCgfT_WsIEbpBlyxGD5-qLNV87aa9tBGCxo6Bx5UVh4h9sGu5kS6UVqoV3lqCeTf2c-eTNjmc6trxZ8b-B169Kp3ObVevvTO59TUYy1BMpenzS-sA0I56NfX5TXNx6o1mJUnMGgYzGvdXNV7kaH2R02R_azX6acH38xsKDXkGlpJKL0ZDt3n4RmVhrq_3J2nu13VeBa8mRhxwNg-hPzupjKnbLipMW6vSQN0dW8XoiEQAeqNZeLEr4sQDY8x6FdDc_RMggVJTxK26TKwNMmr8m7qIMZxPBpmkewUii4qL1XTwL2Pwcvnba8z-xy4_9yj_DQ9jQPthSLki1UB_2Cuy_cyMMbP6xh5s9lf4ZSdCH59HdvuPDP3vdiFdOyZN555PGYKYHu9leMGwmsu9iG7_wvpkMGrgyQtJp9krPfUItwI49bDtW7zDbazCudbg52NdcwASbGP3GxYUf8oOrFa9eKtcdM4qVNy91UsIXFTOcC-fOIUiS2USSY5jfMjac4Fb43ZydsDiUkT46iJZdHh09KKyZTGztU_JAx7N8cAMrG3g_hTl7zgt9oeuS-78HFpzPL-6snskNXwwCPH00ZAdU1ccKFZIc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
🇮🇷
على تاجرنيا:صحبت های بازگشا مدیر پرسپولیس سخیف است و در شان من نیست جواب او را بدهم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107415" target="_blank">📅 12:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107412">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnx-3IcFW2J2gg6IC__ITdoqSoySmGicnjDYg2yE2IprqgbfQeT3ebKFa92qsVY6Vf4Ore0nV5uIVvOdVFjxTEdZBupwVDh8709gAZo4-TBQnVYPmY4VMkrfzZm-otnBMiSIxtpG5ZrW1QMyoexS9QNSpFbR5c_4KJxfI6pK-vHDMkwmaWHD84DKRijwcB9zg9IpIVoGt34bran_sXOD3Nhhg2AaT4jbMB0uexmuYZ7jCalaiWJr6KAryi7wuQej30YoGQPxcYx0ltw2Q6B51nTes4OfubwRw_asyCPGeHf7ETMmnwJSYt8a1AvQ9tzycG8JW9kJWW9u6wK81gQSGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🌍
آپدیت رنکینگ فیفا پس از بازی‌های اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107412" target="_blank">📅 12:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107411">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2bfc79cd9.mp4?token=DfHmNkYwmkTF9hGWxI9o85-DvZD7GpWCV1NwxOCIhi-ckTDIS7DDPCyIK4swG2Ak--nRQZFM2l3cWP0EyirIqmp2T1jCVswoCq45idTgYLIsBijVkXD7YdI8zHMhC3VRyKy3G5znmycGk7Yj1CUdlMztFP-y027jRG5DWHnrF56CntSyK1sFt1VYz1BW5Ooy3eHHhTky8tXAu6dTxFeOeBun6rzs5u9uvnBP3FpJgpCrhs1N-2-O0ng33IOiZPLjoKdN5QrD49i6QS7QMY0qPIYFIBVHudeu26Pe7sjY5NC_ldgz366ak10zmceIMFLDhwUpkrpzYRrFSDVFLL-GOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2bfc79cd9.mp4?token=DfHmNkYwmkTF9hGWxI9o85-DvZD7GpWCV1NwxOCIhi-ckTDIS7DDPCyIK4swG2Ak--nRQZFM2l3cWP0EyirIqmp2T1jCVswoCq45idTgYLIsBijVkXD7YdI8zHMhC3VRyKy3G5znmycGk7Yj1CUdlMztFP-y027jRG5DWHnrF56CntSyK1sFt1VYz1BW5Ooy3eHHhTky8tXAu6dTxFeOeBun6rzs5u9uvnBP3FpJgpCrhs1N-2-O0ng33IOiZPLjoKdN5QrD49i6QS7QMY0qPIYFIBVHudeu26Pe7sjY5NC_ldgz366ak10zmceIMFLDhwUpkrpzYRrFSDVFLL-GOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی پرویز برومند در جوانی ادای جلال طالبی رو در میاورد؛ عجب تقلید سمی بود
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107411" target="_blank">📅 12:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107409">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwTZOtuB6GO3MWZZFOVbVQEg4N5q7pbHLgng8p7dsj-jobG1hGQXhCPqrxFDv580TW8oVrBcOcNWh0wzcbwcG5XMZDlzkxQOOY-0MDTCTPtUX3vJoNrPj5r6uaU95hS1KQxrGTvoD5lFzxl_wKPKtF-h5tl6K4gaXBHHZhjN6Q87vXyGRvfQzWf-WKtN7fF0nP5jDWsl8ZkVHpOeGMgneW4C2p0_dzZbKa9KnYplsGdkiKKuAjl-cG0IoEs0qwSkDCmQvRSBJ6uRMoSuk5F3jJX4XzsCN2HAfrQqnZPwvJBNy8sfMr-ale7e4NALpwWaUAHl-6DImB9ON4MEjaM25g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
بیژن مرتضوی به ایران بازگشت
بیژن مرتضوی، خواننده و آهنگساز، دو روز پیش وارد ایران و روز گذشته در منطقه نیاوران مستقر شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107409" target="_blank">📅 11:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107408">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/573c62a08a.mp4?token=Ze22kgo9VKdv1ORn_m5eifdOhxGPrAjFRvUrI4hoWS-a6wCL1f6fkBp3kYJtEzkHKYViGgBNsTlwx1YVKBcOoWMSE5BI_YRxz_xv82LOWLqO_Gr0dKGNhzkW-xgt9og5jTzXuUVjaqA9Sa70Z-17vX6aSPjcvT9bBTl4IW9-AjDkRTc8UA-XxnC6WQ2vCbW18p4aXowcEpTvEWr_cF2p3HephgiZ-JmHLf9YgZvwIDtjkHIWGfrgCPg_Aulz-B-isuW8wSjxUzl9E1ELKtAhN6cKhdTRtgIii3eaHkaWGuhn6cx5nPEIQd0_zRNc31Eqmpa8Ai7KGNqObMEXBCKduQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/573c62a08a.mp4?token=Ze22kgo9VKdv1ORn_m5eifdOhxGPrAjFRvUrI4hoWS-a6wCL1f6fkBp3kYJtEzkHKYViGgBNsTlwx1YVKBcOoWMSE5BI_YRxz_xv82LOWLqO_Gr0dKGNhzkW-xgt9og5jTzXuUVjaqA9Sa70Z-17vX6aSPjcvT9bBTl4IW9-AjDkRTc8UA-XxnC6WQ2vCbW18p4aXowcEpTvEWr_cF2p3HephgiZ-JmHLf9YgZvwIDtjkHIWGfrgCPg_Aulz-B-isuW8wSjxUzl9E1ELKtAhN6cKhdTRtgIii3eaHkaWGuhn6cx5nPEIQd0_zRNc31Eqmpa8Ai7KGNqObMEXBCKduQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚔️
درگیری شدید بازیکنان در بازی دو تیم عراق و کویت در تورنمنت جعلی خلیج‌عربی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107408" target="_blank">📅 11:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107407">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2719da70df.mp4?token=Hr1QmOliG686caw_K8Nyw-Ohdppbzj-rEkBh1QmVj1n8Q8HErrybJ-MVvYoepcPof7DYmkqi54qjxLSHl3yXkCJlI1_L5dJao_0YuY0QHUszclL4DPlktphBNzMk2E2kCFySJut2PLrhaCCVBvSbM5EkNjghK03Ws6XBV_FJ7GCi3HrrhT7b3CzDy0VNFC9Xgz___HuNS6X74AFFQ5JuQt-G4gZE9tDiW3eaIGph5xVCZhFLnhkelsHkl7J8gDNPGBbRv_k8AeHWRDmue6_umyKjhBD4FprVWiO-KtRtN_bhZbwBmDm9DEreRpMARN4dplo42tCcmXgVhi7ZoHHYeI1ayuJUNy_qmrNdoy2b1en7zWDm9O_iP0qU_gHlw6rYPD_Y4r340coakXbJMoODtCv6cE81uyzUr51IWlayKdlfJYc51Yd2VIvUk9VjjFVjkCk12mVvBX1DFqTcUtf45MO3A90dBt-5pVbXIFCxeYq9nSA1NlOjM4XnSNm0DE1X58tJ6CCJoG7ZOu0RZeLA4jborRv9UlelbelvyqSzNfWs7AwoTtO3qUjnDcsO7Jf7-cau1g5QZk3fV4GtKaDyznZgWQ_ottwzmASO4Ran_sXoWiJPjufitPopc5GUega50XpR7TA53t59qxdK5FQyND_99L_xKx8tilG6Gia-8p8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2719da70df.mp4?token=Hr1QmOliG686caw_K8Nyw-Ohdppbzj-rEkBh1QmVj1n8Q8HErrybJ-MVvYoepcPof7DYmkqi54qjxLSHl3yXkCJlI1_L5dJao_0YuY0QHUszclL4DPlktphBNzMk2E2kCFySJut2PLrhaCCVBvSbM5EkNjghK03Ws6XBV_FJ7GCi3HrrhT7b3CzDy0VNFC9Xgz___HuNS6X74AFFQ5JuQt-G4gZE9tDiW3eaIGph5xVCZhFLnhkelsHkl7J8gDNPGBbRv_k8AeHWRDmue6_umyKjhBD4FprVWiO-KtRtN_bhZbwBmDm9DEreRpMARN4dplo42tCcmXgVhi7ZoHHYeI1ayuJUNy_qmrNdoy2b1en7zWDm9O_iP0qU_gHlw6rYPD_Y4r340coakXbJMoODtCv6cE81uyzUr51IWlayKdlfJYc51Yd2VIvUk9VjjFVjkCk12mVvBX1DFqTcUtf45MO3A90dBt-5pVbXIFCxeYq9nSA1NlOjM4XnSNm0DE1X58tJ6CCJoG7ZOu0RZeLA4jborRv9UlelbelvyqSzNfWs7AwoTtO3qUjnDcsO7Jf7-cau1g5QZk3fV4GtKaDyznZgWQ_ottwzmASO4Ran_sXoWiJPjufitPopc5GUega50XpR7TA53t59qxdK5FQyND_99L_xKx8tilG6Gia-8p8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
خاطره حنیف عمران‌زاده بازیکن سابق استقلال: هر بار گوسفندان را می‌شمردم، یکی اضافه می‌آمد؛ متوجه شدم خودم را هم دارم با آنها حساب می‌کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107407" target="_blank">📅 11:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107406">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818f1ea358.mp4?token=XFwwjp-lU5oqLah39atujWOfXbADswAVfAWZxKoM9c2nFfIghbv2XPd1N1olwDbMYUhgBIfwJT4cIV6o9nF-p-x0mE5UYx7riXo40BkfUGPCh980rVilRh_-P0jLUsQrW0ugfWSnJVxPS9iLa751XePWHL8_4j8HWQPAw_DUV3al1vaZFT3AxpGWeh7VOqlicI3T6EVYMvkFOkvuQj5PV_NV8wlgYkVXiuvX0ucF1Cv0jA8-v_uSokenfzWt9WVPPALS80AYJSppuYx8gJM_8XMYTM-v4fc6avVjqXB0V0bOYnJIQgwFKAu-Lz9NqInk8jwHiHUFHJ-FPfIWVm58coWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818f1ea358.mp4?token=XFwwjp-lU5oqLah39atujWOfXbADswAVfAWZxKoM9c2nFfIghbv2XPd1N1olwDbMYUhgBIfwJT4cIV6o9nF-p-x0mE5UYx7riXo40BkfUGPCh980rVilRh_-P0jLUsQrW0ugfWSnJVxPS9iLa751XePWHL8_4j8HWQPAw_DUV3al1vaZFT3AxpGWeh7VOqlicI3T6EVYMvkFOkvuQj5PV_NV8wlgYkVXiuvX0ucF1Cv0jA8-v_uSokenfzWt9WVPPALS80AYJSppuYx8gJM_8XMYTM-v4fc6avVjqXB0V0bOYnJIQgwFKAu-Lz9NqInk8jwHiHUFHJ-FPfIWVm58coWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
با لابی‌های علیرضا دبیر،‌ معافیت بیرانوند همین‌ شکل یک‌ماه یک‌ماه جلو‌ خواهد رفت!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107406" target="_blank">📅 10:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107405">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fe4bcfcae.mp4?token=HG5YxFQh8HatzXsNCO9dzp9ht5X4hYCuhSY1bEv9BigPJedmKPEzdGLZPKyOqAWCwxlZ4lwrNSdB15tqKMcNOvGA4FuodEg6VmJA-ZyxM3PDKYz3NL3YZ8c2PbyduGGgy5KLBt07HHOl-FN8K38icMPJII5FwQuPdveWC3oMln4lQXNLGocgfDWNZv6rW3mA6YqLa_x43Uradko_jVLlj0wqWCl79pKhEJ9TDUV_f8X0yC_L_D2CXNLiM991JZxwDNIbLP63Ma0V0H_BifwWsa_KwX4RHN7nVtzPTt19qj3iWc5BXilAyYK95jCBJyPZzgJTjYplHDMoffsk9f2Zh5y3b9vMkRUcAmzNHx5pdsPmcf6ItQEIKXPMnae0jtuNePzC7edomU6QTd82nd3dCPiSPolBuCR2tzMHGbXG0tL5T_0RcOBgttVnAZtZgvZbNFIPdaTpUI4GoXZP1L_JzNPK-Pqkyehdxk3sTxEjSKPepBbNo2dw3wEVVTvdVEBc9IMaY429hMt63hjyUkXnTj-SAUYO8i0oHvDmRw-_ldHloDOLinJhdQqsXmDKZu4Gbpv1WQaSkcS6bc79SreUYSacBIhm80tEqEQ-ZJcJXp5efsJtAxw9DmyQk7m33l8C06F2s-Xh7jVJ927XN4K_ZTYGBzx9RvZ-l91MZMkltqY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fe4bcfcae.mp4?token=HG5YxFQh8HatzXsNCO9dzp9ht5X4hYCuhSY1bEv9BigPJedmKPEzdGLZPKyOqAWCwxlZ4lwrNSdB15tqKMcNOvGA4FuodEg6VmJA-ZyxM3PDKYz3NL3YZ8c2PbyduGGgy5KLBt07HHOl-FN8K38icMPJII5FwQuPdveWC3oMln4lQXNLGocgfDWNZv6rW3mA6YqLa_x43Uradko_jVLlj0wqWCl79pKhEJ9TDUV_f8X0yC_L_D2CXNLiM991JZxwDNIbLP63Ma0V0H_BifwWsa_KwX4RHN7nVtzPTt19qj3iWc5BXilAyYK95jCBJyPZzgJTjYplHDMoffsk9f2Zh5y3b9vMkRUcAmzNHx5pdsPmcf6ItQEIKXPMnae0jtuNePzC7edomU6QTd82nd3dCPiSPolBuCR2tzMHGbXG0tL5T_0RcOBgttVnAZtZgvZbNFIPdaTpUI4GoXZP1L_JzNPK-Pqkyehdxk3sTxEjSKPepBbNo2dw3wEVVTvdVEBc9IMaY429hMt63hjyUkXnTj-SAUYO8i0oHvDmRw-_ldHloDOLinJhdQqsXmDKZu4Gbpv1WQaSkcS6bc79SreUYSacBIhm80tEqEQ-ZJcJXp5efsJtAxw9DmyQk7m33l8C06F2s-Xh7jVJ927XN4K_ZTYGBzx9RvZ-l91MZMkltqY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
❌
آنالیز فنی از تیم‌قلعه‌نویی که مشخصا چیزی به اسم‌فوتبال بازی کردن بلد نیستن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107405" target="_blank">📅 10:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107404">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e340f6f2fc.mp4?token=vzyecF-RvdrHNLqVeNGXFiaivebLenHtXp7uoCDHUu1jmZZlKvujYTYOqYkup0j6lUJI1xLBh84wQUp7k5UgiduvOdNep7OfbsnlMUq7jrZHc81ZZpYIqXqEpp6yOd16ynZfQrCIsCD0Npl5IjxCYb9rahYdTcg2WLEOdqqgj4qRfKId1bcZQB6F3KNZd7-zZfM6spbFmbru6cIUVqlUJ98ahZTea5yf5evEX09G5WfwUym97RRu63ajcMPBaSGaJMjDpV-uSdgUlH9ooFcRD2XdOEm2YhzGsVeE46Tr-eN-XeC_-H1uboHmSuDkKi6-z42vH71-rcSJs8pBc3gnDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e340f6f2fc.mp4?token=vzyecF-RvdrHNLqVeNGXFiaivebLenHtXp7uoCDHUu1jmZZlKvujYTYOqYkup0j6lUJI1xLBh84wQUp7k5UgiduvOdNep7OfbsnlMUq7jrZHc81ZZpYIqXqEpp6yOd16ynZfQrCIsCD0Npl5IjxCYb9rahYdTcg2WLEOdqqgj4qRfKId1bcZQB6F3KNZd7-zZfM6spbFmbru6cIUVqlUJ98ahZTea5yf5evEX09G5WfwUym97RRu63ajcMPBaSGaJMjDpV-uSdgUlH9ooFcRD2XdOEm2YhzGsVeE46Tr-eN-XeC_-H1uboHmSuDkKi6-z42vH71-rcSJs8pBc3gnDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
🎙
مرور صحبت‌های ژوزه مورینیو در ۲۰ آذر ۱۴۰۳ درباره اتهامات منچسترسیتی و پپ گواردیولا⁣
⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107404" target="_blank">📅 09:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107403">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3HYvTWkviQF_DISyB7KGKrZOzamPGU0UsP282sbH8H_fzKQVrVCiQJMAoNpbgNPwzZNWv5aYsT4C7ISUC-UZFvMzcjjCYil92luGAn2mAxjG-6y1ol44KasjJqaN_clLYDQtIjpetP6suymCuiHHoocxNYInH1RXq5RUOVa8nSWlANyRm5u2Y7AoToFbg03G-9Waj4jip7_KErMR2wX2I7Rheg9q6jbJDo9XI9sgjNUZYRpye-z4UJPgk69eTG3GUnzBQKZKMr9YKYJ8xBQ0wjCxirD3Py96C5bMTbJ5Z8-_KnzOv8r9UNA_1fx18eZxkGq3gZMK8LWQaWMV0d4CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
علی‌تاجرنیا خطاب به هواداران استقلال: جواب پرسپولیسی‌هارو ندید چون مکتب استقلال بر پایه احترام و اخلاق است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107403" target="_blank">📅 09:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107402">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTRNg7Im7huNYVBi0Dm7n_wKmtG4qHeCsbwTKbtpBbsrBiB8UAkbp5FWGlOUc-C-I5p4KThBcXWYU4Y3zs-fnsMg_oGkfq6Yq6DoGxghT_yr7e9RQhy9FsHNeH3efBH8eL_tCqdQTvKkk6mG1L05XO2SqBAJALB6NrvH10DLrMfgmmRPDhGo1i1a1FBUWSazlkMVviMiKBr2CGfDPTbLs0wMMmOmDbAeCoOvIbEoWzqCP0rlPucpyMzSm6hVzECtr4iCSvMmymgFVKFKsO0RXw3QSkgi0IvLaOLp-Mfgg7MnpQi0Z1qigJDqJyL_wj_oIRZrZhj3bSLkfKU9HIoumQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚽️
۱۳ سال ناکامی‌مطلق امیر قلعه‌نویی در ایران!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107402" target="_blank">📅 09:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107401">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f1638a09e.mp4?token=Sm0zJqpymUh9ntZU5rq0xtLeHYQ7zqkzGVbfUshLHk9aNqZCwNSjXKhX0TkhqR2mhl_Ik98B426KHKXhF-ROntkOzv2csBo6bQXuhYwY3dKCLhScmPGxwVMxxQB829vhUYGrkpJ1CHDR9Y3atkvgtsn6fhlWS3dNeFSxjOyqYO3hFCSIRX8kD9obPOPQTRMebi8MpRRY_9u9yz750pwIyhaqqrspwC1JeOAaBXbGdbc8o1X4VGslSvjRdIY29Op17aB6eSLGVg9j2k0QfXNGMjs1qnd0UVFld2kWK3YQeqKe7dUxslIJEfz__-Um504wNTknBun2aqZDLUZOzfm0tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f1638a09e.mp4?token=Sm0zJqpymUh9ntZU5rq0xtLeHYQ7zqkzGVbfUshLHk9aNqZCwNSjXKhX0TkhqR2mhl_Ik98B426KHKXhF-ROntkOzv2csBo6bQXuhYwY3dKCLhScmPGxwVMxxQB829vhUYGrkpJ1CHDR9Y3atkvgtsn6fhlWS3dNeFSxjOyqYO3hFCSIRX8kD9obPOPQTRMebi8MpRRY_9u9yz750pwIyhaqqrspwC1JeOAaBXbGdbc8o1X4VGslSvjRdIY29Op17aB6eSLGVg9j2k0QfXNGMjs1qnd0UVFld2kWK3YQeqKe7dUxslIJEfz__-Um504wNTknBun2aqZDLUZOzfm0tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
❌
مصاحبه جالب بازیکن خاتون‌بم پس از گلزنی و برتری مقابل استقلال در لیگ‌برتر بانوان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107401" target="_blank">📅 09:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107400">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c65f44125.mp4?token=eM4R8yzARhsA3QlzEudUuknvmcuyJVqwa29VXwtgQbXN4SAmPFhdMjd3M742wND788_yjP9oBGSAcy2W3pmv3oB7wI4Jl3mRObMHqzq8FDEQ_kvH6USo9BzLfkf6kjriX6j-oVeToT7YAzGJVYBW33TOMhYsTk8Q-atzv6y2mCn4uk-wJfyV1u-3Ek--osTJagHzB4cRUtaRQ9RvKBS5dnLl-nTWpc_s9V3FrPizxyRYBFzwUtj1lApcN9b2EP54J3SCyZ9TKC6UY6OctquVjXnXauqnm6rZOoQfkWmdj9ZPG0ajVgYdUis2opIF7WGWfFAA9URm0LWKT01NYvtn1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c65f44125.mp4?token=eM4R8yzARhsA3QlzEudUuknvmcuyJVqwa29VXwtgQbXN4SAmPFhdMjd3M742wND788_yjP9oBGSAcy2W3pmv3oB7wI4Jl3mRObMHqzq8FDEQ_kvH6USo9BzLfkf6kjriX6j-oVeToT7YAzGJVYBW33TOMhYsTk8Q-atzv6y2mCn4uk-wJfyV1u-3Ek--osTJagHzB4cRUtaRQ9RvKBS5dnLl-nTWpc_s9V3FrPizxyRYBFzwUtj1lApcN9b2EP54J3SCyZ9TKC6UY6OctquVjXnXauqnm6rZOoQfkWmdj9ZPG0ajVgYdUis2opIF7WGWfFAA9URm0LWKT01NYvtn1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🟣
سوپرگل لیونل‌مسی از روی ضربه‌کاشته در بازی بامداد امروز اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107400" target="_blank">📅 07:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107397">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PiFotpqCHqbTFLWmJlgFnKjgcT_OWoCru4LdG3yBCuJAg-zTomyv9_bYYLavlGgXNRS4h5XCPpSGFiD-4gt3vf1bZoRkBVIabYiPyygxI0b8uCazE7yKvN8fAyTL5qkMChtYh_UkvdC6V0O1Smi_OHqCGU0lgcafbq7wTWmaggbILOso6t5rONtZNXR3SgHRDitQFvaGP_Kq8kRP468VV940u3GM3-5HWdKLpakuRwi0PVgSf1tBJEstzhJ_xGsWpigQ7YUFrGvqw5grse1ruI54m-25ESaFHAKP0hIYI7Pgsd4szWtfG5m2dnS11aACKIficuhlTd8hz6ORuog7vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
ژرژ ژسوس در مورد نيمکت‌نشینی رونالدو
او می‌توانست در این بازی بازی کند و مشکلی نداشت، اما احساس کردم به بازیکنی با ویژگی‌های متفاوت در این مسابقه نیاز داشتیم. این به این معنی نیست که او از برنامه‌های ما خارج شده است؛ ما قطعاً به او تکیه می‌کنیم و ممکن است در بازی‌های آینده نقش بزرگ‌تری ایفا کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107397" target="_blank">📅 00:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107396">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhHODdyyettf3k0MJfxnZciG6PY5H7333KYwd3wxl5HHtvd6yfybL5lvn4mNhc3fHygK5907h3HlUdUyE9vSKYO82ZLJ6E_k8HbXWJpdLGWwHgA4FXQp4v8iYBKOVUyPV84ajIc6yBsmRGolrAdnfV0psO0UFIsjOjZXkM4flbPzVJVzMc4ZWuxi6WhEUOwSJH4JH-3nfoMzzYYfUYzgtcVkZwqBfBBnCPLuyRd-Nr9QrhnN65gElXsQLeMvAHtd86IvEz0iOh9im-iAgW95GWQUqdUtL4pAqgtSscrfrPL25bmHWlBWiIBxd4v3LQg_vgzPp_BfWWJuRN_8L0FyDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
❌
آلمان تحت رهبری یورگن کلوب:
❌
تساوی مقابل هلند در اولین بازی.
❌
شکست مقابل یونان در دومین بازی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107396" target="_blank">📅 00:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107395">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCsev8p8Q_IdLQOHzHMqvxt_lkJEXPWqRftIfQkYuyY7vl3Qp-L4J9dv6J-3pPPP8qBAk0DdNgzmGyWIvAI0DkTHh09ulFTwIPZIk2p6ulyeYMjJirLJjdK_NJpSgJCtPF5_UzTmZLfj0n8N4iI6SrhyMELv6h1S4cDqUrlpE1ftEk5XT6llxFvPPuxo2_C3bHOjeROGuOuv4qC5rFXP_NKNVMcSJVczUloXXcuLAbWoloCR7SA3Uny0V9RDqcbRS1J0kJLdaAaA15CNFZKkQz6MJPH8C2iY94x1TfGF5UF9Ur0hSENNBo1-3gRhm6rKJwSWGEHfKozTLt1Zc8GTNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🔥
ارلینگ هالاند، [65] گل در [57] بازی با تیم ملی نروژ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107395" target="_blank">📅 00:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107394">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6P5BIkE-JhQa1HUCBnn219Nr0zplK8vHN7LqD4GU9EazSJa1dn0ac0TKl8nMlTIUC9AWHjbtQQko_D0Be-BbnSfQg2GDdrj64k27NaimgL8RjH5EjoEX8Kr72RnB2pAKs1XBB1hHy_xgSJMFrsLgcoq_dnhYGZz_a72pKc9blMAajC4T7f6LsfpCzXFU3RbjXIagph3rqiJSQNf90uJHo0NwbDYM3gXH9EsIGqB686ssmAgo4yRkcjog3-UBwa0VgTxeKRz_MS8aKt_DaZAnTAllGz9rM-OU_ElKdwaGc7Y2FM--YD9qAmHFMa9LoURF3E_v2JQ9u-VSF-vKBcu4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
کنایه معاون فرهنگی استقلال به پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/107394" target="_blank">📅 23:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107393">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHm51XKbWnvIEUPpbd_mq80t25ztNDpJ0OmbulSmLfSgVRQvJMtbGVYSqB49MaJl-AYD3RVYSWEHyJaiQcra1sg5uPqXgUa54u5OaGL91ZK_QFKlCGgDEdzfu5IBMH1mIomV0WdC8Qa-J_hdIdqUBHwIiLNLEkIlY1d7FST4kJ6gAQGCniF9aIDzpZEvyuKkREmvU0OMPAeMu85Sgn7-LImbQyTSuLhJmBCiy6st8luMCgdD0EVbpyHZDv__EjlYICtktf3kKI3Iz21MD2NNEvrrvxHDMZMWqjMZFjvjgs8P_ub7xSfbGZPNao5bwTs6kuYbQxwXM_hqB8u06nYcWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
صحبت‌های تند زنوزی علیه سرخابی‌ها؛ جام در منیریه زیاد است با هزینه من یکی را بخرند!
🔻
تا جایی که ما به خاطر میاریم، جام قهرمانی رو در زمین به دست میارن و نتایج مسابقات باید تعیین‌کننده سرنوشت تیم‌ها باشه و شایسته‌ترین گروه جام رو بالای سر ببره اما متاسفانه…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/107393" target="_blank">📅 22:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107392">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qh4XytGkimc87TLVx4Wp3820865Gf8ZNeJ75-G4DK4MIblAliRdIRUou6aVu7v0aL2wjHBK3ZsUgtU4Wn9AwZnaArUkz4U8acL8pXit4LTWmHmWAW6LVFp1GPQ9aCF11lXO73rRNbhreslOfhnKwoEbaMxYduKJnaUzkUH-mWqIB1Fmwrwq53ikydPQ2LrOUJTAvh563cz3FxfkiTmFx-ygHGgAnJKNpbBR3lb2jmr3Pcli-f2CxPQcPMaOtCzErjZs-ddBjuH9qwYv9oZ5v74R2q605djoqFEXLrrnDRQA-MUKOSz1Cx1HVaAiXE8z_f8P6e3E_AIg7f1WByGF_-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
امیرمهدی علوی سخنگوی فدراسیون فوتبال: من نمی‌دانم چه کسی به علی‌تاجرنیا گفته که جام قهرمانی را به استقلال می‌دهیم. هیچ‌ بحثی در این زمینه شکل نگرفته و صحبت‌های مدیر استقلال برای نمایش است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/107392" target="_blank">📅 22:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107391">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADEdyUnfNeo2yZdZYjJQYcsL1iD_O-Pg4jhA_dNIY32Qvm-32qesl27iVovbcQyi1vtp8QDOC2y3E7QYd0EH_QEE2KCkMoUmkKmkXs6qgXNBLIC7_ke5ra5nEsHEJdqtsEO9k2n1xBXd6QXXlhiSXrYtMcjaCgLFtEl9TNx9peLjyKyt4XA5qZdCRtauH4i5C30b0Ld91MKPtYQVKK4gx0UXcNK8_8TVbsbQ78Yl1EHpgioAcWnbhCd-x0ugMJ-oo6k4VWs5FuFNlAj-p2G1qZ79BJPcDQeYBE3ldX3m5jVxD8Wd_tXWOtPak4HW0pmGrXI_lbKEnKjyH5Jx1v2dfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
کنایه معاون فرهنگی استقلال به پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/107391" target="_blank">📅 21:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107390">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWkFA6pct-gU3m0w17r-FtdTOLbs5vO9Bg_2_CwSlxGRLqa4Z63M-5ZX3rrLg_XyPMi5nZMoCjNVKHAtSMLDoRNV74JZaiagF5QOPArXfKeKsrqqPS92May6mtJ1IWcT3ScrN3bzD93SZzcu1n9Gy9NxhdCYoik74x-01ih11VGl8LX_CFrYljRMVvupF1TRrrgh_CGoGeG0Fp1VVz-puOkbEplJ9BGC6TBQjYGoLdqyOpbuagaid7oax49dpZLfyduOs_hUFlRLlWe6qMdxporFVearoup-cj1i-g52n-_GdHCSR20LT6zCnHovkWN1_6AD8iBlkZTH8vq6DnXmSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
رونالدو روی نیمکت پرتغال مقابل نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/107390" target="_blank">📅 21:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107389">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2062dc3d8.mp4?token=vWuDAp_ZTC9YlWeIxR8BMSLQnkv57e_wkviUyKcGLzpDMq1TMvoePy5He9wJW1DFxTsdwqp4mAxHt4ImPRb2sS1E1e8g6mKDOLuK7k8q0CPzZBnl0otj4VeGQSbDA6nc1vwcQ6LHrMDFArsRqMM_rKrFpdvdStf_caxJiFjj6GhBFcNzHCfIH29-x_V18juyb6my0Am6m5icp3RecglryRDNI85BfdGmPJd7XD2Xb5F5EmTlRRmQ_K91S24YGNrBkvyN94K1qQhDeC4E30W9xuKQobO30UJoLlrma0EM69WnBDmKu3tHAtIma-bWDi2rqncNX_6yShVakAgawcFVow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2062dc3d8.mp4?token=vWuDAp_ZTC9YlWeIxR8BMSLQnkv57e_wkviUyKcGLzpDMq1TMvoePy5He9wJW1DFxTsdwqp4mAxHt4ImPRb2sS1E1e8g6mKDOLuK7k8q0CPzZBnl0otj4VeGQSbDA6nc1vwcQ6LHrMDFArsRqMM_rKrFpdvdStf_caxJiFjj6GhBFcNzHCfIH29-x_V18juyb6my0Am6m5icp3RecglryRDNI85BfdGmPJd7XD2Xb5F5EmTlRRmQ_K91S24YGNrBkvyN94K1qQhDeC4E30W9xuKQobO30UJoLlrma0EM69WnBDmKu3tHAtIma-bWDi2rqncNX_6yShVakAgawcFVow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
انتقاد شدید مجتبی جباری از داریوش شجاعیان!
مجتبی جباری، سرمربی جزیره قشم، بعد از تساوی برابر فرد البرز، به انتقاد از رفتار داریوش شجاعیان که در دقایق پایانی بازی در نقش یک مربی به جباری مشاوره می داد، پرداخت و مدعی شد هیچ بازیکنی حق ندارد در کار فنی دخالت کند. جباری همچنین خاطرنشان کرد حتما با شجاعیان برخورد می کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/107389" target="_blank">📅 21:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107388">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJ0bA3QmZ9yDkMxBGFTCaIY1SE-yj_ahXzCLS0p7UbaRy2C4bsYaGpe3QABDyLpdtoj7eIwTA9B4XmZbQfM449tEZnw98O-vtC-oTFj-i5fvUMlYB3-kMrUDW5B1NRw8N2LsOfp3fmCdb98O1ZkmbvzGYBmx1Xdt9aHWqdK6VzsW0-9pXmvl0_daZeHhcYa7RwBGaGdwP6svwxHPsK_9CVOHLzyIJZTh3_WIlybausw6Cx9mxi6orVhCaN08UqUM38WwJf_jFw9EzGBod5DKl8b7xawHO_CTuQ-p_OnCMBvkrFJqPj_3sZjLrTn2wwu_a9QbNNneNUpKE1wHrZSNeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
🔴
استوری تتلو گونه‌ای رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/107388" target="_blank">📅 21:05 · 05 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

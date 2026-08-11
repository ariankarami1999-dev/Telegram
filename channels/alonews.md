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
<img src="https://cdn4.telesco.pe/file/TF5VU5EXClRNOWjcIzWzl57iqYxUzwjq_8beCc6MU455pTd7H9xnNvSAP1AJWQIz_H-jrEzaUp525VoHVKoFf5jpa9VxSV7Yq99avX8acNk5q4CFG7k9NsTZzSZSeS3LpVubPU00PJwBNWcfEW-7ULPudr4fWCTzkFPZtw8Ttapi5jS2_5rcvVvBhy_9ov6035OM9gW-z3gOuG14cO4NMEWaRvQdEnC6wfE_vi8xyRjUQWl6ljjcCTCoFoAU0oqMxiOSiPXZ5irapoGKLtJhlEZ9B_XGOU9iInnSgWK5pxoie1O7aK3krUu72y7PIePwTRZ6wfV92TVKwTKAozgC2g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 968K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-20 19:21:46</div>
<hr>

<div class="tg-post" id="msg-141179">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
محسن رضایی دبیر شورای امنیت ملی:
شرط بازگشایی تنگه هرمز، پایان جنگ و آزادسازی پول‌های ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/alonews/141179" target="_blank">📅 19:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141178">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJI7LI-sBid1vnYe5v4T2z81TweFeMlB90YmgGiUXc_LGSEynpLonat4pVa_VaObg4mJ9NurZ9AnsAdbZI3Kg8k0_n-mINKDX77yVqBSYNkb71_b6X5joDOhrydsEcryfWVrgyNP-9Fe7PG8VzEFm9UTpQeTDHA2RX9ei2eJmXDRz7I4GJxv-s1hLCD9Lpb3_zwLliGmMp5TVZkga6QmtnesgPc7172-HuQvo-n80RqTQO5RAUeMY264ECsObQ3N-6Gpez4JFijPDevpST3-8WSxIoG61fn_NU3ugUuC7lxi7Bg9txdXf_0u2gxEDVLTU-tZwpWIvCbS3WxsmP29Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجری: شما از آینده هوش مصنوعی نمی ترسید؟
🔴
پوتین: من تا حالا تو زندگیم از چیزی نترسیدم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/alonews/141178" target="_blank">📅 19:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141177">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e386169ba.mp4?token=OmwX6l5TyoFL_rhP1nc5VKWxnSA3xhZv19E3CzhVXUaKGOu8vp8n2d0fGMkuAVj9NfbHzZDAuHD16Cy6T-j9N5-5BLrGYfgJYUIYc5NLPfIe6dW2T0HbKq8Mh5UxoihnyNcH6fdkof2_zZcmUPvP8WJucEYtVqZ8b9Nj5Ad8XMeuV6vUy6jaELreu9uJnxUUaCZe3qcplg94Ku91CqFH-6wDbW3WooJpE17Fd_8bLLjhsCDH6pYwpS9LX__OWSEhIhCDnH77s8wWK-22LoM3WX5ZRee93P8Xpz3lrgoWcygzHvKNm0dCeHWayzCOIJ99D2tqZuqgwOQNA9SfZYCLWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e386169ba.mp4?token=OmwX6l5TyoFL_rhP1nc5VKWxnSA3xhZv19E3CzhVXUaKGOu8vp8n2d0fGMkuAVj9NfbHzZDAuHD16Cy6T-j9N5-5BLrGYfgJYUIYc5NLPfIe6dW2T0HbKq8Mh5UxoihnyNcH6fdkof2_zZcmUPvP8WJucEYtVqZ8b9Nj5Ad8XMeuV6vUy6jaELreu9uJnxUUaCZe3qcplg94Ku91CqFH-6wDbW3WooJpE17Fd_8bLLjhsCDH6pYwpS9LX__OWSEhIhCDnH77s8wWK-22LoM3WX5ZRee93P8Xpz3lrgoWcygzHvKNm0dCeHWayzCOIJ99D2tqZuqgwOQNA9SfZYCLWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو : این منطقه جولانه پرچم اسرائیل اینجا به اهتزاز دراومده و همین‌جا هم باقی می‌مونه، چون این سرزمین ماست
🔴
امروز این سرزمین متعلق به ماست، دوباره به ما برگشته و همیشه متعلق به ما خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/141177" target="_blank">📅 19:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141176">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a895c6e9a3.mp4?token=dXWX0PNv2nC_lPS3coAtlIDbBWATF1_Esnk6KNHa5mqRQdjTOsVqR3Q_pcEsZ-yPysoejful4dteuC5-ZAop7e_XV0xrIkgu-rffw8s3RTxs0XHJx9MvgRBhZHsTL87Zo3u09tXuV4RThMD0PtJcRCRkik2QVYqMaI99gpciz1y1QXLlid6R9aFlrCvgbj_oEzPtJ2_0ParGJkXNZLbyC5Tl9rNY6BlQAwBDthptSqS84F9fGbk4s5XF-7ACs5YAMGC7PYT83kRZPhyk7MWYW30oFAfXmxlIKjM0eMSDgaVu-qTgimB_QQTD9jfXQfUF6sIunCTXoCYInQdld-pX3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a895c6e9a3.mp4?token=dXWX0PNv2nC_lPS3coAtlIDbBWATF1_Esnk6KNHa5mqRQdjTOsVqR3Q_pcEsZ-yPysoejful4dteuC5-ZAop7e_XV0xrIkgu-rffw8s3RTxs0XHJx9MvgRBhZHsTL87Zo3u09tXuV4RThMD0PtJcRCRkik2QVYqMaI99gpciz1y1QXLlid6R9aFlrCvgbj_oEzPtJ2_0ParGJkXNZLbyC5Tl9rNY6BlQAwBDthptSqS84F9fGbk4s5XF-7ACs5YAMGC7PYT83kRZPhyk7MWYW30oFAfXmxlIKjM0eMSDgaVu-qTgimB_QQTD9jfXQfUF6sIunCTXoCYInQdld-pX3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت مردم پاکستان بعد از توافق مکه با عربستان و ترکیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/141176" target="_blank">📅 18:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141175">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
سوریه اعلام کرد آژانس بین‌المللی انرژی اتمی به‌زودی از دستیابی به «پیشرفت قابل توجه» در پرونده هسته‌ای این کشور خبر خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/141175" target="_blank">📅 18:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141174">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
شورشیان نیروهای سریع‌العملیات (RSF) که از امارات متحده عربی حمایت می‌شوند، در کنار جناح «مجلس ملی سودان» (SPLM-N) به رهبری عبدالعزیز الحلو، شهر مرزی قیسان در منطقه نیل آبی سودان، نزدیک مرز اتیوپی را تصرف کردند.
🔴
نیروهای RSF و SPLM از خاک اتیوپی به عنوان پایگاهی برای عملیات استفاده کردند که به آن‌ها اجازه داد به صورت غافلگیرانه از مرز عبور کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/141174" target="_blank">📅 18:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141173">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
تسنیم: درگیری خونین در ناو «آبراهام لینکلن» ۷ کشته برجا گذاشت؛ این درگیری پس از اعتراض خدمه به شرایط نامناسب خدمت، کمبود غذا و مشکلات بهداشتی ناو رخ داده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/141173" target="_blank">📅 18:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141172">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
فوری/ترامپ: ایالات متحده می‌تواند به زودی با قدرت بسیار زیاد به ایران حمله کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/141172" target="_blank">📅 18:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141171">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmeIXtyH7pQ-uJX9JAGVo5VmapaTINaMjE-2vizyL3bN8MF93mciVeoHgr2tXY_rb1mnqmpzhG6lCVX3sTnSKYKzPFUyklRFF_4-01jS8krWyfvbimpZdQLL4eOmlEmpdGrcfcjSFkM11gUP3tm5ApUPyHNHHXIAildOQStG0h2DT_D70FtnL56E2pguTEQ0gAhL2ThSv3mdneLVLiaDrO5NbGfIsurqRiy0Q3VtGjg3I4E__FdoFJOsiMR7cigtooHK7NAk0V1yg35c7MADGouRFDH_DWtDX0f9vKYYpWQLE4yxF5l70KEhiMjGndxFCa5MBPjynbPf2v0FKOdKig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس جمهور لهستان: صبح بخیر ایران عزیز!
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/141171" target="_blank">📅 18:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141170">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
فوری/ترامپ:
ایالات متحده می‌تواند به زودی با قدرت بسیار زیاد به ایران حمله کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/141170" target="_blank">📅 18:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141169">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
وزیر کشور پاکستان با عراقچی دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/141169" target="_blank">📅 18:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141168">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5ASlerZ8958kGuoqlbTBtONbyRzsxLyxsXFRnw2dNofDtyS_feyxxKecHW7VbjlkpUx-whWuF0-FyshXhVOb0-dhWLqVYULLfdE3DkdN1YcW-Ylx6b0458J_HK_pV_rdO2zfpVwkv1jLzpj_MPFdIhdWB7dhgLu_Pwuu8CmkAkb4iN099zeySZcNkEpImihbhtEJHKE3Ui82Lw_wscvNXz27NCvqHOpjJIIkJAQeR9dUx91qH1vg05BXEhZrlTKtT3xlu69FzaWs1Kxgxh9DGECEmfvTwidopeIdtVPwvsvRGSLQcsC4W0nwuFtcMIVayUVP_SJnRr0BknVgZUKKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
می‌دونی طلا و دلارتو کی بفروشی، کی بخری؟
می‌دونی چطور ۱ میلیون نفر پارسال ۲ برابر تورم سود کردن؟
📈
با اکوتراست
✅
همین الان ثبت‌نام کن، تست شخصیت مالی رایگان بده، تا دقیق بهت بگیم توی چه بازاری، چه زمانی باید ورود کنی که بیشترین سود رو بگیری
💰
⚠️
فقط ۵۰۰ نفر ظرفیت داریم!
👇
سریع کلیک کن و تست شخصی رو بده تا بهت بگم چی بخری و کی بخری
👇
https://storage.ecotrust.ir/marketing/landing/index.html?utm_source=ArshiaYar&utm_medium=Telegram&utm_campaign=sinaps-marketinglanding-0505&utm_content=Telegram
Alo</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/141168" target="_blank">📅 18:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141167">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: می‌گویند «آقا بروید صحبت کنید»، اما طرف مقابل با شمشیر آخته آمده؛ نیامده که بگوید صلح کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/141167" target="_blank">📅 18:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141166">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ترامپ:
ما از رویکرد ایران در مذاکرات راضی نیستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/141166" target="_blank">📅 17:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141165">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
دلار 187000
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/141165" target="_blank">📅 17:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141164">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MW4tGC-WZEYNIDuPGlAfRe2NTRRd3f_Zk2TGtaipOnOOzvGxhzsDvqFHahyQ-YfL8w3dspPE20s23_6wyMGzeRLIYw_toiuEfsugR1OHrM1_069JVyDj3mRht-uPBSNBoyqkODhUcQwjrmZvSgepIolsSt1qLoJKelDxe19QGWMpxhCJbTuP6apoaYr0yQCYzD5ojs43oyGXkc0GigP9t3SY1rhFMpwlzNlb5FG3wNH_h01Ub-69H71YWt-Lw7ZZnmNzOkuS3y4ZK4mo5aaKE1s8CAowGGvj6Qx6YvUk7OM1nQlKmR1iPj8jjJfZvFPvCi8NHzCof6XH7m84rR538A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زاکانی: وقتی بیت رو زدن، خودم رو با موتور رسوندم اونجا ببینم آقا چیشده
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/141164" target="_blank">📅 17:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141163">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9676b05e8a.mp4?token=ZHOJ4ZL_ckUIakSmnnvDSWl9mFydJnyibtSLdmgKqRX7xKybf5MeMWFDAWvNCL5gRuxdtsLmTuqRYOL2LxkfmWn4nmoCwjld2ru8S6auW3nS5CTiq8Hr7HriiGfwiIRNfjZqiS2vxjVJMgXsny8IfuKgDK2Xn9k1TWIerFsRf-HQ2k01j_s54zYWQfxwBFrirbqMS5vudW4ke0Hv6eC7kl7Y94hGxLdERvDVBukEuLcA6nr4Mf2hu67cW3qv6I5Tg4Eja34okMeAaopMxFqq5lRVuO9RMC6DWHUjF0JCNI6Er4CQx8HLbJPNGyZLq2WuZ0XG2agQM3zwHXpqi6HgHg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9676b05e8a.mp4?token=ZHOJ4ZL_ckUIakSmnnvDSWl9mFydJnyibtSLdmgKqRX7xKybf5MeMWFDAWvNCL5gRuxdtsLmTuqRYOL2LxkfmWn4nmoCwjld2ru8S6auW3nS5CTiq8Hr7HriiGfwiIRNfjZqiS2vxjVJMgXsny8IfuKgDK2Xn9k1TWIerFsRf-HQ2k01j_s54zYWQfxwBFrirbqMS5vudW4ke0Hv6eC7kl7Y94hGxLdERvDVBukEuLcA6nr4Mf2hu67cW3qv6I5Tg4Eja34okMeAaopMxFqq5lRVuO9RMC6DWHUjF0JCNI6Er4CQx8HLbJPNGyZLq2WuZ0XG2agQM3zwHXpqi6HgHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قیمت خونه و برج توی فرشته تهران بعد از جنگ، متری 2 میلیارد تومن!!!!
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/141163" target="_blank">📅 17:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141162">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18584c6055.mp4?token=nflgKyvfHweCTYSuMbzSWCsmXu9eyaFo_K4dRQfOobkDyPqmXsW8EV-OxEQzzaQDWi7txlxMrOUvDHhm9eIrOCib4I_FoY_xyYxaAK-Gx4LcV5VmQoNzAQc7hDZ5L4c1yLWVaRjiyRwvHOAR6nsbwybxC3KUl9rvFuqLUgf95oAAXOvpCD_mbpkgjNoghSSaK8eVNWdTOnez3IRXGhdfl6wV1ldOhCNTXoIOKsAWmPmNtki9L6jvizPlchEd74BHvMXa6KfSycO4aCHk9H-ftITrly_ND40hBWCUzTwiq6wJETIKzqIkmyeVkw3lLNLHb-2Ntj2n7jWGxmVfW7nlYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18584c6055.mp4?token=nflgKyvfHweCTYSuMbzSWCsmXu9eyaFo_K4dRQfOobkDyPqmXsW8EV-OxEQzzaQDWi7txlxMrOUvDHhm9eIrOCib4I_FoY_xyYxaAK-Gx4LcV5VmQoNzAQc7hDZ5L4c1yLWVaRjiyRwvHOAR6nsbwybxC3KUl9rvFuqLUgf95oAAXOvpCD_mbpkgjNoghSSaK8eVNWdTOnez3IRXGhdfl6wV1ldOhCNTXoIOKsAWmPmNtki9L6jvizPlchEd74BHvMXa6KfSycO4aCHk9H-ftITrly_ND40hBWCUzTwiq6wJETIKzqIkmyeVkw3lLNLHb-2Ntj2n7jWGxmVfW7nlYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محمد دادکان: چند دهه حکومت کردید و نتونستید کاری کنید خب برید دیگه مگه ارث ننه باباتونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/141162" target="_blank">📅 17:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141161">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF):
کمی پیش، نیروهای IDF یک تک‌تیرانداز از سازمان تروریستی حماس که در منطقه خط زرد، جایی که نیروهای IDF در نوار غزه شمالی عملیات انجام می‌دهند، تهدیدی فوری ایجاد کرده بود، شناسایی کردند. بلافاصله پس از شناسایی، نیروهای IDF برای حذف این تهدید به سمت تروریست شلیک کردند. اصابت شناسایی شد. نیروهای IDF تحت فرماندهی جنوبی طبق توافق در منطقه مستقر هستند و برای حذف هرگونه تهدید فوری به عملیات خود ادامه خواهند داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/141161" target="_blank">📅 16:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141160">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdTIHbJGXsVID3vV5fWcL3xAazp2XNqRW5Y9yi3kcYrfxLRoetz4HE6-9NTjH_mJxoLNpCmT_bfCOszI8qAOpWUIAn39w0-pcBvEp61eHk6lo_Wn0ECFnc1eFE5yuvdIS7iJZJmxv3TJrlhdP9tBTkd8g366VOBLjwDp6me7tIJLVmzU9zkCwB2FuLw8qz20M2ZvGIF1XVfMtakjnL2hCRCcKKUJeYbcvOx0OvDfJ45dzlt1oGQIkMNh5Um8qKT1tlC1lkZGuQYM9GS2cHYc4Fpu-3HhGoafUqwk5npMer-a3Uy5sPUt8xQMBU0bn13VbesS8ALwzPKLZn1EDE4IDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علم الهدی: افرادی که می‌گویند جنگ را تمام کنید، منافق و عوضی و بی عقل هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/141160" target="_blank">📅 16:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141159">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: تمام توانم را برای افزایش قدرت ایران به کار خواهم گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/141159" target="_blank">📅 16:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141158">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoWdZCJEmmvyzQ9A_fLWBowLA4i9Jkz_j5UiPxCRZF0v6G6x3IBFL0Aeb3HfE_l-8dKcA1_X-Wfi0he93PDBiCQIZnzdVbIO9QhhlWgJLwLCeGqzvO23JwefPWunoxLet9EE9Vtrqn03d6ClbttvOXFD3T_k_3fCRU7c-UM528aoDd1kfGaAGQmpipz-OqHIAuJOjnU54UQd-SBWYVgByzWYo0iON56--PNRZCc7oUsbR2NAVlaY7saCHgb6Xh_RZyFcqyO4VKPsWq1hVu0YywTGxNHo4Ro14ReGJdqJpJI9-GA1lY56hdEYyUJNCAXfRali5dXgHV0ByOyyywupSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: تمام توانم را برای افزایش قدرت ایران به کار خواهم گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/141158" target="_blank">📅 16:27 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141157">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5-x8vXGmCaD789yGhLW9Zc5HK4c0zFxfSWULC6CdTVc6I9us2nUOntfXa1kcGVX3iaLtNVr5hCrb6KBpF3MBMDQGRDm5zp0q0NBszONCswzRAbL7y1G3Sn2Ueskq7G4EYXjGElfLLecLftsqAfZX0VQaCPHP8rqOq8Rm33bzL9dIkoiclsZFSzi3awiYufmW6yyNs4i6DO5l3_Jr4iNW30OhLvKFuh0w9yJJFeXtqlUYGA737JOPMocLs6-pl8QB-0aUsDYTrImvvVQfUbrSlKAZL6fSbGN1BYaWwHtUQp3fVuj717IMbe5hVgHk9y1LdcD0N9Z_LlKdakVaDd3oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مهدی مطهرنیا:
اقتصاد و ارزش پول ملی درحال نابود شدنه اما برخی آقایان در توهم هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/141157" target="_blank">📅 16:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141156">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
وال استریت ژورنال خبر داده که نیروهای آمریکایی امروز به سمت یه کشتی که با پرچم پاناما حرکت می‌کرده، شلیک کردن. ظاهراً این کشتی قصد داشته محاصره بنادر ایران توسط آمریکا رو نقض کنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/141156" target="_blank">📅 16:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141155">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdiQx4esSFkEL0e10TGYfpaeZiihfNRBj-YXdTriOu6VQOzZiqo6aCyqnUzzpjy1S_7ttYCx2tPxfL30R8lR5-DwtMcyCLNycu7kpLNevsL80JQ8HVSmMnL22TDX3yM8tYCWhji5ZcaDuP8sf0Ooe5nlLdcqivcj_3tW3NrIS1sTT3uNwLopCffrn1nNdl9XxpZEQvaqt6-hAqFTl_yx0yavuZo5pgiXJcdMKfitr5gbtCDvalud6jR7gHy6Za_nP5EY-FYvhRIf_mIWKZ9TPHU12r_iutD4JoFxrUa-7ARwVtom-fe3z6Q6O3fiDIlCWcoOfykIASDepvPJJ62WFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فایننشال‌تایمز: پول و نزدیکی به اسرائیل، نفوذ امارات در واشنگتن را افزایش داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/141155" target="_blank">📅 15:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141153">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
بلومبرگ: پاکستان می‌گوید ایالات متحده و ایران به توافق در مورد صلح نزدیک می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/141153" target="_blank">📅 15:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141152">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b38gIVD3xxX8FTmQKxihHQGjbmx01iyxL-RzIXjBI8PfMR2z75ZjvnpsR7ulhXo6tdLkXqY-OyNSQ1SB5IYVeYfQ5s_TfVViNbmb6Lj1gY47kHaZfNxM_4rW7s-HoPtXmFs9mxGEjrLEGuGjPRgOOny4ML_GjF2pv8R-kYdUf6wbN7TBnCwsfDR3v5Z44Jbcmlujmf-ggqMUFRl8tPuMiSObhks-L669Qe5q_YwliB-4oQi1ziGjaHna7a_f8axEbfW0h2B7xHveGporOIM_iwRkMlmqP2t1wMAfrsPNATQw928fIwVWSDTbBQvxdr7DfvJkeOSz8lORwrvV218m_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آتش‌سوزی در کارخانه نخ اطراف بیدگنه «ملارد»
🔴
دود مشاهده شده از آتش‌سوزی در محدوده بیدگنه «ملارد» مربوط به آتش‌سوزی در کارخانه نخ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/141152" target="_blank">📅 15:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141151">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJLtCTbtT5bSH4RyZTYdn0S-lHHz5NRvkC-9YjXWdt7M1OoMtADTv4fnCT9pW9Vji7o76UUxWDNbXHNXo5ypl_lKBm5pz6swqoEbuXMiVqgmzkbSuSOmweJt-FsUXeC18YRIl99zPY5JUk-dcLmd68xwAvM_nO70R2MD8GTxE9t0gC_ZFrPsJB_mfQCATZcKw79CO_-h93EpEOhDLU2ttPrfg65chhuP1riLZeWdlAHZZO-Oo7JKG6Ix9zMjfBqV_aQMaKKfYxTTVlRsqpR_CYJhUBUCWW8ZnhhBQADTHHBBnnd0YVnD2sl3-xBzxqmoms3jr9ULifXe61TmPPLWkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای دولتی امارات متحده عربی از ابوظبی به سمت تهران پرواز کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/141151" target="_blank">📅 15:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141150">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سخنگوی کمیسیون انرژی مجلس اعلام کرد: افزایش قیمت بنزین فعلاً منتفی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/141150" target="_blank">📅 15:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141149">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
اکسیوس: دولت ترامپ با سوریه و اسرائیل به تفاهمی محرمانه دست یافته که بر اساس آن، آژانس انرژی اتمی بتواند مواد هسته‌ای باقی مانده در یک سایت مخفی در سوریه را خارج کند
🔴
این پرونده طی ماه‌ها و پشت در‌های بسته، با ترکیبی از تهدید نظامی تل‌آویو و دیپلماسی واشنگتن دنبال شده و به یک راه‌حل رسیده
🔴
دولت بشار اسد بخشی از مواد هسته‌ای مرتبط با پروژه راکتور مخفی «الکبر» را در این مکان نگهداری می‌کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141149" target="_blank">📅 15:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141148">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
وزیر دفاع پاکستان: ما به دستیابی به توافقی در مورد نوعی ترتیبات بین ایالات متحده و ایران نزدیک شده‌ایم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141148" target="_blank">📅 15:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141147">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
وال‌استریت ژورنال: آیت الله خامنه‌ای با تغییر مقام‌های ارشد امنیتی بر تقابل با آمریکا تاکید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/141147" target="_blank">📅 15:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141146">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
رویترز: بعد از پست دیشب پرزیدنت ترامپ و درخواست غرامت از ایران، به نظر می رسه امید به توافق بین آمریکا و ایران در حال محو شدن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/141146" target="_blank">📅 15:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141145">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8efdeab47c.mp4?token=t4SSQwsVR52l9b4sPIgF82svAJJrJ0tYKAl1Rt_BjiX46PAMRRkMUkTtyyNmXwWxz2COyXgTm-_1v2Z0dMIa5cAf6shanzEOeugb3WkgRNEZCAycIj2lMqTVFii1HR2DCmlp1LWcDqnpsVgcyGLEy74aLVryjL6PMyKSKWIBfny_TZHme5x3QQFPR8B8BBva8PUQek1_g0Hfp2tdDcyx--7WT2PwpsU-MF6cQraaDtYChBYgcpIROi0jMClxdfyLVGK0P9f3q4dJQn3jsntaKo3hraHhU3IB8bYX9WyMhnxL7HMXba-neLM4kpymd2viCR25b3TWXJ3Whgq44Rb-ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8efdeab47c.mp4?token=t4SSQwsVR52l9b4sPIgF82svAJJrJ0tYKAl1Rt_BjiX46PAMRRkMUkTtyyNmXwWxz2COyXgTm-_1v2Z0dMIa5cAf6shanzEOeugb3WkgRNEZCAycIj2lMqTVFii1HR2DCmlp1LWcDqnpsVgcyGLEy74aLVryjL6PMyKSKWIBfny_TZHme5x3QQFPR8B8BBva8PUQek1_g0Hfp2tdDcyx--7WT2PwpsU-MF6cQraaDtYChBYgcpIROi0jMClxdfyLVGK0P9f3q4dJQn3jsntaKo3hraHhU3IB8bYX9WyMhnxL7HMXba-neLM4kpymd2viCR25b3TWXJ3Whgq44Rb-ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دود از اردوگاه‌های تجزیه طلب کرد در اربیل به هوا برخاسته است، پس از اینکه این اردوگاه‌ها مورد هدف قرار گرفتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/141145" target="_blank">📅 14:53 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141144">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe411039bd.mp4?token=sOzlHs4aAzyBAaB2rcLTd3wZPvlheBk6cdCiZt1wyXKNT95bfhDpJWOzh0EIgBkRrHRBdNd_oTa6uqw614b0B9qVzkQs2XiGWZE06-8aQOhf2tmXebVbZm5JsVj6jfPdEnkJfXkVj8VSnLVHlHJc1JVIw7Q0Y6QMfN3I3eoHM46A7e0nSVXUsyTSTgsDHRfWNK1xVbgWm9Y2QqCv4lz99isA_FkiUd5TEJcZixnRz6Er6jcwwZH6cOOY49lMl7zOxHSA7BVXhnMq07bs7dDyG-k9ViLVoBVlcqZCPEzEGuR0MijbgrKJ2NtzUvGsaB4bO612UwcwFaffZBoUV29HQ1-abAN1VyQy81Kw163BDFPPZdaH6VyJEvpxFoFr2Usx7uhABhtdshvtcjvWb7oitc0prbouEOIMQfpZPe6hoIRF8caOrrB-JrXhJUPmvs9QL-aOn8D_8OeKwMJf7nsLROetQ8sPTUrZQQDvQMChkCY0gv3vzrC1f7ibPvGnei2d6C1o2-PbEOzdnHlyn8Mz0WEisabMpyNyucL7mcoUPR5gImG_8D9RiPWfW9wab-GTsp5jou-wSrgvhZJhv051DizLwHKq5dMpa_N1FP1EkSH_ouSeuuHkJIKko3l3iEUmibgx0-cXLultGZQdO-DDBCRLlZMmpMZLWeMQefEdMPI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe411039bd.mp4?token=sOzlHs4aAzyBAaB2rcLTd3wZPvlheBk6cdCiZt1wyXKNT95bfhDpJWOzh0EIgBkRrHRBdNd_oTa6uqw614b0B9qVzkQs2XiGWZE06-8aQOhf2tmXebVbZm5JsVj6jfPdEnkJfXkVj8VSnLVHlHJc1JVIw7Q0Y6QMfN3I3eoHM46A7e0nSVXUsyTSTgsDHRfWNK1xVbgWm9Y2QqCv4lz99isA_FkiUd5TEJcZixnRz6Er6jcwwZH6cOOY49lMl7zOxHSA7BVXhnMq07bs7dDyG-k9ViLVoBVlcqZCPEzEGuR0MijbgrKJ2NtzUvGsaB4bO612UwcwFaffZBoUV29HQ1-abAN1VyQy81Kw163BDFPPZdaH6VyJEvpxFoFr2Usx7uhABhtdshvtcjvWb7oitc0prbouEOIMQfpZPe6hoIRF8caOrrB-JrXhJUPmvs9QL-aOn8D_8OeKwMJf7nsLROetQ8sPTUrZQQDvQMChkCY0gv3vzrC1f7ibPvGnei2d6C1o2-PbEOzdnHlyn8Mz0WEisabMpyNyucL7mcoUPR5gImG_8D9RiPWfW9wab-GTsp5jou-wSrgvhZJhv051DizLwHKq5dMpa_N1FP1EkSH_ouSeuuHkJIKko3l3iEUmibgx0-cXLultGZQdO-DDBCRLlZMmpMZLWeMQefEdMPI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خوشحالی خانواده برخی از کشته شدگان درعا از حکم اعدام عطیف نجیب، رئیس سابق امنیت سیاسی استان درعا سوریه
🔴
همچنین احکام اعدام بشار اسد و ماهر اسد هم به صورت غیابی صادر شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/141144" target="_blank">📅 14:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141143">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
وزیر ارتباطات: در جلسات محرمانه، یک جمعیت اندک اما پرهیاهو می‌گویند اینترنت صرفاً برای ۱۰ تا ۱۲ درصد جمعیت کشور کافی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/141143" target="_blank">📅 14:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141142">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
وزیر کشور پاکستان وارد تهران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/141142" target="_blank">📅 14:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141141">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
شهردار بوشهر برکنار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141141" target="_blank">📅 14:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141140">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوری / زمین‌لرزه ۳.۳ ریشتری حوالی تازه‌آباد کرمانشاه را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/141140" target="_blank">📅 14:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141139">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
یوسی کوهن، رئیس سابق موساد، در کنفرانس الجلیل: ما بارها وارد سایت هسته‌ای فردو شدیم تا بتوانیم ساختار این سایت را درک کنیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/141139" target="_blank">📅 14:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141138">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
الجزیره: دولت ایالات متحده به شدت در جست‌وجوی راه‌هایی برای خروج از جنگ با ایران است، اما خود ترامپ از این فرآیند کنار گذاشته شده
🔴
او هنگام بحث درباره مسائل کلیدی مانند جنگ و صلح، در حلقه گفت‌و‌گو‌ها جا داده نمی‌شود
🔴
گفت‌و‌گو‌های محرمانه‌ای بین ونس، روبیو، رئیس سازمان سیا، و دن کین، نماینده ستاد مشترک ارتش برگزار شده
🔴
دن کین خواستار جست‌وجوی فوری استراتژی‌ای برای شکستن بن‌بست در خاورمیانه شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141138" target="_blank">📅 14:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141137">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
وزارت خارجه قطر: بازخوردهای مثبتی از عمان و ایران دریافت کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/141137" target="_blank">📅 14:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141136">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه قطر: مذاکرات میان عمان و ایران اکنون در مرحله پیشرفته‌ای قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/141136" target="_blank">📅 13:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141135">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
وزیر دادگستری لبنان مجازات اعدام را به طور کل لغو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/141135" target="_blank">📅 13:56 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141134">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TjNkg5jlBsf9wJ6OOmvvFQ5Roxs0Hb-bCmw5_WRNRz2SUE9qMdY8IbftX8zVqTpcbZEm5TYgpsUndXV0Qu7_FTpJC0xnKCyQwt8i0ZxRziX8XQGSMXd8Z0IH4vFEY_y5KFY7uAL6EjsLRuCxo85tpGxLLKdFd9WRLYW8Q-pw5RwOE6aomqIZb0rDNdkHEJ2x2WUEOfWcWkrgnoh8eUam37j6_Lvu0VQxBU1N52ANHQzyuTwrOLFvDx695BcF1w6Ctk7joQhTHhW9xCZN37tVbNVtYtDuOvre3Fe595-jHgCjhVB1fHOrB9AI3kgfTKwaM2XHb3DaRdTyJKpXxcrbgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت بلیت هواپیما از تهران به مشهد
🔴
۱۹میلیون‌تومان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141134" target="_blank">📅 13:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141133">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jh9LrXDjoKvFxxxHzO4IbkpjPYhjZlCdBPSdlHzxQ6uxrw0DTh0pJPExazxIUOUPxdXcJsMuXBEbsblWssuqSzOy_0eETurOjs0aSPv4TjllBlh_vHOAOfxfftzl6ke7BsVXOpkSH8GZkE-34WYT33Se2SXaU1D_YlV2cy7K_gzFcWbe4C1fTlsoS1oDWziNqdXquI-n2jtgPPFXa7nSeC1oC_Kwz6xvSSBbplz4DrUegVAvfkanRwowHvaJmHqgTHlZRsdwkUfBIi3eIIodKOlYBQ-AMP8VfmtWcFKhamg5igFN2TbgMWDBmSYjOvyt0TY1p7YhHE-R0mCLgbAQ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز :
آمریکا دو نفتکش تحریم‌شده رو که قبلاً توقیف کرده بود
🔴
به یه شرکت بازیافت کشتی تو دبی فروخته
🔴
این دو نفتکش قراره تو هند اوراق و به قطعات بازیافتی تبدیل بشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141133" target="_blank">📅 13:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141131">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/naBGltK6Y7oYp1Ie7svEvl2PxlLJyz3swY7J5rC34lZJE7PHwrHlJwqCwKBH3G85Uph9BRlDyoWreDNFI6LDXmnwwX892WZFDjc38o7GRSXWfzXDYOGMiKpz6qWPZKG7KgxPXjKcCF82jvBUFqkWtapV0eRM4wEpbtHsHC1H6TbrsisKBM_5BcRIE8Yu-jbYAmd211F8fcpWYPoZL9sdijbFFShyw3Etl6_dXjvyTE07ZX2jPVh3P3sFq9Pr7zeFR6WiE9SpHgLNOkkwbTZg3B6t5TNZiV4J9tbxCChm_ShEChMSqKRJ7t_rMzHG0eqW0FoOEtg2CR-LBvgDeIUJ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ciZiXse1RAfBfpGP9hKaZm1QYMuSp-wN8UIlZccWleVj5EHQzqyGkRmd7nmH5hRSfOxVCaNYIhUyPI1wWoLK7D_Ugf_9kw3bnWoNhWGZxVGu8_nkOlDXBDW4Z3fgGrwfyQXOjT5TfxspANBi71R2bJiwkDa6t5KzSwdHIaJ2QSfvNvIzzVpffxvH0iNRRlklrZM2WmTZtzjesJ3h9GD-hGBFG7RgZ_wkA1gsbbVwQp-FHsuDbV5-ARKE_f0MtTEpjHrAUT91arwDcAZV6VsXKqIzvdjGqPh1JBDsO1zU5FqUGoqmBBlqhwl_XGPgr8Q_3B0t266LElWVYsxxWtXtZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
انفجار اسرائیلی در شهر مجدل زون در منطقه امنیتی جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141131" target="_blank">📅 13:42 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141130">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4cef38868.mp4?token=eDP5KlTm4-qpBWmAov6VVRaQ8eH6ZzVrOnJO9t_VJKmk-zcJIpr7LGTDUbry8Dd3yghyfw6gYvVNdZ78cJH-DGOZwvMo9tQk0RWxVzbuDZs6C6qJ22d6XqZVIQpI1JstylFMNux_eQsELq7LAjV5cxWgs2n-HQcawMMoOteE_Q8HFC0bV7MfqvJr81o_EJ0gv_jDa3gKHUuxqZmbTohGNQWMjTtas08ScMq_if736xd2R89MGUgaCM5-SMBnZfIPzUdMGWeO_B8iXejAYrQZPKBvtzmtI7IN75S6ZN7tYr96EZa4znJx1ziJdUMBmA39gsrnLTnhKjjKhxOk1vlrFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4cef38868.mp4?token=eDP5KlTm4-qpBWmAov6VVRaQ8eH6ZzVrOnJO9t_VJKmk-zcJIpr7LGTDUbry8Dd3yghyfw6gYvVNdZ78cJH-DGOZwvMo9tQk0RWxVzbuDZs6C6qJ22d6XqZVIQpI1JstylFMNux_eQsELq7LAjV5cxWgs2n-HQcawMMoOteE_Q8HFC0bV7MfqvJr81o_EJ0gv_jDa3gKHUuxqZmbTohGNQWMjTtas08ScMq_if736xd2R89MGUgaCM5-SMBnZfIPzUdMGWeO_B8iXejAYrQZPKBvtzmtI7IN75S6ZN7tYr96EZa4znJx1ziJdUMBmA39gsrnLTnhKjjKhxOk1vlrFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مطهرنیا: تنگه رو بستید ولی خودتونم نمیتونید ازش بیرون برید، چه فایده داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141130" target="_blank">📅 13:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141129">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac6a1ce92c.mp4?token=rNJ_-P9UHBuQalE-57PT_58RYH4Rt15ppiu_7iPnG29IV9U2I1XvLh8vDDfqwakuYynYcVTUPySOz0rgFUvem11woYAHmRgdESZjYItBXiAqUOmGI0c9snpEu5x4FtzYIVrsom62V0OkIvpPyLd7ypaQ5WK4_9qgQQQ_BuiUO9hBQa30XSSEjNgdJUK090uRYD59JCtJatPRQylzfzt-tA2oiAytEydQ1bjj_fdph17W0YFhnt5SURt1Knnx4VKurunpJPPo6wKBbmxgUwIRUJQP_eOn2u3ZqsPwD4zaVQlaO9GThK88SqEaJ1XI8c2DILj80NVVoygwNmsZwgL8Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac6a1ce92c.mp4?token=rNJ_-P9UHBuQalE-57PT_58RYH4Rt15ppiu_7iPnG29IV9U2I1XvLh8vDDfqwakuYynYcVTUPySOz0rgFUvem11woYAHmRgdESZjYItBXiAqUOmGI0c9snpEu5x4FtzYIVrsom62V0OkIvpPyLd7ypaQ5WK4_9qgQQQ_BuiUO9hBQa30XSSEjNgdJUK090uRYD59JCtJatPRQylzfzt-tA2oiAytEydQ1bjj_fdph17W0YFhnt5SURt1Knnx4VKurunpJPPo6wKBbmxgUwIRUJQP_eOn2u3ZqsPwD4zaVQlaO9GThK88SqEaJ1XI8c2DILj80NVVoygwNmsZwgL8Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
ساحل قشم نفتی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/141129" target="_blank">📅 13:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141128">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
وزیر بهداشت: نزدیک به ۸ هزار میلیارد تومان هزینه تهاجم و تخریب زیرساخت‌های سلامت ایران در جنگ شده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/141128" target="_blank">📅 13:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141127">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
وزیر بهداشت: هند در تمام ایام جنگ حتی یک کشتی مواد اولیه دارویی برای ما نفرستاد؛ برای ما شرط می‌گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/141127" target="_blank">📅 13:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141126">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7jYuVtwFVACsvei_Xun7EBg40XvRY1GORM0xVyMrL4tsePZrWaUh5yPE_mvkwgn06mVWwxh-G98GH8kMEpzDFl-KP71Ea0klDwsSW3I17sjbTV7ntDeilpXIig45UQkSiUH9cBmcw015UOPhrhmz6PR-yTcN7Op1xEi_hxoSljm_cQyUPd60Be3rY-Hgaa2xoH9AucRfxnCbjwk8Zd4ANEdL_wt6IoJZmLynLkxe00T-HxW2wm-296cUq60DCoszLWNE51I-6hAKhbcvBLfXe2WUJS8T6L9dpo6e7tFaAROckoSr_D1KP6JU-Q87C7qIsI5vWQLZXG-nzp-zgzG3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کشتی مورد هدف در تنگه باب‌المندب توسط حوثی ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/141126" target="_blank">📅 13:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141125">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
فوری / سازمان عملیات تجارت دریایی بریتانیا:  گزارش از وقوع یک حادثه میان یک نفتکش و نیروهای نظامی در خلیج عمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/141125" target="_blank">📅 12:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141124">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
دادگاه کیفری دمشق، حکم اعدام بشار اسد را صادر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141124" target="_blank">📅 12:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141123">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aU3cSAn2zTFFjjl9ikLlEXtGMeol5kbszR0xuPRkXgxnYUMNWQm2X8GAasRUbC_L2YwV2NAruRDBpzqdPXDMTTl98sG7yu2rruKWST-gI4owwZPHjJNBVS13cOb_b899LIueBmuw7J5B8SwFjqzQWZLC3jnNLkKSjcWE42yZi0gtgTG-y_qfp6MpaTXd_OwnF91WOQUbbp8BfOkCNwj0typ-tO6FPrqxMN9Xf7U7QMR-4Pr-WjKIDLLMDGJhku_Lw4iWVi-oc2PbpYtw6hgoQ2IlBpzF0wKvJpSi1YpD4ivpdXRgHyRAgSpP86I8QbOoyCGboS8MrcL1RocV41NrYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
احتمال بردن اکثریت کنگره در انتخابات کنگره آمریکا برای دموکرات ها به ۸۵ درصد رسید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/141123" target="_blank">📅 12:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141122">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6bd64135d.mp4?token=pbrWyQvunvhT6vuEB3zZ8vKY5zzIRpkbrku4V93d0tgFYMiaQgVR8fFjXCIHY9O89UotMfHPoOEjkDLlkS3ZBn5GZ2nRE-_YqVn3wpGe4V_AhPS0EcP0PIDeWdMHWVGb5baITzHDjwEiRNAvmyDT1avpHlZ4T5B94Kl37lHXKWn72OeG7BCq-hsDS8pz_rFZylPvmoxn_WMm2jkqJbE6ZvZHjpOr3EHF41eM9p6_UvfvwSBPn1UrCH0w3NUjMpHYE7a_uYqtGDs-4A7UwMLVtfeLN2tYAmqFWvdL00_NcIzvglcvtE7VxfugosWB8cIezZrWoU-jxuyJqmMk059l5kjhaTGqexPVwJNSZMVFcSScVROHxbahKJAvd8DmIkIcqND_NszXUrt3RpAequJNeC8VkxI5WdNyK4AdGnqKf2SdZ2o64N1-uOqudzSrMrxJR4sVq4lTHWBewlZJPo2Co2JQ_Q7UDZPRDwmcW971JfmhAm-8pROg-3dwdn4S8qG2lMLPsweHTZYNPr_EvqIvgFf7F_Io4fA_Hji_dNP7EIbtwpYwviI3TYFtcsSZ-ni4cLjL7VJWNt1XfT9n4kL0sNS2Z5hKM45s_vb_2QRO57hNVhJ6m69ZtCp6RBYp5GfM8V87JNoEmzl1CfJse8H2QfbpFmgdyVaotlChC56C9Ik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6bd64135d.mp4?token=pbrWyQvunvhT6vuEB3zZ8vKY5zzIRpkbrku4V93d0tgFYMiaQgVR8fFjXCIHY9O89UotMfHPoOEjkDLlkS3ZBn5GZ2nRE-_YqVn3wpGe4V_AhPS0EcP0PIDeWdMHWVGb5baITzHDjwEiRNAvmyDT1avpHlZ4T5B94Kl37lHXKWn72OeG7BCq-hsDS8pz_rFZylPvmoxn_WMm2jkqJbE6ZvZHjpOr3EHF41eM9p6_UvfvwSBPn1UrCH0w3NUjMpHYE7a_uYqtGDs-4A7UwMLVtfeLN2tYAmqFWvdL00_NcIzvglcvtE7VxfugosWB8cIezZrWoU-jxuyJqmMk059l5kjhaTGqexPVwJNSZMVFcSScVROHxbahKJAvd8DmIkIcqND_NszXUrt3RpAequJNeC8VkxI5WdNyK4AdGnqKf2SdZ2o64N1-uOqudzSrMrxJR4sVq4lTHWBewlZJPo2Co2JQ_Q7UDZPRDwmcW971JfmhAm-8pROg-3dwdn4S8qG2lMLPsweHTZYNPr_EvqIvgFf7F_Io4fA_Hji_dNP7EIbtwpYwviI3TYFtcsSZ-ni4cLjL7VJWNt1XfT9n4kL0sNS2Z5hKM45s_vb_2QRO57hNVhJ6m69ZtCp6RBYp5GfM8V87JNoEmzl1CfJse8H2QfbpFmgdyVaotlChC56C9Ik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره لابی اسرائیل: بزرگترین تغییری که در ۱۰ تا ۱۵ سال گذشته دیده‌ام، اتفاقی است که برای اسرائیل و مردم یهود افتاده است.
🔴
آن‌ها لابی بسیار قدرتمندی داشتند. اگر به ۲۰ یا ۲۵ سال پیش برگردیم، قدرتمندترین لابی در واشنگتن را داشتند.
🔴
اما اکنون همه، می‌دانید، اعداد بزرگ—اگر به مجلس نمایندگان نگاه کنید، به دموکرات‌ها در مجلس نگاه کنید—تغییر کرده‌اند.
🔴
به مردانی مانند شومر نگاه کنید. او عملاً فلسطینی شده است و به اتفاقاتی که آنجا رخ داده نگاه کنید. واقعاً شگفت‌انگیز است. هرگز چیزی شبیه به این ندیده‌ام.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141122" target="_blank">📅 12:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141121">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/397426053f.mp4?token=vxs6MmFpVlt1-KGuIf8KRlSzeuYrA5VAiJF7PS-Ih6fFPIP23bWgvHorJXlJF911Sxb6y5Hp-3vMOgG9Gi6QYrchrXrYzdqI3FLyes0ujuDnZYJbj70u_FQT6RNFZmESTi__i-HNNWGLeFIQOZKNP0IL3qzonvWWHd7u_-tPhIXLtrB05L3S7U5XAyqcTeTUbJA6Mq91sqQlimtoVakwKMkOmDkvRlbrT69SyFBzRuGRsjDwxR7NRJa794ezXQEo0qLp5tQArhN-TUgKI1vtm7AcHD9BC-UlB9Wf2Q-iUWG3Wme5cDSMOEQQDy87FCNhC7zb4a688t42y0iDwmHfxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/397426053f.mp4?token=vxs6MmFpVlt1-KGuIf8KRlSzeuYrA5VAiJF7PS-Ih6fFPIP23bWgvHorJXlJF911Sxb6y5Hp-3vMOgG9Gi6QYrchrXrYzdqI3FLyes0ujuDnZYJbj70u_FQT6RNFZmESTi__i-HNNWGLeFIQOZKNP0IL3qzonvWWHd7u_-tPhIXLtrB05L3S7U5XAyqcTeTUbJA6Mq91sqQlimtoVakwKMkOmDkvRlbrT69SyFBzRuGRsjDwxR7NRJa794ezXQEo0qLp5tQArhN-TUgKI1vtm7AcHD9BC-UlB9Wf2Q-iUWG3Wme5cDSMOEQQDy87FCNhC7zb4a688t42y0iDwmHfxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جدیدترین موشک چین کمتر از ۹۰ ثانیه پس از پرتاب منفجر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141121" target="_blank">📅 12:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141120">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ترامپ: می‌دانید چه کسی توربین‌های بادی را می‌سازد؟ چین. آن‌ها از آن‌ها استفاده نمی‌کنند، بلکه آن‌ها را می‌سازند.
🔴
گفتم: «چند نیروگاه بادی در چین وجود دارد؟» آن‌ها سعی در فکر کردن دارند. به اطراف نگاه می‌کنند. آن‌ها یک یا دو نیروگاه نمایشی دارند، مثل اینکه «این‌ها این شکلی هستند»، اما از آن‌ها استفاده نمی‌کنند چون خوب نیستند.
🔴
می‌دانید، آن‌ها بسیار گران هستند و انرژی بد تولید می‌کنند. بسیار گران. گران‌ترین چیز. آن‌ها محله را خراب می‌کنند.
🔴
میخواهید گورستانی از پرندگان ببینید؟ گاهی اوقات زیر یک توربین بادی بروید و هزاران پرنده مرده را خواهید دید.
🔴
واکسن MMR، اگر آن‌ها را جداگانه بدهید، یعنی M، M و R، مشکلی ندارد.
🔴
وقتی آن‌ها را با هم ترکیب می‌کنید، طبق گفته برخی، شبیه یک سلاح هسته‌ای هستند.
🔴
پس چرا آن‌ها را جداگانه نمی‌دهید؟
🔴
ما مهمات می‌فروشیم، جنگنده می‌فروشیم، همه چیز را به اتحادیه اروپا می‌فروشیم و آن‌ها هر کاری که می‌خواهند انجام می‌دهند. آن‌ها این‌ها را به اوکراین می‌دهند.
🔴
اما بایدن اعدادی را فاش کرد که کاملاً دیوانه‌وار بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/141120" target="_blank">📅 12:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141119">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwPQXM6SKm6gQjit7fR1Uk0_PP5keyyPhD7c1k-oAzXgfcgDQcRLuNqUPOqioRhdX8DshfV1whQZNvU1URD4CqnqiFJq9FihUoAYuplkk7Re1iz1VCRZpClGHLOSZeGY2rsPbLj5_LL-1cNda_Wlbt1446JZt1CHSfmOFXp2MV_iMq_PSo0XAv8IHVKetQGysNiC8YgWFD4535P2wYU7uoYTtpBpP0gAb8Q2OkJBvdFjh2snTsF-8gIoli282_RN6vlJTsow9oJL820BOyZ-KIoltJAz8sMvmR4TCRSLLvvbyFJlXJ51aR8cZMkGIqHI7tlYJ0jJFWOg9Hbj6AriYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
استاندار آذربایجان‌غربی: حجم آب دریاچهٔ ارومیه نسبت به سال گذشته افزایش ۷ برابری داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/141119" target="_blank">📅 12:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141118">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7beb0c8db.mp4?token=AGCVfErYwIbimstvUmYL20vgEd0oV2rRLdZ4NLXFexE8Inl6D2L1dD6_hMy-IjfMPhrA1EcTbqG2l3moXOAV8pSPJt_oXtoQB1NKVWzQLR4hex310KcNeNIv7WgPibqNwGPGqCRngmR2x6dhQFwDAjsHLEPUSWzgAlrlNWRTErEPHJp41CiIyjzBKwDExVJKsdxekJ6PkH0jcQDYeGWrZtMJisTm7Cj29KEga5BxYb6PqFHkMDchkOGwfQDzlk779um9rx1Wth4GjVeCj7oVV8HGpeOnE9n1ppSyjZLPd_SwkhQrNlFhQ06u5Z8KUx5b25Tutwxg3VUVK5igsx5cLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7beb0c8db.mp4?token=AGCVfErYwIbimstvUmYL20vgEd0oV2rRLdZ4NLXFexE8Inl6D2L1dD6_hMy-IjfMPhrA1EcTbqG2l3moXOAV8pSPJt_oXtoQB1NKVWzQLR4hex310KcNeNIv7WgPibqNwGPGqCRngmR2x6dhQFwDAjsHLEPUSWzgAlrlNWRTErEPHJp41CiIyjzBKwDExVJKsdxekJ6PkH0jcQDYeGWrZtMJisTm7Cj29KEga5BxYb6PqFHkMDchkOGwfQDzlk779um9rx1Wth4GjVeCj7oVV8HGpeOnE9n1ppSyjZLPd_SwkhQrNlFhQ06u5Z8KUx5b25Tutwxg3VUVK5igsx5cLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل زیرساخت‌های روستای زُطُر الشرقیه تو جنوب لبنان رو بمبارون کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/141118" target="_blank">📅 12:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141117">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
حمله جدید با موشک دیگری، یک کشتی را در تنگه باب المندب هدف قرار داد، در حالی که نیروهای دریایی در حال نجات خدمه آن بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/141117" target="_blank">📅 12:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141116">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqAKrXmCAkWP4a-7jJpKznfjk6IsyOHErEl0z0p9eqlZja80caTgTpRJAIygRUEJJcXIO2I9XH--jWx3wQwGkmeH6xIeqH4pLUpe9CnZwpvm5-UX1p2Q4zCNeo9xbNGIalvhBEz22pWM1AMfA4oT4usDFQXu32KB6Rnm7y2LY8EIRYDviS-iiElc0jVgcc5WtISSQpnmEKDIE4w8kYGvQfLrbKVTlmBExTDLFe7TGLXBZSvJYg3u2r0TEamV6qxNiBOKmhktpcdB_2p4DaLbZ0K-2SqIbiata_GL8uuD6CrB4zQyuUX0h3ifqCEqGvkNMO_1l7yAKJxMKOmCMnLDig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
حداد عادل:
هرچی مشکلات الان داریم تقصیر پهلویه
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/141116" target="_blank">📅 11:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141115">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/954ac5fabd.mp4?token=fnviZdptVE7VUh5zsv4p_jLhGvkXxRkrys_GkkIqn7yLZ0gUq_zgD8fw8FeTkd5kP2mhHazMe4ElWWcujyKtmG_yt288G__gYuY1Sp4NLCw5oJR72baILagkZncWL-hhkMwS48V2L-Bf8G0zFigEmrDgEfdPFDhwCQuUgeoRksUfiUd45ZUpKgZBHOi9mXEXhGvsE__ir9ZgdQUNp0KTb_qm6mmWBYYNhrZp0AFYQaXL7Nd4lDIICHVmLe6BmicdGTUJmUy8DkWGmVn0VpdiuGWRnj-pRpxnx4UKNSKkN0y80-VdpKXbjhhZMqUKULP7u8KIe424dOmuM2LKo1mUTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/954ac5fabd.mp4?token=fnviZdptVE7VUh5zsv4p_jLhGvkXxRkrys_GkkIqn7yLZ0gUq_zgD8fw8FeTkd5kP2mhHazMe4ElWWcujyKtmG_yt288G__gYuY1Sp4NLCw5oJR72baILagkZncWL-hhkMwS48V2L-Bf8G0zFigEmrDgEfdPFDhwCQuUgeoRksUfiUd45ZUpKgZBHOi9mXEXhGvsE__ir9ZgdQUNp0KTb_qm6mmWBYYNhrZp0AFYQaXL7Nd4lDIICHVmLe6BmicdGTUJmUy8DkWGmVn0VpdiuGWRnj-pRpxnx4UKNSKkN0y80-VdpKXbjhhZMqUKULP7u8KIe424dOmuM2LKo1mUTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: اگر اقدام نمی‌کردم، اکنون سلاح هسته‌ای داشتند.
🔴
دونالد ترامپ درباره ایران : «اگر کاری را که انجام دادم، انجام نمی‌دادم، آن‌ها اکنون سلاح هسته‌ای داشتند و شما مجبور بودید آن‌ها را "قربان" خطاب کنید.»
🔴
این سخنان بخشی از سخنان ترامپ درباره تأثیر اقدامات دولتش بر برنامه هسته‌ای ایران است.
✅
@AloNewd</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141115" target="_blank">📅 11:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141114">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ترامپ می‌گوید  دلیل کمبود مهمات این است که بایدن مبلغ 300 میلیارد دلار به اوکراین کمک کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/141114" target="_blank">📅 11:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141113">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
داده‌های حمل‌ونقل دریایی نشان می‌دهد که تردد کشتی‌ها از تنگهٔ هرمز دیروز به ۶ فروند کاهش یافته است.
🔴
این درحالی‌ست که میانگین ۱۰ روزهٔ این آمار حدود ۱۱ کشتی بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141113" target="_blank">📅 11:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141112">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
رسانه‌های عربی: یمن به یک کشتی عربستان حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/141112" target="_blank">📅 11:27 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141111">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/293e8a0f47.mp4?token=MoDtRA1M8OkObcKJeEkdNeg78bRUxklf1JeTC8V6ZiUVBUaUwolfPxLcnqd8VV75n1EZ8Y6-g_5uzfcYtRsWi-Ke3EA3z7jEwUxcBC9zjA_7Rf1_xHAGglhK_fBP7ERRwuYac74PRVFti6qle4H4RGl4hnR9a5cS72Xvwo4kX9aG1UmtyBDDmn4AG-hNOxbaL_lsI0ZDHhueIKj_XKWT357MeZEoO_ygqySZtbXTBZO43aReC8jj1nslXJpCRcn_PcVVMGnCPzOB_AH1359mgxGP52TnUGWMp8oQxfAXPBQRSKPO3dWj_4TVGhQJs1UQrungNnzNFvGVFCLhHgGRFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/293e8a0f47.mp4?token=MoDtRA1M8OkObcKJeEkdNeg78bRUxklf1JeTC8V6ZiUVBUaUwolfPxLcnqd8VV75n1EZ8Y6-g_5uzfcYtRsWi-Ke3EA3z7jEwUxcBC9zjA_7Rf1_xHAGglhK_fBP7ERRwuYac74PRVFti6qle4H4RGl4hnR9a5cS72Xvwo4kX9aG1UmtyBDDmn4AG-hNOxbaL_lsI0ZDHhueIKj_XKWT357MeZEoO_ygqySZtbXTBZO43aReC8jj1nslXJpCRcn_PcVVMGnCPzOB_AH1359mgxGP52TnUGWMp8oQxfAXPBQRSKPO3dWj_4TVGhQJs1UQrungNnzNFvGVFCLhHgGRFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
تصاویری ترسناک از زلزله بزرگ کلمبیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141111" target="_blank">📅 11:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141110">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uz69vj2kR1PEy8JjyDL4-11TtSt1QJVpdMo2_-xoci0rj3uBS7ywlyCP37qCnchYZiEQ6pj6TNO64DRFZL7WI59VjM-rWTb-gqQk-5Y7sXxlIOc_TSQN5X9xpz7b1be2fnlPbWcMgmpyCrcPCD7a9C2nwvpDySVzGkjAqkzTTj5oMjBP0ceU-AWVwLgbPC-754j8IS3td-oqbMwrXypmyq___3tsZYYgQgtpdBqzFJn3fatanvl_DSGt0QSy3nj8OnSRcOGs71s55KNEj7qjXfzw1_N4jzjMc85XqwU5OTWpzCJEGLWLL9-arifTI6wdXm5MyK1EtZccXtRe0ZJ70w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توپخانه اسرائیلی شهر زواتر الشارقیه را در منطقه امنیتی جنوب لبنان هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/141110" target="_blank">📅 11:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141109">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/207604b3e3.mp4?token=V3coT6LZahnuYWMdXZnnIjAgLfLvg3bmyVTFHYKd7XbbGrN2ZLzg64LChvA9eDEeTqkmMyyp1CEhlBTLXFKn9LByPv2g4wMieFb_crD8iGKsNsIlsdFJG9Qry8ALQn2PoLMrONIpvXPOF6tjIijS1m9xj-UO3HrVBnCKDW-qei9NN21FxdEt-eU1uz4NYGu8d_r7STOMtt3G3HcQ1lDw7gmi7u0-gXC3NHHH2PKpkBjdU2uB6EXRE3tMoeh7EUJdLbYcpeGj6jhOepHztaGh7R6AyI039t14KGz7nXdNNSug1yB7OluwAah3EXpXgmnqdX_yZura7uxgVibIOT1QWoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/207604b3e3.mp4?token=V3coT6LZahnuYWMdXZnnIjAgLfLvg3bmyVTFHYKd7XbbGrN2ZLzg64LChvA9eDEeTqkmMyyp1CEhlBTLXFKn9LByPv2g4wMieFb_crD8iGKsNsIlsdFJG9Qry8ALQn2PoLMrONIpvXPOF6tjIijS1m9xj-UO3HrVBnCKDW-qei9NN21FxdEt-eU1uz4NYGu8d_r7STOMtt3G3HcQ1lDw7gmi7u0-gXC3NHHH2PKpkBjdU2uB6EXRE3tMoeh7EUJdLbYcpeGj6jhOepHztaGh7R6AyI039t14KGz7nXdNNSug1yB7OluwAah3EXpXgmnqdX_yZura7uxgVibIOT1QWoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله پهپادی اسرائیل چند دقیقه پیش به یک خودرو در النبطیه هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141109" target="_blank">📅 11:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141108">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
رسانه‌های عربی: یمن به یک کشتی عربستان حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141108" target="_blank">📅 11:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141107">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c02a0c926.mp4?token=a1cydcXAHL-zm1fMWPEjuk_TNqiGj51aF-F_avNdzqqPBALrdrLjUgCR0ccMDL_GUyzpo6PdfJtIBeo--AKad7Dm-gUPYgxpixvYu7-2lYdjPpIPpoMB-XgRMJ2oIOyMP5-Lg66Xrn2Ke4JTmtprQWsH7UXgQw5bTn-K1q6FxzJ2bZ7O6_CEZJUAkR4L_XhSjvzmosXTjJVWi3f9ak7Us2dhUs5oStFCsSFlG5oWW0fAyf8Imnz7iLtPMHhQoUy5pGPdI3tz5mfw3LJpDNJV0HHSNCXd71m7KV_zEaXKDSZk-62tCigUDgUXng53uDZs3YDk3KAgoP3fm1F17BHA1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c02a0c926.mp4?token=a1cydcXAHL-zm1fMWPEjuk_TNqiGj51aF-F_avNdzqqPBALrdrLjUgCR0ccMDL_GUyzpo6PdfJtIBeo--AKad7Dm-gUPYgxpixvYu7-2lYdjPpIPpoMB-XgRMJ2oIOyMP5-Lg66Xrn2Ke4JTmtprQWsH7UXgQw5bTn-K1q6FxzJ2bZ7O6_CEZJUAkR4L_XhSjvzmosXTjJVWi3f9ak7Us2dhUs5oStFCsSFlG5oWW0fAyf8Imnz7iLtPMHhQoUy5pGPdI3tz5mfw3LJpDNJV0HHSNCXd71m7KV_zEaXKDSZk-62tCigUDgUXng53uDZs3YDk3KAgoP3fm1F17BHA1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عراقچی: ترامپ که اول جنگ توئیت زد «تسلیم بدون قید و شرط» بعد از ۲۰ روز برای مذاکره التماس می‌کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/141107" target="_blank">📅 11:07 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141106">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f8cba287a.mp4?token=rh6PjWMI-P4yppQGiC2yLXNO1hLYxCyrN9U9wF8N2YljVPK6wCrrlp47jS3UnCuBb-wuDflVL6hlltpi7a6vSfIhX_0xXqPmXw0_kW1TAAg-ZobBZndOT5j_jQw127-lVwi7s_F9PEuoU6SHvHA6jzG5arzOPOyjgsSSVGM66RZ_f_tv4lxSm_dTziRzpMWlHGAaZmEiAhZbE1yz68f7avMrU86KQzeON7-Ti24v01cPJq83MPtnLOhEqutR23a8N6NH_z2mqrAWWXJPDn-dpOGy0VBImefpDY_mwWUoewWTA0vTleJRo-Dg8cL6f7mltqW5nPmQ11Lx1oyLy8Sebg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f8cba287a.mp4?token=rh6PjWMI-P4yppQGiC2yLXNO1hLYxCyrN9U9wF8N2YljVPK6wCrrlp47jS3UnCuBb-wuDflVL6hlltpi7a6vSfIhX_0xXqPmXw0_kW1TAAg-ZobBZndOT5j_jQw127-lVwi7s_F9PEuoU6SHvHA6jzG5arzOPOyjgsSSVGM66RZ_f_tv4lxSm_dTziRzpMWlHGAaZmEiAhZbE1yz68f7avMrU86KQzeON7-Ti24v01cPJq83MPtnLOhEqutR23a8N6NH_z2mqrAWWXJPDn-dpOGy0VBImefpDY_mwWUoewWTA0vTleJRo-Dg8cL6f7mltqW5nPmQ11Lx1oyLy8Sebg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عراقچی: به گفته مقامات کشورهای مختلف ما هم جنگ را بردیم، هم دیپلماسی را
🔴
به‌نظر من اخلاق، شرافت و عزت را هم بردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141106" target="_blank">📅 11:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141104">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cb5c8ae2f.mp4?token=qwrWK6TtgXGj1Sn_KAjSOMbtIqO8VRHCOrNS8jFkqSCDJvD8wrlk6KFkcg67plq2K80MxK1UqjlXu5e5Jx_sbWIhHzebBSPIRS5swj39YBkvT1EwS4yuxtuvj7ka27doBBhtbczR41p9-hDsnz4Kd7MfS7Qi3kZfd1I7dnDz4wIUMb6bGXuCV9DhSEAweUvltU4YTMnumvkyUkFvOmz62vbRFWGbofliDTwTfUcxuaNOg-Z0B-9CLP0TF3OJEbd0IWWoRF03tOYyEVQG0ZCEbTFieXpqjFBkaDBd9SnB_bgDqsI-nKqPw67okRqv3nTul-Jiq2EYuhV1YOE_GNpgHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cb5c8ae2f.mp4?token=qwrWK6TtgXGj1Sn_KAjSOMbtIqO8VRHCOrNS8jFkqSCDJvD8wrlk6KFkcg67plq2K80MxK1UqjlXu5e5Jx_sbWIhHzebBSPIRS5swj39YBkvT1EwS4yuxtuvj7ka27doBBhtbczR41p9-hDsnz4Kd7MfS7Qi3kZfd1I7dnDz4wIUMb6bGXuCV9DhSEAweUvltU4YTMnumvkyUkFvOmz62vbRFWGbofliDTwTfUcxuaNOg-Z0B-9CLP0TF3OJEbd0IWWoRF03tOYyEVQG0ZCEbTFieXpqjFBkaDBd9SnB_bgDqsI-nKqPw67okRqv3nTul-Jiq2EYuhV1YOE_GNpgHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شواهدی وجود ندارد که اورانیوم غنی‌شده ایران زیر آوار باشد
🔴
جان برمن، مجری CNN: ایران اورانیوم غنی‌شده خودش را دارد؛ همان چیزی که در آغاز جنگ داشت. آن‌ها همچنان مقدار قابل‌توجهی اورانیوم با غنای بالا در اختیار دارند.
🔴
جیسون رانتز، تحلیلگر محافظه‌کار:
"زیر آوار دیگه؟"
🔴
جان برمن، مجری CNN:
"نه، هیچ اطلاعات و شواهدی نداریم که نشان بدهد اورانیوم‌های ایران زیر آوار است... و آن‌ها همچنان هر از گاهی چند موشک به سمت ما شلیک می‌کنند و همچنان توانمندی هسته‌ای دارند."
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141104" target="_blank">📅 10:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141103">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
رئیس اتاق بازرگانی ایران و چین:
تبعات ادامه محاصره دریایی از جنگ نیز بیشتر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/141103" target="_blank">📅 10:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141102">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d987e3f89.mp4?token=FnIMu1gkxUjkXD9sKQjUDFCUGKaiZpiWN6hZfK8WmnshP2tTVzWTB3puVbUtpwGxY9NsxpbRda7gKIT71ScDom9fZhBTc2sDsLqfAli2hg2kXJ0GUC8vfh6Jt9FkQR0eLUEkEKnoFhH9ltmiVhFFYxHjvpYtfbp7LuSJntw42DQ0j-Zr1Hb1cfy7jlQiZ0ovKdbzpF3QjIYQ0078PJ3nkONFas8qjDPbRuaCMJijCrgTb9DeHyMHCY3Df_Jch_P6ZXjTGmL0-NlZc8HaOXzFctcqEU3MrNbx2abg1lgMmGxtr0r6cDKk2wnZaoxdCEbdvPLUwRamAhENFulB1Jee4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d987e3f89.mp4?token=FnIMu1gkxUjkXD9sKQjUDFCUGKaiZpiWN6hZfK8WmnshP2tTVzWTB3puVbUtpwGxY9NsxpbRda7gKIT71ScDom9fZhBTc2sDsLqfAli2hg2kXJ0GUC8vfh6Jt9FkQR0eLUEkEKnoFhH9ltmiVhFFYxHjvpYtfbp7LuSJntw42DQ0j-Zr1Hb1cfy7jlQiZ0ovKdbzpF3QjIYQ0078PJ3nkONFas8qjDPbRuaCMJijCrgTb9DeHyMHCY3Df_Jch_P6ZXjTGmL0-NlZc8HaOXzFctcqEU3MrNbx2abg1lgMmGxtr0r6cDKk2wnZaoxdCEbdvPLUwRamAhENFulB1Jee4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی از محل گروگان‌گیری صبح امروز در خیابان ولیعصر تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141102" target="_blank">📅 10:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141101">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/285c35004b.mp4?token=oIoH4BXqhbc6fpmsdkVBwRh3LHHDGnevj40ZEHl09aqnl7PD4UiulBaOwqPbERwWhiv5ODIZdtfxn5eQu6YjWtsKfxa676mbwiR52XK6p5G1PHwNwaJhwejaDYymQ3bTuDvLpnwT9RV_Uwxmmkl4-GwnwAXO6EayVch2uXqWnX9wdiX9vC038_oQ3NTHzsxvP4EFXwlmWv5JMFjvVq1eJ7AxdLi_rImLiwJSBtl-M0GrTTPXG_LO7nQQC9idZZAgKO_hBSHr27Ih3AOXmlOx3JaKS6S5O8DluO65I1e_71C77i11-leWdMP_UQuzFkfWm7BvVDv0y9iJO7dV4uBQSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/285c35004b.mp4?token=oIoH4BXqhbc6fpmsdkVBwRh3LHHDGnevj40ZEHl09aqnl7PD4UiulBaOwqPbERwWhiv5ODIZdtfxn5eQu6YjWtsKfxa676mbwiR52XK6p5G1PHwNwaJhwejaDYymQ3bTuDvLpnwT9RV_Uwxmmkl4-GwnwAXO6EayVch2uXqWnX9wdiX9vC038_oQ3NTHzsxvP4EFXwlmWv5JMFjvVq1eJ7AxdLi_rImLiwJSBtl-M0GrTTPXG_LO7nQQC9idZZAgKO_hBSHr27Ih3AOXmlOx3JaKS6S5O8DluO65I1e_71C77i11-leWdMP_UQuzFkfWm7BvVDv0y9iJO7dV4uBQSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه انتقال گروگانگیر خیابان ولیعصر تهران توسط پلیس نوپو
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/141101" target="_blank">📅 10:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141100">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpBLgOPgXwpb5X94GSzo2JlkJx8dIv-h5LBt_euQVIUa-2Nfr4LcUhU0Rx5OrguGoUQGIcSErPA4LeASye2nNWA40ZSv6LlNJ0Xm6ZDEHfBv0BXSapJPFxGlROz-gbC03q_xTqDs_Sy53QWn3GxBzgh53UYp1WumwO8ve1DJqTp0teNwEA-j4iHVEqGzPJMBrHbb9pb4jovI6DRu030KOOv3c1ihYB_72tHEfac30PQ4MiDMebOneXKwwfcyWUlpLhsykBdz3ofGHtLfx93uAk72I8GIT67sXTms3SmqUh5SDhWjetdyBNkm69qHLzcnXM1Z8AR9Z20vjF2QeKbncA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیت هگست، وزیر جنگ آمریکا:لیندسی گراهام، مدافع بی‌قیدوشرط ارتش ما بود.
🔴
پایگاه مشترک لیندسی گراهام میراث او را برای نسل‌های آینده زنده نگه خواهد داشت.
🔴
آسوده بخواب، سناتور؛ ما نگهبانی را بر عهده داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141100" target="_blank">📅 10:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141099">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
صبح امروز یک مورد گروگان‌گیری در خیابان ولیعصر، بالاتر از پارک ساعی، به پلیس گزارش شد. با حضور نیروهای تخصصی پلیس، گروگان آزاد و گروگان‌گیر مهار شد؛ اقدامات تکمیلی در محل ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/141099" target="_blank">📅 10:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141098">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ان‌بی‌سی: ایالات متحده معتقد است که اولویت ایران از سلاح‌های هسته‌ای به تنگه هرمز تغییر کرده است.
🔴
ترامپ به مشاوران خود اطلاع داده است که همچنان تمایل دارد تلاش خود را برای رسیدن به توافقی با ایران ادامه دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/141098" target="_blank">📅 10:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141097">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
مایک والتز، نماینده آمریکا در سازمان ملل: ایران در مذاکره‌ با ما، صحبتش فقط پول، پول، پول است؛ زیرا آنها بمباران‌ها را تحمل می‌کنند
🔴
آنها به دنبال دسترسی به پول نقد و دارایی‌هایشان هستند که ما مسدود کرده‌ایم؛ این همان نقطهٔ فشار است.
🔴
این فشار همراه با محاصره، چیزی است که در نهایت باعث می‌شود ایران عقب‌نشینی کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/141097" target="_blank">📅 10:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141096">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
کارولین لیویت، سخنگوی کاخ سفید: به لطف رئیس‌جمهور ترامپ، هزینه زندگی در کشور ما مقرون‌به‌صرفه‌تر شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/141096" target="_blank">📅 10:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141095">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
واشنگتن پست:در پاسخ به تهدیدهای ایران مبنی بر ترور، ترامپ به طور مخفیانه از ترکیه خارج شد و با یک هواپیمای نظامی دیگر سفر کرد، در حالی که کاخ سفید به دروغ ادعا کرد که او در هواپیمای ریاست جمهوری بوده است.
🔴
برای پنهان کردن تحرکات خود از رسانه‌ها، ترامپ به طور مخفیانه بین هواپیماها با استفاده از یک کامیون تدارکاتی متعلق به فرودگاه منتقل شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/141095" target="_blank">📅 10:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141094">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0etForbi4EYh1kEEaufXZ2UGGT8c8a8sJqumNBEHZDDXV_Y0QwATK3XgSnOU2Ilo0eLlDEimSgVvU35hs4ltHudYmCgJ9RzpUDaPWNgZLYg3eXOhdj8VeMuW1YEs3i4D83sjGYF1-QRnPKMSO8Luly2iEuibFD-4p4okToWwiMndk3rmTwXJ79DcJ_kzkr0MML7AmBz-A161nzB_F3I1x-lUUzADcTAVCtW5cAHhMSSLc5KMejO7MNLF9rzgoWG2vexIXz408t3wHpwHr37EJRpZFq4QHB-r4zgCtn3eDTyH1EojZgqL8FopglOovBolEwOX7K__UtfxFk6zlUnVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق ارزیابی اطلاعات نظامی ایالات متحده، اولویت استراتژیک ایران از برنامه هسته‌ای خود به تنگه هرمز تغییر کرده است، طبق گزارش شبکه خبری ان‌بی‌سی.
🔴
مسئولان نظامی به رئیس‌جمهور ترامپ هشدار داده‌اند که هر عملیاتی برای به دست گرفتن کنترل تنگه، طولانی، پرهزینه و مرگبار خواهد بود و هیچ تضمینی برای موفقیت وجود ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/141094" target="_blank">📅 09:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141093">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e070d14b5.mp4?token=WMoVSj6DF-ZXroOo95boqjeahP5u5od3PhcBMILgjDKQdt5x-7L824FwPy7-nUhHW8cb6do6u8IDk6H_nLuZTAluP4_2cuS7lPbeGMKfDkHRR7va2yNPRm2EdMUX5JrqoSNpKsi8_VA6RhlGRPw0F3IiTVcMvVfVkNJbfk_QhwQTab2SC1O-lKbG74RH8hsdd3eWMDzgkJ5Fde660ffz-r6T-XlTuXLhNUAO2h59OWJ5-VfjMF_oMMto7YCwpasRBHP0kg1G3qozGKRST5TyyeVe3f2Flmju81YIGU-7rLrRY2MivvdeMswULCxWuGNsklQlTdrFxRa7PYdaEo4p3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e070d14b5.mp4?token=WMoVSj6DF-ZXroOo95boqjeahP5u5od3PhcBMILgjDKQdt5x-7L824FwPy7-nUhHW8cb6do6u8IDk6H_nLuZTAluP4_2cuS7lPbeGMKfDkHRR7va2yNPRm2EdMUX5JrqoSNpKsi8_VA6RhlGRPw0F3IiTVcMvVfVkNJbfk_QhwQTab2SC1O-lKbG74RH8hsdd3eWMDzgkJ5Fde660ffz-r6T-XlTuXLhNUAO2h59OWJ5-VfjMF_oMMto7YCwpasRBHP0kg1G3qozGKRST5TyyeVe3f2Flmju81YIGU-7rLrRY2MivvdeMswULCxWuGNsklQlTdrFxRa7PYdaEo4p3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارولین لیویت، سخنگوی کاخ سفید: به لطف رئیس‌جمهور ترامپ، هزینه زندگی در کشور ما مقرون‌به‌صرفه‌تر شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/141093" target="_blank">📅 09:42 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141092">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOLNQgBHzYQHEUeFBhsDoE0veY4_Moc3gy-33sghmL-olweKVz3poe6qtjdxrfvb6CEehHxOH0Iu9iL0jJ7ahrpeUTXMC6Jt924HWi45k3sEgFmWzHTO1BALSgrcI251YGqGjvzHP466UzllIjQv4MeSQXi_WjBVty4cvWBScuaNTEdqW-SteR1TZB0PRzSG5PfxVuKuhK_iT3csqZjfrXRzRZ5s5TxtXtkZGmc3941QszqpDjLJz2paYDeDJWlxcrBmsmb_ncW4pVr2ixXdewOC3_IaSmpFeBhhfxdlacOW97-xqiCTbuYnN7YyjnqxNZ5YFnTJiANKuUPoht-fKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ درباره ال-سید و نامزدهای حزب سوسیالیست دموکرات: آن‌ها برای خانه‌ها و اموال شما می‌آیند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/141092" target="_blank">📅 09:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141091">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ترامپ: ما سه استراتژی برای برخورد با ایران داریم؛ نخستین آن‌ها زیر نظر داشتن میزان وخامت اوضاع این کشور و دومین آن‌ها ضربه شدید به آن است
🔴
استراتژی سوم فشار اقتصادی است و ما در هر صورت آن را اجرا می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/141091" target="_blank">📅 09:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141090">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
وال استریت ژورنال: کشورهای منطقه آماده پذیرش کنترل تهران بر تنگه هرمز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/141090" target="_blank">📅 09:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141089">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vukT2-3jcFjnhCKoi--xou5QIoGXIkUs2oT_4HzMY0wx0w1Bd-WbDP2xBsRM3r7E-3pmgrfQGNhkwaArFcn034DXKm0fSXFz1XH5m0PpOWNY4-lGnSJqa5wrpUCnazTTUPqt1XV_DFacr6OxiIA2tvaHpfp0zAU7uUtvL_6bS8yK5HXq0aSa8riu5Gyhzpg9XrnEkxjMDG6celcJZT1ULfAhetqiepV68Pm4xRYwlhD6fd-iTFGPG_7bgC6P_edLE02rXdG7el9D5eVyjqrgxGp-qWPQGvYIFBYKlYiqranDoqGbgcUGZYAq4wvmtDtVUayfyz1gcpS9hPFEPy7DFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نهاد مدیریت آبراه خلیج فارس:
آمریکا در فرآیند درخواست مجوز عبور از تنگه هرمز دخالت می‌کنه، از این به بعد از مرورگر فایرفاکس استفاده کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/141089" target="_blank">📅 09:07 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141088">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXRyYEiNyNzhoi9PEf8LgTbvSMbxEwOo1PEqbtFK2PG1DP8mruO6y8HQYNwFkyONfopoGPVVPHJRZ9680OR_ijXMxKx8Q0Aq5j5U9C4YMyaSdnghLlSCEskDZl2DWQqflUtBDWn3M-_nEqVf-n9bEMT0NLbPoRy3Cyhp0mBZUu4qskG9o9ykRpKwOTp6UNAQuJ0cMpp7T-AfnVFPmrPPZs_Hos4LT1hZBtTytb8N8T67bPV0b-LjyRN73jLgFcJEzVd-_gMaBKB6R1v9sviodo5w3_vc43JDZnMwf6zwZxXawYUkdrPEAFEoCsxzWKxeWDBHVFfN9RqvXi3y1nb_GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقایسه برترین اقتصاد های جهان در سال های ۱۹۹۵ و ۲۰۲۶:
🔴
سقوط رتبه ژاپن، فرانسه و ایتالیا
🔴
صعود قابل توجه چین
🔴
رشد اقتصادی خوب هند
🔴
خارج شدن برزیل از هشت اقتصاد برتر دنیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/141088" target="_blank">📅 09:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141087">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OD3m1LBy3kF0SQp1LfIyHieycIzzFq5dpp0Srs04VvMxGKfC-m_MDgUcLbn_24SAcdSKS1q6wkiXncw0FsHXsrpCbbolGpY4MDn_YkANaWfd_eyCRwg3bqvjOIiH5NHXWVEPMcM5SSUXwJC178382mYHseOPBUs7gLFxmUIc2LfDwXk3QkwENYWb3DhGW04YbSKEd1s4Xi80i11s2R_eRjMTBgveZnlCay0vaw-TW9j509x-xsGxelt5o7DaszTUW-Tvm8MTOy3gqv1ZORJ2HOrR7j6ZKz64dtXsHBRgyEqVEUuc0bbO_hVfyZepcLGdffQvMfjtANkyDJJ9s2101g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، آخر هفته در زمین گلف خود در بدمینستر، تحت تدابیر امنیتی در کنار یک سامانه پدافند هوایی کوتاه‌برد AN/TWQ-۱ اونجر (SHORAD)، گلف بازی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/141087" target="_blank">📅 08:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141086">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3946ed98ea.mp4?token=kWBcrsKUO_YCB7WoufIErOUCBuQDec0TRJCUsujWKZg0Bg3dpbpZgnC3jxqpKxzU86GRgO8ReIezITXM_W6uAJr-qIT-UCurKdzv-acLAneodzytenJ00EeJc9ILcFk08QEQXrHDQQI1-dApJQUEUd01dKc2FrdCZrt46H2fZFb9CTnKx9QZMxe6kZQdMvb84ioHH8EOLXe386amLOeS-YOHOnr2cijPaeKmoTXjCoi0_sp33lzG4qazpxHXilHWgck-86Slni6MbVEPcz5YX_zAP6L_gPora4t57sOJYNpHU0ELYFwaGbi5pMWoCbEmRpEJVUDUnWV57294X9NOFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3946ed98ea.mp4?token=kWBcrsKUO_YCB7WoufIErOUCBuQDec0TRJCUsujWKZg0Bg3dpbpZgnC3jxqpKxzU86GRgO8ReIezITXM_W6uAJr-qIT-UCurKdzv-acLAneodzytenJ00EeJc9ILcFk08QEQXrHDQQI1-dApJQUEUd01dKc2FrdCZrt46H2fZFb9CTnKx9QZMxe6kZQdMvb84ioHH8EOLXe386amLOeS-YOHOnr2cijPaeKmoTXjCoi0_sp33lzG4qazpxHXilHWgck-86Slni6MbVEPcz5YX_zAP6L_gPora4t57sOJYNpHU0ELYFwaGbi5pMWoCbEmRpEJVUDUnWV57294X9NOFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حرکت عجیب رامین رضاییان و نمایش دادن تیپ و لباس ایرانی‌اش
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/141086" target="_blank">📅 08:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141085">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
سی‌ان‌ان / توقف مذاکرات اسرائیل و لبنان با میانجی‌گری آمریکا
🔴
تلاش‌های دیپلماتیک دولت ترامپ برای صلح خاورمیانه به بن‌بست خورد. منابع اسرائیلی تأیید کردند هیچ تاریخ مشخصی برای دور بعدی مذاکرات با لبنان تعیین نشده است.
🔴
تشدید حملات هوایی و اختلافات ارضی بر سر عقب‌نشینی از مناطق، مذاکرات رم را ناکامی‌ست
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141085" target="_blank">📅 08:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141084">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
وال استریت ژورنال: ترامپ به راهبرد قدیمی «فشار اقتصادی» روی آورده، به امید اینکه در جنگ با ایران به نتیجه‌ای جدید برسد
🔴
او به مشاورانش گفته ترجیح می‌دهد دستور حملات بیشتر را صادر نکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/141084" target="_blank">📅 08:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141083">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ترامپ به شبکه «ریل آمریکا وویس»:
ایرانی‌ها بر سر مسئله‌ای توافق می‌کنند و سپس بیرون می‌آیند و به رسانه‌ها اعلام می‌کنند که چنین کاری نکرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141083" target="_blank">📅 08:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141082">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJjlviWRjF6Z8ZIrsDgv701Yn1itG8R_thKuvepHKFZHn6u_kQw6eHPUYoVugQASa5fvsALu6aEkVN1p2FAFwM0LTPb6yRJHtATIZXmDEe5FWPW70RY2slSH0g_jGaSkWSjwsfa-kohHqP52DAtyAghEess0UkUG4fNLEJGNms2uXArZqtN1VLAg4Tq-4xM_9ZjgnFPHAwJ0zO9eGvGLBoynmnNbeE5riZIHKkJlsgrgZn2ntmKUlNklZHwXUShzNRJ8-i9aD-muAtyghondXIFJfKVOoKBjd5g_G1wTdddVGvThrRRdfJXs1dt6nUXmJSamxCOMhzxL0XrqFJsd7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : اگر فدراسیون جهانی فوتبال (فیفا) به هر دلیلی به فکر برکناری و جایگزینی جیانی اینفانتینو بیفتد، مرتکب اشتباهی بزرگ خواهد شد.
🔴
او فوق‌العاده است و موفق‌ترین جام جهانی تاریخ را برگزار کرد که سود آن چهار برابر دوره‌های قبل بود.
🔴
اگر او برود، فیفا دیگر رنگ موفقیت و سودآوری را نخواهد دید! از توجه شما به این موضوع سپاسگزارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/141082" target="_blank">📅 08:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141081">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqTW44DCvJo23t4JONp-qzz9rhE6JllAbiOZR_ObznDL2pAdIB_ARXR5CBzHf-AxRLuycEZHpfxKV9-MY5A7AYW7fRHPgSA8RbO0PFBFgdc2UjyomvkiI_cpmyHY53G3rDkUzxcaKjjZVwlpU0OvV9js0Lshqoj4gRko0wBsfKvi-cnbXdFq0nmPl5ZtVaz9aId3ZaD5usARDM1D3o0Y5IlCTJ4rOYEHvPs81P2hMaFk3lDMU7NpvSNUj8hhW20tHlrwgVjTtC9BzXr52nMQsJ-ewpJjzjcVPzEMbTs1RGChNqQRIk_Noui6xr-DXukaMy-ULZeLMT9p_XqZE3C8bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلعه نویی: پاداش ۷۰میلیاردی در مقایسه با سرمربی‌های دیگه ناچیزه
🔴
مهم این بود افتخار آفرینی کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/141081" target="_blank">📅 07:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141080">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aaaa507a1.mp4?token=f8ZkIHiskdYWzRLEepTAW5uILSVO0yP2k6O2c0t3ZZgGyF2R3qQX0zpkPe2HQ2RQ-Xwm4GgZHv0c1EhhfT0VnWFF22hAvOcPXUKt8C1e5QaeaVFEh3OMQP5c-7WK6XNbxQpNsVWRG6gn972VgzniCAi6QQHXBT82DtZpMhgUupc6GCVT1XJ7x-QzPJbO2tnujEnUpqFSb5srZR6bi_0eVXFIq6GYp_u0Tj0sMxFvL5J-Uj72abjJoWYEasFeuAMPZcceRUoE3IDpZv-1L8CGh5dy3RYJZUrYbLKF81nFSE7rdL_M-MjnMXOEdrEj9amtVEMe75eOlIE9O987OU5gWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aaaa507a1.mp4?token=f8ZkIHiskdYWzRLEepTAW5uILSVO0yP2k6O2c0t3ZZgGyF2R3qQX0zpkPe2HQ2RQ-Xwm4GgZHv0c1EhhfT0VnWFF22hAvOcPXUKt8C1e5QaeaVFEh3OMQP5c-7WK6XNbxQpNsVWRG6gn972VgzniCAi6QQHXBT82DtZpMhgUupc6GCVT1XJ7x-QzPJbO2tnujEnUpqFSb5srZR6bi_0eVXFIq6GYp_u0Tj0sMxFvL5J-Uj72abjJoWYEasFeuAMPZcceRUoE3IDpZv-1L8CGh5dy3RYJZUrYbLKF81nFSE7rdL_M-MjnMXOEdrEj9amtVEMe75eOlIE9O987OU5gWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جانباز شدید شیمیایی: لعنت بهتون که با این وضع بدنم باید با تاکسی کار کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/141080" target="_blank">📅 07:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141079">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghoXeQYbH3MgkwIScDhitZNtVpACFAowqwim-CNg5LAxIyeZsuN4R2sqXuiqQBp-nTVsqSajzzYNqYTdCFc7p1wAVkY3i8BlOGPzlJEOwbeGbWXvF1t04PWEh6Q674lDKBOqDkI3WtHsd55x7yMnsdUPwRCKX6mKA5buaLln_4bOa6limrMMhF4cy71J0Io3PE4Hl8DNbL8dFwqOWlz0uRNz3HSFt0GCXW5GDgAGXnnkERMw68d_nqskgZV9RvikSN14BP9tUiLVKIcLCB8m0OAh_QN9A80Dax-4UzcMg4ysRCSEItDSTwv34tbE1Phi5Z5Dn55HnizhtZepywH60Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در حال گلف بازی کردن در تعطیلات آخر هفته
🔴
یه سیستم پدافند هوایی کوتاه برد AN/TWQ-1 Avenger هم گذاشته کنارش
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/141079" target="_blank">📅 07:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141078">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromربات هوشمند اطلس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4L6BYNpNpvcuWACe9S9_nvnJMQ60mdFvBxbOUlYKtKQN2J-5raqu4gqDqJnWc1F4n2Hcujqx5Il02UlPszGgFHwP_k44wDVRz10arUfjNlK9dtKw6Q0-gXRyBA82u4ffNGyDZ7S34ruBEhiRUYGG68qOKNklHYzXG_EjFJKFBxSrM5HAScxT45g2fykbqC5aZcJ2lQOTN4OmiLygUF33MtqcMbKZQPxi7xLMlP4PmFKKfFJynTPxUydkznhEmETrB9XqRYgO4hyWzmL-wyzuVqVImDnRclUZ94LBoulwGbni-HyKe8Zyvm8NRBI3zyZExiNBx3nrcsR5_RyK_9Dbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/141078" target="_blank">📅 01:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141077">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_eY6XmvuDR1oC9gzp1f4Pl6eaZHX-vwecSRnCeIB0-Mrsc9oKIJ1VX-cBsxh5Uyh74By0nDj3MLot12gu7HxTfqPLmAS4WDP9Tsno9aIWhU5mhys46UxtJwIFxicbfZ7mg16i9U7aa3sYG5YRtz19hHs9Zz5oSvGpwArUxcA5uFXgigwVoHF8UoXT-Nbz0ERICyabGklNCbGA9B-EPbpE7cineFt-NhslBKp9G4aYV9yOxUQn9rwr1HRuGrtpE9QhOVFXEx8_oXEOXdXjuZgln2_CIXmez5LNaEvBex-aF2Ug7R_9NYukHsWqcElkYtnBKeKUIzXbQsCBStpm6FvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقایسه برترین اقتصاد های جهان در سال های ۱۹۹۵ و ۲۰۲۶:
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/141077" target="_blank">📅 01:28 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

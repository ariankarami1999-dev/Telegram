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
<img src="https://cdn4.telesco.pe/file/man4gbsvlq92jwlvInPaz3qqQw6iItsphY9VkDDgVYkl_KrWLaas2BKrIit-2JS3oCmPiAVLku5NzuSc7kAOYJgKxWDQ6qdn-dXkzXGJG0U1dirCHsgqoib-tWQPjRIJZ-hojS4zwNIasBv8b3w3UJSeTgmP28Nxg3wSNjqHtbcIXfTagJCqXKGMCjAY8IUWoIhgVRDmJmD54dBDFca764lnRIoWGxyfUtPJ50STp86gTlbNtrko9Pquui1l8b0yTgE46qGfzVhK9CiuePy4mUMDSwrPPQfPwQ-ME378kLQjHrryx3niS_ZaXAY6JRvYCwWCvoNmRZac5bTl2rJGHg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.6K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 15:21:35</div>
<hr>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_Uljm4Zx2Fz1dqPll7bLv_fMbk-8spyxFUmUPv-h6w8B-bqc7wh4YBeps-UNGo5AmPyeE2pukq8q5iPEq1eOL4QDn4GXzvEeKNeu9EQb0VwTp4d4llVvJG_mKuHoMmggpNeIMGQfGTpss4ZlDd9vsuSvq5Mgr4V14oxGIZyKYPd6JXcUV76wc7JwbhqQMfunF1gZ259HUxNjA1ymY54FNo9rPHbhXfCQQlTNMjQAl95Z3I6SWNsGaNiwGqBzvQqrUixJVLenYYSy3bGenhqpHus2n77Pa-rSito2fRadR6cYLs3INeHKlPXLn7Q-DHHhluOk5c0imrqJ9_cigU7wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=e1GnF_NBOrd9h4_1ohL5vGK3utWNRukG3tT8Yb9S7olexIR67vy7kJOtKBGNq3FJ0raQa6wAUew59JXZlOZ2BRCpxFgweRtjXqwcH4qqsSXeU9EKoVCL_Zd-a_xcFBh2JoAB9F0NbjcTzvzGf0_1hOtr5Y1yO6XEYsU7U175IVK1eLLt3bq76Xs6kdw7f7BJCyH1MeXtEPdLHu-ZKq9vuPFE4xVR2_E8mBAppMe2ayxEGzLnRjp5qhbtx9uSHlzG84UPVtY7BjfJcBkFw5nhzJShq5bm2wMpISVWr7iB2mXlJaFKWQ_SpU9e-tp8QX8HdExdd5EW_pcv6vToFfxpBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=e1GnF_NBOrd9h4_1ohL5vGK3utWNRukG3tT8Yb9S7olexIR67vy7kJOtKBGNq3FJ0raQa6wAUew59JXZlOZ2BRCpxFgweRtjXqwcH4qqsSXeU9EKoVCL_Zd-a_xcFBh2JoAB9F0NbjcTzvzGf0_1hOtr5Y1yO6XEYsU7U175IVK1eLLt3bq76Xs6kdw7f7BJCyH1MeXtEPdLHu-ZKq9vuPFE4xVR2_E8mBAppMe2ayxEGzLnRjp5qhbtx9uSHlzG84UPVtY7BjfJcBkFw5nhzJShq5bm2wMpISVWr7iB2mXlJaFKWQ_SpU9e-tp8QX8HdExdd5EW_pcv6vToFfxpBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=CXqMRIpIVFNgDfGf1NwIw1FGnXT9c5fSGk-GRS2VyV04dMVRUaBC7FZOw8T6m388glOIARc3ZtuLOWRy78ydwr3Ai8Tly5dG7oITICPoxZQLvOxkCNAcgkhKd6HY0lW0nWNjxvKPVeTOs42-gXb66vMQqwVfS67SSfh8oA1Ad6pbKOMqBbEM2DMACmlrcuKNIEStmv_jChPiUtQtIvNVyGVegSyaGgurqNNRVLO2CDbP7quJ5HF4ND-NhxfKZL8V1Cl8YSVFiAkZx-XjHT8_JLEeVkQhT8QZCkeHtMesUB-AHGswJYE5dlN72WdNalu9kw4zwkdfBr-wR9oSa0-mgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=CXqMRIpIVFNgDfGf1NwIw1FGnXT9c5fSGk-GRS2VyV04dMVRUaBC7FZOw8T6m388glOIARc3ZtuLOWRy78ydwr3Ai8Tly5dG7oITICPoxZQLvOxkCNAcgkhKd6HY0lW0nWNjxvKPVeTOs42-gXb66vMQqwVfS67SSfh8oA1Ad6pbKOMqBbEM2DMACmlrcuKNIEStmv_jChPiUtQtIvNVyGVegSyaGgurqNNRVLO2CDbP7quJ5HF4ND-NhxfKZL8V1Cl8YSVFiAkZx-XjHT8_JLEeVkQhT8QZCkeHtMesUB-AHGswJYE5dlN72WdNalu9kw4zwkdfBr-wR9oSa0-mgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2TIF47akLexrcJ1Zoxo6b2mGdkHf5k5C5Z3J7Altx4nK6OA7j4hYKjVoeeDXaz-qXpSpaZNCvuEDZiz0d_FA-TPIchyhmdW28FP9FdklxhGRLYqbOVXMJjb0fQQSc8MFl1wWGMtV5NGR_oeXlB5Dh8aUGB-o1jCHnPG4fzMrJwBeteXAwNoSTWoijZEguaw34N709mKmvh4ScbNupFV5NKM1mP9Ge87VWOt6suytVSdXhC500RwcDDVxyq0q-3Y1taTGmAyEOvAQzu7ptS2GzMxItj3sjo1wnOAncf-ZvZOtp0ITps9afQeKxAtmd4Y5TpaX3HsqWZkmRAUZL3cBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ رو به بهانه خونخواهی خامنه‌ای راه انداختن
۴ هزار لبنانی کشته شدن
از جمله بیش از ۷۰۰ کودک لبنانی را به کشتن دادن!
قالیباف رسما و علنا گفت
«برای جمهوری اسلامی» بود.
بعد دست به دامن دنیا شدن،
با التماس و با تهدید به جنگ با اسرائیل
و با قراردادن «پیش شرط  شماره یک»
برای تفاهم با آمریکا
در پایان دادن جنگ لبنان،
اینها رو از زیر چک و لگد اسرائیل کشیدن بیرون
حالا اومده میگه ما فلان کردیم!!!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8rChMa6x3iaBk8XLpiEIvS3KxEwDl21U8K8KuBVKm0X2BUALiDVr_d9JH3o1s_8jpSj73pciRBp45eNwPaJCGOcMFEa-nbR__No2YMuzVcpA5OACtfIVuoPXuufjuvgltd-8jH14YOHMRwYrpommsROp_60xHfK2eMjIJsKPlgszvxnAcWH1-f5S52c4D_xL-Tvtt8_FkBxEnzhc5E_otPHUX4l7FKgt0EHwG-Af1vaS7xl4jHmhc5kAOrCu2VXKo2Qsl8AGAnRWBREo9aPGaNie7zHvpOxFHCI2fVYTX0f5ZtGnLaPkyoIGsi5DwkHf9nKsn4tudAyhvN8KobkEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xm7o-GV1KoYkVzK9o-r3wTvJk06jOLtRVavho0oI_PJ-ueqtn5Fct4iK1Z_8khR1ETtitTux8ezERjJUyPhoWe-tb9KFswyaRyzb0oGvuH4l7L2BUxhdsK4Tn09mG0UsHX7DAnbpi2rGrUZT8vtacGowAA0ROsL4kkV6H_Pm6iQVWfrBuRCnDt_ea3G-MRzzWUtiMC305tvXk4WHNNNP0jtCQ0o9wqLFMxrdHY8YpQ1HXP1NpLuifT9UWGVN8t1lDXOK_3_-Y3WUj0AbJ76jMfR8ptkNcSXPivXAl6aA-gmfdcokNc0gG9SOBLYK8_VXCC86XmKpU02lDPfVfh574Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHi5c9-FHS8-QGeypFRHvH3TEyHYN-AW_TOSouXDoxa4BsiGSIGaJ0Eo-Sr6CUb-JIiGyasuIL4rI7VDXhJBfDzehgdB0xkWRN6EaCc6-7Kz_xEvBGeUFPXszUhFkfSXV9khqXm_5BZqUqUvU6RolqiBvfHclt7wRcQMNOIsVbcUqb5f4CWYgiOmgASqaZdkrwHAyiRWkNG4xKGuVs2EphZ27dIcWbE45aoH3qZtTmweargcasM3peq3TimOdefF8X7XZ5S_ubchVLFbdzvJju4LGI4W6e5g0TVwdxaFU6iPRLUizQPm3HspCANhYYDkrs5F7QLHUlAnkuzR7OrNSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9VnE06oP2lfyHGRfLfXWLl4AzCcwt5wb-7_WZP4K8vFnYwzMEDcN3Z6zrGu87VMTG0mTGGbPIu3zeCJW4_zV-CH6ohS01GBm65l30M-xYvv1vQjED5hYOoQmX8D21FNKHjQUIr7gsL1jGH-zEB5_-Md8CC9WE7Zufa8DKBgIa27d-icmMlLPJCY_faFssHygLk7p1m5jbHgczkWxp2Z5EnNac0_vRNllcnaplIsBDrrTuY23u5bdqjE1SLLuMCMzJmvNrhP4JW7FS_Oou82tdRNi1R2LdXTStHxgynQAD3yQY-wKRVm31vNkyCy0fxTRpF330av3iPagnByuC7Q6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCnNTw-5iauSaCfv_TwxEWpQMO_RhTRSAHeLH2KGFSsRW6BOgaDE6kTDQEVbIuddNfGjSTxounT3P-rzuVJu9D0tlAOzwxJB1rClU6eIUu9wIiu9Zu91bOTcii-g-KICiQ7_V4nsb3_jDyUKD4WTMx5o2YLp6Zxh2TgCdcWPQLvb8XOxKtQCswYVH4Dg-Tdk2U81Mo9Jf9YL8uI7EjS_JdSu4WO559x8IU0UcFG_f8gVqT0NHkBEq3M221QGxioXVVwspAwoUHVutrffEQhXClZROGmHYzDZ0cScztpRjIGY1EU-k5eBnFuYCX3PBB46vEXQRgBfR_hqnlPpco8sQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVbxWBeg6_4AYyAFzRAu661PcQpL3yEX4ugFP6AmVh_MWHfD06-Xj4WpIHFmgR56iG6E82IsF8GXOUDkMvHwIoOcD38BtS40aTSZ8TJRfZcqDAh9vNhCSBbtuLgILwzt7LV3gI4rJF35SJ8IyrzXC94RuMaH3hW6crSDXn-6Xq4QVE3o77ATxFf4iVy1MaSkt5MkNds96JQwSn53ujaOHE0AgbmLApMwmPnExEmOuff1tHM-ivJGEGjcFcAJQNCdvKYeb7w9orieY4iBE93pQlqmZhOa_Ucj1vFOYqIc1VBobqdbS-zoQ8SGqlHeHetwqzeIi63z_n1HELz3Mzrp0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlUAdS89jJqDljgPo7Ns_JxYSG3cvmPo9ts_o5GOM74l1nYRbpfeWI2o2T051iqMZ8TPfh4lK3hW3bjmOzPQBcLYAXCIFkJbm5Ff2Q_73SO9hpjo3rEVGv_Tlz-H67q7O-sO2-yL1f72t0dSUTV_WUOfBXu0o8_w17Cdz1nCsqPchvAgecXzjTrq_eL82qwN6ITTjyJnHmF5Rhd4lBDHA2WO_LokWR7okDule6Ojrf_cl9sHoDhgoSBStOU-KTH3ngsteoelqe5iZmS-ktuJK8dx8yDqVX2lTHza3AlqZcmxKZ-3Xgkep3Xhm0c3dt-cLapnRqvgQ7xJEwcYBYyzKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=WnGf4R7mK8dtQ9ZIm-0rPjVl0X46Rtx6P09-pFeidf69FP6Xh_aFxCXXeMFZxd5nqXg_FqcGUDASUrQVZR_Iy82LBpcC16hiyCXBdQ2CMiqQsmBYCekWo4UTyXUkZfHerU97MAyaHQD7-Nd88gA7MbwDq4CiX7YWyR6IM2vvh3j5SND967Lyb2-oqtVuy29QfQuQnUGj8E3_4cHdEEztnb-YdTUWK7x9fsdPxL27AyQ0rfPswdY52ycXely9k_cDItHryWSQZHnHabIIysE8BUL8x68FDNsxjktWNsz6cA-bqq2LQQ06YXITwRSETzgWPtH3HnrnTLc9MesZC1K_Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=WnGf4R7mK8dtQ9ZIm-0rPjVl0X46Rtx6P09-pFeidf69FP6Xh_aFxCXXeMFZxd5nqXg_FqcGUDASUrQVZR_Iy82LBpcC16hiyCXBdQ2CMiqQsmBYCekWo4UTyXUkZfHerU97MAyaHQD7-Nd88gA7MbwDq4CiX7YWyR6IM2vvh3j5SND967Lyb2-oqtVuy29QfQuQnUGj8E3_4cHdEEztnb-YdTUWK7x9fsdPxL27AyQ0rfPswdY52ycXely9k_cDItHryWSQZHnHabIIysE8BUL8x68FDNsxjktWNsz6cA-bqq2LQQ06YXITwRSETzgWPtH3HnrnTLc9MesZC1K_Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvRBQ8NHwhfUbOhqJkT5V-FV1mYtxot1nznGleZTemuWyJ1eAEMqwZQuAeveoa9SGjapruC9KlnO-IC6OmJd1FJOwhTqaxnOyKXFQfdxuYElvkYlHwN48P01OCTcjmYn5NsFVnjtcUB7QUsNSpYY4dfqVsNyy1XdTBYvnhzeBJZe6yV13Sc9lNSaPJ2oK6lFGDsn6AwYEx5Ni8tr_mdFLTZIp8bxxq1xOSEiUxV_uGiqBVWtxFgCFbAGpeo4xRoUzGikwyd4Mmzk-1Lxyu0k1Mc8c5OZNYN8gS-SiiG_GUI4ENGb4yNLS6ItEWyyYSBg1GAkAsQQaCHl8CyDdsGVYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=a2bdzsbq7eX0PdPDE3FRuD4Gyxl16z1kqnXO-pxdBE57KmXJvGuJ-kDD1E72YgG1m0MRVnMk2CoXe-mIhjfo21zptmLFsho1-juoHwm139WKxZPwvfYjlVz-61ZP3exr2bPsIk8Wf16fIHOQ7aCMnF4cJnkLFTPg0R3SUXf8QrRDbtHPBi17MeMnYWIpt3u99HJ3DRuKuLKl_mW_jqo2a8bvsWgyZlm0QvTkbR3zTKBE2t-HxpAzmdHPineHspeBSf41G4japNOkelLnWvbC5H1l2HJoZEQ3WbvHqgpy9LPle2GcqW5uJX1ZVYJvfvp0OAVbR_3lCz2pOVXFmWFvpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=a2bdzsbq7eX0PdPDE3FRuD4Gyxl16z1kqnXO-pxdBE57KmXJvGuJ-kDD1E72YgG1m0MRVnMk2CoXe-mIhjfo21zptmLFsho1-juoHwm139WKxZPwvfYjlVz-61ZP3exr2bPsIk8Wf16fIHOQ7aCMnF4cJnkLFTPg0R3SUXf8QrRDbtHPBi17MeMnYWIpt3u99HJ3DRuKuLKl_mW_jqo2a8bvsWgyZlm0QvTkbR3zTKBE2t-HxpAzmdHPineHspeBSf41G4japNOkelLnWvbC5H1l2HJoZEQ3WbvHqgpy9LPle2GcqW5uJX1ZVYJvfvp0OAVbR_3lCz2pOVXFmWFvpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=om8cxolDtUVY_rt0yjrjECExvMPz-f6ILd5dpqglE2SI-gzRqvwAOBa1h6HS0wRfRFiZXjWuh0hTbmm4D98i4OvV9aMzrP0C1KnNq6lbkKIfUIcIdXxDnNSfLWEuNi3Yj-0Xxyzl2TlnAiOYc-IKNMnyNmrBo6wKDHQgNIbSuCxXfGR3XtlILHFSbHs-k5nQ4E3IF4-0Cw0nkYMdnD9G08ocKOmtyRESqkvuxA9_JH2PO3t7Cnk8CsCosnJSWB9VukpYHaGng83BOUJTWwxXrXj2d9P07cVsQcfRGw9Ai1KsYC5ysBMNfYy_4XOHIezKkCn64Dfp6tg5lHa7LsFyEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=om8cxolDtUVY_rt0yjrjECExvMPz-f6ILd5dpqglE2SI-gzRqvwAOBa1h6HS0wRfRFiZXjWuh0hTbmm4D98i4OvV9aMzrP0C1KnNq6lbkKIfUIcIdXxDnNSfLWEuNi3Yj-0Xxyzl2TlnAiOYc-IKNMnyNmrBo6wKDHQgNIbSuCxXfGR3XtlILHFSbHs-k5nQ4E3IF4-0Cw0nkYMdnD9G08ocKOmtyRESqkvuxA9_JH2PO3t7Cnk8CsCosnJSWB9VukpYHaGng83BOUJTWwxXrXj2d9P07cVsQcfRGw9Ai1KsYC5ysBMNfYy_4XOHIezKkCn64Dfp6tg5lHa7LsFyEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1Mw2Gp5Ktf-eMPm4WZTiTD0lMs7q0PjS5daHsxPj7J9lt7RonCi8OSFvi_IEp8Jng8-J812oqXQs10j-RPgv4Ie0FHZrSIrAyte_sDexo1hPZMlpy2lmaVuGzQoIgnH7pyTo6w80bHOCafNtmvR8X4xSk13wMxJEDd7srlFZo6PjEh6dR6CpFgfLGC-rAIT18TiokJ6NfRMOJNbKMZNsLcIlAPCtmwzDtKELCrylCFioXV3Jw3rtF2UqTqtwLSuVbDNdYxQFDNLq5jfTv09rs_I9MAE3s4dx-T42cpwtpHhDt0qXLzwqBy4xXRjDZClWXSx3U-LAw_LA_CRm75tGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKnwdJASwO-etmtxI_t1ixAIlTPRVbs5pp0UyTv-4UKtU8MRxF2bd7UJdycQPkdFI0gv6IWNZzqHC0chO1vyzQ5196Bon9tnemFLvfD95ZRsrBUvE_dAkjbqp-zktI6UcIN5JpblT6OXM6rtFyJfjm5lD3I2RKMafLxORewwN76IfE4pgfjjVzdwN0DfTjt1XUQMOPDI8_iW5RD75tWiSvOWtsXvjufp0HPiDUtNQCOaDZrBG-1NJ0wOTar-ekeY1tM0lomFmC02L2ezv7OGF_zB-nthS5ePh4jSfy0LAspPivGj2EF8sJ9ldShrd83eS-qZVpIf1q8si-DKa9UdBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با افتخار می‌گفت ما مشت
و سنگ فلسطینی‌ها رو به موشک تبدیل کردیم!
همون موشک‌ها و ۷ اکتبر،
قدس رو که آزاد نکرد هیچ!
غزه رو که نابود کرد هیچ!
مخفیگاه حسن نصرالا رو که تبدیل به یک چاه
با عمق ۱۰۰ متری کرد هیچ!
بیت رهبری رو که شخم زد هیچ!
رهبر فعلی ج‌ا رو که از ترس جان
به غیبت کبری فرستاد هیچ!
حالا بادبادک هم نمی‌تونن دستشون بگیرن!
اینها همه پیروزی‌‌ان!</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
اسکات بسنت، وزیر خزانه‌داری آمریکا :
‏
🔺
امروز «عملیات طرد اقتصادی» علیه جمهوری اسلامی ایران را آغاز می‌کنیم؛ هدف ما قطع تمام شریان‌های مالی و اقتصادی این حکومت و منزوی کردن کامل تهران است.
کشورهایی که به ایران متصل بمانند، باید انتظار انزوای مشترک با این حکومت رو به زوال را داشته باشند.
‏
🔺
خطاب به رهبران جهان می‌گویم؛ امروز زمان انتخاب است، یا آمریکا و یا جمهوری اسلامی.
‏
🔺
هر کشوری که با ایران تجارت کند، خود نیز منزوی خواهد شد. هر کسی که تصمیم بگیرد با ما همکاری کند، سود خواهد برد.
‏
🔺
به عنوان مثال تمام شعب بانک «ملی» باید تعطیل شوند.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=pgk_kH9oVL39hGdO8vmviLNUMrHOVHcy7R8oaCGideXXG4cxm-xbxRin6dgaQjMyjy1i5SMUIB93A7GqHEilR-uutskgYHbqBllM91OzY5qoswbjZ1j6S1zIXpCb-70pKIqaM3RUlIFDhMyV78rZuEff243mxrSZinyQ8sF3l1e43MN74R4aICuDpmwak1AztB7L2Clc57nLKCgTrUXPem0E_UUOtYRAiVSAblN1IZR9-tw0pjV76VSs36O1WsL_NKmMbFScQj_69HgNSg7FsTYrwwPUjLN5wgywDTlDMJphHuN4Ioq-wb9HOzjT5fDrHTk95_N9v2DdHoMLtsg200y1RtV5jreCSQ0j0LP2RoNgG30raQfoMRqHL1GEyxjHnZrJTtNL9vPO8sTOhIutWdfH-S1KPDik9vPPV3BdRiJjAJQ4ng6I4HoPyydOieofmdULec6csDCYossWrcYGOffNZ2Bf6-wTku3LrHGBzB3FfGKFt73w9pU87aaUUwZRZfFju6att1EWoCBQ07allAl3ySUjM3llbsJSapO-2vNPYht5hALpra0-bqSvre_SMoTMed1Lbnb84EmzNw-JnHx04-o-hiSBannnkIegfO2iHh33uGM1LKm3M_VypeTQop9sXRmfayShyB_7bv9MAzsmXOBFZzkDZgw3pmkjfRM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=pgk_kH9oVL39hGdO8vmviLNUMrHOVHcy7R8oaCGideXXG4cxm-xbxRin6dgaQjMyjy1i5SMUIB93A7GqHEilR-uutskgYHbqBllM91OzY5qoswbjZ1j6S1zIXpCb-70pKIqaM3RUlIFDhMyV78rZuEff243mxrSZinyQ8sF3l1e43MN74R4aICuDpmwak1AztB7L2Clc57nLKCgTrUXPem0E_UUOtYRAiVSAblN1IZR9-tw0pjV76VSs36O1WsL_NKmMbFScQj_69HgNSg7FsTYrwwPUjLN5wgywDTlDMJphHuN4Ioq-wb9HOzjT5fDrHTk95_N9v2DdHoMLtsg200y1RtV5jreCSQ0j0LP2RoNgG30raQfoMRqHL1GEyxjHnZrJTtNL9vPO8sTOhIutWdfH-S1KPDik9vPPV3BdRiJjAJQ4ng6I4HoPyydOieofmdULec6csDCYossWrcYGOffNZ2Bf6-wTku3LrHGBzB3FfGKFt73w9pU87aaUUwZRZfFju6att1EWoCBQ07allAl3ySUjM3llbsJSapO-2vNPYht5hALpra0-bqSvre_SMoTMed1Lbnb84EmzNw-JnHx04-o-hiSBannnkIegfO2iHh33uGM1LKm3M_VypeTQop9sXRmfayShyB_7bv9MAzsmXOBFZzkDZgw3pmkjfRM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDAyabxhb5kyJxUOYd9oOKcrl653j-BvjoigAorz591hhwyfs8kr0MofsYAv8IVdCOB_KQxzG3xXBJrI3epxRGTQ9vpAxvUW_xGSEpZfAZBakiJ7vVBlFYNk9-oWGvW9NpulJlxzZzK3ONKw72epdgrFMKG2lkJO0M_n4m7ViAtUT7jnURazfq489OX2l8rhB2Mn0qtc42c6Za2CyojtVRsdPIJ7MDcLgwuVNOvK6oqEd58PTK5BKx6Yc9HafDGKbbiZ9p73awLxsVSJiPhTczV37iNzv-tuztD9g9Pyzx6XuKvT7PxoD2skYfKfey3YJVD1MDnC_l4jTiLL_GtBlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=Mk8c9fqkdAuR1x4kIQkEyU-DvSTg_e0-n_Qu_CqmBFN0aoO2-BmEi3OwMkl-Uy51kyqegz9VOjOgW6EJS-Z3DuyZ5nSXZ8KQQOqkZ8TG1mclpxdDgvuS1VNI7FMyXf35s3Ptb93WwNQIOjF0i6gDPgKL8p9fJVhaZYzl6npfzQbr49OoNXuaKIPowhw-KrJL1S-OY3j289e6PpLelBLaZKuhrH2YHrr7B4qPGjrhti3lptxKYIwI1F7SuKodPiRSwTg0FhKlNUC9VBsFScgBSxbpZa-m5s9Xyk0h4eeT5SE_zDugTarwuIiHz9LNEGvMIVxgCQDZVPZy45_t2ao7oJV08dQJFkd-S0xUWRP2EoYY7tl-IGtmwn_zCpklRLx5ZA5YZwNL106zLS1h4QroL_nNF9AXfCo7hnD-IyvnsO1j5PBWaJ8Lu53FtudonTAiwHg6zXB11CQoRO4_6jbiPUqUVNPDKtFI5bZkPDqPZWQPcwIeJEesAxZvU2x6ctI9Op44zCXN1f-wlScWGBqp9Bx4jHl_p-MC1sybitEQrKYEbW0OWBgfG0mKqBpxJGW_aj1riU0Mqu2RPeQNsoiPlEVcbUpAM49szNdx84FAdYMJ26eTDMVfjnmtqu6hnIi2FYXaLjCcTVaNzw0Hw1CSq7GqtYm_Efylg88J1RyuIW8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=Mk8c9fqkdAuR1x4kIQkEyU-DvSTg_e0-n_Qu_CqmBFN0aoO2-BmEi3OwMkl-Uy51kyqegz9VOjOgW6EJS-Z3DuyZ5nSXZ8KQQOqkZ8TG1mclpxdDgvuS1VNI7FMyXf35s3Ptb93WwNQIOjF0i6gDPgKL8p9fJVhaZYzl6npfzQbr49OoNXuaKIPowhw-KrJL1S-OY3j289e6PpLelBLaZKuhrH2YHrr7B4qPGjrhti3lptxKYIwI1F7SuKodPiRSwTg0FhKlNUC9VBsFScgBSxbpZa-m5s9Xyk0h4eeT5SE_zDugTarwuIiHz9LNEGvMIVxgCQDZVPZy45_t2ao7oJV08dQJFkd-S0xUWRP2EoYY7tl-IGtmwn_zCpklRLx5ZA5YZwNL106zLS1h4QroL_nNF9AXfCo7hnD-IyvnsO1j5PBWaJ8Lu53FtudonTAiwHg6zXB11CQoRO4_6jbiPUqUVNPDKtFI5bZkPDqPZWQPcwIeJEesAxZvU2x6ctI9Op44zCXN1f-wlScWGBqp9Bx4jHl_p-MC1sybitEQrKYEbW0OWBgfG0mKqBpxJGW_aj1riU0Mqu2RPeQNsoiPlEVcbUpAM49szNdx84FAdYMJ26eTDMVfjnmtqu6hnIi2FYXaLjCcTVaNzw0Hw1CSq7GqtYm_Efylg88J1RyuIW8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIcfPuC0n4Fw4B2yfKn8WOWPupgH9rCYjOvkKVIFKc6pt9qaanBHZbtK1LOrG1pm5iVBvWvjxkOeuQ3sEb3maRVpiN7ZiRrjMAQK58Y7b8YQuaOUeXJkvcNgTHz9C9z6w7SiJg31AfrWIbI9aA3V7dMrD4mPraBTtNBMBHAQ1BWzGYtFB137Ey0H8zXT5WW6EolcjK-VwhAnlUC-zGNr7KQMhmXZjuECOtWpLXrqCZ0UXOOcGntA1pY-jT8uiYyF7t3N6GjT8TbhZ4TUdfMxMg5TetnOxuMwksPLHwjhh9WMx-8fD2o5ImGqlpPnlhTAYqBoVSApLPxq7rKTB1JaVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJPeKa8GCtcNHDu3dGdl4eehK_ebUL3c-llumYcVcJnpEk09aUjIwNg-3FKmYfxmvONLCa7AqTGyKHk36dY9cwjURJpj7kKL_7nKJuv0ZX39k1-OMcFPI1AA1GgXBs_QbBhzkP_k137mf1p_FDXgpINmPUY_C1UUsXbBFBmi5Xjlv1CoEvZTuKbYq1pl9hI9P6u_aRwe8kY2zkdQo4WhJs5mhS0C_hZaGOhYazRjsSxjNysp50JYn4Qe6vcgszPkjHAdSzqMi6QtQHtsOHVKciS8a6aq5OPVxqv9tzfyiYb_jGWVXuH9JM4TI6MoVXgmDhTqd7yZG66rRbbORO5iZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJpECRE1UYnEZbUAOBBMz23JdOmtYpWwZfxIBfn892vTv9rendnvA9DwWThF6OMBvoud8RmWrtPEB3mABHhN5J5jSxenhIKaPJXRUF3InfNLjJurHD47MC_fcv8s-2DGgnEarCbDdPVCgZbCZm9EUse-MQ7g_0xcmsPVeckdNwMFRmX2wCnzVeGJQBOkDl_2vKfhHnV6c0PAJrrQKB8RC5bI8gOZpo9FJPlmcPTlxHPG2FFOWuRWoPZQDmIJMmnshkzSE11hUfnxXiZddg6mU6CrrNiCJ9dBTi-EYTcc0Kz652qnWmfWxQU8zHDnjMalc73VsTqYzLaYnmNZ2ndxVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iA6w9toYUdpjRi6uvWk0FJnFbtxYlo6UGEiWQhT02i7jIQCsI55AVBoSAm70a1Ap69RRQB_8QThzT7RG_6VOtp4TRBECFb1Qq8aAHZSdxzC5b_FrQMpSTT_dFzOrriElg6VtXaftXiUdVO9LELrTMPqRsFGucV4mZcIv-8ISJ66ikXUQXS61vj9-P561BASnVeh6lPoqylHucmub8MRN_Q_WMsi_zG1wm2HIH_-E3HXEsdE6inGOX8qRck9jIPxve_gQVKZHzS4zvbkkteOWdXvkSaqPGhNDcCO6JT339XsjWeVfWtBspicNqiIcdBTWjcM7A1PZgMDFa0wSLavKtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7txNhqwSMxF2sdLvz8gzcUah7gIM9TLsAYcf3iFt5muUpT7pLbND91SurPPASVT_tUS4iQHxHK78r1CvSH1DQ7AQfYmUOLNN5YxkcU5-6zYPJ4ftVcqBTG_IVrW08nuv8LJ1g2rCfdmF2_rbIJfor3tc254I86JdZyvyOGsJ3YJnROQowrcG42cy3ikuL6BCvpSP9hyo4RPoQ5sRrQFWNcYMfkOtaLUG2KGmjtM08LJTm6i6MpY9b1SrhD6yi5reOlNe6yBYrCqYG73vblibppVzWlBtJSNZG9k54NSA3gjP6EQDKnxTrYkqfIp3Oln40T7fFd9eam_TQuZ1iMDzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfzRPaQCVcVb_z4Xo2OxOK60bnWFkcKTSx-cLeiNzbIEsM-4Hc-wjKaAgnTy7GOKxxoAaTvLm2gf_45TAFuK0YoNEMSS114Ntpnz5uYub7l5drCViPHeDE8jHBUlKsXSpwb7OvMFKsf_S2a2s_OddEmrSaVdMsSt6wfDcn-1yehmftZH9Y3ttcQmM5RPwyeDhT1rUMCLET9IquRo2UIejQSia5blBIeujxrkS6fIQRqcGJS5z2i-sjXSY2cH5dHZyzMvCzxoJaTfEBy4MkT_neCFMObx8UhUsc_vLH94rN_IqFlh5LUTAKXg-u8NDCPnBx_R6o_R-FBLoXTnkV_F5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8Q7qw-ydtZUlleY_QL4f4d8-NPkVmZTid79sxzdHy-AiIxJsUVVA-XElNymP-lkvXvwrHfZeQF3djaj-A2IMgACkTKj8IeiTH3DBHOQyxVt6UEW4idk0DYHQ-aKVE_1E94fYFS2G44O75ir7ABfNmRdMrxn6aJEZyN3z0uRMQdIuBfMiu5f5ObPGqs-WLmlGRVixbS_XTo2cFwVxx1gnerWa7cMFpIeCvwTHCy6GTIEU1o304F8d3oxAh1qr7BUieFI1x3aEY-ec0d8hmPr7XgNPJpF9BVaFmT5oNWug6RrZ3qui98Xb3js0uQ66dQ7Du9F38f4rJN1z8JLGisSlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOOC4Y9nHmo7oh1m4F5kEyY4rjRH8lMER9hnr-criH_xU99u8uAFVc45PE62YAsWuxX8mWRNLIpdNMIm3ndunoLK8HzuPyeS_EQrYhui8AMmzAcDbIdlCe3tsPu9W4jhTpFmjybyxEJxM24GyvMF1Al6BPoADVWXkfZkZLxVsNvZdzUKs5R-4V_Ajn6YncLV-IrR47jEI8UGFPF85se8Tp9oRkAG55htAH4HAZbZedkytDUSqlhGhqp8VvmYq3Gsi6KIfBK3agJ6XZpHMbbKSkH8UksdUH7TwP1QnQNuBbYz59UE4nc-FMzhYy5D3A1zH88qAbUorjIau3xE0u3wKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScE34M34cm5U19Mo1CLyQByz24taaGeancMmNBjaOV5zs_nh6ed2VcBQm7tLadeKwcbACKm0MHW54-ObDSfjZs2_VrJajrUMhziuWyf7nzcRLLoWf01Ej_g3IRP_4TmPFJJ39fIgPOAiGAqDzdcVDqkSFqrJ0mlv7ri6Tez-Gp8jXRloGcaYQ1dERRpKOqhQq7oSGosi1UIytCNmg06W55BHg-y0Kitgfog7Z4BSJB5dUMC06CMhKNHv-82jYyVLpahG4s6NTijc7AqSBjRRt3vSjnaBSeQUmFerks0Zo223nhwwD1tFsJDe56DBe_t9MA_WEJOVrpssJAVwdfqLgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k66jTbt2dOQ7vFRQy5qd86i5vWBGYXzfG-gxMd4vGtOVfhUxS6rFA8jwr5Z1-zd8CbxwDd4PxULipK1AqktET3oADJc8EKztDv4Pz5bKGTsUfPyxwMS0C2xR1yLFlbEDz1F_tFElarS4z5IplsPUKn9RSB25qbJNgilWjm7242bGYGYz_4JhbZ6ateeLInaZl5neIh253kaD7Tc4znBSthNfalPFhktnPRrYIJmeORDSzh7oa8zLB7j6CV3scE7Y8jR0M3phIbsdTZj2Wsy9ipHALH7t-pZJnlgLP18c-Ha4L004Ase2exHcjVUUxGBkIgoIm79G6_co_yM1b6O66w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g16MF03kiOVH83GMTRPp5h1FYdtndc9u_1VU42hzIUqVhtSBojWs4AVnLmGq5FI9Nwr8u87WC-nrA9x5h5Z_mxVwSVbLHoMaGcyM4vPuJ1OwjjwSm8WpVEXvQuGEyPxDe1zEqoBfRuGGiLbNdwSO5xZEdH5pk6LG3Y11NmvDEa7uB9a-e3r_S4lgvgaXpWYJm9cK6inFMzeJWpEcDgJVzeosmCa8nAL9UWXsA1ilSLOusZ6vndVYHBUrjvYJVssc4HEruSMtOTtJgkWVHIQrPMNodhkmD43UlJiNvwmFLtdD3jRBOw5TQKH50j3kY3pgGtJc97VeckMjiFjG1oliyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4wUQnHqr5DFSTthxpuPMJq2b25yR_27OeTEbtBzaHTzb9hE4ZIKSAqEj8X_sD8BreAuroaIqAH2jx6-46ErpcfCQHzseRHS2qXSIzfLikPrPuBAvP3lLaNvwUyS7qOCmC2854FguF5IhxIATrR9mC8yrA1HdPCiuyt2gxN01-ejppN8WydqWSI5OBaYh64Y3-37vEVQJj_4ZX_x9z9IpL77T5f-VAGeBAV40FR_ioiYdoOXmq5f8ipgyaslSwlvykciaLFa4yM-QbKHSq08XrXQyQwowUwKwD4d_mPxIIIn6Pnot5d68IK-eozlJw6qs5NHxvHydhT_vcw2o60XJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFCawFqafdmgwtn3hCWA1Cd0JwemuUJ5xSaX8cpzBeylk-wKCWDYHvxxEgJIrYFwSIiF10sCu95velQfZITIQnP1UUV0tmorBzI-gnazk4xVRDTEIRFH7sXQd8rBUAInPLC9zM0UnFNt5NSCTXc8uj8EpJSLoVjXQ9kApwgFaPtLbhczn06z2qbcRJnypVeg8oPaPsqY-ziKkSKqa3yKwOj3WIIXk1qOBS_aqq_fBRJBkqxBvh54B4_UMMswCt1Px6mQRR5PmiM3Icq9ZEmgqy-ukcLwODvPZZyqal0lzrkYYsAUN5kf1fuCH8DBT7_REhJb6y_v48rRRq0Xe6muGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plagyozbik9cmUabx7ukzN4RseXa0MhldSwJDBcssNMWkEHHajiTxNyGVP9q9EO0QVNR9BTeX3v2JCfLFnnFco1G3aZk1lkYN6y0IhnoeCpDTkT_GTRamz98S9xd-53IhJTqtKSTiQVpz_a8ssGYUjKPNuwcrZiEGIdCwVEajL_-AhayDo5jeacQMfzw6iKyD_ac4K5_eCiXd0ZVoge63cb2Ml9qyzw-neXga5kNZDsuT1ctPLsOMcg21Uknyd7_ACMoSbfRbPCFrqjqz7Zh5i48reciua1kH2DpAm0T00YHOhkzE60ROAAqKJwlXWLBvsrVFj6m6uBOPjkpGi3t6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند
«مصدق علیه دیکتاتوری شاه بود
و شاه علیه او کودتا کرد.»
ولی یه سوال! قبل از اینکه شاه حکم
عزل مصدق رو صادر کنه،
چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند
و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟
بله! یکی از آنها «حسین مکی» بود!
او نماینده ویژه مصدق در خلع ید انگلیس
در صنعت نفت ایران بود! به او «مرد پولادین» دولت مصدق می‌گفتند
به او «سردار ملی» می‌گفتند!
او دست راست مصدق بود! او مسئول اجرایی  ملی کردن صنعت نفت بود!
اما علیه مصدق شد! چرا؟؟ چه شد؟؟</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6616" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5gMurkMetIfqdQe97bXexGb8lxMyJiJfR3KFOkNBMwPind7L6KKrYdkKACmHGNOOR5jDoNiiUwge3b8IfPsNgD-c3eAk7bP3xo6pTiKhdZo8VmoHKWYcofj0wsSxmtVx-LgErq9LswmUIBxGOqqN7TMLwKdB1rrjrk6-rDr-f-CJj9uSSE4EaJsz0hRefxaU_YIPGbcIACtUS70cyQqsoUoS3xdB2uqO-gzkomFSdKcyTjKPXyBgHCG36cg3RkdAFkfORnuCxi8e7RvRyO6eqSQAYhFlCTBD0Qo2dGWz8Uyx83VtjoRURmbmVrjomK99kb_ZZA9zm6QT5M3ub9gGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bi9rh6rp_XQ5P89P8nX2TJH7xK4uvYNGm6efws-DG05BTcxdfZkuvwOmENSPuLYtFoGGjV_aBgqlkqJO9iFAqy7jSXQdpZKxFc4XErigET_YdVM6Kd8zijCui6wdYQQ_LjAJVg3EwA-ObnQK1DsjeGRP5fKuOXODO7r3um3GSDWhWJbwvJy8KtNUz4zJpk6XY4wibVZ0Iet3wzx3hY8bEFvUZbAoEVuwLw8tGeQ4hgt-SglEQDXZJh320YDhQGpu_MvKnh7ozMhU_qDeXTS2RvXjCGUSgHdRZ8YUspD4xiy81RxLUW49ocv5xrIoyV9vEPMA01GSm-mOoqMIuxPpPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rwXLTRtXQ51mHnVF7HMNuktLgN26kyW3BM8UTKPanIrM7LO8jVxmFnsAfb26bXOW1OzDzuIzLjXaFMODJkSlABhfknvl_UMBi6oe86KGIoZvF6ULi7pOKKWX9t5wIYbEGPY02P3p1-Jitd7_6sPPxFnq3wIayWD9jRZHmjTiQ9Xr03SKDQj3s8zrYha_vWP5O7f6WtRQY0a5AWMqbPUrazg0duiA5MxVgjkGWtiBhxZQzJHx7C5fIt6CkwKZ5tsKOGNs8sXkTWl7TqML17P4cc7LeRB53YLpt1xQH97J3lbiELvlMPZ3ml849OKFLU27Vn1KCxrZkVXpp-w0pMTLsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IQIgoxPFDM94JenDYv8qfztLO_Apo1y9m7LRg5anlB8OIHBWramiG98kyu-rQ8OCkhqm5nxAsKJFmMKJEsOJsLZr1uq873eHRsHJmcYlCx4HXDvLYHuX3tO5G0Hm8CdZHDYtBNcYLwULgFjy6kdjK2wunwYqtiNXbUet-YcomknwSV7QFlnlPetUy8681T5eDf59lRcJ3sweq6sS_e9VNtH1hjePOHN4MhARSEPaF1fFRH1gloAmgwVGlgveVhYl61UMKsadNEvdFz2-o1fg0IB_RPTcNqNhn7mTpS_iX9IhgKtMtBF0fqVlfSgLdYiSbOgoz0La3QIILiIeXBJBNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urgLtsKWtPJVZ1tcQ6IkQj1RhD8-dOPynkVBfSbgDIIMXIblB8_ul1y54o2FM39yw1zyVpbPq5aSL1fZ6DON70fDjlerc8KJbX6tOCP76kyLkTsWU_RfwDuxuL1v0b4N3gXDYAAivBUXOszpDzsfPmviGeYFVJbqkV8juqOXha78aEXfw90LE3bmMrSY8vWWduQDm7_ecrJk8zcTNkyBEH_JvK5znCoFLhjsPBXxKPYNws8p4B8QZhS2sbHtVyIVJMsIkumnHryAr9pC9Z3znuCfWaB3mEBI_sWJA3h1cNh4D0V30_-d30xdTHzlwdHVfV0Y83o5V2YKFSPflvHzlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kd4mU4X5qnIVJDdq4aBFKIkLeELZXwioXFyCmUpFIdtq4Mb6OC5_L3F2Mu4Ie_na2B7s9FFbwMybG8xj9eP_ECkE4xh0KZrJ2WIRSoszCprqmMego_4nVmtrbCkY59w_qNjYO6eGZOkUCkahITOLXPLAtXcROsKZ35PZ00UMPHcBhFNU7pvw7A6ewOP3auh4O2vQb1RTRwc2bQXODWOyYBuponNEN12Qfp_44KlYJEstEMVMzkbcteALz4KroMrDJ68zhAVLnVaKQ9SSLVX2ZywuDps_nRv4S17LKlaa0IhM8Aa-s7g-rDj0A0TVytVKGgU_KG2xosdFBqpW6Ht2yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4Pm4Fi-8UT1e4DSwhq5EX0mWV0V9x3yc9TRLfI4f7GxEgv-jf5b5DwW3nXvUB2yDwjC9Q6u0xaZNYyQkalO8vkJxhmr75vpb9m56mXry2iuAd-Vo8RjwiLv92xH9gRDjes9f9xV9TxHqZ4KhA9XLg1CTsD_PNACWwdBXpevUiBJ2yTp0bqMZ4D1d6YD2GNN2HhI38GTQh8UUGOgzFlSaDvPgeAnA0EWxv0Ov5Rbbd5N_UsoxQxh2YhpBOoPInMC3uaQ9pu8cfD2_qkqDFifrvvL00RXRfilaJwpOryCgkoRkCzQPVpINap9LhOmAkghzRf5nPnbhgT9KSMEybDMdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jf90pxLlZZWD0iMDkvHXMmSG-SqdmbrFkrKrqDwqSzfkjwugJm-TFfvLwZyjK_9wT2WRsHS3U9lqgGHY0apbAQ6QJhmEvkOwkHUs29m1v6HJZmzuyvKe26yu4o3NKum9u3IfTm5YUXVocBNtt2sQbGwNrvSOUoBnkYwgYPNpQw94etdsLlObX0boq-NPaai25baUphDnsLLsiTIAPAc6NvW6bzuEIVS3RGimfphxp5oAAkhocjfAH675R7T-oNvJabhbrEf9GVTU47XW_RfkY4xMa3uYvV57UnCaUhDhuSuAWluWEudkAsNNFkU-csDO8gtzl2hPWm1Ll3L5Q1ryoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogJR6S8cK_--MdlgMappiG9ZW8vGtLE8Qy0wFxGHec_XlWn8VZgMzrfuRUynsq6xuFnGB_ICEJxvMbHNIEyCyxFc32FAAGgcdSFcMhveH2RyISYMQbToIoq3xIDS7UROFONTXpWTQA_44yr9OBxGRVE6Ss0LO5kCYZ9Ztau0l1d4qaQtFsiutwfF_0TfAAzViSuS58n1ARJC91iIZaO-DV0-iLk6XVqr5LEAZyLQTBNU7sa75XI4nTS38rMNbEEt4u9SYGlm9XUZNqReJ6G-NMakTFqAj2EoOjpCblOhspC0X7hjAZHJSAyRzGrK4HoXmam1iGr2KwmAsrWfXKWtww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mkcaca1YhViLKYEfffKSI2mBXQYpxvB2pi3HVw7MELs8g-BvZsr78g6Q0fVczpndjn2kr-M2B9CqNYDpt-aiIrbFMpvl12Zjnz-kMLouVGtrC3h0cbbtxIoGwH6LFBjgeruCyawTfiy5fINY1oRR1QCoP45TyJ3fpIM-ZLf6bNdrtZ1dlJA4DDhFQSkVgx9iJpl9E4RUGZQYxfZLG5e98S88z6IRlAsq597o4vcZLURRNAw8QgH_bjlwgG5J4-KbULBHbn9ylThRs3gnF_mZe6rJZJxY5BFGLerTO9sTZK1HMxpyhc1Xt9dSWJIlRKccx0I5qBUsIjrsiyONjRQkWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRyvnbpW-9gu9AfP_YsAV1mzoJSzqyp-k_mXJMLUoNC0DGG1r0Ke0k-f4yShxixdXl5Ay5pbJr31ZNeDUM7h5NETI0e4vQmT2weT19bU-Aqptdv3v263cBvOM0AncS62_iTIM3K7hqnZ90GGwq9jlodxDKbFy0-yl_YPYYp7OtfjBRLSZ3qIrwHwLrcfehxqKoRRypnH9ydnf1o10OeTyRziD4TUby4OY0JUZMADv7-Uug_5lD3Ibs8RIPyHJtcW-OBEB6I8qKRciWrsI6XBQ-nVpS-FSzm22eFsaRQIvfdWmbdCr1CXga1u2BF8yeDefAEwo3fDDKYsUinfbbcuGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfR-JbpGvNzhiulesnvW72uhVjenFboHCMkxDtMcGBHQJe9rE7Now5k_9MvX8SKZMRrIVvi0Jth_cwz4NxUbawV1NahO41eLAXb2cjhiaT_boI7G1cs0YVwmGhfqS6O4-Q25tgUqfvwaoMymDopAlN480qB5FqQ1viopRhUM5sIB4HqpAdQHcfCvY8z4wCQA34JEIQFfLEWA4w1xwIOeAgapv7GXAHthAsRCjqL79VpvDfWj2feIlIKHc6A8K4vCs9G5lt0Q6PmhkzA8F6sUXd9cs0ONwpoMtxTvWZrFaxXM8xWRjp55ZKhTsD_x_89ZNGqwusfukaHh0BEcDv_Nuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9AnZcniQFo4fej49zUdRaLeSVleb8OVTwOEPiSzkf2RVBrh6salc-mf7SV7Egw_0YiZoWSRtciGnrwk7Ch26xrPeLtE3BWGgZMpgFKFuqzNA-FIizk5ZbtYJRSAGDFuhJoYmysz2wkAn6uGlws4iDNfZ69VE_-fhspZrieewf4D6JsCAX3I2dVzovYYX9bYRZpu6wJXW52_YV0oYOx4-dCQKyWkHYjrAUvg_Qm8iM586P00_c3XQgjRXV1e-94X1md42KES38Ez8KqgwQsS-BfQQ0U_1C6p5AaCaLFk0L4xB9aV1scZ8ElaZplhr14WmX2cIWmp3XtRRKpOvexiuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPmMQfOggIikTddvy-2iYzv6bU0AaDQsi-RIcwG0L1DXiQUW7s5w3UVEJvXvb5knvlXEEmqUqiRLnr7IQ08z8DENmlvPP73l9luxHKKOqNt_Ztv4KStWyfycDFZVlTIKb5Reb_yCHJVsgMrsXxoqPqykP7phgVgEK3FU_EYybQ3Jx1hxlTDbTyD5grLHO0YyqVudJ425lTrXTARHtlPHOx_02XSQgvVL2KVa4lR_jTlDxYF1Rcw8uFHbWySIynBCIf41nLWWWkjeqYeiAYC0MTjr1Y38Zgx5W8xU1bo1nKWjfyvPDzTsOMUwxzPwwVk5gfkKzvd8N1k9OV5hQ81xUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e987968VxOaV4LauTDs1RjqU4b7gUqebRqbY5RI3hKphR7EMAIfvb8He29MYZz1S7ucxMw--QsZ1kt_hNc2345o2M3JAZXwzyy5AdqZW_RS7EBZI2l4Jp3MDvrKDnaKR9BNuu1uY8I6-tC2SpL4XRxgNLrp8N3N_S5dwsqdMdpQXvNryfPi6QocmTeswwTd9bauskqOJSsC0VGlyEwTMVM64I0U6-Fl5Fb6juYkKClqIBWoPtL1pkAm3JHBU6ciGp7hkt-nmoY149aUfg23GrWP31EG6Lo31AuexJRIGlZVtFaU438mtzeH0srRWD-R5ZPVXv_OZytC6G11Wp2fISQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUzISvCZXvy8w4n3XMoBXQwGWq4knNzulSTGlCMbJNBKVwTSErLLc_MUEwQefH5zx2p2jG6RF0pki04eiLb9jyD6iqU1S0oa30npXiTb2LeIIYmoCw_eZ4unBqhuqP1fiM6YVkR0Jqe84m64MifqTYCxQNBoCrba7d1mJ_i2leN4CDMZvuHVBWloOsa8SWchzMhGpL55M3DU8KsgZHcqWIvbpLRfL04C0i8rs_8IxlmZWTG9i6Qp4PSwbwOA67pMcysUOC1ia34YV33794eBYdfv2gOkhVtG1Mg5YDvSoI3hGPE4khsonobngksY8UNI49M2WQmKdaOotoHLreI-jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5mDVFvskb2PR1Mcg_zVk42nrHiSgnsGfjXpWFbH2ugcJJ7VeVEP5MuDNlEUNBqvOxOYQtzOdn6hLOaOLY-aDLd90gwcyZx_PQVD21vri-u6x0xNi62uYFmQkw4Bw63KjQPjaRpIinNOpUyQGdJP_idoliiJlZpMasfZxfHbOzrUx9T3ojxa2pQiPplU-w7Abl7sKP595B35zyXH9iEZdkSxpwoYetD8MII952FCNXLWOi2JmmE0XhT-NuJRCsXgPTP4RVMu-nBtlX3BnQ4fj5MOJs0JtdSe-Sa2VHdsBnz3EKLcLChl-keIEc5q1tXP0L2G1_Kr5Jn8ubYA8sY2jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIsqezF9R265IPXSR0l3WUAZUfoFjn7OKv5BexMHwNJjnP8ZIrk398AnWYGxYkjnGaHr2Vw1nQ94PXHUZD5TwohtBt_hxkjIdg3uRXT_BaZn4gfZ36ahXf63ligi_yG-iVe_ojuJOkaRvCwxrkaE_QdPvZG4uUPdhiD7BFp9dydIUt5EW1p6sYjg1cbuIctUeTiH__I5486KASs9q-51nimF_ebskCgXvSq9PcKDh-H6F2hr6lLYml53FVun3IOImYUp8wqRFsCrjSHVFGPme7L4e206SpKiUgfKK4oENtT5Wjs8VOO_8Rszv6jxWxwMfr7-hcUixlhDU3pGwFmSDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEEZg2fJCc21xaCoZcTVP9E_XqLI4nIk-ESmkPZTJ0g0f864j2GglyLPb_0mzueGBw_PRY3ttuab0yl91VWkWygmVzltEjtDKvtCcv1BlfAHZnm1dYpDh9H7uvLd7CLo0tvuAXNRN7Ra6s6Fi6RWYCgrmt_EL2D490y0U2ZhohYytw7ZT3pssk6IKWhGZtJaOii6MPk-2ktgQkow3J7sXGdneRnys7hlScvSg4JMf8qFewZYEil7l6bwYHQEqAoTHPVM4lIuhiOqoZiwOqmQZwU2eBI68cZm5Gk91Ifi4S5L_DVz20nc5cSEKexYTAOkOefFDv-hEGX735Z9Ymcf_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت.
ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى،
چه كسى میگفت؟
این حرف‌ها را مصدق میزد.
مصدق حتی اقدام رضاشاه در آسفالت
خیابان‌های تهران را به درخواست
انگلیسی‌ها می‌دانست!
او ۱۰ سال پیش از آنکه با محمدرضاشاه در بیفتد، یعنی در سال ۱۳۲۲ ، نطقی در مجلس داشت از آزادی حجاب در زمان رضاشاه و تغییر چهره شهرهای ایران و آبادی آنها انتقاد کرد  و از جمله گفت :« رفع حجاب از زنان پیر
و بی‌تدبیر چه نفعی برای ما داشت؟
اگر خیابان‌ها آسفالت نمی‌بود چه می‌شد؟  و اگر عمارت‌ها و مهمان‌خانه‌ها [هتل] ساخته نشده بود به کجا ضرر می‌رسید؟»</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6596" target="_blank">📅 11:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6595">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMGdZ6jzMrLkc52_CSjVQ85gzys-ZW2GaYUHadHFdZcVhzDDcxG5PItBJ0Fg50gr3U1tt4RKVaBbDIUIq1YLV9f2JzBAFA7GbR4sxaXNH2qHe9MWC4C_9MtwJ5DfDHkI_wSO6s95bWuVh5Oi31ujmxgkJ1i7G8JEyHsVYBy8KbZ3KgtkZ97vClyXoIUomkeSWqKSbwy54V0IZRjzad9f8JSEnrL9PJQcafX_0oypa9QpGxD70QirZkxLveqEavGyYY9zqKxtCFH6wj_UAKKTe7axelQNMwTJJAvwzucbyt442iMpFrXGlvuswMqoOqzHGbpZW9B5Z1yi56aWkjO2YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز نچیروان بارزانی
رئیس اقلیم کردستان عراق رسما درخواست داده بود که بین ج‌ا و آمریکا میانجی‌گری کنه.
خوشبختانه جمهوری اسلامی
همون دیشب با پهپاد به دفتر نخست وزیر
اقلیم حمله کرد، تا یادآوری بشه چه موجوداتی
در ایران حاکم هستند!
کار خوبی کردید، قطر و پاکستان رو هم بزنید!
قطر رو ولی حتی بیشتر!
که اون شبکه الجزیره‌اش
کپی صدا و سیمای خودتونه!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6595" target="_blank">📅 17:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6594">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپایگاه خبری انتخاب</strong></div>
<div class="tg-text">🎥
تماشا کنید: «۹۰ میلیون ایرانی متهمند، مگر اینکه خلافش ثابت شود»
🔹
این هم نتیجه باز‌شدن مجلس پایداری!
🔹
عقلای مجلس از تصویب جزئیات خطرناک طرح جلوگیری می‌کنند؟
🆔
@Entekhab_ir</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6594" target="_blank">📅 00:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=mlA8bwcLhNuMuq-_u3mpbyayM8LI27MmRAXcdnj4ETxcWxsPVjrCvffherxBWhObHYcEGmT91eBtzg9vvYX7h8mRb6iw7WfG5a3BxazB7mpSsvTeOsiWg78iwqZDQ6VaRLn8nZpPEoMHD-c_-ftMX3SzWGArBxTLqHZd4I_dcUyVpijDt9XX8qn92qOJZvwG2tu9s0cSHkNLr-iFXYrgAyrtASFFKS77E8TaS9dLHJTquCjS4f_msUrf9D_9fLcYy-nSgoukIDBbpsB6Uj6XcL-KhpmpaBUceLf1zVtKW_kkJ9oEZF11i5o63arYihVMOIey8gPKJKxzQasZeg3STg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=mlA8bwcLhNuMuq-_u3mpbyayM8LI27MmRAXcdnj4ETxcWxsPVjrCvffherxBWhObHYcEGmT91eBtzg9vvYX7h8mRb6iw7WfG5a3BxazB7mpSsvTeOsiWg78iwqZDQ6VaRLn8nZpPEoMHD-c_-ftMX3SzWGArBxTLqHZd4I_dcUyVpijDt9XX8qn92qOJZvwG2tu9s0cSHkNLr-iFXYrgAyrtASFFKS77E8TaS9dLHJTquCjS4f_msUrf9D_9fLcYy-nSgoukIDBbpsB6Uj6XcL-KhpmpaBUceLf1zVtKW_kkJ9oEZF11i5o63arYihVMOIey8gPKJKxzQasZeg3STg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنبش شعوبیه یه چیزی توی این مایه‌ها بود
اعراب فاتح، ایرانیان رو تحقیر میکردن،
زنان و دخترهاشون رو توی بازارها می‌فروختن.
می‌زدن توی سرشون و ازشون جزیه می‌گرفتن.
ولی ایرانی‌ها گفتن اصلا ما خودمون از شما مسلمون‌تریم!  و در اسلامگرایی از عربها جلوتریم!
انقلاب اسلامی در هیچ کشوری عربی رخ نداد، در ایران رخ داد!
جمهوری اسلامی توی قانونش نوشته بی‌حجابی ۷۰ ضربه شلاق داره، نه فقط نوشته که اجرا هم میکنه.
هر روز پلمب کافه‌ها و... رو داریم.
هر صبح اعدام داریم، هنوز چند ماه از یک قتل عام نگذشته. اینها اما برای موشک‌های جمهوری اسلامی قر میدن و میرقصن.
البته که مردم ایران آگاه‌ترین مردم جهان نسبت به تاریخ و هویتشون هستن! خیلی!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6593" target="_blank">📅 18:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6592">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJ7Ey4mKc_o5GVWuEzznL-OxsRPzbgDkanWapRSSEUr5BVVNDdaryy9pBYMynvas0dGEZBBKjXUrZZtRdMqMeshTkZSr9D6x7kjpZFjG63EYhZDbmr-OLvijBs3zuruExN-RpD5Xtq_lI1dpjMeQQiIqMOlR4ak7RGYvxl78v2m4Wc4IxgMzQFX7YNDP6KEj-m9ZpGRntezE7FcXdx_HlCz40J5Wzr5yWL9KTpDZEP_4zaFeWQySATIL4UxksTUI-wkqkIVI6MmdkXnaZ3LctoYA_sfn9dQH490gxGFFNqvAT0Bj00lGo-snO8ZP6f-em5_uvxlrHtsddLEnoGA1ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آیا به بردگی گرفتن زنان و فروش اونها و یا ازدواج سریع با اونها اگه شوهر داشتن مشکلی داشت؟  نه! چون خود آیه ۲۴ سوره نسا صریحا اینو میگه!  وقتی هم قرآن بگه  هیچ آخوندی چه شیعه چه سنی نمی‌تونه مخالفت کنه!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6584" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=cy-4SCo5OeX4OryU81QAm0WVEPgBalhx6dyIBRZPN3dbmrkwVvErlH5fLuUb_WXpyMn0SX8fT_GZ7pHmPVnLfIcgXSID4JILPiz892McgYUnVLzu9yyhwOO8Pp4naX7zgbWFRYQMFG3v4qYi1YXdxvZg60F6oPw1VT3uEligMtdBYZNyjoCYFKTPFuAA5x_76P4TP50YG_9QS9pPrvytqJ_iFz4iQ6gMpBT-dii6j46_WLz-F_sDu6QvhWm-zFtvsrMZIg39lSP0sDs9p6Kyg8X2OBfxJE0VqzfbvejA1h7yjVQoZs1LMCV71onw_b0jlPYbqA6Wow-gRtbdIUKUEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=cy-4SCo5OeX4OryU81QAm0WVEPgBalhx6dyIBRZPN3dbmrkwVvErlH5fLuUb_WXpyMn0SX8fT_GZ7pHmPVnLfIcgXSID4JILPiz892McgYUnVLzu9yyhwOO8Pp4naX7zgbWFRYQMFG3v4qYi1YXdxvZg60F6oPw1VT3uEligMtdBYZNyjoCYFKTPFuAA5x_76P4TP50YG_9QS9pPrvytqJ_iFz4iQ6gMpBT-dii6j46_WLz-F_sDu6QvhWm-zFtvsrMZIg39lSP0sDs9p6Kyg8X2OBfxJE0VqzfbvejA1h7yjVQoZs1LMCV71onw_b0jlPYbqA6Wow-gRtbdIUKUEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udNOX8IPoI9smLWAxpZncJVMvq6BSKJ1t40GIxL2wXhPKHLbeEDqEYsCohVHXEeRiEHtCXL0FWdWJGwIRyiEegHftJC9Hx0erWXNCs6kLBkimXgKvzlvKQ7zttxp-m3bkvLUkrdEimsgg2H4Z7unIwi9bqYI8sc9fDdMAgyyOUIEnzd0Bc4e5mU1KqcNCRY_ofQalD2VF3JeUdUwAqI1049N2JZzNV0UKBWSyOC4BETBNsLRE3VJynrEeZu4dyzLkE8qcG0xew-NW3NFUmRnmoM2eXmQAf4-yCD-Hwv3BmFao2J27J4Ty_fLgM3p09QFjV8wonYCvJLO481f_vmu7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kabI1NHBo2AMen1LBb86K7Em_R7USsqiIxVPXPsYjawWKZif3zAObP46DZLbfl5J2BRPP_kQlHP1eMJ7QS9rlM9OGRyDXxF3yuivpRwQX1EIkdka9bIlRmF15ds9tDJ4LGpj6uCHtctxwuwxmR6i1kKvp2qnyKw901Vtxi-2g-HucCLx6xAoMWQwRVl_PmM67M7WsEWe-3mhXkiGxnRJu5E5dKq-9ZiHefvhMyEacFFMEtaY2tPAMeBglfVCVSSWCkpNxQbmgivIWK8S741xRgpT_FZZQvUHMvLPY9SWr8hT68nYQbFTavo-MXUmhYnXzIi1Q2EGKer1GMjoAGG0lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=ZJL_7Xqzr2sXdz88xHATrnVYfizlfmGqIFX_j5HnkANOHBq1WrhaaHow-5lowP4gRQ52_HSDcta1feM3culzU5oqwiIio30PZlvbTWhY-Ai93Dp41oZ8E-cIDxOn6c-OnfPuWoMwuldv3fAKfS7ajxv_iDzXmbPvckbM9GvWR0SidewR1DVfovfAustmvUBVQg4sFjqJljAPjFzdr3TO07fI56rLSEbTMX9lvVs3prPppE3amx-FLiQLbAoTqjQcqNUwm3Ioo90EseOg4fLxgY13daubAaP_HDnWcjPY2b6qu-yUG5QlSJvlC5BBTLjw61cIramSwgnTtMOYryNqfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=ZJL_7Xqzr2sXdz88xHATrnVYfizlfmGqIFX_j5HnkANOHBq1WrhaaHow-5lowP4gRQ52_HSDcta1feM3culzU5oqwiIio30PZlvbTWhY-Ai93Dp41oZ8E-cIDxOn6c-OnfPuWoMwuldv3fAKfS7ajxv_iDzXmbPvckbM9GvWR0SidewR1DVfovfAustmvUBVQg4sFjqJljAPjFzdr3TO07fI56rLSEbTMX9lvVs3prPppE3amx-FLiQLbAoTqjQcqNUwm3Ioo90EseOg4fLxgY13daubAaP_HDnWcjPY2b6qu-yUG5QlSJvlC5BBTLjw61cIramSwgnTtMOYryNqfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpPXTinOWd_7h6T5RPULgziu9sAAVa32RR0Un74gm1sRd2ZjutmLoI_oCypJifvyGZ5__u4eKuA-UhH1HlR2WfsrD2UBY2Rawugla97YTXSQNuGn5lS-iP0cJXIGVvxosEZgujDLlCArgm-oBXjkwInBgXqC1wzWa9qM-W2EoSGfKOGE1rXblUQjII4bGRL9-v_uRe0hlSP6UbbJ9T1Y4So0ETKhZw6HbyW4CEeGDAoLqid5ngUzKDaPHnZH0osThuoxI4IPRrzztmcXMa_hDERaXUiHzmnLzzIa5_4YDt7YPEqU5ctLNMmNyiKeMkWLftwYtn4JCSBHUDuPy7bS8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه
اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد.
اما اين الگوی
به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى داعش اقدامى
ضد اسلامى انجام داده؟ پاسخ صريح : نه!
آيا مذهب شيعه، مخالف اين كارهاست؟
پاسخ صريح : نه! به هيج وجه!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6579" target="_blank">📅 13:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6578">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjhekjka2ptZW1lG9qDlnAG5rSIcs1SM7F4XvU86WgJpJSZyjOg-ms-clkjE21W6vxtL9hAA80-MEBwfGOtjQIRfyLtL3JXRUZrsOHSX9MapBs4VKAjUDiPnqRruJI8JQBoWtYGMPuN3yQCetpZtJYoCSAFF-N8s4IGYZEPXzqiN_ynZSRHOrUiMUEy-a3OVCY5GpSU9gURK0qRoBKBybxndeOyTl-OmvG8xJh2B57YtYYeYnbftJeykt9vMjnCfPJzTUamR9sB66jFjJPaFdFhh8VVUEDn6-ATBM0eCDitIdKY3FYePJWV31ebaO4CbKplOPd-n6Pf4wJsxw-CjTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLejE_Suwqb1aaGOg9kr-d2Mxt9zWmJEg1QYknLoQZAJ4MxwLKVxYjpp5vrunHLEzIKtCBRAM7WFa3apckwAYIi7q8SyDZ3dsRYtICovG3bxrpJuJG6AtbHRT8oU_RED2XFVPc7myiiHtXs1s_0gasPI43lunhkHA1aIl-I_Ad2nwC0LnNYtSh661qYiJbmKiT27eL8GxosS_l0J5ZtzsKlpjpoTvjPIlpDF4qS5VMXylCPH9pQ_lwRGKkpK_VHORoO-hNquLBusmgTlhEB7Pjq11UkcF-kHuYrBr5vx-Q9mX0tprZ8kxgGElcIe03Yca02ZggFmKrEaafmUFwpluA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=k6l-DFUWbH-LO1KPoPELaRuYGT8UionetKf8DkYYWHkFa7genhxBNXuKb8fE1KilMrhuKTrsOaE77vbKbfmx7wIO7Sml6_oXgIrjjw6sHjDGPw32rwyOWnuyZ1qVA9-yA8PrfzgvxagOyPz94-eeUap6BG6rhDnP5QdnB9eYTb6OrhLjuzHqc6g382s03Yufexn116pDdNeGcEyx-pUq9U5iLBA631N3Aceq03YUd7Xs141LGreMux_Q7Szwk7zkcmYo3fkYa8tMdkMoj4I1dN_kTP8_NWBmbAt01LSraD2MYF3tBz7xNVwDxp78rIOOpf5quVoSd489c82DsOPj-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=k6l-DFUWbH-LO1KPoPELaRuYGT8UionetKf8DkYYWHkFa7genhxBNXuKb8fE1KilMrhuKTrsOaE77vbKbfmx7wIO7Sml6_oXgIrjjw6sHjDGPw32rwyOWnuyZ1qVA9-yA8PrfzgvxagOyPz94-eeUap6BG6rhDnP5QdnB9eYTb6OrhLjuzHqc6g382s03Yufexn116pDdNeGcEyx-pUq9U5iLBA631N3Aceq03YUd7Xs141LGreMux_Q7Szwk7zkcmYo3fkYa8tMdkMoj4I1dN_kTP8_NWBmbAt01LSraD2MYF3tBz7xNVwDxp78rIOOpf5quVoSd489c82DsOPj-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=ltwu3jYywEuP5tkzHlv8Z3WYP-Ue7E3-r8nRvv7Te9T-TKD2gTDGBXeSdfgyWLYX2cArGSFhQzBvw3HxjDHW0Y_uT02xNFOig6lTThLQ1DOVPd10QcFrasF3AnfCm9PiTigz0SI9TLO2sTb0g8DqsUJpB24ielri737VBofJMrVWm9VGKN9gFs0zkNrKWj98BdXpxw0cyTlPXc5YtFafP9JoyrnnBvmk_1cy4ubSchWnFwV6ZlmijHgCaa_Y1DTGWZ-Ij80Au-CIMKeBssC_GyyN26ssSci-0CrbMlbkgxxGD-BshjH_7YAErNUv4y9q8tv9ijBmSD6JvKtFxP-Hlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=ltwu3jYywEuP5tkzHlv8Z3WYP-Ue7E3-r8nRvv7Te9T-TKD2gTDGBXeSdfgyWLYX2cArGSFhQzBvw3HxjDHW0Y_uT02xNFOig6lTThLQ1DOVPd10QcFrasF3AnfCm9PiTigz0SI9TLO2sTb0g8DqsUJpB24ielri737VBofJMrVWm9VGKN9gFs0zkNrKWj98BdXpxw0cyTlPXc5YtFafP9JoyrnnBvmk_1cy4ubSchWnFwV6ZlmijHgCaa_Y1DTGWZ-Ij80Au-CIMKeBssC_GyyN26ssSci-0CrbMlbkgxxGD-BshjH_7YAErNUv4y9q8tv9ijBmSD6JvKtFxP-Hlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماينده ملاير با چفیه حمايت از غزه و فلسطين!
«مهسا امينى به درك واصل شد.»
مگه مهسا به شما چه ظلمى كرده بود كه اينقدر طلبكار هم هستيد؟
غير از اينه كه به خاطر يه روسرى و به خاطر افكار عقب افتاده‌تون، جونش رو گرفتید؟
حالا ناراحت و طلبكار هم هستيد؟؟
توى خودتون و دين‌تون و نظام تون
و چفیه‌تون و فلسطين تون!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6575" target="_blank">📅 21:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1vonE0J8TBi-KYVSRNHDrWtuOmkTFbdhdqFAv_ubR_hKrr6ISJyOwZX4SRWeuXcz_eUz0cFQs3R7BCU2BB2aCXzUlzIU2XcSE7IyUKtyBPsVFI7iX2uyX9maeNxZHx4NtPXJ2JbF4falsKdBBcjFrK-RiwL8VErw8q_bYZbwdkctNWmEA1l53SxCmmfScV89u9izWMHfbaXxvc2ptBthGpjHb4CQ-wZdZdcubKbd0nXdNzveSfnJcbE38cvT9d5uzSqUo2lMknpJH8P3PrSahMQnr6rqzTQEf49ymjoKKK24q7-JOMOxooFfqpdqPPqC7-c4I67Q98ZPKmGvqOdxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا اون روز رو نیاره!
همین ایران و غزه و جنوب لبنان
که حاکم شدید کافیه!
همین افغانستان بسه!
میخوام ۷۰۰ سال سیاه گروه تروریستی حماس نتونه حکومت اسلامی در غزه ایجاد کنه!
میخوام ۸۰۰ سال سیاه گروه تروریستی
حزب‌الله در «دکترین ضاحیه» بمونه!
و رهبر شما هم از زیر گودال و چاهِ حقارت،
«علی الاصول» بنویسه براتون!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6574" target="_blank">📅 11:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJo7yeeAMXsmwulD79JFIGrFu_f5PcucbCRFYhW8Giuf1-JCsDvrgnph-HgYDXdKPMhu9FAeHG46uccXvjqzyKZwZ02RoJXZdTm6T9bNgAYNcIIl5eFFlx9rulBC3YFpb9XLltJQDssf797sTYHsfUN_AzF-uTy4KfOOsB41Hub46pjMiqTFIdziGH4I_HEO020vkKgOBZ4gdSAejrTM5TopHJccTPE_XCWhELo-CSWcvVQ2c_tVfCVjpOcjwmSavfbGuJRzx06h0QwrHj8yhXg8dwmwFXKc6nlYeaFOT9STlcQbdHtI6qD2KC1hxVzI43hYkqZ71-WLkkScZ4O-lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDBicT24g4VRs3X-dGO3ZhCZ96iFOve_dG9JTdW_L0bwUZw5hHuekR77gNGU1RKYk_INXMn9aNX56QW6btmtTh2gzBPxv3BiBSiA6kQSF1hNHPXzWvChVSZawaBb0xCoShnT7Sjhq5YLmL051YRMn9gZUtGzVQJRiA0d46pMe0zKYsuzHhfgc_BrYxrBQPT2vLAyIChfVvETqu8B3rcHpeTJxNvFn9kIMr9GN59emu4n59y3HvYeACjQm1IQ2CWYbsdryxC2TiD7zW8QQ8Mu47LAYp_XhsD12eTmYDlt5M9ND1e2X83APYP4kJws_88CVBaZTTxHj6Z2FaycHtsc3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXS9YZa3oevoD-T05HJKRbp7O_C5LQCbu6oIJhiJmG8sbYk5mVvJ7qTyqlJul4IrNCYMNFyIymaCt5FUvGtHIPbSwwzseeKIEAYrGG6eHzq-Axf0kfL5cmuqEzYfjFpKI6MOWQPnfcp-oOxjidmrXVFR-hm3RuoFW8jDBV4EEvnBLGBcGfhgOZxA7DjQJ33QlTziLGG_qRCn7B8TKt68BhEXuobSs-ar33EY7YzBWlKKEnWguTBeixSNZVPXOQP6omNkoz17gvNTM5xY9OqPIbgBeOKcv7A70dMTxZ-GEobq6kjK7w5d7N4Tnck0ShI_3rqYQFBLfDf0jbt-yALHIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBE4hHM_RD1zBTdf2xhJGuhFduzMuE92KP_hO1KTrVYezPmeQfYpVmcMLXUwUO57bjfhulwctCImf-HQ66r_g-Be_BW53vN9O5kv0BaGyAnYu4uiXvIXHtgUo1vttXWJ7XWrSM5VJUJYqDArUtNV_ztzoIzShS5wsvodpfHJKWRDeASdgGqJcwfHexsdHAjhc9BkzOHauXu3oxLAqqF25shQ3r074r5A-j96_zXN4mppTNQTSKHKnGQGZpVOjCkinffOpCYL6IdMbwLx-vmpKvIQqUiwysEGgHHYPVQXe76x5HqNXTOkl_jIjON-3sruULwROlC57o8VQE0jXxOXKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sE_e95gNUzB8nzQpLkNP5Q_xK1OZwAGBHrf1WDv3X_hhJeZuweHs5Ia-NAy7nDu521DMAAz6FFOYNP5lALKpsI7nitkXaWYBJpSXLGPGgWK4Qo5Wbgs0Vt4Ap-ZeZ9pMx6QaW6hjuAWaXUaeQLRwnVG_mCzR5r_WHojItOckQ54h9_WyuBppJ3lONC-sFZlla9ZiVn6KwNtQiWeh4S9B9dONqGtrNGW8jLGwGlmWbj0JxSBhCZDmwckLgFBDDtyNq8xMenfS41NnaVUobwIU7LTcEpQ-7Q0VHh2lyZ-eDp4NA9mS8jmF0SkcdYeflq-x25lV-aUGx8RqzOJDzPDDQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر سیاست‌های این افراد،  از جمله این زن و شوهر،  کل کشور و جامعه ایران درگیر یک بحران  عظیم شد، آنها از رانت‌های بزرگ حکومتی  برخوردار شدند!  سید محمد هاشمی، وارد کار و کسب شد!  از واردات قطعات سلاح برای وزارت دفاع تا واردات چوب ! از جمله پول…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6569" target="_blank">📅 10:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">معصومه ابتکار و همسرش «سید محمد هاشمی»  که او هم در تیم گروگانگیرها بود،  در همین ایام گروگانگیری، با هم آشنا  میشن و باهم ازدواج میکنن.  سید محمد هاشمی خودش فرزند یک آیت‌الله است!  گروگانگیری ۴۴۴ روزه موجب آغاز خصومت شدید آمریکا علیه ایران و آغاز تحریم‌ها…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6568" target="_blank">📅 09:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDaDlfDdpt8pVW7-v6blou-VZdlAZKnbqHS0Zt_SvB23sqkuyqysorOeYqcKgS98Tbq4ZJ4yPr0GEfgXGZAfPAnXPAKmSQXpjoeY-ANqKNqUgI0WJ05dyn-ZSJUvz8JY1zBirvyEPONB2rdH2eKb6eyzmZdoJkfGtXz3bvbPZrnMY7o-4sad00eUDH_R7g6DK76XuzcSTonkv3PSRwRv6TD0G_0dPhsbYgcvOi__jdDh3QCsad4Is58UPACvYIYk64srBML16S7dKvRRV6Ihx13F9cslj7CDyJB2rQ4pJGeO0q8gc8xxPxeDqGY9GLIRgZPxqXv_uOH_Q5wfsRGdPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم در این نامه به مقامات آمریکایی نوشته  کارهای «معصومه ابتکار» ربطی به ما نداره!  ۴۷ سال پیش بوده و…..!  توی این ویدئو که خود مریم گرفته ولی، خودش دست به یک مقایسه میزنه، میگه بقیه پرچم آمریکا رو زدن ولی ما پرچم امام‌حسین رو!  در واقع عروس خانم خواسته انتخاب…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6567" target="_blank">📅 09:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6566" target="_blank">📅 09:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=PY1FbSQp-Fw1e5_wxiYSWz1bmmqZkasUyYaHMywkpm4ytkz8C_R_DmBTX-vITRW0MxmCHVQhtUghQobDTibKWf3jsijkLU2_KuC1jyFyamSqfUN2xdiCbcNUfnsk9v8BtGqXO_M_ghCglMOMtdeTWMiTcKnVzzuo9EKyq-JZtl53WSf8In14AQ80ra_4cTFhyiAaFVy3Qbm0KMEYusCmbkglRR-3VZnBAIlhNBxR4TT4tEFy_sB7H3tdPyPKvlVIs0LoFPip1mIAkVbz-yJtm9yGgDpkXalu0VCRw6X-5ntoEh3XX_G_YT_gS2oUuPbI9EjsKJ9P3FSv3cD-bTsIuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=PY1FbSQp-Fw1e5_wxiYSWz1bmmqZkasUyYaHMywkpm4ytkz8C_R_DmBTX-vITRW0MxmCHVQhtUghQobDTibKWf3jsijkLU2_KuC1jyFyamSqfUN2xdiCbcNUfnsk9v8BtGqXO_M_ghCglMOMtdeTWMiTcKnVzzuo9EKyq-JZtl53WSf8In14AQ80ra_4cTFhyiAaFVy3Qbm0KMEYusCmbkglRR-3VZnBAIlhNBxR4TT4tEFy_sB7H3tdPyPKvlVIs0LoFPip1mIAkVbz-yJtm9yGgDpkXalu0VCRw6X-5ntoEh3XX_G_YT_gS2oUuPbI9EjsKJ9P3FSv3cD-bTsIuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مریم، عروس «معصومه ابتکار» در نامه‌اش
به مقامات آمریکایی نوشته که مادرشوهرم
[معصومه ابتکار] فقط مترجم بود!!
در حالی که چنین چیزی واقعیت نداره!
او «سخنگوی گروگانگیران» بود! که برای ۴۴۴ روز دیپلمات‌های آمریکایی رو به گروگان گرفتند
و واضحا تهدیدشون می‌کرد.
میگفت شخصا می‌تونه اسلحه رو بگذره
روی سر یکی از گروگان‌ها و اونو  بکشه.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6565" target="_blank">📅 09:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=uztIhiAvDsGZ5RuSi1TFgPfyvrfbR2wy2SRWLEEpQ9j3MGuCljaJQWFWFr8gEmn8cPAcUkusElNEfOtyh14hqgndGwtDqVAhmr2Ju4upwnKAIqEJWgbppdwKy18fiOgz0EK4J-S5zTTyzQJdpmjlFagJQ5UUCifZ_nInmIOJ5Fx8BqzGQ18Jyeeo3uMbXy5osM9I5JWngNcT6IKPx6upfvL6w2xr7LSeEXtlUkRF4zWoDoSvdSCWrgVZjo9Ym7XgK92FqC4E_9IH4MFed8w4c8rxlI2wUyyTgDYJEoBj4422uAOqJVTEsm_ZRXasp4pqdJPb-kOBJRUG2mDNkTW1xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=uztIhiAvDsGZ5RuSi1TFgPfyvrfbR2wy2SRWLEEpQ9j3MGuCljaJQWFWFr8gEmn8cPAcUkusElNEfOtyh14hqgndGwtDqVAhmr2Ju4upwnKAIqEJWgbppdwKy18fiOgz0EK4J-S5zTTyzQJdpmjlFagJQ5UUCifZ_nInmIOJ5Fx8BqzGQ18Jyeeo3uMbXy5osM9I5JWngNcT6IKPx6upfvL6w2xr7LSeEXtlUkRF4zWoDoSvdSCWrgVZjo9Ym7XgK92FqC4E_9IH4MFed8w4c8rxlI2wUyyTgDYJEoBj4422uAOqJVTEsm_ZRXasp4pqdJPb-kOBJRUG2mDNkTW1xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6564" target="_blank">📅 09:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است!
و این خونه عروس معصومه ابتکار است.
که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،
حالا نامه نوشته به مقامات آمریکایی که من
عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6563" target="_blank">📅 09:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=bB3VinOTFK-n0F35AcqHOy2vxnV4pUgDrLPbpMMYJ3SSovXG0cr_lzHo1qV6rZpNkewo_OiF08l1RWYmnteqEbDjYbsEXgmX51rMGocAybMcA7Ek3JZu9g11OFxy4JE0jw5Bn5PLtf9LGSL7XVMk1R1Lt29TZUSOvpf2gmFFah1nOJoZrL6sVGzD2IESNzFxekiR6KqxvfRek3q1mJ6uQCgS0mt1TBkLjRU2czuy0tumzY4OlcDTxoUy8UVtdBhQUyoKfaumWyBX9fPFHFYcXQn8Bq1q9bYkbf11NXAkqBbLjOEOzvAFtF7QILie5B1R1hwsKzUmj7XCPf40-GTHJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=bB3VinOTFK-n0F35AcqHOy2vxnV4pUgDrLPbpMMYJ3SSovXG0cr_lzHo1qV6rZpNkewo_OiF08l1RWYmnteqEbDjYbsEXgmX51rMGocAybMcA7Ek3JZu9g11OFxy4JE0jw5Bn5PLtf9LGSL7XVMk1R1Lt29TZUSOvpf2gmFFah1nOJoZrL6sVGzD2IESNzFxekiR6KqxvfRek3q1mJ6uQCgS0mt1TBkLjRU2czuy0tumzY4OlcDTxoUy8UVtdBhQUyoKfaumWyBX9fPFHFYcXQn8Bq1q9bYkbf11NXAkqBbLjOEOzvAFtF7QILie5B1R1hwsKzUmj7XCPf40-GTHJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت نمی‌تونیم بفروشیم،
راه دریا بسته شده.
چرا زدید زیر تفاهم‌نامه و حمله کردید به کشتی‌ها؟ که قیمت نفت بره بالا
و به ترامپ فشار بیاد؟</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6562" target="_blank">📅 08:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6561" target="_blank">📅 17:00 · 23 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

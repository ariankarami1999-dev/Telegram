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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 22:31:47</div>
<hr>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJWuY01drZNVG8GPoMrii_P1eCcskbHS8d12ELYOFoG42S6CSBkoFtdx_K1bZFJwkfOx6EWloQU5LbztAkkaTA4eggBx-kiezZYuyhg4jCOpnptmYBXpEFt6dsQeBFqOzjRc4rUGMrSNrlI6v6SZM21lFrboMvkpqMcRL00IOdAMGWnsOuCFgMNxLu5Y1W8IKkD1LWpeTg_IZ6fPopOmq_4GiYh_RShRZqHIABRzkEqYwAaxhuThlsgFndWYYt5u-BH2uuPdu0pezAyBJnGbxi1DSWZwPA2tpSsgl2MznNYQ4ylwot9ZrCCpZ8R7LpEZmBaI83HSEd3qC5mIWIqg8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WP1ardfHXK_oA3UfPU5e43RYvcdW2SyappBciTUhcoBc47unluEIuLP2TzCkrSy-NBym8Gm9888b1akkgEwqEwJKMc8sCWgDsqmUzJ6yDxykiy7tv1OI2J5nnou-2sY3Ocjf5DkMuMhoQkq-r2rMg_mjiP2_B_D4HxqkJddDSv7JjvCJuWv8tB-95dVYKOSCqTla3mTrFkZbhZ6yRy9Em7W6gOM8FTnWCCa3jKJFzuO6SrBD25cw2CULYQ9rdnzTytgtr4r9vUVXBK5m_DCZQ-X7IxTR8YYXIqWWZaiouu9UvK_5i67auYbPBGevQXf9SSty3BTg_ckm2q0mZo0F6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=e1GnF_NBOrd9h4_1ohL5vGK3utWNRukG3tT8Yb9S7olexIR67vy7kJOtKBGNq3FJ0raQa6wAUew59JXZlOZ2BRCpxFgweRtjXqwcH4qqsSXeU9EKoVCL_Zd-a_xcFBh2JoAB9F0NbjcTzvzGf0_1hOtr5Y1yO6XEYsU7U175IVK1eLLt3bq76Xs6kdw7f7BJCyH1MeXtEPdLHu-ZKq9vuPFE4xVR2_E8mBAppMe2ayxEGzLnRjp5qhbtx9uSHlzG84UPVtY7BjfJcBkFw5nhzJShq5bm2wMpISVWr7iB2mXlJaFKWQ_SpU9e-tp8QX8HdExdd5EW_pcv6vToFfxpBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=e1GnF_NBOrd9h4_1ohL5vGK3utWNRukG3tT8Yb9S7olexIR67vy7kJOtKBGNq3FJ0raQa6wAUew59JXZlOZ2BRCpxFgweRtjXqwcH4qqsSXeU9EKoVCL_Zd-a_xcFBh2JoAB9F0NbjcTzvzGf0_1hOtr5Y1yO6XEYsU7U175IVK1eLLt3bq76Xs6kdw7f7BJCyH1MeXtEPdLHu-ZKq9vuPFE4xVR2_E8mBAppMe2ayxEGzLnRjp5qhbtx9uSHlzG84UPVtY7BjfJcBkFw5nhzJShq5bm2wMpISVWr7iB2mXlJaFKWQ_SpU9e-tp8QX8HdExdd5EW_pcv6vToFfxpBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=CXqMRIpIVFNgDfGf1NwIw1FGnXT9c5fSGk-GRS2VyV04dMVRUaBC7FZOw8T6m388glOIARc3ZtuLOWRy78ydwr3Ai8Tly5dG7oITICPoxZQLvOxkCNAcgkhKd6HY0lW0nWNjxvKPVeTOs42-gXb66vMQqwVfS67SSfh8oA1Ad6pbKOMqBbEM2DMACmlrcuKNIEStmv_jChPiUtQtIvNVyGVegSyaGgurqNNRVLO2CDbP7quJ5HF4ND-NhxfKZL8V1Cl8YSVFiAkZx-XjHT8_JLEeVkQhT8QZCkeHtMesUB-AHGswJYE5dlN72WdNalu9kw4zwkdfBr-wR9oSa0-mgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=CXqMRIpIVFNgDfGf1NwIw1FGnXT9c5fSGk-GRS2VyV04dMVRUaBC7FZOw8T6m388glOIARc3ZtuLOWRy78ydwr3Ai8Tly5dG7oITICPoxZQLvOxkCNAcgkhKd6HY0lW0nWNjxvKPVeTOs42-gXb66vMQqwVfS67SSfh8oA1Ad6pbKOMqBbEM2DMACmlrcuKNIEStmv_jChPiUtQtIvNVyGVegSyaGgurqNNRVLO2CDbP7quJ5HF4ND-NhxfKZL8V1Cl8YSVFiAkZx-XjHT8_JLEeVkQhT8QZCkeHtMesUB-AHGswJYE5dlN72WdNalu9kw4zwkdfBr-wR9oSa0-mgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8rChMa6x3iaBk8XLpiEIvS3KxEwDl21U8K8KuBVKm0X2BUALiDVr_d9JH3o1s_8jpSj73pciRBp45eNwPaJCGOcMFEa-nbR__No2YMuzVcpA5OACtfIVuoPXuufjuvgltd-8jH14YOHMRwYrpommsROp_60xHfK2eMjIJsKPlgszvxnAcWH1-f5S52c4D_xL-Tvtt8_FkBxEnzhc5E_otPHUX4l7FKgt0EHwG-Af1vaS7xl4jHmhc5kAOrCu2VXKo2Qsl8AGAnRWBREo9aPGaNie7zHvpOxFHCI2fVYTX0f5ZtGnLaPkyoIGsi5DwkHf9nKsn4tudAyhvN8KobkEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEPavcw8PueoZtosKxvoO9-PjpYyVEfP-2Oksy_Svx1YtV9DokbMRcKwKfqYDAFWR-AvVof65gUEF4ALo_X7rpjm1tETiL6dIHCmqW7F5MmzN9Fct-7EB-UxyOlzK5l1i73ym_9yCzNSI2tO4k4Anca7oqYeIvuJ6HVcQ5AIuhKUFcmp6yPGMPQgjImTlRA7tapNMaYFZfFMWxszmgr2BRWsQfAqCNhpsx-O23c6RUTuB1JDMPSR5GeCea4Dot5dnZt3_2FCjQ9YAaJlMHDixUZ5hLMVdxnQL14DCI1Hj51MqaDrb-ZwP9bFYxnegMPSpi3AI3CzofuY1qwNvrsykg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHi5c9-FHS8-QGeypFRHvH3TEyHYN-AW_TOSouXDoxa4BsiGSIGaJ0Eo-Sr6CUb-JIiGyasuIL4rI7VDXhJBfDzehgdB0xkWRN6EaCc6-7Kz_xEvBGeUFPXszUhFkfSXV9khqXm_5BZqUqUvU6RolqiBvfHclt7wRcQMNOIsVbcUqb5f4CWYgiOmgASqaZdkrwHAyiRWkNG4xKGuVs2EphZ27dIcWbE45aoH3qZtTmweargcasM3peq3TimOdefF8X7XZ5S_ubchVLFbdzvJju4LGI4W6e5g0TVwdxaFU6iPRLUizQPm3HspCANhYYDkrs5F7QLHUlAnkuzR7OrNSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9VnE06oP2lfyHGRfLfXWLl4AzCcwt5wb-7_WZP4K8vFnYwzMEDcN3Z6zrGu87VMTG0mTGGbPIu3zeCJW4_zV-CH6ohS01GBm65l30M-xYvv1vQjED5hYOoQmX8D21FNKHjQUIr7gsL1jGH-zEB5_-Md8CC9WE7Zufa8DKBgIa27d-icmMlLPJCY_faFssHygLk7p1m5jbHgczkWxp2Z5EnNac0_vRNllcnaplIsBDrrTuY23u5bdqjE1SLLuMCMzJmvNrhP4JW7FS_Oou82tdRNi1R2LdXTStHxgynQAD3yQY-wKRVm31vNkyCy0fxTRpF330av3iPagnByuC7Q6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCnNTw-5iauSaCfv_TwxEWpQMO_RhTRSAHeLH2KGFSsRW6BOgaDE6kTDQEVbIuddNfGjSTxounT3P-rzuVJu9D0tlAOzwxJB1rClU6eIUu9wIiu9Zu91bOTcii-g-KICiQ7_V4nsb3_jDyUKD4WTMx5o2YLp6Zxh2TgCdcWPQLvb8XOxKtQCswYVH4Dg-Tdk2U81Mo9Jf9YL8uI7EjS_JdSu4WO559x8IU0UcFG_f8gVqT0NHkBEq3M221QGxioXVVwspAwoUHVutrffEQhXClZROGmHYzDZ0cScztpRjIGY1EU-k5eBnFuYCX3PBB46vEXQRgBfR_hqnlPpco8sQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVbxWBeg6_4AYyAFzRAu661PcQpL3yEX4ugFP6AmVh_MWHfD06-Xj4WpIHFmgR56iG6E82IsF8GXOUDkMvHwIoOcD38BtS40aTSZ8TJRfZcqDAh9vNhCSBbtuLgILwzt7LV3gI4rJF35SJ8IyrzXC94RuMaH3hW6crSDXn-6Xq4QVE3o77ATxFf4iVy1MaSkt5MkNds96JQwSn53ujaOHE0AgbmLApMwmPnExEmOuff1tHM-ivJGEGjcFcAJQNCdvKYeb7w9orieY4iBE93pQlqmZhOa_Ucj1vFOYqIc1VBobqdbS-zoQ8SGqlHeHetwqzeIi63z_n1HELz3Mzrp0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlUAdS89jJqDljgPo7Ns_JxYSG3cvmPo9ts_o5GOM74l1nYRbpfeWI2o2T051iqMZ8TPfh4lK3hW3bjmOzPQBcLYAXCIFkJbm5Ff2Q_73SO9hpjo3rEVGv_Tlz-H67q7O-sO2-yL1f72t0dSUTV_WUOfBXu0o8_w17Cdz1nCsqPchvAgecXzjTrq_eL82qwN6ITTjyJnHmF5Rhd4lBDHA2WO_LokWR7okDule6Ojrf_cl9sHoDhgoSBStOU-KTH3ngsteoelqe5iZmS-ktuJK8dx8yDqVX2lTHza3AlqZcmxKZ-3Xgkep3Xhm0c3dt-cLapnRqvgQ7xJEwcYBYyzKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=Kl-BpG5EpS3he8Bd_2a7ocyNE2MGDiIk9dj-LHPkbeUOv5aV9XgyQxGzurh5-j6M__1mAYzj9KFqbRwesScCCmceqSzAzWgMB-OCR7Qrwj7SusV7G10Dl6aOMQjN-Myjnc5P3rqHcNfQBh5wUG7HQG9VYEkBqL0BQ7EQU6BKXjfb2WiMg57fSY1KZwAdCI6h3pRY38TEtKB3M4U1b9WrPhXEV9zBPXJg9rClUpg_LteWiEhfTXzFyO6dQQesTNik03QPRmzf2HAf0B3pHKb5yZyjOKd1b7H8RFffSVEvdG-orqDgdnisY7B6uyZCNqHCCXtVcPfUR1OQHBsQhBjTJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=Kl-BpG5EpS3he8Bd_2a7ocyNE2MGDiIk9dj-LHPkbeUOv5aV9XgyQxGzurh5-j6M__1mAYzj9KFqbRwesScCCmceqSzAzWgMB-OCR7Qrwj7SusV7G10Dl6aOMQjN-Myjnc5P3rqHcNfQBh5wUG7HQG9VYEkBqL0BQ7EQU6BKXjfb2WiMg57fSY1KZwAdCI6h3pRY38TEtKB3M4U1b9WrPhXEV9zBPXJg9rClUpg_LteWiEhfTXzFyO6dQQesTNik03QPRmzf2HAf0B3pHKb5yZyjOKd1b7H8RFffSVEvdG-orqDgdnisY7B6uyZCNqHCCXtVcPfUR1OQHBsQhBjTJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUTjEqR2Ls95AwNOkPrdtZOUnqLUcLJiX7p8KmDzO5U9cUCzakO_2ApcP8zWyYW2YkG8tDi0CuIaKHhKmejnqTWLuFE-PNzCL76fsyZMq2MxMWUD-bJe4DxsZ4HBscTsJwajh1wijsLCjAlAjsGCA2lE39WXeiS5v_R4poj1OOf56jG_MebFBXgEQUqfExpnnZ4gyP2yqkstilaTcUSldQX0jno9WK4pg8kGTJWMxwDjdnLNEtGLF-GIQU9nMQS8yl91EdIL8uJGboT5xBLn83BYo0jXpHlsQVSsJ_FhvsVrNeSWjgOHb7aEtRVkp9joIYKs02tubhqAuwvDJ7L-GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=luZB8Ly6_2cYnLcCf1ZFg5TfTavIyEKt9Yezno5Ce_cLBO_Pj3nUVrUoR7AeG2i2yu2D1ziQIotq-UuEMCxkWaMWMyXGqPBbdrS9DMxPQ0OLzpJWMNYXth3OXnBn7fyqeXJR4IYzWRIvcOMkcsL9jwrdfGBJo-UEItNWbH7PYClfLXAPfKplZsKG0uGFU7LYsST9lFbTtFHxUd0oPZy5t6Cu-w-luG0GfjwY6dJ2FQKs_lUlrmd9kozjjIIJMzaer4OAYBzcZisqSGNPsGrYdzRgYuFJ-EoIHvREKjsHuUk1yz_JZh7VipxBXuuTPhnF9yi522LCnSpiYbWRiD3qig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=luZB8Ly6_2cYnLcCf1ZFg5TfTavIyEKt9Yezno5Ce_cLBO_Pj3nUVrUoR7AeG2i2yu2D1ziQIotq-UuEMCxkWaMWMyXGqPBbdrS9DMxPQ0OLzpJWMNYXth3OXnBn7fyqeXJR4IYzWRIvcOMkcsL9jwrdfGBJo-UEItNWbH7PYClfLXAPfKplZsKG0uGFU7LYsST9lFbTtFHxUd0oPZy5t6Cu-w-luG0GfjwY6dJ2FQKs_lUlrmd9kozjjIIJMzaer4OAYBzcZisqSGNPsGrYdzRgYuFJ-EoIHvREKjsHuUk1yz_JZh7VipxBXuuTPhnF9yi522LCnSpiYbWRiD3qig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=VX4j5XjU2w-yEvLtgJ0Z8EG92Yc4G4xnl22o31EPYX_F1t0ciA362hqTbZz3bT6Uj1fL9RHSHxagegyHZKg68V1BbBWrYZs_Irw5QXueeSX-2GknSscvb7h36h8eZ7TL_rjurPMK-qK3AfPYe36mBuyRDzSm8gWhLfpFuzkxoORMmEZNWzW3GzXbPV6EQ3IdXITGEIm4Aa7SLj_VpGJqWxkDXlMhjCkgjeadACuklq41OUoXc6SD_KpwFCMWc2sgt6ynlWubokm-ygzigj1w2ILxOA8q7uNAJM7ConhOCgSDhgUCV6eXtLm7f5KOcRu_VJunduZYiSND2uBnbrv_6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=VX4j5XjU2w-yEvLtgJ0Z8EG92Yc4G4xnl22o31EPYX_F1t0ciA362hqTbZz3bT6Uj1fL9RHSHxagegyHZKg68V1BbBWrYZs_Irw5QXueeSX-2GknSscvb7h36h8eZ7TL_rjurPMK-qK3AfPYe36mBuyRDzSm8gWhLfpFuzkxoORMmEZNWzW3GzXbPV6EQ3IdXITGEIm4Aa7SLj_VpGJqWxkDXlMhjCkgjeadACuklq41OUoXc6SD_KpwFCMWc2sgt6ynlWubokm-ygzigj1w2ILxOA8q7uNAJM7ConhOCgSDhgUCV6eXtLm7f5KOcRu_VJunduZYiSND2uBnbrv_6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oh-RmrLQe-dgr-ZLp4myk9x3HSUe0ImYvh72kwhkqkWzRszbSXLDP9oPKaDO5ckJaOEtYyc13t1njv_o2J5NA31fS9Vn1u0SSgMBNzp-FcxXG7bJ29_nBQ6FTchi2sOAUnJViUH00YLazf6yO31rBmGQr1dZ8qrnZjxgds9Pf2zKdOKCPw1IrJsNTQBFtTUTSfrb0lZ1ASX6Bcxqri8LzXHE_OWAMb0DRu3GBjGtzsZyUwxP9Xny_Dea3VMkh4qTKIVpyn2EfA9qyCmQnjR-FG0Xfr75DRzzFOJFmIHg_d2tf8qtQ8e1_sFmPSbTJqd7mVjbcUfE-crgjMN9OJuQXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRTYOSncKBZjRqsb2tYUMlx4SLb5M9uzHGSEO3non5nJYjY3OlQDM28lafnqTxr7KVLPrraAZHlNwjCmVkl6P1gfAQEwx1ZkgevqUMgonZpPGaO0AOsKhO8qsfGiUQbD_sUmvaRByijn0lxhGTB8m7BeceppO4kbdrTX2_ienf5rF9HdzMBzOxWBQwcq3qaFrZBTgi5oerXw1WfwIc82dJ7sBctN0OHlzjBIyDDSWLUgIVyprTY7Bpa_QDCq6Kaly0tEYRV_7De4n6Ho-LvFHJebyFjiwddLyQTlL-AupE9YFwx6WBnS3y63KXnzKC5MvYWuBUBzpw88L-lTRBmkhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=cYi7bL-4BoptR-6HC_TjAF-rB6tk5U9MTinSou0sOVLRpQbooOxxMjLLvHvCmMoPmO4m10RnLyMk4yZs3v6Ht6I90l4CarXh_Xagx1fb4tsJlOjqIsm8TM1VGkStvLJqG2jeSqSz1Q-UJfo0N4lZhTJvh5RUvZ7xziuznvbikWWwqETmzH_EpHu5HNUU71pOFFehcAge47hFoV8JDb1CHHxkNuJ8Kkh_UYBYv70-WWVM6we8wgAEnSSLjBW91WUlBiNdEvVQQhzbGokT0mcaQOGMBnEdU20yFbuJsLcRDq9FVXLov9aBmddWu7t7ycew74TJxD3bGM_I5CQ7T1CFJbpSxzbE5EF9zZuxq9cDcKLzvHa38QuTMjsUP4E_R0D4v7cvF8S1eDR8NG7rMhKBOevApJnAMiKqfj0EwrCAACJmpJwM33gjJHUZ1ahEJ5fjvSn3gEJKZDNrh4gotsW5twhKkhNSPARuhwmKgtyMGw-s9BEuZmDEPuRh15uHVmBZH2LIkhv9PmF18HuuckQjFRyq6VjT2BRXkLncSZXfKkrxH4u8zSgYKFhZ-2Kdlj_3AHCwVUTIy8rDkdRFajQ-iecvho5OqSWjc70Y_ExSf6Sv6_4hRHUHBxDecrcH9gR0ys5rm8TP7D809xcbCrqchfPIyCqYw58FsyXWUoo_mxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=cYi7bL-4BoptR-6HC_TjAF-rB6tk5U9MTinSou0sOVLRpQbooOxxMjLLvHvCmMoPmO4m10RnLyMk4yZs3v6Ht6I90l4CarXh_Xagx1fb4tsJlOjqIsm8TM1VGkStvLJqG2jeSqSz1Q-UJfo0N4lZhTJvh5RUvZ7xziuznvbikWWwqETmzH_EpHu5HNUU71pOFFehcAge47hFoV8JDb1CHHxkNuJ8Kkh_UYBYv70-WWVM6we8wgAEnSSLjBW91WUlBiNdEvVQQhzbGokT0mcaQOGMBnEdU20yFbuJsLcRDq9FVXLov9aBmddWu7t7ycew74TJxD3bGM_I5CQ7T1CFJbpSxzbE5EF9zZuxq9cDcKLzvHa38QuTMjsUP4E_R0D4v7cvF8S1eDR8NG7rMhKBOevApJnAMiKqfj0EwrCAACJmpJwM33gjJHUZ1ahEJ5fjvSn3gEJKZDNrh4gotsW5twhKkhNSPARuhwmKgtyMGw-s9BEuZmDEPuRh15uHVmBZH2LIkhv9PmF18HuuckQjFRyq6VjT2BRXkLncSZXfKkrxH4u8zSgYKFhZ-2Kdlj_3AHCwVUTIy8rDkdRFajQ-iecvho5OqSWjc70Y_ExSf6Sv6_4hRHUHBxDecrcH9gR0ys5rm8TP7D809xcbCrqchfPIyCqYw58FsyXWUoo_mxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUT61ekjBFHPF6KGY7ZFkKBmlGPclokpa0DiSOdnJpcSPtTXeifHH5iktMYHyKu8mdH0-4wjxF9wD-dVwmHc422AqcGgDWlvIGUVIvAUO5e_sUPhnpEUOpBKvoO0AQmdmvvSEDrJzFpgQuA37RKIRUK9o-_8STupJB_0rePV4qSDUP5CpLA7yyEqSMgyXVovGcVM0TPdjN-41YlNslVsmqM2KiqyBsKdIqqbNNTmhonuJgUP1mnkqpqAZyW2wI8nPoOUayzve_iCgxne2xKisWe8j3NarwEtC8VzhH-xbYEWp8GEH2Cgn-VnkvEkIVAkGzYOV-Ku-C_sHgxwWZok1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=sB2rOMtiTla6QJTiHMUScPvNBUcZ-0M4bQvAULuHNjI3gV24nqUSX_8Wm5g9lgqkTeveyZDZXPRHiN3xU-Qa1oVNYIC4XOfdsgb1E12p_aoPyi_8OsjxrhpDzqH-k06ysf6cFaomdK5rX1tw8GDmqLNUbWbGlKbMGDj39m1MKBYFa1ZyXvUhKi8E5uj8DD-6Ku3uo2zUZX1dZxTONzKZxS0qQz3h3Pyo-xXSDiJI0AFSVPfYoXlLTQriqRf5PCIdwpEqoIUaXGaofUM3auRSfiHdrK1QeHtpwVd6VTO0MmvQTZ3s0T3CBzObzTw_qZjzLWSAj3uD5SBo6puCxu3xen-5dBbKDSqTdYjPcAm1VGMfVDgrYBioK4KQb0EsTE6DOnoKqVlcaLzm3AsvDFJef6HPSb_S1DbD2lHPeN0g7e1oQGpDEeeLPflwgT-hAMpAQxysw1tmdkMDn54kBFeYs5gmQLdawnj8nWAKwB4TrHrxAj25-PyCov_JkKnt2yUXoOu4CaRwzyOFbmcv20P3zRw4O4QqpODNzgaVJSInzxZwp84ZVG_LkWDU-Tl8Yx2mYL7VQpoQY7gdIiEY4caZzr4OluVKr8e3Q9uA7oC_2iudj_ER-9cQqIOq1Bs30FPFkngt_qr1pS_bbG-JkXeqEvr9mNadn_RyLQMQt1a0wOE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=sB2rOMtiTla6QJTiHMUScPvNBUcZ-0M4bQvAULuHNjI3gV24nqUSX_8Wm5g9lgqkTeveyZDZXPRHiN3xU-Qa1oVNYIC4XOfdsgb1E12p_aoPyi_8OsjxrhpDzqH-k06ysf6cFaomdK5rX1tw8GDmqLNUbWbGlKbMGDj39m1MKBYFa1ZyXvUhKi8E5uj8DD-6Ku3uo2zUZX1dZxTONzKZxS0qQz3h3Pyo-xXSDiJI0AFSVPfYoXlLTQriqRf5PCIdwpEqoIUaXGaofUM3auRSfiHdrK1QeHtpwVd6VTO0MmvQTZ3s0T3CBzObzTw_qZjzLWSAj3uD5SBo6puCxu3xen-5dBbKDSqTdYjPcAm1VGMfVDgrYBioK4KQb0EsTE6DOnoKqVlcaLzm3AsvDFJef6HPSb_S1DbD2lHPeN0g7e1oQGpDEeeLPflwgT-hAMpAQxysw1tmdkMDn54kBFeYs5gmQLdawnj8nWAKwB4TrHrxAj25-PyCov_JkKnt2yUXoOu4CaRwzyOFbmcv20P3zRw4O4QqpODNzgaVJSInzxZwp84ZVG_LkWDU-Tl8Yx2mYL7VQpoQY7gdIiEY4caZzr4OluVKr8e3Q9uA7oC_2iudj_ER-9cQqIOq1Bs30FPFkngt_qr1pS_bbG-JkXeqEvr9mNadn_RyLQMQt1a0wOE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hsm0QteW-0pTZSD_TxFO3FXNsvQz5u8uFzl3vj1YlbJ2c6SjncLNJcRUX1ZwiKErnzUL1yXyEFeyOUHECfBO3SHBmv8zbdLTuZ3Oh73fuogl0A_0M1BiYtZe4IA8w2alEMQ1SRIXh4cH8FiRJsHqQwRoLCErY--0eel2WNfsHWrBhHLYc5zEfbhbiUWpbRDPA97GUcFP9caOFpGmNP9RFW60QqMfMjGU5DjE6fQuwzGz9CXTmoSifzDR7Ds7wOZQTYO80vBPBqsieZ9fHm3MJuGvxxvm_WvPGDi0zjZOtoKnxs5h83epj1t_gBESWFg-1XFq3gXcOXF-upNFHQJC1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgKGlnJdwfq_HU9NArXV9186Kggfy9OnHP99j7Ii7DUcdSv8n9gszPlEF0TWku2RcdInCWTeJiyEeEqL5kPA0ngPiHCHrPbLx3HsDZKy024OmlkK3fVWOZq0QIlDHDBvpwqjwTJNskUU6ASxFC9tO7UrCAzPAqnJYAbrIwBxAG7AsvJe1lwVl-elQCYxXM60ArzLwUbN0nNp-KKOAkPIP5ddaX2oyM0qDzdj7TKJtvD9sXxrJZ0lqEfKDrXtlTZ2VKwukmZeELbtcoAzlON-k7QmK8xqNwlJZ2lTkdbqi9k5mtNtYSc-zV-ElRHJRH87uYOvH_DTGInVkJI6CM_6gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIlQEafhrNiUh-ZY6ujQ3wuMnAvCdg_i4BeZAhsxZnQ_N6ZfnT7JvezEnia0gZBp4VrrQzh8IytZrDt9DG4senL15RjH3haU04kwXkP4EDJofqY-lAyhQGu7s_4A-v4xI8wrJju7XeSQcvVxt5SFY6zd0K-Reo8DqarkYy7xGCzqY7lE71KpQGxRBpPxgegR1AdctaeSmTla1IG9FbLzv1FtpgOl9LVWPRYfsjJ5oQzyDi8GG1h6ixEEcWWsYf969E1ptnLBLOxg8xpsOV2U5d7f3X6Kel3BMQFAquxoSdg4JT6TwiYeULhMQRX_hPp2TQ5cNuvuvT22Lm8FRzAW_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xz41SultiSCpkCC40v7LUjGBH3UJOoi2bmudfhfKiK_hkG8U6xZLdUaJ_xJ32bboNTMq8LT7cnMF5Jiqqs71xsARn9TG7XcbPR-X3CDhqf7nOMosxI0luHBHUql9D_4g27DVT0C0TIGmwu2WjxrKCKImbpYq8QRtj1yi6htrVDLlM9RwhcxgKxTOJxUTpNv06RHl8H7rEdsfBDrbP9wzensn7RkPEGZUZ6EyuMR2n7iqQo-SFRsFoBFVNnGno0yfN10q5-kC8RxoFWmnXuL_LusbxLQ2YyXGb8tdtOPftGALmbv7O5KLwa1FIyWPP0JvwzrN66Z8Xo-3_T2dF1SJEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDFIp5jv2gwkE1WyOtzbTWk-JIJyVWu9tnMm5L5vpBQ9N5rLmudxYwGY-ROHo7qnOTNDgYrmXR-fdP6xdn9frPItPRgy0X9aqfj4HYie46HhrjTVY70kFYOSOBBlz3AxR0ibnFSrNKw67DVWjgATdSbxg2hyvXR75eeCounXpAn8uqWe6MfP6ObLNtZOvucERlo12ASmrm0J7ZiwDd7dm1WhiHpmysiPqb9MKeyUnGbaw3M-WXffEwg76_yvVAHRCbSC05fohMgz-XG6XUklDil530WGrKqHPM2IYcxTF7iaMmPmF3lN_x2UXFxGzHQ0GdUgVVHnhtm9tJWtENAhDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBuYaWh0wqtI7O8YmCTHD3HhF_imaVa4kSeEEBSFya6yIbALXMBlXQt-GHZkINLyydRkQbwbrg-t8Ws_Xbm_dtdVewIZelqvQmfr480-01xW1TCz3RcFLIfpz6Z0XX2K2c9jaDXaQlQm2ChxhXJgXfkdg1nHR_fUtjHyboOaj2MKosK5sFf0pLBEZgpp9ld0jI57-QX8FciHE6_TuNqLRkkClntGw945DLjP-lkH1sF4Ckjx0CshGT8bjYYveDwtTzJXYE5dTMrWyAT4NVTJS_m29dlpUs-6Exrk1wIOIGAqbJ4j1Obtnxn4Te-oi4V0G7FjzrNvljJB4l6lh3hjCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvx3AZE5NCKfn8sPsbIFT47EXGesp_bo0roDP8EOIQmNr3bhe_mKbKYqwHfO6bJG-wzld6J_pFex_qtQFO8QhzMXL-TMp25ij_VykZY1WDBwHCXFBKR8sxRcbDrOZAEvdj55DZDU86f7ttpSesBtOXwhZENDAUXtxOtWSxs7zX3AGsn-Bf9gJYzQxJ-8QWLXECj-uFQkeI7-td3baxE1QlFlLtW4NEF4l_X6v5uBI3HsYTl4MhY73skeeYegCTOnyxLS6ZP6P0znWLO_DIizmTOFObE9xPRmgsu4MZ-P2WhANdKNfl76G8P5c9SKosMd-M0UHX9RJkBuRY1sfbWBUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckATFbA4FlPH4XrV-yKXi0D9JjJXcZvCR777sBwAbMn3pakmW39tgAx_Cde6RgwJK5JsH5bnIdGu7TtxJ7n5gBo5yBbgxy_S4Ei-Up97mkG2O4rg8ffcgPAl-P5aX4R68XinPjtXEj4vBiMCy3IL3LXX8dZf1bqxxwifmqyxwNffQANVlLpdL_dzyxrn1maoMaEYisa1aonCbvxCXocDXkoRNKeyGoVkg0bJ6PTXLFeKyxsUN9sG2_auLUDq6axXC8CSfVo_xKj1VrATy5R76gm-IoTjREOW_voc5TAw3Az5iR3fNybi2775URXPMLsWJdLXI02irf_TaRMwotjCaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i--z5wCnrOxTKOs-otf1h3DHaflX6qAAdLshCVrbQWClZnA6y5w8wvy2vg0HTqav0EX23ONk1NXUrxNUh94lMirWYUtuw_d2VVQJCCMd5LdG4v45-e3Y-g7uyvO7jeh140O0REbM-D-TYQPi_qbxn3_kV1yccCXq15vdD_IcyNiR-f5LH6U_-iETO8DXw2zMe4QZ_nhiVE8CCIMJd5TcX08g1X2iLRq34VqSoB0QF82CBUNCto1EVoqvHJKrX5qMUcwpJ_xgJYadmu-Zc2Yikeg4uILPR4SFEmoxDgJDGWe3DIZua-dmCD3t3uWEpnAfZVmG0oXet11BvjecLCRHMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWkwYrWTAG9TtMFqWAQ3RPchteiTd1lYGEupjoh2mFnLx6x_WVpwEu9gcuIAGzJCk8x7Q7diajS2ltJdrTiydZlLbMlIKlUECQKT70bsB_tUj08AWCq_yk76Fyz-Z9lWr9MHfzSoWmy9Mc4frlqFxj6wZlcGSUpUjKqPzLwJuo-6j9avvclFrGdGdz2WMMJUDQhD6NCOTGu4pfOBu4rbKmZnQNc3LPfFAoUktgZrBf6FHp41LBbyWGPS4CwDNwWiYgLDRJn8XIb2ZNDv0xzxHzqd3rfJwvmym-_SVvYDRIA64VJ3zyD_RcQfpLYgRHEZmVsDxrriR_97kYS5XxCV2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQ4RYarLFquawnPW7qAcCeNTq8aTm3ADLb5lpaoCCDe5keQUngimS6kooCVm0ct08hO1ob6_1uZDPR_ORXlhpeqm2Uys-mPe7Oa-hqFStDpj67SPDBYdsJBC8N2_MdiAN2XPHgOdY7MA4wPOKKqwFHQPQTd2r7y81LhUpPQ2_KuGEMZz46ic7R6rKeJErkFO32SGNr4vcNZn1eSQmt3HCd876rntwdNgaJE4vVUInhTqbFa2KMx-bLg3KQEjydd2-RIVzOuS7ADLDGtcUj2akN5F4Td2QERBDlnYcuC51qvlVAMd-nvQlwQQOx_lifA5yT3-tUw8nK-MeOn-rMYeIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jnlfz3am4LFug2xMs_sxNZAw541t8BD-5Xrn7Y10LzH3DRsr1YFux9mHP7ujmCXVEb1F0qnVcAuBULBpi7hRJVFBZrcAqs3Iq9vpzNXODrpMerlV1YTwekMmziPntTw8UWver1csfbJvxcAPAqAWa-ETpJRtSvieW_3UuQNHyYbx81ab8jE6bUA4R56Z9vEBzoXzSM40c4mPOMA4fesri2uclsibIW4wd3sKaXUpdZhp01XA4IrOgGdXj8AEuZ8lzKXlkDQzOIcej29TZA6vlDhM6jJ2cambWw4aWa37eE5tOJ523nq5ktzZ3GTfIwYoBItpjf7z94F6UR6f-XBWgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvaTuLeG1HwH1YX7dj8diVUBtdS0ctEy5hux5eBaLrWS26kit_IxP8EzBOxQEJnuefcmQ9EFWqZyUMou_bjpSxM4l4A_BPZY4TfuEF2IIgorbYaK80fNaEjk5GJ9XT7oIomCo7ZhNeaUqKmA8MapJYiBEllE2oRHVHVGhxbb9C6YMoQzAtui5b9AmUeCXGgDciJ7ZLafjRB5x5xEpxxhcmEs872J4TszxedTZQN6R3AugmDy0QlfcByw19z96XVihjKweiIrrQ46eID165nWD7aOV5ikI86gx4iuUyte6jgf4V0c9U0IE91pJlpzffczRVWKLt3wVdCPeLL_QXHcog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qkr5C4aRGlmBI_vX8stGjWqeZSqpePsQnAqLhc0QouAotF8o7dvqwLh2Ekn7EJwxY8awnlw0WbL5R2URSiUs0usrezH-4e9znOgs6UyrtlFtTPSM-_1gphlKD_Fit7FYJ-ly4d3ObGuFygA-3Chjdgc9yYuc3TPV8muMImu2MpNblw8QPVWyOsRhsIoCBoNUzCNRWlAYzqFn1zKcgTFJ3pX4oFgcFv1ddFx-t5nadTMYfGf5Ht5QMwv4ztRgJCCwlOfCdYc189f98Vxqp9YWapZd8XZV5ohmAPYsaz8m-JEs71l-nw62tyuhmlXyNLDZ8DHm_kXM-cmVAB-etq-0SQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6616" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdW7Jx5F92uVL8Xgr55pkj7F0d_EeRjdEgTH_pB2v8OI6GN9ZOleKHyspKER8G3y3-EOZFAG4TFZOk518ozr4jk8_UcrpSaNYKKrDiCTrcE1yUGmYvW1qv91SQLAa9AzNKGTPB85sGzVR3EUDAQzFo5oYx8XkmcfgLM8FfLnDNIZicp96nKpBuPf-M5RTBiFPKGiurWQdIykDAxVmr1XxNuxyi-viIzl7ok6AEXbLGnurgaPaoAI4ee1c3WgGvIk6vXUlpBm6nj2BMHEvDVaP1QPBASy3XV78sH4gvPjROMKf9rP8zmF1b9tJSLepGFDgNKcd8_5f56zKPuZEtRuCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkYEZxSEZgljv-u_oScnYuqGwBIrP0dgsed52J4VRDULk11SsLQy8JR2vLFMK-vHklKGb9GaSKrKJGgf5-0jZZhTDnsk435d1y-U1tO3oD9DeVSGt2Ga1flOP-SRsH4gYAJ8pUoY4kv0Ast7A0kCKeVyQfrO9rLTxkSzhVRAZ4FwBe1dLX1vtcPAFpA6rs0vH7JOOodBB4_ck4EpV_CJUlsvbc7bzn1x6WwYW4evrRWbENs4hI83_mZO_eLvpa7Jed173R-haQMDCBr_1XZO6BaVzsR1N1mKrtHod7BprOYdxSH9wirRPX2aiieulBipb3gxLV2V3POHq_QUw8oS9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jE19duK7j4_hcGYTm1Gk7MTEwDcF3nzNMYBjf9xqb1HayVUq2JQU423ctO9Os5RMQgo26lbe2W19556XyzGn-tywFMob8X6WRmGI0-DrJbMOf_tB1Z2ep_sPBhvDlZJIJjXjYrfMyODVYBbefbQjB3kkDmqKgUgqostN4RzDBtD1yF6b0L512qGcpKZllxkIGxfFMNOaCFuIlBt6ziVGCN4ITzFmF_W111WNtPq7_ZaByjuh9kuEz0GbM_W6cP-c0E2z33NkIgqN8erB5VjS4zjMMr2VprW5H7lqGBOyuhpHxaX7iG9pladL2R10PKFq_8TyhdAwGmCferK2TlMwDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KCT6V34EDDqrOtiYReYp1at276DPNUOMuLa05qYEudqbU9rCZgvP86V7J1TSH0AIZICX74q0lihVpS4FPAfgfHfk1yEqjQ44xyddocG_UQaKKpZxUymrone_RaLp8fudzUVzKXLSGCFnR75N37tWwNg_T3lmItfggQHvsL225Rpo5JmiiTvgBTfeChAlod2cCUCxQZVHJrajuARVZ38W2ivVoLnNloJQA926Vt_gGbkKYmoQky9CXNYUMdBF3zO0urpB_pwWzqCaSC7RAYqx2wXHf5AyS3WAJ_FRjHZoOCv45XRv87pKRezdQ5eOEzprwxWKseQhj6D2glxasZgfVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qi2WMn56WVUBuuQluQ3xoD3Ev02fBbl1UMoaiCC2_WYwLTOW2NgIk1xWasMuV_W_wfhZ-kkSHuAFcc09GwnJPI0qOOdobeB0v_jGBIIUuusIZ26I3E76ipxTLYRprTMd9mXFuh_hAvt8d4A7mA7WqA4yfeSwlsYu6fLCeWX8bWMR6KxE2yl_LVN6YZyEDwVZo9np7geP8IBInwB73-seIEnqNwFwfr2P_sEa8DifGxf1vCALuOCihqZ5r0lOkLk8-Gvw7N27vDz4OZxRZni9Onf3qbjwJDY_yXiaIG5eJggUHhygrv2PAsP-yEsai4651b_TXRSYXHZNY6rsYJRMeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_IXFvtU-rx_h_kJRTPpK_xmVpSyKpVJ-mrG6l858-LvBynYYIrFpKVHk8oVZUzMBltt-QOvTzCOdRQMQlhd4_VMio907q2uwEN8_B8ROjmLIL0E32rKaXDcuiV2lA5vyuMJqxwTV6zAWqppDTMv1s9L340biRNtyP-WGjXYPeOKdNJleERAGd0-3KQWDW7LDGxEyqwlfBG_t5mTfzfa9Y4ydBr4yaT63Q73fI3QT8mouT6mIwxkJadCLLLBFMpIboLtMCaAYdabg5JaMi2aPw5mPVZ77r7_MEY_faPrhXSXx3wX2-i4VZXyPwsgTPLE4EDPEGHkVKPubeMQvOM6ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BosJSsj9xGFVVyjhwWCktNrShcYEepSwhkjx7TcaXd5jGvpQ46BrDTIKPW8T7frO50uU0b3WISKY3pF03ukAd7qjPEeUaJTEmGqoGl41xHNwaLTLFFGx75P8KsnHpZFSUgSzUdy09kT2ePBqjHYh1ATGTTKMkpWa5PF6diRs0cY0GApYpAccdVMO7iCXkQs2gvjZkoENSatOWvSaNtvlD52nzgCbfyaf0KFhfw0AbkU2kM1oQW-OtvNdYYiwJQB6d7ipZst4BQgIw9w7juZJ_IZuMiof1Hvwss8em7GxpMpc6US_MTooHstNewKmi8FRP4ssh9H-hAP5HxmGh2M9iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ni3AXhw6g-HCnnUZd_bCbZFSV1owX7SAyM-TU2ytX7i8eKBDxNxyG093A1GU1u3WCoLkO8Apz0G6UYdYvH8d3l34qiV4xoCjrty8twxeYMjNNIgAPi0e52OMEjZs6N8Z6eKZQ4GxcimGwwZmjOO_iALrpMiJTx8z6MikMSeBU87y-r_Yo3zqGzKZ84zhj6qS_JUshEblELHCMB5vvtFB_Xeg1HZ_NL1-Sfq2_NvRPuAmMfaKPtWMWYtdHM6vguPZtKvCUwh3x-eqQUJ1bSLBVTb6XE7bt0UYdceMe2PwpRpjdaFc7apjrGAkhCUuIoB6A5nvuiSeN1kfvVU5vhJe1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daoUvEX7jD4UVkuvwx9fva-b7SzGU-DifgFuP3SzRxLpoqZvaCtoIKwbLce1youa9T5iM_3G36cQJbaBXYaR_DdqGBKtp9PaOK-K4BfVsRVVrgvaKeSrRuOv6Io53lj_cijyL9Dwjvhm45rCE3Rh6bFjMzxtyjgxPwma--YR1R2Ib1oin1XC2ySPn2zDwN6W_n9TxV9KQX70iv73E_dgbvCuQT4xHMX7_zDyei30Gc3RgMv73sFLFeFUvSb8wwRny8LLOrzp5pkCrOaiez_B3y2ZeLW4X3lKDX0BdgrxT6eLtgWNIgutlHBteVKuEbXfFgXTUZtiYUGh8m746jIrvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iULBcU-uY1KbLXskgbki2P4HlpHgHca-iGBiKR8CJvZBGNDnr105PPJabOW92fp20apX84qqghybL3LBewybRBZAXi7_Cuw4SBxwiBpod8D55ddp7wuBE9nNbEUtD2t9Oqtsl3RAM8r0REyLhiEs2TeOgzR23kfcWX1Yn-b8QWpu_wETBiLorPOBmln1pcG_WctbvZTSdw3-sumNEkwIWNfBa3BKWKTdvLksCN87mziQMh0DROEWEcEi85_eQcxdqUVsHpLhNBLl1ssxPXZ7Ru6NZGx5v57NWqtIoejNgQXzxzppwrrGsWZVcSibPhpqSdwDqZMYTWTFlTf4elLNnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uH_t-yDEBlZjvzxCbCPqVVb-zxXXzeV2jjsqZfRTna1qVfLajaxJimgVApnzjwI34bCsTybGGQkvVD5egrCQBEvYm6phv0yX21Jxwi-7xwovyW9UhrwXwi0vTEwilC0ZUUlBOMa1WKUSdRJRjSyOekbDTOgj-sDE2G8ewzKXeL7Nyr4FAT1oxfJGZENkjKzdaPfseVUc6WZyAGnxeAr-kHdpcFfCwsA-xqrXCU8p-Jk7P82KOHsItgItmfrOvkcb4e2wRLRqloyLGAN7Klz4AkNyavProi1Hyy9_VgrQs8qs_8scZYCLpmTAQ0gXhgPWjNDKxanczd8cw7UwsuVQaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkCp8yvEguBkUZ2FlAvCEsB6ceFOvm0yTWIsTk4XENF3dh8bOa7zpt4_loULuF2sgjQamou2UBZO-N_qS3goEWo7Ql11tCmOqbhxfHL1BSB_mWSgCkQGLvQXUQw0uvnbZvySNfmfXiHvQHJIHW-XO9NE2eL5LTR5Q-VptlMoY1-ffWgX6U5Ryyetw8mfU8ZLmIFpWDAGhOsmBZDUHW7ihvtB282GSwF4bvv_QTMhHWcqlHiZyMKKGkDYc9Xfj_268qrrxEB_0jv9gBToQqQPD1pJpOpQHgdjVMEkjo9xgvcgIzwBllDY7jQCLiRDvjUOmfL0s2uZbQxpmfLe194LGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUqTpt2Ouhzusisiug8VaYa78QO0ULIZaKKlYZYwgkiH18NHlZr3vEiqi1p1zviy_2w7O2FRoB9FaGk153eYrbzkyqgkZPScVUPmIdzOaW3MES1rGaxfDStjDEsgtfm1N3qHhIXDb99nSGc5b2waJeuKmFWhkf1jJXRxucp1A27yBz24DeuBTjtoxRYomxKvSp9y8qCDLR9Mei_2d50NcoCiYXI8qV2CMcrMdPueTVGGFUWD9mb9qqiN4LQbw8Y0pbXjCm9LiqR8dQgibEsZCMGAZPrdLvetCuJ58o4bxWdcqH8nBTirhAFSaduhorMm3_nlZExMFcFtqNTrT1V7GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukaiDlF7y39vU3xyJLn9fsgw5ulOD7da04khKxzu_v0ABFFv8-8fFQ45cI7pCUpPmSHBvYECqJE5PC70AOkBzDHRnx_-N37Jjc1YdVBd9NhUKv-tuzICCwm_WNoAT--7PfbBhOeh41DDLDiVEzmXqqMaQ9m2eWXA0mk4AGEAH1sfMNm6xrSL929Ak0aurt8jFiWYT1NQxcjDKCq3VYXKdLTmFPooDO8peN9c23iY8x_R4piOWpcR-4mlucjbCCFriHwQPzn0pNWV02ffEXeAi60gjNJghI7_CyaZGgHdj3ijFtHLbbmc9jIYoUyPURNYqf61JrBq5Cy47j9gm6Zsqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USRhIgChVyURyn5mcNVZ3cXjbOVRlxXQ8ehVqkftDooo4OlKDlqmpkaG2MR_c2-_JPCF10zOs8dO4C6Jv_xQaVJi0JOKgIUlWUJQ5pQVft3kv4Y-xy9CrcE-UQQYm9ZK9ChAn_BWsegpHFI9KYEBTmz4wrkBnbIi7mfpwLWeKtIsWfi5mtrYC169PIrxRPFpqLk7mPUaCvZgf2yVj1G1HxQXGZkOgThnda3jGYhH2t1-ESVrZVGjOfP0LEjm5K0KlGl4Eitq72eR5nL6gmEUxVBo4xfgCRrllFRq5wuVgsoyRiRxwhITToTZ6U5J7BHmNmnq2tKkiXOwv5mgdjIW5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPmpVVFeSEXYCLmlwDUEKP-Ndw6Un4GHr1N8sxNFGvpq1XF94QXmh5tN1qxYqqZPw6VxjZM6zGO-QoBkmBmQfcOhBkgP16wDjU8YwatneUpxdgZD5LTEQxYx9g-KW6wbbAaSvDIQD7RRxdcA9Z0oLKadEl9smqVNCxO10ZVCPBt6qs2u16T7nWFwrBlzDClLZNcYarAkYkELQ7RcfHOU2sHN5HHJc20JFyDVIxSvH6c9M7yPHEo2GhnRQnzrAbSKx1iJcq2XZtLDzqzcBQ_W0nVvqhXVRrbKs5Xp_ADxw0DC85wYetiCCvw_doomt6h3rahSRzSwFrozjtObpxaAIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlZ79Y_YCVthXC9wWCnfXNsbNP4Amn-5PUlpARDrN1qCr2-S_gyR4YTog36y_lDbzsKPMOu247GgtKWrRrXatH7FcvwwNMGg3UJXBJFAgbZawXk9umXZvINRik1hd2SoxYO1u5-e2w1d24fGFXZEnmr-mXUCZ0mZx7QQZBBsF9weXeBuDPoR6gd2Zo1JdPZW86bM8u1BMjQmh5yc4PXfx5Um2tWyoAsLSk7zp0qjmaDYIxU132hudHGmEuHWIAEiw6TfXLLHcHztFnChznmQwvyTXqCDpGJNsuGGmtw-MMORbeORi9VamO7lLME3WXMiFKMiIfUe8J3YA3V0WhoOBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCifRzyRpIAF1j1TRh3C2Y7IoJm400tVZC06OTbZOk4o8f3VxYldAgB70-1fkxMxphjXuOEVrLaVt6VReT7lVD3zU5HfM57JsIztuXRtWbwmbXotzpdBx-AC-2FYVlteDGS3yn9bBgMU3mIn1mkBDf9o0JaikQBZMLHc71AvZ4o41iK1x1VrnNpXxe7FpVgbJ8G2BQqMgYIKxXwz-LCzbMq747aFhhrXd3cWH8OEVfBqQzeJXF91e7aPk3J_66VaJD7c2hvITmpSz-cAoyvFPuj0fxFPGCXLiCA_k6gzV2gUoyqm3gpipbjgb3FlW4ZRq4a8HfeMOYUWSAZdUV6A4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9W6kNa7LEuzbozhAsE6dL7dc_Kni6fwvtgOMHtkVCSdmEAlDzapZpzUtkFSRjjP1IkX9GIXvAdg0YsEW7RbfUDsWkt2th9uJRA_3osudPYVQVGpu6fJQTMib-gAUEtx3IJ9evfKib9p6Ck0X3fRIaYbe_3JpcDW2akwbm0VuRNOMXC7p22o3Y_8QiEO-h7_yB1JUIhg1YrsAh1VzMvUNEiTjnrMkM1RUNLPU42clnIzs2DrPQKOy4INheA_vzdfzbBJUBB151OJysphX74cAIxO7oBQ6kSQ0xcIzsfqTyIs0QFg1eNJPuD0EabNmYhA1fBeBtxvQcrQY3DMghdYyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rg6STywdiytgsMShr-8IxaUfB98j67K-sA0wXed64y5-fTaneUVSSBhjIZaqhcy8z6_mvd52bmpV9MjDbyFSz6Kv5xKRueLmWgYMqo5OWnf8BvlsxjJP2fh8PVHpPf-cdSoWJNhsEOmLfxMtrHJARwjGUdk1YIQyL5JwJ7_lW-XLIFrJO3NgpDYt7FlQkRqfIDyrXFWKD9_4yQhnq_j-IyfW5dLpCEFEOVrt7UqJX_7NUtASeGlPV_qTDokloz1Y3m77JqS_tDOy4d1-UVrw7kmi-IZc91UHKKYHmLpudr8QZaLqdRwrlaZ5L1oQhzTjYdwaENoqF9RLXGtSabKR_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6595" target="_blank">📅 17:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6594">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=ogChmwQJL9o94t3pRd9yx3XhEpAfisjjBBsf3JN0fqN0lrMg6WJJTzZV9ENBUFT4PMH2iTWFjwdYOFjPRRhQI5DyZJlZL_qycWXegIA2xH_eFPokK3DlxaeB1tImXSOAAVTNs0eyw1Ow0QgdbDxXzJsBWXDi5Hp2PLoLXGOV9UxLk33MMPTNupBvaF5JIeSIfgWJdiXFyUcAmg-W_1-P7Axh6luxI3n-xKqPi3ncD7OZmOGvgMlsAxYmy8_Fv3AhsIfMPEKZfkshL8jLkzJ6_bynvhM1UWYrpu6ahWqt7hPod-W54OKQiQ3lgwm88pAKZ_ms3hpz68MfVgT9LK6t4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=ogChmwQJL9o94t3pRd9yx3XhEpAfisjjBBsf3JN0fqN0lrMg6WJJTzZV9ENBUFT4PMH2iTWFjwdYOFjPRRhQI5DyZJlZL_qycWXegIA2xH_eFPokK3DlxaeB1tImXSOAAVTNs0eyw1Ow0QgdbDxXzJsBWXDi5Hp2PLoLXGOV9UxLk33MMPTNupBvaF5JIeSIfgWJdiXFyUcAmg-W_1-P7Axh6luxI3n-xKqPi3ncD7OZmOGvgMlsAxYmy8_Fv3AhsIfMPEKZfkshL8jLkzJ6_bynvhM1UWYrpu6ahWqt7hPod-W54OKQiQ3lgwm88pAKZ_ms3hpz68MfVgT9LK6t4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l98NzIxoGYfOBPxNInDpaE9FYdNabrg9QWm3zmm64SFANd1JdfP2rJYsGYv1ZnFUrJmuUlwrsuD07kQwASi1q0gxsjYhB-GJLNjN2-gBTuLCKpq2yIflXRG2NM0NAjharlhucr2leiv7q1JL12x5hds9OEjJOQMBLRQnN_B5qnlA_bgqjj7v3ep5VfDHm3YNyNSGZifE_ZC0KoJnkzmTT4xRRFSv5RX5dabZy09qJeyCLjzXr5SOVheTrNiO-aD2hTup_VJM5Wg42rbOr177i8H9TQQlwvarFuKUrsl4OAQyrKXWuUtzfcJS4JB-Tcpx08zR5tB9SeE08vI5VHX1FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">آیا به بردگی گرفتن زنان و فروش اونها و یا ازدواج سریع با اونها اگه شوهر داشتن مشکلی داشت؟  نه! چون خود آیه ۲۴ سوره نسا صریحا اینو میگه!  وقتی هم قرآن بگه  هیچ آخوندی چه شیعه چه سنی نمی‌تونه مخالفت کنه!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6584" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=W1_xRyVQOkDuuOepdtqjlihOtay_oaebk2_vgGsYjaindf4cL2NGk7hcgdLM3JfvBrzwg-LFr3PcmSNR6QtLGCYxyLDaPKrgPgyV9He1K06NPuvWoCMiFyuAjsLvQgZnCvu5eOuXwV2fA6WrQ61v8JwhZ-aJh3o7qWc6PKLs492DrrSCp6ckKH4M6GyiIF08UkLEwRmDPNqYavp8SC90TfdGYGuPssS3T7VN00X9BKymYO6wwqSe8bow5WcIwehJ8Tme2w7bPALbNad4u_JrAKId1EZi-WUlBiOhr2wCQP79vrjYpzmYPQbWFr9U5bpiHw3aqtbqdHzwi3F3_LuTPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=W1_xRyVQOkDuuOepdtqjlihOtay_oaebk2_vgGsYjaindf4cL2NGk7hcgdLM3JfvBrzwg-LFr3PcmSNR6QtLGCYxyLDaPKrgPgyV9He1K06NPuvWoCMiFyuAjsLvQgZnCvu5eOuXwV2fA6WrQ61v8JwhZ-aJh3o7qWc6PKLs492DrrSCp6ckKH4M6GyiIF08UkLEwRmDPNqYavp8SC90TfdGYGuPssS3T7VN00X9BKymYO6wwqSe8bow5WcIwehJ8Tme2w7bPALbNad4u_JrAKId1EZi-WUlBiOhr2wCQP79vrjYpzmYPQbWFr9U5bpiHw3aqtbqdHzwi3F3_LuTPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0sKAgHRhYy-lccpMFcdpGqRCli6V4WtO8aOiJyvbZ_dfha93ZvWUYsBdjDLatJmcKmXQN3vf-A9EpInLjchW6sFJjXdm6MdqEH-FubXdDrVRrd43HFiujaHuwWqUFcStAYM5384T2Z5wjgYXt0xOMKQfuYlmw-bh30ktaBF1af-S6X2hKDLItUMeowBJv0P1A5jc7yve60RJlJv294u7DAYmr9dzCGJ2q5rSvjvKghq-3aFA44O1IO3-WtOX-mpXJWxfXEW7KyRdx7ViliBWDakG5d6eT2z6Z2JUGxnr6F6RnBfHf5zFu0_OIfCL6FqIzPSwjbaQzYN4thH-GPMew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifUG1RBmwIFFnTRCWE3rpDG5cj02bFH1wbl8hmwI5OdMSVwO7GTE4PzY1WDA2G3_CUUbyS1qPiu-DvX1XGCyfgM-DSY2FaZCKEl8_jhOK3tiAXvpJY2l0sNRXR6PLeIyinbCxryEMhfxOfnzvJtd6u5QJDSGWFXG98mkq4X9lZ6iWWFwbSNKIjZC6uFufgOjc6ieZGYxO2F_DJesVoSCyDSNABRb13USlpNpPZ6ggT7JPkwzmtXpfb0xoIDHFp6JVSwBKEwgmJEvQfrZdaNXFZ3JLo-ehMipgXx0l9CUIcILnihI0aceIrUKcCPgXhhTiha6eOviWyL5qaefORbnNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=sKSBxo3jTALd2o9ayrpA0zdItXScpGQmPRLvd6USJfU3ZU96pk3r4CZNs4UWoxRTLHbzlDcfxgnpJ5_rBmyJjCkLdGZyn9vzz-nXE810vpJVZlLY8qoJMHptwh_yVk16j7udjywxfSy7iIyf3emhale8YQrDNdFFYwfHXSlgXaFRqDXSDkxZc3aY6eW4BLO2NZ8qhFzjPSDh9B7qa9HFae6jh4N-6s0QJXvcpDDsJd1lXbD7O02T9-WmMKxPRuVWUVFGCbhKMdilozMSFmGVzavGRLMOY4hNRFm69AdleAzYOoVjmBILQHQ7XsRFSYrsxEFcVWD7WOoACb7LD0jYdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=sKSBxo3jTALd2o9ayrpA0zdItXScpGQmPRLvd6USJfU3ZU96pk3r4CZNs4UWoxRTLHbzlDcfxgnpJ5_rBmyJjCkLdGZyn9vzz-nXE810vpJVZlLY8qoJMHptwh_yVk16j7udjywxfSy7iIyf3emhale8YQrDNdFFYwfHXSlgXaFRqDXSDkxZc3aY6eW4BLO2NZ8qhFzjPSDh9B7qa9HFae6jh4N-6s0QJXvcpDDsJd1lXbD7O02T9-WmMKxPRuVWUVFGCbhKMdilozMSFmGVzavGRLMOY4hNRFm69AdleAzYOoVjmBILQHQ7XsRFSYrsxEFcVWD7WOoACb7LD0jYdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Em8l6LG57q4zD1yEvjVmMTQnBWzCzeP7OPDGUeUL8EjshR-J_bD1cNCUSwPoWmb0LLNxu7aY0uIvcz_zW4JbAGICkrFP1tivNhXrj00IKF-EBDJ9l9TSbhSfWtvk_QTeU0FWxI-1znTgn26vTyrv5Wo4cjJgEdzLeF_AQtiLBWAC1rGJL5D29QJGX_OT5BxjbhiW14n4kIDTlqI6ui0AmQZEB3izs6joxWHe0cT-JFwTD9coNVuYbYaB5SymNsX5auWxMQXwE8iCtXzaI77hqrrxqIVXEt_nCgnlrmRo8MLPHZjC9VQJaP_1P9dgG3dIK02EMtKJrkplRb1ob5775A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/km7v6--uW_0qIyCj-JqplSm0cxx-jACRNLTHbY4zlT5ZzHOP5QL3bzmGq8xauDEagWir3T_UO-eV8PpvwnW5Mlu8fR_kH7K9o2PseV9EhhjZ55DHCQndM2-jp7t7tyKM6Ez-_BUFrm1g7JxZKwRMo6AxFI87CaJ_uokjhMYmykVcdGrSa2BZ9_hmMVLM-cYnvkvt6YP_jYBE5znoARgU2JZCjtXgCJv1iR-NtSJX5SkE_9AS1E2lW2IhykdeiipKvnABeNTnSPwvkLPN6kaL3GZBWrikKLiB7Qlx6PCd21XBDeg2ilxjO-LfnUJvdpaJ0f33PjD7fVKKOYou6ckffA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlTpWPjT7fvEzDPxni3AZmxZTzbvAPGAz8wY5yBG5Un1OF2T5w6Z93ENvXHvm8zDl-XCdN4yrGEqXGZaU6UmBvYEyh2q2x_h83G_6N6EaBpDCqwoQSiIYjBUbs6xC7FfcimmUzRy007Zl8g2Ar7qExWU7b-9dDYh_GjLr6VBfaJlGu-OJAmEypoY4XUbpUwmFNZovZ5iLeDITkgIjoxwgi9gz4hL5OG0RIaYQrqANlC1zrUaUZbZtOmJbyuhJLjL0h-p_EDOQ1TshXGM9AmrfRJvGZF19HsKauzJ5ZCjDHazzR6MxGGSNS3_hCpUgZsX19KLC_78FBhTaC37Mq1jbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=eumzLLSjiaJjSeEBADooBwY1oUClvZ5LJS2r7xlyKVCZeuGD2VkRaGdCcY_dW8QPU-ma-pcO7oQI4QsDV7nBaWlSGde7OFArdRdOSR-IEccVYbOXJ9DVw8iKVMs2yCM1EHt5Mw7pNvMHGf2OSr_115bYlZW2KcqS_hIxbfrjC2FDPHvwVcTu-3RRlPuQTkjBMPOdRP8-58muGYrbylEX1ZIeiwAKyh0Zy_6_jZdHFJtb3dHiRSIo4C9X_ebHiao5SFFQo0VvvcxEyMmbGw7l-IMapiCn94knhrWxWuZg3l2ts6aAPVSsawVckbhI4UanUsdG2MPMDT3M3yyRNQZT5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=eumzLLSjiaJjSeEBADooBwY1oUClvZ5LJS2r7xlyKVCZeuGD2VkRaGdCcY_dW8QPU-ma-pcO7oQI4QsDV7nBaWlSGde7OFArdRdOSR-IEccVYbOXJ9DVw8iKVMs2yCM1EHt5Mw7pNvMHGf2OSr_115bYlZW2KcqS_hIxbfrjC2FDPHvwVcTu-3RRlPuQTkjBMPOdRP8-58muGYrbylEX1ZIeiwAKyh0Zy_6_jZdHFJtb3dHiRSIo4C9X_ebHiao5SFFQo0VvvcxEyMmbGw7l-IMapiCn94knhrWxWuZg3l2ts6aAPVSsawVckbhI4UanUsdG2MPMDT3M3yyRNQZT5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=JT-xEQrlj6BSrXwkmhxYA1587STPj9f9h5zAIttTmfoO3Io4jjWBbvenDPL30GlGjKjUzbUNIAeCT_ic2B8gu-VnElTSrlB_mevyDWKAAA8u-BNkdWWNulTudyOEUUPK04FUA7_gPWQVqhmtrTfN-a-na-Jy5DXZ89Dau7Y1G5oUSBjpjP8ts4b2gzqdMPJoRGBQiW-GiQrZdawafXwg4EYlc51UZBvQubcoTdIjqh9AoEE6rfrXaFIGmYPUuNsHrlJjuLFz85fnpZ94a87g2VjPZKDcnqFvAlvshqCKF3A_AJq42hj0OPbplkODIi3jsrM7JtyB5JijLQQHiwGWbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=JT-xEQrlj6BSrXwkmhxYA1587STPj9f9h5zAIttTmfoO3Io4jjWBbvenDPL30GlGjKjUzbUNIAeCT_ic2B8gu-VnElTSrlB_mevyDWKAAA8u-BNkdWWNulTudyOEUUPK04FUA7_gPWQVqhmtrTfN-a-na-Jy5DXZ89Dau7Y1G5oUSBjpjP8ts4b2gzqdMPJoRGBQiW-GiQrZdawafXwg4EYlc51UZBvQubcoTdIjqh9AoEE6rfrXaFIGmYPUuNsHrlJjuLFz85fnpZ94a87g2VjPZKDcnqFvAlvshqCKF3A_AJq42hj0OPbplkODIi3jsrM7JtyB5JijLQQHiwGWbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماينده ملاير با چفیه حمايت از غزه و فلسطين!
«مهسا امينى به درك واصل شد.»
مگه مهسا به شما چه ظلمى كرده بود كه اينقدر طلبكار هم هستيد؟
غير از اينه كه به خاطر يه روسرى و به خاطر افكار عقب افتاده‌تون، جونش رو گرفتید؟
حالا ناراحت و طلبكار هم هستيد؟؟
توى خودتون و دين‌تون و نظام تون
و چفیه‌تون و فلسطين تون!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6575" target="_blank">📅 21:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRNLJ40t7WlGdz1zLdXA_L84fvzNfFqEn4RU3bZFoHpKyQf2g7gA4by3qRakhApWynunewQcC7BqHf2apiLJYl4YbVOGwKvQW7S2bqg52_mH3TZGcT2DozcnEy68H_AGe7VBEaO30zQXCxNmy9zIvRVf4fysDamhSsedIUsWfT1K0qgjxnpJuMA_jHLqEuZmPKwWzlK9Gq-uWkSOyO4ONVs6gKIZ1wgTRwpOLlliGrfW5SdZOFJ2EQqazrNJsq_Y32lB7klmqK5i7Ox0M822yHCyFHjlXmSoWIHTXfe2Ap-CP2QY_pB3QLIZZemRrZjT_vTAX-nPquuSXip-H11Wyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgDPokRMoZ_pAtYPJrzJniBS1jMJphlQn6EpOgpgvFveRWJ86DQXDMSWPApsIwczwCciXaBz3w1m0D66Q9ixndFTWfG8kLpQY53winHNKVwNtHi3UgSbL5bYgy7S3dBSTcy-Nq1g-bziHn-OfFNBFN5XvHyVtZKI5T3LfDGHD8wgDVK618HRsPXOI0LY0_R_k8uUFKc8yzIV32HlDf7uvlij8O2G4Bld0UZj2UA8kyG9MwFSUx-pV3GjQs81T7wBGPVlONgpON6iwqMEcmH9TMj_dODyeB3YKv3uzmWZ5YwFddb_TZhu9l7ybI1Azeqr0uxLZBGmIBGRdHBGjKaphw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQgqC0J7BS2EdstOjZIi8useb8y4V0LnpCTfR8qA4y909zuhlli_g4L4QU5BkRNtqP65uLBbQFYAEWHcXLEh5qRiJn3p_nmm1kLlwHE3xbYc9XHlP1SI7ZRTYgAYSIz-fnGNW6oKhiKrdhZ_ZorIx7ms3ue9pzfv3hPZzAMIh3lL1xWtB-mRkVHJBKBItmVUuA_hhXzN7OqDQKo0NmXpe2Mme20D1XAn1Qj7nQGqFMKZ_zevV5g2RJFQGXpHpVFuUhB4kJ3JbdrmVU6WZvcsp7A6mYgbQOwt-z2G2jMWMWOx30g23fglUxPzD45Aa86TvECqJKPhoNLJ8ihwqBjKCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tq_LLkHbTZ0ci-sc-tSs-A-AoR7gUwLW95G0Gvu74NtOAnXo97Hi8aFkrrvRmQEj-tj1V-rfY8vyRXrk3E6qsTyee6KoBk4alnuITZ8uqOAyY4sG7QP0-N9Fg5q2gGNAxEb3Hl62C4WwPZJ6RkenpQbp95HZLlZTdkFW2YrJupuP3ORGfLwSefBBfiupO0n7jK0LJMsp_Mve00cnXKmMYiD545YhMl_PvCi2iXQsgU9bXoSFRhnhZf2PrSyf-CJolhwfqcbk3LYmKA8WHuF1XxfL5lQSOKV4lKWaE0PQc_wAqOd5nsTuxFGACVwMWD8xkZ4tZFB1Vdwbv99QkHHdrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fk4nmo5mT0JPmeWx1qdFAx57DPDmhc0p_zTJ1xh5kF2wiIIwfttaw_MxExNpWOesjCDc868pPEqiePfcPPOhJtQH21Q4YMg2r9VlH_ycCjd216P9OqK_pkq_RUEdgWb6E76BCWnsTQPWBa7qFw2gbucl_4VCURLLRHrm-MbOtpGJSOtmYPIZewgJB1tpg5ACxA8wPrgfFj2vVlXQvqIE7Y74oPKkhtLfgMKRI3MSaTMEjQF14cPCqsAHgmyvw1pvVvKQHfT20c5k-uA2dFM3r8Hvvw7FxmG5fHfZ-jcT2-xgsDmB1nv-o1k90HUFkHkivluXdtT8xC0SwP1cwA0f_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzPXSHA0zY3mwMf-bkJsbGksii-NsmMJD37w8dnwbJwADT2lZS6Fj4QQu3m2IJQgj4uTLYbUS5FIl4S63O4pq0SSXxjWtdNzaVbsM6Ib0BRtcXnjmaZ7pbNdQodzkg71kQk95NhBTKFRAjntc7lCrdx0KU2I92gxqRrQoee-XDv8XdfX4dVQ_yu_yx5SJiSBUO23C7S6BxGKggWBrep6O5Ii6FUP9u-TxhhUhyJFBNgBMIDpAxObtJZHmqknK1jUvEYhWLxIQkZr-LKVUGLiw2LSUCarrd_PiNNGyOCEYAMvTn0DuqBasxwlwkOh6hBnXTp-97ccDVqchCvD6nbyWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر سیاست‌های این افراد،  از جمله این زن و شوهر،  کل کشور و جامعه ایران درگیر یک بحران  عظیم شد، آنها از رانت‌های بزرگ حکومتی  برخوردار شدند!  سید محمد هاشمی، وارد کار و کسب شد!  از واردات قطعات سلاح برای وزارت دفاع تا واردات چوب ! از جمله پول…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6569" target="_blank">📅 10:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">معصومه ابتکار و همسرش «سید محمد هاشمی»  که او هم در تیم گروگانگیرها بود،  در همین ایام گروگانگیری، با هم آشنا  میشن و باهم ازدواج میکنن.  سید محمد هاشمی خودش فرزند یک آیت‌الله است!  گروگانگیری ۴۴۴ روزه موجب آغاز خصومت شدید آمریکا علیه ایران و آغاز تحریم‌ها…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6568" target="_blank">📅 09:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tE-FhhGnkNFNAOxtW80UotEXVL3upv1tZdZuXSX4jkbrj-N4AgKTkvIiAvPcYdY_vvv0JnZZLSfZK-oIGphZtK-i2iUDBti9nFMs74SqQxoUlD4hXM4KdOCptcRgTcvGDm5REUZF9QTL3eOvfotONGDN0HojAx3G89vpqjOJ33EwIkfUAzFEiTz1ZfD86o6svor0GfvzlJxGn6jFYlgfuFOTz2Ht9cfc0w0X31Gs9fmUCayWPIYRGfVuQD1QswGSfSYn-VCa0yRKqe7BXZa53Rb1a1CTj815ZZvvaumyLL9XZabHKi4NilTKUG9-RvzAMFF8j9Ehuf9k3a2078GaJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم در این نامه به مقامات آمریکایی نوشته  کارهای «معصومه ابتکار» ربطی به ما نداره!  ۴۷ سال پیش بوده و…..!  توی این ویدئو که خود مریم گرفته ولی، خودش دست به یک مقایسه میزنه، میگه بقیه پرچم آمریکا رو زدن ولی ما پرچم امام‌حسین رو!  در واقع عروس خانم خواسته انتخاب…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6567" target="_blank">📅 09:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6566" target="_blank">📅 09:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=gJHdw1NXqM7oSCmR_Bf_3eoihM0XM-2o-zwnSLUgLBpBxaQlAlnBRS1ZsTyZxXOf2W9ShjxRyxPo3MNYcLcc01F97zAQsg74DdJ68jdxo9Aet5o247Nm9kZdEyfqcB_uacIH7rU5eWaiUVJMXUYES5b-HVAvjvC1KkFkZtogZkgXEtnb_qc7fTGt9a8yFKgBE28qMP4duZPNFQDnnVyai7MlzmTqw9LXIZBDtN1fdlyDNQ2jgqXIi6AkmQ-7VH2ENhrDyXCXBiz28XTnwCs4KPmNTwYmvsQnKMtKQWnk5wPGSkyFa_RniSMkODaGMpRwCfIqXo94C1jUhnqrwFM5Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=gJHdw1NXqM7oSCmR_Bf_3eoihM0XM-2o-zwnSLUgLBpBxaQlAlnBRS1ZsTyZxXOf2W9ShjxRyxPo3MNYcLcc01F97zAQsg74DdJ68jdxo9Aet5o247Nm9kZdEyfqcB_uacIH7rU5eWaiUVJMXUYES5b-HVAvjvC1KkFkZtogZkgXEtnb_qc7fTGt9a8yFKgBE28qMP4duZPNFQDnnVyai7MlzmTqw9LXIZBDtN1fdlyDNQ2jgqXIi6AkmQ-7VH2ENhrDyXCXBiz28XTnwCs4KPmNTwYmvsQnKMtKQWnk5wPGSkyFa_RniSMkODaGMpRwCfIqXo94C1jUhnqrwFM5Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=frOG6H6uUbu0ekvhfeWW2YZmQQMfQ616dCuJ326eaf-UXcvvIO8R3hHyaaIwhqZfIx2R1cnUkA-xXrvl00rEH_F7_IYhiRMtOvqbkqJYBqe41K-y5cUiipH6tts30CwxRdT4hV8Yab_W4lcTi6zFplkq2TTioQURb7bVvf9TI6NO6h9UbRpXuZPSEByYXYVYY2eezi2mApIe3sD8ez6MbBn2GjwxVvP00gqCGbfA870h3F-axVdD78oob4OY7q7cfgFhltvdYlB3b-uhqE6905BAJc0mm3adi8oxouB6SI085zU82jtGsB8M4QfJ1qNSFSXfH50ES2ZzU1Yx8pjDWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=frOG6H6uUbu0ekvhfeWW2YZmQQMfQ616dCuJ326eaf-UXcvvIO8R3hHyaaIwhqZfIx2R1cnUkA-xXrvl00rEH_F7_IYhiRMtOvqbkqJYBqe41K-y5cUiipH6tts30CwxRdT4hV8Yab_W4lcTi6zFplkq2TTioQURb7bVvf9TI6NO6h9UbRpXuZPSEByYXYVYY2eezi2mApIe3sD8ez6MbBn2GjwxVvP00gqCGbfA870h3F-axVdD78oob4OY7q7cfgFhltvdYlB3b-uhqE6905BAJc0mm3adi8oxouB6SI085zU82jtGsB8M4QfJ1qNSFSXfH50ES2ZzU1Yx8pjDWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6564" target="_blank">📅 09:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است!
و این خونه عروس معصومه ابتکار است.
که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،
حالا نامه نوشته به مقامات آمریکایی که من
عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6563" target="_blank">📅 09:03 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

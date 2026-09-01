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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 19:17:59</div>
<hr>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJWuY01drZNVG8GPoMrii_P1eCcskbHS8d12ELYOFoG42S6CSBkoFtdx_K1bZFJwkfOx6EWloQU5LbztAkkaTA4eggBx-kiezZYuyhg4jCOpnptmYBXpEFt6dsQeBFqOzjRc4rUGMrSNrlI6v6SZM21lFrboMvkpqMcRL00IOdAMGWnsOuCFgMNxLu5Y1W8IKkD1LWpeTg_IZ6fPopOmq_4GiYh_RShRZqHIABRzkEqYwAaxhuThlsgFndWYYt5u-BH2uuPdu0pezAyBJnGbxi1DSWZwPA2tpSsgl2MznNYQ4ylwot9ZrCCpZ8R7LpEZmBaI83HSEd3qC5mIWIqg8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WP1ardfHXK_oA3UfPU5e43RYvcdW2SyappBciTUhcoBc47unluEIuLP2TzCkrSy-NBym8Gm9888b1akkgEwqEwJKMc8sCWgDsqmUzJ6yDxykiy7tv1OI2J5nnou-2sY3Ocjf5DkMuMhoQkq-r2rMg_mjiP2_B_D4HxqkJddDSv7JjvCJuWv8tB-95dVYKOSCqTla3mTrFkZbhZ6yRy9Em7W6gOM8FTnWCCa3jKJFzuO6SrBD25cw2CULYQ9rdnzTytgtr4r9vUVXBK5m_DCZQ-X7IxTR8YYXIqWWZaiouu9UvK_5i67auYbPBGevQXf9SSty3BTg_ckm2q0mZo0F6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=e1GnF_NBOrd9h4_1ohL5vGK3utWNRukG3tT8Yb9S7olexIR67vy7kJOtKBGNq3FJ0raQa6wAUew59JXZlOZ2BRCpxFgweRtjXqwcH4qqsSXeU9EKoVCL_Zd-a_xcFBh2JoAB9F0NbjcTzvzGf0_1hOtr5Y1yO6XEYsU7U175IVK1eLLt3bq76Xs6kdw7f7BJCyH1MeXtEPdLHu-ZKq9vuPFE4xVR2_E8mBAppMe2ayxEGzLnRjp5qhbtx9uSHlzG84UPVtY7BjfJcBkFw5nhzJShq5bm2wMpISVWr7iB2mXlJaFKWQ_SpU9e-tp8QX8HdExdd5EW_pcv6vToFfxpBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=e1GnF_NBOrd9h4_1ohL5vGK3utWNRukG3tT8Yb9S7olexIR67vy7kJOtKBGNq3FJ0raQa6wAUew59JXZlOZ2BRCpxFgweRtjXqwcH4qqsSXeU9EKoVCL_Zd-a_xcFBh2JoAB9F0NbjcTzvzGf0_1hOtr5Y1yO6XEYsU7U175IVK1eLLt3bq76Xs6kdw7f7BJCyH1MeXtEPdLHu-ZKq9vuPFE4xVR2_E8mBAppMe2ayxEGzLnRjp5qhbtx9uSHlzG84UPVtY7BjfJcBkFw5nhzJShq5bm2wMpISVWr7iB2mXlJaFKWQ_SpU9e-tp8QX8HdExdd5EW_pcv6vToFfxpBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=CXqMRIpIVFNgDfGf1NwIw1FGnXT9c5fSGk-GRS2VyV04dMVRUaBC7FZOw8T6m388glOIARc3ZtuLOWRy78ydwr3Ai8Tly5dG7oITICPoxZQLvOxkCNAcgkhKd6HY0lW0nWNjxvKPVeTOs42-gXb66vMQqwVfS67SSfh8oA1Ad6pbKOMqBbEM2DMACmlrcuKNIEStmv_jChPiUtQtIvNVyGVegSyaGgurqNNRVLO2CDbP7quJ5HF4ND-NhxfKZL8V1Cl8YSVFiAkZx-XjHT8_JLEeVkQhT8QZCkeHtMesUB-AHGswJYE5dlN72WdNalu9kw4zwkdfBr-wR9oSa0-mgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=CXqMRIpIVFNgDfGf1NwIw1FGnXT9c5fSGk-GRS2VyV04dMVRUaBC7FZOw8T6m388glOIARc3ZtuLOWRy78ydwr3Ai8Tly5dG7oITICPoxZQLvOxkCNAcgkhKd6HY0lW0nWNjxvKPVeTOs42-gXb66vMQqwVfS67SSfh8oA1Ad6pbKOMqBbEM2DMACmlrcuKNIEStmv_jChPiUtQtIvNVyGVegSyaGgurqNNRVLO2CDbP7quJ5HF4ND-NhxfKZL8V1Cl8YSVFiAkZx-XjHT8_JLEeVkQhT8QZCkeHtMesUB-AHGswJYE5dlN72WdNalu9kw4zwkdfBr-wR9oSa0-mgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8rChMa6x3iaBk8XLpiEIvS3KxEwDl21U8K8KuBVKm0X2BUALiDVr_d9JH3o1s_8jpSj73pciRBp45eNwPaJCGOcMFEa-nbR__No2YMuzVcpA5OACtfIVuoPXuufjuvgltd-8jH14YOHMRwYrpommsROp_60xHfK2eMjIJsKPlgszvxnAcWH1-f5S52c4D_xL-Tvtt8_FkBxEnzhc5E_otPHUX4l7FKgt0EHwG-Af1vaS7xl4jHmhc5kAOrCu2VXKo2Qsl8AGAnRWBREo9aPGaNie7zHvpOxFHCI2fVYTX0f5ZtGnLaPkyoIGsi5DwkHf9nKsn4tudAyhvN8KobkEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHi5c9-FHS8-QGeypFRHvH3TEyHYN-AW_TOSouXDoxa4BsiGSIGaJ0Eo-Sr6CUb-JIiGyasuIL4rI7VDXhJBfDzehgdB0xkWRN6EaCc6-7Kz_xEvBGeUFPXszUhFkfSXV9khqXm_5BZqUqUvU6RolqiBvfHclt7wRcQMNOIsVbcUqb5f4CWYgiOmgASqaZdkrwHAyiRWkNG4xKGuVs2EphZ27dIcWbE45aoH3qZtTmweargcasM3peq3TimOdefF8X7XZ5S_ubchVLFbdzvJju4LGI4W6e5g0TVwdxaFU6iPRLUizQPm3HspCANhYYDkrs5F7QLHUlAnkuzR7OrNSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9VnE06oP2lfyHGRfLfXWLl4AzCcwt5wb-7_WZP4K8vFnYwzMEDcN3Z6zrGu87VMTG0mTGGbPIu3zeCJW4_zV-CH6ohS01GBm65l30M-xYvv1vQjED5hYOoQmX8D21FNKHjQUIr7gsL1jGH-zEB5_-Md8CC9WE7Zufa8DKBgIa27d-icmMlLPJCY_faFssHygLk7p1m5jbHgczkWxp2Z5EnNac0_vRNllcnaplIsBDrrTuY23u5bdqjE1SLLuMCMzJmvNrhP4JW7FS_Oou82tdRNi1R2LdXTStHxgynQAD3yQY-wKRVm31vNkyCy0fxTRpF330av3iPagnByuC7Q6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCnNTw-5iauSaCfv_TwxEWpQMO_RhTRSAHeLH2KGFSsRW6BOgaDE6kTDQEVbIuddNfGjSTxounT3P-rzuVJu9D0tlAOzwxJB1rClU6eIUu9wIiu9Zu91bOTcii-g-KICiQ7_V4nsb3_jDyUKD4WTMx5o2YLp6Zxh2TgCdcWPQLvb8XOxKtQCswYVH4Dg-Tdk2U81Mo9Jf9YL8uI7EjS_JdSu4WO559x8IU0UcFG_f8gVqT0NHkBEq3M221QGxioXVVwspAwoUHVutrffEQhXClZROGmHYzDZ0cScztpRjIGY1EU-k5eBnFuYCX3PBB46vEXQRgBfR_hqnlPpco8sQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVbxWBeg6_4AYyAFzRAu661PcQpL3yEX4ugFP6AmVh_MWHfD06-Xj4WpIHFmgR56iG6E82IsF8GXOUDkMvHwIoOcD38BtS40aTSZ8TJRfZcqDAh9vNhCSBbtuLgILwzt7LV3gI4rJF35SJ8IyrzXC94RuMaH3hW6crSDXn-6Xq4QVE3o77ATxFf4iVy1MaSkt5MkNds96JQwSn53ujaOHE0AgbmLApMwmPnExEmOuff1tHM-ivJGEGjcFcAJQNCdvKYeb7w9orieY4iBE93pQlqmZhOa_Ucj1vFOYqIc1VBobqdbS-zoQ8SGqlHeHetwqzeIi63z_n1HELz3Mzrp0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlUAdS89jJqDljgPo7Ns_JxYSG3cvmPo9ts_o5GOM74l1nYRbpfeWI2o2T051iqMZ8TPfh4lK3hW3bjmOzPQBcLYAXCIFkJbm5Ff2Q_73SO9hpjo3rEVGv_Tlz-H67q7O-sO2-yL1f72t0dSUTV_WUOfBXu0o8_w17Cdz1nCsqPchvAgecXzjTrq_eL82qwN6ITTjyJnHmF5Rhd4lBDHA2WO_LokWR7okDule6Ojrf_cl9sHoDhgoSBStOU-KTH3ngsteoelqe5iZmS-ktuJK8dx8yDqVX2lTHza3AlqZcmxKZ-3Xgkep3Xhm0c3dt-cLapnRqvgQ7xJEwcYBYyzKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=Kl-BpG5EpS3he8Bd_2a7ocyNE2MGDiIk9dj-LHPkbeUOv5aV9XgyQxGzurh5-j6M__1mAYzj9KFqbRwesScCCmceqSzAzWgMB-OCR7Qrwj7SusV7G10Dl6aOMQjN-Myjnc5P3rqHcNfQBh5wUG7HQG9VYEkBqL0BQ7EQU6BKXjfb2WiMg57fSY1KZwAdCI6h3pRY38TEtKB3M4U1b9WrPhXEV9zBPXJg9rClUpg_LteWiEhfTXzFyO6dQQesTNik03QPRmzf2HAf0B3pHKb5yZyjOKd1b7H8RFffSVEvdG-orqDgdnisY7B6uyZCNqHCCXtVcPfUR1OQHBsQhBjTJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=Kl-BpG5EpS3he8Bd_2a7ocyNE2MGDiIk9dj-LHPkbeUOv5aV9XgyQxGzurh5-j6M__1mAYzj9KFqbRwesScCCmceqSzAzWgMB-OCR7Qrwj7SusV7G10Dl6aOMQjN-Myjnc5P3rqHcNfQBh5wUG7HQG9VYEkBqL0BQ7EQU6BKXjfb2WiMg57fSY1KZwAdCI6h3pRY38TEtKB3M4U1b9WrPhXEV9zBPXJg9rClUpg_LteWiEhfTXzFyO6dQQesTNik03QPRmzf2HAf0B3pHKb5yZyjOKd1b7H8RFffSVEvdG-orqDgdnisY7B6uyZCNqHCCXtVcPfUR1OQHBsQhBjTJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUTjEqR2Ls95AwNOkPrdtZOUnqLUcLJiX7p8KmDzO5U9cUCzakO_2ApcP8zWyYW2YkG8tDi0CuIaKHhKmejnqTWLuFE-PNzCL76fsyZMq2MxMWUD-bJe4DxsZ4HBscTsJwajh1wijsLCjAlAjsGCA2lE39WXeiS5v_R4poj1OOf56jG_MebFBXgEQUqfExpnnZ4gyP2yqkstilaTcUSldQX0jno9WK4pg8kGTJWMxwDjdnLNEtGLF-GIQU9nMQS8yl91EdIL8uJGboT5xBLn83BYo0jXpHlsQVSsJ_FhvsVrNeSWjgOHb7aEtRVkp9joIYKs02tubhqAuwvDJ7L-GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=L5K9bSBJEldPh7KnomTCIgmwMK8uVTT2j1_5s6CxwcEqV_A6qN5Li_DxtqGd_19YCx5n--iwxfHIV0BfJvea27P35RLzc8bPDrT_EqzgrDrjgtIrZRjWdYy0HUvOGVGG2VhQ7UBpBScFRAzyLa8HBODyhVDgFfYZPbxucp9WdKnIXiWILvDBkSewobyW-J5PYxhdrvGZAXxV4irDTnw_RjmC8awqBJTTR5F1zARqeQSBqFBBThRPxlFmQSyPl0QkIX-dINHTfXhc2qrrjwu4oAYC365yi4JC1qsTQD_LhW07GBtAnMCGtyLU4x7Nj95vo039pG2Q5F8EgWxqv9HEzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=L5K9bSBJEldPh7KnomTCIgmwMK8uVTT2j1_5s6CxwcEqV_A6qN5Li_DxtqGd_19YCx5n--iwxfHIV0BfJvea27P35RLzc8bPDrT_EqzgrDrjgtIrZRjWdYy0HUvOGVGG2VhQ7UBpBScFRAzyLa8HBODyhVDgFfYZPbxucp9WdKnIXiWILvDBkSewobyW-J5PYxhdrvGZAXxV4irDTnw_RjmC8awqBJTTR5F1zARqeQSBqFBBThRPxlFmQSyPl0QkIX-dINHTfXhc2qrrjwu4oAYC365yi4JC1qsTQD_LhW07GBtAnMCGtyLU4x7Nj95vo039pG2Q5F8EgWxqv9HEzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=om8cxolDtUVY_rt0yjrjECExvMPz-f6ILd5dpqglE2SI-gzRqvwAOBa1h6HS0wRfRFiZXjWuh0hTbmm4D98i4OvV9aMzrP0C1KnNq6lbkKIfUIcIdXxDnNSfLWEuNi3Yj-0Xxyzl2TlnAiOYc-IKNMnyNmrBo6wKDHQgNIbSuCxXfGR3XtlILHFSbHs-k5nQ4E3IF4-0Cw0nkYMdnD9G08ocKOmtyRESqkvuxA9_JH2PO3t7Cnk8CsCosnJSWB9VukpYHaGng83BOUJTWwxXrXj2d9P07cVsQcfRGw9Ai1KsYC5ysBMNfYy_4XOHIezKkCn64Dfp6tg5lHa7LsFyEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=om8cxolDtUVY_rt0yjrjECExvMPz-f6ILd5dpqglE2SI-gzRqvwAOBa1h6HS0wRfRFiZXjWuh0hTbmm4D98i4OvV9aMzrP0C1KnNq6lbkKIfUIcIdXxDnNSfLWEuNi3Yj-0Xxyzl2TlnAiOYc-IKNMnyNmrBo6wKDHQgNIbSuCxXfGR3XtlILHFSbHs-k5nQ4E3IF4-0Cw0nkYMdnD9G08ocKOmtyRESqkvuxA9_JH2PO3t7Cnk8CsCosnJSWB9VukpYHaGng83BOUJTWwxXrXj2d9P07cVsQcfRGw9Ai1KsYC5ysBMNfYy_4XOHIezKkCn64Dfp6tg5lHa7LsFyEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bc03eDp0jj71lMqx3LJ4NzGYZ1GeX3Q3c0-YMZ2tklf6WtHn2OwGBLMEjtkjKcDKWHi5sdnNUCHRiQhFkmIwfgUI4VCOwHgFDoly6SrHXiO8b1_NrShHgqJqClEUupFKDrL_Hc1Nys4Ax9TACbY56fuDsjHJo1IBLUIDkVy1ITM0292ugO1a40yGnywftnq0y7K2Ou7BlgUUiUjckTRPhi1Ugos7tOY85kW-JTVnHUw_jhhD4m0ruyvZjh1Q7AEpdLSFq9FAsdoCchdAcSjAeFZnfxX7fXOZOEb65cD0B-CALiIfpfIw_zyrBok9Rz_gso08MLUwe62HaPm3JPNV6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQen14QVTlbgzt_KV7TtFcjiKY9QyqVOMo67LXypUSe3QYzRZaQcTt9bEx3NJs9uDS-No8hdqQ6Gyjjj1rkqMKJIbSJBDKEQmxuGjSHN8QB9T_j-vKMvpGppJPQJ0cuRbOfPM6YLxMNBaF-400wdZq-4zDRrI1St26HN8grkitYZbZ3a_qbybxnug3hFr85_6F0S-NNmGWsySYNPtYDaMg-ud0qo-z6x07FHs_XLf0-IManPpCF8uz8k5Pm4z8U8hFuieOb3eXew0ImZNDIyOG5MAEzvdfBFHgJ7EwyliTUbBMDwxLAflpAtyeTBVXUQ-cR_CqNO2Q9dosV6otf42A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=pf6G8ahKqFBsGWDHsFurRB2-WAMVTgSJ4zQVAA_YuBUrLNoKVYmm4aySwsF7WnpUeec9I0jjpg1aqG-93Dmbuf5h4HvgTVhHmPW4jitJE8dmqLKbFiJGAHVUI33lao2azQLfi-ZnV3evTuv7MW2XkzuD--0dqqjzd4-gbxe2dAB2Y8Fy_fEqxt4gtra-v1nWa2RsMfzQgS4OtCgZyA6sm0HcXVMV7cF5g0igG-ouI99msb1WrIRUBlhFmNc0fTS0lRloQ3PlPd2Rev8JWTur9GEsvvCREn0mjxhuRqB2GByNALD5saK7tkqxwR2MyUsa0i4zBs3y4mkFBVET8-M56oqPOpHtLEZ8mm_jEaEtVQvsg_ePMN5YKekbP-Pv63E0gdbSYC27ev1BA_UZ7-rbW4Ar5T5b5ttMhv9xP9sNSqPYvVBcPwXvRveibdpU6D2DPU-iDz4m8bF3uQQhPM30ejWjw084jZNq47E6sdA4NSv6KbNPL4crp49pXDbOzrzuoEp5BYMS4DzppTzsiu8VWekAbWEBG1q4fhNSxiNu12KAJE1Rnyf3qJc8at8cKp9l_91eWEEIeRHy47cP4nfOz7rnXnrGiTzQVw2RV52Des6ochUp4AwvrRaBS16G2ScoZbhj3jftd8i0wsrTvbkKoG_C3o4IAtveGN6LjB799iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=pf6G8ahKqFBsGWDHsFurRB2-WAMVTgSJ4zQVAA_YuBUrLNoKVYmm4aySwsF7WnpUeec9I0jjpg1aqG-93Dmbuf5h4HvgTVhHmPW4jitJE8dmqLKbFiJGAHVUI33lao2azQLfi-ZnV3evTuv7MW2XkzuD--0dqqjzd4-gbxe2dAB2Y8Fy_fEqxt4gtra-v1nWa2RsMfzQgS4OtCgZyA6sm0HcXVMV7cF5g0igG-ouI99msb1WrIRUBlhFmNc0fTS0lRloQ3PlPd2Rev8JWTur9GEsvvCREn0mjxhuRqB2GByNALD5saK7tkqxwR2MyUsa0i4zBs3y4mkFBVET8-M56oqPOpHtLEZ8mm_jEaEtVQvsg_ePMN5YKekbP-Pv63E0gdbSYC27ev1BA_UZ7-rbW4Ar5T5b5ttMhv9xP9sNSqPYvVBcPwXvRveibdpU6D2DPU-iDz4m8bF3uQQhPM30ejWjw084jZNq47E6sdA4NSv6KbNPL4crp49pXDbOzrzuoEp5BYMS4DzppTzsiu8VWekAbWEBG1q4fhNSxiNu12KAJE1Rnyf3qJc8at8cKp9l_91eWEEIeRHy47cP4nfOz7rnXnrGiTzQVw2RV52Des6ochUp4AwvrRaBS16G2ScoZbhj3jftd8i0wsrTvbkKoG_C3o4IAtveGN6LjB799iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZhBkN7dH7EHIow0NXi4eVCeY9_80ngwgyMQLVd8qD97HKtO5WdCHGLNKhPhBfvsjdwZjKNgZERGmn3oYz4570m8Gd8PmYEVHXDKJLEL49o36OQqor1O1NCYsHMq0WjQpp7NZSRg2uzIuxOlaeIoY3tcvENttxnBD3kAr_TcPMGFKnVdbcJqgVS22uoS-lHnUlNQG16cCWuFrtWAWOZ2a-dBhtHp9859K3LrlLe9ffBxEGb0rMsx7-vSB9MM71k1gpYU5VIqQrxSqncnn9nV6JESvIH9Rsnp6mpuVKTTq6OToL9YR0BQjyj218BTYvs761CluIXS5QH1LCNukHi3Vg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=ukDuOdP_Z_CQuEtcgs7kh01UQroIgqF7aINuPSjYUmlIhJTVaRSJ0_rI164p94CxQXnmobY6S2pHbeTTumAERvx6NglNrxxZfkzX0X_9SEcZNEkNYMDhLPp8PZAGhFKptuG0eUzA-5-yC117eViCkbSpmzBj2dKtANcTtMT4_zbZySjRfO8HAxxgoN7G-s3zjtWtceU3DAywTS77S5tTJ8CTKt-rUY6-19j_ks1bOweTLincuADOiFKfVXCtUQyuH82SXxqBbnovy7ew-r4LMHeAyOL8TXL_l_j16E8j2inlwEzXi5DEj2VYN5ZkJ9Lx8ADSiBJj43pxyb5JXL2LqaoedZA_5VytHxJtvKHwydVnUDUvIH50EUxA5gfZLPWJhFxcToIZOCC1n9lDSqSjH5YVbsqZrBj7HpVYNZxEw3e_p6m9VFEscLCFgn_ApQjcsRxZiaRTc_aE2rKUZa6AwN-xzHRdIrm7Y06tEk1p5ZO8WGoWVemmfeTIK5jsVR41xgJ-boY9v37atIaXbBhZ1EBtag0UtCgIWThVNGyuz3FHyYAWW0ZmgjiONWNIqHMTnM6eRdlEFp_-eL7In4qWmI6zpbGToZY-ork-c1FHuelGAU8J2BAb_Z2jiMU7nRYfgkfGb3yAm5aXNCywlG7TFdl_MpAIknoViqGBWK4pwlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=ukDuOdP_Z_CQuEtcgs7kh01UQroIgqF7aINuPSjYUmlIhJTVaRSJ0_rI164p94CxQXnmobY6S2pHbeTTumAERvx6NglNrxxZfkzX0X_9SEcZNEkNYMDhLPp8PZAGhFKptuG0eUzA-5-yC117eViCkbSpmzBj2dKtANcTtMT4_zbZySjRfO8HAxxgoN7G-s3zjtWtceU3DAywTS77S5tTJ8CTKt-rUY6-19j_ks1bOweTLincuADOiFKfVXCtUQyuH82SXxqBbnovy7ew-r4LMHeAyOL8TXL_l_j16E8j2inlwEzXi5DEj2VYN5ZkJ9Lx8ADSiBJj43pxyb5JXL2LqaoedZA_5VytHxJtvKHwydVnUDUvIH50EUxA5gfZLPWJhFxcToIZOCC1n9lDSqSjH5YVbsqZrBj7HpVYNZxEw3e_p6m9VFEscLCFgn_ApQjcsRxZiaRTc_aE2rKUZa6AwN-xzHRdIrm7Y06tEk1p5ZO8WGoWVemmfeTIK5jsVR41xgJ-boY9v37atIaXbBhZ1EBtag0UtCgIWThVNGyuz3FHyYAWW0ZmgjiONWNIqHMTnM6eRdlEFp_-eL7In4qWmI6zpbGToZY-ork-c1FHuelGAU8J2BAb_Z2jiMU7nRYfgkfGb3yAm5aXNCywlG7TFdl_MpAIknoViqGBWK4pwlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWm7IC5BirTYCyc8yAdGxOFdxLw87rN28iC1E9eE1eUPtRlB6zbUmf917j7dNUuu7xq-G8nRblwYrk8DR-cK-Z1l4Rc_s8xlU3dclb63NLo3GkrvIDG_AANcvNCSQBQ5P7kVHpQ0BkoUNmm4_CGzZnP5sKuRugHVMUeGbnZdqMyLHUuLEg0VWW1nTxT8amPxcWl5xXwUAq-1CBcLXcEiZCJPFxSftOgY9-2sh8UDTJ_D2WKehuHzdZiAEp6ElqxhHwtvYJ54_vJZ4MQ7ZAQXrzi1AJejN1Wt0Phq-8PJHbp4TGcFv9PLXl_EZgUX49ugzyQcnVNOB7h7wde_Gc2DRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfHuTj_53SUIObZfGcxvjHGGzhv3KbUC4zF64F40GO4qzkLWvts2EAY3SS1LFFz0X323vJHEy2ri91VhFytw89BWA2Xj1BVv4Qp_q1vhW8GFZp2LMPpc43JEUh9jZXQC10sdDI1A__N59Rmmzin527MbBmkNEnnc_J-Pqf298vTYEleVc_vc2NrQ6q6UhG4bkKkzT9xOkeAPMkH5wlTA16ukOa5HBl8BYAG-a1bHcDZLwz1aAkhboMwhwGb1rbq-G7T0xnQceliI5eoHJNJNby9jDfvJSV54RJy8PwHaF2DJ4O2kBGGYDnkLb6_Ngtcq2M3fFrpa23CzJm3O19YHFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIkMzyD-NI6ARdcljVXECfQx5TXbxNbtXl3W-Z2wF8tUJ0MVWey3GdH9IeBXX-5eCD-z8hDDtfqOCFuQGzVPNM_dw4I9pR657WVkfZCaw8FE0AFk-mYM7r_FJ4CLnIHgDgsEiF8K6PLcbCwWH30JlpdrQkGmNIqSdXKIq9ddv2znfJ3I6bI4xJ17R-bFBaeFfRppBfWvNLcMg__v-mBPBfrP8plie0dcIUIwLDSyLYU0QXGXEuQysmT0pSr6uQ07c6YH03IjUEEDlJEP2LPr96bcRQ3rclRGBb4ada1oBqmwbkjq0eh_DlqRuw94sSccMfNeMr4soZTW4yizbmjGfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iA6w9toYUdpjRi6uvWk0FJnFbtxYlo6UGEiWQhT02i7jIQCsI55AVBoSAm70a1Ap69RRQB_8QThzT7RG_6VOtp4TRBECFb1Qq8aAHZSdxzC5b_FrQMpSTT_dFzOrriElg6VtXaftXiUdVO9LELrTMPqRsFGucV4mZcIv-8ISJ66ikXUQXS61vj9-P561BASnVeh6lPoqylHucmub8MRN_Q_WMsi_zG1wm2HIH_-E3HXEsdE6inGOX8qRck9jIPxve_gQVKZHzS4zvbkkteOWdXvkSaqPGhNDcCO6JT339XsjWeVfWtBspicNqiIcdBTWjcM7A1PZgMDFa0wSLavKtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKLULQGfzOZvT6l-U_E3IPScOrU1xnJTMNC1n-weqd_84XzchK6NsiNUbhBHNblvSKfabAboPJ7_6p8SBN8efchIQzKvp4Xu9U-pRSh8kh1cktDtYtmladS_JIEFKUIatsNeadHqfqee-T97D9BWX-S9iw9Zs2OyAhJUIYDGx8xh1remz9diZVPzCLEL7bDMvJzCaq8TrkDUl-eCjJ8fzgpklUEpD7zuplsrxpVdO7jZTibt5VxvVZfRujIv_9JBk5w8AGcP1ugxweeWYrcUetnyCfCBV1A7sMyxNGUWsp-RCBDW2LyJaB7LQLMlufMI2WREvqAv_Ox9p6XOfMpfXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZ9MidkuAsqtEq4PA9MkLZfCkg3X6r4oEXrZSl8uhSuhTI-DwpDJEUdVFF6KQnjtmdfNX0oG-9CHnBVO-LHYLVA4yMo5w_A3q1frQKkNQp_L2eAZyhrYxrNTBLjIxJBN12E7nZGCm2OFMVFlfHfTY65UjfyMowdg1Cd4iUC5C4UqNggo_nH8Txp966B2QnBTUuIVC0yzyK2crKJ4TsGcfIPSdxQalbdDRdyDIKksGWNO_-O0Hel0WTBLzRXasrmTL1scaIvEiqv9hmJFiAB8RrR8a5BiuxI2aePJ4P8J52ot2IGJuaiwtf8Jusw3120lx3uRHgCVPPrdikNv7M0oRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URO-T8h8mF1Wj7C1uM6bPvYtTszdhgNlzyHwE2MreHcU2W0P2iBSLB6rUMxf9rDDaVij1eFj3f-CIDfHwWf7HwWIKNhVtqT6fE4jNMix5Sf46d-JtJmBi2KvPxBK8ckMGUmMCWI8gc0tzF_9219yZcG8pEJByJVUYpG-u4aXAsiP31LuhVrjQgVG8kbv2gIgBw4N3dlsHlWnPtji8u8Kk8BerKvhmErEtbr3SiZxDVShRnn37sEEg4LEYrFYR8w5wBXfWVA0AHA_0FWDL9lp8hhD1eYhBwKDaLg6opdNaji9FCSYxSLpN_UcLdYYmLMW2AIB4LDW7PNGmlPwVsZ5YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikgXDGPu_ZmmK-WmsxOL-V_bbczb1EBdl6RVOelRuA4dHXe_XK4kGWw6fq9WXBSNmVSVX8GOTyeZBA32BqBzgX29mCRQH_0RxYfvN7I9NEYWc8RdRnH8achDTPuC5UJLSC2tlcEm_bp8jBfJ9FOzDQY2Y4l2S5UO4xKv-XA6h-DRr2BNm4E-BgMZuOwYPkeiNNXsYDZZ3rrE47y-PLbeSTrqmgogBGO0WelvAv-_KlHri2t5IpzmdI5vEEqHzuxm_dV9r4tWlvwNlZIZULwNUi492ox9uV4t4zZXJ70tHSSEGO1nXiwbmKm6y5aoTCQJlsQE6QxCTknflaR1V_O6mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoPx4jnoERxrCObgytovrhcogAS0qVscBVG6Ov1_KhwlMvvcGMij_sv7FsXawDlpFZWb9TnskzpIZ6MqzGoro5zqioX7La-BgRKb-F4fQybmIKeFoa67U5zhHr2MHFpDlzheKnkDM1IwQjBXn34jJmr7xVj4uQHfB6F-6pvvfhry-_OXFgturJQyzr8ANxfx4V7o-mruHxitPbLGV5ERibuyRn8E64WpkOIBzcZcngARc2xVXZMBgqxkotO132QBWFtzSNuVcJHe4C0sgpHHph0X_nDqLCp2wwgcCwieXLA6Ewz4XxWKiVknSZYuwTNkPAU23BiUBCvA7GijGCBAmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y37etZkGGuXZDcjjmc-JgSyI4jPNMtoLkbmMjwhyOp8s10AQ3OeHvpnRdQHv2GkQDdIlYmADZCRoIxa3lPYuIw59cD2bOhwTveTKmCBHHOYkbJ1Sl0mgIUUrcl_r7a8A8i3fH5M7VkUlTizPRisXVCLPMgWkYc-QY0IC46iUGBzVpApKKZzwjFfTjvlY1ylAFhjs1ZribgMnVXI9T3UScS2H_HWrH9ULcc6YYRQBmzo8cJcBvf2Wg6XxPmNUczwoqcHj_HOsrefkTFLnM2_YGIlK7rBxXenRgKLhYfET1uY-h3CyqMPr2pa8UdOgm7MNCpiwGWVotz7dBD5sqAmIPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzlyGS48gR3_pvwdmUKePqKa7DieL1w4LmaiipLUpTu_SgLQj_jqOVv4CIghesUAT3tSLvq7xD-AbAixKcgXJ87blZw3za2OTD5UKni2889uIhL8-99UMmyRPk_pOzRHjDTVk_1UDlhzraQ4JOFqJZKSCtbOfaQ6tg1hfTBAo4tWnSU3kIzkCA2JzPtnljtA08PVosmp5ail9XJkBYH1OxOW9U7DA-l2Tt4TflWtMltEzg2SoeLTMUMQANASzUM54joX1io6vwFRxVDEXSWWHBUpS43UuRmpF9vPpAl3F5ao_vYWsFo3ANgqvJj9F66piEzlryGbr5IIdnxxwvIh_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEHSrf3sMKA7X6Vz8M0-9x7Rh-7HLmWEZ_62rtSwa9pT8FNxh8fIjN6AVAFij1vLfFFiz0t7frk3gM-ZCj25vbmIwhvJcg-DcNFFZmUlCrvw4nR0LOSxfM7zJKRU1McWCjQBI-qGUS_j6UQGPLPCgDtneNZB6F63nSZ3O_AsQ_vX1700-5mn-DtmAvMjK1PIXz7eU9EsxaWWLGm435U9NzgyVlw77RCV4qyvUS5Fm2fEoTBf5p1LhMs0L56xkTpOBsKKeN8QFyBeszw6aYhtxG7gPXNHtEmLoH9948ZfdpvMKZ1ya5oF4E1Gs4YrF9li_BqkOOwI4_MDwEXKsDHC0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClRcGjd6MbOdz3n3QHkZHRw9TYHa1hc67nWTnljlP7SzsQdWZFDFdZdrOrAXh7zobBUTwgOmBGmZrsWSka4jeaslM_TExeKnX22pRqJk4tihgLwcpU43bAe3Tpiuu9Ue9mWrBIcQhZwDqrAAAO75FFsuqId6MNPbjOjA5CvV0BS_c7CJQGnXRDD1NFYeQfSXeRrtVDwA8bsvCHreq0IGFFc2x0fysBG7_Iu-o51bQvlmYS36wxibWzxnuMNvQuARCdkH72vH3FZt-Jv-dAGyJm1fY5_MJnS-m7PtElgA-NxGT9qSfRz-QrY2Uqn7vJ9abeBjZG3VGR-3drIzY3itUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fd7uwHnepUyjQjJlSNX7noDucHlT-TkYl16nQs0gOSWILdtt2ZkBCZiIj3bVhp4vr4eO6s3sb_UsxQ5Hrup3vIJUfmgLdXZYgJ19PE5vtkLXLQ0ZdTfmVotTvfI9HKs-SojN7tYAFrtGjbmg_3iPHwpLlxLVrEo6jc6-1iFYsPW7Ca75zjhAHSkNUlM0_xS1IfhXVShdopMzk7x-jhObTLCgl3pEuF3OeN8xXCpVnLdCznnZazZNSvRXZznzZLi1N8Q2WPvvL18mN7uVUD2PzOlriIP2CQ6Eb8AD7mt8h4cpImxmVokBFqP_l3CRVcEHHMvAW2At6nG7aSK7R3GKZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4ock7CxK_WeeJ09nY5KPGOiLHC3fbaWbq5anpH6Rq4-rE5_H9vCcQilt6-jr6q-Dke8f8UFSoREiGJiur2X165RSJZsrKqmeoIo4hHRH7W6Tpt9HjnTAb4D9wAGCX2HLpjhDYIJK3dCNviF-L1EKCFc6hXGX7QVs7t4YdnGbJhmKyWBVdz4K_zU1FPYhWr_yZWqpZ0IHULgWKsWqzsknOqy6Af5ObaCRD10yYIYDsmMHHse2fIn3kSsDtF_BWCa51qTeQXOqs7suW8KoOdJoHjSBk087uNS5Y_oe3-wZgOprM2fq0pty0D0pKWBZKv9VDkLAA6irMRF8azaCx9KIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2yrzKTt6Fk3jrJxXL0BvuNPEwyvW25o28WxwyElDC-ps7P1dUPZpcXK7TE4ceaZqDdIhOEe5j4KRibGJi5-cZDS3laiPquXWGL5sNIstMiRemGO9fe-Fc61Ms8Llw2zEOkkg-yNt4U9mk9ncoLYGNjSTfXH2hPZihN_TbMb5v2QgJf7hmIv6DyHoQoPjaWIHdxRsJ2I1WA7c4AU4ezyd-V5Yb4VJ38DP9f3oEWAv0_E0PnOu76tRCx8YtjPz6_EkRrqBTJosDko0xmnb-L8Ia3TW5HprFnlBLSGlYx-cjfPYcofQPyJUivMz98rtmjtOdXA_MqsNmiF8jR_lP4mYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iA2qKf5lO_YSYJmfhpBDNtiZPtPK-FukgrspsJMvTOisFITutDjdBIRRI2A4F6_zVFMCHsD_1PkGQakRQxwYdi4UohjLiLsYHUkYsaiOX2e-Z0nByLWdWaTOfU2k5slSzwBkpJNHHuvmz28fxPxhxzYxY8i4VJVqkNxSsN1vsPDCs3bUyl7h7M0gR9v-MkyI-yKYMF8Q7SL-0n3lHcIqHlpL1_WEZwkAWVdPZM6LX48n8nwKH2pkxrwgg9sYyTyohAUIpRAYWJBhTZwgr8z8H7CHcXeAB-zVnKHFE9m24r86KvYTsxIS_IesjvcEePgRBOL3xLLYbrzelgsbv4-5yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EsJUP1GHjkT1neJ1gwIGClraYpEj6MX-JfDYdGkiB2pxSldDqNY9cBGd52m2-MogzeDGdYLk3Z0FbA1J96Rn5N9_Wp_FWnDSxmqB66s0VNcZuv8oMl-W_Uyv6tJBOnmR_XcDTWCqontkvq_9xDx3yNM-NKSofyNEnnfGkBwxT1qj7WeFJ_UwQRqL7cN0sxMphZ-5I2AN5H8lH30UqrvsPKL7pkT4pM92ZJZxqP-mTR3X_6qKiJcpUAtjnfLukGa54HSlYzt2mv_4VPYrG5MZHPRP557PrWMfUzyo6mzxL42L19j9PosUglgx6-16wcsxbqoHnfe3rzfnb0LtorNlMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdRpbLuqlqNxB4h2BSoDoVcDMcEA9SwMxoobmsfhEypOv_yz4NQNhFmW2oNYdTf6I8DAkVkG7FTotDq8hQxXL0OzcrhJfxtT7uP4D4ructbJKcG2l0gP5HGA8vRQQpAb3ZTwV26dZ0JFqYRvpB6RQRCnyaP1XtCybVT45h2O9_8TYIOyTyV_x54i4u_jFXZAj1LIvh6pPor1c45q9ercj1j-zqQ0qV-SWpzswhJC-SWSC_ZTAK_dsUOTKfncLcb3TAcz6k3rjZSrExWiyAC_MIFc0ulszh20OmJVBa2jEtK9fmWWX0fCXZuD8pKToxx4_7gd8HkqMQgnIZ-fvwhFxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHzkwbLlg3n71OROJD7Gfc141JeizfAGIf7gEl5yNCvTESS8EHqHnbXRPokFoKPH0fNYIZDYlJeSTLz5hEmMzAmuBBCaIYkm2O4V4VPBXxWgwC0ZswLFy_GDK7CqXCq0uooUOhs0bEZjJCkRrMnCMMQHMqZMyrvzHkx7Txup6TTv3mkSPQ-tFLh5zSy86X0jFFXU_1yC_L4Guj6c-wvoW1F74zbPKAmwIpEjQhhWT3wvRLqk-cOQ6JwzKKtBJhU27-kk16vDxz73rVq8CGg1FPGmiGX_I0jdIedpf7qwOiuuKvUMuEMWtr_UpOcfriKIxyGCcCB6tCDYCJ9sC3nLuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxlE6rEcjYmkU5Y_JLw_zFay0q7gojNfpSd2FkQyMmItUBE4LOJmlH0A5WB7qwGTB2RQiTFGHrrQ3aGwNTw9IqVuu7xuf-h_cn1Dw-PXk1NLXUdPyNk3EexJaKJ_vi0gbH_huZZs9S9hlgYGw1N8ov5_I_rGcRatWEveh2NjVd42nCGskrjruXARoiEsOpfDmj1JDM8WvERLsucvgXS-jYPBqdYARvHbrK9pwdYdqrh23UGdU8_Ne8l5IxyW4N91GjMnGjD1djxsX46PMSGkjUfX1m-l0z76KXiXkJCR1hSJF0Ff1QeN3PWAd3qQsKKU9qRp5S3AxGxL5oknO8nzVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/af21PdqOC33e5JRC9E1CfrAezkJ4Jf2b74zRfhuXY-Z-MdiK0_VuM_gLo2YP3LHPD_r0QznQNXOiP1ywDrzdns3vC3fyJ3YxQ177NHInRei2Rct12HltXLV5nu-xajnrnytojY-jOhjtiTqmFZojjgyHzrfW9YNsa7lVWI2olPnww1E0LI-xzabRqvA2hkNKljMnI9eniDIxK2FaebmC6EmAY7MhiqrFYfEzKNuL_B8_65Y9oBpTGLQbAleqSzRTdDyuzfg0zBDNlYx9Aa6MzXNFdNO6-pBMnhjw5oKWY40OudLoddiVlHZCaRCjz2XdPuG7-ozAMJqQP9rr_MJJkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbHOQTKNVm4J8XLPRPf_K9Lq5gYgNJQZDbwwcH_zsu_g5twe4CLxZ5CghInAC8AtlMSfiRZuFZk06-nPLFkRJB3n61adZbNBzl8_XhJ4vxGOifqitGCULmO3mRQC1p08rGFA5mkTOYjWgJa6elb88bBmbvD-bkOKmOOqd0mGcREzQlooOGwxtU5xwGoR2-MZQx2OwnkUqnJR6lDyixcm8_8AjJBWB6eS6Loz94U39HiE05SEDizpE02ZgiNLGRMzN1A8-PAZH6VygtiMeLLDz5jCbAehf5SI3QZhCwkQg9AXDcwpgzb2IrfFa79FcGZWHDRJNAV-yRJvl8f8FivmTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clXM12-ZHV6ldp698HdyNVx5w2KdzqJfEKeYVokra8fCgRrhp_Fffmmk--HDyPUcA-NEFOE7Dce_y9bdoRdrYBN767xBv8TTfjIu1QsTfMgcooKbS-6LQ3gr3syNM06sW8eMl6_4X_CaiMeS3qqUxNViNzFrzzBFQ2MnVymjjMwEU68Rsm2glfNDgUY2NwzHR9KJuOV1JaHi5O63L5wGWT-kiTiS1aGq47uXL0b0nBAEP0q_BnlIuvxPsztNpWtkRdobOjkkkW6QS9hrebp1Yhj6aEHN5fbVxpDBWM0gVnXVdr3Cx7RmHtpkyh-ZwYwdFL5b1EgIhsBVgYLdsCAi2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrHCWmcoRzLdYtcF13VbAyEjkqykDvZaDo--LECcvALfLVm5BzwxNUcCbbtKSN6AZF9D_H6jozX_WgNmxOY2cpIRWveErkZ1Tf7VeOKf1aHC3XeSX4pgLfVK7me494re2BTt44_AarTyEPit9WWMJDgSBgKZbBDVvpKpofdgIWOC2lKOgMNlZag8uuL2h7i-8onUscd06BuSaQuu9-c0EkdEa605E4TDKJIlVVzPkmW4xdZnIfyR2AwyAP3X0A0VK_Y-QxRGXRu9S6EcbeNvsf2JVeHIWcWPbVjV7MI4xrnCn6ttfxypxSp7R9d78AzZo_rOlhPh0QCGdUEDu6k4mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-PNqReFvPn6bhC2lId343uoJp6-1eUlApQjO5nN7c6MNcfxrQJoCMjVnrOnw3fygLwzD9ikMzJ7HU3TfHVpurWCSVSYQXlY6JbvwNRDUdopYuERH2_DIY18EClh0l2oNRnxyhX6mG7zQsKvc2aA8Zqigy-cX6Ra_eFipLydRPaij3QYzKJ3Ibd5Mt5GiFvY0HyOZFZ2dc0jS58wniiSUL39FZL7cwwH9fPJFy1NafU-W5K6yU_o19rYl6JVr6hvvBZNijWvEp1MUBXrdY-YoCq2vEfSGIqUCo8tyfXi6vou_X2YFYKCgnLa1w4jMdHZ-d48EtofvjeajuDLeWxbtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1T6jUMnsj6bMie5o0jWMw6-GCWRC1s4NYMPVKZprs0uYIw2K105fDKETwhnL9zhNKqD2yDXLlvoOeXdvJx_w2Un5ogDtfSBWSY2T4srId2ft-Q7sE-h7OPq8N95MK6zxEs7kDcQGa2RhWkEdzcxyqt8NM3ecnRtaDxWtx8ba92k8BzGsObPxv__rsK_fZPsOIiFmWWhd164cKMwqGEFGtvJGMBg_hRNRJqyj6qMvvkN50eVcvKz8VDjWAnxgQw7xmdq429hkr87NFp0_2Uy1dEqnuwppgmCGXtjZTK2weCZAB6ZSIK8UgSlJx_7BWdXO0lhu02ABg6AcxzqQYo9yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JI4PLqTfWlO0B86rRj9AE5xVekriwVoMZwL0sB0SOzPlXtB-1RRP_9uEV7dxUIcUT5oiQlZskAXfKI57kE-zssb22L4tNw_ac-s3GYXdffaNvVTh28lH-iiSSw3maWiZGHkJKc0fymhmlLbaUUWIjswfpLeqZkaHuhNdOgw9qegf-5IKqREOYx_cluHiVBsf1WTy3KraF36WevUCSKsgI0FLGZlDrmPWjq0WA4Lb3Ia_aSt2DRS5hQI23nX9hJIVhYJe6GvRaszfQeh8ZSlY7jcPQSuIUzIpKTmmGkcTAReLXqFp6lSHsliiHTsMIPoZN06-TCqvQOLxIq7O8RYXnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OrEHduyeAb8N_B8ULtP__uyQySaJm_g5ktL95ogrpZP8Ky9AIwBRFf6S6rmU2V3TVo-rU-FMopWw8Kzi_lqoJXe0O4rD8LYYCIRCdQhO_VIr7bIzLhvxxiPkefWJ-hIy4ndEcbziLpYOGNcdG5GHBvzcM_PpJgl4qd-rc59JsTm4nGtyXlzaoxtQIJ_4KPGcRqFGGpiI2738TrGZh0VWblnIbZk5svk3GuVzlsCHjGHniOp_99zFYCEwKZaLsnlXRojn6cv9FOkC2mFvmyEGQRuyass-gVxX7TOXRMIG4piiyxaWGGjDi51Hc_yeivfFyr-Los_elluSjh3VOxuHmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4ogfs0bERxhZMz2K0c1vNrELFkrAAE0eqg_fuP9-O2kCKxnbGBOE-uNgPqEZiZYoaesZ4nbcDshwKw2xtoxF5YeERkawWYv0ib2FHbUAr8JmQStR0-AhiirKkdzCKA7Do0GgOBeUtBu56Wntxje9UwIlztlULcmrjwRmA8bQ_TGfylgLEsM0AnlGOoGe1sZ6WHB6W1b13n3ijFK740LwFV9X1-WXy57-7diqEXtfVPxPdwz6Q6iviq_1LXnlwuqjTyMI0fxkKb1MTcLao9EpNXYwkhRQQ1iLkK3KVPtregh7Im1Ig5spbIvEk54507hZnXMS7MhmX5QsMWU87YaYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9Ab-nlTDG0rUKyz9miJ6MFiw7_erN8KRbcOkEjlUdf7BSrKY6cxeWuVv0RcHMvgDF8-MDHIJrm_6GdnxI6rOxmT-DABIHz7u9kUjUmhn3x6yAHth4LB_ZzoKWdbg91UcQ3GoYRN1j7Scg8rd7lL0JQntJIrvRSX6_rvLRufYfW5wYSJk5Z4jk0meVdiCir14SpoPz-kp6GqvzCRcoKcZyk4ty7Uyas6lw2dFMJGmFg-XRVwAvKwi7NrFx98Cl0FMC5tIL_0CrKqVEptcHjzsiIwQQdUiOGmh0w2Hv_AL1eb9Q-R2SnMN3RBfax0RVzIG_DlxJewBrPSRIPqFNe1EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7reYNACqsL_jQYAVwA12gCdM1KKtelx4x0y7Lz0Zuu9XV2gz3f8SxfmRym_Q_Gqk1AOT5QnJTpqFUKoi5_O_CEIN-VbC77Imc0UBT32RGLDe2Oqg5gL3fJhiQ9Tedpt7nC9QXgFvPUHemCWLFyd8hvX8xoWKlxo4HXiB2OPxh3e7rGYX3Zik5tgAG_apzCGqflg62nOjGin2xf_Ikq0Z_coc-1H8yVew-iohDHLDy4IY9Z1sIDNpqJdLZfMWXYFIgjwnXjIu0-IJ6tjup3nbUq_zi1dM_a3MYXbpKqIMRO8tZ8ZFTlnFk2mci2sUSVDCTy68DYhqjhWMfigjzDM2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1OtSVs1aVdmAQGKJgvx66Qc35OjDWgSh-10ySDNHBhuUtwYcjWAmtdvqGO1kAz1zbb6NDiQecL9ejahYdlBMt1XTm-Uc2OQcOGZ_4HXvm608kgHngofOypPpjZjvdECvAHNfV0C6-nhqYjVSs22_8HdJHaOcE3NnVJrpAFfw_lzSyTBLMqy10jBLGWg0BiPNWwZXft8MBH96OwgZrel6ZjTbhf3RRzLJvNfkfgaMFafUAP837T4qwjPm7g1e8oPCrXBFqUow38ptWOecNQFzZ39KMsHjqZ0UnXOTSx2M7-TOVXEporbfuhW_8I99WRI7JZVbSaDto36uac2aPFUkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggpsrq6EJWKaie38ObC1TalwGyUcIpMtg7lopky4_LCMO0FVPy4VTK3HKImyVwU2TtfgllOqsKSTAEB23p6CwTmijb0xlSJgS3dZseVWkOYAfu8lWrRB-3RIBRQ5Ub9DMyk6HlptQwEavt_MqZ0Zobzmmc2oQQaQEGLyZDdvUZySwamSmzbZQJIJc18ypzgZp4ocr3pchJ1EUId6Q5kSiPHaYonazv8amOmPDcLGy5ExPxkWBGIad40-qhGeDnLa8XFXzv20qQEM2tpkWUtMyCTWpbZUkNZX11WLQp5VXJRwODd-SmvGjRYIIoYzPVzbAL-4B9qgDgWTP-NSi4u7Hw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=LckB4aqufr6N5FCWHh1k5F7MWk6B-rf1iw1wXaLyPgKEP931ZyoyxPQEMdoJIFMKesW6sGe-mMS42bhklAiRzvLnLUFFYfo6ugTttsFYU3R6wc7xfKhW6VVzpOrT7bC2_B8zAS61yUZmhR4VLO2BE_kruBiZGzUkuvJJ7TOWhWiRg8Qee-J7wkg0fuo7u8aobOsjEd0bQKpJrG8548hb_e7SHfNtA-5ILRLI301veNzxrFxX-66JLrFbyycZZmmF3cvCymu_AjZaWXzhkkNBN9tiLgl2vL1CQSm4K5sq1U8wD96o3V0y8XuOTmuGlYldImFujSTrSrwhUpDmmWvFDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=LckB4aqufr6N5FCWHh1k5F7MWk6B-rf1iw1wXaLyPgKEP931ZyoyxPQEMdoJIFMKesW6sGe-mMS42bhklAiRzvLnLUFFYfo6ugTttsFYU3R6wc7xfKhW6VVzpOrT7bC2_B8zAS61yUZmhR4VLO2BE_kruBiZGzUkuvJJ7TOWhWiRg8Qee-J7wkg0fuo7u8aobOsjEd0bQKpJrG8548hb_e7SHfNtA-5ILRLI301veNzxrFxX-66JLrFbyycZZmmF3cvCymu_AjZaWXzhkkNBN9tiLgl2vL1CQSm4K5sq1U8wD96o3V0y8XuOTmuGlYldImFujSTrSrwhUpDmmWvFDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUQf2IP3oWJ7pbw48ndeY40_V0VFcPSXnNYXdo_8k29zvcYtiYcI26LCvBUbx7bJvkJ9asY6IqHTo3u8Y46XkYc1giHCisgvKY38MnkLP9s0pT5Mwhx6YUUDa3EZ3qdHSEEIY-V8nm77dbemrncfT_NWXCY98dqdn07CXYWlin5PeH3E16Fsltmt5URixT3OvaZJfrmaA6spyfPUvRuZ83pNMBBQQzE5EuwQgzlx_X4v67wSHpUByRlO-CkutXMVjSAjvVQ6s1IzqE_C1d-P-dPiuiNy2C6_9E8thrmqoPQkYegjEaQMA601_GGXYBIHsCC_W3r2tu9j1WjtKiDbpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آیا به بردگی گرفتن زنان و فروش اونها و یا ازدواج سریع با اونها اگه شوهر داشتن مشکلی داشت؟  نه! چون خود آیه ۲۴ سوره نسا صریحا اینو میگه!  وقتی هم قرآن بگه  هیچ آخوندی چه شیعه چه سنی نمی‌تونه مخالفت کنه!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6584" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=sBpEmWf3yEjUV55ywVekfgZT93L-wNhGu5tJmz3BUIAmXDke5Q20EydthFNS7rSMloqbHgU_YA7HZVjS97VG8VD5ZfXGnWB0vmMrrS6Z5X4pnT8h9-lo9XvaQ5LcAPMdUaoY0TLawt6KQjLwmuziP259_Emn7KaI5qc1TrGoNrwjr5Pxuvacf9OOOPZhWiTqPXRqqE1elK_rbyGP1OrBrAPmP9sUJy4Awfvniht9jEPLG7-jBRyldJcWavt-yBE9yhcV0Tc4zpYijP8FI0ybWpFaIWWk7f4dSOVNa7YRHd4mO_wA_3qG8IRoOWgJR0FB379jOleBfBxPjAXiDQKSSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=sBpEmWf3yEjUV55ywVekfgZT93L-wNhGu5tJmz3BUIAmXDke5Q20EydthFNS7rSMloqbHgU_YA7HZVjS97VG8VD5ZfXGnWB0vmMrrS6Z5X4pnT8h9-lo9XvaQ5LcAPMdUaoY0TLawt6KQjLwmuziP259_Emn7KaI5qc1TrGoNrwjr5Pxuvacf9OOOPZhWiTqPXRqqE1elK_rbyGP1OrBrAPmP9sUJy4Awfvniht9jEPLG7-jBRyldJcWavt-yBE9yhcV0Tc4zpYijP8FI0ybWpFaIWWk7f4dSOVNa7YRHd4mO_wA_3qG8IRoOWgJR0FB379jOleBfBxPjAXiDQKSSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-QPpBAm9J8Jq-902yWe4LTK4wNK1wjDQM9l1kIlijht_Tiqlj2KZwWpnA7Y1BuANOubk_jCyoZbfKXJ4i1nHBRZsHYYALJyeluKCKIvM-px7VqCk5YVOLff6ThxgkOPUHAOLnQKszQqFNyhbOI4yimtQIbbCbgMGvrzeF46Yd9jHImBmqF9yZm86dbl70O7gTbjblcqDFPsdbuuPfaMuHes6EMPlr8dq7yUqw3q95X2kV6NGDn8sWDmPkTQki0X4WlrVguuzHmHtYW65qL0Q5TaN5z1YRew2rHuveRvY_PcusiIgOl0Is-dNDKM4xg8OH9yfzbzOHndCVnUpLQSNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdTAIDsS-ODn0zHqaz8eY10-ZhPVPKHD_gJCn_lYYioj4Na0gL_X3ZgwHutkRPJ6tr8jVQBqakiKR6s2bJjhdLiA04ygz9zH3RSHq0D3eQI46qUo9Kf86cAHOmh0yRdUUA8hixRkSSpNObTc2bJwx45jONC-ShuyZvh6it_SwoUtl8dPUIuOLTGt0V9dQ-72XZ6_eNsYzd2IS7kbmWjNnjfm6_nchg9BRBOJarR_-BClDlQr-QYFaKb2QDlWkjrD04KQJwwMIPGyBIN_UslP32CG8fVzjyKcIh9eWFbDCF1RGAUOUgZvi3DVDNZyBOlzjejeIN15qnp9V8EiYjREng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=QHM2xiUKu5WebeOGAiZJiyKT2pW0kwXy3AqES1-n5D4C_vybwsMg74dndhvyokkG6BI9caM4BzaUktaEeegCqseqGD60GUsRhLY0XBfCZ9nBxR8EiwGQ5Oy2N9cei2zi8Jcd9zVYy7LWaVqK9v91jOT3V7h24Wid5qDHFjOEgp56yAsBvGZTNCPZLo_hubJ_GrMB7bpHmq3rH8VUi_GvZ035HaqJjBFLFjZZ7lr3CvqDbDpsKBEDeKxDz2ESHPDBjvuLjf1sJnMhPqVWcZbdWo5oJuP2Pe4ZsPjjbB_LB0cOnbCRmscXDNfgC2yGAkvb5epP8jTEaWkqGyHFRpSLLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=QHM2xiUKu5WebeOGAiZJiyKT2pW0kwXy3AqES1-n5D4C_vybwsMg74dndhvyokkG6BI9caM4BzaUktaEeegCqseqGD60GUsRhLY0XBfCZ9nBxR8EiwGQ5Oy2N9cei2zi8Jcd9zVYy7LWaVqK9v91jOT3V7h24Wid5qDHFjOEgp56yAsBvGZTNCPZLo_hubJ_GrMB7bpHmq3rH8VUi_GvZ035HaqJjBFLFjZZ7lr3CvqDbDpsKBEDeKxDz2ESHPDBjvuLjf1sJnMhPqVWcZbdWo5oJuP2Pe4ZsPjjbB_LB0cOnbCRmscXDNfgC2yGAkvb5epP8jTEaWkqGyHFRpSLLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lb3vmcgA41RuUjvNRJrxXpG6S9j2yZBOfYh4BUrL511or1cNe_WaIjJHjhVLC9bcMXfacEbhCYDB0VgHeDlUqlCNWfoAJ0mYZctle52sOrBcUUMlR4jZTrpeSPvoYkPiLoAnqoI9IkDkBUZepmtbFa-tjvjyDOvrtWNuCHs_IkPXF5aOWUW4X_2nZ5wU6g9703leTHIzX_Yd-rM9W8ahMOP08dIDSP7i5qM6ctbbDcVQ71lAagX-0dQWldjB1gJRuoxJdIrfkSOjHUuRb96VSPiDfCy5FClfGBGlZbz1mu8NsL1Z0IoCHrU57bqHv4fxMaU5ArmaGzU8_waceSmXCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwdaKeThCuyVZyIeQ9vFHcMfNu07z6_OBO1Ty01NVjCuWyVCnjxpjE1xgQ7ULl5U0OogtGNHz1fmWVowi-VINmW4t8A1ILF7NbNfQB0Uhy43jIb-20c3ip8fiicS6w68D5vk4C8hpZ1ULeFyQbfrRf2BohEgw1GXn2YjHkTa5oXvUmodk61VzE1I0FBWZsALwZnSi8N-jfPJY6IgKYaHXEEpnlWND23zkJFOUV3mWtxCZhyOEG64FE52Pvdnv3DkgnQhhDlqQUkHec0Ju5BsUlICL2g3WcA2XYVugkMgu6AC_An7-F2rUHXubmDLfdf7gzH8P5cNAE92F8tmkkvjkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIPLmH4TbW0OzdHqWokTC9J17yDzibN-Kpf4aV14iAAG0v4LjHGtHi2gTJOSaN6S4DylqNFjX8pM7e8A4Zt5kkGTD1KdcB7gqx85a5rNhJZ82Y0IsofPoTcy7yLl5OciCtipoPZhJRn0jB9cXcOrs93T9idQ34uamd5IVVA6YGePDx95-8xHOFnxnuNmcrE4UvO0lrlJd7EgOzJKCtXN-OEZq1Pd3Xd9FScWOLofUsBrKdw8ldh866UwyDCkVtX1zew4aYWPfpvidL2SCCDL8biiY5C91p8L746EagV6_n2s-8rTNzbKCRdSW3cS1_1MqhSoj8lRjjS0_0JlyH4Zzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=tlK8GR-aMUyCnRGXfQrZsJGsRwFO5EY5RRd59VE2KEnSiaZTINVGHNX92IiNARSF61jw_EcmLB1fopHmabIeTqMo3LWSHY6Kgq1Z5J0mXEtR0bZTzLZNRLmM_6NaJ_XnzzKRXJCvjW8WDOfY0zAAfDZvUCZFNsFgBDSdoFlp5Adss7PCSPYufjct9GIIabVq36aTPM2IvTgNrot8znFsS9LNcIWz1o0RnmzdnnPjE8rXL3efnprii1mcpCWnYh0TtaGVnsfp2rNafqfF9v2XsaxwonlcLietlI8BbMI534lrJczUON0nYxcn6DLm0RPtV8ca9ElEsqIVAS0pENSd3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=tlK8GR-aMUyCnRGXfQrZsJGsRwFO5EY5RRd59VE2KEnSiaZTINVGHNX92IiNARSF61jw_EcmLB1fopHmabIeTqMo3LWSHY6Kgq1Z5J0mXEtR0bZTzLZNRLmM_6NaJ_XnzzKRXJCvjW8WDOfY0zAAfDZvUCZFNsFgBDSdoFlp5Adss7PCSPYufjct9GIIabVq36aTPM2IvTgNrot8znFsS9LNcIWz1o0RnmzdnnPjE8rXL3efnprii1mcpCWnYh0TtaGVnsfp2rNafqfF9v2XsaxwonlcLietlI8BbMI534lrJczUON0nYxcn6DLm0RPtV8ca9ElEsqIVAS0pENSd3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=hasqsiQODo1C0lk5I3tqKJ8ydl5jlaL6gp82EccL2jRi9bdW69mibykXPMaPQGNSZYCwTH9fXh1V2drbEfo1_5-P7XY8vfyPNgrCCFa7j0ze9O_DvpFTlll8tWJeo6ycthD9lJG---Wl1nesQcHV-SzCQ8UmQXvGURTgRX4h81mLJFXDFQ96p1jGRp06cIs_HD9b1zorWq1zPNz1LhwbZeNwiLA48S8Rk16UhjLi8YtqTkIt3kgvDXUGRaoAf9mYokZXU8f42ZAPTCo0IhAIUl-E14uQDEEpn1EPg3bC4rTjl8oAtffO0i5O3eBFYhBEGQb3kRqcLQDC9SN-pYNvxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=hasqsiQODo1C0lk5I3tqKJ8ydl5jlaL6gp82EccL2jRi9bdW69mibykXPMaPQGNSZYCwTH9fXh1V2drbEfo1_5-P7XY8vfyPNgrCCFa7j0ze9O_DvpFTlll8tWJeo6ycthD9lJG---Wl1nesQcHV-SzCQ8UmQXvGURTgRX4h81mLJFXDFQ96p1jGRp06cIs_HD9b1zorWq1zPNz1LhwbZeNwiLA48S8Rk16UhjLi8YtqTkIt3kgvDXUGRaoAf9mYokZXU8f42ZAPTCo0IhAIUl-E14uQDEEpn1EPg3bC4rTjl8oAtffO0i5O3eBFYhBEGQb3kRqcLQDC9SN-pYNvxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0zuUb-6t1C8BRU-a4oq85ZlFyiqiHxd1c_PBPqOU8au-9s3ZGY7OO8gDN6FSO2RMlGq2VpLy9ht5cOFyKsueYhJapK58jhpPYDxQ7ezNVyoBX7588K4-5gu-r3_GYXwGEQGsNecAvN_r1FmkTVopBGg6E2wYM5HcFZ3-q4TYc2NS-Lip2h2-UbwCaWgGb8WtD5JT_r1L0rlxM8LPz_66lzLkaQsHCKJEAZpfZTRvLgFY3RlQGN5GrNjExfepNeBSsU3FjeyqFuHDKW_C0qKyz5vR_MzThstsxBW4mNpxuCbYYWgKRl-tKOlxUnaZ9x8choTTXI2YBLwbbpEb6fw0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USkcnnY3XfbSi1l_guNxwSb9H2ORoCmm2WSphSTBFgpeylymP7cxKzMDykEko4aJ8LPLUn0Rt2qqxInvWB5RHVcneOTP2JXpFseSkmGWI2T2r3Uo_ffZ96rwGWVbL_GKNqPx_7-Em9U9tZFPWjb86HO_-IS6bxznWF9DwLAAyPv0VYjIpixcPZ5g_yjCFHbVyQn6zlEUnQvUjxurClm_K0IHEMOuAmzNIDqBnWRatL3xQ_QfCGVbdigN6YysdxbpBPkrCt09qUUQo-rlkso69na98UezjQu0VnKydp2jmlcDJICqg5lCNUEfLGd2tIy0OwuERRQiihMcUfEkS3MsUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nfh2K8NLuzcRBdNFJgiMYGHdNT7JAZ0dp0JYBvsaoz7mryGl6U5BdKjW192rcqXnPKmvQdM-M35xwXVhD10vzcapMFNrBkHgrTj_1b1gZScGX2DovtOyb-guwK_eLOLYbbrHrojgsWQlQB-rYHYlivoLUzOGup0OeQdRxRQKavcwgINtJOBaCrqaVhgkN-TAJSzlLjXQ93xrvNTNnB2DlQPPc7aO8Y6y3qkjWca_f9PsRlTfWsZhjlkKfm6W-Pj3XmDA1FWe_Z3QWqYFhBSKCREpGRkm9JiaWAwa8qup3_w3DyO6tFplHlQ71o-keCSQolc_5GjL_3SyNhZWlZk6fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o07HvPgEBBc3-VmI5I0HmMS4QCuT9leg8Wwth-moUFQOgttH1Ifrhuama0BMqniwVjivWnpeLlsn5hE-bEw7Q0seaJp5aOs0ff4I0p5W4qQrnBaZpLgci8RcT8gLLa0fC92YSOeLpJR5K9JTQdcBSmZstjsB-865K43OAIAd6vtlfl28zN3gW2NeKN37Kfng7u1b649kbUvKIETVKOXZfcjcVH_O3DTAAi6SpoVzjlIKFRJvS6sg6VHzufyZcuiK5YCLBmCwvBWgSt-krOnUliwc0jQ79IkmP6TqZXtSt_vWrgAHegNKfXd981cSkV3RNGLwVu_wx-IE1qt9L2KoUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6WkJbgfgNoQ7lGu0KKxiyWbj6sxHHqeNGJAcj-bYdt5qn4-0Ch-AdcM42N7sX_SzzZabRUWprweb3TVfiLNTaSpcBjvvlpSBLmTgC1gTqFjzPZJZ-hHZNigsZnaW1EjkaQ6ljoQ3uayHvnEYNDZY4irhE_z3I9FW641HLBBCsNNecCqzsAdH47KeYyv0qzHYU009DU4HB7njstEkiSJtHxiXz9xcESVeRGVcYA7OVxIKtT0ySoi8aAXJoQO3Q-NBKY-jSXS730f7I0Ld-GflPaAYCL6KZP6-3aQVueVMcaHZ-5xg2ppucPheWTHnA940cSgGN9ffjZGluOYO5qvZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sC-e-BjT4BgsQ19igRe42oMgqMHA_zph0Vd6IYJ6VCxSfQfy6LUvrasDknCF-tp4OSv0OonT-uv-ckXreWy7inYhKy7Am5lAjP3SwpTWpDlYMJvhei6PlqkYCm0NOI2wfJTTjC4RygWjhK04LBlyBRfWKCJFTkekLsYoq3wze7OCTiM_KHYplfP3OjgDZCHlLiK9v11gRnjdKKoa0SD7Xgf2EVGgZcQGTeqngO89xGea5Jvj6hm_VkS_Ym8xcbvWPr8jJDm-brACLWrTX2tq0batOALOKZBUH_JajNjc1ITDKXrkzSG7VUJkyp0X5EzdGDQUpNfKQk6UAiKwdeFqug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر سیاست‌های این افراد،  از جمله این زن و شوهر،  کل کشور و جامعه ایران درگیر یک بحران  عظیم شد، آنها از رانت‌های بزرگ حکومتی  برخوردار شدند!  سید محمد هاشمی، وارد کار و کسب شد!  از واردات قطعات سلاح برای وزارت دفاع تا واردات چوب ! از جمله پول…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6569" target="_blank">📅 10:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">معصومه ابتکار و همسرش «سید محمد هاشمی»  که او هم در تیم گروگانگیرها بود،  در همین ایام گروگانگیری، با هم آشنا  میشن و باهم ازدواج میکنن.  سید محمد هاشمی خودش فرزند یک آیت‌الله است!  گروگانگیری ۴۴۴ روزه موجب آغاز خصومت شدید آمریکا علیه ایران و آغاز تحریم‌ها…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6568" target="_blank">📅 09:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ba2r5Ax1TT5v7a1kAjllMCYVur3MxZT8XmeriCvbXI0KJQpwJD3-gLDs-jCDzUptoaAJnkRhjN0redqItHQT4I9JunvC7MaKvmXBUTe3mI_SRhShwd1ytg5JxLVJSEukml4bO_gsXR4sxex7ClqYR_OT0gvLhrfh-b7xD5b12N70wDnPiReblz7wcykn_WQw8kdTZeQsWe66W9kozpF9RgZfFlGtx9DHj2O767jEwfIy6xwps-4nwTAKsnQQUvkMNvkDipYgoZVAvtaSrMXP79R-XI_Z6JNJ3nLC_Ucq1xUQZ3WPMv6wKFSXYwcylxLiJkE_4BcVgarq3vF5G_7SjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم در این نامه به مقامات آمریکایی نوشته  کارهای «معصومه ابتکار» ربطی به ما نداره!  ۴۷ سال پیش بوده و…..!  توی این ویدئو که خود مریم گرفته ولی، خودش دست به یک مقایسه میزنه، میگه بقیه پرچم آمریکا رو زدن ولی ما پرچم امام‌حسین رو!  در واقع عروس خانم خواسته انتخاب…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6567" target="_blank">📅 09:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6566" target="_blank">📅 09:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=fpa1mhQSw9TJW51tDWGMovkEHxpAwsmIzgjWtNWTSlP65RSDQhnX5yjyo_sO1uQalQcpk9P-fswqVOZZvJt9J2Q7OYv2x45-MRAKxS1UjOtXancE5t6fHQ3EVLNumfzQG75oOQCBhnIhsEB9FYI70y_ORd52767qhEq5YP3pRiIb0cZ5tCwjglCqShKvn2aVPuS5pg7cmZo3sz-kC3Bfr5QwrA73SjXU2h42AcYmT9Kvp0QCJ-SZy6uW16mDU4isdK30CTuyGVBoupdhXSFOnfCadZscDWjCbrV6onsIgtVPsr58WHkhgaRasO-ox7hTZawT-L9CpTlQct8bcrp0DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=fpa1mhQSw9TJW51tDWGMovkEHxpAwsmIzgjWtNWTSlP65RSDQhnX5yjyo_sO1uQalQcpk9P-fswqVOZZvJt9J2Q7OYv2x45-MRAKxS1UjOtXancE5t6fHQ3EVLNumfzQG75oOQCBhnIhsEB9FYI70y_ORd52767qhEq5YP3pRiIb0cZ5tCwjglCqShKvn2aVPuS5pg7cmZo3sz-kC3Bfr5QwrA73SjXU2h42AcYmT9Kvp0QCJ-SZy6uW16mDU4isdK30CTuyGVBoupdhXSFOnfCadZscDWjCbrV6onsIgtVPsr58WHkhgaRasO-ox7hTZawT-L9CpTlQct8bcrp0DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=GlpDmOw7edPN2JPPaBsGpyMjcKzyd0qTh5kQjhJA0bJ2JKTMoPCcCYjPOIY6toGG6MOtzuGlfxQfs-Ag4b34FWpttIMWtTjU3yaTJeQKuFL1RIp075Zm2urUWcS5u7ISPxRycSi0fuDe-vV6FputD4V0xLRW2-AKNi1L1qxVdNLPjHqhtktGV4CCco4o443EEN8LEwQIEtrWPCzmUJzDtZ29kzbcgo_Vj_w1G-GBZ0d32uk0KBJVf-LX64c-OsKkLPrCadvKpXoaQ1_m7gf_K3g5akqkkGQkYdv2pDZ4N-LhDfN5i-zddOE8ZK__qjRXLoz7pKBFgnNrHw3qa8NF_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=GlpDmOw7edPN2JPPaBsGpyMjcKzyd0qTh5kQjhJA0bJ2JKTMoPCcCYjPOIY6toGG6MOtzuGlfxQfs-Ag4b34FWpttIMWtTjU3yaTJeQKuFL1RIp075Zm2urUWcS5u7ISPxRycSi0fuDe-vV6FputD4V0xLRW2-AKNi1L1qxVdNLPjHqhtktGV4CCco4o443EEN8LEwQIEtrWPCzmUJzDtZ29kzbcgo_Vj_w1G-GBZ0d32uk0KBJVf-LX64c-OsKkLPrCadvKpXoaQ1_m7gf_K3g5akqkkGQkYdv2pDZ4N-LhDfN5i-zddOE8ZK__qjRXLoz7pKBFgnNrHw3qa8NF_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6564" target="_blank">📅 09:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است!
و این خونه عروس معصومه ابتکار است.
که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،
حالا نامه نوشته به مقامات آمریکایی که من
عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6563" target="_blank">📅 09:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=nlyw36Bd-xClM2V3MNft7d8NJamok3ydVZ4TkYCNM8d2n3daUsJmtqWEuu4FdItwS8DiwpHaAFH4uymIZOz0N7UBYET0g8sPD7nlSRit2Bvk33mjXi_2xYeVzusRfpQfCCoLhq5SRnc_GrcahQKtIiZJpQ41KSGcQ3qSDyAi_x42wS5LGs9AaPR2lDDda5IVdURc2zklM77lOsntOD8gLA433m0DKSSa6_2q37YxQK2djxH_OzS9huRG1BLjrC6Y0K48srLKFOvkc20UgoiyEUBVtspKjle4iZRblXNlBCJs-QeqNBrZKePF20HBD5leCi6GqxPE29LDaeT--99Ofw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=nlyw36Bd-xClM2V3MNft7d8NJamok3ydVZ4TkYCNM8d2n3daUsJmtqWEuu4FdItwS8DiwpHaAFH4uymIZOz0N7UBYET0g8sPD7nlSRit2Bvk33mjXi_2xYeVzusRfpQfCCoLhq5SRnc_GrcahQKtIiZJpQ41KSGcQ3qSDyAi_x42wS5LGs9AaPR2lDDda5IVdURc2zklM77lOsntOD8gLA433m0DKSSa6_2q37YxQK2djxH_OzS9huRG1BLjrC6Y0K48srLKFOvkc20UgoiyEUBVtspKjle4iZRblXNlBCJs-QeqNBrZKePF20HBD5leCi6GqxPE29LDaeT--99Ofw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت نمی‌تونیم بفروشیم،
راه دریا بسته شده.
چرا زدید زیر تفاهم‌نامه و حمله کردید به کشتی‌ها؟ که قیمت نفت بره بالا
و به ترامپ فشار بیاد؟</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6562" target="_blank">📅 08:43 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

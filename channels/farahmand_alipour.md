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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 09:31:03</div>
<hr>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_Uljm4Zx2Fz1dqPll7bLv_fMbk-8spyxFUmUPv-h6w8B-bqc7wh4YBeps-UNGo5AmPyeE2pukq8q5iPEq1eOL4QDn4GXzvEeKNeu9EQb0VwTp4d4llVvJG_mKuHoMmggpNeIMGQfGTpss4ZlDd9vsuSvq5Mgr4V14oxGIZyKYPd6JXcUV76wc7JwbhqQMfunF1gZ259HUxNjA1ymY54FNo9rPHbhXfCQQlTNMjQAl95Z3I6SWNsGaNiwGqBzvQqrUixJVLenYYSy3bGenhqpHus2n77Pa-rSito2fRadR6cYLs3INeHKlPXLn7Q-DHHhluOk5c0imrqJ9_cigU7wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=HsHTvMPf17IsN775MwKaOnWmvK7F1123JBryAR-JHZsohtZcenB9_pkKZOThH7F1pTn495XvVqzwvL6InMvpzV0tx5fSADVu1OOSswGVokKx4hxGOhMNHBa23ZNAJYzdsnklcAylh7gBEicmdIkE6dx5u6cZFKIMYLHu6-38r6_LHT5feO584P-Lhoop8Uwgi-WtGx_lPrTWfi58PPQDMHw9sshaCt2MgzOttVlerVketzlKZ--BZQOcxrGQ1SNxjDmEocT8cjChH1K_92wrY2aef7g8tIRGjB8Y59PUZ3od36cWf6XPwjY-lLW5DeOIOtnk9oWVoBNF-fnaC0MNOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=HsHTvMPf17IsN775MwKaOnWmvK7F1123JBryAR-JHZsohtZcenB9_pkKZOThH7F1pTn495XvVqzwvL6InMvpzV0tx5fSADVu1OOSswGVokKx4hxGOhMNHBa23ZNAJYzdsnklcAylh7gBEicmdIkE6dx5u6cZFKIMYLHu6-38r6_LHT5feO584P-Lhoop8Uwgi-WtGx_lPrTWfi58PPQDMHw9sshaCt2MgzOttVlerVketzlKZ--BZQOcxrGQ1SNxjDmEocT8cjChH1K_92wrY2aef7g8tIRGjB8Y59PUZ3od36cWf6XPwjY-lLW5DeOIOtnk9oWVoBNF-fnaC0MNOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=YiHWVco3cExOOjFoq8nm_05Nwr2xUQORAqaPjyoLjEtZp23_QCbm9nKtXnzAoAGqKJjUASNXQ_rfO1R5EjVQ2Q4plU8lF7tU3zU_ZIK4igMz6mTKShfcbzSqRR5pn6MD9XcWMncGW7OC0YYjwH2smZU_vay2oxsWSOb1wr0HEAOceueRtV3WS2CD6HtbovY3TeEvmmwP-LS9D20kS1h9trLqzeA95Z1w1awijcVzt4vearMVZbxVRRRq2oWRXRUpt6ee326BGJVZo-84o-MupHnEQO33AX7p-EZPKQA8HFwBN0xkFp56PS3Dz6aw3c77PyI2urZQwiweFKhvNyRlUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=YiHWVco3cExOOjFoq8nm_05Nwr2xUQORAqaPjyoLjEtZp23_QCbm9nKtXnzAoAGqKJjUASNXQ_rfO1R5EjVQ2Q4plU8lF7tU3zU_ZIK4igMz6mTKShfcbzSqRR5pn6MD9XcWMncGW7OC0YYjwH2smZU_vay2oxsWSOb1wr0HEAOceueRtV3WS2CD6HtbovY3TeEvmmwP-LS9D20kS1h9trLqzeA95Z1w1awijcVzt4vearMVZbxVRRRq2oWRXRUpt6ee326BGJVZo-84o-MupHnEQO33AX7p-EZPKQA8HFwBN0xkFp56PS3Dz6aw3c77PyI2urZQwiweFKhvNyRlUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qG0-OTma0puj4rgqkq_En4cvNdj30Q4CWTviFDtT9zDXXRasTwlCsTeLccSFPIVeqoHopNEM4doMX-VZgMx3figw1YbXlGbL1GyDrkEAZVb78Av1pqRvY-lDUpVvpYCxSd0s5iuZW7QEVXeFpLli54EYj8UCZDJl7JeM-zYf9xHblztob0yxCm68xkHPIrPA_MKqR6_IqLpodwT0k160nOypVQ8j1WDVN98hOcT3sxa4v5Uyiq2wyzv5vjkYNfRk_zXZCGUCfdvLn8k1_qXYAB8WIBu_oJQPXZu4a9i2RNZ2P9LbXz_7_hTW55E1OWA5DaY64VQNtfxxT0BWZXdmQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8rChMa6x3iaBk8XLpiEIvS3KxEwDl21U8K8KuBVKm0X2BUALiDVr_d9JH3o1s_8jpSj73pciRBp45eNwPaJCGOcMFEa-nbR__No2YMuzVcpA5OACtfIVuoPXuufjuvgltd-8jH14YOHMRwYrpommsROp_60xHfK2eMjIJsKPlgszvxnAcWH1-f5S52c4D_xL-Tvtt8_FkBxEnzhc5E_otPHUX4l7FKgt0EHwG-Af1vaS7xl4jHmhc5kAOrCu2VXKo2Qsl8AGAnRWBREo9aPGaNie7zHvpOxFHCI2fVYTX0f5ZtGnLaPkyoIGsi5DwkHf9nKsn4tudAyhvN8KobkEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHi5c9-FHS8-QGeypFRHvH3TEyHYN-AW_TOSouXDoxa4BsiGSIGaJ0Eo-Sr6CUb-JIiGyasuIL4rI7VDXhJBfDzehgdB0xkWRN6EaCc6-7Kz_xEvBGeUFPXszUhFkfSXV9khqXm_5BZqUqUvU6RolqiBvfHclt7wRcQMNOIsVbcUqb5f4CWYgiOmgASqaZdkrwHAyiRWkNG4xKGuVs2EphZ27dIcWbE45aoH3qZtTmweargcasM3peq3TimOdefF8X7XZ5S_ubchVLFbdzvJju4LGI4W6e5g0TVwdxaFU6iPRLUizQPm3HspCANhYYDkrs5F7QLHUlAnkuzR7OrNSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9VnE06oP2lfyHGRfLfXWLl4AzCcwt5wb-7_WZP4K8vFnYwzMEDcN3Z6zrGu87VMTG0mTGGbPIu3zeCJW4_zV-CH6ohS01GBm65l30M-xYvv1vQjED5hYOoQmX8D21FNKHjQUIr7gsL1jGH-zEB5_-Md8CC9WE7Zufa8DKBgIa27d-icmMlLPJCY_faFssHygLk7p1m5jbHgczkWxp2Z5EnNac0_vRNllcnaplIsBDrrTuY23u5bdqjE1SLLuMCMzJmvNrhP4JW7FS_Oou82tdRNi1R2LdXTStHxgynQAD3yQY-wKRVm31vNkyCy0fxTRpF330av3iPagnByuC7Q6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCnNTw-5iauSaCfv_TwxEWpQMO_RhTRSAHeLH2KGFSsRW6BOgaDE6kTDQEVbIuddNfGjSTxounT3P-rzuVJu9D0tlAOzwxJB1rClU6eIUu9wIiu9Zu91bOTcii-g-KICiQ7_V4nsb3_jDyUKD4WTMx5o2YLp6Zxh2TgCdcWPQLvb8XOxKtQCswYVH4Dg-Tdk2U81Mo9Jf9YL8uI7EjS_JdSu4WO559x8IU0UcFG_f8gVqT0NHkBEq3M221QGxioXVVwspAwoUHVutrffEQhXClZROGmHYzDZ0cScztpRjIGY1EU-k5eBnFuYCX3PBB46vEXQRgBfR_hqnlPpco8sQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVbxWBeg6_4AYyAFzRAu661PcQpL3yEX4ugFP6AmVh_MWHfD06-Xj4WpIHFmgR56iG6E82IsF8GXOUDkMvHwIoOcD38BtS40aTSZ8TJRfZcqDAh9vNhCSBbtuLgILwzt7LV3gI4rJF35SJ8IyrzXC94RuMaH3hW6crSDXn-6Xq4QVE3o77ATxFf4iVy1MaSkt5MkNds96JQwSn53ujaOHE0AgbmLApMwmPnExEmOuff1tHM-ivJGEGjcFcAJQNCdvKYeb7w9orieY4iBE93pQlqmZhOa_Ucj1vFOYqIc1VBobqdbS-zoQ8SGqlHeHetwqzeIi63z_n1HELz3Mzrp0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvRBQ8NHwhfUbOhqJkT5V-FV1mYtxot1nznGleZTemuWyJ1eAEMqwZQuAeveoa9SGjapruC9KlnO-IC6OmJd1FJOwhTqaxnOyKXFQfdxuYElvkYlHwN48P01OCTcjmYn5NsFVnjtcUB7QUsNSpYY4dfqVsNyy1XdTBYvnhzeBJZe6yV13Sc9lNSaPJ2oK6lFGDsn6AwYEx5Ni8tr_mdFLTZIp8bxxq1xOSEiUxV_uGiqBVWtxFgCFbAGpeo4xRoUzGikwyd4Mmzk-1Lxyu0k1Mc8c5OZNYN8gS-SiiG_GUI4ENGb4yNLS6ItEWyyYSBg1GAkAsQQaCHl8CyDdsGVYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=nfrEpT-JrxHnX01m20nCAwVYV654m0whkXhnIN9MTJaPg72NRBwsFtegJYEG_wlIRoG4RdhjCbPE22edBtBMbdhmnY271ndltwN4ITUEoPnaLJXpociGjckdCh4mgAKaKsK3EYijpteZcsiuKls4b7EhPFn3ddXGhQNxbFpoRlyLlT8gA0YvDiDkwWvmzXYp3a3dTQFG0hIRI6dMCDVk0KIQtyC99LWU15_CAAuwXm0j3xpPE07nL2gVjZVxDUsC0xuxePZ2VqEXNHxZ-V7JQsyjMr9c9SDsjydrVskR-Zpkfkz8BbZbT8jZ7c7Z_1jnKXxcFUlBc8IrdIe_5jwXSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=nfrEpT-JrxHnX01m20nCAwVYV654m0whkXhnIN9MTJaPg72NRBwsFtegJYEG_wlIRoG4RdhjCbPE22edBtBMbdhmnY271ndltwN4ITUEoPnaLJXpociGjckdCh4mgAKaKsK3EYijpteZcsiuKls4b7EhPFn3ddXGhQNxbFpoRlyLlT8gA0YvDiDkwWvmzXYp3a3dTQFG0hIRI6dMCDVk0KIQtyC99LWU15_CAAuwXm0j3xpPE07nL2gVjZVxDUsC0xuxePZ2VqEXNHxZ-V7JQsyjMr9c9SDsjydrVskR-Zpkfkz8BbZbT8jZ7c7Z_1jnKXxcFUlBc8IrdIe_5jwXSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dG-LphQoTR5T092ojTU417nZ5ZNwuLHgAMIGosCkm3S7rZs-KdlUMpUrzrAOiFarjrUrARfctqBw91QP__JSY3u4TK_o_m2vsgLaLMNAW-3n5bj5UaK6OgDb9zMSncwXIQPFaJBFQ-KJsCEUN70A4x0ReQKfBAQkRQLw2Lp3ZCtclt1eTHJrIaG1DAWT3U5_GW_XL8nijD-qqDJ1zGURUIanA5zwNqqD5Tvdt500AM_R7wIsz9ZVc-3Qxy3KMOXM4i0CANdw40YeMsPgZIbQueI7XX4vZHsSi8nqNOerDGWVUMYCVfGWS5My9WYMrm4mWOjb23WBavH2epzZQF9Umw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtjRC8ZLcWUbaIUY5de_ZUh9LQvFgwrk8N8dIlVsHOmqkyI7SL17t7d0yghqdwWqLyhbZr7wMTF8dAlcEXZBfXNM7R3VnOKkI5F-rKYpieuLYDhTRTRlBT_YKJmgYaQPd10cGZCX7bhXXxEMzJUg8B9MQ4nvQnCviUEWtvCcsqqzvzaafpZG83GOIZuwYPFD4o7bLTQaEryygGAo09S364wvSG2xKHb5mWd8zyTdlRFAXrxWuEWJ5nR_1mtxwLMVbfUqu6WVcCE47w8iq9n5w0UMGSbuK__HYEYadCepE339oYH6XrH5ER_58sCFAvrGChnng4DK8XZu5BTRg7u8HA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=JR2_WTeJib78nZp7Kc5g7btyJtGlUXr_6QQr9-k2zxVnOCLUCmAW-Zipbt7V_3H2mIQWkeElhggQiFzrEOK7F0Ziyn2181Btv6gUJDMEBcx99eFvZz0SCPMi1r0XAnw9b4m4DRcgkX7HC63jjAUawThm5XEfzZCVrkYeB6xaGjIaqlr7AFLXc3tUsLyg7x3gOSiWRNnDGd7B5-8LqUr2p33PArB7rc3P8SWflBEJ0qC0b9Pggk4GKMchAu3g11bv3hVmtUSCN5JFehfvU8I0p_Gx6l8dkXaYgBgSgOTsjZQ6M32wHKzWtYpPOAFtIx84hC9DA5_HH2d41wHZ8uKoDpRPV4Ct-I4rFBpezO-cvPZBgAhOZyhpwr5ej2oTjpyIgi03OJOlE6UCoXupxDcyscUnd9P5Va48vIr7zLVvSY-CsdjJwuKd4Qy8nf8TZGlv0fkaWiSJR5oAlCjw6ru4dRb_1Zs5U1Bq21GxjblwMjNlPb7A5OC-_r854veiHNTDyTnwERJ9EBmGxPUSLhkoGU4cGSd8eWufVO1orvRwEx07DZIGS9HeycksCbQIw2qhmtUNxT5j0zCIL7DRdqR3QsNcNMlJqVmSsj0fRt1Tt3I_kKKnh2oqCcHHWxhesoMbaTh1N4PKrFo4wzDdlyzRTgQ_mbLQDZdBYnB8l1yfHQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=JR2_WTeJib78nZp7Kc5g7btyJtGlUXr_6QQr9-k2zxVnOCLUCmAW-Zipbt7V_3H2mIQWkeElhggQiFzrEOK7F0Ziyn2181Btv6gUJDMEBcx99eFvZz0SCPMi1r0XAnw9b4m4DRcgkX7HC63jjAUawThm5XEfzZCVrkYeB6xaGjIaqlr7AFLXc3tUsLyg7x3gOSiWRNnDGd7B5-8LqUr2p33PArB7rc3P8SWflBEJ0qC0b9Pggk4GKMchAu3g11bv3hVmtUSCN5JFehfvU8I0p_Gx6l8dkXaYgBgSgOTsjZQ6M32wHKzWtYpPOAFtIx84hC9DA5_HH2d41wHZ8uKoDpRPV4Ct-I4rFBpezO-cvPZBgAhOZyhpwr5ej2oTjpyIgi03OJOlE6UCoXupxDcyscUnd9P5Va48vIr7zLVvSY-CsdjJwuKd4Qy8nf8TZGlv0fkaWiSJR5oAlCjw6ru4dRb_1Zs5U1Bq21GxjblwMjNlPb7A5OC-_r854veiHNTDyTnwERJ9EBmGxPUSLhkoGU4cGSd8eWufVO1orvRwEx07DZIGS9HeycksCbQIw2qhmtUNxT5j0zCIL7DRdqR3QsNcNMlJqVmSsj0fRt1Tt3I_kKKnh2oqCcHHWxhesoMbaTh1N4PKrFo4wzDdlyzRTgQ_mbLQDZdBYnB8l1yfHQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnsvnFzKjAcJSixvacsoT3nhR6v2JcPOgKrI5aLlAQSfbrY_HWDjInJBntnlIfXMReDtmGOtP7Yi7F2ZrsZK5Cjbgg0UOrCCPqUpz4_m_Of-bAmYjgCWdikKmSzl4JgicoybTnEWMCLeCJ9nkTH22Irhej8z6NnyxngaqS5SRLZ8mbrIcN25_In_Z5rSn8QbUtLUxMAixgBbrjvpLregDS5sGmPfX_vtyneVHyIGCHPEZM2ZsY1JADKepNclMhEh0mlbdt1iLbccdtBjZ07gYNr4PhX1HxEWwg3o0lvvQyQrGr4KyTfxCFa0fQzsPv9U6iyKchZHJSsOofRMc-RUGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=SYaebKb1POFCmwLq2fL5ETxgfORAf10g4PCW4Mg5qr8NIEBHPfmVCYe3XpW9AI5fFbO1ImXJ6oe0cQEJPyJ6YZZlmo68EHgjdouRMh-UaJisPGwOelqqMdWr0SurSBrGFHyk8rBNIt8Z90hJ-H5Befayc59kqewIcNowmanzgjndtdPsMDvCPKJizjwIRU3IzeremGa_VysKD74Lf_92l_L2wXW41QDuEFH3bWXaaIvcZx64SJxfHqgwXBjZy0ujoyOMYkeIUf3igI3BuH47DoaOlg5UCaUpUB5koSUHBuDo2i8OpcI04KhUkNEiuSZk56lI7FEXWZ8GWSbvdkDak3SXL6c4MYq_1heveDC-dFX15in8QmmSfqgU4P5k7x69iJtlOwtFHzitkeded40tGaauU2dV1LGOoQn-b60u7fD1IzLoOdRAHrh8r1OkPZPpU8lWjHeoEhMP0JWic04s1Nc0ickaTPmxUFLiQKLJnrZhLMl6aeB8nxUw1_9DhhRPGbcJJ4QdfET-mJM2LR3BnoIhsGmQExWyKO5HbPh_RaXwVPmMmJaAZnHNFq9Ju300uVBP4Aa8QBzT903wq8Q2chm3jWBoMO0LNxa7h86i_qcMswKfpWYI4-IAw65Of7FIC03nt-a4QH1LgVWjk_jSFEPEOHOL2oswN61xuv4C8A8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=SYaebKb1POFCmwLq2fL5ETxgfORAf10g4PCW4Mg5qr8NIEBHPfmVCYe3XpW9AI5fFbO1ImXJ6oe0cQEJPyJ6YZZlmo68EHgjdouRMh-UaJisPGwOelqqMdWr0SurSBrGFHyk8rBNIt8Z90hJ-H5Befayc59kqewIcNowmanzgjndtdPsMDvCPKJizjwIRU3IzeremGa_VysKD74Lf_92l_L2wXW41QDuEFH3bWXaaIvcZx64SJxfHqgwXBjZy0ujoyOMYkeIUf3igI3BuH47DoaOlg5UCaUpUB5koSUHBuDo2i8OpcI04KhUkNEiuSZk56lI7FEXWZ8GWSbvdkDak3SXL6c4MYq_1heveDC-dFX15in8QmmSfqgU4P5k7x69iJtlOwtFHzitkeded40tGaauU2dV1LGOoQn-b60u7fD1IzLoOdRAHrh8r1OkPZPpU8lWjHeoEhMP0JWic04s1Nc0ickaTPmxUFLiQKLJnrZhLMl6aeB8nxUw1_9DhhRPGbcJJ4QdfET-mJM2LR3BnoIhsGmQExWyKO5HbPh_RaXwVPmMmJaAZnHNFq9Ju300uVBP4Aa8QBzT903wq8Q2chm3jWBoMO0LNxa7h86i_qcMswKfpWYI4-IAw65Of7FIC03nt-a4QH1LgVWjk_jSFEPEOHOL2oswN61xuv4C8A8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oe2fLbsFNQ0Aktm5jPHVOpl7kKMJpZlmIjUh-qc-UgE02a4ExiaReo_7aLoHuokdNp7iVkEVZ5TtmSFF3zN9NjEHZebDDPiCqs6hh2KEB4xaLt7cwE9A1r6OyT4XJUxmDmu6mYcNJWZPzOOFPysWzxk9sd-40FKpff36ZXZvQVfTOiyCcoUeMqOEl6-pAX-6br5-MhG6zMGfxVjbKPMGPnmZRVVMUVNUW_KE-yCr-c7DOUCVpzBuL30c5IWmlIY0EW8THDTAQ2qSjCJLs-X_PakSTTrigaID4te4Nw5Remyc09SW1u1JY7DoU8cMqRLILJE83B2zSJJP_v7EVvypJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5cjShk2Bjrn9gIWg6HQ4NsnmayACM6jZyavBxncPC-kbDDBv9I4NeYIMP803y0CGMrVjC6PF_BxAT3ONBsDYPLTSXPkmZQ1HcbF_n-8_iyIcQS8HvX7K1lIOGmQu6z7SXWnSMORKsU5V0TZZv11MrJE4cko6yjMANIOD4vUcuY-2LIES0E0LO6d92wqxXNU97Ev7r_nYpBePYBM6-Y2U9rEG41ttpdfAU67fAyic6sT0AsuX47S1S6AY-an2uX8ffwSDWDdTZwUqwkoEcMmS1NkUPp4ZrPHnqjfHOFh3hOg5v0QU6Qq1ScK2D4wW3k5_x8b62IWi6g5b7IvF5YOCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpVVz4OXTFJbO3StFj9ELUEMVe9gKSFRySYMB1FUsc3z1SOZhgFXgB-IGVwaqyjSo6YFNnS0HTTi1bT86r1zZNT9cODapU8SRyGIQX_1hEwaBkif248w32EeIUcEplIrZZ3cqw5uhwIx_seKNsNb-dFbp3jmw3Xs00bqSxOiXaaNqxMDiX5Erjzjq03boDEQcaI1GoV2mZh4ywSHW7X0M5s26fdB1Fd2k2YMpmTZZtPZsJo6042lsNaXeA7DmZqxfUnqyRFYQ9ydYZVKcugNAE7UNmPHc-dLvAHiRt30BBd0PQTMImFb4X7gy0ydFhRt58Udzg2MXN5O9a22JL6mTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXJb9mOba-9092hv3DCyHDdDA6DOsa73eX-651grsVous7BWUIHe9KEkxh1L5hRpRMC6nhtMAUaqcVgjD8kHDXDDWB8xCod80IZNVcOLFa92XRnd6w0uB59QVLApm_Ml6wuNMORMqMufLpQeAw1t8ZmhCG_hfGToyx8wDj1ymh6vBB4xTglFRdP4-htC_dXjDI01Cl-BMGyys8Q0xsMCnhZOPzBq0zUVMAvfpY5-OSL0sd4W2KDIQyZWLTHbpQ_iKbwfrmPTjj_zqVwpjqbCnX18j0d1iA6rXLM3YLHPDNK7z68xKoCCWGDq_Gxb03Urd-O8ouE_sbdK_jDAHDqAYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juUlWXSMWJHc7xqecnYtRwdtfzo4ZvKQr_dEg0lP4oqinpXximH6VMbOT_cwkjSgtQ116wySroz0cormdwY4FAmqHNWDJkG2O43CTZZshF5apmAMU5OfTxbyL6u4lgsBWxbYmWWfNbnN0DKNrzi0rFjIdsmIs1XTOIKDZl9r1sjbq9whvbuUw3C_E_i5FsTUOcZwqI5H36BLzcB-FyhRKoBHM3hGc-W50oYplMrxOBrnT4LY_oQdboZn06CSjNJ9q1iU7jralZCsw2-4UH9Mu6WkNNYK_YwQFeW_PxjXxwVLd2G4Pjuszmk_ow0Q3HEyynKRRQMd6GsRMgrUiXv_gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4O1yhJ1m8eQ4aH2uddxbIOmMZ36XvOHPkb3tAHJ_y0tCgx7jY4ZReftqCeXrRAs-SNhHt_nhp33BjCMkw64fhhsWo_LOg8LLb8U-Ry_0BZTvZigJY68fDei4ftZ9cNx1BwwxYq0x_19cZxvqcauCuKZQBotLT3HAjBUWHbwi0qw2D8f-pm3mVhGNSpfdMzyot-6MjqrwpxbX3HkpmYriJSZxnOI9uuk0Gu4ZtZMdWU-5wEKGUasvavnmqMx_ClzfIbxOSCbR53usd2IjVJAcJaStkgPnI3WVQ7J95Zcl38B3fytguRCbJaFzONmxz7arHe_puFZgYJQL-yYb56eRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TM7DGE8NIOKqzCzMc6rOvV88JZHI_PXxtWnd9sikXtS42bn6_8PuopnzCQ8HaC3hZMw1FKS9-CJ4CAh5Lq4pu6f3xnfbPHFQ21Un0fkZa2-dhqZsxM-le7mfRozrxnJbY-LWn95h9NTpqFEBq19-3P9nOadfSRq1D0R7lEAIbcAocpWtu9QFqjNiTWObBkczQwLywcq4_cu7c_a7K2UGl7lKb0ZUgiEiCWfonXIapIE1XJhl-gIK3YM9lddsPKhdcau9tgAYRNvrksB9IpJQQyVkIPDL2gCtvgiPoGTU1qF2AzYyyM4-jaLs_84uHdiZ5rSTpiKFgIvm8_MC-h3mAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0bEgHyMCfuWv-Vlu1ufebl-PNj_-cJQiP9UxeBSN8wpxm44A6_1IFLgSt9Cg-dloGqtTZ3dtZnpfzS-M_3F-Z2cICRcLRz5ygXaZLniqf8g0mmIXRjKE_urHFqJySltePSV8GgJVfh8Y9emaQrdj1lMwTKxG8WuM-8aAD7l3lZDiU1aSrRxisS8lWG67zrfpdTCc69x35wxLR3aIm1xeTFj_BS0np2iha5dUd3TSETbpIU3Wjk4pxtnkTtwvfFR109EBe7q-kw3pGX5lnzU4PxJVdXWaFK43WTEZ3J5NT2p_V69XicXIaskMH540WjJNTiMuh4J3Z84Ei3pIPo6nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swiSOmgzBq6uIu5Tb2xH1A-GZU_kAWlmQVrIO-yv5UHkx6gnP-b0li26l-2QSofGDX0vQLzCODc6qSdG6qiQtd-1DORa5l6YrK34aQObLUIyfI2gXb2p0Z_gcdAF8cYIbrZcVLe2u6XKtPwBj9UCp3rIfrxI2E26EQX--Kg32XP8zE-e7xNMB4U3yn_ECjAhkTfr1sT3K9EgwTGyXJ1qzHH_ISBbS8avmLFmRIuXxGqYQQ7jtm9z_kg-3-Kg2iGdxkXX9eFJ4EH8pvc88c3g-egLDOmdm6eyy8F7w8JSJz00PCs0HpAf_lTWcY8zoLMr0IhWb233eWXTbAdpfWkN5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkHSX-F4Q_pnHDkTHoKH_mhTxuYFmGJqKcBBxRzHMHiaadF2aOzi6fVIIcFYOCM27wvWS30w-fDCdpmN1b50nEtVr8PI6rbnpHM-KkGGRhXcWgJYSXhCmGKbUO0g15afFQvArDzAbLIyf2BdBs1BgVXDhFnHfpbNvLbI_3mabrYYTsy9P1JQEjIYe6ujb3SRUeYkZH0ln3Tk8go5h3i0vFIHCVmNsuuLjQiKSLrBdvt0PTEdsyBU2wmY377EGgKWJo6UZFJQFrVAYxa10LyVD5M7Co7OhwKSxqtX-SkIdutwBxwy74KEfjHoUWvioWTEntbQNdz70XD6TCGafg0AfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuYou588dWCZKeKBkTukgVxy_ycHu-RGPHGkN0FeNy_kc0C99GvneIowxo10bI1T0wQPcoeTJi0qwB0WRnGx-6s0fBEJF0IIvujJPyhrQTsjEutyFMyLix6HXijaEkaNOp4FeUqoJg_ujlC9DogbFLihbJZVh3c6X0BS3phskiPVdFyHGgwVEg8YGpWPm5BsdGJn0SVzb14uh7EMO4BKQRYTSbRQb9vbTwDfBvx9BJd-KNzNhVGUET_tgCUFAJYw4APWioP-8Gja762AF6Qs06fqBtbH6yP4SFlj3d1gtBz0sGhCR2Ktglulwm4gKSiHoC5_7Yt8uWkB9zWVLWthBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGX7FGIUfn_ZbQnLLg-3U1EVxfJuQ16PYOADwt0pKd6uTkIvMkBXzVOqidX_ILtiYwI1zlI2jJvQGbu2b_MxN21r0a5W5eY4KC2opajl0iPNM-eBUSZ7GcjnHPHXoFaaIouarHEDus3zJuq_mD_i7suyGUngd542jNH3nRvLRNBYeTV80OVzgrc8I3Dj5NC23rhnUpiIpKw_Mpp0JYadd7hbYT9V-LCFnaaWG-Qo0uUMybMuaVdqwIQLtR1cjLxqQALnRg3Cv2rV_sKg-iaXvyOt24VUJmuzQLsWGa5hAjY_8iLC1NhE0BvnEgqi9nLjJTlluPdNiY4y0eWXxtCi3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imveAftW_bViVIZxpPjO6h5Zdw28owx6Sta5RjpoRd37SZVm2_IyEOdPdmlCrzUPHsDFHtQAQzH1pE7Kw_azGxCCXatU7NK6GTgI-Mv3z8Zf4He5KCo5HhnIYu1D3qJzpYqdyxNmLosaDjAHhBPhwMZRDB-bm8lygM_-Zl-Ek3gUIj9j-zsFUgNUoYdjYXsL2Z4ghiNJADGlViFmfO4wWA8zIsYA1x-ZO7kmoKz3jWzNPgqf4_Ya0A5iU7mkKjA6ZItvy5ajxy3v-6ECkhASnIHUKOxcGQgnIwgVZG-GnrTIk5AudhN40WZKdFH-c0kVY7y0DL_WkYDMJVV8C5_HrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6616" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmhrqzV4NbE4zlUB2TgDR7PSFWgrtCu8w72gL_Mjw2vkXKidhyZcNleC8FXExu2TE5PVJIq0JI7pSviPAD_NtgcAu6q2j_2i1dN2CSGEzt0YZznsR7-gXamTMVdgFXLMM2tq-JXATwpexRzHEwbTlvTe4vFgJ85BRTAH0pqLbGDpf-TeCMOuijutL9LY1fTawUwcsC5X9c8rpQinHa7gBbC6017KUe1pGLL0m6MgFKDjVA9FOW8oAfwdXu8_p_69mrMps1tM168vQbc24aQALfwSxeOeV6ImgdO6ZMQ0ENf6mDHhfhohyS2kz0Hh_rMzLPfkr0tmtuKUpwrwFgqE4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VthVn4VauZiA3AtNQ79QmLyw4knUUmhbZvkbzP4q5McjFelofG1B8kXV0MjS65pL_6UwxZ0v4H71X3eLArsxLXwkRKNm0snuMhkf6YcVkGj2XMLkPD4KrzB9mZKlecLp8fjKkvgXPDgbDml8FseAQxXQEWiedHPnUS-ald0o04rvMdqyWCB3k1q4gIY1RRd4AnrswDKoYD4Zh6nfi1hHdnPy936wxW5HEFAgGbz4vdaK46kA_YNHUwCTsQWGFjAOv8X3d4Zdvy597V6_sbwk2bs0veLo8bjdwLXUPjLPYHoLEuEmLeIZb679Xkd2y_qVfZfPbmgHTvDRn7UKb0B9jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v8CTvWwn1EpbjYdBOCpbsex-9m1ITomh3CpQDIzY-NL73Uy3aMmZQe-WeTjTUg5CW1roR-nKA9UhOnax_73oalh1NXTerMB_Fbyg67fYxhn0bQBwPK1oerdACv9sX7kEqooMU6ojsJEOHidgNBTmIMjVNFBmivB3yQUvVDINsvKik2AOrjKZntH127oQW2pOgfvDzLgoLgn5ABU8AkcycSnBWjn27ZlNJ8EbjCO3XSmjxExdfo58Tyo2WinP8GFGX3OpnxuUNi9fhcJstaCidg6zwkIme5yHu_c2lEB728JNYZkByjlw7Fzizs81AQBpqtM2YWckbs03-oSlnvnnCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HoaFMHCeIUyB2sHKOEQ5dsuDgNfb68oxY8fbM8vW8vmDsQSMFIRDQwb6CowljI3G8z93ijxJwhRSZ3UMTXFc_v9_YQdK-hx1JFaRQFEBsGl3bo82clIvArdccQ2j79CfVv_KcSrGr4h7H2W8gbr29wsCbq69UGf12I_fSm5K2NkcuNVcVG57A-DaYz22wMkbfBc7Ba_WOe6Wqzx7THpVyG-KfdxLxrM-u3xDqWA8oNqx_ZIzV98ZTLRBPDldQsJ4aTsY317Q2vMgnxOtD8VgY6Hn6VUKLOKixb9bpcGcMzv_hdmPo9fpj8rXljSPcVrplWedifSBC8dSrIvROn0hpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXMqEH4jtmp3L8DuBU5rWDZGFN892tQJCqvempsQRjOR6KevxsVWjEn65rCyXWcHG7uz8wWPZbRKbZDhN22dGKBpS0r61dGzkLUKkiJBNpMl9C_BlqbUmPkhfrRJqs4_zAlr_E5rq9HmuoJa2gCsAkfcUgialkLgDIaxbPzgapbNtS98GSeU9dY9UJ5_HHDfbseoHINA5XoCpXBha33OxMUcCh4rA2QeiL3BOUGP7zeajITlq8PcMeoiuCshzWnqs4iJV-Vgvd1-5JD5HRXJwtL3f2EZHlmlzxM5ERn3O_CzEJ_QzJoWbayYt79c_gm8OZE29wCWjmmaGAsi_ypcCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2Gsocgyf57Beanc2sEOMrGU_vjAsVJbWgEdm7DtL_2Tbzjyi6mfFG45bEL7FV1lHvYGeHFloys7_VJamN25aBeNwalLPhk2kqHM5Vrtp-Pals9TTHzmz3AmO0vfuQ4Cl5-641Uw1Q-fSyIre4KAmY_xlIFeMIRG1XiNBGiFIQTVAmy82VOTF9oshfustxQ_faOzy3x222rNLGiH0AhjGClE_sXerNACSjxAoUw_SXhGprtAx0R-wGQFgNMlhaJkcvISQLPRECuVyhtNUxQd7aaEVG-ARs4POTZBYlBzDyneSytX1_w-Oj1snzxLymKkcdjRCaITYfy6up29MjhT6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZm-5bdPeg-KL7aKTiPx8xrcGzraerhCCsBUDj4eOtBth-da4nlSRHiKeW-icfz96mWcUwCkiCvGol6VB6NdKLLVZR-TbzNcn8s5YwVvuDY1zH8kVBQI7b3WVM9GCIK0gmqYZb2hmbErZe8ZUpicSZTr6U_akk0iN_2p_BL6pKsfsG8xt3Ig_Ykpr61I3IuFj_aXpJ6Cy-nLJIoS0YDusrvbT5ROLOe6bAgyDINzTmCGld_pzYsXnU-kN6qAUd7DOmSBaqwCx1mJR3C5vb8qhcT3-xv9Cq0EbjTbGOtyctpJzoxgasjB7B-vmnUHOMY4WnqIQPgC9dTb7zS6eWZ0pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHcSSldb4Vv_RFO0C9bw6ASyjCKJAQirymnvkzdaSfaPDQywx2nrlyQ6BW2RTLy_L6LGQ8IHOAlijATp7xaXFYAC0PXsL3vApiP4Th3r0ABposf3UVxzR3wiZU4Zgmz5M8epuPnV42gEvoXL-6syVU9DZ--qUV57U1WHNbWvtO-V93dBwPLt3_WEjyWDzPfciw0ruj44aHep4A_aVEQ15kMq-qw0QyoB5nnHzJKSqsrmuac7lFRQWZtk0EnGuVPPGiF4w-bXePPXXG0KjqcVePDaRsyl82zfDHenKC0jS1PfQRE3v9J2Jr9JJEbyFjUHGU80ODH1gRaEhE_t-CcTdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNH_iVswlFLntXaz3MrZyvCygjsaUAbNtrY6lnL1pxMNRQTgL7OqGDHU5FBEXF1DPpLCxiVOdtAB7lgaFcLTFGn3lforQdFvtuldP0A4huqcc0rydldfVOcljCM082mGKiozTE7ci0Wp7_muzZ2Ik-7idHvgLrT2-0i4-wd2NPAlirLTXsdKignuxj7MjXp1Z6ZQ0OIqtPc56QyLQ44wzXTtMFAHit6UNYGnWBj6ENB5s0bg13o-2ZHBMxy8h-Ooz6qro_g4X-XrxORUJ_gUw8HCohU6BGQg44PrlRFGwc4XvRCUHKh-aymm7l3eHhA4D74_CY9j2OxB_9lYC2c1wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgN-zHczCmgmF9c5Dq0sXt6QRP9F__vtF0b-IxFpg2y-akQeEKnglTHk9vu3U4VaQWgLfTKloMVz-D1DtlhVVHK-kX8CayCz9DZOSFJTsNkC0DTah4LKQmvkmwfj5TdUtUTsVDbhFGnyZk3XVWynifHozNJH3Vl-QFcxbPtfAKGgC0q_xgRKLIZhsj9qUylVlX3_KiSXWrbLKvFNvmyCF5XA_3Uz1MkJdP0u0h8K0kfcZkb0LdZIQYkRQP1goX1NU-Q9bvLZs_ThCG6sJnOzbZ2C1IXyypx3GDtepxSyYYb0V5d8TtIXte_aBc1suMIKeoact2IUfmHFFL5UXZGuJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAN9iCoHg2ns4omKZ21tJoe4f3oQHWzGTjGrl8grNbMOvjZ7aeuXkYII0n8Cyu8VPZLzpfhYVaZuCFO3lnLrvhXWLBc-qPYt4O35LYh8MeRoMb4SDqhog3YY5LBWUyAeAgKLi518Tej4qgNFOp0l71qB9fXq6qnjLhwBAJc1UOx0pjzBTA6hHQDNP3VmBONl6m-nFJKxWZBtrAota2Y67FN4VNcMQ-CX1om14Gka1GSOBGgAcNTD0imEmjsFmesMUXnBPI__Xwao6lnLTIVl9fjX7BJX6X4MuqEkejSMWDIgjAXHcwxgdN3y4l1K0GaavY7P9kT_MtGg6_tONjCYrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4PQBRMP3VH8RdlQUnpQCWOW_y0AVguYtFyej2pSrcL5ASupNrU_nEOEtHuEQikYGblxktH0HbotGeT_G96VInaVa6NHNAGwjNbZsUswA92V3NjMQsfzZsHQnTLCcYF8exWSEK3MhH3ysFFgfq0SsTzqMwydKizEFGdYKviQE5AB7EpnG-e_cstYfOOVv31zwnpcg9hdfwfQVPw6OeMEzi3QvUuV4gOwQqbx-oSaho0wQtpqv0WCJqvBg1IaRE85UDrBwu6Qf8ibU33F2GGe-dx5Hct6h_nRhZR_iQkYO12T8MHrr957mZ9lugzz3tdFcEx-aSbpe_qlSARPDyFGjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upjqYI4sLTMQo1FXrdmbBuEhWCqbkg5CVdtU9PGG5j5RCkvaeVKKmOEkbhmSpNRiof7JaCfX6rNOfVy2mvchJGJNEywnJ8yZQY7QcsItx7b-fxsDT3lsBy5XzdYHTBVRRcnNVH66OJYNE9KvFpAe4B9nYe1HZouqYu0oE7hoAdDNHG6XXQi2_tGuXlTvJO9qDEHI3vS9fivg0ej4tcrdJV-dn47w3MYKSpD4sQblM1pohzWsHzQL455wKGBnY-FLrEj45sVfJ_ga40RYKBY7eF8TmPJWK1uOs4yVNavveCclRxA_S0F2MvXgapoOxnYt-mtrhMRZdpZ_28qnbqtuBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEpW9Jl1Xjfex_KRR_lMUhUa-R3Oq0kxRyrQ17_BfMuy3Wd3BDBM9Q8V5FFd-N_kbCbtO4WPm50Oq9K2lGvKxzyTsbyAQOytyFZZvdz6nG11Gc8wiQwY43_Vq1TlaPQb5G3zsp_v_LhIvECaOMmUa-SDWShwmbE4lMboRsacCAL1LX4P56bDDnnWa3n70CfahiWxNA7a7f8-8jK07sTNzWCvRJrY8guJ8g4zgR-CGYH48FlYZMfMR7n8cc7m4SOW9t8T26eNFVVSkskYOfNKEkSxjXBJLx4uIVdIRmstVgW_cOC9xgZHqG2suyCrx8O8_b5g74Nl3O0ELr9XRPBB0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HhVgoHaxdI6BwU3hCQWPjqaFbW_Hy3UfboYVjfjfKGb9QPcsEgAALZMtJKc6jPVJs_xmT7KmOJkLLtFZtvJVU7oOL6YoRCpgCm8Ewbjh9-lnU-sj2M2-jPjyGC5O2pQwO3Tyz0_4NnrN7kaIQGySqnEYRBbL8CFo9H6fvdJydzBmM1XuF_lL9tLjDTwJt-j_h7XWRY47HUkiclTVnK6SPotdIOoWsCvBw6nYWAhthKjXzx42GzpFfGTr6692NMOzDE1gofbNtpTOUVleW4aKEzZeL7_-r0TcEeNhGJFASkYm221LUf-AdAJObfloHPqPfXezOJ6uqj4dvob88i3B_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6gxV0bnlklHKF22Oumqi4vXRmjtvB7b_zzBZRWQ1gdKMsHE38gFlZBATESMz1bXErlKuC7q6iJW8c9o7jlemmnndInU3Yc99FaQsMWPUAUvvTgsTk9nVgfZ5C1TCw3ovy2WOiy4aLB0LOzuJ_r3VjKjbdGVh4pc9g8Pagqxgu8hgzxZCtbav9fUwqfqPpnxgoVR2xwxkh-Ng3PTT5EcFndtmarAsoYqbxYtch5G5jyELdioaKkgoh2CIXaSF7WmMlvrYjGdhRO0KcuLZoK4QwMl0uWXkaX76niCEuvNjbHMOM6CTYpU9UqfedCaNqJgP4XGVxT-mD0Sla6r6sjfGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrloiaHE67LBZjD84QD-nVqJDb_2dNi10ZSH0SXj0kIwGBceucfy6PIGl74oZufEx9J8hTgOgU_bIy9Ld0ZnSId5HhdFm9hodhKZ2P0g7tIbJ-8EL6HTwO39G0GOlXBlMooo8Lk6bfAzSxinqVKcEN6sORx3yUDW__xMH9N7uQMgtDdLVEWEaWsngkErm_Bj6BtM8he4Vrcl1vLJl9y2gGYT_8gpy8v0rbaqsg5mK8npzl5Yis_FpRd0R_BF_v8sbrlj21tqmD0zMWAlL6n42wepgFKgY93pFu_KGEPtHsw_QLakc5pqdwNC2NeaPQgr6i3cSIgWuBvF2s4qR0lv3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSNoB5s7bq3gHY1dU94ORMRptja7kzr1gJ4MTJ1Q5rGx9FQ1YN9r6NPuia7n36ScNmPBH2ATGLB_Mv2JPaIIEX6Sw2vJEyEBGr4axtxoH_zurhhocshiAgOMnEwJ_ovFQIz_rEEZE1pN9hIkOnzbNUXBu9zFlqP0UnTO8FsyO72a7QFvdW8DfphFPeELAbPnnfVoEnLnic2WPDiY7KJhMzdeyH3MNaR3o6k7gm1YkDh43DJ3d2pJip75JWTu6pWdysOTzTm0nuD1ysGBNn3pnCBIPhugALubSr_12Iwb6vuxgOIv9TX17eicDBT83FSP6beuyiAwFwd4MypyuimG_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9lUqviIFRrenaAGZw_9fqOfTbK8H5QL3hBw7QDm05ZLs0f93ohbmrBUDCN9L9XYqiziN_JFFGxB9hNHXhDFfkgeKpz-57iFTQkq5bYxn2w1hwjzxMo2qwzfuyjbCVfsSpLnNEG9lRyYo7h2oiuvrN1loIcLGBWaXkxCJq9ThEnq6pmUZRXA0iQKhSIbte_Ziebiy8IpCoUX6EOWuilCsJWsvs_Of3iE8xOD1IKAdRUrG_Ntionde9Ias06d-tlZkWUDnZz64mtcjdSj5ompizRLDlF2D8CCVq7jqa7FHa9a4wWz0i4dLAQRLMdoqLF1b2eeUo8rXN7EkrHrXN0QHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTEDCuXuvGvNtPrlK75lrkZ6eBW-QVl_sCm2XSXkd1Pj6Qna8cnL9sx-BrnpVQHXC_r1hX_jZhlGCoIUK_rtwoqcI38Bq9a-xMUDgkglan4lTZX0Hg79Pl86XgwWPyg42G6TdMl_ncpUg6Yn4XDb8TFN_NOMKkaaZukn8iKnyd5wvzMKiBXYhyTADyseQMN4miYIcra-pgeAMzR6ox_qrwqwfPj2g8TUkeIe7bKF3nMurRQWvOqmDISnpOTPNlZY1nODIb0JIMR_A0XtsjwRU7cPQAHGwMV6GsTY5azL2BmdgdKS9BPBgy8DK610MvfSTw6gsoCCljrOB6E9p8Fazw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=SpMCgCw1Q7WrOIeLnuhlnv7S-eV61pQCfPrfIZz1RFVan153xY6R0kXrHsGMxOnzGzCYvIPJlK1e5l5E9p-EP3yzVXJ8erqgkLhwKq9uvbZzCCYfiN8XNQis7sA7lU5KFiiFWhiscWU_iUB9BXZNQ1ffvMnHV414D-6pogtr9Ir8INjLpi0Fzr8wZnf1bjM_CLhLeMOkDu2EZV9AkpHSeBFZmj5q4CyK9LwNZ-N22D5Qgtg7Es2mJ1Zw77gRWHOPO-ilIQgnkhOhcDiQjDdfpHtZIH0VaasW-jkBeWQRFCucEvPHI8Y5wfgcpkAEr7-u-ed4FVq6WEKNpr5NU2VYpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=SpMCgCw1Q7WrOIeLnuhlnv7S-eV61pQCfPrfIZz1RFVan153xY6R0kXrHsGMxOnzGzCYvIPJlK1e5l5E9p-EP3yzVXJ8erqgkLhwKq9uvbZzCCYfiN8XNQis7sA7lU5KFiiFWhiscWU_iUB9BXZNQ1ffvMnHV414D-6pogtr9Ir8INjLpi0Fzr8wZnf1bjM_CLhLeMOkDu2EZV9AkpHSeBFZmj5q4CyK9LwNZ-N22D5Qgtg7Es2mJ1Zw77gRWHOPO-ilIQgnkhOhcDiQjDdfpHtZIH0VaasW-jkBeWQRFCucEvPHI8Y5wfgcpkAEr7-u-ed4FVq6WEKNpr5NU2VYpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6593" target="_blank">📅 18:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6592">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6kSYsems0PPCdVBxp1D5lfdEGeRL3txpmBTEIKIh2fa78mkSqYqGtFrM8vbHCajewrcAiQVHb8VhQrmlrqv1558k0wbyXQBtNNX8Ca49ANIOLZbOZUnphjjhX3UPMIU9tp9ORMYyt-dAvA4O6UxWWuospFhqmehoTRr_lTyUFaiH9-trDOjQF77R1ceDZ2sPMotIVK_GOdKatNcJkn3G31_NHlTuTpDbNWOJMw03SlY9Uo7LfWJbDquAjJTIlsrqYWzNcfs0vZNKQYQ0KeWXMT4aJ7dc8Xy5HfwXgalhMyuqmFRvHH-a3KZa58h4577Nhbt9EAaetfPXNW7CSlssA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=CPpuwyBvBaMZpe1ITU4NUCD5Abjao1RA48-Tq9lSt8IQAtqLIvFWsOhzOY7YCRqMfsEFuzUwTcQM2cpPq5rUUJmj0pWggbxrvusn8s-jsnOxjLmZA9iJJyV6x7WgC4QciCJdwJMa2Q1JZ6ojVJDIKGPRK7YBMYeJ-p9KAynXWZip9_m0eLGk3DnTtjWUIsJeeBrvQiKkqv7GB1wxCQrm5zMLnM04MKaAx_dt5BsgY_uhxczuxC4sa_yqERc0oQz0Th-zLAHptm3gAQ611PjlQZwWsEfQQybY67wc0RJwTF7zZOF4NtA0-f0fmjNT5wFdaUp2jSxqnTWJ3g1-AUT4jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=CPpuwyBvBaMZpe1ITU4NUCD5Abjao1RA48-Tq9lSt8IQAtqLIvFWsOhzOY7YCRqMfsEFuzUwTcQM2cpPq5rUUJmj0pWggbxrvusn8s-jsnOxjLmZA9iJJyV6x7WgC4QciCJdwJMa2Q1JZ6ojVJDIKGPRK7YBMYeJ-p9KAynXWZip9_m0eLGk3DnTtjWUIsJeeBrvQiKkqv7GB1wxCQrm5zMLnM04MKaAx_dt5BsgY_uhxczuxC4sa_yqERc0oQz0Th-zLAHptm3gAQ611PjlQZwWsEfQQybY67wc0RJwTF7zZOF4NtA0-f0fmjNT5wFdaUp2jSxqnTWJ3g1-AUT4jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KI2z4g2-Vp14d153m4uxPoAqRDryaEILvOOjXCDlyj1pxjpF-4Uys3wWQnmEbE7oaOlk1JxAbJJduNn8iC69mmrZE9yJAuOYd-qsR9Cp7ZYGxzgcnOr6zTq73P2hyOJGBQTYpXdVZZi9i5U_7CtX46M9WgznWYSXqnwiWD6rESx95kCOzwC7Me6piUbB4Na-gUC73u1QUDYm25qKw3wQ7SCa5o9JXPdlNt3yHp1IuPGDoP-r0K9V1JPi1pRu0cNqwiIPRHqftm-sd0LiFGIVqhlAJj8agKCjElKQbJ9D2WL1TjKqvkuJNlPh_CVhKhelg3xaY37NDIX_7LMd_CjwpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmTN4V2bJtURdMadeoBt3PYprueIy_maHmfjYH8kUXWkWg8nBu8Qbbz1SaoyCgK9OnuBRgseHCsL2CrEIcLhB-OdPPK1RF39nHLSZa75GG8wlIQ4mlVKusk0PpZczBbZwq3jOULYm0kfSUx4n1wLba0b5g_q6lu8oUQFL_--I5K92QAVM2VUt_e_srI9yeSxdKB-NOVDPZFObMu2e-I4hq5OAwLI0qFu7sBntDh4JO5fEEEUqxS3XsFKr1-8JINW0y7jOOs1OZULhlGLP1F5wG5uI9EUmZ4m_D1y3Eftlchmmpil49WttSqkno0I672xrju3bAuSkUHdeqURSxLlSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=t9CXJZdAiqGjjli4IfaINhD2CacvNdiuyP2eVqZ3jvm7u4SFbaqHIQ4Y_VWlA2ZxmdLwH5nUBbi-f9eH6E0jyVIwmD7d-D0FDK4LlHCNY9pvdxjJiOur1opoeYTR0t-7VFKrnITRzSpRE7LOi2ZNMGqU-EmOv3UBXpCEyyhYqgxHksMqzaWNMjlX2up2N3WFcGdexeOPGslw1YkJ18HhgKBF1scKxSs5zMQzTrqmrpvXiBKUErSv0-OCFoIv4YKRzzqx8_hrQS1WfEkB1sk_4k7o6DBidDMsBjutsXMlfkIPTKavB_bxdA6wUZmpbdLTJfD2Lw9aX_gKwWtrgUtFmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=t9CXJZdAiqGjjli4IfaINhD2CacvNdiuyP2eVqZ3jvm7u4SFbaqHIQ4Y_VWlA2ZxmdLwH5nUBbi-f9eH6E0jyVIwmD7d-D0FDK4LlHCNY9pvdxjJiOur1opoeYTR0t-7VFKrnITRzSpRE7LOi2ZNMGqU-EmOv3UBXpCEyyhYqgxHksMqzaWNMjlX2up2N3WFcGdexeOPGslw1YkJ18HhgKBF1scKxSs5zMQzTrqmrpvXiBKUErSv0-OCFoIv4YKRzzqx8_hrQS1WfEkB1sk_4k7o6DBidDMsBjutsXMlfkIPTKavB_bxdA6wUZmpbdLTJfD2Lw9aX_gKwWtrgUtFmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgyTFB-b8yED-Js_XWEcb_CWcOIzu-bqqBgCaKgd0jaIdEDFXHwy5JCqCG99XfjsJCsMjtb474I4BKNq9rhKey78K_MFWOsmjXJhoOLtqyTyjY2x0Wm7pKCW_xkKpiBH0RN5JhLXFnlf_LRdbiKDHxYsRU7tgS0DN1dnVLdmcFrKhzwq5-JYc71JgTGEZFmA1TiF1VbYeBWY_FpoNFhVnvPBYl_uT0w4RK9VV9O2d82ftNPDggXVxzgsiQewvv6DKqbQCENljwVoEh9jhNrshCIQP0-ZvZArhm_wjY_Pl6Q1Fc5LVgMzKj-nj9wi2jgomY-IrmRtvTvyj6U7Xrod0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QC1OAdOe9nrReljgHTIFMmmVW2ePSKH7o9oc66CkzgoY1b_T_oEDD5F0FzX6-asukQmKzHNlAaJYZWvFnpN6j83aktB4afkn_eZhJQp6c_xb02ymnRelNHWQdzgrbHRtUHqPb8A-lUp82jjYwIwOFQIoLYvcs0xcCBvDcB3cLQy3tvO4jL2bdJa24m922q3NHis4aynh2VXuqg0u_Ba41dHZNBjigqDu8HYpyk_HzTqBKPmSvhEb5-kNDBpPZdvSx86ZDt0834PEC9or9c8YGzudBuATSrdXG8waV03LoPAFi3Yk90X73tPZVrYatz1TrOpevh3RXGP3vGGVMc4oMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLqqXPUecJ6Iti2IS97dxo1DTLLR0WbvBXsh6PiDop3wEKc5xMGuWPpFxJqGPEVsTZGSJUTf4R69d8cbTAkYCgqSyGRcMHKJKEz7sZFNXk_3xaSQDDERnkHy9XReHDy3zBnescrWxO5TEk16Lbxl1nwnRdijtbyF5TNuslEkkJPDrLeirJE16MQshirj2QYquJNjA6bvSmFWRaKuRFPuzC--CnUVKD0o3rEoWCtfmyB45LyuM6SLIJTX_0_MB1bhKVE1UUZX6bmcbuFqqj9ZqRVkzkA9IOs7Q1fPFNTpQ2Fipwn64ordtJ2s5ayISMtvTnctLrt2RyxdMA3geO_8kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=Cfir-KK1vXbvxY_W2r_aXhItCQ8Flau3HqqNqFzKDPrtZQRRScFoau9TERt4Xe1goEM3NpwvKARqwctlAQQas6gI_YuVQHi0NlQkHf13IIDMLNajvW3DrgZ0XrQL9_P60XV-e1yrBPTB56UR1lYet2X4NPo_WaUuUJSk4riqeThXV2Ib0GkUxcr8JfZ1_nK2-QHwB4_PUAwfpYovRimAeu6tJmvAQIt6_9cm1GJyyK-R2grQemcW4E7ijUJ9i-V55eXa_ndWePnZhM2bCkqiFSbPK6znXe7JLGqr3z3JMKk5OQxKchrEuIjUYto7xQYtEvQvuPrDTVKDJM8e9W1HjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=Cfir-KK1vXbvxY_W2r_aXhItCQ8Flau3HqqNqFzKDPrtZQRRScFoau9TERt4Xe1goEM3NpwvKARqwctlAQQas6gI_YuVQHi0NlQkHf13IIDMLNajvW3DrgZ0XrQL9_P60XV-e1yrBPTB56UR1lYet2X4NPo_WaUuUJSk4riqeThXV2Ib0GkUxcr8JfZ1_nK2-QHwB4_PUAwfpYovRimAeu6tJmvAQIt6_9cm1GJyyK-R2grQemcW4E7ijUJ9i-V55eXa_ndWePnZhM2bCkqiFSbPK6znXe7JLGqr3z3JMKk5OQxKchrEuIjUYto7xQYtEvQvuPrDTVKDJM8e9W1HjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=r4bUZPY0g-5JLwvl-6wWv5GqqAW-ti1jZ1K6gNmhIxsmiSRWZymdv9xj1watcP8Um11nYNk4w9gCnc-7kRu8llQxzfIZtZ6cW23H3n99ka2cvdDue1aMuqN0e5WB3saceIk2OogNnOfygxBaW38ZP4tuF4AFkD_p8NTxrn_yF_RstBpuUsy88545n2ychJUaR1rfseWR1NZ4drQUO7T6Xw-YhfbzwFynVm93MpsY0X6UoV5YcgIYLoCmiw5T5Y89DrtSl3tXJyFkPahLzXE96q-fH7BZ0HfJkTDaqLs6IpeOoKl2aJ853cgvUoB5Zv-BOgIXFSzwGU7dLez7JrI4jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=r4bUZPY0g-5JLwvl-6wWv5GqqAW-ti1jZ1K6gNmhIxsmiSRWZymdv9xj1watcP8Um11nYNk4w9gCnc-7kRu8llQxzfIZtZ6cW23H3n99ka2cvdDue1aMuqN0e5WB3saceIk2OogNnOfygxBaW38ZP4tuF4AFkD_p8NTxrn_yF_RstBpuUsy88545n2ychJUaR1rfseWR1NZ4drQUO7T6Xw-YhfbzwFynVm93MpsY0X6UoV5YcgIYLoCmiw5T5Y89DrtSl3tXJyFkPahLzXE96q-fH7BZ0HfJkTDaqLs6IpeOoKl2aJ853cgvUoB5Zv-BOgIXFSzwGU7dLez7JrI4jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9nE81SsmcR-sJEAiqXX4rPhS1szQWRLRFCl4iQ3QwlDjVNI_Dbg50iLdkghPMplR5z6aYTgUpHmUI0ue2gNnVidpudR3OrxGNLxfEzQCZ6yHA6JA9hDaNt_iMuHfaIU8AZgJe-8U28PrV7pkM8Ft_D0XYtnUWz2IAgFOGL6gmDrOSe3eoErzswk_VGEz2WPYolKHPFrVVVQQxdypVpYoNP7fVgAibcnyK8ycfl8mUR6905YmNq_0ycJ2vE3fX0Dk0fxdwmt3lvrYFrTqV-FvMX1xOJ_32GEZ9jx1501d1kg0f2cLhp-FDE0km_4jo_2tUHIX8HOEqiBDvFwBYLr9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTt8gZQaqo3KL-27p1zunUfbxcuXmRzBlYdqKb1enIRBaLyUd1S5-mlWYHsZTNoQM6kyBgS0rjpOn9dlkXDb7-5jPh6pAFTOKaFeAcvhM1r24RPxq8Y2vUwy5RZ5OjhkyVs81JNQfV_YDlKSesIecqIN8EYq_CtJp21C7ZIYDrM9vG6566FW84jS3DuVP1j7XPPblJHfC56nUw7jggxRa4DD9YykwvnZNDeEr8pVo5dhF3GY6zZoIzoGVnWqjnR4vclYwKWV_oEWVfsrNmIdURqKiqmmcmvFTNXBSNMcbOBooceY2SRKXCp0sjc9b5SdSUO8wVtKCZmycNUp35dfpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHgCH1VJrPsosynt0hiccJsuDZh4Ipv-gcOuNE0KEz-oFaDoxcFdc5yKP9OZ5vZdtuqkoaQdHD5LqQJRSuZj_maM5o7cEjKhlVGGK4H1O6NxExbq_BLsDTI_MdI3e48n68gGJtaFFrkEK3PzsYiUzfvN4IT8SSoD-HtW_kEwzJh1CF9-19A98B5V8jNOcdiiOsWF3xdFVNPDpRf9NhfvHQYaLLox6EPT_jrBr4Gg66eii6-D715ovVELaSFpkFGk26hnsdKhnoy5bc4r2riNw49kIeOhTVg3QpxpgNfHi0I6Mf1YWzh8tqomuug4FJXSTbUwUJ2szF3TwkvP2ELagQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSHqOEcY4jKlAdpWE04rIGTRfUx6z6Pu4JHZ80kM_SX0CETMB_nCtL8l3ssm9UkzwHndunAblaratAvEaiL83A9qiUZcR1OPogrx1D_3QAwLJf4gcN3wfP5Pj3TDo_gDqs_XfSeYZmQTqKD-7DOAWbwuyXdOrv6ajno2kRxiUwuD6O5TgfqjfZ1AYYpNXV6D3wT4ZztU-1MmhZbTn-Z0DnHWi4WTQUx0ZkfRSzf8mRdsnTs54yVYrhck8r_aDTicGiuGI2HbQLpQVeg4Wq4NNyusyYgVC3hmOiKue7404u-y22Xlf6XO7Yf6zLgLuIG0bg83FxckzOeumsmxjvDQLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EA3Wghfyqvbw1zu2envq5eGlmYrdi_YjpnGszfcCtEq-74MRK6gPMVPrXzxbYTz2uEcgEqML0RUHXA0KGvMQQoqkqlav-H0uKNx3aRvGWyrtyNh_nsrk3Fnt-jU9Vo7Xuap-sIxYxwYTmH83-WSNc1zB2pTYfJTLOEX04ev9UqynG4wSuBrrqkI8tcMO5CNw8eqJEkSvrOabtn5ug2WAZ7kgSM1m1CsmFReOjlGhI2dFrDANA-G30O0j1G0HgaM4AYhSLJ-cyDODanReM_2u3-dlKoya42fOYA5LJYqejkw-Nnj2Io-hDHKg273VNCZ_AskIeTPlBmN48WEAJh-xlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqFP7BASDw3AFEFrFTIIijcV22O3cOMwFyUrcx9jOiItnwSYSBN00kPJrMRnj-CMc_T7ULkZA_I869tSIBOPnBTfCkhis-ENUwjm7WnVc2ie1qrOQvvuAAbzlxT3IwiLpBJohKQEn8LUagbUG_b5Ywx878dZoyc6ioYTME60bNMBXgyRiJl4tqNFOBJxLg1GPuwFtzDVo2EsXNsrKl_MhjAkiROhCjfK7p3timkKTQvHydSvdSDBQu_dmNMa4sXWs8EVp0-Be5mSQvKnVUV0-e629FpWI5qc2LEvm9JetnLos5dlow9wnfkPgiUUpYVCvlLnsZenggQdXCj_0I1dVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWug2Gyy7yb-GodsvXGJHz6bwHVCG64VmfUXFydZuZgFUcBLZnDS1Y_JXkxarjduxIhNxR6AwQtPtp00fGEzsrSTw7ycUAoda85MOLfGQGjhQV17FraFg1ho2rfZWKJJJxxuMlAUDYa1yGvONixCEc9CMUk_mrWR_9MLofnW-pAOstVuHzLRn0Buq1tvZ8YvMiDSWtoEwwLamI_frUVjVbEQpFqUfWmwWqcDQlWq2zdxCNQ9-jsT9zHc6rdIZH3vyGX5Ys3WcWeb8DBrhgI83M_KY9awQjlo-Cm4a6SIQMTdHdf2jnvNHu0imxsYcykcXvZGyaJb2DN2v_Kn-bzaQA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=tV3wEmK44kLYaaXcVJ7Y8tFBbBq7DB6oMD2yirG1LmUErf44X8FO4UD4hvOcn6ha_6YNoba-DeX6UfteUbQYcVo9ek4fjNqNBMlQ7HX9A9Py8zYJzVO4b6eRCgAdPpa7ae8IkkCUUUfO99grUMCx2K8Qzu2vTngdhrOsY1V6XGotXpthhxjL856ZXTD4btp9vURMMY59_p0vYOrrXr5zgmz8NycJp2mJhSLOAeMGtRJrAFCUiXAv5d-uEHarRFAIfjCrkguwipzwnHTN7BzNHy9RPkP-N66_pn-3Vyv06eeehkz39taasUe5u85D5ppUI5zCvw6sG_GlZN4dggn6lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=tV3wEmK44kLYaaXcVJ7Y8tFBbBq7DB6oMD2yirG1LmUErf44X8FO4UD4hvOcn6ha_6YNoba-DeX6UfteUbQYcVo9ek4fjNqNBMlQ7HX9A9Py8zYJzVO4b6eRCgAdPpa7ae8IkkCUUUfO99grUMCx2K8Qzu2vTngdhrOsY1V6XGotXpthhxjL856ZXTD4btp9vURMMY59_p0vYOrrXr5zgmz8NycJp2mJhSLOAeMGtRJrAFCUiXAv5d-uEHarRFAIfjCrkguwipzwnHTN7BzNHy9RPkP-N66_pn-3Vyv06eeehkz39taasUe5u85D5ppUI5zCvw6sG_GlZN4dggn6lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=o1C1ITHRcw0ZeDsTGqVpxY-Ns49ZqamTkat7qmTJx6Aizx3wXiweJKM6N8dgYTziieZYMyhmbEd3zLRGKLS-uq3Ahn44-mh3OTgXKGOAKu7qs_xeYqzsnce2pWHG8cF1EhpxtmUpMak84mwzGaaMIruJZo-PunlC4yu2KThiG2mkxGI4XOXrd63XjdKPzrL0UIJBSDw5QBtxAC95ZhdtbMDl_r3k6a-XkaMhPTkdDNpUWF_wQu9PCsgnAwEArlYeh1g_Eike7AaCfNR2D68AEQpxh7aC52o2OakNP7aoAZPsVpwuVF2JZeQLwRtXC2nhDK86wenSzH3xGhA83coG3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=o1C1ITHRcw0ZeDsTGqVpxY-Ns49ZqamTkat7qmTJx6Aizx3wXiweJKM6N8dgYTziieZYMyhmbEd3zLRGKLS-uq3Ahn44-mh3OTgXKGOAKu7qs_xeYqzsnce2pWHG8cF1EhpxtmUpMak84mwzGaaMIruJZo-PunlC4yu2KThiG2mkxGI4XOXrd63XjdKPzrL0UIJBSDw5QBtxAC95ZhdtbMDl_r3k6a-XkaMhPTkdDNpUWF_wQu9PCsgnAwEArlYeh1g_Eike7AaCfNR2D68AEQpxh7aC52o2OakNP7aoAZPsVpwuVF2JZeQLwRtXC2nhDK86wenSzH3xGhA83coG3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=ENvUtdxQrPISGRjXpGLl3ekTXjkKpf1gdOJVfaM8XNktw-4XJ3HgXwEO_hWvKU8V3xVcT4gl82ciuCvg-oa2kDnhUifUAKNpzzWuXWXoZxjAv_SVOAj59Ao4AJOlfghr8FJ9zqKKWXLFQwF_cj7WkH0sMdAzGqBlJ5Ef8EXv2QeoWRfqtXEkTLVjhuT_LfDau_6pnNe66nlWxjQ_uZ9jKtj9IJF7Rgv3J5WXo2JQNGFeVYFnxzs5lOLjQ4MfdxHLjTx43scJQ4Kw0HybNdaYqjAN0pIlYEzJhYFopnvjH1HSYuWqBtFp3cjm4M-vXNyLqvvYbCNOYznikLy6IOF4mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=ENvUtdxQrPISGRjXpGLl3ekTXjkKpf1gdOJVfaM8XNktw-4XJ3HgXwEO_hWvKU8V3xVcT4gl82ciuCvg-oa2kDnhUifUAKNpzzWuXWXoZxjAv_SVOAj59Ao4AJOlfghr8FJ9zqKKWXLFQwF_cj7WkH0sMdAzGqBlJ5Ef8EXv2QeoWRfqtXEkTLVjhuT_LfDau_6pnNe66nlWxjQ_uZ9jKtj9IJF7Rgv3J5WXo2JQNGFeVYFnxzs5lOLjQ4MfdxHLjTx43scJQ4Kw0HybNdaYqjAN0pIlYEzJhYFopnvjH1HSYuWqBtFp3cjm4M-vXNyLqvvYbCNOYznikLy6IOF4mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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

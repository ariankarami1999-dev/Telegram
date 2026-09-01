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
<img src="https://cdn4.telesco.pe/file/XB2ythHcej57DlD7JhmuDuU8mbhG5ZetExkrw9SfezzBic6ya87Eh5W4z7MBG831jUAENXyuRqTRFjDTYPX8kFuva4C5IyDxeP1aHvoPwjpnJTyrMWfS38HNBN3D0bRFOG3a0skbTmQEe8y2i02X27AJnZe-phrt5Fp9CyoIUbuBKgbTGOHxo5e5fJABkD57tyo_RTA56V9kWbYZSbpAkyImkLzac12o3hJUvkGcdrtQ38ub7jbWzBjIw5xPIKP8hN5KjL1JODIEVyIrtOL86k8bwF0xY3lH3FN09tcOi17n7kjbibPLWh-LSK2egiKSmDMuqYuzH1x4rsz8ujp8-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.6K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 04:27:56</div>
<hr>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_Uljm4Zx2Fz1dqPll7bLv_fMbk-8spyxFUmUPv-h6w8B-bqc7wh4YBeps-UNGo5AmPyeE2pukq8q5iPEq1eOL4QDn4GXzvEeKNeu9EQb0VwTp4d4llVvJG_mKuHoMmggpNeIMGQfGTpss4ZlDd9vsuSvq5Mgr4V14oxGIZyKYPd6JXcUV76wc7JwbhqQMfunF1gZ259HUxNjA1ymY54FNo9rPHbhXfCQQlTNMjQAl95Z3I6SWNsGaNiwGqBzvQqrUixJVLenYYSy3bGenhqpHus2n77Pa-rSito2fRadR6cYLs3INeHKlPXLn7Q-DHHhluOk5c0imrqJ9_cigU7wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=HsHTvMPf17IsN775MwKaOnWmvK7F1123JBryAR-JHZsohtZcenB9_pkKZOThH7F1pTn495XvVqzwvL6InMvpzV0tx5fSADVu1OOSswGVokKx4hxGOhMNHBa23ZNAJYzdsnklcAylh7gBEicmdIkE6dx5u6cZFKIMYLHu6-38r6_LHT5feO584P-Lhoop8Uwgi-WtGx_lPrTWfi58PPQDMHw9sshaCt2MgzOttVlerVketzlKZ--BZQOcxrGQ1SNxjDmEocT8cjChH1K_92wrY2aef7g8tIRGjB8Y59PUZ3od36cWf6XPwjY-lLW5DeOIOtnk9oWVoBNF-fnaC0MNOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=HsHTvMPf17IsN775MwKaOnWmvK7F1123JBryAR-JHZsohtZcenB9_pkKZOThH7F1pTn495XvVqzwvL6InMvpzV0tx5fSADVu1OOSswGVokKx4hxGOhMNHBa23ZNAJYzdsnklcAylh7gBEicmdIkE6dx5u6cZFKIMYLHu6-38r6_LHT5feO584P-Lhoop8Uwgi-WtGx_lPrTWfi58PPQDMHw9sshaCt2MgzOttVlerVketzlKZ--BZQOcxrGQ1SNxjDmEocT8cjChH1K_92wrY2aef7g8tIRGjB8Y59PUZ3od36cWf6XPwjY-lLW5DeOIOtnk9oWVoBNF-fnaC0MNOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=YiHWVco3cExOOjFoq8nm_05Nwr2xUQORAqaPjyoLjEtZp23_QCbm9nKtXnzAoAGqKJjUASNXQ_rfO1R5EjVQ2Q4plU8lF7tU3zU_ZIK4igMz6mTKShfcbzSqRR5pn6MD9XcWMncGW7OC0YYjwH2smZU_vay2oxsWSOb1wr0HEAOceueRtV3WS2CD6HtbovY3TeEvmmwP-LS9D20kS1h9trLqzeA95Z1w1awijcVzt4vearMVZbxVRRRq2oWRXRUpt6ee326BGJVZo-84o-MupHnEQO33AX7p-EZPKQA8HFwBN0xkFp56PS3Dz6aw3c77PyI2urZQwiweFKhvNyRlUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=YiHWVco3cExOOjFoq8nm_05Nwr2xUQORAqaPjyoLjEtZp23_QCbm9nKtXnzAoAGqKJjUASNXQ_rfO1R5EjVQ2Q4plU8lF7tU3zU_ZIK4igMz6mTKShfcbzSqRR5pn6MD9XcWMncGW7OC0YYjwH2smZU_vay2oxsWSOb1wr0HEAOceueRtV3WS2CD6HtbovY3TeEvmmwP-LS9D20kS1h9trLqzeA95Z1w1awijcVzt4vearMVZbxVRRRq2oWRXRUpt6ee326BGJVZo-84o-MupHnEQO33AX7p-EZPKQA8HFwBN0xkFp56PS3Dz6aw3c77PyI2urZQwiweFKhvNyRlUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUyRcX9XGqv_yzGyU3aTCxfsQ2DV1JQFncQVA8sdBMeEtr2SdybF-wakj9Np6JI4M1KI5gY_UCb_s5eKvXlph_I6gCkajKIlSakTaCw7hetO-arljL3-Sqe5_wqd7sBjwffPJyMUGbUjyGNco8iI7va9xdOTvyo7vGEmG9FLr7RKj4znoTESUzoDz_dtjhhZFDRTrbV4HGbS0_bY6vOYvtLkiTvcUptEb4adED9iutV0NmkFZZvRfKmvqiQEPZwrltkzH-dsnj37nh_Ft8jv7OQOSQSsVpi-2ap2fa7EYe2hiMFdHoZ4td9RjZ1GkOI355uXvOsL52PL5T_BqU6txQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iv3_swxgGbeAN4vCo6ax9guy0BVUzGe7D1qeS6OnU8DLHFV9jh8Z9wZvoahy7Ya1k40uGZjlqPGxXYV1dBowwo9adZqpCj6Pxp0Aq9z-Dkx9dzqPXvbpmBFJ_8e3d-41Y0yfcIR_-6OL7khp-PmwNldZcyDK4aP34HtZ8Ck84MMMoNj2yOSbfRRC-AwsxVX_gnaxhoRkX2DOv26LOZ_cho9nyrlCCrQrshO5udPV4lD90WQFzJhHbjIB5bxTQAbLYsGlQudmWuQxq30s1hm36Om1jOb9eRAsLFMU7zH9eJLjkdFuZEkHx-6tdxy9RhraDr00ywsOGiMNycB451Ilug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEzM2lQQpXMbr4EzEqQGCDjE5915gjR9UsgYOsPiryq5OKZsOIHdkI0IuNtISM7AJpnhOVaCXD9QHpUpfD5-L2d278g3SKt-tMqwJO1LSJMdbzrD6EPvjBvIcLB9YfmKYjnVpvPstd0MhmTRiJGoF7qFafkv4KlRFDMO8RR7ndt1fEl2kSnXjk8EQc5xRcTTiWLtz-NGVxtXlSOXmjOojZcJP_6AcnHGdbBvWEReJbrMjXGiwsBrZtHxJLFMc24jpErLg3BuYS9T-F0H6C9lPnGHu5rPj5Dpa-uYfvtDYqYkQx9D3ulEw_Gje0q9j2mkglE_VHUrOmm1IzdjDqPcIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEgBPAxlsTAM7E7E9j7JVFNj3NU6G1qrlJIXT3NZB25fCpFYDTwn60ELPxNbOtuhFZInXgdO9hYKv9bCOxgWPQ08ndjBHQtV0YSaAb1wdjfd2o6WulSNAlwkI0KpPfe5kUIHzEX8IWR31DCZnzGhvNp4UxX0vn5MJFWnmdcN_TcOeMa1SmERSwkUuq52Rm_3yFAi71LbLvP68qezEIMqX2h-xuh76WwVK4pzz3wibmUhAxWq9WjBdMDH5lWeJBM3UcJX_pxINTTzb-zPdd-0NpQQebXP1l_wzysw5qMRZFWhz-5qE9NIQrmIS2A2h2glA8rDiiClylsMirJ_P-kkKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSnAG0UEoU6hw6xR9H7dfpd4waX63lchhKQ8DwNzQRklC9ev4E8Zvw8c-Dt2H4Fj0MyQn396TG_Ja1agBh_dsol8NkED7c8VOfgft7bt84jwdyzKhgxmgMl07Ome3n0IOwGFkZQ3-bz7XepjT9_RSKQv4Osn327XKIJYW3Jjp7EfJU9LQEpHHI4zlEye8SKmLO7dmmuMieJG6oL4dzGGo2ThRNyRFotpS4Nb4OwU1A15D1O4gWVVATA26hICISJqCoUlZnb4z1YVerK-A-K-BleMQslgRXnmGR5G2iBt_2XYw5ZNjVN7W7DtmGA66zW-h6WB57-UFyNu1__rV_tFmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpC8BbFsL13pV-XuR_aT_ZLgu12s6ydbri2e1sEar4W1wjZXTe8xN1ATa0xjW7MKRdEPhQYW6qIrqIncjbp5pDlEAt0pE-pOmpBaiexwDLYFnI02SnOPTKnPV4c8RKdWHX-ylvM-mqxe-9ZP2TqpMHq_pY5u5jV1acQgLxjSEyOskVaHk1WOtcXz5CJy0ddF7paX3TzCN5i5kU7ZXFmeuPrOA-WEq3raAmP8mOnMnh1tbudnw32y3vE0uJkl3KFRCB5IA8LocOQiNr4AwWenIxS6k9HsU-dGbtLveYHpLmTVmvrUPAHl0OobKXXsG8I5DrKaPXj5Aw5ymfOZXWz4QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=WnGf4R7mK8dtQ9ZIm-0rPjVl0X46Rtx6P09-pFeidf69FP6Xh_aFxCXXeMFZxd5nqXg_FqcGUDASUrQVZR_Iy82LBpcC16hiyCXBdQ2CMiqQsmBYCekWo4UTyXUkZfHerU97MAyaHQD7-Nd88gA7MbwDq4CiX7YWyR6IM2vvh3j5SND967Lyb2-oqtVuy29QfQuQnUGj8E3_4cHdEEztnb-YdTUWK7x9fsdPxL27AyQ0rfPswdY52ycXely9k_cDItHryWSQZHnHabIIysE8BUL8x68FDNsxjktWNsz6cA-bqq2LQQ06YXITwRSETzgWPtH3HnrnTLc9MesZC1K_Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=WnGf4R7mK8dtQ9ZIm-0rPjVl0X46Rtx6P09-pFeidf69FP6Xh_aFxCXXeMFZxd5nqXg_FqcGUDASUrQVZR_Iy82LBpcC16hiyCXBdQ2CMiqQsmBYCekWo4UTyXUkZfHerU97MAyaHQD7-Nd88gA7MbwDq4CiX7YWyR6IM2vvh3j5SND967Lyb2-oqtVuy29QfQuQnUGj8E3_4cHdEEztnb-YdTUWK7x9fsdPxL27AyQ0rfPswdY52ycXely9k_cDItHryWSQZHnHabIIysE8BUL8x68FDNsxjktWNsz6cA-bqq2LQQ06YXITwRSETzgWPtH3HnrnTLc9MesZC1K_Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvRBQ8NHwhfUbOhqJkT5V-FV1mYtxot1nznGleZTemuWyJ1eAEMqwZQuAeveoa9SGjapruC9KlnO-IC6OmJd1FJOwhTqaxnOyKXFQfdxuYElvkYlHwN48P01OCTcjmYn5NsFVnjtcUB7QUsNSpYY4dfqVsNyy1XdTBYvnhzeBJZe6yV13Sc9lNSaPJ2oK6lFGDsn6AwYEx5Ni8tr_mdFLTZIp8bxxq1xOSEiUxV_uGiqBVWtxFgCFbAGpeo4xRoUzGikwyd4Mmzk-1Lxyu0k1Mc8c5OZNYN8gS-SiiG_GUI4ENGb4yNLS6ItEWyyYSBg1GAkAsQQaCHl8CyDdsGVYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=a2bdzsbq7eX0PdPDE3FRuD4Gyxl16z1kqnXO-pxdBE57KmXJvGuJ-kDD1E72YgG1m0MRVnMk2CoXe-mIhjfo21zptmLFsho1-juoHwm139WKxZPwvfYjlVz-61ZP3exr2bPsIk8Wf16fIHOQ7aCMnF4cJnkLFTPg0R3SUXf8QrRDbtHPBi17MeMnYWIpt3u99HJ3DRuKuLKl_mW_jqo2a8bvsWgyZlm0QvTkbR3zTKBE2t-HxpAzmdHPineHspeBSf41G4japNOkelLnWvbC5H1l2HJoZEQ3WbvHqgpy9LPle2GcqW5uJX1ZVYJvfvp0OAVbR_3lCz2pOVXFmWFvpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=a2bdzsbq7eX0PdPDE3FRuD4Gyxl16z1kqnXO-pxdBE57KmXJvGuJ-kDD1E72YgG1m0MRVnMk2CoXe-mIhjfo21zptmLFsho1-juoHwm139WKxZPwvfYjlVz-61ZP3exr2bPsIk8Wf16fIHOQ7aCMnF4cJnkLFTPg0R3SUXf8QrRDbtHPBi17MeMnYWIpt3u99HJ3DRuKuLKl_mW_jqo2a8bvsWgyZlm0QvTkbR3zTKBE2t-HxpAzmdHPineHspeBSf41G4japNOkelLnWvbC5H1l2HJoZEQ3WbvHqgpy9LPle2GcqW5uJX1ZVYJvfvp0OAVbR_3lCz2pOVXFmWFvpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=nfrEpT-JrxHnX01m20nCAwVYV654m0whkXhnIN9MTJaPg72NRBwsFtegJYEG_wlIRoG4RdhjCbPE22edBtBMbdhmnY271ndltwN4ITUEoPnaLJXpociGjckdCh4mgAKaKsK3EYijpteZcsiuKls4b7EhPFn3ddXGhQNxbFpoRlyLlT8gA0YvDiDkwWvmzXYp3a3dTQFG0hIRI6dMCDVk0KIQtyC99LWU15_CAAuwXm0j3xpPE07nL2gVjZVxDUsC0xuxePZ2VqEXNHxZ-V7JQsyjMr9c9SDsjydrVskR-Zpkfkz8BbZbT8jZ7c7Z_1jnKXxcFUlBc8IrdIe_5jwXSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=nfrEpT-JrxHnX01m20nCAwVYV654m0whkXhnIN9MTJaPg72NRBwsFtegJYEG_wlIRoG4RdhjCbPE22edBtBMbdhmnY271ndltwN4ITUEoPnaLJXpociGjckdCh4mgAKaKsK3EYijpteZcsiuKls4b7EhPFn3ddXGhQNxbFpoRlyLlT8gA0YvDiDkwWvmzXYp3a3dTQFG0hIRI6dMCDVk0KIQtyC99LWU15_CAAuwXm0j3xpPE07nL2gVjZVxDUsC0xuxePZ2VqEXNHxZ-V7JQsyjMr9c9SDsjydrVskR-Zpkfkz8BbZbT8jZ7c7Z_1jnKXxcFUlBc8IrdIe_5jwXSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dG-LphQoTR5T092ojTU417nZ5ZNwuLHgAMIGosCkm3S7rZs-KdlUMpUrzrAOiFarjrUrARfctqBw91QP__JSY3u4TK_o_m2vsgLaLMNAW-3n5bj5UaK6OgDb9zMSncwXIQPFaJBFQ-KJsCEUN70A4x0ReQKfBAQkRQLw2Lp3ZCtclt1eTHJrIaG1DAWT3U5_GW_XL8nijD-qqDJ1zGURUIanA5zwNqqD5Tvdt500AM_R7wIsz9ZVc-3Qxy3KMOXM4i0CANdw40YeMsPgZIbQueI7XX4vZHsSi8nqNOerDGWVUMYCVfGWS5My9WYMrm4mWOjb23WBavH2epzZQF9Umw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmzxDGJMseBc0ZBSc85eF24sCYMLxxMw_30qCOQXUvX-jFao1CY82yFzYACzKX3-GUye216LFYulLmBgOdg0qFKsOLsVNZVJvL7C67hSP6D_SUsO3RdpUiXs2evS9hvfBHRaC_TPX38vVPTmhyZiPrnzrxgYXzXuo1Wgb0EbR1x72n1ZuTBrgJa0ll7l2gzfhFRAdrizDqeCWLllUHMmLCQQ_nnEe8tnMpoWH6xKfn5UiqDIMdmc-E0wqd0l9nyVH4uD6EspTWRzYbr6798WKIESSTv6hJMrcP6F_pJ-nlFU8QTNIKyK7ZcWAcLYQi3945Yh05QGjqGyDvFsqtl_PA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=uj9hl-bQNAlbcbzNXL9sAR8QIm2I-FipFdb6Hqkh6e5u-MmWXD8cp2W8qXc6Yrzm9eilmi-x7Wpa8aZxw8E2TWyi02p_vWJ3yz9OBW1VTpAzri0Ad90oLPNygZutQ15f0a7RSHC1xcpP2kM_TGgM0YrPAgCd97kBpocwbKgab1b-CTA7qsOIX5XnL4CAkKCa4vU3nxYj70Sx3OIpGy802qJXyEnbWqLbavJ-2DmvcKodY9JiyPXG3S0U0eYS3gt34T3P4uGrE0Z0lXFEm07bcUkF0j0s61XGiPSJtkSFKtUT3LSZDdkuGMMdANYFqfiRHnPGgIKca7l7N-xdeKRsJQhbPS8s1sfmFH_cR7dOFfnJqmg4o02yLe53raxd0Yx4YmuXdvjII7UfhB0o9mvq4FyRkoJJ3wQzfaR1tKyB1fOjIkMV0LQvVHB5czDGoPVwzchBJuwlLTXeRwVvQXcio4Hqn1JBCAYDXJl7NFNb7TZUIBk5up3WGbu4ge4cQZg4bNn484QWztIva2nRiU1mMKx_e-NbgYAqOk-0AYFF_QG_oLuHaq2tcS2DO10lIeiQrLTlnWWcuzUQ3-iW6zNEtT2Z18hzy4FxP5Ep2nCPOkybpIgU9XxfLstKNtCD_4KP4psEzEaNfjzQQi2maKHh-FhmMn0wx8c7e14BLtNHA1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=uj9hl-bQNAlbcbzNXL9sAR8QIm2I-FipFdb6Hqkh6e5u-MmWXD8cp2W8qXc6Yrzm9eilmi-x7Wpa8aZxw8E2TWyi02p_vWJ3yz9OBW1VTpAzri0Ad90oLPNygZutQ15f0a7RSHC1xcpP2kM_TGgM0YrPAgCd97kBpocwbKgab1b-CTA7qsOIX5XnL4CAkKCa4vU3nxYj70Sx3OIpGy802qJXyEnbWqLbavJ-2DmvcKodY9JiyPXG3S0U0eYS3gt34T3P4uGrE0Z0lXFEm07bcUkF0j0s61XGiPSJtkSFKtUT3LSZDdkuGMMdANYFqfiRHnPGgIKca7l7N-xdeKRsJQhbPS8s1sfmFH_cR7dOFfnJqmg4o02yLe53raxd0Yx4YmuXdvjII7UfhB0o9mvq4FyRkoJJ3wQzfaR1tKyB1fOjIkMV0LQvVHB5czDGoPVwzchBJuwlLTXeRwVvQXcio4Hqn1JBCAYDXJl7NFNb7TZUIBk5up3WGbu4ge4cQZg4bNn484QWztIva2nRiU1mMKx_e-NbgYAqOk-0AYFF_QG_oLuHaq2tcS2DO10lIeiQrLTlnWWcuzUQ3-iW6zNEtT2Z18hzy4FxP5Ep2nCPOkybpIgU9XxfLstKNtCD_4KP4psEzEaNfjzQQi2maKHh-FhmMn0wx8c7e14BLtNHA1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8aBgQp3r1X5JQ-eVcjM5T12Bv4t64E6rLKLub7NTb_rYC02oQXMOy0EqE87QE1YfqLsx8zyW32z4AfbCHyoQjwZuk38Aj7nghLjoFZ_uNHHJp6IsNwH63lwbfNgf277-kW_mIvVIb-fHAnf8f800yDDYcKE-gp3-oDyOxFIn3gbvFK8t1fgTer7kp_QkQTDNkTArdrNHLy43ivSb0Z6gYM7hpc7-QaZCQqbv6m5oOVkdbUk04yrB3K1V6uG0Xie1mE3GoHFHJOZDf-Mt8s7UGLjJmzj0heRvl-ZCtB-85CfYV9HU_yVx2sz1nkrIaNfUceG_9UbzFjY5jAJmYUp_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=m6GKe1fobJovd4VEfFTFJbyE7K4ALkXRRjZo_5X2JpF9Eznu5p0ka_CDFLVNMoM3vL968xWypvga_40IGaMZnDDOwhOuQIA7UmcUluVwO8U3cwH9G93v0vdWR2nPoBI45O_P8bO08EeaVfIzbkzHZZo_hyB2urlz5-pZa5A_BRdguaYVJLWCDJ1gm5a25IHcgIOWb3okdNKkSXVHK_IdWLd4Ufv0McM8ZiJcgLbQ1yMkNeF5O6R4DHTZ5dbt1K1me4831tmBjblLQMI7wGIyC2tAII7Cyz3N3jNqmghbKbhuDCqsTmZwfxCttnfslcFoL3OMEb8Sn7WpVnr3WEtoG1pFlT4a-D1dt9Z2a_E7nNK7ugOvyESeE5wA_iHKFpcLcb8fMCT5QRZPooyfBppp999FfG3d-UbvDy2p5BsXVa3hAI1JnT6ohGw5up0oRtEnswGTWoyaQF7zxX_mMGBYy-nBny68Q5YR_UyVxxG2EsFyF2hxMfLeEKuxghRd1q6etvSv4FdHP4MCJ1jwkVo9lKC__PzvP4STbs4PAbA9nD3MvhD-VdXyBtvZcnMjO7lzKj0MwM1alghuWPBFx94rsM0ZpRlukxVhGSorGLJuxGLftTdB94YMpxyCvdY2NePsskGRtzJU30AzCXg0PbSfmwgzaq4w_1ydQiqg8WtLNL8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=m6GKe1fobJovd4VEfFTFJbyE7K4ALkXRRjZo_5X2JpF9Eznu5p0ka_CDFLVNMoM3vL968xWypvga_40IGaMZnDDOwhOuQIA7UmcUluVwO8U3cwH9G93v0vdWR2nPoBI45O_P8bO08EeaVfIzbkzHZZo_hyB2urlz5-pZa5A_BRdguaYVJLWCDJ1gm5a25IHcgIOWb3okdNKkSXVHK_IdWLd4Ufv0McM8ZiJcgLbQ1yMkNeF5O6R4DHTZ5dbt1K1me4831tmBjblLQMI7wGIyC2tAII7Cyz3N3jNqmghbKbhuDCqsTmZwfxCttnfslcFoL3OMEb8Sn7WpVnr3WEtoG1pFlT4a-D1dt9Z2a_E7nNK7ugOvyESeE5wA_iHKFpcLcb8fMCT5QRZPooyfBppp999FfG3d-UbvDy2p5BsXVa3hAI1JnT6ohGw5up0oRtEnswGTWoyaQF7zxX_mMGBYy-nBny68Q5YR_UyVxxG2EsFyF2hxMfLeEKuxghRd1q6etvSv4FdHP4MCJ1jwkVo9lKC__PzvP4STbs4PAbA9nD3MvhD-VdXyBtvZcnMjO7lzKj0MwM1alghuWPBFx94rsM0ZpRlukxVhGSorGLJuxGLftTdB94YMpxyCvdY2NePsskGRtzJU30AzCXg0PbSfmwgzaq4w_1ydQiqg8WtLNL8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCQCJ3EbbEiIzDuT6MxlP9YnVeQjM_iyAgZLITv382fhP8NSSsN_71npkHG5gMjgoF7JyVAXMrH6sKqyg96wU8_8c-gNFdjx22_h1f5tq_0iome6284MVnpnJs_m9EqPgWTD_PBd6sbRs_OySyJ5x4AF-wImOpf2B0QVL42FCIfSfPh2zVkEpZpoHxGl5xcTH8y_UvJLa5HvMEdCg-x-mFZHTowNbnYoc62pSDc3siNmlEUESzhAsodKKImrc4g0bgoHu7GyUNvR8DK7BNFmql_KgAC15hcpvKs9Ohqa9zBY0st1MzZ_8x4Zh_8uQteMEpYBQ5zLSMLmfLiBxyYVVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbJJ3VlFeTNwWOGos2mA8P7HMRrn3nY97KHt0O0R1xzmy4Zkeq_tJ4D886nYvXXarBJpozF3QUCiBsf6eb9ezyED2_pd8BUTyY8TxoCOvBgunjfmyGXnhnc75TiZHFfwXjw7R402lfPnY9F61TUn90b_qOmhoF2NcyoJs5wx9etlZvO42FoRBUnPIeo2EpKwC48nVZ0NfiH5Fcmx8T1zTxvYe7hThD7RJH57bXYYdPVax-ywHmrdZs1qKfi2or_SP4N6IL-zGmG9QDaaQ0uP00O6p5RPqN2oG3dt6wlWOG8CoKuIlC-XuCHBDzPa_auK1hSCiIoeG9AMNsuQDoq7Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnHQeI0Xh6so45c3sDBweiJa-qtFUfU9TAlzak6hFC7_XA3NzoVoOCQGP5lOd0f6joK-VmhekWCE6vwcffFsdhdThBnrBShPfz9C9_vfLDVYcDMBV0JcNFFK7nSY5KJ3MW8hw3hg7kKTf99RtyE8oTGhgk630ZbIb-0NO8A4wR-xFygdfHUKItfsH0pfHYEna2GemC-y3B3EAg0MgJY_9jobh8SbpUZal6gOS_B2ukvC92inZBVSoNS9zBwlagPLIwpNEt2nAMrxk2EPXVgAGwmemOuoubznl5BrFZUhJenWGbmV6Yfb39Yv4Gw3AVLsjFuKE09lu2EyNsT250GWRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iA6w9toYUdpjRi6uvWk0FJnFbtxYlo6UGEiWQhT02i7jIQCsI55AVBoSAm70a1Ap69RRQB_8QThzT7RG_6VOtp4TRBECFb1Qq8aAHZSdxzC5b_FrQMpSTT_dFzOrriElg6VtXaftXiUdVO9LELrTMPqRsFGucV4mZcIv-8ISJ66ikXUQXS61vj9-P561BASnVeh6lPoqylHucmub8MRN_Q_WMsi_zG1wm2HIH_-E3HXEsdE6inGOX8qRck9jIPxve_gQVKZHzS4zvbkkteOWdXvkSaqPGhNDcCO6JT339XsjWeVfWtBspicNqiIcdBTWjcM7A1PZgMDFa0wSLavKtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwZEFTdnNsRzACbILyW8hNdDCA-meCrJj2rauBAO7FbPw5023tMlk9LS2UQGoEM3W9dZBSG2S2XdIcP5NoFTn1YLStQ1ukCneLqrA6e-KHaEymsXrpIBtmbGQOFm4ettlUDNhlA-6SuNmDadD-Eh1nqo8xaqRT2pNZKDT7BZ_p2oRNlNel-ILYWeCRhD_ZBeLGr17Qryef2sYoIJPkZiayMKzf_o2l-laxsi4relzzzceOddWVAzG-tIkjqzQKiTrrLEoT-IQ9Sj4Q-oEUAMcnsx8ZTkPhylmybVbXwc-uJ7KItgoxmhu6tkJ5Yo3o65ajC7Nw9R3ttzZNzMxwL6Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gy-tWKj4fx3gWylj7RYlkwFXo9LLR8J-S5s-IARdZS3EofiPnciIenY5_xlzdbK6yw8gNk-uF-uiE8JtC8zxyZxNF_Q0RRdCUU4HGULkPp4pQFueSKesarIdN_NzyxNXc0c8pmGUnCzeIQu_bToXdc2QpkfqT51ykzGIK30ZiKvT0hs1YkjcWtlqtieqTZbYhmQYiBJwTbe4PrWnLCgrDnRR2u0ZSAdS0ELg9s5OU0pIaAFcn5aSNDVrfc2GH23BKRir4uA9HNnnQEe3oHqNZZ2BIp50Pp5_nb5A_Lzj55X9000-4WDBWtSaijSnJ1qjGDHwH_NV1GfFsu3qO4k9hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPIy5EN-0Ew9El2OQfkuT8zbKvpIup8TGoa9LtRA-TF-Rts7hWtF83v8GqlouhUlddMx3KdDu3lo2iNlEWHasitQlsscZFwSzrHiQft5IeFnPD3-miHlDOZ5LEy_FrgF7EZhGFwwMMdjGqXTjZ6dH7wkOBr3J5EXvlpEGo5Clw1v-lc4heheW6J2kQQSet6qsR0tVRjIfa7nZkCjEZZ2o1xmCOBOHg31TBEU0SqKUhqXJAteM_Y72-ILW4oWJCGsgvjEIDnIEJrl-zNtjYFLqm9rwIpDuYECk5_gAy6tLh-O_g9VsF6QCcoR51W_61pSoHst8WeOhHCrcCpH6Df2TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRMV8Z882k7nr8OfEOD5O7-TvMHS46bFplBQnCNxzGwt9zDTW4lYsJaSBBlX932l_pPxYTKz6EKYSi4ZVEYqx3k4zA33r53VJw9jLNq-3qiwRh_hMZu-x7sS0yql-70ih1WLaIEG3G8tdyy0sllq9HVNpXjTWkfGAQNvSw_wZoM2u-Ly1h0JjkM31KgkhmnZPnqE4ee1ZFPeqfF_5asJCaZ487xJKZGMjALVc6EDAEVGXwV1ayZpYfQeTC80i7L5yQn6NRP2WETpu95OSAAewgI9AdkoRrkFEo6SjhV1AKQEc0tB05zuZ9z_CO66rhVVKbKdzjj3O52VDKjHxOWROw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zx_267jJKdWwv2uq1aL5YqU4jv5zuD-E6qqOHnKF-K6Z1Uy-tFe0AVB0ODmaWEZANNaPDyQYRbWjGsGYAp-dSJZ65AIFTY8Ckz9dw2eTiHCHrqHL4EH3_n4YW9ifFqJl2GX1j7M4Pu-NWmm86MmIrxgKjg3q8ydxPS13IV8bKfwzoYZljPllFeiIiKU77J521JFzBIMc9ljBiId8tlParJ63chuxJejKYbjgOZCVGpYJMIb9fqVWN0kKmGa8TNdlhnLcUID87jRKXyLDcY-96dlgYdhjCTw_OG3NNbHq_BQs6BqUpAIjPPupMtPAgvYE7EKfuJrOdK_8EkoAaSAZoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qS1TkSv9NoIKUYzUGzaKAf7ykV1wvIsFyTfNMS7N3E99dWdsJQzPgh9nlAKqbaBGwyVFS_lDmVpttbRNqw1BX8ABh9cpSaKV9-cA7PqSiZRbl6qj84XgCT_o30GEqDLH9w3eLVEz4TmTYFraB5ePqqwVawccRs55aE91hB5lq-kXObbf7ZJuGYe_vliTXXLC6cl3K6-SvqvDr1ju7Jx9gErdwGEMXQe-4PnVOQkbJWIpNnA_O41rpt6i89aTU9vBDTrEIv4rLKg4chfo8zAsO03_hYfyGZgT5IPwTyPnJESoAVqmQgbu3tkTJIoCu42bV9LnrcVo1ZrN8WNht4wj-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8Zh8Uwu73VhK_Xwm8eyyMiKG1n00K6NoRH5rHmxq5qyrI3D7CLsYH42VJRiHVvYP4kPARGkm-91qPQJ1aws1_EHa6-vialiHbifQ15Xjwku6s3DpZi8mUJ6Za9yZqWpMDh8Odu_Te6gnh__vto_L-c9DhScTIh7q-WKyGnkQLsHhWUBMYCv1-B2Im9zGTzPx4twn1r6wWhtDbSsBRVmw1IvfJSz5WWYJtiTJjsklYcg3wSg2DhLukKnbsTpfhQoSsrfNdvP5k4IRzppeT5vwCoKiqM2ny_3saP66xo2mhXBGUtRNB5R8TPa9TjU05AuAbsplm8KAtmO5_8GxjaGXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFQht4Cmop1E8m-39626GqU7RtRB3uDTjT0dT-htkMvHMspn9cQlsstv-bjqRkRgpXelbQj0QrSkaY0G6uRs3s-ulSQOFruRGAH_BfypZlfY8tUtXYakThwWqxUKoLoAYAPLAo7acyCF4LJmhv8inzp1mx9RJCd2um7tzrxM5crq-w1-nYsTSIcwk_OL-9KtiCdvM_LxS1gE6NzsfZNFuntWXQTVTIotzAJU1ujyHofGph6-vQyrK2bEAXVqASVH_H1zIq3W53hEl-MoDUPnZSLI3cxVCbi87JfzTU5I68qd1QaZI_AVPVrJt1UHV-6OmVXrtGoAJhhSuZuWtRAjKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XY8Gg2hkuB6X5JqOXZVDoFXJhTcF4EBWsTFCvNFZ8kTUbeLlMUBuh7rEgs3B9GZLgChCaG_-51UMLRRWfpEJp08IbC4D_RqAy6rKRsTQAg7-h48RaC2-GCSn3lOoiuICmaXHKZ97Y7Wg9lXNXHvHz9cIFn-GQAsVKT1X-ctAtxNS4xO6IMv9aEbnkcpb40UeSYw6ETIiUX7T4Ht1PkREW-yGAzqa-Fxlt1XfjcHbq64dirJCvsgIKj6SwCOtguUzTIyK5KcnaQRy2oZNjWQJSS-UuP2Mm9X5_qh60ZelPpyW5jrG3m1k4i5jm-7YTGcv_1lUXe-Zw6ctc1BJrfzZqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIzOMCokP8l1dHZ4b8cVtGu1auM6lzZw_f_miSxcKHXrqRdGl2Rp0dOO7_DwWmAjKPIcM-KHrUqb7PkECB1mV57uP5SCrKISm7SPMMUzcb9LgMIxuQpjfp-aqhRtYvlf8XFNZCowGAke1YnDHMdQyg8C_aajrM6AkXYLw4Ado3m1WXflrvB9q-muu3EMhEMpEVFpRINPTWc8yBRNoPchPQBSIBsPbjFMI977CC5ZvIWdPBPKriNG3RKf6PRydwwR2nZW4oAtkG4E4AJLkOuLSCYSWjDMJZ0Wv7g_bq_8Dxd_jozF7c-Xd0IJg8ZoN1neWf9cuiTIUh7MJLGxHZnfSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpShpPKPzwn9W_yKlYL3lUV6dlr7ifKZcTXwNLLDBrVts8bEn1DKVnNrRSGv_Lfbfbh0pgEAVhEksGJXDAfrZUCDAne2S3FtDD_nBuP13OmYzx_b8i-JyPAQWLsEP0QkQ-rxdbDjBCmWVoxwgQWLwll8um3HMxUGEhWzRK48y_M2hGlPUeNC2AJEfJmAjeHVM5mcX3tEXksodp1cSps2JMQBBqKxBW6dhHAF9MbYff5Lz4yKBMF2PKhmAd0ADFiic-zneWXWdkR4crpfR9XPF7iG8OUT6sILcTtCivgHKnR6Pb0nDhxr3GXCFNGGL9lICSeXxeJHUM1S7fw1x6zv0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IecWnkniFgkmE6m0rwV9HML4WeIuw8Wll5Po2SQewjvZWkkx2aSy-ML8tDzIlwonKHs6Wg_sFoSS3HHB8w5WBY59cmGgJuqo4UjO8zpE2B7Gh9O2Muban03_fILWykKxbYALRJ8WKssdsnNOqaZZSOrNugYNo6EzJ70O2ns4fcfm_0wu6_9d7bLx7ZnfJKqfMRrtaN7kWZLommUmvFdcaAsKU2NiBAwqfHOlcifibml1CZPw-VmZB7yCDGyZNdF6f3pUu5NnHl7kBSQfzTttH2rQliSey3jAT70kQuPpEybcBuR00diVwRK9n9dKWzKI4tf4WZVkGiuPFU-oyeajbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AQSWI0oCUeZ-JqsH35G28JCX7AQ7hqOM0GUMZPiX3rRcSV4YvvDm_o7_2IR71GBCyGJKWQZJe9MI36QBfRWoONmbydIeUlw86x7C9RKvPc5Ta402BdB-lm7jJ4KZpY7cQL1FdNGrHGSO1TAOeqH5jEJHNUeSB8XXALhtdiMmLbTZqAUFnOMscpVO7HnhqWH5H9vk_zGdMnT6a10h1I_FBE50BKy2ebKgAQS7Ow8voiNAFft0FqttLSd-f8E0yuC0IJJjq_WjZQjaRAYQXnD6Rfcgowv87RTNqTKX-XUuTi0x1_tsASQN8Nne7UZhdgsLnUfXThQpF4W4R7mEEnveuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kCyGsisqS7zMa76kRvO2uDSl6-SppWhih3wKqLky0tm43J6gWMwvafSy47MhfQ9pPdZT4UlByNFo4D4j5Fy1s3NExVbBSOQoeZP1-OLNLbteuIx2O6F-g1_CyeX1gSpK708D6AaVtLZMb1GCTo0nLYqpDXwKPg7ElDGyeSEzi59Ye3QiZcncMqNPrYz07y_6JZrMBlgt26TJedQ7XB4zyDfyJfWkZmnFCBuapPoa1m7sY_3nPBiAoTUv38fkUot4diSLjtxfxusb2D3JkV8ow728h8zKNFyoQIzLdjSziWuT-g8DP_034XZQp-eUAPYoeteBnRyU1txQzyk1FV9sNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLFafTN1y8FxPWwqLEFsonEiXnBCkOGUMjTo5HXwIEe8Z2LmrERho9hErKq0rYJQ51jq-MVHJoUe-yHX5bQ627xwHgV--x3_T-6IGssXPM0LyqogQee39_IWDSXkmMeq78gKqX7UaFih6g7vkI7cf_r8yPHxuxq2HQoY_s4oQUQ8r3QdUqZLMwydJsXd7thKLd3A2w_2b7Qx91k2vPqlSRR8wQZMXcKLNKjrf8H2pX2G9ptMzmECOXaaViGiVT8butBLXFr8hIMntuH5Uqn7-c5xTyrOEo1hKboKrelZko1UnxrFcf8S757YQJDmk0cnvQ91zQE9qmtAizqXRqwpxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Emtaor8f9hwai-IAxVpurwtDnyRmYawmTJkD52oy8U60c49cnc3mOFfpbY_pTgWLsBPjVs9Jyh3wYTJTHcV68i9S-NDGUNNx0gbkd11lyZKaygv2iSzo4XKQlsIPJPFkeE8WwR4V5ZVJ2M06Zi97eVG3KM64a3UCg1UYH1wpRrjIjT6_zZN4WnYaxDwVujQqAkeOxbCCJC4zETG5laymotvfbHRCQiFtGwRyg8QGmiC0TB0mGhl06LvTPIG-JiLu-HPTiCkcvp5xTi8wpPQv5CiG3tGvAVLx_U1HIvqjoHDqMj2HRejA4IM7f_CegkOwwH24w1aNpJh9G2TzOFzJww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZm-5bdPeg-KL7aKTiPx8xrcGzraerhCCsBUDj4eOtBth-da4nlSRHiKeW-icfz96mWcUwCkiCvGol6VB6NdKLLVZR-TbzNcn8s5YwVvuDY1zH8kVBQI7b3WVM9GCIK0gmqYZb2hmbErZe8ZUpicSZTr6U_akk0iN_2p_BL6pKsfsG8xt3Ig_Ykpr61I3IuFj_aXpJ6Cy-nLJIoS0YDusrvbT5ROLOe6bAgyDINzTmCGld_pzYsXnU-kN6qAUd7DOmSBaqwCx1mJR3C5vb8qhcT3-xv9Cq0EbjTbGOtyctpJzoxgasjB7B-vmnUHOMY4WnqIQPgC9dTb7zS6eWZ0pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHcSSldb4Vv_RFO0C9bw6ASyjCKJAQirymnvkzdaSfaPDQywx2nrlyQ6BW2RTLy_L6LGQ8IHOAlijATp7xaXFYAC0PXsL3vApiP4Th3r0ABposf3UVxzR3wiZU4Zgmz5M8epuPnV42gEvoXL-6syVU9DZ--qUV57U1WHNbWvtO-V93dBwPLt3_WEjyWDzPfciw0ruj44aHep4A_aVEQ15kMq-qw0QyoB5nnHzJKSqsrmuac7lFRQWZtk0EnGuVPPGiF4w-bXePPXXG0KjqcVePDaRsyl82zfDHenKC0jS1PfQRE3v9J2Jr9JJEbyFjUHGU80ODH1gRaEhE_t-CcTdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ek7AtyLleZiGFEmpprj_9CWh6N2RvqPyUqreVoQwNQbZmPUQVEZOQvurZhAQEGwNp3nu90OZJCArbDVL3hQ7_n9t-UteekCK2B1veYOj-TpT6SRMghMJjbRRNVLYgKGcRjBRRsRo_OWvhogT8cZwDyfrArhonfpCyIMRrm_TvDYGVd5rC-E0ULSOaFUIrngO8p8pzPtBKNoQMfwHTSBra6gZDm1bzZoMPQQ0P8LfwFSBwVLdi0S91nuK51s6eUC57vDtiNwNtmqjilv_Gw882EXhRtooC9XiMiKsGJVA97YKgIUocAWowtjcK0CQq5pZfrXfILoyehBy1bjsT2xQfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHWULB8HYcMjnD1Yr2vuHtScxb3zR5KVvS8Pr57iPCit2Ac3ej3Rae4WF-sobrf3wtQyQ2H4THHYHAPFPRuATLUs9f2ZvzBS5KCqNk3rWnmCKFnacjyzpqQd2WsWt-1fI9eEBiFrHbvfQMXS1BgUNeHluVcPMLsNT70zRGxwk33MRH67tMBSEzVADDt5ek2zlkOeb26qk7-HyFyx9EEzDRGK6tyWuRYtP-93swKqqvZWcFspEQ-JsW6CU3VsqIv1loboWIWJl4N6CKT9j8aOp4MFWddKqpfIxtWDkGqUbLTaddiCc0wUkJY1r5tOuBI5_pP7nBWKH_v7uk75RX4eeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHquN9dRmpCfbWD7h4tHmkQhrPGvnkuVdL1n3Kom_ccZ1N0GFq8xikZHRyAlN0vm5cEdaNnICHNyOpnmFLH0UTe7AOkuVcE2Fi5voPlrB6OSNipqi0liTt_7t_cKVd0bBIYPRz3jw2BMKSSunaMlzE3-C4kvMN6C3Puu0tgudlammIQACisFmlfcQq-85JxvS0sWNwzO96JWSxmbDk2ViGB3kfFa1Up61DegQjq2bKCJmUEsLb4t1FbXWIvVdJzlNtXYZ1st5vrQ6YERdVjK1xt81hChJcuUT1kxL4BhsYbeU8qrcWOnMUDGx-dXFVrPLAMfbd_M25y9ExF8QurwwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4PQBRMP3VH8RdlQUnpQCWOW_y0AVguYtFyej2pSrcL5ASupNrU_nEOEtHuEQikYGblxktH0HbotGeT_G96VInaVa6NHNAGwjNbZsUswA92V3NjMQsfzZsHQnTLCcYF8exWSEK3MhH3ysFFgfq0SsTzqMwydKizEFGdYKviQE5AB7EpnG-e_cstYfOOVv31zwnpcg9hdfwfQVPw6OeMEzi3QvUuV4gOwQqbx-oSaho0wQtpqv0WCJqvBg1IaRE85UDrBwu6Qf8ibU33F2GGe-dx5Hct6h_nRhZR_iQkYO12T8MHrr957mZ9lugzz3tdFcEx-aSbpe_qlSARPDyFGjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIDFxw3tACjjOMeGgOypfDjuBxTMLiWWIdgTSi-cWNdvAF6VNJ9QhKuZXVcDJw_hkI-gDbspEDiCGYZ-FempmHUYLLGdcX94Q2nWwd9N4DUVNm38gwVSKBg7LsN3g52Bq8sjweQKTif8mATY73JHycV-9o5DGo5iXueKdf6RJCRVZiO2R0sNCz78q2TGiX_TqtsTS04YuAR852v3TTKB3yNDHhLAMRAlVyBsECuVuNll-g70f2sgsiCC5BV3B3N7GvFNrr1e76l1svoS3CkhQms89gO2lYtveE8J5t5BhQsjmiIlrrIabGQDgRFnILSMyYeuAm0UopIuSR7BPMXH2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6wlUScTmrwvSQa2SfkPEJCTsF_SyU94gp0PMX2XYeeiIrgnHQaAE0hTjJRuN5PLbJHGi-g-fRB7Y4h2xPeGi4Rnp-ySUlZI5_ST4tVt7KtolsABU5yDJ0R8aXnTwGuW51Dt5S4l9cAbZsvf-MS2r15aN3aCMUheP5KBUXYxaKIRAb3YgDqUs21W2JvV5wYSYYyZLEyEB3Y96eGMMEbvNUUzG2vtLcISDkie0cQe53LNH3k7WPTiXX7IlQg9cE6ORP7Q2JgX7mQ24g_lh54uCjtpoFvSH2TMFUrqExGSgZPOgdSmC7pMsQsApcAcnlJy4kiNx_TQWQm0GiknvFVY-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HhVgoHaxdI6BwU3hCQWPjqaFbW_Hy3UfboYVjfjfKGb9QPcsEgAALZMtJKc6jPVJs_xmT7KmOJkLLtFZtvJVU7oOL6YoRCpgCm8Ewbjh9-lnU-sj2M2-jPjyGC5O2pQwO3Tyz0_4NnrN7kaIQGySqnEYRBbL8CFo9H6fvdJydzBmM1XuF_lL9tLjDTwJt-j_h7XWRY47HUkiclTVnK6SPotdIOoWsCvBw6nYWAhthKjXzx42GzpFfGTr6692NMOzDE1gofbNtpTOUVleW4aKEzZeL7_-r0TcEeNhGJFASkYm221LUf-AdAJObfloHPqPfXezOJ6uqj4dvob88i3B_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPvkhJuokcQUmYTiTHIzAYZtk0ENyUDFMHB2tNEAUaz0XlROfcQGK6vVuflx6cSZZS7Wd-AEVnOjonX5I2UZMdxDGYM2l8WU5WlAFPs8GqUNXoSPZoDPVNHZCCMjoCinwfmD4Dh1zOwHnL7XksskDbkftUVJW4o-_I-28YJYiP50M8lFRWkWU_8B9MhcLExZv0batTY_rly5SKzMqZHpzhOG8UJ53Jd5HX0rtlZYPaptLbZNoIUDESdXpCRqrA4bgcEXREqw5XXQ6qMfgvv66prliwJtydCMzI0Lvi7znztVJR4Ztn1jJfTcPfPbS7jEmiAMkDYqBwWImKFhmRXlgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etotfwT0M8UJQDj_4zNZ6rOUrcT40tT2oJT50bOjgpVXKJmqdBXORry-fN7SsjcCLHP8CgVGNLvy6Ehl3A5iMN-kIjng5R86j_f_Wqi1aRsXcXk0XEzEx3ito72Q1WShhF0wxO-aVY3TKsIVv3zOVJFJpu1FCXk91EHXaWqn761n1XW2u85lASmfMbO2VKtpcZEJkUje0q3XZnOtgXIRGQEZkrOtQ2u72Hd0ZHJZUfhdoFjfapzHnhgWLBmH9awQ2G6gN8fw46Z_FhywcvjKsWCk0qURGcFkoIF0F-rHr-ZbkNToUtzGul2l7rADRrMQMqydk0sTLYz23uEAFVMGmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6dQ6I-fUKBMv8-_trDcwtoy85N4NYqeHTFVK-s16hn8wtH76hfe9ptJr2akXHQAA9ZLvVSj4LFdVZg9Ua7d0S5j60uiZ_V9oXmWJWRpjl-3t1SqqmWMCxth-Fhxzf-DRWcLZTckqZC_A6H-YkfqddTatQ6xycWVuFcObRcu1HH2WGBT8TCREWZstGyC1m8MZmp5wd30s64TBFPfpZHVPF9ffvqp29BIGZggopcD2TxXWnP1S2nbOJxs-ciQADyMKcB939-14cvyr0s1d0EYETbe9fuU2ebGw7bCti8EpQcAj9hmqUWNOtDjXrxQFMecIHUba9rc6yjh4MAaXOPKHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p53yQoyIEJn8d6SDL_Oo2-ZkgFH3TB6PCEG3zTrm8G7nbUpTRPMGORHYG392PVYHVwzf-0qK-yp55xZ-mhrGCiIAgkFuTZsEk1XOexWZdPuPsjyCPRxn22feHmuQvJYo45h9X6GMDpdpUIJupR-gPgnoDqWtvnO0WBHL0pEe0ezVoyBAKiQWWT9flBMjBLH8EVR1o95utxGOkxW6qugtOJ8OgWKKOymBGYMnwu9xApms0KWCD2BO2a8MHaE5_lA1rIVCQpgVJV61THeLhRvN71g-IN9Wdf-9g0narFWpJzSWepxXIcQuegGAzlddvdBglO5ecBzX0SXHMaFtpi5GGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpFDJVLKn--WiI9TkN1XtH0QfhnSpA_6oRqdgroNryqTylxk-VGQdfuqQ7dhRp8ZISKjAvmuQeYYjVkTv0xDGi57g7ZxuPwS9dQU-zOU_OkDgrgVf3I2Q_ENQX5eJ_cJmjA8IHMqwz-kaWpUFjqcPDcXtMghsIra7-T60dQFrQkXq54iJ6jm4OKv-Pq9R1ekEIu8ly6zygel1c2PbbmjpO-jFrRBvuP8uv1KSAETioHa9oApMGxkbIhuRATqsgme9-PJad6em85ufkwr4q-5N9Si-bOkGjI_PRZM7UI0IQP7UG6Lbwaqt40S-_qphC8MveC3_ejiYxuIYZqgFAgpfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=F6coH9hTx21D49n9TkQB3dLeEXJ1WIgWHqTG1uT6Av9Xgera-JqMn-SX3C1co_4ylUFCMsJ7PqAHQ8oP0EriJsSWytTV6Iz8P-BOIV_E99XXKmiIFeFzpEHzFyJfVLzPpVub4pKureTBYf2u-JCwTqamdHajdfZwHbC1eK8gjRx_bffgdvEk1CkbMAzljw9OwLXj6Sq2UPvRmZrQW555lIw1Ejy7tFQ0SMaNJTAkAfBY3mX9qQVS2My2GmVv-TK-XtgDcxcL0WaGNudsaBZUDeWpmf5wUVBrZPzkJ_8BfF95VwNI_Y8id_FxACER70OlAM9HguwopnASBX1hT5ZHLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=F6coH9hTx21D49n9TkQB3dLeEXJ1WIgWHqTG1uT6Av9Xgera-JqMn-SX3C1co_4ylUFCMsJ7PqAHQ8oP0EriJsSWytTV6Iz8P-BOIV_E99XXKmiIFeFzpEHzFyJfVLzPpVub4pKureTBYf2u-JCwTqamdHajdfZwHbC1eK8gjRx_bffgdvEk1CkbMAzljw9OwLXj6Sq2UPvRmZrQW555lIw1Ejy7tFQ0SMaNJTAkAfBY3mX9qQVS2My2GmVv-TK-XtgDcxcL0WaGNudsaBZUDeWpmf5wUVBrZPzkJ_8BfF95VwNI_Y8id_FxACER70OlAM9HguwopnASBX1hT5ZHLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2Wycdoqrd_wMbt8Yf4f_JOGNtvN2PrHfZhc0Nhm1xsJQMWVcYmD4A4KBjfvM0eJsX8dFt5UfSjlTpZKxc_EoWC8rCZ76eJrtAf3hIvw-O2P9wJBlxqnL4184mIZEpzGrROj-4e0jAj2UxJixCLNkT2vVX4eR4Sv0LmUyQECRkoPcYMx5qxb9NKbbVsUuMR0yNu4gLI1M5wFoDVPk4JQ3nR_sV2BK164vQtjjdBF8p-c9rVxjAWhG615W3PE-1THtNztmw-YH3tn6xR0_kiw1jaC4V712vgGdXmx3j1dzQqrpAnquUcrKNhvcudETCBjaJKecXz_ljl5l3enui93IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">آیا به بردگی گرفتن زنان و فروش اونها و یا ازدواج سریع با اونها اگه شوهر داشتن مشکلی داشت؟  نه! چون خود آیه ۲۴ سوره نسا صریحا اینو میگه!  وقتی هم قرآن بگه  هیچ آخوندی چه شیعه چه سنی نمی‌تونه مخالفت کنه!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6584" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=sfN7uQr-QeMp5tsQ8bWl23CCj1sFcebJUbXdv1xOQVK7-tfbslqf4nFxHrw0JwtoNwu_GVltnJoSMHUUJrSgPRHnxNobE4Y-GjeYyiZF4tX1khJIwGY1WRHOtOah4DFyoksYCclNF7FvpETMNsV7kWI0Vk5fpe4s0eAUq1_pnO0T6vLWYP7LOZf-jPdxRnggiZytwfdyBH5QC98oBUAb-ovHiK73ZnmuzKIecC1faBo_CQkkMvzEwRnLqmOjSCtrnSRNomEey5mZ9EcXexNpvhLPsCIpskkhpayVKJBKM85R6VJ24dsixzhIUQSAFYYtk464i-Oe_FloZgVYZQ6y5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=sfN7uQr-QeMp5tsQ8bWl23CCj1sFcebJUbXdv1xOQVK7-tfbslqf4nFxHrw0JwtoNwu_GVltnJoSMHUUJrSgPRHnxNobE4Y-GjeYyiZF4tX1khJIwGY1WRHOtOah4DFyoksYCclNF7FvpETMNsV7kWI0Vk5fpe4s0eAUq1_pnO0T6vLWYP7LOZf-jPdxRnggiZytwfdyBH5QC98oBUAb-ovHiK73ZnmuzKIecC1faBo_CQkkMvzEwRnLqmOjSCtrnSRNomEey5mZ9EcXexNpvhLPsCIpskkhpayVKJBKM85R6VJ24dsixzhIUQSAFYYtk464i-Oe_FloZgVYZQ6y5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHsszX2JaY8yWFllUdh607ZBfoARGC_lZOOhF3mozJgS4PSaafbhQzlv6OQovPOc5k_FHNTuZY9FfwjJv6vkjTGvpJrUTXxTK0fFzaPiFbGCtblKgRCUrD7ypJIJql8fS0Ki2uspM0p1PHWh8nq8Pz_rccWIo-fAbD0ANSIWvOo2hXbyxfFJLcfsxOZGUp1UuQnWISGwsli7iU7Ose41ITGKCcKQ4bbEIfX7Z0KDPvZIBZ3DFkH_pgbwtDemwe3io5BK9KveIAz7fHpMhVs93ek45Sh0lYkEX_AZ4xx9GrGEdZTQpxFLTIZ3y9vFCsq2pO0S8yqjlFkm5vsMMTM4MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVf_Pj9rt8ZFmJrPnrwizYK17UWpmpTPvD__RUMLnK0L5LF-QP0u_7BDo7IaeiBq7nGpkOgfRywuMvBWVF5iy4SzhckW5Wh_1gj6T8OudEHO-8K3K8n-fsUJAwRHXvkP7lnmHMxakTmTWM2P2DRbXn6hrJ449VIwtWjHdYtQpzaIE8F8C-l2SSLcAwzABduMc9tso2wos3BcoaXj-54fPSXmfe0tPakLVvvshc-95TGoFX7LgeZCJcxoFqge1a6mWcz0pM5ZyIEUOqKPwvxMwQlm9NXlf0zXHWI-6NuFlTXsTcA6emvwfJRdyz-GSv2xDVLlGtn53NzJc5VGVnrViQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=oOXsihXzKFLwD5tZKdTq95itWJvonhMh_hDARREcCq1DOfgZ2XeSSRjLnc_1enxvh9Rvi7GUmSIDSQotCbLqFLky4o20ql8XNLqRakGKjmVgdQ99V96jmfCdGApQ-2gl0HQASLFangz7ZO4RA2aipWIOYTM85O65jPbRRspDkl6fEn3PXERpS8VTDlvM-JftGe3f3FLp-_tDjf-9EO6qqjSNCpkFRNxmWfTTLVHaAtfiZsbX8qAul7RxDIDW4XcdHLUq7YeVqbndAtqoxVNXN1dcz2517CyliGtDb95AttyK7N3LH1v31lsKGqzsWpdt80rdBrUOume_Oj73AmRbzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=oOXsihXzKFLwD5tZKdTq95itWJvonhMh_hDARREcCq1DOfgZ2XeSSRjLnc_1enxvh9Rvi7GUmSIDSQotCbLqFLky4o20ql8XNLqRakGKjmVgdQ99V96jmfCdGApQ-2gl0HQASLFangz7ZO4RA2aipWIOYTM85O65jPbRRspDkl6fEn3PXERpS8VTDlvM-JftGe3f3FLp-_tDjf-9EO6qqjSNCpkFRNxmWfTTLVHaAtfiZsbX8qAul7RxDIDW4XcdHLUq7YeVqbndAtqoxVNXN1dcz2517CyliGtDb95AttyK7N3LH1v31lsKGqzsWpdt80rdBrUOume_Oj73AmRbzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5SV2PTEnp-Lv3PjXBqVI4nxbmNrcJIlpJg1OQ4SUM6Xv7I3UJPvYqH9Sd6mM3s5j2MFO-TkjfrEM8KyNb1sAKkTDiWw5rH6K6ahUJgQ4RCWifQjcAAdaUHUk4qSkqlo26ATl7zpLhM3iDLH9Akwp-LWXgfm2HzxbEmYMC-QnJnVZEwWkeM87cJI4ih4yIGrkBF2D74RNidW4SNqNCMDRLgk5eJSn27S5kVrXfKmPkqSBqG28MdaQcPiUitgQ0sWccNdsEilc9s_inPmLmjzNdRSxMqo0NR8GkaecQ6muAQNMm3z5R6TdXzMOeJTtfSRMiE8Q37qWqgKvQVZ7F-q5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kB9uCrtmU0NF6MwZNu4mXSsvYIjqB91lMqOur0q4npXGvDqzgiYEPD7ewkrZM468RFYD5JQLF-rkvATGvbofNPPQmUgxDOZY1cMOqZWvfqKz-9EPzD86A9kAUUk_gb8JESNMRE3GA2uxvESYVZtGWkrVZPNM8Prj9DPq8xzBZ9kgbCjMAIe7L4iEhUE_9p3Q8qXXvuYO6JWMgjNC_AUymHUan93m2ZoH0GIDdYvsVYpCkL4A--4QVnXkll5Kf8tF58keimFmULJI_PtvgsMHn6Mhh6-XkRyp-Mc3_gW01dyk8ZE0zjwH4l_27GQZ3FTKkuTMyyobbSK5AxGx7KtpMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8knGQegBBjYKLWvrRTIaPTX82STANBxR1WYH4eMjKrCkrs4P3IXHqY052U76DSEXO0xY60_T1RGWSO8n3yVnVTDHnOvElNNyDId5jCn6zrKD6b3INk2Mk4fUI_gpDk_Y4lX4xftVmir3DPK85KP9so8BQDX_6QRu6DJLdFhhO5dlg37S-R9TupM24fxeus1wJKoNQQvdSw9SMKCgUaXyvg4ZC3vX4AofjaYoYDd700xqZVjjKDfJsE38J8QaOr7QyiCqYIeZuSEYPKV1YH0X14iKCL4R8VfcCRKx1WY9CclwmPj1cr0iAt8QG6rD3kBkscuOfX12m_H0wHlIKY4Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=LRAZIml27Cj6WZdmAs3eEDGD6lVijSA1N4vzQZw3-E0DHWQbV-kROL_PE8GvQeKbxxY8L5tNyredv0vXznmeHnPULSVuRqoQbb-d9Wm2pjjEXGyDEr1eOL4Ev9OtToDIu31o7KiLUoObRNKlKxAU-evkT9ScF90ay7_MVrc8udqaOr1UMzeEAAi9dQfhXTeT_rgiGdBI-u0kfaltjdgotIM_mTLgKBaUzCSyN3JSI1NuDfvtQTD0KeDV3IFlBtczJO42ZI3i5rcM7ls_Hvj4qX7Pcblg3Yc7AZngHRsZSpdSYw7c-WAMCsqRSgpkAQSRy0o1TYYxB54_cnX2-saBwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=LRAZIml27Cj6WZdmAs3eEDGD6lVijSA1N4vzQZw3-E0DHWQbV-kROL_PE8GvQeKbxxY8L5tNyredv0vXznmeHnPULSVuRqoQbb-d9Wm2pjjEXGyDEr1eOL4Ev9OtToDIu31o7KiLUoObRNKlKxAU-evkT9ScF90ay7_MVrc8udqaOr1UMzeEAAi9dQfhXTeT_rgiGdBI-u0kfaltjdgotIM_mTLgKBaUzCSyN3JSI1NuDfvtQTD0KeDV3IFlBtczJO42ZI3i5rcM7ls_Hvj4qX7Pcblg3Yc7AZngHRsZSpdSYw7c-WAMCsqRSgpkAQSRy0o1TYYxB54_cnX2-saBwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=bKvjthRJodU9Nrgif_-I0yer_7dtMfx1nGYe-rKZObWuxrsUcmyM9bF6zDpUHkILHijIp9lMRELw9zyxtTDe-IiFcFAUZEMtx5bfSX_fYm_5WMkQxxGEPxUux6pXUHQC77QAex05MTXaxiU92nYMlfOo_YbV_uT_pu5g_QxW7ROt2XdRM4Vfe72Pekfm8xY6sB42uNr9oNGr0sxEgZQ0dBbPIiI4hmMfIPipa3e-Q4hov78tkrBenfAm_oZeMni1EQGZHTAWTaXKh6oR6AhZqIesp1Eb9EB5XjnsDhQ1Spup0XjxB_oZf3oyMN-xKS1QL7q9mFH-1BoBamsu4-pkkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=bKvjthRJodU9Nrgif_-I0yer_7dtMfx1nGYe-rKZObWuxrsUcmyM9bF6zDpUHkILHijIp9lMRELw9zyxtTDe-IiFcFAUZEMtx5bfSX_fYm_5WMkQxxGEPxUux6pXUHQC77QAex05MTXaxiU92nYMlfOo_YbV_uT_pu5g_QxW7ROt2XdRM4Vfe72Pekfm8xY6sB42uNr9oNGr0sxEgZQ0dBbPIiI4hmMfIPipa3e-Q4hov78tkrBenfAm_oZeMni1EQGZHTAWTaXKh6oR6AhZqIesp1Eb9EB5XjnsDhQ1Spup0XjxB_oZf3oyMN-xKS1QL7q9mFH-1BoBamsu4-pkkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueQ0GxZhiVe_oAgZLv7sVGca5INm_4kWiNH3TJ38S4esMwmwOCdCCtcxLH-X8lHcebHXLWyZdLMoS5BvbZD4MylqgoiMPmZRh0Tlb2mDYZLCLVwd5pjeyB_0KguztXKC4UKnJP2xUOHVaQQ88NwR9CzjMEmGcptRYAsgFu5Fr71iANuNe40Kx94TxfZBkFNqVT-5Yj617rEMKCZ25dAswy8fzkkEc91zULOx0m5n71LGtpwdUPT9SpWPHygYkRJKXB6WwdiBKsoghSbwlf3Y-ch9HBJzB9-0kPfdt3lyfu3iPbfjJP3SAaT4ASagJHQsyVqFOsZC8bM0crlkni1PSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا اون روز رو نیاره!
همین ایران و غزه و جنوب لبنان
که حاکم شدید کافیه!
همین افغانستان بسه!
میخوام ۷۰۰ سال سیاه گروه تروریستی حماس نتونه حکومت اسلامی در غزه ایجاد کنه!
میخوام ۸۰۰ سال سیاه گروه تروریستی
حزب‌الله در «دکترین ضاحیه» بمونه!
و رهبر شما هم از زیر گودال و چاهِ حقارت،
«علی الاصول» بنویسه براتون!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6574" target="_blank">📅 11:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZGjdftGzjGRI6FvH9bgjAHaywQ1hcikQor7ZvqvsEk3QgG-LN8uma178M6TUuyvwEHulIeDsHe8JfNdeKJsywnuAtVjeW8OBYz6ylAmPI7MCIU8jqZ4mAO1E3tc_6JRKEfHFnQLnkncXmRKcYFk6oLAEBgQXWY4VGZYwlSTIJ1TR_ywV06pJYxVBRbamgurOz22QTrFaJnokElJcD4cLVkJSwzqW_r9OZ1-2_sM5bIFWhiZZwsyrTedMxn0vxmMT3rXDO3dSl3IGIUeD2DH3XjKVKn4oB-_lFUlncqZQlZT8hlK4Wlsoi1fSnFMyNOyFbHN_JFH9TzBHrHdJUrhpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ON8yhpqh-d2R7juK-nQxCKMFNjpUH7YS7DHIb_DdCndhO_Vqnt_GY2aUx1mc-E420EIk1mjX4jeXuFvjSpO8RPIG7hBRgX_rkGSL43mt2xXOhC4vW1MJlPDNp3ASQ6WF09nbwZxfoWBIsS6pJsO39QDD8hI-5kalaKSkA3JEN0xMumnVuBfvCPB3IbzSzFVHxXBobCDg6IpIvt8G8mvhFw7fPwfYYTeFVW9lxtB_-jwhtwvY2nntGx_73ENs0j7flXQ7333aNYjeTky9GBudBqNf3E6CY1JexzM6qVxKWRe9zmWBiB2t2JbcV332gMwg4F1J6C8iTzOMzc8gh_6RIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iP_XVz-kW2iNZc8E-YlbukQ08T2543GsVB2eMTktTphacCli2FBSA-mSxsYOxkUwQNSvq7XLIl8mU_tAyxfLK5HNMw53RvJZ9MEZaqPp3Re15SyW_EiKSlj752GwGFEQrNO2QT5xOKtPhpftUXkSA_CPVoy6NuEJM9GHOEsWa1CUtxylcRKk1euZz9Ojjt6080JB7cx2yfNpYQLjRou3qVWAceMA03C4dU0zPPl1B4A3iX2WiYeRkoEoqMJnc19k8WJN6bRcaCrt9c6a1y_MvbwcJrk4QMsTT7bn3I2kjRIkbBkNRQWT3NmiD9XFu-qDkmCe9OIqH7Z1orofRdNYjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5Jo2f8OFOnl3pOGbkiIPo1emrIn8clswS7ZWlOx5kJ6OZ8mzPyia8G9TNjyVjZW1KA8IWSDKRFuLYrPqi1XpEfLUI1Olp9FTBzGEh8wC1YeaDVypZBrYhPSyz2GsGarHEgLBOadU5Bkr7oc1iUqhEqqqFeMoxHAy8Rbi4W704K6lKjTzILYucc7vaebA7W6c6EWGbcnOMrAun1yODELq_UDLLC6fFLyoA5ZE52y1gfZ7kvK6FeLGmcJMVa-46fWT9n6gSE7LuXxeNTNR8g2exPJ7BXqgCITb2PsRcj63WftlGQfcKlKsNJSi0r3gEyid8RlNd6FH76StbeThVW8FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQDvVQz4rbT54O0dBUA2P2r2hpwKswwoUJ562oX5dPXFO4H_PCSRXiHTgPtewvDdsNxP7kA1aPJOznD6EWif4SkF9dCy6x4XIYWKJHcljG78g5Ls_kxbNmamw2FeL4K7Wn45g2SxqB0EzmuI4Rfz4-mlelOKwhV0KGNUAFYIu4iJYPvARFejOe4yYFKh8tc3IXIl_zCevc5jpi19BoyiLkWuFOx7qg29RlcylDq7x5FKMsE-25Q9mPC0g81vAGAfqcaJuPxNAIRRqrvJfa6WwPZeZeaQ8tTAU6HjeAlb5keb6cMRblrEmPcr9-HazKYL46iJNdJV8bR1ZHw67ZTkCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر سیاست‌های این افراد،  از جمله این زن و شوهر،  کل کشور و جامعه ایران درگیر یک بحران  عظیم شد، آنها از رانت‌های بزرگ حکومتی  برخوردار شدند!  سید محمد هاشمی، وارد کار و کسب شد!  از واردات قطعات سلاح برای وزارت دفاع تا واردات چوب ! از جمله پول…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6569" target="_blank">📅 10:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">معصومه ابتکار و همسرش «سید محمد هاشمی»  که او هم در تیم گروگانگیرها بود،  در همین ایام گروگانگیری، با هم آشنا  میشن و باهم ازدواج میکنن.  سید محمد هاشمی خودش فرزند یک آیت‌الله است!  گروگانگیری ۴۴۴ روزه موجب آغاز خصومت شدید آمریکا علیه ایران و آغاز تحریم‌ها…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6568" target="_blank">📅 09:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsE61qJ5-9yA35A7Ac88W19qKYgnlOKrdMthowe1IFWtj4YDC_zdAsvsfkjphZY32BxudNDwD6RQp9JheAhqJ-lwjljG2sqPuqLDWKIWLRGn5WNpSMjfLvhrqb48IQf34puxJDjjGabxmFBXnRdlLXWnH_wcKXJhcZ7lm6aErOxGNL3WCo54VD046gqvONn1r1qGxLaHwioMGAGX06ENi9DBhm3Ft7_CRvzqlq6Zh5z2g0RXTfupy73dtHUC63uh7Zqcu3yLJ_zPh7xygeGT1_vHwNXDIBkND6asUeczvriv1kK558xjcoqbTpIQPHP2OXiIvVfQds1SqUCdh7aWYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم در این نامه به مقامات آمریکایی نوشته  کارهای «معصومه ابتکار» ربطی به ما نداره!  ۴۷ سال پیش بوده و…..!  توی این ویدئو که خود مریم گرفته ولی، خودش دست به یک مقایسه میزنه، میگه بقیه پرچم آمریکا رو زدن ولی ما پرچم امام‌حسین رو!  در واقع عروس خانم خواسته انتخاب…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6567" target="_blank">📅 09:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6566" target="_blank">📅 09:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=kB2A1z9nK6hwEtpmZqDkxDyJwXx_wZQEqHVtIjODvvhU3XBBQbzaXcuNHwIa1jTJ9Vl1v3njeITd1fdSQcyXNm-tkIGgW73HaIxJLX2h5JrOkAbCtUb0aPefo3dX7TnBDOtUL10QAw3uJvs5LjM0WDK0lhewNXWzKZOH5KPBO8UBY3e1I4SGeyZ4k_SaLgrsOdDBzNKafeHnaTrXOgtd0m_CCjQ5IvQ5EbIhl1LuuYppfWv-zpy06lkAnrbyqDRJAvnduVgqrl60EqV5cde6_SW0a3N00TNrh5ErZKLAWkxJiyHr109eo7d9D47L76i0krycEZqPybv7anOlS_yOcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=kB2A1z9nK6hwEtpmZqDkxDyJwXx_wZQEqHVtIjODvvhU3XBBQbzaXcuNHwIa1jTJ9Vl1v3njeITd1fdSQcyXNm-tkIGgW73HaIxJLX2h5JrOkAbCtUb0aPefo3dX7TnBDOtUL10QAw3uJvs5LjM0WDK0lhewNXWzKZOH5KPBO8UBY3e1I4SGeyZ4k_SaLgrsOdDBzNKafeHnaTrXOgtd0m_CCjQ5IvQ5EbIhl1LuuYppfWv-zpy06lkAnrbyqDRJAvnduVgqrl60EqV5cde6_SW0a3N00TNrh5ErZKLAWkxJiyHr109eo7d9D47L76i0krycEZqPybv7anOlS_yOcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=OVaiZLxndG5MKtF1aDdmKvK9s0CRxN5L0QfszRYeMeyFVyU_Y3yYZWFKS8-2FjpeKNWuF2XEEE4U1S6oOh3rqx123nBKcjjz5XbXoMJmObesjeMkxwuPsrOf2O5hEPO2VBTHUI0a4EEra6iX-kRXLz3wFeGnhnRfH7_IlMNzNR3CocuSAgG0T_fMG22qDsmt-GodQyoC9YCkvLM3nI6VhkY0aTcwsPYWQp3AO7fFDoUBkZ4U0HYIJJ_2JnzH891ACpw9sT78DX89HcnMKFAc6Y5QEq5xCtuF7RXRTrjkAccql53YnVU9k7xviY4Up_R2_tK3lJtJ2UK6FraqwzCDTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=OVaiZLxndG5MKtF1aDdmKvK9s0CRxN5L0QfszRYeMeyFVyU_Y3yYZWFKS8-2FjpeKNWuF2XEEE4U1S6oOh3rqx123nBKcjjz5XbXoMJmObesjeMkxwuPsrOf2O5hEPO2VBTHUI0a4EEra6iX-kRXLz3wFeGnhnRfH7_IlMNzNR3CocuSAgG0T_fMG22qDsmt-GodQyoC9YCkvLM3nI6VhkY0aTcwsPYWQp3AO7fFDoUBkZ4U0HYIJJ_2JnzH891ACpw9sT78DX89HcnMKFAc6Y5QEq5xCtuF7RXRTrjkAccql53YnVU9k7xviY4Up_R2_tK3lJtJ2UK6FraqwzCDTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6564" target="_blank">📅 09:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است!
و این خونه عروس معصومه ابتکار است.
که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،
حالا نامه نوشته به مقامات آمریکایی که من
عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6563" target="_blank">📅 09:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=ZvoZHy5NhGHtDmC5H7u5KLbi2ruk78h9TGhN_fAoLRkxms09qi3VhUX16hznA2NmTwQG6038BDbd9eigEK1q4kyBTshbFLxzlTnysaPkB6CSQj11KzGLjGBoyRX9JbBa7VVJD2xNVwy3ZdB5VZbWvP6-EHZHHgvw8NelyNJz5sDRvo40qVHvT1qpKJoforTtqBmGIRWsbE7Om8WdASUmxrCcOGAsI6ZyuYtjJ1UnhqtHDi6tg-HpolvkY7-9cBQENdfq9SDr2OW6DCVsMO8-FzG11NIrRPPetXw2sJ-pZ0Pgo3tjmL-jRgqmwzmnrrKQEmI3hkJhfT7TWtGjV_M1vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=ZvoZHy5NhGHtDmC5H7u5KLbi2ruk78h9TGhN_fAoLRkxms09qi3VhUX16hznA2NmTwQG6038BDbd9eigEK1q4kyBTshbFLxzlTnysaPkB6CSQj11KzGLjGBoyRX9JbBa7VVJD2xNVwy3ZdB5VZbWvP6-EHZHHgvw8NelyNJz5sDRvo40qVHvT1qpKJoforTtqBmGIRWsbE7Om8WdASUmxrCcOGAsI6ZyuYtjJ1UnhqtHDi6tg-HpolvkY7-9cBQENdfq9SDr2OW6DCVsMO8-FzG11NIrRPPetXw2sJ-pZ0Pgo3tjmL-jRgqmwzmnrrKQEmI3hkJhfT7TWtGjV_M1vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت نمی‌تونیم بفروشیم،
راه دریا بسته شده.
چرا زدید زیر تفاهم‌نامه و حمله کردید به کشتی‌ها؟ که قیمت نفت بره بالا
و به ترامپ فشار بیاد؟</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6562" target="_blank">📅 08:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6561" target="_blank">📅 17:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2226555990.mp4?token=YppJriDuff8UjnTx8QA1RLKcBLYpd32ghlQ5CK6880H6dGnfegbkM-1P8bLmEGllCesrx_IbfDGOtM527ObIfKpvUk45MOtzM9ypvFLp0_yJLJx08WptdBwJihjPVQOlLCCuP3aaIKKuaF5Fn_TGmsSFPXQ8H8hR9GqCb58iaBqnbEQ8ClWhgJx2DxPs-aJTg_THmW4zyG5BEaWElIgVHvYzCcycypj64va2klZnZAryBnP1H6mOlalV9JHqG20RQus5sDCTdunjMh0JjdfPrp8dK3xdXs6i7nBvh3ICQf5GK1dGMBps079miZS72Zqe41x7ur3O_9t4pHIICth0og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2226555990.mp4?token=YppJriDuff8UjnTx8QA1RLKcBLYpd32ghlQ5CK6880H6dGnfegbkM-1P8bLmEGllCesrx_IbfDGOtM527ObIfKpvUk45MOtzM9ypvFLp0_yJLJx08WptdBwJihjPVQOlLCCuP3aaIKKuaF5Fn_TGmsSFPXQ8H8hR9GqCb58iaBqnbEQ8ClWhgJx2DxPs-aJTg_THmW4zyG5BEaWElIgVHvYzCcycypj64va2klZnZAryBnP1H6mOlalV9JHqG20RQus5sDCTdunjMh0JjdfPrp8dK3xdXs6i7nBvh3ICQf5GK1dGMBps079miZS72Zqe41x7ur3O_9t4pHIICth0og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و تاریخ ثابت کرد حق با آرش و آرش‌ها بود!
فهم آرش از «شریعتی» و «آل احمد» و «هما ناطق» و «شاملو» و «غلامحسین ساعدی» و…. بسیار بالاتر بود.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6560" target="_blank">📅 11:22 · 23 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

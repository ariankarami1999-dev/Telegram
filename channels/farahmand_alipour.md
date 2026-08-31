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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 20:38:04</div>
<hr>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_Uljm4Zx2Fz1dqPll7bLv_fMbk-8spyxFUmUPv-h6w8B-bqc7wh4YBeps-UNGo5AmPyeE2pukq8q5iPEq1eOL4QDn4GXzvEeKNeu9EQb0VwTp4d4llVvJG_mKuHoMmggpNeIMGQfGTpss4ZlDd9vsuSvq5Mgr4V14oxGIZyKYPd6JXcUV76wc7JwbhqQMfunF1gZ259HUxNjA1ymY54FNo9rPHbhXfCQQlTNMjQAl95Z3I6SWNsGaNiwGqBzvQqrUixJVLenYYSy3bGenhqpHus2n77Pa-rSito2fRadR6cYLs3INeHKlPXLn7Q-DHHhluOk5c0imrqJ9_cigU7wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUyRcX9XGqv_yzGyU3aTCxfsQ2DV1JQFncQVA8sdBMeEtr2SdybF-wakj9Np6JI4M1KI5gY_UCb_s5eKvXlph_I6gCkajKIlSakTaCw7hetO-arljL3-Sqe5_wqd7sBjwffPJyMUGbUjyGNco8iI7va9xdOTvyo7vGEmG9FLr7RKj4znoTESUzoDz_dtjhhZFDRTrbV4HGbS0_bY6vOYvtLkiTvcUptEb4adED9iutV0NmkFZZvRfKmvqiQEPZwrltkzH-dsnj37nh_Ft8jv7OQOSQSsVpi-2ap2fa7EYe2hiMFdHoZ4td9RjZ1GkOI355uXvOsL52PL5T_BqU6txQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iv3_swxgGbeAN4vCo6ax9guy0BVUzGe7D1qeS6OnU8DLHFV9jh8Z9wZvoahy7Ya1k40uGZjlqPGxXYV1dBowwo9adZqpCj6Pxp0Aq9z-Dkx9dzqPXvbpmBFJ_8e3d-41Y0yfcIR_-6OL7khp-PmwNldZcyDK4aP34HtZ8Ck84MMMoNj2yOSbfRRC-AwsxVX_gnaxhoRkX2DOv26LOZ_cho9nyrlCCrQrshO5udPV4lD90WQFzJhHbjIB5bxTQAbLYsGlQudmWuQxq30s1hm36Om1jOb9eRAsLFMU7zH9eJLjkdFuZEkHx-6tdxy9RhraDr00ywsOGiMNycB451Ilug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEzM2lQQpXMbr4EzEqQGCDjE5915gjR9UsgYOsPiryq5OKZsOIHdkI0IuNtISM7AJpnhOVaCXD9QHpUpfD5-L2d278g3SKt-tMqwJO1LSJMdbzrD6EPvjBvIcLB9YfmKYjnVpvPstd0MhmTRiJGoF7qFafkv4KlRFDMO8RR7ndt1fEl2kSnXjk8EQc5xRcTTiWLtz-NGVxtXlSOXmjOojZcJP_6AcnHGdbBvWEReJbrMjXGiwsBrZtHxJLFMc24jpErLg3BuYS9T-F0H6C9lPnGHu5rPj5Dpa-uYfvtDYqYkQx9D3ulEw_Gje0q9j2mkglE_VHUrOmm1IzdjDqPcIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEgBPAxlsTAM7E7E9j7JVFNj3NU6G1qrlJIXT3NZB25fCpFYDTwn60ELPxNbOtuhFZInXgdO9hYKv9bCOxgWPQ08ndjBHQtV0YSaAb1wdjfd2o6WulSNAlwkI0KpPfe5kUIHzEX8IWR31DCZnzGhvNp4UxX0vn5MJFWnmdcN_TcOeMa1SmERSwkUuq52Rm_3yFAi71LbLvP68qezEIMqX2h-xuh76WwVK4pzz3wibmUhAxWq9WjBdMDH5lWeJBM3UcJX_pxINTTzb-zPdd-0NpQQebXP1l_wzysw5qMRZFWhz-5qE9NIQrmIS2A2h2glA8rDiiClylsMirJ_P-kkKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSnAG0UEoU6hw6xR9H7dfpd4waX63lchhKQ8DwNzQRklC9ev4E8Zvw8c-Dt2H4Fj0MyQn396TG_Ja1agBh_dsol8NkED7c8VOfgft7bt84jwdyzKhgxmgMl07Ome3n0IOwGFkZQ3-bz7XepjT9_RSKQv4Osn327XKIJYW3Jjp7EfJU9LQEpHHI4zlEye8SKmLO7dmmuMieJG6oL4dzGGo2ThRNyRFotpS4Nb4OwU1A15D1O4gWVVATA26hICISJqCoUlZnb4z1YVerK-A-K-BleMQslgRXnmGR5G2iBt_2XYw5ZNjVN7W7DtmGA66zW-h6WB57-UFyNu1__rV_tFmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvRBQ8NHwhfUbOhqJkT5V-FV1mYtxot1nznGleZTemuWyJ1eAEMqwZQuAeveoa9SGjapruC9KlnO-IC6OmJd1FJOwhTqaxnOyKXFQfdxuYElvkYlHwN48P01OCTcjmYn5NsFVnjtcUB7QUsNSpYY4dfqVsNyy1XdTBYvnhzeBJZe6yV13Sc9lNSaPJ2oK6lFGDsn6AwYEx5Ni8tr_mdFLTZIp8bxxq1xOSEiUxV_uGiqBVWtxFgCFbAGpeo4xRoUzGikwyd4Mmzk-1Lxyu0k1Mc8c5OZNYN8gS-SiiG_GUI4ENGb4yNLS6ItEWyyYSBg1GAkAsQQaCHl8CyDdsGVYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNHWR8wFUUz5FFR5lxRY0dIDdVtT4MhK3U8J8amOsvGB_97H1VkV6-HlNzv8DVY9N1X9DT3luNhYh1c1a3NTg-9mJagnaBOAnih1AUTzGR9hzyw09uZsf7TG393YN5VXltbcLAnlNqL14AudoKGMGU4oN08TL249E9EP0dfcO7dK0vMJudsYqcQW6cOIddoFgCZa5Yv8gztpLV5uOSzHmOFruIwe6RqKFXMIqHL2b_3mjbDMbuIEtI6QeXr3jZDway-KmYg41EwldoKtMvHH2EDyhXoKg-R__tiXS1j_krJkmOHCa2M9cQ__CyLI3MlrCuvGKBCui3Xh5NVb3gymMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=iDOtFLWWOjPAig7Ve1rU2a4Nbls_U0k72XnQokaNj_Uira3xfD3bA5wOdDZNX0zGt1PgTzAop7gtC5s81Dzfm0TV9ptMsOFSVOGARf33AQZnaPlbrG64RqIthtFsUcHv6Ly7LfihvXHxLGMB6O68WsIOETXnQvt9VXllspTentZKwBhnYptPI3yk2sHYN-bBQTSCujMH-4tbF3dDM01p8XuzgPSvmaWU26cDGNwVwh2IWk-DNun6cRnDWES0BoaCbeHuCfdbHBYbc0faSwUTJWoU6o2mtW4nfJ7VIWdwdS4JEPqW02F3fUEsryElOSbWY-ceGz5shsc0_QTNoYhhYGtyKR60q3DvUfvedrEiDFs8unvMaAWLhDVPyF6m_Sxf8ViIXMXa94AkbHFrYtRs3owWKisiEnC5i7Dbf8idrkg4JWUwO9JvIhQONngn69ThUt6HqcS_6Ta6rsA9tLD_Ypvt47cIon0S9CiFTCxtGtOP-UsRJD92eACA_UIihWFETiLquE6C8sQoroA28f8SqEM2sst8MlfMEo__s5_vBFQLh24I96O6LIbUshqrbybGgsmVTECoLRKEfQxMSRo88Gw13MyVK6QqB0HIAN3_gnBsHQjCI94U7sR2Ww-GnUS_OKd-TklNnQw-2zYc3GeGmGlJ2ZBEkEEdgRw9mMrATh8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=iDOtFLWWOjPAig7Ve1rU2a4Nbls_U0k72XnQokaNj_Uira3xfD3bA5wOdDZNX0zGt1PgTzAop7gtC5s81Dzfm0TV9ptMsOFSVOGARf33AQZnaPlbrG64RqIthtFsUcHv6Ly7LfihvXHxLGMB6O68WsIOETXnQvt9VXllspTentZKwBhnYptPI3yk2sHYN-bBQTSCujMH-4tbF3dDM01p8XuzgPSvmaWU26cDGNwVwh2IWk-DNun6cRnDWES0BoaCbeHuCfdbHBYbc0faSwUTJWoU6o2mtW4nfJ7VIWdwdS4JEPqW02F3fUEsryElOSbWY-ceGz5shsc0_QTNoYhhYGtyKR60q3DvUfvedrEiDFs8unvMaAWLhDVPyF6m_Sxf8ViIXMXa94AkbHFrYtRs3owWKisiEnC5i7Dbf8idrkg4JWUwO9JvIhQONngn69ThUt6HqcS_6Ta6rsA9tLD_Ypvt47cIon0S9CiFTCxtGtOP-UsRJD92eACA_UIihWFETiLquE6C8sQoroA28f8SqEM2sst8MlfMEo__s5_vBFQLh24I96O6LIbUshqrbybGgsmVTECoLRKEfQxMSRo88Gw13MyVK6QqB0HIAN3_gnBsHQjCI94U7sR2Ww-GnUS_OKd-TklNnQw-2zYc3GeGmGlJ2ZBEkEEdgRw9mMrATh8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQKqC7DxBcjKQtrPDK-xp_CyFnkoUNXLxKl7BNRf4hLNQrKUg6-2eR598KsyGkd8WI62KZ7KzNhY8LNkRKS4gyRiMvSaR4G-pewVtUJwOsKp0v0VdxbeaysdjTTmd0DLB9o5PTuvauZHRShaCalU9O_0j_tSFFoMGiTTPyA0E12QUf4fCBw4mBNjUSlN-n32XGod8AoaNn5UbSNBKyik0WoO06zXCqgAomNaN1yC6MS0HE6KHD5fy8hgCaAZ2Qlx3cBfj_6GoQMv2Yv3uPihPhRrTR72eZaAmNinFlUoFmYZRU9qntQ0-A5LJ1URaExYzANwXkqC0iEPlfqIrvrO3Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=sKitviaayDlLGCn_AV0zvnLiDDOtr6sDPK--ElbXcaea61ysDBwltXgdUHMWuZJcRoOkgW_0FOY5MBgEvgqa8H0YBiExwu8f9CFNG0Y51oeLvh32nyRf0iBpgDIMwcfjX8E1yVOdTGny2d7g7QmW_6IaablB1mO1eWkvK-zRzycbq3bkX6au7iWLVZZQJLg3zV_efu8kZPcXQfcr3_DHkzdahkqIWINbFi27nTZ0hgQcXqxdpPS4TtWoe6XPDoxXnbl8Jo7it6H47BBk8HvqT41j6OT1SpkMTrRZ94RG6wn3wA109m0qkcHixWiitw59ZvJJue4qyS5DlsPbNejC3wTqvLVs3g1pxwCs_aY0HL15ZAUc9GsrTLBWdvDLhhpGWFwxpPrKZDI17HxyZBnExHKFRMUe1Jq5CkmAZ0Z_bnwmD-XKyNU4pT1h3aeyJ8qMxlI5Q098XD6kldrgpgSKKQa8zUQCPYqG12vruJTGAfy8cTD5MieAwyZ2UvmYXlzpNbba6K3-KbO_oAHFYqNJy6PWiC6coiZyQw6s5HZjKaaRUF0DDsQ_YuxA4bwzUwgNrFeTiUpHSDxLkz6SB_uywiGhDy3haCDsHtmTgQGm1oNfQ82x7EI7vKLXzbvguDPWNIuqXUl08DLkCGJz2mHkOb9BoE7ImfFoEKkkVyPwV4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=sKitviaayDlLGCn_AV0zvnLiDDOtr6sDPK--ElbXcaea61ysDBwltXgdUHMWuZJcRoOkgW_0FOY5MBgEvgqa8H0YBiExwu8f9CFNG0Y51oeLvh32nyRf0iBpgDIMwcfjX8E1yVOdTGny2d7g7QmW_6IaablB1mO1eWkvK-zRzycbq3bkX6au7iWLVZZQJLg3zV_efu8kZPcXQfcr3_DHkzdahkqIWINbFi27nTZ0hgQcXqxdpPS4TtWoe6XPDoxXnbl8Jo7it6H47BBk8HvqT41j6OT1SpkMTrRZ94RG6wn3wA109m0qkcHixWiitw59ZvJJue4qyS5DlsPbNejC3wTqvLVs3g1pxwCs_aY0HL15ZAUc9GsrTLBWdvDLhhpGWFwxpPrKZDI17HxyZBnExHKFRMUe1Jq5CkmAZ0Z_bnwmD-XKyNU4pT1h3aeyJ8qMxlI5Q098XD6kldrgpgSKKQa8zUQCPYqG12vruJTGAfy8cTD5MieAwyZ2UvmYXlzpNbba6K3-KbO_oAHFYqNJy6PWiC6coiZyQw6s5HZjKaaRUF0DDsQ_YuxA4bwzUwgNrFeTiUpHSDxLkz6SB_uywiGhDy3haCDsHtmTgQGm1oNfQ82x7EI7vKLXzbvguDPWNIuqXUl08DLkCGJz2mHkOb9BoE7ImfFoEKkkVyPwV4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hq02Ojv_Vmo_s14WiBNHGOdwrLPcqQoFYAUJQ1jFU5qYqS-t4cHRhl3-ducZMa6EZuX1A_9xiw3nbBQbD0kFju_bx2119ypjHKKlvKp6SNs7KpIb2A4Yjso3_5K7bDu4HAd9CcyDhNpiNwtbtowygZ03YvRvMKoaJ2cyPWhgaqziZt828i8d5IBnN_j3SRIQs3QtDXwNhkaxND7K9TbLUwmsMriEV8K1ZYC-i25QN_VgV6RQB6_kGJzaCM_IxloXn_wnHCoY1F5-wpfKKIPe5vWZX82o1oJck0ouAdyna2PW7KpxF0-_5L6_g-d1E612cK4OefuMDY1s6nIYxL_eYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4SEuxIehrIc5cAAaPQx0x_JqrAUBvI2YjmLbQoC6LFQIe5GrHU_1i-6qQPhE4sL7ZskNgcUb-bDLAklxAHvIE4FGU13SbZabHtNk6aH4DTjGJPiZSK3BxTkWB2e8QTbxjnpr_l3htMG5myztsL3I66jN9SPhvryhskWotcoLPoFQ1APG0ZuPs2z9OSTIbjgkNLknCgdr8QmOa0vsDmEbajD6wLObnzUMRY-4ACvq_eSEeRICjBToonKyyzJpC8YnVfj2iNR56q3xLLfhSSzHd2C1rjGy5TbkrpBtS-VR-vi15S13ObMbFKJg81d0tu8cXBBTosp-OGowAHxlVvNig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RN3WF5VxyLMXOJBV7nZEL4pYVtf4tEzlVX94DvdUkyXeuJ5PnWouqYrCLnUem9nfygMAfztL_i3VCDDYjDg_gXxBHu-735g5CU2gzgGVCEADpNoanho8sKRpcKbQFgOsYrkJguBzpJWIznDLXSQgTyTLFCPLbvThKq1KKVOM14AHr0jFD6To7w_J-0YGxw10hQT7zc6nJ9Ic-FB_xyCr54M_x0qHBlOXvl7U5_o5KBPcakIFE8-VtRQdlxIfZbpslia3V4ZS7s9caQYs0yW0bAzwxuddb9DN6brzFlot0fVwbZ7ZxTwD9oiCcfQtbR8HBq76G_VoStaRfQ1T94ZeLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAffwG9SFm9SQ0j9c3ePxwh-fbme6NlHEQ6Go08NxIO-7Qzt-PLabel7EUwIAjX-TGrgnoEDrVNxD1Sv2sjxb-XYUNqTpGSOKFSu7o-5bZTtF_VyiaYoPtwlWMLBCsl1FfEaDVQvMxaE3b6fMriQuKpmFyc-ZbVb7d76dOeGQTSfFk6q0vtYB7HDzaRlGwhaCve_QDKG4MNl589nLSIM_honMxd4I5hDkILAgZJ1p9RqWCaKPm24w9Xifp2ndDt6piPKcXV5bnffD5XDP9ghAZsh-SeDHuVp5o77cil74dH5bMuZh5RNwTBmkMcvFTcCY7AIT-G03TlJ_pRQltspHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsSLI8zgsLzm_eBusw_FDQWtVz3J8u1k4f3RT0gujjqVHe_kJsg9VbiJaH1OFscZbKCU8VefLi3yCN-fTjQ5FqFx66U_Y2R1gakQYV99eg53RfWPEvMU7Bk7TyLu0aYQ5SHOhLwJBkC7dtQmQ8_yQvrOLhJIL55pwTVl3s5Hwj8_s5weEpC4Ufn3m7k-cP8MglnhbReNgs4z7WNCxr-uomP8xUM1vgM-5Llm7S1iBBKiSQSjzmhW-8yIKb4frlYNYOcioTA1rVyx0eTuktuLLpZhxSTZNRxDidNXnuDHQUuwjRqtICAbfSBNo9gnXn1euAf5LLUlvsnCPYGZZuTsWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lor64n_tJwdahKVI4-NYJ0Dt0jL-f_-_YBB_TpQKLurHBuVjm5jYLpcaxIT9mKKQtkOvAxPPxYGtgyii_oDF8JVp3mB2lSbHLZTjmSn7jDqHKc-Ogg59-wnlVnLsd5Pf0gOUPvNxT4EZkKaSRr1MfPjmxUqGKK-PMQf-VmgpiaGvaziF7UDzZ2Xt5qxP1AEJ0M_yDGof1pU7M153UDoCJuCUP3W5lHxeH8-5lopvBa-c-AdCPPqUdILO62TCIcBkYCYw_X9H2DMiqY_-vTOvJ4i1YTo-1QSV2ez_ak-UR_i0TjIf0NsUAOQh7-Jve9oQ8sEQuJhpq-bLp1M9LaYmaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awlp9jSjcP9VXM8SBrrKJ-mUATikDeP69tisV86VD48dCX1-6Nqfv_Yo8ahOJZqfuN9G_uEAKq7E5SieIQWxRH3igQtKJm_zhDM9x2p1oFopZ-EwmW1G7MYgUlsW5dGJFJOapPg9n4p7JvtCNmGaSDwVILJ3ZrWDHjUVdF5QYy6akRCQ6On7hmgiudP1dGkRdal8UbLQOzTMzL8L_Zfe58OBbzp2rbGYMNzDXtm5jTNw2tfLylwsrDu0orOqObZhyszQO7zIJkWNeO59zw_ypf2DzIFzb2VB2zVX-ltkX-L2rQO_Cg6BwaK9OA84T6Xz1whd3ltJnpoWFfNGIGMDaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtYxN8Cc2IuZ3u5fmtmFsJCmEDiFuvTz5EN8tiFeJBT5ckQS53EaZW_JeK8pwCd0hsI5skmCZEtNrmgo4fV7ySi69JieYoO-R9b4k6XnZ6hvgDFGjI_41R9L53MunE4wTOwBrpnhlNSV9TigMrWUHo6SYNKdSjnfU3lgFpO-_pt0_cngOFyXb0tUhUnVf3UybWQdKZW0vdAd60L8ae0jpOZe2lvMOR3osp0QVi7ajbvHhta1M6ENQEy-57QS6rhKg378b1pSUlzQC2DRiVfXc4Dsj5eRj1FM7hH3j0aAeSkTREb8EOjy-q7Qww_6oojdsYR6LMQr9MLezc4IpqS4Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiMXMUmIQzbP9qSVazXog2Ir4eanISMMENYk-BfSEdUMOhC3QQVtbTqPCc5SwH4nQlOurs-3-Y5VzlsAzREgoS8PH1EyNy7zZJ41_UMpC7qtQ8UyejU8KU0LI3Kn-u-UCuZ2YMA8-i2hTA2k0tqAITLIjIq3eUOOW3hzifKUmYLjs6NB1fbxLsGYkxeSm9UCK3hwChpmcTOiyj-Z9-PR2I78ME-j6_6kFyluGi76CtIsd8vMYJuWw2rWFEkMnYBhkrKNz6B9fAhZgooTDjyCGheZytxXNVuyqU1lU2q9y-eQATtJTmcH3FwhmR0zJZ8te0krGueVg6ozjTWajMTbNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfMCmxoXwdp2d6_458tod0e05wi2bXUru92Z49SDWaHTUTyV4dQWHcvioo4_olXXimdMm-kJnzWc_oFAgnE48Tnf9u-m1YwYmOkV2YsKi8lM_mJEHbM6kySK-ywvO-fIcy-UwsCtI5w3cuGS9g654-IBxFE81CKIcoy_XZH6KCusC2-tR2qn9TuNI-Hu7nJMYe5NBeQHz6nc1qefCup6BvoTupnNN0xIbpWBSgVkhED5emzNeosHdBZFdQmR3CR5fRzduPHn03huF22m41PNpmjtKmWYOktvw_53vFyMI2SHZ9bNvCL0SNldBumayNzrkoCdcoThh4Kr2af9bKonwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9di_pX1pU52Uo1lrNmuhKV1E6MEtXR_OF-cKXp6zQYkn5Bsf1qD7oPOxUMm00OHjRzn6Mqna8Dl00Ofr1Jht_OEZfHyvZ-znFUdL4kJ6wcm3JI_6lvHQFAwum6sATlgA4izxHwG1KJDFm87i4M891l35okdt7vWK5KlCLANZc4iAkqfuMwu-OpV0Ke-dKql5eoenEx5BGQtWRxXvWdn0BWsT7yTnCHDsIqCqCODeG4FzFllNBACgBLZt4gMGRgdjWo9eo2AFkJn1XpSX3Lg-Jnzp5Q-C6dIZYGWu3PDOyxSuuMN-J59jrbhMuz5ONhH8fq_S_uHqqV4yhX109uTkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AiKT7j-0sESkcInfDFXqr6MOgXwTf5ixX00w7-jufOHnCbj5JJVrYH60TpZDbfcTTgMouH--21Y3Zcxyt7hF0lihq5Aw5kw_arNH36eU_btaVv9eWGUc991jRiJU19GLq-spxhTkzKyW8LW4FGt1OYOjzo4GhjJL7-jtGO3gXUGWmMEoiCgztsHWkVmFo_xbI-BYmVBNojYsgJmIdwVptvr8kp01ZGf6z2PX2J_OmUlB03o6cU97doNRrLbercQHcC0_Z7KdtJBd9vrxkpDnqNegfYurRdUbwKj5kc4J608NF3I0kVn-O_wGMwR8iUaAH_3WdBOQM97XX_iOGm-tkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZ9r7mJGUm78EfXqfKX1TtuixOSWkFXfuNsgIzq9bffDGZ-m_p-vTBWaPdF0Tvg41sLrRweSqqgpwarwwm8tQQOxNNItUjp9dp9gENeTWIISvYHa7nNLK7PLqbJWu-8tdKT8_zLmtsXSQ9NKQaAH7HMAgyUGHTid3YhUbJRrYyE54_VYcpQ5WApV61ZXT-GBRhww7vzMMCpK73wHBR33VKaw9ScwfS7oRIR3yUVAeqZBSzhxse0Kb7mrIMzyBVZ53UZUGDXopq0yZWQl544Ziku3TZOeElQLnM5M9vhFXXJ9U6AwT1TsnTYatcekYMrXSJz4YOoEVGHQEEFxUQ6mdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vE7qGsXkwPR1tv4gG5RHLXdAea_-huAI4HToPc8pxWR1tOnyxBpAvX0IOem6xsqGO54Rx7vkOJ36ENSiziS2ryrKQh-8OrUlXQNfh3eo_I1pn8-Wkd-purEh86sm73tIJN0Xdi03WX5mTnkJRYq-H5r6yeqklJf4fFUSQ4fYeWlgXscSfTiUXfwuhsH8pqG3-XDM2MttGlE0FH0tYfJNvqOVkiVj6uTBSqpFCfRFXsiU7q0AeLZuiNOvQMFO9DySWaeqiudZpQgREnrIQRvOvWX_LauZW-6kik1Vl1D_EGfCQ3rDIc-rcIsvbFIIB7mcT5llkHkiGctlqeShZVOYIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0D7BN5uMWk5xztaAf2hWa2ioszs2qH55n56WCyME_dMDmQ_wrQ-6N5dwrV266yLiM8dlxsubwfz9qiS_q5QlDn0bU-UjmRnhXeELBGgs8DLJ5Qrd9mXyPPgAU6AvAzgtAwuJ2wKEbXta_Ku_Jye8qsvR5RvnYV647mJu3B9x18G-rmOeuaWZOPBqf2pYQjz3Z79JRQz2ngikYJWSKAFX5RnptJGdUDp7t72IeFWJRygqHzbOofD8mAY4AbDsQx4st2_t-UTPHnL7BMAc95bcB1J3B04dh1LaBjAPEnxvpEonmbWgIX2afgsn63pdc6s9OejA3KbwKIl6l-gTKL40Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OF_sxxf-aImZQ_hxwcDEqWCGLSFyiD2aAz2zI3qDFA9DK7kabP4AXHZs-YQrrKRLt6ClGXMN4GEmE5Irp9RLWl5SrWVJbHXSwshnu5kZb8G72GWWhPy5j-A-G42O3KMNkFbOYberMEfEIXoCO45xnqcepJ9Scz41HOqua679YxTOLPyGm1fXohho1DFvFJGuiDIwQD4pNgyXxJwo27KW97XeR-0HWtLYhGOpi0W2PQzrKyBRl9hvaO0L6gWKoAtbkHH0BYdZIlOU4LRiK257oYXQER1OGfd--CicSQ4CbdhIE5xBWLWHpxOq2NpEB3wV-eBbsXzHf9YZVZA_iAJYuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NDm7ywQF958mkNr3xqN_tlo6ACNxzhkVGtLQ_qdPvfSh911MSECFYF4LbfiB_8RbmL86LOMQXju2qOXWnolar-gcASTSvuikeQrZQQDVML272K1WDdMnDMH3nDMimRIJgjLHTB6OnCHZliNHW8ylHFXYezMsujqmEGSnWGv-IbFRkCcPNGWBRbWBimiDRuee_5a0y7W8uZGWAVaDB42WaLmeDdw2sjfFWW96ce3CHZzWlwr4A_UIcGAncesfTYY69nCHcHaPj6uzwA4XVZJn33ZFgFfnkFB4Rp6HrgneHF7_2jSAn_yP9w_HTRLynWBN6wYGU3ZEQYesjivRschXsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iZnSRQYLGnv6C1fHJlrwGr6T8CN09bnhxNiJd5U8xzHZDIj6lOBcrrHTfsDW_YT115syP4fvT5ngO1CaAquyLpXr367sUQut8g5CvBGK88xO-u1M36JKfAXSwG95kBs53DifmLCoajbryBCF_c5lUHVHwK4Z92II4bJ68C5aT6SNiyYVtqzWF1X8vjXW2fx8_RFb0LIRIbqEx03xwHTkgmLCikYQnA8ptrMYuY-col-4QSEwKRgLdomjmSUjwb-5oAI4T6IoIgVWDa9b7jC1vOBJS0s1LLc694aQKZKEhVxjT9tfbh2V9mV8X9kbh3bN_u2xbyoLl8S1IthpkF_ohw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzTnFBuAzV6LU2gVC_zR4k7xVl9n5Y5t20Dures8ZDfj8q-CLAHf22DFb236yUSQRLNzemu615HzumrVDRFrhOHV5SPW3ZbiBU8oUEObpnoosBz4-WMFI5A8hohL2Zt8j25Unvc59L8CZQxyA-5YIqIneGvP_xLYko6FV26us1wNfRv96oknv3IkaTjEBODUKgUa22SfGdrB8cqdLSYKP3TiSQMME3vJoHnRhP6kSLJwQNROJlABSk2MXFPzIXp2LlRiAzb0uTQ0GlbXLlqcMTbTxaZoYozoLdhyPxV8hxzNilyaO07bRjZ9zgIXg5R5rN-dQcH4_FEZ-eouk20U9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPW0aDfAPxDzLsPNtEufb01bAfA_HolkOnZiP6gyh7N_4xAjbhP1caFUIugGECWEULWD3uPps4QBYHwa5svgBVktyxLT5Eg2dSswoHJ3gA9nIxdYatdZEkXqiVdmcqi0935b5aI14OZYssjYhWSDIBez3cX_OGL0y70YSg2mvG_OE32sIJx6gUoJuxXJSZk0Hq08brTFsYC10C3Z4KOHF4obWz6Pvn5fPDYUQoloO7xcga7QLkd2NDgHW_fhrRRLbfgLVIiIfduCcd8Uo5uCw-_3x8gaQTPnSTWjPFLzhhrJEgmsCmdUXTNFhq4E_XwQMaN6l0Gpp6VRhXCwYEt65w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLMF8AdUit-mQt6ML1vw1Tb5JCEsLWoWYYtQyNIl176iQGBce6pvsGfQQFm624yOnASIWPRIAwdDJ3Td1L9xbK5_LSkMaEoUNG8LH79s3EHHQqa-_Z4O0Ueh7bDmUDDjqeIkusNfgOpG_MfdIKUaQc_uMPJHByv2latgpMNCmd5j3RwwzayS-mHfCh3dhkw8LKFM_hWJN_jiW2qYzhDAao5T8vptMEFHp5_da3wgWSxJ_HHxO_dfEk73bOs-YWBAMrgaG82Rmob1v89VhHcRleher0YwXGIFvFArE6hJL91p08IGWLBXtbwxJAho5lxGurWJ1F-7VcOaYSJTICJNMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZkAs-eY77U2Bh7guASTCvPOi3NFJLMC-ucYvAIexiYr5l9MhJyCSOE41vfXS4IXzqM6wu5K_y5-6bBRzBjENq7u19OYo6ww_VR2w8SORl8GbQtBxSAEPOG5qJfFY3DMljacBxF0kmGPfwMG5SzHVx-McchrRXj19-iG7j5RaGT5Eg40UzAvj9ISYguAecSjShhC_f86t8JJAKMykeouW0hPuPuPNaavaRDvAR-GYAzseTvaR5a--Hw4CFh2q8S5xC1IGxT7-wqfQhtXTZuFSxN8z3R_FTAVf0Am6-Wi8UL-LLPKUIjPTx3pSFC8GCRG8aKGxoqR-nPEq7fX6QhiZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mm4jwwU28wTLTTiAqi9i12aNnJ10-RdlsRH6wZhH8n8pJl_-GqLsU9pmY8rA8OEcveN0BUIxYAy3UMCASJ7PODPIUFY080FkCiXq-hgd663AQoG3X9MLj4q61bT1SSOTzK1Q5pWKOLPXuzQW4Dg-Av6BzFvU8j2oZXJ7erfHEuUqInG-YtCr7ljsGIfDHvVm64gHgOAZ3pY2bnMY8HpzSRsQz5fhW3WFxV0xGfKe67def8TH9LaZrG8E2Y9RlZEeEzdHKXrt8Rz_4SOS2xcURlAeLFaGD1Hmy29-4ui8XuUARYC6HqrnQ2VWArpxxXsWUCz8jhLnTqS2MihZ_Oe1OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZdDKNATQ0kQi49lUKJxSGrLqO49FHw8v7a_AVJFExs8rAUM_o2suTrun7pQ_zUQQgbPc5Q8FnwbUNCJ5LHKuNNDiMV9jLwSPhFMMuFHXinjXxKhVSSyKL7JSaOGtdO7_6vVLbLMpzJ8JHrJVgc9llDBIQGXIILFyN81CXF5I3dK_lTiyuXWO4vz_0H5mpiPzw_8in9AgDFPZRCZJem31IyBSHMgmAnqdl7v1TNmLuLMEDvl_2wr_N1U76FoOodY5k06coiYIWjGlkg9-nBgq5v7_sB_KHx7xffjELriCCDCa8CzVzzQqJ6356kV9RXbq_clE9Ppd05Fcr80pV4jig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHrpnoxxx5HY_7dtY1BdBoxRUD7DtqQXMZUIJ7ERJssHccUbyTInRmakX5QvOIGe4OyaCcSfq8LMKj_e6cf91GmUaBSJvfHQsM4haOJFat372w3W9WOBgVW5dqxCvU7svTderYdlD2aXDRpZR3kr7q9yHN1Y_1KQ03M0C_fFOOyXhiIHsqIh_d9ZYK7QBFi-eFti24t-nHuiJsKY_V8qs7IYZYlTXNAhCJdSDZZL_TlMwJBTl_lXQC3rm9XhlL7McUJVS_zhocvpAfsiIjUeeyTcECIwjEHu0JU2Gnzch1vr24_5mqfw0ckswWzJxPl7jvlakJ11gtsglE1VSF-1MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNGvHXx_d3lkpwb1UgslWenzPa951c1SWILez_P3FkuYS-mmCQk-90foKIi2FCctoKK4yRjuyY0daBPe-ZWM2C8MkXuZniNFGULrY53XrhsFmG8WMyhrL0wcEiLzF4hu9TxD-GQ__i_2pZi5HWCxpYM2FyCizREhpTapGFPy7Y18jl39FsYC4Xi0995sOnqYIGZsmtmfwCXBpDssjP29QlKyQrVRkueT2zsHIZaFsqmFRHwQWfuODlsfsNXIFjtQngeNcqdElNFGbnRANNN05NsGQ4Kc78bdQ0AHa9a84JIx6eF2jMknNI2I5zAvjSkGDjBxhbV41BeFvxVL50uB_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEIi0xqv9NCRIVXIBXa2dn-qUbAAdVVg6v6n_hWnJthPGDjqxmr0dhf3WbfQ6-NHwewe8qaxiwpMC4jhlgIPcxsVBY4zIodFRyQv8cnHFiOf8s0tBzJlOvvU5O5JEnGLNGg-ceIebI3paWWSRoU3X_TNqxzf0R5a8Ssfp11d4iJXbHstxQagp2GeIZMn_vJQtAj9Alw9jQArw7_mLPHrbk5eIlkwXeWv66r6wPuj8DdT82fMCVoilmHtu_Fec71GvVhZiWTrvb9U7_k9rBcXF_ywnFbvQZa7dMTyImIGMOB2F7WDFeTZkrNTAnmhOkwHA-ghX-MwemHUhoVoyWXkVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DykDusSOxNLdbz9hqxxkwH-U2rwz1fcz1KEl3kKf2ZtOT7ocS31mVeM4mTpZ1gi5CJBM8Z_l9QykN1YEPMLgnNLs4_Slmki7dZM3FEFqtBeKrzjiZo6nfwnIl4VXy41hM-LPH98zB_ggjCbbnPGm4utkQnBZk0I7GIIH_JbwoMkE684xN-1BfioDACmfi7rv8-Dz7CukP1GXXDNgYjzAl5dQ1g4p3JPVrLjCxDK91nym8I-garDcKz8FxlmWF4VNg4T2KoR7ecyakji1zYEy58IWMysOSKx6GJwwZkiWdCkx8QDobKSw86XFMc2_5lRR2qo6uDQUSN-W6xlg_n2bpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8pXlMIz41NizKne8HhwTYVmibC68O_Os7XRHco0Wyvm3ittcF6c-F3xsPdHHHPHlo3LI_fkHq5gslI6ebCLUxutFFzDSKRrFS0ndwJ6lwpHslzQ0mtrIKw_x4w1sVg4MHuti92D6uvJNANHqjKz4fge-eSJfNQqaNQ0xXd4NgLOkEOIiLBTeKjChEgBtKToh2Ig7EFnw9Uw7iWaQMlxTiX7n-TUX73P8asB3tGRK6GuRUDutwD4TEWuk7Ie7YyUtlBoLhrD4ZsdGyJVVw2grwt7ftK87JI3haFM4m94cvKld8i6ZjNa-bTLoRw-5tf3kqIxppMNxJCLkUu-WmSfAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOfnOyvIneVTygyrbvkweiBR6LCQyIm4KPNR0YqvJvKcawGSv1CS-yeJxKBnsg3MAlaaOGfQ5-KYiHbI01XaEb-lXM9286FcDB4S-5uednWOM8RztAn3FlQzcRCQH8V9GxjeQHEUihwU4Ha0NU6qPP9mMPAi7iWvsVqyDh5YCih1NutMYTaA9cBp5yhJQSyV5h0lEZiMABU4vG0yThRGie7bF6yBu3_XOfkU48M0H_LX3dDkVbaPELAs75Hi2bEXtiqgAYnVq4a5UGtwZQo4XTH7Uy6-6PrYW7h67QD6QgNLbLZx6Hznji8TYkI65AH9l8pnpR_ojoj0YfYYTbLMDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHzXO04qjcc_LWAzvyskxG1GRfmeTbXdq14kpRshe3ox6_V1xCUxMCfQy0xQHfgH-g6eucRRrLx5Gywam9QTigPttgjUgIZgGGQkC53C88MtiuamDOk7DXvs83V7aBn216aEfhiBkgTm5ejaSTACA_HPgQgsTgXYBNDCm3wO0b-9qO2VRNr56mF_9e9ruTTijASJN8kAlwTprBnJ7O_YUAyzHeeYj3PK-bQD4GNEe4CzoZbQtXSLJZRIES-c3Q6SOOQG7E-0f8QTbfaPsfFxcvFwNRtGJclHqabFYCqAkGuSxsToDLsDaHH8bDopYAeQ9vaCQK-6FZDsMyUZlUrqAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5XDjGlTvytqf2pR6qHHqOE7OAhaZDQhIapkPO8S5wSjhqPh7R8-08W9DC8tt9LFq8cEy5j462fFNWg2IrFIFeUpxXHKl-mdJa63NOWRwZmM4chvs_lKfMZ1rYh9oR7bz0AjSmFJZioP9XcUKKdwHaOPFCc_8uSeI5wgSPX0OL2OQJfMqjMr7FUlxXTE5v-FM51a-jrcTOuElcV4-gsquUQQ-Ai4rnorUGZPlyhlenYNWxCHpubR4rfHiTiGWW5OT8iK6K9X5B9gH0zVynGh0cI5heZMGeBaOcbsUaK4hLaMeJdV_Q09lMj0wMAQWYQTdPGvTGtfQEJnoYtQFYGNOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-tMhXAH4FelIajxRMNfFf3FPrADxQjkPKO9bzGm5I0bzVVHC3zamKbQyNThz_Qm8aMJMgKPWa-_TtZahQxanErKZAKB6e3SZtN5maEGgZTk2gqQcNyu2GUPRQcPTu5EogoUATYZrZvB9k8ew2sQBmvbzd57rbNZuhn4b-S45vdcm-MMIG_3hKWVYh6g7149VHhTp81ImvLyK_C6JHIipzx3HQrwlPB0gleHLAYl0CtDHMMa26c947tj9u6OU_EqkMFDzBgBlnsJqSKCr7n6iDDITcrQCTt2JDCcV6kNhmOwmB8zRgel0XB4inajOL2f2ldsdgb-gepar3eCU-kSdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6596" target="_blank">📅 11:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6595">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Or49oK9btGSpqjgTQwLeG8PQhvi1RuiLEmUcupXGTLJhec1ttGtHn00FS3MP89FCQikQ3uxHqTNeCJL-mI1aBtJduIPtvUJp10sL85DfGqJs77Ymbi8vDH03-zeQF_uIfO82sk1A1bMxULD1NxlrNhOGn3mDy94EJ0CNMGj76sj8ywKlOorDUKQMvzquLh1l1AmEYKnCpzmnLZitRLSKVMcVpK6-U-obtKr7U_DnMxvwVTQGZqCnBlqTlhgYeLErYL4F8P7dPlJ7axbPL5peExt70W11LU6cRt0upGLC2OJXyfEbVTEjkJEwMsw6FHjBWc_MiRkA1SgqSTivBSfKQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6594" target="_blank">📅 00:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=BjZqxq86VZxwpzZmXxe7kTh_1FCFYU9BKzvpHcg-1jO-RfX8DcgRgWJHvv6Ee9SU-tBXgqnwUiy2bM4LZkPof2dF1bV7LMqH5qC0dlaWcYz0F6bo5hc5grGZ86jH9gOKYUcEOTfwXiOpDKbJNFrpjmF9NJHAh0omUKi0cvEAHMqvLdwF3ALBszer0T4WcYt1Zfbw8NPSIaF1xa_mNFvX9s5BSvSvrebO4N9bmTYlaEWEUapyF5sTWbNwD24_F6YQwujJvj305m10T4n7dAwoTj5wXz4vnHsXVqBkQk0kTbAagsS-AnPKaIP_anGZ6DAzO6upbuj_hYinXEgNln0LGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=BjZqxq86VZxwpzZmXxe7kTh_1FCFYU9BKzvpHcg-1jO-RfX8DcgRgWJHvv6Ee9SU-tBXgqnwUiy2bM4LZkPof2dF1bV7LMqH5qC0dlaWcYz0F6bo5hc5grGZ86jH9gOKYUcEOTfwXiOpDKbJNFrpjmF9NJHAh0omUKi0cvEAHMqvLdwF3ALBszer0T4WcYt1Zfbw8NPSIaF1xa_mNFvX9s5BSvSvrebO4N9bmTYlaEWEUapyF5sTWbNwD24_F6YQwujJvj305m10T4n7dAwoTj5wXz4vnHsXVqBkQk0kTbAagsS-AnPKaIP_anGZ6DAzO6upbuj_hYinXEgNln0LGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0MIuS7JXNVHHyimf8fiW0mwOULslxSlY39e2UoofZ8LJWmPgyrQlm9CKCZSV7cL228vbGahUhnuucKwMMJpJRb9oPEoagkgseQhMtx8636Y3s0x_BtdvPScIUu-SPKGdtwwi4ho-jrKnGfStaxjr953Z_ruCF9RRvRJeqzzVRU1xfvIphYiahI4rKIe32bIysxLll5zKMrVXpEci1_Ihu1EpJ7PCjsOwUH1nLdajXX5NPk_swtTMLRvRxTEInetkNFVIC6IXrU07oOkP0Cwt2RnbRfRyH2dLsQJeIwppMcDcO6J9XWTjHH3cz933FJofe7PKLKR13N_4ZROW_cVGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=YgDgzqABkFJA0AluNO_GVMK4YzDN9Fr992asp_GDwdGUf8xvt5kv895pTjuzPfn8Z856EDJtVVNL5oNJty90is5AWsx4FqI9ru25hcaZqDrj7ONu9vJVB_v28o5vSmo_AdHvQOirvodhD68ydRC-GNoaFF-dwFGK-p1tiTnWH3WbyfKrkGhKF7NUGNhxIPkp90zLCzDfI7CufWXn_LlPUp7ZPDZ4Yh5ptGx2ys4v4d2goBEa-5hVJm0ZjyipA4_gcTdcQduU5YcZoJERCva9-Dot3Ni_eywQfidQUWwg-Z1lMtCGvfJIHxa5z7UubSmfEpz10ji7s3QMXAk6wao3NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=YgDgzqABkFJA0AluNO_GVMK4YzDN9Fr992asp_GDwdGUf8xvt5kv895pTjuzPfn8Z856EDJtVVNL5oNJty90is5AWsx4FqI9ru25hcaZqDrj7ONu9vJVB_v28o5vSmo_AdHvQOirvodhD68ydRC-GNoaFF-dwFGK-p1tiTnWH3WbyfKrkGhKF7NUGNhxIPkp90zLCzDfI7CufWXn_LlPUp7ZPDZ4Yh5ptGx2ys4v4d2goBEa-5hVJm0ZjyipA4_gcTdcQduU5YcZoJERCva9-Dot3Ni_eywQfidQUWwg-Z1lMtCGvfJIHxa5z7UubSmfEpz10ji7s3QMXAk6wao3NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alqQ36t3hKa3DokxgMk3CvfYbw9v54pd9Ez1W4Y5-b4AIsDpyo7apOhrwc_ay9HkuqxoG96z9DFTILuaW-Lgm5Qlzb-aCCf-SAtnuo5E9K7-6Sd8d9IlvcwgZF9XlwJpjhOcw07hDz6aDBw-PLb9RqUsZGkGsYGoJQOMnEs7FRK29r-SJOseaLF8Uq5uim0pABDeZzOvvzebFTC-eH_EdwV8_il8Ygp-c4HPWMzhcO6fvC-iJFCmlhbEkRuOzi534EJ1PJTXpvEVVISxopKlxhei9BBhJl5AtcVoPk7QglE745kBtac96HOZPZb-7FmaVD3hZRufNTG9jmws_c7cLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOC6_fZBpOMI1W4LZ6BznqU5sdc094aSM0cEG_nd15UEFVBC3iA2TtdLnEV3H36tA3hu0VE3ezztSMNPZcy7HumYPHOnBHANCCIhk_if3lDJhz7pXOKTstVO1K8j7mePi8IwmU9vokunEHC1I09gSXSldE36p6fgnCVmA7Dr_7D8Xomno2ebC2_rbTOX8N6hG9LziSq6ezOFPzm5WXEEvc1BYgMkkExp0c-a_66HeVDoW7Oph4jnjh8wRKqqpdK0rtaJhmeSdIOnNExR-hRi2kzoG3si2wKxHUA00BSpLx_FuC1x9X_bRO3VE14KJOcF9gwQE-50_K91haQ6f9yffw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=d-XbkU_G9spKe8LE11DKhqbv-S7WIM_OpcdDLHy1rGI3lWRy84_7Mly2nyAAFbfHYgtN-ocObo8EgZHFprCO4OLLCWzJNB1CUmYGNKhmcUdQ2VWiKh4DLQhcH9PtaSgc2KIgSRda6CjJ8ftPc0BABudYCRzwLiHtUO4vZSjZsjjnJlTBPvC1CdCMUjlv3UFZSvmmNRmuel-plzCoqYXro8RSqcCbkkiv9oRV5w2eFGhzDaliFpxi4eHJlaIdat5y-JFLhpoYvgZQdHQNiBaXrVNvPXAImB_VRRPMoodWwgdDe8m-PDzs_1HMq-jOorTWk1uflv6NWn0mguFx2k6f4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=d-XbkU_G9spKe8LE11DKhqbv-S7WIM_OpcdDLHy1rGI3lWRy84_7Mly2nyAAFbfHYgtN-ocObo8EgZHFprCO4OLLCWzJNB1CUmYGNKhmcUdQ2VWiKh4DLQhcH9PtaSgc2KIgSRda6CjJ8ftPc0BABudYCRzwLiHtUO4vZSjZsjjnJlTBPvC1CdCMUjlv3UFZSvmmNRmuel-plzCoqYXro8RSqcCbkkiv9oRV5w2eFGhzDaliFpxi4eHJlaIdat5y-JFLhpoYvgZQdHQNiBaXrVNvPXAImB_VRRPMoodWwgdDe8m-PDzs_1HMq-jOorTWk1uflv6NWn0mguFx2k6f4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXVlcSL1xSn1Ylzc0WB-TfaGrdYEqYyvSKV4h9RPArGM09Fx0AN8E89GWeG441JQFpV1nS3vvQy1LZq41eCCbN-0S8szyi-vk3PGqxvY8fMQ_ONBNjTwWzVOpCktdcqCo2ZgAocfROuspxH_fn1c86NXbVPHy_Zk5u4jMUtPRvY6xetr5zvjJQ3mxvQQYbLRN7Gp9UOrZP9IwDR88B_cGzx1thXVgKlQqenW9mzx9LLB1IOW-uEXipGXbufEiDhA2ZrnNGpwNBpv-KVIHiCs-X83a6TUtVcd95TqhEMfRvaZFyWHCqjL4lyWZaQJu5RGgifTnjYgiBZhNxsYbvoPpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه
اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد.
اما اين الگوی
به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى داعش اقدامى
ضد اسلامى انجام داده؟ پاسخ صريح : نه!
آيا مذهب شيعه، مخالف اين كارهاست؟
پاسخ صريح : نه! به هيج وجه!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6579" target="_blank">📅 13:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6578">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BX8q0kqBWomonxr6hue66WlPu1KWuHtZ694Rp0VwUNhTetRl0vpMzNB9ewj4x4ln28kTrMPi54yK7VgqfwuRf2khCGRk2FagdjOjEbWOiTZbPUr4nx2IhoZN3v4Y1Tx6bYXlnClYjpeOhWMEQMPkCswoLNnxQ-aYpbdhaM_F-yzNyb6fywou64Wbetyn4eOF-GAUzJ5xUYRE3qaggzo7qVvEfvNsmjoFPDtyNwfKcHhEJ_0i1pbkMwwwDgaiQ_wx_mpySEWfE8Aoz6_vpZ8h4q0Snw65J7_Zb4fp6ZjO69VVMMCQGvZsFPEFYggqlSuIiT_FU4TbccQJHnZaCINRiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhTLxFsudpOcsgg8o-ylRe0iT59yIEQt9aJDp2Zx2evMUcgvnkdTxjbNSZgB1PCVm5eRsSuryHRppmjZuv_XZerCArMgpGs-ystz_ClMBWU7RZlZAKVndT9onQ5N-zBzrPX2XT1pyq-etn8vHXQNeklP0xOtdORQZCtpSqUx71JNlpP8ZbhfyI32QdKdCSKvwDuvU3Lh2jSNYRXpDpvO23nPJLpVKb2SQsFoDGIqWnM6hw9scknlPO23x0ssgWICsjVBFioKnBHWVGIwJpX1w2euP7vEHYL5EZwjReqpj6Ghp8BeljlsbBF4vp89onthvu4Cwy65qrZor5FA1Domqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=bdRv_W1n3AEY1NCQaZWrz6yrjrX_RaVshkhF54qANMOh22y6lRWZVnql18uIbeNtXKwls6ObeRmZj7IKYDiHJlyML4_vllT3AiyrbW6lxwjPcejlmOnaflkuwcEnnJa6FkVHTR6IpTzBTBHB9GQraLizuD7jgMWBdy0T0OIDLGm53JrAnvp5-RQCwPt-EwKn2j__bEkmM0znOSW5YhOc2FO8dAsc08kic54e8grwssrAOSwyfGVV5W684hsLeFKF8oGofC2AJ8hIj-wJF_bPGKWFib_3Snwdkd3TopHTO1Z6S7pZFN50rx_o2STxRkCD41NgX1bx6q_mBBvsAumAJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=bdRv_W1n3AEY1NCQaZWrz6yrjrX_RaVshkhF54qANMOh22y6lRWZVnql18uIbeNtXKwls6ObeRmZj7IKYDiHJlyML4_vllT3AiyrbW6lxwjPcejlmOnaflkuwcEnnJa6FkVHTR6IpTzBTBHB9GQraLizuD7jgMWBdy0T0OIDLGm53JrAnvp5-RQCwPt-EwKn2j__bEkmM0znOSW5YhOc2FO8dAsc08kic54e8grwssrAOSwyfGVV5W684hsLeFKF8oGofC2AJ8hIj-wJF_bPGKWFib_3Snwdkd3TopHTO1Z6S7pZFN50rx_o2STxRkCD41NgX1bx6q_mBBvsAumAJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=Ue4KzY5fXW3qFHg2zzp4yY1NOJC5_YsCcj76_S04c6FNceZttQSHbeOa7J1TYDUMqdp_MgoJCYZdM63H2UyWnyeAMSIVVYbDpi0jzdZLS-AUuQ_WefaGBgfrZmDdBYv6HVkGNP1xcBJYErkNtfkDy-BI1qLcrTuI2-uWiTav1hKvpxFdZrSfX-TbYAKi4JabkBvufLy1ZdPrK9YiY4MJ6utJfQO6l06HUVu7fZDfgcm9qc023mSqSJ3cz62kDnnCJ9JcUi4gtBX5bwWGfkLk_7lrwxy8PzxthYI0McGiSD0SzFRXfSdkhFWVEenaPc-9QgPQXwFHDj2lsB7wDHVsmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=Ue4KzY5fXW3qFHg2zzp4yY1NOJC5_YsCcj76_S04c6FNceZttQSHbeOa7J1TYDUMqdp_MgoJCYZdM63H2UyWnyeAMSIVVYbDpi0jzdZLS-AUuQ_WefaGBgfrZmDdBYv6HVkGNP1xcBJYErkNtfkDy-BI1qLcrTuI2-uWiTav1hKvpxFdZrSfX-TbYAKi4JabkBvufLy1ZdPrK9YiY4MJ6utJfQO6l06HUVu7fZDfgcm9qc023mSqSJ3cz62kDnnCJ9JcUi4gtBX5bwWGfkLk_7lrwxy8PzxthYI0McGiSD0SzFRXfSdkhFWVEenaPc-9QgPQXwFHDj2lsB7wDHVsmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvSHb405Kqe5p1I28uEt-eAjRJJRdiF5AMQOP1AXuXrBOYcNKNVHRcNm02B6s08kR4wtePiXruJKsuVTvT5jDY7-StJff_WtGk088iIekCmAMbCPfvqNUCM46jbLaNp94l05rQ5uFu29DgAE3fU2e0Zn68nlRXu2-eF7wTtl5Tv80rOU488jRPDJQmf_9be9efAsQ01N9A7ixbG4k29KCNXxL-g3UGw4q_PNSWSSPCsAiES2kSMvUByaRFVOLV94vFOdmoIp_UGq6Ak7MXlc6mXeIIU-OlQ2oEgWqlRa13fhac4y4Y4sfTLrRUHlYzf39aTxtEpCF0vwzEpRHtZHvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHAKQPpEYk4j4wEZsSrQJ98wwRgBLhIaKuCoHNghXi_iCQHlddmMN1dIVASRtDccdc4HBUNUzja__egCIVYLqlWDDgevS0qpxrYqnat39de6FjPtorAAugBTp37HxziwgRcLyqvRj1EBO6GceNl49Gn1rgdKtr8YFiuTef_l6PUwrcOsTDQvRw4ZPGyEnn5Xl7c6m5_aseZqqUobt-skWzXz9cGPSNWQ5JmBPN9JGvXrCqdFWYLqRfPnQ7B6fIJoMnqWJw0D0f-eQFJTBL71L07wc1gWnxEgvLz6qeA1vhCsJJShwf_93J_Da515mSokCusN6HwPcgeovDd3latk3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pK4vwRhLqMuh_N1uI8UC89JhF_VyOzSHNkTimejEvp2rmy1HdlBw8EcV2CrsNkQKM4dn3fv1kuTEZQpJsVu3amTSC0v6sQW5gX8UlfeCcpj1GlmslY3p8HVwSe6VhcX5QYTmRrfrgG2iQvbXFHehJlcFOJ_8XHOEgxXDAmYA78MbwIZ3V-Y6s4b4aTWJJiWTCYYGY8oWi3jf9QHBAfgoyoeun7FEHeM0VedtsN9kxHZQRTLQ92olhfZl7yQDIBhzIr3PHsu6nOTm9WmmAm9_1tqIMJdKm_Y4Tg1tmXOBSO361A9icVfgvnJi4N_FAb9EV39lAtW_z7AtbfQGBBiuIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyecLcgdDK2BL3jVGi6VHSje8a22s_8XLeYjmMFT_VUU8fQaJAP9hY2hy0jIuBv08NA7SN_RMzmVPiEELzlWZJ_-Jk1mWFXJQ5DRRKikRZawqDQyQoavV00GkSLkx_ygRRJx6ebfSL8t440lWrKkhTXuiugcRKszQRr6IQOdjzhY_ea2A0hFKT7QKEHnR1Cmwokxs-tXySOMl1mzPX7GdEFmsspXIUONI-IE7BsCZMJGEDRABb-tBXCgiOSceWQLxzz8drrvF_gR0IqtTqeiEZ8iE9ypu_donVwoXbqxuULzYX3B29DMFJYSZC6JzLaZXSj4WkveRty2faXunLq2xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBbuvRCaee_ccibGIE4cjraI5QnQJJm6HTc7bA2vwarqSbRT307OmbPOGBQKne8Xh50oxhlEUODIZb6d8ZPdOdqYHXGeOhlcqOycYK1Pj5g2mg1dR0hWhi7IYUMwNTcq8vUv0PPL9rz91SvzrAE8b1AWpRZ-zMI5nc0PtD4K4STBnaR1Oa2iOEnRWbX9iEhtolNgAN-DUnYNwSI_ZxJNOtIBZ_QagKUg82GdZijr2zgXcxJZA8ei1n0yz8AVCIvnE6ZUzSGwwab076qhu6F5z2dseybV4IWW4kFY53K34--bavjNKOO8mHkV1sc99Yq6G0Rns9Q4PQ774LpPSmqgpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOMoQ3mFz-ooVbxYj9hpudqLRd4Ob2SfXYOcyttpGzpDF0TXc5ngzM1kS91DupdBx9Obj7vOCNKstbR9KXTpQSCr_-9poP1G-vqHGe_kNqXnl5DWZp_uulPNu137CUEeHG_IOIdmPPHqwgUgnoCtlD9euSOqyozaNMnOzDoIDKSa5FDOZH50Mda9rpAg86UtBfJv3KFkTnpZrXgDMQvACiPjcc6wpDezyGQM4XuvPaw8YjXgLzn2QE0462-1tK1bR79kqzDsLeN-ga97s1BxiX0HzYewcR5XZWh-qkegnI4bbQDBEhNZRdVq9LKQ47lORmWX145e8p9nb-ci_anHnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdoIjTnio2z4U92H8scPlSMQDGNaqmKI1inad3jYDGd-ueEO9_tT9nIvVXG3u1yuwkk0Blbn8b-8BOTjbgVmYH3u2HmhiOnny9DHLFXkNA_AkpXcX9AuPM5HNEvfJFAt-0tOnK5xSPHF8PqP4qi7-btCTAUSI49XHaGvO2H2_3exRGmNFPLJW0BZKN2NJyBjvKGUZTnCJXP858BLn3JHQGtx_k6_RPS9Q_VUT5MTjtB173z2eGYLnb7NeN7T1eTRsOCsWZ4AiKGCd9VeZ5-Ey2rpPsOyjdS57Fx9zfGv9DTumAKUtxsaQBRXwdnIPiXnyN2OcRpHixgdvNQbIqUTUQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=ICF3cO0fV7SxvrClCN-U9dEC4lykwxP5GEhjL8sAKfIChY9hMAgAKC4ylqOJyVBim087XyZdTt0qIdA4wyRFPXgATO66X6tKNuDpkpBxGgHTx7U6vK4zFFOgZL21RP5vHjuOGP_J4jlrE_TKD-iZeT6RgS35LB6Sbd6HibUD21wcPLi4Vrx4UkJYuD3pBJtxSzWbuoHwDkE-qgewEEmmJrCHJ8PyZ52c5tO2qp7802lSKnSoEQtGgchrX43feARIR1DwFxA9HxNIrgrU91VGmmsMBKzK5gzTWgmBU_pd-GsVciCNpvxqw5yiTW1-pEHSm7lEXJt17ATD3SmIh_52iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=ICF3cO0fV7SxvrClCN-U9dEC4lykwxP5GEhjL8sAKfIChY9hMAgAKC4ylqOJyVBim087XyZdTt0qIdA4wyRFPXgATO66X6tKNuDpkpBxGgHTx7U6vK4zFFOgZL21RP5vHjuOGP_J4jlrE_TKD-iZeT6RgS35LB6Sbd6HibUD21wcPLi4Vrx4UkJYuD3pBJtxSzWbuoHwDkE-qgewEEmmJrCHJ8PyZ52c5tO2qp7802lSKnSoEQtGgchrX43feARIR1DwFxA9HxNIrgrU91VGmmsMBKzK5gzTWgmBU_pd-GsVciCNpvxqw5yiTW1-pEHSm7lEXJt17ATD3SmIh_52iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مریم، عروس «معصومه ابتکار» در نامه‌اش
به مقامات آمریکایی نوشته که مادرشوهرم
[معصومه ابتکار] فقط مترجم بود!!
در حالی که چنین چیزی واقعیت نداره!
او «سخنگوی گروگانگیران» بود! که برای ۴۴۴ روز دیپلمات‌های آمریکایی رو به گروگان گرفتند
و واضحا تهدیدشون می‌کرد.
میگفت شخصا می‌تونه اسلحه رو بگذره
روی سر یکی از گروگان‌ها و اونو  بکشه.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6565" target="_blank">📅 09:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=GFKRbcT5AVrLtGRHDQ7ET7KLxIwz_AqHs8Fq713506lTBIJIhXkhO9voQCYZxZ4mdeF1VMVhrlbIeFDEawGRgraQFnBwtY9LCoJxcAtyFZCJ0q788-agDOvSiM7gFCuMfzv-6Wo6z5W5-7osSZApXclkpgwT0cwIfgb_hDKA2rPG7UaLERKSx-FW-BliLbHvNM_U11moidY0xUYv436rnW4Qgw7cnobCI2FEYd0fHlHl7iOfFp_l1bc6_Qsjy9n_vuoDZY3Po5I6Lp4GvWQFUw7Q2qfpiJe-7Q-K--G_jsiQjPu0YiCFa0R-9OIb1df-qrAU6TCqdXS4PAFDBDWleg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=GFKRbcT5AVrLtGRHDQ7ET7KLxIwz_AqHs8Fq713506lTBIJIhXkhO9voQCYZxZ4mdeF1VMVhrlbIeFDEawGRgraQFnBwtY9LCoJxcAtyFZCJ0q788-agDOvSiM7gFCuMfzv-6Wo6z5W5-7osSZApXclkpgwT0cwIfgb_hDKA2rPG7UaLERKSx-FW-BliLbHvNM_U11moidY0xUYv436rnW4Qgw7cnobCI2FEYd0fHlHl7iOfFp_l1bc6_Qsjy9n_vuoDZY3Po5I6Lp4GvWQFUw7Q2qfpiJe-7Q-K--G_jsiQjPu0YiCFa0R-9OIb1df-qrAU6TCqdXS4PAFDBDWleg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6564" target="_blank">📅 09:06 · 24 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=MQHTRVRwaqmilVT_yjYcgCvjX6PoV0f2a-jJs2vxuEppFZEvxflM_twUFjRGmHCwgUunin5rXba_onsDgzRxh1ifwE7BMfM1l3IPkDDycqDn9I9gZyls4Ro9IpVr-mcK8umOgGZ9QJqLsOIy0FKX9CmOcDaG_0fWftp1d9B5JLjh4lUijPIJ2edygH9jQW-BKj7vl9GZUj3CmARcPOrGcUJ-Q9t1GGPdp6yIEJFCqiz5edBMcmSPToXqSuxDYKkC_9taZ6uA7AVQS7reObMm_XiwSPM5S7p3geUWYVibofMF159BaxzsiM37vJMpH-ZzxGku34kukofmpD_ni9Qqcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=MQHTRVRwaqmilVT_yjYcgCvjX6PoV0f2a-jJs2vxuEppFZEvxflM_twUFjRGmHCwgUunin5rXba_onsDgzRxh1ifwE7BMfM1l3IPkDDycqDn9I9gZyls4Ro9IpVr-mcK8umOgGZ9QJqLsOIy0FKX9CmOcDaG_0fWftp1d9B5JLjh4lUijPIJ2edygH9jQW-BKj7vl9GZUj3CmARcPOrGcUJ-Q9t1GGPdp6yIEJFCqiz5edBMcmSPToXqSuxDYKkC_9taZ6uA7AVQS7reObMm_XiwSPM5S7p3geUWYVibofMF159BaxzsiM37vJMpH-ZzxGku34kukofmpD_ni9Qqcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6561" target="_blank">📅 17:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2226555990.mp4?token=djPM6oVf2xg4Or4qkg6pvhscuAP12cBr_Ex8hHm6OoJ8UvhwEdMYmvokw1WdJ08hpBD_9NXm4JdOwgKtwbTFMIaZF_40kSNo72VTF9AwHsqHicODnVZ70ERONL2Qn6G_kiIww2srMB4KW6_m98QMic5UEdjkuem6dCg-8-LomjE9UKD0UbqiyKnfjg8fpwRGE3KvtRSfBin-QBUziFnweye0BlAvA6jIcV6Bq3lIDD6_KNMOgQLUT3NZywDlv6xT5QOHyfookyFnphxZZwwX7A4Puf61bwGnzjHFJE8cJsIuuDNQRUKo9BR3KPoyYpHRg2acwzY9rSYJ1wdBX9-Y6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2226555990.mp4?token=djPM6oVf2xg4Or4qkg6pvhscuAP12cBr_Ex8hHm6OoJ8UvhwEdMYmvokw1WdJ08hpBD_9NXm4JdOwgKtwbTFMIaZF_40kSNo72VTF9AwHsqHicODnVZ70ERONL2Qn6G_kiIww2srMB4KW6_m98QMic5UEdjkuem6dCg-8-LomjE9UKD0UbqiyKnfjg8fpwRGE3KvtRSfBin-QBUziFnweye0BlAvA6jIcV6Bq3lIDD6_KNMOgQLUT3NZywDlv6xT5QOHyfookyFnphxZZwwX7A4Puf61bwGnzjHFJE8cJsIuuDNQRUKo9BR3KPoyYpHRg2acwzY9rSYJ1wdBX9-Y6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و تاریخ ثابت کرد حق با آرش و آرش‌ها بود!
فهم آرش از «شریعتی» و «آل احمد» و «هما ناطق» و «شاملو» و «غلامحسین ساعدی» و…. بسیار بالاتر بود.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6560" target="_blank">📅 11:22 · 23 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/QMG8LJBZNzAHxu-odr1Wh9vtowLgAVmEdLF5Std5b6KpTAqDYx0f3W4FvEK-XR6tpI4eXgkk0GeShH3JKmVwCVzeejE1r4IOzh4q9GHAHvXd3TgR8_RGU7gwyM4CBhjQmqDt614TMgEcHU_g9XW_2661nI1VHIPX55RUwDgegMhZ585-JRI-G2uqogmTD4VkQRx7SfonqBWPeZ2GYGhjolBEh4o3FHteHjyMPOp3yM_UINNYjbW1HiT6RXgzaB5prhVpY9NcDl3WH8f0CcCyeN1OgfZIamWriv2K5-8LYSDR166NozTmEuLBCEZz5mQFej_jxlQk--kDIj_FBv7PLA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 923K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 19:06:53</div>
<hr>

<div class="tg-post" id="msg-146516">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmAleP4XGJtkgAWwLEgDzkWQjPHPYYtxMG2UqPINYfNP7Bg1FmwGauZ1S_4tWUBrp-mLqzBiogZEHGfCDQ0kG9oL2IjG0_z2MjHLKlEACzTOJ75fVJyN4AHCpIW_NBuByzJAStLDlTMLbmsy5owutcEZatDFrfGwe05bUZ8rYQdozbMsm7ZnQ3kR2CoMKDaqmSrYetMvHYbGj0Q525IkTaunWplN63J_5QAT54GNz9wmyeQIIW0bg2eRuq9K8a_fuS_ZsuY_E6D1Flmzec0SipOCYVPmY2B-S4Fte72PYPHjeYvatsoEJKx7PbFsy6lntLCriT-Wxt283tCpuODwDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت 101 دلاری شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/alonews/146516" target="_blank">📅 19:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146515">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
تعدادی از ژنرال‌های پاکستانی در حال حاضر در ترکیه حضور دارند و احتمالاً جلسه‌ای در مورد تحولات یمن برگزار خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/146515" target="_blank">📅 18:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146514">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5n7wGoXRbtXQmqq-UDTSVOyQJHpTSxfRSlMj7KQ0jUm-7R3HMgva6L8LZkCCf6nz120MBb6v44z3rqcysGAqm4CyOrt-imDErP_dyxsJCNFZtwfLEtiKlIYTTN_tECYGbc4RiHeT6UoObNVgrBhCpHUYw2ageWzKCYznhLKFaAa6Xf5iYUiW5bm1M9Bz01d7PjiPZbNNS8FWscybadnME-0Watp5ViSqPqk-rhDhH8cxd2OguuQzZHJtUSzK9WLrH14M2CHwBMqQgXLUYUHjVB_zjW0ywuBzE2bh5HmUEyITIsruWkfTzH92cRtobzCXHC5G7c8DtuNQpTOouQkog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس گزارش می‌دهد که بسیاری از جمهوری‌خواهان و دستیاران کاخ سفید تا حد زیادی از تلاش برای مهار پرزیدنت ترامپ دست کشیده‌اند، حتی در حالی که به‌طور فزاینده‌ای از شهود سیاسی او تردید دارند.
«
چرا زحمت بکشیم
؟» یک مشاور بلندمدت گفت. «
رئیس اونه
.»
با نگرانی جمهوری‌خواهان درباره انتخابات میانه‌ها، دستیاران به‌طور فزاینده‌ای «
از خواسته‌های او پیروی می‌کنند».
یک اهداکننده این پویایی را این‌گونه خلاصه کرد: «
هرچه بخواهد، به دست می‌آورد
.»
با این حال، افراد درون‌کاره ایده‌ی کمرنگ شدن ترامپ را رد می‌کنند. یک مشاور با استدلال اینکه ترامپ حتی پس از پایان دوره ریاست‌جمهوری‌اش «شخصیت سیاسی غالب» باقی خواهد ماند، گفت: «کاهش ارزش ترامپ را به خطر بیفتید.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/146514" target="_blank">📅 18:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146513">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c6836a952.mp4?token=p2W41eDEwydQ8hqqFs6MPN9a2M_4mT_GQnZwfsxEe4TkaiampfNjtAv6dIR2TOlO8fLxw-1LR92erz6ge_-L4XIjpx3ArXb2HSKLL7KGzaq06N8JikZZqn28_ZsZwZ83Z_amyeEY5GvBPDKXZlkY9DdOVU3JIbTlhqaHLbMN6qNpBeljQsUBDwXT2wWvj8vvCF2AdGeeUc8VJFGlQhjGNiGZBX14q5r_a8BzIwK9G5hoN7WgSoLLDSytJ6geIzFtzJNarjXSdDHvrJ-KuLQR67f-b9LKB-jPeK4E0V4iwDTVF_BNwTQQHK-ztgKZhLYgtl17FKWb0D4IRxTXKSV0ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c6836a952.mp4?token=p2W41eDEwydQ8hqqFs6MPN9a2M_4mT_GQnZwfsxEe4TkaiampfNjtAv6dIR2TOlO8fLxw-1LR92erz6ge_-L4XIjpx3ArXb2HSKLL7KGzaq06N8JikZZqn28_ZsZwZ83Z_amyeEY5GvBPDKXZlkY9DdOVU3JIbTlhqaHLbMN6qNpBeljQsUBDwXT2wWvj8vvCF2AdGeeUc8VJFGlQhjGNiGZBX14q5r_a8BzIwK9G5hoN7WgSoLLDSytJ6geIzFtzJNarjXSdDHvrJ-KuLQR67f-b9LKB-jPeK4E0V4iwDTVF_BNwTQQHK-ztgKZhLYgtl17FKWb0D4IRxTXKSV0ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعاری که دیشب گروهی از حامیان حکومت‌ تو شب نشینی شبانه می‌دادن :
🔴
تو تاریکی می‌شینیم، ذلت نمی‌پذیریم.
🔴
بنزین رو کم میگیریم، ذلت نمی‌پذیریم.
🔴
دلاری گوشت میگیریم، ذلت نمی‌پذیریم.
🔴
مهریه کم میگیریم، ذلت نمی پذیریم.
🔴
پ.ن: این جماعت ۱درصدی رو باید صاف فرستاد یمن تا برای میلیون‌ها ایرانی نسخه نپیچن
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/alonews/146513" target="_blank">📅 18:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146512">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOlv4L2GpttlrVuajrdCdtd5s0S_dD85CzRI1nDrGIS6zdiBa6VJgUg9k4vegns7jVroEoXC1PhDnPJlm3G9bs_pjBvgA87fUEN6QMU4G5O_mqlrRT8zp_DpwAiHSX6bU0cxVrvhfmPlIcpa1cWXqqwIyO9BH7cGbJyWDwbPZvCkJZDdj37JIEs_82sCiRtBFxDDvJAO4itOoYhpNWl-7Hj0t-ZYP6nXvWKxjEaMS1_SpRjRXwzGzWE6MJWakEYplOLkavdVbzbPzAWm8FDymv8EyvEekJ8JYwggVhkyC-guntjZH3P68OidxyPozgVEslA0wNv7du_NimHNWsxvqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تانکر ترکرز :
آمریکا در این دور حملات شش نفتکش ملی ایران و ده نفتکش دیگر مرتبط را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/146512" target="_blank">📅 18:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146511">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IuxgwAq2loJ8nkC49wJNnpX8HO7aacRrjVviOB64jRfsX0mh8WXvTYWmc2qekz2VpBCwdi0eIAlWO8HhZRyjl3Kc-jE1mRD7VvSUCnB3ocqBhnq6LoAquTMRf0q4PjeE3x27j-651lmijdhsiszHnnGQyRfSuo1HwRDVUV75yR-YPay4d_JTpDFRRTUqYHEVDinmSAgLW-nazaY6e2ITaYhmj5tgWhaQ95RWrmlaESMwK06_Y1quonXk_d88S5mJ_TJWPDiuYNsVHbaYkGw5ZwMrmc-sPZOilOKMPfyJvM55Y0oNAJTQ45jGAA2-UV9XU8JqcMZlZT6CeG2WbCwimA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل در حرکتی ناگهانی اعلام کرد تونل های کوه علی الطاهر از کار افتاده‌اند و نیاز به انفجار آنها نیست و به پشت خط زرد عقب نشینی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/146511" target="_blank">📅 18:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146510">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">جالبه دیروزم ترامپ میگفت دیگه ایران اصلا نمیتونه با این وضع سلاح هسته ای داشته باشه  یعنی حالا توافق هسته ای هم نکردیم، نکردیم!
🆔
@AlirezaMehrabi_ir</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/146510" target="_blank">📅 17:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146509">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNQFD5XYw81kdJHM14lUwKo7DFZRxCKjeSqBkQgvFRePQbz8GDWzhANZPMVLFXhkBHErIaB15CUt8ynM9KVjmBfb6M-pNHvEa55deaTzvS5ioWgJ2V_MFdtD4Gj25h8ihwo6vu3xDWdx6vjHrLGSsubB1j3MeXEKZ3NYkqTF5q9f5Nf3eSXOzRCBA2iNBajnxgaw95pqupx1BqVcKJmdtAVwxyJ511UhvDA-bBMyrwqHYmfFE3kUVekILtddTYAZECJ2z1_WY6kdf2fbWqnMUVTr6ZzXIw_pHzmxvbQl-sI1VX8iPYokj3FC96fGZmT9D110_ovVmwAaPEFkO6quDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تعدادی از ژنرال‌های پاکستانی در حال حاضر در ترکیه حضور دارند و احتمالاً جلسه‌ای در مورد تحولات یمن برگزار خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/146509" target="_blank">📅 17:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146508">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
رویترز: در پی حمله به نفتکش «هرکولس استار» در نزدیکی دبی، یک نفر کشته و یک نفر دیگر مفقود شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/146508" target="_blank">📅 17:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146507">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
اعزام سوخت رسان های آمریکایی به عربستان!
🔴
طبق گزارش ها چندین هواپیمای سوخت رسان آمریکایی در حال ورود به پایگاه های آمریکا در عربستان سعودی می‌باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/146507" target="_blank">📅 17:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146506">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
روزنامه جروزالم پست:
اسرائیل در حال حاضر خودش رو برای یک حمله چندجانبه از سوی ایران در روزهای آینده، همزمان با سال نو یهودی که برگزار می‌شود، آماده می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/146506" target="_blank">📅 17:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146503">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mJEvji_jHPO4UT2Ik0cjc1XJMNuyQBXQDGKW9YynY0z_bJomsUnm9x21mnO2wzN4a1Ee6VdoMplBumVnUPaZt-Pu2D_3oIxKUwkwFsiJycrp-3f4d65z8WPsTOKSq12DYrrhm1_EQ0TCUSSsZe1NX3-FpMZn0ZLtmCwz4IAEAnUGD65kD0Tz6nkbCfIzVcsQ6LWN7fUupoa-MeEZeLGSz-a79iycpgHdHgwzcPsffaQFEiL5253rcYSS-780vI-JfhD20v3bybVgV_uA5-EZ5L4oZCQQhJSq66u7tyeM0ImlgljTJdYBe-ROxIWwzvGwwgrKTLigjzSnOZ-zdF7vag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mBSvzj7czB-c7Lm03Mp7yaJTxqKbjYLY9G1M-eBpXTawykELZjt09C9t_KxpovuJoKkE4bSO3_aa6HjZ8zc2OHNmNmYNXj3IgJM0qo-foSr4yEuulgAweBvUeqOkC-8f7QBtL8QXkgWNZ71mRf1HStuSycrEKeHYtESZ8udMl2nev3fywy_wW3wFwUZ_8SWFGlyRnexwOBKB1HCLfB_ej9cOsp-WizWt0JJzoialaQ9hQ6Nz-u3MYfb3VKpaM85VP1BuqdNig8Vq9CXepNqOTf7i4_kPzqUCPJkxWm0tySTQ8mGPIE-NAMYKennNFeNxFY7_ur6d3ev2Kkm-MhDBFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qLTeNoMLgxQdTVQ-RH9E2BQ7C5KaBZg-I2aDancUcgMfARkHcIDYqELpA_RPMzcQfgWarvi_o0psT8RiA-_UHAlZ8oC58zV6qop-Cdt9UgvScRyfuUqvbzZlUWk7SOyGOEnbA1hE4nEvUNJh9MSk_aBV6h00BOSHETJ1cCrALRKyxkjcgx0nxrvLhXxWTMAQLOqRhXVWlzBfnyZb2zE7gp6bZleRT6E1spbBrmtr7MG4aBb6EeDsHrYL4RbMvhoNSMxS0Udg8Ie3XTSneiIu-isGkr9T7Xpj_Q25P6CkoFnoSPrLfL9jUGzI_tmZVno29AOLYWfMD8YR3M_S3-kYkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
نتانیاهو و کاتز، وزیر دفاع، از قله کوه هرمون در سوریه بازدید کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/146503" target="_blank">📅 17:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146502">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/guQAvN8Nxy-p9wfUJTkYaLfPPaLPJfrdre84NCwc9dNcELGhRhkSiTqflcEXKujvQo7pRLg_nsoiGGjjxsc9VDSLSOk9bWhdqw9LKBvnHb_EOPFwkExOnWIehjwDwOabI8WfuwISLB2ZpzjHjJMq7ieZ_CeeB6GK_9Se5Upl3LFDCpCvR_tqkLBQ1uN6EeK5NJb1zR4KF9d4-v6zi9niRlHk8KYXlKDiAap_CP2KQ0SvsmSXuJ6U7SDAN0ON0jAH1jrhHF5zHO4rVXAfF7p6NGqfcH7RHnGQ7A4mapM9ZwViGAXATq49E6IzqW8BDH6rJ22N6cL8_5mevjfTdc4-iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قبل از رونمایی رسمی، مشخصات آیفون ۱۸ لو رفت!
نکته قابل توجه اینه که رسما از آیفون فولد(تاشو) رونمایی شد.
آیفون ۱۸ پرو توی چهار رنگ گیلاسی، خاکستری، سفید و مشکی معرفی میشه.
قیمت پایه آیفون ۱۸ پرو: ۱۱۹۹ دلار(۲۸۰ میلیون)
قیمت پایه آیفون ۱۸ پرومکس: ۱۲۹۹ دلار
(۳۰۵ میلیون)
این قیمتا بدون گمرک و... هست، وقتی وارد ایران باشه حداقل ۳ـ۴ برابر این قیمتا خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/146502" target="_blank">📅 17:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146501">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
مجتبی یوسفی، نماینده مجلس: خودروی چینی بی‌کیفیت رو دو برابر قیمت به مردم فروختیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/146501" target="_blank">📅 17:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146500">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
دلار بزودی 300هزار میشه
⁉️
🔴
تحلیل ترسناک نوستراداموس ایرانی
👇
🔴
https://t.me/AlirezaMehrabi_ir
🔴
https://t.me/AlirezaMehrabi_ir</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/146500" target="_blank">📅 16:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146499">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ارم نیوز: آمریکا در حال بررسی حضور تفنگداران دریایی خود در برخی جزایر خالی از سکنه ایران در اطراف تنگه هرمز است
🔴
در صورت اجرای این طرح، جنگنده‌های اف‌ـ۳۵بی مستقر در ناو تریپولی وظیفه پشتیبانی هوایی از تفنگداران را بر عهده خواهند داشت.
🔴
هدف این طرح، ایجاد نقاط دیده‌بانی و پایگاه‌های لجستیکی برای نظارت بر تنگه و حفاظت از کشتی‌های تجاری عنوان شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/146499" target="_blank">📅 16:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146498">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
شرکت نفت کویت، این امکان را به خریداران ارائه می‌دهد که انتقال بار از یک کشتی به کشتی دیگر در خارج از تنگه هرمز انجام شود تا حمل و نقل ایمن‌تری به مقاصد نهایی تضمین گردد.
🔴
این شرکت اعلام کرده است که برخی از کشتی‌ها همچنان در شرایطی که ایمن است، از طریق این تنگه عبور می‌کنند، در حالی که انتقال بار از یک کشتی به کشتی دیگر به عنوان یک گزینه جایگزین ارائه می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/146498" target="_blank">📅 16:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146497">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
اوکراین در حال عقد قرارداد برای دریافت حدود هزار موشک رهگیر پاتریوت با تأمین مالی اتحادیه اروپا است.
🔴
با این حال، تحویل این موشک‌ها در کوتاه‌مدت انجام نخواهد شد و کی‌یف به همین دلیل از کشورهای غربی خواسته بخشی از ذخایر فعلی خود را فوراً در اختیار اوکراین قرار دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/146497" target="_blank">📅 16:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146496">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
روزنامه جروزالم پست: اسرائیل در حال حاضر خود را برای یک حمله چندجانبه از سوی ایران در روزهای آینده، همزمان با سال نو یهودی که برگزار می‌شود، آماده می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/146496" target="_blank">📅 16:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146495">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
وزیر امور خارجه اسرائیل، گیدئون ساعار: اسرائیل تنها کشور دموکراتیک در خاورمیانه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/146495" target="_blank">📅 16:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146494">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6573f5e81.mp4?token=iUbLPRi_i7QaiNlZFhZLN_hY8gArBpx9U_u5GIJm6tALPHHZhndXSSt63dgXrPHOScMiPBS_9iq_5sXrlC6bwCmZspgNBgq7MxKYoNIbXvP7CT2n-hFPRU-xGPLV7XJxP86pPcNZKPQAfJIIl6q9eeCY5BkpPa3Lz1t6TnWDzAu-4JxaG6LLptruuKVf5zY-DaIt3PuwWcWbvqXti17AfSWPzyykd2L9KaQcjct7w6TCzAJD4e1DCThPMmqBxJXsE_uSP1A7YdoaKmf_5uiHhZTarPIXk3jHizW79N4VPTEWY1phkDOvlMM-vtdQrU8vx4qNj8urFwm8Cc3dCYMwfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6573f5e81.mp4?token=iUbLPRi_i7QaiNlZFhZLN_hY8gArBpx9U_u5GIJm6tALPHHZhndXSSt63dgXrPHOScMiPBS_9iq_5sXrlC6bwCmZspgNBgq7MxKYoNIbXvP7CT2n-hFPRU-xGPLV7XJxP86pPcNZKPQAfJIIl6q9eeCY5BkpPa3Lz1t6TnWDzAu-4JxaG6LLptruuKVf5zY-DaIt3PuwWcWbvqXti17AfSWPzyykd2L9KaQcjct7w6TCzAJD4e1DCThPMmqBxJXsE_uSP1A7YdoaKmf_5uiHhZTarPIXk3jHizW79N4VPTEWY1phkDOvlMM-vtdQrU8vx4qNj8urFwm8Cc3dCYMwfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای ائتلاف جنوب، نزدیک به امارات، سعی کردند طاهر العقیلی وزیر دفاع یمن را که مورد حمایت عربستان است، گروگان بگیرند
🔴
این دو نیرو علیه انصارالله یمن با همدیگر متحد شده بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/146494" target="_blank">📅 16:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146493">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zt6FRjLKujET_MT5KsYq8M9e6Nz-QMA929WHtD7tZRw-y9XLNxMZIH9MwUH7uj-G2Z-sfqtUv0sIjHRodyK3eVdnIuFDbl1gaaOvx6GQx05UBP4Hh8Mx2EYgCbraQq0VytNGecTRYW5mIqjptWk_kslrARbv5h3sVxUlGdH_llBWQITZodlQeVHyaGjVR-waaGlDLF1KdBt9LxbwpwCrjdDZhx9m6jB4M3jiqidTNrgWL_nCS5KRWfVywR92OoVSdrhSuqGp9IrV6_lZhNuue6DW_TriH9h7IUVYYUs9Ypy_JYFyE6x2IzXBpGvIkeBrYRIpQ10Q6BBNru8DrZQq9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه ایران، چاپ شهریور ۱۳۸۲
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/146493" target="_blank">📅 16:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146492">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
شعار در شب نشینی‌های شبانه
دلار بشه یه میلیون
تسلیم نمیشه ایرون
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/146492" target="_blank">📅 16:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146491">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
رویترز: در پی حمله به یک تانکر حامل محصولات نفتی به نام "هرکولِس استار" در نزدیکی دبی، یک نفر کشته و یک نفر مفقود شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/146491" target="_blank">📅 16:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146490">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fc965eb9f.mp4?token=Lf1mz2OjvZcrOcqNWjxTtL2RAedj5i9v7z2cQYmZbFlw_auHW3XC6xP05GQZhm20LC2kqn7oDqIyHfJV_6DOs5NWcY_3P0y-lNarZnLLUUAp-_fjvBGwn33fra4Da0LWUnSVzenO6LJeRw1R-lnZBFG3WYThe5K8P44Y74P3O_HN8PB-F4I4eU42esIOQD8uFpvXiHnR7VtiQJolqzR8MmMO1HsKNJxAzvpoWaXH7rsjSJNMKF9tieqtkZxeolo8U51jodgdcZAJAUOYlr-BnKrbBPzwLGDqH1Uub3wxp-ieeYXrgt-BQDF4VW22eUDpmP3DdYqXeuFDJT9p9GYi_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fc965eb9f.mp4?token=Lf1mz2OjvZcrOcqNWjxTtL2RAedj5i9v7z2cQYmZbFlw_auHW3XC6xP05GQZhm20LC2kqn7oDqIyHfJV_6DOs5NWcY_3P0y-lNarZnLLUUAp-_fjvBGwn33fra4Da0LWUnSVzenO6LJeRw1R-lnZBFG3WYThe5K8P44Y74P3O_HN8PB-F4I4eU42esIOQD8uFpvXiHnR7VtiQJolqzR8MmMO1HsKNJxAzvpoWaXH7rsjSJNMKF9tieqtkZxeolo8U51jodgdcZAJAUOYlr-BnKrbBPzwLGDqH1Uub3wxp-ieeYXrgt-BQDF4VW22eUDpmP3DdYqXeuFDJT9p9GYi_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز، چندین حمله هوایی عربستان سعودی، مواضع حوثی‌ها (انصارالله) را در جبهه مریب در یمن هدف قرار داد، این اقدام به منظور حمایت از عملیات شورای انتقالی جنوب (PLC) انجام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/146490" target="_blank">📅 16:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146489">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">تتر توی برخی صرافی های ایرانی تا ۲۴۰ هزار تومن هم معامله شد
🆔
@AlirezaMehrabi_ir</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/146489" target="_blank">📅 16:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146488">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
الجزیره به نقل از یک منبع عراقی: هدف قرار دادن نفتکش در آب‌های سرزمینی عراق، در نزدیکی بندر العمیه در بصره، رخ داده است.
🔴
نفتکش هدف قرارگرفته حامل ۲ میلیون بشکه نفت عراق بوده و در منطقه بارگیری قرار داشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/146488" target="_blank">📅 15:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146487">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
حوثی‌ها (انصارالله) اعلام کردند که یک جنگنده سعودی از نوع F-15SA در تاریخ 7 سپتامبر، دو بار به زندان مرکزی در شهر ال‌حزم، واقع در استان الجوف، حمله کرد و در نتیجه، تعداد زیادی از زندانیان و بازدیدکنندگان، از جمله زنان و کودکان، کشته شدند.
🔴
آنها گفتند که این هواپیما ساعت 16:30 از پایگاه هوایی خالد در خمیس مشیت برخاست، حملات را انجام داد و ساعت 16:45 به پایگاه بازگشت.
🔴
این گروه هشدار داد که عربستان سعودی به دلیل این حمله مرگبار، با عواقب روبرو خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/146487" target="_blank">📅 15:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146486">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏
👈
سی‌ان‌ان به نقل از منابع آگاه: تلاش‌های آمریکا برای تدوین برنامه‌هایی برای حملات قاطع علیه تأسیسات هسته‌ای زیرزمینی ایران ادامه دارد.
🔴
‏این تأسیسات زیرزمینی احتمالاً به عنوان پناهگاهی امن برای برنامه هسته‌ای ایران طراحی شده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/146486" target="_blank">📅 15:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146485">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره
آیدیش:
@khabar</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146485" target="_blank">📅 15:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146484">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9810b14509.mp4?token=so6uyqdrsaNwFaJIGvZVL2fBYPgf53UtF5M85yu229M69zunkTFdd8BtrcKlsQ6jlWoiocO_ZKnp6AUzhPDKqAAiU_YHeRC-Xdnpfz_KNAxzXhUefdnXNCbHsPg1UWHWDrusjMH8KriMDltlrNIVrYN1gQXkEbzjgzjXd6eku1ZnLtSwZ7m1IMk6SLRso-f0FJVc8gMbk25G9PW9b6KXKn9S177qyI_IlEaUcoj9MJBg_1vb9FKeoH242SOfKEKA6HA8FC7sfSaoTbHDNxPzi_BFa6-DKvCrCVinAtZKCpTIg7Z2CAYZd7g_okpicTPwQkxoVaXHVUDmaz1dFSugAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9810b14509.mp4?token=so6uyqdrsaNwFaJIGvZVL2fBYPgf53UtF5M85yu229M69zunkTFdd8BtrcKlsQ6jlWoiocO_ZKnp6AUzhPDKqAAiU_YHeRC-Xdnpfz_KNAxzXhUefdnXNCbHsPg1UWHWDrusjMH8KriMDltlrNIVrYN1gQXkEbzjgzjXd6eku1ZnLtSwZ7m1IMk6SLRso-f0FJVc8gMbk25G9PW9b6KXKn9S177qyI_IlEaUcoj9MJBg_1vb9FKeoH242SOfKEKA6HA8FC7sfSaoTbHDNxPzi_BFa6-DKvCrCVinAtZKCpTIg7Z2CAYZd7g_okpicTPwQkxoVaXHVUDmaz1dFSugAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیشروی ارتش ملی یمن علیه مواضع حوثی‌ها با پشتیبانی هوایی عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/146484" target="_blank">📅 15:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146483">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
نیکزاد، نایب رئیس مجلس: با عمان درباره تنگه هرمز به توافق رسیده‌ایم
🔴
نماینده مجلس:  بخش قابل توجهی از تنگه در مسیر ورودی و خروجی در اختیار ایران است؛ حتی پادشاه عمان این را پذیرفته
🔴
زلف تفاهم‌نامه اسلام‌آباد به تنگه هرمز بسته شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146483" target="_blank">📅 15:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146482">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از منابع آگاه: تلاش‌های آمریکا برای تدوین برنامه‌هایی برای حملات قاطع علیه تأسیسات هسته‌ای زیرزمینی ایران ادامه دارد.
🔴
این تأسیسات زیرزمینی احتمالاً به عنوان پناهگاهی امن برای برنامه هسته‌ای ایران طراحی شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146482" target="_blank">📅 15:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146481">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
گزارش بلومبرگ، تشدید تنش‌ها بر سر کنترل تنگه هرمز باعث شد قیمت نفت برنت به بیش از ۱۰۰ دلار در هر بشکه برسد.
🔴
نگرانی‌ها درباره امنیت عبور نفتکش‌ها و اختلال احتمالی در جریان صادرات انرژی از خلیج فارس، فشار صعودی بر بازار نفت را افزایش داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/146481" target="_blank">📅 15:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146480">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
شروط جدید ایران برای توقف جنگ اعلام شد
🔴
سخنگوی سپاه: اگر دشمن خواهان پایان این وضعیت است، باید:
۱- ضمن توقف کامل جنگ،
۲- از تهدید مجدد دست بکشد،
۳- ارتش رژیم صهیونیستی از لبنان عقب‌نشینی کند،
۴- محاصرهٔ یمن پایان یابد،
۵- ۲۴ میلیارد دلار دارایی مسدودشدهٔ ایران آزاد شود
۶- و از هرگونه مداخله در توان هسته‌ای و موشکی کشور دست بردارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/146480" target="_blank">📅 14:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146479">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
سخنگوی سپاه: دشمن ۲ هدف از ما بزند، به ۲۰ هدف حمله می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/146479" target="_blank">📅 14:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146478">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">یعنی هر لحظه ممکنه پای پاکستان و‌ ترکیه هم به جنگ باز بشه
🆔
@AlirezaMehrabi_ir</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/146478" target="_blank">📅 14:46 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146477">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
پزشکیان: قدردانی از همراهی مردم در اجرای طرح بنزین
🔴
طرح «یک روز در هفته بدون خودرو» از سوی دستگاه‌های دولتی اجرایی شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/146477" target="_blank">📅 14:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146476">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
گزارش ها از صدای چند انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/146476" target="_blank">📅 14:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146475">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
سی‌ان‌ان: تحلیل تصاویر ماهواره‌ای شبکه CNN نشان می‌دهد که ساخت‌وساز در سایت هسته‌ای «کوه کلنگ» (Pickaxe Mountain) در نزدیکی نطنز، که در عمق زمین قرار دارد، افزایش چشمگیری داشته.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/146475" target="_blank">📅 14:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146474">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
رئیس‌جمهور لبنان: ما مذاکره با اسرائیل را به خاطر منافع لبنان و نه برای خشنود کردن هیچ کس در خارج از کشور انتخاب کردیم
🔴
درخواست من برای پایان دادن به خصومت‌ها با اسرائیل به معنای پایان دادن به جنگ‌هایی است که قابل تحمل نیستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/146474" target="_blank">📅 14:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146473">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
مدیرعامل فرودگاه بین المللی تهران: هیچ یک از پروازهای خارجی لغو نشده است/ هیچ کشوری مکاتبه‌ای برای اعمال محدودیت‌ها نداشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/146473" target="_blank">📅 14:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146472">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
سخنگوی سپاه: هر کشتی که از منطقهٔ ممنوعهٔ تنگهٔ هرمز عبور کند تحریم می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/146472" target="_blank">📅 14:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146471">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
سنتکام: هیچ ناو آمریکایی هدف قرار نگرفت؛ ۱۰ تانکر ایرانی را نابود کردیم
🔴
فرماندهی مرکزی آمریکا مدعی شده هیچ‌یک از ناوهای جنگی این کشور مورد اصابت قرار نگرفته و تلاش‌های سپاه برای حمله به آنها ناموفق بوده است.
🔴
سنتکام همچنین ادعا کرده نیروهای آمریکایی طی هفته گذشته ۱۰ تانکر ایرانی را نابود کرده‌اند.
🔴
به گفته این فرماندهی، این تانکرها بخشی از یک «شبکه پنهان» چندمیلیارددلاری بوده‌اند که برای تأمین مالی سپاه پاسداران فعالیت می‌کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/146471" target="_blank">📅 14:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146470">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVQmIs4HRm92dcs2N7HEgNrIPVQaXbC6Q6iN9ir73gIuGx4wyK4mH-XClZNOhXxmR6y1F8xKE2E_OS6nF1XYA_SSTZTQ4GevC5qbtwP2i9toxgUbFqYS-bpyU_9tyy-mbiZuLmHjMrqd2MTCYDsylhG1ClyOa6DYbd8foLpn6Feq9I6r8hCcBAabnKgcpm-QMlk4fAYHLN0F0LKIq6PwQ_2Qr2rvx3AiW4YU3Ah0W6e4Nh0RNFuhYdLjfSNg2cuvuBoDBBcsy9ZeQEJgCaK0ZCF7kUHctuWfGJrMBJUAH2AOxCIKVp03ZSBR08TaNEDTjwVaT_rbAhzCIJ5bvLhaSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: یک کشتی با پرچم پاناما در آب‌های سرزمینی عراق توسط یک پهپاد هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/146470" target="_blank">📅 14:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146469">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
الجزیره از متن پیش‌نویس قطعنامه آمریکا و اروپا
:
در پیش‌نویس قطعنامه‌ای مشترک از سوی آمریکا و کشورهای اروپایی که الجزیره به آن دست یافته است، تأکید شده که ایران همچنان به تعهدات خود در ارتباط با پرونده هسته‌ای‌اش پایبند نیست و از این وضعیت «عمیقاً ابراز نگرانی» شده است.
🔴
در این پیش‌نویس تأکید شده است که نبود اطلاعات درباره مواد هسته‌ای و اجازه ندادن به دسترسی به تأسیسات ایران، دو مسئله‌ای هستند که نیازمند رسیدگی فوری‌اند.
🔴
این متن بار دیگر از تهران می‌خواهد عدم پایبندی خود به توافق پادمان‌ها را در سریع‌ترین زمان ممکن برطرف کند.
🔴
این پیش‌نویس از ایران می‌خواهد به‌صورت جدی و بدون پیش‌شرط وارد مذاکراتی شود که هدف آن ایجاد اعتماد در جامعه بین‌المللی است و بر حمایت از دستیابی به یک راه‌حل دیپلماتیک برای چالش‌های ناشی از برنامه هسته‌ای ایران تأکید می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/146469" target="_blank">📅 14:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146467">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
وزیر دفاع پاکستان: حملات حوثی‌ها علیه عربستان سعودی ممکن است منجر به فعال شدن پیمان دفاع مشترک شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/146467" target="_blank">📅 14:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146466">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
وزیر دفاع پاکستان: تلاش‌های میانجی‌گری میان ایران و آمریکا ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/146466" target="_blank">📅 14:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146465">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
آکسیوس: تصمیم کاخ سفید برای مخالفت نکردن با تلاش بریتانیا در مورد تحریم شهرک‌نشینان اسرائیلی، نشانه‌ای از نارضایتی واشنگتن از سیاست‌های دولت نتانیاهو در کرانه باختری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/146465" target="_blank">📅 13:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146464">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
دلار به 232,000 تومان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/146464" target="_blank">📅 13:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146463">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28a9989cd.mp4?token=ObRyfDMe0BprhD6EbLLgPBrDvvuRFO_FjABeqLkAilinlaW6ZmYJapbbA49D-XwzP1yg_VX3VgFFJJtRc6q2V552oDbtr4Il-tb-2MSW0zVi1bxb3XtRjSvt9fLh9Pttdfc3mOiud-BJy1gvLsC8u_Gx329ZNsw4lhMxRr7AhpESpU3ao_L7i9EVhxe0h9LlAqZ13DjijgzbIvKbdP1mLpPcTsUr1mU3H1mmOx6NQnPy0e69MxBltJnQXar14RaU8FoovM_f-AZmWCa4X4vAiYo4_a7odPm5F_o_R-Nc4yjul1tA0X8NxfIKKd7zKnWmqOm25qcJz-_6v2qsumEFtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28a9989cd.mp4?token=ObRyfDMe0BprhD6EbLLgPBrDvvuRFO_FjABeqLkAilinlaW6ZmYJapbbA49D-XwzP1yg_VX3VgFFJJtRc6q2V552oDbtr4Il-tb-2MSW0zVi1bxb3XtRjSvt9fLh9Pttdfc3mOiud-BJy1gvLsC8u_Gx329ZNsw4lhMxRr7AhpESpU3ao_L7i9EVhxe0h9LlAqZ13DjijgzbIvKbdP1mLpPcTsUr1mU3H1mmOx6NQnPy0e69MxBltJnQXar14RaU8FoovM_f-AZmWCa4X4vAiYo4_a7odPm5F_o_R-Nc4yjul1tA0X8NxfIKKd7zKnWmqOm25qcJz-_6v2qsumEFtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شرکت پخش فرآورده‌های نفتی
:
موفق شدیم رقم ۱۰ هزارتومان را در پمپ بنزین‌ها نشان دهیم و برچسب‌های صفر ثابت را برداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/146463" target="_blank">📅 13:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146462">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
وزارت امور خارجه قطر: ما حملات مجدد ایران به اردن را محکوم می‌کنیم و آن را نقض حاکمیت ملی و نقض قوانین بین‌المللی می‌دانیم.
🔴
ادامه حملات ایران، تشدید تنش‌ها را تشدید می‌کند و تلاش‌ها برای مهار تنش‌ها را پیچیده‌تر کرده و تلاش‌های دیپلماتیک را تضعیف می‌کند.
🔴
ما بر لزوم پرهیز از هرگونه اقدامی که تنش‌ها را تشدید می‌کند، تأکید داریم و خواستار بازگشت جدی به روند مذاکرات و پایبندی به دستاوردهای حاصل شده هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/146462" target="_blank">📅 13:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146461">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
رئیس اتاق اصناف: گرانی کالاها صرفا به دلیل قیمت تمام شده تولید خود آن‌ها است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/146461" target="_blank">📅 13:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146460">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
عوستاد خوش‌چشم تحلیلگر صداسیما:
تو پاییز یه جنگ شدید، اما کوتاه داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/146460" target="_blank">📅 13:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146459">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L13zpol1xRj67vcbjyYMyjfhgiwZLNzKCyeuCs_wLxKb0bExcWdfxxEaiezkyh6ZROk8Nf1KVPYGEMGUeaiqaBcOT-SXEK2qH0zlTVrI4uZWt5NH6uvy9oWaWz6uwAGs9tF0lMkm-T41UY6cCAjC6Un6NYZ7TavnoEHESyaFvuE3kRM2wdzZ631kGxaknEonCHmVJe_7qaE-Y08EXhivfHlL5eMdgZ2-BMPiQ2O-HrfSn4Y2DPNPum5KjubR_lctXeYhA8xWbwXpNrgpKvWrxs_fOd33dP-HYJoibl2FI3EfJ2tvh0BOYjDoaoXw5xijtMN3UWwA82ew-hsX3GISfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک کشتی در شمال غربی بندر رشید در امارات متحده عربی مورد هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/146459" target="_blank">📅 13:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146458">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
یک مقام آمریکایی در گفت و گو با الجزیره : موشک‌هایی که ایران به سمت اردن شلیک کرد، هیچ تلفاتی در میان نیروهای آمریکایی برجای نگذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/146458" target="_blank">📅 12:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146457">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دلار و طلا منفجر شد
‼️
این پسره یه تحلیل عجیب گفته
😐
👇
https://t.me/AlirezaMehrabi_ir
https://t.me/AlirezaMehrabi_ir</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/146457" target="_blank">📅 12:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146456">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
شعار دیشب در تجمعات : اصلا دلار بشه ۱ میلیون، نمیریم از خیابون
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/146456" target="_blank">📅 12:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146455">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5eec3b402.mp4?token=Nyi4zQ9dM8-wXJarM5VtPvyZJdkyo9cuYuaGNig6RS1uWDA4ZevM1_--6E9Mrds-_f1AeMmeHsIfZMOGbwahmluxK9vjrv41xRLJGD1vsLd9tCG7_Yqzt_Oxcp0tIxET5xRdHWtxwNV3NxOHkHzzwHyZR07DLg_zPuyeq7nNPlPkzULwygysJcb4O9PQf6Jj0H6UkqTM3b19N0ZsKwWdY3AezgcKI7_z0Il5EL_0AriNVf0NzAPsLVgB6zhXjl_MxvsyDEBZwE_O1ggay9xgCidHuWWsxWLFDFAi-hoz-Rz10msD4jyGTwWDydwPvzf30GxUv9cuvmLumw6It0HxEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5eec3b402.mp4?token=Nyi4zQ9dM8-wXJarM5VtPvyZJdkyo9cuYuaGNig6RS1uWDA4ZevM1_--6E9Mrds-_f1AeMmeHsIfZMOGbwahmluxK9vjrv41xRLJGD1vsLd9tCG7_Yqzt_Oxcp0tIxET5xRdHWtxwNV3NxOHkHzzwHyZR07DLg_zPuyeq7nNPlPkzULwygysJcb4O9PQf6Jj0H6UkqTM3b19N0ZsKwWdY3AezgcKI7_z0Il5EL_0AriNVf0NzAPsLVgB6zhXjl_MxvsyDEBZwE_O1ggay9xgCidHuWWsxWLFDFAi-hoz-Rz10msD4jyGTwWDydwPvzf30GxUv9cuvmLumw6It0HxEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یادتونه ابوطالب گفته بود: «دلتون برای دلار 78 هزار تومنی تنگ میشه»؟
🔴
امروز دلار به 3 برابر 78 هزار تومان رسید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/146455" target="_blank">📅 12:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146454">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1602dc700b.mp4?token=hoyS9cKV_EdhhC0il0EH9CbsFqZMDw7uP3jEc2CnNlMIn11tz4r52I7s46O1uuAML3xlozZSEWIDoLxLDdOlgL4DP3MvvveR8cEZUARqltdaCLJP4NlP9iQLLc6W94NDvaqT-rMN_6XtCC7RkaaM-GwyOrsxa3_XX_bonjkstGfkNSIh70ump5xkco5yX2Jjp7Un9ZA8K8nhHvqb0ggUUwIWLMg0lAimzCOiyibBERXXEuRiU4F2m6r1omOXvlO31iPxDc-u0UiHqw2hZpzE0AjF3D2U22msfSxM9-r41PZ2qW33qPot-xuHaKbM_AirWqAj04UzrdzKS6tYnJr4vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1602dc700b.mp4?token=hoyS9cKV_EdhhC0il0EH9CbsFqZMDw7uP3jEc2CnNlMIn11tz4r52I7s46O1uuAML3xlozZSEWIDoLxLDdOlgL4DP3MvvveR8cEZUARqltdaCLJP4NlP9iQLLc6W94NDvaqT-rMN_6XtCC7RkaaM-GwyOrsxa3_XX_bonjkstGfkNSIh70ump5xkco5yX2Jjp7Un9ZA8K8nhHvqb0ggUUwIWLMg0lAimzCOiyibBERXXEuRiU4F2m6r1omOXvlO31iPxDc-u0UiHqw2hZpzE0AjF3D2U22msfSxM9-r41PZ2qW33qPot-xuHaKbM_AirWqAj04UzrdzKS6tYnJr4vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از انفجار در شمال ادلب سوریه
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/146454" target="_blank">📅 12:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146453">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
رسانه های سوری گزارش دادند انفجاری با منبع نامشخص در شهر سرمدا واقع در شمال ادلب به وقوع پیوست
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/146453" target="_blank">📅 12:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146452">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
فوری / سازمان دریایی بریتانیا: چندین کشتی در شمال خلیج فارس و دریای عمان، در پی هدف قرار گرفتن با آتش، دچار اختلال و توقف فعالیت شده‌اند
🔴
هیچ تأییدی درباره وقوع تلفات جانی یا خسارت زیست‌محیطی در پی هدف قرار گرفتن کشتی‌ها در خلیج فارس وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/146452" target="_blank">📅 12:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146451">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
فوری/گزارش ها از حمله پهپادی ایران به یک نفتکش در سواحل دبی، امارات.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/146451" target="_blank">📅 12:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146450">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
کامران غضنفری، نماینده مجلس:
در آستانه جنگ جهانی سوم هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/146450" target="_blank">📅 12:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146449">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IR5MGrsEBSncB1W8-ExV_mfJx5hHWIG9l7rfOdZ7x9Cpn5kdRy-4GgdSuL28gy3wJJi8H6IHQ4RTDO84Sln06ognmUOZ5OhrV1c0NkIHLR9L720hcoO2Ivdg6-PeWRZ6CaUyhKP709Po61yTLUaJ_IbBiFwRyAa3Qdr228JotrMg87I0swY_8vu9nSKmCdUUKrKQguOnpQz8hckOH7QZb8boFM0spvfrnZ9nY7XvQIdDbBZT48WTZQozvd71Mdah1iIMsyO2_kcD-_ceatQ8L2Yp05HWq9S4lMORaQDbpLcLZTGOgOfOQ6cX9MEZTjkWqczqeGHNN_Mvbe-uWKFBqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایوان هوبینگر، مسئول بخش همسویی در شرکت آنتروپیک، می‌گوید که "احتمال بیش از ۱۰ درصد" وجود دارد که هوش مصنوعی در ده سال آینده "تمام انسان‌ها را نابود کند"
🔴
هوبینگر گفت که شرکت آنتروپیک "تمام تلاش خود را می‌کند"، اما اذعان کرد که این شرکت هنوز برنامه‌ای برای حل مشکل همسویی هوش مصنوعی فوق‌العاده ندارد و "هنوز به وضوح در مسیر" دستیابی به این هدف نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/146449" target="_blank">📅 12:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146448">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=BU0BQbOD_53CL6sS0mbN0gRjMHdqNrqyLIa-dQ3KsZHrm9Mju1lOo9CYu8k3ED-2au2MOagjme9PGocvp6rzvSThstxCp2BfX4V95Y96spWFQpw6bBe5TpKHv-b9l_bfdsFSmEHH-BSQ0JahKmgDDIizLpTCpDM9HF9UwtYHnQfK8CEFqdgFlt_bbGRcbpMJLhlbcROr41Emi71mMWsfVp31gE6DoBMfzCsubABjMQ-YUSmh0SqMcRBlXZK-WGzxk4qWjR2lcenqNgnNZ82bbNhSzHsGDOqVIbGO63Wx28h-J-AvDKM4BLzfmZah2sSzjR72iam4zARv66xxBEqLng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=BU0BQbOD_53CL6sS0mbN0gRjMHdqNrqyLIa-dQ3KsZHrm9Mju1lOo9CYu8k3ED-2au2MOagjme9PGocvp6rzvSThstxCp2BfX4V95Y96spWFQpw6bBe5TpKHv-b9l_bfdsFSmEHH-BSQ0JahKmgDDIizLpTCpDM9HF9UwtYHnQfK8CEFqdgFlt_bbGRcbpMJLhlbcROr41Emi71mMWsfVp31gE6DoBMfzCsubABjMQ-YUSmh0SqMcRBlXZK-WGzxk4qWjR2lcenqNgnNZ82bbNhSzHsGDOqVIbGO63Wx28h-J-AvDKM4BLzfmZah2sSzjR72iam4zARv66xxBEqLng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دلار 230هزار تومان
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/146448" target="_blank">📅 12:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146447">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrrAsXCA5ivW3U7Xp6-A936CEWTn3t1XGPUoY_HYs8yBSebwO75E9eJkcfgn07ObBOD15xVFTpaDsuweLBfVuVQZ7jK2XBgSDV0vL83arisqQhEyrgO9ab8lLG7z9BJHgGvKjXBGeZ7iodUZhYj91odmbii7SX5F3VEH7dLITM-UfbK_6f2enM6b8ipAvKsWtSBuxwjEyuPqLR1lh1O0uwZ0EGRAIdb5jVR8QCmw_88qNpp_n9ONeuRX7CA9RT5nx6BGC7riCYzhpWAgBDadIJ3kjkjRhbbs22Dw9XSY1W4pkafxV4XDMqZym1n4HOpIQsHihS8vVcicNaS5Ccy7gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیماهای تانکر سعودی از پایگاه هوایی فهد در طائف به سمت یمن پرواز می‌کنند تا به جنگنده‌هایی که یمن را بمباران می‌کنند، سوخت‌رسانی کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/146447" target="_blank">📅 11:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146446">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
طبق اعلام خبرگزاری ریانووستی، بر اساس داده‌های وزارت جنگ آمریکا، شمار مجروحان این کشور از ابتدای جنگ با ایران به ۸۲۰ نفر افزایش یافته و شمار کشته‌شدگان نیز بدون تغییر، ۱۸ نفر اعلام شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/146446" target="_blank">📅 11:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146445">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دیروز بهتون گفتم ارزش ذاتی طلا 24 میلیونه
‼️
الان با این قیمت‌ها هنوز تقریبا 300 تومن زیر ارزش ذاتیشه
🆔
@AlirezaMehrabi_ir</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/146445" target="_blank">📅 11:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146444">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
قیمت هرگرم طلا 18 عیار به 24,000,000 تومان رسید ...!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/146444" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146441">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfA0w-zjae0HcAsnvp3PKDMmJ7bU3uvzqol6AerO2-5mVqsx9eZvLDtLQNue83rrAo2z5oICrRvVIlflvM5Hntgnpgv4rsUa1n1bOvGI_T42tq-B4lwWY7yEVB_hVdEF-DLIVkDseU3nzQNWGTKSxOM934aHrh4BQXbFHLQM6gyha7o0lMmugPI-h9hijcmb1hoSF0lGhLGfcBxh5Xnwr8KgCSsqYzIWNA_ZgKvfBDzwGeaGAYOJblDY33Zd_BOIl9cSkWnauRfiaj_gUvwSFms75GsLyihRh7OT1ddNt0XlQpaV3F5Em_yMLV94Yd9b2IvBKmMjXjGgJGtOzXYYBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c690ff7b.mp4?token=fmamnhF496tGlgsnsEzx8xNHtb6jGMF_pyd1rO-K775ZhWbo8Pv1ll8iHner8wTcwXM08aOw3kWQ_x1We2eSWegQVdEWpMZl-C9UTgP_kX2V6fgVARX0SeKt0iMKtbQFCFUJ5hkTnxghRv0h8gzr7gVUgou_YAd8Q4tR0AJjk7R7aagst-Wd0aNhlXJWgwgzlHuzMwMYSe2zQn0RRPgm5TkK4S-mJH7N4SKQ_kSe612Kt0rL9NLl8KwWXZ1qv-Zl77PHKc2o3PkXtW3b-6szTJ4jV2sEOr7bjuCohVFGYZUjCW6v8KAXssTGHlExHHP0d7nNmsvvl6YwkAoLa_a_eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c690ff7b.mp4?token=fmamnhF496tGlgsnsEzx8xNHtb6jGMF_pyd1rO-K775ZhWbo8Pv1ll8iHner8wTcwXM08aOw3kWQ_x1We2eSWegQVdEWpMZl-C9UTgP_kX2V6fgVARX0SeKt0iMKtbQFCFUJ5hkTnxghRv0h8gzr7gVUgou_YAd8Q4tR0AJjk7R7aagst-Wd0aNhlXJWgwgzlHuzMwMYSe2zQn0RRPgm5TkK4S-mJH7N4SKQ_kSe612Kt0rL9NLl8KwWXZ1qv-Zl77PHKc2o3PkXtW3b-6szTJ4jV2sEOr7bjuCohVFGYZUjCW6v8KAXssTGHlExHHP0d7nNmsvvl6YwkAoLa_a_eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای اوکراینی شب گذشته به یک پایانه نفتی در نووروسییسک، واقع در منطقه کراسنودار روسیه، حمله کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/146441" target="_blank">📅 11:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146439">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jKXfXMtjMohAUJ12GXX0sgObEn455J1tnmiFJHpxYUCoMktfwsdab7c2XjobYpE0ZLMRIRt5hmtQfY2DFBmnLtEUjNbiDPm6omSANRwiY0a8IY8J1NkOBqPnKUvdVorLViz2HRt0Agsl0vByzLJlX6Is2BIBWdG4k1nBViCOQ3BISH1hBddA0j3SUPvoc4OQkEWD069w7KtIo8I582zVJiH7WHf54oUtc84_3aGhlf8KgJYU_wIHwS9WqKoR9QZefeGwqNAjtM2PekCuuIChw7to7xJrWFKl3SnS7c6U-eenAxW9ai14q9i34VJg_QKthDUNsEQxi5ogvpWTidbITQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sxcXCSQpVcqoG7N-s15WwqRoHpjIvnxZ1SFUa1dwCVyX0ZPSb5J52viWa3I5SrvXmodsNxUv68T2odkXw6QSxJ2td4gUlSMJjvpIxvCReiJh80y3jrnH5c1RHu4-U3YqYiXx3GwahwmhYy9CUgxwT4MgQWa1JzAlFdhSvi4MpAusH_1bLPCCsu01Ze4Ux1VrAVO_CReogx_h2XV4AcISxtW5oY6wLj_p2MgXM9vNK3OM3G8BIIuRHriZ3kezSTO8YTbZ_BZG5f9qaNLnamy7tNvRNzHU-LS9uqFSAEL7u7q7q8GEQnO-G66q9dlD0wOQPd6nzOuDtqzAnvhrEnCP6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
اولین گوشی تاشو اپل با نام آیفون Duo و قیمت ۲ هزار دلار معرفی می‌شود
🔴
جدیدترین گزارش حاکی از معرفی موبایل تاشوی اپل با نام آیفون Duo به‌جای آیفون اولترا است و مدل پایه آن با ۲۵۶ گیگابایت حافظه داخلی، حدود ۲ هزار دلار قیمت خواهد داشت. قیمت این گوشی با حافظه ۲ ترابایتی نیز می‌تواند به حدود ۳ هزار دلار برسد.
🔴
همچنین برخلاف شایعه‌ای که پیش‌تر از عدم پشتیبانی از قلم اپل در آیفون دوئو خبر داده بود، گفته شده این قابلیت در گوشی تاشوی اپل وجود خواهد داشت. شرکت تولیدکننده قاب گوشی Dbrand نیز تصاویری از طراحی این گوشی تاشو را منتشر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/146439" target="_blank">📅 11:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146438">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d1aa66745.mp4?token=WGUAFC1gIl-31LsYl6KKkqmwgz8GiH6QKZLpn3pGrhJpRL9jZwX3sAWpHhEmEmoSPk02K3hUW3_sw8An37B5KkBzTSUgrtEfzvL7KMErLOSnVDLxHFTwKr9hmxF7L-LRVdpgtBeI5RXbKaY5YkFPi-RCkf-p3q-Q3f4nTClZcOsBsvotXSzpQ57BNS9aQkXDQsMd6D4pxG64u-BwHfTZ3ypf6jbrn8apbUIk9IaWCmIfhetYJspX6pIV2UJZJ5ak7InW3soMmKOYiUvf-_oRHZMLjdx-vfxT3QnSaJslL03n0fApTzGys_5daoJfa685pSHaC5H1o4f_V4m0Fc2yrAivB0W60gy8TW4wxsJt4QFMX0qQGpCL2vDvqJT5-fCPqCVT7qKBiblU7L465vH957DOR5QUYMVOzUYYWX2r-aczAH0N5lJKOd_GD7fnF3yEEwJ0tVSBQHNeHk7mjqWaqMm160IRVjKoHQXJeKdXgpd4WqURjoifhZDrjB-gy_ZHUKD3TN2Ov6rG9hTTC4LW5RSCsBwyRgeQcF63uIroIfltJeM3iTrHPk5kV8qYz17TH_HzFVIRHS2n5JuexwfOVBwrdDTUgv4Z33i_JD8OwbHaAeKqKB3vNYKRgLCWVEb5bkQ5u8tDpKPP_pzl94bzvxKi5isNF9R3QCoalfOGrQ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d1aa66745.mp4?token=WGUAFC1gIl-31LsYl6KKkqmwgz8GiH6QKZLpn3pGrhJpRL9jZwX3sAWpHhEmEmoSPk02K3hUW3_sw8An37B5KkBzTSUgrtEfzvL7KMErLOSnVDLxHFTwKr9hmxF7L-LRVdpgtBeI5RXbKaY5YkFPi-RCkf-p3q-Q3f4nTClZcOsBsvotXSzpQ57BNS9aQkXDQsMd6D4pxG64u-BwHfTZ3ypf6jbrn8apbUIk9IaWCmIfhetYJspX6pIV2UJZJ5ak7InW3soMmKOYiUvf-_oRHZMLjdx-vfxT3QnSaJslL03n0fApTzGys_5daoJfa685pSHaC5H1o4f_V4m0Fc2yrAivB0W60gy8TW4wxsJt4QFMX0qQGpCL2vDvqJT5-fCPqCVT7qKBiblU7L465vH957DOR5QUYMVOzUYYWX2r-aczAH0N5lJKOd_GD7fnF3yEEwJ0tVSBQHNeHk7mjqWaqMm160IRVjKoHQXJeKdXgpd4WqURjoifhZDrjB-gy_ZHUKD3TN2Ov6rG9hTTC4LW5RSCsBwyRgeQcF63uIroIfltJeM3iTrHPk5kV8qYz17TH_HzFVIRHS2n5JuexwfOVBwrdDTUgv4Z33i_JD8OwbHaAeKqKB3vNYKRgLCWVEb5bkQ5u8tDpKPP_pzl94bzvxKi5isNF9R3QCoalfOGrQ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بارش شدید باران در مناطق مختلف ژاپن در روز‌های سه‌شنبه ۱۷ و چهارشنبه ۱۸ شهریورماه باعث جاری شدن سیل و آب‌گرفتگی خیابان‌ها شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/146438" target="_blank">📅 11:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146436">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ehRJcqsP2tHcHhXyNKbndFH59DNOJZhuibL6u5AoYxZGecwLjftoCIpTNtXUtnWvpBl6zqvdNk1xInOsxZWcpUxGz4ulQOFcrCy-LwYP9f_5D5dQAAMlgOmvxaCBJUS0OvCy2QkJdr3Pw-ms7RVHClBAu23vg-67GkJyQtjepVimdHlp9nRf64tg0xVbTGOlJr9E6DJQZWThM6x7sLoLQvdv63Efpi6Qnzyt7hfTi2jdJhH4MSmrkYHJC6CWC6W6meOGNNwkogNWr-5wxlgIeFWUy9vY0IKO2kxTyjDhvzvU665VFhm_3LBQP9JOKXZzuajX7Ougu3oyO_RZPw5GsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vgpF8n58OA-jFUm-VnPpXqxWluXMEriXtILUz1qDDVHyTHf_1hdhwHEOHXan_bVpyOlUNZljXlib0k1zz-YYwl5G3ThGUB_sHlw2rcEEsL-sOe0SGuS2V7b2f1PgYi-dc8QDmvCgbdqVo8ex_CkPclwacCUHFfN7dR-wRmmj_SFW2hvQ8oVAwY_zDpwomgE6__P-2x4QLNNjr6rNJEl7jW5X3l5Cm1qesPIthREOc56RqVA4mtPxM2q9cAFhFP5ed2Q_jx9ncEKQC8sYvovdPxsBAYoFBVzAeboP0jXy3_Z0F2ZtrItcylaa1ynvgHV7idrIEX_C6BlHG5z3-Yz07A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
شلیک موشک از یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/146436" target="_blank">📅 11:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146435">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 300 میلیون
‼️
🔴
دلار به زودی 250 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146435" target="_blank">📅 11:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146434">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjMyP0YhhDtmp8yi9aNCDnBmsUvE3iHFptoYZkIw4cZAQz0cwH8cBVXz8gFATB0od1-n-xvkk9MAsdAA5RzTjD9sIl9miqvFsjrRVQYFHLuFzK5sdzgVTm85Fwy4Z3O8LNzSDuLMlu1LB9bDNdo3x_It141Uv3BBV1xkj-jt9W4NQBUpv2AKatujBTsFcUj_BUoBZj6mLvWmZnBi0MBjnRPWFnXXJ49hY_YkvfSXl6pl78ugJW3FsbHEXoRVRkqpy3WjKqPRHjQnUwHAjuloOrHmqNbJZCZJVBNZMWTqxKGi9hCBYbmFiBtQE1IueMxWxhUF2xlxirUnKpAH8PgBhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یاشار سلطانی فعال رسانه نوشت:
‏در پرونده فساد فوتبال⁩، برای تعدادی از مدیران ارشد و چهره‌های فدراسیون فوتبال به اتهام اختلاس⁩ کیفرخواست صادر شده است
🔴
مهدی تاج⁩
‏
🔴
محمدمهدی نبی
‏
🔴
احسان اصولی‌صفا
‏
🔴
تهمورث حیدری
‏
🔴
خداداد افشاریان
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/146434" target="_blank">📅 11:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146433">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
احتمال شنیده شدن انفجار کنترل شده در جنوب اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/146433" target="_blank">📅 11:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146432">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBwQVTDVnFzHF8Y6HRnUNM5yCZlEzS10U9cV_vjI50l3UkqjKVk2-Azkc1CViC_pos91jIo2raJl1ja9x5dqd0DUUqMLJBkQysZBFTlD1t838zIUVuDjdSdjyCdDHDWyzGoKjy4IiudnabLhtShrkqy6WpL57btbfEvuSUpHXmamaTSTzxrfwoEFP8fm5nTW9Zh_t66rWYpVBu4rRGl07jIPzAy5mc09GXXT3nUODo_sfbP7k-ZcQyh01ZRpbg99Nkz3wboZpZUVHeF321NEKsz8gdTiC8QZHnR7CsH0vxwSOy_lyrmlMNg16zcgBRJQspRg3QcthRcHsP91NDuREA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر جالب و ترسناک از رعد و برق در رشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/146432" target="_blank">📅 11:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146430">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJE2vKdhHYAbPVf_qjJoed15w2t693lbC2ytIgBGlawXVAtQrYKLh4iOGbd4rQVltfX56baDMPWECM6QkEHiDnwwnTjJebDGNzNErAKppmpIyc-yjGZUi3LkHIVH3hqOghuPoGge57G8OZJl1UeWqr1Mw9Yg6IOXrQ-WsW19IHToF-h-3-3FrC_1RT2_hhvsXHLk_HIVdpDx5XxYJDO5mFPgvFCwwtE0gwYIUkkhLxg4O62NPsRi4-znsjw7Ka3C-k7_hNDL2KRrVc3mHSquWrTfJEAEdhE_dbOvlAkYtSKpk5x3UoPO419hNwholkndAS8IpC26Vp-sKsyGgWhOxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/759ddd2cc9.mp4?token=WjpMj2puOBfb87365UMCUDUeeruV_HDr70ZYa6iXvIFl9gXmfAqx_EPc_A3d-aPZSSg3GRgPjZUaSm4xOMteWg0kJvG-1fpkQA8_JPkqsRMI9OLum1GBAy8n4yJ5LlWSuFH7u17FtlM_INFydQUv0ywC944Qria_ocX5vP88ymZjA0t4HEyZKLDhvSEKVxyxTjO10khoSYpgRXev5Elt9l_iN-WgAdHwcwIg1uNVQCr6d26ayzABzdeHn0pJ6KIK577IlhsKnftIp0YWAo7HruflJKiPtvJ88xqHhXmXGApIx4EBNFarRzYz186EOPEIgk5s-Db4xuoS28tgCxKg9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/759ddd2cc9.mp4?token=WjpMj2puOBfb87365UMCUDUeeruV_HDr70ZYa6iXvIFl9gXmfAqx_EPc_A3d-aPZSSg3GRgPjZUaSm4xOMteWg0kJvG-1fpkQA8_JPkqsRMI9OLum1GBAy8n4yJ5LlWSuFH7u17FtlM_INFydQUv0ywC944Qria_ocX5vP88ymZjA0t4HEyZKLDhvSEKVxyxTjO10khoSYpgRXev5Elt9l_iN-WgAdHwcwIg1uNVQCr6d26ayzABzdeHn0pJ6KIK577IlhsKnftIp0YWAo7HruflJKiPtvJ88xqHhXmXGApIx4EBNFarRzYz186EOPEIgk5s-Db4xuoS28tgCxKg9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رنگ‌های آیفون ۱۸
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/146430" target="_blank">📅 11:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146427">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRzNUQ8PDe4dM76qpnv-J4ndiSEyWtBzKOozPMJCHS7zZ-cLywL3q8cT95roKDYn2cqGGcdHj-AInbuDPKvg66exU72eTnfFMc2KOMZN0OduNgyDUN_hQd-aBwq0MfmFv0RY_pISP75a6VdTnqmjen38T8OpYwrQoBQV84VKMEcb0hc0r7UIUQ4MFA4Pqs8EpeyUHuocdqXLB3HmaCJh59Gd783p_s11snib7XNzVc2TOMvnsTrdPChPT3zgKlR_9-QyxRTk5fqRrzQjBio0LCTSco_JGZYa7irKQtzLTJY0V2qoHEH7-t1_euxM0hIkUtSlgZ9SF6XurcI3qUObUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت خام برنت برای اولین بار از ماه ژوئیه به 100 دلار به ازای هر بشکه رسیده است، این افزایش قیمت در پی تنش‌های اخیر بین ایالات متحده و ایران رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/146427" target="_blank">📅 11:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146426">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e37c9e54d8.mp4?token=LhnGOmiHk97vsWPp4Z6EXB1dGA75a1PcSwnYfIxuXNc7q71TahbEZEbDTSHCNlYo97cKd8fFqXD59rL4dnZZ2SCwGUW9ySe72XG4rxgHWCR9udsqQNrMRjFxT_7hJDGn4w8d7Du6U6u37UXCFAua5_ajhetqHKjnANZVCjyXDj55wCEO7Y30trKfVpcm7fWtNdWZZbrkHyCj4c8Fh5bSt5_2EtBIvLFVp2Je0meO8S-_-ntsXYyV4H45kCQw6q8FZzt3XIcCxbIYzIli5r_IP1A7pya1NroPSyEsxOwiYt9cO9ABZqS6c4fSijMndKS7y4jNVgFUVLmpsEjKZFbrew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e37c9e54d8.mp4?token=LhnGOmiHk97vsWPp4Z6EXB1dGA75a1PcSwnYfIxuXNc7q71TahbEZEbDTSHCNlYo97cKd8fFqXD59rL4dnZZ2SCwGUW9ySe72XG4rxgHWCR9udsqQNrMRjFxT_7hJDGn4w8d7Du6U6u37UXCFAua5_ajhetqHKjnANZVCjyXDj55wCEO7Y30trKfVpcm7fWtNdWZZbrkHyCj4c8Fh5bSt5_2EtBIvLFVp2Je0meO8S-_-ntsXYyV4H45kCQw6q8FZzt3XIcCxbIYzIli5r_IP1A7pya1NroPSyEsxOwiYt9cO9ABZqS6c4fSijMndKS7y4jNVgFUVLmpsEjKZFbrew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تذکر صریح معاون دفتر پزشکیان به مجریان صدا سیما: شما همه چیز می‌دانید! تجویز نکنید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/146426" target="_blank">📅 10:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146425">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsCsO3SRH1ul07CK7o-c9rrNaIvNwtnZBNNQeZJSNlWecCxv1yptwTbpxLfGCQ6r3x4nhll1-CW5F7xhF4vLkVF7kuKIpsyo4mFv5wPfkltbthzkAje2tx82lpyUMAElZovLqI7XgbZzOneS50_T3deXoPW_JyS6wgCsF015dPg2jkc2MwBxDV7Z4ISuokTqkS2sQMXYc0ejf-cduCMYHcMQqYG3SvARmOQzIkdoBBo5km0EJqq2IekvJlh--TdTcI62_t--qJ1ezpeJDfZYbRGHFdfViTiT4Qogmm0ajTbG3fqWUuJAoWCxH1-0l6C7_1hDD-oBwspfRj86Rrg37Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش رئیس سازمان فناوری اطلاعات به کارت زرد مجلس به وزیر: دفاع از حقوق مردم اگر هزینه داشته باشد، افتخار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/146425" target="_blank">📅 10:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146424">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
اسرائیل در اعتراض به تحریمهای جدید بریتانیا علیه شهرک نشینان به کنسولگری بریتانیا در شرق اورشلیم اطلاع داده است که باید ظرف ۳۰ روز تعطیل و تخلیه شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/146424" target="_blank">📅 10:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146423">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
فوری / گزارش‌ها حاکی از آن است که یک نفتکش در نزدیکی سواحل دبی، امارات متحده عربی، در حمله پهپادی ایران هدف قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/146423" target="_blank">📅 10:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146422">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
مقام آمریکایی به نیویورک پست:
در صورت ادامه شلیک‌های جمهوری اسلامی تمام ناوگان نفتکش جمهوری اسلامی  را هدف قرار خواهیم داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/146422" target="_blank">📅 10:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146421">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2dd7afa6.mp4?token=chu7hYMPgI-BSmEaA7k3XPSSvApcfWv3f2DJwnxD-N_csSfxanbVrPnb-eaBzVgJVz6rEl6_dN9M33IK6pkmWQdHK4HIDdKUiRbJfU1e4jx_HwARChyPHXYt0claSV5kM20ev9PhKovbCGajDON1i8lygZohkPuxAuawNbKwRYFWWmyR5MUfUMyd6p3o-DfnGcFtUPkmPjSyWTpV5-t9Chn4Hkwnqaj5HWc7IeAgHTk1t5cUdNu0Fqxwtq669TqIhIO3VECzT3Fidsh5EYeTs-0rgFTeYjMxUxz29734NqlVJGB0jsHtRv3A2hiwzzzJpv2yq1lkoNZ4iNDZwJLd9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2dd7afa6.mp4?token=chu7hYMPgI-BSmEaA7k3XPSSvApcfWv3f2DJwnxD-N_csSfxanbVrPnb-eaBzVgJVz6rEl6_dN9M33IK6pkmWQdHK4HIDdKUiRbJfU1e4jx_HwARChyPHXYt0claSV5kM20ev9PhKovbCGajDON1i8lygZohkPuxAuawNbKwRYFWWmyR5MUfUMyd6p3o-DfnGcFtUPkmPjSyWTpV5-t9Chn4Hkwnqaj5HWc7IeAgHTk1t5cUdNu0Fqxwtq669TqIhIO3VECzT3Fidsh5EYeTs-0rgFTeYjMxUxz29734NqlVJGB0jsHtRv3A2hiwzzzJpv2yq1lkoNZ4iNDZwJLd9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از انفجار ایجادشده توسط اسرائیل در شهرک المنصوری در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/146421" target="_blank">📅 10:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146420">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVwt01G0tW47zWlOKufdn7rjB4y5f7nntaJurIji2GWumhcI3JOoFyuLTKrfAxVmc-B4Z2Pi7TzGkpowopSb_VPooajHXJoK6430fBiej3XyWwUbpdxYgHvT2ItOlfsngefdquEv8SHfyEwK-kB_a1ITb8drd5AiBD9f4JLX94QOWVebIDr6-xOxb2PdFSsDEUNixHTjEGk26rQ0-3RsuzOxljfjwLUALxc21w0rYIX35xnSVJb9WTr4tm-0PbtFTAjJdJtCmS-5rLsoYN8Wyf8NE-RfG8pQCKVSa_XYhsZ3umpRIfwXfOeFVwtCME2CX_GMoE4wqx1EjzgtFg-_-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردم ایران با دلار ۲۳۰تومنی تو مترو
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/146420" target="_blank">📅 10:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146419">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پادشاه آفرود ایران شده 1/300 میلیارد تومن
‼️
🆔
@AlirezaMehrabi_ir</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/146419" target="_blank">📅 10:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146418">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
آخوند ، طائب: آقای ترامپ اگه میگی مارو شکست دادی، پس با کی داری میجنگی؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/146418" target="_blank">📅 10:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146417">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
هشدارها در خمیس مشیط، جنوب‌غرب عربستان سعودی، فعال شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/146417" target="_blank">📅 10:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146416">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره
آیدیش:
@khabar</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/146416" target="_blank">📅 10:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146415">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5KNhbaNWq0LGTfyhmBLYN0_yAnaiwZvetuDX1bzx_T9vk47Bf0oaA1EdAW-VgiaGNjy3aIrA0lniyVVL3-Dsgz6XXBuO3nbqBqOoQMDpb26hx0qMx-JDsFVMQiU9n_4urCTEKMtRlqSHMiLaAQA-5STqsjAdG3QmG3Ud1IYC-DB4NxAOfEHcDLUeQ-CwVpASpJn5OSMvDaiJ4EqjghGUKLoEgNn8pSFJ3UncxGsmJ9T3bmu_yfya9KYBG-Vqvh9hUf0eIdAwIV087mc4HGCwjdp9oc1qKug241skhyRyUv7qUKvmGYo8wEwLhU_JW72i3QP3-RMM-W--Idfvdg-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انتقاد حشمت الله فلاحت پیشه از هدف قرار گرفتن نفتکش‌ها: ثروت‌ های ملی به آتش کشیده میشود، باید به ایران سوزی پایان داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/146415" target="_blank">📅 10:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146414">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c43f6f01e8.mp4?token=g_Z31IviVSjczsPj_j9ac4yYJ6m1uXxV6iv4UDXwXJWOTUg6YyJF-vo1zrQ2qdllN0Y382XGxwtNRlZ4m8t-AkLtKKSF4E8xSLdBkzn5RX5U0G2113wARPSoju6sswcoSI9EF5QmgzdbuC__rK6x0mdNX6v84pvStcQXb_EUssWfS-JQ-fdOaPoPCeLT_KfCQfb17EDcmpw5aJ5JR1n7m86paaq10RhC_nbz4wgQ_1FSYDo1mTdJz7YBdQNbBqla48rvAslbGlycZUVtohX-z7U1FJhL0bAXRmb0e1gpJRN9bwEBNndAd0bqR8DfJi3ShPOL6WVoqDTtuJcMdqmoeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c43f6f01e8.mp4?token=g_Z31IviVSjczsPj_j9ac4yYJ6m1uXxV6iv4UDXwXJWOTUg6YyJF-vo1zrQ2qdllN0Y382XGxwtNRlZ4m8t-AkLtKKSF4E8xSLdBkzn5RX5U0G2113wARPSoju6sswcoSI9EF5QmgzdbuC__rK6x0mdNX6v84pvStcQXb_EUssWfS-JQ-fdOaPoPCeLT_KfCQfb17EDcmpw5aJ5JR1n7m86paaq10RhC_nbz4wgQ_1FSYDo1mTdJz7YBdQNbBqla48rvAslbGlycZUVtohX-z7U1FJhL0bAXRmb0e1gpJRN9bwEBNndAd0bqR8DfJi3ShPOL6WVoqDTtuJcMdqmoeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترمینال نفتی روسیه در دریای سیاه هدف قرار گرفت
🔴
پهپادهای اوکراینی دیشب به یک ترمینال نفتی در شهر «نووروسیسک» که یکی از بزرگ‌ترین بنادر روسیه در دریای سیاه است، حمله کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/146414" target="_blank">📅 10:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146413">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
اسرائیل در اعتراض به تحریمهای جدید بریتانیا علیه شهرک نشینان به کنسولگری بریتانیا در شرق اورشلیم اطلاع داده است که باید ظرف ۳۰ روز تعطیل و تخلیه شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/146413" target="_blank">📅 10:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146412">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/co_kKBK4cvNU_k5Rva3GMl0g-Klyhlwg84L1iOKFeKUOzyXTS2qV8LXlAleKjs-MN6U4czVwdPfBbO0UERaiO8bFk5TRvtcmq1RAtI3-1dp-RvDtEYUH4idoool83lEepvzeaK0sYhURopBmaKJQ8QxyEGwMDR1rgbUed95x3p-p6bWdGt0ZMhA9UpWn5tBNThpyd9XvlBhhSx3__mNZ_Vr7kwcYbODh961F6upwVeJ9zpN7rlRiTtGkRpZkhlfuv7keMdiaPJaYN6XB7BeSEV1yUWl_B_RXHztN3spODbzEsd0nroQAYTM5v6a6GNZ51Ckj7P_AfEHAFwB9yH491A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مدیرعامل شرکت ارتباطات زیرساخت ایران: قطعی فیبر ساعت ۰:۵۵ برطرف شد و شبکه پایدار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/146412" target="_blank">📅 09:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146409">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/inIuEH8QAhIfHrT_2Skj2KXK9wlO2eyiyvEpXGx4DGz9khO4Mnan8lpWgsaCz6HGP37wVxVzbBmvu8MGkb_BLo7d35zzEVQMZVHVvK1A79ZPSVky0V5C18K_OW_9gHxFxDUghRE-S_1XwCczOPs6MWydR8WVLxIKjhLad2E0IOp_6vG9tstAzJrUf-upStdDnBq3m5E2kmT6zzgba4OqZKUHth-DNMJI79QS83PofzHU0QUL5lvoXy-tTdkImRJpZPt3kp7Ub2Ue5y6Pt-cxpVWo4cU_CBFianeqGbcMFfz4EYxyVvVtkXFOhAXy8znPXSF5B-xjonh8MXyMY9tlhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PjmB8-XZw0GePfMtS-2g-iIPCEP3IxCartSfwtbsC_jhRZ4Xi0YOf_4hNoIQva0Xn89V3ek2rLP8Izkdg9cc_-7stG5EiyKQ-nWDfFZssg3H1jHKslGbXWd6khnBvkbY-d4xonapiZ_Rnk12MmW2xRoyPz8UJEWRnzudhb9d8iXmWx23OtKoYqk8p9yTlBU-D4dlkOSFI3uzzv4sdXYRP0X4pNfeXvfEtBKzwY7Hd9u22UANIWNvAUNDOEaisEcy93C10Z8AEKMuTgKmpXITS3NPa44l9BU_WUSDJ8_UfEYHZMtrCf6eGSVlhBb-Cupxihq6kCvR93Vd0I7QqdNJkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eoXSU0_X1_EUuDUkgxQr4MSV1sWQMIrSV8kxueX48eodPusVmWwXMsnroWW8h3YEFvcRdWa8TvIq11Xant4dcYCLE4s9pGqIhWk9qsYJa5k5c2Jl7g2ZSGqtTZEmNDAMGCGOhNritU7RIhNUtQ5GbeEL4g_isW6NHLBl3-JSe_DCA8vcy8GNCyxD9NyVMOxvkk4yIy6WhyzlrCGh4JyAm2hIPddO0OGEeJbfsqKYM4mG78U7sRDAAsb8OWop3SLIxBwjtMxzg0xRb-mXnbeshpabiof5e96_HrA8Jk6J6TrITz012HZlSe0ICLxQ_pB3VEyH0at6nWUzc_gE7TTfEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
آسانسور غول‌پیکر چین؛ کشتی ۳ هزار تنی را ۱۱۳ متر بالا می‌برد
🔴
سازه‌ی بالابر سد Three Gorges Dam در چین کشتی‌ها را تا ارتفاع ۱۱۳ متر جابه‌جا می‌کند.
🔴
این سیستم عظیم با وزن ۱۵٬۵۰۰ تن، زمان عبور شناورها را به ۴۰ دقیقه کاهش می‌دهد. استفاده از ۲۵۶ کابل فولادی دقت این مهندسی را به دو سانتیمتر می‌رساند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/146409" target="_blank">📅 09:46 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146408">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
وزیر خارجه آمریکا: در واکنش به حمله به ناوهای جنگی ایالات متحده، به حملات علیه نفتکش‌های ایرانی ادامه خواهیم داد
🔴
هر بار ایران به کشتی‌های جنگی ما حمله کند، یک نفتکش را از دست خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/146408" target="_blank">📅 09:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146407">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b64f3accac.mp4?token=GLfgkCbNXh6K3fxOQuoURdtF5hZ8-Zfvvw3dxiNAc9-Df4MMll4ys3TDawMhCHGBOgKCrkul9eWVQ2-VYKkSuOvIcy5CUJW50Str5VubNUzjqzjBPlLrk6MT0MMpodTVY1n9YRcwyZKnGUCy1oC1_UE8hnJIlz6MrWsa-jPAdBX-POjLqYH3eAsnvUpSFOrTW0okDW2ga-giszdtxMnKItzPyVXVCFOxTXjm7IJHM3IJoTYEugqYPRFxXx0rHg4KQlk92a4O2mAxCdvAUZg5MokWsodN7PFbN1POjD1s9nKrd1_kukdOcVN9ET428T0rOBTk8ODOLa4XEOs0xkTaKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b64f3accac.mp4?token=GLfgkCbNXh6K3fxOQuoURdtF5hZ8-Zfvvw3dxiNAc9-Df4MMll4ys3TDawMhCHGBOgKCrkul9eWVQ2-VYKkSuOvIcy5CUJW50Str5VubNUzjqzjBPlLrk6MT0MMpodTVY1n9YRcwyZKnGUCy1oC1_UE8hnJIlz6MrWsa-jPAdBX-POjLqYH3eAsnvUpSFOrTW0okDW2ga-giszdtxMnKItzPyVXVCFOxTXjm7IJHM3IJoTYEugqYPRFxXx0rHg4KQlk92a4O2mAxCdvAUZg5MokWsodN7PFbN1POjD1s9nKrd1_kukdOcVN9ET428T0rOBTk8ODOLa4XEOs0xkTaKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
34 میلیون تومان وجه رایج مملکت
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/146407" target="_blank">📅 09:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146406">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
سپاه: ناوشکن‌های رزمی DDG-119 و DDG-53 آمریکا مورد حمله قرار گرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/146406" target="_blank">📅 09:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146405">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8hpwdcJJe8JrUhvSDx4BKuGFjwqb2hIsrUSPT6APJKzjO7eVAL0k27-vMA8TGZthfpuzWNFSnC6oYRS115VjuF7GPI3pxky6u5zJb6z9FRe9coS30khR7Mx-KE85y-CsOJiSqqXPRhSO3nOpH8SB8ARpXJx5Qvd22uFl1m7fUX0gka4OFrjhgNVe-vI-MVJG01GnWofatl28v9yjxdWYgpMEKPiOXa_X3mbGv2lipF7Bi5Gb-EOAhgx1oHn4DvBBa3AFSn8ATdcGSWzjsbxH0FkVty10v0Ltx7Qv_JF6HmMtNWe6dcNWzPHqlXMr2d9XGuTK-M_w3lPwkG7AHWlUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس: دولت ترامپ با اقدام تحت رهبری بریتانیا برای تحریم شهرک‌نشینان اسرائیلی و نهادهای دخیل در گسترش شهرک‌سازی در کرانه باختری مخالفت نکرده است.
🔴
به گفته مقام‌های آمریکایی و دیپلمات‌های غربی، اندی برنهام، نخست‌وزیر بریتانیا، پیش از اعلام این تصمیم، ترامپ را در جریان گذاشت؛ اما ترامپ مخالفتی نکرد و از لندن نخواست مسیر خود را تغییر دهد.
🔴
مقام‌های آمریکایی همچنین به بریتانیا گفته‌اند که درباره سیاست اسرائیل در کرانه باختری نگرانی‌های مشترکی دارند، هرچند با خود تحریم‌ها موافق نیستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/146405" target="_blank">📅 09:21 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

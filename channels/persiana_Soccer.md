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
<img src="https://cdn4.telesco.pe/file/gP7Gih_e1TfWC7ws5IrNMdfbarMNY8CbuOJ2deizAjVUQR_Xjf1bv-PDumnegGfyZ4VMQj20Qatd-PPyMjymY4vmltHDziOOEiW3KbcbA8KPW-WKt8Ap9Akx7pKOo6f6lB_mt2IQLg5l8Whn9ZoW8O1Ya4IPzwAyr4PVD_80QG2uKe8-JQ6OWjO3buC9-nZ3C7XV45n-8uxVnLv_Z5UzwwhjoSue5B9uhlrSZbQTDbXx-k-4f0N6mim2Hjkwlfy7BpywY9FseToecF6-KMEM9abKQaYGCcQVtj5ASh2TQVO_gNGOvA2Crj2PafftzmqAygWB-4eglPuCgBHCCe3_bA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 606K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 16:41:34</div>
<hr>

<div class="tg-post" id="msg-26879">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e6b766e58.mp4?token=hUxtuggM9yKRrgxDBdNMz3_HlPmvPgXw0KYtrshL5PDRj8atdGVfcDYslbISAJ2AuZhewmHA-f2PK-OHVXh5cqtU9E7aqc1SuPgUcgw_PQKeCxgG0jpWpRKJ3lU9qRNyWFTUOjFZDXMBw4348yljuGZLlr_-yLZ87JA-WBA0tAd3y88K58ehLwvHc-ImLwS7pGaB_SWzdUUk3eENMIMmkP9eAGcu56gwBWhT7FmDUH8nrDuj8rwAhzulcR5-mAsWlr-us_HHLAnAFNb0xdgM7bBxuJAnqykgOzzgETZ6JntLLZrbEqHXeOPAP4wZrqzeYmJR77JPHUrEq9f5AYjSdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e6b766e58.mp4?token=hUxtuggM9yKRrgxDBdNMz3_HlPmvPgXw0KYtrshL5PDRj8atdGVfcDYslbISAJ2AuZhewmHA-f2PK-OHVXh5cqtU9E7aqc1SuPgUcgw_PQKeCxgG0jpWpRKJ3lU9qRNyWFTUOjFZDXMBw4348yljuGZLlr_-yLZ87JA-WBA0tAd3y88K58ehLwvHc-ImLwS7pGaB_SWzdUUk3eENMIMmkP9eAGcu56gwBWhT7FmDUH8nrDuj8rwAhzulcR5-mAsWlr-us_HHLAnAFNb0xdgM7bBxuJAnqykgOzzgETZ6JntLLZrbEqHXeOPAP4wZrqzeYmJR77JPHUrEq9f5AYjSdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بااعلام‌‌باشگاه‌‌آث‌میلان؛ فرانکو بارسی اسطوره و کاپیتان‌سابق‌روسونری‌صبح‌امروز درسن ۶۶ سالگی درگذشت. این در شرایطی است که در روزهای پیش خبر فوت این اسطوره منتشر و رد شده بود.
📊
بارزسی افسانه‌ ای ۷۱۶ بازی رسمی برای باشگاه میلان انجام‌داد و ۳۳گل و ۲۴پاس‌گل…</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/persiana_Soccer/26879" target="_blank">📅 16:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26878">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de98c1f92f.mp4?token=QWtXW4ckxMS_Z8LxcjzR6tOjnMTj3QAptbwYDD5_DcmqiyLcgtXEQ6sEPu0yqUFD2YilgV6E7Mrz-j62ubBbyF7PSEl-wAMC_l2_yn6jv1FJiGfKpL2T0PaA_uO2GBUTZwix4Uu3GdzM5zj3PcJX1v39b0ai4datnyHGvvm5OnsnoDX2gdJvzeEwbwQftggPiVrqp374inqbzVKpA1YFlhNphcD_KFfePWb5WPcOUMkHOLZW5MlgFfLF2x59uTo3ap-sx2TagrdBTgm9T21X36s1_WXAHx38MPXHpoA-36cC9kWqsbBA8HdoF-F_4zgj6oTSMLcfHeDqM_dxBIlbgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de98c1f92f.mp4?token=QWtXW4ckxMS_Z8LxcjzR6tOjnMTj3QAptbwYDD5_DcmqiyLcgtXEQ6sEPu0yqUFD2YilgV6E7Mrz-j62ubBbyF7PSEl-wAMC_l2_yn6jv1FJiGfKpL2T0PaA_uO2GBUTZwix4Uu3GdzM5zj3PcJX1v39b0ai4datnyHGvvm5OnsnoDX2gdJvzeEwbwQftggPiVrqp374inqbzVKpA1YFlhNphcD_KFfePWb5WPcOUMkHOLZW5MlgFfLF2x59uTo3ap-sx2TagrdBTgm9T21X36s1_WXAHx38MPXHpoA-36cC9kWqsbBA8HdoF-F_4zgj6oTSMLcfHeDqM_dxBIlbgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی کوتاه از یه مسابقه والیبال محله ای در زمین‌های خاکی؛ جدا از بازی‌خوبشون و اون دریافت خیره‌کننده‌بازیکنه به‌وضعیت داورای بازی نگاه کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/26878" target="_blank">📅 16:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26877">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjkcygl8AV4TBXK66UHkx5XMnaQSTUR-ugJ8irgPfywmI_YhcQu96aqj0H-sM_f93Jo4lS2GowU6ALO4thz-Mfo586guwTc7HP9V4t3W2dhyOvBaOsxTc11ARvxjW3SfPqOvyjZ_C3aYpg-ahLBVBx0u9CsVWndXxRlmrx4Ly8UDosf3Q4Jiey0KqZen19aDXd-qKW8KRSpaHJmMkY2guOjB_zPpoBa7DygWRHqvkvdl9eVYwsHO2iUjmjLOhk8TKKSfOPmomajdMap2y5Ukhd9dmA-w1-evuaCZmz6S4BZM9zem-rFZRaZhhfhQgWZNESLHHMPwoR-OCWnfumN_xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات|وحدت هنانوف، برایان دابو و ابوبکر کامارا ۳ خارجی سپاهان از این تیم جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/26877" target="_blank">📅 15:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26876">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kp9_ZXi--1k39GArbIrWmB085UNhO3q0un8a4hTWoREpaaosP5YFxl52MNBZnJ6sJ0duBHSHSL_t4OSbv-dpV6p3wgAQf4e0z39jMMeLE-E158_oQQmMe8Y3cx-Hz1x9zVRNq_NVlOT4JwGSKSfZ7--Y8C2he0h1mXTEXMkRQj73GzkzF5DHLCw-CnCSUVCBmCS33ZBri2uXSHz3tw7lhhB19MXwiWR7HiY7dGK8xpo8tfM_qS-MlxEh1OJZr6gk84Xlnq1toqmpPLTLHKZ9CCEDxeXCFzzgLWgS47_IK1U2gWJMJuIrf3FsKCaVKZjziVxaQMknta6FH_I9ChcEJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه تراکتور ظرف 48 ساعت‌آینده‌از محمد قربانی خرید جدید خود رونمایی میکنه. رضایت نامه این بازیکن دقایقی پیش از سوی الوحده امارات صادر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/26876" target="_blank">📅 15:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26875">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f12e49800d.mp4?token=J4LGHYhb1eM6gDjGWgXEw-jh27vUYGMR4WC1IfwLUZDIv_JobhnVfCYC7CJiESltiMfNrKQ3t5SbftDzySNcBQj1H-pwzg0Y3ulnh8VpheeVUABb20etxqDDrFXDBJfN7h0HevIsxj0-J8l8GShGN8ra1Dh68QQmaZNVon0rC6ekt-kf9YA9EblOMThb65CRW883vXkg-u3AQWkTXEF85xtAtPM1e-_lpt-JbAg_BiQV0iwJZpaF3vnhLSCAX-V4E5ne48RoNVctewSvnQfmHiwS_40mzL4Il9Pk5AsvaHMfHd3UEmzPZYqnL0IAmPV-hxiPa6fOH6unYLL6oTGwqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f12e49800d.mp4?token=J4LGHYhb1eM6gDjGWgXEw-jh27vUYGMR4WC1IfwLUZDIv_JobhnVfCYC7CJiESltiMfNrKQ3t5SbftDzySNcBQj1H-pwzg0Y3ulnh8VpheeVUABb20etxqDDrFXDBJfN7h0HevIsxj0-J8l8GShGN8ra1Dh68QQmaZNVon0rC6ekt-kf9YA9EblOMThb65CRW883vXkg-u3AQWkTXEF85xtAtPM1e-_lpt-JbAg_BiQV0iwJZpaF3vnhLSCAX-V4E5ne48RoNVctewSvnQfmHiwS_40mzL4Il9Pk5AsvaHMfHd3UEmzPZYqnL0IAmPV-hxiPa6fOH6unYLL6oTGwqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇧🇷
پوستررونمایی‌رسمی‌باشگاه اینترمیامی برای کاسمیرو خرید جدید خود؛ قرارداد یک ساله همراه با تمدید خودکار به مدت دو فصل امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/26875" target="_blank">📅 15:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26874">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzESNnSo9XWyeJxAMsPfHHJfBJHbAt1OE4I8lTPF8ndQ_0IQC37gw3h5GMw90TeEuPTEyR9ImD_MHD8-3XeSRIcLqMb9FdFboDl-nQJwoXgIAZrXIEcRR8NGwYRNvzd4U4HaPpmtlJXzN8e8at5duLei2Uhhr1nuatljG0gJKPWigGal1t4Y9rOjs6ZkE67J-iqm0aJFPlsKLqbE80HvqmAoY44MtlG6WNsbCZeEi_H6j04cwvHPOJsKYcJgr55zHsYC36qy34UfPw_5Oc-39SuDz8dSYcPtQhy1meJPCun2JfVP6TVfHwsn4JgmrSVthuet7_R44rHKtUQZinAUMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استارلینک توکشورعراق‌فعال‌شده. قیمت‌ها هم با دلار ۱۹۳۰۰۰ تومانی: ۹ میلیون‌برای‌سرعت ۱۰۰ مگابیتی و دانلودنامحدود.۱۵ میلیون‌برای سرعت ۴۰۰ مگابیتی و دانلود نامحدود. میانگین درآمد ماهانه مردم عراق: حدود ۵۰۰ دلار که میشه تقریبا ۹۵ میلیون تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/26874" target="_blank">📅 14:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26873">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0molnG4jUPPGvf481j3SMYcg3D5BpYoPPtYu2_eUYhy1ojzPhW875Lxhu-E7Wm994kl8u9hE77Ev_AzppxgDmcdkFVZGFbRs-aGNbJb_lrinjFOrqHDjW4eR694OlbcaOaeLwq-h0Z9cJOjpAs_0otICIbwwPJn_okadG9xjVCuCpQ8kXhKhrTAJTsuQkqojLBVJnB_l1RdKK-jR9jyPjEp_fuI0SXp75WNJzwS9GID0njRzzNpOXd9-h--bkSVEOi_Ui04KxnE1TGTla1M9LOJQLs8kOjQr-DQSiPxxsnBY7LkctRmLZqT0aV43NR9UTRQyR9CtHOypJ6v3f4mkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
باشگاه آرسنال بزودی بندفسخ قرارداد برونو گیمارش روفعال‌میکنه و از خرید جدید خود به شکل رسمی رونمایی میکنه. تمام توافقات‌انجام‌شده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/26873" target="_blank">📅 14:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26872">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a91beb718e.mp4?token=iY5NcvczBePxJ7_8x4kbmtqReYJA-f2i2eIyPrjidL1vIPPv1_u59sQ9ai2iY7CqJaVRW5KMKHx8szCW0YI-OZwcYkZl_lwT-VyLjJla7G30o234WKAM9CFCoaQ1LvRfQQm7BbB3QYH66GA2gDehZ7vWguMzVXRwbRynvvJcsov3MudjjbGrmzIkl5YC-_-7DBaD524Ygxkjit9zw2K3K5HuC_8ZLhDK0SBdHZ1YL5hO_lZM47FtjgOIssas5Ma9vOn1o48BeukCV9lOlw6tgtHCRNt6K7tZxNE5qwJbTQTvN8JliT-nmFlh5CcYzGxXWWNBJ4pvHnVczQ4kTDjNIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a91beb718e.mp4?token=iY5NcvczBePxJ7_8x4kbmtqReYJA-f2i2eIyPrjidL1vIPPv1_u59sQ9ai2iY7CqJaVRW5KMKHx8szCW0YI-OZwcYkZl_lwT-VyLjJla7G30o234WKAM9CFCoaQ1LvRfQQm7BbB3QYH66GA2gDehZ7vWguMzVXRwbRynvvJcsov3MudjjbGrmzIkl5YC-_-7DBaD524Ygxkjit9zw2K3K5HuC_8ZLhDK0SBdHZ1YL5hO_lZM47FtjgOIssas5Ma9vOn1o48BeukCV9lOlw6tgtHCRNt6K7tZxNE5qwJbTQTvN8JliT-nmFlh5CcYzGxXWWNBJ4pvHnVczQ4kTDjNIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
برنامه دیدارهای هفته اول و دوم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/26872" target="_blank">📅 13:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26871">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9k9j7dI6Xr1X-K4DlWcTPF02avDCMl5h3BRaAVPkoeWy6_Yn83KjcVayEP3hkCKL6s78gGDhGoKpmJ1QFwhVc9UbArWqgQhmkcTvnpnA-6njd7wRqSYGRJxeipkccypn6SF2PLWYqtUcJ-Po26aOnIDE9_e5-ut6j9fhcgVpL2Q1ZvoFYd3teboQY53L2U8e_Bz5xJsCh_rAx78UTBtURZP5zsiYPZFL1yHMa4tst8YITcsbdX0rlCybdGuuXsqui2OW-euVcJkKr-2DO_9ylaWXVFQbqdZDyNWkmKoZFmHPb9eqOgZzHH6kR-LisqZrS2as52hOPMS1SRDmJCqIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مایکل اولیسه که علاقه زیادی به پیوستن به رئال مادرید دراین‌پنجره داشت تو تعطیلات در حال خوش گذرونیه. ویدیو مثبت 18 بود تو کانال دوم گذاشتیم. بزنید روی پست ریپلای‌شده کانال‌دومم‌داشته باشید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/26871" target="_blank">📅 13:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26870">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2b1c64c36.mp4?token=r_KcXMcOl2rB5CgEwNBvTmrkKZd_-C1ldWBImZlbZ30plCPkTNTghHhrLLSHHGc3yQAcPcsWKDxyCBkYCw5wbdZf0yFtiKMpugDzRqIYf6WHuM7h2XyUseeTY4aWLQZsiXlw1_pwmXJsluwV2M57zqim7IcIy-s_4rgqX63kH324PsbqpvXpsazWgQhrhVJ8RoQsnlIg5IMB-wQ_bcQ2hTjMBdYft4KqyigY0moezYw45xmPI8NgbiVqCfXh_eGicmoccerVO69pmxghCxOgmc6l0jWTDwRQaklChC8DDdQ9CeuxcUihaLTmZk_BqzwX-k-zlL36vqdWizs0UNOrrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2b1c64c36.mp4?token=r_KcXMcOl2rB5CgEwNBvTmrkKZd_-C1ldWBImZlbZ30plCPkTNTghHhrLLSHHGc3yQAcPcsWKDxyCBkYCw5wbdZf0yFtiKMpugDzRqIYf6WHuM7h2XyUseeTY4aWLQZsiXlw1_pwmXJsluwV2M57zqim7IcIy-s_4rgqX63kH324PsbqpvXpsazWgQhrhVJ8RoQsnlIg5IMB-wQ_bcQ2hTjMBdYft4KqyigY0moezYw45xmPI8NgbiVqCfXh_eGicmoccerVO69pmxghCxOgmc6l0jWTDwRQaklChC8DDdQ9CeuxcUihaLTmZk_BqzwX-k-zlL36vqdWizs0UNOrrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
توضیحات و عذرخواهی میلاد کرمی ملقب به وضعتان چونه درباره تبلیغ مرز ایران اربعین:
‼️
یک بلاگر معروف در فیلمش گفته بود در مهران ماشینش دزدیدن از این مرز بد گفته بود خیلی هم وایرال شده بود خیلیا دیگه برای رفتن به کربلا مرز مهران انتخاب‌نمیکردن؛خیلی از مردم ایلام…</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/26870" target="_blank">📅 12:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26869">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFygl9nbpfW4LYY1SGGnIzGpnzZBNQ7lJG1o20GVJQ8pcVuGUwy44hfLsfiwn9d53tY6huk0oxnSdTZ9cwV1_7uXpTkipPoQAPFNolPO7Vlxy2YMWhREKCMLGJg0NNCZ76LpNMxrR0O13lMmIXEY6FBvDDzrjOvEg6XRoGheOZBWvNXwzr6ZY2RsUFK3lWxjXe0oSjJcl72KM3aDbGy8zvNtE-sUCpFRvAWt35Bo-DigEKQJJILIlK5ZAWt6dDzMa2gDNS4THztWh7l2qt2ExcKGfddDeMMiVzPONbe9wr2xYaaX_f_tj3_Un5saz_QHjjWKr5gPIVqRunFxqjxMiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
نشریه‌کوپه: باشگاه‌فولام به‌درخواست آلوارو آربلوا سرمربی‌جدید خود؛ باپرداخت 70 میلیون یورو به‌ رئال مادرید گونزالو گارسیا مهاجم جوان کهکشانی ها رو با قراردادی سه ساله به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/26869" target="_blank">📅 12:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26868">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1C-xEwKIcGOCadr_r5wWKttIryor2CDyx_F_PCNB1e-mopaNzQ-Y3WRymA6GYD0-A9Q7FzYwsj6o-s_eEln0wnLYFvJfr60-Q_GNQNvopT0eRPhopRVckGPdRz549CzojZaAsySyi97uhsX7nm_cfxNUR_iwYRbkdP8MkpkdBia24mC3ThgznhhCbtO8Fwo3eiOsM0VFAH7uYYX74dNFh7LWdMo_CgHRbV_HteQsr_yhRR4VIJ3UGnUM91lNwI5HajUJ9BnjAaDRlBPaRi7mTdSiCPKk8MmT5afr_ocwKqe8BiPqNvmH1vmTXxGeXkxr6NYN3PNtqfTp7GWIaSxEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شکیرا خواننده کلمبیایی: جدایی من از جرارد پیکه بهترین تصمیم زندگیم بود. اون با خیانت‌ هاش بارها به من‌ ثابت‌ کرد که لیاقتش رو هم نداره حتی باهاش هم صحبت بشم چه برسه به زندگی کردند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/26868" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26867">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLcR2tJxq4mOEyLGgDcj_hb_MMgQrbQzdqn52nxxA1Ni3G_uxBgJlXpmla61MqtDOLIa3LWvomjRZ_RKcAvChZ9bzqUMdLL1Eur39UtswWKaW74s26fgP80TYfT-cLdHDyRwer1SzYZDrnmbVb47LdopTp0QtX4f-FLWN8EFpeD9R9IgCHtnEIjTBiA0qVA-4H75Y-WLiDL9xySjHa9Eau6W53KpWV1GIgGVJknacTuNRP7qDbquRZOoS5WLyugCPKFzw5jkyaGHD6YHpvmT_lmsQ2yBgyhC-0X5wViXo5cNb_1Hgqisy2Kmx9bGTatQ7jm9N1nDtY2mJxhD7fwV8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیمار داخل یه ویدیو به محله‌ای که توش بزرگ شده‌بود برگشت. یه پسربچه بهش گفت: «من پادشاه این محله‌ام» نیمارم‌گفت: «یه زمانی منم همین‌جا به همین اسم صدام می‌کردند بیا باهم عکس بگیریم.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/26867" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26866">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJHwWzH4qkSPQX4AvKsuo19eKghdv3g4ntJ1qWqFowMlgyJ3ST9GgCuqodUQpVk2jUbe95OUkzNGdfkWbxYSIomK9P5Hjqk3d01he1pZf4VAI-59MFIf7Fmu2VLiQOOT170FPuIbMVZ7jqYKyjKPZCh4LpYMxlm40HXum7r-Rr6A_MvSN3G_skPUrXJwtonJRNOp53hlJUfAU226vaVKqlP9uCkbJJbTXKL3NePtor7leYsse2MerFab5CMgHy-MBqOtV8hr9HEMOwL4pw7CXq9KdusRwRp413PdnMbB0uULl4aANAQvJab9gkuWyoQSlBKGBLaW8xCrjcLplvtZAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
توام میخوای به راحتی از فوتبال و باقی ورزش ها دلاری کسب درآمد کنی؟!
⭕️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
💵
اینجامیتونی‌روزانه درامد داشته‌باشی و سرمایت چندبرابر کنی
🔗
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/26866" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26864">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VWBPoERA5RHWCmZ5KRHLDzEjgAvie0vWTca_FYAjC6bexW8TEF0gL6vb19LpnOCvUaoak8vjM9jiw2aP5m8-gzzcirBF3dMIl-DJs68nKQo7-zd-tuoAn8Pv1OASrZTv08cwQEsb4XGE4zGDIx0VmcNMrFhQ_dPAGMbfecxE_Lxj5yon9NAU-Gcis3G-59LZgrhYWCsm9s_86DdapHrdnAykb172em40fPrX_WPyrpMVRmlyog_5yagCwyj5XcT0E5CC6Vodn5lw0UEBar7eWADo7DpImQ2F8DUOfELAxBBK_T7qEtsRdk9RKpTe2JlMZIDOqaPPfinR5H5qEl03_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NMN3cQF4m3-4YETe41V1cWgskZ4yrNvZleefe3tL1E31olNGYao9I6YhIewYuOrdIKAlrIdG3xtrcheJBRKjnSpAzt2h1JB_gkIi1zqwySL-de-j0Skol-KdFUkZ_nm1rerjXm8kgz1n9Xw4mjMOSKlapVlzi4oFxRlXoLPZfrN9sHEsfZk0O-oRhl2aFXbGp6YsGjBlfNXI5VcobhMgK78rxutHqYhIQMqleVles80Nv5xaIAICD2d3-_V0kmQRsrTleE14Uq-AnQbPiDofx5AQf7cDNtAV1lL5WT_Q3hN9EQt6OqWe7WZbKGGUoWFxIenUCYh3k7dZvKiYaFKDNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رنکینگ بندی جدید فیفا برای تیم‌های ملی و باشگاهی؛ لاروخا و PSG در صدر قرار گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/26864" target="_blank">📅 11:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26863">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpMBGldqEShvZ9vLaXcFOZliyouRRFdi77YgIRuorxgmvn5ca9fixuzZCdWWeuZlpfipN8AsOupjBbOTWSipxzCaRSSR2V8phtFZutnsF7xB_KAMsQ20oIj2rXUXdGnBU6WLIYB1f4h1N__eRp5DSvylUS6CN4MJkA6Bb2Nj9wEhEgU0Skb6emql5_VVDJUIPCH_pW19nhGeZiwmKHZTa-AndajpSdldIw7QTmNrhrREyxqXTE6w-V5YK_9uMPgJLs1oV99NgwulIfR1PhWoXYlkOF6NE9zWZCLFFHh0auwcs3t_HYvFe2xQfYiBjWuQMK-TkDYJ2IRuq0-wHTEV7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سعیدمهری هافبک‌میانی‌سابق‌تراکتور، استقلال و پرسپولیس با مدیریت باشگاه پیکان برای پیوستن به این تیم به توافق رسیده است. رقم قرارداد مهری در پیکان برای دو فصل 25 میلیارد تومان توافق شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/26863" target="_blank">📅 11:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26862">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4UZka2AF3bEJVIseKfllpqgHVgh_mLvOxLk8MbHgZqjpvKKqWcpBzWMScvfOj3JiIYXC0cAlhYRKlAiZ3kYMn4M8uAX0HNuflXf5PBLQi5h_6pVwi9xTsQSg__4olUozkmD00RR0UWSkuq-ITrRAjwAKkiyS3H9F9n-N43V7CDg5K73_IJWTuj2h2f3Mxg14q70vEfq-YaiSOOKyWAH1-7SrX4OoNRHBjCg79ADavEs0y1JGX3q20wcR9Sbm-fgz1chcBlXNXLfQM1ubrZhT9aTc27Owh3RYK-SEoRFYjtwBYb4TRHaRaJ1SdXKqzC0W8MpspzzMeKHhl63Nr37dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عیسی آلکثیر: به خاطر دلخوری از بعضی مدیران و بازیکنان در پرسپولیس، به استقلال رفتم. با خسرو حیدری و ریکاردوساپینتو مستقیما صحبت‌کردم‌ و هر دو هم موافق اومدن من به باشگاه استقلال بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/26862" target="_blank">📅 11:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26861">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5b33a46ab.mp4?token=R_ENGyQ9TAJAbFJQo9-kLWoJepHfPdPv_or1v1Wf3nA3MTx6efxiLs7xqgyy8t9u-mn0UGqNNu-sGWYTt0-6RMtpk30_eEUQhSGCBfIKl_FCrMEc82kcWmtHl3Nlg5dsSrnotVHgO3pLJ92sCUmN_48MA8sPugJ64CZFahDp_v2kQgy_Vz-ybo0hhorQ7eE4T4-k1NTcxmVX1A4bkPZRqkZow1tAXAkCF5dQMyvjeaex_m7StfGmd3CdfPapuNrerVSSC3Kk1fgZXZjnTH8YVnwlgwqhIXbQwFW7gBo95wNFzk_1nrBXLssIoNd0RnNWHnCpIo7mP_JjWdG4_AJPbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5b33a46ab.mp4?token=R_ENGyQ9TAJAbFJQo9-kLWoJepHfPdPv_or1v1Wf3nA3MTx6efxiLs7xqgyy8t9u-mn0UGqNNu-sGWYTt0-6RMtpk30_eEUQhSGCBfIKl_FCrMEc82kcWmtHl3Nlg5dsSrnotVHgO3pLJ92sCUmN_48MA8sPugJ64CZFahDp_v2kQgy_Vz-ybo0hhorQ7eE4T4-k1NTcxmVX1A4bkPZRqkZow1tAXAkCF5dQMyvjeaex_m7StfGmd3CdfPapuNrerVSSC3Kk1fgZXZjnTH8YVnwlgwqhIXbQwFW7gBo95wNFzk_1nrBXLssIoNd0RnNWHnCpIo7mP_JjWdG4_AJPbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/26861" target="_blank">📅 11:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26860">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mir4HqA8BqUqAAaEaDLE4omq_Vsc8aWueg5UE_GH9snTBO4QQp00VfNvY4MpV62XdO03awFw312DF9LfTFr9sFfm6utJ2gFBNIxlqI-pFZkyY_sdPuahyINC3UpE3nIdB8rPS3z9cZhFL8TaTFzi4uyba6B8Q7FMGIrTzyzqpsizy6jOfW4Ai_F9aGPUbUzoXc2K1_XSn6tmAny-1KBF4_hFH5W-GL7UqLkOG5BtBg40r-6JVZE6epxUcwknX7q4rl75aFw941AdhgZRlXz9KU4WifR_GVCZdo-ank-tRn9xSNyX8Eg0rQ8vOky3pXD2uwXGWWou_1Z-Hav-PZ7yaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
باشگاه خیبر خرم‌آباد رقم نهایی رضایت نامه و فروش مهدی‌گودرزی و مسعود محبی دوستاره 22 ساله خود را 150 میلیارد تومان اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/26860" target="_blank">📅 10:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26859">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBJdqzV9UI9PUSFCnEQf3wh9RHkhwJR9YP_j4DOwe1KV2aUhwDrLAUkc5BPydZpVrTruR6dSMRd3mRxXs21ZggRU2YSeGGAFgJMI_FGunmxlbVLtjd8GLdZNtx8QoDJvHEm5e1fYafy0VRkrU92C0cHXN2uvumeJ7UciC5IoKL_qKSrEoMXTThpm9_uJBrc5sqkER30tkkpAgpRfiSpUEcLlBWizGbM71RiTt66H_jlzdfQI_L3iiN7FI9Pm1LZ2TjAEnZW7YOA6PH_s2YJlVYjHiCYi8WuJ-u6yFcrvEocnuu0rPUS-cAmvam11bdm2217H2akedOT4M17_3gDdbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ عثمان اندونگ مدافع‌سنگالی 26 ساله سابق گل گهر از طریق ایجنت ایرانی نزدیک به خود آمادگی‌اش روبرای‌پیوستن‌به پرسپولیس اعلام کرده است. تارتار به‌مدیریت سرخ‌هااعلام‌کرده که قرارداد دنیل گرا رو فسخ کنند و اندونگ رو جایگزین کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/26859" target="_blank">📅 10:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26858">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAsSy1IG2Hj0Q5YJ8GyEUUTaBllSncQdAePH6dXxRPoz0TPRaxdAfm28x9IMUSS7-jbTp2N-uKP7OMMi8eJ3NdvhVpTqiV2FwWt9G6HPkp05X0TW5DyeiBh0uWgefsNPuqcTJEkkDjttk1ypwxE9yVdjkaOaNHo9ZyvpoJG2YH6TROuynLC71FyM0XYHHQ6zq9QS2Jww3YxUZ3isj9iLVSJVZOJPpxHV28O3VLbaCJ86juWLG66Q6eVc38DSU5x44LmCA7wlg1cTOwRvR9iEdrnr2Gn_vN5Im3UALwEUZMJ61M14tH2b33vs7ZZlVtTen5nQggffFkHzLIxkeSk49w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌فابریزیو رومانو؛ باشگاه رئال مادرید 25 میلیون‌یورو به لوانته پرداخت و باعقدقراردادی پنج ساله کارلوس اسپی ستاره تیم لوانته رو جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/26858" target="_blank">📅 10:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26857">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWbnaP1ACiXAKBxe5MaJEFIN0x2PkY-n-ppTlpHXNK34GihwgIFxZOBeV39AWk6kdjsbW_NPGYX8vuhaV_o4fMYVdXicEeUvGdCSFKcXztqGWuTc_2Np6VahfKVQD7u1LOfqbLQn1bzQcTaaEEX8lUKOBplXk6hnO_Za870PrRhMnlLONPj4pYFOMNP5GrGL2Up1PkCRI3yU9gvzGUX9_SwdN6wNJLj2AUiKbJr9btH0uXawHb9Ho6IBUe_H7dH3lv08w1oJF19Cknfx1yPat1GlKEFRRi0Vul5ZfCFthoUMAZxQFLDamcYWrFZXdjJFIHYNWAuBX-XsUHx5klssXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بااعلام‌‌باشگاه‌‌آث‌میلان؛
فرانکو بارسی اسطوره و کاپیتان‌سابق‌روسونری‌صبح‌امروز درسن ۶۶ سالگی درگذشت. این در شرایطی است که در روزهای پیش خبر فوت این اسطوره منتشر و رد شده بود.
📊
بارزسی افسانه‌ ای ۷۱۶ بازی رسمی برای باشگاه میلان انجام‌داد و ۳۳گل و ۲۴پاس‌گل به ثبت رساند. سه قهرمانی لیگ قهرمانان اروپا، شش قهرمانی سری آ، دو جام‌بین‌قاره‌ای،سه سوپرجام‌اروپا و ۴ سوپرجام ایتالیا از افتخارات این اسطوره محسوب می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/26857" target="_blank">📅 09:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26856">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmnGHnr7PbmQ1wVrNn809iH_X2zLXW2LWxEi8wL8nK5_d-2XEA2vNahnyiOl9n-atrauq2IqhjDURjMffwY62TXXpKhCmz26KlP62Ho7V4_qqVKuuy0au0mHcqmZAz1hDj44CXUjUyoGOz-E61LFY7L_cAOwv0n1jK8jdczaSMgzyxYO2xFZPPqdLkXP4GA6gyPRWoMTa3BbgNhKNcnIsw8GKm47-9-msu48IhNRtGWYp3DMXCQ_dVhJJU5mb65x1x0PUphHzMZBzEiBMRKkRficIDqO2mD3beM2tJVZiIVOPV_LzYukWuHadqPIFdtuwLoAlXDPUEVN0LuWi4lB5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ریکاردو ساپینتو سرمربی‌سابق‌استقلال‌که در روز های اخیر با عقد قراردادی به پافوس قبرس پیوست با این باشگاه قهرمان‌جام‌حدفی شد. از معروف ترین بازیکنان این تیم میتوان به داوید لوئیز مدافع سابق چلسی و آرسنال با اون موهای خوشکلش یاد کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26856" target="_blank">📅 01:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26854">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pLbnlz72t8ZjFqZUgCMwjYmEeggfC5xnvGDDXeMVBcdxx3QxZMWR_I8GORrLrfZm7EAm8SBWOOAAqP_9Y3M2fLy7CsHZsOWH2h7BrKK-4qR4i8edGes_7k20ac9Ut1nIwtQ0NuAHlIeMJmrgQS98EbvkFNcSM5To5OCNNXtHJuC_6iHmDXgec5xcAQk8HmUnj6iLImsZvLEcqxqTHwyqZDTELJFn5IPynna9jgoX1AwPpUTd1iNARBPDsANbs76TMlKhQzMByNNCUbBtWhAba9qiZkz_f0j5ADOv_mlIKnI-QSkwVhIFz3CIYbguY-NaqbpiV1NgSDhtTogwQYySbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RpG5N-ZLDcL1B_PR7KwjAT-z4dil1syubaox35gB_s6lkKYofpjHAj1c1GVtIM2Vsav1iAIn79s7hW1up20iB4GQse0SKCMvcSXgnwi1ObrNl5vzDrBDtR7BOo-UQu_g4uJ6OM4fsawrSWAMEN7scdXHkb79Te6OnfywS0ntvp3-5X9H8jeSx-Pde4ZV7ZxeJDZjwh7NvPBrpO3MvoY4mtHoinTXp7QWB_Z3-JLpu8sxsN0kZPNg2vefSzu1swTjFFkdQcZNrYeZEkpKcR81r3c_SNaR--JSgcPXHd_6V0Ues8F356j_RQAXZrXc_VbVYnqocQnKe2lCeKXc2bCweQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌وتاریخ‌برگزاری‌دیدارهای‌ سه‌ هفته ابتدایی فصل جدید رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26854" target="_blank">📅 01:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26853">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBO-_Kwd4Xgzz9gj-f_SbV_bCITtVJuyDps2v4mF58J8gpPxUmAOWsKni0yv_LCFae5WL5XIwVECmSWceRVh3FtfPZ468U0pmhFKHqmuQ4e_OYfMEDWLLCkcC3OWb8zWDaOZxG7_vXlDqOat_fsFQD93oqTtnGHupcGvPti_HwDRVDOCxaqykd8TwfGiDulAfS0tIfl0aNJ4fXwuQzHkmrhALryF2KdH3Lnss3SE01HFJ1jTuEOfUeynPJDzm4EKAQ0oZzY2r-hspihrIefNNADOpY4N_WwMrBrnDkwRNBv434wAU76HrZ5_09pyKoBeG7pTcV6M0pSsv_t1gUfn0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه‌استقلال امروز پیشنهادمالی جدیدی به رامین‌ رضاییان داده‌که 15 میلیارد بالاتر قراردادیه که درنیم‌فصل امضا شده‌است. باشگاه به رضاییان گفته ظرف 48 ساعت آینده پاسخ نهایی خود را بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26853" target="_blank">📅 01:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26852">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiUS8OyBfucTHzgiQRIkm_rZ8mcBxAq4A6t9aEIeEcAFKAbsPIk0wlcSuarMJwIm5PQyIJ2KCBKo7aI9Ur5_-JBPoyLjOPyV4Sx1-BlWmBNRlatkzn59Mwm-zY9nJGYpy2jgTRFix-hekjtMJ0EH7xahxMJnv3SV-jcBpI9yFFVEBmSEwm66eP3qAvlujvJu6wjHz1e1aJ4NLVYGGFNyDzxhzlm6YID9jj2SBxZmCJsisvsThX7gxDipUa7OwhAFLhGRYdio9ZWA5vNF2XxuA0LBLFaAYoIyslCsJbR94hIPmhhYC6fnuvQgw-fGrkHuhlwNYJeKIbGdyoqaSAIVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل…</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26852" target="_blank">📅 01:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26850">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eItsiETGpFimlN2r9aNEVPjGItr59ZaOEJ7cZScfNZ8zerC2H6PERjwdLsdWMRDSMSG1eeiHVpd-By0P2rsIvukCMPxUW82ubMObPEB_8JEtMeMK2V7IXfXb0nX41X-H-2rX9YE3Wuq3JV7k42CpPdc7QJuMoHlMWrEDxT0IsVIzYJ5cOp8xOUeDjx6rd81Z-13KJPvW4trtbYhlfx7ebYfBrtZ9C9Tqywz0yhy0IBZQxX-7ywYRoAlzltxZYzGckY-HU4RlKJjwd24Y-4qOfckuoJ0vQh5SGz4LHEhNO-kruBnKcKLWu02UZpgaKbyp0imr5XrbOQ61_T5XMig2Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی پرسپولیس درتماس با مدیریت باشگاه پرسپولیس‌خواستارجذب عثمان اندونگ مدافع میانی 26 ساله‌باشگاه‌اخمت گروژنی‌روسیه شد. مهدی تارتار از بین ایری و اندونگ یکی رو حتما میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26850" target="_blank">📅 00:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26849">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=aKQXajZAZqCw-7m1wX_a2TCSWQHTlxBlahjpwWrCv-nLSqz35AYBpjVCi1wn85d-ZrwRGx6Lpp1agP2PGwMbJYCGCmUrsUiHihtWq0P4jEgtNYWnZmEPfOL7HZuekMfTWFkCQr7a8E2xFwnkQ1XvPXS6QA5m9NZClQpcsqDH4yFpaNCpn18E0_1xz1YoHL6LTGqf4AhfrsKW_6dDecsUNIi_H4He8pQ-r9BqC8qdkI2fiG6zijWIGqqkDSsddO2EYOLi2b-KbndmWCeZELzwY3SH1IAyfT8qafjTn58YKHWwzlpLcgTHAw2qUZDXlf7ouJhJjc43_CYWW5xpzaHHWV8e_tcJETGGJmHgD6KcAShOJOq-cTxalJz-eNUex9Sh3kADuqpHns1RrPfE7JtpSs-tqwbmKEiGkOqoHDNH0-h94mpYNSbeWuafni0SNGTn5tWAIfedbXrFM2ahaje4lpo_BnL38HbhpkAmqyOo-YDglyH65mf8FEzDoKwtEmnlB7IiIw1CKXQq2oUQmTHqU83ozPm5OjJd2DQL06zuDMq5ub_g-JqJ-RsRZxV2pnwRLJoIwGKldomktp2Mslo8hGaO_aTTI9FyLqxGJzqZVKjxGWzhUIex48aFRnHNL6p5S5kKOjWGbuJVxYC-X0E19whEDwFy51kDWAiQ_O-kV1I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=aKQXajZAZqCw-7m1wX_a2TCSWQHTlxBlahjpwWrCv-nLSqz35AYBpjVCi1wn85d-ZrwRGx6Lpp1agP2PGwMbJYCGCmUrsUiHihtWq0P4jEgtNYWnZmEPfOL7HZuekMfTWFkCQr7a8E2xFwnkQ1XvPXS6QA5m9NZClQpcsqDH4yFpaNCpn18E0_1xz1YoHL6LTGqf4AhfrsKW_6dDecsUNIi_H4He8pQ-r9BqC8qdkI2fiG6zijWIGqqkDSsddO2EYOLi2b-KbndmWCeZELzwY3SH1IAyfT8qafjTn58YKHWwzlpLcgTHAw2qUZDXlf7ouJhJjc43_CYWW5xpzaHHWV8e_tcJETGGJmHgD6KcAShOJOq-cTxalJz-eNUex9Sh3kADuqpHns1RrPfE7JtpSs-tqwbmKEiGkOqoHDNH0-h94mpYNSbeWuafni0SNGTn5tWAIfedbXrFM2ahaje4lpo_BnL38HbhpkAmqyOo-YDglyH65mf8FEzDoKwtEmnlB7IiIw1CKXQq2oUQmTHqU83ozPm5OjJd2DQL06zuDMq5ub_g-JqJ-RsRZxV2pnwRLJoIwGKldomktp2Mslo8hGaO_aTTI9FyLqxGJzqZVKjxGWzhUIex48aFRnHNL6p5S5kKOjWGbuJVxYC-X0E19whEDwFy51kDWAiQ_O-kV1I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل فردوسی‌پور:
🔴
اگه قرار بود که من چاپلوس و دست‌ بوس باشم الان‌صداوسیمابودم‌و نود روداشتم. چراباید دست یه مسئول رو درمقابل‌جمعیت ببوسم؟ چراچنین چیزی روباید باور کنید؟ دست کسی رو نمیبوسم. هجمه عجیبی علیه اومده. همیشه کنار مردم هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26849" target="_blank">📅 00:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26847">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwexBoXhtka_ipKVKopRBrEPwsuEvHAaB9282H-8a3uMD8kujJHZ2TWvSi2t7F1sKHEZop2my_sDgOoRQ9M4bldRrnE2NzOAsyDDeWtGcjZdQNWQa9tUzD3ECzvXQB0OfIJ5ttF_iRExOwvgzrf9OGOIBjbBl6I_ryffMGPR0BrhuEJknmnhFq5ln4iuVWpjqebLsHYHE02ssHKvxoDcEgaDeXGnAPhhhbSiLzzswvj98bnnaxmCDMh2mCNVdI7a4lAOUrG11BVXR3ibAD2QRfpOiZueqeFZRu-fC4KHN7hmN9l4xjwR8EWBXW4dJmbemeUBhmfacSxrbpKh2hUsbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
بازی دوستانه آبی‌اناری‌ ها برابر تیم سابق جود بلینگهام در لیگ برتر انگلیس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26847" target="_blank">📅 00:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26846">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mP4lzvFHn8POlgc-mTJ2_aYetcKeDbgGeY2rsWQ8qJYLZ14tZwkwHnrCzyBcUy5OuynKRBGyZN1yQedGAcCA2OQtmV3UmUoOrzJ8diIy0Ye15jMiUJSNxufdo5BtfBdzgwYTosJ60gLv-DrBYneKzv21IrKkubFuKrAkoccQZFhre_8XMOg7JX1irpagDkkafvIWONwqkirFmbi6s_Era5EYqTTZ7hrAtxSejH8PPdcPIOGKiegW3e73dqj6uWmbvm9IenbypbyaASw5NXXOnyJLPvl49bIVuNb1BJ73vkx9QOK6iApPm6SMGzJwPi2mpld5VQc_Rz2AZFshd6vM3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ کارلوس اسپی مهاجم 21 ساله لوانته بزودی با قراردادی 4 ساله به رئال خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26846" target="_blank">📅 00:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26845">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ND_3VJCLeWdwvl3AJ3h6t9Brwt2euedKH82p-PkY856B6vT8xhz5HKoJodDN2ARNzw9RIVVAHbJ_N2oeZxaRq7p7DMLLWjtRE6iA5WRFKbuXdvJuAKXSpbtT80ph2OP_l9t3V0GC04LxbENQS438vbXeGukMikbFpqeNvRXhP238t-UJ36KYdF5bKm1VOA-NYHKdZ3CY6BQRRBlWHi6lggS5-D8nG4EnX074N4w9sKdFQsH4GFawoS6b1Yq0_eNVc1-BHsUwO4hCfDS4DtAAowmtNFc10hBPrS1Yfc4n8MrQ1icAMeTE5G9gi7xABKgnQ3ch2wD3oqK6fpYkyf8XWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دو گزینه نهایی تیم‌پرسپولیس برای جانشینی میلاد محمدی؛ اولویت مهدی تاتار مدافع جوان گل گهری‌ها شد.
🔴
باشگاه پرسپولیس بعد از توافق شخصی با امیر جعفری مدافع چپ 25 ساله گل گهر سیرجان؛ امروز صبح با ارسال نامه‌ ای به این باشگاه خواستار…</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26845" target="_blank">📅 23:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26844">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npLRAEP0RaCestX3TaO8iPw8VW63FUR1aYVJF1g82E8QPVuxxIQAbBaOHuiGZXd_tzVgSoovA5_OpwYQ32N06BrYkkSVw83U7Lw1TRCcXTNKq9Uqr0jxt4eOdRRzv2Kye1N2bs5dZv3kjMczm8X6Htu8NwmxsKBh1OrlcSoDdJsxdI7PR7uAJfwLEnUKOCmJsIwdeyqtDtqMlYog-VEqZDjB6VzAvdtP3w3XpAnuRT6qiLAVmGv755Adw32-gdt-gyRR1cvV1Ar-WH0DFW75eiZy9HafzNx90Nx9S1d2HNAM7dNuQj1mUuhb-Fn3UyJ3GzZR1-8FGtAD-i-QcCD0ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل…</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26844" target="_blank">📅 23:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26843">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aiHaP1wBYQ0JXHXds86ID2yo9pu_qVGJCHT7RCfVFJ39NkXcSptmwjI0HhaK2UohJleM2AngeCkl6BrT4U7cgkVR9Tk-OmH-T-1ElSdZyTtxETroJ58QyQez86i6K1srRhU7rmxNwlJrNAq48AKVVZxL_xM01wG0MrsB1zT4-ROL-BKTz9uLSeSxw7ZULkqFZXufstqpk1Drtjrr6bmyDgDCUqkQDJNKrPxOlJzc-UCUXCGgJXd9Ij5BhbRCzmM2-d1L5qXYXktxFTJHwQzJtEXsCED5glbl4X37nU-oUtrC4RjNZ94GKv4IM9hyR1tlUD1ov9_GYictYCdi49JSBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی رسانه پرشیانا؛
سعید دقیقی سرمربی جوان سابق پیکان مذاکرات مثبتی با باشگاه‌صنعت‌نفت‌آبادان داشته و احتمال اینکه بزودی قرارداد دو ساله‌ای با این تیم امضا کند زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26843" target="_blank">📅 22:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26841">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPIZ22TyxfKgQiPTy2qGO_o1zp39tv98bZa33wAUS_dWKP4yr9AOJ-ilFHkozSCiaxrw4zqcfE3RloBV696VD8io00G5dASvwLiQ6hT-hStsnGZNLQV9L2B2SxauxxYnviygtm0agvxix2qoSIwv51rCNpDf5_cW4lkbOWhloGUxyfjRiSFU60GWJFfa6Z87QA-xQOCSsixUIn08msim99kjdfsAGmDUbNc-GAMPTU8SnYpufKnL7sLj5Xi202daDWzv_0Zh0glvGnH3c7uWJ14jok0Lrvu354ApK8u8M24dlkKZkE4pMF5OPOC6-wPc8fyT9VOexERGsXi0io2vig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل در یک فصل برای بارسلونا در رده دوم این جدول قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26841" target="_blank">📅 22:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26840">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjupyPt1pcGAlq8iz0Erbv8JwRkE3fAK1G2X4jt1Qho0AZEo8-Bf_NJaJwekmJJ-yrAhvuV8D6WGzJvnbqyQxnxuthu-b0-ji4Z-fKA9PUvclSjRJfWAw9J1mjlUuoh6J2W9Ez5S-l5V2_R1A9Nxld0Xdg7JwtqhpW9SREuyuUM8nBOYyyIQDVBNS3zNN_1gzXO5hII3jAsehGFAb8kVHXhLkZfcAtxHznudRjq_-iOT8uhG34Wm22rMlWrvkm5eWxdnTlL_8Nx7STOjxKUzSR1305PxKH6KOXhk-4CZxtWjhmkBpi9TS1Ti4qIUkkEFFMTbTIJlu9MYy5AE_P95dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
نشریه‌کوپه: باشگاه‌فولام به‌درخواست آلوارو آربلوا سرمربی‌جدید خود؛ باپرداخت 70 میلیون یورو به‌ رئال مادرید گونزالو گارسیا مهاجم جوان کهکشانی ها رو با قراردادی سه ساله به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26840" target="_blank">📅 22:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26839">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHuQ1yS4bVy7Tm1rY7IX71pmbLoNKRTRTL-ZXNPZ8ivbpCuZJmPzYYCS9usqNC6Rqc8UM2zZAZ_YchLlDWvTrAs9-jacxlXPYjlyVmfClfcj5y0XLyXb2CwzMaSn7XYYWfmkd3pGKTPNxUuTNqgMAcp0vdCp4yZi1eQDS23x2Z3m4rvlWextCMyYp8N3VgG8zp6vOqkte2Mlb-1xN7lSDglntsKY4373r370HB-pAEagYJbnrmaokPKmDRyXcpUXlqw1M58RfPPd2h9Yec3CkvC1dr00_FWYjAr40y06IfmJF0miZpTsFYBrfwgVgmDdTD5-yOE_OYjY9Rd4F1AG-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان استونز مدافع میانی تیم منچستر سیتی برای عقدقراردادسه‌ساله با اینترمیلان به توافق نهایی رسید. استونز به‌احتمال‌زیادجانشین باستونی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26839" target="_blank">📅 21:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26838">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4isEYp0s-xZLLlzq2Di7I2THPTywQ-Hb7i9wF45J4TGZOzoeVWSHWi2j3XW8Bc-f5llxw4nSbz5FKxW8gNryA2D4Dv4Et3c701QQ0ucVzmbGNqextyyPY_3V8MjWNu5enulXAPTSaEB1Vj08z0CvkvuveFphgGjoBEXUZPcKG9SYP8wL137q3EkbjbysWZjKKJi0gy_hG2KvVSntn88VHKVGaSWVDUpmXyTNYD0B3RDI7nCB9kjaw8ffGHPkr_7Bddn5E_E8PeJIdnZr78-FsvSaEN68ara5-Pc-jqJX0sApovSAhSmogRYDcuvWdX850MNjry4p3VqlxJuHnedhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن…</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26838" target="_blank">📅 21:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26837">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDUgBM_Q7R3msA2bC4s6pSnH7AMSLQxM0zEj2SR5yp3IqjyKRacI1DuM0S9t2y70uX9eCdUw26S7Z9o8dNuY-POYaoEl3OAvs_XTdtqerSK6VoDhpo95ShrZrIzBo-ykPNGfHgv1n4uSSmySffIlIkFSfXA4LKhmr1Cro-SibI6MiMlCZZKhuKCI8jARWHyerL5yNKGJMnSuJOINgTiFCqyO1a-h_FijRQAdmj6Po72H8WVtQjEKiqelZPuOpqjjw1wHdBH1jf6C_sBwXoNJlwoRiMihyj6SZzCFvIceUK7iEXTFcenBuhmPwuGvA_XnuQYETQWIId-wkGafrWgxPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس آلن‌هلیلوویچ‌هافبک‌کروات سابق بارسا رو به‌ اردوی‌سرخپوشان‌پایتخت در ترکیه دعوت کرده و قراره‌ظرف 48 ساعت آینده هلیلوویچ بعنوان‌بازیکن تستی در اردوی شاگردان مهدی تارتار حاضر شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26837" target="_blank">📅 21:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26836">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhc5VxldOqbK9NCB3XlphwZGwT0_3iYWGHRu9XEjHqsloawgsEYVzfVAc0mq8_9OU4sGxmAiQJIQJew45RPWwTtC79WcPp39TdxKRCEk37lzLryeeXPE2ZxlDMaEMNvGE74byKYQv5dmlnaWl7xKNB2W-9xXiURefsCGwq7yj1oeEqRqtPbm3V7h7A8CJOlSoFuuuSzpKiRGbjyUtzZYrxJb_XCf2A105MAfggKr908ZuJIZxiR2utMYA4DckHkGKH2zCVOWyEcW_riizTWLYEEHHm9AcMmqZl3OG8qG_Xq3ovGILIj6oFRskPLsMpoiVNWpxyC3Z4kWkSbWzujC6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌جدیدترین‌اخبار دریافتی‌رسانه پرشیانا؛ روزبه‌چشمی‌کاپیتان‌اول‌استقلال شب‌گذشته با رامین رضاییان تماس‌گرفته و ازاو خواسته‌دراستقلال بماند.
❌
پ.ن: دربین‌تمام‌آفرهای رضاییان رقم تیم استقلال بااختلاف خیلی‌زیاد از بقیه بیشتره. تاجرنیا گفته رقم مابالاترینه…</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26836" target="_blank">📅 20:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26835">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/391acb06fd.mp4?token=RQW0iNIJgAZofrNUpt9mmbM4ZP3Kle0bXuayo2N7eo-2AYFRGtSsJQ4YtJFjUXMmz0dvqIxH_Xje1egtponiFsTEXPThECnKp-8j7-KRBboiJBFbbKNF45lqv0J2PHJmqIVtEX8bERSQLt6ID5nmH4mKDBws_bWY0AA269s2mFtpMnguv_VkaMN5p44hnO0I4fiyqg6ji_S_-LYv7beWD1cMjSUN_cqec1Sq_Rfy7BXnVWLKfXuBprMSmnaIQZvFtMizLCLSsP8TCKL8EQSPmxjz5GyI0QDUD7QuxskXBjxQ6u6vxLJXxLJkSU03n4RC-K8Ey7P4QcmWr_dqYVo4bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/391acb06fd.mp4?token=RQW0iNIJgAZofrNUpt9mmbM4ZP3Kle0bXuayo2N7eo-2AYFRGtSsJQ4YtJFjUXMmz0dvqIxH_Xje1egtponiFsTEXPThECnKp-8j7-KRBboiJBFbbKNF45lqv0J2PHJmqIVtEX8bERSQLt6ID5nmH4mKDBws_bWY0AA269s2mFtpMnguv_VkaMN5p44hnO0I4fiyqg6ji_S_-LYv7beWD1cMjSUN_cqec1Sq_Rfy7BXnVWLKfXuBprMSmnaIQZvFtMizLCLSsP8TCKL8EQSPmxjz5GyI0QDUD7QuxskXBjxQ6u6vxLJXxLJkSU03n4RC-K8Ey7P4QcmWr_dqYVo4bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
کریستیانو رونالدو:
در باشگاه رئال مادرید اگرموقعیت یا پنالتی خراب میکردم، در اتاقم رو میبستم و توی تاریکی با خودم حرف میزدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26835" target="_blank">📅 20:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26834">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDVV7KRj9WTAoSSSS4eRaFUiCu9dEvdoHzNV4skpOl2_yr0gUSA29R-C-Q3MFfDJ2DwSIRIE7DnM-mQEDcw6_8g_u2olcBInt6ZMp1bR_Iwu6iTqunc0bXUPxe4w3bg6EGivdYfpO6QycFqxc7KDeB01458tKNH4Badzwn5eY5lYBwEroagSCF4BHkfmnC6K73GZEdOmfaeseqZR4G4SXUxd4gZpos74tYk3f1flljjeliiil_mvZuHT8ndS_hJJoOVK1PUxWgrMlsV95NoPCQWqODyhECybBv8uFaUQ5WPH_I2xuAfupNRKpH8-vLNur-GFhh84qU8ijGFRQ2soTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب‌تیم‌پرسپولیس برای دیدار دوستانه امروز مقابل آلانیا اسپور با حضور بازیکنان جدید این تیم؛ مسابقه دو تیم از ساعت 17:30 شروع شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26834" target="_blank">📅 19:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26833">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpMNAtD2ouF-ZbOkNUXMyMvr0ALXCj3vjyapiLO5DA27HZHRoAsxFF4guHY8haC2RV8odRovYazOMZPHcJMJRksCkw3iIRFUcUTmFbcdOQAWagknUxZA23XSLta7J24Tfqao2wyIqYS6UmcI8UAspcc5mCtjo1Move-q1fwTOfrU_flMn4LpdvXAsOUwulzLnj4s2EYOFODzPsmroM7SR9Uopu8JWzH6ae6TgJHzwLdo3NUUqgvW7IKoji0N4z7aZK8GZd2QFm9pFJaw7DxyhLXwO-1LOaflxJWieT-hmtIL9iLqi18YyB-wo2Fbxvv3O_aZU8a57ElPxPciNe1CZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌شنیده‌های‌رسانه‌پرشیانا؛محمد رجائیان مدیرعامل‌سابق‌آلومینیوم‌اراک یکی دیگر از گزینه‌های علی تاجرنیا و هلدینگ خلیج فارس برای مدیر عاملی باشگاه استقلال به شمار می‌ آید. علی فتح الله زاده، سعید آذری و محمد رجائیان سه گزینه فعلی هلدینگ برای سمت مدیرعاملی…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26833" target="_blank">📅 19:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26832">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hob74vXC-i39Nw7LyIICCbRQtaJSbF7mEb1pBQs1CWAcyA_v0qh7rV6c9J70BUFiqLhQ1rhYYNTqUUPkUQleFPQ4TLHGX5HOUiqFrAKJnbGpUiZzubHr8eDR1GWBmL7Iagw6el7acC2G3-UYF8tvO48DkVCgFud6ZSUv-HDKCKDGl5p4li8aofKRqAi-mafsDaXIFX9_DpBQ1W6WLfk2BpwnKfgXbxQIO5u08OmcXUdwREI85l4s7UPaSRgqGnlgjnQH2o3-9P_2rHKrZ2tjMeyb47FK_z-tXwyGR4NTvXe5E1HrGYsVEdFzf1Zhy2ERX1FbyniekQwKNVj_getffA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مالک باشگاه خیبر خرم آباد؛ پیوستن مسعود محبی مدافع‌میانی22ساله این تیم به باشگاه روسی منتفی شده‌است و بزودی به تمرینات خیبر باز خواهد گشت. رضایت نامه محبی 70 میلیارد تومانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26832" target="_blank">📅 18:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26831">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2c2e717da.mp4?token=IyuXvm0zCR09CuUXNnPtL6G7TRvFs3Pg5o3tycGLrmqKMQxyZSL1yVIm43REzE7LpnCv_Zk2OGYGRI4M0YtXAE3-mfzalULCnNsBV7ezGtkvwMZh8FhTkmy5SqFp5bWVyPV7kqV4CQXZ90cLy69JSUHYH8U-GraPTm31wbMeNNsw6ACV3fL-LAZmeoUB0lDiBYWCnEIOLE-PFqJIiPZ9D54QEmGNgWv7lOnoQCp9LZ-6TDfaCD6C6pyCMUfYUT1Z_qSgkPGqXDrxcS4J9nG0wdzjtnp72rQPcF7CTi7Uy3BjEG7qRMvBtDpMPnqIn6w-JFDTP14HTxphKur7ff3nBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2c2e717da.mp4?token=IyuXvm0zCR09CuUXNnPtL6G7TRvFs3Pg5o3tycGLrmqKMQxyZSL1yVIm43REzE7LpnCv_Zk2OGYGRI4M0YtXAE3-mfzalULCnNsBV7ezGtkvwMZh8FhTkmy5SqFp5bWVyPV7kqV4CQXZ90cLy69JSUHYH8U-GraPTm31wbMeNNsw6ACV3fL-LAZmeoUB0lDiBYWCnEIOLE-PFqJIiPZ9D54QEmGNgWv7lOnoQCp9LZ-6TDfaCD6C6pyCMUfYUT1Z_qSgkPGqXDrxcS4J9nG0wdzjtnp72rQPcF7CTi7Uy3BjEG7qRMvBtDpMPnqIn6w-JFDTP14HTxphKur7ff3nBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
نصحیت‌جالب‌کریس‌رونالدواسطوره پرتغالی فوتبال جهان به کیلیان امباپه ستاره رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26831" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26830">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdCMstrtvobFUN629uK7ZO2B7Dh0LQULVWZLk0M5PpdSBRlS_XYSKzQ5GFCJJ-7dqGh3JntQbMmpyY5OHE4GztsN47AObra4pgISRTGkZE1JjUZL9ElziGwpFZKmtGipRGJkE-ETIglDhdBMCY7efs7IUbZAFXwsAaDmHG_o4j4CQDEmB3K9HEzc5dneSQqS0-VkosCe1ulM7_nSPwJF-ibv6TE_VJzwJkbXAC6eUwHeDqv8YLLk2N-_g_jpOErZr1zZMH_agnGkRYTMiEWbv5Xp6jGOutV_NzPrWSpGmfR3T5-ZpOo_zNmXVYgYkikj6NK9BBP3dUH23SWDcT_lew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
کادناسر: تمام‌توافقات‌بین‌دوباشگاه منچستر سیتی و رئال مادرید انجام شده و باشگاه اسپانیایی تاساعات آینده پوستر رودری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26830" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26828">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQ4l-fF-tXJcsjWP8siKXUAfyCX3MSws1_qmKDfQ0pJxKYb0bF8KZ80kIybFnFUbwWtcISSwfUvJgGm76CaryTEafAfpDguubYdXjcwvGGpGvnKWRff4sZoWYmJHOxgDoy_F6E-O_QxhZurgD-pheSkwlnizUexDpD75MYWbeFspHLQ_R5QYZbl0-8vfVbxNqsaYGt3CdipPyXO0PSHYEwJtfOZztl4TwbSe7S1xJtWjbwoJaKE2dlydTvnU0kmINx4gB01ACWJObk22_f9-2h3OkGbQvELFlX4N0-YfkvlxEasQutHFiOdZBMjZ4q8huVssly1P5c_ohmYXgluv4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مصاحبه‌احساسی همسر انزو فرناندز ستاره چلسی:
تو 16 سالگی باانزو آشنا شدم و بعد یکی دو سال قرارگذاشتن باهمو شروع کردیم، وقتی که دیگه باهم بودیم.تویه‌خونه کوچیک که ایجنتش کرایه مارو میداد زندگی می‌کردیم؛ وقتی دخترمون به دنیا اومد ماهنوز اونقدردرآمد نداشتیم و براش‌ لباس‌های دست دوم میخریدیم صبحامیرفتیم‌ایستگاه اتوبوس و اون میرفت تمرینش منم گاهی وقتا پیاده تا سرکار خودم میرفتم. ماخیلی‌تو اون‌دوران سختی کشیدیم و گاهی وقتاغذاواسه‌خوردن کم‌می‌آوردیم ولی تلاش هممون بود که به اینجا رسیدیم‌. روزی که انزو خواست مارو ترک کنه بهش گفتم به یاد بیار چقدر سختی کشیدیم باهم الان‌که‌وضعمون خوب شدع زندگیمون رو خراب نکن که خوشبختانه‌خرابش‌نکرد و باهم‌زندگی میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26828" target="_blank">📅 18:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26827">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Et266uVcPlLXQsy7gG7JWOmA2MahU6WhfDEIfn6Jvf95suE9lgkyKsax7Uqdh5mKkCLgjx8AUCosxJ87yr6vj4LUaajbPD2xkOmrE1xry5i3n5W8275oDovZB0a_IyzRbwTup78lO2BL2PH3dhE1tRolNMuAoSIbb4aQMAtyBOz50Oxt8oxUw9Ev2BzVuJsTjQltOPQp8rl2uuPiDGhQWB4Id5-UBneSoA8yotn3GRIbn0uicEPVp0W7mShr0ygHrZAIuEOcFy_qW0UCSg_6vYnY2cW8D1uSB9bf2WD3pVx3DH7ikDPcNovUMLTQeHNEic7kZJLBibGG_tuI-z9R5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب‌تیم‌پرسپولیس برای دیدار دوستانه امروز مقابل آلانیا اسپور با حضور بازیکنان جدید این تیم؛ مسابقه دو تیم از ساعت 17:30 شروع شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26827" target="_blank">📅 17:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26826">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/337c4609b0.mp4?token=jiXtFLeT7qHlSbJCEdeT_WSXujcUMVzeEXqGIBPrLYXsRdGFTyDf95FUBKYGJHBaR611IYx9nLak_dd7i3HPQlStwJsFuG2C1NYlchCZ6dSHFJcHSzs11y-2xNQ2IFY_-0bsp8lH9O-0ENfPGQ7LIPSgqMh0-blta0V_gRlVGbCr1hOP-KQnPaI3XbWgJzT9if8EhkQHr6wGNpvyAnLm--qqS4nRm0bgzj0K5d8_coCapS4lB0eqJKhUMsiPpC_nisVU8LyUAvrbsneN_u7gEBp9FGT6rwUpUEZHlGU41h3DIgWkaH1FePebQdToPw2z3U_EQUguYBLiZIQTsTPVdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/337c4609b0.mp4?token=jiXtFLeT7qHlSbJCEdeT_WSXujcUMVzeEXqGIBPrLYXsRdGFTyDf95FUBKYGJHBaR611IYx9nLak_dd7i3HPQlStwJsFuG2C1NYlchCZ6dSHFJcHSzs11y-2xNQ2IFY_-0bsp8lH9O-0ENfPGQ7LIPSgqMh0-blta0V_gRlVGbCr1hOP-KQnPaI3XbWgJzT9if8EhkQHr6wGNpvyAnLm--qqS4nRm0bgzj0K5d8_coCapS4lB0eqJKhUMsiPpC_nisVU8LyUAvrbsneN_u7gEBp9FGT6rwUpUEZHlGU41h3DIgWkaH1FePebQdToPw2z3U_EQUguYBLiZIQTsTPVdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های حامد حدادی اسطوره‌بسکتبال ایران درباره علی آقا دایی بهترین ورزشکار تاریخ ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26826" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26825">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6K5jY5yPz2pHYqGoPeA7i7SyWR0gNPfEncuMptzGdBSRURbV77_0NYbMBjhlov0T9JOCCiEM0tNsvwzQ-FfiNClD_utXPryzfXE2vCUPjjmgs7qrFVzLPKMGikcTTPepjQP-Neh8dVwChNbORTYAIPqNmtRLLITJWIUwxdqBoXG-Kj53dXN0kzpkJ21F3p1vwEUOnJf3wTtuknpjrpqwfy6_KOBdp-JKXMz5Z9LbPRKrH3KjPYJkUMFp4ZGMfm0yLItoq7hrRQqZDQtl0ESZCplgkkMmQsTRIn2DM2jccjvv1S_rfzOTqzmRBQfTnrLlRNJLfsXatJMCzx_Nyz9Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26825" target="_blank">📅 16:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26824">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f949cdb55.mp4?token=dfLycQsooqSWbchhVMa63s3PVlhr9JTmuD3RzifENGaZZPKqR1Mk0BOlfXg2cJobH0-Q8AS6DeC1sGbkpPPulMVKFdYhU3WdkpOE0H-Jow3DOD7bLH5HgHp5ViSznuaCsOpT4ea_1CbFFAgFy6EmpSEHJVRPGfpy807SfBnHsOd-ADskwLIGvEEFgDFNonKBc5llz4nmXJe5-zP2WH0763Jcnz6kSAg_Ri8tqkMVL34wf5owJJbILdPA2tL00EB4BJIpk15tHXa2KuSz8h2FRM2kKdkYaBGXLVK2N3VuJJFEAFt6uj4Qxbb5z4iDuQcWJv2_bYXxM2GtZb_uvu0mPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f949cdb55.mp4?token=dfLycQsooqSWbchhVMa63s3PVlhr9JTmuD3RzifENGaZZPKqR1Mk0BOlfXg2cJobH0-Q8AS6DeC1sGbkpPPulMVKFdYhU3WdkpOE0H-Jow3DOD7bLH5HgHp5ViSznuaCsOpT4ea_1CbFFAgFy6EmpSEHJVRPGfpy807SfBnHsOd-ADskwLIGvEEFgDFNonKBc5llz4nmXJe5-zP2WH0763Jcnz6kSAg_Ri8tqkMVL34wf5owJJbILdPA2tL00EB4BJIpk15tHXa2KuSz8h2FRM2kKdkYaBGXLVK2N3VuJJFEAFt6uj4Qxbb5z4iDuQcWJv2_bYXxM2GtZb_uvu0mPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نیوشا ضیغمی، علی دایی، احمدرضا عابدزاده، علی پروین،نفیسه‌روشن‌وصدف اسپهبدی درحاشیه مراسم ختم زنده یاد اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26824" target="_blank">📅 16:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26823">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NthAQXnWlhNET1Y62ce4hVm1lHlUYMUoz6ONd-JuAv9CoTEQ9OCVBt6n9AShtpwatMxCnUTua3ep9L1ctc1jFf9vFMn2FFrTD3dOY40os_034nHxLtW9KcmBMaMlynmclbHPdYwnrQYIRkgIvNYji0dyYIndc5-EQRU4UBOOG5OQmoiRjZDodIrmT36bYxyvzqE4UmbtxwyVQWrxXEw5e33uH7-xzaXqKnp_fO69omVbk4trlfkUlCkfSBDNYQHWpJt5J-LGRtHYqj-Fj_GaWCImkJa1MbaJN1Cf35RZDpdkhdZjwhyR_BJPrggoZx7tKc7ckmcRS-wKjdYgkxTb6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدئوی جدید یامال و دوست دخترش؛ یامال: اگه یه دختر جذاب‌تر و خوشگل‌تر از این پیدا کردید من ابروهامو میزنم. پارتنر من از همه خوشکل تره:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26823" target="_blank">📅 16:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26822">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrqRPp0e373MiI_qKgMSCoNY760nCXPsM8XD5shTGhCFyp6sek5D9ZQdQFKkY1IkBavQqUBO1yrN3hCjlXmuKhrLnvUc3HJPBKpGAfvCxVT-sDjWr7ZbONAW5JfvYavr7n8rTpfDtAZqY-Cx4n4mJMK91v0wL89o6s86oTzXZz3Anuvx7v3aWFENk0KdzR0RlOvIR8MNB7cPej11ux2-mzgdHnhvCq5Df8_AxZ_hK8lAO2zfemGkphP2rm6-5Q-9YxR7OI0CtPRLHbgyaYkg-75M1PoeCop6_AGR-NtGvXACRZY1ZZpPC5pRaOss7oMZbMVl9AaRYGO-OCrFO5W-2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26822" target="_blank">📅 16:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26821">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1d53ae06d.mp4?token=UYyFdOJFVGY8ad4tmhtwK_VIGsPyVqJKaH5KjEFCUjzFOtGCM31uXXTMDorHhkYd2tu0VmAq8SrJBtdk9072a7lbVD3z1JBOJDIuvR7ZcX4zkMUlz2tQKIMYJAWQK1HMJZfdijj_l-SbLP_n3M9o9Iz6CQy5RLjHwWruC948NZGoHoo0KcakQ-dAacrjvZ9vaFFFYuX_EF0mZ8xLmhkKPZI7aq_LSGhPKDWvN2EU1-hJfy3uWBEmSD4dQAihLvCNvNCHNLPw1PZFxdNST6PPn1-57TSToMh1wwyc01dm9Hg8VB3ZoTAD1aI_v7cdLVbTw0v3jhkwWGJJT_6Wmu8EI3KpGOnaEzKhFeZDTmO3VTgQfqKwiF1gPSnsWPxxEOO0ZqsYqiQjibIjrP1v3gzHA0uVQbfTdO5CJuqpRdwa28LqeA29CGwSnaKizI0hhgq0B52end2VawK1h2rqTPw-67ChgHreIIWjIHShMrtbQ-n8_AHCbcNj5jW9gpinlnKTVdE5_z5szwv3zRq_WaiZ4wYVu3D-yoRsF9aUCwuMZ-5_df4wqkZNFjv9wNNuSI71qcLtwAIs0K7gWMq-bz2CAjY5PoeGaFZN9oSNBfVYKej_xOsomgnMRNpPBLIKr6TOQzy168iANQplOnAL-S0KuaLukP_UG-0qzq04QQ-ZdQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1d53ae06d.mp4?token=UYyFdOJFVGY8ad4tmhtwK_VIGsPyVqJKaH5KjEFCUjzFOtGCM31uXXTMDorHhkYd2tu0VmAq8SrJBtdk9072a7lbVD3z1JBOJDIuvR7ZcX4zkMUlz2tQKIMYJAWQK1HMJZfdijj_l-SbLP_n3M9o9Iz6CQy5RLjHwWruC948NZGoHoo0KcakQ-dAacrjvZ9vaFFFYuX_EF0mZ8xLmhkKPZI7aq_LSGhPKDWvN2EU1-hJfy3uWBEmSD4dQAihLvCNvNCHNLPw1PZFxdNST6PPn1-57TSToMh1wwyc01dm9Hg8VB3ZoTAD1aI_v7cdLVbTw0v3jhkwWGJJT_6Wmu8EI3KpGOnaEzKhFeZDTmO3VTgQfqKwiF1gPSnsWPxxEOO0ZqsYqiQjibIjrP1v3gzHA0uVQbfTdO5CJuqpRdwa28LqeA29CGwSnaKizI0hhgq0B52end2VawK1h2rqTPw-67ChgHreIIWjIHShMrtbQ-n8_AHCbcNj5jW9gpinlnKTVdE5_z5szwv3zRq_WaiZ4wYVu3D-yoRsF9aUCwuMZ-5_df4wqkZNFjv9wNNuSI71qcLtwAIs0K7gWMq-bz2CAjY5PoeGaFZN9oSNBfVYKej_xOsomgnMRNpPBLIKr6TOQzy168iANQplOnAL-S0KuaLukP_UG-0qzq04QQ-ZdQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی نوستالژی از درخشش فوق العاده ایسکو ستاره تیم ملی اسپانیا در فصل 2012/13 با پیراهن مالاگا که باعث شد رئال مادرید او رو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26821" target="_blank">📅 15:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26820">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2998bd2af.mp4?token=k_c40a99CnUIQ31-6SBQ_52uxDOUwmMNuefGGd4W0D614zBJ8-8haoY2PY3FK5MPcUkwghcpc3mPNdTnnVwgGTeIHJu05M6aGOqn-6JqVxC08uLuHs0-F_U6_--HI_D9dr6rSTI71zjmGAL4odf9s3h-6jx9_q4u7ZgLgAOWnC-0pv9Qq3O6UubP23xQW3N5f-8xWLcW38MuGhMQCidctjJSkBsKvs9DEedCa75djfXoomzf8IvzQ4iw_WXQMhmJQcowAdwkfNSiZdxiQD38nnxD6Nyo5yIV0oBzk7mCb3W5OKR_N-GJA1G2a_75xanZfaNwvnqxSzAVvFv2qR96gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2998bd2af.mp4?token=k_c40a99CnUIQ31-6SBQ_52uxDOUwmMNuefGGd4W0D614zBJ8-8haoY2PY3FK5MPcUkwghcpc3mPNdTnnVwgGTeIHJu05M6aGOqn-6JqVxC08uLuHs0-F_U6_--HI_D9dr6rSTI71zjmGAL4odf9s3h-6jx9_q4u7ZgLgAOWnC-0pv9Qq3O6UubP23xQW3N5f-8xWLcW38MuGhMQCidctjJSkBsKvs9DEedCa75djfXoomzf8IvzQ4iw_WXQMhmJQcowAdwkfNSiZdxiQD38nnxD6Nyo5yIV0oBzk7mCb3W5OKR_N-GJA1G2a_75xanZfaNwvnqxSzAVvFv2qR96gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارگردانیکه‌سال‌هابهمون‌رکب زد؛
ویدیویی که از گواردیولا درمجازی‌وایرال شده بود، طوری تدوین شده‌بود که انگاراوروی‌نیمکت برای یک صندلی خالی در حال توضیح دادن تاکتیک‌هاست و همین موضوع سوژه کاربران شد. اما تصاویر کامل نشان داد ماجرا کاملاً متفاوت بوده؛ پپ در واقع مشغول صحبت با اعضای کادر فنی تیم خود بوده و کات دوربین باعث شده چنین برداشت اشتباهی شکل بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26820" target="_blank">📅 15:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26819">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fr_WW1B2xifr7E85SjFS8fXozYFULd2aXQXOgCQp6UhY8u5f8sOlXXPaznVBxN4v26m9f5uE_Z-OY3E1y-phFmFI_I4kTg4L9ImVn0imwvxo6MwWek-k5Rx_FJAU9lqV4Nu0Yryzd0W0FA2W99HPsStN2UNdREhrVCW1_MMKtVQ8I6cLQKh05DaI3Wh6CFjfLqPMtMnh7CDUwLW9gN8afvyAoXtXdDaIo31bcOPWV20h4GL6aeN_NFUfTKtrkwLfmGJ6urE2YAjvhL8A13n_i644mc7x6eRiwHYfhupYX2C2QokJzLlqtF503Cxop5AuOeHxsjJMfUQwZd_rPbXOPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26819" target="_blank">📅 15:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26818">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzHt6hAmKKzatLdJFhJx39MLMEKaX29jV45u0_N1BEB_Oof1E89eh1WFVt1--9_Y8649Fk9E0qxwi9NlCYIzpO8f6At90prND6ICwa-ReLwPlAZdj1DBEDR-1ZQeuA0Tmhfjx0cSLQi-U3CVy_0VZRHA7jWxYI3zMyvMutNbD77sAzfIJ8-cN5aWKXPoJatyKQHJg0fBpTy4E-hw0VePilKn_KiYGGUcRlWlz5hN-yInVEJh_En_u7N3d6bjnNbmrG7_XJHKgyVYgGQyBhTYKBX3uPybhWf6rqfTDiUin8rqs9UjGII7mixiWRBUcwGgw7vy0B0xnbQ5M5ZraiEciQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26818" target="_blank">📅 14:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26817">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3X7ddtz1ZPjBX7gsCkNZ0Y5GgItWxzDHWppkvwU8ZyneQx1lX78TexwEBfhG2kjBf1aAk2YD1Zpezh_yDfiIGmujDUkutYjR1YlgoG6ead66z3yruGu72xYPCFvxx0oLJsQBmnvYGXXM2Vsg5aEt4MONGXFZ9MUn8UYtwPoCFWIf5clBau0Im0G3vYs1LSnZHqcA057nkMVXAhC2Lx21FlUNkJDZ71jX2oTdpfDMBdql6SrXqagET9wfQo53KGLwFpvsaKyCwtCohlgSZnvyKgIFyYd8f6OunNB5bph6Xhd1HqtYFdjZnfHaYU8YiIEappbPrgvqw6RTIPJFSkMgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه نفر راموس و پارادس روبه‌مبارزه دعوت کرده راموس انگار بدش نیومده و پست رو لایک کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26817" target="_blank">📅 14:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26816">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hirk3V-vYCczR_LPzVpVageR2Cu7fRtp6-fkDfJfOowi8lYGLdxy2ULW8oDwoopVerJ5x712tChfx9Ll0XcCBFZT2iivLCCJqpQszvUI5UnYqeVx9-l32VHHq4PrhDNzYJP4nKjnr26OQxFsi6a3dWuuPOrKG_HxeZ9RMR0TnXTXSYWvtrLT_HiIiGiKDUbDwjWbmGoBlpejQ4McthmvB59xkIgWXM_8akbS7pyumnQO1RunbaaPS1K__6BVb7VNPrEaQ6cNsK5sp0Bl71wHK3KXy79N-AgEn9P6uTgxI5cpFC2x5KnLZdL41Mcfu9WmefA23E4TlytL0xalw_SFKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بریز بپاش‌های چلسی طبق معمول ادامه داره؛ بعداز جذب مورگان راجرز بارقم 137 میلیون یورو؛ حالا سران چلسی باپرداخت 60 میلیون‌یورو با عقد قراردادی‌تاسال2032 ماکسنس لاکروا مدافع میانی 26ساله باشگاه کریستال پالاس رو خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26816" target="_blank">📅 13:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26815">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkwKej9KviQbaOyt_5NFCM4lqYFCn864dkSHfhC2Wa7Z3aSI9gAmAuoRFd2EZzUbi3mBCr1DfT2AJz8EyvmJxuE-ygJqoCE6ftyfUllR-8_GNLrQ_t3Walv3st8l78B_SIgoDa8c1DqUscaj4CigXYMW6hhVD-b2Y1KCvA2OFFu1PRPPcpx5sAa3w0b7Wbp_xM_U6Siwp_1mHRX3VKgq3QFxeEWjpvWdrIzH8cgeqAvHQXPQ2QnKg2Z_DnoSR3L8L2eATMLF7yDJ7SjQLYIbDv9_XoEf0IHOsqjQGRa3b-HpOuqCrorMXC7dROfhHcYon_7ZmK_Pg93jbb_yugbKOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛روزبه‌چشمی‌کاپیتان‌استقلال ساعتی قبل قرارداد خود را به‌مدت‌یک فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26815" target="_blank">📅 13:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26814">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URo-BnEVUXqfA5ebqCiNlFds5M4wN0Z-FMP7cZv-fIFCBvrvmOWa212cT0ff1l5rEqAsUVN4_nVX6OClw0hSJAgQOuq1pu03fiYBn-V3RV3ffEKaHAu9kM4wnkf793-1m2m2la8gMLVNMkyKP_osNR553zlxFpVIrwImM9xfgQEp972tpnj0ykIadBpx1X4QASb1ub8V398zbulCMsfH_fMUCSWsqN2RiQC_LwhqtoqrKQGnvCUbEM10zR6IaaExWonHdMH3kx637Gqk9H7v3Uqnw8ifivADXwmv6tOFUMQA8tQFQvw8HFdhWwuNKLavJtGFXcQ-qiiN0h6JEBrY6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه اوضاع کشور آروم باشه دیدارهای هفته اول لیگ برتر روزهای 23 و 24 مرداد برگزار میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26814" target="_blank">📅 13:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26813">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rU0l8p7wom3zZwIlL8dCx2NFlswWoBt_dLe9ohOs3oY8NOq-jExk1YsShXrAUgO0d1_jip0nJ59GKr9PQZKw03OJ4jUoLWtBEPvo0wK-Vbnuth_IG8fcuEC7ljnmkqpUHqG792hTLz6KQBSWQ8EimIKsPBMTy9oS8Ei_PZSu4xkYKeF3LhmKTW7W7bBssS5stC9K7KPfCt3R8bMr6aqJhoMPRh3a1DvDhARk1-NHnDFg1b0cRGYBSdXdxD_Y_RA1OgWb0oX-HhekW_adk1YVt2cz8ewHEhiW4Qsc5izaIGNwosxVTfyqxf-Dp2cM7wFAawmoJkIdJgP_jGl1KPfCYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ آلوارو آربلوا سرمربی‌جوان فصل گذشته رئال مادرید با عقدقراردادی سه ساله بعنوان سرمربی جدید فولام انتخاب شد و در فصل جدید لیگ جزیره شاهد تقابل جذب او و ژابی الونسو خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26813" target="_blank">📅 13:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26812">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkOfXLhbPiVqaUJsYsVEIRANOQHGMezytNiGCswzuW5C3UxxG09TlNs88tc_KmEu_yauKsb-Fbq3C5IwMd-47Z32DPO3PV3oREhPOQPZPLR1K42QhGtbT4Yd9a75RMbA1nFbQ4TMLkg8SgPt4N_F3qbnQXyN74MKBf7ETWonNtLMIdmjEUW5cM5my55d8d4QHfY8UssqhROrH3iEGf9jFJBuNNbKPbgwMEME6V7RO6M3u8noSfaqWiOirm5T9VKs0NBR_dqITYpvZ_dvwItwRY_QoqMMZXn96B41ujaKOEWQ17LARppQJakFJ-dXPG8AQBn0vULkxXfzhPjyqMpsfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
"بچه"بالاخره‌کارخودش‌روکرد؛ باشگاه پیکان از عقد قرارداد با جوادنکونام منصرف‌شد و قرارداد یک ساله باساکت‌الهامی سرمربی سابق تراکتور و نساجی امضا کردند. نکونام دو شب پیش با باشگاه پیکان به توافق کامل رسید اما تماس های محمود رضا بابایی باعث شد که قید قرار داد…</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26812" target="_blank">📅 12:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26810">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_ttjJs7fSwUleigsVKct-w2IpjLIGImqqsociKISqRtUJO9OQlLLCNwhxTmNkg68US3TyApn52nSWv6h6EyM6O7KfX0HQ4gULBFz05QJszzvEegRgkRiQoS8F58TBskmnn53ci4eKgyxZO_hR_OMF-AHgwGDU3N9gjoLgkifp4mi0SVjyj1ORNEZWC2ytXUeZOi4zK5XS5c24L16NU9d6lhBsTEwjSEv0ZFlorRjR-O6WJQ-exwyiObAV28ILITV3K1SnuqRhPArQoJH7q7-MMR0JKKtI09iM8085ey57MIEMZ1NltlO4wR8aB6UrUpKuP4GsvelG9QnsxQTRvhbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقای‌اولیسه‌بازیکن‌بایرن‌مونیخ‌هستن در تعطیلات که ویدیویی ازش وایرال شده؛ به قول خودش اگه رسانه میداشت حسابی دهنشو سرویس میکردند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26810" target="_blank">📅 12:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26809">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P01ZCwwiKVL-Houm6nwKZPH1jAAh6Sepkcn3EvoDXZc5dp6ykbZulOxeH7_ljZ0-5M-FCxgZ7cc76ynSslZlgpbvUnwyfMZS7DKZemFNHx-jo3vNlqtKvLOwFL7HuUy2WQcwIkU0XFAytSEkGb0OmzbMimsOysMlfW-DuvaTOG024lO2hF7p0q9d3B-8V3Tkge6LslTlpwyN3EXdEknHDr2KqndQu01XbIhEck-gpaHzUmrnu9a79mHyNXWoGss1Bosg0B53xoqfnagXDkbjJkRkxoYlPHdVogLOVWIO5qbzC55RaMTpQwY6YC6cC40v5_TcBklP64nTnGez9vw1Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مسعود عبدی مالک‌باشگاه خیبرخرم‌آباد: باشگاه پرسپولیس سه‌بار برای‌جذب مسعود محبی به باشگاه مانامه‌زد و مذاکرات‌خیلی‌خوبی هم داشتیم اما خودِ بازیکن علاقه‌داشت‌لژیونرشود و ماههم به تصمیمش احترام گذاشتیم. محبی راهی روسیه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26809" target="_blank">📅 12:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26808">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVLh9Z9BFE3zOLmA-yJsXtnmtKQgnm_g-UGphxRLpZl5nQ0kEK_Gh3jt6ur-UjSi6e0csp9AfAsVJEE3xTXiTh4UMEeVw1jldHnMKCLfQ5xvZlECz48YGnnfBJaw4K6IG0CMeLOzwVWc-sJ5dovl-yERe1DoNhmvJqZQlR-U2m90RgupRBhcNEwgGWj88M-GRrOY__HBCCKF93adPzsi_RnrrqxCX5qn-04v6L63G7UR8jK5cv71gVChIHxXzBBLmr5diN-lcHbgqeB5irytwEVtJXLfGwVYwgmvki9CtXZwwMWSGd0kpqEcnN2ZyOmKExyT6XhTR6X647fcvpSwsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇲🇦
سانتی‌آئونا:
ایوب بوعدی ستاره‌مراکشی لیل درآستانه‌عقدقرارداد پنج ساله با منچستر سیتی قرار دارد. توافقات بین دو باشگاه در حال نهایی شدنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26808" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26807">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a69d4793.mp4?token=qOes80bWozsonMioJfr_VGsyh8GI21oTF5rOh-5Sq--QIav9aNY1QKrNIOzOPXemoXvtoT5M2544_Nd9kCLo0MiXMjrErtvWlFQcr4Fld3wfqu7YMyoB2l8JLlnJR9dvWF8dye2AZkIpxQD9FrWHI65X7zY2nBtkyJ-Zr3qeT9Vm7kA5svFjj6cOzXY_1KDp9XTiiLaTCRWPN-A6vbEwzKYquVq0WOFCwwuu2VayydAVyJl0M3fVSXrcMe5WZDRZZaQrt2yl5PeKiOxjOmoJPvoJT-7-bj3SNIm80j5TeasHTP27wK1KDkqqQL2fxTFx7xmknHQXUEA6T0cgG3qZ4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a69d4793.mp4?token=qOes80bWozsonMioJfr_VGsyh8GI21oTF5rOh-5Sq--QIav9aNY1QKrNIOzOPXemoXvtoT5M2544_Nd9kCLo0MiXMjrErtvWlFQcr4Fld3wfqu7YMyoB2l8JLlnJR9dvWF8dye2AZkIpxQD9FrWHI65X7zY2nBtkyJ-Zr3qeT9Vm7kA5svFjj6cOzXY_1KDp9XTiiLaTCRWPN-A6vbEwzKYquVq0WOFCwwuu2VayydAVyJl0M3fVSXrcMe5WZDRZZaQrt2yl5PeKiOxjOmoJPvoJT-7-bj3SNIm80j5TeasHTP27wK1KDkqqQL2fxTFx7xmknHQXUEA6T0cgG3qZ4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نیوشا ضیغمی، علی دایی، احمدرضا عابدزاده، علی پروین،نفیسه‌روشن‌وصدف اسپهبدی درحاشیه مراسم ختم زنده یاد اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26807" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26805">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbvtxpxazITXp0d97EVxMxlSL219_8nZkSDHkLn-hT8bWMNMO5q0ZUPINrwnQVOcktrxfkTjc4PGqB93y6gkbS1wBAa_59uY-T7n9ZnnnDbpNPKQLFAk0q6oaARXADDzFdC_q28rqLNWbiyxLEX-fCJDoLcTyuO3HHwMZjAA6LtERAmUnVScwFwmyW20ttm9S1i5vvsWIPl4HJOuqa_Qtm39KAWubjAuV2eXVDtn5c1hN3UZYb5XB3tZpvVKsAVSgqbUC3opP9uxkKfXl9t0Qh9U-0I_fORoX_ROsl9q8eLxWXsjUz4zddep0hNN5erqlvrIMaigQBbYBgnPnsCjHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا
؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26805" target="_blank">📅 11:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26804">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErH9Myci-Mf7-sKHT_5bJWt16UzU96cMNq86aVifRKOr1MCG4M9TX3c_oEP7Bmb04xx3sRxpvVa0O-UXvb5nX-hg0ZvUnHl_ZhqsB0OXj2qYnzxlEKXv1_vtg3g_p7tu25JnU29TypvxnyJp4nPLxUK7qeiBIHnxJh1Y_HioNErnykXt8_9OB70ymK4n25MLGgFdOAhXAE7Icw36l499hQ6AGkQ5brBJ0Oa9AefG_X4650p03Ah5BzpMSyk_ntMPubZ4ejAuwE7ggq5tgfBpmy4kQSh_vjv9MazyJMkT-NIn2Ocml6oMggHQGozc_hw-uosk4y8HhVTwctRYufY5HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
با مخالفت مهدی تارتار؛ باشگاه پرسپولیس با وحید امیری برای‌عقدقرارداد یک ساله بعنوان بازیکن به توافق نرسید و به این بازیکن اعلام شده دیگه در تمرینات سرخپوشان پایتخت حضور پیدا نکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26804" target="_blank">📅 11:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26803">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‼️
ویدیوکلاس‌رقص امین حیایی سوپر استار سینما وتلویزیون به‌همراه پسرش در فیلم جدید «استخر»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26803" target="_blank">📅 11:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26802">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wm5z6zoJGQ_9ARMNWZVxEgt_JhnuNxkrrfE1-pF0VbZfkDvZhO4fXnG6ZG5S0LYg9z3TAgtG9rdi0pi_YxY5mswL8TefAmrE6UUqD7edv-IUUaGLqlxxSjG0F5PJaF1kLf_b71QdTWwBTkcrS0CeUpyK1WQsaqq8rT1z2d-SpKHynCgMN9mEYjdCRP9s3Lts9wAxaSbjb4zfGDnVs2_Ql3fyVgR4-faXuKzfnCLl0di22mX0WmMK_an6tX1HLf2D-A2hDq2u3jv8kQdZe3TBFWoUqzR2hO8hmuhAD80HPGCPExHtNRGXWmhOQwopDcsfPLfTTd-Z03h-I7DzY1qRgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریه‌مارکا:ظرف 72 ساعت‌آینده‌انتقال رودری کاپیتان تیم‌ملی‌اسپانیا به رئال مادرید نهایی میشود. سران منچستر سیتی تمایل خود را برای فروش این بازیکن با رقم 70 میلیون یورو نشون داده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26802" target="_blank">📅 10:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26801">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78462fd8c6.mp4?token=eNzhMSyp-HsD4IDBjLg0Mghgh83T5-_AtL7MyKfLg4LGHApbUul3JLinLPiLE58z5fbQI3DokWLmBgms7SNzeDlOh8yoWdLbhL0SfBh8WpJ-e9dXr9s-uMlOg-I-BzHSMGB7pT_2xaAF-gMMdIapvkA_M4jyfze8H526E-vh1H_reIgrMi9IxD8t2rDOp1yuiZJdjnN8OPR9axmYcTQR1zCIMLQ97uw-JKRKLnrHThrnhkQRpoi_LLSIBGN6kKjmlmT64zE1-cK30OSBob8LFWhqOYkxTMZ4Ky0H6UZslLgvXGk7twut1pM-00eVSHeuZnslIFCKcrZSWjR0ohaV8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78462fd8c6.mp4?token=eNzhMSyp-HsD4IDBjLg0Mghgh83T5-_AtL7MyKfLg4LGHApbUul3JLinLPiLE58z5fbQI3DokWLmBgms7SNzeDlOh8yoWdLbhL0SfBh8WpJ-e9dXr9s-uMlOg-I-BzHSMGB7pT_2xaAF-gMMdIapvkA_M4jyfze8H526E-vh1H_reIgrMi9IxD8t2rDOp1yuiZJdjnN8OPR9axmYcTQR1zCIMLQ97uw-JKRKLnrHThrnhkQRpoi_LLSIBGN6kKjmlmT64zE1-cK30OSBob8LFWhqOYkxTMZ4Ky0H6UZslLgvXGk7twut1pM-00eVSHeuZnslIFCKcrZSWjR0ohaV8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روبرتو مانچینی سرمربی تیم ملی ایتالیا:
🔵
ماجرای‌من و تیم‌ملی‌فوتبال ایتالیا مثل داستان یه‌رابطه عاشقانه است که به خاطر اشتباهات تموم میشه. متاسفم به خاطر اتفاقاتی که در این سه سال رخ داد و تمام تلاشم رو خواهم کرد واسه بازگشت تیم ملی ایتالیا به جایگاهی که شایسته اونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26801" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26800">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇧🇷
نیمارجونیور ستاره برزیلی سانتوس شب گذشته به این شکل برای دختر دومش جشن تولد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26800" target="_blank">📅 10:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26799">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_YABucSmlU3igXhw6XHDgtUVjh0Dho7F_OsKsUICA2hpFvUhFUIvEWxfaXdXsLk3y3N-dpmtXaYTY7PVu36CpfxLIhII1B5ktLxQRsdKGIAyCgOxXRKm8ov5y44edjKgxLY0Pg2Sts7mswEJtCnD-mK_g-nnAZZeFX4L6jcz36KHo4TqsIe_KZxUXuIbMRUzpKm0_GEZXQzx8exaf9-wvZg5TUITsrQLkIGztK9ZyHg4cOrgTYlMaj19HUfLKnWp4pCBGIax9HBwzDRTHEKHqpBiOomvhHvpdKXxxssqf_OwXrqnGKX0raZhegSbgn0af2X46fKFF2Fr2AymXbNtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اکثر رسانه‌ های یونانی از جدایی قریب‌الوقع مهدی طارمی از المپیاکوس خبر میدهند. این‌تیم‌چهار مهاجم داره که گویا سرمربی این باشگاه تصمیم گرفته طارمی رو در لیست مازاد قرار بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26799" target="_blank">📅 09:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26798">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmt5rQrlWS5Az65t3tTYU21u8o5rqCxFEMrRanFtrwQoNHI9BzTiffKyz1k7dwbbsvmUV524G880WMIR7xSMO8QdvwCSqU93s2Al0BkemASCiLK4iWx9WP4Pc12rAmpqWAID9EqOoX1WoRI7VaAW_hWar24ptcqxby9fjiK_uma_oC2IuqOVhabYOIpd9o_0jwBg37WnuluySwnOCVL27fHqOEw8drSo9Oyb50ZD4h3NpLBTFAdAifdGPZhIlBPllvn93N4tByytN9xtNpdIAOlKvtcRkJqDmISCr-b-ERDIbrEApdmYlPhXggSA3u9YQ6rcoDWWkeGbwN9B7nV5jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار های‌ دیروز؛
شکست دورتموند مقابل تیم ژاپنی و برد سانتوس در حضور یک نیمه‌ایِ نیمار
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26798" target="_blank">📅 08:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26797">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2YPErolUwwZtnPBXbTJ4D8Nbpxx8u8mDB9salmofqvGqVEs229n9wMEKSOjKf3rXDkRKBqQTkyj2SZaHHZupXBg5KulBmgYaB1B2TEOzr5KQu2oxkeJYbWosAup_wafEXdahNAkHpbV3EXKToRN2FyuNkhhHl8ygOAJyxQvgABAFxMxKXhzDWBfTogAkuuQ52srqhUsGEJKM9Kd-lIE241pNN7l3sy8YwP64YuGF_sN1G9H5payf5oei6GkPsZrqiPsYfQc5COts7GXONMg19X4bepbVtqh8tr-i6NYNr7EHeNbID40mwjX2A4iOXvH4hxZ-NMMM2eyKWZMyfQmoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26797" target="_blank">📅 01:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26795">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fda6c0e0e.mp4?token=ucRlsA6i2pytLeOdYOs1cNGBNg2lc57zZtFX56ijPBdx_l0HMGI5umAsuHnIC1k23KetSgCJcUNPSve8NFPusbJlrijk7rzSXrp1aTwY0D2GVVf0nP_52_UGu9_92W60moXFXCBy9ZiUpxnvnXK-JNNIIYWzeRe-oJO2KfnASoc5uOaVIaObuE5QdZUojR0TMV8P01VgAHZUdXG7x4P2lNDlNyThmKlAlYpQtje-2uT_B5e4EpfdYxwYiqhsDD5pQJRVsx0VxspO_rQnTEn6YYMIL1YgxugJQNjXcoc_K5UVnA1z8NKcVfcPrE98B39-nTr96J4ggMDrRmomeK0qYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fda6c0e0e.mp4?token=ucRlsA6i2pytLeOdYOs1cNGBNg2lc57zZtFX56ijPBdx_l0HMGI5umAsuHnIC1k23KetSgCJcUNPSve8NFPusbJlrijk7rzSXrp1aTwY0D2GVVf0nP_52_UGu9_92W60moXFXCBy9ZiUpxnvnXK-JNNIIYWzeRe-oJO2KfnASoc5uOaVIaObuE5QdZUojR0TMV8P01VgAHZUdXG7x4P2lNDlNyThmKlAlYpQtje-2uT_B5e4EpfdYxwYiqhsDD5pQJRVsx0VxspO_rQnTEn6YYMIL1YgxugJQNjXcoc_K5UVnA1z8NKcVfcPrE98B39-nTr96J4ggMDrRmomeK0qYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دوگل خاطره‌ انگیز از ارسلان مطهری و وریا غفوری به پرسپولیس و استقلال در زمان حضور در نفت؛ هر دو گل هم در دقایق پایانی زده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26795" target="_blank">📅 01:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26792">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R65By41Ue0nkiA7DfEsvFI0w8i3RDp6UAVVtXglKjDnkOza5flxZi4YDYphJoTcHTqgwGArI9eIzMtr5scNkLXLeM1N8PdVsheOoAzVG9GNkPq03QzmjK0ayGdvQi4K-PbFGgDa9KM6gUdD-nlpg0cRVhmrX-f-ketqK5HVDIAqN3XXRIvepCFClJFHKrNGFrZ6-jXNwSGkTRYcg8E8Hi9Mq1I6uArV2ijliIAzJoIDblm5JUk0FNzcd05EZJ9bnObrYtLZOiJP1NpeFQr3XKpblH4WPLRJwuWFLpkjXc1v1Fiuq9VsGFyew3MgS-ONVsHyJXQiGczW-ziQFx62lmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کریستین تیو:
وقتی بچه‌دارشدم، همه برام کادو آوردن بجز مسی. اون‌بهم‌گفت‌که کادوی منو تو زمین مسابقه‌بهم‌میده. کریستین‌تیو توی بازی مقابل لوانته هتریک کرد و هر سه پاس گلش رو لئو مسی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26792" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26791">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DqgSLGJSe1iey5r50Z9tfm91FjnQf4MRuGTy0cEyYgVGLe6C39hK5SUjvFNWxGzs6thGlUq2C5vUSkdk3GEElJV-eSbsiDTeIrwbPaq8Piy5aUaKDOqrSQaMP1ybEqvNzO5aj_dV2B465o-4jTBf-9UrycGQqawmGmr9bd3gT2itPPV1Ia81y43dwdSECtIZBmvzJGkfjgcv_4t5oj07KbtT4O45JJ0vd0Wjqf1xIY6Jnw8Enl2bsLle0JZgFhz5pKqoL2v1BJ0eS7SyG-JH7riF4JIApHsr6eqWJmzR6Y2g5C8x-C4hfBtUf-OtZQUG6c9pe3lemjsn5cJhzYhSqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اسکای اسپورت: وینیسیوس جونیور این تابستون در تیم رئال مادرید میمونه و قرار نیست که جایی بره. رئال مادرید به تمدید با بازیکن خوشبینه و هر دو طرف خواهان رسیدن به توافق نهایی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26791" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26788">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hS8WExxThX0dUQgjdruyKGRB4zvgdoOpqAgbkD_WZOuh_lb5b1WX0kp2oiFe8sVKTzQvuM3stFbaOaGbwI4PITSJCZR0s59xJ5QOHJtB-NhqneY9CkJd29kGTJ1CpTH5Cs2jfLBiaI7FH9B7L0qS8jeEJXc6NMHtUni7GXgkspuNhgOk40FXxhVIGv-QPJBfrYvaQdzH4B-h74T4VyO7SrGADUbD80HrrHgsJXWwy_zbg4cnC6BupPynBbwU3Q4dQFu4bVLh_qQRUfPNSuOh2uW5eqcxLbAq-0qsKggfmabo-WKFoC9kS-gcDoSnnGoGtdkrZEautbQt-ljqted3iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FfFiaOKK7G93zcOqGors2CgOPL6axwsDp3ZtXQc-K4l8mf1HjKSNH6CwjVL0Cyke7zdrK-0nBPy4Wt0ZmzoC5tnmmj2riw_F9D28B0FEpvyNavi_89LEZIU11YhC4fTiwuoWzWBuJs4ZBwDwCrQVozrmnbDnqv01aEUsEyOMCxYEPGQcc-g2e11FskXx4hDtL9fTt8DY_Zdh4xL5S3SjIMRt5lyf6zxV2ZshqfyM0Y9t12xNBk3ODh0fIeA-BN2E7qoRQAs70b65UY1jmcLwWXg619wvx9i0Ar-0ZEJx1WvlsBht4bVBcojM4o6xbtFNNM8xKRSmh__m1Mq5NTkxKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
تیم ملی والیبال زنان ترکیه با برتری سه بر یک مقابل تیم ملی برزیل قهرمان لیگ ملت های والیبال زنان شدند. زهراگونیش‌بهترین‌بازیکن تورنمنت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26788" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26787">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d1f12784c.mp4?token=itcvm6L94Id-SPkm6QkDbS9WHWuBm1fObUECHgo2GtD7UrPiybbby5rLn8GMXtnkiaeU6NplzrvfsXPaGio3V_APxHeQt1a_rDEbESrZVihnDODRN65KShwyzSxFzvfHm5x3ovnnEMwW1CnIJ55qzJXT_L2l0I3t7tOvBYY-CbC5k4EzBmSLBZ0Z8GuggVipQQHwiVzCvbZS_tMgVCk55XZ8IC9-qNoT7gy7g7Ngv_HeD4YU8BNzDSQVGgBMHvkkUL6IWK1R5Yf295YNc1Hz_qupZn_LHaMcDB5eOHhREFN-9P7HzvJqnBoqo_0PL4CHKF6JeLcj8p_aF86mKBuKVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d1f12784c.mp4?token=itcvm6L94Id-SPkm6QkDbS9WHWuBm1fObUECHgo2GtD7UrPiybbby5rLn8GMXtnkiaeU6NplzrvfsXPaGio3V_APxHeQt1a_rDEbESrZVihnDODRN65KShwyzSxFzvfHm5x3ovnnEMwW1CnIJ55qzJXT_L2l0I3t7tOvBYY-CbC5k4EzBmSLBZ0Z8GuggVipQQHwiVzCvbZS_tMgVCk55XZ8IC9-qNoT7gy7g7Ngv_HeD4YU8BNzDSQVGgBMHvkkUL6IWK1R5Yf295YNc1Hz_qupZn_LHaMcDB5eOHhREFN-9P7HzvJqnBoqo_0PL4CHKF6JeLcj8p_aF86mKBuKVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛عصبانیت‌آزیتاحاجیان‌ازسلفی‌بگیران در حاشیه مراسم ختم زنده‌ یاد اکبر عبدی؛ مگه عروسی اومدین؟ که لباس‌های سفید پوشیدین و دارین سلفی میگیرین؟ خجالت بکشید بابا. مثلا الگو هستین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26787" target="_blank">📅 00:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26786">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556eaf6051.mp4?token=QkIhRpPRGxso9Z9lagUsTtvdNPLAkl85gmSA-KJqMYxe_8ori_9xwduLlT2HS25v8tsgCJUoH9Nadtwy2hkkWWxusomafiXtBiJUQnaoUjdi5fBgqzuet_fYFr3lIMQ2QA2rLb6J22FkNpLFB5ONFUNxOTGpgHIgDL9tTuEBUhyP2IjX1UMxYGnAhqKsVsFwHiIWmJcd-euxHO-yc5ZcJVD8Wraskb757oTPwsSFOVt5mFaYOPUWdzrmz3-O6QVKA5DcBrfbrPkisYSrFtXlWRAHc_PZeyy0mP_FUT_CX2OiLsIPjqpIcctZOeYxROS4Tadgo1dWDtPZV7fW6BgUww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556eaf6051.mp4?token=QkIhRpPRGxso9Z9lagUsTtvdNPLAkl85gmSA-KJqMYxe_8ori_9xwduLlT2HS25v8tsgCJUoH9Nadtwy2hkkWWxusomafiXtBiJUQnaoUjdi5fBgqzuet_fYFr3lIMQ2QA2rLb6J22FkNpLFB5ONFUNxOTGpgHIgDL9tTuEBUhyP2IjX1UMxYGnAhqKsVsFwHiIWmJcd-euxHO-yc5ZcJVD8Wraskb757oTPwsSFOVt5mFaYOPUWdzrmz3-O6QVKA5DcBrfbrPkisYSrFtXlWRAHc_PZeyy0mP_FUT_CX2OiLsIPjqpIcctZOeYxROS4Tadgo1dWDtPZV7fW6BgUww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
حضور عادل درمراسم‌ختم زنده‌یاد اکبر عبدی که ساعاتی‌پیش درمسجد جامع شهرک غرب برگزار شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26786" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26785">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NeBTQSmR6suUvKvntcdsMLtlhUqPpIYxFHJNiDtNyzEgxhmwmMMB_aJXzJUqtmdRP8Rx14zCG-OrkWM2I6vV8ZG9jKNoCGZT74TFB7EwzOlEaQaFcio1oFm5aJkipCRrnhNXwcaBRZKkFccny4EtF5tgAmr_3ScXA8D21HNcWdAE3a10hRpcu77AesfuqZY2mGpQP9zflvmGu8oNrHfcLU3tIIUaVr-Xc0YRsSsf2BUZvIYFqujSuRLJxKzjp3XaZZY9SrMWiPDN4wj-4kEu8kqnBFkh-D0utyoEtPwBgmBF_v_17uJ3Jvj6aFTItCx2SVvUjT9XS46lX-TIcUVQ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26785" target="_blank">📅 23:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26784">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3npBtKCYAyUR4zUgRhQznXde8ycpEKsQsdFIUOakLI1fHxdW_u9tGpjmAoL_FfAJTILyZ-LI94s7bT3rqCBFB55da5xxdYZ8jMeQdiAoETvTeaAjQ5qia7bNHe3KcFIJtzkF24bCx5P5rlrFP9tUizGeQ6_bPrH3P3VF-YYt30O0hOYPskVoP86WFN9snaGUUreKobFII5s4ynBNYEdaJS1FgDk3Ai7ICmwGACtuOBXPykyOLR6jOC6ngxftFywkmcLVTcQMprOXTJi2CSl2xdjdfWNj3f5f5MzRNesnpmUkWvcjeqPKt3KOkLNCYUxW9i2nkJhYiijF5NBmXKnvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛
مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26784" target="_blank">📅 23:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26783">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/787ac45905.mp4?token=pxEe3IV-ukc6W-Q20viReAmUBAvpfT3-kpohhpY64pBu61G0Hs5-rBX93wbVShSTq6mNpieCLML2GKGLrXPMqcLe7OWSFsAR7YT-QfdlGkmy-tHrgZKWO53BhmLYAyl0G7rJes7UeJZc9oKEWZfsIzEo7kSDVvoB7FhN6GtM3_Y9N_uQTYKT-i1tUYfd7JCPfOFCuty5NU3sm4lDSgWfo4MZlNN1eEiYZnkP6mpvyiLN4OWGKA5MOPltFASo20mltO21AKxCAJvxfywmfkcH7bNDmkBBmmbifC4nb_ksXvZgvYEWdCPIOeqKscvluDTXOqRpyMIfdelESQD4AlTvhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/787ac45905.mp4?token=pxEe3IV-ukc6W-Q20viReAmUBAvpfT3-kpohhpY64pBu61G0Hs5-rBX93wbVShSTq6mNpieCLML2GKGLrXPMqcLe7OWSFsAR7YT-QfdlGkmy-tHrgZKWO53BhmLYAyl0G7rJes7UeJZc9oKEWZfsIzEo7kSDVvoB7FhN6GtM3_Y9N_uQTYKT-i1tUYfd7JCPfOFCuty5NU3sm4lDSgWfo4MZlNN1eEiYZnkP6mpvyiLN4OWGKA5MOPltFASo20mltO21AKxCAJvxfywmfkcH7bNDmkBBmmbifC4nb_ksXvZgvYEWdCPIOeqKscvluDTXOqRpyMIfdelESQD4AlTvhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌ازاین‌گفتگوی تاریخی بچه‌های غلامرضا عنایتی با عادل فردوسی پور که عنایتی به بچه‌هاش گفته قبلا مربی بارسا بودم؛ عادل از خنده غش کرد.
امشب غلام رضا عنایتی با عقد قرار دادی یک ساله رسما سرمربی تیم لیگ یکی پالایش بندر عباس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26783" target="_blank">📅 23:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26782">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f6c32deb0.mp4?token=JgFN0HZn3uOodznVn1pHTXZ0wqLbOdjRvOdEHW0q5rlYyVngNcEoMnLnV9G2BTdIP4Chx7wwl-B98zr1kAjK4nZ4yNEWPXW5FC61mMmG59H_xy0feQcIXmAezpmWmL1wCTzgfTGA4YIgrmA27Qp7HXtfWqagZ7foU1WNuGsQDWkMXdgpCmT0cmnm1yWXPhdEocMcqPKaXkd4E0kHnNRtYbn_2OgdZR8Jr1QXa2QaG-DbYi99Jrd2v8qoyktvdGu7ysKU8TufXQIJBzGoMJXuT83SXt-wnqVn6fl0v8rKWSmjq2IvtaquzWMqeypbelaCWfQ3AzK6thcLxZAzuHgHkRMz3DJp4oZNSUlVL9U03gKtunp-ZLTT9_nBMlY2xshuIl2SS7aV2EIEPcQgmtVPwbUCPC329LTOvlbV723RR_XvvV9CduUGhGr0IEVEFZGDQejsAMc72g0_mkCRY-jCBTRgAmghb3Es7dTwNxeGlAZ7jieaAYuck8M5DyHIwp07t-ar6nsiOcN3k-0HjYtZmCoWiltWHeu-WeyZpt57lAs_oEWBUb6ppmmPG56vraSt67FoaQk8ynMbSuPxDyfzmq48uka8hw2xsukpJMXsFGi4OCMudyNAS-gbNVPgO1TRd609i6XGbxWN79O2bMcB17NxIaC2oZ3Jjv3XTYDpr6s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f6c32deb0.mp4?token=JgFN0HZn3uOodznVn1pHTXZ0wqLbOdjRvOdEHW0q5rlYyVngNcEoMnLnV9G2BTdIP4Chx7wwl-B98zr1kAjK4nZ4yNEWPXW5FC61mMmG59H_xy0feQcIXmAezpmWmL1wCTzgfTGA4YIgrmA27Qp7HXtfWqagZ7foU1WNuGsQDWkMXdgpCmT0cmnm1yWXPhdEocMcqPKaXkd4E0kHnNRtYbn_2OgdZR8Jr1QXa2QaG-DbYi99Jrd2v8qoyktvdGu7ysKU8TufXQIJBzGoMJXuT83SXt-wnqVn6fl0v8rKWSmjq2IvtaquzWMqeypbelaCWfQ3AzK6thcLxZAzuHgHkRMz3DJp4oZNSUlVL9U03gKtunp-ZLTT9_nBMlY2xshuIl2SS7aV2EIEPcQgmtVPwbUCPC329LTOvlbV723RR_XvvV9CduUGhGr0IEVEFZGDQejsAMc72g0_mkCRY-jCBTRgAmghb3Es7dTwNxeGlAZ7jieaAYuck8M5DyHIwp07t-ar6nsiOcN3k-0HjYtZmCoWiltWHeu-WeyZpt57lAs_oEWBUb6ppmmPG56vraSt67FoaQk8ynMbSuPxDyfzmq48uka8hw2xsukpJMXsFGi4OCMudyNAS-gbNVPgO1TRd609i6XGbxWN79O2bMcB17NxIaC2oZ3Jjv3XTYDpr6s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌ سراسر سم از گفتگو جواد خیابانی و خداداد در ویژه برنامه جام جهانی؛ خداداد خواست کاری کنه خیابانی کم بیاره ولی ببینید چیکار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26782" target="_blank">📅 23:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26780">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DyWsWQ6RsWpb9RG1HlxLMAK4Bx4VG5gow6mn71pdZ-trR57cATM58H4dff4JmhSj8uzPGX72KF-05x31-ZktbHb3gnAKb6cKhlcy3F8WXv_iSjBROUGS_Zslk03i43pLMwzSAIxISxCIQ4rQdiKzoU73uIHuHQ5r8WSvaqAMJmzDluiHLfNLrqhcDSr9aqo95LENVjz5odB-6bx3wj30ssFQR6fIZ_d3B59Sg5pPhZgsbluCF7dVoaNVPIzXYlJCnAgJTfwizwms5hEEj133b9UNskCQKNIdw37KrxAwiPfLu5ZJctOKywvCYIIawfGC_yu5HyebqwxEfGfGt7qbcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q4EzytR399MYFBDaDmtbQ0LpFKdN0T5N6PbzEFYKJdYtRYSVDjlnD70CKV-Qxh7py5-yc2QoH2JL1evVsN5ddTKSNNYMIETcJSyzANWyHTNFjuQRlzfjktaaij6aLe9HDmOo20jRrGk2ECNFSbmh9uwzfkbb9fcCDtu6MivTR14h0z_yRDMx2MAif1esctBuSAiwmMITKokNSIcnlHEsbGAVQAxSjmaD5Hlth1N0GYvA0ywl5696Z4A1CBZ8fxKlfcK8clCVlbSCC9tAyrUHEquXZSV2jakV671fy5aAOZkTezLOBu_GSubO8Bal1JmJo961PgilRvTU8HecAFxxyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌دوم‌وزیبای تیم منچستریونایتد انگلیس برای فصل جدید رقابت‌ها که استقبال ویژه‌ای ازش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26780" target="_blank">📅 22:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26779">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOdESV4NwsgxnvrxKofZn4qghGydz3SuaETIocTgxwLX-L3G6I-okdyNqhwB5iumkd1mqTb83WskcdWeE6l9_SgEDzf91-aHK9OPj1HYN0u7P-ZhObulBEGOmvzop4EtxB2GAOMg9bvTWilfy30Bnvh-7nZvnCCojfY7DjrRNne6idGfx5NZvfKMj8dSCbj1w4QjcO3uXlPllEhl1mjA76Ls8IBuPzlQlLkfgCvCrkiqIQP5o2bC7UrQSb3kwHFeotwsh3oA1b-9KWXAWYJa4El-RqCihhyUqt_79tzbdE9e78UjnEpN07MX6zuxus6dNE_NhnVkypbMbHHU1J650g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال بامدیربرنامه‌های جلال الدین ماشاریپوف‌ برای‌تمدیدقرارداد دوساله‌ستاره 30 ساله آبی‌ها به توافق نهایی و کامل دست پیدا کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26779" target="_blank">📅 22:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26778">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQEDgJXcOQq4hEyTdC6AF2XaM9nukhEMx-sn8a8ygY6ExotIeB_hqrT5EXEWZzAr58BpVQAJp-_1o-9lM9L5_CCT75ENleToP4qitmbU1nBg1JY2HbbpSAW9EomlzSfCubEGQ0SB0hjAFXLQMA3Vhjea1hoZVPK-EVjqbLCw8VFOy7tRQGwvUxnogkJYTOWdG6Q4hmONmgCmG2HyFtWqNSQtSJc-n3tps0YrLIm6PcUKLprAFuhCHJ06Ew2biDqNzputs2b5n6LI7apz6eo-oCjBR_GjpYhhO4t0vhjHdttLCQwvDo9N1MR137WdyHtut54VX0kgDL8uU_-qGRRi-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
خبرنگارشبکهDAZNایتالیا: آندره‌آ استراماچونی سرمربی‌ سابق‌ اینتر میلان از فدراسیون فوتبال ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی 2030 پیشنهاد رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26778" target="_blank">📅 22:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26777">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5heu7BW5KRsQQCfgiLbehg1SM5Y1671386KPc400T1jlIQu6diUfsOXscbEFvdiIkPQpUYKsROQdlvf9ErS9hT_25z7qOgSvkoCvRifLSFZQ5ukp-7ngyxdV7k2sgF59g0ao2q4xP2Qx6OXpWN0ozdLnXEb2noUArCyLrYnbmyzcLL50QLgsbOhztis-M0YwEaDp3w3qd9vEan0-kttlvxByJBuCaDuepnea-HLJSSoqB6B8IDgDne2lrRkL9EbPg_1b8h0Pe2wFthgzWQQE8vrnBYXaJBFK7zCUnLI8r6LRNF3u55_-sic4pKBEFHjL7vU3-ej1ftCVmrgoEoLgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
خبرنگارشبکهDAZNایتالیا
: آندره‌آ استراماچونی سرمربی‌ سابق‌ اینتر میلان از فدراسیون فوتبال ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی 2030 پیشنهاد رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26777" target="_blank">📅 21:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26776">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHyH2DcwGnGkBMDxQbU3PxlfaMS7fCkj7su7oOvfeJyvCx-TQAEYIDhJOpmp__plxCSpLDVlTZy7kauAIsOpYZ7jqnnjyUC2KZggRudbPMCULgiyKRfpMEoGFcpeLfzDLbYToYQxqfHlJVUnDdMdXd8mQBeU1l4DL_jb4hoWxtksZsNZIUnrZtHzs1dpwust_XWfQV4wdN2AtBfFN73xf9cCpDb_TvPAjY-gn9nUxfMCODxvhtWX9rJKQp4LdAyXr9_O-3MyWTQhSLqpowJmNx6SyrRE2JHNjQN8-TocKn-l9md9naRVXcNvkgPF_VAiWXfFWY5soZdyOnO7OVFQTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26776" target="_blank">📅 21:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26775">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/762527d0f1.mp4?token=BiGrQ5ZaCAVvri2eGuB2O-pzRwCFhSyEBlW-npOXh-v6Zq1qquKWK-MmNrySIJJ0uvw7tzVaMLRmZ_l8bscHghyHMamLuFqUV-bospTbz8fjdUzXhcWidQHVmzJdAAz0UwmiWhGNa22LjLQSqhq83ORZ-ZDdjvTx-t9p8_W4C01GQnJTAwzyZaDstjTpK3cHB0En8WlB9JdZMV-tpdkwLY4a0naCQkRF-92N_oSOoWchVSDYDKflEOt9V78VSNfu11VWd6Fta5oC8aeASPQE864XC9DtU56mMOyRhtBlGg_AVxfwcqSz0F0g54k1zP5ech7y5cXVCOZCXpma2jyy7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/762527d0f1.mp4?token=BiGrQ5ZaCAVvri2eGuB2O-pzRwCFhSyEBlW-npOXh-v6Zq1qquKWK-MmNrySIJJ0uvw7tzVaMLRmZ_l8bscHghyHMamLuFqUV-bospTbz8fjdUzXhcWidQHVmzJdAAz0UwmiWhGNa22LjLQSqhq83ORZ-ZDdjvTx-t9p8_W4C01GQnJTAwzyZaDstjTpK3cHB0En8WlB9JdZMV-tpdkwLY4a0naCQkRF-92N_oSOoWchVSDYDKflEOt9V78VSNfu11VWd6Fta5oC8aeASPQE864XC9DtU56mMOyRhtBlGg_AVxfwcqSz0F0g54k1zP5ech7y5cXVCOZCXpma2jyy7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدشد...بااعلام‌باشگاه‌سپاهان؛قرارداد احسان حاج صفی با مدت یک فصل با این تیم تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26775" target="_blank">📅 21:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26774">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4063938cba.mp4?token=tQN4Y3bb-VIJZNU41B-oPThPIhfJUdVxFF4YMvPeVUqM_PY_7vb2EUltIPGJKj43pewJ7lWCaajCHubGLn5XaE0vRgsACI8HgezZM5xeayD5YcbsT9CUxm5zkVL-utUqcuCHL5AGFzZt8ZGbvv_aFHbEprumpgjPX83VL1lDUW-SOxtfkMcNti_0q2sjpISV6aTrnFHf9u58t4JQmaTyLh-czJ8v6-T92BqU1Ln0rL_OwS4ECxlzXUxkaz2P_a2XeF0Xv7LKv_w-niKu9MXqrfQrCk0da2HVLISg9n8igXBIzeRpzK0UJx_9DusAQbTIxOsWfgY82flnqSqg37hHxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4063938cba.mp4?token=tQN4Y3bb-VIJZNU41B-oPThPIhfJUdVxFF4YMvPeVUqM_PY_7vb2EUltIPGJKj43pewJ7lWCaajCHubGLn5XaE0vRgsACI8HgezZM5xeayD5YcbsT9CUxm5zkVL-utUqcuCHL5AGFzZt8ZGbvv_aFHbEprumpgjPX83VL1lDUW-SOxtfkMcNti_0q2sjpISV6aTrnFHf9u58t4JQmaTyLh-czJ8v6-T92BqU1Ln0rL_OwS4ECxlzXUxkaz2P_a2XeF0Xv7LKv_w-niKu9MXqrfQrCk0da2HVLISg9n8igXBIzeRpzK0UJx_9DusAQbTIxOsWfgY82flnqSqg37hHxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
استقبال‌فوق‌العاده مردم از علی‌آقا دایی اسطوره فوتبال ایران در مراسم ختم زنده‌ یاد اکبر عبدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26774" target="_blank">📅 21:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26772">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dkq7QqKbt3WEO2hGXan5-6jrqIJ45kuhxG_EfMRLBMQrwuL5yO9ep8DA5JtzvBzIQJ2yd1-dVm1Cu-KVYJqrly-085YsYS3lRs1k9zy7WZ8uskpCIX10V8yhIkjAqhYZhZEjzyeJAkrLYZsKs5pm6fGJXIcMR3h_NOozhSHBtTXU_sPG7cgGuMBuGbEY8Uf-FLQb6sF2ziYISGIeHU5Q6iVFmBiWvfWB1tl02r-NrdOqHwwZjtRpZXj2izhxAvXcrZxSSMpoXkeUZcvMJ8nFzQ-Svkto_YB4IcJ1DRCTCUA8p5HJwHBQRrRtT_uHEPifuuiZolMA1LupcdnsicA6Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mE3IIKC1uHjMGjvk4sMhVXkKLCIGuYhu2Vge2PQSH2Du7FoWmEHzfvs8JZEt91ZwymuyGx9buq_S4xCMu73EqWIn3ykSorkHMNDL78JyPKe4iAkGuN5q8Gf7ApjZN0bvHQXyZYbehKtQdcZAwEdxGD1-R0pbiAxwpAHUzxckBDlp9jIguphi6FWGOgMbBoSNdAmzejMXfUvG1pes5KXgbeNc8YR-tP78ft3e_JmYBTIPjSbKz8RmSGuXwPVLORFdefine0G5WMMCkHpkOQjH-ocn-UFRnwUT4fkW6w8XXqNErMcJBuIc3rWPOOwuEev89g__36lwD4LTfmm86E6m0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
ویدیویی از مراسم عروسی شب گذشته گابریل مارتینلی ستاره برزیلی آرسنال با پارتنرش؛ مارتینلی حدود 8 ساله که با دوست دخترش بود و بالاخره دیشب باهم ازدواج کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26772" target="_blank">📅 20:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26771">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3befee8bbd.mp4?token=jHHlsc7xERcboKbKGKWxqpxHFMAEEvLNn4m6oY6YqPwn_2lh0_psssTQxpDiMEHp8oE7wCDaA8SsNKrMMMjENiRcADWMDqJjDAri6ZfUL_UQHvX4P8UadbVV0yZNEPCosLT5ZZzoLBdNobqmzimtoGkhXBFNTU4y5-0bO0RYbmfS01nMDwBIj5BWQHnc2wUmfq1xxg_r8eHaSU5tTuIzQgHnV5331lRaGihq9CPC99tI8pdNeIYL_QYM5xE2PzPUai35vfh8eh3NYj8V4KzR3-OgHZZatGN6OaRXeuqGzVXAtz-qjIyEwJ2ySTFcTmtmkNxrM_FFCnY_E-u_x0KSrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3befee8bbd.mp4?token=jHHlsc7xERcboKbKGKWxqpxHFMAEEvLNn4m6oY6YqPwn_2lh0_psssTQxpDiMEHp8oE7wCDaA8SsNKrMMMjENiRcADWMDqJjDAri6ZfUL_UQHvX4P8UadbVV0yZNEPCosLT5ZZzoLBdNobqmzimtoGkhXBFNTU4y5-0bO0RYbmfS01nMDwBIj5BWQHnc2wUmfq1xxg_r8eHaSU5tTuIzQgHnV5331lRaGihq9CPC99tI8pdNeIYL_QYM5xE2PzPUai35vfh8eh3NYj8V4KzR3-OgHZZatGN6OaRXeuqGzVXAtz-qjIyEwJ2ySTFcTmtmkNxrM_FFCnY_E-u_x0KSrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
حضور عادل درمراسم‌ختم زنده‌یاد اکبر عبدی که ساعاتی‌پیش درمسجد جامع شهرک غرب برگزار شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26771" target="_blank">📅 20:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26770">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qze2bkRA-uqbPS0FFFHfVI064Xgc6BNp9y3UQgE2Ly_99CjEvG7WiHz-frNU7pzn1yTXR6GAAAjZ4YxvS6bIpUT9njR1c9WCItoNLs-TR1Eaod412ernOLteqJGHHLX__Xv5WX7fLgWvcLBSDaNTtOlgHrQNVSuBPCnNEVNiTOsgufN7Kr_mavnrQJMXqIhcIiSFm-wVbyC6Ky6qaSMtnUBV6fm27ZShh6exF7U-9Q7SFsiXiwpttRjkKlwKXz9sHv_2o4rjLlIyz8_Hhv2Y_WwuWVA5h-OpsEnttS15gg4ieSsQkKxDNw6ejiK45REpPl7kg844LVd310JvAHQgGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇪🇸
🇪🇸
باشگاه رئال مادرید بعداز توافق کامل با رودری کاپیتان تیم ملی اسپانیا؛ ساعاتی قبل اولین پیشنهاد خود را به باشگاه منچسترسیتی ارائه کرد. انتظار میرود که سران سیتی آفر رو قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26770" target="_blank">📅 19:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26769">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsK_pJFgyz230ZNj1ePDCgTkh9NHWtWU3leWCuPCr2UgFJdJ0SDJHVrOvHELvMdRgNgvTNSIWRGD-GmkwCatN66tGx6r-lym735VaN9QfMrtK6BzakynDYoNnsZNW-3U1Tf1ui_8YKZ3y-MCK6tp6-ZbOV9nh4p3xaeL8p0a7g6dODKxffGgBlTh-Bd2tyW-j_L5sQKwK8q4aaIuhZ5EpPsJ1n910VPkbOSthg35xrZbnwnGeG4do2ET5M8BKAWFKaYzooKJf97G52Qf_EsD-_j4qjd4bRA1jwfX8PJw3S1OdCfYI7KyZyIkg-GeF3KL2jcVl2UD28BJjoeeVYdaPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۱۰ بازیکن‌باارزش درمارکت؛
هالند و یامال هر دو با ۲۵۰,۶ میلیون دلار درصدرجدول ترانسفرمارکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26769" target="_blank">📅 19:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26767">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee1553fa64.mp4?token=Y67UwIryMEPdPkTMs95R0O4kSETBtY7BjPbYOgUpFVQ26fzVbxwrijvXHQXYkuBve8jYvrMkntP0Rz1no5Co88FIzYHKEIRhPb1HbHDtWfmbgXIPAv-g5uRTvf0xbbLfc3juQZ6d3yognO4dajsbZ3r6o0MWlJqLLv-U7TBYVQmuRCXqY51EA6V_EDDEYNJ-VTkugxXiEL-DngeuwAyLUYgfa4Sol2SA6q6cNFUGLpTSNetX6xWAEOIwcdZlC86_2qpZx0F2gWc6Agq2Ju4ZRu1iohztdZdzDmU7ToNslAk_6ZGMFREXXVycMmq8q3ePX5WP0jgP7thV_pkcwH-pIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee1553fa64.mp4?token=Y67UwIryMEPdPkTMs95R0O4kSETBtY7BjPbYOgUpFVQ26fzVbxwrijvXHQXYkuBve8jYvrMkntP0Rz1no5Co88FIzYHKEIRhPb1HbHDtWfmbgXIPAv-g5uRTvf0xbbLfc3juQZ6d3yognO4dajsbZ3r6o0MWlJqLLv-U7TBYVQmuRCXqY51EA6V_EDDEYNJ-VTkugxXiEL-DngeuwAyLUYgfa4Sol2SA6q6cNFUGLpTSNetX6xWAEOIwcdZlC86_2qpZx0F2gWc6Agq2Ju4ZRu1iohztdZdzDmU7ToNslAk_6ZGMFREXXVycMmq8q3ePX5WP0jgP7thV_pkcwH-pIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوان‌رومن‌ریکلمه درباره‌ مسی و مارادونا:
«مسی و مارادونا دو نابغه‌ان. عادی نیستن. کاری که اونا می‌کنن، هیچکس دیگه نمی‌کنه. من عادی بازی میکردم اونا نه. حرف‌های فروتنانه و جالب از مردی که خودش هم هرگز معمولی نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26767" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26766">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hs6OqXPLzp5j1RvGfG3Hn54reOJ0_ZRTPZaQx7eZzWp4y5kyAniZ046jHGhxMdTTs2fFyoElDPw71gRfTxpGE5Q0X9B-vS7yzpIRoZpGb3IGlFCWkLY2L1iwhmdbyazoJDQO61nmzjVKtnmxOrLkHIJxyk4BG7301VN_VjeGcr1vyi9DCIuilohP5EfBVXufhqpAecIv1rGL7ztPi9AJMhHhCHxnIcxc06kMMy_JDYa9-WlHrK94ZU7nEAwWZJ_35Beg_9riUewaeZJfbaDRM0NN5NaT40bF_09fOtBIX5-NbLZ3MJTYZ7J6zTRunURzXTGct5TtepBJNA330mrtdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امشب‌محمودرضابابایی ملقب به "بچه" به رفقای نزدیک جواد نکونام گفته "بی ناموس عالم هستم اگه اجازه‌بدم‌باشگاهی با جواد نکونام قرار داد امضا کند.
‼️
سرمربی‌سابق استقلال ظهرامروز با مدیران ایران خودرو برای قبول هدایت‌تیم‌پیکان به توافق رسیده و قرار شده فردا به…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26766" target="_blank">📅 18:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26765">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijjOTWtewFDU7B9LvpX9cOrkG3vdeWcNSgWUJExlQIIEuZG6q67S4EcUi0IsR46oS2vIrNoRGPNnQtEyXc5drJrWABOtnHiVrGSZujAgm4FqIXO07CGPG2dvVOJwoqk0ujsq72SO6Vrjs6qT92zPU5kaxljSzWE81bcHM2ICkcr2gGWuitkgVsa0AwOWZvPa_yqOkYHry0_Mow03z04Xj00a0uPYr63ePI7axRKpyc4RaAtmp4ll_kG2CYhkRZizAjpD_w5Wm17xD9ggbKT9X7hG5hQrJc_iy70G9FRNmHtGQJuqZvuCVydhy6lUeXB-hXcetRzs6bttpLo-SaM29g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
نگاهی به عملکرد کریستیانو رونالدو در چهار فصل حضورش درلیگ‌برتر عربستان و باشگاه النصر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26765" target="_blank">📅 18:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26764">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97aa505010.mp4?token=FKmlxEZpIK7n_J9jZSdSKtG8dk0l8rTSzvmle9W6MKoVIOSoLLEznOE1IC54b2-SnxnYrTy3x5ZPbTGf7VQXFr1JYMMnQOfxQp_Bd7cEl8HN_OHKRBHBrtiYuxcSjLzIjSk8M2uTDwVmIRL8qteZ5j44cJoWxhTgljp_PIWSAeCzpgwF7vdMtdeyyyYj9mJ8-puiQweKOZGpSIGnNBQFwmY78ICN6SDqH2mBASu6hzwQEKyfg0iXHzFr-rIhALMF8kZJ_5h-XoMMNT7Q7geFt5Yn4levh8cllSfa9_ry7jHOba-dKxiUF-bp57mJm-dPiFguoh8wGveAfkz5Vz4y4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97aa505010.mp4?token=FKmlxEZpIK7n_J9jZSdSKtG8dk0l8rTSzvmle9W6MKoVIOSoLLEznOE1IC54b2-SnxnYrTy3x5ZPbTGf7VQXFr1JYMMnQOfxQp_Bd7cEl8HN_OHKRBHBrtiYuxcSjLzIjSk8M2uTDwVmIRL8qteZ5j44cJoWxhTgljp_PIWSAeCzpgwF7vdMtdeyyyYj9mJ8-puiQweKOZGpSIGnNBQFwmY78ICN6SDqH2mBASu6hzwQEKyfg0iXHzFr-rIhALMF8kZJ_5h-XoMMNT7Q7geFt5Yn4levh8cllSfa9_ry7jHOba-dKxiUF-bp57mJm-dPiFguoh8wGveAfkz5Vz4y4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛ گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26764" target="_blank">📅 18:43 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/kq-TLgnxTQKix_8NehwwZtXcnZP_ybdflKCc8zOrPVDPYKKu5sQOM6-OkvAS52GTnX-vdvvD_DjZL4VNgk5QunWhmJr7gZePtOqJhkO2mUd62yB3dk4UrZ5BYMBbEr_F4FK846amyD9xcCxNMI7B_RV7KLapgT18xVQfuaivOrQ_aLAEKE2NDjjkWvuKAeAp89rNWMjGwE3eNJTg4pT9EYYLLc4lvZvzVSLH2trSV4YGSdJeR2LGeGe0g19UBceP-wYSbqAURI2DBZUUOddj46Ve8WQM7P6xtw8HRG57ef3sG9blqzX1wy0ldL-0l2puCW8FwPq2-JdtA873C3QWbw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 922K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 09:32:03</div>
<hr>

<div class="tg-post" id="msg-146979">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
مسعود پزشکیان در گفتگو با یک رسانه هندی خبر داد که روز دوشنبه توافق عمان و ایران درباره مسیر مشترک تنگه هرمز در حضور وزرای کشورهای عربی حاشیه خلیج‌فارس امضا و به سازمان دریانوردی بین‌المللی اعلام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/alonews/146979" target="_blank">📅 09:26 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146978">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از مقامات آمریکایی: چین پیش از حمله ایران به پایگاه موفق‌السلطی اردن که منجر به کشته شدن ۳ نظامی آمریکایی شد، تصاویر ماهواره‌ای با وضوح بالا را در اختیار تهران قرار داده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/alonews/146978" target="_blank">📅 09:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146977">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c24f8e1f79.mp4?token=FqbVHebqbQjzbJx_COGrgCUE1VgHy-lhUGzyVsu6tome8kfd-o-yEdndkF-w3U7ptdh_BFAQbfi9HgSnirdQ1e69VRo7eXFs67A-8TNyp-a4pNehn4MDZS0cAnu8L84ie42uN5bN22YKs62y-fu-AW8djiEmo3ICquVtpuJ-_uPKMELhYM3BzyoRwbyBT1er9CVy2O31FblZWoJtK6VRn_5I0Sq16_Yb-eKKlYd21qMY0rTXIY5LQwX3rdEEInW68i9D8VlzPWQOCYsgfqTGRmhSzY4V3dEE5Y6_XGNYyh9lN3H4V6WOQIk_WC-0i0_DgKJp29xKMqYIebPu-u0N7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c24f8e1f79.mp4?token=FqbVHebqbQjzbJx_COGrgCUE1VgHy-lhUGzyVsu6tome8kfd-o-yEdndkF-w3U7ptdh_BFAQbfi9HgSnirdQ1e69VRo7eXFs67A-8TNyp-a4pNehn4MDZS0cAnu8L84ie42uN5bN22YKs62y-fu-AW8djiEmo3ICquVtpuJ-_uPKMELhYM3BzyoRwbyBT1er9CVy2O31FblZWoJtK6VRn_5I0Sq16_Yb-eKKlYd21qMY0rTXIY5LQwX3rdEEInW68i9D8VlzPWQOCYsgfqTGRmhSzY4V3dEE5Y6_XGNYyh9lN3H4V6WOQIk_WC-0i0_DgKJp29xKMqYIebPu-u0N7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حملات پهپادی روسیه به نیروها و تجهیزات اوکراینی
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/146977" target="_blank">📅 09:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146976">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
بدر عبدالعاطی، وزیر خارجه مصر، بر تلاش برای آرام‌سازی اوضاع در باب‌المندب و تضمین آزادی دریانوردی تأکید کرد.
🔴
وی ادامه داد اختلال در ناوبری منطقه باب‌المندب، منجر به خسارت ۱۱ میلیارد دلاری به کانال سوئز شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/146976" target="_blank">📅 08:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146975">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
پزشکیان: تنگه هرمز به شرط اینکه آمریکا دست از محاصره و حمله بردارد، باز خواهد شد
🔴
روز دوشنبه در مسقط در حضور کشورهایی که از خاک آن‌ها به ما حمله شد، توافق عمان و ایران بر سر «مسیر مشترک در تنگه هرمز»، امضا می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/146975" target="_blank">📅 08:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146974">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ac66aef0a.mp4?token=Hj7ABJCtZGdDeZXVCUM8sa6VrRusBEWLpPozz6IEltxcPeRq0gr3z2LtJRu81-0cPnHdSh7rTtkairHimS1hH9d5PEbKPo96UVYpolwr2Cdx8y3PuD5uuMv_IKf07N1ZPVfKS_7FeRIGkHNmflYoQZD0KDkIu28wtHLLv_D3vMlAqs6WrTT2wkxHAy7439tFTNWe24hwcTEf2w8n7bnIBaYs5MaGMcryj2uGtyAFs_3kPq1kPQENFOAo4PT3kWUvJ2QEgUqYjo9eItihyq75sPS77sFjvV9utiUxY06gv7LLxkRlUOxsClA8XsXwTAKNvzyNKkp_jyZrcAkC2lOkKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ac66aef0a.mp4?token=Hj7ABJCtZGdDeZXVCUM8sa6VrRusBEWLpPozz6IEltxcPeRq0gr3z2LtJRu81-0cPnHdSh7rTtkairHimS1hH9d5PEbKPo96UVYpolwr2Cdx8y3PuD5uuMv_IKf07N1ZPVfKS_7FeRIGkHNmflYoQZD0KDkIu28wtHLLv_D3vMlAqs6WrTT2wkxHAy7439tFTNWe24hwcTEf2w8n7bnIBaYs5MaGMcryj2uGtyAFs_3kPq1kPQENFOAo4PT3kWUvJ2QEgUqYjo9eItihyq75sPS77sFjvV9utiUxY06gv7LLxkRlUOxsClA8XsXwTAKNvzyNKkp_jyZrcAkC2lOkKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: خیلی‌ها فکر می‌کنند اگر در انتخابات ببازیم من عصبانی‌تر می‌شوم و کار را یکسره می‌کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/146974" target="_blank">📅 08:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146972">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CMWuZCPcBBF_pDFQ2Mggpt0rpBtd5xEgdWE4dfk3HeiJEuwTTRJGIhsu03xrRvk5arVSjk1nGohKzuWoh0s43BjFs7Kz5WiCWUfWEsOoNWG_1E1_cMGn-Ya5kN9OLJbqLPAdEnjjq9vizkUxPMHN4BiiGbJ5reH2u6I8-oqsXmYjWDNX-Q5XmlcvsZaKOzWkSsuQYZhmjFZVbZLJ82vjamUTQjWBTsyRtnlWJwJLq0pTVxDXVjIxFqek3fsTpWYkWy5XmSd019jo1E44LODzQ8a-Gn32Zr-bN1sd9QU91lyKyhBtBuRhtBhjNsmloP2F12YEQNEQhJjgZ0FCRMgjWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iBu743Puko_yEnHqW0iez4cnzwEI40ptr_cWSt3Vk8Mu2ZNZCt_NzmrT0P2s0Qpi3jZ-_Sga0FjaK9R3R6uG5JhSnMlOi4Ye0sTfC6gTV1dQlfzPON5XRMgWcmXpmgLKqni-GNWIiKaa9VJG_BvsMLryQ7MHCors2wnzj6H29cMO3iYqo-qr6ncG2Ptc0D1_3Fd_kPgpYbm8kgbZUMCe7ewVjPMwSrO34glWCfGE9pmMury7wGAreGnIgwKtECCr10c_EurVWFimKhHTAxYFD5XbDXz3xattuW3W_IibgPGdWswSKJCLtADwwUBDpMryuWEexfxA5IG0vceMlaYrbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
وال‌استریت ژورنال به نقل از یک مقام آمریکایی:
🔴
حمله ایران که در ماه ژوئیه منجر به کشته شدن 3 سرباز آمریکایی شد، ایران از تصاویر ماهواره‌ای چینی با وضوح بالا استفاده کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/146972" target="_blank">📅 05:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146971">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b31d12ff0.mp4?token=ufQL1-DagEcltRNw-97l2-TNE2jenzSsXV0ILlNUnMtK2BS3eQMErnkWJuZy0-liHnc2xYAVjcmzmJExU41D8FCNA9n8BBwsXL2v4EQjR-og8_n6u-3W_4QzR8ZKRvwtdx1XQ7PyFD9R_i_3vwH5gx5b38-uXHdjr4TgYzySb5OsmYcAXyH3ovv_zK-it48h5Jyz5x4aOVKRdIE7D_dVzin0bej2r-Qouo2WVOzmFpFYFxo7yekRnppOCdp5TbxXTdfAhdDmrWTK95XoKSBMEs-kRbpcy-aJfTeYblDVEfHEj6YUavBosAWKnGsLaTvBcmBJRQFbmiU00VNw5pBrWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b31d12ff0.mp4?token=ufQL1-DagEcltRNw-97l2-TNE2jenzSsXV0ILlNUnMtK2BS3eQMErnkWJuZy0-liHnc2xYAVjcmzmJExU41D8FCNA9n8BBwsXL2v4EQjR-og8_n6u-3W_4QzR8ZKRvwtdx1XQ7PyFD9R_i_3vwH5gx5b38-uXHdjr4TgYzySb5OsmYcAXyH3ovv_zK-it48h5Jyz5x4aOVKRdIE7D_dVzin0bej2r-Qouo2WVOzmFpFYFxo7yekRnppOCdp5TbxXTdfAhdDmrWTK95XoKSBMEs-kRbpcy-aJfTeYblDVEfHEj6YUavBosAWKnGsLaTvBcmBJRQFbmiU00VNw5pBrWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عراق مرز با ایران رو بسته و هیچ ترددی رو اجازه نمیده انجام بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/146971" target="_blank">📅 03:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146970">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
مرز شلمچه به دستور نخست وزیر عراق رسماً به روی ایران بسته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/146970" target="_blank">📅 03:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146969">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
مرز شلمچه به دستور نخست وزیر عراق رسماً به روی ایران بسته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/146969" target="_blank">📅 03:26 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146968">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
برآورد شده در دو دهه برای تاسیسات تپه علی طاهر بالای 2 میلیارد دلار هزینه شده است که خب مشخصه از کجا تامین شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/146968" target="_blank">📅 01:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146967">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f254d9cb95.mp4?token=e6fZ3eE7H_XMtYBgeokkNaR8PsTSo8sUTxZs9LkU3XKo2OT1xHwsqqxNOz_lF8Tm2L7Kn0t4AXsMY7PbwmkU1KnBufmC6ado1d3QmN_7YtIK5BHq7tCsRChMbV-4kjzuF2z-NU7zJl4qbY1ddsLpC1pbdZQInLtWix0gfnnYmGewPrM5IeVCaM4845haFcJ3B5IGjuHtA6X21KZAz9Qd7eT7TgmD2r3W7gvqyBl_iZ1m6F2Z-F91H2b-dEjysqCCR6zF-BLuF_9q90-bVmwgrD1KDOtAYoQWFcvR1aQS0RXwyrNpzzp7pkblXvVawCK1-sBG_GDhcyQmsDgD2-N9OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f254d9cb95.mp4?token=e6fZ3eE7H_XMtYBgeokkNaR8PsTSo8sUTxZs9LkU3XKo2OT1xHwsqqxNOz_lF8Tm2L7Kn0t4AXsMY7PbwmkU1KnBufmC6ado1d3QmN_7YtIK5BHq7tCsRChMbV-4kjzuF2z-NU7zJl4qbY1ddsLpC1pbdZQInLtWix0gfnnYmGewPrM5IeVCaM4845haFcJ3B5IGjuHtA6X21KZAz9Qd7eT7TgmD2r3W7gvqyBl_iZ1m6F2Z-F91H2b-dEjysqCCR6zF-BLuF_9q90-bVmwgrD1KDOtAYoQWFcvR1aQS0RXwyrNpzzp7pkblXvVawCK1-sBG_GDhcyQmsDgD2-N9OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درگیری‌ها در مأرب، در استان تعز، همچنان ادامه دارد
و گزارش‌ها حاکی از آن است که
نیروهای شورای رهبری ریاستی (PLC) از شهر عقب‌نشینی کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/146967" target="_blank">📅 01:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146965">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kqDra4pjTx-IMr7uRVlxVS5mtIKGRiZ-IOY-XI-dUzX3csHFtdoKgqjWIcPNE0DLEuDsmHKU6ZVN4ZQvNfsZFeEEk1W3R5kaj8Gpo1673O7FbQ7IN2CJ9SZLyapvfDArymSVblHSm3cZA-jSpfitBhoU22-dxaphKtsbxJ4w6K89z93mumfsdxmiQ2WpEBDRtS3nnIXzlDvWp1q5TYBAvruyujb-DjGpSF3ZHoPGW6tSqG_GCIZHmdn82LBFhaGLVBT2Fz683k8a935gWPstK4pmbXmFRUKmmUt51ZmPSP00lqDBnlr1Sl-ta9W8ctdyQAARKiNS7OrJ-yx3o4f9Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b1eGeGWL9qB0_zkXt3EOY7D7rNd8Zkdo-qshaAKMYMjL1kY-4S1GAGZ5JIL9_v4Mo2tRxq2tSrZodONjbiwsyE1hP-cVyeSpepeGSMZieRfihSpKCI8Jbq7n9UtUd-AvWg4IgPTFv3KWcc6UATOSw8mEyI99WEa27GVb3UXH3ctb7lL_e2Kq3earuqkXm7LJT9-dhjTop2HXDaYWVowBSwoy7d0I4RPh1xejwBXFQaT7aUceG3xg_yOBYLUQ1bJEdn7FDBaP2NhIAjuKL51Z75jDFgko8nGbwh5CaXk6c_VbPkTPN6ZlOCJPbs7XSjdGlz5i2PU9aVs0pX2tRRKG_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
برخی منابع ادعا کردن که تابناک گفته بخشی از اموال علی کریمی در ازای تخریب رضا پهلوی آزاد شده ولی سریعا پاک کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/146965" target="_blank">📅 00:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146964">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4ec3edad5.mp4?token=bgISn63jlx1rUqfMfFqiLh0tq57cxe6Oqt9AlzrRjksRPD0mvDAIq3l8ptSciDcQAv7gIb_Tfv4TVvohnwUQ5C0gLf_DBsEPVz_s0xX8g2BwxCz7cLnUEyZoVc6pHdHW_1RZiEMJj24ulXANKGEpuWoNmKGz-cLC8E46i9JCyd2sWntyELfYMEctGn_KY-BCK9W3XVrkslTplTlqff5SZ2Dti1g7ch39KcznWnyZbTSpP_DjLGsptRGaI0FbPu3Z1fsjWJY4ZuYxqfmup3AAv-dyaF2o010tggVeFild6AVOQNJUyH7TAXiL3ugOkusoimn_BOaOymtrJieCppiM-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4ec3edad5.mp4?token=bgISn63jlx1rUqfMfFqiLh0tq57cxe6Oqt9AlzrRjksRPD0mvDAIq3l8ptSciDcQAv7gIb_Tfv4TVvohnwUQ5C0gLf_DBsEPVz_s0xX8g2BwxCz7cLnUEyZoVc6pHdHW_1RZiEMJj24ulXANKGEpuWoNmKGz-cLC8E46i9JCyd2sWntyELfYMEctGn_KY-BCK9W3XVrkslTplTlqff5SZ2Dti1g7ch39KcznWnyZbTSpP_DjLGsptRGaI0FbPu3Z1fsjWJY4ZuYxqfmup3AAv-dyaF2o010tggVeFild6AVOQNJUyH7TAXiL3ugOkusoimn_BOaOymtrJieCppiM-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمک نشناس مثل چادی هوپان
قبل و بعد قهرمانی
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/146964" target="_blank">📅 00:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146963">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
شبکه خبری ABC آمریکا به نقل از مقامات آمریکایی:دولت عربستان سعودی در روزهای اخیر آمادگی خود را برای انجام یک عملیات نظامی گسترده علیه حوثی‌ها اعلام کرده است، حتی اگر لازم باشد به تنهایی وارد عمل شود. با این حال، ریاض هنوز تصمیم نهایی در این زمینه را اتخاذ نکرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/alonews/146963" target="_blank">📅 00:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146962">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c414beafb6.mp4?token=oYsFM024yrzGVRcgU1vTr6qc5y9H74yb_zzXhdzmOZncrkeZbCfeQx1YXr8BUVUYliFWWdw8trvXzD8m-ZT7WQ_V8_bGmX5GAfRU_ei2y_-kw8c2sTmCgsFe7otsLsh5fhHAU4KvnkX7iytuUzGCmGreyG8bVDRvVGy5KQLQOy0x3ROWrQcE8Yg2h86gUFqZxFJYnJd1FxOFlEVMszIJzadz9uZT_vMU9xoHjxfS6BC834nrtqVE6GW6lOJVww1FCitNCbIXs-paxToG7tT_aIBlaPYatOaV8lLybRaj4rMr9c-tLrX9cKrYq1U8pRsIbNZMD3zEHzQYxdIwT0rhBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c414beafb6.mp4?token=oYsFM024yrzGVRcgU1vTr6qc5y9H74yb_zzXhdzmOZncrkeZbCfeQx1YXr8BUVUYliFWWdw8trvXzD8m-ZT7WQ_V8_bGmX5GAfRU_ei2y_-kw8c2sTmCgsFe7otsLsh5fhHAU4KvnkX7iytuUzGCmGreyG8bVDRvVGy5KQLQOy0x3ROWrQcE8Yg2h86gUFqZxFJYnJd1FxOFlEVMszIJzadz9uZT_vMU9xoHjxfS6BC834nrtqVE6GW6lOJVww1FCitNCbIXs-paxToG7tT_aIBlaPYatOaV8lLybRaj4rMr9c-tLrX9cKrYq1U8pRsIbNZMD3zEHzQYxdIwT0rhBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره بازسازی مرکز تجارت جهانی:  پیشنهاد من این بود که دو ساختمان یکسان ساخته شوند و ارتفاع آن‌ها ۱۰ طبقه بیشتر باشد.
🔴
به نظر من، این کار می‌توانست یک اقدام بسیار عالی باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/146962" target="_blank">📅 00:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146960">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
برای مردن در ایران حدود 1 میلیارد پول نیاز دارید که خرج کفن و دفن بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/146960" target="_blank">📅 00:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146959">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2693036490.mp4?token=oo2BspfD_lmgi74-c42VdWYL_RD_Sz8jN8dwyTcITByCTwH_VbiRHNtKyC0OYQGd7I86BRwnyuh_voqwfQTGTOwsLAnKtQiDvj00XZNG36HrojXzS-A2opl5L6C4OkoeAUiv1V62rYdlEDFE0lnU86Ab0D_GGagTDe3hjMiGnuVJnbqRcNo0dT8-Aer3jRxDxJO8KX5WDHdt6dv9e19EnuAgCynTrSptdPyV00Mzhw2dBNGiMZLE_LoPbzDhQ4jdAXWo355J3ZJfCpTa3Mm1ykEWptvcdxYLXr8Fyga55L5tw-wT6-ZwZ_-SXLtECC6FAwrPYjJY9lAUCAA8DEdjMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2693036490.mp4?token=oo2BspfD_lmgi74-c42VdWYL_RD_Sz8jN8dwyTcITByCTwH_VbiRHNtKyC0OYQGd7I86BRwnyuh_voqwfQTGTOwsLAnKtQiDvj00XZNG36HrojXzS-A2opl5L6C4OkoeAUiv1V62rYdlEDFE0lnU86Ab0D_GGagTDe3hjMiGnuVJnbqRcNo0dT8-Aer3jRxDxJO8KX5WDHdt6dv9e19EnuAgCynTrSptdPyV00Mzhw2dBNGiMZLE_LoPbzDhQ4jdAXWo355J3ZJfCpTa3Mm1ykEWptvcdxYLXr8Fyga55L5tw-wT6-ZwZ_-SXLtECC6FAwrPYjJY9lAUCAA8DEdjMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کانادا: یکی از دوستان من نتوانست یک هواپیمای گلف‌استریم را در کانادا بخرد، به دلیل یک قانون خاص که در آنجا وجود داشت.
🔴
من بلافاصله تعرفه‌های سنگینی را بر روی شرکت بمباردیه اعمال کردم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/146959" target="_blank">📅 00:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146958">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
درگیری‌ها بین نیروهای انصارالله و نیروهای همسو با شورای انتقالی جنوب (PLC) در شمال غربی شهر مأرب، منطقه‌ای که تحت کنترل شورای انتقالی جنوب قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/146958" target="_blank">📅 00:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146957">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
ترامپ: من رأی اعراب در میشیگان را به دست آوردم؛ اتفاقی که قبلاً هرگز رخ نداده بود.
🔴
رامنی فقط ۲ درصد رأی آن‌ها را گرفته بود و هنوز هم دنبال این هستند که بفهمند آن ۲ درصد چه کسانی بودند! هیچ‌کس نمی‌تواند پیدایشان کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/146957" target="_blank">📅 23:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146956">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
المیادین به نقل از یک منبع ارشد ایرانی: مذاکره تا زمان پذیرش شروط ایران امکان‌پذیر نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/146956" target="_blank">📅 23:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146955">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
سنتکام: از آغاز محاصره علیه ایران، مسیر ۹۹ کشتی تجاری را تغییر دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/146955" target="_blank">📅 23:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146954">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfec33d636.mp4?token=Fu1aw62H9igZV6qipBF5hikcQhvl2S3oQSoa1Yc4Zo7Wo2UlN7acEhH4g-1AM9xzx3_77xGf5R2NzCy6PGoOdt_IokqBlRDB_0wZp2fpqOW21vu_RMjRQKTAVLcWU41ckjzYenI-8eNmrBok0sBykfBXx0oGIZrKIlMyOyujZhpfCv_EahGsdtMX1HyqUV-Gwvy5VwDAYEh3_Aw8Jd16HJmhY50UPcJ_N8xWNvdWjuRKnwUaQWvoKJKWl6N9RYUOi71tvgnQ0_ejCIs6wguKcMIJIZCL0TUhIq9mVTkBH2gTjoSIbJTTsCtqQ6V_7612IaiSkKo1V5hciFV6rV65JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfec33d636.mp4?token=Fu1aw62H9igZV6qipBF5hikcQhvl2S3oQSoa1Yc4Zo7Wo2UlN7acEhH4g-1AM9xzx3_77xGf5R2NzCy6PGoOdt_IokqBlRDB_0wZp2fpqOW21vu_RMjRQKTAVLcWU41ckjzYenI-8eNmrBok0sBykfBXx0oGIZrKIlMyOyujZhpfCv_EahGsdtMX1HyqUV-Gwvy5VwDAYEh3_Aw8Jd16HJmhY50UPcJ_N8xWNvdWjuRKnwUaQWvoKJKWl6N9RYUOi71tvgnQ0_ejCIs6wguKcMIJIZCL0TUhIq9mVTkBH2gTjoSIbJTTsCtqQ6V_7612IaiSkKo1V5hciFV6rV65JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور تد کروز درباره اسرائیل: می‌توانید دولت اسرائیل را نقد کنید و ضدیهودی نباشید.
🔴
اما به شما می‌گویم: صددرصد ضدیهودیان، ضداسرائیل هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/146954" target="_blank">📅 23:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146953">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d902513f5.mp4?token=cxFdfmEpir5f2nnsLpiyEhsEv9-MRaZ0_6lwr-smZ86NchqJBME2L-X-O-8L96bxh3HGj1ZrUEsMoF1139SMggZptKqjc_A78GwPMna-1J3IsIUgCgVQeFP6n5vIUYtqtl6RLiqAwOP1by9AI2YJKymrQKqdbC97xkuCGcJ6Wc76EFzsrms94K_fJx2uLAk4ejj93wnPzNLSjVqMUwtKWDfOSAeuxBCJmIx-rp0Wk-OpRUHsJ4fJsECbluaL5irCTlOOLbHKiB7iRCaJKvW54OOA_FEkOjlD_aRJQlbYwoJsI-5HSrRsK90jYbsRfmnzT4pdqnoUUMT9KPINoB6PAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d902513f5.mp4?token=cxFdfmEpir5f2nnsLpiyEhsEv9-MRaZ0_6lwr-smZ86NchqJBME2L-X-O-8L96bxh3HGj1ZrUEsMoF1139SMggZptKqjc_A78GwPMna-1J3IsIUgCgVQeFP6n5vIUYtqtl6RLiqAwOP1by9AI2YJKymrQKqdbC97xkuCGcJ6Wc76EFzsrms94K_fJx2uLAk4ejj93wnPzNLSjVqMUwtKWDfOSAeuxBCJmIx-rp0Wk-OpRUHsJ4fJsECbluaL5irCTlOOLbHKiB7iRCaJKvW54OOA_FEkOjlD_aRJQlbYwoJsI-5HSrRsK90jYbsRfmnzT4pdqnoUUMT9KPINoB6PAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: هیچ‌کس فکر نمی‌کرد توماس ماسی می‌تواند شکست بخورد.
🔴
او با اختلاف ۱۹ امتیاز شکست خورد و از بین رفت، بنابراین من به این افتخار می‌کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/146953" target="_blank">📅 23:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146952">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: ما در وضعیت «نه‌ جنگ، نه‌ صلح» نیستیم؛ ما در وضعیت جنگ هستیم
🔴
تحریم و محاصرهٔ دریایی به منزلهٔ جنگ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/146952" target="_blank">📅 23:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146951">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b7d6fd0c1.mp4?token=q-7uJwLa-932ZurvDEksIInDEcXRBjNypmzhgcNjpO1lieB_cxrF831IMmuroOEOUlbBdRUssnIFwjNfmpdPzAeTvUE7o74dbGk2kOOxNj4CXnRUngKJbHhJGr1Ir86hNuQaQWEVHtTpt5vxYmNLtz509qrcRimOpnErShHJRFIb0h5top8q1fkD2ijhPwKjiFEZyIxWfqLpgNXh_B5yvWd3XR-v__rPwSghhBJzbpc6Lf5F8mZiHLAKkrwcjAIVFnTmlq4zJshFJ6FUydlMZB4Tun7zfF2pv87Njd8xsvNdzROOgDI6nkluTjOF2V_99ysEAVGkopleLGcXbYg_og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b7d6fd0c1.mp4?token=q-7uJwLa-932ZurvDEksIInDEcXRBjNypmzhgcNjpO1lieB_cxrF831IMmuroOEOUlbBdRUssnIFwjNfmpdPzAeTvUE7o74dbGk2kOOxNj4CXnRUngKJbHhJGr1Ir86hNuQaQWEVHtTpt5vxYmNLtz509qrcRimOpnErShHJRFIb0h5top8q1fkD2ijhPwKjiFEZyIxWfqLpgNXh_B5yvWd3XR-v__rPwSghhBJzbpc6Lf5F8mZiHLAKkrwcjAIVFnTmlq4zJshFJ6FUydlMZB4Tun7zfF2pv87Njd8xsvNdzROOgDI6nkluTjOF2V_99ysEAVGkopleLGcXbYg_og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور جمهوری‌خواه تد کروز درباره ایران: هر زمان که یک تعارض نظامی در خاورمیانه رخ دهد، قیمت‌های بنزین بالاتر خواهند رفت.
🔴
و ترامپ تصمیم گرفت که الزامات امنیت ملی برای جلوگیری از دستیابی ایران به سلاح هسته‌ای آن‌قدر مهم هستند که تحمل برخی هزینه‌های اقتصادی کوتاه‌مدت ارزش آن را دارد.
🔴
من فکر می‌کنم که این یک تصمیم مسئولانه بود که ایمنی آمریکا را افزایش داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/146951" target="_blank">📅 23:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146950">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85f29b9673.mp4?token=Dm9Asw_R3TzL-4QtxN-1YsfF-L_inhPwnKq1_wJjgNLAADy08x9curTe8-QKwWjkfIeS-bI2nglWfyIKafdxoH5xY38vHEWQ0UOwOhE1aiBbKKekPQ7NVyJA2ia0gxCVt3Ivnr41qEXKIl9GMuyJDG7BDoR66clvgHfhAbJ_F3LpAB0rGXzoooB9h7Zv8Yoi1lOrb56ar7e_HDSKUvJ-8IIn89QUecySU8kapzLjaxezSNZ6CDzO60UVOXPsEQ8meajQaZ6ElhypapnCB7R9X4K04Zh1kbR8dET6vLGGNW7uNF4TolvMqXKqpxQjjGtcvMnhW5OqLgBaWF8fYMVvCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85f29b9673.mp4?token=Dm9Asw_R3TzL-4QtxN-1YsfF-L_inhPwnKq1_wJjgNLAADy08x9curTe8-QKwWjkfIeS-bI2nglWfyIKafdxoH5xY38vHEWQ0UOwOhE1aiBbKKekPQ7NVyJA2ia0gxCVt3Ivnr41qEXKIl9GMuyJDG7BDoR66clvgHfhAbJ_F3LpAB0rGXzoooB9h7Zv8Yoi1lOrb56ar7e_HDSKUvJ-8IIn89QUecySU8kapzLjaxezSNZ6CDzO60UVOXPsEQ8meajQaZ6ElhypapnCB7R9X4K04Zh1kbR8dET6vLGGNW7uNF4TolvMqXKqpxQjjGtcvMnhW5OqLgBaWF8fYMVvCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کانادا: کانادا سال‌هاست که از ما کلاهبرداری کرده است.
🔴
آن‌ها سخت‌ترین مردم برای انجام کسب‌وکار هستند. آن‌ها فکر می‌کنند حق دارند.
🔴
آن‌ها باید یک ایالت باشند. می‌دانید، اگر یک ایالت بودند، ما مشکلی نداشتیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/146950" target="_blank">📅 23:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146949">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
خط فقر برا خانواده های ۴ نفره به ۱۰۰ میلیون تومن رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/146949" target="_blank">📅 23:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146948">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b10559faa.mp4?token=dkFf4-d3wgZWRqB3PODuv8luD8R_HhvYeWwRLHxnrf55Fe6fflj3ea5xnx76QPQ4GMD5F6Ibj6_htGKRxwk-5teivduN-bBWRbRaP-8coROyuUztMLydcw77RQ0zCLeuCtUS4C6OeRgfIjEvqDCzB217QHT1CZq7-xeCi9WgMOUGQqDzHWetyNoHi7pRMrEbdzdvyuahYuxTNYymwIaLsv1gfzBNUZg1_oYbN7t9qHsVBkhYvOUwGOAlBONPO7CvteIMncHzVzPMFNiZYMLAzXuKxXtdsTjjwHAbRe99EgjzZVGsB6RWB6WhFZHmb1iyhFG8ctJqHFJ8MSN7nysXcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b10559faa.mp4?token=dkFf4-d3wgZWRqB3PODuv8luD8R_HhvYeWwRLHxnrf55Fe6fflj3ea5xnx76QPQ4GMD5F6Ibj6_htGKRxwk-5teivduN-bBWRbRaP-8coROyuUztMLydcw77RQ0zCLeuCtUS4C6OeRgfIjEvqDCzB217QHT1CZq7-xeCi9WgMOUGQqDzHWetyNoHi7pRMrEbdzdvyuahYuxTNYymwIaLsv1gfzBNUZg1_oYbN7t9qHsVBkhYvOUwGOAlBONPO7CvteIMncHzVzPMFNiZYMLAzXuKxXtdsTjjwHAbRe99EgjzZVGsB6RWB6WhFZHmb1iyhFG8ctJqHFJ8MSN7nysXcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره جمهوري
ایران: اگر کاری که من انجام می‌دهم را انجام ندهید، آن‌ها یک سلاح هسته‌ای خواهند داشت.
🔴
اگر یک سال و نیم پیش با بمب‌افکن‌های B-2 آن‌ها را به‌شدت بمباران نکرده بودم، الان یک سلاح هسته‌ای داشتند. و از آن استفاده می‌کردند.
🔴
اسرائیل از بین می‌رفت. خاورمیانه از بین می‌رفت.
🔴
شما این را از آن واقعیت می‌بینید که رژیم ایران تمام آن بمب‌ها را رها کرد. من منظورم این است که مردم، مانند عربستان سعودی، متعجب شدند. همه شوکه شدند که به جای آن (موشک‌ها) از یک سلاح هسته‌ای استفاده کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/146948" target="_blank">📅 23:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146947">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d866f8f748.mp4?token=OtnaMGJ5_IFuo5Y5tFwCyBs9-fESobcGmKcAYCuszV9vTsRtr1fapsFgyD7v8ohua2AO3aLpQqX92GAllk7keKVNTGCw6tmkKNc66oDC8dGG0VAbz2Y_VW825Gj1qavS2Fo6hzTZpHdKmuSCqrk5fYq8IWV52yVMQlRh5YPGbpR0Suqm_iqXYQ87k4sMMakqMjhjItqYiqicUI2lN7uN6zPqt2bTTfWrcQRLyoOApnqgi5QAzl4QtQWKwhE-ZcLcW-FbfNpt62RFxq_32TWBovQCd3oyTYX2q046noN8cKIvChwKbzZGjPuZtEssvt2URWcw8OZvAV198P3I2BmO4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d866f8f748.mp4?token=OtnaMGJ5_IFuo5Y5tFwCyBs9-fESobcGmKcAYCuszV9vTsRtr1fapsFgyD7v8ohua2AO3aLpQqX92GAllk7keKVNTGCw6tmkKNc66oDC8dGG0VAbz2Y_VW825Gj1qavS2Fo6hzTZpHdKmuSCqrk5fYq8IWV52yVMQlRh5YPGbpR0Suqm_iqXYQ87k4sMMakqMjhjItqYiqicUI2lN7uN6zPqt2bTTfWrcQRLyoOApnqgi5QAzl4QtQWKwhE-ZcLcW-FbfNpt62RFxq_32TWBovQCd3oyTYX2q046noN8cKIvChwKbzZGjPuZtEssvt2URWcw8OZvAV198P3I2BmO4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره تاکر کارلسون: من می‌گویم که تاکر کارلسون هرگز از من خوشش نمی‌آمد. من به نوعی کارهای زیادی برای او انجام دادم.
🔴
من و تاکر رابطه‌ای بسیار نوسانی داشته‌ایم.
🔴
نکته جالب این است که او نسبت به جنگ حساسیت دارد. بیشتر با من و جنگ. اما باید درک کنید که ایران نمی‌تواند سلاح هسته‌ای داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/146947" target="_blank">📅 23:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146946">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d78dd6d27.mp4?token=ErRVlz-uU9-Y6FJmPcnUdSOQvpIaGzruzyWJH9bErfrQq-B_4epqh_z32dIs_wrqdaRNbucVzCf-8COCQjHNmxm251vqc3sqfmN5FnUPQd8RVRyDdahnPTOzaYstcFFU_y5R06axivhfeGKRNUwQp2maEJlSQ5-LkBvo1giqVMidmad_knMzrWaik3F01mFfNXbpcRg36Zmxs86pNIDE44_2Hzntpj50m7Klr1VqbJR6HPG3o1JEtsIS8kNLyJapGKno1iTWOywAD3f2ixyQPlxqOAUpcvjOH8UROGiAJiVBtp252kgZ0ZLNYZs0h7yWlLzorngr3CinFUb0vlwRPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d78dd6d27.mp4?token=ErRVlz-uU9-Y6FJmPcnUdSOQvpIaGzruzyWJH9bErfrQq-B_4epqh_z32dIs_wrqdaRNbucVzCf-8COCQjHNmxm251vqc3sqfmN5FnUPQd8RVRyDdahnPTOzaYstcFFU_y5R06axivhfeGKRNUwQp2maEJlSQ5-LkBvo1giqVMidmad_knMzrWaik3F01mFfNXbpcRg36Zmxs86pNIDE44_2Hzntpj50m7Klr1VqbJR6HPG3o1JEtsIS8kNLyJapGKno1iTWOywAD3f2ixyQPlxqOAUpcvjOH8UROGiAJiVBtp252kgZ0ZLNYZs0h7yWlLzorngr3CinFUb0vlwRPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ دربارهٍ تاکر کارلسون
:
من تاکر کارلسون را از مدت‌ها پیش می‌شناسم و رابطه‌ام با او بسیار نوسانی بوده است. او بسیار ناسازگار است. و شاید من هم همین‌طور باشم، اما به شما می‌گویم، او بسیار ناسازگار است.
🔴
او بسیار یک فرد فرصت‌طلب است. البته، چند ماه پیش او را رها کردم چون احساس می‌کردم این کار نامناسب است.
🔴
او چیزهای بدی، چیزهای بسیار بدی می‌گفت. نه لزوماً دربارهٍ من، بلکه دربارهٍ بسیاری از چیزهای دیگر که در حال وقوع هستند.
🔴
او به افرادی مانند مارک لویین، که من فکر می‌کنم عالی هستند، و دیگران حمله می‌کرد. شخصاً، من از این موضوع خوشم نمی‌آمد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/146946" target="_blank">📅 23:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146945">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/612e19ba40.mp4?token=BxXHHrlqdq3uKrmnbJwX23qY0VWUIedHaJ5q5OdwUjkEcsrQyFHc00moPpER6Hl00psaYEdXjEDqz_8R9y_ZjcvXWC7-OM-1CfqUkYx6tyT6e1xs9ITNumrCdz3J0oTUXPaTMbpeS-PGtbcOmYfj7rlMSG026lPQ1EFoWyc8bqOmpMAViBJU_yqbBa8DB_IQTxcybjuel1dsqGc5riMHYe7o7VvJeZ4aWcllC8ZtTNRpHttJrrAGsQE0U_tYZkX6Jeu5dGv6rTTDrs4CHnxsTjgR2Ymg3H3XgmztlvsPyHOwVHvk8Y56ZwqDyzJ8GPw2L5n0TTiBy9OUHXfIwQciHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/612e19ba40.mp4?token=BxXHHrlqdq3uKrmnbJwX23qY0VWUIedHaJ5q5OdwUjkEcsrQyFHc00moPpER6Hl00psaYEdXjEDqz_8R9y_ZjcvXWC7-OM-1CfqUkYx6tyT6e1xs9ITNumrCdz3J0oTUXPaTMbpeS-PGtbcOmYfj7rlMSG026lPQ1EFoWyc8bqOmpMAViBJU_yqbBa8DB_IQTxcybjuel1dsqGc5riMHYe7o7VvJeZ4aWcllC8ZtTNRpHttJrrAGsQE0U_tYZkX6Jeu5dGv6rTTDrs4CHnxsTjgR2Ymg3H3XgmztlvsPyHOwVHvk8Y56ZwqDyzJ8GPw2L5n0TTiBy9OUHXfIwQciHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: امنیت منطقه باید با گفت‌وگو میان کشورهای منطقه و بدون حضور بیگانگان تأمین شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/146945" target="_blank">📅 22:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146944">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
وزارت خارجه: عربستان، ژاپن و اردن تبعات رای مثبت خود به قطعنامهٔ ضدایرانی آژانس را خواهند دید و ما آن‌ها را پاسخگو خواهیم کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/146944" target="_blank">📅 22:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146943">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be896fba71.mp4?token=ChPOT9VpprC0BXw6ghqsfKEtoGfKkxyvn9PwnBpStt4fQlgSswB7ZBpUVQ6G9vLLdJit8-uhX9DqLn1YflgxS8S47HqTKwBXCXoFtbyUKtW_jyptrWj07qPZ1UKxQ45rwFuFwTcMlBv88gfCuJUiEo3K59w8WPS0UcaltUz1dfLhBFJnlWcSodRBJjNV0kLUmnTjjBop7d214lzDzj4IOKUhWG_h2-eEcTQddg657vRjR4X83SQMX-pumHxx4j-pRDiEUvxwVRhu3LWCPAaUI0HGWd6abl0JnSsTAxGqPSJWOaMqwJbazUowWNl1G6W0qT555aVRFndanvD4b2AZrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be896fba71.mp4?token=ChPOT9VpprC0BXw6ghqsfKEtoGfKkxyvn9PwnBpStt4fQlgSswB7ZBpUVQ6G9vLLdJit8-uhX9DqLn1YflgxS8S47HqTKwBXCXoFtbyUKtW_jyptrWj07qPZ1UKxQ45rwFuFwTcMlBv88gfCuJUiEo3K59w8WPS0UcaltUz1dfLhBFJnlWcSodRBJjNV0kLUmnTjjBop7d214lzDzj4IOKUhWG_h2-eEcTQddg657vRjR4X83SQMX-pumHxx4j-pRDiEUvxwVRhu3LWCPAaUI0HGWd6abl0JnSsTAxGqPSJWOaMqwJbazUowWNl1G6W0qT555aVRFndanvD4b2AZrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: محدودیت دسترسی آژانس نتیجه حمله به تأسیسات هسته‌ای ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/146943" target="_blank">📅 22:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146942">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8466606615.mp4?token=cM9wOKEf4nwVbgdtY4gtGQuR8DV_8Rh602e9O2CiFjiVYJuSCkZ5O_VhqXj0JuyY1u5yW0D0SBJWIPdS_7eFH2yVWA9Gt2EsNuKSnLGtB6rk0g2o6ZLmuuExP4q_fSyOZk7ujcsnWdTO7uft_yvd8-GCCCgAaWovqQU76UhNWLSdgXlGq_XDP-pw65j2FD51sLL0qxK7HzdV8cgyKN5EYVs-NJWRGdNo2VC8jFjC4SrCl7mIIw3r_9DsH3rZKy4QT6Ia0HB5FNORicSr584hoBGUAA1cQgQjGjzeiINhE1gTMqWPY40X9F69V_B4UqUa4NU_JiWpwboq-DL6mzBvpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8466606615.mp4?token=cM9wOKEf4nwVbgdtY4gtGQuR8DV_8Rh602e9O2CiFjiVYJuSCkZ5O_VhqXj0JuyY1u5yW0D0SBJWIPdS_7eFH2yVWA9Gt2EsNuKSnLGtB6rk0g2o6ZLmuuExP4q_fSyOZk7ujcsnWdTO7uft_yvd8-GCCCgAaWovqQU76UhNWLSdgXlGq_XDP-pw65j2FD51sLL0qxK7HzdV8cgyKN5EYVs-NJWRGdNo2VC8jFjC4SrCl7mIIw3r_9DsH3rZKy4QT6Ia0HB5FNORicSr584hoBGUAA1cQgQjGjzeiINhE1gTMqWPY40X9F69V_B4UqUa4NU_JiWpwboq-DL6mzBvpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره بازسازی مرکز تجارت جهانی: پیشنهاد من این بود که دو ساختمان یکسان ساخته شوند، اما ارتفاع آن‌ها را 10 طبقه بیشتر کنند.
🔴
به نظر من این کار، یک اقدام عالی می‌بود.
🔴
آن‌ها این کار را به روش دیگری انجام دادند، و این مسئله قابل قبول است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/146942" target="_blank">📅 22:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146941">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feb351c81b.mp4?token=uBa93Uxfbf8-NTjEcixxY56RbP6hk1vN-B_o9PTSfkbj0D4KYGzsx-A7iR_BcZHCH4nlM-QFGE__AjgHeImbTz4-VUPPx4dkJB0K5cOkU3HEX1GuItXHnQHnmfIo8zDRRhKyEL-Hm8pePk_-uO_Lc5e98szNIaSbimucA5mnY8dweTrIPQUNbXsbY-FsaQUxW-8CSCV9UcvctTbrNAOZCMlV7rTN8KR2ZdhmIvUynTIAryGBGxzQtx-q7dbtZADw7qMnjkjGLLFgGXX-821eoznkBGmI2sVgDADUn2eGF18S7mNsreNO2Bq6uG5Pb39T5b8kTqroyOwoqPIsyfT67g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feb351c81b.mp4?token=uBa93Uxfbf8-NTjEcixxY56RbP6hk1vN-B_o9PTSfkbj0D4KYGzsx-A7iR_BcZHCH4nlM-QFGE__AjgHeImbTz4-VUPPx4dkJB0K5cOkU3HEX1GuItXHnQHnmfIo8zDRRhKyEL-Hm8pePk_-uO_Lc5e98szNIaSbimucA5mnY8dweTrIPQUNbXsbY-FsaQUxW-8CSCV9UcvctTbrNAOZCMlV7rTN8KR2ZdhmIvUynTIAryGBGxzQtx-q7dbtZADw7qMnjkjGLLFgGXX-821eoznkBGmI2sVgDADUn2eGF18S7mNsreNO2Bq6uG5Pb39T5b8kTqroyOwoqPIsyfT67g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: سیاست، شگفت‌انگیز است. شما با برخی از فاسدترین افراد دنیا ملاقات می‌کنید، و همچنین با افراد فوق‌العاده‌ای نیز آشنا می‌شوید، اما در عین حال، با برخی از فاسدترین افراد جهان روبرو می‌شوید
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/146941" target="_blank">📅 22:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146940">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/40e05b07a0.mp4?token=n7HIaoijP1LC9Yz5jWWAV2ex4Ddk7JE-T9gPqEwk469wXAx4bmkd0vpV0LyYxzT8E45ugUEjP7Pc9268vWyZ5pHM745wyrbNX9eT4Ar5RP_gyYA-35E4VSgO2xPrI-437YB63ehVmyC9uiwyhSRt850TH2V2Z9eK_y82PhQGZOXe6HseKXkXAN-FPrx1h50DGkcrBS6qfOlEHmkS7HiS2lukBUo6zVxMJKepE06jYsG1aG0SASbLsjjzXSJuyYjcvgVnLrWo8nSURhpZ1EkgSqXlD6gqD0jBKElkJxVwyhfk_-ePHKUQgtztV1tS4DTHzxBouqXj5wxof2jL7fvuiw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/40e05b07a0.mp4?token=n7HIaoijP1LC9Yz5jWWAV2ex4Ddk7JE-T9gPqEwk469wXAx4bmkd0vpV0LyYxzT8E45ugUEjP7Pc9268vWyZ5pHM745wyrbNX9eT4Ar5RP_gyYA-35E4VSgO2xPrI-437YB63ehVmyC9uiwyhSRt850TH2V2Z9eK_y82PhQGZOXe6HseKXkXAN-FPrx1h50DGkcrBS6qfOlEHmkS7HiS2lukBUo6zVxMJKepE06jYsG1aG0SASbLsjjzXSJuyYjcvgVnLrWo8nSURhpZ1EkgSqXlD6gqD0jBKElkJxVwyhfk_-ePHKUQgtztV1tS4DTHzxBouqXj5wxof2jL7fvuiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رسانه‌های نظامی ارتش ملی یمن، تصاویری از حملات هوایی مشترک یمن و عربستان سعودی را منتشر کرده است که اهداف آن، خودروهای وابسته به جنبش انصارالله در منطقه ضباب و مناطق جنوب غربی یمن تحت کنترل این جنبش بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/146940" target="_blank">📅 22:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146939">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LURPw-PysA9nZWqSfbd7njuSsYEI740j-MIkl7-IusMknvThEd0g-0Ceh5klOT3nHvSwuMBpVVCLNu0EIEvsk5Ym4htZf6A6tzJO5Ne7nX_O_OgL2BQZ-m-2M99ZtJD527uI2PeOVvyDGxULx3Ij4uu-Oe0Ec9LMU6w95xcM9dlknEHsOgV2VXAwMT8L17rgfquJcgh7W8H6_C3jCnplAHyHfohbV9XjEflDS08x4tIPawVp4g9BjE3y0UdM-fQlI6X3PC8XylhWRtMJsCiQlWyKwqK5NSIwMn_biEj01qiBKWGs-Pd396u90j9uZVN1Q5uMZbGIcSe1JIVQ1_L6kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : بخشش ۵۰۰۰ دلاری ترامپ"، که به همه بزرگسالان در ایالات متحده تعلق می‌گیرد، به این دلیل ارائه می‌شود که کشور ما میلیاردها دلار در زمینه توسعه اقتصادی، سرمایه‌گذاری و موفقیت خالص به دست آورده است. این موضوع از سوی "دموکرات‌ها" مورد انتقاد قرار می‌گیرد، زیرا آن‌ها امیدوارند که این اتفاق هرگز رخ ندهد - اما این اتفاق خواهد افتاد!
🔴
به عنوان مثال، دموکرات‌ها در مورد "قانون بزرگ، زیبا و باشکوه"، یکی از بزرگترین قوانینی که تا به حال توسط کنگره تصویب شده یا توسط یک رئیس جمهور به قانون تبدیل شده است، این ادعا را مطرح کردند که این قانون تصویب شده است، در حالی که دموکرات‌ها می‌گفتند که تصویب آن غیرممکن است. یا "هدیه ۱۷۷۶ دلاری" که سال گذشته به ارتش ما دادم، تقریباً از همان ابتدا با مخالفت روبرو شد. همه می‌گفتند که این کار امکان‌پذیر نیست، اما این کار انجام شد. سربازان وطن‌پرست ما این پول را دریافت کردند و از آن راضی بودند.
🔴
وقتی من چیزی را می‌گویم، منظورم را کاملاً می‌دانم. بخشش ۵۰۰۰ دلاری اتفاق خواهد افتاد، زیرا مردم کشور ما شایسته آن هستند. به حزب جمهوری‌خواه رای دهید - و آمریکا را دوباره شکوه بخشید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/146939" target="_blank">📅 22:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146938">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
مدتی پیش، هواپیماهای جنگی اسرائیل حملاتی را به مناطق قانترا، المنصوری، زبکین و نباتیه الفوقا در جنوب لبنان انجام دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/146938" target="_blank">📅 22:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146937">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc6c5ed95a.mp4?token=Ye44oxtYfu9yY8Ibbp-BZGJYybyXY8VOvNgSCI_Su6v3aTmioyJu9qiNs90KNUJzuPEgktX6O1RIyPOL0-Fdr84tmpne8SOwfYFPTxo2FQWK7HzdYvqA_9XHrZt8ARju_McSTEqxefOjg0c8Lsqymr1RpsV2XLsRvJH_dd5yNlpZX9PFRXWsI5Yd4bXHA5EG_irSGDRgtmDM0VVCLV928_ByBVEUk0RvSbC8Cu5xzpyqmff9oYl2RgXMCu7qgqWsI4gMhoBAAscahKwnDFUGrR5G_DwN3dJUGgg5ikV1KJ7GlP3y1EerAuKeIktoTwYzNkCDdX5ZflHykG6SnHBMsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc6c5ed95a.mp4?token=Ye44oxtYfu9yY8Ibbp-BZGJYybyXY8VOvNgSCI_Su6v3aTmioyJu9qiNs90KNUJzuPEgktX6O1RIyPOL0-Fdr84tmpne8SOwfYFPTxo2FQWK7HzdYvqA_9XHrZt8ARju_McSTEqxefOjg0c8Lsqymr1RpsV2XLsRvJH_dd5yNlpZX9PFRXWsI5Yd4bXHA5EG_irSGDRgtmDM0VVCLV928_ByBVEUk0RvSbC8Cu5xzpyqmff9oYl2RgXMCu7qgqWsI4gMhoBAAscahKwnDFUGrR5G_DwN3dJUGgg5ikV1KJ7GlP3y1EerAuKeIktoTwYzNkCDdX5ZflHykG6SnHBMsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: امنیت پایدار خلیج فارس تنها با همکاری کشورهای منطقه ایجاد می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/146937" target="_blank">📅 22:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146936">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WkSH3Unri9jv7I4WxGqqeDOMtcBGg1pz1Ij8ICL1oP_XpTqvWS47-5TrdgbcLAi0LTln2QN7pAnMtXrsI2bYu_-4nrsTfRomGYd-qah2erfYTTgplTcElenTQsMKmXpsEaaU5gzCMz4hHHvh7z_vgo2fdM0rlCXNByohiySH4WOHXyMLlVJuS_QeWTRn0ulSJsTygYiXdcuRcPYmwav-weGn3QaeYsbNdCMBk-HzgWu0uv4arGVt7Tchrs8wAssfK9-bU4KnZX379655FY0oSSngIcLTKF81MQAPcbmwylgDu9Sa_nt3tVpISbYSaGoYqAkMjAtSxGriFwxsRJjzAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاکستان درخواست عربستان سعودی برای حمله به حوثی‌ها را رد کرد
🔴
پاکستان می‌گوید پیمان دفاع متقابل مکه «شرایط از پیش موجود را پوشش نمی‌دهد»، بنابراین فقط جنگ‌هایی را که پس از امضای پیمان آغاز شده‌اند، پوشش می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/146936" target="_blank">📅 22:37 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146935">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/146935" target="_blank">📅 22:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146934">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: ما در وضعیت نه‌ جنگ، نه‌ صلح نیستیم؛ ما در وضعیت جنگ هستیم
🔴
تحریم و محاصرهٔ دریایی به منزلهٔ جنگ است و هر آن‌چه که ما در این وضعیت انجام می‌دهیم نامش دفاع است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/146934" target="_blank">📅 22:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146932">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImbOXWU9cuqghMCitOJlrSRE6kmvcMC6vQ21Qa8mexPnNcKkL56Hp-QwauPHWk3OaGjphVdDDkBWsQ9b5VlHN0SqPCI1RNp4tPKTbZud_JqGunZmEL2L7xuTKtwLAaG-QpxgS8hLCVWNiZ6Ak8FyGAataC4Y-Y3qjD5k3UmsoZ1HBlW7NUvKHcbJckFWJzkcgcM2l6OHvRdF06eNhk3uudX280tbZ4hohuZ9-bwzPFYd4M8CzZ8vzDUpTqR9TwdUeLrmsblxqFqOjvq-eSEh8qb-cj7gYrutXJzBmA4NV7K0ubn1Wkc1pBKPi2gRIaNdpeujVK0dUeBG16uW4YzP6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سلیمان العساد، که از اقوام بشار العساد، رئیس‌جمهور سرنگون شده سوریه، است، توسط نیروهای امنیتی لبنان در جریان یک عملیات ضد مواد مخدر در دره بقاع دستگیر شد.
🔴
دولت سوریه از دولت لبنان درخواست کرده است تا اجازه دهد او به سوریه بازگردانده شود، جایی که به ارتکاب جنایات جنگی و قاچاق مواد مخدر متهم است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/146932" target="_blank">📅 22:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146931">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
معاریو: نتانیاهو پیشنهاد حمله نظامی مشترک با کشورهای عربی به انصارالله یمن را داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/146931" target="_blank">📅 22:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146930">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvLX7KtOHPzijfTokMVzoElHlJu0mHA7DJ28ZppLYVvXB8htiNIMpR1lPxWWc8mWEkCGfBcAvBQmetOmaE7lGbSNbY9N-0eqlI16ABJ_Khcm0o7guKKrh5zQuT4YtAMWBf3vS5-2DFB5RNpeq2KQGq7zzjmxtbhCAUgTjW76nfnXXjn8cg-QotDHki1u0qJAyfqqqYWn3RcXsWVB9k8yr9cKmX0XE4kC6_tpOeaBMo2tKd7ymvIjzQTbO47AQQD5rUtMssUUOBKPXCpRK4nmYsvefOjnlVF4a3GYJfWpMudW04-juEH-AVrpoDgcQN4tljqBnx-vEvY_Qdb8n1u6vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نه نفر از خلبانان سابق نیروی هوایی سوریه، که در دوره حکومت قبلی بشار اسد فعالیت می‌کردند، توسط نیروهای امنیتی سوریه در شهر لاذقیه دستگیر شدند.
🔴
همه آنها به اتهام بمباران بی‌هدف مناطق مسکونی در طول جنگ داخلی متهم هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/146930" target="_blank">📅 22:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146929">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
طائب، رئیس سازمان بسیج: اگر دشمن درخواست مذاکره کرد، باید با قدرت و با هدف گرفتن حق با او وارد گفت‌وگو شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/146929" target="_blank">📅 22:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146928">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
وزارت انرژی عربستان سعودی اعلام کرد که به عنوان یک اقدام احتیاطی، لوله‌کشی نفتی شرق-غرب را به‌طور موقت متوقف کرده است، پس از چندین حمله به این لوله‌کشی در مناطق ریاض و مدینه در روز پنجشنبه.
🔴
این حملات همچنین منجر به زخمی شدن چندین نفر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/146928" target="_blank">📅 22:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146927">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
نماینده ایران در آژانس بین‌المللی انرژی اتمی خبر داد: برنامه بازدید بازرسان آژانس از نیروگاه بوشهر
🔴
ما به همکاری با آژانس ادامه خواهیم داد و برنامه‌ای برای بازدید بازرسان آن از نیروگاه اتمی بوشهر وجود دارد.
🔴
آمریکا معمولاً پس از تصویب قطعنامه‌ای توسط آژانس، حمله‌ای را آغاز می‌کند و این اتفاق می‌تواند در آینده نیز رخ دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/146927" target="_blank">📅 22:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146926">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJQoNvWoQbPTBAImGdp4Z0eJSfQiz10QOLW2PqS1kaSzGUHLe8z12XYYJYqxpUx_1J1R88kbDEjnBhCNREhvXl3ttPV5EBK612mK8Yao0LjP84VCcJXL3GQVGr2PsIw15vHxfpny75Z07ygfWg1DJYUDBlwBVD7xeInG82wPEGZb0HFNgt7pAfaVu5oleaiGoyEAp5zYY8-0IJOAO8CqztsLB-lGJhh6GBM_f2wY5fz1T_OEkFG2nKSUUspz7d_WdjiEItUDfvoaygYk9zKWHJhd8dSHG2NQa2WZ2d2fT2y0PZcK9E8ae63PDR6M4cWSwviXoCl62N2sIScBnjJ39w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقامات رسمی امریکایی در گفتگو با CNN هدف قرار گرفتن خط لوله جبیل-ینبع عربستان توسط پرتابه های یمنی را تایید کردند و تصاویر ماهواره ای با کیفیت نیز منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/146926" target="_blank">📅 22:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146925">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aby7y9gIYxhrT12T6riNlkI2-K8wiME6Rw_orXfbP9JBpA53UXNvCwv9FQGCdH6R9ve3h482O1OnG9rcxaUbkgvDZmY98t9tox2IaeMEKFPJUSHd6OW0ylbKUVPr3CYPS9YHRIc3XMsAAyClwCu4LqNq4xRukmao-huK8BX5H4mMuqY3orTSBIVXciA53DqlXWc53zNVcoIzPG4T0bdCYswKuEaEtg2LGlvfpRw0qh0TgvYzqLxEWhuhWgDbrhgO1iU12PMC-YTvzEYieLmP_R7e5JO2yDz-KABaqCiS_mMFhqdtp_ly7oUBjpaapcgQWlyvaAF1cjkET3ekoilrnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از پزشکیان و نخست‌وزیر هند دست در دست هم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/146925" target="_blank">📅 21:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146924">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
پزشکیان: ملت ایران بر اساس باورهای انسانی و اعتقادی خود، تسلیم فشار و زورگویی نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/146924" target="_blank">📅 21:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146923">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocv-a3GGpLSRa-Kqp77G5NdZNRSV4JIXLrA_g2KWyZQEokdXHYzo4BxnE6leRS2m0TsNXOREN1y_xXNfK85cdWOF3Bd1MIz7MCtBpZcySUxNAxOEDCBKcOKawuZqJlw-nHZuq3GjY0KrwZw7_7EbLk0mkYj6E36d-WbJjUTvDygpJYYubdhPXW_xBr_7n458Ihm_z9KpWzrm1QmMoKUdWXzlaAkZUS_d1PMNf2i86se374YIZh7lfgQyNFQpOsSCdqKr94RAvpz22M6HneOUq7yd6aRngDSas_lDUr0shqivksUbBDl2n70Cbr2IzHhYES2xQK5Ff1jfF9W1rEYKgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله علی کریمی به رضا پهلوی:
من از 13 سالگی پول درآوردم و خرج خودم و خانواده کردم
🔴
منو با کسی که پول تو جیبی از مادرش میگیره مقایسه نکنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/146923" target="_blank">📅 21:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146922">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb519e251e.mp4?token=QE-42ijNIQ0WFXZqWvyJ1qZYf-tj9PNF0KJU8pImc4wcSZS9FhEIqG8LoFz5dl3aBqAG8_IYyh-Fs216E04KW0VpUU8SWPI9_o0O7mVg90KBnABsABSJ3s1sdlZzyes8o56rqVAhLUk5f1u8W_2g5GSLSLQ_e6scUf_YVnJmkVBbIrOzAN1jktY_5HEcg8NkI4W2JO9HLw24YfwFsmBjTaKPf7ikgFKtjLcH9HQwho6h7LJGRxvRZEbDOr9XHIhRfQL5VZuzbIwMQcr5rhA_h_yo-Yr7Pn9oxu5Agdo4VFbQaqWicjm7u_r4QXGk_2xzeybGMzYwGF3YK353npU-pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb519e251e.mp4?token=QE-42ijNIQ0WFXZqWvyJ1qZYf-tj9PNF0KJU8pImc4wcSZS9FhEIqG8LoFz5dl3aBqAG8_IYyh-Fs216E04KW0VpUU8SWPI9_o0O7mVg90KBnABsABSJ3s1sdlZzyes8o56rqVAhLUk5f1u8W_2g5GSLSLQ_e6scUf_YVnJmkVBbIrOzAN1jktY_5HEcg8NkI4W2JO9HLw24YfwFsmBjTaKPf7ikgFKtjLcH9HQwho6h7LJGRxvRZEbDOr9XHIhRfQL5VZuzbIwMQcr5rhA_h_yo-Yr7Pn9oxu5Agdo4VFbQaqWicjm7u_r4QXGk_2xzeybGMzYwGF3YK353npU-pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صداوسیما: آقا مجتبی دستور بده توی 24 ساعت سلاح هسته‌ای میسازیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/146922" target="_blank">📅 21:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146921">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DsXzO_w1JKbf0LUU-d-V6sAV0dqeBNPcAliE7p10TCp-Qg4LYKiIdyn-LgAeYZiO7zqKlK1jMNeL7cR45YuPGfxVSixDm3JktGLxjZdmHsdialX4PlNajDYLDEy3abNCjU4rHvIc5gJXRsF0MFtooISlSEqQLUXjeDlUUCNc64CIXZcq3VvTLdEgW-RNfaN_677xhgVXEomqD1Sw-Ydf50je_2AVNmPmURToVpHzO0B5g3npHy00oKHEXLQSCasMmeRk3YnNEKNKemRZwEdpAgOhsQd1jZ4QAWh5oAevkKq0iegPF044LbAJ352JDNVpYGVoVrr80E10pBh_xgMYcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شعار جدیدی که دیشب علیه حسن روحانی سر دادن : نهپاد، نفوذی هدایت پذیر از راه دور
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/146921" target="_blank">📅 21:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146920">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYIyKhXqB87c4juZb4NI5Tlg_C4ZJUMt4ufaQ-uJpds2Kgnsl8_HuA5cu3vDK3MmrkXTbQp_e-FcDwxd9lWU7rzq8AKVM5y280do2sdi8iskSuOlT_0G3vRhhwKFOaP6mRtmLi5QxgfeFgxNYpHQKMaDNea57gZstAuhLmOT8gYp3qp9RnUHCegy-1CPG5ZeSwxN0h8krKqIzUdtrvMAl-aTEClN2da4se6-yUstfDfzfTh6LKbCs7_lmJ9fXVRP-0xRSFaZPWb2ICCH8EOuzZ0S8Rvwyel4SuPR7cF-7eDhhrnISvNPWEBa9fq9oWbSKYY9S2dQ0FscXIhyhm3OsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: و اعتصموا بحبل الله جمیعا و لا تفرقوا و اذکروا نعمت الله علیکم اذ کنتم اعداء فالف بین قلوبکم فاصبحتم بنعمته اخوانا و کنتم علی شفا حفرة من النار فانقذکم منها کذلک یبین الله لکم آیاته لعلکم تهتدون
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/146920" target="_blank">📅 21:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146919">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeVj6HxMjzwhFeo-fL-e7EUz5LIJ_aVZjc6JGX4L4zHmzrK0f4RLcbuqJ5YOooJy4sC2aAsemGH2aCbqmEzoDvW5KbF57DJj21X9PdotLtO4A6AtZKi3d7P4xxYTXEPj631ix9kfgbm1yoztyrrB7qm30qOyMBT72CBNMJfqL_NKIDaii21P9TtVM7B8txnVYDsXP69CsppKLt3DQXM4rc1RFG5j_RF3Z1gTAZT9MOr2ksKM2s3dtfMdb7MWDZSEGX97guRNHYgOKqlU15XmAGlA6gY6IiGNJe_I2p-SaA6l4_0dtvVDHM4uxMRlDlPHEQRLSTFJEKRA5NLmVcs6yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دنا پلاس توربو ۳.۵ میلیارد تومن
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/146919" target="_blank">📅 20:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146918">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
صبح دلار ۲۳۵ بود پزشکیان رفت بریکس پیشنهاد اقتصادی داد، الان شد ۲۳۶
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/146918" target="_blank">📅 20:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146917">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/465d849e71.mp4?token=sT-ldZu6jlYXsqfCZCWnpCQ-fYjZ1fdITGotn49IWKuZ_aacAbprJYaIGRt-6wJ6iIZXKRWRVTy9CNucMAeI2PipEDwC0sQ9knIEyN6ewR2MyCkooq1AZhCASm9ck4uBQj1SCvWpTR6rb0NbzzpndOJ2-5l0EqwPiTvsmstsLwzV-Xyywn9gR6Zo2sU2ElHdeaTGujBrD5hjvXKSr98spYnodW3aIJsrkQ5_GywDnB32_dWmJH55UnOJDs9wTSv1FSUYSm6PRj1OwKlHLhS6BFPuQzdK7LfxvROVWJcwsrbJ_2AB6vMR4KCkVVWYRV3sYTiyoRVvOjzuQaKzjjus8oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/465d849e71.mp4?token=sT-ldZu6jlYXsqfCZCWnpCQ-fYjZ1fdITGotn49IWKuZ_aacAbprJYaIGRt-6wJ6iIZXKRWRVTy9CNucMAeI2PipEDwC0sQ9knIEyN6ewR2MyCkooq1AZhCASm9ck4uBQj1SCvWpTR6rb0NbzzpndOJ2-5l0EqwPiTvsmstsLwzV-Xyywn9gR6Zo2sU2ElHdeaTGujBrD5hjvXKSr98spYnodW3aIJsrkQ5_GywDnB32_dWmJH55UnOJDs9wTSv1FSUYSm6PRj1OwKlHLhS6BFPuQzdK7LfxvROVWJcwsrbJ_2AB6vMR4KCkVVWYRV3sYTiyoRVvOjzuQaKzjjus8oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یاسر جبرائیلی؛ فعال سیاسی اصولگرا: ایران ظرفیت سکونت یک میلیارد نفر را دارد
به هر خانواده ایرانی ۴۰۰ متر زمین میرسد اما زمین را احتکار می‌کنند و به مردم نمی‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/146917" target="_blank">📅 20:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146916">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgoPHGITDy8bPK_LS9eZ-hOLrK2eVRy1QmEWT1JB3cN5DYNd0FvVJxSvOeio5UyH9QMs5oGu_n4OxgkvoS2TYc5kcwUSWxiqR8N7t07UJnjmXdMhQvVRgy109JN0ETh-UHeVGF2CeiAB12ZWRptY1DlxWJxPqx7GzNkNgjucEA3JUjKgJrqj0jN5NikXK18vdXfw5v7nrsSwsRV4As7328sa_srD6Xfvs_4dVmifUhx_qsDfGjjAwGct1DfBCSALJLbFNCITsoyJmxjDipSrHCAUIuzqMyk8Ft-XFPWpfBlcjTZqAQsoiwAsG_fho6HOaEkVzW5W6IEsZTcO3oQzjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادعای
امام‌جمعه یاسوج:
اقا مجتبی روزی ۱۰ ساعت فعالیت داره، تو ختم پدرش هم حضور داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/146916" target="_blank">📅 20:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146915">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aECLPVhXMjH1GGS0v57w09Ri31xCm1xYwKJ412XkgWDgJfP-C1UXTBy4cF_c7hF3cMvVRX--2JcTFiweLHXM-hrtVxk0J_4-iuzHNVMKr-ZOW1wIwLfxnLs65SRzJe_2dYqt8C2poJNbrJIBAPmkjxsNUHvtTh53Tgcaak5IO8UhwTkEZqovbacmJHMT9vQPuFXIvyOuzxBDAxE1-Ze0c9tn2DAzMj7t_Ni3Bu2ArGgFuW2RTj4qzKzDIL-SDIqmS4lepQf---dAiYJuVnoD65_-RW1A_FelKxCRzjyjHuyLz65n-CJ0NJauMjWaIXpFvuvKTsfLoWP0wBAuTdO03w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق پیش‌بینی‌ها، یکی از پربارش‌ترین پاییزها در راهه
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/146915" target="_blank">📅 20:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146914">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏
👈
مهر:
صدا های شنیده شده در قشم تست پدافند هوایی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/146914" target="_blank">📅 19:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146913">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zji1VdM7DXWPEPJwwf_KsUkHWY88Od_ftGN6P7V6lv1M7C7K20M_YlQESlCQzY8_VGWh0rMZ1yQuTy8NHFkre3dQfFk5mYaGxzoNJv9MiJmYeLqV1nvMNqxcLOtGByVPQekHhbqWR03hxydrE1K-Y1JF0LEH2h4HeLTePgYhEA04lTMMNrOtGldjCUlk5GOl2sR1d68LSNekZItKXdr7IFvUb0MvrEJWRxCzcEGQm4ngsbjRcYAY-XmOSN9GlSqQc24emaCSVIncTrE23j-foISe5Sp6cHEuN6V-1RCxyz2ew-yBRX-Q2Mo5JGp2axN-OoYrKn9SpMWNdJ3vByapnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امام جمعه تبریز:
اسرائیل ما را به بمباران اتمی تهدید کرده؛ از همه مسئولان کشور می‌خواهم دکترین دفاعی ایران را مورد بازنگری قرار دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/146913" target="_blank">📅 19:37 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146912">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63cda7faae.mp4?token=TBQV0ffltitKCOBTWulkNwbnLzNuaPvi_e8hXypO4ELo1jPT6Geu0zJrYr8sxd7vm1FNFva7nLzpunT8HZc-gtkNsdfftGwNlS-hI0ZlYdmo3LbVY-VZle8zfEbCut_g2BvNqdQr7fwEUlBEKmTlZFLdAcrQCFgv9bPoZwoI0M5sYv6tVNL_P0L9Hu2SoQJLh8Xac5sifKk_xZeAeaUC5cQszmbu4ILBBq7zfon0HVklRX2556-Z0mKr9MGoiueGx_Uxr22AlMl7miGglSKGNvGp0Q8RPxOgnT7rGwItf7cHse7zTCGh6Et1cgjL3gh0pHfSyOR2DbNln_qq46E6cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63cda7faae.mp4?token=TBQV0ffltitKCOBTWulkNwbnLzNuaPvi_e8hXypO4ELo1jPT6Geu0zJrYr8sxd7vm1FNFva7nLzpunT8HZc-gtkNsdfftGwNlS-hI0ZlYdmo3LbVY-VZle8zfEbCut_g2BvNqdQr7fwEUlBEKmTlZFLdAcrQCFgv9bPoZwoI0M5sYv6tVNL_P0L9Hu2SoQJLh8Xac5sifKk_xZeAeaUC5cQszmbu4ILBBq7zfon0HVklRX2556-Z0mKr9MGoiueGx_Uxr22AlMl7miGglSKGNvGp0Q8RPxOgnT7rGwItf7cHse7zTCGh6Et1cgjL3gh0pHfSyOR2DbNln_qq46E6cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوریا بختیاری، فعال اقتصادی:
خودِ ابراهیم رئيسی می‌گفت که اقتصاد رو نمی‌فهمه!
از ما دعوت کرده بودن که واسه رئیس جمهور ممکلت، انیمیشن‌های اقتصادی درست کنیم.
تازه گفته بودن این انیمیشن‌ها نباید از 3دقیقه بیشتر بشه چون ذهنِ حاج‌آقا می‌پَره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/146912" target="_blank">📅 19:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146911">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnEYEddVORO5spW3dddJdU3-NVY6A0b4i5RH-3F6xP_fUhb-3NCvV6d-KSqEUsqyKhf9Si-zS_tiM3vdp-9jJaF_sR749RY3USPp9M1EwrpmY-qofFNO17WeIDLt7uEIfpVZ0CZpcTyJBGDMTSR2JiAFpU5zYfY6uD67_QBre4uj96Tdz489LTwMn6_0xmraI3FqZSfwYKR6Bw7WbdY1Ars2puTVPnl-YsvMYHP5Bq3xDDkvmn0etpmmzAn3VktM48dP2oghFcsWttX78CTAwWtIObI_oKX2zxo6beC0lLWy4WfOG7OgkmBzy9K-lzdHd0MgZlGHYdbLrjZ6T4X4Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی اسرائیلی به نبطیه الفوقا در جنوب لبنان، ساعتی پیش انجام شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/146911" target="_blank">📅 19:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146910">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p1X2k3iTgn6Yr_mdXYLPQ4XDKtp500XNCXqGzzUalLnzlb_gncg8r_NWa4RpQRksbieEGxow9pcT0SuLRyornIl1iJTNl5McGzqK043IU1sjaleTIXeqpzUY0tP31WwiGvvNm7hmaw8UD-8pi5HhJ6AGjIzy7yuUw4mgZn1qC0kSVkonbGJk0uM03ZJsRbKAQqTENB2nrHBQyyOnXTFZWglzVkxK8U-IElBYXqV8Qdir2XUSaI5C1qEXUgcCQHrUNwzGJNt1AO-dL6P5iYe0C4ktCPuEqgnHOZIzwXgucElorrYS8eXHzee8dyO7S6082Rn_cS7BwhIZHQdQ6ZGLfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال 14 اسرائیل:
اوکراین
مرکز کلیدی لجستیک جمهوری اسلامی و روسیه در دریای خزر را هدف قرار داد.
حملات شبانه‌ی اوکراین به بندر مخاچ‌قلعه، پل ارتباطی و حیاتی دریایی میان روسیه و ایران برای انتقال پهپادهای شاهد، آن را از کار انداخت. در همین حال، ۳ ناو جنگی روسیه در نووروسیسک به شدت آسیب دیدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/146910" target="_blank">📅 18:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146909">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HkskbwmMIuIhzgN7uEEdO3dMSTfoLXLFTTPamwR7oM-UjawRHq9w9QPTkc92ZTSwuYnHj0j8MEl83EmHkn8blxFxBPHXwBupTGQX6sHuF4uXe2h5CZaYgEA81_06WNqwR5IOZY77vTNOfCWSeM-Fu6QkyhZrDIh4VmknkooD2I2TGFeMgQmOeH05f83g2tfyCxGpKNqkNZdWlsf04QhXap2e5mKpsUyq_oxcq1ODoBo33kC5Ih4koRgG9aGeH3bU_SYD4oj6e2M91rxjk3VYRsp25OTAq-Mt8ywZkdJWxOoK2HJhc932ug5CNOE9UYtvX6mzvVs6Fn1NG0RGnyl29A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
VIP مخصوص روزای قطعی و اختلال اینترنت!
😍
اگه نمی‌خوای وسط قطعی اینترنت بدون دسترسی بمونی، از قبل
VIP
تهیه کن و خیالت راحت باشه.
🚀
سرویس نامحدود با قیمت فوق‌العاده
😍
قیمتش حتی از
پاکت هم کمتره!
⏳
ظرفیت VIP محدوده
و ممکنه سریع تکمیل بشه.
❤️
برای خرید و فعال‌سازی
👇
👇
❤️
@NetAazaadBot
@NetAazaadBot</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/146909" target="_blank">📅 18:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146908">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2f8a98470.mp4?token=GAjZUFjHmXXqF_KRrNhJNDcvowLqTHO8EHfuknRMd0gsXW-5GkSTxfzci_g3Cq6snjd3TSXCyQv6w5B6x3rcPJqvPiqQHLlYmG5cHK7TTIKPyzLzHVuIf4eb_U__51Qvgcs5H2TF8SLKJW8oiCNbor98opuvZ9MwEdXzYRnG6CrTzTFmkIRvpt1TaZx3-vlY7J-33Nou_bYvyAh0eD1AjAcYHFyVsGX7LMcth6dBIRUUC_iZSBUowjAKMMv2LucMs2K3Tqjb10kgYDANlQ16GtG3eDePNc-wEaV3ub1K-aNhfk0sGSz6qEH3fWYH-V_XY6Pa6hjjhfRG6r_oKAvLvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2f8a98470.mp4?token=GAjZUFjHmXXqF_KRrNhJNDcvowLqTHO8EHfuknRMd0gsXW-5GkSTxfzci_g3Cq6snjd3TSXCyQv6w5B6x3rcPJqvPiqQHLlYmG5cHK7TTIKPyzLzHVuIf4eb_U__51Qvgcs5H2TF8SLKJW8oiCNbor98opuvZ9MwEdXzYRnG6CrTzTFmkIRvpt1TaZx3-vlY7J-33Nou_bYvyAh0eD1AjAcYHFyVsGX7LMcth6dBIRUUC_iZSBUowjAKMMv2LucMs2K3Tqjb10kgYDANlQ16GtG3eDePNc-wEaV3ub1K-aNhfk0sGSz6qEH3fWYH-V_XY6Pa6hjjhfRG6r_oKAvLvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیتر هگست:
تاریخ به پایان نرسیده بود؛ هیچ‌وقت هم به پایان نمی‌رسه. مبارزه با شر ادامه داشت و الان هم ادامه داره.
🔴
و این مبارزه تا روز قیامت ادامه خواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/146908" target="_blank">📅 18:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146907">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06eee79e79.mp4?token=CRXzeH_5tUbFwbn39h_w3Zt8rSPjWBk-MpR91mHa9S6DPqqQMafgguh3RboJn08qkYt4LYuhVBiiWdt6yOJbY2pCOA6C6yC_XGBwKI0bZ56m8JzlzMH39k92-1e5OrYjmO7BwztynqwDOZuvgHTWDwTGmzYt_X_w2GETufz6mYYGuSpMndrONkR5dI1_lrZv4j7tjoqzGEwbvzFBVRuSBAgq37y6W8wH19bdNyuhjw1-q7K364SFcOjX2ucL6mB0xSWlbFJ-3nE82bcQi2pRNNqAYhYq6isvhsyona6c9vUIbvVuAlIldTppCADWdCplpCbKgCEAGXgh34X3W-EXng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06eee79e79.mp4?token=CRXzeH_5tUbFwbn39h_w3Zt8rSPjWBk-MpR91mHa9S6DPqqQMafgguh3RboJn08qkYt4LYuhVBiiWdt6yOJbY2pCOA6C6yC_XGBwKI0bZ56m8JzlzMH39k92-1e5OrYjmO7BwztynqwDOZuvgHTWDwTGmzYt_X_w2GETufz6mYYGuSpMndrONkR5dI1_lrZv4j7tjoqzGEwbvzFBVRuSBAgq37y6W8wH19bdNyuhjw1-q7K364SFcOjX2ucL6mB0xSWlbFJ-3nE82bcQi2pRNNqAYhYq6isvhsyona6c9vUIbvVuAlIldTppCADWdCplpCbKgCEAGXgh34X3W-EXng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
هگست درباره ایران:
تنگه را ما کنترل می‌کنیم و این نبرد را نیز تمام خواهیم کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/146907" target="_blank">📅 18:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146906">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e4eb98a5d.mp4?token=gU6G_XvJmcRxUcDpHLL3AgpXS7eHmQN3jH2aETOiC8guK2tO2H3LVML8Gh-L-9RjF4OOaTBb5x9gNeETuAyz0lVx9HJjFdsyqY0tpElukB02jDl1-dgFiwCRbh1RWoj1gt-pLEytEDPiij_uXg7WX8W2lD31whpwei5mb_scbdT3iOCgLjn4AQwOQ_Yb4ngDiUCGpj5jtZKFfT4yShROV7BJXgBnYEC0wUVZErUFOyv6rym4Z6o6RcXJVzDTdwIGgD-YeRG19gvn8GkRIGnf_EKLza3nvWM-Dy7i5ogmpAK8Y9KzYGQz6in16goqZgiCuVMEYbwTQDBe10KGIexvwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e4eb98a5d.mp4?token=gU6G_XvJmcRxUcDpHLL3AgpXS7eHmQN3jH2aETOiC8guK2tO2H3LVML8Gh-L-9RjF4OOaTBb5x9gNeETuAyz0lVx9HJjFdsyqY0tpElukB02jDl1-dgFiwCRbh1RWoj1gt-pLEytEDPiij_uXg7WX8W2lD31whpwei5mb_scbdT3iOCgLjn4AQwOQ_Yb4ngDiUCGpj5jtZKFfT4yShROV7BJXgBnYEC0wUVZErUFOyv6rym4Z6o6RcXJVzDTdwIGgD-YeRG19gvn8GkRIGnf_EKLza3nvWM-Dy7i5ogmpAK8Y9KzYGQz6in16goqZgiCuVMEYbwTQDBe10KGIexvwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما هیچ‌وقت، هیچ‌وقت فراموش نخواهیم کرد.
🔴
به همین دلیله که ما امروز می‌جنگیم. ما انتخاب دیگه‌ای نداریم
🔴
تنها چیزی که می‌تونه وجود داشته باشه، پیروزیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/146906" target="_blank">📅 18:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146905">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7dd01ae09.mp4?token=pJk0fS2w8AF5xrQJB7VqNqDDxUMXHXRp4H6_7FmROKoZXvDAkA7YIk5o88_N5TnPfpgNPeaHJ-NF26hUroV-irsrroJcso4yfEsfC6VdkzdtObWWxuT8NnaWS8j4LzRhB0cIJpTrdhANDTcSSnxW_hQSAZMd1wTnOFLqEKjzSMtRetWlfgeSooRUT5I-6u1mLMuIdpTIJVVxaRfGfE68c9iytGQCptRxV8YnlEcUAl3AEZFQhc8vkof21wkcKa6rUVuTNmZ-w8LJjVcAqeOk-xb3Zqaxc4W4MM3S7TJaE7MqiC79PMAQUAq1DH3axZf2uWWWMUAuLqvVjh8CO98no7QS6RBSfEWG9XGQWclgQhKdFC2e3fTiJ7r6xPGTFoCOkZLffZPDCp8cP85z5y2zSR6GMdBCHcs8XrOh9EVy1_TBNJxpYY3zSYWdJpKyZ8h-FgeylK--YSAmch8RSBQbt-U--M4KpVDCE-DQq68WAO9qzj2kB0Eu_OVAs5aTg3UGZHALXV12qRFy-4Vf7JPGjB-CbWc3rPmCOpWFCIrRl17Gcs1Lkt6USFAzuZxPrm-Rp4JKl2k7VTLLJRJmiTL5rjyBvZCIDHNxrTuBTzasXlsIIwCwojAnCwY2208cGjV1NBBK4docEnZY5-0zR3L9vrLDYDYBKoAtvz24EQAhRIM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7dd01ae09.mp4?token=pJk0fS2w8AF5xrQJB7VqNqDDxUMXHXRp4H6_7FmROKoZXvDAkA7YIk5o88_N5TnPfpgNPeaHJ-NF26hUroV-irsrroJcso4yfEsfC6VdkzdtObWWxuT8NnaWS8j4LzRhB0cIJpTrdhANDTcSSnxW_hQSAZMd1wTnOFLqEKjzSMtRetWlfgeSooRUT5I-6u1mLMuIdpTIJVVxaRfGfE68c9iytGQCptRxV8YnlEcUAl3AEZFQhc8vkof21wkcKa6rUVuTNmZ-w8LJjVcAqeOk-xb3Zqaxc4W4MM3S7TJaE7MqiC79PMAQUAq1DH3axZf2uWWWMUAuLqvVjh8CO98no7QS6RBSfEWG9XGQWclgQhKdFC2e3fTiJ7r6xPGTFoCOkZLffZPDCp8cP85z5y2zSR6GMdBCHcs8XrOh9EVy1_TBNJxpYY3zSYWdJpKyZ8h-FgeylK--YSAmch8RSBQbt-U--M4KpVDCE-DQq68WAO9qzj2kB0Eu_OVAs5aTg3UGZHALXV12qRFy-4Vf7JPGjB-CbWc3rPmCOpWFCIrRl17Gcs1Lkt6USFAzuZxPrm-Rp4JKl2k7VTLLJRJmiTL5rjyBvZCIDHNxrTuBTzasXlsIIwCwojAnCwY2208cGjV1NBBK4docEnZY5-0zR3L9vrLDYDYBKoAtvz24EQAhRIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ از ارتش آمریکا تقدیر کرد، اما هیچ اشاره‌ای به نیروهای کشورهای دیگر عضو ناتو که پس از حملات یازدهم سپتامبر در کنار آمریکا جنگیدند، نکرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/146905" target="_blank">📅 18:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146904">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ترامپ: ایران بزرگترین حامی دولتی تروریسم در جهان است و هرگز به سلاح هسته‌ای نخواهد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/146904" target="_blank">📅 17:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146903">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93e991788b.mp4?token=a7ch57Umu53k2-spBKMNkur1Ci_vnu2Lq1_1jlhf11r8YQD2XTR9l8vxGuplPT0YwC4YfAwkDOvwFoi097S2ORwofL-UqBMA6t_Sdh1EkjO5il3Bd11XiCYYbgHfgtWhTKWzGr-ToxK-kkwEr2YOvLeYJawT1qMcauQ4Wifa3xuNPME6Sic5bJL39FLzYP7hm7HaOVlQtHT6R54hKUb_81ys_2BurIi_j5OIEPOPNU6t7jmmk-B6Hf1sVQPAGinw0W0Clb5bTn2eqzcv42rZaOsI3H4SBv49941xQVpAGbVQR6DGLCPlu2lkzBKWRd4JqiXhrc-rME9WIahR2Sm-Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93e991788b.mp4?token=a7ch57Umu53k2-spBKMNkur1Ci_vnu2Lq1_1jlhf11r8YQD2XTR9l8vxGuplPT0YwC4YfAwkDOvwFoi097S2ORwofL-UqBMA6t_Sdh1EkjO5il3Bd11XiCYYbgHfgtWhTKWzGr-ToxK-kkwEr2YOvLeYJawT1qMcauQ4Wifa3xuNPME6Sic5bJL39FLzYP7hm7HaOVlQtHT6R54hKUb_81ys_2BurIi_j5OIEPOPNU6t7jmmk-B6Hf1sVQPAGinw0W0Clb5bTn2eqzcv42rZaOsI3H4SBv49941xQVpAGbVQR6DGLCPlu2lkzBKWRd4JqiXhrc-rME9WIahR2Sm-Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره حادثه 11 سپتامبر:
ما همیشه قربانیان و خانواده‌های آن‌ها را که در حادثه 11 سپتامبر سال 2001 جان خود را از دست دادند، به یاد خواهیم داشت. متاسفانه، این یک تاریخ بسیار مشهور است.
🔴
آن روز، در ابتدا، روزی بسیار زیبا به نظر می‌رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/146903" target="_blank">📅 17:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146902">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd606e096.mp4?token=r1AFHiFrIeoATibtZPzO0RqW3oJ-LTsS-ihX5SKzajK_BR09L-nrwE_r3NSfGovhnw3r_XIufpSKoM3Axs62dYxWu5BES3DlNVOQ9I5oyQXdOHEUSR4XCTR2l2CAVKayGtzDEnUQu3ZfVotHUOO_ouDctxOsUDXd5nlHbX5SqaTW_adl65Kl99BOqvprpuvaO9B3MdK4Eyx8EJiQABGSf6Jb4CmDJ9t84yVx9o1WHerGDpL87fqR1A6zNUGOX1jWWgdFdindpP2b_s60BMaPXQWKYDKcwKyuHyjLdBO9ane4ERUF8CsnYfGr_xuHOw01x0tnXyRP0rgw3eQzuEHzXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd606e096.mp4?token=r1AFHiFrIeoATibtZPzO0RqW3oJ-LTsS-ihX5SKzajK_BR09L-nrwE_r3NSfGovhnw3r_XIufpSKoM3Axs62dYxWu5BES3DlNVOQ9I5oyQXdOHEUSR4XCTR2l2CAVKayGtzDEnUQu3ZfVotHUOO_ouDctxOsUDXd5nlHbX5SqaTW_adl65Kl99BOqvprpuvaO9B3MdK4Eyx8EJiQABGSf6Jb4CmDJ9t84yVx9o1WHerGDpL87fqR1A6zNUGOX1jWWgdFdindpP2b_s60BMaPXQWKYDKcwKyuHyjLdBO9ane4ERUF8CsnYfGr_xuHOw01x0tnXyRP0rgw3eQzuEHzXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، حملات 11 سپتامبر را با جنگ خود علیه ایران مرتبط دانست: ما هرگز این واقعه را فراموش نخواهیم کرد. به همین دلیل است که امروز می‌جنگیم.
🔴
ما هیچ انتخابی نداریم. تنها نتیجه ممکن، پیروزی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/146902" target="_blank">📅 17:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146901">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YU6XvKQvy3yM8lqW01chd8GronMwizD0oUwKTQ-kr-JOMR_p2Cy9ottk_eTHuFjQtC2Z0WHdSC91BROCkfZ0K05xA50hVFBq_z_qIfqBX0TKWrS2b1ZX_VcOaTB8pManw5rXVTxA_bd5UPz0285ztCMRyhvHPnH9IyPcuSBw2vWvTZK8tTxC3tXkbat8N2G_ceKRHv8YgSaQPczDbI4eWG7vOX9WYp1Zqt1CGWXRQWMHmCSd5SFnjOX0LW8V9anUT4-7_bkp99_yySe9WKFHLGUn-j2zYyLA-AdcDL3EI40VUJ1mvacr4Tir0k2hT2MnKU7re-tEbxp1bauR4R75FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی:  اخیرا محسن رضایی از عاصم منیر گلایه کرده که چرا صرفا طرفِ ترامپ بوده و از نقشِ میانجیگر خارج شده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/146901" target="_blank">📅 17:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146900">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
رئیس جمهور اوکراین از حملات شدید پهپادی به تأسیسات نفتی روسیه خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/146900" target="_blank">📅 17:37 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146899">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14e35d7d19.mp4?token=IzP1Q8-tfNA9c1nXZsgWvC8OwO5aaMheXtveYjjfdHJ3c7fwqhNZiYEh9d2FFugaBoebJRKCGuOhGTW1ZyAJLO3a6sDWZ_VL91rmHcbPULJnoHQq8X2WA2-gx8lDQXEO9f4xEPlPRWEK1Nk8VMsylxw46O8MyBksl2EXqH73J0Y33jcPk_8FeG_BYdYh_wM8UmFqJ7UyrZxxqNq-FdPcDE6kyteEDuc6_luDCDhbct71G3vQ5-gYc61G_G3WtsJYGfibfoO-G3D4U3dJgpvDEd0BkxT69xGWnVg7BsX5HHJHP3-boU2ZP_BEP57kREsxR9GAjcp64UlvUOUAyLyYKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14e35d7d19.mp4?token=IzP1Q8-tfNA9c1nXZsgWvC8OwO5aaMheXtveYjjfdHJ3c7fwqhNZiYEh9d2FFugaBoebJRKCGuOhGTW1ZyAJLO3a6sDWZ_VL91rmHcbPULJnoHQq8X2WA2-gx8lDQXEO9f4xEPlPRWEK1Nk8VMsylxw46O8MyBksl2EXqH73J0Y33jcPk_8FeG_BYdYh_wM8UmFqJ7UyrZxxqNq-FdPcDE6kyteEDuc6_luDCDhbct71G3vQ5-gYc61G_G3WtsJYGfibfoO-G3D4U3dJgpvDEd0BkxT69xGWnVg7BsX5HHJHP3-boU2ZP_BEP57kREsxR9GAjcp64UlvUOUAyLyYKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین: طی پنج سال گذشته، بیش از ۴۰ درصد تولید ناخالص داخلی جهان توسط کشورهای عضو بریکس بوده است
🔴
در حالی که سهم گروه موسوم به «هفت بزرگ»، نمی‌دانم چرا به آن «بزرگ» می‌گویند، تنها ۲۹ درصد بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/146899" target="_blank">📅 17:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146898">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7637eba24e.mp4?token=q3ZAhzzxC1XxHJebpIMN1Y1U7KYcrZufUZKj_4LWDpxuq_czqptQwJbB62vej80J7hmArdhJNPcr_6DP0ripCdWuPMsu4F1i3Ay9QqbJ9qHUnrW7QdYyqUFpEGsUPUDjnW-NB5uzHHURN0cpoUSQF0K3EA_oaoI1XU5KDtbv3ITlDxazlct6qL2-zuzVB_C5ViKXeEInMVrxCPMJLEMo0AUeGfSo8J4U4AH_kCpmI8gSv3kR8Q9QTzev-UXPFwnAqIm9hb0z7FKEyqDLkb7nM27PF7ULv_a0fhuu7Ujtp3AMbYhbtTZbQeKq9VgdwHnrqtX79XaBf8iwV6VZVs-0-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7637eba24e.mp4?token=q3ZAhzzxC1XxHJebpIMN1Y1U7KYcrZufUZKj_4LWDpxuq_czqptQwJbB62vej80J7hmArdhJNPcr_6DP0ripCdWuPMsu4F1i3Ay9QqbJ9qHUnrW7QdYyqUFpEGsUPUDjnW-NB5uzHHURN0cpoUSQF0K3EA_oaoI1XU5KDtbv3ITlDxazlct6qL2-zuzVB_C5ViKXeEInMVrxCPMJLEMo0AUeGfSo8J4U4AH_kCpmI8gSv3kR8Q9QTzev-UXPFwnAqIm9hb0z7FKEyqDLkb7nM27PF7ULv_a0fhuu7Ujtp3AMbYhbtTZbQeKq9VgdwHnrqtX79XaBf8iwV6VZVs-0-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: ایرانی‌ها در تلاش‌اند تا در آمریکا مشکلات اقتصادی ایجاد کنند
🔴
اگر به حساب‌های کاربری ایرانی‌ها در توییتر نگاه کنید، می‌بینید آن‌ها تلاش می‌کنند در آمریکا مشکلات اقتصادی به وجود آورند؛ چه از طریق تغییر نرخ بازده اوراق قرضه و چه با دستکاری قیمت نفت.
🔴
رسانه‌هایی مثل بلومبرگ، فایننشال‌تایمز و وال‌استریت‌ژورنال تا حدی به «سندرم اختلال ترامپ» (حمله به سیاست‌های ترامپ) مبتلا شده‌اند که حاضرند به ایرانی‌ها تریبون بدهند تا علیه ما مانور بدهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/146898" target="_blank">📅 17:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146897">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-zEWriLsWCd5So2cHiNgJM77oeWYEyuEEsB0_5AZ9UzZStgyR4wKQc9H5BVV0AFIigz_qiHl28ywIHpDNhicCirb9RhJBNQ6slBT9dQK_Q0iYveJKiFN9USpYVk09bqxdJForAhKRXk3U2Q-3w3gM4c-yxIYbFuVIQdYzB311T4qug1GTxBXu1XhlpXolMho4k3rsQxRl-F5Fh_9lwMSSXfwkx4ZGTB-K4JcMoa-YBu17hP8kQNsbZ-nXn7YwFX780BEzAHO-OV9pAUSqfE9c9ks9y2ZeAQlIi-ds9_Hq0rF4R3KzLTYeVTKonaNVuT3vyzprc8OgLDE68zoHhyUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان با نخست‌وزیر هند دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/146897" target="_blank">📅 17:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146896">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
وزارت امور خارجه : ما روز دوشنبه، با همکاری عراق و کشورهای خلیج فارس، نشستی در مورد تنگه هرمز در عمان برگزار خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/146896" target="_blank">📅 17:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146895">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
امام‌جمعه یاسوج: اقا مجتبی روزی ۱۰ ساعت فعالیت داره، تو ختم پدرش هم حضور داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/146895" target="_blank">📅 17:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146894">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d562e33a76.mp4?token=tGZpsbGxb-AzgbdGnYPgCoWDwLzeFrWhdHekPo_8VDRDbiLIo4InWXo9WTDAa91tQdHS27c0jMqEp2Nv5W13QfsMVfWy8VQa0mgqelM1o4AQXzEiIVc79jCOhz7S6e2rBYdbrHjVdGFdirxzIlCLisF1h9X03TrVhj7kROnraCUuL_zzWbjIQINKzxL0YfsQX2l8rIwtWzYQ99HqhfZFY9LqxcjOZ_E6BeSv4aDNEaCmSPO2PeO8_7tnjYGE9cXljvCvNDIThIYSZndwW1Cp1K8Ei6HEtLyobvS-1gccBBjuyFLvB_d3KS45SIsfjUF9rAkil_0qzgx3cymCaGXSzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d562e33a76.mp4?token=tGZpsbGxb-AzgbdGnYPgCoWDwLzeFrWhdHekPo_8VDRDbiLIo4InWXo9WTDAa91tQdHS27c0jMqEp2Nv5W13QfsMVfWy8VQa0mgqelM1o4AQXzEiIVc79jCOhz7S6e2rBYdbrHjVdGFdirxzIlCLisF1h9X03TrVhj7kROnraCUuL_zzWbjIQINKzxL0YfsQX2l8rIwtWzYQ99HqhfZFY9LqxcjOZ_E6BeSv4aDNEaCmSPO2PeO8_7tnjYGE9cXljvCvNDIThIYSZndwW1Cp1K8Ei6HEtLyobvS-1gccBBjuyFLvB_d3KS45SIsfjUF9rAkil_0qzgx3cymCaGXSzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ا
سکات
بسنت: ایرانیها، اگر به حساب‌های کاربری آن‌ها در شبکه X نگاه کنید، تلاش می‌کنند مشکلات اقتصادی در ایالات متحده ایجاد کنند، یا با دستکاری در نرخ بازده اوراق قرضه، یا با دستکاری در قیمت نفت.
🔴
و می‌دانید، صرف اینکه رسانه‌هایی مانند استیفانی، بلومبرگ، فایننشال تایمز، و حتی وال استریت ژورنال، به شدت تحت تاثیر "سندرم اختلال ناشی از ترامپ" هستند، آن‌ها می‌خواهند به ایران‌ها بستری برای فعالیت بدهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/146894" target="_blank">📅 16:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146893">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03112531a9.mp4?token=iYMIMZl-M4mEr4BoFfPnJqGyQbGtyStopr4RALADrWF8ml0-ZFpDRguxJWVoMOWkIPXJ5-2qlqTC-_2IV3QxpfAJaUUuxjyVliZnHJdwoHLmhOOvXdFUvqftpe8R2YbFGW3HnQm9eCdX_nd34Vw0eAdGWNx2qgFU5_oF5f-SmB8GnynMjxt9RJ871wmqmT45qSJObGlWmu7a0wlG9FZyGpkZI6gwQrkSzXc-EHyyAP4qWtad6CSK4nFVyHC6ymD6nGgrV71_IRyrqdKNLDDP68mwkIy76xMe-uO19PSvUei1SGk9ZqHrnShHXveXqE1UL6AsSxzpDxI0s8vxfF4gxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03112531a9.mp4?token=iYMIMZl-M4mEr4BoFfPnJqGyQbGtyStopr4RALADrWF8ml0-ZFpDRguxJWVoMOWkIPXJ5-2qlqTC-_2IV3QxpfAJaUUuxjyVliZnHJdwoHLmhOOvXdFUvqftpe8R2YbFGW3HnQm9eCdX_nd34Vw0eAdGWNx2qgFU5_oF5f-SmB8GnynMjxt9RJ871wmqmT45qSJObGlWmu7a0wlG9FZyGpkZI6gwQrkSzXc-EHyyAP4qWtad6CSK4nFVyHC6ymD6nGgrV71_IRyrqdKNLDDP68mwkIy76xMe-uO19PSvUei1SGk9ZqHrnShHXveXqE1UL6AsSxzpDxI0s8vxfF4gxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: استفاده از ارزهای ملی در تجارت بین اعضای بریکس باید توسعه یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/146893" target="_blank">📅 16:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146892">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDbdxI4_70D2lWmDWw6GAIAMfDZEQ0oiU2fESrz-kJCBd1ChdGH6ipmdybdRWDk6GexwiKsNGUmXmdkQ_lNXUaZqAzPUaHk1-zdwQVQQxWimYWSr5dr7hYjoeiWOCt47Tzg7FvNJb4LsyjdHLzeFTPPhRqAg8EvgJ54Y3rstxo1QZfhuELAZoOWrRUk8tzTu3qkfDvk_LsKhoXdFP9DAGN972MoG-ETniIbv7kl2FXTpYs7jC0KgT-EpgLTe3NZIo9UuOo7iHYwrjfSfr791_zhZi0tsnMJL2c3McOGJR0dAJtDKlZ1gQQ93J6rn0p4KbLijj6nDl6CsWvuWqAjkfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: وزیر خزانه‌داری آمریکا با خوشحالی به خود می‌بالد که می‌خواهد ایرانیان را فقیر کند و اقتصاد ما را به فروپاشی بکشاند. اما در عوض، او درمانده و ناتوان در برابر افکار عمومی قرار گرفته است؛ در حالی که جهان روزبه‌روز اعتماد خود را به نظام مالی آمریکا بیشتر از دست می‌دهد.
🔴
بحران ناشی از هزینه تأمین مالی بدهی‌های آمریکا تنها آغاز ماجراست
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/146892" target="_blank">📅 16:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146891">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
پوتین: کشورهایی که فشار تحریم را علیه روسیه و ایران آغاز کردند خودشان با افت صنعتی و کسری بودجه روبرو شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/146891" target="_blank">📅 16:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146890">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cac53a8e4.mp4?token=sOi9iutdvcQ0b3H_4b2UbOyIkT17njFbcZEfOVogmoI_aboJnyeyLNfEyMzchu1Yh8XL1MjpQpKZB-SZw27nvxC9XIdHapmdw5scPoCEq9JOl2-DHvAOKrv1xWEpVmDmMLPqcATtUPfWmAFdeeCW4FXXTZ9Hk2UutUy2oKswe3gVoGs4ggeLhj6ahqmkBzsG7bcMKYoMCnRMJj-Ok0rGN_AnOaAcryY7lBrmoJVijqsfUWxv9WL4I2xQBQwtB7SDOpldECEwD9SKNpIe5GJf6RgzHYwR-71w67wVDtGPHAn8wdBasAXGA60k1srtIVjtBY8bLeCtjQf1ef7hSC7n5DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cac53a8e4.mp4?token=sOi9iutdvcQ0b3H_4b2UbOyIkT17njFbcZEfOVogmoI_aboJnyeyLNfEyMzchu1Yh8XL1MjpQpKZB-SZw27nvxC9XIdHapmdw5scPoCEq9JOl2-DHvAOKrv1xWEpVmDmMLPqcATtUPfWmAFdeeCW4FXXTZ9Hk2UutUy2oKswe3gVoGs4ggeLhj6ahqmkBzsG7bcMKYoMCnRMJj-Ok0rGN_AnOaAcryY7lBrmoJVijqsfUWxv9WL4I2xQBQwtB7SDOpldECEwD9SKNpIe5GJf6RgzHYwR-71w67wVDtGPHAn8wdBasAXGA60k1srtIVjtBY8bLeCtjQf1ef7hSC7n5DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: ما نفت صادر می‌کنیم، ایرانی‌ها صفر؛ نتیجه ۱۴۰ میلیارد به صفر به نفع ماست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/146890" target="_blank">📅 16:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146889">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51fe8f52d9.mp4?token=XbqgnO943HSQlP6y1H2guygJJy6tMXA0PHx3nDsxdv4jvDZ0mLzjp6B0e-oA66EXAb3d6CnAOKyXhWRo1m238EgAmYrF6xJWGNAUguU8wLMvbtvYed5RKD8sRcVkMJmkL_XxB3DY3h1phFV69tJvY8_R6wlbLpdhwxBiO9dyskw34a3EDcQYTXKgMI26KNQEhitBLnrhjpzlJQ24gEjgSHTkmaHcJZwcxOi0WQHpVRfH74eO1o0_EPgMKxDTIWW5ftpswjaUzJiPRNCMKXTW7Qr17T51NemTPCHmr2RmvZxEgFzhw824sMwFTAZgodfzRYdyiZXigLQ_tfW0x_820g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51fe8f52d9.mp4?token=XbqgnO943HSQlP6y1H2guygJJy6tMXA0PHx3nDsxdv4jvDZ0mLzjp6B0e-oA66EXAb3d6CnAOKyXhWRo1m238EgAmYrF6xJWGNAUguU8wLMvbtvYed5RKD8sRcVkMJmkL_XxB3DY3h1phFV69tJvY8_R6wlbLpdhwxBiO9dyskw34a3EDcQYTXKgMI26KNQEhitBLnrhjpzlJQ24gEjgSHTkmaHcJZwcxOi0WQHpVRfH74eO1o0_EPgMKxDTIWW5ftpswjaUzJiPRNCMKXTW7Qr17T51NemTPCHmr2RmvZxEgFzhw824sMwFTAZgodfzRYdyiZXigLQ_tfW0x_820g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکات بسنت: هر آنچه که ایرانی‌ها می‌گویند، بیشتر یا بخش زیادی از آن، ریشه در خیال‌پردازی دارد.
🔴
بسیاری از این حرف‌ها، آرزوهای دست‌نیافتنی هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/146889" target="_blank">📅 16:22 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146888">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1144f5e406.mp4?token=hYKH6H8yob4ogJ0j6M3xKmOefWyB44h9sYGN50c9t4Uwye77mc6nQK2r6I2alpc65pEwUeLiUDerJRxB0L_Lx8FRBxB3fpjASA0uGf7zwHDjmQ6qxrQCdHFV7NAwRhb2DU6gw2dp2-TKioBuv_yhwcJDL-HWXSCFSsDpHvb2o-lM8QX02Ysdls6tcO6HW86fdu89h5m9Wf869yb9DyLPUQbOYa68Dn1KbbLdw3blz4ZDNOJ4ZJpo3s30uKuqia63ZnIF4NL2ZJ1ZqhoPXtn_2Wgd1dQDJlOqMIX96P8mdMhJ5eTIaoa2mv2_RKP0DQX5yszJUeOcFrH16y2JdKcXaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1144f5e406.mp4?token=hYKH6H8yob4ogJ0j6M3xKmOefWyB44h9sYGN50c9t4Uwye77mc6nQK2r6I2alpc65pEwUeLiUDerJRxB0L_Lx8FRBxB3fpjASA0uGf7zwHDjmQ6qxrQCdHFV7NAwRhb2DU6gw2dp2-TKioBuv_yhwcJDL-HWXSCFSsDpHvb2o-lM8QX02Ysdls6tcO6HW86fdu89h5m9Wf869yb9DyLPUQbOYa68Dn1KbbLdw3blz4ZDNOJ4ZJpo3s30uKuqia63ZnIF4NL2ZJ1ZqhoPXtn_2Wgd1dQDJlOqMIX96P8mdMhJ5eTIaoa2mv2_RKP0DQX5yszJUeOcFrH16y2JdKcXaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسنت: روزنامه وال استریت ژورنال گزارش داد که ایرانی‌ها در حال بازسازی ذخایر موشکی خود هستند.
🔴
شاید همینطور باشد، اما میزان و گستره این بازسازی چقدر است؟
🔴
ما ۸۵ درصد از کارخانه‌های آن‌ها را نابود کرده‌ایم. پس آیا آن‌ها هر هفته یک کارخانه جدید می‌سازند؟ آیا دو کارخانه می‌سازند؟
🔴
می‌دانید، این‌ها فقط تیترهای خبری هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/146888" target="_blank">📅 16:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146887">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a99219ae2c.mp4?token=TrPEWQ_tcU6XYQrFkD90W4qzE0OagQHDZhCAyHH9cCugmPD-DwUr2HSFPlLvAF4P4me0J4mO1Kbb64ZoaMLDL6-w-Wyz8pyN_bxOzRZ_yj7CaKvggUTfvdIZVZUZ7Y2DWJ2SGdJUWNOhYPyfMoTtTe_qtNeu2cQZFUUeBml6_XU-RHCpYcv6vtuJAor5zsdvihfRShsGQyOl6Ve6RweVZ_UaGrSuIU35OnVhtHoMMb1a_enYSOg1C7McfTD61RP61nzE6cKo-hcLQaVRV8GtNVwoMzLsiqSBVUPIpFbGc-qU8CMVLUDX2WTHoJqRNB_JNsAKf_MgDvJrcqUyQ9R68A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a99219ae2c.mp4?token=TrPEWQ_tcU6XYQrFkD90W4qzE0OagQHDZhCAyHH9cCugmPD-DwUr2HSFPlLvAF4P4me0J4mO1Kbb64ZoaMLDL6-w-Wyz8pyN_bxOzRZ_yj7CaKvggUTfvdIZVZUZ7Y2DWJ2SGdJUWNOhYPyfMoTtTe_qtNeu2cQZFUUeBml6_XU-RHCpYcv6vtuJAor5zsdvihfRShsGQyOl6Ve6RweVZ_UaGrSuIU35OnVhtHoMMb1a_enYSOg1C7McfTD61RP61nzE6cKo-hcLQaVRV8GtNVwoMzLsiqSBVUPIpFbGc-qU8CMVLUDX2WTHoJqRNB_JNsAKf_MgDvJrcqUyQ9R68A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: بریکس نباید صرفا مصرف کننده فناوری باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/146887" target="_blank">📅 16:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146886">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
پزشکیان: ایران آماده است در کنار اعضای بریکس برای ساختن اقتصادی بازتر و عادلانه تر تلاش کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/146886" target="_blank">📅 16:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146885">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/29761d0702.mp4?token=tm83Xg6xc6ooru370GadJ7FixWFAfz7O0S5BeMc4EBwEnvhZ0OOJhWsSoWj3zXTEo_O_ypVSSYvvDX2iQq1uWwiTBYH7CoyBEXhxNYny8Ziv0ntEatiO-udXD8TxEPIb7TqXyIYigfYpl-VyOVofD_uVhEE6wGn6NYtllVHjaroKGpm9wm-bLqgfYNkVpPfXEOY7JKgQrr-iZrHPuI-2XC89p7FxInLVHzCoGbQkTM0TnW8KHx_le1HV6tDCd3Ww2uhCPba0SpHjLc4PHZfOBGw2yvSlzW4HhvTYRuECAzZrwCvkN4FKVwxv7v9umCgWMC-suaHWg5qVl5GgoMekdA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/29761d0702.mp4?token=tm83Xg6xc6ooru370GadJ7FixWFAfz7O0S5BeMc4EBwEnvhZ0OOJhWsSoWj3zXTEo_O_ypVSSYvvDX2iQq1uWwiTBYH7CoyBEXhxNYny8Ziv0ntEatiO-udXD8TxEPIb7TqXyIYigfYpl-VyOVofD_uVhEE6wGn6NYtllVHjaroKGpm9wm-bLqgfYNkVpPfXEOY7JKgQrr-iZrHPuI-2XC89p7FxInLVHzCoGbQkTM0TnW8KHx_le1HV6tDCd3Ww2uhCPba0SpHjLc4PHZfOBGw2yvSlzW4HhvTYRuECAzZrwCvkN4FKVwxv7v9umCgWMC-suaHWg5qVl5GgoMekdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: بریکس باید فضایی را ایجاد کند که هیچ کشوری نتواند تجارت مشروع کشورهای دیگر را مختل کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/146885" target="_blank">📅 16:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146884">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PAhovtRGFAnIUyKL8hNFRrBUjvyYOddRtWfH6nrPX6HIpC1r4vtIEsWB4tLuCjY_945WYlVHRqiRAS6b3qppqlPhg1-Tvfg8h33A2XJYazYXj-f8E2HDlzufObdXUV96QzOsC_qbIE-9d4wlUlBIGmzwS4uaboX8GbfKIA_tfCz2KG32GS8KH-vEwv2iUTkXCXgZOELHtRjhpiAUTEskIGDR-XQaBF4RlJaJp9zZjIAFpH1dfnDXsme0-y-oBIJ0fXaZM6LrNBJfaHh-UDrOGvUNwEeqGAWvNlC1nu7MiYFVLxdnVrFuow49R2nEjMrMZRuRBEJbaDMxkE6c3SKDdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان‌ملل با ۱۶۴ رأی موافق در برابر ۱ رأی مخالف تصویب کرد که نقشه مرکاتور کنار گذاشته شود و از نقشه "Equal Earth" استفاده شود که سایز واقعی کشورها را نشان می دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/146884" target="_blank">📅 16:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146883">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
علم‌الهدی: دشمن تا ۲۰۰ هزارسال هم بجنگه، باز دفاع میکنیم،‌ تسلیم نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/146883" target="_blank">📅 16:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146882">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad5d711ee2.mp4?token=adVhIP0YxUhUsixsfyDVE_Lh0xfZyPamKdtAu3dxyAwg1DVXEuLsWxcFsrSjv6h_KTvzzSfUuAc-OKTS1vSQjJs0MdAsLfMVx8W5rWzL7Szpo_ILHg2pofoTXKj05ziPd3Idj-fkA1GZxF-qfuN_FHFwnuBQrgPRV1KRFC3-x0iyRKZnUeqhj2cj02bhwM3xN1N8zCf7ynGYUGrIaPB0iSZfXs7YZ1QOEIfrmMxtvXyapU7_03DTfy-kehJjENTL2thhdKORlBMO_N7PHnE492YqlNM7MX9WeMIjieBw3XWrcJumSvn88kx6XtiV5xFmo1UYOAuo6p_UXCDK6Ani6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad5d711ee2.mp4?token=adVhIP0YxUhUsixsfyDVE_Lh0xfZyPamKdtAu3dxyAwg1DVXEuLsWxcFsrSjv6h_KTvzzSfUuAc-OKTS1vSQjJs0MdAsLfMVx8W5rWzL7Szpo_ILHg2pofoTXKj05ziPd3Idj-fkA1GZxF-qfuN_FHFwnuBQrgPRV1KRFC3-x0iyRKZnUeqhj2cj02bhwM3xN1N8zCf7ynGYUGrIaPB0iSZfXs7YZ1QOEIfrmMxtvXyapU7_03DTfy-kehJjENTL2thhdKORlBMO_N7PHnE492YqlNM7MX9WeMIjieBw3XWrcJumSvn88kx6XtiV5xFmo1UYOAuo6p_UXCDK6Ani6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عکس یادگاری سران بریکس در دهلی‌نو
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/146882" target="_blank">📅 15:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146881">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dcf6775e9.mp4?token=SBqPqYZYTarKADwB2i1P_rq21VH5yJQ1qG8lqTALgvC-neuIfWJlAjAo80_ruxPEFB7mDe7h7dTz43utAXHzOiK3IyyeizzPwZkhI7XtEHay5CKKoTkeZAloCCEWs0YR2LVi-VttKLyQ5KsH67eq1A4jyK4glT8CNguigP_TZuJd_3FKeLAbIWvKGO9UHYnkX8DVorHeBw5MNeV65-mqvmfqdisPblNM2BXvJO58qifAT_mBq2v-k5bRxI5FjEaUM-X8Jg-dDi8_KZFn1oSYPKvwNSP4gOwEgQnO0F7sdr6wg6QSwZixItMS4rVFoD0u5RGk3_QpyyzBuOPQRvU42g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dcf6775e9.mp4?token=SBqPqYZYTarKADwB2i1P_rq21VH5yJQ1qG8lqTALgvC-neuIfWJlAjAo80_ruxPEFB7mDe7h7dTz43utAXHzOiK3IyyeizzPwZkhI7XtEHay5CKKoTkeZAloCCEWs0YR2LVi-VttKLyQ5KsH67eq1A4jyK4glT8CNguigP_TZuJd_3FKeLAbIWvKGO9UHYnkX8DVorHeBw5MNeV65-mqvmfqdisPblNM2BXvJO58qifAT_mBq2v-k5bRxI5FjEaUM-X8Jg-dDi8_KZFn1oSYPKvwNSP4gOwEgQnO0F7sdr6wg6QSwZixItMS4rVFoD0u5RGk3_QpyyzBuOPQRvU42g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترکیه مرز بازرگانو به روی مردم ایران بسته و اجازه نمیده مسافرین ایرانی وارد ترکیه بشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/146881" target="_blank">📅 15:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146880">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
وزارت امور خارجه : گروسی گزارش‌های به اصطلاح بی‌طرفانه آژانس بین‌المللی انرژی اتمی را به ابزاری برای توجیه آغاز جنگ‌ها تبدیل کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/146880" target="_blank">📅 15:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146879">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6n_hBDeKk0CQN9hIJQ_WeVCcGZoU9cdQbGnOn90B7m-AHg5q7SFxocU76Nie-U8L4YyzKcqB1vUiNBiaxuzO3R6LEWkBrWxpGu8LSPz-3VPwkB1qKL7CJ0SBvm_7ES0FxKwcFFD37Vf9QdJaBCdvj6bg5zqbCVrXfR8obndg7f8oCZHdH2U8evnl3SOp4YwlEtNiIqDCNleY1TZoDSJwzXEMZAkbOm2o_L-yNt8NO8wytN3aTVIpLH8shFmNzwrsCfGVyjU5xiNDp4BIgIobUIc_k_pkEESI4jHHEnJ2hltGb9wZ0__5qzFlFOEF_UedvhqLomlFMiB5AjDVibY5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چندین انفجار در شهرک المنصوری در جنوب لبنان رخ داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/146879" target="_blank">📅 15:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146878">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
فوری / وزیر جنگ اسرائیل: برای حمله به حزب‌الله در سراسر لبنان آماده ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/146878" target="_blank">📅 15:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146877">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0be2bebccb.mp4?token=QZv_irP8zaoidShbo3-ELQCFvb7FeUZ7vrBI48gtp9Oe_87b4uFc_xqlp4UBlSnbIJA9IEPRWHQitynzIktIBrLDudzJgePU9zfJ3T3ReGZftCdW_RA2nJhV5nEnb-BaeOQXXBWxp0jESH5e45xnTyazlORuCWI9tnXL_EuG_KitmPttIyQ0RXd_JZVnVV5kAFX6WCMsDPPPo-4LxVJi6Nio1YqHZ5Au42eVr68MnECGGU8g5rETQStIS13vxINKyiO95SlA_BULfKHuA0NgeE0HJFmRIr5PjE9rrQq10DXojkobP1UdVRgHehgFgQgMl-WyuDubXcXPTPAq7jQeIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0be2bebccb.mp4?token=QZv_irP8zaoidShbo3-ELQCFvb7FeUZ7vrBI48gtp9Oe_87b4uFc_xqlp4UBlSnbIJA9IEPRWHQitynzIktIBrLDudzJgePU9zfJ3T3ReGZftCdW_RA2nJhV5nEnb-BaeOQXXBWxp0jESH5e45xnTyazlORuCWI9tnXL_EuG_KitmPttIyQ0RXd_JZVnVV5kAFX6WCMsDPPPo-4LxVJi6Nio1YqHZ5Au42eVr68MnECGGU8g5rETQStIS13vxINKyiO95SlA_BULfKHuA0NgeE0HJFmRIr5PjE9rrQq10DXojkobP1UdVRgHehgFgQgMl-WyuDubXcXPTPAq7jQeIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسموتریچ وزیر اقتصاد اسراییل : وقتی مردم ایران چیزی برای خوردن نداشته باشند دیگر چیزی برای از دست دادن ندارند و این باعث سقوط رژیم می شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/146877" target="_blank">📅 15:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146876">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcWIytHFei_xUED-7GXJmf7nkYzMSpyGhkJDXgV89bs1RRG3U52m4vC6VaHLIZ1WN2oZCvnKxy1UP4qnfqsTAztlirMOoz32mtzZvznKLux7TSJsz01rC8Dn1VYKwxfhiEcErDRV017EbQUCZABYS3QDc6crPh40TN4lejvYcxCEacLNbygHLkpF3sDPqHFV8xVopJQ2AylImKkbOcP_rhWryKljFR4meU2u_c_AKPWxjdhZwpnYkDyHzVrpT9V0D2Z1PFtHb4lg02UrHi7rtrKgKKF7XWoCG6IwS1rHCtixzDpf0CgCePR346E5S0wblAVuNbt735J7iN5lohrHBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای یمنی به شورای محلی منطقه "ذو باب" در نزدیکی تنگه باب المندب رسیدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/146876" target="_blank">📅 15:18 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

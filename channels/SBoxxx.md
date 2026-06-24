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
<img src="https://cdn4.telesco.pe/file/KmxajTR05LXVpvXVrAnJIfiEwi0FfwkckQI-kK26T89es_K9l2_tvx8_3VVtZr7jxvs_3MPmUTnSFFgS9OnPB-1gFjjC-D5c3NJo3KX33Y3LQ4Kw_7EsVsf8S3TGtXl0vDvV1pFs7nkc6o7LacvsB90gKCUI9DIeEVwKjHqWXA8idpN-t3oCu2AONrZlNV1pGjizWgcOtzFLekBBZpdMjEz65bhXTs_p-Th6yGcU0TSs568DaBel0Ls1M-l_ZKEAF6jsHz-Xe0OEB3vH7_7QxA9o8a6lc5iVKR-TJYlSa5LafuuULm1Tl6FERytOFhl2oI7dXzZgS-ldxtSLqX9ZPQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 00:37:27</div>
<hr>

<div class="tg-post" id="msg-17971">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ درباره اردوغان :
او دوست من است و از جنگ دوری کرد.
می‌دانید، او کاندیدای اصلی برای ورود به جنگ با ایران بود.
شاید در کنار ایران، چون همانطور که می‌دانید، طرفدار  اسرائیل نیست.
و من از او خواستم لطفاً دور بماند، و او این کار را کرد.</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SBoxxx/17971" target="_blank">📅 00:05 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17970">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506e64b21.mp4?token=ppAT-bTNjwYSS0kKycQXHLa667v2bH8QIp460jmuk3qaYIshCrA6CjTfFN1gXgdcZksqT1S7hrU7WzpFCwnLL1ui_z9cWi9dnkjbjBUimr97YVRt7OMlAuHdMyvDaf_6rfMkcQ91tbAczksXoiaYa21TeOsqNcoLvhjjIjsW-NqG7-p7IwNeHYo1eUNvoC1ioHciDx_Uv-0Wl3K60pkcHd1QRFAZ20Zk5bAxqUBQnIDgoIMRg_dpPyVqej2Y_wcA-rZHjDdFFoTjrI0M3rNGTF1t8xlnYXpuiyC23m7xjOcZ9VEO65JYCY-5Ulm6K1D6MTWoNunhMQEjaTeAVcO5cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506e64b21.mp4?token=ppAT-bTNjwYSS0kKycQXHLa667v2bH8QIp460jmuk3qaYIshCrA6CjTfFN1gXgdcZksqT1S7hrU7WzpFCwnLL1ui_z9cWi9dnkjbjBUimr97YVRt7OMlAuHdMyvDaf_6rfMkcQ91tbAczksXoiaYa21TeOsqNcoLvhjjIjsW-NqG7-p7IwNeHYo1eUNvoC1ioHciDx_Uv-0Wl3K60pkcHd1QRFAZ20Zk5bAxqUBQnIDgoIMRg_dpPyVqej2Y_wcA-rZHjDdFFoTjrI0M3rNGTF1t8xlnYXpuiyC23m7xjOcZ9VEO65JYCY-5Ulm6K1D6MTWoNunhMQEjaTeAVcO5cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/SBoxxx/17970" target="_blank">📅 00:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17969">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ادعای ترامپ: ایران امتیازات بزرگی می‌دهد  جنگ خیلی خوب پیش می‌رود. همانطور که می‌دانید، ما با اختلاف زیادی در حال پیروزی هستیم.  ایران امتیازات خیلی بزرگی می‌دهد. خواهیم دید چه اتفاقی می‌افتد.</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/SBoxxx/17969" target="_blank">📅 22:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17968">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ادعای ترامپ: ایران امتیازات بزرگی می‌دهد
جنگ خیلی خوب پیش می‌رود. همانطور که می‌دانید، ما با اختلاف زیادی در حال پیروزی هستیم.
ایران امتیازات خیلی بزرگی می‌دهد. خواهیم دید چه اتفاقی می‌افتد.</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SBoxxx/17968" target="_blank">📅 21:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17967">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">#USOIL — W  در تایم هفتگی به کف یک کانال معتبر هفتگی می رسد و از اینجا ریزش بیشتر توجیه بنیادی ندارد.  این یادداشت را هم بخوانید.</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SBoxxx/17967" target="_blank">📅 19:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17966">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbtZtwlQKcpZRI2NQbzWdpP-2-7ef0LUCa7GxYN9Py58GNXlyglfIskS9jRXpR7Cm3k2dI-dfYwAaJjwGmlJVjdrbRsSwf_MgqoLnAt0QkPWvxOZSUWISv2ufEpHGsUHGNzDE2asV2tvAOea0zuu6O6TVzuS7RX_RWyuOp0ADCVOECm8mxm4xkyER2o6iDg_KzXKA1RyOQmiRu64Laho_W0JGECsRlU5kwyanUSyJ2IjEANdg8pckI2O_Ol6x7qT0Llh_dgWegvKyx5ePb4VTZSotINX1PAic0lEjS-aeck4UDs_ipwjFau10Vs1wpbzfPyTv9lAMvgD3Mn_axoiIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — W  نفت همه رشدی را که به خاطر جنگ ایران تجربه کرده بود برگشت و اکنون در حال نزدیک شدن به نقطه شروع حرکت است و زین پس دیگر هیچ ریسک پرمیومی برای جنگ در قیمت لحاظ نشده.</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SBoxxx/17966" target="_blank">📅 19:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17965">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دلار 166 هزار تومان!
بخشی از این رشدها به خاطر کثافت کاری ها و باج هایی است که به طلاداران داده می شود. وقتی اونس سقوط می کند دلار را بالا می برند و بر عکس.
تارگت های 240 و بالاتر همچنان در دسترس هستند البته اما  این رشد دیروز و امروز برای این است که گفته شد.</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SBoxxx/17965" target="_blank">📅 19:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17964">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F99pQzLYCkgHK5Sq-vz7ShK_1iF2lgzJTNxSrz9uRzdNAH0oxB0w8_GdBtb_snQ-teQeL_5_yQKzlY2_xC7bzSY5hiUPP-g8iSzHb_Kpwy9pT2LFoUs-fx8m-vOAUmee71h8d4wrXoDmLWM9c2K9-YrbWKpluA6pMZh3r629ufdoBY5EZEaDzTMrgSuhHS30i-KRnjDjFmkJ__mPHBOwTbz3L-QW9xPOO3EVn0hdQVsREYTuqWHhZESSDOJbUEFBDn7ekXBZk-U-BwqYP7aWpk2q9o-ph-jBEPeO0XgXiOOp2_MlxZvi82WxfUr4RU-eAuD_BQgpa0aEB5GLUZJUzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H2  در محدوده مشخص شده می شود به دنبال موقعیتهای خرید باشیم.</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SBoxxx/17964" target="_blank">📅 19:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17963">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رئیس‌جمهور ایران مسعود پزشکیان رسماً نخست‌وزیر نارندرا مودی را به شرکت در مراسم تشییع و تدفین چندروزه رهبر عالی‌رتبه آیت‌الله علی خامنه‌ای در ایران دعوت کرده است.</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SBoxxx/17963" target="_blank">📅 16:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17962">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">رئیس‌جمهور ایران مسعود پزشکیان رسماً نخست‌وزیر نارندرا مودی را به شرکت در مراسم تشییع و تدفین چندروزه رهبر عالی‌رتبه آیت‌الله علی خامنه‌ای در ایران دعوت کرده است.</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SBoxxx/17962" target="_blank">📅 16:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17961">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">رویترز:   سپاه پاسداران انقلاب اسلامی سلول‌های مخفی در عراق ایجاد کرده تا حملات پهپادی علیه کویت، عربستان سعودی و امارات متحده عربی انجام دهد. این سلول‌ها از جنگجویان شیعه نخبه عراقی تشکیل شده‌اند و مستقیماً به سپاه پاسداران گزارش می‌دهند؛ بین آوریل و مه حداقل…</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/17961" target="_blank">📅 16:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17960">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">حقیقتا «الکسیس میانرودان» لقب شایسته ای برای عراق نیست؟!  تل آویو - اسرائیل برای پشتیبانی از عملیات هوایی خود علیه ایران، یک پایگاه نظامی مخفی در صحرای عراق ایجاد کرد و حملات هوایی علیه نیروهای عراقی انجام داد که تقریباً در اوایل جنگ آن را کشف کردند.  به گفته…</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SBoxxx/17960" target="_blank">📅 16:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17959">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lb_smU8wtPmsM9MnBRKzbHhZcm2P9pDu42KBQuiTvwi_F1S6Idh0ny_S-1NFiwx4PzH4KknH-NmqLbqW8HSg8WOLiZYIeDTfdUYqxWx8ODKJ5eclPoiHNB3yF9iskpABNB84wBeo_U9dLQLTaYyqnYrYZk1axbWrcNTQGAgO71rgWKgCql-VlIFBSfA8ui_J6SewI9VB-kfOqIbZKfS42-Ykqh6BBLil6OdZues6NMVIaTp_tTJwb99yXiY2ZoBgHnrTPMJEpQBQUnj1uce3aprM71jdhyFSx1U6K37Sb9Koc4knRPh9Q376ov-UX5XOl84ct6H2MuJU6PvcgArHLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#DXY — W  پس از یک سال رنج زدن، شاخص دلار به صورت کوبنده ای رهسپار تارگت های اعلامی شده.</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SBoxxx/17959" target="_blank">📅 16:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17958">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2cSK-BgPjwHnaifdBY_Jo6RCjwcfWhfMGVpxOPiVPkhffyKTwB6JSDq3gK8BEaGiTvevqhlnToxAqVKwx-0dBp7F08T0q2xwAzaI5UOL5lu9tfB3YwILUtcDlJ3bFs_V1gr0JoJ1EQMZOXXt3fpN5BcqswgUWVkqYsqLCAIpgaIaHAgOIgqmBDbCwr-8dgzeQ9YvmxY4l7LkaXjZQfA_24kStzoL9fBcu7WaKwsBmWlRGyScCOpCEImpL23FrfZjwj1KOOdx60G_cVD60Ylci4zftLD_ajaVja43ML3ZMHNnSX-ugJA7AG4muFQkQ3GXYrMpBVWlFawYIruA3AMcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#DXY — W  رسید به کف کانال هفتگی!  از این هفته فروش دلار که ممنوع است هیچی، خرید هم در دستور کار قرار می گیرد.</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SBoxxx/17958" target="_blank">📅 16:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17957">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ: ۵۰۰ میلیون دلار در ابتدا برای خرید کالاهای آمریکایی به ایران داده می شود</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SBoxxx/17957" target="_blank">📅 15:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17956">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/925922fd6b.mp4?token=dOntI4LBVZLtEVE3WPDwHEAkVRJ_99ebE5d44XwUmslOZQSEmPd-a_VH8KrxIBhtYogRix7ch3_JmTBhpG_sr98gFTInqOrEMPmMkAo9XD2VapACodId_tsMNQX52XGWPDAlK09guSt_QEqWOLDQ7bIAmbhvNjWFaG7WBS0-FMI3NTMhEOZFtqi5TwN-42KrIXgZg5k6SDx6h4vt8vwK7_4B-EZEiOYMSiBBPxb5dYSTUZ0pK0q5KTmhZZ5_uFfGhsWoQg9df4bC8BwyO7MaS8Q1sOKqWl57SihNshxLDBVvRCEwsZkJwzCYwAJDQ0zpRINy4M-Vpd86C9tawrMFjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/925922fd6b.mp4?token=dOntI4LBVZLtEVE3WPDwHEAkVRJ_99ebE5d44XwUmslOZQSEmPd-a_VH8KrxIBhtYogRix7ch3_JmTBhpG_sr98gFTInqOrEMPmMkAo9XD2VapACodId_tsMNQX52XGWPDAlK09guSt_QEqWOLDQ7bIAmbhvNjWFaG7WBS0-FMI3NTMhEOZFtqi5TwN-42KrIXgZg5k6SDx6h4vt8vwK7_4B-EZEiOYMSiBBPxb5dYSTUZ0pK0q5KTmhZZ5_uFfGhsWoQg9df4bC8BwyO7MaS8Q1sOKqWl57SihNshxLDBVvRCEwsZkJwzCYwAJDQ0zpRINy4M-Vpd86C9tawrMFjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خارجی ها مخ شان سوت کشیده و فکر می‌کنند بیرانوند راننده یک تراکتور است!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/17956" target="_blank">📅 14:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17955">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یسرائیل کاتس، وزیر دفاع اسرائیل:
«حتی اگر از سوی آمریکا درخواستی مطرح شود، ما از لبنان عقب‌نشینی نخواهیم کرد.
دویست هزار نفر از ساکنان [شمال اسرائیل] هنوز به خانه‌های خود بازنگشته‌اند.
ما تمام رهبری حوثی‌ها را از بین برده‌ایم، به‌جز عبدالملک الحوثی که در تونل‌ها مخفی شده است.
اگر او در تیررس قرار بگیرد، کشته خواهد شد.»</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SBoxxx/17955" target="_blank">📅 14:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17954">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GSA5lJkE5cq6fWPQsWRMAHS4oPcpVhhzreRsxxRUg9UnNrcsKNukqWFgT3yomD-6VpAOU60kElH8Vxfp-iWgOMeWumLJWtme2nwYgQnNfxV5a53zhsqTCcf_J3BmXYXzccGMZKNrUHBH1xzvGIlwcaXA50s8AvyUiHn0rYJKb0KF-k0DTB3pk6foWBs3J24vgp7uTLIJV5NHZQhadTldNsBm9e0PjsaeCWi8m9bbiNT5fEs05gKHm_ku01IquEtXcQw5Sf1Wwbu14i-6kXAQJ01FfCkhPMepnctfQ4jJrbzP_8JDpr1jvK_wmfq-jyd4FArZVje9GbPM9Z4ZCjQVCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SBoxxx/17954" target="_blank">📅 14:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17953">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrGK8RuLDjZlsittil98QWpmeaiFkvxrVhVSnaYVFWREqb1tIsVm7-MzkdFNeLdik1mza4VZHJwmDDvJRweGOaXWD1bLnLT0WU47XuwSn8JxcVtbRWymGukphuxJOYlR8OJEFMqLbngMrZZS2hGdPuaWu1i_r4ucA1D8MVKSikSnuzJVacJ2p5tdtXa4Q64SYgukGdo_AG1K4UHQp-ZxXC3Kj4O-Rask3vgwK54A5g18dzsCCNZnWP9dfQW6W3k-FrrQ3LllGXx7sj-htPRT3TU9RLW7uPH593bIlMb0xRZjs17eudLgVfzZ2uw16lS_GhHKzV7X3DPsunnVz984zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#طلا
بر اساس نمودار، احتمال ثبت یک کف دیگر پیش از پرواز دوباره قیمت بالا است.
بهترین محدوده خرید میان مدت 14.2 میلیون تا 14.9 میلیون است و تارگت حداقلی 29 میلیون تومانی فعال خواهدشد.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/17953" target="_blank">📅 12:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17952">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">هاآرتص، با استناد به منابعی در ارتش اسرائیل:  ناامیدی و احساس ناتوانی در میان افسران در لبنان به دلیل عدم قطعیت ایجاد شده توسط اقدامات نتانیاهو و کاتز.</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/17952" target="_blank">📅 12:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17951">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">برخلاف تصور رایج، «لابی کشاورزی آمریکا» یکی از قدرتمندترین ائتلاف‌های ذی‌نفع در واشنگتن است. اما این لابی یک سازمان واحد نیست، بلکه شبکه‌ای از انجمن‌های کشاورزان، اتحادیه‌های تولیدکنندگان غلات و شرکت‌های بزرگ کشاورزی است.  نکته جالب اینجاست که این لابی، برخلاف…</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/17951" target="_blank">📅 10:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17950">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">توییت ترامپ در مورد ایران:  با وجود اعتراضات و اظهارات نادرست آنها، همراه با تبلیغات مکرر اخبار جعلی که همه تلاش خود را می‌کند تا پیروزی آمریکا را کوچک و بی‌اهمیت جلوه دهد، ایران به طور کامل و جامع با بازرسی‌های هسته‌ای در بالاترین سطح برای آینده‌ای نامحدود…</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/17950" target="_blank">📅 10:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17949">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">هاآرتص، با استناد به منابعی در ارتش اسرائیل:
ناامیدی و احساس ناتوانی در میان افسران در لبنان به دلیل عدم قطعیت ایجاد شده توسط اقدامات نتانیاهو و کاتز.</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SBoxxx/17949" target="_blank">📅 09:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17948">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتحلیل و رصد</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a0802e26a.mp4?token=VArKmKX8hWnB2WZ6ip8t3qOtr_q-0CrfJNicsrGw5iaPKNt3g8TtOf6ylc4ejJhu-pXNoduBESLA5NtVNR_k2nghEXaYt8xV1ZsDsFtabJ1dbX4lJ1e_bjn0cdtuoairX3sG47wv8T7vyG9IUPnIzEB5iCoPPk-KCi0y-lSYj63OdRLgyA-T3KtHgH7kWlcnQnazzDrzLa7N4_OyvKQlGwdNaQvJsE-w7wYAXUHMxAOwN64DUQ-J6aGK73UHSMxUCWYdsElLrQalpYKmFPC9GhR-nfAufJLwmIia-SyEOf-Mv8bHDy6EHQ3mgdpOTk0inXmxZQwljCEwWSNJ15WzDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a0802e26a.mp4?token=VArKmKX8hWnB2WZ6ip8t3qOtr_q-0CrfJNicsrGw5iaPKNt3g8TtOf6ylc4ejJhu-pXNoduBESLA5NtVNR_k2nghEXaYt8xV1ZsDsFtabJ1dbX4lJ1e_bjn0cdtuoairX3sG47wv8T7vyG9IUPnIzEB5iCoPPk-KCi0y-lSYj63OdRLgyA-T3KtHgH7kWlcnQnazzDrzLa7N4_OyvKQlGwdNaQvJsE-w7wYAXUHMxAOwN64DUQ-J6aGK73UHSMxUCWYdsElLrQalpYKmFPC9GhR-nfAufJLwmIia-SyEOf-Mv8bHDy6EHQ3mgdpOTk0inXmxZQwljCEwWSNJ15WzDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">.
🟢
وقتی دکتر مسعود، نمی‌تونه از کاراکتر دوره جَوونی‌ش فاصله بگیره!
پزشکیان [در سفرش به پاکستان] به نشان دوستی یک درخت تو اسلام‌آباد کاشت که رسم پاکستانی هاست.
ولی نکته جالب اینه که هی شهباز شریف نخست وزیر پاکستان اشاره میکنه مسعود جان بسه کم خاک بریز. نمادینه ولش کن. ولی مسعود هیچ رَقمه گوشش بدهکار نیست و فقط بیل میزنه.
@tahlilvarasad</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/17948" target="_blank">📅 09:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17946">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⛔️
کارشناس اسراییلی تشریح کرد: ۸ کانون تنش بین ترکیه و اسراییل؛ ترکیه ایران جدید است  یک کارشناس اسراییلی با اشاره به اینکه تنش بین ترکیه و اسراییل به بالاترین حد خود رسیده است، به بررسی ۸ کانون تنش بین طرفین پرداخت.  ایتان لاسری بر این باور است که اسراییل…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17946" target="_blank">📅 23:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17945">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نخست‌وزیر پاکستان، شهباز شریف:
«کشورهایی هستند که می‌خواهند توافق را مختل کنند، و من می‌گویم که بدون ایران نمی‌توانند موشک‌های بالستیک داشته باشند. استانداردهای دوگانه قابل قبول نیست و منطقی نیست که برخی موشک‌های بالستیک داشته باشند در حالی که ایران از آن منع شده است.
یادداشت تفاهم (MoU) به مسئله موشک‌های بالستیک ایرانی اشاره نکرده است».
«این یادداشت تفاهم به موشک‌های بالستیک اشاره نمی‌کند. هرگز روی میز نبود؛ هرگز در دستور کار نبود.
طرف ایرانی هرگز نخواست حتی درباره آن بحث کند».</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17945" target="_blank">📅 20:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17944">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🟢
پاسخ به توهم برخی درباره شکست احتمالی نتانیاهو</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17944" target="_blank">📅 15:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17943">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکاخ رسانه</strong></div>
<div class="tg-text">نفتالی بنت، نخست‌وزیر سابق اسرائیل درباره ایران:
هر بار که اعتراضاتی رخ می‌دهد چه اتفاقی می‌افتد؟ اینترنت را قطع می‌کنند و سپس هیچ ارتباطی وجود ندارد.
پس کاری که من شروع کرده بودم، فرایند تهیه و قاچاق ده‌ها هزار گیرنده استارلینک به ایران بود که اجازه می‌داد اینترنت و شبکه‌های اجتماعی وقتی قطع می‌شوند، ادامه داشته باشند و به اعتراضات امکان هماهنگی و در نهایت سرنگونی بدهند.
متأسفانه، دولت ناکارآمد فعلی اسرائیل این کار را متوقف کرد، همانطور که تقریباً هر برنامه خوبی که ما شروع کردیم را متوقف کردند.
و وقتی اعتراضات رخ داد، آن زیرساخت وجود نداشت.
@kakhresaneh</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17943" target="_blank">📅 15:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17942">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">توییت ترامپ در مورد ایران:  با وجود اعتراضات و اظهارات نادرست آنها، همراه با تبلیغات مکرر اخبار جعلی که همه تلاش خود را می‌کند تا پیروزی آمریکا را کوچک و بی‌اهمیت جلوه دهد، ایران به طور کامل و جامع با بازرسی‌های هسته‌ای در بالاترین سطح برای آینده‌ای نامحدود…</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/17942" target="_blank">📅 15:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17940">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KHkX7NWlk_RyMGxnLiuT24uBdLFwSWzdo8076HQesyLrm0r0rQTKXio80MM8PxltI1rv-4ZiXcG3iRmgpvxhrf6E-ZrPoVn-J2m075os8ze0K-r11Kp6UeMzIGwf-IVINeODM3Re8cyUINuuD_31ynKjsj_WrUSF4dX99ItQUh7Jks20ihiP4d7ASVQMPSq-frqOmNIbnODJzOihIbLGjI61D-AgWMcRfyZfM7WjVJt1zUlO9h9IvSV0OzDhWPSxM7sAqH3Ukz2LYFXIJuY-SYhsbodNz0e262m9_8Nrc2uLfSGTxTjKGKyflIyurDwwqRAgacrAqB0SQ9rnCkSbcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OrRzlcWx-OCXokf3YGaiCmDZLWPZvZCKc2__090roJUvoXHqnzITlaFgH0Av7EZVQ2wVCNJTtT7HqgFsvO6nu84YQGP5KkgLOnLMlnJ-YlGqmdse9E2UO71m5LEFFYwyRIN24w_eyfvBxJX6phid7zHmQug-ptckev3WVJ7qa-bKFz3AnwpLgwm7fori06gNODL4mYm2lPRYzItdeC7KZ405oHvqlkvpAYJ8RBLhil9eD90SRA5kUzoYKWOasrYxNkdu1IORigbNxbFRMZVPQnOqmzGVIVfgJccrHvBxuoRPvL9QFBFUhLrqQThiEKnlv4InB2lYws0knUmHpZcD4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر چه جلو میرویم داستان رابطه مسعود با شهباز
دارک و دارک تر
می‌شود
پناه بر خدا!</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17940" target="_blank">📅 15:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17939">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏
امیر پوردستان: آمادهٔ عملیات پیش‌دستانه هستیم
رئیس مرکز تحقیقات راهبردی ارتش:
🔹
در دکترین تهاجمی، عملیات پیش‌دستانه نیز تعریف شده است و چنانچه مصلحت نظام ایجاب کند، ممکن است با انجام عملیات‌های پیش‌دستانه در عرصه‌های ناشناخته، دشمن را به‌شدت غافلگیر کنیم.
🔹
نیروهای مسلح هنوز بخش مهمی از توانمندی‌های خود را عملیاتی نکرده‌اند و دشمن می‌داند که در صورت ارتکاب هرگونه خطایی، با پاسخی فراتر از مرزها و تنگهٔ هرمز مواجه خواهد شد.
🔹
در یک ‌ماه اخیر، ما چند نوبت تا پای جنگ با رژیم صهیونیستی رفتیم؛ لانچرها آماده و دست‌ها روی ماشه بود تا در صورت عدم عقب‌نشینی اسرائیل، جنگ آغاز شود.
🔹
تهدیدات قاطع ایران سبب شد تا آمریکا برای جلوگیری از گسترش جنگ، به رژیم صهیونیستی برای توقف تجاوزات به جنوب لبنان فشار بیاورد.</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/17939" target="_blank">📅 15:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17938">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">توییت ترامپ در مورد ایران:
با وجود اعتراضات و اظهارات نادرست آنها، همراه با تبلیغات مکرر اخبار جعلی که همه تلاش خود را می‌کند تا پیروزی آمریکا را کوچک و بی‌اهمیت جلوه دهد، ایران به طور کامل و جامع با بازرسی‌های هسته‌ای در بالاترین سطح برای آینده‌ای نامحدود (بی‌نهایت!!!) موافقت کرده است. این امر «صداقت هسته‌ای» را تضمین خواهد کرد.
اگر آنها با این موضوع موافقت نمی‌کردند، مذاکرات بیشتری صورت نمی‌گرفت! بر اساس این و دیگر امتیازات عمده‌ای که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و هیچ محاصره دریایی بیشتری اعمال نشود. با این حال، همه کشتی‌ها در محل باقی می‌مانند تا در صورت لزوم محاصره دوباره برقرار شود، که در این مرحله بسیار بعید به نظر می‌رسد.
پول و/یا تحریم‌هایی که خزانه‌داری آمریکا آزاد می‌کند، در حساب امانی تحت کنترل آمریکا قرار می‌گیرد و صرف خرید غذا و تجهیزات پزشکی، به طور انحصاری از ایالات متحده، از جمله ذرت، گندم و سویا از کشاورزان بزرگ آمریکایی ما خواهد شد.
این‌ها چیزهایی هستند که ایران به شدت به آنها نیاز دارد. این یک بحران انسانی است و من احساس می‌کنم لازم است که اکنون کمک کنیم، قبل از اینکه خیلی دیر شود. مذاکرات به خوبی پیش می‌رود!</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17938" target="_blank">📅 14:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17937">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🟢
طبق اعلام معاون اول مسعود پزشکیان ، در راستای برگزاری مراسم بزرگداشت رهبر فقید جمهوری اسلامی ایران ،  13 و  14 تیرماه استان تهران و 15 تیرماه کل کشور تعطیل خواهد بود</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17937" target="_blank">📅 14:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17936">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">⛔️
دولت ترامپ ، دسترسی به 2 مدل هوش مصنوعی آنتروپیک را برای کاربران غیرآمریکایی مسدود کرد</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17936" target="_blank">📅 12:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17935">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپارادوکس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c175d38c15.mp4?token=tyN3_IpFkATthZ_nxaxz4oaxzWAHMjtzP1KiKwN88igEmDZ3zuKq5Lvzlb9RLq_9y-kN9HaMaWMbMukwHgv110SayepmnSoT85zMDeyfgR5pZrJEexg81ZkHysmPKof5c3O32a2wbZ1yFL1UDO1ufEKnnuGMpTEwM1MHVyvfHcqDzaXcYM5eCmLscxdahn4fQUVMDaZV5CZaJQMfJc92Q4k0nD6my5eNEO3vHvVee21phAw-iyg-Y5sOctSKUs6HkgvbVY9ISdPfz7vu4TK64BQZNujQqAN4TpLxvkZEWMJGWI_vrHFAHw22STYIbqGKgRfi0bQvP9YlNbQke2AGKhFs2lhVSFNxNCi25QDnSxv3vP4kqOoILf4kGTugR-rCkv7Rrt8bAO2W2xLHeOmgbRLW75J0HcX1EBDkMq7PXfvq-8jF9toInV8XP__4cXK4myk1WjNWFo4q2vr1YG3Mm1OpsE_gqF_xhP4pdegnVD1tbEB3q4QDKbMHAUOXD8wPze9xnrCigEi_wL3U8JsKvdx85KjHwvn8AbDwDD9XN-z3MC8BaQYeqSntb3exGKb_n8o-7mrjdRUlseIV2kQje6mr-JYo9S2OSUlhFJ_wcG6uBzXkvO9IN36yJ6U0_WVWyYBabgVlfLLTiBgLxuQm81Yhw3Ey3_v9FIMkk_OpfWo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c175d38c15.mp4?token=tyN3_IpFkATthZ_nxaxz4oaxzWAHMjtzP1KiKwN88igEmDZ3zuKq5Lvzlb9RLq_9y-kN9HaMaWMbMukwHgv110SayepmnSoT85zMDeyfgR5pZrJEexg81ZkHysmPKof5c3O32a2wbZ1yFL1UDO1ufEKnnuGMpTEwM1MHVyvfHcqDzaXcYM5eCmLscxdahn4fQUVMDaZV5CZaJQMfJc92Q4k0nD6my5eNEO3vHvVee21phAw-iyg-Y5sOctSKUs6HkgvbVY9ISdPfz7vu4TK64BQZNujQqAN4TpLxvkZEWMJGWI_vrHFAHw22STYIbqGKgRfi0bQvP9YlNbQke2AGKhFs2lhVSFNxNCi25QDnSxv3vP4kqOoILf4kGTugR-rCkv7Rrt8bAO2W2xLHeOmgbRLW75J0HcX1EBDkMq7PXfvq-8jF9toInV8XP__4cXK4myk1WjNWFo4q2vr1YG3Mm1OpsE_gqF_xhP4pdegnVD1tbEB3q4QDKbMHAUOXD8wPze9xnrCigEi_wL3U8JsKvdx85KjHwvn8AbDwDD9XN-z3MC8BaQYeqSntb3exGKb_n8o-7mrjdRUlseIV2kQje6mr-JYo9S2OSUlhFJ_wcG6uBzXkvO9IN36yJ6U0_WVWyYBabgVlfLLTiBgLxuQm81Yhw3Ey3_v9FIMkk_OpfWo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
⭕️
چگونه نام تاریخی و ریشه‌دار دریای کاسپی (Caspian Sea) با یک ندانم‌کاری آقایان پر مدعا خدشه‌دار شد؟!
یکی از تلخ‌ترین لحظات تاریخ معاصر، روزی که حیدر علی‌اُف، رئیس‌جمهور وقت جمهوری باکو، به ایران آمد و در دفاع از نام «خزر» سخن گفت، حال آنکه سید محمد خاتمی، رئیس‌جمهور وقت ایران، نتوانست با تکیه بر اسناد و مستندات تاریخی، از نام‌های اصیل و ریشه‌دار این پهنهٔ آبی همچون «دریای مازندران»، «دریای طبرستان»، «دریای قزوین»، «دریای گرگان» و یا نام بین‌المللی «Caspian Sea» پاسداری کند.
او در برابر آن ادعا سکوت پیشه ساخت و حتی با صدور بخشنامه‌ای شرم‌آور، این دریای کهن و ایرانی را به نام قومی وحشی و بیگانه، «خزر» نامید؛ نامی که هیچ پیوندی با هویتِ تاریخی و فرهنگی ایران‌زمین ندارد.
⚜️
@paradox_p
⚜️
پارادوکس
⚜️</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/17935" target="_blank">📅 11:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17934">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gM0I8xMoXV9PAewqQiBh5nq3E6FLlkVyXxXqjPItoz4Ik1joMoX23m-WrY_xRt3PukPMUoZRD7xb3HzqIDLIIVhD7quxYKGh0gxDRk8FFrDuFgSUNCX1PO8PpK-1he6j8dB0txLE1n5Y0FMEIy2CK1pebHjxN1a5mIA0jzcC7lF6o9fhDtB52Z2aemzezIm2y9Paym988yO5Ix5bvlj7rkFA524IeuayVBPNaIrELAdA1gkjlSh6AnHWOjMZJBFOF_yw0KtWc8jNCp5wm-FvBfIj0-5_RKgw_veZIGy0wr8lfnkBCkoJe7JIwvCd1GOuKcQ_AbRV7ieUwWJZ1lZKvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت استاد!
از تبیین کوانتومی آفرینش و پایان هژمونی دلار با ظهور بریکص رسیده اند به رفع نیاز جنسی با دوغ!</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17934" target="_blank">📅 09:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17933">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">این را در دیدار حضوری با تیم ایرانی گفته اند !  پس دارند میگویند اگر کشتی از بخش جنوبی تنگه هرمز عبور کند، عوارضی پرداخت نخواهدکرد  اما اگر از بخش شمالی تنگه که تحت مدیریت سازمان معظم تنگه خلیج فارس ایران است عبور کند باید پول عوارض بدهد!  خب شما به عنوان…</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17933" target="_blank">📅 07:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17932">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">این را در دیدار حضوری با تیم ایرانی گفته اند !  پس دارند میگویند اگر کشتی از بخش جنوبی تنگه هرمز عبور کند، عوارضی پرداخت نخواهدکرد  اما اگر از بخش شمالی تنگه که تحت مدیریت سازمان معظم تنگه خلیج فارس ایران است عبور کند باید پول عوارض بدهد!  خب شما به عنوان…</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/17932" target="_blank">📅 07:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17931">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وزیر خارجه عمان:    به قانون بین‌المللی و تضمین عبور امن و بدون اخذ عوارض از تنگه هرمز پایبندیم.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/17931" target="_blank">📅 07:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17930">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نخست وزیر و وزیر امور خارجه قطر در مصاحبه با الجزیره:   آنچه ایران در طول جنگ با ما و برادرانمان انجام داد، غیرقابل قبول است.  اجماع خلیج فارس برای دستیابی به دیدگاه مشترک برای گفتگو با ایران برای حل مشکلات وجود دارد.  ما می‌خواهیم شاهد همکاری ایران با کشورهای…</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/17930" target="_blank">📅 07:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17929">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2vyNeS-U6OUzdX2HjWQWqHLfsfcchZDCz3qVM7xcO9veBmSczTQVBv9_pxWwA_mbyYIZbetSrJn2xcUEFFLAPqp347xU_QYW76ZVb-l5CW5LE04IDQVBSSW5J2A0-h5lOtAJoJrsTNnwe5KzMW8tPtLco_ce1VO2xNQ0e87a1KfPzES_gKhFL6HMsK7tKeblc4iqgsN0eF4ZXVzzmDBcUuq-5uq-F88e10XbD4kQjXYL6wnuJdp05srB3Z7XJs73Igh7n9jwa4BFNzLrmGJKWlXyzB2UUtCvJatDmouwYqdkbPXRf6lgdqWugGTYvDEzDZxMU8q2caw-zn70gmBKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همتی رئیس بانک مرکزی:  ما سالانه نیاز به‌خرید میلیاردها دلار مواد غذایی و دارو داریم پس چه بهتر که در ازای دادن پول‌های بلوکه شده آن را پرداخت کنیم. البته بخشی از پول را هم میتوان صرف کالاهای غیرتحریمی کرد. به هرحال این معامله با آمریکا برای ما سودمند است.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/17929" target="_blank">📅 01:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17928">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">همتی رئیس بانک مرکزی:
ما سالانه نیاز به‌خرید میلیاردها دلار مواد غذایی و دارو داریم پس چه بهتر که در ازای دادن پول‌های بلوکه شده آن را پرداخت کنیم. البته بخشی از پول را هم میتوان صرف کالاهای غیرتحریمی کرد. به هرحال این معامله با آمریکا برای ما سودمند است.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17928" target="_blank">📅 01:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17927">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سرانجام کتابی که وعده دادم درباره پیوند ژئوپولیتیک و بازارهای مالی ترجمه کنم، به چاپ رسید.  به نظرم در این شرایط که چندین جنگ همزمان در منطقه و جهان در جریان است و تنشهایی که میتواند بزودی تبدیل به جنگ های دیگری بشود، فقدان وجود یک دیدگاه تحلیلی چهارچوب بندی…</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17927" target="_blank">📅 01:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17926">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔹
شبکه ۱۴ اسرائیل :  بنظر ما ، جمهوری اسلامی ایران به سلاح الکترومغناطیسی دست یافته و با استفاده از آن درحال تاثیرگذاری دلخواه روی مغز ترامپ است - رفتار های دونالد ترامپ هیچ شباهتی به قبل ندارد</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/17926" target="_blank">📅 23:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17925">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔹
شبکه ۱۴ اسرائیل
:
بنظر ما ، جمهوری اسلامی ایران به سلاح الکترومغناطیسی دست یافته و با استفاده از آن درحال تاثیرگذاری دلخواه روی مغز ترامپ است - رفتار های دونالد ترامپ هیچ شباهتی به قبل ندارد</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/17925" target="_blank">📅 23:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17924">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pt1-cUDKJEN-IQgNoyymOReHYNeLrOUdhK9gfxiFkZBzh39Ces37BSV4vKKMGoZ-e2PovdiaD27l-XPOs7fCWaT5XMJ3Y09qPfzwbXlUxR4efagv7hggYoZEtKvv44YnaySP3NlONQQntJiGhhCUE5DeGnv4yyYlDA_SUIEp_qgLnPEDf8c4UgZGw2uEV7TsiiHGc7FiEaOXXnsO49jYk8ZYiuYD67q8ZgR4qdq4n1pya-uITpas-DEvzOpSUoArg8O7V4ks3lf6ANBDcvtKTRsgFVDWlvSmdQQWgnVIdU9hiae_PZc1Qz9_o0jRErrQcPX9fGKa7sLMNo6CE6yl2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوستالژی هر ساله ما آغاز شد…
جای کیان رویگری خالی…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17924" target="_blank">📅 23:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17923">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">المیادین: هیأت ایرانی تا زمانی که ترامپ عذرخواهی نکند و اسرائیل از جنوب لبنان عقب نشینی نکند، به مذاکرات باز نمی گردد!   ایرانی‌ها اکنون تنها خواستار توقف تجاوز نیستند، بلکه خواستار خروج (نیروهای اسرائیلی) از جنوب لبنان هستند.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/17923" target="_blank">📅 22:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17922">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">هند قصد دارد موشک های کروز سوپرسونیک BRAHMOS را به ارمنستان ارسال کند</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17922" target="_blank">📅 22:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17921">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ:
همه کاملاً آگاه هستند که ایران موافقت خواهد کرد تا بازرسی‌های نظامی انجام شود تا «صداقت هسته‌ای» را برای مدت طولانی در آینده تضمین کند.</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/17921" target="_blank">📅 20:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17920">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">خوش‌چشم، کارشناس صداوسیما:
آمریکا خودش تاسیسات ایران را نابود کرده است و حالا می‌گوید در بازسازی آن‌ها سرمایه‌گذاری می‌کند تا در سود این صنایع شریک شود/ به جای خسارت دادن می‌خواهند ایران را استعمار کنند و ۵۰ درصد سود صنایع ایران را کسب کنند</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17920" target="_blank">📅 20:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17919">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مرندی:
🔻
ایران قصد خرید کالاهای کشاورزی آمریکایی را ندارد و دیروز هیچ بحثی در مورد آمدن بازرسان آژانس بین‌المللی انرژی اتمی‌به ایران صورت نگرفت</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17919" target="_blank">📅 20:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17918">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">تهران توافق برای اجازه ورود بازرسان هسته‌ای به ایران را تکذیب کرد  خبرگزاری تسنیم ایران گزارش‌های مربوط به یک پیشرفت بزرگ را رد کرد و گفت که هرگز به بازرسان آژانس بین‌المللی انرژی اتمی اجازه ورود داده نشده است و ترجیح می‌دهد که هرگز نیز چنین اجازه‌ای داده…</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17918" target="_blank">📅 20:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17917">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrJ3o1YYS5jvTLJl8c7rvjW0J7CDdBCEelKfaBoYWe2LDJ2sWsunJ1sWzQFfC3s7CE81dYWg0njRwiBMChopPLULOiG3Sz1pl2odpLy5NFhyt9QNWTYEASb4BCV3pk9Dr70tG8SL0stO-oGY_KXPMtrZm-3-NWEBRrT0ct9hiD4i5rd7fdgUP5tFcTv4ikQwOCnxKmtXvdnESrVzLxMMi8FbDmg7vkF2Wrk3C7zTfpBzF8XMWFXJIPRURsV9IIo9oXBivTBQoWrje8S9IFfFF1TZQprtAPzXJczBCVLnslSmH5MubVtUPCfCj-nCU8u5bM0FMM73xPFLd0gEGgvyrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه ایران و انیران خواستار ابطال این پیمان هستند جز باقر!</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17917" target="_blank">📅 19:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17916">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">خردمند کسی نیست که بتواند میان خوب و بد، خوب را برگزیند، بل کسی است که توان تمییز خوب از خوب تر و بد از بدتر داشته باشد.</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/17916" target="_blank">📅 19:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17914">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hxlPwtauPfES_R7ehJZuInEH4duV6V7ER4qZcEzRPtdcf4NujoWXf7yVoGiKR1WnnVO3wYhPt28U_GF-mFzulkLXTddQq-dVkkBk2dAUHFWkRQupcOzCbA5iSiW_DpCQUKw93LRlY7SHQnonlrtKzWdFmcuvDbUlVWMus-pDmNtEwtcbQsprqhlRYcVdUoLD9Un3qBG3kItJMdVGyeEvMYqQWpz1lkHqH4b8i67mGkWjRTNqLN8gwkwplAmV6sIqF8bj3BESq-HA-NsSYxn29HVtcCZOPLTX0H_yaFlEnR8uOM0809MqNxhdFrcVg-bCscOQF4c7hfPh_1oAxzaLgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T6hLsUD7ylvTLbvmZUH0vCSBK_xzfTzetXhteCDE5OQFON4wKg5_RUgMvoDP5Jeo6cLKs-eOXbkjPwkxrgVRmq8BnyIrnhNbO1Xs228VszCFo6I2qKW5LeDc0NFyt7noVHTM-txIDXkOLef3irQjk0IcW54iMb6Gjn94LSHtTEnJqJuCYSGFJDaId92AEoxdFh2fPn6j_46jOsw31oW8cD7s18WzaEUGE5aJ0T9hQFxlTIgpkmT367VUNn30tf0db6j-Nz9kDHOthxQLX5DvrdnLJLBulyCGj4hwZu_MM9ocrU_KvGSzwCw9wSegnnWr_2oMXh1_hkWtX9MpLIAUpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نمیگذاریم اسراییل بزرگ تشکیل بشود اما خودمان دنبال توران بزرگ هستیم و این نشان می‌دهد چقدر مادرقحبه هستیم.</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/17914" target="_blank">📅 19:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17913">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromیدالله کریمی پور</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngu9hweX2jKdrNrNin8mNeitmHIVKlgQmefmS_L1CMZf4n84GX0v2JfE0rZBWgFTY_s1udZHvCRch86ct4HeZi1fBGzqRujA-NXDZPT-p9Vo1PuF2EF0mcDpBp-UBxrglrXRHFOQt8gKnaHOU0VKROBbRuOm_vaihVqOV8slCHiIb-pSDG1bSTui3N6OkpgXVnrqRJO0gxLeb6o6hztwpqwfqEKuqFQS1ttXSW3zAAR9ByD1POQKgKqgaBxNQ4TVVUrn5SSt2CcHRlbwMp509GbjU7WnICt3m_J2QjFR3w0s4tgvUvI_VSqY5X2AjT9BWrr14j1OetNhgTVg_Cx3oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو دشمن اصلی ایران
این‌نقشه، راهنما و توضیحاتش امروز یکم‌ تیرماه(۲۲ ژوئن)‌ از یک کانال تلگرامی نظامی اخذ شده است. بر نقشه و راهنما متمرکز شوید:
"کوریدور خیانت؛ تمام حملات هوایی به تهران و حومه، از این مسیر و به طور روزانه انجام میشه... آذربایجان، ترکیه"
کاملا درست ترسیم کرده و نوشته است. باور کنید در جنگ‌های ۱۲ روزه و ۳۹ روزه، تقریبا هر شب و روز‌جنگنده ها از بالای سر من میان البرز می گذشتند.
ولی این کمترین سزای حکومتی است که حاضر به گوش دل دادن به پژوهش های بیطرفانه نیست.
بیش از ۲۵ سال پیش، پژوهش های طولانی مدت و استراتژیکم طی دو جلد کتاب با عناوین: مقدمه ای بر ایران و همسایگان (منابع تنش و تهدید) و کتاب: مقدمه ای بر تقسیمات کشوری(ج یکم)‌ منتش شد . کتاب هایی که نه تنها سرداران آن را خواندند، بلکه مقدمه ای شدند برای اجرای پروژه اطلس استراتژیک ایران. پروژه ای که بارها برای سرداران فیروزابادی‌، شمخانی، باقری، سلامی و ...سرلشگران زنده گزارش شد.
میدانید چکیده کتاب ایران و همسایگان چیست:
دو دشمن پابرجا و اصلی ایران ترکیه و جمهوری آدربایجان هستند.
ولی کو گوش،شنوا.
#یدالله_کریمی_پور
#karimipour_k</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SBoxxx/17913" target="_blank">📅 18:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17912">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/It7inTe0jEUKYYVgRkiIisZ3zorr_Gr6qj-zCqwG4nGOadx8s0Qnp9ZLbxHkKWL5oetH1sS80R-8vX_JO18VMnctVm3AA23MkvoFSzdRAlv5rD2wedAQpcIWtNZ2IG5wLgPNHqWJW9wOE4oO-yie8PP65PgM_GZygk4hTFb-QW9DGDYYRRF5i_pTtH17MfWsjLQRJ6bji76vxQDfxR057nj3MsYFqKar3-NWfhn-zQyU6hbasNo_2t3S4yi2kCIdqTR5acniF4M6ifHTrs40tOqX_S0kFhxWr4UuamVaQJ-05h-aVaWrHcXrMslpV3O-Koe8ttqeg8Z9djNy_ILG4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ترامپ: دارایی های بلوکه شده ایران عملاً صرف خرید سویا، ذرت و گندم آمریکایی خواهد شد  اگر هر کدام از دارایی‌های مسدودشدهٔ ایران آزاد شود، ما روی آن حق تأیید و نظارت داریم، قطری‌ها هم حق تأیید دارند</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/17912" target="_blank">📅 18:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17911">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تهران توافق برای اجازه ورود بازرسان هسته‌ای به ایران را تکذیب کرد  خبرگزاری تسنیم ایران گزارش‌های مربوط به یک پیشرفت بزرگ را رد کرد و گفت که هرگز به بازرسان آژانس بین‌المللی انرژی اتمی اجازه ورود داده نشده است و ترجیح می‌دهد که هرگز نیز چنین اجازه‌ای داده…</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/17911" target="_blank">📅 18:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17910">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس، درباره زمان شروع بازرسی‌های هسته‌ای: احتمالاً این هفته، حتی از امروز</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/17910" target="_blank">📅 18:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17909">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">انفجار در کارخانه گاز طبیعی مایع قطر؛ ۵۴ مجروح و ۱۸ مفقود  وقوع یک انفجار داخلی در مجتمع صنعتی راس‌لفان قطر که تأمین‌کننده یک‌پنجم گاز مایع (LNG) جهان است، ۵۴ مجروح برجای گذاشت و عملیات نجات برای یافتن ۱۸ مفقود همچنان ادامه دارد.</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/17909" target="_blank">📅 18:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17908">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDEDDYGkiOOS2uBd-pl3pF9o22r8bZSe1cCUIhlFjVeyles9wEv2KuZYR5IeO4b5F6nxWlw1aYBtTcXH1tuDhsplWRCKvyOsuZmxHFwJYEwArpJb_bNvKnRELK8Zs7Dhw4R9EsrRriFSRbr5AJpju1dpYYIZKYJIR0BAnQV04OM5RCLsCBJDEWpM0yd2QRWuLtdfaFrux3vuEG3hkENDKW5B-RN_8JkJfXON1v5bZw70cqjGQe4_NR2DuBKuVK5D7468vzruRVVBn7DcOsImI-FVbMq50As9WppfVE49qU-md0WLy-bjmtY-RmZG_RqohyjsZa8_7C3F9Afd1BIVxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
یادداشت تحلیلی: آینده بازار نفت در شرایط جدید ژئوپلیتیکی
بازگشایی تنگه هرمز و توافق آمریکا و ایران می‌تواند فشار عرضه نفت را کاهش دهد، اما بازگشت تولید به سطح عادی زمان‌بر خواهد بود و رقابت تولیدکنندگان دیگر را تشدید می‌کند.
در سمت تقاضا، رشد اقتصادی جهانی در برابر ریسک‌هایی مثل دلار قوی، نرخ بهره بالا و تنش‌های ژئوپلیتیکی قرار دارد و همین باعث می‌شود بازار نفت وارد یک دوره نوسانی و چندعاملی شود.
🔗
ادامه یادداشت را از اینجا بخوانید!
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SBoxxx/17908" target="_blank">📅 16:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17907">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نخست وزیر و وزیر امور خارجه قطر در مصاحبه با الجزیره:
آنچه ایران در طول جنگ با ما و برادرانمان انجام داد، غیرقابل قبول است.
اجماع خلیج فارس برای دستیابی به دیدگاه مشترک برای گفتگو با ایران برای حل مشکلات وجود دارد.
ما می‌خواهیم شاهد همکاری ایران با کشورهای خلیج فارس در سطح بالایی از اعتماد باشیم.
مقدمات برگزاری نشست‌های خلیج فارس در دوره آینده برای بحث در مورد امنیت منطقه‌ای در حال انجام است.
موضع اصولی قطر رد هرگونه تغییر در وضع موجود تنگه هرمز نسبت به آنچه قبل از جنگ بود، است.
چشم‌انداز ما برای تنگه هرمز، باز بودن آن و آزادی عبور و مرور از آن است.</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/17907" target="_blank">📅 16:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17906">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_qUbZnui2LUwH9mHnQIunrv6V0wXA3vixu5LP4tNDA0eU3cYdJJuWuifAkAY_5xsZulCzr8DFf3mxq7bUO2wOn5Bq7ctzc-RfY2gngpWboY_tplCg57MI1bsXRPcJiN7s-Pf3QoK91TsS_gdxZODn_Q0zZ5e9zZ-HQfWckE51hjRP8iid6CbpO6JOmXeyw8uzIuCVx_RPGaBVIt-EdMkIH52y84t15ocuzPYBbN0SwqYjd6vN-OidgiJmwLdtd87y5BOvOeFHwXNJcoVf9ngDIVbOtnxnA4olCNin0EiRIrL6Z0yiuzsNEQPXLcaKzAk4VKTbLpOjWNE_OhPy9D4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش احتمال وقوع رکود اقتصادی در آمریکا به ۱۵ درصد پس از توافق با ایران طبق تحلیل موسسه گلدمن ساکس !</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/17906" target="_blank">📅 15:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17905">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">معاون ترامپ: دارایی های بلوکه شده ایران عملاً صرف خرید سویا، ذرت و گندم آمریکایی خواهد شد  اگر هر کدام از دارایی‌های مسدودشدهٔ ایران آزاد شود، ما روی آن حق تأیید و نظارت داریم، قطری‌ها هم حق تأیید دارند</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/17905" target="_blank">📅 15:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17904">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">کار خدا را ببینید که پاکت زاده های بدافزار «بله» آمدند کانال مرا بستند حالا تلگرام آزاد شده و بعید نیست خود بله و روبیگا فیلتر شوند!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/17904" target="_blank">📅 15:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17903">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">جی دی ونس:  آنچه جرد کوشنر و قطری‌ها و کل تیم انجام دادند، به نظر من، یک توافق کلاسیک ترامپی است. اگر دارایی‌های ایران آزاد شود، کشاورزان آمریکایی را ثروتمندتر می‌کند و به تغذیه مردم ایران کمک خواهد کرد.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/17903" target="_blank">📅 15:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17902">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">روزنامه وال استریت ژورنال:  آمریکا پیشنهاد داده ایران فقط برای خرید دارو، غذا و کالاهای بشردوستانه به ۶ میلیارد دلار دارایی مسدودشده‌اش در قطر دسترسی داشته باشد؛ ایران هنوز این طرح را نپذیرفته است.</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/17902" target="_blank">📅 15:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17901">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">جی‌دی ونس: ایران مذاکرات را ترک نکرد؛ ترامپ به اظهارات تهران پاسخ می‌دهد
جی‌دی ونس، معاون رئیس‌جمهور آمریکا، درباره گزارش‌های مربوط به خروج هیئت ایرانی از مذاکرات گفت:
«ایرانی‌ها تهدید کردند که مذاکرات را ترک خواهند کرد، یا دست‌کم چنین تهدیدهایی در شبکه‌های اجتماعی مطرح شد، اما آنها مذاکرات را ترک نکردند.»
او همچنین درباره واکنش‌های دونالد ترامپ به اظهارات مقام‌های ایرانی افزود:
«دیروز به ایرانی‌ها گفتیم وقتی وارد چیزی می‌شوید که نسل ما آن را "کری‌خوانی" می‌نامد، نباید انتظار داشته باشید ترامپ پاسخی ندهد.»
ونس ادامه داد:
«وقتی آنها حرف‌هایی می‌زنند که درست نیست، ترامپ هم به آن پاسخ خواهد داد.»</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/17901" target="_blank">📅 14:58 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17900">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس، درباره زمان شروع بازرسی‌های هسته‌ای: احتمالاً این هفته، حتی از امروز</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/17900" target="_blank">📅 14:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17899">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس، درباره زمان شروع بازرسی‌های هسته‌ای: احتمالاً این هفته، حتی از امروز</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/17899" target="_blank">📅 14:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17898">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس: ایرانی‌ها موافقت کرده‌اند که بازرسان آژانس بین‌المللی انرژی اتمی را بازگردانند</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/17898" target="_blank">📅 14:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17897">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس: ما پایه بسیار خوبی برای یک توافق نهایی موفق گذاشتیم</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/17897" target="_blank">📅 14:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17896">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس: ما پایه بسیار خوبی برای یک توافق نهایی موفق گذاشتیم</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/17896" target="_blank">📅 14:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17895">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پس فرق این دوره ۶۰ روزه با بعدش این است که ممکن است بعدش آمریکا عوارض عبور بگیرد!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/17895" target="_blank">📅 14:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17894">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">— یک منبع اسرائیلی به سی‌ان‌ان گفت:
«اسرائیل در حال بررسی اعلام عقب‌نشینی‌های نمادین از مناطق جنوب لبنان است.
عقب‌نشینی‌های نمادین شامل عقب‌نشینی برخی نیروها از مناطق اطراف خط زرد خواهد بود».</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17894" target="_blank">📅 14:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17893">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">استارمر نخست وزیر چپگرای انگلیس استعفای خود را اعلام کرد.
دو ضربه بزرگ به چپ جهانی در کلمبیا و بریتانیا در یک روز!</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/17893" target="_blank">📅 12:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17892">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">انفجار در کارخانه گاز طبیعی مایع قطر؛ ۵۴ مجروح و ۱۸ مفقود  وقوع یک انفجار داخلی در مجتمع صنعتی راس‌لفان قطر که تأمین‌کننده یک‌پنجم گاز مایع (LNG) جهان است، ۵۴ مجروح برجای گذاشت و عملیات نجات برای یافتن ۱۸ مفقود همچنان ادامه دارد.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17892" target="_blank">📅 08:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17891">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انفجار قطر بحدی شدید بوده که در بحرین دیده و شنیده شده</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/17891" target="_blank">📅 08:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17890">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بیانیه قطر و پاکستان در مورد آتش‌بس در لبنان چه می‌گوید؟
طرفین (ایران و ایالات متحده) توافق کردند که یک «واحد کنترل درگیری» را بین خود و جمهوری لبنان با میانجی‌گری تسهیل‌گران تأسیس کنند تا از پایبندی به توقف عملیات نظامی در لبنان طبق مفاد تفاهم‌نامه اطمینان حاصل شود.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/17890" target="_blank">📅 07:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17889">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
بیانیه مشترک قطر و پاکستان در مورد پایان اجلاس بورگن اشتوک
بیانیه مشترک قطر و پاکستان:
🔹
اولین جلسه مذاکرات سطح بالا تحت چارچوب تفاهم‌نامه اسلام آباد در بورگن اشتوک سوئیس با حضور نمایندگانی از جمهوری اسلامی ایران، ایالات متحده آمریکا و دو طرف میانجی، دولت قطر و جمهوری اسلامی پاکستان، به پایان رسید.
🔹
اجلاس دریاچه لوسرن در فضایی مثبت و سازنده برگزار شد. پیشرفت‌های دلگرم‌کننده‌ای از جمله ایجاد سازوکاری برای مذاکرات فنی بیشتر حاصل شده است.
🔹
بر اساس این تفاهم‌نامه، طرفین با ایجاد یک کمیته عالی رتبه موافقت کرده‌اند که نظارت سیاسی بر میانجیگری را بر عهده خواهد داشت.
🔹
مذاکره‌کنندگان ارشد به طور منظم به کمیته عالی رتبه گزارش می‌دهند و گروه‌های کاری متمرکز بر هسته‌ای، تحریم‌ها و یک گروه نظارت و حل اختلاف را برای اطمینان از اجرای مؤثر تفاهم‌نامه و سایر موارد رهبری می‌کنند.
🔹
کمیته عالی رتبه بر سر نقشه راهی برای دستیابی به توافق نهایی ظرف ۶۰ روز توافق کرده است که زمینه را برای آغاز فوری مذاکرات فنی بیشتر فراهم می‌کند.
🔹
علاوه بر این، یک خط ارتباطی بین طرفین برای مدت ذکر شده در بند ۵ تفاهم‌نامه ایجاد شده است تا از حوادث و سوءتفاهم‌ها با هدف عبور ایمن کشتی‌های تجاری از تنگه هرمز جلوگیری شود.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/17889" target="_blank">📅 06:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17888">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
عراقچی
:
🔸
میانجی‌گری خستگی‌ناپذیر پاکستان و قطر باعث پیشرفت‌های بزرگی برای پایان دادن به جنگ در لبنان شد.
🔸
همچنین تحریم صادرات نفت و پتروشیمی تعلیق شد، محاصره دریایی برداشته شد، برخی از دارایی‌های مسدودشده آزاد شدند و طرح بزرگ بازسازی و توسعه اقتصادی ایران اجرایی شد.
🔸
اولین آزمون واقعی: واحد رفع درگیری‌ها در لبنان</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17888" target="_blank">📅 06:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17887">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گوستاوو پترو، رئیس‌جمهور کلمبیا، نتایج انتخابات این کشور را به رسمیت نمی‌شناسد و اسرائیل را به دستکاری در نرم‌افزار انتخاباتی کلمبیا متهم کرد</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17887" target="_blank">📅 04:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17886">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">رییس جمهور چپگرا و معتاد کلمبیا امشب شکست خورد و جایش را به یک راست گرا داد.  قاره آمریکا در حال یک دست شدن است.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17886" target="_blank">📅 04:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17885">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دونالد ترامپ، پس از ونزوئلا، اکنون کلمبیا را تهدید می‌کند و گوستاوو پترو، رئیس‌جمهور کلمبیا، را «قاچاقچی غیرقانونی مواد مخدر» خواند.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/17885" target="_blank">📅 02:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17884">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromورزش سه</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6be0b658c6.mp4?token=Glccikc2MDwf8MiiwPH8fJdIhVTmqJB3NH9vy5QWvmoLY22LHejui0dtehoLtemM8GrFOuETwCPszLNV2exFKWHHrXczXpqZygvBPJ2PjOCJuVwpuBYrTQu_reuHYceuknhaTKKWqo3hvvby6C5TaME_NKs7RAni73E-kDBkdJAJUUe7wu7idqDOxthYRCVNLsIQZePz5gk4qytbIHUrlZdUlj5O-EGT1iWQknP-XFJJkhhzQeRx4uWYRrYhfKV3IQfoBatw2mVggO-YHTxRYi12sPpIuQjco-sFiIaKrsd1h-15bMxZOiSGP7Ks-b_MUGj87vGCBWLTsgjAgBdGBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6be0b658c6.mp4?token=Glccikc2MDwf8MiiwPH8fJdIhVTmqJB3NH9vy5QWvmoLY22LHejui0dtehoLtemM8GrFOuETwCPszLNV2exFKWHHrXczXpqZygvBPJ2PjOCJuVwpuBYrTQu_reuHYceuknhaTKKWqo3hvvby6C5TaME_NKs7RAni73E-kDBkdJAJUUe7wu7idqDOxthYRCVNLsIQZePz5gk4qytbIHUrlZdUlj5O-EGT1iWQknP-XFJJkhhzQeRx4uWYRrYhfKV3IQfoBatw2mVggO-YHTxRYi12sPpIuQjco-sFiIaKrsd1h-15bMxZOiSGP7Ks-b_MUGj87vGCBWLTsgjAgBdGBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سهراب سپهری به جای طارمی؛
😂
راه حل خیابانی برای گل مردود ایران به بلژیک
🏆
در قسمت دوازدهم برجام رونمایی شد
🆔
@varzesh3</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17884" target="_blank">📅 02:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17883">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">به نظرم تنگه هرمز را بدهیم بیرو ببندد و خودمان برویم تنگه مالاکا را ببندیم!  آبش را هم بدهیم آقای میثاقی بخورد!</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/17883" target="_blank">📅 00:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17882">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خارجی ها مخ شان سوت کشیده و فکر می‌کنند بیرانوند راننده یک تراکتور است!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/17882" target="_blank">📅 00:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17881">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_FHmry6FzMv8fIDth35nm2FQHOeAfHoC-fFlMaNRsHvsQhbIyZjGc8yehkrRQAJvQ1KlRafkXVD6f_h_UTmeeK_BSwRXTxDnfKj1LTHQzouVm9NfZ64_lxRYtrlQu-n-BKSBki2bRLamh0h1AyfDx-2Y2QfbzGzdZ6o3AJt-MGCvHKuUarONo8Iw4dm8e29111-nO2T7prXSdp694THKrcryHEmAA94jemaOLlfi8-u8U1FPVd8Z87RwEccZlE1ssxDitjxJdFSZqDbIo4CYisqhv-fc417j_-wR6j5iZvmJqfZ5PNNRHBsjyAb4ciO6h2918czmWhLPfqrsHTDGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب تاکتیک های ناشناخته ای رو کردیم که سبحان الله!  انصافا بیرو عالی بود و ثابت کرد یک گلر خوب می‌تواند یک تیم نابود را نجات بدهد!</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/17881" target="_blank">📅 00:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17880">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOzYfSW_pX4GojD8YOkP8hwi3JJYXsYOY4foCbYGGD6GMq6t3j7PJP0QGyMN5bD2U1uyIH8-iswSv75d-l3Snp-UqpwsnfCEiluYWilb_CqRu33ebEQHRLDC8dqScDcfulNXUCsQ4ds1p2vp2ezbXu_OS1N1SHuD-D0YB5KbNT6sUhxs8ftnLnA_9SykDAUvJwwfM4GlKATWaHB8qp66LMAXKowV1dwNVn0LWlIMRbQaO2R4CyLyR3ITW5Wz5V6h0TTKWjJRpH4rMHu6Z4Ca4ywe73LT_V8KaYry4FMYzmICSd78-2IPwL0AcIDoG448JuiEGCmJ5vKJArgVBYBg6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب تاکتیک های ناشناخته ای رو کردیم که سبحان الله!
انصافا بیرو عالی بود و ثابت کرد یک گلر خوب می‌تواند یک تیم نابود را نجات بدهد!</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/17880" target="_blank">📅 00:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17879">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9e2be94a.mp4?token=saELqz4I_ANxvwgXYaRZqP65TK6CoLXTYdpN0oh-WJTrwF88HMyBAD_5whYQUWw-wjXBxzlXOMEtzLBDOEXEAmxL97TxaNrZvpkwXHi-X45YzYG8aDp9860SKcdLSlMR-1p7-NgNaq_ALJcp8K6JybAFEC9xJSzbUPwLs38jfeymMwzQN0b7HpHNI-5cT9gcUTjtbx_i7nq7kd-r7wZ0F7GaFC0RSUxHKQI980UavQ_2ODxH2bHw6uZIm-IM7_T60_K48zUyueDU-NI6HukzZdmfwRM2lOGpWgnNxJg8w8bdQGGQr5YPZf0Ci-VbiaMKe6Gm-1DQk54ckjc70AWS6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9e2be94a.mp4?token=saELqz4I_ANxvwgXYaRZqP65TK6CoLXTYdpN0oh-WJTrwF88HMyBAD_5whYQUWw-wjXBxzlXOMEtzLBDOEXEAmxL97TxaNrZvpkwXHi-X45YzYG8aDp9860SKcdLSlMR-1p7-NgNaq_ALJcp8K6JybAFEC9xJSzbUPwLs38jfeymMwzQN0b7HpHNI-5cT9gcUTjtbx_i7nq7kd-r7wZ0F7GaFC0RSUxHKQI980UavQ_2ODxH2bHw6uZIm-IM7_T60_K48zUyueDU-NI6HukzZdmfwRM2lOGpWgnNxJg8w8bdQGGQr5YPZf0Ci-VbiaMKe6Gm-1DQk54ckjc70AWS6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دلال های محبت فاکستانی را ببینید!
شهباز شریف از عراقچی التماس می‌کند تا با ونس ترنس دست بدهد اما عراقچی پشت کرده و می‌رود و بعد شهباز شریف و عاصم منیر شروع به ماله کشی برای آمریکایی‌ها می‌کنند!</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/17879" target="_blank">📅 00:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17878">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">راس الفان همان منطقه ای است که ایران تاسیسات گازی قطری ها را در مارس به آتش کشیده بود</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/17878" target="_blank">📅 23:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17877">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خبرنگار صداوسیما:
هنوز نمی‌توان گفت که مذاکرات به پایان رسیده است یا خیر اما از شواهد به نظر می‌رسد هیئت ایرانی در آستانه بازگشت به کشور است</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/17877" target="_blank">📅 23:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17876">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وزارت کشور قطر:   انفجار داخلی در یکی از کارخانه‌ های منطقه صنعتی راس لفان رخ داد و تیم‌های دفاع مدنی به محل حادثه اعزام شدند و هیچ گونه آسیب جانی یا نشتی ثبت نشده است.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/17876" target="_blank">📅 23:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17875">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇶🇦
🇧🇭
— گزارش‌هایی از انفجار در قطر و بحرین.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/17875" target="_blank">📅 23:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17874">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇶🇦
🇧🇭
— گزارش‌هایی از انفجار در قطر و بحرین.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17874" target="_blank">📅 23:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17873">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyiXLdoqD5C0Dy__o86Vk32BQL5I6wGzHfe5i3kl4CWNR2JqexuSG85IWsEk9HqCQLKiKYdaODRIuWEnSd43dEZgPO9REwwg-1ENCkikGc0_ZrHRgy67W08_rLcnbNb7GI3ncRjFRoOqlSrExUgH0BK-M1D8lNuy6SmIJO78eO3eOYT02v-ZjmnVKpGdszywJXVy8HGwMxtGTpITaj1BkuHpnsCT8SL-jiiph19kXHwpTXapLa30xz1sfkXhcv68Bxljxyrax7UZ3V7-Aams4cnawGuseuQgQ7voiQX6Cxgvw-5jX7wvO0JLjwumbBIp39K_7caVI_DxMOGE0ltXag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه به جای طارمی، سهراب سپهری رو میذاشتن نوک خط حمله ایران، الان ۱-۰ از بلژیک جلو بودیم  》Keyvan《  @OfficialPersiaTwiter</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/17873" target="_blank">📅 23:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17872">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتوییتر فارسی</strong></div>
<div class="tg-text">اگه به جای طارمی،
سهراب سپهری
رو میذاشتن نوک خط حمله ایران، الان ۱-۰ از بلژیک جلو بودیم
》Keyvan《
@OfficialPersiaTwiter</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17872" target="_blank">📅 23:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17871">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">به اندازه قهرمانی پرسپولیس در آسیا از بلژیک جلو بودیم…
لعنت بر پرچم کمک داور !</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/17871" target="_blank">📅 23:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17870">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تیکی تاکای عالی از بچه ها !
منتهی در محوطه جریمه خودمان</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17870" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17869">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتوییتر فارسی</strong></div>
<div class="tg-text">از نادر محمدخانی به اینور هر چی مدافع تیم ملی داشته امشب فیکسه.
》Footfun《
@OfficialPersiaTwiter</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17869" target="_blank">📅 22:24 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/FJrvpWPIZfyRb1Tjfumk2UA7qKznMrc8RPcdeb_QiaruklC7tacA1YT7XxELDrjYu1d2dW77P33Si-_-hkGDZtkf-2iYsFnbvdc2ypAjAPTaSPkn1CuENGU2iV56-i3InAlchjY9P7ARAXaxhfd_79QmO_coqG29B54aOOQF98B7gXfnqfcZANLPPZSAXbUSkBQ-HbTKWsB5Hv0iNUTW3hug9jOjvgUHL2Rf2kBOef6qLszkpcxlWQTxnWLt75jSnJRtH3SAl-h6ZNLzHFrA6y4DP_iSXeN1S75LhzW0gX1XN8ZVnFZlG0kEoiWhRLrP8V8BknfzUKFa1bfl1J0xSw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 10:42:50</div>
<hr>

<div class="tg-post" id="msg-134079">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cfc110b2c.mp4?token=W-Dc1GdmyThV99MGeWkkx3OEg1Vnue7VbVn8cdGM8RTHZkv7xLCvX7v3rwSaBk_pJ2Gcy0XiHxQ0h8HOW4-vjoPPc3ftp59eDr13sRWHtXRwEH_e5x5oHaZthOCIVElxHsg68VvicOE3VlAxxy8v-TLQVwXnSkZ65YYAHoobV57HpjSL1-2nDvMrejso64sQly40m0ER-sefBKyiuB336zFdUAQt4rdunj5t2jfA8fNEXgxmFMBmCBapYikLtIuQ_3eHdg3uLQ1wwROQl1mBAT8kYrX3JWLfYcRpCw9YY7SkP8U_v0n2TX7xYG_YO3zEau55xi1-09nQcVJBTVybm5Z83bgAmdXqoFUvKTKznVpUOuWkEfQJJEoQ1IdAiKCo4Wf_icN7feMNy98dOiUBJTKXb_ZqTId33yDguCOcBhYvCH1gwFdDruTv0G26FAQg_67xEAPqgIquQ3IRIpHT1KVK7CNLJatUcwGwwt2aMbteLA1olKLeczhQ_edov3qM62WGRwnGmMNsh-Y6noASpqkcgLDVL_1j45bjycIc6irz4pUyRKoq1kp481rRqAwHd18sWelrAEd25V_x6Pp0VMz_aVcOGjwswI5uGUEV8qIew5eYLnDjlaLEHsWB1789Dcj2qDqbU1rOSSeh2jHZR6yZkg0PZwbgwhJGeJ04Spg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cfc110b2c.mp4?token=W-Dc1GdmyThV99MGeWkkx3OEg1Vnue7VbVn8cdGM8RTHZkv7xLCvX7v3rwSaBk_pJ2Gcy0XiHxQ0h8HOW4-vjoPPc3ftp59eDr13sRWHtXRwEH_e5x5oHaZthOCIVElxHsg68VvicOE3VlAxxy8v-TLQVwXnSkZ65YYAHoobV57HpjSL1-2nDvMrejso64sQly40m0ER-sefBKyiuB336zFdUAQt4rdunj5t2jfA8fNEXgxmFMBmCBapYikLtIuQ_3eHdg3uLQ1wwROQl1mBAT8kYrX3JWLfYcRpCw9YY7SkP8U_v0n2TX7xYG_YO3zEau55xi1-09nQcVJBTVybm5Z83bgAmdXqoFUvKTKznVpUOuWkEfQJJEoQ1IdAiKCo4Wf_icN7feMNy98dOiUBJTKXb_ZqTId33yDguCOcBhYvCH1gwFdDruTv0G26FAQg_67xEAPqgIquQ3IRIpHT1KVK7CNLJatUcwGwwt2aMbteLA1olKLeczhQ_edov3qM62WGRwnGmMNsh-Y6noASpqkcgLDVL_1j45bjycIc6irz4pUyRKoq1kp481rRqAwHd18sWelrAEd25V_x6Pp0VMz_aVcOGjwswI5uGUEV8qIew5eYLnDjlaLEHsWB1789Dcj2qDqbU1rOSSeh2jHZR6yZkg0PZwbgwhJGeJ04Spg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ثابت‌قدم، مدیرعامل شرکت توسعه: تا هفته آینده نصب صندلی‌های استادیوم آزادی به پایان می‌رسد/ عملیات چمن هیبریدی هم آغاز شده و تلاش می‌کنیم به اوایل
لیگ برسد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/134079" target="_blank">📅 09:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134078">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5172bbee52.mp4?token=HKCiiLPHHC2d68KQ8_-koI0j4Xjv9Ihq0sKcTQVNuF-jTMFdTTEqOyA5v78FRPBgVgP4VHgH5SQn2BuM3zyvHP8e6wcQn11uQUeAp9-kcq8u0K4IC1zPjqOwjowwUza43akFEQRfp8vZnkmzC4PBkIbr_ZKpPGK7ZvYVuctfbpKP_QJeZAVTGU7c3gGFDhEJr3hwcuz9OmqzRPQJpNdI718esgbZ4lkjO6rcNek7JSTxIEhM5cmC4y0esn3rPhhTfASMldWjJEOndzOBywPv5nSvwemLhvkDRhkbE1dV4HhobRz231ew5xkalu0V5EQGznqSsQPtbms9rQ62aoOIiX3Sw4pFWfF_eyP37Zopy_rmj_o_v4YIRPsCgtp29_kVvVzcn5iDsDThwwEby7O99C8OZ47HGuct0aMsxJtSDb3NRUJsGrmAmViCXLE-0Lz5f6951W_2ngsD8Qdw4GCAOxN3su7jAj8GrM5glbar7TgpczPW5VqaHD6rlpyTImf6LapyYYWPSC0lhGMvtBhCP6bkA8o9i1U8K-pXv4aebWCt60Fd1gLlHuHSJ7h2IwLRBkIDw9rdMr02HhBg7AWm9wGO_G4utqE5mswhXUv0sp8j34LA9OFWVpYKb8K7F1UCXepJ50yM5-DjD-OxPzxHR9hChscAlaX9cv_VV47GSPo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5172bbee52.mp4?token=HKCiiLPHHC2d68KQ8_-koI0j4Xjv9Ihq0sKcTQVNuF-jTMFdTTEqOyA5v78FRPBgVgP4VHgH5SQn2BuM3zyvHP8e6wcQn11uQUeAp9-kcq8u0K4IC1zPjqOwjowwUza43akFEQRfp8vZnkmzC4PBkIbr_ZKpPGK7ZvYVuctfbpKP_QJeZAVTGU7c3gGFDhEJr3hwcuz9OmqzRPQJpNdI718esgbZ4lkjO6rcNek7JSTxIEhM5cmC4y0esn3rPhhTfASMldWjJEOndzOBywPv5nSvwemLhvkDRhkbE1dV4HhobRz231ew5xkalu0V5EQGznqSsQPtbms9rQ62aoOIiX3Sw4pFWfF_eyP37Zopy_rmj_o_v4YIRPsCgtp29_kVvVzcn5iDsDThwwEby7O99C8OZ47HGuct0aMsxJtSDb3NRUJsGrmAmViCXLE-0Lz5f6951W_2ngsD8Qdw4GCAOxN3su7jAj8GrM5glbar7TgpczPW5VqaHD6rlpyTImf6LapyYYWPSC0lhGMvtBhCP6bkA8o9i1U8K-pXv4aebWCt60Fd1gLlHuHSJ7h2IwLRBkIDw9rdMr02HhBg7AWm9wGO_G4utqE5mswhXUv0sp8j34LA9OFWVpYKb8K7F1UCXepJ50yM5-DjD-OxPzxHR9hChscAlaX9cv_VV47GSPo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
فیلم خلاصه بازی نیوزیلند 1 _ 3 مصر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/SorkhTimes/134078" target="_blank">📅 09:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134077">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
جدول گروه G جام جهانی در پایان هفته دوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/SorkhTimes/134077" target="_blank">📅 09:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134076">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❗️
قلعه‌نویی: معادلات گروه را بهم زده ایم و به دنبال صعود به عنوان صدرنشین هستیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/SorkhTimes/134076" target="_blank">📅 09:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134075">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
جدول گروه G جام جهانی در پایان هفته دوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/SorkhTimes/134075" target="_blank">📅 08:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134074">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
جدول گروه G جام جهانی در پایان هفته دوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/SorkhTimes/134074" target="_blank">📅 08:58 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134073">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUgzWTSDN56Mv3LBdfNGv8GYJKLbVTmiJundFwoBnAByFBkgSdQc6suqV1mQXbZZQkLDNTxZtO0iqBDkzKvhUWXAMUb8byzPVFpPuVgLqdEdJsDTrZaOUVI4H-SJ1Kqq81EuA2vaxiZtxZbaQZgdJLTScseTp3wk0snaGXJWb4ubX7D24L2w-15BsPbisiZoWWmn66GENQDo_GPyNsSfEIRIXszLV_0kHgMQNSYS7-1aVg34bCFtH0e4XVrhOG_QhoWiN8GA4jxVk2FtilCUuoDwDL5u8Nw53Ci1ytLYEHQO5d4772D15S2CqIdPgT5zS9Ci7BxU37VxPN7WdwSVYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جدول گروه G جام جهانی در پایان هفته دوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/SorkhTimes/134073" target="_blank">📅 08:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134072">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/if8H3oQ_V_mttY3yoI3KXRYhBYsWKrQ-84M4bt-Uh3d6YiuIlaBtH3Sjx7EC9t1-QO6wguMKOnE3bgBVOk17-xgkC3JCi3Y5Arsg9FtlGRzkTb0AJUiO0oybtTT8OfTsVonkSJan67pNPnGsU1MTrgZ9wzWiQDVX7qT_IevQX_b3T0e5RdGO2sXIkW4NDglo-kEHhjUM892j9eKN9RbJbLVhEhizk7DP3mfOpYQVC0s2l7FI47npe5Sj2mcoMIouUSI-g_ELCK8-xt7782mfOvt-5RUzpqZtZm_z4jxtRDdnhx2Zo_5yeJjgOeyym-DRzk5cD0XbwY_QznwugWHdpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
نتیجه بازی های دیروز جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/SorkhTimes/134072" target="_blank">📅 08:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134071">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reoKrnHZ2DmTjBFFqF2GpFJ_EAV5sY0j5QFS-HCz7Lee_CR85ixY4slOABPrVCLKJqS1cb2YmwMRWdQciHlhmEisg6QbUaZBvmz3gOGKph1r11yVOTv0amB5ElZ62slNXH2wDR2eJqaF2-Y9VT0DtsdTvb_ZkcpacDo9lEXCHWT750mxRGSbpFiyPZyHb71zeaAWKf6kMHqlmvc_pd1iaEOb9imG7urrF668h5mvgnrlOGidV_yY_EDv9YNJwHKR4VTIkZFVbKxICmD5KZ-HYCHOfR1Sw_tS35mxTjLdvm0pgB0T5j10yxx_ziSa2_KUnxowE7ZtdIqDW8u-f7Wqrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
ژوزه مورینیو:
بیرانوند هر توپی میومد سمتش رو می‌گرفت، بعد از همراهانم پرسیدم این پسر کدوم تیم بازی می‌کنه؟ و گفتن تیم ایرانی انتظار داشتم بگن یک تیم بزرگ اروپا و فقط محکم زدم تو سر خودم چون حق بیرانوند این نیست
❌
اگر یک دروازه‌بان بتواند آن واکنش و مهار توپ‌ها را مقابل بلژیک انجام دهد، یا باید برای یکی از بزرگترین باشگاه‌های اروپایی بازی کند یا اینکه استعدادیاب‌های فوتبال آدرس او را فراموش کرده‌اند. بعد از بازی امشب اما فکر نمی‌کنم آنها دیگر آن را فراموش کنند و به سراغ او خواهند رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SorkhTimes/134071" target="_blank">📅 08:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134070">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mp_x8XYAm1gL9zg8dwCmmgKKJ9sHt2x0irsj6DXb5LD-gbh6IRONvzzSrBbeMgYnZpIQ6P3r5rF0JVQxUlpNo5a0FI4Jz-50PNjfD6oJxs8HlTrP8c75OBXulSl-tIyIhnW2Vc6-65nQlDqsj-2tyizICtUvjnBnxA9F0dCbZes-BdeyDs1gOI_ztkKcFW1uIC8Ac216XGAJPJ2AccKQC_hDDXnPwwrb8ZFPY_amm7fyQVZc3HcKJUOs4vEhdidLZoRE3Wu57cr2wZTlPVa3YMr1rQILGIli0DEm2afJ3TZUnBW6Z_pexqS7VzBzk6WVjwFS4ovfWHjoyDX_TaWgcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه G جام‌جهانی ۲۰۲۶
[
مصر
🇪🇬
🆚
🇳🇿
نیوزیلند
]
⏰
بامداد دوشنبه ساعت ۰۴:۳۰
🏟
استادیوم
بی‌سی پلیس
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SorkhTimes/134070" target="_blank">📅 01:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134069">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✅
جدول گروه در پایان بازی ایران و بلژیک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/134069" target="_blank">📅 01:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134068">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpa8YtdO4_XJdINT9-IhcVsWaT7fSindVTaiTPLIx0DDP1xtGuielGAqzTZljewy4k7Qx816avO_zXfvSqHAuhZqjHXN3_WH_-wd3Dt0QenKag792p9KrrvVSuivYFAHFiRRB0bRfuDNaq3NO66XFLq4cmud1xpppxwAmVY5lmsqvNRjx4PREadibk_Nkz8n1SRmZT3zvyrjqqbhEhLMkP1D6mp1DEqi1VVtRKIUkloWOLZDO0TieMhtZOBDflbTouMPlP_3msaU1G6H-kse7xgyN0S2UOMaSPmiic-4ghzB0Hqb6a4s6eSjlijwc8uG6Kka71xd9oxNzTbFG8YA0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جدول گروه در پایان بازی ایران و بلژیک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/134068" target="_blank">📅 01:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134067">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PycMVdEa8iTqm7gnp3cM3wp4d9ntn5Ge-4VBuiLQS4tuioy6QKoTS6fc9yzuVufHhFtpJulOliauYOIPMd8rT6kHMxDRaCa7-zP07XqCRFWBaN6qW4GXd6Bd1ep5rDl1fDIVWJinURIg2ogaFraSKCW65q8LeAhlwBIEwUmv-qYCuinK_NBF_VAnlIYvshoNn7ZPezz65LVXkZKoOCDQRL5-f8wkznzjEHFbuCnXnSdW2cCJpiEBPk24eIJqnBYxSAOgVMcR2Mlu6lvgpT6EVr8_Wdwz3UVt635Bsi6omzNQIplIh5xn0kE6Gw3zSRIRXHySoEOzJhXGjET_6fROeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نظرت در مورد بازی ایران و بلژیک ؟
🔴
ابراهیموویچ : نزدیک بود نیمه اول خوابم ببره و نیمه دوم واقعاً خوابم برد
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/134067" target="_blank">📅 01:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134066">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmkEbROXPt6wSXikO1DWfJZ9V_PmkFYpiozMiZ4f2Wm1HKstb_-eW0iJSpxSzCTz4-DcyDfQPlcOe5a7ozinaI-YMIHn6eCYtTmmR8dCole6orwbdv-rAHyANNPCxb8o6hVQiV5oEXsvVS4jMtOWK1Rx1jS5iogPjCyoAW__KDbSvrZAx6ISgxK5Np4gvzjvrGmZVUve2Flh94GiuiTJEJ-dHSRyUVyt8kpWIEQ1Lvpk9egjeMJLvfPAtfUU1yaGedxArESRgPP8oqmQ8oW3eZTUJu54_lQo4I5lovj7fIuLXYV3_cmvLUFj9W__0B1yrVWtfvFFU1AATW_kUE2W-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
بیرانوند و جایزه بهترین بازیکن زمین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/134066" target="_blank">📅 00:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134065">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nddIX0Nv8FH_IVl40j44J9cIkf3iZzzgxfWiqE1IlX4hfmBIlMUZ9peVbomH5GGWxsO4V5bCfRpT0i-OsMg6YSXiuAWXfldR_PgIzfAFMFit5maWhvssB86R1Q2Aat2NKjvBFYhKLpyY10z9k3dVQ_uw5R8_L3A1lvfSAxps3grReGG6qmnOt5O2xrhsHokxCdlbXV260z1cy561RVXeMv2WG3yWqjY-WczFOczGmJ5zqo_o_nWnP3K6sPcPu7tyw2kLuPZTnLISSJsr2l4Tbkohw_O3K5cTEczEWT1QsRS-yu91mJN8Oy9kD2BuuLy7-IZBSWfSLVIL1cJUw4VOjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سرطان اخرشب بیرانوند در کنار مسی، تونسته نمره 10 بگیره(:
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/134065" target="_blank">📅 00:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134064">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135ac7b305.mp4?token=aFrwW1dIUKoyZGU3Nrb6VZc4pNzuFxnen_kRUOqA3HrWLxkgyPdoZRfoo43Vb1zuLPLJogIiVkvgHNEzpW20QhY-Y-f_rEKkKhMmtil9xpW58xEVtRlBnbRJamAqd2MocBFF8eTpJqJRguw4dPFa4fI9n27bvQemh9aLmGWHx9Ib_iSNCnP31FmDNKL5xzmRucesiMCb_YygJ_5JwUYJMvuiTd2DEPDKhAQghTmmYhiwKpJchYcKDqXdPNB5V1voG2eD4AjRQxyudLsqwniKEs_eiH_8qt24VzInOzFaVTv6_h24Ki7xjVUVZOFQb8JO88GcDfAj5AP2XcKu3RDDF4mQOwakG1x1-D3ZZA9Y41Q08FFrwZ3e6OHvCJ4nVoTmMlf8IfRoerSo3_V-wQRYR6IGQw-ZwvrXODjEGyAQj-3wB03sIMNLbb03mLRURAIyGXMJ6aKnerwxNFaEBb94fn3ljuOZy1sdTKWLLQzLb19FTCLOKgM7BhOiA93KvtjmGLYrMeqyuJ2gmOONT8_3gUiotsBl37L4SBKwkPZJh0B9uh3FRKKcKHWh1b8dfAdik19Xckncd20HwwoWPgY6iTs0iAfrp9J9wEmDy6H8Z5bRP-amQwZc4Am-BVel2rdfVaSJtYwXWe4UpXJZL0EoB6Vw-yQW4ISZPT0fKUwY5Ik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135ac7b305.mp4?token=aFrwW1dIUKoyZGU3Nrb6VZc4pNzuFxnen_kRUOqA3HrWLxkgyPdoZRfoo43Vb1zuLPLJogIiVkvgHNEzpW20QhY-Y-f_rEKkKhMmtil9xpW58xEVtRlBnbRJamAqd2MocBFF8eTpJqJRguw4dPFa4fI9n27bvQemh9aLmGWHx9Ib_iSNCnP31FmDNKL5xzmRucesiMCb_YygJ_5JwUYJMvuiTd2DEPDKhAQghTmmYhiwKpJchYcKDqXdPNB5V1voG2eD4AjRQxyudLsqwniKEs_eiH_8qt24VzInOzFaVTv6_h24Ki7xjVUVZOFQb8JO88GcDfAj5AP2XcKu3RDDF4mQOwakG1x1-D3ZZA9Y41Q08FFrwZ3e6OHvCJ4nVoTmMlf8IfRoerSo3_V-wQRYR6IGQw-ZwvrXODjEGyAQj-3wB03sIMNLbb03mLRURAIyGXMJ6aKnerwxNFaEBb94fn3ljuOZy1sdTKWLLQzLb19FTCLOKgM7BhOiA93KvtjmGLYrMeqyuJ2gmOONT8_3gUiotsBl37L4SBKwkPZJh0B9uh3FRKKcKHWh1b8dfAdik19Xckncd20HwwoWPgY6iTs0iAfrp9J9wEmDy6H8Z5bRP-amQwZc4Am-BVel2rdfVaSJtYwXWe4UpXJZL0EoB6Vw-yQW4ISZPT0fKUwY5Ik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
❤️
علیرضا بیرانوند: هنوز هیچ چیزی تمام نشده است؛ از همه مردم تشکر می کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/134064" target="_blank">📅 00:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134063">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❗️
بلژیک رو هم الکی گنده کرده بودن چون واقعا تیمی نبود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/134063" target="_blank">📅 00:36 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134062">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
ایران با ی بازی سرد و بی روح و دفاعی و بکش زیرش  ...بازی و صفر صفر تمام کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/134062" target="_blank">📅 00:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134061">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
بریم برای نیمه دوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/134061" target="_blank">📅 00:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134060">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🔴
پیمان حدادی: تا پس‌فردا بین اوسمار ویرا و دراگان اسکوچیچ یکی رو بعنوان سرمربی فصل جدید انتخاب خواهیم کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/134060" target="_blank">📅 00:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134059">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❗️
ایران با هشت دفاع و بکش زیرش و خوابیدن روی زمین .تونست نیمه اول و صفر صفر تمام کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/134059" target="_blank">📅 23:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134058">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
بله آفساید اعلام شد ولی گل قشنگی بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/134058" target="_blank">📅 23:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134057">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✅
بله آفساید اعلام شد ولی گل قشنگی بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/134057" target="_blank">📅 23:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134056">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❗️
❗️
جونم ایران ‌‌..گل اول و زدیم ولی فکر کنم آفساید باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/134056" target="_blank">📅 22:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134055">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇷
🇮🇷
کم کم برای دیدن بازی ایران و بلژیک .امیدوارم خوب بازی کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/134055" target="_blank">📅 22:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134054">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇷
🏟️
🇧🇪
ورزشگاه سوفای لس آنجلس دقایقی پیش از آغاز دیدار ایران برابر بلژیک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/134054" target="_blank">📅 22:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134053">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇷
🏟️
🇧🇪
ورزشگاه سوفای لس آنجلس دقایقی پیش از آغاز دیدار ایران برابر بلژیک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/134053" target="_blank">📅 22:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134052">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FRXZR8vJxSbeVKwASte3DCByYXFNveNV3fh-G2kdReccEk1TTwgbeBTEKtEBm2xihxic62U9afQ1tBS95NbeWFNwqL9XxBy4RWqWFlosxt5UY1iWjmGgB3Q3mVK3XaO0m-ou5MNggoH6Nq_4YMgAtcXzXhcPt_pffbprYMo7_X0kxHfXsJGuOqbexk6kbJWSpeYIoGYsh_uv6XTKMBR11Hp1gLvvjyYDa0ubfll5Bcvhjvv2C5HlFeR2fANfRaZepBmUrd04ldmtzHaaTmIfBRCJQMtYehF-DeNK2-VLhCRThFvF5RfFTSUTfvvGhkfJctp7R3rag4J-HfLmfrdBKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
رودی گارسیا سرمربی تیم ملی بلژیک: برنامه ویژه ای برای مهار رامین رضاییان داریم!
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/134052" target="_blank">📅 22:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134051">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRYhZDaS5KRXzVwL1sV6ZBNhETVtbjSLqBTRBpz50AW5650OnUS5rMW3yrr_4fGEgh6Mt4fwapWKNKuwHo1y3VVvmat3GyGvA-Va78pHLJLHrH2Ni-pBwrqkU3qbCOB8SmcAnCNbn1ar18jrEL7emhNo1u0O6hq0Ooz_kxmHPSiadRlwoASDZfk-8XmiVeQ1PtZ7sB04QAogXaXesMktJuoc7GYt5gNi6clqriBoVPwTFB0Xm5PEJU30GodEJjKLDv-Qp5jdfhsYpBjlBpXO2nyv1fHNFEzZDZF8Rrkkq9hEqadmKjTP2wYbE36pwwYkzrvZ00nVOk7mcu3s33gOoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
به نظر میاد ترکیب 5 4 1 هست و با پنج دفاع بازی می‌کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/134051" target="_blank">📅 22:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134050">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
با توجه به قانون جدید که فقط هر تیمی میتونه 4 بازیکن خارجی داشته باشه، اسکوچیچ از پرسپولیس دورتر شده چون باشگاه بهش گفته بازیکن خارجی نمیتونی بیاری/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SorkhTimes/134050" target="_blank">📅 22:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134049">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff62ed07ca.mp4?token=JxJqJyxTBN5n70yDdPtkLhxfqLsyUtaK367W9aNw7yt351REJbrmnhQ22jA0-S3Fj6ofU7jPwmopt3BaaSI8shyxMn_cDwcQW5kUJvwV_kGJBRj6ewWSr71unTAn7pXUbSD_tgRjEGMOU3ZS6vYhVVX_FtdRNssHfh9BwriyuC0cNEh5-LHbcgdu79b4XKDMg3sK4aPQS2KZlUsgnYHJLgIElpYcUu1RhZ4Fkmzk-SsY4omkqRLM5y4G2c35Cw0FHF2oV5a-WfQHciePFQj2U2wyQSZBmZgFV9Osu8HjaE-06znw1igEANc9JqPbDFLBt93lki0MZCT6_MPSNui8lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff62ed07ca.mp4?token=JxJqJyxTBN5n70yDdPtkLhxfqLsyUtaK367W9aNw7yt351REJbrmnhQ22jA0-S3Fj6ofU7jPwmopt3BaaSI8shyxMn_cDwcQW5kUJvwV_kGJBRj6ewWSr71unTAn7pXUbSD_tgRjEGMOU3ZS6vYhVVX_FtdRNssHfh9BwriyuC0cNEh5-LHbcgdu79b4XKDMg3sK4aPQS2KZlUsgnYHJLgIElpYcUu1RhZ4Fkmzk-SsY4omkqRLM5y4G2c35Cw0FHF2oV5a-WfQHciePFQj2U2wyQSZBmZgFV9Osu8HjaE-06znw1igEANc9JqPbDFLBt93lki0MZCT6_MPSNui8lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گرم کردن بازیکنان ایران و بلژیک پیش از شروع بازی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/134049" target="_blank">📅 22:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134048">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onuBOjQI2hIEF1Rt-Ox-2LskUuaGUC91JScoK9DdwY0kMmm3OgZsjPCXAEUP-EpeH6LJhyZWNK_TzGrKsEMIX_K-OWBP4iUHwfu3O_5EN9qykVvvORyImPG8R5FbqYUl58ODOoVWMBi7R1phM5BLyfROKHXJ7vs1COVPso78n96fCyvrhXbUY5cbHXdrS7n0g-g-vtPMKBZ9x20IwaKVbV2vRjVpexK31IFQqPztqG3c_r-D8LvEbs0k-wSu7pc--tYj6Lw2hTNR_I9UnaDeC24_hiVw_ASWXAa_AVuGgtColZNdjlObZXrnwHQp_FDRUNHLHZ-RMg1NkdYL-Wn39Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇧🇪
تصاویری از رختکن تیم ملی ایران و بلژیک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/134048" target="_blank">📅 21:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134047">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
#فرهیختگان؛ بین اوسمار و مدیرای پرسپولیس بی اعتمادی شکل گرفته و حتی اگه اسکوچیچ منتفی بشه احتمالا اوسمار رفتنیه و پرسپولیس به سراغ مربیان داخلی میره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/134047" target="_blank">📅 21:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134046">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
گزارشگر پرشیانا اسپورت: قلعه نویی یجوری ترکیب چیده که کل رسانه های دنیا هنگ کردند شماتیک این ترکیب چیه
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SorkhTimes/134046" target="_blank">📅 21:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134045">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
گزارشگر پرشیانا اسپورت: قلعه نویی یجوری ترکیب چیده که کل رسانه های دنیا هنگ کردند شماتیک این ترکیب چیه
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/134045" target="_blank">📅 21:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134044">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
ترکیب ایران مقابل بلژیک
🔴
علیرضا بیرانوند، صالح حردانی، محمد حسین کنعانی‌زادگان، شجاع خلیل‌زاده، علی نعمتی، سعید عزت‌اللهی، احسان حاج صفی، رامین رضاییان، سامان قدوس، محمد محبی و مهدی طارمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/134044" target="_blank">📅 21:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134043">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
یک ماهه
25 گیگ 220T کاربر نامحدود
30 گیگ 280T کاربر نامحدود
35 گیگ 320T کاربر نامحدود
55 گیگ 420T کاربر نامحدود
100 گیگ 600T کاربر نامحدود
دوماهه
50 گیگ
380T تومن کاربر نامحدود
70 گیگ 450T تومن کاربر نامحدود
150 گیگ 700T تومن کاربر نامحدود
200 گیگ 750T تومن کاربر نامحدود
سه ماهه:
120 گیگ 680T تومن کاربر نامحدود
160 گیگ 730T تومن کاربر نامحدود
230 گیگ 800T تومن کاربر نامحدود
320 گیگ 950T تومن کاربر نامحدود
400 گیگ 1.1T تومن کاربر نامحدود
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/134043" target="_blank">📅 21:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134042">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❗️
شبکه ۱۴ اسرائیل: قطر و پاکستان از ترامپ خواستند تا پیامی برای کاهش تنش تنظیم کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/134042" target="_blank">📅 21:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134041">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❗️
🇮🇷
ترکیب تیم ملی ایران مقابل نیوزیلند
🇮🇷
🇮🇷
🇮🇷
علیرضا بیرانوند، شجاع خلیل‌زاده، علی نعمتی، میلاد محمدی، رامین رضاییان، سعید عزت‌اللهی، سامان قدوس، آریا یوسفی، محمد محبی، مهدی طارمی و شهریار مغانلو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/134041" target="_blank">📅 21:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134040">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✅
فارس و تسنیم : مذاکرات بخاطر تهدید های ترامپ متوقف شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/134040" target="_blank">📅 21:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134039">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anlsLlYUXr_U699ezmUjz8icG2QK9WGh9qxBzHlG9lZfoyaqj3VsBF1UgpPfutAjDH6QtaKfDYKdAHq4hZ50j-ijmUHNng2QEWeDUNyiCnleRsfHWFur8U0J-5yOPS-QCvhol3gMHdEQJnz3Ahjh3eg4wcg6JHZOWUqjyocCHCobxkxw_LWXmlJHhOR6JrFttprzeBCxdCpkeEzlHHMr_OlSw3UMz96Z63fwazbu975AE_yiMS_OE0n67fN787LDUzt8wKKlaHGf4K7TbevdSPtVGKKXIwB3W2hk9vN9BDd2dRS4jnNy0D9RIxbJ_zdGS3pGH2XXPhukxxc81qDlRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه G جام‌جهانی ۲۰۲۶
[
ایران
🇮🇷
🆚
🇧🇪
بلژیک
]
⏰
یکشنبه ساعت ۲۲:۳۰
🏟
استادیوم
سوفای
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/134039" target="_blank">📅 20:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134038">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
کسری طاهری اعلام کرد با پرسپولیس به توافق نهایی رسیده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/134038" target="_blank">📅 20:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134037">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✅
فارس و تسنیم : مذاکرات بخاطر تهدید های ترامپ متوقف شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/134037" target="_blank">📅 20:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134036">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c475ba2cf.mp4?token=gF__h3_noSJx-qWVXsnhAQ0lpBma3B-HsSvOZatnp5Cmi3Z8ScNQbdDfQljlPeb_hVdsH-KUDQy9Usp1zOsVNjCqXqjr1Q4Q9mqL86gZc9WBuVaa2_gVT6ofLjoUAPhuVut-6fuYM2vGR2NifRvznA2bjJiI4hdVZiFdpAzOldQlF51MWL5YNzhpEBYnsM3_cQb9va3y9vMpNRtjVFuD1yyhp-XsDalcJ65F52jaXvMPyI4uuvPgfbFDdJFp4E3uutN_NwgpTNn7umDTla5g8zTdy3ld_bScZYaxCyV-FbG6-7HOTyx08caiptpYMVDLOwmPcosVHdoYtW9reFRiEgjDIN3Ge69d-zdCbsAlVb-SO0R5ZhlvJE_IIiWk4eNKGC6cfSKKRdjLo4mc3IgIGEspE41xQFYQ33bn-Va1IaaIJEp8Z60wMF18P5i-MNZR0fyR4W4sMKM3CBskp9mpfG-GbC8pW7raDS9RQuLTiTWcqw8JHEu0PVELdDkD9IJAByuBhBAUx0OXrXE3kqySjmoeGHlO-5qt4ltyevFs1VwqUOguhO2rDY1Cu2_DTbp99vQPdfigN6o-M9YXC1gPnJMulU54gkav-6IFTi4W08jI9dJtzPkyGWaG2HA04jUnNxUsMQZdMutEi8tAnWa3Hzzym-FWUZOnYBzrk3ysZg0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c475ba2cf.mp4?token=gF__h3_noSJx-qWVXsnhAQ0lpBma3B-HsSvOZatnp5Cmi3Z8ScNQbdDfQljlPeb_hVdsH-KUDQy9Usp1zOsVNjCqXqjr1Q4Q9mqL86gZc9WBuVaa2_gVT6ofLjoUAPhuVut-6fuYM2vGR2NifRvznA2bjJiI4hdVZiFdpAzOldQlF51MWL5YNzhpEBYnsM3_cQb9va3y9vMpNRtjVFuD1yyhp-XsDalcJ65F52jaXvMPyI4uuvPgfbFDdJFp4E3uutN_NwgpTNn7umDTla5g8zTdy3ld_bScZYaxCyV-FbG6-7HOTyx08caiptpYMVDLOwmPcosVHdoYtW9reFRiEgjDIN3Ge69d-zdCbsAlVb-SO0R5ZhlvJE_IIiWk4eNKGC6cfSKKRdjLo4mc3IgIGEspE41xQFYQ33bn-Va1IaaIJEp8Z60wMF18P5i-MNZR0fyR4W4sMKM3CBskp9mpfG-GbC8pW7raDS9RQuLTiTWcqw8JHEu0PVELdDkD9IJAByuBhBAUx0OXrXE3kqySjmoeGHlO-5qt4ltyevFs1VwqUOguhO2rDY1Cu2_DTbp99vQPdfigN6o-M9YXC1gPnJMulU54gkav-6IFTi4W08jI9dJtzPkyGWaG2HA04jUnNxUsMQZdMutEi8tAnWa3Hzzym-FWUZOnYBzrk3ysZg0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇧🇪
خداداد عزیزی: اصلا بگو دوکو نباشه لوکاکو هم نباشه، ما به صورت تکنیکی و فنی و بدنی هیچ جوره به بلژیک نمی‌رسیم و نمی‌تونیم رو در رو بازی کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/134036" target="_blank">📅 20:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134034">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
فوری | العربیه:
🔻
جلسهٔ دوم مذاکرات اندکی بعد آغاز می‌شود
🔻
هیئت ایرانی به سالن مذاکره بازگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/134034" target="_blank">📅 19:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134033">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❗️
فرهیختگان: حدادی اصرار دارد که قرارداد اسکوچیچ یکساله باشد چرا که ممکن است با ناآرام شدن احتمالی منطقه، این مربی خواهان پایان همکاری شده و آن وقت درخواست کل قراردادش را بدهد.
✅
اما اسکوچیچ با این خواسته حدادی مخالفت کرده و اعلام کرد در صورتی به پرسپولیس…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/134033" target="_blank">📅 19:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134032">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
اوسمار خواهان ترابی و هاشم‌نژاد شده ولی تراکتور با فروش هردو مخالفت کرده/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/134032" target="_blank">📅 19:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134031">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
ایسنا: پس از ۸۰ دقیقه، نشست ۴ جانبه ایران و امریکا با حضور میانجیگران پاکستانی و قطری جهت مشورت‌های داخلی متوقف شد و برای تنفس جلسه رو ترک کردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/134031" target="_blank">📅 19:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134030">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
لحظاتی پیش مذاکرات ایران با آمریکا در سوئیس شروع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/134030" target="_blank">📅 19:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134029">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس مذاکرات با دراگان اسکوچیچ به سرانجام نرسید و اسکوچیچ منتفی شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/134029" target="_blank">📅 19:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134028">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
❌
ترامپ:
🔴
هیچکس نمی‌خواست به ایران زمینی حمله کنیم، نه؟!
🔴
حتی اگر همین الان هم بهشون حمله میکردیم، رهبران و فرمانده هاشون فرار میکردن به غار هاشون که زیر کوه های گرانیتی ساختند.
🔴
این کوه ها خیلی محکم اند و نابود کردن شون سخته.
🔴
الان از غار اومدن بیرون…</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/134028" target="_blank">📅 19:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134027">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❗️
❗️
بیفوما با وجود اینکه جایی در برنامه‌های پرسپولیس نداره، به خاطر قرارداد ۷۰۰ هزار دلاری فصل بعد حاضر به جدایی نیست و باشگاه برای فسخ قراردادش به دردسر افتاده.
✅
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SorkhTimes/134027" target="_blank">📅 19:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134025">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس مذاکرات با دراگان اسکوچیچ به سرانجام نرسید و اسکوچیچ منتفی شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/134025" target="_blank">📅 18:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134021">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
|
#فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس مذاکرات با دراگان اسکوچیچ به سرانجام نرسید و اسکوچیچ منتفی شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/134021" target="_blank">📅 18:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134020">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/134020" target="_blank">📅 17:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134018">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
به گزارش خبرنگار قرمزآنلاین، مدیران باشگاه پرسپولیس تاکنون در دو دو نوبت با دراگان اسکوچیچ وارد مذاکره و بر سر کلیات قرارداد، تقریبا به توافق دست یافته اند. مانده جزئیات قرارداد بندهایی که هنوز به توافق نرسیده اند. دو طرف در حال صحبت هستند.
✅
البته برخی می…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/134018" target="_blank">📅 16:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134017">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
❌
قدوسی : با یه مقام ارشد باشگاه صحبت کردم، بند تمدید اوسمار فعال نشده و غرامتی قرار نیست بهش بدیم
❗️
حدادی و خلیلی در حال انعقاد قرارداد با اسکوچیچ هستن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/134017" target="_blank">📅 16:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134016">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
🔴
قدوسی : پرسپولیس و اسکو به توافق کلی رسیدند و فقط دو بند جزئی مانده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/134016" target="_blank">📅 16:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134015">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✅
فوووووووووووووری
🔴
گفته میشه اسکوچیچ خواهان دو بند بسیار مهم شده
✅
1_ حق فسخ قرارداد در صورتیکه جنگ بشه!
✅
2_ اختیار تام در نقل و انتقالات و انتخاب تیم مدیریتی (سرپرست) و رسانه ای و کادرخدمات تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/134015" target="_blank">📅 16:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134014">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
آخرین خبر از روند مذاکرات پرسپولیس با اسکوچیچ
🔴
مذاکرات مدیران پرسپولیس با دراگان اسکوچیچ سرمربی سابق تراکتور، در ترکیه ادامه دارد. پیمان حدادی مدیرعامل پرسپولیس، محسن خلیلی و علی اینانلو در ترکیه حضور دارند و در حال مذاکرات با اسکوچیچ هستند.
🔴
برخلاف برخی…</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/134014" target="_blank">📅 15:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134013">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❗️
خبرنگار الجزیره: ظهر امروز به وقت محلی قرار است مراسم نمادین امضا و مبادله متن توافق مرحله اول میان دو هیات ایران و آمریکا برگزار شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/134013" target="_blank">📅 15:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134012">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipE06O0XCJQMlgEz-V-XcIY1sFmoTf6m0wcHOIStQBNT5o-nGNJ6PMSAPIhjB-tQ5BIZs40uFsojtBeK0oQzfPDPErqh6zoT2UiM2ETZEsiCkQlHZV3S-4uR8fbJcNVi3bxnsLqTml0iWD2_RwCRlq3toDlcQf7pPWvzXj1cYMGxcGeNk4RjUyQtM-qZd7j6-hqPQUMe4MiyDP8KVEdXbxlK_OI1FQmM6KRqZ3CVO7e-JEcB40fP_WfGvBY1Mh0w4jfIHrwH-TFMaOuz-P8_kG4gv2GOXJfWbKNrscSDrj8juJsWXVhtInq1T9nqoQDPawWOcqlD9vdrU_jmpxbwiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇧🇪
غیررسمی: تروسارد از ناحیه کتف مصدوم شده است و احتمالا به بازی مقابل ایران نخواهد رسید
❌
پ.ن فکر کنم تا شب که بازیه کل بلژیک نرسن به بازی
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/134012" target="_blank">📅 15:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134011">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qb_38PEX_kGGQ7WT43X3pJXjIaL-AjgpcTGzUOjjEzRRDDgUAAxgG0SaWWM-Z95-T9_oDvHTKDMxdWDFuERlxchbGdKd1p_o_BF96tfAYAIMASeOUNfUlMf4ocUPh-4QaS1eCmUgRvAL47GNEsxC1vkJe2LXRKXeiwChIBKzbXPHCWn1JfV7Ii3E1jlgOvqqkX_b9NESd4ZkmSAc0s1aMaTKQMq1qSwfMNgc4bcoZsFdnlmxF0HZIgtVq_c3tSmCemwPkLy4Uj-NmGDMblcqFArO9J3krGFAU3XXTA41t_IAY_cIttVvkGSPbIK8VGfYd41N3nJze24Y6oH9DCU2wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فووووووووری / آنا
✅
پرسپولیس با اسکوچیچ به توافق نرسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/134011" target="_blank">📅 15:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134010">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">⚽️
خداداد: هنوز با پرسپولیس قرارداد امضا نکردم
💢
درمورد اسکوچیچ هم از نظر فنی و اخلاقی واقعا حرف ندارد؛ هم در تیم ملی و هم در تراکتور نشان داد مربی قابلی است. اگر پرسپولیس او را جذب کند برد کرده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/134010" target="_blank">📅 15:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134009">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5ynILuyA3ZD0Cbixt6WoyrabNk63TQtZWSRa2EFw9EJPRRGW5jE5AfE3lLhAkoU5I-BXFjamvZ9YBRIIRZI1173ZmsEI_GRP9wIIzWezkMWKJnaJ8OGvXVmE3HV584_XrmbKDy-yWzfKqK7IxateCr5EoBWlMhm63u0TSzk-VcAwvLpZZBRKlxZ5lpeTAr5HvXbE8rNzcmrxrBeAYjuGyCsRtaCDinbvLCuGrQ7B9dCFgZMVecwjE0umkXtwyGc-ofbk3poHanjq0sj57HLm_2IJlTnzxyAiUTsX5l8eINe_QdjD_eGL2h_mxYyGssGvOS1KXJ9xuF7o5GSeJttmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سهراب بختیاری زاده با عقد قراردادی دو ساله برای بار nام سرمربی استقلال شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/134009" target="_blank">📅 15:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134008">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✅
🇮🇷
برگزاری تورنمنت سه جانبه برای مشخص شدن نماینده ایران قطعی شد
⬛️
طبق اعلام کارگروه متشکل از اعضای هیئت رئیسه فدراسیون فوتبال و مسئولان سازمان لیگ، در صورتی که کمیته استیناف اگر تا 31 خرداد (امروز) رأی کمیته انضباطی درباره 3 بر صفر شدن بازی گل‌گهر - چادرملو را تأیید می‌کرد، گل‌گهر به‌عنوان نماینده سوم ایران راهی لیگ قهرمانان آسیا 2 می‌شد و اگر تا این تاریخ رأی این پرونده صادر نشود، یا رأی به سود چادرملو باشد، برای معرفی نماینده سوم ایران تورنمنتی سه‌جانبه بین پرسپولیس، گل‌گهر و چادرملو برگزار خواهد شد.
⬛️
به این ترتیب و با صادر نشدن رأی دیدار گل‌گهر - چادرملو، برگزاری تورنمنت سه‌جانبه بین پرسپولیس، چادرملو و گل‌گهر قطعی است و تیم‌های پرسپولیس و چادرملو باید 5 تیرماه به مصاف هم بروند و برنده این دیدار 9 تیرماه رودرروی گل‌گهر قرار خواهد گرفت تا تکلیف نماینده سوم ایران در آسیا مشخص شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/134008" target="_blank">📅 14:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134007">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEodt0Kg5pdB2-UE_eeY8VA2nnXuQG-ypa6pgKI2Gseis-Bg9DcYvbCueuY3fzdz-fBQlRzpoC_xxrvnzjZWxwLxBmKritz5BERrUyAgMGXy2f7AAgGFW9dmjxv9Eh9qrIdAVE9Ssr6LrW1jUIuPwi5RVOcDaWPNCxNKRBHklWpU9eoV57aeMkpW2GlorEdgNdh_byo-GOX5jORRI9aIvyXcglLLUNVwM_NLqppTDzufnH0JAtO21Y6vlFlsFswrKfCwMMkwdFiusbNf8UXpunP73he6eXjdod3C7YC809Wxsa77Xfh_rkuzh22crcNNsCsbHzwNeDswmUEO2FSQNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس ویژه جام‌جهانی
6⃣
2⃣
0⃣
2⃣
همراه با وینکوبت ادامه دارد!
🔴
Belgium -
⚪️
Iran
⚫️
جام‌جهانی گروه G
⏰
یکشنبه ساعت ۲۲:۳
۰
🏟
استادیوم سوفای
🎁
🔣
5⃣
1⃣
بونوس ویژه به مدت محدود روی تمامی واریزها فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
⏰
این بونوس ویژه وینکوبت فقط تا دوشنبه ۱ تیرماه ساعت ۲۱:۳۰ فعال است.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/134007" target="_blank">📅 14:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134006">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqX8k3l6ojpJp5f9hP-57rxW7B4bLDtPEyg9Vd6wIQrslKL4WQV2kL3ytr1k4lCzHtVcl6T2F_LiaE1myg4_ZctJheqAgNkcY1nS2JJT_uxrp2qHEl4v0fbNo1G-PAJXBUcs-abU4PBevpTo3T0p9KeB7lT6vI29rm3dall2KzteooezQknKLBuSNZ4y-UcbzOwvFyMmkp7ew61qbZAGGuR27H69pmsnZnSUa5hFCCAPedOrDiFN2mKeiYMJjJCbSiI1ZDISDIYeKyQA16tx502OibWBIMuuJarq5j5t3LiduOczO9oi794nYRG8U0Z3rzarTZs16cuAzOth0RLZ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آخرین خبر از روند مذاکرات پرسپولیس با اسکوچیچ
🔴
مذاکرات مدیران پرسپولیس با دراگان اسکوچیچ سرمربی سابق تراکتور، در ترکیه ادامه دارد. پیمان حدادی مدیرعامل پرسپولیس، محسن خلیلی و علی اینانلو در ترکیه حضور دارند و در حال مذاکرات با اسکوچیچ هستند.
🔴
برخلاف برخی اخبار که حاکی از توقف مذاکرات اسکوچیچ و پرسپولیس است، این مذاکرات ادامه دارد و احتمال توافق نیز پائین نیست. همچنان مذاکرات در خصوص برخی بندها ادامه دارد و در صورتی که در برخی شروط به توافق برسند، احتمال توافق وجود دارد.
❌
همچنین در خصوص فعالسازی بند تمدید قرارداد اوسمار و احتمال شکایت او از پرسپولیس، مدیران پرسپولیس مدعی هستند مهلت فعالسازی بند تمدید قرارداد او دهم اردیبهشت‌ماه بوده که در آن تاریخ این بند فعال نشده و قرارداد اوسمار تمدید نشده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/134006" target="_blank">📅 14:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134005">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❗️
جنجال بالا گرفت؛
❌
پاسخ باشگاه پرسپولیس به صحبت‌های تاجرنیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/134005" target="_blank">📅 13:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134004">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZYhMRJJnpVqsoCB_3DaaVmJ2WlGiZ_sLQyH09JkNtC1fOCLk0w9V-HqiVafNd8RzhB44MCX0FMLiEty7CxeNHnqEqaJ64Nq5q7QITaCoWep-YuK6aDKP802ZXRVjyTbJ5VPOlueAJ7sBZwjuj3o28xQbcKMY_ItnDCeUokc2sYfeHzqjtj6YEMT0H3fbDUzZR5xg2bsMxjyEGR1zUhWQahnCRIcAimg2Z_MSqQ9fqv9lj1cz3MRBmFWFAF0sSlrklFzAFedZycClZhicil9NQsvBhOhYwVa74VqQag6D6ccodROvEJ_8OMmBORIiapTXQU2acM7Npv2kDOTOF6ASg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تاجرنیا: جام قهرمانی رو بدید به استقلال دیگه  واسه سهمیه سوم هم جام حذفی برگزار کنید
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/134004" target="_blank">📅 13:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134003">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✅
مذاکرات پرسپولیس و اسکوچیچ بدون توافق به پایان رسید / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/134003" target="_blank">📅 12:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134002">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✅
فوووووووووووووری
🔴
گفته میشه اسکوچیچ خواهان دو بند بسیار مهم شده
✅
1_ حق فسخ قرارداد در صورتیکه جنگ بشه!
✅
2_ اختیار تام در نقل و انتقالات و انتخاب تیم مدیریتی (سرپرست) و رسانه ای و کادرخدمات تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/134002" target="_blank">📅 12:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134001">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
با وجود توافق اولیه بر سر مبلغ قرارداد، طبق پیگیری خبرنگار تسنیم مذاکرات بر سر دو بند همچنان ادامه دارد و توافق در مورد آنها تا این لحظه حاصل نشده است. طرفین امروز بر سر این دو بند که مربوط به مسائل مالی نیست؛ مذاکره می‌کنند تا در صورت توافق، قرارداد رسمی…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/134001" target="_blank">📅 12:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134000">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⚡️
جزئیات قرارداد دراگان اسکوچیچ با پرسپولیس:
⚡️
قرارداد دراگان اسکوچیچ با پرسپولیس برای دو فصل تنظیم شده است. اسکوچیچ فصل اول، یک میلیون و 200 هزار دلار خواهد گرفت و برای فصل بعد 10 درصد به آن اضافه می‌شود.
⚡️
در قرارداد اسکوچیچ، 500 هزار دلار به عنوان پاداش…</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/134000" target="_blank">📅 12:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133999">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
#فوووری
✅
ورزش سه طی خبری مدعی شد؛مذاکرات با اسکوچیچ بدون توافق به پایان رسیده و با توجه به تخفیف اوسمار ، احتمالا این سرمربی برزیلی در پرسپولیس موندگار خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/133999" target="_blank">📅 12:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133998">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❗️
❗️
ورزش‌سه: پرسپولیس با اسکوچیچ به توافق نرسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/133998" target="_blank">📅 12:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133997">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYPrHpntAvGf4H8Ck9XWNOiJeE9pkdZpvHKb18MslHWECxZgg_VPh2ufCZmtPov5dai0vXyBuR958sb-KMzy34E11SDG1riQhRNDXf0N-kWEQW--Ji4O-c4sEQitIG2gpAJgLGrdvJVzLk9YIsRcYST16zXVBXC9bQHWowMPxWaSNlTmXBZo6NRcCOnsnlkwtMT4mKPCt7Q8QmwG8h-9MP4ZEw1c0m3kxb0kTDVyOC1FsYkeR8BYXAICRVA38JA8IdXfQ16DM2ie7zlEyiI-J74Wtm9XeFdZaDePBciejCGBR0n7xDIPSONWYeZ_duWw9UmvtzshQP_v5DESPtkfHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
🇮🇷
ورود تیم ملی فوتبال ایران به لس آنجلس برای انجام دومین دیدار خود در جام جهانی مقابل بلژیک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/133997" target="_blank">📅 12:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133995">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
امروز آخرین روز مذاکره مدیران باشگاه پرسپولیس شامل پیمان حدادی، محسن خلیلی و امیرعلی حسینی (مسئول روابط بین الملل) و یکی از اعضای هیئت مدیره پرسپولیس با دراگان اسکوچیچ در ترکیه خواهد بود و انتظار می‌رود تا پایان امروز نتیجه نهایی این مذاکرات مشخص شود.//تسنیم…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/133995" target="_blank">📅 12:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133994">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZl28iWabpAcEMwZBB4TGhx4KqSp2E_zDfBwrypsUSiKQ8otLvu8enq8n5m4FGjNkPPVmePw_IP0IPM2-58_9UATlJbMPTMlEi4N0vAlF1tG0eewxpOyURtAMEy7LPg5z0uoMlXVb9-FWh2hZ-cacRUV2OQfJ7bd4QYuAICvX1GsvPTyKEjodhn4v1ahnwT6I4fnyQ4hLrU6fe3YO4cr_05mYaKRumEwHtZ4_ZNwWw8BW5BVWlX3xcNOgGrNPDZPv4eYo86VyNj2M4QUSrxy-V9yXgVo4756PJ0Ci6ilwTZ69c_I-GlDD1R9rmQjTkoOojtVxJuDLYP6f62g4fprPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جام جهانی جای عجیبیه!
🔴
🔴
توی یک شب میتونی راه ۱۰۰ساله رو طی کنی و این معمولا برای دروازه بان ها میوفته
🔴
🔴
مثلا همین ووزینیا دروازه‌بان ۴۰ساله کیپ ورد که تا ۲۵سالگی زباله بازیافتی جمع آوری میکرده اما با یک شب درخشش شگفت انگیز از ۵۰ هزار فالوئر به نزدیک ۱۵میلیون میرسه...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/133994" target="_blank">📅 11:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133993">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmOJo4WkSI5yP05sVzLj3QA0PsNt2n622P-A-DjysaaxjGcFb0jlzUskPR_uxV7snQgBzRceCBoym0fbBrkezWCoOaW1LeaEVyp979FxHlbrFM7E8BNYc0UoyfWs3FytjJ9hJaV2fU-v9Mi9MfGVhjjP6hIW0cSz0rRJWfkWMYdODuw6d2gg19gVnHH3rDMYSpjaaQVBSI6dH3ZBrWUlXkZqFVNIECfRLRXkG1j2AGk2tAcG16z5qzijwLS1G7IUH-FCUEIEJBonOh2sPrXcp7F9NvruZU1ekw9qGqD2Yzr0lBKIrb0DymKb7GveB5F65yX0bXYRRlqz1Wt1Wlx8ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
رومرو لوکاکو از لیست بلژیک برای بازی با ایران خط خورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/133993" target="_blank">📅 11:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133992">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
دانیال اسماعیلی فر ۱ ساله با تراکتور تمدید کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/133992" target="_blank">📅 10:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133991">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
با وجود توافق اولیه بر سر مبلغ قرارداد، طبق پیگیری خبرنگار تسنیم مذاکرات بر سر دو بند همچنان ادامه دارد و توافق در مورد آنها تا این لحظه حاصل نشده است. طرفین امروز بر سر این دو بند که مربوط به مسائل مالی نیست؛ مذاکره می‌کنند تا در صورت توافق، قرارداد رسمی…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/133991" target="_blank">📅 10:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133990">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❗️
ادامه مذاکره پرسپولیس با اسکوچیچ بر سر دو بند؛ امروز؛ صحبت نهایی
🔴
مدیران باشگاه پرسپولیس پس از انجام صحبت‌های اولیه با دراگان اسکوچیچ، بامداد روز گذشته (شنبه) برای مذاکره حضوری با این مربی راهی ترکیه شدند. روز گذشته  مذاکراتی جدی بین پیمان حدادی مدیرعامل…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/133990" target="_blank">📅 10:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133989">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❗️
مذاکرات میان اسکوچیچ و حدادی مدیر عامل پرسپولیس روند مثبتی داشته و اگر اتفاق غیرمنتظره‌ای رخ ندهد، اسکوچیچ به‌احتمال فراوان در روزهای آینده به‌عنوان سرمربی جدید معرفی خواهد شد./فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/133989" target="_blank">📅 10:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133988">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
هواپیمایی حامل هیئت ایرانی به سوئیس رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/133988" target="_blank">📅 10:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133987">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✅
✅
تاجرنیا: باید استقلال رو قهرمان لیگ معرفی کنند، ما حاضر بودیم لیگ برگزار بشه ...!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/133987" target="_blank">📅 10:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133986">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✅
✅
ورزش سه :  طبق تصمیم فدراسیون و سازمان لیگ، لیگ برتر فصل آینده با حضور 18 تیم برگزار می‌شود و از لیگ ناتمام امسال، هیچ تیمی سقوط نخواهد کرد و قهرمانی مشخص نخواهد شد .
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/133986" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133985">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
🔻
پرسپولیس با اسکوچیچ تموم کرد / قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/133985" target="_blank">📅 09:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133984">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPeEPIqOMjX5-bHl4lP0qRGu8Sp6JBdR9ZkweA3-TVmLWzvoMcPutOlZSavDY48-nM5rukf4ZwOWmmTbqlxPXVRsBjG_Ov--IDuOuk3qkuPAefyq2GI3DCVBFOa-TQJaMC5B1D08eWq3FhqYy5u9seUXvh_Z1RbrDtdN-M2y9vEMhqWcBkl4m0iAjak4n13B7crGT4ebkjif_C3X-OGHJztQ2g14xFqA4QzD3l96fTzkFq3yNlakel8H2m47l6NVrWbFqPe3J1kqIzStXHr9D--3f0-4Bhy1XYoo0XVr9gfpEpAOtaSYW_fn1IssSq1ZvwvXCOY4BMz2Gz_tT6fhFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امروز 21 June، روزِ جهانی دلتنگ شدنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/133984" target="_blank">📅 09:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133983">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arIq0hBSJv7L9vS8Ko_zbb_spRea1HReOqQYEVymNay8L7k9YcKqOdSgIEScRDjr__mC5PbgX4mgSVk8MQc_V1l9rk2q4GlPj9JAL1OVGjw6SiA0urmgHhvWTw_psl6jTF__rUBXAAggXU0oNtUj7T3hUWD4W1Rdlf8e8YmKocNhYgHHzT0WNKFxEUorhOD3PjWsxSO_3xI9ZF_8EjZWHyQQOgWonK0xjSe3r637189LnY-LznwTbwMn8bfBZSlzfSkLs4eYE1Q6PdkCqlE1BgkPC1iqARDgSlW4Tme80W1-_deFhGgKI-Z001U4DaaeL7xd09VvjK2cPOqX8jSPpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس ویژه جام‌جهانی
6⃣
2⃣
0⃣
2⃣
همراه با وینکوبت ادامه دارد!
🔴
Tunisia -
🔵
Japan
⚫️
جام‌جهانی گروه F
⏰
بامداد یکشنبه ساعت ۰۷:۳
۰
🏟
استادیوم بی‌بی‌وی‌ای
🎁
🔣
5⃣
1⃣
بونوس ویژه به مدت محدود روی تمامی واریزها فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
⏰
این بونوس ویژه وینکوبت فقط تا دوشنبه ۱ تیرماه ساعت ۲۱:۳۰ فعال است.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/133983" target="_blank">📅 02:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133982">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIguqkz0wIlXXseJiF_ujgV6ZM206XwbbCGSbadWbZacuJmOA6JA5HFJ8-VfliCxsO0s-0fb7XfUUNSUIAgpY9OJJW7D3c70erTKlrLW4BhKOtsf3W3REuw5Hr07GJ22BPkEKu5WzbeBLg8WGGprw4IRYXPc6-X9gMZBEuLhhmaZw1w-u7D4v8DhsTrCc0NlKOewtVbxTvNNpcAen7d5xdVo9T_TLmuaqZz4xrTV9lIRBTsj0tZY5onQdUclb2oXS9FXsatKKsRiW4DHRKDEToGY-vAXB3qmwEJyyYGyJQSmNNG68xa2RfGc6a6CcaEowmADEM0IeQ54ckR9dnCCxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیش‌بینی اپتا از نتیجه بازی ایران و بلژیک
🔴
سایت اپتا براساس ۱۰۰۰۰ شبیه‌سازی نتیجه بازی ایران و بلژیک را پیش‌بینی کرده که در آن شانس برد تیم ملی ۱۵.۱ درصد است. در این پیش‌بینی شانس برد بلژیک ۶۶ درصد و تساوی ۱۸.۹ درصد است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/133982" target="_blank">📅 01:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133981">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">⚡️
چه زجه ای میزنن ایجنت های اوسمار، بستون نبود هرچی نیم فصل خوردید؟!
🧐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/133981" target="_blank">📅 00:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133980">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
|
#فوری
⁉️
🏅
به گزارش رسانه «سرخ تایمز» تاکنون قراردادی بین باشگاه پرسپولیس و دراگان اسکوچیچ امضاء نشده؛اما مذاکرات بین دو طرف در حال انجامه و اینکه آیا اسکوچیچ فصل آینده سرمربی پرسپولیس خواهد بود یا نه نهایتا روز دوشنبه مشخص میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/133980" target="_blank">📅 00:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133979">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">⚡️
علیرضا نورمحمدی حماسه سازی کرده
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/133979" target="_blank">📅 00:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133978">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b80ddf04f1.webm?token=PyEWJQIXDV6MlyYpJ_rP82sG3fgngoX7BSQawYs6F2BgYcDh5M0cdNgsnhA9EmAQ2gRAjDBwQeYhMqkfiwY4ktjrWLKy8WeG9AULRw1snmVYtHl-9A2HSB_IW4gfWhmG0it6EPNckCs3wCQSzbcuiCLJXUYGoLATBOygKlAqmAchnBiyShXh2rw3HCU2qR6u_JIU2aIP00xoGACgaHLUfXNWQxV6FWIxWt2mqpOKdovtBJymj4oJKkaNoXfRhgxQFrOnHC0tNKhZdwQp7EAfDnTs4d170Xp-Ij4sA7PubE-y2d3CIOnObnCI34NDrP1-7DjyMyj7MzHqVM1jfBlTVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b80ddf04f1.webm?token=PyEWJQIXDV6MlyYpJ_rP82sG3fgngoX7BSQawYs6F2BgYcDh5M0cdNgsnhA9EmAQ2gRAjDBwQeYhMqkfiwY4ktjrWLKy8WeG9AULRw1snmVYtHl-9A2HSB_IW4gfWhmG0it6EPNckCs3wCQSzbcuiCLJXUYGoLATBOygKlAqmAchnBiyShXh2rw3HCU2qR6u_JIU2aIP00xoGACgaHLUfXNWQxV6FWIxWt2mqpOKdovtBJymj4oJKkaNoXfRhgxQFrOnHC0tNKhZdwQp7EAfDnTs4d170Xp-Ij4sA7PubE-y2d3CIOnObnCI34NDrP1-7DjyMyj7MzHqVM1jfBlTVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🆗
واکنش من به اخبار نقل و انتقالات این روز های باشگاه:
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/133978" target="_blank">📅 00:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133977">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🆗
واکنش من به اخبار نقل و انتقالات این روز های باشگاه:
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/133977" target="_blank">📅 00:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133976">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✅
بقایی سخنگوی وزارت خارجه
🔴
مردم مطمئن باشند که ما با آمریکا تعهدی را امضا نکردیم که‌اجرا نشود/از همین‌رو هیئت‌میناب 168 تیم مذاکره‌کننده‌ی ما به ریاست آقایان قالیباف و عراقچی و همتی راهی سوئیس برای ادامه مذاکره با آمریکا شد
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/133976" target="_blank">📅 00:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133975">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❗️
جرمی‌ دوکو ستاره تیم‌ ملی بلژیک دیدار مقابل ایران را از دست داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/133975" target="_blank">📅 00:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133974">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
بقایی سخنگوی وزارت خارجه
🔴
مردم مطمئن باشند که ما با آمریکا تعهدی را امضا نکردیم که‌اجرا نشود/از همین‌رو هیئت‌میناب 168 تیم مذاکره‌کننده‌ی ما به ریاست آقایان قالیباف و عراقچی و همتی راهی سوئیس برای ادامه مذاکره با آمریکا شد
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/133974" target="_blank">📅 00:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133972">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcsu-8VDDDjEIOPUwiUkqYEVG593aHd-rY9WvE6a2UdoqM650rxUZQJGavCCS3mpc9ioS2X9jpTcxdafsCEJSuiJzFJv2BXIq3rMZdtFOo6pO6x0n8fekAmQc6AWAst_l6vYcQO6u2NCr14Hrtk71fDFRfF2WlzfoOWHOqEc4S1D1noRVobzO4JpZCkA5OcW_9LMLma0GN-OnP2CqUN5y87Xk0pCD5uHN8YPktRRYm5rSXBvGZqcxVDmj1fRtjSI7Q-K79SWWr-lh-nQSL_GinwGaJLEwFBifISWnT1gbN_bMCcK55ESCa8BzETpWWkWbwpnf99hcTuITv6yLxatmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/133972" target="_blank">📅 23:50 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/Kk6zki0WAcTQH4lrISgtfPA8VutdwbqykJx-bZhBubUujfcBmzthiU4JZT5B9h3aOflFpk-lM5L7O2bWA4oRBCmq4YKngJlJvOl8W34wUMqirm0GSm_WuOBXivBx0fQnjodfS2amdTNxfHDE-ReRpZQHLAsM5kLfq_lER3GktdXTfMXTnACo3wKNp1eneo6i9ATUGry_kF-mJUxLzxypRcTmscCJjv_IsFGOiXkQOOyHtSoGVM3BSKuYxd67Yw6hEXEZvTLpDYjGVSABZkdG4hfd8hbnaezcmWALMFPETl342Y3BYHz4wUFGOlbjNqBb8sZsrg3Sd1unUySRKqXaTQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 957K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 20:54:24</div>
<hr>

<div class="tg-post" id="msg-124878">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecc68640c6.mp4?token=Fompo1x1qfjh9-6cfqOcinCY_gj4NNuRnkHUipJQI3nZMw_vu3zkV_22qhznm-aHW7fvOQe8L4VAKVenBGjRtNDnS2zscPSN6lZB2XTVrkUa3-f55wpB6RfeCilUbGNt71fSzAIEfkhmuTbw9bNByR50AB98kjnQfCVRF7qLIAaHb4UdfBEALWk-e193cobum-hpVyGfJSrM2Bif1rXQ2M2oa0kiN1fLj6i2A95XrqsrpBbyqpIESf7qyxcpAgyIKf0K0MK8glr69H7rnb1FuZDO-oJMZ86OVLkrJjwkUNuNoz5FOJKiCCMbW6WFmdtKFvSEUGK9G8u9rSAm0N1Omw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecc68640c6.mp4?token=Fompo1x1qfjh9-6cfqOcinCY_gj4NNuRnkHUipJQI3nZMw_vu3zkV_22qhznm-aHW7fvOQe8L4VAKVenBGjRtNDnS2zscPSN6lZB2XTVrkUa3-f55wpB6RfeCilUbGNt71fSzAIEfkhmuTbw9bNByR50AB98kjnQfCVRF7qLIAaHb4UdfBEALWk-e193cobum-hpVyGfJSrM2Bif1rXQ2M2oa0kiN1fLj6i2A95XrqsrpBbyqpIESf7qyxcpAgyIKf0K0MK8glr69H7rnb1FuZDO-oJMZ86OVLkrJjwkUNuNoz5FOJKiCCMbW6WFmdtKFvSEUGK9G8u9rSAm0N1Omw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو : با هم انجام دادیم، تو نزدیکی و همکاری‌ای که قبلاً هرگز نداشتیم
🔴
باید دوباره بگم، رئیس‌جمهور ترامپ بهترین دوست اسرائیل بوده که تا حالا داشتیم؛
🔴
هیچ‌وقت چنین دوستی تو کاخ سفید نداشتیم، او از همه جلو زده، و این شراکت خیلی قوی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11 · <a href="https://t.me/alonews/124878" target="_blank">📅 20:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124876">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvS3_lLr5dhEPBRFtfMaims3lEzC8veMpCPUFgcZe9Ik_z_hrSWqc8kj7xMMeWOEGUHVV5McvwTrxtQJdbBRa4ky2w71p2IA_5qmHPKVB_nWEcXrTjNZs3ctit7ejdzJyY-jILPWZkPGGQloWM_2ztB4pumfTnMj7u0bidAbn8VyyEsyAsYKON2c0HblwEhDtlY6iqv7_r7dINyrHYGyn4bdOzfK1g-YKDDw1AZlvKZDIN5Fva8NcO22QAjfKrUra0KRFUqy97IDfU-NvkooFaSpNV1Y91yQixrFoDCBNgAm3ckFzy0KbugujTdb4m8GN-cO4wh7eghYVxj9HgCLpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/194eb7223c.mp4?token=VLVWK7rVKolP1Y-lCP1fsFptcK17SUSinvYshLOWLRptwn56FBZdWWneJuOBsEKZP64omg84VLHCBuHFsPI2GQ8hIzlXcMuwoHnF0pf2VEyHKPoeOUPwefvLVOSQDsHdWsLYYCYMQ0YAEYc-_nU2rR4dDb9NwOSDtqhWtXgH7hxttEnCE6oWv55rL6AtXDYCmoR1Joga0-O3aPREUFei31stVNx4wETxsN8KHYN5HjDYk5usRSUGmMSmTO5Z5-BxIyLiH0up-B8-F5t6GlzjYqKKcE6Yf03TSI5AMPsQVsHmQ1lUACrqGOWn8_oa3l2RMHWkZkvLn5McaT49qFwXVBcFFdzIjeA5UwCdj5EqcEBPfrLG0ksakTWqg3iI-HW9dsdMsZKXPeiSO06T8nh3Tld_xKyeJCgnSi0y6s3Rc2HGI0UXAHHheBMaKWXV1HM2pv1my2Oi51hYSK-GwsQmC2mbNBT2BYi02YkvkhgUtwh4_Zl03TymRBg36wwxljuAjLMDoY7x2MVUHAxYx7AisSgfLPyC3Hku2qxjVU3D_Bk9XK4sAV26M3GOkG20GRTW-EqrMsIC-RVdlFQXTFGTkcjqRoXAUgJjfp_EWvyoi2opcqx8f9zDrFqdNPgVoR_BHGJx-51N2KTI8ebCci4vgkAmCBhvE7AY9DO-rN6smQo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/194eb7223c.mp4?token=VLVWK7rVKolP1Y-lCP1fsFptcK17SUSinvYshLOWLRptwn56FBZdWWneJuOBsEKZP64omg84VLHCBuHFsPI2GQ8hIzlXcMuwoHnF0pf2VEyHKPoeOUPwefvLVOSQDsHdWsLYYCYMQ0YAEYc-_nU2rR4dDb9NwOSDtqhWtXgH7hxttEnCE6oWv55rL6AtXDYCmoR1Joga0-O3aPREUFei31stVNx4wETxsN8KHYN5HjDYk5usRSUGmMSmTO5Z5-BxIyLiH0up-B8-F5t6GlzjYqKKcE6Yf03TSI5AMPsQVsHmQ1lUACrqGOWn8_oa3l2RMHWkZkvLn5McaT49qFwXVBcFFdzIjeA5UwCdj5EqcEBPfrLG0ksakTWqg3iI-HW9dsdMsZKXPeiSO06T8nh3Tld_xKyeJCgnSi0y6s3Rc2HGI0UXAHHheBMaKWXV1HM2pv1my2Oi51hYSK-GwsQmC2mbNBT2BYi02YkvkhgUtwh4_Zl03TymRBg36wwxljuAjLMDoY7x2MVUHAxYx7AisSgfLPyC3Hku2qxjVU3D_Bk9XK4sAV26M3GOkG20GRTW-EqrMsIC-RVdlFQXTFGTkcjqRoXAUgJjfp_EWvyoi2opcqx8f9zDrFqdNPgVoR_BHGJx-51N2KTI8ebCci4vgkAmCBhvE7AY9DO-rN6smQo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
جاویدنام سید داوود امامی میبدی ۳۹ ساله، ۱۸ دی ، میبد یزد
🔴
علیرغم تلاش رژیم برای تصاحب مرگ او بخاطر مذهبی بودنش، خانواده اجازه ندادند تا این اتفاق بیفتد.
🤔
عرزشی حرام زاده، غیرتت رو دادای، شرفت رو دادی، دینت رو دادی که اسلحه بگیری به سمت مردم خودت
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/alonews/124876" target="_blank">📅 20:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124874">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
وزارت امور خارجه انگلیس امروز چهارشنبه به بهانه ورود یک پهپاد روسی به رومانی اعلام کرد که سفیر روسیه را احضار کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/alonews/124874" target="_blank">📅 20:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124873">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
خبرگزاری فارس، به نقل از مذاکره‌کنندها :  ما هیچ توافقی رو قبول نمی‌کنیم که لبنان نادیده گرفته بشه یا از معادله حذف بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/alonews/124873" target="_blank">📅 20:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124872">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05cf1b4b47.mp4?token=DRVxmkG742-_Uc7LIplu5DmNqSVpASDH_mUml7BfuNYjNmEPIgaqXxvd6nR-FTNU5OC5771R2sT_QS9SozEUcY0L8jz3AlIwvYBzhFpfWOc0kNtuD4oeDEeyuDszjjU5yVuwkIrdHN3obgN9NcAgFR5FHpRtMbfajR6gy8azVIlZJTqbm_uB1biIWCrStl4cEgyhxRQ3XqNUnAVdtm3nv4shBPiRZCFTTgd87XkF5l1FHmlyj7S3Ub_HZMxZfp0iLiahhOtDRJzJYTt7Iy0p-kuaKo7T3-2fZdEO-B1wSg7XbXFzQbeNNFswhUkwNXSDhkalyPSOBtMbTID1aIY3ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05cf1b4b47.mp4?token=DRVxmkG742-_Uc7LIplu5DmNqSVpASDH_mUml7BfuNYjNmEPIgaqXxvd6nR-FTNU5OC5771R2sT_QS9SozEUcY0L8jz3AlIwvYBzhFpfWOc0kNtuD4oeDEeyuDszjjU5yVuwkIrdHN3obgN9NcAgFR5FHpRtMbfajR6gy8azVIlZJTqbm_uB1biIWCrStl4cEgyhxRQ3XqNUnAVdtm3nv4shBPiRZCFTTgd87XkF5l1FHmlyj7S3Ub_HZMxZfp0iLiahhOtDRJzJYTt7Iy0p-kuaKo7T3-2fZdEO-B1wSg7XbXFzQbeNNFswhUkwNXSDhkalyPSOBtMbTID1aIY3ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو : اسرائیل آمادست، آمریکا هم آمادست، ایران داره با آتیش بازی می‌کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/alonews/124872" target="_blank">📅 20:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124871">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
نتانیاهو : ما با مردم ایران دشمنی نداریم، ما با این آیت‌الله‌ها طرف هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/alonews/124871" target="_blank">📅 20:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124870">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
روبیو: گفتگوها با ایران درباره غنی‌سازی اورانیوم و بحث ذخایر است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/alonews/124870" target="_blank">📅 20:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124869">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ترامپ: رابطه من با نتانیاهو عالی است و در مورد مسئله لبنان بین ما توافق وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/alonews/124869" target="_blank">📅 20:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124868">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
مقامات اسرائیلی: تخمین زده می‌شود که اسرائیل در روزهای آینده به بیروت حمله کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/124868" target="_blank">📅 20:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124867">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiPLgWX_HdO8eZGX7OH8Lk3cIbYilaKqqdnEJFmqQFULXCBJ2yUUMyz085F99AMIjc-Yhu_I38PDZvgEUOqBYE7K8gsi0HzaqSzJF41cyn171XdyIOXToVwSZi7NEa6agDkpjn8p39hfCw466MqXzOTC2TtQDp0lV5VlQIUTxpM9Z44h3BURzPeTckuPTp2iG1NgS2sTV3CsBoR4bJ0hkEijww_L54gxnpXn7QpHRhPEe08OhRnO3ZACPHJ9Hmk3JdC10F6_iYV0HY1tlZJDZdy-no-XrDZhiIgLZwmLT7qvsT-uYAdIh-zXoS5DPGG7tVWbTcEWHw-b6Ij3eVk9Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قدیری‌ابیانه: نتانیاهو فیلم تجاوز ترامپ به دختربچه‌های کوچک را دارد!
🔴
علت جنگ آمریکا علیه ایران این است که نتانیاهو علیه ترامپ آتو دارد و فیلم تجاوز ترامپ به دختربچه‌های کوچک را دارد و نتانیاهو این را اهرم فشار علیه ترامپ قرار داده تا هر کاری اسرائیل می‌خواهد، آمریکا انجام دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/124867" target="_blank">📅 20:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124866">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
روبیو: تحریم‌های ایران کاهش نخواهد یافت، مگر اینکه غنی‌سازی اورانیوم و اورانیوم با غنای بالا را کنار بگذارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/124866" target="_blank">📅 20:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124865">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/450fe35b73.mp4?token=RTv581s7h3Gh51AR3L7xp5tKIqJuNMgjwFPWZ36J6aQHYsLvUpJdAcUrLKjn8tZusgSaqRBa7MkDiFsTfU_pl4wiyzf_aUQwotwR7yeluoUzQmkwvDg8-J9X7pn8dLR1N0YWxnJDt0EDSxjM-tF148OgdNxmRrtGCVqefdJd0Stnb0_5atXNn6FMg894qGOLOBaG0YGbCuQ_JnmtXdjM-nfRK06YJd9sde3gPHhOfRXpoFiTU4y2CbBWDe7kImsg5Ap4rJDWHl8HOElKkz-L8kGPWfAMY0wUskqbhhZX3VN6RhSMMsREI6p21AYmZ60pwYEFRo8PDPU_xMLwCUFMHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/450fe35b73.mp4?token=RTv581s7h3Gh51AR3L7xp5tKIqJuNMgjwFPWZ36J6aQHYsLvUpJdAcUrLKjn8tZusgSaqRBa7MkDiFsTfU_pl4wiyzf_aUQwotwR7yeluoUzQmkwvDg8-J9X7pn8dLR1N0YWxnJDt0EDSxjM-tF148OgdNxmRrtGCVqefdJd0Stnb0_5atXNn6FMg894qGOLOBaG0YGbCuQ_JnmtXdjM-nfRK06YJd9sde3gPHhOfRXpoFiTU4y2CbBWDe7kImsg5Ap4rJDWHl8HOElKkz-L8kGPWfAMY0wUskqbhhZX3VN6RhSMMsREI6p21AYmZ60pwYEFRo8PDPU_xMLwCUFMHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: ما هنوز در ناتو هستیم، اما ناتو به تغییرات قابل توجهی نیاز دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/124865" target="_blank">📅 20:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124864">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4735e0d3d0.mp4?token=mEBMGmqB4QhPHPj-W5mJmHtinY6jv0WosCr-TKVVW8OUNsvj_Q0wXz-JGNmepzBWGK60ErVfIkRNOwTLu0qkzyLjcL9G6QZLhuIQHFef68-C5xwNFYtrtXK5OGYVfOSTnjcAkuujBg5wa79TYYxV9_ALUfRZ5nEKnM06EjuFb6bxQaD8EsuNW9xRRzqjX5ci8OMrYmehEeIJF6F3KAF5xw9sIZEJ2Hztz9uzAT_OBPyEC6rp_fvIUceg0cpTZ7HsQ_qwRIVVD7zlRhwgnT2zQxDZPDHLhLPvwBvbuqE8kRKYu7EjV0bVbo7uAADnL3fUYv4ZQOZ6CpZs2MdILY-qFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4735e0d3d0.mp4?token=mEBMGmqB4QhPHPj-W5mJmHtinY6jv0WosCr-TKVVW8OUNsvj_Q0wXz-JGNmepzBWGK60ErVfIkRNOwTLu0qkzyLjcL9G6QZLhuIQHFef68-C5xwNFYtrtXK5OGYVfOSTnjcAkuujBg5wa79TYYxV9_ALUfRZ5nEKnM06EjuFb6bxQaD8EsuNW9xRRzqjX5ci8OMrYmehEeIJF6F3KAF5xw9sIZEJ2Hztz9uzAT_OBPyEC6rp_fvIUceg0cpTZ7HsQ_qwRIVVD7zlRhwgnT2zQxDZPDHLhLPvwBvbuqE8kRKYu7EjV0bVbo7uAADnL3fUYv4ZQOZ6CpZs2MdILY-qFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: خود ترامپ در نشست بعدی ناتو در آنکارا، ترکیه حضور خواهد داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/124864" target="_blank">📅 20:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124863">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
قالیباف: دوران تهدید بی‌هزینۀ ایران به پایان رسیده و هر تجاوزی با پاسخی پشیمان‌کننده مواجه خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/124863" target="_blank">📅 20:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124862">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RwdY5cUxynGTfZ4BzG7kn2qyBOipBykB__yOevi-BOVlTmu5h2_SJk-L0TW05GEH_4LLiKC8-0hJz685fdAh1OCKvF7O8LyPcOVHkrmpL2MGZ0P8pLFwcBYpxLnutG2QHPu2WmmdwAbeyNvmgy77qYzU13hgOXX3pd8vAgonODt41b7PfOi4usz2Pn919HRGBXjAfGOenFQwiAw_y4hiI20ZZKFwIbYAdXbYbYFh6JwC9hwb6-jOJpnNk76188nkPpONV87Wl87fIep3FRVWDKrAnWu_g-b_8qKhJaVyDL1pykkqXxEOg79smsJJkUkrHKJOS5GI3VmgOKmeWL033Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سردار غلامرضا جلالی رئیس سازمان پدافند غیرعامل: علی‌رغم همه انتقادها، برخی از اسرار کشور را افشا نمی‌کنیم، چون اطلاع‌رسانی عمومی در برخی موارد می‌تواند موجب ترس و نگرانی در جامعه شود
!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/124862" target="_blank">📅 20:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124861">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
رئیس ستاد ارتش اسرائیل: هیچ برنامه‌ای برای آتش‌بس در جبهه لبنان وجود ندارد و عملیات تهاجمی ادامه خواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/124861" target="_blank">📅 20:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124860">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
وزیر صنعت : با دستور مستقیم رئیس‌جمهور، تمامی موانعی که منجر به توقف خطوط تولید یا معطلی مواد اولیه در بنادر می‌شود، می‌بایست برطرف شود.
🔴
امروز نیز خط تولید، خط مقدم دفاعی ماست.
🔴
مسائل و نگرانی‌های موجود در حوزه تامین مواد اولیه و واردات با همکاری تیم اقتصادی دولت در حال تسریع است و اجازه نخواهیم داد چرخ تولید متوقف شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/124860" target="_blank">📅 20:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124859">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
روسیه: مذاکرات ایران و آمریکا باید به ثبات پایدار در خاورمیانه منجر شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/124859" target="_blank">📅 20:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124858">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
به گفته برخی منابع: تصاویر ماهواره‌ای جدید نشان می‌دهد که در پایگاه آمریکایی «علی‌ السالم» در کویت، یک آشیانه پهپاد یا هواپیما تخریب شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/124858" target="_blank">📅 20:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124857">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf324326a7.mp4?token=Bfh78W6_vFYubqMDqs0A9iX4s81vobu5xpdC5FZ7o12tB7hMZR0k9GmqeBVlKGPNqvAovshuNTVo51J2gltknwKj5o8VPgeeY7-qvYtIsqM4In4lBRixQ9plUISMOcgYZ4AnlGIZKSAEms0CYvCDDHGPeS2iP6xo_E_KqEl9iJtdB2rKnNA1dWd9zkY0MxaohWtmDRofr0V_ysBBTZ4hmlb_cJgJPfjBmYSwJkKOaRT6Z6SekaLXhX8dANVmzZhuZQzkeYDilEL_bHyiccAPWAAe1j-opYTvaEVQynqCwRpBy9U0_t_BPn9BB47awTeXqFa93sVmbkdTy9gDZ4QdJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf324326a7.mp4?token=Bfh78W6_vFYubqMDqs0A9iX4s81vobu5xpdC5FZ7o12tB7hMZR0k9GmqeBVlKGPNqvAovshuNTVo51J2gltknwKj5o8VPgeeY7-qvYtIsqM4In4lBRixQ9plUISMOcgYZ4AnlGIZKSAEms0CYvCDDHGPeS2iP6xo_E_KqEl9iJtdB2rKnNA1dWd9zkY0MxaohWtmDRofr0V_ysBBTZ4hmlb_cJgJPfjBmYSwJkKOaRT6Z6SekaLXhX8dANVmzZhuZQzkeYDilEL_bHyiccAPWAAe1j-opYTvaEVQynqCwRpBy9U0_t_BPn9BB47awTeXqFa93sVmbkdTy9gDZ4QdJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حزب‌الله فیلمی منتشر کرد که نشان می‌دهد یک پهپاد FPV مجهز به دوربین حرارتی، یک خودروی زرهی نامر ارتش اسرائیل را در حومه جنوبی یحمور الشقیف در جنوب لبنان دیروز هدف قرار داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/124857" target="_blank">📅 20:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124856">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
رافائل گروسی مدیرکل آژانس بین‌المللی انرژی اتمی در گفت‌وگو با شبکه اسکای‌نیوز با بیان اینکه از موقعیت مکانی ذخایر اورانیوم غنی‌شده ایران که در جنگ  سال گذشته هدف حمله قرار گرفت، مطلع است.
🔴
او ادعا کرد که این مواد همچنان در همان محل پیشین قرار دارد اما دسترسی به آن به‌دلیل خسارت‌های فیزیکی دشوار شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/124856" target="_blank">📅 20:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124855">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
فارس: تاریخ برگزاری آئین وداع، تشییع و خاکسپاری رهبر اعلام شد
🔴
۲۰، ۲۱، ۲۲ خرداد/ وداع در حرم امام‌ خمینی
🔴
۲۳ خرداد/ تشییع در تهران
🔴
۲۴ خرداد/ تشییع در قم
🔴
۲۵ خرداد/ تشییع در عراق
🔴
۲۶ خرداد (اول محرم)/ تشییع و خاکسپاری در مشهد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/124855" target="_blank">📅 19:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124854">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
فارس: تاریخ برگزاری آئین وداع، تشییع و خاکسپاری رهبر اعلام شد
🔴
۲۰، ۲۱، ۲۲ خرداد/ وداع در حرم امام‌ خمینی
🔴
۲۳ خرداد/ تشییع در تهران
🔴
۲۴ خرداد/ تشییع در قم
🔴
۲۵ خرداد/ تشییع در عراق
🔴
۲۶ خرداد (اول محرم)/ تشییع و خاکسپاری در مشهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/124854" target="_blank">📅 19:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124853">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
وزیر امور خارجه آمریکا: هیچ پاداشی در ازای امضای توافق به ایران ارائه نمی‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/124853" target="_blank">📅 19:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124852">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aea964f03e.mp4?token=llQCMWho2_baxkPfK1wVZhc-XclJeJFJT_U7caAgmBOFUC00QGoON29YrLFl7mEsW0AJl-sm26I_oPCdTSh98t6-GAIvHsfozI5pQ61R4IaQgbOPAIvlLvzzxoVMOuoHKOTX9krPisb1BPYZKY7pNVfzuAj5xQmohDa8kCf_VIooSs97TB2oEWQiCLaI7LGmiZ-j8nX4kXm3G9nSvr99NQ2ycIA7JQD-St9C0-K8mhC-34smUY3y47V7LPU01qIfbnEfjtoy1fruKoQoMYSK2n0hupJgZTEYkTbGhPvmzmDrKGt9CocNlrSXzt5NEnCdEcIfBwUtkP7-gHzllbE6Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aea964f03e.mp4?token=llQCMWho2_baxkPfK1wVZhc-XclJeJFJT_U7caAgmBOFUC00QGoON29YrLFl7mEsW0AJl-sm26I_oPCdTSh98t6-GAIvHsfozI5pQ61R4IaQgbOPAIvlLvzzxoVMOuoHKOTX9krPisb1BPYZKY7pNVfzuAj5xQmohDa8kCf_VIooSs97TB2oEWQiCLaI7LGmiZ-j8nX4kXm3G9nSvr99NQ2ycIA7JQD-St9C0-K8mhC-34smUY3y47V7LPU01qIfbnEfjtoy1fruKoQoMYSK2n0hupJgZTEYkTbGhPvmzmDrKGt9CocNlrSXzt5NEnCdEcIfBwUtkP7-gHzllbE6Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انتقال گسترده تجهیزات و جنگنده‌ها از طریق اروپا به سمت خاورمیانه ادامه دارد و ظرفیت نظامی در حال افزایش است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/124852" target="_blank">📅 19:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124851">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHQzz_K5DPgQELPsKFgu3zJiRgtT_sZZiJoNxJQduRRvfnCwb9Yq8elm6CPyNIwQ-UPPSv3cukGsBaDdoh9_6bQAugg5UDybi0T3vrYOGcb6suFog7x5SizvbsnS61GjJYPDUZW0kcLlOYYuFqDo5_zFbgzisZ5VZkVPsP6m7mLRUnHseEx-UrpnN_9PvXtiw-GG78ETMYfeRKWrDqPpwl_F1O4l_v4w6JtyHmPB76jin6wSGU2WAfRimHraFV6wUFBm9ybwSl7X5cgIYMyGeIWwfbe8qbTiAJG2-owfyy7bdLRRXcm1wi_HAUF9lGuD0q3Tl5JBLr4ElmRyetY0-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثروتمندان فوق‌ثروتمند جهان کجا بیشتر می‌شوند؟ / آمریکا اول، چین دوم
پیش‌بینی می‌شود بین سال‌های ۲۰۲۱ تا ۲۰۲۶:
🔴
آمریکا حدود ۶۷ هزار نفر به جمعیت ثروتمندان فوق‌ثروتمند (دارایی خالص بیش از ۳۰ میلیون دلار) اضافه کند که بیش از هر کشور دیگری است.
🔴
چین در رتبه دوم قرار دارد.
🔴
هند هم از نظر تعداد و هم نرخ رشد در میان کشورهای بالای جدول است.
🔴
لهستان، قطر و ترکیه سریع‌ترین رشد درصدی را تجربه می‌کنند و جمعیت ثروتمندان فوق‌ثروتمند آنها بیش از دو برابر خواهد شد.
🔴
این روند نشان می‌دهد که خلق ثروت به‌تدریج از مراکز مالی سنتی فراتر رفته و به اقتصادهای نوظهور و در حال توسعه سریع گسترش می‌یابد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/124851" target="_blank">📅 19:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124850">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی مجلس: توقف جنگ در تمام جبهه‌ها در صدر متن توافق ما با آمریکاست
🔴
اجازه نخواهیم داد آمریکا و اسرائیل خدشه‌ای بر اتحاد مقاومت و ایران اسلامی وارد کنند.
🔴
به پیروزی مقاومت معتقدیم و ایمان داریم با فهم مشترک و تلاش هدف نهایی که همان نابودی اسراییل است، محقق می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/124850" target="_blank">📅 19:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124848">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBZP1d20ZjYg2zaj8VXKd5bIeFXYxODRlPk8UEhqov78wCrxQjNziAdYHiySu1Dq4RVjks_D-UgebKXLaFfY69qLoT5WSZPDtWQsiR-gwzBJGeigH2l-ZkMi4Euxhz7nvauHI6cE_fi2CAFgyY4rF20KKD6wzT6PpIzDwmSC5ltPgEdXWlWYZ26ZakllAGwE1TSLlqG20RWIxVVCX9-LH6VYUjSJ6aswIIaWvfoGGSJ0oDtEekXgQHUUn2bQCSBrS9WxsojpKVymeZQk4Xq7B9-EYZAnuZ0W6apLsOTT9B3gRXTvT1kDPFh_Or6MZRnsJ64_zFvxQxIEXKNCq12Q5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e23753c660.mp4?token=IhIs_1pke82LDOMJSlr1Zwuoe2bgVBQf0wZh7bQXtfghCTuNvNQVgIiHt6wxFIy7djqA_UEMEy7hn14O0Mho4Uj1rDMwPeocvgmKUOoRin9zRJgonY5Oz_yJrWaqc7PKaOVyXFPHslPfAZf0eJ6NDI2MF7hnxITMD0u6C4SSku-bCad7JBr3mt9lnpRFpYTy68unGc9-S68uCKBCeXeLZQN1KvlIZWVbc34umL-9iDbC5f9ArVNLkcmBAfaop7Cg8BvVSCapoWO9WAvIo5B_IqyQe2_sAM_mMYr2BBpcaAF1894dkMR0v4yUCNQpinTkeJkUIeDDq7W50xoiKKbDuYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e23753c660.mp4?token=IhIs_1pke82LDOMJSlr1Zwuoe2bgVBQf0wZh7bQXtfghCTuNvNQVgIiHt6wxFIy7djqA_UEMEy7hn14O0Mho4Uj1rDMwPeocvgmKUOoRin9zRJgonY5Oz_yJrWaqc7PKaOVyXFPHslPfAZf0eJ6NDI2MF7hnxITMD0u6C4SSku-bCad7JBr3mt9lnpRFpYTy68unGc9-S68uCKBCeXeLZQN1KvlIZWVbc34umL-9iDbC5f9ArVNLkcmBAfaop7Cg8BvVSCapoWO9WAvIo5B_IqyQe2_sAM_mMYr2BBpcaAF1894dkMR0v4yUCNQpinTkeJkUIeDDq7W50xoiKKbDuYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
جاویدنام محمد جعفرپور 25 ساله
🔴
محمد به تمام آرزوهاش رسید، حتی به آخریش.
🔴
خط آخر: «من فدای ایرانم و تا توان دارم به ایران و ایرانی خدمت می‌کنم»
🤔
عرزشی حرام زاده با قتل عام کردن مردم عدالت علی رو میخواستی به نمایش بزاری؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/124848" target="_blank">📅 19:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124847">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
واکنش چین به تهدید تعرفه‌ای ترامپ:
جنگ تعرفه‌ای و جنگ تجاری به سود هیچ طرفی نیست
🔴
سخنگوی وزارت امور خارجه چین به گزارش‌هایی درباره پیشنهاد دونالد ترامپ رئیس‌جمهوری آمریکا برای اعمال تعرفه‌های اضافی ۱۰ تا ۱۲.۵ درصدی بر کالاهای وارداتی از ۶۰ اقتصاد از جمله چین واکنش نشان داد و گفت: پکن همواره با تمامی اقدامات تعرفه‌ای یکجانبه مخالف بوده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/124847" target="_blank">📅 19:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124846">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
وزارت کشور بحرین: ۱۵ نفر عوامل مرتبط با سپاه بازداشت شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/124846" target="_blank">📅 19:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124845">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2e58f8442.mp4?token=uVCx3pNunqZJm6Pk8KoGu6MVI8uAwf6mKQ-AttZqQ4nMWaE_7p8OmxIvLxqI5G9h9TDQk9jRCPUtijcZRgUbfK6kaZnu7quib4a_aLb5HLQYQRBLBTyZTLxakypTD2W_fEnwphjTcvCvtyLpbqwwG9WCcfR12CnXkGsi5eOTkDhR1vZBUxoP6TBp4nYCUFoPI_OJWk8vi4VbTiNYevvgyMuIDwOwr_XcbbqItXDOsBszoIZQK9L9Ehrygc2zJ-2GpXVBCMBWTcGsPh0hVXHqnirpql1Ok5wZ29afJBhMPCfOV6WQb4iqQ-ZlnFcdZLDSE3asKI5KtjzOpYAE5BK7mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2e58f8442.mp4?token=uVCx3pNunqZJm6Pk8KoGu6MVI8uAwf6mKQ-AttZqQ4nMWaE_7p8OmxIvLxqI5G9h9TDQk9jRCPUtijcZRgUbfK6kaZnu7quib4a_aLb5HLQYQRBLBTyZTLxakypTD2W_fEnwphjTcvCvtyLpbqwwG9WCcfR12CnXkGsi5eOTkDhR1vZBUxoP6TBp4nYCUFoPI_OJWk8vi4VbTiNYevvgyMuIDwOwr_XcbbqItXDOsBszoIZQK9L9Ehrygc2zJ-2GpXVBCMBWTcGsPh0hVXHqnirpql1Ok5wZ29afJBhMPCfOV6WQb4iqQ-ZlnFcdZLDSE3asKI5KtjzOpYAE5BK7mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کیم جونگ اون رهبر کره شمالی با تیم فوتبال زنان ناگوهیانگ ، اولین تیم از کره شمالی که قهرمان لیگ قهرمانان زنان آسیا شد دیدار کرد
🔴
واکنش اعضای تیم بعد از دیدن رهبرشون دیدنیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/124845" target="_blank">📅 19:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124844">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb8a354c14.mp4?token=HVOioWhrz6xGgHtSAG0ocq5_2geaAtflKR4rLWPefLnkS1T_LhAI_r_L1KvtZeR_iFWnGRuR8QJ0l6753chIWDUQYGJYvosIRz5W6KpsA-LWKyy8hAsvfDIj1tz35OjMzbnARRP-S6ZszO7n55E-ydTcbFQMB67GLZ0hicf-0rTFZVuFoNh4gxXquFl362C1QptFQA6N2cn93LG5P09N70uF2tECiE-9umb3pFHn0g-X2QI4lYqy_Gn-vLAigz5GnVMjaDKc_Q0V9jbwHIqczOiqELfTe_tCseWPydg1BamaeEPeAmMT8MruGIH9U4pCJ9zUZw28IYgCGR3dF83abA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb8a354c14.mp4?token=HVOioWhrz6xGgHtSAG0ocq5_2geaAtflKR4rLWPefLnkS1T_LhAI_r_L1KvtZeR_iFWnGRuR8QJ0l6753chIWDUQYGJYvosIRz5W6KpsA-LWKyy8hAsvfDIj1tz35OjMzbnARRP-S6ZszO7n55E-ydTcbFQMB67GLZ0hicf-0rTFZVuFoNh4gxXquFl362C1QptFQA6N2cn93LG5P09N70uF2tECiE-9umb3pFHn0g-X2QI4lYqy_Gn-vLAigz5GnVMjaDKc_Q0V9jbwHIqczOiqELfTe_tCseWPydg1BamaeEPeAmMT8MruGIH9U4pCJ9zUZw28IYgCGR3dF83abA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حزب‌الله فیلمی منتشر کرد که یک پهپاد FPV مجهز به دوربین حرارتی را نشان می‌دهد که دیروز گروهی از سربازان ارتش اسرائیل را در حومه زوطر الشرقیه در جنوب لبنان هدف قرار داد.
🔴
پهپاد FPV مستقیماً به صورت یکی از سربازان ارتش اسرائیل اصابت کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/124844" target="_blank">📅 19:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124843">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5578c6acc5.mp4?token=tEnCMSQ1nI1Rf-l_X2huZsLvK4L-QhBfOu9z7FpEKvMBs96lKpZtsTvQcihgm_PZhAt3E-cCnFu4KnMNidRKT4b9Tp1W09pQP8-YiJ6HTBmP5xV28Em6EbHZNyBiijNGBHwXntsDeD_WIu3mR07GfymE20dWYARB0kBOxvsnkx6jsZX9TDjYZy_hVGwiKt1jmApUgr_dTwILAmWWRYdQVU5ONbxfuYBsWl8MG13mt0ODrci3lZGjHwNPtimUaRKFS9UDwrfA_fJE_Wp94OmkiWNIL5GiPymSzzL7qe1tgyrzD_BhksV3tplaC5hBov9shCAulLWt8ObvHhOy4Cl3jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5578c6acc5.mp4?token=tEnCMSQ1nI1Rf-l_X2huZsLvK4L-QhBfOu9z7FpEKvMBs96lKpZtsTvQcihgm_PZhAt3E-cCnFu4KnMNidRKT4b9Tp1W09pQP8-YiJ6HTBmP5xV28Em6EbHZNyBiijNGBHwXntsDeD_WIu3mR07GfymE20dWYARB0kBOxvsnkx6jsZX9TDjYZy_hVGwiKt1jmApUgr_dTwILAmWWRYdQVU5ONbxfuYBsWl8MG13mt0ODrci3lZGjHwNPtimUaRKFS9UDwrfA_fJE_Wp94OmkiWNIL5GiPymSzzL7qe1tgyrzD_BhksV3tplaC5hBov9shCAulLWt8ObvHhOy4Cl3jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جیک سالیوان، مشاور امنیت ملی پیشین آمریکا: توافق هسته‌ای بسیار شبیه توافقی خواهد بود که اوباما، جان کری، وندی شرمن و افرادی مثل من سال‌ها پیش مذاکره کردند، اما ترامپ از آن خارج شد.
🔴
ما به چیزی شبیه آن بازخواهیم گشت، در حالی که همه این هزینه‌ها را پرداخته‌ایم، در حالی که اصلا نیازی به خروج از آن توافق در وهله اول نبود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/124843" target="_blank">📅 19:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124842">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
الجزیره: ۲۴ ساعت آینده برای «آتش‌بس» اسمی در لبنان حیاتی خواهد بود
🔴
به گفته منابع سیاسی در بیروت، این ۲۴ ساعت بسیار حیاتی خواهد بود و در عین حال، ممکن است بسیار خطرناک نیز باشد، با توجه به این واقعیت که مذاکرات در بیش از یک مکان در حال انجام است.
🔴
چیزی در واشنگتن و همچنین در قطر در جریان است و تلاش‌هایی برای رسیدن به یک آتش‌بس جامع در لبنان صورت می‌گیرد
🔴
آنچه در ساعات گذشته شاهد بوده‌ایم، تشدید تنش بوده است. حمله به یک خودرو در جاده اصلی بین جنوب و بیروت، بسیار نزدیک به بیروت، در منطقهٔ خلده، و پاسخ حزب‌الله با ارسال پهپاد و سپس موشک به سمت شهرک‌ها و شهرهای شمالی اسرائیل.
🔴
این ما را به نقطهٔ اول بازمی‌گرداند، جایی که قبلاً در آن بودیم؛ هیچ چیز واقعاً در حال تغییر نیست، بلکه فقط بر تشدید تنش افزوده می‌شود.
🔴
حملات به چندین شهر و منطقه، به‌ویژه هشدارها به ساکنان الخرایب، که در شمال رودخانه لیتانی قرار دارد، بر این واقعیت تأکید دارد که اسرائیل می‌خواهد مردم جنوب لبنان به سمت رودخانه زهرانی حرکت کنند، رودخانه‌ای موازی در فاصلهٔ حدود ۲۰ کیلومتری از پیرامون خطی که (اسرائیل) در گذشته تعیین کرده بود (که به اصطلاح منطقهٔ حائل مرزی خود را مشخص می‌کرد).
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/124842" target="_blank">📅 19:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124841">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
عراقچی: هرگونه اقدام خصمانه با پاسخی فوری و قاطع مواجه خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/124841" target="_blank">📅 19:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124840">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
نتانیاهو : با هم انجام دادیم، تو نزدیکی و همکاری‌ای که قبلاً هرگز نداشتیم
🔴
باید دوباره بگم، رئیس‌جمهور ترامپ بهترین دوست اسرائیل بوده که تا حالا داشتیم؛
🔴
هیچ‌وقت چنین دوستی تو کاخ سفید نداشتیم، او از همه جلو زده، و این شراکت خیلی قوی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/124840" target="_blank">📅 19:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124839">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
این فقط بخشی از جنایت حکومت در 18 و 19 دی هستش.
🔴
هرکدام از این جاویدنام ها عزیز یک خانواده هستن.
🤔
عرزشی حرام زاده از عدل علی بگو
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/124839" target="_blank">📅 19:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124838">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
فارس: تاریخ برگزاری آئین وداع، تشییع و خاکسپاری آیت الله خامنه ای اعلام شد
🔴
۲۰، ۲۱، ۲۲ خرداد/ وداع در حرم امام‌ خمینی
🔴
۲۳ خرداد/ تشییع در تهران
🔴
۲۴ خرداد/ تشییع در قم
🔴
۲۵ خرداد/ تشییع در عراق
🔴
۲۶ خرداد (اول محرم)/ تشییع و خاکسپاری در مشهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/124838" target="_blank">📅 19:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124837">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
نتانیاهو : نباید ایران تهدیدی برای اسرائیل، خاورمیانه و آمریکا نباشه؛
🔴
سلاح هسته‌ای نسازه و ابزار حمل اون رو هم نداشته باشه؛
🔴
نه فقط علیه اسرائیل یا پایتخت‌های اروپا، بلکه علیه شهرهای آمریکا هم
🔴
این هدف مشترک ماست، برای همین وارد این مسیر شدیم. همچنین می‌خوایم دایره صلح رو گسترش بدیم؛
🔴
همون‌طور که من و رئیس‌جمهور با هم در چارچوب توافق‌های ابراهیم انجام دادیم.
🔴
پس هدف مشترک داریم. گاهی هم، مثل هر خانواده‌ای، روی تاکتیک‌ها اختلاف‌نظر پیش میاد. اما همیشه راهی برای حلش پیدا می‌کنیم
🔴
ما به‌عنوان دوستان نزدیک این کار رو انجام می‌دیم؛ ممکنه صبح با هم اختلاف داشته باشیم، ولی عصر به یک اقدام مشترک برسیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/124837" target="_blank">📅 19:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124836">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
الجزیره به نقل از رئیس ستاد کل ارتش اسرائیل: آماده‌ایم فوراً به جنگ علیه ایران بازگردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/124836" target="_blank">📅 19:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124833">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cwl9fYIAKaJXf66nGY9qaXvQ_v4Qi62TmvcXylkBqlC9t2j3WFtKx7KkUcnhPIE7ITEBwVp9b6tkdV5bwASAkIIvW9TVxZu-qMgWxMLkn17AEcHh9vV550qLw4ifEU9FGtZuVR5kdopP_iwvibLKwFm0nR1lk1utrKRz39-IikvJ9wMfvHE7aD59nF_DFMyaeA85e8FBhsQ8tw9V6QmEEL16FBFMnQ2J3U7IU3Jddo0DsuGYRCWnyCuv7u1HvvCX_yy57tVt4PmOfH9BNkJqu2uh1eX2FztNcfrjkY8PFrx2C6pVHqf7vWVo_ZpxfzaIkEYJYfM1h_GycAaf298c6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dbV8Ur37-Fz0R64in0E-P376ShkCXeMLYfvfVcga3Eb41P2M2Z8aBqOg2fL7yodzi3Wfq8HkXIebK-OFn1IFEVqtSrzO44y9AVttvnc__b0kYc8OvoOM2YWDaW3W4fCvdqLBuNd3kIx2zEoWXCBeEhx9iwp_qlIbo91Bh-xOn_eiZWhNG69QrfYfAPsBvYv6UCbAJIRfzqvFKulQNc2ot0pXzuYaYa9_7AqazYwfLBCwWXdITp3KyiwNNKTZOxSy1XI4QqcUq-_yf0nNnafoGeLKL6v5P8nTboHGdFYen_W9e1dXmwBSzY0IpO_7FmTmMHDZoA--0NHRgbM2ANwppg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EEdDQRYJuFSaRg9GxB8--z_rc28YYLtellJxF5yFdyOf9iq7hfoV567cqpD2zIsA0YmfF3SiZMbnn6IbDpXHEIc_WA-IRZPnq1w5vYuLkq7CUieEmXKFDM8D153L6q33jNuQ5HHtO1PjRh2kb3b3k1YDH8-dUonjCCrv0TiJ1v0GdhSGQlZrzaKfxYGDICDP2B-xjQDlj3XfotzAmpWvuEC1-4ME0fYugCgFX5K0nkoLt8wm0f2FoZegSS8TaB7ImqbdAiDmNy9ko3m667y6wH1BzRbPmW2IVGzclcNAZfG0Rt3rI0tHz2AB3RP2iJ2aQxg2D5WFDD20JjXOAC7Q2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیل ساعاتی پیش مناطق «باریش»، «تولین»، «الطویری»، «صریفـا» و «الحنیه» در جنوب لبنان را هدف قرار دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/124833" target="_blank">📅 19:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124832">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
زلنسکی: من آمادهٔ مذاکرات مستقیم با پوتین برای پایان دادن به این جنگ هستم، نه اینکه در صف بمانم تا همهٔ درگیری‌های جهان تمام شود و بعد نوبت ما برسد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/124832" target="_blank">📅 19:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124831">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af1ca0ddb0.mp4?token=If74748DqvoFFQjdrFDziyQvZUev_uqn_MGqTWFi5WDyCehCrB5C0-fwZpUneeyX4OycDCQtjgT_GgrBvyX0q4ZT2rjLxM9fr59Ut1GuA45M_Vp194fxpp-0Jd8syfrMZgS363X9A6vK4CfnSbR8uH_EYjEL4QJ3Ri5xYfbPGE6FfNUH9NopLlxpDolnDdTLiFR4EStUyX2EmGXVd1mKWCEbRwkV9N_ezn_mV-DwMJwLN8BVKxirERAIKHYChxUkZTWvMjhNnQAaZBxOQ5ZtEPMO5hUWNJH758NVHaO92g-vaQ76d-R0bA7kb8nvuo_H8A9vvK_OC_5nIGnUXWdotA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af1ca0ddb0.mp4?token=If74748DqvoFFQjdrFDziyQvZUev_uqn_MGqTWFi5WDyCehCrB5C0-fwZpUneeyX4OycDCQtjgT_GgrBvyX0q4ZT2rjLxM9fr59Ut1GuA45M_Vp194fxpp-0Jd8syfrMZgS363X9A6vK4CfnSbR8uH_EYjEL4QJ3Ri5xYfbPGE6FfNUH9NopLlxpDolnDdTLiFR4EStUyX2EmGXVd1mKWCEbRwkV9N_ezn_mV-DwMJwLN8BVKxirERAIKHYChxUkZTWvMjhNnQAaZBxOQ5ZtEPMO5hUWNJH758NVHaO92g-vaQ76d-R0bA7kb8nvuo_H8A9vvK_OC_5nIGnUXWdotA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی:من هر روز برنامه سفر پوتین را دنبال نمی‌کنم.
🔴
ما فقط به حمله به اوکراین پاسخ می‌دهیم.
🔴
فکر می‌کنم حملات ما موجه است.
آنها باید بفهمند که اگر به استفاده از پهپادها و موشک‌ها علیه ما ادامه دهند، ما نیز همین کار را خواهیم کرد.
🔴
اما ما فقط به پالایشگاه‌های نفت یا اهداف نظامی موجه پاسخ می‌دهیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/124831" target="_blank">📅 19:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124830">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
نتانیاهو در مورد توافق هسته‌ای اوباما با ایران: ما به ایران یک ماه مهلت دادیم قبل از بازرسی‌ها. آن‌ها تمام مواد هسته‌ای را خارج کردند، تأسیسات هسته‌ای را تخلیه کردند و همه چیز را به جای دیگری منتقل کردند.
🔴
آیا فکر می‌کنید این یک رژیم بازرسی خوب است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/124830" target="_blank">📅 19:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124829">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cb62a290a.mp4?token=um_-RoLkbpXktt_76D-TEWezw9JH6H9AHBX7N_Rs81Yk0Z4WlGfiDu9FrylyzSvbPnQMNqjqqwc-9pcro3f3v8qSMA9t4th-3k7VZUNoNINNPf0ihX1UcBNcsr73_H-D3nFlFfaN4vek2ZjVjL_Zqu-2oedxKP5w2VfSuE8GfyDeAx-zEcTywgo_T1A3s4fB5ssozEMbpntKXt4w7MWZ-4G_C-jv8qWSQzqGAtDdJnBFug_lXBk2gUEBcaPxYazuVSXh5T3i1jfCXXJtl30ByhR3Z8NxAlXA_BxI45PHWcrkkSIJ2-KHDAPv41wp4sSWXFC31GZvrj42oPQGK8ZaEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cb62a290a.mp4?token=um_-RoLkbpXktt_76D-TEWezw9JH6H9AHBX7N_Rs81Yk0Z4WlGfiDu9FrylyzSvbPnQMNqjqqwc-9pcro3f3v8qSMA9t4th-3k7VZUNoNINNPf0ihX1UcBNcsr73_H-D3nFlFfaN4vek2ZjVjL_Zqu-2oedxKP5w2VfSuE8GfyDeAx-zEcTywgo_T1A3s4fB5ssozEMbpntKXt4w7MWZ-4G_C-jv8qWSQzqGAtDdJnBFug_lXBk2gUEBcaPxYazuVSXh5T3i1jfCXXJtl30ByhR3Z8NxAlXA_BxI45PHWcrkkSIJ2-KHDAPv41wp4sSWXFC31GZvrj42oPQGK8ZaEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تیم غیر ملی جمهوری اسلامی
🤔
شما هیچوقت از مردم نبودین و نیستین بی غیرت ها
@AloSport</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/124829" target="_blank">📅 19:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124828">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
مرکز فرماندهی مرکزی ایالات متحده می‌گوید نیروهای آمریکایی ۱۲۵ کشتی تجاری را بازگردانده و از ۱۳ آوریل، آغاز محاصره بنادر ایران، ۶ کشتی را متوقف کرده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/124828" target="_blank">📅 19:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124827">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9cdc097f8.mp4?token=tXDYkzVB-248CXSE_82HGLAQ9pOfhRlpQ1iaOafD6RWOL7PwMekfLm4yGvImvxlTBGiENTxCQySQTdlF0J4ju3yG8nDiWDkJJe-3MTLTWTWw1oCH_8n0HsUJ0_0MdqSjfXI4gKJUsysUEhLiE8PKPeuyGpK0hpeDslWOCMR7yHmPeIptfM5Ou3_f8lCOPhzYkyG2ZqReI5vMnT0MAeGkIrJaed8F1SM8zyMzy8uqWSmumDsGiS3t8aZOXpbHjG89do-IIDdDBJ8KkHOeX5yVA7eEsPfz73JLfWy1ANiq0GjDOQ2lR0Yjmi3DfguKYO6fh9vM5ctWxPl5CvPWWJL5aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9cdc097f8.mp4?token=tXDYkzVB-248CXSE_82HGLAQ9pOfhRlpQ1iaOafD6RWOL7PwMekfLm4yGvImvxlTBGiENTxCQySQTdlF0J4ju3yG8nDiWDkJJe-3MTLTWTWw1oCH_8n0HsUJ0_0MdqSjfXI4gKJUsysUEhLiE8PKPeuyGpK0hpeDslWOCMR7yHmPeIptfM5Ou3_f8lCOPhzYkyG2ZqReI5vMnT0MAeGkIrJaed8F1SM8zyMzy8uqWSmumDsGiS3t8aZOXpbHjG89do-IIDdDBJ8KkHOeX5yVA7eEsPfz73JLfWy1ANiq0GjDOQ2lR0Yjmi3DfguKYO6fh9vM5ctWxPl5CvPWWJL5aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت ایران اگه توافق ۲ روز دیگه ادامه داشته باشه:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/124827" target="_blank">📅 19:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124826">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
نتانیاهو: مردم در حال توسعه منابع جایگزین هستند و در حال حاضر در حال توسعه مسیرهای جایگزین هستند.
🔴
به جای تمام انرژی‌ای که از خلیج فارس عبور می‌کند، مسیرهای دیگری وجود خواهد داشت.
🔴
بنابراین به جای تمام انرژی‌ای که از خلیج فارس عبور می‌کند، همچنین از طریق عربستان سعودی به دریای سرخ عبور خواهد کرد. و فرصت‌های دیگری نیز وجود خواهد داشت. می‌توانیم آن‌ها را مستقیماً به مدیترانه ببریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/124826" target="_blank">📅 19:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124825">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
نتانیاهو: هدف و خواسته ما سرنگونی جمهوری اسلامی است اما به صرف انتخاب و خواست ما این اتفاق نمی افتد و ما تلاش داریم مردم ایران را کمک کنیم تا خودشان این کار را بکنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/124825" target="_blank">📅 18:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124824">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
✅
⭐️
فقط گیگی 8 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/124824" target="_blank">📅 18:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124823">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RF0nMvCnrs17db5wZgkNV1KZsveZAKSNP_6iMGhZy0u8hk7ia1v9ahUfX6yg46pD5i-ytUhlZ7nPWfsiAF_7icWVL46PMT7vkZIkvBoFJ8NOmCFZRRso2ai4SF3md5rW6sD5fBvumOaDfDdCaL2uWBUwuLaNmgm2cTLPI3UCtZ3HRfVPFxkKtn83nUALUzT8TtPTKc1jT3BVs6E491MXe3XoruQw8iJ74OLgZOPYxrh0APVI3WpV_Qtadcw7RUFUi5rt-8JqYpiHmsoaPqToqN-nqXGQjCqJxNHEa_Vry6hiHYde8182H1Ei65MafdtC-7hOHv4yI7-WztparQmL4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
✅
⭐️
فقط گیگی 8 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/alonews/124823" target="_blank">📅 18:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124822">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
سایت عبری والا: نتانیاهو از وارد شدن به جزئیات تماس تلفنی خود با ترامپ خودداری کرد، اما تأکید کرد که رئیس‌جمهور آمریکا بسیار پرسر و صدا بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/124822" target="_blank">📅 18:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124821">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
نتانیاهو: من هر دو روز یک‌بار با رئیس‌جمهور ترامپ صحبت می‌کنم.
🔴
به نظر من فاش کردن موضوع گفتگوهایمان برای ایران منطقی نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/124821" target="_blank">📅 18:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124820">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
نتانیاهو: آنچه می‌خواهم انجام دهم این است که در آمریکا — از کمک به شراکت فاصله بگیرم.
🔴
اسرائیل آماده است. نیروهای آمریکایی آماده‌اند. ایران با آتش بازی می‌کند
🔴
نتانیاهو درباره کمک‌های آمریکا:
دیگر به آن نیاز نداریم.
🔴
من از هر مقدار کمکی که آمریکا در طول سال‌ها به ما داده است قدردانی می‌کنم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/124820" target="_blank">📅 18:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124819">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
نتانیاهو در مورد ایران: مردم ایران خواهان دموکراسی، روابط خوب با آمریکا و روابط خوب با اسرائیل هستند.
🔴
این اتفاق می‌تواند بیفتد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/124819" target="_blank">📅 18:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124818">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7WFKInfjsS8YBMwHH6ZZjcSJDG_Erj8vQyPsjV8JN5ysO2I0oE1oniXPlTLsjliY1CgiKXsiK3kTg9OQ_kPwH8bDPZTa3LAgUJexfHMrFc8dPW-RInbUh68C6lPb7dh99kZcY2eKZHGynlz8_Dnukjhv4V-4dAYr_J7kAMUg4G5kn_rCp2-gu6S8fmignSdjYxus147z01vJORrKQxoy8HdYwoSJM46PdFO8TYi_9D1EGXbsRVQXq2f3R9UTwKlkRM1Zpa4zUsTNnnxX0A2xMXX359IkByEe95zZDOfhfrSIr8GJUnFb5ZviHTZbfIRcJta10Nj8D9-ek6GoLOPQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاور رئیس‌ امارات: حملات به بحرین و کویت، همه کشورهای خلیج فارس را هدف قرار داده است.
🔴
او گفت: «هیچ کشور حوزه خلیج فارس نباید به تنهایی در برابر تهدیدها قرار گیرد. امنیت کشورهای عربی خلیج فارس به یکدیگر گره خورده، منافع آنها مشترک است و سرنوشت واحدی دارند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/124818" target="_blank">📅 18:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124817">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
خبرنگار الجزیره: حملات هوایی اسرائیل شهرهای باریش، فرون، تولین و برج قلاویه در جنوب لبنان را هدف قرار داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/124817" target="_blank">📅 18:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124816">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
گزارش برخی کاربران: صرافی‌های خارجی در حال ایجاد محدودیت‌هایی مثل مسدودسازی دارایی و تعلیق برداشت برای کاربران ایرانی هستند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/124816" target="_blank">📅 18:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124815">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
سی‌ان‌بی‌سی: چرا نمی‌تواند آمریکا فقط تنگه هرمز را باز کند؟
🔴
نتانیاهو: خب، می‌توانید، اما به مالکان کشتی‌هایی نیاز دارید که ریسک مالی برخورد را بپذیرند. از نظر نظامی ممکن است، اما ساده نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/124815" target="_blank">📅 18:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124814">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
صدای انفجار در شمال اصفهان مربوط به مهمات عمل‌نکرده جنگ بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/124814" target="_blank">📅 18:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124813">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
مارکو روبیو، وزیر خارجه آمریکا: به عنوان بخشی از سیاست خارجی ما و به دلایل متعدد، به صورت علنی درباره این که آیا اسرائیل دارای سلاح هسته‌ای است یا خیر، صحبت نمی‌کنیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/124813" target="_blank">📅 18:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124812">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
نتانیاهو: ما تصمیم‌گیری در مورد اینکه آیا تشدید تنش ضروری است و آیا باز کردن تنگه هرمز از نظر نظامی امکان‌پذیر است را به ترامپ واگذار می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/124812" target="_blank">📅 18:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124811">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
نتانیاهو به سی‌ان‌بی‌سی: ترامپ در حال بررسی چندین گزینه است و ما هر دو روز یکبار با هم صحبت می‌کنیم
🔴
ایران هنوز با حذف مواد هسته‌ای موافقت نکرده است، اما فشارها رو به افزایش است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/124811" target="_blank">📅 18:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124810">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
هند: حملات ایران به کشور کویت که باعث کشته شدن یکی از اتباع ما شده است را محکوم می‌کنیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/124810" target="_blank">📅 18:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124809">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
روبیو، وزیر خارجه آمریکا: رهبرانی از لبنان و اسرائیل هم‌اکنون در ساختمان وزارت خارجه آمریکا برای مذاکره نشسته‌اند.
🔴
امیدواریم نشست امروز بین لبنان و اسرائیل به بیانیه و برنامه عملی برای یک مسیر امنیتی در لبنان منجر شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/124809" target="_blank">📅 18:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124808">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
روبیو: ترامپ به ایران اجازه نمی‌داد که یک سپر تسلیحات متعارف بسازد که بتواند پشت آن پنهان شود و برنامه هسته‌ای خود را توسعه دهد.
🔴
عملیات خشم حماسی به هدف خود که درهم شکستن دفاع سنتی ایران و کشاندن آن به پای میز مذاکره بود، دست یافت.
🔴
نیروی دریایی ایران اکنون در قعر دریا است، دیگر نیروی هوایی ندارد و قابلیت‌های موشکی و صنایع دفاعی آن تضعیف شده است.
🔴
سکوهای پرتاب موشک ایران آسیب قابل توجهی دیده‌اند که قابلیت‌های آنها را به شدت کاهش داده است.
🔴
ما امیدواریم که ایران جاه‌طلبی‌های هسته‌ای خود را کنار بگذارد و حمایت از تروریسم در سراسر جهان را متوقف کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/alonews/124808" target="_blank">📅 18:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124807">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
نتانیاهو: ترامپ معتقده که میتونه مشکل غنی‌سازی رو با مذاکرات حل کنه؛ من فکر میکنم باید بهش فرصت داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/124807" target="_blank">📅 18:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124806">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/544a3dbdda.mp4?token=C8ICe2MeYN6-BGp_IC0zfOyEYI3IFEatxPTiHyi0RmTCTFR_OAVkv09r-kc1X9xlLxQ8Z0MDGSpnGi3gaHC9Uu2KNjYuvxFJGxxn9yDRAOGAqPsHXOHFpcByYz04_ijm5Z0F_3MVApW3ix0lYAbVNmo8JKPF9YXlSApbPZK85xyQ800fJCKRnN21a95iYmbT5KZTS91NHMisaEyKF6F9qGMeOwTXvn9VydZJ5cFxxTDUk-8dwJuzyuUXyBXOcLb2GMhnxkeroe-y3W1dsURqgqy0UT4hBWD_NhD2bbrM3TZbsKKju61bOP02hs2JDNoy0c0PyuFkcFp_RqC5f3dqxHs5xsGfPWwhEBoovbiwVlWnbnTUP7YunzeWTwSIsmwn-nvuuEj9y88fgcYPIMGyTVq5ZjKsnWg2WNPRtda3RBuHEnf8E-jFuWokDuYTM3DGCrKYPcZYLykBGdZ5aP8ii4rWh44oP-1qGDpTaMjP9bf-OHPp-pgMZIx9MQx2TxYPA8GVQUxaQEK-I_rqwD96ZHxgf7VQLJjDngDBAZWF6w8HPjteuBApWuWSrI37t7HY8SusQaOAL0dxDyEc5utm579-p43K1XetmWeLQaAPoy42L34Uy_J6yUWzKKafLATX4RdKKRaKIjRiBMF5L3uFc-VuYWzeZLR88abWNCeN2XM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/544a3dbdda.mp4?token=C8ICe2MeYN6-BGp_IC0zfOyEYI3IFEatxPTiHyi0RmTCTFR_OAVkv09r-kc1X9xlLxQ8Z0MDGSpnGi3gaHC9Uu2KNjYuvxFJGxxn9yDRAOGAqPsHXOHFpcByYz04_ijm5Z0F_3MVApW3ix0lYAbVNmo8JKPF9YXlSApbPZK85xyQ800fJCKRnN21a95iYmbT5KZTS91NHMisaEyKF6F9qGMeOwTXvn9VydZJ5cFxxTDUk-8dwJuzyuUXyBXOcLb2GMhnxkeroe-y3W1dsURqgqy0UT4hBWD_NhD2bbrM3TZbsKKju61bOP02hs2JDNoy0c0PyuFkcFp_RqC5f3dqxHs5xsGfPWwhEBoovbiwVlWnbnTUP7YunzeWTwSIsmwn-nvuuEj9y88fgcYPIMGyTVq5ZjKsnWg2WNPRtda3RBuHEnf8E-jFuWokDuYTM3DGCrKYPcZYLykBGdZ5aP8ii4rWh44oP-1qGDpTaMjP9bf-OHPp-pgMZIx9MQx2TxYPA8GVQUxaQEK-I_rqwD96ZHxgf7VQLJjDngDBAZWF6w8HPjteuBApWuWSrI37t7HY8SusQaOAL0dxDyEc5utm579-p43K1XetmWeLQaAPoy42L34Uy_J6yUWzKKafLATX4RdKKRaKIjRiBMF5L3uFc-VuYWzeZLR88abWNCeN2XM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری: ترامپ شما را «دیوانه لعنتی» خطاب کرد.
🔴
نتانیاهو: گاهی اوقات، مانند بهترین خانواده‌ها، ما این اختلافات تاکتیکی را داریم. همیشه راهی برای حل آن‌ها پیدا می‌کنیم.
🔴
می‌توانیم صبح با هم اختلاف نظر داشته باشیم و تا بعدازظهر اقدام مشترکی انجام دهیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/124806" target="_blank">📅 17:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124805">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
نتانیاهو به CNBC: بسیاری از کسانی که اسرائیل را هدف قرار می دهند در بیروت هستند‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/124805" target="_blank">📅 17:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124804">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
نتانیاهو به سی‌ان‌بی‌سی: من با ترامپ در مورد مسائل مربوط به ایران موافقم و ما گاهی اوقات در مورد جنبه‌های تاکتیکی اختلاف نظر داریم، اما به راه‌حل‌هایی می‌رسیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/124804" target="_blank">📅 17:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124803">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQ_ZHHUhmPTizhg0SXrfQQUSAO2bPv2ncR21XtrEDh19ws5tGEOh0EaGkeR5ZrV8cjuIrVczR25tDY20_Liumzy2kTEloMVV_hsXCGHyn1AvXUq2Y6BXt7RarZyQirqFnF8V-iecnjN0H6Anj0elNILHjrgy7lrfSgMdsgtTrZhyrwhPIe-K-irEOeVvlXQFh1yGDyIvG2KU-MCuY-0VaJiogcA3N8r4gME-pDfwrXlh9dW27yeLqfchkrPxkDYRfu7QKIbXY4j0rI-cMiUg1kWXlrDwb5KODLDXML6zJx7xjd5m6jhg5jIRKAuRZHR48AvLzpGRlshk06BSvTkHRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بارگیری نفت همچنان در خارگ ادامه دارد
🔴
تانکرترکرز: یک نفتکش غول‌پیکر برای نخستین بار در ۴ هفته گذشته در حال بارگیری نفت در جزیره خارگ دیده شده؛ با وجود این نفتکش‌ها و مخازن خشکی، وضعیت ذخیره‌سازی این کشور در شرایط بحرانی نیست.
🔴
از آغاز محاصرۀ غیرقانونی آمریکا علیه بنادر ایران، ترامپ بارها گفته لوله‌های نفتی ایران از درون منفجر خواهند شد اما با گذشت بیش از ۵۰ روز هنوز هیچ اتفاقی رخ نداده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/124803" target="_blank">📅 17:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124802">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
امروز نماینده های مجلس طی نامه ای به مجتبی خامنه ای ازش خواستن برد موشک ها افزایش پیدا کنه تا بتونن دفتر ترامپ توی آمریکا رو بزنن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124802" target="_blank">📅 17:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124801">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
اسرائیل هیوم: واشنگتن از تهران خواسته است پیش از اعلام توافق، محل ذخیره اورانیوم غنی‌شده را روشن کند
🔴
واشنگتن به تهران اطلاع داده است که پیش از اطلاع از مکان اورانیوم غنی‌شده، محاصره و تحریم‌ها را لغو نخواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/124801" target="_blank">📅 17:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124800">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N24Qt-AT65jAqYWu7awjG4tGNzT_4U0-3npwoIgqBO-zDcWIlPs-MAKEQK7GpvTR6FEkJrysQ861FFUZGzBDeulGK51qsjWqe0zLry0GKfqU78QAXCOjDHAa0QnBDIlQqG62uLYNib4wzOdeju0LyYld7_w7CoqNsRmRGoXIT81TZ9YasuQnHipOTQfX0smcQd7Ntf0XYOtJlXCuuTjSbui4tDe7KG4oZd0vcwxNWUVgvp3Dj0aKSQue39Hj0kiwhYGyHEyqM1VybFEHhtuc7yTH8ArSQtHCHTEI36CwEBR80AL-Sn3TJCyjcmRhQlfJYtU6pHE-aQcXjpZZj7TLyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی‌بی‌اس: خلبان جنگنده F-15E آمریکایی که بر فراز ایران سرنگون شد، چند هفته پیش‌تر در آغاز جنگ نیز در یک حادثه آتش دوستانه بر فراز کویت سرنگون شده بود.
خلبان هر دو بار به‌درستی از هواپیما پرید، اما در سرنگونی بر فراز ایران دچار جراحات جدی شد.
عضو دوم خدمه پس از نزدیک به دو روز پنهان‌کاری نجات یافت. ژنرال دن کین، رئیس ستاد مشترک، از «استقامت و پایداری جنگی» آن‌ها ستایش کرد.
یک ژنرال بازنشسته نیروی هوایی این سرنگونی دوتایی را یک «همزمانی بسیار غیرمعمول» توصیف کرد که با دو بار زدن رعد و برق قابل مقایسه است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124800" target="_blank">📅 17:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124799">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
وزارت امور خارجه کویت:
کویت کاردار ایران را احضار کرد و دو دیپلمات ایرانی را به عنوان «عنصر نامطلوب» اعلام کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124799" target="_blank">📅 16:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124798">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
نخست‌وزیر عراق از تشکیل یک کمیته مشترک برای تدوین سازوکارهای قطع ارتباط با گروه الحشد الشعبی و انحصار سلاح در دست دولت خبر داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/124798" target="_blank">📅 16:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124797">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eu61sexEnxN37qvHKLh9ATGwxIc4Y2dcr1cCGYEKvjEZl6LuyQkow9hmB-IT-6COT9R8uKIxN-JQRtfYgjR_REi9ZjUbRoJYMP1nbDOaSQ1gGLY_Du_wT_XA_ooGoylpoERO_0Fd05Aj6R7AstrzfRXL2ZNAG56a0HEwnf5hvenkV0XoJlOrukGlK1DM50YKjYmNro5V14ICVvTsWm1hi85kD7btokGFG5KI9m9WrWRu0RYOjGpBHhrMVCuTL_wPRrfaXCYFlDWepgJlJ7HGXoDJMw_BbxUmcwma2IvIRid-M2m9fgBOVAmCT2fNbzqzVrurNXcsHJyKZDNdmGgwAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میمندیان، نویسنده پاورقی و دوست شهبازی:
به محمدرضا تجاوز گروهی نشده و تکذیب میکنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/124797" target="_blank">📅 16:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124796">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b12cb328d9.mp4?token=MqNceYfKmk62Q5saJ0OXgk3bKWpxkmqCrP3EC-v3K9w3I4DFUgcboPCsdzPJt-lyv1lk70ZmZgQHzHGHhTsqFEBNeCLqmle4F55StYrCC9OlWyvkWKf_DCFHVUu50dMH37Ls4cSHur1n2a-jxzoo0a2r9kuhFBNdc6P7lNf-VayH4eR4ifNUHwnRivKICGTdl4NUH26h4d5Zo5P-clS0ZaxudKf_BHNnuJcQl4Exn1XF4yTorAqFhtWH-WwWrEEx3dSPm7gb_YuoKe-KFaeOkLV6TI9dzZBxWd3cZ-gMqJ3nH7kceWv4GaFhQjBvvgP6CCjFFWTKGh_vr5fLS0KfDpCw40mPdxkf6yLJIt023dujghmPzs7hZde3jEtJe970rzw-gvSX7LXphOFrw6eOBZmOMYhGIlHaqT1UlMQe5gbALn2GreWruX2IJdn7SwCT_CphLBhoAWWzj8ABqVdWAwoX21ap04ZNYtTEjPd8njTRCPb62tA1d06oXH5xQMaYy5m7daeEJ_kHAaD4ePH-oveFxOiYHK1S1TBh_J6MlkPzX_XV-txTToO1DhegKyWSHiZo765DMMGLpbe9tVXefklmeJW62gA7eFBB7PwaYnSvK9-UTFaL7gOuOLs465Un5gOdswpsODepB2iqhI9uPoJQZTJtGlBRlXf6rLZpprs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b12cb328d9.mp4?token=MqNceYfKmk62Q5saJ0OXgk3bKWpxkmqCrP3EC-v3K9w3I4DFUgcboPCsdzPJt-lyv1lk70ZmZgQHzHGHhTsqFEBNeCLqmle4F55StYrCC9OlWyvkWKf_DCFHVUu50dMH37Ls4cSHur1n2a-jxzoo0a2r9kuhFBNdc6P7lNf-VayH4eR4ifNUHwnRivKICGTdl4NUH26h4d5Zo5P-clS0ZaxudKf_BHNnuJcQl4Exn1XF4yTorAqFhtWH-WwWrEEx3dSPm7gb_YuoKe-KFaeOkLV6TI9dzZBxWd3cZ-gMqJ3nH7kceWv4GaFhQjBvvgP6CCjFFWTKGh_vr5fLS0KfDpCw40mPdxkf6yLJIt023dujghmPzs7hZde3jEtJe970rzw-gvSX7LXphOFrw6eOBZmOMYhGIlHaqT1UlMQe5gbALn2GreWruX2IJdn7SwCT_CphLBhoAWWzj8ABqVdWAwoX21ap04ZNYtTEjPd8njTRCPb62tA1d06oXH5xQMaYy5m7daeEJ_kHAaD4ePH-oveFxOiYHK1S1TBh_J6MlkPzX_XV-txTToO1DhegKyWSHiZo765DMMGLpbe9tVXefklmeJW62gA7eFBB7PwaYnSvK9-UTFaL7gOuOLs465Un5gOdswpsODepB2iqhI9uPoJQZTJtGlBRlXf6rLZpprs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مصاحبه شاهکار این مرد وایرال شده؛خونش رو زدن و اومدن باهاش مصاحبه کنن
+ خبرنگار: شما که خونه نبودین.
_ نه ولی
کیرم
دهن اسرائیل.
+ خبرنگار عع این حرفا چیه آقا
_ خب الان چی بگم؟ بگم ببخشین آقای نیتینیاهو
کصکش
؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/124796" target="_blank">📅 16:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124795">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
جنبش النجباء عراق اعلام کرد در صورت دستور آیت‌الله سیستانی بلافاصله خلع سلاح خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/124795" target="_blank">📅 16:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124794">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
حملات هوایی مداوم و گسترده در سراسر جنوب لبنان در حال وقوع است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/124794" target="_blank">📅 16:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124793">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnU0rjZ7kFwP3RSNR1LGHC_PPZpX1XJ1Uw6X7gWeMbWyjQExQyw_1wTepGswqZHVif0a1Y1NGtnDlfYYuCShkHCpTnIvsxPU4YUBqneXG9ZP3jfGpCtuKNIadwZ11nIlnE3E1lxewlCN7yx_77DnVS0GibmblUUmzFNAFoRlYQtHS4ghuh03ZMxDBNBDJuqGHD9sVJaJQYVCsk54YySSHg9zmlcSJfGB5SuIisTrbdCgGveGV2vssJ44rqvsGkFJIZtVFHKZNEh-30G0PKOwQwaRrC3NT0YGEPEE4Jh88-SLzmeGDKmGaIeH3aoZIVzhq3mR6Sil3OMlMDS3NZXJzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جهش قیمت نفت همزمان با افزایش تنش‌ها در خلیج فارس
🔴
به گزارش وال‌استریت‌ژورنال، قیمت هر بشکه نفت به دلیل تنش‌های مداوم خاورمیانه افزایش یافته و هم‌اکنون به ٩۶ دلار رسیده است.
🔴
تنگه هرمز که بخش قابل توجهی از نفت جهان از آن عبور می‌کند، دوباره در معرض خطر بسته شدن قرار دارد و به همین دلیل، مذاکرات صلح آمریکا و ایران پیچیده به‌نظر می‌رسد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/124793" target="_blank">📅 16:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124792">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
کویت : دیشبِ ایران، ۱۳ تا موشک بالستیک و ۱۷ تا پهپاد سمت ما شلیک کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124792" target="_blank">📅 16:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124791">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGwXtsZQHXkxYGBkZAXEHsa1d76W4YAsswazsqGnxNhZQ4RxL4eWs5IGO_ZjfeMpWTcqW7igYnird54sPO3Cj6-LAhFypGhx-GIOGHJnBSauN0Q5FSLUbGvQ2O8cfZ8mPJ3jo-twf5yMnX1cQrC7blTBLgcNjwjbR1HRQMXO4NntqXInozjQoan8NVdHZN0NoN2vihB8YT385CWOIxi1vjTEdTXRaHLNG2AM3FEslS301MIuRKvO_RhJZhKcMTTHrmdO8WAXfDalGwXs1Rwx2BaB_7ZAD83iRpflw1ZqfS1lXGcsmrSdMuJWJlBcP44hauVyHwNlUNIDNwMbsEag2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124791" target="_blank">📅 15:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124790">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
ششمین سال خشکسالی در فلات مرکزی ایران؛ کم‌بارشی تهران ۳۹ درصد شد
🔴
مقام مسئول سازمان هواشناسی بااشاره به تداوم کم‌بارشی درفلات مرکزی گفت: تهران با ۳۹ درصد رکورددار کاهش بارش‌هاست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124790" target="_blank">📅 15:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124789">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9yz4a5GWXdLtKOO71lJiGEq1oQpkFoepgY8M292sWzuYdYZw3koLpUJoZjy0sfXUWKlqRip2ObEP_lzd9gY-0HItXyjHxihbwqrtWn4oEOMrIqrDF8tdll8Uphp_bw8_E14Nu0csvSL1V-_TXS7VdYegvxpd0INbuZ1t4cj46uunVwlXH1Tr0CMxrGlyq4ffUNCHSUcmAORwd9-5vBNIfWvniDKzJjXWUVBT4wjERVpL3vDMwJqnSTKclOjj3PotEa8Ro5KSR7lZPeAkHdqcGsr5qg5ZjnZ7FfHvfWKfIe4VE0FDT5WlFN6epHVRrv4uKKI9gnA9oxrZPapzN1Jqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمار وزارت دفاع کویت از تعداد پرتابه های ایران از شروع جنگ
🔴
۸۶۹ پهپاد
🔴
۳۷۲ موشک بالستیک
🔴
۱۵ موشک کروز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/124789" target="_blank">📅 15:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124788">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
نخستین جلسه قالیباف، نماینده ویژه ایران در امور چین با وزرای اقتصادی دولت
🔴
وزرای اقتصادی دولت به برخی نکات اساسی در مورد رفتار‌های اقتصادی چین در ایام جنگ و همچنین دوران بسته بودن تنگه هرمز اشاره کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124788" target="_blank">📅 15:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124787">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
ارتش کویت: ما ۱۳ موشک بالستیک  و ۱۷ پهپاد را شناسایی کردیم
🔴
یک مقیم هندی جان باخت و شماری از افراد زخمی شدند، همچنین خسارات مادی سنگینی وارد شده است.
🔴
به دلیل حملات، امروز ۵ بار آژیرهای خطر به صدا درآمده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124787" target="_blank">📅 15:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124785">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqoiK80nAFoAGrb2Sv6nyk_66A5H7i8fjRKvklTWghIgTLNQCMz3rPJ6Ns0FmE7Y8z79YKfrn3E9us2fuyKn96szTvmrxa6ZoC0Gf-bDPVo6V30lq7I52_FRKpWX0WdC58CN3yrAAD56vD_MLKeBNMF_3mb29Atykh_ALAubLlgvnTmx1eXrRNdT_HY0oilPJYu1X9VflxEl7GlO-p6UNHewqu83OebS5AGXJ4YUBKDJiGs3jYRZ6rmn6TMXJW9J_TYzs-nuXIou7zVHjbjoSgpGTBGzqB5VtXiDAodJDTgaWF5SVsEMq_eHeuayHPn8PmhIxNoFHUSksJmEIPe0Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61fbd0e8c6.mp4?token=EY9ZT4GGxCCP0BeLUyw3XFuEfY7EuhmSY8ihVPrkPEAkQOwcCA1Mo9NxOra_iyTFsnLEeE9un4rrTzF_SobZxkCLkH4zm6YLzziIgNGE1xkPB6MDZphd02r0IHztz9w9WdRpzK50lNkKv_lP82i-sgEI10Zkb_VuAfLb5n9fWMZZrXTef5pZm3lspJgzwIPJ6dY-5BY0QF7SlEV90fHd6hIVKJsnhOiUQkq5Ru5KxMkZJkH6dlvCnE75nltZCUId6PteKNiB5m6OYei0kD6rB6KCeuDYJ5PVvKhiw-ckkmoXws9DnQlkdf1qLYIsjifSUwUtI6ur_CTWdqOIpHos7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61fbd0e8c6.mp4?token=EY9ZT4GGxCCP0BeLUyw3XFuEfY7EuhmSY8ihVPrkPEAkQOwcCA1Mo9NxOra_iyTFsnLEeE9un4rrTzF_SobZxkCLkH4zm6YLzziIgNGE1xkPB6MDZphd02r0IHztz9w9WdRpzK50lNkKv_lP82i-sgEI10Zkb_VuAfLb5n9fWMZZrXTef5pZm3lspJgzwIPJ6dY-5BY0QF7SlEV90fHd6hIVKJsnhOiUQkq5Ru5KxMkZJkH6dlvCnE75nltZCUId6PteKNiB5m6OYei0kD6rB6KCeuDYJ5PVvKhiw-ckkmoXws9DnQlkdf1qLYIsjifSUwUtI6ur_CTWdqOIpHos7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای جدید، تخریب یک پناهگاه پهپاد/هواپیما واقع در مختصات ۲۹°۲۱'۰۴.۷۲"شمالی، ۴۷°۳۰'۱۴.۰۶"شرقی در پایگاه هوایی علی السالم در کویت را پس از حملات موشکی و پهپادی سپاه ( که به ادعای سنتکام همه رهگیری شد) که اوایل امروز این پایگاه را هدف قرار داد، تأیید می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/124785" target="_blank">📅 15:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124784">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
به گزارش وال‌استریت‌ژورنال، قیمت هر بشکه نفت به دلیل تنش‌های مداوم خاورمیانه افزایش یافته و هم‌اکنون به ٩۶ دلار رسیده است. تنگه هرمز که بخش قابل توجهی از نفت جهان از آن عبور می‌کند، دوباره در معرض خطر بسته شدن قرار دارد و به همین دلیل، مذاکرات صلح آمریکا و ایران پیچیده به‌نظر می‌رسد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124784" target="_blank">📅 15:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124783">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
✅
⭐️
فقط گیگی 8 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/alonews/124783" target="_blank">📅 15:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124782">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jxr6myGJD7ZBuhrAPvbxwvxrVyz0EywH6CGteVyqSqBu6mkVgK6U8XUrml_Kfih_FXV92VPdAE23ytoF-qmreTppnuHLQe4Wbw4BttXV2sXb_LVwjTIbL_g4w24ZTGeH76suo1CFTJjT0dS0DCVQlq5C_NPVEJ9HlrlEY3BeVpSk8rkQvHvrq0TLs7lkpei_a8qQL1dUewm2T6_vlcjfW5iyYFKHH46jegnuTmV8lUxRFYOO2ASoU7dBFEFtGbc0ZpqVn3dAiq6lmCJUqoHDDjmbCqD3uXT4hEHKMDhnoXWpvJq-bQF-pHLO2H7zxdlD0QdXhWNAWfDMFERq3jOcWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
✅
⭐️
فقط گیگی 8 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/alonews/124782" target="_blank">📅 15:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124781">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وزارت خزانه داری آمریکا: هر کسی که اطلاعاتی ارائه دهد که منجر به افشای یا مختل کردن یکی از منابع مالی سپاه پاسداران شود، جایزه مالی ۱۵ میلیون دلاری برای او در نظر می‌گیریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124781" target="_blank">📅 15:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124780">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">کی ب کیه
تو دنیایی ک ب ۳۳ کیلومتر میگن تنگ توام بگو بار اولمه
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124780" target="_blank">📅 15:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124779">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
جراحی زیبایی به قیمت جان؛ مرگ دختر جوان در پی عمل بینی
🔴
دختر جوانی که از یکی از شهرستان‌های غرب کشور برای انجام عمل زیبایی بینی به تهران آمده و در یکی از بیمارستان های خصوصی بستری شده بود، شب گذشته جانش را از دست داد.
🔴
اولیای این دختر جوان ۲۷ ساله از کادر درمان شکایت کردند.
🔴
به دستور  بازپرس شعبه پنجم دادسرای جنایی، این پرونده به دادسرای ویژه جرائم پزشکی ارسال شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124779" target="_blank">📅 15:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124778">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
تغییر ساعت فعالیت میادین میوه و تره‌بار پایتخت در روزهای ۱۴ و ۱۵ خرداد
🔴
فردا پنجشنبه ۱۴ خرداد ماه همزمان با رحلت جانگذار حضرت امام خمینی (ره) و عید سعید غدیر تمامی میادین و بازارها از ساعت ۸ صبح تا ۱۳ فعال  هستند.
🔴
روز جمعه ۱۵ خرداد ماه نیز مصادف با سالروز قیام پانزد خرداد نیز تمامی میادین و بازارها تعطیل هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/124778" target="_blank">📅 15:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124777">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/046f93f3b2.mp4?token=WltqcbHjlqKk6EEgO1-kvpZqSjNEYZbCcT4A5eSKArM9g-bqgXbqhHDsWQuSU-p05_glX6fntCtmaR3em4Lkyc8uH_H3MDTysrXZMXzhSo71VrKz4Oen0NXOdSAzkcLeFG-x6RlYJyyeWxv5kGWG93Wmgkr7mDskLpPgdfBVsSIrUKHI0GmbBNTUvB_ouGAFQH092gA2vyadIJmqnJEGfPSf0qpHxV507jYqXREy6UQdc8pAd1aEUafcOFiY-_eW2Ucwr9e7n9u894wWkllDTEr1Jh21IYrIUfjWlhhYAXc25komF2LzOY8scHVtI0pPPeAlNcF28Prhnt4Zz-KOmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/046f93f3b2.mp4?token=WltqcbHjlqKk6EEgO1-kvpZqSjNEYZbCcT4A5eSKArM9g-bqgXbqhHDsWQuSU-p05_glX6fntCtmaR3em4Lkyc8uH_H3MDTysrXZMXzhSo71VrKz4Oen0NXOdSAzkcLeFG-x6RlYJyyeWxv5kGWG93Wmgkr7mDskLpPgdfBVsSIrUKHI0GmbBNTUvB_ouGAFQH092gA2vyadIJmqnJEGfPSf0qpHxV507jYqXREy6UQdc8pAd1aEUafcOFiY-_eW2Ucwr9e7n9u894wWkllDTEr1Jh21IYrIUfjWlhhYAXc25komF2LzOY8scHVtI0pPPeAlNcF28Prhnt4Zz-KOmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل یه ماشین تو جنوب لبنان رو زد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124777" target="_blank">📅 15:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124776">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
تماس تلفنی بین وزرای خارجه قطر و عربستان سعودی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124776" target="_blank">📅 15:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124775">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3e001f7b2.mp4?token=mEGzlLVCCDZ0zHoh58GO0SYj7w6NreUzewTpbsU8R7o3KcFIb57XPaTe6CGHgOz0Vg-pDVfX1SWhAz54-Vr3hhPTGkBYR5V3F4Im9CjGFgCYD1C4EqWKdvY2G2JvUZkIjsiDPKkSNFXfLtjk2HRBz8H50QkXAoegsCbTCJOdUhVTET7O7TIDt-0E8oQeU_ESmrQToKxIo1K_WGI465lUD4WfqCyvNBMv4K4YZm81qAlOp35lT67rplzVI5cdpOnEZH-59vdHkjsh0PwOkDnESRKz0GHMbFsAM2rPWW07HvdwEKaLsHr9hF4a1InMkPHLILcP5C22bj-MBonoJG4PXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3e001f7b2.mp4?token=mEGzlLVCCDZ0zHoh58GO0SYj7w6NreUzewTpbsU8R7o3KcFIb57XPaTe6CGHgOz0Vg-pDVfX1SWhAz54-Vr3hhPTGkBYR5V3F4Im9CjGFgCYD1C4EqWKdvY2G2JvUZkIjsiDPKkSNFXfLtjk2HRBz8H50QkXAoegsCbTCJOdUhVTET7O7TIDt-0E8oQeU_ESmrQToKxIo1K_WGI465lUD4WfqCyvNBMv4K4YZm81qAlOp35lT67rplzVI5cdpOnEZH-59vdHkjsh0PwOkDnESRKz0GHMbFsAM2rPWW07HvdwEKaLsHr9hF4a1InMkPHLILcP5C22bj-MBonoJG4PXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
کسایی که تا دیروز به بهانه ناموس جنایت میکردن حالا بصورت عمومی جهاد نکاح راه انداختن!
🤔
شرم و حیا چیز خوبیه که در وجود حرام زاده های عرزشی نیست که بصورت علنی ناموس همدیگه رو دست به دست میکنین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/124775" target="_blank">📅 15:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124772">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qqOlmLLY9MHyKyehzt-tI_5OszvF3h1UTHtkKsLms4sJzlpOMbv-C8MluPv65dfV0dqcIrOy09ic7MpDpNsr-UeSl58_RG-_qSzqlEpiujBxY1PQS7Ho4DgeapQcWnAAiU9J85uAVbpir38cT8L9nLnJpTLiEakq_7-ahw9tbLV9eIRnK3viBPZXpku03wN1ZNQdr_8112mI_LpUh5ehCy4YWM4uSLzeUPmJBX-IwBM8wjHZStRbie-4TEHzmP8xwSIUDZjZDIecJ6Qrp7QVXnlKG_Crz27XrU_Iamh1hfEaOI4iWQclp7asXrU8eIYktitjFEW9_ZuBP0lh-54hog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BY64PcATaQGUS8tnhhTPwnfZtZlOmtII4b4WKl6Gi7ykrI577fp-ZiiZ7zibciPrxk_Pg7m4DuKgCZPm70SoVgoIK3GNzQArsmXjAR3rxxcJExt_sWX6L4zTx7gtaqLVLoivJusV4lArvbQPDjhAn9wnO0bUPFINEcRytZXK6Ox1IEypJC6dr1eE0G_cPuaiCL-M6jVY3cX4Vu8j9mPXnf0-GEvBRLrTCIvTb4x5S48TgGkcIw-ZDyzqJgtpmkhs4FNLANXgCyr0oT10S6tAAlrL99bK_6-LyOHdD85pBiByn--bJJCKMDpC5spGGXl6PGoLUK7GwooQD5eYZ_Ki3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A_p3GmohvbhuXcrmO5Jl1Bl-qSLCh6dJQN1IG9ip9T4L9XkGAHNMZOWsGoq7ntDlxGolNehbCtem7DCYA9WxbXjPs9VVGdCuDsg_VjvAEN7wrSlgIlv3SKgJxEe7AI5vHX-CsWw-jAadaIDv3cayLdU-cHI6RjXc7F9t1efQlH5PNHyMkBjFwn5jJUrJeFuZhxOaBmUJMcN4A4dQ39ZU8GywafjnOLSrT18Tq3ddMmuyX-wZrWlgHOx-n5OeenxG_es5ic_laJfRIjVHPf02aY5IiaTaI-K7_FoBTKLcdMbvVp8DWS6K4ecX29YId8XdL0BtWzkmy5idJYfVgyGwgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هم‌اکنون حملات ارتش اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/124772" target="_blank">📅 15:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124771">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRsdoijQHPzeTa1aj4luFAUgQKKgYy9xw-hSi1vciBXN_JEp7xw62K57gb_nSKn_rbcZXkivyylpNh8VrkA19HVC5Yip6rgApzQ9q-BKIpflP8yZHlKdQMYy7lq6KRBQTEKYJdcPPg5itqWVNQs_3W1A3lk9dEdJePMK8rZRkVuduNP7mT_r3wpwY0GOPYjI63qVkPTvtqI3MXQV0hrQl8MleujB7H-5Uq4az1l3VW95tzSSzl9u3qlhRjKO-23WwxrcWXYSzPHzSmtROgZW8xJMBP0SGfgtfqhgxC2bI9Xu_DuqpRpWO5rrq4G0yFwAtxaW-EUoq0yH966JoV8b9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واحد سگ‌های اوکتز ارتش اسرائیل برنامه آزمایشی‌ای را برای آموزش سگ‌ها به منظور شناسایی و هشدار درباره پهپادهای FPV حزب‌الله از طریق صدا راه‌اندازی کرده است، که هشدارهای زودهنگام به سربازان، به‌ویژه در شب یا شرایط دید کم، ارائه می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124771" target="_blank">📅 15:23 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

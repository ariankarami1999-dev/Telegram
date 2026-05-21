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
<img src="https://cdn4.telesco.pe/file/sXLZOdC1sNLnBR_lL_MLHgn1dUpBEAqkzN77Y9uYEA1EtegLQ7iijhLRgjZftVLRTwcjsrOX4tjVO959EQfaiWUtXLOvCTL2ZNLQYncm9zFYYmxdfECGzQHJvpk-cX5AW7ywRJaHw83VQTnD1gq0XgRvZJoPZ3HYFOzUOt6Sa0VAJwvJ1pFL1y3e9NE5aq_j9VV7vDBdgYIMRbNb1pWMir9nGqSOoD9S-1--k2lb233iea4so2uuEZrtB08vBZTOf-UnVxXiF29GVfsaQxkMxcbKtg40Vi0Rmta4__Fq8fIFeLXoghsBwwoGua-4Yt4VLr4KdQeTeF397qnW-Y6ohg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 165K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 00:16:57</div>
<hr>

<div class="tg-post" id="msg-75519">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">امروز سالگرد درگذشت اسطوره بی بدیل فوتبال ایران، ناصر حجازی هست
شخصی که نبودش بیشتر از هر زمان دیگه ای حس میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 724 · <a href="https://t.me/funhiphop/75519" target="_blank">📅 00:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75518">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">باز خداروشکر ایران اینترنشنال هست، دو دقیقه میبینم قیمت کل محصولات بهداشتی و غذایی میاد دستم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/funhiphop/75518" target="_blank">📅 00:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75517">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">عاصم منیر که امروز نیومد تهران (العربیه گفت سفرش رو یهویی لغو کرده) نکنه تو این مدتی که نبودم توافق شده من هنوز داغم نمی‌فهمم؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/funhiphop/75517" target="_blank">📅 23:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75515">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">النصر قهرمان لیگ عربستان شد.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/funhiphop/75515" target="_blank">📅 23:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75514">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">العریبه به نقل از منابع به‌شدت معتبر:
عاصم منیر، فرمانده ارتش پاکستان احتمالا فردا به ایران سفر خواهد کرد.
اگر عاصم منیر به ایران سفر نکند به این معنی خواهد بود که متن نهایی توافق ظرف چند ساعت دیگر اعلام خواهد شد.</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/funhiphop/75514" target="_blank">📅 23:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75512">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">البته بیشتر شبیه گل عالیشاه به استقلال بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/funhiphop/75512" target="_blank">📅 23:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75511">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">این گل رونالدو منو یاد گل کروس به سوئد انداخت
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/funhiphop/75511" target="_blank">📅 22:59 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75510">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">رونالدوی مادرقهبه برو دیگه</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/funhiphop/75510" target="_blank">📅 22:56 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75509">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">جان جدتون یه کانفیگی یه راهی یه کصشری چیزی برای دوتا۲ استیم پیدا کنید هرچی میزنم پینگش بالاس
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/funhiphop/75509" target="_blank">📅 22:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75508">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">از فصل بعد تو لالیگا به هوش مصنوعی قراره نقش تو داوری بازیا بدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/funhiphop/75508" target="_blank">📅 22:41 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75507">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🛍
تخفیف ویژه تا پایان امشب
🛍
دوباره تخفیفمون رو تمدید کردیم
😍
هر گیگ فقط 149 هزار تومن
‼️
✅
پینگ عالی و پایدار
✅
بدون ضریب و محدودیت کاربر
✅
لینک ساب برای مدیریت حجم
✅
پشتیبانی ۲۴ ساعته روی همه سرورها   200 گیگ شارژ شد
⭐️
تا تموم نشده به ادمین پیام بده…</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/funhiphop/75507" target="_blank">📅 22:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75506">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🛍
تخفیف ویژه تا پایان امشب
🛍
دوباره تخفیفمون رو تمدید کردیم
😍
هر گیگ فقط 149 هزار تومن
‼️
✅
پینگ عالی و پایدار
✅
بدون ضریب و محدودیت کاربر
✅
لینک ساب برای مدیریت حجم
✅
پشتیبانی ۲۴ ساعته روی همه سرورها
200 گیگ شارژ شد
⭐️
تا تموم نشده به ادمین پیام بده
🔗
کانال مشتریان
🔗
خرید</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/funhiphop/75506" target="_blank">📅 22:21 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75505">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7vC1qoLULt7X_ZREt7r6qSf_sAC4I1uJmXKG3E0mieF3QeFYPTn881IABIdifK7T0h8Hz3zhP0wgGqBVNIQkzn75q-Yid7X6pgXhLXA1eXDdJWCeni_DwGWxl52BPrJVaquJpm5z1tMPiMcLWiO6enZVREKOTOGNwMWAZJkovuG6ZR7Ke0HnuKn55vFPypHrvaqVBBdW8v3MA1Rd_VhNQfQCurUnHCwH0jcl10bL0lw9V3d8CllJPqNCWmYqofXlxoDpxrBpDeqwIAKySmaDOIS8T72otXmnMfQdbj5v5Frq7ShcPHhqtIO_MBQfNqRrRsQ-BQc_CNSPzAE6M2kWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایی دیگه کیر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/funhiphop/75505" target="_blank">📅 22:05 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75501">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دبی با 49 ثانیه قطعی برق در طول یک سال،کمترین میزان قطعی برق در سطح جهان رو ثبت کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/funhiphop/75501" target="_blank">📅 21:35 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75500">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">آقایون وسط باز یکم جو خوابید باز شروع کردن به گله از گرونی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/funhiphop/75500" target="_blank">📅 21:05 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75498">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb792999a1.mp4?token=c0ffVcedJiBT3smf-7xKlT_Ah3QGn002mXz2Rn7u-RTKFT6Nt_hkAbFWuTx-rNYvPK7QcksdkmsArwBr1vmZUvURymwHkNZqYBB8zkLMzTziUNmptHXC1cbw7TCWbt0R7tzcsTS1_tPKNEL0tAzGdXkcAzRtVSHrw428Ygk0TwsXKBNNuVYrgiWczGuLbe8mbLQcgdXu-oDXHyhoukoqOCqazh3D1OyiudT1uLvGSONFfJ_NKEqO_LhOpEaRK2tkUckkdtDK2s69TJHvQi4ukS0SnZ-mifzof8dL2utovq_Ehz0j_yj8H3FWCHSfM4VKuqc4hREtlfpe_kAELcHexQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb792999a1.mp4?token=c0ffVcedJiBT3smf-7xKlT_Ah3QGn002mXz2Rn7u-RTKFT6Nt_hkAbFWuTx-rNYvPK7QcksdkmsArwBr1vmZUvURymwHkNZqYBB8zkLMzTziUNmptHXC1cbw7TCWbt0R7tzcsTS1_tPKNEL0tAzGdXkcAzRtVSHrw428Ygk0TwsXKBNNuVYrgiWczGuLbe8mbLQcgdXu-oDXHyhoukoqOCqazh3D1OyiudT1uLvGSONFfJ_NKEqO_LhOpEaRK2tkUckkdtDK2s69TJHvQi4ukS0SnZ-mifzof8dL2utovq_Ehz0j_yj8H3FWCHSfM4VKuqc4hREtlfpe_kAELcHexQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/funhiphop/75498" target="_blank">📅 20:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75497">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ای کیروم به ننت ترامپ خستم کردی</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/funhiphop/75497" target="_blank">📅 20:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75496">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بچه ها اگه کانفیگ میخوایید تهیه کنید میتونید از ایشون تهیه کنید، ۲۰ روزی هست باهاشون کار میکنیم کارشون درسته
قیمت: گیگی ۱۹۹(بعضی مواقع تخفیف میزاره تا ۱۴۰ تومن میاد پایین)
@TornadoAdmin
| خرید
@Tornado_Ping
| فروشگاه</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/funhiphop/75496" target="_blank">📅 20:30 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75495">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">😠
کله زرد بنگاهی
ما نمیخوایم تنگه هرمز عوارضی بشه
کنترل تنگه هرمز (محاصره) کامل در اختیار داریم
نود و هشت درصد توان موشکی ایران و از بین بردیم
ایران نمیتونه اورانیوم غنای بالا رو نگه داره و اگه بهش دست پیدا کنیم احتمالا همشو نابود میکنیم و ما این اورانیومارو نمیخوایم
درگیری با ایران به زوری به پایان خواهد رسید
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/funhiphop/75495" target="_blank">📅 20:05 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75494">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDKfK22qFYw7yts04fcWPniSwTe31LTWScadDgDHj2zaahi13oxm8-IWrjWqZ_awXgk16SKpaThoSH-LP8beyix3y_2k5SEA31NhhJ_YbJli2pfiVk3IYCd9naRmUWUUIBsc3jfeNadONvItPrHrz5S0SJBFfdCWcYY5s_T9-x0k7MEDipf8jewIHK1YHHUENRPK-VPQ3qCMwjGM6WThfOWTEuqBSXl9T-pAIZxqD6Uvnwwi51BPpowEEUIjtrsIq2fgsjyLj5B0Jqcn40T6dnmw5QgyD7qNw9zuNHpUNBCU-TiOlvJ-Ytr59cVjR8ogj_0rAzO5YHOYZ__YuXSsNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔜
فایننشال جوس
مارکو روبیو، وزیر خارجه آمریکا، گفته اگر در تنگه هرمز سیستم دریافت عوارض برای عبور کشتی‌ها اجرا شود، رسیدن به توافق دیپلماتیک
تقریباً
غیرممکن خواهد شد.
😶‍🌫️
این حرف بعد از خبری مطرح شد که گفته بود
ایران و عمان
درباره
دائمی
شدن
عوارض
عبور از
تنگه
هرمز
در حال
مذاکره
هستند.
👻
یعنی آمریکا این اقدام را
تنش‌زا
می‌داند و معتقد است می‌تواند مذاکرات سیاسی و توافقات منطقه‌ای را سخت‌تر کند.
👍
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/funhiphop/75494" target="_blank">📅 19:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75493">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">امشب النصر قهرمان میشه؟
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/funhiphop/75493" target="_blank">📅 18:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75492">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دلم میسوزه برات ناموسا، کاش میشد یکم عقل تو کلت کاشت.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/funhiphop/75492" target="_blank">📅 18:10 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75491">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjQhZRdYnDw-iTwg6aSRu-mqQ9DwZONUTRJmAX26CS_TNdzfzY_NeR70YVLhV24V4tmCS_igS_5BsjutS6a5IrUl8deMmfdRT2fOsVXa_eDwEkOPVrS-oEnnOspfIvaKD1JHoInXRLyFoa1cxjSc4Kcytp9Yqm8QHh_t3Y8eUKXsZaPmNr9M-d7-zVUWOYYKsWgT6-h4RvOwVQBaiiwix5AWX05Nqbya5hj9tdemolF9OuWesv80kANIb4pfJXI7uYr5xWMg3iSN_D3QK2bsbipCFcDuYQ0FKL7KStBrzXGwocubJsDZE02BOfwpH84kh9xRfRxWZDVMzvHl9Vkz-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلم میسوزه برات ناموسا، کاش میشد یکم عقل تو کلت کاشت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/funhiphop/75491" target="_blank">📅 18:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75490">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">📶
بهترین ارائه دهنده فیلترشکن
🤝
آیپی static (ثابت) ، مناسب ترید و وبگردی (اینستاگرام - یوتیوب و....)
🔥
| بالاترین سرعت ممکن روی تمامی اپراتور ها
✅
تعرفه سرویس ها زمان دار :
🥑
1 گیگ | 4  روزه ⇐ 290 تومان
😼
3 گیگ | 9 روزه ⇐ 850 تومان
🛍
5 گیگ | 14 روزه…</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/funhiphop/75490" target="_blank">📅 17:54 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75488">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فاکس نیوز
طبق نظر سنجی 60 درصد آمریکایی ها با اقدام نظامی علیه تهران مخالف هستند.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/funhiphop/75488" target="_blank">📅 17:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75486">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tvLfik2Peeo-clqEBVguUV8lxkylZW3v1Hn-8qBvk3ET732H4VWqUF4zk8rE8ZlBDOUaNYCGfH2eHn43n31EY59VGelqEpcpk02KlV_EaCrTnDUSC3FLyxFuT5xfMkWrnJQpZ42IZJr4DqLPfJcrK58fu-GGTjp85qE-rSK3urap1meAdc-g6PARJE5POi4IHLmQA61MhaBEyKF6JurCU5s2vezdF5yglcso8Y7XJppaOOjWQn8-VzkIbVQDwpUVmhErw79IH2IH_By7QcF4vPjwmcTlvit2s3qdf_kPg4pD0s40_nxW4GObHOiR2Zo4a9a9OhtnzCkyRoHb1KKUnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e5fHo3LWlBe1gvJXekONsGu3WRkHmQBimxjh0PZFEfcNAuPLP8c8XBnXGyf7MLo2p-WNip6i1CqzGElSBU2czAvu-OtQXDaKgnxEP9dvFiNKSrc1Ct9zNAZil5rkPoOhfgLHabosASsghx18PMRS2wjrb4N2M1PioMMbAiJIGbxfgZ_86LEYL7ueIHCaBsIcp2qCppH0_9NXbJ8BVKxzDPRElbpH8BP7SJwuqYTxmZDiQtRtVzTEJdl7JvMbNqYP75taFzFChYrZJQKr-W4aeedwMB3C2kw_dvpIN7DxyuhGKQSgNp5aXyNkAwYBObIcE_asbmqd3e5oNsi9wG4eRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همون همیشگی دوستان اشتباه شد دارن میزنن هنوز  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/funhiphop/75486" target="_blank">📅 16:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75485">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">هیچوقت نفهمیدم چرا رپرا وقتی تو ایران میمونن کم کم بنجل و گنده گوز میشن
وقتی از ایران میرن کم کم دچار زوال عقل و بحران هویت میشن
چرا بالانسو رعایت نمیکنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/funhiphop/75485" target="_blank">📅 16:21 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75484">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ:
ما داریم با آدمای خوبی در ایران مذاکره میکنیم/مذاکرات داره خوب پیش میره/اونا با عقل شدن
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/funhiphop/75484" target="_blank">📅 15:08 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75483">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">حالا ترامپ کصکش باز میاد میگه مذاکرات مثبت بوده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/funhiphop/75483" target="_blank">📅 14:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75482">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رویترز:
مجتبی خامنه ای دستور داده که اورانیوم غنی شده در ایران بماند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/funhiphop/75482" target="_blank">📅 14:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75481">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">به پیر به پیغمبر من خشخاش نکاشتم، دست از سرم بردارید
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/funhiphop/75481" target="_blank">📅 12:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75480">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJDX0JqzQlyifJHclVV7g4W0ZoGc0N8P3X1g5CKPVcCeo9Uc8ApSpGMeciY_d8HQ16XaZnwLMp5EyELYRS4v8JgBQH92moKlyRE2-aSbEh4vcx-ZiURK9QshK9mTVldDla5u7lPB9Y_AniMt1tuUAB2siP61s_77VlEZHxM3AXnAujrpbNuCJM6d1U82sY7uB9eRnN_J9xfPj-jM3Z1MeqrzswzhLHiSVa9F7mHi1iUB1psJ2MkQ7DbJjfk40eAv5SQ1a0qVmy8D02TP4-2r-1KRURXOYDNdSk3BHsZgi6XHUpnGMZ7448RG6puzuz4hetOwIIS0W1oxCJ3l8Wq1Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید سردار آزمون
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/funhiphop/75480" target="_blank">📅 12:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75479">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ویناک رپر سیاسی شد رفت
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/funhiphop/75479" target="_blank">📅 12:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75478">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">حواستون به قحطی نون هست که خیلی چراغ خاموش داره میره تو کونمون؟</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/funhiphop/75478" target="_blank">📅 11:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75477">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">واقعا چطوری ملت میتونن طرفدار پهلوی باشن من  الان داشتم با بابا بزرگم حرف میزدم میگفت اونزمان ملت حتی نمیتونستن یه جومونگ ساده ببینن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/funhiphop/75477" target="_blank">📅 10:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75476">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec7c8d7ea8.mp4?token=ktU5PsbvYfMMGS9e-RcKKEgRn8ShIYXg9Fy8-pMAMmUM6mLr8mEbWcHluEm14VCzDUqMzUR-lHkELx00BhYbMeBltmOJ2Li7m0zZ4HBQe0iNMnuRLE0jvufk4wHbdFvYy_9y0xKw0k53GVHdrAdqTBIU9ECuOczJ51qrmCl5HLhfrAjDq1cZzKgvOgREDJiJ8lADhp66LASINcVSuMdm1xhuYFjntWGVR3JN6oAi4E353nz66Ut42tZ472MdGIsswzttx1j-JY38o6D_qUx7MSS7zZsphbep6YrDhcqCosel5gy3MDUfwPmxOYfT8z3X_ITRGcMGqNUA-G-tZOqN3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec7c8d7ea8.mp4?token=ktU5PsbvYfMMGS9e-RcKKEgRn8ShIYXg9Fy8-pMAMmUM6mLr8mEbWcHluEm14VCzDUqMzUR-lHkELx00BhYbMeBltmOJ2Li7m0zZ4HBQe0iNMnuRLE0jvufk4wHbdFvYy_9y0xKw0k53GVHdrAdqTBIU9ECuOczJ51qrmCl5HLhfrAjDq1cZzKgvOgREDJiJ8lADhp66LASINcVSuMdm1xhuYFjntWGVR3JN6oAi4E353nz66Ut42tZ472MdGIsswzttx1j-JY38o6D_qUx7MSS7zZsphbep6YrDhcqCosel5gy3MDUfwPmxOYfT8z3X_ITRGcMGqNUA-G-tZOqN3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحاتی مختصر درباره برنامه هایی که رو گوشیتون نصب میکنید
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/funhiphop/75476" target="_blank">📅 09:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75475">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">از اتفاقا دی حدود ۱۳۰ روز گذشته و تو این مدت بیشتر از ۹۰ روزش رو انتظار کشیدیم
ایوب هم بود روانی میشد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/funhiphop/75475" target="_blank">📅 09:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75473">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">😑
رویترز
کشتی‌های متحدان ایران مانند
روسیه
و
چین
اولویت عبور از تنگه هرمز را دارند.
😅
برخی کشتی‌ها برای عبور امن بالای ۱۵۰ هزار دلار
هزینه امنیتی
می‌پردازند.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/75473" target="_blank">📅 00:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75470">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">معاون فرمانده نیروی دریایی سپاه پاسداران انقلاب اسلامی:
دست ما روی ماشه است و
اگر ترامپ فکر می‌کند می‌تواند تنگه هرمز را با زور و کشتی‌ها باز کند، باید بداند همان نیروی دریایی که ادعا کردید نابود شده، شما را در کف دریا غرق خواهد کرد.
دشمنان ما باید بدانند که کاملاً اشتباه می‌کنند اگر فکر کنند این ملت با تخریب زیرساخت‌هایش عقب‌نشینی خواهد کرد، این ملت در طول ۴۷ سال ثابت کرده است که ممکن است تخریب شود اما تسلیم نمی‌شود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/75470" target="_blank">📅 23:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75469">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بچه ها اگه کانفیگ میخوایید تهیه کنید میتونید از ایشون تهیه کنید، ۲۰ روزی هست باهاشون کار میکنیم کارشون درسته
قیمت: گیگی ۱۹۹
@TornadoAdmin
| خرید
@Tornado_Ping
| فروشگاه</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/funhiphop/75469" target="_blank">📅 23:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75468">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">با اینکه نداریم سیم‌کارت سفید میشناسنمون تو ایست بازرسی</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/funhiphop/75468" target="_blank">📅 23:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75467">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">خبرنگار :
پیامت به خانواده‌های آمریکایی که از هوش مصنوعی می‌ترسن چیه اونا نگرانن بچه‌هاشون تو آینده کار نداشته باشن
ترامپ :
هوش مصنوعی فوق‌العاده‌ست ایران نباید سلاح هسته‌ای داشته باشه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/funhiphop/75467" target="_blank">📅 23:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75466">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مایکل بی، کارگردان آمریکایی، درحال ساخت فیلمی بر اساس مأموریت نجات دو خلبان آمریکایی پس از سقوط جنگنده‌ی ارتش آمریکا درجریان جنگ با ایرانه؛ تمرکز این فیلم برروی عملیات گسترده‌ای که تو پشت خطوط دشمن در کوه‌های زاگرس در غرب ایران صورت گرفت، خواهد بود و بر اساس کتابی آینده از میچل زاکوف ساخته می‌شه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/funhiphop/75466" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75465">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2221a06fe7.mp4?token=CvyYzJEZOjcvbxr2a8th-jBKuAQeK06lSjucwa0GFpoJn51liolxhQRK-oiZ1Y-lwEzNxPyRzWPido9pSQvEJKGsk5Z_nE7h41rtMmPwMN84wyOofzyQ_o0zUTJmPAPhKpgYGmaJpqZiVPz1I-grnZ5hsV6SV1iXBnWCxWQJu711jLzMtuoTfft09EMrUiBd-HOi1estkJFImJVVxVIusMrYY2CErn0YPueman8_nBvi1BzECQYgp-A8f6fVzco9Q8aMvyzs2syUey_9nrJAOgMDwPaVFjWFsJVGF1opI0RC3b93tprc3CswvWtHjct8es0-QddkGF6m67ZJXJ2laQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2221a06fe7.mp4?token=CvyYzJEZOjcvbxr2a8th-jBKuAQeK06lSjucwa0GFpoJn51liolxhQRK-oiZ1Y-lwEzNxPyRzWPido9pSQvEJKGsk5Z_nE7h41rtMmPwMN84wyOofzyQ_o0zUTJmPAPhKpgYGmaJpqZiVPz1I-grnZ5hsV6SV1iXBnWCxWQJu711jLzMtuoTfft09EMrUiBd-HOi1estkJFImJVVxVIusMrYY2CErn0YPueman8_nBvi1BzECQYgp-A8f6fVzco9Q8aMvyzs2syUey_9nrJAOgMDwPaVFjWFsJVGF1opI0RC3b93tprc3CswvWtHjct8es0-QddkGF6m67ZJXJ2laQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
اگر پاسخ‌های درست را دریافت نکنیم، اوضاع خیلی سریع پیش می‌رود. همه ما آماده‌ایم. باید پاسخ‌های درست را بگیریم.
باید پاسخ‌های ایران کاملاً ۱۰۰٪ درست باشند، و اگر اینطور شود، زمان، انرژی و جان‌های زیادی را نجات می‌دهیم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/funhiphop/75465" target="_blank">📅 22:36 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75464">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace87a5520.mp4?token=IM1K8P16DzQ98vo1JEVWe1HEbTtDZYOPwKY4QuteT8RX9DvjGQM3dqC0AxbCWOgz5ClPlr4d9G4Bs3fzmtyWRh2BEN7lI6i5viPyU7hTz5C-e3-7tDqUax2dEzCdHigM4QiWj9qRN8xLQeKWOsoUvCAlOebUGzWCoRsriS7emtnrWNL4i4Cpk41KdG38a65lSuhqeMRpYhibM9cYyG-421uCwJd79FtAG3JzEhl5342CANu3qRvn2Eh_WFzR4YB19OyIPpKq2ua1GxHjXwxOQRMyXw6UZTPhNteiObjkz-Wa085z4nyq1Sipk70xwexYvKsZHIrVHdIoL1QxhR3Jaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace87a5520.mp4?token=IM1K8P16DzQ98vo1JEVWe1HEbTtDZYOPwKY4QuteT8RX9DvjGQM3dqC0AxbCWOgz5ClPlr4d9G4Bs3fzmtyWRh2BEN7lI6i5viPyU7hTz5C-e3-7tDqUax2dEzCdHigM4QiWj9qRN8xLQeKWOsoUvCAlOebUGzWCoRsriS7emtnrWNL4i4Cpk41KdG38a65lSuhqeMRpYhibM9cYyG-421uCwJd79FtAG3JzEhl5342CANu3qRvn2Eh_WFzR4YB19OyIPpKq2ua1GxHjXwxOQRMyXw6UZTPhNteiObjkz-Wa085z4nyq1Sipk70xwexYvKsZHIrVHdIoL1QxhR3Jaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
آیا آمریکا در جریان مذاکرات صلح، لغو تحریم‌های نفتی علیه ایران را پیشنهاد داده است، همانطور که رسانه‌های دولتی ایران گزارش داده‌اند؟
ترامپ:
نه، من چنین چیزی نشنیده‌ام. تا زمانی که آنها توافقنامه‌ای امضا نکنند، هیچ لغو تحریمی انجام نمی‌دهم.
وقتی آنها توافقنامه را امضا کنند، می‌توانیم آنجا را دوباره بسازیم و چیزی داشته باشیم که واقعاً برای مردم آن کشور خوب باشد.
اما نه، ما هیچ پیشنهادی نداده‌ایم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/funhiphop/75464" target="_blank">📅 22:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75463">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ درباره ایران: ما در واقع با برخی افراد بسیار خوبی درحال معامله هستیم. ما با افرادی با استعداد و با هوش خوب معامله می‌کنیم. ما از هوش آنها کاملاً تحت تأثیر قرار گرفته‌ایم.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/funhiphop/75463" target="_blank">📅 22:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75462">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb46c8698f.mp4?token=l4Yg3TBS-QlzQD2OwhozuQ0wzSJJfRqsRgrr_--t9XG6BuNATxZox7ym-toY3qTzD5yAOnfZmRPekRFC7OK_AdqdFzwvXozE6ywOUqVb82nS7376sCqz5VA3KZ6BPN4HcxXV4jB0U-LOJMx52LPKXBPAwQd06RMc0wEuMQSQp376PU6Xn7RKqzqWyO38BT0gn3pi1fEIGjF9ra0-IhEKppXy1mLXKNTuHyeTJosj2Czpx1SDQTAMUT7bMAHtIGIN1FaLZUklb3gMOCJOvNZ3HI78QjJgs-EvBZ1EpjN09mSOGR8ZB3-yQFYaCubdytfflZUvsStH7xMeGwFkbqr2DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb46c8698f.mp4?token=l4Yg3TBS-QlzQD2OwhozuQ0wzSJJfRqsRgrr_--t9XG6BuNATxZox7ym-toY3qTzD5yAOnfZmRPekRFC7OK_AdqdFzwvXozE6ywOUqVb82nS7376sCqz5VA3KZ6BPN4HcxXV4jB0U-LOJMx52LPKXBPAwQd06RMc0wEuMQSQp376PU6Xn7RKqzqWyO38BT0gn3pi1fEIGjF9ra0-IhEKppXy1mLXKNTuHyeTJosj2Czpx1SDQTAMUT7bMAHtIGIN1FaLZUklb3gMOCJOvNZ3HI78QjJgs-EvBZ1EpjN09mSOGR8ZB3-yQFYaCubdytfflZUvsStH7xMeGwFkbqr2DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
ما در واقع با برخی افراد بسیار خوبی درحال معامله هستیم.
ما با افرادی با استعداد و با هوش خوب معامله می‌کنیم.
ما از هوش آنها کاملاً تحت تأثیر قرار گرفته‌ایم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/funhiphop/75462" target="_blank">📅 22:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75461">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2e93lisiWNFcr7JevkwXlKNs5u5GR-GFrkXGjcfV_F_iEAFCL0b9SYdAHKf-oT1CrLxmIiiNrHRf3w2EPAODfwFAGaUPubAyH-M2ZM2r1fr3TzAZwOgZNOs7VtJo-r77z9pNRPihGUcEJfpCV0L-lKdTbhetgsBuF8yH0e_zDJdYrXCM9NRdFPvvYsQ3CmeBf0XzRBgjCkikXFZ9vR5g_gwtFIH5-OPtrO0mPs8HrrH1hkpBo0tF0yQ8DW0LX_5Coct6BGxz6iHAu7G69RzSP35dF9WFyeqHAyFFJEYBS3L2y2D9uOkbq64GX9HuH52bGu6FLelLxBQCTB0QTdVmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من الان که فهمیدم که لارنس نورمن در واکنش به حضور مقامات پاکستانی در ایران برای پیشبرد مذاکرات گفته این جالب و قابل توجه عه و اتفاقات جالبی درحال رخ دادنه تا ته ماجرا رو رفتم جدی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/funhiphop/75461" target="_blank">📅 22:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75460">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgZqgQbq7Qi5PrSZ6KnNzgHiVL5evpBdOdwSyJOX1o1aGvyUf7LL92f4DFGxa1vVL9Tf39eJsCu1DW0tNh-cyFmChpy85zARAI1Eti-qfj24ysE7-FSmRVA3lpT2WSXIo7sOup3skiYutX4P9gmQGBgMZhtaUOqKSv8DC1GDxjEy0STiyDsukOZVvIELD74a_RU02xrsaPSo__xIoLQtC1-tKIza_AFAStSreaLsx9GT4vPmSFJ2L-xz99l7bJ0dm4qKusxBP6pmrJ8pksQFvhROf7aDxvHiC6D9Uv_WvGsiJyt6PzJ2-KrIVm_M5SolIHMbFg1B14iaM5ly3iiyMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرزیدنت بزشکیان:
ایران همواره به تعهدات خود عمل کرده و تمام راه‌ها را برای جلوگیری از جنگ پیموده است؛ و همچنان همه گزینه‌ها از جانب ما باز است.
مجبور کردن ایران به تسلیم اجباری چیزی جز توهم نیست. احترام متقابل در دیپلماسی عاقلانه‌تر، امن‌تر و پایدارتر از جنگ است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/funhiphop/75460" target="_blank">📅 21:51 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75459">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">العربیه بمب دراپ کرد:  کار برای نهایی‌سازی متن توافق بین واشنگتن و تهران در حال انجام است. فرمانده ارتش پاکستان ممکن است فردا برای اعلام نسخه نهایی توافق از ایران دیدار کند. ممکن است طی ساعات آینده از نهایی شدن نسخه نهایی توافق بین آمریکا و ایران خبر داده…</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/funhiphop/75459" target="_blank">📅 21:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75458">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تیراندازی افراد مسلح به سمت یه خودروی پلیس تو یکی از جاده‌های شهرستان سراوان، منجر به کشته شدن ستوان سوم امیر‌حسین شهرکی شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/funhiphop/75458" target="_blank">📅 21:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75457">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">آکسیوس:
دونالد ترامپ و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیروز تماس تلفنی طولانی و به گفته‌ها «سخت» داشتند که در آن دو رهبر درباره نحوه پیش‌روی با ایران اختلاف نظر داشتند.
ترامپ به نتانیاهو اطلاع داد که میانجی‌ها در حال کار روی «نامه‌ای از قصد» هستند که هر دو طرف آمریکا و ایران آن را امضا کنند، که رسماً جنگ را پایان می‌دهد و دوره مذاکره ۳۰ روزه‌ای را درباره برنامه هسته‌ای ایران و بازگشایی تنگه هرمز آغاز می‌کند.
یک منبع نتانیاهو را پس از تماس « با موهای آتش گرفته» توصیف کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/funhiphop/75457" target="_blank">📅 21:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75455">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کانال ۱۵ اسرائیل به نقل از منابع:
پیشرفت‌هایی در پیش‌نویس یادداشت تفاهم و اصول بین ایران و ایالات متحده وجود دارد، اگرچه شکاف‌هایی باقی مانده است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/funhiphop/75455" target="_blank">📅 20:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75454">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سازمان رادیو و تلویزیون اسرائیل به نقل از یک مقام ارشد:
مسئله زدن یا نزدن نیستا.
مسئله اینه کِی بزنیم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/funhiphop/75454" target="_blank">📅 20:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75453">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کاش هند همین امشب به پاکستان حمله کنه و خوارشونو بگاد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/funhiphop/75453" target="_blank">📅 20:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75452">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">تو آپدیت جدید اینستاگرام هم دیس لایک برا کامنتا اضافه شده هم میتونید عکس کامنت کنید.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/funhiphop/75452" target="_blank">📅 20:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75451">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">امشب میزنن.</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/funhiphop/75451" target="_blank">📅 19:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75450">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ: آمریکا در مراحل نهایی مذاکرات با ایران است. باید ببینیم چه اتفاقی می‌افتد.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/funhiphop/75450" target="_blank">📅 19:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75449">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">این چند وقته هر VPN گرفتی یا کند بوده یا هی قطع شده، ولی این یکی واقعا خوب جواب میده
💎
هم سرعتش خوبه هم پایداره
✅
لینک ساب برای دیدن حجم مصرفی   هرشب سه گیگ قرعه کشی داریم چنل داشته باش.   @mortalvpn_bot</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/funhiphop/75449" target="_blank">📅 19:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75448">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvABvriz-9z3CgzRD_1iarEJVGbMv18pynegmVUGHeUr55y0gJnfddoDIaSgjMK_CJuGf9T0MMry8tu0leZoJzciwkX7mQtwu9gBNdSBupa9ocAKL_vYn8XYLKtJPvBn3N2EG5PSg5CXeu_NaGBRLlREk4ppXVtXGe5TJyURQyT6MNkFbUGOFNyoV1-iE7nxQ8vPG7Awy5xBtn1PUh7QkAH94SXiATlHNCSUvJW1FyQ4HRwO1bBvC2SzxMng0Iz-CcKeGWdkKsmawxjjGyFiQayMrZI-ixuxVwdZ9L5tFP5oYA7EHUNpkNxhlxgjez3ysjgkFDVGa4L7Fqg6BbAkBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چند وقته هر VPN گرفتی یا کند بوده یا هی قطع شده، ولی این یکی واقعا خوب جواب میده
💎
هم سرعتش خوبه هم پایداره
✅
لینک ساب برای دیدن حجم مصرفی
هرشب سه گیگ قرعه کشی داریم چنل داشته باش.
@mortalvpn_bot</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/funhiphop/75448" target="_blank">📅 19:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75447">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ:
آمریکا در مراحل نهایی مذاکرات با ایران است.
باید ببینیم چه اتفاقی می‌افتد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/funhiphop/75447" target="_blank">📅 18:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75446">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سخنگوی وزارت امور خارجه:
ما نمی‌توانیم به ایالات متحده و اسرائیل اجازه عبور از هرمز را بدهیم، زیرا این امر بر امنیت ملی ما تأثیر خواهد گذاشت.
وقتی ما خواستار آزادی همه‌ی دارایی‌های مسدود شده خود هستیم، منظورمان دسترسی به آنها به عنوان حق ماست.
استفاده صلح‌آمیز از انرژی هسته‌ای و اجازه‌ی غنی‌سازی یک مطالبه در مذاکره نیست، بلکه حقی است که توسط پیمان منع گسترش سلاح‌های هسته‌ای تضمین شده است.
وقتی در مورد لغو همه‌ی تحریم‌های یکجانبه آمریکا صحبت می‌کنیم، این یک مطالبه در مذاکره نیست، بلکه بخشی از حقوق ماست.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/funhiphop/75446" target="_blank">📅 18:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75445">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">العربیه بمب دراپ کرد:  کار برای نهایی‌سازی متن توافق بین واشنگتن و تهران در حال انجام است. فرمانده ارتش پاکستان ممکن است فردا برای اعلام نسخه نهایی توافق از ایران دیدار کند. ممکن است طی ساعات آینده از نهایی شدن نسخه نهایی توافق بین آمریکا و ایران خبر داده…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/funhiphop/75445" target="_blank">📅 18:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75444">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">العربیه بمب دراپ کرد:
کار برای نهایی‌سازی متن توافق بین واشنگتن و تهران در حال انجام است.
فرمانده ارتش پاکستان ممکن است فردا برای اعلام نسخه نهایی توافق از ایران دیدار کند.
ممکن است طی ساعات آینده از نهایی شدن نسخه نهایی توافق بین آمریکا و ایران خبر داده شود.
دور جدیدی از مذاکرات بعد از فصل حج در اسلام‌آباد برگزار خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/funhiphop/75444" target="_blank">📅 17:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75443">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2e5bd4236.mp4?token=Xl3O8pXMxCl2hR5sZeaWOlvAVQ4yg6ywgkIvPCL1CHtQdeeq4E48RqEqCcezLSCt6POGzONbuha3S2sBx1N-nYYZ5f-mmj5U33dkbyleNIzQPBXyeExS2zl5GydXQwodiqx82TaD_ajqU606KuU-xz4eFRZ7W90A2A05ze6YuwsrC0HqdB72do13SNTr-1vFwmEwNRw_HG9YipZA0KVvLPewz2vGpo-4_Rku7LLFXtwOfB4BArgN5yagbuyEE2YDnWgOt8_lzY6yXlTAwSe6nUX5xYR-ALAR-yG9jJ34MTLpMSTG4o1I0SIMfWVBTIVr4rbVvJFnTIre0XrttyrQ1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2e5bd4236.mp4?token=Xl3O8pXMxCl2hR5sZeaWOlvAVQ4yg6ywgkIvPCL1CHtQdeeq4E48RqEqCcezLSCt6POGzONbuha3S2sBx1N-nYYZ5f-mmj5U33dkbyleNIzQPBXyeExS2zl5GydXQwodiqx82TaD_ajqU606KuU-xz4eFRZ7W90A2A05ze6YuwsrC0HqdB72do13SNTr-1vFwmEwNRw_HG9YipZA0KVvLPewz2vGpo-4_Rku7LLFXtwOfB4BArgN5yagbuyEE2YDnWgOt8_lzY6yXlTAwSe6nUX5xYR-ALAR-yG9jJ34MTLpMSTG4o1I0SIMfWVBTIVr4rbVvJFnTIre0XrttyrQ1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در ادامه:
در مقابل تعداد زیادی کشته، می‌تونیم هر دو روش معامله یا جنگ رو انجام بدیم،
ولی من دوست دارم تعداد کمی کشته بشن.
فقط تعجب می‌کنم که آیا مقامات اونها خیر مردم رو در نظر می‌گیرن یا نه، چون بعضی از کارهایی که با من می‌کنن نشون می‌ده که اونا خیر مردم رو در نظر نمی‌گیرن، و اونا باید خیر مردم رو در نظر بگیرن.
الان خشم زیادی در ایران هست چون مردم خیلی بد زندگی می‌کنن.
تحریکات اجتماعی زیادی هست که قبلاً به این شکل ندیده بودیم، و خواهید دید چه خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/funhiphop/75443" target="_blank">📅 17:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75442">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خبرنگار:  چه چیزی به نخست‌وزیر نتانیاهو درباره ایران گفته‌اید و تا چه مدت باید صبر کرد و از حملات خودداری کرد؟ دونالد ترامپ:  او خوب است، هر کاری که من بخواهم انجام خواهد داد. او مرد بسیار، بسیار خوبی است. هر کاری که من بخواهم انجام خواهد داد و او یک—او یک…</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/funhiphop/75442" target="_blank">📅 17:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75441">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خبرنگار:
چه چیزی به نخست‌وزیر نتانیاهو درباره ایران گفته‌اید و تا چه مدت باید صبر کرد و از حملات خودداری کرد؟
دونالد ترامپ:
او خوب است، هر کاری که من بخواهم انجام خواهد داد. او مرد بسیار، بسیار خوبی است. هر کاری که من بخواهم انجام خواهد داد و او یک—او یک آدم عالی است. برای من، او یک آدم عالی است. فراموش نکنید، او نخست‌وزیر زمان جنگ بود و در اسرائیل به درستی با او رفتار نمی‌شود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/funhiphop/75441" target="_blank">📅 17:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75439">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBxtqD8lfsXI0SAnGnVseJxvFHKShsY6jxOqWl2uA38Jtr_6c0tR3gcEz7JgRjVOZQWrrMLqqB0ee_rL6WpnIcev2LXWnzl34DgJ3nr90_t3l_rng8QYE45SXcnVjx8XC3hrsPCzHsV5rJ-w3qsSsgB4JrHealKZnY0cVhATw8ZH6fKS-X83-RdYeTPecQabEtgrRK4wZ5R86u7asPAi_VxvK8_lsZMUl3J8oA8n1R2xkKdOWiTCxF9danR_7C0NL6h8TETQ1r8Vo1vViQDLLGK--nic6EmYJhu_pQr7VN15OJIRfPIkOP5FxvV9ZXdjTDUyCgBRfguwotfVlT3pSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صببخیر  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/funhiphop/75439" target="_blank">📅 17:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75438">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حصین زد یا فدایی
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/funhiphop/75438" target="_blank">📅 16:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75435">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BcqYvGoL6MLfYiZbgFsRvB6hDU7Mk0nyJ2by2SpKJ6y8e51A1d2yQHr_qrYGsXNsgFDxH-C9flrl7bInh2IVikfiW_dIlPzIPtULKfuiMafI4rMHsDItN2SPUvkukLxPZLMF3ryiH_5epy8_aDctz9DOvA_DpMeIt6_EVKy1Xmf68QJ6tn_otCdeRpIU6Bc5R9FkoVuc2M4_FBBhZ3cv67lOQziUAN4WqO9XF41qjcB_jhhzbLQuoElbiLQ4L33ZWk6znE42FS_uyiDrLsqtOcYtCC1dNdD89FkWU7zdBYGuC8zRgSHqtspmNwLoKdN1MPj4ZG8soKNb2eS_jIJC-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست خدا عیان شد حضرت آقا تو یه کشور دیگ رویت شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/funhiphop/75435" target="_blank">📅 16:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75434">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نیروی دریایی سپاه:
طی ۲۴ ساعت گذشته، ۲۶ کشتی با هماهنگی نیرودریایی سپاه از تنگه هرمز عبور کردند.
@Funhiphop
| ALI</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/funhiphop/75434" target="_blank">📅 16:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75433">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سی‌بی‌اس به نقل از منابع دیپلماتیک: اسلام‌آباد تلاش‌های خود را برای حل مناقشه دوچندان کرده است و معتقد است که شروع مجدد جنگ برای همه فاجعه خواهد بود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/funhiphop/75433" target="_blank">📅 15:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75432">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اگه کانفیگ با قیمت و سرعت گاد میخوایید میتونید از چارسو تهیه کنید، گیگی ۱۹۰ بدون هیچگونه قطعی و افت کیفیت:
@CharsouVPNBot</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/funhiphop/75432" target="_blank">📅 15:36 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75430">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نیویورک تایمز: هدف اولیه جنگ، به قدرت رسوندن محمود احمدی نژاد به عنوان رهبر ایران بود/در اوایل جنگ خانه احمدی نژاد مورد اصابت قرار گرفت تا وی از حصر خانگی ازاد شده و کودتا کند.  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/funhiphop/75430" target="_blank">📅 14:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75428">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بیانات-رهبر.pdf</div>
  <div class="tg-doc-extra">115.2 KB</div>
</div>
<a href="https://t.me/funhiphop/75428" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">تا ساعتی دیگر پیام متنی و pdf شده رهبر به‌مناسبت دومین سالگرد شهادت شهید رئیسی منتشر خواهد شد.  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/funhiphop/75428" target="_blank">📅 14:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75426">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvdGXwSgyYVfnVgKIJPTFx9uFRJinEMfyRbD9xea2DvuDA9DKA7lQ8Jo3fZiZ2_LgGtt8B7M-BqjLcFJ5u3BiPgTb8nLVZh89a5g3_M_xDRT_lkiTx_RkG_7-Ndy64xVkTKcrp802wd5Onj2KtSHIgBw-_uy8uFfX5XhrdH2lMSgRgPKpvuJaUaHhRmzXdMDI-XgmpVeTShHkAMLM4IqCOuHm414oc96_ODyM3v5stl3166nEVLcSk1L06KA_nNzzxrIvFIaFEdIuq7pRqsLPVvZellUlA60adSvSwYwkOo4GaoiMqhHt8MfXepGO55-jqDcNHfmFuR-KT9dArokWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf67fa05f.mp4?token=twn7HXWxclR42EuFKD2-Zov6msWeq9tP6FnI74UBAgNtcVJ3DEDKVPfBVyvpX1h9zTKRVdlA4OjBw08BT9wNArbmZRiUizgYrrkH2cAWCmyUIsRkZci5g3HSRBSDk_UpEghTdXzwdrB-CrusP64Gm-WhsXVXh10kUBfch7ktnMV9rOtqOzDfW30ftV0snMg9rkTao7y8UbdTX7sw1fpw86CcLkyfxEW5wC3X-od1N1pQghh28iBE58ehYFfZQtXgLSadPEADr5241b_uC_4JXhhusC0PxMGmNPgqmocZA8RDq8jG46NMbKV9j02zK4gibQKKHSRQDa9WEyAHY9Tx0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf67fa05f.mp4?token=twn7HXWxclR42EuFKD2-Zov6msWeq9tP6FnI74UBAgNtcVJ3DEDKVPfBVyvpX1h9zTKRVdlA4OjBw08BT9wNArbmZRiUizgYrrkH2cAWCmyUIsRkZci5g3HSRBSDk_UpEghTdXzwdrB-CrusP64Gm-WhsXVXh10kUBfch7ktnMV9rOtqOzDfW30ftV0snMg9rkTao7y8UbdTX7sw1fpw86CcLkyfxEW5wC3X-od1N1pQghh28iBE58ehYFfZQtXgLSadPEADr5241b_uC_4JXhhusC0PxMGmNPgqmocZA8RDq8jG46NMbKV9j02zK4gibQKKHSRQDa9WEyAHY9Tx0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانر مک‌گرگور دوباره به UFC برگشته و تو اولین بازیش هم قراره 11 جولای مقابل مکس هالووی قرار بگیره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/funhiphop/75426" target="_blank">📅 14:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75425">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚀
Velora VPN | تجربه اینترنت بدون محدودیت گیگی فقط و فقط 180 T به مدت محدود
‼️
⚡
اتصال پایدار و سرعت واقعی
🎮
مناسب بازی و پینگ پایین
📺
بدون قطعی برای یوتیوب، اینستا و استریم
🛡
سرورهای اختصاصی V2Ray
✅
تست رایگان قبل خرید
✅
پشتیبانی سریع و دائمی
📦
پلن‌های اقتصادی:…</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/funhiphop/75425" target="_blank">📅 13:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75424">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXadmSi1ShgY9YLP9JPUkxu5q-1TS1EnjozE7-0F5aJ_A6whPoH9NJZTVFU_pz15b387Fn0uMVUqPhGyspNf9DhEanOqGrhWRFkG4at_lNTZjS-30313JqDF-7iLk1nMtFxuTFERPMqVxUqeAmKJIDg0CKLJyDWhTKvb7RtmJe20Ag3aQebgBjLVVnnzec5czPemcNIUOUYBeYeCi3ykPJQfdb6ivzFUWjiYvytJ-BFXUyJ3kOIku5UwAy9VacO3Z4bPhdvfhVpA4-u2lJ0e-ObrLtRA9m3GgbP791UpAKV5rBL0j_USrr_Y9TB036VKHPeKj2YFyjbj8cswnbgL7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔜
اکنون روز ۸۲ام
#Iran
در خاموشی دیجیتال است و پس از ۱۹۴۴ ساعت، کشور هنوز تا حد زیادی از اینترنت جهانی قطع است.
در دورانی که قطع ارتباط حتی برای چند دقیقه بحران محسوب می‌شود، ایران همچنان رکوردها را می‌شکند، معیشت‌ها را نابود می‌کند و حقوق را تضعیف می‌کند.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/funhiphop/75424" target="_blank">📅 13:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75423">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رشید مظاهری قصد داشته است با تغییر چهره و پرداخت رشوه به ماموران مرزبانی از مرزهای غربی به‌صورت غیرقانونی از کشور خارج شود که در هنگام خروج‌‌ بازداشت می‌شود./ به همین دلیل هست که در زندان مرکزی ارومیه به سر میبرد
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/funhiphop/75423" target="_blank">📅 13:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75422">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تا ساعتی دیگر پیام
متنی
و pdf شده
رهبر به‌مناسبت دومین سالگرد شهادت شهید رئیسی منتشر خواهد شد.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/funhiphop/75422" target="_blank">📅 13:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75421">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وزیر کشور دوست و همسایه پاکستان مجددا برای گفتگو با مقامات ایرانی عازم تهران شد.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/funhiphop/75421" target="_blank">📅 12:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75420">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">صرافی ایرانی اکسکوینو مردم و اسکم کرد. قوه قضاییه داره دفتر های این صرافی و پلمپ میکنه.  البته نا نگفته نمونه که مدارک اسکم این صرافی از چهار سال پیش توسط فعالان رسانه ای اراعه شده بود ولی کسی اهمیت نمیداد و بالاخره این اهمیت در این روز ها شکل گرفت.  @FunHipHop…</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/funhiphop/75420" target="_blank">📅 12:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75418">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/funhiphop/75418" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75417">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/funhiphop/75417" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75416">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhdcifJo-uFnj0hsUSQrWOhiFXCj0pXvx4YhBcUFMFeXgJR2dg9etPhRLbKSsTxsOATspmagUs9KlTHiM8pg8H-zU-chmz4g7ZVtLpMVnzeanqq5sAZJVc1Nd4uNlmrMVfjqYIi4whUMUYz4l-8Vq8XjBBNkPqLepfeBXr6_ADX-uVXYJm9s-U39KNiOxGjPpltpSavrwiUHczqywvpzaPdR2ZXXeSWRxufFlJLdb5GT0Z-29TQeqEGM5e076apit1yke9HBDOdZor2AgVEiKU7iVmec2lngyNAqkgTj08-ifFKD0NODOaR5h0Ce3k6T7FreH1VXNgCmD1Z4FG42Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز:
هدف اولیه جنگ، به قدرت رسوندن محمود احمدی نژاد به عنوان رهبر ایران بود/در اوایل جنگ خانه احمدی نژاد مورد اصابت قرار گرفت تا وی از حصر خانگی ازاد شده و کودتا کند.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/funhiphop/75416" target="_blank">📅 12:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75415">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVoWy7fk3P92vgiXYa-L6boCYymRewjyIWG--GGjUzbtL2d9MjhzGnICADvE-siDkGueP6PVLeqFO_3nH6MAUBn-tcDwJFk9A1ayw4QZniUYmfK5yUxpIuWn2uOkbJ39zlULTx0AhvF_VgCkKCKlOfdDvA3-9Tdpl0ug8jgQQi0MclcrHZwzIIN0PLHc5hyxbs9nrVmVXQxFCPwK0hq0i4vxQRheiCUKx8vqIfQldc_zssjm5SKrRT6H7k8vDczNd-ZkDP7rf9vlwVxEIlPKuV1EdD3dS5SuIhZ-gMUUCvKWAEyZWBfgDseolw9fKsjrLHdFqialM9co3_5BjWIDnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یسری وصلی های جزئی به اینترنت داشتیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/funhiphop/75415" target="_blank">📅 11:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75414">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBtU0da4Q0DuUQ410eigPoJNTGqlV5NQJioq2Fz4TJrJwc4ylx-nHwajKDxUK2wD6cTLmw56vAq5xehwn4LUTS-Z_pVe7KnrnrAsfsrWrRyOlBqDLhTBG56IYlDVt4SjHPAz7rhRL39AwZb8k68BdUvvwdCF0QZvS3EunELt8yNZc4PrnZgrDqWMPsKJvtmKkzkHRPcJ_U2O-D8A3Arf1Xr0ij530aqnSIcio1sudq3VBrVTL1NlYqnHctwxi-xSJFeL0DGlZNy_PdWCKTvX1ez0BOe9rWbIKuKWI-ekDDo7LsSSjPIXTd1rKBykTT3krsjbWwh1npt67mbMUGdPWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Velora VPN | تجربه اینترنت بدون محدودیت
گیگی فقط و فقط 180 T به مدت محدود
‼️
⚡
اتصال پایدار و سرعت واقعی
🎮
مناسب بازی و پینگ پایین
📺
بدون قطعی برای یوتیوب، اینستا و استریم
🛡
سرورهای اختصاصی V2Ray
✅
تست رایگان قبل خرید
✅
پشتیبانی سریع و دائمی
📦
پلن‌های اقتصادی: 5GB | 950T
10GB | 1800T
20GB | 3500T
50GB | 7500T
100GB | 13,000T
📩
خرید و پشتیبانی:
@VeloraSupports</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/funhiphop/75414" target="_blank">📅 11:41 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75413">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سپاه:  اگر بازم بهمون حمله کنید اینبار جنگ رو از حالت منطقه‌ای به حالت فرا منطقه‌ای می‌رسونیم.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/funhiphop/75413" target="_blank">📅 11:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75412">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سپاه:
اگر بازم بهمون حمله کنید اینبار جنگ رو از حالت منطقه‌ای به حالت فرا منطقه‌ای می‌رسونیم.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/funhiphop/75412" target="_blank">📅 11:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75411">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">حمله بعدی امریکا کوتاه هست و میان یه لایه دیگ رو حذف میکنن و دوباره مذاکره میکنن و فشار میارن که تسلیم بشن.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/funhiphop/75411" target="_blank">📅 10:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75410">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPIQ26nE8R1tahyGwEGSCaRMP6XAf1aJrbPODUrnE-sDqdfg1SGV0d6RZ0MtC9r9Dl9Xx7fkqbuLXnsZMAT6Jzp5E8MTai0a1cCqSteOjKV4mL7LX7EEk4C_39ZuTEde5XXG58Enn9W5f6jOWuYmCnuqK3YExWldgtNCgIO_DNDGzYM-LEueV9fphRED768KNePnMxsOMKP3UAaVZ6hqalaib3XvdyBPT6dyYhb6tK1FC715zoEL_PljpVJivhZ5fMxkWVs-QQYrmc7UxxG0N7N_cJfvONvjrJeCY7qbXXgofd_kjoVLSfcCBz1fxIeQjt6FEUJjWbd_TxyzpqXq_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره‌ای از ۱۸ مه نشان می‌دهد که ایران چهار ورودی از پنج ورودی تأسیسات موشکی زیرزمینی آبیک در استان قزوین را پاکسازی کرده است.
پنجمین ورودی تا حدی پاکسازی شده است.
این سایت در جریان حملات هوایی آمریکا و اسرائیل برای به دام انداختن موشک‌ها در داخل، عمداً مورد حمله قرار گرفت.
ارزیابی‌های گسترده‌تر اطلاعاتی آمریکا نشان می‌دهد که ایران اکنون دسترسی به حدود ۹۰ درصد از شبکه موشکی زیرزمینی خود را بازیابی کرده است.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/funhiphop/75410" target="_blank">📅 10:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75408">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DZn5GeaN6Tjv5J99Y-kTrMJFOuRvhRxpNtXP3KQjIL-TezFijoynlIf2MrKLDM8lx6yLPmh9ebxj48jpnyGyFsghz43k2clZD7kro0xMBjZdWdfkQ35Gm8Dr9gX3Qq54vacyF_1Dx3Pt28eLoPD-DKPsZn40A53mWcPEcawlapZ6_fTsrpdoxvNemyTHsfpLq53vrUBqOaPQftEFVuzjWEqoCZRuwIrTgX1VDCqoqkb5BXeUZ3gKK4hL2oVBIYPDjyUxngMuA2yHNZo0qTOmsg09qQeltdb9qW3ffaz8IhJ5JRX7BRMoy02ffN2gjQqEEiVYE7q7Y1h9xDjtsqGbiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tn0etvdgtqhTeqHc3Qyrp2rlXSEXmhs49ZKvnGECpaZFD2_QzXmVQiBUjbwSxpm2lkiU_qeXRuMFIPC9IMGGfpEgUvD_K8OmVjGWWCQ1plK4dRrwSazbDl1T0a4MYrGM0pWdrfKpOn1O0LrtoS6iT9TpgLzqKnoPsYWinSAD7-ocJ4ioquoVqoF8Nq98pYj0m_MFLaiSzCl1v_g3rIZehKooob8tZdaSS9CboJhFi5BTJzqnSHvYue0iERd9F1w1rmRpwUeqn3wgWq3KRccQ6o8kqu4qFS_LZwIJVs9YvG6iRg64Sal5Tqg59_98al6LFLYTofhmsCtuNL9aEeZQPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به مناسبت قهرمانی آرسنال، همچنین یادی میکنیم از جاویدنامان امیرحسین الوند و علیرضا صیدی
❤️
@FunHipHop
l Farid</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/funhiphop/75408" target="_blank">📅 10:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75405">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">شمال یجوری داره بارون میاد که شبیه افسانه ها شده
سال های پیش اصلا چنین بارونایی نمیومد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/funhiphop/75405" target="_blank">📅 08:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75404">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پوتین رسید چین
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/funhiphop/75404" target="_blank">📅 08:01 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75403">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jw0kv7NfPyy5Tokkvbbkq1JbbCxVr1H4PeqB580S0U4lSHDtIR6QNUgTUuH-SS0_smXijWNNB2rfdmJIWU-UDT2gkqdvFPFi-oXK8YKpWH-M8W8PA_r8an-5Cuc1uxg2BaddjJLbYpCQ1DG3hbPulMHmvaOMl1_0FjSEciLwEx1-rmv_yYYzCn86NggEoOg5i_lxH83kfjmOhdG3ld21ABfnNq46UMGH7qWIBQdndmUhTMTuUHhY4vYj1VwuRbgay-iYzY4rIfwNufahiQxDHodV9a6f8Bn74OBjCnO2nz1v3WdsgAVkyZMJYCpzF9u-xRPvwtrqVS-JfFuUXepckA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی ایرانی اکسکوینو
مردم و اسکم کرد
.
قوه قضاییه
داره دفتر های این صرافی و
پلمپ
میکنه.
البته نا نگفته نمونه که مدارک اسکم این صرافی از چهار سال پیش توسط فعالان رسانه ای اراعه شده بود ولی کسی اهمیت نمیداد و بالاخره این اهمیت در این روز ها شکل گرفت.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/funhiphop/75403" target="_blank">📅 06:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75401">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نیویورک تایمز کاملا از حیطه کنترل عقل خارج شده:
پیش از آغاز جنگ با ایران، آمریکا و اسرائیل نقشه‌ای برای نصب
محمود احمدی‌نژاد
، رئیس‌جمهور سابق ایران، به عنوان رهبر ایران طراحی کردند.
این نقشه زمانی به مشکل خورد که
احمدی‌نژاد
در روز اول جنگ در حمله‌ای اسرائیلی به خانه‌اش زخمی شد.
از آن زمان تاکنون به صورت عمومی دیده نشده و محل فعلی او نامعلوم است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/funhiphop/75401" target="_blank">📅 03:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75400">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آکسیوس:
برخلاف ادعاهای ترامپ که می‌گوید یک ساعت تا صدور دستور حمله فاصله داشته، مقامات ارشد می‌گویند ترامپ اصلا تصمیمی برای حمله نگرفته بوده است!
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/funhiphop/75400" target="_blank">📅 03:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75399">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کانال ۱۲ رژیم صهیونیستی جنایتکار بد:
ترامپ در ۲۴ ساعت گذشته هم در گفت‌وگوهای عمومی و هم خصوصی موضع تند درمورد ایران داشته است.
او در جلسه‌ای با برخی از نزدیکان حامی حمله گفته که هنوز گزینه حمله را کنار نگذاشته و این احتمال وجود دارد که انجام شود.
در مورد زمان‌بندی، حتی در گفت‌وگوهای خصوصی نیز ترامپ یک جدول زمانی «مبهم» ارائه داده که بین یک تا چهار روز متغیر است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/funhiphop/75399" target="_blank">📅 02:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75398">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پس از ۷ تلاش ناموفق، بالاخره با عقب نشینی برخی جمهوری خواهان، دموکرات‌ها موفق شدند و سنای آمریکا طرحی را تصویب کرد که مصوبه کنگره را برای ادامه حملات نظامی به ایران الزامی می‌کند.
سنا با رأی ۵۰ به ۴۷، اکنون به طور رسمی «قطعنامه اختیارات جنگ در ایران» را پیش برد.
این رأی فقط گامی اولیه در سنا محسوب می‌شود. و حتی اگر هر دو مجلس کنگره این قطعنامه را تصویب کنند، انتظار می‌رود که ترامپ آن را وتو کند.
اما دموکرات‌ها می‌گویند این اقدام حائز اهمیت خواهد بود و می‌تواند طرز فکر رئیس‌جمهور را در جنگ تغییر دهد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/funhiphop/75398" target="_blank">📅 01:41 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75397">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcSgkRpaeS5z2bWArtjJDTyuZ_2oCUWVJYdTkVq09-yrHYJiXD1rWBm_hqrZyEKKwzuo40VRn8syzdnhSsRKITKjrUlf5gwlBSBb47C97LEBk04p5CS8QgUQa9YOtKbvbivSC0m5cQjgjJg3as1vdY3EPeoonVvebJ7pMhiHC-eEhGjsqVEoQN6r0ay6-vLeX-vUiDBvlcREQO-2BfJWCdWj1ln-F2sYTG_Am7ajcdVp-GVrHysswGykBfQEWkw7MQiYhIk_37XBowQLyU1rEQ3QYv3eW_sh3fKVlQWhfQYEL1rxmOcF1OJzb-IjS9yw89y1iaddFFo7z1WkJNV3Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز:
فیفا قصد دارد بار دیگر ورود پرچم شیر و خورشید و پوشاک مرتبط با آن را به استادیوم‌های جام جهانی در مسابقات ۲۰۲۶ ممنوع کند.
این پرچم همچنین در جام جهانی قطر ۲۰۲۲ محدود شده بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/funhiphop/75397" target="_blank">📅 01:18 · 30 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

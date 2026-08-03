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
<img src="https://cdn4.telesco.pe/file/SES8NjRJR1AAGWRoj30pF7867y7pcPsp0VY-EoBWzTZ60yy85BLJk6RGteDAFem2QP-Y80I3M8Evs_eFsBn2uvpRGBdKpklxWkYV4S8zvRRfVyWX5raq1MMbKZaJyD5McCNdLBc3EbU0PYijm135FY00HKMhtYd4mOMCeITR8y9mYTsT6jKkbqPVkJtKMZdHwZFVgYQU6Y1ECjg0ZkF4InRpUN5AuvHOig0TQxg87-V7QLPa6ln7uzCu0L6oQf1poUrRHXWHTNRDYKqrq7QAH_CZ1HYLEkRPJcndMOrhVFgq73RlTNftIaE65cqR5DAZ5epjzMYKhL_yo1teIxhUQQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 17:48:11</div>
<hr>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a204c96911.mp4?token=mU75bvsSKXFTS5iNgw4RVdKiG7u5VSxWirSHUXLxh_LjSGYBPSlyT6220MHX5rv0Df1xiGSMsHIDelXXMdp4ZTqHBcjoeY-w1lzUQFGU1JDfCjiU2FgEWXUOy6ZZm6ER104i3Rrxc3jn561u8zy0-5r4ra9392Wl0hn_KaErfVYQ3pVrS3xkO4-katB3Zk4_2YJKdt_RMfELBgJjiOg07mkS44FPYxDHStGt7bXR5Fx2wVZ_QPzopgadt4Cvs5OZbEUEKV7J_MzxCZK1PybwAVA7hbfOphTHlR11NBRXOU7NnNGrYQWYqwIA1S1mc2SGJ5QBdmSTGP7MM6N0Q1q_CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a204c96911.mp4?token=mU75bvsSKXFTS5iNgw4RVdKiG7u5VSxWirSHUXLxh_LjSGYBPSlyT6220MHX5rv0Df1xiGSMsHIDelXXMdp4ZTqHBcjoeY-w1lzUQFGU1JDfCjiU2FgEWXUOy6ZZm6ER104i3Rrxc3jn561u8zy0-5r4ra9392Wl0hn_KaErfVYQ3pVrS3xkO4-katB3Zk4_2YJKdt_RMfELBgJjiOg07mkS44FPYxDHStGt7bXR5Fx2wVZ_QPzopgadt4Cvs5OZbEUEKV7J_MzxCZK1PybwAVA7hbfOphTHlR11NBRXOU7NnNGrYQWYqwIA1S1mc2SGJ5QBdmSTGP7MM6N0Q1q_CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«تبعیت از ولی‌فقیه بر مسئولان واجب است»
می‌دو‌نید شمر تا آخر عمرش
از اینکه در کربلا شرکت کرده بود
هیچ گونه پشیمانی نداشت!
شمر خودش از فرماندهان ارشد امام علی بود!
توی روایات اسلامی هم هست که
هر بار بحثی پیش می‌اومد دفاع می‌کرد از کارش! میگفت  تبعیت از حاکم اسلامی بر من واجبه !</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/farahmand_alipour/6492" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6491">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=QlRKxm2ajft7DlLfR1eCkoCcbaotfpYJm5SZQG3QZ2BGIGm8xPnI2W9W7V0K74LBDgWq7i5XbuY-fWiapOxwr6yZq1jCaivNAzTOUXUuMcjYNr-lOKZ0YmB5TAI5UI4eOKhr3AtrI6WQJ7v3pfeH2SPH3EASLbLQ7SJfxccApO-fTfJ74FgxVDcZIffVn0YWPlU7IeLauCb4wepp6ogGBKuVle5tfzQJtP9fnQ7HDBSt596qLXGmmqvBCXfoRHLHmShIRawNB-xjoj1sd6HxQF2rdV5Gi4bZcGh9fodi2_vvBMVtwF8cPWj5fndcAfY4YOBf029xOiD1vOlD8Wvv8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=QlRKxm2ajft7DlLfR1eCkoCcbaotfpYJm5SZQG3QZ2BGIGm8xPnI2W9W7V0K74LBDgWq7i5XbuY-fWiapOxwr6yZq1jCaivNAzTOUXUuMcjYNr-lOKZ0YmB5TAI5UI4eOKhr3AtrI6WQJ7v3pfeH2SPH3EASLbLQ7SJfxccApO-fTfJ74FgxVDcZIffVn0YWPlU7IeLauCb4wepp6ogGBKuVle5tfzQJtP9fnQ7HDBSt596qLXGmmqvBCXfoRHLHmShIRawNB-xjoj1sd6HxQF2rdV5Gi4bZcGh9fodi2_vvBMVtwF8cPWj5fndcAfY4YOBf029xOiD1vOlD8Wvv8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم نیروهای نظامی مراکشی، از مراکشی‌هایی که از خاک اسپانیا (سئوتا) بیرون انداخته شدن :)</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHAFBFcnvXuewN6H6Mr-97u3vLAllyfEvjUOEngOptXF5VjVKD77NsS_E_iJrlkMXWZ556Xek-drGE_lpy04X2e7GNm02uMBa_7gEOvaNEICvH8rNFRbbKHHy-uGxfM-zaoE7PRob_v2vIgrJoWMO0H68rVbtdriag0Kdzs092EgMtSY4V2BlB8B74OmjhzSSclgeb3xiWhWdFZ2LGFRgSdyemtnKU-n4XgxEEeyuZCi4ers_RYpaHxp5Krsxs1TKMv8gabADvUDZjnitiv8wbkMLYZfx3sS6udYvyeZmheljitgGWmBTPbWvCdTk_8vuUicl7xRFQRIBSqmO6ojOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtGw8K29MtYV8qwafr_11h5bRz6yBfjpYPnJo9K-PgOF99nRNds4_kh7tDCBMimQ2VIAYyZJ6MeKqpjKoElkijYzuL1fz8V2CYyt5ai611SjXFP5-vxBeoYPNdhEiyXYWdECQ_TqCp7nnQWACcIkH55rpVy14xSsbVca3Y5jetrnO5UIAHljd_hm5KaWctJmYDCooAtvBQvSeWzE5rw1xtg2dYy5iHDZ7clmneIfABvJop1DFKY-vzdiJ3FVTtoLD81I_pe8ZJ5MkZlLA85k1wMJkFCGHnifJCXyNvt-FxaTWAIBvRovrTyL_w1QDmogThlhwlpnDyeDz8_OrnSKsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tj2twco5ejiuMHZ84JP0wcvFlzHd7OaXlxdfIpaMcczC4D1C-5J_hIgplXGFT01_etp54A7AIOM4fCeRPnaVfBSPqEwBPBJ1e2rvOZLK-VXGwSPZj_6NlvZ1RAJK3umTBccGpce9VWvbP3JPhnYnSbGfeB2T_0jmKeJkxOtQVJHEfZQ-yocsV6iKHjiYnNZ8Piu4b5l8uE4oOuBDb3rYD5HzbHrbPcGDySvu8u3HEToMVOUU7PQ2WhmnIEP2lHiDji2C3jMI31N76zt4yMb7CcYvezV0OEDT7yIQGnEUJA_wURgcOdK7pt9syCcCaQQDJH0_7hHif6NcIXh8S9PUVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gikmSGLqJGCWopa-vcotBpNI08bGSoUBEUQ7JQi2Lap48K3EZyWJ4y2iF2wq75F0Pvuq2stEVFrE2pz1LGmuJbdGjkA7dTmbSmDjYfo8e3XuruGJfhlP9osPBY7u-H06augoQciQDY7Gw3Oyh98Xbf8eHhKkZZ-HzKS7TCxX3eRyFRMW5ofAU1sV862scrND3n3RxpjPo_wFT7pszW5kBJzv7PlawCTp1rRt_bhnkOLEAbVRvNvRkrACabV1swzmMEj12-HkrvZ2QqSP03Kha5fJ2R8jR0PHf3i4fcukgbC4Tpp_N7h7Tt6sA8J8cSVA1RNn4hVU9fvBrwtWRhrrqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBsRqkdqM72B8JE-ckFufxObNJaBFXBVYr6QoRBdWHWtMbKAaBKe91gju1-ecvjyNhOhCoqvRp0YhnJxfJo2sBRFIEgnfMnpBi_Pa44v8U8bs3kDIF4KzBZK6f4T7JS9cl43nH9oIwdVf2fDSaTnil1EkdpJ-aeqo7sTzJNr7TfUamvCxaKNna2ULO-Gka6-j0ZyLkDjQIVZW1xNYTNysidFK-DAJ3D6TCDI52WwKBlIgd6ozFvZgvowPb0aZfn5Ex6jdDXf-yEF5OeWiYv8JHH1o3Co4A41TtOUnpbQsn2mSAgCEVu4bl-ZKvNMrnMZxHPPaUlKc9yPyiMuIfnRaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSckZ-TBIiTdoOxEDmXs5ytxzTVe6-XRoW4mCU50uoAiaUo2gcifF-ZFbYHi56cmwbaLZ-13ijgG2rxk9fWyKri--0N0sMCSDgnLVARR7D7SCtNz7JGf8i3_YZ8kdtS3datfRwgrQKff2AEgO2wzMKWuERqR5JGpxk3yQXQQpO04ymIvA8UZ0fR50b1NJ2-cUTHwfHT99nT2lATViVs0xjroOYcI8DDPycgGZ3DsGOXhRoSJLjGIVQpcCDgWkmFY8jIsfd0Rws37eJsV8qnsqZkxGl5m3E_Ekc6VjqHA3i_1OK44q4xlb7synyfzgB_2Kp_dgZ6VNgpB_bkKAlQE6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQ1k5UbzFqqvs0wJl01nz9jJJF2d1O8Qzw13R5o31_OAzoewIa7VEvd8833-vddTL8gBNkKFtQy1Zct7FZ-WgO5RWdXuXsT04iomza0KlfXmZUkHADAWaNanMeZlcSm4OVzihmNi8wS4IRMLT5mTEiLXgYo6mt0rfaoUJlx_-jDoCGmEXUc6Nod-7ceZtP5qRb6iB3jdijhkkZQDecQB6YEtNxLPg0ZGDmfeCL6UWPuwL67ApKIjVKWYWQ9EhVOz4e6SkQY-6mSB7TB6yRXgvMoNAMXR2FXvTNQ-KJPTFMZwUtl0qhGZz9eQsxee0Eqys1ncHXDLFWZv4PWwZG6rGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-uYIYkUxeuWcMkQ5Sk4QuOMxV6E0Mtyifht6gYLv4p0Lx0yAOKqeP2tMtK7r7I-znH_ph4PE-TR4cKtid54Q6hmIv5eGTcmAq9etpUhUeqaq7WPKO3Wtog-_t6GnFW2dln_d0JmiyGKlstkrO2MaOqrUyDcu5pQeZBlRIx_EJ0_ahzFfW55NxOUSK2D-lrDIkxxl4eTtmwXO6Qjcfb_J0m2xFW8VXCvYTvTl1NC0QqOzESHyhtXFoE8a9GpClHH0avfxcaJyTljeME8iI3DyhxTTEq5r69tDXT1i2AacTyckCnf6o1XOaf641W5vSAOmNNE7_3s4o6Sxqb-g0lI8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7sH94k4tMmPxpeqIS3PsCCsS64reOf1lH59D3yf6gMmG0kCGwvlA3p4wnmPHnDOV57BIT270R57F8cZ5W-crXnCFxg-_RhzyXC3IhwGnW8MJ-ainEp8WLOqiAEn2WQyJ2xc7U-U_epNGB3jJW6QxO-h9MjD_U_Kl5wJmCihl_yA5wZJ4KSYy0U8kPBwW1SdmAyVTQAWYEAYt7u4-ktP4EVTMKImbzUK9t9QkIuweMmlFyk3-3Q19ABn0JUC3zGlG9-IZJjtofndl5zavJx7_cwA4UlLiYll8F1Inm9SyMLlt1xcLE374blQgRaQKocf2rPEVn9NaWuXwJxF6gMWDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرعون، جسد نخست زاده خود
را در دست دارد، زن فرعون گریه می‌کند
و موسی و هارون،
در گوشه‌ای از تصویر دیده می‌شوند.
برای مجازات فرعون، پسر او،
و نخست زادگان «همه مصری‌ها»،
«حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس
که در زندان بود.» همگی کشته شدند!
حتی! حتی نخست زادگان گاو و گوسفندهای مردم مصر!
و این تصمیم و اراده خدا بود!</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQegXSkgHUzyOVrtA0fNECy1Chq-PphCRQzuGM-rwjVgubTBuKwruLlNOWXqx7WUpl3gKezgRdHNLUi6Tji6Yi7RBHZYhR7ROJ22COXcZ1q0wiyyl2G3YpAWE2F46gsRfXxoUQGknD1slmCIXHno__Skjc_qkA9cZ3vhWWCdiSQI5u9r9LjNOQ1UhPJqhFEtmwI2jNpF0tSHznMPEAIkxR0bz1nrO3cKrMSxtvh8VtUAkRx9GT16UBNeOLnoyVtKjjWqWKtq8eygoSDCwVLvL32qCtJt1HMC13KnXu54JPPXIzjumA6pLev7mcqL7wHT1RKBQh6vQe5DPr05dxnBBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0MWkowWQmmdyAMvkgGh1G5mVkxL23MFrlfWmxa-mAjG5h1MTm0Ex_YBAxpHAt1MzgLwLboeQaDNpQofypn1txFukyzvpHRiwb0FYtHz7kwHcrrDaFDPRPqluHN3Sq6Zk5ASwVbkcJgNSLVzhADvGjKC1XScYUNlaaXxcisj7euuiooq-nVPvcM7OxIWsdnPp8GeTmxtjCA1i56GFxlZBgAmD8Ti-kAu9WZv54MzLppT4fAYEn4fj7YrrjbCPXyn-al6z6x4mj0Jh8plSmyCYTyMLKLHCgKxOItC-KgMLYjCpmki_wEK4IuMop8HOYNvtN_ZQyW73Yia6-rqu8xU_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.
‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،
‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا بتونن بچه‌ دار بشن. این رو خود آل احمد نوشته،
‏او اما آنچنان ضد غرب بود، که میگفت باید از اسلام، از منبر، از مسجد، سلاح و سنگری ساخت برای مبارزه با غرب! تمام هم و غم او‌مبارزه با غرب بود. می‌گفت روحانیون تنها رهبران طبیعی مردم هستند.
‏اساسا دنبال این نبود که اسلام تقویت بشه تا مردم برن به بهشت! میگفت تقویت بشه تا با غرب مبارزه کنیم!
‏علی شریعتی و علی خامنه‌ای، از چهره‌های شاخص تحت تاثیر اندیشه‌های او بودند.
https://x.com/farahmandalipur/status/2083853984113054084?s=46</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b21yOC7U1ZrtHxdvG74FKnhw4Gma9Uwo_1czO3uuqx_lMKWFl75WI_un87Qp7QW0PgrHkPjQ3AqW9-jdETdUntk9pt0h-_eP-aur04vnASBnP-v4uKe7OhGfKd_NifryRio2iexFZP_z4_qi_YDh6yBLRxf71iTEp9cuI8pOf99G-9swQExaGoaWi8eUR7Q5WG7OzxrotLyFjH0Nu8IdhruUCP0WpAbp9eJQWWabTKEgwXEVUh64RoV4dH0WlIdfgKXpRD6G7xs4exwH8UPS71_Zy2YdhAwpNB4xCblX13arKJvYeuf8_RyBRqzNRP_wQkagP9SaL4agXMr8yCK88w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIGxKpEutFmgVZOI2g92HD0QFQp-OutM3DTMaM01HPUcTF7kUJ_RhWOAQ_bYYFkVfejmLFVhHuabFkzayJHQr9ibZoeZ_Jo0s-WWYfrOxdIjyQivOpmjEjOkR0M3P7kOJlRW1QfT8dxGvXz03YQwFklrBkslJVZbPAHsr9mnrI90wth6D5PrV4CCvve3w3Cf2W7Hvi8jxkO0kNmynNinjz-Mgl_KZBvE1qfw80A9mGFub3BQN0_mMC6IYYMwzKIv4rXCUtvOAn-jn0I7sA5I9hQtnVWS-MjSc98oP8HVKkwiu_Xl2JbfaYhOP0d61XVeGa-pFZw8xSz1hrUIHvDMbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -
سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!
تباه در تباه!
خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».
احمد شاملو - غلامحسین ساعدی - اسماعیل خوئی - منوچهر هزارخانی - هوشنگ گلشیری - باقر پرهام - محمد علی سپانلو
اینها روشنفکران ما بودن،
جامعه آرمانی اینها، ترکیب کمونیسم و اسلامگرایی بود!
از مسببان انقلاب تباه ۵۷.
از مسببان گمراهی یک نسل از ایرانیان،
از‌مسببان  تنبیه نسل‌هایی از ایرانیان که هنوز  به دنیا نیامده بودند!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAmdDjgu3QxQoyMSX5jGg8eiTvSaGamEepQINQUNbttda4ZrTfLcIA1UWvZzMqWT5ICRWFMOK0P8H1vZLfNmcFm10RK8ok8wQJbXNOmTmwBKVokfIbAqeMqO1r3ANxVbdukxFVNc23QcJNjrZ602bQfx1_8ZjokpcTv0r9reIVEF1afW59xh8Bqtl0FCNkyYfROiZXjmJuX9JtpHaxv0PKCQ087XupiwuL0sg-ZbLK_k5shEdZ8tfa9tPfCP_9rpPLfESSx8iMCez5HE25mIFczY0-ziE0_8oiEu6x9IR0ueabn1yVOT9MTlJk0PevLogIZ7QFwt6KW59JZdQRaxiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=ioJIej5YbayuKcU0qJRr1UBTfDm4_Rli3nzplhdDHmxj-vSEMO-Hw-WYHumtYq1U1fqH9OzEouaXtoAuWu01e5viEp5JQbwHaXPqbPgBCC6bH6TCsf8UwkxeDTRa6Byb0nEp1ICKe-5pZ6Vpghsso5uqhH_W_-tVFDFyQIL6Roj151iUZejFn1J-4RGgJ_nl-5x1ty841n5AbT1z1FtGhNPNW1S1V2ri9KfDN5R8uhBM4TkzE05gxeFgv3qWJ9tQEUfmRqf5TOtzOQEi-JVw_UAqWXrx0U8B0U_hNZhwFcoTr_pxcTKjC4MBrwcuU-KbiXe_1CmOBGn5GZuOKyiP6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=ioJIej5YbayuKcU0qJRr1UBTfDm4_Rli3nzplhdDHmxj-vSEMO-Hw-WYHumtYq1U1fqH9OzEouaXtoAuWu01e5viEp5JQbwHaXPqbPgBCC6bH6TCsf8UwkxeDTRa6Byb0nEp1ICKe-5pZ6Vpghsso5uqhH_W_-tVFDFyQIL6Roj151iUZejFn1J-4RGgJ_nl-5x1ty841n5AbT1z1FtGhNPNW1S1V2ri9KfDN5R8uhBM4TkzE05gxeFgv3qWJ9tQEUfmRqf5TOtzOQEi-JVw_UAqWXrx0U8B0U_hNZhwFcoTr_pxcTKjC4MBrwcuU-KbiXe_1CmOBGn5GZuOKyiP6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYed9fUA93dhYdfNmttVcm-2lUMw13RTbLImI-z9mIYAp3Fn2k2kwxWO1ig3HF9kt__Qd30l4m1S2SDDhtjk5O0OQsidkXQ07ucDS_PfMsyPqIF9ZhT1o8M2Cxsd_EbJQdDbi9aBA4SfwyLGuP6nOffLvRWw7t8OIr385KWwqDP63fknUcx9lGhmSwZ20KPLmq_5e37EHVefD9YRhdJu6ixoSXKTToGezCK0UiQndY6nkAU_-eRTxFwse4feS584QcekMbB0tAYzlBdDkGKmgpvLIimfjExjasGpdPQADAzfOTbty7ziR-RNmt2mTKBDmtYnfK69_5xd6506jVO7-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qp-uWfFXcnmLv-0yLX9U0HSaaUUxpVEYsNA35IzA3RZ-mM09Z8qB8OWIInZRV5Fe5j1ZjlLlWA0DazcSD2o0xu8nMZ3ylh3dgmLYJw4cWa_sQc0zyzCin0Qbvx1roTzR6johL1kwCcTY9qRTifFt9OubskB7kzNkKy_yiCe2wjUf4Rim-bMz2KZahHQ25ckWSh3Nebd1taY4UxIihZQn7f69pMlL-EJplk5JVhn2Yw4agFirJiH4DSJsR70EE6oEzkzw_d9MyyExhc_W7tCeH3FiKLjiprPnDrY5dfw_ZNe1cvNuh7Bq8f0xN8kOgk6fnqMRLOmKSOo82voIFrZTHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjUcCmckFhian4fxZ1CPt_X04Yk4G8LvzCk76rPDE6hZ-lP3sq3DRxi0vaxhA4hl8M9pNUa3QUNtth4SqRQZqUIcLA74UnsK_BPTS6Bgf7GNfkE5jfk1PNSoy0Z-Nal6KoKmZzYgnrEcipTB5LCSysETkY2UCmtC9W_frZ5AJU0WJUbf8SwLP3_WtodCIrf5oxk6gnE5v71AFZdHvikJAyCVbnur0zKhhuZcRbMvD7lj0cBlxQbcUSRVRelz6dp9KuB31v_i6bCWRUBIL4QRyPXcyCyFwRlkaDQCAZxiOHi68xsZNv_V0yoVkKiRfa_AR3IN29c3dY7Mmhjk_EPy-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDHacnr0c20XU-Mn93TwxdYQRPmMslQKLr4o29QPvJyAKcy7m057gOm1h_52sdyyk_wggwQkfehZCnuX1RnlAf3I_jxlOS5hRxbmAD-maLHYDu1uVPwIl--RLi5p1rsAVB-Ef4J8rkNCiz8P8EargrLZEwUbNs_qBx8TwA6U6m51lQqg-4fttpnt38Y1lwQRV_Luo4HcJdrJ5a9VNV-YaMkM33Ahvegh46Xp54iHD80eSPYkdgMoWrnVhOWH5nkzBtXmrFNBX3E9auenCTk0vkDWS3FW0AhkgOJQ6OQXOQ2b1Tjm_FpV5WQDTDWNIGyg2Ed44ana0twl559ztAUL6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDfHNt4GXQclXvWuWNiVIBaGakhureYSj4633v2bMtJ6pJTRcJdbWnS4xyxyOs_y17tCCLk3M1R-HNLfYcHDFA11nfUVDtjedH6NViBc4Qe3xiAPUjpIKQv6cvl5UEaDoGq88xjGN3zWbN2lZlDvupRJv_nh4lqYncoWsM3AGZ5JpyKkTY5MwpdAoqgoyisi50QRTQejxI3O7yLxT7TmjjxedDhia5GRtdr-kSxWwh0aa3CZy52Mkn95d0_7AURaZywKbjRVVa6GRYQOIBAuAn8yKPIpCu0-3q4ScgNpjiS_lbaTP9GGLz_ey-1V0TkiWqvL8hXuqMEx-Ip2PsL6kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3cOm6D47XdKcv28TZwFqbTbRedUe1YX1hwqOgg9cMrvjvVzjJkLeHz2A8qxAZUF8EWnG3xIEGEzAi5SpA6Z9kjssRDX-V6Bi2Qq4qzse_91g0BLB9EZuQkQ_pjtav-eIyQQcn2e41_3rv372HT6P7x0TUNdmsUtwaOpCyCS00bUiVggq3ljPbhrdL1pUDHzCHhU5CZpAUjaF-BK8Ag1qmAbuOavQXzjTWMK_2nvaVtFt_hcJ2AL4ttwqnlUsKMrOc43DMSyarmPmrLMMi-ek5JXSpM7WD3UIOJgS1fb6GfE6yUjm8SZG3-5xdP4ENjhM4MAgkcojaXPZ81GGWxk2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEyodjps_bm2yA99yBgWdx2zSaa1wR_aQw6i6ImDrK0RNnNWXWo43EO2boAb2GfVyvBn5hpPNYvM2mOwZFsY6HO3neusGmwCt17sV74wvXjE0agIGQ1MBg1LBCeHQG6Ceo3lmK5tIW4N77AmG1agcW6DOroYToAuuSxzUkxRKqe32A4H7_y-e7-VlpS7cWKRWbai7QFGxUNkwMctQ4q5DH-Xc4aU_vwxoMfaTy3g8pulNnQqc4MKswQubIhzfyFDxsecjIYRMKeSrrbEtQu4jVlj2nUf2rdlNc7fKpoluWnENxrdBNRZkxsAY_Jjei4jtha1EObITALVCRMeVf_gJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmJrjyADTDdw8RmBD7kYTzmHGtRg5EpB-QAvzCX4yghevoGRHvQs8MNzuVpIoFaU3g3VIWYpRqb39rseALyA80HMUKMeKjOafQYNwkATwhIVmLY-V1jzcdEA2l9XVbdiIfSTTyT1g-8azyF-cW6xLEgq5WtKVdqUjU-oGoMY1Sm0edxo06SCJYhhJyDHIxd1rxVK5jUfdZ3kxadKWMytpA-IIk_xw4sL4TeXBqO_820LgEinBUjuKMSaesLlX1vyG-CMcQNDYaYP8XqzheMoHVemgJGUyJ9OSFDzsYny_sJYYmNdTrupAXiXmpAkJxRX581y057tbZk-bDuTqFlLEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دولت ایتالیا آزادی رفت و آمد هوایی و دریایی
بین ایتالیا و اسپانیا رو به طور موقت لغو کرد!
این بدین معناست که تا اطلاع ثانوی،
پروازهایی که از اسپانیا به مقصد ایتالیا است،
دولت ایتالیا مسافران آن را کنترل خواهد کرد.
اقدام دولت راستگرای خانم ملونی،
فشار بر دولت چپگرای اسپانیا را افزایش می‌دهد.
دولت پدرو سانچز هم اکنون نیز دارای کمترین حمایت شده و پیش‌بینی‌ها حکایت از آن دارند که در انتخابات سال آینده از قدرت کنار خواهد رفت
گرچه برخی از راستگرایان امیدوارند با انجام انتخابات زودهنگام، انتقال قدرت سریعتر انجام شود.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=g39fOU1xiZt8rubRTiErA0Jf8tdZ08EPf5vKvdDwuO7IbKmPdOqrikqUU50un_B6l-nhv-zUz2kV7pzMS3z0n5kw2WuZ0aEveBw7JHRc6MGWV59aud6vB0yJDVLKLWkiI99dFW3CfFIAoqqloB7z9yh-r-Ka-NdFxmH_UuVOTfkyOTry1Cp4j8P4dTFr61uiecPoYNGReXe4uyi7nqBFwMuqjN_rR--Q3wNXJ-WMTXNcXqf5w4H2a9-8Fm5jsyjYitpn427nCuF0en0GRvsn-ShlZN6wDKWz3EnP6w6AaWJI87Pu2zZ-zNkWsYI0TuuFmAeS0XxQeuQFPoMVZFOVww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=g39fOU1xiZt8rubRTiErA0Jf8tdZ08EPf5vKvdDwuO7IbKmPdOqrikqUU50un_B6l-nhv-zUz2kV7pzMS3z0n5kw2WuZ0aEveBw7JHRc6MGWV59aud6vB0yJDVLKLWkiI99dFW3CfFIAoqqloB7z9yh-r-Ka-NdFxmH_UuVOTfkyOTry1Cp4j8P4dTFr61uiecPoYNGReXe4uyi7nqBFwMuqjN_rR--Q3wNXJ-WMTXNcXqf5w4H2a9-8Fm5jsyjYitpn427nCuF0en0GRvsn-ShlZN6wDKWz3EnP6w6AaWJI87Pu2zZ-zNkWsYI0TuuFmAeS0XxQeuQFPoMVZFOVww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8AkV5ox---NyhWjcrdVjg-HW3AIEDVZOOd3wRpIlHP6A1O0y2ZKSbCebQSFLz8YxFHo4fZ0bl7dbahD2-qk9diEKHXEGmq73BGnICsHaCikppTPuox0ZBEDxNfxbtXvDkL3h4YIE_lxct4uIWZhOg63PEuTV_3NW2Jpn44cxf1shRqGnu5pLVEfY1v-M83bY4LT2WMKXiI1gwGBQ9nbyeDoGHaCXftOgaItmWG1Lw4dF5XAthrcWZMo2f2iJXajZBGQCYOjUnGUum7nosF2hOa0JqAi085qBw4TXOdQ-nJ8mgJXbDY8ezWrQPDOcg8LxDAmHoyQFgzos_19Xvzgzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTLz0ERiFuyR7Z9h8YhOnTD18SGOkrs-9OtScVh6ldInErFxrWzw6g64Gr3oRxuPoJAKcEOF7VU82sH_XrA6Zo5logTifJhHu0SzAryCCCSgTs2yTYyFqj7MJI-KqKjyh8VzAFFpzDc388ghHEtObhfshGIbTBZ6K7ordkY3alf5y146D3PhByMwH9EJbNrT1lQEOKUZpdmbbvaCJ0_yA2LeEDDxrQed9RMGfbp4PiLnaEm0N_g6BiX3q4Vk2Vn5cFuSVoqEjqWLDSKDy3kdw543Ah59-2v7eQFY9RvxY1wpFo8fz435uA3tt1Vt7caal8Z3NKICAKvZdvorteugAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIsn4-pYKwb2YKm0Krrmy7x9F9jUBuOKTjtXdTaSdd5gjTY5FkKZlIuhXPOCSXG7Gm8tbcY5pjJ0DBD4YnTuJzEUWhOjNkQAIYUNM32naC9XmWP953xnRyiVRPA6w2aCNYWcqmQiFXIWBY17cCAaGo3oGxvK_dH3-fYYgz6ixvrplKZLledbiLUU4KVqHGNI_GTaYwWUNqP5cme2o_vYXWwWFEQBQ03kV2HZ38kss_UXVz3pGmnYx8G4VO_X_Cb2Xb171k6hcJFq_7YLbD95fc9n_OnOPiY9Jb3zjAB1Mr4qPp0xfDmuPN-mPUa1NRW2jFqkR8erKt1v6hAcIwtRkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j610iV4gTXh-kWqQCV8jZByOMWfsVi7e0Sy0nZkw450ZKtlyF_7TPXKwyY3rMQFZ-xnEFt09wvAVu1XkVTXv7foOXcevoYjWM82kyk_Cuc_7gGcPK27H1-EDCrz6Rij7qysirtMsfKDzpNnLFoOdX0-Fv9ND3JQa90hJ-0KI7llCPtw9N-3VSBN3zKf2Jb32HjQPTMpzjr_0tPss5mr6cKEAIuiUOfORfH-ylKRq10jp7nR9W_SnDtKraXqDRax_ypEqLqYArnJeT_QOICAB_VaJHYyRakJps2Dlp0NC9zC5_B-LnEuzRYrC8BXd9nhhjHzyB2GL8SoUI5BxzjaPzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbukSswJAoDpHD-r_hmtZTxUIDuQDvjn78SFXt1FQG_XOZoK0Jy3Wfgn5HILYUry43YyTOe483MsO2iXTQFpAX-jTCVAvq65O01M-wmp8ysRESYqKrCeXxE7oeFsHdRYbEY4eI6_7_-A4SiK4tJ3YTspinZQznBCJw-geUFPWOQulqD5QBDeUhdTIy7i5JKT3PYlVokU-o0CB2acJKsvokLnS5cL4gyC1VGgokk1g4wxzVxSuxxaOXfTiiIim99Cjtq3vrcZDma_VcvKfnu7_kGkhOyNiB46XCoVZH-Tal2RYki1kFw62kPiRuBaxi8dDyWliTM70J8pIAzkI_R-TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbGyw4nH0WjOc5mwlGZiUssjgKJtvQ_ckMNfHUAuPg9M2H3qZnVBDxRb7XnRv8IEMA-T765R-pAyIBtWalRAlS7VQSbuup_j1CO7-rXgcqF-XVPRF4hNQ7CARPlr_5JdMMKSUIQWaR3G0z9phGEJ1QgkI5rbWVxoZpGPlEeMWBy-jx1yi_ftajCXwP57Z4TKCmMZI4L1y9o_n5v_CVt8nN70S-xffbpvohmcr_TCnYfIGTqS57cLhz4ipn2V9Lvr4zeksVJGZrLjmEQD8AOtz_zBU4ZtlshXBohCjlrTqT6KJYqBpV7qwileKMxzIdS3uJbzVjUaAUnxvjYrmWOHNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CcVJ9gn1L04wqOMvUUiHONCQxH7iW7_SxkIsnbiqdLbKu90cSmOIQnXzCa2nPAFoXxnyQnUoTw6CyH8W9snmu_V1KZDPkhL-B4uCJBhEJzknYqJsiRM0to3uHG1bjb4YV307Uz9pXYyraz5587KUCdIRh2RDr7mqSN5w7hd3bTGTEWYpxxpCq1JBZVh6vO2N6O72iSICmTeOorG07Uu5ocnSx_VgoojPdhbyCR8RFAzqtym-UDdkfEZpRw8I6KmtYqTvXPzAVN0I-EHsT4Rm3NQS8n_UmsddDRPlnC8yrC8D1mf3jxnSryScMjdqNvDszJKL-2iWJI29nZawG-iwKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=AZyesAR_BN4vCQUCZpRimFk5gPDO4EJV8AIgdBssvVPmHh7m9CUfcRaPyRHjiCFTmCFaqAGy4hE_oLCsiWp2JizOycLRCd1eB-SPPDmxtFt2sQWXRyDuiy3yJjMeUNeILrzbWeD5tKIihyNOmwF5lBfV8mk3w8-5XoPZpUfzvvTkEoctBm_p_wI-KV9rjZ31QyKajkKGh2fdvntwoHj4bspw0vlRuM_EHqGRbzcVXyP_pEQTIxD43i9Irgg4D9dUIwDuktRg4SjTZKrBQO7Gcr-zXAu7MFqnkk5M_re7paluYvHzjjCV8H0xDBt2A2lqyRXVrmBZp2DmNrkGLxbufbOQjZWmxcTppyyKrRx1l3JvYsq2vr20pxjchax-xQGiqjnp1cDEKtOvTKwIK86eDHaT3SoW5mCH6k6kxADZykX_4pKo_aQ2-TkRjXWK_Ea_-KF91oDV9FmIem9CFsPGv97gg8p-2WqtLvPGJBXIswDn8TMa2mrTLC6bA5b_Re0PExXtpIWU4RAh-aDeHw-3DL6ShzImqu2kNgNTGR8G2YVoOHW_lEz3-9_HrIh6Uf0ThoEyElL3NfW2L5zQVoesUjoNp87-nVut0CaQi__1jkZ4sHmOeGbmqhvgvT4PQbHbmPIVaX-FjbxWBjf9ar9Sx7-KTmwqebBQnfXRTDJiLWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=AZyesAR_BN4vCQUCZpRimFk5gPDO4EJV8AIgdBssvVPmHh7m9CUfcRaPyRHjiCFTmCFaqAGy4hE_oLCsiWp2JizOycLRCd1eB-SPPDmxtFt2sQWXRyDuiy3yJjMeUNeILrzbWeD5tKIihyNOmwF5lBfV8mk3w8-5XoPZpUfzvvTkEoctBm_p_wI-KV9rjZ31QyKajkKGh2fdvntwoHj4bspw0vlRuM_EHqGRbzcVXyP_pEQTIxD43i9Irgg4D9dUIwDuktRg4SjTZKrBQO7Gcr-zXAu7MFqnkk5M_re7paluYvHzjjCV8H0xDBt2A2lqyRXVrmBZp2DmNrkGLxbufbOQjZWmxcTppyyKrRx1l3JvYsq2vr20pxjchax-xQGiqjnp1cDEKtOvTKwIK86eDHaT3SoW5mCH6k6kxADZykX_4pKo_aQ2-TkRjXWK_Ea_-KF91oDV9FmIem9CFsPGv97gg8p-2WqtLvPGJBXIswDn8TMa2mrTLC6bA5b_Re0PExXtpIWU4RAh-aDeHw-3DL6ShzImqu2kNgNTGR8G2YVoOHW_lEz3-9_HrIh6Uf0ThoEyElL3NfW2L5zQVoesUjoNp87-nVut0CaQi__1jkZ4sHmOeGbmqhvgvT4PQbHbmPIVaX-FjbxWBjf9ar9Sx7-KTmwqebBQnfXRTDJiLWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=SDG_EQlju0zUbNzY4UYMJZr6IAbX3WMdlxZaP1WT_LGSSBGwagBFEe4MJ9VUuYTV49XC3twLh49rlumKSak9hSwYL8AQVCzrEFLUikMVn_3EnkDi-t94k6wFxDMfuuoYHFHWxZH_d903C6M_jcnt8PA-Bv7PO1i3uAtywH-7K04e0msXWhRGfQwSZutDJ4imTJhrDHXcqNrcIlzGjeamumihSuZhqcL6XK79ssrqmojg5ZMznnu8tZ3f13Ah0HI4BFBOlCqhGEOY1aC3zH9s7mHcJFrulQZ57q-Ay2q3ouBou6QB-4y5DMPR9_hN5BrFiBbzJkPR4rcWwTOVPaZIDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=SDG_EQlju0zUbNzY4UYMJZr6IAbX3WMdlxZaP1WT_LGSSBGwagBFEe4MJ9VUuYTV49XC3twLh49rlumKSak9hSwYL8AQVCzrEFLUikMVn_3EnkDi-t94k6wFxDMfuuoYHFHWxZH_d903C6M_jcnt8PA-Bv7PO1i3uAtywH-7K04e0msXWhRGfQwSZutDJ4imTJhrDHXcqNrcIlzGjeamumihSuZhqcL6XK79ssrqmojg5ZMznnu8tZ3f13Ah0HI4BFBOlCqhGEOY1aC3zH9s7mHcJFrulQZ57q-Ay2q3ouBou6QB-4y5DMPR9_hN5BrFiBbzJkPR4rcWwTOVPaZIDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4B4ARLxT8Yjm6YsuHI4o1nyZ79I8eSFV5UHjGfH8UxaTKSVOvJ8bWuJjGVC5TbbXVzSZDuJ0BTdxXB4XTS0HBXe6hnq8s8pOuu0fSgyc8E-nZM_MRrQpHpYRQmnUvspioc2QNcDGZypIKWqE_CsIC_BisFBugfk3yzf2ARU8F3ReLbWdGt0XG-PqmVIGLWND8CFz4DPyFlzvgleVTrFxDIBG3TFK0aLCFGaXQPMrTh4iOqO_Svz0z_lhn00EEA8sJzf66Xy7TFY4DiW3ZmCWauNYfHu54CUifF_bFB_OcTafvfWOlRhqB7cBPL3hCbttNzheihs-O44Hyaga5Rm8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Znt1yN931kPckdgQ7PMJ5qjbU06YitIUMnMLucTWRWeQJXX-zsoI6MHMcZwesfOvjxV4WKzYYQK7PD1KtB6q7kCutHSPiN6Bbdv4SpCDIhMSBlKvRm9gfacqellMjNb2QdW73KI1fIupRTyomHo6X8Ys9UjR0Tmk_kt_88TtyQ8bJhisH7qjI3Zo7Yfq9ZMlBm3Pkp5REf7liT9YRdgbEF7LgozH0OQ14TWxNp8e9DNyVeoLs8iScJlRbTQjzRDHTPStedBH3hl0tldChAeca6CVeAprN40Sa_uPHn65WAwadVpMrQCvVsZTbUPhd3VhoCkfK612Vsmu-PykL6r-8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=OtlrfMTjIlIvJm1fdQfuo3pUQfR-sdSTGxHcySGg-IVWlmXpyZjQwOSKDAO3gTIXCP1WwmT52jIikelj-cLzy6_6PB_jQj6m71KScfGNS3LA-2xd5nS7D9CYNUlqgAAKuRIS82XAVc6Nqayyxb2lY2znkd4m7fjmSfTAj-zMlkJa54eVstcabH3H3WU2DsVwBb-xKumwS0OAMghvsAbcAymJ1Q9plKB-Jes3h-kj6JKZyjNtrnXsl24CxELhR7wH1j7v7aG9GL-SKuOvURAE2wcO1ZpqWYeUB59_lYMvww5HLAgOMPV6aVZ9cY70WZUDNtqT8TIN4qP2m70eunCSnzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=OtlrfMTjIlIvJm1fdQfuo3pUQfR-sdSTGxHcySGg-IVWlmXpyZjQwOSKDAO3gTIXCP1WwmT52jIikelj-cLzy6_6PB_jQj6m71KScfGNS3LA-2xd5nS7D9CYNUlqgAAKuRIS82XAVc6Nqayyxb2lY2znkd4m7fjmSfTAj-zMlkJa54eVstcabH3H3WU2DsVwBb-xKumwS0OAMghvsAbcAymJ1Q9plKB-Jes3h-kj6JKZyjNtrnXsl24CxELhR7wH1j7v7aG9GL-SKuOvURAE2wcO1ZpqWYeUB59_lYMvww5HLAgOMPV6aVZ9cY70WZUDNtqT8TIN4qP2m70eunCSnzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEl-EmXp_4mOrsLECbyA2LX2h9NimHN8sQgiHX_UTKsJebmIHs2JmiifACQRoj-6i4Wph1ZCH9tp_anIBXCj1wvKmc21JdIwB1tDtuAxmgAis7OvQ7w9DQ-8HLHR2gNNVaZQarjrmxwEz7KH_9KAi4cS8mN4KDCEbuad1FSotYkfAeF5bsExRannPt0aFBoQmc-N4sTwyqJ-qCE6Hh7Kz-a-AGGhcVEXZDkcv_yN-OSIY4de8Dx8l5GNUIPIbFjAPMR6JKAZ4Tj1qVysT-rnpPONqjdJU5RHIpCS9QLI5MFXgGxl9ZOIl3oCq0IlwsCj2ILSnJW2KX0qjrhGzYznWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی ۶-۷ جمله نوشته که خط به خطش دروغه!
نوشته که مصر یک شریک مهم منطقه‌ای برای ماست و نمی‌دونم امنیتش برای ما فوق‌العاده مهمه!
در حالی که مصر و جمهوری اسلامی ۴۷ ساله هیچ رابطه‌ای ندارن و مصر حتی ویزای توریستی هم به شهروندان ایرانی نمیده!
همون موقع که پروازهای جهانی در اوج بود، حتی یک پرواز بین دو کشور هم نبود!
نوشته که اسرائیل علیه اتحاد و همبستگی اسلامی است!!
مصر حتی برای کشته شدن خامنه‌ای، یک خط تسلیت هم نفرستاد! براش این اندازه هم اهمیتی نداشت! کدوم همبستگی؟؟!
🔺
دیروز به دو کشتی حامل گاز مایع در مصر حمله پهپادی شد، دو تن از مقامات ج‌ا به روباز گفتن این فقط یک هشدار بوده از سوی ما.
دمپایی پوشان یمنی هم گفتن کار ما نبوده!
حالا این اومده میگه ما روابط مهمی داریم و همبستگی اسلامی!!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5XTdZbCIYkSNpLDq1nYYrJGToLxdFwgo-hhuBaz_GN1KrxQZRbVHFhG9N56DqtA6bogF4irl0gkSiw4GMc6sEmMVAIt6zyl6pkECVvUjNojwzzrP7stLJjgvWE4Gjm_9WMR7y9E5E6g-eCvLsXcs3wcBTRKH5RJI1qms8rOZXVp91ix09PJmXSoZ_NcRmqEriAWS-WAxmEcLVNAnNTNbu5zEGucoySMPJoca2DsKxf8feiZ0WFOnyA7KnUDFuLp5BL8vYjtdw8LHQcXWXvP8pN21wKXzfgLCVgsVR36OJ8NOMQdCirQ7f0jwYTYIZiWuc7mTNewQlS64705Lkx4EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DatQi8jv2ZBb-gt-3E-ssK2cueV9VzAb16CRX28pPfvdylz3pbJ1-ZyfA2OlIyrrxZQh3u5UJH-BBlizvWui905mGqGoLq6AjP2bHDOAR5unYshgfpcQYcQPJK-Am_HSEmy2TdgO6crC3ItayJ4UiSB1oSL_QRF_7Xhwu6dAaccHA5CCWVeVGPwXwIahK_o0NY081px9ohlZ5jO9FEa9FRz_z_lZEjpawQP66ebb1e1Qj0vuPkzaqHIvTzt7Kc2HzVEw30yWDu-FD3TIARLOZkKVq9Rcda-R16ybXGpwGF4BtmQMQex07qKwVeAWxOrkDN8O-pMMR69y7DGVrng96g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵۰ هزار نفر عمدتا مردان جوان
در ۲۴ ساعت
گذشته وارد شهر ۸۰ هزار نفری
سئوتا در اسپانیا شدند.
🔺
احضار سفیر ایتالیا در مادرید.
در پی انتقادهای دولت ایتالیا به دولت چپگرای «سانچز» در عدم کنترل مرزها
و درخواست بستن فضای شینگن بر روی اسپانیا، موجب خشم دولت اسپانیا شده است.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6442" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V799qT9WPnn9xDSfeixFjHgM7ud826do_5drX5zjspnDU4aBiPDgFEazcvlbocwl5bUKQNCZlocLnT951JLj60pru4UAsOaxriJLnAXJiiytJky_PN3dKqd2eHmBZt2CWgl-63kaV1S7JSJHqxQ5oFGY7tOsig4p2Yg5A1QQRGwLyh_ZdptDOAYsqnDscmxITkplmRs3xaBSLlsoypTvwiho1HyumV5Mjf42xuhqN-xXfy0cbbbhnw6kDXu62lmOSlunkyM-Tb90eM9eIw9VZg2tLjsTaGNko1B4E2aJyz5DtUdbcsu84I6-xqD03RDyNoUdTmg13sMG5HcBjFQaeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه بار هم درباره حجاب نوشتم،
در حالی که اکثر زنان جهان اسلام
(نمیگم همه‌شون، ولی اکثریتشون)
دوست دارند مثل زن‌های غربی لباس بپوشن و…..
زنان غربی هیچ تمایل و انگیزه ای
به لباس‌های زنان کشورهای اسلامی و چادر و مقنعه
و عبا و نقاب و برقع و پوشیه و ……. ندارند!
نیاز نیست حاصل تمدنی که اسلام
و جامعه‌ای که ساخته رو در ده تا کتاب قطور جستجو کرد! همینکه جمهوری اسلامی با حکم
«۷۰ ضربه شلاق» و «گشت ارشاد» و بگیر و ببند و پلمب، ظاهر حکومت و فرهنگ اسلامی رو حفظ میکنه، نشون میده، این تمدنی که میگن،  یک آدم برفی و یک توهم بیش نیست!  که به سرعت آب میشه و میره!
فعلا پول نفت پشت سرشه و بگیر و ببند!
حاصل ۱۴۰۰ سال عمر و ریختن ثروت و اموال مردم ده‌ها
کشور برای صدها سال به پای این درخت، هیچی نبوده!
نه هنر، نه علوم انسانی، نه صنعت، هیچی!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzhmzVnBnz8-Jc2oTN9evSjSPEJq-5SYxcLcutad30vXDyqEpTtv1rX68pR0JMoX0Wx6mC1ydvpumE94Vm-6hmGvJl762km8WFhKrRy1iAaZ47c4CV9esEYBh4JqsEjQnaeyKs9EXoC5t_TkvP1Y_XhwJ57uUeq78b_qgR-jM0gviedCIdIfWBtykhecxNenJoHhnIhYti8JVoyj7_kbCd_nX-PzOgVmp2nZmIY2eBn0pl4QlOeb54Jf4-nW6KkVyvCQAfRhhmsap3W_LvQO9rpPF9L3wod3Hd6plmYe1k7ikuJhyzcdDXNP8i1U4_KMOaKIBDLqxm85_wTrPCO8Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=IG81s3RiW0JX8b6zR3vMVluZoVFokz1nDaEERo7NeszxoJvpKOf4ia9LuTFsLIIc2iPmKpfGxu28jaingcnsFqMJmmmkbhgSTgiH8LPTnPtQjNtVEUz5DWdXgdC1Mc9COqGbnXQU0Oq-nK0V-35n-_MOyMTJnqgD1kA2rtgFEu-Ehbjwd_kLf8IGEViFNIujpWmxOyAwFUCmokDHH4JPo5akZzYiF4WWqA4l8mnuR25frIsYjScdblhnJ695l71-tFffpnxigHH4eTE049_hBGgu4Yai-3ZyioIgSylZAxQtXBoZVenoY0j5bvConJD7reXxevybQQFXY2zrvS9dlXkuC_6qSi1IL5IDdoi8n1zwz7_XTpZX0qwf0LRv2S-WiR6ysNap-6ZbSRJ8mhkwL1-f-MgBbMBKuYiETpocxYF9pGw3uy5Gp9jQk1yYGatLq4XeMsFoksCUKgpWqAFcyK9Y9vjctD3v9UZpFcwAUd2DEc5Vfhv-91AogkDxztzv5pgq2AOzxj2oIxc2x7JdzKPyu52493qR6T7jgWL742PoI8gfFhM9aHwZeE8U5jfykCJRB7FNImbPH9tYw-bZESlisAx5HljHQ3Tynw5SpSqm6GWH7ISBryXuLAR7BJq0U7r967GoQEHskTR4K92P0BiurHviNph2t-7-TlDD9nI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=IG81s3RiW0JX8b6zR3vMVluZoVFokz1nDaEERo7NeszxoJvpKOf4ia9LuTFsLIIc2iPmKpfGxu28jaingcnsFqMJmmmkbhgSTgiH8LPTnPtQjNtVEUz5DWdXgdC1Mc9COqGbnXQU0Oq-nK0V-35n-_MOyMTJnqgD1kA2rtgFEu-Ehbjwd_kLf8IGEViFNIujpWmxOyAwFUCmokDHH4JPo5akZzYiF4WWqA4l8mnuR25frIsYjScdblhnJ695l71-tFffpnxigHH4eTE049_hBGgu4Yai-3ZyioIgSylZAxQtXBoZVenoY0j5bvConJD7reXxevybQQFXY2zrvS9dlXkuC_6qSi1IL5IDdoi8n1zwz7_XTpZX0qwf0LRv2S-WiR6ysNap-6ZbSRJ8mhkwL1-f-MgBbMBKuYiETpocxYF9pGw3uy5Gp9jQk1yYGatLq4XeMsFoksCUKgpWqAFcyK9Y9vjctD3v9UZpFcwAUd2DEc5Vfhv-91AogkDxztzv5pgq2AOzxj2oIxc2x7JdzKPyu52493qR6T7jgWL742PoI8gfFhM9aHwZeE8U5jfykCJRB7FNImbPH9tYw-bZESlisAx5HljHQ3Tynw5SpSqm6GWH7ISBryXuLAR7BJq0U7r967GoQEHskTR4K92P0BiurHviNph2t-7-TlDD9nI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnBemxJnbKByS4PfUXt8B3hQkPKKcZJIjJc7GNz9BZGj95upczx3wDq_FCVp18CrECAldclSyN9x3GlYsp9i8kbnoDkljA7bdNy7cRNz4pIeTR-Rz1rLj1rSLq_U8Da6yFeYx7Ud2DnNbHCBrbQ8SRSro28vtYtGCZiGy2s4sGc6sBZWbzkfSSzrGmuBT22VYb64WR8kkTkauz-z3qsi0SdpYOzAg1nMVDI1sE1j-4SH9RbJdTFHZNz8z7EHOOQBY68y-m8P-Tzu7hDXKPhw16mj7y8Ng0yuWk3myNYp45aGXPLPCGXB1cCgizv-CvsDjJK2GDlphjUkRV4LeCBErXJ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnBemxJnbKByS4PfUXt8B3hQkPKKcZJIjJc7GNz9BZGj95upczx3wDq_FCVp18CrECAldclSyN9x3GlYsp9i8kbnoDkljA7bdNy7cRNz4pIeTR-Rz1rLj1rSLq_U8Da6yFeYx7Ud2DnNbHCBrbQ8SRSro28vtYtGCZiGy2s4sGc6sBZWbzkfSSzrGmuBT22VYb64WR8kkTkauz-z3qsi0SdpYOzAg1nMVDI1sE1j-4SH9RbJdTFHZNz8z7EHOOQBY68y-m8P-Tzu7hDXKPhw16mj7y8Ng0yuWk3myNYp45aGXPLPCGXB1cCgizv-CvsDjJK2GDlphjUkRV4LeCBErXJ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=rzO_JZcIeDVVceCwXL7m8Vgi3ZjjVfv6tzLU9rxQPjmXze1fwqUvXllSJHOTqdIhc5Q_F4aY3A2Phftr8mLC5pCTFAwxhx4_2PSOPEGMUYpr86ireftbu32rDpA8Wk8DqrJazqiD4F8cihUSpNi_f8HZMAbziK89k5ayl3fP2vD72VW3hs2nGqxxZ5DCSuySOPCtYtfhNo-WIHKKKFRsvFz_v_AmsLPuaftW1L19YIJYDkb-WGQXD73bOS3X64LW7qbTF28s8yntO7shlKpgRc-pmpPqCaLz5V_WYXvjr6a8hBzPjEW44Acx9GsiKi4SCARC3MAF5wZsqK4aE-diTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=rzO_JZcIeDVVceCwXL7m8Vgi3ZjjVfv6tzLU9rxQPjmXze1fwqUvXllSJHOTqdIhc5Q_F4aY3A2Phftr8mLC5pCTFAwxhx4_2PSOPEGMUYpr86ireftbu32rDpA8Wk8DqrJazqiD4F8cihUSpNi_f8HZMAbziK89k5ayl3fP2vD72VW3hs2nGqxxZ5DCSuySOPCtYtfhNo-WIHKKKFRsvFz_v_AmsLPuaftW1L19YIJYDkb-WGQXD73bOS3X64LW7qbTF28s8yntO7shlKpgRc-pmpPqCaLz5V_WYXvjr6a8hBzPjEW44Acx9GsiKi4SCARC3MAF5wZsqK4aE-diTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lN9x4zpdhILNlP-Oj0DMitpoyGzMFcbDNKUDT76bcAwLjNqwqEMN0Jq66-INuOOt0rm7SkxNHJGwSxykjZ7rcUOpK19hPo2OkhryHewca4mRY8ZGfqHKKFhbDpX4xI7bx-IoAXacOv7puDunn3tOUGefNL_zv0poXNqAekKpgFYLd4xzpUls5opmyocZTRZTn_3pQJv56wXe_fj_RoaYQ6rfGOyVlC0j5T6kyJzHHbKHtUMyItXKovouhGTQoA1yfmg_I-dQzicgTqyahhnFrnKlRE0drJmmvUR1VCeGdDIywTTPZjA9dv9afdjjs-e4iglQAMYnG5hKE7kPt0E0qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUMGdFWXkFtzpqM9s2EXWifnatF8rX_zLuu9t-DXoQy0CSwn8QS3Oyag5Fo6p21pUlMLutioKEplhrPhkQFE0nUclvPvsBSktBgWBnNugfeIY_XOc3QFMPkyNBbu62jA8f0qwxyJIuvyPbzbjSFp2XlelanzxmcbhG8nRtRmzoj17dU9nZMJfacJ2l3_NXl_xnwqkf9G-n0PlUV4P-22bun8ur6v34Ka9rKPI2xYKplK7SKGFmafPBRRiwDyNJzd9Xe8qmdthKKAcC5j_sWr44ArQv-ekRk1ue1Qy5xIf1_bIWUvK3hSC4eJnjdTQQD2xECwdf9yAkkt6xK2IngJUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=NzD2RS9vlurlg48p3MCpuY08-mt4fkDV0L5UO85LwWfmcrdv_ZQMXa2qL1yQAuWSQKKgrUH5oFlcAdP7-Xlsg7mtZDVLQTc_5QyDFPetvuTocoLO4EPJkWEGaKovn9rgaFc3SDncZfpOj_SiFS0QUAHpZoEy8_y76CVooiOSVmTDSxLm_7DwWiKHHvDkrppQzpviu5FE30a94gEbqPJ3wZQa4t1u__wFMmzNEfC8T_3TEHi8ytMbyZGkd1DeOCyZwT8ic7V4Z4tIGCPq6FZWrjfmYlLUJ5g0cd9qZljfXy73eYGyW4_dh7gWH7YJ3hS0A2UagGLBlBCzwKp0kvX6Cmyw9uInXDLDXEucBEbN3AbaqE9_fRgSvQNbBvB9N8GInqulrUZ1f98Ko25Ve_xn-JOQn98EStet7b_JfuMbVZ_IjLyZUGisLHRpGvlLz6Ydd5h9mNuEcOI1P9miCUAurvSUWSYDs7-IcuEfsnmpPpNwIlwmDtHrSDikZ6D12b8y0JA_ZjMV7RYbkljCZtHbT_A2iRnJaR5fw5DyhPfkVLiVhwbiQjNoSyk9jTZDMqdVWFLkILCAHoN59ORAFav_FY6GKx_6CgxcLpD5L04hdV_EFmMxAfCYqlnDpe6gHgGeQ-ko_RRzWUy6Hebt2lJDC2XbLDy0TKDzZ6drY7oxcis" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=NzD2RS9vlurlg48p3MCpuY08-mt4fkDV0L5UO85LwWfmcrdv_ZQMXa2qL1yQAuWSQKKgrUH5oFlcAdP7-Xlsg7mtZDVLQTc_5QyDFPetvuTocoLO4EPJkWEGaKovn9rgaFc3SDncZfpOj_SiFS0QUAHpZoEy8_y76CVooiOSVmTDSxLm_7DwWiKHHvDkrppQzpviu5FE30a94gEbqPJ3wZQa4t1u__wFMmzNEfC8T_3TEHi8ytMbyZGkd1DeOCyZwT8ic7V4Z4tIGCPq6FZWrjfmYlLUJ5g0cd9qZljfXy73eYGyW4_dh7gWH7YJ3hS0A2UagGLBlBCzwKp0kvX6Cmyw9uInXDLDXEucBEbN3AbaqE9_fRgSvQNbBvB9N8GInqulrUZ1f98Ko25Ve_xn-JOQn98EStet7b_JfuMbVZ_IjLyZUGisLHRpGvlLz6Ydd5h9mNuEcOI1P9miCUAurvSUWSYDs7-IcuEfsnmpPpNwIlwmDtHrSDikZ6D12b8y0JA_ZjMV7RYbkljCZtHbT_A2iRnJaR5fw5DyhPfkVLiVhwbiQjNoSyk9jTZDMqdVWFLkILCAHoN59ORAFav_FY6GKx_6CgxcLpD5L04hdV_EFmMxAfCYqlnDpe6gHgGeQ-ko_RRzWUy6Hebt2lJDC2XbLDy0TKDzZ6drY7oxcis" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=XcMWmXtIuAdMv6zfqtO7lWW3H5ZIMNCyHyMsSyzzPE3k2rtJJS4e7W31n4E7ex87DHjFAT-TyIPOdquG9VIBdQHRsnearElAj29edpVcsq98dB4zsDJcowtWa149l0d0Z-0HCrCgRee9rp_veQS3YLfUPnBBg6q_b5xbQSADqBVwFD7-LtBi8PCcxCOrJZoiZ11wY0raf-aOG5VeRy7PhaPFHckGs_gcd925mDnz7rRlouoePULH7YRiGX2iGMIpB6d2lUxe8wnJGcU4xs_yQoCGkS-CC1M1FejEMv_08YFrOT7G23tLEYzP62CbhvOcxjvSZ7mz4b6l4hBE05TIGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=XcMWmXtIuAdMv6zfqtO7lWW3H5ZIMNCyHyMsSyzzPE3k2rtJJS4e7W31n4E7ex87DHjFAT-TyIPOdquG9VIBdQHRsnearElAj29edpVcsq98dB4zsDJcowtWa149l0d0Z-0HCrCgRee9rp_veQS3YLfUPnBBg6q_b5xbQSADqBVwFD7-LtBi8PCcxCOrJZoiZ11wY0raf-aOG5VeRy7PhaPFHckGs_gcd925mDnz7rRlouoePULH7YRiGX2iGMIpB6d2lUxe8wnJGcU4xs_yQoCGkS-CC1M1FejEMv_08YFrOT7G23tLEYzP62CbhvOcxjvSZ7mz4b6l4hBE05TIGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBsDbGd1g6EeHYf7Rw5SDTYswgZ8-q41U3sWQ-vNhuA3PL_CZAJEMsWmV2uA54vFVy4qv2SydmieDHcgzM5rDUpDX6jI_mtbGIJ80t0wT3zTSfjUyNUwbw8qbokvvSrNSnoO_6UM_g50yOCxEJpSuO91lhgaBFhj80CGvyCExscn27k3G__yOV5RWwY-LcxIXv-aANW3-EmCu_g5KufXfB4STMV7kfYEYnY-2rsWIdehYD7El0PRBZ3Yarz-yjrPPSLYGGcNesjJ1roPfxOCVtZmPsV_F0L3OO-CN3i2YwWdYT5Rw5E4ZBeN2F0PJXg6W3ktSVDeFe0ZIw_pWCWCsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P_cM1C1YY5SZyVAHF_zV3sKSCewhyJH8gBpJtNTqqHA-nq7PiRYxdn2G4ZBYJVpHHIQo538Gq62xqi1SWzGNgq0m6nO1e4hed-6wgYcPuHOch_R8ylvep1ImxA9w8OvWq-zJk_WuIf7XGVJe9EsAN46GDy8M3DElXoNpLdsQeyO2kvJxDZL0CoV55upIrzZ4s5FzyMUKy6iafP9uqd9hsYGCxNysGGqgmXRzjWpoXdJJ1NJflyu9vOb8CCA0dA4f4sOl_gWjHlBC5wQp3-FVokH_7kDXdrz7-5JrZtHJgVoZJ7rraiwhHdylqolrK8gqqirfhkPaio8AonsKfhIn9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K1HeID0ssM24NMohB90VmAEaqhX8Ouas7w0gM3fc2OKKznGBfEhmrc2na4W_JCDlNbTPwGAIkDk9ZzlRWIa29kSdUNZjsGJy1deHZo6emI6KJyVZvqcTuYD7TAjN9nN_CbHlqrzOq4lSfmpuYe_g1p166iyqU_Raqjk7pvksllATU_4Jgn-sMfUYdH20V880oOu2HzeCEvOPpb_erPqpfRLcKiUw6lTzkAk39ZsyR1SKHwgSiJYW_tyeOQz7uPMZg9nQd9x-gxgE84yp-vlUYajbwKP5FS_jl-WkgyegFY28pzNVsGOdlfmYdHzl6znmdnWCUBsQ3x-7EjqzuBBLcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=dbq_DiXE0DJAsmtbss-tG_9s3jCu4bTTvobVAsI_dV9SWSKaGwF5QPlAeZC0tmOntmyFln-wRzsiZJEsaY9OzJIDHy2Fy0NPhHGe40Go83xOMd1FALMRKnCTfQRLuunYJYGpS4KlTYmi06bV83NFa-4-7J0dgeso8rJcz9MfOBMecIdNH0t5TrCo1CftAPU_u2UAxTItoak97gdDFcGUYVsT_NGPy0gNg2wBONCO8T7jIRfVk8IEg7HGwDPSWeMngm73KzIdq2A6OrTNST2p2CJDTfohjHvyOXvufZGpFBw88XntLRMwat1PalBQKEpFSmzU0icTkXBYNXpyCxAI5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=dbq_DiXE0DJAsmtbss-tG_9s3jCu4bTTvobVAsI_dV9SWSKaGwF5QPlAeZC0tmOntmyFln-wRzsiZJEsaY9OzJIDHy2Fy0NPhHGe40Go83xOMd1FALMRKnCTfQRLuunYJYGpS4KlTYmi06bV83NFa-4-7J0dgeso8rJcz9MfOBMecIdNH0t5TrCo1CftAPU_u2UAxTItoak97gdDFcGUYVsT_NGPy0gNg2wBONCO8T7jIRfVk8IEg7HGwDPSWeMngm73KzIdq2A6OrTNST2p2CJDTfohjHvyOXvufZGpFBw88XntLRMwat1PalBQKEpFSmzU0icTkXBYNXpyCxAI5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=j0wWjxWBZ5BjwjuMxBHsAMeo02q4sswAZjUmVldeqpHB8886mBojGXm7C6UNUBGh1PCL659kvt9EdCsrV_McOKGNBCtiod7DaE9zboGdg0uFOPkv9YA7RezMNfSi8-SiUvOYsC-QmehThqcqg79bUG00xcPg7goTq1aQhiZlQNVBrpxWwUxNajpoi4bFGnONwfEGTsKdHKrRWXCTatITy0NK2QUtsMoG-s_1GVFgi4ilZY1wfkZJjU16oWs5o-8yFhTvWAo9bh_6nivnpqH354w0VwvrjR2XCtkqy6Y215PfL6-lHZ_91S-U7dSHCb4S4VUNxmhEqeeddR1mJ_tFYh_6-WEwCsqptHRs6LZilb6Ui_9nNW2K6b8HnAjPPk9N0yvpwDnud4dsX3T8kUs451s4Io5-yz9oeZukRjNLIOauRDHyyc4GcWrhTewJ9XlvwN34Ofhuo4XClwQISMsN5VDG-Q1UYV4kz6XiarQaUxRtVL-CGuwPhX6sCzDLYkU2Y0sLUBAkuvq_jqqXWW0Cbt4WcRsGoqcgUM7yPJvh6WKyYluDzeLloanjMehbRswxrKVOTu8esL_cEtmM1j2zLApjITJZvnGQw9C0o750_Vhf0JhwKyuyt_973SJZsK4kDZJDw6pDaKozLN8ZxQfomoBwNxip3OlGSdO3fCzOogI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=j0wWjxWBZ5BjwjuMxBHsAMeo02q4sswAZjUmVldeqpHB8886mBojGXm7C6UNUBGh1PCL659kvt9EdCsrV_McOKGNBCtiod7DaE9zboGdg0uFOPkv9YA7RezMNfSi8-SiUvOYsC-QmehThqcqg79bUG00xcPg7goTq1aQhiZlQNVBrpxWwUxNajpoi4bFGnONwfEGTsKdHKrRWXCTatITy0NK2QUtsMoG-s_1GVFgi4ilZY1wfkZJjU16oWs5o-8yFhTvWAo9bh_6nivnpqH354w0VwvrjR2XCtkqy6Y215PfL6-lHZ_91S-U7dSHCb4S4VUNxmhEqeeddR1mJ_tFYh_6-WEwCsqptHRs6LZilb6Ui_9nNW2K6b8HnAjPPk9N0yvpwDnud4dsX3T8kUs451s4Io5-yz9oeZukRjNLIOauRDHyyc4GcWrhTewJ9XlvwN34Ofhuo4XClwQISMsN5VDG-Q1UYV4kz6XiarQaUxRtVL-CGuwPhX6sCzDLYkU2Y0sLUBAkuvq_jqqXWW0Cbt4WcRsGoqcgUM7yPJvh6WKyYluDzeLloanjMehbRswxrKVOTu8esL_cEtmM1j2zLApjITJZvnGQw9C0o750_Vhf0JhwKyuyt_973SJZsK4kDZJDw6pDaKozLN8ZxQfomoBwNxip3OlGSdO3fCzOogI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKoEaCL_LWXQUv3dK7s4kmlF8kBJLqHsKmT3zrWuRU7VrYO-X8MxJEUopyQMxRYyyckkDpH41AhZLRG3CqWv2yvMlMd9cYGbGV-Kf6lw-jgu0dcLOexqqvumUt2RElblLZAcxhmxtPeQQ4c_RoMOUxyuUdhKP1k55vQFT_DnDR12pFiPRbYWS_lT6XzZ_i23N6zw8peUizYh88gfE7-Z38vzZg1xrUsRP5Ay2ujC1mzXx7vLDnokORSpLwSkE7TGbkF9bsVYWvKsn5IWhksW4dtupijwsH5zTf58Ovmrf8w1n2B2UlAJVqpHKsnYpFpDff_hfv37a1-v-Umu3YzE3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlLV1E1b5Mpa8orddzXLMimRox9G5O1EGi4dRSRf5NASqCs27wO80pIC4ZFHkvIOGrsRZa29Pbi2e4Y18UYGRA8nIXdo9G-LQthcQJY1J5XTHglbT9b7VKmdtfQyvSFibFmRjH_uN-VAKUA8JtRSaIFFrPAc_XJoRN8wD3XnWaS5aDKxdFTAilL0VuG6KKMahvzhYQeEoU1kHAiX_nk3Gg1lH5MNEFkE5my8RhAdhnMhKM6dzLW_HjEXoskqgbdmeLgJCne33I176YuMCJLiPPO4K08UVfD-CAuFMcD5KDDexXVUgJF--borxUIQvK3V5yfYHqobObHQkdH2tOz6Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=AEODWjGju4waa8jyJHJ2RT_rXtCrou0SCzjS6gWuBXc0MNVyiW-JkhQnThy3gPH85JmCHbPOPaGP_y8k68zqsEiMxgFaBQx6w4Wtgzwf6pfJfnd2qACj8mK7prgmKIdatHBL4YSCv6tRCkD-_nMJSIq4EoR0M0eNwN01cT0ybdTBzP5E3Q1fxnA7W3bL7ClsTtV9PNnE87nFEglN99026ze6qAIYLetv046rtM0CiiFfB7NHwtWZXpxTqaAXWhWahM-F8QBMXxlMDjwRV9JunUg3fFIiZyF3Bj7iG2Zrgju8BE1LbTkE_k6PZqhRWqEIDdQeg4Z-uXhgRuaNFpT9fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=AEODWjGju4waa8jyJHJ2RT_rXtCrou0SCzjS6gWuBXc0MNVyiW-JkhQnThy3gPH85JmCHbPOPaGP_y8k68zqsEiMxgFaBQx6w4Wtgzwf6pfJfnd2qACj8mK7prgmKIdatHBL4YSCv6tRCkD-_nMJSIq4EoR0M0eNwN01cT0ybdTBzP5E3Q1fxnA7W3bL7ClsTtV9PNnE87nFEglN99026ze6qAIYLetv046rtM0CiiFfB7NHwtWZXpxTqaAXWhWahM-F8QBMXxlMDjwRV9JunUg3fFIiZyF3Bj7iG2Zrgju8BE1LbTkE_k6PZqhRWqEIDdQeg4Z-uXhgRuaNFpT9fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zl2s0DQX3LXp5qotF3ToJ8rAhLIiZ_jUDe7DpHcXJ41U8ZTMSmbdklgf_WzLpmZQjvCg6wLR2yfumXllWASbVsLRvkdghtoFhQwzoLtvZopfo5oNuDYzde1z-jWC_u7uJDFbIdDj2MsE7ZhI-pwHjVwPX3IPGDxfrAZMR2XPPRwuV7vuzx855oTRK97AH8tQDJayO7duHKbD_Q7HxelFGaQ-PYCn3iwvjNIgvrY8izuSrF0tlbxZ6uaqS-8dYPYCofwDdXCe8LUrlQl8BtLjrCdVTRPliP2wEYo7mxnrqM1WDcfTktzVOFEOmVMupI-Pa4VYnqd9gAqYO6Dl2K151Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دیروز جمهوری اسلامی با پهپاد به دو کشتی حامل گاز مایع در مصر حمله کرد.
امروز دو تن از مقامات جمهوری اسلامی به روزنامه نیویورک تایمز گفتند که این فقط یک هشدار بود.
(که علاوه بر تنگه هرمز و باب‌المندب،
می‌تونیم در مصر و کانال سوئز هم تاثیرگذار باشیم)
🔺
صبح امروز هم سپاه بیانیه‌ای صادر کرد و از حمله به دو کشتی در تنگه هرمز خبر داد که قصد داشتند از طریق آب‌های ساحلی عمان از تنگه عبور کنند.
🔺
دیروز صبح هم به سه کشتی در تنگه هزمز حمله کردند.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Us0H5XEG-zXil2N64XApiJYd7W5Q5nDODGvO0uXVsdAunbUm4sj7UU9fG1D480OMj3OfHHemGLfQICAVjlH6s_2L6iy_mm8wZ1y8BoE7VctSPq62C9EpCBkrhGZ-GrJgZUszO_nDquCCntAkrwM-jZFXgNHqaAsnrdkWfV-1_h3X6eDXYwDyWx9NbJ7iG0czvOBTUosgeTEbsEYT82aS2SN87bY06kyuD3y6IrgNPxwmK2tfDGczmdELOtTK7CJLpRxQAExa5PV68PaMkWarSXEX5nxo_6pbjm5LvFXG-daC8LBhsKCvTIaA0tW_W3gU2lxb55ip77SNUkbMSVsRdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی آمریکا
به چند نقطه در اطراف آبادان.
شنیده شدن صدای انفجارهایی
در قشم، بوشهر، کازرون.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDco9I3Cb2RRX6ZeVL0X_d4Ix7eolU8sS_yarv36lMrEN5YQczhrNEf31RU8-povZbvtfbXlwC7m0-y01eCFbW3ipOzytKmeovdw-c7MPR79jxHA46w5U0b1__S9xF-RbAmvAlNDQWNSCIiKUWRjA5UdK5GxtlHguqCKHim61tmgFxj7UrPeZL3sdZxxQ35T0m73DRVQYXIp48bRMTkON7aGntzYHDUbJUv4kUclm2JDHhdXntKy6_nmlkexXgLTymckxrNWFkXOH9z1eTTVd22C7k32M1TBxDD6Xceq3y2ZKyUnUfHbMy1SPTpfiwrBoz6JwhbJrj0CYQcdta69OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLWTEDroNKamFFLoXzUlLcGHsIYarw9J0yZoPdEfoqqNSU2s2cN6jrZ_JXN8m8N9UnT2ugSritXGwgNLaP9Ai75Gjsc-m3FtZK8aZZbiO1gwP0HBqR81Win25UupfOd7tmNsBXDY3g78Fth8Z48L5OaKmlIA-b2o17xuUU-fDisUHzlS2H3y9CWK4fEoqMqhhYxNjBXmCz0HtxKeMdrnTNqBHdeR4c9a_VHl5X1AKIhw3Zpwek1B0SFwETqrBgwNST91pnXmVW-udHxzXvLhTh49Me-Y8ScbfFDqL0LoL06FJdsBYqlsODXccvE-dDClyQCKC84_Zpg8cylJvgkZJKIY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLWTEDroNKamFFLoXzUlLcGHsIYarw9J0yZoPdEfoqqNSU2s2cN6jrZ_JXN8m8N9UnT2ugSritXGwgNLaP9Ai75Gjsc-m3FtZK8aZZbiO1gwP0HBqR81Win25UupfOd7tmNsBXDY3g78Fth8Z48L5OaKmlIA-b2o17xuUU-fDisUHzlS2H3y9CWK4fEoqMqhhYxNjBXmCz0HtxKeMdrnTNqBHdeR4c9a_VHl5X1AKIhw3Zpwek1B0SFwETqrBgwNST91pnXmVW-udHxzXvLhTh49Me-Y8ScbfFDqL0LoL06FJdsBYqlsODXccvE-dDClyQCKC84_Zpg8cylJvgkZJKIY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sRJ_QnFdKmDOcjaszf7Wr02j9KAG4uj03j8SX6825npAj36dhsMTCDrFBhvHbte6bIc_v1CNMXxiSbI90ijrbsPbuGkBjNKjUVZ-BI78vcIUgiPgTrjooGfCqm7zRS2p0BhiPzJw5jCJQLi05_dpbdCfuxaQFENaXe5n2LxXHas4I_zSzAMs30aJYjImw2anu-4jwZVG_UHSxmQN8yGuNwnokITWP7kIbmjIEcVrdU0gb0acrtZv1latHuGxbwNAbXwdNCT0UFa0VVt9s-B5L0ota8hN8IQivNyYmU0BFmYbzbs7JUWRGrgmpz1MeE7heupJtALhNNYcgGHSeMNDfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V4zbR82bQXcynckpqSCeej5kypLHjgnGmRt1jNkPKCLzM50iqe0x3HhFVA3ikkonFUaxkBathPWX2WXr2rrDxPt-hVKRIuKDg6L7Kd1oen0jpVGbSam0_djhVueDPvmR2qljnevXrsg_vCT5Bga-XkdeVcX3ChZF_zf0aDIdp04CzlH1osLAYmXAUvovmt4vJpZPcsIix5rJUcCZaQj07B-BX1XDqu4TL33pVD4UtC6GDQylraGcrDK56ObMwDrUtpGCxbSGSISCxg6kkI6GDOJDrQ4qGXeA9OXKrTAsPEi5U4qj1GwPCxwHwRR6Oj4p2Onet2U-tYjKTI52kCt5vQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=R1plC0PlZcFtdSAwG4n3R7dOgzEqEvetWuWPB3qcMgJoEFWDruAzOaeAMHMqQKDsq6bWO4k69yKSzGpKcxW2IRxFiXL9DE1M6Fvf91JLXhAORZI5sdCvbelKGcQmTx3iMz6iyRY4Hi1Hsn7nwg1SrXR-Dgi23zg-_GY_bprQmzHJFj6pcjmvZu9saQto5Yws0mzwNEzP94dZLO6xKrz-gmrtq3-JsjpGIwS-UZkhvLrSiJXCzANUY7Re-HbEjFB9bpeJHToZZdTNC2NWgCC2KYipjtCNEbSFaOCzWNjhQGDUdUexs43lhQtAnpCeR6hUUqbaxpNeekdcxFJAnZ0Wcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=R1plC0PlZcFtdSAwG4n3R7dOgzEqEvetWuWPB3qcMgJoEFWDruAzOaeAMHMqQKDsq6bWO4k69yKSzGpKcxW2IRxFiXL9DE1M6Fvf91JLXhAORZI5sdCvbelKGcQmTx3iMz6iyRY4Hi1Hsn7nwg1SrXR-Dgi23zg-_GY_bprQmzHJFj6pcjmvZu9saQto5Yws0mzwNEzP94dZLO6xKrz-gmrtq3-JsjpGIwS-UZkhvLrSiJXCzANUY7Re-HbEjFB9bpeJHToZZdTNC2NWgCC2KYipjtCNEbSFaOCzWNjhQGDUdUexs43lhQtAnpCeR6hUUqbaxpNeekdcxFJAnZ0Wcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=ss13pnSeYHH4hPAc_AHKEYOoVftcI_btgEfHmP3Srewnsji5Xc2gtfSbd8CRJf9bN4OzDnSMXyYS6Ru_bVXzoYp26CqL7cUXEJxpSZHOAuzJmP9SBSJXvrz7iCz1XfPiThG_lo8LydPcBUlfTkYenuFV263-pAOFduf5bz4aatCyTK1a8MXLe1LugjY5s7tYoGxQhez06lDhfLcvW23zMsUFUwwFkmv4-54gErA25EOpu-6iHcLS20qzb5XXPG4Egme1590wo-TNUJShGssj7rwbS9f-Ym7UT5lEi3xvgcOntDYkC18T0HwT_uhDnID93WAKq7itBUpazoJA4OvM7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=ss13pnSeYHH4hPAc_AHKEYOoVftcI_btgEfHmP3Srewnsji5Xc2gtfSbd8CRJf9bN4OzDnSMXyYS6Ru_bVXzoYp26CqL7cUXEJxpSZHOAuzJmP9SBSJXvrz7iCz1XfPiThG_lo8LydPcBUlfTkYenuFV263-pAOFduf5bz4aatCyTK1a8MXLe1LugjY5s7tYoGxQhez06lDhfLcvW23zMsUFUwwFkmv4-54gErA25EOpu-6iHcLS20qzb5XXPG4Egme1590wo-TNUJShGssj7rwbS9f-Ym7UT5lEi3xvgcOntDYkC18T0HwT_uhDnID93WAKq7itBUpazoJA4OvM7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoLDtrRro2IK2-IwqMAVfgpqVQj2oC9UBHOK9HRBzhx1j6DKVYY_8j67KBaP6oAaYLIqSBKYLOVo65vJiiSyXhg3QVKKpGxvDmpIoXBSb4-Q5Tc4YbzImWty7C1xncjTDTU4zu47-FY23801bPXy0HMswxzB6Ir_Fr-vdZiI9XBLefGVs7yv4dLfnVVkMqLEw9lTQardsCXk3Rpu1QmOVg0csBwAIc8JEZEg7xA-ttLot57K7e7VhTIlqqtHJ4T-qPY4q-4v8jHg7Dp01g2H0CMLg7_xmx0_qjWUf0snUNEdGP2J2_RP-KkjbBc_1VxhMa8hFbZkueSPbGYE8xNnEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lApwul-LJ0iez920zHwyKIIYpYcS5gbTK0vlJqiQ726a-l2iAgEOanrWeF1Waltj4OActAEGwuZzE-5S5bLy8b2brjblCFSCBisuqgwc1SmO0EOC0EbzBZMe_8kLCplcVwDixJCNzklJMFVnnHT4kzdfz6dc6aiRIDufsFBAniSEArXVbPkxyVowHqRvGblcMET52ctbSnMuUaThr9HmJ8Nvg5yx0KKoX7aJtODJC9LyGHHG-QZoRVv9s-EG3dXj4W3XrTAofiQHjKLx9K1EYJmN7LQ5rBRPx37DKKeyKlE6dKiudxNjJJrmG3tY32mqHMnJpN_9oSzymIvrMpF9pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی صدر با صدور بیانیه‌ای به شدت از «سپاه»  و «شبه نظامیان افسارگریخته» انتقاد کرد که از خاک عراق به همسایه‌ها [عربستان] حمله میکنن و موجب میشن بقیه کشورها
- عربستان و آمریکا - به خاک عراق حمله کنن!
این داستان دقیقا همون وضعیتی است که سر لبنان آوردن! از خاک لبنان حمله می‌کنن به اسرائیل، این بار هم برای خونخواهی خامنه‌ای از خاک لبنان به اسرائیل حمله کردن.
ولی اونجا مسئولیت دست آقای «املاکی»  - ترامپ - نبود، اونجا اسرائیل بود و چنان درسی بهشون داد
که خونخواهی و انتقام رو فراموش کردن و «آتش بس» در لبنان شد مهم‌ترین و اولین خواسته جمهوری اسلامی!
سفیرشون رو هم از لبنان اخراج کردن!
در هر جا و هر مدلی، تحقیر بشید
خوشحال میشیم
✌🏼</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6405" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=U0_RVCVNNxHAc2HVpdSs6pkdnEY8DJDHigmR1HPp87qiS7WpQB-7u1zPgUWrfvZTC-pkmkpDnvV_GtXVfWYN76MdRkF6dVQt-P-_26BDcBYl0rIQ1jtx8x7GiE9CpCIyAuOhlC5u5y8UrQ8c6ox7qVFBXbM2dFRn9nOS3kHEbaMvtPmoLMYLNN_6-3RNOXsTVoOqpRGEMsaO_PIfSon7cGoabxTHmCwwxwDB-ucyPNWfI--nYoemU_KlH0jmK4w4YF8XUcfbgad7JlGpV-ysxa8SusBbsFuJZbEUt9xM1ijW3ra5OrHiPE70eS8mRYt2wGWtZ9SNg16c_KFXC-KVCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=U0_RVCVNNxHAc2HVpdSs6pkdnEY8DJDHigmR1HPp87qiS7WpQB-7u1zPgUWrfvZTC-pkmkpDnvV_GtXVfWYN76MdRkF6dVQt-P-_26BDcBYl0rIQ1jtx8x7GiE9CpCIyAuOhlC5u5y8UrQ8c6ox7qVFBXbM2dFRn9nOS3kHEbaMvtPmoLMYLNN_6-3RNOXsTVoOqpRGEMsaO_PIfSon7cGoabxTHmCwwxwDB-ucyPNWfI--nYoemU_KlH0jmK4w4YF8XUcfbgad7JlGpV-ysxa8SusBbsFuJZbEUt9xM1ijW3ra5OrHiPE70eS8mRYt2wGWtZ9SNg16c_KFXC-KVCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا و عربستان شب گذشته
به چندین مقر گروه تروریستی حشد الشعبی
در عراق حمله کردند و تاکنون اعلام شده که ۳۲ تن از این نیروهای وابسته به ج‌ا کشته شده‌اند!
حملات به مقرهای حشدالشعبی در ۷ استان عراق صورت گرفت بصره، کربلا، نینوا، کرکوک ،
دیالی و واسط.
در ۷۲ ساعت اخیر حشد الشعبی بیش از ۳۰ حمله پهپادی به عربستان انجام داده بود.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6403" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=J9tASKnT63yQX2dsfuB-c80uNJHm2kMnXdwDstfuOLsxs2D_4Ifq1cgz8vNez4S-e5u3DtTTsw3iZivaUaVMRRoGzQuSwTYSLLBsTGHK7cX3BB9BdwHqFVP87R8-VrJGpqK-qfEmAJ4Nf04yXpekbBZk-jsFN1IGgstKHnzlXIfagS1bMAcvrp_1Dy6_frLbdlb23-NfWIdGThInNZvVqJ4Mri2WNQs3OHF4ijDFAgjv8UfqNQY6QhpurFc4KjbZ5BZf2pHWTvdJoU2YyKeUqw9e9v2Qr9yl4tU0FwwvSxEpQmnzl3UEh4Hw6xtmIYAyhBxNPkjAJKuF9nJbqwc2oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=J9tASKnT63yQX2dsfuB-c80uNJHm2kMnXdwDstfuOLsxs2D_4Ifq1cgz8vNez4S-e5u3DtTTsw3iZivaUaVMRRoGzQuSwTYSLLBsTGHK7cX3BB9BdwHqFVP87R8-VrJGpqK-qfEmAJ4Nf04yXpekbBZk-jsFN1IGgstKHnzlXIfagS1bMAcvrp_1Dy6_frLbdlb23-NfWIdGThInNZvVqJ4Mri2WNQs3OHF4ijDFAgjv8UfqNQY6QhpurFc4KjbZ5BZf2pHWTvdJoU2YyKeUqw9e9v2Qr9yl4tU0FwwvSxEpQmnzl3UEh4Hw6xtmIYAyhBxNPkjAJKuF9nJbqwc2oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YabudMf6hliZAVR3Kn6c1nVjkKQLE-4xa55pzZ2HIceWr_gi2WIK0aqTwy_buYhkKsSuQwjNhOFTlaqclLXBSSPE3UJGZzTBCCB54_M2FhK_A0GopJKx75mmFU2eu41OJqRZCTpoqNWOz6t0636Shus9p2tU7MA6vi3R0_8BKt0cO5b-OrKnZ5qaLt4s0RYysqirDcrRgLXYJ2zkfcK65-docmqywasveQKHDXrz_ZklIfQ_4sjrxUgklRTnuYiJkPnceI-YBM-fBp8z07ysHW7krOyFh08WKp0CqtdGrpJyL6SexxrwI9KkqZeDMAq4cVtQAJMnQiBxLn3f0yvFRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟
این تجمعات شبانه دست کیه
که هم دولت و وزیرخارجه ازش
ناراحته و گلایه داره و هم سپاه!!
کی بهشون یاد میداد که بگن «بزن» «بزن»؟
کی موشک میزد به ۳ تا کشتی در روز
و توی خبرگزاری خودش (فارس و تسنیم)
می‌نوشت : «به تیر غیب» گرفتار شدن؟؟
مگه معاون سیاسی سپاه در یکی از همین تجمعات سخنرانی نکرد و نگفت
: حملات آمریکا به ما «واکنشی» است! یعنی ما اول میزنیم و آمریکا پاسخ میده.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6401" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGp_C3APSHc2UioKBK68R_uD6f1XrrFz5sCzQukPhX84nB3dA1trfoyODVgfw2FlNKCwQmRJk7VCGyng2ihJZoPSPhJUz7GqU1JBierPlOPFih5TDJvSobgTMhQkdLqKPrF2fCfDB3HlItDSiX6cfC58mTB1mqIpWTu9IAwbCXwYrsu5d-Gb5rQkl5jxtoU4g9RsjIv85V-GOtdUJq589tINgbdBnQvQGXUiQHdr7WcSdkCt6a6k415KFK1MtdTqOnhZhr7OE3GmZT82wBhw2dRd17DiaFlXdkVEk0SNEkoU4OyEILRdo9_Do7FSVF7cXeijGPZo96jWrUcD5N8aXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ls-QKAJ-jm3tu584NTdmgL_ebXVuJxLqBxbR8sXDP2I2lr3NLAYEges3KkS41-kLgOa-7DZKDn4JZhppNwJR1CieMJ9oMrzK4fuQFHPuxDmcEnsrp8cjp8ncTYicFpQ7TyqmPurfnbyMN0lLMHgEG37kom5VNyxuJ4iSJ25mYLFTuEzaXdz_8MmhI2q99G6QKOfOSzPDtE_bP3YSNllqybvpBDHNzyWXAUhoKVBnVR1UWS0R9U_0QsR9IH5QlfD1OllXQqpTFXEdnpJk7e1GeKDPm97lR4zeR5u3VOpJJVgfnxV0D0iDBj2O_2ID3oMWhbQWo7ALSVVK4H0u3MKYug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNqVNlG5cYd5_oxoCllf1NGqNlIFapxqK26dkq33jOJ0meLWfhAFUCwqTdwRYQqFxru4bWldvthzVXXWBF1BrU36t5SxqOhYHnBAtXnGuoXm-VCm7ZHb62ZO2IQQjTF2LDHpFOyIMDS7lBPMlMne_sF8xO42vGFn49MjwjPFFQUTDfSwZMSV9VbrhBxqaJwWxPVTixVFjVlmNbMX6DAeluQ1qL9xdFhD38IFCxmytSFPYUEMuDjvmux-nII6HQ5SjiNKUxFZ_FzPESShUKG1GnMYo3-YBnb7h8L91S-13tTFrJa8qmakxz5Z8GrYaGE3ncXCPe4DzMhpumJXjfzISw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k4KR3HyPVa_GMUpL3PyllLtteoU36Hbu1lJKqonr1CHX2h6p7WdrovxlmQsyWgvJiMcWaZaa3ZrAcjQzd3gNvr1RZqf2TGK9duyhpRDrPbtovxoVkDb2XhmRXeejbqosMWoJ3LWVlPDACIA-i713GfVfIVvjfvMn6j81PdBz6bEeULDkPJkBFdK_Nn0mL3vl3d4d0B50OGiMzm1hZ9GgwqN28ARt1MdB9igkdzJyFEFGWtJ_5z3L8VU-3jLeMQFfm68p0-O-oPsD-cLBI4wLehlTy4n3TjIUYUPgt7t3HNmE6n8Vr62od5-0OKkBJ2hhuCNR1509oUVorXmRpCM5Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VF0QVE8cPe9B7M0upmmTes7tR1bopFlUvDKArAaAyWgKygGvCxmJNK6GFTXgqWJX3ukHBcmtvBvZrihfQh0MvzzK8WmtzDPzyI2gXIB3VPevsAlcCvnx4rR7L2lt3RIM3wp9Fn5eYp-YZ0FUPZx0hBp1ZTjYfpRb_yjfqe_bU_hI6DIewYNTnz33m1-HwrSiK6MmvkLmqvckdUdDuRzmpJu9rHQ-v5kMQEIFaJw-_LmRrQm_kz3kPh9L-kKP0H3y46ufeWdiW0_0kLu8rRlcl_vCOj7tfnvuoqT7Xr6FIcwfTNbHMppnePXZaByFkrUn3pMZ8iqyXiBebzAbctdoig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rVyzc01jpu1QrJsb7NF3qUQtzaJvIWbntGar8Pmj1rUqIHXAsjgbAaDaooOcUoVkHy1OgFUqwKobhc9lgjKYRKDCtFEtX9XCk-NBTCl8m0HmFpdbnBwIhf8sGYllL7j4cimo40_sjdITBICBEyZEAMTanE-iUiqYT-EdDzVNGai3iuItxGuhfn1Jgim4pEBkdV8dT749qdBTzeaEvMUQPxFj-71ZIWuzMAyiG8UJL_ZOMep_BqtdwynaS9T_S4z7ASr_eTGYRrUEIVTz42Q_eQi2ERBnsZhrHNrvpGwL2thhOaQ5Auwy0q2Pp-PXvRz07JC_9uPgJBd5e2JPT_8Agw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/anx0Rwsw3OoVxUlR4B9nn9K4YqJe969jvyvyeljblX1nXBG4n0Bi0hZaVkfcApLqImDpUnSdIOXIRkCe7HmpYBA75Sry6-sFI1hnMLd1IzkgbYIFN_7eibprGazF-wPSwwsbLRW4gqz2pRo6AiPMlWIzovrZBYNlOC6Nx_1OpNnXzZcAunM84waVpD26ASDk6gTMrFnETQEacTuEh7Mrgv80EX2JPK16rbiymyhhn6xpJibWmHgbDM4gSwo41GZDqMpiu4MwQ_ZuHfNgrvEgpU_ey3p92Fm03jrt21uphR-i1PR4b_d3abm5ppPYjcj9PUPFtZWQ74dFW0iV574ATg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">میگه ۷۰ سال پیش ما در خفت بودیم
که وقتی اسرائیل به مصر حمله کرد
حق دعا برای مصر هم نداشتم!
اما امروز باید خدا رو شکر کنیم
که از اون وضعیت به جایی رسیدیم
که آمریکا و اسرائیل مستقیم به ایران حمله کردن!
اینها از اینکه به مرکز فتنه و جنگ تبدیل شدن
احساس غرور و افتخار میکنن!
امروز با مصر قطع رابطه هستند
اسرائیل و مصر دوست هستند،
اسرائیل و آمریکا روی سر ایران بمب میریزن.
زمان شاه که در خفت بودیم هم مصر با ما دوست بود هم آمریکا، هم اسرائیل! معجزه آخوندها !</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBsSvtWPZnTDEm6hY9s4WIBSOreFqn9JXqJid-TtLz3XiFS1fwR0aY7WIk5q3_o_3qiyFm2sqKZe0vJbOUwcYVpPnMe99N0M4ibXuDvBznPNPuHJkkJn-B8vNEXoftJpwg9rpa1m2xr0B-zBcIRPoZAidYskbdtDbT4SLcSYNEl7gqryJuYndfAMcwxowx1nRfck8mJKZyMgEf9YIf9CNWDm6IdPDuZhmaTeNnjyQIY_UUDV55MCu0eBx78sXhL6-FXLKhIVi0Qa4Cvi9KumTB2-nZUKOEOQb0sETUujP1Oys9CUj7bUeX-2-gt6sAWouEPHgD1OELoXHOvH5Zf9Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2EHuFOEFruYMUesPDjZnJ2P6B3ZUKlArpal8Mm540fQh5zmheS1CBaQXEvY-RwnYP88lc2PtqOE2fTfbeRzhMKCy_d0rQeIfL-D6K7Tv8pahOIgFwUM_yqXqCneXem1ow9MD_xKp8xYqZpJKWZ0x-Db_DjV7QBDRjJEjz39wCd8TUYK_47Xw-eY_EyRZ3K5wDJAdohEC3WwMfsYGSUxoa-f_nWV7SyJJTkhnAN43YpL9O6_FyKifRHqDNn00lTenSrWvcwr4xBHTgOgNLSkgfE1-3bHu1lq--DL9Pa0FaSUroru-WH7PMx5IgCtusrZzXZm0thIQarABIGx5tBZPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=KalucNuD35iv-HVvzv9T_4guFbKvozxNZUXnAsVNfGVttzpd1ZLcaCa_-Glqx9qjAVVFYA_DEIahHOW4_lr5l7PIpHwgpLDzj_NoMj-rGR0P6jNHLz9v9Fznye1CyQbLcAi2M7C0-zuXJ10jM9Y9YRhYNStgDsuLIdYU_P4-FcEnO8A4Ysb7xRe7mgRQ9mG8cgHinnT86Y6cbF6SaEkwH7I5BYRBNfSES9vjMu4Orj8xWUGsWtuZOo8NJ26vDy-ifk-ylqrDR0Y4eQADdiVyqXvr9ciGjtijx3KL0I2eltuCM8CViWI0GF_WYGupdJ98MkBb6n6HmVdi9-iMafpw2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=KalucNuD35iv-HVvzv9T_4guFbKvozxNZUXnAsVNfGVttzpd1ZLcaCa_-Glqx9qjAVVFYA_DEIahHOW4_lr5l7PIpHwgpLDzj_NoMj-rGR0P6jNHLz9v9Fznye1CyQbLcAi2M7C0-zuXJ10jM9Y9YRhYNStgDsuLIdYU_P4-FcEnO8A4Ysb7xRe7mgRQ9mG8cgHinnT86Y6cbF6SaEkwH7I5BYRBNfSES9vjMu4Orj8xWUGsWtuZOo8NJ26vDy-ifk-ylqrDR0Y4eQADdiVyqXvr9ciGjtijx3KL0I2eltuCM8CViWI0GF_WYGupdJ98MkBb6n6HmVdi9-iMafpw2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با اذان صبح،
دو جوان رو در اصفهان و در ملا عام
اعدام کردند!
ابوالفضل سپاهی و امیرحسین صفری.
مردمی که تجمع کرده بودند به
حکومت جنایتکار جمهوری اسلامی
اعتراض کردند و درگیری‌هایی میان مردم
و نیروهای سرکوبگر رخ داد.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=qubhEQmx6mtad-VuyrHELhgNLr_Co5Q54Lx0oprbCS1DyqfHiAxrnWIudDjDfUuy0r-m3WQoZ0Ttrn4h9cS0Pz5f2OkfKgNS2Cs5KRZETvg4jeCERXGd2VNTluK3gvk_NcGXgRMNo7s-418uIhgGcR91sixJQ39du7-jfDm7qEg4aXHk1VcZpOpsqJyYB21k2zO5z7rkjZDHS-2AsZdYYOQJNW3ph5-7TjgdKc9k0DL_IK9_5xQ6UDRTgZXvrFe2ODuH8DgZ3G6-qzJTQA18QJR1-voInqJiYkPu9eIZ9RAULoJiUDGhyrRN5CWstOtBAEH8ECiT89lJvWxJ80h6bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=qubhEQmx6mtad-VuyrHELhgNLr_Co5Q54Lx0oprbCS1DyqfHiAxrnWIudDjDfUuy0r-m3WQoZ0Ttrn4h9cS0Pz5f2OkfKgNS2Cs5KRZETvg4jeCERXGd2VNTluK3gvk_NcGXgRMNo7s-418uIhgGcR91sixJQ39du7-jfDm7qEg4aXHk1VcZpOpsqJyYB21k2zO5z7rkjZDHS-2AsZdYYOQJNW3ph5-7TjgdKc9k0DL_IK9_5xQ6UDRTgZXvrFe2ODuH8DgZ3G6-qzJTQA18QJR1-voInqJiYkPu9eIZ9RAULoJiUDGhyrRN5CWstOtBAEH8ECiT89lJvWxJ80h6bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

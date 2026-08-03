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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 22:13:24</div>
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
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farahmand_alipour/6492" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHAFBFcnvXuewN6H6Mr-97u3vLAllyfEvjUOEngOptXF5VjVKD77NsS_E_iJrlkMXWZ556Xek-drGE_lpy04X2e7GNm02uMBa_7gEOvaNEICvH8rNFRbbKHHy-uGxfM-zaoE7PRob_v2vIgrJoWMO0H68rVbtdriag0Kdzs092EgMtSY4V2BlB8B74OmjhzSSclgeb3xiWhWdFZ2LGFRgSdyemtnKU-n4XgxEEeyuZCi4ers_RYpaHxp5Krsxs1TKMv8gabADvUDZjnitiv8wbkMLYZfx3sS6udYvyeZmheljitgGWmBTPbWvCdTk_8vuUicl7xRFQRIBSqmO6ojOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtGw8K29MtYV8qwafr_11h5bRz6yBfjpYPnJo9K-PgOF99nRNds4_kh7tDCBMimQ2VIAYyZJ6MeKqpjKoElkijYzuL1fz8V2CYyt5ai611SjXFP5-vxBeoYPNdhEiyXYWdECQ_TqCp7nnQWACcIkH55rpVy14xSsbVca3Y5jetrnO5UIAHljd_hm5KaWctJmYDCooAtvBQvSeWzE5rw1xtg2dYy5iHDZ7clmneIfABvJop1DFKY-vzdiJ3FVTtoLD81I_pe8ZJ5MkZlLA85k1wMJkFCGHnifJCXyNvt-FxaTWAIBvRovrTyL_w1QDmogThlhwlpnDyeDz8_OrnSKsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tj2twco5ejiuMHZ84JP0wcvFlzHd7OaXlxdfIpaMcczC4D1C-5J_hIgplXGFT01_etp54A7AIOM4fCeRPnaVfBSPqEwBPBJ1e2rvOZLK-VXGwSPZj_6NlvZ1RAJK3umTBccGpce9VWvbP3JPhnYnSbGfeB2T_0jmKeJkxOtQVJHEfZQ-yocsV6iKHjiYnNZ8Piu4b5l8uE4oOuBDb3rYD5HzbHrbPcGDySvu8u3HEToMVOUU7PQ2WhmnIEP2lHiDji2C3jMI31N76zt4yMb7CcYvezV0OEDT7yIQGnEUJA_wURgcOdK7pt9syCcCaQQDJH0_7hHif6NcIXh8S9PUVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gikmSGLqJGCWopa-vcotBpNI08bGSoUBEUQ7JQi2Lap48K3EZyWJ4y2iF2wq75F0Pvuq2stEVFrE2pz1LGmuJbdGjkA7dTmbSmDjYfo8e3XuruGJfhlP9osPBY7u-H06augoQciQDY7Gw3Oyh98Xbf8eHhKkZZ-HzKS7TCxX3eRyFRMW5ofAU1sV862scrND3n3RxpjPo_wFT7pszW5kBJzv7PlawCTp1rRt_bhnkOLEAbVRvNvRkrACabV1swzmMEj12-HkrvZ2QqSP03Kha5fJ2R8jR0PHf3i4fcukgbC4Tpp_N7h7Tt6sA8J8cSVA1RNn4hVU9fvBrwtWRhrrqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBsRqkdqM72B8JE-ckFufxObNJaBFXBVYr6QoRBdWHWtMbKAaBKe91gju1-ecvjyNhOhCoqvRp0YhnJxfJo2sBRFIEgnfMnpBi_Pa44v8U8bs3kDIF4KzBZK6f4T7JS9cl43nH9oIwdVf2fDSaTnil1EkdpJ-aeqo7sTzJNr7TfUamvCxaKNna2ULO-Gka6-j0ZyLkDjQIVZW1xNYTNysidFK-DAJ3D6TCDI52WwKBlIgd6ozFvZgvowPb0aZfn5Ex6jdDXf-yEF5OeWiYv8JHH1o3Co4A41TtOUnpbQsn2mSAgCEVu4bl-ZKvNMrnMZxHPPaUlKc9yPyiMuIfnRaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSckZ-TBIiTdoOxEDmXs5ytxzTVe6-XRoW4mCU50uoAiaUo2gcifF-ZFbYHi56cmwbaLZ-13ijgG2rxk9fWyKri--0N0sMCSDgnLVARR7D7SCtNz7JGf8i3_YZ8kdtS3datfRwgrQKff2AEgO2wzMKWuERqR5JGpxk3yQXQQpO04ymIvA8UZ0fR50b1NJ2-cUTHwfHT99nT2lATViVs0xjroOYcI8DDPycgGZ3DsGOXhRoSJLjGIVQpcCDgWkmFY8jIsfd0Rws37eJsV8qnsqZkxGl5m3E_Ekc6VjqHA3i_1OK44q4xlb7synyfzgB_2Kp_dgZ6VNgpB_bkKAlQE6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQ1k5UbzFqqvs0wJl01nz9jJJF2d1O8Qzw13R5o31_OAzoewIa7VEvd8833-vddTL8gBNkKFtQy1Zct7FZ-WgO5RWdXuXsT04iomza0KlfXmZUkHADAWaNanMeZlcSm4OVzihmNi8wS4IRMLT5mTEiLXgYo6mt0rfaoUJlx_-jDoCGmEXUc6Nod-7ceZtP5qRb6iB3jdijhkkZQDecQB6YEtNxLPg0ZGDmfeCL6UWPuwL67ApKIjVKWYWQ9EhVOz4e6SkQY-6mSB7TB6yRXgvMoNAMXR2FXvTNQ-KJPTFMZwUtl0qhGZz9eQsxee0Eqys1ncHXDLFWZv4PWwZG6rGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-uYIYkUxeuWcMkQ5Sk4QuOMxV6E0Mtyifht6gYLv4p0Lx0yAOKqeP2tMtK7r7I-znH_ph4PE-TR4cKtid54Q6hmIv5eGTcmAq9etpUhUeqaq7WPKO3Wtog-_t6GnFW2dln_d0JmiyGKlstkrO2MaOqrUyDcu5pQeZBlRIx_EJ0_ahzFfW55NxOUSK2D-lrDIkxxl4eTtmwXO6Qjcfb_J0m2xFW8VXCvYTvTl1NC0QqOzESHyhtXFoE8a9GpClHH0avfxcaJyTljeME8iI3DyhxTTEq5r69tDXT1i2AacTyckCnf6o1XOaf641W5vSAOmNNE7_3s4o6Sxqb-g0lI8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQegXSkgHUzyOVrtA0fNECy1Chq-PphCRQzuGM-rwjVgubTBuKwruLlNOWXqx7WUpl3gKezgRdHNLUi6Tji6Yi7RBHZYhR7ROJ22COXcZ1q0wiyyl2G3YpAWE2F46gsRfXxoUQGknD1slmCIXHno__Skjc_qkA9cZ3vhWWCdiSQI5u9r9LjNOQ1UhPJqhFEtmwI2jNpF0tSHznMPEAIkxR0bz1nrO3cKrMSxtvh8VtUAkRx9GT16UBNeOLnoyVtKjjWqWKtq8eygoSDCwVLvL32qCtJt1HMC13KnXu54JPPXIzjumA6pLev7mcqL7wHT1RKBQh6vQe5DPr05dxnBBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b21yOC7U1ZrtHxdvG74FKnhw4Gma9Uwo_1czO3uuqx_lMKWFl75WI_un87Qp7QW0PgrHkPjQ3AqW9-jdETdUntk9pt0h-_eP-aur04vnASBnP-v4uKe7OhGfKd_NifryRio2iexFZP_z4_qi_YDh6yBLRxf71iTEp9cuI8pOf99G-9swQExaGoaWi8eUR7Q5WG7OzxrotLyFjH0Nu8IdhruUCP0WpAbp9eJQWWabTKEgwXEVUh64RoV4dH0WlIdfgKXpRD6G7xs4exwH8UPS71_Zy2YdhAwpNB4xCblX13arKJvYeuf8_RyBRqzNRP_wQkagP9SaL4agXMr8yCK88w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYed9fUA93dhYdfNmttVcm-2lUMw13RTbLImI-z9mIYAp3Fn2k2kwxWO1ig3HF9kt__Qd30l4m1S2SDDhtjk5O0OQsidkXQ07ucDS_PfMsyPqIF9ZhT1o8M2Cxsd_EbJQdDbi9aBA4SfwyLGuP6nOffLvRWw7t8OIr385KWwqDP63fknUcx9lGhmSwZ20KPLmq_5e37EHVefD9YRhdJu6ixoSXKTToGezCK0UiQndY6nkAU_-eRTxFwse4feS584QcekMbB0tAYzlBdDkGKmgpvLIimfjExjasGpdPQADAzfOTbty7ziR-RNmt2mTKBDmtYnfK69_5xd6506jVO7-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K13-EWVk300XrJ1Fkt-iGX5-rnfHdE5dP4IGPa1Z-kiTzlysN7YV214S91LGQ61UIw7oSfy_cGFHq1jg4qsxvzCCJVrWcnJtpjBrDiMxrhKULT-_NcEyVybLvqpra15vHesFDgkfDnpjjBziAcQ03FVy-0eQtcv9WiP1HL8QAiqGJ9CkPdCRkRG5uiyYtJdCWWHiP9Zi-He51y4XmiI_R0XePJ_t6O3Z_h6mGKtzOK_bnFMdpCpjERYz0XcX3ywl7ZuY-cbARFf6ZHg6zgSP4-HfsNMwzeOwSqp-aI3YZNP7RBmhZJuD0e0WDz47DeR2jr-C0rN_F5zx5kZLolamTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElMFs7SUtkwZSMFY00cmcOjyImvYnSG6MbkuhV5RWEU-JY23FALPdYBgn1VxZwidANVuNIxbxaAKtb91U8XlRQEFAR7A3qY_FLHP2g_4AqE5RHoOUvox5HXQkSNsJCznRuV8BtFwLc8iPDwVA5SlUnt_wi8NGBs6DwDF_CGZp6jW9rIP27jcX5ZOj2uh_sRTses9P-2qoDcAnE6UmVoqcvtqREfEHVt1-Q_xsdl-57tZzd7uUUrAaLQe_ReoPq53NsFlkK8Z8RsMC0Q0MLlLHW_pZnKCWWV9HP-BYESgewK1TXEJAZFGSFY1-WUFtO0kLHMZu6MgGdoEnGd_-WggxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2qbnk3jZgsXhsB9zU_TwR607Y8abZJ0ufaz80o-oxUw_FPtslLXSzac3DHGxjCwEFMeG3GoOVEbi9gFOQRoy6TmDBkGVLr0MQjiVnNDtNAvyPzxEoyzEVdBvqlM3ugo6-V-oNUb4WaBiownT-oej_B5o4UEfrIIVipfavG9Lk_GW6E9Pknz_589dsn7yhCcVqa9uQVp2OWt_r1yw__Y3cO9EThuBMqm7eSzuiGv0zLWpk51egJvHcGBHq96cj3FpusvnEcU-yINwQDAQZHvPtG8z2bx8aEpXAefuXBvWazpho7cjUySlKFMHpivYMkrQdNNfYMtEhxl5F7PbFGs_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxSVYg0rR7jM5F5P4rR3NDSUm3oecGND5NxlIXsfjJLiMqMIalpmt2x5w3mb_sU0f7RIv59xuIlLWPV2p6UlygNI4SoUjFUGZlP_HGU54FlIdnpTD8OJ5I3MZTKUCU0qYsHlb02VWmSQHPway2GzigQhWq4wqOBIW9maUu5JkX9jYlacHK3jCWHRltH6wRVvmceOw_Ara1j7RZCkXEIgd1k1h_4oKiFQQsY2K7Jqf9Ifw0jQnFxlU8xSFaldW5WQlw8sezcnOWcIjLuH2YVsLECkiUf6lW7v9P5FJewe59EuSj_bZYCM0DM3ErjchtVd5t0v5SRTXWWgQniFxR-HVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nH91JE-ZudjzRDoaXjImS3e4gn1o83vYWHn8G4hmpnO3C-5twR1ITHCMkR9k23jxA_uQPcvHQU2gOQMgk8JuWUb4EGAWSuPu6Kp2dBbnGoXppLBbTf8mZaPBGUF36Kf1TSlQnhAVYpnk_VRnT6nnA0IJVBEMKM_9JZqpayJ37IjaOZDngKBIKEcR8BkyaPI_41IRx2REA6Dk3RRL3qyngWoi9Z1iZkbYm8UUEs7J5i4Dk9l0JjunY9oFGNvlX_QJPtIcJIq9ar76bRRG0OgnlR3k8j4sndyNu4IBSlkb_e-8nzAwf8fPmr4X-4ptWgWz_Ke1hBkMu_F2U5aVBRYOAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIxvWBZsk-ijz0t_FDyRYtystOJ_apke4txRk-0uVDq3g4bKKhdrAFmOse2aKfmeytFBqjA2OEn3MQgmZhicrIJsemm6LAFOM02yfmZK3rSvQkMsayDyQASd7KXfd0Br8peOdmJdJ5m5VLBw8jiw1WCJhlew8DRvwQI28YeTgfBX4VyUfwvfO_Re1CD22TdkYoYr-PcfRMoJvhO9pyZgoOiJ0x89pja_blYNjzqByGIe8r8gGi1XwzQzJKcT3-K5qtlt07ebaFDJt5Ho2m0Q-B_nXaPJDjICDGT-nHuRWMZ6te04GHMyZTVp8Ci3-73tbcwT_uQ4zak9eL1N762CyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPFAHOa7Ltr22HmS-nNFwIcmoviJbLOPEFeQqWHcAn_YZfNFiEh2K6bK0G1IZBwXaCyfLHs0htr41rAcLkbfLwXnyqjNMeM1Ddw8m6oSlPw73ZfrfHe4GsCZti1u3qK_i8bw1VxEYJDHSv7SQ6Do7_gVzTI39k8YVIe8jkHohWzsXpDL1k1EAOVspCJnv1-BTHCLxj3R1hg2WtmkDtfS1H40UJdI6E1n7nxHjbOHo1Ft-6RINWr5yVa0AQMBEzjMhNZBEmxIpgPXBGFZ0ziGSimeNolda5PRVDtPzYy_hHGWYsgOPzbtSMz587HcVdba_7wZ32VjgdLLPQHQZoR_MQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=mzTUSGaQsvGZHurmIIFFQhw5DNtswzLeO0Fueaj-h4eJ7AMopEQeceHpY--gi5BB-ulfduFDKmBDVliUh2nJXAAnLIXN_iWIT6IoAKuOHB28oZPGpEZJiXAwN9QjAk6QNbV9-T7Ep4GDBG8URIhukbhG0dAL6l4hedMMxKfbFXSqH9ZDI8Bys5XuK4WoF3MM2-WtyC1BB72uqmarVBTIjmfpsnoKkM4w7GSo8hgJ4JwiIToXumwjNWufdxiLD3UVBKUfNker6AJJEgvJwresRyb_d-h1jVhgob7e1PlE-UrqDt6tD-MEjtuZv83Yb6_Ag6Jn9xwFDG2FRXdHpM4fMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=mzTUSGaQsvGZHurmIIFFQhw5DNtswzLeO0Fueaj-h4eJ7AMopEQeceHpY--gi5BB-ulfduFDKmBDVliUh2nJXAAnLIXN_iWIT6IoAKuOHB28oZPGpEZJiXAwN9QjAk6QNbV9-T7Ep4GDBG8URIhukbhG0dAL6l4hedMMxKfbFXSqH9ZDI8Bys5XuK4WoF3MM2-WtyC1BB72uqmarVBTIjmfpsnoKkM4w7GSo8hgJ4JwiIToXumwjNWufdxiLD3UVBKUfNker6AJJEgvJwresRyb_d-h1jVhgob7e1PlE-UrqDt6tD-MEjtuZv83Yb6_Ag6Jn9xwFDG2FRXdHpM4fMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMypwLyHE62yIADCzi1jYzwZKovzp5JMRvyCYfKWb32x5yxyPYnHy4Mc7hPYUaD_WA3FOA5WnUt8H48Sv3msonT6gX-gztG7KlMKhqzvxnKckOFRd2RywE7x-8U5iwcykt0kgqhZ1vt78xZGVW4iTeM8Pc4lRXo0TUc5EKp5U8r6H5ILmVenwCc6lQc8_dfMrhkjr8yHy19XdRRkumHJ_vwwQ-PQYyWCuKrj_xuhDT1XvrD0RtL3ZZ3r3fQQO70Ckoq3f6kpBp2A-4UbJRWBiU9Mh7Y1BGqIufwQA37p0c2hpk-65ivvwJvTW824tM74vdwTfqSCvpFYA9iHQuIjBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SciWmcLYOAVuVe588ClZRSQ5_JTMNwSZud5xYMUQaZ2pQVU_iKhuQ7__E7PYTS8aSrtSrpd9djUpeo2QveoeCS-uAKVMYNTGxDREe038u5tNx_Fm9ongrSAibeWkcWRcimsYqv4mfKmoqIya4Sw7M58yOGKzQ3DI0TkLrB4QgTMc6VvkbpOIv4k-pdAEzxWpG9DxvUCZP5UTC6Tn1zmJHDvjGpTl1D8ILp-1JgohXzlJSSCi7juRKSlo2cGz8qvv7Hdu2u1rkUG3nN_dhTIOpMAsHIZtZhMpHQZzWOPvywmjNPnDC2pmMH9VQumLJ3r54aQWiX29yfZsdsCXD4MBaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDbSaZifkzLV8YiNZ1Z-bfCGFDYlkaIeSugGa2h3OFg0Tomf1sn1qOMCp5JBCt5VBeCysmsVsEDL4Ly3OmhD7vO_vHff2qOyqH1D2fbqOkvjC6Xg7lqw3urDre_ny6ILZ-eMZ_4_zbxu5NYKJjZyc3nj0aVUvfzu_asO-0fPC4Hft3dvUOUNNOzZdBk86rT9FdHoCTwOqhPrLNEV0z3kIzLls1cVTNx5SgvVYjDcwu0bA58PZRz2vqFRncAbgezR5JlkXp7DMDLTlu3LLF52b7p7qrSNIzmcDGzLOQs7s9VkGTqUa9xCQFl6cYOjGIe4mvO9VpYqPSubZ6FOMtOmRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2cxxSpQOdAMc3VyrsX7p6Caayb7EXVD3IWa5jK0cdsw1vrRpMRena9e7TmVzUW0bIUfUvZK9JuLN2fRZoZUniQd0p4Rzp_wkiWhb6XGa18ojy8Vqroh1pBZ3vtm-Do-C78pcPVELhfqoYCeNJmHnJKDKKs58MzDtVjKGADHLnPNV-GdTdNkyTklqyqYHOeJAYXquv5SLVwQ-IbGLACVYKf1eWRJ79ATNUsE2masWa5M53f1T8ZMy8-IOFpLhMWOfbnmos5RLpur_xzB2WPuxMI0Y_Uyo5mKAiVX46qD5nsqqcQ1doGSYLbTzSZEzkoJRz5QQ6o0ZtaitilJEO5trQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brn9I6X-KYSAxXKBI2jE9ljBQTf5a9MxBH7cmCdVwQJGySJBQ8rWxfaqs7gk61_sVItKUYnDBSPdr8Qgw0o9b8GPcMyyfw1bew1GqW37HXAS0ndwHKt7bxHQi8pcG7Oz0y9XaHoW9fXe8G0VkHx9v6jbcLB9wO8SxxfOis2cBPTJfTb6F6-AD3FKizo54OOWd2pPX4QUK3tVCw4w1uv6akB6baf47DOCq-pwdIVmG2bFkVbqVooesqLGVTBq_bNNk6llvAHirUGOuKaGIhhr6n_8pgKqze3RMS9HSLD4p7V8e1vPva_kXGWqB_loSZJ5CE4eJwP_mqNfZIbhdkZ9Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sosmYsKgUWkSID2dkZeClOhcTo_yGfOzfCqkk7lS2wpqgi38bRm3w9yxJezhwzkSQ1Exmw32waccghoP3nC1z5wzXJeNhcr8G8KlETinyP_suBmkRbnY3aJcRuzqXv0nf_mwTDGO1bTd5y_ZPa7V3OkdrqED2AQGPTvjKSf-AjukSLybyM9CEajJI8Kb__x8PoOA8NQxayh4vHsAT9yYsoQXKSE11T0zHZpVz3QqwsYA7DZqyI9dvRDhqDv_YgJ2D_jc90Y9bI1fPiSE9SVaS567dwd3gDp-ML3TCeWXYQ1rMsvPjX6BDuSpZ0FTiJc3K-MMHmyyESDDOSU2gen2cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfFO3g-lMCse9_RYt-6f21srSIw5wcFeYqlukgrP4p_I2xJTp2MUlx-ItQGzbx7qaLfjV67rfQz4GDSqieUIjjNr2E3MvXeuRw-T-oY7-pK-oXJ8Iy8Xr71Sm0b6L20OPYjK4VzUymRhkaNbatqHgzT3p670l1GyKOpx6NcXOTzWUH21JuHIAURDSmkJdx5vqZRTxo2zf42eNrPz0SPQv5LxiuyJkBUVtUpe0e747PvJ6uPwgCy43aAw2V--ej3FsMMLA145Q8Ut7CLCfLO9kBtjApB6yL3efIUmZJfwmQQwWtQIJun16r4fWUhSgnv7QmjgBnFxSqnFRtDD37IaWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=s-3T6f4zTuQSg-wpYYspwLsMzSU-fkm7v9_GBcU9cB_QuNBb3d60TVa6V1QF-KJNhyl5CPYWUYmX5-T0t5WF_vq4RKQcPQ3TCFurJonsF-8rDXVDzxUa9P8G337TbbmgX8ocApYhI_OLoj8kmfA5nrA5NhQRtsNwqO9Olm3e_nBAtuOzWSbb6keBL_wowWkAgtgby_1NnnhAJe1SZPl5Bv0VO9F47nnncmi8iZ6pDOORqlV8rnzCZxoXO-kSBoRTDf9oSdLuccA0WyoKI0YdjuUPHbQX6qCce9OWvFcxXbjpBzcqSnXhICi4aFo5Zg6NzFwazLdQTTjbdrUfsVoUsZuvjy3z1CojvEsRCt054Ln6W47qEoS5DkiqUZs_8M91j-n9rhEiCriLQ4pImTg6Cnl8iYtyuifweglrxWQoIMGqNrYUB7_mILggu4tP0pVOK3_e1EVn0HWpIvvYnSZWCePjW2pbVaINc03BKQGbugkvXzdPKxLKp6pKROFEWV3FhsF3_B0fBDPf9eym7Ewn0NYANrGWnicssKask3Z-aVic_QjxwW3XnOI9WeX59bzj-DtnrE7j6iCzvUdfjQ3VRPUMo_646QpWmzbDx8CpzK5d37pMSNU1BFXjorMaZgm1OeIRLYkABStqEreuiUvKvJPOzFDww1z3gf95OqFrXY0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=s-3T6f4zTuQSg-wpYYspwLsMzSU-fkm7v9_GBcU9cB_QuNBb3d60TVa6V1QF-KJNhyl5CPYWUYmX5-T0t5WF_vq4RKQcPQ3TCFurJonsF-8rDXVDzxUa9P8G337TbbmgX8ocApYhI_OLoj8kmfA5nrA5NhQRtsNwqO9Olm3e_nBAtuOzWSbb6keBL_wowWkAgtgby_1NnnhAJe1SZPl5Bv0VO9F47nnncmi8iZ6pDOORqlV8rnzCZxoXO-kSBoRTDf9oSdLuccA0WyoKI0YdjuUPHbQX6qCce9OWvFcxXbjpBzcqSnXhICi4aFo5Zg6NzFwazLdQTTjbdrUfsVoUsZuvjy3z1CojvEsRCt054Ln6W47qEoS5DkiqUZs_8M91j-n9rhEiCriLQ4pImTg6Cnl8iYtyuifweglrxWQoIMGqNrYUB7_mILggu4tP0pVOK3_e1EVn0HWpIvvYnSZWCePjW2pbVaINc03BKQGbugkvXzdPKxLKp6pKROFEWV3FhsF3_B0fBDPf9eym7Ewn0NYANrGWnicssKask3Z-aVic_QjxwW3XnOI9WeX59bzj-DtnrE7j6iCzvUdfjQ3VRPUMo_646QpWmzbDx8CpzK5d37pMSNU1BFXjorMaZgm1OeIRLYkABStqEreuiUvKvJPOzFDww1z3gf95OqFrXY0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=hVjLLvm5lSBA53DEbV_l0SLpU7bAnhHohzXdl036t_ebNsHbtd2SUT1YInrFyfYHWJfuglMSanxy7N-f_KMEZUKRkQD9eHBLOXmQQJo3Is7_geoKoWuqnADk3brtz5wCcAb3SWhT_2YL73SQ3F_TATI2t2-2DsVbt695qGa6MYBLRTIjH37Uwa1MfUTcgs7nrvcWKkvmqtiygqi6EMt7fFSSumv8fcFi1tOCsqFDHQ2I8cdHU4YCCKP97e2A1uyLXS1dZ95rvdXoPU6IUrHc2tNtqluRqtq8-ioK5zhgk32ZXmsClLh7JQJVUrbHbbCReaVUTcOq1zz_AMx8TggD_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=hVjLLvm5lSBA53DEbV_l0SLpU7bAnhHohzXdl036t_ebNsHbtd2SUT1YInrFyfYHWJfuglMSanxy7N-f_KMEZUKRkQD9eHBLOXmQQJo3Is7_geoKoWuqnADk3brtz5wCcAb3SWhT_2YL73SQ3F_TATI2t2-2DsVbt695qGa6MYBLRTIjH37Uwa1MfUTcgs7nrvcWKkvmqtiygqi6EMt7fFSSumv8fcFi1tOCsqFDHQ2I8cdHU4YCCKP97e2A1uyLXS1dZ95rvdXoPU6IUrHc2tNtqluRqtq8-ioK5zhgk32ZXmsClLh7JQJVUrbHbbCReaVUTcOq1zz_AMx8TggD_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIBhpPOt1a1AaxsHb9g72hnmgQd5dpY7R7psG3T3DyO5mHxmjiFxq3Ogi6CyT7ILx65cow-bYSw2lbbHCk7RSBm7HsxfoRD6ITGhIvihQObN6quyhDN1PtvEHfz2wDkuJINPUs1WbVE-GU-1tKoe46ZYKbQOkjo4efv8fiMoqVjRpkddPO9n6xoOwqXkVhVY4ihT7lpQBAqqk1AVkz1XvEZfUjdhQe-Okbvcq__AFv8kmOjd5EGyC3hI-dYp1mb6VyKcrzdjT_x-a0F_MmEnTiphjEzFOEI4Mwn2dVYIk2Au4tVNInmSfe2cFcVxV8SM-_oB4dw8U-C5BXQs_HP9eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNu-7UnuJ_ANogZyFu7rs-gwdnoCdEsL-wS-ZaFt-iV8dZVSXQ55lbhDbxaS5Xam3BjMSOmDiTlaWEDVN8Q_O2JjIBraUZEsbrz0zTQewyjyFAYVhStJQJFMm5HFJJzoOyMVpMqHZCrivwqx2cQSL-o23xSiXzpTj7kaJCGo5TkkDtPzdyCDuclWWtG0JTm_p495kuUxwr42CsrCDYOfo_7bqjGJERKGJ7hiT61bIhClDcbthmmRxHyV9o26G_jb3l9lI-9QsDjXpReRGiG1oP8jgvFeSNph-SjloD-K-qvnDQW1pnfWM1lTuGob09tvhvEr9CdgGAjAR5H4TtkR4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=iaOAZwx5H_EZVAjmx0iMwwiBYx8NhTBpb2XWlmsjdkGfRDGBmAHd6Re-Gn7GnuHeZ2tGfjCm5Wybz0MKZXI8vxXqBQ-Boqw5PnmcT_7jJw9BFSLwXO6ZxSpvX8MB0-YZaaaRAZpBAu_1ztX17BdbbvN_4PtrYIVo3aha01ljmVH2mtvhaI2v8vG3hAYrggUpX3m7RxqIXuSfzC9_83sn3D_CcfPmzbbcEMf7s4DfEQyxFuhXkaV3JbRlL7_9nzYzADyM51hHbLgAGRP4_N1YNgCf6LTWPNwmPLouzAXUQFem-12z4y7EskxlV4RGeD_JtLuzJ5uIgRnIhEx8QukpGYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=iaOAZwx5H_EZVAjmx0iMwwiBYx8NhTBpb2XWlmsjdkGfRDGBmAHd6Re-Gn7GnuHeZ2tGfjCm5Wybz0MKZXI8vxXqBQ-Boqw5PnmcT_7jJw9BFSLwXO6ZxSpvX8MB0-YZaaaRAZpBAu_1ztX17BdbbvN_4PtrYIVo3aha01ljmVH2mtvhaI2v8vG3hAYrggUpX3m7RxqIXuSfzC9_83sn3D_CcfPmzbbcEMf7s4DfEQyxFuhXkaV3JbRlL7_9nzYzADyM51hHbLgAGRP4_N1YNgCf6LTWPNwmPLouzAXUQFem-12z4y7EskxlV4RGeD_JtLuzJ5uIgRnIhEx8QukpGYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzzelA6NZV7HZqnLCR8-fiBHw34fc-0L36isr0poOifp5Fv8zUeBc3DUMKKRZaygTtdukZjNfyriCI5AgV8yQM0uXT3vzRaC8qIklMVgcCfbEYVGr67b4d6qPBz6hDtLsQURWS0hudYuZcfIBtWMqr6xmuSiJaOl8GLwrWaivVUm3djN4IZaxvmlGFwWANKQb6qLZU0tThRBkYzbXauV5_Zf48-e9Rv9cP38HLdso_x5zdwU1dTJqUeZ0bXxZyx9DgeT_JgitOEF2EEXd2900qT9eXkdXZX58lAlfYZKp44rFAZrGz_oOwyM1AhbN1LlgfZRwl3hAfVggvJsGN6crg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COAEUK13-_Ms2KUf-JCgmJe4vguPCdxgY9G5sEwqBg3z6-dmEsxt0nfgpHCK55KF_ZDzVGvqoCKV8n5LTombf7ggFMvPb4Qd4lNglLXlOzSfARyEHFZSkn6ExJoyT5kgP10x-CMB-UEpZjo9aq57ttTSnQE3YK-r0V15EzXJZGYfgeDADnB5sSALBU5ykcuyPGw5ib9jCAIONJQxVqC0GVlcpT7gK0vsfTn-oPRLgnXZAK9Hk_WrG3_SioyCTO3JmKl0Ze0eXJzP2w1UqWbEho0S48uTlxe1nvi24_od9aPaNEQJdJLREpTNGXEdjk1qW9_Z-Wf-DN14j2OOAdYdjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tkfc9bYYWmf8PLbQULFkA49Soh-7DsG66NiHLyCPN9SyoLi1W-aQlFOB3Hk1yIHPpWXy6ur2rsxuBegIaF6l8gQKNu6unrUVZM8ZJqH9hUdbXWt1XgamfCvCm205tdfKz1OBwxOkyGCZOTB5F-kCDK-3D4ImtN9Cs79zzXpeU2slTKn7MdNtdweGcD8unC0v_pWTJ3trBC5-kV07t2SJozz9aLyQj_UWl4xHJseGPjYXKnH-dJfJ6MvMWzlmuGe3CczyV41MXN6tvx-q_KjApq08yTWH7eVPG_pyyuZRNk5VMhCbNmHPDvsDQ3y2cLA76ITVzh5W8DkFMeMiIMh39g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrW6J2HIK4-eCmCE6PpPdRi9zOlx6cEmFUnZie7cSKmNtHcAPfZgxjqmR370Uk_nEX7mITTwWEqmsokhCNRXO92Kg6UshyFyjQNzx1gBO11y6lRU1jiGp0RdYOBVL2BTCTWVkbFx6g7VFpLl0fur_9YXSIf_Y6_793E54_ZtYXGQuY1QptUqBqV0qTVm9ZmUcZYOxJJ2MwbsKwGjUA2pDaiNqsH44CnZyCDIZ4HE7ZSazW0ECikmHgY0rxYMrIGuvvapJc1RTkmbVQYgZM13ttQEUPJUrdu0v_V0mhMsELMjHHLX4PW2BkibKNcuX2BY9RqoXZm1tKqjlxVedgXE4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnT13onXdbEZ224SE5G_U996e4tfNLtVPtxKdJvxbRyD2PmZZtfPd_ZbDxyabySTe8NosM7odWM3N7VPVsN4PFKWlWFrw_FulzUkbvahW8Cm12fzaaS0LhPXhycJiXhNA7kjsZSZwwlRrY0aAmAsXP8dfqq3jQIkoiSXmToIPymCq5L9CvDKcaeBZ_gb0yGQwyEsKNJk4GxXifzTRsftuVzsRRJopLDBFeEazBEFyO77Yj5um77OJDDYnEEMlu8m7ft3_GbfNd3A_QHg51tHUEe6AbabXszT7yV4HL4fR94VdDURoVeCGAsMxhYON08bQ4hMT0mkZFcZrmLEZ_8l3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJUcRC75SKHTOHBHaEFUINCGJqHWqSL45suMJninBMZVSiZZMC7zm73SOoEMf4B8OPfwTsCIGYYB_2391t6ME_n1tLzJOEcXuCiIjEk41Ws6KcnhhZbq--VIekjytK02DmUjj4HFM1iOzo_kGcVnhSQsD4Hgf3yy2BZZvAfVnZnh-ioS5lz3J7_zXhQ1O2Lo_QUFczofQ83VG_lP2aw5bsxmZ_rKEMMdCSvEVVRJhbEjreOyHHKqK9IHrNbyhHmBzC-jECWEF8OA63bBx0mo_G0e-kFsYXBa6o16EHTXNCrReZx85t4ZQMeDfcCjd3Vi8Ih3D25fC49l8v10DRxw3Ymk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJUcRC75SKHTOHBHaEFUINCGJqHWqSL45suMJninBMZVSiZZMC7zm73SOoEMf4B8OPfwTsCIGYYB_2391t6ME_n1tLzJOEcXuCiIjEk41Ws6KcnhhZbq--VIekjytK02DmUjj4HFM1iOzo_kGcVnhSQsD4Hgf3yy2BZZvAfVnZnh-ioS5lz3J7_zXhQ1O2Lo_QUFczofQ83VG_lP2aw5bsxmZ_rKEMMdCSvEVVRJhbEjreOyHHKqK9IHrNbyhHmBzC-jECWEF8OA63bBx0mo_G0e-kFsYXBa6o16EHTXNCrReZx85t4ZQMeDfcCjd3Vi8Ih3D25fC49l8v10DRxw3Ymk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnJrpjflSIwkg0wJyArJqy29cl6Jdm4hnt2WT_ZRx7DrC17DpX3OTO8mf2s4M0H-YFF9j6c3TRW201Rj7BzJry1Stnf3F7nA_OrQtKYk54QFdowbZu7tBrhYFGf3iWDvG9SIRbjdQ6BLFE_DAPHt_bUYtZbQl42WZCeFEj-BA9gnoL7J8g5Dv9rwuKWflIGEwWjErnpSqjFaJIzyXcxTn5odoNxC330Ww1CPQ_9Xrlk-3XdIfCF7CZNBHUh2upPXseL3pHT751WF6BlIT_ulsczGPccqkCQtmRQ131nZU1HbZ412KSkUUbwErtEXjPJKE_Hf9XTVxvLBIO6UDd2ZUtIo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnJrpjflSIwkg0wJyArJqy29cl6Jdm4hnt2WT_ZRx7DrC17DpX3OTO8mf2s4M0H-YFF9j6c3TRW201Rj7BzJry1Stnf3F7nA_OrQtKYk54QFdowbZu7tBrhYFGf3iWDvG9SIRbjdQ6BLFE_DAPHt_bUYtZbQl42WZCeFEj-BA9gnoL7J8g5Dv9rwuKWflIGEwWjErnpSqjFaJIzyXcxTn5odoNxC330Ww1CPQ_9Xrlk-3XdIfCF7CZNBHUh2upPXseL3pHT751WF6BlIT_ulsczGPccqkCQtmRQ131nZU1HbZ412KSkUUbwErtEXjPJKE_Hf9XTVxvLBIO6UDd2ZUtIo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=VOAIGbrquWxxqBBai47bNC3gqmJ0hBKgEfm23RXj6917DJJ98UO7jc319VKyfpvSAFBm5e_sKY-LpSZYcIcIgiFEu-2BCCayDzP0Lgs81y_Q8Kl40-yLMF8UhcZ_wvznQ8tcHbq8ieneqhVjsDYAMSsLQS8gxWgTvLNOddvcJEobGhh2scjWjrTP45LgMiEs4ddu2fy-lFrJATDop1iqLCGfwbUXZtjo_X5lMi8YFCvRys-KkE37Py8xjTs76dKVA7R9h1MYa68tvM1MTz5XMyIBIDXFLokErjqcbRU0v8ciucdhYPeqoVTNFrpIuZSBxl_a29LeVgwC2YnIZX4OfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=VOAIGbrquWxxqBBai47bNC3gqmJ0hBKgEfm23RXj6917DJJ98UO7jc319VKyfpvSAFBm5e_sKY-LpSZYcIcIgiFEu-2BCCayDzP0Lgs81y_Q8Kl40-yLMF8UhcZ_wvznQ8tcHbq8ieneqhVjsDYAMSsLQS8gxWgTvLNOddvcJEobGhh2scjWjrTP45LgMiEs4ddu2fy-lFrJATDop1iqLCGfwbUXZtjo_X5lMi8YFCvRys-KkE37Py8xjTs76dKVA7R9h1MYa68tvM1MTz5XMyIBIDXFLokErjqcbRU0v8ciucdhYPeqoVTNFrpIuZSBxl_a29LeVgwC2YnIZX4OfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MalwMldwrZOwrhV6lCPxra7DhGpV6ocOKTCq4XlrMJ-FsdrAaMF1FHhygdTEuVli0xEKDNkQae3A-vLUDa6nkBQEAQg_Zwy20X-h6C0CdlFi3Q5tNamXJQPZNvIq3RaS8TIPa92VefjU1Ks-lm1D6Xk26eKUPO6Q0aP8nKZokntiZPmcEalmqRey634uPYq7bNnFfPwSqx9E0We6JPTUpGmQPfQKBdkvO1V4_45pr9MX5IxMI_tEJ46j_SVp6uSzL7fWOmP6f-f04yj5HDXH8TQucxtevp1L_udW14atJdQkYF5OHc_w03_AeOEWeVqr7XZ-3JTVCSfj8hYSLr8E4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JufCag1D3Q7HVLu2v_zwcw7zV3zWi-S0J0N9-lBgPM7JY-Dyl7_2VhRAZ1uKjU9D9YidO-rLSdyOasXLElaEHQN4jvafL0HGeuoQEY1oCvsCJMX7EWLkkbm7vg6Bt7Y3nXM0du6dlozpbIij8o6rpiwfCPiIJ_ySfGBIasqbFa7gGyIsRB47S5QaYnCMvptE1722Wnk2Sn5_WyDIXXH5xiMUTLQA0kztkNPW1KbjFTveqFM30B9IIK2cYxYTbuni1Ng-reE7T_y_881J-CNUMWHDxTNOp4xfZ4x-q4FGXl7CKBrr8hWNSHZ5sCO9t6I8aLcG1Pvo7CHf7n7XKsW9Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=ramMFwF_hkeDYiaPg39fSl1mpyLS5gJhW-2W67ae5dkEwfqsL9TlOtJ_nAauvsZsGv1ElrmsGhryZGW-W_enawwaRHGOHnWgaPBS5_5kgSMBAnNR9WmPWZ2YURJJY4T7VyQtd9yS-dFN2nAgpsiD9ppiPlCGeECMApeJMllB7C7o6AtvQylO6Ke1po7Zod6QR9MpDM_2G3nA--7YBO-6wgotCz2WKqJ8zwQbxJBBI2EzH70h8nSY1y5e1N3OBSMYsJpZe-hGtC1PtYh836MvKOSoPxpwFFfn_ZRPwypd_G0UUZ8csqopZJHH85SMcVMRHO6qKW-3qOusnLPg1czARDlzlsnCREw9vQZTFUV3O_oL3Kg0JLG_A6wFXvVovWPgzzxhMU7sT7TCydWnhIHn6XXr8077ULur9vYYgXSs77SG6KwMOLA6qsFwRJurzk4edaW3jBzOYonj_yfo5p0aimED472GK2E6XRjtJ83b3xMoxbjBCNxxxjkS2XIs0099ZCXzQWwDGXKREXDfcFvoE0GIZrVWvUdToAjeDZoWWz_uHQAmM4U_RKvJQCjy5hq1y3letjJWa3sAEAmtWyNbRIrrAwVsiZs9yicE1ZJt6cHu-mVWQgLL1EArAVtM19VxZDYx5xfJYAG3-oXR0bIBHQPLOXHRBTQ9vJShI5Jq9q8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=ramMFwF_hkeDYiaPg39fSl1mpyLS5gJhW-2W67ae5dkEwfqsL9TlOtJ_nAauvsZsGv1ElrmsGhryZGW-W_enawwaRHGOHnWgaPBS5_5kgSMBAnNR9WmPWZ2YURJJY4T7VyQtd9yS-dFN2nAgpsiD9ppiPlCGeECMApeJMllB7C7o6AtvQylO6Ke1po7Zod6QR9MpDM_2G3nA--7YBO-6wgotCz2WKqJ8zwQbxJBBI2EzH70h8nSY1y5e1N3OBSMYsJpZe-hGtC1PtYh836MvKOSoPxpwFFfn_ZRPwypd_G0UUZ8csqopZJHH85SMcVMRHO6qKW-3qOusnLPg1czARDlzlsnCREw9vQZTFUV3O_oL3Kg0JLG_A6wFXvVovWPgzzxhMU7sT7TCydWnhIHn6XXr8077ULur9vYYgXSs77SG6KwMOLA6qsFwRJurzk4edaW3jBzOYonj_yfo5p0aimED472GK2E6XRjtJ83b3xMoxbjBCNxxxjkS2XIs0099ZCXzQWwDGXKREXDfcFvoE0GIZrVWvUdToAjeDZoWWz_uHQAmM4U_RKvJQCjy5hq1y3letjJWa3sAEAmtWyNbRIrrAwVsiZs9yicE1ZJt6cHu-mVWQgLL1EArAVtM19VxZDYx5xfJYAG3-oXR0bIBHQPLOXHRBTQ9vJShI5Jq9q8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=mO1rP2QaiZl-uRpTq_XrxQSWGkynNHwaRCUCkQD4DEF6g6GSwSjJuRHrA1kmF436I1M_8ZARPN4GA40eG_Aza7iVjUtKZp4P2-Na8fXdkgcNKKSDNSlOe0-MFr8hXmRQOjfZPh4Sm1fwnYt0FMcPwaXrkRCZMNTwrORai420fDwwP9eOah9yFVjzRLpbZsZFv5RpJ8DDq2BTTyC4wMKCIYtnEuApQeczJM8Ea4S04EfmekRCxkVYLfxdnSVAEhegQnC1_u1Ji-bZ-a2Vdp2yTWlq1_W4wJA-cBQtcII-wGG2iPvv5PUOnreJmI9ch8pHofx2vKI5juOA-1ikqcitDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=mO1rP2QaiZl-uRpTq_XrxQSWGkynNHwaRCUCkQD4DEF6g6GSwSjJuRHrA1kmF436I1M_8ZARPN4GA40eG_Aza7iVjUtKZp4P2-Na8fXdkgcNKKSDNSlOe0-MFr8hXmRQOjfZPh4Sm1fwnYt0FMcPwaXrkRCZMNTwrORai420fDwwP9eOah9yFVjzRLpbZsZFv5RpJ8DDq2BTTyC4wMKCIYtnEuApQeczJM8Ea4S04EfmekRCxkVYLfxdnSVAEhegQnC1_u1Ji-bZ-a2Vdp2yTWlq1_W4wJA-cBQtcII-wGG2iPvv5PUOnreJmI9ch8pHofx2vKI5juOA-1ikqcitDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBYWhfM3AFfbAWEoXt9dXtcIiB0TL562GjyUOeScqB2O7xfxHg7paNpbe2qzlLAf-2HUhackpnjdJj3jVCmrAViRd3n05EMOov8dkH-qaXNSlLEKWGdpqbaVR8yRzuZD4NOQcX_HtmZS8z7odZLHziDBaRM_Snu-71_nR1Jo_W0vLyMOdU1i5y2DDdZsxTfMuwb3Tsatb-bXuFtK2oUZjw1J45pQyXPlkkQMHHlAr1HP68uW2Vfr2zdzfBzYlZfTf39oHXWAwvJorPWAnDh12sAwePFXTod_TUnTsQ7MzDfF9cujHfZi9k9jKzaZLL73UYjU4Iz4Wj5d6-eIJswoKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZZzKbJc4DdiOGLmgS3j1IoYd22WWbI2990Y-jalojHXmW9cpphh8iv5Tdqo4HECvo4ISOA5JeCop4Xt1QBkg3iGcXrh7k-C4V29N9TVL_IWdcdiVOVRYl_5v98Vh9qD7zPZVBS2nexb9HH5LUh6oDUqowmDeHFOlrrBGWCJvO1mbs6A5Nab52OijRmy-NwmBt-xVTZ-UC_w_9jg99oQ8YP-oAX8S4_CC-dw5J8GCz5icPu_b-G7pVC_MrU6SSbvlm6m6NxccFrB8JfC9O2OO3w2dQ0YWu0DeOn_PufP49wnsyqYvQ0YF4vm_OXVLyZBHuWssCNeVGbN2o58p1VebFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s_Q7D6npJHcDAK31f8bj0yg61KzF6WdJToGKhcxhh54PsX3fiwJb09eL0vYb2JMTs5s5EGIFtmi7JgR-zMLZYS2fxqns4Go4aF0g-brow41JbhILX4cABokEEd4hqrKIjr5mcNXIi3of6B1kHWdhtAUlZNrxOG7IwASinjydXDAF8TrSD2UFNEcj9nLE-aiSghofPPQGqgHb0tQG7hkGU-3TTPxj4aZ1lo5r-ZmdZuF59b9CqU5YLXNC9KK7-v6Dp3jTqWrV2Z1afNOS-epN5_5nvCxOjQm84R7kFsHoG5r82aJ4eJwVlMdoys_hs4YlecutoALYfMz6Nt-7--SRmQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=CPFdXPj1BMTfNUgnsEMuV0fRN3er7Ex9R0J6YQDMzFFEE-rCoTRH-MDeIv6IxweYq_5oZcpgFJDawXIDQLn1krcjI3EdCz1b2vuEBhWEw5IQBmr2me746FCn5mxQGsrt022vv0bPk3qAnRtFM4x1tEa3-zfeSM_Fg_X9gGLU2T_SIy2AA2YtVZK6seWQrrX-sui7cj4K47Y2iRTvM7BMoT2wE58mDBJHYg_HpqyXHOfZMNksW5K2SuAv8TN5UDEPmCIMCTMu-g9U-6d9h-rWnJ1Z3UD1AVJSPrVWH3TvBZe_SD2L6kkQehZLXg-xJSHMKKsMIf7LEAV7FARCllurPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=CPFdXPj1BMTfNUgnsEMuV0fRN3er7Ex9R0J6YQDMzFFEE-rCoTRH-MDeIv6IxweYq_5oZcpgFJDawXIDQLn1krcjI3EdCz1b2vuEBhWEw5IQBmr2me746FCn5mxQGsrt022vv0bPk3qAnRtFM4x1tEa3-zfeSM_Fg_X9gGLU2T_SIy2AA2YtVZK6seWQrrX-sui7cj4K47Y2iRTvM7BMoT2wE58mDBJHYg_HpqyXHOfZMNksW5K2SuAv8TN5UDEPmCIMCTMu-g9U-6d9h-rWnJ1Z3UD1AVJSPrVWH3TvBZe_SD2L6kkQehZLXg-xJSHMKKsMIf7LEAV7FARCllurPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=OosnbDX5ZZ6BvhQ5qaQISyaVPjWNVbzCl5rEDUTSJbWySx6pzZ-YeNw-VCIfNVp0RkR-_dDwP9bnoABomkCwx_uj-MLj3whgNnjmoPLfmAvkPVZuPS-ISHvEYC3sKRu35dDRnBK9z88sk5vYZD3_TcklSxETCbV6x-Oo751rt8i1s4S99w4muq83R64cnjT9giuAHvsECNjshi-fJDjTD3cuEYcdqjD6KMxlMwYVEJi_W-HmlVUGTnuVlOoChL9AerLEuH6xIUSp12L128roEk4gYh1-L7M6HvonNm47s-L0dvGi76YYCw6YF6jNMUTB79PYMWpZ9dvYO9dWVh3jnTXJNOExrBmzwHxgSEZoym_UDkRPqvHdWGAexGDT0lu1xsythswHydWECK6mS20yZ0wkvIYZIQMOxIlI9Tc8enxgMD-8opdeFkaW9pLpURkvlf9ZMKJP3OLCAbeS9QgficmTiuxxVZg4jTEixW4EROsDDsinsQaCfkHpzJD_3eoTWgJvCYg03eJQ0xrUMoqgLp1iFE5FlysuLhHPT0Zacl_yKA3pP2UfaIZTaSUoLkT5b3V0GbG0Eais215_b7qsPHqpyS-UrdFyerZ18zzSJahoJdRB9QPuk7S375evDnjpYV8n2vh0XOk_Vt6uUDdYAgb2Soc5zN5S87VTcmO-tXo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=OosnbDX5ZZ6BvhQ5qaQISyaVPjWNVbzCl5rEDUTSJbWySx6pzZ-YeNw-VCIfNVp0RkR-_dDwP9bnoABomkCwx_uj-MLj3whgNnjmoPLfmAvkPVZuPS-ISHvEYC3sKRu35dDRnBK9z88sk5vYZD3_TcklSxETCbV6x-Oo751rt8i1s4S99w4muq83R64cnjT9giuAHvsECNjshi-fJDjTD3cuEYcdqjD6KMxlMwYVEJi_W-HmlVUGTnuVlOoChL9AerLEuH6xIUSp12L128roEk4gYh1-L7M6HvonNm47s-L0dvGi76YYCw6YF6jNMUTB79PYMWpZ9dvYO9dWVh3jnTXJNOExrBmzwHxgSEZoym_UDkRPqvHdWGAexGDT0lu1xsythswHydWECK6mS20yZ0wkvIYZIQMOxIlI9Tc8enxgMD-8opdeFkaW9pLpURkvlf9ZMKJP3OLCAbeS9QgficmTiuxxVZg4jTEixW4EROsDDsinsQaCfkHpzJD_3eoTWgJvCYg03eJQ0xrUMoqgLp1iFE5FlysuLhHPT0Zacl_yKA3pP2UfaIZTaSUoLkT5b3V0GbG0Eais215_b7qsPHqpyS-UrdFyerZ18zzSJahoJdRB9QPuk7S375evDnjpYV8n2vh0XOk_Vt6uUDdYAgb2Soc5zN5S87VTcmO-tXo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s67tcQs2tqgAAJxBHnM8rdGuFkrN1U6QF6Ni3Kblri4wObvGljtBQC1CZFwEhywbBmmT-jj0DMCXV4QsPPJzrc1VdIZQQQ_U1sjgxpekk-bOMYZP-j5friXQlrikQDsqp19sEceCEaeviUKF0h3whfCsZTmu5VE1vnOAQjhCRIbkjTGdSdKOzqR1OF1FpADXHYQS93VrXsE-Btv3G8YQSkt2SyVoD26AzD8MwkOw5dRVN0boIje23UhDE64k5XUwXjQwnxZd138XBLRZV3y6LxUc1EMANAm3VKp-t0ylpTo6Pr8OnO_JyZ25mj69FQBwLCrS5Li7FommTghNHHe_Jw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsxPDNhglNlQ5H6tSvNkWfDlWHJQ_nFhS3fe5y3pKZ8etBloThqXtrrWdnpC7eBbt7Jxg5UwReZ-hKqVc-AQBgdQYzIWMpDGg5vww7al4lP0lcIlXebRdGK4JLnWyUFWhmbu1fc86uYb6mh-15wQJbod0knkCIYjYkG2wNLMACrYVKon7h_KNdtTGOMIiVxZfglGqgYfoxeQ_1dUfcxMNxuorvWVsu5Un51zjV_ScZH9Mgu9KjuTNDISPrD-nBMtgimsh0J5oHdBhciguKUhFaBnL2JB29aM8mZGapwOJR8iJPcD2bAPNLB0T1-A-HDTJdjVn9Grm1NNaa-Oq5T3Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=cEg7B4xDDTxZsCDG0lLbVui-5I-BrkLty8ij_fXob3EffgEsuvRRnIO01inAq8st4lTCckSrK9r4V2ytT3Kza_-caOlKiikZkWt5RmosA5n17Vn_YG9jgqVgO8L5qXGEGZmwuXXu2EL6_4C-oE2WQTOFbieF5OIDji_SaSF--fu_bkiLgfuDsE4bTbIw6kVQdLEL0WHfxYZMxztfeuJwBo263BVnfGayk5-Q6Vx0wWxm4xf9mKAZS1ZxzjBxmtBcxYSTi8aTHVQuotAwErogRpEYtLIbTk0681SXUpWxBFZiFr1UwbP7muYumlpygDA0WaWofffDnilEc8-HCTaQSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=cEg7B4xDDTxZsCDG0lLbVui-5I-BrkLty8ij_fXob3EffgEsuvRRnIO01inAq8st4lTCckSrK9r4V2ytT3Kza_-caOlKiikZkWt5RmosA5n17Vn_YG9jgqVgO8L5qXGEGZmwuXXu2EL6_4C-oE2WQTOFbieF5OIDji_SaSF--fu_bkiLgfuDsE4bTbIw6kVQdLEL0WHfxYZMxztfeuJwBo263BVnfGayk5-Q6Vx0wWxm4xf9mKAZS1ZxzjBxmtBcxYSTi8aTHVQuotAwErogRpEYtLIbTk0681SXUpWxBFZiFr1UwbP7muYumlpygDA0WaWofffDnilEc8-HCTaQSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6M6I7x_mDdRYPhuiurbScM48D6YsSNAGZbbHwtL-Vog7ulFDAe3xQOpwBr3TgLYu3WuCuNGEZ44MaVOwsojKXvjc0okqJ56d4pbdH6F26EXR_qInDUMM2PZEBF_xNaOZ1AP3bYYLdfFNsLFLtaWvk8EflMck_t5Wy50eMq0wDw_JQeqTeGDgH3sIqnDohkHvqb3cz4nF9y3UFpeqqs-rC7ViSFkuvXSYzXBSPY5X4KuRC00qvmD6GuxS41OJ-GbuNqGi-lrF95c2QHjOh4qsPridaMIjnN9E9M1xOeAqvDtbD39lCg_I33cqSELZtI8t09UNodHMaPoYz6Rp-qHJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lq86RxULqwXnl9SmNRoQ5egKGFnks45qDPDfxrsrZzHLo_UL0J3OxdFrM-4mlAQwxXf41SbEbJRG225oNiXFvjX8Olh8Xq7PjflB6eZjl8qe2VCn1ou1oXrUinlT6Od7rM8APCqgDy_N0mlBD7_fUkryNgqG-Pm5g3eWB4eQw27taKU-0Gb6TXRNBS_c6BhTrcuPlbd5IvpXq5BlCCXuWUwTX_XkO0U5IIw1LnYfaXCYvp9Fo6cbJn67vOfDSjZkIq9VxqBvlXm9NmkbUqjKdNx50pfECW4RctgyxHlZ-0jr2lDksSaiiFFGReP6dmF78aZo9HbW_ZcQB3LmmTv6xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lV43iJ4oQ7fFNGgUy1BAEjl5VLj1gJMGIokA8N8vZxbBolSUz3MmIH6eOUb427OmQ1YiLtqmM6Je0frRNZ-wSP3gWS-iZfkSuWcU_JqBA5LkEkcCtTF1SdgqdCBcUeyiYKWXHa5PcZjE7NGgqN8-JIDQDS3N5G4fhATcDhGs77kgLvaiwffcI6TqoS_LwgDocdB_7jf4sZfgAvfQ2_KZnwmK4JlNhnyoXC6RWckByAz1VvS94FkkgGLGxONoXaw2gJssfGiwGywvaLXHnTmkPJ2htAy2U-p_G8Q2ZLZqRxkvQ6RlefVwUxUw9jXtMgR8_ccVFuBwSZd0SijQQ4jU0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLW2O9z7slE1CPEk2kXY2LespNtMOBw0_nfRINi69IopyYzvefgF_LuH34zYh9YVXin8GnoGWEE2DkI9M641jcV08AYVC94ZqM9k7iT5YWtB5WYvOvGM3LCt7OQIbkMJ_Sszz1U66YIq3D-r8HUINm4hDgUbTv6_vvRE3OSBFFL_4qIfhvJSCzXMeQRNcth_e7XiTn4yYdfrQlWKrg7Olh39CAGdptbW1SF5CysV2Iv_bsP7Fa-GXUkkTSsH_18BNk3CdVPaU_wRmGxs_ZzfebiX0yaBSuDtGqOcKLavNrg_PXBtWnQyBlKmCwKko1vdTjsbsxaVMCjb3qEQw-1wrCKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLW2O9z7slE1CPEk2kXY2LespNtMOBw0_nfRINi69IopyYzvefgF_LuH34zYh9YVXin8GnoGWEE2DkI9M641jcV08AYVC94ZqM9k7iT5YWtB5WYvOvGM3LCt7OQIbkMJ_Sszz1U66YIq3D-r8HUINm4hDgUbTv6_vvRE3OSBFFL_4qIfhvJSCzXMeQRNcth_e7XiTn4yYdfrQlWKrg7Olh39CAGdptbW1SF5CysV2Iv_bsP7Fa-GXUkkTSsH_18BNk3CdVPaU_wRmGxs_ZzfebiX0yaBSuDtGqOcKLavNrg_PXBtWnQyBlKmCwKko1vdTjsbsxaVMCjb3qEQw-1wrCKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vcNZoVdYsehBWwrN2u5otUEqr90mKPNj5piIfQhe6C4VJfZr5Rv2LCIBJNDnbG9VMW94KuD3_BPXOjQBNAiDDS13TleEfK_so8HTijiTDOmE0Yd8UCUhEquyXiHv8VELUnBco8SwivRR4dDVo-1HEMcTIw-sBhrvV7GaR-UG7fBsdKFlj_pUo8F8Ngu2KOvdkIU75ZmVNqkI2rc2VuMqKMMHd0QfA0PAOmgJc0DleNNpAzgwgnru58ed0QxCCJz3tG_FY4d0JayHL4XxkR7ZcXwuuWSYHd44jVMSvW0mZn487OUv1cl2ebLvNv2JqxfvJ_YdarI4uQe4bT3sA2Wb4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lhc0PJt9Cb2TzCiaIYK_qyLwKoYjhyeC03h5Oj__6Da6mjAE07c5WWI8RwWcPxD8e0VYtK7-9gWI2E-kVsdrNt_YhadhlFSpxHpb9JjK8u0Xx-52FEiWpB3LROFTcfyuDr3UiRzLs0PK963VYBHobixXJ3d3VZGX07v_VSf4Gsomo512LA9qyCY7u-hT8aTgKtW5nkunysoAIlWDsq3oxsCev-p722shX8Yo9FTGmEw8rqb4RquL6ezfZ3n-7zs7s2TXjN02xx-Avxzosb7NFpTaVlPltBUl1KX8dNy6IgqS7t-4PHFBlZfwLaF_qIOjcBjijc9tDL-pJf6G2Q72vg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=ojaCue1WfqxVIKaRKzVc6cy-n6HdqM4tfGQ2GlrlYGi_9MOo_dInoiHugcBbJjYEXSCpBFNwfXBaiPdW0uotIdfFJwAgO7XI5KFevyq5rUocYz5g1V7N1tevLLP_c_3k22f6huMOI5268umzfY4HNqUr6FIwyE1H7aFiJLolIo6X27eBPtLlfga1E_zkmKbtyj5epG-hP3PLK2io1xP69SKB8V5kjSNf000UNTlJFNcY5u9mqRuE6tQ5aV24-Wt0tWWzitubG4EtGdR81HgMM8rwrj_1RdW6mPP8rXOvBs1TVITrOoW53yf6qUStjR5CDVzWNfv_NCnhoVzPSgzrWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=ojaCue1WfqxVIKaRKzVc6cy-n6HdqM4tfGQ2GlrlYGi_9MOo_dInoiHugcBbJjYEXSCpBFNwfXBaiPdW0uotIdfFJwAgO7XI5KFevyq5rUocYz5g1V7N1tevLLP_c_3k22f6huMOI5268umzfY4HNqUr6FIwyE1H7aFiJLolIo6X27eBPtLlfga1E_zkmKbtyj5epG-hP3PLK2io1xP69SKB8V5kjSNf000UNTlJFNcY5u9mqRuE6tQ5aV24-Wt0tWWzitubG4EtGdR81HgMM8rwrj_1RdW6mPP8rXOvBs1TVITrOoW53yf6qUStjR5CDVzWNfv_NCnhoVzPSgzrWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=wAydTwGJqVu1el1yg20XlN_aUcpQ1drhYlvgnac-wG4yepXi8I4b-uq6RWhCLbP7sdRL1QdZbAcpiRWpEq8gq8IwmJi10y2_qETwUlcAVu2c4tAf4mw285GsUPwnJ-79sRHAAv8zHYBl3aFZZCyoB2XUzvGJ_U8-EHrefoj3lIOiRc2qVJ_0hkg26xju6-1WFJOVwA4stccnTwCXZ2khkn-g0RLS66HRYfLpyUcu7f3-ASOnMzP-GucWlHtPo6_FV-T2wwcOcRLyeNSfjJ_JCEKs9ovNbD_zGM8iX71L8GYExJl9kWVTFTIbfUly0Jd_OeLdO3a5Fc_tufkWaIdV8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=wAydTwGJqVu1el1yg20XlN_aUcpQ1drhYlvgnac-wG4yepXi8I4b-uq6RWhCLbP7sdRL1QdZbAcpiRWpEq8gq8IwmJi10y2_qETwUlcAVu2c4tAf4mw285GsUPwnJ-79sRHAAv8zHYBl3aFZZCyoB2XUzvGJ_U8-EHrefoj3lIOiRc2qVJ_0hkg26xju6-1WFJOVwA4stccnTwCXZ2khkn-g0RLS66HRYfLpyUcu7f3-ASOnMzP-GucWlHtPo6_FV-T2wwcOcRLyeNSfjJ_JCEKs9ovNbD_zGM8iX71L8GYExJl9kWVTFTIbfUly0Jd_OeLdO3a5Fc_tufkWaIdV8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_Lo-nFf5kzDWNOt1XOUSIskilY127OW7UehcG8nUo-JM5X9ZDwOSdDikYmiyVGQe8bxq8ObKoLDpncTPBwHCL16Yo3BR_XhemN5PkPj2c1bRRTu69x-_SKxq6lo9-NeZkT_AG6tufzfCkG1LxYE9XjuVDb_7Wn4dqR4kb_q8JpHfDxt6307Pzj8dztzW7GhRkJ0WJFFy8Sn6HXWgVVZFk5ZDaIYksaLaJR9f02-D-SMQmw-Sfso6Qf-BMaVZCX_-tJm4rBTG7uxLl6CqZg9Z6rDYpATmHZXYkY5eUxwe7b0NNmmSmiA8z0i6_LgagSo82yozd38npQHF5vLMe3wMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyG0RTgiTGQ1SgOOeLoedsvGiMXzfCUc9wkSKIXstb5XXnJDnBGDHEtlcj10FGUk96dojRumKhZ4_YnCpi3BFfjTdgCfDXXbfl92lOSdZgWpkHvQk7XzydCIReKFcEl-8GoJ9mAiKXCkBYRQs6086Rt3MfGar9GCd46D_fWdN3Riz4xWYg8DeCSMxuo_jFweprZMtGL505iGyihKsVaQFfC_3IyAGqVZ92NFaIQihrTQS8QO7nuQYgKCoE__XYJ7nkEtLmbnPpRZ66_k950N1u3oUkwNmlesKveOmr1XyNkYRj61oLOqdGdCjuNQFgR2j0csTNDIG9ajbmO4n4WAIQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=W-V0F5BVk38YX4Vy3XW6LiycqSgd08_IalHK-i9aNcEPOpYJu43e9OAmTqvjL0NoZ173Qq3yOHxo2JYXyzbEa7Jc9d7POv4rJOv8pW-a4kccRE8VZ6_U1h7Vq9zUCwrSMsFfIO7mQ6gUKN9n3dCGltctygqMNgsO5iSTiOOVCSrOZZJOZbSA0RqukEqa8XF0K0agu466p6n7xlSvmqwRGpl9cwre7LW-iA00u5W-0rp8uaRYBQl1grUk5tDwx9XDoCrIX1Ca4XZF2B5wexfp-vKp5KMXvEBnaegW79f2EyQ1vyC50nKZ6ayDwuZjDDGieDVmk26fnE_47JNxsKsFcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=W-V0F5BVk38YX4Vy3XW6LiycqSgd08_IalHK-i9aNcEPOpYJu43e9OAmTqvjL0NoZ173Qq3yOHxo2JYXyzbEa7Jc9d7POv4rJOv8pW-a4kccRE8VZ6_U1h7Vq9zUCwrSMsFfIO7mQ6gUKN9n3dCGltctygqMNgsO5iSTiOOVCSrOZZJOZbSA0RqukEqa8XF0K0agu466p6n7xlSvmqwRGpl9cwre7LW-iA00u5W-0rp8uaRYBQl1grUk5tDwx9XDoCrIX1Ca4XZF2B5wexfp-vKp5KMXvEBnaegW79f2EyQ1vyC50nKZ6ayDwuZjDDGieDVmk26fnE_47JNxsKsFcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا و عربستان شب گذشته
به چندین مقر گروه تروریستی حشد الشعبی
در عراق حمله کردند و تاکنون اعلام شده که ۳۲ تن از این نیروهای وابسته به ج‌ا کشته شده‌اند!
حملات به مقرهای حشدالشعبی در ۷ استان عراق صورت گرفت بصره، کربلا، نینوا، کرکوک ،
دیالی و واسط.
در ۷۲ ساعت اخیر حشد الشعبی بیش از ۳۰ حمله پهپادی به عربستان انجام داده بود.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6403" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=teFOyrLYu6lKcXBRpTu7DeoFmfS7Zw-J8ltfzChhcF4Lc0OPINrNRImFR4mPVXyVXLF5a59morniYcj4S6sBz8T9Wb7ktjA4YmgTnH6JQiYfnbDKta8O7EroVw-cIZHAVoP7evgw9RCNHjeGHgu8c8eR4lfWCPO_UEuD6CXZq_P-VjJLYbXnJGcbqD1lBmw-VqLGg2erTV3IeOB94uLI4iOv2q6Vo-mM9MI1ItJccGH9TtZ3oOBDZ-46bDokz0HKgLnKIdyCVJEQacTYeJOFG1RUXdaYGo0oA5cZcAB33jyBUNFK_kEntymPitnNSWdFeXBHvGxcwzTCRpcziprwxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=teFOyrLYu6lKcXBRpTu7DeoFmfS7Zw-J8ltfzChhcF4Lc0OPINrNRImFR4mPVXyVXLF5a59morniYcj4S6sBz8T9Wb7ktjA4YmgTnH6JQiYfnbDKta8O7EroVw-cIZHAVoP7evgw9RCNHjeGHgu8c8eR4lfWCPO_UEuD6CXZq_P-VjJLYbXnJGcbqD1lBmw-VqLGg2erTV3IeOB94uLI4iOv2q6Vo-mM9MI1ItJccGH9TtZ3oOBDZ-46bDokz0HKgLnKIdyCVJEQacTYeJOFG1RUXdaYGo0oA5cZcAB33jyBUNFK_kEntymPitnNSWdFeXBHvGxcwzTCRpcziprwxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PII54XNPyz3x_CLJ9X-MPx1vb-KP1GVqQHdQ_INdFu7q2KjMAMXDvzU2XSXWC_WpIdY3cuH4CobfgFbISXBeAeM4RWetHfGJzTbvb5we-aBQic7oSuXgO2xhcQrzcCtiP8QJ-zcpVyJIOd8NZntgGmGiFEY1nG819wBJZHAFkzpYfRbEDwVtmxphBdrigsHAIiRASMM5Kd3fPl3ZuNAA8lwJTXrPdefHql5UYO4fccKGJeyuXgKPSNCLEmOK8QDuu601Lq9DeviOqLZq92Nh-z64OraLvDzvxj5OUxiX8A_NW6Q4bwGO4i9zxnVwooUY8ARAxwrrN6HJdBzHjIp6jQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juw8MbmGiAtzO-ZKYmdZS8FZAWjrtvUpSnYR3ezM2UpDi6jCnGlhzjL7zYnU_KcnUsxcN4Ib2U2uG_rPXYQlLfEAj1EkewonNCyCeCmrMLtNTwxu8vWy8nBmS37SwVwjtZ8qLaDb9h103WRSQY5IvpnP0Hk-IF6VDZY1kF_QRm-pr_wi-ek1WoP_BOTqjOiL8ZTThzFxX0GNr-NvVJUyoh78bqgPUoUFazcoA9mREqYwgeAUFKyURCq9bA0vO75el8C84M0gw_U5bU1WQa81OaCpwFiKVzz2ETe6qFGWJClv6WVrniZW7oaXZrBNKzHQ94__18BoSSxN-qzteBbypQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKC_SEONo-ZR80mPuskx6twSvF-zSwpdcQMaDjn8KY57dN78D8504WHJkp423sXomK25n12Sp_p5ezAkOaVRaiuJFyHAT1nBy7rTgg-MSoJq_Ngs_RcayPVmKis5US812Zc9EIw1tDTX_rNrYpwyJb8aGNFUGDZQff0I13OB8FzJyENJfnxPVguBvQ2vrQcFMgbOr4_fOH12euc6DHtQn0IIMdJgYjqLZsRY9Xq3WOJnTony6kL1-Rtr5O8-oKRUlSPMQWSIX6KLE7OR2k07MaXQ-7reMiS81Lqh3vkAFH5QVjjBmu4kwNdtYiaTr0Q_qKFqPbXUjKo3QjMBxw5Mzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzMqO1grq5O_Hmb8-WehcIoDKWxm8X4acR-lMse0ybJjByQXCdEdQchwh1vZqZdGFSY91c40DYhc1t-k27znN0wDFNbRPlQM0oZLNZb3zEkVnz_rxndXy8qZ1JKXp2wPXnLCWRlr0n6fcOtcWqiaUm369bUKsfkyJj8-Ym0iyZzaOuc0w0a6irhCiIB1B1F-HdSQeSdt_odHXEx9lL_30dl3HIr8CDsB-BvCMBp54SKI13dxncrYxVqsf-auXnW9P5J6j-fMErwGQH9AMoYv5CvqBKdFVDFd_f4-xN01MSZ6HCnSzUlqoqjBcX7oSZE_BpnrNdm5NgZ0HgF_HUDYsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TfzWOE-_1Re7FHuY6WxxgvD2BcYQJD4HZgtjQnUkxj4q95oi16QsqmQMehboygP538qFkAmOIg0epVp6Tz3l4riKdKLGzJOT1_ZOax3mUOdAdfE_qbJE4lZLnNuqt4NusH5T6v0uwlqFFCys4M_2cgKtTWsb4CbQACV3H-_KMRJPqQ7F0YA2Ia_R9BWH2-_EbjAIrLX90KLq81_s_T8-AEMNHxtzqQ4d68xrVqMi848FoBGWENV2e73-mD8XjIHU9OoNohyWZDwvz55bP7lDGf5lGwY_c4R5mvzcWGnTz53GaSqbn_j41s5Of8QizkHzO9elSgKbvrQDAr3ZECrF3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QpHXF-WkvHKLY_t0wK5kfOpJxb_JCKdIsmwMDV8Mvko9Lg6iP8xt2tC_R-QlXwfOyTAOVnkDZoy-EZVr0T7lpH1ZN7n-M6YhjtLT8BzuCo56Giy9Q1kaSSXh3DzgBdB_1J7rz3j8Cm09Pi5kqm-635CYyETJH8RLBHYqoe8dFViVQ0Y81n1SlKv807airEmmUuDL1cCTfMdoZJFlBQ-QVMcqS8yy6yT3Lil9zfdBxWyUc8iqTMTzf1Nvgpw87-4KLiuHam8cBIjteNUn0KqMMmghrivKFtWcBuOVt9ZQX1KD89xBeHimDBpGTL2mDSZtK7qunmLqRWtyBbrFstzZeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6VwF338xt8i9s6hYWDC-15QD55GMXj5EXFTjX4WG5SaqOHx0UgVh4PPEMMtz574hS1EV4CNdj8uolW0Xo6tssRgNBywJOpyiZv8tDUk6x36JZ8WL1MQGQciZzOY8q4N5QMbe0_ABPTcqx2V2ZSQ0EXqiFEv5LZTGI9IytmDznAt6wgwgDk6C_QzJDNqDndZ4RjQ4v5hWhoROMJkC6QFua3XZbw3QLyXDQYZPUmgDD13PHkfOfK7sExYhSZzWRBx3PlaZYPMrRKYfCnRD7uGUYRhaH6ZyMMyCdOJfduun2Rb83AHiO6sfN-cZQr-Vpis8z1LtXcgomEB7FAhyC-0-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T1MAkOjsakyJ_1LhORl3ElbX-KQ8SaA1b4XxnO7JiB5VkJec1pTu36hIGlwnZ0B5qEWF3IfCA0VgMiI21OO-Il2Lz8QA5_ecxKprlSlDJ7q3FvN9Oa79aN8t3gQSROVx6V3JMJr828EMWbYhmnAhcPSQpOG0Yeifx4I8ZBTGnBzkV0UbwJxs6lvfVVAI06dJRmOSN9unxOYiGC5sG-a-0z50LzAam-olaYhKCPe1Yac6e2udLEYnY-pYLz_jvsVZu3eINUGShlQoq_adzhelQD_rdv2JD3SBAMgicwvaqC9mcCTMatDx83BRE6QyuBz88cPblDIaDJJMsbzPAw9JYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v34UN7GVD6XmlDV7RMrews1kgAkLQZ7FdBX5WLinS5_Q-XabssTSHTCW4sqfyQLZIV4FMRkoFS5Ub2NqU-c8_zlCho_ZukOxuvuCejJjYbzlqVqMrc67TZhBWfv2Nxym-OX7gNC3jqg-XwmhFWK6yij9W8Tcil8A8EDnUpIQERdk2AOpU4YhjfO6zjdAfEszagkOTqybWcZHURKBx7Czq664xuobYoa8MMh4XXqFfctu4fpmhJL0nqIcOePFBLoWFt45xFawSbFUUZhYhxdP_8z1myu8ZxEeBmy1fWIU_P-qjbN4wlwTmSrZHsdnbz3q-LMLn-CFqw3kPnO0wammTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFYc9Z9-Cf9HSJp36wmll7MUWNUdAXvPlcxCKjFWSGhhwKxNuQJDnt_3X9HOINn4zBY4eBCT04zJEconu1dBwTdWIIvzJVnck6pC-euTCetxyQlpp5GWmposBNmlgwUFZNK2ZHuSzuC2MhzLBP2sn7O48NC_Xf0vQwzcRylx-uHmc0BpCRzMpMpBq9rFXjV0vIWynQUT9oMK-tzHiHlRn3xLBTMjxcCxM-V5yKs2DzahVskEHviZQ8cIPr5af3Bbu49TmhBFHQX7BT0TgV92H-nMKh_016U3EvDhVWRPr3fk5RWMqORblhwneilV04nrAAq1LT2WczcdTK_0sWTanw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=gpbvihAMJZD1liFJk6hFdxF8YyePGc3oTZfVmx1twspSgGPx6zBGcWbV07CdbeM_5KxaO8ti2Fe4AvqCRXNsj1FErNCNSWK9XzhQFI4hCKX_5K7t88D0MQfkRYcV7dLi9xMsHRmJ-eDHkOdYYNhzJDeWhFfF_sOiJrPVrwSWl8RNB4m5VXg0OE6xavSaRfxperWt-P1nH1U36LN_4zBUVPmMeXTFg5LXFJVtqgjBLnKKJ0f7c-RJZWGT26WWO08gFPyYyIJWpTmBSeVCHOpXXwnbHBTt-9ZappfMYnE6wo3EfautkGLo1c1y3OROGxtmpCfHsEB5x5_yWfQ5paXpGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=gpbvihAMJZD1liFJk6hFdxF8YyePGc3oTZfVmx1twspSgGPx6zBGcWbV07CdbeM_5KxaO8ti2Fe4AvqCRXNsj1FErNCNSWK9XzhQFI4hCKX_5K7t88D0MQfkRYcV7dLi9xMsHRmJ-eDHkOdYYNhzJDeWhFfF_sOiJrPVrwSWl8RNB4m5VXg0OE6xavSaRfxperWt-P1nH1U36LN_4zBUVPmMeXTFg5LXFJVtqgjBLnKKJ0f7c-RJZWGT26WWO08gFPyYyIJWpTmBSeVCHOpXXwnbHBTt-9ZappfMYnE6wo3EfautkGLo1c1y3OROGxtmpCfHsEB5x5_yWfQ5paXpGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=TwYAin0kA5ZRjTGI1KyQcdjkATuYbPSDZq7FuufM4aKtWZiwSl-moBDYULmfnxcXUJyfUqQOpyC7KX7Unn67YDUtkpZfL-mina115mI5RDiI4coAgYUcDZkmw_nbB0nfNaIR3JgyZ4re32OIUwSMkhEo-DLCWJdn3OcUjFjbbLI543bn78eq5imhTsYBLdngnwbByNxW0msD1t2a6JmNOS1Prwq3mFBjSJBGw2AfEIzbaKpc6HrW9PnT9J-JqQEXfm_bqI7Ypw9eA0IMrtbjFwcWzVW8zaq8_q0FfJb2vptEFsONiHMrFTKAB39fOBIl7DmGPqyyCWeUMlHKSgWPtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=TwYAin0kA5ZRjTGI1KyQcdjkATuYbPSDZq7FuufM4aKtWZiwSl-moBDYULmfnxcXUJyfUqQOpyC7KX7Unn67YDUtkpZfL-mina115mI5RDiI4coAgYUcDZkmw_nbB0nfNaIR3JgyZ4re32OIUwSMkhEo-DLCWJdn3OcUjFjbbLI543bn78eq5imhTsYBLdngnwbByNxW0msD1t2a6JmNOS1Prwq3mFBjSJBGw2AfEIzbaKpc6HrW9PnT9J-JqQEXfm_bqI7Ypw9eA0IMrtbjFwcWzVW8zaq8_q0FfJb2vptEFsONiHMrFTKAB39fOBIl7DmGPqyyCWeUMlHKSgWPtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

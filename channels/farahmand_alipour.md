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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 20:14:56</div>
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
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farahmand_alipour/6492" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHAFBFcnvXuewN6H6Mr-97u3vLAllyfEvjUOEngOptXF5VjVKD77NsS_E_iJrlkMXWZ556Xek-drGE_lpy04X2e7GNm02uMBa_7gEOvaNEICvH8rNFRbbKHHy-uGxfM-zaoE7PRob_v2vIgrJoWMO0H68rVbtdriag0Kdzs092EgMtSY4V2BlB8B74OmjhzSSclgeb3xiWhWdFZ2LGFRgSdyemtnKU-n4XgxEEeyuZCi4ers_RYpaHxp5Krsxs1TKMv8gabADvUDZjnitiv8wbkMLYZfx3sS6udYvyeZmheljitgGWmBTPbWvCdTk_8vuUicl7xRFQRIBSqmO6ojOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtGw8K29MtYV8qwafr_11h5bRz6yBfjpYPnJo9K-PgOF99nRNds4_kh7tDCBMimQ2VIAYyZJ6MeKqpjKoElkijYzuL1fz8V2CYyt5ai611SjXFP5-vxBeoYPNdhEiyXYWdECQ_TqCp7nnQWACcIkH55rpVy14xSsbVca3Y5jetrnO5UIAHljd_hm5KaWctJmYDCooAtvBQvSeWzE5rw1xtg2dYy5iHDZ7clmneIfABvJop1DFKY-vzdiJ3FVTtoLD81I_pe8ZJ5MkZlLA85k1wMJkFCGHnifJCXyNvt-FxaTWAIBvRovrTyL_w1QDmogThlhwlpnDyeDz8_OrnSKsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tj2twco5ejiuMHZ84JP0wcvFlzHd7OaXlxdfIpaMcczC4D1C-5J_hIgplXGFT01_etp54A7AIOM4fCeRPnaVfBSPqEwBPBJ1e2rvOZLK-VXGwSPZj_6NlvZ1RAJK3umTBccGpce9VWvbP3JPhnYnSbGfeB2T_0jmKeJkxOtQVJHEfZQ-yocsV6iKHjiYnNZ8Piu4b5l8uE4oOuBDb3rYD5HzbHrbPcGDySvu8u3HEToMVOUU7PQ2WhmnIEP2lHiDji2C3jMI31N76zt4yMb7CcYvezV0OEDT7yIQGnEUJA_wURgcOdK7pt9syCcCaQQDJH0_7hHif6NcIXh8S9PUVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gikmSGLqJGCWopa-vcotBpNI08bGSoUBEUQ7JQi2Lap48K3EZyWJ4y2iF2wq75F0Pvuq2stEVFrE2pz1LGmuJbdGjkA7dTmbSmDjYfo8e3XuruGJfhlP9osPBY7u-H06augoQciQDY7Gw3Oyh98Xbf8eHhKkZZ-HzKS7TCxX3eRyFRMW5ofAU1sV862scrND3n3RxpjPo_wFT7pszW5kBJzv7PlawCTp1rRt_bhnkOLEAbVRvNvRkrACabV1swzmMEj12-HkrvZ2QqSP03Kha5fJ2R8jR0PHf3i4fcukgbC4Tpp_N7h7Tt6sA8J8cSVA1RNn4hVU9fvBrwtWRhrrqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBsRqkdqM72B8JE-ckFufxObNJaBFXBVYr6QoRBdWHWtMbKAaBKe91gju1-ecvjyNhOhCoqvRp0YhnJxfJo2sBRFIEgnfMnpBi_Pa44v8U8bs3kDIF4KzBZK6f4T7JS9cl43nH9oIwdVf2fDSaTnil1EkdpJ-aeqo7sTzJNr7TfUamvCxaKNna2ULO-Gka6-j0ZyLkDjQIVZW1xNYTNysidFK-DAJ3D6TCDI52WwKBlIgd6ozFvZgvowPb0aZfn5Ex6jdDXf-yEF5OeWiYv8JHH1o3Co4A41TtOUnpbQsn2mSAgCEVu4bl-ZKvNMrnMZxHPPaUlKc9yPyiMuIfnRaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSckZ-TBIiTdoOxEDmXs5ytxzTVe6-XRoW4mCU50uoAiaUo2gcifF-ZFbYHi56cmwbaLZ-13ijgG2rxk9fWyKri--0N0sMCSDgnLVARR7D7SCtNz7JGf8i3_YZ8kdtS3datfRwgrQKff2AEgO2wzMKWuERqR5JGpxk3yQXQQpO04ymIvA8UZ0fR50b1NJ2-cUTHwfHT99nT2lATViVs0xjroOYcI8DDPycgGZ3DsGOXhRoSJLjGIVQpcCDgWkmFY8jIsfd0Rws37eJsV8qnsqZkxGl5m3E_Ekc6VjqHA3i_1OK44q4xlb7synyfzgB_2Kp_dgZ6VNgpB_bkKAlQE6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQ1k5UbzFqqvs0wJl01nz9jJJF2d1O8Qzw13R5o31_OAzoewIa7VEvd8833-vddTL8gBNkKFtQy1Zct7FZ-WgO5RWdXuXsT04iomza0KlfXmZUkHADAWaNanMeZlcSm4OVzihmNi8wS4IRMLT5mTEiLXgYo6mt0rfaoUJlx_-jDoCGmEXUc6Nod-7ceZtP5qRb6iB3jdijhkkZQDecQB6YEtNxLPg0ZGDmfeCL6UWPuwL67ApKIjVKWYWQ9EhVOz4e6SkQY-6mSB7TB6yRXgvMoNAMXR2FXvTNQ-KJPTFMZwUtl0qhGZz9eQsxee0Eqys1ncHXDLFWZv4PWwZG6rGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-uYIYkUxeuWcMkQ5Sk4QuOMxV6E0Mtyifht6gYLv4p0Lx0yAOKqeP2tMtK7r7I-znH_ph4PE-TR4cKtid54Q6hmIv5eGTcmAq9etpUhUeqaq7WPKO3Wtog-_t6GnFW2dln_d0JmiyGKlstkrO2MaOqrUyDcu5pQeZBlRIx_EJ0_ahzFfW55NxOUSK2D-lrDIkxxl4eTtmwXO6Qjcfb_J0m2xFW8VXCvYTvTl1NC0QqOzESHyhtXFoE8a9GpClHH0avfxcaJyTljeME8iI3DyhxTTEq5r69tDXT1i2AacTyckCnf6o1XOaf641W5vSAOmNNE7_3s4o6Sxqb-g0lI8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQegXSkgHUzyOVrtA0fNECy1Chq-PphCRQzuGM-rwjVgubTBuKwruLlNOWXqx7WUpl3gKezgRdHNLUi6Tji6Yi7RBHZYhR7ROJ22COXcZ1q0wiyyl2G3YpAWE2F46gsRfXxoUQGknD1slmCIXHno__Skjc_qkA9cZ3vhWWCdiSQI5u9r9LjNOQ1UhPJqhFEtmwI2jNpF0tSHznMPEAIkxR0bz1nrO3cKrMSxtvh8VtUAkRx9GT16UBNeOLnoyVtKjjWqWKtq8eygoSDCwVLvL32qCtJt1HMC13KnXu54JPPXIzjumA6pLev7mcqL7wHT1RKBQh6vQe5DPr05dxnBBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b21yOC7U1ZrtHxdvG74FKnhw4Gma9Uwo_1czO3uuqx_lMKWFl75WI_un87Qp7QW0PgrHkPjQ3AqW9-jdETdUntk9pt0h-_eP-aur04vnASBnP-v4uKe7OhGfKd_NifryRio2iexFZP_z4_qi_YDh6yBLRxf71iTEp9cuI8pOf99G-9swQExaGoaWi8eUR7Q5WG7OzxrotLyFjH0Nu8IdhruUCP0WpAbp9eJQWWabTKEgwXEVUh64RoV4dH0WlIdfgKXpRD6G7xs4exwH8UPS71_Zy2YdhAwpNB4xCblX13arKJvYeuf8_RyBRqzNRP_wQkagP9SaL4agXMr8yCK88w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYed9fUA93dhYdfNmttVcm-2lUMw13RTbLImI-z9mIYAp3Fn2k2kwxWO1ig3HF9kt__Qd30l4m1S2SDDhtjk5O0OQsidkXQ07ucDS_PfMsyPqIF9ZhT1o8M2Cxsd_EbJQdDbi9aBA4SfwyLGuP6nOffLvRWw7t8OIr385KWwqDP63fknUcx9lGhmSwZ20KPLmq_5e37EHVefD9YRhdJu6ixoSXKTToGezCK0UiQndY6nkAU_-eRTxFwse4feS584QcekMbB0tAYzlBdDkGKmgpvLIimfjExjasGpdPQADAzfOTbty7ziR-RNmt2mTKBDmtYnfK69_5xd6506jVO7-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qp-uWfFXcnmLv-0yLX9U0HSaaUUxpVEYsNA35IzA3RZ-mM09Z8qB8OWIInZRV5Fe5j1ZjlLlWA0DazcSD2o0xu8nMZ3ylh3dgmLYJw4cWa_sQc0zyzCin0Qbvx1roTzR6johL1kwCcTY9qRTifFt9OubskB7kzNkKy_yiCe2wjUf4Rim-bMz2KZahHQ25ckWSh3Nebd1taY4UxIihZQn7f69pMlL-EJplk5JVhn2Yw4agFirJiH4DSJsR70EE6oEzkzw_d9MyyExhc_W7tCeH3FiKLjiprPnDrY5dfw_ZNe1cvNuh7Bq8f0xN8kOgk6fnqMRLOmKSOo82voIFrZTHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAD3ISk66tWNGZjVWSlzfTprYYqcpZPFGeom-F1kWBpbBNKOUai2mLQzqM0mHkPLFwSpgA6AdmzRSgA4X9bkN1ISO4oJ2xh8HtHiYyGjMtODCWGvDdPH4mBOHSQlE1cAK0ykeU4l14UVM2adXD0r_-yNSr37iqZvIZVaoO1KI_RtvbAYOFy-q1JlebV3gVWZnIpcKkQeZvn1YFzxhoo9zIQ8vrd8ZeLw7pI8lWKttYmsOVHfnJFvW2gAoz7O7rrPOFp_b0DyAIiJeJFrdU2yU6vngYivCTULypb1fy7_q2FnBCHchhSdOWBY-J3DKga-sJAuS5kkEDO7kLdYqTeB4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-7ZJ2tRaZBoYQ-quxq7oiiYk8mAt4b_UcTLWZylaOpwjrmhZ-BLTgmcuKWl9OYM9_6GpBml_CzXMmLCZpqlrrZ9Q-eVnLyXxEWJhwR6hz6Cm1CiNf-4fsIE3HLWukQB19tOlQixnIzFpc9zZfnJRg2yf20fsH4slxdOtRfZyJ6AHH4ydD4zrSqyDy1Tb1RI_reFfBKjiqOoJtqR2Fs2Eg_1KxLT5QNV-p0ctgtsrM536RLp0nB6Z_6HZsF8ThQOsf79Od7PluLh3wC7YMEm-WIF3N0uMdibkGERZukenqV_O59nu_vdBMYoEEFXi30cOb9FfJ-qmUsNnpiSHglGag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tk9qdRaeP-_kjYbMwi_KZkBCJCfUE-5AJeAkLb4EIdM6episKX-lkr5DGF5i6wfWfIOZy001skaxMNRkvLk-CkUGfpa4WBfwst64BLyOlkdIjffeH5bKVK__k55ypwviMIOy9CAQ9itJ0ryDRcTgUM5X4hBnKawKdCqStaQkQFOoj_OpddGl0PVkyDoOAlAOfOFyqobMrpG0LOYpmRRYgmsDcm2BpE4HxmCgneCsL42LISQFZKRyZQzn2kbOE0GaSuzFdC4AkDhDlhO6RFHMlPjue-cJ_UUZULLxGMwSLPO7pzmfSbPmUvY42Diu_n7UY2q0JxxUuMelyXcjwS1_EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnzahIL9_X25dBGOMu3TisJ7dfoKC_0_IX-c5O8lKdAP7ptw87rDtaz45K64b8DP9yJ7FORnEjuU4D2c-d0wwl9H0hC5-1LyzU9JgGBmpkSd0LgVmg9P4WES_tkBysh64thxKocHSuMw68PPxMIU21hps0z4oCVyQoeVE1i-TiRdqpgwjVhKFG-lrh4-AcBPGx8Fd-xPxYnsTuK-WN7qvULh4liWcNZGcuCFOCcU9NLJ8eKMt1IG_2nG9LtZ3OKCY2-7MUNCJBo7p6HbCnRp7IhtTQSyG76thSujaWaees5Z2h0sicoFKLfhMJPeXg_ngMgJYbQG_f1ao53T-Aelcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbG9_iEiJ1ro55wWb11L_TwR7hxywVoO2kQ-1yM886TKEF4IwAT2o0Tm6PbXv2gr7ASiNRPNjPg8AfN8O2PWlGTJf9v8SvjylOLYoxSjjw3jdnPQsQs-nGKf3k1s2UdpOsNuvvQG4fdYCj6J3O9Ss2hyiW7wX1N2glDV4p2voK2U9arVdncgrxc6lu-kBK3pCTPCwH4rxZ4_zf1N34-PWWiWwpPP2eZa7SRvLqPwJK3F3Wp8VSJx7bneQ8MsqJAgduig5CwgT4lsw4DKdygbGFXofgKh3gaH1SyAJncGgm2t8w7Jec7KZoFk-AnP66c8rCGV-J-CijEWT1Tl8uqevQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sgbj7SvMADHF21a2gDmfTuc4M43LQOXZak2uWNNLlr3uT8U6yL5XD9QiWMqzFqRoafghTB6sh1VsSBchjhd0v0QsM0qjQVHvKf56tU-ofCtOQGgFDWZ1XJYBupsjNZLtNDDbri9gWstnO0hSNZ_EEjZUcLlaWMe6LsiHYtg_CpW1sfWD7rgNo51bk1U0ccQB_AFsQzGSYxfn1KD9Q1AEvuxeQUt3NY4i9Sv5VV6mLejM31J4GXaz7ceTpFtYKCG7PLt7wE-FsImh2j1gnkd_aFTjmesv_tytXXNeScfa9v6NgfwcFfcqzaOitg5hZsh_VSt-BtT5e5wS-focUbnkjw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=GMsLH8Fl4mU-Gp0yCQNkXrWvuBXmhnJ3B4_tUn6JWK9bwWlqYkrRGW1BuCXBc16SFBwHWnLCvU-EYjftu_MuvcqX-HJnRSZ5n7F0aFtjcVGviZ9PbpT6mv56-TyYBqzIamfuzX3LiPuotcRvY-eY8srirFS3tHDYGDrDVdCsjaH9zmKRwMiaB8Ni0VXBJlSIQ1Btx84_UcXnVGThmlU1-gUPp1oq0Btnqk_bdB1ZqQGrV0pjwnZE-t8ISXxurH2k4HPo4lK4kB06ZoRIfhmh7AqGBvq3jKREMaurf6Ub3uuTeWZWA0_rNcEUQIbjTpPmTTpJEfQMJEzzu-oURy5-uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=GMsLH8Fl4mU-Gp0yCQNkXrWvuBXmhnJ3B4_tUn6JWK9bwWlqYkrRGW1BuCXBc16SFBwHWnLCvU-EYjftu_MuvcqX-HJnRSZ5n7F0aFtjcVGviZ9PbpT6mv56-TyYBqzIamfuzX3LiPuotcRvY-eY8srirFS3tHDYGDrDVdCsjaH9zmKRwMiaB8Ni0VXBJlSIQ1Btx84_UcXnVGThmlU1-gUPp1oq0Btnqk_bdB1ZqQGrV0pjwnZE-t8ISXxurH2k4HPo4lK4kB06ZoRIfhmh7AqGBvq3jKREMaurf6Ub3uuTeWZWA0_rNcEUQIbjTpPmTTpJEfQMJEzzu-oURy5-uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgZ3zTN6w59OuFD4op85BS1rNayjIav4SDXwuiBKNVEirlnfjUqG-FloYu48JEQUdArMMpMoJ-tu5VTu6YJkbC8DEss874yo1ZcD9NBuMqnDa8Q7TY9sCjvyY3c36vICu0nwksb9R2JXOzCrCDzg2ZNpMJiuGDHKhJqdgTvk8PM2-tFjERCnm08PNdBZhbsq7tCIYzRASV7kUrNDINgkYc896I5AEFcmwEzfeghcBF-2d7loUWEPSU6VEPbnBuHdaz6_hNmfRaU-3DhrfrrbK_eqA6kWTnRIUhh-rhGlPUea8__3jvKH5eIPNxdbIbD_FyhTolo3zTFWLK7yOE3Zdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPa47igBeq542VFVtq1ORkT11hKd0ecnZ4iuGG_CIMJPPqLHIgAVNQPo4_mtNXQTBXdcc34izKanwnOTMx43RMoAWGtp2d5InXswvaPllmR3-QX8mxD4xqHQS_bN1Y7ooz2WlP5DuaqsP9yvIGaPh-q2J360AHojiLWgN9gAoCNFNSK7W8E_9YmUzpqajMCm_4tgFv2r23cuiOZEKKu1Aku29Zo8Regqu_PuTvG10fSfhZezlXR_tRThbrCXqMAUxUREN2O6QqVl8gGHo28eExiBJcB_Z2iTVEhRxsrnnPTboLnjex-Kny8pat3Qj3QSLa8sM5am20jSIDBwgV0MpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiM_icpexdWNQohnppSdCUrHD61ggGXecpzRplrl3cS8uBfZqColleA23mHGpkxWT4Ik4eEMqQ9u6DcuKFnFiJ6cLCKU6WDoxmlh9GQVEs_IiviqQu6fDgi4v6oTxwlDRtPmzwlELeaUsMyt6qUNM8ckAcE3kUMyj_dyfU2I462molp1DioeL7dXbA1hjkwwkZpuTauf4RQ98Ng29sE8xOXHwAueiLF7oj22ZHERRZmI9d32KibFc1Gccki3vkuC0r9zbs8Di6Dkhv_Y4htsJQoAymSGeaj2HpGBPrcfQNn7NMBlE751_-is29btnmrWW5FmB1YNYCeis4Aesgjbkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPyCWxMAVUBkseXHfzXFca0W9WknDn-5eFXbfQ2TUP6a35seZajSqDQtBlc90Rn-7d67cx963d_EpMlURHEi6Ct7Vp2JrYnbgXfnx3Y_EMxARJU-MjM7s1TGQs8eijjCTibbQf8bMeYB0nhhEVS66Orsf2FJJCYF0EQ1z77fmqxF0k1gyw2Fys1HW6Nb02KAjenUrWuEz1QrK1QG2xcwCh5M9Ujy7d5bP845pZgMKBEOFFE-TeyR5hhYaeKNNcnG7GnTOZL9V7EujhLcOD_kFYIKC5hGfktbODZBIvQx0PoWtOKf43JbDtL9asVOGgzY8hJsTHYJnPUED-4N_HbjQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcD9DD0izI8tVAOy8olGg3uOfxIbmCryDouwf95s9kbJsAKWgvGWf-UbyxRzVIF0DvqAgBSzeuD18y-SKh0s9E9YCdnIQw81-JhjoaO_cdslFB37IfeDvkJLhzkxJTGS6PYoteVuvDfVtUM7Bg34yJGDuRVEAOD0Vo01_c8YaYivyXL4mYCAuRdDsp6o5a6A4pQ4eg88VRhjZvv9FA8JeDlkwEVQJi0m-wUOyzJ9nCTkOVTIIlnCaXLeomDcVqDAoyBPw6SDVoEty8w9s254Ui5FU3HjiEGW3qFftKJcYcJMWA84vrqEfRsuZQE_A0o1C6sK3raTnmtBVY9IbZbmNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5mzOfLJm0BvzQomyhmIMWGFd-4gaPNZOVIf0RWqrvYIb2WhGnFH3Q1-n0pAt7Um4e5tzRObJLTH2ZnrGVlZSEITopA9e4EGFHy9kSeuc1JLLQK6T6ocv_yoCenhhuovbzwoFL4-zwKG_U-mqoQitKa9-0CyjmAAm4N52a3sUtDnzsO7I1IsVi23VZojqmydcnM6XgHHJWT8zw_iTT-YFZ3EZ-Z1zrsX7y_DVejZq5cJszzb9BUIdTEHVYgLarnu-entltoJkVcJn_QEMZTl_FO7QxliFTvcmnj0UYFItCpDVNwG4D_XJGGU2XJ8Q0p5rv228Zms_1jJd2JcsqNk_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vm1bjONaIi6ciZ0L6HsLjxViHYBxfblLuTfu03nkFV2IxGcUOX6u5xYM_lliA79lLejul7PbvFLABcj5yV9W6-cyWy4Gvxhka3e3tzHmtp04DH09WVx5ppNAHFLa8CT5M3cc2tbGLaxh2kxFTyFeUgXDrCM_WnnaFMqpQzBFQL2l8viwRTwNxrvch_ItZZ51NjVhLCfmsoldR4DaK3XPNCF1mAQDF8_ZQ5UlTTJOL4gtC6FCS_Y10VnDE9lT_yj6cEnMlbT2n0XT2VsOuWslRC1HsF_0fZFmzPOwqg8XhqyPY64z8sqJfJlZmrCN492Q8Atd3tzGMp2p-pT7Pzscrw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=SH4kvgkd_ZUSRGCK7QBcdzWfG6c4MW1TK0Ujr3SZ0moNN94-RJN7cCjlnYoOUYw1WC3iJtYy9a45XW31ttFtfw4y-OlJCz5MdhbhybPP13b_w8N_E5o-VM2ZGr9VeDYj_yl5zc2aZwHUYyk6u5pkUJ1NzBXk1K2Ze1rQ_aBdgrhVJXfte32d5SOCqM0nQUyrlDkqVb9yMoHpaGkVMUMrJcbxYUycdEZ_Gux6oXMyTnlvyN-KeTqXIt4S94gA9tKZKhDIaSyVlBUW126TUGtojiG7cfE1aOs53QgiPssqPjigHGBuc1YJJCaIvyqJmrJo1_QBonyL1layiaTVDBA6AqDdU7k9kKqhL3g06COO1MtEsWCqUp_p3-92n1FdS9hlzcS25E2OMu3UxGku5DkagN6p1RQpj1gJVt1GCvQ8ehBOw8T3iyKpoohfqNOIKULePNt2j9Cb9D-ihwmozLJq-RNGcA-T5ViVCDuaKY2h_X94lJJgjjOjeiJc3YA-yO7hfuefnMQ9XmILwNljZOEEr9tRfgaFn3Fo1TULIlaDiPhx9d37u9S68xPuTf1woIESN3PFPhQWEio98-zgizIA1ZCUmCuRhKmF2DKV1RPnUKcdaX8FESrQBTdfmGTDYhsgvn-XwCmDKUrfOJvNJdoKeBi8algYS45XJAf9cg_wXBo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=SH4kvgkd_ZUSRGCK7QBcdzWfG6c4MW1TK0Ujr3SZ0moNN94-RJN7cCjlnYoOUYw1WC3iJtYy9a45XW31ttFtfw4y-OlJCz5MdhbhybPP13b_w8N_E5o-VM2ZGr9VeDYj_yl5zc2aZwHUYyk6u5pkUJ1NzBXk1K2Ze1rQ_aBdgrhVJXfte32d5SOCqM0nQUyrlDkqVb9yMoHpaGkVMUMrJcbxYUycdEZ_Gux6oXMyTnlvyN-KeTqXIt4S94gA9tKZKhDIaSyVlBUW126TUGtojiG7cfE1aOs53QgiPssqPjigHGBuc1YJJCaIvyqJmrJo1_QBonyL1layiaTVDBA6AqDdU7k9kKqhL3g06COO1MtEsWCqUp_p3-92n1FdS9hlzcS25E2OMu3UxGku5DkagN6p1RQpj1gJVt1GCvQ8ehBOw8T3iyKpoohfqNOIKULePNt2j9Cb9D-ihwmozLJq-RNGcA-T5ViVCDuaKY2h_X94lJJgjjOjeiJc3YA-yO7hfuefnMQ9XmILwNljZOEEr9tRfgaFn3Fo1TULIlaDiPhx9d37u9S68xPuTf1woIESN3PFPhQWEio98-zgizIA1ZCUmCuRhKmF2DKV1RPnUKcdaX8FESrQBTdfmGTDYhsgvn-XwCmDKUrfOJvNJdoKeBi8algYS45XJAf9cg_wXBo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=Bf8a3KL5Ks9cgSQgNuRC5hqwQOJkpkEw2tDjgqM87q8BnU2LObPhV6eX5ys2DffRzxvyGylMRob3reWBb8PI3Cmly8BWIaizFb9katEExQsnPEp3SQWTJt2ogVxtsxkbBquAJQNwGNuCzsplUvq1Ea5Us-IxbO45eGVGUnAf6CLj9Dc-_DTertrohfxmOoTfVhGq4PddF2hnG1YqEJx9L58VzLg0-FXAvaieqeqBg0OAM0lpagEkzgFVuDZt4qQOlzDCAKwEpGB3DugtoBq6pOTL_iyJlE0uZIp3ggHpKFvh7BYsyVw8dCZLWDwL-BhFHCLtTQEFE45iRac7xqEOrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=Bf8a3KL5Ks9cgSQgNuRC5hqwQOJkpkEw2tDjgqM87q8BnU2LObPhV6eX5ys2DffRzxvyGylMRob3reWBb8PI3Cmly8BWIaizFb9katEExQsnPEp3SQWTJt2ogVxtsxkbBquAJQNwGNuCzsplUvq1Ea5Us-IxbO45eGVGUnAf6CLj9Dc-_DTertrohfxmOoTfVhGq4PddF2hnG1YqEJx9L58VzLg0-FXAvaieqeqBg0OAM0lpagEkzgFVuDZt4qQOlzDCAKwEpGB3DugtoBq6pOTL_iyJlE0uZIp3ggHpKFvh7BYsyVw8dCZLWDwL-BhFHCLtTQEFE45iRac7xqEOrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3f2CLUjBOgNERwzAKY8-FHkIZL381qVoUfOs7A4EN-p_RaLnd8zsHFHPHI2bLdmI1wcjIzD80pPO41lqCtifK5CHWul0wlrXU93d1hOzTx6nYAhqqYHUutIClU2Yae08AyZqG-52jdAD204mqShSzfRrWjeqHUMDsRL8wfbMRkLmGO53F6Psonwp2jqGeBLCDv1xhQumSV77_ys0ajfaLbs_JZ5FL1XEHQOxnVDaWm2r-idlr0yk637liwpV0zU6F04DZVQcHXzfSxnYG2GBHruSNIWSpYQI5_ro5ztlPat3ZSUBI2lgHowDlubqIalPbz57FzqysgC7MbS3VtnKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kb7n28vq3BfRVfVFBDjksA3pt6w7lWtLuWWqu_x3BWajVeRNlF0u6ijR0KbRvDjCyzmAkrvbpqIaxRaP11bzT6qta4hs-No7AbvKxau7gFDMR1rodJNlVkjVY7B3ulfOD8e0YUqTIfYUl5yhtjCyAJu4af9z-AFIky_bI-zThxI7xCITyxvyUKxFeXAwBtDzNDf4TQ7ECHdRZ8gTdkj8Ex-uPtA_PmHpT24b0HatdAupOwdGX8J_g5z_-6-xZhRMgG6YeEcgf0Au9SoEn4kxPU8bPd8XO0gPm3JhgswzeK3Qm-QgKfnA1lQbqtMSptthBfcXtt-vvWHb9yvuQESo6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=v718i9FEz2xwWsqi4kXSA4td-mBkF8ozACFlZr0GX5G7dQTXfI2X9QePJOJTIBa8TXVOCmqoXbclvv3IfPa2d6SjS4qCXGi_7zMy50ecz_5JOsTq8HQnTkjSipsAlGN0CvsYlNpV0EkCX3fBtqbgu5LaKA5e5UDxROZEz1pA-cLGLyMekYgM0wu88mv5uqDa9m0wzVGoSj8_4GBhACPEo4QlbWO61I3NNuhbkn7-C8kmAd5M9iHah_K5WGFzJm_KwI6HuVnVJGrPwuPcQ3EksGP-uk3gSpxQ1xwTMafu80ppJnhumxcOn2qusBy7VS32vz1kTsXPK-24Z58FTiMCZDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=v718i9FEz2xwWsqi4kXSA4td-mBkF8ozACFlZr0GX5G7dQTXfI2X9QePJOJTIBa8TXVOCmqoXbclvv3IfPa2d6SjS4qCXGi_7zMy50ecz_5JOsTq8HQnTkjSipsAlGN0CvsYlNpV0EkCX3fBtqbgu5LaKA5e5UDxROZEz1pA-cLGLyMekYgM0wu88mv5uqDa9m0wzVGoSj8_4GBhACPEo4QlbWO61I3NNuhbkn7-C8kmAd5M9iHah_K5WGFzJm_KwI6HuVnVJGrPwuPcQ3EksGP-uk3gSpxQ1xwTMafu80ppJnhumxcOn2qusBy7VS32vz1kTsXPK-24Z58FTiMCZDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaaB7GaTFptYc6Dzcma4TwlURorxj1wenNWWB-6Z3zHj1yvJR6dCa9dRwPP1_nlvdzFDhqF5R7bjIwXCqMLmyP08u_L63Fv3C9yZT2XBDIh8TKxD9-acqjukdNQNiH2a7jrkzHb5BGh7yXWok4WiSJ5UA1pz3XSiczPu3PK1RBLdNe9kSNUPZiR2F2x2S622rXbKSicIeUrc1JfRdW3cWfoAG1cafN3ujKmDCFNGzVFsLDvF7I2mUO9BF7TB3QqtR-O4ZPSzqbvgeDlcHpUjtMh8wbxdCVcXpw5C6USyyuRUk7vghZ0D1x9BqrVZgg7z8NLinolnQ4lwkU0PVXAl0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfuhGyXnvDLK8dNGOK-eU2u3ir58N8PashJVypEg31-fuw-x8yRDLRRckxbfNvduFxnsJFu1YpRfL4rOKUQL_6nWEVoSSLE6LOdW_zfW0Eo8j1FxIRjBqMOtApL2QJAPT-9Kqu83TSGHOgD5VxxtLFzbzynPH5zxCUXknOrB22trryqzq6xP7OtmHwBXuaDIlwUMVFavf2VPNKKM7A9x6u8KETFHv_maEyljybEqkLcgeUP7_0bBKUmnQrmsHfcr3clvkG0vOmBqTjq5jvLu18aFthFtnMCTw_HFzPqQURzIWZvgtFytJgUGDzp3N31koT6zFusK98LXU_yHIAChnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQHm-rnhq2gzZcQN3jEd-IHYPx00BUW8CV6lhwKcpdKLslkKlzMjYKlmKHs6LdoU2oIRWG0BHceJK-XitWNmbYBSLsz7cM-8fYFayI8HS7Q7eAhCDrOXcCABSj_0CSPEU5IyG2JikVz6psK36lWVJF7_No2O3Lef4yV6wZxVwaH1rWHsM28wPEj5gonHmzbA0NPZOv7BEd4O_DSottCAxGIDQVayWyf3DAemfFIIRt0uNBRyXITkpHI7RL97nrH3nOCpsmKwMf0tdAQsZtjadHeyltV8xu6arK4OUDuMAaKnqo3u_2MJm7SDtuHTffe5lC8UC1YDGYx17psx1nr8sw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMevrrk8bl0FlNxAnxzCe3TpP1x5V7MYWKXK6bCbXB01j_3w1EhLdSaSWz0X4AOGpJP_iGOiLXTEJazS8reRgLPsc1X1EbBvGHFoWK2Nbi-bLn6ALWBwO67bUW6vijWPinJb8s9XHMLau7pReP2tKnBnuSlzKEVvviZ3zvVxPeQqvbJ0dGjLKq_0FwOAvNkQDCJPa-HFgNC1aXg7ALo_HGUyowS9wrb-KVhuHfWbxAwxn-VgLxu2nw8NvoUV9fF4fIJ_pNMeh2CUR1WYGeIqkyO935nO3PLUwj7ftaiRY8CNCBQwdW8qVUzdq6TqOGKracVAMmifkzAXpb8cqQJ80A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqA26pwYMfN-fUxoX0q9uMHSvsJpt6RsBZ3ojQv-GCabI56XjJlf1fW_pwamat343baTICGqw1HU1MOoiUpW6GAGn-5SMHu8s-TYd4rLu0q084BdUE4ad5JReU0EWSKWmD2Cuqx1yEJdUQlrDfJ9y4h5PZ7P2anGf-5t2qytNaQ1WU2TDCzpe_oK_6clBKO1IMH5B0euEHIivTtd41nc0FiS8glEZj2gHaYDlcB1P1Xa3n7IT56407td7eoHOiNj8bW1ZYC9-LRjkf6dn_vRIj7nMCIrkSooYCJnPCa96CVVyCQ9Y8fnwptLILt0p9Q2sFeOK-L28CrY6PAPkYN8Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5R8eJoG_YFvNlH7Uflpsg7z0XecrL5zzAx7Dt0LbIiqHjhmLS5jqKaJvipEb4jAhAjmhImSRW6LUJ2plIFcsh0hwGUFbdQYn9FRcgaYi_obwwr-tgTHz8iu9nV8x3ZVbNbUNtIsSteILZKar6GiOFt4yGUu-y7s13z-DXylDwqkGF7qV7LYM9qpvSQm5AYzgSco7WE12XU8huBMpbRQL3EsiwP-U3g3gVL4Y2qw-kJ9Zo0QWyhpRMF3TwxV9siPTpKboRRfCHQR19UcB5JINEqAvmEM_e_wSRMQZNTrXqDCiNUpfcqggaCjTv5dy71cA9zIExrDAImrf7R-wF9xld6Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5R8eJoG_YFvNlH7Uflpsg7z0XecrL5zzAx7Dt0LbIiqHjhmLS5jqKaJvipEb4jAhAjmhImSRW6LUJ2plIFcsh0hwGUFbdQYn9FRcgaYi_obwwr-tgTHz8iu9nV8x3ZVbNbUNtIsSteILZKar6GiOFt4yGUu-y7s13z-DXylDwqkGF7qV7LYM9qpvSQm5AYzgSco7WE12XU8huBMpbRQL3EsiwP-U3g3gVL4Y2qw-kJ9Zo0QWyhpRMF3TwxV9siPTpKboRRfCHQR19UcB5JINEqAvmEM_e_wSRMQZNTrXqDCiNUpfcqggaCjTv5dy71cA9zIExrDAImrf7R-wF9xld6Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnEhnVA9Qs26W4PpMFYVynKBf-_BkHAw60WUIXyrMdwhlR88HHzDMhox6TTtBw8C1tSW4V2uXaS1b3ESQQNmlMcHrS-to290rpzYEsSDJ7agYqU_OLaRutAj05fwfAceLnNQJint8ikPL9MBO0cvjEZlc8rhxZR7iYrEMWJBpjQRmH4qQs9MA3B-Z49BSV21czLqXVggnnCgR7uHhgYVckk4l45eyO9ATDIKR2KwBWtmoYLCGoRdBub1Y5XuZiBHk8-D08P0VfpksLn0PAP0c9nruLHX9TRlmuu5pccHpzQ0CQaR1Nb7JC5YBRMnUPEt_R3Bi1P8auYUXskSyWEPBSO0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnEhnVA9Qs26W4PpMFYVynKBf-_BkHAw60WUIXyrMdwhlR88HHzDMhox6TTtBw8C1tSW4V2uXaS1b3ESQQNmlMcHrS-to290rpzYEsSDJ7agYqU_OLaRutAj05fwfAceLnNQJint8ikPL9MBO0cvjEZlc8rhxZR7iYrEMWJBpjQRmH4qQs9MA3B-Z49BSV21czLqXVggnnCgR7uHhgYVckk4l45eyO9ATDIKR2KwBWtmoYLCGoRdBub1Y5XuZiBHk8-D08P0VfpksLn0PAP0c9nruLHX9TRlmuu5pccHpzQ0CQaR1Nb7JC5YBRMnUPEt_R3Bi1P8auYUXskSyWEPBSO0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=Rfos-t6v08jiqwoQdrUu0XUEzpADsK6J69xWxW_xEqEnT_oMd34ZsUEvYfzjj_9CoFmeOnwlfR3zmfu-Sc8GPRhMFtvdo2GM_ZCq9gqbL15oPllUXLG1r_cb3xdjMk38-t6Fbj0Jk15PqpPfRYkoQCKBPs_VYuoOhCyP9pap8P7jskwrFU6EYAQMVfaygqwnAQTuX9Lccia8xqu_O6m0Wa9OxDzL4lBYsN05z8ByUHHf7Br6Utnid45qHqa1Iq-bBao5gsx7KJmeDfphOsnIeJWlBs6TOLtGQUO9GrocxaRBCRoolhLkXLbwx_l9u6_Dxz_uf6xe2oxt0uD-CMdU7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=Rfos-t6v08jiqwoQdrUu0XUEzpADsK6J69xWxW_xEqEnT_oMd34ZsUEvYfzjj_9CoFmeOnwlfR3zmfu-Sc8GPRhMFtvdo2GM_ZCq9gqbL15oPllUXLG1r_cb3xdjMk38-t6Fbj0Jk15PqpPfRYkoQCKBPs_VYuoOhCyP9pap8P7jskwrFU6EYAQMVfaygqwnAQTuX9Lccia8xqu_O6m0Wa9OxDzL4lBYsN05z8ByUHHf7Br6Utnid45qHqa1Iq-bBao5gsx7KJmeDfphOsnIeJWlBs6TOLtGQUO9GrocxaRBCRoolhLkXLbwx_l9u6_Dxz_uf6xe2oxt0uD-CMdU7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sv5PIenfCptGYeQRC64kk9Y71tG4IsA5haI6dAjp9s6pOfN5g9036ANPmkUumnp-2Ve-NoVN_oTrbSme9RjYmDVfR0g35kf9GyB_gMv5TGbPXBS6pG8g6GPrZijsJ2Jl6gzWtxXHdug5ZAIDBSQFoES1Rg59JH0xpRvTOGxa-RJ3Es5XH32rDHBbdjcCbZXbCZd5M5ZHTYHXEXhUxDTCTAMMjDQyXJfEVuDFPFLC2TN17J30kgcVeDoijHPBAz7xZvQbaWnUjFdFuXQ7kHRjKsbwZi8vpi35iv_ohvqHFXuAYgwU_soV1P1Jajmh54vxh214P_F1lxuKqXhL50Trbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKjxGNLKqP6p4oT7iyLgadPxn8aoP4ixOaRSZKr01gXR4Et02U9LrPKWG0Pt1PxbPPxww2yKzieVko2OdloDrrU720dUHnRoLY91NlQg-zQHs6fhPpTkPXMfpfkFOXLD9PL6TqmTGwAvpSVopliUaJQ7XGikzq8GmDkBsHeYaD8J1HymBfqNTRExSg2dGsLwnwZgryHId1BI8XNWZIyWI1FzI550jmVwo9s4UwYvITGfvIb6ZjY9hmr6eO8uY4XNYHxFYFxKirIFhT7v8qZnyc4Jk3LYYSTOisdwWrNwtTCmM_-JuCRSkwTiGDCjXp9eKdnzDF-pKbss8sqUWu7UCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=MvjI90ghx8x7BHtyTpY2n5JvrcvmOuCHzg-k4taiJ3qdaG7-CcfjoZCFqJ1enMS6jy_QJs0YZGfNdL5hBX6YUISrVaS1DoYQGJkX1iLAZ-hL_5NlB7gKM6EwUq5SF3akP-Vn2XKeI18BWUUt5imuwCjHA5JktgoAeRPTrYJ3mrcjFnqXjzXzBIEL6YwuHPzUxql0yAU_T7-_zozpR4ruyFSa0kB3pz8desegomcChJKENHWEQBlfS6vsOqabSiFELFAF4-ki9sVRFLCl_kuExi9EnUNuTZan5AyfGc9g1C1bxMNBA8itaZPQJlWWT0vrWKybGJh0WdtcXTmEwd53IYF56OucMz9BtqnQev-7wmjz_yJ6BZu5LoKyCRwrIQsU1GhxcF48S6zPtTUlIeHA-y1olRhkFC9DCHRfBuxLY03r4bBIrircKZSJYdaCTiiNdVwIuFqrKCGWpEESILgoOFYJabXKTokKOcSl8RNf7lv47dypVyGngdYCr5WvwGEotEsh4INL79ZRoNJQLhBSjDJJNcWIGwVlHn9Yq3H20Rv2Y04hxhC8b7ZwQqeCvK8-hRhJjTkGSAIoO8JOABFbwsyfA4bBdESFmS_WVdeXltKnUq_Hf84pvJa8iQaNnZI41_LHf6fp2OZVUvVz381TRwvj_Kt4zYXUJpZDFn1gvG4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=MvjI90ghx8x7BHtyTpY2n5JvrcvmOuCHzg-k4taiJ3qdaG7-CcfjoZCFqJ1enMS6jy_QJs0YZGfNdL5hBX6YUISrVaS1DoYQGJkX1iLAZ-hL_5NlB7gKM6EwUq5SF3akP-Vn2XKeI18BWUUt5imuwCjHA5JktgoAeRPTrYJ3mrcjFnqXjzXzBIEL6YwuHPzUxql0yAU_T7-_zozpR4ruyFSa0kB3pz8desegomcChJKENHWEQBlfS6vsOqabSiFELFAF4-ki9sVRFLCl_kuExi9EnUNuTZan5AyfGc9g1C1bxMNBA8itaZPQJlWWT0vrWKybGJh0WdtcXTmEwd53IYF56OucMz9BtqnQev-7wmjz_yJ6BZu5LoKyCRwrIQsU1GhxcF48S6zPtTUlIeHA-y1olRhkFC9DCHRfBuxLY03r4bBIrircKZSJYdaCTiiNdVwIuFqrKCGWpEESILgoOFYJabXKTokKOcSl8RNf7lv47dypVyGngdYCr5WvwGEotEsh4INL79ZRoNJQLhBSjDJJNcWIGwVlHn9Yq3H20Rv2Y04hxhC8b7ZwQqeCvK8-hRhJjTkGSAIoO8JOABFbwsyfA4bBdESFmS_WVdeXltKnUq_Hf84pvJa8iQaNnZI41_LHf6fp2OZVUvVz381TRwvj_Kt4zYXUJpZDFn1gvG4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=RzOVcXCM-vs3fcM--JGWnLGHL6LSzymdYUEBGZrMynb5RSF2_v-XcLhv2z3W_qFuA3tSfbTYsQ17LG4Yc3GChrSZP_A04Epa_mFGSAzc8jQjclViYcpuTSEpsYYIVA7hYW0LTtJa2UAMbOP55pK8kyTODj4eEp5rvVZAGC4-uwcMVdnRHVGWDBtsKis0wNKs78f48cr-xkWpzCNKQgml-tZG-BO1M50nk_fQOlMk0Op9h5v1DcvVldgy4PnRa5TS9H3pK3Rhqizb1_PJCfsFn1V27V9yQbQ43B8HY63flMByg3uKDDJ81Poc0UA1aSpdEZmoRDe2SoaFVuWH7JuiPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=RzOVcXCM-vs3fcM--JGWnLGHL6LSzymdYUEBGZrMynb5RSF2_v-XcLhv2z3W_qFuA3tSfbTYsQ17LG4Yc3GChrSZP_A04Epa_mFGSAzc8jQjclViYcpuTSEpsYYIVA7hYW0LTtJa2UAMbOP55pK8kyTODj4eEp5rvVZAGC4-uwcMVdnRHVGWDBtsKis0wNKs78f48cr-xkWpzCNKQgml-tZG-BO1M50nk_fQOlMk0Op9h5v1DcvVldgy4PnRa5TS9H3pK3Rhqizb1_PJCfsFn1V27V9yQbQ43B8HY63flMByg3uKDDJ81Poc0UA1aSpdEZmoRDe2SoaFVuWH7JuiPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMOXU9_12hL8jwnhNnav3w3KLdf2euCXvYloGEkOgWh7vDRklM3yBDs7aKZhZu855iCFfsbnGz1wo_a3c5WlxhB7H3E1A389bI1L4YfGnFKNisV-kDM-aH3yy1hK8103CUhO2Np9yGJ2pqe14a2CfwLdSsNcnH01cv2zNpJmtq3P-kpswAUBvkxZ8F0LloBmZW5davv0wACm6ONtp1f4PAroTiCYtUl4_7mxU-eZCQulro-RtfzJeueQWxi6twnjYljC1gB0rUFkxpKaryakvkYjoGHq4HcetsjpuD3URic3_vKUrFWY8oIRu1fAddcsvXz1beHrIyzJARmg-oOK7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ROOxAr6QQWm4abDAx3muAx1SlSjQcSIrmM7PA1t2XhZsbO5AHICDdFA7AvKrMgQF4Ydxc10356laa4J9ShkQBobVNZryea28JXuesRr-wflHnq23eiDO80El9bv6PTbiSxX-XfvSGIBjt9ujt2Bd-LHKFdjHFJc5sAwSnvFCu_fNwYEZGQtB_WbChw_P0s052EtFSM9mXffdClH-D7eyRT8sJIEFacRXnPT4xfxLh1ICihyRHQcztjTG0rDGiqZCAemvKR-0UuBlBQM8-94bWhGpBekJgAFtn1ARQkaCXp94FYGD1acMcuz71YClsNknehcUY9OHtU8ON76q6a0CBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sKAU4XsqYI54p3w1vaRXiGFOCjVXDhGiXYRWqFlyOKH9Wt01Y7mOtIjgSlQZuIR32o-uOP0SoF8jgfNSmab8-fPyS10AwAS3fAG5C-TC4L9pn3Mn_YBiBP1UpJ4st_E49PSiCfE48sG2VO1LPpUXF77qa0ggq7Scq-v8alBeYpAdjhR5QdRykkzHG-y2QcLOyiZx5qK1g0VYvGrLv1V8rcv0witzxxxuDT71Ie7HpHlCy3awduFLLMlEU_D7XLi0CKeHwN--vosUWAMFb-IPB2qyIRMWCM2_7u7NPF4rjAzeFF31EMiNwxFk4tHcgxRtkGqrsKUW0YGAEk5eIznW9w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=EQoMxYZJVLrrh_cMbKASoBIMgZW5wd7qY3jPHKEJ5Hd-RNLGLNEoYDJpEZxtIc74WYr-6VbTxeP1zN5OR7n4V0Liov76UcU5FB5kctGm33xCCKRcCN-EDj4DbFTrGJRatt5Hr7mMTGcxV_LtuINHU2F1Ez7eoEO1QjlinqAyEAK6QevcdoSIWhLEtfazqGMLzZZAT2sukGZtXe9ZxHt_t2Rg8jqRPNSZYfz4k8_XFXJP-Koban3j7Il3UH0x5vr5IrPPdHFUAvfr4t0h2ZqCr-fwnepPQ0tzmih4q9_FuSQg7osOiXHanFUogfM1wMnzhY0guEHcD4uG5x1lQNQ9yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=EQoMxYZJVLrrh_cMbKASoBIMgZW5wd7qY3jPHKEJ5Hd-RNLGLNEoYDJpEZxtIc74WYr-6VbTxeP1zN5OR7n4V0Liov76UcU5FB5kctGm33xCCKRcCN-EDj4DbFTrGJRatt5Hr7mMTGcxV_LtuINHU2F1Ez7eoEO1QjlinqAyEAK6QevcdoSIWhLEtfazqGMLzZZAT2sukGZtXe9ZxHt_t2Rg8jqRPNSZYfz4k8_XFXJP-Koban3j7Il3UH0x5vr5IrPPdHFUAvfr4t0h2ZqCr-fwnepPQ0tzmih4q9_FuSQg7osOiXHanFUogfM1wMnzhY0guEHcD4uG5x1lQNQ9yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=JwZskMwOQ1utnGv8qej1LoRR3GYkC2dMYf7OFUFriV2vGjgzJgKpMj6cg8xZZCFKEu6iG93Ze2kKFQu75zMhA3jg5vm20OMIri_MQsWATj6-eAPvsjRPv02siNXlpbbMy6eceO5rOjBHrwh3RMXvfewASN4RjmHYf3M5Zb7FVWA0ZaQYRWBk6oRAqAOAHdppzZAqW5VlsafxMMr2yMKQW0QdJz9NcRqf8jvuHKkDDuICkA3BOx7hvX9vt2Sj8RmKfY1sUhD3tfojXD-_-wUKPbsRiu-KmkvBfuSmVxZpgshMUakq-5BOysTYVpvVn6Pn_KPnFOfFSH2LA-bsmUHWq4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=JwZskMwOQ1utnGv8qej1LoRR3GYkC2dMYf7OFUFriV2vGjgzJgKpMj6cg8xZZCFKEu6iG93Ze2kKFQu75zMhA3jg5vm20OMIri_MQsWATj6-eAPvsjRPv02siNXlpbbMy6eceO5rOjBHrwh3RMXvfewASN4RjmHYf3M5Zb7FVWA0ZaQYRWBk6oRAqAOAHdppzZAqW5VlsafxMMr2yMKQW0QdJz9NcRqf8jvuHKkDDuICkA3BOx7hvX9vt2Sj8RmKfY1sUhD3tfojXD-_-wUKPbsRiu-KmkvBfuSmVxZpgshMUakq-5BOysTYVpvVn6Pn_KPnFOfFSH2LA-bsmUHWq4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3V3bEQl2Q2Xk-nz3K7aDokwztXaARnfR0ZIeMsfsNp19CU9ZfaSFaCCe6KpDqRUUpCJ49_rdxw7zI-GAEvN53dSeHDq0q3jtnHaOCSbFpRe6DVFeVcGM3wRddeviiXMDIAWYRHV9GLjrtZr6hdM_AIYy7FKcMcEW0-Mm7RmO54z7DC463rCl8qiP_o1bQbakx_6XKAaN3op4dqeNo-Xase3asIrddR0VVTYdLcpIkJ8--XmjAEfNhKoTq4PwTFFCD90okCPuNaw3RzUrnpT_VA8Ltq3PErx1Z3DGXNez6bJ_IKbr9k0q-bsnoXrzXNlVJH_PLk-tA1xwDBdFRf1DA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYPx57doqEihvVU6qdLrXs23x-EgOfW_agCBjTnFByyI8nFXrBpdXdWeBouwT-DjfJOC8Wdhk7ogNM8NL8pLjKi4BjOnW2pWfY6T8fVI6E0M8yowjpYE_-STf5CM7B9X5J09ndH0JPENR9SI0ZBr4VddrOAx4C0tX-393R1IymYIAkeNKKkYbP_Mr1LvIQvFC_vxDW5PXqSquSqubtlCA9ohAu7xJglohDeTiTudAQyqzSE52ndd340KXYBbjo69hbJ_iJUEcevQL8ppqPO5sDrKFWj_2xNXzQYst_-kdLtTZFZFw9iFtEUEdw3_kWZlcVwPhc-qjZvh5UqmJFlNTQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=sLoYu32-Ien4w1sskKOLJ8Txj-7r04ZCbBoauDa4pG4LSUEaw8FDzTkPSVGKKUyHSO3DWM2Cj3dQ025moiWccPHW6XOVbXijZ7DEe99C1WU15Ngp_fZPfXn92AVe-qPtbcrbvatbdJ194JoBhujT2Pn-Yb1zjvA6p1ktqi9EuSATngg0bp5Zkj1nsXnJI-pBIhlfyy3H12za0N9mDjVCLtwsLoLVQGymda3aOnLT7TdmQAGzTyhIIL4b7Qjm4PgywnNCz6u6nIdkP8W1QsoXEEFaj_d_jkAKvQH7-Mtmp1u_CV21yDLL5O5COlTA2eQ1MqGKu1GefslpD2HdcKhEew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=sLoYu32-Ien4w1sskKOLJ8Txj-7r04ZCbBoauDa4pG4LSUEaw8FDzTkPSVGKKUyHSO3DWM2Cj3dQ025moiWccPHW6XOVbXijZ7DEe99C1WU15Ngp_fZPfXn92AVe-qPtbcrbvatbdJ194JoBhujT2Pn-Yb1zjvA6p1ktqi9EuSATngg0bp5Zkj1nsXnJI-pBIhlfyy3H12za0N9mDjVCLtwsLoLVQGymda3aOnLT7TdmQAGzTyhIIL4b7Qjm4PgywnNCz6u6nIdkP8W1QsoXEEFaj_d_jkAKvQH7-Mtmp1u_CV21yDLL5O5COlTA2eQ1MqGKu1GefslpD2HdcKhEew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t41BcXGjkDFg_bBTflw39DYEl9yyoNbza1YxmuvxexdZNQjua-9rMYsJyCewaGe75BP8HIFgYf9p59QRTVWeh1Bk21I1V1-MhYLmqYuUzGEqJV0fkbWFCh8ismAVbI8kLZ6TIF1lhOdLiFYr-ys4WtsBDrBWOyhaX8mEZOgrfU5Jxc7uz9IERuHwPWuERyQMRHt8SCvGYmm5VX5G83q9HmY33ghQJmUUuf97qeVd4nB9oL5TZbf9jxpwW6d2npH99wC4R4l0aifEzpCt8bRbOJb2dRsScCRRgmcPTfBKuJ3VSzIycu10qSZszB0a3oSlaTfBgjJtPft7_5UAsbFPvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFOoSGdQHf7WytVGKJYDK8FDZJu1x92QN2ZTW_JZ7y370es5XGY7ASrDsUYZF4n49zYBTEr1nBKyi9aoEjUDHb8iGBj2y9RQki2trSqjoBRaUIIrBjoYafhXrweDn2zgCke1_MDeF5JnyiqBj8Lzql9fgY83vM-NqQpUbMN8AofLT69skHn5UKDgLwsUSPQv12Ygey5v3yVlm_zE6yIcFq8OlGDXwvZ6DHZ5AYzyDPXkDKtP-lE4d2ua4WhlbW_3C5NZJ3tretzzkRQFqPdXPXW5j28ER0Hfz77-eQMd0J-EWm-a9PaUcQA3p-ic4LqaWqE7wQXNVsiQhK8_KxZBog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsTTbrcTVarVOiCXBRNpScy3_xhDe4fLiVj-bNT9llLNpSj0aySEJhQcoscFjY9_FVjUd_0ygIlDVPIgXaDJoUdRsLBD4xX9-b_cpihUM7Zyyz2CjLplb4vW6CDGGD2aWAfPimcsn3dT8xHy1GBSpqLNbVJ3pZCd-A2m6ngeXdQF_mQqZLtgTTjeWNZL_sDUsVbV7UDTuC9hSHZpsThsLddwgqrpf2UOk1sLG-hvgcHAAkw7uuZCdWACSVzEYSJaLcXshT13qDYOQArjzxpvOnD0zBtQJ7RWwbsdJ9yktQhP7uvJV4xQJBpli0au15HRQyfeeTdabjBrt12WOYYbeg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLY5AxhBPYWac6NtGLw3LHlWt_NR8mQKRyrYrjEoTiZ7CXvIXvUveeHXH4JVY86AMlD89ajjsfZUkKsyOa8obFmE0_8wk4I7Md5jH9WZ58qtX2X0DJCsyeomxG_yBy0TBDJ0WWizOxyjP6gm5HHSULBQIeqZVkY37WdJtzcLTfb7pyGjtQNqzBmvbcuN3nC_oJKDCAYgLH0tDN8dx1gsPjq5nAQ5ZtuBzE4bwCoC3xWGX1E65rFkvZ5g7YOKEN43Ns_NqjVFEgFcvToluSTsQnpTXFxz7FtW3is6iITmORENDyZITivdd4td5wTnkEl0X9B8KNpUVDpcvfAKgWUtgV9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLY5AxhBPYWac6NtGLw3LHlWt_NR8mQKRyrYrjEoTiZ7CXvIXvUveeHXH4JVY86AMlD89ajjsfZUkKsyOa8obFmE0_8wk4I7Md5jH9WZ58qtX2X0DJCsyeomxG_yBy0TBDJ0WWizOxyjP6gm5HHSULBQIeqZVkY37WdJtzcLTfb7pyGjtQNqzBmvbcuN3nC_oJKDCAYgLH0tDN8dx1gsPjq5nAQ5ZtuBzE4bwCoC3xWGX1E65rFkvZ5g7YOKEN43Ns_NqjVFEgFcvToluSTsQnpTXFxz7FtW3is6iITmORENDyZITivdd4td5wTnkEl0X9B8KNpUVDpcvfAKgWUtgV9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s-lHENhtElsQyBMw--TxvYzlMR8atL8ogDwM9QbBVrntZdKwht4JrNH-b2g5poDgXYA_PjrzwTRGKwY70QDIhKxtgUrV58VEkaObLPvwhP2hpOliNQY31WtHBL19LvAtfovSBvAtYqt9q0SR8ZNt69dzYEokbkk6oW_cooeU0ERiSL__XdvAvSHdfOylvhY3y0MoyXsghfNHbJQvEO9PbHZmiSb0Qr4UYEo6nF77mkkS4sJycmT3npq3lkbQH9jhIXxyTo-tjCddGc9--RsLs50vEc7Bm8sNHJ4YjqQpGHqPrVg56YqMMF692c5Vv12fphXtryWXDbxnkGXpco0RMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H1MxWh32Yu6WsQPzy94ewt7HabH3_FoNuxiHIDiwKsTo0EXIPSuJChPzXV0-tU-AW--IIcEOyX4I1wrZXvLojF-ESfza7m4JBlcTutNpIUN2DH6w-qNW1pZrLWnp_b1dJO3ZXq4apdWJkh62WE5EQLmcz87mFwwIMa-hH3Y64OJZxGZfauKR8Keb2VDBIbZH2_IyU8SX02SJ4WcHn-Ir-PjeLb4P9Per0-5c6prJTSZxrBuNZb1uWD6za9MlNy2kqnEv3jow2XxWcKqW41GXRA2aCKfOBZ4co7rRoAGG44uGSWZGUFv0OE0iUYCXfbRhV_QdYjlOvZc3UfPszhGGkA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=tvsrW9qZX2qeeVMiErQba9x0MnW1_KpVMfoDSenHHEmKmXNCviqHSCqIN_U72nvBCVFIP4myGoWGDiyS32uZeITorR__8P4EJPNgu0MjlSqPlcoaVODsLW4Qgur1x3-INlg0uBC4jlkO-LHVNCHu8_6jyYuJBKrg3KVAyROJHjDvX9FamC2L3WaeJ54MD--N0tz5cXyJ2KyYdeq-h2cHLaTQxmewvNVPq1Nvbd_iIAWCi6nFh-Z4DGY8XUuihMf-Hzk7WtCO8UFvnuZzCh0QgwN5TWxXh1Q42VLnM5oD3QPzgk1EgPwu6zx4Mp7Zyz3yHaRZOnbeQXh-mAw9I4q5OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=tvsrW9qZX2qeeVMiErQba9x0MnW1_KpVMfoDSenHHEmKmXNCviqHSCqIN_U72nvBCVFIP4myGoWGDiyS32uZeITorR__8P4EJPNgu0MjlSqPlcoaVODsLW4Qgur1x3-INlg0uBC4jlkO-LHVNCHu8_6jyYuJBKrg3KVAyROJHjDvX9FamC2L3WaeJ54MD--N0tz5cXyJ2KyYdeq-h2cHLaTQxmewvNVPq1Nvbd_iIAWCi6nFh-Z4DGY8XUuihMf-Hzk7WtCO8UFvnuZzCh0QgwN5TWxXh1Q42VLnM5oD3QPzgk1EgPwu6zx4Mp7Zyz3yHaRZOnbeQXh-mAw9I4q5OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=VC6a7JSrcOEH4FjVAYWId1CbwGlSF4QMdlaOeVWi8MYvD6HDXSiea9LB3fnWfl5Vf0fgxpusqDhJlk1U6LO-odqkRottiCiSyJ7lpnBHqTlcS5h7owRCfFbL_DVPRncvW6O22UKvVnKQMiVunfPW_eSdnAdJBQhP2CCoZpVaRyoyFcLED_uAUtxep1aduoT533fIOQmzWUjklj4k0Q57IoCyST6UqT0UscHlLPgZVneWDpCeDfFrV0B0WGz77Pr1psJbEXBwyFh-f1Mqwap3FMcrMRufD1Fr5VA6p4QtpwUjR5Amm8M8ulBoClA4NAdfiP3FAXLl72NStR9OuG9W8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=VC6a7JSrcOEH4FjVAYWId1CbwGlSF4QMdlaOeVWi8MYvD6HDXSiea9LB3fnWfl5Vf0fgxpusqDhJlk1U6LO-odqkRottiCiSyJ7lpnBHqTlcS5h7owRCfFbL_DVPRncvW6O22UKvVnKQMiVunfPW_eSdnAdJBQhP2CCoZpVaRyoyFcLED_uAUtxep1aduoT533fIOQmzWUjklj4k0Q57IoCyST6UqT0UscHlLPgZVneWDpCeDfFrV0B0WGz77Pr1psJbEXBwyFh-f1Mqwap3FMcrMRufD1Fr5VA6p4QtpwUjR5Amm8M8ulBoClA4NAdfiP3FAXLl72NStR9OuG9W8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4hhCJGAxh8FeMhLcveHMG1c3kHuiG5iiOgSF2JL2_oSFPLA2YgFgywpQflXbDH0MQYBGLwVU30gv3FDR55MfoNhbUcce2CmV9jh_0IaDJmQqkZRGwm_pNVBmtYSypxWagU-c9a6AQ6cZ8UhQ4lu-EWYie5T-084Gt3P_49jphdNOn_7K2j3xH3EY5RannPmc4OgmOhB1cci4HfEBAHIIuuE0JJcd3GsgnWEoHqJXswDJ8CrYOk7sYId82gy5i2s7F-BnW9fZneoKmAFG4xOy8fr0w6gV0G2ykt_uIf5s5RzhiSFkzTqpx8a66D8Ixf5u73r99lo41_KQDZxkF0sHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtarF8EZZTkDCZjf2fy_YzubPYaNYZvdR62UF3UPcrhCHGYu8doX9RtN2zdeWa8IfPx4iHqd1ZnmVIjJoWkDXqolLUb6fZmg2Y21lwZYxeB1--eBrzwsWhqwAFfTHFMjayedHM2VUHHo71XwRuPYIKnWX_-8bfpIIJi707J0XXoUUD0cikP7KFtCzCvEOH5ei6GXq4abs6qdMNKu-ZvJhR69ZXeGheyexLVueMEXH_OXW3_OmHWzFzfPiW0RdDtrxsfh-QMHppttAWaUey6IBlPFLder5k3jMIr2Js6l5BKU8izpWz33mFrkU02CFJhCTkk1YFiYzVWdeTjj_Sxjqg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=gkglTlURMaHmsTtKkq59Qd2j7Y0r0MbT5B2eZ5AaKfotR7eEDqbjaas90Hcd65-40sdxikn5oGtXcdRyw23FVA1J8zW_eOeRsiMH7ebATSa4j8V7RHdHk_9RcVa8o486qlw-bMLPmjbyu-2cjVvHtSz1hRTx-mt4q8FjG_62NsHk0hnl_bayHNdxoagRl_tiHcNYlmeGE4chxWXpE3fNp4z58iG719g43NO21tcgKWLssUvf32al-ogTwnqv1DKwB38Zp0xV53bqTNs64hun3y5Zp2J07ZDiqBi48AuDMC7H83yz9tJ9x9mVLqJkXEEAzTitN39A7gL4p4hL5uGx7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=gkglTlURMaHmsTtKkq59Qd2j7Y0r0MbT5B2eZ5AaKfotR7eEDqbjaas90Hcd65-40sdxikn5oGtXcdRyw23FVA1J8zW_eOeRsiMH7ebATSa4j8V7RHdHk_9RcVa8o486qlw-bMLPmjbyu-2cjVvHtSz1hRTx-mt4q8FjG_62NsHk0hnl_bayHNdxoagRl_tiHcNYlmeGE4chxWXpE3fNp4z58iG719g43NO21tcgKWLssUvf32al-ogTwnqv1DKwB38Zp0xV53bqTNs64hun3y5Zp2J07ZDiqBi48AuDMC7H83yz9tJ9x9mVLqJkXEEAzTitN39A7gL4p4hL5uGx7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=Dkfe5B0aoWFgtIfPGYoaLbxQysIw2Je0CiffdjfA2iKgtC0nIb9we3bqMFiZCSjQ3BZ7pQR_SWjOdx82Edzk2LqEnunXLCMHM0qHaXVkMcdumbSAUz36tRVrV0Uf9m_2bof7JX3fYhSe3p4b3We_2_Af23iZc_A5RhafChlNo4P6UqCxpPq4hM_iT-uAx8OWaFjKg72CYpb5g458Zy0K2h_zoPZwd4VeCR98GW3t9CgIh7xTLdrtA2gp_SEPFEdsfuScK9NAaFbUBYp3qGAagnQDeOi4yUUp7_eOeMeO4K9w440iVIrdwjdEESqKAKKue1NJR2Mi0P83njHdQGGAUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=Dkfe5B0aoWFgtIfPGYoaLbxQysIw2Je0CiffdjfA2iKgtC0nIb9we3bqMFiZCSjQ3BZ7pQR_SWjOdx82Edzk2LqEnunXLCMHM0qHaXVkMcdumbSAUz36tRVrV0Uf9m_2bof7JX3fYhSe3p4b3We_2_Af23iZc_A5RhafChlNo4P6UqCxpPq4hM_iT-uAx8OWaFjKg72CYpb5g458Zy0K2h_zoPZwd4VeCR98GW3t9CgIh7xTLdrtA2gp_SEPFEdsfuScK9NAaFbUBYp3qGAagnQDeOi4yUUp7_eOeMeO4K9w440iVIrdwjdEESqKAKKue1NJR2Mi0P83njHdQGGAUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rvp51qaEskdan7I7oJPYsJZklaEuX0r53WDnucT_KGO2u_dbtup41XH9cjqqNv2G16067NXSrSZ90lzd1IlcE01Oajo8RE-zpXQqFy8BSCG7HDaixfhl9XNMwmvL1jsMmopie8v3Fdu_mqPlNpq_FXmqzNtpbT3TJgJn9G-sP1YUVJwroZH-KcxwcdWvpqyM54-CjJqGP9PPXH5FQP1_2sbpEEds8rBx08FF3svjgyVefCF8SSHa9YTb5hyCh0gcTwaX_GJcxdiQb174jo1ty_k6QEKzvvADxNEUlE6HVxk4aGcgNSR53LYlisb09nbiov17bmUrsJ-Bn-v80XcP9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKFBL9zHZJgmcI3lXvRPCCHcyHczKeMnBXSql2RJvqOTZfZWUXP-XniRLUdlmNBU4vlKiCvl602UZsHwAqKzCVRj7TeseDFwFD43ss4-TyzrLmkYsnfSk7GEnmMZhxYg7V8_cdCTdgYT8rAscOu7aUQm6uzmPauLJ4RTDuJs1B1s3wScD71wvBc5P-e8kyW3dr7hYRfxNxbX-D_xe8rOz2iYToPNoDoYfXkcZDF1MD3i2LtOeR193eWK4SCEgvkpFegtvCZPKl0dqKp9cgnILYORFMbOHRYFGhqiOxX61SaBfG_o3jk1uF_iScs9l2muO5f6hHEfX0iUYfbLfek5Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTkzUdXQObrz1K6wJwtu9gZbMmeao8h51Skc7YUE_o78Try136HLSn6AP15oK3OlIucyTTluwAwiS18Dauu3W3MNK10Sp2GmTfD-Qm7S-OtvVEUom24HEQZjhm5ZTM8IOJ3HevKSmg7ipX4DOcgqujLiyZHVqx9d_TooyCCknvAecwuUOUZi_-0dZbZInuwQMImL-LqGAgLCvS5zVeIcCBf4I4Ntk3i2JEFF8nYf4hlj-Sdp2vsZJdv0ihfjScUGBLx3UoXxWVuE_HsKXVfKyqLuJZqcMgPhZc_oXgpV1V3kQmNd3XBjNnEmDKGOlNP3D1V0s6uiEwsWKDk97trwOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cg_iWCc_k8V4LZR6ikbXofv2sESAMjknEFqKzGILuTKH5QvO5LEqffbijZVRMm5tNQjX4x7PWggkxwj-Tqqej_kzpTRk3Hx8A4f4bC2MOzxlPyQ6V88yHI1YUXpIVV6ZhqwDMh8kO99yjVhPcHwj4md6nuIYdWyga9sOFKJs7hlhBoZHSAkIx8P-kPLatMtQdMTKm0SuIipnfC5EuS7hyn2yfVe6d5L-CAZv_7jLEHAw9l9JLklXwbFhqfNfkCMdq8sLLpckKtFFT2TW6GoxF_-ACOE_cd52a49py-kN2hBn_UGzQjt5zisTyL6fBFkFr0fbdrasONI57r6RJ2qy0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IV08UXGpBK1zdAxLnnK3G48-EKSkwRmTogKvJHnyl7RSUgu_Cyh4331q0EgjIjO1sM4g_KXBeryikoavgwBDjqSAVAbm9FiXObkXUkkzzZsN8xO-k7zyWCjM4SBnO8K_5hiqB2W7_qfW-S1pDIFPu7o8odh5oaarLP9LLpTBEySibEt54VcW7zbA8rSkjvoveMMqEvAzLL7PjNJuxA6IRwn4vWWy0q7brPXHt9QbMgUU9-S5A97t6i9sENiUh1zFSrmGQ2i5Cl-Wo6KtqWrLpQMsx6wkfAQja4HkrK5h-9iqephTGJnjtuOxU3kQwNTX95fO_A0RhrgpI3moy642rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TfEJbk7P3ueOB0gcYmq06E-rCjM3-ZsoZDnryqMdnRcC2W5HJ96oXHNLcHxtL9eMU_6PBRf8Ua4iMQ3AhuVYR4P1NZ72KYce0aIuPdPLJ9xtEiBkUPiv-HKqeAKL52SxpGVrGDVtHzA8cIoYi0ioJVSpLLl7o4vrtgCWGpUnWUmVewmDohDW_STNEY9sxyou_AYOKRS65Ql43Q2unCfL2ZLNzzs8T1Q8PmO8wpH_ijX-H2mOOzh97aGVRO-IqydpZmfEYKliYMUViifsjlI4PW3KqmLEPxoJZXkXyLNb7TMyTAxJ4Pk9F15OAv_9BqTBaGw8qaSDoDj9gocXvmFjNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/otlHT8Oyfm68KZXQx2ikNnHrW8i66sDfQ7m6gEQJyUA6A0wDlCzPotXzHe_9J_5XQEFN60Ujy9KACRqaUxSpqZ2FQITtF053eOv8TZ93TDYmo91eLrXqclBkJkKq2dtsboFguN9KrOXsTeX3phEmUN8XHe13WOZ51yrqWF95ecrIbJS1-FYOYfCvT6wM60sSURFuYrsww7USe5qiwRjZxJVNh8exxWDG0TSxHKk5RDqVX84uSr2pd4dRs_jAx9U5PvBhF6rHTQWnmTQvxHKdS0fdnD2ZGhw8oOtm1HmakuTpJXKlljE5S82cqdXsSmbie-AaeXBymEbpEYR2DHNRaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AtNRmJ9Gm7KH_6KXzw7goN_ULzzJDs88qnCdXxH5GteV-7_fgCUuC6xl4UetjKieRC0ZHtYweH7TjdDQERsCYdWxrkA5dJ2f8rcsPLFBgEGnGOvrEJ7meMl8XoTft3abMZ7VKKHGo4iBSCCQpJPp6nBH8fKbpW0Mh-7WhyrZtE59dvrKXLl97xYxrMM_P5EudleVYu8iig-6J7dyzLhzSbVE6DrulwqN4XzuJllZCLEztld6gd44HTfZc-1u5zD8J9zPZ1nxD7dooM1Qlv9iSI2aYXsAjAY_i4Tg8A-y0dswwal_rL4mKMdihR8IYgkR0MXk3kl8AhQchmN-nFRcDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swookYcZ1rlZVF-RaHZvXlicG5CB1zqD1B89gh0SDd13-57D53SMGLs_idGiL98j33-Uw9mub4zmNHdyKXdxd6ds7cql13cMMOW-k03hrSycfFLBIaTdqFnrtubGu_liMJmw25OiYcrBGsP5QicHR02muem3mJ2aV4kav08l344_viBvPHz3D4-zaj58ggpTuzPdrhi9IKcgHUmLy38unZ-EbrBdr8gUfjs2hVZW03PA_NzFLRBOVlvHR_YnsSyUmIJEHEs0zsBBqcR5rPDrrmOS1TzxrkssQLLAOC8jmiPwLx3GmprHFPZqWMxTLMUfTIxBRozlQEKhZ3wXRqDjSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKA0cV1718suTxUwtBmfMfnpw1MT29rZutn3rZEj5fkKxheU0s36ka4tE1DDj8cheQAAQLy-OErrRZgYrixZz25KcTUzHRlghaVW9LXHTt5NrUf46KkJ0lpP9rQeWtDEnBJokIi31abQh0_Gt3V1NDhjRKK9jXHiyi2AJSO5jeKpPF6OfFW7lbJfrMFIUOSrBIjcIXp-kyq5VSUhz7UC1w9IVObIOGvlOY_CQGGCrEXtHEgPeXvGjaOT7ijU7MoWyxgwQi05TRbbbNWPWNKT6FwV_yZ6mbJ89z7bY919SMFxL_oxAjhs7DE2Mn7BLE9anEfCVfeAnuLI5U9HfHB4Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=LDAAmv4cRdF89AqPrsCuZ2d5zKIY_uR88g7OmB733Fe4-1Afsq0e1j-fQKaOfiCnLXFdsfI1hdzX1PlTN1xBuyQlSSgClel8zeGarOhSmsS48upHBZKU7FQ0hxpxv75mUAE-k903vlpBGnr8m3vTSp8xhI1GEl4zzS3cphmagciyxl1VMVoaYb6WmmsmymobqbLQGMhSBeXdZmMDWsY0YpNXl3H8BEhOqEZsqtow9Q7Win8kxp365cdoumNsvqtkqL-Yt4dQUIbVEy_E_iPxkSaKnYQvosmpBxT6sgb_MNqPh9iVCXbB-UUikaIJT7DiOGUyGb8XYwLyL95z7W0hHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=LDAAmv4cRdF89AqPrsCuZ2d5zKIY_uR88g7OmB733Fe4-1Afsq0e1j-fQKaOfiCnLXFdsfI1hdzX1PlTN1xBuyQlSSgClel8zeGarOhSmsS48upHBZKU7FQ0hxpxv75mUAE-k903vlpBGnr8m3vTSp8xhI1GEl4zzS3cphmagciyxl1VMVoaYb6WmmsmymobqbLQGMhSBeXdZmMDWsY0YpNXl3H8BEhOqEZsqtow9Q7Win8kxp365cdoumNsvqtkqL-Yt4dQUIbVEy_E_iPxkSaKnYQvosmpBxT6sgb_MNqPh9iVCXbB-UUikaIJT7DiOGUyGb8XYwLyL95z7W0hHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=leScCTB6SM3o0EocJsdmGQmGhamqHjDdNfelCsdNuJWcP0lvQiDmWY2Y0wgq5iAocJgbQmjRai9VwF6m7eGbu0JtnXL-uXX9ycdFiMF_gPSEb5DzPRAW0KLfRGPFOJX1V0i1CcNGLik7PqLoKF39Zu0tbU2ky6PccMu2x08XVSZ4sab3yqhcpRj5t30w-y2_J8xlZeUoyNPNzwR5HiRDOhyusoh0NKjtL7aPGwg04uvV8zibDT8GU-RbQZyd66S7lotSoco6iSEaiaGNGJDp6ovA6kKxi7uzAmMb8dA7ADV2BtThCTRX6vMQHM3PTA7lzFq0edo503_sxr50tqn7dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=leScCTB6SM3o0EocJsdmGQmGhamqHjDdNfelCsdNuJWcP0lvQiDmWY2Y0wgq5iAocJgbQmjRai9VwF6m7eGbu0JtnXL-uXX9ycdFiMF_gPSEb5DzPRAW0KLfRGPFOJX1V0i1CcNGLik7PqLoKF39Zu0tbU2ky6PccMu2x08XVSZ4sab3yqhcpRj5t30w-y2_J8xlZeUoyNPNzwR5HiRDOhyusoh0NKjtL7aPGwg04uvV8zibDT8GU-RbQZyd66S7lotSoco6iSEaiaGNGJDp6ovA6kKxi7uzAmMb8dA7ADV2BtThCTRX6vMQHM3PTA7lzFq0edo503_sxr50tqn7dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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

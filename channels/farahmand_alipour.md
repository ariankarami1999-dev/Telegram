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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 01:06:27</div>
<hr>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=RNifQ7TE77IBn5jPtQfW32O-dFl47vBo90hGnGhMzJXFUYkqeQ1et8R97BS9tuIN6VKc-bMpkyttvPX53PzXmUOOWeNec0jH3UV95TIrF6e0Z_rruJv6txkao2jgmY-pZqykk6jJBmFjl9ZmFXQqKEwiYYpWRQC1FHdiBFu-oJOLbr3Gj94JINOqUqeP41BEHqiFYGXQXgFT-Dk1QI7RBknWVPwHZGdX-hBfZAfkFUVh0sTPqcfTmp1xppKKs-JVTqXxCZHNcxrus6hPIkjKIVUILpwY104NGPxGHKPrTY1ytkRLj82hG_Haw_JQ_275uJ7ALfJZBwHD_M-jOUckBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=RNifQ7TE77IBn5jPtQfW32O-dFl47vBo90hGnGhMzJXFUYkqeQ1et8R97BS9tuIN6VKc-bMpkyttvPX53PzXmUOOWeNec0jH3UV95TIrF6e0Z_rruJv6txkao2jgmY-pZqykk6jJBmFjl9ZmFXQqKEwiYYpWRQC1FHdiBFu-oJOLbr3Gj94JINOqUqeP41BEHqiFYGXQXgFT-Dk1QI7RBknWVPwHZGdX-hBfZAfkFUVh0sTPqcfTmp1xppKKs-JVTqXxCZHNcxrus6hPIkjKIVUILpwY104NGPxGHKPrTY1ytkRLj82hG_Haw_JQ_275uJ7ALfJZBwHD_M-jOUckBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای :
پزشکیان ۲۸ بار استعفا داده
و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/6492" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6491">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=GBXZ0RlZcZGQ3odp8MYklRjAYMYnleEUphkbswMpE9rPe5j4a1pZXpLtHtVjWAOZJjaMLY1Z2YGyUctG6mPscprYUxlVXYAUIqBZWRPpOFa5uc1G9gJZSOQk2PR1fVuNchfkvIsKR70wBqAvN1BOCyXRQ0NHf9pxamNQL6FiSduoIieAW9Rg-AVgBBSEKTFRhhFd7M09YpxxiB27uUvjBwJtqND7e94bKLHuMpdMTkMaaxOHqdlIvSN22HkXphHwegySRxIP42vLeuVhcUzdvPOVOoRcA5jhriXGP7v9dKO_yly44BH2U0bVo6J9eQ5QCvFTVIC3TqU9_O_siBKlOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=GBXZ0RlZcZGQ3odp8MYklRjAYMYnleEUphkbswMpE9rPe5j4a1pZXpLtHtVjWAOZJjaMLY1Z2YGyUctG6mPscprYUxlVXYAUIqBZWRPpOFa5uc1G9gJZSOQk2PR1fVuNchfkvIsKR70wBqAvN1BOCyXRQ0NHf9pxamNQL6FiSduoIieAW9Rg-AVgBBSEKTFRhhFd7M09YpxxiB27uUvjBwJtqND7e94bKLHuMpdMTkMaaxOHqdlIvSN22HkXphHwegySRxIP42vLeuVhcUzdvPOVOoRcA5jhriXGP7v9dKO_yly44BH2U0bVo6J9eQ5QCvFTVIC3TqU9_O_siBKlOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم نیروهای نظامی مراکشی، از مراکشی‌هایی که از خاک اسپانیا (سئوتا) بیرون انداخته شدن :)</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHAFBFcnvXuewN6H6Mr-97u3vLAllyfEvjUOEngOptXF5VjVKD77NsS_E_iJrlkMXWZ556Xek-drGE_lpy04X2e7GNm02uMBa_7gEOvaNEICvH8rNFRbbKHHy-uGxfM-zaoE7PRob_v2vIgrJoWMO0H68rVbtdriag0Kdzs092EgMtSY4V2BlB8B74OmjhzSSclgeb3xiWhWdFZ2LGFRgSdyemtnKU-n4XgxEEeyuZCi4ers_RYpaHxp5Krsxs1TKMv8gabADvUDZjnitiv8wbkMLYZfx3sS6udYvyeZmheljitgGWmBTPbWvCdTk_8vuUicl7xRFQRIBSqmO6ojOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtGw8K29MtYV8qwafr_11h5bRz6yBfjpYPnJo9K-PgOF99nRNds4_kh7tDCBMimQ2VIAYyZJ6MeKqpjKoElkijYzuL1fz8V2CYyt5ai611SjXFP5-vxBeoYPNdhEiyXYWdECQ_TqCp7nnQWACcIkH55rpVy14xSsbVca3Y5jetrnO5UIAHljd_hm5KaWctJmYDCooAtvBQvSeWzE5rw1xtg2dYy5iHDZ7clmneIfABvJop1DFKY-vzdiJ3FVTtoLD81I_pe8ZJ5MkZlLA85k1wMJkFCGHnifJCXyNvt-FxaTWAIBvRovrTyL_w1QDmogThlhwlpnDyeDz8_OrnSKsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tj2twco5ejiuMHZ84JP0wcvFlzHd7OaXlxdfIpaMcczC4D1C-5J_hIgplXGFT01_etp54A7AIOM4fCeRPnaVfBSPqEwBPBJ1e2rvOZLK-VXGwSPZj_6NlvZ1RAJK3umTBccGpce9VWvbP3JPhnYnSbGfeB2T_0jmKeJkxOtQVJHEfZQ-yocsV6iKHjiYnNZ8Piu4b5l8uE4oOuBDb3rYD5HzbHrbPcGDySvu8u3HEToMVOUU7PQ2WhmnIEP2lHiDji2C3jMI31N76zt4yMb7CcYvezV0OEDT7yIQGnEUJA_wURgcOdK7pt9syCcCaQQDJH0_7hHif6NcIXh8S9PUVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gikmSGLqJGCWopa-vcotBpNI08bGSoUBEUQ7JQi2Lap48K3EZyWJ4y2iF2wq75F0Pvuq2stEVFrE2pz1LGmuJbdGjkA7dTmbSmDjYfo8e3XuruGJfhlP9osPBY7u-H06augoQciQDY7Gw3Oyh98Xbf8eHhKkZZ-HzKS7TCxX3eRyFRMW5ofAU1sV862scrND3n3RxpjPo_wFT7pszW5kBJzv7PlawCTp1rRt_bhnkOLEAbVRvNvRkrACabV1swzmMEj12-HkrvZ2QqSP03Kha5fJ2R8jR0PHf3i4fcukgbC4Tpp_N7h7Tt6sA8J8cSVA1RNn4hVU9fvBrwtWRhrrqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBsRqkdqM72B8JE-ckFufxObNJaBFXBVYr6QoRBdWHWtMbKAaBKe91gju1-ecvjyNhOhCoqvRp0YhnJxfJo2sBRFIEgnfMnpBi_Pa44v8U8bs3kDIF4KzBZK6f4T7JS9cl43nH9oIwdVf2fDSaTnil1EkdpJ-aeqo7sTzJNr7TfUamvCxaKNna2ULO-Gka6-j0ZyLkDjQIVZW1xNYTNysidFK-DAJ3D6TCDI52WwKBlIgd6ozFvZgvowPb0aZfn5Ex6jdDXf-yEF5OeWiYv8JHH1o3Co4A41TtOUnpbQsn2mSAgCEVu4bl-ZKvNMrnMZxHPPaUlKc9yPyiMuIfnRaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSckZ-TBIiTdoOxEDmXs5ytxzTVe6-XRoW4mCU50uoAiaUo2gcifF-ZFbYHi56cmwbaLZ-13ijgG2rxk9fWyKri--0N0sMCSDgnLVARR7D7SCtNz7JGf8i3_YZ8kdtS3datfRwgrQKff2AEgO2wzMKWuERqR5JGpxk3yQXQQpO04ymIvA8UZ0fR50b1NJ2-cUTHwfHT99nT2lATViVs0xjroOYcI8DDPycgGZ3DsGOXhRoSJLjGIVQpcCDgWkmFY8jIsfd0Rws37eJsV8qnsqZkxGl5m3E_Ekc6VjqHA3i_1OK44q4xlb7synyfzgB_2Kp_dgZ6VNgpB_bkKAlQE6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQ1k5UbzFqqvs0wJl01nz9jJJF2d1O8Qzw13R5o31_OAzoewIa7VEvd8833-vddTL8gBNkKFtQy1Zct7FZ-WgO5RWdXuXsT04iomza0KlfXmZUkHADAWaNanMeZlcSm4OVzihmNi8wS4IRMLT5mTEiLXgYo6mt0rfaoUJlx_-jDoCGmEXUc6Nod-7ceZtP5qRb6iB3jdijhkkZQDecQB6YEtNxLPg0ZGDmfeCL6UWPuwL67ApKIjVKWYWQ9EhVOz4e6SkQY-6mSB7TB6yRXgvMoNAMXR2FXvTNQ-KJPTFMZwUtl0qhGZz9eQsxee0Eqys1ncHXDLFWZv4PWwZG6rGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-uYIYkUxeuWcMkQ5Sk4QuOMxV6E0Mtyifht6gYLv4p0Lx0yAOKqeP2tMtK7r7I-znH_ph4PE-TR4cKtid54Q6hmIv5eGTcmAq9etpUhUeqaq7WPKO3Wtog-_t6GnFW2dln_d0JmiyGKlstkrO2MaOqrUyDcu5pQeZBlRIx_EJ0_ahzFfW55NxOUSK2D-lrDIkxxl4eTtmwXO6Qjcfb_J0m2xFW8VXCvYTvTl1NC0QqOzESHyhtXFoE8a9GpClHH0avfxcaJyTljeME8iI3DyhxTTEq5r69tDXT1i2AacTyckCnf6o1XOaf641W5vSAOmNNE7_3s4o6Sxqb-g0lI8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQegXSkgHUzyOVrtA0fNECy1Chq-PphCRQzuGM-rwjVgubTBuKwruLlNOWXqx7WUpl3gKezgRdHNLUi6Tji6Yi7RBHZYhR7ROJ22COXcZ1q0wiyyl2G3YpAWE2F46gsRfXxoUQGknD1slmCIXHno__Skjc_qkA9cZ3vhWWCdiSQI5u9r9LjNOQ1UhPJqhFEtmwI2jNpF0tSHznMPEAIkxR0bz1nrO3cKrMSxtvh8VtUAkRx9GT16UBNeOLnoyVtKjjWqWKtq8eygoSDCwVLvL32qCtJt1HMC13KnXu54JPPXIzjumA6pLev7mcqL7wHT1RKBQh6vQe5DPr05dxnBBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0MWkowWQmmdyAMvkgGh1G5mVkxL23MFrlfWmxa-mAjG5h1MTm0Ex_YBAxpHAt1MzgLwLboeQaDNpQofypn1txFukyzvpHRiwb0FYtHz7kwHcrrDaFDPRPqluHN3Sq6Zk5ASwVbkcJgNSLVzhADvGjKC1XScYUNlaaXxcisj7euuiooq-nVPvcM7OxIWsdnPp8GeTmxtjCA1i56GFxlZBgAmD8Ti-kAu9WZv54MzLppT4fAYEn4fj7YrrjbCPXyn-al6z6x4mj0Jh8plSmyCYTyMLKLHCgKxOItC-KgMLYjCpmki_wEK4IuMop8HOYNvtN_ZQyW73Yia6-rqu8xU_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.
‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،
‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا بتونن بچه‌ دار بشن. این رو خود آل احمد نوشته،
‏او اما آنچنان ضد غرب بود، که میگفت باید از اسلام، از منبر، از مسجد، سلاح و سنگری ساخت برای مبارزه با غرب! تمام هم و غم او‌مبارزه با غرب بود. می‌گفت روحانیون تنها رهبران طبیعی مردم هستند.
‏اساسا دنبال این نبود که اسلام تقویت بشه تا مردم برن به بهشت! میگفت تقویت بشه تا با غرب مبارزه کنیم!
‏علی شریعتی و علی خامنه‌ای، از چهره‌های شاخص تحت تاثیر اندیشه‌های او بودند.
https://x.com/farahmandalipur/status/2083853984113054084?s=46</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b21yOC7U1ZrtHxdvG74FKnhw4Gma9Uwo_1czO3uuqx_lMKWFl75WI_un87Qp7QW0PgrHkPjQ3AqW9-jdETdUntk9pt0h-_eP-aur04vnASBnP-v4uKe7OhGfKd_NifryRio2iexFZP_z4_qi_YDh6yBLRxf71iTEp9cuI8pOf99G-9swQExaGoaWi8eUR7Q5WG7OzxrotLyFjH0Nu8IdhruUCP0WpAbp9eJQWWabTKEgwXEVUh64RoV4dH0WlIdfgKXpRD6G7xs4exwH8UPS71_Zy2YdhAwpNB4xCblX13arKJvYeuf8_RyBRqzNRP_wQkagP9SaL4agXMr8yCK88w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYed9fUA93dhYdfNmttVcm-2lUMw13RTbLImI-z9mIYAp3Fn2k2kwxWO1ig3HF9kt__Qd30l4m1S2SDDhtjk5O0OQsidkXQ07ucDS_PfMsyPqIF9ZhT1o8M2Cxsd_EbJQdDbi9aBA4SfwyLGuP6nOffLvRWw7t8OIr385KWwqDP63fknUcx9lGhmSwZ20KPLmq_5e37EHVefD9YRhdJu6ixoSXKTToGezCK0UiQndY6nkAU_-eRTxFwse4feS584QcekMbB0tAYzlBdDkGKmgpvLIimfjExjasGpdPQADAzfOTbty7ziR-RNmt2mTKBDmtYnfK69_5xd6506jVO7-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K13-EWVk300XrJ1Fkt-iGX5-rnfHdE5dP4IGPa1Z-kiTzlysN7YV214S91LGQ61UIw7oSfy_cGFHq1jg4qsxvzCCJVrWcnJtpjBrDiMxrhKULT-_NcEyVybLvqpra15vHesFDgkfDnpjjBziAcQ03FVy-0eQtcv9WiP1HL8QAiqGJ9CkPdCRkRG5uiyYtJdCWWHiP9Zi-He51y4XmiI_R0XePJ_t6O3Z_h6mGKtzOK_bnFMdpCpjERYz0XcX3ywl7ZuY-cbARFf6ZHg6zgSP4-HfsNMwzeOwSqp-aI3YZNP7RBmhZJuD0e0WDz47DeR2jr-C0rN_F5zx5kZLolamTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzZXqyT-27IT8birnRUQO9iWEShsp4D5CAnqHG73eZJccuPWYJ4QlN7iQZsLd40PnG_6T6LwOFyF_mBZo8IqJL7tu0NvCz_Oim-9oNVELnvwId-CyaYL8-eGfcsluFhe5B_bxKFQbaavHgTVC4bRCPx-1ZbectrZc4NMsi6Peyx00GpS9Y5hmSGjJa0h9G63xP8n-tWzuOQckiXmUm7ipJEU_VTvxaBOulufY-dJM5xLZAhsdcCA2MevKrten2sfnzAGtcckwyUwKMHEsFoqmf-BXQ-uGdOx3-F4UUczyILHPhndXQHhaKEIV6JmI3O4_9bHS4jiVHlGj5N2l1cL1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZPHTIoomfOqVt-REz-VFrw2K2L5O0ojbJ2pARpNE3kWJpzFSazq_gnO4R-vhQwuQTZn9oNlLVgqKU6NnrUHh--ggwJYhyIe-gSKxxieD3MFWG5EWb6OJZaHAFRzf6knyZ4lT2rIIc5CyFpjKWxvIeILBgqgcGQWMQLuug0I4SeQCByHwzPBcAmimkCypgJJyQWd0mcHZ2QwRlusk4OkhGANdpwg7CMewrs2M16KxregChaVNpCw3-ZKOyM2-4kFvy1OnoRZftySF-uPUvqz8nFaQv0_WlL5I5FkwmNDfbLPJ96onpC5De0MhvrxArH7Hkhd2QURUB9ugLt4Y4gAMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGqLX56XQCCEIWTU17jn-ET9cZtqPTriNU_wg5kZMbppX7e3HUO-gpk7shcT1-eB_Qho89eYMAu3-OcT_sZuoipKuz7U1m6PDm3BU8vQMBQZY9JV2h4O-vuoX9_8EnvuNXs4BkPQCgjMXFzr005_x7f2MzTicuZKh4ZBImglneUjmXCWt9vMLaggn4-w-J93KDA5UgrkV4ypmF4GthrsJf7IEkANbySD0a2B1wcwVefDgGZBJpEMyLUMgGhkrLFx_RR-Kz1zjBWVbC1UqN-aJrhBTFEDw0rEidorqB65qmmzfCjh4FLysCQKQw3-SnXJO6PtXnCk7hJ3c1HF2iooQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPkSS6JCdx2csVd9VidYGMalktPoR7M70epREVgtd3WnNXiBBmuQqOCCfl8nRSws817iHXrcyuLhQmxe3-Z6IxQEWkC10iRyQ8AaDFPshy8TfQM8o3g_1T4mv7pp4JQE8tQUVV0MpHrTVJVukxPpDXKzlkk5ouID0ZwIGxUkQCYwgWhljF8PzltbzTnd22pkoSB47U0IsljBitlOUhV6Vdx36SbmbaQJM0vN8YfYGJaK2U_4kjVdrpli4s-aXEvAzAcEdchwGgAphXb7Dx-8ViEH3O3wtBb1XyiIbsJoysW0pN47o3-PklDNcHpWsNzFrLjcvUFgnJjPQjfF4YxpWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwbTAOxs6iZVZrYScUx8tRBYdW-RRs4FtTGq6AJN8683SCxTms9q7b3BjrOw50sQumYTvD3FMpk160mATyxYE4pWhARcd4OHydi_38UW-URQP36AlwdZVM82eMniPAlFv8ZFeAmZXHhxkFtPp9LGyOsf_TyA2Aw1_IqlDq7qXtSa14KAVDEizSwEc85SN8dQG5ioFTgDtOTiofZ2e6qsJfb47w_B_GlulyFdKe3Ez8qQyDyhrN6FBhSZQA5cG5_DRP9Q-TqPf-uEQlbK0gcLr6SGCEBMv4ca-9JgGpBadu22pgNk20xZ_dS7CFNYpmxAdHJK2X-ksAkJU5oObUljRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdECpq8MKI2u-7o21TVbXRUOoJ61ikQLSw_6q-TwxPBjFIOG4S5QUWvx6_VNRTzBTSovpZLC-U9yC4lUc55JZwenEE2aTUwSM5wUCO2x72scMZILe6zYY-QYdgKWKf5XsAD29Sw_ijz_PnZk5Xo9Iz-zI3YiDgbFN_ewhbZMsV9H1kYik4is3cUMnU48ZmEHzPKEMHY_p6oOca-A7et2PhGCTwLffUeeei_pY4eAd3UA-3IUegIw96K-H5EDzKgtZN5KmBbOsnsR2R-TTLagDJ6LwWWVv8l7fKCqbNWltLAhCshMwWf3qzKpGCei7wXHVR1ISQJct4JiCfMfSt8XHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=ISI9t5-GVs-PcX46qZHXAHGtZ5Qst722yx0HdBKCPlUubkzxmgnAMYVPeNg7HWCVEns183XpUz5KzoeipUKFfN5dgEzmm5fLPH3gnuOrx5jqKdTFtxbpmZ7YYD_AdPQ7K03XIRi7POg6gqZC8Ak7RfMzx6yzFLk7nyAoxcJRuJ2bwoM0YQ0kipWyGfcOLrjQ35u3nk2cJ7WxCEoeSjPJ1HG5GbNvNAaASrO4B66e_m07hvBsVC0T3bD_fOksP95HT_YvbbKFrtO3_UovP5NaNfBAMSSPRL2bSS2UpsOrUuiHx2TdE_Txld-mBrZ6dK9NihrOkgd7qiKgS5lTgSBhEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=ISI9t5-GVs-PcX46qZHXAHGtZ5Qst722yx0HdBKCPlUubkzxmgnAMYVPeNg7HWCVEns183XpUz5KzoeipUKFfN5dgEzmm5fLPH3gnuOrx5jqKdTFtxbpmZ7YYD_AdPQ7K03XIRi7POg6gqZC8Ak7RfMzx6yzFLk7nyAoxcJRuJ2bwoM0YQ0kipWyGfcOLrjQ35u3nk2cJ7WxCEoeSjPJ1HG5GbNvNAaASrO4B66e_m07hvBsVC0T3bD_fOksP95HT_YvbbKFrtO3_UovP5NaNfBAMSSPRL2bSS2UpsOrUuiHx2TdE_Txld-mBrZ6dK9NihrOkgd7qiKgS5lTgSBhEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bacJLG0lqicjTKG6a8u5oFW-sZ2EuZhdIwNnCgn4RY13GF6VguWsVaEseDgl8s1YqJQIJe_O-JS7wi14d6zBy0Mxf5RsdVZYQ1EwMH6divLQq7_B2vVnOAqTunf-0grcF1M_VoUUMLdmy5dVyQznPSddTwfqq7i5M-bYGJoDRw3hIeWbexgEpPQ6ZQhebi9LhcNQ3yQXKKsh8SuKFXE1sAlFFY1QYuM6WcQCGT5c69irnRmfN_zrSuYfhMt_sMH0ah9xWCrNOZQdQjtpogfhI4XTSJmjTA6xPh3TLalFj-5vypH1jc5sv2gCdGhTeEdUuX_4dy_QAAGoiYjN3_13KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_V3cVKVBN9huHUdSjo544kvWukwszalZRWs9_E-OR69mXHip4ZRqs8Nkq7XSkDwAKWhRyrsSKQrY1S7Vz1rrsGrrtUC6sW8PJvdQJrX_i3ol0uwNQrDg76K7jAcQn4IPo2mrkQdor6a6IP5VckPJGKefvnnJDWKxikQ8XqgXL65r2uVpI_iUg-GWyFWP2LiYeKJqx1pwwmSByUamHpdz3AG5uwZ7C_m8gdpgEtkMJFn60NGDK14ezDcRCFhEo8Yl594XZXV8GO-HqGesCUC0i0oU_sUAnlR7hiLo8lmRHOEtdTNkZhPjK4m8DTpWI97EqhtKokS6S0Om8iYKO8j-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGXk-Va93WCojEXYLuq-sITPdez76ruAGhwskFCXunLI9aGWyh74icecK4sG8gkvzC_fekdY8wPIPpZgpB-dcHXosAYvlo5sllIBPPy2f5fFE6oSrO1kLAGFOXmi1GuW-_hxPhFsO1wf72-aroWaw7kjVAa-leBWDaYzr80Nt7IknahHS0326whF-cBYtXYiJpqT1W5KbI6x3XsLuSq6KlIwpxibziaI-tZJ0mI8-n5SPA-GJpCPg84wMr8vUW8OVS85FioKKJdVVyjfPZW_aRVddLb7jRfmNUfT-aBLTnrHobJeGhV_ReWs6_adR_Hi6eQxVM-L828ORpHa-TtNAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uh2ygYLazkld4jq6wb6-atIKXTOKvkCC_aW7pb0Cv38Xwwe_7tK7ivoOjgcNZVhU6DwgV6xibkjmqzPu0VTrDLkaNboH0dqPUhH35aXyf29yTExP3X45G4EkT6JWteOww88eqPAT68oNWxOMn0pZ-4RkIzLcGm2Gkf6baQks2dCSji7dXhS8U3NeSeFpDDQMq21ZizC5qBcTW12_sCX2-pJP9zi9eDUJb4nWkW6GZvXoLpO8_OPbtAzMzzn2x3QD6LFsBd8GlLMwt8bBIS4ok6L1RK-kgLpEqjkqzqdNc-rDUzv8R2no8jnNqzYakDFhgnBp0MofJ4ZuLhsXIdcyKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjTgqI2z4bcyFlXOTeIjtGLTbETecXCwHeABjm6q2c3zM1Qlb5NUQEo6ENwPaEz0QCkAf29YP44-xj5T3rAG_ZXffL2VSrA6vWOSL_-2CrJEklFFTffXGf1ZE3FSFuM1NeAlX1E7dfu-JTpPB0fKAEqV1F17WgKDfcfkDpekFeoukFg-m-XMvqen0X5dzTgMdZQ5D1M8sEPkfdGKVl4Dd4yKF2KIyQkUNygDdkyE9dS0uPKmc03I84fhhh9YOm1qXASeZEkc3L7WOVg5pABZTljReHezN5X18A6AGfOKlRuEN_6pk0cA76Hi0539-b_IVm1R3Z_b3auE-8H_HIcXWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJQO7fNQSh6rh2MGL5qmMkR3Cpqz5b5fiJyaqgPEKls657z6-MDUuXGZSyBG3IoUvhx2yuuNJAM4uhCVidXcT7lrrK6hYXH8nF46SyK02hgG2exr74RcN7EEN-lklO6sz60dUyumPs8NL_kwjvxLgikQuKczBfllu5AxpIgSPGLe23G-1kunbPdPMK2oFPGvUY5vONRpgyM9Tmqu_p2p_-82hnoqfkSbd0euWSoJ2tOMDBlUCX6-m_pGe0O0osfeGPbVisGKujqgAssJxBNKSy9tkgq3u2g4f86kVSK-UI_opjm9GEBupK0f9aq1zeoe2i821iLNwmeoAmeBz-BPYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgFgSPPuZENdNxKZvjVQwmjBHb5v95msSDkoyoAf9gtbxCqpe-8yXz1HXEqv_WizaAjEQte1RZtT0lhPym24KomnhNeYq_fIlRCjo9PHzKfYPtSJrOYmSjgv3rVSZI-gZELkKxKaBoPw_7sEXZVm7msLUlg0fqwBxuPHAIcDMCXLs9ikphjj1kpMlDnUqRZLy9Ipni4rt8egHBqRb721i6ziaO--RgcUk-xf6aBmfWJvP3ktLx-lgXCv4bA88Vm7zMQNEY1h55PVetk4w7oZzwT8ncoZf-gVqOk9aWVvRW_OhUNEuGntowyyvW7ojarUgQ8o1MIgbxiVLrr6phtpHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=Lhysiv71q_qPG_2eLKkvV2y_loik7M036M9x3hfXVqk9mXNs6YBye3ZQ-tSeiV_BadQSOY4Rmxg2pRMWiRxNSWGqq6web-yTIFvp50NDBZlGz7bXemGOxUCsiGhoahKtSpKBNvU9nZMV72xXbDH7iwi3ExKl-q1yZjkk9mog0boZChRmX32u3BYNgILIMY5lrKeo02Nrx0zBJIL6pdyzz5d_M7UKPD8GFiPEJ_p1LKYJ6y12EYxKje_tdtbLN4cxiU6ujQwGNJ3GXrY5ncxWSpnUqRgpB6hc9kEPKShK6pZ60OK-8aIqHe_lepcj-aK5ccPiRc5sxuwHldj5VhYmjIlEXKCi_tc-mH8RH684LsAf0T-c4SovI4Oi3kWDYxIRpQnW-FcXVgKHPFOGyXY40ECTMGL4sHwVwIPxLa4aweaSnfuEZT86Dv4hpIXfdhQzIpya3w05m9SDdC36NqS8dTLhJhKH_AVCYOvycWcZeuSmz0k_H60kVcGWosxuVZms5RIbbTuvpJh5sN6Bg7Ixx3QN1iWrfwdCesqfxGzxFvx1ZXxEUAoUfDqU5zqC2CMTXl1AGZw4D5U2IiFB4RwbBbLkV8Bf5erGmA85NhAKU2l3xnoAy8TtvJQfcCS6WSXUKXmmY5MZ-rsKTKJRos1qiAkcUh36CyDdI8J2ai-5Uj8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=Lhysiv71q_qPG_2eLKkvV2y_loik7M036M9x3hfXVqk9mXNs6YBye3ZQ-tSeiV_BadQSOY4Rmxg2pRMWiRxNSWGqq6web-yTIFvp50NDBZlGz7bXemGOxUCsiGhoahKtSpKBNvU9nZMV72xXbDH7iwi3ExKl-q1yZjkk9mog0boZChRmX32u3BYNgILIMY5lrKeo02Nrx0zBJIL6pdyzz5d_M7UKPD8GFiPEJ_p1LKYJ6y12EYxKje_tdtbLN4cxiU6ujQwGNJ3GXrY5ncxWSpnUqRgpB6hc9kEPKShK6pZ60OK-8aIqHe_lepcj-aK5ccPiRc5sxuwHldj5VhYmjIlEXKCi_tc-mH8RH684LsAf0T-c4SovI4Oi3kWDYxIRpQnW-FcXVgKHPFOGyXY40ECTMGL4sHwVwIPxLa4aweaSnfuEZT86Dv4hpIXfdhQzIpya3w05m9SDdC36NqS8dTLhJhKH_AVCYOvycWcZeuSmz0k_H60kVcGWosxuVZms5RIbbTuvpJh5sN6Bg7Ixx3QN1iWrfwdCesqfxGzxFvx1ZXxEUAoUfDqU5zqC2CMTXl1AGZw4D5U2IiFB4RwbBbLkV8Bf5erGmA85NhAKU2l3xnoAy8TtvJQfcCS6WSXUKXmmY5MZ-rsKTKJRos1qiAkcUh36CyDdI8J2ai-5Uj8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=mgZyXRmmgYx_YqZQTTrHE3yFv34hARHp2CrGGs0SXA-wGGkJkWg6gyVoogbiZK_fdFF5vqnjgGsc9_w2Ptc2PcYtdKbqOSNMuhPYuSxHZcckdoGkmmNOmmE0LChG_oNF4QFES4W_X8wvsOw3aHNb3lXGhHYyifYIrxiGhiMUk3GYZY6MAd5nRuv6LcjobrWsys7nAfyq822gA_8HF1MvnlOLMdg8Fi7c81-faDn3994roDiZ3aH2YhfwEix9QGuOKaE7w5bXfrxDwJcmbT9wa_7pV6EwRbRj4D8ORS60ReqNY3sbEtwhJWY8vMi3JbvmqJjDieS6h4sVFDvbf4eDdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=mgZyXRmmgYx_YqZQTTrHE3yFv34hARHp2CrGGs0SXA-wGGkJkWg6gyVoogbiZK_fdFF5vqnjgGsc9_w2Ptc2PcYtdKbqOSNMuhPYuSxHZcckdoGkmmNOmmE0LChG_oNF4QFES4W_X8wvsOw3aHNb3lXGhHYyifYIrxiGhiMUk3GYZY6MAd5nRuv6LcjobrWsys7nAfyq822gA_8HF1MvnlOLMdg8Fi7c81-faDn3994roDiZ3aH2YhfwEix9QGuOKaE7w5bXfrxDwJcmbT9wa_7pV6EwRbRj4D8ORS60ReqNY3sbEtwhJWY8vMi3JbvmqJjDieS6h4sVFDvbf4eDdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCCNKpDiPosxiMMpZC3oHHjgxmyzoh5Kiy5tffplSf0YFnTKO5408g1Hfz3r0UoCHpGVNbR64w7QUBDRCDwCwSf1nZS6eH5ZLkQIEbH6K7SmIC3jvGtx8SCbr6yyPJbEu6valXnWfuv7s1Ik89LtviHth18MLn5VdUHKULGe2SiRoLWLExrPrRZCLAXA4wZeIiIglZVzCMHlWXdxFlM_3_W9UtORMSRiy_I8CkPKiQu4ndPOunLl2ZgX8EgfdMdaXzgsQGYuGA9jDKarr3S2083EJ85bWnSKFcH8zm8-30hHPiln8PBHYicgvYjiLU0zdLUWAiC3Lqvvrs-lVAqL9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DyOq4aMse0TJhSYNXqjk4lWgrPVygWfTL3p4r1Ev8vhBy4kFW4IyX1y2_0qBpb22IQoS69Qv5o4EecCkvI5gN9vxJ4cWFJOC4kbnCLO_zlMDwsbmXIOJ-4RxeC_Ie_ykdQOCZxlkZAbCE9JZd4NET57YrCfOSDz1YZpN3tQWIpL3sEKZdE-8F9exIccGfj_TlA40LerOye7_yxvBOPML4tagJFTldKylceRtzCBmUbZYVLxMVBHI1K8vUQ61mV168LEEMrCca89E8vLDl_BUxXN70Us_iZiJH0eNtkiqNdwG_xXHz7bgTI8qv4Kgc7MUzneW_-v2uyGIEaX3vV_NQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=qqqD3EiB6crEgHS2ThIqf08JK738LZtHmXJ8hSEviUEdRrv8dKzwBl2GWtpYxk0dmSauoDz-ZAnma-ZgakgMqDwKhd1swuZbhw67_BHu0Z5jZ-1P69vrxL7OQ86SxM0o5jwE5QdKIldf-A1kLK2um0nV0gUijTU3zhLkCvHXSGIiUUjouakF0ulg1_HM8RBnP_4hvb07DpnNTRtT3d_wrIh0URLHRAOWYaXRpCA1Fpy_oTNvDuaWE7zPZowYQuni-fYrNYdhZNmOhfFUamOYyOGnEzp1__0Rk-UI1vEHsUAZP5hBfRhUQGuZKJ00-PVBaHizHY_5P9Iy9BPP8WVE-TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=qqqD3EiB6crEgHS2ThIqf08JK738LZtHmXJ8hSEviUEdRrv8dKzwBl2GWtpYxk0dmSauoDz-ZAnma-ZgakgMqDwKhd1swuZbhw67_BHu0Z5jZ-1P69vrxL7OQ86SxM0o5jwE5QdKIldf-A1kLK2um0nV0gUijTU3zhLkCvHXSGIiUUjouakF0ulg1_HM8RBnP_4hvb07DpnNTRtT3d_wrIh0URLHRAOWYaXRpCA1Fpy_oTNvDuaWE7zPZowYQuni-fYrNYdhZNmOhfFUamOYyOGnEzp1__0Rk-UI1vEHsUAZP5hBfRhUQGuZKJ00-PVBaHizHY_5P9Iy9BPP8WVE-TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t62NokxCYTgI804w0RTijDcH1EkDkiQ5WVbczslVRIq1hLMLp23xBr07xInR-rTBPB1ry_Su5VUUjeknRlNrhzpVKNxVAmhgWl1XdkwAVRTCfIY6OlV_6MH4OHp2XJ4pcGWLEjdkXi1L70emotEUEiP58dmPEP56bWk7xGiBfnawqlMMW61zpz5UpKUwUFFGdtXFMQcMSEHBV2GPaE1YJUy8SxdB5yBuv-9FSa9O16_qv24E7It-1uCVlAUF-mICBQDCkL7lu0pB5W5yI5GlAL0gHjLmtEf48aXSFQd1WPvyaukiArGqN4sxc6Q2f0rf9f7vMauLxrR9b9eS4azB0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhkjJ86g47twalzMjKKe1ENDYGVxE4io5TUmOLRmuwUWGiXY4ZC01WW5B7RstSeBdP32at_wuWkS0VfD67imIHasO1HF79JGEPUas_5XnM2H1hQTlQrBAtO69LG_paeEvIj-E_tlLJZ0e5bgQNa-Uia7HgXFkIazDgHgsXSSLXvZzQlVftwSn1mHS92bdIpB-80XxEu-y0JzYej5t71ZgzAMBj0h-eA_4z3nquRSF8yXGmXwLusy-XOaOp1eIjbzpdRkIOw1pomsomXRNAmceLdbCfDoaqF2DMDOwKVngXOD4xMD3X538jWFnK-vgsJP9AQtE_pYHUTP9gy4mVj2ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkhurHQYHeG-zkT8g3HEPsElNXFsXQ7rvLGbdjnf2BCLSaAZWwmlunpYP92hE7O6IcPnLFs0ySLcQa-2S-IhGmfVwKDizv0c8QDnWfurGjF5Xe6egUcFGQAreOngWI_uPidhY4I51l9bh8sSCoLttJUsAlpcHEzocCXqFBkbchIDseNoKUIZ2QXGbFrep-VqmZY-6Fj5mfilb8PkEch9XJLG4zd8VRUMZ7jfks3xIjgdkpxSC8oAb-x9o2V1ElIr3byg4omOf8Gt-WtisPnHa0zL5IJvAafA43gsBOMLw0sMPw1XFQ5Nv_k5zU4aJkxgdV7IC3KP9DbDH1Xi443xoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nv1176_SXDm0oKhv_1Mp2A59W5zI9u0voODbHxFarq8VmLvIATrtsRic23t-1hKCu3Y_uSf8KuSy6OlNZA1guTRN_dHl1rivfoJJ9h_EQ097wd_KON5vyUzYBlh65CHfGT-2UOFGZZ_qe3_4kD8pXziwvEy_LS0YOF5u7CdRSh7mNrIgJQ4kmXE_nlHgLBCqv4UEdvI-6KZ82mkYk7SkdzZyOozkgIJly_LZVtJrKVVruUJhsUHml2BRwz6Q-SigBUky09urnnJDHPwGOD5Q0M6-ch4a2GVqwa2mGX3qui5X8yBngO9DN5cjdcku2j8jW4M-SBvkaB5rzBwErA8pSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaLOXCT0Ys0pTTe6o2U8cFput0UBt1M3K6zVIJQ6hCZwvVtbpsFCKWR4BKnk8pgFTzvWaUT47fKZtha__dZu_LRUE6_YLg7y3aOsozGS-8SixD5uiCUkmOo3HRS45AfHvXdCiX2bOHgwQbWL7HZv-BiXsdzWRqyGph6ZneX4ChznkzzFNiC3jLYf30391-vY4z5Gd1rXj1w2KEnbOPbp3CIjmqRCsY3uHKn6KTVtC0Pr1QjnmyPLbxGrgy_i-2wir5wH8idZ--w7DwyJpnT0Xh2THMkLVIDzDVFnArOYbGgX7egrPnLBZdBMnboE4SkwYGyQrMu327trkYHQjGLHfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5Ui4-NkR_94Wp6JlYEnTcJ8BITyGpOb0nhQmS9riHu7nZVR-aiMhSLn0i9-Xh_Qaomzyx5aV4qfyI1vpuQ8WZsf5H2K2t9_YOsjDKyI4plpxDCDxD0b6DJPeLGXWbn2FG7hf8u7fjQ0G_HJP65AEQz9N-AZmO01PIYTdJz29fiqt0tGV5nPIrw8vFqcZuvruqczKrBpxuA6Rl4D_nQyygDMg9keOZpLrY-tD3M_t5Z7NFciTbsLoQ0ZdTVopJ3OAa8wIdakpBe6Zk7XtNTuwWum_ijHPRdaqVZwqObNIBNIO70cBhGU3EnhyWnU530ue884bGFusO8PPsfAHtd9yxjY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5Ui4-NkR_94Wp6JlYEnTcJ8BITyGpOb0nhQmS9riHu7nZVR-aiMhSLn0i9-Xh_Qaomzyx5aV4qfyI1vpuQ8WZsf5H2K2t9_YOsjDKyI4plpxDCDxD0b6DJPeLGXWbn2FG7hf8u7fjQ0G_HJP65AEQz9N-AZmO01PIYTdJz29fiqt0tGV5nPIrw8vFqcZuvruqczKrBpxuA6Rl4D_nQyygDMg9keOZpLrY-tD3M_t5Z7NFciTbsLoQ0ZdTVopJ3OAa8wIdakpBe6Zk7XtNTuwWum_ijHPRdaqVZwqObNIBNIO70cBhGU3EnhyWnU530ue884bGFusO8PPsfAHtd9yxjY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnLQYL77OxRTB3hJKfpca_prR5q8Qm-3l4tePEt1WLNHJwjDC3NulFtUCrGQV-gHTunLkalFRnCp2I974Qe_zO3vGojfDKal8ruju8HZz1zk-vhfREX5HS8e42YzK2Zj9fsd_XbhVjaxoUQBGgAncNii8BxMX_LaT5HbswlNERSEYXTOnqJX0VWXw8ncGhGDEVyyKTP1tAuf-enolcq0psJl1LJysLCeAFdNixAA16YTLswE_v6W69_39YtoekUB8s3GFAqsk1jDIyB686RIt685Aq7MAczW27pxfXJmDpBC1K89OLUZ2Os8RmQwXKd0rsTlRk2pmyRkRpnLACcGlVu4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnLQYL77OxRTB3hJKfpca_prR5q8Qm-3l4tePEt1WLNHJwjDC3NulFtUCrGQV-gHTunLkalFRnCp2I974Qe_zO3vGojfDKal8ruju8HZz1zk-vhfREX5HS8e42YzK2Zj9fsd_XbhVjaxoUQBGgAncNii8BxMX_LaT5HbswlNERSEYXTOnqJX0VWXw8ncGhGDEVyyKTP1tAuf-enolcq0psJl1LJysLCeAFdNixAA16YTLswE_v6W69_39YtoekUB8s3GFAqsk1jDIyB686RIt685Aq7MAczW27pxfXJmDpBC1K89OLUZ2Os8RmQwXKd0rsTlRk2pmyRkRpnLACcGlVu4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=V0h_bIQaN1jOcN-UucFmZsW3zfFk4EMQMl0mLvDcbWO11Q-Pv3ILW6YKahSYK7gXJERfjxhFaxyxg8AwVs1ZcsdbqV_9mTXjOw-gFOIpMiJYlK7FVT3JkrBFECs2CMCShEgkG1Dyq-6AtjulpkQ-fqq4hVKo4WMCE2W38Ur8ru3F2W0J9NV6Mehn7k2-BM_-7o3jCT9KN2aOe6SJEZ21YoylrYqmCcfVjZWtWQc9h27VCRj1Bly4BpLjCeAKJTPz-dChrrGR40Inyz9QL8XgpVfCMOHKvSKcinb8AskTovAp8akVXIRsvRD1g-rqajmmNMHzgwx9itKeBv59Jiy88Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=V0h_bIQaN1jOcN-UucFmZsW3zfFk4EMQMl0mLvDcbWO11Q-Pv3ILW6YKahSYK7gXJERfjxhFaxyxg8AwVs1ZcsdbqV_9mTXjOw-gFOIpMiJYlK7FVT3JkrBFECs2CMCShEgkG1Dyq-6AtjulpkQ-fqq4hVKo4WMCE2W38Ur8ru3F2W0J9NV6Mehn7k2-BM_-7o3jCT9KN2aOe6SJEZ21YoylrYqmCcfVjZWtWQc9h27VCRj1Bly4BpLjCeAKJTPz-dChrrGR40Inyz9QL8XgpVfCMOHKvSKcinb8AskTovAp8akVXIRsvRD1g-rqajmmNMHzgwx9itKeBv59Jiy88Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHbFIwxXs1ySFtyW3IhfptOUunip7O-p0NM9oVaa8nUThaaiQteF8A-eC8wvVOuJxkEG4BuTgJlM1WhIk6cguuaEeAevQPrl9kExj8p9rb0DTjxWWae9wjsJTBtogkft7lnWoEHeUT5tLro1wR06cM0fSjXM6-ozDsqvQI-r6vPbSuw3OJWaUYQKpOqWlz_Q2Xfa8qI7ic8QtwNBCfN0-z76Pe3EycIsHfT8Z86__IhmbNpCFUl7_DviHwIlehnITx5MUMX6RMQ74Qb7y7kifjkjQchKfhO9TVSKHHwLXE0KruXIpBuxs6wcCW14wlbLAlTNngPLDuEDgfAnoP6AdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqDWg-g7fInuU9hZkV6KxJVlTPFzAbLunaUXqgMt9QBrYMLcRlbO4TgQje4CzpEKw1cVvcfsF22amKe5Yr9WBgpQsybVcU1qxuxSvPzwgJhFyOh5vyxDF7uj3v-NxEygUGLkla-tl2Ykjq62MmjT-jSfxUwI5f3CzQqibl46-LKcGt5WLgY9L_4A-TjiDxulJ6tL5gVNogzgEPaD7EsBSiE654h85Na8QbFJnvwDo6VdBURonS6FiaBbH-A1gJ0GxnOAPO_AXJgPH3OI2Wwvu0xteY1gLfesEjfeU5UqibHpTjh70c__MOHvzjw4u_qfeq2QfmNnDmbioD_2o1VR8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=LOcZsBI941FCEJYu8shqvXGDYjoffq4o_clFISdE0Q1Ar-ZI90uZB1osIfi5N5t5NGGpUOu4Zmb4d1GSgMmpNowFY_OFwqvlQHOmwiAFCENrGviQBnBtANqznusYw2urz7rIhOt_fNoH-nSEfuZjBzxSNCHtBV8N0YCM70-r7qtgYsJQUlK-bMODWY77N6eKtKiMgyEg6R30_uIWffMhaNVZXGkOHuUPW6ZcjcuZzuWZfP_VYcEr-ZVCnp0PvHDE29NQvXdfn8zPKw1MW-vc9yRgqj2yW_4izlale-EqRn7D0fhrbR4gyDNTV38yKY7uHK-_onJV6-I7LW5DLrhn8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=LOcZsBI941FCEJYu8shqvXGDYjoffq4o_clFISdE0Q1Ar-ZI90uZB1osIfi5N5t5NGGpUOu4Zmb4d1GSgMmpNowFY_OFwqvlQHOmwiAFCENrGviQBnBtANqznusYw2urz7rIhOt_fNoH-nSEfuZjBzxSNCHtBV8N0YCM70-r7qtgYsJQUlK-bMODWY77N6eKtKiMgyEg6R30_uIWffMhaNVZXGkOHuUPW6ZcjcuZzuWZfP_VYcEr-ZVCnp0PvHDE29NQvXdfn8zPKw1MW-vc9yRgqj2yW_4izlale-EqRn7D0fhrbR4gyDNTV38yKY7uHK-_onJV6-I7LW5DLrhn8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHaXGn49Im1GEzJbiwVvuQvyG2IZKE7YuzhWhDayIZ_rdKZOYKLS2lqMRYSVo3Inqxu-dOvRgWnz3-KGYllgJjL2qVCiWreUtOilSDKoBeFSJvY4WM1nvOLpSZvt7ILynIlqyFfg1pK-9lghc1MR5UezxbuZ68usdCLjRMO2KiAQBJV0LL57ZIo6_ArVJ2-sBqk1N_aK2ptUYT1sbHFBk46Ujm-_gpxs3V7Z4Wn2e3TtZ85GMTgc67qzjZKfrwvS2i66H9IvfhptMeV1h_CJGpmweSXFpV1G6OLZ9OFkc1HTWYdp1Hg_GOGhIxsFYe9W0yC5VSHyHrjKJ86i8w8Cyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZZzKbJc4DdiOGLmgS3j1IoYd22WWbI2990Y-jalojHXmW9cpphh8iv5Tdqo4HECvo4ISOA5JeCop4Xt1QBkg3iGcXrh7k-C4V29N9TVL_IWdcdiVOVRYl_5v98Vh9qD7zPZVBS2nexb9HH5LUh6oDUqowmDeHFOlrrBGWCJvO1mbs6A5Nab52OijRmy-NwmBt-xVTZ-UC_w_9jg99oQ8YP-oAX8S4_CC-dw5J8GCz5icPu_b-G7pVC_MrU6SSbvlm6m6NxccFrB8JfC9O2OO3w2dQ0YWu0DeOn_PufP49wnsyqYvQ0YF4vm_OXVLyZBHuWssCNeVGbN2o58p1VebFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eh6RxO_7mmljHo4tqfcHWJlFV2O3PE762lh9AMEYZ1_eIu_vX-G----uO2R2GPNZn_jsPK9mII3xmQOaCuePjHwl3NGWvMvagvbSWyJe8T_EY26EljdSW86ZCF7LwaFyN0-AK9ifJGI1fPcZlR0g2W9EM37zvVmtvQ74BmVd9PmwWhgu0K4Vo3A478QKZsnZpXmzNHlQSjpGXP9PtoZH82Zb1bPj0SuZl6plwdDNwDwBEjneuMXayf3QlqHNaTMyV_2qeUQlVQCPv0XFXnsNag_U0OonO72vZx--j1wlZqkeJtE5iC1LWCPoqLIjFOflX8BkLulQauTfcXs2eAhAbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=GkdikNhHM8B4uKZhc7k_pf7f9EMNZ8JHR042WR3efl_u-FDzOseYtQfOWd6LzSsjXubJE-VS746vf2Bcm5DLix5zjHrIq0phjOfecudI-WneNjFku4UCjuH7Atw6bGjrm9R7iOCQGSPXYR-99dWrs47Tj66ZNHEFi8Et9irDMn3-izzGdX_gCVnQjUuWF1R69JDyqAUiiNmPI2-Fh3yn6jDsso5T5Y-AeR7JrlSRFdd25odG3M7AaU4o2yS4SzVftOfX_pW0ZtiF-7tOd0KORgT_pPbU0Rc3hfWjJOpNF8QC0jQ5FV93rYK66usSrqcaQfi-WKWXY6gx6U9EsMnmFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=GkdikNhHM8B4uKZhc7k_pf7f9EMNZ8JHR042WR3efl_u-FDzOseYtQfOWd6LzSsjXubJE-VS746vf2Bcm5DLix5zjHrIq0phjOfecudI-WneNjFku4UCjuH7Atw6bGjrm9R7iOCQGSPXYR-99dWrs47Tj66ZNHEFi8Et9irDMn3-izzGdX_gCVnQjUuWF1R69JDyqAUiiNmPI2-Fh3yn6jDsso5T5Y-AeR7JrlSRFdd25odG3M7AaU4o2yS4SzVftOfX_pW0ZtiF-7tOd0KORgT_pPbU0Rc3hfWjJOpNF8QC0jQ5FV93rYK66usSrqcaQfi-WKWXY6gx6U9EsMnmFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=Vh1k3zmZa2oQvo0Klh28pJ5wYBSpNe9-B99mtmGC5TtNy0Wtr-XTPOvRQVXL2VUCEi8XTHw1FPByvWPV78YcL4Plnk1l55Uok_z7_DmHdNxHFFfqJLG4YzKV8AdnqlM-9mnp4qUg0S4tlJkUtHlLCxAcoBzKJcBu9cbRIt4u6Xhde6ZQgoB_EO1Qo6uUfp9LFTiH6peEmlWpCcX_M59kBJVk1xfVd62t4bL8UOWthi9qddUnvlZICJEHImhpTP4BY9xzicCnzHNr5LTSCODRPiexkeZaekRsda-6jF0KklsBtc-1BM8E-KdpHyNVvcugXnD8YEDAD_POoaP0Xx0zNYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=Vh1k3zmZa2oQvo0Klh28pJ5wYBSpNe9-B99mtmGC5TtNy0Wtr-XTPOvRQVXL2VUCEi8XTHw1FPByvWPV78YcL4Plnk1l55Uok_z7_DmHdNxHFFfqJLG4YzKV8AdnqlM-9mnp4qUg0S4tlJkUtHlLCxAcoBzKJcBu9cbRIt4u6Xhde6ZQgoB_EO1Qo6uUfp9LFTiH6peEmlWpCcX_M59kBJVk1xfVd62t4bL8UOWthi9qddUnvlZICJEHImhpTP4BY9xzicCnzHNr5LTSCODRPiexkeZaekRsda-6jF0KklsBtc-1BM8E-KdpHyNVvcugXnD8YEDAD_POoaP0Xx0zNYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxMXdo49vwZ8ErKvY1iIkGo0MJXHlr-JA_oQ0VDyCnOJ20kE9Qix227no_W9Rgg9jy_fvY8ay4Fr1djjBfTTj9uv6UU8_gkmxpn0bPg82i4MKkdTEIJLvY4FtuIasZi99664LuW_3TXBBWyeJwD3SNpYKL7aIT_CziyV3VnT3Uq1FnKhADhj_dgwT2nz5QTBICrcqf16-BzHdM8h9LcpE5JCrUpx9JQaG9DfgAt1oBBCAkQ4s5HsAJJflpjSfqsl9GymjP91yVP_t2_DdNXpmykNjuAuVYnHvRd5FfXTzsNw2_LIKHv-nfzKh78dwjpiJeIqx5bffx85VN63ZCjwhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkJ9ZyRPtQcaw3MrKOt89_YfHrkSPCJP1uzlzQnNHejvipOMEHHGUqnuMT25fKnjd-YMAgoQtbJTlqCZCsohyNwZv8LCS7lKTNEMuCubmKLeOA_mGenxue2b-QfwRdcPdOTavBrVLStHb6Z7GO606eVY68-w6owOww7B-zPDbT3F5pyngKZvspvmlZpzIUm9UBhkQFgxj6rd_Ytal5mVyORnpqvQS27aY5k-Wgub77jkLlMyTSmU-XhFpTv-CHvsRJYLIfzzOnLD3H4lmrYXcufuGuMpSL3044WOFiDtLKqMFp6wQtaJUcjIn7F99Vr3wQhEH3sM4N1YlsyW-HNO4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=R-etO5r9F011TlUixw6mSRlrRi0d5i926mbCbWtmrSruMDlBL9nJnu8Rn2UpdLsvbk3fWNOtu54N49BZSC_HPnt0e9pL7bTDbP1oru9kzTZTY1h3f6K_KGk5dlFOYTrSC18IFU78DR7hKUGfolkL3K0L2qTj8hw05gPq7UlMI4-pfqy_RJVACKC1vmLifeHvABnfgB0FmfPJogwHOhw44jtxCyKgTwVkbOcPlEXsb5EbYDSO-EfD95yKYd2UQ17uI13hE0pOn0Jm0En1j-aHiLdaygG_2EUOVO9UoiQ2ip_2kQpInzLxzRoJXneEtyXug9Q9lZ7MfE1OD5bLDFH2Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=R-etO5r9F011TlUixw6mSRlrRi0d5i926mbCbWtmrSruMDlBL9nJnu8Rn2UpdLsvbk3fWNOtu54N49BZSC_HPnt0e9pL7bTDbP1oru9kzTZTY1h3f6K_KGk5dlFOYTrSC18IFU78DR7hKUGfolkL3K0L2qTj8hw05gPq7UlMI4-pfqy_RJVACKC1vmLifeHvABnfgB0FmfPJogwHOhw44jtxCyKgTwVkbOcPlEXsb5EbYDSO-EfD95yKYd2UQ17uI13hE0pOn0Jm0En1j-aHiLdaygG_2EUOVO9UoiQ2ip_2kQpInzLxzRoJXneEtyXug9Q9lZ7MfE1OD5bLDFH2Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrWgBlAG3IE-H789n6PvQhUm1rrE3V_SvMFgzD-XPYfdFn--YEZFvcoBtt5BrK2qxx6RELP0FLQBupJF13PnHR72ySmQDY8mnfOAcH4cbwWLtkF233Difyv1PPa7S9x6k_yf4A7rdFUNXMOS4Lv8p-9WnD72cILLqL6Qnpvssxj_Ul6XZJngqdvq4P_Gp1yVwwGeVUQipCV8gcMM_c514tVYfhPSi2WMtReKoSJ7Es3yh0TeLEEjz4ztZ_BLUruwEFFBkmSO_gmJ7478x0svqPHnpIlKu-nnpKB5RJ8SBeNvj6QnQzLTFJUVSMuNR26GM7h-Xjq4wiWc8H4Si2C0HQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRHUm5v3OV9mNazRiw5uuGtyG2nTpJhTy0JZSykBFKYkhp6KpRpp-DXph7DpaYiqAEO0zl1lH5YSq4eWILg05nstHA-I6Lx349idsIi_vfoMmylbp1qMdwt7Ejr-HoG69NsiOD-kwqf1tBaeHpHaOOd_XWm6oTtu7Y2GgUQuAf7uzTTaUi7AvLX-5PHEwAzaedgTDrjrPEEGNXO0MwS7THR-mLTBWbdizUklbC9IIi5ZHLs3zNhE2-ir83UG2Mld6jHIb4ezAYXxzgjBsSBhKjGXtOTUaEjNF70yXWxv0km_OADp2h81gy42--448p-0hezPo6aW5-zv3npEeXq_xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ss68hBg4aUEP11QJBWnX6DfBEBsZ-7IjXmo1JsciCva5mFddb29rG7gIgcZyNwoJubBPowH-CAWwsvZML-CzFcXUn3nxas0AftH9g68g5eO_zO8g-g1wCMNqCBu80hnNZshcqB4l4hHugPbG5r-wEtq04MotMm7RrUlUh_E6u06t-1xILlKPxMRDBDxfaW_qCRFGB2Pc0ZDTMsTMWKXpRUvJzVSZA5UaHeXbQ9K3RABjfxqGgz6r5XkvK9i7U6AgYx6eB6k68CZVfVeUQYX5qUCg39LFqMyy8m55D-3XPzyCIkp-zdA1DG3RKwqca0rNzVKLme0xlGSQIG_bzZTkCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLWactQEleYcuNJPc1eBhAikWxhHyIKfl6SXWsTxEcRVofWVvyCQSbPjH65sGnyskDiIrcs8uev9OLst8vIzkUyNkAFDAW1U7M2YbBE_i0XaBfylQhjA5aBYZsQYGXNRASQ4jSRbZBOrqtYTrD_dYphBu8dEn6dQNc6-ufoJXMLsRXgr4DnywaDWf_-j6Jaj5PEWMqf1iQh8xg9cYO6Y9M50e1Wc--4RPhZHcOGjUYT2DiMNp99rWWj52dpp8NvEbdiRCnQ7aQDrp16iHfmmj9xlZwM8OuW7lkqzgm9FR2bHkrudRDyn2_M3Ys1kpDnAexRP-_irobW5NJkUGd1-z1RM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLWactQEleYcuNJPc1eBhAikWxhHyIKfl6SXWsTxEcRVofWVvyCQSbPjH65sGnyskDiIrcs8uev9OLst8vIzkUyNkAFDAW1U7M2YbBE_i0XaBfylQhjA5aBYZsQYGXNRASQ4jSRbZBOrqtYTrD_dYphBu8dEn6dQNc6-ufoJXMLsRXgr4DnywaDWf_-j6Jaj5PEWMqf1iQh8xg9cYO6Y9M50e1Wc--4RPhZHcOGjUYT2DiMNp99rWWj52dpp8NvEbdiRCnQ7aQDrp16iHfmmj9xlZwM8OuW7lkqzgm9FR2bHkrudRDyn2_M3Ys1kpDnAexRP-_irobW5NJkUGd1-z1RM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q_QNkfNrpoFH9xqsgtIhBq7vBT1Kw4BiOl-L4Dzyb4fCPN73QaLse_ODoSqpWO4SRLAXKC0LrnSHgtWqJUAG0zbYnFRmGBlDX7mALvna5sz_lAjZozgzaTzXU02gl26kfz31-UHti3TicOfG8HEW-9OorIlmdMU0uu-dJOF5JdVAmm28KZsCZ8bVCij5QnnptgiPNVWjB58DZKvL8-Eem8LjLLPbYOfG0dulfuKb-A7JMvAkc8Q0wgvx2hRlUoc5ULDLmngpYJcbRw_d1IJiKqYIfO-dfYi2ImitiaVuhBQaASlrJGAcp3LWE4K5SpnKMST6kp4sKqpVTVVfWwo2pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ekro5katWUQTnhS1YvbGtLrZvHxJIkgAWzyiz9EzPM_g3rBztd5_PLS7gu3osItYoEbUIzL6-AZPwRnnSPF0motDOs3bKbauSGrwcRXrTchfL3b3JAb4hQn3W6Y98bQT-nEv8gToU5ljumDhwSYELatfos5mZl_yUdRBkL4bADFt7SYMIbsPTnR6Dkz35OEhcyiPWrVku3o2PARyWhy6aq39r_nH52Fa48OW0eCDiAJSIpJkQ-wGuXgkSQMrihruozoDTejlVdctigDEYLk5TBKJI_X9nI91QEVmkuNBX7KntK0ZwrKa-Nqft5-LqR_-VS5dk3VOkrqrrPgmF5eGFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=JGz2AujCtLuHl93bj7-zYn6DXYi9OxiUOTuoROxMjTNpXNOw_lqNmOV6at9_ZgRTsdZXaDfn88s8NGJQWcXpj6UsN76hmyajr2EcFyC9pfWfXGgiLyu690HXAO9v5lT8CxIE0-km5bUeOF8i0jVdwLpuUQ8d32RS8U3Smc5uoQ3Gx4MhlaVob_CaiQgX7Z0g8Fa2oFHy6ntdZchIGcbG16iO8O2OYnrma1eILfOGS-sUejrspwMBJzup4c1zqeHy_Zd2gevbFmrMeEg2fHx56J1C5je898Ydvn8ieA3imGVGh2qJqOUqXcghwbh-LI3di8MYEEKLOtckzuPF_6mbJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=JGz2AujCtLuHl93bj7-zYn6DXYi9OxiUOTuoROxMjTNpXNOw_lqNmOV6at9_ZgRTsdZXaDfn88s8NGJQWcXpj6UsN76hmyajr2EcFyC9pfWfXGgiLyu690HXAO9v5lT8CxIE0-km5bUeOF8i0jVdwLpuUQ8d32RS8U3Smc5uoQ3Gx4MhlaVob_CaiQgX7Z0g8Fa2oFHy6ntdZchIGcbG16iO8O2OYnrma1eILfOGS-sUejrspwMBJzup4c1zqeHy_Zd2gevbFmrMeEg2fHx56J1C5je898Ydvn8ieA3imGVGh2qJqOUqXcghwbh-LI3di8MYEEKLOtckzuPF_6mbJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=rLNwiD-V6OA89LMsYFzVXxp8QLtOt1HJeX2s1f8z_vRKanyb5oxh11FFlw8PzVE7_9W2d73-26fHKZvDwfi5gnIgbkMpmq_4iYalycfOKy_2_rzP7zkWk8mmfGjeCxnbxPrnbbEvDhpWMNgDKJ2zmPfH8Gdzdh8n-rlzKNTXDwHHvmHn1Om_s8UnzFFmVUW8c6ug-aNFHTJzlJ2PpJ7rxT37tv9dLne2VGT8mIwBOSICRuTNsdUoQljjMYYa_3z2F_cWBH_UifbjU84qMYiSrWYAr11tfBW3bnzE0QDTTETM1dTyP1lncHCzg2PWubQBZ450rl4WYQTboSSdlnKD8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=rLNwiD-V6OA89LMsYFzVXxp8QLtOt1HJeX2s1f8z_vRKanyb5oxh11FFlw8PzVE7_9W2d73-26fHKZvDwfi5gnIgbkMpmq_4iYalycfOKy_2_rzP7zkWk8mmfGjeCxnbxPrnbbEvDhpWMNgDKJ2zmPfH8Gdzdh8n-rlzKNTXDwHHvmHn1Om_s8UnzFFmVUW8c6ug-aNFHTJzlJ2PpJ7rxT37tv9dLne2VGT8mIwBOSICRuTNsdUoQljjMYYa_3z2F_cWBH_UifbjU84qMYiSrWYAr11tfBW3bnzE0QDTTETM1dTyP1lncHCzg2PWubQBZ450rl4WYQTboSSdlnKD8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgtIhq5zK82tbP5tXJbpf1IVw0J-WyMlyPlXP4H2YKOqa1bVm4Jmv03GP-TZi_cKaEBF9FvFswQ95MpgmfFmWfTyPWeyT5mP0jGmDhtLdTTqAvBeWQRPJNWIcTHUO4W7vcYA4Gtslh1dmSCFek7Plaqo_EAseQsecRw_PaDY8RXNcWsQeX63MWIXXxTWBKnxRepYRDYpBQbnLV-X-wi019uTURIkQEDdZizTGrOhIGFif-RoS6XBxS_KCAb9897sAsyI3Hq6WqeDiR2DJIxV00Cik4Q1nlIjGrr9ZhJdObMiGcB3gr-CG33lCaiwSuyCPVcMFx0KLKKjizmCC3I-Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ko-Z0JRFASbQEiUvPWNkzwq8jbPGFEYF3YtLc-kIr_RxTStr38qdIkM6AISar2clUtsAUteL12pmkgJdaGFkRAqQnHbeN8-gtvQtVOZ3Al-UhgX625kwY8TinUn98aYU99MbH9O3CdRc_9vf5zLNgi4hSSdv4KpJQXng9SnFB_P-xK4OmeAq0cuRPYnl7VfajMYwdgJak5o4yFnOHUGc6o8_vaUou8DeAQ9kEVLWCL6JEoJPV_2OkzUXnP5Iby3R3twjAHmlL7GPpYPaxeoWlQDwub1t7B-_BOLPJZieP9mI92PC4df24rpebSyCHlWY8BW2QSo0vbcldpUHDZchIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=cWNGaOSfY4g3mvy_CCOYTmLvgT1H_OoyQEORYDVIvoY8E7qilGLOfVTBGrnATfpcAVsohMmZxzyKxPeTAehf7Z9LVk4AM3SULkd9-S6BzCMswOfuaT5we_WGgzWciGxi6-gg1VHHo0xwze1t0r3Wzb85HNhcIr6LJYNo4k2_4Tu9HEPCLdPWzoEBVT6liQs-O3dNRUSzhE6-VJR-_oGzyx32IBuy8OGzWDkbnzwQ8nQlHU92RAIMeog3W4ckWUqsX0RgpIrDa8la6fhFnxKvcVXbG9hD0H_StZWRsrTwyAGhcWI8L2n6qOWfxJbo9v657V1fk2CKfqx2g2-gEeVbfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=cWNGaOSfY4g3mvy_CCOYTmLvgT1H_OoyQEORYDVIvoY8E7qilGLOfVTBGrnATfpcAVsohMmZxzyKxPeTAehf7Z9LVk4AM3SULkd9-S6BzCMswOfuaT5we_WGgzWciGxi6-gg1VHHo0xwze1t0r3Wzb85HNhcIr6LJYNo4k2_4Tu9HEPCLdPWzoEBVT6liQs-O3dNRUSzhE6-VJR-_oGzyx32IBuy8OGzWDkbnzwQ8nQlHU92RAIMeog3W4ckWUqsX0RgpIrDa8la6fhFnxKvcVXbG9hD0H_StZWRsrTwyAGhcWI8L2n6qOWfxJbo9v657V1fk2CKfqx2g2-gEeVbfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=mfCUqoCaEY5XgPr2PFkbk5PF4JfCyAMV_BLnHbjmmyqgsQPF9sOq5l6p4bGs_IlIG8He61SY6pcnfnYNjqoVvtlZqmk4EQx6lOiZ2bZWnQJXAM002-S36vZQcVcSnM30DsfGi4o7z6-qkSh3Qhmk-i0rUyg_xHycfhdDWMs_Tf7M8G4TU8rdIohGBNK6eNG2kskQdUB_aWdDkQiMuzXs-TBS-SUh2LCjWa7nR4Q0hKdYNrVgOFv5engW0XxZ56JToaQGC-h8kQkK4bby2QHMcY0qW80BTeItXJFek0-Ibtzzn6BRNSyNumyqqNyRB9iAQ1SnjI5jj_JIIkfQet6inw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=mfCUqoCaEY5XgPr2PFkbk5PF4JfCyAMV_BLnHbjmmyqgsQPF9sOq5l6p4bGs_IlIG8He61SY6pcnfnYNjqoVvtlZqmk4EQx6lOiZ2bZWnQJXAM002-S36vZQcVcSnM30DsfGi4o7z6-qkSh3Qhmk-i0rUyg_xHycfhdDWMs_Tf7M8G4TU8rdIohGBNK6eNG2kskQdUB_aWdDkQiMuzXs-TBS-SUh2LCjWa7nR4Q0hKdYNrVgOFv5engW0XxZ56JToaQGC-h8kQkK4bby2QHMcY0qW80BTeItXJFek0-Ibtzzn6BRNSyNumyqqNyRB9iAQ1SnjI5jj_JIIkfQet6inw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ui2aZEZ7d1vCvK-aaQCKEf3x6L9coW4zMUF7NpiLS_FQt0MNgxmRDn_F9o9UR-r82u48HSTKGso-pYRnCf32JRHyG4Puh1y3PcvIoQ6yw_DWaDHgAzVNITieEVjK78LBdYnkPtMkYqEUpyJZcOIgAl4x9XRnUDB1PE9sOJUeU0ggC_98NYXfCCLjtqs8rblVNbO2vZYG9Za7H4PbOlw_7AiPVKfYybxhHGCAhFqbFdGmH6ohmB0ZdSsE8qXG36iJVLvEX5puBT3YseVmBnUy2_2vQ4biCslVOz_vBpi3d8KFFP0rby6qgCse2dOhk6m3vWdXpIWstEhE3Vy-KH1OZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6401" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuhDcTOokrhcc4wcJFTIQv9oW8ILhSQqi0-SNTbzYWEeti0p2RsoKYP7GBDcRberAR7TvyPoWIBLAzQdKS8VeyqC6UmmCfILRykNL34TDilCJIc7PDwA5LOVyIbKnOEJBR3uDDEa5dtXn99_uLi_ArtJuo6YDX48rOiPpaKRr2I2dF6EPTk2La2OVWiTeCF9LMH8QGQOA-gjZNQrJUcIKTSKL79dCwcVHAGQp6OIg_Yt1ts62MxWpLuGBgVFvATTl8sZa6mjnlpcqzyb9DDoY0Z8rl9_PlOp5bXSmd99vL1vnOquZn0TrU9mMfatqONC3F7hA5Gqtcyp4BDhlfC9SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQwssCjwr1hlyhKINB9KGzmicpy07iLuEEO8n5N8K5Z5bIVFtn2yOuhlSgevaUmRcvHsRAuxc4sVL9I_JFYWgMJCHEN_4YSLEmc9zAk5k1HGuzSTgbNdWUw3vCNgsJVItXjs9EJ8EfoxICZTJ9bSWl8X4vLtRNiuPCZBxbcMv5ZfuZnaIyFWnspNoyyUqLNBzfLO8wW4Ghhu0RVHqQFO9PaIvwghTRla2Xl0FyxeUUSYx7kpGrdFTtrpl9cYNTNTndMb_MOjwrP-LJgsE14JpCCm2NPj1YwW8Va_07QKQfMhJtVoKcym_Npf9GJU2fanw3boUIEzM-MCN-ajLyEuDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsICx01CAPRthEh1eDr0NkNC2Dp7deRgPulS1JZHFwJJ34QU9zYMN2jSdYLLUlxrnzXLvY7z4M_kG0R56f2p679lAS-e8qSWQ3AFrWBhhY_1s4qyvQlNf9FVAGFUQPkLeDbe6nTLXSJuGXC69Cfix0ANGBC6ZnN_qAECFWjpVJ5bkykvRqoHDYkvKEnFoDEjut3mhwgMT1Xjgyq5PCbE5Nfod1vIis8P056X_80bOV2v3cAPkA5qhlpd3EXM5l2W5vVtkXMoHUNK-iBoxC14Ic70xu9JXA2JoBu4lYOsle5tOIE67V6mrgklBvmPmAjveVPTeRsftdHdecRx62mSvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yv9phF1XZsGUuBjk4d4x_6kUA11m64DaYkWk3kee8C7jaq8FwUMlBJkzR2-hpIkhC6TA6bdG8YfHUZiWP6QIIG178W80wOXiL9WHauWsFbGoS8Cmlt-ITA8UJMwYSkQC1SAHd3oFZoOnAdXDr-dZejDQEi4vILm1tsDLWDUIn16g9amHJIg4XVZa1Qyz-uhK6pryZkN4-eiT9d56kpVaAaESdd3-LbesNEBjMCtJ2iKzcOUKwBc6FPlvEgyn5JG0hgqdJaKN2i1hk8_pfAA2mwUmClhUG9F6aZclUZCuYN_vig3pzjRwi5bp1OK4Oy8Etfs-aIaiNnIdlPPW6dnrVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DH5t3pBs3ohbhCOp5AFqeK1ULb_iBZQeQD-Yl_CekNNaTl1eIvziZCy-Erx4HO6qq8TWb5iQQDVX1pz9b52wV76QxdcpEssCkUYIb9EAcN5dCkhg3MhcALcQDRm56K7RhTPaDdKHC4ow4oe-Ieev1FHeRZWl-Upjo8PiHyJKaGpL097BtRmGXkqIjWovj7kqCgp88Yzvm5y9fBy8hqt7Od15OA-0dbmZ9KlZW9RwI6N1gXtcOpPTzayPMup25tw43pQj2oT2lRDeRx7jVgX5NrWekd3DkYYx1uE68cV5g6_qlX2EvvNE3yL6W4R_zKfo_3h5XMOC5iBQFqoBYyfhIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NW4G87CfXpoavhrKtjvifqom2FDyYa7BCUA9V0bjdYwdGg3lMei79Nr1zo93-rUE2lRcQdGXtYZ7kyFC5eWUH9pT0mRTe2hMAk3xkqCXHwoBHcUtqOifO0iiU996RCELfm0Cu_yahNozEu5nU15B7RFIgvcaQWbirtjmEuRt-5VEhs4Xkj6VU0bq6ET-187kIMGr3fJYF2OlXp3jJV9AlOXo8kg9373qo-GmkyVz1BT1ofUvfYqsIlJvctp--nILNVLjb0GjYKZ2DSIx00eYpBjBg_KSsMfozTAOfyn1PZwuGtw6U2gP_PVoadt1PEDLJtNS_-8KZ4w_ODrCJ2NztA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKkgv8XNLkos4ato3cVhdGq_g5Xx-ku4Wp-Sy7C5nQVN3H5OGlEw06V0Qxu6kzQ-0OMucxK5UzRWgJCPWj2IkubF5EkEUa1iqWCPnmEKW71J1_B-_FcIYGBmBhBfBTnL7fCdNJAIQfMZ9eozXhwwOn_MyRHjJdOXciK6nDYJLjPRY85l64wG-K3lbwN5qcEgZQw8nuyB_DkTSC53jmyEeVkhDeK_ZkkUSsxwqGHVZcgWNMF1jrdFiDJ5bahHFMluMhV8mjS36JEppi8ST64sFM_Hvy40HDxLQTXBF-m40civZY_10LeV0My8zTyod8T6tWaSZZXQvfEgBI2WUZLs9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8r5cuMLUJG7CtqZWxObs_uBrikO6hMw5pdA5L3QsRk5niq50CEV6Hazgx6wzlHT04BLAtecq69ef3yK6WbeRsHxADFrzki2qL0umPC5FsxHvTrdxXLca0HqIbMAyfthqwWkdb2e2joQXubLytMGPAIvjeyUmIVwhQkl57rBnxy2x2LseC3TLUpWKpuB0sqxZzunF3FpmqAqYIZ3raeOq0oTu1pVb7Hjknt9TS1hRIsm6pYoh_ybQhdchp57vmc7cMyEpZTbnQZHytQ3Qnz3m1WCeaCvrJ5dRcpB9F3PUVpFPAf9EZLt82p8jFYTprqrodOCjdmyLi3ing0Q3UYyag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ez4PlZHEG3uQ60vICUn6XFv9C1CxYZn8dyX9iHrRTY2-Hh67JlrFsE3cFfF7zM0OaHSbFvqvyRn4XBbnqnJLqoDxKv5sgpAAyQqsXhvjPZB-kyj2_81c2fhSR4CSnDUSdCVCsz1l-I7YfQ6NubrWlCQoky-cNeow7am0Dm0eOG6p8PHiKoNquNAqaZj7ulxGZPwCBUcZihXwwDTtqUl9D8yJ9sKPH6VFlyrvzKKoQo1r_tkxXEf7m2ihsyeEhmReQap-rsPf_XIC9_6EK5QFx_802_ts9cc16AO55Y4hzFo9dMHP81kfqxKO2LI6np95wfziS1dfUnOujOpN2-is5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=SMXFoYnscYgycvHI2uJIZVRoVYmDCKsXPElr4Nr6zwIQDfYZnjSB0YeLHGDaWhNkn1wGaISW8vj4YCbeWbeGirGL39oKv_oBWLAi24An85Mu7cr651mWufoghJLqT_TlqCJ6hPkyBXUMWopi6qs3Td950fRHIxSvQiRzHPqODMwVoNkNjOViBsKE7ra18YNz8LtbZUV88uWTCHJpzhbchrIfdKNdJz0-oNoeRFMV0bfwlt6zJlv2FP_aQZmjeD4leCHjbdcean8R5cifDsRhDVz5xcsU3t7hKSPAib9n_jj_JloPEXWi4b-Nzar9hpDozIQ8qfapD4LVvZOQ_S7RHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=SMXFoYnscYgycvHI2uJIZVRoVYmDCKsXPElr4Nr6zwIQDfYZnjSB0YeLHGDaWhNkn1wGaISW8vj4YCbeWbeGirGL39oKv_oBWLAi24An85Mu7cr651mWufoghJLqT_TlqCJ6hPkyBXUMWopi6qs3Td950fRHIxSvQiRzHPqODMwVoNkNjOViBsKE7ra18YNz8LtbZUV88uWTCHJpzhbchrIfdKNdJz0-oNoeRFMV0bfwlt6zJlv2FP_aQZmjeD4leCHjbdcean8R5cifDsRhDVz5xcsU3t7hKSPAib9n_jj_JloPEXWi4b-Nzar9hpDozIQ8qfapD4LVvZOQ_S7RHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=UHZUsZhe8PiZ3vBECgjUAFJq0lQoDz6BT5Z6rNhMvFXnFaCyc1hpz0kpErgX1tIPThvfxmEpN05HzPEj6YZLmi-wlTZIJuT1ay8K1kGKEkwwGWlttej4GNfdtuOdRQ09mGu7EasVb8u56ukwjWB6WYWG_IbpzkWUnbjjgBnOToSnFjNR72ooEw2Nabz7Ih7RH7zQpY5o-s60BP_cKwCacIt-8UNupxkZao8_AfO2VrhgPTJ4UUvjO3sB8GCPZkXAJDp6iWSVtBoVFHATA_SRVpm7MKOJORC0T9_A1UorSE-Obus_KL7c7qNeyXf1u89QXiRxLU343In3QNI3uuTPwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=UHZUsZhe8PiZ3vBECgjUAFJq0lQoDz6BT5Z6rNhMvFXnFaCyc1hpz0kpErgX1tIPThvfxmEpN05HzPEj6YZLmi-wlTZIJuT1ay8K1kGKEkwwGWlttej4GNfdtuOdRQ09mGu7EasVb8u56ukwjWB6WYWG_IbpzkWUnbjjgBnOToSnFjNR72ooEw2Nabz7Ih7RH7zQpY5o-s60BP_cKwCacIt-8UNupxkZao8_AfO2VrhgPTJ4UUvjO3sB8GCPZkXAJDp6iWSVtBoVFHATA_SRVpm7MKOJORC0T9_A1UorSE-Obus_KL7c7qNeyXf1u89QXiRxLU343In3QNI3uuTPwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/fe7zuIXW4-1Taw7Fh9wd-BmMrI6_JcLaEX1sHH2nexdbvIfyeLIqk8cKCKaoN6KYk99QsJ6ChkqwP8gc5HphuTFZQMmvaTDNSxDodXVQ7dFEKqOIF3-Z8QbLj0ueOcKRI5N4TakGJQ4F25uUkmUp3O4z2j49Z9NyWSgD-W3sI4k2BRmJFCqpVWim3Q5pB-tugdhgjtNBEXFd5z6eLuEXyDgy6OsY65moca9tw_a07qPDsv3OqIYSuKQ4YxbwHdH6ErTBKB8AK7JGxd-nBUaquwE3csGNxForoLvvgkfW2SW70YbhQrbUHTNaGKiXm71ZHwwnuSjHBx9Atj7w3K-MUg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 256K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 20:42:00</div>
<hr>

<div class="tg-post" id="msg-84416">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وزیر نفت جمهوری اسلامی استعفا داد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/funhiphop/84416" target="_blank">📅 20:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84415">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDaYLv12BYM9N-F1fr_8mUhLvpUa766jKJi2w2RsKthlqRFuEtiH2tN8_bLnpaZYIh8WdMG59VXqA5JoTfMnPiHZ5AuKfNnB_HnffAUZAIq70FDL2QWh4rbQ_htkrVvAKgnsfDxFtcy6PCAOljqAB1Ee8PQ9bEL_17F-DKsEgx6b-qJ2pPWnrAe94Ibxhbp1O2L3BmkBVh2vBVlLfPwRW0dVpxao8L5nitI-kH8bt-j8lX2yVRuuIXNVPCUE2QKs_FLfgPLA0CyFKoqKaJCe_MEJIlvo3M-qcBbzB-PrVtJVZtzBso3O6UMabbOr0iLORlaTFUkljmicJpQ8okuxww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید گوچی فلیم و کاگان به اسم «هالیوودی» منتشر شد.
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/funhiphop/84415" target="_blank">📅 20:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84414">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ti9uP5_BrCXGxzMrb8byHsjkLh61KYpE0zTiYvM4-IfUe50adjxnofT2oGWdcmZebRPeybFW0v2VpZahTh7SOWYDJiwDeFBh2tfqZv4BghXyMHLEDLwmiF14FL2iyNT7z-XsJs4QQAL0RrmCqfFyMM0bgZy_Rympvq6kgkBU6rxb1fVPdOCYQOSygOMYWGiV3XKpSJobpKi6l4Hr_Mr4j1a8RpjZ-d87qiiGVMq4DpBaGmBIk38-taH2ZgQkQ-kkL7Juk7XkkpGZFGjhDjzMs4v4FNXsTXJJDh9pZOMLMYJrQOf-UZu34t1zxPfE9FgmP3XsUknUa6WE1WkQkrwgQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G12
🅰
🛒
ورود به سایت
👇
✅
https://vsdgyfcdosko.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/funhiphop/84414" target="_blank">📅 20:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84411">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbMhFCtArXY_qHrNE8YtPivllAWNyVEB5ZxKetk4iPuNikLED1bhGRy-BJJSGg6Rw9YKKhs7MdpdhyI4t30yUQSs47IQTFRw9QTmHpZ8jlUVbeAoHT3TSL6LTQRwwWO8P9N2tEXm7yne-UKVEXKCYn2XFjUbOa5bGFIl1WkpNb9XBrMYTU_EPX10qtd3mvcJkYVVCUca4FzA5GGnaKtwQyCHJ13ePIIzJQmUG1IiC3R3TVojA5yEKFzZaTxKJRA0aGe-7vPaZe02luBiJOecBWWKptiFCVfFAV3MYTuotatbEP1hZedAWvvHbzy7wHLc77w_qiKV4hW2c3fRfdC-8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاد کلیپ های دوران بچگی میوفتم توش میگفتن من از اینده اومدم و ماشین ها پرواز میکنن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/funhiphop/84411" target="_blank">📅 19:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84410">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تهشم داداشم جوکویچ پیر سگ مچ زورف رو‌ خوابوند</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/funhiphop/84410" target="_blank">📅 17:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84409">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دلو از دیس به دکی پرایم رسیده به دیس ریری</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/funhiphop/84409" target="_blank">📅 17:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84408">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دلو از دیس به دکی پرایم رسیده به دیس ریری</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/funhiphop/84408" target="_blank">📅 17:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84407">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqfdUHeNE8l6ydPDwQ4jH63nxpZKzvJdZ7pVD2Eyhb5q_vCBaLRp7u7yhEkLRha2_f_FvMSzvABzDlMtBPEezB7y6lmPE8pBreitZIQnHp8kmU1s0C4-w26wXOK6swk5Epjefou2n9SNelAEUMPWt7v21hqDSdjnGM-65G7pbOYNah5sa8brJ3wAOBiIqUZzApZVVYHV4XvVP3w_IIMBlspBU1w8Q6zx5ah3Zlc4uZa9na3-cWeZbd_WOFzFHDvcLr4xLHBPISjBlRGATC04pogD-U9whBkNrhk8AoTYWDu00AwbN95W5ijdYwYZXdBjOX7MVO3TICVu1pLKhDVXKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دلو به نام "هاها" ریلیز شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/funhiphop/84407" target="_blank">📅 17:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84406">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2c0ed177.mp4?token=YJ-zhvNL2IFPBZj7YwoLq23SKsNqPEDdOzCLp81j5EktrKq4Ccv_g0xiqlQwPhx1ar7QovlZB9IMVQxNfJHVzCFHih35Es78l0Iuo2Yw5tR9eF10jWUyf-FSzRaJVdXklK0un3bNZxy2AGRf2tSFgW__OcJvZgGHyNJEI3COsvY3SgK9UiZSkvkN5OEbsPMLOWra3DTmUxz-_BNxUNWH7h4Hh6G6eqzcctWkoJGWNyACz4cbJWQ0cOO70nKsdfVXuva_yvPmoAlDkKwIr-LizK_lRQW0Z305iCN3chb2uZW7VcNZN6HMi3ILW5BoDS1CUswFAS4FkiwgPRo7HlcKjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2c0ed177.mp4?token=YJ-zhvNL2IFPBZj7YwoLq23SKsNqPEDdOzCLp81j5EktrKq4Ccv_g0xiqlQwPhx1ar7QovlZB9IMVQxNfJHVzCFHih35Es78l0Iuo2Yw5tR9eF10jWUyf-FSzRaJVdXklK0un3bNZxy2AGRf2tSFgW__OcJvZgGHyNJEI3COsvY3SgK9UiZSkvkN5OEbsPMLOWra3DTmUxz-_BNxUNWH7h4Hh6G6eqzcctWkoJGWNyACz4cbJWQ0cOO70nKsdfVXuva_yvPmoAlDkKwIr-LizK_lRQW0Z305iCN3chb2uZW7VcNZN6HMi3ILW5BoDS1CUswFAS4FkiwgPRo7HlcKjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عالی بودی حاج اقا
یه آخوند یه ایده به سرش رسیده که رزمندگان رو به موشک ببندیم و در اسرائیل هلی‌ برن کنیم.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/funhiphop/84406" target="_blank">📅 17:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84405">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuzY3A6xmNdV6DQ73afOSKwlYSfxOl3pNejFX-w3QuDxICqqdBLZxUI7UP5eRXZcFUpMwdTKzDmv8mm7Y9thXrT9aHO4EyhzXAh-Qdp-0LWBCCc1B_LobCcE4xrxw1tZ8y71YJMQ00wA0wFAKtyvJsPvMhDfxCiPPhd6rPPrWwI0k8sE0tyokgat4FmdS3e9orp37Kg4TAb_uqUQrtpFo4LwlZ3L74ABG8L5WG622qs248K2y1fRhWigbUbZphsHJZDAqBKAGZbtAYmMjkAfwH9UZE2aoQh8PFVlP5j7plbUciPhSXUo1U-9SHD5Pbr9rr0cHI0WPAx-EKgT7jhNIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کل زحمتامون بگا رفت، تازه تو ویدیو هم میگه امیرمحمد افتخار ایران
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/84405" target="_blank">📅 16:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84404">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3ab332668.mp4?token=ECSx5KwJWdTVquU0KQup8j32OhJ0gIF3HCyTQELw5QEPUkpFEGJtM0bCF-TRV4JsLTvZdBa4bGXH56egZBvvZDDknuaVSUpmRVSvo85INytiv1sEyxX2LXkAYuWMYb3O_dQHWl3106pW9BGH7WZN2mH6K-uMWm-w7TUrBNNfr1vZTeNd2HNLOdBFMS4v4LLxc61y5M11CpOdontu3iAFLIaA8meV0vk4MMXiJXArZHPjr1GTrAIxa-3DwThux0Zy1vNQbENcmLHIOt7lspc1yEpGGR6ochcqrDrvG1f-EpBI7p0J4lCsMpxfQxrLOJT2-TQPNbgPPjnftD60LbyhbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3ab332668.mp4?token=ECSx5KwJWdTVquU0KQup8j32OhJ0gIF3HCyTQELw5QEPUkpFEGJtM0bCF-TRV4JsLTvZdBa4bGXH56egZBvvZDDknuaVSUpmRVSvo85INytiv1sEyxX2LXkAYuWMYb3O_dQHWl3106pW9BGH7WZN2mH6K-uMWm-w7TUrBNNfr1vZTeNd2HNLOdBFMS4v4LLxc61y5M11CpOdontu3iAFLIaA8meV0vk4MMXiJXArZHPjr1GTrAIxa-3DwThux0Zy1vNQbENcmLHIOt7lspc1yEpGGR6ochcqrDrvG1f-EpBI7p0J4lCsMpxfQxrLOJT2-TQPNbgPPjnftD60LbyhbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بچه ها شاهکار
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/84404" target="_blank">📅 16:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84403">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42b7e86ab7.mp4?token=Zx5xwCHgG9pCvcUY6gUIHJITF0w4P0fdJkub_mVld5MaZAqPNLAtAV7vAy3v_-gQ2iUvOrEpKqAg5PAdFtX-lSYkEAaS42sMoIarx6ZYm7dv1wjs3xFa_IKVummuumb7nztWSLeEVQUCEiUXfSYtkeA9-VfPyvU1uDg-w2ctdzKLbJLbQaFYn6lK8xUrLgr5h6TiLqM5WMfNW_UV7S5RU_hANjKsOI0_XPb76moc3Pum1s9mf2aS_T7dFKm8L8GlHUpBcMNvJPrhvIFUgALFB6nm_4dACWeV6c7wMlH1W5-898B1gIWoStheMNaP_9Z_ButQ-8NhfxfJMmwMo9FHWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42b7e86ab7.mp4?token=Zx5xwCHgG9pCvcUY6gUIHJITF0w4P0fdJkub_mVld5MaZAqPNLAtAV7vAy3v_-gQ2iUvOrEpKqAg5PAdFtX-lSYkEAaS42sMoIarx6ZYm7dv1wjs3xFa_IKVummuumb7nztWSLeEVQUCEiUXfSYtkeA9-VfPyvU1uDg-w2ctdzKLbJLbQaFYn6lK8xUrLgr5h6TiLqM5WMfNW_UV7S5RU_hANjKsOI0_XPb76moc3Pum1s9mf2aS_T7dFKm8L8GlHUpBcMNvJPrhvIFUgALFB6nm_4dACWeV6c7wMlH1W5-898B1gIWoStheMNaP_9Z_ButQ-8NhfxfJMmwMo9FHWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هواشناسی یه بالن فرستاده هوا یه سری نگهبان معدن فکر کردن پهپاد آمریکاییه با برنو زدنش.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/84403" target="_blank">📅 14:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84402">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3FeGyi_AhR9xdC1slgN6rqNG7IT-byXZw4-XCI2F84Ipg8t4QvIWMOFmh2KkMJqRzG77ppw_frZqTFPAvOdJLXpRRf_bUXq6c4tm4KNvJrp5yMmqkrVH_GjjcJKRYG4Ev1CDjp4ulR_7G0Zsd3Mf4dLA4OdYL7g0janSzcQPk6ImyW5IbmDaBbMcmpTZT_jUNQWFymyMb82AV4dfis-qr56J-39dIxAnxK4a6HLmwdY-VUiyBeJQIr1lihqNQ1YZ_uKsAQycDaN6x_z7Bw90GnOjHGAaCVIia3b7Q_E3O0StpGFW3hjgsaAd3kgavFXxukGmsaN8mcmdIR5-RUj7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زندگی تو ایران هروز شوکه ات میکنه...
دو خواهرزاده، نسل دایی ‌شون رو منقرض کردن!
چند روز پیش تو خیابون آتشکده اصفهان، یه مرد میره به طبقه بالایی‌شون که خواهرش اونجا بود، میگه صدای سگ‌ تون ما رو اذیت می‌کنه.
ولی اونجا اوضاع بد پیش می‌ره و دو خواهرزاده (متین 29 ساله و مرتضی 35 ساله)، داییِ خودشون رو با چاقو زخمی میکنن.
دایی چند روز بعد میره ازشون شکایت میکنه و این دونفر هم به بهونه گرفتنِ رضایت، وارد خونه دایی‌شون میشن و اونجا انقدر بهش چاقو میزنن که کارشو تموم میکنن.
تو همون حین، زن‌دایی به همراه دو بچه‌اش (پرسان 6 ساله و پرهام 12 ساله) از راه میرسن، این دو جانی، زن‌دایی رو خفه میکنن و اون دوتا بچه رو هم با چاقو، می‌کُشن!
در ادامه هر چهار جنازه رو به بالا پشت‌بوم‌ می‌برن و سعی میکنن با ریختنِ آهک، این داستان رو مخفی کنن ولی نهایتا پلیس متوجه میشه و دستگیرشون میکنه
.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/84402" target="_blank">📅 14:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84401">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">قیاسی سهیل پرنک رو دعوت کرده برنامه اش، سهیلم با همسرش رفته، اونجا گفتن باید یه اسکارفی چیزی بندازه رو سرش بعنوان حجاب، سهیلم قبول نکرده و نذاشته برنامه رو ضبط کنن و زده بیرون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/84401" target="_blank">📅 13:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84400">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">Winter Is Coming
بابک زنجانی: زمستان سخت در راهه، اما برای ایران، احتمالا یخ بزنیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/84400" target="_blank">📅 13:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84398">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhUHP-iNtJK6cSOCXOSp3cXt2utMzVPdQFRHkdyXRobCcg1xjmXz-7MWIuhwKJ_1fSbOSGpe-imPgvi66iMZTCigEnXUzRDz5UWf4535GBRicMe3fcAkjbI5bzwdSa0wV-igDjSarh7KsEP7oxkR8q8lSqurzBh3a0YPT-LfllG6PddZDdtQZKnPuuhdWw_P-p2i6hXwOdXWXI1dwx0e25PicNnxDDHZMkB_Wtcz762eFuzvmqpA9F5cA0_36Ug7IxhRSaRowrTfLHclV0-iT4swrJw4qaWX0FLr2plG0ZB_5aTIvKB4Lp1nuyeBvKHiKLy5wzv0b9cGWYGxx2vYMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظهرت بخیر ایرانی
-دلار:۲۷۲
-طلا: ۲۶۶۰۰
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/84398" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84397">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ba4e1d6062.mp4?token=jdPRoSaMLEbK54xI45YwgqAeaxWlZqoJe9awufaXFK8j4ilUy1losXiwtC9rc9COcO0IqySazhlfhzLqDQZJ7TiLHQBETOm-qKsCtREva4aQohjTYyQHDErlbJWx63nk9NE4a91oIa2CRaM_4dehv5-xVi5s6e4gNj7HMReu-4NB-XEQc3n2TF_qyjVjao5T05wharAUMpZBKB2oxgeVRt-hwyz9ygb-JNGOkXtrJiSWCpBi7jb71DgDDyg0D94tqtSfUV9KXdNUEpXbtRb-PXJKxrJRHI-teARauMY8HkovPCwxWh4FAFv3WqClODm2EPuhJ4LIwjeJgWqHoXFV5g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ba4e1d6062.mp4?token=jdPRoSaMLEbK54xI45YwgqAeaxWlZqoJe9awufaXFK8j4ilUy1losXiwtC9rc9COcO0IqySazhlfhzLqDQZJ7TiLHQBETOm-qKsCtREva4aQohjTYyQHDErlbJWx63nk9NE4a91oIa2CRaM_4dehv5-xVi5s6e4gNj7HMReu-4NB-XEQc3n2TF_qyjVjao5T05wharAUMpZBKB2oxgeVRt-hwyz9ygb-JNGOkXtrJiSWCpBi7jb71DgDDyg0D94tqtSfUV9KXdNUEpXbtRb-PXJKxrJRHI-teARauMY8HkovPCwxWh4FAFv3WqClODm2EPuhJ4LIwjeJgWqHoXFV5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/84397" target="_blank">📅 12:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84396">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFVahtAJByTNjGfWzaWtve9dh4Oczu4kAMcdUcas4WA_mRp379cNF_38MTgyDvhU1GllBYY885yeyh2OgGVZuAWBsJ4wKQDNCuAyst5gCHv-vgLlqMvRrw1dK6aXAYBLgMaBEwvgq1MMDamgd7HhOs29GpSAzsr61XsgNsZD9Da9K7-GKhdYTg9Q1Nxgf6HvICqoW7eoH6Z87t8Ps0ZKXG24hmYlsrL3SyC4beBMygzJhhw8Z6i5q4wHe_mNjs_0RwUmNR68AwyAm9m497ScfCfDAAeKG8UzhSXWI2pjA1af-jf1AsSY0pUkm19ClNh29Y2VjjmbDnLTtPE28RHIOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا: یک نفتکش در داخل تنگه هرمز هدف یک پرتابه ناشناس قرار گرفته و موتورخانه آن آسیب دیده است.
روزمون دراماتیک شروع شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/84396" target="_blank">📅 12:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84395">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8EsyRbUuENhBLQUD3oVVI9EcH2iVnTsxLETWCNpl-Wn5fEwK8GPjxVlVHa1zLlovhgjQXA_3G6bLQRPp_YNAoifgFzVwVIaFFTbJ8-dc22xIa6Lk11D4e-iKIhXoC5jAC4xcIxy2FG9powrFQlNXEpWs2x7rRnXMVyzxuw9Y6b8KoOzalItxIF5Gmvr2WeqLFHsD3jjnA8-PQvBByxWTB1Rcg39sHBAEJ251_Aq3zfE7_aBFhA72Sa20SZyFBCFIeQcALHvbpOIVg2vM5SsOUNOye1NffGN4KzTDlIir8IHhZIieByvSwKZpAFICHpv7QTxVNvGNduJclg9YQeouQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشین جدید ایرانخودرو به نام 207 elite
قراره از این به بعد اینو فرو کنن به ملت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/84395" target="_blank">📅 11:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84394">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⚽️
مسابقات ورزشی را با بری بت پیشبینی کنید
⚽️</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/84394" target="_blank">📅 11:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84393">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJ0JkFmocF7qIiE4JHWLp7DPU96h6l7QAImVEnw3GOhMon1p6J7tiq3sshvefva224PdBTqZUJstyupLc8Pvb5K_V5ns1s07yRerAwzNM8jDpq-6vcWrzBP6wDv64edKBtwDQSlinb_hwr_IKn0OlH5vJfL02Eul9bPFJmX3uup7AsEHrc0RiHb3cRMdV1afOT3VHrulmkq766feP9Tje5iCUPBE_oMoKUGbNJvxR8bZrDiwPB5-UReONtN_nZL8Kraj063dxL4siJRhjGNXsBfOd_uVxI_qnYM8ci3hYoEhQyhm25FKvZ9FAo32MKp93HYE-TqcaJaNPUAH8TJcJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
فرانسه - بلژیک
⏰
ساعت ۲۲:۱۵
🌎
📲
رومانی - سوئد
😀
ساعت ۲۲:۱۵
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R12
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://vsdgyfcdosko.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/84393" target="_blank">📅 11:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84392">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0466e7e7a9.mp4?token=Vx-5c8ZaPrltyC6x0qvPEFyyyryliy3enhMspD26EPz590263CROqCz82yXj9vHVNInsRd71ZfLqczynkSMywJLlpKjpdQkNBQvxqnYZ4jqBow-N1WmZmjxplde7WFQd8mDgQJwucMojScCk_cyunxJitTPxeaQh42rdyBvFqQKkYfbqHkJE1d3WFiv-Xgay6TCnjuOPmrKbFtKUWkmdt0vTtgXi0Rkg4ZHQHNuE_2aqYnKYnEVC1nfJ8yu49u2pKMVUmWGaxNFEN3lTxotAxcI3WjAHoGOmTKY2gMdQvJOOHRwQnWle_E5TJGOzioD0e1SfBEpu-MVEUkg3EW3BnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0466e7e7a9.mp4?token=Vx-5c8ZaPrltyC6x0qvPEFyyyryliy3enhMspD26EPz590263CROqCz82yXj9vHVNInsRd71ZfLqczynkSMywJLlpKjpdQkNBQvxqnYZ4jqBow-N1WmZmjxplde7WFQd8mDgQJwucMojScCk_cyunxJitTPxeaQh42rdyBvFqQKkYfbqHkJE1d3WFiv-Xgay6TCnjuOPmrKbFtKUWkmdt0vTtgXi0Rkg4ZHQHNuE_2aqYnKYnEVC1nfJ8yu49u2pKMVUmWGaxNFEN3lTxotAxcI3WjAHoGOmTKY2gMdQvJOOHRwQnWle_E5TJGOzioD0e1SfBEpu-MVEUkg3EW3BnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتش سوزی در پاساژ خلیج فارس عسلویه
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/84392" target="_blank">📅 11:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84389">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پاشید برید مدرسه بدبختا</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84389" target="_blank">📅 06:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84388">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSVWO2NLXTE8QtVGmnFye6FxdCSd1HQMM69Q_mHbIMmOuRxZ_aMYxsxPbUJKZ2h8FA9Tr6e-Ghd5_A_3f17sJrGkCXWHGeQ-qvimqh3A8AFL9HvxmFqGpwqFk6p5ygfGAOwNFhy4IUWUOxwxHYqkvOW4hWrg125GSRWADF5FHwbwMmZL7_CX8tFUb70ac5HVPnwIZUi2L8uoH_JjlH9XclWPz4da36gGhZuY2hO5qJW2bMJVkOcpZo40jDQ1g5LBpXOm_pe751af0Z3JweFbv90vy9UAGCvFWxEQox6tp7wVRQCcSCi3NjHZsN2sSSA7_JF1EDnPDFMU4GFUHchhlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۷ دقیقه نگاه کردم اخرشم نبوسید
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84388" target="_blank">📅 02:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84387">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFshw4bhdZ7bZQek6Sbp258WF2maY0IgcN6hmMkwP22H1HPNXLD_QBHp1YbdtAMtVzrzac5h63osYaJUwtqsKurMJQLct3RgXdukBPhVX7AA_1oqYDSy_5bTX-bAkRt6zTiGpozLpP4vf5vv5MxFoMEz7QzvfFdTLdSqqJH0ewoJfk3n4KbauhtK0BpOc_zzDngPN40GpN48_vUa97nRjSbiSwZ9cWyz25A6xP0mK6-pcr2dCQ6NB1WUs5EyJHPtcPuRrB0SAdp7DSPhYacGJYJA9m7zQL-uJyY1djXmSCrwyNcMQ1-CEqvMKE8UvOojfmm4u51BcmTa8895WZRPqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای پوریا عرب نامبر وان یوتیوب فارسی
🔥
@Funhiphop | Nima</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84387" target="_blank">📅 01:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84386">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/979e96f7d2.mp4?token=IrjN7_sow9saThdSKQPqIqBhYq6Js2H3eYrAcOLO1ME7qfB5GV-W2gct_ihDusvjmtpzaSGCEuEB-GRWVF2X-w8NKnOHEgq7FIH4HKAY2KllzCa1Mnn4skI16-QRiO11F5Qi0YgI3Ciwe8PaZTu9TWwsEKlzgSl_OxLrkjczFBdP1lVkgriCJTHlbuc41orqQEYpQhxSjamf1bOmVsiCXu175dhA64l2KzdAhWMCRsqAM_UDZOqZs4zhc_fVAycTgOxN72iim6qa0Zry75szyWYJmsVvHzPLGdZsJX6SyzT-8zsFueRdOscLiigliBQwSFZ14GpbNsPpONnaQMh3jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/979e96f7d2.mp4?token=IrjN7_sow9saThdSKQPqIqBhYq6Js2H3eYrAcOLO1ME7qfB5GV-W2gct_ihDusvjmtpzaSGCEuEB-GRWVF2X-w8NKnOHEgq7FIH4HKAY2KllzCa1Mnn4skI16-QRiO11F5Qi0YgI3Ciwe8PaZTu9TWwsEKlzgSl_OxLrkjczFBdP1lVkgriCJTHlbuc41orqQEYpQhxSjamf1bOmVsiCXu175dhA64l2KzdAhWMCRsqAM_UDZOqZs4zhc_fVAycTgOxN72iim6qa0Zry75szyWYJmsVvHzPLGdZsJX6SyzT-8zsFueRdOscLiigliBQwSFZ14GpbNsPpONnaQMh3jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رعد و برق خورد به نوک برج میلاد
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84386" target="_blank">📅 00:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84385">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پزشکیان: نوک قله ایم و نزاشتیم فشار اقتصادی رو مردم حس بشه
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84385" target="_blank">📅 23:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84384">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fc135904e.mp4?token=gVtsQVI7Ylv9Lh046Vc0U1pRYykec6ehKbm3Gahv4A6BZzwLkT_rf4QIudK9Vah-1mwJIZ-sACD7I8-2pKMohWuIadPKp4Qh8_GSRgAgNgtNwdwEKrsXgA3DJ_uo9F1UYLaQ7Dswcb059-Rs5FWyyhxdWPEcQ1Na4Ts1eZksgqA_ebMHt-QhjIicTUiYwDsVCclwYTAOYm7L_ZHUtotFaecFEfuuyNox27YeT8kCSZ7rfIRM31n_GryZnktM72h48jOypk69nZb8KCSyicq_S3jL3lz7Uo08Ra_oHMNzCBzoEMcy389fOkkNpDWnIrh04o2Wt3jO3OhdTOKkqkGtlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fc135904e.mp4?token=gVtsQVI7Ylv9Lh046Vc0U1pRYykec6ehKbm3Gahv4A6BZzwLkT_rf4QIudK9Vah-1mwJIZ-sACD7I8-2pKMohWuIadPKp4Qh8_GSRgAgNgtNwdwEKrsXgA3DJ_uo9F1UYLaQ7Dswcb059-Rs5FWyyhxdWPEcQ1Na4Ts1eZksgqA_ebMHt-QhjIicTUiYwDsVCclwYTAOYm7L_ZHUtotFaecFEfuuyNox27YeT8kCSZ7rfIRM31n_GryZnktM72h48jOypk69nZb8KCSyicq_S3jL3lz7Uo08Ra_oHMNzCBzoEMcy389fOkkNpDWnIrh04o2Wt3jO3OhdTOKkqkGtlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همسر بیژن‌ مرتضوی: به جای نفرت‌پراکنی بیاید کمک کنید ما بتونیم از پس عکس گرفتنای مردم بر بیایم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84384" target="_blank">📅 23:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84383">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">توپ طلارو واس یامال اماده کنید</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84383" target="_blank">📅 22:23 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84382">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گورودن با اینا حرف بزن نزنن بعدیو</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84382" target="_blank">📅 21:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84381">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHDnjLuDlOa570bJYpT2uMk_5mVEo0fB3Ywun0hjQK3MFJX8POImOPBnZvHpW0KB-8WpZMnrZvMaYSbQrsCLTBtObLF8UMQUAlNgfuzweP5G-D1E7DVDnEPr7229JZ-seCQuKiKkYirssU1rHQ3kFt9KD1yDTkgBF56ZHmRnyqH5Aq3VDVHsXCUCQShPeoehmGBstG1f1R-6uvC-h2AJKF3gYhvAwtOAsAT0zA2ZSVh9OgMyhJND3-vw8BTKaR1Mzz5lfe4pXpB-NsacpQhkiTYNf4ASIG-L68Hihht6rH8N0ocJwQGcpyvX_XpwnEEUsCrofQBmdEi0-54gur0dSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته های سردر اتاق رتبه ۱۳ کنکور ریاضی ۱۴۰۵: دوست دخترم مادر شد من هنوز کنکوریم.
پ.ن: بیت بالایی شو هم کونم نمیکشه ترجمه کنم تورکای عزیز تو کامنتا خودتون کارشو انحام بدید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/84381" target="_blank">📅 20:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84380">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بلینگهام داداش لوییز انریکه رو میشناسی؟</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84380" target="_blank">📅 20:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84379">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUD3lD2mv9FEGl7_8ku3ikNFDGy7y8IJa-OAfcXCb1xd16O1gojFLFiLcktgbxO5kHHnBe47OEjii00nH9smiiKklGVQGxow4OyHt7IRbiO3BEqgU9wv-7oNHYQ3d5FLOQO7HN7b2KqU93LWRqvvZclyGyiCJq4gPrtSekxqtWKfwpfnaoKFe91UR8wedinMPxvddUb578SqSS9PgN66jH1p-EiSWpQgKSOT09OH_TOp37WndRSjjq4zLWuSJ8gCACc7tkTViSAYSKhA40M54cW6wXxhqe1Zb6jW_idhC05tLZN8rTE_S8IZlxIqGO-x1bNLyfJxFz822YEXYtZvFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واس بقیه دوستانی که رتبه هاشون رو کنتور بندازه به یه کشور بدهکار میشن  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84379" target="_blank">📅 20:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84378">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترکوندی شیر
به دستور بانک مرکزی، نمایش نمودار قیمت تتر در صرافی‌ها متوقف شد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84378" target="_blank">📅 19:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84377">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6db6ea36f.mp4?token=NtDmR8Mmfd28O63GnzPgOC_Y5_5Ei9J6iPOkLs16RxxC8l2pnWPZdRlxybYRD6totFohgC4E31BREM-Jbnoy4hQyvMLzbWl2neHXXAsUFdrFgt35MKmsmb61UfnHJz9t3KUTMzo9VKizCDakefEaniS8mS-DhLjgKVcrGREJRZTn6EbweaDLD3YFWW9l2Z_yjzjBcrM3w2tgvbn5vUcwPQeMsWRgX-wSp7yKKQWCQ016LHAL30tAyvt7Z4Uhtem_RPm-LwV04RB7Llinp1l4pTg6d3R3KFPQ7CbmD8tQQJ4d9nViDbn9vvhelsY4Ub2ib_d3kcnAV-uie0ZlA7LyZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6db6ea36f.mp4?token=NtDmR8Mmfd28O63GnzPgOC_Y5_5Ei9J6iPOkLs16RxxC8l2pnWPZdRlxybYRD6totFohgC4E31BREM-Jbnoy4hQyvMLzbWl2neHXXAsUFdrFgt35MKmsmb61UfnHJz9t3KUTMzo9VKizCDakefEaniS8mS-DhLjgKVcrGREJRZTn6EbweaDLD3YFWW9l2Z_yjzjBcrM3w2tgvbn5vUcwPQeMsWRgX-wSp7yKKQWCQ016LHAL30tAyvt7Z4Uhtem_RPm-LwV04RB7Llinp1l4pTg6d3R3KFPQ7CbmD8tQQJ4d9nViDbn9vvhelsY4Ub2ib_d3kcnAV-uie0ZlA7LyZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این چرا هرچی خز بازی در میاره بازم جذابه، خسته شو دیگه کصکش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84377" target="_blank">📅 19:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84376">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حالا سریع و خشن هیچی، باز خداروشکر از دوره ای که ملت با سری فیلمای یوری بویکا فاز میگرفتن رد شدیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84376" target="_blank">📅 18:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84375">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jppV-dHx-vRol8m3PHNZFOSvL6_n_QqbrTgIM4Vs7OJB8eDSW4tDN3V1M2qRzg8MULVPnhu5J8KJ72rPPYLbPJu0A3EQ3_x9ti2vL_0RUfq1oPFBsH1lz70QL73ZGNjo-nIZ0v2Ku0pQ5L1c_hpWCXi-o-Orkm9spAIW6TOLvM1F1i0VGQvAys8SQlXJCEUAD6kdNOdnTdrI_VWAQ3AbcpLJ-oC6Y7WreT9hH7T9wBWEKMosNVAQ1l5kgPd-q2pE9lnq4EfiDH10mQb42UmnD8lO5OGobQnf2ysLrEmXEY857W3SqwpRKaJngUFafQ08NNeT9etUS2sw4KzR45jQCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته شید ناموسا
سریال سریع و خشن در دست ساخته و ۲۰۲۸ منتشر میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84375" target="_blank">📅 18:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84374">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaeea73ec1.mp4?token=DpeGIUPCIsEgQJuMJmmUNGAjaCuiIvaktdH5IrWC6eEr1O9UDc_CBQeG_I2XpB-iM4h7gOmBN4KNtAyImvy4I4J-K1G7NS3Oqly-onjKeUuT0P4WFUesxaOEzOk05h6EHQxMTapZyCUl_RnXAw7ZEUyDq1-JJgTwXnfFZGZNssW4f43t6_Dce6Sq1JoK8xWrW5lzhtf5qmcOftMW8znVmyU5EurceazPQ0pUs-c3LIYLM77xsvqeZ5asuM6nokHMSFi8yqz7VTicmAH2Y9Kq9BQB3MLXJ_FuiNJem3nxsNy6NMG4YM47fMLMZbkkA-bd8n3xrgFAHpgYIyEA16V0QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaeea73ec1.mp4?token=DpeGIUPCIsEgQJuMJmmUNGAjaCuiIvaktdH5IrWC6eEr1O9UDc_CBQeG_I2XpB-iM4h7gOmBN4KNtAyImvy4I4J-K1G7NS3Oqly-onjKeUuT0P4WFUesxaOEzOk05h6EHQxMTapZyCUl_RnXAw7ZEUyDq1-JJgTwXnfFZGZNssW4f43t6_Dce6Sq1JoK8xWrW5lzhtf5qmcOftMW8znVmyU5EurceazPQ0pUs-c3LIYLM77xsvqeZ5asuM6nokHMSFi8yqz7VTicmAH2Y9Kq9BQB3MLXJ_FuiNJem3nxsNy6NMG4YM47fMLMZbkkA-bd8n3xrgFAHpgYIyEA16V0QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دست این پیجای ادیت اینستاگرام
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84374" target="_blank">📅 18:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84373">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">روسیه: به زودی میزنیم پایتخت اوکراین رو کص باز میکنیم(
چند ساله میخوان این کارو بکنن
)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/84373" target="_blank">📅 18:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84372">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DB05R2roulBCWJmVeoOXdrRu-ptyJbLSVE2hizDnKCtJ7C4_vwCAFLGfIHpYbfu9gnPaJCHQXt21nH3Yxl9FzbMtUMoK_0W3BdYN-zHxZDEaM5hZJO29QQz96exlEnvg-58byxidal70H_OGwGk1tP7D2uoYQ8K4cYsMk6v7gd6h-p-Hyl6PL-IkbOuCe4R29K_h8DNxFjCeou8ZITcEbDA0fVyWeVnuBchJDJaAZrfhw6EJ1WxKva0rcrtNHRP2JaeIucF-2x54ZPTYTZd0kdKJQpyG2twM_eKJg4IW0QBiABn9Hc9iPaVAq4Wcua6IrG7XtVNVudUOPsjmecLAtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقیقا منم با این تصویر موافقم، به نظرم قاف باید برگرده به خیابونای تهران یکم جنس اعلا بفروشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84372" target="_blank">📅 18:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84369">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">عجب هواییه پسر، امیدوارم عشقتون تو این هوا بهتون زنگ بزنه بگه ما به درد هم نمیخوریم خدافظ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84369" target="_blank">📅 17:58 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84368">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgPmT3mMdPef_ibgOqiWCRcynr_2h0-IRhE6EdrhgoXo-Uzw0mYy9tvemOY20px5G-y4edumAVyW2znrMmIxuJSw3lppnlZWPSUnUDWS2Etv-VwSu0TdIPNSAxeJfmGJeiMJ9azrS54k3lx73rU4_AAaM57yQDNwHkxM2liepKbv0UcHaZZAeHyayB6Yrdf3FYGOgCIbpO63YxwL5kHpQRRkzOo8Vz14do6wMz3SjkdPV3EyuBEAwMzgXPmtvUyi_6rYX3E8tdW_6I6KxRRgGZ7my7jGSdg4F5K5kGsCoyxqQV2VSYv9Vv_aO9Fkt_-DNtZxywMsfoVguNAAh8heUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سریال the gentlemen پیشنهاد میکنم ببینید فصل هم ۲ تازه اومده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84368" target="_blank">📅 17:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84367">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اگه مصاحبه فرهنگیان دعوت شدید همین الان بلاکشون کنید، بعدن میفهمید چرا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/84367" target="_blank">📅 17:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84366">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">این میمای کنکور چرا آپدیت نمیشه، هرسال موقع اعلام نتایج همین میم ها تکرار میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84366" target="_blank">📅 16:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84365">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دانشگاه سراسری تعویض لاستیک قطار فرار کن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84365" target="_blank">📅 16:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84364">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Joo9AK5ztPYOVW6uEy66g28zWWeUVsUvBdzAPHcmJhnUuLG-KitJb_MQNpEqyy7GACPDBxKgNlQkZvydmNxMY57aHdOvC8dZyWW0aaLe6jpOuJ4Q3Sxk7rU-gzyE6gwfj8OJlEcFgLVC0gZ7m8RwSlJkE3XWCBCt0uEhGl4JmAo63_aw32k69z_tC3PEXWKeYaybzyiqH8NwbfdUP1I6YvyE7mmiVAFg_nAQmiEKUMnP5oGmDbeyvDJ1lGYoCfVMuCPoIjXwvKChcuzN45vQGwg3PBjNBDrXPKHutk6kYILPNicTung_MUioTiRTIIpRxoYJGZ5a2uLYXNYy1euCcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانشگاه سراسری تعویض لاستیک قطار فرار کن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84364" target="_blank">📅 16:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84361">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQdHcvimiTq1IbWi64G4BYFetRm9D38_lNtfjEX_iZtagtLFUvD244FsmsEkjFdD-mFPPpgK9Di0Tn5uzB5MNsRSqQrQaKf-jLktbW_yoSUvIDgNl5AnVhu-pfqWcrAbYaUs2ad3UxDpeZAeyZpxNJX5PahDfcTkw15arbfxvWiMk8GdquOg76L7Cx1FpLsf8cZbNADD0okQkFerYulc2o3_KbmiRDpdYU_PXjxxJimFiWF-j4PZcIDiaUHx2d5R5oxGNKomA6ouPKOYOqbWUVbviWFf-cquqY2hiCSVuh3emlPZ3c1uDNWeHlHRY_pwBFIQkMmkoxcIUP7Spj1AyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واس بقیه دوستانی که رتبه هاشون رو کنتور بندازه به یه کشور بدهکار میشن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84361" target="_blank">📅 16:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84360">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTileKhersuk🐻</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CO-QHAn3Jm2THP43KwfA-ohm1o4BzWt-M4DvQT00cEomeoKgwzHstW9TTOBy7COTQ2dD29MAIZkWoggiocJ1SrCOvDcY7eSHcbQ18NzGpgJZEGiDwwqTD4R663Dn-OrOmpWLuFgbfHlAng2CWh24AoRl4p7mrdtAWXaDakqLZQ3PCBCqQURsd4DCG0GM1FH3wFJ8Wgj71cOklz37lj7tD8v8OJmB3LddtbY4xSipHryK0jY8VaYXMKdC3uiT4HMAaPB2vZiRzCcykHjxU82GYRjwhIcm5OhIZWiN4Xo1kbo5-xpLBKq8lj8ue-xwSTk3f6OVrvIW_L6v6dguYjl99w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر خوب</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84360" target="_blank">📅 16:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84359">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نتایج کنکور اومد
بفرستید ببینم چه تپه ای فتح کردید</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84359" target="_blank">📅 16:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84358">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">جردن های تولید اسلامشهر که مسخرشون میکردیم هم دیگه زیر ۴ تومن پیدا نمیشه، های کپی ها هم شده ۱۵ تومن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84358" target="_blank">📅 15:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84355">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بسنت اومد گفت تو دوماه آینده دلار ۳۰۰ هزار تومن میشه، همتی در جوابش گفت آمریکا هیچ گوهی نمیتونه بخوره
حالا دیگه خودتون حدس بزنید تونست بخوره یا نه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84355" target="_blank">📅 15:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84354">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دوستان استرستون برا کنکور رو درک نمیکنم
کنکور فقط قراره انتخاب کنه یه بی سواد بیکار باشید یا یه با سواد بیکار
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/84354" target="_blank">📅 14:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84353">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LJqsPp68bqq9CnFhwhQ9aLH6lhmPtdYsj9JMkaYg3lPh5MhrGzzMOX1y_LgXrPSHA1FveX-5FNgpo8yP0XhmZMuymHsUgWDuy744QjlSpvH4Earu8Xm2A6iNght0Hu5bh0aAIrrgkLl6B8JD5p5dT1C89g13Y4c8ImDodn3JGSkc57bg0mCJqyz_HsZH-AbDjSYJOuoIjJfNINun0Ymz-WxALci_phdfvLTJ5z8qgu3BEaoNZbt9dNjRL8m6_pvUnSDmC0ffy3P4ZstUVGLm6uT8T2NiMZHTQezmHJ15VwAQ6CkL7MgvQQWN6dbV6m371r-WgzNf1kyyRODPq-NDlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینترنشنال یه گزارش جنجالی منتشر کرده که میگه یه جاسوس موساد به اسم «مهدی نادری جهرمی» وارد دانشگاه امام صادق میشه.
بعد از یه مدت وارد سیستم حکومت میشه و انقد خودشو حامی حکومت نشون میده که بهش اعتماد میکنن و نفوذش بیشتر میشه.
انقد توی فسادهای حکومت و مالی دست پیدا می‌کنه که دیگه از موساد پول نمی‌گرفته و حتی بهشون کمک مالی هم می‌کرده!
حتی توی یه مورد به یکی از نمایندگان مجلس ۳۰۰ سکه رشوه داده!
طرف توی انفجار کارخونه موشکی ملارد، شنود فرمانده‌ های سپاه و نابودی برنامه‌ هسته‌ای دست داشته و در نهایت از ایران فرار کرده‌.
و یکی از مدیران اصلی برنامه معروف هفت هشتاد بوده.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/funhiphop/84353" target="_blank">📅 13:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84352">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">هروقت میرم اینستا میفهمم نسل چهاری ها بیشتر استعدادشون تو بلاگری بوده، شانسی رپر شدن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84352" target="_blank">📅 12:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84351">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نیگا ها و فلسطین فن ها فرانسه رو دارن بگا میدن
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84351" target="_blank">📅 11:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84350">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jG4Pw1LVcJU27U8sBkgkqIMMRohkLnn99_mZz2g1zYl4_pzpDbM61sF5GKI1iwrJBrbXynP_ML12Y_n1xiId0bWbT1RPPrSOiZI8QnfKag6Ryx83cap8x13mDSRlH4hvcKkD6EBm3F4Ygc0HU9zG7hJHKrMYY9F2ioD0Zw11S8aA5SfB05HUiIncsGlXM33oSM1DHH12bk3Z-ft2aeo7qNv_JBBbuM9h-hm21qmijJD-4iA7L7Of8vTbzdw0T-frHt3qr35C4VK5Q1yotoEmoLBiuHJzmi-wdjE2HbdHMHmMMWAztvHXeUq6eQ9eksfH2kphA5e0EgUDDy7SFJwE0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا کیرم تو این اکسپلور
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84350" target="_blank">📅 09:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84349">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c459c9f9.mp4?token=orOV2WhzXA1i2cr30wPLebpjyrVOo35X3ao7nrUn9yjqbnxErEy4o7xarl1GyqpJ-MuDqzduGKuQpM9ie1UErNdrRkx5Bbz0bgpfvCPtRbN5faOnbBxkSUTHFJ3IYqGdcTXlwqy-LNh3beNcsfoOKpOrPdYrI3Zp-Rznfc0znbdGghP5662ImOFpVCJbkYFWzudie30j6ACyau0PiOZkdb8H6wMDm6DGrrmf3iWuZTbEWKHuqL0tFx945J1siiNiEbogk270EUzTm3Vbb6ThJTICgGjFhTzwpuoKhMVYfE6nBDB5Mnq9-Co-9JqBNvaWvEKC9YwrvaLOc1afeWaeuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c459c9f9.mp4?token=orOV2WhzXA1i2cr30wPLebpjyrVOo35X3ao7nrUn9yjqbnxErEy4o7xarl1GyqpJ-MuDqzduGKuQpM9ie1UErNdrRkx5Bbz0bgpfvCPtRbN5faOnbBxkSUTHFJ3IYqGdcTXlwqy-LNh3beNcsfoOKpOrPdYrI3Zp-Rznfc0znbdGghP5662ImOFpVCJbkYFWzudie30j6ACyau0PiOZkdb8H6wMDm6DGrrmf3iWuZTbEWKHuqL0tFx945J1siiNiEbogk270EUzTm3Vbb6ThJTICgGjFhTzwpuoKhMVYfE6nBDB5Mnq9-Co-9JqBNvaWvEKC9YwrvaLOc1afeWaeuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش هایی از آموزشای جنگیری
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84349" target="_blank">📅 08:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84346">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8d924213c.mp4?token=ujJ-yCC61LwCjqq4YEJr4HUlZBj9GgGH50AV-XNAcfVQziqUH7eQzK-LzPTnilBQylLRuXqLf_fJfCJ-9Ecrb-C9h8WckReP2l8gqsz9Af2plolVrDMQ3tIcBo0-kWcs9nY8NPPJINGCBCrNVgSZEae6bcCdxmhFQrp3VYy42MZAHUkC8BSuWdIxjv2leSssKxrT6wxMsYbV-5GF6eWt4ZJUOK_Db7wNIrcMvbBesbUmuc--5u6zsp8gyLrrVgEWSZP83szvE9Kw1DPsfYH3zhyoKtj8YRVK_2ZBfL5W8XFuP5BDB88VbpDaOamnMPg76tccdyWlNzBPeonNjel6cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8d924213c.mp4?token=ujJ-yCC61LwCjqq4YEJr4HUlZBj9GgGH50AV-XNAcfVQziqUH7eQzK-LzPTnilBQylLRuXqLf_fJfCJ-9Ecrb-C9h8WckReP2l8gqsz9Af2plolVrDMQ3tIcBo0-kWcs9nY8NPPJINGCBCrNVgSZEae6bcCdxmhFQrp3VYy42MZAHUkC8BSuWdIxjv2leSssKxrT6wxMsYbV-5GF6eWt4ZJUOK_Db7wNIrcMvbBesbUmuc--5u6zsp8gyLrrVgEWSZP83szvE9Kw1DPsfYH3zhyoKtj8YRVK_2ZBfL5W8XFuP5BDB88VbpDaOamnMPg76tccdyWlNzBPeonNjel6cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روز خوش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84346" target="_blank">📅 08:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84345">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUr38jxC9BFF-zca3ywr4pS092nz1kfodqyu2RwAnbTobirV3DDcp9_IlcHWnz2EVPZX8McMqAr9K8YfsxA1iubniKpA_UXygwWNayT7aU9J0sQFvNMLLjUaHxlT4RUCIGrtolELz-Ih7l8UXRxRVs4FtAS-ltRMcv1KOfyYk4bp6xdq8C9cLC7L8cTdOlmNZHg7ONEyBtOgFhjPDOXhS52HK2g1YeWaAoq2fFEQxHLCIXkTN7snshKyDYtAt1A93VKV6jmk2iN85GAy5B4nBiA3phYSmI8z6UHZODC3vTuyYXSzcA8RphSaQ9nV1LTQ_iwr7AuoGtsTB8SSNuBixg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای پوریا عرب نامبر وان یوتیوب فارسی
🔥
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84345" target="_blank">📅 01:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84344">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgDqSHGT4U0ljRu4DV9gQXne46JFoQewN-WPC9wuL4Isor9bMVIr5B6VbYWoxJwO_QQptFQdi4Kh2CHczXbVHeCeAtTx6GstO9AgzvopR7-Bq14ElEkC96GQpSt9o9aXTNax74-Kd_EXQ8VD4B806Ucnd0ldCQuSGVEm-Q_Wof6qOuCevXO28RDhJ9bMrOaYE5Y1FbmTpRBPLBnTEkkgQKAqbU3-qC8Sup9y_RI7hz-tLeRFfIaeGh5DazFNM7OCWRszBQ4ybYgperiXKq_sYi2O8jwmKC2WUBTIhI3JO0pyn4fgprBQ0b04ebPPEnP9LfaAgvhGh1bzob-YsoJPvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Batman: Iran knight
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/84344" target="_blank">📅 22:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84343">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8a0a505ce.mp4?token=sATeLC058UlM31rKlBFofK4gjnEZNbA_Wddp9vJA1sbmKiu9YeLQJQUd3PZ021IiYhtnRovkkzNRnQGSBK_qgauULioGcL_K65o-TJ6-fjZ_SLrdwT4k9gMtD5g7iI2N0XW4Lgt7wfQTS5gh9JQgTa3FtB8idRKn76rHhRgWB0LWKPFeR7dtpHx6fep-yPiwHMZJxLsVEGo6hfDR92KjgQDAPFlR4V2VOSc_D8nQjoUyGB3UW5StSTddLPPZlItrmODFrpD4Q-R7uk6tdz_EfNxxJw3_kguqW54QYCa4-O39Xsd0YM8rnLJmmzERpEHAE76jU74cv0I57X7QWs4aQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8a0a505ce.mp4?token=sATeLC058UlM31rKlBFofK4gjnEZNbA_Wddp9vJA1sbmKiu9YeLQJQUd3PZ021IiYhtnRovkkzNRnQGSBK_qgauULioGcL_K65o-TJ6-fjZ_SLrdwT4k9gMtD5g7iI2N0XW4Lgt7wfQTS5gh9JQgTa3FtB8idRKn76rHhRgWB0LWKPFeR7dtpHx6fep-yPiwHMZJxLsVEGo6hfDR92KjgQDAPFlR4V2VOSc_D8nQjoUyGB3UW5StSTddLPPZlItrmODFrpD4Q-R7uk6tdz_EfNxxJw3_kguqW54QYCa4-O39Xsd0YM8rnLJmmzERpEHAE76jU74cv0I57X7QWs4aQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو کمتر دیده شده از رپرای رپفارسی که ریلز با مضمون پول رپه منتشر میکنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84343" target="_blank">📅 21:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84342">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UknBylqrIDy2xAdptYqig-3YNP9LdAOIMIZOGDwxHgZv4OsogeC5g8SPlxZKcpaZVpobvPjO_N1grfnkz3gswscbDSmN8TSR5WZbzL0dX86za8s9rxsKDMPYSRfsKV1kQNBdKSuL1CfDLAGTOkHfPuRResv2Xjop4YKFHehaKo6-BpYTMS9xir2cO1PLLdORkXpSYf4zECsbFdY6bLr5cS3CPNPLQ5CpSnkmzkUIs7pKHqlOf4iSDpX_dxX4ZDN5Jkhqn8qATZbPfDm_lqNN8ZtphN9k7310iu17CN-1zfHjHQqIg_z6K2FxfzGR-F3QLoEjzIrFLaYvXfeLAWyU9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#خلیج_فارس
جهانی شدیم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84342" target="_blank">📅 20:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84341">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">چه عجب آقا دانیال تصمیم گرفت بعد ۵ سال یه موزیک خوب بده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84341" target="_blank">📅 20:21 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84340">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترک جدید دانیال اصلی به نام "ADHD" منتشر شد   SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84340" target="_blank">📅 20:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84339">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Isu3EcfqpETs8Jjwxrp9JJ2VQkppe1D-btPTwFfD3R3P5dYU9t-WIfwgNMXiyswbgPVUpZ6UuyqtI2AKlfHWB-IITql5MOn3CpWaM0cBL-qdBn-DrdKEHjtdcY38FjVeP6d3MawAS_J3G6PSODAcZ7bIRJtv0r6uW-wrzq3joXlNdEhiSKKQhTnIB5oJc2lvEmXyUwQtJcijDiUr9U4PbZQBsLhr9uSXCdOVPz6POWSxzDI1UYUpZGWZDz-DshL5cHu61IiTDTAwQH5GLqIucVMn998YL67IYVoQeHZrSZsaq4LMpnavJQXXHHEG6aoKtKrt4_dRQewR75uphMbsZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دانیال اصلی به نام "ADHD" منتشر شد
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84339" target="_blank">📅 20:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84337">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MB7OQuKT9-qe6a8MJgVdVRXr-3GlKPwtXXrQpZydYmfeuXlJ5Kfej6DQbpaDEmuHcIZa-T-ci3xQWuJ0AN50yaa-xRT56VWIsJG1qSehzdw7SK8THo7xJOtC4RRntE9gqQljQi9GmDPHApn1QYjBCN3EeECjVtE5_LPZLjKG3c9ZHXt9D6ULWvr8TASAP6q6hyILRYgugW-NOpu6UqHsmkflGxX8t2scLSNUlYkD8V8LDzzFoJrrqpaslhAwgPo-3FNdC9VNwi7tOsB_LYRXXw_6qLh0QLGDkWsUOATtege1QdBpxbA7qBOnT2ugvimMVhE51ZiQ8wET2gTbsP5xZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e52f441c3b.mp4?token=H6Mayiw2pLdBFpy_RiMxT80_vF9HqTdOsT1B3GGYQ8zKvxaVkXnyC9yC2DS2vEtwgXnMGn8OM99jWgy_1_YT-R7jFQbLXqFgAhYQmYTqe9_YLeqRF1C74vLjgkZ8JqixoR3HsRTW_zSXL9oqFljTDJbBs_FRqiqhMW7ZWsQtHbufnuSE_sz_SSR3mn_XQceM46PbJHGpAdO3SzlsnXZVVvfDytnLVpDks_ctpVCrW3iE8vlLUcAjIWTOYcNqSPN0fGRkloPFDKoixwC_ixKXhfX1kd4hmiaCxnb-h4fd0L2HBQNiqLLI1pyNArix-bYjtFbKTdQYuppQ3XtKO0gfRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e52f441c3b.mp4?token=H6Mayiw2pLdBFpy_RiMxT80_vF9HqTdOsT1B3GGYQ8zKvxaVkXnyC9yC2DS2vEtwgXnMGn8OM99jWgy_1_YT-R7jFQbLXqFgAhYQmYTqe9_YLeqRF1C74vLjgkZ8JqixoR3HsRTW_zSXL9oqFljTDJbBs_FRqiqhMW7ZWsQtHbufnuSE_sz_SSR3mn_XQceM46PbJHGpAdO3SzlsnXZVVvfDytnLVpDks_ctpVCrW3iE8vlLUcAjIWTOYcNqSPN0fGRkloPFDKoixwC_ixKXhfX1kd4hmiaCxnb-h4fd0L2HBQNiqLLI1pyNArix-bYjtFbKTdQYuppQ3XtKO0gfRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بچه ها یاسو دیدید چقد متواضع و خاکیه؟
یاس:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84337" target="_blank">📅 20:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84336">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26448031d.mp4?token=A_WppNlKIZ-ysfJENCYzj0GRyrS_kf6Y-Pe3UdEzP0QD6eFXgUY2_00Bm0B4TS71Ce_D1DuB8JT_b5gT-xQu4flS4jP1N-TUQotd6H0n8bmkhmUSP1358MbMuz7UZ-N6ZMvTSy556NBIwPYhDH7eizxuqRMzNbasBSPJIhYLXmzmPrya-GQGa_DlaOAjyTsc8dfOg4NcLyBw_6bRn6aqL7xqIpaa_GdKBQzqzgrz3ZR0hEr3bTA19mM1X15KHi4OC0iRw_kfcglAO6Xw_uGIqwTuOiVrpAHBRK2w9JF83otPH45XGnovK6adpC0L6dHUvD8Urx0WSL2riJ2UZSM-5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26448031d.mp4?token=A_WppNlKIZ-ysfJENCYzj0GRyrS_kf6Y-Pe3UdEzP0QD6eFXgUY2_00Bm0B4TS71Ce_D1DuB8JT_b5gT-xQu4flS4jP1N-TUQotd6H0n8bmkhmUSP1358MbMuz7UZ-N6ZMvTSy556NBIwPYhDH7eizxuqRMzNbasBSPJIhYLXmzmPrya-GQGa_DlaOAjyTsc8dfOg4NcLyBw_6bRn6aqL7xqIpaa_GdKBQzqzgrz3ZR0hEr3bTA19mM1X15KHi4OC0iRw_kfcglAO6Xw_uGIqwTuOiVrpAHBRK2w9JF83otPH45XGnovK6adpC0L6dHUvD8Urx0WSL2riJ2UZSM-5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برام سواله یمنی ها دنبال چی میگردن که با اسلحه ها کاری ندارن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/84336" target="_blank">📅 19:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84332">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سلطان حمید رسایی را آزاد کنید حمید رسایی را آزاد کنید رسایی را آزاد کنید را آزاد کنید آزاد کنید کنید  آزاد کنید را آزاد کنید رسایی را آزاد کنید حمید رسایی را آزاد کنید سلطان حمید رسایی را آزاد کنید  #سلطان_آزاد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/84332" target="_blank">📅 19:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84331">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">فان ژوله غیر فان ترین شوی فانیه که تو زندگیم دیدم</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84331" target="_blank">📅 19:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84330">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCf2DqTK_DJxkUP65bf5d36XpCYfYFFs3d6QibGJpg2dR3ZJGAX2o9oIfAWLefx0WSxxNRoUGKNXgsh-JC8gGbrmkYImm4zriuK_d-2Bxr17GFL5Og0Ry-G6DmZS8k1z5YhRbf_QxjVUEbPuVf_bOlc-DXXlmKaLuklAoCDIQvVTypDogDRPRymon8GE_xybq2BOZ9o5nRV1mlSd2n0jb1N13UuQkC9OHmKKV7XUJtHYK9N4RX2IsBfb0x7AiTwqdh2e8t-D0K3_Sg3Yo4-ABw2EkhjGNajf5nTYsYKPDtkY-LXTWwSDbRq44FCGI9LsLrPQBteSpPBUuq8LCsvieg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران حتی تو معروف کردن کصشراشم پسرفت کرده پسر، از این رسیدیم به امیرمحمد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84330" target="_blank">📅 19:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84328">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rZKZq8JG73QBFmdjrLu3X02vh1RnRlufSTOnBpU6lwKjaUAJqut-iQSqbiEZMIbYU5DXiEIzCfd7b3D6FcWulVM6J7si69SyS3ia0ramDcYW52VT5wkqInsD_Ugjz_9HhJX2nehaPItN1NnlEIBZru9JGJqdhzRH34a16OjuxuY-efjq32ETenoBJYn86xJASmAKm7QbJUxPTJHtsa_ay78wfgcUeP9LzWAu-qeC8kBCHL_LH3Ko1TUBjPpgcKysbLnq9YrUwTOgkxsODSerqVcXJI7_46X2jhUzfVg4d2_K9cod2oRwJIUyrxJ4jrPnM7Jg7CVUSyocXlsEYu-Gjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a455UvIlakdb_P8ZWo6IOi9zmwS5dNOX_sO9zQ2URj3ZICg3BsUhcrJpRHUqDk-cKstwGyV4YHbpzjdHXnlYubkmaut2G8FIg88xb59gx17TFJz89q9hIsIWdpsPrHIeuydcrqas6kILKtaFrh-xJVK95OXMPKNLxtUqwcmrtuQp8txFtUc7dPTjM-46T5AaIag6bo6rSBBbn6POdCxZky0TjwmtLehqL1MYkTCEW5P68Zu-1KvlJCT9l9A-RhGSCewIgza9wdNT3WXqhqS2qa3UY8_bj1LJgcWRSFOFCyfWI1Q5735skwt1kJwbAUtj139dkLH34mnVUkhdOd1rgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترند جدید اینستا اینطوریه که دخترا دارن کامنتای کلیشه ای و کصشر پسرا زیر پستاشونو متقابلاً برمیگردونن به پسرا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84328" target="_blank">📅 18:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84326">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">چرسی: شایع اون تایم برنامه گنگ گوه میخورد که من اطلاع نداشتم برنامه قراره از فیلمو پخش بشه، اشتباه کردیم ولی همه اطلاع داشتیم که ضیا داره با اون پلتفرم حرف میزنه که از اونجا پخش کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84326" target="_blank">📅 17:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84325">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6261d1f5c.mp4?token=fnx2fUEaEWo2Yco1eDE1f9JQUpSuZ-FB1A4kmzkHFy4WvcQQyFPZtrFpYwHgvZUsqs_X4e4LgTCA0Gr6nw-BO6_ZhSQIbQjH8Gut37jR-Q0cDfMigaQ0QlN84MYXAw1txE3lmGdTFgS0eIRA-JYaWAnGgs3ZxW7NIv5Exib5h9uh41-s39KIDNClMhHEJafB3nzU9u0yHK0tKpSV_yPCxjA-XEW-SqDKjST_vav-0ETYQFIKOprL0RMdOml1-utanFLWGeTx3lMUg7nhixOC_6jjmx74TWzXSQqG0HPsmqOd7WLNNuSLUfiTQ5t5FM4oZRA5IIKwDNpOX7Zvl8ulDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6261d1f5c.mp4?token=fnx2fUEaEWo2Yco1eDE1f9JQUpSuZ-FB1A4kmzkHFy4WvcQQyFPZtrFpYwHgvZUsqs_X4e4LgTCA0Gr6nw-BO6_ZhSQIbQjH8Gut37jR-Q0cDfMigaQ0QlN84MYXAw1txE3lmGdTFgS0eIRA-JYaWAnGgs3ZxW7NIv5Exib5h9uh41-s39KIDNClMhHEJafB3nzU9u0yHK0tKpSV_yPCxjA-XEW-SqDKjST_vav-0ETYQFIKOprL0RMdOml1-utanFLWGeTx3lMUg7nhixOC_6jjmx74TWzXSQqG0HPsmqOd7WLNNuSLUfiTQ5t5FM4oZRA5IIKwDNpOX7Zvl8ulDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی گرامی خدا لعنتت گنه بیماریت واگیر دار بود فک کنم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84325" target="_blank">📅 17:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84324">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">یعنی این گیر دادنای امیرحسین قیاسی به مهموناش برا ازدواج کردن اتفاقیه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84324" target="_blank">📅 16:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84323">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دلار 260.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84323" target="_blank">📅 15:49 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84322">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84322" target="_blank">📅 15:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84321">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">شماهم جدیدا ترجیح میدید یه سریال کصشر و آبکی ببینید که صرفا زمان بگذره و دیگه دلتون نمیخواد سریال های طولانی و با محتوا ببینید؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/84321" target="_blank">📅 14:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84320">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUNitehUbgD10QxGx7McK_yG4Lc3aTSOSI-YlPk_giQ8rraNjw24dlLac7o11FvzmCxTo91VIJ32JXlrrPVRfWNzc4KZK8dLlO0I9Boj-vPJq7UqQfGBbq2M1tly0QxsZBPsdI-aMcYUsCyczqQNfMydI0g2yg2jzxNNMy1OqBxJU7ueN_jLx75DBKYGasV9rK0sABBDpfu_i2KPArRQ0V-_6nvUDJaLSj1e4p-o0HdVdwkCIQXAddadDpHNXLsWjSWuGhn3wrpv97-HFxJcRuzIW8EzV8vRamt_afMba6dJjR7OKAI_agFRE6W057QF2teKbhrE-Ttm_HdwWCsOpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسرا بعد این که کریر همو گاییدن:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/84320" target="_blank">📅 13:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84318">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NE498vW7WBusS_M-djd2hgaHiieXe9Pj4kkZRlKWdM5Zf7Nfx66Ri1KY_po9paJlL-9Q3gplRuGArDHINRJatQF3ataKZq--ktc9RZzHSo-5fL0XA5lAr6_dkzexg0U24dwjkp6rpnhzy6DK1H8dbFnYhCYpoP_YD7sZARjY9Jt18XDGiI4wHuBkR1t3El_45b2C6eQAGSzfOqxgAk1y939MWidMGBVzbSpjkFHra9UOyzjZOU0Z3Wvbzb0V4At3RHvzh3LZML7vXR7LGYO7o6BTjagPYAgkiD9wX5ktEDZf3RXxQ7Xi-6aquybdEu5HH5CloHXjTanRH1Z6iRCanw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداروشکر داره عادی سازی میشه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84318" target="_blank">📅 13:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84317">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7384d8a494.mp4?token=msnKQUzJXJ-fRdeOU7Rm8FPJKuVuuylvBUqKMnxwx-7dlcD9ufutFxxh_4ErQimImfmBSrl-9mJQZRVI8MwzInG6Mkl6d5fTxJEhomykeTtx9S6I02iVFMV_6Q1ek6QhuHkUglY9sE0exLZkZwmMOVyslCS36I0opgsXGzr2-Q9BDzYZMc3h3cV5_-jfmNnUctHN7e-yAHbQLhpvbA0LBADTPpWxBGFjl-Dyt68tYZ8uQMtiHLskM-C7mFOvzPBi53fgnLQXsHgeA6DQiSs0Jqb3rC3yKGB5IHM9T9t24aw_UdTl3910mghotVX-WxuXMSWnAwiJ8I0yPBbRyidNnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7384d8a494.mp4?token=msnKQUzJXJ-fRdeOU7Rm8FPJKuVuuylvBUqKMnxwx-7dlcD9ufutFxxh_4ErQimImfmBSrl-9mJQZRVI8MwzInG6Mkl6d5fTxJEhomykeTtx9S6I02iVFMV_6Q1ek6QhuHkUglY9sE0exLZkZwmMOVyslCS36I0opgsXGzr2-Q9BDzYZMc3h3cV5_-jfmNnUctHN7e-yAHbQLhpvbA0LBADTPpWxBGFjl-Dyt68tYZ8uQMtiHLskM-C7mFOvzPBi53fgnLQXsHgeA6DQiSs0Jqb3rC3yKGB5IHM9T9t24aw_UdTl3910mghotVX-WxuXMSWnAwiJ8I0yPBbRyidNnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسر ایرانی وقتی میره رو کار
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84317" target="_blank">📅 13:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84316">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6273e63d25.mp4?token=Lh3mIbf4W1QdTppHWLG7a8MrSerHoa2jX6Y3uz3dATHZ6MLqHMTrybNn7x7pQ6C-5qDD9V4xuXPCBgLVkG1gLijcNcyYR0HO8oQyHnzeOjdNfHuo53A-XOPbs_9loM_U4vWoJoGsea8JCRoLGlCJyV1P4KRFp1BCLa1ibCUd5gR_qTrXUa95rEmvQ7mQcJ6EAsxrB6mwGOfjuZUREy8HyD5hRBV3OgmRe1ei8VsNkmw8CmqNYrI7GP9wG3LXQX2-66hXUngIuoN-CgsIhHDK_ysAwgYp9duE-MBG4_u8tpOw4Q0lInAElCQCofhEKGMl1YfPzNd8VFXWcEGv-WHE8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6273e63d25.mp4?token=Lh3mIbf4W1QdTppHWLG7a8MrSerHoa2jX6Y3uz3dATHZ6MLqHMTrybNn7x7pQ6C-5qDD9V4xuXPCBgLVkG1gLijcNcyYR0HO8oQyHnzeOjdNfHuo53A-XOPbs_9loM_U4vWoJoGsea8JCRoLGlCJyV1P4KRFp1BCLa1ibCUd5gR_qTrXUa95rEmvQ7mQcJ6EAsxrB6mwGOfjuZUREy8HyD5hRBV3OgmRe1ei8VsNkmw8CmqNYrI7GP9wG3LXQX2-66hXUngIuoN-CgsIhHDK_ysAwgYp9duE-MBG4_u8tpOw4Q0lInAElCQCofhEKGMl1YfPzNd8VFXWcEGv-WHE8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تقریبا هروز تو شهر های مرزی درگیری مسلحانه شکل میگیره و سپاه اینطوری یه خونه تیمی رو با rpg ترکوند.
امروز تو درگیری ها حداقل ۵ نیروی قدس-فاطمیون کشته شدن.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84316" target="_blank">📅 12:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84315">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e0832652.mp4?token=v2Yl1Za63dbVzie-zl71hGdyN11AAyEIpP3Dd2VCw9ARm-dJSrusZSYJQQaflK5RIOo29llFK37sIoFXEju4-RxC2zYHovoSpr4M4bLDHtrzbzO7d8eeJXd7mi1ytY9S_V379kkcFIozkLt-nuNeovt2mZVWl69Nsqm1kjGyb_o1aU73NDYb7hHdnbthZK9LpUzyL3yw7kDI-Vlo8Mzd-BsByE6fHyVse2POwWQWku_MJtVMaXnkSRIkvkd3XzxYRIvn4ErX4jAGsp65_ag0kS_voTgjELKW78rJ6Gq6_KX8HH70Cc4aoTaQR7QYBFhpOsgBJwBOUfUDkaSlXoCkZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e0832652.mp4?token=v2Yl1Za63dbVzie-zl71hGdyN11AAyEIpP3Dd2VCw9ARm-dJSrusZSYJQQaflK5RIOo29llFK37sIoFXEju4-RxC2zYHovoSpr4M4bLDHtrzbzO7d8eeJXd7mi1ytY9S_V379kkcFIozkLt-nuNeovt2mZVWl69Nsqm1kjGyb_o1aU73NDYb7hHdnbthZK9LpUzyL3yw7kDI-Vlo8Mzd-BsByE6fHyVse2POwWQWku_MJtVMaXnkSRIkvkd3XzxYRIvn4ErX4jAGsp65_ag0kS_voTgjELKW78rJ6Gq6_KX8HH70Cc4aoTaQR7QYBFhpOsgBJwBOUfUDkaSlXoCkZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پورعلی : مجتبی خامنه ای شبا به صورت ناشناس تو تجمعات شرکت میکنه. دوشب قبل نیم ساعت اینجا بود.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84315" target="_blank">📅 11:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84314">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d8bb7d42b5.mp4?token=FZcG-EbK1FWoVp3w1waz7iTYa5MS6Rte8A2YqVi-y-a7LScdPKnEGDjY987ItAYMw4ZznDkvRxQHX6u4zZ1Tt0aAVK_U7Q1to0TTp4lPq_2ZbKK6fld-KCK_mx7VjCHFGF7u3yjRMzPgYRVHAjTsA-SxbKlyyJBh9pzQpB_iH7nbzPGKsa3WHmNhG1y7S3RGhP26Nl84yIVrrWaolXtKFVB5ico_1pDmbAjXuIOiHj5kRx2zeJKYp68defTgwyf_7j10GB3jSC-6Ij1yKxgZ7HCKVhEx5bsqmZt7LBd_ACVV5rsDweqPBUaRodV-k7AwTWbkd9VuAUz1WgNV3pKPkw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d8bb7d42b5.mp4?token=FZcG-EbK1FWoVp3w1waz7iTYa5MS6Rte8A2YqVi-y-a7LScdPKnEGDjY987ItAYMw4ZznDkvRxQHX6u4zZ1Tt0aAVK_U7Q1to0TTp4lPq_2ZbKK6fld-KCK_mx7VjCHFGF7u3yjRMzPgYRVHAjTsA-SxbKlyyJBh9pzQpB_iH7nbzPGKsa3WHmNhG1y7S3RGhP26Nl84yIVrrWaolXtKFVB5ico_1pDmbAjXuIOiHj5kRx2zeJKYp68defTgwyf_7j10GB3jSC-6Ij1yKxgZ7HCKVhEx5bsqmZt7LBd_ACVV5rsDweqPBUaRodV-k7AwTWbkd9VuAUz1WgNV3pKPkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
یه توریست و بلاگر خارجی اومده بود ایران و با دوچرخه میخواست بره یه شهر دیگه.
دو تا خانم دیدن شبه و خطرناک و تاریکه، برای همین تا مقصد، دو ساعت تمام اسکورتش کردن!
حالا این بلاگر پستشو گذاشته اینستا و تمام دنیا به مردم ایران افتخار میکنن!
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84314" target="_blank">📅 11:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84311">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea0a9e79fa.mp4?token=nqsCd7-6YFrw8UbbfCPDQ5JERR5-HSgG1qBNP13lQyN9S5iisLmKYW-pqzuvuBr8npBRWuo-FaxhcXeX1cJ1vMwKiKY_madta6s3Zx_hp1BwMpqhA065xz9FNmytbkrphBwTkgV9NnpBHWkReim2T5iupYlW3EWpOMFHE3gtbGGQxUU3sl0ASVcO5hFhRfQ60p-8XWUyleGeU_EIQGjHPtPRoX-s_w_UNXUfOCpIOxeqDUZF4WHA20JPdcKIp4ZKCtosySqKtAzofUFqAWMzXJAMQhPszXtR3XXaT-7STplAZpBTMS0KhrrXJAIc0HJ-1OjXN7vuWlZS112UKZf1TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea0a9e79fa.mp4?token=nqsCd7-6YFrw8UbbfCPDQ5JERR5-HSgG1qBNP13lQyN9S5iisLmKYW-pqzuvuBr8npBRWuo-FaxhcXeX1cJ1vMwKiKY_madta6s3Zx_hp1BwMpqhA065xz9FNmytbkrphBwTkgV9NnpBHWkReim2T5iupYlW3EWpOMFHE3gtbGGQxUU3sl0ASVcO5hFhRfQ60p-8XWUyleGeU_EIQGjHPtPRoX-s_w_UNXUfOCpIOxeqDUZF4WHA20JPdcKIp4ZKCtosySqKtAzofUFqAWMzXJAMQhPszXtR3XXaT-7STplAZpBTMS0KhrrXJAIc0HJ-1OjXN7vuWlZS112UKZf1TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رپرای جدید تا حالا واسه زلزله های مخرب تاریخ مملکت خوندن؟ نه.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84311" target="_blank">📅 09:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84310">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e286f8be43.mp4?token=lzasYIyczDUzU4fMOpXIcpRSD2QoVG6MeiKO45f9h_6-E_DrViotm8fC5NKPb17hm4tVanZqMauE0VpbjJCWnBk39E8kQLbKtrBhCvn8nxkXdAwMsVZXgPZPH3Ir10q7uCCK6rkEBECm79l24i0wBecHvZH6biX15OvZq2_d3WPtidKq7FFk2XcUpt5Vavop7j7pL1vYOqsEnxBC1N7nAxuY9EgJVnOj0ln94WL0FYLvL8yY2SmIMr2ijWOohr3woMuPLn_U2XvwkBMkaPDAKProzQp_zTYdwQzPtcVQK5T9Ro1F5eEE-TRU56CnGUjmy-BIvOK8YgRoJSQfXK75jpDtO7rjuGxRqfzTJAJU5NYP6eVe1FurbM7vt-41zHIZhDtKuHyrFnnm3GG0GMBybKtBcQivIVW80TsnJQMT04ai_K3AuBjuFhwHZBFG_gLqQS-HDa1THahtHryIX8j2o50QQRIYuYTnFkeBev_HBtt-bhNY4B-qEnMVRBVWoZsauBigsuLNBewf0B0McW_aAUP8aI6OVRNlHsLOrldOu6qON-ywUFUHplxkUnKW2jdcaQZVsxScJIIBnt2xkoUYMj0g2eoh_UczumsrkbWg73N6tDvwQDDuI-ksq1PxWVFwfZuNq9pR_7oqWVRtGgxhPeUDlPli1TgZIiOAp2eUVQ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e286f8be43.mp4?token=lzasYIyczDUzU4fMOpXIcpRSD2QoVG6MeiKO45f9h_6-E_DrViotm8fC5NKPb17hm4tVanZqMauE0VpbjJCWnBk39E8kQLbKtrBhCvn8nxkXdAwMsVZXgPZPH3Ir10q7uCCK6rkEBECm79l24i0wBecHvZH6biX15OvZq2_d3WPtidKq7FFk2XcUpt5Vavop7j7pL1vYOqsEnxBC1N7nAxuY9EgJVnOj0ln94WL0FYLvL8yY2SmIMr2ijWOohr3woMuPLn_U2XvwkBMkaPDAKProzQp_zTYdwQzPtcVQK5T9Ro1F5eEE-TRU56CnGUjmy-BIvOK8YgRoJSQfXK75jpDtO7rjuGxRqfzTJAJU5NYP6eVe1FurbM7vt-41zHIZhDtKuHyrFnnm3GG0GMBybKtBcQivIVW80TsnJQMT04ai_K3AuBjuFhwHZBFG_gLqQS-HDa1THahtHryIX8j2o50QQRIYuYTnFkeBev_HBtt-bhNY4B-qEnMVRBVWoZsauBigsuLNBewf0B0McW_aAUP8aI6OVRNlHsLOrldOu6qON-ywUFUHplxkUnKW2jdcaQZVsxScJIIBnt2xkoUYMj0g2eoh_UczumsrkbWg73N6tDvwQDDuI-ksq1PxWVFwfZuNq9pR_7oqWVRtGgxhPeUDlPli1TgZIiOAp2eUVQ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا لحظه آخر منتظر بودم بزنن زیر خنده بگن جدی این کصشرا رو میپوشید؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84310" target="_blank">📅 09:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84309">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/337199248a.mp4?token=tfmAaeOh6IDjSirYE7eLRrb0OAogvGgIiStturI94eghOI9X7RZw66h0YXVA1p8NDHMcdhSTiwEkt-TjW7IvTutP0pDU_mLuPVip7N7UdEQ4aEw9AnJcXxgglbTjBYOD0YvJgJ4uYtWiQmyjVT16e-5CA-umCrh4dlGBEI6Fp721CJ6Iuu2uFU5PBDbGI7CGDjp-6dCKf741kQKwRNnunW_N4TPCmBckA-Ibrjz_VSCQnkFdE3466XIuskHKrh_vEVTKSbHhdRVZX7_XqVfH92P0mvX725DPPkjs2KjH0vUVk_6j0jGj1wcSEKtUk7IkF5OIXbZUN_6WKplYEhoItQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/337199248a.mp4?token=tfmAaeOh6IDjSirYE7eLRrb0OAogvGgIiStturI94eghOI9X7RZw66h0YXVA1p8NDHMcdhSTiwEkt-TjW7IvTutP0pDU_mLuPVip7N7UdEQ4aEw9AnJcXxgglbTjBYOD0YvJgJ4uYtWiQmyjVT16e-5CA-umCrh4dlGBEI6Fp721CJ6Iuu2uFU5PBDbGI7CGDjp-6dCKf741kQKwRNnunW_N4TPCmBckA-Ibrjz_VSCQnkFdE3466XIuskHKrh_vEVTKSbHhdRVZX7_XqVfH92P0mvX725DPPkjs2KjH0vUVk_6j0jGj1wcSEKtUk7IkF5OIXbZUN_6WKplYEhoItQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کمدی شاخر : (شاهکار+فاخر)
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84309" target="_blank">📅 08:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84306">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a90438c76b.mp4?token=f7AIUv25ToHbXrzC2Y8p6tvJywQs39_mXCRjIjdpqBm9IYd1gnGu7mBMjSHYZKnItDIIV1hNNbvoAtPS4Kh1MCipUZqkFhVjgtEOxzfQNiK9tYAP46YnPGYT85aJM2MqWW0f10WKdp5_MERSW1x4UaqpQfmmZHse2zmg5TiRU8R6mobwDWpym7GtzN203IiT5kHPqQWT02ANT2RqdWzrGzrbkiez1Fxj05MrBYlgGrHfmigv8_0_PurN_BUOsj-bzSzLKE2I9mmADFa_Vw4HUvsd0_K6XjGc7sS2pkEiXKpZf7rSk0JSNSwuYHZw-avOgiEkBSKf-v3QAsuBZofUGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a90438c76b.mp4?token=f7AIUv25ToHbXrzC2Y8p6tvJywQs39_mXCRjIjdpqBm9IYd1gnGu7mBMjSHYZKnItDIIV1hNNbvoAtPS4Kh1MCipUZqkFhVjgtEOxzfQNiK9tYAP46YnPGYT85aJM2MqWW0f10WKdp5_MERSW1x4UaqpQfmmZHse2zmg5TiRU8R6mobwDWpym7GtzN203IiT5kHPqQWT02ANT2RqdWzrGzrbkiez1Fxj05MrBYlgGrHfmigv8_0_PurN_BUOsj-bzSzLKE2I9mmADFa_Vw4HUvsd0_K6XjGc7sS2pkEiXKpZf7rSk0JSNSwuYHZw-avOgiEkBSKf-v3QAsuBZofUGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو حاجی  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84306" target="_blank">📅 00:28 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84305">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed8253be66.mp4?token=d09j2G8nXWCpUIVG7PoPsMYjhq0PQTT27UOy_SkmuO0v8NslrGvUZYf_wUfkHmDhpU6R20SzGlnaD_phDVuL5uZSD38xf2MqO9W6KdZq99FvpCKtiycGkFLe3cMa7RSjOOrMmbW3xqcB1zoiKOSxk4VXpHS6aQeGRZ7Vh7zoFq3H5VmNyMnrgbG1aSlzxHOsUFcaUhVOAVFEWdi3jlnHao3q6-M2pM5_ZIkVkxWLg9r6o3LRTtxBiVTSkwCt-umNWsajf8MFQ41qF0rWB-i5vgGSqpBAX-s6nNK4DoLkLwsOgNm0IzgXZamEPshXpmC-ro_BpZ9RdcvtHVpPZkgBZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed8253be66.mp4?token=d09j2G8nXWCpUIVG7PoPsMYjhq0PQTT27UOy_SkmuO0v8NslrGvUZYf_wUfkHmDhpU6R20SzGlnaD_phDVuL5uZSD38xf2MqO9W6KdZq99FvpCKtiycGkFLe3cMa7RSjOOrMmbW3xqcB1zoiKOSxk4VXpHS6aQeGRZ7Vh7zoFq3H5VmNyMnrgbG1aSlzxHOsUFcaUhVOAVFEWdi3jlnHao3q6-M2pM5_ZIkVkxWLg9r6o3LRTtxBiVTSkwCt-umNWsajf8MFQ41qF0rWB-i5vgGSqpBAX-s6nNK4DoLkLwsOgNm0IzgXZamEPshXpmC-ro_BpZ9RdcvtHVpPZkgBZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو حاجی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84305" target="_blank">📅 00:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84304">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNxP_Lm3zMZ1wjbEf8fOMGZi0saWEbhf9ZZqQi_3EEhHR-Dn4XcUxkKFOUfKfp-t_1keqil5qLr5mVUVrkLnGzNUe-DRhiy3r6s5u8I15M2WpX3c71OTu7-Ovkp6yS-tn9DXIMt-tOsxnEnrsHXrRph44BLALCGX1RrcJv5Fl5Q4PFY_KTRfGVxopMgnVBqST7js33f00wKEdVUY15SKBijfcd0190fwz5IpBG_g7TFIW5WO9Bwo8jpVeXM8gBnj2zJHD3PoCj1jMLf0_sK4G0thKYP8C8WG4fdXtfBzaW0_AJ50Uwy0vmuGzQYguKlLTM0H2ejzdwpBobmp7zERww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصکشا دیدید بدون رونالدو هیچی نیستید؟ رونالدو بود دفاع میکرد دوتا نخورید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84304" target="_blank">📅 00:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84302">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دقایقی پیش وزارت خزانه‌داری آمریکا شرکت های ایران‌خودرو، ایران‌خودرو دیزل، سایپا، پارس‌خودرو، زامیاد، هپکو، راه‌آهن ملی ایران و شرکت قطارهای مسافری رجا را در فهرست تحریم های سراسری خود قرار داد و اعلام کرد بیش از 30 درصد درآمد صادراتی ایران را هدف قرار داده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84302" target="_blank">📅 22:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84298">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43faf33322.mp4?token=DWdvkI0teyDoD5407ubmuxKb31JppJGs5cPibkEafTEm2jPcQowtzUTJmRFyJnQsukL6SSiS8WR8ZW68lsGsZ0AcUXpGjSayLQK0AfmYlVftn91B9gVVOEWNXKAv2jwkIWvAcOm_VBAbP3ISvBJIJa1AWISQFP4bTlNL7id-3NKv1QrzcTfbLrSNjtidkkQFiDvBs2k_Lt-CnL7Iwy8tt8q6CZFjzuABxPjNRSyOd_mvkd9qj3D4xILa6NmeZsOABReKqDNvTYMz627Ful_MJX5Ypqphb_FeXqqo6UbYrbS2V7K2TWeDIBw8DtsYQWfz_9mS0X6bX7-NSoLdu2YvdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43faf33322.mp4?token=DWdvkI0teyDoD5407ubmuxKb31JppJGs5cPibkEafTEm2jPcQowtzUTJmRFyJnQsukL6SSiS8WR8ZW68lsGsZ0AcUXpGjSayLQK0AfmYlVftn91B9gVVOEWNXKAv2jwkIWvAcOm_VBAbP3ISvBJIJa1AWISQFP4bTlNL7id-3NKv1QrzcTfbLrSNjtidkkQFiDvBs2k_Lt-CnL7Iwy8tt8q6CZFjzuABxPjNRSyOd_mvkd9qj3D4xILa6NmeZsOABReKqDNvTYMz627Ful_MJX5Ypqphb_FeXqqo6UbYrbS2V7K2TWeDIBw8DtsYQWfz_9mS0X6bX7-NSoLdu2YvdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید میلی گلد بعد از حواشی و شکایت های متعدد مردم با کپشن: این طلا، بخشی از طلای میلی است که خارج شده و حالا با آن، تسویه کاربران در حال انجام است.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84298" target="_blank">📅 21:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84297">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">لیائو کصکشو تا ۱۰۰ سال پیش ۷ دلار میخریدن الان شاخ شده شماره ۷ رونالدو رو میپوشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84297" target="_blank">📅 21:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84295">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2BM51J6pSsWmEn8Y8t9ZmaZUBrAtQw7Efrdq9_njNnyCwbZmYlJ2wgkAtJNnI_BLeJ270GsQ0PR3TD6e6d9WirCJxAb0fUZWstOdSqd8VxO12Npr1JttANQWpvmysuk5WSxmT7LAwVJOyszhwvwGITxvTCo70uG-FkzGk6PJ2L_Oeu2fXE0eTLPRN1AGhWGETFcXKaL2yb4B74w6-ukAaoeClkEcIdGFmnup2jujyfBDD30gFucpIHv8HmouNRX7bCUapJF2f4hYMg1zoMN99BNjWO-1LLViOCEwMueHmjejwtnSvTv4lZ9q3mVv_H9mKRKjkx9uulqMP-NU6c4ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا جای این کصشرا یه شیر چای تریاک نمیزنن این شرکتا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84295" target="_blank">📅 21:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84294">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پوتین رسما ناتو رو به حمله اتمی تهدید کرد، ورژن ۲۰۲۷ کره زمین قراره هیجان انگیز تر باشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84294" target="_blank">📅 21:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84293">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پوتین: کسمادر هر کی که به ما حمله کنه نقض هم نداریم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84293" target="_blank">📅 20:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84292">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مهدی چند ماه اینده این ناوی که زدن چند میلیارد دلاره
یک مقام آمریکایی به الجزیره: تا پایان نوامبر آینده، ۳ ناو هواپیمابر و دو گروه آبی‌خاکی در اطراف ایران مستقر میشن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84292" target="_blank">📅 20:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84291">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝖕𝖆𝖐𝖍𝖆𝖜</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHTLEFM1Bh3thtCtMPhnVOjXQNmmrD4x5l620f_qAmPwOJAwKAxxR2LUJbccZ8fR0NuImYxBYXpBS9JrwfX0UEPWHz_45sxe74oh3JENZezcSjszZx8xLP_B-1Y30QTdCy1jDVN3M1Hls7jHo4X-xOtuXelazlYExx_G7aY8yATHPKKafC944cx2g0yar3wPHsg3nI1SjnH9BRuGpBcsjUXgKmg6FD1l_8z1jI3UETQEY7C6mgwFHtdaMZnTnrQiqguQSJXuosxvLcpUlX2_z58HIt__PYk1lWt8dawyqgBjk37Z5Isww9El739COLXPM1NLAqL4j66-eko_sYqjRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیه</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84291" target="_blank">📅 19:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84290">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVPATTjNdW7QyvcXIye6qDXH2jOlG0dLvYW2kxRTNhQ8rf06WD4IdDu_qmKTNBovu44nlxi7wW7hj2GhUIvF_HgQY0d-d7mI0B69TUSL5fLNQz8oWhnEjh-GcI_4YtuRJzTVFtBP74XjfAYwSuhbIFmCN9iF86EBPRcDeRqWniccj6ozcTpq1zM-9W3m6yiNQ9np0HKo_udzcvNSkrCO10SPrxRQawHXyeJQMjEBGPtAvjBpuQ-wZRyoZbu3Y30qpjmMZyt_X-jQqCtDGYhOnh7ZSiJVO2fYwKPExTaJcnlQmT2ql8MHqqnWjgV-Wu4TYkRKy7n4aheB69fGPH_T_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به این فکر کردید امیرمحمد هرچی دلش بخواد میتونه بخوره بدون این که نگران چاق شدنش باشه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84290" target="_blank">📅 19:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84287">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tVSKTHgf91eB_Q1sr4JwWTzzDQf0pRrXWlirhkAzmZHTR5fPKBbLBoJTOWmhm0If5kpuqXAVQ3lAqnNU5UMZByKh4bzxBBBnZnLcqqlg1w_IpxCWAD7faEgyjMo9Jj3fRGU6095MErhlEu2D-wf2GgtMwmX9S0Sn3YkDzkyoBGH_gtmWkN52svOzDik6GeinKK7eNQmV9dvjCYjrwrSGiyrDZOVimSB85iLYAzzOAtysCTAqJA7kqzlyP66vDs3MzLiWtKJXjF_37jFeJ0vvwZ4TxYgSWRs-Kw2DX5uPFSZmkLR7TdfakwBmzY1mK1UJCKAP4sqEy-7BztbRy1B9Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NfyKhjWyuNz0t2TjcSEhTIPo-L1-TJFKZLio4n8WY4zMV62BHPLpjBQQ9PVyHyRZBGxCzlPwvj0h6GnTc-wkSywTtK_RYZ2aaaevRTepJ-evesK-rBNTiSG1yLJi2E8vPn0mhk-Rt1CkLFnEm7GCaYUAU2YQH9J48BNgjhKsVNPB21dAAvA8M92QHMv6iPnickKL5vnPrVCgfWNAE4JAs8peAb3-3xG_ib716B9ClgLhNTXR68J7uj1TNJhYFyad-Dd96tNkFkoyugUg0Zz-cG20aUF7jLl39Q_BzcxStm0xfln3IGaxz8e8JGF8pD6LaqTvUH7iQRTDuz-_TZTA5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DfxQuzSYBEi5Mr4HLgGxUPdzwHj28kwabPQgMr1iVXBkIY2o3cK11VGb4nKemdERwg8kxqt5tjic1Sg8lzaUSVghZcotT38GUlBJJJKILjllJFN5sKgLaSh_qeD81bZblvaGemkeHDxyFFAkkT8-R5dFz7mgQgfzmI-rDwRlL8n3pCIaGwlVEc1vhaQz03c6f20dLllAZwewKD-Kx0yJEYha-dRdlrmjka_3g-wdnrRu777gI8B47_Nmaivxeb_QZxp47AzfIBbGWo601b7S8uYViR_KnSKrDgq2bI4w7zgRfW_AeVOOO2K1Dgnbfbto5m1Fpun98L1tT-1BsOV5yw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ریری یه جزیره رفته، ۹۲۹۱۹۹۱ تا ازش پست گذاشته اینستاگرامش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84287" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84284">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ناو هواپیمابر تئودور روزولت آمریکا هم پس از نهایی شدن مراحل آماده‌سازی راهی خاورمیانه شد تا نشون بده دکتر عراقچی حتی تو نیویورک هم با تعهد کاری و تکنیکال عمل می‌کنه.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84284" target="_blank">📅 18:38 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

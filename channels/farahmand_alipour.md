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
<img src="https://cdn4.telesco.pe/file/Yl2RUoYiemKQi5rNNYFyfLcm8o5MhhfneU4uZsocHtX5zEUuhKs9lFOBdlwRxVQNq_gNKGKT4fKfcouyhx3ZdSCt1ukt_EyMyP8R4jnAFp5kbhF6RmT0o7ZlqTTd75DuiPCodm__EHdD5uUuCnTFPxBYgLxnVSrU6unGDo4SYvdl2OYV3EXgZl8EDQAPW1FfO3aws_D_QcEqicv9bksTa7Dv4dHSX7EJ7sz_ACPgwXtiwRhAGsfwS2YUfcwRbACWszHpjR3bW_o4eo9YlRAEtp_xi-OTl-oOSECXoD66xF4FdbIoET0CjhR94NBI_8WCv_uP6Asl1CQ9G9i98iUcrA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 13:03:45</div>
<hr>

<div class="tg-post" id="msg-6802">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbRNohQNMJwKjiqfXQ0XChBg4e6gJ0ux0aI70Ml7_gB3Rd-01f5Ldzf5jJgXyjmYQ5zAi7-qEbOew_VdPBiR3aK8X_N2jyHIf6GzP56rbp-auRJy4whOw5HY_ClzYTDXqWwBV-8-jffVvIb39mL0gWqiANvzmGpg-sjcP6JwYw2y3ofW4NmEAv5rjkOOJ-dOhAUkY7Un6dEGtpUDoc75pCnWT3f94W_PqjrF_p052rwhDy85JtpFXjQfkgXseXqRrIXqSkNaMAdgM7J5q9uDzo0ooiD5KBh7ycuteb1q_uVMhuYTjJ8ceQkLFvSHC5STkb46sEWYVbIGh7oOFgQ1GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن  که آخوندها دائم به نفع خودشون و شیعه و….. استفاده می‌کنن آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟  یعنی قرآن وسط تعریف یک داستانه، و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل  و فرعون صحبت میکنه و  اینکه خدا…</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farahmand_alipour/6802" target="_blank">📅 10:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6801">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiujU7etkJDR6jofgdnFQuhOQ1a-BOPQctUc038IwANMD8aS0vyiNwx5kmj_EW1lnFksWq4ILSI6sRC29A6vERo1VDtAgWGsVPi24ten2gDLhkinG9N4bnmyjdX6sgKeMaEMlTXGCDaT67pLVPYi-jPGeygfSHY-PFpp_obH_ez8GUa_5pVmOcWt1343YwCZyNAyZCwJT8UzUJnYeSlNyEqJL4B_MdQyA_63VlklEw6HJT1eiqVVe8wpLPfKb33xcYEEtG8tjsMTXGWbrdR4Kv6Bd3qY0t4SrW_w9H49yWL4apiciBOd9SvY1WOULsOEKC1KuuFTs9_jPkgsmazYlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن
که آخوندها دائم به نفع خودشون و شیعه و…..
استفاده می‌کنن
آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟
یعنی قرآن وسط تعریف یک داستانه،
و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل
و فرعون صحبت میکنه و
اینکه خدا اراده کرد امت بنی‌اسرائیل
رو  پیشوا قرار بده و البته «وارث»!
این آیه مکی است و این نکته مهمیه!
چون آیات قرآن در مکه همه در مدح و ستایش یهودیان و مسیحیان بود، تا زمانی که اسلام در مدینه قدرتمند شد و شمشیر و سرباز هم به دست آورد!
اون موقع آیات متفاوتی نازل شد سراسر سرزنش یهودیان و مسیحیانی که مسلمون‌ها  رو تحویل نمی‌گرفتن!</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/farahmand_alipour/6801" target="_blank">📅 10:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6800">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/farahmand_alipour/6800" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6799">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebe3608b04.mp4?token=IoQrhEki4PLdPka5c7i1ZbnIaznK4Inoi0DPqVpccQcxS_5PIp6L7894ouy17AtNsjbIViyRZp5MImETy4yN9oYfDW5GZ2tpJUBfqhcC029cMWnRmLj4vWKAj8Q7l68sd1S22OrmeQGSMyuyoBafZxksp9ZaRJbo06WfGPGUrbWbgjgh2cRRKUZLGtMwb3zuRGC6DMDqqNb0v--I5ef0NUv_EJgFIjTRTdgRzpPCFkaNlhAibqhtu3MW2TYbIM-T1X5PtvYEJrXA7snvqJAVEwApgMDAjenQBadQDtSQb-w5Oxmk1huuAO42R4an9gwGbxMjAPkDSjkLAokiZGRIEa0oxqxV2yWj2ugYxJGrcCP5vRZKnXxqBlK7RP_gy6x4JMyAxo1IbyTjXwnOxVMq6fokr2FKMksU1eFtdIT2d5q5GCVvd4vCHTCrbvtX_e-_xuhoh-LV3j2OkfOBFBD-I56NOj85ABLCXGvtkBzVfzs9Ua9jJNmIapj1fs5wdutH1nWEmj438gpkhBqLDPpD_yXQyRYthqn42uQmEnoVQOjZlypZ4oUc7vegId_GkLJ59uuFvnu4JDD1TZh1Bmw2rQL9zRiwki-YK3l_REcOdHygrLcEyfxYgf4Y-sngWyOkBzl6jdUOAtgPxpqurVqOkD0V59-U2ABm7zyXF_kVtZY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebe3608b04.mp4?token=IoQrhEki4PLdPka5c7i1ZbnIaznK4Inoi0DPqVpccQcxS_5PIp6L7894ouy17AtNsjbIViyRZp5MImETy4yN9oYfDW5GZ2tpJUBfqhcC029cMWnRmLj4vWKAj8Q7l68sd1S22OrmeQGSMyuyoBafZxksp9ZaRJbo06WfGPGUrbWbgjgh2cRRKUZLGtMwb3zuRGC6DMDqqNb0v--I5ef0NUv_EJgFIjTRTdgRzpPCFkaNlhAibqhtu3MW2TYbIM-T1X5PtvYEJrXA7snvqJAVEwApgMDAjenQBadQDtSQb-w5Oxmk1huuAO42R4an9gwGbxMjAPkDSjkLAokiZGRIEa0oxqxV2yWj2ugYxJGrcCP5vRZKnXxqBlK7RP_gy6x4JMyAxo1IbyTjXwnOxVMq6fokr2FKMksU1eFtdIT2d5q5GCVvd4vCHTCrbvtX_e-_xuhoh-LV3j2OkfOBFBD-I56NOj85ABLCXGvtkBzVfzs9Ua9jJNmIapj1fs5wdutH1nWEmj438gpkhBqLDPpD_yXQyRYthqn42uQmEnoVQOjZlypZ4oUc7vegId_GkLJ59uuFvnu4JDD1TZh1Bmw2rQL9zRiwki-YK3l_REcOdHygrLcEyfxYgf4Y-sngWyOkBzl6jdUOAtgPxpqurVqOkD0V59-U2ABm7zyXF_kVtZY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو روز پیش به فراخوان یک اینفلونسر مسلمان
و هجوم جوانان عمدتا مسلمان در شهر «وینچنزا» در شمال ایتالیا، شهر  به آشوب کشیده شد.
در این ویدئو یکی از دیگر از اینفلونسر‌های مسلمان رو به دوربین به صراحت میگه :« باید اصول کشور مبدا خودمون رو به اینجا بیاریم. باید به کشور مبدا خودمون احترام بگذاریم.
دیدید دیروز در فرانسه چه کار کردیم؟
همین کار رو در این «فاکینگ» کشور [ایتالیا] ، این کشور گوه، انجام میدیم! تغییرش میدیم ، مگه نه؟ تغییرش میدیم!»</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6799" target="_blank">📅 12:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4MI5XsLbkYJVxKdTuBVEJg7sopC0Splyx39IDxnGJQ2_o6dTlejlu-2gwFO8ms4fKpySmU3noG5Fp07k_WDH_hgaz8hcZXO-8RI0d1d4dsO_4o-rKGAta24IXx95qHFqMbOBiLSNtNFNjgDpngYRNGdfnl0mWujwGOIpZquTDLy8Pj7RRqEqi25IJtxhph8bgOEGKPsDslGUpt23C6B1iR_HzZOBDhSqZH9OF0mfQRRdY-KFww0q5fQE9O5LV-lOXqhzrOPTCGP7zGY7Iz3_V3gU-AH5dO33QBck7snARW8DqujQ1gSEzG8pgcAL0d0cXy4vmSezgBxEn1et5HkuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»  در تخریب‌های اخیر خبر میده. دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.  در حالی که اعتراضات دانش‌آموزان…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6798" target="_blank">📅 12:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6796">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tEMIqN6ChCkjSJ7w0ytJ35W2jVJ7JDKrIr67oWD6e9KqHE8AzuiwJOG3DzfRwEFgAUh6djOuQyIhqMRq5l8jrStQUxmdquICzX5CFyMm6jIh07IwzUR9cntAZ3nf_ZX3De5PL7KxcqzYTXvnotJ5d5xl6Fm3ai7iwMhD9RKAknigGynBbTjZJyOBQbQI8hSF_hzsp79qUDt6Q145hEiG4Tx_HgGeuWmYElneVBps4iBcvnNCoBExabo6dBz8yDQWllb9MsPnHQAVRMGXVPnfJUs-PRf3n-HbvV2PKsV4oPoThnN0V0OuuMzjO9KQSzIEJyu9Ej1d2npw7PkrZ4Lu-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h-AlWmAdRybtctOGmMYiSeLAGrvavmd9XPig-TIc0kxFd6FvvMqJY8m-1SLjJO85aR0IWPj4otvDntjdKK1qLx-gHEh3hyxISrXjAvSziAr0ioGxZbWV-WqLn6pXhDi6bTeWE3ulKHT6tkgfvrOBJhxz99Pvc69d9AZuYsJ6JPgdN00i7x7H2dYNVfkS2TX8Qac55CAE0jg_yhHkjoB6vLzATKhmSjHOLtcCogBLk2pDMOFIfxy5UcO1u0jkX-fRwBM3MIVV-Ibr2wA9vXH0QUqD-8PO5eFP5B6JOv2OJPL42ON6zFZyvx_8zPkST-YQDzSsdYY8cwtkEz0QnaGPUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»
در تخریب‌های اخیر خبر میده.
دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.
در حالی که اعتراضات دانش‌آموزان فرانسوی
کاملا مشروعه و دولت بهشون مجوز میده،
عده زیادی با پرچم فلسطین، الجزایر و مراکش،
در تجمعات حضور دارند و دست به تخریب میزنند. دقیقا مثل هر بار که بازی فوتبال هست
و همین جماعت شهر رو به آشوب میکشن.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6796" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6795">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">می‌د‌ونید چرا جریان چپ اینقدر خودش رو
هم داستان و همراستا با آخوندِ جنایتکار دیده؟ می‌دونید چرا اینقدر چپ از جامعه ایران
متنفر و خشمگینه؟
چون همه هویت و هستی اینها مبارزه با آمریکاست!
ایران اگه یک پایگاه ضد آمریکایی و یک کوبا
و یک ویتنام بشه براشون ارزش داره!
ج‌ا، چپ‌ها رو قت@ل عام هم کنه براشون مهم نیست!
چون هدف و نقطه مرکزی آمریکاست.
همه هستی‌شون در این تعریف شده که جایی آمریکا
حمله کنه و اینها سریعا بیان وسط میدون
و ضد آمریکا شعار بدن،
در قضیه ایران ناراحتن که چرا آمریکا حمله کرد
و اکثر مردم ضد آمریکا نشدن؟
البته به جز اقلیت مزدور اسلامگرا و اقلیت بی‌آبروی چپ که هر دو اساس انقلاب ۵۷ رو داشتند.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6795" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کار به جایی رسید که جنگی بین  محمد بن‌ابی‌بکر و «عمر و عاص»  بر سر حکومت مصر شکل گرفت!  عمر و عاص، دفاع قبل توضیح داده بودم که اولین حاکم مصر بود!  و جایگاه محکمی هم در مصر داشت!  و مرور کردیم  که اوضاع مصر هم از زمان حکومت  محمد بن‌ابوبکر از لحاظ اقتصادی…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6791" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">معاویه برای محمد بن‌ابو‌بکر  نوشت که تو که هر بار توی نامه‌‌ات علیه پدر من می‌نویسی، و یادآوری میکنی پدر من فلان بود و بهمان بود، پس من حقی ندارم و خلافت حق علی است،  پس چرا پدر خود تو (ابوبکر)  همراه با عمر در سقیفه بنی‌ساعده،  حق خلافت رو از علی گرفتند ؟؟…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6790" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6789">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بعد از چندین نامه تند که معاویه نامه‌ها رو هم می‌فرستاد برای نخبگان و مردم مصر،  (البته محمد بن‌ابی‌بکر هم خوشحال میشد که نامه‌هاش خطاب به معاویه،  دوباره برمیگرده به مصر و‌ مردم مصر هم می‌بینن نامه‌ها رو!  اما قضاوت مردم به سود محمد بن‌ابی‌بکر نبود! نمی‌گفتن…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6789" target="_blank">📅 12:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">محمد بن‌ابی‌بکر نامه می‌فرستاد بدون سلام!  همون اولش به مادر معاویه فحش میداد!  (این موضوع فحش دادن کلا در بین شیعه به شدت رایجه! حتی در متن سخنرانی‌های امام حسین در کربلا!  یکبار هم مستقیما معاویه برگشت به خود امام علی گفت تو با من مشکل داری با مادر من چی…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6788" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مصر، ثروتمندترين استان حكومت اسلامى بود،به خاطر جلگه رود نيل وكشاورزى پررونق و...! به خاطر اينكه در دوره حكومت امام على ساختارهاى اقتصادى رو عوض كردن وساختار جديدشون رو هم نتونستند به درستى پياده كنند، اين مصر بسيار ثروتمند فقير شد!! يعنى اوضاع اقتصادى داغون!…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6787" target="_blank">📅 12:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">این رو هم در نظر بگیرید که امروزه به خاطر حدود ۴۰۰ سال تبلیغات یکطرفه، اکثریت مردم ایران میگن حق با علی بود و معاویه در سمت اشتباه بود!  اما در اون سال‌های اولیه اسلام،  چنین شکاف و فاصله‌‌ای هنوز وجود نداشت!  بین نخبگان بود!  برای عموم مردم، جایگاه این افراد…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6786" target="_blank">📅 12:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6784">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">محمد بن ابوبکر  یکی از نزدیکترین چهره‌ها به امام علی بود که حاکم مصر شد!  یک جوان تندخو! از این حزب‌الهی‌های افراطی و عرزشی‌های گنده‌گو!  نه سن کافی داشت! نه تجربه داشت!  اینو امام علی گذاشت حاکم مصر!  حکومت خودش که متزلزل بود!  چون وسط آشوب کشتن خلیفه سوم…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6784" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پس تا اینجا همه می‌دونیم که  فقط شعار ندادند!!  همه ما این قوم رو می‌شناسیم و ۵۰ ساله که حیاتشون در تنش و بحرانه!  اما فرض بگیریم،  فقط شعار دادن و حرفهای تند زدن بود آیا در تاریخ داشتیم که حرفهای تند زدن باعث جنگ و ….. بشه؟   بله! و اتفاقا دو مثال روشن در…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6783" target="_blank">📅 11:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید که حامیان حکومت،  در دفاع از خودشون میگن :  بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل شعار میدیم، ولی کدوم کشور به خاطر  شعار دادن و پرچم آتش زدن و حرف،  حمله کرده به یک کشور دیگه؟   البته که همین جا هم صادق نیستند، …</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6782" target="_blank">📅 11:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6781">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید
که حامیان حکومت،
در دفاع از خودشون میگن :
بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل
شعار میدیم، ولی کدوم کشور به خاطر
شعار دادن و پرچم آتش زدن و حرف،
حمله کرده به یک کشور دیگه؟
البته که همین جا هم صادق نیستند،
چون اونها فقط شعار ندادند!
خامنه‌ای رسما در برنامه «گام دوم»
که سیاست‌ها و اولویت‌های جمهوری اسلامی
رو برای ۴۰ سال بعدی تعیین می‌کرد،
اخراج آمریکا از منطقه خاورمیانه
و مبارزه با اسرائیل رو رسما جزو برنامه‌های نظام قرار داد، بگذریم به اینکه در عمل و با افتخار و صدای بلند می‌گفتند ما به گروه‌های تروریستی حزب‌الله لبنان، حماس، جهاد اسلامی و….. موشک، سلاح و پول میدیم برای مبارزه با اسراییل و….!
هر گروه دیگه هم بخواد مبارزه کنه،
بهش پول و سلاح میدیم! اینو خامنه‌ای هم علنا گفت.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQqkbam3U5s3oz4T0wXdwG1PbYUSMNkylB29C9kLYgC0FmTJTwFLJIvjpimyGzsP0WK4rF4nbJdse66j7dQ_BdmoKgN3att5hgV2PXlQMsqMsytWTpk3eA9Xq2wGvLxySsWUuA4v8MRQm-qQK9KUvvuo4hf0sjfgvJAffxOzKgfigTss-HVdc8GiOdUgluZqlcc6hVxMpKyEspQsPH2ImbU6pCHPZ1qtYnaDY_fVECDQzEZnfW7MVXRXo3ML_jo7dpofpib21W5kAQuoJn0WmjF8NB_8nxlusiX3cWBlyk_LkQa2ckd91xHVcZ7LCGmg5aEG4an-lnuwm5YSC7aRRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یورو شده ۳۰۰ هزار تومن!
و دلار تقریبا به ۲۷۰ هزار تومن رسیده.
ولی یادمون باشه که بزرگ‌ترین
فروشنده و عرضه کننده ارز در بازارهای ایران
خود حکومت و عوامل حکومت هستند!
ارز دست اونهاست!
صادرات دست اونهاست!
حکومت و عواملش خودشون دارند قیمت رو بالا
می‌برن، تا ارزهاشون رو به قیمتی بالاتر بفروشند
و سود بیشتری به جیب بزنند!
اساسا برخی از دامن زدن به جو جنگ و التهاب،
کار خود حکومته و مافیای حکومتیه، برای افزایش
قیمت‌ها و افزایش قیمت ارز
و افزایش درآمدهای خودش!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzhpmJNYfRH5uSe9I-6MP6acMRj0EIULzEry902zRnq9mfR8Gc-nAF95ZuhvMUDNxlqvW5AFz3GwtPwaEij_lCtkP0e_lHhkwOguBAK5QtCo7gGJpscLIMFZ2XZLMYns4A7_rODaBVSHQJsnu3JHVxuHONnnItgeG04P8amljiVEn5btqQAKE08htgCctrdSnyfUj7tjWPrSyKo2hx1-rdjl4G55-hA6m3gS8FNKkfXPuy9z86RNKuhYN0PPiZXFBI6F1cc3B7egOR9ccIJ3Vt7k1d-CNMmFE07JZ1l5zOYFa5g6VVDF5juBkOdI6bjQbSuQYF42ihOo2fEd5m7bfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی این ۷ شرط رو داده
به آمریکا که در قبالش  ج‌ا تنگه هرمز
رو «باز کنه»! آمریکا گفته تنگه هرمز برای شما بسته است!
برای ما که بازه! نفت که داره عبور میکنه!
و اصلا درباره تنگه هرمز مذاکره نمی‌کنیم!
اینها مثلا زرنگی کرده بودن بریم تنگه رو ببندیم در آستانه انتخابات قیمت نفت بره بالا،
آمریکا بیاد گریه و التماس کنه!
برای «زمستان سخت اروپا» هم منتظر بودن روسای جمهور اروپا برن بیت رهبری گریه کنه، لکن هیچ کس بهشون محل نگذاشت و خودشون دچار مشکل کبود گاز و برق شدن!</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVdMrHB_15SHWeIEy_CcIQGwtlb7ehPOj3rvs3Gek3UlXy1-b7spGjZPCERl17P9jWowRqCDvKbZhGuWqrovVhNoJFE8fnCK43WCQq3__EGmEhJxhjd_NKT2JoZfjKT0DQn2Ym8eT4Y81SHUQ60MCIA3YDIxgVXTEme9w7ZbZM_GYfTYTq-LKdS3QS-2feR1OFodFApFXSUxNW1mXW6-DsmqqjQWzy-Iw0fAMxPUze5ClGxm62vhT3unCDGKEIPc82ORpHP006gyj8wRvOoPZvYgFiR5LhoP0Q25az7e2s2zVbpGlR25wba5qmCf0NEWuKc9f8TdHGqILhkxqtD07g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=qXaXC6CmNTx1hPHgi81wX6lNUEMo9MwxdFoNNyHhCzaQwiWGI_lYjDCKHzIkxbKvgkJv01KOpMMwFPhnBzZ0OnGCkZsLkKYb7vAiXGVrhlez1_LHfI5nrT09Gmn9NFE1bAqbgew_f7Jph1-ZDALu7lRxFwfXFjCVDA8iHUR2m2fQNfnC31fwzBAZ1SYlHMsyA1s1qs_IkjczWgGObMbtQ0fr2gYvTxJ8cihbmvWVdfYd7EQXetTg4hr44hAFsEugn4mRswzIzN6qS_groKuYNjapNK45Xe9wZMlqx9WoFldMWFGvkfPGU0v7eOOAIEfLsFVylHp0spThvMoFk3MS8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=qXaXC6CmNTx1hPHgi81wX6lNUEMo9MwxdFoNNyHhCzaQwiWGI_lYjDCKHzIkxbKvgkJv01KOpMMwFPhnBzZ0OnGCkZsLkKYb7vAiXGVrhlez1_LHfI5nrT09Gmn9NFE1bAqbgew_f7Jph1-ZDALu7lRxFwfXFjCVDA8iHUR2m2fQNfnC31fwzBAZ1SYlHMsyA1s1qs_IkjczWgGObMbtQ0fr2gYvTxJ8cihbmvWVdfYd7EQXetTg4hr44hAFsEugn4mRswzIzN6qS_groKuYNjapNK45Xe9wZMlqx9WoFldMWFGvkfPGU0v7eOOAIEfLsFVylHp0spThvMoFk3MS8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند سال پیش یکی از دوستان با آب و تاب تعریف می‌کرد از سیستم پیشرفته
بانکی ایران و کارت و انتقال پول با کارت و …
همون موقع بهش گفتم این گسترش سریع
فعالیت‌های دیجیتال بانکی به خاطر پنهان کردن بحران عظیمی است که اقتصاد کشور باهاش دست به گریبان شده!
وقتی پول نقد دستشون باشه خیلی بهتر متوجه میزان بحران اقتصادی کشور میشن تا با پرداخت آنلاین و کارت و…!</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=IbsyQ69O-kLVxcJib68ooik8CDKwE0Hrkvp2uYBoC09u5Ge6E0_6svB5WRCjoz1gmSgeKuKCDbrYTByp3U9xq1f34d6easRnIJwFlxhbWqgA8maopWtQMvsLL-v4pjh9zyaglD49qktVEe0_vzDqWEyc5Ik_FlxEQ7BOhnZCqDhhiawd9Qxf5KKZVdzJQs90SvQZUGB7MwruoRpWDHqrVcuUZelTUdVaJdQEtsRvCIftJyh2PGJUWbPr7TdwtOqkoE2fOrowJrtaYn506__N0xOrA8fzdbPzLMMbc3g3jMOHVx-wE-StLhXlxR9BEqFtoJm8YFPZbDnLwfk3lhvsDq00azbwHD4gMbKcj7_qydTxC5bL-xLAcAXrQnzWu4NjpR7EBVsTq4Lzfo3KIVWvxI5eysqX4shsmeNXuAhVVvNwSx55wnMiuxlpgTi40HFh3qoHRiAdloTaPp-dwHDZemI36_2q2OCQMp8auzn4Jt9PQiV3cMgKNi7mMAvokMQSUkhQScdt7N-pduJ4DCEWY0irhy2grSlBWJ8XYRBvtdyKKiidByo0NonpZtVQpcUBJyvErhZ67ZMdJQBoQJlSL3Fd-jRMJ1Yyq46gv8DylxMOnCxpTOuIeWwplrvlCZQ_oCzRFyQzLpX1rbkICxYvsVMuO22e3Xrq9EvrmEyNxHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=IbsyQ69O-kLVxcJib68ooik8CDKwE0Hrkvp2uYBoC09u5Ge6E0_6svB5WRCjoz1gmSgeKuKCDbrYTByp3U9xq1f34d6easRnIJwFlxhbWqgA8maopWtQMvsLL-v4pjh9zyaglD49qktVEe0_vzDqWEyc5Ik_FlxEQ7BOhnZCqDhhiawd9Qxf5KKZVdzJQs90SvQZUGB7MwruoRpWDHqrVcuUZelTUdVaJdQEtsRvCIftJyh2PGJUWbPr7TdwtOqkoE2fOrowJrtaYn506__N0xOrA8fzdbPzLMMbc3g3jMOHVx-wE-StLhXlxR9BEqFtoJm8YFPZbDnLwfk3lhvsDq00azbwHD4gMbKcj7_qydTxC5bL-xLAcAXrQnzWu4NjpR7EBVsTq4Lzfo3KIVWvxI5eysqX4shsmeNXuAhVVvNwSx55wnMiuxlpgTi40HFh3qoHRiAdloTaPp-dwHDZemI36_2q2OCQMp8auzn4Jt9PQiV3cMgKNi7mMAvokMQSUkhQScdt7N-pduJ4DCEWY0irhy2grSlBWJ8XYRBvtdyKKiidByo0NonpZtVQpcUBJyvErhZ67ZMdJQBoQJlSL3Fd-jRMJ1Yyq46gv8DylxMOnCxpTOuIeWwplrvlCZQ_oCzRFyQzLpX1rbkICxYvsVMuO22e3Xrq9EvrmEyNxHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpbzMCpJMUkaDvHic4OFVRfMX2OPW78Bg2zu5cHm1lKTuMD4K1W7k7QUgcwnRn8wWMBPRjpYG5_f_2NKN-yUUqnibQ5WfsAsw18lQV4Kxnn06f3Sl3EOmqLnc0salAoWHgcWSgXbuuRo9-k0BWzlmGHmPw5dvAZS6dlPZRbC9bo_p7TqHLHwsC9YKTIPjacSAoGFW856H_zwzOV-xEExSIinKL7dNUQRsPY1pVR4NCGdkikkjyYNrvoHyN_ErL-UZL-aRYfn2vGPWhKrBqHACT27MLtyP2sNgmVRUFK1XHPuCFdQDuirXrKpO6t7mGOUkBqBLz7eBAsk0iPH6ISxyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/scR5SebmMejKR9kMCDHTZrrQUrdwbj-xR59HYE3myXPODkFS9H-oVsMtADEKFOQpMpFS4DgXZBr1rdK7-rLDYGBHhC52JIto4LSRCLIUpqu-gJ231CMdXlSw82OAZuF4NBeqfcp6pK45oG8PzZA9T5CJC_XKw27jjSSBH0cVtg8cuCkxwreHxwf2eEY7RcaBHRtmJxJ2J5ycOmC4pDLjTyEbvUjJ3XsPMGjDwbyh5IddNFIFK_V0wLv16wNR46yQEeHsBqXmitOLrCaD64bByS3XvLN3nEf1Lj90J98sxwA5WzIAM8Ed6_KCESB4ZbjfMZsUccWXMXN06Yv08EWOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJ6JGwTS1GryFvrCmk0Fc0ARwWwRgSXDa-qs6QhYkCugQfiXjrvVWCVO2P9_RcOIUOmQcRohlSjPGCogReDa0lkTqsVt_ovVXRombCo4D01ZdDhIyJqpgZhC-Aox-XvLNKOFRnrGY6kyxMmI-Q2uoE-WtiSOxRs-oC4Qpl83rOYvz_k1MCHYnIPzRuyUX8QtAM6YCtM0nDClLzwJqgylBt_s9vt4N8NoSpiZdY7kDuXVPr5WUUc4xfzR5gzHbe4bDHrprIaVuUMtZGO1iSSzekZTZf91qCX6d7txPnInHLXd56bRg9ZTCvWPaQF3rqEd9_0KZ0Oo1Mfv1Ot5WcHdfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=Xn-6wNpb6Lk079obOiLyYy2nzc4ASo3G99R3L3w4IOKCL505tC8-3xx0hQAmhL_eR6x7RcO-PmT1V91SmqIVuP48vXn7NuS5U2KMIV0HAMA-8FJzxusa9K4vW9MXetLkcDjFai4TMIcCU2n13EVHcCWJOg-CG8cAM2PkpU1Lxa3CHlByriXkivhLPmQ_xsqMk4-WtB52_DtdYDT6viqs2tD5sBsaJzjCLTbk8M-CDUwun1xC1VBq_2WXyJmtPzmdqSRWq1pIQ_q0q0FEmd25JWiL5EdAeRUXQUbd5DZhvwb5LvAoL8yF8GGCAhAJK6ZEHDmm4jrzigRg7ssiULO3cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=Xn-6wNpb6Lk079obOiLyYy2nzc4ASo3G99R3L3w4IOKCL505tC8-3xx0hQAmhL_eR6x7RcO-PmT1V91SmqIVuP48vXn7NuS5U2KMIV0HAMA-8FJzxusa9K4vW9MXetLkcDjFai4TMIcCU2n13EVHcCWJOg-CG8cAM2PkpU1Lxa3CHlByriXkivhLPmQ_xsqMk4-WtB52_DtdYDT6viqs2tD5sBsaJzjCLTbk8M-CDUwun1xC1VBq_2WXyJmtPzmdqSRWq1pIQ_q0q0FEmd25JWiL5EdAeRUXQUbd5DZhvwb5LvAoL8yF8GGCAhAJK6ZEHDmm4jrzigRg7ssiULO3cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو سال پیش
حسن نصرالله، رهبر گروه تروریستی
حزب الله لبنان، برای چند هفته،
ویدئوهای تهدید آمیز می‌ساخت!
کج نگاه میکنه! انگشت میزنه روی میز!
رد میشه و…!
رسانه‌های جمهوری اسلامی هم جشن گرفته بودن که آقا اسرائیل «با یک ویدئو!!» بهم ریخت!
تا اینکه در روزی چون امروز
(۲۷ سپتامبر)  ارتش اسرائیل با احداث یک گودال ۳۰ متری (به اندازه یک ساختمان ۹ طبقه) در بیروت، به تهدیدها و ویدئوها  و گنده گویی‌ها پایان داد!
به همین سادگی! فقط چند ثانیه زمان برد!</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=bP6xCeQqxsA_C0tJb9XeWokZVyXPZRjXFcIqmfOETHYRksz5pZ_jHcvW1143qoNvPCzaOW7GHggNCBdGVoCmXEE9DfEkWAJHSUzf-KOjsdOAZLo6o5ITlhJJGSz9h4ZumpkiquBQjduHwWQx6pXNnxIf8icNEe1PMSXgDU-KiuUAir0siB9BXOIGy3RZrJf9lxW_I84qG34sHHKNa7PAZPCpjwlUXzuVXgk4tOeTrO0zvrPdVUioniQi2vcEPhDMW5ZaUbO5fYDWWTR-v1gyXxsX2b1qjuCcC2vP616J_6yVWmW6fdEIYwilOJrDbDd_OHUlti5Uk8ocSB-3HShkbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=bP6xCeQqxsA_C0tJb9XeWokZVyXPZRjXFcIqmfOETHYRksz5pZ_jHcvW1143qoNvPCzaOW7GHggNCBdGVoCmXEE9DfEkWAJHSUzf-KOjsdOAZLo6o5ITlhJJGSz9h4ZumpkiquBQjduHwWQx6pXNnxIf8icNEe1PMSXgDU-KiuUAir0siB9BXOIGy3RZrJf9lxW_I84qG34sHHKNa7PAZPCpjwlUXzuVXgk4tOeTrO0zvrPdVUioniQi2vcEPhDMW5ZaUbO5fYDWWTR-v1gyXxsX2b1qjuCcC2vP616J_6yVWmW6fdEIYwilOJrDbDd_OHUlti5Uk8ocSB-3HShkbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBsnKz0FVtTwonsT5XcAGUlmcfoIPCC6XHJnZkonyUymLQLyIfB7rvg3uARHvhecaLl2li2Az5Gy0S-PJsvoRnAK36dEnShlVUmEfMtvRNu4WZBxizJK-Kh1PaQzZehXutbX1rZRFK4zzO426TWPMTXST854jAi6ZjLNJejbhO7Elh88hH2lOG1o5om9qEqM5TUkHk9tDuA7b9VKM_IkN1nD2JICBVMYs4aLFZp5uvYmwmG-bIcQ6Ogi2xtCQWSaSGfB5xmKQ5vjoFSNuTX2mLRn5Qei_0wi1xGhg0XrHnScpp28QCWMS7mchy-JqCAY0S2w5rJ2kYWQCg3PpYNf_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=rqcFE7ceXwqoNQpQJE6wXYj4Zp9tFOd2v8fIWuWFblKcRfZcoEtXHGm9VN-R4e-vhJhYFAqJcnp-fEZYNgXWbsI3-35QS6urNrwrwpIUpw4K-Bbwfwm_6QOfcjsp-URI1qm15k7roupvhYclgt_Id-w_NXTSU6uSeJwkm3FSrkKRW-hr5hvHhKoLdfZvE0wuWNlhEpId_jujS-ZK9pJTkdDy-thPXeCIwLQ-YjDBmzU7BoPGGei0OVyhxFwDZXgV7TgiFNXsaDQHdf_RyJ01t6AW5uXW8XUm13KQ6Qsu0DgSb2QF5RHdtk5PwppIMWBkUDlZrjGIkfYevbGD_Csc2r79-VDgmq59Vft8GswZTXTgfEk2R5YE9v5kw43ifx3oSd1GKDe5mrIxG-4NN9xtUUWMPzIGvNr0rVaO4nllkZcdKwMqenBTx7CpDC2fXT0xEPP98_y4my84WFT5a0n-EiP3xcPQLKU_mWjJNkR_x-BoANpbI_d0f_i3RDGO90wlz1M9ZJTM6dLBON6MyYqig2kjT1TH8Exie-Yca5kaabG1ApyJLJHjoy4LTobPt7tDxbML_BOCle33aIrjwAV0b8EAIOTGTurDyhah91qxBN3l_Ni0RS-mSnNdydvu8aWipoxUp3I3SeI_r9sUuEXg6hpzU_bXORxXAlaZenJyfE8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=rqcFE7ceXwqoNQpQJE6wXYj4Zp9tFOd2v8fIWuWFblKcRfZcoEtXHGm9VN-R4e-vhJhYFAqJcnp-fEZYNgXWbsI3-35QS6urNrwrwpIUpw4K-Bbwfwm_6QOfcjsp-URI1qm15k7roupvhYclgt_Id-w_NXTSU6uSeJwkm3FSrkKRW-hr5hvHhKoLdfZvE0wuWNlhEpId_jujS-ZK9pJTkdDy-thPXeCIwLQ-YjDBmzU7BoPGGei0OVyhxFwDZXgV7TgiFNXsaDQHdf_RyJ01t6AW5uXW8XUm13KQ6Qsu0DgSb2QF5RHdtk5PwppIMWBkUDlZrjGIkfYevbGD_Csc2r79-VDgmq59Vft8GswZTXTgfEk2R5YE9v5kw43ifx3oSd1GKDe5mrIxG-4NN9xtUUWMPzIGvNr0rVaO4nllkZcdKwMqenBTx7CpDC2fXT0xEPP98_y4my84WFT5a0n-EiP3xcPQLKU_mWjJNkR_x-BoANpbI_d0f_i3RDGO90wlz1M9ZJTM6dLBON6MyYqig2kjT1TH8Exie-Yca5kaabG1ApyJLJHjoy4LTobPt7tDxbML_BOCle33aIrjwAV0b8EAIOTGTurDyhah91qxBN3l_Ni0RS-mSnNdydvu8aWipoxUp3I3SeI_r9sUuEXg6hpzU_bXORxXAlaZenJyfE8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد
تا به دنیا فشار بیاره،
اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=aFqM0oHW3DZYUQ4IaSk8mxDMjLh3l2zO0gevFUKt7Fr45XIXJwtk1uVGCg4OBmxjpxi3-zbNacLIisNQS7PZO736ckpjH7xSfA_r8V6CTZtEWpEb4zo6LB28ySZ-pe93UgBpXxL5VSkfFkdSJBCfi2alPrHUXu4T14BLSWVjHDDooy6cyfTMds_p31QAIzOH5XM-5TzZyS2KSlFSYBRGeckx3qehCl2glxLZPwf9EDNKZUCSf8YBMn3sq-oQgyLwPqhdYXX6b9ostvlcPbenjQt8qcJLpG_fOvhBhHAvGdvodsuQcCEUvHBFEhrIfpdbPc8O7eE65mrA3GYl6s6REw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=aFqM0oHW3DZYUQ4IaSk8mxDMjLh3l2zO0gevFUKt7Fr45XIXJwtk1uVGCg4OBmxjpxi3-zbNacLIisNQS7PZO736ckpjH7xSfA_r8V6CTZtEWpEb4zo6LB28ySZ-pe93UgBpXxL5VSkfFkdSJBCfi2alPrHUXu4T14BLSWVjHDDooy6cyfTMds_p31QAIzOH5XM-5TzZyS2KSlFSYBRGeckx3qehCl2glxLZPwf9EDNKZUCSf8YBMn3sq-oQgyLwPqhdYXX6b9ostvlcPbenjQt8qcJLpG_fOvhBhHAvGdvodsuQcCEUvHBFEhrIfpdbPc8O7eE65mrA3GYl6s6REw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCaIEDOxQ2lL--ijfXvi-EfEQ4KYr3wP58e-pQUeOel_no1zni9TJiMsgMMxXgjw8qeDcYqa2cQqPKD7vrSc0NHmH0EXuPWvV47vtDBHbSAO932cwm4OH7E9D9N4hxRnkFFpdoOgO7rTPIW7FilHp1V5yHRLtDEGu_dLs4gqycsshbCC2zk7wOc108UgPylVjMkWSDLNq9VkXqzhUhzuvJc5MeHhZZdbOTQsSJLH_ejaLS5Eot5neklPad0EfkJtW8pK50zK01xX43T5mijriYllvQ8ALO2jbrbLM3Fcv7ZPF9UNGp-zb0_vMJW-xDS2V10G_St33XnGRIH0nOlxLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=akk7iPujBeH1hr9pF5qmVB4wS6BhSIvSsMUU8RWnAyzPWvpWGOL3U4eK0KZgMW0trgbC_NpeJlhrVTndfv-V9C8MvYAzADbgqpJLUTrNthFPVhDSOLq4uuOS5IvgRpws2XgJXCGlIf4Y4fnS7pPjJ-s_8w--cYU84KmEkrta3znx9Smb3gR0xiKoHVS7xCysJ5aMjkpDDT9635gIlqCz7zhJ-2hRGqnM145lyUiuk24NJYoU33wkA0eZPqDXbLnzZIiHI_n5AILIdG0cSl3dpF0TdDHPvhVdYZ-J2TSbaGGKSf1AGncDxJGoYDNxlqvaTNnrRediixfdo4Pf9LDp5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=akk7iPujBeH1hr9pF5qmVB4wS6BhSIvSsMUU8RWnAyzPWvpWGOL3U4eK0KZgMW0trgbC_NpeJlhrVTndfv-V9C8MvYAzADbgqpJLUTrNthFPVhDSOLq4uuOS5IvgRpws2XgJXCGlIf4Y4fnS7pPjJ-s_8w--cYU84KmEkrta3znx9Smb3gR0xiKoHVS7xCysJ5aMjkpDDT9635gIlqCz7zhJ-2hRGqnM145lyUiuk24NJYoU33wkA0eZPqDXbLnzZIiHI_n5AILIdG0cSl3dpF0TdDHPvhVdYZ-J2TSbaGGKSf1AGncDxJGoYDNxlqvaTNnrRediixfdo4Pf9LDp5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو و این حرکت
یادآور داستان‌های عهد عتیق است!
شجاعت و جسارت فرزندان داوود!
که در عین جوانی و نحیف و خرد بودن،
مصمم و بی‌هراس،
مستقیم به چهره دشمنان خود می‌نگرند!
مثل داوود، نوجوانی ظریف و آواز خوان!
خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه زده بود، اما اسرائیلِ ۸۰ ساله، از این نهراسید!
یا از اینکه جمعیت ایران ۱۰ برابر اسرائیل است!
یا اینکه مساحت ایران ۷۵ برابر اسرائیل است!
در قطع سر حکومت جمهوری اسلامی تردید نکرد!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VACZ2uchnzD7hFBDfm_FD763fFg59PnGXRK7WG02xkt1ZFhkeyBNZ1Dh1KhwA_6CakZkyoZ99-kHwfPmUGpjG3CyLSAhaXgup_wkyEHeWkNaAZrTIas6Gia09obJBOr149xr1ZGtbmb2xBAS3EPb3qaQVIKYbO6AjTaKPB2X4i1mwIs9m7y-v63BdkI7EN2vaim2vtyuwKuTcCKwOU2zitEyW97hEMwa5P3DEkqfw62b0kSS5qlp7MOmcRJXUSwE21-J-w5K8PeSpI-Tk_Uuf3EsJPrhFSytAqgl7LT7zh4LZMVC9Oi44XemDuGHo77HEa_WqWGCmkcV0YJSWt8jLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HN5pjrtdYQxWptxA8y8-Wp9EV1ivpRfVU_1fmJ1fEr7kMTrvtjGvT_21Yu5lmTa4GMZt6XNsqf06A9RrURj_WVtolsLyovsdgbh7MtwX2WfU6cD_5isIMHA0-9lULhxw6-u8qfNoYt6_iNyGI1nATgBSIU-LmCOZpSWVQp-ESXkyVMmZ5DwZlkBq97xN0a0pOjiA9jNHGCyTYf_6oSXeapPh0hqfqFosZbPSbCTASpkQcuUbj3z25uPXUPpxdQM5DXPHyfT8GiV4F8na89f6tzrwk3juIuERuUChW4vn6zdbebnza4wRnvn1wiiZLTgOiycv-IllQqfs8iMXMAb1Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود
که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.
.
این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،
و نقش میانجی‌گری این کشور.
(وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،
باز هم ترکیه این مسیر رو باز نگه داشت و گرچه  از انتقادها هم مصون نماند، اما کار خودش رو ادامه داد و سود بالایی هم برد)
🔴
با توجه به وضعیت افغانستان، پروازهای ایرانی به سمت شرق (چین و..) هم احتمالا ادامه داشته باشه
🔴
و از روی خزر پروازها به روسیه ادامه خواهد یافت.</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=KWm7JCKdWOkBDhCeF06VYIXumpT4OkxTnWtceNy7ePTXByGvNhBhap7JnOI5EapbFGlJc142v8IzoOmpFER1DIEoVvQyejAQ8y63d_FFi6_IQx3-AUyFAuEjSxyEz1uZaLpcuFAHd3bKpEFO2P8w5uwhIkgaGJ1XUY1hEYJBpnOjxyXjoVpinkF4zFz-oXRThbI_4cHHzKY21VzG2KJpDO7aMoqm9xp2hDcXnQyVBKPVYAhuqSyIjU_kWUiDiwfdp2FeID1betr3O3yPW7MsHhiVWQwh9dNwt0RoPPvtRUR0piHMfkcK3H5ewox7b0jRDv6okT4ABbcTK4KWZxh72Iir2f1SNQpCVu1nTovXWcUqJeTGwJI3V--geR1mgVNoNIKjV5KlHFnrMlOWeVSWuSHVL4enogOWxaDd1hhuEOrFpJ6Epaz75dJRJszepqTt1juxQ0FGXyaLqtC43ORJC-BGwrJaa0yvej8K0kQxWvj5vtxVC_mUEsRe2m49rwjQjkhKYhzZ2aqe1gP6vH_kQg1U_C5UPsgx9cCwydIW54Bvz8YudJh4y7ZbMvqJ_j-Gl5dYjk5gQ7_Jv5twSSk3XmK3LZrmguPIDZvK5qHVJylOCK-B7sKgxTnSNIaIPVu37FuF8yfsUrddERPG_xWmftsMU020Z4fpZD1ywCCwKQs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=KWm7JCKdWOkBDhCeF06VYIXumpT4OkxTnWtceNy7ePTXByGvNhBhap7JnOI5EapbFGlJc142v8IzoOmpFER1DIEoVvQyejAQ8y63d_FFi6_IQx3-AUyFAuEjSxyEz1uZaLpcuFAHd3bKpEFO2P8w5uwhIkgaGJ1XUY1hEYJBpnOjxyXjoVpinkF4zFz-oXRThbI_4cHHzKY21VzG2KJpDO7aMoqm9xp2hDcXnQyVBKPVYAhuqSyIjU_kWUiDiwfdp2FeID1betr3O3yPW7MsHhiVWQwh9dNwt0RoPPvtRUR0piHMfkcK3H5ewox7b0jRDv6okT4ABbcTK4KWZxh72Iir2f1SNQpCVu1nTovXWcUqJeTGwJI3V--geR1mgVNoNIKjV5KlHFnrMlOWeVSWuSHVL4enogOWxaDd1hhuEOrFpJ6Epaz75dJRJszepqTt1juxQ0FGXyaLqtC43ORJC-BGwrJaa0yvej8K0kQxWvj5vtxVC_mUEsRe2m49rwjQjkhKYhzZ2aqe1gP6vH_kQg1U_C5UPsgx9cCwydIW54Bvz8YudJh4y7ZbMvqJ_j-Gl5dYjk5gQ7_Jv5twSSk3XmK3LZrmguPIDZvK5qHVJylOCK-B7sKgxTnSNIaIPVu37FuF8yfsUrddERPG_xWmftsMU020Z4fpZD1ywCCwKQs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMXW8vcVRJcxzGGCjo4XGU-mjy4sfUWhsBUN_7933PSbUjPEva47xuf83cVjB727OeAVlKKZYtlQZ5YrLztvNrAQNzeP8dcGEjk4Tj-OK8G4VyhY0U7P-m2RjUMIUJFH3D7kDiiLCFo1rAi3lqoN_HfBKqc1vdJtHWTMSYt5MzvciPQ0C0egPaiktvLTvVKdFxeXO9ns6PoxXvP9KTeOPjWvs7ykoPvOVj-xi06NV1Zl1FKn8vnrNm17BsLKkDiafyNosBSY2NCoNk508IYZrUTi14j2MeJmg0f_S0Y2muc82CteTNg4MHwoAGZPhExAB6PYCHhF2LgubHay8onKuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kj9Gq26gw2CYpwWy8aCNmZxGi0kBIdCtlSDsBsx3RqoCRhGz81Skz8642E5GpYEss9L9ShsFE54w90nnFfWRW6qDaDbZhtkvNDebc1LHGab4Mii0pi24z8PjSugWbx0rY-whqhjR0uMmBzLErB2q_wUYlR9M8oMQouoR9RFpFd-hS4XyKMEJg3W02pzqNhL64HYqyxsVhfCtPutORbXZ_JJEfAOF6hg1PyVyoHnpAbbE5MEx2f9ddtfcXSCahHu2XqQpk9ZlLcrk_QdnwvElVvb4_bYpl16rnZSHhRXgkKImFT2X6hEX1pqn3w4hzLx2yqABwyxcI6dciYn6ydy3mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=CCv9kCH5mfQ0G0ZzPmloyEfzxNVBrIvB0lVRVilV-xkgFKCUARmE9fkgZsNbA9_wg4YJKuPLLBrJqVU25tk1CNOdygOIhFWZ_YJZGe311qoBpKDbHT_qHzMENjSN4MA9xSRcCawGDjsnYPL74i92YTgWWpvY_0XeYpSiKpSBoA7q3l5UoYZ0d53Fmhg7_8H4zZjMthTvbs8g_NdgCouDqPlPVAmIDImxexyIuDOY5ET0zlWM1ullqp2r6nENOiJTVCV0XRf3EAZMx29oq3FwtuonShd9tonie7OS6oqE_dDebiSa7KA2y_RzdN0niksBAxPSbfU0QAdM5A2J4a8CMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=CCv9kCH5mfQ0G0ZzPmloyEfzxNVBrIvB0lVRVilV-xkgFKCUARmE9fkgZsNbA9_wg4YJKuPLLBrJqVU25tk1CNOdygOIhFWZ_YJZGe311qoBpKDbHT_qHzMENjSN4MA9xSRcCawGDjsnYPL74i92YTgWWpvY_0XeYpSiKpSBoA7q3l5UoYZ0d53Fmhg7_8H4zZjMthTvbs8g_NdgCouDqPlPVAmIDImxexyIuDOY5ET0zlWM1ullqp2r6nENOiJTVCV0XRf3EAZMx29oq3FwtuonShd9tonie7OS6oqE_dDebiSa7KA2y_RzdN0niksBAxPSbfU0QAdM5A2J4a8CMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=HTlLok1HfmKwh0v56m1QcWzitFUHcUU_I4VKMFs1VUliUPpyx0Y7dNBqhqd2oK2sCbpJHGwwBXPfHeDhIncEFwJ8XwzujaGRqYpZg2i4LFElUNQ-6LymhsN-OGde9R6_-gXu2NS77ZOtkRkNTbExM2i0aJ5rMDjsttBEIVtMZk9BeJxMK8_4zZ02ETP7MN1BzHNkALZpJUIYmj5JUVj_20D4MpmdbuEIbqq6CLFw0erjvmB2bZPjN2tXjYN9CtQjItbw4Bk4DpDfvRaz5W1EEwQksU9ahj9KEAinAymoOTSfcXFi8dScBWSaC9-QUT8a7VcL3MaTUesLP6dHgicdyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=HTlLok1HfmKwh0v56m1QcWzitFUHcUU_I4VKMFs1VUliUPpyx0Y7dNBqhqd2oK2sCbpJHGwwBXPfHeDhIncEFwJ8XwzujaGRqYpZg2i4LFElUNQ-6LymhsN-OGde9R6_-gXu2NS77ZOtkRkNTbExM2i0aJ5rMDjsttBEIVtMZk9BeJxMK8_4zZ02ETP7MN1BzHNkALZpJUIYmj5JUVj_20D4MpmdbuEIbqq6CLFw0erjvmB2bZPjN2tXjYN9CtQjItbw4Bk4DpDfvRaz5W1EEwQksU9ahj9KEAinAymoOTSfcXFi8dScBWSaC9-QUT8a7VcL3MaTUesLP6dHgicdyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=rg0RG2IO6hSzWfW2xWhlk-xyPg6cMZKQBVJw4rzkeIcf3KFp95pVenrDGif30sJ5kFrigHt8LyeTwUi2DgjP9Ccdsutv53a5dpXmCcwqKp1Ms-TbM4fgwBRCe9SG0dNSyh33yvxjbO_7qr4Dyk7YYxZAk08BW4pfqSbaqrNK2JAnP54NS2BTfDKrV6n2x0Wki8k2ZXaM0us76Yp02rJG9IwPCkpGVCmmA9StjBFPZCFBUk9-c7Uk1EwZJG3lUXEtqMgiWljAsrY3BRW0wf-AIkvstIW60wPVBKJMpIMHStNUrp0jnhnzKXdu5ek_mA1jyZoRECYu5eNElBfjagseqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=rg0RG2IO6hSzWfW2xWhlk-xyPg6cMZKQBVJw4rzkeIcf3KFp95pVenrDGif30sJ5kFrigHt8LyeTwUi2DgjP9Ccdsutv53a5dpXmCcwqKp1Ms-TbM4fgwBRCe9SG0dNSyh33yvxjbO_7qr4Dyk7YYxZAk08BW4pfqSbaqrNK2JAnP54NS2BTfDKrV6n2x0Wki8k2ZXaM0us76Yp02rJG9IwPCkpGVCmmA9StjBFPZCFBUk9-c7Uk1EwZJG3lUXEtqMgiWljAsrY3BRW0wf-AIkvstIW60wPVBKJMpIMHStNUrp0jnhnzKXdu5ek_mA1jyZoRECYu5eNElBfjagseqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو :
«نصرالله، دو سال پیش هنوز در پناهگاهش نشسته بود. الان کجاست؟ با من تکرار کنید: پررررر!
و سنوار کجاست؟
پررررر!
و ضیف کجاست؟
پرررر!
و هنیه کجاست؟
پررررر!
و با خامنه‌ای چه کردیم؟
پرررر!
«سران ترور را یکی پس از دیگری هدف قرار دادیم.»</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqE2gJuDRY02CAiAQkIJDd32335JsiKpAeFF3WfHDVRR4I4u4i3ey1TuQ9aJPIwEeYzQgoN68gbfP2I-iHd-6EwOmw5R0OMZDnxwlBkHoNWlwBdW4HNzwbljIhHZBf7Jm8uX7z08xXYCqW4nphEAIJ95rCnikcSgZaplZRc4YahkTIS6SzT-F5BBWvujPuo6mI34bIw9GsyisyzcmffANEnAT_wohOmcOH3oNg8S3WBkfrBl4AtDJYe4pUemuxkAG_PCUSs9OlLoVKX4gDiDptzU7hCYsZjKLSvK8FcgKTKs3mYrGnXEwLcvUk5FJVeaWyAP2mBbc3SuvZ1kCL1hsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=EfWAXC3-4Yvhj3Lxg0J3N7lrRB-cK4iZ3MJNILpdLfYokVh2EZ0y2k_Z_uAnLFKa5I3TvlBhm6iIigLl-VwPojnUogzOTMuhWTCmXEQkQuGbrQrkAwxv4mggbz59kXYoa1nhg6N5k0f7WJmArpP8tDzyZaDh7Gbw4MYsvQqHmyKF40JeGADugs9W8z_nYCZHSC4mHV5OHwRBZ6y1FuLCj_5uvcv9fmdrlNy_IvztYktNgnkJK5sg4pxdGJ3EzRrgilnr7jfjBZMohAtfpyebx_NcjAXBnpDDaqEVyLiJfT1_ymO3w1id-d-WAxy5aD_lVcCTdPhHkRRnftDzRUBroxFIrp8XVA6wS13vzb87xsaFmhLFpUV4WecVwncEOpLJooTrE8zCcB7-d3EEuClwmFFRFj8sUCUPqt1Zty4C0rd2AxKMubd_Q3WYGDIQH7pXEgKD6rYNlsr5h2ULHpMgkilMdXOK9kzD40EvUuGkvbUDwQHRl2NE7MInPiJ3uGlM4NgIrKIwxCH3yEQegrEYfYTv77no58VzSH1D3YXNsSt50C0z1vIJdTNdHqKU72m4VCSmB64YcfXYReBkgbMBkPU0EMurn8WLPICjAuwnWOFPEM4suqIAEqkQ3-xaaKPXzMLYk4WOpU8Q6jugaQrFMRkwsnA7FlNo_WRGfpPrJ_U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=EfWAXC3-4Yvhj3Lxg0J3N7lrRB-cK4iZ3MJNILpdLfYokVh2EZ0y2k_Z_uAnLFKa5I3TvlBhm6iIigLl-VwPojnUogzOTMuhWTCmXEQkQuGbrQrkAwxv4mggbz59kXYoa1nhg6N5k0f7WJmArpP8tDzyZaDh7Gbw4MYsvQqHmyKF40JeGADugs9W8z_nYCZHSC4mHV5OHwRBZ6y1FuLCj_5uvcv9fmdrlNy_IvztYktNgnkJK5sg4pxdGJ3EzRrgilnr7jfjBZMohAtfpyebx_NcjAXBnpDDaqEVyLiJfT1_ymO3w1id-d-WAxy5aD_lVcCTdPhHkRRnftDzRUBroxFIrp8XVA6wS13vzb87xsaFmhLFpUV4WecVwncEOpLJooTrE8zCcB7-d3EEuClwmFFRFj8sUCUPqt1Zty4C0rd2AxKMubd_Q3WYGDIQH7pXEgKD6rYNlsr5h2ULHpMgkilMdXOK9kzD40EvUuGkvbUDwQHRl2NE7MInPiJ3uGlM4NgIrKIwxCH3yEQegrEYfYTv77no58VzSH1D3YXNsSt50C0z1vIJdTNdHqKU72m4VCSmB64YcfXYReBkgbMBkPU0EMurn8WLPICjAuwnWOFPEM4suqIAEqkQ3-xaaKPXzMLYk4WOpU8Q6jugaQrFMRkwsnA7FlNo_WRGfpPrJ_U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=K9VWl4hcAQLJ6nOFUAcL_pCjZqvp4n-QrhCxlX5tc-VQU0HTu9H7abLF-rTFOy6Bi3Dj82vTAC89bNgWV3q7nquHTO9z3bM4uuxgf17izf23pwMiPp8cN_2Q3Xj6fObpL0XcXR7Y6TNzCxKu84lNptW1jvjRSo4Oo-qDAzctJMuf9RcQ9LgnDq9q8Ampy9fRbdcMOHnPRfuthSonv9lYGRv2RXgfiT42ZG5cLolRdgoI17gxQ-EVw5VjKmjhKzZB0d0GrG05nnpkdKFaQxmH0EfMe6BLaTFj0quDKBVKDEaOd2sBKN7BMplAICf5AmFBX9NRMZqjNNaDbzTT9UgD-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=K9VWl4hcAQLJ6nOFUAcL_pCjZqvp4n-QrhCxlX5tc-VQU0HTu9H7abLF-rTFOy6Bi3Dj82vTAC89bNgWV3q7nquHTO9z3bM4uuxgf17izf23pwMiPp8cN_2Q3Xj6fObpL0XcXR7Y6TNzCxKu84lNptW1jvjRSo4Oo-qDAzctJMuf9RcQ9LgnDq9q8Ampy9fRbdcMOHnPRfuthSonv9lYGRv2RXgfiT42ZG5cLolRdgoI17gxQ-EVw5VjKmjhKzZB0d0GrG05nnpkdKFaQxmH0EfMe6BLaTFj0quDKBVKDEaOd2sBKN7BMplAICf5AmFBX9NRMZqjNNaDbzTT9UgD-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhc-zuwaWjHOzXt7m7Zwoscsd7eRUqZET7gBmZg8GU-U0uLlJua6wBwip8jmTGytPwGTIKA6TC0zn8hgGYIEOEVYUcP5dTDFdikCA3e5Qz0kkIbiwmBFrdiCw2PovMVMKwqlzlSdPXPR9Rm_K64wI0gONg3XabCR5E62Hz2XPgS64V7NTcuErDf8-JavSYUrOxf2w2451DDg6XQEjhtOkItjNY7GtDWaxxvR-PqK48_XLYFT-5EB6m8vi3RK1DqvcWeLC3l4mMTrJBUcW8qhAVXXurwoRGuU5IFpXCGnnL06WSVmdH9juPVeNG6cNBSZUHhTsfbnVhl3VLzcALC4AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=GhL3w4UOhAY5fvlcACJtBc2kE3wVmSuqKsbsSn5O-HivqY0sg16Z4HBr3sMQsNfl7amQzT2qDXgl-tl708gktk89bnlIIVNe29_40DlYlnZ9RRgtgfz5UUx-Dh0xK-PGmVtbNRaaFGVgbJDAsFCFctXn76EkQoSuN-uaKgExbPtVcBYtR4Px9_8Kz7l_NTmm4YLOtSF2W4OpaQPZgOP9yxqiBz0npdDQ239D-_KLoa3VuwphYUyc7fuPJmSbKM7Ak3jseaVrCjRCmojaP6rhlmvXGq9f960w3-pNDq49PKmQQkyw_oIa7BJYhhxwyiWW9ftLkYm3-2Y3Q6vTP9N-4Zcy4ILoTucATD2WaN89vFCDCUl5bFdVG1pjeRVRZhx1tOknRIIU6P98h5-UlaEYPcKoC3ePJpO6jh4mzi1o3TuyWxF5Yd_Z13xIKeS2AtAYNyqgYUErdk8Jf1LYnk-Kta4QdF6dFe8KVWtsqLRogShvcadz4wK9vEb-njIEOS6aayGXbJde1b2-azRu1VEHijtcL27a4RhYtI5VfR7dJVQolFEjeCc3yA8VyjUDwNwwW7q4_rR2p2dOVQ0wn01T3ihH2s8fCy12y6UZVVnfhqAO9BX1vatwSplq7hEnQIkSHN2c1jTrNeh0K29pJSqxZii5l3Iops4nkuBqLugR0cI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=GhL3w4UOhAY5fvlcACJtBc2kE3wVmSuqKsbsSn5O-HivqY0sg16Z4HBr3sMQsNfl7amQzT2qDXgl-tl708gktk89bnlIIVNe29_40DlYlnZ9RRgtgfz5UUx-Dh0xK-PGmVtbNRaaFGVgbJDAsFCFctXn76EkQoSuN-uaKgExbPtVcBYtR4Px9_8Kz7l_NTmm4YLOtSF2W4OpaQPZgOP9yxqiBz0npdDQ239D-_KLoa3VuwphYUyc7fuPJmSbKM7Ak3jseaVrCjRCmojaP6rhlmvXGq9f960w3-pNDq49PKmQQkyw_oIa7BJYhhxwyiWW9ftLkYm3-2Y3Q6vTP9N-4Zcy4ILoTucATD2WaN89vFCDCUl5bFdVG1pjeRVRZhx1tOknRIIU6P98h5-UlaEYPcKoC3ePJpO6jh4mzi1o3TuyWxF5Yd_Z13xIKeS2AtAYNyqgYUErdk8Jf1LYnk-Kta4QdF6dFe8KVWtsqLRogShvcadz4wK9vEb-njIEOS6aayGXbJde1b2-azRu1VEHijtcL27a4RhYtI5VfR7dJVQolFEjeCc3yA8VyjUDwNwwW7q4_rR2p2dOVQ0wn01T3ihH2s8fCy12y6UZVVnfhqAO9BX1vatwSplq7hEnQIkSHN2c1jTrNeh0K29pJSqxZii5l3Iops4nkuBqLugR0cI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzE_jMKcsQNmsjrtU3CxQAqjZ1QlC_AWCPbIi-J2b9UH9bNKXTBBVt_dpHc0g-xRoIYoQA0LYtFlXcaTkVs291KMr7t8M72tvbBVm9sS_-fsk-Ro9l-RwYe4rUeWHn9nUr7sXHlMykrlMhSJBwhK94iVM2WiFDbcPpvuOvDw2eHEBjYZhumpm9EAWf2TmdQkxIfQQ6kDFBa9A7OFkqN_5_zASDUdYP4S-fUhephGuapI1c9h43NlF1wVF-nmThXL1E0no52JpzxUzKNzPiM2QXFA8CwBcuAXcN3L0gWGe5Acds5zSPsikOYUvx_U5QPAMvzNa0dwVYYE6-6VztU4jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی این روزها
برای عروسی در یمن شیرینی میدن،
۳ سال پیش برای عروسی
در غزه شیرینی میدادن،
پارسال برای جنوب لبنان!
عروسی‌هاتون و پیروزی‌هاتون پی در پی
✌🏼
۲ میلیون اهالی غزه سه ساله زیر چادر هستن
۶۰۰ هزار شیعه لبنانی ۵ ماهه
توی توالت‌ها و گاراژهای محله‌های مسیحی و سنی پناه گرفتن!  پیروزی‌هاتون پر تکرار!</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=RSBXpH6sbUq13_drzGPq3ZgAqJHqLUSqCpFxtywgqM_bwSicKA8S4pXdKNrhO1wm2ZIAd9aDOzCcBtNxdyn64z-c7FrKsxGqwkZ7HdNF4_tlW9HsCYYulHLBykt30oi_FMhJeEVEUxBkL5lZkt14fFeMrJgVnVWequy7Uw_8bFIenvS9hzNCTm3O3UHC88O5tH1nW7fmq_fC7gc29fnYynMQZjIGHQQumkkMETltQsiZwVKmwBwzzLc3Bj6aBPH4_6IBiymykK3a2J29xBWLglRWIVTT9TAGMlh9fYWafUkaKKv2FRIlGU-1R6ilKUyhWVD_scANmeeZU5iNIW7f2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=RSBXpH6sbUq13_drzGPq3ZgAqJHqLUSqCpFxtywgqM_bwSicKA8S4pXdKNrhO1wm2ZIAd9aDOzCcBtNxdyn64z-c7FrKsxGqwkZ7HdNF4_tlW9HsCYYulHLBykt30oi_FMhJeEVEUxBkL5lZkt14fFeMrJgVnVWequy7Uw_8bFIenvS9hzNCTm3O3UHC88O5tH1nW7fmq_fC7gc29fnYynMQZjIGHQQumkkMETltQsiZwVKmwBwzzLc3Bj6aBPH4_6IBiymykK3a2J29xBWLglRWIVTT9TAGMlh9fYWafUkaKKv2FRIlGU-1R6ilKUyhWVD_scANmeeZU5iNIW7f2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMTksy7Nb0TvRzZqxtMglUmME8Wh6GiJgXUvsvqST0WTydarWbK_5eMBeDDUo9Oc45PW0q2odO9NY-i8v7nYHBG1iDEniw-BIoBAt85JLN9_wc2Y29iRtRWhM0Mz6z8KFuPDSn-rnXJupHjzyngXLmkBv0jVo9F4ikLLnt9zq7XrHdxNsPlfVl7Hl5W_JsdZbrANgPgivnZVRh_Q9ocB7Ff9IyCEArFuzhLLb6F-3546DT_o-8g-SrHyBh8ggZ70htlv3RMg_1LinLmfh-Wwoc2ATX-JzBY1jLoTqr3R-Cvk5i9gRP_XddW1b-7wg6EdZhmU_81uhN7BEv8AtZd_bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiFhftvHXiCLPjdYl3QyEjPDGeV5pzKDMcmcME3lgjNrlWaPloR3Q3fR9yji84-bCYYqX6aW507Vp1QT9hx3XatF8sBRqsENZ5nUE7YRA9Sbm3DIqTL8_bEyRIJqyLkaUdTIiQ2bpiLtZMLswkA689Y5cRhn3BQShDQF_74QKquXzdJ07B-NkHh7Xvn9yi6gqnuCEwCoMYCx3eJHk-58TxW0WhkXEEQNZbktzrAuAy4XXZUY0g9Vh0Kc8qAgCSkrSD_FvQFBSXsdBjY9BWuiPzsHHizs3p7Gnb2apaJFaOPFlycbo_yLp0aly7tiBd-aIkDZ8AvJqpFuijR8jxpVvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PiZ1p7cTqT7doHzW9G5-R_1fUAl-9Ty9QbOuNQ8xixc0Axfkhe7hXQcn93cgC-hZg0QJ6qFcYf2chHIvkTaiwoMkm6tr8QdYZ6_dksXq110faDEXcm48nfeeMYiHbr8EQhVrMaA2ydH8vtmnnAaESW9qhckO3no_0kbVzvsdJKVlNXRWsazzoNpYOofTtoMXpUPHdCQ-K2v_hX3T6xxFuD1153ZseD_5W69f1UTrmCq809qLDoZ9ShcRN5y4kUrAn5F2MVOgGC6fIuUN-me-K8B4dkdGMugGpgFRstiSaIAPMwc0EPFWxzReVv3jViXzeQvkiTREETg0zVUDGKrasw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=CeqyMqEcMvIy-1DQd1xW_MBQO5pr7yryDOBgoWPeMW9BKKgh3SAnjkYyrO-sIWF-Pv27LxfD-MNAxqskyx2PGTy6hXI6q8DJGF4oucYj5656b1NZfBAu4zhJNSKnaUyPbRFGGbw0Bzu_PUwnej-UJABN-kjD1dpmBMZQefNgnr-DW3-hMh4hVyj2EX2ahfRABvvhX9seLXVI3Ug1bDcPN1xi2USp0tfUMM_Eg8etesx-QIjhGmwVB2WdbpjuaQX9FVDJm-vNdk2z9UYx9ac9Ngs_AUF0ErEF5yg2fEIocWFAYyQIa0RiGwFmcDywvpP3IWv2saR8gWO0EnwPzJl0Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=CeqyMqEcMvIy-1DQd1xW_MBQO5pr7yryDOBgoWPeMW9BKKgh3SAnjkYyrO-sIWF-Pv27LxfD-MNAxqskyx2PGTy6hXI6q8DJGF4oucYj5656b1NZfBAu4zhJNSKnaUyPbRFGGbw0Bzu_PUwnej-UJABN-kjD1dpmBMZQefNgnr-DW3-hMh4hVyj2EX2ahfRABvvhX9seLXVI3Ug1bDcPN1xi2USp0tfUMM_Eg8etesx-QIjhGmwVB2WdbpjuaQX9FVDJm-vNdk2z9UYx9ac9Ngs_AUF0ErEF5yg2fEIocWFAYyQIa0RiGwFmcDywvpP3IWv2saR8gWO0EnwPzJl0Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrNcE5-ljmg6yM9LMGbTTJpfFL1PSRGh0ERbvG9gW-mC-JTGNQb3u9hlP80kGbKVM7Tq6IH0G1zTGpDyzYp7g168Pu70GMrGMkFHzSI8hzYd6CXSRItdtD38rfOtJN04FvBR2XJSv2p3-kZpGYZL7fcrSwJjJY79FIl4jndb5UtaskZEgRVJUnJOpDGT3WUY8VV467QJHZ4PnIwQI6-sIiVGmt9BEHM7a7lMUTDmQqOAgd9XdPVm5xQd5WcLsFRzJ_2DeXSyF8dq1fD9rGtECqtv0IWfiQxRGUOR-QdhueCRHdLe6qZKpOn-sBJfuEPW0-U0VELi5kSiLykkgktk6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=ngcFTQTvxuoQfUrDutcjYcKZffNOkgkpsP-BdNILgwKsRjzwCQ6XSq5GaFXhXn0ElqgtYb64z3LvdxIC1Gd3COObywVDJiti89knzBQot5dl0lyqeNF7-F7Lh5BzIhaaVA4irAfuQ8-4oH5eAnCdquDWboweXGukPhtB-Jo7TigSSWj2c313k8U9vILbzMQ4Qdz3foaZQzqqCVX3wyJ2-0MTb5NDejwncmqItAe6rUe525C98yiqxRZZFYHqFHVN9MrDE_RKObPluBJ-FvSRQp3o4rrwR33DcOgtMdg18c7MnlNOdUIsC0BNEwPyQOgoXWZuLZoI4DWe4cdFXAzp6aznYneD8TZ2Mxj3az2GrlOiwLwVAukqHGQ66tp2O75gz8WU7kSo3f4SJQi8oKW1HVDWuqYoRof00sZt1_sMlP1zA5eYP6m4nyesKuQvII2oQzab6bTDYueEB5kFLRnTP77xWrKHukcv9faTIiMWFq35HI7o0Ubv4gIlUe9TrW964kQQN6ofMEKvrUUcxJEJ_2Fq3ZfO1Vn_pCDEBhcxwE3ukg_vztg3-DdrT6vlHXqFbHNk8HzHtzX1PBsQOQP_LpDQUVLje6ojz0iCQ7fn_4xHa785IzCO_zuWGZ9C3fjz6BV0VIIx_h-IfC6vgIaQmk-3ISTm2LmD3NtMfRPaN3I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=ngcFTQTvxuoQfUrDutcjYcKZffNOkgkpsP-BdNILgwKsRjzwCQ6XSq5GaFXhXn0ElqgtYb64z3LvdxIC1Gd3COObywVDJiti89knzBQot5dl0lyqeNF7-F7Lh5BzIhaaVA4irAfuQ8-4oH5eAnCdquDWboweXGukPhtB-Jo7TigSSWj2c313k8U9vILbzMQ4Qdz3foaZQzqqCVX3wyJ2-0MTb5NDejwncmqItAe6rUe525C98yiqxRZZFYHqFHVN9MrDE_RKObPluBJ-FvSRQp3o4rrwR33DcOgtMdg18c7MnlNOdUIsC0BNEwPyQOgoXWZuLZoI4DWe4cdFXAzp6aznYneD8TZ2Mxj3az2GrlOiwLwVAukqHGQ66tp2O75gz8WU7kSo3f4SJQi8oKW1HVDWuqYoRof00sZt1_sMlP1zA5eYP6m4nyesKuQvII2oQzab6bTDYueEB5kFLRnTP77xWrKHukcv9faTIiMWFq35HI7o0Ubv4gIlUe9TrW964kQQN6ofMEKvrUUcxJEJ_2Fq3ZfO1Vn_pCDEBhcxwE3ukg_vztg3-DdrT6vlHXqFbHNk8HzHtzX1PBsQOQP_LpDQUVLje6ojz0iCQ7fn_4xHa785IzCO_zuWGZ9C3fjz6BV0VIIx_h-IfC6vgIaQmk-3ISTm2LmD3NtMfRPaN3I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=mFvgKe_wZAALEypIuUjQK_-Dcb9eoxa7w1n-2QxNXJRu4o8z-tDcjc22fL0gYdhxEcVIigTmATMbfTtPFyDTkgZIFUYyq37ywec22QvA-CB8cULESYKIWiZHV0tqRMgLgMf9S-HEJmDa7W7Hd7Ub0kZX40C7WkURtZAhBfM1FocT6K7tqE5tRgL6tCibK6yU7aGDxK_cYJFygmKuSjdMviDf6fiZH3TH3qisg1W01Jh3PlilKTOx1tWP-aN6fCbp9ayBObZsEjszUOkQ0bPeHOGlE4NKbBgZfUer-jlU43OHscCv8lYocu0vqF46cpvIv7MNgpaZpL06v7e2KseJ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=mFvgKe_wZAALEypIuUjQK_-Dcb9eoxa7w1n-2QxNXJRu4o8z-tDcjc22fL0gYdhxEcVIigTmATMbfTtPFyDTkgZIFUYyq37ywec22QvA-CB8cULESYKIWiZHV0tqRMgLgMf9S-HEJmDa7W7Hd7Ub0kZX40C7WkURtZAhBfM1FocT6K7tqE5tRgL6tCibK6yU7aGDxK_cYJFygmKuSjdMviDf6fiZH3TH3qisg1W01Jh3PlilKTOx1tWP-aN6fCbp9ayBObZsEjszUOkQ0bPeHOGlE4NKbBgZfUer-jlU43OHscCv8lYocu0vqF46cpvIv7MNgpaZpL06v7e2KseJ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=jTa4PKMyFBM4SG1VSo5Psrh46ApAUJqfJvvNwl3IHKkyv-4i8kI1o_jR2vblf-yhvQAvuMm14hKwXcUcipCqNmIi8oPqWmmoCDLCy_ujpr0l9m2pjyQtxoJJMTzSDBPXx112Z8HIZFFDv1ZYT_ye4r1v-3kvXWv_tuKn-oiSJH8U4M6NnVOruBzmReVlfgGpy_pWwNJQY32ueqKAigHl0Gr_qr9Wp9r5SeHnsZ_lrOC3s0qyV8XH1lbwcw_KzAM8oMcTezk7tKLmJNrZ_0JbC6v92FyEqSYSzEgHzhVm3Hu_2Lo52Obi9J-CY9DWHMu0T0YsxYeLx8ukJdoqcxZUPbdSTGBmgxfpBLmUCVl3KmrFLhsbIrJcSiD8hBfysYWNxXbpz6R1kUVdGEfhdROgJFJGaFTlrMK2b9d7wjmgCwCxUzB75PZULLzHHYFiouz9c5IGfcJw5XQOrdOcAZ2Y-3q19C5Zh6Yu9HQfov3jG1gDEaVSlq-3trGI-gSPvrOnjQiIeaIxS6ou8EgWb3FExsHHttEVqIKLN-os8cTykrNp5K0GkBZFL1MZW1mWmVoVjSfyNNjoeT9lhGYU4LRlnCc9LKFY9YE_V-pHifcnMyGPumwkBHgBUDMNTr1Co_Kofs3eok7tBOG1AIPT8l3r5KJNR7MlADF6ar1n8lc8O3U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=jTa4PKMyFBM4SG1VSo5Psrh46ApAUJqfJvvNwl3IHKkyv-4i8kI1o_jR2vblf-yhvQAvuMm14hKwXcUcipCqNmIi8oPqWmmoCDLCy_ujpr0l9m2pjyQtxoJJMTzSDBPXx112Z8HIZFFDv1ZYT_ye4r1v-3kvXWv_tuKn-oiSJH8U4M6NnVOruBzmReVlfgGpy_pWwNJQY32ueqKAigHl0Gr_qr9Wp9r5SeHnsZ_lrOC3s0qyV8XH1lbwcw_KzAM8oMcTezk7tKLmJNrZ_0JbC6v92FyEqSYSzEgHzhVm3Hu_2Lo52Obi9J-CY9DWHMu0T0YsxYeLx8ukJdoqcxZUPbdSTGBmgxfpBLmUCVl3KmrFLhsbIrJcSiD8hBfysYWNxXbpz6R1kUVdGEfhdROgJFJGaFTlrMK2b9d7wjmgCwCxUzB75PZULLzHHYFiouz9c5IGfcJw5XQOrdOcAZ2Y-3q19C5Zh6Yu9HQfov3jG1gDEaVSlq-3trGI-gSPvrOnjQiIeaIxS6ou8EgWb3FExsHHttEVqIKLN-os8cTykrNp5K0GkBZFL1MZW1mWmVoVjSfyNNjoeT9lhGYU4LRlnCc9LKFY9YE_V-pHifcnMyGPumwkBHgBUDMNTr1Co_Kofs3eok7tBOG1AIPT8l3r5KJNR7MlADF6ar1n8lc8O3U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=FD4gvP9blIhgss4GPd1lCPpuamAQ-rwI29k9OIDzpxk7OjL83rLQS1zB8LS7_ZWsCZFo0Go6YBmLHXwecRQ2Ti9SknDGWWgB6oCBkSfU6jx4exfGyCXRz3Jf40dNK5KRxfv8I3IkZSS4VxlCUkmGucLcHjv9ILos_2SMsodtpsYyQTqn45p07bTI2xw8TGJzNiHImMUHyefVP5jqvLt5e-DRB1IrVeGIIF3O5deKlmZ1KixEbMocX-da_lE59XYwMFfBB_A7OYWSvTnymr4T8SN1KVofKrHibMhdhi699XWpsNSqa1xqKRpkqXeU7v5Z_i1n8dIcsa6rCB_Z9AvW-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=FD4gvP9blIhgss4GPd1lCPpuamAQ-rwI29k9OIDzpxk7OjL83rLQS1zB8LS7_ZWsCZFo0Go6YBmLHXwecRQ2Ti9SknDGWWgB6oCBkSfU6jx4exfGyCXRz3Jf40dNK5KRxfv8I3IkZSS4VxlCUkmGucLcHjv9ILos_2SMsodtpsYyQTqn45p07bTI2xw8TGJzNiHImMUHyefVP5jqvLt5e-DRB1IrVeGIIF3O5deKlmZ1KixEbMocX-da_lE59XYwMFfBB_A7OYWSvTnymr4T8SN1KVofKrHibMhdhi699XWpsNSqa1xqKRpkqXeU7v5Z_i1n8dIcsa6rCB_Z9AvW-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYAzGEOTl9isEbqfkY2kubUFlZDFEK_ezv6i9EqZsvdBvh9-2sovAKWRrzq_uhAyDk-2PzGeBdA975UyzAE5JP9JVt9QJh7V4evnKWeKLV4TQnwIBy_8_L0RX-C7OSP7ITXpn8ToAg86asDO3izboTHl6bUj9eh73j1QyC2BeH4yhWL92ou9uBtAvv22NGFff8cCADbnbqfD7m-GAj3KmiNWPPZptlMFNHOFPbDCXhldaxqmQE3Cvzrk3vozNpXzY3_NAWTq8neQgTK3z7opjPO1j6UoqHfwbBg84mJbHEj3iCwIYzFC1PssPERMkn5mukQZpLa2ArLPFNYSMhdoAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=ds9ZrkB4q0RjWFjbC_D8EKbcWx5tQDG-9SpvWPaQfEbo9ICb0WWei3P0x2H7wJA1gcthfQHJ9pKtT7B6PyAflSf8e3cVXNtIOHqmiPreYqfExdRb0XQi2eHmzQkkyiYAZBHGBjK19capB-fE-hODzdJA1p1CCxUe3DRxcVivG4badzoXWGVGDKAx8WWJtgcKf0t-XUiWo4wAibUz1mknEmwMzKapaNclWwIzxUfCpoyK_yavJqLYebzLPYibPFe75IvJqL2iySKDT2a2TG2wAynBIWAqerwlM8lmQekWWqDtRa4Cet4-wrXyaDgbPjqEMWv9jstcmCsLE1rwcWVK8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=ds9ZrkB4q0RjWFjbC_D8EKbcWx5tQDG-9SpvWPaQfEbo9ICb0WWei3P0x2H7wJA1gcthfQHJ9pKtT7B6PyAflSf8e3cVXNtIOHqmiPreYqfExdRb0XQi2eHmzQkkyiYAZBHGBjK19capB-fE-hODzdJA1p1CCxUe3DRxcVivG4badzoXWGVGDKAx8WWJtgcKf0t-XUiWo4wAibUz1mknEmwMzKapaNclWwIzxUfCpoyK_yavJqLYebzLPYibPFe75IvJqL2iySKDT2a2TG2wAynBIWAqerwlM8lmQekWWqDtRa4Cet4-wrXyaDgbPjqEMWv9jstcmCsLE1rwcWVK8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=PNuunoLSwbcu0rDxPeGsqaK2Ya9w-R0FT0UgYgXyaMb1Py1TT38sBgGB9ibaKkOto2cT2PDrItQJyOrLz97iT0-qS5xCesAI_XGUSB5BXRQkCAt8RMqlAR8apoXiqWmRn4SLklLjc8_UkR4JnMegNhBsNUkIp3uvVxJEKKda0N6w6SmWFf3ViQMQxQ-YhJwaD9oKpFvj_yk-iCzKCftHGqOrqKciQhPGirTnP1twgFfw30C8h9O_iJhItIGjYxBscOkD4nCXbwnj6Fk87PpdxyeOuQ_pUQUyOPXoRzT4JRB6uJ2HTz3FLj0OTaYKs-zB9O65kpoKeN91lbVJTukEj7z7-xP0YQgPyvOz4ZDIyyu4dOGYIkKL5U69Li4Ny6gfWYrO7UuTy28FuhTxkQLBMA3Jm4fI8kQv4GHN_GuX59HLg1jP_6T9KXN3f6KkGtVN6F7p19Y0VvBe-jOPMpPzz8KB0Yb7CL5mWfGzH8MkZVAu8qD5IkaQZe8O2bkDoURWx7GicC96ykBdbVSPhMc5cShr4v6r3TYGCb6Z_YJzbNZx95lRABPa-mxiB5EUkPee7YBq3aFdccVGvzdOdK_GerR1gGQOXIxsZVJJsfjZydREASCL_9P_UXXUUkYod0Gz5rjnyQwcSLF9s-BykhM-xixEXZVmKOdfnrlfTptmy5o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=PNuunoLSwbcu0rDxPeGsqaK2Ya9w-R0FT0UgYgXyaMb1Py1TT38sBgGB9ibaKkOto2cT2PDrItQJyOrLz97iT0-qS5xCesAI_XGUSB5BXRQkCAt8RMqlAR8apoXiqWmRn4SLklLjc8_UkR4JnMegNhBsNUkIp3uvVxJEKKda0N6w6SmWFf3ViQMQxQ-YhJwaD9oKpFvj_yk-iCzKCftHGqOrqKciQhPGirTnP1twgFfw30C8h9O_iJhItIGjYxBscOkD4nCXbwnj6Fk87PpdxyeOuQ_pUQUyOPXoRzT4JRB6uJ2HTz3FLj0OTaYKs-zB9O65kpoKeN91lbVJTukEj7z7-xP0YQgPyvOz4ZDIyyu4dOGYIkKL5U69Li4Ny6gfWYrO7UuTy28FuhTxkQLBMA3Jm4fI8kQv4GHN_GuX59HLg1jP_6T9KXN3f6KkGtVN6F7p19Y0VvBe-jOPMpPzz8KB0Yb7CL5mWfGzH8MkZVAu8qD5IkaQZe8O2bkDoURWx7GicC96ykBdbVSPhMc5cShr4v6r3TYGCb6Z_YJzbNZx95lRABPa-mxiB5EUkPee7YBq3aFdccVGvzdOdK_GerR1gGQOXIxsZVJJsfjZydREASCL_9P_UXXUUkYod0Gz5rjnyQwcSLF9s-BykhM-xixEXZVmKOdfnrlfTptmy5o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gySKKBo0NDtJYRzdM7zV5XELKenPxLNUiCbR8QnXp8vDh5LX8NJdSYL5L-NjkuCAh-LKANEi_H80vjBudHJxk1k1jcR1ANa-sW6rjEcU0UAAEYOWeEoAF_Gs02GjGFhuQJzjRvO2W4dchfHXvkLYWelEmhIVnEfiMtcTDhFnqRZjMG6Mu1U8fi34P-c5fwdbsPT5L9D49n_qds6UwUz_8pmfFYPeS9wjTg46P4dJzriOYsEJZ2RQNebenKGxUChegvbk7ilbefSL9tSWgVmi1CvyGv56fbcWb6mn3qKAvIUFUJKp28xzgVKgglQX6Ro_vcM0gQ1xThWz2CzRObE6kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=cHAxBYsmtJQtFeljbUB6O--AA2Rbv7gXSV1qtrWIbsCEvLpiuhYw-vFfYDpraSMznyhFstweAC_4I13S2rJbP9uHYuGB7rZNQAxAohCMnGxqIjCFNDS6yNZZy6ZrO8STD0_4dAeta2rPpVcGeXiM5TjP5PZhED_IpbI9WXIvmV2uRPz56gzzcfIrZcvfozom29khN7tuac49cQ9GhFTc7UC_ahg5VU-vYup-Wl2S4HA5MVCL52uPNtaA5-9jSEoq1j5EVpJx0NwQAcEtictxycA1ZjXvyyVM7e8QNnWB4jxeq-eGi4IYG-KKZqgh0U2Z9usQV9nYJjd6VbPJdnCAM7sdc3fjo0o-fIvttl5_CHUPumjreiszwGowd4CuYyq9htnNhUgR9xP9VPSfmB-M-DD03YckNOGZnwZ7pbdFdftGjOlSY_MjDQ7PtgQTMTfRCpci4bR5g30Acm5tirn9GS3wZKckag3cpPpXrkF3fmgsunqbQwXK7Fw1DQbAdlvBLny11L46slxeBg3i15ToEhIVhd5Sz4Tvyqevdxe65DbN58YBd8e1tYyZmYuHNAaxJ0hCllD4lO_VqM34q4XqLxKKfIW_DTPjyEmCUqWoHEX2F_HKaQeAmM4jnyks9iyD3ec_Hj4aZNO5AnOsL4Ijyot7SDh_4f2DK4fXDgmPqow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=cHAxBYsmtJQtFeljbUB6O--AA2Rbv7gXSV1qtrWIbsCEvLpiuhYw-vFfYDpraSMznyhFstweAC_4I13S2rJbP9uHYuGB7rZNQAxAohCMnGxqIjCFNDS6yNZZy6ZrO8STD0_4dAeta2rPpVcGeXiM5TjP5PZhED_IpbI9WXIvmV2uRPz56gzzcfIrZcvfozom29khN7tuac49cQ9GhFTc7UC_ahg5VU-vYup-Wl2S4HA5MVCL52uPNtaA5-9jSEoq1j5EVpJx0NwQAcEtictxycA1ZjXvyyVM7e8QNnWB4jxeq-eGi4IYG-KKZqgh0U2Z9usQV9nYJjd6VbPJdnCAM7sdc3fjo0o-fIvttl5_CHUPumjreiszwGowd4CuYyq9htnNhUgR9xP9VPSfmB-M-DD03YckNOGZnwZ7pbdFdftGjOlSY_MjDQ7PtgQTMTfRCpci4bR5g30Acm5tirn9GS3wZKckag3cpPpXrkF3fmgsunqbQwXK7Fw1DQbAdlvBLny11L46slxeBg3i15ToEhIVhd5Sz4Tvyqevdxe65DbN58YBd8e1tYyZmYuHNAaxJ0hCllD4lO_VqM34q4XqLxKKfIW_DTPjyEmCUqWoHEX2F_HKaQeAmM4jnyks9iyD3ec_Hj4aZNO5AnOsL4Ijyot7SDh_4f2DK4fXDgmPqow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=CWSzbqHBi-GqGeyvAabMEukkcZamJVz_f4VKDk9E-uLe_nN-7wOMql_AYfxZdWAFdKMhZ8ZvF6ZBFCWBw_mWhH3Nq8SRbM1cIHhU0UragTU_PA3ThcUMJfWgXYV6bDiyM2gZU6zZLjDrDQmITmRi3cLiY7xZUhJigekqE62J9eZazyGbXYPUY3SIxjfP3b-N5wkRZqrDrhS5l6FWwRSRGhiE0HywwSGi619-SdMJw7aN07TkHSFVqhUL_2hLf1hGowhIm06mb9BkGAdlRpvR8X2YSxcNEnTnF3cQMIgIRiJnXtMAsCvJPYONXUVnJ4INJwsXdLZi93Wqmk-J8AfGb11S3kCHgVoKyUz6Mqe_kFN5M-R93VZsNbGSua2dTRXGUaUkK-S1ODPDlk1pdIg8dzTlmJXW0iWimnG7ub2Ezx68XbwM-XClIa_EWqwobuhXkCbsvJXlbNHa_rEC9khs4Fsh3lHb7nOgGAYJafvsykFioQZan9rw_FSWjZM_aRxPArHDnJsw8_Uf8SjS_k4HxVGMs6hQ-5iBrLMcAUw9MBzTGXXLLSLJPFroDrjL7e1lbdIsy0d3qgMK-vGFhQbgOpnK35qthR0Fx7yZtWjPUssIq4-3h6335c_XGy2Rh2VQPVqJr_cD-hbH36MQda4Pn85Y_RuQRsSqKvQLBiABQlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=CWSzbqHBi-GqGeyvAabMEukkcZamJVz_f4VKDk9E-uLe_nN-7wOMql_AYfxZdWAFdKMhZ8ZvF6ZBFCWBw_mWhH3Nq8SRbM1cIHhU0UragTU_PA3ThcUMJfWgXYV6bDiyM2gZU6zZLjDrDQmITmRi3cLiY7xZUhJigekqE62J9eZazyGbXYPUY3SIxjfP3b-N5wkRZqrDrhS5l6FWwRSRGhiE0HywwSGi619-SdMJw7aN07TkHSFVqhUL_2hLf1hGowhIm06mb9BkGAdlRpvR8X2YSxcNEnTnF3cQMIgIRiJnXtMAsCvJPYONXUVnJ4INJwsXdLZi93Wqmk-J8AfGb11S3kCHgVoKyUz6Mqe_kFN5M-R93VZsNbGSua2dTRXGUaUkK-S1ODPDlk1pdIg8dzTlmJXW0iWimnG7ub2Ezx68XbwM-XClIa_EWqwobuhXkCbsvJXlbNHa_rEC9khs4Fsh3lHb7nOgGAYJafvsykFioQZan9rw_FSWjZM_aRxPArHDnJsw8_Uf8SjS_k4HxVGMs6hQ-5iBrLMcAUw9MBzTGXXLLSLJPFroDrjL7e1lbdIsy0d3qgMK-vGFhQbgOpnK35qthR0Fx7yZtWjPUssIq4-3h6335c_XGy2Rh2VQPVqJr_cD-hbH36MQda4Pn85Y_RuQRsSqKvQLBiABQlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=ot1XJj4AArYB_lBSgG-o7zoQZRHygqR1PTjtnpkPJFjWcN9xsDnxzca595SJQAj4y-WZXx3JBYtqxjuQ5UVkl9GAaXp6o239aPC_tf_Yd79Vp5tfMj0SM3nXS0HdZNCiaQ91-0dgsNu28BDn51zkDPxTpRqimh0uaWWQGd04v1Wl0W_VzpR8dg9GU6SGgTJGHzmPDtGuHQ2XAoynookWMSXoDNtP7PAqTwOAAAId8BijPCQW11xRqKV3VuRfWqLKLGTQtcwxKxSHNntNhaBrb4KgkWxh9lOFenMAFFAZgeIEOLnctl2bd72zjdNFlLiSs_9TEaBplYFdFqGSNv5ffA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=ot1XJj4AArYB_lBSgG-o7zoQZRHygqR1PTjtnpkPJFjWcN9xsDnxzca595SJQAj4y-WZXx3JBYtqxjuQ5UVkl9GAaXp6o239aPC_tf_Yd79Vp5tfMj0SM3nXS0HdZNCiaQ91-0dgsNu28BDn51zkDPxTpRqimh0uaWWQGd04v1Wl0W_VzpR8dg9GU6SGgTJGHzmPDtGuHQ2XAoynookWMSXoDNtP7PAqTwOAAAId8BijPCQW11xRqKV3VuRfWqLKLGTQtcwxKxSHNntNhaBrb4KgkWxh9lOFenMAFFAZgeIEOLnctl2bd72zjdNFlLiSs_9TEaBplYFdFqGSNv5ffA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=q-oinfNshzzUx3_3vp7MHnTbU1gEFEGLtUUs5KprxC7E8jgyiJxfW-P1pf9JG9q_-RuAMRh9zSiYmSVatnzjLpbo2A_ByZqnH-Vu3cmFtnDw1-_WIxWQlZcLryNGch-PU_MvwPEh9J_4B-NLLFeg9SGx4V6maJKJ2Re7hdNN26tckao-QvqeRabEwoIvsnQWX4diCqwQVdrXxKrZRlDYe42ayP2pM7PGi_U57723VMJmmo9GZZTf1wWEQeeqU3F_iNjW9c8uboCnDtrFhXALAENQvpNjjJv3q0jReMXPQ5QgntJZcZmoMcwJOwAlzxKwFM7kZ7vISEajTaTgYuo04g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=q-oinfNshzzUx3_3vp7MHnTbU1gEFEGLtUUs5KprxC7E8jgyiJxfW-P1pf9JG9q_-RuAMRh9zSiYmSVatnzjLpbo2A_ByZqnH-Vu3cmFtnDw1-_WIxWQlZcLryNGch-PU_MvwPEh9J_4B-NLLFeg9SGx4V6maJKJ2Re7hdNN26tckao-QvqeRabEwoIvsnQWX4diCqwQVdrXxKrZRlDYe42ayP2pM7PGi_U57723VMJmmo9GZZTf1wWEQeeqU3F_iNjW9c8uboCnDtrFhXALAENQvpNjjJv3q0jReMXPQ5QgntJZcZmoMcwJOwAlzxKwFM7kZ7vISEajTaTgYuo04g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=PA895O_ZI5UUGorLh01vNEClgtfrs1bELNs719DNVtntagRR8VG9wbWKiPTY4JD-Qz9Nx2UiV5fNaYH2zeYXcsXQiSCLe_NmtkMgrs-unZTHqCI9B-39IjNTPNBlZqxVxKNLfa3iqj085I4iwZBwquo08iM3q3Uq4vO7LdYMDX-l-Lx7pZxxxuf1DqNR7bmAzH2XPPQuxg0zzw53soTgFtCyPbamY05IMMnnR013d4oLSlLBzmwuHWqINHkKJCjpK6A_g4m7_KxZLE3fJ2YAxbMLoLb67e4tBZwVoF0_Y7luhKut_1F2U38RArVJnEJurUS_AXDG-EvvwVGZrj7DFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=PA895O_ZI5UUGorLh01vNEClgtfrs1bELNs719DNVtntagRR8VG9wbWKiPTY4JD-Qz9Nx2UiV5fNaYH2zeYXcsXQiSCLe_NmtkMgrs-unZTHqCI9B-39IjNTPNBlZqxVxKNLfa3iqj085I4iwZBwquo08iM3q3Uq4vO7LdYMDX-l-Lx7pZxxxuf1DqNR7bmAzH2XPPQuxg0zzw53soTgFtCyPbamY05IMMnnR013d4oLSlLBzmwuHWqINHkKJCjpK6A_g4m7_KxZLE3fJ2YAxbMLoLb67e4tBZwVoF0_Y7luhKut_1F2U38RArVJnEJurUS_AXDG-EvvwVGZrj7DFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=sJ5Q8JoX7yKZC0w_uxj1uW05XKx_sb0zGJdl1P_629ZXFO3gW1BFNJU266CRUUh_OeNGfVXvYgI2K3Cvej0fCDhl2YYp3KE3OgGtm3Xr63v3jwYPx3qLkz3TSfh5jzbk9m3h27Vvly7G4p90heRKWPM9-IiYBmnQ1gi0nFGrFPdTvIJxJzphyEMlht8O8E8SChDO_0PrT8A_-QVBQnRtSN1jNQtFzDDJnHDrvMQXnk761vT9TGFunY3YDEhIyBhbZv-qzFys4V7OlomJyrPoKMLeDFK8oY-62-4ytf7lWXjt0SRJc402ak8C8YjqIO2EOUGoXYeG06nKeifQSTQTFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=sJ5Q8JoX7yKZC0w_uxj1uW05XKx_sb0zGJdl1P_629ZXFO3gW1BFNJU266CRUUh_OeNGfVXvYgI2K3Cvej0fCDhl2YYp3KE3OgGtm3Xr63v3jwYPx3qLkz3TSfh5jzbk9m3h27Vvly7G4p90heRKWPM9-IiYBmnQ1gi0nFGrFPdTvIJxJzphyEMlht8O8E8SChDO_0PrT8A_-QVBQnRtSN1jNQtFzDDJnHDrvMQXnk761vT9TGFunY3YDEhIyBhbZv-qzFys4V7OlomJyrPoKMLeDFK8oY-62-4ytf7lWXjt0SRJc402ak8C8YjqIO2EOUGoXYeG06nKeifQSTQTFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=feR3Im_hy7YIyisQhGZDtlytSUYrKwr3i2Pj7kUpXXvqvykDFrBgdz7eJjlYjhBAWC6-gyDRDqdZJARgmCCGuBHwzdcYY0Io2_3zz_sbcQhfZDfJeemznjErggMH280mYsVzUxVYnttbzSwcD0L7uTg0oBDnYkX1jtQ6SZjS1lwI_IgcrJjJVeMLPxK4c3ZopXiOZOz3sAyHcrjlvJjdsk630He_t5KTgNtHyQUjJ0NjaCnaBnSgUp9OR3FWMKUVAEIE8RegRwSj7lnGk6UCwfgQa6bgOkK39DDdGqZLE7l53xbXf35MJ_tYn3FfAS7qwjnoYxDJk8poqVK5d7-xUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=feR3Im_hy7YIyisQhGZDtlytSUYrKwr3i2Pj7kUpXXvqvykDFrBgdz7eJjlYjhBAWC6-gyDRDqdZJARgmCCGuBHwzdcYY0Io2_3zz_sbcQhfZDfJeemznjErggMH280mYsVzUxVYnttbzSwcD0L7uTg0oBDnYkX1jtQ6SZjS1lwI_IgcrJjJVeMLPxK4c3ZopXiOZOz3sAyHcrjlvJjdsk630He_t5KTgNtHyQUjJ0NjaCnaBnSgUp9OR3FWMKUVAEIE8RegRwSj7lnGk6UCwfgQa6bgOkK39DDdGqZLE7l53xbXf35MJ_tYn3FfAS7qwjnoYxDJk8poqVK5d7-xUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=h8dhh1rchhoc6YBebc5DuJPmPhfqNlKZSYkWN1-oexCQ3RCxewazH5rJumOesqIuRo26F62pwEuLn8Dtuq1I9EWwEMgJpkqKGYpHNCIUsW_GI9you4af2O6osmFgj148Mbk3BrP28ewXttIRKvv_u3Vxvl_SbNP3aLpfa1Gs_vTx1rfsaac0QfgcBAUls6Hv-8b1hq8AAtPlHgeZhXRpsLpCVcbWkMmJf526YPIPDmenh6vG8VHEiW8NFlkDmutXDk8-MxUwCDZfSDYWUMZ8HZzIQbJrYg6r_cQCvDg2fa6p6d2lUwiQUWoe9Laiv6ZTxGWI7QdTZ9Sx9FsyBB-BhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=h8dhh1rchhoc6YBebc5DuJPmPhfqNlKZSYkWN1-oexCQ3RCxewazH5rJumOesqIuRo26F62pwEuLn8Dtuq1I9EWwEMgJpkqKGYpHNCIUsW_GI9you4af2O6osmFgj148Mbk3BrP28ewXttIRKvv_u3Vxvl_SbNP3aLpfa1Gs_vTx1rfsaac0QfgcBAUls6Hv-8b1hq8AAtPlHgeZhXRpsLpCVcbWkMmJf526YPIPDmenh6vG8VHEiW8NFlkDmutXDk8-MxUwCDZfSDYWUMZ8HZzIQbJrYg6r_cQCvDg2fa6p6d2lUwiQUWoe9Laiv6ZTxGWI7QdTZ9Sx9FsyBB-BhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=sgiDk0l2uKtDXcmCj8gklthkGPCVzMcKytk3xDZZlMBvKOnQnrXbMVRcxpiB1-LqY9i5ufLd5B6Gt914Dxvp6IZKC6cf12bWa5WAa-wcKEBPrJg4gV6TVIndaFGyHLbLKyKhv9te2Rq1iiVeZgeKWHsGuGYoqyGSoqYv7svVRWQMzattrzs_z42iQIgVTFI0Wl0j-qTzWjcmO9aTidNobuF6lHHspxqCeBCAxbH_1KYxqD8CXNjX1GDiNCHd4pG3hMvDupDlSxBwR1zOfLOSZrlw2U6KcWTRjPEOlM06bFVvtDBw5eDcEGoXB0GFhQbl6b5k7xpwN5DD8pEdUCorBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=sgiDk0l2uKtDXcmCj8gklthkGPCVzMcKytk3xDZZlMBvKOnQnrXbMVRcxpiB1-LqY9i5ufLd5B6Gt914Dxvp6IZKC6cf12bWa5WAa-wcKEBPrJg4gV6TVIndaFGyHLbLKyKhv9te2Rq1iiVeZgeKWHsGuGYoqyGSoqYv7svVRWQMzattrzs_z42iQIgVTFI0Wl0j-qTzWjcmO9aTidNobuF6lHHspxqCeBCAxbH_1KYxqD8CXNjX1GDiNCHd4pG3hMvDupDlSxBwR1zOfLOSZrlw2U6KcWTRjPEOlM06bFVvtDBw5eDcEGoXB0GFhQbl6b5k7xpwN5DD8pEdUCorBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clIMEGmY7QMyD4UlXy3Pf8gu6C4I1m4EHpnnyD10Maeb61p-wO827zuhAPNStu5wHxwRqpbU8nhzkzr2PnyFP8jToVgFN9IalDzUOT9_RNo7cQ7qquQwEuOFzsIRHv0Xmhr0n733SY4hJfVkqEhCRBblpHpt30-mS1anKZnqKAIGDQipmHa4tdhAn0QbLsBDTyzg51QcKnucVXt2lZniqVCQObIm4k4YfWpUQiTG3ce0jUVfXGGcas1_PEJsKp_JusnHShn_9m27N-rySEWCC5QlnSJfLCtXWDuHdDlddW_as72QNnM9mQk0tECSkLJBeZmimKKnk4-7V7nhDukJaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=Fl_6U5Y9D_EDP4Flae5OXUBBMEMMpxoA-AzBQWzAJOPxmNQaC3p6iJ1ELVMzjeD0vIWYuZSdTlEMSPvF6lewVVBkfFZTJJkhvGJBV9DBl48P_FtxqmZojXyeTALZK9DTURjvz9O4nrAzYeDqDN6dMYGl_bxM6xiWhow9GiJLveR3NeJ-2u30pzHlyEL1uu1D1d3EUNqSUItDQvHJPMnvjjTaimKw4yge41WB8kmeIcKoP8Mm4QE903AnTyPa4b8TuoxU2x1ubYnNHapaPEfVyhZg_TcmWGOUZIqbmRlO0YC5LSS8QRiKWQmZy212yQVyyg5vDvqb0Z1iL-546I0Lnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=Fl_6U5Y9D_EDP4Flae5OXUBBMEMMpxoA-AzBQWzAJOPxmNQaC3p6iJ1ELVMzjeD0vIWYuZSdTlEMSPvF6lewVVBkfFZTJJkhvGJBV9DBl48P_FtxqmZojXyeTALZK9DTURjvz9O4nrAzYeDqDN6dMYGl_bxM6xiWhow9GiJLveR3NeJ-2u30pzHlyEL1uu1D1d3EUNqSUItDQvHJPMnvjjTaimKw4yge41WB8kmeIcKoP8Mm4QE903AnTyPa4b8TuoxU2x1ubYnNHapaPEfVyhZg_TcmWGOUZIqbmRlO0YC5LSS8QRiKWQmZy212yQVyyg5vDvqb0Z1iL-546I0Lnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=g3dX8FTFsyyjlufA0EuYGrwbpAZg2HRdxweHwkjANdkawBdSOu4DVY5NiLHe7Ds5bBIuzg8GkvoE4nvGHslDE2HNuCJLQdlD6tSiNUfR-GX5LkplZ4DDB7duD_xdUBTL6YbpG5F_vVFLuV6xjugquQUtpoSZ3RVFf_5bMitWK_IhcNEz-Mn_tYK-pE2HepbWaLfZREfyVCV4N0BdjuyjIgRxqV2q21ym47snbBRaMQ7Snbm9lih8s1BSeTpUeiSn1iRUli3w77V9whXuMgatkaGFqIWECKoFzquRQdBEL_fY4EFxChYvExN3ex3Nv97blW82Aid-Ay9BvBybYbmghA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=g3dX8FTFsyyjlufA0EuYGrwbpAZg2HRdxweHwkjANdkawBdSOu4DVY5NiLHe7Ds5bBIuzg8GkvoE4nvGHslDE2HNuCJLQdlD6tSiNUfR-GX5LkplZ4DDB7duD_xdUBTL6YbpG5F_vVFLuV6xjugquQUtpoSZ3RVFf_5bMitWK_IhcNEz-Mn_tYK-pE2HepbWaLfZREfyVCV4N0BdjuyjIgRxqV2q21ym47snbBRaMQ7Snbm9lih8s1BSeTpUeiSn1iRUli3w77V9whXuMgatkaGFqIWECKoFzquRQdBEL_fY4EFxChYvExN3ex3Nv97blW82Aid-Ay9BvBybYbmghA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=uPOpQU7wJxWu50KZTokEMb_1ZSkOBmnNtp6gZb7vFFReX6Fwy7tjpnMAGaI3VMjcTKvr-61IjpiUIb0L09VTlqPjv4KAKZPjRGj985T1ozvZzBdxtY2vEBH7dpR2qObJjXuwimbE3Z6KraCSHYqOalHLF2ztM7ZDwgDrjtEgsDAIRvjMg0AQ9JP1TzXsYd3ALvSFExle2zDW3dBXDlre_VqGqBrng8Vjga4mHcaTanFAhSkxjwJnzmIvvgPUkJU9FSZ6vkYYCuicdhkyV3SohVG3jIrceyOS-gHPmfVSRuvA9oYNp7tcIbfknZCGZhwwjdK3luJCjDBoV8jaOfww6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=uPOpQU7wJxWu50KZTokEMb_1ZSkOBmnNtp6gZb7vFFReX6Fwy7tjpnMAGaI3VMjcTKvr-61IjpiUIb0L09VTlqPjv4KAKZPjRGj985T1ozvZzBdxtY2vEBH7dpR2qObJjXuwimbE3Z6KraCSHYqOalHLF2ztM7ZDwgDrjtEgsDAIRvjMg0AQ9JP1TzXsYd3ALvSFExle2zDW3dBXDlre_VqGqBrng8Vjga4mHcaTanFAhSkxjwJnzmIvvgPUkJU9FSZ6vkYYCuicdhkyV3SohVG3jIrceyOS-gHPmfVSRuvA9oYNp7tcIbfknZCGZhwwjdK3luJCjDBoV8jaOfww6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=I2pPICKjyfTY73EOuw6QrdCv4uP5akE-NKRw23YrzVPu_cK5UXs1F56Xv2Kncb0tzkS-vIyGanlUPpaZ0X6LkTirjgZBkBArqJ-CTMBSKd2pycmDS6NCAQL7gUfmuh0oKO5aes3O7qpBHeGxGMd_l2ELmacEbTPGYfrO2kMZnDWQLYDz5y28niPRn6Pxxju96cUQP3b6rl6wA2Nq0oA2qC9XyqMgb-Ur8Ye7QPxqhJo71SpXbGVEZT2oitlpS5oRtT2pV0DDHh7G7vFMEciq-O2N6sNZuIrzp5sz8VdeDvLixprM2Uqm2qytSf3aNbkQ7Sx48DoerKJXTzekhDpNQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=I2pPICKjyfTY73EOuw6QrdCv4uP5akE-NKRw23YrzVPu_cK5UXs1F56Xv2Kncb0tzkS-vIyGanlUPpaZ0X6LkTirjgZBkBArqJ-CTMBSKd2pycmDS6NCAQL7gUfmuh0oKO5aes3O7qpBHeGxGMd_l2ELmacEbTPGYfrO2kMZnDWQLYDz5y28niPRn6Pxxju96cUQP3b6rl6wA2Nq0oA2qC9XyqMgb-Ur8Ye7QPxqhJo71SpXbGVEZT2oitlpS5oRtT2pV0DDHh7G7vFMEciq-O2N6sNZuIrzp5sz8VdeDvLixprM2Uqm2qytSf3aNbkQ7Sx48DoerKJXTzekhDpNQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJB-qEDZo6ez8Z9JT8GgwaSFf7nw-36g4g4mJGvpkEqSR0HxR4KP_uWe9PCNtRc0P7LjFJxaOAM2BbtQVfZ6HdX8isza5mzLx6xQ0TARQOScUM1U4zXYRqrNYbMqRQlSVI8FRZMK5iQcYkKSDgGbw7GnGeMwr2TG2HIaxiU5TNdYZrZx-n_qOoLXTvwLXaTsRBxtQRhI2xsN-TcuCm120lkot0SIal1hENqL-u2sz4cKIH1DoyIXD25in97D9intFLehLZItkKXa4EZaheA7t1CjsYFbzusyu9SgIE7btsuX2Es_8h7PubIczAJYpOCTNU5TT9wWMNFFak8Dz00Tdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=kGKHcfQtw7Tz8L-DTQCOu0apaLwmMh8yd3sZGW-O8NWqYg2oN5ufUJrripwBbx-bUy58NSp9rsBSEHSmdarQy67yTAmsulElw9MKNKO9_1X4qViMauscRYglInX2or3yK54VDIn1ckijWv4tusQ2taNdLXBwcqN4zZjcDnwm0CPT707XXbTz2WJgJvsu90WDjsPHRixzcEPn9PTVz6NmCqb2vX_fm4qDMcYUfLPSNZet2F2fqTyYma_OzfmkeVdwur_6uxI_pvO6JxH7XbCb7Q-Yj48WNNIQg1c1Ar3G6_Dpb27TkOuW_pbI61DMjbGhCWL3X0Z6n4dNmoWj93XjozzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=kGKHcfQtw7Tz8L-DTQCOu0apaLwmMh8yd3sZGW-O8NWqYg2oN5ufUJrripwBbx-bUy58NSp9rsBSEHSmdarQy67yTAmsulElw9MKNKO9_1X4qViMauscRYglInX2or3yK54VDIn1ckijWv4tusQ2taNdLXBwcqN4zZjcDnwm0CPT707XXbTz2WJgJvsu90WDjsPHRixzcEPn9PTVz6NmCqb2vX_fm4qDMcYUfLPSNZet2F2fqTyYma_OzfmkeVdwur_6uxI_pvO6JxH7XbCb7Q-Yj48WNNIQg1c1Ar3G6_Dpb27TkOuW_pbI61DMjbGhCWL3X0Z6n4dNmoWj93XjozzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=lCcMadpLf49BYKFtKN4s6eOmXlq_SQQnvoHb5cxuswawFlKB9872J86gkFk2X3Uk3sFKQdfnyHqivSrR8Ev2-k_mHM_ZhsyQjVFdNmhSEMk9-QIBDsIquOJAz6vJJKTucV0P99UVS-kX63mytd1Sw_T6ONfm4YJD1C5EUzad1Z4PCJDxLa4-BhZ9r7bwQfeVX728HuYUbB1C0na4j5TO0AUhSqM0rXY44zowdOkARN-KHhAIG746OdDPxo_8624qU9VmAuEh-h0WgwwkRmkKpw_xnjfL8iQYgYUKqx8-eOqxn8I3GUO8BNd7lsSSH8gypyK0PO2cC9jvZdXuaJIyyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=lCcMadpLf49BYKFtKN4s6eOmXlq_SQQnvoHb5cxuswawFlKB9872J86gkFk2X3Uk3sFKQdfnyHqivSrR8Ev2-k_mHM_ZhsyQjVFdNmhSEMk9-QIBDsIquOJAz6vJJKTucV0P99UVS-kX63mytd1Sw_T6ONfm4YJD1C5EUzad1Z4PCJDxLa4-BhZ9r7bwQfeVX728HuYUbB1C0na4j5TO0AUhSqM0rXY44zowdOkARN-KHhAIG746OdDPxo_8624qU9VmAuEh-h0WgwwkRmkKpw_xnjfL8iQYgYUKqx8-eOqxn8I3GUO8BNd7lsSSH8gypyK0PO2cC9jvZdXuaJIyyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hwt-kIuulDUBv6IU2pF213bYxlyu7D4wc2Yni3Hwr-QEb3vVoN3f7jtUHJNMHQy1BPt4N_JCy_dIwpKt6nKb-wkeUBJQuTSPmZmf_3aXV4YVp6aWdlI8LDk8cdeDJUtJbynCn9tbIhGnXUTYCYoOZLnQlek0lJCaNJuKaDioOfCOjjuHL28wnUwsZkpmI7ogs1S5ZBvONlaz268o_z_Qbp0fK121J3Y2X62ofy80xVL7KBH3_Aj32M_4M3UDOPmEk2tL9r6lJu-GSc8UEu7IXsC-ptrxX4TSW_j7A9LklxRCRB4KJkTnqJmESc90rns53lWm2wAoHDK7EeFHvAhb0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j33KFcWvAX0jXsvOwsOUY4f2eaYY1fE20dWGjgICsu1cLuNQrohIcWIXdgWBsaVKUO6c9duF7jLg008Yoc8Ax6aTK9r8YaS6c2PAJDLab1WNrDGytfnu1jb2eswID16D5I8DxW8od8gfcbw2FUbRJvPw44ETE1TjEPIexQlVB_OQj3GvIz0ZblL54S2MDTrpLxqV2nU2C3XAbSZKigYiLFYn4y7qNGI3SIJKFaojsVHTjUWhIrmNESHosDjtd3i7b_o8wU6RIC9WOLG0TuNV045v0NVqGWm83QydnlSuxFHMqc5tJZff5Oj9_lyrVbPezZ57GX6gXgB2YQZ1V7eULA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=AZNXA6lwgunCP45s52fqGxMrUPneLPEvE8M_wpsGluoeIcHPxONDHTsoLs7hAgPlRerD6PF_xcsfrNFNqmo6x05cI6a21PbKMf2cMNj8ynpyy3gG2V7Zd_oK4sbdRAQqkkDncdufq8lVg7c5oCPBdkyFZ2CmKFx7wF3eUQML7hEWK6dVP1FLpgU57kscIxvAip_3ZqU3y17VnRnuvgyjJblstxIS5Wz1Ra8JAcL6Mqpnz7UKstcInRaO6qVhshMc7LK5E87TClyLBajQHjLZuDuwp80N6KHhgKe8R8HrXTH0GbsLeQ_QGOZesxNVHo1yz70yi1Kx_0bgDIlTUOPekw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=AZNXA6lwgunCP45s52fqGxMrUPneLPEvE8M_wpsGluoeIcHPxONDHTsoLs7hAgPlRerD6PF_xcsfrNFNqmo6x05cI6a21PbKMf2cMNj8ynpyy3gG2V7Zd_oK4sbdRAQqkkDncdufq8lVg7c5oCPBdkyFZ2CmKFx7wF3eUQML7hEWK6dVP1FLpgU57kscIxvAip_3ZqU3y17VnRnuvgyjJblstxIS5Wz1Ra8JAcL6Mqpnz7UKstcInRaO6qVhshMc7LK5E87TClyLBajQHjLZuDuwp80N6KHhgKe8R8HrXTH0GbsLeQ_QGOZesxNVHo1yz70yi1Kx_0bgDIlTUOPekw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMVeBWDYI6zo5-wOc7WJaq6WRin2-U1X4hIeiScvPK2iK6kZDY33sBihhvWGGBtv-imvXSPNjQKF-mXrKVgcBIdoXTlPlRDK2ULPyzmD9s_gRD8oFj8Fquh6gnSq-PAnxjEH_N8c0OIex-06xt0tKqWqB0ZlcNuS4YHa-h8vHz18HYgHP7StXHUNv4-RmQxmk1OXoGzeD2mC7FCeU4kRvP_P_o0gbeTj474B-3mBZXSSQlqlNpg0ZyKjbT3Gz_rufOhYcqjD_XLdSdjqmqMvEFRTOmdsLwTROdYdmkXUcbHTaLTIRczwL5rRaXp9A1Dn8ZKCMhTsYLw0sN_zup_2SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNraA-ch4FUCIRjC4QUyvaiThhzCpIU0KA5KCVNCrpDJFM6aEkjBJ7CRwaCGfIhpkHh9Plp9PGSPeDlvA8egvJBbr90QDETB9wYXRIfF4oHvB0T9dWGt7f3Ij-14uaDEzUAP2koh-Ip7JX6II7TlVccQnuhrYWPuwdWF33xexzbqrbB3i1POHpPvnqqi5L8G5p6mXLlzQnsPlTEyu0S7o-XSXKrWjK1skOZLKY7l708E1ZDzPVXHN6dOBxEQfbEHVD38GmfgJZS4ULFPhiVBY-o5baaLYVnmgy8I25_Z3r5ghjRQ6LQow01kGGHuJVZANrVXw8V1rdIkTuKl-JSSww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-dmuOkNUffm81dn-gZMO2OC-pRMJMuKaipKeptf_VmqHGhFNIGpe21eL10g_V8ebRel7C1oSXAAWBtj24QR_YRxZ4At-SFqTLK9rq3eNpjkYZG8G0JSKz_vZe4OkV32EPViZQ4Q-JZ3wn5pN72Cq6ER-D1MWo8vCFf-82pTva3s2z42z5ogStHgWcdVBN-6oKnvpz58HrXOIudE7ja4NXfgCBFiHbo1jqAjpOUCihmf_NBDX-3Qyz5JQiMGPzDa2_NWflJtIgEwXzzoI_vQRyspwOdyO1QrQwLq41ej87T3jq1Mu2F3VPHVAPnNCHFjo-kmWSdRQWvhLjp24a7Z4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

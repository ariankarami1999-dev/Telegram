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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 20:36:45</div>
<hr>

<div class="tg-post" id="msg-6802">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbRNohQNMJwKjiqfXQ0XChBg4e6gJ0ux0aI70Ml7_gB3Rd-01f5Ldzf5jJgXyjmYQ5zAi7-qEbOew_VdPBiR3aK8X_N2jyHIf6GzP56rbp-auRJy4whOw5HY_ClzYTDXqWwBV-8-jffVvIb39mL0gWqiANvzmGpg-sjcP6JwYw2y3ofW4NmEAv5rjkOOJ-dOhAUkY7Un6dEGtpUDoc75pCnWT3f94W_PqjrF_p052rwhDy85JtpFXjQfkgXseXqRrIXqSkNaMAdgM7J5q9uDzo0ooiD5KBh7ycuteb1q_uVMhuYTjJ8ceQkLFvSHC5STkb46sEWYVbIGh7oOFgQ1GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن  که آخوندها دائم به نفع خودشون و شیعه و….. استفاده می‌کنن آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟  یعنی قرآن وسط تعریف یک داستانه، و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل  و فرعون صحبت میکنه و  اینکه خدا…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farahmand_alipour/6802" target="_blank">📅 10:52 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farahmand_alipour/6801" target="_blank">📅 10:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6800">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farahmand_alipour/6800" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6799" target="_blank">📅 12:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4MI5XsLbkYJVxKdTuBVEJg7sopC0Splyx39IDxnGJQ2_o6dTlejlu-2gwFO8ms4fKpySmU3noG5Fp07k_WDH_hgaz8hcZXO-8RI0d1d4dsO_4o-rKGAta24IXx95qHFqMbOBiLSNtNFNjgDpngYRNGdfnl0mWujwGOIpZquTDLy8Pj7RRqEqi25IJtxhph8bgOEGKPsDslGUpt23C6B1iR_HzZOBDhSqZH9OF0mfQRRdY-KFww0q5fQE9O5LV-lOXqhzrOPTCGP7zGY7Iz3_V3gU-AH5dO33QBck7snARW8DqujQ1gSEzG8pgcAL0d0cXy4vmSezgBxEn1et5HkuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»  در تخریب‌های اخیر خبر میده. دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.  در حالی که اعتراضات دانش‌آموزان…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6798" target="_blank">📅 12:45 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6796" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6795" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کار به جایی رسید که جنگی بین  محمد بن‌ابی‌بکر و «عمر و عاص»  بر سر حکومت مصر شکل گرفت!  عمر و عاص، دفاع قبل توضیح داده بودم که اولین حاکم مصر بود!  و جایگاه محکمی هم در مصر داشت!  و مرور کردیم  که اوضاع مصر هم از زمان حکومت  محمد بن‌ابوبکر از لحاظ اقتصادی…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6791" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">معاویه برای محمد بن‌ابو‌بکر  نوشت که تو که هر بار توی نامه‌‌ات علیه پدر من می‌نویسی، و یادآوری میکنی پدر من فلان بود و بهمان بود، پس من حقی ندارم و خلافت حق علی است،  پس چرا پدر خود تو (ابوبکر)  همراه با عمر در سقیفه بنی‌ساعده،  حق خلافت رو از علی گرفتند ؟؟…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6790" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6789">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بعد از چندین نامه تند که معاویه نامه‌ها رو هم می‌فرستاد برای نخبگان و مردم مصر،  (البته محمد بن‌ابی‌بکر هم خوشحال میشد که نامه‌هاش خطاب به معاویه،  دوباره برمیگرده به مصر و‌ مردم مصر هم می‌بینن نامه‌ها رو!  اما قضاوت مردم به سود محمد بن‌ابی‌بکر نبود! نمی‌گفتن…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6789" target="_blank">📅 12:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">محمد بن‌ابی‌بکر نامه می‌فرستاد بدون سلام!  همون اولش به مادر معاویه فحش میداد!  (این موضوع فحش دادن کلا در بین شیعه به شدت رایجه! حتی در متن سخنرانی‌های امام حسین در کربلا!  یکبار هم مستقیما معاویه برگشت به خود امام علی گفت تو با من مشکل داری با مادر من چی…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6788" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مصر، ثروتمندترين استان حكومت اسلامى بود،به خاطر جلگه رود نيل وكشاورزى پررونق و...! به خاطر اينكه در دوره حكومت امام على ساختارهاى اقتصادى رو عوض كردن وساختار جديدشون رو هم نتونستند به درستى پياده كنند، اين مصر بسيار ثروتمند فقير شد!! يعنى اوضاع اقتصادى داغون!…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/6787" target="_blank">📅 12:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">این رو هم در نظر بگیرید که امروزه به خاطر حدود ۴۰۰ سال تبلیغات یکطرفه، اکثریت مردم ایران میگن حق با علی بود و معاویه در سمت اشتباه بود!  اما در اون سال‌های اولیه اسلام،  چنین شکاف و فاصله‌‌ای هنوز وجود نداشت!  بین نخبگان بود!  برای عموم مردم، جایگاه این افراد…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6786" target="_blank">📅 12:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6784">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">محمد بن ابوبکر  یکی از نزدیکترین چهره‌ها به امام علی بود که حاکم مصر شد!  یک جوان تندخو! از این حزب‌الهی‌های افراطی و عرزشی‌های گنده‌گو!  نه سن کافی داشت! نه تجربه داشت!  اینو امام علی گذاشت حاکم مصر!  حکومت خودش که متزلزل بود!  چون وسط آشوب کشتن خلیفه سوم…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6784" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پس تا اینجا همه می‌دونیم که  فقط شعار ندادند!!  همه ما این قوم رو می‌شناسیم و ۵۰ ساله که حیاتشون در تنش و بحرانه!  اما فرض بگیریم،  فقط شعار دادن و حرفهای تند زدن بود آیا در تاریخ داشتیم که حرفهای تند زدن باعث جنگ و ….. بشه؟   بله! و اتفاقا دو مثال روشن در…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6783" target="_blank">📅 11:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید که حامیان حکومت،  در دفاع از خودشون میگن :  بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل شعار میدیم، ولی کدوم کشور به خاطر  شعار دادن و پرچم آتش زدن و حرف،  حمله کرده به یک کشور دیگه؟   البته که همین جا هم صادق نیستند، …</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6782" target="_blank">📅 11:44 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vd4rL_rxDdhuWNQPpfoc-W-j6sDy8AOyNYS_lYSPMSFUUxKFhOKTlHKGHFY4HS46gSfLqctAfRLeUoWP_drlk70r2o0QkrZJuaCUVkOdWAZ67lLHbwxdvyrd0r2ZcQw5xLfDRjBJry7Zg_O3MU_Yim94xV8VFjrkLIYZZrSxAHe6hvM8TItk9ll0wup7kIEUfHxqteuUeXW0y1yEkpHT5HTu93azyP4DkeBwjxRw7cXBgQQSsIyCAgguQcNtQiZ5M39-yQYVyeuiF5J_3DnlJCCw5AoaUMk_mjcHNOjKKHOhXhmu7XoE8OX401-BfXNVlBMBDF_-WLCl-vD5H0AZ7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZFplDUBgK1207mxKHhjGUDOCa2nBfYPyTNjFyjUUU9YB628-S28VvlhSr4m3ST3BHvj6WfgGoMFXJ8JjlvqzjQv8WcgeRSn_u6vOD3YoARZoNy9jlUJSvQfeD2AuYH2G8ASv9d0pdh7fxcQ1uAdvte9I5USz8VQIr5ISitA9J9yDmHTLh2L0E_5E-OHukBUE224Wz8CX1w1JejGpUvUjXWYXTX72j5WxnJb2_XD--VPxqjP3eY3N9sIpfyuFFKCCVCMpsLGwK2Dj1ETQ8zN4IT3VjRt_r-XdmwJvx4rmfHnhiNm1kfRKXv5PFLXfb9_uLOvW1OJEcK3D1lF-DuSww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی این ۷ شرط رو داده
به آمریکا که در قبالش  ج‌ا تنگه هرمز
رو «باز کنه»! آمریکا گفته تنگه هرمز برای شما بسته است!
برای ما که بازه! نفت که داره عبور میکنه!
و اصلا درباره تنگه هرمز مذاکره نمی‌کنیم!
اینها مثلا زرنگی کرده بودن بریم تنگه رو ببندیم در آستانه انتخابات قیمت نفت بره بالا،
آمریکا بیاد گریه و التماس کنه!
برای «زمستان سخت اروپا» هم منتظر بودن روسای جمهور اروپا برن بیت رهبری گریه کنه، لکن هیچ کس بهشون محل نگذاشت و خودشون دچار مشکل کبود گاز و برق شدن!</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEXcNY9a4m4enX1naBWO4K27iAd7dZaYccijJ4iidB9GU4UArs1ALj4pPpxyb9p_PiYpYwUPzspzOha50euIOjbXQDvzRuQIZZgJ3_OzurfkLrdXSuL-atZB-UuGIbMc660-iVy95H3BgXEETdzKANWtOUd7LoE3PspASOKN4bLIakTo5AKa_xhGVqRmCyoCaDEiSa_KWbXcRbxmSHMcUEB3niC8onVzSe-mx4gTdS2r1K8Jw0dWzeoQ8vfSevYqBsXrGh8GZ_d-dZdyttSVfiC0OnKiEBbxVBnAez-4LOMKgfeHPWs79BJpciXo2lfBU11EMPIER2kCbF6thrJpvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=l_w8WlGGkkK9oiautyW25Wk-XGIBO17OKr4IWrqAEhUZy5XfVXRIxDwn79PEc8pwNYdYfWLuNkX8Q-fsbtHaWw3iFJkmLEP7JSIxCxmdOjKQS5P1DMPaYQFfDo65-0wL62ozRZfEoIKjpZtkR9fknIvHKsy_Eypd8gBc_qezJcI20blK4ZO5DfnmU-_5Bhdg4uJLr_4TGwCWyzmGAr7Yrop3ygpYooWquleNYeSc4TdkKWkNTsGzXTBfkrnizQ9jB60Aoe61kWz4aUrQu2g9WFPX8_b8X--OAxv3WYaW3Xo8mKRl5XEI3KgIrgZ1rMDI4w8IHYRGgVRongenaSDRIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=l_w8WlGGkkK9oiautyW25Wk-XGIBO17OKr4IWrqAEhUZy5XfVXRIxDwn79PEc8pwNYdYfWLuNkX8Q-fsbtHaWw3iFJkmLEP7JSIxCxmdOjKQS5P1DMPaYQFfDo65-0wL62ozRZfEoIKjpZtkR9fknIvHKsy_Eypd8gBc_qezJcI20blK4ZO5DfnmU-_5Bhdg4uJLr_4TGwCWyzmGAr7Yrop3ygpYooWquleNYeSc4TdkKWkNTsGzXTBfkrnizQ9jB60Aoe61kWz4aUrQu2g9WFPX8_b8X--OAxv3WYaW3Xo8mKRl5XEI3KgIrgZ1rMDI4w8IHYRGgVRongenaSDRIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند سال پیش یکی از دوستان با آب و تاب تعریف می‌کرد از سیستم پیشرفته
بانکی ایران و کارت و انتقال پول با کارت و …
همون موقع بهش گفتم این گسترش سریع
فعالیت‌های دیجیتال بانکی به خاطر پنهان کردن بحران عظیمی است که اقتصاد کشور باهاش دست به گریبان شده!
وقتی پول نقد دستشون باشه خیلی بهتر متوجه میزان بحران اقتصادی کشور میشن تا با پرداخت آنلاین و کارت و…!</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=O-iYVWpzxit1Yijs23ulTWulI19tI8bAMv7C2qWjZVZrDIx8rFkAv8uKtzsjzTHXyxKk72wKZtYd2r45I3VRjpTa-uQRtdVNAQHrxYB3c1WCqzFQ0bA79MhhX4XfVC8UHqMXXDlNGM-_VWF7tcZYgqLxRnxpEpjIvEa4aiDefVc4LlY8nXQRZcFahzm1x8viukx2dAG5Mt84bPk4-U3NJZhu7zF4h7qJv5EXlENwidgwwYJ1nRpVDtEyfmnMuu4O1glf6uXekrhFxwnMTK-rf3Gd89APjpguL-XTPqaiZvtKFkmTeMeEvXuYzADZagxwjVeX1RkHBhAD8VqoC_mXDB4B9M5mtmOIDjl5Le2okm1yloCYZBNh6BIBrcPc5smEEFRgOEw_aT6Bm6QmX4WFx3pC2OqnihTdQYwskRwstQTD_fbE4QGLV6M1zdMDp5z5KuS_gFG4Xl8sGReEmZVk8DJPyxYlZRFnnG9URe9Z6T2IRrM6P73kZVTWUVnO-C3G7cWW4SbVgsQHE0vKMcJg2m0-LlfPwAUAqL_7Pqh_EU74WpKonIQFv0K-SBfeeYgb4lwYbxJtORxltB0MTEcSsTuHgX7Jm-efA9ibTgauUOf2alizlGiFvk4guvdeT53BNy_SrfhpnhNwODSkApTGlywtLFoy2ZY80AS9rZ7tJU4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=O-iYVWpzxit1Yijs23ulTWulI19tI8bAMv7C2qWjZVZrDIx8rFkAv8uKtzsjzTHXyxKk72wKZtYd2r45I3VRjpTa-uQRtdVNAQHrxYB3c1WCqzFQ0bA79MhhX4XfVC8UHqMXXDlNGM-_VWF7tcZYgqLxRnxpEpjIvEa4aiDefVc4LlY8nXQRZcFahzm1x8viukx2dAG5Mt84bPk4-U3NJZhu7zF4h7qJv5EXlENwidgwwYJ1nRpVDtEyfmnMuu4O1glf6uXekrhFxwnMTK-rf3Gd89APjpguL-XTPqaiZvtKFkmTeMeEvXuYzADZagxwjVeX1RkHBhAD8VqoC_mXDB4B9M5mtmOIDjl5Le2okm1yloCYZBNh6BIBrcPc5smEEFRgOEw_aT6Bm6QmX4WFx3pC2OqnihTdQYwskRwstQTD_fbE4QGLV6M1zdMDp5z5KuS_gFG4Xl8sGReEmZVk8DJPyxYlZRFnnG9URe9Z6T2IRrM6P73kZVTWUVnO-C3G7cWW4SbVgsQHE0vKMcJg2m0-LlfPwAUAqL_7Pqh_EU74WpKonIQFv0K-SBfeeYgb4lwYbxJtORxltB0MTEcSsTuHgX7Jm-efA9ibTgauUOf2alizlGiFvk4guvdeT53BNy_SrfhpnhNwODSkApTGlywtLFoy2ZY80AS9rZ7tJU4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Veie0GM4wxZajA1zFCiSnkcE0wnOxv_rSpgMWJizHFTzCX8-r-ULSPHVP9SAN4oDFZUN0mwzwpX7FncyxhqYks88FSCOun5_Cdsc44Sj0-4daqgDAtWiX-I2vo7rtU84xwoLd4ZVvk_fe12S3bk05J5fdflj33aDYzvErgnH7WYP12NAwfCDgMNq6PG-6NoB8je2cwrthUY-i5MqUHx97PWXLGUPJdtOTt3sWVp3z9FSNW3h2mKWfV8gerVhVXBvqKRGKU5xe0AdseDuAhuEUdH2CFE-m1OeKXH3ZiIuhVjZ5zkRChuzreoUgUK-WtGOQSPhLDrC9sPDV3u9udyufA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YUMxDczDE19YXk37NhSPRrIxlcyYQwlJrAgRRfCv-U68BIG8s09B8bZKl4XcBQI1jdjFMaEg71QLFLHSk5NPEB63TnVdj9QJ0dSjmQi00G4VPbtN7DjlmCBLW1EI-LOGT8sHLF8Gi5Bp07k1CbumzI1ZQCD1Gq-BeDf7Im7HVpQrf7px92gdWWKTX9_YDSi4yZe-sGzJi7Nf9ddI2I7qY3VYoGMH-oPD6esLvFAwHePdPtRYSseoKYuBY1kajDKyIeUMZmtssUA9W-9u0uuP9ckK73pPRReYgAltKzBkv1SPltEISBlJxmdUG2oPlgX2ljyYr0G2E7YhZimNR6P5QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hMQ8Fwc72r-jtJyFWmJZpeRCKDo2s2-AUkfpE2gw_-nK0ghinE5dh9wjmZlTeCXE49a_kBSJo4nO2XC18DTHU3Lg9TlTk-bBNpJFkAvKwUkat0qULIUrFZ0pPB1YU3W-SIPNLHvASfaQ3034g1PulQ-PTOtnIYWqfrHHaf_29IHRbeKEEZwxhrPig9wULkehYsC6yGCv7B5JhFDahafWwyAAWYNQuegu6X3aTU8DF4Li6Ejx6roLagTYDSRSdmyxaY2ONn_6Q5_f1tXpTBtu6SOn5TS2htpai9Ed84EFL6j27L9izPx7-Vvta9SqjY-z5oETtunVEqUlVqylagA0NA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=aDvDXfxa1qOusshavJ807EAanPCf963veQlYgWwlJLD5OZ0N5t7Wf8UFYhMjcJi7WOfO4JLtzvijXtA5xwMWcFIiY_VYbt6MOWk_lSxeGpQmSdsvWVJQHPtUDv5Nrlwe9W--v5JC6f4l3I9zjiCyAqGPQeHvNacLubx2q2uasGzj5hOms-jKXzFRDIaYFr8pwwA6AXfo5ce2hyYMauX7QEo8Vh7E6BkWkrtpIUD8fZKEbpBsf52sldO2NOkOanjVHzt0aESAXxvB-QHhgKHhSIWNfVyM_5o5oNOLGnuq5VF3E3aFv_goxdTJgpmyR4kVRWSAvAwlLZBEUNEpnniefw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=aDvDXfxa1qOusshavJ807EAanPCf963veQlYgWwlJLD5OZ0N5t7Wf8UFYhMjcJi7WOfO4JLtzvijXtA5xwMWcFIiY_VYbt6MOWk_lSxeGpQmSdsvWVJQHPtUDv5Nrlwe9W--v5JC6f4l3I9zjiCyAqGPQeHvNacLubx2q2uasGzj5hOms-jKXzFRDIaYFr8pwwA6AXfo5ce2hyYMauX7QEo8Vh7E6BkWkrtpIUD8fZKEbpBsf52sldO2NOkOanjVHzt0aESAXxvB-QHhgKHhSIWNfVyM_5o5oNOLGnuq5VF3E3aFv_goxdTJgpmyR4kVRWSAvAwlLZBEUNEpnniefw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=P_jTq1-aUFqqnuqdd6i6oUKtDpcrHpiSuafzSVLPkeYo_5Lsms7DZXEnTRnJy7Cq_oGDBxNk5q5jxJvEeq3lZzzdFsZjNtGlOhfEdI1Sq_JTZUHvMiWAfC6pYm4EzMgR5NiZt1CxvXS22IfeH1emSpEm572fZrrl1fp8PVJ7DBwrPjwjzViof-Jw9joI2r_rXMZ_fgtm4SopUjfOCU-hUPp2e6p1NHk-TBR4UfntBuo3-UBViaT90Ji071Sr7f0afHoABnGXggMZH8UsKrOr2fSTv1Fzh-AqbE9G5C03IYhxlxBLklEeW6G_6oI74Ex9gx_5QQ03tin4raZ-aoQrcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=P_jTq1-aUFqqnuqdd6i6oUKtDpcrHpiSuafzSVLPkeYo_5Lsms7DZXEnTRnJy7Cq_oGDBxNk5q5jxJvEeq3lZzzdFsZjNtGlOhfEdI1Sq_JTZUHvMiWAfC6pYm4EzMgR5NiZt1CxvXS22IfeH1emSpEm572fZrrl1fp8PVJ7DBwrPjwjzViof-Jw9joI2r_rXMZ_fgtm4SopUjfOCU-hUPp2e6p1NHk-TBR4UfntBuo3-UBViaT90Ji071Sr7f0afHoABnGXggMZH8UsKrOr2fSTv1Fzh-AqbE9G5C03IYhxlxBLklEeW6G_6oI74Ex9gx_5QQ03tin4raZ-aoQrcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVNRgxnwl0d38jL15MNWrGnAPQvxExw-jpxECqZSiu8aff5uyrZUU-L1lOky7nDv3FLT6N-ElWi7lzh9nfmsTU72mlKVj_cQ70UJQ_Rnr0EYaGpACor9UIgRIiLOtw4YBMKhTcifNnZANiic9Vo-fER5dufoEMjVgEBc0oZ0UQPsSl-0vkecywaF4kkaZo2xEcqxYHrOJO01CiOozGaDRnlUosN4LzYOAo5vhePvDtGdgXX10FeaNPaSxkqYE4nBl6ynF3SVN4qunvg29huoE1HD_rebuugk3g-j0E8ll9a6NtjGY4TWj91IuAlvsKw4D_tfwuhn2YRpwMbG3OrVjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=Uclsk2XsbLEGlT5PV2O0gkkq1mHrlV5SVo0O7iZPyu2NnJp92E5dDLoywhDzeXH0RAtrQDfhTZSEqI3nrp_gEl6AA6lq2gqIbQ7Ofxrxi_ECNxz5BP1Fr6-jmkBa7ymTrTkkWN9Cv9_apwyA04DmrKjDVlgVUPffqa67pTMm_vbYjYcv1PaBlQRllwOZw3c0fk5orMcod069VIz0Gbnc3AT98ARYuvPrDQ6j4vlKZZx0INxtEqaGytqcURWAxOuoxMGaGTQpEK1VSCndntvlqJNR4zgiaxJS9-VwtytWwetdpYCIiyTb9QwFifftzl3Dh-8NehroZCgaigyACgumbolcopxjSKTIUKc6TxwiivtPQqegovIjdg-TU0DmeZuVHgtiCKBM90duOdhyquX5hxMcSMjraWO3ANpLIPnCvWieJKRbZ3uSEfTFJhx_9Kx9IO1hay2Rp30CwRJlQ2UVYD7C0hyJaQPjjhfqN1zjw6JHXfIKUJuVfEDut5GmCnlvyj_Wy82I8GAcx22iA-pExum8lFLXZoP2J8k4UQou3LMHk8zXyaPNh1sNDFRXSoVjG9MqRDLAPbJMv3ThP4CF47bt_zrEn3Xp4PcRuIeBvxCRzwwdjt5G9BoquV-RVo2wq4p83LIoOng_xdqY4I8Dia2R3iVRF7Zczpev-fmftCo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=Uclsk2XsbLEGlT5PV2O0gkkq1mHrlV5SVo0O7iZPyu2NnJp92E5dDLoywhDzeXH0RAtrQDfhTZSEqI3nrp_gEl6AA6lq2gqIbQ7Ofxrxi_ECNxz5BP1Fr6-jmkBa7ymTrTkkWN9Cv9_apwyA04DmrKjDVlgVUPffqa67pTMm_vbYjYcv1PaBlQRllwOZw3c0fk5orMcod069VIz0Gbnc3AT98ARYuvPrDQ6j4vlKZZx0INxtEqaGytqcURWAxOuoxMGaGTQpEK1VSCndntvlqJNR4zgiaxJS9-VwtytWwetdpYCIiyTb9QwFifftzl3Dh-8NehroZCgaigyACgumbolcopxjSKTIUKc6TxwiivtPQqegovIjdg-TU0DmeZuVHgtiCKBM90duOdhyquX5hxMcSMjraWO3ANpLIPnCvWieJKRbZ3uSEfTFJhx_9Kx9IO1hay2Rp30CwRJlQ2UVYD7C0hyJaQPjjhfqN1zjw6JHXfIKUJuVfEDut5GmCnlvyj_Wy82I8GAcx22iA-pExum8lFLXZoP2J8k4UQou3LMHk8zXyaPNh1sNDFRXSoVjG9MqRDLAPbJMv3ThP4CF47bt_zrEn3Xp4PcRuIeBvxCRzwwdjt5G9BoquV-RVo2wq4p83LIoOng_xdqY4I8Dia2R3iVRF7Zczpev-fmftCo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد
تا به دنیا فشار بیاره،
اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=nUyhsmRFWdGIDDExJoyTF8ciARsvjIv45PFAWlUPwbvkam9_6zM3Po0G7qWm2gdva_YPI8COymcL2pneoDs_R-XDrtZvcL2SOd67Cnl5Hfq6HXYEmF2ASjDDG-DvQOLR6rfQpyBt4VwgYEYutidD3dnnJR-MJLx7ilW-5mV-2djeh_bcuR9SAD9FjtejvCDklnikdztS0udXbZj_rGPjVdg_khGIflOz9q31U8NIgIynrthZbwP0LRXbendw7HGih0ARExf5YrEvjhL42rSNykNcCYZHTtYjmcVH5HGm2ElVOUOikD0ddyP4zNa9VZiQbvCmzhKzoxTYM1ePHCYQJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=nUyhsmRFWdGIDDExJoyTF8ciARsvjIv45PFAWlUPwbvkam9_6zM3Po0G7qWm2gdva_YPI8COymcL2pneoDs_R-XDrtZvcL2SOd67Cnl5Hfq6HXYEmF2ASjDDG-DvQOLR6rfQpyBt4VwgYEYutidD3dnnJR-MJLx7ilW-5mV-2djeh_bcuR9SAD9FjtejvCDklnikdztS0udXbZj_rGPjVdg_khGIflOz9q31U8NIgIynrthZbwP0LRXbendw7HGih0ARExf5YrEvjhL42rSNykNcCYZHTtYjmcVH5HGm2ElVOUOikD0ddyP4zNa9VZiQbvCmzhKzoxTYM1ePHCYQJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvF_Gb303CdHbTzPIsrWjGZJnniv99lBVYLwKuTQHJlUTnupTfE6fFAE4etJb-c88VmEkA5FxRIEXNUOLS74_xnHPMCHS62Ctwb7eAws7MBENbx-QW56XtCwAnlt7oNpwOIPiy_YGbE3xcN5P4Su3x6YiKEws6-3jg3knmOfzRZlWvXkBniyZFdtljc6ys5uspuvvwUBRm_ZVLQLEzFZfupJ-2xis6aoFJNs-DuQYX5yYR_j0XlrcFTz2pOZ-MEYkw18aZsrvFvwkuv1iGjSlboFgMawqcgcBig7dzwWi1uUDIeeKPH-2KFxnS3JQJK0XkCUNoQ1sl_qz8LgzVhYzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=HSK-vI8a7ZTQ504cWr_dLjoArc3_jNlx7PlGNzaF2EMyWJm-8SFuaE_r1ly5gZwkH17Y6k3l0PFyPn0xMFKThIe8KQmv9M_zwzB09MIkr5zuR4L5ig_f2pCBtFCJNlcna8BBOAmyYBtJM-K7ffWTQ4vCGLxynmax5_lP2QEGGyPfrAFWZllWF3qQyrY-k9dJZIX6j8FxYsjwQp2QW3ej_7MwLLC9918n5jj_nHyRKTdUQoA40vTKnhasm-IAlatRNTi1bStxqp0n5GzzRueyQ9aBByWxVUYgrZT7AzJKYEVy7vpCjuEZUYyYxPjxc1q4REybJjjOul933BXCBU23Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=HSK-vI8a7ZTQ504cWr_dLjoArc3_jNlx7PlGNzaF2EMyWJm-8SFuaE_r1ly5gZwkH17Y6k3l0PFyPn0xMFKThIe8KQmv9M_zwzB09MIkr5zuR4L5ig_f2pCBtFCJNlcna8BBOAmyYBtJM-K7ffWTQ4vCGLxynmax5_lP2QEGGyPfrAFWZllWF3qQyrY-k9dJZIX6j8FxYsjwQp2QW3ej_7MwLLC9918n5jj_nHyRKTdUQoA40vTKnhasm-IAlatRNTi1bStxqp0n5GzzRueyQ9aBByWxVUYgrZT7AzJKYEVy7vpCjuEZUYyYxPjxc1q4REybJjjOul933BXCBU23Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMYHD_WofISqR1I1r15b_k4AOK0sK-6uS0QZCqaUGsR8Utqpe_zFybmfo9OLZoyOlPT3u1bhMLwLNeZOfVS2QeX3Z1n7o6ErgVSICGAnypJINavkhK3So691j-HGrZ3pok9KBPAtrW0IdE3Dgc5cOYQa5xasFNUTlZqtSskQ6PpQNQSkVGn5YTPtKGnii9I1k2iKoXgXhDdUKXwG06jj8FrN0uhujiSUEMVn3vqmlMp5AwTGbKR9mmdTh5UwUVQ3WAD2CEgnDGGQfSzcY6-jUOD4XHX_f7E_TCQiEFsmZE7NrP1U5H7Bta8Muj3lamlSRIb2qVihbeApa4clBjNtKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exDE6p9JrA3U4j3JetNV8Hl8TwISG1zqUpdD8Sduo8MGL9UBXmTDsmKkwdZosJOgdX1tU1I6aP4ECMcqb8xsiDi85_aPoHs8uBd18-DDbr0BrX_XXJieeSWMN0u6FGjzv6NsATvvusNXQS0B13nPyQFhWJTV_JXfTVtgVfDgMF-0oa9cyGHSVmhGAeRs52cZ_OUmQjA0T5JveyP9ozw5ZGjSxfuU4_gFFtOm9Kc71lfl_3-ZbkBe_Q4GZFnBpytdCM1IyMn2-39m8zy4DSaSEIPqDonPVm3zanL8JiPFdjWXNO6Nb6fGNumawKpWFDeah6W9gPlC9AEOLp2_ZQl0PA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=l9OwoeYbd1ECXoOID74RSiP7B9jqtyvJwAmzDxQihxiSq-tJbkD46n8nBN2mKpLxMfN5jkEl9ULLtt_rXj5684GwuvE4zjp4nhOwOaVgu_l7x7zlryKqOqQDG6GOONS2T_e1R5HbK3qlXPqHqPIP5l84_APuQdENcDSYpOC_a3OJLQbJH5USr3HCPWJhB8nnS2qZRleIFRw2mXyCrKNHu5uO6e_8YOF2cC_8ZkwD8P94Zb9MXQYe-3QvFBJelzoEvSGXGl0EDP_1uCbcSXy6qcx7BrEyYI25XXm7hlBPple3_7pAvP_7BXjz0Y4hOkapeZXuuKfxlymcICd7pJ0yKLcW0lWxPm9jHUmfHXhOhds1SIjiCE7FbycKN1pT8pi2R1SGp5kZ1-4UbgGSwTHIHvdreeeBf0nOwfqDbIPb4Xfy9pQSPZZx74gCXPFFxrVodnaJHzysq26ch9vtvGMRflYnF01iJPqrEwy3k9JxHJ0W8E4pxQKMKU2F-dGHPqkEwTVrGE4b6TzL_kaVoXgPDKdK_fEGW3vvE4zcIoRYg4a5VSgIY0Luni9OtNBwvsKuZ-XLOcCxOe-p3LCblbEkVBKREtlauPdEeHyY_PN9A86mC47uUbM5DHXkTBL9Rh1rX0zQD_990aEbx5_uhxFR8gaWkYUsqZLEgAigvWADe7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=l9OwoeYbd1ECXoOID74RSiP7B9jqtyvJwAmzDxQihxiSq-tJbkD46n8nBN2mKpLxMfN5jkEl9ULLtt_rXj5684GwuvE4zjp4nhOwOaVgu_l7x7zlryKqOqQDG6GOONS2T_e1R5HbK3qlXPqHqPIP5l84_APuQdENcDSYpOC_a3OJLQbJH5USr3HCPWJhB8nnS2qZRleIFRw2mXyCrKNHu5uO6e_8YOF2cC_8ZkwD8P94Zb9MXQYe-3QvFBJelzoEvSGXGl0EDP_1uCbcSXy6qcx7BrEyYI25XXm7hlBPple3_7pAvP_7BXjz0Y4hOkapeZXuuKfxlymcICd7pJ0yKLcW0lWxPm9jHUmfHXhOhds1SIjiCE7FbycKN1pT8pi2R1SGp5kZ1-4UbgGSwTHIHvdreeeBf0nOwfqDbIPb4Xfy9pQSPZZx74gCXPFFxrVodnaJHzysq26ch9vtvGMRflYnF01iJPqrEwy3k9JxHJ0W8E4pxQKMKU2F-dGHPqkEwTVrGE4b6TzL_kaVoXgPDKdK_fEGW3vvE4zcIoRYg4a5VSgIY0Luni9OtNBwvsKuZ-XLOcCxOe-p3LCblbEkVBKREtlauPdEeHyY_PN9A86mC47uUbM5DHXkTBL9Rh1rX0zQD_990aEbx5_uhxFR8gaWkYUsqZLEgAigvWADe7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQhpjFIaWVr7Wsue2Wvlm6GunACxcUXhHtd-dqfqtN2d5x6vLbfo5f28KaVcqIwZg2FfdyAB0QRE3s55cwL1SU0Gup9Pc1BjqZlI25pisnYTd1BEdQGvZlxg7v0CgVL75huUF98fu4hnmCWf7D-ZWBgnatwo6UYTXJXqmETZnU8_-lHVM6jbpdUhXbw7xju5nTEwpRq6CZzSf-n5Rr_eaCyUHSJ_OI2swqMIpUbWzUbzmL0294Vv7iqh4T-9JvCkqgA93oa2lcgdvivMVnE_f7qbKNEA9CJDPuYFjoz5wMC7FSOcAZuHiY2HLFAP0MxDgRzV_vzbyYtgmJIajgDAew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DT5OKdH9R99IxOrf9VdO-3cbb1xlBjLfC84x3tujBzGAOiLJDvg2fI0w06kn6F_YyVWzmHbal-vXLemGCLqj6es7hmSIUVzdq1zaxvUyqoSbuQeS7SxceKrPR5SLfdXHwaQcUjfsOHDgnGZCwfN_pWXWPcZ04Gc8vVbG_RClMlcVlrCTZbZBsgF1KPNvBfB9quMRjzRmdservPXUc0Ns-GWWHQnrwVfuYQvHY05ScXKn4tLIyR8slFf8Lk13aqcEOwHoEsALVa_DVHnNhNdWsdobTzXcs9SUBJcHFThTaOa24hL8d6rVgYEF70Ul9IeMNom5GBD9pZvPHxgBSgBpdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=dG5TgRZOsJhNcZqk5hHENGRB-B5ZrmJlWh70jkJRJesRJoB61r_oCuP-k44OGqsV399hIBnpUIzKpt5tcEmC9RbEktOMWqZ-sLzBRhoYPx3m4nOF0k1LpQw7eHxcpArKaJHSK8pEbktPbkQy6TiRLjak-2RFP57lSQKCdB0rb-dAKZwkbENjkLoUDKbHkthj6SyyNtbuhL-b9vpjGjrBluSNDRDye2SCsLxf-tlCRBvWc4YjtW_eCqFYkN1CQpMKyJKZqZenbljF64BjhwU9JpGQFEDEGh5wAqZ8hAyGKLKQ3j5iGxmiD_81BmFc5cb91Pbyi4euNlhtCumziJIQPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=dG5TgRZOsJhNcZqk5hHENGRB-B5ZrmJlWh70jkJRJesRJoB61r_oCuP-k44OGqsV399hIBnpUIzKpt5tcEmC9RbEktOMWqZ-sLzBRhoYPx3m4nOF0k1LpQw7eHxcpArKaJHSK8pEbktPbkQy6TiRLjak-2RFP57lSQKCdB0rb-dAKZwkbENjkLoUDKbHkthj6SyyNtbuhL-b9vpjGjrBluSNDRDye2SCsLxf-tlCRBvWc4YjtW_eCqFYkN1CQpMKyJKZqZenbljF64BjhwU9JpGQFEDEGh5wAqZ8hAyGKLKQ3j5iGxmiD_81BmFc5cb91Pbyi4euNlhtCumziJIQPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=v5RTVCdH3kqNtECqCEFkSdrVhbQmDB15avRyydnOkKUpu6eiXTlD483Z3WO3wU0sqVCsZJNtTeHQvxI27jjzwWvrpbiQdHSazoTu7Wwg_UELb4-wVVJO8P2zJm995U5Joa1axZl5VAUxKCBKnBZeGkplzOi2231GXd2g9iOZwmAEfoRq738JY7d3aKmdlGqfdIPjz0fiLMuKg4OJQZamqTwtMnq0AvJUwGTMgVhASzdd0dqQnW9a2TsP3CZbZoUNWb6Hw9vYpAJpyOYThIGOP9na8lRB4BrPjQChVrx79tg0i6Vzqswje7NN72JL9AUGVDAvpJ-utdcj2xL-lP2Ewg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=v5RTVCdH3kqNtECqCEFkSdrVhbQmDB15avRyydnOkKUpu6eiXTlD483Z3WO3wU0sqVCsZJNtTeHQvxI27jjzwWvrpbiQdHSazoTu7Wwg_UELb4-wVVJO8P2zJm995U5Joa1axZl5VAUxKCBKnBZeGkplzOi2231GXd2g9iOZwmAEfoRq738JY7d3aKmdlGqfdIPjz0fiLMuKg4OJQZamqTwtMnq0AvJUwGTMgVhASzdd0dqQnW9a2TsP3CZbZoUNWb6Hw9vYpAJpyOYThIGOP9na8lRB4BrPjQChVrx79tg0i6Vzqswje7NN72JL9AUGVDAvpJ-utdcj2xL-lP2Ewg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=RFbSqWYj4U2APCwbev1c2vYWNPspBYD-Ek-4E30LEW0pgMwSC7ZLYrW7je_FScGk-fUytVXbrcXDnxmcyaMrNWSU3GK30xUWnxFhTdaTnQIveUpvlLLf5xoMZRJUqO2sFOtAGybew5lWwlVFOe0dJMIIeXKq2psE-nylTBSj3wEH3_jXePu2B22hy6dHivJpJ1zQUR3WUxFp6uNDzXHHPxdIeHxCGr3Ygwlh9PSJnPgjMVzBgBicxrOzNyBFu5dNzmzdMzj2hV6YLIedRTtPzsZhJj9LK50UKp5-4wO1zuV0Fjq4ZIivteAtBIOKVjzVrNt8UocakdW-6UPqRyWePQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=RFbSqWYj4U2APCwbev1c2vYWNPspBYD-Ek-4E30LEW0pgMwSC7ZLYrW7je_FScGk-fUytVXbrcXDnxmcyaMrNWSU3GK30xUWnxFhTdaTnQIveUpvlLLf5xoMZRJUqO2sFOtAGybew5lWwlVFOe0dJMIIeXKq2psE-nylTBSj3wEH3_jXePu2B22hy6dHivJpJ1zQUR3WUxFp6uNDzXHHPxdIeHxCGr3Ygwlh9PSJnPgjMVzBgBicxrOzNyBFu5dNzmzdMzj2hV6YLIedRTtPzsZhJj9LK50UKp5-4wO1zuV0Fjq4ZIivteAtBIOKVjzVrNt8UocakdW-6UPqRyWePQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_E5ZNgy-HXNo4LmcZzzRnv8HiLIR7SX9VcNUJyaGGX0upz0aNYQsuKSifxK-cwzq-KAnORreFmqxUqc6lUU0RfTxzdwaj7ggzpM4qwevpdE2wV1krKRMbHOfHH0F9dG8chDPI4RJA_LUk1Z3ZJosDI4LaCfeIYOwwkh8kAn9RUs29yxo1XuQRBagqGtAoyqh0Zu_hSaL_90lZfrPkKKNKBqWWVyuMk9d1LkFbuW7uMYTRmNyp8iRSjy3C86-IXjzJAu5OkP-wdC8ZWo1Jn-xalCq2eyNpYa8LQAI1ZUG41RlTh7Fu6KOIcl5jMXTn-39hGFmVouK1v2pMNqlND5gA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8CBT5F8OKPfxqt6yg9tdoeCXaho9eOtWlGlS7LCIep84DzPdqngbe-66hcYRQ0rhIzpbbIcyoDpvdOEkDUM5Q_gfcCbWeiHYxgqK-_7yUQCunSQA0DqNLm7SlHA--D4PuoIIxak_0YAWVt1VbUAvj0u3QvICXg6CW9pofmBdgFXklnWAmlsEe8SFoPHTkj-seZowUtLQYMldKCq3NTZdrezVzsbwXOTqpFdaJql-7Eh_0nnbod9iEVEHoYC7cg_5wB1gC-mqtoDcpZVqxD1nm0fI1_s3RAh-E1EBNmi4o70OZjSGGXlSQ_MMYNufctM3cNrcuIaCvBU1G1q-1ewZbFI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8CBT5F8OKPfxqt6yg9tdoeCXaho9eOtWlGlS7LCIep84DzPdqngbe-66hcYRQ0rhIzpbbIcyoDpvdOEkDUM5Q_gfcCbWeiHYxgqK-_7yUQCunSQA0DqNLm7SlHA--D4PuoIIxak_0YAWVt1VbUAvj0u3QvICXg6CW9pofmBdgFXklnWAmlsEe8SFoPHTkj-seZowUtLQYMldKCq3NTZdrezVzsbwXOTqpFdaJql-7Eh_0nnbod9iEVEHoYC7cg_5wB1gC-mqtoDcpZVqxD1nm0fI1_s3RAh-E1EBNmi4o70OZjSGGXlSQ_MMYNufctM3cNrcuIaCvBU1G1q-1ewZbFI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=QDFHWuhA49psCBcQyqhSkv7PvSFX7cQ0RcWbVj-bs-_9DfpQzS4d1XBnsfWPvqeFCSjHcsYawKneN09KBMxZeoyxCRwbVBxQ6wVM0wkupz3Ko9BVoE9W3Vup6H1quCqQKI3J48hSLc96XBAxrYiniIKq9Gojdas9TI-QiRyr9s_iqtnhqOOr5vsIHILF2uIgafDj87E6qG4sQTjIm1jmA1smCsPT0TYQGm-DTF0tmV4sT4g4dh8MCdhv_dC4_teyLTEN0fE7p7UWrQtEUXFSTjV0EV8aU_0wSPB1lhU3SLU-l4YoPLfpzzFyEQmn0859KIcpoql2gPrL3ITCE0FCVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=QDFHWuhA49psCBcQyqhSkv7PvSFX7cQ0RcWbVj-bs-_9DfpQzS4d1XBnsfWPvqeFCSjHcsYawKneN09KBMxZeoyxCRwbVBxQ6wVM0wkupz3Ko9BVoE9W3Vup6H1quCqQKI3J48hSLc96XBAxrYiniIKq9Gojdas9TI-QiRyr9s_iqtnhqOOr5vsIHILF2uIgafDj87E6qG4sQTjIm1jmA1smCsPT0TYQGm-DTF0tmV4sT4g4dh8MCdhv_dC4_teyLTEN0fE7p7UWrQtEUXFSTjV0EV8aU_0wSPB1lhU3SLU-l4YoPLfpzzFyEQmn0859KIcpoql2gPrL3ITCE0FCVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YN9ul0IAMI08Qi-D-VxOaKg4yQB2REQb4jeNbtW-0rlE4WL2ogFOoXmgrtD5mWkxK_YTHtn9sjeS5qqxh6IiEL0ow1uLe2pPZGP7XUnVJz4U-pUb4yuFj8M2pgfA485M3BXzBNp5J5II8eTZO1v4XcTxrWJVZ7LCgiXODAI81NHPDod8mU4CCFbAHzeP9PuyFx040n3fthh2OIuvjgmj2KPkNnRxwzr3To_3jMqp1q95sc_QdoLV8gLBiCk-sNrKhRsr80tjcGrWvE4A2yjCeh4tTp5YUsl2gehK-nl1mHRC7x5QzC6puGVeoLjsrO0YkdDwRTY3cUjiZXx7-6Doqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=XMtZ2qx-3mWZp5_utST3pPB11VhmEwIe9nTAFDxaKWiE3WR0w0jmC16cizNKFBV8paa5txG9qRsFDXYYAbEh6Kuj-ruQy7mU9gqpSo9RwRGCNQwyX2ygVLD9w3LU1zGImZMBFdTrYfoP4km82Hkim2NWSmjhPCBQRAP6-8DjqbYRuN6AzVmKRrAGSLsW7x1gmCouL3qz-_7fxl6fq7irKeitHu4aAhHER0mI7YEwODn1kMOZB727pe6Okj6U26lrS-KmRbtflYQ6re3bSMOMXljvdSOkEIsqwa-ovBrtdXoEsoSaM8b-FG8iWxbesh3dFDLd0eUdT1ff1r2oT_JBjlcQgUN9bU5LmHcXYVpGnoi6ffynIFW_equjffQy25BwDCH6HucEBRt8m32ozh294KJJE6j0vbd7u58vdALwnZTiWOISvSQR4k0ok2fyBiXroQ6RHlj0IErceMNdk1BUZv6fCSX_nDKu9ILavXlP9Zt1xva1EypO6VHH_NLnPfRBPRLAQytVF-x9QK-fYPclSDlTCorKCPOK6BDOpbpItYxaT6ZSXpCsljYxSRzgLQ8FvuX9XmTjOcw95XOr1Tx6NmeamGZnUanyvaofhRqDc3vx8rkStQczT9ajvEgX6TX_2C82U4hXqtfJxyR9FyyEdKDquGbh9pumzLPZhHYSNDk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=XMtZ2qx-3mWZp5_utST3pPB11VhmEwIe9nTAFDxaKWiE3WR0w0jmC16cizNKFBV8paa5txG9qRsFDXYYAbEh6Kuj-ruQy7mU9gqpSo9RwRGCNQwyX2ygVLD9w3LU1zGImZMBFdTrYfoP4km82Hkim2NWSmjhPCBQRAP6-8DjqbYRuN6AzVmKRrAGSLsW7x1gmCouL3qz-_7fxl6fq7irKeitHu4aAhHER0mI7YEwODn1kMOZB727pe6Okj6U26lrS-KmRbtflYQ6re3bSMOMXljvdSOkEIsqwa-ovBrtdXoEsoSaM8b-FG8iWxbesh3dFDLd0eUdT1ff1r2oT_JBjlcQgUN9bU5LmHcXYVpGnoi6ffynIFW_equjffQy25BwDCH6HucEBRt8m32ozh294KJJE6j0vbd7u58vdALwnZTiWOISvSQR4k0ok2fyBiXroQ6RHlj0IErceMNdk1BUZv6fCSX_nDKu9ILavXlP9Zt1xva1EypO6VHH_NLnPfRBPRLAQytVF-x9QK-fYPclSDlTCorKCPOK6BDOpbpItYxaT6ZSXpCsljYxSRzgLQ8FvuX9XmTjOcw95XOr1Tx6NmeamGZnUanyvaofhRqDc3vx8rkStQczT9ajvEgX6TX_2C82U4hXqtfJxyR9FyyEdKDquGbh9pumzLPZhHYSNDk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhXpy026fzhLhZW5EvKsm-yPalbOCyjeZu1hGVNcOUctqpqYcas2NWqasbV_z5rkK0-4GIqUJCNl1My9J_a-ponF4GBLPw-YC3VT55-G5R4fAn1hH8RNSGpixsWKVFDFVQc93niz5w5q8_IgGCEBvK57gg-2290ILHMTL2guJxxilnua9pOH3Zpg4qMclOr3Vw0MZ5i7wScFxTOYf6bRk_oj1bXMh8GCNIQTNAw0R0TQgolViYOmBLx_5xf0M8aZ5Khi3xjWulSDLu8nBo6YKldsqA5EMhfKAwR0nOp1WbBQUfdrvYENyBgtSaK-m0v3Avtk9vVJid4Ws7xucZ8V3g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=Nj2kewuA3q5PU0mbzBqTvn11nXovWY8wylufq6wvHNCNfsvZ2QumvI0ecu51R6AINA5f6eikUIAAyE_mXrAshR-GZG_ix14qc7rvZecHjOBJ6nWrd2nlR4XTNTCABabXizgomNFH-5C09_muMBlMqenW1_zfCnC4VNwvnRicq-LQYKpUyEhm-Vw8MkHCo3Ca8E-8EG5S8FoFWh-AqONHR2MqDKWzU9Jco4Q3FRp3gG3tYIBRVJSA7jnYnHkHhQHU-EXo0gJivW0VNUMrBCu0x_0rigOcrdOXUiSnTBNCYrAV9lZzbsj0oPuPDFe-yC898-mQUkzG074a-olFAwM6wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=Nj2kewuA3q5PU0mbzBqTvn11nXovWY8wylufq6wvHNCNfsvZ2QumvI0ecu51R6AINA5f6eikUIAAyE_mXrAshR-GZG_ix14qc7rvZecHjOBJ6nWrd2nlR4XTNTCABabXizgomNFH-5C09_muMBlMqenW1_zfCnC4VNwvnRicq-LQYKpUyEhm-Vw8MkHCo3Ca8E-8EG5S8FoFWh-AqONHR2MqDKWzU9Jco4Q3FRp3gG3tYIBRVJSA7jnYnHkHhQHU-EXo0gJivW0VNUMrBCu0x_0rigOcrdOXUiSnTBNCYrAV9lZzbsj0oPuPDFe-yC898-mQUkzG074a-olFAwM6wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaNbBjRyCrRg8e-Ws0njQCXi-1pl_I2nNyuLOx5PFsidtSH_UvHqo6tNqaGuMefUhRurMdnVNCeTSjLPRw5rdBpmkp4hoe39mB_WdfZUGy4qilFXV7Y0TGIcdqHzPvOfOnCveIP03_ViQBli1zoK9oky2-kUxOCE6PuNoFrOnXz2TsSkLwDt06rDLRRYxqUK2q96VNYS_F34j9woQlWszBSpOrNF9pWkmvgQvgvn53DrpCBvcj4otQJ4dnxnopo6vLVvp3fnr5tr_kC4g0T-fM7y_c7df-lRtJ9TdvkJtklzAwNC7hUn6ITGUeuH9KZ8OCNFBgWKpzGgl6RnGsnFpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ha-3wW23jNd5gPPdrEcuKQ0GyMDrjNVf8u_Xyjfhcq4Cmvr11T1E4sbz100yWmmOpaSMpBzuBEBrKuthyuVMYxwsWoS6ObS-_pqXYETFa3J2AAMZNOmDzH3nCyqHo9mbEUUj7tlscsGiPQ_m35PdOkpdZUaJq8FpCkQHFDpB6jns2UV3CUFtajh6lyEurBnCe_0PEmjO_TjvekfR63GLH-jjoIPurng8f66pqZlp3z6A-OFUWdnzEPYCUO79fvsdr_VvhG3GoFiuZsb59WzuCf9b-_GPcXAur1yGYaDFPmCBVOHFhSLzL9L5k6D-BArfV2OOHwZNtKGqmTHQDzHgAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Biypl7v0agSF33zixhW_9s9VCrvSzNVpfHu7rIgwg7e_LC3LVvRdlWpY3miL9T879Gd5DBRVGpHIYNOxa8OU6pNJyInbAWNnzbp_I-cQDNmSAfhxAxKGxrsqLEDGbUulZadRqLqo79fAuSTejdK0mwckb9WO0vraFH01b_GrtY6hFB1ldyOS5n3fadMpgnWykn9FVLmtvyUJjsMVYCeV5d-BSxqZhzvuRhF_mR0WAzwcl4sVCMrtIsUx6fcvy-T_jWetp_wx1FwGCSS61E6rEMBkn9WlytLRGcvlg3yc_VkPmFKcI3SbTlx1zEMKL6nhM8T86pcUGGQQ13-aHX4F1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=hZBzHpc6U2DAH99vL1jpIl9TTQG6kNpnRjKbIaVQoaOhXztXkuEXIKUWD3kbQ9ZWRDXxGtVA25yCXZilS27cU3fUyz18siEo_w3wc41_wpCCH8iACgvvnqVSi08JKsx2hfBdEPV4Oqi9OhgsjlI0GcUHSKmdzbrhG72gnUwIiuodTMJibgfoA2oTG8rmgiI7dPX8ei0mgbp7aAxzlszJ8SoVy14uo3Y_-dnjJqugZbvEOdIA6aAzJKFSsoUQqLDt5MRbPVkDXTmTkxyrCQbPyAP3vM1NgO5P2vjBbTo32QCuMscwiYQ-IdrfAFcRuxx7cwmq67YsYdYL2GuSo-VZIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=hZBzHpc6U2DAH99vL1jpIl9TTQG6kNpnRjKbIaVQoaOhXztXkuEXIKUWD3kbQ9ZWRDXxGtVA25yCXZilS27cU3fUyz18siEo_w3wc41_wpCCH8iACgvvnqVSi08JKsx2hfBdEPV4Oqi9OhgsjlI0GcUHSKmdzbrhG72gnUwIiuodTMJibgfoA2oTG8rmgiI7dPX8ei0mgbp7aAxzlszJ8SoVy14uo3Y_-dnjJqugZbvEOdIA6aAzJKFSsoUQqLDt5MRbPVkDXTmTkxyrCQbPyAP3vM1NgO5P2vjBbTo32QCuMscwiYQ-IdrfAFcRuxx7cwmq67YsYdYL2GuSo-VZIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6RHktceAzB-lba9HpfzuxvZY-I8qkdgyaccvkfEF0R_YbNnTawvvU5oPJ7a8kXT7WkE4BWivIEt0MMju2yjbc2aa4G5C3bPPp71TR6zRlZGJyV_NPbLvdeYWg_wQ--NUY47gejNDDa3lA3h5pgzuqKGR1trV8ShVtaxHQdvdI9J4C6p73ZCuHr3rq7q1-2hgZlJrnSs5Nc8JRC1N25JGYklckwDFgTRltrvtwYat0E8BoxIcezb4j4xU8dfyAXy7skqJYCZrWYTmVDn5Q0pkaybx9UtaYAT4H7Auz4Qsmq7DuFkNsqgTUdIgPWBEXlcupKtfRjGmXxl1IeltqpubA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFLBqiY2Vxr5i7au5Dnh_ocGCnBWte9Zcy_Fz8odbxBv3dduof3gEXkrTOXcp7KqOLondEj7Zl-vVEA_PvvqrCae3B0Q94YepCD5XjVfN1okhtj5IAPyA3EvZQlhZkQmoNt5j4GEsk91B4fW_COJQRdEep4c73PfTfvWdXyJkYh6NdkHWOUOr7QPE2hsaLCcCkQlFvs0kQe0JdzbZRcNPadbkeo_eISWx_92ascHWTK3jsp6mUycV4U4zr_BqPObUB35TwJu9uyGQd6zq_cvmephkhS3kIGjUiG3SjNk0uIfpta80GL8BRlvK3NJzGiSFaBIYWdF8liapGXuKGjqSX1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFLBqiY2Vxr5i7au5Dnh_ocGCnBWte9Zcy_Fz8odbxBv3dduof3gEXkrTOXcp7KqOLondEj7Zl-vVEA_PvvqrCae3B0Q94YepCD5XjVfN1okhtj5IAPyA3EvZQlhZkQmoNt5j4GEsk91B4fW_COJQRdEep4c73PfTfvWdXyJkYh6NdkHWOUOr7QPE2hsaLCcCkQlFvs0kQe0JdzbZRcNPadbkeo_eISWx_92ascHWTK3jsp6mUycV4U4zr_BqPObUB35TwJu9uyGQd6zq_cvmephkhS3kIGjUiG3SjNk0uIfpta80GL8BRlvK3NJzGiSFaBIYWdF8liapGXuKGjqSX1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=Vbit8HBYjEWwgH8rHFF7TSDTxyhr4Um7vnCR5JBoFk5IXRWnjys9MET35_9kgmvsbTFwjERsYEUjCWzQwv_I26yHysSKlyt6NREbSUozS7Fo6XX-BftO2jX0MF3T9cUV0agWuoflYqPOdZxp_5mRTGK2FiYcaTd0Ulcw8ROTd7AoY8fXA1gK2PaqWtQtVRh2UGC3pL_OpuYGHp8mbQUvblicTxThRnDfTDBtOrIRd7eOTyZ6l8YfqXAL0Yz8RrbAjrTHKPXKgeUS3pqCxYQq4FfcMqnUV9KIxmBCMwbHI6Z9in7V9jz4yqQgPx1z0rUSt2jF388FP3dwUTH_lEquww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=Vbit8HBYjEWwgH8rHFF7TSDTxyhr4Um7vnCR5JBoFk5IXRWnjys9MET35_9kgmvsbTFwjERsYEUjCWzQwv_I26yHysSKlyt6NREbSUozS7Fo6XX-BftO2jX0MF3T9cUV0agWuoflYqPOdZxp_5mRTGK2FiYcaTd0Ulcw8ROTd7AoY8fXA1gK2PaqWtQtVRh2UGC3pL_OpuYGHp8mbQUvblicTxThRnDfTDBtOrIRd7eOTyZ6l8YfqXAL0Yz8RrbAjrTHKPXKgeUS3pqCxYQq4FfcMqnUV9KIxmBCMwbHI6Z9in7V9jz4yqQgPx1z0rUSt2jF388FP3dwUTH_lEquww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=vAS4J7eA7LHQPW9lspzDis58hq4rx_JesehNCfdBHX1sgqa9Q9sVSQi_SixVJBl_zC0Cwg6e2QZRfywfgOqVKnhfl3t1-SeUFbk5mZbhr2VAlyUjIynsXqElrWsIHWEqQQ-JYf1Q9LG5aIAo6dA5NswPyqKs5RwY3tB8qS-Lyaa1sVCDA2yF2WpWU1TQfRp2CZtCpAOFEuzsdpSinOBOoQ8FZsfzyBrs0QS1CGRQngWrTzRr6Cl28CXtAi1cBdcEP6sAG4_eWFmcN4wiTHbFYrh6opXB-AT-AptRQhNQLTvSydZFqhY1VdG2rrFyd4XoQiElvhWJDQvV6MZSpDz2jLgWKDcH_CKvPe9CTNS9BgIMe8fVO8fhF25tYlTQ2KaAB7CGzeQ3eaU5HrNaSNjxoforFVRz_SMYm7Ux-PsbFYPy71MSxrzrsBILCq_PJq18uXEW28Wfd6WewZhbprl_2YXT7RvJ4gNqO_nsVMHLW-85IL-isHPwIq30EzZGbbM3tzd7-WtoOZkX-VsoO9slFgX-CscYcjmP46E5xJYXqwPM-MlpxnC8vxMnpNbJTyI6bIR61-QPOnJ-9fyyJwMH-QPoBpZoM03Csyy2WXDTbqXaZ0cekUrbkoZ-nUXIXlTQSB75-2XKFtSIjRCGiJd-RpwjBNfMRuEhyNtVQwEJd70" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=vAS4J7eA7LHQPW9lspzDis58hq4rx_JesehNCfdBHX1sgqa9Q9sVSQi_SixVJBl_zC0Cwg6e2QZRfywfgOqVKnhfl3t1-SeUFbk5mZbhr2VAlyUjIynsXqElrWsIHWEqQQ-JYf1Q9LG5aIAo6dA5NswPyqKs5RwY3tB8qS-Lyaa1sVCDA2yF2WpWU1TQfRp2CZtCpAOFEuzsdpSinOBOoQ8FZsfzyBrs0QS1CGRQngWrTzRr6Cl28CXtAi1cBdcEP6sAG4_eWFmcN4wiTHbFYrh6opXB-AT-AptRQhNQLTvSydZFqhY1VdG2rrFyd4XoQiElvhWJDQvV6MZSpDz2jLgWKDcH_CKvPe9CTNS9BgIMe8fVO8fhF25tYlTQ2KaAB7CGzeQ3eaU5HrNaSNjxoforFVRz_SMYm7Ux-PsbFYPy71MSxrzrsBILCq_PJq18uXEW28Wfd6WewZhbprl_2YXT7RvJ4gNqO_nsVMHLW-85IL-isHPwIq30EzZGbbM3tzd7-WtoOZkX-VsoO9slFgX-CscYcjmP46E5xJYXqwPM-MlpxnC8vxMnpNbJTyI6bIR61-QPOnJ-9fyyJwMH-QPoBpZoM03Csyy2WXDTbqXaZ0cekUrbkoZ-nUXIXlTQSB75-2XKFtSIjRCGiJd-RpwjBNfMRuEhyNtVQwEJd70" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=LujdoImyHm3SrpouTpr-_4oDcEFTaGclkdRs1BaHywWV4lKAXYkQTu6GBwVkaM5RG9T1REePUKf63Wqy474hbxHEH8wngxCTgtQuQdeDSVtbCgh-I7hyFIoWICYm3aSLdYeGSOee_Bsqcs0OjzXBEzLGhP_Oz_jfMj5wvCOmF62S92qukanUWX-uUX3TxLG5tIC44yVsNjQ1U2Joc1BiN4fD7BPsWxbJv145uNA7Fxez9ZhnoZFVV0LaDl5EnIfYe7_eLdcvzCxmCiIF6ysiP7lcZFTa398GPYwpk1OW4Z5KWaSZPMp-6eJmNCr1B1Jx44pwPog11psHvDzAWt3QvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=LujdoImyHm3SrpouTpr-_4oDcEFTaGclkdRs1BaHywWV4lKAXYkQTu6GBwVkaM5RG9T1REePUKf63Wqy474hbxHEH8wngxCTgtQuQdeDSVtbCgh-I7hyFIoWICYm3aSLdYeGSOee_Bsqcs0OjzXBEzLGhP_Oz_jfMj5wvCOmF62S92qukanUWX-uUX3TxLG5tIC44yVsNjQ1U2Joc1BiN4fD7BPsWxbJv145uNA7Fxez9ZhnoZFVV0LaDl5EnIfYe7_eLdcvzCxmCiIF6ysiP7lcZFTa398GPYwpk1OW4Z5KWaSZPMp-6eJmNCr1B1Jx44pwPog11psHvDzAWt3QvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-7AKCN9RM1uitpIqoImODQ6IzxUzsCJPnCT-ecB9WXYynW7dBck_asxfz05NqAXdWmasjTN_hn-OtOPU6H2Mm3UJbLSrmunQQp6bvcMsstnAA4SKxBZdf7q_c1BurKx77OOG_RXktzrD6IIKu_6ejlpEaXeLycFxuAZDdXvckLZfSL3GlLq2qHstexzlG2LUnya4ykPaVYRPk3qsSBGN7VQ2Sd9HgQNzXCfYgftT2jxp6zmLFPlwTFpesbyB-OMX6_rZn6QNVJyzE2C2VNUOUnVeo0zmD1wPBBAkf1a21DUDVgPjDMn-XRG3ZX-CQP-FJR44_74TImBP_iVAlUHvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=Y6uJAsYd0kXFM73L98K_mFt8kt30miV-0X1b_GskscSW4DYpW3sbfoQyYTutYSlsu6N9D6w4PCzMWqJ7Ig0oQdoBxFIcY4FhMcK1-O1uA0MeSC_6HRTvtJWLCD6WLGN71FtD8HJqnavgpdSuqVz4EYqXwqWW38rCI86Cotz1kgfqbzCZyK4bC4XEoROMXBVYajimJTrRv1n3LsazIidL9bA2ZxFPQdAblrkGGojyQdBaIyQQpJ09JmRT19t3yt5OGw95fBD2WmNbFx74twx0L8G509-kyvn2Ufs8lddRKvBtpmJIKAPCFAIRNOjNJseUDOZZ7wLHHBtu11opFYwADQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=Y6uJAsYd0kXFM73L98K_mFt8kt30miV-0X1b_GskscSW4DYpW3sbfoQyYTutYSlsu6N9D6w4PCzMWqJ7Ig0oQdoBxFIcY4FhMcK1-O1uA0MeSC_6HRTvtJWLCD6WLGN71FtD8HJqnavgpdSuqVz4EYqXwqWW38rCI86Cotz1kgfqbzCZyK4bC4XEoROMXBVYajimJTrRv1n3LsazIidL9bA2ZxFPQdAblrkGGojyQdBaIyQQpJ09JmRT19t3yt5OGw95fBD2WmNbFx74twx0L8G509-kyvn2Ufs8lddRKvBtpmJIKAPCFAIRNOjNJseUDOZZ7wLHHBtu11opFYwADQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=uFlFcYiYRk9HRCdtfVpnVpW6qXnrvTiS7ndA2hQGHbt_cBnox5CfPskiHBrhoaKiMFCI7uIYZnHlrL8uglYs4zTItpdXjgQGPORHEcCiE51m8NuC0A4w2KlQ-mDLHuKoiapXDVlQqRyys-StQ7a94xOFjckJZppY4RgeGSiDcRvzAzKkxeA3-4Yq5dtPJf0hGv_21LZxp873E6KIOdaIE53fxQ9AK_Myg41BsGdJWIy4shu8dDv1jENR1rLsSz00jeUkgNQiODMtUlS-XGc-2Q0jxdgFt7KTxJaBl5rnBngupr9paWZp5BRZ9sADZAWrPZ0n7YPx6OrgEE4rpV3WX1mbDo8fPNcXly75ghdXaXOVQ8Rg6bp38k6SNcR7mrk2__54I8FQY5_tzOJiAhPbASzsOZi65d12B61Ga72Yo0tOaLkpEIToVHIeWIdIw9UhfmHV9lLqDJPu54JGVq0MKqekV13_ag8t7yoNVmAebsy6NdOn3IYI1t5S17C8BT5KbbuvlaYC9IqwWKMZT3bLItthjmuB-uf3zBvllsY1wODbaC7tiWfizxEDbH62JUSvBcujMRGcx4pWkRzmViGe0nMNidGIknqdk6adL1pU_xT5wpgSzvC0xk0XS_dgBoDi4AcdiV87PjoUpSOZCwVwjPxIcX7_Dp4Kb9v8GKLNjXc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=uFlFcYiYRk9HRCdtfVpnVpW6qXnrvTiS7ndA2hQGHbt_cBnox5CfPskiHBrhoaKiMFCI7uIYZnHlrL8uglYs4zTItpdXjgQGPORHEcCiE51m8NuC0A4w2KlQ-mDLHuKoiapXDVlQqRyys-StQ7a94xOFjckJZppY4RgeGSiDcRvzAzKkxeA3-4Yq5dtPJf0hGv_21LZxp873E6KIOdaIE53fxQ9AK_Myg41BsGdJWIy4shu8dDv1jENR1rLsSz00jeUkgNQiODMtUlS-XGc-2Q0jxdgFt7KTxJaBl5rnBngupr9paWZp5BRZ9sADZAWrPZ0n7YPx6OrgEE4rpV3WX1mbDo8fPNcXly75ghdXaXOVQ8Rg6bp38k6SNcR7mrk2__54I8FQY5_tzOJiAhPbASzsOZi65d12B61Ga72Yo0tOaLkpEIToVHIeWIdIw9UhfmHV9lLqDJPu54JGVq0MKqekV13_ag8t7yoNVmAebsy6NdOn3IYI1t5S17C8BT5KbbuvlaYC9IqwWKMZT3bLItthjmuB-uf3zBvllsY1wODbaC7tiWfizxEDbH62JUSvBcujMRGcx4pWkRzmViGe0nMNidGIknqdk6adL1pU_xT5wpgSzvC0xk0XS_dgBoDi4AcdiV87PjoUpSOZCwVwjPxIcX7_Dp4Kb9v8GKLNjXc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUwwb5r0CWEsKfzklErVrWwsjfNwT4ghMDKaUMV0khSGx4q9uJKvk6O1vhFxW8mPfGTQJEQd5vQhrFERWcbMPIaV5aJf0v3uNqop5mv0Mc0WvpjAOZJFg1YbDYr_kjUPOGH8c3o9HOJp1L4S2xEYbmH1WGtZ4HoXRCahc3fxHZYU2pr7TnG4mrUYaoEwgDysBWIqqhrC7NDZG_ekaJ63Sl8npagkBFXxk-xW2IpemTB8IahQrbY5lAIJhVc2LT0dDsyL318eOsXNkODfSdLMzYDKyRG31_fkUbo96i3cCzEmBsD5EdEzAgotFmklCS3_dP-1XH9IQvwfLAIj7mThLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=KY8Q3w3pWiunMMuBUqipY1so29FwLLm88VA_-1egYz-sEp_R3zCLSMPnwdZ-5qxmwMCS6xKqLiaVg7MKmiIiNXq-EjvOwjkrj0d_E4wwuw8NSP1dPKiT1L7K_y6-lDcDE61MjciUay6hgItzxku_gPkyJm9gI7V4rzOa-h4vtDbQ3uVoSMexTXo8SOWuZf2iOT0R5h3Hi4_w3AJEmUVemBuWeEFg6ADiGJv2p3XXv5pLCnkhZQspj862vGxu2q8w6cjJHsKXxGEnQmyRn1itPQuhIv3szFzsSRvq5Cm-ysFeix1LBupe-eRjfkfF9CZaIsU66SZQdJ1w4OnIVWXsn5oD2QsaFkf6_YcVpda25WOkb2ulUYxCugufET432MuK8jyPL4urcG73WUatBEWa9wB_6E37fzhf-2tl6UDu6LRG3DcZvLgrebDM1Hh_ZTy17etuuVTAWi5QXx-vHvyy--0eDdN4lYrTEdSS3oo0AavxjViOUOtX4qaqf2AaC3TgG56oPscPDp5g6tq5PMLC8ikXVyLW2S85hxmR3kFbWCNOlOL7ZUtYr6FWRdmn8d41I170QNIJJFKfnoGIdsUvteDllnXp9-xNsr8YvCJLmmZbNfmDJtwb0KyijVNnmgehIyKO5gPGroURM1n6Xokbrn4LooGtPRMl0FODZyQbHbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=KY8Q3w3pWiunMMuBUqipY1so29FwLLm88VA_-1egYz-sEp_R3zCLSMPnwdZ-5qxmwMCS6xKqLiaVg7MKmiIiNXq-EjvOwjkrj0d_E4wwuw8NSP1dPKiT1L7K_y6-lDcDE61MjciUay6hgItzxku_gPkyJm9gI7V4rzOa-h4vtDbQ3uVoSMexTXo8SOWuZf2iOT0R5h3Hi4_w3AJEmUVemBuWeEFg6ADiGJv2p3XXv5pLCnkhZQspj862vGxu2q8w6cjJHsKXxGEnQmyRn1itPQuhIv3szFzsSRvq5Cm-ysFeix1LBupe-eRjfkfF9CZaIsU66SZQdJ1w4OnIVWXsn5oD2QsaFkf6_YcVpda25WOkb2ulUYxCugufET432MuK8jyPL4urcG73WUatBEWa9wB_6E37fzhf-2tl6UDu6LRG3DcZvLgrebDM1Hh_ZTy17etuuVTAWi5QXx-vHvyy--0eDdN4lYrTEdSS3oo0AavxjViOUOtX4qaqf2AaC3TgG56oPscPDp5g6tq5PMLC8ikXVyLW2S85hxmR3kFbWCNOlOL7ZUtYr6FWRdmn8d41I170QNIJJFKfnoGIdsUvteDllnXp9-xNsr8YvCJLmmZbNfmDJtwb0KyijVNnmgehIyKO5gPGroURM1n6Xokbrn4LooGtPRMl0FODZyQbHbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=gbPWGZp__nDb6yYWqKjJZrr2G3pv7Ibp5Rq1ul4lNXj0UURLMXtgGqOK8_MfnSgjn-uzuw1aohLCVzaln87ZwOxQbs9dg54AS6tFtklCf3YGRp1-xFcWhF9hkri_Sv15Yyb-sOw_MZhM3-X1rqhoQYQ2N95MTR2GNbGbUwiqTUjG6f2_oBlxupjklrCkDnYHOOrUj7EbDsQpLRcrXhGOTN2nunukkp8A-3BvTAacM9KKcrbSxcAxv5X5Yb0DCOP-OCRSn36Jo8RocF075bT9N5f8v8VloycpJ-GIPVMoUYvYzCq0qdo9GHt8QE5T1pic86V6Hx6VY4xh1GOOKSSaGzN7tJlIz_pVyHXtLMqC9voZrzk09a79bVrQnVJsRySEdogC-QMgeZL8hfo2mLEaCpl5EEqRGmzgF9qqG4JwnFyLrRDWUnyh6NU02hOIUnhPEYLPJXohwg2Dm9Dk8BuF28K6PLe3qtHDZoYo9GzMs7oHHwUxKgN23UrHYaMP05LxOa0oy6UQGvRP8aOwxQMitI56FLqKyvMS_KKrARmvG2dx-WRlslC919B3laUnjFlAQC2Oz4FMWZeU_cdujN0UdXk_Yx4phoGMaoj2jlsDF8b5JQEGxeVgNYAibkaUeOpj_x9hgKm9Dx70mLtXM_GFnQzXgmJrVhof3bE3jN10hkM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=gbPWGZp__nDb6yYWqKjJZrr2G3pv7Ibp5Rq1ul4lNXj0UURLMXtgGqOK8_MfnSgjn-uzuw1aohLCVzaln87ZwOxQbs9dg54AS6tFtklCf3YGRp1-xFcWhF9hkri_Sv15Yyb-sOw_MZhM3-X1rqhoQYQ2N95MTR2GNbGbUwiqTUjG6f2_oBlxupjklrCkDnYHOOrUj7EbDsQpLRcrXhGOTN2nunukkp8A-3BvTAacM9KKcrbSxcAxv5X5Yb0DCOP-OCRSn36Jo8RocF075bT9N5f8v8VloycpJ-GIPVMoUYvYzCq0qdo9GHt8QE5T1pic86V6Hx6VY4xh1GOOKSSaGzN7tJlIz_pVyHXtLMqC9voZrzk09a79bVrQnVJsRySEdogC-QMgeZL8hfo2mLEaCpl5EEqRGmzgF9qqG4JwnFyLrRDWUnyh6NU02hOIUnhPEYLPJXohwg2Dm9Dk8BuF28K6PLe3qtHDZoYo9GzMs7oHHwUxKgN23UrHYaMP05LxOa0oy6UQGvRP8aOwxQMitI56FLqKyvMS_KKrARmvG2dx-WRlslC919B3laUnjFlAQC2Oz4FMWZeU_cdujN0UdXk_Yx4phoGMaoj2jlsDF8b5JQEGxeVgNYAibkaUeOpj_x9hgKm9Dx70mLtXM_GFnQzXgmJrVhof3bE3jN10hkM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=IUB6asYK_cXwg8eLoaHEqD6MUH9sUsGTPKkELdrXR6KrXbB7ngiscXSELC6iVKRBMDxQ6CE7JiOP5_BCyDk7nQmqjePHx8m9dKSCjLHNKVtdndPQ9gciFDNeE5bVsePG0YdQvJ-6_NpHPElaGmj94-_fatFgRYABj01H7YoO7jXDerDgjHoWmglP6fULp0PGomAtMztbIkXdw8Yj6nUxNdlfHxHkAnK4kSAy94DvaGl76PbZcAKbzHC1j1qsWFsa9r3laZOFBVH_zCnCDSry7W4cxA9s-OB18cQLNsR-H7Pt0dkfkz0hG1D4HtzQKSmxPtmjx5Qp-UMjpw6FoUtjYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=IUB6asYK_cXwg8eLoaHEqD6MUH9sUsGTPKkELdrXR6KrXbB7ngiscXSELC6iVKRBMDxQ6CE7JiOP5_BCyDk7nQmqjePHx8m9dKSCjLHNKVtdndPQ9gciFDNeE5bVsePG0YdQvJ-6_NpHPElaGmj94-_fatFgRYABj01H7YoO7jXDerDgjHoWmglP6fULp0PGomAtMztbIkXdw8Yj6nUxNdlfHxHkAnK4kSAy94DvaGl76PbZcAKbzHC1j1qsWFsa9r3laZOFBVH_zCnCDSry7W4cxA9s-OB18cQLNsR-H7Pt0dkfkz0hG1D4HtzQKSmxPtmjx5Qp-UMjpw6FoUtjYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=AmSJIzwEnpQjAgzbURLo4uKD5Wsj5DoS093R3fPTrmq2emOHOeQq3wGsiEUBFY1oWqQUqNDD6f79ir5mXoORknw85ZrMGOrU7kzmlmOH0GqPEN9qepLuR9wDyVd0cbxCY9t5_I-w4vZ_ZqBif5FqhuwBLZ9wn3xjASGBgmAiNa31zXhuMwu3BAuEsqtUPBS4DNYkzNvbfU6dtO9Xg24s9fSMAS00mm6-86QOqBTxUTw2mRnmIW_4Oqf3z_LuXcfImszoW3AAkJRdR0GhOEbFOgbTPslGzm8Ho-O_RaL-q368AluC8wieQ9cRQ3jpykMwkTfsVZjpcPRIWh4eWpi8kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=AmSJIzwEnpQjAgzbURLo4uKD5Wsj5DoS093R3fPTrmq2emOHOeQq3wGsiEUBFY1oWqQUqNDD6f79ir5mXoORknw85ZrMGOrU7kzmlmOH0GqPEN9qepLuR9wDyVd0cbxCY9t5_I-w4vZ_ZqBif5FqhuwBLZ9wn3xjASGBgmAiNa31zXhuMwu3BAuEsqtUPBS4DNYkzNvbfU6dtO9Xg24s9fSMAS00mm6-86QOqBTxUTw2mRnmIW_4Oqf3z_LuXcfImszoW3AAkJRdR0GhOEbFOgbTPslGzm8Ho-O_RaL-q368AluC8wieQ9cRQ3jpykMwkTfsVZjpcPRIWh4eWpi8kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=QT6Y6ijcVSG9rN2yjZ8gSDuYlUDRMW5JWcAdFSoKcizVyaagu3XX30YmDc5aLCbfZhv7HuMLhWvYQugloBFnaOgJvX3NgUyIil_8PfxjcSuzqSyCZcsP4k-YuC-jWC516Fi0Pj9PRgX1kYm5BhXgxem5s7ym2Axmq8-Hx-SuyCcQyZ0mlTN8v1H0I5-hzSfIsmxenF6u9gZL_7rU_p-bX4LYeF-ew0t5_MXdU1uy8SaY_roKoN44kWsBZU3IAMUlqg5CWEYuqpHIlMNUZHM6CcaXFnCh3GGedc-gp75aYXf3S5PhIBiggb4IONXb54Abgv4SLxqIQs8mbuufb9EcPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=QT6Y6ijcVSG9rN2yjZ8gSDuYlUDRMW5JWcAdFSoKcizVyaagu3XX30YmDc5aLCbfZhv7HuMLhWvYQugloBFnaOgJvX3NgUyIil_8PfxjcSuzqSyCZcsP4k-YuC-jWC516Fi0Pj9PRgX1kYm5BhXgxem5s7ym2Axmq8-Hx-SuyCcQyZ0mlTN8v1H0I5-hzSfIsmxenF6u9gZL_7rU_p-bX4LYeF-ew0t5_MXdU1uy8SaY_roKoN44kWsBZU3IAMUlqg5CWEYuqpHIlMNUZHM6CcaXFnCh3GGedc-gp75aYXf3S5PhIBiggb4IONXb54Abgv4SLxqIQs8mbuufb9EcPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=rGLhePlX9jrGI9bErcg7OvqkOxYzjjuR-LZoaPLfqRB0acoZZMWJvuEbhU9qP1nLeaA3S5R1ejwTyUmhvnoY1MSLsCnIGIEB_0cJPMTgKqtGqJX_Du4qDPBp8Rh6Yc6Mhk-kmzcsrMxCOrri_az09zbS4PIXIpFRp32jrVSx4lt0MThTdF3hgka787GnLXcIsY3EkPKr3RGmxq2IZk8bnTqp2MdluL2UXwdmBWoC_ThnY1nBotl5EaIvrhtZuhdZ740zGJ-3HMhMr2GXnOrzSYqfZ4Ya164Vw6Xx6_d3lTBGAI1UrMnnVXKM-tCd77T-ExUKLV3arIOrB_BCibbE7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=rGLhePlX9jrGI9bErcg7OvqkOxYzjjuR-LZoaPLfqRB0acoZZMWJvuEbhU9qP1nLeaA3S5R1ejwTyUmhvnoY1MSLsCnIGIEB_0cJPMTgKqtGqJX_Du4qDPBp8Rh6Yc6Mhk-kmzcsrMxCOrri_az09zbS4PIXIpFRp32jrVSx4lt0MThTdF3hgka787GnLXcIsY3EkPKr3RGmxq2IZk8bnTqp2MdluL2UXwdmBWoC_ThnY1nBotl5EaIvrhtZuhdZ740zGJ-3HMhMr2GXnOrzSYqfZ4Ya164Vw6Xx6_d3lTBGAI1UrMnnVXKM-tCd77T-ExUKLV3arIOrB_BCibbE7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=mMUys_FlNakhAEV9G5bubT83VGTc0MfFgz2-2EeiSe55sXRfVJEj9fofoEpJgRX2qQcvxBWLI7DNx7Ods5_XWR9UOoxM4VKkI8oaFxwrV7xe06Uz-eSJMtdtP-jct3eVbZNcGmjmMy-v5l_ZHLyvL_WYM0UZtETXcL1sNM7O2kTX7huy7vxfLgjR5bodt8kvesaGgXCyWg-R74pMkmF5ExJ6n4r6W0ZvuC-E06bs3nf41d_fepMOFJOCHtrB6jZQSueur4TJgBJYijFqGhfKA2yO3tU2Wa5-JIahkdoUcsRi-gcpZ6ODJG4SKgOsuLfXcD3yxpx0zDvLGaz4wQSwZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=mMUys_FlNakhAEV9G5bubT83VGTc0MfFgz2-2EeiSe55sXRfVJEj9fofoEpJgRX2qQcvxBWLI7DNx7Ods5_XWR9UOoxM4VKkI8oaFxwrV7xe06Uz-eSJMtdtP-jct3eVbZNcGmjmMy-v5l_ZHLyvL_WYM0UZtETXcL1sNM7O2kTX7huy7vxfLgjR5bodt8kvesaGgXCyWg-R74pMkmF5ExJ6n4r6W0ZvuC-E06bs3nf41d_fepMOFJOCHtrB6jZQSueur4TJgBJYijFqGhfKA2yO3tU2Wa5-JIahkdoUcsRi-gcpZ6ODJG4SKgOsuLfXcD3yxpx0zDvLGaz4wQSwZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=bFKZgnGUbP5gMgUE0gDfcJtKuQ2aNITFsbCcqBOXaxrD0TXhjCiLt4v_1aIv-oZn7Q3MdL7EPjDXVwoyolTJC8gvWBA4jruGB49bCCh6nl_cyw0ILLm3lipm_r91PC1H8_ii1fxIlgeOFFfcGT_zHY00iJZQr-NNM2Non_yjY-iH4G9UfmAQWiouYfXFAjftsBEqm8iEXS3QDiSXgKtWzQ2jHT9jF6G2mqKA0t1N56sNPNU6vk5djj1fsIICmUZqXubCB02Ja1yuj3P7Vr10IDz4FnJATCBdgnS20DkBsEgpo8-546HIwXL61PeeCs0LXZQAVrYceGwr7UY-NM50xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=bFKZgnGUbP5gMgUE0gDfcJtKuQ2aNITFsbCcqBOXaxrD0TXhjCiLt4v_1aIv-oZn7Q3MdL7EPjDXVwoyolTJC8gvWBA4jruGB49bCCh6nl_cyw0ILLm3lipm_r91PC1H8_ii1fxIlgeOFFfcGT_zHY00iJZQr-NNM2Non_yjY-iH4G9UfmAQWiouYfXFAjftsBEqm8iEXS3QDiSXgKtWzQ2jHT9jF6G2mqKA0t1N56sNPNU6vk5djj1fsIICmUZqXubCB02Ja1yuj3P7Vr10IDz4FnJATCBdgnS20DkBsEgpo8-546HIwXL61PeeCs0LXZQAVrYceGwr7UY-NM50xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=QHPwKIOewtAHHUM6hAQ3uTe0ict5fTBvQdntCq5mGtG4xCLoQWn-BYN6-lh5i3Ytslzp3HlOU2rYkhRQsRo93T3_HuzOMrErGwSBaOGo2wCu0i5352trmUp72Hi5VKvNZsEsLEraE52sG5Vd_pC51YnG8NEgakuqRLKKRY37N7XTNoENBwQHZjuc4-UO6MoRl5lGGvMclWBz63OY5nrCCGEk3A87kL_svWvTQ8_nIy8gevqSjIyo3vkw0sot6hJ1F-5J-D_MhXKrW720kfVzpNrYeoShVB3O9c_kYjQI6r6hpXeIX4e_1jilYBmAnlLZkVzwAoZCHpU5Sv_byI-jiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=QHPwKIOewtAHHUM6hAQ3uTe0ict5fTBvQdntCq5mGtG4xCLoQWn-BYN6-lh5i3Ytslzp3HlOU2rYkhRQsRo93T3_HuzOMrErGwSBaOGo2wCu0i5352trmUp72Hi5VKvNZsEsLEraE52sG5Vd_pC51YnG8NEgakuqRLKKRY37N7XTNoENBwQHZjuc4-UO6MoRl5lGGvMclWBz63OY5nrCCGEk3A87kL_svWvTQ8_nIy8gevqSjIyo3vkw0sot6hJ1F-5J-D_MhXKrW720kfVzpNrYeoShVB3O9c_kYjQI6r6hpXeIX4e_1jilYBmAnlLZkVzwAoZCHpU5Sv_byI-jiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-lVMAf4fOTvPmK-tnxYG8l0Z7io2LkXXk4soTK_JWVSIz6NFPT6BWPsBS5tKD_KKsxzXSeuQvnrdiDQM_BH_5X7h_oEjN5KPCYHMoTlDiRICHHFO5gM_5CptBBtfV2LRb7-jxFO4vfFMYMgN2nP11fKQGZPvyrcTADaIPzUO4yTWh612rJ-nQfSuznpjQQtOmimep-c7FD4ldDSQc9wq8S8p13n1i1zpNR2RWilDnuvNgwUCk5K1TFjBibJvVwRNwxLI6FVK9qCqNcFUJA4k8lG9wCOibN1hPGlXCL69WaPqHzPZQVA8FwsW8jUiP2blovuEnW6ghi5_cHJno5STw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=DX6-HnxzQ1SHFFFxwbksQxOygtfGM6LokBelxO_stGd2yPzsovLF8HjCkzmvVpEFLNLI_RGfSFwQT-z_8gOuCUE-DF-qgAttC3Fj3vy0ZCKTTOGV9zv2rvpiXpqoDpfKoxn1HtTdu6QaYD6fSpFZzFHYPVLnbqW2y9jzy5eNtFVCKOOWWACZsB-xMcauwicjPiSxksReUUUFw0pHspIScmGNCtmgqOd_kzu5d3GEXvVJhz_Dzyfv0wQXc1W5DsQVvKtdF_bO9-aQukHbS5PU_3Z80ok-1_CK1hYC0fq1RTqDfg7f2H4Ofab_caSogEx8RWKUmn8R9vGxpfzmI3S4eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=DX6-HnxzQ1SHFFFxwbksQxOygtfGM6LokBelxO_stGd2yPzsovLF8HjCkzmvVpEFLNLI_RGfSFwQT-z_8gOuCUE-DF-qgAttC3Fj3vy0ZCKTTOGV9zv2rvpiXpqoDpfKoxn1HtTdu6QaYD6fSpFZzFHYPVLnbqW2y9jzy5eNtFVCKOOWWACZsB-xMcauwicjPiSxksReUUUFw0pHspIScmGNCtmgqOd_kzu5d3GEXvVJhz_Dzyfv0wQXc1W5DsQVvKtdF_bO9-aQukHbS5PU_3Z80ok-1_CK1hYC0fq1RTqDfg7f2H4Ofab_caSogEx8RWKUmn8R9vGxpfzmI3S4eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=GMahP9jlR_0eer8hNCddukxWUx8YRq8aFY1VtQ_zJnaGIhx-ppIdEIH9VriztyB4EFE5yZZ-XhgrJl1RvcDDuFatZjR4NkJGTldHWA7wF7WNZiT0HAuAHQ_v7JSep9ArFyCDRmEMLf9WjrtBH2CvH-nXjEc27sKWZY1g1CLFNys7IcMN-1KTycD4ffBuaDm0IjGbcbEpFmKYvMH8MBahRZ-nFnp65d41MBLCKEUxPHrfLjnExXnRdzBZP4NZb84zApMlNJo53qAQQVfUF20nYJrC9SjVOUMSGXVpRfK9QGaG8s1rWyoVKBvMLalnm-eVtZwoFoQVdu9tyzqOLqz1ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=GMahP9jlR_0eer8hNCddukxWUx8YRq8aFY1VtQ_zJnaGIhx-ppIdEIH9VriztyB4EFE5yZZ-XhgrJl1RvcDDuFatZjR4NkJGTldHWA7wF7WNZiT0HAuAHQ_v7JSep9ArFyCDRmEMLf9WjrtBH2CvH-nXjEc27sKWZY1g1CLFNys7IcMN-1KTycD4ffBuaDm0IjGbcbEpFmKYvMH8MBahRZ-nFnp65d41MBLCKEUxPHrfLjnExXnRdzBZP4NZb84zApMlNJo53qAQQVfUF20nYJrC9SjVOUMSGXVpRfK9QGaG8s1rWyoVKBvMLalnm-eVtZwoFoQVdu9tyzqOLqz1ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=kXKPN4Gntw3htb_jMEzO_GB2jt2_Dj_JGSOd7i7OlJmaYeGkxrVrdedvVt9G8BliZn9sidegVYbeCZs1Dpr1RMH0SSkIBKD5_Bp_Q8-bzH1uwO4IB8POiYNIpEFzmqQMnZDwAj2A3jW7BVSpdeg168jtYHK7clJECW70w92Hc3yA3SacEhJtRGvG9IFGr2DnpyMWGsGty09sx22QG3YJ7a4U3jkR4E8BILGYo7ntHTGfuJg8DXgKZEYNSJcy01mD1sguMVqxPEE1YHDY84pkj38gCkFg2yYr0hEN11QnLwst2WDlC1sj2EHHZP8S8B53lv6SjwN74TpbL-VROr2-VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=kXKPN4Gntw3htb_jMEzO_GB2jt2_Dj_JGSOd7i7OlJmaYeGkxrVrdedvVt9G8BliZn9sidegVYbeCZs1Dpr1RMH0SSkIBKD5_Bp_Q8-bzH1uwO4IB8POiYNIpEFzmqQMnZDwAj2A3jW7BVSpdeg168jtYHK7clJECW70w92Hc3yA3SacEhJtRGvG9IFGr2DnpyMWGsGty09sx22QG3YJ7a4U3jkR4E8BILGYo7ntHTGfuJg8DXgKZEYNSJcy01mD1sguMVqxPEE1YHDY84pkj38gCkFg2yYr0hEN11QnLwst2WDlC1sj2EHHZP8S8B53lv6SjwN74TpbL-VROr2-VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=C1o5KT3acocphxKHu1sr7GdcFFKwMPX-QFrN5IPOro-6kdrlkkzkn7SHp1YmfjLUvDx2ZLxeWBHb8yQFGEUhTDsX0HI1C6efzfu0uKHJNw22y8jipUJsfmgbP4MHPjiJmmXM9cp7TojrnI3Dh_vf0ihVzSpDBxEH9AXOKv4cvmlJlLgzQallnzHjUuL-vCzHFyhxjar1ePrnjTHBoWG-lWu0SDYGzlSK9JqadInq_KcehRiwr8-5JEpdrX6FglX5KaOVcpHi1RUkH2fPuRDi8Wx9QZXpjExp5SYP2dPx1JySYrf5giaZBsuUN78AAT7uun4khSENLzZjoOnJdyo6nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=C1o5KT3acocphxKHu1sr7GdcFFKwMPX-QFrN5IPOro-6kdrlkkzkn7SHp1YmfjLUvDx2ZLxeWBHb8yQFGEUhTDsX0HI1C6efzfu0uKHJNw22y8jipUJsfmgbP4MHPjiJmmXM9cp7TojrnI3Dh_vf0ihVzSpDBxEH9AXOKv4cvmlJlLgzQallnzHjUuL-vCzHFyhxjar1ePrnjTHBoWG-lWu0SDYGzlSK9JqadInq_KcehRiwr8-5JEpdrX6FglX5KaOVcpHi1RUkH2fPuRDi8Wx9QZXpjExp5SYP2dPx1JySYrf5giaZBsuUN78AAT7uun4khSENLzZjoOnJdyo6nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3G2al_i_1rwQwbg6kfWI3LgxGXMriwklhhjrGxos98Rg1l_4rfolkmCJ2E46pDxg8e6vOvNvVL4SQh2JDxsTxarUWx8U6scJwzRvvOVk07jXruHyAcDzTMF1MnNmz7bgGdmL_9CZnGkicWnLdGdbUsUM_wwp4nj0V-WKIro-ms17hLDrnJYMYNs4GcqfVHXxC-hdC3tt326nT1_j3qeHsU_3EaVg97ZTKtSzYTvrywUD4AK1AE9lYglARo_xiDYVvrcgg0rEU4z0c4PC8C35ZqiM7CPyjUzN7CinllXh6JP78ns_PmzOtktpgLRjFCKLzJusBAomPz9NwQiK9s_pg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=HIBh93x0nqljn02fENwq8ciEnnhoJwHQq8S9Jgu77N9GCWcO7FusLY79lSx_NHccprTcRNfTA71WBnNHmkA9PCK8b-lHOg3HKVfn0WQPtMnB5s5ygpZWJmDmgPMU1mQaSvnLtdWGZExKv9LRNcyCTRqAXYTJeA9GzLYAeDonXZKERbCDM6zrs38MMkbTVvEm8rD9B4URu8Pawlly-3jaAc8Wn0P85IMFHMDAGsuWn4YSc0yXWbERIQvRamxlolBj2zMaEuTLh84jSPRt7X2pVWCB1_HaTd8vZ7dxDpbh-MgXbaqg5FYiynQS99SzncT1XPWzzJGeV5SKDxJs3J3zwDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=HIBh93x0nqljn02fENwq8ciEnnhoJwHQq8S9Jgu77N9GCWcO7FusLY79lSx_NHccprTcRNfTA71WBnNHmkA9PCK8b-lHOg3HKVfn0WQPtMnB5s5ygpZWJmDmgPMU1mQaSvnLtdWGZExKv9LRNcyCTRqAXYTJeA9GzLYAeDonXZKERbCDM6zrs38MMkbTVvEm8rD9B4URu8Pawlly-3jaAc8Wn0P85IMFHMDAGsuWn4YSc0yXWbERIQvRamxlolBj2zMaEuTLh84jSPRt7X2pVWCB1_HaTd8vZ7dxDpbh-MgXbaqg5FYiynQS99SzncT1XPWzzJGeV5SKDxJs3J3zwDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=ZRb9msLD4rvCO7mwnd3DEKx0anX0pnXpbwlC5V4SsX40jPmcyZo-Wzb8UWfBM-Ba9VLbTWLJ66KzR2bOB4E3OINc88kplzWSg7P-mGS8n_oOssGQDYLsahwnQ14Nr760gDgsKLTe9vnlqS5iFci1-56Eu_YrSLG2_wHItpe030jAN74N51xgNMImhVdI_5WDQOBcLtiOZ1pcdaFUC-Dv1aryOdvbw_mVlX13h9OR9Eurks-opUbNGfAQupDGprvTDptGxiLs2pbzJfoHGvYRsxjpYJVKYP-M01Z8wqE6cJVEOp4D2hoxij3MTTk9Io3PuruGjfczfGqjWM5yXOOZ-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=ZRb9msLD4rvCO7mwnd3DEKx0anX0pnXpbwlC5V4SsX40jPmcyZo-Wzb8UWfBM-Ba9VLbTWLJ66KzR2bOB4E3OINc88kplzWSg7P-mGS8n_oOssGQDYLsahwnQ14Nr760gDgsKLTe9vnlqS5iFci1-56Eu_YrSLG2_wHItpe030jAN74N51xgNMImhVdI_5WDQOBcLtiOZ1pcdaFUC-Dv1aryOdvbw_mVlX13h9OR9Eurks-opUbNGfAQupDGprvTDptGxiLs2pbzJfoHGvYRsxjpYJVKYP-M01Z8wqE6cJVEOp4D2hoxij3MTTk9Io3PuruGjfczfGqjWM5yXOOZ-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C8o2wM6rjiRwY0aDHswV5q3BnIXJxEw0Uk4fewZ6sl-7kyA7fqm9Qni2ZaQ_wZKgAYgDa0mzXGtsmEWqKiXix2cCVTH5JFGoAdjHvxF1NMZ0lGwUeF6iYqb6W7sisY1ZN19U2OAlQz1bkZJyY-wUCjTqfG3iKXF5UqCzmQqd-CCaWLMHsOvjJw00DGrvLMfMUoGY5nQHPVaoulszGzw5lBIUXWKAH1r4AwCQq16DEihjfg16LIG1sjEE-Tz5GPLp6J9B8soDr7hrleQ-iY-BVtJReDYtaN4ipymrWWQ66B2FPcMQUtpOu-BZRfa-k5PmMAGFpwnq1mck9YtlDLXPhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C7vFJtgEvoHMdkyRSAtj1y8FOg-TIckg5lWhIs4G6SlnV7DSffWE0yKAH35WYRJvHvHnNnXJnuSEkYgSOrzRdkFISE1S4NjpnOMISExG_VyPNGMU1udf3o0J765JsEx7gun89WXb8T0ZlKKUSTL5bwrmpZEm_PQGXIjl2fpwDQ1JizEoCkXT9LWyBW3vScK_echGmO9MOoNoyUgkejjkLxp9299z4qUIPhUrGRG-CRETAMKbL3fxf-C3rPI9DfTEI3hXpYE_tgnKH80r5-IjqjLn1riqkbgdcuwVeIaCoZYNRnVyjsbZO41NJ6HmBLeaaVI2SWzQUZljJhmgXOpSbQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=t8J62fBE62_Un30hf9uUm_HjV5hiducvrBGiyhRzH2BFGNbvxg2ird1LrJWD6C-08JNzbPB6tHsW4qJ1eAW2KKI_0s-a65D5gGzdMZQwepi4A2pqkFyDDb4lmyRBhNxhA633xZJuBMPKEB9og6z5hdDoZ6ZmCLAfAUjY8m11JYZCfBAfJfSiUzjyNG1oXdYzvHU26sfZtngfHXz-zm6QV8FBzMupjD3J6uNV0sgcM_AXwrDY7dAP1SEEzkFjFrf5yyGOvoBXXQbInhVBwxb530S_0amOeRaKJkV-YNtLFXYEPuliMf3Uh7_DtWbHKSnJL6ixgVF8LRpwSLBlZOvq2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=t8J62fBE62_Un30hf9uUm_HjV5hiducvrBGiyhRzH2BFGNbvxg2ird1LrJWD6C-08JNzbPB6tHsW4qJ1eAW2KKI_0s-a65D5gGzdMZQwepi4A2pqkFyDDb4lmyRBhNxhA633xZJuBMPKEB9og6z5hdDoZ6ZmCLAfAUjY8m11JYZCfBAfJfSiUzjyNG1oXdYzvHU26sfZtngfHXz-zm6QV8FBzMupjD3J6uNV0sgcM_AXwrDY7dAP1SEEzkFjFrf5yyGOvoBXXQbInhVBwxb530S_0amOeRaKJkV-YNtLFXYEPuliMf3Uh7_DtWbHKSnJL6ixgVF8LRpwSLBlZOvq2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mp9UQ2gy-wp9xJBkhQAJYl6KPpUMfLmEL9-OTqEaaytTf4Afqw0Fv3EOh9YYcomoy9wvEweHWFHZMElkYfwCKiUAJkT1NsZcDvHZfXtp6GZ0ogpY6cjn-DEz5b6YZfxSHKt7415ACwLR8DO8EgdKHasC4wzODdAejyY6aK4PDuqrT0jjthK7Roo2RMCiKkumbIkn_7wD0723AF5QvK4VhLk8_hKUOPljRq3mHFiC3UTsWIt80EniFwWJQ6hYkL2fV98XBfWQwdZdljj9gIjbTjwt5eFGqxQ8wTP4U96q1EHcJkXBD6q8BV5u_VFGfBFqF3y8h9xv2TLk80QFY1Lu1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAIqW7C5FRtmkIX-kLo21r2DbxA2RV_8UyYQQbtO3zAZy5HY9HbPVh4huWY8TRGodjYC5TDW5ajjzw90nmOJl12SJBKNSmWO8IR75MgEUXShltAxscMrLe-xGdCiUeO_ZoMOZZBAjfVoGpBnEt16ngdf5dDDw-b9ZABkifzAP5LB9gDkbz1smcdBsMMUXIxYLFjRhH_ignRsMWbjgMVE8sx7jLnylL3Us7jHYTWrOyzxPUUaWQzf0qmo5EXP3om08fLCam4KFUWwEGalMijVlqf6BCqf3vVDMm94tXm9iZGZbgnzwegF_E79R1VSBn5FOnrSTPn4VuN7b-T_2PsnxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxcmj9rwiV-dNrWXUqI8_1x3HczD1j4jEFdg9_3quC0pbujJvrz-clXhrCB-_MOy28SzSkwaPI9oGu8kubiEUcjbl8qYFIVd4ek6UAavphfCBc5xjFE7F-gZunea-iqqeJLpj3NCXZWpmgmC-vBaf0l9XPorEPIzjiuRt2f_xFHRLHMdIiyUFBVCoqZGI1tnMtvtMJ0Sbr2yFFC672C0eABDRLvideeE6nM0HylZbzfLFTmKJOtzhpqk4GwCdhwyOP3GthU5SxRa2qcGytvyLhQRYNLf2UteBXCiG9yO5WDKdGwSKsnT6p7-jd7XRRJqg8CT4aOr3ft5BxwYk2KGvg.jpg" alt="photo" loading="lazy"/></div>
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

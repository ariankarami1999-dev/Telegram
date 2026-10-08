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
<img src="https://cdn4.telesco.pe/file/ZBKwSSKyFaDo5gZTGFIejcAyq4jjwfFXZfiCoq1rsSGeBNL093Ym7vKRxV8Rwi4GzvKN0CoMI4HC1aCWV25aqfgNVuwLtGx5QVnZS7usU2sM8zbMhN3FimQN3i_9_iOUWaBpS4ORuM4WNtwJMiX19ULc2yeEZMQUZ8oJh3Lz6pb_V62paqzWni1GFMnmMwGeMBnA12-FHChP2GHaau80xMpBo4-Gqs7qdf7Gh52BEbCqZgheL5DgmlIvbpeHeDC7dAGCjmGl00qIZGoWEoPuVRiG0PWU6K2R2y2HbyJ0dP-9PMLJ3CIh9uxsR1u3qUl4EnhO2JV2Ww_ibUyUUhdabQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 05:37:29</div>
<hr>

<div class="tg-post" id="msg-6802">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbRNohQNMJwKjiqfXQ0XChBg4e6gJ0ux0aI70Ml7_gB3Rd-01f5Ldzf5jJgXyjmYQ5zAi7-qEbOew_VdPBiR3aK8X_N2jyHIf6GzP56rbp-auRJy4whOw5HY_ClzYTDXqWwBV-8-jffVvIb39mL0gWqiANvzmGpg-sjcP6JwYw2y3ofW4NmEAv5rjkOOJ-dOhAUkY7Un6dEGtpUDoc75pCnWT3f94W_PqjrF_p052rwhDy85JtpFXjQfkgXseXqRrIXqSkNaMAdgM7J5q9uDzo0ooiD5KBh7ycuteb1q_uVMhuYTjJ8ceQkLFvSHC5STkb46sEWYVbIGh7oOFgQ1GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن  که آخوندها دائم به نفع خودشون و شیعه و….. استفاده می‌کنن آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟  یعنی قرآن وسط تعریف یک داستانه، و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل  و فرعون صحبت میکنه و  اینکه خدا…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6802" target="_blank">📅 10:52 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/6801" target="_blank">📅 10:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6800">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/6800" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6799" target="_blank">📅 12:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4MI5XsLbkYJVxKdTuBVEJg7sopC0Splyx39IDxnGJQ2_o6dTlejlu-2gwFO8ms4fKpySmU3noG5Fp07k_WDH_hgaz8hcZXO-8RI0d1d4dsO_4o-rKGAta24IXx95qHFqMbOBiLSNtNFNjgDpngYRNGdfnl0mWujwGOIpZquTDLy8Pj7RRqEqi25IJtxhph8bgOEGKPsDslGUpt23C6B1iR_HzZOBDhSqZH9OF0mfQRRdY-KFww0q5fQE9O5LV-lOXqhzrOPTCGP7zGY7Iz3_V3gU-AH5dO33QBck7snARW8DqujQ1gSEzG8pgcAL0d0cXy4vmSezgBxEn1et5HkuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»  در تخریب‌های اخیر خبر میده. دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.  در حالی که اعتراضات دانش‌آموزان…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6798" target="_blank">📅 12:45 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6796" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6795" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کار به جایی رسید که جنگی بین  محمد بن‌ابی‌بکر و «عمر و عاص»  بر سر حکومت مصر شکل گرفت!  عمر و عاص، دفاع قبل توضیح داده بودم که اولین حاکم مصر بود!  و جایگاه محکمی هم در مصر داشت!  و مرور کردیم  که اوضاع مصر هم از زمان حکومت  محمد بن‌ابوبکر از لحاظ اقتصادی…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6791" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">معاویه برای محمد بن‌ابو‌بکر  نوشت که تو که هر بار توی نامه‌‌ات علیه پدر من می‌نویسی، و یادآوری میکنی پدر من فلان بود و بهمان بود، پس من حقی ندارم و خلافت حق علی است،  پس چرا پدر خود تو (ابوبکر)  همراه با عمر در سقیفه بنی‌ساعده،  حق خلافت رو از علی گرفتند ؟؟…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6790" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6789">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بعد از چندین نامه تند که معاویه نامه‌ها رو هم می‌فرستاد برای نخبگان و مردم مصر،  (البته محمد بن‌ابی‌بکر هم خوشحال میشد که نامه‌هاش خطاب به معاویه،  دوباره برمیگرده به مصر و‌ مردم مصر هم می‌بینن نامه‌ها رو!  اما قضاوت مردم به سود محمد بن‌ابی‌بکر نبود! نمی‌گفتن…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6789" target="_blank">📅 12:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">محمد بن‌ابی‌بکر نامه می‌فرستاد بدون سلام!  همون اولش به مادر معاویه فحش میداد!  (این موضوع فحش دادن کلا در بین شیعه به شدت رایجه! حتی در متن سخنرانی‌های امام حسین در کربلا!  یکبار هم مستقیما معاویه برگشت به خود امام علی گفت تو با من مشکل داری با مادر من چی…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6788" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مصر، ثروتمندترين استان حكومت اسلامى بود،به خاطر جلگه رود نيل وكشاورزى پررونق و...! به خاطر اينكه در دوره حكومت امام على ساختارهاى اقتصادى رو عوض كردن وساختار جديدشون رو هم نتونستند به درستى پياده كنند، اين مصر بسيار ثروتمند فقير شد!! يعنى اوضاع اقتصادى داغون!…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6787" target="_blank">📅 12:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">این رو هم در نظر بگیرید که امروزه به خاطر حدود ۴۰۰ سال تبلیغات یکطرفه، اکثریت مردم ایران میگن حق با علی بود و معاویه در سمت اشتباه بود!  اما در اون سال‌های اولیه اسلام،  چنین شکاف و فاصله‌‌ای هنوز وجود نداشت!  بین نخبگان بود!  برای عموم مردم، جایگاه این افراد…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/6786" target="_blank">📅 12:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6784">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">محمد بن ابوبکر  یکی از نزدیکترین چهره‌ها به امام علی بود که حاکم مصر شد!  یک جوان تندخو! از این حزب‌الهی‌های افراطی و عرزشی‌های گنده‌گو!  نه سن کافی داشت! نه تجربه داشت!  اینو امام علی گذاشت حاکم مصر!  حکومت خودش که متزلزل بود!  چون وسط آشوب کشتن خلیفه سوم…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6784" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پس تا اینجا همه می‌دونیم که  فقط شعار ندادند!!  همه ما این قوم رو می‌شناسیم و ۵۰ ساله که حیاتشون در تنش و بحرانه!  اما فرض بگیریم،  فقط شعار دادن و حرفهای تند زدن بود آیا در تاریخ داشتیم که حرفهای تند زدن باعث جنگ و ….. بشه؟   بله! و اتفاقا دو مثال روشن در…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6783" target="_blank">📅 11:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید که حامیان حکومت،  در دفاع از خودشون میگن :  بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل شعار میدیم، ولی کدوم کشور به خاطر  شعار دادن و پرچم آتش زدن و حرف،  حمله کرده به یک کشور دیگه؟   البته که همین جا هم صادق نیستند، …</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6782" target="_blank">📅 11:44 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pd2VhEJ32FqCcPXhIfwNqDdXuh9wv4rI_XMpuXNsxxUvuJFCSpKIoa29EihQErDdHZKmK_iHml7TRPiZwQyrMhWdF9nUEANqyMw1oJTigl5lLaC2r1iwg9xHSvnQhJ6nI1yNU--jro9P0IzZdQa77DFmhM-1Ie2bzwwX3FjdPn8WpOZO3LjJkqV4ZNJQRKHtjf0OTYwlwdW2_sPB4udWeHpXeepAoasOaYNsiPPTYiMRqPS_5X2-ZRNnglcfJO3ijSbjciHdrcwzWP0TTn6DMVKzCf_AJ_ILlpwOGoe64DlY1rhgJhMR9win9eziyIc7D4bnra89Y0SgquxKnbMJ5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9kormB_Qm86rIt5NXWhvBkV12xEJKqkkd07k9OkOVOgNwCQ2wzFrKIp7Dqjw6pziJExL-t4Xlq0Dex6G0xVc03XIsUVPY36Q4yrNhlDu9YUpKE3eqKfsm8nbWWB0dnVRE3PO6vojpDSmPjqvkZNjuza0wh1s9xH0fMMAG4dnBDLn_eIz7etOzxl4d6I7zGnkhQAzqyfqK17XvMuCLA-xud4lxKGy5DUP2o6M_WKxYnb1rlCE2ruBO6ZC4-3l4jOT8HL_nxnmYJvuijsUE_msI736JVliPgoLidKI8C4nl0M-9GoeZRV2VaK3eNmdG4AtNLLDFV_FmzDYYfYMoKg2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی این ۷ شرط رو داده
به آمریکا که در قبالش  ج‌ا تنگه هرمز
رو «باز کنه»! آمریکا گفته تنگه هرمز برای شما بسته است!
برای ما که بازه! نفت که داره عبور میکنه!
و اصلا درباره تنگه هرمز مذاکره نمی‌کنیم!
اینها مثلا زرنگی کرده بودن بریم تنگه رو ببندیم در آستانه انتخابات قیمت نفت بره بالا،
آمریکا بیاد گریه و التماس کنه!
برای «زمستان سخت اروپا» هم منتظر بودن روسای جمهور اروپا برن بیت رهبری گریه کنه، لکن هیچ کس بهشون محل نگذاشت و خودشون دچار مشکل کبود گاز و برق شدن!</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTfOcrKyWC5gVsTmFycVS_2eNHGJnNFM43BZBXEFXftQ3JKkkrj9hGnli1241iof0UoE6MTiNqyIBKr5CqNG54pmDZUuss432GlQEjov9Sv-CoezoDOtSCMUaVS4rcxd1BHFn3MsFplQdmQr_DkyxdCmEQ2NtMKlkeh6bM3Wq0uDrNJs_fYKUilxR1T7pMRA3_0oADuPHYZS52OSwF5mkEzyH9z8Kj6kEwovmurwWe-7KxCEOukTzZa11v4fy9-IzAiWJqWeOdrX1devKuOJPTxaBFuvX43E-xd7ypR3GsTJsI_5xsVsPuia47TdhxapDS1o9PjCc-Kozr_zhxglgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=pK5A7FXfFll9wS7JgrlyNbj3vuDaZsFZS8Qurp4NJ1mWglsRv0KXXg1tVYLu-1KQXYq7Sf_bLicIY0U9jioC14ORFCU4BgRFtQnlVfwjna_6Y1V3r9bUGzIalg8QpBCoTbRchf8lL8ifiqKTals9HKCIcr_Fvjc-GL9DKgoKs8SycysziNHHt8ezl9mMgvNcEoIvy_-u4qNcfC4RwTrdoPWKlC4WvNiFms-MANx8lxFVIDhTcuKtclW6VcqjzpoE5Y6YkARDWyQq8z4k55vpYgDzBbj0fZjCPgIBwN1X6qCSHJvhWnHSXfl67ZGeOvI-U20irZr1g3xZ-WyfDWzTSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=pK5A7FXfFll9wS7JgrlyNbj3vuDaZsFZS8Qurp4NJ1mWglsRv0KXXg1tVYLu-1KQXYq7Sf_bLicIY0U9jioC14ORFCU4BgRFtQnlVfwjna_6Y1V3r9bUGzIalg8QpBCoTbRchf8lL8ifiqKTals9HKCIcr_Fvjc-GL9DKgoKs8SycysziNHHt8ezl9mMgvNcEoIvy_-u4qNcfC4RwTrdoPWKlC4WvNiFms-MANx8lxFVIDhTcuKtclW6VcqjzpoE5Y6YkARDWyQq8z4k55vpYgDzBbj0fZjCPgIBwN1X6qCSHJvhWnHSXfl67ZGeOvI-U20irZr1g3xZ-WyfDWzTSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند سال پیش یکی از دوستان با آب و تاب تعریف می‌کرد از سیستم پیشرفته
بانکی ایران و کارت و انتقال پول با کارت و …
همون موقع بهش گفتم این گسترش سریع
فعالیت‌های دیجیتال بانکی به خاطر پنهان کردن بحران عظیمی است که اقتصاد کشور باهاش دست به گریبان شده!
وقتی پول نقد دستشون باشه خیلی بهتر متوجه میزان بحران اقتصادی کشور میشن تا با پرداخت آنلاین و کارت و…!</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=MpHyaBmIPsrBKHDmY-f4gGUOcUKnRDmkHobuMSdb6QfQAzNSfSp2FSNwOLS--Ye_AVObUDB76CCG_bxM3RwrcmRl8Ye1CWI2hDJsNnIE7Cw32yyVqyO_4kt8y8hYvLvCkxDNP4kvNaJ23riNFuGhPFO50ePa0eqBxIz1TfBaNuZW758Z2oFH4hsM8AyVSO33zTptL7_KNQapleZPMmL7p72mwiA8KU0kMJt0Mn-ue64PHTk0PM0P5rrHsiSNhDCXvgNKGjo0ljeVv-ZoAYILmaIekVyD2ecdIVEYAmSpWZA162aiU3_mxb2YipfTHMFcjy-UBrm_MOPRpFjdhkiGGngEPqLq0JNpGG1VkijjQhwso3FLnImJ-iBWMB3LcbvQIcIAcAAqfIkwTHpntcVIUZLYj2AUySSXX5Iti8gbtU_PmtDxaBNWIbzJRFmRDmfqwDjJn93FMM3zj5QncVUj6EjnvDVdecf6FsRecFC-BXaq7po4e8LlaaDCtaUnMNemQzS-CbI7eWKjwdtHmr0XQH6UHy9jYcPm18HyHzeiHPVww1oTm75_WNa1G9lVzsMo4DfibisWE4sYGF364KJF6OHsgIqcVUybYig41wAwN7-ik3RiegoKS2pJ8q6tpYq_FFve8Zn9SC38Ue7QTl6fNXDJD0lmC5oe6fq0q0gZ6ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=MpHyaBmIPsrBKHDmY-f4gGUOcUKnRDmkHobuMSdb6QfQAzNSfSp2FSNwOLS--Ye_AVObUDB76CCG_bxM3RwrcmRl8Ye1CWI2hDJsNnIE7Cw32yyVqyO_4kt8y8hYvLvCkxDNP4kvNaJ23riNFuGhPFO50ePa0eqBxIz1TfBaNuZW758Z2oFH4hsM8AyVSO33zTptL7_KNQapleZPMmL7p72mwiA8KU0kMJt0Mn-ue64PHTk0PM0P5rrHsiSNhDCXvgNKGjo0ljeVv-ZoAYILmaIekVyD2ecdIVEYAmSpWZA162aiU3_mxb2YipfTHMFcjy-UBrm_MOPRpFjdhkiGGngEPqLq0JNpGG1VkijjQhwso3FLnImJ-iBWMB3LcbvQIcIAcAAqfIkwTHpntcVIUZLYj2AUySSXX5Iti8gbtU_PmtDxaBNWIbzJRFmRDmfqwDjJn93FMM3zj5QncVUj6EjnvDVdecf6FsRecFC-BXaq7po4e8LlaaDCtaUnMNemQzS-CbI7eWKjwdtHmr0XQH6UHy9jYcPm18HyHzeiHPVww1oTm75_WNa1G9lVzsMo4DfibisWE4sYGF364KJF6OHsgIqcVUybYig41wAwN7-ik3RiegoKS2pJ8q6tpYq_FFve8Zn9SC38Ue7QTl6fNXDJD0lmC5oe6fq0q0gZ6ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1Gv7U8iVC0aMakx-ULC9dLJvW7oC6B0qj8BYQ4YPGq9oYKavb-Sbs-Bfgi50CS7Eaw5kOwHtXDSM77E9IBRujQs__pQyE7017ByLEeuFQZRtkpSwXiBZKzawc5BkSkW2WJqFaJToQflgDhVgwhXyZDU1poyud2w4W063rAgJB2_EJ-1HJvtKpZi1IMBnIOtNtGcAKW9zE6a-oqKZkwPtL9Dbgcs7qEG_cyKEQkueV3ROvjwFqDfMH1X8HlkVY8DAqz5MihYKwltdEdLkU2lOaaBEir06XsE52G0i-IwOZRzZfTsED0oC27ZMuA9dW_aY7dO5r2fLPcfQccBfmCiug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rep8jBe7SVIM0L2QbLUL_XkpjH5sgSTtM8LzSW-Gs38JiWSaBxjfxWXg9KZgl3KA0cxpsKx-FBYoXced8n9BE5yefo31owvLKpY9y1YLD3GYMpy9sdx_GQ5gJj37bS8X3FD3JvMNxfRYjHub_Ja8QzKHVlOvvQRnTPNKZa-rCqvx54FkjGPkQ_oxdjTu3M9nIOTKEyvH_-x862Ea2QkTv3H4s_GYGCzs4GNyE2UP_KZgYBVoEZSL04LjsNpuql89u5eaBgOJCLsVXnACpWTk-6f2_12Vm0CRCT_40HLbefXwppbm-ERZ9pZtmqbFHM3vB5D47QZIFzSRGdGBR4b3DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GgIx24GQVFvFlnd46hv-qw-8QczaltXZS5xU-_YS8X1U1nGZeboruBYYIUed7evpI1SSM44uUJ-cjgPuX1XpwEnf7W5mPL2cS-oTldwyCcTtWlddMJ5xiourBrSOntMOVC_xmNmEuQL9tQHfhp-XbFoDfMh124gQJxc_z6xG37ZrqyfrpmMNOnKpDNWDUpQk92cLE9zG0mS2a8skOHnHTXadCRlDAz2DsEjdONUR0lmOD8xEM8Jn2hmqp_2jnVj91EzmOSHhgkwhO3sZnquqP8OsvtOeVGucXZruNaQIMbxSZvJSQfFMELFOxZaBzs8g9eOiVhVTqt1nC2co_iyxfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=ELDnS6P9wDEntzhRhSE9f6CxQgVHKUR8dvDKTN8_0W4A_MBytN-3XXb1uSxSMvYf_x-zzyK0q2J_YP6JJVeK65FMsxfeTpoeJAVDRxNAo4fiKvKXhGeZA0raJHoWIo1gSq-0Ww-lWHDdPl2LsWLo0Ppbz73lcouWimnSRZRWcqsKaQSvMCRdGqoJU-kYgoNx7EDszFMyhDidzluHG1hv_Nl4E_-ygmbTCR-zKiD7ZjV-RUCGP-xb3nYevz3NchaWKSi-Ujk1TgBnNLsp3mPPhNqw_N-GXEalG428_mDCP3SeTQcOYnCrjNsf5n1uyX2MNVQ5X8BwRlLQNLwJcBy3Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=ELDnS6P9wDEntzhRhSE9f6CxQgVHKUR8dvDKTN8_0W4A_MBytN-3XXb1uSxSMvYf_x-zzyK0q2J_YP6JJVeK65FMsxfeTpoeJAVDRxNAo4fiKvKXhGeZA0raJHoWIo1gSq-0Ww-lWHDdPl2LsWLo0Ppbz73lcouWimnSRZRWcqsKaQSvMCRdGqoJU-kYgoNx7EDszFMyhDidzluHG1hv_Nl4E_-ygmbTCR-zKiD7ZjV-RUCGP-xb3nYevz3NchaWKSi-Ujk1TgBnNLsp3mPPhNqw_N-GXEalG428_mDCP3SeTQcOYnCrjNsf5n1uyX2MNVQ5X8BwRlLQNLwJcBy3Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=B_J845Ii-PAwyGLW8iExeZiCwnSTKyXPCo5Ur5JWKnoE55vdXzTKPQ8BYatCwPUaZmSMvBFLAGnSSjbAj4obgkl1pZI9eTx2a0nS9-OX88dtcaFRLr3QHhH_7Z0z_QkIE6YJ4-nMhJKn3YLHO9rAzumeh0fTwrxX8h2P-tHzDspeTRIIrGlTDOJMugnoQ5LNj_b2tUoPKjXP_XF84C7Ez-ZXdNmpfzSz6xun1OKTbTUfBV55N5Y8TrkDv8sSNndpMMoBMyI1CzA7owS5IUYnJOrp8MSVcFGZHRxVz9aBdzkdP1xfZiPsjr1vNNaVgXgIOyW8efwY3sChMRwSemNzYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=B_J845Ii-PAwyGLW8iExeZiCwnSTKyXPCo5Ur5JWKnoE55vdXzTKPQ8BYatCwPUaZmSMvBFLAGnSSjbAj4obgkl1pZI9eTx2a0nS9-OX88dtcaFRLr3QHhH_7Z0z_QkIE6YJ4-nMhJKn3YLHO9rAzumeh0fTwrxX8h2P-tHzDspeTRIIrGlTDOJMugnoQ5LNj_b2tUoPKjXP_XF84C7Ez-ZXdNmpfzSz6xun1OKTbTUfBV55N5Y8TrkDv8sSNndpMMoBMyI1CzA7owS5IUYnJOrp8MSVcFGZHRxVz9aBdzkdP1xfZiPsjr1vNNaVgXgIOyW8efwY3sChMRwSemNzYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4GVUTkG2J2tTOj1hY7ZbCDv006nUes3IewM9Q-L1_H5MMj23cr5PvAwxdORt2GHMaLDe8Un1Nmo534gDP1DsokbAty8tg7A63u50G-UEfiI_pmEHVtF0D6GH8cHXD6u15jqGYI66GcrNmwzI77eR535swh6ZwUx-dVfyeWIKvyH-D09qIArbObLSDMrlviRo9_ypm1TefZl-zFSD80l_r81qh5my_nOx2js-KLUlWGq6_qyHZnxPgheSh_7c17pDKUPflsOU9s2FrFBygaNZLgYjbm6qmbsxgsdxhEct0Ovec3chPyHbGpUfaC1uxnvpmDenxVPwO90bTcMUK7-Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=Qad6g1X5FgthOu4l_oUwIUlOfgHjafIy_X7JPYUd4h51jOH4nLzdUqCxNdsLhNJc8FxeSexNLf_ZxXOjWa-iP5kcnYSlRVsUwzwfCesnuHwu6FoavBRulWomxOq9rdRzZkNy6SRwJ7GXNygu_5ZUyXavcQHi_ieTSp2kIts3Kkj41UuOCoxlO_JLu0EmPWnJF5BLeeY0oSDT60dq7yf8xjztBN5wx0u0VTDu1C78EZHRLhGpuHEI211Bv5l076ZgdsbFzlNlCVXN5cclZIBuSOkIHwOAPD_ocM5oCKBvwDd44WOBBttSmdAZv0DhPa2C3ExHfx4QPolAIuVYCJT-2lCkpMYOrbBu04nu_gfaDU3QWTOAsf0cuGb_q0RP9Ula1jmN4nZtXtU1Wk1gGXdcvhKel7AqJHgKV6_Ym8CUdKIovMALGBttfp9jlRU-0A6UpalCOYJrJhrc0Pc0ziqcACnMoeOvjYU6YsmJ5wASyB8lFRYw_QJLVUUX_7ivrqNdBYIpP5e8sPX_V93GD93EJNZGLecawf-Skxu_ApwK5g7yqqeFQ3TiPJSWcTHZEh8rinvLKbogTCaPp50EhNcnxwm0JY3Pf_5AM-OSvJT2Oi28ShfSX3_MwW14K40njmNksTnaie44SqtfpItf1T4RnhP-no8UXTV_sJnIANDoVYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=Qad6g1X5FgthOu4l_oUwIUlOfgHjafIy_X7JPYUd4h51jOH4nLzdUqCxNdsLhNJc8FxeSexNLf_ZxXOjWa-iP5kcnYSlRVsUwzwfCesnuHwu6FoavBRulWomxOq9rdRzZkNy6SRwJ7GXNygu_5ZUyXavcQHi_ieTSp2kIts3Kkj41UuOCoxlO_JLu0EmPWnJF5BLeeY0oSDT60dq7yf8xjztBN5wx0u0VTDu1C78EZHRLhGpuHEI211Bv5l076ZgdsbFzlNlCVXN5cclZIBuSOkIHwOAPD_ocM5oCKBvwDd44WOBBttSmdAZv0DhPa2C3ExHfx4QPolAIuVYCJT-2lCkpMYOrbBu04nu_gfaDU3QWTOAsf0cuGb_q0RP9Ula1jmN4nZtXtU1Wk1gGXdcvhKel7AqJHgKV6_Ym8CUdKIovMALGBttfp9jlRU-0A6UpalCOYJrJhrc0Pc0ziqcACnMoeOvjYU6YsmJ5wASyB8lFRYw_QJLVUUX_7ivrqNdBYIpP5e8sPX_V93GD93EJNZGLecawf-Skxu_ApwK5g7yqqeFQ3TiPJSWcTHZEh8rinvLKbogTCaPp50EhNcnxwm0JY3Pf_5AM-OSvJT2Oi28ShfSX3_MwW14K40njmNksTnaie44SqtfpItf1T4RnhP-no8UXTV_sJnIANDoVYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=IqmXZIGw0CPJIkCbIdAur-VqsFk95Wosy1wWDnmP1lqd_Z1uQ7Aa5MZErAooJlHJLrkGdQZrv4wMe5SdbSo2XVZfgH0xl5oICTs0SpQOTqlm4FuBXMES4j6wA9LEOqVZ1TMJIzuxM70vryx1zk4hDkYKa7EcnNynRFVZ3OUp0EYX9h4mQmyKXUcYm7v_zFa-vZHoWpDIWA305PDZqqwE0Xm-YDGAHLQHnB8JEoM64HZieG-0PALw332HBZ5OOQrHodUnEN38feBOozu6YP3WC8cmdLZxA1Dum1b7QVzAhdxaz8HqHZQdypqUrDv09cLxNf0y4c5SSR1oRXxIUrI5Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=IqmXZIGw0CPJIkCbIdAur-VqsFk95Wosy1wWDnmP1lqd_Z1uQ7Aa5MZErAooJlHJLrkGdQZrv4wMe5SdbSo2XVZfgH0xl5oICTs0SpQOTqlm4FuBXMES4j6wA9LEOqVZ1TMJIzuxM70vryx1zk4hDkYKa7EcnNynRFVZ3OUp0EYX9h4mQmyKXUcYm7v_zFa-vZHoWpDIWA305PDZqqwE0Xm-YDGAHLQHnB8JEoM64HZieG-0PALw332HBZ5OOQrHodUnEN38feBOozu6YP3WC8cmdLZxA1Dum1b7QVzAhdxaz8HqHZQdypqUrDv09cLxNf0y4c5SSR1oRXxIUrI5Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaMzSSqTvfOJiMHYArZv8_P15MoUeIU4Kr5721VCY08nEmT6XXVGfKAiBjeGXy9Kc1pSfeQ88JQdj-peSbO432zMZ7fyiDpLFoy8KKW8DoAGk7ZPakMfdK8JOpwE6XorgX6cN8PbfnqybTHpWPvlNXX4UCZxBZ6i1Szz8wbSUBJYlYOzx-iLCHjdhqMM4r1vxvHaxtASCykBZHkEB7DZpwCcFqsY4CypDowVZGvF7UMGZDoWdcgicpGKF3DWux-qJMjyR0sqs8HPz9k4t0uG9g0MyaYRMTOJgKmXbcA7w_xmLJcunN6pvzWNN_PmOShMFgueQW-2zD4hDAGVforiAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=As3nvbDcDt4HRh3hL6ezQ3n3OzU0YK9SO3ABG4wdcD4QNgh2kLy75u_nIVJL3HNu1YZqt7TNmdMbelMMxY03ureopAD4ujuy42QNTvYAp9yg5f5iAx3I7ncl9mS550FVqoC7px-25uHFLMzcgcjGyWJKltnLxorANHXN_34L_2zYq9B9cQ5o7xPeUvPxOUaGpss9Jh926rrl-zqfPrr_j_86NRKJk-n-PK_yBKICU4pVuh3l4MnS_slLFnxE9wQriV7OU4zb9GlULOAI5cPSEfxguQX6zGZN1PUlv3ZUBrBv_cNiLdJWowRhERjavXCq6oDYQubuiB6ne8L0lGNwpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=As3nvbDcDt4HRh3hL6ezQ3n3OzU0YK9SO3ABG4wdcD4QNgh2kLy75u_nIVJL3HNu1YZqt7TNmdMbelMMxY03ureopAD4ujuy42QNTvYAp9yg5f5iAx3I7ncl9mS550FVqoC7px-25uHFLMzcgcjGyWJKltnLxorANHXN_34L_2zYq9B9cQ5o7xPeUvPxOUaGpss9Jh926rrl-zqfPrr_j_86NRKJk-n-PK_yBKICU4pVuh3l4MnS_slLFnxE9wQriV7OU4zb9GlULOAI5cPSEfxguQX6zGZN1PUlv3ZUBrBv_cNiLdJWowRhERjavXCq6oDYQubuiB6ne8L0lGNwpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDqbuJ3iSPE17Vr3-SKGrxfGbbI-4xpMOBGezCjzElLANK7jFauJ3F7JbLAUDApgMrRORDMjFOuGv0aNLyXwmQvfXUZBBRUiaGSOGdimVn4EUQteae0rEyqHYvCWjkG7BbqEz5QHbm8NovxRDMf3R1BGNyCLBRFEXsin0mdZOKkkh3XvTzg90OpdR9ZPcMlAAiOqWD5LvuBRERYg6lXvk99N4LjpgCPRFpq1tGCR_yNgsvi0TPXvcAZC0I77aHOjbYSMdIMvZZy3X77j4oahKvSQuDEQnnqaaJBsTZrZANnksvIqvfddry_5bwmUaK7JmXpR1NIUC8Ky-y_0TJNr_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6YAE_-RT0fbVO5vg0vAR0lc_NzbBvU1X-nfkJqakntAHBmats4yOk1EIsXO1mltOcE_VooVBG3JFt5dSSao6dadlOHgjXkosBwXldvK9-NiSXbIBGwNhc-R7iy3v_0rJeLPnhYBy_odFlBd9Zj8GB-04rNtIlvsOdpR5YvqcuLhjwf-0U9GaGPTRZkixTNVmpyErQwO6bLUEaLu3ikPuxLyl0Pgf_LpwOWFXgLCUrDUpX7ntH1FdqtP75vjT6aA4QSve6Min1BZa4jBeb2dDjp7z0SY57MBqsmhwUaSzqW2RYkJ2a1GcjdcGHoVjcZ3tBF9cGCRR5yxHfsuOPV0Sg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=XKi0YMtigpqxgiy0hnP_3bSbGckdW7mXoTAkZmu3vRctiKDgsxHfcsUg6ply1NJF2I688QMgFZZrpS7PxMsCw1rAjsEei3hvp-Q9LdQNc4JjDHuqMN6Ea7G-pTyPnRgyA-rKczOz8fk_mtZwaCS0m2prdXYV8Z39K17YpUlu3v1RA71-zap2AhXtOXrCArcKPdKiQ6iek6Wfgd49XQTsanaYit8_rKk_rZx-qRCLC63ptWi0oTtH7nCoX-ktyptBQd-H3U3tNiJMnlTsjodTNqVLNHOevQtwSitThIxUTb9uLSu05EdTWSzxNv8raw6hojKyaNlRcw_WQx896n13pk3Fx8Gb8UA8u1b27FS0suIWipHjjjZ5rBz4FOtOaLenLncaglSpS8JWN3ZlVVCX8jmpPbLqkuYDROXJLGE4l6XSCuU5RfIoozz3YSNRH8flR0ZSampiWOzalDmITxWQ2RtYSt-hKy1opbxx0iAtmkSHbxSyuKBhjbXqowqH0rTuqyAZ8RFocq8DLVSPTQP_G0EztEol_1owOJdybtKRMyokySfHw7EutDbajMoQ0QIbj6pMijLX4QX3Gpi6XcYCpXKIyYZEFkjOKFHZz50Ileq8Bg9CVQfl_luqv1CugaLwZtBXLC-caVBSwFqRAjHpGTSQHbPHL_Zfi6a4AqIIODs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=XKi0YMtigpqxgiy0hnP_3bSbGckdW7mXoTAkZmu3vRctiKDgsxHfcsUg6ply1NJF2I688QMgFZZrpS7PxMsCw1rAjsEei3hvp-Q9LdQNc4JjDHuqMN6Ea7G-pTyPnRgyA-rKczOz8fk_mtZwaCS0m2prdXYV8Z39K17YpUlu3v1RA71-zap2AhXtOXrCArcKPdKiQ6iek6Wfgd49XQTsanaYit8_rKk_rZx-qRCLC63ptWi0oTtH7nCoX-ktyptBQd-H3U3tNiJMnlTsjodTNqVLNHOevQtwSitThIxUTb9uLSu05EdTWSzxNv8raw6hojKyaNlRcw_WQx896n13pk3Fx8Gb8UA8u1b27FS0suIWipHjjjZ5rBz4FOtOaLenLncaglSpS8JWN3ZlVVCX8jmpPbLqkuYDROXJLGE4l6XSCuU5RfIoozz3YSNRH8flR0ZSampiWOzalDmITxWQ2RtYSt-hKy1opbxx0iAtmkSHbxSyuKBhjbXqowqH0rTuqyAZ8RFocq8DLVSPTQP_G0EztEol_1owOJdybtKRMyokySfHw7EutDbajMoQ0QIbj6pMijLX4QX3Gpi6XcYCpXKIyYZEFkjOKFHZz50Ileq8Bg9CVQfl_luqv1CugaLwZtBXLC-caVBSwFqRAjHpGTSQHbPHL_Zfi6a4AqIIODs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qaSQ1CGWP07j9HCARI_FZsG1GOSOpzY3sARW83onq1LrfeGn8IMRar_a03tjOqetEunPxdWK6LFxzGiB7tJIsbY9_UdrcVZhlomSuCgmaMMQR74fSIzwFebJVr3NQ_NWZB4r8LFWw5lYPw_yqtecTbqdxbIXK7WrZUTjWXOpK-yRnTF-crWv1b1GKBOLJOwMr5bhyUszrSD5Hkj2v_26dWqh5yW0CltWVJoaAc01F7VnX6-asaFK5ZTPMuraBJ0YUKpBpgvEMxO-WnyVVxAFxsTihf2CHbQWK02VsVfmScmrSivqbp21aui2HUZfomi8Zv8mOtQ_hSVtleC3Qb0XZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGWJuUbV6JttIJFIFa10Iql4YHSupKFOjYPbDPROt64ZClUwa-Q8IIgW4Jvl9tB7Ywo3930Fqd4tMVPJi3fNT16VK6NdH0htJi5lTag7Hu2rErfh8Tu6gfDTa3UYQBY1zxs0DCBohyz_eg1RGCbRvbzUOPlOZOLQVOW9XeDSXzy1sZair33C34NpY9UlLjGP7Wev4PFgCLnc3uGWKSfDZnXtjtYLrOhvEJn4YcarOqlJ0QUOVlhhQBgSOhsRKv2Idtr5EqCfVsYlcXudra4EawjgaAUjTi22AkfnIfSNuscm1Ztr23i7gkDNopu_d2UEPcznM3sXbYOgSg_bv2baUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=jQVv6NDkJAbrW9BT9b3FHfO3FGj8PYprLwwmgnUh9qlu6JS7x1_Yfy5Gvv7uIKegmdwKSUCKf6pn9AFUxrqMHiHQAIt314rH-VmUS-1old7p8NKvJI_1QB8m3XKRQf0Q4rnMO1Sy-hkoG6dcP9TccVrhBWkoiwVJvV_YTpqUtmDi9gShpptI4XoXDMUtndjLEUrKWFFvmlzTBrofbbHNS8VT4-3lLAGEFGQ0V-dXEb7PIC5LGD2DfODBLNjC4vGz1IMKONfxquqaWGGbozcoA9bXqQbIdhx0_RGmWTO-GFUWoqahiDQjWJbTGfE1sN3TH2kAXoUG1uiOM-cSf61ZgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=jQVv6NDkJAbrW9BT9b3FHfO3FGj8PYprLwwmgnUh9qlu6JS7x1_Yfy5Gvv7uIKegmdwKSUCKf6pn9AFUxrqMHiHQAIt314rH-VmUS-1old7p8NKvJI_1QB8m3XKRQf0Q4rnMO1Sy-hkoG6dcP9TccVrhBWkoiwVJvV_YTpqUtmDi9gShpptI4XoXDMUtndjLEUrKWFFvmlzTBrofbbHNS8VT4-3lLAGEFGQ0V-dXEb7PIC5LGD2DfODBLNjC4vGz1IMKONfxquqaWGGbozcoA9bXqQbIdhx0_RGmWTO-GFUWoqahiDQjWJbTGfE1sN3TH2kAXoUG1uiOM-cSf61ZgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=dZTo3WfnDYfyyhvKDaWK0eHCrOM2MI53qvAjr7z8HCbMgOn4wHJ4otSiwFA5VK2oAncJ_PZ2MxgCkDyrA-OBBVUupzA0YyrZvtWNKgkHNehaP3lwixd_-0RIH7tpx5jh40-WnvbJjub7rf05OV_ySUskfwOk24vuPXtxHGPeZQtFeB7PguhNJ0T1ZBjQqs5k64NHxfdsAUaxgbVuTaYeeCsKgrLm0J-kD4qQMPy5WEr2nknv4RVXckuvx0RtSk34CobMzUkEDuQrFcE5nrASRJ0G0yUrvp5sIWPE7e9ovRxX5Fr_SzPemZb4s6wsujohERGb2vdYXm82lF0FlleM1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=dZTo3WfnDYfyyhvKDaWK0eHCrOM2MI53qvAjr7z8HCbMgOn4wHJ4otSiwFA5VK2oAncJ_PZ2MxgCkDyrA-OBBVUupzA0YyrZvtWNKgkHNehaP3lwixd_-0RIH7tpx5jh40-WnvbJjub7rf05OV_ySUskfwOk24vuPXtxHGPeZQtFeB7PguhNJ0T1ZBjQqs5k64NHxfdsAUaxgbVuTaYeeCsKgrLm0J-kD4qQMPy5WEr2nknv4RVXckuvx0RtSk34CobMzUkEDuQrFcE5nrASRJ0G0yUrvp5sIWPE7e9ovRxX5Fr_SzPemZb4s6wsujohERGb2vdYXm82lF0FlleM1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=mMHgSdSiURjojqsdE3jZAiZ2WgGhyaeiPw_0cX-pgUh5w8duxwDedRr1F_dMOs71zvUwCYMzWpyQAlJkuraM0gE6313BemuvEX3j23gJYY3ChLLErJPQ5zR6EGgAGIUfZN1hWfcru1zEm9adJ-x_ps1CovCYUuun9Nnr2ajtKI1Y_9e8pn_1sEtYPqS7c0RVBwIInrvMZcdJHJpK9atD8Pu3VY-wMomUBawLvYvl6dvfJ9ucTyiqW-UWBbeVkIJ7jlmR7dlD71amTXi9iptNfAnttAVn08S0c-RmKfEBNLFB9h-oqUqA3TmaFWOmvpr0nId4OLQ-JArdvcLp9S_vPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=mMHgSdSiURjojqsdE3jZAiZ2WgGhyaeiPw_0cX-pgUh5w8duxwDedRr1F_dMOs71zvUwCYMzWpyQAlJkuraM0gE6313BemuvEX3j23gJYY3ChLLErJPQ5zR6EGgAGIUfZN1hWfcru1zEm9adJ-x_ps1CovCYUuun9Nnr2ajtKI1Y_9e8pn_1sEtYPqS7c0RVBwIInrvMZcdJHJpK9atD8Pu3VY-wMomUBawLvYvl6dvfJ9ucTyiqW-UWBbeVkIJ7jlmR7dlD71amTXi9iptNfAnttAVn08S0c-RmKfEBNLFB9h-oqUqA3TmaFWOmvpr0nId4OLQ-JArdvcLp9S_vPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_99Lx6am7CAn7_XxsJwzqO98fprN5p55LhZRZT3A_EyPLqAM4EIOa1WZTh1WDlmcwz3fTIF_Cm2c_R1MSLPwpor_dVVV8QRc4Y7PgFSW4GI_564ykSJZZhfogK6rSM-WwtBAw-VbARjN0gd35sHNHJ17u7VrMQMpvZh9_PKwy09-gYG6BBdGIsYWPAsYvtAK6wpZMboaClU8b4He9vRji-EGjOLNJZB7jk-huWu0TUT2cKmjyRTgIQgbTgmtbIpHTqSInCK9wKVBAwXCYttIENDyy6tmsln4tAhVqN5lYIhI5VnX19HpmRtafJv6Y0W9XvNMNquENckSAAC5axKzQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=iBPJTasIy0Omreh7UoLpcYCZ9hANpU3NMY9zAb955Q3237mFhmzSKwXkWlqBv0929FdaZR-Qwd2GBy8hwFo5kcPbXOlxlU-LTeG4cF_dO-ClW8wQsUd2i2v8Yyg_l_8HuKGQ5VXUpq_KoPc2g9CQL3y5hzu96cIjOnD0__6E7SfuijHnQDxpu6YnYWLHXZ5t2-Ij62XIaCYrMQEOJ-0tc2r4NOI66kQ5MER6lF4Ior1e7vIBJg8RKMvXBwXAzOY8uvJbdPLsG2lI1xttYvkfSdwJYu2DUiA6NoSz-dBAr1mROg9Z-seMC5XigkIk022bqyHR-Lfd4PXvVR-UkZeOslFC_QSFkh70nYvLfFpMKoKcrgAW4cmoNgbftP9c5xwRaSWmJgMfL87PplzWBdyiMCDcUE5W6En8i_3JUF9C_sR9SouwfSaVipwIZtipUGlpwujq6XegtxWU8RXV20pSS-HQ8qeqGg8DhOTYmrTAnyS0ASbCtThF4KX_0-FCwj0alLwSfFjnR-VIMCUCYmV0Ct7ByoJ3HsFRK4DIITEyP1USSWz24JGGM1ivjfhG_Qmo01sba5kZRboqGCikEJsFmHR4Njs_UR7Xuj5iPTnseM-BNamxrs5EQb2txciqVZsa4no7moLK3TnbtBfvY82CcinIFc6iZNhhBhQTG92IDIo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=iBPJTasIy0Omreh7UoLpcYCZ9hANpU3NMY9zAb955Q3237mFhmzSKwXkWlqBv0929FdaZR-Qwd2GBy8hwFo5kcPbXOlxlU-LTeG4cF_dO-ClW8wQsUd2i2v8Yyg_l_8HuKGQ5VXUpq_KoPc2g9CQL3y5hzu96cIjOnD0__6E7SfuijHnQDxpu6YnYWLHXZ5t2-Ij62XIaCYrMQEOJ-0tc2r4NOI66kQ5MER6lF4Ior1e7vIBJg8RKMvXBwXAzOY8uvJbdPLsG2lI1xttYvkfSdwJYu2DUiA6NoSz-dBAr1mROg9Z-seMC5XigkIk022bqyHR-Lfd4PXvVR-UkZeOslFC_QSFkh70nYvLfFpMKoKcrgAW4cmoNgbftP9c5xwRaSWmJgMfL87PplzWBdyiMCDcUE5W6En8i_3JUF9C_sR9SouwfSaVipwIZtipUGlpwujq6XegtxWU8RXV20pSS-HQ8qeqGg8DhOTYmrTAnyS0ASbCtThF4KX_0-FCwj0alLwSfFjnR-VIMCUCYmV0Ct7ByoJ3HsFRK4DIITEyP1USSWz24JGGM1ivjfhG_Qmo01sba5kZRboqGCikEJsFmHR4Njs_UR7Xuj5iPTnseM-BNamxrs5EQb2txciqVZsa4no7moLK3TnbtBfvY82CcinIFc6iZNhhBhQTG92IDIo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=SfnY5Y726y1xQyQ9sR1PU8dxDhBrf4r17a_KANAR1-umeXBRkFeyG6V5QL10X26Kbq0zog-kvxYnpsO4FSMlYlruBf3PdKbhGmKEG83Cn6aGXntJyjkGD_m_c2e-ZAJCSINTe6BhWfKoyBBb1l8XcDvSWCggnesfTb_Lzg9vXtqp_oB3WLHZJuQPmbpI3g25dqKnfQpaHgev2OswGGRW5MJzvPlTzpyUbkt-fHlg7IEeGDqfCRnKM7L5OtFYXV2DIqdxqRMqeM0EoEDWD8FyRPpGXYiMnm2SO-LqjpErNJlW1TInj5eRVbOrfzXnf2EgwOaqBaEAC8oqkuLYe98E8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=SfnY5Y726y1xQyQ9sR1PU8dxDhBrf4r17a_KANAR1-umeXBRkFeyG6V5QL10X26Kbq0zog-kvxYnpsO4FSMlYlruBf3PdKbhGmKEG83Cn6aGXntJyjkGD_m_c2e-ZAJCSINTe6BhWfKoyBBb1l8XcDvSWCggnesfTb_Lzg9vXtqp_oB3WLHZJuQPmbpI3g25dqKnfQpaHgev2OswGGRW5MJzvPlTzpyUbkt-fHlg7IEeGDqfCRnKM7L5OtFYXV2DIqdxqRMqeM0EoEDWD8FyRPpGXYiMnm2SO-LqjpErNJlW1TInj5eRVbOrfzXnf2EgwOaqBaEAC8oqkuLYe98E8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iP3Y7YiQE1hBNsmrHnD1tP1FDSsmGqtB7f6oqu_8JegSq8wkeOoalP7-FWqw6SpkLKFPiPP5AtPHNLGqWtktLBEQO09BMwsGtEV8CBZvfDObWQ3tzJRNnctbyGD48fgrOW_UnUexlDKY_YRF4ylum0ASwZfwkLOR_Nl_KoLABujK-X9bfB_FaHkmxp6oSVGtli0a4OkJyDu4ej5_E41rD-VlCrk0p76-QkQiqxKJ6hkm6esk6h_LZ9vQt6BNuMvyqKYgV0xfr6WV5kFDf-fdCL5Y4RcdPpCVQkearKeITitGWLhVP6k_lWq_EhwJwWP-wiFO37E42p5YYtHv0yYX3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=AaTQd_36ThW6b_sXxIrtGhdMopcR4k5WmrDAWGtqrQcBsY2OgnpdBPw-cPW-qn1lFO_AUmyUOYJwkTRJRJLmrcAS00EORDa6xvKC-UbSA3p-BiaO3hMcGBqDVs4i5dK0guGIP4iPPyyHJ-xLEN-CJkedjoGAhbl_dcVulBQyNh8aagV9QCerymESllvjVKISIbCVKXnQ_o6552GyRPPD4vAdInJjTKKJIibgWUnYWnSoLcQlPGT-xJ4KISN51i3Uc8NOasBssPx8WL3j148CnAu_DP4olyODrMrFGt-sWzuasJA7Gm__ORe0Fl5q9rd1kJvCwL_k-934-oHcBavKQiU9jOr3c4M1C49Yv2Z1QEGoCLgFuq1bOmc6Kn4YzUknVmDtIKQ_5kp3NNmchLma_5FEb79yUNBmA8DQi9JpumA5tz48d7thUYUv2sLvyamtsnHifMeAQOaBkYhM-hIsvLdWS653GjKMOS8FSibHjzc-bTFh4fhzIdgQ8c69uOrCIFx0ZU5UmHOB_5R3aIa74Gz2byVhNeSW7L1iuj9noqqWP2PsfyLio4CAL4Aw8207FKfaOx8r1pNBaJ7eZebgU4I6PphO70sBevE6Go4c2pKtQFP1FWPQ02zYyVyj3rXI6zpszijnSfjrFz5iFx3H_0cODgLndur4Vkrsif0xiR4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=AaTQd_36ThW6b_sXxIrtGhdMopcR4k5WmrDAWGtqrQcBsY2OgnpdBPw-cPW-qn1lFO_AUmyUOYJwkTRJRJLmrcAS00EORDa6xvKC-UbSA3p-BiaO3hMcGBqDVs4i5dK0guGIP4iPPyyHJ-xLEN-CJkedjoGAhbl_dcVulBQyNh8aagV9QCerymESllvjVKISIbCVKXnQ_o6552GyRPPD4vAdInJjTKKJIibgWUnYWnSoLcQlPGT-xJ4KISN51i3Uc8NOasBssPx8WL3j148CnAu_DP4olyODrMrFGt-sWzuasJA7Gm__ORe0Fl5q9rd1kJvCwL_k-934-oHcBavKQiU9jOr3c4M1C49Yv2Z1QEGoCLgFuq1bOmc6Kn4YzUknVmDtIKQ_5kp3NNmchLma_5FEb79yUNBmA8DQi9JpumA5tz48d7thUYUv2sLvyamtsnHifMeAQOaBkYhM-hIsvLdWS653GjKMOS8FSibHjzc-bTFh4fhzIdgQ8c69uOrCIFx0ZU5UmHOB_5R3aIa74Gz2byVhNeSW7L1iuj9noqqWP2PsfyLio4CAL4Aw8207FKfaOx8r1pNBaJ7eZebgU4I6PphO70sBevE6Go4c2pKtQFP1FWPQ02zYyVyj3rXI6zpszijnSfjrFz5iFx3H_0cODgLndur4Vkrsif0xiR4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iS6Tm__mhcQYKQ5xsL9LOxsba4deHQfqWoDc3qGF-nloI6vEOFGTDsOlgAX5eBrRm8HSI2kmH-tY1B0xvPJwNrUP90KcjCfqckM9DYHw9ZNoj__tKwICyNpHF6Q8lPownNocKcH_FMcUI7XHpyf4tORcSMqeWfLNUlJXjqvLTgFuiS4DSvyG4tpiNPvQ6k1Jt7LPuxcdQiTAmbU6ov6XX85QYWOmQ9wjx-tlryXchW6Mg_PCcZYI0AXTh1XTOslC93YZXVp4PZr4Plgi37g0vI4IYa1pkrkW55nh5Cy_nvuRWLl3JZo41xJMHFQZgKTEh7GfsYpOA-rQHyV7iL1qtw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=I8dQGCPk4foKdM6w-AY3UBu_UN8sZn_Cn05onYElsT-g_Hy5p_3ACu-wggAqD26b8oubPt40bPQ0eBdIT5PVjvdurgAbPj4fZ2VcX4uyHdmfGLeN7DLlki1nFwywLbsH_McAkn698pTCrRsVXKwaaIYvUZ8h_qvy68y4f3mEDi4R9_olgCumMqIM4ya8UqHx392-byNNZt5d_JihoUmB3jJeVljeqhGawlSV0Kv6THLzP7ZsEoDjB-RZDlmV6j3EAw36QNsz0i1LI0vqWMy7wgsJcp6t23VHzHG6RFck-cIrFRXPhUxW3nC0haiLWpAmYILX2IL7sMVom___gGQjHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=I8dQGCPk4foKdM6w-AY3UBu_UN8sZn_Cn05onYElsT-g_Hy5p_3ACu-wggAqD26b8oubPt40bPQ0eBdIT5PVjvdurgAbPj4fZ2VcX4uyHdmfGLeN7DLlki1nFwywLbsH_McAkn698pTCrRsVXKwaaIYvUZ8h_qvy68y4f3mEDi4R9_olgCumMqIM4ya8UqHx392-byNNZt5d_JihoUmB3jJeVljeqhGawlSV0Kv6THLzP7ZsEoDjB-RZDlmV6j3EAw36QNsz0i1LI0vqWMy7wgsJcp6t23VHzHG6RFck-cIrFRXPhUxW3nC0haiLWpAmYILX2IL7sMVom___gGQjHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLjDGsJ_7lZir6mEWembpVmnn08cEDe0zLs_-1DAmxNkfIG4oe4CFfGJ3nNpHrYUaHgqBwwcElqemM2hLHillYsbCUeQ3dXKQdrsyB_c0JT4JrMf_rt0zNsfGZA4tNsMCoDdSTcZ_l6t32GhYal6vxBgLpZS8VTz-gCM6r62GB46voIGukkETN26dvVhAhtkH5CEfb4CXGGmJJZpY6HgladlCnJ3hleriE6BguqtE6efUsJ-5D0U4xifCWC2Jm80mO-ZEwEmXJhJAyZLXzWeCcD0xPYjDmiEaAbuXWKjcaKk1jKlFC5tX7wnOW5wKJWeDwx9oMme6aRzeKq98oGEiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVGUscN1_tc__OcTWz_A-A5ajXH83IJ7FpGV6HVm5evaaYgWkcv2VZPe9clMEf50u0nEu3fDSQ4AW6FRQB62LvzV2r8KOZyHs4gI2-qqNUeZKZSnF7MnFkca6msnHIDPbX2y8WVAXh0aIaZyfM0MhSO--K9dAuhdJEagLLftgwWPneGBlGGHgMV-TiAdnPbCPu58Mv4lx-gR4XVJHfAg8ngRGqymadbmnCpGQcqLh_uV2phGrDrPtoLTuZTGFZz9Z_BYhQFatye01sKXe938OPEfc3BhdxB8wSsHCn-JJt03L6Ivrpnc4HBsE8kN7IKWBNiRRZlrNEnA7qd7yPFuag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mITcVi2PawgpvM5ps0lVRXFN2qfRBNZLzW4b6thBpfQIz6PE106IsLkRhGETeNmfu8y0pqBibdm-27QOeIZ-ZpfUgvWCM2bB7IYFY-SBGB1Jt4Jngw64ZyuxVgyWSdcbiXNTMrKghf4l50w6Bk48NItSlRET01dwrbQFO8b-1YBGUVnEu6vIzAEWsQpVGMSb-pz9MvBSjSGFI6iAeJoc_oNlnH3bTaGS84nN7IuGe2tAawxWHQUzPYaDU4r2S_NFQSpzb4cXxvlOuJqDcP4ZQaRp9vulkCZyDdNQTV4eDsFVZB8wtdpwdkNaEbBcAZMVoTe0WA9NQ5PNeWsSsGnQNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=JCXsr4aKgXPwkdF8fha-bK1ltqa3md_jFKMXuYGADSaU7QQzXcOCajK4noLFqXB6D-fD1ppVx_9U4e917mYAv_1_hcwDImEUljVceMkkkyz02Wflz3F6OYsjEQbVYNxGkvPLCyN7SOfNrs6bLMwlM1UgwcSL0hNmNTJPqEKg4yWLAj0ZycqmWIYIbPjBEnicQZ00Fm8vmLaEa7zcAkJknl1DnGsjk1ZHKO7SY054v570QVnGLKFXAntoIKY7yE-3s2JI-PuVRGaGJ-d28WzllRdG7MYQmBn6oJkn6Zk235tsUr92ESBqVAHyDkI9A92zOSWuIKCiaxB_-CtpNTfAZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=JCXsr4aKgXPwkdF8fha-bK1ltqa3md_jFKMXuYGADSaU7QQzXcOCajK4noLFqXB6D-fD1ppVx_9U4e917mYAv_1_hcwDImEUljVceMkkkyz02Wflz3F6OYsjEQbVYNxGkvPLCyN7SOfNrs6bLMwlM1UgwcSL0hNmNTJPqEKg4yWLAj0ZycqmWIYIbPjBEnicQZ00Fm8vmLaEa7zcAkJknl1DnGsjk1ZHKO7SY054v570QVnGLKFXAntoIKY7yE-3s2JI-PuVRGaGJ-d28WzllRdG7MYQmBn6oJkn6Zk235tsUr92ESBqVAHyDkI9A92zOSWuIKCiaxB_-CtpNTfAZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULnrIYmI5FNVZyJzZyTKiFot-XD5BlDSd03DzkvM4qxGX8FBB52Bvj6lEsmKqlzRr61RHwZQvwyFb2ZzMfml_Udi44yQx2Le1QOIN3_XZSnEjTeaOT-enbLBMuVf4-hdcIgTontx-JZkI8hnW8YAHzmthDwd3pdQDQrwq45aYAnV9XSQV7pLdPGzghkL24LqPJXcjtRjTanFObjj7Hajnf6Oc7mznGWnsdNTEJvjfutQ1cz9Q4QEPlIHBp56dhYgM-RygTbVJeaWe7Gkn49RKP953dcFmyXA7aGSANmPY9RXQJtaUalbQgxmF8YANITScwfLyuy-IVA3ebgtVn18Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFGJw1s2LuAQFkVcOw2AzPca63IGwuvdJLkaWTZKxC6q75bQ44GDJBridkq1xV1Ld44cA0IEcSSGWW73P4bW4SBqYy2faDXl7pumViZgIuALd22_rubBy-NxcyL7LXw1Xu4sxqzkZKXfvjWcU_gFzrM1fjRhCu_vw7XAN6k7zIr5OX2tV13-2doRz4wtJx0T0pHNOs9acFAdbKM7gcyTU4zS8Wm4lxPUExcn8-sILRzXMkIswwzwdPXnlozgF8YL5gSI8cfIX7Z0ZEDg48Y07KmxXKtrH5jWUXl3XGCNdC2AO4xcmf5J4z9AHCZqCCMjtunRXTq0WMvQx0tIytb88BoE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFGJw1s2LuAQFkVcOw2AzPca63IGwuvdJLkaWTZKxC6q75bQ44GDJBridkq1xV1Ld44cA0IEcSSGWW73P4bW4SBqYy2faDXl7pumViZgIuALd22_rubBy-NxcyL7LXw1Xu4sxqzkZKXfvjWcU_gFzrM1fjRhCu_vw7XAN6k7zIr5OX2tV13-2doRz4wtJx0T0pHNOs9acFAdbKM7gcyTU4zS8Wm4lxPUExcn8-sILRzXMkIswwzwdPXnlozgF8YL5gSI8cfIX7Z0ZEDg48Y07KmxXKtrH5jWUXl3XGCNdC2AO4xcmf5J4z9AHCZqCCMjtunRXTq0WMvQx0tIytb88BoE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=T6HRRJR2kzQf7XmQTMHpIZuFHVW2dy5amsptt3uVxznERzKBogIHR2OB-r4HFPQ--bc_tfLPt-YJTy5i3t1yGh8WdW6K6EbQE-NcWsxrf_IcExCkgOjfv9Rr5-0tbDabD9Q1ORzv9kA0KyZT1WwvBop_e11B2N3AvCahCdx4zRCadMSLRUwfQFW8C0NGI7-U75egV0B9hanjfLO7u7DoGezC63z0n3s34b5fA6AVA-hMO2Ddvl01WrzM03XIPaYmlPaGdMPrEMlsSOcgr4BGwlyngvC4PQqStll6bFPT8mX2uPTNHyncLTUWlKES6x_MROnesQXYrLVfx4Dv1AZ_Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=T6HRRJR2kzQf7XmQTMHpIZuFHVW2dy5amsptt3uVxznERzKBogIHR2OB-r4HFPQ--bc_tfLPt-YJTy5i3t1yGh8WdW6K6EbQE-NcWsxrf_IcExCkgOjfv9Rr5-0tbDabD9Q1ORzv9kA0KyZT1WwvBop_e11B2N3AvCahCdx4zRCadMSLRUwfQFW8C0NGI7-U75egV0B9hanjfLO7u7DoGezC63z0n3s34b5fA6AVA-hMO2Ddvl01WrzM03XIPaYmlPaGdMPrEMlsSOcgr4BGwlyngvC4PQqStll6bFPT8mX2uPTNHyncLTUWlKES6x_MROnesQXYrLVfx4Dv1AZ_Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=GBUWXB8VhSqCSsJI2gPwKVRJbmWi63voMpA4eywz8oX9mYjBs6AT3B6BY7JwjPna7A4-IXcoq9Pq3SRDxJ_LoplfDIP8c8P4xCbM6RJy96XQFytbHOiYFPzUDlxKWYeHvX9pYaown3NW0BRDdDE0N9ez1RY7MeNXoSoRR-lscg45UJAqMJ_LkfOcbPz8g6zcMEBoz-hKvpWLAOqFSibWuF4i8N4xctLTWVe0pP0cbwqArDyCB_UCO1EX3__UWqPRWen6MRwLW7yNwUSTru5GX2Qf3-g4oV9_4VudgL7g75zR1IcWZjPqP79DDL8Y3QOX5mZnbY4gJJv0xId7HTRCC2A7E1BJVAPuhT3DLjNa9i_IodGcTiKw5VrSf_bfp1JQGvXp9P_MVeQviWARuVBLlLXZ-_UkYdDuC8k-p0jIOVr89EI4xQlbDbuHiAq3JrvFVUqTdvc5IkrAwklrVpwKieDVLvSSKoHEPgM4zU50p0H2522vN54ZZm0-70o7JzmKhoggcJPDtFeybV-THbpEbL6eyQ153uHjk48daPVQdPTftS-f_zQYzE0ZT7lNwV8ghYw8Dm67pQqug-xGHAtCcj1l2dSRDAuwudo8fP3F3pavZ4YsIGgwh26rgUX_UA1gDN8zrZcSmcKd65UwJXHvovUE37unZ4gvf5eGTw-bSIE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=GBUWXB8VhSqCSsJI2gPwKVRJbmWi63voMpA4eywz8oX9mYjBs6AT3B6BY7JwjPna7A4-IXcoq9Pq3SRDxJ_LoplfDIP8c8P4xCbM6RJy96XQFytbHOiYFPzUDlxKWYeHvX9pYaown3NW0BRDdDE0N9ez1RY7MeNXoSoRR-lscg45UJAqMJ_LkfOcbPz8g6zcMEBoz-hKvpWLAOqFSibWuF4i8N4xctLTWVe0pP0cbwqArDyCB_UCO1EX3__UWqPRWen6MRwLW7yNwUSTru5GX2Qf3-g4oV9_4VudgL7g75zR1IcWZjPqP79DDL8Y3QOX5mZnbY4gJJv0xId7HTRCC2A7E1BJVAPuhT3DLjNa9i_IodGcTiKw5VrSf_bfp1JQGvXp9P_MVeQviWARuVBLlLXZ-_UkYdDuC8k-p0jIOVr89EI4xQlbDbuHiAq3JrvFVUqTdvc5IkrAwklrVpwKieDVLvSSKoHEPgM4zU50p0H2522vN54ZZm0-70o7JzmKhoggcJPDtFeybV-THbpEbL6eyQ153uHjk48daPVQdPTftS-f_zQYzE0ZT7lNwV8ghYw8Dm67pQqug-xGHAtCcj1l2dSRDAuwudo8fP3F3pavZ4YsIGgwh26rgUX_UA1gDN8zrZcSmcKd65UwJXHvovUE37unZ4gvf5eGTw-bSIE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=CPjYxrKMpt-DVB29-TWATEN4z0f5rnAWH5oNKHNqzuZPOcsFZkbOttvnXw8ZDeG2SIKJiwLe9nq4U86dv53Jq8_ZCPlmjVYFj-uAvui2GUyLMY_yVtT4RZpDmdb6DbtUqPmsV1rSLn9ru4M3RkIgI2NRaEt8XGPFTw9qGJ2xGKB0MylWAXWZ_yKkQJuCy6wvQkVGGPWRM1McQYTLG3gP5iCl9HaqpT9ps0mDJY-aWZI6D4eI1QX_Uar4svut8TFHZHFL1N9PxbLTt9c9BrGhWW6vF8eToev8WdR4gz4CFeTT_yJM-BRMRaCuOYxUkl1pD4wFYg4M_QWWzRCW5iPpMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=CPjYxrKMpt-DVB29-TWATEN4z0f5rnAWH5oNKHNqzuZPOcsFZkbOttvnXw8ZDeG2SIKJiwLe9nq4U86dv53Jq8_ZCPlmjVYFj-uAvui2GUyLMY_yVtT4RZpDmdb6DbtUqPmsV1rSLn9ru4M3RkIgI2NRaEt8XGPFTw9qGJ2xGKB0MylWAXWZ_yKkQJuCy6wvQkVGGPWRM1McQYTLG3gP5iCl9HaqpT9ps0mDJY-aWZI6D4eI1QX_Uar4svut8TFHZHFL1N9PxbLTt9c9BrGhWW6vF8eToev8WdR4gz4CFeTT_yJM-BRMRaCuOYxUkl1pD4wFYg4M_QWWzRCW5iPpMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ld_3Jv6TYhJjQY9adD5oGj4M7ID1a6pQpFW63BxRZIUUlGQU1yJBuVDzABakOfZ_KgDwixWA1yx1P-PvbS46Am2D3Sp4eMAvYk7mWQ-_zYCKGFsoM7EeX5By1td1d19dxi-MWEdL1p7NvdrC5wFGnNb9srVB6tLTnOeAcjrf_tfBS58XPhFQVP7xjb5nYhCzAZRcWmGUNdpLaZnToZH1A4wMED5lS2daZCW5LpMUwdwhXCrcrNGAUfs589W5sxTJOjfLWjuoVmFW85liNGNFEytF15mrngERqVI7-J10UOW-NoH8njwAgXea_IjeZtbAtaCXhcYTMMIlp6lueUzk3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=VZF9hVRyxMYegcbmtyRSJRWIIOVbZoaIUipkYXHTdnFadcTL66mFMmFhd7puT_6JMKibrnKXbkftkokEdZ5wJzFf6cjPSDnbngsHB1ti5nlxD5fVITF1LIk8tWyTmE3p0Plu7A4LrWFEzS48s459FX4FE1cEE11HQttnf21OLhd-94S2RxltiMy9AbQ0d1geEQRHSEeOQMDK7jx63WtWB1vEJGMNxgNpjnb2z4dyNYul5i7gDQonWKQWmsfqhZgq0v2mYdfXPg65-ouLhzlqkpmADzCDbgqLAJHik-A1ihuGLB6-m7FTK5fJThwDhOFXLC8dtlrMKfU1JsUcp6fo0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=VZF9hVRyxMYegcbmtyRSJRWIIOVbZoaIUipkYXHTdnFadcTL66mFMmFhd7puT_6JMKibrnKXbkftkokEdZ5wJzFf6cjPSDnbngsHB1ti5nlxD5fVITF1LIk8tWyTmE3p0Plu7A4LrWFEzS48s459FX4FE1cEE11HQttnf21OLhd-94S2RxltiMy9AbQ0d1geEQRHSEeOQMDK7jx63WtWB1vEJGMNxgNpjnb2z4dyNYul5i7gDQonWKQWmsfqhZgq0v2mYdfXPg65-ouLhzlqkpmADzCDbgqLAJHik-A1ihuGLB6-m7FTK5fJThwDhOFXLC8dtlrMKfU1JsUcp6fo0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=ekHUtW2tG_IWgRGbpo01ye4MSgmdirNWY1O28lGglwC2V56Hkj44z8df0OyBnpzUl_ZD_wnNl7Vkq0Qybc3lA36-UIRkZCqfFx3nIKVpVBP480lrn9hn11lsnY4oVAQ7rx9vX7HbQAExNRyN_cz8Ldzgy-u6SHmOKMZAtK_20gvBU20OdiYKxAk6j3ptdHdJxyC-B5Tjb_LmSk4W6AGLLM9YJCK1DgefH4R6tyvGUua2FycQI3Rx9rJlqpiQWn1myJ8ZenuwvmPPc9x6jC9o_TLgIpqzR9YD5rUu3ljw5Qz2lvqsjDd9wqNir51yFIr4EhruJR_5KdVU2uEKD6JqWgymg7nrAi0GWLDKOObHbKrMj_8g3UbCIJ5icTV2HliK8RTEekpl_FLZ6mppF7s3mRPEg0OZID3axz06pQFRjX6uhBXCt7VxXENE-V4zBSz0fjWExERgd6SCEsaxf4knVG923CE2HIAarR9fzWzR6UrgS2SFy539XGA2rp5AVx_DbpvHEm51gHQI6aXh2RsDXRv3FLpmcG-WiQ8R4e0EvmX9qGxWNriRkW5NRYWaQ-YOOztqpuICNGTxe-_jiNCxI-F4Y9OR4rkcQ2AvVgRnJSpTS6_P-YLZF4pXPrcQEYzu2FbrSljic5SfeDoJq_qD0xZS7oCrzDkzH1PxksRiLTc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=ekHUtW2tG_IWgRGbpo01ye4MSgmdirNWY1O28lGglwC2V56Hkj44z8df0OyBnpzUl_ZD_wnNl7Vkq0Qybc3lA36-UIRkZCqfFx3nIKVpVBP480lrn9hn11lsnY4oVAQ7rx9vX7HbQAExNRyN_cz8Ldzgy-u6SHmOKMZAtK_20gvBU20OdiYKxAk6j3ptdHdJxyC-B5Tjb_LmSk4W6AGLLM9YJCK1DgefH4R6tyvGUua2FycQI3Rx9rJlqpiQWn1myJ8ZenuwvmPPc9x6jC9o_TLgIpqzR9YD5rUu3ljw5Qz2lvqsjDd9wqNir51yFIr4EhruJR_5KdVU2uEKD6JqWgymg7nrAi0GWLDKOObHbKrMj_8g3UbCIJ5icTV2HliK8RTEekpl_FLZ6mppF7s3mRPEg0OZID3axz06pQFRjX6uhBXCt7VxXENE-V4zBSz0fjWExERgd6SCEsaxf4knVG923CE2HIAarR9fzWzR6UrgS2SFy539XGA2rp5AVx_DbpvHEm51gHQI6aXh2RsDXRv3FLpmcG-WiQ8R4e0EvmX9qGxWNriRkW5NRYWaQ-YOOztqpuICNGTxe-_jiNCxI-F4Y9OR4rkcQ2AvVgRnJSpTS6_P-YLZF4pXPrcQEYzu2FbrSljic5SfeDoJq_qD0xZS7oCrzDkzH1PxksRiLTc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Stk6XaM8lM_KHhvzW5jPqlQ93VZ9dRro04HWBHQSnI6SbT4bdz6rDb1-BfCiTo2rQ4sb8Id5BjTG8JgDKGQOMB6AvdjNDpmxLkYBrVLxsAN5svx1E_nOOBawhkFfQQWsdWLZxd4EnR7iJ3QGDsaR8b0slhCrbPB95FyEaWXBezBdnVwit4fyw23zB40TcLVqoh5LTdP-698jdmPeQuJ7dXSFHKHc7wVvH9wwk1eF8PyxoNYkh1H4iRMOMtxX7zSde1H27O9CzWfa2YNofGKjJWdJjrnFzlISNFdDHQuEaH4CF_hKRbKW9svT1eNznf2A_aGOvmD3liyhRr1VwHzeBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=E7R0In3db3Guci2ErwL40N_KLNSZWPOs5xMutEHYJonJlLEpKfx9YnxuGOYKbNu-85zgJVdqpCHl7KOVQQt5zj4pVvZsdIi8pb0rIG6gQQe9EYQ0fB_KAErN1J8eUhKKjzsn8g_8k43ACSZAd6OI3gtSSGyAJq2fTcYXx5_Egb4xq07pU80TIq3ZeYA1cYd9mmA6z5Ed3XB1x38a31hk_hFJI1joW30JJQlNafUwNZczyExyHjtEqAPLLFjm1ZFSREpIVwHgt95OHW8D0SY3YV--_dE2ZCfsypANBG9agvspwgQhmxNflUhIlea9vd2PW0T1LP3f4s3JVt_mNYfWP2C5iWW_Ehj7lJvwABnmIfKKUHoKEClz5wBfCr1vnnJsk5jrS6UEa919nvc7-TvIxW6V0-NpMsVZFrbOc-7Sc26XAIIowRMNZ0Cv_RftmTcrrS1WlP8lh6dyZKeYt8x2j7OoEPh24LWVZKPQ6hiz_vDyHLZuRP46gr8Eo8skIEknTdLrtCJw3pEotaqXysYw_Nxl6TSEstR5_EWwrvuedsSdERepba5VuFBufotTtduVyU5KfewV8tNsgVYpOEszt8hAjaw9V3SRA1cJEOiHf_2k2OkCzYtMqBcNV2mMwOozwYHa3T2YgECYQUbbH2zN3q3dcKp6gHvTMeh5_jxlCrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=E7R0In3db3Guci2ErwL40N_KLNSZWPOs5xMutEHYJonJlLEpKfx9YnxuGOYKbNu-85zgJVdqpCHl7KOVQQt5zj4pVvZsdIi8pb0rIG6gQQe9EYQ0fB_KAErN1J8eUhKKjzsn8g_8k43ACSZAd6OI3gtSSGyAJq2fTcYXx5_Egb4xq07pU80TIq3ZeYA1cYd9mmA6z5Ed3XB1x38a31hk_hFJI1joW30JJQlNafUwNZczyExyHjtEqAPLLFjm1ZFSREpIVwHgt95OHW8D0SY3YV--_dE2ZCfsypANBG9agvspwgQhmxNflUhIlea9vd2PW0T1LP3f4s3JVt_mNYfWP2C5iWW_Ehj7lJvwABnmIfKKUHoKEClz5wBfCr1vnnJsk5jrS6UEa919nvc7-TvIxW6V0-NpMsVZFrbOc-7Sc26XAIIowRMNZ0Cv_RftmTcrrS1WlP8lh6dyZKeYt8x2j7OoEPh24LWVZKPQ6hiz_vDyHLZuRP46gr8Eo8skIEknTdLrtCJw3pEotaqXysYw_Nxl6TSEstR5_EWwrvuedsSdERepba5VuFBufotTtduVyU5KfewV8tNsgVYpOEszt8hAjaw9V3SRA1cJEOiHf_2k2OkCzYtMqBcNV2mMwOozwYHa3T2YgECYQUbbH2zN3q3dcKp6gHvTMeh5_jxlCrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=rHdEubIJ-Tqe_lf7D5Iv3rWf1Hp4aLJj7Gx9eRVXGB0LGzMrwy00QGXb96erjF6v0IvwHqBkemQKNtSik34Y8L3Qz31Eb29D9eRphWlUg19adWp_oxisAlm3mTXQd3uWuXEB9pRYSoyxTy9gk3ISAkntGa6N2yneU3RMNm7w_jIz-1hOW0eERIndiKX22RQ5TiS9Tjf_agjGoHwH_W4KGMyyD-FTeMHbUqQhEkoM5b605cbbqtxoayb7Y-iOa_WTziyDLMEk5_unE4PHfJH4TKfLvQCJRGsX1WgxIaGmp0ZrSQaHHSYqKBYTK3mhXupyjr5fCyH_vYpt32Dr3EMEkkgKJ2iedp9tTuv5D2CEGks_dutqPc0ItwysZlXqIdvg0cfvVcfKI9uLI5Z_uBJ3uXrEJAbYfl8W2S09jHYFV499ZGK-NsmBfcSIPR3ClbKJmtdBBpQA8JyH6oTJus2969-Y-g9AswdQo4rbwVqQvEnFOJ8JsldGFK3SL0-nnSh_rT9SyWbLnzUmiX21gjnji6eHEjSK0HA2P6d8C0I_qPv8IyS8cY1qDfo_y31suNXNlQl7jmZVznVeYWIIz5xD-YugpQXnshk88n06YfkUcHikVGVnoVCr4tYoxWlOL8hnU8a5bqKYd3DeDfx-iO3TITmd1pO-XoEDqMuiJ1wWGu8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=rHdEubIJ-Tqe_lf7D5Iv3rWf1Hp4aLJj7Gx9eRVXGB0LGzMrwy00QGXb96erjF6v0IvwHqBkemQKNtSik34Y8L3Qz31Eb29D9eRphWlUg19adWp_oxisAlm3mTXQd3uWuXEB9pRYSoyxTy9gk3ISAkntGa6N2yneU3RMNm7w_jIz-1hOW0eERIndiKX22RQ5TiS9Tjf_agjGoHwH_W4KGMyyD-FTeMHbUqQhEkoM5b605cbbqtxoayb7Y-iOa_WTziyDLMEk5_unE4PHfJH4TKfLvQCJRGsX1WgxIaGmp0ZrSQaHHSYqKBYTK3mhXupyjr5fCyH_vYpt32Dr3EMEkkgKJ2iedp9tTuv5D2CEGks_dutqPc0ItwysZlXqIdvg0cfvVcfKI9uLI5Z_uBJ3uXrEJAbYfl8W2S09jHYFV499ZGK-NsmBfcSIPR3ClbKJmtdBBpQA8JyH6oTJus2969-Y-g9AswdQo4rbwVqQvEnFOJ8JsldGFK3SL0-nnSh_rT9SyWbLnzUmiX21gjnji6eHEjSK0HA2P6d8C0I_qPv8IyS8cY1qDfo_y31suNXNlQl7jmZVznVeYWIIz5xD-YugpQXnshk88n06YfkUcHikVGVnoVCr4tYoxWlOL8hnU8a5bqKYd3DeDfx-iO3TITmd1pO-XoEDqMuiJ1wWGu8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=dSnFsmJC9lOyEcy2Bv8b7bb90Vb3Ib67WWZzmLL0BxSh-OlHl6pVOvz6yZQ81a9hzN5VHNQjTY44r_LMEm9CMwseg1_j6Hdme3LbrRnxAc2L5eRAwIwqfUr53yZSJzRTjuGBWVp5vQhlUXcnPQ3NI6fcyuArJ09CbcCLPTK6le6t7Ik2LzLr7ZYI77ap4mAD33qC6FjjQKTtJuIQQ6OUgNuSDRxfkqCmR9e2vehM4LJzC3UsxKOOarazANh2IAqMvLStsQEEDYIyGC0FzZXbPrW_zPYdA-7i6za3dW4hh69VR1AY2sm3D-gq8NVzuidY6jnUHXsXQ5pDvDs1iYYhPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=dSnFsmJC9lOyEcy2Bv8b7bb90Vb3Ib67WWZzmLL0BxSh-OlHl6pVOvz6yZQ81a9hzN5VHNQjTY44r_LMEm9CMwseg1_j6Hdme3LbrRnxAc2L5eRAwIwqfUr53yZSJzRTjuGBWVp5vQhlUXcnPQ3NI6fcyuArJ09CbcCLPTK6le6t7Ik2LzLr7ZYI77ap4mAD33qC6FjjQKTtJuIQQ6OUgNuSDRxfkqCmR9e2vehM4LJzC3UsxKOOarazANh2IAqMvLStsQEEDYIyGC0FzZXbPrW_zPYdA-7i6za3dW4hh69VR1AY2sm3D-gq8NVzuidY6jnUHXsXQ5pDvDs1iYYhPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=IjzPaKEkY_uTRm_hhStKxKCJ6Nfo3PXP0sk0f0Itrp2EN_yY6_s7D4jHiDkZ77inSpWwYXch-c1YzxFNha04_cvphBoXcWHLbiT5ZCFbOsUxYVLNh7mrtjk1q6MPMxTITv5Hw6GCXK9ahcWWWEG4qSvB9ckSTYKp6FDYi9IeHEulqgHkg8MjzpROchG3Ei0Mf4obljYLJKwKhesbgThx1IML6S_fXshFHBKD9u77Id8xraVwf5HkQY2-ZOnrQpZxTtr1YUL7HOZsFr-FGcIgcimW97fpB69nCv3EVkEc_7M9utBhisMd-Vt7RHsAW0HuWFiyGC3_P0yPKYmUspxMOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=IjzPaKEkY_uTRm_hhStKxKCJ6Nfo3PXP0sk0f0Itrp2EN_yY6_s7D4jHiDkZ77inSpWwYXch-c1YzxFNha04_cvphBoXcWHLbiT5ZCFbOsUxYVLNh7mrtjk1q6MPMxTITv5Hw6GCXK9ahcWWWEG4qSvB9ckSTYKp6FDYi9IeHEulqgHkg8MjzpROchG3Ei0Mf4obljYLJKwKhesbgThx1IML6S_fXshFHBKD9u77Id8xraVwf5HkQY2-ZOnrQpZxTtr1YUL7HOZsFr-FGcIgcimW97fpB69nCv3EVkEc_7M9utBhisMd-Vt7RHsAW0HuWFiyGC3_P0yPKYmUspxMOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=fBoLaAznZdMq0mdWBPocGWH7YOtAC0pOaeuRlPudoB3Gnz_qxF9uO7YUzxjtNvsTdgom5ju9obZjj_tjpBKYGNtPOx2g0ldTWpuGvH-yCrJl7RW8myoNG-FrljaC5S78wlBd6qs4_b26Ac395BBk6Yb5H1p7Nyi9fvlWykYuJuQ03bnK3igpreVC9tTgb45LNcKHpNPxRLMyaUF2ZSoz5yV4IXV-vq_kLL9_EfkWwi2Iwwjn7hDS5aOa6db_UAA4Y2RALVyMxdiIth0R-2KXl6J-AqNsubbVFe-u8sJWlcFEPiZabrBFtToafLNjgKAN2J8FRhdkGpsyujAT5rNung" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=fBoLaAznZdMq0mdWBPocGWH7YOtAC0pOaeuRlPudoB3Gnz_qxF9uO7YUzxjtNvsTdgom5ju9obZjj_tjpBKYGNtPOx2g0ldTWpuGvH-yCrJl7RW8myoNG-FrljaC5S78wlBd6qs4_b26Ac395BBk6Yb5H1p7Nyi9fvlWykYuJuQ03bnK3igpreVC9tTgb45LNcKHpNPxRLMyaUF2ZSoz5yV4IXV-vq_kLL9_EfkWwi2Iwwjn7hDS5aOa6db_UAA4Y2RALVyMxdiIth0R-2KXl6J-AqNsubbVFe-u8sJWlcFEPiZabrBFtToafLNjgKAN2J8FRhdkGpsyujAT5rNung" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=K0ezL-TV0f_7Flaora51X5hv-OG4ZtbNp8ss244jsSeYjVFHjlu6BsWHimrN3xUQNPbDdVGOQy0VgcwzAfV_M_BzhiZw78vGuYEBCRcoBUbgfENPc8fatUWEJNWYiUBYlVYQlcR-VFXtKI_KzrAh5HYZqtJqLHGnGZvvRduS79SSYwl6kEJFHU2JPmCa2QsU65ms1etZ_bd6d09ZD1O6tRu1m0bw8rEjg3InUePdrUfbT1KU2L_U0fNVHXz5e0m_f4o03uoUxYzc0AuRWntYPHn88w0GchRgzMib-oRNj6IYVBf3GBy41URyAjOnEl__wi5aA6aqp31PLxeqa7DEpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=K0ezL-TV0f_7Flaora51X5hv-OG4ZtbNp8ss244jsSeYjVFHjlu6BsWHimrN3xUQNPbDdVGOQy0VgcwzAfV_M_BzhiZw78vGuYEBCRcoBUbgfENPc8fatUWEJNWYiUBYlVYQlcR-VFXtKI_KzrAh5HYZqtJqLHGnGZvvRduS79SSYwl6kEJFHU2JPmCa2QsU65ms1etZ_bd6d09ZD1O6tRu1m0bw8rEjg3InUePdrUfbT1KU2L_U0fNVHXz5e0m_f4o03uoUxYzc0AuRWntYPHn88w0GchRgzMib-oRNj6IYVBf3GBy41URyAjOnEl__wi5aA6aqp31PLxeqa7DEpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=sUK907SuXdlevdGdaMJPWnjEcNc_psw2qmPSNp6XjjawCL_f89mCuRi91L7igE8oSxB9nlcXWl7ymPxjy0-XrlPF5sFOBzxSZzxxYG0WkplJDlM2rCRJfdlTvOPof0KM1TQ8H92WiIjOGdOfb9ocwM6EZZ7e5JEcguehGG0u3AB9AOtTZAL-fZcPTAxaAAwTFdfL6Tac7r3TP6olCijCY9FL83hyUSTjB416XC3rP8oXdjoiGQpKDgha2cwapMJdvrDKA8LoPxxVT1q-XfaWqPkzjglLEjVdhqt78FYi5LWZFYH7bFCE2Yz8wEkGpH38UZyXrU2tjijJyPu0mmCjjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=sUK907SuXdlevdGdaMJPWnjEcNc_psw2qmPSNp6XjjawCL_f89mCuRi91L7igE8oSxB9nlcXWl7ymPxjy0-XrlPF5sFOBzxSZzxxYG0WkplJDlM2rCRJfdlTvOPof0KM1TQ8H92WiIjOGdOfb9ocwM6EZZ7e5JEcguehGG0u3AB9AOtTZAL-fZcPTAxaAAwTFdfL6Tac7r3TP6olCijCY9FL83hyUSTjB416XC3rP8oXdjoiGQpKDgha2cwapMJdvrDKA8LoPxxVT1q-XfaWqPkzjglLEjVdhqt78FYi5LWZFYH7bFCE2Yz8wEkGpH38UZyXrU2tjijJyPu0mmCjjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=mwGjp7NdjsghdK7E8jt_6MvXUpUg0uRuGtOjxrSo3E7iPaTh6A8vPYYf6z6Huw82vdYRDlpJIT83ZTYL3pScYOBMX8zyDrfxSCrVGSN8JMaHaY3WXcYY9ev0CklPt3Ei8akxVKjRrPg4M6OYANx06j7aIMisXCrgbpMTAmsn9KMZYg9C1s2Uq_n3JlQLG9aeyqIF5Gb_gr5Fsiksz0XzWvGLaLro-_Pf8pmXv9DabsbVMPSkS5EnHH7zKCpAuyZY9ivdsErhcZ5Xgo5hKvdo0kK1W6pnC8nIPYzQ2KJrZKpxlLBpRSS0DSWgCwbDDm0BvhRfLlpDSYr1PBkYe1pq3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=mwGjp7NdjsghdK7E8jt_6MvXUpUg0uRuGtOjxrSo3E7iPaTh6A8vPYYf6z6Huw82vdYRDlpJIT83ZTYL3pScYOBMX8zyDrfxSCrVGSN8JMaHaY3WXcYY9ev0CklPt3Ei8akxVKjRrPg4M6OYANx06j7aIMisXCrgbpMTAmsn9KMZYg9C1s2Uq_n3JlQLG9aeyqIF5Gb_gr5Fsiksz0XzWvGLaLro-_Pf8pmXv9DabsbVMPSkS5EnHH7zKCpAuyZY9ivdsErhcZ5Xgo5hKvdo0kK1W6pnC8nIPYzQ2KJrZKpxlLBpRSS0DSWgCwbDDm0BvhRfLlpDSYr1PBkYe1pq3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=dw8OEX9Kx5VQYgG_hcdypFbpxJPx5chuzUYWOTyaJd6_qnZRWftrOowRywaJoCVMUf9utMFAikijPEqROqgfx4-jRdBK2cTmX-Dr08dqJMiK9Dgi2Tl5Gb5_lbb7xWe-Iy4-YOJC9lGQJXtSD231h-iJljInRKKQ8a_5zO9jzVQetb9MbMv76kvhhXskjC0o2FpVB_B3abeVlHMowFtktqNqSGrDisMAY0MSaHtgrmbKl_ZDVLM30L-L5PqDbrRh6iXWsY2vWluOAvwZl0zJBDw1rmXrRS15UGWbEdM2Szrc0ZpitHlLOYV6k-kBjFTTMBBM2-voaZNKXtXiUjO_Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=dw8OEX9Kx5VQYgG_hcdypFbpxJPx5chuzUYWOTyaJd6_qnZRWftrOowRywaJoCVMUf9utMFAikijPEqROqgfx4-jRdBK2cTmX-Dr08dqJMiK9Dgi2Tl5Gb5_lbb7xWe-Iy4-YOJC9lGQJXtSD231h-iJljInRKKQ8a_5zO9jzVQetb9MbMv76kvhhXskjC0o2FpVB_B3abeVlHMowFtktqNqSGrDisMAY0MSaHtgrmbKl_ZDVLM30L-L5PqDbrRh6iXWsY2vWluOAvwZl0zJBDw1rmXrRS15UGWbEdM2Szrc0ZpitHlLOYV6k-kBjFTTMBBM2-voaZNKXtXiUjO_Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWR_zOOHTqIkovuZsTDO-8g4fp8Fas5hyYPCQ0e_QvUmppOvcOSyhgz8iyXGoP9pWMJzd4sCR-oZBEJZ0SZQwyChaG7p6GYf-VId8iCnyqhzSjRNZrDcXL0Qzema28MkwnB67u8BRnKMflW_VMm3f9YrqRjm5YEmqb_ci6t5i2WgGVWtUyXBnzQsNxwF9Qy8IaZsGXmNS-kCspLaAzpwyOffT3uWmANxLYXspVB41-UDPJ03vPtk8TzhHR6aSHuqA4q-E4c--voMBWuj4halsqkGFzQxuNkUdkSz8lF0fhC4WTpHV4iw48SgS73CNWqGtyvRWNGy6QHLta-Cu8PSbw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=sj8bQH9o7V3ggHdVDsrNDF__a7fDJzVpq21WQN7CCUh5doeRQYB3Dc0doPbH4iYzi3GD8QvSBiZ7-3oGxBuCwj9IZjz4VvmKhOHo60_ne98WRGjEwcT5dTj2zIXbpQyQ2k-W-m9WIz1eaJGp9tKtorTP2EiuBKLAtI4ZHFEOUQxBBQIRs5i67dhhc_xlFHSHvdKUVktLKPvSngufBQR5G1p2pjkSKKqOCdtIscWai99y9UrWw8l7j4Abfehn84NBRHuTiODVfLTWpY5RJuDcEe63TCS1rrlqElEy2s8ix1vyYFcBuadMUXV3wbulWCadryo5DAIkV60nZlfeN_Oq6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=sj8bQH9o7V3ggHdVDsrNDF__a7fDJzVpq21WQN7CCUh5doeRQYB3Dc0doPbH4iYzi3GD8QvSBiZ7-3oGxBuCwj9IZjz4VvmKhOHo60_ne98WRGjEwcT5dTj2zIXbpQyQ2k-W-m9WIz1eaJGp9tKtorTP2EiuBKLAtI4ZHFEOUQxBBQIRs5i67dhhc_xlFHSHvdKUVktLKPvSngufBQR5G1p2pjkSKKqOCdtIscWai99y9UrWw8l7j4Abfehn84NBRHuTiODVfLTWpY5RJuDcEe63TCS1rrlqElEy2s8ix1vyYFcBuadMUXV3wbulWCadryo5DAIkV60nZlfeN_Oq6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=amMumIkxR7m2ugJqmN-ClE25xsJDqy9iZyTR7SkXVLI1Znb-ZVf1fEYTNYJ1ogI6jE3O3duPgT9ee7EAT9Qglgy9jhUX7ssEXSKF6imz_UJK0ewvEZmnpHa3lglBEj9n4xiJ6eafX1h3HJ-X8hDOzCf9rcbJI_HHpUavG1yyxiEZ8uqKS4mYjWRtX9MDceI3azWBMaqrfgz5yvOodvpRAFRkkemACKWcHalsHZKuZcUtUf9nmxlWAZZa6Z22l5cwA7eduIugd2cePvlpY677yjZ78oVYxeeMZpGLiwVI6cAaxz-P8jITI9Lqb0pgs8VvOkisaPxtWEG3BMyQlDNOrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=amMumIkxR7m2ugJqmN-ClE25xsJDqy9iZyTR7SkXVLI1Znb-ZVf1fEYTNYJ1ogI6jE3O3duPgT9ee7EAT9Qglgy9jhUX7ssEXSKF6imz_UJK0ewvEZmnpHa3lglBEj9n4xiJ6eafX1h3HJ-X8hDOzCf9rcbJI_HHpUavG1yyxiEZ8uqKS4mYjWRtX9MDceI3azWBMaqrfgz5yvOodvpRAFRkkemACKWcHalsHZKuZcUtUf9nmxlWAZZa6Z22l5cwA7eduIugd2cePvlpY677yjZ78oVYxeeMZpGLiwVI6cAaxz-P8jITI9Lqb0pgs8VvOkisaPxtWEG3BMyQlDNOrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=u1whUMckQ5HJKWF5QqGVr3RroqGH3YR-PucVOHmr4Nry2Hj5BGpzSP7HwlJ71ZEkCnMHzihigf34FuYXmqgj6JdrfK5NxZmvTYc3uB1xI5ZVP9UaxCrnPjiWjIrSHLhn3O_x15m4Mt95s4eJzieYsG_bqh2dcg8qrtg4XUquXvadbSdqzwtJeb4g06KKH55J7UPfw02bYBAr2slzNP_RojCtZl1bFMpi-p84gD0MsDTfyYtyHe56A1V3RbL8Z3g-C7aA_Sr15_ETcwiSzw3e5OeP9r7Zvfwm3w31TtP9JV2DpfPMkD1fEkm7vqR1PgYKnSPV01SiKSYm_MHQ0A-HAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=u1whUMckQ5HJKWF5QqGVr3RroqGH3YR-PucVOHmr4Nry2Hj5BGpzSP7HwlJ71ZEkCnMHzihigf34FuYXmqgj6JdrfK5NxZmvTYc3uB1xI5ZVP9UaxCrnPjiWjIrSHLhn3O_x15m4Mt95s4eJzieYsG_bqh2dcg8qrtg4XUquXvadbSdqzwtJeb4g06KKH55J7UPfw02bYBAr2slzNP_RojCtZl1bFMpi-p84gD0MsDTfyYtyHe56A1V3RbL8Z3g-C7aA_Sr15_ETcwiSzw3e5OeP9r7Zvfwm3w31TtP9JV2DpfPMkD1fEkm7vqR1PgYKnSPV01SiKSYm_MHQ0A-HAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=VunWKBAidclrL4Y0WQM7mgYNbuOz45F3kxLk7cVjNY_3Vu0K87AsI2QlztpuC6k76g9hmeBqd7nHuiKOCsPEBZIWlJEfleAGEm254KLYdDrj3k9yIqsOkMNlnr6P3TcNgf7cpMpx_jNuVwroowh89XOp-tGBnbOHOPPLAVGIBb_16TBUfz25HVnkGd5PBldiB3cp-gisFjauzrEbGo98uOFWTCYHm5e1x8RXb6vEH-w6ta51prgPvJyuhK5x0AHffgbSRqkExZWg8jfLAYjfHttbHRgM46_ClY3pGj_U9-P7mJa5UWlkjZ0wqlgWz0bjj9RYBZSCFCAT1E6mjZrJcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=VunWKBAidclrL4Y0WQM7mgYNbuOz45F3kxLk7cVjNY_3Vu0K87AsI2QlztpuC6k76g9hmeBqd7nHuiKOCsPEBZIWlJEfleAGEm254KLYdDrj3k9yIqsOkMNlnr6P3TcNgf7cpMpx_jNuVwroowh89XOp-tGBnbOHOPPLAVGIBb_16TBUfz25HVnkGd5PBldiB3cp-gisFjauzrEbGo98uOFWTCYHm5e1x8RXb6vEH-w6ta51prgPvJyuhK5x0AHffgbSRqkExZWg8jfLAYjfHttbHRgM46_ClY3pGj_U9-P7mJa5UWlkjZ0wqlgWz0bjj9RYBZSCFCAT1E6mjZrJcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZGKRc0hmiAchdskQwj0vxJCT9YtihQF9R5OD5HJH6oXEscv7jj9DFiVYwuolvYbhKSovg3hl3h-J-JMInBEqIYxP29SUZFVNC1c-3ctunitTtbjjDGkGY6RNmba1antbJMBEBf81skMCpeaR5IBiO5TXJ3-RFSp9yBOyg5nPjfqSC4-qNvFeo1VIquCNoE-UyVn4iVMnPxoyyImXHrUzZDhLFslQ_agrqMhh6A0-eWH2tMQS4Vp62noi_pbYk4nkhtioWXl-KzjqBn1YN4ebYwUEKLjs_9Hy1j99IddsCEsRh78gDku6pBSZuwd8xWe4rDGmIKVds3mCfQGwHCrsg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=B50vtt8w4Meqeqs-OcxHwtEz5p_VNY__B8uC5JztowwLGoIIswv8g-33hE4Y-fKHpbU4v8_kd5Ghgdv0R7F4y-Ox0pF0vrvMWE3iaaAm7TOvW_3oB0SeB3d4JipAptP5sBn_F1zjYlYz1rh405uQFKLrfOI003aorMp6vzcDvxfKpvrucQG7usdWBqFchXSF7gHzKXEHt_NeWP_ckjihhdqkNbgD2yWZt9f2NpCdcjCp1rVWCDWwqhKaMrrACbwXxd_En3Wu9TooQZXdQzbs9Kt_5C9nH30sX2LvADaxdwZ4w4tBnZWU4XKo5iIA2Mg8noNPPAVJDfg9x0fcic_Rp4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=B50vtt8w4Meqeqs-OcxHwtEz5p_VNY__B8uC5JztowwLGoIIswv8g-33hE4Y-fKHpbU4v8_kd5Ghgdv0R7F4y-Ox0pF0vrvMWE3iaaAm7TOvW_3oB0SeB3d4JipAptP5sBn_F1zjYlYz1rh405uQFKLrfOI003aorMp6vzcDvxfKpvrucQG7usdWBqFchXSF7gHzKXEHt_NeWP_ckjihhdqkNbgD2yWZt9f2NpCdcjCp1rVWCDWwqhKaMrrACbwXxd_En3Wu9TooQZXdQzbs9Kt_5C9nH30sX2LvADaxdwZ4w4tBnZWU4XKo5iIA2Mg8noNPPAVJDfg9x0fcic_Rp4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=b-yptel4bnqY3hdHJufoqHhaT1KZtB19DaNXTAIcpCCjLda65SZvbaqfkK0C7k_kzUj00dSpIndlW_Zq85joqcWxfGvuXLKaCA4WCh_Urc4Kcd2ybJ_fvsKsnkTlTbgYPrJjiZQHrtOsu-D5TNgpTw55a2hF43ONV6XczGxAZxMAW1FvaqRX4PfjYCHBYN3t8ijODikt-ON7jJk-kGmoCfORzNvXRGFi-MXDGAMCBXwcWKwj-nUi_cYClFg9UbEQLsbRsc6UTZUbCDi4WBtNjBN8b_qkO9t8cir4Jz5p8MV9c-nbnh4tHgfVgXlusgZkaSmaKEUsdFQry0U2GpeKfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=b-yptel4bnqY3hdHJufoqHhaT1KZtB19DaNXTAIcpCCjLda65SZvbaqfkK0C7k_kzUj00dSpIndlW_Zq85joqcWxfGvuXLKaCA4WCh_Urc4Kcd2ybJ_fvsKsnkTlTbgYPrJjiZQHrtOsu-D5TNgpTw55a2hF43ONV6XczGxAZxMAW1FvaqRX4PfjYCHBYN3t8ijODikt-ON7jJk-kGmoCfORzNvXRGFi-MXDGAMCBXwcWKwj-nUi_cYClFg9UbEQLsbRsc6UTZUbCDi4WBtNjBN8b_qkO9t8cir4Jz5p8MV9c-nbnh4tHgfVgXlusgZkaSmaKEUsdFQry0U2GpeKfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JEMmy4reaZVWSkfzk_8zbsrD-mpGTJGfqtr4CZ0L6y8np-pZnDS5NVM8-j8DeiyOmJCYQlR2eH9TLGFD3Nwfu0-wHQb-AE7NKJKfXRFKdvpNcIddaghSzC0AQNMfIDyK4uBmIh7PiAcp3HaipzdDcG1_DGMF1WKpue5oFiCMVfGOkpZTTZV7lnyTevtMXhOkFiwoYhxvorI7rt-YPBQgk-DYoCTwy26WJFH-0hiy-iIGn2gn1wBf-2CHL98bsCljKepuZ-iSZTSR-WLXYBHIw0JKvfHTI4HkgPdEDjOvAsHw8QRTXIKmc_1Svs8TgiwFRTmNY5R8Gq6JIsCpVpi6bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cicGhX27l8ycayQSex0pThC7QaWAns1iwrwSEwYFUhsSL3d9txkeRjtlJaxfrIh0Eyz2ZfgddJJIBNbFjaghXTgNyHTYxfjQnrMm2tCvVWzanYstwHcIOBt0GH4GBdjU7utju1LaVVuwlbdaysCrzip92gXbV7Tyt6Ixa6ELX9ggSng5ciHIjHpBNZZHgqAWnUawqaCmxL__8Jy9rEiBSrfr774ReqDfOffiXw2lACtWdUNgzIJ5fS9fAoq60lN8aGK06ERs9rQ9_xrMd9a4UWIxPTXGoBPUugygb1fSX6bduQHzQ4zEjgUWXZOA3I48saF50G8iD86M6-SFhtNbfA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=DnUP1yS89k3tDE0LNruExb8FdNboLbnOu20e2N5OU5mwEwh-zaYL9RNT9su3QdNEVtNFgm29Cmm8F-HP_colU4RHpS9wq6gC88gwIchPYmJw7VCMlSg4ZjVNy_mKg-Vs8JpA2knXBAs7EzRN7nYvg2y4tFCHHEGH3EyOfArgYCscLUMpqQlunO87vQGc3ytpjkF_VEwNbrwR2IDdvaZP1ioutiu2Psd8OL7hup9Uc3T8y_JRbZszHDHe83KGJsM4Q3wuHWUv9d2hxKPjUSiPDNT2vkEVb1U4zW3X-BSawbK0WHaibefFNoHuF0NADZSjc1bBPTHVgbuzgPd6YHnlpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=DnUP1yS89k3tDE0LNruExb8FdNboLbnOu20e2N5OU5mwEwh-zaYL9RNT9su3QdNEVtNFgm29Cmm8F-HP_colU4RHpS9wq6gC88gwIchPYmJw7VCMlSg4ZjVNy_mKg-Vs8JpA2knXBAs7EzRN7nYvg2y4tFCHHEGH3EyOfArgYCscLUMpqQlunO87vQGc3ytpjkF_VEwNbrwR2IDdvaZP1ioutiu2Psd8OL7hup9Uc3T8y_JRbZszHDHe83KGJsM4Q3wuHWUv9d2hxKPjUSiPDNT2vkEVb1U4zW3X-BSawbK0WHaibefFNoHuF0NADZSjc1bBPTHVgbuzgPd6YHnlpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEWF7-60gt_uio3zn4mRcMuF9sV_UjYQL3fj17lQKrC9zfOLWUiE2iGTfByJq5FAk8v2ATJGVw02wKrdomgGrJrUU_u2zvrNH6XQiuXgg5M1c_k7N5by-GuXx_QCeQgbBQ6Fe2_DpRzb3fD1r9eSO19VGH6RccPf-RG2pvBOoCb98wC9rKC5WxeB9PSELLBB2ro9Lq_0o8OnjB4uCrreO1FDm4Hf-B3LnBIQUatxrqkm_lasgXl2StMLALfNqUAwhnYxMZnCdTO1tw1g8dorR7QOwon8uJnVfw8W-WIZiEoC9U_h1NHvB_TrtMdjx9979llpFeoWS-mnLrcip-8Kig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cb1yW-5gT5SawmJ6wnNeGjldC4DJjVmRBSoRuZcNnor8vBk5AaYSpQqOZQEoDE55zn8nOSVaP0kJLC7ZlX-G3Zjpv-8hQfEm67P6zylT1R1M2rhtqmX7PPKOlJ8KCDw0aVrnFGsT96-lLL2TLrctrAAcguB5hWj2mXMb3fItWdJ_ECGWBe_rgO4xztS9pvYQSS0TOcQX9JxiXnjr2sHe8A0B17N6FVUASDeaGFfcIS1m4T3yO2h_2CMFbTUpqfnhOPS1udSCTHftbNep4fJUEgOQJGEtE6F2yIkm2naPp66Au67jHCspqC6wzHaYoq23zYHMhPJUvNt08uytK2-59g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1kY-Tww0DrMAP3aDJ3N8qAzz2JdDxzaqJJkBcSKSAiq50BvgA9jO_ScdfEQuNzCM21asokk5jMWa1rRg7Ky0xcylUiZPLLljiaefRz-uFr_xXN3ciubWF2njlWIBmszGvEEKQYsGKK7eOr62h9xBTukGAwKXme8fhe11SrMwx1ScwVufm4acA-yPMgEFumW9Mrdl6bh85M2Zck0C-_QsS6yntP0E9D9YgssSGuVAILMPW3VElzLqBVSn66fYrEWzphwvOCmMzP8Vbg4kzyxFgwvSnLmjqVogNexoERr4RMeikdzp7TmllYIURMZKRKOiSq4kC2o9hCghYRNuXUO4g.jpg" alt="photo" loading="lazy"/></div>
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

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
<img src="https://cdn4.telesco.pe/file/NHHJfyRGJ8Abw4zYKd-7kQtVdMe6pRwiOCrMKOt-VSkYrgGT5mR6XI25aLo3chNfD8zJS06cCHVGV79Hzx8bPlqI0zu7TJUaR2kL5ZxK2pR3GYVjWnAjRqdu7yz76Q8xdfsK8HraLLK1cmVx9Y-wbU0O6lfpYFZcUDrA438AL4efGnzan2_GnEaBa_lHg-WamVsoa1y1LJgB4KnRAvrxqKFDKDYIhCvzRbcep6ZlLPKVZmd-0Lv8M6_Cyc1-wUZKxAvmxly0KALJY0Jzwz2Llb8UKzSh9nAY_YFc0cA1Ps3USNq3ozocoUIB9dXauUR5kLPhO-mdKh8AAashQjFv8w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 09:45:22</div>
<hr>

<div class="tg-post" id="msg-465625">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd9f4785c.mp4?token=GYO8KXGaI7192ukAZlPMeREfNuohPZyqLtqcMQrY2zYDESrCT1S0dW0DA3nLKm2yEhfYC7Gic_PNIEOVv6EXlAz5Vr04GZHRwmDzv_qVDxT0D3KAhjTZReQRQeA8DlRVYHKq52d6L84dEQzMvAU5uLl_1wW6hw-mkrlzCGXu8bQkfRM_B0WIFQI9ofA9ZIibew0Gp0eupO0nUKro-RyCpD0qbnY0NYXvvPnR1j5oCRcL3Ua8pwSmaggRtvp2fXilh6mBO21N6HyAxhPlWBwUNdFviEzadVUaiJLOPzFpU5R5gEb8cw3lWuTEU3lqU0MAqqJn4H_NO6tdZVnRvaKmcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd9f4785c.mp4?token=GYO8KXGaI7192ukAZlPMeREfNuohPZyqLtqcMQrY2zYDESrCT1S0dW0DA3nLKm2yEhfYC7Gic_PNIEOVv6EXlAz5Vr04GZHRwmDzv_qVDxT0D3KAhjTZReQRQeA8DlRVYHKq52d6L84dEQzMvAU5uLl_1wW6hw-mkrlzCGXu8bQkfRM_B0WIFQI9ofA9ZIibew0Gp0eupO0nUKro-RyCpD0qbnY0NYXvvPnR1j5oCRcL3Ua8pwSmaggRtvp2fXilh6mBO21N6HyAxhPlWBwUNdFviEzadVUaiJLOPzFpU5R5gEb8cw3lWuTEU3lqU0MAqqJn4H_NO6tdZVnRvaKmcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رزمایش جان‌فدایان با حضور پرشور مردم زنجان آغاز شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/465625" target="_blank">📅 09:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465624">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isfC4gGpq_GsnblWRmpnBfl-eCtG51FLrKIZlNhCiYStThCAR5dJfuXBMoPy5LurtW7ic7If9LrGUcHrssH1Qbhlz5KWflYeoXs6uRoEhzhF65dZjpPxT7CIku1q9UnNclJ6bbKr2bdKyWFdHK-3JdE0361dtRoaB743vHG_r2GJy4h7m2gKTggISCFPR6P5eY9wlhr4nxk2Eg8IvfOphe_OiDGmNZhESNgu9Z_Hn2xvYxkQdIX5I0SaR9vIhQ96sBoNMdlDdAsuDPpZm7-oDwtC0qIubO6wkHBcGwvZBOOl5jXuqXYib5WLnR-bj9rjDAwQkZNiPdh4PSpQ974sfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصلاح‌طلبان بیش‌تر از ترامپ نگران بسته‌بودن تنگۀ هرمز
🔹
خلاصۀ یک‌خطی نتیجه ۹ ماه جنگ ازاین‌قرار است: تنگۀ هرمز بسته شده، قیمت نفت زیاد شده، فشار به آمریکایی‌ها بالا رفته و ترامپ شکست خورده است.
🔹
تمام تلاش‌های آمریکا از فردای جنگ تاکنون، به‌جای براندازی در…</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/farsna/465624" target="_blank">📅 09:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465622">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K801MzYMj6Z4p1ufYyPUuvcMga0JXlPMCAAr1j8jTVIZQqyVXG_Iysl3GZdQ7vdz_iAycaJ5DDGkclCVGZ7RsHJLbXoxdNOCNEvFe4wmKjHCbJDH4F4B9LjvHJ-vPwbYc_ZQUWFVp_8cgfny1AI1qGLRA3Pz9v3JuEfBUAoJG0gfAvhH2PpIEupEUmuUpYYACQv1M6l4uaztzwZa-RTalser0cXY7s61v7PQ_ql-e-dNHdgbWXYqetllaymNap9cP8YNDabeUcdRFpJTUzzlrEDlRR9mFgZRc2lkfvTvIL4eklG7ve9P0sczzjlKeMG51hw-CgecJAS-ocnstFO5QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار جنجالی درباره کی‌یف: «شهر را ترک کنید»
🔹
اولگ سوسکین، مشاور سابق رئیس‌جمهور اسبق اوکراین، با هشدار درباره تضعیف شدید پدافند هوایی کی‌یف، از ساکنان پایتخت این کشور خواست هرچه سریع‌تر شهر را ترک کنند.
🔹
به گزارش ریانووستی، سوسکین در برنامه‌ای در کانال یوتیوب خود گفت: «دیگر کار تمام است؛ کی‌یف محکوم به نابودی است. دفاعی که قرار بود طی این سال‌ها برای شهر ایجاد شود، کاملاً از بین رفته است. همه‌چیز را غارت کرده‌اند و دیگر پولی برای پدافند هوایی وجود ندارد.»
🔹
وی با اشاره به آنچه «بی‌کفایتی زلنسکی» خواند، وضعیت کی‌یف را بسیار نگران‌کننده توصیف کرد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/farsna/465622" target="_blank">📅 08:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465621">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">‎⁨پیام_رهبر_انقلاب_اسلامی_به_سی‌وسومین_اجلاس_سراسری_نماز⁩.pdf</div>
  <div class="tg-doc-extra">527 KB</div>
</div>
<a href="https://t.me/farsna/465621" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎥
قرائت پیام رهبر انقلاب به اجلاس سراسری نماز در حرم رضوی  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/farsna/465621" target="_blank">📅 08:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465620">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eee080bf40.mp4?token=V7RCTObGtYHi48eg2hh5eHQ3mYSXylEDNni2g22bWwFNfheo-rSqRA75bOyM2QA8YusMysZJa22L5qMaHhMhexhVN0x7tdnFdX-RElJYh-mi-zrsepw0WfMH0Q0mWBisZWNvxXlL0kIfNb5OoqqybKe7NRod7avUL_Qi1i-uHT7Ehg-FqrAOysgjYTtxaW3mMHJs--nm50zv7QiqX2pCJhO-TvGX8oEXvu1OxlztPwtoLItwr-TSR60lwJVazokUtZ6gizxJr6Jni_WGM2wuZSoxwlzoPeNQEF5VbA8NtZDAyuwqnD-sjaYjyMHmdURflp7Pb8W84YUes59yU9_7Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eee080bf40.mp4?token=V7RCTObGtYHi48eg2hh5eHQ3mYSXylEDNni2g22bWwFNfheo-rSqRA75bOyM2QA8YusMysZJa22L5qMaHhMhexhVN0x7tdnFdX-RElJYh-mi-zrsepw0WfMH0Q0mWBisZWNvxXlL0kIfNb5OoqqybKe7NRod7avUL_Qi1i-uHT7Ehg-FqrAOysgjYTtxaW3mMHJs--nm50zv7QiqX2pCJhO-TvGX8oEXvu1OxlztPwtoLItwr-TSR60lwJVazokUtZ6gizxJr6Jni_WGM2wuZSoxwlzoPeNQEF5VbA8NtZDAyuwqnD-sjaYjyMHmdURflp7Pb8W84YUes59yU9_7Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رهبر انقلاب: رهبر شهید اهتمام ویژه به امر والای اقامهٔ نماز داشتند
🔹
توجّه به امر والای «اقامهٔ نماز» و به‌صورت خاص برگزاری اجلاس نماز، از جمله اقدامات ضروری و بایسته‌ای است که از ابتدای دههٔ هفتاد در کشور به همّت عالِم مجاهد و مردمی، استاد قرآن و مبلّغ زبردست…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/farsna/465620" target="_blank">📅 08:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465619">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رهبر انقلاب: نهادینه و همگانی‌شدن نماز در جامعه، زمینه‌ساز رسیدن جامعهٔ اسلامی است
🔹
اقامهٔ نماز در همهٔ مراحل تکمیلی و سطوح تکاملی‌اش در پهنهٔ جامعه و کشوری که پرچم اسلام ناب محمّدی صلّی‌الله‌علیه‌و‌آله‌وسلّم را برافراشته و به حاکمیّت اسلام مفتخر شده، در…</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/farsna/465619" target="_blank">📅 08:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465615">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oys-UOn5Hv33VIi5V60uwikzdV16J9DLpfqcpPBu06slr_CkocuL7wDkv-oJl7dModuAJPaO5GysVCYYR8YjIuRGo5eoxAddgij-fb_5YUdPWgTHcx6wGKaQwJDh-Fvtw7sU56uzIRzmiwUb0JdRbeB83YeUazFgQwMXKFOrYuOc3gY4Iuz2-6_z3J5P3phsCL1KgFcvfV_4F71FpXaAVsg8kslcZ3J1LZQdrdgNYV5s8FFfz7by75c3nr7TQfsDEXGk3Cx3GhGhrwxTvCY_yMYdr42Ffmx5PSMI4pXzH-1IjfUqbVicn7kyDkrNVYKGTXQQhIwtLOMxVvOb1whPuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر انقلاب: اقامه نماز در جامعه زمینه‌ساز رسیدن به جامعه و تمدن اسلامی است
🔹
اقامهٔ نماز در همهٔ مراحل تکمیلی و سطوح تکاملی‌اش... برای فراهم شدن زمینهٔ طیّ طریق از مرحلهٔ نهضت و انقلاب اسلامی تا مرحلهٔ جامعهٔ اسلامی، امری ضروری است و بعد از آن است که نِیل…</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/farsna/465615" target="_blank">📅 08:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465614">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0MEJpQcndAPujWWy6I3W_KfYQPB1lczokZsDiSB65-QRRN-dwZ6uPbNZh1LBAo_g8ZrYbrt4cQBoTPqJWzx342AWDn4P8JXWcDRnd8mQcQp_xeiTtnAvNFHx5ec5QVCVd7dWom8dj_YYPCg33lFUe39iHA3A64nVyveR6WvHG5xRVSOvkoZIO8KjvxkdZ9Z_IZTnOS-R5tFkuytKUpkxmUSBoJDYvtzOxfrfcXLPL3qOnldpUxwbJ8cSKv2Cs4uG95Sf1DnQd1IIiLkI7K9_5TNFYua0Ze3UWlvuBxq3al3syjgUD2c_lAi8taxEd72lGGLpgjS8BMAgRGjV2TXNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر انقلاب: اقامهٔ نماز اولین ثمره و نشانهٔ حکومت صالحان است و در جهاد و فتح ظفر نقش دارد
🔹
فریضهٔ نماز، تنها یک تکلیف فردی نیست و بنا بر آموزهٔ قرآن، برپاداشتن نماز، اوّلین ثمره و نشانهٔ حکومت صالحان است که «اَلّذینَ اِنْ مَکَّنّاهُم فی الأرضِ اَقاموا الصَّلاة».…</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/farsna/465614" target="_blank">📅 08:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465613">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7zTsHopjGDTAe8DK8wyl50NjgCt-pwb0zPvSEejAbOCBWLzHSYVv2WLB3XPYg3ZDkElgXTcak8TEyEt3UKAWGsIQ0lBtYWtlA5e9-bw5sOYlSfqa4RhAno2ijJsbj92RDzx8s2lmFwtiTZKfMhqo0moVz6Yz2VhI8WydHIlS8i9Ya_GGt0PJOdH6dqCMB0-AKgHBaAKuhnvcJsZ8kz4XaZyMvpmuAzGHidji9BIv4_AaqjOiBbTtst3wYVb5Hxk6tTVNuglN8xjoDj2UDIFxXx4SC5QQOotYqzlygucpjKRoQSEmoc0vXO7Cbv95sB6aguHkMdDk2sRMqEsWwj0-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر انقلاب: نماز تکیه‌گاه مستحکم امید و اعتماد به خدا است
🔹
اقامهٔ نماز به‌عنوان تکیه‌گاه مستحکم ذکر خدا و امید و اعتماد به او، نقش ویژه‌ای در جهاد و فتح و ظفر در میدان‌های مبارزه خصوصاً میدان مبارزه‌ای که امروز پیش روی ملّت ایران است، دارد. @Farsna</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/farsna/465613" target="_blank">📅 08:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465612">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CinEN15stRjDzMC2NgW1_rs6McIlH57OcDKauUa8X1EdDzIekfYJ7XMzD6WD4mwkeOtCgkrrVtsldOIrhJZ2H1jWw3uWBvqyeClnMyKJ22e6lAaFiDS2TGwbZB5v0RpHwTd6H8rsNnilytmdyHVX2AMaGRdZDUJa1eYnrs30leCuDzcFRI6YYaf-Y73l0wnVCxQuvcvnqLO4n-gX-dWYMczl6OZJA5XD7EHLks1-DKRYQ7Kuscfc2pS5tUDNoPvDW9Q25xsaiJA9KREI1p9s5B_l4vUntH5_RGNB4DKwNi15aI0a5sZMXjzxpE1CHphhpsJ_0l1L4o1ebTjfw8gHcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر انقلاب: نماز رکن حیات طیبه و پشتوانهٔ مستحکم مبارزه با شیاطین است
🔹
بخشی از پیام رهبر انقلاب اسلامی به سی‌وسومین اجلاس سراسری نماز: نماز از جمله زیباترین نعمت‌های بزرگ حضرت حق جلّ‌وعلا، برترین نهاد و نماد و ستون دین، رشتهٔ اتّصال هر یک از ما برای ارتباط…</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/farsna/465612" target="_blank">📅 08:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465611">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m93Vs3Umid7aSkenq2okkLhTvuM5iAz_NmJyImKnS-AjJVxzKb-FOknO0bLPX9a2_61tGkxu7uW4FFFmzVEpmQg241TjayHgAWHXsMzoLf88AvTuFoCS5eBcDqpyr_qaUogV80FRV1tps12wSJP7h7VyDohfMMVfTSquAn5EjPx6mKdppEt-a9TXs192boJUXCCCQbTJUrDDsFEsIcd1uBi0b5RbDPtdFGL4_Zw5XFTi_b94GJTyqedC8u-IcrZ8LA98Ygdanq4eNBxGocFhPgOpUyr29aUywLCRI5uPUs1mGD71o0RAO3Qt3aJSCMoB2oIxJaBCOOYC-7u_sP90Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام رهبر انقلاب به سی‌وسومین اجلاس سراسری نماز، صبح فردا همزمان با قرائت در محل برگزاری این اجلاس در حرم مطهر رضوی، منتشر خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/farsna/465611" target="_blank">📅 08:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465610">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEzPeeaMk1fRml6EniaaUkA4GJjLQbwQUyVV46_RgAl9SIRav4gMvB6lQdhvsipGJMfX7sbZOiQxGMSzdX5s2VQcp0IstPMT2ObQs_PlQKFPvMYas7x-OLr1ICYqm-6RkiQ32R4TWP3sQklPCdtmfKZwDHsEBS5vv2OVO-soYL_73MQunyi8OYBMhDhKbc4DZaEloiqFMCX0iD784k0dHrm1v0dJL7UVDabhdPjvCXTXsMcMkx7EX7fT9GocR5bF4vh99Ddv5JZz5EtPgyVxLo-ep60YsNYvXTgT3zhUj6cAb4EfiEZiEK_ZT5l04dhGbRkCcCMow5-P4yCeWtJeBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی: ایستگاه میدان شهرری خط ۶ مترو هفتۀ آینده تست گرم می‌شود.
🔹
حدود دو هفته پس از تست گرم نیز این ایستگاه افتتاح و به بهره‌برداری می‌رسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/farsna/465610" target="_blank">📅 08:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465608">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6a9c266f.mp4?token=eB1oLlH6J4E5k1USFr8eDkKXJg3QttgIvuIgUpJMr9yGPpoyLw6LTUKJH9Y-8pzcyLzMswA0g9iQGGZ9UCFT8CdKR5SyaFjhXdKPViNswBqDUORZOPpun7s2ggTsEYMKIFZMWvwEPrZPud2hWmWUFuyr4BfR9VUGbXAciOKc0RDVOjF7XctVtEmEanwCkElyfCsgGPozrN578y60A3SD80JXz2AJtcOYzUTeOt4k-fhbMXaBooTXo0r4tYs2yuUMLxG8fVS4iaJoAtLm4kygB19yCaHFkJZzSTW7m9q2F2MJBsJm_YMYTJ9-l7Q_57LxpmJW4M62Xx7QDAIsQvn3WkycflI8w9vJEH9sbaQh7xdKr0IEk8ww-KSalM8Gl6My3rPvjvmh6l-Ou5ZKUWJqwY5zQIZfLT6871dEU3v_hvnxjydJqGwigTvGJnqVVV0j9cQr3AqrmT9Ca0qhIeivQEzRCDlz5ZVfJl2H3_1Em-WQNB7yE9b_WFST8T1szoK8-etn7TvP0T2DvdToJPOzSYn1cFMh4ad6OJvqlwumTJigF2snnz7FygCTAkcJxqlpTEXROOO7_U3LA4CLwd0ntQZ5D1iAY1vFSWL_2EX6zEyeDnW5KlnX5498V0IteI7JBdNppvjtIvANgxbpQ9-_pnGEclUzyXpT4fujOYKfCwo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6a9c266f.mp4?token=eB1oLlH6J4E5k1USFr8eDkKXJg3QttgIvuIgUpJMr9yGPpoyLw6LTUKJH9Y-8pzcyLzMswA0g9iQGGZ9UCFT8CdKR5SyaFjhXdKPViNswBqDUORZOPpun7s2ggTsEYMKIFZMWvwEPrZPud2hWmWUFuyr4BfR9VUGbXAciOKc0RDVOjF7XctVtEmEanwCkElyfCsgGPozrN578y60A3SD80JXz2AJtcOYzUTeOt4k-fhbMXaBooTXo0r4tYs2yuUMLxG8fVS4iaJoAtLm4kygB19yCaHFkJZzSTW7m9q2F2MJBsJm_YMYTJ9-l7Q_57LxpmJW4M62Xx7QDAIsQvn3WkycflI8w9vJEH9sbaQh7xdKr0IEk8ww-KSalM8Gl6My3rPvjvmh6l-Ou5ZKUWJqwY5zQIZfLT6871dEU3v_hvnxjydJqGwigTvGJnqVVV0j9cQr3AqrmT9Ca0qhIeivQEzRCDlz5ZVfJl2H3_1Em-WQNB7yE9b_WFST8T1szoK8-etn7TvP0T2DvdToJPOzSYn1cFMh4ad6OJvqlwumTJigF2snnz7FygCTAkcJxqlpTEXROOO7_U3LA4CLwd0ntQZ5D1iAY1vFSWL_2EX6zEyeDnW5KlnX5498V0IteI7JBdNppvjtIvANgxbpQ9-_pnGEclUzyXpT4fujOYKfCwo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز همایش ۵۰ هزار جان‌فدای ایران در کرمانشاه
@Farsna</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/465608" target="_blank">📅 07:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465607">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار لرستان</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c921d0c509.mp4?token=K_nupvrLjLLcthNMFFywrISDJNU4zWXvG1o2wj1AOu5Up-9ztV6eLfXCyeu5moMCf1s0qczyPFFaRyXG9bt_1Csc2DCgoUrajPxDlgZyAHlnFyN3Nnen22KasX0BkcoA59bz3FWQUCnY-JPEE28EXxXpE1TY7eqHb7gSQXABqdN5Myp8k3JVOQiOoUOaOfW7VmlJ9bjgYuy3JTG8mxB_MecGrIo1gIZLuzeCXGRPMn0kmIuBcx1vuGixWdbzQKO5-VHGBjthsUq6nqhW-6yvGuahAuxoHSgUhlUlAxXVrmhnYq7iFfii6Tjm4Xh6BFkRYoGImCAjjIso5nOshyGV5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c921d0c509.mp4?token=K_nupvrLjLLcthNMFFywrISDJNU4zWXvG1o2wj1AOu5Up-9ztV6eLfXCyeu5moMCf1s0qczyPFFaRyXG9bt_1Csc2DCgoUrajPxDlgZyAHlnFyN3Nnen22KasX0BkcoA59bz3FWQUCnY-JPEE28EXxXpE1TY7eqHb7gSQXABqdN5Myp8k3JVOQiOoUOaOfW7VmlJ9bjgYuy3JTG8mxB_MecGrIo1gIZLuzeCXGRPMn0kmIuBcx1vuGixWdbzQKO5-VHGBjthsUq6nqhW-6yvGuahAuxoHSgUhlUlAxXVrmhnYq7iFfii6Tjm4Xh6BFkRYoGImCAjjIso5nOshyGV5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جلوه‌هایی از پائیز رنگارنگ در مسیر ریلی دورود
@Lorestanfars
-
Link</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/465607" target="_blank">📅 07:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465606">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFZystL_B78jL7kXySdG-qgF-gmxvcKrZ4VmF3qhQnEj9AvTvI0ZYGDx1Q1K38ggqOPii-a5An3u5GqtKhqn5YLCKlXwkcIQRz6xaJ1-Bt5yqOsSrkZJjkeMgoXaAkS_cXDNrHA8GiRDWTKtKPo430sYW1GtJOJehy_IGkG7Z3QAWUcpkmWnK2aY6EOeeye4yeo-kRXd6J8YW4AC51FSt0TDeKhQWtby1nMQDXqg8SSJLMH4E7Yff4hLSehWr2gAki-cImH6kiMbn_lFoqwelX8yWPvR-U5PwJBgHVVIuQUSL6pexOUcSCw_rrDM9Ys61oK-ugK-R9auSfsdru2Drg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات هوایی پاکستان در افغانستان ۹ کشته برجای گذاشت
🔹
خبرگزاری رویترز به نقل از طالبان افغانستان از حملات هوایی بامداد امروز پاکستان به مناطقی در افغانستان خبر داد که در پی آن دست‌کم ۹ نفر کشته و ۱۱ نفر دیگر زخمی شدند.
🔹
ذبیح‌الله مجاهد، سخنگوی طالبان افغانستان، با محکوم کردن این حملات ادامه داد «ما این اقدام را تجاوز و جنایتی در نقض تمامی اصول پذیرفته‌شده می‌دانیم.»
🔹
در مقابل، سخنگوی دولت پاکستان اعلام کرد که در این حملات هوایی ۲۲ «تروریست» کشته شده‌اند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/465606" target="_blank">📅 07:39 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465605">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‌ بالی به سرعت برق‌وباد برد
🔹
مهدی بالی در وزن ۹۷ کیلوگرم کشتی فرنگی ۸ بر صفر حریف قرقیزستانی، دارندۀ برنز المپیک را با ۳ فن فیتو برد و به نیمه‌نهایی رسید.  @Farsna</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farsna/465605" target="_blank">📅 07:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465604">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🎥
لحظات آخر در ناو دنا دقیقا چه گذشت؟  @Farsna</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/farsna/465604" target="_blank">📅 07:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465603">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پومسۀ انفرادی زنان صعود کرد
🔹
یاسمن لیموچی، نمایندۀ ایران در پومسۀ انفرادی زنان به‌عنوان نفر دوم گروه خود به دور دوم صعود کرد. @Farsna</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farsna/465603" target="_blank">📅 07:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465602">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‌ عبدولی هم به نیمه‌نهایی رسید
🔹
سعید عبدولی در وزن ۷۷ کیلوگرم کشتی فرنگی پس از استراحت در دور اول با برتری ۸ بر صفر مقابل سولامان از اندونزی به نیمه‌نهایی رسید.  @Farsna</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/farsna/465602" target="_blank">📅 07:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465601">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">عربستان حریف کشتی‌گیر ایرانی نشد
🔹
مهدی بالی در وزن ۹۷ کیلوگرم کشتی فرنگی ۷ بر صفر حریف عربستانی را برد.  @Farsna</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/farsna/465601" target="_blank">📅 07:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465600">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‌ عباس‌پور‌ نفس‌گیر برد
🔹
سجاد عباس‌پور در وزن ۶۰ کیلوگرم کشتی فرنگی یک بر یک حریف هندی را برد.
🔸
عباس‌پور در نیمه‌نهایی مقابل علیشیر گانیف، دارندۀ مدال نقرۀ جهان قرار می‌گیرد. @Farsna</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/farsna/465600" target="_blank">📅 06:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465599">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">جودوکار ایران حریف اماراتی را ضربه کرد
🔹
الیاس پرهیزگار در مرحلۀ مقدماتی وزن ۸۱- کیلوگرم جودو، بر حریف اماراتی پیروز شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/farsna/465599" target="_blank">📅 06:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465598">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eh7a8pTYpQysIcx4o2mpUqc7xhFnh5OlAIjacuowq_46BuXnDmTDBbPihCifDRLvA-FHzwfycE2J19qRaJk6dyZkSjE02dm_2Iimai0CvovHzH1gk9xS38ABGY0_Q6OEwhyUFABTeQ06UPIZpEn4FBv9Uc0_yPeH-GlEe3g_kjbGd7g6wENIiiiDPdlou1wtxP3NVjMBs9TlANEeTF0DWUdb-qdoDxxYd4fnWnpeRMLoqSF67GVtz0d1d1yj8svRcR4HnIhqfWf2asRSTCjzulVU1CxEzL89_Wz3DDuFy9UnVLduVR6lA2QB0ypA9A9ArxE03kOmkpwnQmEyHDly1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت کار جدید بانک‌های خصوصی اعلام شد
ساعات پذیرش مشتریان:
🔸
شنبه تا چهارشنبه ۷:۳۰ تا ۱۴:۰۰
🔹
پنجشنبه ۷:۳۰ تا ۱۳:۰۰
🔹
تعیین ساعات کار کارکنان واحدهای ستادی بانک‌ها با تصمیم مدیریت هر بانک انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/farsna/465598" target="_blank">📅 06:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465597">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‌ عباس‌پور‌ نفس‌گیر برد
🔹
سجاد عباس‌پور در وزن ۶۰ کیلوگرم کشتی فرنگی یک بر یک حریف هندی را برد.
🔸
عباس‌پور در نیمه‌نهایی مقابل علیشیر گانیف، دارندۀ مدال نقرۀ جهان قرار می‌گیرد. @Farsna</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/farsna/465597" target="_blank">📅 06:28 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465596">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">تیم پدل زنان کنار رفت
🔸
صبا نجفی و ندا محمدتقی‌پور در یک‌چهارم نهایی با نتیجۀ ۲-۱ مقابل فیلیپین شکست خورد و حذف شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/farsna/465596" target="_blank">📅 06:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465595">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0zrq-naj6zwYLUGfXmL_Q_3LrwpYYVB_VnbvSKV0CWe1oLehudskvUt_eCwxaPljYwkwXB6qv4-e9FifO6zrqBnDCSTo7VmBNs1xhqQBWxeP6-r7Y8cnlaOmWk7DPc7gD0YLXJTI8CuCvo0TrWWSqryKiNMsjrOoAe-RXr9octSJlg8OKbDwSa0llEoag62FaclJSNvjIx1OS2XzS47SFCIhZtLG7yZVd2j9kIKzuhbhqfkceG1GjKA6_pemXYJ4m647H13q4NzfFdkkSo-_075KltYxa-3UiuYWG392fGeepL7xbX7Mv9kEIIvTxaiX5IxvmMCjEiAqYyxM6cuBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعلیق ۲ شرکت مسافربری پس از ۲ تصادف مرگبار
🔹
در پی وقوع ۲ تصادف خونین در آزادراه همدان-ساوه و سربیشۀ خراسان جنوبی ۲۰ نفر فوت و ۲۹ نفر دیگر مصدوم شدند.
🔹
حالا رئیس پلیس‌راه راهور فراجا از تعلیق ۲ شرکت مسافربری پس از بررسی کارشناسی این دو حادثۀ مرگبار خبر داد و گفت مقصران برای رسیدگی قانونی به مراجع قضایی معرفی شده‌اند؛ این شرکت‌ها هم تا تعیین تکلیف نهایی، حق ادامۀ فعالیت و صدور صورت‌وضعیت مسافری ندارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/465595" target="_blank">📅 06:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465594">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بازی‌های آسیایی ناگویا عباسپور با پیروزی استارت زد
✅
سجاد عباسپور در وزن ۶۰ کیلوگرم کشتی فرنگی با نتیجه ۵ بر ۳ از سد هادونگ تان از چین  گذشت و به مرحله یک چهارم راه یافت. @Sportfars</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/farsna/465594" target="_blank">📅 06:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465593">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نمایندۀ جودو از رقابت‌ها کنار رفت
🔹
سمیرا خاکخواه در رقابت‌های جودو برابر حریف چینی شکست خورد و از دور رقابت‌ها کنار رفت.
@Farsna</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/465593" target="_blank">📅 06:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465592">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/538d7617ea.mp4?token=tpNCgidoHxCNctVDfUXKExP3oNfqJ9Juho-ilqZaF7nw-pTb2Ix8v7VsuqfQH_dbvwNV-4SYydZAWcDB1Xul3ZUea_uFfIs5DOKur1YE_OxAt6XZiq62PWaslUj4X7ho5sawmtaVTO3a3naDGS5ci_bFPLJ9ukUh8QS_wZid4yjCc1wLale70hJjJ3tYDL_dQWJ_0USRuYm5Y2ot0HGaEcyqvnx_W_Ph0cCSVM6cwSdWP9EwMatc577YLSxjgcQ3Isq7T6q-OD6_WO0ICx6ZTA0LvMTu7wDXzkAH2XEQxRKZ0xc_7MjHyjQvM2xJdTtNDEupUgD3EHclJVZAAzjyYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/538d7617ea.mp4?token=tpNCgidoHxCNctVDfUXKExP3oNfqJ9Juho-ilqZaF7nw-pTb2Ix8v7VsuqfQH_dbvwNV-4SYydZAWcDB1Xul3ZUea_uFfIs5DOKur1YE_OxAt6XZiq62PWaslUj4X7ho5sawmtaVTO3a3naDGS5ci_bFPLJ9ukUh8QS_wZid4yjCc1wLale70hJjJ3tYDL_dQWJ_0USRuYm5Y2ot0HGaEcyqvnx_W_Ph0cCSVM6cwSdWP9EwMatc577YLSxjgcQ3Isq7T6q-OD6_WO0ICx6ZTA0LvMTu7wDXzkAH2XEQxRKZ0xc_7MjHyjQvM2xJdTtNDEupUgD3EHclJVZAAzjyYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربستان حریف کشتی‌گیر ایرانی نشد
🔹
مهدی بالی در وزن ۹۷ کیلوگرم کشتی فرنگی ۷ بر صفر حریف عربستانی را برد.
@Farsna</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/465592" target="_blank">📅 05:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465591">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e34a3dcd.mp4?token=dlJFvK65d-HLSPsFv8TSndd4NMjOiPWcS9QgCpkESssgBDcQmwsU6nKCDpvmNHBBXgUFf_wFAyn0NprVqzsxYr3phsRVqkuoS4Yd1FufNOfySGa36iSlPBo7Siirdfw6QED2XsQHhtFzp5lTI8D2UXcMHQjPryK0L8AwS0AZelJ7gPUV_TnTJwiQumVqU52mDAXrkGbFMfBKOKYI8bXcK5LTaOh7Ili9o8ET9tzeoIjrRz_-Dwk2jYD92jkRUiDjO8sDrCh4zYWwhaKDvomTHoXZNan7NYKE3_N7Yahpy3p37q78U8aeaPuwKI4aM7hs0Pl0sXgWtDfbPEeBO5J8vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e34a3dcd.mp4?token=dlJFvK65d-HLSPsFv8TSndd4NMjOiPWcS9QgCpkESssgBDcQmwsU6nKCDpvmNHBBXgUFf_wFAyn0NprVqzsxYr3phsRVqkuoS4Yd1FufNOfySGa36iSlPBo7Siirdfw6QED2XsQHhtFzp5lTI8D2UXcMHQjPryK0L8AwS0AZelJ7gPUV_TnTJwiQumVqU52mDAXrkGbFMfBKOKYI8bXcK5LTaOh7Ili9o8ET9tzeoIjrRz_-Dwk2jYD92jkRUiDjO8sDrCh4zYWwhaKDvomTHoXZNan7NYKE3_N7Yahpy3p37q78U8aeaPuwKI4aM7hs0Pl0sXgWtDfbPEeBO5J8vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پومسۀ انفرادی زنان صعود کرد
🔹
یاسمن لیموچی، نمایندۀ ایران در پومسۀ انفرادی زنان به‌عنوان نفر دوم گروه خود به دور دوم صعود کرد.
@Farsna</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/465591" target="_blank">📅 05:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465590">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edb7b65819.mp4?token=JDXCiQgsFMscb4bqS4W5asYjZKNy5TxYaTRmuch4oyKp4R7ig5zSdHNDJSP8iAR0HIbSOreKFp7GcW5ersosJ4QLj-YFWQBXvQfXUZ6bxqCvbSDgw5_0iUaZit2KxkD1sgVBc59wA-WEt-Nz5qSyiWWGvXdLFVUC1RZm6zhiAaxMi1qRoplwCqYNYAQIN1GAceA_oDjesaDCQERWOEjfut_MH1LJu43vVi6hsSKXRcUexPIc01Qs3sn8Ni33JI4H6x0r53JiK-RcI4Q-6QeVYWunaht2rfOVAVDwE0tngB1NhV3Arclipv1B0iZQ4pHS9j0sNaExONNvVz3I3e51U6jsGr7bwTAQCOdM2_eXU3h9f8RBwZbo0KlNfyx2mYtn-wrSmNJ14_uqoSF6dZX6JJ6whczQxBkzmic5Bd8hsEl7g591z2bhrEdDjOz1hOqKNeu_v8Y3SVF3x0rqYqoqoDkvdIUvCIyy7QZY2IW7PmnaMfg0CnWX8KmGjLlgeJqqH-UVtTcbsIKDIJ53EYzM5uIR3ModaqRy7Wzz7PjrH2Cpz_p8rKLY2L-NaC3pY2pNbPLrTuY_uh3VeOLPJRlPrBJTEcyPdKZIUI0TnP7csWs4Kff3CVyq2bdHDROSGGwb19cFjaI-zkdhn8F8D3I6ynpVCionZPxNiVCJCSsEX_0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edb7b65819.mp4?token=JDXCiQgsFMscb4bqS4W5asYjZKNy5TxYaTRmuch4oyKp4R7ig5zSdHNDJSP8iAR0HIbSOreKFp7GcW5ersosJ4QLj-YFWQBXvQfXUZ6bxqCvbSDgw5_0iUaZit2KxkD1sgVBc59wA-WEt-Nz5qSyiWWGvXdLFVUC1RZm6zhiAaxMi1qRoplwCqYNYAQIN1GAceA_oDjesaDCQERWOEjfut_MH1LJu43vVi6hsSKXRcUexPIc01Qs3sn8Ni33JI4H6x0r53JiK-RcI4Q-6QeVYWunaht2rfOVAVDwE0tngB1NhV3Arclipv1B0iZQ4pHS9j0sNaExONNvVz3I3e51U6jsGr7bwTAQCOdM2_eXU3h9f8RBwZbo0KlNfyx2mYtn-wrSmNJ14_uqoSF6dZX6JJ6whczQxBkzmic5Bd8hsEl7g591z2bhrEdDjOz1hOqKNeu_v8Y3SVF3x0rqYqoqoDkvdIUvCIyy7QZY2IW7PmnaMfg0CnWX8KmGjLlgeJqqH-UVtTcbsIKDIJ53EYzM5uIR3ModaqRy7Wzz7PjrH2Cpz_p8rKLY2L-NaC3pY2pNbPLrTuY_uh3VeOLPJRlPrBJTEcyPdKZIUI0TnP7csWs4Kff3CVyq2bdHDROSGGwb19cFjaI-zkdhn8F8D3I6ynpVCionZPxNiVCJCSsEX_0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی‌های آسیایی ناگویا
عباسپور با پیروزی استارت زد
✅
سجاد عباسپور در وزن ۶۰ کیلوگرم کشتی فرنگی با نتیجه ۵ بر ۳ از سد هادونگ تان از چین  گذشت و به مرحله یک چهارم راه یافت.
@Sportfars</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/465590" target="_blank">📅 05:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465589">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نمایندۀ تیراندازی با کمان کامپوند به جمع ۴ نفر برتر نرسید
🔹
بیتا عاشق‌زاده در یک‌چهارم نهایی تیراندازی با کمان کامپوند با نتیجۀ ۱۴۶ بر ۱۳۵ مقابل کماندار فیلیپینی باخت و به جمع ۴ نفر برتر نرسید.
@Farsna</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/465589" target="_blank">📅 05:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465588">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‌ تعیین تکلیف آمریکا برای عراق علی‌رغم پایان حضور نظامی
🔸
باوجود پایان حضور نظامی آمریکا در عراق و تکمیل خروج نیروهای تروریست آمریکایی از خاک این کشور، واشنگتن همچنان برای بغداد تعیین تکلیف می‌کند.
🔹
المیادین به نقل از یک مقام آمریکایی گزارش داد که واشنگتن…</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/465588" target="_blank">📅 05:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465587">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">میدل‌ایست‌آی: تنگۀ هرمز تکرار درس تلخ ویتنام برای آمریکاست
🔹
مدیر مرکز اسلام و امور جهانی دانشگاه زعیم استانبول در تحلیلی دربارۀ پیامدهای جنگ آمریکا علیه ایران و وضعیت تنگه هرمز نوشت: این آبراه بار دیگر محدودیت‌های قدرت نظامی آمریکا را آشکار کرده و درسی مشابه آنچه واشنگتن در جنگ ویتنام آموخت، پیش روی آمریکا قرار داده است؛ اینکه برتری نظامی به معنای توانایی تحمیل نتیجۀ سیاسی نیست.
🔹
کاهش شدید تردد کشتی‌های تجاری از تنگۀ هرمز نشان می‌دهد که حتی قدرت نظامی آمریکا نیز نمی‌تواند به‌سادگی امنیت و جریان عادی کشتیرانی در این آبراه را تضمین کند.
🔹
آمریکا ممکن است توانایی وارد کردن خسارت به زیرساخت‌ها و توان نظامی ایران را داشته باشد، اما مسئلۀ اصلی این است که آیا می‌تواند شرایط را به وضعیتی بازگرداند که تردد کشتی‌ها در هرمز بدون ریسک و در مقیاس معمول انجام شود یا خیر؟
🔹
ایران حتی بدون برخورداری از توان دریایی هم‌سطح آمریکا می‌تواند با ایجاد نااطمینانی درباره امنیت عبور و مرور، هزینه‌های اقتصادی و سیاسی قابل‌توجهی ایجاد کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/465587" target="_blank">📅 05:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465586">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8oKEDTMxnnekMsnKsk7d4U3wgIgNxRLqNSN5fnLFeodRLsk3y4I0P2TCrDyl4PbSXClz0dLWOWAdbtvc3u_aMTuIa4sztII1oO6VCNpVThUjEOoNCN-oqByW86AjlAyRCde8rYcGoFZm1utYbmOa_d8a3arP8UToNBoe_H09ThjnLTqwzbT5EjOa1JW35vJSy570gIIcNjWEjvbKPADAYlwAgPSC4OIqWJZshvFOuILtV3H0bjuHzdv7AAFFdl2pBtcnuhWSH6UbGGoA8C1VksQJDg7pGt-T1RPdUTy1likz6_RnFK832ANztvBkTShlit14XXXAMFuxOyASO8ojg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلاش آمریکا برای دخالت در انتخابات ریاست‌جمهوری برزیل
🔹
مقام‌های اطلاعاتی برزیل از تلاش‌ها و اقدامات آمریکا برای اثرگذاری در انتخابات ریاست‌جمهوری این کشور گزارش دادند.
🔹
درهمین رابطه، آژانس اطلاعاتی برزیل اعلام کرده که مداخلۀ آمریکا را از «جنگ قانونی تا دخالتی که آشکارا مورد اذعان قرار گرفته» شناسایی کرده است.
🔹
آمریکا پیش از این دخالت در انتخابات برزیل را رد کرده است. روز یکشنبه دور اول انتخابات ریاست جمهوری در این کشور برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/farsna/465586" target="_blank">📅 04:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465585">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/452d37f684.mp4?token=gHp0h17S25QeKgRLvJLjz7I2xjAZhqaX6QHIYxocy9bgzIrbcqhzT6spwCnFfAIKi3SnrJFa3FMldenJYOrngawndFX8vAxlEE06a6kWzgvQHNdksCw1EJzu1tP5axlVaEUeU69VVso4dZaMKX-1BHbFIx2pmWM8zcTWy21JWol6VmNUW9KzjSiF06P07DfgMvJz8GoOvJnib_5CQYUAn0j3EXUpBLew7JWJjHJCpS2poHemBxW_L3pNyNE-4ifjPiGKfRQ_Furgmx-wt---Zmiuqg8tClhra5HcSCwlOwypOpPmO8xWRd_GIRdKyfEtz8IqmgeSVTm35NiidjGRSYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/452d37f684.mp4?token=gHp0h17S25QeKgRLvJLjz7I2xjAZhqaX6QHIYxocy9bgzIrbcqhzT6spwCnFfAIKi3SnrJFa3FMldenJYOrngawndFX8vAxlEE06a6kWzgvQHNdksCw1EJzu1tP5axlVaEUeU69VVso4dZaMKX-1BHbFIx2pmWM8zcTWy21JWol6VmNUW9KzjSiF06P07DfgMvJz8GoOvJnib_5CQYUAn0j3EXUpBLew7JWJjHJCpS2poHemBxW_L3pNyNE-4ifjPiGKfRQ_Furgmx-wt---Zmiuqg8tClhra5HcSCwlOwypOpPmO8xWRd_GIRdKyfEtz8IqmgeSVTm35NiidjGRSYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی جبهۀ شریان: برخلاف ملت، احزاب هنوز مبعوث نشده‌اند
.
@Farsna
-
link</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/465585" target="_blank">📅 04:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465584">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf2aaf03ed.mp4?token=Cv7RW0zluG8au12o--D-hkx2xzxsJvdy5DuioELDvjAkv0J_JXwuwUQWJ8XhO5ZsFq_FKgsvMXC9nLqZsCc_RSheWh5Of0MmEBFuFiv6j-BAao7mGWyCvA8X6YbevswZhWcCqQT9Yks1Wx5Na6fecnE4k718HqRpBu4iBaHmx9rE4SLLEFltFOSOehvhPRxeQOpZO7OKlmKLcM2g5ZAYu2NYs7BNmSeQdDe-9pHigJSu_ZRnoUYG25kQ75gnvcZnJ1quYhuPMZJy0xDpI9SlHgOi8zVLec0mDmcHPWMiR7-CPMm8JHwX2IEykoVpkGadsQVzpX58AR2hiuPOA-GxhDFrNnkhj_8fgbzsMVSEDXXuts1BaC2r3PP7jDo674kz7tgYtVOMmiryeVzaicx2R2BqtVVH-uxNnpMV_EXqfe91hlMNLPzO8y6gUdVFV7iLjpqvE6s-PG8FiKjZdP5-09Fu5HQQq9DihKRPpavNtqLJ_my-KQP-2ozckM_q1hKndd7htcZQMZWCuKo2AtNM7Iezex_UDJEqpMyEBDXZiCjlQ4dmPpzPlohySUd404yOCxgvI_NoiAMgD1No0_g-htRtrWOpOuJvu2h8bbdqJ5yr9-lQXDa2VnABEso_Rq34E43cQUNdRMmdhcasTS9MxUHfmVBlKXrfvGUVslEdq-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf2aaf03ed.mp4?token=Cv7RW0zluG8au12o--D-hkx2xzxsJvdy5DuioELDvjAkv0J_JXwuwUQWJ8XhO5ZsFq_FKgsvMXC9nLqZsCc_RSheWh5Of0MmEBFuFiv6j-BAao7mGWyCvA8X6YbevswZhWcCqQT9Yks1Wx5Na6fecnE4k718HqRpBu4iBaHmx9rE4SLLEFltFOSOehvhPRxeQOpZO7OKlmKLcM2g5ZAYu2NYs7BNmSeQdDe-9pHigJSu_ZRnoUYG25kQ75gnvcZnJ1quYhuPMZJy0xDpI9SlHgOi8zVLec0mDmcHPWMiR7-CPMm8JHwX2IEykoVpkGadsQVzpX58AR2hiuPOA-GxhDFrNnkhj_8fgbzsMVSEDXXuts1BaC2r3PP7jDo674kz7tgYtVOMmiryeVzaicx2R2BqtVVH-uxNnpMV_EXqfe91hlMNLPzO8y6gUdVFV7iLjpqvE6s-PG8FiKjZdP5-09Fu5HQQq9DihKRPpavNtqLJ_my-KQP-2ozckM_q1hKndd7htcZQMZWCuKo2AtNM7Iezex_UDJEqpMyEBDXZiCjlQ4dmPpzPlohySUd404yOCxgvI_NoiAMgD1No0_g-htRtrWOpOuJvu2h8bbdqJ5yr9-lQXDa2VnABEso_Rq34E43cQUNdRMmdhcasTS9MxUHfmVBlKXrfvGUVslEdq-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اگر دنبال آخرتی باید در دنیا تلاشت بیشتر از بقیه باشد
🎙
حجت‌الاسلام نوروزی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/465584" target="_blank">📅 03:28 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465581">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MC43NXNEAgiWjWT_49Rfsq3PtXJeUOe2eassjreyyVWXmdLtq1iZ-mWmqZxyDr18ePcxXbvwJtGfKl3_FI-W4b-OTp2LNd_aDWxzu4OBQYdBwaozFPa8B9PcdDhn03Zw00hs1O-qSBrOjLxEBPXYqVdfSf8JbmfCZfd_b5qhdXaGc1jNpd9mOm0wYTt9OW1AlbWnI_5Cyq-7sry-wJVwPpUYzpgt9T0uql4tG2jZLYH-A9fSGlST04vqOgbkILti54kq9XjjfBxEFgDvkeCLg2l5k0BmrkWeZghFTq7ME9GI_O9ml09fZNT4mdazSmDTWzGLl7-oRUeI6d7y0_EQfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NOp0ZOSraciVWWSOgvmSN8j5P35y6Zyre2QX8ABoF4-v39fXjdYicLE_6FhdN-LB-IkGLYgIPlRi8bSt1WCWMmasYFSLW8XipAkbERL0pn6Z6cO0Y1NKX8_o4geNcTxpDmhdnli8700pB-zCvd8AoFoqhrbXICaxHA6DUvDJdiSeuWdYewvMNSI05j64nZCb-Uw1VLbBvoDITKLkr_cfSTKafV2X96mO38fz9ugPwTm6FR7_4ykl6rGvUKElR6EDWU0da48EqwZRMLtp83guts4uCwjFs7VHed90Ht2pZ3LtMSDyKHeUS4kS9IEQyWVSlH5hN_7aEheCa4dW1_w3Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ugAq0F0_vpzg0Cn56cQL1TlmJMB6YEbHe_M091CT0m623vjV6GSdUA5N2BpRWYs92CU-2-EvgrSXl8tRORuT1Oy5YJaM3-cQyaclKNpXTbFteNB6ZPSpvbq9YW2a-0H-yKuLhLGQ0yOtM5NNB8O8gu4Q2pKfgZItdFPwO2jBdEC4WF4B1J7ecIdpYh8WKK4UUIH5hTK_5AJRH2Y0hDCpq8zVY-co9F4GwNyo3aUa-rqSibuuHSRjs4lUNTEmfT_M8ZHxJitCLhMKWHx-ONq0oQPw__Vd0c0ZUcxJbRx8-UHM4ITYl9vmOufsykKzXha7LwyCTu4y-yjTkY3XpTIO1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اهدای چفیه و انگشتر متبرک آیت‌الله سیدمجتبی خامنه‌ای به خانوادۀ شهیدان سیدعباس موسوی و سیدحسن نصرالله
🔹
جمعی از فعالان جبهه فرهنگی انقلاب اسلامی در جریان سفر به لبنان، با خانواده شهید سیدعباس موسوی و شهید سیدحسن نصرالله دیدار کردند.
🔹
حجت‌الاسلام والمسلمین پناهیان، حاج حسین یکتا و حاج سعید حدادیان از جمله فعالان جبهه فرهنگی انقلاب حاضر در این دیدار بودند.
🔸
در این دیدار، چفیه و انگشتر متبرک رهبر معظم انقلاب اسلامی به خانوادۀ شهدا اهدا شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/465581" target="_blank">📅 03:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465580">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دولت ترامپ ۲۵۰ هزار روادید را لغو کرد
🔹
باوجود تبلیغات هالیوودی برای رؤیای آمریکایی و فریب دادن مردم جهان برای مهاجرت به این کشور، دولت ترامپ، رئیس‌جمهور تروریست آمریکا روادید ۲۵۰ هزار نفر را لغو کرد.
🔹
سخنگوی وزارت خارجۀ آمریکا اعلام کرد که بزرگترین لغو روادید در تاریخ این کشور توسط دولت ترامپ انجام شده است.
🔹
او این اقدام غیر دموکراتیک را یک «نقطۀ عطف تاریخی» در این کشور و نماد تعهد تزلزل‌ناپذیر دولت برای حفظ امنیت مردم آمریکا عنوان کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/465580" target="_blank">📅 02:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465579">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ: آخرین نیروهای آمریکایی درحال ترک عراق هستند
🔹
رئیس‌جمهور آمریکا: آخرین نیروهای آمریکایی درحال ترک عراق هستند. این مسیر طولانی بود و تصمیم‌گیری‌های بسیار بدی باعث شد اساساً وارد این باتلاق شویم، اما به‌زودی این ماجرا به بخشی از تاریخ تبدیل خواهد شد.…</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/465579" target="_blank">📅 02:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465578">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
حملۀ مسلحانه به ایست‌وبازرسی در راسک
🔹
پلیس سیستان‌وبلوچستان: ساعتی قبل، در پی حملۀ بزدلانه و مسلحانه به یکی از ایستگاه‌های ایست‌وبازرسی در شهر راسک، گروهبان یکم علیرضا سنچولی از مأموران انتظامی، به شهادت رسید.
📝
تلاش برای شناسایی و دستگیری عاملان این جنایت ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/465578" target="_blank">📅 02:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465577">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqhLmcCHK6H5FFfrZAyIn_c9PL_PQVUWz6Lq95AU_g1pwEIVjvAzZPW0yggT1YBk8Zp_XBXsUVxsxsdmPKUKNTs9mygnBhGF-uUfgb1WK_y1UQ2XjKw45RYwGw1BGzumkqlS2gRjt3TZplyaqYcILDRLdXw3Im5ZVi5wXLPoPXrJowTB8nUs62MBClJAPTHBkayE-MdumQXW9tzThdo8-i9AI92dNQePGPftDuq1bs3zG19YYY6o7hILU_vU1BDjzXqjfnu2mVWOL1XV9IaHFlwURnclYki5_MDshznTENdDKFPBc1cKOVe9h1XjEqvpjartZ9HoC9sn7muCMZ0SKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نبض حساس اینترنت در عمق هرمز!
🔹
کابل‌های زیردریایی، بخش اصلی انتقال داده میان قاره‌ها هستند و بخش بزرگی از ترافیک بین‌المللی اینترنت از همین مسیرها عبور می‌کند.
🔹
آسیب به یک کابل فقط به معنای قطع یک مسیر ارتباطی نیست؛ تعمیر آن می‌تواند هفته‌ها زمان ببرد…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/465577" target="_blank">📅 01:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465576">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLpGG1PEuKdzYgLK05UtoNMffcqXV00TRipEeacfUT2ZQeeOXqh3YzqVdn7sFk28554DPKi2OplD2skB9R8rWkYneK-HBEX-tT7U9sfNmvEP8v6tNFwipmjFRSHk2l-12DInQMES93PwXZsOOdpF3xBFqjC175CBPzYh2Doyc85oeeHs_XmrAIhV_PWsN1NLFV_Vxs7k_6LyxPnfLwNZzWROCmCJitMmjBYRErDsJ60LSXJ4Tb_gIZGb1ymZo-vBA_NCCa5dgJrvx2Gct5mzIWjZGFLo3kvD6laYS3Xq8Logt_7uFM0oqGQrED1HSojjyvCQf17vBWE6bwLU6yhIsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف رمز ۱۱۱۱ کارت آزاد جایگاه‌های سوخت آغاز شد
🔹
استفاده از رمز ۱۱۱۱ برای کارت‌های آزاد جایگاه‌های سوخت دیگر امکان‌پذیر نیست و متقاضیان برای استفاده از این کارت باید ابتدا از طریق کارت بانکی احراز هویت شوند و پس‌از دریافت رمز یک‌بارمصرف، می‌توانند از آن استفاده…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/465576" target="_blank">📅 01:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465575">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بازدید ۲۰ میلیونی نامۀ سپاه به مردم آمریکا
🔹
نامۀ سپاه به مردم آمریکا در سکوهای داخلی فضای مجازی با ۸ هزار و ۳۶۰ محتوا و ۱۵ میلیون و ۷۷۰هزار بازدید، بازتاب پیدا کرد.
🔹
این نامه در سکوهای خارجی با هزار و ۶۶۰ محتوا و ۴ میلیون و ۸۸۹ هزار بازدید، انعکاس یافته…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/465575" target="_blank">📅 01:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465574">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🎥
حسین یکتا در مزار شهید نصرالله: شهید نصرالله می‌گفت آمریکا از منطقه اخراج و رژیم صهیونیستی زائل خواهد شد.
🔹
به جوانان وعده داده بود که به‌زودی در بیت‌المقدس نماز خواهند خواند.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/465574" target="_blank">📅 00:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465573">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">تهدید جنبش «حرکت یحیی» به گرفتن انتقام از مالک شرکت داماک امارات
🔹
جنبش مسلحانه و تازه‌تأسیس «حرکت یحیی» در پیامی با اشاره به حمایت مالی حسین سجوانی، مالک شرکت داماک از ترامپ، تأکید کرد که شبکه‌های مالی پشتیبان ظلم سرانجام در برابر اراده ملت‌های مظلوم پاسخگو خواهند شد.
🔹
در این پیام با اشاره به داستان گوساله طلایی و سامری آمده است که ثروت حامیان ظلم ماندگار نیست و روزی شبکه‌های مالی تغذیه‌کنندۀ آن افشا خواهند شد.
🔹
این جنبش مسلحانه تأکید کرد «پول ظالمان از ارادۀ مظلومان قدرتمندتر نخواهد بود و ائتلاف‌های تجاری نیز صاحبان خود را از پاسخگویی در برابر افکار عمومی و تاریخ مصون نمی‌کنند.»
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/465573" target="_blank">📅 00:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465572">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سفرهای گالیور</div>
  <div class="tg-doc-extra">قسمت ۳</div>
</div>
<a href="https://t.me/farsna/465572" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۲ – سفرهای گالیور</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/465572" target="_blank">📅 00:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465571">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5001bb0671.mp4?token=Vfq-_18hmSlXInJc6YOlPYKqZcI_zeX3jXwtnbG3D7Z4BBQ-mzbo35X-U1oBHcp5xpQNakqZf3DlFOiQkcZW5D_1tQ8p4uo13wRRBE_60wLGjvp0WYW5Ui2AxXDw-3GIcZNmMc6qiqhxsnfbesktLTfp-MtV7oZMtgSDR6P7gLUADo3s9T7zjn8oevP9GIlF6o4RX2KlIJvZpb7y0s0W-EQP_zq_yRajCC_tzy0xXuUm9YEP1mAOCtJLFgylvuu_YfGdfa5U5ndlKSNJcRx5Zbx05MeG0YCP_qVA78o456VeGWb4KLvWj_RVzas6d_dIq6R92qdnBOe1fLcBpMMMIzUac1RM7hcKjksF9XCoKC-Ae4NpI0A0AzA0maZxt441Xa8uSmv_yWdRw8km3DxCvkJ_HrxXpSxkFKFLKTEAtJmHSUqgEPAa6MPuyKurnqFdEiKUVOx7EB5gDkeM4cIF5pKTlXWcLgUx4P2QDe2a27ePf-yVgi4rvdIA2gvFTt0GncGTNSnnpvAeHF9i179xafLAkTCcFzuNqDxjmxGXuvMKo4E3ogKKAOf0NGtGhrpTYsV8ev6PAN-TRP9WC_ogBVA1JbTHxGC9vM6RppRwb762CvEtSYaJdrdbVPutbtOpgqS_a5zlahQNr0JnlNekW3u6B2zMXcmJoFcUVUILkVo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5001bb0671.mp4?token=Vfq-_18hmSlXInJc6YOlPYKqZcI_zeX3jXwtnbG3D7Z4BBQ-mzbo35X-U1oBHcp5xpQNakqZf3DlFOiQkcZW5D_1tQ8p4uo13wRRBE_60wLGjvp0WYW5Ui2AxXDw-3GIcZNmMc6qiqhxsnfbesktLTfp-MtV7oZMtgSDR6P7gLUADo3s9T7zjn8oevP9GIlF6o4RX2KlIJvZpb7y0s0W-EQP_zq_yRajCC_tzy0xXuUm9YEP1mAOCtJLFgylvuu_YfGdfa5U5ndlKSNJcRx5Zbx05MeG0YCP_qVA78o456VeGWb4KLvWj_RVzas6d_dIq6R92qdnBOe1fLcBpMMMIzUac1RM7hcKjksF9XCoKC-Ae4NpI0A0AzA0maZxt441Xa8uSmv_yWdRw8km3DxCvkJ_HrxXpSxkFKFLKTEAtJmHSUqgEPAa6MPuyKurnqFdEiKUVOx7EB5gDkeM4cIF5pKTlXWcLgUx4P2QDe2a27ePf-yVgi4rvdIA2gvFTt0GncGTNSnnpvAeHF9i179xafLAkTCcFzuNqDxjmxGXuvMKo4E3ogKKAOf0NGtGhrpTYsV8ev6PAN-TRP9WC_ogBVA1JbTHxGC9vM6RppRwb762CvEtSYaJdrdbVPutbtOpgqS_a5zlahQNr0JnlNekW3u6B2zMXcmJoFcUVUILkVo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد لبیک یا سید مجتبی زنجانی‌ها در شب ۲۱۴
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/465571" target="_blank">📅 00:24 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465570">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udKW8ownpLau4CGqDu-wKCJmzjJ4Ozj0n4kkFl0qKT4-FFNOuo9y2_ErKxrDde8JDPfexeVedXL6GxhGL8jrpnbVHeSuaX3Ap9piyaX2xs5VKPoSUE3F9VH8W5MAaxvaDwBDFoevJPL7nCLRLc4n6lMg3Astz1gpmFHnweX2xxLNJyfP6ABytg-NANfaemECLO-l4yvdarW92gZ-G-xiJcOTVXzAmI-mZ_RW9phjGLE9rfxkNKX1ma0YCZTN_ueMOye8uI-D98Ts9k0jJdGgR3-YAGmGfRj-sFkUgZL3eaOlLuQWpGaQozuxRpMyjN35bitu64EG7T_mcKxs88cXFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیک اندیش تا نیکی آید پیش
🔹
در زمان پادشاهی انوشیروان، ۲ مرد به دربار آمدند و جلوی قصر ایستادند. یکی با صدای بلند فریاد زد: «بدی مکن و بد میندیش!» و دیگری گفت: «نیکی کن و نیک اندیش تا تو را نیکی آید پیش!»
🔹
انوشیروان دستور داد به مرد اول هزار دینار و به مرد دوم دو هزار دینار پاداش بدهند. نزدیکان و درباریان با تعجب از پادشاه پرسیدند: «هر دو حرف یک معنی داشتند؛ پس چرا به یکی بیشتر پاداش دادی؟»
🔹
انوشیروان پاسخ داد: «مرد دوم فقط از نیکی سخن گفت، اما مرد اول از بدی هم یاد کرد. هیچ نیکی بالاتر از دوستی با نیکان و یاد کردن از نیکی نیست، همان‌طور که هیچ بدی هم فرقی با همراهی با بدی ندارد.»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/465570" target="_blank">📅 00:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465569">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESsQ5Dnf5NAea-OW8dHwm5ykylPeXme-m72zTpK-VR7C3UXUsXbimBFlFQ38COiqGZtarduj1nb9roMo25SU06qIhfqhM0S8FQnfs00JYIyFiuAXWTEbT8fynMbnm2xG6MYMfeWAc6lZ5dzFnsNkzsJp48J6Gui_1GobbiVN6Vw_aq8u42fjT0u4yPzcxVnMgyC8hDE6YpE8nZRn7ujSNaLzAAW_V49D8oc-crMJ8Vd1ttS70u0zbsb4jcKxt4vB9dFqMWQEJZ1isvK7mToLiZPpgSx7F2zb6iwCg6btGjhNWtnsAJbmHT8Oh6Xl6dNruhqPcTcoEdfTPc_9o5W9sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس را بدون اختلال دنبال کنید
🔸
به‌دلیل محدودیت‌های ناشی از تحریم‌های آمریکا و عدم ارائهٔ برخی خدمات زیرساختی به خبرگزاری فارس، دسترسی به وب‌سایت فارس برای برخی کاربران با اختلال مواجه شده است.
🔸
برای دسترسی پایدار به اخبار فارس، آخرین نسخهٔ اپلیکیشن فارس را
به‌صورت مستقیم
یا از
کافه‌بازار
و
مایکت
دانلود کنید.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/465569" target="_blank">📅 00:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465568">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d63025fdec.mp4?token=EoAXjgFdMMt6Db6fekjhVGsOJfPtdcsgHTQBRZ4HAgTDkRUkLCc29KJm1lG1uMNov4FEB_Lqw7CaQ7vsTqsTN8sNTH1xJjaaIlQYUZYKHJim-m0-7gcGuhqYFN5mjGFgJwuVdZTepUasW7XReVsTVTbvEBEDOJn-fs6Umhda_t5Hq4Rj6Jdtzc5CulTYpoSgtejO4CS4GA3uD1M5ESq9hcUC99vDMXCuczl28tPEJJx9BQFu5xSL4475JShGaRHRhwRTrFSb__iFxE8bPEEX9bg7i2o77IK5IW1Ihe4llcMy4QAVeORz5m4YXQpxgRQ4D7u3wivA25pyBcMnhiGpiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d63025fdec.mp4?token=EoAXjgFdMMt6Db6fekjhVGsOJfPtdcsgHTQBRZ4HAgTDkRUkLCc29KJm1lG1uMNov4FEB_Lqw7CaQ7vsTqsTN8sNTH1xJjaaIlQYUZYKHJim-m0-7gcGuhqYFN5mjGFgJwuVdZTepUasW7XReVsTVTbvEBEDOJn-fs6Umhda_t5Hq4Rj6Jdtzc5CulTYpoSgtejO4CS4GA3uD1M5ESq9hcUC99vDMXCuczl28tPEJJx9BQFu5xSL4475JShGaRHRhwRTrFSb__iFxE8bPEEX9bg7i2o77IK5IW1Ihe4llcMy4QAVeORz5m4YXQpxgRQ4D7u3wivA25pyBcMnhiGpiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یاد امام و شهدا در مسیر بیروت؛ سفر جمعی از شخصیت‌های فرهنگی، هنری و ورزشی ایران به لبنان با حضور حاج سعید حدادیان و حسین یکتا
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/465568" target="_blank">📅 23:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465567">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUbKuKUsSEwbPeWp3EDwjV5y7hv6ej9Xy6J8TMdoUU9HOOkzVUGPkjyFKXcLSnjD2wSNhiWKvGVXAm9AHHM7EkuiaD_sQK-ndw80WE3M2uTOUVAn2vK3K5yRljUNjgqkOCG4gRJ5EaJtg_AMKHrxYmoiWkA5JYa9L5i_Nbf3EsYw-sXtTjANgbMXy2JMyVIt3H1LklK-qNDfCLwKqTI0YqWVzEWry7wvpewUkmpyS7hUe5WBKvr5xKtZtZDcBSiiGMwARokkbhc5rSYhodlpv0iVp0beRiqbpZaohe0OIBz62vJnBuoCqs7OsEfEmsVVfZ_FdaCpBQMwiVzNJ-9Vrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افشای احساس «تنفر» ترامپ نسبت به وضعیت جنگ با ایران از زبان عروسش
🔹
لارا ترامپ، عروس ترامپ: جنگ با ایران ممکن است منجر به شکست ترامپ در انتخابات آتی شود.
🔹
ترامپ به‌شدت «از نحوهٔ پیش رفتن اوضاع با ایران متنفر است» و آرزو می‌کرد که «اوضاع سریع‌تر پیش می‌رفت.»
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/465567" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465566">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70242d6d56.mp4?token=OlFutacbH2qpnvd0yjNkkuOPKz6HkOh8oHHR3xP0tMLaMw1qBIxYkdTz4yVgi9zMuA6BSX0G2xv5i0SMYfN54ASHhU10Ud19GB6QD6DcPCHwHws8N7i3l7FHaL83sqLzkxfMHiVopRIJSCE7b3XaXuBBWvW9FPjtkjCiDPJYb5mbYgO0vBwt8ZC1zcHBEiFon4r9c27UC8uwVdw_r7Fs4LRpfIMMaBr02TAhIcz2kBJKPTkHia9VfzbaWH6twlmrV4hC33FAojA7U_F0txkrnxXP1f8uj5PbgV83M9n0qLsJ4xAf6zd2jlSNy7LDX-LF98Fh12Ri_zdCxdJvFUVsKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70242d6d56.mp4?token=OlFutacbH2qpnvd0yjNkkuOPKz6HkOh8oHHR3xP0tMLaMw1qBIxYkdTz4yVgi9zMuA6BSX0G2xv5i0SMYfN54ASHhU10Ud19GB6QD6DcPCHwHws8N7i3l7FHaL83sqLzkxfMHiVopRIJSCE7b3XaXuBBWvW9FPjtkjCiDPJYb5mbYgO0vBwt8ZC1zcHBEiFon4r9c27UC8uwVdw_r7Fs4LRpfIMMaBr02TAhIcz2kBJKPTkHia9VfzbaWH6twlmrV4hC33FAojA7U_F0txkrnxXP1f8uj5PbgV83M9n0qLsJ4xAf6zd2jlSNy7LDX-LF98Fh12Ri_zdCxdJvFUVsKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ وزیر جنگ آمریکا به رسانه‌ها بابت افشاگری دربارهٔ جنگ
🔹
وزیر جنگ آمریکا: همان‌طور که می‌‌دانید فضای اطلاع‌رسانی هم میدان جنگ است اما رسانه‌های ما کاری کرده‌اند که رسانه‌های دولتی ایران معقول به نظر برسند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/465566" target="_blank">📅 23:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465565">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff6cddf678.mp4?token=Nj7d7rUeaRQE_O_p0xTOYmr9lKVjDNkiypERnZiLwLK2aTWOnEkHYuWCfZQ33ftRdwsjchmYEkDgrXcjNs8mZs0apSkIrnrPZkS7XLnt8F09nR2wZMTFyezoaUi_ST8yp9O6P3_NbmIO30amrOgOkgMIAQdLI7jm7XbYsEEpYG1Rpfcvj4rx1vmSrzwyDL6w3OnQME0jZTuTwysp7kCGlnuhZXuAunDx4BZwxO8aENDmkJm1bCOKSJ2hwlyoiEFSHObOh_F0P-2_48SqKGiSgKHe58qgkubV253nNRoIHg1N_bXtZ3oQvL1RpeKwi_7Ar4AglR3NTa4emGG6UrlPDbB9ueHGmZkgVr1Pz9IQFDaSYXNV5L9JC7_yJHYnOel7b9YJR0Vh2vDq_i7baC80tqL7jmMgKwOo0aoNkczQTvoXhVNQoPY31lWDRueOJbryi9nNVSKcEkWwzCZgwkFLs2j-uucTDS-G5L4lJiRByNvH5DN16tvbml_bSkTx2MW1lAjAErcLTAZZ4MkMxfbEMkiWhJFoGkq5MGySvG5AdWeICCuLu0C77AORtx8l3WCstfmxS8m3Jft2l_WzoKwZIAi04WzRx5ff8nxV79paR5GtgL5vILrWVTZIc_iuVBvNXNkzimDr1nKPDrrQWW2yaJgN0gp5fNYzMGHZ_wj8yPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff6cddf678.mp4?token=Nj7d7rUeaRQE_O_p0xTOYmr9lKVjDNkiypERnZiLwLK2aTWOnEkHYuWCfZQ33ftRdwsjchmYEkDgrXcjNs8mZs0apSkIrnrPZkS7XLnt8F09nR2wZMTFyezoaUi_ST8yp9O6P3_NbmIO30amrOgOkgMIAQdLI7jm7XbYsEEpYG1Rpfcvj4rx1vmSrzwyDL6w3OnQME0jZTuTwysp7kCGlnuhZXuAunDx4BZwxO8aENDmkJm1bCOKSJ2hwlyoiEFSHObOh_F0P-2_48SqKGiSgKHe58qgkubV253nNRoIHg1N_bXtZ3oQvL1RpeKwi_7Ar4AglR3NTa4emGG6UrlPDbB9ueHGmZkgVr1Pz9IQFDaSYXNV5L9JC7_yJHYnOel7b9YJR0Vh2vDq_i7baC80tqL7jmMgKwOo0aoNkczQTvoXhVNQoPY31lWDRueOJbryi9nNVSKcEkWwzCZgwkFLs2j-uucTDS-G5L4lJiRByNvH5DN16tvbml_bSkTx2MW1lAjAErcLTAZZ4MkMxfbEMkiWhJFoGkq5MGySvG5AdWeICCuLu0C77AORtx8l3WCstfmxS8m3Jft2l_WzoKwZIAi04WzRx5ff8nxV79paR5GtgL5vILrWVTZIc_iuVBvNXNkzimDr1nKPDrrQWW2yaJgN0gp5fNYzMGHZ_wj8yPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور هیئت ایرانی در منزل جوان‌ترین شهید مقاومت در بیروت
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/465565" target="_blank">📅 23:46 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465564">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🎥
تصاویری از انفجار داخل نیروگاه حرارتی دمشق  @Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/465564" target="_blank">📅 23:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465563">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43dc64f223.mp4?token=UQYS3TcMsBf3_CEYrD3ITzGVD2NHX3_nkfrncRcw9S2qKW3SCTW2MHxSK9WwH9jXSxBa-YbGO4xpf5Du0JoghfnCogvJFylqcTQ8TRulYdjv4hEbI7ZIc1qMDAb8XAAj6bU9QfpLO_yQHrHDxWtTsjZykeDru77OVI5actJBn7QZ5A0hFMIHDvd3BT9Y4r7fUuADDPPxWRIKvWcKBpiqQRclzUNdDKakw6LntHfxylgyo02EyFhdkVDuvaQRV-NeVcfGN8o21Ce9_kkOxJBPM6c6Sw3NVdzXnOybTIuCKlJ6WNaVvbe5lgqzc3TaIl117AGrNeX53nQJBqZQFhhk4ji-eR_Rq9d72ttjWMS11yqtZ0PvJLJ00i6JZU_0azuiwaU0ixC1uI0wpD5x0vbpxfuUXqaQk6vRmdxuPU3PYJN3AFXxOtkauuymG30VGm9H1dv-92AByrRzVLvIlUON28OQ9lBr2cHpO2WJFtgSkM40P3aFy0kCgIermxT0W4Un0Rt7ggVX3aFnGLGsGKETPrh3HnvVTlvlo7vW6HRIctSaVhj5ZBA3pa9gKJH76Qex1FwkcE4CJD2HSim0fwNz2lLrE1Rve3JTLlc_AcHI4DPKFBO85Zbl6QY7ajBQjXZnwgz6LXLC4Q2bkGFu0Ec4uKVls0Fls2M4TomKqcJmdUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43dc64f223.mp4?token=UQYS3TcMsBf3_CEYrD3ITzGVD2NHX3_nkfrncRcw9S2qKW3SCTW2MHxSK9WwH9jXSxBa-YbGO4xpf5Du0JoghfnCogvJFylqcTQ8TRulYdjv4hEbI7ZIc1qMDAb8XAAj6bU9QfpLO_yQHrHDxWtTsjZykeDru77OVI5actJBn7QZ5A0hFMIHDvd3BT9Y4r7fUuADDPPxWRIKvWcKBpiqQRclzUNdDKakw6LntHfxylgyo02EyFhdkVDuvaQRV-NeVcfGN8o21Ce9_kkOxJBPM6c6Sw3NVdzXnOybTIuCKlJ6WNaVvbe5lgqzc3TaIl117AGrNeX53nQJBqZQFhhk4ji-eR_Rq9d72ttjWMS11yqtZ0PvJLJ00i6JZU_0azuiwaU0ixC1uI0wpD5x0vbpxfuUXqaQk6vRmdxuPU3PYJN3AFXxOtkauuymG30VGm9H1dv-92AByrRzVLvIlUON28OQ9lBr2cHpO2WJFtgSkM40P3aFy0kCgIermxT0W4Un0Rt7ggVX3aFnGLGsGKETPrh3HnvVTlvlo7vW6HRIctSaVhj5ZBA3pa9gKJH76Qex1FwkcE4CJD2HSim0fwNz2lLrE1Rve3JTLlc_AcHI4DPKFBO85Zbl6QY7ajBQjXZnwgz6LXLC4Q2bkGFu0Ec4uKVls0Fls2M4TomKqcJmdUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مداحی عربی سعید حدادیان در محل مزار شهید سید حسن نصرالله
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/465563" target="_blank">📅 23:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465562">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/458ec4c8a8.mp4?token=N3OK8TAVyIzuItHEsQhnhYP3muS9YtgGytRt7ZCsQHuv78a0v678_xepeyNLEDibtGxJGmMucdwUOkE2GcoA2z3Grr2nWzXE9KNPud708gbKbDnzC-h-mfYiCmajAzodP16lxaCXbAQwBvVwIvQ9lhVOcfMySnXke7YUDotQlQbkr_GhTuo6cYE7e_IUlkBK0UN1NkBsT5s5yEMUO437w8TpZXObqwPDR6myZiwL-Hbe3EITG3F1xMJtlLiP-Vc7nR1sC-IXp3jD_ypEjRoB5PPzW_EwhJHaBcL_WFUzR84k-y_p8bAsmrbGJ648P4aDBu4sPZYynHFULeJ-UMAShCkKmoGaZxhKCo1Fj4m7z5W4cyaZlbj-o4suIOGMR-hWtvxtICnEeOco491IQi5RDEvFotkRItNTJwNhI9CBhrbvGWXQDy-YK-j39XsUcX5l5Mv1lkPvU6jv5hfOLkwm3-_GlPQZyJBDsvDaKH3Bvb0ldvSpMjkY3jimThE4Qav561CAcErCX_G8Gu26cU1GsmxZcnHpIlNArpa6IYz7nLbE3bghjjVUlGEzWYi6yEmGDz7gwzveICow6YIFvh9wcPqexCmft7WvWMvfqxU0QbaNTlDD9EYwX-F7iJqtrtNG1WchxMQuNS7tnK01AvCd0i5lRtmlSkbiXdOHYa98Qhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/458ec4c8a8.mp4?token=N3OK8TAVyIzuItHEsQhnhYP3muS9YtgGytRt7ZCsQHuv78a0v678_xepeyNLEDibtGxJGmMucdwUOkE2GcoA2z3Grr2nWzXE9KNPud708gbKbDnzC-h-mfYiCmajAzodP16lxaCXbAQwBvVwIvQ9lhVOcfMySnXke7YUDotQlQbkr_GhTuo6cYE7e_IUlkBK0UN1NkBsT5s5yEMUO437w8TpZXObqwPDR6myZiwL-Hbe3EITG3F1xMJtlLiP-Vc7nR1sC-IXp3jD_ypEjRoB5PPzW_EwhJHaBcL_WFUzR84k-y_p8bAsmrbGJ648P4aDBu4sPZYynHFULeJ-UMAShCkKmoGaZxhKCo1Fj4m7z5W4cyaZlbj-o4suIOGMR-hWtvxtICnEeOco491IQi5RDEvFotkRItNTJwNhI9CBhrbvGWXQDy-YK-j39XsUcX5l5Mv1lkPvU6jv5hfOLkwm3-_GlPQZyJBDsvDaKH3Bvb0ldvSpMjkY3jimThE4Qav561CAcErCX_G8Gu26cU1GsmxZcnHpIlNArpa6IYz7nLbE3bghjjVUlGEzWYi6yEmGDz7gwzveICow6YIFvh9wcPqexCmft7WvWMvfqxU0QbaNTlDD9EYwX-F7iJqtrtNG1WchxMQuNS7tnK01AvCd0i5lRtmlSkbiXdOHYa98Qhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاشمری‌ها در شب ۲۱۴ باز هم قدرت‌نمایی کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/465562" target="_blank">📅 23:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465561">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54986f0b91.mp4?token=P7o3sD5I_azaRD1nADbCC4BfKaDgIb8rH6K6onypW1mRz7PZjRygc2MW_A8AYYiasYTwIPFLPVxVl3jDmqJZu1Vf-8EdRhV7BFWKHagTMfTxm2mD3VEXo-qGqePprmYdgUyKq_LJ3Ig4eUGcr6MxTw46YWVcVCndLgFT2ehr_A4t9ZsyJfIwFMCkC8lFxgI5fYYhYii3b6y47P6AKgPRXWu5fhh_EhiM3M4v_YxmkypuL19Gz-u7xs0v2IjiAw08IhyGQSr7uME1AaQkgWXjgZeDW5ScoXhVOIQa5iW1_-BeLzsJNU4fEAYx3Bay6uure8oN9bcpkjYcrTf4FEMAyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54986f0b91.mp4?token=P7o3sD5I_azaRD1nADbCC4BfKaDgIb8rH6K6onypW1mRz7PZjRygc2MW_A8AYYiasYTwIPFLPVxVl3jDmqJZu1Vf-8EdRhV7BFWKHagTMfTxm2mD3VEXo-qGqePprmYdgUyKq_LJ3Ig4eUGcr6MxTw46YWVcVCndLgFT2ehr_A4t9ZsyJfIwFMCkC8lFxgI5fYYhYii3b6y47P6AKgPRXWu5fhh_EhiM3M4v_YxmkypuL19Gz-u7xs0v2IjiAw08IhyGQSr7uME1AaQkgWXjgZeDW5ScoXhVOIQa5iW1_-BeLzsJNU4fEAYx3Bay6uure8oN9bcpkjYcrTf4FEMAyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار بروجردی‌ها: پرچم خون‌خواهی روی دوشم، وطن نمی‌فروشم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/465561" target="_blank">📅 22:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465560">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6uPKukTV6yHbE-JBvoQRfGYVj23GVjBCO_hASU7Bkmw9bCVV5MVE3C1BPJHT98UQJFcal_TE5a5sS-JqxmEEutNBaE5vw75wU8xnvNNxDFUd8JJRn2bIwQRfRgaRLf_8XKTyK6T1uqPDs09X7NtjAIBdUV6F88acsT3hXw59nirRpXgvZopmcVfysL0QXv364pY5dbFALonV2twtoBOH9fAZSbnXuwoCWxDfNDaqo9Ur1R4BG36PHgPuNlC7tsOKNprsYDR7sKUZIax-0SYb7VGgMPZk2or2Z019vLhu2Qb8MXwDDAxQ4GHIqP433Rt1CRgNIRBpbZ6FKgMWpkIog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
کتاب نظم جدید جهان اثر محمدصادق شهبازی منتشر شد
🔹
کتاب در نگاهی از بالا به تغییر نظم قدیم جهانی، افول آمریکا، برآمدن قدرت‌های تحول‌خواه، ایران و جبههٔ مقاومت و نظم جدید جهانی می‌پردازد.
🔹
کتاب با بررسی عرصه‌های مختلف سیاسی، اقتصادی، کریدور، انرژی، فناوری، جمعیت و سرمایه انسانی و دینی، زیست‌محیطی، مدیریت دیتا، نظامی، زنجیره‌های تأمین، چالش شناختی/بردگی ذهنی و نبرد رؤیاهای ملی چهارچوبی از تغییر نظم گذشته و عرصه‌های محل نزاع برای شکل دادن نظم جدید جهانی را معرفی میکند.
🔹
کتاب با بررسی ایده‌های رهبر شهید انقلاب در این‌باره و ضرورت‌ها و لوازم نقش‌آفرینی در آن، تلاش کرده مهم‌ترین عرصه‌های محل نزاع که مسئولان و جوانان و...باید نسبت به آن حساسیت داشته باشند طرح کند.
🔹
پیش از این کتاب‌های خودسازی و دیگرسازی، کدام  انتظار؟ انتظار انقلابی یا انحرافی و تشکل دهه پیشرفت  از همین نگارنده منتشر شده بود.
🔗
این کتاب را می‌تواید از
اینجا
تهیه کنید.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/465560" target="_blank">📅 22:48 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465559">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOTxxe5s8UMQdFmOd_NavedvljN8UTXnt6Fmy4NfjBq20aHvxS8_k4IWgm81zKRkZk0BNKUhhVUW8CVtkXElwb8Z55IdG1dP1OsoyspLJvyzmfe1vMl4ie4pohxbqM2t-Io_Fkp8ODUErVBc4JIV1vNafFZg9y3Np074Fbg_bBxE4p7e9XnwrmdVLI9GWZTJz9T11AFiwcoYm5nmOm8OKBHCbbV0IXrDSuLXMElFHwVvX8nCDqFRLKlZkHlfDzAhYlGLe1qZgCC0yVRXTdOJCEbm77T2AJiu3SfXYwUHYeF__buj98lmbNgZUyeNjowV8WalyoPJp9lsZmyVB_VDRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاور امنیت ملی پیشین آمریکا: ایران تسلیم نمی‌شود
🔹
سالیوان، مشاور امنیت ملی پیشین آمریکا: تهران تسلیم نخواهد شد و ادامه وضعیت موجود، ضمن بی‌ثبات نگه داشتن شرایط، هزینه سنگینی برای آمریکا به همراه دارد.
🔹
باید این جنگ را پایان دهیم، دور آن خط بکشیم و بعد ببینیم چگونه می‌توانیم راهبردی را برای پیشبرد دوباره منافع آمریکا تدوین کنیم.
🔹
می‌دانم که اکنون نفت بیشتری خارج می‌شود و می‌دانم که ما عملاً نفت ایران را محاصره کرده‌ایم. اما معتقدم این شاخص‌های سطحی، چالش اساسی را حل نمی‌کنند. چالشی که این است که ایران تسلیم نخواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/465559" target="_blank">📅 22:36 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465558">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fb259f096.mp4?token=sJd7OxLoCqDxouAW22KiX75d_DaO6evPvX6k9roPlKorOhFMJLoDzKrsPvw-nVO7ZpTh0gAxYgpBRGhMp82loM-vOLQ_zjAhqzfflns4mFG11fl6RYV48EhpZw1kq8i0KB_wI6h3v_jG1qXOjrV4McBwLMCzIL6xlBhUlRWazY8LEjMvfyKzRqGpp2Yy03doIpj8SFjxQOTofgEUT8HKPpL4D_yVfqUDXaqB2XtzoZEBtG1dp4OFiEchKdRECp1CntiN6Uy1NSiX_faI1_9Ci3X-bkyGUdyvSXYTrT-HXPOwG9GvPKD3gdk8KrG2hH1BtjDnWYaB_nU4hGEzotWPeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fb259f096.mp4?token=sJd7OxLoCqDxouAW22KiX75d_DaO6evPvX6k9roPlKorOhFMJLoDzKrsPvw-nVO7ZpTh0gAxYgpBRGhMp82loM-vOLQ_zjAhqzfflns4mFG11fl6RYV48EhpZw1kq8i0KB_wI6h3v_jG1qXOjrV4McBwLMCzIL6xlBhUlRWazY8LEjMvfyKzRqGpp2Yy03doIpj8SFjxQOTofgEUT8HKPpL4D_yVfqUDXaqB2XtzoZEBtG1dp4OFiEchKdRECp1CntiN6Uy1NSiX_faI1_9Ci3X-bkyGUdyvSXYTrT-HXPOwG9GvPKD3gdk8KrG2hH1BtjDnWYaB_nU4hGEzotWPeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار نقدی: مردم آمریکا فکر کنند که چه چیزی باعث شده ۴۸ سال آمریکا و رژیم صهیونیستی از ما شکست بخورند؟
🔹
آمریکا که بودجهٔ نظامی‌اش ۱۰۰ برابر بیشتر از ماست و رژیم صهیونیستی که مدعی قدرت چهارم جهان است، چرا با این همه امکانات شکست خورده است. @Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/465558" target="_blank">📅 22:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465557">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46b9c1b7bd.mp4?token=JPMKcCGK__JZ9YBtRPrPvPhh9qF_SB6O6gVCiBwPJTfMrgZHxr5PcSikn0IOg5T6eSm3oVc7HaT5anYebZNrciZ84fUma4EsRY7MPjmGZla18umJ3kx4K43YjgU_79HpdQtyo-8EFB0PJYKFCk_lll75wsBg4U6c7E_-lclKngpdzboQBeUWwMpaqIl8kQRjxi_KfEw1RJZXZqK1booSYykvZ-RCDDrYSWAivJvWIUWrPNyBEQzXFJnnzxApwGZ3nt1MrZKO6vGffzo0Ww4hQCfzJZG9V5LcwR_MpjIDEYdnPCNJrJYUX7_X-mhKXZburQSJxxzxy2qkUX8a_-aQyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46b9c1b7bd.mp4?token=JPMKcCGK__JZ9YBtRPrPvPhh9qF_SB6O6gVCiBwPJTfMrgZHxr5PcSikn0IOg5T6eSm3oVc7HaT5anYebZNrciZ84fUma4EsRY7MPjmGZla18umJ3kx4K43YjgU_79HpdQtyo-8EFB0PJYKFCk_lll75wsBg4U6c7E_-lclKngpdzboQBeUWwMpaqIl8kQRjxi_KfEw1RJZXZqK1booSYykvZ-RCDDrYSWAivJvWIUWrPNyBEQzXFJnnzxApwGZ3nt1MrZKO6vGffzo0Ww4hQCfzJZG9V5LcwR_MpjIDEYdnPCNJrJYUX7_X-mhKXZburQSJxxzxy2qkUX8a_-aQyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔹
بنا به اعلام برخی منابع رسانه‌ای، تصاویر فوق مربوط به انفجار خط لولهٔ گاز به فرودگاه حرارتی تشرین در نزدیکی فرودگاه بین‌المللی دمشق است‌. @Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/465557" target="_blank">📅 22:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465556">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🎥
منابع عربی از وقوع انفجار در فرودگاه بین‌المللی دمشق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/465556" target="_blank">📅 22:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465555">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f525e09ca4.mp4?token=XWIGFhNEdkAP1F-jJmn93889BpQJcaFN5raDGLzL2nsd2Ov5bGJ4qnIf1gh5tPvuouiNo5sJv8qAEsX4fE6ZyIyyVg1F0nOFVUF2J7WRrpfgXS5GXjxNf7KYOkeRhdcjJde7tdBzqUsaaYAga89MTC-HJlsHeKsEvGTOxQUyawGI-Vt2U5afKFmVerbjxTS9W3YKpEDsRCXjEbDwzT1ewkRzA3-pLmKIp9m-zEimiSm7jLAQz5BaVXQw33CPC8g0p_7YbfW4ADdiAEPBR8uXEWWOXfH-CKlLVLsm3YMXRsSnN71v7KLLOTsIPjMB3KtBkk015qThRuSUy0VCVq2L8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f525e09ca4.mp4?token=XWIGFhNEdkAP1F-jJmn93889BpQJcaFN5raDGLzL2nsd2Ov5bGJ4qnIf1gh5tPvuouiNo5sJv8qAEsX4fE6ZyIyyVg1F0nOFVUF2J7WRrpfgXS5GXjxNf7KYOkeRhdcjJde7tdBzqUsaaYAga89MTC-HJlsHeKsEvGTOxQUyawGI-Vt2U5afKFmVerbjxTS9W3YKpEDsRCXjEbDwzT1ewkRzA3-pLmKIp9m-zEimiSm7jLAQz5BaVXQw33CPC8g0p_7YbfW4ADdiAEPBR8uXEWWOXfH-CKlLVLsm3YMXRsSnN71v7KLLOTsIPjMB3KtBkk015qThRuSUy0VCVq2L8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار نقدی: مردم آمریکا فکر کنند که چه چیزی باعث شده ۴۸ سال آمریکا و رژیم صهیونیستی از ما شکست بخورند؟
🔹
آمریکا که بودجهٔ نظامی‌اش ۱۰۰ برابر بیشتر از ماست و رژیم صهیونیستی که مدعی قدرت چهارم جهان است، چرا با این همه امکانات شکست خورده است.
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/465555" target="_blank">📅 22:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465554">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پیام رهبر انقلاب به سی‌وسومین اجلاس سراسری نماز، صبح فردا همزمان با قرائت در محل برگزاری این اجلاس در حرم مطهر رضوی، منتشر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/465554" target="_blank">📅 22:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465553">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11a3b4e4b7.mp4?token=gNewoZ-nZ6hKVdghEGQy_L56Ey6udfdfN_QgJeCySypxa2ZRmCrG7eT5qhJuk3l4jTPwyzpQ1TXurkzZi89DyqDhwVFaj4joIdu8ODHp_l3h8PimVyljOWJXgkCXofdaLLA-66A2i90J_96M_C6uVPXfHPsjTXTJW9XwnwZKZOVP_5RMUG3Ts-MkMtKXJH_ydq8_ygTtyKcDIUdM5FzVt4l6C0szw6-zhpMkNEb3xLLMR3hiZxgSj4qCs0qsjH8nMIa5yuylgHwlWoehxUm5o1PS8Zq1E-dLTFgqd9w6C-0GasQeE2qru1h1g5p5nxtpJKReHVuDJVfGWsRf5g9Ryg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11a3b4e4b7.mp4?token=gNewoZ-nZ6hKVdghEGQy_L56Ey6udfdfN_QgJeCySypxa2ZRmCrG7eT5qhJuk3l4jTPwyzpQ1TXurkzZi89DyqDhwVFaj4joIdu8ODHp_l3h8PimVyljOWJXgkCXofdaLLA-66A2i90J_96M_C6uVPXfHPsjTXTJW9XwnwZKZOVP_5RMUG3Ts-MkMtKXJH_ydq8_ygTtyKcDIUdM5FzVt4l6C0szw6-zhpMkNEb3xLLMR3hiZxgSj4qCs0qsjH8nMIa5yuylgHwlWoehxUm5o1PS8Zq1E-dLTFgqd9w6C-0GasQeE2qru1h1g5p5nxtpJKReHVuDJVfGWsRf5g9Ryg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منابع عربی از وقوع انفجار در فرودگاه بین‌المللی دمشق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/465553" target="_blank">📅 21:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465552">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd0fdb7957.mp4?token=i0bpyRzTezWT8vPnVeq5NT7dibEj5MaeFk6HkcXfrj9DrA-R4zkmbgpFzrAj15m5i3rwjQGfD7y1aGY3VmBNbNG9uGJudo8J77fpJi7fN4nyKTHHbKAxNF3z2TxKTq-bfdtNcEPMYfwyst1nwUVaMwqgfwMKD93ej4GzrB7p2Ukzi0lYcceJtO20RVqfmHf2wtc1fC6y42UEdND7thJ8mzhd96AWI-BwG0pX63s6riaJUl3_FcxI4WAv9sJuTuad-LiNLF3fdkuD7Jkah2FlEnQ8xSlZmsJjI7_8AQmtF1WebmUEO5l90loRhLEYNDM-C6RTgYBmts-o53t2qgHAdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd0fdb7957.mp4?token=i0bpyRzTezWT8vPnVeq5NT7dibEj5MaeFk6HkcXfrj9DrA-R4zkmbgpFzrAj15m5i3rwjQGfD7y1aGY3VmBNbNG9uGJudo8J77fpJi7fN4nyKTHHbKAxNF3z2TxKTq-bfdtNcEPMYfwyst1nwUVaMwqgfwMKD93ej4GzrB7p2Ukzi0lYcceJtO20RVqfmHf2wtc1fC6y42UEdND7thJ8mzhd96AWI-BwG0pX63s6riaJUl3_FcxI4WAv9sJuTuad-LiNLF3fdkuD7Jkah2FlEnQ8xSlZmsJjI7_8AQmtF1WebmUEO5l90loRhLEYNDM-C6RTgYBmts-o53t2qgHAdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: الزیدی شانس نداشت با حمایت من نخست‌وزیر عراق شد
🔹
رئیس‌جمهور آمریکا: مهم‌تر از همه اینکه ما عراق را ترک می‌کنیم، در حالی که این کشور نخست‌وزیر جدید و فوق‌العاده‌ای به نام علی الزیدی دارد؛ مردی فوق‌العاده و دوست من که من از همان ابتدا از او حمایت کردم و حمایت کامل خود را از او اعلام کردم.
🔸
او در انتخابات نامزد شده بود، اما حتی فرصتی برای مطرح شدن به او داده نمی‌شد.
🔹
من در عرصه سیاسی تا حدی از او حمایت کردم و در نهایت، او با پیروزی‌ای قاطع، تقریباً به‌صورت یک پیروزی بزرگ، بر فردی غلبه کرد که از نظر من آدم خوبی نبود.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/465552" target="_blank">📅 21:51 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465551">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53baaadb89.mp4?token=W3uPnV5582Y2YpdjW_qZoEe8kXcCVPlQ2duT4oSztZrbOUrDu_r4ZyBnY9VWdWrSNk-d3fnfkCKIQga5-V7vO7Gyib4-XZnkC-uUGlktKLKiZ9pKYr810-f0cc7ikshWgNcU-hKy4ReWSZLbD9xNJyYxWtloYc4Q7URI66lnmIVKbJUB3LRl-eivY5DfrPTSDFzvQbUfs8Su03YIb0gOog5dADJzj5ku0o1EcsGQH_cEgpXm-ax2Iv58hQRBf8b2VSFYKt8csJxQrlcEbFAMNZRzfcnMdu7SOx40kvhFl9UEqtZ33OsSitEaDbIbSd3DgzFo0ujc4aleksjzBgy3AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53baaadb89.mp4?token=W3uPnV5582Y2YpdjW_qZoEe8kXcCVPlQ2duT4oSztZrbOUrDu_r4ZyBnY9VWdWrSNk-d3fnfkCKIQga5-V7vO7Gyib4-XZnkC-uUGlktKLKiZ9pKYr810-f0cc7ikshWgNcU-hKy4ReWSZLbD9xNJyYxWtloYc4Q7URI66lnmIVKbJUB3LRl-eivY5DfrPTSDFzvQbUfs8Su03YIb0gOog5dADJzj5ku0o1EcsGQH_cEgpXm-ax2Iv58hQRBf8b2VSFYKt8csJxQrlcEbFAMNZRzfcnMdu7SOx40kvhFl9UEqtZ33OsSitEaDbIbSd3DgzFo0ujc4aleksjzBgy3AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ما ۶ ماه است که در جنگ با ایران هستیم؛ آن‌ها ۴۵۰۰ کشته داشته‌اند و ما ۱۸ تا.
🔹
این ادعا درحالی مطرح شده که کارشناسان و ناظران اذعان دارند آمریکا آمار واقعی تلفات و خسارت‌های خود را به‌شدت سانسور می‌کند و اخبار آن را به‌صورت قطره‌چکانی و با پنهان‌کاری…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/465551" target="_blank">📅 21:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465550">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5977566b.mp4?token=MJqhY6JJSiUq8p32oVBkp3AU3bqlVCfzSekvTYUuiv7-uGxHf_aqQjLLQkOESdgt5TO5sz4mpMl9mknMmRznUQ7PiD7tpGNYfkWODYc5MsxyqWVKBLjP62w_sQQ7qGSh2yroWmjM5Lh6rpWejouLQPMCOvMCGosCtYcMPIlyDuY59pAEJb7QLv-_c7pl8MZLNo3NP-89YM_yBnkUZZkytyA9ZTl_MVAXSzw2JxEz-BRbt2nrtYXa2R-g0O69AOInkKDP5SYLkuN4TtG2uXr5vDndry14dp_gbX_rbkrd8cZxCoIBZyE7v3REdQgxsbYWtXf_FUPGnkt-pO0mW-AAKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5977566b.mp4?token=MJqhY6JJSiUq8p32oVBkp3AU3bqlVCfzSekvTYUuiv7-uGxHf_aqQjLLQkOESdgt5TO5sz4mpMl9mknMmRznUQ7PiD7tpGNYfkWODYc5MsxyqWVKBLjP62w_sQQ7qGSh2yroWmjM5Lh6rpWejouLQPMCOvMCGosCtYcMPIlyDuY59pAEJb7QLv-_c7pl8MZLNo3NP-89YM_yBnkUZZkytyA9ZTl_MVAXSzw2JxEz-BRbt2nrtYXa2R-g0O69AOInkKDP5SYLkuN4TtG2uXr5vDndry14dp_gbX_rbkrd8cZxCoIBZyE7v3REdQgxsbYWtXf_FUPGnkt-pO0mW-AAKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ما ۶ ماه است که در جنگ با ایران هستیم؛ آن‌ها ۴۵۰۰ کشته داشته‌اند و ما ۱۸ تا.
🔹
این ادعا درحالی مطرح شده که کارشناسان و ناظران اذعان دارند آمریکا آمار واقعی تلفات و خسارت‌های خود را به‌شدت سانسور می‌کند و اخبار آن را به‌صورت قطره‌چکانی و با پنهان‌کاری منتشر می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/465550" target="_blank">📅 21:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465549">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P51mb_P4X41CpgXKymsf1WzXv4zkzkkgsLjWvBWEIKSYXSkLB_2rLDVSmSnxHiNQOkW-7k2wPFmz7dqLUO0Uq2rUYAYl2rsQ8qFuCy9zC64SwKuHxMAkg1KvLT4uIliT0LwxDhZouXL10tCzv-KzQ5sKDR2IqZ4x_Qc5wZPVFgfl3aqRAzdfUvrKJVCV1a7-lFlBffXhFc_lmdVgEWQgvOkiZufVo7WbtZo3gOCYV_FLLeRjRZ9iV4EMVcczkHY9vcuhDYowopNIrRQaY-9PfFFWKGurndWBlkePCSLLl_RkH62XrYpGEefZqOIxDyOyoihIug-d1eYx077hDCwY6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف در پاسخ به گستاخی‌ اخیر بسنت فرمول اقتصادی جدیدی منتشر کرد؛ اهرم‌های فشار ایران بر اقتصاد آمریکا
🔹
محمدباقر قالیباف در پاسخ به لفاظی‌های اخیر اسکات بسنت وزیر خزانه‌داری آمریکا که مدعی فروپاشی اقتصاد ایران ظرف دو هفته آینده شده بود، توضیحاتی درباره اهرم‌های فشار ایران بر اقتصاد آمریکا ارائه کرد.
🔹
قالیباف در پست خود در حساب شخصی‌اش در شبکه ایکس در شرح وضعیت شکنندهٔ بسنت نوشت که دولت آمریکا در گذشته وام‌های زیادی با نرخ بهره نزدیک به صفر گرفته بود. حالا موعد پرداخت این وام‌ها رسیده و دولت مجبور است برای تسویه آن‌ها، دوباره وام‌های جدید با نرخ بهرهٔ بسیار بالاتر بگیرد.
🔹
از طرفی توان و ظرفیت خریداران اوراق قرضه هم پیوسته در حال کاهش است. برای مثال خریداران بزرگ اوراق قرضه آمریکا (مانند چین و ژاپن) علاقه کمتری به خرید اوراق جدید و یا نگه داشتن اوراق قبلی نشان می‌دهند و به همین دلیل نرخ بازده اوراق رو به افزایش است.
🔹
قالیباف به بسنت گوشزد کرده است که نقش ایران در بسته نگه داشتن تنگهٔ هرمز و بالا نگه داشتن قیمت انرژی و همچنین اثر‌گذاری بر افزایش بازده اوراق قرضه، خزانه‌داری آمریکا را با بحران فزاینده روبرو کرده و تمام دردسرهای او را تشدید ساخته است؛ به عبارتی آمریکایی‌ها تا حل این مسائل از طریق احترام به حقوق ملت ایران، توان غلبه بر این مشکلات اقتصادی را نخواهند داشت.
🔹
نرخ بهره اوراق ۳۰ ساله دولت امریکا روز گذشته به بالاترین نرخ از سال ۲۰۰۲ رسید و با روند فعلی احتمال برگشت به نرخ های سال‌های ۱۹۹۰ و قبل وجود دارد.
🔹
قالیباف همچنین در پست خود از تصویر David Zervos مشاور جدید بسنت که روز گذشته منصوب شده هم استفاده کرده است. او به زدن حرف‌های عجیب و غریب معروف است. برای مثال، او سالها پیش ادعا کرده بود که از اصلاح موی سر و صورت خود تا کاهش نرخ بهره توسط فدرال رزرو پرهیز خواهد کرد! انتصاب زروس به عنوان مشاور بسنت، دستمایهٔ طنز و استهزا توسط فعالان بازارهای مالی شده است.
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/465549" target="_blank">📅 21:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465548">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de7c192ff2.mp4?token=ge-m30W2Upqo3R0uQ6fTJmCulMHgucaZekITtt-fyhXdjtGdRAnzI7QGEbMww1BlGjHSu3KyY-hGj5OY5bCx12DpmVaZoCHeUTh7bKRB_A5-7Udi3RGd3A7pSXG1yAVUUsjRwBXw43jpJX5v5HW-yl6xunso_BVEdciJMYDd9thX1oEaW79nF2ghLSaP0pl1ASmou0N9TDqPHEp51Rv7gv1VZpu4naBs0j5Z9DHOu1DPqjVu9YCnRaPBgRyAcH3gsy52RUiePpEofGql9OHl2EK6AJCBpQhAG7ThZP5AbaaqL6D3ja4yOns-GRhrZ7qowHMVQcYb2pKjnmxn_-arnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de7c192ff2.mp4?token=ge-m30W2Upqo3R0uQ6fTJmCulMHgucaZekITtt-fyhXdjtGdRAnzI7QGEbMww1BlGjHSu3KyY-hGj5OY5bCx12DpmVaZoCHeUTh7bKRB_A5-7Udi3RGd3A7pSXG1yAVUUsjRwBXw43jpJX5v5HW-yl6xunso_BVEdciJMYDd9thX1oEaW79nF2ghLSaP0pl1ASmou0N9TDqPHEp51Rv7gv1VZpu4naBs0j5Z9DHOu1DPqjVu9YCnRaPBgRyAcH3gsy52RUiePpEofGql9OHl2EK6AJCBpQhAG7ThZP5AbaaqL6D3ja4yOns-GRhrZ7qowHMVQcYb2pKjnmxn_-arnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پهپادهای ایرانی؛ تلفیق مرگبار هوش مصنوعی، رادارگریزی و دانش بومی
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/465548" target="_blank">📅 21:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465547">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-mMJu6PeWHu6kRf4EgR4F0h_nVHkveyMMeNqn9LT5PyFJcq2YksSQPgIelV_AB52ItmFtYKXKgnVO64rM_R4M9MOirvm5YMt3HNyhsxA9GWT967n4VH9w0vxVYq28XAUbaO5ic2d3Vi_JFcPEqGr4wdEdPjE7er2AbdaG_09b_8GpNLwNTVEgNxqvsmrlaA7K01oNm7rO-N-SPaiwYeex3932la_cTmZ2c2DLn6l7AXurC_4gaDFxEba2vpVWXqIGDiItFbs238P_94K5qGeV1yE7He-ELkEUoxoC50RydcNA_TpWdTGtarX0awXtT207AdhUhLdYLRLvD5Gh_m7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا از عراق نرفت؛ فقط شکل حضورش را تغییر داد
🔹
با وجود ادعای پایان مأموریت ائتلاف آمریکایی در عراق، تداوم حضور نیروها، تجهیزات و همکاری‌های اطلاعاتی نشان می‌دهد واشنگتن صرفاً شکل حضور نظامی خود در این کشور را تغییر داده است.
🔸
علی الزیدی، نخست‌وزیر عراق،…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/465547" target="_blank">📅 21:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465546">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/481095a354.mp4?token=NvyB4LexxN9FNtvtOFkDDkKDgs2dkYJy4PRz4_sl312Zgjv8h0gI9S8VKdEKcXc4pu-Gm8bREGUqmVU7lvwsvTjYuUwwyDvBKqtWvNeUScf_WsmpD-ySfckFF9zyxllVGqWUIF4cO_Nn4T6sUJ0AjoovgLk3l_PnPCOzaxWT5yDpIGzqTDrvTDSLzBxVniJo43xvyq_535uO8MMAFiAeNyOCBSTXD7iMXqKQNA1RjVHCLqyK3JRvBzzmemB27N01HSxTpgAbz7sme1U2XutIYeOBJGX_suc4ZEIoJKN4qDYosvIL11A0M-GbZ2rWHNMqhR-VCm8uU6S57UJb914cpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/481095a354.mp4?token=NvyB4LexxN9FNtvtOFkDDkKDgs2dkYJy4PRz4_sl312Zgjv8h0gI9S8VKdEKcXc4pu-Gm8bREGUqmVU7lvwsvTjYuUwwyDvBKqtWvNeUScf_WsmpD-ySfckFF9zyxllVGqWUIF4cO_Nn4T6sUJ0AjoovgLk3l_PnPCOzaxWT5yDpIGzqTDrvTDSLzBxVniJo43xvyq_535uO8MMAFiAeNyOCBSTXD7iMXqKQNA1RjVHCLqyK3JRvBzzmemB27N01HSxTpgAbz7sme1U2XutIYeOBJGX_suc4ZEIoJKN4qDYosvIL11A0M-GbZ2rWHNMqhR-VCm8uU6S57UJb914cpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاسبان خون چگونه جاده‌صاف‌کنِ جنایت متجاوزان به ایران شدند؟
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/465546" target="_blank">📅 21:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465545">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01c793a1b7.mp4?token=Gk2ZFbZwPdDrOQUZ-5Gzs6_uJsO4xJpaQy7_WS1MIIOt_V7PLLymTaH42xeHMnArC2P_TgjWpcVp00I0tF746IURoQVhOViGjql7zfm97L6XelUUHvYORqrY1XVO3BH-7CuddyeLU1FSxDczP1CF28vxvW9tVkNOWHrTt3EqpQfhIV9fynCNPGiJAjAQULBm-h_DGYG3P4fbiK9bNOQ9qdulfuHjHE84LfQiR-lgE49gHL6xn27qRjkott_4ka2-7k6URkL-hyoXDP2BCcadXvrLh7R1u2a8iG9TDDVMHlQ31D85G-w5Oo2iG0B5yxZ0aTYnEdO-Q6oNHQ2P4RbnKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01c793a1b7.mp4?token=Gk2ZFbZwPdDrOQUZ-5Gzs6_uJsO4xJpaQy7_WS1MIIOt_V7PLLymTaH42xeHMnArC2P_TgjWpcVp00I0tF746IURoQVhOViGjql7zfm97L6XelUUHvYORqrY1XVO3BH-7CuddyeLU1FSxDczP1CF28vxvW9tVkNOWHrTt3EqpQfhIV9fynCNPGiJAjAQULBm-h_DGYG3P4fbiK9bNOQ9qdulfuHjHE84LfQiR-lgE49gHL6xn27qRjkott_4ka2-7k6URkL-hyoXDP2BCcadXvrLh7R1u2a8iG9TDDVMHlQ31D85G-w5Oo2iG0B5yxZ0aTYnEdO-Q6oNHQ2P4RbnKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منابع عراقی از هدف‌قرارگرفتن مقر گروهک‌های تجزیه‌طلب در کوی‌سنجقِ اربیل خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/465545" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465544">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c651ef6ac.mp4?token=Kzo7nHH51rmfr4Ritoo-mc2phWRGWtyAsgXwnz7ZFLtwywtM-Ophl9wUSDBnfb7975uz8Uv4g8Ro6NzS8SBwJKZdb_z3lTPogrfu0k4JPYONYQeaQ_WEQu_08h8MhYD5mprhNUQRoVgXQFfxNKfss24cSg7GG3H0goRRVVwi1RUKNH1yIX_bEkcOXzlQrk9B5quSFTClQAKvUWkgQqEoEqeAUYQLKMfX1l3bVFZjygpr1cgQZURn8SsmK9DRyn1lyYZUkfuanoXunIjl-JJNgpyfy2UsGA6Oz_JDvdlOCmelE3ta4jNQUDx3oj6knYn6uBc1aXtP51Kk0tiHKdslTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c651ef6ac.mp4?token=Kzo7nHH51rmfr4Ritoo-mc2phWRGWtyAsgXwnz7ZFLtwywtM-Ophl9wUSDBnfb7975uz8Uv4g8Ro6NzS8SBwJKZdb_z3lTPogrfu0k4JPYONYQeaQ_WEQu_08h8MhYD5mprhNUQRoVgXQFfxNKfss24cSg7GG3H0goRRVVwi1RUKNH1yIX_bEkcOXzlQrk9B5quSFTClQAKvUWkgQqEoEqeAUYQLKMfX1l3bVFZjygpr1cgQZURn8SsmK9DRyn1lyYZUkfuanoXunIjl-JJNgpyfy2UsGA6Oz_JDvdlOCmelE3ta4jNQUDx3oj6knYn6uBc1aXtP51Kk0tiHKdslTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعدام ۲ عامل شهادت نیروهای امنیتی در مشهد
🔹
علی همتی و مجید نیک‌اندیش، از عوامل میدانی اغتشاشات ۱۸ دی‌ماه ۱۴۰۴ در منطقه طبرسی مشهد که به شهادت ۴ نفر از نیروهای حافظ امنیت منجر شد، پس از تأیید حکم در دیوان عالی کشور و طی روال قانونی، بامداد امروز اعدام شدند.…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/465544" target="_blank">📅 21:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465543">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e50adff3b4.mp4?token=KnzstAetKE9lCAEPWzvlYPwdMGoIC0DNRGukchGrZ7HbbsB0sBmvPyt2gdibQuCV9LykAJSpZox6hn8qTo0hpIfhFHoqFENs5zcldGuLi64bAJLVx_KD0SS5cXyvVOgzqbryObxuSXf1Vpbc7BADHlP9B1SGWpHixSJqp3jO3JkGDRi_38hjDk9I7NJGFPx93A9bvHJFxQF1TAO1738bWnV8mRaQK45GyxOjNbJGkXOEAmEzmaLbTc9UMrk36mZDsXckN-YQc8p9uey-OcA1z3B9D9ztORPzadVg7Z3NRitvqLiyr-sobyK-dX-C0IEC0Gp6ajLnd7ljlhrZHoIfVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e50adff3b4.mp4?token=KnzstAetKE9lCAEPWzvlYPwdMGoIC0DNRGukchGrZ7HbbsB0sBmvPyt2gdibQuCV9LykAJSpZox6hn8qTo0hpIfhFHoqFENs5zcldGuLi64bAJLVx_KD0SS5cXyvVOgzqbryObxuSXf1Vpbc7BADHlP9B1SGWpHixSJqp3jO3JkGDRi_38hjDk9I7NJGFPx93A9bvHJFxQF1TAO1738bWnV8mRaQK45GyxOjNbJGkXOEAmEzmaLbTc9UMrk36mZDsXckN-YQc8p9uey-OcA1z3B9D9ztORPzadVg7Z3NRitvqLiyr-sobyK-dX-C0IEC0Gp6ajLnd7ljlhrZHoIfVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: گاهی به اشتباه گفته می‌شود که قاضی زن نداریم؛ درحالی‌که اکنون برخی بانوان قاضی هستند و رأی صادر می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/465543" target="_blank">📅 20:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465542">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/190e86fd1e.mp4?token=Mfr8FDRmtulQGTMDP_4LKpWV-8LkUKrziV_7r7s319NWv9BmWhLHE-ZFJMQ_XC7xMZHt3QHriHWAxew_AjYA2pD6A3iipV80_Ss_5D-G8o6YrQ9UXgDDgKwQJGzbVzVNE3TX-R5D6HfWVv7XeNUHNNFOKYELvKJA4LezYNNKyiliVTrJpBSw8iTNigWUSsPm1doBnZMHBy78pBFfeMb9YbGJD2a9bmOTgHJ0mpH9UVwMb1MI5l6fgWiSp9xT956c3ZVjPyoSB1DBW7CdBCiFZ7BztJtH2jvmlydu_OQaDycxLGBmP4XGI0E_374gDi3kaomcpDUDMK1EYpAkU7DttjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/190e86fd1e.mp4?token=Mfr8FDRmtulQGTMDP_4LKpWV-8LkUKrziV_7r7s319NWv9BmWhLHE-ZFJMQ_XC7xMZHt3QHriHWAxew_AjYA2pD6A3iipV80_Ss_5D-G8o6YrQ9UXgDDgKwQJGzbVzVNE3TX-R5D6HfWVv7XeNUHNNFOKYELvKJA4LezYNNKyiliVTrJpBSw8iTNigWUSsPm1doBnZMHBy78pBFfeMb9YbGJD2a9bmOTgHJ0mpH9UVwMb1MI5l6fgWiSp9xT956c3ZVjPyoSB1DBW7CdBCiFZ7BztJtH2jvmlydu_OQaDycxLGBmP4XGI0E_374gDi3kaomcpDUDMK1EYpAkU7DttjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شبی که خیابان‌ها روایتگرِ یک نامه شد
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/465542" target="_blank">📅 20:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465541">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7d25557e7.mp4?token=IwQUQyAzWnjunUV2PUygcUV1oatp3nPNUAxZYk-FtU9Aer2kOoUgrunpf6LsfGAZpv5AOnTiHlc49E9d_6BGgN5IZaMlDjH2rMUFvoCSbBo7MF52drmt6txiQUepjwp5oOuJKK_CfO2Ta8rSWImePDGKBGBjQEEDwEYfZuOq7QjagGNH7rPNHColRJUujaNHjIvciDffHny0Tt0ca94X85eUvi2NGuOZm_pDCcHd2MNusjrirQ9rdWtKsIst8HKW9R0iCPkopzz8z37OiIMDMLdYixjpF9SrzUgnCqltUPXpDQ9heF8e3-c_8aw38FCCoXYIJbBa1omN2gnDBlraNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7d25557e7.mp4?token=IwQUQyAzWnjunUV2PUygcUV1oatp3nPNUAxZYk-FtU9Aer2kOoUgrunpf6LsfGAZpv5AOnTiHlc49E9d_6BGgN5IZaMlDjH2rMUFvoCSbBo7MF52drmt6txiQUepjwp5oOuJKK_CfO2Ta8rSWImePDGKBGBjQEEDwEYfZuOq7QjagGNH7rPNHColRJUujaNHjIvciDffHny0Tt0ca94X85eUvi2NGuOZm_pDCcHd2MNusjrirQ9rdWtKsIst8HKW9R0iCPkopzz8z37OiIMDMLdYixjpF9SrzUgnCqltUPXpDQ9heF8e3-c_8aw38FCCoXYIJbBa1omN2gnDBlraNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر صمت: برخی قیمت‌ها در بازار اصلا قابل توجیه نیست؛ بازرسی‌ها متمرکز و شدیدتر می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/465541" target="_blank">📅 20:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465540">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJjr_bTzztG9faPJX8gXRH-bcRwBg98Y0Hf32m7LTrGVTFGyhke0MrVb1OJklHusumCxCHMXF8R7vIvXdyMW8W6mALLqjyMs2QW8QSuTv1dw4u8NtZVNZRKMSIM30ptMLur-FBzKSoAf8g9y0GPtSUpP1uvHudwuy1kIo-ILoVGZKn9sTEO-ZM2cGory-HEFVBFELqw_UpChBuGgs5rn_hrdXKuP9B_po3PnMG-y0GfMJaLftfNrkpMWeMb_HDtep8Pjp2dgmBIC41kMWriwX7zXxfIVrxZMHSjW62oWnu8iLWEpvU4_FNHs77_KYaxDL5KkjGTm4IgEbLuLby8eeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آژانس امنیت هوانوردی اروپا: آسمان ۶ کشور عربی خطرناک است
🔹
آژانس امنیت هوانوردی اروپا هشدار خود به شرکت‌های هواپیمایی را برای پرهیز از پرواز بر فراز آب‌های خلیج فارس در محدودهٔ بحرین، کویت، قطر، امارات، عمان و عربستان سعودی تا ۱۶ نوامبر تمدید کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/465540" target="_blank">📅 20:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465530">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tbyDCpbJNwoxK523Zpm90WKw9QV8_AbSZX59WvCdxKx9-PRcjmYHd0-QPEpTzcP3GDC-wPVZ_Uigo6Ja9Uz3vbemXdFq9FofPkVe3CQScUwxPfU1Wowf6ebybCn5vR9hCBkD0xEyNThh0Ci-3t2Wd4fBznELFrzP5Y16AJZeNgLx23miHUpq_-sc0bV8xNrhr77qrpxf6pXzqoZlxepl_97Ft6cvLSsduFSmiLpj6OLWV9S78forh7rJAXZiHxTsWQr5eVvvRl5opPXhA3CYw-DTdbjqcgBeyohswifnJZkO87Zn0wniGwi1SoV83Zv9El4XCfftY_S-ZHBKM9ZUBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nZZfs0s05Q3tvbwqh5hxxvsDvSxag2rQyefbyXYAQS-Bu8bc_FlRKBAw6L_R1r42m5Za8rhwAqDVZFP0A9w-KcxeLFe1KMTPdMDxGU4oxSbQzdzfCJnYO5fFsupUvT6uFWWTXo3KXR2vnR-v1M5Fbxh8vDinHKSEFGm9XvSP8Lk92KwPL053IgLTqvZwb9SDwh9-_4Ft-5edhXsYAOtTqSczrSs93KX8VPPLEGBLd7DPjkexbcYLdU3jva3lpIUMcPku6Gb0MSsq3FXFbcLGxtUKSjlyRx1UGFVuhhG1icHVI6aMlwDJDQhkUvHkJayVJFdO33jqbtZc0SrXqMbppQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VmFuDwqM3NLafiODIXUpBFEUerzfAUrg7NoIsOVAZrj03wBARnaXMmDy1iZ-0kW9cGrOo3FNbb5t-C4MqrWJkK1DI_N91agc6HlBaIaNLQUQai3jRGRHN4q5QHUokSlDfLiWQr6Y9tmYPJmCeHP52eDHZV7M3QA3CVUaeWqIIOFBWYzQuoDHnaEkVvWnbjjQD6lTsH-HdebJsr3VFuBoj_p7sJv7k_7gTxU5U5SuagkIQsSgYUdinlgrXvyTNQNXHF802jw3SAoxeeHYWTg6a8r9utfYisuJ0S1bWI8ArciDlDsOWM6CRRt9mgGHjGH74D3CN08gm01Z0pMAJobCig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nBwnhVpySWq96j3qPxA7yZ1Aije9Rm2xcfyLau8AoYaPWlb8A57rKFnf34o2c-XFhmLMDIXYni4WuVwtS5MtFCDE0y2m4fksdg63cCMLbpwURLLfdc8M834f8c8do07f7ChL_SibU7kfan8R_KfsqTjkGMrlekRI0ykJD8yT4UMZtC9fdQVtWfE9y0A0K43p19j3glsddOmvCrf9tpVBH5kgQBVfONCWLVjp7AR8LA1ozmdnPksbpUZm2BIPCrXcNqqX9le7QeFCFrd0ObqLY1BMB8OOebvHDEbJBBaXEWmlnvE0KVYimn69gVpKwB5JxYyBfdPG6c3I79lNm9S0pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hb2Qcj01HHGuKWw9YgKa1m6IFADU7IqHD81gYjNXRk_nrZ6Yl74oxsKLylk0Wt_A1WupUMiOw7Fd6n6jR9OT0CeGB4US1KfAiyx4lAUk2hqsvdo94NgzbsY5disaJXkYgO4OZBtg__ZGXH7iehWqKa5Ag0gr2e3A4IeuT0pWb5qoVrV5xmx-JHG3PLfLMlEROGiv97rSX0jbZBdQZr7bSeujoofm_YzhhymRDrk2sfx8nPXx0EPHw9lMI6oYJLsV3TRga6RP7i-hETNZVRsLQOFqc6lRklWUNXwDskmlFfu7oLsMko9kh_RxM72jw_g9pS4JSpVonbfZU6rgMAKKbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ln5dwVNpRRj-GGudR4J_6F4LTYCwjx2UuCOktjqHKBgqYa9pmiOV485ENxzAzMcgO2nl_nbE1TbxwRe0cIWlnEaagPU0_YeqJqpsnbckYDNP2GjqM9sVXVwHVL4hMnXrL5OOe79imz6edPnMd81h72AhJ2XgHYKN7pCEx7uaIWoWcwOxiBnQjlWnMH9bNjbsOOgEVxbds_QvWvwXRrynAjTiP84zBNFfGdwviY8xvV76i5Ru8zd0pTqe-HkMiFRs9roQDJtuBmd3W1bcy23h86cziAGmw7Wvxe_4JkNAJliiGTwphJJspy9THA2Q1erMvXT2o_08UU0VOuTpaBy12A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ab2h-oD7Iw8VVwUVLNe3AbF3vGlAD5EoyFYGdT1KUczHQ68IkW73IlEeIXpaoG1s1UpuSWh4eDdEnzhHnkciqWlVtDRWlbrCKHaGoHePrwhUY1TlcOTigfOj2Y1E4pRk9OyqoRsCk3cPbKr1kxJkfgfEZ4EcMmc2huSlVTE-bDa2fHJGfnVRNijTCTJuAJw7Jat9A-szI3l1yZjp_4E-2E4qOZ9_nYi69RkKRtOGr-ecQl-jFOuoVnWrmNZZkdPx36dLlRmcqVzYPcdYQTgLykmGvys8e8vwsweWbhpj2wyk-u_jKkGSMd1gLzY7oaWzKdx_8taTw9wwHxr2o4Tizg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VhfW-rt2ev1qd6zuICwbgORZCaACxK6RVISeC_u2yGXfR-6R2UQ9y-ApOmjYW54lbgimigkoDwq6OHEJVYnWa9tkV-_QP9ecxdFUmXaHJT182iHcK3pxS1DjByP54fkdVSqdII-GCsDv_1v4H3c-SjqbL-JWNvpf6c8_sZY_q_FsuNUBwKYyVwrmAjCUV-EckdDJN_3VRafHizKJrfoiDzq2k7uFVv-e7uTRRHdkWR_zTEHkBVzCrIshLkV_hdEtvReq-8TFBVTFcIpSqNT-qpHxF4BJBAVcm09fiDtRtkjOdlu5aLXiy18pVLui8GlR-y5lGULHY_8cf4ugtsTFTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fKaPCDKSeQ203Nnb6IG_nUK6ch9TW8TGl6zsJ4GCpvKE_cKA5mk36GDpgvr93YnUDld_6-Y2q6KnhoYRpAueCChG0LoxxLfMHP5zW96I4c4wm84Iq0118-qhGTkQDjR7rg81A5VZRdsxKNhfqNBrR2_F438k32fp-QxUO3UMvNLepuQNcyeyPGEQU_6xO1l6Vmkc7gGhcSTZV6AgXEal9g106PtfsrIlQSPfWm1qcSHzu7CmH4sscG-AmOXZbBNZv1Gw7LeI985Zp-6ItV54SenRtwOfuT7TMuDS4l-lWuCRJoamqK1jDB_3nxSNa2CfjtpU_TPFCd5yVjtV3DlL0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tln6NXZABIlpUJgpiUPGxHXjMcrubJgGGo1_Vh8KOTNnmwdHF02anX-z8ScYRJtOt1-3XQEN56tCCDm-gjMpEsFvFGRr9VC5r59spgQMFKXQGHOBMTle4Risxzzuz1JEIuHSDmPrzze0gKyazFhRRzGGcM6uXM3Vl4mNZyY5ADVCL8I6d5tKIfUDoA-fuKvO7EnlMLkHT8mbE3LmIAOk-QX_RONjEZtbHq8_3b8AUHENw-VFqHC-lv1Q5eENDHb4vACwSCWXgl4SiMynL1vzV2FoPJZTl1m6BjdQ35708c-6IdGH9VVF8V1lmBLICTm5YjgspZyH8yv5Fwx2YLywhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احمد ناطق‌نوری درگذشت
🔹
احمد ناطق‌نوری، رئیس اسبق فدراسیون بوکس و نمایندهٔ ۷ دورهٔ مجلس، بامداد امروز پس از سال‌ها تحمل بیماری، در ۸۹ سالگی درگذشت. @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/465530" target="_blank">📅 20:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465528">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2ZssaMzaEYGSE2k3vcFKZEKybHAH8WbZBZjGRiwHIAUeYZRVNY5ouKuUrvNm7gDSCFsv6xxoQV8LLbkGwXkT_8Ow2Wj9jaGAx_xYEOOOdXV9lqT6OUgqP6jdDZG5YzsE92g8gIlRhZO-TB5yoyrC_djX4l2JO38UHpR7hBIBEhD3J4xSDL67KZ5Z8s7fj1CmRpDMTlWBZ2FnNcYkoIbW_b64AH109HJ1ab3NC1P_Cte7Ixt2FxI4-CT-1XvdQjt_BU2ulvH3RTV98vHdIJKKRFApC3jXtf9ShCJ7XHXcf4XBCrRKHPLk2CalwbqXTHymh6A88u1taPuQYQ6SWaNqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگلیس پس‌از دو روز فرافکنی علیه ایران: بمبی در کار نبوده
🔹
پلیس مبارزه با تروریسم انگلیس اعلام کرد هیچ دستگاه انفجاری در نزدیکی محل استقرار نظامیان آمریکایی در انگلیس پیدا نشده است.
🔸
این در حالی است که پلیس انگلیس روز یکشنبه از وقوع یک حادثۀ بزرگ و احتمال…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/465528" target="_blank">📅 20:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465527">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbaf08f2a2.mp4?token=iAnZ6pbWF_cjAkBwnwpbpT9ULSrTOUH0F3sJYcwQowELOfcEs6QwA4LN-80E3L-OnkIgWWVwBbLdMqVnwWUoFoZAXPH6YiVVmpK9uum24JAQm3OkINPdA7Hxf7L8iXgt6vH6gDrulveigK9mw4SLC3w8FX_RPOiJLV-vRUikKstPoclTZbIhPIe0_wlR4SewBY3dapvZOV9aUzowaP-2RuNxjS0O_Fi8_dtupZWaXqGy7Z8cIV5ahBMnniTMWFby9o2uP8Acvp1SQfCFloef-SGej8UPHE4trLTqMnCZQYsh7rMIDejyW0gAk8TmGbYi-3_2hXKsVI7GjvV8TVg8OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbaf08f2a2.mp4?token=iAnZ6pbWF_cjAkBwnwpbpT9ULSrTOUH0F3sJYcwQowELOfcEs6QwA4LN-80E3L-OnkIgWWVwBbLdMqVnwWUoFoZAXPH6YiVVmpK9uum24JAQm3OkINPdA7Hxf7L8iXgt6vH6gDrulveigK9mw4SLC3w8FX_RPOiJLV-vRUikKstPoclTZbIhPIe0_wlR4SewBY3dapvZOV9aUzowaP-2RuNxjS0O_Fi8_dtupZWaXqGy7Z8cIV5ahBMnniTMWFby9o2uP8Acvp1SQfCFloef-SGej8UPHE4trLTqMnCZQYsh7rMIDejyW0gAk8TmGbYi-3_2hXKsVI7GjvV8TVg8OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر صمت: روند بازسازی واحدهای آسیب‌دیده سرعت خواهد گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/465527" target="_blank">📅 19:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465526">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‌ عربستان خلبان مهاجم پرواز دبی-تل‌آویو را بازداشت کرد
🔹
پس از فرود اضطراری پرواز فلای‌دبی در فرودگاه تبوک عربستان، مقامات سعودی خلبان متهم به حمله به همکارش را بازداشت و تحت بازجویی قرار دادند. @Farsna - Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/465526" target="_blank">📅 19:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465525">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6_CMrI4qdNGDGtUKxi0VbyDORjoEyJx9cUJMM4WvubzfR48QAnR5pnFnG6rQZdpqppM5ITTlTZ6Ez-5raLTOanZMmimSssi0cjf7ccRRhEWQLOVFOSWzx1Cf28RmzaWsPhI6UiJtIvkwpbdK7zhTWHsT_qxE6Y_CETS44j24I5L5W_44qeRLBzvbShvYE794xPvyRKPjkfapiQiraEBEyZIrdnECccuLTUam8hn236brLhwWTBD_CZ6852S4d59sxZSg8DaoyQdSQHqQlyixlgsucdy5qTnG871_fxStt4T1o24ulRGYCAHtC-WHiNzC_BPx29eIPLrv7RRcD34LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب کشاورزان شارژ شد
🔹
سازمان هدفمندسازی یارانه‌ها: ۴۱.۸ هزار میلیارد تومان به حساب گندمکاران کشور واریز شد.
🔹
این مرحله از پرداخت‌ها شامل کشاورزانی است که گندم خود را تا ۶ مهرماه به مراکز خرید تضمینی تحویل داده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/465525" target="_blank">📅 19:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465524">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd034e6117.mp4?token=kny9GU1Ty-F5BGrbqs2n1E-OpJ5PA7-Q2wfWeilB6blSMxLP8KL7pHGTjr5Yi6d9bAUwQLQCIkCOiX9yba8TowpZEIrjmc4G4BnfjjO27PHdtaBgX0s5UGK9oVUO32GLlhvtE3fQj_33Uttnq5Kti6UuYV5PMjwQwlqVK7J2CbXonameKrbUsK1Hbx3RnUS5JOR0tOPN_1Ep83gOr8pFJk0Y_O48sh8qlBk4CIR9gqoDEF3d7sItahi2GAHpdCiq3rNH9sX6TWiqfIhaFmwovV0PnAN78QGw0bFbHSli-aZFWGD5CSoT-S6O4zpcJYQa_yjTbQGUhYV4lZ_P70tCmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd034e6117.mp4?token=kny9GU1Ty-F5BGrbqs2n1E-OpJ5PA7-Q2wfWeilB6blSMxLP8KL7pHGTjr5Yi6d9bAUwQLQCIkCOiX9yba8TowpZEIrjmc4G4BnfjjO27PHdtaBgX0s5UGK9oVUO32GLlhvtE3fQj_33Uttnq5Kti6UuYV5PMjwQwlqVK7J2CbXonameKrbUsK1Hbx3RnUS5JOR0tOPN_1Ep83gOr8pFJk0Y_O48sh8qlBk4CIR9gqoDEF3d7sItahi2GAHpdCiq3rNH9sX6TWiqfIhaFmwovV0PnAN78QGw0bFbHSli-aZFWGD5CSoT-S6O4zpcJYQa_yjTbQGUhYV4lZ_P70tCmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جهش بی‌سابقهٔ قیمت سوخت در ترکیه
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/465524" target="_blank">📅 19:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465523">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تعطیلی معاملات شبانهٔ تتر در صرافی‌های دیجیتال
🔹
طبق اعلام صرافی‌های ارز دیجیتال، از چهارشنبه ۸ مهر تا یکشنبه ۱۲ مهر ۱۴۰۵، بازار تتر-تومان هر روز از ساعت ۹ تا ۲۱ فعالیت خواهد داشت.
🔹
همچنین در این مدت، سقف خرید روزانهٔ تتر برای هر کاربر ۲ هزار تتر تعیین شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/465523" target="_blank">📅 19:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465522">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e23998377d.mp4?token=eI-ZBWu31rDIen4QLl4ifapWosXhUIXDX-MFFZVkVVQRl9QNiW4XYR_XB65_dDbVBwi5g5R6H42GsWz_bQs1_9gfhV5KVHBrhsFjt0Sc40cw6I49hZCG88663rSRh1lJB-M5TEL9RlOeOdaiMranRX8JCf4dCz3oo10X9YnUzBF90XEIHowtoUqGYWc4NbBgVNRE3otlMri1YHaceZXycI7ih0_Mu0PlxXQ23DPdRon8LRNDIfLSYP2zbMmm6NVGtnfa1EjniKi2GI8xS6Q2u3Zp0AYQLWzsqLCWQMoUbzTSY709raojiosRYxTtptocCHTa_IlBZq63KKl_XnC6UjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e23998377d.mp4?token=eI-ZBWu31rDIen4QLl4ifapWosXhUIXDX-MFFZVkVVQRl9QNiW4XYR_XB65_dDbVBwi5g5R6H42GsWz_bQs1_9gfhV5KVHBrhsFjt0Sc40cw6I49hZCG88663rSRh1lJB-M5TEL9RlOeOdaiMranRX8JCf4dCz3oo10X9YnUzBF90XEIHowtoUqGYWc4NbBgVNRE3otlMri1YHaceZXycI7ih0_Mu0PlxXQ23DPdRon8LRNDIfLSYP2zbMmm6NVGtnfa1EjniKi2GI8xS6Q2u3Zp0AYQLWzsqLCWQMoUbzTSY709raojiosRYxTtptocCHTa_IlBZq63KKl_XnC6UjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وحشت اسرائیلی‌ها از این نقاشی‌های کودکان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/465522" target="_blank">📅 19:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465521">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b5d339493.mp4?token=FYs51i3wkghcOIHmWXwR8P8vSpbH638QsYojoJiwJp9tqJQmdvFd6h3laNPWhX3m9qRopkAK02wYA58G0OpQZfIt6sHy8rOzFB565LtQbypMH1MX-K47u0QMMQB1y2-C10XenISTEBp-pZFSx3oLnQk5G_33dBxlnOjWGjeVvShGXJ9C7XcJwjZp-EKsy_TJsC1U65Iyz_2Ny1Wbb4U2VvpH9XmxB063c8gMYZ9VNLO5rzB5Fka-i3ylm6LcDogsOYJcVi4ZOpda-g8I2ROEQJmYwX1a5YdMWtnreuoSEZGC-iobbILD7M5eR-td5rV4udT5UK7iCpK77maQtVg3HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b5d339493.mp4?token=FYs51i3wkghcOIHmWXwR8P8vSpbH638QsYojoJiwJp9tqJQmdvFd6h3laNPWhX3m9qRopkAK02wYA58G0OpQZfIt6sHy8rOzFB565LtQbypMH1MX-K47u0QMMQB1y2-C10XenISTEBp-pZFSx3oLnQk5G_33dBxlnOjWGjeVvShGXJ9C7XcJwjZp-EKsy_TJsC1U65Iyz_2Ny1Wbb4U2VvpH9XmxB063c8gMYZ9VNLO5rzB5Fka-i3ylm6LcDogsOYJcVi4ZOpda-g8I2ROEQJmYwX1a5YdMWtnreuoSEZGC-iobbILD7M5eR-td5rV4udT5UK7iCpK77maQtVg3HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پزشکیان در مراسم ترحیم آیت‌الله شبیری زنجانی
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/465521" target="_blank">📅 18:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465520">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmamSXUbuU-ABTIx3t_BCyvXPQOXUlRhXmiq03OR93hmwBy5rkkBUl5cL0w2O7aE-G_xpsBaIuVnsyUhVL5VdLqO0kbCZ7JTrlaKVmwr15lmco2gsUY4-bsipBHXcI7v21Qv3pabSIOZ1Jm_P7Fa-RU81c-5lEEdGh5Mr8Z_TcoUnIAFpohNutUtHCgH2ypkxe92rRc8CRF52qaJlZAdLL5nut55A4e6RPPgPaBFqFYfHHFffyjPG63EPwmE8emYPUUUHrkU88chdHsqDBllFSMXFIPNf8cm9X91YmXFbz4a8mnEJUW8Jyxn9tojy7NJIgNJl3zkscerp5AhBEw06A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا از عراق نرفت؛ فقط شکل حضورش را تغییر داد
🔹
با وجود ادعای پایان مأموریت ائتلاف آمریکایی در عراق، تداوم حضور نیروها، تجهیزات و همکاری‌های اطلاعاتی نشان می‌دهد واشنگتن صرفاً شکل حضور نظامی خود در این کشور را تغییر داده است.
🔸
علی الزیدی، نخست‌وزیر عراق، که این روزها در پازل آمریکا بازی می‌کند، نیز گفته است: «با تثبیت کنترل نیروهای امنیتی بر وضعیت امنیتی کشور، مأموریت ائتلاف بین‌المللی تحت امر آمریکا در عراق به پایان رسیده و مرحله جدیدی با محوریت حاکمیت عراق آغاز شده است.»
🔹
هم‌زمان با انتشار چنین ادعاهایی، نشریه آمریکایی وال‌استریت ژورنال گزارش داد که «تعدادی از سامانه‌های پدافندی و تفنگداران آمریکایی در عراق باقی می‌مانند.» این نشریه به نقل از یک مقام آگاه در پنتاگون نوشت: «آمریکا قابلیت‌های اطلاعاتی و شناسایی خود را که می‌تواند در داخل عراق مورد استفاده قرار گیرد، حفظ خواهد کرد.»
🔸
شیخ علی الاسدی، رئیس شورای سیاسی جنبش نجباء، نیز روز گذشته گفته بود: «این اقدام آمریکایی‌ها مشکوک است و آن‌ها شرکت‌های امنیتی دارند که برای جبران عقب‌نشینی نظامی آمریکا وارد شده‌اند.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/465520" target="_blank">📅 18:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465519">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XK5uKzn3RxnJA60tQ0fQCPSAwgwbPOJB1TzWwojuF-maqHvkAa6lxTrV2UO3w7tNoZc19DbBHaz5zi7Jr8C-ru-4lQKff4uLAfE8vunSI-T9GB2rnNIR-hIWmI5hEUAOe03ESZ1o8VO-UaRauwurxDAXRO0ZjkdqtUnxvyfl_qDdQSYys5f8ZhtjVpCLeySnl0na7LYTn60F7gr7Np8UK4aluhlhJjDIwNssMn4KuAYhTCBd9mektGXUXI-xP3nofZWngGNvVOY6lal_sBk70_W6Iw49G8Qsa1ykd4fIxh6xTPtFw7Ztcds1xYeMl6aoUVJ1MdYqFQUi-MBhM8T6Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وام برای خرید طلا و دلار ممنوع شد
🔹
بانک مرکزی: اعطای وام برای خرید طلا، ارز و رمزارز ممنوع است و این ممنوعیت شامل تسهیلات مستقیم و غیرمستقیم بانک‌ها و واحدهای دیجیتال نیز می‌شود.
🔹
بانک‌ها باید متقاضیان وام را اعتبارسنجی کنند و منابع بانکی را بیشتر به بنگاه‌های اقتصادی مولد اختصاص دهند و بر نحوه مصرف وام نظارت داشته باشند.
🔹
در صورت انحراف وام از هدف تعیین‌شده یا تخلف، مدیران و کارکنان مسئول به مراجع انتظامی، نظارتی و قضایی معرفی خواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/465519" target="_blank">📅 18:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465518">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۴۱.pdf</div>
  <div class="tg-doc-extra">2.8 MB</div>
</div>
<a href="https://t.me/farsna/465518" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۴۰.pdf</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/465518" target="_blank">📅 18:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465517">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دعوای دو خلبان پرواز امارات به اسرائیل را نیمه‌تمام گذاشت!
🔹
رسانه‌های صهیونیستی گزارش کردند که پرواز امارات به‌مقصد تل‌آویو در میانهٔ مسیر کد اضطراری ارسال کرده و در فرودگاه تبوک عربستان به‌زمین نشسته است.
🔹
به‌ادعای کانال ۱۲ رژیم صهیونیستی، علت این حادثه…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/465517" target="_blank">📅 17:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465516">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نتانیاهو با دعوت رئیس امارات به این کشور سفر کرده بود
🔸
دفتر نخست‌وزیری رژیم صهیونیستی در بیانیه‌ای گفت که نتانیاهو به دعوت رئیس امارات، به این کشور رفته بود.
🔹
در این بیانیه آمده، این دیدار بر تقویت روابط دوجانبه و چالش‌های منطقه‌ای متمرکز بود. رئیس شورای…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/465516" target="_blank">📅 17:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465515">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfkWnLX6SKIIPQUx41aGdaaLvbXVN0IJMRuXW58FL3zIeSUc7SiZZUlEytz_BpsevceWh_vGKl8GElgpZ5TVdeTRdDFJqTFVclCxnHITOWBGr8WGxjTQw3G1n08W-j44a-BmyeHu9_HpYKNgq4_1yS0-mvIyrlu63N_IKnThxCmb86t29Ww4dA7CPeR6fPXksW5FwzOMd-kaFgOaS4107zor1_t1ZKEJDUmOPjS0t6LPKMESHUOtOIwFeGl4bJDqD_FBE1NUwsd22fYi0G56bp8SahmktLTE__hHRK7bahqgb6spiV7-A6QFtmuwOWAaoHqqQzHMVCH8YRAfpUs5qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
یمن ۳ مخزن ال‌ان‌اجی آرامکو را منفجر کرد
🔹
تصاویر ماهواره‌ای اثرات انفجار در تاسیسات گاز طبیعی مایع‌شده (LNG) آرامکوی عربستان در ینبع، در فاصلهٔ زمانی ۲۵ تا ۲۷ سپتامبر یعنی ۳ تا ۵ مهر را نشان می‌دهد.
🔹
در این تصاویر چند مخزن ذخیره‌سازی آرامکو در ینبع منفجر…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/465515" target="_blank">📅 17:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465514">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F63PsHY6uuzZPPK6Js2WtMUwZFEG99oWrLUAmvG9MZHxNKJ_UpzA_F1u7CNb_ALYNfDytDsGUyden7aqvj_SrR0i18be0BpJrg3jwx9-AKc79nupcKk4ACMGXrXV1_8w6YdADAgJCT7BkMA3zCQpqaZS5p6_4k87bTaRKjog6VhoRLccALGnvvH1Q8u_Byeb8lIFOMPDxEVQ45WhWDf-hA3hHgrsID2Bl_DsTbCS5i2IgjspPnKz5JE_hekbO9o7qcRemDhCraqDnhYRR8r5FidGrIufeQ8oNETMgXNzZ7HmfvkFyaQ4wZuGn2S4esqsd0rAX7Uaa4H8xCUOlz3_rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ماکرون: اگر انگلیسی‌ها بخواهند به اتحادیۀ اروپا برگردند، این هم برای کشور خودشان و هم برای اروپایی‌ها خبر بسیار خوبی خواهد بود.  @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/465514" target="_blank">📅 17:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465513">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_5Q3yiFe898ddUWjZeS7a2XryjzFdX_YdBCI_q4REep2B6dFV1xNtpUNdbN67j1FoKFC4K7jhw43WBeNblkuD9Igu5C1wagLga3H_PaIBgdF-j34T7WjQPf0XvfGLwFweAVDFF8GfGyDPTYiSqRYzc9YWnVFxze6h5ViAgecFf1YP9mVVDrGZJKIi-MHwTpKlo2NKjgX_gQQEhuzQlFQPZkVfdpdr5fiC2pzhAt2qFi5MB2_WQzYNFiqsoXT4jNa0snoDEbAe0WkRenzidR69eFmlAqzznFk96wvZL00jpCP3hhzn5DiZNIBi1kE64SUpmNPiAGRqL2YUXbFANdtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرضهٔ ۲ میلیارد دلار اسکناس به بازار ارز
🔹
بانک مرکزی: عرضهٔ ۲ میلیارد دلار اسکناس برنامه‌ریزی شده که فروش یک میلیارد دلار آن از امروز از طریق شعب منتخب بانک‌ها و صرافی‌های بانکی آغاز می‌شود.
🔹
تمامی افراد بالای ۱۸ سال می‌توانند با ارائهٔ کارت ملی، تا سقف…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/465513" target="_blank">📅 17:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465512">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bd68e1dd1.mp4?token=F2juKH7zo6rtfit7P9INs0Bl3pE6cFA6W6OQref3zq0GqH0-S5h83OdlyuR7BvYsPlOykNmzPWPDurBXkezMYd_41Iaj30ZVdyH4ruTcTUKVvTfSzDhbLkjJaowve6OSlXqKPB28z28ozS3o2_AndGo_yFx84ByfnTrEqu_Z2lVHNpMIXuaQG5NPgZWRRlRHRurCm1lzG6Aa6ehgn19WbIR61zrCVOlPfdgsBO36FB5JfpA5ncilKbz4oPJ8jysZaZi-nrqGQJyo88Em4M6wpJtRk9ulls4fVnqOZz_by6P-nZ765UGje8fapAbh5XjYgcZbftB8lVWWt63BLAARJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bd68e1dd1.mp4?token=F2juKH7zo6rtfit7P9INs0Bl3pE6cFA6W6OQref3zq0GqH0-S5h83OdlyuR7BvYsPlOykNmzPWPDurBXkezMYd_41Iaj30ZVdyH4ruTcTUKVvTfSzDhbLkjJaowve6OSlXqKPB28z28ozS3o2_AndGo_yFx84ByfnTrEqu_Z2lVHNpMIXuaQG5NPgZWRRlRHRurCm1lzG6Aa6ehgn19WbIR61zrCVOlPfdgsBO36FB5JfpA5ncilKbz4oPJ8jysZaZi-nrqGQJyo88Em4M6wpJtRk9ulls4fVnqOZz_by6P-nZ765UGje8fapAbh5XjYgcZbftB8lVWWt63BLAARJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماکرون: اگر انگلیسی‌ها بخواهند به اتحادیۀ اروپا برگردند، این هم برای کشور خودشان و هم برای اروپایی‌ها خبر بسیار خوبی خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/465512" target="_blank">📅 16:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465511">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b20f2524b9.mp4?token=CJsPju8PZdHI5N8jVaXWGSabp_fmYRM9yVbguLXs6_cQbEpLOP8uLiWajLn-JQObV4TSQZ9wVV4MLSMuh9PYdgOZCvW57uCbo0tXIFEinjv8YADD9e8046bsfxCTI7JHLVK_HVG2m3Le5W7n_P9ISEz_aQmhBix04cszxXUpX8tJCq_eE5wMnDbACID2tOuvpw2avJFvyF2yK7rO65ZvKNuiJ7VWvGIRsDT1Kq0QIO_Nso9IExi9OCe4TKTMXN3owarZN6Kj9hJ8jMnF0oshlIl-r1v-hCbA1An99wEoE5UyercwYNEyJQ66sqvxW2yUDlbS0P266lhTle1qm4JzLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b20f2524b9.mp4?token=CJsPju8PZdHI5N8jVaXWGSabp_fmYRM9yVbguLXs6_cQbEpLOP8uLiWajLn-JQObV4TSQZ9wVV4MLSMuh9PYdgOZCvW57uCbo0tXIFEinjv8YADD9e8046bsfxCTI7JHLVK_HVG2m3Le5W7n_P9ISEz_aQmhBix04cszxXUpX8tJCq_eE5wMnDbACID2tOuvpw2avJFvyF2yK7rO65ZvKNuiJ7VWvGIRsDT1Kq0QIO_Nso9IExi9OCe4TKTMXN3owarZN6Kj9hJ8jMnF0oshlIl-r1v-hCbA1An99wEoE5UyercwYNEyJQ66sqvxW2yUDlbS0P266lhTle1qm4JzLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یمن ۳ مخزن ال‌ان‌اجی آرامکو را منفجر کرد
🔹
تصاویر ماهواره‌ای اثرات انفجار در تاسیسات گاز طبیعی مایع‌شده (LNG) آرامکوی عربستان در ینبع، در فاصلهٔ زمانی ۲۵ تا ۲۷ سپتامبر یعنی ۳ تا ۵ مهر را نشان می‌دهد.
🔹
در این تصاویر چند مخزن ذخیره‌سازی آرامکو در ینبع منفجر شده‌اند که شامل یک مخزن افقی، یک مخزن با سقف ثابت و یک مخزن کروی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/465511" target="_blank">📅 16:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465510">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس افغانستان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSIivA6ZxPh5aIXv4tglufrO3BxZq_B2NmfR-GRx9wojtI-YVnQTHe_3iC7nnIrCPZjLDPegnWT3b69ntbD1CZkce9JWk6_y4LipLYPDQSUwSOdCr9eq9wSY33wpzSnTUtW0rSamWvsCOUBns19kIO0c2E05INe4wTZmZ940S6nRXE3nmxwltHyTU3IWnAngkopk8Uk4RNDRhgUHOQBQxwDomiVrbUrgALomXbh06rE7104AG8wxl_VXxqBUPDApamozYtWmjPLH4uG3qb7cSF8MOTryTBB1IAYmhQg3xQxTcv3ohn49Cl-vw41w475FLdCxPdYh9G6kTwdZl2HW9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طالبان زیر بار تحریم هوایی ایران نرفت
🔸
طلوع نیوز افغانستان امروز چهارشنبه اعلام کرد که به‌رغم تحریم بخش هوایی از سوی آمریکا، طالبان به شرکتهای ایرانی اجازه پرواز به افغانستان را داده است.
🔸
چندی قبل وزارت خزانه‌داری آمریکا در بسته تحریمی جدید، ۲۷ شرکت هواپیمایی ایرانی را در فهرست تحریم‌ها قرار داده بود. به دنبال این تصمیم پروازهای ایران به کشورهای مختلف از جمله عراق، عمان و ... متوقف شده است.
@Farsnews_af
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/465510" target="_blank">📅 16:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465509">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30bd7bd1b4.mp4?token=BWOYhNsF1LKxkSXvGC8axMK6W1Y9W0XBM0kKzaDIHO4MkhA6BXpPjMd0w6AiQEUR6okJQsiHlrV_pkVwU-Ihjve1HDSYsaA-LoGHq0OFQwtA2I17CICnIjxfi5AALO6yHOLP9fV3TyLn6p2IBAMCv3iUWMtcYKuaoRuk0dpobifHFbvyLqXIubCNWQOeUCwA730DhDYfaCaXzI_swwMHRpY7avYDr1CEm5kIlGDVAyvE5vzYCBv5FGfII3m82evcT9LVY4YMk1Raux_ojxAZJj5a-7Au3_U_idllJ6trGAfOshf09WOA794Ckp8VQbLrb-HcOxLLAfMD_hLzGkf1ZGSPbj0ZUwl92qSBCOj5sn5il3bXipdO0GPd7Ki3y6ou2Ru-HLV5WhyPV-Qz2mla7Njo1-fbm0kJorSFVpVWk_2ncoqY4XqkDW-jLiOxMz1785JPKXtxGmFTUFy_9AIAa9ElUr4eM-euU4yHRlCVYREZZVGZnVX7EnL7KolkTNxHWfDRe-9O0fniOxEQLe9kEiVQmRwXgYfpAWrCtw80IjBNxAFq-YpwVj2WYzLtg-FxpXfHlYLIf3-xxcqZo8YhQnKhEIPP1qzcbENCV9HSwhGB7uzmJoPN0nsn81pflKKgeWAWX-mbg0uE3fc_zh-pUWjrBsaIqdT-aL5jG1LLLCs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30bd7bd1b4.mp4?token=BWOYhNsF1LKxkSXvGC8axMK6W1Y9W0XBM0kKzaDIHO4MkhA6BXpPjMd0w6AiQEUR6okJQsiHlrV_pkVwU-Ihjve1HDSYsaA-LoGHq0OFQwtA2I17CICnIjxfi5AALO6yHOLP9fV3TyLn6p2IBAMCv3iUWMtcYKuaoRuk0dpobifHFbvyLqXIubCNWQOeUCwA730DhDYfaCaXzI_swwMHRpY7avYDr1CEm5kIlGDVAyvE5vzYCBv5FGfII3m82evcT9LVY4YMk1Raux_ojxAZJj5a-7Au3_U_idllJ6trGAfOshf09WOA794Ckp8VQbLrb-HcOxLLAfMD_hLzGkf1ZGSPbj0ZUwl92qSBCOj5sn5il3bXipdO0GPd7Ki3y6ou2Ru-HLV5WhyPV-Qz2mla7Njo1-fbm0kJorSFVpVWk_2ncoqY4XqkDW-jLiOxMz1785JPKXtxGmFTUFy_9AIAa9ElUr4eM-euU4yHRlCVYREZZVGZnVX7EnL7KolkTNxHWfDRe-9O0fniOxEQLe9kEiVQmRwXgYfpAWrCtw80IjBNxAFq-YpwVj2WYzLtg-FxpXfHlYLIf3-xxcqZo8YhQnKhEIPP1qzcbENCV9HSwhGB7uzmJoPN0nsn81pflKKgeWAWX-mbg0uE3fc_zh-pUWjrBsaIqdT-aL5jG1LLLCs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نایب‌رئیس مجلس: مجلس تعطیل نیست
🔹
نیکزاد: فعالیت مجلس برای انجام وظایف ادامه دارد و نمایندگان تنها ۲ دیوار آن‌طرف‌تر از صحن، وظایف قانونی خود را دنبال می‌کنند.
🔹
در هر جلسۀ وبیناری مجلس حضوروغیاب انجام می‌شود و  اگر نماینده‌ای به سامانه متصل نشود، غایب محسوب…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/465509" target="_blank">📅 16:31 · 08 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

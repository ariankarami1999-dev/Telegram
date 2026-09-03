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
<img src="https://cdn4.telesco.pe/file/sqOqi7ycA3_O3W-g8bqXcDBYV9WhtsCc1LC6OAq0Vr4yyK573neshimRoCHvJP8Uu9P4-O5eppSRZhsGk2WTKIaDthYC5edQ4pyZ9OTsXwhuDZZ6JLv4b65i6lEguXeydHxeBYR1TRGLV2Jm-fJwNcsQ7rc9SRkWdQQSPRGi7Xjsm0kI0horbtk8LYgYRAsITBdzUV_4ffVuV0w9eqeAy9hPG1O69ZrxxJ6WNiEkSSsJitvn9_Pvq2p9wFkZO2p7oMxfrAGuy6lJcDI5_yDQ7FowLLYLrTaVgo0bxa80LiCzCCSxmh4OcHYmAvcA1CDuZHBFXutaDJ7VvY7vB-vVJQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 01:51:16</div>
<hr>

<div class="tg-post" id="msg-460025">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b9a5461d9.mp4?token=Y_qls0o9hHuH-UDF5T9fdRc3rnFlzkS7QjMbVAVCkz5n1EEHA7pEeHcHQk3PMZiydoP2-Sqj9MM2nRbk8HVviqu4-d_Yzz6r3qud95IOlVfr6N29aC0z1enpsEm2J3ZKZBUuXNgCETdJoQQLfOL0Zb2ZJ8FseOKUKJoZmG9NT-ZHdUPG-YH4lalf3ZE4huZCNa4jIc7ISneEotY9vFCcWBHLbSLkJOmovffMQBIxVoZGnGNfE2GBkuGxXE6d1Po0GbfP9O1SAfKUc_QdihUv_0pjADTQEMgr7Jrxek2U-HEjSLJ3URFGlXAoNI9DLPswoZEjxolNUoMeH8KXFgKpUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b9a5461d9.mp4?token=Y_qls0o9hHuH-UDF5T9fdRc3rnFlzkS7QjMbVAVCkz5n1EEHA7pEeHcHQk3PMZiydoP2-Sqj9MM2nRbk8HVviqu4-d_Yzz6r3qud95IOlVfr6N29aC0z1enpsEm2J3ZKZBUuXNgCETdJoQQLfOL0Zb2ZJ8FseOKUKJoZmG9NT-ZHdUPG-YH4lalf3ZE4huZCNa4jIc7ISneEotY9vFCcWBHLbSLkJOmovffMQBIxVoZGnGNfE2GBkuGxXE6d1Po0GbfP9O1SAfKUc_QdihUv_0pjADTQEMgr7Jrxek2U-HEjSLJ3URFGlXAoNI9DLPswoZEjxolNUoMeH8KXFgKpUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از تکثیر شهید سلیمانی وحشت دارند!
🔸
رهبر شهید انقلاب: امروز مستکبران از نام شهید سلیمانی وحشت دارند، ببینید در فضای مجازی با اسم او چه برخوردی دارند میکنند؛ از اسمش هم میترسند و از تکثیر او وحشت دارند.
@Farsna</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/farsna/460025" target="_blank">📅 01:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460024">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlDoWsP8HzB3lshrSQnHYj0yoT9nRIeXdU_4S2Kt45YRJBGm8Ni6mLk2iOVGVmJo1xrfD-3qCmXzABk4_ijLY-7VYRbtqwagbAKHVPec1Amf9wp4Yw0F-uD216pVM8P63nm36GInU1YQ5x3q05YMvB9huUMCp82x-0ffpokBcLU0hXBuGu3uwjC-Ox8mrMIwD2F_FB8YlIqv5HpxponHIZpcULJoxAc4OpCJAPJAmQZps5UG6SNqiS1-ujiXbOl73muz9XLMEg6eFaax83oYy2ink2ckoDH-4-fTDPWoXfE6db37E6gDAsaFTd5zXo74-d_yps47I-g562KuVLYCSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف مهمات جنگی سنگین در مرزهای سیستان‌و‌بلوچستان
🔹
جانشین فرماندهی مرزبانی سیستان‌وبلوچستان: در درگیری با قاچاقچیان مسلح، ۴ قبضه سلاح آرپی‌جی۷، ۶ گلوله آرپی‌جی ضدزره، ۶ خرج گلوله آرپی‌جی، ۲ هزار و ۳۸۲ فشنگ جنگی کلاش و ۷۹۶ فشنگ ام۴ کشف شد.
🔸
قاچاقچیان قصد داشتند این سلاح‌ها و مهمات را برای انجام اقدامات خرابکارانه و ایجاد ناامنی وارد کشور کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/farsna/460024" target="_blank">📅 01:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460023">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7c4a30d19.mp4?token=gjdOCXwSQlQg4MadEu-oJzBZ5GYZFJvyZlw9FU2Fp3O3KH5ocHMvl3oqWMPKh1moLxpecYe5zI4lOS9gUKDI700pCmWMgjVLQ3Vdoli_F-wO_taaKzFu_rRlZziKzmj0RWFMpTYU9nAsukqtSt7wlYDO81ttbnijMPr5R91fYaQtA9mCUZpJM6bmOGjPHxaIrq3EBVEsh5iiWMW47T3vLzk7L66XIQmqiYdFJG_D50X8CFOZTnrTqxYzbPFIaiKWVq3weF4zTKn7r5sXOcwoZgDl9QelCaBu_N9YLhPVGVxyCwh0Htc68z_bA4rXhICWkCJxvqVru5vk0_o4p9gGlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7c4a30d19.mp4?token=gjdOCXwSQlQg4MadEu-oJzBZ5GYZFJvyZlw9FU2Fp3O3KH5ocHMvl3oqWMPKh1moLxpecYe5zI4lOS9gUKDI700pCmWMgjVLQ3Vdoli_F-wO_taaKzFu_rRlZziKzmj0RWFMpTYU9nAsukqtSt7wlYDO81ttbnijMPr5R91fYaQtA9mCUZpJM6bmOGjPHxaIrq3EBVEsh5iiWMW47T3vLzk7L66XIQmqiYdFJG_D50X8CFOZTnrTqxYzbPFIaiKWVq3weF4zTKn7r5sXOcwoZgDl9QelCaBu_N9YLhPVGVxyCwh0Htc68z_bA4rXhICWkCJxvqVru5vk0_o4p9gGlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف ناخواستۀ ترامپ به عدم پیروزی در جنگ علیه ایران
🔹
رئیس‌جمهور آمریکا در ماه‌های گذشته بارها مدعی شد که در جنگ علیه ایران به پیروزی رسیده است.
🔹
با وجود این او در یک لغزش زبانی جمله‌ای بر سر زبان آورد که نشان می‌دهد که حتی خودش هم به ادعاهایش در این زمینه باور ندارد.
🔹
او در سخنانی دربارۀ جنگ علیه ایران ابتدا گفت «به محض اینکه به پیروزی برسیم» اما بلافاصله سخنش را عوض کرد و گفت: «همین الان پیروز شده‌ایم.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/farsna/460023" target="_blank">📅 00:54 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460022">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b56d43c04.mp4?token=WvNFrbiVXwIN3RrkyKIM45VneVtFNmWHkvKvneWhT9N_nT7rNCTb0Sqibcjq9FmYBMNbdy0rf_rPocN31TrLUs49wWu3UM50kZU5K6bayc_zZEQJV5RzdhJD6ACazKmdv-SmRWsLTbegxRlQpow-2C9LZDqDO8JvYvVFE4jWVwYsJEysCWA2d_XyCo75nJJl2a9VzaaC16nsdUU3dyrUVKs7VoexHa2gIpAKQKbt2LEpEKJm1BdyFw3imojra9qTqbng2zsrzhuLiD94FnaoW_qqrOp3zwt7gj03etukAEomYKlZnQFsPAyTfpZxvrE0J1UBs4RjzCjpcmxB8brFOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b56d43c04.mp4?token=WvNFrbiVXwIN3RrkyKIM45VneVtFNmWHkvKvneWhT9N_nT7rNCTb0Sqibcjq9FmYBMNbdy0rf_rPocN31TrLUs49wWu3UM50kZU5K6bayc_zZEQJV5RzdhJD6ACazKmdv-SmRWsLTbegxRlQpow-2C9LZDqDO8JvYvVFE4jWVwYsJEysCWA2d_XyCo75nJJl2a9VzaaC16nsdUU3dyrUVKs7VoexHa2gIpAKQKbt2LEpEKJm1BdyFw3imojra9qTqbng2zsrzhuLiD94FnaoW_qqrOp3zwt7gj03etukAEomYKlZnQFsPAyTfpZxvrE0J1UBs4RjzCjpcmxB8brFOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع مردم دزفول با خلبان شهید نیروی دریایی ارتش
◾️
شهید مجتبی باقری در حملات دوشب گذشتۀ دشمن آمریکایی به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farsna/460022" target="_blank">📅 00:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460021">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYTWK2pYm2Sl2yaGaNYkXZRmj3ay0BxwGtsJWTJ4Q3lnQzkwJ_eXbuOOrgzyH1Xb5nlVZdNCfHFofzCfN47QuAn3hwfngdyKtMfVrfXqOOb95PHBJHi-2tCaCPBAbUwfMBJd61-_g0fYVqSClNdoLoB_FnQKoBVh34EDgbb3EEl3zmYn9PYQrchJ3c_eTzDbP-Tcx6XGHxER9Us0RjZhUruxb_5X5zqp0PSpDTgqx52M-c4jWoZMJgrmC42e5XRLXYsPFV6Kn7euVrTcx0vXBLee5miKC_2PQNINj8tAgCV0e-U6U123U3JEUvGTEDgZSWflh-UD6uGIzl0vn9bHfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارن‌پالیسی: چین با ابزارهای قدرتمند خود، از فشار ترامپ علیه ایران هراسی ندارد
🔹
رسانۀ آمریکایی فارن‌پالیسی: چین با در اختیار داشتن ابزارهایی مانند امکان محدود کردن صادرات عناصر نادر خاکی به آمریکا، از فشار اقتصادی دولت ترامپ علیه تهران هراسی ندارد.
🔹
چین حتی می‌تواند در صورت هدف قرار گرفتن شرکت‌های چینی، واشنگتن را با اقدامات تلافی‌جویانه روبه‌رو کند.
🔗
شرح کامل خبر را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/460021" target="_blank">📅 00:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460020">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a8334da6f.mp4?token=HCuWUvZs-8dLQ9HV9YSJWKnpMNB11-YwW50JBher1nL4_RtVpA_OIcHgjQY-O2t41MzVreRxQzOoADctf14mVtpe6Vf29yr5TGOYFeQOlQRdjduBYfP0r3oy7zon0wN3jZ8kXwpcYDGMHUnEXQ8U4MHkT36HAmBdoWeleQhtckyEAcmn5CTqwmc7x-XwVwNtsqzrgrlHlZhtdQ_c8Sd-zmlFn3GqqNsI0vorhF0PwRLCU98auCN4g6ZlTgWBHvqGXqjHnuWkULKKp1MXC-UdZO2riELJWC2kESrqenTg8fHzKBqamm_N2nbiOuPATIzIFzlXg4ltvK0QEW7aXkv6FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a8334da6f.mp4?token=HCuWUvZs-8dLQ9HV9YSJWKnpMNB11-YwW50JBher1nL4_RtVpA_OIcHgjQY-O2t41MzVreRxQzOoADctf14mVtpe6Vf29yr5TGOYFeQOlQRdjduBYfP0r3oy7zon0wN3jZ8kXwpcYDGMHUnEXQ8U4MHkT36HAmBdoWeleQhtckyEAcmn5CTqwmc7x-XwVwNtsqzrgrlHlZhtdQ_c8Sd-zmlFn3GqqNsI0vorhF0PwRLCU98auCN4g6ZlTgWBHvqGXqjHnuWkULKKp1MXC-UdZO2riELJWC2kESrqenTg8fHzKBqamm_N2nbiOuPATIzIFzlXg4ltvK0QEW7aXkv6FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم نیشابور در قرار ۱۸۷ خیابان را ترک نکردند
@Farsna</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/460020" target="_blank">📅 00:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460019">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">حملات هوایی و توپخانه‌ای صهیونیست‌ها به جنوب لبنان
🔹
منابع لبنانی از ۳ حملهٔ هوایی رژیم صهیونیستی به شهرک المنصوری در جنوب لبنان خبر می‌دهند.
🔹
توپخانه ارتش رژیم صهیونیستی هم اطراف شهرک النبطیه الفوقا‌ و کفررمان را مورد هدف قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/460019" target="_blank">📅 23:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460018">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14cbc03b8f.mp4?token=qqtXrs4rZYIz9MPe0VvlpL5rONg4mBCLFWV7j_ibtzkDkYiKCBIz8hzWTdib_iXePkRIH4ncKo7PPLUgULBp1e1GCRAiwmfNcYV957_xbA8_1Gl9WzJye43Gq6YNWxz7U7e2z7AtHhzXGTeY1-nx1V153wnHTOzGwsCJR5FIv2Y36TO39_1ArXtBdKdADEtHAAt8BceZPRs5me3TG06yUbE9XFc27N4_124EjopFSkfKFXpgz_WtAo2p2fv-Ne3H9zPcvrT6jSbgeFdPmW5i89U_PZ-xg5sUQEfzjbW72GidkLJ4ts8YhCAi5W5AaNNIHNYJIMg4ZHr3nZNukXOD3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14cbc03b8f.mp4?token=qqtXrs4rZYIz9MPe0VvlpL5rONg4mBCLFWV7j_ibtzkDkYiKCBIz8hzWTdib_iXePkRIH4ncKo7PPLUgULBp1e1GCRAiwmfNcYV957_xbA8_1Gl9WzJye43Gq6YNWxz7U7e2z7AtHhzXGTeY1-nx1V153wnHTOzGwsCJR5FIv2Y36TO39_1ArXtBdKdADEtHAAt8BceZPRs5me3TG06yUbE9XFc27N4_124EjopFSkfKFXpgz_WtAo2p2fv-Ne3H9zPcvrT6jSbgeFdPmW5i89U_PZ-xg5sUQEfzjbW72GidkLJ4ts8YhCAi5W5AaNNIHNYJIMg4ZHr3nZNukXOD3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرایان خراسان‌جنوبی؛ ۱۸۷ شب، یک قرار و روایت ماندگار همدلی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/460018" target="_blank">📅 23:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460017">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🎥
بروجردی‌ها در شب ۱۸۷ همچنان باقوت در میدان ایستاده‌اند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/460017" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460016">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/le78mLpPwiU8_FeTjb8jb7c5440wUvNoPix5kTw3sZyrLZX3eTxQ7Le1BWCdUN-MnVS6rmkjFxS1_dotQiyO_DtBHFwbWDXB2erNCjq7RylYCH5TgRPCftTMNQgCY40m0wpKgG7Iq_Tje7igEiKORM6UTdgNT_Igmk95K1pdIh-yUZkOaq83hYfCiwbE9vMon10-wtDSNnD5FQYWyAj52w9jsqJdHUn5d84mEod5V0qHINam7wGtn24P0SSog5q0P7nkawwE5AvF7tUR9LTiaiyyXhIQN7PEkQlQPFrmxXmO1LCcmkKDt41Al_zwiV2dsfvwyKCmcBSPX0g0K4fR-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بقائی: برخلاف آمریکا، ضربات دفاعی ایران منحصرا علیه اهداف نظامی بوده است؛ گزارش رسمی قطر نیز اثبات‌کنندهٔ این واقعیت است..
🔹
سخنگوی وزارت امورخارجه، با اشاره به سند ثبت‌شده توسط قطر در اتحادیهٔ بین‌المللی ارتباطات راه دور (ITU) که در آن تاکید شده ضربات دفاعی ایران، فقط متوجه پایگاه‌های نظامی آمریکا بوده است، نوشت:
🔹
دولت قطر در سندی رسمی که به اتحادیه بین‌المللی ارتباطات (ITU) ارائه کرده، تأیید کرده است که حملات دفاعی ایران علیه نیروهای آمریکایی مستقر در خاک قطر منحصرا «متوجه تأسیسات نظامی آمریکا بوده است و هیچ منطقه غیرنظامی هدف قرار نگرفته است.
🔹
تنها استثنایی مورد ادعای قطر، حمله به یک تأسیسات گازی در ۱۸ مارس بوده است. اما در این مورد هم باید در نظر داسته باشیم که آن تأسیسات در آن زمان در خدمت عملیات‌های تجاوزکارانه آمریکا علیه ایران بود.
🔹
این واقعیت، یعنی دقت و مراقبت ایران در تعیین اهداف مورد حمله، را مقایسه کنید با عملکرد آمریکا در حملات مکرر به غیرنظامیان و اهداف غیرنظامی: مدارس، بیمارستان‌ها، مناطق مسکونی، مراسم عروسی، پل‌ها و موارد دیگر.
🔹
تفاوت عظیمی وجود دارد میان ملتی متمدن که اهمیت پایبندی به اصول اخلاقی و انسانی - حتی در دشوارترین شرایط - را آموخته است، و حاکمان جنگ‌طلبی که در قدرت‌نمایی‌های خود، هیچ اصل قانونی یا قاعده‌ اخلاقی را رعایت نمی‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/460016" target="_blank">📅 23:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460015">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pea59xaaP8HDmQ-YpEB1YZQCsaQPNO2NzLlNDq00oLBciA7DVxDizr9yMTJyAp53Qjg-r00LFo58sDwMSxKJtastNJlmeHz7jlyGUd0IKwrOk87XlVxrhff6jwu0PqAyrbCVROSBAn9fJxYVOgesQA0_PxIQ9sOT7WjNiTnh9jFywi01m-oXT5TRYeKec2BdbzyBdje1n5z8gah-zVTIRXCDIaPUJ7uopx2HKPp7z8gJe_og__Ak9Qfg2QvL9fYyIxi6hZodJlKyLWum56eiTZReZ0fc-7Ut2JY4acY4TPGbu2OgKk8quWURryHk94HbT87rKu8dykJMVLoszCRQMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اقدام جدید آمریکا علیه دانشگاه‌هایی که اسرائیل را تحریم کردند
🔹
گاردین: مجلس نمایندگان آمریکا روز پنج‌شنبه لایحه‌ای را علیه جنبش دانشگاهی بایکوت اسرائیل تصویب کرد.
🔹
براساس این لایحهٔ دانشگاه‌های شرکت‌کننده در بایکوت اسرائیل یا دانشگاه‌هایی که برای جلوگیری از شرکت دانشجویان در برنامه‌های تبادل دانشجو با رژیم صهیونیستی شرکت کرده‌اند، جریمه می‌شوند.
🔹
لایحه‌ی «حمایت از آزادی اقتصادی و دانشگاهی» با رأی ۲۳۷ بر ۱۶۹ به تصویب رسید، به‌طوری که ۳۳ دموکرات برخلاف هم‌حزبی‌هایشان به آن رأی مثبت دادند و تنها ۲ جمهوری‌خواه با آن مخالفت کردند.
🔹
در پی تجاوز نظامی رژیم صهیونیستی به نوار غزه، اعتراضات دانشجویی گسترده‌ای در آمریکا در محکومیت جنایات اسرائیل آغاز شد و دانشجویان تلاش کردند تا روابط دانشگاه‌های خود با اسرائیل را به حداقل برسانند.
@Farsna</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/farsna/460015" target="_blank">📅 23:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460014">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43137cc482.mp4?token=iXJDP4E_3M9k-mg2J0Uh624ULiu7PQYdCXw-DKP3mguaZHkr5VQ4-YsY7vMqLCnnRH2-wC5UJF_EAiFcqDSTRvbq22hhFdwqZcq5HO_MoUUvbsVmkFrtPTI7mWCyVx5SAoBhhNwutyN4_DWvwGOYfh3AjWB-IgDy_9-FNdNQ36EmKdGZjwyY-BN6HOxMbmjT1dz4JvogTGNBn3-QeRUEInSnNnDK4jC0oV5RDn2ocSMwRSPAQQCx5jB8JqHIwRQGtPE_Ep4Np0uF3IwN-OfEiPlFgt74K7AfAmJpIPhL4rQ__QZqfn3X6KCQo7sPh126fb7QazQ53KCfz8rPJdlz5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43137cc482.mp4?token=iXJDP4E_3M9k-mg2J0Uh624ULiu7PQYdCXw-DKP3mguaZHkr5VQ4-YsY7vMqLCnnRH2-wC5UJF_EAiFcqDSTRvbq22hhFdwqZcq5HO_MoUUvbsVmkFrtPTI7mWCyVx5SAoBhhNwutyN4_DWvwGOYfh3AjWB-IgDy_9-FNdNQ36EmKdGZjwyY-BN6HOxMbmjT1dz4JvogTGNBn3-QeRUEInSnNnDK4jC0oV5RDn2ocSMwRSPAQQCx5jB8JqHIwRQGtPE_Ep4Np0uF3IwN-OfEiPlFgt74K7AfAmJpIPhL4rQ__QZqfn3X6KCQo7sPh126fb7QazQ53KCfz8rPJdlz5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تشییع پیکر شهید حملهٔ آمریکا به سیریک  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/460014" target="_blank">📅 23:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460013">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtNAdmc6FoTmXePnpTwOEOHu4dtXWaQ5aTVpe0sVfth-pNBU7WtDcr-bZq9HxMeIkhWtiygBZ8vuoPbrQ3oi0QDKLdmj8pTbXlOj4ohYSbQG_zGT366FqgVLh6p95l1SRP6h9yIdcnOqSo2O2lN97VGhznP_SQ2u-sDIcXSirDPiLxMkG-gmntpe56eIMnFSgR0zdyGkFejRg46jkA-4GBi6BJrTcytDZvZxwSbDN7Z4jgCEwvuPF99VUhOCytY_NRwOVyWSYYCJqcIVhBLXzII-cxvKrjqgjq9uoemafLBz5iA2u1H-o28RynbuMYqOS64YcJR2WO325OaL3jXP7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشروی انصارالله در جبههٔ تعز و فرار مزدوران سعودی
🔹
منابع یمنی از وقوع درگیری‌های شدید میان نیروهای انصارالله و مزدوران وابسته به عربستان در محور تعز و در جبهه مقبته و ساحل غربی خبر می‌دهند.
🔹
براساس گزارش‌ها، نیروهای مسلح یمن(صنعاء) موفق به سیطره بر «مناطق راهبردی جدید» در استان تعز شده و به سمت بندر المخا در حال پیشروی هستند.
🔹
بر این اساس، ده‌ها مزدور سعودی از جمله فرماندهان رده‌ اول کشته و شماری نیز به همراه خانواده‌های خود پا به فرار گذاشته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/460013" target="_blank">📅 23:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460008">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dmz7v6-mvmmgF1QPZ5Lo42Zt2Oic6eevSStoYWNYstDUWA0KUp4gN0hQFWeF9ffRJjQBwWIjIoo84pDrD_vIIKdlwe_03Q9osiMuKiW4Lv9Tr8HIwH1wrYwLL6NeuQhIikD4a4tAE5Si5Msn8Bv3NBlp66LgU7d0wwrVkWTdEZlRpPyi7CscyYucJ_zTdsk0Ucs-gs-ymAPjNqLjiOS68fGlGCoqXXqDMBE-LIN7vX-oZKcFfdJgRPgW9LIrv6FGcp2gSsuv4sMz3BmD0pj5ZUlZip6wXiUl9FLapYxOa1klkjMz_TxdqpHitJ_de6uYI6JeH_FArWqQOMDw9KAMUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nhZEML7rS8JcRDpnz_hQiNNH3upzElBKFf9JJiGPxmJIITEt_8XA98ce-CCfIXTln0yrsfidIjmyHMAqLzJb2amRyZg-QZNAH-sn7UPLyut7TEC6lZLpMuLvKE75WD60kLv5KwmUyza_RrpjAK4GfCOsf_fNLQIeota9o4XBdFay6iM2CsJCh7a2R3RF05PrHTnHmpaZ8QCad1CazRbwY5ivvywyrQ0JPf35u9jrQFbePQ2BtwLYfKhX4Jxahk9k2N8r59GTbXaHTMSpLEwgP1E8u3jQUE17TxdmE2Ucl2U5dTO-U3SmFm6A426NVIPrNVpfHALp6rvHIUXtxuvnIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cyj_VAX-khfuKk0JHhLLuHfNhh3MMfl1jsK0rucAnichUEWiP80ebAaT5tAh25WqO-k1hNI4_D87zx7X93il3h6fUcrdFrHtFIKBw9g8IC_Rqydet3kJfwLIKswvMEwsaUUhzoXWHnLOejfVu3bvICJcbrUTiC2-2XKxjOsdpuQFsrNBz3bc8hvWEOIFe7ffSePWBj-epYVILY7i9TZ3UFJt2bBB_bl5N9iBMWHZrIc6_B5t3MOhqpeTsyMGwaLhZxjYE5TZ_bbo38QCTyODgYS8bGWSnozH1JxQec0rpT7UuA39JDqI_NPD10-9rviafhWvW1Gd7K6dwqyCTMEc7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PrT8gurI9dEePkE8BCvhF2p2I-TwBgmtuk5oo4030aZ-A3UIgzgHtqcWuR_0VWu4Vd_kZNYT93iC8zEoghciiOh2Tnnfbcj8APIQg-iiuRAAWvbsMGXvZ_fDsrXD1CGyeySjCBmV1fr58J3h2lFAFfFISkqS9rjTetPS9tdigZ3zUZu1aEd3NgIrpoaXhQd8KtC166t4T_8EcwpJJ22TCz3kZE1myrzRliIQJRDJY8h5DQnZt5G5T65RToK7Na8dqoi_Su4zmMD16g2m_N_B3uk_0Uei4wMAOYWvvHu3PbDDLyVviuqnG6ESTgbgN7xvp3RNSf34HlwhnjSogPqBJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TcUKvg9ONVX428L1nG-mM5-0gnMVq0wZ5gZMDS10Bq1ZQFHxjwdo0D59sLH5Nv8mUbAjmmwc3HEfSvOF3CcicnN18A5TKxiMFhHWA4J6Eir-S0VnSaRVuya9pYrb5_4ZhDd_9Hah7blMCWnRk57p9UqSozk9Ziut9A8Fs64eP-Exk7LU8akw6H7lpWN2TrvLgnKURLxG5PD1RDD08580pNGueSWoubkSuDchUqYDXBapKxpc6loaPk179Yon9ddBK0ZyN2eCtQjVg7SBu0h3PPUtCiDgjszQT5haOnc9CcLVBHHalXYt--hK04EWMW8tXXAvNJXOnPfefk373EzTjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بدرقهٔ سردار شهید جعفر کهریزی تا زادگاهش
🔸
پیکر مطهر سردار شهید جعفر کهریزی که در حملهٔ دشمن آمریکایی به شهادت رسیده بود با حضور مردم در روستای کهریز کرمانشاه به خاک سپرده شد.  عکاس: بهروز احمدی  @Farsna</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/460008" target="_blank">📅 23:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460007">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tb0-Au2rHkvapJR_-Cpgp8wlxHVmiNm2BcnL4A520JTqoAVU0tQlpbHY1w1kKhPxGjVsVNiesRaYJoPNw4hMILYGo9-U7EO7J49X93mNnqYEHLKfuoaGN-eDDism5JJAvS69KwEV3IJFEVtHBHxlEX-0aFveKx1VPlC94aY17GjYgohcmJBPVKeD3nLnZM9PZIfpeKAlABiSwhjJ-1u8LomyM-LtGo9YOwBEq4wcXlV376B7v5CkHLbwUFQcvNrgyYuzqR8MolJY2YrlAkDmGZr6PKOew9j3WkERd1bs9AgK08iLNwsp7TVL1KfAsV9SdZdenxprG5DSaY6Ucyw_Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هراس صهیونیست‌ها از احتمال حملهٔ موشکی ایران
🔹
شبکهٔ ۱۲ اسرائیل از نگرانی‌های این رژیم مبنی بر احتمال تلاش‌های ایران به ویژه در ایام اعیاد یهودی و هم‌زمان با سومین سالگرد ۷ اکتبر برای ضربه زدن به صهیونیست‌ها در خارج از فلسطین اشغالی خبر داد.
🔹
این شبکهٔ عبری افرود که ارزیابی‌ها در این رژیم حکایت از آن دارد که هدف حملهٔ موشکی ایران به بندر عقبه اردن، ارسال پیام هشدار به اسرائیل بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/460007" target="_blank">📅 23:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460006">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e1734fc33.mp4?token=Fqvh9XpTk7ePMszyCWS5c08wSR8QMV32GrO4Lv4RiWRQ8qcOwEs_cWz8Hu7Zbd2m_LC6GWFASguDW_2HnOc0fntOQPWPL88-kHBQoQUg1e3_ZdC3UZ7KRxFdmE_VqRdjoCieyTCc7rO1D1fs12orzS6t1anulFomqo1EwefXeYXe4kwSkNPXl0vSAaN_la3_1LZ62CHRuBrgxyxf8qtHtLf0cuh-ZWWzI9btx8aePUuXFWuJnm3xiH7PQT1TujPOuO_LvfktLfodj0Q79NX_Y70wTtC70wVggF9OSmE2cfr_LARSRCPhVnazHhP5dmwyYiFtGfu_gkxi_RE18iqqcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e1734fc33.mp4?token=Fqvh9XpTk7ePMszyCWS5c08wSR8QMV32GrO4Lv4RiWRQ8qcOwEs_cWz8Hu7Zbd2m_LC6GWFASguDW_2HnOc0fntOQPWPL88-kHBQoQUg1e3_ZdC3UZ7KRxFdmE_VqRdjoCieyTCc7rO1D1fs12orzS6t1anulFomqo1EwefXeYXe4kwSkNPXl0vSAaN_la3_1LZ62CHRuBrgxyxf8qtHtLf0cuh-ZWWzI9btx8aePUuXFWuJnm3xiH7PQT1TujPOuO_LvfktLfodj0Q79NX_Y70wTtC70wVggF9OSmE2cfr_LARSRCPhVnazHhP5dmwyYiFtGfu_gkxi_RE18iqqcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نفت: حفاری بیش از ۳۰ حلقه چاه را در پارس جنوبی شروع کردیم که برخی از آن‌ها به نتیجه رسیده است   @Farsna</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/460006" target="_blank">📅 23:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460005">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53969dced.mp4?token=bomvEbBSJrPgtHX5Dd-bIDyD8f9Z7aKV-ZFP2vA_ICsy6F_5XHbHQzkRYYCxlMpTTwB6q1h0bLgX0md9T1zBOmerQxAAau3lIWQy7pfXW9opRlFJnOgZrwuHVeLc9Gvw4fgq0q7TkUfqOP-dUTobAChmbmAqap8HeJZxlCxc1TOP9iHANrj2j8MkjWhDEgLtXmNaPSDeFm70HhTEqpw_N9UVkqZ1Vwrbz7vLVptt1Iz_MSt6ays3TmT9yrMhtWmbEXfR-Zf7TQIKNSSZxRC8vdnkJM6R9RWIt6H7eRiLhmN-fmkNUAVVLiL9PTfIAbJUwF_X1Qr4LimCGgVD5N9FMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53969dced.mp4?token=bomvEbBSJrPgtHX5Dd-bIDyD8f9Z7aKV-ZFP2vA_ICsy6F_5XHbHQzkRYYCxlMpTTwB6q1h0bLgX0md9T1zBOmerQxAAau3lIWQy7pfXW9opRlFJnOgZrwuHVeLc9Gvw4fgq0q7TkUfqOP-dUTobAChmbmAqap8HeJZxlCxc1TOP9iHANrj2j8MkjWhDEgLtXmNaPSDeFm70HhTEqpw_N9UVkqZ1Vwrbz7vLVptt1Iz_MSt6ays3TmT9yrMhtWmbEXfR-Zf7TQIKNSSZxRC8vdnkJM6R9RWIt6H7eRiLhmN-fmkNUAVVLiL9PTfIAbJUwF_X1Qr4LimCGgVD5N9FMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درخواست مردم شهرکرد از نیروهای مسلح؛ «بزن، الان که وقت انتقامه»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/farsna/460005" target="_blank">📅 23:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460003">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/823b00509b.mp4?token=oVJsOMwIEt6_Wah6zRjwhVYPpYK1wNGAxUqFvAwj8wDzT-qTVzjWYjbj97n5Z_VQpXeqAXaKY9BJFl_gPTzZCXAjzWNseRbL86HpoFAhPXz8URQepUZtKq-DbZVfGNDuAAh6-tkUAgp4Xi9mZeHBOYismldlBIHtzBJcD7dEJ4mxfTpqS0fQNAKls8IghsaYfLz1bAVnC9Ou9WzF5N0UOukE2wbokeHPrLvis1BK715m60ULPXSg8e_9KChXUKn9TPn-JlyqP0ipRV7u0vUWUg5b8yojaVszpi7xAx1vP3rB0_wUzq7G1T74MDa2u-Nu4O6W4fvHFHhbwJ7uffIVJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/823b00509b.mp4?token=oVJsOMwIEt6_Wah6zRjwhVYPpYK1wNGAxUqFvAwj8wDzT-qTVzjWYjbj97n5Z_VQpXeqAXaKY9BJFl_gPTzZCXAjzWNseRbL86HpoFAhPXz8URQepUZtKq-DbZVfGNDuAAh6-tkUAgp4Xi9mZeHBOYismldlBIHtzBJcD7dEJ4mxfTpqS0fQNAKls8IghsaYfLz1bAVnC9Ou9WzF5N0UOukE2wbokeHPrLvis1BK715m60ULPXSg8e_9KChXUKn9TPn-JlyqP0ipRV7u0vUWUg5b8yojaVszpi7xAx1vP3rB0_wUzq7G1T74MDa2u-Nu4O6W4fvHFHhbwJ7uffIVJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون ترامپ: علت گرانی فعلی بنزین در آمریکا، حملهٔ ایرانی‌ها به کشتی‌ها [در تنگهٔ هرمز] است.  @Farsna</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/460003" target="_blank">📅 22:54 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460002">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba0e9b2f62.mp4?token=tcbgcgCkHQ7RRKJq_2ymWBHZ-p8DEI9-qttyMOc5HY1ocGr50fZygrolXohybJ-Ad3hp_EtfrafgxrkKO2i-FjOgmXqMXaWqn2NBxrvLNDMSLfgTBnr0QGPqP_nOFlJk7ZMkqL0du1OTwkpFIqHf6ICB6-nxWE3OtzInVY4pZjm9FwsK6khtTHPO4AproZhCCQuir4BuoV7Z10GfcwDIsa3oZOu-XCZSpd7bAJFf7rmX7tU-OLNVuOwbx0pC3gZFSQV07ZmHi2P6guMvWKyQUOkzAvOmfAMt1UhutYEcYvU5dFOuWYmLDjM4oRdKXVDCKFeB6SCIMw1XbQ91Sa0GVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba0e9b2f62.mp4?token=tcbgcgCkHQ7RRKJq_2ymWBHZ-p8DEI9-qttyMOc5HY1ocGr50fZygrolXohybJ-Ad3hp_EtfrafgxrkKO2i-FjOgmXqMXaWqn2NBxrvLNDMSLfgTBnr0QGPqP_nOFlJk7ZMkqL0du1OTwkpFIqHf6ICB6-nxWE3OtzInVY4pZjm9FwsK6khtTHPO4AproZhCCQuir4BuoV7Z10GfcwDIsa3oZOu-XCZSpd7bAJFf7rmX7tU-OLNVuOwbx0pC3gZFSQV07ZmHi2P6guMvWKyQUOkzAvOmfAMt1UhutYEcYvU5dFOuWYmLDjM4oRdKXVDCKFeB6SCIMw1XbQ91Sa0GVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نفت: شهدای صنعت نفت در سخت‌ترین لحظات پای کار ایران ایستادند  @Farsna</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/460002" target="_blank">📅 22:54 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460001">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e00759c5.mp4?token=Y7-9GzH8SLQVoJyTPuy8-7UWOhjyTeIfxP_c5DdFUeCUepxEku8kh_TsHGxrBv1yvYace19PmAzTDYHakKosZr8m5kcOVDgGwRPybsRod5mP1cez608_i7JSY3zNKqO_JPVDBlxy1t0VXsk6H-uJNNYkvEtwRyJivconHw7M6wTjIfeHbFUX1xZASMeo6yPU6R_o5dGfJmEtiTi37oiLbI5HjQy2_KnLI15FORoxv6i-hLmyxu41b-OCumqjDOsJHbVR3HWEEBZpVyysTPKHRzCgzr5U_IMZJF53xUH6iBOjuSSck3QqEf_Jda3LRvXQd17sk5xTNpmBTVHegODblw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e00759c5.mp4?token=Y7-9GzH8SLQVoJyTPuy8-7UWOhjyTeIfxP_c5DdFUeCUepxEku8kh_TsHGxrBv1yvYace19PmAzTDYHakKosZr8m5kcOVDgGwRPybsRod5mP1cez608_i7JSY3zNKqO_JPVDBlxy1t0VXsk6H-uJNNYkvEtwRyJivconHw7M6wTjIfeHbFUX1xZASMeo6yPU6R_o5dGfJmEtiTi37oiLbI5HjQy2_KnLI15FORoxv6i-hLmyxu41b-OCumqjDOsJHbVR3HWEEBZpVyysTPKHRzCgzr5U_IMZJF53xUH6iBOjuSSck3QqEf_Jda3LRvXQd17sk5xTNpmBTVHegODblw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون ترامپ: توانایی ایران برای اختلال در زندگی آمریکایی‌ها بسیار محدود است اما صفر نیست.  @Farsna</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/460001" target="_blank">📅 22:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460000">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0539e701d.mp4?token=vAoElMCtJuuaI5k9HupNhHqLVw7l9cF8E7WiGixFD1mj4VZqhthlZVuCzdfU__WbRAzkLUfnbmxrFFYXm_2tUHm1xj-w9P6U1Mx9L326wcHRB5UB2xgfmPMxFvS0O-yT_fZXaHLBGuTY3AstOdr2AzRvqhX6-06rjbVmSetlmmcupPI-R_7R7W2MiVP0uqDi6WRZVXjieaX8HRbOwfOLqM1ooLpKmsJjj5hHmSiSufw2IOhzddMyJVwkDlpv-ysPWKWyDCuvvt91mzi_f2fmeDoOL9zDbahpbCHTaZSMT111yd6OFD4Cx55h1exd_TDOw_NQ6mBoaSnuiFCeLGDk6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0539e701d.mp4?token=vAoElMCtJuuaI5k9HupNhHqLVw7l9cF8E7WiGixFD1mj4VZqhthlZVuCzdfU__WbRAzkLUfnbmxrFFYXm_2tUHm1xj-w9P6U1Mx9L326wcHRB5UB2xgfmPMxFvS0O-yT_fZXaHLBGuTY3AstOdr2AzRvqhX6-06rjbVmSetlmmcupPI-R_7R7W2MiVP0uqDi6WRZVXjieaX8HRbOwfOLqM1ooLpKmsJjj5hHmSiSufw2IOhzddMyJVwkDlpv-ysPWKWyDCuvvt91mzi_f2fmeDoOL9zDbahpbCHTaZSMT111yd6OFD4Cx55h1exd_TDOw_NQ6mBoaSnuiFCeLGDk6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از شهیدان حاجی‌زاده و باقری در رزمایش موشکی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/460000" target="_blank">📅 22:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459999">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e4e36871b.mp4?token=ewZHZmJtgQkLfq4JeiefkGuF1fsKtHHcvo5Tx3cMj9bajTqNKSGyhgLEr2WcDlaQNcu9dsqO7xLXuiTPnGFaAj2iZdXJ3yVil-p1cgmGF9yCkKRfFihZJ-hF9I6gKc2B-911CdzSoO0wV4Nu7-PkY9jXZGJ5ZOobqXRAPp3Mxn7ElqPrbW1OI-eJQoGPt7TYE8wkM8zofNsIaw_gve8QYIjfxdDluGvGWjBYnInsDiFd-bdxcWRyYmyxMkCZZfxeOqdwCAnAWwhS32lAu1BMbpe30i1JYwKWB8pvmhSam6_geu6Z_q2QUb48x3142kFpMJnYLSlct01ZLP8PqZ7x1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e4e36871b.mp4?token=ewZHZmJtgQkLfq4JeiefkGuF1fsKtHHcvo5Tx3cMj9bajTqNKSGyhgLEr2WcDlaQNcu9dsqO7xLXuiTPnGFaAj2iZdXJ3yVil-p1cgmGF9yCkKRfFihZJ-hF9I6gKc2B-911CdzSoO0wV4Nu7-PkY9jXZGJ5ZOobqXRAPp3Mxn7ElqPrbW1OI-eJQoGPt7TYE8wkM8zofNsIaw_gve8QYIjfxdDluGvGWjBYnInsDiFd-bdxcWRyYmyxMkCZZfxeOqdwCAnAWwhS32lAu1BMbpe30i1JYwKWB8pvmhSam6_geu6Z_q2QUb48x3142kFpMJnYLSlct01ZLP8PqZ7x1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نفت: بعد از جنگ ۱۲ روزه توانستیم تولید نفت را حدود ۷۰ هزار بشکه در روز افزایش دهیم  @Farsna</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/459999" target="_blank">📅 22:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459998">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff5a77de4b.mp4?token=PGzY3KMv-f23_KO-wrVzFJMNFu2s3fKdF4pdVcgYTCeV7vpwDLHM8kX8TpqBsPKj45RUbXxPwZ_hPnCb31oF_FzsLPjT5tVQCe8ouEH25Fmj3YErRsosYRCCvqLWHGUGRwHeFzT3Ykq_e8vZ030-OIeCkvat6crMU4f0NFhqx-Xx_5HROP4SAZEKxtwHYFPA4vnA5HhR93JrQPAhxahtMYknfkW4wiW2um-s7IxkUq5NH8OBB4TWoBTb7XM0zbEurm0iqJvyThcpxSYuA13JeWUA_PcmgFk6TH2UebijRj-6XM2nnuy0nPvOwTeqiDQanvF3DNV9YyTfN8w8_Cv0hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff5a77de4b.mp4?token=PGzY3KMv-f23_KO-wrVzFJMNFu2s3fKdF4pdVcgYTCeV7vpwDLHM8kX8TpqBsPKj45RUbXxPwZ_hPnCb31oF_FzsLPjT5tVQCe8ouEH25Fmj3YErRsosYRCCvqLWHGUGRwHeFzT3Ykq_e8vZ030-OIeCkvat6crMU4f0NFhqx-Xx_5HROP4SAZEKxtwHYFPA4vnA5HhR93JrQPAhxahtMYknfkW4wiW2um-s7IxkUq5NH8OBB4TWoBTb7XM0zbEurm0iqJvyThcpxSYuA13JeWUA_PcmgFk6TH2UebijRj-6XM2nnuy0nPvOwTeqiDQanvF3DNV9YyTfN8w8_Cv0hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نفت: در جنگ ۱۲ روزه انبار نفت و پالایشگاه‌های فجر جم و پارس جنوبی هدف قرار گرفت  @Farsna</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/459998" target="_blank">📅 22:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459997">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1a092430.mp4?token=QqryeD4X2bjYcLeIKU4VQsMy515Ykw3hUwVnTEIB60zLbmT_iD21JGpYIatUtpNcNBvSIUfr9-6RARE-VOmJszfJwulUCvFlkue2GL4gd0t48lNk2qI9Jg8Vd2kETG3XNtaUgL5nY4FL_MAobnxvs91Q3uPMAQLD8q2d7FQRARs01jIPM83vrRLpDvu6X-fq5JEXCSlwiwEj__W6UbIVrI3lXsoddUXvOjlcwfRGoZqw-waPN46JEAcWRYwPxGeRq5-Ygd1LeiS0cakSq6iVzbNnr8v6cP4aJ0DaK8_q6uVR0Z0VZArY2QUnANBjjRwosSnqPFW_xkRV2ECt2tmv7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1a092430.mp4?token=QqryeD4X2bjYcLeIKU4VQsMy515Ykw3hUwVnTEIB60zLbmT_iD21JGpYIatUtpNcNBvSIUfr9-6RARE-VOmJszfJwulUCvFlkue2GL4gd0t48lNk2qI9Jg8Vd2kETG3XNtaUgL5nY4FL_MAobnxvs91Q3uPMAQLD8q2d7FQRARs01jIPM83vrRLpDvu6X-fq5JEXCSlwiwEj__W6UbIVrI3lXsoddUXvOjlcwfRGoZqw-waPN46JEAcWRYwPxGeRq5-Ygd1LeiS0cakSq6iVzbNnr8v6cP4aJ0DaK8_q6uVR0Z0VZArY2QUnANBjjRwosSnqPFW_xkRV2ECt2tmv7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون ترامپ: اروپایی‌ها به‌صورت علنی از ما انتقاد می‌کنند اما در خلوت به ما می‌گویند اگر آمریکا در مقابل ایران کاری نکند، هیچ‌کس دیگری در جهان قادر به مقابله با ایران نیست
🔹
ایرانی‌ها باید حمله به کشتی‌ها را در تنگهٔ هرمز متوقف کنند. ما با آن‌ها مذاکره نمی‌کنیم…</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/459997" target="_blank">📅 22:37 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459996">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a46994777.mp4?token=CMk0A0E2GGzRvUjbao07ERQtNu72Vx4QEck3n5Q7A4ercHrIpN-rtzYs9fbn6f_06pNSHETYKV6VotA9ys5OpZEY4oEMF7ZyqYziGip5qBBx10EfHPbZS2OziOoF_PCHXKtwUMAccFRdc9rNZsLl8gwQGsevf69hA8V_qz8tKVBHnRhuE909bOXrhnMED2cAeU9rn3NZ-4cYFRPaVpYEfZSKZMD6Qbv6jd3NR0MuRa2i9uGJ3uXPHjiqTYdr6Fg_hGA5LoA9FVc8oNtdiYspg-DOyQbgOqkdMp5bvy8t5H3Wanucjzx6i4TgSbG0prw0jmliLZqrLNX9ODBfa6pfTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a46994777.mp4?token=CMk0A0E2GGzRvUjbao07ERQtNu72Vx4QEck3n5Q7A4ercHrIpN-rtzYs9fbn6f_06pNSHETYKV6VotA9ys5OpZEY4oEMF7ZyqYziGip5qBBx10EfHPbZS2OziOoF_PCHXKtwUMAccFRdc9rNZsLl8gwQGsevf69hA8V_qz8tKVBHnRhuE909bOXrhnMED2cAeU9rn3NZ-4cYFRPaVpYEfZSKZMD6Qbv6jd3NR0MuRa2i9uGJ3uXPHjiqTYdr6Fg_hGA5LoA9FVc8oNtdiYspg-DOyQbgOqkdMp5bvy8t5H3Wanucjzx6i4TgSbG0prw0jmliLZqrLNX9ODBfa6pfTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون رئیس جمهور در توسعه روستایی و مناطق محروم: در سال گذشته ۶ هزار میلیارد تومان سرمایه‌گذاری برای محرومیت‌زدایی داشتیم  @Farsna</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/459996" target="_blank">📅 22:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459995">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a94cd510ec.mp4?token=CAECejRDyYabtKKfZw-yyj5ge17gJpYd1SrCEqPpPIsuL3AzsWp4HF9k95cfxzPfxovlu-xXJPjtQbixdvEqJT4nt1_edP9hA-H828Fm8L2i8gL9xmQ9_m0BsZYbcIh1hSCsNVGHPsRW1I_drYbzmtyUoLJsJtfH6IwVj39BGJhoN85VnbqYh7LDEy5dI-mUoD-J_IG485fzK8R96LOrmBCFOBJO2YTKU9DvAUoLWNGNIzdKH1EEbEx90D_E1U-3w5jJWb4LJY85sR9zq0pHLWLNnyoDlY13O9WP7_-k2inHb6cKpS0G9bIcqqLbfEap5l69AZhYH4bSzyYF7-28XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a94cd510ec.mp4?token=CAECejRDyYabtKKfZw-yyj5ge17gJpYd1SrCEqPpPIsuL3AzsWp4HF9k95cfxzPfxovlu-xXJPjtQbixdvEqJT4nt1_edP9hA-H828Fm8L2i8gL9xmQ9_m0BsZYbcIh1hSCsNVGHPsRW1I_drYbzmtyUoLJsJtfH6IwVj39BGJhoN85VnbqYh7LDEy5dI-mUoD-J_IG485fzK8R96LOrmBCFOBJO2YTKU9DvAUoLWNGNIzdKH1EEbEx90D_E1U-3w5jJWb4LJY85sR9zq0pHLWLNnyoDlY13O9WP7_-k2inHb6cKpS0G9bIcqqLbfEap5l69AZhYH4bSzyYF7-28XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون رئیس جمهور در توسعه روستایی و مناطق محروم: در سال گذشته ۶ هزار میلیارد تومان سرمایه‌گذاری برای محرومیت‌زدایی داشتیم
@Farsna</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/459995" target="_blank">📅 22:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459994">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e8792f237.mp4?token=byAkClhMXxKqB167wp_XMfF0O10frV96EzHna-E_Ti2Expi9RgBnoXdNBDmLL6Yf8CTMKHA8cWod4Kb8mQ6UGE-HgBlO4o5jX9nfTpdP-UPoR7UTZXTttXuNCehsEB3LLL_2prq1faVzQf91CBZnN9AH7Qcb9430jngrdSd2Zzr20XiHlkP-1JduH-_yffRMwkn0mLAn4F8FYlpR8vMguRyU85thGSnV0Pv0Itu7J-b0-ugQVxwmv3O9oWahaOVexo7Ipj1uRaEJSRizFaJbrZYhS5Dls_dCZWxukza17gHh8EVXuGsIc3vbTst6LymZg0jjHUNMtRxzcJW4BDK0iyBBcoKy7X4eeWXRnXaZ4hgPhljykgGRzqrz35CjfgIL36Pt-Rai-yxdJTIRLnJHaIcqtDQZg_xK5tWuQQ4p61qCnb7SH6Dky8tFHnzvBHmM1qMOOHnNsLSVmupEpUbuVf2tQQ_g4wfM8yJNug9ZJtQim_0bEZJjzz9qU2gjb4j3wjoWONaikmtDmlsiY7IBuppfOVfQEKJji6fRsorBWe1YiRCufuzVFDY2OFwqGrb_zkgVu04cGX8gADf2iteO-qLwvrdn25NQDJ9SUjesf1h27mAzt8gC2i28XaonUPIymOCJ-QDNNRuZA208Q1ntCbvCMG1ckR4Lkdbi6Qqfbek" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e8792f237.mp4?token=byAkClhMXxKqB167wp_XMfF0O10frV96EzHna-E_Ti2Expi9RgBnoXdNBDmLL6Yf8CTMKHA8cWod4Kb8mQ6UGE-HgBlO4o5jX9nfTpdP-UPoR7UTZXTttXuNCehsEB3LLL_2prq1faVzQf91CBZnN9AH7Qcb9430jngrdSd2Zzr20XiHlkP-1JduH-_yffRMwkn0mLAn4F8FYlpR8vMguRyU85thGSnV0Pv0Itu7J-b0-ugQVxwmv3O9oWahaOVexo7Ipj1uRaEJSRizFaJbrZYhS5Dls_dCZWxukza17gHh8EVXuGsIc3vbTst6LymZg0jjHUNMtRxzcJW4BDK0iyBBcoKy7X4eeWXRnXaZ4hgPhljykgGRzqrz35CjfgIL36Pt-Rai-yxdJTIRLnJHaIcqtDQZg_xK5tWuQQ4p61qCnb7SH6Dky8tFHnzvBHmM1qMOOHnNsLSVmupEpUbuVf2tQQ_g4wfM8yJNug9ZJtQim_0bEZJjzz9qU2gjb4j3wjoWONaikmtDmlsiY7IBuppfOVfQEKJji6fRsorBWe1YiRCufuzVFDY2OFwqGrb_zkgVu04cGX8gADf2iteO-qLwvrdn25NQDJ9SUjesf1h27mAzt8gC2i28XaonUPIymOCJ-QDNNRuZA208Q1ntCbvCMG1ckR4Lkdbi6Qqfbek" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تناقض به سبک معاون ترامپ؛ ونس: غیرنظامیان را هدف نمی‌گیریم، اما گاهی اتفاق می‌افتد!
🔹
ونس، معاون ترامپ، در پاسخ به خبرنگاری دربارهٔ حملهٔ آمریکا به یک مراسم عروسی در جنوب ایران و کشتار غیرنظامیان گفت: «ایالات متحده ۱۰۰٪ برخلاف ایران هرگز غیرنظامیان را هدف…</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/459994" target="_blank">📅 22:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459993">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaKNWUXNGkT3Y_ywk4CSCuP0Fz11qrXRhUFyOxj4KSyOt8ggpX71gfysZ7WSz5aKkWh3-XThCDHAWsX_w62jTFu8rJkDV6dB3ZVntSQh_r1KLo1B3he9AZfsM1I3yaPv4wpNXMmpU62Z-ZTU_nUV9hiJ6yE3cF85Qh1HjpFAjvT87DV1KObA2olqctWHLOLt_dsB_vJjkHtRRCOR-lgRQSLO_2fQ1w4K_sM5bk_i4xs9fXUGiU4mchdGXBHdr-5r9_nu3mEu4RtO4SxK1XNnArQTJ2mLxXAqMx662ba9hCNgVFrv4-5Rl1VsQSoky3yDqqQzVaFW6aJxtHRhuquogQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
واکنش شورای عالی مدارس اهل سنت جنوب ایران به حادثهٔ کوهستک
🔹
شیخ یوسف جمالی، رئیس شورای عالی مدارس اهل سنت و جماعت جنوب ایران و امام جمعه اهل سنت و جماعت بندرعباس در پی حادثه خونین کوهستک، با صدور پیامی این حادثه را محکوم کرد.
🔹
در این پیام با استناد به آیه شریفه «وَلَا تَحْسَبَنَّ اللَّهَ غَافِلًا عَمَّا يَعْمَلُ الظَّالِمُونَ» آمده است: مرگ بخشی از حقیقت و معنای زندگی است، اما گرفتن جان انسان‌های بی‌گناه و نابود کردن حیات آدمی، جنایتی نابخشودنی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/459993" target="_blank">📅 22:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459991">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/044bd12ec8.mp4?token=HKggrx7F3V5z3Ila0YGtdKgPSfGLpSSo8-i5tkDMzVtSEyV21S71IsblGX_o3DSuWME4BnPccZ9IoTSb8knydsfd4f5pLJIu7NtM0QW0gzGSF5oKjGPzAdCWQyS05fDTeVbA6iIOhVNjt0wT2DlSzaKNgiB9VnwiSvs0a1iff0D_So9VCQwJwq0TiHkv-m7GVB9nZNK6uZjKNE_RJerr7cqxrPaCD4GAhS9DFsKTrZkS7UoAjkxRQgwKXtA1iZjC-ix2vndyWUXIvm9v3meVGcCO2mqX6CaBW-VgtnRq_9mcv_qQK5poNcx-0-34645NzbLOhS6dVLqvJZmtT9hrwTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/044bd12ec8.mp4?token=HKggrx7F3V5z3Ila0YGtdKgPSfGLpSSo8-i5tkDMzVtSEyV21S71IsblGX_o3DSuWME4BnPccZ9IoTSb8knydsfd4f5pLJIu7NtM0QW0gzGSF5oKjGPzAdCWQyS05fDTeVbA6iIOhVNjt0wT2DlSzaKNgiB9VnwiSvs0a1iff0D_So9VCQwJwq0TiHkv-m7GVB9nZNK6uZjKNE_RJerr7cqxrPaCD4GAhS9DFsKTrZkS7UoAjkxRQgwKXtA1iZjC-ix2vndyWUXIvm9v3meVGcCO2mqX6CaBW-VgtnRq_9mcv_qQK5poNcx-0-34645NzbLOhS6dVLqvJZmtT9hrwTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیابان‌های ایران ۱۸۷ شب با حضور شما مردم زنده است
@Farsna</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/459991" target="_blank">📅 22:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459990">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8lUp9vUpD8Ng-SLtSu-XM2gKKi9KwtYzQuwqG0G9BSNi23JvzN4xYe2pSFkGVSmOVNz-mymA3ME4Mfg5ej_8NpVaLIi0_cJkxZqtdYZ-Vo5iVatkpGXHhBGxPAGltlYVTerzkc-Ghgo4oFjwwel3b-ggEPV_-tcBOtfi2gboL7hgEA7dtelytpLvYUTc4g8eAnC_3KPN7yZdUpkVGtvly6N6X6M-4cfOXEVg4NAfCSxBD2qm8ahWZMWdonP_izTjbo4gBDpnjk5JO1FUMIrclnruFK9Z2CGcsxQX94kZZbdID9OYyZbg7fo9LUId_SFHRhopd9x0nRKp7HuqtP-tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس قوه قضاییه: ایران در راستای اهداف مقدس خود به آمریکای جهان‌خوار با صدای رسا «نه» می‌گوید
🔹
حجت‌الاسلام اژه‌ای:  ایران در راستای اهداف مقدس خود برای آزادی انسان‌ها و انسانیت از یوغ استکبار، همچنان مجاهدت می‌کند و به آمریکای جهان‌خوار با صدای رسا «نه» می‌گوید.
🔹
ایران با آموزه‌هایی که از قرآن کریم و از پیامبر عظیم‌الشأن اسلام، اسوه عدالت و فضائل اخلاقی، آموخته است، به هیچ وجه زیر بار ظلم و زور نرفته و نخواهد رفت.
🔹
در جریان تجاوز ددمنشانه آمریکا و رژیم صهیونیستی به ایران اسلامی، کودکان بسیاری در یک مدرسه هدف حمله قرار گرفتند و به شهادت رسیدند؛ این کودکان معصوم در این تجاوز وحشیانه ارباً اربا شدند.
🔹
حمله به مدرسهٔ شجرهٔ طیبهٔ میناب، یک جنایت جنگی آشکار بود؛ کارشناسان سازمان ملل نیز این مدرسه را یک مرکز آموزشی غیرنظامی توصیف کرده و خواستار بررسی مستقل حمله شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/459990" target="_blank">📅 22:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459985">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B1BxekpLBjBf6gLCRSMasolKpgcRe_OGwypFAjdiJRUMmwE--MyWQo1coGCX4mcME-Ops9JuwgDbbFmRhUubNmmXuUsg0pwNdCNRQABdcXTh3Yw9rJYILb32FPsAT8VkuZ6Y7G8s7oQW5jlGK_VA6oixUCHe3G137_KNmOjOTK7pi4fsmiTe_DKzmnJFfurmZKPL6jN7aSqyY6oBx5VYf6NWHvpDkCT6L3A2utm0gaxFhjJgROxtGn9VpfxhZ1aATcN3N5_xNS9ALZYzDQnnGYWs881ITd-G7vYRJitJWQW7ACeUAMLF2FRyu2vKvE7LbF7EbLmJPaCt-RM0JyitpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P0_udPkpATy83AejEXJFuOsZFy7EqmKKIuXs0Rv6_LXoHzhgWkrbyPTrfDNkfUjlyubmrRznF35eKtKMpReu5ZDqgw7WsN5meh49KttjPnVLH0HmoCUinhSeLVWbhUvrujAV4mo5KRvWhv4h-axnbR1TmxOAwlLUZK4OU6IOz0qCe1_uqAL08exOrF4bmBBu5t73y5M2bfXwr778MytrjGOxVHz7Pc0oKEINQoFwkYArJy4kZrtmT5icGgEGjyUKFuKc6384seEn_akevW_EKVTi4_dEPCt8udhpxwP3h-mKPdtC-DeIljAeIJpRDZCaLDAl6KQCR53LaZZuHmS_UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bUHWFHUHlAjrUVAqNjNK9GEjy9Ig7krOFCZruEc7rdOr52t_0ldM_ZmnWbhE9CWG3zNnnBKyjMY4_y4A_E_dsFu8V_pTpjvuW1f_CdzGn_uqyOqBx-0XITpNnPnSnkEYNcTOPjB-iO2LYisretvVhHV2U_CiQGBNP-ZkWsJZA-ktbwZlZggRnebovcIOCeQqr745fQmdtxSQP1YdpDDN1YkshFS24FUMAFEI2WusoqB1eN8VTmqBMiRSMWI13gKoygK70uL7ks0C_pqHA4tzLVAonDTBJtFKuUg2q4DZuQFcMmCMU8UNilZHxt7GntG4pDmx2U6nWQ3YutCZmZW9vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LYfu55HlZK4oL7n3-v3WXmeJyLqZkkT3TNw6VMTTxVvSb2H-qqjBpAXO6JieR5nCbYaoMz9QrNBRCTX3getf6fKfC7SOeg35v6t_wYhs7h6TXy9d1P25-61atQvSdRcdcUq6SMS_fiHBNOgIwrSq0HlKya_PEipzsyRalg5vxmt64mZEKXvYGrPBF7UvZimmLhSyC5Zd0Eja5TkMUXTgsWTg4NBqzjuw_JzBvUukGQkW2ACCBB4Ff5EF2VtMiuy0o8hWExx9YUbBczhbUuqG7ycN0U2qNzl_SAeSXdkiw0qsAAJ4DL_Z8RMYRC3dUEJBWKAS9YtawD93XxtyPEecoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H6h0dHKUHDFdhOzoGD-6C6aBkc_k7uwXsCUsM9cTKYaa9_JANgQDw7RFgWvzxGnkIxnlvs-sojnNUYvXIt0hnbQIXYiuP51Ak4DpHY0gXNCUDTCwA_uK7BGo-EaYuRscbUI7cy4K0j7chWrX7c-mY2seeBN2eGDLz67JGTlbV7RHpGlmhuhDk9y8HNHoC5k35kryBfH6ZysZLQPhff5_xdjmtoDbXUMob7IBHp-iO7LzcI4OHkBoGtWVKYi4PVM0AYM4yriY1l-QbvWXkF7bHeYJH2V8A0Hmatpo5Bmfit3V5R3WedyV_0biA3ikvcdqosgu94eXt6nRPkWzN2pcxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
تشییع با شکوه شهدای حملهٔ آمریکا به سیریک  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/459985" target="_blank">📅 22:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459984">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54e3c94760.mp4?token=RAIKtmqgFj4tbMH0GtCWzd-LZjcdnQf_cgW3R_nx5RZBImCH5g0iMeCr2LNslfLto0YkHSOEmYdfOkMg63IUOyhlldqOcfP2WGiBk8JtkFqq5KhU3bbB5Xz3EnTT0rYCgHlYstXqtBQxDV3AimecXVEsE0sKwGqmMt5g2cF2BozaioBKYGat2kMKWdfuPZe4kKWD-AyZa4TZ3pAB_azD0TbbR5kaDzg-uEFYd-gXWLVvEV8YiPKHDp9rYGKW0aXglxagjb6lTX3prE74AUm-RunI1VrCMT_aDVsrCG46lTmHY-D9pjNL3E61OCiYYzy0T1dfrXqT8iagHsEdjqusQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54e3c94760.mp4?token=RAIKtmqgFj4tbMH0GtCWzd-LZjcdnQf_cgW3R_nx5RZBImCH5g0iMeCr2LNslfLto0YkHSOEmYdfOkMg63IUOyhlldqOcfP2WGiBk8JtkFqq5KhU3bbB5Xz3EnTT0rYCgHlYstXqtBQxDV3AimecXVEsE0sKwGqmMt5g2cF2BozaioBKYGat2kMKWdfuPZe4kKWD-AyZa4TZ3pAB_azD0TbbR5kaDzg-uEFYd-gXWLVvEV8YiPKHDp9rYGKW0aXglxagjb6lTX3prE74AUm-RunI1VrCMT_aDVsrCG46lTmHY-D9pjNL3E61OCiYYzy0T1dfrXqT8iagHsEdjqusQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تناقض به سبک معاون ترامپ؛ ونس: غیرنظامیان را هدف نمی‌گیریم، اما گاهی اتفاق می‌افتد!
🔹
ونس، معاون ترامپ، در پاسخ به خبرنگاری دربارهٔ حملهٔ آمریکا به یک مراسم عروسی در جنوب ایران و کشتار غیرنظامیان گفت: «ایالات متحده ۱۰۰٪ برخلاف ایران هرگز غیرنظامیان را هدف قرار نمی‌دهد»، اما او در جمله بعدی اعتراف کرد: «اما متأسفانه گاهی چنین حوادثی رخ می‌دهد!»
🔹
او ادعا کرد که نظامیان آمریکایی «وقتی اشتباهی می‌کنند از آن درس می‌گیرند تا بهتر شوند.» اما خودش را به فراموشی زده و نمی‌گوید که آمریکایی‌ها همین چند ماه پیش، در حمله به مدرسه «شجره طیبه» در میناب بیش از ۱۵۰ دانش‌آموز و معلم بی‌گناه را به خاک و خون کشیدند.
@Farsna</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/459984" target="_blank">📅 21:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459983">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b54dc7ca5e.mp4?token=SHxqX4BLa2ufZSaC4vEEt4T7pgOz5mIn-culwYRrCpvZV1KLukNn7aHqzPLXwvgGuYj5PrBdcxEzrN1o0ic44G8VsRwRi5_5K4RYGigat1Jyz3lYujxMsEGai4cyUoFB8OhLW-sP7rU4cKjb8KfPntekdsoHbnTMtj_gOBgOY7RyPsi288FBZun9VdZkJYkL0yhGb4LXzNeYmUV8-F7pSJl-7RdurheohzsRFlYFtFrdW-kvCGfqOsvIDxqhSUiGAvOrhnj0gPojxLdoyyQUJqXAnv6DOn3OG2Lq2SiYXDKtE238uzb2eo6EmjVLxYAWcM2aIHk1tuJ5_LF-VRlhog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b54dc7ca5e.mp4?token=SHxqX4BLa2ufZSaC4vEEt4T7pgOz5mIn-culwYRrCpvZV1KLukNn7aHqzPLXwvgGuYj5PrBdcxEzrN1o0ic44G8VsRwRi5_5K4RYGigat1Jyz3lYujxMsEGai4cyUoFB8OhLW-sP7rU4cKjb8KfPntekdsoHbnTMtj_gOBgOY7RyPsi288FBZun9VdZkJYkL0yhGb4LXzNeYmUV8-F7pSJl-7RdurheohzsRFlYFtFrdW-kvCGfqOsvIDxqhSUiGAvOrhnj0gPojxLdoyyQUJqXAnv6DOn3OG2Lq2SiYXDKtE238uzb2eo6EmjVLxYAWcM2aIHk1tuJ5_LF-VRlhog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرار بود ۳ روز جشن و شادی باشد؛ اما...
@Farsna</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/459983" target="_blank">📅 21:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459982">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🎥
مردم ولایتمدار بافق یزد: پای آرمان‌ها و ایران تا پای جان می‌ایستیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/459982" target="_blank">📅 21:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459978">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mdw1j_2D6RgpUdAmcVGXW6bIb0enCH6Jl1OqJ9GgmuMLEdSwjrZwR7PlvCIvt6OFTs6JadGTogucoIw2ANsgcSOvLRQLLPMpVS4OTCW8nNb5xMMJG9pMPTXiG46Rv71yV1zDPUbuiEfV9SEo_f4j491sGiw92eZLvb7mWwKrZ4UbyvNJ3a1XE7Ij-i8-NXbQh8vrRkz93AhenoaZ_6TjUn3VEMY4wSBdVEyImg1e-mIDGq5dptEPKPS06epXqhXAxcufkuHDL-Bhxvz6HnaHHC2aOH6ffksj2BAvl0EIrekHzRIVUGpkTAp3170C7H9vxtOuJqQwzbXZLMtg_9ZODg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UMvmKCPkMaVrGGUP6QoNmrUdRnE6XzAY4e-Nr4s2tJ3_blLU16ZZS0QtK5KJfm-O0FA8jw9GHWYZYKURqirkKULxhCemaYuAYnbGTjkqFqzgdJ1PBGaklp_SxwT-LPfJyOcPjj3wXUK2--1JWHMj4jsi6aPDYwd-6yfTSrxejtw06Iwv9_VWSKyoE4uaenCFwhTbUHigSiGZBclm9hRkODLhI96HoipOYn0LYIy2K2jg0TmLt0uFCjRcBZnl4w3bmdIc52mOX5TLXKfp1UV6wFj6wAf3nc57mJLYAL9lgiqu_ST8Dex1sjNiUkn8SA_DTUxjLfZdQna4fy29zG65cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BnRWN41sritCIuqW993PqOrTbPFb2KOIoyVCa77Bjz7l_eMoOCxqwGX982CKK00JbJtRoZVAUVNBEcCNkV7_5Xo_99YA8PWAFZhTFqWLZwySyXleWvTmzhyK1OhlUw5ggBIrJTjjAk_793BoZC40B3WI87yPMxAS5PO7FizJB49OivdIJs8CndQD4p4l_8h1USEvdDdepLifW7eRW0AX0OhdinmQqqe_5QvCb3Q_0ZXYXG_2gpzp4qA0wbepErqQ8zQi7BIQaBlQKXwYywVOzagtMxAIeiaUUBOZi1eJT0HPTMAz1yy3vqZaOqqBX0loZ-Xyrcc3C-Hayc-x_e_4qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S07ZQ9jm560T2-caCUValqmKVI4mANuw1fh-Yx1PNp9IJ1dnyRUBnzb5n-FrPTDqMaG4RynsZ_ZVqAVx_kWR2B5T95-PMdoHsexLZUG_BWjEaSwVOgQlm5A1mm9H7-tFP0PWwcQhoxBphopLTGuOPw6nJ3utWwNF3GBJN6dbfryOM9VzjzDn4aKjiSqpXnJalxgQfBCym2f-MZhL-T5uxhBEOT0OH5UWlIF9HbU3QoBOJEYClqC93fgFurycHeqpLuyWTAQ0r5lRM1Y7MGfLxDpDfYgj3KsDoz1UpVBwnr8WG85A0pGBZOvjEHTcai4O88nxmfSlMbhvVLc0PR6z6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نیویورک تایمز: موشک آمریکایی عروسی ایرانی را به خاک و خون کشید
🔹
روزنامه نیویورک تایمز در گزارش تحقیقاتی خود با بررسی ویدئوها و مصاحبه با افراد محلی، نوشت که آمریکا در حمله به جشن عروسی کوهستک از موشک‌های JSOW استفاده کرده است.
🔹
این روزنامه با استناد به نظر یک کارشناس تسلیحات و همچنین تحلیل‌های بصری خود نوشت موشکی که به یک منطقه مسکونی اصابت کرده، ساخت آمریکا بوده است. این حمله به شهادت ۵ نفر و زخمی شدن ۶۷ نفر دیگر منجر شده است.
🔹
«ترور بال» به نیویورک تایمز گفته است که بقایای موشک اصابت کرده در جشن عروسی متعلق به یک بمب سُرِشی است؛ نوعی مهمات که فرماندهی مرکزی آمریکا (سنتکام) از آن استفاده می‌کند، اما نیروهای مسلح ایران از چنین تسلیحاتی استفاده نمی‌کنند.
🔸
نیویورک تایمز در بخش دیگری از گزارش خود نوشت که حمله به کوهستک چهارمین حادثه‌ای است که این روزنامه آن را مستند کرده و در آن تأسیسات فاقد کاربری نظامی هدف حملات آمریکا قرار گرفته و غیرنظامیان کشته شده‌اند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/459978" target="_blank">📅 21:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459977">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🎥
حملات صهیونیست‌ها به جنوب لبنان ادامه دارد
🔹
شبکه المنار: ارتش رژیم صهیونیستی اطراف ارتفاعات راهبردی علی‌الطاهر را هدف حملات هوایی و توپخانه‌ای قرار داد.
🔹
همچنین جنگنده‌های این رژیم بار دیگر شهرک النبطیه الفوقا و شهرک حاریص در جنوب لبنان را بمباران کردند.…</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/459977" target="_blank">📅 21:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459976">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fy3HjY6tQO1IYzBwSq4ofAB_LGVU54vnA_cvOpR0Nk8oRcbjM_27XK3NIdRht7oyXAUlUMCpuxXaYE_4CI5kQGlLBDAYBBMLrlQZ1bh0pqYRKaOkUpKhQWsB7VitaXvuTOaXiD1FHZM0me5ERdGIGSNAuvZLp-AiQKRKxUrICWpmimieFpId01k4GTOoJ1ZgtHiFj_d6K8jxajvSlT4I1MuHbv9IFsj-EmosrdH0Hm_51wPIlpmdxbTHBD4xMLJHe1Hi2_ohL-FnEVhEEiPOmMrVQ8dOeUx5obiWcsahL28uppMB2Zju8Du9oo-2elsa3rB0EeVHp8Rwoug6-1jXzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو ارشد کنگره: جنگ علیه ایران به شکست انجامید
🔹
رهبر دموکرات‌ها در مجلس نمایندگان آمریکا: ترامپ متعهد شد که هزینه‌ها را از روز اول کاهش دهد، اما تحت حکومت دونالد ترامپ و جمهوری‌خواهان، هزینه‌ها در ایالات متحده آمریکا پایین نیامده است. بلکه بالا رفته است.
🔹
وقتی افراد در مناصب بالا این‌قدر بر پولدار کردن خود، اعضای خانواده و حامیان خود متمرکز باشند، این یعنی به بهبود زندگی مردم عادی آمریکا توجهی ندارند
🔹
تصمیماتی که گرفته شده، مانند این جنگ بی‌ملاحظه و پرهزینه در ایران، شکست خورده است و زمان تغییر اساسی فرا رسیده است.
🔸
تاکنون چندین عضو کنگره از تجاوز نظامی علیه ایران انتقاد کرده‌اند. قانون‌گذاران با اشاره به افزایش قیمت سوخت و هزینه‌های زندگی در آمریکا، درباره احتمال تداوم درگیری‌ها هشدار داده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/459976" target="_blank">📅 21:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459975">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdab2cd697.mp4?token=j5jr5gGdrZorVYSy6Oyte7udIGgVI-NdVfe3DgzAB9JhtPMtVk0krJb-HlVsajEyY-jZd7u7tHpWbwDZuPBXyPA72N1PV5Xre-eBfl5gt9icDtkSJ7148D2G5d53X-UeZW6xOta7d1R3pkWcpkihOJQnEZs7D14lhxQLVlhq-mHeXUFIHS2R8uvt8dZOeiXKel3l7-_EMGMGhHOhob0Y-bcxuZTM9X2PHib9PUxlkq-KAaKiWmIDj0DEDpVmkV04AU7xzejEkAw9ft1vjvR8pDICvqZD2ABqeh5PposXpcpQGjH9f3Db9yRvazAUWLDMWfuO7SIoi4KVh_NpO5jCcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdab2cd697.mp4?token=j5jr5gGdrZorVYSy6Oyte7udIGgVI-NdVfe3DgzAB9JhtPMtVk0krJb-HlVsajEyY-jZd7u7tHpWbwDZuPBXyPA72N1PV5Xre-eBfl5gt9icDtkSJ7148D2G5d53X-UeZW6xOta7d1R3pkWcpkihOJQnEZs7D14lhxQLVlhq-mHeXUFIHS2R8uvt8dZOeiXKel3l7-_EMGMGhHOhob0Y-bcxuZTM9X2PHib9PUxlkq-KAaKiWmIDj0DEDpVmkV04AU7xzejEkAw9ft1vjvR8pDICvqZD2ABqeh5PposXpcpQGjH9f3Db9yRvazAUWLDMWfuO7SIoi4KVh_NpO5jCcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
رئیس قوه‌قضائیه با پرواز «میناب ۱۶۸» به هند رفت.  @Farsna</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/459975" target="_blank">📅 21:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459974">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb4fefb46.mp4?token=mmhfuJJ9uIuy_wphRF6dMvGfFIe5c10bPwTUdl8ZQyJKCHqgvdzTqi-fbuCH-m7xamKeF-KJWtqV4qTFXEykhtpWX_1SZWkOIiK8Zz7-mW9AMrZPuz5y5CeRTYjsKQTy4zLUrVtDZ9O-cZcP8l4A7Vbvq3NRroINCv7nAqLTOZJpcJGOnzFtw1TApIb8jxyA3RT4N8S4HPYGwZJW9UJc-V553fCqxqfbzTpPXk_F6PEd95b146AUX-EvXiDt0MT4jEAOiypdp_xS87W1cx42kH6rkxIaLwrQ49dN-0A96A4QoTmBAcgz369Tc7eglFgJH_ZI-T3IfHfDGSedcoABTQKHumTwgPZ-K4CpHclPzpyyf8UUgNISfl0W8uelyZoYC2OF18hBd6ksKhj8Sd1Vtm7KndVYxSSnnahygYmAn4-mbuf-REHo4uMjRYwhSQX30tB0gBRbD3LZ8ex3mTsH3sJ_28nPA3k1caKmpar-VnAHCN0fRN6EWh_zlPg4CDODcx5VUadcVeeXNbclOLkxNVF0cLePfMLVbZzlV5ZQGDdDl_uaJFG0BSF3EACYzCkjveMjAKr-a2wGxqYOsrpk7QfyzDETpS_UoBNjZzy02PQ-kT-hIhozNjaxZuo15Fpx3gKdFz5X5R1jJoKX3PT_dkz_5QQwV7pobrZrdpU12yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb4fefb46.mp4?token=mmhfuJJ9uIuy_wphRF6dMvGfFIe5c10bPwTUdl8ZQyJKCHqgvdzTqi-fbuCH-m7xamKeF-KJWtqV4qTFXEykhtpWX_1SZWkOIiK8Zz7-mW9AMrZPuz5y5CeRTYjsKQTy4zLUrVtDZ9O-cZcP8l4A7Vbvq3NRroINCv7nAqLTOZJpcJGOnzFtw1TApIb8jxyA3RT4N8S4HPYGwZJW9UJc-V553fCqxqfbzTpPXk_F6PEd95b146AUX-EvXiDt0MT4jEAOiypdp_xS87W1cx42kH6rkxIaLwrQ49dN-0A96A4QoTmBAcgz369Tc7eglFgJH_ZI-T3IfHfDGSedcoABTQKHumTwgPZ-K4CpHclPzpyyf8UUgNISfl0W8uelyZoYC2OF18hBd6ksKhj8Sd1Vtm7KndVYxSSnnahygYmAn4-mbuf-REHo4uMjRYwhSQX30tB0gBRbD3LZ8ex3mTsH3sJ_28nPA3k1caKmpar-VnAHCN0fRN6EWh_zlPg4CDODcx5VUadcVeeXNbclOLkxNVF0cLePfMLVbZzlV5ZQGDdDl_uaJFG0BSF3EACYzCkjveMjAKr-a2wGxqYOsrpk7QfyzDETpS_UoBNjZzy02PQ-kT-hIhozNjaxZuo15Fpx3gKdFz5X5R1jJoKX3PT_dkz_5QQwV7pobrZrdpU12yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی از دیدارهای صمیمانهٔ خانواده‌های معظم شهدا با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/459974" target="_blank">📅 21:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459973">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">حملهٔ هوایی صهیونیست‌ها به ارتفاعات علی الطاهر لبنان
🔹
رسانه‌های لبنانی از حملهٔ هوایی رژیم صهیونیستی به ارتفاعات علی الطاهر که مشرف به شهر مهم النبطیه است، خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/459973" target="_blank">📅 21:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459972">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e1896b0bc.mp4?token=PaPjLS6lyeF6ShzFkRr9XD4ZubyTK_4vQaoUIw5g3bxmgGs9OIFOVJxiLDIHwq7K7ICKqUuI-44U0lY0zkqve7JIglA5ik8qJEP7M7Yd-Mylby8EZhRcIlJ0ZyiScSkAgqy1tq4QcUCj-p6LZtLYAIhpaMSkTbcbYuDDFt2xXAEb8bdqwpJb9K6n7JpTZSd19TyHtAF-LccOAsPR3u_eZmIPbA9MK4RXDu1WT2LPqST28e-Hd0FRdrIKSKklPGjK4tcyx5kDSRK4ZHibV6ga1k9HFpx5O4fSyeaRGBolKD9xa459umEY55i025L6uJkqAwpWupP8-ada5bvPerr0iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e1896b0bc.mp4?token=PaPjLS6lyeF6ShzFkRr9XD4ZubyTK_4vQaoUIw5g3bxmgGs9OIFOVJxiLDIHwq7K7ICKqUuI-44U0lY0zkqve7JIglA5ik8qJEP7M7Yd-Mylby8EZhRcIlJ0ZyiScSkAgqy1tq4QcUCj-p6LZtLYAIhpaMSkTbcbYuDDFt2xXAEb8bdqwpJb9K6n7JpTZSd19TyHtAF-LccOAsPR3u_eZmIPbA9MK4RXDu1WT2LPqST28e-Hd0FRdrIKSKklPGjK4tcyx5kDSRK4ZHibV6ga1k9HFpx5O4fSyeaRGBolKD9xa459umEY55i025L6uJkqAwpWupP8-ada5bvPerr0iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چگونه ذهن مردم گرفتار روایت‌های دروغ می‌شود؟
@Farsna</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/459972" target="_blank">📅 20:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459971">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2809a2027.mp4?token=duQprFcbTAO1eLwAJGrNPfcCJnBm-vwmox_Fc3_veIQ7uRwwQErneX1ytuU0IM1etbui4Pb5ggFUEmEXAyTMkw9joOl2W8oQvnySU6fzyWvZNDjMZafn3VOopm6N1bpwoHQgtNkwvePHQybLLWa-ju1cwU8K-Y-UG1S2OoD-0qmb2QDPtgLZyX9MGFlCEgOxxHkdgN75r9MWYSZjJIcfPHi4CYlACxQQ3nZAnbuEh_S1wgDblyo7HYvjywUeyktXshgh_JCOFnL76cx8C8RemNjSkKDrBA_D-dkgKdwT_95Da5lwC70KKXndPAGHSNL2MKJuIL3VaoqEZqnv5bJGQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2809a2027.mp4?token=duQprFcbTAO1eLwAJGrNPfcCJnBm-vwmox_Fc3_veIQ7uRwwQErneX1ytuU0IM1etbui4Pb5ggFUEmEXAyTMkw9joOl2W8oQvnySU6fzyWvZNDjMZafn3VOopm6N1bpwoHQgtNkwvePHQybLLWa-ju1cwU8K-Y-UG1S2OoD-0qmb2QDPtgLZyX9MGFlCEgOxxHkdgN75r9MWYSZjJIcfPHi4CYlACxQQ3nZAnbuEh_S1wgDblyo7HYvjywUeyktXshgh_JCOFnL76cx8C8RemNjSkKDrBA_D-dkgKdwT_95Da5lwC70KKXndPAGHSNL2MKJuIL3VaoqEZqnv5bJGQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نفت: قرارداد بزرگ فشارافزایی میدان گازی پارس جنوبی در اسفند ۱۴۰۳ امضاء شد  @Farsns</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/459971" target="_blank">📅 20:56 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459970">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35001b930c.mp4?token=LNhPJ4XTb19cnfGALeKhzAUAxLRr3Kze1rSzVxJD4dy5Uk_1YveE7myP8Dis9B-s0PcqKBG0GhpK79Xz50CwyzhzOLKKL-SGjYOUUr3FDlqi3smz8fk6m6UunqPhjOg2GsQMJdY44q94QpI48U45wWWdDMeaWMi96jj3wxS_a86Hz5lgCp-gjGhroYD1ixt0A-tSfAN7EdMCQozDgCDWwwQe0cPNof28P20WHR2WHsXDIWUxE_3H9liCTsOyGUly80mBSvd2zvhI8_6xAHsmBHKj8bpoz7Utb_B1HtpsNlGyJRIpCCpMQKjBH2afH_cUITa18wSrC7dks46QQXDweRDFCUcHZT0hEdJdE3FiJr5fn-9xSo43rirSGhyPk9gCyLLphTefP2eYP82uGU5tSdQ6xDyXHOHmraNADxgKAz3xzstvAXHl-21MhSUrViAMuKhtOF3H3uT7x2P_9SCWJD0LKu60VOHDtd61IcfPLE--1pKlcld2bl1kUPE0CiPOuOEFDN-HnDq30rmgMVrl_rGBEMKM2IApKH0X4bLxyiBEIiBr3HHHlzQk54ZDpo9Elnlrbc51Q2ZfNTLFBGhAV3IJpGVRVPW2Vr8GEkfaeARQ_eRDpqrwOiLn36B9HijHDUG_WnzEAIPR0FJLmbmn52CA3yL85ya4LDR2YjPwXk0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35001b930c.mp4?token=LNhPJ4XTb19cnfGALeKhzAUAxLRr3Kze1rSzVxJD4dy5Uk_1YveE7myP8Dis9B-s0PcqKBG0GhpK79Xz50CwyzhzOLKKL-SGjYOUUr3FDlqi3smz8fk6m6UunqPhjOg2GsQMJdY44q94QpI48U45wWWdDMeaWMi96jj3wxS_a86Hz5lgCp-gjGhroYD1ixt0A-tSfAN7EdMCQozDgCDWwwQe0cPNof28P20WHR2WHsXDIWUxE_3H9liCTsOyGUly80mBSvd2zvhI8_6xAHsmBHKj8bpoz7Utb_B1HtpsNlGyJRIpCCpMQKjBH2afH_cUITa18wSrC7dks46QQXDweRDFCUcHZT0hEdJdE3FiJr5fn-9xSo43rirSGhyPk9gCyLLphTefP2eYP82uGU5tSdQ6xDyXHOHmraNADxgKAz3xzstvAXHl-21MhSUrViAMuKhtOF3H3uT7x2P_9SCWJD0LKu60VOHDtd61IcfPLE--1pKlcld2bl1kUPE0CiPOuOEFDN-HnDq30rmgMVrl_rGBEMKM2IApKH0X4bLxyiBEIiBr3HHHlzQk54ZDpo9Elnlrbc51Q2ZfNTLFBGhAV3IJpGVRVPW2Vr8GEkfaeARQ_eRDpqrwOiLn36B9HijHDUG_WnzEAIPR0FJLmbmn52CA3yL85ya4LDR2YjPwXk0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم این‌گونه جواب گزافه‌گویی ترامپ را دادند
@Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/459970" target="_blank">📅 20:54 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459969">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3811f3d433.mp4?token=vfSMyf6tIqZmHCqHZOgFwFQbAkEpKyc7-KhMc41b-SIpy5n5qCBp9N5hf5yJsN8FEFutSFOPctniaWAfBk5gwqiPKVODTApyNIJi6jkKoWNgKSt-ef2yDHOZ5L4WFxY-U7XaosS0erjiTKYixP31GNYIFXhn0GJ3pgrULi_LTHNChqJeGjUUcHp783pNQba1J3TE8ME6X0B8lefabePUNVLTtnHIt22jlvLD08kSHPpvD4Xe_J8TeoLiUaqFoLOVIQgl6gi4yyWezIQDhuotbCV2kFKur3s-87KUwkPvCaCLaclKW4JDiR2FgmbDGhNoKMA6E14nt83xdmJDAdQwKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3811f3d433.mp4?token=vfSMyf6tIqZmHCqHZOgFwFQbAkEpKyc7-KhMc41b-SIpy5n5qCBp9N5hf5yJsN8FEFutSFOPctniaWAfBk5gwqiPKVODTApyNIJi6jkKoWNgKSt-ef2yDHOZ5L4WFxY-U7XaosS0erjiTKYixP31GNYIFXhn0GJ3pgrULi_LTHNChqJeGjUUcHp783pNQba1J3TE8ME6X0B8lefabePUNVLTtnHIt22jlvLD08kSHPpvD4Xe_J8TeoLiUaqFoLOVIQgl6gi4yyWezIQDhuotbCV2kFKur3s-87KUwkPvCaCLaclKW4JDiR2FgmbDGhNoKMA6E14nt83xdmJDAdQwKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نفت: قرارداد بزرگ فشارافزایی میدان گازی پارس جنوبی در اسفند ۱۴۰۳ امضاء شد
@Farsns</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/459969" target="_blank">📅 20:52 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459968">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f1a577ef0.mp4?token=l2nNuGIX3YAy1BXG64PhgZvUssrVIu3nEijP0XOCci0L2S4i-PNuUK2myU-M8Se-hOeekqW7pP3no93whOJdKTak3WWkazLJ5p_wKvP11eYcSRxCaw7ULclTCNnBu0RMEG1oI2e7MkXYUGRvOQUh0-yf2_CODWW9QE7vlVuLGcYBgTATbo-JJxqR1l32YpTEQJMeMWBcz7K6MjeB0W8M7ITTPia7vwzQdB32D0n7tzQOBl2olqV22orGSjchunyCo02IfZ8s3uPWfW-SOIA1Q_5q-Mtypb9jc4teKRtwGV9EKlGPrDVscWLMVTB3sfukhY-JGQz4oRlnNjskJzkGtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f1a577ef0.mp4?token=l2nNuGIX3YAy1BXG64PhgZvUssrVIu3nEijP0XOCci0L2S4i-PNuUK2myU-M8Se-hOeekqW7pP3no93whOJdKTak3WWkazLJ5p_wKvP11eYcSRxCaw7ULclTCNnBu0RMEG1oI2e7MkXYUGRvOQUh0-yf2_CODWW9QE7vlVuLGcYBgTATbo-JJxqR1l32YpTEQJMeMWBcz7K6MjeB0W8M7ITTPia7vwzQdB32D0n7tzQOBl2olqV22orGSjchunyCo02IfZ8s3uPWfW-SOIA1Q_5q-Mtypb9jc4teKRtwGV9EKlGPrDVscWLMVTB3sfukhY-JGQz4oRlnNjskJzkGtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ناکامی سامانه هوایی آمریکا مقابل پهپادهای ارتش ایران
@Farsna</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/459968" target="_blank">📅 20:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459967">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GaetN9tGt3OWEJV8ETjL57RxKnaeqJKSXnlg74W85H6J7U_HpHH8ELHp-aXsfVPWMYJ9yZ0DhTPyTSgwGKnYvw6YmxrM2PQpX6tMGVBYXlPK6fP2cZEiDoII9j7VYcCtZDWgG0zpFmy6C-cybDk2SyRjEWk0FhBV45T-bcyb-TbToE7ajTJEQLDrB9HfugOpw4c9sIIFogKQJ4F0gqGR2KE4O76B7nl0OyQJKTUBjKyiRQg9AdEplQr4vK7PJBKWpO2pQDdiuG7II5xzRPbgJuifMVuKMpWob8oww5mwcLckDlARUjZleVCofbjF5oQnQdZA1d_ywodxmtHNAkdCrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف خطاب به بسنت وزیر خزانه‌داری آمریکا: کاهش سریع ذخایر استراتژیک، افزایش بی‌سابقهٔ نرخ بازده اوراق و جهش پرشتاب قیمت نفت آتی، بسنت را در لبهٔ پرتگاه قرار داده است
🔹
«قیمت نفت آتی عمان، بازده اوراق قرضه دولت امریکا و میزان ذخایر استراتژیک نفت را خوب تماشا کن.
قهرمان! هرچی زور داری بزن که در قیمت نفت آتی بیشتر مداخله کنی! چون کل حرفهٔ تو به این بستگی دارد. یا اینکه به تخلیه نفت از ذخایر استراتژیک بیشتر از حد خطرناک ادامه بده و سقوط غارهای نمکی ذخیرهٔ نفت در اثر کاهش شدید ذخایر را تماشا کن، یا به خداهای نمک تگزاس پناه ببر و دعا کن که چاه‌های ذخیره سقوط نکنند. دنیا پاپ کورن خریده و تو را تماشا می‌کند».
🔸
در توضیح این توییت رییس مجلس ذکر ۳ نکته ضروری است:
🔹
بسنت برای پایین آوردن بازدهی اوراق بلندمدت (به‌ویژه ۱۰ساله) دست به خریدهای بازخرید در بازار اوراق بدهی امریکا به امید کاهش هزینه استقراض پیش از انتخابات میان‌دوره روی آورده است. اما بازار تا حد زیادی در برابر این مداخلات مقاومت نشان داده و بازدهی‌ها بالا مانده یا حتی بالا رفته است. منتقدان (از جمله برخی چهره‌های قدیمی وال‌استریت مثل استنلی دراکن‌میلر) این اقدامات را ناکارآمد و بی‌اثر می‌دانند و بازار را در لبه پرتگاه ارزیابی میکنند.
🔹
به دلیل جنگ با ایران و اختلال در تنگهٔ هرمز، دولت ترامپ (از طریق وزارت انرژی) حجم عظیمی از نفت SPR از طریق تبادل اضطراری آزاد کرده است. سطح ذخایر به پایین‌ترین میزان از اوایل دهه ۱۹۸۰ رسیده (در برخی گزارش‌ها نزدیک یا زیر ۳۰۰ میلیون بشکه و حتی نزدیک به محدوده خطر قانونی حدود ۲۵۲ میلیون بشکه). ذخایر استراتژیک نفت در غارهای نمکی عظیم زیرزمینی در تگزاس و لوئیزیانا ذخیره می‌شود؛ یکی از مهم‌ترین سایت‌ها Bryan Mound در نزدیکی تگزاس است.
🔹
تخلیهٔ بیش از حد این غارها ریسک‌های ساختاری دارد: فشار هیدرولیکی، پایداری دیواره‌های نمکی، یکپارچگی چاه‌ها و امکان فروریختن یا آسیب دائمی به ظرفیت ذخیره‌سازی. گزارش‌های کارشناسی متعدد قبلاً به مسائل کیفیت کار، تغییر شکل چاه‌ها و ریسک در سایت‌هایی مثل Bryan Mound اشاره کرده‌اند.
🔹
برخی معامله‌گران نفت با سیگنال‌های بسنت به کاهشی بودن قیمت‌های آتی نفت امیدوار شده‌اند و این در حالی است که قیمت آتی نفت عمان و امارات که نشان دهنده انتظار بازار از وضعیت لاین موازی عبور از هرمز ارزیابی می شود، در روزهای گذشته از ۱۰۰ دلار هم عبور کرده است. آمریکا روی کاهش قیمت نفت آتی این کشورها در نتیجهٔ بازی‌های روانی و اطمینان دادن نسبت به بازگشایی لاین جنوبی هرمز حساب کرده بود. این انتظارات از قیمت آتی نفت، در کنار ته کشیدن ذخایر استراتژیک و افزایشی شدن نرخ بازده اوراق قرضه، وضعیتی بغرنج برای بسنت و دولت ترامپ ایجاد کرده است که تلاش می‌کنند با لفاظی در مورد ایران آن را لاپوشانی کنند اما شاخص‌ها شفاف‌تر و صریح‌تر سخن می‌گویند.
@Farsna</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/459967" target="_blank">📅 20:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459966">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqX4lad8L1b6sOQoG_pMHe0KGdYS_PIgwbLZ_LsiNhaFqxyvCv7a2fDi9s3Mw_TYZ-DRFtk9YcNLXdCEPnL3v5BGhfj3E5SvKdSFUtskSFHfsxEDCKVCpQZ92XOBwJanyfuVh3gXqU1QRn8BJhEvsV3b2wBw277g_9nopZynuYY7rp8Kp6XDhhMGZe598QSV0yUCRfbQ2fcR1Y_XcsmmM29JoepFqMrZlibTFkDf26BQfwkdcKYo-9Puw1kzfndukNYtPdY1b2iOKqSPGeVCSg9_jtMrJ9KikO1X1q7alebNq4HSTqv3L8niSR6zquqz9yrAggmMeWO0t62jcP0FZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطعی بی‌سابقهٔ مدل‌های مشهور هوش‌مصنوعی در سطح جهان
🔹
گزارش‌های گسترده‌ای از اختلال در پلتفرم‌های بزرگ هوش مصنوعی دنیا منتشر شده است؛ چت‌جی‌پی‌تی، کلاود و گراک همگی با قطعی سراسری مواجه شده‌اند که کاربران را در وب، موبایل و دسکتاپ تحت تأثیر قرار داده است.
🔹
نکته جالب این است که این اتفاق درست همزمان با شایعات مربوط به رونمایی از مدل جدید اپن‌ای‌آی با نام «آسترا» رخ داده و کارشناسان حدس می‌زنند که دلیل این اختلالات، مشکلات زیرساختی در سرویس‌های ابری «مایکروسافت آژور» باشد که اکثر این سرویس‌ها از آن استفاده می‌کنند.
🔹
گزارش‌های کاربران در کشورهای مختلف از جمله بریتانیا، هند، فرانسه و بسیاری از نقاط آسیا و اروپا نشان داد که سرویس جمنای گوگل نیز با خطاهای پاسخ‌دهی، کندی شدید و مشکل در تولید محتوا دست‌ و پنجه نرم می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/459966" target="_blank">📅 20:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459964">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/doo3Vg65GQabEauIvMcIvIJMIrWIaTtc0Ea9JTpA8kT8FGQmZfN7x9v1IvTXgtdYkSUmGEMKP_Z1IO84tXlXYH7RNVz94xXbnnj4xUIGNIgPoP5kc-hQ-BrySb8zVg5pbFM3LUQFHlPAsklyS_Ss_Bc11aDMAehoQP8WfRDTXHOuDKSe82_4uYjbqI3i4PuwOQfDWgMdX9V5fiR_l_AkzNyedm6YHxUpyM4jx8yvDhbgQIbchkAHLqsAr0V0xAjDOlbkhaoDBZz-hPB4XgqxtEFzLdTjzmlV199bvYpzJ3xbVhGlbnN37lGlkJKDPBRt-6UNOa00w-BzDltRFgozuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g66Lr9ozo24ficQr_lbnh4Fuffjim6HIfJfk5XKMHC5CAedepNS3Q6uPQyTBKTutIGzkBNJfI5xZRpbmfxIkBw7zZ7GaJKCmFNks-0JIa2uejYnRfRWRMTrHwGgRvVvP7H1CHXjXl00NlJnBMau_wZT7yr-vc9LvJ1lN3o5TgteLITPOtbz0wz7l1tu3kB0Zn7QecoFM1fu0gLnUVkoOGSz6QR0rIBQQe2tbiaoIQKsHyq6PR1o0Ovw8MSdPHqfWayCSIofzmXFnlzDjyNmTSlvMGzukH7S1suinQiU1Rg12D7onOmhTUalONAEBBZXqtYbzhSHpgl_elzvYTNXJSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ رسوا شد
🔹
طبق رصد ماهواره‌ای از بخش جنوبی تنگهٔ هرمز تا ساعت ۱۴ امروز، تردد نفتکش از این مسیر «صفر» بوده است.
🔹
ساعاتی پیش ترامپ در تروث‌سوشال تصویری منتشر کرد و مدعی شد، ۱۸ میلیون بشکه نفت از تنگهٔ هرمز عبور کرده است.
🔹
تنها نفتکش‌های حاضر در تنگهٔ هرمز ۲ نفتکش مرتبط با عربستان و یک یدک‌کش است که پیش‌تر هدف حمله قرار گرفته‌ بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/459964" target="_blank">📅 20:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459963">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jO_vx4rAfRRaLYUwcVH2ITpKQ0Pjz6t9OxQO2oh10UM3Qxt7HfPNi2VV0qeuZPFBw7rNsM8XQK2leEv7kMp3KiCEUl83nUBPYgNAAW_UVwtN5LCJmlYHD6pfRo7nFWeKUJooFiHuqnYY5LAG4vHhrtGcEo41TC0cAuqEG_0koXRfurCb8DKYAIUpLnWzePSRcQUAy2dcSKTKS6VG9ZbO6EpX1Hc-tU5Ot8nouhUmISXT_TlS_BeK-plOTi6yCsPpOzPPs6vLieEemL_tEct43Gu2zTpio5BY4MrBQ4rmM58emAqrUA0KQ6Aj_07QenDl-y-6QIhTlK_ZDdHNsSJFOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسکن تعاونی ارزان‌تر تولید می‌شود
🔹
معاون وزیر تعاون: شرکت‌های تعاونی می‌توانند با استفاده از قراردادهای مشارکتی در ساخت مسکن، به افزایش سرعت ساخت کمک کنند.
🔹
از طرفی تعاونی‌ها چون مصالح و اجناس مورد نیاز را به صورت کلی خریداری می‌کنند در کاهش هزینه ساخت هم موثر خواهد بود.
🔹
با توجه به تامین اعتبار برای تعاونی‌های مسکن می‌توان از تورم در این بخش هم جلوگیری کرد و در عین حال ساخت و ساز مسکن تعاونی هم سرعت می‌گیرد.
🔹
در حال حاضر عدهٔ زیادی از مردم هستند که به روش تعاونی مسکن صاحب خانه شدند و با مبلغی کمتر از ساخت و سازهای غیر تعاونی توانستند صاحب خانه شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/459963" target="_blank">📅 19:58 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459962">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca81a14c1.mp4?token=Qimd7WEVZRIbWKbIYjFa9UehAGY3sHsvTE1me3AtRhLuQM-ZzdxCc1li-4HB4bhW1-XMeKKH8-lYzPTqS6Y3Ld9FvGJSG-A5Xr0Vot0-6ns6amGtcCuGco8sEySB0yHPGyK8Yo9NhrG05ligf-_5JJMtvcCaUKOdoItjpHAA9lM3fd3MZwKV2THDs6xnV082OoHIRgYCFsZq2edsbeJBXtuWAFsM7ZW1gD2oetwqlJdN4TSZ1JTvQW0v0EmPTBlfwxYlg9U7ETdauQRRZLeh4mDnbmhWX0BGShiqG9DBRtJ_UNO_qwYh9Va3aPc7XLwt40DxkX7-OCbQkQvexi-ywQTr6R-uhAnb9kLYd-zRW0QCsdkhixmiMI6E-IxGrzSXwUWBlTmjFsitwOFmmsUDEgJKMG83xUp-9RHyDkivNpA8pl_iPF1FTAnZ-m6HZXc51IVe-hT2t05tMeKtGfeiVEJUYvusNZLSqtr8reneXeDyT6LkgtRTDewBAEIOS9XNa35D2Y4R3YY9tb477EUwN9zE5gcn_faOZsBB91J8yn5ezrFlmKh-EgotYu4EqF9ZlNAbJ_Daq77W7hBvVoLymQFiHkuxKbQBYdhS-MgV-rev3Bo7n1Z2vQ6Oxjqaro7WTs0hT4SWqRYXuN_RCG1Fs1acnS7s_mkeEnBNQlRCvCM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca81a14c1.mp4?token=Qimd7WEVZRIbWKbIYjFa9UehAGY3sHsvTE1me3AtRhLuQM-ZzdxCc1li-4HB4bhW1-XMeKKH8-lYzPTqS6Y3Ld9FvGJSG-A5Xr0Vot0-6ns6amGtcCuGco8sEySB0yHPGyK8Yo9NhrG05ligf-_5JJMtvcCaUKOdoItjpHAA9lM3fd3MZwKV2THDs6xnV082OoHIRgYCFsZq2edsbeJBXtuWAFsM7ZW1gD2oetwqlJdN4TSZ1JTvQW0v0EmPTBlfwxYlg9U7ETdauQRRZLeh4mDnbmhWX0BGShiqG9DBRtJ_UNO_qwYh9Va3aPc7XLwt40DxkX7-OCbQkQvexi-ywQTr6R-uhAnb9kLYd-zRW0QCsdkhixmiMI6E-IxGrzSXwUWBlTmjFsitwOFmmsUDEgJKMG83xUp-9RHyDkivNpA8pl_iPF1FTAnZ-m6HZXc51IVe-hT2t05tMeKtGfeiVEJUYvusNZLSqtr8reneXeDyT6LkgtRTDewBAEIOS9XNa35D2Y4R3YY9tb477EUwN9zE5gcn_faOZsBB91J8yn5ezrFlmKh-EgotYu4EqF9ZlNAbJ_Daq77W7hBvVoLymQFiHkuxKbQBYdhS-MgV-rev3Bo7n1Z2vQ6Oxjqaro7WTs0hT4SWqRYXuN_RCG1Fs1acnS7s_mkeEnBNQlRCvCM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نکات آیت‌الله عابدینی پیرامون ضرورت استمرار حضور مردم در خیابان: دشمن می‌خواهد خیابان خالی شود
🔹
لشکرکشی مردمی از لشکرکشی نظامی مهم‌تر است. مردم نباید خسته شوند.
@Farsna</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/459962" target="_blank">📅 19:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459955">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iu9SOPR_Vg2Txsps84oTR8vVIGzK19XQSunArWgG5-o5kNDwoiE_sDZm4sqvGJKaDmzahNNGhHluC_lPDu3DM_TnSkMMlmX4h1ezKphH_Xw3EFd6WDMaqU4fC2pUm_u-9iavS2fiZzGj7-rNwegdxTPaCTA_-13512JX8kE67Y6DQTGEKkBYnNnYW99-meREjI9h4dUBqbncZAt4dBh-pAxtd9enJ2jOf3gwNjf3ZNa8fiDQThzO7VGPkHHplMtmOxYThPePBsRKf0VTH_LlYGQaU8sStnDvrvZgjKLe2XFWXZqGHVcMi5tvqZRbKmZv4Zo1Ulr9tE1LrCbYc6_6xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p4C9R8R4uZqPAl_6q38QWbBg8yBGRYWnBXHeGbuDa7EYfyzVkv62RAKLVGKVO3MKRklH0_A9fGR8ji0oYET8FHtWUDZ8CBGLsaA1j9VGenXKrumjqUkTTURxqwwytFw3wsho-uHQtpHUhrBHD-6s5_cs1MhRk1yZLDPYiEjRf8nY6HDjRucTdReRASUWboQnDhmm6q1-4DoTfAC4sILjwU3xgbHIiavoZmbErHo4qNKuTIyUk_-HAP8IuBM8qufhcpq5vxqcV0o_72zu5-hIpmEgU3cs74xh_cEP_T0GW8bpmoi3ejYFhcZNFbZ7WcpbkA0gIQ0Eo9BeJO7UcUJvag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aNSUNJOHeN-buYUDL9AHFajC_PVNqUhnJ2ePJNWcrXth8IO3mCGTotlq-ZDqSPnOH8ycYPygD8jk6oo9DfOGpAQvvjmqhFWpLcrVBXwBA_yyvbd9AiC8NxbPw2ESRyXvEpF_CFx1OwjrEw6Q90bW-ydOarHtqwBK-m21RitCc_2JU_cQa2rLioIZ8ikB1XdYHafWh0mryLRndsHUIvFoMHkhsQXfKGziViENCJ3Z99JEgDyuZLPwZFmDNam13dRK3wS0jwGI2jRsOzmuG9isjHM9ifOV4PMZurBMCFqIry5C0TAWGXBkyYhHZoybpkPDnGzj0L77B7gccukfRPDYbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LSxypO-WOoQNl0g6v3UDfGjlYYAaQ8LTjxaKvCxjHYL0IiLqRcDncj7ICnT8NKQFMVAr2oisOvAXwjEvXDcrGWaj7Uso6xCoOfnK_ITyDg3tjhj3eE5FqZtEHzggBUB61mqHI4Rgsd16mcmtTpjf3cCt8TB1AAKFAIbw0gTsJX6qQFInTX0pj7FvvlMPmiAdUVuPtV2-lj7axiDDd5WNkAs6TET5XririDrRf2sW15RhaqGDBwbg3Nb73DZjYA9luaD26OVjTffXgj9D3dLEZCcR8mMGsPkkhhXYPyZicfb1mGjCT_Pqn2NW-N7ZjvYcEfNdjTcPFR8E756IRlhnmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vuMndQ_dMzkQJwbiKsBYFL45QYxExQyB3ByYtg2UfA6llYD_RnBQkyuNGGGEC1cDSi0UVBc7gMtlJ3SmsWHnZTVCft_7mEnmbjxDPsAsnKLb7VPoRPybrV5PgolUZubYyJYO9nivoFabLdSY2DeYo8G9smO92WCU4GEMly23pUtzDCZzNZpGpGZ_OUdkvCn7lhwHPGtxtWbmK4VksQZruNq_FRb5PGcxHjyHb2kf2Zu4_Qm8hHazuhPd1hRT0DPHpysywcp5Iw1Tj7-LlIoFvT9cVbLVNtoi1FacA9_LTXFUIP8PNc87TOnun-2obL8BbrNHkL9_Zaw028FJ7d3cEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LdYaF5Svn7HAsSRsQYbJu4bIEBP4XPCzZbHsXY5HwXmkgMqfVM9-Srq_HPwNKQDQWOkrPrqVaDnLdFyd7Q838thVb4ePT6wTHkMcnqemKVverJo_WkOEXwxVpNy0LAReMVsWEF87b3vatJJYxQIymx0FKWGKa5-a5nPgrx7Kf3HYoXO7cQtcZU8lMkT6VpCZJhyGwaKpEWzF0aW75SEsobM-RVNogOuNH04DUeoVuLfqV21K1RZNFvWAq7NoRS5M0m_1hSl_Q9fGX9x10x4n61KNbyr6Ma5Tqhx-o1zslE8qSoyMfLqu0IHowzNkSYNfadjXR1a8rMiw5OcpANqkCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gW5loaEwOPDcuYHzLzvO4zzc3yLh2AYDU3VGmhZVgDA5WOO-i4vuqxEewaTlzlkVI_jo4eVoicGhrTvWp7tpUKGXTp9AgzIhInczqLGZWjHIAu2d4rejrd3Z5NXDTBfXK2Ge78VMiqzaScT169Q3dkyByotMdDF1c3xljem5Fqv0x3h_Krv4IQNZk1dQXXLM2l3e4cCDN6wOj6R3lNhuJ__NV_iloLk2Cfc02yPY0CCoPf3VWSPn8I4N9j41rCc7XJpI85KN4zm0v62dcys0cHgG0W_Cy-3Bk8atGsRDGhl2djdJYd5x_M9IV2ORRYGNJTXHLmORCTrAKAuklp2jyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشنوارهٔ غذاهای محلی و ایراتی در سَرکاء مازندران
عکاس:
غلامرضاشمس ناتری
@Farsna</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/459955" target="_blank">📅 19:37 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459954">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYzCzdO1tbQw-aFmklmQIL8ZjX1EUpYuPkV1oBqB-tf2d-H1nsUVJFPKs7RGnWtwlOCRGz9J_WUD5MG39pByZHueSJGBmRa3FJOvAvc1bTOLL3tRQUcQHcAa2mffgdCOsf5aG5XtuEdjCynhZnjq-iLKDlk8gB0nlqYK4qUQfkM7yEdM8gKYahPi-49FeK1ZbKU_XpBNZH2MPDfz3YiXHXOwNzL78IS5j49pQaFeSrTF-celN1tdXc5v0ChjVXpXSmtMcb5q3XFkL5ke2F7zznUYMB9eRNTe5MwgeTY6br31Uyo7Oc1GYEeJ7p0QbZYl2zmWQF7rMiXjy0BB-bP1gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحریم آمریکا علیه روسیه به تشک کشتی کشید
🔹
قرار است مسابقات RAF روز شنبه در مسکو برگزار شود و ستاره‌های بزرگی از کشتی آزاد روسیه و آمریکا روی تشک بروند؛ اما درست در آستانه این مسابقات، موضوع حق پخش تلویزیونی به یک بحران تبدیل شده است.
🔹
طبق گزارش ESPN، شبکه FOX Nation که قرار بود این مسابقات را به‌صورت انحصاری در آمریکا پخش کند، اعلام کرده که رویداد مسکو را پخش نخواهد کرد.
🔹
دلیل این تصمیم، نگرانی درباره احتمال نقض تحریم‌های آمریکا علیه نهادهای مرتبط با محل برگزاری مسابقات عنوان شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/459954" target="_blank">📅 19:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459949">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZjpdprvOFfny9BpaRNA2bC-7HjtZM_5qv6cmHeosMr1Ou3mViV9mTH1OsNT1Xcrgbp7hI7tjR0RI5SfRwZaWM3Ip-592EDtTfcXIwm2txyUuIdjkQaq-mU6N3__khURCgbcKPgAvUSgmHVO210lY1K3eQJQuPAl0vC_m0yksB1LTvS5f2KJ5XealPl3h3EiqIkP7u6zqKF0rafkg3O5N9DY-2NWoFMMowEvDRGaWYUcPb99nrcgD_Na4FC0dwSgXeg6ZJ1bzDcLh39RrJDiWBlJU2h-sFRvS7I-MqWVRthsPDDZQNpNcJgMicFX_ANE9k2DdkEuoBvegK45nnamqqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j546J2JiVKsST72xasiUxk7lhnejLnOayHSKMmNhBMth_Z1s7xXhMng4U80cHM_obJWC-xVEoVGUPC1mN5Y0C9orPtS6JJPsqeOprg7O2eXYLJcqaW2VtKiqtdvkgrDHm-OLaVvo_3fMRuGc-nekeiWT1ptF9dgCcXUOlAMEqboSP_rEE4mMjuKMk6LCPZZYHS7euXceNZz75U91Bd4mvPSCNIhh952ROThw9GkcC4vqs5VR5frxch3qiDx_MR9zb07v6-LuTWdAreW7TlmYFuTMkKWAln3DRcMViSUufPVRvYv80BASoeuDaPlXM3fEM5uB4Mr07nurFBsds6q6SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IK-YfGIZDp2wBo4X_fi5MNk3rq2wx70ZqDQzUJFiz9sgVc9s-JkHtiLdl-90bPnS8pWRuOUAL_UvTQY59NCijz8Bi_jp4SFelv1WpFcaCsJgTpllu3BCjQGJbAyDBVbg00FcIo4e_z0FIik-NJFT9affaC6ayiUAuHsOEvKePPXE902ZhbYaYHqY_B4sDYm5qOHMCz5NGe-4PTQIW0ukY9Gc0_jCZUKq_VP8CgTKPQhT3t-Hl7m__tXaqYSthXXweQ5pMUFuStJIDR1W7bR4VpUcEky_DSDv7YpGxDq_9hrb5bhdeaFUbON4HBzDTw2c_cEAIyStLxa_yOqSia1Fyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bb6FUUutPsiBMqJ8mr6O__IeaySvo8cC-Cyf-eZ4B2jAX4DgTPSXvvsjRadz9Vj1FPKeVKtEym4ZLUtABGyuCd8Cc7LWf77I2Z3i8z_u6stH-GSpiZftF59aZ2cqDwuBMerzDhDY8CIpt-CRPj5waKMzqB8_3-qlkYWEa_vO_XUAraGShHdNfZg79TLju_QSk-yqLtNRt_itgWL3iR5pafHLA8PM_4oXmDt6z4Hro4T9o0xDMBS3GfU7o93t7IqJk40-bS0vlUQGz0RSPQ3pC27jUM0of7s6x8p9De-pqzXVcMYcRiLOaxSZPaWSZVy6dpjLx89Aj1h7pb4uJbPBGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ccmAax4WuTn_3z9Yt_Xk71Mpt4l_jKFi1YUfB592VuiFT-sAHB_pUtAQgwGkuBclQCWzS80GHwbzgpnB7i9JRY_hgTQCsZEVdIXyHLdNWwQjMVzEPPTwwiYuwBA4VDkpBSo5kzagETXAXStEmCyI12-KqhLDszWDxkSNobt54WJf8RAAUOBX6v0NTZe6x0gQAjdWJS6dY2323ojo15ytZAQLMqUCJW_h8GEAaSEU8KpzE4lDsx36XSrBSEjAl_hhcxhnNGhSZN0y5CdaxKQlMc8BZDKNLZqcYhfOjGM_C8BCzbdSPnWhN9UZOqojMTT_ZlViqwxk_xxgIxmO0hVGjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بدرقهٔ سردار شهید جعفر کهریزی تا زادگاهش
🔸
پیکر مطهر سردار شهید جعفر کهریزی که در حملهٔ دشمن آمریکایی به شهادت رسیده بود با حضور مردم در روستای کهریز کرمانشاه به خاک سپرده شد.
عکاس:
بهروز احمدی
@Farsna</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/459949" target="_blank">📅 19:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459948">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnKDOgJV2MzuC3Z1i4WG9cWImwiC30KlnXdfCD3fbI6mViHwp6753R41xn3R5o5dBcxr6qMiogwh7y_vcoJrzviYhPtBoYpygkgQLPM13Up8YbW32P_zpAvWNKYh9c7Ao6f_MigmwVy-atyYRMBvIYWR6-tjiYVNi77rWU6oWz4fIBXiapwC6jhm0t3srsPDhUaE10OUE9QlX99EPxZJ-uBysofuSMGsj6aXr5ZZabfnDAwWpLjvtIsyy5nQeW4Pds4dNzRXDQBe_YsbaKCLxQcg1uFqkd7ld9d73kj5PD4yp2L8Ud7kmvVKvj6WSMdbWeuXi2jUBcsp5HF4xdlt3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
مقام کانادایی دربارهٔ ترامپ: با آدم بد نمی‌توان توافق خوب کرد
🔹
رئیس دولت استان منیتوبای کانادا: «همه دیگر رئیس‌جمهور آمریکا را می‌شناسند؛ او بی‌ثبات، غیرمسئول و غیرقابل اعتماد است. به‌خاطر ترامپ است که ما در حال حاضر هزینهٔ زیادی برای بنزین در جایگاه‌های…</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/459948" target="_blank">📅 19:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459947">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQIl33MSvF8RPn6tkPgO9m9W9y-MNyBOjI8JiYNGVeJcY-vKkkVWElvWwCvwpt37cLoeeRRF0Do_FcAMlHxjkoa-ANNGpO59Hg8mfnVZpgKjdVAsBXE3Fut6cM0FgOAHYUYsdVnK1pvcQzGnCVf-StsdV0kkPWNkfuAVuNqAvjYS26KNHxDcuD3uTAke7soxPvhSCJKyUqHu_gtzvu2cyYcwHumJ1c5d7aWnMbVchIVO80tqAjM_uThvbOC9XGGTDI2zAEgT50_q5XVO3dDaJNQ503_4DDvswEBxFx-IVy5e8yyBlQqBCte1vNSloyPL-JrK7SbwMXzOiXKAaN_V1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع اسرائیلی: حزب‌الله خود را برای درگیری گسترده آماده می‌کند
🔹
منابع نظامی، امنیتی اسرائیلی به شبکه عبری «آی۲۴نیوز» اعلام کردند که حزب‌الله لبنان، همچنان به جمع‌آوری اطلاعات درباره نیروهای ارتش اسرائیل ادامه می‌دهد و روش‌های عملیاتی، الگوهای تحرک و محل استقرار این نیروها را زیر نظر دارد تا برای احتمال ازسرگیری درگیری‌ها در جنوب لبنان آماده باشد.
🔹
به گفته این منابع، حزب‌الله در حال به‌روزرسانی تصویر اطلاعاتی خود از نیروهای اسرائیلی است؛ اقدامی که در صورت ازسرگیری درگیری‌ها می‌تواند زمینه را برای بازگشت این جنبش به روش‌هایی مانند نفوذ، کمین، استفاده از پهپادهای انفجاری و کارگذاری بمب‌های کنار جاده‌ای علیه نیروها و خودروهای نظامی اسرائیل فراهم کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/459947" target="_blank">📅 18:56 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459946">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udxjBTZ91oomLpVncVrpJ6juw98GXZqPtBW6znFR5sNSiQT2-7_Uwnf9znxKC4qdGMyXM94fo4_uhWmIsVJOERh0LOF2ukXR4RzHLZVwc_xSqtJ1bs2ZlOHyHAvA0hk_NxUlOq9B0xOtP46L6iN99j3-6QwU1yfQmGP3E7AjzKJdhp_nG-TqIaqiy0xJka4Irj34VzHIu6rkbwXzBnFv61owiMuUheTZ3hJiajgPZt9qbcOPdUFfJT3Ptzgl2xl3uDTngjPna3PG8a2Y3qWnllBuw4ONVmbOF_mId-RMe4nqHCwu82fVGxEw6T7HxwsOuidemonwTCTvoPj7Wvti4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
افتتاح بزرگترین و مدرن ترین تم پارک ایران در مجموعه ارم با حمایت بانک شهر
🔹
طی مراسمی با حضور جمعی از مسئولان و مدیران حوزه گردشگری؛ بزرگترین و مدرن ترین تم پارک ایران با نام «دنیای گمشده» در مجموعه ارم، و با حمایت بانک شهر به بهره برداری رسید.
🔹
به گزارش روابط عمومی بانک شهر، احمد مالکی معاون اعتبارات و وصول مطالبات بانک شهر در این مراسم که با حضور معاون وزارت میراث فرهنگی،گردشگری و صنایع دستی، معاون بنیاد مستضعفان انقلاب اسلامی و برخی از مسئولان کشوری و لشکری برگزار شد، گفت: بانک شهر با سرمایه گذاری و مشارکت در پروژه های تفریحی و گردشگری گام های موثری در راستای گسترش فضاهای تفریحی مدرن و ارتقای کیفیت زندگی شهروندان در محیط‌های شهری برداشته است.
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/farsna/459946" target="_blank">📅 18:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459945">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-jffVPLhM0jS-k157iDMs1SGBkCGHoAH1lVVm0E4bIz_O3v-QZHmbfZdeXM0rFRdxm9YgZCZzIB470E2Wd1HLBcPSi-TWDI0WhiQ3GlJPjSE3yIfxgcMx2K0WOJmrev0ddAzzclxfDokgJYwBh7upiTh7J_2c9ZxaZEy6C3FCII8Ug8cY-43Eg3gjb4p972fM14fZgl6lNnmWi1H4WbtmugyHWWa5ousfru8WS7eyLyq0nn7pHMssp9RQPqks2X-nIqM_8jOkct-K9r6e4mH2qeeGd37llwCLu03mkoBmPlGoOzdeVk-tXYadYy2HsgJC2PsnzpzmOJHD3c3WCr_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🤦
حل گره‌های نقدینگی و توسعه خدمات شهری با ابزارهای نوین بانک تجارت
💠
مدیرعامل بانک تجارت در دیدار با معاون مالی و اداری شهرداری مشهد، بر رویکرد نوین این بانک در مدل‌سازی عرضه پول و تأمین مالی هدفمند مبتنی بر زنجیره ارزش تأکید کرد.
🔻
دکتر اخلاقی با تبیین کارکرد ابزارهای تعهدی در ایجاد نقدینگی غیرتورمی، بهره‌برداری از محصول «ستام» را برای تسهیل امور مالی و بانکی به شهرداری مشهد پیشنهاد داد که با استقبال مدیران این مجموعه همراه شد.
🌐
مشروح خبر
👉
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/459945" target="_blank">📅 18:54 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459944">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/459944" target="_blank">📅 18:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459943">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9_OFDYP2Doyac-yFzd5GN9PGlmUauumx74F56gI0mdn4DxHZ0_8anXSuGCPwbsm0ZaFKR-F2s5HQyKmnAFi0diizPFAfrKGli8iuKWHEGcf4lRFhQ63OBO76OnEH8Yd6rtUhuZo2zXhJAB_besGrz9Pi18TvJsT7qxZD5EwYcPVg4bGkjeA_uZilmLJ3DsGVSOI6w4UAnfkw8oS6VyQjnhBAW4KsDBL0dVOpzvtkopooOWPViiPbViJr18fek9fTcc432zwV1qzyuI-1_9GFHfNast3Od8hCtNsgQbjr3YvUnunQTuL8eeDfyDTnXtRs2Uo8lUHZfKaL-yw5W0Geg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: افرادی که می‌گویند آمریکا مهمات ندارد خائن‌اند
🔹
ما به مقادیر تقریباً نامحدودی از مهمات درجهٔ متوسط تا سنگین دسترسی داریم. ما این مهمات را برای خودمان نگه‌می‌داریم و به بقیه نمی‌فروشیم.
🔹
دولت بایدن آن‌قدر مهمات مجانی به اوکراین داد که بسیار بیشتر از آن چیزی است که ما در حمله به ایران استفاده کرده‌ایم.
@Farsna</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/459943" target="_blank">📅 18:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459942">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bb7ybUM2vfnLxXGqVoMb4L_EiEvcYqwTNip2FGpP1OnVFmbfpVWYz41f71VsVQgEXauKvaM73FoBJ7ZjZ8Vn5zC1ZmuEC-HDfIuz0KXuMKqw5wG5FJoKwn_lgFH_AGfUpXMEVLNqmGNGQotwg6-P_7fyteXVmW47luLjxXmhndS5pfMKA4jd-UNQXKNWCBQO8hhUkLlhv_5FwfE9wj-k9UxD44xIb0e-s0WrO6LAHv5W2rCIr2gzE_fMJfDGxiGxqy6brIKabjjcjr8y5meWdEoH9tVy5wBKXPufLc_65OMkuWdC2V6ElLTmEu9GfUFqptqIlluQKMZvOiYpLyj-1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پای پلیس امنیت به تتر قسطی دیجی‌کالا باز شد
🔹
چند وقتی است دیجی‌کالا فروش تتر به‌صورت اقساطی را از طریق دیجی‌پی آغاز کرده است، اما کسب اطلاع خبرنگار فارس نشان می‌دهد پلیس امنیت اقتصادی به این موضوع ورود کرده است.
🔹
دیجی‌پی از تیرماه امسال وارد حوزه معاملات رمزارز شده و امکان خرید چهار قسطه تتر را از طریق پلتفرم «دیپکس» فراهم کرده است.
🔹
تتر یک رمزارز با ارزش تقریباً معادل یک دلار است و قیمت آن امروز ۲۲۱ هزار تومان بوده اما در طرح فروش اقساطی دیجی‌پی هر تتر ۲۴۰ هزار تومان قیمت خورده است؛ یعنی ۱۹ هزار تومان بالاتر از بازار.
🔹
طبق اعلام دیپکس کاربرانی که تتر را قسطی می‌خرند حق برداشت تتر خود را ندارند و تا زمان تسویهٔ کامل در پلتفرم باقی می‌ماند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/459942" target="_blank">📅 18:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459941">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2m1XZG6wsgcu2R9clk3qw3lOWVep1kkkNv8PPDX6b7_Zus-4cyNB0DSqibKlEJvDhexxlNrbcyrjlagX3QCgYM3lx63XhG5BT12o4yWRNMGm0ht-Dt23suXdXpBwJ6YrcJh0WqUL_Df2LcoIuCEhjWqNCBj3G6r6iBTK5QTQPeidQscUJKSxso2iuhVNCmCRk4ZPF_mRu8NvMJ5Y-nZKns4NxJYbxVM-byZDj6M7CYAwtJn2FQSI-BLqm8L_8icNydkT_MXI5OQFR7ZCmkUZC3L99AGKMH-6uoNQbibEcrWlc3koxXDVfD4Q1iO1LjJ8wABFjDWNLlBEWmg6116dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر ترامپ بابت انکار تلفات آمریکا در جنگ علیه ایران عذرخواهی کرد
🔹
هوارد لوتنیک، وزیر بازرگانی آمریکا، روز پنجشنبه به دلیل اظهاراتش مبنی بر این‌که هیچ آمریکایی در جنگ با ایران کشته نشده است، عذرخواهی کرد.
🔹
او به کشته شدن ۱۸ نفر از نظامیان آمریکا در این جنگ اذعان کرد؛ این آمار تلفاتی است که آمریکا آن را پذیرفته است.
🔹
گزارش‌های متعدد رسانه‌های آمریکا حاکی است آمار واقعی تلفات بسیار بالاتر است اما وزارت جنگ دولت دونالد ترامپ برای کاستن از فشارها آن را پنهان کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/459941" target="_blank">📅 18:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459940">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VM4trdFu_YS1Fg70gipqgRQ09orTnH0fuu0JKIMUx-2xPmRauREjd34lOBC-v9fEA4IGbV7F-7NKIxubWqLd0T2MY7oFGkf_mu82htrwo8fR-L73YZPZzEa-yKeC5hSltGAxQ24XbAaP_bAX6R0KgbgDnFCfFYEyZumr95TWtKdd32IY-wtI01PCj3csA1_m_OacdHfgapj6vZysSWPeyDlM45uZKOFnII-SPT5SCU-vDE-Ee9iVKWHJempCDk-5Zxj_zGx0cRD25hz0B8vi4H_lRvt50sqaDhv_GyC0Mq9c3vFP3QbMvrGXovexbbXOfITn6VBEGZWrr-Ku-xThVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمار شهدای حملهٔ آمریکا به مراسم عروسی در سیریک به ۵ نفر رسید
🔹
رئیس دانشگاه علوم پزشکی هرمزگان: آسیه مولایی‌نژاد، ۲۲ ساله، بعدازظهر امروز بر اثر شدت جراحات وارده به شهادت رسید و به این ترتیب شمار شهدای این حمله به ۵ نفر افزایش یافت.
🔹
در حملهٔ ۲ شب پیش آمریکا به یک مراسم عروسی در شهرستان سیریک، ۵ نفر به شهادت رسیده و حدود ۷۰ نفر نیز مجروح شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/459940" target="_blank">📅 18:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459939">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4f7afd1e7.mp4?token=d_RQfgNMxtQMdimpejyDbZqQnaV_vrn44Tw6hFdpQb0IjgfMiXxwReDjfgmxnxv0X58CJsEccoDizi5BU_55UeW9qN9wNRaYRqrhGJyF9iVGwd1eNHNsClxNZ1b5GdiBSj5tacIGMl2QN8DvIUoPEqx0fc3Kt-9AfA9O1lyiXxBDt3F_qKGIl6BBZlFWyCu7Y6Z8sRe5mgedU-1oAwv12t5THUWGh0pj-5KgvC6b27vU5kPVBSzrKdypcu2qb5nbqENbplH9e7exRoZXHFBLch70dhBx5656qu6OcO5tA4ay2O5zsruh8REeV9-idt1C3sSu5GLxll-HyvowEWwVbVfYFtbVf3qZnpjNMcJCHgU9LfNwEayrEVRdmKzSIPy44HffLSmhM0DYlkXe6ge07db7YXoJqwKz6FINnwHs2LvTweWQVE15nJjYwQnoOwu5uyeOgYYmQk8KoqsEVlzbOKQzDwGJqdpTUz2AS_PEqqkqhSFYbCEKH9hcp0ocS0P2UlCt_M8SoG0tIA_xYzFKB5-2wZ6nmm8-qtrsdiWnw8tkb_FNjw3Y_B2Q7Drxs3DGHeRJ2jYXDWkKhLBWk6nGJvMD1WdmT3N9phbc8b78ldnSRI4yujc6oePX6gF1EX7BwwJVYTSScUq80K8qYw7Zn2_sxcZExSLG2b895Ijc1uc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4f7afd1e7.mp4?token=d_RQfgNMxtQMdimpejyDbZqQnaV_vrn44Tw6hFdpQb0IjgfMiXxwReDjfgmxnxv0X58CJsEccoDizi5BU_55UeW9qN9wNRaYRqrhGJyF9iVGwd1eNHNsClxNZ1b5GdiBSj5tacIGMl2QN8DvIUoPEqx0fc3Kt-9AfA9O1lyiXxBDt3F_qKGIl6BBZlFWyCu7Y6Z8sRe5mgedU-1oAwv12t5THUWGh0pj-5KgvC6b27vU5kPVBSzrKdypcu2qb5nbqENbplH9e7exRoZXHFBLch70dhBx5656qu6OcO5tA4ay2O5zsruh8REeV9-idt1C3sSu5GLxll-HyvowEWwVbVfYFtbVf3qZnpjNMcJCHgU9LfNwEayrEVRdmKzSIPy44HffLSmhM0DYlkXe6ge07db7YXoJqwKz6FINnwHs2LvTweWQVE15nJjYwQnoOwu5uyeOgYYmQk8KoqsEVlzbOKQzDwGJqdpTUz2AS_PEqqkqhSFYbCEKH9hcp0ocS0P2UlCt_M8SoG0tIA_xYzFKB5-2wZ6nmm8-qtrsdiWnw8tkb_FNjw3Y_B2Q7Drxs3DGHeRJ2jYXDWkKhLBWk6nGJvMD1WdmT3N9phbc8b78ldnSRI4yujc6oePX6gF1EX7BwwJVYTSScUq80K8qYw7Zn2_sxcZExSLG2b895Ijc1uc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع با شکوه شهدای حملهٔ آمریکا به سیریک  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/459939" target="_blank">📅 18:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459938">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73d69df331.mp4?token=h0jW_oPCgggWJOai0ff0X4CXrwhb1c9oSHHlLwcKa2pJNZRID5pvO_sILIJoZ5h1flzkL74Y_87jnWraJpQ-z1R9FwRoDuK5kmkua-XocGfveBmQ17K8FbF6pj6iUO5LuKhnBng3PnriKrsvmquGlKjVwLMfKaWMYMbMXzgeTxwm3TaK1JfPAHcSdjzrKrZD8HcmslMvPqn5U227GOxwHDRKrcJlqwFCN6PWRXVUa342IQlYw9YaYr6VneWxxNbrzAGBxC_EBL7LdAgetSyMW5OFHYdhU-XbZACX0qbeh9R5n53haetZtMVaapRtUJbNMR_0s2yvfujhe-R_AgWA6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73d69df331.mp4?token=h0jW_oPCgggWJOai0ff0X4CXrwhb1c9oSHHlLwcKa2pJNZRID5pvO_sILIJoZ5h1flzkL74Y_87jnWraJpQ-z1R9FwRoDuK5kmkua-XocGfveBmQ17K8FbF6pj6iUO5LuKhnBng3PnriKrsvmquGlKjVwLMfKaWMYMbMXzgeTxwm3TaK1JfPAHcSdjzrKrZD8HcmslMvPqn5U227GOxwHDRKrcJlqwFCN6PWRXVUa342IQlYw9YaYr6VneWxxNbrzAGBxC_EBL7LdAgetSyMW5OFHYdhU-XbZACX0qbeh9R5n53haetZtMVaapRtUJbNMR_0s2yvfujhe-R_AgWA6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تشییع شهدای مظلوم عروسی کوهستک فردا برگزار می‌شود
🔹
روابط‌عمومی سپاه هرمزگان: مراسم تشییع پیکر مطهر شهدای مظلوم مراسم عروسی کوهستک که در جریان جنایت رژیم آمریکا به شهادت رسیدند، پنجشنبه برگزار می‌شود.
🔹
مکان: شهر کوهستک، از بلوار ورودی شهر تا گلزار مطهر شهدا…</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/459938" target="_blank">📅 17:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459937">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrsAmp2VwDGp4FoXS-02qCzSdnmgVSS6jk2YLfs8JMjBBkmVA0gkksyeWt_BY5B8gqnHR_qBhb0lkpTVRzkXiB4wxVb9gABwsJc62RjrxEfAERpnSfrug3lbz5M-krKoRb3gB0l82goJOPjZx4beU46w9cdSk1qUXUbhe7-NWrkOYn-RntOMe_D-GEy4os-6ofgz5czRUfQFfOKkErsW8a9ER5DkWL8zI_aWhzEUQq1bjX6LGS5aVdNqgFWWlgjbRmYj1-c-H3mdnXISijzoxI763jwcQDrj4J9mL7cenke_vzJBgXsl2o3jFhHaDkPilI275JZtojlGKUuH2sxi2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشکار جاجرمی نایب‌قهرمان مچ‌اندازی بازی‌های قرقیزستان شد
🔹
محسن میرزایی، ورزشکار جاجرمی، در رقابت‌های مچ‌اندازی بازی‌های جهانی عشایر قرقیزستان با کسب مدال نقره به عنوان نایب‌قهرمانی این مسابقات دست یافت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/459937" target="_blank">📅 17:56 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459936">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfkMjmu5IefWzvq-TsiMENKVNnMSMN9lo5y1qmGtEelEdaXraoK9DWeTbyIuHo7Xa8kIDKkWx1l45_5qtb1Tc-LCs_sE0kZoEsQ_stoEzbb7Jrx_CmwvzBnktP_Jy__68MwAgytwhdWV80trKjHmu-xp9RVsUV_O3pZAqWWoWMyesnmQjY3zk3QoNATzSbadYaMDuEWOlOyBR4uMfO1Tbf0Ylle9aU5iPrVxy0S9awRc8AO6xJ4_tV5ghw3WEfanZmYQ9IPm8-1_h89g657wHZ9CmRdI91nhq-KmvGbneI0fiYbt2ppYHaQ-_wEUhvUtoNGyBV_ucXB_2318ZfN7LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران‌خودرو قیمت خودروهای مشمول اسقاط را افزایش داد
🔹
هنوز ۳ ماه از افزایش قیمت محصولات ایران خودرو نگذشته که قیمت مصرف‌کننده محصولات این شرکت باز هم افزایش یافت.
🔹
خودروهایی که از تاریخ ۲۲ اردیبهشت ۱۴۰۵ به بعد پذیرش شده‌اند، گران می‌شوند و ایران‌خودرو می‌گوید…</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/459936" target="_blank">📅 17:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459935">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8bbf88ef4.mp4?token=cRmekn1NIsyA0UmSvXWGK9MEaZNQkI0Ji3c1acvEAwqimHihqGzjimnZk9OjjL8Lg4vcIqtnTyzdquLebhUO4pjcO3qF6DMTNNRAFHjZWak2Sgayt4kP0ZhYZHDx5FCiF49iFwpYyXJ-EmkNW4sA0qE-298WNkDc5gZzQ8eJEfNUwheT43Eqie9idyLYfPUdoierVidSyeSDdiX7-bnlK0gaapLeI0HYcU21NFQfZl_OplvfF2jWlEYIMzOXxU1JHga74NuEKI_b3rST-RsYd2JuL-edV0Q_p1uO4G8Qf3JH_jH-hTsiP08LUQ8E7juv9mZSNGPss7f6ckVNEAlP_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8bbf88ef4.mp4?token=cRmekn1NIsyA0UmSvXWGK9MEaZNQkI0Ji3c1acvEAwqimHihqGzjimnZk9OjjL8Lg4vcIqtnTyzdquLebhUO4pjcO3qF6DMTNNRAFHjZWak2Sgayt4kP0ZhYZHDx5FCiF49iFwpYyXJ-EmkNW4sA0qE-298WNkDc5gZzQ8eJEfNUwheT43Eqie9idyLYfPUdoierVidSyeSDdiX7-bnlK0gaapLeI0HYcU21NFQfZl_OplvfF2jWlEYIMzOXxU1JHga74NuEKI_b3rST-RsYd2JuL-edV0Q_p1uO4G8Qf3JH_jH-hTsiP08LUQ8E7juv9mZSNGPss7f6ckVNEAlP_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت دختر کشمیری حافظ قرآن، از کمک‌های مردم پاکستان برای خانواده‌های شهدای میناب  در برنامهٔ محفل ستاره ها
@Farsna</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/459935" target="_blank">📅 17:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459934">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e81f42667.mp4?token=YPgJtam8TNtQ6eVxQPRgmyzPOtucdKE6u--kOTHfFjyl5LUV0JoozkmGvdJ4qwr7LdANoZFlR9Q803ScAFNGDbCbWLIew26L3mDFxZIqg3t1cDGEc2-vPQ5P1Eiq-6rFH4AqglrWi5Zegi3Q-u7SO5sDGEhzd21BmyPIjKrLe33Mf86pThM3VoBUvyMWcWCvAU18N7r4si3RGEx46faklbCff8xos54I_Of4Z07gZQzKxjWIX2IaQBg9jnIgxeyol2hRq1emAGF_Gj_rJawYkS5ef62ecgBk9PyAtl-EIgOpMk0EGj4W0zqoG9IQUz_Liz59tyni_W9hNZBUduQa9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e81f42667.mp4?token=YPgJtam8TNtQ6eVxQPRgmyzPOtucdKE6u--kOTHfFjyl5LUV0JoozkmGvdJ4qwr7LdANoZFlR9Q803ScAFNGDbCbWLIew26L3mDFxZIqg3t1cDGEc2-vPQ5P1Eiq-6rFH4AqglrWi5Zegi3Q-u7SO5sDGEhzd21BmyPIjKrLe33Mf86pThM3VoBUvyMWcWCvAU18N7r4si3RGEx46faklbCff8xos54I_Of4Z07gZQzKxjWIX2IaQBg9jnIgxeyol2hRq1emAGF_Gj_rJawYkS5ef62ecgBk9PyAtl-EIgOpMk0EGj4W0zqoG9IQUz_Liz59tyni_W9hNZBUduQa9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تفحص پیکر مطهر ۲ شهید دفاع مقدس در چیلات ایلام
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/459934" target="_blank">📅 17:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459933">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZXyQpOiWkbVJTMNG7NJlKTMr7BWgaZVsQIOKA4scyRhVguiPGyNZ0yB9YYNcDKlAlbdzhdyXQEWbraoHlDMMuAj_YIiPqLFXWyQqnVdwyA6c7-kjsfywBDA3dOKxG_HZ38n7OFdBSvuddfFB0QW2NRTElPqz9OTGKP1ScD_dMeojg2DoHvCBEQvpeDiNbZwP239jq4gG0XozFUb08Q7NKjcpnfJ_d1LlFcQZA9SjZhd_InutII8RvgzCGEEOul6pTQzafHNu4AGQTFJjEK6fRS-HVBfWaCoaPXdTetbCiFnD_J5WCoj8_clmj3eZRtmitKG1ESQ5QKsdTqsEMhvEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵ اسیر لبنانی امروز آزاد می‌شوند
🔹
رژیم اسرائیل قرار است امروز ۵ اسیر جنگی لبنانی را با هماهنگی آمریکا آزاد کند. برخلاف گزارش برخی رسانه‌ها هیچ مبادله‌ای در کار نیست.
🔹
شبکهٔ ۱۲ تلویزیون اسرائیل گزارش داد که آزادی این ۵ لبنانی به عنوان «اقدامی از سوی اسرائیل در چارچوب مذاکرات میان ۲ طرف» انجام می‌شود.
🔹
در مقابل قرار است کار جست‌وجوی اجساد چند صهیونیست که در خاک لبنان دفن شده‌اند با جدیت انجام شود تا پس از پیدا شدن اجساد، به اسرائیل تحویل داده شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/459933" target="_blank">📅 17:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459932">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92eda2be7b.mp4?token=QENex_D58XPp8qHuqXE7WSslgeoWoVNMWuE7X7cY4ddPkGsPMcjuxv_R01wNBpfnOpSuOp7fwRxR2dVVTtqwPrqwmsWgh3mzbI6QX4bcmiE1o5ZgosApElWdii1jvU954SruqhLMGQdGDcYT3hdW9AMBRGlnu0nBLKf3Bqq69cP-Pcm5HIeo_jj7OxXJZQHI3Nq1hMu1VyM0yFSboYqg83yQRCUp8DOrtJEuh_97a5O49Q0jMgLc7eLnKAphsBBrNM74nb1UEzIk-eprV8FSEKuOwzbhUYb1Q0uFW_pd1Cszykz9Bp6xAGoO6g2nOUTtf1hmfKoUXhTWD72mcluJYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92eda2be7b.mp4?token=QENex_D58XPp8qHuqXE7WSslgeoWoVNMWuE7X7cY4ddPkGsPMcjuxv_R01wNBpfnOpSuOp7fwRxR2dVVTtqwPrqwmsWgh3mzbI6QX4bcmiE1o5ZgosApElWdii1jvU954SruqhLMGQdGDcYT3hdW9AMBRGlnu0nBLKf3Bqq69cP-Pcm5HIeo_jj7OxXJZQHI3Nq1hMu1VyM0yFSboYqg83yQRCUp8DOrtJEuh_97a5O49Q0jMgLc7eLnKAphsBBrNM74nb1UEzIk-eprV8FSEKuOwzbhUYb1Q0uFW_pd1Cszykz9Bp6xAGoO6g2nOUTtf1hmfKoUXhTWD72mcluJYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام پناهیان در برنامهٔ سمت خدا: دوگانه‌سازی و دوقطبی کردن جامعه، همان نقشهٔ صهیونیست‌ها برای ضربه زدن به انسجام داخلی و عقب نگه داشتن ملت است
@Farsna</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/459932" target="_blank">📅 17:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459931">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رسانهٔ اسرائیلی: موشک‌های ایران به هتل نیروهای آمریکا در اردن اصابت کرد
🔹
رسانه صهیونیستی «اسرائیل نشنال نیوز»Arutz) Sheva) به نقل از گزارش‌های محلی اردن گزارش داد که موشک‌های ایرانی که سه‌شنبه شب به سمت این کشور شلیک شدند، به هتلی اصابت کردند که افسران نظامی آمریکایی در آن اقامت داشتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/459931" target="_blank">📅 17:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459930">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55e904617e.mp4?token=K5jH9866h7yHmovMbAP17NMFt9_MT_Ef4R8-97FZEcU47A5tuJLIMQEQha8a-C77hDwq4XyoL--S6AbZWNXQqVdlzscIiEgz_Ivq-tHRFxJ2q6CmfK4B6p-ddpy3GkFaIjoMFRN25A_Q4_486ntZdJf15zxs6cy_fFCR8VAypdvNlOeM-Nqvz3r1grDZlufNoTt8zJAxw-FiUd4krAsUPPj25e4dcDDaVHJ0pIxR_efUqdDTHzjKbh42tjX0TtS-5K4CdY_jJGBBJsl4--RVxxZ737mbkC8tDLOcGlbdG6WyrQO7iYpKJta6R6q51TVgWzr4hzoTtUidq1vmp9W20w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55e904617e.mp4?token=K5jH9866h7yHmovMbAP17NMFt9_MT_Ef4R8-97FZEcU47A5tuJLIMQEQha8a-C77hDwq4XyoL--S6AbZWNXQqVdlzscIiEgz_Ivq-tHRFxJ2q6CmfK4B6p-ddpy3GkFaIjoMFRN25A_Q4_486ntZdJf15zxs6cy_fFCR8VAypdvNlOeM-Nqvz3r1grDZlufNoTt8zJAxw-FiUd4krAsUPPj25e4dcDDaVHJ0pIxR_efUqdDTHzjKbh42tjX0TtS-5K4CdY_jJGBBJsl4--RVxxZ737mbkC8tDLOcGlbdG6WyrQO7iYpKJta6R6q51TVgWzr4hzoTtUidq1vmp9W20w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نیروهای صهیونیستی با تانک مرکاوا به خانه‌های باقی‌مانده در حومه غربی شهرک حولا در جنوب لبنان حمله کردند
@Farsna</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/459930" target="_blank">📅 17:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459929">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bolf7HxhZf3AkuAbxNH243XYRGbfxMPTReEbl8xvCA0cWb1rTmRm7YIR4pni99zq9UUbnENnUNk9T2ziz-7sIYhX-KH-cdRoWWUj4p72WwCOeoiEawyXOjXLU0qOPoieIagN4FhYsCltzZqQPNKr8EcSKOkDQXs9IoBitpfqHooGr93BJovB2gy2C7WodNbA5skoMRlSxvT9PbagiaQNIgJwFbQ9_7TFRvCtBtqEZYs5u4Bho03SSdDtqFeDP97nADyGaZeg2HjFpgMITR3pahhwAhDj_1z0rNOZNmyLhoxO1gQqGOg8-K8wTwdVW9DD7Cynwch42JsuZ6oaA4H35A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقائی خطاب به بسنت: تاریخ فراتر از خاطرات حیاط پشتی خانه شماست
🔹
سخنگوی وزارت خارجه:  در چنین روزی، بد نیست نکته‌ای را به وزیر خزانه‌داری آمریکا یادآور شویم. کسی که برای توضیح تصورش از ایران، به خاطرات کودکی‌اش از حیاط خانه‌ای در کارولینای جنوبی و کشتن مارهای سمی با قمه و شن‌کش متوسل شده است.
🔹
اتفاقاً مشکل بسنت همین‌ جاست. او عمق تاریخ و تمدن و غنای فرهنگ ایران را با مساحت حیاط پشتی دوران کودکی‌اش اشتباه گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/459929" target="_blank">📅 17:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459928">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tfy167kNNFI-7--U9zMdRUckwBCUnI17mLOoQ5pMYrY_A3VZ1tFc7bAEPJWHhgeoJu5dXQKRBD3Uk-qX2TfWJdCqZB8AJX-Tr3eXFaJEzOYu9wi69tICrhcIRt3DVeLn1d1Pn4gBBRc2n1W6urxNvScocTU4MvNmIroNL9NKOqqwnc9ogK1EDAVrqO3nR89KZDaQ_gsD6FA34eOAWtJ8ILy8eGL591S2Wyh8mr8lrl7Oe0fwvV7S1XWTmrb9lWoxHn7KX8S-yB-wfPvZJRZWJkc-Tg0oALkeELu7VClHwqEcFnDwHAxCn8QlQkGcrQ2Ix9ufQG4H7zsOLs9gEemhUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستگیری تیم ۷ نفره از عناصر وابسته به گروهک‌های تجزیه‌طلب کردی در ایلام
🔹
روابط‌عمومی سپاه امیر المومنین استان ایلام:  یک تیم ۷ نفره از عناصر وابسته به گروهک‌های تجزیه‌طلب کردی شناسایی دستگیر شدند.
🔹
این عناصر با تامین مالی و هدایت سرپل خارج از کشور، اقدام به تهیه سلاح نموده و به دنبال اقدامات مسلحانه در شهرهای غربی کشور بودند.
🔹
در بازرسی مقادیری سلاح گرم شامل کلاشینکف، انواع سلاح کمری و شاتگان به‌همراه مهمات مربوطه از مخفیگاه آنها کشف شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/459928" target="_blank">📅 17:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459927">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">📷
نیروهای مسلح یمن تصاویر جدیدی از هدف قرار دادن تجمعات و خودروهای دشمن سعودی را با پهپاد منتشر کرد.  @Farsna</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/459927" target="_blank">📅 16:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459922">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pk6T2hAVhKMRzOSFnB2Mz46ivNuFlZIRmuYfQkp24-ZdGLj_WPep3xRHxoZnm8Wgm6ejxavxOKlxMP-cqXgU0MSAKN1SuYwyOEjDBxjE25eXHLd8Oh_M538dkK6LM52-wdD5IPUfv5M3KVwsQdERDbdKf9sEmz-7Tdcx35eUF-WnXrcA1aEfn_wQ2FlQphwhz90PPc9ckx4xZWt5Ip_qfI0A2z15AnaNx40EDlvVLIUL1f6WydN28v-6aGfBZ2NqZzQlSpnnPB47baerRa8t1JkXpz6VIGAJrjcROJNTsBW7KdE3q6kjjqho-ldnQwhxQRJKBGgwBv1mU6cFN9Evhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NTAIoKL90IE-CbCqROUzJ1T9qP6l8ApsgepjTPyjkolc6C14FohlA5wFl3O2dFnwu0x5hi_J5U9ATwk3X3nizueRQhkkqyyv8mIAdTgNT_6qcCVd3mgPAJ1fExaPh_g9yM8QORiVgyhjs_b7xxLa0Ykes1cDZJwgs9udFogELqJjc1eo6w9eDxlUWd81pN8DozrxNMkc1-GPLJprOKNavGqOGNkoCY1dC-hRV1EhR28lKleFYCF7mj0UVhpIGqinY1M82A-iGkr2wM2K5K2S6s4SmmlYItZSVx3Rz3U50IodUyhaW6QCo4O93lU8rU_dZBd42oSjx1i4jARvVX8TDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZI3bq-GsoIn9w1u4FyvGViHXvmsUorVNzUh_WYQwJLRGFJnLeasGgXvzkwN9sHxl86ZZVQSmsCZkZe4OFZyrfQZcTgI3oWR3wP1CbBcEvDp-YxmmTqixa0KaBwCKy2MO-1G9ToqxeIdISCLCDM5y01Ux6YSLHpHi1MhI2a7IcS_vuncBpDyPc5jo60wc6rHpH36QiCQ5WQnUXdLM0iptYW4HgWEKl3085WYta6oaHuXqrN918KBJ7SUVYS9NewbFKnVEhb02Gv3PQryDyMKoq6D6qZT2tYY8KV7GRbfZkLdWzbYzOl1tDP6pFD2wMqw2o8HyXX1WKDeQXa_Zuw-jXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z33kKb4-uc-dHNN-64QNSFOpjevdKZGB0QEnyGpiWae6Zn-aAaAMT8NxeAe04E5csWaaoejI2zqioq538UiDsHPymoV_9wzKvK1MzWLu6mDDTlN2sCQ77G_i0-00ja4L3CelA2xUMV3JIQuS8xMkYP08w9wMfo8saELpUZG-za_3SDUY4Vr9p6PJjx0WskXyn2lxpZEP066rmkN_EHaBTlc_6BAjlGSdWPOKn5fEA9T4GDY4Oxynjm5esJ-ndfdrhaUuMdrkEqmlbgsO7kmH6a7oTTFHVO8vtD6G-PLZzQ6vswTpzVM0f0l79jSUyT9GaAA08l-O8dQinxINQXA33Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LozPo3Z_x1W9J_lN02qKsfYwk8WQAiQvSCsORLefZp-3BctdhhDJFbgXaKQpWEy9Z8LYKHf5AQjbDtRDHt5w0yLDwctu7HdF5RpaIisONMg_quKACe4Rn-ZU2KluS_c8STcqhxb_g83YV-_ZL4QU3MTNgtQUivmoZmlXvLgC7HkIWg0IE6_bta26cOLyX1dbm8XHiBdMLktWCq4sQcbajnImA2KdHjt7SLpyNdg6aoBfxLIX1r9Z9iLVapEbmjKd_bYOw28_dccTnAZaERTd3dWXNVkiVOCLs0stm_-TEdLN-GWohwo2tk6oknWVJa_qmjPq4vpt-WQLq_rXtz95kg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نیروهای مسلح یمن تصاویر جدیدی از هدف قرار دادن تجمعات و خودروهای دشمن سعودی را با پهپاد منتشر کرد
.
@Farsna</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/459922" target="_blank">📅 16:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459921">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6y5UGouFv7Gsgrn99f-ESXu5tUm9zHzz3JdyK8YNpbtnFAfbCrD-YWl8X4QI0RRwDfp4Jtdz0icvIxgeTO8GGJevtgC9M2Uidc7fuOwgWrB8uezPCezuVQ0xGLC5fOKm5Osco6VfoIWIF5ghjCKrtdBuKY2TcTZ0HYLaV9KlWqXc1jtD-pzG_qT0XAniBV8h66GY3VzABpcculdSZ8SWSjwQA4PUnQuTZ5zJ5Ks_hJd7Dnf642nQ5jLc4CTRjQlzU-k4WBZIr3ni9Wqmr7vkR0zC-wz7A_Of8xKS_K3o7fIvMEyg-mCAet5iOOqSKNGpa82bf2U8C_FiSJdX7ZBuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رئیس مجمع تشخیص مصلحت نظام: جنایت جنگی سیریک نشان داد تمدن آمریکایی چیزی جز توحش بزک‌شده نیست‏
@Farsna</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/459921" target="_blank">📅 16:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459920">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‌  پاتک پارس‌جنوبی به تهدیدهای ترامپ
🔹
مدیرعامل شرکت ملی گاز: با اجرای عملیات انشعاب‌گیری از خطوط گاز ترش، زمینۀ بازتولید زودهنگام پالایشگاه ششم پارس‌جنوبی، فراهم شد.
🔸
پیشتر زراعتکار، معاون برنامه‌ریزی وزیر نفت از بازگشت حدود ۴۰ درصد ظرفیت آسیب‌دیدۀ پارس‌جنوبی…</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/459920" target="_blank">📅 16:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459919">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gje_rk7aAm-GkpPGusgPa9XoxL4kR0AEFso5uVXACh-hez5eqGq6N8WoFifnsl92GEhAw4L-Ik39RhPvWAehR2QfKyveZGaWgFp579NkCV4APW_Kt5lEJEKjeA1_wnXdI0zGBI199xzxqacUg4L837OLe71_qonmc2NsG2MH8kO5pZlk79sAfwcq1ZjH2Sn-aMJ1x7A958LBgQPPPM2YVlD-5tljDorPZmvA-wlmJ-fsRu6qTpt6NVQtgFPuQq7SIV80Kqe0iZmEwRF8g8tiV1V9KpfC5bn4iU-W3drRR2_VQPBf0pgG28kLgZoDyOXbqTKnUzNR3Hl8-v0UsuRJhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتش: همیشه مطمئن بودیم که روزی با آمریکا خواهیم جنگید
🔹
معاون تربیت و آموزش ارتش: مجموعۀ اطلاعات ارتش آیین رزم دشمن را دائماً رصد و منتشر می‌کند و آموزش‌های ما نیز معمولاً براساس آن تنظیم می‌شود.
🔹
ما همیشه مطمئن بودیم که روزی با آمریکا خواهیم جنگید…</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/459919" target="_blank">📅 16:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459918">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c27655e7e.mp4?token=M6lSvyAd6HxIsJeUz74wY8M7awVWKSVR1xBveSB2JjbpU4zqUpybl3MQcxTncElYWec4tA9Z6GIBooXPVYmqaSNmbIjHGqmvDi-Zi37Bpx3cYUKMj5wbOYOlKf-xvr8eutU8Dyrdy1sTSYFaA6J2m6gXujgHYA2Wj5Bho6s8LYtmLBXyd6225rkUNvqlebmlUtuRJTjvh9pSqxUFLX2ujkZAjMhDA_t26x-ImTT0Omtydy3eHfnUweGueIJjPiJ1sYIdLdJP0aV2zeFM0wq3RuWPbM5j2_LkYo3w-3inCWIkBQZA40D0b0s3MM4JdpuVHAbgEg_RNfs7JC0Y5SbMZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c27655e7e.mp4?token=M6lSvyAd6HxIsJeUz74wY8M7awVWKSVR1xBveSB2JjbpU4zqUpybl3MQcxTncElYWec4tA9Z6GIBooXPVYmqaSNmbIjHGqmvDi-Zi37Bpx3cYUKMj5wbOYOlKf-xvr8eutU8Dyrdy1sTSYFaA6J2m6gXujgHYA2Wj5Bho6s8LYtmLBXyd6225rkUNvqlebmlUtuRJTjvh9pSqxUFLX2ujkZAjMhDA_t26x-ImTT0Omtydy3eHfnUweGueIJjPiJ1sYIdLdJP0aV2zeFM0wq3RuWPbM5j2_LkYo3w-3inCWIkBQZA40D0b0s3MM4JdpuVHAbgEg_RNfs7JC0Y5SbMZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایشگاه الکامپ، فضایی برای عرضۀ محصولات دانش‌بنیان
@Farsna</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/459918" target="_blank">📅 16:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459917">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ce05RXJ8uuKgjzmFly9VFfMBY8aVLSaihYE2lxFQQMYkY6J1ltxbM-ofYM6cqF4gGVRWKMv5klxNsoY3jPFwuNuwXm0XzSjF10fTCgnkcpNTNm3ZVffNiFTMIz9yOoqhZ3HuKU9tPQWfj-m3ogXzyUklAkf2nkh2JXAzXit5cf6wx4wsOTJ_Chcv_a3RkMyO0oMsMqMDYBSFpoe3pfRvpiCPLlKTglE5bREpCwEh2vIZ3pfkdlHfl9eC_S4UKNmT0o29ACYs_DwA2bwOfNJDBqAEgGvUxlD3YI2FXaD1gqm9r_lnAWFLREFjVESCsNHkPh8EOnND9x-QT8yQnZ1LXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتش: توان حمله و نفوذ در همۀ سطوح را داریم
🔹
امیر علیان‌نژاد، معاون تربیت و آموزش ارتش: دکترین نظامی ایران دفاعی است، اما آموزش‌های نفوذ و حمله در تمام سطوح و با تجهیزات مختلف، از نیروی هوایی تا نیروی زمینی و دریایی، به نیروهای ارتش ارائه می‌شود و این…</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/459917" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459916">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTOKCBxHcEp1Vkm-4QbumIEv1GLmfesCUeGvo3z_iIFcAcDvq3yp739G-A0FDZvWG7ickpiifD5FnFpSAfkw5mwGku4Dz-5AhN0hiXzsA024kCmJiu6buv6Qfx-YKMmwj0rRx5LbqKGlxwMxjJt2NfPBeMcf7UkCzJeeGvy9PaqFYrWTACr3kOutdL-mbuXvzzH3L2EpSlHK9bZZ9qdMuDpyx4FKknBIUrIVdo5zpxdy8IvI8PLCIYUbu272XVdvlL9j-rzHXunlFdNvrGLSx7yd8hVGKsYkkEkAljXMBNSDDfvLePF88Trg4GchWOnUksiYDQu9jXVF3n9pgvrp2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتش: توان حمله و نفوذ در همۀ سطوح را داریم
🔹
امیر علیان‌نژاد، معاون تربیت و آموزش ارتش: دکترین نظامی ایران دفاعی است، اما آموزش‌های نفوذ و حمله در تمام سطوح و با تجهیزات مختلف، از نیروی هوایی تا نیروی زمینی و دریایی، به نیروهای ارتش ارائه می‌شود و این توانمندی با دستور فرماندهی قابلیت اجرا دارد.
🔹
رزمندگان جنگ‌های تحمیلی دوم و سوم آموزش‌دیدگان دانشگاه‌های نظامی کشور هستند. ما همان‌گونه می‌جنگیم که آموزش دیده‌ایم.
🔹
در جنگ ۱۲ روزه آموختیم که هرچه آموزش‌ها واقعی‌تر باشند، کارآمدتر خواهند بود. این‌ها درس‌آموخته‌هایی بود که از جنگ تحمیلی ۱۲ روزه به دست آمد و الحمدلله در جنگ تحمیلی ۴۰ روزه مورد استفاده قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/459916" target="_blank">📅 15:58 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459914">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
سرلشکر وحیدی: نیروهای مسلح پاسدار حرمت خون شهدای کوهستک هستند
🔹
پیام فرمانده‌کل سپاه خطاب به خانوادهای شهدای جنایت آمریکا در مجلس عروسی در کوهستک: بار دیگر چهرهٔ خبیث و اهریمنی آمریکا، در اقدامی تروریستی و ضد انسانی، با هدف زدودن شادی و نشاط از صحنه زندگی…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/459914" target="_blank">📅 15:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459913">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
سرلشکر وحیدی: نیروهای مسلح پاسدار حرمت خون شهدای کوهستک هستند
🔹
پیام فرمانده‌کل سپاه خطاب به خانوادهای شهدای جنایت آمریکا در مجلس عروسی در کوهستک: بار دیگر چهرهٔ خبیث و اهریمنی آمریکا، در اقدامی تروریستی و ضد انسانی، با هدف زدودن شادی و نشاط از صحنه زندگی ملت شریف ایران و ایجاد رعب و وحشت در شهروندان غیرنظامی بی‌گناه، در معرض جهانیان نمایان شد.
🔹
این جنایت هولناک که در حریم امن میهن عزیزمان و در میان جمعی از زنان، مردان و کودکان معصوم در یک جشن عروسی رخ داد، نشان‌دهندهٔ عمق دشمنی و کینهٔ دیرینهٔ دشمنان انقلاب و نظام اسلامی و عجز و ناتوانی آنان برابر بلندای ایستادگی و اراده پولادین مردمان این سرزمین است.
🔹
سپاه پاسداران و سایر نیروهای مسلح، پاسدار حرمت خون این عزیزان و دیگر شهدای اقتدار ایران اسلامی در جنگ‌های تحمیلی دوم و سوم آمریکایی صهیونی به‌ویژه نبرد هرمز بوده و با قدرت و صلابت هرچه تمام‌تر، حافظ امنیت و آرامش ملت و مملکت اسلامی خواهند بود.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/459913" target="_blank">📅 15:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459912">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b774a39ae0.mp4?token=hRATx7JHD8_tVvDbFMaeklQP3mHZjL8h43NcWrG8FknCIJm8luLXZ7qSHmFEKgqCvxELbl-qDoRqAx_er16tuPaaX9-jUnCBxrmxsYoA8vjZzL9woNawG_AIVEiKWfY2mnnKMHkS1uSlJvHbxkPpXLDdCcxhC5GE187DYdPXazC1jXg2ApOlwzvCv3boHEUzxf_0AlCv0ElIR5yx_r5F56nrDk434A5BD3qvgtO4pk_VrgdsvzLuEh3y1D3URaqki20MdzXifjL1kjBE5drBzI6M26KcPe-3uvuc8h39HHMsNqJUWQUfy0AjHghu9j9V0fkG2EANeyzgkEmmIqWWzr6y26np8lajB0tH4pSuX2gkDLwyF4C_JwQCK6hzaPYmAWRIQ3gyr7K49rNrMQjvtKjZ-PNACNEkkGUKQvKpj8t16O4uQpGc1FEyMSdkjomD8ZumjuMMKMn1bU1aYUid6cK1FBMFksfbcdH2ZxmTrQBwlDNMYN17eGVxJ36oJlU-PkbDGoO9nVzvcJsPh_f7PB65AL6X_cf9Sro3uw8eIx3ANi9z7w7H7-EpI10PFAdvsSSEuwDOfZWaeukt0eOVsUBoSTcGk5lHoEx5EtTZ0iBpK0RWc2rdD3ZTedL4nmKwiyeGtEtmhXXwk4b1x7ERcg9N6FbAfn6ft8J3zhJmCac" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b774a39ae0.mp4?token=hRATx7JHD8_tVvDbFMaeklQP3mHZjL8h43NcWrG8FknCIJm8luLXZ7qSHmFEKgqCvxELbl-qDoRqAx_er16tuPaaX9-jUnCBxrmxsYoA8vjZzL9woNawG_AIVEiKWfY2mnnKMHkS1uSlJvHbxkPpXLDdCcxhC5GE187DYdPXazC1jXg2ApOlwzvCv3boHEUzxf_0AlCv0ElIR5yx_r5F56nrDk434A5BD3qvgtO4pk_VrgdsvzLuEh3y1D3URaqki20MdzXifjL1kjBE5drBzI6M26KcPe-3uvuc8h39HHMsNqJUWQUfy0AjHghu9j9V0fkG2EANeyzgkEmmIqWWzr6y26np8lajB0tH4pSuX2gkDLwyF4C_JwQCK6hzaPYmAWRIQ3gyr7K49rNrMQjvtKjZ-PNACNEkkGUKQvKpj8t16O4uQpGc1FEyMSdkjomD8ZumjuMMKMn1bU1aYUid6cK1FBMFksfbcdH2ZxmTrQBwlDNMYN17eGVxJ36oJlU-PkbDGoO9nVzvcJsPh_f7PB65AL6X_cf9Sro3uw8eIx3ANi9z7w7H7-EpI10PFAdvsSSEuwDOfZWaeukt0eOVsUBoSTcGk5lHoEx5EtTZ0iBpK0RWc2rdD3ZTedL4nmKwiyeGtEtmhXXwk4b1x7ERcg9N6FbAfn6ft8J3zhJmCac" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایندۀ آیت‌الله سیستانی: ایران قدرت «توانستن» دارد
🔹
شهرستانی، نمایندۀ تام‌الاختیار آیت‌الله‌العظمی سیستانی در ایران: سال‌ها دشمن تلاش کرد ایران را از فناوری و ابزارهای پیشرفته دورنگه دارد، اما امروز فرزندان این مرزوبوم ثابت کرده‌اند که باتکیه‌بر توان داخلی می‌توان در برابر قدرت‌های بزرگ ایستاد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/459912" target="_blank">📅 15:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459911">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52391e8544.mp4?token=M6JEtJ5mNoO97YfSaaCYeK0UX_7SgWOnCkqh_wgq8_hAETS0N9Pjp81eOrnNtC9TS8Uh9kepS4UpLgwbO0zf9xvRBmasE-0wdkScs2gY5IO_9piBcFUQyktJqSWSGQpfNG2AZjsX3ijSOIAC4kaSvIMZPTCJM09GbCF_O5ejU3bNPcpQ2YG29ti3CnOWheuf5NoLNhFWBBvFVYqeo4xeMNkitRz1OZr-JAUezJEvlQT--aAsU7--Ww28ocDe-jbZWJcCA9UUo0-V7gzTKCzNXZfYiAqPmrInGUy9fffSiJpfyvBGPvzLHkpvrkkXLVY2ue4NcGadkIj3SNGwja-5Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52391e8544.mp4?token=M6JEtJ5mNoO97YfSaaCYeK0UX_7SgWOnCkqh_wgq8_hAETS0N9Pjp81eOrnNtC9TS8Uh9kepS4UpLgwbO0zf9xvRBmasE-0wdkScs2gY5IO_9piBcFUQyktJqSWSGQpfNG2AZjsX3ijSOIAC4kaSvIMZPTCJM09GbCF_O5ejU3bNPcpQ2YG29ti3CnOWheuf5NoLNhFWBBvFVYqeo4xeMNkitRz1OZr-JAUezJEvlQT--aAsU7--Ww28ocDe-jbZWJcCA9UUo0-V7gzTKCzNXZfYiAqPmrInGUy9fffSiJpfyvBGPvzLHkpvrkkXLVY2ue4NcGadkIj3SNGwja-5Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌  دیوان عالی حکم ۱۲ سال حبس و مصادرۀ اموال ساعدی‌نیا را تایید کرد
🔹
مرکز رسانۀ قوه‌قضاییه: حکم پروندۀ «صادق ساعدی‌نیا» در دیوان عالی کشور تایید و او به حبس و مصادرۀ کلیۀ اموال منقول و غیرمنقول محکوم شد.
🔹
همزمان با کودتای ۱۸ و ۱۹ دی سال گذشته که از سوی دشمن…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/459911" target="_blank">📅 15:00 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459910">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a1ad3bfd1.mp4?token=Yny8gXUaz5KKwjs5q6cS8m3Wsko995N9dAkcmC4cu47O_M_f4UBgK6QW5pA6EdsMZi9mYZ5ONWLwE-jcnvksBnS-Zk4Vm2021VHGKG_0JmqkT8akwE2hIlJWJghWjickOaIDQcErRrMHXw45pW3Wa0a9cOsXhcNlHqY9rlw2lysXAeJpO4SQdxYaLoAz7OufVOaWbGdQSlP2qsKjXpegCjNZZ66D0H8t27Mmkm6MZK4qg1XkS8TewP3i6bMg_boqjMLluqG8D91IUv4F4U-34aOROBNjOa3tlBqHeoVGWuDqluRjVEdnP7kjS94WqzpcQxZiKpks7Hp4H9l1JGHKIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a1ad3bfd1.mp4?token=Yny8gXUaz5KKwjs5q6cS8m3Wsko995N9dAkcmC4cu47O_M_f4UBgK6QW5pA6EdsMZi9mYZ5ONWLwE-jcnvksBnS-Zk4Vm2021VHGKG_0JmqkT8akwE2hIlJWJghWjickOaIDQcErRrMHXw45pW3Wa0a9cOsXhcNlHqY9rlw2lysXAeJpO4SQdxYaLoAz7OufVOaWbGdQSlP2qsKjXpegCjNZZ66D0H8t27Mmkm6MZK4qg1XkS8TewP3i6bMg_boqjMLluqG8D91IUv4F4U-34aOROBNjOa3tlBqHeoVGWuDqluRjVEdnP7kjS94WqzpcQxZiKpks7Hp4H9l1JGHKIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شکست ایران مقابل کره‌ در کمتر از ۴ دقیقه
⚽️
تیم جوانان ایران در دومین بازی مقدماتی جام ملت‌های زیر ۲۰ سال آسیا با نتیجه ۲-۱ مقابل کره‌شمالی شکست خورد.
⚽️
ایران با گل دقیقه ۴۷ محمدمهدی جان‌نیا در آستانۀ کسب پیروزی بود ولی کره در دقیقه ۲+۹۰ و ۵+۹۰، ۲ گل زد و صعود ایران را به اما و اگر کشاند.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/459910" target="_blank">📅 14:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459909">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3a1ebec2.mp4?token=k5L7xY7qpUwBbddPrPYoaUF-zAemaeKGi4Hav4wTQ2vuYZ4zKDbRHPxcjr-DnHawbwFpk65-vJLnojY042Dlc3tGuzjTQf55oeCxS6KDrn5TSougV5Fv5IViAeDR9X4Zk7aXWsSmYBrJ7tEnvKb5qGlpzFYRXjZY2z04w6NlI_cADBrCMwjOMYi2mZP4fNy0MUUIiSvxA_ZeCjFKr4_oMkspnLdaq3N8LZZY6nomBSozFQih1YuwlSlcS4zElwKt12alwVtNsNbpFxlHhiDI4U805uktw4LFCnx08qH-FXi5oqW7ZE8cIOmAW0Zi46TA6gqzXfETg3Ypg7TfLU5p3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3a1ebec2.mp4?token=k5L7xY7qpUwBbddPrPYoaUF-zAemaeKGi4Hav4wTQ2vuYZ4zKDbRHPxcjr-DnHawbwFpk65-vJLnojY042Dlc3tGuzjTQf55oeCxS6KDrn5TSougV5Fv5IViAeDR9X4Zk7aXWsSmYBrJ7tEnvKb5qGlpzFYRXjZY2z04w6NlI_cADBrCMwjOMYi2mZP4fNy0MUUIiSvxA_ZeCjFKr4_oMkspnLdaq3N8LZZY6nomBSozFQih1YuwlSlcS4zElwKt12alwVtNsNbpFxlHhiDI4U805uktw4LFCnx08qH-FXi5oqW7ZE8cIOmAW0Zi46TA6gqzXfETg3Ypg7TfLU5p3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پایگاه‌های آمریکا در امارات و کویت زیر آتش حملات موشکی و پهپادی ارتش
🔹
در انتقام خون پاک مردم بی‌گناه و دلاورمردان نیروهای مسلح، بامداد امروز، ارتش «سامانه‌های ارتباطات ماهواره‌ای»، «انبارهای تجهیزات» و «آشیانه هواپیماهای جنگنده» ارتش تروریستی آمریکا در…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/459909" target="_blank">📅 14:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459908">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b4ac6bc55.mp4?token=RO3dekiYlHIigAWA4qb6-D74c6PY82z0hagm6Io71c-ZqnLdz33OkWPMwXZWI51StSvU5j_Eej2fTOSvR1Romtol6u7xv8kUHlYgjWkLHRFx9xNqVSPLVLJxhNEIGwtqU8qwb3x1C29EH8hGwm3zkkKE4s-0QpMvFFtzVfh7sGn2gfsylmuUn6XySjLqLLwNPJQK7KCRthCShcbVWqkAMRJ1iQvQqJt5CcoaKzTKEVMXYsIupeRPyFLdAOBxkEOJcszXbuDZwPZfVq_3aGLcE5pLsLg_rDAe2UZh0BQbjOOwdocBbdZ-ve9BTFSoeJHVdO9nGrBBQXfbvIginBZSJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b4ac6bc55.mp4?token=RO3dekiYlHIigAWA4qb6-D74c6PY82z0hagm6Io71c-ZqnLdz33OkWPMwXZWI51StSvU5j_Eej2fTOSvR1Romtol6u7xv8kUHlYgjWkLHRFx9xNqVSPLVLJxhNEIGwtqU8qwb3x1C29EH8hGwm3zkkKE4s-0QpMvFFtzVfh7sGn2gfsylmuUn6XySjLqLLwNPJQK7KCRthCShcbVWqkAMRJ1iQvQqJt5CcoaKzTKEVMXYsIupeRPyFLdAOBxkEOJcszXbuDZwPZfVq_3aGLcE5pLsLg_rDAe2UZh0BQbjOOwdocBbdZ-ve9BTFSoeJHVdO9nGrBBQXfbvIginBZSJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: طرح ثبتی‌مبنا از نان شب برای ما واجب‌تر است
🔹
اگر بتوانیم مشکل معماری سرشماری عمومی نفوس و مسكن ثبتی‌مبنا را حل کنیم، مملکت را می‌توانیم درست مدیریت کنیم.
🔸
سرشماری عمومی نفوس و مسكن ثبتی‌مبنا قرار است از آبان امسال به‌جای شیوه‌های سنتی و استفاده از پرسش‌نامه‌های کاغذی اجرا شود.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/459908" target="_blank">📅 14:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459907">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oObJ8pmj7rd9kWLk7HlNsUwfRZl68StbpYq3TlIZDLjR3ze9VOoc-IjBUXPlvieLckzFAzqYgkPr0zubhTERXWg0vE91TLojgVh3xFxmB22P9w5zpyj0mooJG4jEVhkUDOk37Xfp6ID7chh56DqcEjuOYuPlBWqM8MKt4fnozt5G0LJI5kmt8VxVODECQ_Q-GsmPvFP-gl9_K9YcbVlaW17K2Jt5MdbS_sG0JSvVeDkRtcgE9xqf4r0nttLfXmgRcEyV4VcfgbyKWfA89h3Mg4AiH3g1mnFn2mxvvjAho6SmEv6VBn8lKuF13HJwp7UzWvQc0vUo_SOSTqdJRhmgTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عارف: ماه‌های سیاهی در انتظار اقتصاد آمریکاست
🔹
آمریکایی‌ها به فکر ذخیرۀ بنزین و سوخت باشند
.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/459907" target="_blank">📅 14:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459901">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FEZkIeByoWBXBp76WvxPcCatFT2f8Qk135mv6k5zHgLRBAWvBt2rnLDdo151Cin6zSNIoJKr_N5Wis1jIFQk6GvzhiLCSvcF18w-ElChmvtFOm85gTec8Zu9SYvYbOlFaqEwkog3_YWqzvcwCCjeoJnSLGaP7yIJipXBpcpqwfWickAz3nyT6Sn4Iaag3nGrZS2if-t7qKpUqtDJs7-OdUO6JsktmJlQYlS0EyVEAuy1aF2WyeIyKw1xTqNYKV83mefxZIhkafpK8lFykhDzyUDNRl_vp1Fb2LR3q4Lf9UM_70gZQQmzIbjmmWssa0vE9nh9i2amhL3_ENsyPVhNXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vhD-shVZ3PXcd66w1NxhWEewpYHHtWu9Z3Oa6ziuOp1mh2V6y4kkKKjKWdMAB2ppXxNLNndORzsDCEhW0aI59b0BypuGom6U7V6WM_txkPIzUXZWiC8kkLBMLkKC5CP6HUxIYN1hvkMt6m06L3yMViXjZYKkaWsnZe9VDW2vYGTekYcnnEDr4hHLYJ-rPEcPI3B6nJSmhId6lwCrdzFMESTR_EmsqvyShgihkZrxl_mu8Lp5iD3_6wZoY0tE0V6Ljd_9eKjnedqic7Rvs1QWC15iwuZ8xPP1XG0A0f6ALDNgDvupWwqlQt29QbHv-vTNc0yF-bJq7pMprXu-_HDJwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bd9GsU_8p1fpkFTO9AlFhgxZMHY3McU3M6jjbR-u04vtVUTlwrPw-n92y-oTJYvLb6tejTmNqO6T_VInOzn0CMILTXk-uwgfVOsdK4EXoCtx_esKRfXEzmuZglGPqFxJADaA7DYHqPwd1rsmQkkmPf7OKMfQ3u0st4R_wfArn3ACDCT1KcE0Vs9D9O0sbzKHCD7A1LkCZqoTDl2lFCEpvV7gCOR4aoMKu2W0C2Naj7lBiFggrdXmEasWSdbBZnU5ADSbYzPCMKwikoLqFDNEQyayqUKaFeCzZwSOVJ9sOPfbQYg9u6d8g66tHSHf1NtUiSM1zIil_L3gXx3zrGCsgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a5zEz4FoIa_7PQ12EgF3bKAdoLMy5TouPJsL1fwPymPy01xailFzVEwlNhRe3Uecc1bBrrE657blquEwHXcxCtDwDcWAV-b7zO-vFWIRkmXW5rEDWa1lalZM3xcAhwcGl3gdGIMU4stRub_UuRFJ64yiXFRsMnaX2aBh_03_BjJRGRV_OQmxig2k3zMgi6R5YCZj6QjjV49QGTeYiLZNQctMyp06kWIBYqJRIYanRLzOR3DjoZ12iDjFoFwZmwZa62fwtbfXdZilX3frz5lHY0xQx28MFfcupDeGcppHv9TVbI7fLGOaPBrDVqzGcVcdnbvGE9vrTWi3ToaDF9o_gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NEEz8J2d_bH9uEz3O6XrTPslUvcm_ihBWASsYaT1BW03TICnAAuCbH4Dfc4dU4DTdrkvmy4SEYpMcgTWtpjsyYkoEMFk2j1ZMcxCetbzbdBleWcpsSNNNwpbcy_K8PILb7qcaC34glaAriVjVnDxf3uvtkmnuxZMI4xIXtHERVowrpk_r9Ri_jowl8Ll2fnOA8kujzE9L040TWbBQxZxOBBkhxd0kugfhTs7uPNsT5f8Cj-9HUuGoVsifk5XJTfWGMkv8t7Aa3WZ6s_2olDMiopfd4gQumz8mZLSvM-uzs20Z3vDng5g18H5AWm4NOnrPRY8o_GYP0IyVa4cmJQ8hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ldPYkXPGALyKArjhlgwk4046JCZDdNeV8D19IBYcM2jnmynKnwtAtXAxLzRjYAWdWoFH1PxlySPxgb8fo0uuHZOxMUxwzko2UieMN2XqKgLQs_mIg2GBeBh-vqqJsuC3_h_WO_NiinekaxP9IhzJM0lRru4SMFpuXmGk8JakQtPitkXYVYReLmJICbnJ4GPZhw-3Ot4Z8rtmjYtMbB-2HSrNptKb56NzQ8fONCoMocE28lSqQi2Db9b0JFi0WleyLnnYj1eBu0iDXIl6FH7okCsIp4rzjaWNG7e1WYNnZlO5RUreN4Nezu2ppW7KkIr1Kr1rKJAs5ZuuwAxiQT6GNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
وداع با شهدای بوشهری جزیرۀ لاوان
🔹
پیکر مطهر ۳ شهید دلاور جزیرۀ لاوان در حمله دو شب گذشتۀ ارتش تروریستی آمریکا در پارسیان تشییع و راهی استان بوشهر برای خاکسپاری شدند.
عکس: عباس کریمی
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/459901" target="_blank">📅 14:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459898">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TaQQcW85H4c5n9_ldYGOX4m48ayGMDiN1AnLqy4jC8t-9gYFE5kJo0DCDH79xEnKFZSJ4fYwjZ20Ad4ElvO1axh212EKPnI_ghIOyibalCRBKzx3jF7heEACqQmlZCK4mRcbQ6NdHg_8U5SaUlD__bmVZsFrgOXZx9RDoWkD1ooAXO5B3joiaqjjbyzM7ENTCVHx1ftTmUqvp40OhE_J1picCx2yzwWio30M_uNM7WW7XlUWjLU9rtD4NozW3zkY2TYUHKLDPM9XE4Zg0ytR6tcRpPuK2qnetV-OMU_AkKmD3ouYshODj_3Ea3oV4yjosFGwQzkPCxSFAqJiUa7J7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nwYrd0w1bqp_J1HZIi9axSZYKJo_suCcLWNNdemgTGOXkonqYMTy4hWNCKWu1q5xTJqzAmngYB0MkbUedynXpiIAscx3Ts37b03on7a0-iLvvHZRhG3FRKiYaV7xzIEbqt-iGEiADzQ4B5Yt1KceiWgIVH_HO0C3tj9OKR8g6_vrGpjGIGQA6QZ2E31GjB9HBM9jEjjZHorXk9GbnqRpeKht8Uo6fbzWCOhRmr7JDBfmRwJsVAzT3MTt7tMsfeSMQd0CKgg9noJ1_9rPxpd2q7m-r86zDh0JUdz0g9N1YjQpBul2fuyFD8aTd219M14axs5aRELyzcrCN-_HVc8mYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CmTmFIkr6qRszHk0G9DriioNEJptu47Pzau9eq_WEqY3Vb7w9vHIi3MeD3lx-LVhWGuJ73OoEGZvWPtBQzQcZmTpKmcHXOUNQLyEzw9LCjuktpt-Y2WLzMbjY1AQi2Og7ueia9SujA74LJx-EvcpheLUGLuJY-V81StnqHC7gblOV2ljocDVLZntojpuvki78vTHLRdr17--mZ5jCkp6wFR0dEcJdddTxrNOIV70QxzWS11z0pJcrci9Add_SShFwPL3_MEY4lRLbIZmbp6QCZsBfsvdCY8AMcWjJCpt1kdBx4yStE_Wg09Empu0OHn-v_nl4Db5twNWXSsS9Dfm2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
رئیس قوه‌قضائیه به هند رفت
🔹
اژه‌ای پیش از سفر به هند به‌منظور شرکت در اجلاس بریکس: این سفر در راستای امور مربوط به تجارت بین‌الملل انجام می‌شود.
🔹
ایران اسلامی و هند تمدن کهن و فرهنگ قدیمی دارند و می‌توانند در افول جهان یک‌صدا نقش موثر ایفا کنند.
🔹
نشست‌های…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/459898" target="_blank">📅 14:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459897">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8cKK54cFnIK-NzMJ8qq6U504QXvrBZDx0si-YzWl17Z-03fQyE-N4p5V77Um_tt5giyotxtbvgUJYp6-JKyAEURA5wQg7ftm2UamTKXsQzu8quWkJ-V4qQiSx_2_jKI2G2_1Ep_pyv2ZwECQWd6yT8wvYEei3vO638SNn7nocKA1w2ARL9rUxhH2J5KkflEID5rNXmkdoR-V_kC0bR18TIT_ofUpOqVvDX5FyeU-HjlQyUGolnkHl9GKxWz9pXvcrkRvWStF0T3C3OL039M7RT2SDKXDo-NWi19uNHRh0EF-QUb1Kb7v3ywY-ruHVFWIFJw428cT42Ym_P0TfnvAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
باشگاه استقلال با انتشار این تصویر مدعی شد آسیب گلوی آقاسی به‌دلیل درگیری با کنعانی‌زادگان در نیمۀ اول دربی رخ داده  @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/459897" target="_blank">📅 14:00 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459896">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_iXlcdVlXZF6KIERA-e35bbu51BRF1sRtDsiIKELcO2RzZ7oPD1frtTHtx9KAt1GzoY86X5lzCH0QY9nTfr2p_uM0jjbuOM1Rpvad0sgcmVC5RrjI_khhC9znxt9F5TH-TwicwGzCENyaZnQZcotMX425DjdPbefx4qi_O1Ee_4Mc4dYKOv0TLPAMAWGatQj7JkRlLJQQHU1C4hSD-RTFPcr1iif6mvibF4TJeXD2oNwkaWs136EoSyHDKHXUY9azRODRcpVJM52KsHWqx51YPdYoC-V5g7j7utFljENBtgH1352jhaTl2ximy-rbFPQB_IOkZE6vBQWeaHyt3Emw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضدحملۀ چین علیه تحریم‌های نفتی ایران
🔹
طبق آمار شینهوا، وزارت بازرگانی چین با صدور یک «دستور مسدودکننده» اعلام کرد تحریم‌های آمریکا علیه ۵ شرکت چینی نباید در این کشور به‌رسمیت شناخته، اجرا یا رعایت شود.
🔹
آمریکا این شرکت‌ها را به‌دلیل ادعای مشارکت در معاملات نفتی با ایران در فهرست تحریم‌های خود قرار داده و اقداماتی از جمله مسدودسازی دارایی‌ها و ممنوعیت انجام معاملات با آنها را اعمال کرده است.
🔹
وزارت بازرگانی چین اعلام کرد اقدامات آمریکا، فعالیت‌های عادی اقتصادی و تجاری شرکت‌های چینی با کشورهای ثالث را محدود می‌کند و آن را مصداق «اعمال فراسرزمینی» قوانین آمریکا دانست که به گفتۀ پکن با حقوق بین‌الملل و هنجارهای روابط بین‌الملل مغایرت دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/459896" target="_blank">📅 13:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459895">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">محدودیت موقتی در جادۀ کرج-چالوس تا ۲۰ شهریور
🔹
سازمان راهداری: در پی اجرای عملیات عمرانی در مسیر کرج-چالوس، تردد در محدودۀ تونل‌های شماره ۲ب و ۳ از ۷ تا ۲۰ شهریور با محدودیت‌هایی همراه خواهد بود.
🔹
محدودیت تردد در روزهای شنبه از ساعت ۱۲ تا ۱۵، یکشنبه، دوشنبه و سه‌شنبه از ساعت ۸ تا ۱۵ و چهارشنبه از ساعت ۸ تا ۱۲ اجرا خواهد شد.
🔹
روزهای پنجشنبه و جمعه، ایام تعطیلات رسمی و همچنین روزهای قبل و بعد از تعطیلات چندروزه مشمول این محدودیت نخواهند بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/459895" target="_blank">📅 13:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459885">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qcsl4oeWSzmqBUIE5fWz7gxp045yiUm7baULS2qG1Q-GW6TzO8ZCGWPWovtr2Jles_1k2f9wDXH0pzmQDx5wrM1ktyspF6c8jRU08iHCszrzp1RePk-KuoRfXTWwyTnMPkA2zN6Ua3g-cy3Ybh8McLlKk0oRFBlAL9qieZ0HbV5IDQg94qql0OO40Wgu018_zODb5BOrbjL0DZNX4NOX-faq-svnrdUnIqOIhlAVLNQ2slcaRCatnzVi3ErDW3tV8iFi1TMF_oV-OWocXi9l99Eb8OuCRb2gbS_k00ZEh2a6M0SDxNtPEewq6ozUdm0NENCdVK0Y45LMQNzWV4k9aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N-w--N874GeUAwJQRuEt_4_A-i4C2wUXSMQc4iGrGQ86agPwTV4kQKJTZql5TAsGx6d4-XAPPYjEuQgdFmwqW2whRLGUrXXSt48Wx7UURwJFCuMvxvTaBaYwG9V2XfIB7WigZviZZOXgeLChQv2hnez-BcJeCkoRWSv4KuKK4M9saWpIdunwf7-wFn4YzIE8f01jpS3Pxmc7ZLAEWxQb_U8wl2vqZeK-YfZpupzRPMO37SL-sULPU705s59ls36fQ17osGJBCUfJUD-s-ebJzF3iBIgzX0Wf_16v3BuL0Qcth03A-G9bDIwc39O8QOutmA9mt2ZWuO8ni1QHNWpfZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cYb8jvfR9nnzLcT2tR5CZATIzCpxT-ukhW8JS-OnmndpiLqsE17JTCE2fp8FSJlKX9Eu0TdnYlIRtOD6EAMInBE6ME1Kd09W_S7WdtMiHWFmCHoHOoqMIL_zxEB7YN7neOMIWQy28P193k0xuaIi16AK94APIJJbyOE0B6P7iRgaYpKrOskscDaioAd6LKQvMr5iMXgXdSi9-8h2YhOB40C-j5Q4_6ZJD5BYO8p_9d6QPHP--V5ByGAVopfknPO6KVZrcBjmAJBHIKTn52UiF_IYz76LyCfWhlL8b0D7P0JmkSPyz43YuEvIsJj2wnnlKfLvMsh0V9ORV2UsJuvNQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NZQjuRLhy3_snhMXttOiITzhmofauy483qQfiWM0RXwxpfBzwfulhC6KS-xPem6G2Ldhrm1qncSLc2_ynF6Kt0rBQypW89pazydQqd6TjXdeLlTiZiKgistHhhFpT06GxX-P68IlmVgeZag3Y0bj22aK6v-GXFJqXEQHRmLp8HdhP23IY7S7gYR4pbj5uu2bDN7-gqdq09WNl88M4d_1qoYSZSeJ30qyAxgGGcdFMHGSBxZllL_WgBxD59t9gPPAM_Fi0M0R0qN-yFsMLxYlC_11dIPlnUHwUcYjeXKlg5_EDS8Bps3OpRoqYuJPOAlkK4jNagGEbHPaota9yjrtPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PkPGwXwPfWFs2-H6NuwKyqza3B_-QZMiDmdBpdMrALtR2Esw4C3ZYV66Ob3aTgsECKb6j7Fc7EsT55owaxOnDMpxCd0zs0ktwhtPVQTIXJpfSbqE35BSnmDufRtpB-E7OGU4czgldI9F82KQDS_n0G0M_0k3RCorKNIaeCcVT0iel7qeipm47ZaJFohyzj-uh6zZRVeGcDeEs7WuNyJwogYPJGBKITJ_6oYteNBJ4XVILzQKNSC9qKepJqj1cmFnO0yPAPFUyhq2NcV6gU1bTVch-KKqByFyAuah0lsCNKhu_KG6MtJe9mFo-fffnmz1H3MB8AfEkj7GdRTnbT-leg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TNVOv7jyUqRJa99ZL0eh3iCRd-rljsnIRyP7q0dCWbDbrUOGu6BVKA5Xuh8kWhWmatRkfKDlLUAHY2rpZtblOLCvc3RLvoR9pydTlrle0WVDclCOrNDl57a9YKZjB6wX2GLEaaF2GGxuAW8IftwXBQvQOL65jMdlLQIM1FnR7mPsXEobq1oUrWfN81aKuChMii1ZiafABlrlcG0f4h-8y3fzxoBIRbk-uWqCD3IDgRICLvKgB7nMJFsedu1go3qIN_XSvfG7jNecsVoasDWp2EPak4Xn1RFC8xWCz8WtII1_NMY8r7BrRck_J4njWM99riwV4lscVRiTicpHqYj5bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SnOImwpR_IycHWDIlQL_WIn8XwEv0rIRvo1vdHGhuO57rZrLsgUwFR1BzrZ_u-D9Tr6AQlAEE4uhSP4Mr9cAp3qF_NV0Yv9Vdg7_Xs0YSnKl2mt8_2A6LSa6NnSspM-AHSj6Z7V6IejqZGqrzQivfS9L7usCpwlO3L1o1LR-T-s1d3w-fbQHxkzKerGVfBdVRo2Sl0IVSB30ffJjPBTRskWsVvHjiILXpfAd2HefI4NxZEMjldVe6vkfRWEohqTRT1Q6RhRUrG2RF-592qgSUaqhVnhpBPRSPytXZ7XxCyvvd75RSPoQIZ7MQxXnsqK3NzUmBy6OEGrndhBTIX8tJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OljGDLuRns517yTgHS_Lf5ocIfSNBYsQtFi9_mDXUowQ-adKZhwxtMvejnrQqoTgIRlNU0gXWxn88JdDJLa_MhVINm49XJBSQfYTukPQxqROzfQnHDVfrNkmFwsLPFy0RMiwmh5y1ByZTwuq-ZiOMTTePuk8aMxnZfV8l5Glau1DCLob9UcyhUVGHbHlkSrSFZ_9u85NQ3zHBl6-dx4MNFI5gZgsEBYQL6uPp1NDgYx76Kvjv20hBK9aPYEDw1J6wzWCgrXNnxrIaM5uk6tX5nckB_qbYpgTRQnSAQLj_Q29FTYKf4LgrBiiO49pXhh5tc9nskf8yT_w2RfsZgR6Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fHAX-XlgF9jq7rOHC1_c4XnQblVMGfhz6psNWf_ZyIk2vvNwJW5cep9UgzxIJBjaApTXEhQaeWr_ksaLwj0qgQuTVxZs0qxo3uUzaEi_BjNpTug2WgOmrRzmhGlWkCcuDC4nLQoz2MvkdfkDoBg0vi-eS3OnELU7LMqBl639gIP63lXEaldrAR0J-JwBYTsgprA5jObjcbHGNnFzbFqRbcwXcLZ-dH3YZ0lf-cq_SpzkmTFPiLjJL1Wc9zHLa1p4xntPsVelERhDd47fgzawD0Qg0sYHU-sugfkNOCM432YQCpRnLe0VlxUW6nVK68yLx_jRL30B8N43sn93T9DJQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KYK5Qvdsbg3lBJ9WJkhxLTfxFJvVHvt-mhW-F-50oXOgyELL_cPAUFo35433Tz4oDCEqCqZv5o0qih_UlAu8UOUWYzrum0qXm8Fekks_T-ur9aErtT4gvnqJK1IFy4gUfQ6XDQ1Ui7ii7vCbGlva8ypd42Zdz6kMUcmLI76g9hQW6oj6OJdqJsQNhuB0xLHNoY8Hy7i0NKFMmtNcdidXrdsoS1NY2kOIWoJcl5q0eOYbyqx6OA1Cc5nU1TYZ5SrTMMBJCWPSY6lT2f7yaqveeIsDvwgMeJmQtFfI5c84j7Ih8hLsT2xqz8DH-exEId3SqPiMwatloVSGvi6ComAdsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
بازدید مدیرعامل بانک صادرات ایران از نمایشگاه الکامپ/ رونمایی از محصولات نوآورانه توسط افشین خانی
🔹
مدیرعامل بانک صادرات ایران با حضور در ۳۸ امین نمایشگاه بین‌المللی الکامپ به بررسی آخرین دستاوردهای حوزه تجارت الکترونیک و فناوری‌های هوشمند پرداخت و از ۲ محصول نوآورانه این بانک نیز رونمایی کرد.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#الکامپ
#اخبار_سایت
#بانکداری_هوشمند
#بانک_صادرات
#بانک_صادرات_ایران</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/459885" target="_blank">📅 13:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459884">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lk4LbnzkIm_EIIU8AOiDEvL3txOsHJhTWLZXymP5CmQ0gM5yX2wX7arHFodx0QHfs_pXYXUefEhE9UVnr3FsLSLdBznmPIM6iiwR3XC9033y6CVmUOfev8NeMe2WObAimI11wHBI2WlGW9z3QNwriz_16iRyAn3Ha_6IBuU1YG4drJH6s1nqNhZWE3fyYqSNobQt1rrnZ9plM4wlHvp1wmVP9uIsFBAYUnlyeDpjKN0oY_6yP_6cwOpyEmZqWaaHzyWz2-T0uPqXCgz8fUSvrAPahHl--O74x8Rm4hbaQFstb3CeRBNr9x2irSHcG1Ubi4DyFhkgMGa3ygwgEQuJeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
یکشنبه‌ها در پارک آبی اُپارک، بازی‌های گروهی منتظر شماست!
در سانس بانوان، در کنار آب‌بازی و تفریحات اُپارک، در بازی‌های گروهی شرکت کنید، با دوستانتان رقابت کنید و شانس برنده شدن هدیه‌های ویژه را داشته باشید.
🎁
🏆
🎟
برای خرید بلیت به سایت اُپارک مراجعه کنید</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/459884" target="_blank">📅 13:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459883">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAZwcXza53Hzz-VkrQuMQXAy6BlrpdU6UhkOccqCLZUPPiBQs7xOypj-IUkym56eIJBpyNSINelq7Ho-MP8phWjv2lObFnsxGNWr5CmqLmte5DhLzZehJXArh7g-dNERsDcCdk-Bm07xn4IGGAABun3X-psvpvZeWJpH1xvf8cPu0o7esjhJgTWVMa9duuimoPfFizZJmBKeFuehwz4JxW7UybYgkNfMsXs9wd0jq-dt5pW30JlkdWXcTCfiJysyw7sfByLkRHvANWFdv8N_9Ax4zXEI5n8IUqwZxPzAbR6bNNajS18qzFCEkpmr9RZQGUj8sWhBvV7X9YhL5X-0zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داروی ایرانی درمان سنگ کلیۀ کودکان رونمایی شد
🔹
داروی ایرانی درمان سنگ کلیۀ کودکان با نام «سیترولیزکا» در بیمارستان شهید لبافی‌نژاد دانشگاه علوم پزشکی شهید بهشتی رونمایی شد.
🔹
رئیس پژوهشکدۀ کلیه و مجاری ادراری دانشگاه علوم پزشکی شهید بهشتی: این دارو پیش از این به‌صورت «دست‌ساز» در داروخانه‌ها ارائه می‌شد. حمل‌ونقل دارو دشوار بود، زیرا تغییر رنگ می‌داد و می‌بایست در محیط‌های خاصی نگهداری می‌شد.
🔹
داروی جدید ترکیبی از «سیتریک اسید» و «سیترات پتاسیم» است که محیط ادرار را در کودکان تغییر می‌دهد؛ این تغییر محیطی باعث می‌شود کریستال‌هایی که قصد تشکیل سنگ را دارند، نتوانند به یکدیگر بچسبند و بزرگ شوند، در نتیجه سنگ تشکیل نمی‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/459883" target="_blank">📅 13:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459881">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e52a16bbd.mp4?token=Z7j5uSwpS5w-7hRAdmITjfYnd2fdOjrPyie62_sH5d1HFxVp6IXTPeMJYMpiCxI9Q9vEbqOwxwidHva66jteF5DDvVvLqpOZUf69qwNdp2CNT9sJQXz2me6-4xZSHZ33U7BGuO_NK6zh3c2BQmXEzn0z2t4w7FM4iOg8gCIr85XhhZDTTtmWea9pk_FGJASg_lxD7gcX9v5s3lwi0gK--zLpIckRfSE-CxaMvLW_OMWdBpXEySjIIybnGR0P5qBY__ue8PgetcK70L2v-KFwP51OnDWyeRuHMwIy25m8NgUULnJrTrab4MWi8WVrNnMQjBHKucMWLOgl5pMh5PjX8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e52a16bbd.mp4?token=Z7j5uSwpS5w-7hRAdmITjfYnd2fdOjrPyie62_sH5d1HFxVp6IXTPeMJYMpiCxI9Q9vEbqOwxwidHva66jteF5DDvVvLqpOZUf69qwNdp2CNT9sJQXz2me6-4xZSHZ33U7BGuO_NK6zh3c2BQmXEzn0z2t4w7FM4iOg8gCIr85XhhZDTTtmWea9pk_FGJASg_lxD7gcX9v5s3lwi0gK--zLpIckRfSE-CxaMvLW_OMWdBpXEySjIIybnGR0P5qBY__ue8PgetcK70L2v-KFwP51OnDWyeRuHMwIy25m8NgUULnJrTrab4MWi8WVrNnMQjBHKucMWLOgl5pMh5PjX8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملۀ شهپادی اوکراین به «سوچی» روسیه
🔹
درحالی که هشدارها دربارۀ احتمال قطع دسترسی اوکراین به دریای سیاه در نتیجۀ جنگ ادامه دارد، بندر سوچی روسیه هدف حمله قرار گرفت.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/459881" target="_blank">📅 12:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459880">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcRdtErGikk7KnoH7XDyXvvIcTI53738bJE9HIfEwgVm160PeKdL4Kqfh92vNmz5wGgcjGfJIHOUIdI5pOSSoG1uNUTd5pnid4z4uOHbbFe3FOtJLpaZsELEfFH8Vf6rUwmpEYcRDpAbItWVALd6HA5Z0C9JmRQtcCpCoeviHyGDVaNCQsANDmJdfVIs9DUJtnv5uvXdLqrNjh9MpCoxfhdLsxsz6Wi9oqY3Te-wHzQUSbcNIIPCjd76-EuYjZmYCv6f0uXMbmORUQyyxUNHW9HAGcqyMwEaO_rFB1don97o1KapMsji7uEDqFKiX8RJhRdQhlLyhBlvs7PCpJehOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
سلاحی دقیق که آمریکا با آن به عروسی در سیریک حمله کرد
🔹
بررسی بقایای به‌جامانده از حملۀ دیشب ارتش آمریکا به یک جشن عقد زوج ایرانی در کوهستک سیریک، نشانه‌هایی از به‌کارگیری موشک کروز پیشرفتۀ SLAM-ER را در خود دارد.
🔹
قطعات مربوط به بخش‌های الکترونیکی، حرارتی…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/459880" target="_blank">📅 12:46 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

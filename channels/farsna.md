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
<img src="https://cdn4.telesco.pe/file/jHvm9JOuobx8kcvHRrhlbzP0AbKrq46aRIinnbffTOa_mwjtlCIwGbIT6NfHA1qWRQGbEws7swxngNQATAVpdkzEaC2-oEf9Xzv3ppXZdjhNCF7cESbnN4v-7SLVHyEOQVFfZBR6yHvFK4DPPME2M5RMWRHC6wdVdnz9PPJsQdGRGpaFHnfFjsKoW5i3V-cK3xjnu8jSdHAf8et0F8oImaguUJt9ahCFfOACEYKtuEEdZc2cYY9X5naQNbfnm_TeFZELkeL8te6OzyfL5-Zy1OQFiySsP9k5usj--BgrVPMS4x4ECd2vPsM0fX5JUlg-3ISmStXpGTccYClFS1ZUvA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-23 21:07:56</div>
<hr>

<div class="tg-post" id="msg-449972">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ادارات هرمزگان سه‌شنبه و چهارشنبه تعطیل شد
🔹
استانداری هرمزگان از تعطیلی تمامی دستگاه‌های اجرایی، بانک‌ها و مراکز آموزشی این استان در روز سه‌شنبه ۲۳ و چهارشنبه ۲۴ تیرماه به‌علت مدیریت انرژی و افزایش دمای هوا خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/449972" target="_blank">📅 21:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449971">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d977dee9b.mp4?token=VtQQXw_E2xc0EZ_Qlwau8HUSJtuMX7jzHQTdl9FuoH_zWhOyRmpqBY4UGVp5mcL2Kd9pBcriD4pH540xC9yr58bTOl7RHRBofpSpXkumLHRI6YLPau3eTT6pWx5AnQsyDOa7J0xrJFPuq5vXevfW0PTSBmL1cefoyr7-C5z28I-aMOOaVBCO-gjaMqtBVCevjeIDhSixTnuH-Ixbx3P1pQPOLMnYhdl5jWCt3s3jtawTd2y63pFm9x3-c3zKcfDqX8FOb2ySlKYfbX5TKTrcRnsDy_6Oj7nTJivoSaszQBT7gbqv88hGZ2rXSmZnx1Ls680gtQpYjgI5v6N1-2yFJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d977dee9b.mp4?token=VtQQXw_E2xc0EZ_Qlwau8HUSJtuMX7jzHQTdl9FuoH_zWhOyRmpqBY4UGVp5mcL2Kd9pBcriD4pH540xC9yr58bTOl7RHRBofpSpXkumLHRI6YLPau3eTT6pWx5AnQsyDOa7J0xrJFPuq5vXevfW0PTSBmL1cefoyr7-C5z28I-aMOOaVBCO-gjaMqtBVCevjeIDhSixTnuH-Ixbx3P1pQPOLMnYhdl5jWCt3s3jtawTd2y63pFm9x3-c3zKcfDqX8FOb2ySlKYfbX5TKTrcRnsDy_6Oj7nTJivoSaszQBT7gbqv88hGZ2rXSmZnx1Ls680gtQpYjgI5v6N1-2yFJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون اول رئیس‌جمهور: مهم‌ترین اولویت دولت در شرایط فعلی توجه جدی‌تر به منویات رهبر انقلاب و امام شهید است
🔹
بدعهدی آمریکا برای ما قابل پیش‌بینی بود.
@Farsna</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/farsna/449971" target="_blank">📅 21:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449970">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3266e0d442.mp4?token=XA3z7F5UsHgTqvonm8hCRNkQiqja7rP16tnvY5IyBhReVqUtSZWT7s76xtBG498SgaVPU31OB5BNH5dRk5BTDYpsq-FU5l3t2oi9XiEosJlXpSn9ebAcY9li626ZwcMf7NF7UqT5lT_dWJ9NZ7t_jsqDvCqN4aJVx32fvyg07ChUAHwlJkLn8O7jixvw8UvqWb9W25nDPULmUal3N8_fnOFhbokRu2gsLDcn-n84GeY5IZIMOWUpJlyENlTNkozv2-fDffGCOYHHZSTnv5uWxj2SXYEZOC0EU0RmtBMRltKg72TQOHc-W2cP43uVK2-Jq4apiDIFukyqe5XrnSsCEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3266e0d442.mp4?token=XA3z7F5UsHgTqvonm8hCRNkQiqja7rP16tnvY5IyBhReVqUtSZWT7s76xtBG498SgaVPU31OB5BNH5dRk5BTDYpsq-FU5l3t2oi9XiEosJlXpSn9ebAcY9li626ZwcMf7NF7UqT5lT_dWJ9NZ7t_jsqDvCqN4aJVx32fvyg07ChUAHwlJkLn8O7jixvw8UvqWb9W25nDPULmUal3N8_fnOFhbokRu2gsLDcn-n84GeY5IZIMOWUpJlyENlTNkozv2-fDffGCOYHHZSTnv5uWxj2SXYEZOC0EU0RmtBMRltKg72TQOHc-W2cP43uVK2-Jq4apiDIFukyqe5XrnSsCEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نفت: فروش نفت در چارچوب‌های قبلی ادامه دارد
@Farsna</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/farsna/449970" target="_blank">📅 21:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449969">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/346a1329e1.mp4?token=Q7NyXiqGR-dcCjNPZV_4wZKBrfq9a3WKUJCHSVYWpFYEkQHbqyQHIlMwuOpDX_3oX-eIvgGw3bW4K5VoC9EOJ41igCb7MfunuRwb_2WY8RZ_sPPJdRmkxszBybajRf-mo8laMBZxk4h8IFBv43F0DFcsXriPpdX1BLP8ZanxWrwwBaTnxWOWdrEKiCSf5Wr76wFQEUl8MdJMsvOtn2yXX0eZ8C1keJKQs3NA9wKOIzcGvkc0wXO0qOb4Xur_QUPBWEplTtG_aNsHoHUTasS1rD6yUqFLG6e5aALc4Twa1B0fHwoZ3VclQras9WsaP_IWKIOh3aqMPLLS_qUOTmhv5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/346a1329e1.mp4?token=Q7NyXiqGR-dcCjNPZV_4wZKBrfq9a3WKUJCHSVYWpFYEkQHbqyQHIlMwuOpDX_3oX-eIvgGw3bW4K5VoC9EOJ41igCb7MfunuRwb_2WY8RZ_sPPJdRmkxszBybajRf-mo8laMBZxk4h8IFBv43F0DFcsXriPpdX1BLP8ZanxWrwwBaTnxWOWdrEKiCSf5Wr76wFQEUl8MdJMsvOtn2yXX0eZ8C1keJKQs3NA9wKOIzcGvkc0wXO0qOb4Xur_QUPBWEplTtG_aNsHoHUTasS1rD6yUqFLG6e5aALc4Twa1B0fHwoZ3VclQras9WsaP_IWKIOh3aqMPLLS_qUOTmhv5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
منابع عربی از شنیده‌شدن صدای چند انفجار در بحرین خبر می‌دهند؛ گفته می‌شود این انفجارات در اثر شلیک موشک‌ها به‌سوی پایگاه‌های آمریکایی است.  @Farsna</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/farsna/449969" target="_blank">📅 20:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449968">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/542073129e.mp4?token=Hr53gQ--sUQaSClyQnPeNaNKQPbLfP1Qz8XkOS10tJ3GOmpYLhq4K0Q_xO4e0KyFKbqttIxF6iQt_AuNAeOk18OVwccronIJ4PyN2cw12rXhxKlMRmV1sVR1JxzVgFt-ldSXMieFcaQJG0pB-bnCheZCiOJN9fO0SXh3GT78IcbG3ZERHpAsCY68g4P7a029ygZGqMDDkd7J3JHBvnWZgdMRzyRHxCCe37P0oErVdiUv1zbHZYPbB1uafO5YNNXziHOLjBdQ7PhoVdZIU_XXM_E7NyegDPVRUuB3owadIDGysQOr6mb3pHLMFnKLu4dZqDzTCI2RL5oGELz7iQmGsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/542073129e.mp4?token=Hr53gQ--sUQaSClyQnPeNaNKQPbLfP1Qz8XkOS10tJ3GOmpYLhq4K0Q_xO4e0KyFKbqttIxF6iQt_AuNAeOk18OVwccronIJ4PyN2cw12rXhxKlMRmV1sVR1JxzVgFt-ldSXMieFcaQJG0pB-bnCheZCiOJN9fO0SXh3GT78IcbG3ZERHpAsCY68g4P7a029ygZGqMDDkd7J3JHBvnWZgdMRzyRHxCCe37P0oErVdiUv1zbHZYPbB1uafO5YNNXziHOLjBdQ7PhoVdZIU_XXM_E7NyegDPVRUuB3owadIDGysQOr6mb3pHLMFnKLu4dZqDzTCI2RL5oGELz7iQmGsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خضاب، کارشناس صداوسیما: آقای خاتمی گفته توافق نباید مخدوش شود؛ حرف ما هم همین است اما کسی که این توافق را مخدوش کرده آمریکاست.
@Farsna</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/449968" target="_blank">📅 20:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449967">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‌
🔴
دوباره صدای انفجارها در کویت بلند شد
🔹
منابع عربی اعلام کردند برای چندمین‌بار طی ساعات گذشته مواضع نظامیان آمریکایی در کویت آماج حملات موشکی و پهپادی قرار گرفته است و صدای انفجارها به گوش می‌رسد. @Farsna</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/farsna/449967" target="_blank">📅 20:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449966">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03d1312506.mp4?token=GOR225kx19kYDfzLQ_jcwmx-ac3MmCohnVL6hqIm1XKDTWegQWpR2Z0gvi3jGKKEp4r73L253qrbuI68Vj2GZoHMyy5GZ5i_m7XOYsljfDUmnpAl45L2W8y24Gz6teuQXlW-ll4HuOK_m8v2lZrfg9KAHAiyECyloKYno2b3sdLkC4lAlTi4c0Vd1nPHktD6Q0f4jVl6O9OSlAa62t_ZHvDlNEbVaCxXZPFjDBWkm_RFvlr-NMh5uqCG9jOQoqoTKF3CeTchExh_-JZBvgLK5cPAZQJGTQHSOncJx1WAr7QbrM7cJMrleDqdaQTX1SIGGWijugaa13fV0daFlBg3cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03d1312506.mp4?token=GOR225kx19kYDfzLQ_jcwmx-ac3MmCohnVL6hqIm1XKDTWegQWpR2Z0gvi3jGKKEp4r73L253qrbuI68Vj2GZoHMyy5GZ5i_m7XOYsljfDUmnpAl45L2W8y24Gz6teuQXlW-ll4HuOK_m8v2lZrfg9KAHAiyECyloKYno2b3sdLkC4lAlTi4c0Vd1nPHktD6Q0f4jVl6O9OSlAa62t_ZHvDlNEbVaCxXZPFjDBWkm_RFvlr-NMh5uqCG9jOQoqoTKF3CeTchExh_-JZBvgLK5cPAZQJGTQHSOncJx1WAr7QbrM7cJMrleDqdaQTX1SIGGWijugaa13fV0daFlBg3cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارتش: تنگۀ هرمز وقتی باز می‌شود که در آن ترتیبات ایرانی اعمال شود
🔹
مطمئن باشید دربارۀ تنگۀ هرمز حتی به اندازۀ سر سوزنی کوتاه نخواهیم آمد.
@Farsna</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/farsna/449966" target="_blank">📅 20:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449965">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15c1d559fb.mp4?token=AlzwUC6zEgzm6LnwkRfHHLcOyHbIfoBM9-FWpnfvCSefufPbMk24C1ATeNyksp1W3nTQaj_oNO0ulsbOMFrie6LyjRBmuD9bbV4Wem58GetuXZCyT2d90h8hLJS_XOu0hcDONyJ7-b8SVj9hkFxznRY0zEcQjCpH5f0emAmdz-PXyVDiui9g_yGnJtjFYvKQSIQrOTSv-ol9u_qimeHHa4NFxiJ4xZC-ajxw-_eCe0ZujIbsnZHa7YxEVqIZJGp6dFZejVJkxxDJ3IqIA4vWnMNLXldlGS_1NjmEXN-flgSsP_PWX68GCjrFC_nkQ2x25kdtklUJo9BDQPOCqu_oPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15c1d559fb.mp4?token=AlzwUC6zEgzm6LnwkRfHHLcOyHbIfoBM9-FWpnfvCSefufPbMk24C1ATeNyksp1W3nTQaj_oNO0ulsbOMFrie6LyjRBmuD9bbV4Wem58GetuXZCyT2d90h8hLJS_XOu0hcDONyJ7-b8SVj9hkFxznRY0zEcQjCpH5f0emAmdz-PXyVDiui9g_yGnJtjFYvKQSIQrOTSv-ol9u_qimeHHa4NFxiJ4xZC-ajxw-_eCe0ZujIbsnZHa7YxEVqIZJGp6dFZejVJkxxDJ3IqIA4vWnMNLXldlGS_1NjmEXN-flgSsP_PWX68GCjrFC_nkQ2x25kdtklUJo9BDQPOCqu_oPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: لفاظی‌های ترامپ را در عمل جواب می‌دهیم و از وجب‌به‌وجب خاکمان دفاع خواهیم کرد
🔹
بی‌ادبی‌های ترامپ شایستۀ خود آمریکایی‌هاست.
@Farsna</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/449965" target="_blank">📅 20:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449964">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucGyMrBLiM6ol1ssPPXvD_woms0STAPoOkDYqwlSk33mZES2dJq8E6icEQuUaGuCfGdZKN6_HmgQizuxu2DbcyJOVPzrzto-N_UxI63ixH5AcJDlXoZyY1yzsM0SxFWk1bCxUl5QhmQeQuQsVlHWXoHsi9lL4liJRQEntUMYivFKH5zhResomeYEyEULsL_O0y2EqnGsxM1TRfpe5A_9GyFPndSRKkowkFwF0Iub3pFMlphApv_MkXPY0TOcl7AQR363pvCROE2xeuRM7vh67x6B_USMKTtOPyv-WLeqJCd5aTEkTJxhJmcFpUjJjd-SJ-FGCyUKGK_QkH3Yhio3qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرقت آب از سهم دریاچهٔ ارومیه
🔹
دریاچهٔ ارومیه امسال بهترین وضعیت آبی ۶ سال اخیر را تجربه می‌کند، اما برداشت‌های غیرمجاز از آب رهاسازی‌شده سدها، روند احیای این پهنه آبی را تهدید می‌کند.
🔹
با وجود اینکه هیچ تخصیصی از سامانهٔ سد کانی‌سیب و تونل زاب برای بخش کشاورزی صادر نشده، برخی کشاورزان به‌صورت غیرمجاز از این آب برداشت می‌کنند.
🔹
رهاسازی آب از سدها یکی از مهم‌ترین ابزارهای احیای دریاچهٔ ارومیه است. این آب باید بدون مانع و برداشت اضافی از مسیر رودخانه‌ها عبور کرده و به‌ بستر دریاچه برسد.
🔹
کارشناسان منابع آب هشدار می‌دهند مجموع برداشت‌های غیرمجاز، با وجود محدود بودن سهم هر بهره‌بردار، می‌تواند حقابه ورودی به دریاچهٔ ارومیه را به‌ویژه در شرایط خشکسالی و تغییرات اقلیمی، به‌طور قابل توجهی کاهش دهد.
عکس: حامد حق‌دوست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/farsna/449964" target="_blank">📅 20:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449963">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
اعلام آمادگی مقاومت عراق برای مشارکت فوری در حمایت از ایران
🔹
مسئول امنیتی حزب‌الله عراق: در صورت آغاز جنگ علیه ایران، گروه‌های مقاومت به‌صورت فوری و قاطع در حمایت از ایران وارد میدان خواهند شد.
🔹
از اقدامات یمن برای شکستن محاصرۀ اعمال‌شده از سوی عربستان حمایت می‌کنیم. یا باید همه امنیت داشته باشند یا همه از آن محروم خواهند شد.
🔹
سرکوب پیروان اهل‌بیت(ع) در کشورهای حوزه خلیج فارس و باندهای وابسته به الجولانی بی‌پاسخ نخواهد ماند. این حساب باز است و اشرار بی‌شک تاوان آن را خواهند داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farsna/449963" target="_blank">📅 20:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449962">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‌
🔴
آژیرهای هشدار بار دیگر در کویت به صدا درآمد @Farsna</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/449962" target="_blank">📅 20:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449961">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نخست‌وزیر عراق: ائتلاف آمریکایی ۳ ماه دیگر کاملا از عراق خارج می‌شود
🔹
علی الزیدی در دیدار با برخی سفرای کشورهای اتحادیۀ اروپا: نیروهای ائتلاف موسوم به ضد داعش به رهبری آمریکا تا پایان سپتامبر آینده (هشتم مهرماه)  به صورت کامل از عراق خارج خواهند شد.  @Farsna…</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/449961" target="_blank">📅 20:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449960">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">آسانی به‌راحتی فسخ کرد
🗣
یاسر آسانی قراردادش با استقلال را به طور یک‌طرفه فسخ کرد.
🗣
طبق پیگیری‌های خبرنگار فارس، وکیل ستاره آلبانیایی ساعتی قبل با ارسال نامه‌ای به باشگاه استقلال به دلیل آنچه عدم پرداخت بدهی معوق و شرایط منطقه خوانده، قرارداد را فسخ کرده.
🗣
این در حالی است که روز گذشته باشگاه استقلال اعلام کرده بود که آسانی به دلیل دیدار با خانواده‌اش ایران را ترک کرده است.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/449960" target="_blank">📅 20:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449959">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82af162478.mp4?token=tg9aQGNzJOx5a5WVvFZKFa0U3W4q4Mr51koHNugZpi29Hgz3Gd-OgSnfxq9P4_CJmOl7mGBdqEphRGfqFsS_PWZhZU5JZYND-F9i3lcrL13seHV4H_Wfm2ypiZERoc313auvnt5aEFOtA_4IOxfYbEydCRTohF3m0JFMwHxSukPdE9R9DZy1WJ1PWd9LD694_dVJZJiuuYpqgmXaachahOVCyrat6UC0zZqAVH2R86UshsJn5lUVuiAmhyORDpgDIjXeaA5gmV6TJCiILOxFCox3T0urOmKvEVi2zIWjSNOxGGzKvj6_KRNCIrOBarp_7Mx4I9tsNEJvmqkvpgeu5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82af162478.mp4?token=tg9aQGNzJOx5a5WVvFZKFa0U3W4q4Mr51koHNugZpi29Hgz3Gd-OgSnfxq9P4_CJmOl7mGBdqEphRGfqFsS_PWZhZU5JZYND-F9i3lcrL13seHV4H_Wfm2ypiZERoc313auvnt5aEFOtA_4IOxfYbEydCRTohF3m0JFMwHxSukPdE9R9DZy1WJ1PWd9LD694_dVJZJiuuYpqgmXaachahOVCyrat6UC0zZqAVH2R86UshsJn5lUVuiAmhyORDpgDIjXeaA5gmV6TJCiILOxFCox3T0urOmKvEVi2zIWjSNOxGGzKvj6_KRNCIrOBarp_7Mx4I9tsNEJvmqkvpgeu5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران سرنشینان یک برخورد دریایی در تنگه هرمز را نجات داد
🔹
بامداد امروز برخورد کشتی فله‌بر با یک شناور دیگر منجر به آب‌گرفتگی و دستور تخلیهٔ اضطراری یکی از کشتی‌ها شد که تمام ۲۳ خدمهٔ این کشتی با اقدام موفقیت‌آمیز ایران نجات یافتند و به قشم منتقل شدند. @Farsna…</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/449959" target="_blank">📅 20:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449958">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMR-vStCJB6NOzWgXjKQYnf1NxB9KPLB0fTgv8YD3kUMoECzTqM6cHInSBgtLr84UDmwhlLwWhrBcor7wKmqJ_7acI9pOn8Ee0gOP_Lv5RBYs17mQ_AfDzGlQxExgD2PXsoIKJ4lfgfAw5KdUQtirarZXY24L40tWaSXnSKv1CLaYo-TdrMt1mhx3vfCOczR2tQpqpaNSqtNrv-TPUfxnZSJ44Rc4uqncC6ug96zfP45GxjgCLgKwtYkwwhIA79xOIZsPAWFX2anqURcSAlWpdUD8dJ5SdDberouIBLI8kSf1TI6AB7RyThrw8nVkVi4ChIT371mUBX8yI16GWkpqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفت‌وگوهای ایران و عمان برای ترتیبات بلندمدت در تنگهٔ هرمز
🔹
روزنامه فرانسوی لوموند به‌نقل از وزیر خارجه عمان نوشت گفت‌وگوهای پیچیده‌ای برای دستیابی به ترتیبات بلندمدت با هدف تضمین آزادی کشتیرانی در تنگهٔ هرمز در جریان است.
🔹
این درحالی است که آمریکا برخلاف مفاد تفاهم اسلام‌آباد، با فشار بر عمان مسیر عبور کشتی‌ها در کرانه جنوبی تنگه را ایجاد کرد که در‌پی آن، ایران ۳ روز پیش تنگه را بست و بر کنترل مشترک آن با عمان تأکید کرد..
🔹
وزیر خارجهٔ عمان تأکید کرد این کشور مسئولیت ویژه‌ای بر عهده دارد تا همراه با ایران و جامعه بین‌المللی، برای دستیابی به سازوکارهایی عملی، پایدار و مبتنی بر حقوق بین‌الملل، در راستای تضمین آزادی کشتیرانی در تنگهٔ هرمز همکاری کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/449958" target="_blank">📅 20:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449957">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چندین انفجار در کیش
🔹
دقایقی پیش صدای چندین انفجار در جزیره کیش به گوش رسید.
🔹
طبق بررسی‌ها این حملات به حوالی اسکله مسافری این جزیره صورت گرفته است.  @Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/449957" target="_blank">📅 20:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449956">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bICzEXJYlY6GhAK2tNmx340frjLKGSpjb13Qw9kdmTearw8gX4ZLQaUrBuT3Cw2XlhDZV7khH5oK5ka2g-TDXMTPToSUg6_6gYE3s3HthwafQ962Y3HXojLor62HB5P0984WqED6B8HzplcVGaltsCugPeXr-f_5RKxm-Df-ygXVLgIyyJdiWyjPK0fzqLroQ0HvVVGbLaeO_4G73--WWwITu8pasb1m4oArTO9iankQt_j0I61MzH16EMx1q0qvEDea8ik2TC7I7sTqzdOiC5ntVSniDdSX_dl_1OqFX4I7gN_AcALF3VOK9vh26bRJOhR3xNLgge9bYQ5wmNwz3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن یک پهپاد شناسایی متعلق به عربستان را سرنگون کرد
🔹
سخنگوی نیروهای مسلح یمن: موفق شدیم پهپاد شناسایی (Wing Loong 2)  را که در حال انجام مأموریت در آسمان استان «البیضا» بود را سرنگون کنیم.
🔹
نیروهای مسلح یمن برای مقابله با نقض حریم هوایی و حاکمیت کشورمان در کمین است و در برابر هیچ تجاوزی، دست بسته نخواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/449956" target="_blank">📅 19:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449955">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jl5eu82MkQfg1OqThHlP7d5raQnBq7_gt7EF8xY-T3ZFkm4BqwGSVwklubnxctjmmMR_z95xt_MroCRDiHlYZcyMzakYsucLOghS8woLR00z39Z7OA7bRsHduqpQ80ZFGwK8ScXJgSHZfWICW_rwzxUHrO04g1regtyK8U_Py_Odjt_FUyzSsmSGA69y1W-stuMGbsa6nptms2oAg38n5dUl1hhM-KQARTYEdCFM2SoXhnKgEzqN91n0ZcEHvn0caWI9CgrPNjwevh0SRhg4kPzSB3qwz_lDA5f8TahXIteZoFTGATnokX_8yvrPrptJFiRnAzW0OD5T9_cUyEJogw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلوگاهی که بازار نفت را می‌لرزاند
🔹
مؤسسه تحقیقاتی «اچ‌اف‌آر» اعلام کرده است که اگر دامنه درگیری‌ها از تنگه هرمز به بندر فجیره کشیده شود، امارات ناچار خواهد شد حدود ۳.۵ میلیون بشکه از تولید روزانه نفت خام خود را متوقف کند.
🔹
۲ سوپرنفتکش اماراتی که شب گذشته هدف موشک‌های ایران قرار گرفتند، از بندر فجیره حرکت کرده بودند.
🔹
این مؤسسه، فجیره را مهم‌ترین قطب انتقال کشتی‌به‌کشتی نفت امارات توصیف کرده و می‌گوید از کار افتادن این بندر، از نظر تأثیر بر بازار جهانی نفت، هم‌تراز با بسته‌شدن تنگه باب‌المندب خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/449955" target="_blank">📅 19:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449954">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">فراجا: نیروی انتظامی در جنگ رمضان ۳۶۱ شهید تقدیم نظام مقدس جمهوری اسلامی کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/449954" target="_blank">📅 19:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449953">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyR8fQpv2omlotiwf2Pn1ADq5Pm4Uo8lIZQiP1neH-4LkIYRj094C_O-1S1iyZhKyFHGoreUA9DOaU6guiDtHLQiaiPy9M7u6Bya62GPH7_INnxM-__noKVxUO89A3k2R6JXx852tNlM7eEQfTkayeDtHoYdcOhmkuiRmYxkqm8Iz7tC81Z5rWH7uB9mBAyV6Stb33FA6mYGtJuPjkjio3AbjdAXKqxHW2K-QSNzZ-5dMBXYaI2wgrG_4fL72KwepJY5Xyf9pRKGC3WbELCX-tatG6UyF3FJRl_r2HTjnQSV1EQbV8AI3ja_Q53YlrexkAlaYoUqyLeVnhjqHnStRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵ بانکی که مجموعا ۵۰۳۵ ملک مسکونی در اختیار دارند
🔹
طبق آمار بانک مرکزی بانک‌ها بیش از ۶۷۰۰ ملک مسکونی در اختیار دارند که برخی از آن‌ها به عنوان منزل سازمانی در حال استفاده است؛ این رقم به‌غیراز ساختمان‌های اداری، تجاری، باغ و زمین‌هایی است که در اختیار بانک‌ها است.
🔹
در این میان، بانک‌های سپه، تجارت، رفاه، ملی و اقتصادنوین ۵ بانکی هستند که بیشترین املاک مسکونی و در مجموع ۵۰۳۵ ملک را در اختیار دارند.
🔸
رئیس سازمان امور مالیاتی روز گذشته در نامه‌ای به بانک‌ها اعلام کرد که همه املاک مازاد آن‌ها بدون توجه به زمان تملک، مشمول مالیات هستند و بانک‌ها فقط تا پایان سال ۱۴۰۵ برای واگذاری این دارایی‌ها فرصت دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/449953" target="_blank">📅 19:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449952">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/607893a909.mp4?token=JBuV19gR4a3L-t1YMOTENhzAZu5koBX52Xb8ndgOqLm8nBF9UEJhPDAFW4JGoforvyctf_VWxCErYt7dUhD12VvRfr-o6poRR9o2NksVFuc88pgkPJOiYhnUjLO4ODHCTsExAUGrynOe5Xz9wqD2XNWvLlETuVynOCgvoHg1QvXbNF-Fc762qLsZBOaX5UAewfa3b-pcZADgtq7XF-z3sykFyTFoSZ2UQ-XAgMBOIfjSdIj2HhtpHeAmwrBQ5u29n1qcNodVGkxnSENTcc20YBn6SN5X4ZtjD1vvnhVbpekdkXHwQKWeFeChP9v_cD_lzr0XXCvDJGrEqf0-F2tABQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/607893a909.mp4?token=JBuV19gR4a3L-t1YMOTENhzAZu5koBX52Xb8ndgOqLm8nBF9UEJhPDAFW4JGoforvyctf_VWxCErYt7dUhD12VvRfr-o6poRR9o2NksVFuc88pgkPJOiYhnUjLO4ODHCTsExAUGrynOe5Xz9wqD2XNWvLlETuVynOCgvoHg1QvXbNF-Fc762qLsZBOaX5UAewfa3b-pcZADgtq7XF-z3sykFyTFoSZ2UQ-XAgMBOIfjSdIj2HhtpHeAmwrBQ5u29n1qcNodVGkxnSENTcc20YBn6SN5X4ZtjD1vvnhVbpekdkXHwQKWeFeChP9v_cD_lzr0XXCvDJGrEqf0-F2tABQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در ۲۴ ساعت گذشته در اطراف تنگه چه‌خبر بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/449952" target="_blank">📅 19:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449951">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‌
🔴
منابع عراقی: شدت انفجارها در کویت به‌حدی است که صدای آن از داخل اراضی عراق به گوش می‌رسد. @Farsna</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/449951" target="_blank">📅 19:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449949">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffed4eebde.mp4?token=NIsJGIwLgcPBWkBCIQH4dOd1fYmaPZPR-kGOQTE4veep3luXqWtvmyMAQB4X1qw8crlf606KjY96up7jllzWgSQGZT7wjGyG0q7-o4ER-BwVqRDpMt4n6LESYvBe-Wpf3Cm1oJDqm6OYJUT4yA1s1CqAk4deOxQLZr71Sw2AKl00B9nUWro_B5XZFk-FY9XzqNqmgjRgn4OuzTjCSndNresTvfIALPUuVw7p4xq1qlxSbVtUJaOUdQtigmLEPcISgwJkLqmO9E8VxUKyNqfkGiDB-dRFCKyJnHDMLuMs01BpMWPkSE2Z_NIr-HArsp7MSTuWN7-osCbvOb7MPluDUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffed4eebde.mp4?token=NIsJGIwLgcPBWkBCIQH4dOd1fYmaPZPR-kGOQTE4veep3luXqWtvmyMAQB4X1qw8crlf606KjY96up7jllzWgSQGZT7wjGyG0q7-o4ER-BwVqRDpMt4n6LESYvBe-Wpf3Cm1oJDqm6OYJUT4yA1s1CqAk4deOxQLZr71Sw2AKl00B9nUWro_B5XZFk-FY9XzqNqmgjRgn4OuzTjCSndNresTvfIALPUuVw7p4xq1qlxSbVtUJaOUdQtigmLEPcISgwJkLqmO9E8VxUKyNqfkGiDB-dRFCKyJnHDMLuMs01BpMWPkSE2Z_NIr-HArsp7MSTuWN7-osCbvOb7MPluDUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ورزشگاه آزادی را شخم زدند
🔹
طبق تصاویری که سه‌شنبه منتشر شده چمن ورزشگاه آزادی به طور کامل جمع شده. قرار است لایه‌های زیرین چمن سابق تا عمق حدود ۴۰ سانتی‌متر برداشته تا زمین برای اجرای استانداردهای جدید آماده شود.
🔹
در صورت آغاز به کار برای تعویض چمن حداقل ۴ ماه زمان نیاز است تا چمن جدید مورداستفاده قرار بگیرد. مسئولان ورزشگاه دلیل این کار را ویروسی‌شدن چمن عنوان کردند اما میثاقی، مجری فوتبال برتر ۲۹ اردیبهشت امسال گفته بود: «کاری به چمن ورزشگاه آزادی نداشته باشید. چمن در ایران مافیا دارد. الان وقت کاسبی نیست».
🔹
پیش‌تر مدیرعامل شرکت توسعه اول تیرماه وعده داده بود: «سعی داریم در اوایل لیگ قطعاً به بهره‌برداری برسیم. شاید یکی دو بازی اینور آنور شود».
🔹
سازمان لیگ زمان آغاز لیگ ۲۶ را ۱۶ مرداد اعلام کرده اما به نظر می‌رسد این مسابقات با یکی دو هفته تأخیر شروع می‌شود. با فرض این تأخیر هم اما بعید است که ورزشگاه آزادی حداقل تا ۵ ماه دیگر قابل‌استفاده باشد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/449949" target="_blank">📅 19:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449948">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/971cb6b758.mp4?token=g4vOOw9XPemaZ1Abl98JfbCx-_5cx_lEA_P7WS1cz3E_i0De53hX4QL6XjQL_noeGGdnBbs3TPzMIV1NVtFQBB2BX1_dV3T9rVvRupLe8kkBgJH8x4hC1ct15L_xwWuiGJRZFuT1r94pnAIdBfc29KMRG-DQooE7qP_LLP6j0msM4HdgXoci3VLnOIm0AMJQ6pcxAj4V4CAn0fMPEfP4cxVb-xijjyyj02M1nxq0ISkEaSVZ0_eYIuyaRZEfY24TI0vE_0eKjzmsEv6xfhnz_r0hGJq_PcuyR9zeXRHaMVL8Cw2JYe0crBDL216wQ-4Er5ttQoREwnA8bSJuJ2F3oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/971cb6b758.mp4?token=g4vOOw9XPemaZ1Abl98JfbCx-_5cx_lEA_P7WS1cz3E_i0De53hX4QL6XjQL_noeGGdnBbs3TPzMIV1NVtFQBB2BX1_dV3T9rVvRupLe8kkBgJH8x4hC1ct15L_xwWuiGJRZFuT1r94pnAIdBfc29KMRG-DQooE7qP_LLP6j0msM4HdgXoci3VLnOIm0AMJQ6pcxAj4V4CAn0fMPEfP4cxVb-xijjyyj02M1nxq0ISkEaSVZ0_eYIuyaRZEfY24TI0vE_0eKjzmsEv6xfhnz_r0hGJq_PcuyR9zeXRHaMVL8Cw2JYe0crBDL216wQ-4Er5ttQoREwnA8bSJuJ2F3oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور قالیباف در مراسم بزرگداشت رهبر شهید  @Farsna</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/449948" target="_blank">📅 19:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449947">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اطلاعیه دولت: مراسم بزرگداشت امام شهید انقلاب که مقرر بود روز چهارشنبه از سوی دولت جمهوری اسلامی ایران برگزار شود، به روز یکشنبه ۲۸ تیرماه، ساعت ۱۰ صبح موکول شد.
🔹
این مراسم به میزبانی قوای سه‌گانه کشور در مصلای بزرگ امام خمینی (ره) تهران برگزار خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/449947" target="_blank">📅 19:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449946">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
حمله به نفتکش اماراتی در سواحل عمان
🔹
منابع خبری از هدف قرار گرفتن یک نفتکش اماراتی در سواحل عمان خبر می‌دهند.
🔹
همچنین یک نفتکش دیگر با پرچم لیبریا که در امارات مستقر بود نیز هدف حمله قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/449946" target="_blank">📅 19:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449945">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
منابع رسانه‌‌ای از حملۀ موشکی به اهداف آمریکایی در کویت و شنیده‌شدن صدای انفجارهای پی‌درپی خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/449945" target="_blank">📅 19:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449944">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شنیده‌شدن صدای انفجار در قشم
🔹
حوالی ساعت ۱۸:۴۵ صدای چند انفجار در جزیرۀ قشم شنیده شد.
🔹
طی روزهای گذشته چندین‌بار منطقه مسن قشم مورد حمله دشمن آمریکایی قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/449944" target="_blank">📅 19:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449943">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
منابع رسانه‌‌ای از حملۀ موشکی به اهداف آمریکایی در کویت و شنیده‌شدن صدای انفجارهای پی‌درپی خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/449943" target="_blank">📅 19:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449942">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfjDUUHwu-cRTz2DGHNk0DSKbZ7qC2O4Fz3n74wR5x1EutT4y9qg8368moQGC2VZ0ucbBiAqbd1K6tfmuFVX7Am3C-14Ej8jgqa9Ffom2a7paKld6E_NgVNDzCUgLzkV_RMZHbycQVcCJQNfuFJ7hhSYtAmdGsM6qjgYxUb5sE31-a3RUC7JzwEGVtDIbWgGiSrlzz95mBfwCjwlkGJOhTqnsvHzfG-A26CuSMXh1gy-hUt5ZxMmOUX20FZ9RcowlQBYI-w57knwnxTETOyRXh-dMLOd3dHi8ns-TR0-M4vWgQPifuBgtAfdNZl_RMU0U5Dv2gqbxDXpDmUAQVkHhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: در تاریخ، جنوب ایران همواره نماد مقاومت در برابر استعمار و پاسداری از استقلال بوده است
🔹
در کنار و قدردان این مردم وفادار و مقاوم هستم. همه جای ایران، سرای من است.
@Farsna</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/449942" target="_blank">📅 19:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449941">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QW9hOlKtx_SuheDRZFpL6v_JA0UJDJMXgPk1AXOiSG40k35rEhONljk7Ro5G0HrcMb9kk-vZHQcqKIsGs64sOQxDFozbGQo6j8DIb8zXuBUrbGFV9msul-8BZlsag4JEeuqnhG3Lm08n5Q-tGeJhkvHR9sCJDzTlCdQo85d_KKEXfJMBBw4EzXk4lzv5Z6L7iawRZC9_mmyFs8LvVIJkmTnmHL_xPAOnWQsfXUeI4BC2ithkNBudsNTcbvBHRRE439inIYOC3u5M28iH25H3lUxf_iQEhOkELqOXjNtlv_KvQ13efQllXFJHQVS0Mt4J4l1KFngfixA7di-5U4gpQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توسعه پوشش ارتباطی ایرانسل در چهارمحال و بختیاری
🔸
ایرانسل، با راه‌اندازی سایت جدید ارتباطی روستایی در استان چهارمحال و بختیاری، امکان دسترسی ساکنان روستاهای جدید به اینترنت پرسرعت را فراهم کرد.
🔸
آیین افتتاح طرح‌های ارتباطی روستایی ایرانسل، ۲۳ تیر، با حضور استاندار چهارمحال و بختیاری و معاونان وی، معاون حقوقی وزیر ارتباطات، رئیس پارک فاوا، مدیرکل رگولاتوری منطقه مرکزی، سرپرست دفتر USO وزارت ارتباطات، مدیرکل فاوا استان، مدیر ارشد منطقه مرکزی ایرانسل و جمعی از مدیران و مسئولان اجرایی، به صورت آنلاین برگزار شد.
🔸
در این مراسم، سایت ارتباطی روستایی ایرانسل، برای پوشش روستاهای کلواری و قلعه سمه در بخش منج شهرستان لردگان چهارمحال و بختیاری، به صورت آنلاین، توسط استاندار چهارمحال و بختیاری افتتاح شد.
🔸
با بهره‌برداری از این پروژه، دو روستای کلواری و قلعه سمه، ۵۹ خانوار و ۲۸۲ نفر جمعیت، با اعتباری بالغ بر ۱۰۵ میلیارد ریال از محل طرح توسعه
#روستایی
وزارت ارتباطات (USO)، تحت پوشش اینترنت پرسرعت ایرانسل قرار گرفتند.
👈
جزئیات بیشتر
@irancellnews1</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/449941" target="_blank">📅 18:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449940">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vaOfhwFyZFPfoX3L11quCr52z8LlXuAWA2KegeKL02PvkIu9ENudnkL0lNB2U7shYNt2Id5CrY_qChSYP08hauqm_hmQ5xoQFfGVXoLQDoq7_obPZ_Bzg_9JbJo-buPcaXEhuL3RZq7DRuFEvReWVoj_0p4etTDLNEPf01EEJxrTFBUKSThr8_QuOLdnLOGOCLNGV-jqIPsMJpJSV7zHM2wxvtp5vW7bCmVKAAxgLDy2KXHckgBmO3cFrKOko263QcuTTKVTKSzv1y7MY2B2P1sd2cYq3A1cA67ViUFfzLrgwJZMHb6GON_bTrop5InJK8xRf5_vl2qPjDpG52iY3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امکان خرید ارز اربعین ۱۴۰۵ در اپلیکیشن بله
خرید ارز اربعین یکی از خدمات مهمی است که زائران سال‌ها در اپلیکیشن بله دریافت کرده‌اند. در اربعین سال ۱۴۰۴، بیش از ۹۵ درصد زائران ارز خود را از طریق بله تهیه کردند و امسال نیز این خدمت با هدف کاهش مراجعه حضوری و تسهیل فرایند دریافت ارز در اختیار کاربران قرار گرفته است.
زائران می‌توانند به‌صورت آنلاین و بدون معطلی، تا سقف ۲۰۰ هزار دینار عراق ارز اربعین خریداری کنند.
به صفحه خدمات در اپلیکیشن بله مراجعه کنید و ارز اربعین را تهیه کنید.</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/449940" target="_blank">📅 18:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449939">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/449939" target="_blank">📅 18:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449937">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd47320c6e.mp4?token=qw3E3fBCprf-sL3BDOeIKwThyIHu2M_6hRhPF9738vkiBCKLphuXv94gby8SqLXbB0w80vZfcjc8Bxfiqa_3Ai88sP3_5sPcAw3s9wUnyuq2hObMnVQGW2TiX3JKFJ833XRwx6Wmn6XWU2sDpPIEteuzdQcgNwmKlj3DXSSMYj_uctXq21LabHrySe9HD_R8jeefhC7WvXQZK2eSW1a4-ciZFIWE178fcKKA41RjqpuwM8CP-dBhOHYhyjGB_QV84KMd8e5-5TEH6ujN5U1D65TEQSlC8XmEP1n1fYWZUtRB1IOzpYUXXp9teutf6e-SM5PHJ1vZZrCT0K8CYZV_sp4p9WVITZO94Plf2y67q3P6Wvgp1e0uk_9XZmnkTr3LDsUxeEIQRZmKQH2s_o3hKxh-TACYy6z0JwfhRW3TK_pZWZ4GBni1-t6W7aVL5JwvJbwtu1nIqpGcKCj4U2SUx5Fmhx5fzQ-QHEI7FqcpcSd2X18ymTnUF2y1YS8cJcmqy3LDdrk0Hnk2R_uQBlq3JhcjGyQg3Oszkn7NycBdin1KLD-wQheeDpTdAp3zWj_44D4ekUT5Y3iqAORIiJJSi_kJyRF2DdW2W4FNagflCCTwBPeXGQsvoNJxAaEVGTEj6P8gCg8hUSxJYtZxZBkFxgb2h71v0RmmYuN8sJoyIKI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd47320c6e.mp4?token=qw3E3fBCprf-sL3BDOeIKwThyIHu2M_6hRhPF9738vkiBCKLphuXv94gby8SqLXbB0w80vZfcjc8Bxfiqa_3Ai88sP3_5sPcAw3s9wUnyuq2hObMnVQGW2TiX3JKFJ833XRwx6Wmn6XWU2sDpPIEteuzdQcgNwmKlj3DXSSMYj_uctXq21LabHrySe9HD_R8jeefhC7WvXQZK2eSW1a4-ciZFIWE178fcKKA41RjqpuwM8CP-dBhOHYhyjGB_QV84KMd8e5-5TEH6ujN5U1D65TEQSlC8XmEP1n1fYWZUtRB1IOzpYUXXp9teutf6e-SM5PHJ1vZZrCT0K8CYZV_sp4p9WVITZO94Plf2y67q3P6Wvgp1e0uk_9XZmnkTr3LDsUxeEIQRZmKQH2s_o3hKxh-TACYy6z0JwfhRW3TK_pZWZ4GBni1-t6W7aVL5JwvJbwtu1nIqpGcKCj4U2SUx5Fmhx5fzQ-QHEI7FqcpcSd2X18ymTnUF2y1YS8cJcmqy3LDdrk0Hnk2R_uQBlq3JhcjGyQg3Oszkn7NycBdin1KLD-wQheeDpTdAp3zWj_44D4ekUT5Y3iqAORIiJJSi_kJyRF2DdW2W4FNagflCCTwBPeXGQsvoNJxAaEVGTEj6P8gCg8hUSxJYtZxZBkFxgb2h71v0RmmYuN8sJoyIKI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظه اصابت موشک‌های سهمگین ایران به پایگاه آمریکایی‌ها در اردن
🔹
برخی رسانه‌های عربی با انتشار ویدیوها اعلام کردند که این تصاویر مربوط به لحظه اصابت موشک‌های ایرانی به اهداف خود در عملیات بامداد امروز علیه پایگاه الجفر در اردن است که نظامیان آمریکایی از آن برای حمله به ایران استفاده می‌کنند.
🔸
بر اساس این تصاویر با وجود فعالیت گسترده سامانه‌های پدافندی در پایگاه مذکور، موشک‌های ایرانی ضمن عبور موفق از سد پدافند دشمن، اهداف خود را با قدرت تمام مورد انهدام قرار می‌دهند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/449937" target="_blank">📅 18:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449936">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svvUWPLiKtJPxWiE1tTqKhVnx4mtmAOKqlFygbxUwLYIwIYruk7mk15zF7clf6OtECv1T1zPlM7G0-AxwVtw1Y9ICzpdDZiwrTyWJB1HeyK5FhKAXf90ZtGDZPiar78t-sYBANuS7GVCIycm291qn1JVkKx5v8bmaqwf_AwPcu62L2Pn42bxVdA7i-DSpV3MCRBCH4HR1LdpdElUSqtlbpg5kP1IJ2r0lsT2lpEWUQrZRRv7fp1ALCXa29hJOOMUgrZmgkmnd0_5Cvu4OTm2_2ti2Ft6b92jshdSzOSTNhnMPu9WSgAYJ1IRUdeTcAyn8D7ggEaVCiNPnQRfEFuSxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترامپ: از این پس، آمریکا به‌عنوان «نگهبان تنگۀ هرمز» شناخته خواهد شد و از کشتی‌ها عوارض ۲۰ درصدی می‌گیریم.  @Farsna</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/449936" target="_blank">📅 18:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449935">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0274d3073d.mp4?token=DUbSauyt6B4QnTW4IiwJhNqtEALiVSMkQTgNwYIGeidBXwfWVawXKLdZ7F8xOVU-KHAyJHkgPLaSX5ilaPJjHIztqF8-JCyttI6rK7Hu0s0rTYu82nOvDSF07v0yiDB_2RGi6hV1VvpknnaJeunGxRZ77J8Tjjpqio7EshEe5VZaMp5izUXnsrNYhOhZX4fDP_e-dIvVvn_RkyTraLT4NmHQ3_aHbayJaxaHGV0AN2fZmW7iLR3xi91Zkbz5oMfSIOcbBBatRfFhqL8efeyhyClPCfBYAMinY0R6uwSlURf10mrvYwjqjYBqzOkCH4_Ze5WcqiwKxhoHZGY8PqFV3bv4lyWCyuD77WaxWul5KGX2omAz0EavHli05Vj4Kv5bdJI69wlUbi8-92A7vABI3ir5ytcadLCb9ZmPUppAnAjtULAp2ieIIPBLMmlRqEOwuzMax0C3jpYRd8-tbLHXVfViwogqxIKd9ecrfQngQMSzaGdTOLcMKqKryxtZJcrukFohEpdbyw8WdmPxk17z5qLWSQgWzlHTEX4tn6YwWir1xNkAV5UAMDjSLMPDx-Dl3YZOPzdDJGSFdlkQmEN98oYkmqu-OwEC4RHEWzuxa1UBQANtkL887AM0J3Ov33yapsO7mvO8OhAvlkaMCURE6SUc2PdjPTcy-KerW1ZWRC4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0274d3073d.mp4?token=DUbSauyt6B4QnTW4IiwJhNqtEALiVSMkQTgNwYIGeidBXwfWVawXKLdZ7F8xOVU-KHAyJHkgPLaSX5ilaPJjHIztqF8-JCyttI6rK7Hu0s0rTYu82nOvDSF07v0yiDB_2RGi6hV1VvpknnaJeunGxRZ77J8Tjjpqio7EshEe5VZaMp5izUXnsrNYhOhZX4fDP_e-dIvVvn_RkyTraLT4NmHQ3_aHbayJaxaHGV0AN2fZmW7iLR3xi91Zkbz5oMfSIOcbBBatRfFhqL8efeyhyClPCfBYAMinY0R6uwSlURf10mrvYwjqjYBqzOkCH4_Ze5WcqiwKxhoHZGY8PqFV3bv4lyWCyuD77WaxWul5KGX2omAz0EavHli05Vj4Kv5bdJI69wlUbi8-92A7vABI3ir5ytcadLCb9ZmPUppAnAjtULAp2ieIIPBLMmlRqEOwuzMax0C3jpYRd8-tbLHXVfViwogqxIKd9ecrfQngQMSzaGdTOLcMKqKryxtZJcrukFohEpdbyw8WdmPxk17z5qLWSQgWzlHTEX4tn6YwWir1xNkAV5UAMDjSLMPDx-Dl3YZOPzdDJGSFdlkQmEN98oYkmqu-OwEC4RHEWzuxa1UBQANtkL887AM0J3Ov33yapsO7mvO8OhAvlkaMCURE6SUc2PdjPTcy-KerW1ZWRC4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ابلاغ پیام تشکر رهبر معظم انقلاب از ملت ایران و عراق و دست‌اندرکاران برگزاری مراسم تشییع و تدفین و بدرقه آقای شهید ایران توسط آیت‌الله سید مصطفی خامنه‌ای
@Farsna</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/449935" target="_blank">📅 18:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449934">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff0ec61629.mp4?token=uXAoaMpteeCRNFbKMp6Z8w4thPO1mY5bjtPpt7mxRZkWb03pKowLUE5z_KOeGnV6B_E_Fjld0NQEv3RgQ85SQhnTXFgkeSTFelLciEjbfXzs5gOZhCf-XcULipzh5AgmeB9LP-9ItdjVevs469GhlPBXVs4A6wJcZR2UnZki3TQuJKsAZ9fRp0bqxYywRqUDcJy07VcnHSMBiEiJoK4XWKb1McHUdacrZzrctDpjFZONOJNOpbJfDaj0ZUx0mZWzGXps0KPeBBkjoKWBATGGhXHIxjQ_VFhmR9-HREJ8e9lh_cdV5dXDcPnY_FrOd_q-7IUA3YvarG1QMvKOwClMjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff0ec61629.mp4?token=uXAoaMpteeCRNFbKMp6Z8w4thPO1mY5bjtPpt7mxRZkWb03pKowLUE5z_KOeGnV6B_E_Fjld0NQEv3RgQ85SQhnTXFgkeSTFelLciEjbfXzs5gOZhCf-XcULipzh5AgmeB9LP-9ItdjVevs469GhlPBXVs4A6wJcZR2UnZki3TQuJKsAZ9fRp0bqxYywRqUDcJy07VcnHSMBiEiJoK4XWKb1McHUdacrZzrctDpjFZONOJNOpbJfDaj0ZUx0mZWzGXps0KPeBBkjoKWBATGGhXHIxjQ_VFhmR9-HREJ8e9lh_cdV5dXDcPnY_FrOd_q-7IUA3YvarG1QMvKOwClMjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز سخنرانی آیت‌الله سیدمصطفی حسینی خامنه‌ای در مراسم بزرگداشت رهبر شهید  @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/449934" target="_blank">📅 18:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449933">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ae5120c1.mp4?token=iOjwSha9MJV-bC-iA00rXIRmHP085oCh5kQmI2DNRiGq55_fNMiCgkOtysQ71aupraQ4GwPgP72wjtX4vytjhL-gVgT2cEbChb99Ss6JkT7FQ2ELpcokkEqLrknjul50YnVIbpgL3q6nO9e8u76TW4voVAf63XvMjIxmF0Z8Nx-wUghq6fvnIH3Ez9l3KqqxMnGktqoO3BAPcSWMH7nbeVguyLA-PcgWhQ5PzmG4KFsUFMEIzmDAPWzhC0MZ79ztya2Gbf0hGptVtPx_mklM_Xx-R5nJL2rxigf6G7XY_kotAM4f8xDmMdZquT72-kdkZSvW0HwSBweFhXyh59EY6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ae5120c1.mp4?token=iOjwSha9MJV-bC-iA00rXIRmHP085oCh5kQmI2DNRiGq55_fNMiCgkOtysQ71aupraQ4GwPgP72wjtX4vytjhL-gVgT2cEbChb99Ss6JkT7FQ2ELpcokkEqLrknjul50YnVIbpgL3q6nO9e8u76TW4voVAf63XvMjIxmF0Z8Nx-wUghq6fvnIH3Ez9l3KqqxMnGktqoO3BAPcSWMH7nbeVguyLA-PcgWhQ5PzmG4KFsUFMEIzmDAPWzhC0MZ79ztya2Gbf0hGptVtPx_mklM_Xx-R5nJL2rxigf6G7XY_kotAM4f8xDmMdZquT72-kdkZSvW0HwSBweFhXyh59EY6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: با قدرت از نیروهای نظامی دفاع می‌کنم
🔹
من نه‌تنها خودم را از نیروهای نظامی جدا نمی‌دانم بلکه آن‌ها باعث عزت و سربلندی خودم می‌دانم و با قدرت از آن‌ها دفاع می‌کنم.
🔹
من حاضرم بروم و در همان خط مقدم بجنگم و از شهادت نه‌تنها نمی‌ترسم بلکه آن را برای خودم فوز می‌دانم.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/449933" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449932">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa019dec41.mp4?token=DihSicb0nhOUaMxoHSvmCI4ywEGBQ_a2wSuDcbbhES8GGC5vy3ulpkiMnhHenE9ANCLRstvqpbWbLU9o9rSOPdtg28sIdmKhC-3zm9wpPG9R7hBGtVDiU_Kf3GtAgUEFst91piYl7L-qrxe0FBeU8zeqsoKIZPtOU37I29XIvUyInuHuOte6OnH2i1g78K4yJH9rKCxMBBTjJ-wcGrcBfF537z_sxh0rcdlRZ7PBZPJjo_TfxaYGSrCBasZzH_GqbouXsrhE9JSytJkJEFJCXgZTP4GDHbELwNeUUXueV5ZZzxE8XRq-PCglze6KA_OuZK1HjfMWkRCqW2bnCNAivA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa019dec41.mp4?token=DihSicb0nhOUaMxoHSvmCI4ywEGBQ_a2wSuDcbbhES8GGC5vy3ulpkiMnhHenE9ANCLRstvqpbWbLU9o9rSOPdtg28sIdmKhC-3zm9wpPG9R7hBGtVDiU_Kf3GtAgUEFst91piYl7L-qrxe0FBeU8zeqsoKIZPtOU37I29XIvUyInuHuOte6OnH2i1g78K4yJH9rKCxMBBTjJ-wcGrcBfF537z_sxh0rcdlRZ7PBZPJjo_TfxaYGSrCBasZzH_GqbouXsrhE9JSytJkJEFJCXgZTP4GDHbELwNeUUXueV5ZZzxE8XRq-PCglze6KA_OuZK1HjfMWkRCqW2bnCNAivA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز سخنرانی آیت‌الله سیدمصطفی حسینی خامنه‌ای در مراسم بزرگداشت رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/449932" target="_blank">📅 18:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449929">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/045c4dcd4a.mp4?token=m0-8NHkNI6TJxe_sh9PGDbaUIA9uwFtI38FzlrlukXFhWrtK--hVbDxLInBA4gxBzry7_MKVdNTdXxQDK6b1nFj9lj9Vfz6q135xt_zyX_gd7JrYJTXVrr4dqhpb4pBzBqjFM8pZto9OEImUzKmitByn1b2SZ9rTeMAi5Ad_mDHNAI3y83QV6-0FRnNu2nOByh2SFFwFQ4wDbWEa014OcZeLwD08uwswik3TAuAm7loARwm3iV3QE0X21apW5KP9gxHfBFTW5pRC9s4rCFeUwppdJyODTLPJsYeOHJh_oZwh8feqV7gheiHXy0yU2kY0JEeRQMV4nluOG9V4vg3Q5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/045c4dcd4a.mp4?token=m0-8NHkNI6TJxe_sh9PGDbaUIA9uwFtI38FzlrlukXFhWrtK--hVbDxLInBA4gxBzry7_MKVdNTdXxQDK6b1nFj9lj9Vfz6q135xt_zyX_gd7JrYJTXVrr4dqhpb4pBzBqjFM8pZto9OEImUzKmitByn1b2SZ9rTeMAi5Ad_mDHNAI3y83QV6-0FRnNu2nOByh2SFFwFQ4wDbWEa014OcZeLwD08uwswik3TAuAm7loARwm3iV3QE0X21apW5KP9gxHfBFTW5pRC9s4rCFeUwppdJyODTLPJsYeOHJh_oZwh8feqV7gheiHXy0yU2kY0JEeRQMV4nluOG9V4vg3Q5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور قالیباف در مراسم بزرگداشت رهبر شهید  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/449929" target="_blank">📅 18:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449928">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_Zt9PbAIKeL1YeXj9sKhWH92gaHBadg9_qotdI2kCcL7wqJuA834oMBs217V030kQu9frWNERyLgLevND7dP3Onp9Ukfl4Z8lhYalbdScojuUQuEogbkiGFf88PVVdNDbzRiu7NviQjy3xvPxX4r3QfClYCqN4LsPIyYEJmA6kZMxXq9iDPVzGMYcLQjueIkVdUzbEuIL0_egJSVdpHg15v5gHd4s3EVEM-t-UUBc4fs2pHlySeSOzLjl3iAEfi1r6DERS10A8jym8kzrxltIhyklF4LmdXMRrLmhGyhlnJR0cfkAdkmu7_jm7VMa781iAv3HIukYjB2ih1V77gfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعلل برای نجات چشمه ۸ هزار ساله ایران
🔹
با کاهش جریان آب چشمه‌علی، کارگروه ویژۀ احیای آن تازه هفت سال بعد، در سال ۱۴۰۴ تشکیل شد تا احتمالات خشکیدگی آن را بررسی کنند.
🔹
حالا مدیرکل میراث فرهنگی استان تهران اعلام کرد ارائه گزارش این کمیته به‌دلیل هم‌زمانی با جنگ تحمیلی سوم به تأخیر افتاده و علوی، عضو شورای شهر تهران هم می‌گوید تا زمان اعلام نتایج، امکان ارائه راهکار نهایی برای احیای چشمه وجود ندارد.
🔹
برخی مسئولان، عملیات ساخت خط ۶ مترو را عامل این اتفاق می‌دانند و برخی دیگر خشکسالی را دلیل خشک‌شدن این چشمه عنوان می‌کنند.
🔸
چشمه‌علی در شهرری قرار دارد و با  با قدمتی بیش از ۸ هزار ساله یکی از قدیمی‌ترین چشمه‌های ایران به‌شمار می‌رود. این چشمه از سال ۱۳۹۷ به‌تدریج خشک شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/449928" target="_blank">📅 18:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449925">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/itIjBdKXBieCGu93TJiFpVQup5mTEg8fN0nnY7KtVf-jWt_bjTiV8_aFmT0gr0IH6kgXkGzntFpot2yhRv-ab1rvqmP4FQuafhMwCEEpq6I0Poa9dctSoZvHLQkj__8b8j0HWIphSsA5YAXBwW7ccjnEWbBNVWHwJ4fhNUPi5C_yWjsm9sU-uqFQnX4cwXqa4LyeL_G5rjZjt3ValxqtgOGP_GYdQ2H39JKJJwDQ1_71PJJKTQGF_cC4AaZwgNhnJ05RH7tR9uqzRf00hRo9ev7GiZSgMYLYd7Qdfz2v4JxaGjTG0XmikDAts-3uX41sVoYlMho7kNs7wVxiHVJ82w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A8uLdkBTVxyOqOZCU8NY1nJtuqbhlJy_CXUkHT9_lABF3bwmy7zo0MKt5bOYMgJUASlcBYP3mmOtaJnmrAcK-55AgGvS2cfwtUdh0ag0BiVi0_Xi4WWLMdVduU-xmQHWLJBiULwld4UwlUXh3MSA-ntVaJlM0_A6PPce9lEapsd3d3yDdsx_Fo3II_U_pFpfPUnuxr6quza7T8iNDdFve7GvoZK5AZAiyxb4_JCBZX9HUrgngWrl2oAkdXGGNc_xgMyk9ydeyKVTIKdrpv88DaKkC8q5q43y-26wa8Q0DG9-p_W_P_uW8e5V82YRjRrNokHSuBnNLoUdoBuNAMPCjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SC0gZkqizlCDvELFbMZklWlBuoMDfzSaXBKdF0hC8n8p5PTNzTgKumdGheOI2AOt-F3PuBid-hXBkfC2jHckv5SeEq1Tb6xeGXW7SIuwFhGoQuouE1DsR60Faa2Vwxb43aSbj3b_qJISnaB9sAufcaTAqgzQoN49cWXzAXNA1ltKNc4Vp9f1kbieR9NMw9UGklrPR-0-5vZYOInq91A6yRVtuzed4WMkXBblWMf-5eN76xHoXQ27bAlnUW7LdzUwqagQ_sPjHN8Quw5mRAOohsPc5OA-HeildBlGwRzHnm8Nc0GNsPkHv557gn5yn8lpFiaCwBH-204rArJ9mbke8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مسئولیت قتل ترامپ با ماست!
🔸
تصاویری از موشک‌های شلیک‌شده توسط سپاه به منافع آمریکا در منطقه
@Farsna</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/449925" target="_blank">📅 18:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449924">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFhzKO9lDDX81H28fM7iV6TNk80hBtC4eTX5HrUsZvl_nNP5p7Guv9Ze-e3JROe8-DjX27ddnSXzv8E-IRwGLBEHKUOSVsNkicROX5eylO8SrbxTNoXCxBabWYzGV1M632QMexexUhqBVYBuum9LSqF1sFYwgA9gD3SXsdmsVkh1r7AbeuhR-wGOvZ_ly5ds0-UyGPrgs5mtSL5B8islVWbdWy5e-oQoMWsXZbuW0eCh5YxsewLxyKUNWBMTrlIXzykSw-W---Tsyn9p6Zdz1ekvTKGYlEp9N_L6CqPWSij7EbiGiW6tYu4g_x0zze1tHlJEoCR0aMonXQhphOO8Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقاد شدید رهبر دموکرات‌های سنا از عملکرد ترامپ در جنگ علیه ایران
🔹
رهبر اقلیت‌های سنا چاک شومر:  ترامپ به‌طور رسمی به قانون‌گذاران اطلاع داد که کشور بار دیگر با ایران در جنگ است. واقعاً؟ ممنون دونالد، انگار کسی این را نمی‌دانست.
🔹
رویکرد تکرارشونده دونالد ترامپ در جنگ ایران یک استراتژی نیست، بلکه دستورالعملی برای یک فاجعهٔ کامل است...  ما مدام به عقب برمی‌گردیم.
🔹
قیمت بنزین بالا می‌ماند، تلفات افزایش می‌یابد، هزینه‌ها بالا می‌رود. باورنکردنی است که این جنگ چه فاجعه‌ای است.
🔹
چند بار دیگر باید این اتفاق بیفتد تا دونالد ترامپ بفهمد که باید جلوی این جنگ وحشتناک را بگیرد و به آن پایان دهد؟
🔹
مردم آمریکا بهای شکست کامل ترامپ در ایران را می‌پردازند. نیروهای نظامی ما در معرض خطر هستند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/449924" target="_blank">📅 18:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449923">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c81c0eaf70.mp4?token=gm-MNlia84ICFWt2JTc-Wz9tkGD_HJ23HzfLEaoHTL6eEf5cMCijeU_ZjAFdrx0BzGEGbt7I-4Zs8MiJQ2iWU3y0TMmnucJswJlVEDYR43DXHTKlX7_h6DgGraweahoQK5eaZQC4FkujXAwWj3-Mik8lwr_1YYoj2ZBTK-A3dSj_mt5x_xiCNK6hlgRq4IWEusatAJOYRQEX3iiUDK95xme9H6ccgqyYfRqGWtzXldn-qtazCEyTdOsdsSNUNcIiNIUIFtUfwBvM3CeDkX9YR15AeFPi4FygncsH6f0h6jzDimd0HAzU4w_cCYMw02Tz7pG2DBw-ZU1Hr7LPSIcIYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c81c0eaf70.mp4?token=gm-MNlia84ICFWt2JTc-Wz9tkGD_HJ23HzfLEaoHTL6eEf5cMCijeU_ZjAFdrx0BzGEGbt7I-4Zs8MiJQ2iWU3y0TMmnucJswJlVEDYR43DXHTKlX7_h6DgGraweahoQK5eaZQC4FkujXAwWj3-Mik8lwr_1YYoj2ZBTK-A3dSj_mt5x_xiCNK6hlgRq4IWEusatAJOYRQEX3iiUDK95xme9H6ccgqyYfRqGWtzXldn-qtazCEyTdOsdsSNUNcIiNIUIFtUfwBvM3CeDkX9YR15AeFPi4FygncsH6f0h6jzDimd0HAzU4w_cCYMw02Tz7pG2DBw-ZU1Hr7LPSIcIYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور مخبر و جهانگیری در مراسم بزرگداشت آقای شهید ایران  @Farsna</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/449923" target="_blank">📅 18:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449922">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApJTvOi8W8DsUHuEEpPAB1qw0UTSmxEhFUr22JnnO8qf9scMuVWkukJ9kvqNKkrRML9-Grpj-zM8slVFDMODPEqsBTscXQcdqfEJt_QtVFF9xv5U7HlXE34tVToWv6TEN3occTJwIvNQ9-o6Jep6GiDTPKyDmGnVg4T1w5wlNOOPw9R8ZGyoWwsYV48JLgCZf7og9Jbrkam0_04PkRwe4178niAKtlkdqhQoLYYNFqHjSHxMIDhwCOLuoAkRdNPNwFndtmUsBbr1ajaafe3S0TaI1EPPk4rk8GwNWuvfAQ1ipg58P2HCxjZ37TxbpvOLZKYZWreMEaHObbJ9xQKyGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز خاموشی‌های پراکنده در پایتخت از فردا
🔹
شرکت برق تهران: با توجه به افزایش شدید دمای هوا و رشد قابل‌توجه بار مصرفی در پایتخت، محدودیت‌های برقی و خاموشی‌های پراکنده در تهران از تاریخ ۲۴ تیرماه آغاز می‌شود.
🔹
این محدودیت‌ها در راستای حفظ و کنترل پایداری…</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/449922" target="_blank">📅 18:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449921">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ace46cf38.mp4?token=lS5XZGUTYoJkmKlENf6mSUM0Vjj5Ur-rpJ-5EfCAzOjXMGIf89UxMgI0SXPLsHnGt9lc235kbBJk_Jjxts2aro6nPx9_5lO2ikawoRDtKmDRmtuq6aMIKAYT9Aqx2p5swgqc2ci54uL7mBcZKhf7ICPcJIXg1MspFTg7O8B5dgaylFPyxxiiJC9EDtIKL1pla2Mdada0Jjs3krDPE6h04krUgnd2MS4F1MTKgMMZKwwV3ZBVMxOP6bOJ5oLqWEDtAjpN2-4c-XRIML6vqi5QPF3Ib4_S7JJLOpTdVsv1rvSuQtzz3nWHJcCL6wQtcr9DIY4avRJaOsGhZkYf02ECLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ace46cf38.mp4?token=lS5XZGUTYoJkmKlENf6mSUM0Vjj5Ur-rpJ-5EfCAzOjXMGIf89UxMgI0SXPLsHnGt9lc235kbBJk_Jjxts2aro6nPx9_5lO2ikawoRDtKmDRmtuq6aMIKAYT9Aqx2p5swgqc2ci54uL7mBcZKhf7ICPcJIXg1MspFTg7O8B5dgaylFPyxxiiJC9EDtIKL1pla2Mdada0Jjs3krDPE6h04krUgnd2MS4F1MTKgMMZKwwV3ZBVMxOP6bOJ5oLqWEDtAjpN2-4c-XRIML6vqi5QPF3Ib4_S7JJLOpTdVsv1rvSuQtzz3nWHJcCL6wQtcr9DIY4avRJaOsGhZkYf02ECLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بابای مهربانم، دلتنگتم عزیزم...  شعرخوانی محمود کریمی در مراسم بزرگداشت امام مجاهد شهید در مصلای امام خمینی(ره) تهران. @Farsna</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/449921" target="_blank">📅 18:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449919">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a4ea4b688.mp4?token=TF2Giuxtzdigtm4z4Oqc3BclxTFKkoF_YO9BGtWynDvLJJvMHO5JtDJtTKrEK0Jr2E7vq4f8lurMopcjI1nhOMltmAHGkUDSWeW5eMN1kq794Y6TrLcFVPZ4DL-WWjMaP2F7jFnxTTnFztSSdQtk7wikCa2qp-mk25KWvbDxwRp2sju9F0KP2QgSvJsdSCUTWSg70-YknV_9OzPJTk9867q8xncD5sZliQNvb6Z63MWkhSdbRnIX3-l8-WMBgihKQLPxh8h932X07Sms1dfnWC4NY5VYH9MNqTkRMmBlLmKcRVX14mCy7S6G_1ydNMC5yZDtQSuJzXH4ieAbDTThsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a4ea4b688.mp4?token=TF2Giuxtzdigtm4z4Oqc3BclxTFKkoF_YO9BGtWynDvLJJvMHO5JtDJtTKrEK0Jr2E7vq4f8lurMopcjI1nhOMltmAHGkUDSWeW5eMN1kq794Y6TrLcFVPZ4DL-WWjMaP2F7jFnxTTnFztSSdQtk7wikCa2qp-mk25KWvbDxwRp2sju9F0KP2QgSvJsdSCUTWSg70-YknV_9OzPJTk9867q8xncD5sZliQNvb6Z63MWkhSdbRnIX3-l8-WMBgihKQLPxh8h932X07Sms1dfnWC4NY5VYH9MNqTkRMmBlLmKcRVX14mCy7S6G_1ydNMC5yZDtQSuJzXH4ieAbDTThsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور مخبر و جهانگیری در مراسم بزرگداشت آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/449919" target="_blank">📅 18:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449918">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d74124c178.mp4?token=IoQFFdZi93Uu-mpIUXrJFJ9-LZ_hzCngL-02GN88dNZNudlv4qnvJlaixtQ9xmhfQB_6zPedcWyi3aYu2huHNUIqqo7xBIBrMVUPU1IEHGqrWFLMYM8geOXa3qhUmQ6lMQRNVDhgp5suRIGn0kCahno8mmTswFurLkFpsws-0bwB4mIPQA1PUBy1DtUT9DXGqZ7MvxKwXz1CUT2a1AaVYsF0KIhSD5E0vaq4GVLG_eGdBRgoZ0okLabc3uBxCs4blrSoFJesADha0fUJUMbzH6L-dnqbT93lxSHsek9a14jlZMFCCQLaro4CqXqH33ArFzlWflETKDewjS1dMIEMcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d74124c178.mp4?token=IoQFFdZi93Uu-mpIUXrJFJ9-LZ_hzCngL-02GN88dNZNudlv4qnvJlaixtQ9xmhfQB_6zPedcWyi3aYu2huHNUIqqo7xBIBrMVUPU1IEHGqrWFLMYM8geOXa3qhUmQ6lMQRNVDhgp5suRIGn0kCahno8mmTswFurLkFpsws-0bwB4mIPQA1PUBy1DtUT9DXGqZ7MvxKwXz1CUT2a1AaVYsF0KIhSD5E0vaq4GVLG_eGdBRgoZ0okLabc3uBxCs4blrSoFJesADha0fUJUMbzH6L-dnqbT93lxSHsek9a14jlZMFCCQLaro4CqXqH33ArFzlWflETKDewjS1dMIEMcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پزشکیان در مراسم بزرگداشت امام شهید  @Farsna</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/449918" target="_blank">📅 18:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449915">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LNgsg4sgURoadu8kwiAE3DQEuKNAAX0EUjOI48bx2IupxL4l3m8pU5KMCfIkc2mzzNXmFzEwF91tIdY3PTfjJNs9vC-0i4BuCBBxgn9P3VdQ1GOfRJDsAFkNDa-o0b6WMQQejwf4NzC6NA230NzugdnbM6nnzgTHpMoGxZgM8WrtadMbeY2hCZZNuvredo_z215IWg9ZwGpFY0tmOGLkR6eGIpbZVveMvfhu4QEX0GY0hGG748uUufnTGOmYH5GOTe7-U0gpsjv_sIWYbmhGSJFh4XvtVhHy1KXzxgSDxSfde7qIEdf6q3oijKagnj5CVKlcN-LPL912wxAMWX4vVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/My1QSs3QU1j8AFc_NLcJRwPDB6g07RH6OTyssi93BQ3P28HkEb3unsiyLWmrvoP8ei4iQLqRjf4QOxFVRrD6mKTKoi1M26hY1Kcq1JQEQZKo-xj2RFgLWTPYjgJkfD4t5Sgm1G1Bv3C-Kv4OpFo-o4s8qZ_nK5_QdpsEIPQqVi9BsWLyNXJDWDLx-V5duukTm5xY0oVb7yixEs5xbtRWZlB4UWmUD58_pOuLnZanxLhZIboFcmKzrZRBDky6TrOpDSJK2Y_nJRPNFGUYM5yHW_s9j2jZ_XLBRLR1w42Biqnrnu8yox4DRj0KRadLfeF-pDNICsJ2QF7Vf9-TboK7-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n3ysQJEiRCqDH3hPAv2kgVSvziBWqNPlVYlM6R1S95TcFJvXnwAs85vPXfFOGmjTyv9GqpeSxSt9GwET_QOP6d5iVa9GOvauqCNYaDHpTT2Z27jlvaD3pEJdCQ6FUlzCoqnHb2T4m2TyUAOI5BxyJ22AjBbNeA3zppBNWBW0DpmbiBwq3Ems2D6HGzLNwDpIE-UUan_DEztFOBnTou2uGjeSlRaFy_o5siH6WE3aJl9xxySDLkasfBu7fUiM3xRAV_Z5QtCbRfLHORl_k7JMPDkaFGkshYaNWZu2XI3Fvj5DA_80OKrmS_UqfZ4jCPb9Jkg6G3ecQwL7zXwoRmFd5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر ماهواره‌ای از نتیجۀ حملات اخیر ایران به پایگاه‌های آمریکا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/449915" target="_blank">📅 18:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449914">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZN78lz71nVqEbLU65VkM7gZCdPx4wEwHTxwh-sHZl-J1ogWIZGxOxx4DU7f_dY6YdwnOr4UTxZcbL4XAVyb3fcGMrRUKltTC1rcEbL-ZYS5PIR8QKcBKu-1S32aE9Rm734CEuswsFvhD1sX60jcS4r5GdL9diRFHY0S2y9WM7N2CjJRERrgSj4pHUd_sWPqqeJwfKvmw67v1DC7ELawXjSmjeTCOS-qno241TvugpYNZPiumCdP6AXV2k2aBAoGbq1djChOVJxQP3KSpyWDq1mtRkDio4dxwW8zY5EDinT379qKdhNoA_DQ3mte-jiqM36qNDgY4hQWauYSpYB_CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز خاموشی‌های پراکنده در پایتخت از فردا
🔹
شرکت برق تهران: با توجه به افزایش شدید دمای هوا و رشد قابل‌توجه بار مصرفی در پایتخت، محدودیت‌های برقی و خاموشی‌های پراکنده در تهران از تاریخ ۲۴ تیرماه آغاز می‌شود.
🔹
این محدودیت‌ها در راستای حفظ و کنترل پایداری شبکه شهر تهران اعمال خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/449914" target="_blank">📅 17:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449913">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nff5cB7cNSq1H3i_c-jnc7ajanyXRV2r8sliI3-fiaNalCpIlN8GYUhRPuBy9EHLV766SThAH_ZM-S_15sQ81VUeZf_MfGncAgStBVa8Qo2efk4xmvcvSu9hefIdbzUofdwK-bzyvInsvn7hj_oxi2C-MX8u3WqHNC_zRLghk7TWgKir_NV3U-idRWnYB3t9AQNQRLbxYjbmHfnmFFOIw_q_VhS9-RofG3-GNwgVDrT7iVmvc6YjBzHUfMe7U2x6sBGJVGL_RkrlvDsz6IctswIOGhqALtc2IEKXje5EHA9QHbdPbmW9pUrAu1d2xM44kuSMgKBCriRsA9FyZ7d1xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امکان تغییر محل آزمون پزشکی داوطلبان اهواز، بوشهر و بندرعباس
🔹
وزارت بهداشت: داوطلبان حوزه‌های امتحانی اهواز، بوشهر و بندرعباس در صورت تمایل می‌توانند از ساعت ۱۴ روز سه‌شنبه ۲۳ تیرماه ۱۴۰۵ تا ساعت ۱۰ صبح روز چهارشنبه ۲۴ تیرماه، حوزه امتحانی خود را صرفا به شرحی که در ادامه آمده است تغییر دهند:
🔸
حوزه اهواز به لرستان
🔸
حوزه بوشهر به شیراز
🔸
حوزه بندرعباس به کرمان
🔹
آزمون فوق در حوزه‌های اهواز، بوشهر و بندرعباس همچنان برگزار خواهد شد و  این مهلت قابل تمدید نیست.
عکس: محسن بخشنده
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/449913" target="_blank">📅 17:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449912">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac3c16066f.mp4?token=R3WU7-ZNPCQZucvpXpKr1OFWJxmPTLwJhkaIeSDe7W1Ydk8M0J-OH1_RTcJM4t4zYhUJZS4FLJBWvNwMWmj4OJB1u1rV1KRGcFaiD4XYeh3kRxuO20ApDa217dKNLjZ0wsfJ3n6fS6L8MQg5oe0_OkHQPa5nc9mmNiXEk0bHNGWVtVYDI1fzf2NPX6C4zNHHWN_mWQnK_Llx3Uas3df7CJ4cW0fyW5XfthPhw_Moc16S9Jp_ug3svQG4qnGf_3VBxqOjeuvtGeS9kvfJfbCWf1Dj-0OB1sL2H3EUsZLfQOWWxMs8NYa61DgGqmbwQsdC5RvylrVuznkI75dmWPD_GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac3c16066f.mp4?token=R3WU7-ZNPCQZucvpXpKr1OFWJxmPTLwJhkaIeSDe7W1Ydk8M0J-OH1_RTcJM4t4zYhUJZS4FLJBWvNwMWmj4OJB1u1rV1KRGcFaiD4XYeh3kRxuO20ApDa217dKNLjZ0wsfJ3n6fS6L8MQg5oe0_OkHQPa5nc9mmNiXEk0bHNGWVtVYDI1fzf2NPX6C4zNHHWN_mWQnK_Llx3Uas3df7CJ4cW0fyW5XfthPhw_Moc16S9Jp_ug3svQG4qnGf_3VBxqOjeuvtGeS9kvfJfbCWf1Dj-0OB1sL2H3EUsZLfQOWWxMs8NYa61DgGqmbwQsdC5RvylrVuznkI75dmWPD_GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور سفرای خارجی در بزرگداشت رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/449912" target="_blank">📅 17:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449910">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b01eac716.mp4?token=OrQfOjtEoBm5Ecqn2limKrboN0xjWxry37KUj0QvT8U99n_D5_In-gTJJ3ihpPW2p-eulfsm7RAa0sDCOKkOEVnGo9gD_0D17KRokdnVFsGTsmMeZ8G6Ac3V_Fl5rCvBft02WlaE3H7l1hcvE4bCpr-5M0Bw7JP0B8fnGy3zQhtV8JwYSsRSdIJeuprUn2hPpP-p7b5odXPq8V47lv25JO00KohzbIjuL3PUCFNTRdpSzlY4GbrMruAsBT4UQTZRDNCwJ4k8a0nmUcaVLtP--DbKXihyRyUM2ZzsUZTlp5aXMuO0ASn4RRHGvtGf2EnRxNp5_ORAgKZR2E97SGPmBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b01eac716.mp4?token=OrQfOjtEoBm5Ecqn2limKrboN0xjWxry37KUj0QvT8U99n_D5_In-gTJJ3ihpPW2p-eulfsm7RAa0sDCOKkOEVnGo9gD_0D17KRokdnVFsGTsmMeZ8G6Ac3V_Fl5rCvBft02WlaE3H7l1hcvE4bCpr-5M0Bw7JP0B8fnGy3zQhtV8JwYSsRSdIJeuprUn2hPpP-p7b5odXPq8V47lv25JO00KohzbIjuL3PUCFNTRdpSzlY4GbrMruAsBT4UQTZRDNCwJ4k8a0nmUcaVLtP--DbKXihyRyUM2ZzsUZTlp5aXMuO0ASn4RRHGvtGf2EnRxNp5_ORAgKZR2E97SGPmBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انهدام یک پهپاد متخاصم در بندرعباس
🔹
روابط‌عمومی ارتش: بامداد امروز یک فروند پهپاد متخاصم آمریکایی توسط سامانه‌های پدافندی نیروی دریایی ارتش منهدم شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/449910" target="_blank">📅 17:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449909">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80299360d7.mp4?token=e_8FgCMfjqHUcxroD0-5EujY542lWw9MIrZwp8tmDbl6cpcAvG0etFUzCHn4oBVhcsdyeIhPaOUPyUsxwki_RCGLffJwzQQS3t3Lrty4b7tUqi7aPosu6Sl-Cous4UW2m5XyEaHD5mULqt34-H_9dY0931fIeabMa7yu06TUX7q9KClBaaY4OuO_sayu1isNf3VxDj3vl9rsQJiuwlfdKSsrT45JPv5hYq8ltJyPqSOWD3MkGLJ9js3oFG0LUFLZzu1W0qhzfykAVoKM9PQOIslzQYLD7dz-nqprwOy4EJnygBSliUluDc71R4t9Lzjfbxb_r2USMEHy_XV0eLvPFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80299360d7.mp4?token=e_8FgCMfjqHUcxroD0-5EujY542lWw9MIrZwp8tmDbl6cpcAvG0etFUzCHn4oBVhcsdyeIhPaOUPyUsxwki_RCGLffJwzQQS3t3Lrty4b7tUqi7aPosu6Sl-Cous4UW2m5XyEaHD5mULqt34-H_9dY0931fIeabMa7yu06TUX7q9KClBaaY4OuO_sayu1isNf3VxDj3vl9rsQJiuwlfdKSsrT45JPv5hYq8ltJyPqSOWD3MkGLJ9js3oFG0LUFLZzu1W0qhzfykAVoKM9PQOIslzQYLD7dz-nqprwOy4EJnygBSliUluDc71R4t9Lzjfbxb_r2USMEHy_XV0eLvPFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◾️
امر فقط امر سیدمجتبی
◾️
حکم فقط حکم سیدمجتبی
🔹
شعار مردم در مراسم بزرگداشت رهبر شهید انقلاب @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/449909" target="_blank">📅 17:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449907">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aaa78ea64.mp4?token=k5omkebHomohzGpA82Rm0J5H5wGYsyc6ZxvHMqR7wktHN0RLBrVAX3svp1vSI0TmNN4T6vbelpO3LD6fXJFbWk7tlWFQHeGeGcZh0PWgPIO6SNdajSkW4w_F16XmIU2O2NpsY0JRHRqQPUaaBvKgk5q8qmGFaNab2jxRnLlByYCy4XkVIyrWT1mkGirGL1bwfoWWqFpgsJPQF88xKqCButgwdiAZ8qYOnDPhfeopE0mslFRw5_vrZU6ltRuJPfcCRA9c9MWCX_yg44iDmntXMV1Pxe4Nyxu3s2eEZ8JKz_Ka28fCo-8nsAVn5YTUXn1IyXz7r5rdBNFq9m0YOZy5Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aaa78ea64.mp4?token=k5omkebHomohzGpA82Rm0J5H5wGYsyc6ZxvHMqR7wktHN0RLBrVAX3svp1vSI0TmNN4T6vbelpO3LD6fXJFbWk7tlWFQHeGeGcZh0PWgPIO6SNdajSkW4w_F16XmIU2O2NpsY0JRHRqQPUaaBvKgk5q8qmGFaNab2jxRnLlByYCy4XkVIyrWT1mkGirGL1bwfoWWqFpgsJPQF88xKqCButgwdiAZ8qYOnDPhfeopE0mslFRw5_vrZU6ltRuJPfcCRA9c9MWCX_yg44iDmntXMV1Pxe4Nyxu3s2eEZ8JKz_Ka28fCo-8nsAVn5YTUXn1IyXz7r5rdBNFq9m0YOZy5Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◾️
خدا گویا که نازل کرده بود از عرش نامت را
◾️
که پرچم‌ها چنین سر داده بودند انتقامت را  شعرخوانی حاج محمدرضا بذری در مراسم بزرگداشت امام مجاهد شهید در مصلای امام خمینی(ره) تهران @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/449907" target="_blank">📅 17:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449906">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb8b782961.mp4?token=mPk8-25SrVMf0EflgCSXX5lSESeYpFD-Wt4hTBU3EIaPvzCkNKUwyoyAnIH-5YY3mVYIxr8LylOtzlbLflZ1YEhogjjoxXyULtA3b1SpaquLU-Zu0AlJKS8ncSIf5QAMXQxQ6GqB-p29-hVSuZZz4re7AbbI6wPli0K7bvoeJ-NbHDH4ah6Wordtnf7FZNfNWElvVID9ZGcmJs6ZGsrhJTTGDnyWyHnssC7zegGuEEfjbAmTGho6qWv3E01NUaEUkB7_pfgFOD8rmrxgWzlilNL9NOSf6RhIcusLvhQ1tmvYL7v2xCwEdH6pB7syO3J9pk-l3CUNteJvf38AUk5TpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb8b782961.mp4?token=mPk8-25SrVMf0EflgCSXX5lSESeYpFD-Wt4hTBU3EIaPvzCkNKUwyoyAnIH-5YY3mVYIxr8LylOtzlbLflZ1YEhogjjoxXyULtA3b1SpaquLU-Zu0AlJKS8ncSIf5QAMXQxQ6GqB-p29-hVSuZZz4re7AbbI6wPli0K7bvoeJ-NbHDH4ah6Wordtnf7FZNfNWElvVID9ZGcmJs6ZGsrhJTTGDnyWyHnssC7zegGuEEfjbAmTGho6qWv3E01NUaEUkB7_pfgFOD8rmrxgWzlilNL9NOSf6RhIcusLvhQ1tmvYL7v2xCwEdH6pB7syO3J9pk-l3CUNteJvf38AUk5TpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور رئیس قوه‌قضائیه در مراسم بزرگداشت رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/449906" target="_blank">📅 17:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449904">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e854c34cb.mp4?token=EQm3dC_3tO2DSiBqbtvxRx4R_EMIb1fOCalT6aMcSOA_FzR2_2iBWvIjO6Ti4Yt1a5wp9jxSK7LkadJXvpHG8gAZiAhlPBp55emiZTrtj2ug7hKL0eI1H0dD6numptyo7TfZSuZ-feTiHjl1XX3bQjCuzIEY0dBdunedYtcYyFhH-qHDp1FsHKdsuYBwMSDD3SvQUbwWv2Wxkv05naDTD96S_-j9RSGJQxODqQSPyotw-7yU9y2XYBk6R8EPNj5ot-a5yHzZe9sz5ZP7SVyJBo83goIxFxe_zQDl9GgXErAOrGYM-XwzCE-Sye0Udu5_P5B8sfDJe_lc46x2fh2P1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e854c34cb.mp4?token=EQm3dC_3tO2DSiBqbtvxRx4R_EMIb1fOCalT6aMcSOA_FzR2_2iBWvIjO6Ti4Yt1a5wp9jxSK7LkadJXvpHG8gAZiAhlPBp55emiZTrtj2ug7hKL0eI1H0dD6numptyo7TfZSuZ-feTiHjl1XX3bQjCuzIEY0dBdunedYtcYyFhH-qHDp1FsHKdsuYBwMSDD3SvQUbwWv2Wxkv05naDTD96S_-j9RSGJQxODqQSPyotw-7yU9y2XYBk6R8EPNj5ot-a5yHzZe9sz5ZP7SVyJBo83goIxFxe_zQDl9GgXErAOrGYM-XwzCE-Sye0Udu5_P5B8sfDJe_lc46x2fh2P1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
مراسم بزرگداشت رهبر شهید انقلاب در مصلای امام خمینی(ره)  عکس: زینب حمزه‌لویی @Farsna</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/449904" target="_blank">📅 17:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449899">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IwaKNfjb2gBFowooCqLsYqf8zaO_Ns_ls-1r2oTaL5DzFXIFVoa6Y4y0hWEbgR397WMKUzKMEs_uCPoc4ziema8qFK4ICAK5mq4L9u5ySKKiXquN5SPNUitPb2zdDOWc2zVPMu9NbYJV1ThJXfxFa3pzj3T2baoxw1Gd5_rMBqXuaCqTrxaC5kHGPqO3lWRqclUslMwnT47sValD7EyrRU_0kFWtCpNZL8dkg4iqsOH7BNno4dBPddnE9ycMWymCMtpzzWq5qc8Tkp4jdi8JqkpHpCL-RTZ813J2vh5F-idr3cF8tPApdLuYXiemSVwYC3EKLsMi3AQsrbSZYvdw6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RRMJV-wAxpbSkDmG2N1zj9dtCzLL6UosBTv31x_zlnmjHfzyXkkWTzREKNSJ6OE2-gfBYm6KNonk6svPm0pi9yN0S0ljdwcy4OiWmprrQudH_C1S8101y6yuJUINvD1T906MsDUEZyIUlxZ-WWVjqqLagSHNwxM6bfJ-QxgOSckySWs1M5zisQ__wCUvhBLmIHT0INCSO7lWo-fHm1q4qbHOfYN3XhT64wT7IQYrB5S45EHuYBzc4aNHT6NqT8R4fXJDycZeh1Y42V0qyjZ3ty0tuG11aBKBSJ1zwXD_ci4JBRta5SCUs7192ai7Ih5frDavUS0iBmhQ3UQ4wr51Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V51Exn4t8bibBML11g8HL5UnkeZtpo9beMsvILy8hb6WkpffUIDzhZf1V_Djq1tlsTuCKgTjadi17GMrQoEnwnwrxQmj8672kRsA64EvG4pQNVM-eAEK0sm3pg-6UjNP0tkTN0_53TuaLqjdKf8qmxRaC5A-o2v2_bLjSUK76_FjE7LpePNxiI1EKHQw3DMGgnrn-2RHAhkqRsjF9FAzZLjFetGARoJM3MJPOKoyru-_Uti4ISwNeapNKgYq78OB7JHXPfp94R1A0BBaKFOWPeog6TIzKzg0Q-InDC2BfiNfsO7piGIj6w5r_aNLzCOPS_GTWOnpZfAvx0-kU6hIWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/buw4A8I7ACdPlszcXL1xrslDUVjFjGKSawPnilzK2DnFDdZ4U6VwLhwYqflFFgoqYq_lG2gHovdqNSBHm-k1Q_WqfMsk2zfo0uka31ZI1YLZtu__0JUSpeny6owmijvnl5ZyCTb3f_lP-zvKNHfMhBBpnH0nsnBwU5zSAOgQGg_43bgymVF-ETt6aKay8ryzEm3UalYSzwJGvpW4ZiwnZEYbWySB0hhtztbyJ3EZg604Wj3fiZPrRGtL_P6J4rfPe_r8ACUEx9S3Z_UwMkavwyuDxOWO43Phf2bDhbXpYv2uqwgVre1LGWxph525DTr2mOIN6Wzh_0tanjclmwe2aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AL2KJKWoLlY63tP3lTyMMDsoZic7z_CcU9M1bIPsiueB8uIywqGT_641MAaIwDfSWt4P8snS3AFpYlwiQhwD1DPCJBoqZBB4ZdvkovMAP2TKzMASSrE2hPyg-w1jMLf1xoEl6aETf28_DlN88nrRjcneuC4xwz7KelUB0GgOY_jgxXrGidpq0_BwI7QJw3kbiNd0b57lDZwqKdCnJJ5m0R4WL9lMGWh_fGLsA5LQtDGSoTPZxhNdD8IVDcg2C15alEECgPANs7AEsBClf3BSIjwaTm4kJzwHyZmsMIxrS-z2XmQO-fyB23pKFytAhiOEoXn6VE40-EZAffE35L_rCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
آغاز مراسم بزرگداشت امام مجاهد شهید در مصلای امام خمینی(ره) تهران  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/449899" target="_blank">📅 17:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449898">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88c7a6eef6.mp4?token=UzDkpI5SS6Fo98rfNARZMfvM11WpN_zopoiADLtz8fhiJWY8cfV1ROrLOC8ba4i__OV4s4OvmpGAfgDS7I5de1-xu2Xyg9wwBNfoOzlMKhox0eaPQJrwOzlNEo4dkhEd8q7gCBLVKpAkRc1-HFA8LdibvOcXWamLKsmAXOYKJW4h-GxL_j5tOVSb7LXdC2gHwIzN_TmWGamGIro7GggVRFOmqyAkztWJlciQ6IWLRyKMrhbYLIVH0T0DECLaE7kAulaglrYOlG5P_7VEF0Uvm8Ua5AFpQeS5bGPebi6fPOsoEegYZKx-0HveeeY-NY3Kej0YX-lnP2ywQw5Ppa7gbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88c7a6eef6.mp4?token=UzDkpI5SS6Fo98rfNARZMfvM11WpN_zopoiADLtz8fhiJWY8cfV1ROrLOC8ba4i__OV4s4OvmpGAfgDS7I5de1-xu2Xyg9wwBNfoOzlMKhox0eaPQJrwOzlNEo4dkhEd8q7gCBLVKpAkRc1-HFA8LdibvOcXWamLKsmAXOYKJW4h-GxL_j5tOVSb7LXdC2gHwIzN_TmWGamGIro7GggVRFOmqyAkztWJlciQ6IWLRyKMrhbYLIVH0T0DECLaE7kAulaglrYOlG5P_7VEF0Uvm8Ua5AFpQeS5bGPebi6fPOsoEegYZKx-0HveeeY-NY3Kej0YX-lnP2ywQw5Ppa7gbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز مراسم بزرگداشت امام مجاهد شهید در مصلای امام خمینی(ره) تهران
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/449898" target="_blank">📅 17:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449897">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a8ddd9019.mp4?token=HwTQCxqkogiADpZXkRF1KAhACbfa1nJMoJ3LxE5w51_PiWsHUlovAi9GLvHIhggRu2mu1DracV0AEx6BsU_uxlBRB0LXt8jSK32FAurgENrbxEe1RPWxEnAsfe03QMzGMl-bjOmx_pBEcOLJcdGRwZ2vY8HRk-ljYpSd5o5cQ0-1SR62jbnrwU4sJ78yyYzyNfeaO7fddT7Ey2byVMF-eLXAElhPItCHfHHdKfrmX0pTRGKoL5EhallDjSqyj7pQvOXhhjGQEADlSORXOyKkgKcB2uA0iknOaDwkNyfm0U9YbulCL9uFA734tRVpSUEbJaTX7RGhrVwFDASwwSUW3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a8ddd9019.mp4?token=HwTQCxqkogiADpZXkRF1KAhACbfa1nJMoJ3LxE5w51_PiWsHUlovAi9GLvHIhggRu2mu1DracV0AEx6BsU_uxlBRB0LXt8jSK32FAurgENrbxEe1RPWxEnAsfe03QMzGMl-bjOmx_pBEcOLJcdGRwZ2vY8HRk-ljYpSd5o5cQ0-1SR62jbnrwU4sJ78yyYzyNfeaO7fddT7Ey2byVMF-eLXAElhPItCHfHHdKfrmX0pTRGKoL5EhallDjSqyj7pQvOXhhjGQEADlSORXOyKkgKcB2uA0iknOaDwkNyfm0U9YbulCL9uFA734tRVpSUEbJaTX7RGhrVwFDASwwSUW3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، تحلیلگر حوزۀ مقاومت: استراتژی چشم در برابر چشم دشمن را متوقف نخواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/449897" target="_blank">📅 17:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449896">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e6d094f3.mp4?token=s-QSh9IE27DUeIGoc4vhKHFwb0YyAxz-5VeqcMgSc8wVvuLcoGascjO8skWRvJlb6Ga-x6KLT6BvKwIjywhhL88xurC_4LzlrBpfKSVGHMUZz8T0gA8JdtXNFtDcrOOO2d6P0RsQ-cR_1Re1d85VHRQ0fobPJSQ8nPWEaxtqmenNRY8rXLrJPAxZMvwtVOdRBMKQTFfeMjC5Pad2vncjL2-h2NCKAdcpmo_hLoheKWGnpPvlZvNupVmJP1h19Siqp11GyUgSkEgBLz854B4xigxMMB-MzotBc6pEQPB5kJipxtIuvr7t-YhgQ6IssSiGuNDz8U7jkQy1KZ9CpZAViw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e6d094f3.mp4?token=s-QSh9IE27DUeIGoc4vhKHFwb0YyAxz-5VeqcMgSc8wVvuLcoGascjO8skWRvJlb6Ga-x6KLT6BvKwIjywhhL88xurC_4LzlrBpfKSVGHMUZz8T0gA8JdtXNFtDcrOOO2d6P0RsQ-cR_1Re1d85VHRQ0fobPJSQ8nPWEaxtqmenNRY8rXLrJPAxZMvwtVOdRBMKQTFfeMjC5Pad2vncjL2-h2NCKAdcpmo_hLoheKWGnpPvlZvNupVmJP1h19Siqp11GyUgSkEgBLz854B4xigxMMB-MzotBc6pEQPB5kJipxtIuvr7t-YhgQ6IssSiGuNDz8U7jkQy1KZ9CpZAViw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم جام جهانی را برای کدام تیم می‌خواهند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/449896" target="_blank">📅 17:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449895">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g50aXsNBW99jiuQ6wR33p-nvdL71V-ibkqJp8bCIZ8OMI7-rKopWQwytRcGM0NQLPgF-WoKNLuQtVB37sABcsfgB2zyuBm0q6MmLe-e3u7ksGubrGRGp7Sduvz0CLpq3hBtE2GSxIM1ldiFAEB3SGLaOQHd4ceFzrVjUsiTt1cjARN6JzbjglmIm8EMQ0HA8H8MnTeMTyegE8x1HB3gD8-_ZTRYvTTAJEYsbv7eaS8KOpSGOsgsh-mhppEl5Bm0e9TIIlyXuHYkbIa97moBeTtrCqr7Ob57xvYru4G5tZ-7DwAipUNc5E_LhzyCocmdWVEevR-RYL9PPwrotSJ4XCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی ایلان ماسک، نفس همسایه‌ها را می‌گیرد
🔹
رویترز: پروژهٔ بزرگ هوش مصنوعی xAI متعلق به ایلان ماسک با راه‌اندازی ده‌ها توربین گازی بدون مجوز، بیشترین آلودگی هوا را به محله‌های عمدتاً سیاه‌پوست اطراف خود تحمیل کرده است.
🔹
تحلیل رویترز نشان می‌دهد میزان انتشار احتمالی اکسیدهای نیتروژن از این توربین‌ها می‌تواند سالانه به حدود ۲۵۰۰ تن برسد؛ رقمی هم‌تراز با آلاینده‌ترین نیروگاه‌های گازی آمریکا.
🔹
بخش عمده این آلودگی نیز متوجه محله‌های عمدتاً سیاه‌پوست در مرز ایالت‌های تنسی و می‌سی‌سی‌پی است؛ مناطقی که پیش‌تر نیز نرخ بالایی از بیماری‌های تنفسی داشته‌اند.
🔹
انجمن ملی پیشرفت رنگین‌پوستان و مرکز حقوق محیط‌زیست جنوب آمریکا از xAI به اتهام نقض قانون هوای پاک شکایت کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/449895" target="_blank">📅 16:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449893">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‌ انتخابات ریاست کمیسیون امنیت ملی مجدد برگزار می‌شود
🔹
یکی از اعضای کمیسیون امنیت ملی مجلس در گفت‌وگو با فارس: انتخابات هیئت‌رئیسه کمیسیون امنیت ملی، در هاله‌ای از ابهام قرار دارد. قرار شد امروز عصر انتخابات در سطح ریاست، مجدد برگزار شود.
🔸
علاءالدین بروجردی…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/449893" target="_blank">📅 16:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449892">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibyHgmwjie-ahOiGmAO_cetrSWDtONwe0BtJAqES1cwvViQ747jZD8jv8E9cMNox2puoxOS7jNXuzGB1hhog4TGDcaoYAett1F7AOuj59Z2wQ5B9XR9odjyTENc9MXAHni7dXU5VvFrkMwq6DlKiAvgmmCGPZCZWAm-X2EMpyKw1FO2IMFMqONseemwzdCitIcTzqL1btFGY2K7iCrXZHv4UXzwwjR0Y0MtuQTX1yusT-Odih2a_xy1PpPtvuhAeXT-aC9k8wFRQcxKTuC_R7L9r3rOMjUL19aFCxloaCNyO4T4iaXmdvHx2SuwijEdZPbT73AmAkRkypdc7-kMo5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیۀ نمایندگان مجلس در ضرورت پیگیری انتقام و اعلام پایان تفاهم اسلام‌آباد
🔹
حدود ۱۸۰ نفر از نمایندگان مجلس با صدور بیانیه‌ای، بر ضرورت پیگیری انتقام، پایان‌یافتن تفاهم با آمریکا، تشکیل کمیسیون ویژه بررسی مذاکرات، تصویب قانون مدیریت تنگه هرمز و حمایت همه‌جانبه از نیروهای مسلح تأکید کردند.
در بخش‌هایی از این بیانیه آمده:
🔹
در سنگر مجلس عهد می‌بندیم در مسیر خون‌‎خواهی و انتقام، لحظه‌ای از تلاش، برنامه‌ریزی و اقدامات عملی غفلت نکنیم.
🔹
از هیئت‌رئیسه مجلس می‌خواهیم فوراً کمیسیون ویژه بررسی مذاکرات و تفاهمات و نظارت بر تحقق شروط رهبر انقلاب را تشکیل دهد.
🔹
مجلس ایجاد تمهیدات قانونی از جمله ارتقای دکترین دفاعی و تصویب قانون مدیریت و حکمرانی تنگه هرمز را در دستور کار قرار خواهد داد.
🔹
اکنون که رئیس‌جمهور آمریکا این تفاهم را پایان‌یافته اعلام کرده، انتظار می‌رود سران قوا مواضع قاطع و انقلابی خود را در این زمینه اعلام کنند.
🔹
از عملکرد نیروهای مسلح، به‌ویژه در اعمال حق حاکمیت ایران بر تنگه هرمز، حمایت قاطع می‌کنیم و از هیچ پشتیبانی برای تأمین نیازهای آنان دریغ نخواهیم کرد.
🔗
متن کامل بیانیه را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/449892" target="_blank">📅 16:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449891">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BycNr6NNtPlmVTZCqDuFQuoVQSO0NHu5lRuRBZxISWj5vjyo-1HWAVgPdds41TwViPbMomRGuaEMQinpUrscIZXI0pmOYWT4NmhZkidNQw6manEoI_6NUu-CKZKeP3hlk1_1NSR6rzu_XCL-kQXi60pB8x73663Ai9JR_Mf9_bxWg83Ea4A9DZ6nzmGvQa52ZPuhvPp6sU_X4W_7SSj-VGgYBhBa_gthJHaZp5uQbMEu15PLDuVaoZn5S_jaYiX50TMn4fTrmJDz4LWSOfEZuYTQ49sEQlCghAnBBY_Qq0gbae00TJqQxZfKnvvqgsjAxAnfm7GPorzfEXkx05yNpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریستوفر نولان دلیل نداشتن گوشی هوشمند را فاش کرد
🔹
دیلی‌تلگراف: کریستوفر نولان، کارگردان برنده اسکار، در گفت‌وگویی تازه توضیح داد که نداشتن گوشی هوشمند به معنای مخالفت با فناوری نیست.
🔹
او معتقد است این انتخاب را برای محافظت از زمان‌هایی انجام داده که می‌تواند بدون حواس‌پرتی روی ایده‌هایش تمرکز کند و به پروژه‌های سینمایی‌اش فکر کند.
🔹
این فیلم‌ساز می‌گوید بهترین ایده‌هایش در لحظات کوتاه انتظار، زمانی که دیگران سرگرم تلفن همراه هستند، شکل می‌گیرد و همین زمان‌ها مسیر بعدی کارهایش را مشخص می‌کنند.
🔹
نولان می‌گوید: «اگر گوشی هوشمند داشتم، به‌طرز وحشتناکی به آن معتاد می‌شدم و تمام وقتم صرف جست‌وجوی بی‌وقفه اطلاعات می‌شد.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/449891" target="_blank">📅 16:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449890">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بازداشت ۳ گردانندۀ کانال انتشار تصاویر خصوصی در لرستان
🔹
دادستان لرستان: ۳ نفر از گردانندگان اصلی کانال‌های منتشرکنندۀ تصاویر خصوصی مردم، در کمتر از ۴۸ ساعت پس از وصول گزارش و تشکیل پرونده در دادسرای خرم‌آباد شناسایی و دستگیر شدند.
🔹
ابعاد این پرونده گسترده است و تاکنون بیش از ۲۰۰ شکایت در این خصوص در دادسرای لرستان ثبت شده است.
🔹
از تمامی افرادی که تصاویر یا حریم خصوصی آن‌ها مورد سوءاستفاده قرار گرفته تقاضا می‌شود جهت طرح شکایت و پیگیری قضایی به دادسرای لرستان مراجعه کنند. تأکید می‌شود هویت تمامی شاکیان نزد دستگاه قضا کاملاً محرمانه باقی خواهد ماند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/449890" target="_blank">📅 16:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449889">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vG6Iqw4aRup2YZdfpNbxPLqhg28_X_b3VlMMROjWEwHFDAaMhqpO9t5bFWpYCRna5GQypYJlvbLVPgMsumODWNz1TWQdt5TQFGnKFH6p-T93pZc7A8pkFWoFVs2aWVnuG0WU7ufOPrEhcEaIjPga4lGwXdxX5aHf4BMaPQZhMVv_5Y4cj4e6nE-5-v3vEjY8IW0s_BXCWEcKGYvFbt_DEjFkdrI0NtuZ4hZO1atzRD3qLL9asajHItRITis28Nnat-__syNHdNQrTpah_15NUuZMARYZscbW6Z7Ph3-aLilta0GFvPutJJ_1hwMTOzU6QHByO42vypvLoPCoCKSwkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ شهید در حملهٔ اسرائیل به یک مرکز پلیس در نوار غزه
🔹
رژیم صهیونسیتی یک مقر پلیس را در شمال نوار غزه هدف حملهٔ پهپادی قرار داد که در این حمله ۷ نفر به شهادت رسیدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/449889" target="_blank">📅 16:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449883">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eba-jlDd18Vd0RvhGXIrTuedrcpgaxAVCr-XD_GGg3v8D2vAtpsqrZX1FTnh7h0H2-Yww3_vBDWKCRKCHbqszbxncpclF5XThzteqi0F2XdSGF2qzTe997XxuJCicWwc6J2vtN1LnhB2qolWOfZknfMv1n1nb02YKDs5NS9MHMhd0lpG5Q_vnb7yMdE-BAeqs3gNAMI2iHH6rtXAFNZc6OvMTAQPtjNNzL8flenEYytaAvisjsJA_4lJ-ZSEesjrz3VzoDfm61mOYw9EwMiZ1v927y1VyyHSw0b5meK6Tof94nE3R54PqH-M0QnAE1Fy9kC3rnsdryUS5EVz5wV3-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZMVfkXP0KN1prVJo5A7_VHcBGhjOgW0H4NsUGFHZXgyGGllYCODRWekTZkRUrmYclvHuS8hsFphRzUlUsYepYs66QWN9bUzVmAvhwrvqG-zWgAYxlgkxqgarQbvIr0Mj-x2-43DRmcp8iz0i1K1f2UUzwgUzgGkdNYVUoAKrpF2DQL8nyPPR_aEbIz2ipUdfyxZLPsGlRwD0RCoNDEQHRH58wH9hGWk1HQcPTiMSu4JkMZmV7gIQIih7fY9L2AJq4Kks0S6apTZAZP8wdqNKx74ldGeSXUnzJWULj1skiAoHkUH91PV1ANoiWt2vy-EHqVgPpzstQW6hjY0eyhfBMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T7NwdfIQlupul3RXa6RBBNs4QCo3Q1-2FAogKj_gI8bHbPihknCWqzu1gkDELJqwyi383OC8_FhrhWa93Ix6Coz7AP0N6umjG1DpDW8mGtSg5E7pHlgbEKFyFVZxqam_F2ATw1a04ZNU26aReF54oIOfTWOG0smJfREREf-tYCjTBO8uRP0Uk000LywuU0vXfBIgvjCkv37vK1YbA5Xn_xQNa7Vtw0YDZdLJi5FHw6_xSeOXMPN_WkVn9-fJtyHDXrQLFw06bp_gOYooj1O9P71qiC4RHAtwFpdW5NPSyWuVe0AFCcDks7cXoE79I3Girx9MlGdJOVrAWKau6IsstQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hOP3PmF_6sEpDq4BTilHe3ddFRWmu1rzPRurfi3uYKjc_oNVQ1TEq5x9q55co5MRnjUOeqQNyxu6c4jNlpH5Iovan8sUVh53rK1vr389QQcZlbKRS_skv4Hp1t5xFG6I3ML58-PmGRRJU8uv5U2f1iCJp3iK36DmFaN97blwsbB4oVphlqUCnVeq_6yGDsaFwT5uY5O1c-JCnYuYgtp6yPMzv78TceWWoh5qU6Og9FiWacYojLY-NS-8olHtfLxSL_yd4J2UEqkFvAtFlah00lvSQ4axY4zRE85ZKTm6Ysts9e1mLK0N6jjnLPzkOR3YKABpObEL7n5TYM7_LdsaWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qmj7BysSPHF-D15h7EgcAxw775Ne4m1SR1YK_KZova1Npjm19SLwEhj5RyFBrVm5EM5_KZtHTl-9m3_5Vm2WNoA3khN_9SEbNBqQOD9ZvIbDvrpL2hbPIcxKhJOUbhYeRxh6Fu7NWF4WelZvf3AiWFI1205DCrxSr6_fa_DVoQkOWCw99ZPIrCFmaRdoy3ksVNADe_NDxVsgqiSYznilvfYKrYciTUGWUGwgeIPreFlKa78iIuHYA0InNiQG4_b44dP_WJOPBqyb-exnjPKlZn7IhPf8GMda2Iv-yrLrC7YTEOVlrjetrl4YncqN3_4kseMwH6ny0USaSBRXSL8QFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kNx_aYxMQQISKQufCn22emvKKHwEtXacPCxOM6d229sgAPb5tJn6V1VsrhPqqYqRVKQo8PkqzMCFHdIUgcQfWmEQLbnW79dI-yHTsM4Q7ZaNX0iTF9duj_HGbUyYXI9Kx1u7Qaw8wGZZ-1k2ZBUm7UFq1eO6aC8jNTNahtja_jU2ObxoPLpjStGpUrKuFGnMqO_ka_8UsjvMrhx5AHaar4JzPRCAVWmTCQ-ZmpunwyyflKBn88fiL9COQrnaTTIC-T1s9PDDprKmLu94ZjYBaV1nSaQj10p13-HaDX7FLu3jHden3hQH_NUDbS9YsmHYfEpryfEFfm6I1Gj45yY5PQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تجلی وحدت اسلامی با حضور علمای شیعه و سنی در آذربایجان غربی
عکاس:
محمد مهدی فتحی
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/449883" target="_blank">📅 16:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449882">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‌ جزئیات حملهٔ دقایقی قبل ارتش تروریستی آمریکا به بوشهر
🔹
معاون امنیتی استاندار بوشهر: ظهر امروز ۴ نقطه از بوشهر هدف اصابت پرتابه‌های دشمن قرار گرفت؛ ابعاد و ارزیابی خسارات احتمالی این حمله درحال بررسی است.
🔹
براساس ارزیابی‌های اولیه، تاکنون هیچ‌گونه تلفات…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/449882" target="_blank">📅 16:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449877">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pJ03KR3luAySza9B4-PKqRwkTDLH5ngp2yUCs4LI79hxLWHgt1mMjtD-XTRP2e6sLJlKE-z9zhU8t6ngoOO5BMvVKooRNxkmICBrcS8Ba7iZt4CchKGngA3C5CPAyWSSnPvqUu0AWely4ZyS_itsk7bRDy7YSkjRZJaFu--YFtOhFZesR8FywWGz0YjjBVXm_nB4eKuqaA-W2C_FjOnN-iF1bd9oHO4z9mesfVzbaNby6BpoRyx2IzpVRjwGV9YP6y5MSHW7x7MgJiIP-UMY_fVcEeAdxI2EaQ8y7HhgBzLdfcAPJySfvetAsRiNLvN1QrXZ9DWpgTI47f9I3Leylw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DEAqjdVT4EPkyLek0I91K1S7lnhrs6yUC4bKWTkf_GMVL57pe_y5T1RZmwOgsA2Ow-EJZyx8MclucQgM_9je0B3e4et8Bs9ilIIS5wuaLKS95S4mksLTOESFqJ-EWS53Oh88KMUdZzuI026lZYX7ozPmywLpbEnA59y96HBgvLktV81VRuAi1xsaZjIQIaH43lc56__FESyanOqV-DEMu93rQr6nb6vHKyOCg3Ne-J2lpgnvKU91WFQrwDvNd-ULpGcjQcl9wpwXE3goD0bv6qGaKzxzyWFdN1ccQDZbyalSjSt0L6j4KECPfBqPiLwF-Ign7U7GmcQQnWFjgv1QsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KsAsgvZJjIpx2TXdRk2HZ2Krbf1zn_yC-T2c6Q9WtgWhvk4wooPH5GMA2BjDVFRioBw76nzX9LFgFEpadqFIVIAdZ7TwbSrSJ43ZiWOlXprElQ3h_6rjFHlGblx96DV0Aisax4iNdMbhQzy0ru6cP_YF1_v1-WrsOnYdRJQe1Wdo4CwDqNN3hXAB2avFAejBPr8AZ0_vTxOKiInNMhnRQSFLkGcpqUWjfoplIBtFjxZmzAsAoZAAhVTPwy_odtL0gVT4zqru9qx_2aB5JBKJSmxRaD-dwDvCqIkwoGNmyLyMtPDzG7AhEyAPcHtud4AxDAmXFw-DjONVrwxUi3j6UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hKbjCRYeHvxDrT5fPVr0JwouFo7vOzr-Cvh4rXHh3Qhlkcw4Zk7lLYBiGS_oyZ6KM0iIehrnjqCdVuU7ru1rQAyz8aCNyRNkO-njrNE_x3JXcDJsMW2AIkyG73U6HO0Fc4sTHO8JlCTtNsq8AcA1hPzYfKiw8Z6R4x04NuAVfcEM-gJ67MUa0ho5IXh-NsBKFqaHhp3Db4rEIp_BC6Uwkuwrv1TbGYxM99NFu0IuTOl1iEsqe7b2cJ_TAfuAFRukZuHEIYNA11GGmxT1y21plSrlkCkEGyUdvQDjmbe96syxn65wr_H9u7ifmqhmDBC3PNf3VWakEsHWdKIwyM7iog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T2ilu1Ekla05MK1Q0OR9YoFwKUbaX6MPBRk3tVqUZKIHel7BCHpyvPTVruCxWfAtzXSifM-dD4IV-UvNfWkT6CaG55Tfe73fBiSkWRWT5_NDKslyD0mtjaHkcrcfCcdTku6vNVmxN8kb2UoWAb1DOtllR0FV4LrmwmHxLgBKQCC7BpNcPriLnPcURZaCMHC4Mlz4q0d9Mkzwaissk9uzqr5PDx_oikJCQzKJbdMAQ1l31KtW02_QukNMyD6eQq8vy3heoKqQygtQdexCpQCrWBHSjBu7QIVth1m5Fp7gX3wbvHX96__TQY4_OEOwE6EuH3kEiKjat8ETMuz6ESSylg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
نهاد مدیریت آبراه خلیج فارس
:
تا قبل‌از تنش‌آفرینی آمریکا در تنگهٔ هرمز، پس‌از امضای تفاهم‌نامه ۲۰۰ شناور غیرایرانی به‌طور هماهنگ‌شده از این تنگه عبور کردند
.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/449877" target="_blank">📅 16:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449876">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvRjqvGnU5UsmpELY5TmCH9q_r8VC1o_DC_qTuoAWBVtAT1FmtZQS_Ayqt1Q451mi4nGpH3jfpK2cbFV73voWm3HcbvWF_5JCUAIuK6MN6fSm7mb_8WFdbpRSBngHhTqxD_NmbEjejmKgb-sk7wQZ8gU93kH3LE0P20Or-9Gw2xvkdycbFpFschyeI9QaSvkDd_zbbSnaDKnbB0eqpeBZNksMPLaNORW-PqMI7f4_W1XNFYaspNkY4lmK-vCG5knZsgzRR2xeDED2rYHXOsT9Sy7zUfydthF8xbkidD2EqaAW6tmW0B3St4HAcqz6WTXPp3foRreZAXN9Nqun-Znlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاجگردون رئیس کمیسیون برنامه‌وبودجۀ مجلس شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/449876" target="_blank">📅 15:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449875">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97470ef355.mp4?token=Li1Fj5jJ90X9LOUDNFwMzP0Lllim1TWuXwC2VxHnkTwnSg8STW0Oh8rN2e16NhAo8GY0fVLLulgYWwbw_IFosN7HnLtkoTQr0CLdgdsjyvITk58YrQMb8WVQc3R7EPydLXuGqqYMOW_mh3mGngfirL5G6yFkBt5YxpXJvnctCH6C3azZNbsybuahn40Ac-KNkepNaBQrKt0_zrjBORiw0l8ZlMathorArHalu48_Eap4auWmIcXC5NL4lGqeMT7iTqd9rIi07Ou2qJav7pzpeUqwg2ivnVi0vAjxoFW_MxTwCXOuXH_Jz4YrfvDIl1eVUudrRdCOcxo4-wd6AAAIgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97470ef355.mp4?token=Li1Fj5jJ90X9LOUDNFwMzP0Lllim1TWuXwC2VxHnkTwnSg8STW0Oh8rN2e16NhAo8GY0fVLLulgYWwbw_IFosN7HnLtkoTQr0CLdgdsjyvITk58YrQMb8WVQc3R7EPydLXuGqqYMOW_mh3mGngfirL5G6yFkBt5YxpXJvnctCH6C3azZNbsybuahn40Ac-KNkepNaBQrKt0_zrjBORiw0l8ZlMathorArHalu48_Eap4auWmIcXC5NL4lGqeMT7iTqd9rIi07Ou2qJav7pzpeUqwg2ivnVi0vAjxoFW_MxTwCXOuXH_Jz4YrfvDIl1eVUudrRdCOcxo4-wd6AAAIgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات موشکی روسیه به پایتخت اوکراین
🔹
روسیه امروز رگباری از پهپادها و موشک‌های بالستیک را به سمت کی‌یف شلیک کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/449875" target="_blank">📅 15:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449874">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCiI3QGoWYOlH5zR3fZ5gW4BbN3IEwe-7LQE5WueQc8ZU-Xzo0Ijh_lB1k62jJX19zMmPZFsCYSWhX1LaxD72s58d2-1spo2IYkA7Dx0ri0aj7kBuIykp_m3qBvAHCuDR4f_uoPkcPYgGLJVJ_1D0TUsml3WUOlViUlF8M9W0EAYVFr9Uq0P5LhCs_NYfK4Xmp-9OAHJp3uq3M15VHZvMWMn-E6nMG9qaVeuT5wupBI-gnL6VUNJq1iaLosIOEaEKuRHKjNiR464RAmWbO4Z7AzrTg3YuhbZgAHV71T8z5PL0BrOAcBXqfUcQjpL7YYy-LuGweLHpAqsP5txZMEC9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجۀ پیشین اتریش: دغدغه اصلی ترامپ، تنگۀ هرمز است
🔹
کارین کنایسل: از نگاه ترامپ، اولویت اصلی آمریکا تنگۀ هرمز است، نه برنامۀ غنی‌سازی هسته‌ای ایران.
🔹
ترامپ نمی‌خواهد قیمت نفت سر به فلک بشد. او آمریکا را نوعی نگهبان تنگه هرمز می‌بیند.
🔹
ایران خواهان اعمال حاکمیت بر تنگۀ هرمز است و آن را آبراه ملی خود می‌داند و خواستار دریافت حق عبور از این مسیر است.
🔹
ایران تسلیم نشده، ساختار حاکمیت آن تغییری نکرده و به‌نظرم آمریکا از نظر نظامی و دیپلماتیک در وضعیت دشواری قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/449874" target="_blank">📅 15:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449873">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">آزادی ۵۵ صیاد ایرانی بازداشت‌شده در امارات
🔹
سفارت ایران در ابوظبی: ۵۵ صیاد ایرانی که در امارات بازداشت شده بودند، در حال بازگشت به کشور هستند؛ ۱۴ نفر از این صیادان از طریق دریا به ایران بازگشته‌اند و سایر آن‌ها هم قرار است از طریق هوایی به کشور بازگردند.
🔹
این ۵۵ صیاد که عمدتاً اهل استان‌های سیستان و بلوچستان و هرمزگان هستند، در ماه‌های مارس و آوریل به دلیل شرایط خاص منطقه و اختلال در سامانه‌های ردیابی، توسط گارد ساحلی امارات بازداشت شدند و بیش از دو ماه را در مرکز بازداشت سویحان و زندان‌های رأس‌الخیمه و شارجه سپری کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/449873" target="_blank">📅 15:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449872">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTkREIkvK0so7ve7hCyURgRL5IG5I1Iod2t8G9-zW8tjqLytsRPAUsf-v8wOacD58eSNZgWA0vwkH4D5VNbB7nsIIGXjDohe6rsHeBZoWozP9e9X4nnrFiZKjhoouPaOwb4beCyHkZRRleKMfq7GiVhRhUxKYlaQJ5ExDpHE0w5fz8X0My65jKi-C7UFSyObiPAcyeNm-b_7mGoMMEIcQzndmytoDwUTQhjABd_JeT-bexp5xdzY2r8VCEYq5MBZFjuYlANXGuScno9uLLeNOLnZ0hB6ooiK4o01JMaKUy3CUllRJ2XwQaI6_rPsCmfu8R0dstsc67mPrTp-e6OxfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فناوری به جانِ جام جهانی افتاد
🔹
گزارش رویترز نشان می‌دهد تصمیم‌های مبتنی بر VAR، آفساید نیمه‌خودکار و حسگرهای هوشمند، بیش از هر دوره دیگری اعتراض بازیکنان، مربیان و هواداران را برانگیخته است.
🔹
کارشناسان معتقدند استفاده گسترده از فناوری باعث شده روند طبیعی…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/449872" target="_blank">📅 15:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449871">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bB_NICydLXOipcZLISXxy7u1zAy9N-xM2FTjVWmKc9olBjC9_vfrO0Fwd1z1_mWAcono-TOUr65YlQhdm6zMxWl-sLj64IwThfHFt41dXhuUqzASgQZCLl3bNv0pJgbA6khap2hdvN6P_SpGRBPj1zud8qaqEwb4v31YlgI26ghGVw6zvlxkB51D32h4ZtjvkND2m0TgDk3t3YmUsRCyGBaqbP1Xn92wkXsegyzfGru-USeY15EobTYouhGGKcm1iRAv-F81vM-RkaojiE-B_OH1P3JLlXaMduEZUaAYx3xT6aR7ObL4N3FtLwYj4ogAx2titdu2chw40KT45Fb9zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل اتوبوسرانی تهران: ۷۵ متروباس برقی وارد خطوط تندرو می‌شود
🔹
تاکنون ۶۰ درصد از ۱۵۰۰ اتوبوس قراردادشده تحویل شده. هم‌اکنون ۳۹۰ اتوبوس برقی فعال است و ۲۸ خط مرکز شهر کاملاً برقی شده است.
🔹
۴۰۰ اتوبوس دوکابین دیزلی، ۳۵۰ اتوبوس برقی ۱۸ متری و ۷۵ متروباس…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/449871" target="_blank">📅 15:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449870">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3e9a1337b.mp4?token=Ypz5Npste9XXpn8HJop4zc7Aq4JHnPlqP8VDMHg-HqC2UkQiRUifel7Y_JwJsFsZUcMi5iSzv2PMdhUQmyayzY1hxc_JMlpdWyaNPKrE4HlsmeI-17YAIRJPCLpKuyTZnQ9fU2w2o0b7VodbIvkBYy8jKo-MsFe8DNx_JMWsGFa7U09N9I82IZY3xPgOmWUBR0m2dMVp-efOgwx9y28M_Le6hTB3nDTvrqRwS5sevifPCJCGzJqa9k2brgDqi1v6QzqsqVxBT7EmrRNEqOgzgaSyjdwpKLDG8_TnpKid7IksKoK6elAq_baXQlCWevUC7BPbJrAVFwCWFAhfSZMi2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3e9a1337b.mp4?token=Ypz5Npste9XXpn8HJop4zc7Aq4JHnPlqP8VDMHg-HqC2UkQiRUifel7Y_JwJsFsZUcMi5iSzv2PMdhUQmyayzY1hxc_JMlpdWyaNPKrE4HlsmeI-17YAIRJPCLpKuyTZnQ9fU2w2o0b7VodbIvkBYy8jKo-MsFe8DNx_JMWsGFa7U09N9I82IZY3xPgOmWUBR0m2dMVp-efOgwx9y28M_Le6hTB3nDTvrqRwS5sevifPCJCGzJqa9k2brgDqi1v6QzqsqVxBT7EmrRNEqOgzgaSyjdwpKLDG8_TnpKid7IksKoK6elAq_baXQlCWevUC7BPbJrAVFwCWFAhfSZMi2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر خارجهٔ روسیه: حملات آمریکا به ایران نقض «یادداشت تفاهم» است
🔹
لاوروف حملات آمریکا به ایران را نقض یادداشت تفاهم میان ۲ طرف خواند و تاکید کرد، این اقدامات در را به روی هرگونه توافق می‌بندد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/449870" target="_blank">📅 15:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449869">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a8e353249.mp4?token=kwVFbzagC_H72DVZb0LdWDOAMUdS9TabhFILyodj3Zws9SRQyNAxJeWucnv5luuAEZlEXdC2WFidqFWmNTM2VPPiA5wc92Yi7iOmceJ_KDTKzrUuuMUsrR0X7m2lW0o6W-VDx18_Wu6ZDBJSINAAlxruiu-nZakxvceMhcLArHLUx5VBz4nOz7lmBv1XfnyRUPt-jVWOZCsnBqpDC64zfqi6Ky9rl2ijdplj8rgJrp-Hv-ZL44p_J2_JOQJZ2DUph_JOljwKVp1D76CqsVtbvqKWhPEfRoN1Pcttdy3_x7yubyRNEqOe6wD7_a6B9ktYzYdBSUPgGdDvbyyVBE2lLYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a8e353249.mp4?token=kwVFbzagC_H72DVZb0LdWDOAMUdS9TabhFILyodj3Zws9SRQyNAxJeWucnv5luuAEZlEXdC2WFidqFWmNTM2VPPiA5wc92Yi7iOmceJ_KDTKzrUuuMUsrR0X7m2lW0o6W-VDx18_Wu6ZDBJSINAAlxruiu-nZakxvceMhcLArHLUx5VBz4nOz7lmBv1XfnyRUPt-jVWOZCsnBqpDC64zfqi6Ky9rl2ijdplj8rgJrp-Hv-ZL44p_J2_JOQJZ2DUph_JOljwKVp1D76CqsVtbvqKWhPEfRoN1Pcttdy3_x7yubyRNEqOe6wD7_a6B9ktYzYdBSUPgGdDvbyyVBE2lLYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله دقاق: خون‌خواهی رهبر شهید به ایران و جهان اسلام محدود نمی‌شود
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/449869" target="_blank">📅 15:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449868">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cf2WXzeuNwze3ixk1BTN-LnuBitmSjaQUBv74h_sLQtT8ZSW2MBiYJ4s4rsuymO2outs03nL8FcHfhh6gY0f8UCDOZD98VHd8DsuWvyUm5i7H67-zIYJ5yj4Ynsef1mpacMuRE6oH9hMVwXYRaIlt7Fh-P4kYkiyzsC5Re2aqBiKQYwZUwjZU4p3rBIRsad-AB3eeXd79zG3aowmg7dTRVrK61OAT_XcwhKw6U_F1yX3MJ1iuv0xSKThsTsh2jiyQ-X_xuKqHtqY_culNvsD7LNl7SVHnBA77Oud6zk7iSYL1d0zXLqmQM2AA31DqXUtrIbHluisj33yblM90G8KxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دست‌دردست برای امنیت ایران
🔹
سخنگویان ارتش و سپاه، در دیدار با یکدیگر بر گسترش همکاری‌های رسانه‌ای، هماهنگی در انعکاس عملکرد نیروهای مسلح و تقویت هم‌افزایی میان دو نهاد تأکید کردند.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/449868" target="_blank">📅 15:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449867">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70a7a1cdf3.mp4?token=SMzLAPLmHdM6bvP00qUG_w6fZcm9a6DIWDkRv1XfoiBZAlN5ih8mDsawMzv3bC47GTxt9IH0JLz5zJVUKuMY3qf_k9qFVZ2_khD74ozblhlqySFuL1Ppmr4VIzzC4kfqPiyIaMrL9CX5w45I2X8kQxTAsurq4wlDYuMrEWELK2Kb6xH5U7b5paDH9pzVm17BD2cCvS_xpWgtmRajgHAv6NZYC2xarIFzNIVmHdd1cS_4bXz3cVku6ivPkPiXkb9M1WkQE7FSt7qXIMOEr8i2SqHLqd6irZ02HMn-pyAjrogFFOYx_Qq3x3kZ-LUCtDeRBLKN20tI6-2mQg1h-KIL_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70a7a1cdf3.mp4?token=SMzLAPLmHdM6bvP00qUG_w6fZcm9a6DIWDkRv1XfoiBZAlN5ih8mDsawMzv3bC47GTxt9IH0JLz5zJVUKuMY3qf_k9qFVZ2_khD74ozblhlqySFuL1Ppmr4VIzzC4kfqPiyIaMrL9CX5w45I2X8kQxTAsurq4wlDYuMrEWELK2Kb6xH5U7b5paDH9pzVm17BD2cCvS_xpWgtmRajgHAv6NZYC2xarIFzNIVmHdd1cS_4bXz3cVku6ivPkPiXkb9M1WkQE7FSt7qXIMOEr8i2SqHLqd6irZ02HMn-pyAjrogFFOYx_Qq3x3kZ-LUCtDeRBLKN20tI6-2mQg1h-KIL_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر صفوی: در سال ۷۶، ما ۲۰۰۰ موشک داشتیم، حضرت آقا در آن زمان فرمودند این تعداد کم است و باید به چند ده هزار موشک برسد.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/449867" target="_blank">📅 15:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449866">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6807a69f3.mp4?token=bKlgKgY_hQ7vrwIknSAq-7mwRJqKv1ZIZn0VSwkADIisK-xGU34mL7O1d9uoiNi5doLvJEy4k1HG1ClzXaOhkpobC7eO3LR-aq7tLrcX5UdvtQp9lQ-rka6Zg69S2dMks4alNayke1692ULNp_Kilwq5-Gnc0szRYp5siddpJlYQksGJpK1myl79xngoTosErHxBMWwjqkUV5DABZVezmHHh861uRn49mrS6GsdKvRcH1a_JrlqmMfqf8V2ZxW4k0PmKpPVmFcHZyaB-yn9plYCtfN8XU6LR-f7q4qEkpnl1UfmYm5CO1fh1Sx3yBL6vpAl8XZgRfoeCnPMRRJ2LsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6807a69f3.mp4?token=bKlgKgY_hQ7vrwIknSAq-7mwRJqKv1ZIZn0VSwkADIisK-xGU34mL7O1d9uoiNi5doLvJEy4k1HG1ClzXaOhkpobC7eO3LR-aq7tLrcX5UdvtQp9lQ-rka6Zg69S2dMks4alNayke1692ULNp_Kilwq5-Gnc0szRYp5siddpJlYQksGJpK1myl79xngoTosErHxBMWwjqkUV5DABZVezmHHh861uRn49mrS6GsdKvRcH1a_JrlqmMfqf8V2ZxW4k0PmKpPVmFcHZyaB-yn9plYCtfN8XU6LR-f7q4qEkpnl1UfmYm5CO1fh1Sx3yBL6vpAl8XZgRfoeCnPMRRJ2LsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلاش آمریکا برای گریز آبرومندانه از تنگهٔ هرمز
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/449866" target="_blank">📅 15:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449865">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPLdzaWm-ZfEJbWCS39NM9GhT-pURDJImPtIe4_QTUzhluMAzuUEuZQ0kjr6I9f3jq2tXeC5zx8BWXeu3x9ka8WDdlRUtpG9-rxaGV3M-Lb6ehM6NJsA85XYnE9Y3LAg2Ge6QxtqHVkay2t_guYiE0_gOOR2uutXHHv_BFm0Ss9PxlLIrGt_oBZGUrSqA3r35rcGtGUs1RqpEuxdeE06lR3YJX_gJGMIYzIU_C92O8lsTsVeelAkYywERq5g8zfZBurQBoFR8DsmgTxCzrgtIx2vjJoExqomlRBx9Pyfn_MmiivXTzyN3YHH-U0JP-aQHlAvwaXhNMM9cRBBGxLhFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استراتژی چادرملو برای تأمین پایدار مواد اولیه؛ توسعه معادن جدید در کنار استفاده از ظرفیت بازار
مدیرعامل شرکت مدیریت سرمایه‌گذاری امید، تأمین سنگ از بازار را یکی از راهبردهای هوشمندانه چادرملو دانست و اعلام کرد این شرکت همزمان با توسعه معادن جدید و اجرای پروژه‌های اکتشافی، از ظرفیت معادن اطراف نیز برای تأمین پایدار خوراک تولید بهره می‌گیرد.
بابک ابراهیمی با اشاره به آغاز فعالیت‌های باطله‌برداری در برخی پروژه‌های معدنی تأکید کرد: معادن جدید در آینده به ذخایر چادرملو افزوده خواهند شد و این شرکت با ترکیب توسعه معدنی و تأمین سنگ از بازار، مسیر پایداری تولید و رشد بلندمدت را دنبال می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/449865" target="_blank">📅 15:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449864">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس‌ پرس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRFV6nnbryUT10MW3oRpf9728tI-PzZnVVJijP7jLbuCrVCfLxGOYed3WkSEGMq-hl7M9YIGclOZgN_3Sc9BuFzmP5iPDReY5Cc5lXR0KaQxixYV6yisvwpHRzCOI35fRmanERFB0plwL7GDX2DwMVO8Y4mDahFZ2qcV_wMKnl0D43sZUeBGHjCOi6XOoggSEZONT5KDiHXy-xT524WcwRVF6EL2BKtKe8SC6Yx9GXv2wHGJ1sF7rBMvo87G0O37qGYxxv79EcPNT9iKwVlpZ7zTooMrEHkyKr3Wpww7oZzm228-_W52dNjy0s2wJ0fsSpqtDkP1A23x75yo8MBQjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
نگاهی به کنگره جهانی معدن ۲۰۲۶
🔰
مس؛ محور تحول آینده معدنکاری جهان
🔻
بیست‌وهفتمین کنگره جهانی معدن (WMC 2026) در لیما، پایتخت پرو، بار دیگر نشان داد که آینده معدنکاری جهان بیش از هر زمان دیگری با تامین پایدار مواد معدنی حیاتی، بویژه مس گره خورده است؛ فلزی که امروز در قلب گذار انرژی، توسعه زیرساخت‌های برق، خودروهای برقی، هوش مصنوعی و اقتصاد دیجیتال قرار دارد.
🔹
بیست‌وهفتمین کنگره جهانی معدن از ۲۴ تا ۲۶ ژوئن ۲۰۲۶ با حضور مدیران ارشد شرکت‌های معدنی، سیاست‌گذاران، دانشگاهیان، سرمایه‌گذاران و نمایندگان بیش از ۷۰ کشور جهان در شهر لیما برگزار شد. شعار این دوره، «معدنکاری برای آینده؛ اعتماد، تحول و فناوری» بود؛ شعاری که بازتاب‌دهنده مهم‌ترین دغدغه امروز صنعت معدن است: تأمین سریع‌تر، هوشمندانه‌تر و پایدارتر مواد معدنی موردنیاز جهان.
◀️
ادامه گزارش در مس‌پرس:
https://mespress.ir/x6RJ
@mespress_ir</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/449864" target="_blank">📅 14:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449863">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/449863" target="_blank">📅 14:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449862">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obO3U8sHVEnNkquPEp_IWO-cxHK1eAjIEQCX4A-03cB-NQyrKCdxA4uLwtU5IiqmxLqFSQBxQL9QfgBxiqq8AyTyaS29twX53RfE2mLMItwjKqNxPF2sOymv_PIrqTCg4f0GAYAutimrEmM4gg9BV8bf3KunM93NZUk_ccTYw60wQwxO-3L2GAxD0kPRhwGfV78AoG5sOqltTz1msU5WSealSeijvYyNX37W2568Vf1eucOI2xDNQ5z_sI8EBe9U9n0B_d7BKCGt4G1z0jQO2eGK1G2da5aIhFQhcvf9ZZyIhg5Xi0d4PnOeUsQd06K_OG2lpTPYsOjaQlyHUB65vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت از ۸۷ دلار عبور کرد
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/449862" target="_blank">📅 14:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449861">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حکم پرونده‌ای با ۱۴۸۱ شاکی در مهاباد صادر شد
🔹
دادگستری آذربایجان‌غربی: حکم بدوی پروندهٔ یک شرکت هرمی با ۱۴۸۱ شاکی صادر و ۶ نفر از متهمان این پرونده به حبس‌های طولانی، جزای نقدی، انحلال شرکت و مصادره اموال محکوم شدند.
🔹
بخشی از اموال توقیف‌شده به مال‌باختگان بازگردانده شده و بازپرداخت مابقی نیز طبق قانون ادامه خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/449861" target="_blank">📅 14:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449860">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1bf31e2df.mp4?token=PHtRfk_UVC-dgyWmrn9w3_vmpT3GdypiZiti2ZSFLDrgGzkf7L7JrebrGmM7Z4P5Fx_s6kseKIJfSMkV4GtO7tquhqLgZLkjwOVHYMcNis2bx1duUcRQ-Zx10ooo3wBz46tTrE7JoucFhmmd731cxUIorG1y6aJ1MfzOAm_jqAbs3KiXkVn7SgMfHQgGS2cOIn225pPohkKQ5sL_PyRSEVYkjm2vBAtt2mlRD9GatXIapeQx54yn2tdZu8ESCSZyOZxulDKvqtRTkitROJaCQK5NpMmrPs80nwuKCv2rolHVIFviCRPZdU-RrgTQnXs03t9LMS0YPtv9lLqeIo_fhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1bf31e2df.mp4?token=PHtRfk_UVC-dgyWmrn9w3_vmpT3GdypiZiti2ZSFLDrgGzkf7L7JrebrGmM7Z4P5Fx_s6kseKIJfSMkV4GtO7tquhqLgZLkjwOVHYMcNis2bx1duUcRQ-Zx10ooo3wBz46tTrE7JoucFhmmd731cxUIorG1y6aJ1MfzOAm_jqAbs3KiXkVn7SgMfHQgGS2cOIn225pPohkKQ5sL_PyRSEVYkjm2vBAtt2mlRD9GatXIapeQx54yn2tdZu8ESCSZyOZxulDKvqtRTkitROJaCQK5NpMmrPs80nwuKCv2rolHVIFviCRPZdU-RrgTQnXs03t9LMS0YPtv9lLqeIo_fhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
نشست علنی ۲۲ تیرماه ۱۴۰۵ مجلس  @Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/449860" target="_blank">📅 14:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449859">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGrS6vUiXMee-mP5rPeEIvv4p0mfcxL3iyMkTw9bawqWaEPCcxtxAdmahAbC1dpt8Dkxb-iHgij3_lNbZeKjsiGjpb3MP8rvL6HHlJgS_935IylOg0_Qlzw0MxuUuDD98kgkbZOUrQn33aOS6SU0kDG7GhXFrhBVXtxSiLDSPtiXPDTw4qKPS8_Y5LnomPwKxxMrocZ91NRmJ3HF28NUUTMo6-xytFfT-qtz_V__GpGsI1HqM9M23NEfQdw0EM_0y0sBFU660dIlNvA3CtW07JIqHNIvbc0mh0Baj2EAJYebqmLuX-GERtVyUGAXMAjJOD6KxyGd7raQRMnkfUn-aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله جوادی‌آملی: اسرائیل و آمریکا در مقابل ایران ذلیل شدند
🔹
هیچ‌کس فکر نمی‌کرد که چندین ماه، این خانم‌ها و آقایان اینگونه در میدان‌ها حاضر شوند و منادی انقلاب و اسلام باشند؛ رهبر عزیزمان کار بزرگی کردند و بعد هم شربت شهادت نوشیدند و شهیدانه رحلت کردند. این جریان میدان و حضور مردم را هم نباید دست کم گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/449859" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449858">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‌ جزئیات حملهٔ دقایقی قبل ارتش تروریستی آمریکا به بوشهر
🔹
معاون امنیتی استاندار بوشهر: ظهر امروز ۴ نقطه از بوشهر هدف اصابت پرتابه‌های دشمن قرار گرفت؛ ابعاد و ارزیابی خسارات احتمالی این حمله درحال بررسی است.
🔹
براساس ارزیابی‌های اولیه، تاکنون هیچ‌گونه تلفات…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/449858" target="_blank">📅 14:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449857">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0b2b196d.mp4?token=lPM_xKdOEGvnNdYWHnJB9e3qBAvJVvcseVdNs2QiM9pmCjh8d-cZWVGWMBmTD7bf4LBYvFLpIO96tpNOtisJrkyAhGwxFYQ_SBpvF1XR58LpVrnurcoXpwnLhvrOuNapW7wTBow926JP0RG7bhquMSYA7QMEpgD3C-vfevxgyrTS8RsjnlFXq5IKQhv_I_r8wLrXrrUr5-dTUGu6iMVgA4u4NlSV7kMeZNv7GPD_vK1u_cgxcBMxauoP-hP7nT13TozQPXnx59ArRlZvNrhOMyv4mj4fdwqnE6pQ-FuefrTYaJ7K4dCGH1Zpb2rwnABe4FT8mpsalkZjTr04FX8sew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0b2b196d.mp4?token=lPM_xKdOEGvnNdYWHnJB9e3qBAvJVvcseVdNs2QiM9pmCjh8d-cZWVGWMBmTD7bf4LBYvFLpIO96tpNOtisJrkyAhGwxFYQ_SBpvF1XR58LpVrnurcoXpwnLhvrOuNapW7wTBow926JP0RG7bhquMSYA7QMEpgD3C-vfevxgyrTS8RsjnlFXq5IKQhv_I_r8wLrXrrUr5-dTUGu6iMVgA4u4NlSV7kMeZNv7GPD_vK1u_cgxcBMxauoP-hP7nT13TozQPXnx59ArRlZvNrhOMyv4mj4fdwqnE6pQ-FuefrTYaJ7K4dCGH1Zpb2rwnABe4FT8mpsalkZjTr04FX8sew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با بسته‌ماندن تنگۀ هرمز کشتی‌ها همچنان در خلیج فارس لنگر انداخته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/449857" target="_blank">📅 14:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449856">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اصابت پرتابه‌های دشمن آمریکایی در نقطه‌ای از آبادان
🔹
معاون امنیتی استانداری خوزستان: در ساعت ۱۳:۲۵ دقیقهٔ امروز نقطه‌ای در آبادان مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت؛ گزارش تکمیلی پس‌از ارزیابی‌های اولیه اعلام خواهد شد.
🔹
ساعت ۳ بامداد امروز نیز…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/449856" target="_blank">📅 14:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449855">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اصابت پرتابه‌های دشمن آمریکایی در نقطه‌ای از آبادان
🔹
معاون امنیتی استانداری خوزستان: در ساعت ۱۳:۲۵ دقیقهٔ امروز نقطه‌ای در آبادان مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت؛ گزارش تکمیلی پس‌از ارزیابی‌های اولیه اعلام خواهد شد.
🔹
ساعت ۳ بامداد امروز نیز نقطه‌ای در بندر امام خمینی(ره) مورد اصابت پرتابه‌های دشمن آمریکایی واقع شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/449855" target="_blank">📅 14:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449854">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13186af33f.mp4?token=myxud-yDm060v__wGfaFW94Tr58ig5-Z_vMxrMvVNGhw0NNO_sgircmBnB1fOiX_jUjRdMPFr4mOUtjDD1efrZ1Io4D8UHLd_PkSa_xf2mduHZhkPyZFSeE5akbt8-BSh2gf8WlW5yTqLxJOnoYzBuIzvZDSj1ymoQmtfvpcwQ4io4r1NgL17MMbvPTFBJ8JmjkWNZ4UXYKMcAiHnLd5ePjfg-4yiJv4_PXQxZb4N0b6gVeZAdkALVS1cLmWQKEJcpry8_p_xrQ5TqEmCKiKpG_hSXiiqhDUAETzjqEGIoTmaLna_cWk_8G3ArRLgyuho081mc5eoColr9Gc5Pui9LQsWyEitjXLMwoXX3CcXUMIG6OVZBG9p7xEO8qXV8VerB9EMk86IItFBSEc8Gi-e2BZY-Y9cW42AswUDs44deff4XLc415U9hkUf9c2QrOGWI63GwVgx1dtoKhHI1DAeKW8lTGfdS56JyPBXgyhxzYa5jXByqeuqNcv2O8BVu-SJaTLHoqOG-jVhmRHW7q72MvfrLCoHu8EVdErlZKKIe-TRNLJCF7uBFFpiLNQgrQAz5kZON2kKk3quXeauV6K2-FTFJqeYSQC1l60A2OPjgjup72s1g_43Xak1fFFAtDWIcL8HAl-mQhFU4uQ97koSY4fk1PmuRkhHcDPb7DueTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13186af33f.mp4?token=myxud-yDm060v__wGfaFW94Tr58ig5-Z_vMxrMvVNGhw0NNO_sgircmBnB1fOiX_jUjRdMPFr4mOUtjDD1efrZ1Io4D8UHLd_PkSa_xf2mduHZhkPyZFSeE5akbt8-BSh2gf8WlW5yTqLxJOnoYzBuIzvZDSj1ymoQmtfvpcwQ4io4r1NgL17MMbvPTFBJ8JmjkWNZ4UXYKMcAiHnLd5ePjfg-4yiJv4_PXQxZb4N0b6gVeZAdkALVS1cLmWQKEJcpry8_p_xrQ5TqEmCKiKpG_hSXiiqhDUAETzjqEGIoTmaLna_cWk_8G3ArRLgyuho081mc5eoColr9Gc5Pui9LQsWyEitjXLMwoXX3CcXUMIG6OVZBG9p7xEO8qXV8VerB9EMk86IItFBSEc8Gi-e2BZY-Y9cW42AswUDs44deff4XLc415U9hkUf9c2QrOGWI63GwVgx1dtoKhHI1DAeKW8lTGfdS56JyPBXgyhxzYa5jXByqeuqNcv2O8BVu-SJaTLHoqOG-jVhmRHW7q72MvfrLCoHu8EVdErlZKKIe-TRNLJCF7uBFFpiLNQgrQAz5kZON2kKk3quXeauV6K2-FTFJqeYSQC1l60A2OPjgjup72s1g_43Xak1fFFAtDWIcL8HAl-mQhFU4uQ97koSY4fk1PmuRkhHcDPb7DueTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همسایه‌های رهبر شهید در رواق دارالذکر چه کسانی هستند؟
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/449854" target="_blank">📅 14:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449853">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‌ با رای اعضای کمیسیون امنیت ملی و سیاست خارجی مجلس ابراهیم عزیزی رئیس شد
🔹
عباس مقتدایی و امیر حیات مقدم هم نواب اول و دوم و حسن قشقاوی سخنگو و بهنام سعیدی و یعقوب رضازاده دبیران اول و دوم انتخاب شدند.   @Farsna - Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/449853" target="_blank">📅 13:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449852">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
شنیده شدن صدای چندین انفجار در بوشهر و جغادک
🔹
دقایقی پیش مردم بوشهر و جغادک صدای چند انفجار شنیدند. هنوز محل دقیق انفجارها مشخص نیست.  @Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/449852" target="_blank">📅 13:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449851">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWvRUsXGLjeM2uWa68baEo2HmEnafHvQv146MbH_sUxKF8Z_Z_2p71oJ2WEAkuceOIcYyB14Lt2ROI_-KuQdrGOkJv-VKmKU5bPnQum-3jQwQTwTpqy025dUFWr2teuvymyE9zU7sFUdW8mOVvHx0QySL2WfTGS8p8BW8jT8M6MYe3KGRws92rs8B4qiD8s25ICdm8LmGaiu1xlLhB9RTrqUYXZStRkkz0GSQoqLsnOTaH0mCQDiKrIiZeZCWcrCJXtyYv8Y1jgY-YxVZlFjx1QtR0xXMZAk2-UgDc2g5Cq9HGP92lt7jSbg-nc6QL2qQCQlPK6sbc7hux-2ntxypw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بوسعیدی: ۴۵ سال به‌دروغ گفتند که ایران تهدید منطقه است
🔹
بدرالبوسعیدی وزیر خارجه عمان در مقاله‌ای نوشت که به بهانه و دروغ «تهدید ایران» منطقه خلیج فارس نظامی‌سازی شد، اما اکنون مشخص شده است که این حجم از پایگاه‌های نظامی و تسلیحات هیچ کارایی از خود نشان نداده‌اند.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/449851" target="_blank">📅 13:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449850">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
شنیده شدن صدای چندین انفجار در بوشهر
و جغادک
🔹
دقایقی پیش مردم بوشهر و جغادک صدای چند انفجار شنیدند. هنوز محل دقیق انفجارها مشخص نیست.
@Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/449850" target="_blank">📅 13:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449849">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
صدای چند انفجار در غرب بندرعباس شنیده شد
🔹
مسئولان تاکنون اظهارنظر رسمی در این خصوص نداشتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/449849" target="_blank">📅 13:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449847">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TlVG8MsSl_uudEi7JuMVZnpskptHDOJywr1k0UlcfAglU8q6QsEL0mOeb3WvkO_AxsRr9tXKODKUTwY6NWthJIly5q92jNL0TaKfFBHN7pNI6O66KCO_uUqXuL530muadO2DEfFV_ExqXAoFNAfk0X72XBMb9FPzffQFLhNvFsBB-F5Ehmp7UpAnN1wGvwfXap--VF56D9ZMRy9GuCp3rg2mkLvthgTCw_6wf19vdEdEJNDDX7tQ-U988GKcPaj2tgbfHOzuiuOANT7lPB4XJuQXDp-Li_CNchwPyll0RmCXwKNlkGxHIC1GkW7tNipWIknfA2KCfykbmsv0Xbkv4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vDR2ne64mgwN3o8j2EZDDpRYSN8ofxT5-XxzVw0j3WURzQ6Vwnr6ER5QMIIPlwa7uFtzyw_hjzOZkNOx9-Sz2tj7783RSG-Gq09mDlOk7-YCb9tAYMgxSQbUIMmDwBq8MAGTvpdyzI__3ONYC87Hi0srwviV294AxfmjHQOmvcHpsi7VuL-pJbTqZlQ8XFILTg2ABa5igm2WvEAaEyBFx8wjkHjWjkHZrWAgYZmbIzlC_HIFSOCKdxgk_bB2BjFDbV37DbqhTGuypDCWeFnp7co2BSRtfapYDkUJQn26SXbB_koTjOzgE8AFS5caANQbdEuoTIsA8X48-b6mkDgXIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پیام رهبر انقلاب به کشورهای عربی بر روی موشک خیبرشکن پرتاب‌شده
@Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/449847" target="_blank">📅 13:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449846">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95cbc38cc3.mp4?token=gZ02yeBv8ETZjdySnwtxUX717uCu4PV8X3SoQIuoQdYLW_y5Z7A63K6OtXhhTgt39l-T-6OS4of5h6ztnrMA2BF6ILkoYWAatdPHiI-z5plC07i0zK4KzlLnG9Haxl5EvSOFhzUt_2JmkBS4YlUbbBSzcqNExKWoyjicEMTWL7hkrqzvII6_CK9hEkpG9Z6ZilTZ2OI06FbfxZV8zbSsrZZXSBPwG1t9RYL8epPreXHxnUEQJbiTftv5vwWvMVLKfyppQPO4_3JJnUlW3fkRs_erWKefU07dO0ycNgY_g5d8KTHxfuaWG1ZGPZ7IW6Ix-5OHFRQUGm3cvlfShZKsFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95cbc38cc3.mp4?token=gZ02yeBv8ETZjdySnwtxUX717uCu4PV8X3SoQIuoQdYLW_y5Z7A63K6OtXhhTgt39l-T-6OS4of5h6ztnrMA2BF6ILkoYWAatdPHiI-z5plC07i0zK4KzlLnG9Haxl5EvSOFhzUt_2JmkBS4YlUbbBSzcqNExKWoyjicEMTWL7hkrqzvII6_CK9hEkpG9Z6ZilTZ2OI06FbfxZV8zbSsrZZXSBPwG1t9RYL8epPreXHxnUEQJbiTftv5vwWvMVLKfyppQPO4_3JJnUlW3fkRs_erWKefU07dO0ycNgY_g5d8KTHxfuaWG1ZGPZ7IW6Ix-5OHFRQUGm3cvlfShZKsFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ماینرهای غیرمجاز؛
سودش توی جیب دلال، دودش تو چشم بیمار!
این روزها دستگاه‌های استخراج رمز‌ارز دارند حقِ برق من و شما را می‌بلعند. طمعِ سودجویان، عامل اصلی خاموشی‌های بی‌موقع در کشور است؛ اما این قطعی‌ها برای ما یعنی گرما و کلافگی، و برای بیمارانِ بستری در بیمارستان‌ها یعنی بازی با مرگ و زندگی!
💔
🔸
آیا می‌دانستید مصرف برق هر یک ماینر غیرمجاز، معادل ۱۰ واحد مسکونی است؟
🛑
*سکوت نکنیم؛ این یک وظیفه انسانی است:*
اگر در همسایگی، کارگاه‌ها یا مناطق اطراف خود صدای مداوم فن‌های قوی یا مصرف مشکوک برق را احساس کردید، قهرمانِ پنهانِ شهرتان باشید.
📬
آدرس یا موارد مشکوک را به سامانه ۳۰۰۰۵۱۲۱* پیامک کنید.
(هویت و امنیت شما کاملاً محرمانه باقی می‌ماند.)
#مسئولیت_اجتماعی
#قطعی_برق
#ماینر_غیرمجاز
#حق_شهروندی
#قاچاق_برق</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/449846" target="_blank">📅 13:01 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/QB2CxLwPBFIUgX9LU8AuAHjfVE4ZUugFVRPKJ2lLpZz0PWdrsbC9_fBaYuIB6cXXTAsaZRIoh271hOhyqzeiyZAPymb-v4FKLVdxF630qou_-apPfZuTFTesCccIfSnpSBwtFvLQeFsW6pkHfjPnKz2d7VQoaBpwutT83YBnjssCDUjjWlC0uVgvQSRnAVU4WxC_SIvVJlHtiPQa2qAq-flMU-NJHgei2BDnxzHaEebjwWb2BE-Qs9ka-ZNcORnDdDwDW7N9RhXa8vVSDPMad-HijIqBx8rim5rWgh5_JC45YSiRj8V_tYSsqNXD8RKVTHoTVA1n6tDHOEfIYccbTw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 03:28:57</div>
<hr>

<div class="tg-post" id="msg-447297">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46aeca7a65.mp4?token=tps8Rab6IVbZQO4Pi_x9CMhfDGgb4FGY1Rr8AVuL70JOmfNPiA3FP0S1iHVooKbBGGk9OZJ0Y7mZrSDLEDvDkzrUknBvR_HtnZSOOVPBjznIWkQPUWEb5KfoCHREV9FYRxV07lXj6NPMbPrqnx_ShyJJYhjSh7z2gXLLT5CbdRp8YNQWefVbhzp35wq9dIwDPtJiKpzco4kJE0vEAwB6IyIrBRJBmB9ypRh0CH-mm3j5zCGeduGHbLE9prGC03cZBPCgv5lkVQh9R8-7Ec-TzIH1VJVkBn2ExrqXbL_h7ZcieiGxXm46XjoVldvztWWnQDKy_9B1LdmkPO9wcuOtgTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46aeca7a65.mp4?token=tps8Rab6IVbZQO4Pi_x9CMhfDGgb4FGY1Rr8AVuL70JOmfNPiA3FP0S1iHVooKbBGGk9OZJ0Y7mZrSDLEDvDkzrUknBvR_HtnZSOOVPBjznIWkQPUWEb5KfoCHREV9FYRxV07lXj6NPMbPrqnx_ShyJJYhjSh7z2gXLLT5CbdRp8YNQWefVbhzp35wq9dIwDPtJiKpzco4kJE0vEAwB6IyIrBRJBmB9ypRh0CH-mm3j5zCGeduGHbLE9prGC03cZBPCgv5lkVQh9R8-7Ec-TzIH1VJVkBn2ExrqXbL_h7ZcieiGxXm46XjoVldvztWWnQDKy_9B1LdmkPO9wcuOtgTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیام دانشجوی آفریقایی به مردم ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 817 · <a href="https://t.me/farsna/447297" target="_blank">📅 03:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447296">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/860521e59e.mp4?token=pW4izN3R668-jpXrH86ffslQUojgiuyVio6vIML5M5Fp7GRZJpObWmQXnOyTLzFnrA31BBH5AAU0_2CCCGmaBMJiiA8wuBXOtorWacRdoNLnYQDfCNRfXdkY9ynVSjecQfuEKFwF_mS3pU0SpOPVpo-Emnrb8gjzEU4okn_t2KL1waNYvbJrhiUPBhVgcy4mcQFRHcDNeLW8vdJjOkCYQTFZX0QS1iXzLvN5b5TWeQ1SwBnRavDfvlD1CwozZskhzIJsiUsjJjH7XKSxzbwEr0J8ylYHBhkDSKzV7GXMtf0SDonfir37kjMIlO_9a3mXir_rHwdSopZFv46zTwP2oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/860521e59e.mp4?token=pW4izN3R668-jpXrH86ffslQUojgiuyVio6vIML5M5Fp7GRZJpObWmQXnOyTLzFnrA31BBH5AAU0_2CCCGmaBMJiiA8wuBXOtorWacRdoNLnYQDfCNRfXdkY9ynVSjecQfuEKFwF_mS3pU0SpOPVpo-Emnrb8gjzEU4okn_t2KL1waNYvbJrhiUPBhVgcy4mcQFRHcDNeLW8vdJjOkCYQTFZX0QS1iXzLvN5b5TWeQ1SwBnRavDfvlD1CwozZskhzIJsiUsjJjH7XKSxzbwEr0J8ylYHBhkDSKzV7GXMtf0SDonfir37kjMIlO_9a3mXir_rHwdSopZFv46zTwP2oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این جمهوری قائم به مردم است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/farsna/447296" target="_blank">📅 03:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447295">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnfQI-kJNWrXGwv_A1NS3ROVsBYepJBauLGYNDkTSUL9QxSRpmb4RdqcGcuQ5NtFyk6_z8H1twKwxkV5xHUFQXj93rJ4BOqxmcBhfTxeV3AcS_rD7dUvCzNpHLXIWs9BgQ2xUyRkYG0sGxyssUjxGjHWeH6nXNZDV31Glf0hkWcCj-NBLOcKbh5Qnox7NqV-iRmFnJtn0opyvjgXZ95w3zjAds7pO6aFqj_1EoGjHl8YToax9_MpSYYVFlyTQwhK3R5tdwlN2bzSVpR8KuhHVnJV3HeoTF-ObklMZwvSjR8VCw5kvctPxLDe7zIaSpqDXJE9uShyXqD9iwjVIJwPjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
لیست پارکینگ‌های مراسم تشییع رهبر شهید در قم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/farsna/447295" target="_blank">📅 02:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447294">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_PhIPbkQ7R97ceNODcWnO6UIQyAXsOj5K_4Dp0ei_549Cs82T0aqN6ZV93oZo_StK-b2kSZD-jY_IpG5w4LUg7OmKbSh7NiSKKALXTU4MKyMe84jDqeCb_JY1I6AeVuOaeTvJQz9dVEyR1ZP3c2ItdN61FPCJA7RMQJ9JUbsE8A_ifWSIDUsd3sbYmwqX_xR_Dk1gnkulz4OfgRa4HyDlL5qn-_2tT3zWozd_nQf4NjLmqAFGYBOHfCheX_RZYYHoT-bJdPjXA0HQjnEtIL4Nen_c1OAZtOlJZ1SxnRcfHfagDRSyc6czC1ulXsxOPJWBUZoRf9n7v8whddUfR6MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
دیدار مکزیک و انگلیس به‌علت شرایط آب‌وهوا با یک ساعت تأخیر، در ساعت ۴:۳۰ بامداد برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/farsna/447294" target="_blank">📅 02:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447293">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">صدای انفجار و آژیر خطر حملۀ موشکی در پایتخت اوکراین
🔹
خبرگزاری فرانسه از شنیده‌شدن صدای انفجار در کی‌یف پایتخت اوکراین همزمان با به صدا درآمدن آژیرهای حملۀ موشکی خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/farsna/447293" target="_blank">📅 02:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447292">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKi0H4BiBehMM3Fcu150amyv8YqHdfFaI6yEMTyTNg-_8bgH89Zev6a8VUlU6cmeWMPmOvGYgqzaB5SEYIbz_XgDpK1KsVcmeBS1u-IGLrJQBlfFwzvVXzDZ20Lh21iGMiIJXFftgWNZ8kyIQNEb-qwkDPZBpCeNfaEC-m1vNmz_ywaNn-QRbv3YkDc5KaYQNh0w21ingnL91vYLZ3rs4iCRPh0mKSndvyXH9DxGJaDA4_Zkml9xEnmbrhNpRNwXQ5Q7p24htCaP1M3aV6Jh4TN19slVXzV1Ha1HzRDeTUxWlzyWnkbw9VnUjXcP_1u3NCacw20HBq7j-exncLHBtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تلفات ونزوئلا به ۱۷۱۹ کشته رسید
🔹
با گذشت پنج روز از دو زمین‌لرزه پیاپی ۷.۲ و ۷.۵ ریشتری در ونزوئلا، آمار رسمی تلفات به ۱۷۱۹ کشته و ۵۰۳۴ زخمی افزایش یافته است.
🔹
به گفتۀ رئیس مجلس ملی ونزوئلا، ۶۱۱ پس‌لرزه در این کشور به ثبت رسیده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/farsna/447292" target="_blank">📅 02:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447291">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbRiWOxKzFnrj6kt86mJzZYG__-0Ysgd7Lofj_ejS8BhDrRUYcInAj5meehUZ_fefXpYGLzt1mdsD1FfYVVHhWJTalV6HA4HMFw77NLJ6QUcFdJwxoP7XdQ6u3qdJhEG0SUQno6gUL-RndSXg8TMqNsimW4f2qDnGNrpzBIpLAX4QmULIvur-SIOXY7sMV2lpXJrSkcKmzGtEh6_eeN0rroWdewf3ropwOYsb3y3TrsQLq6B9d2UM9inaMamjOw7jlrmi5Zj07mcMG1iomuOUVbVnqSkYIYbioAPml3cReIjPM5liI-sxE3AR-XHzS6rkNOdAFtuYem0c-4IvGw4mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریم باقری اولین بحران تارتار در پرسپولیس
🔹
مهدی تارتار پس از معرفی به‌عنوان سرمربی جدید پرسپولیس، اسامی دستیاران و همکاران موردنظر خود را که در سال‌های اخیر نیز با او همکاری داشته‌اند، به مدیران باشگاه ارائه کرده تا کادرفنی جدید سرخپوشان هرچه زودتر شکل بگیرد.
🔹
پیگیری‌ها نشان می‌دهد مهدی تارتار تمایل دارد کریم باقری همچنان در کادر فنی پرسپولیس باقی بماند، اما شنیده‌ها حاکی از آن است که باقری تاکنون تمایل چندانی برای حضور در کادرفنی تارتار نشان نداده و همین موضوع آیندۀ همکاری دو طرف را در هاله‌ای از ابهام قرار داده است.
🔹
حالا باید منتظر ماند و دید در روزهای آینده مذاکرات میان باشگاه، مهدی تارتار و کریم باقری به چه نتیجه‌ای خواهد رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/farsna/447291" target="_blank">📅 02:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447290">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfdv7Lq8SG2L2AV3XAosz4vydJb0ytMR5pgKe-0_d20rxQ9aMG2Z1tBhNovHTSrdN-EHeCAObhYgrIN8R-cDp50BIeXIZuyZDqcgoBrZxcPjqgMNeeSqP7sovY9KR9GA2L-DON9_Qg9EhdHZnIkPGRy2w3bbn9Y1aeTMbG5bsWPflKhSAEUkfcQrgjsOw5d1xpl3Rb_zpTEzt1-bniii90VXSxzY-D8orFWjNaNvhSj6f83pyXxipzpgQZMF0rO01caWWrn9EJfrQVF0xZ_2f4ISFV4MZjYxtUcmD24mOtdIOjl1PYnOXaVr4J2q2WR_hhs2Q0iZTZJYQIHPRYmlHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلوک‌های سیمانی «کشوردوست»، سیاهپوش به مصلی رسید
🔹
پسر جوان با ثبت حرف دلش روی دیوار سیاهپوش مصلی می گوید: «آقا جان! مثل دیدارهای بیت که حواستان به دستنوشته‌ها و چفیه‌نوشته‌های مهمانان بود، یادتان نرود قبل از اینکه ما و مصلی و تهران را یتیم بگذارید و بروید، سری هم به دل‌نوشته‌های این بلوک‌های سیاهپوش بزنید...».
📎
اما مگر این بلوک های سیمانی چه پیام هایی برای رهبر شهید دارند؟
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/farsna/447290" target="_blank">📅 02:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447289">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c8a5d084a.mp4?token=XDQNMqZfkfyxDQrxeb5QTiRIZEeiGk6lEjxYOirf9IDDBiVNHYWGg4wgdWuPqqvxXzUGviJ9hMGFzWOxrFjzV3KgvnP-0DGFIME2P8gwWUU4ePv81JATRq_xIrVT4YyjLoU_sfkKz6UQGttUvgHq57kCg1EGMj4NN_3Fv3IHyKyKKINm7uuC1u6ip1ABSOKsEtQGG0F3mznNl-Xt0kgeP2DPDVak67gmjxROhM8bAnD8sErJm3eOHqXuRgi05KfmkNTM36yFGsH9xz9CZMJAqYM3IBbVehzLrrvoLrl5wvgC7VAIkhb-794yENXfu4A1TCNUe9JudS0wSMkQ1mG_EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c8a5d084a.mp4?token=XDQNMqZfkfyxDQrxeb5QTiRIZEeiGk6lEjxYOirf9IDDBiVNHYWGg4wgdWuPqqvxXzUGviJ9hMGFzWOxrFjzV3KgvnP-0DGFIME2P8gwWUU4ePv81JATRq_xIrVT4YyjLoU_sfkKz6UQGttUvgHq57kCg1EGMj4NN_3Fv3IHyKyKKINm7uuC1u6ip1ABSOKsEtQGG0F3mznNl-Xt0kgeP2DPDVak67gmjxROhM8bAnD8sErJm3eOHqXuRgi05KfmkNTM36yFGsH9xz9CZMJAqYM3IBbVehzLrrvoLrl5wvgC7VAIkhb-794yENXfu4A1TCNUe9JudS0wSMkQ1mG_EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
️
به رسم همیشه در دیدارها، حرفمان را کف دست‌مان نوشتیم که شاید ببینی و بخوانی
@Farsna</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/farsna/447289" target="_blank">📅 02:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447288">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91581c02ef.mp4?token=TZ1sjSjNz0lRsdyHuSF8yYOd60eTTognQ2jSISWbRDC4em6EyXQzCyoxWQdy0_k-o3TNHQNJQXmkt6FnH7WCyDzp4Gh7a3c2w9bxh8cmYu6OFg4XeN_F1aAN9m5gzOIzytSm9fLahKaxdhdpxfpO573AP6tPsxE_rHxHqnpI_57kERhyduztABDM6CNMxVyqs54A2O9cdQBIkX-Vm-1tNdjeGUPVhroR8-wVFdqV5Eh5JFJBg6AMRgfiFoo4RXd6zwnpDI8P_7cjp-ANTaJf_TIgUqVVNiqncV054N6BuFB1tHFktgmh8gpBhzfmZuM-L3NSwucVkJbm_WkZ6sNDogFBFTcoIQzDPDiBjvvlpxMIQEdVnCTtB21fSXarNnRY5kh-PlofPwJpV_RiJCo3ADFjHfA0r_KvFIK6-68M6U2EagmX3YFOqeJEsWtdDWcukNUIVTCAzx8vATmy7W1oOQPmbKqTfzQ6S4G-Ogisqh9xip2FjLXsIB-MVZwuiNBcKYkTnGfQzicObMkCr4T5ZLTKmYZiBF-dWXZl2A7lQQfjeXtpPzc7NsyGDDCircVQqo4Vb3TDO2h7rfCuUX1VauSV0qin8dk1dRkOFIwgVtz0lUVuF-tMS_y7eOy3XjAut30Izm3PgDe0Ao4nYMDex5aDBpR9K5Pt5o9puQ2EX38" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91581c02ef.mp4?token=TZ1sjSjNz0lRsdyHuSF8yYOd60eTTognQ2jSISWbRDC4em6EyXQzCyoxWQdy0_k-o3TNHQNJQXmkt6FnH7WCyDzp4Gh7a3c2w9bxh8cmYu6OFg4XeN_F1aAN9m5gzOIzytSm9fLahKaxdhdpxfpO573AP6tPsxE_rHxHqnpI_57kERhyduztABDM6CNMxVyqs54A2O9cdQBIkX-Vm-1tNdjeGUPVhroR8-wVFdqV5Eh5JFJBg6AMRgfiFoo4RXd6zwnpDI8P_7cjp-ANTaJf_TIgUqVVNiqncV054N6BuFB1tHFktgmh8gpBhzfmZuM-L3NSwucVkJbm_WkZ6sNDogFBFTcoIQzDPDiBjvvlpxMIQEdVnCTtB21fSXarNnRY5kh-PlofPwJpV_RiJCo3ADFjHfA0r_KvFIK6-68M6U2EagmX3YFOqeJEsWtdDWcukNUIVTCAzx8vATmy7W1oOQPmbKqTfzQ6S4G-Ogisqh9xip2FjLXsIB-MVZwuiNBcKYkTnGfQzicObMkCr4T5ZLTKmYZiBF-dWXZl2A7lQQfjeXtpPzc7NsyGDDCircVQqo4Vb3TDO2h7rfCuUX1VauSV0qin8dk1dRkOFIwgVtz0lUVuF-tMS_y7eOy3XjAut30Izm3PgDe0Ao4nYMDex5aDBpR9K5Pt5o9puQ2EX38" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این خصلت آقا زندگی‌ام را تغییر داد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/farsna/447288" target="_blank">📅 01:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447287">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvoVtIlkBosISU9ZEsxJw83d3Y_NH87uHKTIyZ6kjhTCcXtBQm-VQoRZJW64vFAvVCx8KrKu9VY6mlWoNVxRLe1PTHdvePKI04mAhEv05cZrj10SdeZ5naeWGkIcIvWdg7Fri2mF8URkbfqStHK_fpQC2OV1LWMmgOnu2DQnbm9NHDCIRR3lC3e6VTWvEKm4bPJhe9ZkdY-wiPsjQUPEboirgNir2lPDfQKgyeWaZyU-tikGeuiKXLvH3T2VllwD8dWeRjnWJn9VUXx63eVWdFAaj1EBMJz-oYFdxouXMR64bN9hU_FLssf1p2anrMKU4WioZueLHVTqy9MDsGgyvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نمودار حذفی جام‌جهانی ۲۰۲۶ پس از حذف برزیل
@Sportfars</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/farsna/447287" target="_blank">📅 01:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447286">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4f7a9b09c.mp4?token=Ctptx3EHUPbmkR-MJ-cIWpQIxp4jAfZ5g86dzvMJ7LCSIMXJQy8pHt7DBxN83J14rHyG0h2TEBW35rubNk9YNfa4I2NHr7Mr7QyBks3F3e1MpAgfS9vpSfy3y2YLPzuu1FYJcDPP5sRiUauv2r_cFYGVNk6LtclVQu8h9Er8xqEiyHeKTxtTSK7IPGGGmOGGh4ZxX7MR9mJFBrH54S8ryEOqszF7o7UnipBGmhCh7ofKdceOEQTh3arVtR11JS127lMagBceurxKN2h5FOVUqGTp3tPWkw8yaJO0FKCO7hI7i3Jr0OHR2YljvVaN1b0n2Y8HVVpe1iB0zt-nHilD6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4f7a9b09c.mp4?token=Ctptx3EHUPbmkR-MJ-cIWpQIxp4jAfZ5g86dzvMJ7LCSIMXJQy8pHt7DBxN83J14rHyG0h2TEBW35rubNk9YNfa4I2NHr7Mr7QyBks3F3e1MpAgfS9vpSfy3y2YLPzuu1FYJcDPP5sRiUauv2r_cFYGVNk6LtclVQu8h9Er8xqEiyHeKTxtTSK7IPGGGmOGGh4ZxX7MR9mJFBrH54S8ryEOqszF7o7UnipBGmhCh7ofKdceOEQTh3arVtR11JS127lMagBceurxKN2h5FOVUqGTp3tPWkw8yaJO0FKCO7hI7i3Jr0OHR2YljvVaN1b0n2Y8HVVpe1iB0zt-nHilD6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین دیدار، آخرین نماز
@Farsna</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/farsna/447286" target="_blank">📅 01:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447285">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvOPa5SWRcDKSvoaPaB7FOxV7C8BEIEekEBHfoS7jNa_lVfvWhwLqlE8MRXs5qi1zU3XH8yiglGdIFJCI33jgcdSNADhLbYP2yCaKuiQkRnRQ8tmhbt6cqL01TfsGq_hrCUUkD1BQO_U3GWQlqHo_d1Gm8RxqT23ewmmMYl_gmcvzJnsxyWyFDwIs4AgrKjYauc8Emrn8XdOUhBJhai70cwt8elCcaayfUwnO71aVdpBCxAhzL9jHdSoznAz8C_YTGiD_pw6BpOpwdE_DHwK5FZ8FlZmHeTDgaL3OEDku65ZTprWk6OFRVRHsaZj1e96d0xWVegKwrz-QdE26n02pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برزیل از جام‌جهانی حذف شد؛ نروژ به یک‌چهارم صعود کرد
⚽️
نروژ ۲ - ۱ برزیل
@Farsna</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/farsna/447285" target="_blank">📅 01:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447283">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cdbff5919.mp4?token=CehbuxGO63wHmb-ZxY29K-WZj0VJ9KuGeb2uu2DzxELKn8MjwwtKIAoXjkgrkc7FHQniYORAVtIwBKQn6SFpO5RMfrEO4uMIEH7d7FB1CHXHsOMTxaRUS4Vlv3wIIJWK1SjYjt9rINJFIc_eiuaT368EMgBffs6rSay-bGazsax-r-Xw5yOdA7Hkxi9VOQ-m0ATWGJu6MiTKinwmUw8sW2renhXGABNCdZlbZp0W6g6aJ3TIy60M8fzNHgPsEBUT3Wd65zeSAf-vpNCj7rHu0SrOgsIrUwlzzFX8JAk5UWNazzpB9Evmmt5177EkKOkSTwhrBnqa1sdKD-MhMqTQLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cdbff5919.mp4?token=CehbuxGO63wHmb-ZxY29K-WZj0VJ9KuGeb2uu2DzxELKn8MjwwtKIAoXjkgrkc7FHQniYORAVtIwBKQn6SFpO5RMfrEO4uMIEH7d7FB1CHXHsOMTxaRUS4Vlv3wIIJWK1SjYjt9rINJFIc_eiuaT368EMgBffs6rSay-bGazsax-r-Xw5yOdA7Hkxi9VOQ-m0ATWGJu6MiTKinwmUw8sW2renhXGABNCdZlbZp0W6g6aJ3TIy60M8fzNHgPsEBUT3Wd65zeSAf-vpNCj7rHu0SrOgsIrUwlzzFX8JAk5UWNazzpB9Evmmt5177EkKOkSTwhrBnqa1sdKD-MhMqTQLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این دیدار با سال‌های دیگر فرق دارد...
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/farsna/447283" target="_blank">📅 01:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447282">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d884ee2d3a.mp4?token=rRgi6Ne42_ZolDQ5R8ju7YPELNgCG4nI6RUmUn7b2zPTartnRG3dsUgnYj_Q7v2uU7MHkw9W56MIN8aIqWZX_oqEBOmOdtDb5dhNO8gVFEsXPzsHfMCcMRlqZM8Nbkp8wqkh4u1WPXjIfwTvg2_XwmdOQl3dt1l74Ser5qYpeuuvNo1E1U6XBM6DDxuqSoKbolqRN5Ob_MKtHA0B5Oir0sRaKhteE2hvhUfR8AnSmxpLDB8v2oZ6SKH_miIsh93MEo5CM8tB_r9fAdlkwzPg4U0tB9XdPb6nycvZ2g7ytiqEFmiVEs7pOVz3PwMTOSTbbpxmvoit9XnCWRCpAqSSHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d884ee2d3a.mp4?token=rRgi6Ne42_ZolDQ5R8ju7YPELNgCG4nI6RUmUn7b2zPTartnRG3dsUgnYj_Q7v2uU7MHkw9W56MIN8aIqWZX_oqEBOmOdtDb5dhNO8gVFEsXPzsHfMCcMRlqZM8Nbkp8wqkh4u1WPXjIfwTvg2_XwmdOQl3dt1l74Ser5qYpeuuvNo1E1U6XBM6DDxuqSoKbolqRN5Ob_MKtHA0B5Oir0sRaKhteE2hvhUfR8AnSmxpLDB8v2oZ6SKH_miIsh93MEo5CM8tB_r9fAdlkwzPg4U0tB9XdPb6nycvZ2g7ytiqEFmiVEs7pOVz3PwMTOSTbbpxmvoit9XnCWRCpAqSSHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینجا دزفول، و دلتنگی مردمی که جا ماندند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/farsna/447282" target="_blank">📅 01:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447281">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eup1D8eWgefAHMsToVuCBx86YnDGNydIk-q9CrSIOFbmQIBHe1pkONwQhy7OUXrLIevRgaEq2pn9g9URR21ro35aqaXP-3LAcVbIXvILXy9pRKUCP6IURF3zc-oZ-ckORu_7ci3Runy3hnHdhn-9cL8dKVGLqoRlax-4kx0VxMHrreM530ksGJKs3US8Y5WiVFEh26hGNsmU-edijFiqJqYdr7t1M760KbdlE1cR9dRGH-4ZOSICXwUK43Z6D69vvteouCl67lgSk4uRq-oDnBkr-eTmU49cYQiv-FvD-S1UCHfH2sMKYnY78YWul1SujYWJsQgbkzBt2d08WI7W8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌سوزی‌های گسترده در پرتغال، یونان و اسپانیا؛ هشدار دربارۀ انتشار دود سمی
🔹
روز یکشنبه، صدها آتش‌نشان در پرتغال، یونان و اسپانیا به نبرد با آتش‌سوزی‌های جنگلی پرداختند. در همین راستا، اسپانیا و ایتالیا برای کمک به مهار آتش‌سوزی عظیمی که بیش از سه روز است در پرتغال ادامه دارد، نیروهای کمکی اعزام کردند.
🔹
مقامات یونان از ساکنان بخش‌هایی از «تسالونیکی» (دومین شهر بزرگ یونان) خواستند به دلیل انتشار دود سمی ناشی از آتش‌سوزی در یک کارخانه بازیافت که در میان شعله‌های آتش گرفتار شده، در خانه بمانند و درها و پنجره‌ها را ببندند.
🔹
همچنین عصر یکشنبه، یک آتش‌سوزی بزرگ دیگر در غرب «آتن»، پایتخت یونان رخ داد.
🔹
سازمان آتش‌نشانی اعلام کرد ۲۱۰ آتش‌نشان با پشتیبانی نیروهای داوطلب، تیم‌های تخصصی و ۲۹ هواگرد (شامل هواپیماهای آب‌پاش و بالگرد)، برای مهار آتش در جنگل‌های کاج منطقه «ماندرا» اعزام شده‌اند. مقامات در تلاش بودند تا قبل از تاریک شدن هوا و توقف عملیات هوایی، آتش را مهار کنند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/farsna/447281" target="_blank">📅 01:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447271">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/resW1B9Je4r-MU3hBUxpCBOunWlDqRFuyKxby3p-vn8xkS-fmWbs45ADQ6iqbrH7hAGmknynTeCzkd5D_Tuuwem19_L3zvBlwDP0XW0pttCAChkZpD0Aj39y-gnznXGZReLuZUUZKdfc4N0zCiV5ivNDQsqm8du3pgwnIPA5y3ZIIRUWoSsTctQLNrvkTJS09vWp0Cm96doAQS5WmAfZaDjMjhnMWhRh9UaNkKeHBFEAShJUSoCHDAIITLJRdHLd4tJozitrZFyjKyB_7Zy8xa_PZeBA7h7y_rtZ7GIv9kq3EI7w67UlCzBWfIQShfZ6aarvgvTgm-IoGYR6kwXquw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TzCtdsqpbzhKHMZEeP86ZSNtjq0GdnaTF9S4bSVv0MOj9O0bC8GfBzQJMskN64_EiJ959AV4aQM3pzX-HA-BLDdc-a7yZ9_NGcYGeRK9FIADvSZfpWOYU4nBkubDT88TH-QT-getLoZ8jNjGcAGgg4_cZLU292_UF4QBqdt1A-rJIhgSnIWh2p4teQj8_EkVHly39CJ9ARk8QOoJyNtHI9ok3_8NxpL5BQPb_7GkRziWagPoS2B0TsaeXg1LcWJdqcwJMUOMdm85n48qcUGz55uMuENAjTDuWAzohliwcvLZ7sgF-T4LfbuFXdF7EbUCXyp9MKy-hsjqdyLvo7PGYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jaBHlbgZ9K_8l_RlB5SV6ilX2SDj9Hbee4Xhw1nn53aNjJWXAn6_7KoRy0hYYNwLRoK7dwCFzY2SoUx3G5A6cLpGD0HUiZRhTswyizTtRHabSfF3i1oykePjJkbs1upNWzeoaon5I7iS1lPIL7l7v46VpdMmkTA9uQ6DCs-1O4vRHpljpKshcp8mSXPARbFqtDNuj4Y6dsLpwf35-NMdMxCnuuZcZt3wA0jUWA09SX83wP28puWy9CdQgDB2xFZBgumk7fAvCaJkcUkkj39iOfYsg6IGOgZ1ogFZxwwCgncocV4nteUmbfvtu7N19JOV0Z3-sBbQCMi7kekpYJPBgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oLBgJi35kdxcbwXWkl7qrUAi-8W12NGU8DSVlhkD3AOpZ4Ov0VXasbDsPKJjCmxWBSJhCtjBHqLCzCa7YV-cMNaxR9Y1mDDyln7abM5cw_M-PA-Qd8YQJLPQiqvc7_UMPjWu61QC4q_5U3ZvpEbOMkEdbUKdB1I88OEIg5XCLcsRiy0uW05b6ZhJFPXp2fkkW1Ee8gPX5wKyUk8QCKnwWICm74cx7Io7tBANsstWOGwhxnseChe2lYShoiBKn861W623D3PwfqeKzNq1ZO0JfSVIPtHk8KsKkNJd00zOLBJQIXjvesMgqZfwY5f-EC2L7Aba0SfgORGB2qLIQv9_bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/stDKNHbfRCXsOrpOhrccevjQmSvwNb364fUgxhFUnpDEAkuhHiUTJPf-zbZocPu-2zhsi1-nIjVrXhNzl2zwDHdkhthtGE002KyXiOwuRzcOSmQd2gNAzwxLS5pk4kp0X0HcvJC1dXps4nOx-7k15HOhV-iO1FLPoTAkeL0wwCUUXehAbOv88nH_40aMkcCAOjScSKLm294g40O6o18EvAMkTsACy-cSgCAtWeYVp53vOwQq9qm6-EOp3Ye6iBMX2T6FjXrptbfcoMfdJMsEg4hTpuO2o9XXkB7_U-16q-PWG9qKuQH3Wdf0sF2DdwHMXaStMrz2g3RLmXpTwEpILw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/py_7znmnn1OxajbyXei2blzTp-D-nV3ySGDXnv54ASiT-qpn2gKbYSFiNUoajrpnn9kBcqghaK3kbe6lqh5y_hjIewcG_jMkKXFYQr4ZonM-G-JmuDmGWBagsSWp0qSVPzrNr-Qm63G-Y1LLSnmFNWXv-oLxDqXY_QBzVij1uVgFDB-_NMVcg_-Cg6Axwp2GMDfnnVwxctCIGy2gbOtaXI-_NQDyRm931qQy2FD6QTQEkIuJ70LUnA5kjGbVofmyUIjygwREhmrnmCODFpndDb20ktO76qB13wQr-Wqoty1fQmZHH00pDauYBdk0sKAx74C_wkdyPlPIPdxd19Ii8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W0RA2NrDPUhluQwCnQH6lPBDIpr9yWBhFIYaQutvajQx4FKUchKR97HUYJV0x6SXUUOhKnMChdJKnLYTofXZva_3otKOzO5ibPRVDVzNvTNXP7G-79aAVKeXvLS3LJkSuNWsT7MQbhx_11eod9e0Y-X4CdnB4IX6P5FxGL5QAFiOAGxC5kA8_SA16uYVTpjrRsEeF8KQiusnhfsD71KDqRPyloICE8NTEZZFiZV4BKpdRXvaNJqwjjkaFRAtqR8p1BE5dl7mDK5uauqUuFVG88u1ojJgeexTmKjcO199NvovPwtQtt4LVfdvMbl42MunWNiEU7E5ArhamJNacZB30g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eOipbfjlSh-LHE4aKG4i8iUrhmSCSvxEY49Rpn12f7DCwqaO_7gNS6IoozmGrU_TCXhsRn_Zrmmuif7hr1WENTo2zb5sT7_E3T0BWh_I6a3vBSl7LcKT3BHoxosz-xKbHmq0ORt1tKsOtnr4T6Qm2QzuG_6aP4-hjfCBpSFRNVVb1U_ArPI5qsunFN-oDrmJ4u9yF6ABP0rMwSwknjVRP0zenpempDctEIn0Do7I_82UpF9GG2qDwda4NPyrjsBuGaen3lCXMP4kXV_OK1Mnfv_hA4p4bXcVy2meAhmemeO74hetT5cTSW5J-ZOwFQhzu-DqoGxFDNlHK17Em5SncQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YkoN6SZSkYScLKIurTQBRvVxmQID41fY9XILCrVP4Dh6pwFO9cpku-BKbhhe3AJRu-2JzjdTtNo2xyZIvmVWlE7rOY9pJFj113U4MlbggGMUzUKikERfgw9yts6L9ugiIm8KCBhkc6Z7cjqdKEzb-G-N6t4aaSmeWrZ8OMWIFbCjcHERgph1KGZjJZSP8pFDIaHhEvYgiDLQAiMr1BOIkknpldh4rwlGuKw7jG4X2O8BOHqADwRy4U922x2vV3o2g5zCGG5aM89qROs9YrKIEia9riRbBk67ESKvoFrYVRSOa7jQrbOc59sph6Ju08x5c7lpelZsyiQZkfjpSr6zaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uoPZp38SZHNiBi_OdNlO2Pschm2TqAW2CsRfKiaMo1lQIOxv3WrMtN6t-MrgwIf0a6ix0KrF7J_FhCiZzeyHUY59IIhHKX2gGbdgH6312jxDADQeXSH0XJj9IbPb5MLoKmqssOgMfPJ45VCUeKtZDA1ICkEeEJ4r3N_bu-A5yEiME6Z0kJcRFHB96NiRQoBM3Qszl0XCAl8lgWK3hFShCRa349b2RPABFRC-q3plAXSfQd7ui8pAM0U1MCZmPtjtvGStcsZTeStBzQCrw2OK6msvqdJjd1zDWNIpEcy6BbZUHi6CuMkH3pIhsf20B5X7GjuyACNq18UPox_z45DcrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | دوشنبه ۱۵ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/farsna/447271" target="_blank">📅 01:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447270">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c11ebc07.mp4?token=WIl1GHqKZJxiUiUe6jjIA43NJ9veUX519vSjmTkOlQP8PG7L2HfCe5uwwZiWXfPBiVnhGpUMJM_zOqEUnstngoOtTJ3dTNXJhm4DDVVBpn6twUe4WtYJPM26q0gYLwdxHSGXV0uEzuRl901tMMCUTTXiNDfvOCY4bfoIjubSJiA0m4ow7V-FD-az5bw4zRM1X9FzXQe0InNE6N9jxm5rsOURCdKBBiTNIZR0hIffS-lCCLq722_ohT1ywmZEnD6ZN0aV6f0Gv58sKPB5PLR8vO9hsImzQVw__YEpHLRtWlN7OyoTdjihRFPJm8C4JF2pQBmMgxsgUNp18etHz6uISA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c11ebc07.mp4?token=WIl1GHqKZJxiUiUe6jjIA43NJ9veUX519vSjmTkOlQP8PG7L2HfCe5uwwZiWXfPBiVnhGpUMJM_zOqEUnstngoOtTJ3dTNXJhm4DDVVBpn6twUe4WtYJPM26q0gYLwdxHSGXV0uEzuRl901tMMCUTTXiNDfvOCY4bfoIjubSJiA0m4ow7V-FD-az5bw4zRM1X9FzXQe0InNE6N9jxm5rsOURCdKBBiTNIZR0hIffS-lCCLq722_ohT1ywmZEnD6ZN0aV6f0Gv58sKPB5PLR8vO9hsImzQVw__YEpHLRtWlN7OyoTdjihRFPJm8C4JF2pQBmMgxsgUNp18etHz6uISA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تهران آمادۀ برگزاری بدرقۀ تاریخی آقای شهید ایران
🔹
بر اساس مشاهدات خبرنگار فارس، مسیرهای منتهی به محل برگزاری مراسم از ساعات گذشته آماده‌سازی شده و موکب‌های خدمت‌رسانی در نقاط مختلف مسیر مستقر شده‌اند تا با ارائۀ خدمات پذیرایی، امدادی و رفاهی، از شرکت‌کنندگان در این بدرقه تاریخی میزبانی کنند.
🔹
همزمان، تمهیدات گستردۀ امنیتی و انتظامی در طول مسیر پیش‌بینی شده و نیروهای مسئول با آمادگی کامل، شرایط لازم را برای برگزاری منظم، ایمن و روان مراسم فراهم کرده‌اند. همچنین برنامه‌ریزی‌های لازم برای هدایت جمعیت، مدیریت تردد و ارائۀ خدمات موردنیاز مردم انجام شده است.
◾️
آیین تشییع و بدرقۀ پیکر آقای شهید ایران و خانوادۀ شهیدشان از ساعت ۶ صبح یکشنبه آغاز می‌شود و کاروان حامل پیکرها از
مسیرهای مشخص شده
حرکت خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/447270" target="_blank">📅 01:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447269">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDnxHknm8AT6SrPVlAAwaYnXgWlbj7tswB-36yZS2QX9yW1nAcsebS7JfwtHNEPbU-xEPdgZGs_OfCyAACIr9wwGIZN3DVl-5f5wpa11ukRBkS8SH8NTwi2iKKauV7DihVpJER5H6DzrquGAPscmzBGyjAoAX4CcVeSQy-FDuvV1iwQ1LjrWAwBk7B3e4LEySPjMgK2VDbbj_qxgF2VBwSPEFbCxuGS23yAa7IBXcMOwo_opm55WBqA4TrqEU5jBj7TLp5vztubF3VSa3qNdCvTllHU07yLeBkGso3mtG_2LDYUJmTP-KRTSmUfUAmwQgwKLnVZyskexlXfyIhy5fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راز دعایی که رهبر شهید پای عکس ۲ نفره با محمدرضا نوشت
🔹
خانه پر از عکس‌های خانوادگی است، اما نگاهش همیشه روی همین یکی می‌ایستد؛ عکسی که هیچ‌کس در این خانه نمی‌داند کجا و چه زمانی گرفته شده است. شهید فرشاد(محمدرضا) پورمقدم کنار آیت‌الله سیدعلی خامنه‌ای که لباس سبز سپاه بر تن دارد، ایستاده است.
🔹
«عکس که به دستمان رسید، حال مادرم عجیب بود. عکس را به سینه چسباند و زیر لب زمزمه می‌کرد چه عکس قشنگی. دستخط رهبر تبرک خانه ماست...»
📎
ماجرای عکس یادگاری و دست‌خط رهبر شهید در خانه شهید پورمقدم را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/farsna/447269" target="_blank">📅 00:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447268">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">شایعه‌پراکنی ابلهانۀ ضدانقلاب دربارۀ سیدحسن خمینی؛ از خروج زودهنگام تا غیبت در نماز
🔹
در مراسم وداع با پیکر رهبر شهید انقلاب، برخی رسانه‌های معاند نظیر اینترنشنال، با سوءاستفاده از خروج زودهنگام حجت‌الاسلام سیدحسن خمینی (که از نخستین ادای احترام‌کنندگان بود)، شایعۀ ناراحتی ایشان از تلاوت آیۀ ۹۵ سوره نساء را مطرح کردند.
🔹
بررسی تصاویر نشان می‌دهد این خروج، پیش از پایان قرائت و به‌دلیل عدم اطلاع از پروتکل مربوطه رخ داده و ربطی به محتوای آیه ندارد.
🔗
متن کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/447268" target="_blank">📅 00:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447267">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">آماده‌سازی اسکان شبانه برای ۲میلیون زائر در حرم مطهر رضوی
🔹
ستاد تشییع رهبر شهید در خراسان‌رضوی: برای بیش از ۲ میلیون زائر در حرم مطهر رضوی، اسکان شبانه آماده‌سازی شده است.
🔹
بیش از ۷۰۰ گروه واکنش سریع جهت حفظ سلامت زائران در مراسم تشییع رهبر شهید برنامه‌ریزی شده و هلال احمر نیز برنامۀ گسترده‌ای برای امدادرسانی در جاده‌ها دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/447267" target="_blank">📅 00:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447266">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e61b3912.mp4?token=uKc2HkIFgiCZYvNq1rvw3FbEdz-8dkTVlRukjgSzIogZNRZGCgcB0meacbJBEdnKsSWznLpnz0vFfZrBLtVzdkZL2ExgSZNq3Ee4892IsFhTvsj8uun2VP-lRqykM3CEfjcn7_ItiqdN0hA6fEl80wCIpTeIabiyyDfVxCnJ_EIBsawdMgXJCeOPXtp44A7FXVMjDFELUO9CiQUqcG7cYSasULeyMjVHieLY9cuQNEL6GLdKdUU1UklW2-doV4hTLkP-ye7L-K8HXR-4kUsE6bMMAi5IR4lGVTp0_O1Y-hn-ZpMRcONrw9BZirTAQkrPkU_DzEDp4rH6vUYbZe-ZoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e61b3912.mp4?token=uKc2HkIFgiCZYvNq1rvw3FbEdz-8dkTVlRukjgSzIogZNRZGCgcB0meacbJBEdnKsSWznLpnz0vFfZrBLtVzdkZL2ExgSZNq3Ee4892IsFhTvsj8uun2VP-lRqykM3CEfjcn7_ItiqdN0hA6fEl80wCIpTeIabiyyDfVxCnJ_EIBsawdMgXJCeOPXtp44A7FXVMjDFELUO9CiQUqcG7cYSasULeyMjVHieLY9cuQNEL6GLdKdUU1UklW2-doV4hTLkP-ye7L-K8HXR-4kUsE6bMMAi5IR4lGVTp0_O1Y-hn-ZpMRcONrw9BZirTAQkrPkU_DzEDp4rH6vUYbZe-ZoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود ده‌ها صهیونیست به خاک سوریه در میانۀ سکوت الجولانی
🔹
ده‌ها نفر از شهرک‌نشینان صهیونیست در میانۀ سکوت و انفعال حکومت شورشیان سوری به سرکردگی الجولانی، آزادانه وارد خاک سوریه شدند.
🔹
در همین رابطه شبکۀ عبری «کان» گزارش داد در پی تلاش حدود ۷۰ تن از فعالان جنبش صهیونیستی «پاشان» برای نفوذ به خاک سوریه در منطقۀ جبل‌‌الشیخ، وضعیت در این منطقه به آشوب کشیده شد.
🔹
ارتش رژیم صهیونیستی نیز با صدور بیانیه‌ای مدعی شد ده‌ها صهیونیست که ساعاتی پیش قصد عبور از مرز و ورود به خاک سوریه را داشتند، بازداشت و برای تکمیل روند قانونی به پلیس اسرائیل تحویل داده شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/447266" target="_blank">📅 00:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447265">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ورودی‌های تهران شلوغ شد؛ ۱۴ ورودی تهران بدون محدودیت باز است
🔹
رئیس پلیس‌راه راهور فراجا: بار ورودی ترافیک به تهران از تمام ورودی‌ها پرحجم و شلوغ است.
🔹
با این‌حال هیچ‌گونه محدودیتی برای ورود به شهر تهران وجود ندارد و تمامی ۱۴ مبادی ورودی تهران برای تردد زائران باز است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/447265" target="_blank">📅 00:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447264">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a18b4fe3d2.mp4?token=CEtxtklf5ff4RuzEVeKLMxWT1-nyTI5AliLBRbFHGme4xHGUk3UdqMOBUR1F2jWi-L3nDtimk_ymnYVOhaD-7Rm9884PjIoLiLgfJV_P3jnjA5SvQ0JVD6ad7-1A62UM6XNNIguWHIkr1z0KUT4g456ViMD_33k_jIbp4vJawLmx7JrV651PuZ-Dp_7apuJAaIex4-KtGLju9BT9hGov5hiNPwLrkIlpdjIDdyHhG1z-YqvtsPU6ajOT5Z8L_D8-q4bTgcTYA373JkSDaQPVEGGn1QH_nW00kdXrluaoY2aUTGM3j5FnukUzXOu7HwMW-vXmyTmLmcsPWFFKTWBSQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a18b4fe3d2.mp4?token=CEtxtklf5ff4RuzEVeKLMxWT1-nyTI5AliLBRbFHGme4xHGUk3UdqMOBUR1F2jWi-L3nDtimk_ymnYVOhaD-7Rm9884PjIoLiLgfJV_P3jnjA5SvQ0JVD6ad7-1A62UM6XNNIguWHIkr1z0KUT4g456ViMD_33k_jIbp4vJawLmx7JrV651PuZ-Dp_7apuJAaIex4-KtGLju9BT9hGov5hiNPwLrkIlpdjIDdyHhG1z-YqvtsPU6ajOT5Z8L_D8-q4bTgcTYA373JkSDaQPVEGGn1QH_nW00kdXrluaoY2aUTGM3j5FnukUzXOu7HwMW-vXmyTmLmcsPWFFKTWBSQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تهران آمادۀ بدرقه تاریخی «آقای شهید ایران»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/447264" target="_blank">📅 00:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447263">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc2918bd10.mp4?token=FQQvXhFYl5xV6_qEgKyO3lE12-K_mghzd6dtNdIenubREjC-GPykOTqilwh12sOE2sZo_YjAn5eN2YuMi8Rs22_sspqoJi766MolF15IxFCvNiAOfLgZTKTmMi4iZkpYCmGGYJjTGsMUeNgb5ZvuvMbagMcBmfHcrAgiqAmaFMAFfzdYTN1qOidFprQMn3Kr4aY5C0LMtrHQoKWvrL_4s7LolzNO3DlCJrDgwN7Z7rxUqC6RpPcAWvkeXj6w5H9T3zCKQ_ZnDWdbjbFCLLQ0W1U4ul45VKYp4-gOlk3xfss0yWe3nMmT2YwaRryfSWl7lDReJBLcUua2SIvPTmNzxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc2918bd10.mp4?token=FQQvXhFYl5xV6_qEgKyO3lE12-K_mghzd6dtNdIenubREjC-GPykOTqilwh12sOE2sZo_YjAn5eN2YuMi8Rs22_sspqoJi766MolF15IxFCvNiAOfLgZTKTmMi4iZkpYCmGGYJjTGsMUeNgb5ZvuvMbagMcBmfHcrAgiqAmaFMAFfzdYTN1qOidFprQMn3Kr4aY5C0LMtrHQoKWvrL_4s7LolzNO3DlCJrDgwN7Z7rxUqC6RpPcAWvkeXj6w5H9T3zCKQ_ZnDWdbjbFCLLQ0W1U4ul45VKYp4-gOlk3xfss0yWe3nMmT2YwaRryfSWl7lDReJBLcUua2SIvPTmNzxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرودۀ جدید افشین علا به مناسبت وداع با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/447263" target="_blank">📅 00:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447262">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14e2779e53.mp4?token=lox4zIcQ-FHDBYcYPuZTB1-rXb-NnR6k5YD7YDLTZSmZTh0uuGpA1rF5RTsPVIrRrKy8XlGWVclAi8zphsTIvL79o8fv6UIffgtwpuAKcQ_jIhPy2Rs0Zljjfh3rOJz6qvXPqzWkQjrva7VbirGq4Y2_odQuber66-WkzK8fQZdWoXJf4E_F3znbDYR8grLb-8hroQBQbsLZuJ5liTFwb4_8eFgIwk11YF5Wpb5XyX3_zEhrrw1DIrNHcN1F8MvRMbTPSKjZ9PR9qrICfy2CaJQTtC8zcPjPbvmGPSsUnTgMvy3aZb5FIT24LBlageuSJWRFjNNb641wjFR8IOr9VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14e2779e53.mp4?token=lox4zIcQ-FHDBYcYPuZTB1-rXb-NnR6k5YD7YDLTZSmZTh0uuGpA1rF5RTsPVIrRrKy8XlGWVclAi8zphsTIvL79o8fv6UIffgtwpuAKcQ_jIhPy2Rs0Zljjfh3rOJz6qvXPqzWkQjrva7VbirGq4Y2_odQuber66-WkzK8fQZdWoXJf4E_F3znbDYR8grLb-8hroQBQbsLZuJ5liTFwb4_8eFgIwk11YF5Wpb5XyX3_zEhrrw1DIrNHcN1F8MvRMbTPSKjZ9PR9qrICfy2CaJQTtC8zcPjPbvmGPSsUnTgMvy3aZb5FIT24LBlageuSJWRFjNNb641wjFR8IOr9VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهدی تارتار به‌عنوان سرمربی جدید پرسپولیس انتخاب شد  @Farsna</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/447262" target="_blank">📅 00:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447261">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqsEvr0TrbfUwN9g8NXcnhwxCMo-fwbAyxXhx5yjBoqz1kEoTUmtnXQ1E3ztFerKusl1gNinFzlJqqjwZ-VkmNAwyi0fJyGnOeL2dQTpzf6ozZfA2yNEdDIUp496ytmGkcMd1uhEsgyDemkmXWnAgrqGrnei8q7iOy6y3RRuBnb7PYgSBjKwkbSnnKDYyE3BQ5RH-yrZ4xqyPJxKMEq6RGa9Pa9rEubAjusKc1kF-AJL4yWUXVNiHPRquKMKD4W0yM0UsbZha9D2v0ASa7PCwbsEJHSa0TOMT-5tG1J0CgbziOwkzo-TKB3nLpTt4hmsGxjCCeTJRRkg-oDn2-WQNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خوب‌تر از خوب، بدتر از بد
🔹
«شقرانی» مردی بود که پدرانش آزادشده‌ی پیامبر اسلام(ص) بودند و به همین دلیل او خود را وابسته به خاندان پیامبر می‌دانست.
🔹
در زمان منصور دوانیقی، تقسیم بیت‌المال برقرار بود، اما شقرانی به‌دلیل اینکه کسی را در دستگاه حکومت نداشت، از دریافت سهم خود محروم مانده و بسیار گرفتار و درمانده شده بود.
🔹
او روزی سرگردان کنار خانه خلیفه ایستاده بود که ناگهان چشمش به امام صادق(ع) افتاد. شقرانی جلو رفت، مشکلش را گفت و از امام خواست که به واسطه ابهت و احترامی که نزد خلیفه دارند، سهم او را از مأموران بگیرند.
🔹
امام صادق(ع) با کمال مهربانی و بزرگواری وساطت کردند، داخل شدند و طولی نکشید که سهمیه شقرانی را تمام و کمال گرفتند و با دست خود به او تحویل دادند.
🔹
شقرانی غرق در شادی و سپاسگزاری بود که امام(ع) در همان لحظه، بدون اینکه کسی در جمع متوجه شود، در محیطی خلوت جمله‌ای به او فرمودند.
🔹
امام که می‌دانستند شقرانی شراب‌خواری می‌کند، با لحنی بسیار نرم و مشفقانه فرمودند: «ای شقرانی! کارهای خوب از هر کسی سر بزند، خوب و پسندیده است، اما از تو به‌خاطر نسبتی که با ما داری و انتسابت به خاندان پیامبر، خوب‌تر و زیباتر است؛ و کارهای بد از هر کسی سر بزند، بد و ناپسند است، اما از تو به خاطر این انتساب، بدتر و زشت‌تر است.»
🔹
امام(ع) به او فهماندند که رفتارش مایه سرافکندگی خاندان پیامبر است. شقرانی با شنیدن این سخن، به.شدت تحت تأثیر قرار گرفت و شراب‌خواری را کنار گذاشت.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/447261" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447260">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P45BsHDbqIjmaBjVVTGI6-A0ZNY9-RBrHP-xD6pFKkr0NkuiRop41BoL9NgOWsCXRABeSq3FX31Eb56VUwbk0ZeFa2HMu4oqWVIv_oqWp23C7kTJCV_ZK0oAHS4t4n0UzpbSNaEGoMIRgZm3GSPWitFDZWFfJQLgxOlsvrn4J9PtnjnT_CyFVGhj8IOGHMJSq3KNTr5voTtHofgpogQxdn_SYK8vOTZorGPbgIucxi9zTAtV7JAzMkSJDqrS7yev453Yo6OynhXnf1Pd0ZWpWNpttMeGfTqYN4lAgQyjbnVchJlvPes7RZHmojYmMnQleqdDScLHqQfD2mNzbTvT9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
| دوشنبه ۱۵ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/447260" target="_blank">📅 00:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447259">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9w2somzkrc7DkX-4JvK3iFPYBtkoIYpSSFnLDx4aHm9G8vTk0IEBScgIovAzCaR-qW-LSFOEWh9SQ5ieaXHcNE0ph7eaEeR4579_LWAVbTX6f6UluKXfI-PSi-AiUAex7pcUcfJpAENFWfSzFShJRgDMEd7vUu-WW9HB1dLdHRSYgRyHfLjzcjUTr4Mb34K9oH4BUHI2tUPK_EeLosqKfVavXiWUyfBtmlCk94YsQ2_5Bzl-wQQSRRtt-n275vpKfXJTMxD1ZD3PgQEXuL5Xt4vozhXnYoGxJaK7mtLjftSdY7PlosfjEVHre2EBNy0dx4We5H4B0F632ElOMlY2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به عشق رهبر شهید به بچه‌هایتان تاریخ یاد بدهید
🔹
زنی تنها روی پله‌ای نشسته، چوب پرچمش را به زمین تکیه داده و دارد رجز می‌خواند. نه به رسم ۱۲۰ و چند روز گذشته برای دشمن بلکه این بار برای مخاطبان داخلی.
🔹
برای مخاطبانی از جنس خودش می‌گوید: «آی مادر! آی پدر! بچه‌ها را دریابید؛ بچه‌هایی که امروز، اسیر رسانه‌های خارجی‌اند؛ به کودکانتان از مردی بگویید که ترور شد اما خودش هزینه درمانش را داد».
📎
صحبت‌های پرشور این مادر ایرانی را
اینجا
ببنید.
@Farsna</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/447259" target="_blank">📅 23:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447258">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf1c51221a.mp4?token=WJ-eelKuIXav6ip_DaJD1qdg0BjjOHqMWIUMW2JJslk94TLLx3KuBr_yHYgW0xMdE1e7t-tFihf827sLzlsNDLccCpUIx-K4o_w7lnQOZkE9LmRw8b-iMYMBvlAjyF6HGEUKc267LlsBWQy8ec2bNPNskR-d5e3FS_8LTycHxtd7dCfA0EXc-oZDryvYsZvmjXNHab4pjAxX3Y_T7tBAzRp56FKj8cbYIOAvZ4gF43G6HWfzyRd8e-xZ4ahi5M1iDoMaqKfaDFxDpN_5VMvpP5C9vLBS0s4kEq5ZIs3yEQTD4GRn6mbB7-DDcDBW7xdhtylsBC0gA7ZyEJ7UdvrZ-RZw8Ib8-TqaY2TNszZo-ksIzkiXyG0Z70tGMzYogqRca05IanbwJfuzDdLzeXi63oNQFcxq5ToiyQzWWK1QxJ1DDLsunDJ2oAC3DDjFY0-VfXn_Y3XVVrw_SGMsNj3nUC8Ng5Ce_aABbElT7ug6mHWoD7PSpLK9PB3HLhx29ohH09aSdMV2ZBQ6K1uhrKKuijVP0f4H9pi1xwzzSC6ClaSFZevNUl4vNFy0woXdpekFGea3MnaTnXNtgxTWIs7iSvIvOnXYfMHynvt5tv2bWQkeGXeyeds-Z-WmXaAwo1-JaiFyxU3BDnOFA5ENMg2tANcPIM9rEUQXXk67gsfkdSk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf1c51221a.mp4?token=WJ-eelKuIXav6ip_DaJD1qdg0BjjOHqMWIUMW2JJslk94TLLx3KuBr_yHYgW0xMdE1e7t-tFihf827sLzlsNDLccCpUIx-K4o_w7lnQOZkE9LmRw8b-iMYMBvlAjyF6HGEUKc267LlsBWQy8ec2bNPNskR-d5e3FS_8LTycHxtd7dCfA0EXc-oZDryvYsZvmjXNHab4pjAxX3Y_T7tBAzRp56FKj8cbYIOAvZ4gF43G6HWfzyRd8e-xZ4ahi5M1iDoMaqKfaDFxDpN_5VMvpP5C9vLBS0s4kEq5ZIs3yEQTD4GRn6mbB7-DDcDBW7xdhtylsBC0gA7ZyEJ7UdvrZ-RZw8Ib8-TqaY2TNszZo-ksIzkiXyG0Z70tGMzYogqRca05IanbwJfuzDdLzeXi63oNQFcxq5ToiyQzWWK1QxJ1DDLsunDJ2oAC3DDjFY0-VfXn_Y3XVVrw_SGMsNj3nUC8Ng5Ce_aABbElT7ug6mHWoD7PSpLK9PB3HLhx29ohH09aSdMV2ZBQ6K1uhrKKuijVP0f4H9pi1xwzzSC6ClaSFZevNUl4vNFy0woXdpekFGea3MnaTnXNtgxTWIs7iSvIvOnXYfMHynvt5tv2bWQkeGXeyeds-Z-WmXaAwo1-JaiFyxU3BDnOFA5ENMg2tANcPIM9rEUQXXk67gsfkdSk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وعده دختر دهه هشتادی به «آقای شهید ایران»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/447258" target="_blank">📅 23:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447257">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e97073945.mp4?token=tM6H09siUtLDBHb88qphxpEzn0HEHIujvlj570fmFu65J4HdLVbuCx4d0rRMpxysgO1B4o2q-3nSzRq5iUfw22msJbPuVd1pdPnXlet_lMafD7EIyPRVNiuUP_TwmZEWTRPEZ7BssCgNJv553xeLBA7dGwTFrXk0rjB4XInRh89SPzwovDVzrOgIWRQ8HCgRJBnWQp5azX8xRfAUHEXY6-7jwJSWMuYtuO8xsU5Hw3cmoHgKzpgHP6wbDQzwD5DAEP4007lcogzrENeKv5lWTuVvhiNpmO8j_ID78t2AoEa_14tNEe8XfTvvnQUBLSZPHpLJrz95-yHIOCSEQUU07g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e97073945.mp4?token=tM6H09siUtLDBHb88qphxpEzn0HEHIujvlj570fmFu65J4HdLVbuCx4d0rRMpxysgO1B4o2q-3nSzRq5iUfw22msJbPuVd1pdPnXlet_lMafD7EIyPRVNiuUP_TwmZEWTRPEZ7BssCgNJv553xeLBA7dGwTFrXk0rjB4XInRh89SPzwovDVzrOgIWRQ8HCgRJBnWQp5azX8xRfAUHEXY6-7jwJSWMuYtuO8xsU5Hw3cmoHgKzpgHP6wbDQzwD5DAEP4007lcogzrENeKv5lWTuVvhiNpmO8j_ID78t2AoEa_14tNEe8XfTvvnQUBLSZPHpLJrz95-yHIOCSEQUU07g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آماده سازی جایگاه پیکر رهبر شهید در مسجد جمکران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/447257" target="_blank">📅 23:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447256">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eefcd0c2b.mp4?token=C2FpHrdj7ON_ngKBX6YIEnYUE517nj8e0L5bQGWd6c9j8tiXdpczoaYwB5rY2HECqrs_dRzyqKGeHc7q06Zd6Vxb0XKN1VpwTQvrLliehXuC-93HTLhFAFjwEd_6EsbNkBP334fX9W4va_ojDinR83q8YoImhzQieQjB5RD7zVkXrZcdCicVlfOSfCQr_Goncb2Vwo33vug0GIo8y6rx0HzILX9Z8x8Sfj8Slf9aB7tGnMRjWdWHKpGBp2rk1fzpp1UUfzolZXWmD_YEza-e9nTmEmuBl7LJa1E-V7OkSHhSwsaeaFNi1X12qLqyaTzVLMdCqaOCGlkB5HkzSzoAjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eefcd0c2b.mp4?token=C2FpHrdj7ON_ngKBX6YIEnYUE517nj8e0L5bQGWd6c9j8tiXdpczoaYwB5rY2HECqrs_dRzyqKGeHc7q06Zd6Vxb0XKN1VpwTQvrLliehXuC-93HTLhFAFjwEd_6EsbNkBP334fX9W4va_ojDinR83q8YoImhzQieQjB5RD7zVkXrZcdCicVlfOSfCQr_Goncb2Vwo33vug0GIo8y6rx0HzILX9Z8x8Sfj8Slf9aB7tGnMRjWdWHKpGBp2rk1fzpp1UUfzolZXWmD_YEza-e9nTmEmuBl7LJa1E-V7OkSHhSwsaeaFNi1X12qLqyaTzVLMdCqaOCGlkB5HkzSzoAjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اگر بخواهید یک کار خیر به نیت رهبر شهید انجام دهید، چه می‌کنید؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/447256" target="_blank">📅 23:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447255">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02f93d2ec3.mp4?token=Cc4ukc6ZJ9jtUHwSMhrhPKLtKmR2BeLS8k6AjgadlHsmHwrgFU7GYhRNeyJjvVij4Wmkms_GSQvDbEAo049QmznY-HJQ9GyNR2ZDMM5_RYOBdBCmU3TGBdKWyodDG4fvVcWgAklCMjxc_1gIBjXMJDdN72tIhLbpvt4QrhSdKFweqFRly2Wrn8W2VHS9cJ1Td-cqwFxXeo514or-kwvspovs_x5txRMo3TfLXP8JsVr5vkj5NxFVMMgDmat2Jbez7OjRbv6AmGopKw_xhwWlFX_YLtRPSY48KYrBzFeEBBmewEt5lwhLahAg2VdiLPm5t0jGc5TCcEcv2O95w2JlFimFWeB0iiay3vfQHgngV6HWDKlLlsDzvS8ILpK5I6Xt3kxeETJ5If7ao65mmoMxF0xpFqb0qbUs0-DtqdzjcUivjtcQRluCkmkXce4wglGBOqNym4G606XX8BQCos-t8aiC3265MRToGroeM7gFhVaNi62gaUo6ek_uYAOwzA4EiTLLW1E3a0TYQdcRw0U6T2SRJrMpfOo-nnUQe8PRH2cYCNc3U6rOaMWiZL7IuueWuk7ZrA52sWjI77ERdydzJptYpeqfh_wHIMiQcZp8lW_dQQdU0UaC9AoDC-35cl27MiX4YWMKWJseE57RunhXOydvRRAG5-Q1pfCl70yc4OI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02f93d2ec3.mp4?token=Cc4ukc6ZJ9jtUHwSMhrhPKLtKmR2BeLS8k6AjgadlHsmHwrgFU7GYhRNeyJjvVij4Wmkms_GSQvDbEAo049QmznY-HJQ9GyNR2ZDMM5_RYOBdBCmU3TGBdKWyodDG4fvVcWgAklCMjxc_1gIBjXMJDdN72tIhLbpvt4QrhSdKFweqFRly2Wrn8W2VHS9cJ1Td-cqwFxXeo514or-kwvspovs_x5txRMo3TfLXP8JsVr5vkj5NxFVMMgDmat2Jbez7OjRbv6AmGopKw_xhwWlFX_YLtRPSY48KYrBzFeEBBmewEt5lwhLahAg2VdiLPm5t0jGc5TCcEcv2O95w2JlFimFWeB0iiay3vfQHgngV6HWDKlLlsDzvS8ILpK5I6Xt3kxeETJ5If7ao65mmoMxF0xpFqb0qbUs0-DtqdzjcUivjtcQRluCkmkXce4wglGBOqNym4G606XX8BQCos-t8aiC3265MRToGroeM7gFhVaNi62gaUo6ek_uYAOwzA4EiTLLW1E3a0TYQdcRw0U6T2SRJrMpfOo-nnUQe8PRH2cYCNc3U6rOaMWiZL7IuueWuk7ZrA52sWjI77ERdydzJptYpeqfh_wHIMiQcZp8lW_dQQdU0UaC9AoDC-35cl27MiX4YWMKWJseE57RunhXOydvRRAG5-Q1pfCl70yc4OI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدوبیست‌وهفتمین شب سنگرنشینی کاشمری‌ها پای عهد انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/447255" target="_blank">📅 23:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447254">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2407c70c00.mp4?token=jB2x7YUoyBiBpJBNK0k9VuZFnxFsP_fhKaEsPQdfg8Xygk9nuWmf89q8jdc1oI6y87rWh4CA9PlYelGmYhweE9IcYmFSUh9QlnLnPFd5glQR1L2R5_RhUxKGGNbuVFRTrkwQOwxU3YnzpOyjwku_pK73RpSWdqkO5ci8YVi8NAvsn4KE52nv-7n0dOeSRhTrcQSJ8zHF0IAfn6BsO9A38oLVVCOckrwkS2aMRD-eQLsIyM3fXoTuSiT0qAqivkiqrDb1bX9thmfFBhJ1trwm8anf6ZraOBm9YnoDe2MG0b5o1dDime-YEZm-VSoKNDw6BCqKEpfHShOUno8Pa7X9gjUxLMkMpMtaIXBVsF1_PqWkz3jPgAgfFTlC1utsr-BwBl9UnfTgYMQmzBuD_LmfRR4x-LVURBtdqLJ9Hr8nTuhxD_EVHEQ6FXmVjl3EmbdoltSeimMU_Kw6rF-jfIXIpVu_IOrV77K11hDqqxMLTFR14ip4JuYYrEJPgzMfX4pVMR81pT53kJ0uy4qIigjBRMTthFjqi6p1igg93QGhV0UU0pacrFSHbF7k-imECcwV5S7_OykfWUSuTPbIyQrwXBEmOpSRPrBr9iCYlC4GAAlm4k8aTFzcOsF8GrCdJgV0_dAzJhdYl8u3c8dP9BR4YlFD0UJwJA34DzCr17Ewq-0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2407c70c00.mp4?token=jB2x7YUoyBiBpJBNK0k9VuZFnxFsP_fhKaEsPQdfg8Xygk9nuWmf89q8jdc1oI6y87rWh4CA9PlYelGmYhweE9IcYmFSUh9QlnLnPFd5glQR1L2R5_RhUxKGGNbuVFRTrkwQOwxU3YnzpOyjwku_pK73RpSWdqkO5ci8YVi8NAvsn4KE52nv-7n0dOeSRhTrcQSJ8zHF0IAfn6BsO9A38oLVVCOckrwkS2aMRD-eQLsIyM3fXoTuSiT0qAqivkiqrDb1bX9thmfFBhJ1trwm8anf6ZraOBm9YnoDe2MG0b5o1dDime-YEZm-VSoKNDw6BCqKEpfHShOUno8Pa7X9gjUxLMkMpMtaIXBVsF1_PqWkz3jPgAgfFTlC1utsr-BwBl9UnfTgYMQmzBuD_LmfRR4x-LVURBtdqLJ9Hr8nTuhxD_EVHEQ6FXmVjl3EmbdoltSeimMU_Kw6rF-jfIXIpVu_IOrV77K11hDqqxMLTFR14ip4JuYYrEJPgzMfX4pVMR81pT53kJ0uy4qIigjBRMTthFjqi6p1igg93QGhV0UU0pacrFSHbF7k-imECcwV5S7_OykfWUSuTPbIyQrwXBEmOpSRPrBr9iCYlC4GAAlm4k8aTFzcOsF8GrCdJgV0_dAzJhdYl8u3c8dP9BR4YlFD0UJwJA34DzCr17Ewq-0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری مردم تربت‌حیدریه در فراق آقای شهید ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/447254" target="_blank">📅 23:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447253">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/712f858aea.mp4?token=LbDug6xGy5hW5DookPuGacZNWIfOXmx_w8N5RfiJWvl26x6PFb7PF8rQu7UDjBzDOlT2DOIxiarXCefBZ7MU_P47QYnwc4rE4ksOTrrv_mII7qFbfj7XyNtNrhBKnVbqDVbk3zDhp-sa7GdjPgNbSgHNAHcYwDoQm9ZsLqx8SdrSTYTWHuNLLQSmy3glYeGZxYWn9o8xgKAm8TEb_RX326sP8zh9GKjp_ILXkh8AQXhzLyVqCMwBITJTcptOalJnRsL8cr16WdgBARcYH_XQJdEAxlEcW_6GRZdSSAigKH7cU6CTDxAwKVeOCYgmJCS9dO5qOpERDZd_HdmXI0mYPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/712f858aea.mp4?token=LbDug6xGy5hW5DookPuGacZNWIfOXmx_w8N5RfiJWvl26x6PFb7PF8rQu7UDjBzDOlT2DOIxiarXCefBZ7MU_P47QYnwc4rE4ksOTrrv_mII7qFbfj7XyNtNrhBKnVbqDVbk3zDhp-sa7GdjPgNbSgHNAHcYwDoQm9ZsLqx8SdrSTYTWHuNLLQSmy3glYeGZxYWn9o8xgKAm8TEb_RX326sP8zh9GKjp_ILXkh8AQXhzLyVqCMwBITJTcptOalJnRsL8cr16WdgBARcYH_XQJdEAxlEcW_6GRZdSSAigKH7cU6CTDxAwKVeOCYgmJCS9dO5qOpERDZd_HdmXI0mYPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت شنیدنی کمیل خجسته، برادرزاده همسر رهبر شهید از اهمیت دادن رهبر شهید انقلاب به نماز اول وقت
@Farsna</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/447253" target="_blank">📅 23:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447252">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/486ac6fc3f.mp4?token=XzAeiavoJVUhoRZYn1sT1RPyW-Q-YAWggiFeHU79S3zsZLbfBOx7mvoLvDmFACjEVneOuX4Adg8OOj97LTzJPqTh5d3iP8BvT9hfpEJ0kXzENMwOPOJFFMDZ5pCzM-gtAZrbh1Xshi-Pnq3vwROY-2SiX9lL-uhTI6oHRZg4rwVTqUpw8y6qr-8FOAFFRz8EbyEOKWV3etH-lBNTUdxJFjXZctNY-ISGHwbyADcUjBsoiJDpnpjH12MGS7R0eJT7cg4CL_YxtvpnB9FnRkiffdN4TUsdktEaQQZ4ZPcGWVkpzrYIyAkdNPONQQiAQbSm2E-6Cx8EFgTy0kKJj4oC0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/486ac6fc3f.mp4?token=XzAeiavoJVUhoRZYn1sT1RPyW-Q-YAWggiFeHU79S3zsZLbfBOx7mvoLvDmFACjEVneOuX4Adg8OOj97LTzJPqTh5d3iP8BvT9hfpEJ0kXzENMwOPOJFFMDZ5pCzM-gtAZrbh1Xshi-Pnq3vwROY-2SiX9lL-uhTI6oHRZg4rwVTqUpw8y6qr-8FOAFFRz8EbyEOKWV3etH-lBNTUdxJFjXZctNY-ISGHwbyADcUjBsoiJDpnpjH12MGS7R0eJT7cg4CL_YxtvpnB9FnRkiffdN4TUsdktEaQQZ4ZPcGWVkpzrYIyAkdNPONQQiAQbSm2E-6Cx8EFgTy0kKJj4oC0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#فیلم
|
به پایان آمد این دفتر؛ خاموش‌شدن چراغ‌های مصلای تهران و آخرین لحظات وداع امشب، با روضه حضرت سیدالشهدا (ع)
#باید_برخاست
@rahbari_plus</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/447252" target="_blank">📅 23:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447251">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15ccb9daef.mp4?token=X-wKnJVs_5VdAv8GToJSf-byOHLQ8ubAa0XxeqwSG71ygwzxHixRIv996uU8DTG5_l7ttCs5bCCjHrrDgY8gGsCWNlJbs2f_9euEj8L_5oTB-j1xb7krlgtM1plp6M03YNgtlGKqxmSb7bGt7Vr9pHDulGGXB1eUTzPRtbe_D4vJrIYePlwwvVv3tA_B9SwQ-xBp0Fn8dl-OPuwznqtznJOnj-zRUc2uU-oIjzhywqgnI3UJvyzzkbSzMWyh0insMpLq9Qr3kxUNnInSjGMHhWysbtLvws16dILl-VOxxw0ezP3p9UnMSjrZ4-_m7u1AS45LTHpzBclypBcFJ_SQag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15ccb9daef.mp4?token=X-wKnJVs_5VdAv8GToJSf-byOHLQ8ubAa0XxeqwSG71ygwzxHixRIv996uU8DTG5_l7ttCs5bCCjHrrDgY8gGsCWNlJbs2f_9euEj8L_5oTB-j1xb7krlgtM1plp6M03YNgtlGKqxmSb7bGt7Vr9pHDulGGXB1eUTzPRtbe_D4vJrIYePlwwvVv3tA_B9SwQ-xBp0Fn8dl-OPuwznqtznJOnj-zRUc2uU-oIjzhywqgnI3UJvyzzkbSzMWyh0insMpLq9Qr3kxUNnInSjGMHhWysbtLvws16dILl-VOxxw0ezP3p9UnMSjrZ4-_m7u1AS45LTHpzBclypBcFJ_SQag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خدا صبور کند در غمت ما را
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/447251" target="_blank">📅 23:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447250">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e141fcec4.mp4?token=H9X_zFLfNdcadA2CJSOw8NOMy_tbDMsVqQGRz_LsHO_ZQemhc5n5PHQwdlmtnZXl6-YzJiJI_RXqjNLhzsLJ5ffFZ9r95oTuy_1oEhQYHCwgR8znRgW0uI3Dhbe-Jo4GeF8VHGiCIg4TxY9bA6lOYdDrLqrBIIMqGaWcU41Wf4PlHguSBuHk0oJKwLibFFH1cDuo-u9KZhGIZ8ONZ7MY-O4OwX8EObUsmK_BAF2Uq5d4nmM6S2-pU5uJrJzxhi2GZ10bLzERCzulZJrj_7OF_pSRg3mX-0i7acARJlUwPWGn5ZPiV43_K8xulehy834tyTXZZeBUY01W83WKDGrGSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e141fcec4.mp4?token=H9X_zFLfNdcadA2CJSOw8NOMy_tbDMsVqQGRz_LsHO_ZQemhc5n5PHQwdlmtnZXl6-YzJiJI_RXqjNLhzsLJ5ffFZ9r95oTuy_1oEhQYHCwgR8znRgW0uI3Dhbe-Jo4GeF8VHGiCIg4TxY9bA6lOYdDrLqrBIIMqGaWcU41Wf4PlHguSBuHk0oJKwLibFFH1cDuo-u9KZhGIZ8ONZ7MY-O4OwX8EObUsmK_BAF2Uq5d4nmM6S2-pU5uJrJzxhi2GZ10bLzERCzulZJrj_7OF_pSRg3mX-0i7acARJlUwPWGn5ZPiV43_K8xulehy834tyTXZZeBUY01W83WKDGrGSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین سلام به رهبر شهید از زبان امام رضا علیه‌السلام
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/447250" target="_blank">📅 22:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447249">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d300c6813.mp4?token=IGbagwxgL08zpEbLUbCRVAReqACG5p2Mk9cDO4TmW1vCzonpmlIEqVV5bzNktyUORLaES9BKSbHQzCq_hg8fjNCiWnOaqMGs6ptIWDIF1jrnZfMNMm94jfLZrcoO58r20fi-VxSjCrj9ZbeYqKAd6bixVDMuUrek43jphAfHaAI4PRzsJK1-sYeoV2tKO0rQ6dQIW0nZhdDNv5gAnDXP1l5382PP-v35r5zW4f8NdOB2OnOdK_HP9zL_9lJinwbqnJ5suo_2H5PGyQcn8n9cwK1NXnJwtUunX6MQ1YS5Cj7XNpL8woTnbR0CeyWu8T73c6qzJjBrBDIsj6KZQp5irA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d300c6813.mp4?token=IGbagwxgL08zpEbLUbCRVAReqACG5p2Mk9cDO4TmW1vCzonpmlIEqVV5bzNktyUORLaES9BKSbHQzCq_hg8fjNCiWnOaqMGs6ptIWDIF1jrnZfMNMm94jfLZrcoO58r20fi-VxSjCrj9ZbeYqKAd6bixVDMuUrek43jphAfHaAI4PRzsJK1-sYeoV2tKO0rQ6dQIW0nZhdDNv5gAnDXP1l5382PP-v35r5zW4f8NdOB2OnOdK_HP9zL_9lJinwbqnJ5suo_2H5PGyQcn8n9cwK1NXnJwtUunX6MQ1YS5Cj7XNpL8woTnbR0CeyWu8T73c6qzJjBrBDIsj6KZQp5irA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گوشه‌هایی از مراسم تشییع پیکر شهید مصباح‌الهدی باقری، داماد رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/447249" target="_blank">📅 22:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447248">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64e84926e3.mp4?token=dEBZKTOvF_m-d4AncW_iKmWHQpM9FQOFsFrbvb3euap20wLGtmTpTg3Pbn2R8Jrbw5ixz5ZZH3KUEk_WsLkRrDmL2fAt8-LxLWdrshgB8MTyykyP8jTL94LGORbDT_MV8WhM_73zPsif5QULDZucnQ2-P4JWAtx8qF3M9aDpPfWP-cAG67gFzLtMW_9ejC1JUKqwGcH0RdrkVWgvYIUZ4jIK9lLqWr3G8enKSnnXe69w9ZE5JySkbm_A_a606t5hSnGB3hxRweWzfXqRoB589juLxwHQFLKNHwNNuyREhtVGZiWGMOJ5BLJTu0BCwMCUWmB5Buc6uV1xiF_zxkw7BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64e84926e3.mp4?token=dEBZKTOvF_m-d4AncW_iKmWHQpM9FQOFsFrbvb3euap20wLGtmTpTg3Pbn2R8Jrbw5ixz5ZZH3KUEk_WsLkRrDmL2fAt8-LxLWdrshgB8MTyykyP8jTL94LGORbDT_MV8WhM_73zPsif5QULDZucnQ2-P4JWAtx8qF3M9aDpPfWP-cAG67gFzLtMW_9ejC1JUKqwGcH0RdrkVWgvYIUZ4jIK9lLqWr3G8enKSnnXe69w9ZE5JySkbm_A_a606t5hSnGB3hxRweWzfXqRoB589juLxwHQFLKNHwNNuyREhtVGZiWGMOJ5BLJTu0BCwMCUWmB5Buc6uV1xiF_zxkw7BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رانندهٔ این تاکسی، زائرانِ رهبر شهید را رایگان به مصلی می‌رساند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/447248" target="_blank">📅 22:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447247">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuxDWacRIMTHsbblHQ988pMZn2gxTCdRO39Of3OU40lA1wbL6Noi2N_DUOwpst0a9c797kiWo3a9n74BrxtU_fgVe7YCBbBz5qEYdY3x-GXorLkgWru4Yq4bbGguIx7mA8IhfcGgAB1XsaGoh0QyPuuI-njs7-8ZrSeJGB-ghUPl_w093BCHOMKnVgFvZEIgriCL63-Qz4hytYB0H5BBNF_iL6EkIx_M3nDqkeXlcayRZGkZoDnDMs8Z863jK3qkDjwxMC-49x289nSo9L-pCaLEJl5YrcKPsWGRcwvl0RAqZnlUSpa1-8-YppHZuV5cUx6cmzJBx0QVi4TdCYW6yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: دیپلماسی به دنبال تثبیت دستاوردهای میدان است
🔹
رئیس مجلس در گفت‌وگو با‌ محمد درویش، رئیس شورای رهبری دفترسیاسی حماس: دیپلماسی و مذاکره باید بتواند گره نظامی را باز کند و دستاوردهای رزمندگان را حفظ و تثبیت نماید و این مهم زمانی محقق می شود که کشور…</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/447247" target="_blank">📅 22:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447246">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
مردم در وداع آخر چه عهدی با رهبرشان بستند
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/447246" target="_blank">📅 22:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447245">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7df973e0e.mp4?token=rOZs9mQmJhHpWJQvqFXj_JcJM10kVljaZN2ccWXEN6fjkarU7i5f9CVgpxjRnltwfZrz847623D97-Ic7IXy0n3lqqENpuh9_SGyJA4vvTSwYcFGsFMBalPRbLU0XHp3sOLNwb9PG-_0WYnkDA3dSya_7NOaRZLodjgimM3uA77i2vhe537uTjdN6pzzNK02gge9XunOGiO4_EVscu3jvwO4Mcmup_TcRTl-kckGDKL_Srxs5lJsdDkh-VEWqe2vgff_9SPfjTFTgjd2S2MJf6frd1xuxzyHuMdQkYllRSwvfi61UeVTklLyuGLxcaq4ADNZPQKvb49uEpGQ-0jU6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7df973e0e.mp4?token=rOZs9mQmJhHpWJQvqFXj_JcJM10kVljaZN2ccWXEN6fjkarU7i5f9CVgpxjRnltwfZrz847623D97-Ic7IXy0n3lqqENpuh9_SGyJA4vvTSwYcFGsFMBalPRbLU0XHp3sOLNwb9PG-_0WYnkDA3dSya_7NOaRZLodjgimM3uA77i2vhe537uTjdN6pzzNK02gge9XunOGiO4_EVscu3jvwO4Mcmup_TcRTl-kckGDKL_Srxs5lJsdDkh-VEWqe2vgff_9SPfjTFTgjd2S2MJf6frd1xuxzyHuMdQkYllRSwvfi61UeVTklLyuGLxcaq4ADNZPQKvb49uEpGQ-0jU6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دردی که حتی کوه‌ها را می‌شکند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/447245" target="_blank">📅 22:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447243">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفالس نیوز</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YYgOIwfrDsfO-tn4xqrRSQu_SuG3J9K1EM_9YovpQFMUFApvctAOrngm-AaOP2YEY0R6QGWjeTjaSNbZ6CY-UqAu8sYrmcKQSqtPn3BeRiTs-NW3__TTeLlht6xPO4fE3rXlCsYcx1Y2Tajcd17-K9Rp1WN0Lcq97_MQo48c_BgEbNYhzDMKSE0bRKHAE-NDnGqSID5ciONg8WFdRL3f0NlTpaqrjHN8AM5_wrInTEFZTeJsNx10DieMkHaBbIItXc1T9al9US1aljHvIBw9yrqlST2Ki-vyutp2RF1RYr1f3smYL-T_LXrfLOvXPwLm4BD4zeM7QnH6r8cmJKJw2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LKujN3EWMiHbT4iVvR4ttIxrfRq_PhzKm_XccGCQaI3CZLkPl8nUmfc-MPKjjIMYxs-ekYtlBn6cXMsj1dfVUMEjkXWjC7i5C2b5QC9Metc2bsMT2J2FRwxKOdJ26SvQlBrUhEQBrKMUe29ckBTLgz95I8SqPQMS-SoBgRRWr41m7HjvFm2LsklMidOtRP2J5K6Ci6FFZzLdp9tgC4gYPfPZ3ldtL6H9E3vte6MenOxddgTrmbq5Vh2UMVoS8HEwH5zVggvL6Ft9i5ErYzfBVXrzDhwwfzz-a1c3rhTr0p_A1mYiqRjh_FsQ3vdWQP4K9mxOTG_rQ5SWmSNx_hHcwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبر اختصاصی اینترنشنال درباره رئیس قوه قضاییه هم دروغ از آب در آمد
!
❌
در ادامه تحرکات رسانه‌ای اینترنشنال و فضاسازی‌های ضدانقلاب برای هموارسازی سیاست‌های آمریکا و اسرائیل، این رسانه چندی پیش مدعی تغییر ریاست قوه قضائیه شد.
❌
اینترنشنال در راستای اختلاف افکنی در خبری اختصاصی مدعی شده بود: [آیت‌الله]مجتبی خامنه‌ای اژه‌ای را پس از پایان دوره پنج ساله ریاست قوه قضائیه کنار می‌گذارد.
✅
این درحالی است که آیت‌الله سیدمجتبی خامنه‌ای  رهبر انقلاب اسلامی با صدور حکمی حجت‌الاسلام محسنی اژه‌ای را بار دیگر در سمت ریاست قوه قضاییه منصوب کرد.
@Fals_News
-
Link</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/447243" target="_blank">📅 22:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447242">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🎥
ویدیوی حشدالشعبی برای دعوت به مراسم تشییع رهبر انقلاب در عراق
@Farsna</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/447242" target="_blank">📅 22:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447241">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef0be33eb3.mp4?token=pG1P9tNkGet-dW69w0hbBNIL77iJdLafVyR_2A2syJ7GbRunb0sdKqWeBzYzPGEB7DDdW46xD3nGu90xue_joLXO1f91c1EJ1rf2i3es2arHYg3mHiplzcO2SYQtrRAD0PhjlGGMfDCWrDTPVr2gFvm8jkbjxuvf4do-WrEEOpY4GSjOLsnFIbT6kT8RmnEnWVO5-cNkc3zS_VjdHR-SHKsQB8Grd0EmuJU0bLoBIKp_mYWLUiDDoiofcVEZ5x56ef4SpqZ5CYGrmZpV-8uH6XJkQCYLtuWtYIv54RqX2UDZdAAW0K0lRYohN48jJbZ6nnJ_npEOak2I2QSQtKzMsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef0be33eb3.mp4?token=pG1P9tNkGet-dW69w0hbBNIL77iJdLafVyR_2A2syJ7GbRunb0sdKqWeBzYzPGEB7DDdW46xD3nGu90xue_joLXO1f91c1EJ1rf2i3es2arHYg3mHiplzcO2SYQtrRAD0PhjlGGMfDCWrDTPVr2gFvm8jkbjxuvf4do-WrEEOpY4GSjOLsnFIbT6kT8RmnEnWVO5-cNkc3zS_VjdHR-SHKsQB8Grd0EmuJU0bLoBIKp_mYWLUiDDoiofcVEZ5x56ef4SpqZ5CYGrmZpV-8uH6XJkQCYLtuWtYIv54RqX2UDZdAAW0K0lRYohN48jJbZ6nnJ_npEOak2I2QSQtKzMsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام پناهیان: اگر حال‌وهوای امروز و دیروز عاطفی‌تر بود، فردا حماسی‌تر خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/447241" target="_blank">📅 22:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447239">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f921ab159e.mp4?token=rh31q-SjbaA4Q3LYUE012kU7R7DP01gsOaEWZyRLdKn18ogj2ac0cdusKjmcnrWQhavr_QkyEnHwoKkFSxInpMQ8uT36YnwYkGJqjK74ib-AnB7iGJ3st0jEVG_FuTMsKQNMVp8Jg0pa5lgKGBdKPcwVtRzfLHwmZ6aIkcVFI94H1jJCnCbqcqyg6W11b8NKRGkwn609anjj_0dTrb2XI6rnOS9H0zA6B92yLWYLW5O4WlimkRD_Ux3PFFHyueH16QwUmA6qgVmoz3-5eHlb0bB7hUQZfK9StiVHLdzSMJlJZvcfyPxP32ZOSVnjMNkdTkheReNqJYkqQ-bziK2Tig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f921ab159e.mp4?token=rh31q-SjbaA4Q3LYUE012kU7R7DP01gsOaEWZyRLdKn18ogj2ac0cdusKjmcnrWQhavr_QkyEnHwoKkFSxInpMQ8uT36YnwYkGJqjK74ib-AnB7iGJ3st0jEVG_FuTMsKQNMVp8Jg0pa5lgKGBdKPcwVtRzfLHwmZ6aIkcVFI94H1jJCnCbqcqyg6W11b8NKRGkwn609anjj_0dTrb2XI6rnOS9H0zA6B92yLWYLW5O4WlimkRD_Ux3PFFHyueH16QwUmA6qgVmoz3-5eHlb0bB7hUQZfK9StiVHLdzSMJlJZvcfyPxP32ZOSVnjMNkdTkheReNqJYkqQ-bziK2Tig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ وداع آخر با رهبر شهید در مصلی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/447239" target="_blank">📅 22:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447238">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa3203834f.mp4?token=N-qV0Grk75vp_V2X1-1_PE3YAz4_yquCyNiU8P703u60wAy9BmNBCMs9rhK2NVsrQfAmy5OGhqhA2RklrL48J_5xBQamc0L5IQoCkZJcPgTCeK9ffD43FEOR0t5TPWWQ2wRVgY5tZqWn3_2I21AIJBxWULoZz8xMb0kqTPmRZoRye8V1oV6_BC0v_AVHIK-fpaf3JNBvPKqOHVSWS0e9IPpZVAyW1yvROXVxzx8BDuLZjFqompgUhxEB8H7iYLoCSCV28I7KJAwGlxTIaJHPdLgBhy4z89ljvLO_rDuk_hyT6_PnG5X1z-scsybzxcw39ZMU4rw1QlHGusmoj-BqfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa3203834f.mp4?token=N-qV0Grk75vp_V2X1-1_PE3YAz4_yquCyNiU8P703u60wAy9BmNBCMs9rhK2NVsrQfAmy5OGhqhA2RklrL48J_5xBQamc0L5IQoCkZJcPgTCeK9ffD43FEOR0t5TPWWQ2wRVgY5tZqWn3_2I21AIJBxWULoZz8xMb0kqTPmRZoRye8V1oV6_BC0v_AVHIK-fpaf3JNBvPKqOHVSWS0e9IPpZVAyW1yvROXVxzx8BDuLZjFqompgUhxEB8H7iYLoCSCV28I7KJAwGlxTIaJHPdLgBhy4z89ljvLO_rDuk_hyT6_PnG5X1z-scsybzxcw39ZMU4rw1QlHGusmoj-BqfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اللَّهُمَّ إِنَّا لَا نَعْلَمُ مِنْهُ إِلَّا خَیْرا..
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/447238" target="_blank">📅 22:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447237">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d2881a783.mp4?token=O7hcREtrkQHgipkYXBhXDk9jBTU9LCPzR3v3sWuBoCzMNu-YtXMz55xaFzpvjZamJK21bYxPaqdimS4sJ-kPe361HQeugOfNmorGXhpN47YSefTSHSAY4n7CxLSkHkV7SG3cKlYXX69sO5x2iZqLbLsJD8pthf5fLxNIwYlp3tyhCR8N27-daroTDTC9PYQmGTHtMxvKzzWlDRfEj6FMbJZvvEQwxXvpkiufyKuMsiPSBSVhK8vmkULLl0x2kzNRSMREuGLA0h-3d2TJQrJvXu0k7AzRf9FzsKGxV9ncRa_MGNWBZbXVO7n12-r2EtHkULIuQ62sj2vMRIOTu7kQmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d2881a783.mp4?token=O7hcREtrkQHgipkYXBhXDk9jBTU9LCPzR3v3sWuBoCzMNu-YtXMz55xaFzpvjZamJK21bYxPaqdimS4sJ-kPe361HQeugOfNmorGXhpN47YSefTSHSAY4n7CxLSkHkV7SG3cKlYXX69sO5x2iZqLbLsJD8pthf5fLxNIwYlp3tyhCR8N27-daroTDTC9PYQmGTHtMxvKzzWlDRfEj6FMbJZvvEQwxXvpkiufyKuMsiPSBSVhK8vmkULLl0x2kzNRSMREuGLA0h-3d2TJQrJvXu0k7AzRf9FzsKGxV9ncRa_MGNWBZbXVO7n12-r2EtHkULIuQ62sj2vMRIOTu7kQmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت علیرضا دبیر از دیدار با رهبر شهید انقلاب پس از کسب قهرمانی در مسابقات المپیک
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/447237" target="_blank">📅 22:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447236">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/789d4d5328.mp4?token=oNgz5XIo-Vk0WL-Be7gIvltwnJnAy-PKzYBk__OXHYoqkiJWi6_1uVUTyD-mG6rZtQ-WPOYi5xuka6cWGCUDyUVtlrQO7tfA_7P3Y5xlhCONlMyZfNrssYZRL-WnZ3Y2yYQQFXli5-4QyaA2Qe7sR-vd9lcQ04vj_fYHgWm--6niUIC8cJ1dly8TmakJCCadM3HcIgdkXDDC8EIQZHAH_f5W5hcPLpR4LYFzFRN10UTw0Fyoy6EyI3ovyml28YNbqt4rECj63t3_9fnbZuEZsJAF14exgCUmQHiFkXKhd7l0_hXGieNevSzg9Onm81rJMud2Efv66uTEk7idyCUcor2j9C6XBWk0u3TUCh3Ik_81Yb-ihsPI8t8I5QU7KP8rsD-Bh5vgZMioFSTzEogpdkFZgKKFsOtLoerbxIPwHrC0bynGC-yvH6FCD8bFXYvbnHW6KdLhbyiFxAlG_hV480FCkARE35f5f395LXAE2-oRt2BrCGda3BAU2VeQ94pIMO6Ke5VIUHmnN21jyV3KoBqR1JZZ7c-GLVK1msiamU_tmAYvmAl0aQx5Y24DxjqeBYmLCh03eOBqLMctSugrcIXKJuSNbz3HQfv0PGQO3rF9FzeG9CIYVtIg217AUvn5JR3I4ggOWcibvi_-Tsksra926hf3OZgM9qaLHfbUDGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/789d4d5328.mp4?token=oNgz5XIo-Vk0WL-Be7gIvltwnJnAy-PKzYBk__OXHYoqkiJWi6_1uVUTyD-mG6rZtQ-WPOYi5xuka6cWGCUDyUVtlrQO7tfA_7P3Y5xlhCONlMyZfNrssYZRL-WnZ3Y2yYQQFXli5-4QyaA2Qe7sR-vd9lcQ04vj_fYHgWm--6niUIC8cJ1dly8TmakJCCadM3HcIgdkXDDC8EIQZHAH_f5W5hcPLpR4LYFzFRN10UTw0Fyoy6EyI3ovyml28YNbqt4rECj63t3_9fnbZuEZsJAF14exgCUmQHiFkXKhd7l0_hXGieNevSzg9Onm81rJMud2Efv66uTEk7idyCUcor2j9C6XBWk0u3TUCh3Ik_81Yb-ihsPI8t8I5QU7KP8rsD-Bh5vgZMioFSTzEogpdkFZgKKFsOtLoerbxIPwHrC0bynGC-yvH6FCD8bFXYvbnHW6KdLhbyiFxAlG_hV480FCkARE35f5f395LXAE2-oRt2BrCGda3BAU2VeQ94pIMO6Ke5VIUHmnN21jyV3KoBqR1JZZ7c-GLVK1msiamU_tmAYvmAl0aQx5Y24DxjqeBYmLCh03eOBqLMctSugrcIXKJuSNbz3HQfv0PGQO3rF9FzeG9CIYVtIg217AUvn5JR3I4ggOWcibvi_-Tsksra926hf3OZgM9qaLHfbUDGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیعت مردم با رهبر شهید در لحظات آخر مراسم وداع
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/447236" target="_blank">📅 21:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447230">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dGY8WuhipwrZpacT-9WPuFLxbPiJzYm8qMtvC9pMWTURZajgNrVFxr4aAvR3cptYZsYwMghwFy-3bbbBf3iFukikqKxys7kDoxAqXW9VL_eoXZID3EHBM1uX4L7IkGlnO275hNk0A24x6u0HnAj-hBwZv2MrNpXsa-JQb3HtE7CDZ0we_O7pHzJ87kEj4-Q_p73VSKnDwiafP9qWuxJZpmr8knktYWD18f7CFgKHAatHa2_CQ2uTYCb0jp8WrJF3QETE5HEnQb88XFIKW3SZV_NRXkYrW9-15ablz3WuXWS60IcYYq25cE7-O25gcoYIGoML7zZ-B5VF07P5UIpWBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QfFVhOY64TSXTF3gC0gUvw1XemXXs7tgahV9JoZ0gUYN2pnuUl9W32tRgH7W3wwH6laxLlpnokE0V64c2z9a8Wz6AJJdICEBCU88SbdaWbVw7h3iEdhQoEXFm-KKxzk2UftVUDXY_YD0aHrBYBPJ7HcswEJBXTMcHnIuuC_jo_njvZxmpq9E7873LXyJGjdOtc5HVM9NuJTt9Lt1Exu8xUP2DnFix1dOvlY6I9ggK2KNEyHVtZdwjdF3Hg1ZERVaF82oKowgd1u0e8NiMWdefJBg3XMiRzbXmAnVT3zqRQejVAhHeuKIk_XEei1EGec7Bo4546xq3HH1fnyx2MvlOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sdvCPeuN5Pu9qxZajcTJNQur1vCNCdIaP4tjEaVBGs29TltqNeK4ihtwSgJMIr1coaaDB7VRNk0VO66kFlBf6-pX92p5bKeDAE_i0JFa21K5kjtV494bpndYbvXkG-qsUemd79DMng2fvf1YmQ7g9YwyILLRTj0hSMg5bxNqmvisJoQcqtV3NVj7mdI29IEm5fHw-yU3qU5WhxGnQMuK4Npkg2mL5UnKJbM_YnR2SFVIuiPTXk0TeudnobaD1iVZgvihgkNFG59NZMaJjemTHQhwp8InhKXBcruV3AwZiRm3LBX_kAh-1ya1K6PF2rN_p7aJ8U-XULNW_fInhGvtrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kodiRcjcKW0102kJCuDjq2uzJ1Jwb1eAkBS6y8kApVZ3H8Dfpt_tRPvL2SDJTi_35uuWV7gXE9kD5-6joGelW4-GKuGMB-W1RLpt1VQ9xrxAbmdIl8PSBxt_cOXN16i_at8b8nM_1MJF8D7CoaWuRWpk3iEQ2rm9qfu_k8zuTNPs9pPUrik5Qj1UO_RkfnXRPYBaGxpucXMySrxWq_kBpb3qZZO1ghPBPmF0KoI8vUf7S2NMLpkLBMcmHwnuXPTIYAozh-MenLTczR3iNVSRaMxAaIWfG9skfK9vRRgWTA549Ach0R9W2DPQYNwQDe2-4He1InA7TV54QPCRtP4ICw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bZ1_GHvqbFzbdSf8zd8JaTgfargCnJLpBXjwPfnAtVN-SFXeih14ahDCmRzXjdHA0Y7OPMWl-rv4CS4W8NqEyhvkrXmKYxYddy83TWdpRDlgO4Hrghlh-h9V2fy8-hEGgPsSnZYg2TmJlHQ0U1eclXl8TjH-kg2hzuVFN6ATriiIxsQdzZA20ojz1ruV_QeIXs8ETcYTKaHiL2Q4qt5oKI1AajZToc4oCsFeVfVJ-llmHUB5fGFl5SGFPUcy25JQC-vz9L-XS5bZ8pMBPEnzQIYLl0iyYfnQSMrwd-pC_PtFJZZ8ZJ-aXQ9Kn7Rxh02G6nkqncVO5v-87EZ12HOvEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SvN6ZpJcKTUIOwEQMKvA__pBwrtfXhuDzPZeAikRTFF345HkMvaGF5g6ayIJYAQxTPJEDVvgj7Q-P6YvusMECB_MC11LEjHlno5r9Ia3M7M-n2dlUadZmuMTnA49bJFPU3Fs14amk-PHHJSGRsjkBvdvCd595z5nV7I2p8eQYq3vhMdEMEt33O5IGvntnfSHipo7h-XEHSV4gEjeQCQ7GgPVxXet9s_V5OLnZX75sNRL3liwiCLYTuq9sNeZvj9czrIe3b5BP2_yW21ZpPJKwvdAGeMwgU36jwPbUyN08Jogk5sgggKuuA1kVbsCpSUEVQZM-C0X-a8JxzrP8s-NXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نگاه‌های بارانی به شهید قائد امت
عکس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/447230" target="_blank">📅 21:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447229">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63ba4e6e6d.mp4?token=EOSE_jncZILTbi4Kc6gv9MBYAraRDwWl060C87hhqijCD6yvV_F62VUCESBY7fgYSMt8-jwgu1P_tt7pKZbW1_do5PscsJ9fPGUSDMSze8VgC155ReU132IlS4CwM_LSVZWtzkXY54f08iNeMS23ohnfT6okxHFXjRjrrmdCubBori0xhAvTYq39yf1KEwK3uEmaPUf0KRWGovrvkWmr6nhYmu_4xq-cddKo8IKdnptEMJvobgngCo7jja26Urs7yl1kPLR_2xWLf0-Jl1g1Xe8k40qXtBGjSi0oHZIYxFrxU4Ni2gjf8SmM9N0I-UN7O9nGfiFO3UAKV9XpLTixrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63ba4e6e6d.mp4?token=EOSE_jncZILTbi4Kc6gv9MBYAraRDwWl060C87hhqijCD6yvV_F62VUCESBY7fgYSMt8-jwgu1P_tt7pKZbW1_do5PscsJ9fPGUSDMSze8VgC155ReU132IlS4CwM_LSVZWtzkXY54f08iNeMS23ohnfT6okxHFXjRjrrmdCubBori0xhAvTYq39yf1KEwK3uEmaPUf0KRWGovrvkWmr6nhYmu_4xq-cddKo8IKdnptEMJvobgngCo7jja26Urs7yl1kPLR_2xWLf0-Jl1g1Xe8k40qXtBGjSi0oHZIYxFrxU4Ni2gjf8SmM9N0I-UN7O9nGfiFO3UAKV9XpLTixrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام میرهاشم حسینی: مسئولان در صورت تکرار تهدیدهای دشمن، پاسخی محکم به آن‌ها بدهند.
@Farsna</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/447229" target="_blank">📅 21:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447228">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1bc4a7fe9.mp4?token=HlKh4yxTBO4TtCgTUyWmZ224wQuCKdgcCbg9R4aHvJkffgMClgGOyNKBZxv9WE0x380fBPpuycy0eBYEqmNx19CYIUonYP1H1IS3GJcZOigit-VLyXQmSzhKn52bEXlU9ZLpsKsMLb5vZmqUGAVgMr9KhcPVy9nDuNyUX9MEqvX9N4bdDQXdG9ho3GBQ4QF3xSLSvP2T78wlCq21iE02rMMo0oe0_vM3AFti-TCXUyfTa-Sgf3Eme5vk80pUFWVd6T0Hq7PZqlcJ6kytN1ysqg40Sf45qH27J9eotI74gUBbaKjNySiacCDXBY_cabet5mlzDwg8PAfYi9lCiN54yTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1bc4a7fe9.mp4?token=HlKh4yxTBO4TtCgTUyWmZ224wQuCKdgcCbg9R4aHvJkffgMClgGOyNKBZxv9WE0x380fBPpuycy0eBYEqmNx19CYIUonYP1H1IS3GJcZOigit-VLyXQmSzhKn52bEXlU9ZLpsKsMLb5vZmqUGAVgMr9KhcPVy9nDuNyUX9MEqvX9N4bdDQXdG9ho3GBQ4QF3xSLSvP2T78wlCq21iE02rMMo0oe0_vM3AFti-TCXUyfTa-Sgf3Eme5vk80pUFWVd6T0Hq7PZqlcJ6kytN1ysqg40Sf45qH27J9eotI74gUBbaKjNySiacCDXBY_cabet5mlzDwg8PAfYi9lCiN54yTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مداحی عبدالرضا هلالی در ساعات پایانی وداع با امام شهید
@Farsna</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/447228" target="_blank">📅 21:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447226">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
برنامۀ وداع در مصلای تهران به‌دلیل ازدحام جمعیت تا ساعت ۲۲ تمدید شد.  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/447226" target="_blank">📅 21:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447225">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f38f101ed.mp4?token=b4KJT0TgxRJf7y_IkAJBJJKm24L_CquY4OsS0D5-ItWpZVfHdzSFMJuNunvqJm7Thdk3RBC-QfEVZOc7B7wOy8in67Mhu3ngTP2oOr9bGI_pN099LqnlSCPeOb_GBv5dp7UjjY3XChUQPBCSmVhYeuapXbELEArgNFYBWgdCM54srgh6_A2hLwk8aWuLFS1HafZbQBTmcUhGtX5mRP3EELhblc0FhdmzPryOS_zFlVDcjuQShVJ_aK_JoK3SimYbonIYGpDecmzPdkt_e7GYxVcar381XIHOLOkxgOjJDBeiTwhPZqP4jS2mJHemKrYpcRwBD22GPD58DQo0aNaFBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f38f101ed.mp4?token=b4KJT0TgxRJf7y_IkAJBJJKm24L_CquY4OsS0D5-ItWpZVfHdzSFMJuNunvqJm7Thdk3RBC-QfEVZOc7B7wOy8in67Mhu3ngTP2oOr9bGI_pN099LqnlSCPeOb_GBv5dp7UjjY3XChUQPBCSmVhYeuapXbELEArgNFYBWgdCM54srgh6_A2hLwk8aWuLFS1HafZbQBTmcUhGtX5mRP3EELhblc0FhdmzPryOS_zFlVDcjuQShVJ_aK_JoK3SimYbonIYGpDecmzPdkt_e7GYxVcar381XIHOLOkxgOjJDBeiTwhPZqP4jS2mJHemKrYpcRwBD22GPD58DQo0aNaFBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استاندار تهران: خدمات ۲۴ ساعته مترو و حدود ۴ هزار اتوبوس جهت تسهیل رفت‌وآمد مردم در مراسم تشییع رهبر شهید فراهم شده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/447225" target="_blank">📅 21:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447224">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34db08e600.mp4?token=umLT4Q1BSmo2HdCkpYBUyHlet4julww-iPbBm-vdnMgRhDNuD928s2_Jp8PwHDrcoiCEIWbkV-bwK-WS4sLMY_3unRX9u9v_HdowQ3AoMU4JpSPtqTH1P4kJ28Xt0D_FzolmtFtv7hc9EWcrVuXlVF82860BX8BKGXofaNHFBTDpdjti3-w8nHho-N5QEBUuB-2Xv_ideBxs5VJQ_4qRdt4d0-AAc25qsMHORb69a43b_MDRD0tsdhB9DkEf-awp2ilLBM7iWrk3I96gdxVGu3YPmzhbRVXC4lxPyqR1DhcEFVcUJRp3IEA0-VCnN-l5SEa60tguAN6SucjGpu_Ynw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34db08e600.mp4?token=umLT4Q1BSmo2HdCkpYBUyHlet4julww-iPbBm-vdnMgRhDNuD928s2_Jp8PwHDrcoiCEIWbkV-bwK-WS4sLMY_3unRX9u9v_HdowQ3AoMU4JpSPtqTH1P4kJ28Xt0D_FzolmtFtv7hc9EWcrVuXlVF82860BX8BKGXofaNHFBTDpdjti3-w8nHho-N5QEBUuB-2Xv_ideBxs5VJQ_4qRdt4d0-AAc25qsMHORb69a43b_MDRD0tsdhB9DkEf-awp2ilLBM7iWrk3I96gdxVGu3YPmzhbRVXC4lxPyqR1DhcEFVcUJRp3IEA0-VCnN-l5SEa60tguAN6SucjGpu_Ynw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«جنگ رسانه‌ای» علیه مراسم تشییع رهبر شهید انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/447224" target="_blank">📅 21:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447223">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🎥
قم آمادهٔ میزبانی از پسر فاطمه است
@Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/447223" target="_blank">📅 21:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447222">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114792c204.mp4?token=UorjZspbJ-vosn8PQ24v9lRW6u1oB8Vp_mmsy2lyweuPRQO7L0Ee_d9DAI4kqZPo4ODQ_ZxTtqpbcl40CFRPgE4JMhNQe6ycu6B5-UMzaxaxA4_aoJ9nZ-vwH8oR9DLuqU2SIrz7gcW_nFSLF6fpFs8smc5tBK3W11emfOJqotLwvySoY68smfPH_sWusTGdciwbv38TTDKy8GDgaOoxh4EtzVFkPb3Bf1YlDAc3vDZHQGihnswonXatQsC85Ln1xyzofPc5ONGj3JC_gDEixnCapxZwQbQHVriDpkebsJIw3b1JgaZhbkCqqDogxxxtFxyAFgv0aPUviQWsIBRRSYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114792c204.mp4?token=UorjZspbJ-vosn8PQ24v9lRW6u1oB8Vp_mmsy2lyweuPRQO7L0Ee_d9DAI4kqZPo4ODQ_ZxTtqpbcl40CFRPgE4JMhNQe6ycu6B5-UMzaxaxA4_aoJ9nZ-vwH8oR9DLuqU2SIrz7gcW_nFSLF6fpFs8smc5tBK3W11emfOJqotLwvySoY68smfPH_sWusTGdciwbv38TTDKy8GDgaOoxh4EtzVFkPb3Bf1YlDAc3vDZHQGihnswonXatQsC85Ln1xyzofPc5ONGj3JC_gDEixnCapxZwQbQHVriDpkebsJIw3b1JgaZhbkCqqDogxxxtFxyAFgv0aPUviQWsIBRRSYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این وداع ابدی است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/447222" target="_blank">📅 21:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447221">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e437001e1.mp4?token=jKhhP8bv_9NnsP8-y9etrvNYB4ELXxRDNWH8q8joC_vZua9w55lbDofRpmaDLaXA5WgpouOR125mRx1S5C_tOvj3KnZUumJ-SMEqraY9XB5zl7QQyGqWHfs9_EwUwYWjxOyyWZfGb04sxZwEAh7au5AMKhwUdF0IpaRgVKkMUxyORIyEmgLsplLh42CV-b0-SVVtJuMOY9KHSS837N-T5zMk2N4OqwT5K2R56X61L55rEGNhpCb3IMv9_mTT5RSkYaS8gMkLzIaLJSCptXsJzN_i_9EmMvEljLyxP-N2uZzs56CMYYqmpzYOf6XfKsRoPkZEh8ocJTcKqVlMoUEIfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e437001e1.mp4?token=jKhhP8bv_9NnsP8-y9etrvNYB4ELXxRDNWH8q8joC_vZua9w55lbDofRpmaDLaXA5WgpouOR125mRx1S5C_tOvj3KnZUumJ-SMEqraY9XB5zl7QQyGqWHfs9_EwUwYWjxOyyWZfGb04sxZwEAh7au5AMKhwUdF0IpaRgVKkMUxyORIyEmgLsplLh42CV-b0-SVVtJuMOY9KHSS837N-T5zMk2N4OqwT5K2R56X61L55rEGNhpCb3IMv9_mTT5RSkYaS8gMkLzIaLJSCptXsJzN_i_9EmMvEljLyxP-N2uZzs56CMYYqmpzYOf6XfKsRoPkZEh8ocJTcKqVlMoUEIfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطرهٔ دختر شهید مدافع حرم از آغوش رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/447221" target="_blank">📅 21:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447220">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3ab0fca99.mp4?token=NT17Q5hEziTKf8Q2s1_FLhn94QOg0cZeNLQfMICgXSNDQBABxHXbwUWZT2HPTKbrWDFyUzXR_QtOkUQCIjY3YLI1upMO7hE20KNeWN6mCPjSGJ1FhkFLpLqbx_ahWcHYQXagFobyDsnGNgtpgbp5ArDAdtJROXnJqbcA9BAzLCdLsVEne5gyLQL2cmaThSkjzlf-rz_NucRX8_Tzuc3KvBndv-YtA9kkUX-EUahDiGQFLE6Pnwb-dIojZlBKDa-zcWFTq1S0JiQJDNS_beIuotZxlyvh5FTL_AJKITXHwWwHQ5lK3bcsV_kWbpAwDPh1vdU-9-sZqnsTn5jWsyBL_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3ab0fca99.mp4?token=NT17Q5hEziTKf8Q2s1_FLhn94QOg0cZeNLQfMICgXSNDQBABxHXbwUWZT2HPTKbrWDFyUzXR_QtOkUQCIjY3YLI1upMO7hE20KNeWN6mCPjSGJ1FhkFLpLqbx_ahWcHYQXagFobyDsnGNgtpgbp5ArDAdtJROXnJqbcA9BAzLCdLsVEne5gyLQL2cmaThSkjzlf-rz_NucRX8_Tzuc3KvBndv-YtA9kkUX-EUahDiGQFLE6Pnwb-dIojZlBKDa-zcWFTq1S0JiQJDNS_beIuotZxlyvh5FTL_AJKITXHwWwHQ5lK3bcsV_kWbpAwDPh1vdU-9-sZqnsTn5jWsyBL_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
متروی مصلی مملو از جمعیت است  @Farsna</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/447220" target="_blank">📅 21:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447219">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1d0c68399.mp4?token=HX2ZJ-mA0JXCw2NcZb63uxhfgiIaean6veDUAYptKyo7Xh_4pCSp4AhAp4KcusWMtGn8DCDrIgkXN6F2YU7E6u3xk6tVe_6H2eOHgzPeSBeNRDnbws-dqmf_yuoMQ0m61VRJJ2HMmyXXtecAfjkqpjENJrNX4CVOscPDhNfjl2Tnj0bgKaeQPmRuInIPdN50ZPhYPD1qbw8aFWJNJm1_9h6SH4DaPnIcYe6-2kdqLi0JH4UMuw_fixWgZz3GY5GV6WAnfdMr3c5UrFUVWQiQsT5OZgrEoyS6E5Q2XDJE-HlkdQfx9Rkd32RWd-So2JUAf5qZ4si3hUGepBJjrFJJEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1d0c68399.mp4?token=HX2ZJ-mA0JXCw2NcZb63uxhfgiIaean6veDUAYptKyo7Xh_4pCSp4AhAp4KcusWMtGn8DCDrIgkXN6F2YU7E6u3xk6tVe_6H2eOHgzPeSBeNRDnbws-dqmf_yuoMQ0m61VRJJ2HMmyXXtecAfjkqpjENJrNX4CVOscPDhNfjl2Tnj0bgKaeQPmRuInIPdN50ZPhYPD1qbw8aFWJNJm1_9h6SH4DaPnIcYe6-2kdqLi0JH4UMuw_fixWgZz3GY5GV6WAnfdMr3c5UrFUVWQiQsT5OZgrEoyS6E5Q2XDJE-HlkdQfx9Rkd32RWd-So2JUAf5qZ4si3hUGepBJjrFJJEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استاندار تهران: حضور میلیونی مردم در روزهای اخیر، نشان‌دهنده دو پیام روشن است؛ نخست، وحدت و انسجام ملی و دوم، تجدید بیعت ملت ایران با آیت‌الله سید مجتبی خامنه‌ای.
@Farsna</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/447219" target="_blank">📅 21:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447218">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51f9b9fcd0.mp4?token=u4BqyXlNmEDsB4B14BV6AwMeQ8C2lhhlNcH-7pPAQtutzkSXrmQYQuaobaeFw9vQpZ5Cl2V53irvJM9OuIEutAonz6tFJ3q8MGsDwFiGXh0jrKQWTwtH4SMsy5EU0c1Ee3odrhxLARIoxAavJZ5K2KE1woctN2W7LJOjxxLqZnUiDkfjVSHWmmZSRpvg3QfbXBjeDGFUir1yTl8NKmaG2EjQhFh1vrEC4J8axT-OtDsdtX6iUpcEeabTaRizOHmlXJVu9LowQhBDVm_XkafEMWmyuyYNtO5wLqxXH5gfl2hKsy6csPrX6mO41ujmZBPZCcUfjLZQUdYBA2h8haPedg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51f9b9fcd0.mp4?token=u4BqyXlNmEDsB4B14BV6AwMeQ8C2lhhlNcH-7pPAQtutzkSXrmQYQuaobaeFw9vQpZ5Cl2V53irvJM9OuIEutAonz6tFJ3q8MGsDwFiGXh0jrKQWTwtH4SMsy5EU0c1Ee3odrhxLARIoxAavJZ5K2KE1woctN2W7LJOjxxLqZnUiDkfjVSHWmmZSRpvg3QfbXBjeDGFUir1yTl8NKmaG2EjQhFh1vrEC4J8axT-OtDsdtX6iUpcEeabTaRizOHmlXJVu9LowQhBDVm_XkafEMWmyuyYNtO5wLqxXH5gfl2hKsy6csPrX6mO41ujmZBPZCcUfjLZQUdYBA2h8haPedg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقت سحر بود که رفتنت رو شنیدیم؛ چقدر گریه کردیم چه غصه‌ای کشیدیم
◾️
مداحی سیدرضا نریمانی برای آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/447218" target="_blank">📅 21:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447217">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4a22b97c6.mp4?token=NXZFXDYORH4bsV_eL1Ef4sgTGxCmvsS0smLdKp39_T-J-ZUi4_9JXfOfxSDg2Ro52EanFYore-TLoZJzvuNPE4KLhFq36ifEVNOQQou9b3L5-MCbx5BGC3wlXXSA8UxF14nWQ7ppSiJiv6-reBE4qKtysT2dpyqEfY1UoFOcMlWn4FFdISbAM8nPQUvkdO2J4BXTpsvZJ8VPL0iQzPQE8TpaGeHDfB6zUiQKNaHDbA_vPc5fUr7vHzPJue1C4ovcdVaTdMJhWKw-QaMFy_XZzH0_iR_ki3yEMXrhMby-qZoXetim53AErauO7lf_OF4x8J29WRVI_NNcScNNomtARA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4a22b97c6.mp4?token=NXZFXDYORH4bsV_eL1Ef4sgTGxCmvsS0smLdKp39_T-J-ZUi4_9JXfOfxSDg2Ro52EanFYore-TLoZJzvuNPE4KLhFq36ifEVNOQQou9b3L5-MCbx5BGC3wlXXSA8UxF14nWQ7ppSiJiv6-reBE4qKtysT2dpyqEfY1UoFOcMlWn4FFdISbAM8nPQUvkdO2J4BXTpsvZJ8VPL0iQzPQE8TpaGeHDfB6zUiQKNaHDbA_vPc5fUr7vHzPJue1C4ovcdVaTdMJhWKw-QaMFy_XZzH0_iR_ki3yEMXrhMby-qZoXetim53AErauO7lf_OF4x8J29WRVI_NNcScNNomtARA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قوم ما قومِ شهادت طلبِ پیروز است
🔹
نوحه‌خوانی امیر کرمانشاهی در شب دوم وداع با رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/447217" target="_blank">📅 21:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447216">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68e4e84657.mp4?token=TjBu5ovchEN8V8Lfr_IJPv3WAGreVkjp-OJXrhSjyCJLB7xnpqogkQVFkYPU8MF1aACVhdmlNmB6AbTlxFTFig9jhors4Bg3eqJY1ZZ08FVC2px-2nauv6xZzeEbQDNTBUvm8lvbOov0B5mvbzBAhADKpfES3MXz6OQkAAEs0_MTIfVPgEj-gNXJWhESPXKRkMzwDAjOsclEPROGjD5sIl2IpITe55wCgPmPmQeSOXxi83wATtkdqSRJLn4VyLMNqujionuzYWjd-ZTVB9YB7uGUUkMvrTRC4dX49WSfve-PouMhWuMmWKmnjuo4JIF69t4Pb0OJFOyatYaocn9ENw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68e4e84657.mp4?token=TjBu5ovchEN8V8Lfr_IJPv3WAGreVkjp-OJXrhSjyCJLB7xnpqogkQVFkYPU8MF1aACVhdmlNmB6AbTlxFTFig9jhors4Bg3eqJY1ZZ08FVC2px-2nauv6xZzeEbQDNTBUvm8lvbOov0B5mvbzBAhADKpfES3MXz6OQkAAEs0_MTIfVPgEj-gNXJWhESPXKRkMzwDAjOsclEPROGjD5sIl2IpITe55wCgPmPmQeSOXxi83wATtkdqSRJLn4VyLMNqujionuzYWjd-ZTVB9YB7uGUUkMvrTRC4dX49WSfve-PouMhWuMmWKmnjuo4JIF69t4Pb0OJFOyatYaocn9ENw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایمان قیاسی، مجری تلویزیون: درود بر غیرت خواهری که وسط برلین حرفی را زد و حجت را تمام کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/447216" target="_blank">📅 20:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447215">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9295861970.mp4?token=HBaw_rjGpJp3phkNwmqp3ib8UbNeEZIFkWA-ungtQSDCd4sw1f6LSroqJHUQhtCv9pNMLdisN6wU2KCINkNhRvyqnGYhkn7Mlk-rEQXtvuETAMpPdGGIw4Su_RfySyhgxmE9GGBgpTUowc002TuXV03xyjatGvXe0AvCNgoBRprikS8dvJ88hhKX22jWeDNemi7oE-j7PIOEgH4QFxSAIvHLFFye6zqdKxjV-y_AvPefP2MjeP3jlL2gCtwr6gzTMKiWI2RH8ocZhYP5_bs9pLShzEmRHxmOpO7Mob-TQ63hWPpoT5k_kKjGCU3S5j8MbAFXu-hSFaRxEKa7HAghTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9295861970.mp4?token=HBaw_rjGpJp3phkNwmqp3ib8UbNeEZIFkWA-ungtQSDCd4sw1f6LSroqJHUQhtCv9pNMLdisN6wU2KCINkNhRvyqnGYhkn7Mlk-rEQXtvuETAMpPdGGIw4Su_RfySyhgxmE9GGBgpTUowc002TuXV03xyjatGvXe0AvCNgoBRprikS8dvJ88hhKX22jWeDNemi7oE-j7PIOEgH4QFxSAIvHLFFye6zqdKxjV-y_AvPefP2MjeP3jlL2gCtwr6gzTMKiWI2RH8ocZhYP5_bs9pLShzEmRHxmOpO7Mob-TQ63hWPpoT5k_kKjGCU3S5j8MbAFXu-hSFaRxEKa7HAghTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام رحیمیان: تنها مسئولی که بدون وقت قبلی می‌توانستند خدمت امام راحل بیایند، رهبر شهید بودند.
@Farsna</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/447215" target="_blank">📅 20:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447213">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🎥
عزاداری عراقی‌ها برای رهبر شهید انقلاب و عرض تسلیت به حضرت آیت‌الله سید مجتبی حسینی خامنه‌ای
🔹
عزاداران عراقی در استان بصره عراق با حضور در مجلس عزای امام حسین، برای رهبر شهید انقلاب، حضرت آیت‌الله العظمی سید علی خامنه‌ای عزاداری کردند.
🔹
عزاداران عراقی با سرودن شعری به زبان عربی با مزمون زیر به عزاداری پرداختند:
🔸
از (امام رضا علیه‌السلام) یک مهمان برای ما آمده و با قدومش به ما شرافت بخشید
🔸
ما در عراق پیکر خامنه‌ای را دوان دوان بر دوش می‌کشیم
🔹
در بخش دیگری از عزاداری، حاضران در مجلس، شهادت پدر را به آیت‌الله سید مجتبی حسینی خامنه‌ای، رهبر معظم انقلاب و بردارانش تسلیت می‌گویند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/447213" target="_blank">📅 20:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447212">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f01c18cbad.mp4?token=fG9OamnbOuUzESurN7KREqEuaB1fHfa34c3Kqjo9JyrxCF-IjkZuSL8KRLK69LJd5FYXE-1mz0S7OyPZ5koNwniLWAsmUTWHIKGTVLB1xjaYTckX4m5MycIs4a7cbvfhnHEGq6vuRaCWyXmhsHkBjgRA6O9AQ6-XG6xdw7eM-HSk0eMS5ciruKjI7y4i_Bu54UsEm8VVIxmj_wBqZ8aVcHDdwmbSIf4hu3GuXDyW_FZo7FG8EuVqmCb-zfBQc-NKB_UqbOlD4Q4U4zh1fFdP6nMHNobrO2ZtowX73f-JbgjOjdlxURbfzT6PfcnrS_WfSdRt6JTCIshDQwKbR4h_A5w1RNwgZEg8LtzpS5HbdRKdSJVAdFB0AR00qCKdAOp49pAEsccg1TD2q-G_Fosg-gm7crGJRW46BULloGU61UNKPD0TLJkxQnsEygiYvdbgZYBeQjSDeiAjWUAJY8kWjEr4eRKFs5ed-H2sV-3EL3OSCsF9FnqRuVJusHvZ7Eidh-CIXFoXSaxyT5wPxQuQ11AjWKgwOM9h_lkJDomuxhXXgLmE4UNKywBS-BUx1EwBdM9tODCkvPth-xlxdldH6XzNAeok13Q096f8g8G-EYtdcttx9hNZWh9VzSCoPmJrEwkLn9lH-X1ryCc7KeyJTTLzGO_saDgIz9LbxgdFsTo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f01c18cbad.mp4?token=fG9OamnbOuUzESurN7KREqEuaB1fHfa34c3Kqjo9JyrxCF-IjkZuSL8KRLK69LJd5FYXE-1mz0S7OyPZ5koNwniLWAsmUTWHIKGTVLB1xjaYTckX4m5MycIs4a7cbvfhnHEGq6vuRaCWyXmhsHkBjgRA6O9AQ6-XG6xdw7eM-HSk0eMS5ciruKjI7y4i_Bu54UsEm8VVIxmj_wBqZ8aVcHDdwmbSIf4hu3GuXDyW_FZo7FG8EuVqmCb-zfBQc-NKB_UqbOlD4Q4U4zh1fFdP6nMHNobrO2ZtowX73f-JbgjOjdlxURbfzT6PfcnrS_WfSdRt6JTCIshDQwKbR4h_A5w1RNwgZEg8LtzpS5HbdRKdSJVAdFB0AR00qCKdAOp49pAEsccg1TD2q-G_Fosg-gm7crGJRW46BULloGU61UNKPD0TLJkxQnsEygiYvdbgZYBeQjSDeiAjWUAJY8kWjEr4eRKFs5ed-H2sV-3EL3OSCsF9FnqRuVJusHvZ7Eidh-CIXFoXSaxyT5wPxQuQ11AjWKgwOM9h_lkJDomuxhXXgLmE4UNKywBS-BUx1EwBdM9tODCkvPth-xlxdldH6XzNAeok13Q096f8g8G-EYtdcttx9hNZWh9VzSCoPmJrEwkLn9lH-X1ryCc7KeyJTTLzGO_saDgIz9LbxgdFsTo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور چشمگیر مردم در ساعات پایانی وداع با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/447212" target="_blank">📅 20:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447211">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/259b338fe8.mp4?token=TLvZ7unqAmT3fdZfXuFXMBkKhGpcd0w6WcDXJ2yUKw8KecREIPgEvMUCwA7J1BB1yoMoEcoQYrMjwidLvEPTU2myMgYyQEFGT4PEs_beZ8JUXq1Tt2rVXDXm_ZyQaSQTguwoYiYFjYJ3ePTLKxNUTefi04B0cPzyHmlIe1gO0rLxmCF4FKI0Ki_dN002qXrca_bJdOMM2m60k70JT4udoBoICE_gKI46_EihjklSXE0E-PnmwJO1t_chS3p1IjTQySMXfdC59ZKkR7g-DfdJN7fV6OKE4hawjZu-4eE4CHH3tpTBE7XCLLDyqhqwWiPx7Y4oViZLyuYidx6FzlCEiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/259b338fe8.mp4?token=TLvZ7unqAmT3fdZfXuFXMBkKhGpcd0w6WcDXJ2yUKw8KecREIPgEvMUCwA7J1BB1yoMoEcoQYrMjwidLvEPTU2myMgYyQEFGT4PEs_beZ8JUXq1Tt2rVXDXm_ZyQaSQTguwoYiYFjYJ3ePTLKxNUTefi04B0cPzyHmlIe1gO0rLxmCF4FKI0Ki_dN002qXrca_bJdOMM2m60k70JT4udoBoICE_gKI46_EihjklSXE0E-PnmwJO1t_chS3p1IjTQySMXfdC59ZKkR7g-DfdJN7fV6OKE4hawjZu-4eE4CHH3tpTBE7XCLLDyqhqwWiPx7Y4oViZLyuYidx6FzlCEiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات برنامه اقامه نماز و تشییع رهبر شهید در شهر تهران از زبان استاندار
@Farsna</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/447211" target="_blank">📅 20:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447210">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dea728980.mp4?token=PtK4KZMSHCiswnjsM5t2TaHKUpwnbmgVQLbemuMvi78yXSuLMpUiFG6LDof33_Bo-RhZNUvLGzaPk5k8L_U8yIFm0C67zdB9LcS0GG_GUwrmDrQuAuM4ZwxbXbGAEbx2qsj7sMobWIdo4ZlitX22sJcUwi4b16VcmTPS3ta1_ezu06ty2aaQZrrqsAF5HfX4kUHw7zes42Kyk03kVR_Bffnm-PZ69ksTIMLRPfA0omDzSm7zGRIcPDRFk0ulUIfs0KkdBcGHcDpnZFyPobOn6o9ZF7JE6GdxrqQ1Pv7CSpWr3gTW-q7vOMxPXv8_2ALRI8UF7LhjZbPO2tTFCPRLPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dea728980.mp4?token=PtK4KZMSHCiswnjsM5t2TaHKUpwnbmgVQLbemuMvi78yXSuLMpUiFG6LDof33_Bo-RhZNUvLGzaPk5k8L_U8yIFm0C67zdB9LcS0GG_GUwrmDrQuAuM4ZwxbXbGAEbx2qsj7sMobWIdo4ZlitX22sJcUwi4b16VcmTPS3ta1_ezu06ty2aaQZrrqsAF5HfX4kUHw7zes42Kyk03kVR_Bffnm-PZ69ksTIMLRPfA0omDzSm7zGRIcPDRFk0ulUIfs0KkdBcGHcDpnZFyPobOn6o9ZF7JE6GdxrqQ1Pv7CSpWr3gTW-q7vOMxPXv8_2ALRI8UF7LhjZbPO2tTFCPRLPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: همۀ خسارتمان را می‌گیریم و جنایتکاران را رها نمی‌کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/447210" target="_blank">📅 20:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447209">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af713189af.mp4?token=uMIeg2QJ1cFE4wVJStiNRnNx0I9IbPQKXh0_0dk7C68CVIaCYc_eR9WkiOnAxIb8nG5IYVaU8X9ZggfIazrnOOEypfEj0OmFe5Ru9Bngvxa0JWx33ksptjTb9NgFjZCa9LCaHFNnKi_5Pmk-eZW6udIu3yI5hl4ZHX846dVbTT2lQaqtRC7vohrX1csPkNhKgImrw5X2Q1KYxYgpQkCXpRILN-OrEOoAyNSprnFLoqa2U7SqtUxgJ3Vlb5PrNFcNPYL9V_LJn26GXb5jLUl1fAtAfm9i4iXB7mlRa38ivsSN3R8wNOTQj-zcfXJ13Gvf2oR7NvhnWNGIS7s3REfpdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af713189af.mp4?token=uMIeg2QJ1cFE4wVJStiNRnNx0I9IbPQKXh0_0dk7C68CVIaCYc_eR9WkiOnAxIb8nG5IYVaU8X9ZggfIazrnOOEypfEj0OmFe5Ru9Bngvxa0JWx33ksptjTb9NgFjZCa9LCaHFNnKi_5Pmk-eZW6udIu3yI5hl4ZHX846dVbTT2lQaqtRC7vohrX1csPkNhKgImrw5X2Q1KYxYgpQkCXpRILN-OrEOoAyNSprnFLoqa2U7SqtUxgJ3Vlb5PrNFcNPYL9V_LJn26GXb5jLUl1fAtAfm9i4iXB7mlRa38ivsSN3R8wNOTQj-zcfXJ13Gvf2oR7NvhnWNGIS7s3REfpdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس قوه‌قضاییه خطاب به قاتلان شهدا و آقای شهید ایران: گریبان شما را خواهیم گرفت و رها نخواهیم کرد.  @Farsna</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/447209" target="_blank">📅 20:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447208">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c01d010366.mp4?token=cpq97S6r1EZb1k6rBbQiubIKhja6701EnkZBn-ai9aHd2IHsh5IxjlpLqYxEZwPqHWvlyPRSbQTXS_g83xVQ1JrcgXc24qxNLoI8ZZeve1sZvvmvjGo_bEMCBfOrn2Ku90Egh3gWj5rRUNxvwpTsMy_5r4Rqp4sqsizbA0JqrYp6Ipe_Wjwn18oMK3mF6SGwANJmGJgdMsAJNAX6UdyQJaH7Fh03z3DcFlfX2NmN-ci976DuND9jxEiy8NyU_Y_E7aN5cX2sWitrn7uWi7vWM7Q8PGy_4yMWmJn35whZRnuotXYH5ipWRXBmuPtcyWFDPrtWjgwP-VvDADRXsdlNxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c01d010366.mp4?token=cpq97S6r1EZb1k6rBbQiubIKhja6701EnkZBn-ai9aHd2IHsh5IxjlpLqYxEZwPqHWvlyPRSbQTXS_g83xVQ1JrcgXc24qxNLoI8ZZeve1sZvvmvjGo_bEMCBfOrn2Ku90Egh3gWj5rRUNxvwpTsMy_5r4Rqp4sqsizbA0JqrYp6Ipe_Wjwn18oMK3mF6SGwANJmGJgdMsAJNAX6UdyQJaH7Fh03z3DcFlfX2NmN-ci976DuND9jxEiy8NyU_Y_E7aN5cX2sWitrn7uWi7vWM7Q8PGy_4yMWmJn35whZRnuotXYH5ipWRXBmuPtcyWFDPrtWjgwP-VvDADRXsdlNxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس قوه‌قضاییه خطاب به قاتلان شهدا و آقای شهید ایران: گریبان شما را خواهیم گرفت و رها نخواهیم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/447208" target="_blank">📅 20:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447207">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a98eae559.mp4?token=eqqqnWmwjpk1ZwRuamAbuDlOahefUux4TnpYXQ_JquY7wvxTfATWTUraMF7uhQiaT5K8qFui6jAnSbvfxaKrVLmNkfqAMR_SWyqMjL7S-J_EnYKw3ALVz9e7-VUhInY2V-7nlem111Nd4E15hc4jMyaW30Xl_pt9k2ok6bKMoeMn1WoiwGTXP-hVp2TJUi7H9U-z7wxRYDLXmZi3p-0OML5564q3X75gMLWYrILn3B9NL-SKprxjSkJffX53RI0SeSRQHcXgdASuwm5KqN56rtED9rS0qwGxQrrZmWNixnqg00k3x1P82LRfjKCppa_5sXn7O03brfqRmzfTWXgJfIrMfbzBGIleAS-gNDyAcYTmkXOESY4oTQOBK4ogUWhKR2uKVktVi1RBULajYjxpiVjg1fa_agcJ6DQh8J1mSNtxdEzKpldkTxM6ftMAprxGk33h_fZcuZRtv1UTx8wEti-i62RTtyDrgsbcALzwjDs3vRpuNxwM2Sgksbnz5jKhxGuGKqEeb6jEHhiQ0eBTIkie-Gv5bQbvcaQCHK6hFqnHnOtU8YKGcMdG4xdalYIF7cHjLqh2iMO2hL67My-Jnfb3XHj4lFpQEOQBiRaSksMWf_lRzA9RNwzwvzon-7K-1wr3LrGQVyV-1dhjObpv_pzNzAKULGuYL7Sc8Ti--5s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a98eae559.mp4?token=eqqqnWmwjpk1ZwRuamAbuDlOahefUux4TnpYXQ_JquY7wvxTfATWTUraMF7uhQiaT5K8qFui6jAnSbvfxaKrVLmNkfqAMR_SWyqMjL7S-J_EnYKw3ALVz9e7-VUhInY2V-7nlem111Nd4E15hc4jMyaW30Xl_pt9k2ok6bKMoeMn1WoiwGTXP-hVp2TJUi7H9U-z7wxRYDLXmZi3p-0OML5564q3X75gMLWYrILn3B9NL-SKprxjSkJffX53RI0SeSRQHcXgdASuwm5KqN56rtED9rS0qwGxQrrZmWNixnqg00k3x1P82LRfjKCppa_5sXn7O03brfqRmzfTWXgJfIrMfbzBGIleAS-gNDyAcYTmkXOESY4oTQOBK4ogUWhKR2uKVktVi1RBULajYjxpiVjg1fa_agcJ6DQh8J1mSNtxdEzKpldkTxM6ftMAprxGk33h_fZcuZRtv1UTx8wEti-i62RTtyDrgsbcALzwjDs3vRpuNxwM2Sgksbnz5jKhxGuGKqEeb6jEHhiQ0eBTIkie-Gv5bQbvcaQCHK6hFqnHnOtU8YKGcMdG4xdalYIF7cHjLqh2iMO2hL67My-Jnfb3XHj4lFpQEOQBiRaSksMWf_lRzA9RNwzwvzon-7K-1wr3LrGQVyV-1dhjObpv_pzNzAKULGuYL7Sc8Ti--5s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استاندار تهران: هیچ‌گونه انسدادی در ورودی‌های شهر تهران وجود ندارد
@Farsna</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/farsna/447207" target="_blank">📅 20:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447206">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/024795ab39.mp4?token=m551MY4xteb9ToLjnnWqrIOj_5HzUYcRyPRTEUcw4wZJK1_zVZoLVRllpHi3wucmLQuF0v1V1xTrtIHBeCbfZ_cJByi-gZkRJrIMLcdxfgnnPpxUinY9U1fFV8qL_Yeksuj2zHgRsFS3Z4s-i6CyH_joUuiJTWBR1-MXCBCZOsWZoJKAaudRWqSXYA5h1-GBGawXMZ4jrf8ZZ_zKR3SGcTerwJSL1kgQCCkMvNct-lORIzW_XgDPEGsLb5WhVZ0SKhl03CKFWrygu6-yUDpa67JR8ovc2XLCvHsm2ElUatcGq1ZIGaklHAJwJOtpFayy0xRP5Nda4RfUR97juhcEAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/024795ab39.mp4?token=m551MY4xteb9ToLjnnWqrIOj_5HzUYcRyPRTEUcw4wZJK1_zVZoLVRllpHi3wucmLQuF0v1V1xTrtIHBeCbfZ_cJByi-gZkRJrIMLcdxfgnnPpxUinY9U1fFV8qL_Yeksuj2zHgRsFS3Z4s-i6CyH_joUuiJTWBR1-MXCBCZOsWZoJKAaudRWqSXYA5h1-GBGawXMZ4jrf8ZZ_zKR3SGcTerwJSL1kgQCCkMvNct-lORIzW_XgDPEGsLb5WhVZ0SKhl03CKFWrygu6-yUDpa67JR8ovc2XLCvHsm2ElUatcGq1ZIGaklHAJwJOtpFayy0xRP5Nda4RfUR97juhcEAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی سازمان آتش‌نشانی: در صحن ۵۷ هزار مترمربعی مصلی، سامانه‌های مه‌پاش برای کاهش گرما و رفاه زائران راه‌اندازی شده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/447206" target="_blank">📅 20:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447205">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJ8K6PywrvkEG0QW-m22d0mhXCrV2m7hAqqvxm_lB-CKsNCpNONTH6hlpoXvhTz91Dc32KbDCo82WwfiVuSqNUx5awKTf1oU1uhEd0T5SGdlLKvbi-o3x1_poU2rNjJ8v0eUOka3rgjw1Rzjqn1wOXgfMUAId_1gRDfFvUiaxj8h290b_Vip65ce-5dCBPdlCbnABwHvaICKpqQMBBIaG-yM_gMAkFLv7wHvkRG7NWeINYssYJxg2eyWfZMEqX0920eTMhu0kxPduruJJpbqz4YLhTjxnHZPrfagAsQ69LlA8T06NBYcgRzaAZtuvGm6m8kpIX4p1cYmEmqGfSs5Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتصاب مجدد حجت‌الاسلام والمسلمین اژه‌ای به ریاست قوه‌قضائیه
🔹
حضرت آیت‌الله سیّدمجتبی خامنه‌ای رهبر معظم انقلاب اسلامی در حکمی، حجت‌الاسلام والمسلمین محسنی اژه‌ای را بار دیگر به عنوان رئیس قوه‌قضائیه منصوب کردند.  متن حکم رهبر انقلاب اسلامی به این شرح است:…</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/447205" target="_blank">📅 20:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447204">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43293ac785.mp4?token=rSw823IFzjwCskHm6U6Ez6_oCxerXvh3ZJWJu-3q8t4vr8bhdiBetMp70WR-TO27ja-0lVRl4qIiL2AdK7EakUZdSKkQs4r8nCoZMrf7BYFeupAwcvKIyyDjY_Mo6a1YBzjxkw2p40-GCj_z3Di-QMXZKwnvs4bs6l3cX0IpOym3QanC-KtaKQEFGiYW0aeHZ9aGHU42Xv1Srz5kRPvd6hoq-yHT6MIM1i7cDHmu-fpdk16z98zHj-8W5VR6ml6WQuf_ZuF4efgxwgq2I9JT4ywLS1LIVGHoP015WIXiXNeN1SxCUgBFo62kJKZhgKp9gYgiCjoX4Q9TjoQBYc3wDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43293ac785.mp4?token=rSw823IFzjwCskHm6U6Ez6_oCxerXvh3ZJWJu-3q8t4vr8bhdiBetMp70WR-TO27ja-0lVRl4qIiL2AdK7EakUZdSKkQs4r8nCoZMrf7BYFeupAwcvKIyyDjY_Mo6a1YBzjxkw2p40-GCj_z3Di-QMXZKwnvs4bs6l3cX0IpOym3QanC-KtaKQEFGiYW0aeHZ9aGHU42Xv1Srz5kRPvd6hoq-yHT6MIM1i7cDHmu-fpdk16z98zHj-8W5VR6ml6WQuf_ZuF4efgxwgq2I9JT4ywLS1LIVGHoP015WIXiXNeN1SxCUgBFo62kJKZhgKp9gYgiCjoX4Q9TjoQBYc3wDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همهٔ شما مثل فرزندان من هستید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/farsna/447204" target="_blank">📅 20:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447197">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vhMunfl8TsDEDbezcmSd7keguT7jNlHQPnzb5Ym3ATO4-VBMUvWb8PzESTrUf6xH-lMmQOJ9qoziEt46lOk6YGP0Kq7jzXzy0QEhbzzWI0j5RUFCVupOrAuMkEZBSiHRyCnnG_GgEtfA9SyyLogG5Z3nvDDLxv5umvJLbm2nThiPEDMmGxkN8tkSlklbDSHFuBsL9E2CjWMp-Y_5bT90VmHKBAgx_G6zUax5bRQY7fZFlsYhN6gYUoF19Ke4dvxQpw3tFyhIjUvLhHMjwIIIitgB-Intl1wuwYStIwfE6UeHNSbAvXlB0tn_sJbtidnmRL5bJ6r0scDtXUbxMlBrWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ruERtvdIl229bGzKUUaDl7Nr5eWuY7qQN6N-GTzHDP3g8Cv35Y7irYay2XVApoMn7Aa_mhXAuoh50wfKcut9Lb8e1DjenXoG0Vb45O1d5BRfJXgT7LR48PnzJW9mp9quEi5Z7R1ywZB57IjWt-nwooUvVdQ-jPZWFWDl2Jc1fhZvh2gqQLbS3TdYT36bCXgRK9Yo_7aaCL2Qg1rchkOe_S3lynYG8rl3TtqcR6z8USCjPvxlChGErJ_SjAbQYHZ4DMNVnVDjGX0srpCGbsvh3fXoHf59F-O-_J9YAEVRQtoJVAs6heRtCifWoJtjdZdUcEH7TP-Rv-ErSxP75liMgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E0pC7Pdjlw9Hkiy_HbjyTq6KdYbQHVFy7X0bcx6Y8ph8h-GKPxKe-NtlOo6L4VWHc9A-fWFgOQ9Q9_W35FWbjJg2KRdRZSIpnFDErSp5LvoELLchottqEmZwNtlt6AOm3Ivc7qfiR26_FgE0-Z1540IG9FufG9JjQxP0RNFBvfHVVccxLGDKerO4aTnV29VOc3NkwljiA5RQOIybLOeorl55YZIVaODYdqta7nLpLpw65E-DHz7rlQ0stjrTPY_f7Zbs_8dLrvUfhm4HOyf9wGyWXmM7AMDUXLiwbvkzhrFLaeg5ss_7nvy4xSb7PFU1rINohl-0wHXQD0WXgbrAZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YKPAt2AjGnbScngVpZwYltbqKEQUA6QuvekOW7bjLhW4lEnBvaRRsal_UzNaeXgYnLGibQSfNC7MUWNiTP5SzCetSP4YI9Bs0a02WRO8opYFJ9AKKzC-C9zudcMqIrcIMr61VHRRyQRivwqLeBpqCXuDiMhFRs7Wji_3Q1PwZ42tMnbpJL_qJLnIwo_D-hejryJTYDtClDFPZcAEwxr0jxcNjcz05i1iDSITJjTpr73wRM3MeSYQAlFxxEDEz0Bk6yFDK4e3aVV32hbTABxkIydR7h5HHOyr8BGDeDJQcb-g8jUTmxHwxoGULUyDoKL_K0fRZfbAiRChNE4X4MvfSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/duWk2UR7f23UjJDZgInotAh-2ILTEPq2cL4ZR3c38flOYH_g4KYJT46EwKCqTHrAC7-5nM8XqtBroFvGpXlkN3VAXYBZEEi-hEq-xz28BTigFHnXxbaqrgRPdPVQ-uJQiy1E1B1w9cBfEbOmP8dOLLz7xCm9O3DYEc4Lef8rt8td77eJpWyUHfeYVlf1PJzJ7YA8i5mMtajCDmLBOQdxEBYNhFaFQp1L9orsUkydxiIQuol_u9k2suocLXCoBNdAScEhYE_hQJdot8Z3AHz_duNvhLp6EprXdf0nHHnLIQZAk7lMhC6AFIdsKVVhfamAZ0zmZ74_X8WW6CZ7vT3hYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/igbjgAWIm4NHdeBedqn4G4lBjf-_2MX95aHTUsbuhQweueLhZoquVWzS0ygUvBe_gETUnI9sNzomPaDA70-CDEEkqJ9tl6foX_l5JodUFY5Wp-mjmVR3dXSNUXs3M2DsdDj62HlraWMP6BHlkundlUuLmQxtH9mLmNopsrtarbZz1NvUQwwRsXhpOdwZY0cp4FybISYeW3P-SZ47V_C08Dn5rhxIOZsWVWcSRVKdW0u3O4FYqMpoB9n5CnImkIfGn7ecXtGRXnw-QAHNypW0AFdtCsXs2OM32UNfYBhil5uwKtJS_22ougJhoqX1NUkU6-6zD35S7Kowex3lLE7wSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nGsaPIojfRE-CEOeuS69Ntrn8NMhtwIwT7e8hAnlKw7iwMmglzbGhMaU9ihY_SIIe4Dp3z3kQJT2AU_JyVWJHsMHdbOvsxzHqhv5R030vrFeUyxI2vyvFoL29eShOkHMuHtFzAhWQus4mMt3mq-KdheiKHe4xPJfz8tC5uWNAJU7fvObSVA0rE0debOxZrqAdSGgdqwUPFftHVSPNGFn8SFyDPgiTjkvk0KtCCwWdrsb3JN5c2a8AF4q90zxc-zmmFDBhJeo8x0SZvFj1C0VP1OPrYBZ_GeGJBjglITrqpoiQQgiT3TrxVbObXmdu1jduihhQ_Va1ZLesV6AEv6QRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آخرین ساعات وداع با پیکر رهبر انقلاب
عکس:
صادق نیک گستر
@Farsna</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/farsna/447197" target="_blank">📅 20:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447196">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c400f5c86.mp4?token=eDVDBXgW2ptMk44stv65shCeRaRj1p195NURFCzPRUlpox9psEmmcTKC1Jfaz4BG-LGVZhcTOqxTgheFJawXBJ4-nGzHif6gWC5pDvPRh2gWIxQcoBjblnFCz93M8WBa91lpfNDxW95H8r-3xR6dyQpZAlGi_uZOy4PfrqEi02ToDblh2ya29Afy_iAUVPJYS5O7-5SDO-5chqRJphza3MnweBd4lQwXLWEnq5_frBoQFTKsTyc8dZFS0dw7C-0HKW2QdwzHOO00YV5z5V8cjU89El0y7pqImfTym9CYXyNzTubPO3WBdZJ0r83KUuR_ZNm12IDzw7ahhd8BWhWNPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c400f5c86.mp4?token=eDVDBXgW2ptMk44stv65shCeRaRj1p195NURFCzPRUlpox9psEmmcTKC1Jfaz4BG-LGVZhcTOqxTgheFJawXBJ4-nGzHif6gWC5pDvPRh2gWIxQcoBjblnFCz93M8WBa91lpfNDxW95H8r-3xR6dyQpZAlGi_uZOy4PfrqEi02ToDblh2ya29Afy_iAUVPJYS5O7-5SDO-5chqRJphza3MnweBd4lQwXLWEnq5_frBoQFTKsTyc8dZFS0dw7C-0HKW2QdwzHOO00YV5z5V8cjU89El0y7pqImfTym9CYXyNzTubPO3WBdZJ0r83KUuR_ZNm12IDzw7ahhd8BWhWNPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دکتر محمدرضا کلانتر معتمدی، پزشک رهبر شهید: رهبر شهید زمان جیره‌بندی حاضر نبودند بیش از جیرۀ همگانی استفاده بکنند.
@Farsna</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/447196" target="_blank">📅 20:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447195">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa8e78c7e1.mp4?token=kGMSBJ5JWVxVLUYd0hw_akMwK-m_OsyKlxJC0bmqikKER1QougAtWYvai6zw72ZdtJG_JS8wf4uzc58GRNz3yoOT3aqzUjNehFE-PiCM1tOtNbrt85UP-L0S7HN7vI1yhxmYOSRc6kKT2qwaBIP-x85lQQaOxz2uWUkewESjpF0A0Y8rCr-ZWO-lUA_fUg4pZxG9AIH7vAqLchR0dKM6ZzVGgur4CERKXp7rnEd46cvIzDWo-_u3bZ9MozxVfjouW4iQHfXCgaNCAGm1zklym7nXxufhsxPDH19v2TdbR5BXORAvy45H2vC1uuJG9s8zx8_FYhtacrndSRWwic-3vl16jQwbfD91ad7ip9oo40roc0_pKpVRY162CM2M2qxNmaQ8nbbC8X6Mk2PLEDH7pl4AU7Ny6kxUQofJPWSV7kiOvoUJBqrz0KtDqZMbkV3vRbBBI1-_zV3yMoZzKWOS5nIn2dONEHCCkZ5xrCvyOouJ8pr5tv2rYeJmaUxboYH6VtzSEj1OxKvOenRumFoyf1gngW22BB9XBwS0aSJcl113PpFIiVfqWCOEVRd0Bz-nVkMFxo7mrFbsYSn_RfDdfqDqtBr16TpprlEDYVQ6PXoTZvgcH_MgNah-VuP4G374i_zxxa_NiZ2UXffvZOkodRSpyz5n6pzXLLAYGXdsBCI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa8e78c7e1.mp4?token=kGMSBJ5JWVxVLUYd0hw_akMwK-m_OsyKlxJC0bmqikKER1QougAtWYvai6zw72ZdtJG_JS8wf4uzc58GRNz3yoOT3aqzUjNehFE-PiCM1tOtNbrt85UP-L0S7HN7vI1yhxmYOSRc6kKT2qwaBIP-x85lQQaOxz2uWUkewESjpF0A0Y8rCr-ZWO-lUA_fUg4pZxG9AIH7vAqLchR0dKM6ZzVGgur4CERKXp7rnEd46cvIzDWo-_u3bZ9MozxVfjouW4iQHfXCgaNCAGm1zklym7nXxufhsxPDH19v2TdbR5BXORAvy45H2vC1uuJG9s8zx8_FYhtacrndSRWwic-3vl16jQwbfD91ad7ip9oo40roc0_pKpVRY162CM2M2qxNmaQ8nbbC8X6Mk2PLEDH7pl4AU7Ny6kxUQofJPWSV7kiOvoUJBqrz0KtDqZMbkV3vRbBBI1-_zV3yMoZzKWOS5nIn2dONEHCCkZ5xrCvyOouJ8pr5tv2rYeJmaUxboYH6VtzSEj1OxKvOenRumFoyf1gngW22BB9XBwS0aSJcl113PpFIiVfqWCOEVRd0Bz-nVkMFxo7mrFbsYSn_RfDdfqDqtBr16TpprlEDYVQ6PXoTZvgcH_MgNah-VuP4G374i_zxxa_NiZ2UXffvZOkodRSpyz5n6pzXLLAYGXdsBCI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماهنگ «رهبر جاویدان» با صدای محمود کریمی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/447195" target="_blank">📅 20:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447193">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/927fb2214c.mp4?token=mKKWXmxUfPtv5qfvauUUcfSj1w2wvOm7wOhrH0bj2yupvkE3-XFSv8jkMg4ZSWw7nZqMmAm5vTYIIeuQxLEqfEBuOCfq4b8z2EyTmWxdGYZFoGWWugWPsP5EFxvtPHCw5az140zEsgbxJF58zwsLzT_jfbhcpnlh3cDAoyFs23JlcZXXKRbwBO3JKCU-TTB4PF5tHHu5wOGRGHWOZ5TYnCZm0NFbeJ_Nr3ct_vRhRAexAZNx5WWS-aqkBFNi5V_erVbafkRKdJ0n21e7k49MWVQgpOOU13VDNfEZlcvCCRL502XRtrIGd3dbxkaoEU0t-yVZDFdH9QEE5bTeMOgI6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/927fb2214c.mp4?token=mKKWXmxUfPtv5qfvauUUcfSj1w2wvOm7wOhrH0bj2yupvkE3-XFSv8jkMg4ZSWw7nZqMmAm5vTYIIeuQxLEqfEBuOCfq4b8z2EyTmWxdGYZFoGWWugWPsP5EFxvtPHCw5az140zEsgbxJF58zwsLzT_jfbhcpnlh3cDAoyFs23JlcZXXKRbwBO3JKCU-TTB4PF5tHHu5wOGRGHWOZ5TYnCZm0NFbeJ_Nr3ct_vRhRAexAZNx5WWS-aqkBFNi5V_erVbafkRKdJ0n21e7k49MWVQgpOOU13VDNfEZlcvCCRL502XRtrIGd3dbxkaoEU0t-yVZDFdH9QEE5bTeMOgI6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی گسترده در مجتمع تجاری در خیابان الظلالِ بغداد
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/447193" target="_blank">📅 20:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447192">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa5b2b7dd7.mp4?token=pxQnw4jZz1d8-nou97v_aAR-QYl8dj4wXwoHfaePuRLhxHhM1-aw8OpuGu2jjYM4A3893qGmV03KgkTflKIsnr0bR5Qr6MxTqIDL_H5ONNJnRWLx-66CVj9LwI72ZxCkgoQJBc1ESAiYw6dDHL4FvaD6SVLLBgz25d0NaMJi_wWIFfAwupR_39m8SsNU-8YNeCz3N0qcoQl2WpPs04WbwX08xr9KIqqbj3BV7h4FS4u6GbTgTcBMe7S_R6elbWmGBT4eEwiZlgo0BUL64Vj4e49NHk74PWMO1E67d6J9f3RSmvzRQgKIz_lx3xscAkr7aRcVEprkLJi7CHLlrl4j_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa5b2b7dd7.mp4?token=pxQnw4jZz1d8-nou97v_aAR-QYl8dj4wXwoHfaePuRLhxHhM1-aw8OpuGu2jjYM4A3893qGmV03KgkTflKIsnr0bR5Qr6MxTqIDL_H5ONNJnRWLx-66CVj9LwI72ZxCkgoQJBc1ESAiYw6dDHL4FvaD6SVLLBgz25d0NaMJi_wWIFfAwupR_39m8SsNU-8YNeCz3N0qcoQl2WpPs04WbwX08xr9KIqqbj3BV7h4FS4u6GbTgTcBMe7S_R6elbWmGBT4eEwiZlgo0BUL64Vj4e49NHk74PWMO1E67d6J9f3RSmvzRQgKIz_lx3xscAkr7aRcVEprkLJi7CHLlrl4j_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
برنامۀ وداع در مصلای تهران به‌دلیل ازدحام جمعیت تا ساعت ۲۲ تمدید شد.  @Farsna</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/447192" target="_blank">📅 20:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447191">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c554448e2a.mp4?token=mVgvuWNU8ZVNe_OHP1PGvfia4uk8nHvowjxZG4-xxPhg_YZnbu27O2rz7X9FrF9WdSgaO7mnywhs8NQJcN8VgfDKpe_SLUqlJOewSsh8ZbqqrxK0QxofDY5bqjQ4aelwXa0nqxxrACcgGp-iwRJ72dnkLKW3cN_HuSs7V1RY77n0aC0E6Sud2UKnqAbjc-XQH8wh68JCTeXI5524lAbUcOPWRI3U1Ul6PoftTAHRtNDR6CsBYMqK-z54cnC-vzgc3bHuEHaqugzN9vrit1G5c6Wd38ra8Vj47Aaf-UUGuUo6UNYWez5b-DIBP1HsUKrCr8kywR07gcAmYrzAvNrHXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c554448e2a.mp4?token=mVgvuWNU8ZVNe_OHP1PGvfia4uk8nHvowjxZG4-xxPhg_YZnbu27O2rz7X9FrF9WdSgaO7mnywhs8NQJcN8VgfDKpe_SLUqlJOewSsh8ZbqqrxK0QxofDY5bqjQ4aelwXa0nqxxrACcgGp-iwRJ72dnkLKW3cN_HuSs7V1RY77n0aC0E6Sud2UKnqAbjc-XQH8wh68JCTeXI5524lAbUcOPWRI3U1Ul6PoftTAHRtNDR6CsBYMqK-z54cnC-vzgc3bHuEHaqugzN9vrit1G5c6Wd38ra8Vj47Aaf-UUGuUo6UNYWez5b-DIBP1HsUKrCr8kywR07gcAmYrzAvNrHXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ما برای وداع نیامده‌ایم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/447191" target="_blank">📅 20:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447190">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5ebf4ec7.mp4?token=qwP9Hg7n3xhP-kP1BBmkaCbY2etJU_zxocmDL-L0tbLmUCFz5EgFW3or00lJ5cjBJfDOLGEpfKfTIOKUwkLgCf2-NxoF4C05cojptvjGEuEsS4FirQ41CRK54qG-3cO-xBrquO9FKiydpYIpwuXW4tA4eLw91gYBeMaO-9RELKKOPOn5vbuqOVsLNenH0LwGZTG1etOn6RmIgZv7nRzV-ntfhDm0s5WQrE8Gi9Lf4okhVVNj8zrCLsu_p4esMCoe3beu6mh_ozk1_YMKsxFtKNe2HERURBdt07v_7w23_AxiBTu_GnM1DfejVUr5p20LxOseLvrKWTNCLT5629AIXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5ebf4ec7.mp4?token=qwP9Hg7n3xhP-kP1BBmkaCbY2etJU_zxocmDL-L0tbLmUCFz5EgFW3or00lJ5cjBJfDOLGEpfKfTIOKUwkLgCf2-NxoF4C05cojptvjGEuEsS4FirQ41CRK54qG-3cO-xBrquO9FKiydpYIpwuXW4tA4eLw91gYBeMaO-9RELKKOPOn5vbuqOVsLNenH0LwGZTG1etOn6RmIgZv7nRzV-ntfhDm0s5WQrE8Gi9Lf4okhVVNj8zrCLsu_p4esMCoe3beu6mh_ozk1_YMKsxFtKNe2HERURBdt07v_7w23_AxiBTu_GnM1DfejVUr5p20LxOseLvrKWTNCLT5629AIXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت «کالا والش» فعال رسانه‌ای آمریکایی از ابراز ارادت ۲۵۰ شاعر ایرانی به ایرانی‌ترین رهبر تاریخ
@Farsna</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farsna/447190" target="_blank">📅 20:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447189">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMt-1kSf79d6Q7Ny0mKwXzZuRPK95RBfLeXayA9392eaf2Cek4pDF7Vzw2X4lW_FDh1ZcvIZuXO-H9hrjLxbsM09XkwwHxmooBtXo7Pw82dIKvwg2HA3SbVZ8JFpjr-KdeQqI6-P-DSYWMOURLbxB8rRC42dd6fEMdSInNsJeQmQm7mvnmFczFYwnN1_GWQJ-0VFZfCqcHjg7OXbLlYwFMTXPEB9LddAwZKvn6WaZ96O3f4oKvyXz3fUQRI2uCLJcBPshp-CILDJ4FvJvyYpJHb5cUPxAK1qr9quh6gKZ31UAzzrF0CGsIPk8EZ-vEMGM5_qR2X1nrA5QDdR-N_OYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تشییع رهبر شهید در قم
🔹
کمیته اطلاع‌رسانی مراسم تشییع رهبر شهید در قم: مراسم از ساعت ۵ صبح روز سه‌شنبه ۱۶ تیرماه با اقامۀ نماز بر پیکر مطهر در صحن مسجد مقدس جمکران آغاز می‌شود.
🔹
پس از آن، مراسم در بلوار پیامبر اعظم(ص) و مسیر منتهی به حرم مطهر…</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/447189" target="_blank">📅 20:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447188">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v56tesAjcQVpj23rsEUZ9YgC2U29ZcYO8qEZ3YJ2Jd7xQ-0O2durMy4bXb9TMt__CXKIYj5h2xUlc2Aa8CQ53lI7N0JK4YbAzbSP8qBmFwV0rLjEHDGK96jBcot58jkJZDH8pMvfcnfLsWDwd19tafSIlww6aofB_niDCvEePEsJhXoGjxmwJ1bcx3rp5r5tcYNnog-7z9rT2Nzo4cUhtfAmZrKluSsmuozRRf0YSnQWxW0dbMnU2mU-RmXnmvE1f_G1yRGDdenDQsc2lZjVTXmzI28iFM-aDeWhbeYGUh5Btpo4U-dz1PQxBmNLZpIeIKVqZwi0je3fCqbRSFRoFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ننگا به‌ ما اگرکه ز خونت گذر کنیم
@Farsna</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/447188" target="_blank">📅 20:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447187">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f43e570ac5.mp4?token=VwbfyWlct2M0-mvt_HagXJO9nNqzOZ-E8CXqPJcptXbIBKXxzfJJ7ECR9Km755952f9YsDHV2DMw_RmWTJxcEDU9JOpBLo8faHBKaSFZpEoZnzQOxKHqP6Ye60S3O3VQfdrY4SR24IpsW58yUkS8-MYMcx01FpgTjwSQ1qmkpNYHGbvzisYo4lU5ZmKAeWvKkg1VqVly5I5o3bens8-N9grEbep7hzEj7P_ZR2EN1QeWuKlzzGL4DLnYg6A2sJgt13XcXNkVCOwCjcjIMDnwdTV9j9y06EC3Cawrx5CiWgYuXSPqppKW2fmRNbQarvd8VRDeyLD8RbG9s4oubtyNtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f43e570ac5.mp4?token=VwbfyWlct2M0-mvt_HagXJO9nNqzOZ-E8CXqPJcptXbIBKXxzfJJ7ECR9Km755952f9YsDHV2DMw_RmWTJxcEDU9JOpBLo8faHBKaSFZpEoZnzQOxKHqP6Ye60S3O3VQfdrY4SR24IpsW58yUkS8-MYMcx01FpgTjwSQ1qmkpNYHGbvzisYo4lU5ZmKAeWvKkg1VqVly5I5o3bens8-N9grEbep7hzEj7P_ZR2EN1QeWuKlzzGL4DLnYg6A2sJgt13XcXNkVCOwCjcjIMDnwdTV9j9y06EC3Cawrx5CiWgYuXSPqppKW2fmRNbQarvd8VRDeyLD8RbG9s4oubtyNtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین اذان مغرب در مصلای امام‌خمینی(ره)
@Farsna</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/447187" target="_blank">📅 20:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447185">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb6d485518.mp4?token=PVeeZxdhwWsb9xC__XnePIfFLVX0G9Sdtuql3MMUQNKX4SGDUgVuMnR6NiaMKYROJJsSvtSiJBNLYq4YBG6bgYqI_4fdudYC7n6tk5PLDj7gsqlU2sqOabEFv0WyGXy5spNTGGZMUqlqC9E2PLnutFY2VE7qpGSQMOWRdz65j66bvmYzKkgmloLi_HduMHgnu77X6-_sQAhU-ntx5EzXv0LokPHprjub8dqaanDHn-5veOwWWx9-50VdBNJRjJeropLnBGUc9QX0vk01wNeFx8NMtpfsmXatBipI1pbUO90hH-AACviZVtGdsu8TdOAZPyZm_Teo9CsuyCC_PUBotA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb6d485518.mp4?token=PVeeZxdhwWsb9xC__XnePIfFLVX0G9Sdtuql3MMUQNKX4SGDUgVuMnR6NiaMKYROJJsSvtSiJBNLYq4YBG6bgYqI_4fdudYC7n6tk5PLDj7gsqlU2sqOabEFv0WyGXy5spNTGGZMUqlqC9E2PLnutFY2VE7qpGSQMOWRdz65j66bvmYzKkgmloLi_HduMHgnu77X6-_sQAhU-ntx5EzXv0LokPHprjub8dqaanDHn-5veOwWWx9-50VdBNJRjJeropLnBGUc9QX0vk01wNeFx8NMtpfsmXatBipI1pbUO90hH-AACviZVtGdsu8TdOAZPyZm_Teo9CsuyCC_PUBotA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#فیلم | لحظه ورود رهبر انقلاب به حسینیه امام خمینی(ره) در مراسم عزاداری شب عاشورای حسینی  @rahbari_plus</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/447185" target="_blank">📅 19:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447184">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67407e3e61.mp4?token=vbfuV9BBV54MLxbhM29F-8jwUqrl2Asvo2OZ9diG9n20f4IaQQIhG4-eNtD4bz4agm8-kcnm_dOyIcJxzWCgMKtk5374breKEEmvQY6eG8fvsRYtNsL7KHCnI0hNf_wnOG6O8rFJQornBFC9qBjTaTBet6k9Euv3oGOcfB-4MkAZR2CiRku5kFc4zmjISEecs6_i9sQcLtTkMVOexqsDAVyH845L_DhxXPa81WoiZUyzm0TTLs80lOzr3J6IhBqgVKPTQlgKFAJ_K94j6QEk2oSbsrZ5-nPRNLHUIkFilqI4v6gSgoMbH6lqppZ7_uPMx1-JOxI-P94GWUrFsQriUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67407e3e61.mp4?token=vbfuV9BBV54MLxbhM29F-8jwUqrl2Asvo2OZ9diG9n20f4IaQQIhG4-eNtD4bz4agm8-kcnm_dOyIcJxzWCgMKtk5374breKEEmvQY6eG8fvsRYtNsL7KHCnI0hNf_wnOG6O8rFJQornBFC9qBjTaTBet6k9Euv3oGOcfB-4MkAZR2CiRku5kFc4zmjISEecs6_i9sQcLtTkMVOexqsDAVyH845L_DhxXPa81WoiZUyzm0TTLs80lOzr3J6IhBqgVKPTQlgKFAJ_K94j6QEk2oSbsrZ5-nPRNLHUIkFilqI4v6gSgoMbH6lqppZ7_uPMx1-JOxI-P94GWUrFsQriUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ساخته‌شده با هوش مصنوعی از چهره‌ها و صحنه‌های خاص و غیرمنتظره مراسم امروز وداع با رهبر شهید انقلاب در مصلای تهران
@Farsna</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/447184" target="_blank">📅 19:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447183">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjep0KPlwOUdVV_xKMJ2o1QQThwEWjKtxXEa4vQoMvPOmmdIM7o59wtBsEOSGwtCi70ivyMSIZFhZLRzIy0pBhUnnanQ52X935h6HygGBw1Wv15sHY7OcdRR51grbETs0AzWu3ZrdGdklQgW3sncPcW4xJVmXbQDc2D6Ogr-qh4KsU0UYLAZ9-cCe4WUwZW80aYXcQ_E_zMGfxYSKbOfdzg1SMei7Imay8zrUguoXagXCVoclcbvr3rjGQVuIcmDg8gUqszDM2z5ldvkqPsys1j_cNRcvBG_ojq1yzz5JIzrZTuRGMceF2LZMyj_sEpj7B7h_Avk1f49kQzk7JTHNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
بازدید مدیرعامل بانک رفاه کارگران از موکب های این بانک و شرکت های تابعه در مراسم وداع با پیکر مطهر قائد شهید
🔹
مدیرعامل بانک رفاه کارگران با حضور در مراسم وداع با پیکر مطهر قائد شهید، از موکب های این بانک و شرکت های تابعه در این مراسم بازدید کرد.
🔹
دکتر للـه‌گانی به همراه جمعی از مدیران و کارکنان بانک ضمن حضور در این مراسم در محل مصلای امام خمینی(ره) تهران، از نزدیک در جریان خدمت رسانی این موکب ها به عزاداران قرار گرفتند.
🔹
مدیرعامل بانک رفاه کارگران طی سخنانی در حاشیه این مراسم گفت: اندیشه‌های رهبر شهید یک جهان‌بینی مبتنی بر کرامت انسانی بود. ایشان همواره معتقد بودند که اقتصاد، ابزاری است برای تعالی جامعه، نه هدفی برای انباشت سرمایه. بانک رفاه به عنوان بانکی که نام «کارگران» را بر پیشانی دارد، بیشترین قرابت را با گفتمان ایشان دارد.
🔹
دکتر للـه‌گانی تصریح کرد: در بانک رفاه کارگران تلاش کرده‌ایم آرمان‌های قائد شهید را به دستورالعمل‌های اجرایی تبدیل کنیم. از حمایت از تولید ملی و اشتغالزایی گرفته تا طرح‌های رفاهی برای کارگران و بازنشستگان. این‌ها در واقع پیاده‌سازی همان نگاه کلانی است که ایشان به عدالت اجتماعی داشتند.
🔹
وی به انتخاب حضرت آیت‌الله سیدمجتبی خامنه‌ای (حفظه‌الله) از سوی مجلس خبرگان رهبری به مقام رهبری انقلاب اسلامی، اشاره کرد و گفت: این انتخاب نویدبخش تداوم مسیر عزت و اقتدار میهن عزیزمان است. بدون شک شبکه بانکی تمام توان خود را برای تحقق منویات رهبری در مسیر اعتلا، آبادانی و شکوفایی اقتصادی میهن عزیزمان به کار خواهد بست تا تحت عنایات حضرت ولی‌عصر (عج)، شاهد سربلندی بیش از پیش ایران اسلامی باشیم.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/447183" target="_blank">📅 19:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447182">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/447182" target="_blank">📅 19:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447181">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5764e1d53f.mp4?token=vwLvIqEfIGTcT8tUy0Iw3TIQjXEYcQcvNIG5WrYpsWomG1IBkI_yUPzcVR5lzjvIIU1TEbxUnq6LCAbjA9V4y6l7VVBY74FSwVYOdYl99Luzqpg8mruVzh69avJFR2e6vM4i280pgMq2yTHLJ9uCKW1mxRdXKC5KeMuASXPx_e_7o5fwZBB3gyNMpOzF3oonGEhLe91OyfDpS2VEjyXL0T9NE3b0UKKdJ1qd-xQBy51xCoN4DHO9AbUK1z8LdsSqnyzDWl2-DBmMCm9c0k2L2eNPiApb-2vz7BzDBcNrV2Yi26HtsVUKPcOWCVkWV-hlYrJ1Ybrsn426hsliVt5Ddg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5764e1d53f.mp4?token=vwLvIqEfIGTcT8tUy0Iw3TIQjXEYcQcvNIG5WrYpsWomG1IBkI_yUPzcVR5lzjvIIU1TEbxUnq6LCAbjA9V4y6l7VVBY74FSwVYOdYl99Luzqpg8mruVzh69avJFR2e6vM4i280pgMq2yTHLJ9uCKW1mxRdXKC5KeMuASXPx_e_7o5fwZBB3gyNMpOzF3oonGEhLe91OyfDpS2VEjyXL0T9NE3b0UKKdJ1qd-xQBy51xCoN4DHO9AbUK1z8LdsSqnyzDWl2-DBmMCm9c0k2L2eNPiApb-2vz7BzDBcNrV2Yi26HtsVUKPcOWCVkWV-hlYrJ1Ybrsn426hsliVt5Ddg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رهبر شهید از آخرین دیدار و وداع
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/447181" target="_blank">📅 19:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447180">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9f3b783ad.mp4?token=VPAOK2NCmIro_XW_Ty_hWG-33957ACx1nDhFtVwfgvSVQb9bQIGHz2dg0SbBk50zRMN5QNib0J46bGUV8VmAyuafe_-bEVJEE98UuE-80v4w_I18kVyJe35wyfD9jX_auklpTYySCgW5k_zXlYg--D9zjTdK0CNSGrPxuexIfTVTQtcvqAkc9ikeYRc6Vdg-2Zz5gBSzj5l0lXzqksTmx-i_JpM0-iun1nbYkLpaquNHwhXTCpThsgHmhvD7Ga_iCSGqGvgUKEgKgiVyK23PbQnjz_LFF1ncAvhN16sb69EV__qwUDf6rY2N3NUKyRg7Z32eUhUYZIedUSuUwFgNuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9f3b783ad.mp4?token=VPAOK2NCmIro_XW_Ty_hWG-33957ACx1nDhFtVwfgvSVQb9bQIGHz2dg0SbBk50zRMN5QNib0J46bGUV8VmAyuafe_-bEVJEE98UuE-80v4w_I18kVyJe35wyfD9jX_auklpTYySCgW5k_zXlYg--D9zjTdK0CNSGrPxuexIfTVTQtcvqAkc9ikeYRc6Vdg-2Zz5gBSzj5l0lXzqksTmx-i_JpM0-iun1nbYkLpaquNHwhXTCpThsgHmhvD7Ga_iCSGqGvgUKEgKgiVyK23PbQnjz_LFF1ncAvhN16sb69EV__qwUDf6rY2N3NUKyRg7Z32eUhUYZIedUSuUwFgNuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاضر بودم ١٠ بار بمیرم اما یک تار مو از رهبرم کم نمی‌شد..
.
@Farsna</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/447180" target="_blank">📅 19:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447179">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ca1bcfcdc.mp4?token=hMlybOekSZkO1dXq2XGmFsKwW4n8dfRa0QJshjDoEETV6OKLjzTDDRhCVXLBPReGClNyb4ADq1ZRwh5qJDjJcj6TumWC7nuUTFF7ZMovyC9iYCue0k57bRh3aEchcxgdzjMwvy0Xe0NyoDmT2Y0vCON5_yixDMRDrq5OrmX-JCMLShqvQi1iRhkbD-IL3zTJFi0Yuqm1yJgeN-jFciqhw5HhZbDZWAjmwvSp0Zb89pDZdYKWSX0sC7AyCeua3O2PWz_tH46Lqb6IyD3SyLjgXO3YZnBHLeNnS3GUuV35e0Cvp2cAHBfUXv80sxK64bN-GQeS0-wsk87J5a5pVvzTgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ca1bcfcdc.mp4?token=hMlybOekSZkO1dXq2XGmFsKwW4n8dfRa0QJshjDoEETV6OKLjzTDDRhCVXLBPReGClNyb4ADq1ZRwh5qJDjJcj6TumWC7nuUTFF7ZMovyC9iYCue0k57bRh3aEchcxgdzjMwvy0Xe0NyoDmT2Y0vCON5_yixDMRDrq5OrmX-JCMLShqvQi1iRhkbD-IL3zTJFi0Yuqm1yJgeN-jFciqhw5HhZbDZWAjmwvSp0Zb89pDZdYKWSX0sC7AyCeua3O2PWz_tH46Lqb6IyD3SyLjgXO3YZnBHLeNnS3GUuV35e0Cvp2cAHBfUXv80sxK64bN-GQeS0-wsk87J5a5pVvzTgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین قول‌وقرار حسین یکتا با رهبر شهید انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/447179" target="_blank">📅 19:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447178">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4wO8b8Pb8RwUt8RUt6gyaRYjozdFEMKa6VVnH70A-tFaVjvnp6WV9s5QXA9yrWgPswng4Ybo7k-JiJw_d4tYRQ6mhuP7SsiDnWllMJdOKje0BWQMWXUojNTSlI0EzBEoEKmS3sQtzDt9-0krZo2_63xG5vof24Fe9iviPVqrfqA9Db8WCEGo1V-eiuSqL4Ht0osqRoNKzt6YJNExULJTPw8yyBbc3IcGMMKzeFL0PS6loO9q5KdsiF6cumY4w9lMOI4GMgYoL4H3ynw3L05seo0NH_hrgpQpTt-R-ucg6z82lycBSt3TwRV1H3JSO9PletWzsNO2OK90j33FEmbqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتصاب مجدد حجت‌الاسلام والمسلمین اژه‌ای به ریاست قوه‌قضائیه
🔹
حضرت آیت‌الله سیّدمجتبی خامنه‌ای رهبر معظم انقلاب اسلامی در حکمی، حجت‌الاسلام والمسلمین محسنی اژه‌ای را بار دیگر به عنوان رئیس قوه‌قضائیه منصوب کردند.  متن حکم رهبر انقلاب اسلامی به این شرح است:…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/447178" target="_blank">📅 19:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447177">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
برنامۀ وداع در مصلای تهران به‌دلیل ازدحام جمعیت تا ساعت ۲۲ تمدید شد.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/447177" target="_blank">📅 19:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447176">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">یک استان دیگر عراق روز چهارشنبه را برای بدرقه و تشییع پیکر رهبر شهید ایران تعطیل کرد
🔹
استان مثنی عراق، نهمین استانی است که روز چهارشنبه را برای تسهیل مشارکت مردم این استان برای بدرقه و تشییع پیکر حضرت آیت‌الله العظمی سید علی خامنه‌ای، رهبر شهید ایران تعطیل…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/447176" target="_blank">📅 19:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447172">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2ikqEI2Zgav3TABhPr8Exre2soVAevZjpA3Y70V0F9m8pCpplaVkJOQnBc-Dja56M9xZns0-SeiNZuH-FXNlV9awKlWyErTDEnl9cBv2m09JPcJUe0Hm6n0oPd_AYUeG2r9T_U9bfDy8wsxelzBjGvTY_4ENvnsG5JiSKwHjog92pJl9qKSjct337hAR4IYwXSCNfG914Pu5jqkgS7-TG5oJsOwVlzaui5OJF_y_nU3fE_qc9OHlRyptROLvdbnqA0OlsALrstXkudHFDwOWKA3SwdgVkOxl22DJUU52wm9ZKAUt8ElgM-5v1uHdMBl30ZWHR-1XVZLpgI4iszy8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتصاب مجدد حجت‌الاسلام والمسلمین اژه‌ای به ریاست قوه‌قضائیه
🔹
حضرت آیت‌الله سیّدمجتبی خامنه‌ای رهبر معظم انقلاب اسلامی در حکمی، حجت‌الاسلام والمسلمین محسنی اژه‌ای را بار دیگر به عنوان رئیس قوه‌قضائیه منصوب کردند.
متن حکم رهبر انقلاب اسلامی به این شرح است:
بسم الله الرّحمن الرّحیم
جناب حجت‌الاسلام والمسلمین آقای محسنی اژه‌ای دامت توفیقاته
🔹
با قدردانی از تلاش‌های ارزشمند و صادقانۀ جنابعالی، به استناد اصل یکصد و پنجاه و هفتم قانون اساسی، جنابعالی را به ریاست قوه‌قضائیه منصوب می‌کنم.
🔹
مجموعۀ مطالبات مطرح‌شده از سوی قائد شهیدمان اعلی‌الله‌مقامه‌الشریف و نکات مذکور در پیام هفتم تیرماه ۱۴۰۵ اینجانب، راهگشای تحول، شکوفایی و دستیابی به قوه‌قضائیۀ مطلوب است.
🔹
امیدوارم با همت مضاعف جنابعالی و قضات شریف و همکاران ارجمندتان در دستگاه قضایی و دعای سرورمان عجل‌الله‌تعالی‌فرجه‌الشریف، ملّت بزرگوار ایران از نتایج آن بهره‌مند شوند.
سیدمجتبی حسینی خامنه‌ای
۱۳/تیر/۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/447172" target="_blank">📅 18:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447171">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571f3614bb.mp4?token=dTvisllvuiE9TJFUqmQSVUMALfkmNZwGWktPXsdxpBfN5so7NCcd2HhJQgywmVANxk3qGpvypl6b2BVVs_1kBnQkv1Kkmo8CIf0jfQ_XNGOHPG9CwXGKzUOT1b7GyVvn2NHiLuQ0xNdcqMS6z0ncaYd16V3BuSrBA1HO9YFBGFGzuZBepCn8d044LanbTa-Sq73J04V6asyrkUPHU3IYHjiLegYDKlcOGuOwoimHPwzK1i0MGsiSc-4xlnxuOebxJTvwPVBsmBBEnMs8FQmh3cPSUf5aWkas_6cuuX_Y7px07HM08mHZ4lx2jX-rmx04dK0cau7dZxDGetWdguRhhbIukRvdamQFuPti331JPEcU86VgeVODNlghjYT8NyBrCvvAfHdGdX7dSRysri00khgh_-_2uCs9gN6uffLetnSEZhpi5Np4xl8FaeY0ydVSpR3eJSLNSBMAaUpAMEKCu4kQZd70UsgRMnJ4UBJtZ6kUkAMThxDPe1qD0qug11WE8s_NG4uNBRjuJMKPJ0J3rtbB7HCdjykitLcwE8hozMDSeTWHJ5_2zWJHuBfh3-7DiB4H1wcttBWUIZAAkjYWHl1wDK4XmjPCpzN0aXTcOQF-7JEdx9FTHsPydJO3JjQ9APE51SbXG1OO9rfU_ukpqJRYVZPxXm9jYuc551tu0qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571f3614bb.mp4?token=dTvisllvuiE9TJFUqmQSVUMALfkmNZwGWktPXsdxpBfN5so7NCcd2HhJQgywmVANxk3qGpvypl6b2BVVs_1kBnQkv1Kkmo8CIf0jfQ_XNGOHPG9CwXGKzUOT1b7GyVvn2NHiLuQ0xNdcqMS6z0ncaYd16V3BuSrBA1HO9YFBGFGzuZBepCn8d044LanbTa-Sq73J04V6asyrkUPHU3IYHjiLegYDKlcOGuOwoimHPwzK1i0MGsiSc-4xlnxuOebxJTvwPVBsmBBEnMs8FQmh3cPSUf5aWkas_6cuuX_Y7px07HM08mHZ4lx2jX-rmx04dK0cau7dZxDGetWdguRhhbIukRvdamQFuPti331JPEcU86VgeVODNlghjYT8NyBrCvvAfHdGdX7dSRysri00khgh_-_2uCs9gN6uffLetnSEZhpi5Np4xl8FaeY0ydVSpR3eJSLNSBMAaUpAMEKCu4kQZd70UsgRMnJ4UBJtZ6kUkAMThxDPe1qD0qug11WE8s_NG4uNBRjuJMKPJ0J3rtbB7HCdjykitLcwE8hozMDSeTWHJ5_2zWJHuBfh3-7DiB4H1wcttBWUIZAAkjYWHl1wDK4XmjPCpzN0aXTcOQF-7JEdx9FTHsPydJO3JjQ9APE51SbXG1OO9rfU_ukpqJRYVZPxXm9jYuc551tu0qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دانشجوی نیجریه‌ای: مردم ایران دمتون گرم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/447171" target="_blank">📅 18:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447170">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfa5a4fb9d.mp4?token=f4X9NVxRD8UwxbBnbsdksBcDpwuavotzKm0NxUF6DSCKhtdXtMqjg8e5j3qWlzxmUEmsuJ1WW8ejCE5Jis8e-ll2OvqBzP-wZ1Nnxwqm_Ci5mW8N8Rz226bYNONQ1acBevgJblg7_G9pbkcvBQD5ZqG-5Dmcilh0vpptJc-GfnYZuGRuYSPrfBoRXFUQhmv0Wk8tnKAOsg4mxcd6yyyu3sOqlsd_1VPDVql_6V22jmKGuTr_AxhHWySFqupIaKQvJeFla5cD4ktNZtxUSL9jix8DUlo7ALKntAL12G85tElEJBhWVRAl7-SY2XK2QYY4xQExF2X6w8SqwHyNUDRznQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfa5a4fb9d.mp4?token=f4X9NVxRD8UwxbBnbsdksBcDpwuavotzKm0NxUF6DSCKhtdXtMqjg8e5j3qWlzxmUEmsuJ1WW8ejCE5Jis8e-ll2OvqBzP-wZ1Nnxwqm_Ci5mW8N8Rz226bYNONQ1acBevgJblg7_G9pbkcvBQD5ZqG-5Dmcilh0vpptJc-GfnYZuGRuYSPrfBoRXFUQhmv0Wk8tnKAOsg4mxcd6yyyu3sOqlsd_1VPDVql_6V22jmKGuTr_AxhHWySFqupIaKQvJeFla5cD4ktNZtxUSL9jix8DUlo7ALKntAL12G85tElEJBhWVRAl7-SY2XK2QYY4xQExF2X6w8SqwHyNUDRznQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در پناه اباعبدالله، زائر کربلا
◾️
نوحۀ وداع سیدمهدی حسینی برای رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/447170" target="_blank">📅 18:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447169">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08b7196f32.mp4?token=mS2YULWkSRLoBaVSaRcGwCbD9YZmdAC-CEcC48l5WZDuGwoLHYHQpm726a73EC36wXmDUw8JsV7TLVHGcW3t0BREYcMalF94GC2GtEzJAuLrJhmrvIqJymCnylv2Gh4HjvB2EwoNSZV6KhZm6dm_XEIy3Tp9BXxiUU1Dz7TXo9UdrKjnJ48BbDi4-TDSI3kOrOdA4ZaeEnyfbIn1-FtveA-unab8zYuJzB1052Y9MxpEHMmcKBzP0YIj8-F2AdiRwMZC02toOuu7e7GHuU2Poj63JO8JsWLSMT8G-IdhPfNXddFwvJuyRA-5NDWEJJLzL4gwPMD4hQfvQTz5IyR05g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08b7196f32.mp4?token=mS2YULWkSRLoBaVSaRcGwCbD9YZmdAC-CEcC48l5WZDuGwoLHYHQpm726a73EC36wXmDUw8JsV7TLVHGcW3t0BREYcMalF94GC2GtEzJAuLrJhmrvIqJymCnylv2Gh4HjvB2EwoNSZV6KhZm6dm_XEIy3Tp9BXxiUU1Dz7TXo9UdrKjnJ48BbDi4-TDSI3kOrOdA4ZaeEnyfbIn1-FtveA-unab8zYuJzB1052Y9MxpEHMmcKBzP0YIj8-F2AdiRwMZC02toOuu7e7GHuU2Poj63JO8JsWLSMT8G-IdhPfNXddFwvJuyRA-5NDWEJJLzL4gwPMD4hQfvQTz5IyR05g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بدرقهٔ ۲۵۰ شاعر پارسی‌گو برای ایرانی‌ترین رهبر تاریخ
@Farsna</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/447169" target="_blank">📅 18:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447168">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33d6aad76b.mp4?token=Stz3eb2lAYeMqwWIRUAmixZoyOptoPOH5zVnGbImoiYtwZ1tBXkY8jPHmmnbZeh4m-G62KOU8Z5m6C-iSkRTl6KiJ4GK09zSv1QFi6m6dzBMRo25ej06iRAq6Vz2UlEUt1jEEvZzhaUP4mBDZeYWFHTxq0mhoBlTF656o2hhlj5yi7rqsn7afQ2bSDIC1f7bpyIck6tDHI83ZhpwXJiDj1pvLTryIMw3DUQGwY8tgnfnQddvc3_DMxbv3FiadXvMWFHlt7dhI67CWnpcEqPWxbmfwi_ZEwQ8ydDRnHwtjCqpOdIshFtVxvizfhfzFLpCCzEuwBqjX2nrFbfskhHdSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33d6aad76b.mp4?token=Stz3eb2lAYeMqwWIRUAmixZoyOptoPOH5zVnGbImoiYtwZ1tBXkY8jPHmmnbZeh4m-G62KOU8Z5m6C-iSkRTl6KiJ4GK09zSv1QFi6m6dzBMRo25ej06iRAq6Vz2UlEUt1jEEvZzhaUP4mBDZeYWFHTxq0mhoBlTF656o2hhlj5yi7rqsn7afQ2bSDIC1f7bpyIck6tDHI83ZhpwXJiDj1pvLTryIMw3DUQGwY8tgnfnQddvc3_DMxbv3FiadXvMWFHlt7dhI67CWnpcEqPWxbmfwi_ZEwQ8ydDRnHwtjCqpOdIshFtVxvizfhfzFLpCCzEuwBqjX2nrFbfskhHdSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت یک سلام برای بدرقه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/447168" target="_blank">📅 18:45 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

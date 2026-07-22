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
<img src="https://cdn5.telesco.pe/file/YDgGIKeUES_mT1P4WbRXqIWyVu2jye9MQxJXLTgqJkjohUcaDUc4z1Bghr96k_6trDA9IWW6tq4nYtIy2_0s7579sc4j0aI1vds7jbHKg0AM1eEtEGZKHdTsgZk6aUSSafK6pJKtiA76qG0wSP3NOF8nFiWSo1gCUDFU5ImKjpiZPVcAC8UQGjnPEy2OEReTvd6wZWXvXJerl7sTpqP-1jwHXjgENYE_8fao6po0pzRneDXkdxwofxVHfCskWG9fDgbd165C7fxLXXoe_RVVzlfsOQCaHrBG8kiXGVYp-EMY1mKcC0w46on4BrcjjCMkXmTtGPNkTHgoobanHdzhLQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 544K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 13:46:19</div>
<hr>

<div class="tg-post" id="msg-101550">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c3187f185.mp4?token=N1deeG0fUwev68ahAWeMQdmE5VDayCDG_pxmhIBL6DYdsG0Q6NX_9g5ZDLmdvsayS5fHxDAshONaUrH0d-RlyvtyAWFGYZOdtuv3oFPUg0_uLuL43lAvcLmifnExxwGYKUIUfRb-sDvJZyenEEdUir9RyPOJVnSHkdJd6X0SkYjxSncQ805FnEg07EEJvtyoI7b7ooslDgn8screXalcOvR3C0F7Ugdb18cFQOFixSBOmp6HBdkCSDQiuqMa0gpODxGig0uQiySO2n3LHBUVYR91749GNOsth8cP9jDYWtqg2lCq3dht4TxpYgxh5a30-ngZXKf2QKzh7nAR5HfzTjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c3187f185.mp4?token=N1deeG0fUwev68ahAWeMQdmE5VDayCDG_pxmhIBL6DYdsG0Q6NX_9g5ZDLmdvsayS5fHxDAshONaUrH0d-RlyvtyAWFGYZOdtuv3oFPUg0_uLuL43lAvcLmifnExxwGYKUIUfRb-sDvJZyenEEdUir9RyPOJVnSHkdJd6X0SkYjxSncQ805FnEg07EEJvtyoI7b7ooslDgn8screXalcOvR3C0F7Ugdb18cFQOFixSBOmp6HBdkCSDQiuqMa0gpODxGig0uQiySO2n3LHBUVYR91749GNOsth8cP9jDYWtqg2lCq3dht4TxpYgxh5a30-ngZXKf2QKzh7nAR5HfzTjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صحبت‌های مجتبی‌پوربخش علیه میثاقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/101550" target="_blank">📅 13:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101549">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c0345d2fb.mp4?token=tzRApRhnnucL9G2lNgbui79nLMnWG9b0BT6pswkMFcWsPZJhdhSQ1KVnlymIv0kY_8x_C2Q1ZOHN61U-lgzIld_JjzUSiUGq8H0GV_fgEUbAX6M3oDaPH6oIBU-JDQsuCIKq2IuJSC8cyVLA_HrVrZ78lmIXtu6umoxPgUqAnemCRgr5ZASgWIBt0QGRWbw2MFWGRk1IqEq8HReC8HMbX82RhuDgq7Gi9LWemebqK7_1ouZ-Pn9akUglPSMXkSmikU5sj9A6zI90atsVsvQK84uPiwmWT1Bmyv0h9ExddpNp-2HCdPcMZGOsWZdBlK8WbNsIj7SbpwS0GytdNP_7bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c0345d2fb.mp4?token=tzRApRhnnucL9G2lNgbui79nLMnWG9b0BT6pswkMFcWsPZJhdhSQ1KVnlymIv0kY_8x_C2Q1ZOHN61U-lgzIld_JjzUSiUGq8H0GV_fgEUbAX6M3oDaPH6oIBU-JDQsuCIKq2IuJSC8cyVLA_HrVrZ78lmIXtu6umoxPgUqAnemCRgr5ZASgWIBt0QGRWbw2MFWGRk1IqEq8HReC8HMbX82RhuDgq7Gi9LWemebqK7_1ouZ-Pn9akUglPSMXkSmikU5sj9A6zI90atsVsvQK84uPiwmWT1Bmyv0h9ExddpNp-2HCdPcMZGOsWZdBlK8WbNsIj7SbpwS0GytdNP_7bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
خاطره بامزه علی دایی از معلم زبان خود و کریم باقری در دوران حضور در بیلفلد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/Futball180TV/101549" target="_blank">📅 13:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101548">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbd74933b1.mp4?token=KmKqFpGUZcYaLkG4QJ9YnlSulj9JLUJpuSjV5yv_--OTOOMkjUMd711mERiF8Qn6_O1a63y6slThKJxgOBjAoIyiS9jc5P9jGuJrLjzcmwuIGHJxwTiRLa2Ft4tnkDUyYHrZMNOQ3HFVh7EkmEohZNCS9OBiF_d4ExUdwvy2hMXuntW2A-VBPdy3BJRcRuXEchqBqdQu3Ss6fxO7iJkwYVCqI9_85pGt-BDbyG_DbGe27Z6p-lkipOZoCLAVj4HPH13f3GuZcGh38Se8rzpgS7nIq5GvnjjaK03eoxzTHJlQgzMfzptJj_WEect33CwO8lI6AgBqsp4ovHR44sWvsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbd74933b1.mp4?token=KmKqFpGUZcYaLkG4QJ9YnlSulj9JLUJpuSjV5yv_--OTOOMkjUMd711mERiF8Qn6_O1a63y6slThKJxgOBjAoIyiS9jc5P9jGuJrLjzcmwuIGHJxwTiRLa2Ft4tnkDUyYHrZMNOQ3HFVh7EkmEohZNCS9OBiF_d4ExUdwvy2hMXuntW2A-VBPdy3BJRcRuXEchqBqdQu3Ss6fxO7iJkwYVCqI9_85pGt-BDbyG_DbGe27Z6p-lkipOZoCLAVj4HPH13f3GuZcGh38Se8rzpgS7nIq5GvnjjaK03eoxzTHJlQgzMfzptJj_WEect33CwO8lI6AgBqsp4ovHR44sWvsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
وضعیت رئال مادرید در این روزها.
🧐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/Futball180TV/101548" target="_blank">📅 13:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101547">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlPguFKVFnNEQphagBLqSVEu1GPSrs2KKllNfo54giB5oNvEeiB6M4q9eEzxL810AMEh1i6s7OOelSNyuoY2NSTf7msAzPW-dMb79znVFWMJWyekHNgazf2MhICRlv-MgPH1XkhYVUVQQkikPm3zbiFQfZhSS3EFJH-7LNRwsgYWfTt4vp-V_CecTEe3tYIIU2SGzia3CK62E5hi0Rg2dqNX3zsCbK-EHvBUV4qwz7dykgR6kW5iHqHGEyVewjloSaEQohAFQB9kuHIkTTuWf5yeMqorrvAB9K1d63eiVIcgr2i-X0vaVP8ivP5jItMvyicmz-qOWof0L2_4Zn2-Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
وینیسیوس و زیدش بعد عمل زیبایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/Futball180TV/101547" target="_blank">📅 12:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101546">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e1e8799b7.mp4?token=EUr45thmLZgb-Rppmqoy0Hfbko_tfPX6AZCSe1LvjGJV2xvWnsyzX-VyYKMJb67LNoZVV7KumD46ZgU5116v7U3igmJuvCr-Rq_DIfxz7vR8-LXEFVY85xwsIc6tjsW9Z_1ncvLRDRtejHiwBDRe2nt-Szk6AWhEOu3xsKaC5mCsukNX-tSEOlGVHoXUmEu25EXfQjmacnk07-RNtVOUI5SwhUgE1HxuoPAzkSAKqJmXeHiAW9EgsxvYOxrajxKYZfK5XY0rqGRpXcHWZEcEYLFsigOHoxmu2mzdMppOJCGG9cB5ylunUJ6jFlL1ybKgZC0bGeH6CRtzQCz9bAZ2f58_KxW3jO7oK1Zti4PWM33i8C_azbm6_q77lCzqacKqRURruxPTrM0fXheIuYwyZIHYplfmYBRa_p-cEAdwQ9XDfZveqgTnLvR4kavwNwjn5v4b6uthZ-B1d1RQcZDF2HdyHzmPrNQSY8cBpJp3ygif6idVBOYL2euvrCPIfcC6QEOBj3LIDVP-Shy-fX0AFHiBwaOIITA64Og_AytehFa6-4lE3X10RRYdZ_XBdFy6mKNf8Yv41DJMvCGtr2356sDTdGQy4m6XwX75zKy3oIpvRQnqZxhOY_IX0oT8nkDvPYHYALEj9t-1ZTYjRHRjlLwX10QhMQjpUk5yH-Cxum4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e1e8799b7.mp4?token=EUr45thmLZgb-Rppmqoy0Hfbko_tfPX6AZCSe1LvjGJV2xvWnsyzX-VyYKMJb67LNoZVV7KumD46ZgU5116v7U3igmJuvCr-Rq_DIfxz7vR8-LXEFVY85xwsIc6tjsW9Z_1ncvLRDRtejHiwBDRe2nt-Szk6AWhEOu3xsKaC5mCsukNX-tSEOlGVHoXUmEu25EXfQjmacnk07-RNtVOUI5SwhUgE1HxuoPAzkSAKqJmXeHiAW9EgsxvYOxrajxKYZfK5XY0rqGRpXcHWZEcEYLFsigOHoxmu2mzdMppOJCGG9cB5ylunUJ6jFlL1ybKgZC0bGeH6CRtzQCz9bAZ2f58_KxW3jO7oK1Zti4PWM33i8C_azbm6_q77lCzqacKqRURruxPTrM0fXheIuYwyZIHYplfmYBRa_p-cEAdwQ9XDfZveqgTnLvR4kavwNwjn5v4b6uthZ-B1d1RQcZDF2HdyHzmPrNQSY8cBpJp3ygif6idVBOYL2euvrCPIfcC6QEOBj3LIDVP-Shy-fX0AFHiBwaOIITA64Og_AytehFa6-4lE3X10RRYdZ_XBdFy6mKNf8Yv41DJMvCGtr2356sDTdGQy4m6XwX75zKy3oIpvRQnqZxhOY_IX0oT8nkDvPYHYALEj9t-1ZTYjRHRjlLwX10QhMQjpUk5yH-Cxum4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇯🇴
استقبال از ادهم‌مخادمه داور اردنی(داور چهارم) فینال جام‌جهانی در بدو ورود به کشورش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/101546" target="_blank">📅 12:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101545">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UntL7sUKiqjF1WdAMXd-83SJV2repKIwJeT7B0c_K-sD_jjjz6hZo9ydDWxTQ6VyQEiwWApC6t5BLr4AP-8-oNRD5-Es3-ZnFyf59J9ltKNQFZ-4uXvZbpevei2uIt7NkicRblQGLFmHYlgXHDNNTi4qUIKYYuNF_sDN1rkcA7wasvfXlOGiQOeHrAON6S2z5CtXKmyuiXURzapZKdNS5_mtLjKctxBcEgKsGEvjhRH_YKIrS_Rh1vh7ZF1wzQ7YoTe6vixp-JJrCBbSS5WJAs62zmLgcpo2kfx1Fk2Sby_czfLAa1TslCRBVmjdLzjBgd-SxluNyGW8JiffwfCXUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
۶ تیم قطعی صعود کرده به جام‌جهانی ۲۰۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/101545" target="_blank">📅 12:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101544">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
💵
پرداخت آسان و سریع با تمامی روش‌های پرداختی
📣
30% فریبت ورزشی برای واریزهای کریپتوباکس (ارز دیجیتال اتوماتیک)
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/Futball180TV/101544" target="_blank">📅 12:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101543">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYDlz1TAvxceBMDoOZS5zFCmQtT4mFzkDBApSaVoTkjR3YEbEO63gG0YOdORovBKHUjA-AiDqdmqVX-NEA0YaWb2zkOfYQzpZgI8_JY9GG6elBT27seXJdej8pwXZZAZLS2eEz8Md1KSO2SUNHaTqjoC8SEkNiH3aNJagvY5LMICefwXy5oFYViONaIqAAgAcmsKmOfPZIiN4GKvWnbNiJXuF4OxqhfKQocOuZZH8b0SYo6xD2FroQacBdb5bfItzhFRhtADQ6DgivYC4JU9eTO6E2gj9CKhLtWA7S4szdne7k9N5Zlzb6eyKTwqa4eMx5DRKbwkFhpp1UZWypk7zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBET
💎
🇪🇺
لیگ قهرمانان اروپا
⏰
شروع بازی ساعت 20:30
🎁
100% هدیه ورزشی ویژه اولین واریز
💰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/Futball180TV/101543" target="_blank">📅 12:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101541">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbcad2324d.mp4?token=hIQxRA-NyvVxLMUNPpDiwiKixU2SvN_wTd0qvLMRzgkx5cc5gNI-rtmmZDTIl4GlcdGyabpZSbhnyRO9d8-fGMD6LnfVQC5LaIDUvBGa8nBqnERF9O5vkOigkUvpcuLLHo9fRAp8S9TTD5h8DbZB2xs9svJQz5NQohvIIB11zqJpD_5YZcb2kW-AnPgaHGsYdfNHwsHZjlWOmes3mivFkAa-EYpEqH6uKOiDcA_mneZHmm_OyaINZgsp1DB6_KsYZx1HOIMmUkXfbocQkgDnPSlJPqz_gyj7RWs4Qw7fBTZ6O2SMbYP5ndUHpuGOsprzqYHZbtbJ8vPWxR_DlZ1KRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbcad2324d.mp4?token=hIQxRA-NyvVxLMUNPpDiwiKixU2SvN_wTd0qvLMRzgkx5cc5gNI-rtmmZDTIl4GlcdGyabpZSbhnyRO9d8-fGMD6LnfVQC5LaIDUvBGa8nBqnERF9O5vkOigkUvpcuLLHo9fRAp8S9TTD5h8DbZB2xs9svJQz5NQohvIIB11zqJpD_5YZcb2kW-AnPgaHGsYdfNHwsHZjlWOmes3mivFkAa-EYpEqH6uKOiDcA_mneZHmm_OyaINZgsp1DB6_KsYZx1HOIMmUkXfbocQkgDnPSlJPqz_gyj7RWs4Qw7fBTZ6O2SMbYP5ndUHpuGOsprzqYHZbtbJ8vPWxR_DlZ1KRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
بازی‌های افتتاحیه جام‌جهانی ۲۰۳۰ به میزبانی سه کشور آرژانتین، اروگوئه و پاراگوئه برگزار میشه و سایر بازی‌ها در مراکش، اسپانیا و پرتغال خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/101541" target="_blank">📅 12:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101540">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cde737c1a.mp4?token=RmfqyjUIPrk_jNYEjgYMaxYJRnQ-DhoWP2M99XTWpzNxeERkMzmGCfPh2_w6cJaQGkOQEekxoTAtr-FxoFYgrEx3tuyVItIZanp1CQBDTYhvRdXG57RY4kSQxKUGmaRKoLBwXU8B0ehIBZz5YJYMB14-wV-UCGtocITKIgNZ6aj7b0SqcH30Oi89vC-MePXTAcT4jcuPPz-1cOVQFhFfIukuVjL8n-Ba48hvC-OPzEym49ii9IMm_xJYWrt4tuLLjVbU_l17QRULWh7sTetRuTCIUrccWzfCigCJVbB1eOyn8xopuC-utKnJM2dFc5C6X53gjebNjKaxkPe3_1UB7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cde737c1a.mp4?token=RmfqyjUIPrk_jNYEjgYMaxYJRnQ-DhoWP2M99XTWpzNxeERkMzmGCfPh2_w6cJaQGkOQEekxoTAtr-FxoFYgrEx3tuyVItIZanp1CQBDTYhvRdXG57RY4kSQxKUGmaRKoLBwXU8B0ehIBZz5YJYMB14-wV-UCGtocITKIgNZ6aj7b0SqcH30Oi89vC-MePXTAcT4jcuPPz-1cOVQFhFfIukuVjL8n-Ba48hvC-OPzEym49ii9IMm_xJYWrt4tuLLjVbU_l17QRULWh7sTetRuTCIUrccWzfCigCJVbB1eOyn8xopuC-utKnJM2dFc5C6X53gjebNjKaxkPe3_1UB7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
علیرضا جهانبخش: به فردوسی‌پور قول دادم که لباس محمدصلاح رو براش بگیرم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/101540" target="_blank">📅 11:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101539">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glRESzEk3xcRE07uYECnsnZzCJj1BDPeLaWqO6z3oMZOJ1U6BATAAT-dJiOlakHDkjiJr_5zuXtFCxEz2D_N7vgDi5vnHDc3VYhvRKgUrXYDYU5NF6KKuf-y8KsPa0SjNNSTznx93_RJZbqAXsl4z4IKcYvRBpNDlZh5UXQSpGQLCL4VUGwpfO7BpRFUFPGCrtkGuyUGm-bry57MNTQgEve4y-WiaiEpY0H5_nfktWx4SmuU_gvq8a7_mlWxcLc7RroGssSovUqU16ZJ9svA6wJ1S399bjTcGhLugjCrTYVA2B6ztX3yJxsEgiauYHaE5AyTNcEYCVJ5i10JiNATwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌دوم منچستریونایتد در فصل‌آینده مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/101539" target="_blank">📅 11:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101538">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovxvhk8mIgsyqcCjDLmAjwJj_1-nWdK-5RT5PcW9vGEejH1GC_-cjxDM-JT3zaJxgtbTMr6CD0W5Dsp4Kg7vEy4fjCB6grPnFGZuLfSv0E83AU2RFs2v5YCbrCN9V92ph7GXyjgUvXc1ESwruZ9HUWDCaYWZ8IQbEblA8sC5gDJbdirhxUNVYfgQTWx7JbufdLzAVzJIEF3l3z4iVlS9R-mrP0k1lpsAu7Jyt5ZW9SrfoSy-pagUnbq0QclepUDPh07844gfj5M8tcwx2bDsYDG7Yo7-JMqhYIq7i92Z3B0YF4zot4i-N9h8cR_Q08cKqAIrLn5o4XQI-oOsAeJx-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
حمایت یحیی گل‌محمدی از عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/101538" target="_blank">📅 11:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101536">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/330d45af26.mp4?token=mjzm0YVkWQMM_lz9FWMn0eTxdyIwNg2XcsBbYzJXC0G_Nq3wm7q3vHPeaaq2OECsJwqfbuUZX7PMuFqJeJzjTNjLIL5KVV484ZPOuslctsAvkid3wF5ODjQy9fbbNu2IB0WqkdF3j6FfZ4UMziO9MvevlxryvtIU3RBZKPZWvkmzz0DB5oh8FODDWpB-o6ag3gMG74Gl1OMI3iAQwYqTzcYejR4NrgnEatp4sr9lyFDvonN7tPh_uzDSKOk3ZEhKXzdy2HVGxvirjyOc89F6qII0ceGfdoqaKh4_2MME9lshJXtrsuZ1DHYuR8cUBTvBRedYXgh4PEYOHXCTBYUDMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/330d45af26.mp4?token=mjzm0YVkWQMM_lz9FWMn0eTxdyIwNg2XcsBbYzJXC0G_Nq3wm7q3vHPeaaq2OECsJwqfbuUZX7PMuFqJeJzjTNjLIL5KVV484ZPOuslctsAvkid3wF5ODjQy9fbbNu2IB0WqkdF3j6FfZ4UMziO9MvevlxryvtIU3RBZKPZWvkmzz0DB5oh8FODDWpB-o6ag3gMG74Gl1OMI3iAQwYqTzcYejR4NrgnEatp4sr9lyFDvonN7tPh_uzDSKOk3ZEhKXzdy2HVGxvirjyOc89F6qII0ceGfdoqaKh4_2MME9lshJXtrsuZ1DHYuR8cUBTvBRedYXgh4PEYOHXCTBYUDMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تمامی قهرمانان جام‌جهانی در یک ویدیو جالب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/101536" target="_blank">📅 11:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101535">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41b3828f7c.mp4?token=NMHbetrcKCoi9EAla8litVSh3F-vaLZi1mPW4SbBL01KE7kS7SxjXJdxddXrQlXcbJWyLXgyEkEr59yv2mG03-6Nspd0azaKFsrsIwL1aV_gsOdWL43oQ-jftcHKP8k0IBO1OiyFNXT_nkpH7m9ntdnsfH7t4kwwhzk7qtk-EDd2Fs3HNx4smdgWUoMxkzbkA9LgBMnyahFDDNo5hXdGqURGipQf7I3SwoKKtKJLya_ILrd1798vvnRHEuReIg1-qomLHvLI_lhWOp2runLybmjbGOCkwtrcSGpCEZqnxm3Tbv46hhuQzNN7cCsdodI2o9TAr1DqUEEhJffMWizAQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41b3828f7c.mp4?token=NMHbetrcKCoi9EAla8litVSh3F-vaLZi1mPW4SbBL01KE7kS7SxjXJdxddXrQlXcbJWyLXgyEkEr59yv2mG03-6Nspd0azaKFsrsIwL1aV_gsOdWL43oQ-jftcHKP8k0IBO1OiyFNXT_nkpH7m9ntdnsfH7t4kwwhzk7qtk-EDd2Fs3HNx4smdgWUoMxkzbkA9LgBMnyahFDDNo5hXdGqURGipQf7I3SwoKKtKJLya_ILrd1798vvnRHEuReIg1-qomLHvLI_lhWOp2runLybmjbGOCkwtrcSGpCEZqnxm3Tbv46hhuQzNN7cCsdodI2o9TAr1DqUEEhJffMWizAQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی پول نظرتو عوض می‌کنه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/101535" target="_blank">📅 10:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101533">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/191f51b3e1.mp4?token=XfC-U8aJ0d2lc_VFjAY4wSS7-T8lQcUmaLUBq3mpm2QnQ0rHpYV3kwFYSwG9Yqh6RAs-d9x5-6F7bwASp5C8R_Mx86MCK2FUb5ybPNOgU2LiY2_O2hQmIcdt0ZVqMbJD3L5FB50unpUhdt0UQmdv3eJy9J1V-fkuL0IUFF1iTy6uWkWBCsH9EfJpc3LrcWXO82KXal0JEgRSkb-1PCC5tS8b41NLWhLxmm7cqpRwI3w4Xb9B1ML7WmBiGkejOl7Dj0His3pGNznzD0q0yiz9pCgfEYLao2U8L5KmV2n6qb4YD2pqgfwkrFTOlpuplrOUzJX9cljjH969pjx0sFusZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/191f51b3e1.mp4?token=XfC-U8aJ0d2lc_VFjAY4wSS7-T8lQcUmaLUBq3mpm2QnQ0rHpYV3kwFYSwG9Yqh6RAs-d9x5-6F7bwASp5C8R_Mx86MCK2FUb5ybPNOgU2LiY2_O2hQmIcdt0ZVqMbJD3L5FB50unpUhdt0UQmdv3eJy9J1V-fkuL0IUFF1iTy6uWkWBCsH9EfJpc3LrcWXO82KXal0JEgRSkb-1PCC5tS8b41NLWhLxmm7cqpRwI3w4Xb9B1ML7WmBiGkejOl7Dj0His3pGNznzD0q0yiz9pCgfEYLao2U8L5KmV2n6qb4YD2pqgfwkrFTOlpuplrOUzJX9cljjH969pjx0sFusZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
یه سری ویدیو قدیمی از قبل آشنایی یامال با اینس گارسیا دوست دختر فعلیش داره پخش میشه که توش اینس وقتی یامال با نیکی نیکول بود تو لایو گفته:
‼️
🔻
اگه یامال یه میلیونر یا یک فوتبالیست نبود، نیکی نیکول حتی دو بار به اون نگاه نمیکرد!
﻿
‼️
🔻
همچنین ازش پرسیدن: «لمینه یامال یا امباپه؟»... گفت: «بلینگهام»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/101533" target="_blank">📅 10:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101532">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">😂
😂
😂
تفریحات جدید اسپید بعد جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/101532" target="_blank">📅 10:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101531">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d084b6a5a.mp4?token=e4v4-hdaBfoBDmgAiCht7mImT2WuFJFEwgtZC_TKl68I_TvPSoYclVyOHWFYqN06RzxHDnga-A6qe01Yeh2ktW9iR92mQZ0G3iPopfmiZCkQLP7HIDaxb_Stiv4PT4Jpuy5oYqBBy3we1HgMFmzzyyvJV1RqCrjnsNrYYrICmSa78DLx6s-RsKZkWtWiS4EvdWen-Oj4wLVmb44H3TNwBOUO_VnAQAKkqP27-x8Zn8Btd0kjrnqb-gdslNUopAp3ywpDahh78RSGNjujX9PjtmRDBI3MES_BhE84cvjm_MLHGXaNVRb0AsVLvC2iBiLFTa7WVX8h1XW5I9VkvzDXXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d084b6a5a.mp4?token=e4v4-hdaBfoBDmgAiCht7mImT2WuFJFEwgtZC_TKl68I_TvPSoYclVyOHWFYqN06RzxHDnga-A6qe01Yeh2ktW9iR92mQZ0G3iPopfmiZCkQLP7HIDaxb_Stiv4PT4Jpuy5oYqBBy3we1HgMFmzzyyvJV1RqCrjnsNrYYrICmSa78DLx6s-RsKZkWtWiS4EvdWen-Oj4wLVmb44H3TNwBOUO_VnAQAKkqP27-x8Zn8Btd0kjrnqb-gdslNUopAp3ywpDahh78RSGNjujX9PjtmRDBI3MES_BhE84cvjm_MLHGXaNVRb0AsVLvC2iBiLFTa7WVX8h1XW5I9VkvzDXXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یادی‌کنیم از سوال خبرنگار صداوسیما از لیونل‌مسی که بنده‌خدا اصلا ایران رو‌ نمیشناخت :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/101531" target="_blank">📅 10:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101530">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sukY0xtcSdDJMI0rMPE9mGB9MN3DcVd_dkQi4tjZlJEbW210JXg5bBozPTiwzSYV97lFiezuVLrtcO3UQq_FlR-AgFI9-2_WN8q3sD6uHJTubz4tYrA1ln-IlKovfv9DmQqDNXIiCCvgtzapKOOcKCAo4uU1bQUh0eUAt4VdVZB67tBPABapDSdRB0ON1jcgZqKsGhH9XHTVNBzwaUS8ViC5v1Dc1KQDQmJssisGCzOwwM1Dx896X_PVUWBbwUUObP_-sb8p0r-4aHjsArQ2dQHvr_sQHPJakSkLKnj3RsOuLX4cYP4fP-ltaCtBV8gX60z-t6hICsNBb59ciEPn3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📅
🏆
شش سال پیش، در همچین روزی لیورپول برای اولین بار پس از 30 سال قهرمان لیگ برتر انگلیس شد.
🎙
یورگن کلوپ: "این دستاورد بسیار فراتر از آن چیزی است که من تصور می‌کردم باشد."
🎙
جوردن هندرسون: "من بسیار خوشحالم که این عنوان را برای استیون (جرارد) به دست آوردم."
🎙
اندی رابرتسون: "ما 13 هفته منتظر ماندیم، اما هواداران ما 30 سال صبر کردند. این مدت کوتاهی در مقایسه با زمانی است که آن‌ها تحمل کردند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/101530" target="_blank">📅 09:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101529">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLDUadm019G0v8bPTwmKxi9HD-5z_XSDKxCAIlXq-MDRA2aeSwBHM47TEqmWd3IvHBtdiMC5vEfdJFSg19XBfb4FSDLwVc1mHQel_V0hhLYswI0Og28VpFiu8uSgqrP1naXYRPX00oXh3Z3hotVzYKTCLph_uKB9_duL1Q_DfZeqAmdjLnaqTMZCjjxoUWOm__VhJPnQz6bL-PzFXNMvOJRVNpjYVMHmGpe5PiFa0mNJuuKYh70UcorIFmRhhh0YAqs4n5Sgfbe1vKMw_-iqe2vjOuzDwcpSsSUYbTof-UJWbW5uCvCViIqqpBRGqrM_FRjfGfjReVDza3-YSZ5rnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو
🚨
🚨
🚨
🇧🇪
🔻
مارک فان بومل به عنوان سرمربی تیم ملی بلژیک انتخاب شد.
𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/101529" target="_blank">📅 09:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101528">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8781c60fd.mp4?token=gBTpHTlMJdqEGs8sgtSSUACShtakjkmQac-ClUfj16zBy0Odi7YGinVkraasYBSaBCV7cizfjBtK42hc8Vn9G-0CgZh7bPNJEF0o-kVJa1uqR9s9VyPK8dDGo9fxIEW8Bzy6G5fsp-rDa_oqpea-rhZJu4daj6ig3ktCUfFcqPskQNGXHOt-g7RDe789v1wX_kXXZxbSU3m9qSocslpGsSD3YEYvBg5D__RrWJskQCCv-s3ZpYXlecdFn2pvb7-34FsDzrE0hNQCDxZ7cjTdGvLgOZt2gVYOVXCSlVPzxAzeSEDS0KaJn1U3acmXG6s_n7sss2_9llxTNyHVudfTrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8781c60fd.mp4?token=gBTpHTlMJdqEGs8sgtSSUACShtakjkmQac-ClUfj16zBy0Odi7YGinVkraasYBSaBCV7cizfjBtK42hc8Vn9G-0CgZh7bPNJEF0o-kVJa1uqR9s9VyPK8dDGo9fxIEW8Bzy6G5fsp-rDa_oqpea-rhZJu4daj6ig3ktCUfFcqPskQNGXHOt-g7RDe789v1wX_kXXZxbSU3m9qSocslpGsSD3YEYvBg5D__RrWJskQCCv-s3ZpYXlecdFn2pvb7-34FsDzrE0hNQCDxZ7cjTdGvLgOZt2gVYOVXCSlVPzxAzeSEDS0KaJn1U3acmXG6s_n7sss2_9llxTNyHVudfTrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
فینال‌باز واقعی آرژانتین در کنار لیونل‌مسی فقط یکی بود اونم دیماریا که واقعا نبودش امسال حس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/101528" target="_blank">📅 09:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101527">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d9304f085.mp4?token=siybEc3rtSTdlw39L0hC2iL_dvJlnQLwOp-C6uRC6C0M8dlpv67bYPoaOm14f-zin8HfBKBs7g0gM5YKSpTbOuFCmvAtLI-xgyeZmLS2j-dU0VJoEIn33zuMJTDtk8jezvy1LCVYZEr2Hc_g2nA6TQmcy30vsHn7QjjID18SXWHHKH86wMKHv4Ayb5U72tXtc53sy62kmmCxwWUG5cfrmeHKtPxQFoCsVFyUyi6bIga3_6OTm6XqcPWgrpsC_Skdo5SBuk4ZKdcVOGs3__6HuAll-sT3D25kRQmQZED4pSBJWfytDR7wc0qZPxxsL1EAEEvnyr5cLnEtInRP4NAsQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d9304f085.mp4?token=siybEc3rtSTdlw39L0hC2iL_dvJlnQLwOp-C6uRC6C0M8dlpv67bYPoaOm14f-zin8HfBKBs7g0gM5YKSpTbOuFCmvAtLI-xgyeZmLS2j-dU0VJoEIn33zuMJTDtk8jezvy1LCVYZEr2Hc_g2nA6TQmcy30vsHn7QjjID18SXWHHKH86wMKHv4Ayb5U72tXtc53sy62kmmCxwWUG5cfrmeHKtPxQFoCsVFyUyi6bIga3_6OTm6XqcPWgrpsC_Skdo5SBuk4ZKdcVOGs3__6HuAll-sT3D25kRQmQZED4pSBJWfytDR7wc0qZPxxsL1EAEEvnyr5cLnEtInRP4NAsQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😔
پیام استاد وحید قلیچ به دونالد ترامپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/101527" target="_blank">📅 09:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101526">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMiEgM-d7vxL0Vz5mnzRELU7AQ5lLDLtGTz27JeMjzJoUdj0og6vxg_uwtqUxLN3cbHu80RNCGuJzAdn2mdT6dZutJyoCLGETy92W5DcLTaAYOEO8xNI0URoTQ3nb7JnB97wfNZWtu9nbDG0IJ6V9gjwKcRd9wfR5MvZsz5NoqTXF6-nkDknX4bMfORWC5iMvV2pJV_PSZBOLq1sT2GWd20CNjz-WeP-Y-TFXDNeS5P773kAchg7qdPKE67beLA4_-gRlkmRbosk0o_rf-E91-qvgxOVAoC5NEvmXbMAphow4_taMMi9O7o7rmlnmD9X2yoGoMiNpC1tFCMXuPqZYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
مارک کلینمن:
🔻
جف بزوس، بنیانگذار آمازون و چهارمین فرد ثروتمند جهان، برای پیوستن به ائتلافی به رهبری آمیت بهاتیا دعوت شده است؛ این ائتلاف در حال مذاکره برای خرید بخشی از باشگاه لیورپول است.
💣
💣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/101526" target="_blank">📅 09:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101525">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab5d3c4f61.mp4?token=EZoQg13Mk29sHWEmIlF8SISgWXs14LfAdZIOYRLfzJwFXZ4VNs3-yG-aJaQqCMZNB5oQaUO90JYX7mKmjsegxJ-S8kzKiW1OYaRFhuJjwJdYwxyJiWuSje6ZfaIuzC1kqByWR_8bA4nu-NLgasHnlcuJ_DmGHWhNoZnBCYe04RmXp9gMazGuAE2RA9MChwHWPSDN2vLgLIGNjhy99Qo4IIWb3I_IelWMEt96o21atPVlymRB-ckQSmJppMRMxtSaXhzcsyHvJ6Ey_OaMBz-A3WS3N8bZHEM6De0gL10hJ-RwSIIfY4Qi8sVHM_ITYG-IZaB6lI11yfGS7QM-Kkl5qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab5d3c4f61.mp4?token=EZoQg13Mk29sHWEmIlF8SISgWXs14LfAdZIOYRLfzJwFXZ4VNs3-yG-aJaQqCMZNB5oQaUO90JYX7mKmjsegxJ-S8kzKiW1OYaRFhuJjwJdYwxyJiWuSje6ZfaIuzC1kqByWR_8bA4nu-NLgasHnlcuJ_DmGHWhNoZnBCYe04RmXp9gMazGuAE2RA9MChwHWPSDN2vLgLIGNjhy99Qo4IIWb3I_IelWMEt96o21atPVlymRB-ckQSmJppMRMxtSaXhzcsyHvJ6Ey_OaMBz-A3WS3N8bZHEM6De0gL10hJ-RwSIIfY4Qi8sVHM_ITYG-IZaB6lI11yfGS7QM-Kkl5qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
روایت امیر قلعه‌نویی از دیدار با یک آیت‌الله!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/101525" target="_blank">📅 09:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101524">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-vkBnVhWthaXyJqWTwvCxDUEhi3IxoVFeNUhfc1b2duF1HtkDeMi_dYBH_uSAiqTCD6My_HwI4zYTuDvaSBTdoVaA-3YfHwIDv1JOcKOhm49I5dd7tA8JxbU937oCTr3B5DOmaWEPx_ZYA-B0t-KY9MIpU742yPW3fksoa1GBuQSJP_FMH3Dj7rxhwXXpaC-YpuB8LfPrCURNHVRNeyv2dqgV95WMYSRPKBSYKgsHewwLad6JfH93zcgoIrfKi-oB9QxNxiISFQxBg_0Iya9xEklcfhHqxBpEIAK32gVfqcURP54aSc8uNtc1_3vkzhx_VVamxbqmS6FZGGU46MCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر شاهکاری یه کپی بی ارزش هم داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/101524" target="_blank">📅 08:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101523">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Obim39LVcCFd3Nr2BfyRK6W-Inhbbryl_67rMFSXm8EwqUD-l3a52i213tIFU-sMnlL7i67DPtryPvXrzeSoOsabe6P8yQZhZ9aUg5o-JdNSQ8DXNdKu0pxcPxH5p8bQJKCrYwZpCcWRZmLUmo3tUSRmD6-9j37JgZ1ybmLwUvaa9L0UGFQpNjeT9qa_wHcrJVjIO2P2zyWKGgAME-_VCm3nDK13aVVFj8qxmehXntj5K1ESUWavrzCOf1Ftm812BMAOqjEKKdtxPottOREXXT9qq3C_maOaQ7PQXL_Ucr9rk-F_QuyAWqoMYMAu-WIuQODkkmYoS3ZI6TzLbbDsKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
👏
دیگه قرار نیست بعد دیدنش بفهمیم که 4 سال از زندگی گذشته و اوچوای دوست داشتنی بالاخره از فوتبال خداحافظی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/101523" target="_blank">📅 08:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101522">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMZ5cfgwCf940Ov2GZHLynfGwQ-b3tLNSYFs6rvFht-58ELx9Rz2Qh_tWD6kzSXGK7nLDKA4jr-0r5BIzXiIAS7Md3U3bxaQF-GD7yWzzt01MAWdtHTtZiu0KVNZU9VwHoBbJePcnvoDOe5VYAq7Q0G5utaGBKzEFIqc8vksiklL2oOmF3r9h9VU-V3Nc6iHIq0yOrTggfYHCxPhxb0mR-XUqPhEyIw0MX-BzL1DQMSe8bRA_uc_wCo9YC2mi9N4fricZAs8ZgZ1nyvfldGp110NNBD1IXoydX-OJaOz4WKD1KrXVGRdg0Rik5HOOZ95BDfHW_qpebOC4nJ-QdELzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">-EURO 2024
-2025 Champions League
-2026 Champions League
-2026 World Cup
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/101522" target="_blank">📅 08:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101521">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
⚽️
ماريو كورتگانا:
🤩
🤩
- رئال مادرید در صورت ارائه پیشنهادی مناسب آماده فروش کاماوینگا و رائول آسنسیو است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101521" target="_blank">📅 02:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101520">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7DT16PZENmHTdTv_d1UzGWG2i89XUYflRi7OL0-E4PgJWr5GOspYfk28n_wQ2p44nxWEvhuL79-lK5v-krGaaNVYJJ3mRHXu5lUZoxW298zl5PN4Yx7ejBu5WLiyzfCFAqlRe-mXpnZYtDy5j3h3gDu6hwISYkQn2Z6McebBJv5AX5VZjeCjmYn2MVjqNGXJqOSMczrvGsKPWxWaY3TA_AyLxmYuXyjE-MYtE_HBAuF9yd_K6Cx3V4_iEe21U02Fw8DBdr0XKvbftQ766MnXN3t0pa8P3jzmahlOK40-oTUo4E2HHDdPyMvPnvLUgOGB9gB7T0FBP_g48-jBe_WCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇳
دونالد ترامپ در یک جمع خصوصی به اینفانتینو پیشنهاد داده که در صورت عدم انتخاب مجدد به عنوان رئیس فیفا، نامزد پست دبیرکلی سازمان‌ملل شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/101520" target="_blank">📅 01:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101519">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHDUiLAOA-e_-mL7f3snV7KiTLIyFw7b9LODteljFLFvTwlspx_acYQT1Ba1dQUYsFUXjP8w4DR8_w405hU4bfAsv82fbGYAffbsNzVpeTc6jRjrq_xoGGfPdweLA3qEseA1Okmp8_-stNTNLo5OIi4OnWEvjUS-6h6cZlMXMosLSEVE5mtzInWHy411IXOSHl21ZLmPA3b9nynvl6GKmkGikTs0SoungEiBMlZnRPEirZVot6fhEPQ3CUN9pi7glS9hA0BOdLW5lVPON7lqkCNJOU0RCTXsE4nnQnjBldMPSY59lHZ1Sx3nKBi8lCitW49YZ3YJSI6aa6g_Ugpygw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیشترین جذب فالور از جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101519" target="_blank">📅 01:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101518">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mocsea6HIQuGEVQQgOCWw-Pog949eR6dGc3WiAr1HbVuxcnQ5iErGqOCpWP_2pa0tWl2YeEauKkTvQqyr4mAUSb9fDXY0vuk_OebXfpG_lGpCCap_MIsjJgpzb_7duc6EVYjIMxZzoKKBZzRwkDLMZPQOKbMLdzNCZ8Zb1BBIkwuIFA0melR6wbxqlAF7gTnDnC54Y5vGTvevf2AuCKWWtXH32vT47kHnQrnJ-ZKARrjDIOdtWhZsIcZcyrp4krPuwiG1VJVY41Ifb63jFuVRhUEJWh4GsLZsMj5iw61ks_JxInco4rsJVR_macVcJ1zf_oTle8UQbY-bJ-WY467Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فورییییییی از متئو مورتو:
– فلورنتینو پِرز اکنون بیشتر از قبل، تمایل به تکمیل انتقال رودری دارد. توافق بر سر شرایط شخصی، به زودی حاصل خواهد شد.
💣
💣
💣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101518" target="_blank">📅 01:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101517">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
💥
ارائه مهیج‌ ترین اسلات‌ های جهان
💲
شروعی هیجان‌انگیز با 100% هدیه خوش‌ آمدگویی ورزشی و کازینو تا سقف 100 میلیون ریال
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/101517" target="_blank">📅 01:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101516">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWIK2oQe5MF1shfjF1DWHxa9bC_rHMSEjMgpXbzm5JoXMSHDU-SmqxzfF_H44Lr9CJ3ltXm3FzEohQAseXQvGBFv3NUYkl5tt02hOy8gvhas6kKaYFRPqsElKV_b8jRzLLFJs9TZu2ox56nimCekAM-J4HvTMr42TRlleZCsAJEmrOdg_5y2FCt0utJ9Tw0aHrgv6p0cX6ZCFT6zvxaVoDxqbaBsd1GDGiEN3ljLDTixK1MX04xXuXsc1OfmAePFDkdcPIg0Ithnil6Vq8yrJKU0ghdpO6cZH28oPcjCvviyRMvOEC1FTI8FBu0XYuVwHvWLnyTJLlwiNaOd9TvPZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🍾
شب‌های بی‌پایان در یک بت!
🎁
35%
بانس جبران باخت ورزشی و کازینو، شبی پر از هیجان و فرصت‌های جدید
⏰
مختص واریزی‌های ساعت 00 تا 8
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101516" target="_blank">📅 01:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101515">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVG0NPNbAmhsFr89vLqGfJVEWm95oI6McvtCUiAclUS5LEUT63LqothvarmlfRC_5b1pqRU3k6avb7HBtp0K9dHciPqbRUO0CpCMZzk_fEFUuw0UXbD37LCYjapbkZ0qFwoIfK7b0lq7wYaJW7OdaaxltCC-8dJMuVd2C8JQoP7vRhPws5U8-BN49uDCWhYejzJmUmzudVPf-hmSag6GggIbYXyLUOBYofaReqLW0DhKzz4I6gt9a8w9wfrnlNB-WBfXahgKgN4nicb2z2KvOuF0DuqfLlURnpOECU4fpe8Zo19wStX8cndbqVBLhWdoP5OO_Q7VwAqtz9SlQiIPaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
جدیدترین مصاحبه رودری و باز هم خایمالیش برای رئال مادرید:
🔹
رئال مادرید بزرگ‌ترین باشگاه دنیاست و واقعاً دلم می‌خواد برای این تیم بازی کنم. من و خانواده‌ام دوست داریم به اسپانیا برگردیم. اگر لازم باشه بدون لحظه‌ای تردید قراردادم رو با رئال امضا می‌کنم.
🔹
مدیر برنامه‌هام با رئال مادرید در ارتباطه اما بهش گفتم تا وقتی مسابقات تموم نشده، حواسم رو پرت نکنه. حالا می‌رم تعطیلات رو کنار خانواده‌ام بگذرونم و امیدوارم مدیر برنامه‌هام به‌زودی با یه خبر خوب باهام تماس بگیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101515" target="_blank">📅 01:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101514">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e61b7dff82.mp4?token=G2SIIBvWjluGXPfmnXYr-WtcB63ae15pxjxUbzhYSO5AB-LjHp76_uooREyRBhsa-Rdh9xEQ1nvIOBgMA4TJ1ESE775u8Qhw8BSZ9mKtyWj4o9g6_SbjZq5zKvUsBSZejkkmDfRAagPBW9nfni-MoF97nuNMyG1zqTFzHv6tFFMPZslj-9xJM5StJTQa1B-j-nvvym7C959CEbG7y3mpKlgzk-_4XioEWGorC_W9rOyfYjkg4QUFXhG5C2LLNCxywj1x0FTH0nb8AZUtYiMinY4y9RMshKJ-lkksIvbpA1zuiWGwe0gqHVMwP0QCi0JLW0YUA0PrugpO3nV04cfXyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e61b7dff82.mp4?token=G2SIIBvWjluGXPfmnXYr-WtcB63ae15pxjxUbzhYSO5AB-LjHp76_uooREyRBhsa-Rdh9xEQ1nvIOBgMA4TJ1ESE775u8Qhw8BSZ9mKtyWj4o9g6_SbjZq5zKvUsBSZejkkmDfRAagPBW9nfni-MoF97nuNMyG1zqTFzHv6tFFMPZslj-9xJM5StJTQa1B-j-nvvym7C959CEbG7y3mpKlgzk-_4XioEWGorC_W9rOyfYjkg4QUFXhG5C2LLNCxywj1x0FTH0nb8AZUtYiMinY4y9RMshKJ-lkksIvbpA1zuiWGwe0gqHVMwP0QCi0JLW0YUA0PrugpO3nV04cfXyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گاوی و فابیان رویز که اهل شهر لوس پالاسیوس استان سویا هستن بعد از قهرمانی با تیم ملی اسپانیا در جام جهانی، وقتی به شهر محل تولدشون رفتن، بردنشون روی ترازو و اندازه وزن بدنشون بهشون گوجه دادن
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101514" target="_blank">📅 01:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101513">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikNBhMv4ZmWLPfngNjcJ2FrGSxI15EEppBk0k8Gy3Jtdqlay49wt50KvejwZXIkr_4u22XAJ5xly1diMPvdWoB2FpAE-9dcv7MV100Wnw7PjSq0-l9TRPWLwVvVbAibpIeLGqrQ1Hu9poKvEOiNE9OM4osbZ2xlN4iehDwHweuYNrncSv-aY6zkrXbOHMaBs6iOhf_YB7stfCQYe-04nRj5hYGlbsNAeZeifBWkGavf7WhzloE2xAoM8sgbns4t7Yj2ewfzHfNGtITzq-v2rYqRlk6fJ2SB1ucwA_Y-gHapCYKgkD0D5TgXH49i3yadK3kFBpSUbvZMNlFdrS8PYug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
۵۰ بازیکن برتر جام‌جهانی از نگاه the Athletic
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101513" target="_blank">📅 01:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101512">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ArHT6wSn1aJC07fih6HvNjuEYezDdQFyRmUSFDry_GHi6xykDCywQXNGC-u0ZD52w8u0T5IUQdm-LTAtVr22c9OjnTHdWcuEYECKmr92K3a5l1xjT5EjTP4G59hknF1kFYiQxzqgnZJTQYsq9AjcUqga--O2PJXBFjXa5TlxvzypfS7TD7TPSIMPKwrQgp0ZbOHGEy-b_1yh6zAjvF4a7uxpUX0iZzwcRem8I_S-XOVFCaAPiupEu9He37DI46LcKEXfjNBy-nK4ZSHIAxhsNtyX1TcBw_IYQiMCT1JkLp7pfvMjQz_zo6cWKOkby-oXOLlphD1h2IfsmDDxkPvVCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
از رامون‌آلوارز: دیدگاه رئال‌مادرید نسبت به جذب رودری عوض شده و احتمال عقد قرارداد با ستاره تیم‌ملی اسپانیا افزایش یافته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101512" target="_blank">📅 00:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101511">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
قرارگاه مرکزی خاتم‌الانبیا: تهدید حملات آمریکا به مراکز هسته‌ای ایران جدی است و اگر چنین اتفاقی رخ بدهد تمامی کشورهای منطقه آماج موشک‌های سهمگین قرار خواهند گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101511" target="_blank">📅 00:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101509">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JJZ7CreKb5xjU4HmpwMGRhuVtLtECGMTgiFDM5kRkew5ZiBl-AowIVijV8fQ3ULCgeNZFO9yKhYrSXto73WbIpTh_HFNFA7FoHP2xrWXx0xPXsGoXM17S7RXvFlXoHQjDPotWBajdZAej2-hmfzvG0_aS_uVSZPilKxgP92kdwnobOu9Y6IdUlwHPPc7orODIGJPxUeq4bR85iqzBCVrnWuECEOF_uo2c0LMSZkQPc1HHIMaXMFSPGLOjmnRmlp_hwf0MXa8B2U-5kKgiTgqr2GU93cT9ugjRLkp4tLP6D3UVhCCWDX8B2MOm5o7OglLbsNxjBTowLp82bqsI8-JqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kvryqQ3tAq-ex7rKZhRlKtGruYRbcagknVC4RDjUZx8N3r5BUDNTVzhDVeH__2FU7mYNmymPL7hyhokp-_Pg3PJCBRJv0nOWLZtec7j8cJw7vHMWAuZ0-Jti7fchRPmrWwOBqTMpOXmO1gVkOAcK4_MzLo_EYnxS-hnsbgMmTShNrmZ8GU-PV39RNsGyl_IIyuNGZs_A5zM_LblIT-D_XKIxOmyOW8tAIE-gvl9m5Sh_JzKnMH2oyprMwDSo8jZgiICROebRDCLZvyQEmU-zhXZ5QE_zWNDU_mT6JwsrM2w7-a5F5hqiEDiUWY1yjJjGpOQVEKQxAnjjMLN8tIBI1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
رسمی؛ مورگان راجرز با مبلغ 137 میلیون یورو (117 میلیون پوند) به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/101509" target="_blank">📅 00:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101508">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/deGmcBaWZKlpeVBQ5PKBedUZtXX2_IPpWqMwmgo0TbD5gcZpx0iK-B9vqfkTquJHWSwkFx1Zvbl2VRKMf1t2upinlRMOpxW6eqIqCZqmWLSeHeHshonA7vDvHcKkN_WLB7fG5pGkEUUSNjogigULtVh7BM0u2vivooa0Pb57bPc0LgFaWKS1ON3IND_uHJvkewpuJZWPnxYCg7dH3YoE9vG7uD6rvG3GRsyrfn6y5grWEnWtnOgXV7zjsK128Aw3gErZyHwBpjYodd2Oq0ckb0s7DsTMoSGJjObVOxnbT_DjSfHBL8KixXETGOzyrf1_DgXO1SLGVWaK-_Y-bqIfog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسمی؛ مورگان راجرز با مبلغ 137 میلیون یورو (117 میلیون پوند) به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101508" target="_blank">📅 00:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101507">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iwg9p8p-xbplg0YBtpdCDrRcYEOgJ0qGFTNvZHG1GXefnsYBCTrf2FknG5EHwSJgDcR7hgePyvgSrkPg0RjzOkKs9SvrhzXSXiOwzr7duY4uoQaUO9OW9zTpVZHrmIEUA1LJKgjX2D1hqTi8J9Fu251yOT_cNvZ2EsZYFweipayILYVD-n7twVLATx26A4_IH8cw1Fix-HqBn4YRfIiCYXBmHZDTTay_fqTmgaYYaQOgYpmrRDDLPgVMMZD5NkHc3QvdQ16gfGBkgy1Hc8iGNIqu69SkkCwi_bSpRhSCqwjaEMe6vGS7TscPGzPv3Gu3hFlp8bqhmJIZ4Ic0ecBcjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سگی که شباهت عجیبی به مارک کوکوریا داره و حسابی وایرال شده
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101507" target="_blank">📅 00:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101506">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGxfwgWXyRjxhUbj2FVSveo_2XbEeFN_TcA-HnHL2_DiPUg1TwwcbJNwQCeBePPVXmedZBH6tkyiFTy-pfDdgdUrZuE0tzM6JdXGf7Do9I9iVUr6RA5oO4TrORrdAwM9e0DCZlNtMNlJ8ZQ5oTbYhp3uCqtgKGXjrckM5m_xx0YS53pUJJqO4KisQELCHhYMrUl4KFIbIkzRljlVLn4pK_e_F8utG9_-K6ZrVcXBGjHUd4mgN6w7t0nQwYJHhc7ggZrF_Uk0SxhoqP6pCcny3jHZ7O-bALhpjNy0-polKIyGMWaEgunor48EsSpGJ8LYBPehoEAbP8q8apFsk_Dtkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسمی؛ مورگان راجرز با مبلغ 137 میلیون یورو (117 میلیون پوند) به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101506" target="_blank">📅 00:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101505">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">راجب پنجره
🔵
🚨
⚽️
امشب باز هم از علی تاجرنیا پرسیدم و ایشون خیلی با اطمینان جواب دادند که پنجره باز میشه و بر این حساب هم دارن بازیکنان خارجی رو مازاد می‌کنند و مذاکرات و میبرن جلو، بنابراین امشب دوباره تاجرنیا اعلام کرد که بهتون بگیم پنجره استقلال قطعا باز…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101505" target="_blank">📅 00:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101504">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWaigHTl-TAP6glF781TMC_J9jBQQi2juJo0mHyqjyLJq7XtXNig1hNWf9bK-YpqpbajzbQ8RBMsmExw8G04UvvDruoHM2dj9QrpfqvzhvjlW7tTvUjHGr64PkHqI0iSGa6hZ_ZhfztuOSy53CJBmQSvv7uH6mI9w8ZHe-ta-1xgakXdoCANSYGFGqoq8UeXe9gvSmmRtftAgyHr-vWs04qLsBR4mZe7_Yuo09WLu-47-DT-UYIvyXE6hU9FT_GgbaUJd__Ufp1_hdhRVhO8tbqzx8DSPf-6IIvorKVh3W9snrEZ44RVQ6Hdlotyb2_iR3DI7qgDg3vkRx4IqWjyzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
زلاتان:
پارادس خیلی خوش شانسه که من تو زمین نبودم! وگرنه یه جوری با سر میزدم تو سرش که کارت قرمز بگیرم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101504" target="_blank">📅 23:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101503">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlzMQ3G7p50a7KUiAczKXpEX8ckQ4M9hUyL1T3RBdIFV3G_UTL0t827UM8t1YSdabamUIpJkP9qVsd38nSq2MREReoPBkMn76GUL7lef6N1PIr9o0_sPKkMY26h25AEFgDdmvr0v8TGAYLanzIqh41K4P1wQ5-RGOv31ExgerX2E7cs0UjE1l_oZrO-BLNXPwCjjRbqXLkoF7l2ZscEGJMJWrCXbl4CnkWoI94gGhQF-b0YkAUgPo6dpQ06kLCuezahvUexHpuC_E-eSUBGtWjf08kJMaWoa7Wf13h7VBjpdPwsFwZffXKnscMT86Sry2LYsEA73N206hMEaVV7gAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا بازیکنان آرژانتینی که پس از پایان مسابقه رفتارهای خشونت‌آمیزی داشتند، باید مجازات شوند؟
🎙
گاوی:
به نظر من نباید آن‌ها را محروم کنند. میدانم که این رفتار تصویری مناسب برای کودکان ارائه نمی‌دهد، اما این بخشی از ذات فوتبال است، و گاهی اوقات خشونت نیز در آن وجود دارد. در نهایت، همه این‌ها بخشی از فوتبال است و باید همیشه به همین منوال باقی بماند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101503" target="_blank">📅 23:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101502">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cd187695c.mp4?token=PcvTAKjsKWMz_Dxc6mv0btm2FI75JnUJr4FRj07g5xrwA5i2OqWZ8-tLaucqCnfCXFFptIAZvi1DTex3s7AGBSEOpxiOW_c2tz23r3vI4cIOy6olz5qbkQYo2FGY4RQWHISTfU3aRRACQu-THgXAABv-aGpiJ9Ue48jz2Zo6bhjwVjT164bgK340MrwROJ1FamPBEXDqKEl1bKirwt318pDrbDBnbnpEDp86y2JdZ8iVqZk5UrqLcIbwnu_HVXT9uoDnKRYQdw8OUpAmfkul8q9JqHNMu2BQCUOgm1Q9EMdf0IP16RqH2alAyKE6V6YwOwB7J4pDviLZAXYawVDD3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cd187695c.mp4?token=PcvTAKjsKWMz_Dxc6mv0btm2FI75JnUJr4FRj07g5xrwA5i2OqWZ8-tLaucqCnfCXFFptIAZvi1DTex3s7AGBSEOpxiOW_c2tz23r3vI4cIOy6olz5qbkQYo2FGY4RQWHISTfU3aRRACQu-THgXAABv-aGpiJ9Ue48jz2Zo6bhjwVjT164bgK340MrwROJ1FamPBEXDqKEl1bKirwt318pDrbDBnbnpEDp86y2JdZ8iVqZk5UrqLcIbwnu_HVXT9uoDnKRYQdw8OUpAmfkul8q9JqHNMu2BQCUOgm1Q9EMdf0IP16RqH2alAyKE6V6YwOwB7J4pDviLZAXYawVDD3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کلیپی که از مقایسه اونای سیمون و مارتینز بعد گرفتن دستکش طلایی وایرال شده.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101502" target="_blank">📅 23:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101501">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UESc0sWOoucjG3RTHgF8PuqYPrQq_GvpaxUXdUfjWnRz-c8K-RpRLWrriEXmwsvh7qUf_PKjDPWl28kMm6M93Z9cAO9A5UFJ2j90G6mqR6y9o_1vQP4SK9a62ml_hSI28F2JaSulDWgliB8Y2ESD3LGeNOGVzZwDrscwHieZyG37DudIfN67nmJywokdNYulnIfI4QNzxbcenUHkgWRFQWho9OokHnenbYB4Fz-NsJ-qhlq9lrxqVAnXehO_-gabCMLeHtN0GM__tmWO8i5FgAPol59X3f9u4TiB2Lt_gfJF5jbDzaQ_dBHzxPf7rairzNxM9JMStbstrufVb-ynOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
توییت جدید امباپه: من برگشتم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/101501" target="_blank">📅 22:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101500">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9116787106.mp4?token=Q2rlpCFWr4YC61Jg2uVpMwQsO5IpQPKPNMijQZr-F_C_yRrfGNxCZAa2AVh9sVBgaMBDw8Y_DQ4H_POqQANVHZow_N_UPFRCqXbTGunWpU31p45N1lzYYyfYqJMcqCSj_D1aYYKAdJhxa55fwJ-rQ6tpxJ_uwZ4HbxYdhjNHPmFxFSPUZ2Iuxk9kouWo4wltkMBzn7NA2cuhqiOu-3Ai98LKjZx6G9jbvbMzz9Rqrik6Kr_gmuODzDRFsBfgMvv6xIssh80-cT1GHkpzWUFSIVHyRYDBWX7e4tpFkPF_BH8mVWXv7qcbh9hpmOWmaimG4Lhu3nsW8SJPFcmRQBHXrIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9116787106.mp4?token=Q2rlpCFWr4YC61Jg2uVpMwQsO5IpQPKPNMijQZr-F_C_yRrfGNxCZAa2AVh9sVBgaMBDw8Y_DQ4H_POqQANVHZow_N_UPFRCqXbTGunWpU31p45N1lzYYyfYqJMcqCSj_D1aYYKAdJhxa55fwJ-rQ6tpxJ_uwZ4HbxYdhjNHPmFxFSPUZ2Iuxk9kouWo4wltkMBzn7NA2cuhqiOu-3Ai98LKjZx6G9jbvbMzz9Rqrik6Kr_gmuODzDRFsBfgMvv6xIssh80-cT1GHkpzWUFSIVHyRYDBWX7e4tpFkPF_BH8mVWXv7qcbh9hpmOWmaimG4Lhu3nsW8SJPFcmRQBHXrIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👀
خداداد عزیزی اومد یه خاطره از اولین سینما رفتنش بگه دیگه جواد خیابانی ولش نکرد و دونه به دونه اسم فیلمارو میگه و اشک عزیزی رو در میاره؛ خداداد عزیزی میگه من ۴۰ شبه از دستت چی میکشم آقا جواد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101500" target="_blank">📅 22:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101499">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mw0zAlFCdoO7r2kIOV0ZGmaYQJBegUzwO1NiefLw_krEJCM2RlIWThfav95ySESWkUPSGIWMXqo2cRxX6bIIsg1xfc3bsWXsOE0-i-z875saU-FQZ3-unqferOwK21L1hQOlCZ2IPBicnkq50NQsxif5LHWZvRqMVr-7816yoxSWsedG1eowF6RVIBk3dB6hl99dDqz15WvoTT9nQKoCJwvxFmwqGYz-KB8f_zwsoeBt-LL3Zv2-HP9zihn7Z7Mb2sNsYoECBIzTez1p7OfZCZkEDwTEcf06k_UJIUFPx15xGLuiWuGG8X0a-SEpOm-SbtiwIxBh9yOkMGexlU2KhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🥂
استوری جدید راموس در کنار لیونل مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/101499" target="_blank">📅 22:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101498">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a3469819.mp4?token=jWfyTwPxcQB77byx_WKvB1a28gNFr-0c3zk71nJg7WUPecgDERWfJbJ62qivOCot_eK2D-XlnDk8z1feKCuWW36VoiJ_n-WOhKSr1FFt2Pozt5xmB7pC8nDBAH17tLMX5JQPLNCzPfdSEgB6yTC2WhR2113NDfpgBLzgvKL1NUULEstXJ8kzej2gZGSn5qwXTF3Gc9aH7ul4xFDFK6nUmlgOe55Rzgap1t-PWs5da7hjpbDAz3pNIXE4nxPOaZVkdFc9rPYUCWSioue7Y0v9ZDmaHuV8UXUUtZZXJRof6kU0eNEzDudYvzOX2DdStWCkcKn8b-fqBGEZDTIuj3exfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a3469819.mp4?token=jWfyTwPxcQB77byx_WKvB1a28gNFr-0c3zk71nJg7WUPecgDERWfJbJ62qivOCot_eK2D-XlnDk8z1feKCuWW36VoiJ_n-WOhKSr1FFt2Pozt5xmB7pC8nDBAH17tLMX5JQPLNCzPfdSEgB6yTC2WhR2113NDfpgBLzgvKL1NUULEstXJ8kzej2gZGSn5qwXTF3Gc9aH7ul4xFDFK6nUmlgOe55Rzgap1t-PWs5da7hjpbDAz3pNIXE4nxPOaZVkdFc9rPYUCWSioue7Y0v9ZDmaHuV8UXUUtZZXJRof6kU0eNEzDudYvzOX2DdStWCkcKn8b-fqBGEZDTIuj3exfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا حتی سطلای زبالشونم شادترین سطلای دنیا هستن
😞
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101498" target="_blank">📅 22:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101497">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9vULwbpum6--bCZMnFncbEK2SR_lVEFDpl9N-x1CxNjwX70fXJfuhV2-sEez4s-oQcT6GnZNRRMu5TP1Vm8nw9Dklm4gaf6xXIvexzvk8AyfIPSa9INCDxPscTIIXzJSLo8vRpL_LMgdDuUw4KK9Tm4YcdUn3XUpDNwVmjWUq6CvdIcMsRqTicI4XpsaiSGr0sx_47FXPiv64iTgp2bG3tlooAOy902SMtipt7mjIaDfvE9cXG9wnCf0UpShdOp9eex89MBOZ8grva113tdWqtQqOnVLJM3ykEslathUvEqx5wODoHKfgs6mfGXqzMdq1H3Hz5V2YmZ8H5MIQSq1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاویه فکو که داری داداشششششش؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101497" target="_blank">📅 22:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101492">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TjNi-w9ChDzAkzeSp2bCKMFq51nAJp3pOYTIb0AZTBZvKaZSkRV4BptyfFuBy4Xjx2yOg128o6RVV4zvt498QvhRrLWyod8izubzTaMVC3c_LdRJo7nZQ0rllOLWlT8JaZr_aRIWbZWraG225qh0W0UhpbBqbbu63nLCrxGuOdvIF6W8dFqryO8iLbB0ovHXhb3_-A7EvkKcEj_TGnsCdQCmyeGQP9j2EnQllREkhA4jh7OSh0IPj94BOWJSFmtqrSOn6FCpvPOmSQlhu-Au9qEv547qoPYqtXFWTHCyOmNrIL8XwX03xexKzXBKqefjfVMTZ54dG-PueNSRIjGCsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A6YL2dl44I2-EZRNG5tky88C_p53mHQWEvMMNY_8KokgAENgDrjK0XqEVrONnN2lTecl7VqJ1po98NpXI0g-pBhi7Y3DLDhVpzIgZdPL5fjrp_XSVYcM-7FU2suB1Dk9GUIGQqZawcWpucfEtTInw7XIKUj6IveesgpT5gU6JW4btT9Hhlr20OiYagiY7e6ilJXLdlUtEj0r8kQSBIClAWpCkwAoW7tiuPimzrxxtw6z5agsVQ0rXT8E69DLc8U5ziRYTYsy34FK2pCmwA9qAjkaVNmwIvVhHSrEg_FiKH5z5aOFdYloCeHJoOYEC_4XjdTThuX1CmbDyBdmz1yFuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tv87mLWGMjgbLzlzYqRVfsWHPu5FnyHteCt21AhCeSk9oLzdMM6oklYeO6wP4I4g6hsLSbQ2HcetIBoQmbzjdMzjXaQMSYZ-OfClBsE5p4VJjV7jDkGXSzJOXufx79VBH23af9H_7sp3GMv2n-YrodHLH3eDeFZlEWpMRgkXxet7-Oa01v-5b27aggcAqIEj3YtXnvyJJ5kT_Y42Qezv7goTZLIdxEpT4ujLS_xb4EzkgMW-7_7IJw5kzyaLKBMR1PL-nt3Z8X6PLnr73qVHEQjYrlM8702TyJwyaaGAx3rO6Kblh27rQK305GoaKrYQPQF1x-s1s15cn7hnenc1Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hNqdIF-a73ApxvGCR3fFoPymwxF6MBtHOs2lZe_8GuDS7vDL_hWFaMmu8oXM5c-oCX_SGmw0dZQDgvKNukJ0Uutikb3aQ9MsSk3YpGC0vHGKJdw5Ga04YAkftbIrdS6-vSavKnpwgAsc65rlfi5kspb8zwkRGXBq3nPL-27_PtGRVJ4BuPW57PqD6fOYyk5YJVXc2_cghLTHcA3hYvLM4pEMycsyV-nc-9XycQWbiN-L9hJqf2TczJF8Xh2vX2_iRQUj5-EB8tjDWesXlbGACpHYGCmp0V8pYoXq9DNVbPa5YwYj30EtL-XSGFurRp8Oj6tFmPa4x9NotFOs4eg2YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BxVIbglWA_94c7VZnR2gOBjvXyKoAN01kiIYPi2AY6_oeeN91y0qnnN2HEmwABIe9n8lVihC3IjPr61QgCrPnzRbkk6xmgfPWsj0N5z-TvDXuvcN1CDzg-0V6pMCqnw7IlGODcfQp7as1QiZh7UsbAG1vMm6f--p_s50JC_0eHBNGwdMb-6CuCukGk0YvP8e2b0Nq-2o0X42liMfUvCZcT2MAbegIpaWRE8VcPWT5uyGGIqgs8n2TCBYqDVy7nBOnFO3_OB1NRdjTuNZHnfy2NUyRjGRqB4CmxuODavW-LEF9BTW3oe_pcHaOyHaRzUnee45G-wYToTkVp7NhHD9KQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
💥
تعطیلات تابستونی وینیسیوس و زیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/101492" target="_blank">📅 22:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101491">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf2aa4c289.mp4?token=Qp654oYj3ndq6GKgshkrgeSs5x8nq3Y0_qkKTRkPDkLWZovOEKBjEOu9C4DxXINGgv0LhpdMDtEq3H1gUMM7fc7bfe6j2Eeo679ryidZkebLA6lcb6I3R3T_BWneyXKk0-IZCObhDJClsNMUayv3-WRIywPDzKEEoZwsDIYeOsPOKWE66B9FLIYGD_gv96dlRreZQB38xfHDkBC40QBa-s_peh2qQTNNKblxshu5dYdIuX249kko1wLUEl8r-xUgxlqQxRrnGnJtZDfWujmZqpOzvdGh_Ok0dU8yX5WXvOsAcXSFs8a22WmJuMWDD-FtqupwOgaXlZ9C9HTrM9ytkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf2aa4c289.mp4?token=Qp654oYj3ndq6GKgshkrgeSs5x8nq3Y0_qkKTRkPDkLWZovOEKBjEOu9C4DxXINGgv0LhpdMDtEq3H1gUMM7fc7bfe6j2Eeo679ryidZkebLA6lcb6I3R3T_BWneyXKk0-IZCObhDJClsNMUayv3-WRIywPDzKEEoZwsDIYeOsPOKWE66B9FLIYGD_gv96dlRreZQB38xfHDkBC40QBa-s_peh2qQTNNKblxshu5dYdIuX249kko1wLUEl8r-xUgxlqQxRrnGnJtZDfWujmZqpOzvdGh_Ok0dU8yX5WXvOsAcXSFs8a22WmJuMWDD-FtqupwOgaXlZ9C9HTrM9ytkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"اصالت یعنی به ثروت برسی، اما حاضر باشی هزینه کنی برای کسانی که سال‌ها از آرزوهاشون گذشتن تا تو به آرزوهات برسی.
بعضی‌ها با ثروتشون دنبال دیده شدن هستن ولی بعضی‌ها دنبال جبران سال‌هایی هستن که پدر و مادرشون بی‌صدا از خودشون گذشتن.
شاید ارزش واقعی ثروت، به چیزهایی نباشه که برای خودت می‌خری؛ به لبخندی باشه که به روی لب ها میشونی و حمایت ودلگرمی ای که به دیگران میبخشی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101491" target="_blank">📅 21:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101490">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-XjWybwIogACcQIcVu_NO8uERLOxOKftj5tmwWZvqMewmzt6ixLHMIXBcdlcVNmxO53OUBsLocu6ika6FJFGmHwO6O2dTCGkDRORxEg8Ysr_stR9Wc_lAo-lpXuXRJrtYjB2WXDIUBGUjlaWYQo7ruNS1HCoRch-LT04TpvqPmusYIZBPjaWjHaxeC56zJKrRDSW8aVU8DjVIojDQhICvfvHBG5h72hVzfnLSha2ds7TVLawgclz_ejWBLMadHUSicnDdkG2lZNn2cylKAOlgZ6vLsOYxGH_gHzPkl239HvKk0D0vXqZ6M31HH9eVvpNdJO_MGxJZERQoAZgti7cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
تیم منتخب بدترین بازیکنان جام جهانی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101490" target="_blank">📅 21:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101489">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QggnkzSzxrRH3_2u2l_vn5enHr8K_UwP_BTOH1Hi-5yct6TVlBBi7nSg0q5oR-k_ym0t_McmyHYSvk5HwNuL6gabZMYlH5JmsnpBZRXjyeDKOHZiNXlf0Y1VsOuozv1Y2Nb06ThfxMalccgApTocZBgl3MKjHYad30fXBiVYwoODCEalvDSFKe533jI8VnJTS0ocsG1j-T_lNzUda5Cd3ciSScWI4aaPovZczvZHejJ2Yg-LtVIF2hPAsqJGk1Pe2AsC32gwLKNXOXY5fjjoidlpOWvs4TEi3D0XKMRZwvHtcdJhqi3UfJGL_Yv6i_mZEFbm3I3NBz4M-hH1xk02GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید وینی با چونه جدیدش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101489" target="_blank">📅 21:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101487">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKKDO0JPFBYSi3ybeAC1KwA3DubMNwUB0-7dL6URLNLzLByL_ydx2XaGxlW-IUdD4LHcHdgIS53F2r8IR1XD4wKSVGMDylnWaHgo3E8VEN4Dta3oqpRyoGMLskN3MZZion5OJqUHihuf-WU6E7vOLVyqtTkQyG2khg9XeY5AmhxqlvSVFJmBJ6ZpjCFLBh5DJqAjlPPY080jpAGO-k5pckz-LD_o_fEQnOAwJy60MrqxyjS0RbXkwVO2jDe6oxqypLaFCYAiL4NJYNdyTOYeF4Ib62wQpw_5zeIMsMkBYPydr5GJU-HeOJhPkXP4I0mdzzSDhaqYSvg5NxngqXU7kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان فصل 2025/26 در میان باشگاه‌ها و تیم‌های ملی در پنج لیگ برتر.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101487" target="_blank">📅 21:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101486">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7KYUmN6a2UjLrvrHlHXYKJD4Yh8gqxp4xsRIvJmimnax72bPMYv20geyQUHZyb1Lcl_2qrX98H68lRGVj_ccMQ2PQ6LtQI7EnADF_I-hpOCBAdQcGlTqGKC_MeB5B6iyXQ64vmXGQpv_QhuUOJJdX9uHE_0vs1nm6VGz5Blz3RXxOg38PyJUEzxEK0ADbAoWtu67S6U_yiamIXPkpDk1GoQQjvT24sYvydeAwjVUiymuxRs_69Y09fz71tZyE8ux50fCRr4se8ysGU42Qsx8slHyRg3uSiK4ZxXxE2iobFrFj7lBJQxC97GaHvWwNlTfHovkSqKU6CrwJ-e7BMhvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رادیو کاتالونیا:
🔵
🔺
🔻
لاپورت جدیدترین بازیکنی است که خود را به بارسلونا پیشنهاد داده است. عوامل مربوط به بازیکن با لاپورتا در دالاس ملاقات کردند و ایده حضور در بارسلونا را مطرح کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101486" target="_blank">📅 21:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101484">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/myRC93cZ0wVGCjkx9vt_ywr9dlWzzqpn9h2jSyBmVHC5CoIyczrPzRoAk-ww_4hhvi_cuyJveTAKFIutsgizFw0lFo1wsmvT5SdM17371-b2_gRGSnyn2HKMxdjJWYhu5GigubNdicoi9yXaG8oxEoS9xSFX-GoQtpUwF-L1HtdNq6RdyqxG6w0zUmJ4WwlBvJiRZqI_Bq6dc7jlKU6H6wfGEFp5kUyZ6PMEBNSsAhIwJq5erWLsuD8oSkNyWV4rkrVNbf-46qgsQ4xMKOqxNhXGP9xEmCeZG0uhn_v5aYcgD4_qGbgANVdnr4ADGa3f2rbAsoGq2nJ8TwRnje0xCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/atgOtw96Nqk_RY6APzKI1dvrD5IGe1cty-9WN3zzbqOacxItjglSlyQlXNsosKpsQLTU8yBd-zoe2oi6lV_1blJ95ot6_8L7aUWlgZ0huRw9M-BePZ1AZPBktZICxQqStWpno_MzBgK6T4jic8rgs1okNeT0sp8V-DrfNNOgF_cGDVvDTA8Ptjh87xzasgtDk5XMnBsdpi12xsFiR77Lcngfffw7js7j_kwv0C-7ePxaE_neLymX-cgb5xPei7J2WB_NwXosdJifGfPi-lRkzXNGSq87uRnAGqwdCqj7NKom-SZXySavIwMp5zVW4_N8f-CsUL1jCFZOvE_Y8Sl4Cg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😁
زیر بغل شکیرا از آینده‌مون تو ایران روشن‌تره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101484" target="_blank">📅 20:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101483">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6kmReHQnjD50W4ggmKrc6LMkVF7Tr28Wzlk7yS7Sgbpf5GEVcmP2_dBN0Ii0YWSrsuFOTFfUgiDIvpNfHMTcqoUEo5qUd3AksADnmkCKr5uPE2ra7qsnyIL0r9Z8ElXU7IqwdeUs6PlNadVzRkPPFzJVbtZPYxTWJxO5ao5URBGB3Ljf6I3MXcpo_tXoVrFHazqkQaZmJvXZ0cBxQhd4s40IRRmjMwTFpvkQAH6Gb7-tcI8zeeCmo39s4G1ai_fqHUrbrr4XMq1agTgzYllBt1tQLb89esGRLc18bAWzWtAsfELR5eV7Mna1rwNssEEs5CgJOdT9HZgVdW9GeGqIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔴
فوری از فابریزیو رومانو:
🔻
لوکا مودریچ قراردادشو یک فصل دیگه با میلان تمدید کرد.
𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101483" target="_blank">📅 20:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101482">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHg98-rxE4X1KmHZm85mvvBIi4NFuirEtM19-SWM4HbqFeF-ErKr1gfEjthlDkeBE3QWS7OXYthn_qTuTxoSljvEYy1QP5smP5dIZFgQEYWFXsVohFOg7AYloxERvnFPMRXMgfMILo48Sbr8Z-0kqJguygf4HxoAAsXG2dwDdw7Ir8yd1ArAIAHtNdj3RRIuvMDiejgK4I1rJfu2-tLeMbdBVjY3LjexdnjIWeWdTOzfC1gOmm9aai4frG4VMXnYZDKSksW-HHSb3gUg8NKOSkPC8JbrG1TAfUjS9-eIclRCXrmDlbNTnQtiUqMA9Q59OFH1JCmFFTJerX3wuVELVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
||
بازیکنان جوان با بیشترین تعداد دریبل‌ موفق در تاریخ جام جهانی:
◉ 27 - لامینه یامال (2026)
👑
◎ 22 -
کیلیان امباپه (2018)
◎ 19 - جمال موسیالا (2022)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101482" target="_blank">📅 20:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101481">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZQTUb5XyfSsnLPnJH-6TF6m191uWLYDKNAQaQCrcr7XCpg0_7sLiJYC4k3hmqulmMNux3WAKojSKJWJOm3CT6fva_LEspkKPaqvCAwzUviu372NQPhmZjkxBi-DetbMj8acErixa5osPAkYINFd8jCc5gQBj_QH1j_IDRzU5FKAbgmnxA23q8OhmSX_7o4dR8FiEDDfrlJWM5yyPScf7tnfSfBdcoXU2lQSqDdQUO8DmlPDD0SMRZNRjVkN--xetNkU-HcWQkakVBFdRozJ4rGP4T4U5Lcz1VSPoAUGUVtKSQdgUfCNnPcYrOJECaKNb-NT1vQ5tnQo5-xbT870HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیلیان امباپه کاور EA FC27
نوجوان و جوان ایرانی باید ۱۱۰ تا دلار ۱۹۰هزارتومنی برای خرید این بازی خرج کنه. تازه اگه فقط بخواد آفلاین بازیش کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101481" target="_blank">📅 20:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101480">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDIVml3bIoe4xsjS081We2jf_79jGFm4XCgz7J2av4ff6uzZVQ2dabQ20sS58xyPkcwINF6I4DheyUF5gZU2f9n4brmXckOo684FSiKQbqdOvWBPX4cRl2NFBZ35lPnfZme7TGQn-05o_G3PT_9RIvJfMvxfDmRKm8utg-gHR9qerLHrgSD_66Pm-QCKH-uppZGy_fGma4WFM_BSkLnwX_AfI1o1KoOQPtIxLh-0C2rteULjYXzRi9Ht39kljdoO9GuzGjiXixue1FtrCQWYDuNkUgJSS_QAvReIawHTmwzGNVbfbYjkYD_xjFrFrmiPXJI4HPjLw0CIBDNvq3z-4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
گلوبو برزیل
🇧🇷
:
🇧🇷
• نیمار تا ماه دسامبر در باشگاه سانتوس باقی خواهد ماند تا قرارداد خود را به پایان برساند.
‏• در پایان سال، یا به یک باشگاه جدید خواهد پیوست (اگر پیشنهادی دریافت کند) یا ممکن است از فوتبال کناره‌گیری کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101480" target="_blank">📅 20:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101479">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33ffcc2a6a.mp4?token=AAXMI_ijDi5HV4qkeiUoso_r1-9NhhUNOh8vV4-g9bzVvA8Q709Yxpi2a7fYXGWmbGX6s4O6MDxYgbJouCoAy_pUM2wl5_aXGSxdw-udLeB_fDIGKa1_PPe1IztDBd3YKBpAd_YyVlYUtu1ERG4MUoXxewqeWfi7OA9iKJncDL2rsCqscdxcq2VzYIVvXbRTLk-VrE42yXbUixia3lfkgb_HeHN9q4gUZuaolQjcnx_UnhTMVHIv20P6G2xCn4uqj5vTuy_uHHhMWEGwYv195obY8eaP8CxRKujZsgvUL9g5yxpsjy9X-qtAvrjd6ZHzl0OrYZZq-Fd_y5mUH5bgaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33ffcc2a6a.mp4?token=AAXMI_ijDi5HV4qkeiUoso_r1-9NhhUNOh8vV4-g9bzVvA8Q709Yxpi2a7fYXGWmbGX6s4O6MDxYgbJouCoAy_pUM2wl5_aXGSxdw-udLeB_fDIGKa1_PPe1IztDBd3YKBpAd_YyVlYUtu1ERG4MUoXxewqeWfi7OA9iKJncDL2rsCqscdxcq2VzYIVvXbRTLk-VrE42yXbUixia3lfkgb_HeHN9q4gUZuaolQjcnx_UnhTMVHIv20P6G2xCn4uqj5vTuy_uHHhMWEGwYv195obY8eaP8CxRKujZsgvUL9g5yxpsjy9X-qtAvrjd6ZHzl0OrYZZq-Fd_y5mUH5bgaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
شیرین‌کاری لامین‌یامال در جشن دیشب اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101479" target="_blank">📅 20:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101477">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1111b268.mp4?token=LiAdkyGoDvtRSE6-QpEaTAhvPI1Ls1MisO2YrjhRJEn6cIWIdeQMv0mBDrXFnbFMGml3pSv5NiKcB04jszpH0p6EAl1xHMHH46XSYGJousONiZh2VcNnotCS5oy1P7W9UvcsjE3WTjjpiTGlbkgJufASymi85MUtyRMNUpsf4iKwvTFrXrdwVnXmd9VfOBHnnxkiocHLNHVHNvo15UKaU9UNl6YDEJUjsFsDdyL880z_tCB4I6NrIvpdNuyGhsH57GfpsNloJAQbHg0gdK5adgiQgQDjHa2SdI4xKH2WzpB98jaN6eu-8kf6tBhPgzf2Jq4va9G8eGMBRB49DSNIxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1111b268.mp4?token=LiAdkyGoDvtRSE6-QpEaTAhvPI1Ls1MisO2YrjhRJEn6cIWIdeQMv0mBDrXFnbFMGml3pSv5NiKcB04jszpH0p6EAl1xHMHH46XSYGJousONiZh2VcNnotCS5oy1P7W9UvcsjE3WTjjpiTGlbkgJufASymi85MUtyRMNUpsf4iKwvTFrXrdwVnXmd9VfOBHnnxkiocHLNHVHNvo15UKaU9UNl6YDEJUjsFsDdyL880z_tCB4I6NrIvpdNuyGhsH57GfpsNloJAQbHg0gdK5adgiQgQDjHa2SdI4xKH2WzpB98jaN6eu-8kf6tBhPgzf2Jq4va9G8eGMBRB49DSNIxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تایید دریافت پاداش میلیاردی از سوی قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101477" target="_blank">📅 20:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101476">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKUssLJRTK_WdavWxkykBAnx5w5_45b-aoQLUzd8nLzBz0LO0BQ3YfTEW_74VYVBXZlTGlbIT7MLYyYk-bfcWq8hX4qMpH82drLGcKnG-bfBQe3QLrg69GFMiqAgLohBVw8rIkDU0UrgELAedTM1T4QrTFeCGSD2C0uvz_Jqr0npgKLegHfu8DQ5GLYAWEHWZOl45zFJKzett2L4EkZlUIa2kEUbLR5bc_h1l76r3dqWMPfnmNcdSlBlkynanMv2lvQWROgfwp_wjo39YmSaF7mAOsbM2FhHA6LtqSHVbD6EzUufSFTknuwnX5oNBYQM8d0K6GKFTCeXQigksNzkrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بازی های پیش فصل چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101476" target="_blank">📅 19:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101475">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04bcfb9b29.mp4?token=bo5P6NqpcmSwNNKLEgVsM5mKaAViShdXQMkF4g8aLSLpaqeyjUuAlU8D2qf6ZbjinkC3iEd8vV1MaWDGbrctF7WBQcCz5dp2GCvp3XUhOHOWA_NLUHxL_PQnSGrfzBgLAyCS5wUr8R5s-VKtTDQXOW9G0Lt5AiJprseUvAu6iruebXu9VdSHZ9XVY7J83LoZkWGjMi-D2Tqw0r_HZCNjl_hrUoVM3cwXq6AQ6dnVSTFWgcDqbP6plCWL_Aiuq1sJZkbk7IMMo0HdgT8e8Dj5LEVchyn5xcdrIXNhjm6AygfrVg-7GNM-aUwLJA5oA54ukiRTn6CGsztuTAdwbS2WwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04bcfb9b29.mp4?token=bo5P6NqpcmSwNNKLEgVsM5mKaAViShdXQMkF4g8aLSLpaqeyjUuAlU8D2qf6ZbjinkC3iEd8vV1MaWDGbrctF7WBQcCz5dp2GCvp3XUhOHOWA_NLUHxL_PQnSGrfzBgLAyCS5wUr8R5s-VKtTDQXOW9G0Lt5AiJprseUvAu6iruebXu9VdSHZ9XVY7J83LoZkWGjMi-D2Tqw0r_HZCNjl_hrUoVM3cwXq6AQ6dnVSTFWgcDqbP6plCWL_Aiuq1sJZkbk7IMMo0HdgT8e8Dj5LEVchyn5xcdrIXNhjm6AygfrVg-7GNM-aUwLJA5oA54ukiRTn6CGsztuTAdwbS2WwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفتم قبلا یه جایی دیده بودمش‌ها!
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101475" target="_blank">📅 19:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101474">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101474" target="_blank">📅 19:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101473">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPfhRwbm30VInIkZnX7b97p5FJUSVOA0ql6rx2vff8K7ZBZ1z9YZFw8c2fwSX98KMlrFZoHIAx0SqhMDyNT_-8tEl8EISjLvfok9Dxnog6M-33iHVYahZlFUbKzRrMPnHA-ZblcCgk7lJ9gGG7V_Zkl3ozu3y1UFrVmXVEEmV_b__57YrGrpu7axEsf5GLKNriUce4FQ1cluWQ-y1aFLv7Sf1KzZ5rkVFPi_h-KCGVQ0gYKuhsET2_TDTXBFeUGAXnxLyN1vVTkik7OYN4MFWF9uWv3eEIATLyuKYYV9__ZetLhtrNvJckcMqNSGTEnHGW2h9lDzD-597kZ-PXZOKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101473" target="_blank">📅 19:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101472">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0fe520f72.mp4?token=IjENPXl4YzG4GB_3YXw9b7558tRgImWkxm2aYxYk1eq9cyssGqP--DroTtBSDysgokZ33Weq3uSc_bmg9K1vMFhbgyFDL9b4c_PIxAwajregwYUmPfVuF_V7idQOzExsVHig5yoi9pTFTcKb8sokzAq5eDyhhFFv_ekhXnNPcWkVsfBheykT1K8IWTja0DZ2tBpInYVV_szmJWrDsM52_7Emde_kXVODAkBcDGGaLc402_r8wam7jlM_6S_Bd0FZ10ZaXPJ-FfQ2SktRE7Azyv8tVghPM-VKPjCJoSYq0tEqDqkh6N576Jb8yFT-GXX33VHKZL5IUq2iZ99KKVSWSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0fe520f72.mp4?token=IjENPXl4YzG4GB_3YXw9b7558tRgImWkxm2aYxYk1eq9cyssGqP--DroTtBSDysgokZ33Weq3uSc_bmg9K1vMFhbgyFDL9b4c_PIxAwajregwYUmPfVuF_V7idQOzExsVHig5yoi9pTFTcKb8sokzAq5eDyhhFFv_ekhXnNPcWkVsfBheykT1K8IWTja0DZ2tBpInYVV_szmJWrDsM52_7Emde_kXVODAkBcDGGaLc402_r8wam7jlM_6S_Bd0FZ10ZaXPJ-FfQ2SktRE7Azyv8tVghPM-VKPjCJoSYq0tEqDqkh6N576Jb8yFT-GXX33VHKZL5IUq2iZ99KKVSWSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
👍
حمایت رودری از فران تورس در جشن قهرمانی تیم ملی اسپانیا: "شاید بازیکنی که بارها و بارها، ناعادلانه ازش انتقاد شد، ولی امروز... امروز بخشی از تاریخ فوتبال اسپانیاست!"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101472" target="_blank">📅 19:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101471">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74d5cadcb4.mp4?token=P1okZm0-aTGwpNVFoZvIVOMHe0kp3Dyv3lprNyFE-oLYLdSvgomSA1sUZzqegGi__5oyfG5EX1leE5C96xfjVsHKQ0_ma8n3tpv-3mWY3dFDIOtf5LDEyIZUGFvojkdFB880u5mzMD6LlsgDKgdEInrRxLrdAeqnLjSyJsAvvCwW6pPll-w3Hxu03WFxyiPSneO3ZcvhW7ywc6v3qA_yGT_hoZWXmsfd4xwIH4zfi2LxUBGLH7VB3KfrmERfNMMBZ1vrMlKwa13JMC8Oq4iWg_qx6569eFhXN0rU6Bpkg0MEmXvlUbeHDHepb_xw2sT7i0RlJyGo5IEMAXRUR_LDUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74d5cadcb4.mp4?token=P1okZm0-aTGwpNVFoZvIVOMHe0kp3Dyv3lprNyFE-oLYLdSvgomSA1sUZzqegGi__5oyfG5EX1leE5C96xfjVsHKQ0_ma8n3tpv-3mWY3dFDIOtf5LDEyIZUGFvojkdFB880u5mzMD6LlsgDKgdEInrRxLrdAeqnLjSyJsAvvCwW6pPll-w3Hxu03WFxyiPSneO3ZcvhW7ywc6v3qA_yGT_hoZWXmsfd4xwIH4zfi2LxUBGLH7VB3KfrmERfNMMBZ1vrMlKwa13JMC8Oq4iWg_qx6569eFhXN0rU6Bpkg0MEmXvlUbeHDHepb_xw2sT7i0RlJyGo5IEMAXRUR_LDUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
امباپه و اکسپوزیتو در میامی آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101471" target="_blank">📅 19:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101470">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXAeMpUETzaPWyuBuyYddGaaFDKqdCrh6qEnSPmUCK8ak-rhx19l55sjVKMIcfLiZBXOYS44FjiDNlsj9ltaz8JLgHBblrQoBGCXbuwyumFYnGuMay4lDIgy9b6V19OBxSlWKdM7DJiILwxvn4hZsD4YrSF5EFusQmdtzajV0jf--uHzxmPIwasB-17Gqpk7sB4AY18NExxrQGA0f8T8G3zFj7iiKOUYX2kCZZjt0fUIJD9YTwWQGKdIi39f5KtPAbj69kaq3d51Q0Vcsufa8CBFDyuPvEust2Hg2tkvnJUWU6TLf4dDQ0vWVNuPFJPluwIlNZPCp7s1KF6saAyDmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولیسه حدود دو سال پیش با دختری به اسم فاطمه وارد رابطه شد، اما بعد از جدایی، فاطمه باردار شد. اولیسه اول پدر بودنش رو رد کرد، اما بعد از تست DNA مشخص شد بچه متعلق به اونه. با این حال، گفته میشه هنوز مسئولیت پدری رو نپذیرفته و فقط از طریق وکیلش پرداخت نفقه رو قبول کرده. فاطمه هم پیگیر حق و حقوق خودشه و این ماجرا باعث موجی از انتقادها علیه اولیسه شده؛ تا جایی که کامنت‌های صفحش رو بسته.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101470" target="_blank">📅 18:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101469">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a52816cf.mp4?token=hZWI1DZwC0Uzk-8nHVHIGXCEfaCOCN2orxacr0K0Kb3vhIo7aJt_vRtbJaNg3sKDGF2mFg3efMrjcjGOWfKNMiU9so5D_cVDmzqUcjd8Oi0t2KGFW8Xt9auOeiG-Y1eCl_v6W9COLkWSmOtp3gXO1EkRrc_7weLIKaHoMnfW7kEibRrzajU1TD4CVuKah8-kn9B93RDpTtZu5lsNzWd24exek2pHcOacAb_azQI6xPW49B-wHhKU9BV0-umA8Zlpq8sP6bJ9S_krWGqw2k4KL8pN6Ob5rdknS9X1mqicFpDhZjqBGOycWjtuqCwrnnEmUQuErJLB98Tajnc04Kj_iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a52816cf.mp4?token=hZWI1DZwC0Uzk-8nHVHIGXCEfaCOCN2orxacr0K0Kb3vhIo7aJt_vRtbJaNg3sKDGF2mFg3efMrjcjGOWfKNMiU9so5D_cVDmzqUcjd8Oi0t2KGFW8Xt9auOeiG-Y1eCl_v6W9COLkWSmOtp3gXO1EkRrc_7weLIKaHoMnfW7kEibRrzajU1TD4CVuKah8-kn9B93RDpTtZu5lsNzWd24exek2pHcOacAb_azQI6xPW49B-wHhKU9BV0-umA8Zlpq8sP6bJ9S_krWGqw2k4KL8pN6Ob5rdknS9X1mqicFpDhZjqBGOycWjtuqCwrnnEmUQuErJLB98Tajnc04Kj_iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کنایه‌ریز دیشب رضا جاودانی و عادل فردوسی‌پور به محمدحسین میثاقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101469" target="_blank">📅 18:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101468">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFsjaUZm2_qOXSMRENwYd113LB0OJPR9JKMMCx_5_dFMg7Q9ql5jiKkJ4oWT1Ilhr5vF1iYL9A4bwm52PpARj4YfMe4g01nmr3k-NGAGMAZAnTo9GVf9WcBcMEcmNJAgaqp7MeawgQESVvUIRpG4zS5xRg8ZwZjuNwN7sM5tuzaLNTqxp0JdVvoK2GFqnRt_VaZ03R2Dl5A1L44WuPYgdHhH-Rptcf-8VATHGGn0z_EH11psPhH6-3ZOoxw7_mbdK-JA_SAF_oMdeRvh5HIvD9AXhcqx3_BZMDWVfU5P6F9iNhPDOLYyi5fdlcNoo2JvthYiH7Pp6A0DuHO1Vys1tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیلیان امباپه روی جلد FIFA 2027
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101468" target="_blank">📅 18:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101467">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeBa20pknOA7BKYmQBVBpCAIWHjnBqUNdmrURW42Xmn7pxkQWDJxk_fOQ6MG_CnI8CYholcOH5onDCmrIPhl202n_a7uvxiCqeFSMagWf5iY7eB7cJKRnK6N8XFdBPh2t_pyG2J5OT-NhrhEdJZ5dO2hhGn3_2_O7RKqfkraSJxFIPdvBXWHCG3i6gQZ4utI5-CJmWYTKGg7F5Uo5gpcUEzizV5qyp-VF-P8zER03JAc8QWGEnJ-Lqhwf_nCMxN0sBrdHL5p8xaxterABCO--mMVsUVDTE6K0UQeHhKi7sLLb7bszWBcMkz2Bx-19kOoe88pOGwTJlGyynynFNBSug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتونی تیلور، داور انگلیسی بازنشستگی خود را از داوری اعلام کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101467" target="_blank">📅 18:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101466">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaJza_XApis6uhbE9CGsqoTKm84wwKDQSnkJahnrN3giLzuxVlYkDm8l0tSus3mup4ohvx2QTVBmwIDgkztklK7n78XD9D7ppkJUuihzwUdsoRYgohT0tpnETN0wXZckxZbLASD2Bt5O0jC8yyhgcCwZGf1MaJ7und6CGnz5WcSJ9WwKiyWYfks89uHw3-EMKrm2LQVffOxW4BQg1omzTfKd8UzSAOGwA6UnMd8c9pbYm9OfDhTnWQt4d7VkBZWNFRoqO4s0oAjMXlrKxNXn4c0bwbG1knsZGnk6-9G7vIfYQMEtUB2UnHozq31F9BZPGYuL4QW9JvAPn7SAICHdRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ماتئو مورتو:
الهلال در شرف تکمیل قرارداد سامرویل است.
الهلال معتقد است که پیشنهاد بی نظیری ارائه کرده است و امیدوار است در ساعات آینده همه چیز را به پایان برساند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101466" target="_blank">📅 18:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101465">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIF_BPOdZ91WF-lcEylKHq7TDTk9php_X_Gf13VUXNmg0bK_zcAHHZjvAOfIp_Qjk2y7QBJGv5Qfm-bu7r6sXd-JQJ2vcAQXXlOhdUh_9Gq970IAMCpiWFgc7UMRNN0qYBtZfn44YI5gBBeeQ5ZX-etu1U9ZYlO6NaUbB6wwWeblqQc8gKjYlpCnYqr2DV-q4HedEuVEkJAoytv5gZ3Tg87D4vj16an_KgrB_Rg7mKr56NW1fw4EmJGkahlSW9REnx7Ci-_ZweLqhhvTypQEdrQG0--fpRm4WHT16ngi4JCq-kfDul-XAI1ZzFFjYvcojTEoFR2viTVB65D_WZQnqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
📊
تیم‌قلعه‌نویی پس از درخشش در جام‌جهانی با دو رتبه سقوط در جایگاه ۲۲ جهان و دوم آسیا قرار گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101465" target="_blank">📅 18:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101464">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f21557090e.mp4?token=erMrlUd7kUrsbDormhCLAGplTg3iMh9jhNLDU4WLd19GnJs40IGcBrJ276zBbjyJBeXBsMIX_ZWtw155Naan24ufp02zHuwxSnTeYzWhPHNVc0MKSu3Qkx-kDhAokqMG-0loDaFAc0xRxMuXPlXj-48qLv_UTY1-kNEjq3BlP8Ec0XOKSG12WJ6egf3PPhqpIhmWOrOjcdaiDIbs7DEHP4ZKe5bOEQC6HbyfQycPlrtvFL1KvWbSwKSczcNrvLxM75rxseezHH8R2b7i4tPZyIH-SFjbwA1bK79lvm5e-qMz9mAKFdXc5doDctJxdCzC7GiyjWxxw_GPeFkuMf_k5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f21557090e.mp4?token=erMrlUd7kUrsbDormhCLAGplTg3iMh9jhNLDU4WLd19GnJs40IGcBrJ276zBbjyJBeXBsMIX_ZWtw155Naan24ufp02zHuwxSnTeYzWhPHNVc0MKSu3Qkx-kDhAokqMG-0loDaFAc0xRxMuXPlXj-48qLv_UTY1-kNEjq3BlP8Ec0XOKSG12WJ6egf3PPhqpIhmWOrOjcdaiDIbs7DEHP4ZKe5bOEQC6HbyfQycPlrtvFL1KvWbSwKSczcNrvLxM75rxseezHH8R2b7i4tPZyIH-SFjbwA1bK79lvm5e-qMz9mAKFdXc5doDctJxdCzC7GiyjWxxw_GPeFkuMf_k5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشماممممم چه حرفایی علیه مسی و آرژانتین میگن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101464" target="_blank">📅 18:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101463">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">😢
تمامی سفرهای استاد اینفانتینو در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101463" target="_blank">📅 17:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101462">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yir_dZIUT7CWw5udI4Y4cVG8cl_Qu_UIdCD2i7NuNyyovRY2RchJR8U-CXciMePYL5jXUHXHJHqO7M5Qa_qsEzs7DQHtk9vXOFe0EEMQflBA2s-bU9fcOrwi7qtrH3Ju-0gEm6SkyAqPU5d9Ynvhts2awLqdyBS7LmDLhromJVH1fRjH1ZdeRWiLZ4JX0e-vuiyl4CZHYhJJ5j40wuKrMFVl8tpsn93odv-vN_TSkkz8Qp-JRd8Vhy4skfmnhdAl-_YCXyGktFCdYcSAxZ6bKw4NIHvKuV8BWprNu8VskFJaX7xc9HzplPdVYqKs0tYjaX2BsN40w83drOtueO0O4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: استون‌ویلا با ارائه پیشنهادی به چلسی خواستار جذب قرضی گارناچو با گزینه خرید در آینده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101462" target="_blank">📅 17:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101460">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oCAO8pV-0FE_nfIZvh97tfIG_Z0BKh7JmEtng1G6OYI19eIJDSPGHnJHw1dEEBjU4wDTIhoAisAVfGk_-3q1Qahr_agLzWv3aON8GPpoRdZjSQb9Bihx_BmTksUzdsID6hR9PuIeiAXHfWLnW_M0JIkd4NB81x_hkluwMInKou1PDtiwqOy7uX67FK1LpjAEYjRJw5jp38ofrCuF1rY41bvZsA86JnsIHGSQLKrR_QWkgZ_iGMwdAx4aGh8J85FoC9ImWdIX_pw1xlbxJK2t2-VgdV-7HKWSgTDGM53jhlwDRGFpJ_K9kTfOOZ0mH_b_tgld1EMma5aLCL26iwN5wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZLzWto1asTlnPJag7WKb5igiw8IrCQvdbDKn6dJWmHhzBvmTZHc3FeYZNynF7bUdyxsihDRrZh60dwYKztkOWxblvW1ju7uBKaFVtYRMWe65VToNegh9TSXj02kII8TCpVLjp_PyRCQTwNoiQ8kWA--clXn6kRjPR9Lo8EIOXqvWBwIfVxEFt03y6iprh4jAJeqxa74bhuRMfYsR3hydHFCwtL_psPjLNyZP3mc6m0ldVZInSE6l5Dywmf6v1s3FAwt_c-mDZeu37rjkm_5M8LBqcELtN-Pnf7Cg8Vl4trmXZqemUv0U04AtpWU_xra-UwfrqdP9AaSEBkihlXsCmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تصور کن ۵ سال کنار یه نفر زندگی کردی و خاطره ساختی، برای آینده‌تون نقشه کشیدی. بعد یه فوتبالیست با ۵۰ میلیون فالوئر، شهرت جهانی و حساب بانکی چندصد میلیون دلاری وارد زندگیتون میشه. فقط دو هفته طول میکشه تا اسمت از روی صفحه چتش حذف بشه و جای تو رو یه نفر دیگه بگیره. چند ماه بعد، تو از پشت تلویزیون داری جام جهانی رو میبینی و اون، کنار همون ستاره، تو جام جهانی از کنار زمین لبخند میزنه. اونجاست که میفهمی پول واقعا همه چیزه..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101460" target="_blank">📅 17:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101459">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/523aa1e339.mp4?token=kzR_Z8JcUDDYYaBNfISkHti1ARlYDuYVIUs7D56ENSakHFd4TBJP0D1BkOX1HrU0-SU7PTIvd3VE9avK1vR0Plvo3CPawC3bI2tjv2zeCPjnxf8gbasgbxwirlDQZMYkqLmFhFvh5PlHv9Og7a7xSezE6pHlaMcZwl6UWx3ssf52m5D5eNhZLM9yC7hckIm5E3hibAYWVgGM-WDMfNxYbP0V67Z4vfbHkHNN51bPQ6VnaNYSycjGwH2AHjw_BajfKlTGZlcS15M0qbFXJMzqrK9jLErFWcW8GZsMjDOL-h6xpv_ffOoUO1HkdG7_ZAXYj9pY0T3zKI4N4JlnRk4vb0Ej4wdvA0DUBVsERy96H_A5Yuo41pTrevCyAojRAsPGRvwPe-2YReH5kVZ-UUt-NoGf5e6NiEp_AJndSZ0BVUOiLU-8fkOoS6ej8kow3iVsfMZmPTjkxDAm6qZiWaWyxnoC3RuGViB-RJRd0q6OyfiXimK-px6N6OhnKtuXj01IMQfs5X24b31mRiobABVIimBO-bkf8rcldfjemLJ-mIxgx_Wg2nSN4nmol3bsNYmv1fD5H-ckOj_-IqY4ZCqqeCFO4UMBJNFNy1zHop1J93rBoKAVxKMvOPIudGoSAPG4v63KRJIZTpFnugoiBog41jYonqXTMPXDsv63-OGL0J8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/523aa1e339.mp4?token=kzR_Z8JcUDDYYaBNfISkHti1ARlYDuYVIUs7D56ENSakHFd4TBJP0D1BkOX1HrU0-SU7PTIvd3VE9avK1vR0Plvo3CPawC3bI2tjv2zeCPjnxf8gbasgbxwirlDQZMYkqLmFhFvh5PlHv9Og7a7xSezE6pHlaMcZwl6UWx3ssf52m5D5eNhZLM9yC7hckIm5E3hibAYWVgGM-WDMfNxYbP0V67Z4vfbHkHNN51bPQ6VnaNYSycjGwH2AHjw_BajfKlTGZlcS15M0qbFXJMzqrK9jLErFWcW8GZsMjDOL-h6xpv_ffOoUO1HkdG7_ZAXYj9pY0T3zKI4N4JlnRk4vb0Ej4wdvA0DUBVsERy96H_A5Yuo41pTrevCyAojRAsPGRvwPe-2YReH5kVZ-UUt-NoGf5e6NiEp_AJndSZ0BVUOiLU-8fkOoS6ej8kow3iVsfMZmPTjkxDAm6qZiWaWyxnoC3RuGViB-RJRd0q6OyfiXimK-px6N6OhnKtuXj01IMQfs5X24b31mRiobABVIimBO-bkf8rcldfjemLJ-mIxgx_Wg2nSN4nmol3bsNYmv1fD5H-ckOj_-IqY4ZCqqeCFO4UMBJNFNy1zHop1J93rBoKAVxKMvOPIudGoSAPG4v63KRJIZTpFnugoiBog41jYonqXTMPXDsv63-OGL0J8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🙂
نیکبخت‌واحدی: ۵ ساله پارتی نرفتم و الان دیگه با وجود هزینه ها نمیصرفه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101459" target="_blank">📅 17:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101458">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67a168b4f7.mp4?token=pKfFL_RkIonJ_9EEH13DMjBoBzRSEHh0TlXhwhYJBRkJAuc4vIjo64wufvOCNZn0swJukx2GdAGxMt2ARECcQn3f3Kfa7BBk4Ij50XTfALlaA0atnahWjzZ7UKsdsISTyxs8qTtM8X9_nheVXGegntySpEz3BP-EyPeUtZgKdGWBtZ7KSFAldoTx48JkKOxJJ5HRCXLsw5VIkEeMlb4WCrdXoyKZgQM-wy3R_OhOdOpa_zRHS-FuLvBxkJNGDeYEVgHooWfjt-OrbzMFIF8XD4tJxU77RnRNCyOe7qbnQF6gOzDGLoq7y9BGIIxe-6s8cC3kRvZYIIHTzKN89FlkHb65tPexaHz-exNhro6837ivkYDPYxFZeMTI9M_R1O1kliPIm3iVE-mNUbrtRI5xODGlmXMexsqUvOzCWcJW7G2bslS9QWryyrM1xGxuKvxWg0u7UVH6p52oU1CzRYgS-zcTYG9kHBvIn1XSj_o_GJVF6KdPDzQ2uPJccpglLTKkD1S5D_APtWpdw3MBdXtIPgl1-osMlUyRW886LTzf-5voq-TERTR2XzeHYtHAXVqRveaMgtXfhYbZ-KEURq39nWpZlyIJj6pFy0iPEvKlkuQbsqobwHfwZ8zz1BWymTqvdc6z62vRLwB4K_okk-tbZ19OpLvlLVDe7mfqGceak84" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67a168b4f7.mp4?token=pKfFL_RkIonJ_9EEH13DMjBoBzRSEHh0TlXhwhYJBRkJAuc4vIjo64wufvOCNZn0swJukx2GdAGxMt2ARECcQn3f3Kfa7BBk4Ij50XTfALlaA0atnahWjzZ7UKsdsISTyxs8qTtM8X9_nheVXGegntySpEz3BP-EyPeUtZgKdGWBtZ7KSFAldoTx48JkKOxJJ5HRCXLsw5VIkEeMlb4WCrdXoyKZgQM-wy3R_OhOdOpa_zRHS-FuLvBxkJNGDeYEVgHooWfjt-OrbzMFIF8XD4tJxU77RnRNCyOe7qbnQF6gOzDGLoq7y9BGIIxe-6s8cC3kRvZYIIHTzKN89FlkHb65tPexaHz-exNhro6837ivkYDPYxFZeMTI9M_R1O1kliPIm3iVE-mNUbrtRI5xODGlmXMexsqUvOzCWcJW7G2bslS9QWryyrM1xGxuKvxWg0u7UVH6p52oU1CzRYgS-zcTYG9kHBvIn1XSj_o_GJVF6KdPDzQ2uPJccpglLTKkD1S5D_APtWpdw3MBdXtIPgl1-osMlUyRW886LTzf-5voq-TERTR2XzeHYtHAXVqRveaMgtXfhYbZ-KEURq39nWpZlyIJj6pFy0iPEvKlkuQbsqobwHfwZ8zz1BWymTqvdc6z62vRLwB4K_okk-tbZ19OpLvlLVDe7mfqGceak84" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🔵
محمد خلیفه سنگربان جوان تیم‌ملی با عقد قراردادی به استقلال پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101458" target="_blank">📅 17:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101457">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a7dec4fc2.mp4?token=l-z_-UhEaDqybB8XF6G4FEOihftxRX6q_NwmD75-6wbv9qEzfVUqlkyx4523CuAX1nVyD7BLRW3RdGs5Nb0G3HYJYRrwYMDwwQpBpXdXhm2NnkdGdJQYqa3_--B6dO1alvKifHz_IvpH9FVlR8kN6Jw2XRu736eulKD2mKDw5-PYk7o_cEzWu7JLW1knWCid0L2e17r6-rJp60mOY248u5iYe5lKJjqQtZKhpmPCfBGgPl-mz3IW5KthZF7CvWemwM4XqaiJ-KeRYCAT0KimqIqQQIw3XKZkOxgMe8neuXlXFVcB7EJiuW0meFjkoRamGl1QXKLMFn7qVeIVCywDsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a7dec4fc2.mp4?token=l-z_-UhEaDqybB8XF6G4FEOihftxRX6q_NwmD75-6wbv9qEzfVUqlkyx4523CuAX1nVyD7BLRW3RdGs5Nb0G3HYJYRrwYMDwwQpBpXdXhm2NnkdGdJQYqa3_--B6dO1alvKifHz_IvpH9FVlR8kN6Jw2XRu736eulKD2mKDw5-PYk7o_cEzWu7JLW1knWCid0L2e17r6-rJp60mOY248u5iYe5lKJjqQtZKhpmPCfBGgPl-mz3IW5KthZF7CvWemwM4XqaiJ-KeRYCAT0KimqIqQQIw3XKZkOxgMe8neuXlXFVcB7EJiuW0meFjkoRamGl1QXKLMFn7qVeIVCywDsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
اسطوره وینیسیوس بعد عمل زیبایی در برزیل:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101457" target="_blank">📅 17:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101456">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48b2d769e6.mp4?token=vJfUowm2T9jFudyqhKH-WiiNvRtc61OY1NU9MDMgwMbuO1lq0yPrgu8if9ttFoYyEFOs345nQ9pwsddz__ZIXByoHVwcmLB7Z4h5_muz5hpO2--6kMPBQBI9LbL4pSXe2hkijzINwhW8mCxsmh3q8Bw_WfeNKYRt5CeyF4rcH6-oltSWZ7Ll2mzv9M1x9hgC8mUEoAYV4SQPG_ArHolCySUCmLiqtFun7H-YxPjtcFrR-1enj_f765UaBCGggnn8RrPeGg3FgKl7sSANBSVfskyynRtTLBgbjSNStxLBJKqxBW1rDpHk9lhQcmeU55J3BhKWubfJQ3a2kzg0mIqlxDjusS_DaX2Sq3y_p40Z3_SgMXT1ET3MhMjhI-3I8dXnFXze04nI2Q_mXSXboSwtsFvh2a81Ak-UJ6tMvN5szRf2dpmbViwRBQZ5ucd39ySFU2WTAyL6-dZTYnGr01lFSUJgL7Vf91QTQsYVLtN0eRBgnjQ1iPlig-NCNrOPb4vWXPEjI-_vTRm7uL0VvRCgw5OB19qvzaFjAN02_7uZagRuWPEVA3W3dJyYuuC_VIFPaS4xZEho-nQogzS_sZ5NHkkmDRktWoLvNQD_BrKabl_7TOfqAshLVeRZOo14djBAA4zzh0TnTA2SlSTSn31j0SvyeYwE-3YBbYnUnQrGpNY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48b2d769e6.mp4?token=vJfUowm2T9jFudyqhKH-WiiNvRtc61OY1NU9MDMgwMbuO1lq0yPrgu8if9ttFoYyEFOs345nQ9pwsddz__ZIXByoHVwcmLB7Z4h5_muz5hpO2--6kMPBQBI9LbL4pSXe2hkijzINwhW8mCxsmh3q8Bw_WfeNKYRt5CeyF4rcH6-oltSWZ7Ll2mzv9M1x9hgC8mUEoAYV4SQPG_ArHolCySUCmLiqtFun7H-YxPjtcFrR-1enj_f765UaBCGggnn8RrPeGg3FgKl7sSANBSVfskyynRtTLBgbjSNStxLBJKqxBW1rDpHk9lhQcmeU55J3BhKWubfJQ3a2kzg0mIqlxDjusS_DaX2Sq3y_p40Z3_SgMXT1ET3MhMjhI-3I8dXnFXze04nI2Q_mXSXboSwtsFvh2a81Ak-UJ6tMvN5szRf2dpmbViwRBQZ5ucd39ySFU2WTAyL6-dZTYnGr01lFSUJgL7Vf91QTQsYVLtN0eRBgnjQ1iPlig-NCNrOPb4vWXPEjI-_vTRm7uL0VvRCgw5OB19qvzaFjAN02_7uZagRuWPEVA3W3dJyYuuC_VIFPaS4xZEho-nQogzS_sZ5NHkkmDRktWoLvNQD_BrKabl_7TOfqAshLVeRZOo14djBAA4zzh0TnTA2SlSTSn31j0SvyeYwE-3YBbYnUnQrGpNY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❗️
زد و خورد شدید مردم بنگلادش پس از پایان فینال جام‌جهانی
🤣
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101456" target="_blank">📅 17:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101455">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba5d859c20.mp4?token=Nqwsa2aPWRjOxuDJnJ6JJnPn9F_jw82gfFHdxEgSfJRFVi_CC32hDHMRxAyAO-MvTldCr7tarDTsJm0SNnTCU-1oC12pHLRR19O6g5J2MiShrEz11IcRzpQ9Hmza7lic_r2yj4RRkW0FtfVyzD0ZeZNAFxojMWINg41Z9gtIXeZvn_kMNCBwAZbK6cqk3y2O0DZJaVhOA4H5n-CMdxKB1uDRy9hqsVeu9R75iILoOt7UPcr4QoMASYzJbY_KG_6-WqITqeexSR04XHJ62WpWhF3E7OrmovwoBWOeYtUF-dkeyGpn2KI8Css1frKfM5aLuEso1aIy2PZVlG2EM3EoVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba5d859c20.mp4?token=Nqwsa2aPWRjOxuDJnJ6JJnPn9F_jw82gfFHdxEgSfJRFVi_CC32hDHMRxAyAO-MvTldCr7tarDTsJm0SNnTCU-1oC12pHLRR19O6g5J2MiShrEz11IcRzpQ9Hmza7lic_r2yj4RRkW0FtfVyzD0ZeZNAFxojMWINg41Z9gtIXeZvn_kMNCBwAZbK6cqk3y2O0DZJaVhOA4H5n-CMdxKB1uDRy9hqsVeu9R75iILoOt7UPcr4QoMASYzJbY_KG_6-WqITqeexSR04XHJ62WpWhF3E7OrmovwoBWOeYtUF-dkeyGpn2KI8Css1frKfM5aLuEso1aIy2PZVlG2EM3EoVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
سرگرمی برادر لامین‌یامال با نیکو ویلیامز در جشن قهرمانی اسپانیا بعد فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101455" target="_blank">📅 16:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101454">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a645c836f.mp4?token=hSDuQqNiazdNXbnEFoyeHw3Yxf9j8aqVqsvk56Xt3Ub_D4M0mFcCn3ebUU49gLk-yXoNg9YbeF7BB_WUXZYkAmgPom6gKITMFi2SUjmjsfKlBPfVmRbgwKc4WAgxQyrGFrYd9pdpBGCfHaJuIpNG3jtiLXu-0zmcsR3lQkzt1zJFpWRup7wFqOscK7YGvzpZSMGh-sJVFX8Fyc6_yaYaLUzvRpRsEzWrbgc6_A76ZAk3cjX3CzjgUjIinGtgn0xz40IS8rdxvj3QLo12qvAQ4LB0pWjT2Lmtys-BqMJJHibAMKTFIfLIUJkUctR4SMLSZcNSocB7h8pu5U-R-4UUwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a645c836f.mp4?token=hSDuQqNiazdNXbnEFoyeHw3Yxf9j8aqVqsvk56Xt3Ub_D4M0mFcCn3ebUU49gLk-yXoNg9YbeF7BB_WUXZYkAmgPom6gKITMFi2SUjmjsfKlBPfVmRbgwKc4WAgxQyrGFrYd9pdpBGCfHaJuIpNG3jtiLXu-0zmcsR3lQkzt1zJFpWRup7wFqOscK7YGvzpZSMGh-sJVFX8Fyc6_yaYaLUzvRpRsEzWrbgc6_A76ZAk3cjX3CzjgUjIinGtgn0xz40IS8rdxvj3QLo12qvAQ4LB0pWjT2Lmtys-BqMJJHibAMKTFIfLIUJkUctR4SMLSZcNSocB7h8pu5U-R-4UUwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی‌کریمی بازیکن سابق استقلال: استراماچونی در حق ما استقلالی‌ها ظلم کرد. نباید تیم را ول می‌کرد و ناگهانی از تیم جدا می‌شد…
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101454" target="_blank">📅 16:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101453">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fA5qyUOMgN9CJfxbpAKnKpqYtPYe536aFvAkzVdSrbdYTVHgh6RZB640t_XFswS8zXSdfm6zw4qfjCDiK7tYz8dQkpji0CwJouCCsHuv0BFFXAOtU-ZBjnEb-qdZx6My3OIStq9YcFpsv388RzK5qfJ1M-T6NtwXg8UpaB07cPyZMXxZmSZj4X5pA3aqKouNShZklsEPOGSbJN1WS9xJwRLjSe93a3NItHMV3L_G_C1HSBRCbr9uTGg7IRbOsDkhDGgQwwz9poxW6nmNDMBpJkOUVBouc0TMLcdb0SN897U84N1h5_nMM7Jg4TDwluJ2I4BMPeHXK-pNn11U0vnpTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
بند فسخ قرارداد آیمریک‌لاپورت با بیلبائو ۱۵ میلیون یورو است و اگر بارسا برای جذب وی اقدام کند، به راحتی موفق به امضای قرارداد خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/101453" target="_blank">📅 16:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101452">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c9c58dc1c.mp4?token=Q94UFBBxud0pkgI_bAFkB0IIgJ9Kgb4t7iO-WWduhPdXlxmW5fqTQ9KVM6IcK-t0il32Jq_WJHaGE3ephEbJ7Ndgw00He-Jb3QW76LwHSbT6Kbw5q5snI3F3U7BDG2U7Jr7IohL88NaYprQosF4VfaZ5xqCVhMfbtGwoFk5I5ZtCkAElspdelh2zE6P2U9kUs2kGhngxy21oUjucl7BCNB0ODkdVZkreJtAglzSrRPQI7IXuzTFYjpzR-6wZjJOIjqS6kADIaP5yGJ21mEsPWe2Or4qrg8aq1lah3SM1GJn5ryCIYPXayH3og_iavahASjIHqK3i66nTXa6E2lPABqTkfryvaRQcMsUC8SOkNjlFXLppYNz8HNZL3syhPdlFKuRPDVLUn7mEcFzkMQz7z0iFg2hBP_4v9hDY63D9I_NN-ZIwh5T6BeNMMtaakZdi9cmujSX0hXPdEm-tWdKmEGzilJEY_y90AcOYy3ZitFqO8PI84FsdtHsB5eUMW6RgDJmr0UcKd1BdItanUszosoU6Q8n1ro3GAQXRs4Uahs9COd-XuWk7MMUyMx_w6_xxjU6lxzSnOOGkMfeYWFO0SzgWkqm61W96mbE-lbtL8CmNE0VuGhiqFQgRiyzGfpvITvOYNKRFYLKIphJSE4qSYfgLejbTELqcbYf9fpCa8ik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c9c58dc1c.mp4?token=Q94UFBBxud0pkgI_bAFkB0IIgJ9Kgb4t7iO-WWduhPdXlxmW5fqTQ9KVM6IcK-t0il32Jq_WJHaGE3ephEbJ7Ndgw00He-Jb3QW76LwHSbT6Kbw5q5snI3F3U7BDG2U7Jr7IohL88NaYprQosF4VfaZ5xqCVhMfbtGwoFk5I5ZtCkAElspdelh2zE6P2U9kUs2kGhngxy21oUjucl7BCNB0ODkdVZkreJtAglzSrRPQI7IXuzTFYjpzR-6wZjJOIjqS6kADIaP5yGJ21mEsPWe2Or4qrg8aq1lah3SM1GJn5ryCIYPXayH3og_iavahASjIHqK3i66nTXa6E2lPABqTkfryvaRQcMsUC8SOkNjlFXLppYNz8HNZL3syhPdlFKuRPDVLUn7mEcFzkMQz7z0iFg2hBP_4v9hDY63D9I_NN-ZIwh5T6BeNMMtaakZdi9cmujSX0hXPdEm-tWdKmEGzilJEY_y90AcOYy3ZitFqO8PI84FsdtHsB5eUMW6RgDJmr0UcKd1BdItanUszosoU6Q8n1ro3GAQXRs4Uahs9COd-XuWk7MMUyMx_w6_xxjU6lxzSnOOGkMfeYWFO0SzgWkqm61W96mbE-lbtL8CmNE0VuGhiqFQgRiyzGfpvITvOYNKRFYLKIphJSE4qSYfgLejbTELqcbYf9fpCa8ik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
ایمان صفا بازیگر سینما: با کری خوانی‌ام دل خیلی از استقلالی‌ها رو شکوندم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101452" target="_blank">📅 16:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101451">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🎁
بهترین اسلات‌ها با چرخش‌های رایگان یک بت
💥
تسویه سریع و آنی جوایز شما
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💯
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101451" target="_blank">📅 16:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101450">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gv14YSxlDfgOwebvaqNXudahdEnV1fB-jqmYv-aR18jfiNoDaTGWOqPlY_yId6AECSMChwGe4SdmiG3CPAFYL08CRYbgewoLnTRL5d2JHinoERw_6DF9mgQ0DI24YxI-bsJgeG1bqjEpWYkTsF8yeDFRvpqzTENzFzY5YbwBDFMusubZMeYswBx8XrXAxjz_nIP7YZLX9H4a-03QLD6FtaQN2C6mtqHIxr83YCskbifFMKJC-OVH_A_rAHpbXU9xGRqZRyt6Y5cWGBzXUHhH9nctDNIZFtc74dsvt0CPIEOoPiLiJzqxjBLY-zWZHYiqRUsFuHf6-Ukmsl8OPQ4K-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
فری اسپین‌های بیشتر، هیجان بیشتر!
🎰
با واریز از طریق کریپتو، ووچر پریمیوم، ووچر اتوپیا و اتوپیا، بیشترین پاداش را دریافت کنید!
✨
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101450" target="_blank">📅 16:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101448">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68a6db964c.mp4?token=p3H5Io3dlEspfHiEHoPkUbae67_g433Ie903D-ike784WWA9l4pzFFFfMs5JY4ZtPiYbM8bJayARcvg1pUtYUPuS-vI29NU-zcIzmJ0jCFC3WgTPX_65aKuVxhqisHeXNzUeEbC2_qZ-YPaWgPxM-p3pDVo5zr8wWNZ4r4ok5syWL7Zik2SXUklHnCyxqYO0omSZcR-ikUiGmRoe8175qJz-Gwmmr4UjrqvHfvddtlYfd89Mul1pr3jXlEGNHQrUKTsOYUNO3szinCbPMj4_-sYbC-cpGfib1JuMpStY15wvV_0x9vToUXmmTq6ewjdpJ6r6l-ccTChT3vZQzVca8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68a6db964c.mp4?token=p3H5Io3dlEspfHiEHoPkUbae67_g433Ie903D-ike784WWA9l4pzFFFfMs5JY4ZtPiYbM8bJayARcvg1pUtYUPuS-vI29NU-zcIzmJ0jCFC3WgTPX_65aKuVxhqisHeXNzUeEbC2_qZ-YPaWgPxM-p3pDVo5zr8wWNZ4r4ok5syWL7Zik2SXUklHnCyxqYO0omSZcR-ikUiGmRoe8175qJz-Gwmmr4UjrqvHfvddtlYfd89Mul1pr3jXlEGNHQrUKTsOYUNO3szinCbPMj4_-sYbC-cpGfib1JuMpStY15wvV_0x9vToUXmmTq6ewjdpJ6r6l-ccTChT3vZQzVca8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🙂
خاطره علی کریمی بازیکن سابق استقلال از اسپانیایی صحبت کردن میلاد محمدی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101448" target="_blank">📅 15:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101447">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53a9000335.mp4?token=AoYzg_efFJOLhJ4-LCDw_YFe_rs7vYAVjpAWcBT_xCgxvvAuTAiyM0qqPUgWBqI_dsPyKzI27V7KIwSNk8jM26XQOEAM7ORZQsgIKFASfHkOFt_VHm2-OIicd5C0bSk6rVd616sS-x6vXnv0h4SCOwo-Vn9yOV5zf55KOFipcbFD22o4CEStu7v8yrJxH4eNZKHM3El9jsXkgWGf0_sfoLFqM8YsoGIQuzTG3b-gR7-fbzKSMkRBmjfDDsfE_2ard3sgZ5fuC9fW8cKjBZZLefVSCtd_AbLq18UZd1RFRUF3Cezm21uVkPN3CK3zaZoRBTGD7-EKKkVlrb8JZ1uDSp7_hRcLnGn7LCmBbPp7zTSGy3b1ECxrnDfjdHuu8h9MCGJzpRaT-cz9rbaFjt49THKuMqGibmPtr7wBkBrqEavTEKwwsqSNHoBdMBCAT9s8NbKpW1he6LT2ey3452efKfRey0ALEtRoGi2TchyZ90PsoSDvGzdeFoApK-LTCNIgnrRj9pfuDRbbHl0OfA1b0PcSj1sYc62m73eoPEvCkwvR9NeM7mcG4pbRXQrRiB9yN-AGNH013oc8qc9_2PTWWnjFskErE_tKUWTgVVxCGF--kaKmb74xYrWt7AqUln9VTVOStGqaMdR2VC2zeaeOeIx3CfBp2KK-nBXppI7AJwI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53a9000335.mp4?token=AoYzg_efFJOLhJ4-LCDw_YFe_rs7vYAVjpAWcBT_xCgxvvAuTAiyM0qqPUgWBqI_dsPyKzI27V7KIwSNk8jM26XQOEAM7ORZQsgIKFASfHkOFt_VHm2-OIicd5C0bSk6rVd616sS-x6vXnv0h4SCOwo-Vn9yOV5zf55KOFipcbFD22o4CEStu7v8yrJxH4eNZKHM3El9jsXkgWGf0_sfoLFqM8YsoGIQuzTG3b-gR7-fbzKSMkRBmjfDDsfE_2ard3sgZ5fuC9fW8cKjBZZLefVSCtd_AbLq18UZd1RFRUF3Cezm21uVkPN3CK3zaZoRBTGD7-EKKkVlrb8JZ1uDSp7_hRcLnGn7LCmBbPp7zTSGy3b1ECxrnDfjdHuu8h9MCGJzpRaT-cz9rbaFjt49THKuMqGibmPtr7wBkBrqEavTEKwwsqSNHoBdMBCAT9s8NbKpW1he6LT2ey3452efKfRey0ALEtRoGi2TchyZ90PsoSDvGzdeFoApK-LTCNIgnrRj9pfuDRbbHl0OfA1b0PcSj1sYc62m73eoPEvCkwvR9NeM7mcG4pbRXQrRiB9yN-AGNH013oc8qc9_2PTWWnjFskErE_tKUWTgVVxCGF--kaKmb74xYrWt7AqUln9VTVOStGqaMdR2VC2zeaeOeIx3CfBp2KK-nBXppI7AJwI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
علیرضا جهانبخش: در مکزیک زیاد بهمون بد نگذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101447" target="_blank">📅 15:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101446">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f60626ee05.mp4?token=b-EJWlwUF90TkfE20-wREokiDiJjQx5ysSPq1GBLy1v4g40Fu4w6nMp-GtSblH3aAYP-QZv2tGemwnY2Dd-BeI1ZIBLlzKTwjsPWunPd8ibQWM0PEob6lax797qO5qPuCjSB7a1VhE-DL72z_MFQLACjtf1F4AZjAnfvAFPtkbZkZoubPericyH7TWTDQOtaZKOfhv41d31fIqPyb1RJPh9_UBYtpwLuclVlWFdB3Vc9nOS5tWYRt7gll8s92pFHlROt8KOrpYwzNpP-OwjVszYW-o8lIpX3KmtmAgGsD2Ymy46fiRp6s_6D6lYBBif4aRKfI-MxMKgQhizWIggW5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f60626ee05.mp4?token=b-EJWlwUF90TkfE20-wREokiDiJjQx5ysSPq1GBLy1v4g40Fu4w6nMp-GtSblH3aAYP-QZv2tGemwnY2Dd-BeI1ZIBLlzKTwjsPWunPd8ibQWM0PEob6lax797qO5qPuCjSB7a1VhE-DL72z_MFQLACjtf1F4AZjAnfvAFPtkbZkZoubPericyH7TWTDQOtaZKOfhv41d31fIqPyb1RJPh9_UBYtpwLuclVlWFdB3Vc9nOS5tWYRt7gll8s92pFHlROt8KOrpYwzNpP-OwjVszYW-o8lIpX3KmtmAgGsD2Ymy46fiRp6s_6D6lYBBif4aRKfI-MxMKgQhizWIggW5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
👤
محبوبیت خریدنی نیست...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/101446" target="_blank">📅 15:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101444">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0WVmcBRwOtxVRcrL1m4KRZj0WTN8HhWmZJvzovgqkLJtf5fI-54DgtPkFco84YHEXmBWPyb31KcsMfqPS7euhpaE9SsyZBRHUTi3JhEOQB5VdOPxxbSc0bXIAl50GToChsBPp8lOyP8q8epcOzqaLm9N7I2msJ6cljds0SOeriIn9DAiItkblP8XltIMTuIYJVgIanTBsDYorK9ZpP54Wcs221waPFAZ7OFevFfEi0-GynRQ4NnddyLfhuM1j-H7MnxAfH-MH1J3ECEMDX5V_JwQhgnluiC5MwGfs9IYS3zvqrGA2bBCFenrqAe1yerWxUEtYRJmomShsSTT6qcmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔵
علیرضا کوشکی دقایقی‌پیش قرارداد خود را با استقلال تمدید کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/101444" target="_blank">📅 14:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101443">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd8a4b410a.mp4?token=Ji71XX7vhxXUFWjNdhYPMMLr4EujWxKWDSkqGsQ0eePPI_b-yn4P-l-KJVhQjVcvb0_2iE3UbzY6I_LEVxMWCO-V3DEQpGAizk-eFuq_s55pj_RswLMBZvyZMs5636KybvNtBsmTwLuVz5Q8jKsjcs_xWQsmqXXX_nppBiv8Vld6sYwHATWCZoUFkn8MOIMnntL4UFYoNL4DCApmvIdLux14BYErTQWGoRqVuIWi-10x93skpeWAFi_eoPTGp-m6ssEidTXoMrKOulNVqHg6oCeB76-Ur3aZ9NnCyAU9AZHykcyPgJsdpBMSOvhaDv6B7mgiHmp68QiijAvUWpA2MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd8a4b410a.mp4?token=Ji71XX7vhxXUFWjNdhYPMMLr4EujWxKWDSkqGsQ0eePPI_b-yn4P-l-KJVhQjVcvb0_2iE3UbzY6I_LEVxMWCO-V3DEQpGAizk-eFuq_s55pj_RswLMBZvyZMs5636KybvNtBsmTwLuVz5Q8jKsjcs_xWQsmqXXX_nppBiv8Vld6sYwHATWCZoUFkn8MOIMnntL4UFYoNL4DCApmvIdLux14BYErTQWGoRqVuIWi-10x93skpeWAFi_eoPTGp-m6ssEidTXoMrKOulNVqHg6oCeB76-Ur3aZ9NnCyAU9AZHykcyPgJsdpBMSOvhaDv6B7mgiHmp68QiijAvUWpA2MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
عکس یامال روی پهپاد انتحاری شاهد قبل از شلیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101443" target="_blank">📅 14:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101442">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLxXpMekjiLV6JF1sKE9UWaRxjqCkB-PdA8Srgbun0Wp4Unl-8MCD2cXF4vgksI6NqTLi0eESARIE7pojzOAoo7ehgtAKbYM5n4tmihhpKVa6FFWl3B39aZazWIwn4zWhSbg0_RttA4fVketbS072T_SO2LfmLItHtPfnbMNrpp6fASyuh8_jQEvKFFotB_PcdmHKDIRXUrkiB7ljN7MT-1N_lR9nB4Gpu2dzq5hv-YnjCkqHMblMsJxbRBxzccTW-2vOa0USdhEOPWEkG4_PhqxX4oVrPp9TQfLQo1_dwY9NoPaIECI0JVfTcYi3gCMbGzEp8_Tcl0ltiOLLEDyGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رامین‌رضاییان با انتشار این استوری تقریبا جدایی خودش از استقلال رو اعلام کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/101442" target="_blank">📅 14:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101441">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JN4k6OyV0eZ2IUmbXDXL0c-TqndDA0ghopneGqZR22uAucQxJYqs_bLgzmglLSnT-074y-ymUXGnXQ8eJUYAvVaidxiDTWWRa4c-qnhFWuAymKC9l1eq1T_gBrxBpclqH6ck7Hb5BR62ELdFBSJ20Q1YPAFDwtT-CKwvM2-y4yqJ1NIvB9tpplWdM9-anfoAdFEhC9M52XGC8udgqsAn8njj-lmjKPAxgAhDbsiVExDszwwXRLxC1T6KcbyXEGvuAt50k1KY6oXeGg1gHx6_h4s_ZypFlmx1DHiC4-HHAXvFbnTDpEWXtjmgt1Hm5JDzqPuw5sEMZ-zGaib30MPAFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🔥
لیگ‌های بزرگ اروپایی چه زمانی آغاز می‌شوند؟
🏴󠁧󠁢󠁥󠁮󠁧󠁿
[31] روز تا بازگشت لیگ برتر انگلیس باقی مانده است.
🇪🇸
[25] روز تا بازگشت لیگ اسپانیا باقی مانده است.
🇫🇷
[33] روز تا بازگشت لیگ فرانسه باقی مانده است.
🇩🇪
[38] روز تا بازگشت بوندسلیگا آلمان باقی مانده است.
🇮🇹
[33] روز تا بازگشت سری آ ایتالیا باقی مانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/101441" target="_blank">📅 14:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101440">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f0fd702ff.mp4?token=QO2PCwpHvOmJoIto4NUggbGffReXzU0M2ATvyAjqCuowCqDv2gXT7oIrD_HrS_hs1dM6Ms_zRDz9OlsjUUUf93EnMp2OGvqP3avB6EDyWHjunnI7c3bcYWGfljqhwN9VyMy9kZmkrrcIluDKR42kXbrvBEVd8qBbH282dtvWqglUEiQ82fQjg8YumIdSXhNH2cCGlTvefGQbnL9Qfw72im-Gh2J2BDwdIeBrrvUS9M-TwonXZvlVqOA1P-CpkfhhXsCDUYbeYqTstzulmgJTkFDNSFIe6xETRdFLRS8sJOhwwwEIJP93TGkQ0RFPuhY7UuOIntdG4eY01Q9iFAHN6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f0fd702ff.mp4?token=QO2PCwpHvOmJoIto4NUggbGffReXzU0M2ATvyAjqCuowCqDv2gXT7oIrD_HrS_hs1dM6Ms_zRDz9OlsjUUUf93EnMp2OGvqP3avB6EDyWHjunnI7c3bcYWGfljqhwN9VyMy9kZmkrrcIluDKR42kXbrvBEVd8qBbH282dtvWqglUEiQ82fQjg8YumIdSXhNH2cCGlTvefGQbnL9Qfw72im-Gh2J2BDwdIeBrrvUS9M-TwonXZvlVqOA1P-CpkfhhXsCDUYbeYqTstzulmgJTkFDNSFIe6xETRdFLRS8sJOhwwwEIJP93TGkQ0RFPuhY7UuOIntdG4eY01Q9iFAHN6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
خانواده سلطنتی اسپانیا در مراسم استقبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101440" target="_blank">📅 14:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101439">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوووووری؛ متئو مورتو: برخی از اعضای مدیریتی رئال‌مادرید درحال پیشنهاد به پرز برای بازنگری در مسئله جذب رودری است. این بازیکن از سبد خرید پرز حذف شده و حالا با درخشش فوق‌العاده‌ای در جام‌جهانی مجددا نظر مادرید رو جلب کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/101439" target="_blank">📅 13:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101438">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e455125710.mp4?token=NI4OaM1xx9jcj1cx-mJsyjHiK0eCHgfYOKwKJfOeSHljqdGpbw8uRECtZAsb_gP-9Fhn4FHVMvI6tAC-p02Owb1caxwZCPdm2fqYFXl73KBkrLaRQdcQqH8lmYoOiscfUi6JaEa2E_A5iPnw1rHVzguUrh3vpMOTquHBZu23fiLn4WLlAsG5OlnZLA9XbmKMHu0NFVQSwSj33-lhHPXsa6qRC4TS3BI4Kh-IN3E3tBn7DK138NBL4JVzJixPAV4LboNvTOKwZc_lwoJh_MWs4poTWCnXXHmOz9ho3441_fUf5NLYz9RsSOLdq96fhmNmFKEBs41pZZuR-HuKYngp-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e455125710.mp4?token=NI4OaM1xx9jcj1cx-mJsyjHiK0eCHgfYOKwKJfOeSHljqdGpbw8uRECtZAsb_gP-9Fhn4FHVMvI6tAC-p02Owb1caxwZCPdm2fqYFXl73KBkrLaRQdcQqH8lmYoOiscfUi6JaEa2E_A5iPnw1rHVzguUrh3vpMOTquHBZu23fiLn4WLlAsG5OlnZLA9XbmKMHu0NFVQSwSj33-lhHPXsa6qRC4TS3BI4Kh-IN3E3tBn7DK138NBL4JVzJixPAV4LboNvTOKwZc_lwoJh_MWs4poTWCnXXHmOz9ho3441_fUf5NLYz9RsSOLdq96fhmNmFKEBs41pZZuR-HuKYngp-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
دیس فوق سنگین ابوطالب به قلعه نویی: ما تو غار کنار عادل فردوسی‌پور هستیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/101438" target="_blank">📅 13:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101437">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcMDEOc5ji3oVCuUuDhYBU2xSMXIEONq4UuqRVbeNOotWf5cbI8Cb8F8v9Hru3kViEy6ZCZhEKmYeyH3bvnjqzZVS5kfl3QuISZNpZvNaLJzV-TgJlLNTyzdcphcz0aqyHS4d3uRUJRwe2iwplB0r8YUOVZ8YNEaEEo2EN4oV1_NK7LW2570Lv3MVnOReMemkqJmhE2mXrlOizLaDom5y5pfTqUr0EDZZVSfFhzccrKRLJYKU-J4dy3iK7N5SSkUT8IJ5GoChLfSwI4fgvG7PE78nv85PzaGYZ7dKR5c4_-1DjiMPuoAPMuJfDcuRBjN8bdpRaYxbO_H6-SP_rdumw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوووووری
؛ متئو مورتو: برخی از اعضای مدیریتی رئال‌مادرید درحال پیشنهاد به پرز برای بازنگری در مسئله جذب رودری است. این بازیکن از سبد خرید پرز حذف شده و حالا با درخشش فوق‌العاده‌ای در جام‌جهانی مجددا نظر مادرید رو جلب کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/101437" target="_blank">📅 13:33 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

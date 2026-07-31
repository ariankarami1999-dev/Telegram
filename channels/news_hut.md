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
<img src="https://cdn4.telesco.pe/file/W-GwR4AepoI8Gx9auHL2O1X5gcndJ8DnGa47vOLyHmIfm061-mSosy22_CxTXjtNpGzuaMTKIG4npt_N0M2-719YHdoBOwgNoY5Fcoql6sAmlJAatBL-GPfBN7P4sqFqnnD4QgIhbFopafN-zSRYIFjn6EBMNIxqdsHU0lzD_2Ul23BfM0KH48_G7m_9rDLPXUjsZK3KeS5Y341cSkSPEgSpTwo8LCHtwvyaqWCJ-BA3MC_x1jyNYcG8wRb6c82yJ0qoKDBn7gf_3yXFnahdPWqZl3Ft31gPMiWhBTF87Sp9T4bFLL7oLwdRWpoL0xaDI2MRTeWjwjInceSOPD2Q2g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 139K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 20:50:37</div>
<hr>

<div class="tg-post" id="msg-69324">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d259260d40.mp4?token=WCoK8amzfKwice_gIVbB-qnZxyYsNBaF-UzlQodkVpUqYECwXVJS-ibF0uxQjZ45oqpLsnHWg1XiQ3_flbuwJhFIgzcAHNb1eRZiY1SiY4FxPucxBxAHRJR9e-rfKXQP0FCuseCV9fPif9j_sgoWvT1s89F5gySAi8ftkHCr5ShRwhj6D1IE2iT3N5me2gwOtRhrHDxqzC_u8K-bfjX2I0FtNhb0tNybZTZPZrxXdsjpPN2au__0eccBEt-tvRpfwpaV4mqFGSPja4OqkaALasM2205l7NGON3npIjkihQ9a18rllqVNg_GPfapkmQR3qaLYvV-DACeD51pEP48lODzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d259260d40.mp4?token=WCoK8amzfKwice_gIVbB-qnZxyYsNBaF-UzlQodkVpUqYECwXVJS-ibF0uxQjZ45oqpLsnHWg1XiQ3_flbuwJhFIgzcAHNb1eRZiY1SiY4FxPucxBxAHRJR9e-rfKXQP0FCuseCV9fPif9j_sgoWvT1s89F5gySAi8ftkHCr5ShRwhj6D1IE2iT3N5me2gwOtRhrHDxqzC_u8K-bfjX2I0FtNhb0tNybZTZPZrxXdsjpPN2au__0eccBEt-tvRpfwpaV4mqFGSPja4OqkaALasM2205l7NGON3npIjkihQ9a18rllqVNg_GPfapkmQR3qaLYvV-DACeD51pEP48lODzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت های یک عرب درباره ایران:
ایران از جامعه عرب متنفر است، یک تنفر تاریخی.
همانگونه که اسرائیل از جامعه عرب تنفر دارد.
اگر کتاب فردوسی(کتاب شاهنامه و قوم پارس)رو بخونید شک ندارم که ممکنه باعث بشه بالا بیارید.
چرا؟چون عرب را به زشت‌ترین اوصاف وصف میکند.
مثلا فردوسی گفته:عرب در آن مکان خورنده ادرار شتر است،خورنده ملخ اس، ولگرد و کثیف است.
اما فردوسی میگوید اینجا در ایران حتی یک سگ در اصفهان از آب پاک و زلال رودخانه میخورد.
حتی یک سگ در اصفهان شریف تر از عرب در آن مکان است.
@News_Hut</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/news_hut/69324" target="_blank">📅 20:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69323">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea4c431667.mp4?token=EV0Bdw8Kn9-FXOcHtc4FCx9FQNPegxE2exNLb5EPav0MbsMuFkn7eYjva_B3-qtvaExou0KlYBrHQ5C69nfHZXByiX6X5d-gAe8p2huw-qkz_JQ_TFpxzMP0lnN8hj4j-wqCrfUC9pXwyaEo502chBhYqHhP0nM5aus0Idd4DtIHrqe5YBRl7byDqk2qIL7g8hOCW7DbV4MmnwSrWX45Jo2Pb2WPT9k8U44V-USU3lL2vfEkVp1qsUoIuwfvVBLrCg__IKf_9F-Gc319xi9HpQM9PSuEkKrF14ye1mJPkWwLCm4TA8keigALnRcW_fnjm1cZS5KiPy5bwf0EXHD5Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea4c431667.mp4?token=EV0Bdw8Kn9-FXOcHtc4FCx9FQNPegxE2exNLb5EPav0MbsMuFkn7eYjva_B3-qtvaExou0KlYBrHQ5C69nfHZXByiX6X5d-gAe8p2huw-qkz_JQ_TFpxzMP0lnN8hj4j-wqCrfUC9pXwyaEo502chBhYqHhP0nM5aus0Idd4DtIHrqe5YBRl7byDqk2qIL7g8hOCW7DbV4MmnwSrWX45Jo2Pb2WPT9k8U44V-USU3lL2vfEkVp1qsUoIuwfvVBLrCg__IKf_9F-Gc319xi9HpQM9PSuEkKrF14ye1mJPkWwLCm4TA8keigALnRcW_fnjm1cZS5KiPy5bwf0EXHD5Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🤡
یه بخشی از صحبت های خیلی مهم ترامپ: بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ  @HutNewsPlus</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/news_hut/69323" target="_blank">📅 19:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69322">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884550e186.mp4?token=r7cRMtTeCWbZJ4kZWDh2Z3ct1NnaUcXOcEulVJJ6NYocBzr8menBqWsl1QzTm0OK1-aUf1loxYh16Yetu2_UOxe8y0LcOS9P7Yu33Shxmm7CmlzWJT8Kcb52gIMSjhfru4T7TZeEtcBBRsfzBM6eLBQnynmeFgUJFA45cOLIt7yNYsIYqYvFQPD-pEv2NWHoSt7CIuNokzewAMvHAGS8vO2SOv-afDC58fKvlv-sorMa9Ng06aAP2ik0krKIg-QEjF9AOgxPpsR11GXImdta7khgFXp4MiYEiYZpi5n-A5Uah66Bt64cxTZgftR60lxTKsO24rsnn-7BFfnw6aiXQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884550e186.mp4?token=r7cRMtTeCWbZJ4kZWDh2Z3ct1NnaUcXOcEulVJJ6NYocBzr8menBqWsl1QzTm0OK1-aUf1loxYh16Yetu2_UOxe8y0LcOS9P7Yu33Shxmm7CmlzWJT8Kcb52gIMSjhfru4T7TZeEtcBBRsfzBM6eLBQnynmeFgUJFA45cOLIt7yNYsIYqYvFQPD-pEv2NWHoSt7CIuNokzewAMvHAGS8vO2SOv-afDC58fKvlv-sorMa9Ng06aAP2ik0krKIg-QEjF9AOgxPpsR11GXImdta7khgFXp4MiYEiYZpi5n-A5Uah66Bt64cxTZgftR60lxTKsO24rsnn-7BFfnw6aiXQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🤡
یه بخشی از صحبت های خیلی مهم ترامپ: بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ
@HutNewsPlus</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/news_hut/69322" target="_blank">📅 19:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69321">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caed943dd3.mp4?token=AvI_0iOjPaUPGOKYAhosLaWT2wbQm750Wz3Z5NqugBPr7icHo2yeQFfyQD6rPoXdGl3b7MBPrzM26vKi3RCtbgN1ia5DxWK_QNN1nthXIWM7_g0_Bet8U8BrdacVqfVe2szpq2UJHGuj5DiX9urXDLOvV8ZK3jws-JQ9vLOnTJGEiZm4Zf0KOGhhlNj2IsPTivvHEpCmb39tDlGcKsW37k9xQWqzurmBWar1GmR5Nt5v8HVkpBF5UUaFh6m0umzTuWVtOZz7ms_Touat0Srt53xZFQ4YuExYQaB4moAPFXqZnlwWPxlyVtYvPcxvv0kRw4IHMMhn7MIa_ltpIIEB1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caed943dd3.mp4?token=AvI_0iOjPaUPGOKYAhosLaWT2wbQm750Wz3Z5NqugBPr7icHo2yeQFfyQD6rPoXdGl3b7MBPrzM26vKi3RCtbgN1ia5DxWK_QNN1nthXIWM7_g0_Bet8U8BrdacVqfVe2szpq2UJHGuj5DiX9urXDLOvV8ZK3jws-JQ9vLOnTJGEiZm4Zf0KOGhhlNj2IsPTivvHEpCmb39tDlGcKsW37k9xQWqzurmBWar1GmR5Nt5v8HVkpBF5UUaFh6m0umzTuWVtOZz7ms_Touat0Srt53xZFQ4YuExYQaB4moAPFXqZnlwWPxlyVtYvPcxvv0kRw4IHMMhn7MIa_ltpIIEB1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خبرنگار:
در مورد ایران، گزارشی وجود دارد که نشان می‌دهد شما پیشنهادی از سوی ارتش برای گسترش چشمگیر فعالیت‌ها دریافت کرده‌اید.
ترامپ:
ما از قبل گسترش داشته‌ایم. منظور از "گسترش چشمگیر فعالیت‌ها" چیست؟
@News_Hut</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/news_hut/69321" target="_blank">📅 19:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69320">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">املاکی تو یه جمله همزمان گفت هم می‌خوایم خیلی شدید به اونا ضربه بزنیم و هم می‌خوایم خیلی مهربون باشیم باهاشون
🤡
#hjAly‌</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/news_hut/69320" target="_blank">📅 19:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69319">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0411d5fa4.mp4?token=XkbIQrD2N1wbmy1g3-Dd65Z7s5SbHxTK2Zz_jcJXcXmtgRB60YCE-juaXge2_55p8waeq4h2xkEgiOmi6tUVvBKGnaFtWvxjhRm5ZSTVVp-ip2UAfNQz44sJLXufdaeDS7p-nwN_etlLLdpdLpy150ojwGnCvYUro8VVZ03F5uS_0eUxEJi_0tvMgznuzv7vcgdCpsGiETlF0QdR7OCcu2FD-lYLrJD8znNnXPoUBFBpxrQcku3obTV2NwgbQS-w5RRWT0JY5UmT2sD4tT2ByDudtizuxyYCHjBok6Zy6v2UtgPcZ5OhRZvsPFJqsov7TlBXwBedE9T09RC5qcpR1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0411d5fa4.mp4?token=XkbIQrD2N1wbmy1g3-Dd65Z7s5SbHxTK2Zz_jcJXcXmtgRB60YCE-juaXge2_55p8waeq4h2xkEgiOmi6tUVvBKGnaFtWvxjhRm5ZSTVVp-ip2UAfNQz44sJLXufdaeDS7p-nwN_etlLLdpdLpy150ojwGnCvYUro8VVZ03F5uS_0eUxEJi_0tvMgznuzv7vcgdCpsGiETlF0QdR7OCcu2FD-lYLrJD8znNnXPoUBFBpxrQcku3obTV2NwgbQS-w5RRWT0JY5UmT2sD4tT2ByDudtizuxyYCHjBok6Zy6v2UtgPcZ5OhRZvsPFJqsov7TlBXwBedE9T09RC5qcpR1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ایران وضعیت خیلی بدی داره؛ واقعاً خیلی بد. اوضاعشون خیلی خراب شده و تحت فشار شدیدی هستن.
تعامل باهاشون هم خیلی سخت بوده؛ هم صادق نبودن، هم قابل اعتماد رفتار نکردن.
ولی این چیزی رو عوض نمی‌کنه؛ چون در هر صورت، حال و روزشون خیلی بده.
ما فقط پنج ماهه اونجا هستیم. اگه به جنگ ویتنام نگاه کنید، می‌بینید آمریکا بیست سال اونجا بود. کاری که الان علیه ایران انجام می‌دیم، از نظر من یک عملیات نظامیه، نه جنگ.
ایران هنوز چند تا موشک داره، اما خیلی کمتر از چهار پنج ماه پیش.
توان تولید موشک‌شون تقریباً از بین رفته و ظرفیت پهپادیشون هم تقریباً نابود شده.
البته هنوز مقداری از این توانایی‌ها رو دارن.»
@News_Hut</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/news_hut/69319" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69318">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b0ec710b6.mp4?token=e07J-KyaHIPycX3xWtVxe8qrgaSQljVou0QsZNwQS7InjYaAgm8yfYurEodzeUFozkc7x8CWBY1hEUtZepsewgu7969Ol8c5z0ICKohwFWRiUbXhvBHabQMrtK4iQ5edZ3XUhQYaHQvyeysg71CAyD_RLjPybvntARXf0iRQU2HoX2UOlQaPL_loKHVAFnfqe3Vvh42Aijco6aM4FaEodrD1nlCZQAECyGjExPaqj7fDOoclm5LNi3R8EfLzrA9Hk9-Joh1HMiGVBXiB0EWPOHRpddfm9L_bwcGwB1NELR-avN-Da0E56cQukUrAAh2_hTNTbU8A94CP5g4xsqTnfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b0ec710b6.mp4?token=e07J-KyaHIPycX3xWtVxe8qrgaSQljVou0QsZNwQS7InjYaAgm8yfYurEodzeUFozkc7x8CWBY1hEUtZepsewgu7969Ol8c5z0ICKohwFWRiUbXhvBHabQMrtK4iQ5edZ3XUhQYaHQvyeysg71CAyD_RLjPybvntARXf0iRQU2HoX2UOlQaPL_loKHVAFnfqe3Vvh42Aijco6aM4FaEodrD1nlCZQAECyGjExPaqj7fDOoclm5LNi3R8EfLzrA9Hk9-Joh1HMiGVBXiB0EWPOHRpddfm9L_bwcGwB1NELR-avN-Da0E56cQukUrAAh2_hTNTbU8A94CP5g4xsqTnfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست:
اگر برایتان سؤال است که چرا حوثی‌ها، با وجود اینکه یکی از نیروهای نیابتی ایران هستند، وارد این درگیری نشده‌اند، دلیلش این است که به مدت ۴۵ روز، قدرت نظامی آمریکا را از نزدیک تجربه کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/news_hut/69318" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69314">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64a849aad2.mp4?token=E4H1q2AJi7Xr_P0sPap6iGPtjJtpGXGSIXguFEReUhiWfbuGG9RiNvdkQAgISW4rXqPBWdfssoZawg45ZN3HGYYhG6UgwjE5DSPJ1hFcgPiw1xlKA7JAHoSw8Z8QrGzzYUTeUNtba9Yf2NwBJFf_jsmfszD5WpNFN-253_LIw4OIBy1h7AqVvtdKKbcskGdB6Ykx6__HX_0N7Q7VT5VRKEIUJ-HBLnn1snCnyVn-zDelLl4x_qvRS_Scxr5VRwKdqtkTj94V98G4lxbYqLLgkrR9CD8ZF3xCn1Qyb1WwbF2-Jh7gckENm8BOZ-H6DUr670Sr9zdzQSBXScE8JqNwUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64a849aad2.mp4?token=E4H1q2AJi7Xr_P0sPap6iGPtjJtpGXGSIXguFEReUhiWfbuGG9RiNvdkQAgISW4rXqPBWdfssoZawg45ZN3HGYYhG6UgwjE5DSPJ1hFcgPiw1xlKA7JAHoSw8Z8QrGzzYUTeUNtba9Yf2NwBJFf_jsmfszD5WpNFN-253_LIw4OIBy1h7AqVvtdKKbcskGdB6Ykx6__HX_0N7Q7VT5VRKEIUJ-HBLnn1snCnyVn-zDelLl4x_qvRS_Scxr5VRwKdqtkTj94V98G4lxbYqLLgkrR9CD8ZF3xCn1Qyb1WwbF2-Jh7gckENm8BOZ-H6DUr670Sr9zdzQSBXScE8JqNwUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇪🇸
آخرین آپدیت از وضعیت اسپانیا:
- مهاجرین غیرقانونی همین‌جوری تو سطح شهر پخش شدن.
- چندین مورد دزدی از فروشگاه‌ها گزارش شده.
- کنترل اوضاع از دست پلیس اسپانیا خارج شده.
- مردمِ محلی گروه تشکیل دادن و دارن هرجا مهاجر می‌بینن، کتک‌شون میزنن!
- تو بارسلون هم مردم دارن خونه‌هاشون رو از ترس مهاجرین، سیم خاردار می‌کشن...
@News_Hut</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/news_hut/69314" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69313">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: به زودی، دیگر چیزی از ظرفیت نظامی ایران باقی نخواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/news_hut/69313" target="_blank">📅 19:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69312">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ایران در تعامل با ما صادق نبوده است
@News_Hut</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/news_hut/69312" target="_blank">📅 19:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69311">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14e0b272c3.mp4?token=IYUBdSWLoYbnN1aaWJb_b-g4YoQh43KraozN3YglwvMSp3XvME8ioHA9OfPaYzoZ00x64BPAOTresDjS3lhTWgy4KGIRgqjpqPTSlVX5hAEXEE7H7OAftXn67ou7vDmV0iM8hdJ7S8USwAcb-eIGlEj7BVDPKwuHcph_7ZKcN_ImEfbMCOBqJPSw0CKrFtakmI-dq5wkFCYouuI_hSLzBaKW6BWCpknPEeSV7G07U7rk0mY5dyinxxSOKFenvva2RMmgUTp-wrUOmXWS3lqRNx2YmxQApniZLeePRKP4Y51BkVIOT34MkaThG0_P3yAypmhOoI4025HBAWY7HAy9zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14e0b272c3.mp4?token=IYUBdSWLoYbnN1aaWJb_b-g4YoQh43KraozN3YglwvMSp3XvME8ioHA9OfPaYzoZ00x64BPAOTresDjS3lhTWgy4KGIRgqjpqPTSlVX5hAEXEE7H7OAftXn67ou7vDmV0iM8hdJ7S8USwAcb-eIGlEj7BVDPKwuHcph_7ZKcN_ImEfbMCOBqJPSw0CKrFtakmI-dq5wkFCYouuI_hSLzBaKW6BWCpknPEeSV7G07U7rk0mY5dyinxxSOKFenvva2RMmgUTp-wrUOmXWS3lqRNx2YmxQApniZLeePRKP4Y51BkVIOT34MkaThG0_P3yAypmhOoI4025HBAWY7HAy9zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
ترامپ با بالگرد «مارین وان» (Marine One) وارد «کمپ دیوید» شد تا سیزدهمین جلسه کابینه دولت دوم خود را در آنجا برگزار کند.
فاصله کمپ دیوید تا کاخ سفید با بالگرد تنها ۳۰ دقیقه است و رؤسای جمهور آمریکا از زمان فرانکلین روزولت (FDR) در سال ۱۹۴۲ از این مکان استفاده کرده‌اند.
نام این مکان برگرفته از نام نوه‌ی آیزنهاور، یعنی «دیوید» است که توسط خود او انتخاب شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/69311" target="_blank">📅 19:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69310">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQTmxReds7fgMeWH9GnXjd-JT4rmg9K2NKc6oLpyi0n6KoIMkvRT4dGsk6rTVIAJ_TqX6AjK18z2-XDYYje6Ls1uFUgOfJ-teHqVvZAFE5eAU2wgf4PNPBD9ZHmQcFRm2fcomp55ecGSvF6MYC3YuQGiqLwbTqufnbYi3Pzfv3S4kmodOuRxSjiMp5yS-AHX4c777pVxxhA0H_OkPhfcEdqnNjlmIZvRdJNOCuhVCZmu96GuPXcwoPASPD2_rNKs_C8mynKpY9z50BKujZrHOWTz3AjVAY9viyNe76uYCNRQC0ZzWn1dJCJ8QrhGcASEPylrqpzycLebbZynRdR_vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نهاد مدیریت آبراهه خلیج فارس:
به علت تداوم اقدامات تجاوزکارانه نیروهای نظامی ایالات متحده در منطقه، تردد از تنگه هرمز امکان‌پذیر نمی‌باشد. به محض برقراری ثبات و آرامش، کلیه درخواستها بر اساس ترتیب و زمان‌بندی بررسی و مجوزها به مرور صادر خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/69310" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69309">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
حملات پهبادی به جزیره بوبیان کویت
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/69309" target="_blank">📅 18:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69308">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31550cb053.mp4?token=CJivoSzLY7TDX9tCRdoHU3JG4cqxY7Zj7t8Fpj-fu4_EGxgPIrMR0mhzjpWbxL8TmqakaYZ9pDyh6xxXMZz9DCkkay-R5JQl6JR9z5OuS7N0wCBywteHWl953fpcEJNJwdF0TIVrW7DKfMEJnVL-q6DFolm4M8bpW7yebaMEToZyV8v1grzNOSbVEReZs-SA18OVcM6ZMtnB-95HMGvjUZ8SB5j-OFtvLOAakWAW_ZijVzuDG-4YyvixWDd71zx_zZ6XaTo6Dw4Y1YJeKmF2FvUf5ULnqd8lyFOjHeOV3nsoj6Cqyso2ydknyM5ix8vYN9A-O6C8lI7bFXJcqf5_DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31550cb053.mp4?token=CJivoSzLY7TDX9tCRdoHU3JG4cqxY7Zj7t8Fpj-fu4_EGxgPIrMR0mhzjpWbxL8TmqakaYZ9pDyh6xxXMZz9DCkkay-R5JQl6JR9z5OuS7N0wCBywteHWl953fpcEJNJwdF0TIVrW7DKfMEJnVL-q6DFolm4M8bpW7yebaMEToZyV8v1grzNOSbVEReZs-SA18OVcM6ZMtnB-95HMGvjUZ8SB5j-OFtvLOAakWAW_ZijVzuDG-4YyvixWDd71zx_zZ6XaTo6Dw4Y1YJeKmF2FvUf5ULnqd8lyFOjHeOV3nsoj6Cqyso2ydknyM5ix8vYN9A-O6C8lI7bFXJcqf5_DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ در گفتگو با فاکس‌نیوز:
«اوضاع خوب پیش می‌رود. تنها کاری که می‌توان کرد این است که به پیروزی ادامه دهیم؛
آن‌گاه سرانجام اتفاقی خواهد افتاد.
ما ضربات سختی به آن‌ها وارد می‌کنیم و آن‌ها را کاملاً گیج و سردرگم کرده‌ایم، و همچنان به پیروزی ادامه می‌دهیم.
سرانجام آن‌ها چاره‌ای جز بازگشت به خانه نخواهند داشت.»
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/69308" target="_blank">📅 18:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69307">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAbO4NI4_Y77orqeebYQsDAtVOA7MP0CoCqceRAS9GvQ1oNwFLpnjhZkvd5TkkCVCRFTHIdldapDJ2JsbrA3lEgkxGeQqaitlZuROPIOxmQxYJuIa0DEVWnPXpeQisRqw9uEwAezPODsq0lTV0Z1RaWJohJ-4pSNGKS65b-dterW0XRK6y0Z7zHhIlO-G28PZarN3tSCBQRuRdJnPYobacAKoOiQAlwaEygg1NJZmLt59dLDS4FTys9M0GQulLMIYlo-kshzjt5ZO2ybBN1O8m3wdEDwopYR0ixrKxnR_5XuKXaZe_1zh-eSIZE4voSBn23VCbUWoUEOcEImpcdeTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇼
❌
🇮🇷
وزارت دفاع کویت:
نیروهای مسلح پهپادهای خصمانه‌ای که اوایل امروز وارد آسمان کویت شدند را رهگیری و نابود کردند.
حملات ایرانی همچنین چندین سایت نظامی و زیرساخت‌های حیاتی را هدف قرار دادند که باعث آسیب مادی ناشی از سقوط آوار شد، اما هیچ تلفاتی گزارش نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/69307" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69306">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4497b03176.mp4?token=hnZyPUz6kp9Ln-Tz3Oqao6qtVhB0m54oGlbOMvergnB2rPH9SrmxPw4Rg01chztPa9IJA5Otq3dW_QDP-L2KV9XAtuV59p-G66SpuVbJMWJSkel81BkGrRQX-e0NS7LG9EfSgra9pSsjv0dcxn6tt-pY7gbxF8hc5ux6FtRjI1vEiTDYdg62qlIKDNQcoGCpYe_hdqfX6DDXIKHy0VxkrOJbqr6yJTSKGBex03Tn0cKRrXInPBGfY67Y_dO-Yn7-qxy3DxdfiCMIMXI-mwjif66KK2tgY--LM89kXOtLuRwgQoZAijJHkCoRjPx2BIa-ytaINOX1wk6BXppRyaMU4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4497b03176.mp4?token=hnZyPUz6kp9Ln-Tz3Oqao6qtVhB0m54oGlbOMvergnB2rPH9SrmxPw4Rg01chztPa9IJA5Otq3dW_QDP-L2KV9XAtuV59p-G66SpuVbJMWJSkel81BkGrRQX-e0NS7LG9EfSgra9pSsjv0dcxn6tt-pY7gbxF8hc5ux6FtRjI1vEiTDYdg62qlIKDNQcoGCpYe_hdqfX6DDXIKHy0VxkrOJbqr6yJTSKGBex03Tn0cKRrXInPBGfY67Y_dO-Yn7-qxy3DxdfiCMIMXI-mwjif66KK2tgY--LM89kXOtLuRwgQoZAijJHkCoRjPx2BIa-ytaINOX1wk6BXppRyaMU4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کابینه ترامپ برای بررسی اقدام بعدی خود در قبال ایران به کمپ دیوید می‌رود.
این خبر ساعاتی پس از آن منتشر شد که ترامپ از توافقی «تاریخی» با میانجیگری مصر، قطر و ترکیه خبر داد که بر اساس آن حماس با خلع سلاح کامل موافقت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/69306" target="_blank">📅 17:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69304">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006b9f5bfa.mp4?token=p3q4-pSEF-bYsXOi1VrZTg61iCzIC4xXyCsQwRlEcD8vDpjF1OGYslnRhVMGrCNpf-r6QchvV62RAkCGvCbLdwEK3QhSaZP2O5iWAHz0Ck3esqM3WnyNrVUN7Mt8usM0GmySXOs_8RBS0f0r0YKZpr9Kho5tWgwmUkOFBA2IqkiGQ0LGo0YRV6QYxU8TpbcizM4MMg3MbSBllibWBIT93kVabmQ0OYBRz3M3qgn1EeMY2j-3xtGmDmzVQDNk6GU2Xv0sj4bbM0326svHd4p37zs7PSsM4k8Xi0melUErbS1ASQ0F7EqzeYMAfU1cIxGnKyuUNlBoWjMH9NaKHHxveQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006b9f5bfa.mp4?token=p3q4-pSEF-bYsXOi1VrZTg61iCzIC4xXyCsQwRlEcD8vDpjF1OGYslnRhVMGrCNpf-r6QchvV62RAkCGvCbLdwEK3QhSaZP2O5iWAHz0Ck3esqM3WnyNrVUN7Mt8usM0GmySXOs_8RBS0f0r0YKZpr9Kho5tWgwmUkOFBA2IqkiGQ0LGo0YRV6QYxU8TpbcizM4MMg3MbSBllibWBIT93kVabmQ0OYBRz3M3qgn1EeMY2j-3xtGmDmzVQDNk6GU2Xv0sj4bbM0326svHd4p37zs7PSsM4k8Xi0melUErbS1ASQ0F7EqzeYMAfU1cIxGnKyuUNlBoWjMH9NaKHHxveQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
شهر سئوتا، منطقه تحت کنترل اسپانیا در شمال آفریقا، با یه بحران جدی امنیتی و انسانی روبه‌رو شده.
فقط توی یک هفته گذشته، حدود
1500 مهاجر
با شنا خودشون رو از مراکش به سئوتا رسوندن.
رئیس دولت محلی سئوتا گفته مراکز پذیرش دیگه ظرفیت ندارن، صدها نفر مجبور شدن توی فضای باز بخوابن و مراکز نگهداری از
کودکان و نوجوانان بدون همراه
با
2400 درصد ظرفیت
در حال فعالیت هستن.
الان به‌طور میانگین
روزانه 300 نفر
وارد سئوتا می‌شن و مقام‌های اسپانیایی نگرانن که دوباره بحران سال
2021
تکرار بشه؛ زمانی که حدود
10 هزار مهاجر
فقط در چند روز وارد این منطقه شده بودن.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/69304" target="_blank">📅 16:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69303">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNEoa3z83DhAmzHX79exkK9qm8caMwF6_7-43V3W11mOpO16TUjW6oYvzNnOtBDb6sFSBgN5grLxLYFwLspNngtuW_HLTrfFibu3cy5gjzKo4A1C3iu2XY-VJ6Rn5kXgWofx3NdaiaZ2je0neZlXIJ61Mi5eFItEexiZDzp3wX_syg9v2EpSgvSZtzmOYO7-7qDNa4dwyIGhQ9lAiXIVL558iP4TdrLO0DW3pcI3ZvaCiR7XEpLpeBlpyIZl86JzVPeR8h_i-lo7OzfT7_TdAidV1Um67Ni2jm1mm9dK5mSqt1quvtRQ2AwcBDkYTnEuxnCyjfbisRhx4UnTQ-QMhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پسر رئیس بانک سپه که دهه هشتادیه معاون بانک دی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69303" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69302">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nT0CMqL5pPY3arsHSxgGKfOSv2B5DwmznjC3YRpW0B_11eqtUwcgQqVSwuvY6_mV49Sd_9ZA2SogOD2z95i6b8lHSjoYGMJffj53FxnT4yfyeyIJwqFmYLWJkao3xDolM7fNNmBP-f5P9ZXq5dE9z3F8FY7blInvMXqlLVRw3KkJIbppJnRf5qofylH29tF9BbQNWq8av_FVr8dXk39XmG8sL6nX0M2y6AprRWs6fhJJFxd8Dz0bHg2jn3H52GnHr5aDMFCOItYnIN5u56wuAmx0jZ9bf9F2eS-Ps93GMewhegq6XZjskDUV8xBxcJI5soJxjHBp_TtP5w9ZheuSdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
طبق داده های نت بلاکس دولت ترکیه اینترنت کل مردم رو قطع کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69302" target="_blank">📅 15:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69301">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1tDxlaxzjR2YB9JxyQWxuEnwLhHabUAIQq8wr0VnJc4sZ7f9oaXx_v9rf2svFmKudl5VVBzBIkXlMttV1rZojBaKnbzGnnyXTIcgEu0gvjgKec83vxZkUcWSfJy60u8c4IDMGnCa_H8NpecIDQuHGXgHsWquRatVx-0UaWDELHqTAcOm3DyM6AF3uMPG7GIw2kAMWzuM9gskdP3FxZTCBwQlvJMPLVismSd6uupipiV9EobYGeqSn8vN9OOq28jQ2-rYFpOPlbNldowfMmW3jCwtITuQynlhmK_Q0QSA0ehmwvFTv30hR1EwCceKd5-qKgQaazAAR28nicUIAthvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
گاردین:
عربستان داره خودشو برای یه عملیات نظامی گسترده دریایی و احتمالا زمینی، علیه حوثی‌های یمن آماده میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69301" target="_blank">📅 15:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69300">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🇺🇸
رویترز:
پرزیدنت ترامپ امروز در کمپ دیوید با مقامات ارشد دولت، تیم امنیت ملی و فرماندهان نظامی دیدار خواهد کرد تا درباره مسائل مختلف و از جمله جنگ ایران گفتگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69300" target="_blank">📅 15:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69299">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb0ff0fef7.mp4?token=dHmabU2NopAQjTroZ22lBRTZYwcCKbxVRa19oJvFM0Z-3xdmteqbv4vndGO8_4Xx4ZSE1ki4DqdKqNliZ66dpUsJXYE2moxPGuNwSATShqYsLZ1o1LU8Yh-TOvbEXNCwxF2b_xbu2x5TjISOsNbjpLLIb65BCV50ub76jSo9NvRqdTcqdkM5AEINzNHkUq-sOENwuISAF0B7A7HsOvcvFIpxqRlXjW_VYMtIRiNIEsa8RcV8mLH4Kz-bWzIeSxxbWaNkfM_6PTuRS8h6PNMdsUE4gl45Y9AhgQnN0OJQFQCIoe3pRuxUjSMOYBL3cp1BQenMVju_SfyWX9AODhWS-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb0ff0fef7.mp4?token=dHmabU2NopAQjTroZ22lBRTZYwcCKbxVRa19oJvFM0Z-3xdmteqbv4vndGO8_4Xx4ZSE1ki4DqdKqNliZ66dpUsJXYE2moxPGuNwSATShqYsLZ1o1LU8Yh-TOvbEXNCwxF2b_xbu2x5TjISOsNbjpLLIb65BCV50ub76jSo9NvRqdTcqdkM5AEINzNHkUq-sOENwuISAF0B7A7HsOvcvFIpxqRlXjW_VYMtIRiNIEsa8RcV8mLH4Kz-bWzIeSxxbWaNkfM_6PTuRS8h6PNMdsUE4gl45Y9AhgQnN0OJQFQCIoe3pRuxUjSMOYBL3cp1BQenMVju_SfyWX9AODhWS-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
🇮🇱
تلگراف:آمریکا و اسرائیل در حال بررسی طرح محاصره زمینی ایران هستند!
به گزارش روزنامه «تلگراف»، آمریکا و اسرائیل در حال بررسی احتمال اعمال محاصره زمینی علیه ایران هستند تا فشار اقتصادی بر این حکومت را تشدید کنند.
دونالد ترامپ و بنیامین نتانیاهو در جریان گفتگوهای خود در دفتر بیضی‌شکل کاخ سفید، درباره «ابزارهای نظامی (کینتیک) و غیرنظامی (غیرکینتیک)» بحث و تبادل نظر کردند؛
از جمله اعمال فشار بر همسایگانی نظیر عراق و پاکستان برای تشدید کنترل یا بستن گذرگاه‌های مرزی.
یک مقام ارشد اسرائیلی به تلگراف گفت: «اگر مسیرهای زمینی را مسدود کنیم چه می‌شود؟ فرض کنید ایران دیگر نتواند هیچ کالایی وارد یا صادر کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69299" target="_blank">📅 14:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69298">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🇮🇱
وزیر دفاع اسرائیل ، یسرائیل کاتز:
اگر ترامپ از ما بخواهد، به حمله به ايران ملحق خواهیم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69298" target="_blank">📅 14:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69297">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34cbdd236b.mp4?token=tC1rsMlUDHsVDALGsuJS3FuG6vQ9T1GYOVL9x9Im0SNA9Su6y-_5GS042UdPsGCiyPCWxMdZNRLGaXbGl1MXLpZIpLL_RXNANW0WCLJrkWuU1zuoHKnHCaifnKEvVBPZ9e3Gs3msUmHZEP0N96ke4LX04pEGlbGgAA6iW2Xe1gnhbcJo6WXJH_SddL8ys1Mx1EhPrQuboNw3_bp7k6YXWmJ2qV4v6WyFD7fTOXpw9QE72qaZJHQkJxxW6cIZRV7PJdGQ7pg6HUwxcpnVWcOUsSsSaO70-Ikn08jE_MNSXQqFC299u7eAk_WJaMWu6ndd7fOfUmLJVuFwwyY7Fnvs-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34cbdd236b.mp4?token=tC1rsMlUDHsVDALGsuJS3FuG6vQ9T1GYOVL9x9Im0SNA9Su6y-_5GS042UdPsGCiyPCWxMdZNRLGaXbGl1MXLpZIpLL_RXNANW0WCLJrkWuU1zuoHKnHCaifnKEvVBPZ9e3Gs3msUmHZEP0N96ke4LX04pEGlbGgAA6iW2Xe1gnhbcJo6WXJH_SddL8ys1Mx1EhPrQuboNw3_bp7k6YXWmJ2qV4v6WyFD7fTOXpw9QE72qaZJHQkJxxW6cIZRV7PJdGQ7pg6HUwxcpnVWcOUsSsSaO70-Ikn08jE_MNSXQqFC299u7eAk_WJaMWu6ndd7fOfUmLJVuFwwyY7Fnvs-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو عراق اهو گرفتن بکشن بدن به زائرا
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69297" target="_blank">📅 13:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69296">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37edae9b59.mp4?token=bqTfJfmsGnevR-m0TZYYwm93yGaAjS0yirk1hkmHkJNiJ9z8uMikPoKvQyZNNyCf5In5rpUws4fI_MzDiORskTegCuYaY1ApWNm7TfP0DdFL1oeFhTOUKc5McQUKAMR0FkgGyT5CRQSXYlm35OSq3ILXnh3P-ZRcTP8yxP1IskyzQnK9H8G4oQLWx9Pf4lkgVF4uZDlj4bk9KWRpuK2xhv5bvAnaUw924kLi8MkeQ6v3sBo6agubVOUgl0Zg22NyN5ky3bcxB3Rx47ohgpiJl5_IY_r9618DH9UCymDNmwHBpf-2WB-UHjUdziSH3Jma60pY3p80rCKFQbu19jq_sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37edae9b59.mp4?token=bqTfJfmsGnevR-m0TZYYwm93yGaAjS0yirk1hkmHkJNiJ9z8uMikPoKvQyZNNyCf5In5rpUws4fI_MzDiORskTegCuYaY1ApWNm7TfP0DdFL1oeFhTOUKc5McQUKAMR0FkgGyT5CRQSXYlm35OSq3ILXnh3P-ZRcTP8yxP1IskyzQnK9H8G4oQLWx9Pf4lkgVF4uZDlj4bk9KWRpuK2xhv5bvAnaUw924kLi8MkeQ6v3sBo6agubVOUgl0Zg22NyN5ky3bcxB3Rx47ohgpiJl5_IY_r9618DH9UCymDNmwHBpf-2WB-UHjUdziSH3Jma60pY3p80rCKFQbu19jq_sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
روابط عمومی سپاه پاسداران:
ساعات ابتدایی امروز  ۲ نفتکش متخلف به خیال اینکه میتوانند از مسیر غیراعلامی ما، تحت اسکورت هوایی ارتش کودک‌کش امریکا عبور کنند، بدون توجه به اخطارهای ما، در مسیر ناامن و غیرقانونی حرکت کردند که مورد اصابت قرار گرفته و متوقف شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69296" target="_blank">📅 13:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69294">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WN0bGlbrSHUJyW6kt4JZqOio16tYtgn-N_986P2CLZ6WD8sVzWkvK2cyRKnhU4Hj6GM-VBotYuYhr15GFiC1lTNZIi9YvH-9YMoJpGDiuW-16XhGi0mv9WgCvaPuPHYJvnAcVGBZ7s1K1NYTR1q_BiPNKojfGCc6Af2Eot4sjW-4hZxclMK5p9Q8CUsEuopM_gSNzZm5G_nNxP43APECVIfa85hFycQOGdNUphM1-bZ8gG2gkqjTcErWdFaKJuvQfXlJ0-VYySnjNgw7N6OvmijbESp9MVydmSxKifioA_If50yNbHDIMoutogHnKUtA0N-j_lBE_unl4FrGq6FWCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bb843e99ad.mp4?token=cLT4ZhsYrrh_9AUixZ98SIG6HqdDBdHzSIZe-iC2xm4uqBUgzL8HM6286Hr9c7D8583YDl8dWsklLeVsgjTCWQZ3D4kx3fk5oe1BTy0MtwD8-Iasx-oYSyY46oYM_gceI7h0dgPDsVpDXTHFzQgkFnxKQ3W34NFiA8dEoZGXEXJmj0qLLbLOiFsQcFP3neAsOpJyR6LAGOJqOTN4-Vm2Qr7A0jMGZGAu8VL-Pk5HnFfYD0ejO5mCbd2ZQWJcklG5ExQ3cOsu40UIPOJbTWVLwWlj4aD7k7M_Sk1FBZi72QjgTx5sWiELgqVWScyz4FxfEWBOjI3TS49rzWAnrv13DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bb843e99ad.mp4?token=cLT4ZhsYrrh_9AUixZ98SIG6HqdDBdHzSIZe-iC2xm4uqBUgzL8HM6286Hr9c7D8583YDl8dWsklLeVsgjTCWQZ3D4kx3fk5oe1BTy0MtwD8-Iasx-oYSyY46oYM_gceI7h0dgPDsVpDXTHFzQgkFnxKQ3W34NFiA8dEoZGXEXJmj0qLLbLOiFsQcFP3neAsOpJyR6LAGOJqOTN4-Vm2Qr7A0jMGZGAu8VL-Pk5HnFfYD0ejO5mCbd2ZQWJcklG5ExQ3cOsu40UIPOJbTWVLwWlj4aD7k7M_Sk1FBZi72QjgTx5sWiELgqVWScyz4FxfEWBOjI3TS49rzWAnrv13DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای توی کربلا در حال پخش شربت دیده شده
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69294" target="_blank">📅 12:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69293">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vttN1s0h7TKAf_frPo9ce-a21jC_c17SLTwQhVBG0taJvi4X1AXXDdU3-7jv2V0Pa2vvFJ33B8c51eaxSYE3o1e2bGt08o8TsDbf0iuxubk4wdArABpN7jtouZjVCCuEitB2ifnWAmefH_yqNtzL6mo8kXcwdEvBipLpE-b1swXtbxINLOUdn0VLXnJDg1gZOesVEf-VGp6Ylabxha90o9bJQnELGu-rHqM205RP1IF6RTMRP98Xg86D-dTQuOaoAqtEs8GK--fRUvMKzAYGBKEUxz3ksxyZU7VPU0p0nUZlDhJLsFrFcT1zIEgdzdnswXIW8BszWixdc28NZ-GZvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
گاردین:
یک موشک بالستیک روسی کارخانه تولید پهپاد در کی‌یف را که متعلق به شرکت «ترمینال اتونومی» (Terminal Autonomy) —شرکتی ثبت‌شده در ایالات متحده— بود، منهدم کرد؛ این نخستین حمله شناخته‌شده روسیه به شرکتی با مالکیت آمریکایی در اوکراین محسوب می‌شود.
این کارخانه پهپادهای تهاجمی مجهز به هوش مصنوعی تولید می‌کرد و گزارشی مبنی بر تلفات جانی در این حادثه منتشر نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69293" target="_blank">📅 12:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69292">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1l9Dk0teRffYIOrRzaJyBf6438qW_BiOznbkjB7lzPaWG3YHEVcTXVW3tTvzgO5VS0c470NKQoHW9mOCXVVbe5vlxI2JUydgl1Dx8TAA0wLtTkvSr8c_1y7F3OVIlIV03HZIyVOtHV46AMV2izfitqEGQaN3p1iLyaTZyNXAd_zGsVzFF50HTy53Hxl8sP-023u2TuRZ1HvAXE0eOv0dQ0K757FntZdiiu6bDhiYEX2kBpgYW8uuPQ3oAwUm9abjSpLYDBzhRFWtaQpRWWEaA30YdAn1r-0vBPEAm5Ovxi9dlHlov6pGYrIDJTANR_pgJvcdgxcWHgkSlB1A4DUmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
به گفته یک منبع آگاه، مقامات سپاه پاسداران از هیئت حماس که برای مراسم خاکسپاری علی خامنه‌ای، رهبر عالی پیشین، به ایران سفر کرده بود، خواستند که در امضای توافق‌نامه عجله نکنند و وقت بخرند.
یک مقام ارشد آمریکایی مدعی شد که ایران تلاش کرد حماس را متقاعد کند تا این توافق را امضا نکند، اما این گروه تصمیم گرفت به این توصیه عمل نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69292" target="_blank">📅 11:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69291">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a885a777d.mp4?token=ZTA2Kl_PpAGlJt07e-k2ncDGaF4RTlqX-YsW5pAUuYP7o9acbJnRqKpsUykxbPBOwz23SmP-gbFs-Jg7fLVjd3Ug4wsR1uzUmcjVueV2UQ3VL6y0TYzxkF7LfW0hgBnN-mzIlgXVazV0ni6JA7eMVdbrCo9wkKS_DTJLrOmUpOZ6z-kh8wH5lAWVrmVRxQb6GmvFo2dtaJABA1ywmX1Do9-QtkXgQAyhmVbCV6-9Pl6OH09vu5wjBMdZ2Ha5uOXJuF_QthiuKrmql9JICP4YAO94oDJLBvLS0-qXkUtAPWTvHS0u0t_QZeRgzXK8XG091QMuSDjlQ8JMvD-Yqm4mzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a885a777d.mp4?token=ZTA2Kl_PpAGlJt07e-k2ncDGaF4RTlqX-YsW5pAUuYP7o9acbJnRqKpsUykxbPBOwz23SmP-gbFs-Jg7fLVjd3Ug4wsR1uzUmcjVueV2UQ3VL6y0TYzxkF7LfW0hgBnN-mzIlgXVazV0ni6JA7eMVdbrCo9wkKS_DTJLrOmUpOZ6z-kh8wH5lAWVrmVRxQb6GmvFo2dtaJABA1ywmX1Do9-QtkXgQAyhmVbCV6-9Pl6OH09vu5wjBMdZ2Ha5uOXJuF_QthiuKrmql9JICP4YAO94oDJLBvLS0-qXkUtAPWTvHS0u0t_QZeRgzXK8XG091QMuSDjlQ8JMvD-Yqm4mzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدئو وایرال شده از یکی از مراسمات عجیب آفریقایی ها که با شمشیر همدیگه رو میزنن
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69291" target="_blank">📅 11:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69290">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBNu6-r1vNZT0xopJwSvuwU3GNhfoJslOgjozCwj-hMH06B3b0sAmdX4h4LRs4y0ppL0OXQ37cjN6FKea9Gv5lp-sBxr-qrCOYjsO8Mz80PeRoL4gRfSB1jMT2C3HmORTz0u0VlbYfkNPykIqqiUAQZPzCMHmSRrIXG5-pbj3lDViuSQsRWunoAe45_77GNwWxrBjsSqKuS32ZgvyPMbEz0B0TLJ1nty_4FmoDgS4h32DYM1irfAmdzwiAhFCUGJ-GKfFei4Axgbh7FkhT6F5ECOMgXJMz_evk2bsIxjMcwqHZlsj0r_MAaLfE1Mppc5BkL9crcizFLONKewo0XVVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇱
🇮🇷
تایمز:سازمان سیا و موساد اسرائیل در حال تشدید جستجوی خود برای یافتن آیت‌الله مجتبی خامنه‌ای، رهبر جدید ایران، هستند که از زمان جانشینی پدرش پس از حمله هوایی فوریه ۲۰۲۶، در ملاء عام دیده نشده است.
مقامات اطلاعاتی معتقدند که او در این حمله به شدت مجروح شده است، بیش از ۱۵۰ روز از استفاده از تلفن یا لپ‌تاپ خودداری کرده و در یک پناهگاه زیرزمینی به شدت محافظت‌شده، احتمالاً در تهران یا نزدیک قم، پنهان شده است.
با توجه به اینکه نظارت الکترونیکی سرنخ‌های کمی به دست می‌دهد، جستجو از اطلاعات سایبری به اطلاعات انسانی تغییر یافته است.
مقامات سابق موساد می‌گویند که اعتقاد بر این است که مجتبی از طریق چندین لایه پیک ناخواسته که پیام‌های دست‌نویس حمل می‌کنند، ارتباط برقرار می‌کند و نفوذ به حلقه داخلی او تنها راه واقع‌بینانه برای تأیید موقعیت مکانی او - یا حتی اینکه آیا هنوز زنده است یا خیر - است.
برخی از چهره‌های اطلاعاتی گمان می‌کنند که سپاه پاسداران ممکن است مرگ او را پنهان کند، در حالی که برخی دیگر هشدار می‌دهند که رژیم ممکن است از بدل‌ها برای پنهان کردن حرکات او استفاده کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69290" target="_blank">📅 10:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69289">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9be197f29.mp4?token=YyfY5dOrpDmFo6egl7iewx10BkggLcvTYaAJlcGDiZHFY_D05NX5YOJInpftv9nkRoE0XNKn9Y__DEm4mHu1T9Fc1PqNYvbkuOFtDNlefFkTdexUb0VH_Q-1EH415BiCfRaiBJmIvTa5X6jIEuca86Z-jTP0Ui1XrieSm0i0DK6PLvlA1m3davRmGM1OuK8QLJfW3lKtIUWpmHAgDvF44tXLblGmgMF8KdF8-ylwCbNnsItaecymZ_rXsnXpmLgOMDnWOVC9fNGMlc6hANeWdDvDVkvFsZhcYM9XPzFzV4t_UTblLMDxEa5Nk_6Y_jwzYlPKnjbsWhzs4JAK3qABXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9be197f29.mp4?token=YyfY5dOrpDmFo6egl7iewx10BkggLcvTYaAJlcGDiZHFY_D05NX5YOJInpftv9nkRoE0XNKn9Y__DEm4mHu1T9Fc1PqNYvbkuOFtDNlefFkTdexUb0VH_Q-1EH415BiCfRaiBJmIvTa5X6jIEuca86Z-jTP0Ui1XrieSm0i0DK6PLvlA1m3davRmGM1OuK8QLJfW3lKtIUWpmHAgDvF44tXLblGmgMF8KdF8-ylwCbNnsItaecymZ_rXsnXpmLgOMDnWOVC9fNGMlc6hANeWdDvDVkvFsZhcYM9XPzFzV4t_UTblLMDxEa5Nk_6Y_jwzYlPKnjbsWhzs4JAK3qABXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از حمله عجیب طرفداران حکومت به بنر ترامپ و نتانیاهو
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69289" target="_blank">📅 09:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69288">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‼️
دلایل سقوط شوروی که صداوسیما پخش کرد در مقایسه با وضعیت الان ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69288" target="_blank">📅 09:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69287">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/418bb6362d.mp4?token=drDi35fRLUsZ1fnsGfZvdxLIv1W8RYUvuFRIIccdPytYsbAPX-gF8WdaNIcbE3NWUpyWVUgrO-PW6pGgkV5cuH_gIxmHc1AbxwCCjDaVzxv1XnqHOC8EaiNIpV_Z7C6VBmiWDiFPU-EQvCwQw_EXbXJIgW6HWDfrfJlK6S7PdDkQo-ZqHuHICiG4JC56SedRxTRg0-WUFMHNDAaJMyTfKtsO5NjBWzOz-Nb7JINv8aEZPIV2c7gDjWCPW3tik45WG7A7VQEz2j5HG1QuyBYAfjbDc3BBogc5PPI7RNPUGX81zDRJqADpdDUI8TkwnfVr9wNffMRml01C216ic-0Qlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/418bb6362d.mp4?token=drDi35fRLUsZ1fnsGfZvdxLIv1W8RYUvuFRIIccdPytYsbAPX-gF8WdaNIcbE3NWUpyWVUgrO-PW6pGgkV5cuH_gIxmHc1AbxwCCjDaVzxv1XnqHOC8EaiNIpV_Z7C6VBmiWDiFPU-EQvCwQw_EXbXJIgW6HWDfrfJlK6S7PdDkQo-ZqHuHICiG4JC56SedRxTRg0-WUFMHNDAaJMyTfKtsO5NjBWzOz-Nb7JINv8aEZPIV2c7gDjWCPW3tik45WG7A7VQEz2j5HG1QuyBYAfjbDc3BBogc5PPI7RNPUGX81zDRJqADpdDUI8TkwnfVr9wNffMRml01C216ic-0Qlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خبرنگار :
کشور های منطقه که مورد حمله ایران گرفتن آیا باهاتون تماس گرفتن و ارتباط گرفتن ؟؟
🇮🇱
نتانیاهو:
بیشتر از چیزی که فکر میکنی و بیشتر از چیزی که میتونم بگم اتفاق افتاده
.
⏺
خبرنگار:
هدفتون درباره حکومت چیه
.
🇮🇱
نتانیاهو:
خب هدف مشترک من و پرزیدنت ترامپ مشخصه اگه بتونیم تهدید ایران به طور جدی کاهش دهیم توافق های صلح زیادی انجام میشه
!
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69287" target="_blank">📅 02:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69286">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrpEpy89ylGlEspXl2ZVkF_yoPMf9mv-tC5kXTlVZosAP3cFI8tHCjqchhwlFN3rzx9Mbds2_L5WUlBiuaNiCNrRvaFwfaWJB4uEcVhJ-PJhOlOHa_LBfZRRXvAKTs7QUPWW283OEZGssQcHS-DdGc9XvbyQKfiBdIAzB8v76LorqvKBFwm_8gYZofhuUYVbkE35ZTFnhNvQcAk7q22tffVHYOEaw8HWQ-px_unHkSc_cvyY71N1Bd-zka3t8OIScOZysBz3V1FTwcy1dQgaMihNyqIHX4MRmkrJbYIKKFv02Z-hGfTNau8w0dfkaX7Pghau86QOdT-0oi_JCQSvww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
امروز، «شورای صلح» به توافقی تاریخی برای خلع سلاح کامل حماس و تمامی دیگر گروه‌های مسلح در غزه دست یافت. این گامی عظیم به سوی صلح و امنیت پایدار است.
این توافق گامی حیاتی است تا غزه سرانجام تحت اداره یک دولت جدید فلسطینی قرار گیرد؛ دولتی که برای یاری رساندن به مردم فلسطین، همکاری نزدیکی با «شورای صلح» خواهد داشت. هم‌زمان، اسرائیل از امنیتی که شایسته آن است برخوردار خواهد شد و غزه دیگر به پایگاهی برای حملات تروریستی بدل نخواهد گشت.
این رویداد، نقطه عطفی بزرگ در اجرای «طرح ۲۰ ماده‌ای ترامپ» محسوب می‌شود. این توافق طی مراحلی با برنامه‌ریزی دقیق اجرا خواهد شد. هم‌زمان با تکمیل روند خلع سلاح، نیروهای اسرائیلی عقب‌نشینی خواهند کرد و «نیروی بین‌المللی ثبات‌بخش» با همکاری نیروی پلیس جدید فلسطین، مسئولیت تأمین امنیت غزه را برای ساکنان آن و همسایگانش بر عهده خواهد گرفت.
یک سال پیش، شاهد جنگی شدید و خونین، بحرانی انسانی و نگهداری گروگان‌ها در شرایط اسارتی بی‌رحمانه بودیم. ما به پیشرفت‌های تاریخی دست یافته‌ایم، هرچند هنوز کارهای بسیاری در پیش است.
می‌خواهم از میانجی‌ها — مصر، قطر و ترکیه — به خاطر تلاش‌های مهمشان و به‌ویژه از تیم فوق‌العاده‌ام که با تلاش‌های خستگی‌ناپذیر خود دستیابی به این موفقیت تاریخی را ممکن ساختند، تشکر کنم.
اجازه داده نخواهد شد تهدیدی که در ۷ اکتبر از سوی غزه سر برآورد، دوباره بازسازی شود!
بر اساس این توافق، غزه سرانجام در اختیار دولت جدید فلسطینی قرار خواهد گرفت که در خدمت مردم خود است.
این دستاورد شگفت‌انگیز را — که همگان دستیابی به آن را غیرممکن می‌دانستند — به همه تبریک می‌گویم!
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69286" target="_blank">📅 02:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69284">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGUn5v1VkJXbjS8hlflw4WDgDsSQMLxGfyT4zYMKSmSzAXhgIfrxbQGm4bM_XCerCsfcMgf89i-cZpsalpPVc9D_1wC_KeQI0VSTXHLwhYR3ZHeLmpp1eIjSYhonEFU6xKmepB-7Am-lcJfd_51OAAWNeVK_-EBWIPr5IZWHVZKlBcR-qMGTLHsl2udbWbexGZcFq1tgxSEWM2C4lHMSVIlxFN2DOO6C-nQR27eP7mEzyTSmZfLAu2gx1oCEDprpyenujFklMUS6-R5H3huKSjfugmJI2nvmBftwY9GeUOaS851bf9UQjxrYluDMUWpYliXgiA2zmxqNHL3rKKf0KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=UqdxEBHUwIbaM9aBbG8IWvgUjiTnmaaA040H1foovjejX-hThb4OG7TnM21CaAiH4-3Z01LBR19stOtDdI2h8JXyGyqMQ53_GIkk5JweKwB11CERumPcwZ_XgSe_j2xcNTqD79IXHXHtG_nxIZtcixvJoyA7Sm9eKUxK6Sf3XEb1tt5Mjx80hbt3KQcmp0ScJIBVxFsVjTAgCnFB7RIG3cx3V76tT9X_CscgSBHjbdQ-coPj6zohQbfNCJ73kAsLz2SOn6qL9KbIJYYPrIpxe9hrekuGhKYHzpeYd5UIFzW1isUzGRCap7HGykK0uQMZEvS8iCRNzzLz5iLIuREoLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=UqdxEBHUwIbaM9aBbG8IWvgUjiTnmaaA040H1foovjejX-hThb4OG7TnM21CaAiH4-3Z01LBR19stOtDdI2h8JXyGyqMQ53_GIkk5JweKwB11CERumPcwZ_XgSe_j2xcNTqD79IXHXHtG_nxIZtcixvJoyA7Sm9eKUxK6Sf3XEb1tt5Mjx80hbt3KQcmp0ScJIBVxFsVjTAgCnFB7RIG3cx3V76tT9X_CscgSBHjbdQ-coPj6zohQbfNCJ73kAsLz2SOn6qL9KbIJYYPrIpxe9hrekuGhKYHzpeYd5UIFzW1isUzGRCap7HGykK0uQMZEvS8iCRNzzLz5iLIuREoLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیدار عجیب نتانیاهو با یک سناتور!
امروز نتانیاهو با جان فترمن دیدار کرد و طرف با شرتک نشیته بود و سرش کلا تو گوشی بود
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69284" target="_blank">📅 01:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69283">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">عجب سکوتیه، موشکی راکتی چیزی نداریم؟
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69283" target="_blank">📅 01:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69282">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromلیوه</strong></div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69282" target="_blank">📅 01:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69281">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">عجب سکوتیه، موشکی راکتی چیزی نداریم؟
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69281" target="_blank">📅 01:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69280">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">▶️
تیزر جدیدی از سینمایی Spider-Man: Brand New Day منتشر شده که دیدنش خالی از لطف نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69280" target="_blank">📅 01:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69279">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apwnlEu1_j8HaNH08LTWhG4RI-XGOtzmgQt1rNPAwLjMUk9CnPBxm5YtEo3AAnV2N1mfK9MFMbZxF6pkSJpFtDTkvqWctf-I22ZkS16iazP_xCIkVlY-70Cl_NPcDqsBClqylc1OTDxdKInr4le3ikW8GpARpZH6wXAEw8IAUiPljfYuAx-x52wgLdLmBT6OZBL919mY5E-1C8PRuMYh_Yc-k950djpo0r7oqGbAsROfcF1ezUCfDaOXvuTZ7B0hE_Qh-3BLJBQ1OI9qw9CzJpZm-X8TYEgNC0k1gwYtKmfGGtety0mXNUN3J3UClG5jhwHWMXBQmsCQhH0OjjYwQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
«آمریکا هر روز یه جنایت جدید انجام میده. حمله به خونه‌های مردم عادی توی جزیره قشم، ادامه همون جنایت‌هاییه که قبلاً توی لبنان و غزه انجام داده.
آمریکایی‌ها عادت دارن هر وقت توی میدان نبرد کم میارن، با ریختن خون آدم‌های بی‌گناه جبرانش کنن.
ولی بابت این کارشون، تاوان پس میدن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69279" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69278">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba260d124.mp4?token=AP0UV5ViNCAVYCCVUOayEllxnMfWnneAoDMcVNrZ-HpollezI67TLHx7p1yXqjGJoy2SmK5NzVtV4wzbvQ31O71ROTo8op_P74BeDcmXudZWSx_hArlVm3YGxi-psVLcr5tHmVI63LtoGAMZHPARSbynPz5USpMpEdC6nms-mvZIcypROZ0sL3zAgrZDKUgoNw9Dc_r2a8IlRFUG6ksDRFPbVBP5BSHoDHDL5BbTV2_8v8qSyZrgaFaRsEMDoA8AeAYyL1TlryF3Tll4iFLOgT1_DnH-GTUnDSSlE-fGeE7uQG958e8lvqWcNRwgTIh8B0S7HmwW-H7mFoZNzKouiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba260d124.mp4?token=AP0UV5ViNCAVYCCVUOayEllxnMfWnneAoDMcVNrZ-HpollezI67TLHx7p1yXqjGJoy2SmK5NzVtV4wzbvQ31O71ROTo8op_P74BeDcmXudZWSx_hArlVm3YGxi-psVLcr5tHmVI63LtoGAMZHPARSbynPz5USpMpEdC6nms-mvZIcypROZ0sL3zAgrZDKUgoNw9Dc_r2a8IlRFUG6ksDRFPbVBP5BSHoDHDL5BbTV2_8v8qSyZrgaFaRsEMDoA8AeAYyL1TlryF3Tll4iFLOgT1_DnH-GTUnDSSlE-fGeE7uQG958e8lvqWcNRwgTIh8B0S7HmwW-H7mFoZNzKouiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سنتکام:
یک فروند هواپیمای P-8 Poseidon(هواپیمای شناسایی تخصصی) نیروی دریایی ایالات متحده در حین گشت‌زنی در خاورمیانه، برای سوخت‌گیری به یک فروند هواپیمای KC-135 Stratotanker نیروی هوایی ایالات متحده نزدیک می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69278" target="_blank">📅 00:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69277">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLMKkZns0LC9yOYztZa2VCyyLnmPTttlaEvCMkDNVxvlxxyiSKMrwGYB8uyuXWMhj3bkoLT1NV26XwwvwGyw_9nGD1ReeMQ_Yehs9bBX4OGtvusEkOVQJ4j6YuypMoXQLd65USn5fDUozGuwAn5MVJ9klgJhc2N5qsSYfLpGmCYLAVVrVlu2_82rQ-Xzl3n7Ex7B9ZpndiyUL_ndIQNZnAS6d3j7WD6cQSKOdisogMyGNI6cy5uzPpEcZ2SXIdqQ0GlRypOmEkw_KlYoiblY2Pz8imJXSP3SrH3SVWrzPhMVNykW-Yr-dkd4prXi36l_N9VctQYdZeAkYQpZGDVnjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آی‌24نیوز:
اسرائیل کاتس، وزیر دفاع اسرائیل، روز پنج‌شنبه به همراه ایال زامیر، رئیس ستاد کل ارتش، جلسه‌ای برای ارزیابی وضعیت امنیتی برگزار کرد.
در این جلسه، تصویری از وضعیت اطلاعاتی و عملیاتی، سطح آمادگی ارتش و طرح‌های عملیاتی برای سناریوهای گوناگون در عرصه‌های مختلف به کاتس ارائه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69277" target="_blank">📅 23:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69276">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89da715482.mp4?token=KR36KgQ5F8AQYbgAWPsqo2CyMxx1EJOwIrxg_OAO2X4TdaouMNH6_8vb_tZr-pfgmUb2fQJCkf_ucjl4_FcqF3t64R3eKTdSdT7eJsJ2EeV_SQ9VgasO0kqAS0ZFr1q1EyPUEy6nhlp8jP0nmwPnApx05-kypD4kSoLo0_oeJLImduhY2-tio-hB7_Vuyxluo6-KJfGNAPtFUeTeXrJ3qS7oqhjfcER_zwe7EAESFq0bA8aRmDvDgEKZbiGUagOACmFxIjmrOuGNZXuL9sqoyhdU2AhqbP5jLOFkV0uv_ni4pcSfZggvUbgdoha9rDhZYojEovrvSPGu6g-U4VK7nw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89da715482.mp4?token=KR36KgQ5F8AQYbgAWPsqo2CyMxx1EJOwIrxg_OAO2X4TdaouMNH6_8vb_tZr-pfgmUb2fQJCkf_ucjl4_FcqF3t64R3eKTdSdT7eJsJ2EeV_SQ9VgasO0kqAS0ZFr1q1EyPUEy6nhlp8jP0nmwPnApx05-kypD4kSoLo0_oeJLImduhY2-tio-hB7_Vuyxluo6-KJfGNAPtFUeTeXrJ3qS7oqhjfcER_zwe7EAESFq0bA8aRmDvDgEKZbiGUagOACmFxIjmrOuGNZXuL9sqoyhdU2AhqbP5jLOFkV0uv_ni4pcSfZggvUbgdoha9rDhZYojEovrvSPGu6g-U4VK7nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند روز پیش یه پسر بچه به اسم امیرحسین رو آورده بودن صداوسیما که اینجوری جواب سوال مجریا رو داد
:
مجری:
منو عروسیت دعوت میکنی؟
امیرحسین:
معلومه که نه
مجری:
کارشناس برنامه، خانم دکتر رو چی؟
امیرحسین:
فرقی نداره، اونم نه.
مجری:
مامانت چی؟ اونو که دیگه دعوت میکنی؟
امیرحسین:
وقتی زن بگیرم مامانمو میخوام چیکار
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69276" target="_blank">📅 23:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69275">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671ccf87ea.mp4?token=a18lnevPwwJOfnm0CKjUuR-PEnAwv-uZpqD_xiNHlLmP8uhXxvGmX729W7kmurqesnqowLkRVUrc8Jg_jsEX3GhXdZTQc2AQC9p8zqF8mdou2wCxQw69ihTE10Ggzh7AN6nHi7m6U0VlWMEvbVm3OhXEalLzDNAaheyCwHY9z82YRJEDN6MnL6eHUrGZ9BmCUi4six9YcYJaimmssjhCN3a1eHUvXl3uZwgul_5ss-HzcJ8QcR8_Ygt5vfyxpkxtNcZ9wvWIvPLA2YlDBMFDMAwxHcTBpoJ2jyXurjFIbp4MZnNq0_MI7LfhCChupkMsvmhqYH0F3ya2tkBUF6se7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671ccf87ea.mp4?token=a18lnevPwwJOfnm0CKjUuR-PEnAwv-uZpqD_xiNHlLmP8uhXxvGmX729W7kmurqesnqowLkRVUrc8Jg_jsEX3GhXdZTQc2AQC9p8zqF8mdou2wCxQw69ihTE10Ggzh7AN6nHi7m6U0VlWMEvbVm3OhXEalLzDNAaheyCwHY9z82YRJEDN6MnL6eHUrGZ9BmCUi4six9YcYJaimmssjhCN3a1eHUvXl3uZwgul_5ss-HzcJ8QcR8_Ygt5vfyxpkxtNcZ9wvWIvPLA2YlDBMFDMAwxHcTBpoJ2jyXurjFIbp4MZnNq0_MI7LfhCChupkMsvmhqYH0F3ya2tkBUF6se7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نقدعلی، نماینده مجلس:
با وضعیت حجاب میخوایم چیکار کنیم؟ والله جوابی برای خدا نداریم.
یه نماینده مجلس به من گفت از درد بی‌حجابی هر شب تو خونه گریه میکنه و خواب و خوراک نداره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69275" target="_blank">📅 23:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69274">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vY-E6oYEkHGAGBzOvLZfriS-THLsLljfcmPoNcw_sZCK5YDUP2htaIdEEtVgFF8vs9fbPIIQulLYfQ_2LBOfW1Q4teJQ0JFJmFpAvwsLotdf4dOwfhZrpY3QngG4H5QLFcyjVedSNaFqT4C7IZqgXYTOb-bHvqPuGJBNKVo3EZB8JvTpu91d2cdAYlXq6H5IpZuYXcv6UHdM9PRgea7uAt8pMgmCKvBTZX9kMMimXHLXJfmi6GJid6JeA915OMdr7UF6iYW-bN7B7Pa8nmmOQpyYcGHMtHTS4yc_hX1dTOqiTLYYgP3gxeAZhBhof8nPlt4KYv5c-Ph5z03s7ZP3aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعدام می‌کنید؟ به‌به چه کتلت های تر و تازه‌ای داریم امشب  #hjAly</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69274" target="_blank">📅 23:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69273">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3fe31b5c.mp4?token=ESpWshazxF0XtRX3D4ET_Y-o6KnPRpcblGphqvzGUvhVN2e0a3hyw6txk6Yc4H-NoCM4R2K599BaWxao6rhwASaBN3xq9h_IgwQXVbUguG0DFSFUuHJreeBCQOFMy3arFEkSqqelQrVrVDpPq4hpchb8gYCqfjyhnb5rZqmq6nbv2H9RACbkxnRoAz59YMLc_HO1v4IwFyKM8Y_KKPenrgcfcMlcb0txcnM-5HZpoGu4BYUtF1RPbhq2R69azTShVEb3hKiIBx5uvP_AsvRXFUIB6Ozc6k5ouXNwSeYGSY8XZ-5WG36NSjYBSl8Fwp-wslz5waa4yEoY9BRSSR7ZhgtZL5kB_r_xTdW40yC7gtZX-hqJIfJFaUhl4tcAcx_pdytsPoJkYfzlu_wumnSu-c-8wpNQ1kiyXMzs3b8IrabsTV6qse-_31RrQtCGzwY5z2PylO9-c1vcKOR2cCOpwA6BhfQMjsldqF_IrNpr-brHQuHyvRLEr8YmKqeq6IJ103OACYbYv5O7hAZlm2pMpQ30fuvgp49d5NB9L3ECUj-lJsj01Fu8UKUDvRIjxWECbmSz00_EXViOY_5AVuO75UAB-CP74FkOZXzmKOiwR8mA--kadCi0kQnR07K6Rss2ULg-UlVteQ8qm7cuB6SxLmyYslawhRGtdeJnQfek6OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3fe31b5c.mp4?token=ESpWshazxF0XtRX3D4ET_Y-o6KnPRpcblGphqvzGUvhVN2e0a3hyw6txk6Yc4H-NoCM4R2K599BaWxao6rhwASaBN3xq9h_IgwQXVbUguG0DFSFUuHJreeBCQOFMy3arFEkSqqelQrVrVDpPq4hpchb8gYCqfjyhnb5rZqmq6nbv2H9RACbkxnRoAz59YMLc_HO1v4IwFyKM8Y_KKPenrgcfcMlcb0txcnM-5HZpoGu4BYUtF1RPbhq2R69azTShVEb3hKiIBx5uvP_AsvRXFUIB6Ozc6k5ouXNwSeYGSY8XZ-5WG36NSjYBSl8Fwp-wslz5waa4yEoY9BRSSR7ZhgtZL5kB_r_xTdW40yC7gtZX-hqJIfJFaUhl4tcAcx_pdytsPoJkYfzlu_wumnSu-c-8wpNQ1kiyXMzs3b8IrabsTV6qse-_31RrQtCGzwY5z2PylO9-c1vcKOR2cCOpwA6BhfQMjsldqF_IrNpr-brHQuHyvRLEr8YmKqeq6IJ103OACYbYv5O7hAZlm2pMpQ30fuvgp49d5NB9L3ECUj-lJsj01Fu8UKUDvRIjxWECbmSz00_EXViOY_5AVuO75UAB-CP74FkOZXzmKOiwR8mA--kadCi0kQnR07K6Rss2ULg-UlVteQ8qm7cuB6SxLmyYslawhRGtdeJnQfek6OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کویتی‌پور، معروف‌ترین مداح دوران جنگ ایران و عراق، دیگه حتی مداحی گوش نمیده
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/69273" target="_blank">📅 22:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69272">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUUGCgU_E_WnluYVPuuGoazoPbQMj2gWpBU4GWRwoayTxLXu6R9EaLizp-DJkRneTu2D6ZdXBcZUwpU4di1QRkIac6p7NQewFatlVPB0tFj3-motIFP_EsiUL7JpvfP20eNA7qfbo5Kc9ISrdomlenpOXhZyCTC8f5UOKzd5zIwkpzfHTqbZWpaEC_gXOaZnDC4ZbGJaN9EhRN2--51oY0l9c5UTIfrlCj_CNQjRDOLwKUINbu_KZJI23M5vlPjtpm4-mp7zeBelqb_fw_9YoGViEjKkrnjBVOXMB67N_HLiy19URyqrJF9ZdBOAvkuJXRYsuVNQy51fdSl1uQMS5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😄
مالک تلگرام ، پاول دورف :  روسیه به‌دلیل اینکه حاضر نشدم خواسته‌هایش برای نظارت گسترده و سانسور در تلگرام را بپذیرم، مرا در فهرست «تروریست‌ها» قرار داده است. طبق قوانین روسیه، من از «انتشار هرگونه اطلاعات در اینترنت» منع شده‌ام.  ظاهراً مقام‌های روسیه هنوز…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69272" target="_blank">📅 21:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69271">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FHbLwGUZmzAVldtGtRIfv6Bgj-ywp9_4akcCNcWxRW9rYalBoXSJ603-ju2Ktdqtl8wRZHpTTtyGEuI3iaxVlcMmPHLYLVBvh0aVVVpSUggX6XF3fjserNVixY9Tu6siCDfUFykb07WgiA_NJ1bmMwIvQlWp4E-W03Px04NH4F7pa3F7qADRM5IlQPRV7XfVHxD5cplGclK717OrT-TgQAZao6OOwFVAJ06djTpdOJNxQOYR2nyVevWEdzRLxWm1JgWIxQLpu3XYsFnU5ksELIkvbkYE07n21nwATd0V2cPQHAMdWzcYu5ZNPZM2FQsmXq0SxM5oT5BBfkB7Sgmb1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😄
مالک تلگرام ، پاول دورف :
روسیه به‌دلیل اینکه حاضر نشدم خواسته‌هایش برای نظارت گسترده و سانسور در تلگرام را بپذیرم، مرا در فهرست «تروریست‌ها» قرار داده است.
طبق قوانین روسیه، من از «انتشار هرگونه اطلاعات در اینترنت» منع شده‌ام.
ظاهراً مقام‌های روسیه هنوز نمی‌دانند که چه کسی می‌تواند چه کسی را از اینترنت محروم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69271" target="_blank">📅 21:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69270">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7ad22e432.mp4?token=jDEGDigWN8BESjgCAVPK09vxt7wNYNwOdYNJgtw_i_rU2bVmuteZ69J0QIrcJ-oUNWafU9hJs3nGDyXDPtVEKDrTlVD46g2xjDJqpLpH-ryjGK9w5CoWQ0RLvLHPxTYiZI1vLfJEzJ0ioUZF_ECA8JhbHA2XAoOWcYzRZU_fCgyyTTUDJZ5HLLmatWQBiwyvR_dX_kx9KW0gVFCjwPITPKQ1X4Quqz3GWydYBsu9hGyb-VsyHOSg72cgxfrGOqpea7QZvLJedXVxX93RbbnsMlxDdJ3CmKISBjx7RxYnyAFbapg2xYo7HpBtDkgIuLcJZEUgl2XCXl-1DvTAuP-WxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7ad22e432.mp4?token=jDEGDigWN8BESjgCAVPK09vxt7wNYNwOdYNJgtw_i_rU2bVmuteZ69J0QIrcJ-oUNWafU9hJs3nGDyXDPtVEKDrTlVD46g2xjDJqpLpH-ryjGK9w5CoWQ0RLvLHPxTYiZI1vLfJEzJ0ioUZF_ECA8JhbHA2XAoOWcYzRZU_fCgyyTTUDJZ5HLLmatWQBiwyvR_dX_kx9KW0gVFCjwPITPKQ1X4Quqz3GWydYBsu9hGyb-VsyHOSg72cgxfrGOqpea7QZvLJedXVxX93RbbnsMlxDdJ3CmKISBjx7RxYnyAFbapg2xYo7HpBtDkgIuLcJZEUgl2XCXl-1DvTAuP-WxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔝
سنای آمریکا به طرح قطعنامه‌ای برای توقف عملیات نظامی علیه ایران، مگر با کسب مجوز از کنگره، رأی منفی داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69270" target="_blank">📅 21:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69269">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64cd6ef9d4.mp4?token=GCyAFbeKA3Xt8VQNGR-L4KQh_biRxUrjd_ZYh8PEKcmsdTv_YnUVdKfNqKY3kTGL8E7iv0IRgoRcY9pW0wXeUf6ApsF3ozCxY9V8kJTFC4aWYHnIAK78Oir5ek3ddg8nCp5vA2BIf7D9lPtycdwJ8CJoU5nuIL0dbATv-xmQFf-uO_wx0CXhgoUQZS45wNJLlnHX_WHGXY-Od_WOtVE4tPsnlZZb2ZifSF2zcZGPrzlYBt49vIZ4i3sMSemS2B8GppHe8uEvlUIdMOT2gUJt62nHDjegY7JElt4u-MzDghpSJ7LXcWPF9KVDYSgonuCJnQceX3TJ0nZHVoXGKuqOQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64cd6ef9d4.mp4?token=GCyAFbeKA3Xt8VQNGR-L4KQh_biRxUrjd_ZYh8PEKcmsdTv_YnUVdKfNqKY3kTGL8E7iv0IRgoRcY9pW0wXeUf6ApsF3ozCxY9V8kJTFC4aWYHnIAK78Oir5ek3ddg8nCp5vA2BIf7D9lPtycdwJ8CJoU5nuIL0dbATv-xmQFf-uO_wx0CXhgoUQZS45wNJLlnHX_WHGXY-Od_WOtVE4tPsnlZZb2ZifSF2zcZGPrzlYBt49vIZ4i3sMSemS2B8GppHe8uEvlUIdMOT2gUJt62nHDjegY7JElt4u-MzDghpSJ7LXcWPF9KVDYSgonuCJnQceX3TJ0nZHVoXGKuqOQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📚
عمران عباسی، عضو کمیسیون آموزش مجلس
:
قطعا تو مهرماه باز شدن مدارس رو نخواهیم داشت.
چون برگزاری آزمون‌ها تقریبا یک ماه تاخیر داشته.
حالا همه تلاش‌مون رو می‌کنیم که اول آبان یا تو خودِ آبان ماه مدارس رو باز کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69269" target="_blank">📅 20:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69268">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dca29ad7e.mp4?token=D4lB0mlf_1NPRo7XNPgZsP_5rIXYXyaqMPLqRQkXwykO2M6wMcUCVQaUkUvPPwKTM_f7Rd3ImpfdOpRN9Ssenobn7em2utlEkXS5cEAf6SdBJC7eHGAowJbOaO2nSwdxiAaSP8zzmO08P4_hfumillQhawuO7FRC8r356U6SbF3b9ul8hDcsYEJ_CjVhNK3Q2AbQscDjt4L0fUS52Lnrich6O2xwS8G73MbKHLY9qg2dWGgUzG17i0WQMbiSxxR1WJvBgoXwHCEsCUeuu00MhS07lZNBaDQRVHk5XC07JQ-VLHoF8y1Ktitdd3blcXu381OaIcGLSoSoOKy07c7l7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dca29ad7e.mp4?token=D4lB0mlf_1NPRo7XNPgZsP_5rIXYXyaqMPLqRQkXwykO2M6wMcUCVQaUkUvPPwKTM_f7Rd3ImpfdOpRN9Ssenobn7em2utlEkXS5cEAf6SdBJC7eHGAowJbOaO2nSwdxiAaSP8zzmO08P4_hfumillQhawuO7FRC8r356U6SbF3b9ul8hDcsYEJ_CjVhNK3Q2AbQscDjt4L0fUS52Lnrich6O2xwS8G73MbKHLY9qg2dWGgUzG17i0WQMbiSxxR1WJvBgoXwHCEsCUeuu00MhS07lZNBaDQRVHk5XC07JQ-VLHoF8y1Ktitdd3blcXu381OaIcGLSoSoOKy07c7l7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
حکومت از امروز یه طرحی رو شروع کرده که بتونه فضای مجازی رو به صورت کامل به دست بگیره؛
طبق این طرح؛ قراره بلاگرها، اینفلوئنسرها و بقیه فعالای فضای مجازی ثبت و ساماندهی بشن.
در عوض می‌تونن از مزایایی مثل بیمه استفاده کنن، اما از اون طرف هم قراره نظارت روی محتوایی که منتشر می‌کنن بیشتر بشه و هر کسی خارج از چارچوب قوانین جمهوری اسلامی فعالیت کنه، صفحش بسته و با برخورد قانونی روبه‌رو میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69268" target="_blank">📅 20:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69267">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46911d7dc4.mp4?token=Ci4cl5V2nGPn8CY-xgwZix_rZCizF2-CWJf5e1nRlOesrkXwAy2bDEhpQDTldgs3N4oEvnfsAbre8k3pqVNLjRqvvHO3iw1cm7aIMuBtJNmM_VGyS8HWPZeaFPJYlsAgEOHiCd8UgKhoTRkMdarB8wAjCF3KMz1Ry9tqxk1yiCQfsQSCWrDRfyyA-JJOI6eYtOpo-7UQ4Qo369bnQ9WkZmdu9Pq0jNB-OtKgiFVxcTxQHlGcd7T6mYUYClWIOOfV5hnmhTKFmc-VXO2LPWIvGcc_7ncOOySSgQywuXiE3JcIGXQpIAeFLFXUNIi6ICuOsdOB-0pXJlL0YZaLm37_oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46911d7dc4.mp4?token=Ci4cl5V2nGPn8CY-xgwZix_rZCizF2-CWJf5e1nRlOesrkXwAy2bDEhpQDTldgs3N4oEvnfsAbre8k3pqVNLjRqvvHO3iw1cm7aIMuBtJNmM_VGyS8HWPZeaFPJYlsAgEOHiCd8UgKhoTRkMdarB8wAjCF3KMz1Ry9tqxk1yiCQfsQSCWrDRfyyA-JJOI6eYtOpo-7UQ4Qo369bnQ9WkZmdu9Pq0jNB-OtKgiFVxcTxQHlGcd7T6mYUYClWIOOfV5hnmhTKFmc-VXO2LPWIvGcc_7ncOOySSgQywuXiE3JcIGXQpIAeFLFXUNIi6ICuOsdOB-0pXJlL0YZaLm37_oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آفرود سواری هم تو ایران ممنوع شد؛سازمان منابع طبیعی:
از این به بعد هر کسی بدون مجوز یا خارج از مسیرهای مشخص وارد مناطق طبیعی بشه، باهاش برخورد می‌کنیم. اگه هم آفرود به‌عنوان یه ورزش به رسمیت شناخته بشه، براش دستورالعمل و چارچوب مشخص تعیین می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69267" target="_blank">📅 20:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69266">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbbb58fbc.mp4?token=THnUG5SvW839sbaqHON85-6qKiSWNkTFBCddQfQkR5M0qYnCGN4Vd-H0LkwihtNHbJWDhla9Db_nTu2lIrdV3FFiqIKfVlQP0TYW33_8e4GCCdinSXo-t2xKc3qaSJM69VEtMhhJ55sGZASQbnAZLTGUIQW4Hjb7z36lrzGTtoPhE52N8J77Jd67_64blRNrmj8fEJXx0HWStbTLuqbVtIqxO9s6OQ0HCgz10zxwuwJFxzRUpjqY73CsmIPyUy1JKb7jlrLNfXoZy4lun3OGOv5uB7mtbPCSc-M3YVTxUaeLFuse5Ovtye6ROvSL-PDq9cm5x7E_oHJ7CP6_TVJUE2zUgT1N4Pg0SLmnZC7wslU_xSuGCrxKzxCxcXTloGFhWnyCBZK2lBFxoGSSUYvpl9vvkRMmkZ7YKVZzUDWweVS3lEk1rW4iiGWSm7v7GPM70d1wkbEpMvm2bZZqj8kh9nJ3ySFHzTePrKfjSJh2_s_mkIAZCBVrYIXJ4K9Jukl5-1Sj1vz3Cei8uAxP1MQMOifCD1PvdSXOKhjMgpP-Bojc3Oh9nokbzKDUeekcElhiDLzwvd62B5DPavbI_jksI--5vPeA0tqe4GiX2wn6pv40_NdRZeHiaCx_GiPG4dcRRQS6c0By1FSNAsO5Hjs5StfF-mWiSNGHtSqcRzGnZAk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbbb58fbc.mp4?token=THnUG5SvW839sbaqHON85-6qKiSWNkTFBCddQfQkR5M0qYnCGN4Vd-H0LkwihtNHbJWDhla9Db_nTu2lIrdV3FFiqIKfVlQP0TYW33_8e4GCCdinSXo-t2xKc3qaSJM69VEtMhhJ55sGZASQbnAZLTGUIQW4Hjb7z36lrzGTtoPhE52N8J77Jd67_64blRNrmj8fEJXx0HWStbTLuqbVtIqxO9s6OQ0HCgz10zxwuwJFxzRUpjqY73CsmIPyUy1JKb7jlrLNfXoZy4lun3OGOv5uB7mtbPCSc-M3YVTxUaeLFuse5Ovtye6ROvSL-PDq9cm5x7E_oHJ7CP6_TVJUE2zUgT1N4Pg0SLmnZC7wslU_xSuGCrxKzxCxcXTloGFhWnyCBZK2lBFxoGSSUYvpl9vvkRMmkZ7YKVZzUDWweVS3lEk1rW4iiGWSm7v7GPM70d1wkbEpMvm2bZZqj8kh9nJ3ySFHzTePrKfjSJh2_s_mkIAZCBVrYIXJ4K9Jukl5-1Sj1vz3Cei8uAxP1MQMOifCD1PvdSXOKhjMgpP-Bojc3Oh9nokbzKDUeekcElhiDLzwvd62B5DPavbI_jksI--5vPeA0tqe4GiX2wn6pv40_NdRZeHiaCx_GiPG4dcRRQS6c0By1FSNAsO5Hjs5StfF-mWiSNGHtSqcRzGnZAk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده‌یاد مانوک خدابخشیان:
"اگر رژیم مذاکره کنه باخته و اگر مذاکره نکنه هم باخته"
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69266" target="_blank">📅 19:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69265">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce71ed1d1.mp4?token=T3S74lomhaLlE0k6xnkc1DQi_667njKKaaQVHsp78fnmQ5SVSi3VVIMjzHN68eZV-SpBlrcZUeBk6_XSP7OcUVFGmQntXoIAPbk2ktLpfvD8-jaxcgSX1FRvHQTUdM3dfnH3x7VH3z-2zfN0E2hZZYfXWhDOMX4hjONv-s6qv2PdoS2xUYmpZwP1IuNF1q4tyshIIL4JlMh6NEvOSHufAsGCpugZos00u0hMoaKtcD-iMjbjzxMJdcEZVC_Bgwq2F6006wotzLopCk5OBjQ4XLsnQ6uU-fTTfA8D6mPQEFPPgx5iUnwCRdeOR_LUARVbgCbjK3g4SvpmyWgz6opGmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce71ed1d1.mp4?token=T3S74lomhaLlE0k6xnkc1DQi_667njKKaaQVHsp78fnmQ5SVSi3VVIMjzHN68eZV-SpBlrcZUeBk6_XSP7OcUVFGmQntXoIAPbk2ktLpfvD8-jaxcgSX1FRvHQTUdM3dfnH3x7VH3z-2zfN0E2hZZYfXWhDOMX4hjONv-s6qv2PdoS2xUYmpZwP1IuNF1q4tyshIIL4JlMh6NEvOSHufAsGCpugZos00u0hMoaKtcD-iMjbjzxMJdcEZVC_Bgwq2F6006wotzLopCk5OBjQ4XLsnQ6uU-fTTfA8D6mPQEFPPgx5iUnwCRdeOR_LUARVbgCbjK3g4SvpmyWgz6opGmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⁉️
سنتکام:در ساعات گذشته، رسانه‌های دولتی ایران به انتشار ادعاهای نادرست سپاه پاسداران انقلاب اسلامی (IRGC) ادامه داده‌اند؛به‌ویژه سه مورد زیر:
❌
ادعای اول: سپاه پاسداران (بار دیگر) مدعی است که مسیرهای آزاد و باز در تنگه هرمز برای کشتی‌های تجاری خطرناک هستند.
✔️
واقعیت: خطرات فوری که کشتی‌های تجاری و خدمه غیرنظامی آن‌ها را تهدید می‌کند، ناشی از تهدیدهای لفظی و تلاش‌های سپاه برای انجام حمله است.
❌
ادعای دوم: سپاه پاسداران مدعی است که سه جنگنده رادارگریز اف-۳۵ (F-35) و سه فروند هواپیمای دیگرِ ایالات متحده در جریان حمله اخیر ایران به یک پایگاه هوایی آمریکا منهدم شده‌اند.
✔️
واقعیت: هیچ‌یک از هواپیماهای ایالات متحده در تلاش‌های اخیر ایران برای حمله، منهدم یا دچار آسیب نشده‌اند. تمامی موشک‌ها و پهپادها رهگیری شدند یا به مناطق هدف‌گذاری‌شده نرسیدند.
❌
ادعای سوم: رسانه‌های دولتی ایران گزارش می‌دهند که یک نفتکش تجاری به نام «ام‌تی نورا» (M/T Nora) موفق شده است محاصره ایالات متحده را بشکند.
✔️
واقعیت: این کشتی تجاری موفق به شکستن محاصره مستحکم (دیوار فولادی) ایالات متحده نشده است. بیش از ۲۰ ناو جنگی، صدها هواپیما و هزاران نیروی نظامی آمریکا همچنان هوشیارانه به اجرای کامل این محاصره ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69265" target="_blank">📅 19:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69264">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/906e47e12d.mp4?token=KTyefsxAhpkiiI8g2JqVWjR1V0pEA27i-KUVBUuPoxDoego-Sv1YRRg6KmrCNnR5LPV5my12J7u7cbe2XjTCteYBAiQfM99WTl3Ep-e-VkXaSyWRVOll2o7c4p_OdRpXK62IjtCXmEpgqosUQG9ByrKckU-trjpX73ILFPdWLppiVDEAavbtPX1xDFyNeHBxjyDBd852aL7zT7zAsDqaIlWIkRhIiDX4AdIEY84GwrMPmJzL8AePz4BEBA4epNECmhyPOm-4tDx2hzGccjBQ3fMQqzcmkcUpcBis3B9uq3hc06cgJejrCGoPBYiLhH1TXj7blqXJbHvLJFP2fn5Jug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/906e47e12d.mp4?token=KTyefsxAhpkiiI8g2JqVWjR1V0pEA27i-KUVBUuPoxDoego-Sv1YRRg6KmrCNnR5LPV5my12J7u7cbe2XjTCteYBAiQfM99WTl3Ep-e-VkXaSyWRVOll2o7c4p_OdRpXK62IjtCXmEpgqosUQG9ByrKckU-trjpX73ILFPdWLppiVDEAavbtPX1xDFyNeHBxjyDBd852aL7zT7zAsDqaIlWIkRhIiDX4AdIEY84GwrMPmJzL8AePz4BEBA4epNECmhyPOm-4tDx2hzGccjBQ3fMQqzcmkcUpcBis3B9uq3hc06cgJejrCGoPBYiLhH1TXj7blqXJbHvLJFP2fn5Jug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پسر جوون ایرانی رفت پشت فرمون ماشینش ی خر گذاشته رانندگی کنه خودشم داره از رانندگی خره فیلم‌ میگیره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69264" target="_blank">📅 18:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69263">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
انفجارهایی در صنعا، پایتخت یمن رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69263" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69262">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhiS1B25nDMtrJ6O0KrhMLtuDqJzp5j2QZmT9HozNdp_U3IBqqw4dwrvSUUUVUeYXARHPMxfCeWV3L7CVTs-V6puwF5D6YzNE5RxhNWjBoFkRPrFZsedEA87xaIWqXa-bjXqz4j22aWEo-FutvGRYfJ3vbELwJeNA4xgVIxH7ULnNCFBWshHMfIjPXuPCI1KZrF7Tbzw74jADnuPJqZozvQlH6cSm7XzyrLw3PlHZNU03uj_mAzSDU5wIopid7aw-YL7BJOspMsTAIbJ6HhDqBsj3dEYGxj103m8rshzj0NbhBDwhrgcmn50Z-Yj4eA_CmnqQpzEUBefxTVZon-bEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه تا از تروریستای مفعول حشد‌الشعبی که در حمله مشترک آمریکا و عربستان به عراق کشته شدن!
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69262" target="_blank">📅 17:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69261">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_69NfNuSLTmpHrGz4NJwf2Er6PZOkQ0PLRvy0MuSh0FBQYInm7oyGoreAzMRfgJLwTjR6mS03uzsNO1X_1E6IvsGyyGM2-4GGoPAZKwzPl0UqFDUSwANJH2DkcoaIiheA6U6XIP-M1Vh29_BAiXASHaKh8DEw--Sj7yNyQac3OGBdxBb-9S4aXZU3Wq1dTSArGuiMRKncjHFhOldOXdYXHWikte1AO-syAW5gDgSQtfBAXEf0SuAbAamrQlTSL4jybQ4r07fbrLKTMR95f31P19lzlRWo8zcx8_UFDI3z9R8CGLH63Ff89CX0QSiwGrXOY30AvQCIfSaQMDPm-rQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
روابط عمومی سپاه پاسداران؛اطلاعیه شماره ۵۶:
دو آشیانه پهپادی و یک مخزن سوخت هواپیما و بالگردهای نظامی در پایگاه علی السالم به آتش کشیده و منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69261" target="_blank">📅 17:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69260">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=UXl-P44NOLID48SUQFdb6Z7nPB2hAEQIeuVfYGf218g7LT8mkLBa6eYage0eDnXND3PGC7vbT-gnn7THud-EvxJCu7k6EbvEQOayiuncGiBPHq5rnsJ6s1jJDgNWlQiwLqmaNUEbImuTr7hLduhK5oqg6hMIOrsoCevq9sQW-3zh8LpR4RCvlKyLg62ic8-tmLVYX_5LKo4VfWLpk_ObzGkgf5YPOFJ_EHRVjvJv17mKgWNuxP-YGWUVB_tgQBbnI2e-oAVDb5dJrHfq69zi7-uDaMKpJf0g990fLWkv8IXZQDwKTZ3oxjTGf_ftR0Ljkmil2csYfYbrhMtS7vY_5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=UXl-P44NOLID48SUQFdb6Z7nPB2hAEQIeuVfYGf218g7LT8mkLBa6eYage0eDnXND3PGC7vbT-gnn7THud-EvxJCu7k6EbvEQOayiuncGiBPHq5rnsJ6s1jJDgNWlQiwLqmaNUEbImuTr7hLduhK5oqg6hMIOrsoCevq9sQW-3zh8LpR4RCvlKyLg62ic8-tmLVYX_5LKo4VfWLpk_ObzGkgf5YPOFJ_EHRVjvJv17mKgWNuxP-YGWUVB_tgQBbnI2e-oAVDb5dJrHfq69zi7-uDaMKpJf0g990fLWkv8IXZQDwKTZ3oxjTGf_ftR0Ljkmil2csYfYbrhMtS7vY_5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدویی از لحظه دستگیریِ نوید زیادخان قره‌داغی وسط خیابون بعد از شلیک دو گلوله به پا؛ این همون شخصیه که تو لایو دخترارو کتک می‌زد و...
⚠️
‌ ‌ ‌
حاوی خون و خون‌ریزی
🔗
‌
مشاهده ویدیوی کامل بازداشت
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69260" target="_blank">📅 17:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69257">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cea20ae2a1.mp4?token=R9xAlCoL4C1s9G8BYHoy36HQXqLWLKtBkrzEFimh_kxwwaXwJYn9YVEmuvFlMZyL1aLG3JZl-bAvxcOeWLfgrXNTsKR1VA43hE9SIjPhfKc__B9uKWiXhRXEH72izOm4gDQDgc3dSJYzLsK2XROOE89avo3WJbqCAIMGcZcm2Hk-dXCwKWDqD7ZjudJcD5dSJpdI3v08cyGEb16_El5oXPT4_B6bG0UWWQk9YTiVmZO8UPnqT9GLcoLJdmx0onO1O8qlJULmb4G2DRmAmgu65HPUnzIDWvykSH496Cx2-WNekNDkbT74XWvOdfUzylTZdi9bv44X7kahExfThU_LyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cea20ae2a1.mp4?token=R9xAlCoL4C1s9G8BYHoy36HQXqLWLKtBkrzEFimh_kxwwaXwJYn9YVEmuvFlMZyL1aLG3JZl-bAvxcOeWLfgrXNTsKR1VA43hE9SIjPhfKc__B9uKWiXhRXEH72izOm4gDQDgc3dSJYzLsK2XROOE89avo3WJbqCAIMGcZcm2Hk-dXCwKWDqD7ZjudJcD5dSJpdI3v08cyGEb16_El5oXPT4_B6bG0UWWQk9YTiVmZO8UPnqT9GLcoLJdmx0onO1O8qlJULmb4G2DRmAmgu65HPUnzIDWvykSH496Cx2-WNekNDkbT74XWvOdfUzylTZdi9bv44X7kahExfThU_LyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
حملات شبانه سنگین روسیه به کی‌یف، پایتخت اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69257" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69256">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d31a669dbb.mp4?token=ABYuy2Gh3noBqER6wvXdGNjxogbxVRhkpUl5LKYxQCC6hqPr_ITlfMWLiF0w3lctu-UBpyvKDBQ5j8vxwDOXNwNzzSR3YszoKpP8gS7WbHcS_BpqnVPI18fRUPcWULzfR8aCNUtlGmwL7s_tkd87znPWF8-tfaD0BgCUpTWHamYKucGJRBe_V1gFUimOUYibBUXiAuOPGSG_KGheQyGIo23Sw01ll3INQVbAHrRuQkoi0FfbcPp7_ON3R5SwOd_ycDKfeZOy0lwDdEg842Fk255uQ6V8uGkRkih9IgZg4iZ7OSwUP-h1Ro2XIkY8kHoIMSi_8RYPiJS4O3jmKua3xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d31a669dbb.mp4?token=ABYuy2Gh3noBqER6wvXdGNjxogbxVRhkpUl5LKYxQCC6hqPr_ITlfMWLiF0w3lctu-UBpyvKDBQ5j8vxwDOXNwNzzSR3YszoKpP8gS7WbHcS_BpqnVPI18fRUPcWULzfR8aCNUtlGmwL7s_tkd87znPWF8-tfaD0BgCUpTWHamYKucGJRBe_V1gFUimOUYibBUXiAuOPGSG_KGheQyGIo23Sw01ll3INQVbAHrRuQkoi0FfbcPp7_ON3R5SwOd_ycDKfeZOy0lwDdEg842Fk255uQ6V8uGkRkih9IgZg4iZ7OSwUP-h1Ro2XIkY8kHoIMSi_8RYPiJS4O3jmKua3xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
صبح امروز ارتش آمریکا به یک پایگاه پدافند هوایی سپاه‌پاسداران در اهواز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69256" target="_blank">📅 16:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69255">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21d6f2f438.mp4?token=F7kddg6cpfA147Ni-I0I7knm1ebiEnYxU7QvvQQi5yWu56ycK4bN5HMjSVefsiPn8lj5u0lyjjdefrPnoPekmQd1syrEwIysGTNK8B0pYJjD_rff-XoUzPWdTNRyL5Gj9seqSqsnOaa4XZ9H0ie6Y_rfeTJr42BYid1SKiyKv_DQBTfeC7n_G_rrNHbyTAkXgLFZtCZOVWWOmsq0VxYf9gl0kxPyYZm58xoH79Fy9u-yYjpgZ_VHO_t3gIQo8raYLi6DizMyqzSYEvLtQ5Qk8Oj2VhuEEC8kDz0_vHJD2seAv7idHedW2TtYCY6QpsZGqx50aS7boElSLAKoG4r1CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21d6f2f438.mp4?token=F7kddg6cpfA147Ni-I0I7knm1ebiEnYxU7QvvQQi5yWu56ycK4bN5HMjSVefsiPn8lj5u0lyjjdefrPnoPekmQd1syrEwIysGTNK8B0pYJjD_rff-XoUzPWdTNRyL5Gj9seqSqsnOaa4XZ9H0ie6Y_rfeTJr42BYid1SKiyKv_DQBTfeC7n_G_rrNHbyTAkXgLFZtCZOVWWOmsq0VxYf9gl0kxPyYZm58xoH79Fy9u-yYjpgZ_VHO_t3gIQo8raYLi6DizMyqzSYEvLtQ5Qk8Oj2VhuEEC8kDz0_vHJD2seAv7idHedW2TtYCY6QpsZGqx50aS7boElSLAKoG4r1CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدویی از لحظه دستگیریِ نوید زیادخان قره‌داغی حرومزاده چهل پدر وسط خیابون:
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69255" target="_blank">📅 15:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69254">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1666d9190.mp4?token=Nt64IyrxA9bvwFMbyN50aPrBIL3ocNGx8WgH87CCBBaoeYXg8pguvyj4LPSlyMofuyopvwQVky2VTRIrcRrh0tJ8iCqZ20CwPUsGzXS2O291UxqZQAQOBjqpzPJsQ9EJyvwxgAspaWzKkXwJKptxX9pHTbxeggmQdzPPlzHP4_BsPKXkRBerGkyJqKapFemdHTKlF_Rmr9NIX4_Jwh0nhPaop2D14lkfQifIIxAzTY3n2nK8qrCpGvOcvBNMcr-qmEi1F5eBWl-AIdGRHUM8EL7PwAtWEVFYlJZ6ncmIz5GxFHqrp4tDi-iiuLe2i0xHVRDm613s68cIQqAcoToHEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1666d9190.mp4?token=Nt64IyrxA9bvwFMbyN50aPrBIL3ocNGx8WgH87CCBBaoeYXg8pguvyj4LPSlyMofuyopvwQVky2VTRIrcRrh0tJ8iCqZ20CwPUsGzXS2O291UxqZQAQOBjqpzPJsQ9EJyvwxgAspaWzKkXwJKptxX9pHTbxeggmQdzPPlzHP4_BsPKXkRBerGkyJqKapFemdHTKlF_Rmr9NIX4_Jwh0nhPaop2D14lkfQifIIxAzTY3n2nK8qrCpGvOcvBNMcr-qmEi1F5eBWl-AIdGRHUM8EL7PwAtWEVFYlJZ6ncmIz5GxFHqrp4tDi-iiuLe2i0xHVRDm613s68cIQqAcoToHEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت صداوسیما بعد از هر حمله آمریکا
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69254" target="_blank">📅 15:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69253">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‼️
🇨🇳
🇮🇷
رویترز:به گفته منابع، ایران ظرف چند هفته آینده سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد.  ۲۹ ژوئیه (رویترز) - سه منبع آگاه از این قرارداد به رویترز گفتند که انتظار می‌رود ایران ظرف چند هفته آینده، نخستین محموله از مجموع ۴۰۰ دستگاه پرتابگر موشک…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69253" target="_blank">📅 15:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69251">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BTf7LnSEWm1VPp277nA6Lg7FvFuKgp7GQUJ1TnnHrQiY47hEvqkIG5c8GAfmxG-nVwLrLNDjUg5O8tTepBUUL16vV49lMxeVgDE31j-gzuALTCABWw6rVlAIsD3lMxYkrtQx5XlLveVOEpyUBrV71VHJ94SmhjwrP-ijaSEfkvXiF-jIckWE_f8apdyUIDegQHyw4341RhQ6ixeMnoeTLfKi3LJC2O1g_-e2bJ5okrq1POvZ9LH1njRZlDQnDMCVgVAg8UplCZhvDgmrb5K_I5gx1hW01ld6Kqr-XTfW2x5TiLXKn51lD1Yh0Ii-IPEvJvJjXYOR6p7s8wULs-UEGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8b887c1d39.mp4?token=jj6o8ozrr_vcWS8kPgGKk8sSC_x80UUmoBkbHqRCR8rwtsGxtoKEfyA56jHDFmqCdAB8LRB_7aWV9B-eMjK6gLyzoJxTeZQwHCWR7FFj_JQbTGyQcapWyLae78XLmhffVzjOde_GcS6u15jJR4YCWD_kLXFRZVSsMqpsH6DD3vGndTgumnOndwGIkVf_VYhX0PPCIQmyF6B_sDqidwjsCMjlqaUehbXKMwpXjxc5Z-iGDOlpN4nIDUnBUsbGE-NdR3QnIq2z-mWN5h3CG4Ap-dqNvZGVxfjb1pzElxkJLxnoQ5yTVo-CGsMeY4wvcawkgxSgJFHhdYyCzFk9s7zJGA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8b887c1d39.mp4?token=jj6o8ozrr_vcWS8kPgGKk8sSC_x80UUmoBkbHqRCR8rwtsGxtoKEfyA56jHDFmqCdAB8LRB_7aWV9B-eMjK6gLyzoJxTeZQwHCWR7FFj_JQbTGyQcapWyLae78XLmhffVzjOde_GcS6u15jJR4YCWD_kLXFRZVSsMqpsH6DD3vGndTgumnOndwGIkVf_VYhX0PPCIQmyF6B_sDqidwjsCMjlqaUehbXKMwpXjxc5Z-iGDOlpN4nIDUnBUsbGE-NdR3QnIq2z-mWN5h3CG4Ap-dqNvZGVxfjb1pzElxkJLxnoQ5yTVo-CGsMeY4wvcawkgxSgJFHhdYyCzFk9s7zJGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مادر جاوید‌نام ابوالفضل سپاهی، که توی میدان علیخانی اصفهان اعدام شد:
خطاب به یه نفر به اسم هادی: بگم برات که تیر زده بودن تو پای ابوالفضل؟ بگم برات که زیر چشماشو با فندک اتمی سوزونده بودن؟
بگم برات که ۲۰ روز بهش آب ندادن؟ بگم برات که فکشو شکسته بودن؟ بگم برات که دماغشو له کرده بودن و آویزون شده بود؟
هنوزم تحمل شنیدنشو داری که بگم برات...؟
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69251" target="_blank">📅 14:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69250">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🇮🇷
سپاه‌پاسداران:
تخریب کامل سه فروند هواپیمای اف 35 و ورود خسارت سنگین به سه فروند دیگر در الازرق در پاسخ به جنایت دشمن آمریکایی در قشم.
همچنین چند افسر و کادر فنی و تعمیرات دشمن نیز در این حمله کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69250" target="_blank">📅 14:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69249">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daa6076311.mp4?token=SCdH6G8hZjgWE74CEXtYn_nCFI-V04d7V0u2nQA-PluCodtnx0ZK4PWd-EY-Vjm0RZyqmi0ZE66NyPegvw3fW7s6SHm7Pn-_Ji5vNQc7bXt6GCRbT65riSDX6R7PeY1l-Bx3J9SAnviqAJcbuIQq-YojmxOsGqwQ1pawBW_WQVg8_YsA9DWI6jt1Pb5eOWpQJVkWSZvucF0BRnwdJKxvmYVJd-NQaotPsc5IxmkPJPMkOTo7Ej7zDJ5KN76kdMrxVDYEizz5Oe8H5azCbxuWfV23h2eycwep5sgdb9gr75y5mwCKBBJ1cOSCXq61QFHMTwA3KIdHXF-zTvy9RH80ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daa6076311.mp4?token=SCdH6G8hZjgWE74CEXtYn_nCFI-V04d7V0u2nQA-PluCodtnx0ZK4PWd-EY-Vjm0RZyqmi0ZE66NyPegvw3fW7s6SHm7Pn-_Ji5vNQc7bXt6GCRbT65riSDX6R7PeY1l-Bx3J9SAnviqAJcbuIQq-YojmxOsGqwQ1pawBW_WQVg8_YsA9DWI6jt1Pb5eOWpQJVkWSZvucF0BRnwdJKxvmYVJd-NQaotPsc5IxmkPJPMkOTo7Ej7zDJ5KN76kdMrxVDYEizz5Oe8H5azCbxuWfV23h2eycwep5sgdb9gr75y5mwCKBBJ1cOSCXq61QFHMTwA3KIdHXF-zTvy9RH80ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرود دیدنی یک F/A-18 Hornet بر روی ناو هواپیمابر.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69249" target="_blank">📅 14:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69248">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5OfT5gkQyOqRG4lzpe6aOv79mTJNBsZ9xj3dknSNYUofvIAn59JOx09W13cKCB0K1ozgO5B5G-En4fd_ocWVx5uG33KFT2SZbPvyE-XVaiCcbYEFRZ3NPlFLX4b4hcoVdsfVvOYs6qSPksQS_9WnfYpQfpor39CX7hwFDcIPTovaz04mM7lR_uVR6L2kG1IZ8UH1oOAkmHyq3y8bT2PLxQiQRq_TYl0GgXz2-d8YjWubGjhexmDfO_NNtKey6Cs4hnLCsPAnDKedlmYJvmAnLy3N2JcB_EdHtcqF73N-VDo_iutxaVqYioT-TeBKzJLojqF0u9YZ8sMGC8MgZ0-4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⏺
ان‌بی‌سی‌ نیوز:
به گفته منابع آگاه، ترامپ در قبال مسئله ایران «به‌شدت کلافه» شده است، چرا که مقامات ارشد بر سر راهبرد واحدی توافق ندارند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69248" target="_blank">📅 13:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69247">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a176457914.mp4?token=ld6DIopT-SiY7TWAMM5FXjGC2gjNAScgp-885zvPPMgSQpoMJXolQ2uHvXT38J7VtSQ7_v7OgumcjaSEGc8j85U2DnALPoNJRWgQkQJaCBeHMyE_jllYkn9F_3vLW9aYpvLG37i4cbd9R6RWZ7qHWoCazAHuKFFkazr8jjzp5fCGPI7stqf3oypFZKTU5Txip1Nzfj8qVFExj5fbtSbxVIv8DMEhYe0CAEs77ZMc05m6ToeSRAgmbzjkkE_cmnciZW9Cmi8AWVuUJHWH89Oqy4334jiId0psHZOlLpbBe0djEuA-yQhzeolYyFVF74TEbCa7f9yc4zyE5igUVyLNNpkPD6EUfKzOexUyUjkArj7IUCWyN3mfT2BHaffVROFmVk3gdI0mG93Eea6_tm4VdZjr1BZO17DWZoa-6jb6b0csMk_VaxRrokZbgxEjmN3H1sBUkvAgueyDkn-LaAMUgUACBkXPkJsktwEUBVoVRh5tqnjiQAF64ojjwdJdgUWRjF9u_kBa4RHtS-Hkcc8MckwInU_LHln4rUR8eb_U80NokR1HXrOOP0A5ygBvbhxr5C0mN9pcfS2ZSDAvODM35ZmI-qr-W4a9vpHvSffKb03E744AeXt9vNrzzhSpUmGmc7Jky0dtf1gphF4Ng7WC_Vim0JkPTP-jkmkLblxub_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a176457914.mp4?token=ld6DIopT-SiY7TWAMM5FXjGC2gjNAScgp-885zvPPMgSQpoMJXolQ2uHvXT38J7VtSQ7_v7OgumcjaSEGc8j85U2DnALPoNJRWgQkQJaCBeHMyE_jllYkn9F_3vLW9aYpvLG37i4cbd9R6RWZ7qHWoCazAHuKFFkazr8jjzp5fCGPI7stqf3oypFZKTU5Txip1Nzfj8qVFExj5fbtSbxVIv8DMEhYe0CAEs77ZMc05m6ToeSRAgmbzjkkE_cmnciZW9Cmi8AWVuUJHWH89Oqy4334jiId0psHZOlLpbBe0djEuA-yQhzeolYyFVF74TEbCa7f9yc4zyE5igUVyLNNpkPD6EUfKzOexUyUjkArj7IUCWyN3mfT2BHaffVROFmVk3gdI0mG93Eea6_tm4VdZjr1BZO17DWZoa-6jb6b0csMk_VaxRrokZbgxEjmN3H1sBUkvAgueyDkn-LaAMUgUACBkXPkJsktwEUBVoVRh5tqnjiQAF64ojjwdJdgUWRjF9u_kBa4RHtS-Hkcc8MckwInU_LHln4rUR8eb_U80NokR1HXrOOP0A5ygBvbhxr5C0mN9pcfS2ZSDAvODM35ZmI-qr-W4a9vpHvSffKb03E744AeXt9vNrzzhSpUmGmc7Jky0dtf1gphF4Ng7WC_Vim0JkPTP-jkmkLblxub_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیلم گوه خوردن نوید حرومزاده هزارپدر که دخترا رو کتک میزد اومد بیرو
ن؛
از همه عذرخواهی میکنم ، گوه خوردم غلط کردم!
بذارید برم توبه کنم ، درمان بشم و برگردم به زندگیم برسم.
اتفاقاتی که بین من و اون خانم‌ها میفتاد رو تو ذهنم الکی بزرگ می‌کردم و دیگه کنترلم رو از دست میدادم.
خانم‌هایی که کتک میزدم، من رو درک میکردن و هیچ شکایتی ازم نمی‌کردن.
اتفاقا مردم خوب کاری کردن که انقدر واکنش نشون دادن؛ باعث شد یک بار واسه همیشه به خودم بیام و خیلی مسائل رو کنار بذارم.
از تَه قلبم از همه مردم عذرخواهی میکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69247" target="_blank">📅 12:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69246">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1958bb40.mp4?token=fpe8fv3lfz6Zr0mHPLqFYtL255Joh2VA6NN_j5rYndhMHnjQEW3JgkcgZpqZUkCe9xoV1Mu_DrUjkuYTiYUmmYIT2x55RsRb2mbPGtzMMYva6Z18hLJOcy-3GwgmGku6EnZSEZl75tE56gpD0zEq79058_0yKsevy4ugGJ2u3q2DneQbGO2JL5wEASw0P3DWcofkyvJBxsNG6XsyVJuhX6RcpAcoB79NI0Dc7aIfYvMCyLF1ONLlHBv9DlWkVbIUVvDO9PDuQNilMBwZ91KI8zo9JR1yrji3emegleROoIa7UpFzUYWwS8cWerulejYbIaF_06zb6xZnu158_-Hxmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1958bb40.mp4?token=fpe8fv3lfz6Zr0mHPLqFYtL255Joh2VA6NN_j5rYndhMHnjQEW3JgkcgZpqZUkCe9xoV1Mu_DrUjkuYTiYUmmYIT2x55RsRb2mbPGtzMMYva6Z18hLJOcy-3GwgmGku6EnZSEZl75tE56gpD0zEq79058_0yKsevy4ugGJ2u3q2DneQbGO2JL5wEASw0P3DWcofkyvJBxsNG6XsyVJuhX6RcpAcoB79NI0Dc7aIfYvMCyLF1ONLlHBv9DlWkVbIUVvDO9PDuQNilMBwZ91KI8zo9JR1yrji3emegleROoIa7UpFzUYWwS8cWerulejYbIaF_06zb6xZnu158_-Hxmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خبرنگار صداوسیما حین گزارش پرید توی آب و فاز کوسه گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69246" target="_blank">📅 12:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69245">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8YtbzbuH36fgqycTzsA0Ldb1ycVDCh_FjUvE2JAJFBTLRUuoozzLVjmfR_Y-qrgxR6r6CGwvS27dKVxzeU_Ee9gU_yt5dPz9MW4iDj1NkJOFUpRCrt4SuKnIxzlcIzpibUvnOSgBpJA7Mp-e-A1JdBi7xhQTQ4iU31SMgs4bM3H-Q2fsX19GMU45cDRIXp1cazeOvUM1RKQ6S0bOSo4Q7r6jXnDjgOHsF2_nDGcsT6YjtJ2yO1absh5TdGhJGbBBwRELSMUszSmSILermfCG7lxNY8qe82ZzmEUTDD8Z3susJmO4lJSkZdU0UbGAtDZ8hb7DC6HeqLmmagTj7izew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
سپاه پاسداران:
متجاوز رو همین امروز تنبیه میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69245" target="_blank">📅 11:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69243">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEDgU7C3BGkOcgVN2_oY6NqPwSckXTf_rGGssdhnxg-6p5YyU_0j7xyQgHsYF9i4rHA2j0JPJlHZpGwvpo0Z1sxbjssuJfwRit_xaXaJg996beBQtHZckev0klmoPJHChajGxKMSeblKGMtGwMKT9rqF-ZvsCjhYvrdmQj63yOibIRGiSHORZngnh5wSbEvjzNHzsALt55mwIVMnAEuX1IwaLQWeLrWHABLMFLaKqI-f57MykfIQYep8oOUWV8appDeUVpsS3eLoaQAFoHpMDHKwW5HvTGOme05sSXeE2sIrUARevOrxRSCty9Znii6jwEC1gJyLuzTFSikZy2S4Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/854dca423a.mp4?token=puCjywg0GoIVAbfEIkxs0-QLZVywp1K-0Kk5c3Qx4SwOYv6yUdJFKWJXgp0jQBcL2_lkTh10425Bz0gBHHYq6RxlNJzCwhltWE4QmuITr0Tih0QUQyWMCC8QQ2rDvjLPyyWM1IO1abmB-3GI90tkDO9vcmwoVz0nUT4i6_FNS_5eFi8Ghx8f5Bo62J8X5KLCAS31PP5HPiaJtkCyg4J192qlYQjlJlCoH41ZAqhpQ13EYPpMD0O51ONk9WCdRsLTkl6dx2SoM6jA_7XPH0RMtjA2IoP76xv5lq8k_75s5mUKqUyp9GH65wmKFrJMBnxwe79LPaFsOM5YTHloZfkQaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/854dca423a.mp4?token=puCjywg0GoIVAbfEIkxs0-QLZVywp1K-0Kk5c3Qx4SwOYv6yUdJFKWJXgp0jQBcL2_lkTh10425Bz0gBHHYq6RxlNJzCwhltWE4QmuITr0Tih0QUQyWMCC8QQ2rDvjLPyyWM1IO1abmB-3GI90tkDO9vcmwoVz0nUT4i6_FNS_5eFi8Ghx8f5Bo62J8X5KLCAS31PP5HPiaJtkCyg4J192qlYQjlJlCoH41ZAqhpQ13EYPpMD0O51ONk9WCdRsLTkl6dx2SoM6jA_7XPH0RMtjA2IoP76xv5lq8k_75s5mUKqUyp9GH65wmKFrJMBnxwe79LPaFsOM5YTHloZfkQaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔞
ویدیوی وحشتناک از یه حرومزاده به اسم «نوید زیادخان قره‌داغی» داره همه‌جا پخش می‌شه، تو لایو اینستاگرامش چند تا خانم رو خیلی بد کتک می‌زنه و کلی بهشون فحش می‌ده.  هنوز دقیقاً مشخص نیست چرا این کار رو کرده و اطلاعات موثقی بیرون نیومده، بعضی‌ها می‌گن دخترا…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69243" target="_blank">📅 11:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69242">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/15118cd8c7.mp4?token=I21lCrbPMmbJ5WwN_PRcZXitDwLo3-LBIOF6QqYElcrIF0DZqrk9dpLNpBNy8f0ofFiKcQZanGhRo438mFuXTl_OzcoNfp0a6HV7I9fnxQ8BJrFMMOVG9cxHCQvdY8llqWpyFl0lhS3cw1fWm--qpYyE8ZU9s_ecjWDsbQEzPlsyFb0jQUHxGrIVDYc8YKrdCdpQwvHy9PPDIeMimZRBJGmk3h5ZOSq54lt23I3fhZsMe2k-yD-_g_LJnok7VVpms65BRknOJ_tzQz-7j9dqacpYfTVNhiOdMJZyZqkOZT6NNkN4SlMWYNIiBrt2LQ5ZoJgW4cEZ_bJKlOXqjvHlrw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/15118cd8c7.mp4?token=I21lCrbPMmbJ5WwN_PRcZXitDwLo3-LBIOF6QqYElcrIF0DZqrk9dpLNpBNy8f0ofFiKcQZanGhRo438mFuXTl_OzcoNfp0a6HV7I9fnxQ8BJrFMMOVG9cxHCQvdY8llqWpyFl0lhS3cw1fWm--qpYyE8ZU9s_ecjWDsbQEzPlsyFb0jQUHxGrIVDYc8YKrdCdpQwvHy9PPDIeMimZRBJGmk3h5ZOSq54lt23I3fhZsMe2k-yD-_g_LJnok7VVpms65BRknOJ_tzQz-7j9dqacpYfTVNhiOdMJZyZqkOZT6NNkN4SlMWYNIiBrt2LQ5ZoJgW4cEZ_bJKlOXqjvHlrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه این خانم در الجزایر و تبریکش به یکی از کاندیدای انتخابات بابت پیروزیش خیلی وایرال شده.
"
منم کلی سوال دارم
🙂
"
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69242" target="_blank">📅 11:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69241">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🎙
خبرنگار:
نیویورک‌تایمز گزارش داده قبل از شروع جنگ، شما به ترامپ گفته بودید برنامه موشک‌های بالستیک ایران ظرف چند هفته نابود می‌شه، بدون اینکه تنگه هرمز بسته بشه و حتی ممکنه به تغییر رژیم هم منجر بشه.
اما الان بیشتر از پنج ماه از شروع جنگ گذشته، ایران هنوز موشک‌هاش رو داره، رژیم همچنان سر کاره و عملاً تنگه هرمز هم بسته شده. چرا ارزیابی اولیه‌تون این‌قدر اشتباه از آب دراومد؟
🇮🇱
نتانیاهو:
این اصلاً ارزیابی من نبود و چیزی که نقل کردید، درست نیست.
فقط یه پیش‌بینی می‌کنم؛ بعد از این شکاف عمیقی که بین مردم و حکومت ایجاد شده و اتفاقاتی که رخ داده، فکر می‌کنم این رژیم در نهایت سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69241" target="_blank">📅 10:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69240">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e988916503.mp4?token=OZK8IaDFfNWSCh08-_GeHuSOSBuZNAmvtRCj5AnN3AGewvD6FNOzvKm3fmJN9q7yhy-BRpKkQTssvdj0rFmtTwk3wF6fMVAwzi408_vKjMt0IItZr543kCReLf5o8r6cvXEzFQvbZOeiGHhgFgEx6F8AAO9zNLUYvgOQF34tjCltCtCVELp1wuT9wPuZvigT14tb1ytkJP6HvergSXmGvqORsmoZByH1d6aIlFVBUNgdh8rKXoDyoZRM5ED3akH3QTbqkEbWuc-Cl3bzxLnF8C7LrETg6e6wg-weg50896NrviWHUfwP2PDF_ZGdNgpx_WxxNSUY1KaDK2D973VPGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e988916503.mp4?token=OZK8IaDFfNWSCh08-_GeHuSOSBuZNAmvtRCj5AnN3AGewvD6FNOzvKm3fmJN9q7yhy-BRpKkQTssvdj0rFmtTwk3wF6fMVAwzi408_vKjMt0IItZr543kCReLf5o8r6cvXEzFQvbZOeiGHhgFgEx6F8AAO9zNLUYvgOQF34tjCltCtCVELp1wuT9wPuZvigT14tb1ytkJP6HvergSXmGvqORsmoZByH1d6aIlFVBUNgdh8rKXoDyoZRM5ED3akH3QTbqkEbWuc-Cl3bzxLnF8C7LrETg6e6wg-weg50896NrviWHUfwP2PDF_ZGdNgpx_WxxNSUY1KaDK2D973VPGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سؤال: آیا هدف شما همچنان تغییر رژیم است؟
🇮🇱
نتانیاهو:
هدف من این است که اطمینان حاصل کنم ایران، با وجود این رژیم، به سلاح هسته‌ای دست پیدا نمی‌کند.
این موضوعی است که من و ترامپ هر دو بر سر آن توافق داریم، چرا که در غیر این صورت، با دنیای متفاوتی روبرو خواهیم بود.
آن‌ها با سایر کشورها و جوامع دیگر متفاوت هستند.
🎙
سؤال:
همین دیروز گفتید که به نظر شما دستیابی به یک راه‌حل دیپلماتیک بعید است. چرا فکر می‌کنید ارزیابی‌های شما تا این حد با یکدیگر متفاوت است؟
🇮🇱
نتانیاهو:
خب، نمی‌دانم آیا واقعاً بعید است یا نه، اما می‌دانید، من نسبت به شیوه عملکرد ایران تردید دارم.
آن‌ها همیشه دروغ می‌گویند، همیشه تقلب می‌کنند و همیشه وقت‌کشی می‌کنند. آیا ممکن است این رویه با اعمال فشار کافی دیپلماتیک و اقتصادی تغییر کند؟ باید امتحان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69240" target="_blank">📅 10:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69239">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctthjT5rfLUCsMd3uAuzqwARvgHUkkpnfLx19Wf4CkEFfX4mEmkzI0pMs5zH3DJNgVZx4KzKLYIyI7sE_wEjmhK8Z8iK6bPNGS3rqLv6hQ7cCpxYsjHvMfPWjjDLhuMr4kPvsBc2ZiM024OzxfGFT_7bwJHsIHMsTXE7IBPzVA_nQQuXeaqYTA97Tcz5VL7E7v9TQORRroaWn2-v_SCBduh3CWBadnBwAVQQP8og9HfmKD62X8vBKSKTS_v574UzSGLEZpcJGClgEIkOL27vZFtt_AzJKF3ibhhyiX9_jDjUrLdri6eEdm8Myr9ehtP5ZMGJ4BYT-v9c9jt0H4vh6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇺🇸
تحلیل مرکز مطالعات استراتژیک و بین‌المللی (CSIS):
ایالات متحده اکنون تقریباً ۸۲۷ موشک پاتریوت و ۲۷۸ موشک رهگیر دفاع هوایی ارتفاع بالای ترمینال (THAAD) باقی مانده دارد که نسبت به تخمین‌های قبلی به ترتیب ۲۳۳۰ و ۴۵۲ کاهش یافته است.
تحلیلگران هشدار می‌دهند که با وجود تلاش‌های گسترده برای تولید، تکمیل مجدد این موجودی موشک‌های پیشرفته می‌تواند سال‌ها طول بکشد و در صورت بالا ماندن تقاضا، ظرفیت محدودی برای سایر موارد احتمالی عمده باقی می‌گذارد.
سی‌ان‌ان گزارش می‌دهد که منابع پنتاگون می‌گویند این تخمین‌ها نزدیک به ارقام داخلی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69239" target="_blank">📅 10:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69237">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d926097b7.mp4?token=UlM34hXoQZ5Vq23QsRWmyHAejfYqQzf1cWhd_3Oq5xp0SCrK0pZiUogxLKqdktn03YMiIeN8lkJ-oR2BG8kXIVz1Nc2kEydZ9Jwba5LK4z3kR4szpIlZTd6bzISoqQpTfefBUFC3LEVF5a6-xzBy64eEKgEaHBdeD9phsYVec9W2nhOR5lvbaIPZUxlIkihASbHc3ZbbHXIxECPryUWaYu4-nMTXxTd2sWvJseh8kALEiSO06G-1qiGveX2o51wY0fxwrXpN3pjI8FhRTXoHQds8K_w9rt5Crh9ZhAz_QNume3DytYdU2FP10s9e8lvWzdI06otZOjbng77hTsLKvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d926097b7.mp4?token=UlM34hXoQZ5Vq23QsRWmyHAejfYqQzf1cWhd_3Oq5xp0SCrK0pZiUogxLKqdktn03YMiIeN8lkJ-oR2BG8kXIVz1Nc2kEydZ9Jwba5LK4z3kR4szpIlZTd6bzISoqQpTfefBUFC3LEVF5a6-xzBy64eEKgEaHBdeD9phsYVec9W2nhOR5lvbaIPZUxlIkihASbHc3ZbbHXIxECPryUWaYu4-nMTXxTd2sWvJseh8kALEiSO06G-1qiGveX2o51wY0fxwrXpN3pjI8FhRTXoHQds8K_w9rt5Crh9ZhAz_QNume3DytYdU2FP10s9e8lvWzdI06otZOjbng77hTsLKvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حملات دیشب آمریکا به نقاطی از کشور
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69237" target="_blank">📅 09:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69233">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04e8c731a4.mp4?token=KTi5AjuDF46IydUXM_vq09r8RVZICQ_49mbVGzNIzA04RM1JNn7ElKAxs6okXB9CiRDRg6Jm4z7LiOLsDu66DF7DBQGriVz-doIq7Paptgx-kEd0NtIn-Ot77KoSbDHIp1EG6zxSvZLQwbbHv0JSol2Vw28w1zbeIv0qXJ6Ozo8wMWWUqYPG1LmygUkE0U23ZQDV6BP9KufsMoslfNsXO13rBWF5ge3ACppjq_LMQjK762JjS9z5gF96p9vBLrxThln6RqyXa-8rhT8n2QcVYAlHGdx1MjNPZYO12TspdFYtshMw89qmtTpI2jv_NlSEjFOLpvnDMwxNsbYSwrfvpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04e8c731a4.mp4?token=KTi5AjuDF46IydUXM_vq09r8RVZICQ_49mbVGzNIzA04RM1JNn7ElKAxs6okXB9CiRDRg6Jm4z7LiOLsDu66DF7DBQGriVz-doIq7Paptgx-kEd0NtIn-Ot77KoSbDHIp1EG6zxSvZLQwbbHv0JSol2Vw28w1zbeIv0qXJ6Ozo8wMWWUqYPG1LmygUkE0U23ZQDV6BP9KufsMoslfNsXO13rBWF5ge3ACppjq_LMQjK762JjS9z5gF96p9vBLrxThln6RqyXa-8rhT8n2QcVYAlHGdx1MjNPZYO12TspdFYtshMw89qmtTpI2jv_NlSEjFOLpvnDMwxNsbYSwrfvpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
هواپیمای باری C-2A Greyhound متعلق به نیروی دریایی ایالات متحده، دیروز آخرین پرواز خود را انجام داد و اکنون پس از حدود 60 سال خدمت، رسماً از خدمت نظامی خارج شده است.
🗣️
با از رده خارج شدن هواپیمای C-2A Greyhound، تمام هواپیماهای نظامی که توسط شرکت Grumman قبل از ادغام آن با شرکت Northrop Corporation ساخته شده بودند، اکنون از خدمت نظامی خارج شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69233" target="_blank">📅 09:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69232">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!  ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69232" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69231">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=di8mBkAAUqQAH-wLW6c8UI_gji0ophkhpzHuEVd1tMAs7VwB-5H7_dAKL3UlfjWR_7frZrqRHSJxkwo2_C5dcg73gGPImrLMgb9FhmPOjh13VQVQathg1twP528vyiQJPTwxKMUuDcH-ypIEVaRbcnQUkchJCiMGzlBIqyqanJCmkDqj6HqfuNM0MlNtdZCmUS8XClIl4ofFa2W8uYg2phfNHvvyKDokGdJnmJtls6yOgid7Ppk97zTviHa9Sb9eLN7g25HE9M8pD4K3KxZFArhT0nHXcU1I6b2R6mvlKfDmJ3VbBp4BQ_yDBeKVYw3H4pGdONWkuM0ZtX8HJlzlhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=di8mBkAAUqQAH-wLW6c8UI_gji0ophkhpzHuEVd1tMAs7VwB-5H7_dAKL3UlfjWR_7frZrqRHSJxkwo2_C5dcg73gGPImrLMgb9FhmPOjh13VQVQathg1twP528vyiQJPTwxKMUuDcH-ypIEVaRbcnQUkchJCiMGzlBIqyqanJCmkDqj6HqfuNM0MlNtdZCmUS8XClIl4ofFa2W8uYg2phfNHvvyKDokGdJnmJtls6yOgid7Ppk97zTviHa9Sb9eLN7g25HE9M8pD4K3KxZFArhT0nHXcU1I6b2R6mvlKfDmJ3VbBp4BQ_yDBeKVYw3H4pGdONWkuM0ZtX8HJlzlhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!
ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی تخصصی بازی‌های دوستانه باشگاهی و تورنمنت‌های معتبر
➕
فرم‌های گلزنی (بله/خیر) و گل بالا/پایین با تحلیل آماری
اگر می‌خوای از روز اول چالش همراه ما باشی، همین الان وارد شو:
🔗
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69231" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69229">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NMzYWovKhR6x-EL1B7RgjvlsL8UkcASYji7Gy0yMhv3Rx-ofiWxXg7HSuGSjMAJzPmccmquUNhbGFr3tT8ReVfYJAWnwSZG99V0YLyyS7As1YN_1U7BfaHzzHM0quPLMSEjn7UZ4-lggTOpuMDyKkY4BBhUH0rHp3W1ZIy-xrdUKpV1lJc8VVpjHpEG5ryUPPgam2z0nG93533hOqbIzrOQ2LEzoCUx5WTjsRqE7_r4O9Y-rbd_I6q41rzJrGK29rbTbw_A28uDJ7IxBFaO9LUH3J_-nAXVP_F7M02ZiWe5oQLt6aBLt_colSy-BbqTikojqGaRsECeWjk5riROThA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QNImWHlne0FBWPghEUkW3yUthav3jF9RmLa1OkRdmm1_sv4U-dg-ZBBDqWtMpjCSfBGoL2AN8-77EVPLr_Hg9XEfRkBpQg0QgSkeb4rtQaZ0_vBCKJzSFoBruUIVrvPOGMWYKtccy2hyPsKkdzTF8oCW0G7CCjOa2fuxoCaPpHV14mH1yJ8RMN3KgxNH_fLnvAEgQmCfkEIcO7NB2fbpC2EgfxP7VUpeZ57lZQZ_gZczJJUA8XWTaR2akLqujm034bK8eC_6KHYAAu_10oIzN2--weplV_8lz6pz_bsJSvCCSLAu2VdSYJEZugB1xV0SYTt4yzWO1Dw5-rpZFx9_Ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
وال‌استریت ژورنال: دریاسالار برد کوپر گزینه‌ای را برای یک کارزار هوایی تنبیهی علیه ایران آماده کرده است که می‌تواند تا دو هفته به طول انجامد.
کوپر معتقد است اگر ایالات متحده خواهان اثربخشی اقدام نظامی است، باید برای شکستن بن‌بست موجود، حملات هوایی خود را تشدید کند تا بدین‌وسیله تهدید موشکی ایران را به‌طور قابل‌توجهی تضعیف نماید.
این رویکردِ «اقدام گسترده» — که یکی از چندین گزینه تدوین‌شده توسط اوست — نیاز آمریکا به استفاده از مهمات پدافندی را کاهش خواهد داد، زیرا توانایی ایران برای انجام حمله کمتر خواهد شد.
- مقامات گفته‌اند که در صورت تصمیم دولت ترامپ برای بازگشت به عملیات‌های رزمی عمده، نیروهای اسرائیلی نیز ممکن است در حمله بزرگ احتمالی آمریکا مشارکت داده شوند.
- کوپر در جریان تشریح گزینه‌های مربوط به یک کارزار هوایی شدید، از حمایت «هگ‌ست» برخوردار شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69229" target="_blank">📅 02:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69228">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/leTGEqZSTpG2_w293hHSecPaTbfPj80_P0oKGWIdmk4ZZsUi27A4YTDe5VimPuYsIS7q9FqUUWP3wub8-V4mb64JB2i5w5CKk4p2BO9HCR9yZbuhx4wEj8fP6sdUrPHgzPDlGvv1Mnwv5v6ENARuFkG58MxsvWjF6Sjr2-GnPmLC8wKEVpB8GN0IM211uQA48-FPP_MK73bfYaD5C3mvVcySWemAGhUXURALPxVwtG5xoXF34pV2srxAw25scucNcbrgB3IUrZvEA7vkkS2IOYMEgS_hUr9qrqNkai6vUeV5F3YKfPfsIq60OurnWeb4uJK951T6FHiOu3SRvESpyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوووری
؛باراک‌راوید:
یک مقام آمریکایی به من گفت که ارتش ایالات متحده در حال انجام حملات هوایی در ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69228" target="_blank">📅 02:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69227">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
گزارش های اولیه از انفجار در نورآباد ممسنی استان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69227" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69225">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTsLDqNAJBW9Sc4fCjfKZsPMYuCDeZMVjUc09pFUFHBs7p8PYfJJHbgXta7ho5fYdej27fbeMagUURnbNAoo8qwFAVerOVAj8xxYvd8IGxJSoUdbsX1tBF-CeSk0t8CwwkyAg0w8JoVvg0xTy2sC90eIgZi_iYiOHIYr3ZewHG4EKLXsNooiXjaWeN7cepphH6nlKfbGNMm-6r2ESYgkKrvljpnVXPdWHPQfU6I9YDm91Mt6z4YBJm3qwmcgwH0NzO3K7HSWwTsR_MmK2Z-mlEEh3ILlHkKsEEwZFbfnzBXFiPvXXUwLhIXGSH2UX0l5H13bFUGLz4aVD1DhTNck9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بعد از توییت عراقچی درباره اوکراین، خبرگزاری رجانیوز، عراقچی رو ماله‌کش خطاب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69225" target="_blank">📅 01:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69224">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sv-Jg_WM_5f8bUWG4nI_OOhseV8ViNC6r5oFWRShayuU2i89fwdj4j1L2UdClI9i4GDrcpSicIC4JeVKjr5G3QfW2uIQ8QH2kcPooC0IHCMUNEFFp47Kpp5l22SnFCGDf_sgtdE46Q0HU7Ah9u0spfiNOjZFM7jy9dELBsQBJvQIkPrKkdqelwbrlx3Hp01V6yVNwYHEa0YYDIdNYT3lZ80cLCtePI2gBSK8rxIxoNjzQQsQ-BKPkZkKsD8dw5Enj1hI5WBXI8k8sdb-HXJ6FtrBm00mG5viPEjKV8yQexTYT5NQuF-7jamiMVNiYQtFGGE1EvtIbdLBocDMS3k_IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حساب توییتر خبرگزاری تسنیم وابسته به سپاه بسته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69224" target="_blank">📅 01:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69223">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8BxY51cofAmgksGL8EpHEYyHCntWDoa8FArdlfl9_7cUbgs63iQwEELYxnPBDY_7oM5i3Cbz4mlAr04gdIwu2QvJ2CLLTedUp25vGYLkhDYtqxQVSRat7MWHynZ8DCFTkqBAV-pe1pBSXBaoCBMlA1gbebFstGhlXNTOBxdj3_5dvTpC2JZCdNuGN5t5dIV22kA2wJ0shqM6jxKf4eTHAMSsYVeaeDrO0mI2qJZ6OZiBeDrvuLV93oA3IwXQlGEGxb1aOAnsAwidvrfxCtmwC0tPgJ1VFkDEQegD8KVGAxGcDrJdamW0-Ad7ExPHTN1NuTAAAevJQEUNPIBLFTqDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‏9 فروند هواپیمای تانکردار آمریکایی و یک فروند هواپیمای هشدار اولیه مدل E-3B در حال پرواز بر فراز خاورمیانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69223" target="_blank">📅 01:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69222">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fK2O8q1kVNGBCC_nCq0EafSyNOnG7JHbRSSliZVx1t8ADT6vf5Jg7PemGUAgx9z95Sp-1qwVgU9gY6AMsKwYm_7F42i1PeW_0JBk1CuLAXyRKl2myg1FMTnAlR3Fn7ai98hpZURsQbbE2WAYG7Uw5fd8ssaBAAQm3HfVVjJj-gsbRufmvfHueXfH-mo0rKS9XfchWa1_HcaiXQwNix62PtvqYnnV3YLf3EPkgKwf_pnTxglHspFAyaQp0M1EfMMgob2td0kTlK46qW_Uz8f4O6yeOBIYnmbHFrVUJng_UFlMwFfRa7D-Fj0z4Y3aR7Kk2u96XdSRxb1kMFRZ8UnXVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شش سوخت‌رسان آمریکایی در آسمان منطقه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/69222" target="_blank">📅 00:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69221">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های غیر رسمی از شلیک موشک از یزد  @News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/69221" target="_blank">📅 00:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69220">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXthQ0M5AdNMHno04zr9uF6fdXaFhpZrNZUrrwW0agNj-q7UaejFqEpwt-nEBlwb62h1r-Uy99ecvMbeXxVkaOdrXFe3EeThU0_9kSNrmcXLuBP-0QgV-l4JNd8M0JDj4ocm6pGjkmKLdlpPYntLvR6Eej4z__t28NNDQbcFm8aK1oUd12JkWuF3zKpGLtyZXuMbu73LrRfdo59c5UP-DV7h7dXAs5R2qJfX7J6waOO46QeCAS6Hh4bhRAdxFNoLgPWjmwI4e_SVPh_DAAdMiwrFeqFZmyH5VnFvPQ2tMLtScHK-kGNajpYUYTsFxqto85L-WjG_NblK5LUlpIbucQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سپاه تو تلگرام یک کانال و اکانت ساخته بود گفته بود هرکی تو اردن و کویت تحرکاتی از نظامی های امریکایی دید گزارش بده؛
لحظاتی پیش تلگرام سیک اکانتشو زد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/69220" target="_blank">📅 00:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69219">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های غیر رسمی از شلیک موشک از یزد
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69219" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69217">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c08d37ce36.mp4?token=SUsZjoCRJ64NBO8fQS1usOkW_rhqN-cZR1wvk7x9MB5k8Se5LBPTjTMVUCouxux3h9avpRsfcvtZkR_HAh2nW8CyOM1wVx133fIoPqecug7FdGy90mHWcvGwxwGNrQFVA750YjdGa_kPCvkuYS1NkFYK8aIgyVVg7_fXX2VkEN7clqTnFl2Uh__1Qz_-4ohKxtQmW4jRyu2MgcAUI7I3-wvz--7x661n01cuwcxv3W29Tu5SzL3vdid1S3C1FKCk2SUeJfUrIU69XPIQ9i67oWNR10ullQNjsB9674FgJiS3JjlB1rtzuuQuL4X9mtF3T-19wjZ-sFnrXDjegxGH9A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c08d37ce36.mp4?token=SUsZjoCRJ64NBO8fQS1usOkW_rhqN-cZR1wvk7x9MB5k8Se5LBPTjTMVUCouxux3h9avpRsfcvtZkR_HAh2nW8CyOM1wVx133fIoPqecug7FdGy90mHWcvGwxwGNrQFVA750YjdGa_kPCvkuYS1NkFYK8aIgyVVg7_fXX2VkEN7clqTnFl2Uh__1Qz_-4ohKxtQmW4jRyu2MgcAUI7I3-wvz--7x661n01cuwcxv3W29Tu5SzL3vdid1S3C1FKCk2SUeJfUrIU69XPIQ9i67oWNR10ullQNjsB9674FgJiS3JjlB1rtzuuQuL4X9mtF3T-19wjZ-sFnrXDjegxGH9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلمی عجیب از تجمعات چند شب پیش خرم آباد!
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/69217" target="_blank">📅 23:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69216">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">این گروه با گروهی که ما با آن سر و کار داریم فرق داشت. آنها قبلاً عذرخواهی کرده‌اند،</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69216" target="_blank">📅 23:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69215">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6df873441.mp4?token=eVGQWnyCoPG3_TaNnwj5AqEiFf_V6koW3tc9cupY2BhGSPqKKUDrhH7f7hkzLGQxtjQ4FJHsMyYXUUqHsogz6t1L4TsB1k4FI7HCm60LACOHxJ1zy-by6a_PKQQwnrNWl2RjUaOa4x8YAAH55lZJ33WWxnIswy_jBGeDtXd5DqR6ajlsTF1fHvai_SqERyw8EA2exbNmzxAJs87M4TpQyT5DQ7yEIPJHZ4aXvdQzEJ3e6yukPUDee8nNfh6N-vLyqP7WnVCWRz9GOmO6L71-vyj045-tiqem5XBh_oWwUqedeWh5doLWZ727LSSirDHnpKc5HqXAjHj9b1ehPUSjsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6df873441.mp4?token=eVGQWnyCoPG3_TaNnwj5AqEiFf_V6koW3tc9cupY2BhGSPqKKUDrhH7f7hkzLGQxtjQ4FJHsMyYXUUqHsogz6t1L4TsB1k4FI7HCm60LACOHxJ1zy-by6a_PKQQwnrNWl2RjUaOa4x8YAAH55lZJ33WWxnIswy_jBGeDtXd5DqR6ajlsTF1fHvai_SqERyw8EA2exbNmzxAJs87M4TpQyT5DQ7yEIPJHZ4aXvdQzEJ3e6yukPUDee8nNfh6N-vLyqP7WnVCWRz9GOmO6L71-vyj045-tiqem5XBh_oWwUqedeWh5doLWZ727LSSirDHnpKc5HqXAjHj9b1ehPUSjsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما ضربه بسیار سختی به آن‌ها خواهیم زد. این را می‌توانم بگویم، چرا که کار زیادی از دستشان برنمی‌آید.
این گروه با گروهی که ما با آن سر و کار داریم فرق داشت. آنها قبلاً عذرخواهی کرده‌اند، اما، می‌دانید، باید کمی آنها را تنبیه کنیم.
شی به شما گفته بود که چین هیچ‌گونه سلاحی به ایران نمی‌دهد یا نمی‌فروشد. گزارش جدیدی حاکی از آن است که ایران ۴۰۰ پرتابگر راکت از چین دریافت خواهد کرد. ترامپ: این موضوع تعجب‌آور خواهد بود. او به من گفته بود که در این کار مشارکت نمی‌کند. او می‌داند که من بسیار ناامید خواهم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69215" target="_blank">📅 23:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69214">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad144cccc8.mp4?token=TRisy0uKg6I4A64zhntW9aQueEEAJAFXdFq5Newzeq2PSpWwmz9G87BQsNBjJQUCt-3dz2sswclibZorIuBS_OU9GdNvyLsqG4voe1DnFfdqta2HtpCZC04EbcpWW5limMvzoWZEClmJ_4q4K3-okwSq9fBEa2PxiC2ivB22oZcPEbGVMo8ix65SBRbAA8w2TkjAa2rHXD1nUogL1kNEY8Rmf2SPu2r8LthwzE0RRwILhethR5aApQV2ZpMfzU0zCpECEVHXN4cxLQ_Lt06Wkm_tPrzxgczosgPMI4I3AZ7dlUvaHGWl3acLXA4vkpYchk3A4XPjP06VWoenYO2ZTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad144cccc8.mp4?token=TRisy0uKg6I4A64zhntW9aQueEEAJAFXdFq5Newzeq2PSpWwmz9G87BQsNBjJQUCt-3dz2sswclibZorIuBS_OU9GdNvyLsqG4voe1DnFfdqta2HtpCZC04EbcpWW5limMvzoWZEClmJ_4q4K3-okwSq9fBEa2PxiC2ivB22oZcPEbGVMo8ix65SBRbAA8w2TkjAa2rHXD1nUogL1kNEY8Rmf2SPu2r8LthwzE0RRwILhethR5aApQV2ZpMfzU0zCpECEVHXN4cxLQ_Lt06Wkm_tPrzxgczosgPMI4I3AZ7dlUvaHGWl3acLXA4vkpYchk3A4XPjP06VWoenYO2ZTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
این ویدیو رو بفرستید واسه اون تعداد از رفیق‌هاتون که عشق دعوان:
دیه‌ی شکستن کامل بینی : 2 میلیارد و 100 میلیون تومن
شکستن فک بالا : 160 میلیون تومن
شکستن فک پایین : 640 میلیون تومن
شکستن هر دندون : 105 میلیون تومن
شکستن دست : 160 تا 210 میلیون تومن
شکستن سر : 120 میلیون تومن
شکستن پا : 210 میلیون تومن
شکستن گوش : 350 میلیون تومن
کبودی صورت : 6 میلیون تومن
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/69214" target="_blank">📅 23:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69213">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3687c44382.mp4?token=B7Q4SO9FU2gjw0_dDbvB-EpJ9hLG3zr46jRIygUhRrppaTw-xkvXggXJHnAvfIkY5m5d_-91Vzm5fyOnQMYkDmreqeDv0jgGLAv8QdUazLE71WgfzHAZJmWxIxD_qKe6dwMTDXOlgXShXq8elYy9-XyedKahX4c8SRMDCCYQvWhj0QjT4XMXB11cwduE1Wf5sY9a-ASvI70zg1B7tMpSUljpSxzB05pHjo2zR_zVy0MfPqv-4_DnCgj-PMOHJ3-_m7p5rR7OyWTqEnhwGt8K64mBWBORGg114-zB63SnDzXACx-wXMz4p-z1Owtx52OIN7CgwCUuzVL_ZrK-1_X1Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3687c44382.mp4?token=B7Q4SO9FU2gjw0_dDbvB-EpJ9hLG3zr46jRIygUhRrppaTw-xkvXggXJHnAvfIkY5m5d_-91Vzm5fyOnQMYkDmreqeDv0jgGLAv8QdUazLE71WgfzHAZJmWxIxD_qKe6dwMTDXOlgXShXq8elYy9-XyedKahX4c8SRMDCCYQvWhj0QjT4XMXB11cwduE1Wf5sY9a-ASvI70zg1B7tMpSUljpSxzB05pHjo2zR_zVy0MfPqv-4_DnCgj-PMOHJ3-_m7p5rR7OyWTqEnhwGt8K64mBWBORGg114-zB63SnDzXACx-wXMz4p-z1Owtx52OIN7CgwCUuzVL_ZrK-1_X1Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما ضربه بسیار سختی به آن‌ها خواهیم زد، چرا که نوبت ماست که به آن‌ها ضربه بزنیم.
آن‌ها می‌دانند که این اتفاق در راه است و از ما می‌خواهند که چنین کاری نکنیم.
آن‌ها دیشب تلاش کردند با ۵ راکت به ما شلیک کنند؛ ما همه آن‌ها را رهگیری کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69213" target="_blank">📅 23:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69212">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ویدیو وایرال شده از یک پژو405 که درحال فرار از دست مامور هاست اونم بدون لاستیک!
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69212" target="_blank">📅 22:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69211">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYH7NaUtTmYHlZJC0wPLPs6N6mBia03dv4yBs1tqEXRHtOOm2f24fO52a6SjT1poUcAwaeL_2haHTC_KdVcku_umeMWISAgapyqQZT6lWA9kFAQkxZ0dg2skFqLdknVRKLz3d2kjYuVOTEWjN4ZFVoCB4fiItUvqTUemRjyJsfm44B20MHGcdRYQwug5NpWy6JajKFZBthZFZun79JcCd6hFHraLHvwa44e01MihKEwDy7TCYR7adj15u2oYxGzpV9eihWs5akhfBdbUfsW5MF7k-QxX8Zk8jdrdip9qErbh8M8tsjqHJhiZOXt54xC3UwlGkKw0O-JfYr8gIbNFMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله دیشب آمریکا به حشد شعبی عراق، ۵ تا از نیروهای سپاه قدس هم کشته شدن.  حالا حامیان حکومت میگن واسه اعدام اون جوونای اصفهانی خوشحالی کردیم، خدا چوبمون زد!  @News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69211" target="_blank">📅 21:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69210">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNSYLtcDsWyNeuHSROvwyV_GHtoM5l3T30xCfmgCvWYUzGn5RXIQcHdmkjX8M-nKrb5vPXhMGV0lIPzdWnBJkOUd0apmVIoGmaZKU3zaAIrgwW4e8Aduw-NGeZzs0-BXcflYkmC8AU8AiA5WyFKz-Gpo7TDVLjblf37CWoCEEuR2cyCsMICdNd1FjjedHRixrCNRDrNdr6oghmH2wOLrtzGeG0bftPbN4paxaJ82n5XYMbpnJ12E1LPB8scPSTmO9r8Uk-6zjT8_KtnOdvNaKePTjLtHOUG2W2obXsUx8GVw9Ndp_TOfbqFMU0fTyJfsFwYya6-J-aWzGrpsBS9W0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
❌
🇸🇦
نیویورک‌تایمز:
حدود ۲۰ مستشار ایرانی در جریان حملات شبانه آمریکا و عربستان به شبه‌نظامیان مورد حمایت ایران در عراق، کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69210" target="_blank">📅 21:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69209">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z6A6JRx29cQxpbKQt57YVrFhHyDOrQjXnnMzXeJ71v0mWdkfrtCV8KkeMreRthnPVb5z4vzx6vcyyCTiwB7kx3CpEe4GFbb84B76H0idl_x28OwFnE9bGnwzl8-kwFB18W-rvGZykDcv1YdX8rgkyYYDXfIPOgndwBwnCDd8TsHmH5Ni6BOajchEQtm-J0HTXAGIb7hfsM2zlpyxOxZVr7bQ_AonfysHl1P0HFsicxhBE_8Y3im3OZ0shGzSN0cUAWzx9OthATw2yey5xEOfbcGBLQKpoMgvO2zocySSgYWrgi2oSl3AuzjG8uD_fTICxvCuxB3450bxFUurZxRJeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله دیشب آمریکا به حشد شعبی عراق، ۵ تا از نیروهای سپاه قدس هم کشته شدن.
حالا حامیان حکومت میگن واسه اعدام اون جوونای اصفهانی خوشحالی کردیم، خدا چوبمون زد!
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69209" target="_blank">📅 21:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69208">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f736bc6e.mp4?token=eXQrAFHNJm3HMUOks09zQ9KkDJnEy9OAHR_7r8CXahhRJ8pUD_LUnqd65dXM28BtNbDfCrEqYpD_PLx3lPeS5EfguY0GMasqAoDDSqAPB2Tc-Z5w8q-t05lscQa93xwlPDL4779YbSq6lkICRGlEHYKInlSeAkc-6sb2gUm2GDcuNMzvjRkktPFIUYUQ5YpmSnRIfbmSiEJ16IrbE8gs-MfFeJp3Y50jsevjdXosxjT00AynZ5rCHbNta3c6tMT6iwAaZ0wqfuHkAppk1H-j8EPLrgJMNLZarRO3TiKMHogYnukMxpMSZfm9KaBqiy3btQ9tzuq4qesJTOGRk98TVje0QYZObEHhcOE_DXsQ_NrySRfwSqpdtWKAQWiy_xOs0O9F0R41vADSjaijMBocigTO4pyf8v75Rsz0xeP7zFOaKDCQOCiYNgFivhDA7dF4BtiUuJgq5Dt6KCqAW89MsfJH6uZJOZkChIY5IswkBkOpBzrKKfI4Xvlq6oNqVLKbbVdEOSuDD7kvgvXkOr3BHIiJhcNo4NY1M2AOe-dBL0UI2FSe-MYV3lmxJLnuWJ4qd-AkQn8uvMjW1Pk5v5A9fuq9qfacbLQSkiiL02prAlVAkhYALxRptNPJmTA-vL-sZ1iq9DXwTaCCe4TQUSzVJv3MhPnVCT2DaFMskp8JtYs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f736bc6e.mp4?token=eXQrAFHNJm3HMUOks09zQ9KkDJnEy9OAHR_7r8CXahhRJ8pUD_LUnqd65dXM28BtNbDfCrEqYpD_PLx3lPeS5EfguY0GMasqAoDDSqAPB2Tc-Z5w8q-t05lscQa93xwlPDL4779YbSq6lkICRGlEHYKInlSeAkc-6sb2gUm2GDcuNMzvjRkktPFIUYUQ5YpmSnRIfbmSiEJ16IrbE8gs-MfFeJp3Y50jsevjdXosxjT00AynZ5rCHbNta3c6tMT6iwAaZ0wqfuHkAppk1H-j8EPLrgJMNLZarRO3TiKMHogYnukMxpMSZfm9KaBqiy3btQ9tzuq4qesJTOGRk98TVje0QYZObEHhcOE_DXsQ_NrySRfwSqpdtWKAQWiy_xOs0O9F0R41vADSjaijMBocigTO4pyf8v75Rsz0xeP7zFOaKDCQOCiYNgFivhDA7dF4BtiUuJgq5Dt6KCqAW89MsfJH6uZJOZkChIY5IswkBkOpBzrKKfI4Xvlq6oNqVLKbbVdEOSuDD7kvgvXkOr3BHIiJhcNo4NY1M2AOe-dBL0UI2FSe-MYV3lmxJLnuWJ4qd-AkQn8uvMjW1Pk5v5A9fuq9qfacbLQSkiiL02prAlVAkhYALxRptNPJmTA-vL-sZ1iq9DXwTaCCe4TQUSzVJv3MhPnVCT2DaFMskp8JtYs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کشتی ترابری گاز آمریکا نزدیک بندر دمیاط مصر با پهپاد هدف قرار گرفت
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69208" target="_blank">📅 20:52 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 22:19:56</div>
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
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/news_hut/69324" target="_blank">📅 20:45 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/69323" target="_blank">📅 19:58 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/news_hut/69322" target="_blank">📅 19:56 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/69321" target="_blank">📅 19:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69320">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">املاکی تو یه جمله همزمان گفت هم می‌خوایم خیلی شدید به اونا ضربه بزنیم و هم می‌خوایم خیلی مهربون باشیم باهاشون
🤡
#hjAly‌</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/69320" target="_blank">📅 19:50 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/69319" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/69318" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/69314" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69313">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: به زودی، دیگر چیزی از ظرفیت نظامی ایران باقی نخواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/69313" target="_blank">📅 19:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69312">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ایران در تعامل با ما صادق نبوده است
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/69312" target="_blank">📅 19:29 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/69311" target="_blank">📅 19:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69310">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQTmxReds7fgMeWH9GnXjd-JT4rmg9K2NKc6oLpyi0n6KoIMkvRT4dGsk6rTVIAJ_TqX6AjK18z2-XDYYje6Ls1uFUgOfJ-teHqVvZAFE5eAU2wgf4PNPBD9ZHmQcFRm2fcomp55ecGSvF6MYC3YuQGiqLwbTqufnbYi3Pzfv3S4kmodOuRxSjiMp5yS-AHX4c777pVxxhA0H_OkPhfcEdqnNjlmIZvRdJNOCuhVCZmu96GuPXcwoPASPD2_rNKs_C8mynKpY9z50BKujZrHOWTz3AjVAY9viyNe76uYCNRQC0ZzWn1dJCJ8QrhGcASEPylrqpzycLebbZynRdR_vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نهاد مدیریت آبراهه خلیج فارس:
به علت تداوم اقدامات تجاوزکارانه نیروهای نظامی ایالات متحده در منطقه، تردد از تنگه هرمز امکان‌پذیر نمی‌باشد. به محض برقراری ثبات و آرامش، کلیه درخواستها بر اساس ترتیب و زمان‌بندی بررسی و مجوزها به مرور صادر خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/69310" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69309">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
حملات پهبادی به جزیره بوبیان کویت
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/69309" target="_blank">📅 18:40 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/69308" target="_blank">📅 18:14 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/69307" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/69306" target="_blank">📅 17:20 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/69304" target="_blank">📅 16:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69303">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNEoa3z83DhAmzHX79exkK9qm8caMwF6_7-43V3W11mOpO16TUjW6oYvzNnOtBDb6sFSBgN5grLxLYFwLspNngtuW_HLTrfFibu3cy5gjzKo4A1C3iu2XY-VJ6Rn5kXgWofx3NdaiaZ2je0neZlXIJ61Mi5eFItEexiZDzp3wX_syg9v2EpSgvSZtzmOYO7-7qDNa4dwyIGhQ9lAiXIVL558iP4TdrLO0DW3pcI3ZvaCiR7XEpLpeBlpyIZl86JzVPeR8h_i-lo7OzfT7_TdAidV1Um67Ni2jm1mm9dK5mSqt1quvtRQ2AwcBDkYTnEuxnCyjfbisRhx4UnTQ-QMhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پسر رئیس بانک سپه که دهه هشتادیه معاون بانک دی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69303" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69302">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8NeSNiyKb32_RQNTDM59neCnqvszEa8JrO0kuUUikVI5PBoYg5oikd3FmNmN6gHu6vxAkYayhg_ZOtPqx0x0jqNmDpjAIFCd7AgPtuZc9Aamj5OLojLUjSUerFVx1IFw51Nir0nrmltra0cIcYI-c1SIlPQYar8r9CR9GdRnQGbWlJeoAza1JgnG2h2nZ4CcYddgrF0mik5SlUjmkqNaYuf3ziiyMkMLTHQeITyLwK8tcP8i0QqmvFHEdrgwflc8AN_Uutvz43v9JlFphcI0cKmbEg9DwiRuatigOU4SYPnyOlpNTZbATHH3_tVKuB0-nR85wyvcXDwxH0Tp6DqQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
طبق داده های نت بلاکس دولت ترکیه اینترنت کل مردم رو قطع کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69302" target="_blank">📅 15:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69301">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7EQj8kxrsTojZKJDXGR5jUi5ZmuysMN1JRiPcNPBkG752Fmsy3Yo4-RY6efs7hrIsmTjigTnkbvZcUTrPUSLO-Q2Jk6ghx97gEIhMY2uVHnJZ6BK4LrCiAEUJkM2fv8ji3_sm3cHKQa8R7tFAcGWwdl6SDrWupvZhV_MmcZkibXBfZbZP8wChpUME0d1518PzdrcQ25SA05QvlyLn7NuQWXDUt14VOR68QHh_oUN9iuCgl_JaroI7NaHVV0wgoCIil5rkknqEEqY0QRYWAItnaCuga1JbatQAEiC1piPzkGnBhh9AnYZgDOPB0E8J1JPsNLLgzzBTLRvpHlkQ-Oqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
گاردین:
عربستان داره خودشو برای یه عملیات نظامی گسترده دریایی و احتمالا زمینی، علیه حوثی‌های یمن آماده میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69301" target="_blank">📅 15:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69300">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🇺🇸
رویترز:
پرزیدنت ترامپ امروز در کمپ دیوید با مقامات ارشد دولت، تیم امنیت ملی و فرماندهان نظامی دیدار خواهد کرد تا درباره مسائل مختلف و از جمله جنگ ایران گفتگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69300" target="_blank">📅 15:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69299">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb0ff0fef7.mp4?token=lSGtfsg0_5liTc5CMbG4G_F5wmISzGLZYJ4x6FJ-iAg7bSI5SdXgZmdo_BKaNvgXvg9rNQlEeLRcxVN0FePcmQwVZavVpKBWPJX4Fo653W8-cnLuFqNQdBYQPls0ESYZvwbDaxFvvprgUaNJpVBY2hZ5gDCl2Ihsd40G8jEb42XUMFzcv_1ujynXDZKPFGamvcNMdvJWodt_NO6InGq1HB_vmiyQjcU7o3E0C03VP8yRHkog0kdURRVQst1oXbTlF9q-fAFwWRGwGhSpfSxeaVRKrLrahUULWmkbej9QAJAKLDwvOfQEvZFJKn9sN4tZ0oJkC9b4lR3WObh2jA6qNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb0ff0fef7.mp4?token=lSGtfsg0_5liTc5CMbG4G_F5wmISzGLZYJ4x6FJ-iAg7bSI5SdXgZmdo_BKaNvgXvg9rNQlEeLRcxVN0FePcmQwVZavVpKBWPJX4Fo653W8-cnLuFqNQdBYQPls0ESYZvwbDaxFvvprgUaNJpVBY2hZ5gDCl2Ihsd40G8jEb42XUMFzcv_1ujynXDZKPFGamvcNMdvJWodt_NO6InGq1HB_vmiyQjcU7o3E0C03VP8yRHkog0kdURRVQst1oXbTlF9q-fAFwWRGwGhSpfSxeaVRKrLrahUULWmkbej9QAJAKLDwvOfQEvZFJKn9sN4tZ0oJkC9b4lR3WObh2jA6qNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69299" target="_blank">📅 14:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69298">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🇮🇱
وزیر دفاع اسرائیل ، یسرائیل کاتز:
اگر ترامپ از ما بخواهد، به حمله به ايران ملحق خواهیم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69298" target="_blank">📅 14:14 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69297" target="_blank">📅 13:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69296">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37edae9b59.mp4?token=ZjWZNVX7sfmjE0g7NlVibZ8_08YcTLoaXEacb-aSZjO9wbu54dV1vhLdkKFAJM9i9VZBmxaiX4ej8Kn4I1DtLi7hBrNLB1SGnPp2YNftMUpcgz2iHx4vwsH28nUUiLOY-GKiW30hdNzHTSOfNeRYNWHQSEKEwI5wXZ3qYblA7ynzc6CQtRn4xwq1KKG69D57chQYvAiUsgezSymhj2PSChKEh0xUsH18Z8i51B9rlMRoRxsMBnifpCRK66Pea041qMlKqOq4ON2rqw6We8wxI5xfzjoJVZzF70R-2-H-6SlgHnouXJ9qHK8RepOPyCR8Qq67MzPFgLdUnveUVwA5Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37edae9b59.mp4?token=ZjWZNVX7sfmjE0g7NlVibZ8_08YcTLoaXEacb-aSZjO9wbu54dV1vhLdkKFAJM9i9VZBmxaiX4ej8Kn4I1DtLi7hBrNLB1SGnPp2YNftMUpcgz2iHx4vwsH28nUUiLOY-GKiW30hdNzHTSOfNeRYNWHQSEKEwI5wXZ3qYblA7ynzc6CQtRn4xwq1KKG69D57chQYvAiUsgezSymhj2PSChKEh0xUsH18Z8i51B9rlMRoRxsMBnifpCRK66Pea041qMlKqOq4ON2rqw6We8wxI5xfzjoJVZzF70R-2-H-6SlgHnouXJ9qHK8RepOPyCR8Qq67MzPFgLdUnveUVwA5Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
روابط عمومی سپاه پاسداران:
ساعات ابتدایی امروز  ۲ نفتکش متخلف به خیال اینکه میتوانند از مسیر غیراعلامی ما، تحت اسکورت هوایی ارتش کودک‌کش امریکا عبور کنند، بدون توجه به اخطارهای ما، در مسیر ناامن و غیرقانونی حرکت کردند که مورد اصابت قرار گرفته و متوقف شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69296" target="_blank">📅 13:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69294">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WN0bGlbrSHUJyW6kt4JZqOio16tYtgn-N_986P2CLZ6WD8sVzWkvK2cyRKnhU4Hj6GM-VBotYuYhr15GFiC1lTNZIi9YvH-9YMoJpGDiuW-16XhGi0mv9WgCvaPuPHYJvnAcVGBZ7s1K1NYTR1q_BiPNKojfGCc6Af2Eot4sjW-4hZxclMK5p9Q8CUsEuopM_gSNzZm5G_nNxP43APECVIfa85hFycQOGdNUphM1-bZ8gG2gkqjTcErWdFaKJuvQfXlJ0-VYySnjNgw7N6OvmijbESp9MVydmSxKifioA_If50yNbHDIMoutogHnKUtA0N-j_lBE_unl4FrGq6FWCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bb843e99ad.mp4?token=k7h51E68y6hVaFszJywXOkSw5MwgPeGbyBpWZVH4H0HvE-a0imSegburo-XxXklFH1XuWpfpOk-QXRyqL4qaGnhLiIvjuax8HwYzrq70CohLRn_b-Zy9kbRStzzu6V9tLpWGYyC2Cjwyk7zSfL2ii8RiLCOygJHvMs4vLcJekxM07dYSZl3tmiOCUzS-xz4SZhPpq7W21vVBmUwVYuMqgA5h4Yrc3sOW-25bk9YidXnZ6Qr-HEs_9iOcT8HKnVHzgQZ5KolBnNaSjypKJENT7b9b81LA-jAL_d_EH3CweVfqZk3NMs02N2PY-r5ChNG2pD8a3tzP2UT7zEjpJwY2kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bb843e99ad.mp4?token=k7h51E68y6hVaFszJywXOkSw5MwgPeGbyBpWZVH4H0HvE-a0imSegburo-XxXklFH1XuWpfpOk-QXRyqL4qaGnhLiIvjuax8HwYzrq70CohLRn_b-Zy9kbRStzzu6V9tLpWGYyC2Cjwyk7zSfL2ii8RiLCOygJHvMs4vLcJekxM07dYSZl3tmiOCUzS-xz4SZhPpq7W21vVBmUwVYuMqgA5h4Yrc3sOW-25bk9YidXnZ6Qr-HEs_9iOcT8HKnVHzgQZ5KolBnNaSjypKJENT7b9b81LA-jAL_d_EH3CweVfqZk3NMs02N2PY-r5ChNG2pD8a3tzP2UT7zEjpJwY2kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای توی کربلا در حال پخش شربت دیده شده
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69294" target="_blank">📅 12:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69293">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmfI1lGjl2BbjCC8vnQzr5U4Jz4l1FT0OL6yHbZ5NBrHVN9NPd3ef76Irch3Wp8TqkOFFodavBUXYKmfQgevlsVYGERLMlC_-725uEFxiFWLlMkiTE5QErWI8vaKYdqljRdHKlspz1vS0D12v9mvASmT0PT-oHvR9JpmROEYnMZwNrwHYCFC8SeJDvdlwSc66h3uX8pPPRrmSZIMIUq-zQx4ZwGzVUFWOEnNB1GUMl2tl6wzNcHEK5t-Z1qmWE7LJGHIJO5W81dknyGkSLW9LLX3w9oQD6jXGhjLasvsXfMB_POh-zntrdowbE57loBoRRAuZoTJe2Q9a7zPmSroKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
گاردین:
یک موشک بالستیک روسی کارخانه تولید پهپاد در کی‌یف را که متعلق به شرکت «ترمینال اتونومی» (Terminal Autonomy) —شرکتی ثبت‌شده در ایالات متحده— بود، منهدم کرد؛ این نخستین حمله شناخته‌شده روسیه به شرکتی با مالکیت آمریکایی در اوکراین محسوب می‌شود.
این کارخانه پهپادهای تهاجمی مجهز به هوش مصنوعی تولید می‌کرد و گزارشی مبنی بر تلفات جانی در این حادثه منتشر نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69293" target="_blank">📅 12:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69292">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B30Fe8vqiQNDosDH78RNo6gSTMR7IkCtYtQB23kznDxQyq4haS0FmFeoukpqIPBjVrbX_zqUzCnXpTxqqOneI58VGfAWciC20dg8zJf4oQlnap_v1pPc8Oc6qtTlZ4Tl1pvR2es587tkPgdAlIf4d3etNRCUgL5xoYq8knlDVgBJAOVaSqE-1D5dgwdpC4oUvZ7UVKO_dvXE4YtqL6dw9IaVdHlIEBE6Lm-Zbz-NpbmLWV8KjAkJRiJC3XFszH3CvcUqzAhGS6hEX0UdcbnceS6F9-uxPy-CHkjKMJSI3_2OoXlDCwUQUEhVR-pIqw7kbThdbeCZNcCCxH720C6Jsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
به گفته یک منبع آگاه، مقامات سپاه پاسداران از هیئت حماس که برای مراسم خاکسپاری علی خامنه‌ای، رهبر عالی پیشین، به ایران سفر کرده بود، خواستند که در امضای توافق‌نامه عجله نکنند و وقت بخرند.
یک مقام ارشد آمریکایی مدعی شد که ایران تلاش کرد حماس را متقاعد کند تا این توافق را امضا نکند، اما این گروه تصمیم گرفت به این توصیه عمل نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69292" target="_blank">📅 11:31 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69291" target="_blank">📅 11:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69290">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NENrj_j_ZF2uOFOUqZ8HbFUpXA6HAfdf0ZxQo3o6iWqD4LVZVnYlnJJFtE7X8fUvN8MjOA9wOieoaL61nKcaKjmaUM9hA5rQmhq7ZKITOEESsCevnwbR4Ju0oIWv_jeG2WD8Rm0LNHgQ5GtvKGHtHg1eS5-TFpq2jBrH01IpDw7nWXAhjBlhN5KAlsShszp56771tdGggmxoYHNGBIGRABnI_ZFxfC0HTL5iTVAXPzEj7Ss2T0aldbhtTU6uvbKqjJcT1kO_F3XFrLApjZYWrGW7j0It-iSqljeUux8FgWuml2V0OCsKowLW6-uAf5IvPTtBL8D65zlfIMwPCMGR5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇱
🇮🇷
تایمز:سازمان سیا و موساد اسرائیل در حال تشدید جستجوی خود برای یافتن آیت‌الله مجتبی خامنه‌ای، رهبر جدید ایران، هستند که از زمان جانشینی پدرش پس از حمله هوایی فوریه ۲۰۲۶، در ملاء عام دیده نشده است.
مقامات اطلاعاتی معتقدند که او در این حمله به شدت مجروح شده است، بیش از ۱۵۰ روز از استفاده از تلفن یا لپ‌تاپ خودداری کرده و در یک پناهگاه زیرزمینی به شدت محافظت‌شده، احتمالاً در تهران یا نزدیک قم، پنهان شده است.
با توجه به اینکه نظارت الکترونیکی سرنخ‌های کمی به دست می‌دهد، جستجو از اطلاعات سایبری به اطلاعات انسانی تغییر یافته است.
مقامات سابق موساد می‌گویند که اعتقاد بر این است که مجتبی از طریق چندین لایه پیک ناخواسته که پیام‌های دست‌نویس حمل می‌کنند، ارتباط برقرار می‌کند و نفوذ به حلقه داخلی او تنها راه واقع‌بینانه برای تأیید موقعیت مکانی او - یا حتی اینکه آیا هنوز زنده است یا خیر - است.
برخی از چهره‌های اطلاعاتی گمان می‌کنند که سپاه پاسداران ممکن است مرگ او را پنهان کند، در حالی که برخی دیگر هشدار می‌دهند که رژیم ممکن است از بدل‌ها برای پنهان کردن حرکات او استفاده کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69290" target="_blank">📅 10:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69289">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9be197f29.mp4?token=rT6SEYZ83iErnQyjI1EXyT9yCVDb63Bc3gbCFPxFBwOqU-oal4smphW-xFE_23AaDqv9zL1C4V6FT3jW1_jLMbVaPSMhE1tBBXDxwKhrJma4kKeID05fKYFgvA5W94juACeKO5vvXQ86tc29xv8UU9hLgs7ZtiVY0dH55DzC0zhJyECYHvXWLpqgVT1nT2LDgDmay7RgdwWlMKM-C16hv1thRLOO9MzHxzctvhj3Hojj1mB0vHStq0GXqsSMlsxuGvbaiREbbnRrpWmcEd9Cd5gtmPJHc-lpkRImmhtX7bqeJv48UzMkmb6-O06jP_4P4HkpP-K2DH313uOblItZqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9be197f29.mp4?token=rT6SEYZ83iErnQyjI1EXyT9yCVDb63Bc3gbCFPxFBwOqU-oal4smphW-xFE_23AaDqv9zL1C4V6FT3jW1_jLMbVaPSMhE1tBBXDxwKhrJma4kKeID05fKYFgvA5W94juACeKO5vvXQ86tc29xv8UU9hLgs7ZtiVY0dH55DzC0zhJyECYHvXWLpqgVT1nT2LDgDmay7RgdwWlMKM-C16hv1thRLOO9MzHxzctvhj3Hojj1mB0vHStq0GXqsSMlsxuGvbaiREbbnRrpWmcEd9Cd5gtmPJHc-lpkRImmhtX7bqeJv48UzMkmb6-O06jP_4P4HkpP-K2DH313uOblItZqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از حمله عجیب طرفداران حکومت به بنر ترامپ و نتانیاهو
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69289" target="_blank">📅 09:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69288">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‼️
دلایل سقوط شوروی که صداوسیما پخش کرد در مقایسه با وضعیت الان ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69288" target="_blank">📅 09:15 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69287" target="_blank">📅 02:26 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69286" target="_blank">📅 02:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69284">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGUn5v1VkJXbjS8hlflw4WDgDsSQMLxGfyT4zYMKSmSzAXhgIfrxbQGm4bM_XCerCsfcMgf89i-cZpsalpPVc9D_1wC_KeQI0VSTXHLwhYR3ZHeLmpp1eIjSYhonEFU6xKmepB-7Am-lcJfd_51OAAWNeVK_-EBWIPr5IZWHVZKlBcR-qMGTLHsl2udbWbexGZcFq1tgxSEWM2C4lHMSVIlxFN2DOO6C-nQR27eP7mEzyTSmZfLAu2gx1oCEDprpyenujFklMUS6-R5H3huKSjfugmJI2nvmBftwY9GeUOaS851bf9UQjxrYluDMUWpYliXgiA2zmxqNHL3rKKf0KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=hkPUzFbLeRB98n-BBKxIuelqbhpz5zIdubqMpF9LZCfigzGR0QubUfsRZjYX7Y9-jKLNXlu2bGJEwziu0rw7m5Ob1TlkMy2WNzkM5IMfmSjIA0A70T4EyyMpttnu4L3bcFFneYNeqhf2-JBwaJqk_YrmxQc2wM4jPG8gPGgNVSQrLCp-HRx68Mg8FZ-g9gvE9is5_FMOXGk264uFTQIdKIRMkgNZdA3e4eU-LyFYRFt5rhpU6luYiAk9CifOOj6_Sk5gCCYcwjRhRNTjLUiqKSUr82Njo_WaClttJhFsHjqYrRcYFM4sxnC7gLn3-9zDL_MKITLPTwWhhQy9_8RDKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=hkPUzFbLeRB98n-BBKxIuelqbhpz5zIdubqMpF9LZCfigzGR0QubUfsRZjYX7Y9-jKLNXlu2bGJEwziu0rw7m5Ob1TlkMy2WNzkM5IMfmSjIA0A70T4EyyMpttnu4L3bcFFneYNeqhf2-JBwaJqk_YrmxQc2wM4jPG8gPGgNVSQrLCp-HRx68Mg8FZ-g9gvE9is5_FMOXGk264uFTQIdKIRMkgNZdA3e4eU-LyFYRFt5rhpU6luYiAk9CifOOj6_Sk5gCCYcwjRhRNTjLUiqKSUr82Njo_WaClttJhFsHjqYrRcYFM4sxnC7gLn3-9zDL_MKITLPTwWhhQy9_8RDKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیدار عجیب نتانیاهو با یک سناتور!
امروز نتانیاهو با جان فترمن دیدار کرد و طرف با شرتک نشیته بود و سرش کلا تو گوشی بود
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69284" target="_blank">📅 01:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69283">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">عجب سکوتیه، موشکی راکتی چیزی نداریم؟
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69283" target="_blank">📅 01:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69282">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromلیوه</strong></div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69282" target="_blank">📅 01:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69281">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">عجب سکوتیه، موشکی راکتی چیزی نداریم؟
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69281" target="_blank">📅 01:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69280">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">▶️
تیزر جدیدی از سینمایی Spider-Man: Brand New Day منتشر شده که دیدنش خالی از لطف نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69280" target="_blank">📅 01:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69279">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEKsccyXcKNF4bptpozrCMFhy_jqd_Ps0FRSarOHWC5PjTvqLcaC2olMQI_2cnsXjORONRbwCdqQLTX3g51uM05BMy8g4zVgoqzLNLI5l4b39hqwa5A7pRH3BgSMVyJwWFXzGz_kU3XTDs4TbghBOVc1f00LbVVgoHkiXSQ3JyajDa7ERwXFWOP01ck9eiCGFGCvrICGzTaFDbNMw3EtagLHFgxchWlaG_Roo-DNl3plEDyJK57qMvhTS3uR4NGV2L9b-zf6CGFo8GOzEXNm-ttXlX579WW_l4_8ddJxc2jMUNs8R6F9lvPYuWIGAoovISK49HsDm1uduihRyAHQ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
«آمریکا هر روز یه جنایت جدید انجام میده. حمله به خونه‌های مردم عادی توی جزیره قشم، ادامه همون جنایت‌هاییه که قبلاً توی لبنان و غزه انجام داده.
آمریکایی‌ها عادت دارن هر وقت توی میدان نبرد کم میارن، با ریختن خون آدم‌های بی‌گناه جبرانش کنن.
ولی بابت این کارشون، تاوان پس میدن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69279" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69278">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba260d124.mp4?token=cK2FfVkp-RZdie75YbdcOtVA00smWHxcr5UA3-dERxIrt1l6pAl0WQ7H53tivEXnwOmhgy9pYfVb0TFarw6jqePIqxcXnuhF1UbKaxTaoFlShPLsLfuprXsUt49HZSFW4vaYD7xxUqjLrOL23IrELL6IAElHdgq1K0w59Y_tbwALJyGWud2N1ofSck89n3ECyXTjfOX3hKvFVxJmN-UHJiCo4cw8iD9Q8tnZfQcuPpMVmNmnquHpBs0JvHzeNifV3zfCeMltsPQmkpNBWG5umysV_O_IoOsJmDRoTzYIPwiiFvIdHtRw-_fA-jeuOEOxqPeJkAQSmbg1UW2HJ8zgIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba260d124.mp4?token=cK2FfVkp-RZdie75YbdcOtVA00smWHxcr5UA3-dERxIrt1l6pAl0WQ7H53tivEXnwOmhgy9pYfVb0TFarw6jqePIqxcXnuhF1UbKaxTaoFlShPLsLfuprXsUt49HZSFW4vaYD7xxUqjLrOL23IrELL6IAElHdgq1K0w59Y_tbwALJyGWud2N1ofSck89n3ECyXTjfOX3hKvFVxJmN-UHJiCo4cw8iD9Q8tnZfQcuPpMVmNmnquHpBs0JvHzeNifV3zfCeMltsPQmkpNBWG5umysV_O_IoOsJmDRoTzYIPwiiFvIdHtRw-_fA-jeuOEOxqPeJkAQSmbg1UW2HJ8zgIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سنتکام:
یک فروند هواپیمای P-8 Poseidon(هواپیمای شناسایی تخصصی) نیروی دریایی ایالات متحده در حین گشت‌زنی در خاورمیانه، برای سوخت‌گیری به یک فروند هواپیمای KC-135 Stratotanker نیروی هوایی ایالات متحده نزدیک می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69278" target="_blank">📅 00:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69277">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLrAyjVS782JXJ68V-wvTFEv1TSh-Ru6An-h8ZZIc-60W9yfNjv1ciEdccOh0Dsb9ngY_nS4YSgslkU7HZCJcSPHg2aIYGq_WLol7GD2bozAYutGg5hKt1JxMHSEZjiWUN-7kyRKMcx4ETW7KBswyf-Y8CvdwMM056sZE3LwqcXzhfb4umhTEgzesphYCqH-5HcmwC5jW3Y346E1CWKDk91t22M7FCk17DAAtINvAlJ_1SJR9XQvQJAVQI4h_XBrsXU1LtNjt7cydLIhLIJoMeKCF9mYs4tUeVdJo0CYyH1bF-yGsk_f73EnRFRRn4IZEiICrxqKEX478lQHsJBBbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آی‌24نیوز:
اسرائیل کاتس، وزیر دفاع اسرائیل، روز پنج‌شنبه به همراه ایال زامیر، رئیس ستاد کل ارتش، جلسه‌ای برای ارزیابی وضعیت امنیتی برگزار کرد.
در این جلسه، تصویری از وضعیت اطلاعاتی و عملیاتی، سطح آمادگی ارتش و طرح‌های عملیاتی برای سناریوهای گوناگون در عرصه‌های مختلف به کاتس ارائه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69277" target="_blank">📅 23:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69276">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89da715482.mp4?token=YbNwGF5Sauc2VUrh45W9ZmaE6ADYvppTb1lyGGW1gvBnjZAM2TVtExy4yngH-Vl7sKMdgbf45UW_EWWQuu-LFqNsiruwsWJ8SchQeWRzdENDbIUSd120g7et98yDn2Agx2vpTzznYx7igPuQDVct7v2GNP4GFkwNoWHrKKNhVtz7gptfM_U9FbFYNuSEQ3SPzQox1EBUW2BQyYmqTMlIQMdQXE_MdjOsXeL860B-2EC9Pa-GpwuxqPGItME-T9gFsR_rKwMtwN-72Cm9BH-ZKAzrSEYz3JSYMz8p7qo69xpQGLl68qryDglGNaoMRCuw0DmQ2LUGq09QAYc2gsWAzw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89da715482.mp4?token=YbNwGF5Sauc2VUrh45W9ZmaE6ADYvppTb1lyGGW1gvBnjZAM2TVtExy4yngH-Vl7sKMdgbf45UW_EWWQuu-LFqNsiruwsWJ8SchQeWRzdENDbIUSd120g7et98yDn2Agx2vpTzznYx7igPuQDVct7v2GNP4GFkwNoWHrKKNhVtz7gptfM_U9FbFYNuSEQ3SPzQox1EBUW2BQyYmqTMlIQMdQXE_MdjOsXeL860B-2EC9Pa-GpwuxqPGItME-T9gFsR_rKwMtwN-72Cm9BH-ZKAzrSEYz3JSYMz8p7qo69xpQGLl68qryDglGNaoMRCuw0DmQ2LUGq09QAYc2gsWAzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69276" target="_blank">📅 23:40 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69275" target="_blank">📅 23:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69274">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vY-E6oYEkHGAGBzOvLZfriS-THLsLljfcmPoNcw_sZCK5YDUP2htaIdEEtVgFF8vs9fbPIIQulLYfQ_2LBOfW1Q4teJQ0JFJmFpAvwsLotdf4dOwfhZrpY3QngG4H5QLFcyjVedSNaFqT4C7IZqgXYTOb-bHvqPuGJBNKVo3EZB8JvTpu91d2cdAYlXq6H5IpZuYXcv6UHdM9PRgea7uAt8pMgmCKvBTZX9kMMimXHLXJfmi6GJid6JeA915OMdr7UF6iYW-bN7B7Pa8nmmOQpyYcGHMtHTS4yc_hX1dTOqiTLYYgP3gxeAZhBhof8nPlt4KYv5c-Ph5z03s7ZP3aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعدام می‌کنید؟ به‌به چه کتلت های تر و تازه‌ای داریم امشب  #hjAly</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69274" target="_blank">📅 23:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69273">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3fe31b5c.mp4?token=D_nMj9J2S-M2_2aUvqdOBl3t_2q2ZFjBlagMGSqY1wTwAZnE02vH4UAHMcroXgYp6KXFcwogfgyOu7L6AVoBGr-eFChiVIDtO4HM872vyvAgftADKStthu-wwOhvoV-xfH5awb_D6rZSUUcAiANQXvxpVSfaut3phFov5ify8MudS60TrJSvIHOg5IajkCjStnNjESQhzib47V3C7y8OXuISEPbQxGbasjvGqLA9tyW203Q_ipzhwuyLvhSmbYHXhJ47PT53qJqkVGH1IR9A4F-mka-G37oidKvlwqagRadCv4xeDVERPl63S9hx6fKg1YhjBnmStPLeA5o23NSi6glHjp_PMj7a3pWv0MAMvoU2Ynu9lEkk9FcnmruHWm3PSOYyqtfcylT29Kf3Q4nJUPBneYhLxFpIXZMwjFHRg-jjUxlu-I4cBl0YJWNMS0QwI94N49314Af5QhTLNz4GS8hsPe71uiUWGzh1elP-8DUgbLyU6Skky5dEh6t7ZbufQm5IQQb_foah979h-SZ7uS2LBzLL5opjk7DvIyhM0EZepGGCY_5Z9DdeVVEtcqQWLVp2KbX_muruc4JOd12dgoE8FCZNMUEBSytDLeOhWXD0l_5k6j4VA3eJGOV9ziqivmbqDi_ouNXfyFarLWKQ4aVef-7vi78BiR0hCVFJJDo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3fe31b5c.mp4?token=D_nMj9J2S-M2_2aUvqdOBl3t_2q2ZFjBlagMGSqY1wTwAZnE02vH4UAHMcroXgYp6KXFcwogfgyOu7L6AVoBGr-eFChiVIDtO4HM872vyvAgftADKStthu-wwOhvoV-xfH5awb_D6rZSUUcAiANQXvxpVSfaut3phFov5ify8MudS60TrJSvIHOg5IajkCjStnNjESQhzib47V3C7y8OXuISEPbQxGbasjvGqLA9tyW203Q_ipzhwuyLvhSmbYHXhJ47PT53qJqkVGH1IR9A4F-mka-G37oidKvlwqagRadCv4xeDVERPl63S9hx6fKg1YhjBnmStPLeA5o23NSi6glHjp_PMj7a3pWv0MAMvoU2Ynu9lEkk9FcnmruHWm3PSOYyqtfcylT29Kf3Q4nJUPBneYhLxFpIXZMwjFHRg-jjUxlu-I4cBl0YJWNMS0QwI94N49314Af5QhTLNz4GS8hsPe71uiUWGzh1elP-8DUgbLyU6Skky5dEh6t7ZbufQm5IQQb_foah979h-SZ7uS2LBzLL5opjk7DvIyhM0EZepGGCY_5Z9DdeVVEtcqQWLVp2KbX_muruc4JOd12dgoE8FCZNMUEBSytDLeOhWXD0l_5k6j4VA3eJGOV9ziqivmbqDi_ouNXfyFarLWKQ4aVef-7vi78BiR0hCVFJJDo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کویتی‌پور، معروف‌ترین مداح دوران جنگ ایران و عراق، دیگه حتی مداحی گوش نمیده
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/69273" target="_blank">📅 22:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69272">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlXBj26fM0fV9HjLURByu7H4xtKEGJCiPr88ypu1uJKeR-VUgDfZAA1vWWB4PgiBq1N6DoYwTZGq1ZXsfzfPELgYes_zF9cRq4C1K0TzGd2cFlt52Yqhb2ccIiaEUsM75BcTkcExJNmWxpc7HZrAmMOH8ae15XRF25DNFoG2JkM-VcsSdwvczLo3z90599Uv12HeOw5uGOTvGtPyh3dl9tHHDiqkGqjKuSUz-AC91XDAU8Ro90qwiCOAdoarG6DLdencHFMs_T_ww3oe8WwymdAf0ufkyTgfjDer4liswTFiLpgrmPQf3BgiWYwEPqAlxPeSggSSqgp51OO-_9dU9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😄
مالک تلگرام ، پاول دورف :  روسیه به‌دلیل اینکه حاضر نشدم خواسته‌هایش برای نظارت گسترده و سانسور در تلگرام را بپذیرم، مرا در فهرست «تروریست‌ها» قرار داده است. طبق قوانین روسیه، من از «انتشار هرگونه اطلاعات در اینترنت» منع شده‌ام.  ظاهراً مقام‌های روسیه هنوز…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69272" target="_blank">📅 21:58 · 08 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/b7ad22e432.mp4?token=EbujmHSzWnN1tIupNuYzqhn2oqgfCqXS8ZYxTgrhkCKcCrW3ay-pRCQ48aaatLnTNe1hX4dr5mKWMn_pNFVdH2Tb0aA41ed3kd3pFLhHIumgS1GrDNnnpu4rC6GvXfYWo-pZ9vSSxkX6hKsvGMR_tBPhUv7VY9MBk3gZZUIBx4ZLmsI4S_3Ot2X1T32a7kt0T1F8MKqTeP7u4GcmEilz9C27pY9E2RLxvWheC726jRgOLFULSK4k6Yix85ce5pzXysOiBGjh4Hn1gsJME0ECeSBNZ6ivYsxZw0D4n8C398KFJ-BpR3PAUbrceirS1sBP7S2xh-_sXoFKKFiPGl9dXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7ad22e432.mp4?token=EbujmHSzWnN1tIupNuYzqhn2oqgfCqXS8ZYxTgrhkCKcCrW3ay-pRCQ48aaatLnTNe1hX4dr5mKWMn_pNFVdH2Tb0aA41ed3kd3pFLhHIumgS1GrDNnnpu4rC6GvXfYWo-pZ9vSSxkX6hKsvGMR_tBPhUv7VY9MBk3gZZUIBx4ZLmsI4S_3Ot2X1T32a7kt0T1F8MKqTeP7u4GcmEilz9C27pY9E2RLxvWheC726jRgOLFULSK4k6Yix85ce5pzXysOiBGjh4Hn1gsJME0ECeSBNZ6ivYsxZw0D4n8C398KFJ-BpR3PAUbrceirS1sBP7S2xh-_sXoFKKFiPGl9dXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69268" target="_blank">📅 20:50 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69267" target="_blank">📅 20:14 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69265" target="_blank">📅 19:04 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69263" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69262">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLXVW_bf_vxRmbeqJnpFt6GWXeIB1QHrApTIg48X1ekEiXjdT1Adh0N6Au1qWB1tBFIii88zp16THuUMUUDHfQBShqEJSBOlLVHJs4IABAMrlATCwyE82YzKkohiCosJFJolRAD_aYUpuZajLpSuj_gD-w7U73v2MJu1tlZSQ1YSW2UVF7lzZoKVNRbvOQR94tvfAs4PP5QBH7IZTbRrG-1Ae33R0NqJzRsRemrWt23YqsbLUFKgaML3YMPO7fklHeP-W94XiQVqrGuv24K6SC2r59ZNnBGXYOQvWiwPau0VjrdwkF1Q8wWJNkdlvMwzf4r8hbQyggewUX12wzslFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه تا از تروریستای مفعول حشد‌الشعبی که در حمله مشترک آمریکا و عربستان به عراق کشته شدن!
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69262" target="_blank">📅 17:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69261">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_69NfNuSLTmpHrGz4NJwf2Er6PZOkQ0PLRvy0MuSh0FBQYInm7oyGoreAzMRfgJLwTjR6mS03uzsNO1X_1E6IvsGyyGM2-4GGoPAZKwzPl0UqFDUSwANJH2DkcoaIiheA6U6XIP-M1Vh29_BAiXASHaKh8DEw--Sj7yNyQac3OGBdxBb-9S4aXZU3Wq1dTSArGuiMRKncjHFhOldOXdYXHWikte1AO-syAW5gDgSQtfBAXEf0SuAbAamrQlTSL4jybQ4r07fbrLKTMR95f31P19lzlRWo8zcx8_UFDI3z9R8CGLH63Ff89CX0QSiwGrXOY30AvQCIfSaQMDPm-rQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
روابط عمومی سپاه پاسداران؛اطلاعیه شماره ۵۶:
دو آشیانه پهپادی و یک مخزن سوخت هواپیما و بالگردهای نظامی در پایگاه علی السالم به آتش کشیده و منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69261" target="_blank">📅 17:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69260">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=HCGg7Ew_4yaqMFWbv9aEB8GJg9cMhO1sbCJLm3h9gEhpCKHfsddvSl-ciLHb0W1KcapLB3BOcx-VzEHUdjJS_61mppOlqMmvUdZXRB4I7iFKgG6orAcCtNhSYKaViR9fDStHXACgpZv7ujOSzHhoj7HWn1FMVlxJPrIirtpeT5liA4NPTiFSbdtAD2f9fnsd1_-bVGUyr3tH6d5mHbtaXJeDI4j1PO-6AwWNjiNCczOmZNhcPnRQ_Kr7i7WANj2GrObbImcha9bjF6ql_a0ZD3itdLEILtrmHSRltiUAz4604k0qo113bHK09jo_g-UKGvmc52f-Rw9_tX4r7XtXOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=HCGg7Ew_4yaqMFWbv9aEB8GJg9cMhO1sbCJLm3h9gEhpCKHfsddvSl-ciLHb0W1KcapLB3BOcx-VzEHUdjJS_61mppOlqMmvUdZXRB4I7iFKgG6orAcCtNhSYKaViR9fDStHXACgpZv7ujOSzHhoj7HWn1FMVlxJPrIirtpeT5liA4NPTiFSbdtAD2f9fnsd1_-bVGUyr3tH6d5mHbtaXJeDI4j1PO-6AwWNjiNCczOmZNhcPnRQ_Kr7i7WANj2GrObbImcha9bjF6ql_a0ZD3itdLEILtrmHSRltiUAz4604k0qo113bHK09jo_g-UKGvmc52f-Rw9_tX4r7XtXOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cea20ae2a1.mp4?token=p3qgZx84jViZylb1sN7NZ8iS6I-jz1IPr1-zawCAD34Z3W6sEPF0KJPQW4EjXjEvAG6ZcKc3bNRbcxmYQPTHK5O431-V3zdW1aDr67dP4b3BvZcjPmKq4EWVGWQtsxely6hOWd44uWa26wgnwFRlbndpdpUOZKacozSnil0njmQ0UyfC4d_3IQFeGvre61dxVReu4NEWXDAqE_TCo-7S2cvJPVa_T4L9JiexdGJMgd18I3DDzocrbHr13r99LaEyB8C9-Wig1GyQC8FmybswdZ8DPLUaOwQUbx7a4XUFm1vMyr4pJfGt8p5AR9w4hp3Q3_WaQzTFrXZESd-FAuzk1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cea20ae2a1.mp4?token=p3qgZx84jViZylb1sN7NZ8iS6I-jz1IPr1-zawCAD34Z3W6sEPF0KJPQW4EjXjEvAG6ZcKc3bNRbcxmYQPTHK5O431-V3zdW1aDr67dP4b3BvZcjPmKq4EWVGWQtsxely6hOWd44uWa26wgnwFRlbndpdpUOZKacozSnil0njmQ0UyfC4d_3IQFeGvre61dxVReu4NEWXDAqE_TCo-7S2cvJPVa_T4L9JiexdGJMgd18I3DDzocrbHr13r99LaEyB8C9-Wig1GyQC8FmybswdZ8DPLUaOwQUbx7a4XUFm1vMyr4pJfGt8p5AR9w4hp3Q3_WaQzTFrXZESd-FAuzk1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
حملات شبانه سنگین روسیه به کی‌یف، پایتخت اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69257" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69256">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d31a669dbb.mp4?token=pBXXsjdpL1HHGDK0je09gWWjsKrCtjboeAtR5cWIhZd3yTDS210kDBMY8hzlrsq-1hQwMkVIDmevz83Lr4OH3JZDT7DF-OgLhBrcnB7gSmbYMy5uxmlRHNH5qgQVDlFoyUlJdRU6XrP98tOwJH6pGySm7skHaLIbTDeDhDZkVT3r5Y-xAyf43sk-xkpDUaEh0YhJGmu-3XDnt4Lpu0KQ-qRWSwh1DgHZX6DxzXtcJGwQGu2Hv4p6nF_UHq6NeBHRIICQVw2ZSWbROTTIFV66dudKmaalOKaY6BvTlTTnFPtQmM-LJd6fTmEPvcpNv2YaeKin9CVR3c0eZ_z1Ii1r0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d31a669dbb.mp4?token=pBXXsjdpL1HHGDK0je09gWWjsKrCtjboeAtR5cWIhZd3yTDS210kDBMY8hzlrsq-1hQwMkVIDmevz83Lr4OH3JZDT7DF-OgLhBrcnB7gSmbYMy5uxmlRHNH5qgQVDlFoyUlJdRU6XrP98tOwJH6pGySm7skHaLIbTDeDhDZkVT3r5Y-xAyf43sk-xkpDUaEh0YhJGmu-3XDnt4Lpu0KQ-qRWSwh1DgHZX6DxzXtcJGwQGu2Hv4p6nF_UHq6NeBHRIICQVw2ZSWbROTTIFV66dudKmaalOKaY6BvTlTTnFPtQmM-LJd6fTmEPvcpNv2YaeKin9CVR3c0eZ_z1Ii1r0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f1666d9190.mp4?token=ck5wDZlXI91tpLWFN5c6SPywlZmI5UUzr-aJ7W7HY_CVYSuQRT0HJtdVkdXbPu9kwlrEgWsi5z4J2F6NWyEDrX5hJo_g5yJxkz5WRS9BMwpqlhZYz0P8SBlRM980AsUt3kBdXdWsTW9hZqOIo0DmbOLQC2dTgfbWAtX6A8zsFA_rj0xrQpeQ5jL-h2kjmw9xnVzYW_uLtfzNX6FrLMNZ7ZkFuO2siYFse3s-F-cPoDGxYjfr3nEkttcz4UyG4nfTZFOq1edD9d3iZlGxWpEjAejBNPzYER_CK5j_gnMkLXGSxSq05C_6e5n2msU2Ie_qxSIGoXP9NJ9YCIUJt26gHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1666d9190.mp4?token=ck5wDZlXI91tpLWFN5c6SPywlZmI5UUzr-aJ7W7HY_CVYSuQRT0HJtdVkdXbPu9kwlrEgWsi5z4J2F6NWyEDrX5hJo_g5yJxkz5WRS9BMwpqlhZYz0P8SBlRM980AsUt3kBdXdWsTW9hZqOIo0DmbOLQC2dTgfbWAtX6A8zsFA_rj0xrQpeQ5jL-h2kjmw9xnVzYW_uLtfzNX6FrLMNZ7ZkFuO2siYFse3s-F-cPoDGxYjfr3nEkttcz4UyG4nfTZFOq1edD9d3iZlGxWpEjAejBNPzYER_CK5j_gnMkLXGSxSq05C_6e5n2msU2Ie_qxSIGoXP9NJ9YCIUJt26gHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69253" target="_blank">📅 15:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69251">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l09iK0hL8NpHfQZGvcJqYWhpsfW5P5pv5zHSN9APwGKKIOAtlLY-37Gm4NfkFDXQhBY61vNkO9n0ZcMqdK1GS_atdzOuVN2tf3K9PiyVVVtv1hhgzaEMSIkSvr4Ezg7PiWXTBjiiPXuf10MeN2vxfeuPCJCpa_jKMke5Jr-ryjr2U-K5OS8XjozbFyCQTMQnJSBJ6hD9xBDw9sJmG5DawXnTXw12B2ZDzePIl99u51uRQaE2hjt9SLet6pcdP2XuDnbkDBjZNcds4il8supXtn-xvRwa5HfvSzDBE0_HNuDpGt4vNw4Ff72C4L4TWHQQ3Fn91p3qvHOwgLmg5x0EsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8b887c1d39.mp4?token=Vc9ESElfdWXi-_PYgtghfhRUuZZMiukLU_px4222EeZo0ooob9fJMV2JUlGrLaGB05KeBJqyo8smXBcNlIK3h2McYZ5jFXWW_eB_tKDI9C0mRmzZUAGV9uDciPeEmhLthMUTVjyPiaSlfiQKQc8Eq7qVF6jNPtYGh1thVxO1Q91QXQls1TIQk33QhVmBbGDdNO_qhuiVg0M0KnztJOSRD2BUhdybPNeRdN-BpD5VpDXxL26I9fhhW7B9KYcXzq25lrSV7osqVrjfv-LTbKJkAComYo5QGV8a4Ug7qkOoew4dB7x_x0GG1Vh-Dhs_-ucpJ-hH5HMEkPHIhE0Q6WMtyw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8b887c1d39.mp4?token=Vc9ESElfdWXi-_PYgtghfhRUuZZMiukLU_px4222EeZo0ooob9fJMV2JUlGrLaGB05KeBJqyo8smXBcNlIK3h2McYZ5jFXWW_eB_tKDI9C0mRmzZUAGV9uDciPeEmhLthMUTVjyPiaSlfiQKQc8Eq7qVF6jNPtYGh1thVxO1Q91QXQls1TIQk33QhVmBbGDdNO_qhuiVg0M0KnztJOSRD2BUhdybPNeRdN-BpD5VpDXxL26I9fhhW7B9KYcXzq25lrSV7osqVrjfv-LTbKJkAComYo5QGV8a4Ug7qkOoew4dB7x_x0GG1Vh-Dhs_-ucpJ-hH5HMEkPHIhE0Q6WMtyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cw6xrVAgZEye9rBpjmoLYibMWIVKIQjDFAnOLBVGbGySuouckDyIbYGHcm2vJlN5oHhZ5jh-UILUqiKFDXwlSTjBJmD1aex7n99QQMdHF3jwiM82CnyaXeDJ4GY73zIPyOXRBEVivRLzoa1TfHQ1MmrqIJzo3LB-lNT4mPs6HlB2B6CTsIHJLcHNXGvYnXAwrSciYIWwWgSOC1Fmb7l96BukWju7NLgHJuBbQPqIWZ021grxysa_s3_QGna8jLWVfb8QMwi4hPIupXVSwY2eSWxklT53EEKvhkPieOjOpo7xWO7Ych_dKIhz2nkr5XTVQqaIEWZ2ZXUNAwYs-IWJjw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn1.telesco.pe/file/a176457914.mp4?token=ZVqyclcgn0BCZpwnZ1CtU6Yk74uXvVonY8_8lxQQWgoVd2qzIzNOWBK-Bakl55zoy5EPCLXL9YkPZQO02xIrjkqi4mDDXtFnVh6tdnd4bnaICybFEQ12kesf33fq8_rGMhLbtVRX9yevCsG_B7KM4PPTNBRYZODwSP828uGG71UZSWFCeJpQHA_5xwiEgEQP7k8FxRLaD7FIdzVe3Bmar9INgmxZaLfdzjDaHj9AaJiXMcn5dNetyAcZVEtZD29bRB2P1jU8OiU4z3-0BZGp1tfn5xhe3KmKjTzVW_MW5TrpuaxkUyvhQ0X21fp0w0JWEdYa33ZFFO25xKjlrl2gEWXXPfL7oATlXJmMfAmUnR23YQls_iWUSoWDc-EeZ9Ejpjs3bN0R16iahc3N0a2KObjWEl9SP1G9YpIgPZzjpnhggeQnU_t23hSW1HtVoPHRBpmDZwlkREEPBF5Eg1R8-AijFDms4NJJxjR4h_IMX2vVpo35BETHz9lyufUGJh0tTe6o5GpzeV0ggMUn5R-sHBixIV2splGNt2SQSWhxiNWMVF9ELjQe2dEWp0-H9SS1IA25n_trhnwo6zCNSX7kZt3SarJ4jYzWaehqyZyKa2w4V0DwhbtBNZ_RBCQDg0A5UWS8EGvNAOXLubJ1UROcGM0ZVn-o8pNjjZxUNvKg4ks" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a176457914.mp4?token=ZVqyclcgn0BCZpwnZ1CtU6Yk74uXvVonY8_8lxQQWgoVd2qzIzNOWBK-Bakl55zoy5EPCLXL9YkPZQO02xIrjkqi4mDDXtFnVh6tdnd4bnaICybFEQ12kesf33fq8_rGMhLbtVRX9yevCsG_B7KM4PPTNBRYZODwSP828uGG71UZSWFCeJpQHA_5xwiEgEQP7k8FxRLaD7FIdzVe3Bmar9INgmxZaLfdzjDaHj9AaJiXMcn5dNetyAcZVEtZD29bRB2P1jU8OiU4z3-0BZGp1tfn5xhe3KmKjTzVW_MW5TrpuaxkUyvhQ0X21fp0w0JWEdYa33ZFFO25xKjlrl2gEWXXPfL7oATlXJmMfAmUnR23YQls_iWUSoWDc-EeZ9Ejpjs3bN0R16iahc3N0a2KObjWEl9SP1G9YpIgPZzjpnhggeQnU_t23hSW1HtVoPHRBpmDZwlkREEPBF5Eg1R8-AijFDms4NJJxjR4h_IMX2vVpo35BETHz9lyufUGJh0tTe6o5GpzeV0ggMUn5R-sHBixIV2splGNt2SQSWhxiNWMVF9ELjQe2dEWp0-H9SS1IA25n_trhnwo6zCNSX7kZt3SarJ4jYzWaehqyZyKa2w4V0DwhbtBNZ_RBCQDg0A5UWS8EGvNAOXLubJ1UROcGM0ZVn-o8pNjjZxUNvKg4ks" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69246" target="_blank">📅 12:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69245">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pq_Vjufdqwn-Sp1AeLppyZnRCjypIyjIZZQGmEu6ON4N0kP51rytUygGGtEunXNSwu9VeK-x32pTOBJ-q30wmoKlq2ZOdKT12vkLAX-W7MbYHCV5VEl17y-B-NvFspE4KMXEPsSqaE1zvDxDfbZ3Z8OHu89SwU5Vc_sIVE5I95el8YI2uynmvr1PlWN_vcens6klSRQWRaBVx2IXiqNohe-DhfFt_Jb5mqp07OurnHmYTe6P4eIf_LI91SZd8SZ3q3Cggvh81HQlb3JMWyNfzTAZgkDWnDvhMBNkWlgqfsHGlqspJPqzUNq_38WYOkR7MkCfzI5qK5CvKpUEwSgN1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
سپاه پاسداران:
متجاوز رو همین امروز تنبیه میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69245" target="_blank">📅 11:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69243">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXFsSoKWZ5Ap0Zu5U7FP_sdraJ0XeOmIuYsTNbQdLefEs76yD_LLrdBPIG3OQL02N5F8X8uutjXSTpqSBi_vTc3Go4NxLm93XwXZRHl9qYUmef3LdHs5Uf5vXgTZ2p8rqxmEejiiHuII2cPa2bEDZgyRb9jhCHs-odkleSHWTsaZO6RvLjb1oFYVdD70spx2FQM6ZaLaACzV_Qmh2eJNNa6DjEPpJmZhkg_wBY32sr7vnpmaFCyV716CeSCOtA0tf9w4KatPsKnB2KKIZRQlN2RS00fj0GdIBHmLMtvvbPNnHlqi5TKJJw2f2ITFZC2KWB21sxRQVbQ25ChH8cro6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69243" target="_blank">📅 11:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69242">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/15118cd8c7.mp4?token=Lkvu_gxGHKmdQbndakw-ZoHidHsCKZJhGJneMWV7gdJrQSTVjBhEy2kNz7iVMRDku2Ecsetz6lGSMQXr0rgDmTtwUKmMuKY13VoDCnS-PynrXJt3BwB6fTO-6lXxevyKDgMJxLEWXGx8s9NpVTAbIwhVEDe3d_F5wyCnx1ZbW1aadwBBLY8CRsKK1yrcPtFgszc0uWR5Y4NnGOEpu_1Up3zYJYXFo8NfJEGpG8oG665hexk_7wOMXeb9wl5unrcbU0gjhp9grFz52EfNnQugnU_FBh1TFrRJrEpGZRthMSAY_zQuxNzPk3JkPL5wRPSOPk5W-bQab621PJhY0Wxayw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/15118cd8c7.mp4?token=Lkvu_gxGHKmdQbndakw-ZoHidHsCKZJhGJneMWV7gdJrQSTVjBhEy2kNz7iVMRDku2Ecsetz6lGSMQXr0rgDmTtwUKmMuKY13VoDCnS-PynrXJt3BwB6fTO-6lXxevyKDgMJxLEWXGx8s9NpVTAbIwhVEDe3d_F5wyCnx1ZbW1aadwBBLY8CRsKK1yrcPtFgszc0uWR5Y4NnGOEpu_1Up3zYJYXFo8NfJEGpG8oG665hexk_7wOMXeb9wl5unrcbU0gjhp9grFz52EfNnQugnU_FBh1TFrRJrEpGZRthMSAY_zQuxNzPk3JkPL5wRPSOPk5W-bQab621PJhY0Wxayw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/e988916503.mp4?token=v6_f-TajHoxPTcELSpCbk73sxy-A1idiRBY3f_ahrsTZKB8uGDK4WBsLIu2gdAUygdRq86MQet7QXvKMkXwggfNyKnIy_h9QRnhabhqSMzC_fqpVEsIAt5u2kCNEwbqkxS_xdiBJbP-oTL_aIHKVb1mQYlqv2PFj1UztwytPFkQ94PlJXsVUY9rov-f6dpRsvXoPekUByCNBQlj25xzsg8viLzlc65tqfJkwHsam5HR0yYeRQ6X95nP1ucPVmXlxnjCicW2SiPH0VxdqrXC2UoozMar4E5ztwC6UuDyfjNfFx3RrYwGVqMjlDTRFlKdnnQ-7FUIYvdCME3PqN-EiDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e988916503.mp4?token=v6_f-TajHoxPTcELSpCbk73sxy-A1idiRBY3f_ahrsTZKB8uGDK4WBsLIu2gdAUygdRq86MQet7QXvKMkXwggfNyKnIy_h9QRnhabhqSMzC_fqpVEsIAt5u2kCNEwbqkxS_xdiBJbP-oTL_aIHKVb1mQYlqv2PFj1UztwytPFkQ94PlJXsVUY9rov-f6dpRsvXoPekUByCNBQlj25xzsg8viLzlc65tqfJkwHsam5HR0yYeRQ6X95nP1ucPVmXlxnjCicW2SiPH0VxdqrXC2UoozMar4E5ztwC6UuDyfjNfFx3RrYwGVqMjlDTRFlKdnnQ-7FUIYvdCME3PqN-EiDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8d926097b7.mp4?token=kZb4_1gRZ6GdmiqNq8uHfElACH0_JdTlCmgWmdOxlx_hJN5V00i1PLoty_tPC3pKYW49dL5OdYXowh032GHHcM0SfaRkwYi9RPpIP2grXE0Xd9G5340wu9ju6ccir4v4D6Bx1yu5626-MJ3rVpTB0XhyfBLEQ1RdmcdGUjD_2k8z3fupsNxr8ko6_7nwrGgMftJyZU8ZDNIKgDxbAZ7iZa_hMG9enlAoJTTb5lIwsErN-gGygtugxJ8J4nnqKZkV5g8H8RT0h_349acs88iBfVxy-WRO6LjzqIil2HG64aK_v55gJCnn5-vnHH8KXilLwkDfQef7mZSMEapGI6ontg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d926097b7.mp4?token=kZb4_1gRZ6GdmiqNq8uHfElACH0_JdTlCmgWmdOxlx_hJN5V00i1PLoty_tPC3pKYW49dL5OdYXowh032GHHcM0SfaRkwYi9RPpIP2grXE0Xd9G5340wu9ju6ccir4v4D6Bx1yu5626-MJ3rVpTB0XhyfBLEQ1RdmcdGUjD_2k8z3fupsNxr8ko6_7nwrGgMftJyZU8ZDNIKgDxbAZ7iZa_hMG9enlAoJTTb5lIwsErN-gGygtugxJ8J4nnqKZkV5g8H8RT0h_349acs88iBfVxy-WRO6LjzqIil2HG64aK_v55gJCnn5-vnHH8KXilLwkDfQef7mZSMEapGI6ontg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حملات دیشب آمریکا به نقاطی از کشور
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69237" target="_blank">📅 09:55 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69233" target="_blank">📅 09:15 · 08 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=CyMcRtViHWYROjsC5C13yTYPOGM4EpSSgwAFffcUPb-7jKwqjrlnT0dSI0dpz7Gwld0ep6vBd3iF5nSlb1uPXiuaK2w8LMI5hnFq5gEeZASTgxVevP0hetkELcm7UZVVc1A1-AzSx8lLMqtHaWP6QLLaJcN3rVTiQj-Y38aWTrx-5bPirUYKRlOIG9B-NBiV7R_seMnGn3Nlvb2mW-m1IfjOcaAF8DRRhnt4e65H2txLenOgsdoRn2gU_T_u-h__0zTx9TMIRx01l1qUZ8JBTb_ibIywEEof2U2DJzIN1a7TmfqsR62MfP0UwuFpQjANzUTPHNSn_oHKrYYxx-ViLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=CyMcRtViHWYROjsC5C13yTYPOGM4EpSSgwAFffcUPb-7jKwqjrlnT0dSI0dpz7Gwld0ep6vBd3iF5nSlb1uPXiuaK2w8LMI5hnFq5gEeZASTgxVevP0hetkELcm7UZVVc1A1-AzSx8lLMqtHaWP6QLLaJcN3rVTiQj-Y38aWTrx-5bPirUYKRlOIG9B-NBiV7R_seMnGn3Nlvb2mW-m1IfjOcaAF8DRRhnt4e65H2txLenOgsdoRn2gU_T_u-h__0zTx9TMIRx01l1qUZ8JBTb_ibIywEEof2U2DJzIN1a7TmfqsR62MfP0UwuFpQjANzUTPHNSn_oHKrYYxx-ViLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FfZfNbxk1WfMkSSwcJuWOWCCFztm2MtSkbcB8ART1XD6U9wYTdmsTBFSMkzRT0R7_L4PV3cf8yv50nkCmYgb04idaIQZt3UYir6aBlIQgbfkr7_6WyQa7n0sxvjC71qZhL6SkEDbUGfMMfdG59eW7dYUZ1NEllEGmyIt27UP3VZOMtRh0yb8S89e-sI-A9zED5wmrk4T6nb-8onHiVcO2SlK44kGbEtyV2Ay_7QydT-KDe0HKG8YH8cxr1VnTS1gNqM4u3CSzG14V1VrlfthvkDZamdV-2wUFwd4CkMYrSNaF0CkPlYKlMAMTUoqiBUCPWP_B7faswDFI95SoYVAsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjDHrsIeb5K4jYY5WE0ruHEZQCme92XRlJ1vZQC3p5Umbu2Tj_ziOd4XsXrfPRMQAwwK7Mi7CZG2iU9GFqr-j2Livgn85iVA44D03mX_mrLVoREcPnvixAUZs_mYWgFnnVffQ9U94dlJU5_uxQMsJG0F5cMR01tvoV9FvMqr7TFiRTnna3nCqAtEHYggFI4vhS06HjzGclxlqgmZEhneToGX6VXN7B4Iy5Hn40V-qRtPl4gxyx3wrEVKvdhxjRAb5N8HLRdiv4mLoDibimIRT96tnv9Wc9EFU12T_wOVkf_u5M3LERwL0El3huCXLhDNJUrGAYEvBrySaWdqDI16Nw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69227" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69225">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtWPqyAmkvYq0VLGbJVeKX4dzkjx5XkU44oY6QaX5zUiZqqYGDVY4N2RQ_yAET2FtaF1RQTQSAhak5V1GnWP2J5VZDCR3X4LTYgV7AO2KadPSVurg3DrnYFFBuclwhnFTQq8mmOFHxtrUm90K0VTODNaGRbRvTgy_toIIL-7gaK4Jz-fhnrey_FrzQaMEbW0rLWa5j--QADNLKE6kQLrHcv4DfndRSKmAuOWeIc7RO6kF08fHThe2dHEUHNKq2CSPMkKxJYpNMyCi9Y_1nbRWI8pP8uq5ELqxqwR7oBpm3myWZtZ1p2R-CvFauH9pIakZuuOKbCkRyVC7GPlu_BIKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بعد از توییت عراقچی درباره اوکراین، خبرگزاری رجانیوز، عراقچی رو ماله‌کش خطاب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69225" target="_blank">📅 01:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69224">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5o9F-tSNvqpnBYS88Es8lJ6moVWvHEN5nyp5Khsx3I8Twt68bTTIixz-7Ym3TJfHWdF-cAGlY3p435ZTVlYG0zmPRPHhBcja6kbgibjgZpw6DZQ4tmpoXpvyoToQznmlO5FTbGpxRdX0m7NamhURb_IqWVhlRD7n10FZt3y9lBp_CvNtB2w1sOsyFWjVUF97AQK4YoED3OOzQueHcl-0LwAKsep7GDJwDQejAP7IBjTfz8s0JZOwXgR-U8NwERBLHu9_a8aWP4nQFwqwkatcI_bQhrRVxtCtYtf7IsVwTbn5IL4Qm_Mset0sXWDIcFWKq0b0uRbYlLBthyhNeCKpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgCpNU2hWLwKMm_gocNGVjWYYZ4Sk2Y-1ykFW0Zgfbz1OoxuVUDh6ab6vZYKeh5l4XM-Ho1afxxmloaxQPXYLmFEcg8s-CMGmBRMEv4MJu-g3ApmVJ-2ApRaToeiZHrPxVxkagTi0w1OGYtUafklkVNNzkqZcAwbHBWx6okLM4_O7_T9kF740NfTkJUIp4KPv6pEfHwbnb5UQgUhlZ9YosmJiZhFx-PiqmC7B18JHEsgBIUUAZD5-TokOnfdy3jpEzKawmFh_LyOWCcgRqDiR0Ic7AuWQs2vMuFpj0yCYsUHK9geVwF8A4X337YE-ML9g0OcEUUrltJqbZEvufYyYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69221" target="_blank">📅 00:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69220">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3OEJJreLQ9-LBlnEwWmm-4iZHV_4JMSVcNejCyWOY3MUMUUt989JP48X5f6tuzySW8nx6wZZnD-HOXol23glJ96YUzdsFlMQNQeUDcWJ-Oo20Di9gv9NpK-wD58YdvyTec1iGQKo7wumPonEfNDKyq-x8UqEfXJLIZdgWzfPm_wHWs-YSQtA_VYIQ4cQKkEljRBsbS-8R455vJAojrxBikPE5mEw5HbvJ15q-FLVnCozz5BjcuieTRs9uzzOkvAN5Rg0rTFuqVlBaTa-9vHUt0BG4YRQdhjm4r8WqFNU5Gh0BBR7jDCotHZdNah9Y3HSQE7lo2Mw2AE153V6FL4dw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn1.telesco.pe/file/c08d37ce36.mp4?token=HntAMzok7Q5bnep0OPiBGGMcRfoM4rheRvikD7c-XqLWpJflLNw_YSFUZaTVky04UqJG_BInRSLaX_svBNluqYippxxvFOGBXEZviVl0tiYs4SNP-5ZjkD_ZOwQF_lv4cN5e1OQq2-bBRFU0bslQoz7BYOS-AMC6FG0shiH-Z9gwxy1ENz01oCiMikQjrhwDWgDbfoqi-J-6RmHuv7B2ExgHsx78LG76VVBerNagbs96v_FWA_ckuDlCzpG4IkFFSRn5OstI_C9DOdaYuJSqGtaIqEZ-uif6ZJ016-UHnVWb2Vb7NHx5Y_BcMIqDIIAOA1x8m_4_cn5wxVpJkPFkmw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c08d37ce36.mp4?token=HntAMzok7Q5bnep0OPiBGGMcRfoM4rheRvikD7c-XqLWpJflLNw_YSFUZaTVky04UqJG_BInRSLaX_svBNluqYippxxvFOGBXEZviVl0tiYs4SNP-5ZjkD_ZOwQF_lv4cN5e1OQq2-bBRFU0bslQoz7BYOS-AMC6FG0shiH-Z9gwxy1ENz01oCiMikQjrhwDWgDbfoqi-J-6RmHuv7B2ExgHsx78LG76VVBerNagbs96v_FWA_ckuDlCzpG4IkFFSRn5OstI_C9DOdaYuJSqGtaIqEZ-uif6ZJ016-UHnVWb2Vb7NHx5Y_BcMIqDIIAOA1x8m_4_cn5wxVpJkPFkmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/e6df873441.mp4?token=QN7SyEya4qEaeF6Qw443gJ8SXj39knCDxDDLeETYtcfNri2b4phU4IcNjesoz-H6UDU0BNVLwgCF-_dHwJWosigrl7yRf_jGbpbCYObwX56evi0wROfGkvZAgn2EzlaLYzyNWBW43_z_KoiNW9sGTK1KTJyd2BbsKSpJ6I0vd43UWmIb5CQv8NuSkV7bOLBfrmbaQD1hTuY1pJBwIfXJseA8A0mgGIYMrfUd1OSiD8kCxuLyplYeLvfGCe2HH6QKa6vOH_MRVt-FT7Ug6ND38Y3pGtLcXJ__fL4RFc0KAwpt-JeYCqvbq3Q6aQ4tPH3KPpezNDJ3Hugg0Fo1M2Be9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6df873441.mp4?token=QN7SyEya4qEaeF6Qw443gJ8SXj39knCDxDDLeETYtcfNri2b4phU4IcNjesoz-H6UDU0BNVLwgCF-_dHwJWosigrl7yRf_jGbpbCYObwX56evi0wROfGkvZAgn2EzlaLYzyNWBW43_z_KoiNW9sGTK1KTJyd2BbsKSpJ6I0vd43UWmIb5CQv8NuSkV7bOLBfrmbaQD1hTuY1pJBwIfXJseA8A0mgGIYMrfUd1OSiD8kCxuLyplYeLvfGCe2HH6QKa6vOH_MRVt-FT7Ug6ND38Y3pGtLcXJ__fL4RFc0KAwpt-JeYCqvbq3Q6aQ4tPH3KPpezNDJ3Hugg0Fo1M2Be9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ad144cccc8.mp4?token=YB5nOze_QM4Uenl58oGob4zzwbmTnp5lQmxbgk8mjOWm0SMmJDoBmmb8Uff-asa_4qUBbb2fWPxiVarWy_RZ0ENdBZFrSmuGnDzovtJIU_l81OroZ4f2YvJ400_nMYuzgQPkrqUGNzY9bXDP2DTdS0w9wflwgdytw-Ob0_ssIM9yUG4ImtWffbULULqeO-v7Rch5tmVd-nh-Fwl0e9zix4Qr8IhGjo5s88-J0wK0anh1baNgTxuV722_oCMjztp0gJF232kz7DhMRNI7mnyOlGKMz9ELyB-mQZzthazXOvLuVWyU17PHc8H5FMR2NQpvrfsHTJUQDoecSGD2N0JTeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad144cccc8.mp4?token=YB5nOze_QM4Uenl58oGob4zzwbmTnp5lQmxbgk8mjOWm0SMmJDoBmmb8Uff-asa_4qUBbb2fWPxiVarWy_RZ0ENdBZFrSmuGnDzovtJIU_l81OroZ4f2YvJ400_nMYuzgQPkrqUGNzY9bXDP2DTdS0w9wflwgdytw-Ob0_ssIM9yUG4ImtWffbULULqeO-v7Rch5tmVd-nh-Fwl0e9zix4Qr8IhGjo5s88-J0wK0anh1baNgTxuV722_oCMjztp0gJF232kz7DhMRNI7mnyOlGKMz9ELyB-mQZzthazXOvLuVWyU17PHc8H5FMR2NQpvrfsHTJUQDoecSGD2N0JTeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3687c44382.mp4?token=cOkhbGb-JJ4PEP0BJ3Pa6IXej-F_PayHiC9r0w_qh-EI-T-73brgSDSodsDvau88_Ki1sFhlKG9tTzLKLHtoYO3WNOV0HT3T8a19PkahT1MX-FwkgvtE82JNHC_E0fppxnx-ih1qazyhitGzPLrfdlwS5RhMRzPWf5nAmLhZkDpQwI4JiKIFU2wyfZyAdzQaLcTUhSqPDKiFEkPl2as2d0MfI38dmVFZdhQs95f-_FVLagQApsdu2M1X1ZOU9_BWl6f1rqb96hLUpQfiAvOPQ68lA-Xb0pSzrh4oOfkVW7p9NlRdGyanDEYh5OrQKSKn8JKEMhOt9X8a0tofPG-Asw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3687c44382.mp4?token=cOkhbGb-JJ4PEP0BJ3Pa6IXej-F_PayHiC9r0w_qh-EI-T-73brgSDSodsDvau88_Ki1sFhlKG9tTzLKLHtoYO3WNOV0HT3T8a19PkahT1MX-FwkgvtE82JNHC_E0fppxnx-ih1qazyhitGzPLrfdlwS5RhMRzPWf5nAmLhZkDpQwI4JiKIFU2wyfZyAdzQaLcTUhSqPDKiFEkPl2as2d0MfI38dmVFZdhQs95f-_FVLagQApsdu2M1X1ZOU9_BWl6f1rqb96hLUpQfiAvOPQ68lA-Xb0pSzrh4oOfkVW7p9NlRdGyanDEYh5OrQKSKn8JKEMhOt9X8a0tofPG-Asw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69212" target="_blank">📅 22:34 · 07 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgIbq07ScKztYPjbBVhM9fz8TEmPJy7iFybwhWpB3GkKd8Mv38LltSaGY_0VllQslPebdt-FVBMnlqQowrzmj1wrUvZKvS5BS3jcXdtUOiSeVZACYtBUNDe2M7ISjSvKP35Z024lK-bZjO1npUj0mRevQbtTXNxg_uXxyfifWk7ukta7ikdyNY7LNft_pFVSB4GGroN83j4TyyLh25xp_DP11qeXXXwpbTK3VdcQMkloy75v1XPGPfX-UQ7s3_CNzCJFC3VXWls91Zaz2LQfmKERt_Q9hThTiwde9sbJxQjon0omyQW76oayv15IQtm7PqsKTR7FlggcBBrA2FFm6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XWtwnOQkBGmf8gQjVa4gLJJsDgtkUHXXaTrQ6jja4T-lPqfmB35bQQrSysbwVWeHUEmcvP5DDz6Mmu7UUs38HRjXlmo44XXbyCJN03fy40Y4iab43IP1Fqf9el7GZLqvMiLjCaU-qLex6UMXfa2wJKE5tsNGhXx_JbutF101pqpA865W4KbDBJAxACyEByL3xaUptxOT4Crt-QWMrUSS1lMgA8Br4WHqIMZ1FB3tZ783NpE-J4im4szJYplbwfiD9hZ7A8HBMeLkgYrejTWCEMEC_9rQSK9eN4TPtWoPrZRE8XVl-8UBvgQGRNxIOX8eCtEJnWAmvXpxvQvM7BBJoA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f3f736bc6e.mp4?token=nzDO2bHspAn39RsoRi76H0idea8plfLTa7ZzbWURUWAlFGUlRQy8MystB5lGU6I7x3aHEoqONT9sd43Ds4qVkw9yN8vC8r2rMYnH130-1nqDfb7iafhmj3LryQOGbCDWCWKSXxt9FTSWZUV2u9-iSmZn8nAnj0ZugrGPjOqQ_q3MVlSavC_mE9em9snCtI0EJTUMw2PgFSuIbEbCD50wrOFoHwdV9tNbzwqKsmasOzueVJt4MAG9hKQa46v3yvH-2Aq4eOqIsv7f9-l30dWd5KL68fdkrejsrqyPUlVZwoQBtzlojum5O9bX44pZvojVabmEaE_SE1YQ7AA2nmZwCSwOjONNBw4yjuL1A6DhGUBfu1OKHpAtQ2nKFLxQV_jo8zMpraV2IVMFZE3F4dVHUkzyj_6RN-jbkS0mog4KV7Q7RhnqddlUFkdu8J2Z_wln5CkmUoUj55AT4m6tPfFTSpAWhYfQ0Spq6zywZKf4VhmuLDpHvjcCMsm0VWut_iVGJ_0mgk7llCUaNtzEfXDtm7WusUEkNcWwmyEu04KvxgbZz_ahqTO-GZWJCAgVngqY6RDqFO0EuZF_g3IALwgaW0tjLTXchTW5sGM69yLU4Sq0CBv6ZNmUJ6HfonSDCry3ox6-47Iw0lJ2LPlyi9N2nf_Kp1JUWsjYz6UdgoqKJlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f736bc6e.mp4?token=nzDO2bHspAn39RsoRi76H0idea8plfLTa7ZzbWURUWAlFGUlRQy8MystB5lGU6I7x3aHEoqONT9sd43Ds4qVkw9yN8vC8r2rMYnH130-1nqDfb7iafhmj3LryQOGbCDWCWKSXxt9FTSWZUV2u9-iSmZn8nAnj0ZugrGPjOqQ_q3MVlSavC_mE9em9snCtI0EJTUMw2PgFSuIbEbCD50wrOFoHwdV9tNbzwqKsmasOzueVJt4MAG9hKQa46v3yvH-2Aq4eOqIsv7f9-l30dWd5KL68fdkrejsrqyPUlVZwoQBtzlojum5O9bX44pZvojVabmEaE_SE1YQ7AA2nmZwCSwOjONNBw4yjuL1A6DhGUBfu1OKHpAtQ2nKFLxQV_jo8zMpraV2IVMFZE3F4dVHUkzyj_6RN-jbkS0mog4KV7Q7RhnqddlUFkdu8J2Z_wln5CkmUoUj55AT4m6tPfFTSpAWhYfQ0Spq6zywZKf4VhmuLDpHvjcCMsm0VWut_iVGJ_0mgk7llCUaNtzEfXDtm7WusUEkNcWwmyEu04KvxgbZz_ahqTO-GZWJCAgVngqY6RDqFO0EuZF_g3IALwgaW0tjLTXchTW5sGM69yLU4Sq0CBv6ZNmUJ6HfonSDCry3ox6-47Iw0lJ2LPlyi9N2nf_Kp1JUWsjYz6UdgoqKJlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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

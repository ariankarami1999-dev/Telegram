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
<img src="https://cdn4.telesco.pe/file/B2tvN5KzewXHsfZw98k7ZkdD-1vJqawC8j3s9XmBaWAlnwPq4N83pLd42W9pJb7A05T0mXev46VKIAh5IyDTB1DOXFqMZs3sDhoCZRvfmlfuFMulrbBly2nmO_FBUDI5gKz2IC1nzE-j8ge7phG9RffmXnomDCgpe5ZiOuRh4tXOLvEA-tVA2OOKaiAJgbYFx-F-BOfVqcYdEy3GkrQotMGDWhoN12Lex7qH9S3veuIz_xqKCRfWngVcBn6tTpnYF_kF4sKx-IKksYKOewlUH57QAkNc_B9qiQP-fdJZAcKRdGmRfoQuUqC1HnFK1iemhfE2_FZJh25E_n0aGEtGog.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 225K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-28 16:53:59</div>
<hr>

<div class="tg-post" id="msg-82356">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">باختایی که دلار داده بود بودش سنگین ولی حالا برگشته با یه کامبک(دلار برگشت تو کانال ۱۹۰ت)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 279 · <a href="https://t.me/funhiphop/82356" target="_blank">📅 16:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82355">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4162625b6d.mp4?token=pCAwSUVvrsw9GJ1tAYRyUw5G2zwwZtYgqhuqU6LstwOAqQO71LlAgksBmZWRDhXpdIvRjRfw5bpAuz-blXrY16Wcaa8SDFj3b8-jm0ujTt0WJIodTVp3b9rVApnyMqbFbYIqm2XHrE_rVL4iPtA6LQBTJo7BJAirilC_iMWEGotaM0UCF-A9aAKOcXsK60971XBB6TK1kkQBCCFZFJfFdwk1wX3TFAaW2Ry4_QBs9XfpgppggmannJ_wg8dBTWN6pAJ9ddYAz99KV8uFwWBQQyftK4Zdg6TN4Wy65z9NKVqMIySTyH7eGC9VJM-U51Bh0HwUltf-ILnTlA3cCaSG5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4162625b6d.mp4?token=pCAwSUVvrsw9GJ1tAYRyUw5G2zwwZtYgqhuqU6LstwOAqQO71LlAgksBmZWRDhXpdIvRjRfw5bpAuz-blXrY16Wcaa8SDFj3b8-jm0ujTt0WJIodTVp3b9rVApnyMqbFbYIqm2XHrE_rVL4iPtA6LQBTJo7BJAirilC_iMWEGotaM0UCF-A9aAKOcXsK60971XBB6TK1kkQBCCFZFJfFdwk1wX3TFAaW2Ry4_QBs9XfpgppggmannJ_wg8dBTWN6pAJ9ddYAz99KV8uFwWBQQyftK4Zdg6TN4Wy65z9NKVqMIySTyH7eGC9VJM-U51Bh0HwUltf-ILnTlA3cCaSG5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زید تلخون رو تو یکی از تیمارستان هایی که توش بستری بودم دیدم ولی یادم نمیاد کدومشون بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/funhiphop/82355" target="_blank">📅 16:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82354">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رضا پیشرو داره رو یه آموزش جنگیری جدید(موزیک) کار میکنه که معلوم نیست کی میخواد بدتش بیرون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/funhiphop/82354" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82353">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xf1vWLLQKjO9b3rNjgasAqpWS2a-n--tCpI3GHOPyetgneKmM_fBLVRpxmvoxdCPLiUYS6udweBgT4IrnUGn7qDy9XWAANN2yW4Q3KMRPJAzSaIPHsJs_DSsZPHFNDofXEI1mOE2JjrOXf7giclZiYI6hF1cpbCPL88ogJ4PGO04pRnnEfEDlDx74dwGU0TlxU7OIzhrkaWnBYAziPB6ciwS-FdC1xhp1UimqICRN7aA8jUgkRF3Uaej-FDM8UVuUI7kI10ltCuGxbxtIarT2ZkCiGYAM5YCfYeYjHXQ2VhJpZM51V5Qq2LhzuC2pLpD35UjpiY1_3f6QDd7zSXxIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا به دلی که دریا باشه کشتی میده
❤️
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/funhiphop/82353" target="_blank">📅 15:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82352">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دوستان ویلسون کلی ویس داده ولی از درک منو شما خارجه، اگر معنای فلسفه رو بلدید خودتون برید چنلش گوش کنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/funhiphop/82352" target="_blank">📅 15:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82351">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ng0ix_kQpD8a0JDePmkcBxUukkVbceo8tChjJe5PzXqpBLeqncKugW0TkUSAPrWsBmdzAQ4GFkZh6j5oPD9AI-iODHbKm3nuuWuSBNyto6EbjJ-O0gbq8ay9qeEy2lHWkJhhEw1dZZc2s3gyoUKO4ymBkPk6n-bTlzZgGcJQNOjONp9sz0kV0eAoaFyLxYEWLSX_CWnqpQVi714qI9WhwvOyNcJlOs8_hgaOKr_lbA0OHvjO3stKeCPVTdrGrQUFtDsXLNgfS0xeelkFDKTiJYgZKZWtNbSNzhUC_SJIprJErr7t1DNFnWhWvNSjL6MXANBj-DmZj2dVvMhwUNmMxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری این زنه که یادم رفت کی بود و حال ندارم برگردم ببینم کی بود ولی به ۱۵۰۰ تصویر مربوطه و داره راجع به مهدیار صحبت میکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/funhiphop/82351" target="_blank">📅 15:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82350">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خب کصخل میتونی آلبومشون کنی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/funhiphop/82350" target="_blank">📅 15:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82349">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fb3975ba9.mp4?token=X9V3jCBqHSOCD4pPIJT9Zkr6PUYBvcdeYDV7rOEiBrNiE60oemKySThDeedBpdXVTjbfLHg8FnZj0TdTnKs8MsRz30WZDqPZrUNLMCc0btgcsR2ewn2z6LWCGPhMwFtVHPxsTm64iFlvoFMIkcZPEugA9SvJ97h6WbPFbK6iMlOFjXTf85acBb6pzuZPUkfb22AV1c_BJMy0QoxogM9RZpr2MZhHgOAz_TYNKNEt9OggiX9yAIoYzVkX3Y3qFucBF3IChvm5EyY6AVSnGlI8uPDB8siICEygAVhOsEXetUv6p73mEi71GJ3WGQRGqLvA-YEDywruEZ5Yoj0Merh0fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fb3975ba9.mp4?token=X9V3jCBqHSOCD4pPIJT9Zkr6PUYBvcdeYDV7rOEiBrNiE60oemKySThDeedBpdXVTjbfLHg8FnZj0TdTnKs8MsRz30WZDqPZrUNLMCc0btgcsR2ewn2z6LWCGPhMwFtVHPxsTm64iFlvoFMIkcZPEugA9SvJ97h6WbPFbK6iMlOFjXTf85acBb6pzuZPUkfb22AV1c_BJMy0QoxogM9RZpr2MZhHgOAz_TYNKNEt9OggiX9yAIoYzVkX3Y3qFucBF3IChvm5EyY6AVSnGlI8uPDB8siICEygAVhOsEXetUv6p73mEi71GJ3WGQRGqLvA-YEDywruEZ5Yoj0Merh0fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جهانی شدیم رفت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/funhiphop/82349" target="_blank">📅 14:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82348">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5ZCNpimtU_L2jOITZcBYbhaZ4eou1O8DZP-3arQQnoZ48gXoxbRPYTbXLalIPYiThri2AXIz21nh9EC_y-Z7KQykY6-jzzN7juyq3cVUbHazVVh9m3jYCWn9KoCZGSfR9MfW82KkIAlqUtDkRPqDaNqk_Ro-yzSf8SnqsrYpjmahxb3rC16cMr2SdsqqgiYuivdoKhGv4oFIDlV4fnkte3EsPE4F5IqwH-h3pfPcmR2XTuOWSWJMbv3vUnDaAPSq_qd4tU_LBg5RCaZLT1Vb8FwHRGxyjh4layDY2er4SwiypREbyLd6h9TrmtLXT1JDXjZvevKitc4ZpVm4HU5NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاقبت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/funhiphop/82348" target="_blank">📅 14:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82346">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1960c566c.mp4?token=ezxgQwG4Nj9x52xmRpuxdFxVueJOgDBJND0FzL0-P0OC1HM_jJuZrl7_wWcZhZkreQMBRqMMfrNNiYQFI2yVJMHOnBke6knmEoVynMiz7pOBumxXOCq4A0FuCwz6va6BQmvzzpufm4dKSwnN9AtoYG2SPo8IssTIorQtEILivZVAPHiLiO1nBGNIoicBSUj6kYbwCW-uR7iofciGHwjivqLLxBXQUsCIxEWRa9LMQmj0syYpzY1ojcVY59PwDA4OoXUtjcrbJYmA1SbT1JKtxVQMecEazc0-xAXIOZxD1s9Phlnpw6mhrqtQJM4jRgshWbiOxD0qs_EJj08PsBel8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1960c566c.mp4?token=ezxgQwG4Nj9x52xmRpuxdFxVueJOgDBJND0FzL0-P0OC1HM_jJuZrl7_wWcZhZkreQMBRqMMfrNNiYQFI2yVJMHOnBke6knmEoVynMiz7pOBumxXOCq4A0FuCwz6va6BQmvzzpufm4dKSwnN9AtoYG2SPo8IssTIorQtEILivZVAPHiLiO1nBGNIoicBSUj6kYbwCW-uR7iofciGHwjivqLLxBXQUsCIxEWRa9LMQmj0syYpzY1ojcVY59PwDA4OoXUtjcrbJYmA1SbT1JKtxVQMecEazc0-xAXIOZxD1s9Phlnpw6mhrqtQJM4jRgshWbiOxD0qs_EJj08PsBel8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این حرومزاده رو هم گرفتنش.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/82346" target="_blank">📅 13:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82345">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDkRXxeloK149QC69Z1_G2vguGdcBqbWRktXkoAowOoJ5dCYGMzrlVgXawH7DGr6HYYhiS0yG2Eoj6RdLyVSrHUu94f46DmWIe2yp83AI2WwtzWyJ_76dUPgWBZe0anIzYbtd8z4XHyHquKWaHNyImAnsm0ONfUI7cMuwwBEhtD499sfFX4QLdQWs6RL7CK7Xl9hyTtT8J1csldeDMwdCxc12lZQTBzBTXp_Gxh3D8sfvPn-VNVD3qPUWxyeisio2_r6v1LSCKP8HLVer48p5lSGDIzHvQsQD7Q32H39AeKeiwnE6Q4tfwnxnE4PHiKTajxpS6NSBLfA0FAzK5qEjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نادر دهنتو گاییدم نادر
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/82345" target="_blank">📅 11:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82344">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5a33e0eff.mp4?token=DkVUwurUL0UqV2KRWwNz-i1BmtUNEW58kqTjBnQMe_cM7J9J3dBbQyuOHpGYZQjV8fJrVEJM-_RWeQtk7WUuUgoBO3sB-sos1LUdQE9CSdv7-n7rZZgFdM8ZVV-S6Y_cUwDSykB71RYc7mQYgWIiskN3WLkl0b5TypbQpdJoMZVYSo9LHybD-Mdi8VSRGwrJ041GMAZ25Xjx1PvnSdR9QLSC-pTM24INOHoIDh2NW3OI4WcpvqS8CjcN_HeqR-LnX_380NGBlT0k1kRHD3KgZdfQIruui-QpE5YU32tHhSnIumai29BwUkeq9oJwPugawMLbztogOnkrjga7_CkFCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5a33e0eff.mp4?token=DkVUwurUL0UqV2KRWwNz-i1BmtUNEW58kqTjBnQMe_cM7J9J3dBbQyuOHpGYZQjV8fJrVEJM-_RWeQtk7WUuUgoBO3sB-sos1LUdQE9CSdv7-n7rZZgFdM8ZVV-S6Y_cUwDSykB71RYc7mQYgWIiskN3WLkl0b5TypbQpdJoMZVYSo9LHybD-Mdi8VSRGwrJ041GMAZ25Xjx1PvnSdR9QLSC-pTM24INOHoIDh2NW3OI4WcpvqS8CjcN_HeqR-LnX_380NGBlT0k1kRHD3KgZdfQIruui-QpE5YU32tHhSnIumai29BwUkeq9oJwPugawMLbztogOnkrjga7_CkFCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادی ترین دنبال کننده لیگ برتر ایران :
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/82344" target="_blank">📅 11:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82343">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MElWxpZeopwk5kY5gxzFSMUwc3UBgv7bsNs5rxy2m2rkPWgux1acfavDgEim6B7OWmO4u1DORWkN8cgOvEUmb06bgmcdooBlwW-8xQntfSawVneHKa6g4adqgfW22oaMS0bP6WI1yrmsDpnx0Wagz8oFR0RrXNyaZtJ6OksWvwjTf5mRdjfCRoEWkz4M7sOLYOuH0qaHO5KLzGJT144wrdsaDpqvU9WQZ6xXbQg-V-MoWGtPsUCFsquMkTsslipK2uAShNZnLomJl9CPisXenEoytZFHjksgtwNHFNGkY-4VcskGItVOS6-bEHZYwDdr6YqaJudOscMCiSGU37uWwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
اتلتیکو مادرید - مالاگا
🏆
لالیگا اسپانیا
🇪🇸
🕔
چهارشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه متروپولیتانو
🎲
با بیش از ۵۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
⚽️
نکاتی در مورد بازی‌های رودررو:
در ۱۰ تقابل اخیر، ۷ برد سهم اتلتیکو مادرید و ۱ برد سهم مالاگا بوده و ۲ دیدار نیز با نتیجه تساوی به پایان رسیده است.
🧠
وقتی بدهکار هستید، بازی تعطیل است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r28
💻
@BetForward</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/82343" target="_blank">📅 11:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82342">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/400ac60101.mp4?token=L2ZTVQL4g-omod-xzGkS_09gjWehpR23oQL3P-1INSU2eVqlcFU_E6da47s-hCxNAv6OFDuXmSqFa6RTJvcL65ScWRh2e3Jfj6tWxKmGaQqkP28n_UC_Rym8WNz5kw_3g1XRswiFrOZ7LqhElFiIyNQJ9KdK24NqEcuiwIbXnDWbi3lQaF6arnwLLrm-UcyYuuV1kSUr8ou09ZL5ChHxDaucrRunjl7zUNC-uR3aTXx_-aTRZxM1dMJgNk59zLZSzWm0i_nMW9i6JwEULHmsB5ucsaQ-P6RsoYLkIC3YUTVgvC92-b-GmAEbkrY2WG1JkzVu6hZbJwu9aOZeuMSI9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/400ac60101.mp4?token=L2ZTVQL4g-omod-xzGkS_09gjWehpR23oQL3P-1INSU2eVqlcFU_E6da47s-hCxNAv6OFDuXmSqFa6RTJvcL65ScWRh2e3Jfj6tWxKmGaQqkP28n_UC_Rym8WNz5kw_3g1XRswiFrOZ7LqhElFiIyNQJ9KdK24NqEcuiwIbXnDWbi3lQaF6arnwLLrm-UcyYuuV1kSUr8ou09ZL5ChHxDaucrRunjl7zUNC-uR3aTXx_-aTRZxM1dMJgNk59zLZSzWm0i_nMW9i6JwEULHmsB5ucsaQ-P6RsoYLkIC3YUTVgvC92-b-GmAEbkrY2WG1JkzVu6hZbJwu9aOZeuMSI9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باورتون میشه یه روز تو همین ایران خودمون
رئیس جمهور تو دوربین زل زد گفت:
دختر بچه ای تو خونه شون انرژی هسته رو کشف کرده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/82342" target="_blank">📅 10:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82341">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSgBTmSbhnePjMyhnvxyAp_ITYWVBN2C0x_PdSSIjniENo_ZyLCUfYJp0lHgn8HwI16B__hAflyqKlx2WRJnmw3vsMYGdO8eiYhii1ZO-dT7o4b7ShLLPkADLMcoDDOUKHm_F0W0ULW1l0iw1RvtOveWEPQqkgr-DUzlEJvP17blxgyFVxvRwoGEA-meeudTGnOkVqFcJo54kLndnuvud2zS9kTmfmoxl55OuNk5F_9NuJ_L1MjaOen5TTZF3xOPOLhX2nx_NoAyCLtMnpwFvf5ZlAtSnQsfnbpR56oolV-v7whO26Kk5AyVutqz9jeLgQYQ_u-P54zXqoB9oek75g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دراکاریس
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82341" target="_blank">📅 01:59 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82340">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmbOhWBc5MLrUM11k6r6v8T55iKpb9Qgl53gqHq7rZ8jia4DH55G5phef9KnrY6MQ6PwGeFr4Efz6ZdByNP2Qo90cQ-THTFVZTAzmiqtbaCUoXgVkBv-f7EtmMQShdQRaAl9XbaZA0c-YhM7mrhIr3eB0Y4H8UcOti08On81WpRMQWlug0k40Tu4VhJ-bV8dJbuB6sb5EqqAFf-SxDjDz2NzkUyLxx8od_RJEEeMhCay6Du9WAEzYB-mEfnhpifiodkJerGI-S9e3iplEREE0Jv1UgJ6DKkowLvxDASEQeC2mdRdAuxnxMA81dR1udc-rHoTAxgde3qaS2s_tpJXTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">والا بخدا همه پایینیو دوس داشتن تو لباس بالایی، آبرو ریزی نکن شیر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82340" target="_blank">📅 23:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82339">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67fee2d429.mp4?token=ea7FVvv1BklNp5NjXVPCis3wJXbIT3tamHhZhh3sWml2AAnpxpAGmENCsz3bN-SQZz7de1fA5k8Kr139F03z8Ihd5-GCXuMGqICx-A3FI1K-lc_ubVgTMBPW6wolz9sps9DxTI-Z4y9fu53J7VxXbKbSRA1eBYfrbtb1n1WzJLpUh71JXZq6rkxfIaEC6G1xQ6RVSsIck557gDGjW4OS2sbofPV3FYmc_B9cj4ubRyvZ1Ha8SbjZx67IhPmae3YgYvGKTfF75un7x91YkKznPbxuN0Kd56sQxyAMOcOKJqNGb0wR-sgCRn0kacgZ9_PY08r3m_00DMUyRhi23L_DSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67fee2d429.mp4?token=ea7FVvv1BklNp5NjXVPCis3wJXbIT3tamHhZhh3sWml2AAnpxpAGmENCsz3bN-SQZz7de1fA5k8Kr139F03z8Ihd5-GCXuMGqICx-A3FI1K-lc_ubVgTMBPW6wolz9sps9DxTI-Z4y9fu53J7VxXbKbSRA1eBYfrbtb1n1WzJLpUh71JXZq6rkxfIaEC6G1xQ6RVSsIck557gDGjW4OS2sbofPV3FYmc_B9cj4ubRyvZ1Ha8SbjZx67IhPmae3YgYvGKTfF75un7x91YkKznPbxuN0Kd56sQxyAMOcOKJqNGb0wR-sgCRn0kacgZ9_PY08r3m_00DMUyRhi23L_DSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه کافه تو آمریکا جلوی در ورودیش تابلو "ورود سگ و مسلمون ها ممنوع" گذاشته بوده، مایک تایسونم از لج رفته داخل کافه و شروع کرده به نماز خوندن
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82339" target="_blank">📅 22:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82338">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">چرا این بلاگرا که میرن تو خیابون به ملت میگن "میای بریم کافه؟" به پست ما نمیخورن تا پدر موجودی حسابشونو در بیاریم</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82338" target="_blank">📅 22:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82337">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">این یعنی تعویق
کاخ سفید: مذاکرات با ایران تا اطلاع ثانوی لغو شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82337" target="_blank">📅 22:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82336">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سپاه 2 تا موشک ول داده تو امارات ولی گردن نمیگیره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82336" target="_blank">📅 22:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82335">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oieJEVJLBQfFs2orccGJKwuhPAlUJp-6lI2GhahtItFLcIaYQ__U0Swi08pD_t4_hXaAbKW9Tt4ZZASpTxsbESFtZTtkk-Wq4C2D-fg2dc9W203pY53-5pnxxD0Qd5qn359h3h6PVgwBMO25mHX_cGupz0SbJgDWJ_9Ha_3gUztp5u-8sZXP2P0zybpKZvJy9DNh_jjqzAwdPbzBteo8dj9hyVo3HmjIirRWIz0umdNxJMQVMChGeaXvzYJV3Rk11x8K3Hr6ffzVNwTpBdDrlGcdohzv1Wy9LxL3Ge-AjQoOWjE2NRHl0Jk41F9YbXS6Sx5lDH-SyKWKIK5hLmQZRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ های جدید کارمزد خدمات بانکی برای سال ۱۴۰۵
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82335" target="_blank">📅 22:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82333">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LEVLKGI3Irtfn1P2n8iAbwZ3dviciXTyVyATVfz5iv5O6FmBjuQieBsPG28evNLG7kd5mSlntY8viD4IXL69Yc_Ge2zRaEnLKt_qG5Y2KL-_3yrgn8-gi7QY11gwE8BQiu5U41N_OQyH1xznanlhGuiEX5fbVnMjy_RKGDHpqlk7P92UYFcU69exQ4mNqo8QyD1JqLwWDQSlKfAMaTYa4kBoBHe-RnKFMBXJVOMMYPpJ5sXKFcLLcxzAsY3WK_bzJ4U03nU-aNU4X97jnuK_MQ04UXRHeuqwb6dEHa1G3np_r_I8IaVVxMHAARA-jDe6hP59GKjvrHdXIu-qnaMe5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/joB3UPKyzr91FSCAPE1G3ddeePO8bEcb22F3PWaZkajvFE8OR5eAeVXS-1HlEcRweGXC54tvQqZLxU3AuD6yD-7i0hSsgWsLou_rZ3HM_q5hKwWw2tfU72NJc07geYIkz7LvaP6yxxCOguQDeJuVmwYQoTcRvsWNV6-v-ed1qS30Picg2kDcIjAUHKy-elgPNj-c3uWcu4iU7Tp-7xQdAnjXEZ15bR7p-NWMLkgDxZL5hzX0REW_DpLaGgIYWhaPMsqkmt6ypOPH0FBP2s3XcC2yKikFP_bJTwTrJI-tJD-MinGANaE5r-ftuZP9cU04Lix_nl6agJA8zdinPM6tAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بعد از ازدواج رونالدو و جورجینا عکس های عاشقانه جورجینا با اکسش که هنوز از پیجش پاک نکرده همه جا وایرال شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82333" target="_blank">📅 21:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82332">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBIcsOSEqec2_0GyeYxVh41nJnQQCgwcUiPV8wtLCj_I3vUzei6D0ooSg29DMlpsL2vD-N2SSqU9gm7ZNC7XdaSgMde0xohS-mx0fHYJqoC8oxjZZI5WlvW1lKa0TcK9xUnPMi8MWa6rKmBtbksf4Gall_G1w-acUDb5d-9mKbOU6hvt-3XMoeLkr-UbMFe2azypgHkMb__3c1oLiBYqyDHdOdw7NAoP8s2_QoJD8zSEutsjQwL6KvY247tvxIVxoY-eh4vZYSaLbsa0kUQf_5QGvHBvjk0GdpGsLxO_nC5G1Vtb_1ZoGkBPzTq3wWgKq7aw-6ajZPBw0dVSvPyAug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلطان وکیل بند شده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82332" target="_blank">📅 20:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82331">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vISX5jit2urXGdlGMZm9mbpM-Sy6BD3j1Bes1Gv_prxUkmpbZAWj9kupv4ZJId-CsPkUWoHkuskqDidZ87ROHk5BogETPu6cDXUC_Eyxhs5wGOW6_ydBiv1cvNmsVhxP8MpehUL4PC79PWa7XADYO_MjQiXbm2oXSo99b-UFqj8YSmrLCDeL_gRfj1BkNM-E76UM_PBSeECvrHAOMGe4y8lAnYxCVTAp6nhKjJh-2Vb3oal7KfpP2e2byXmo80ee6ckYua_QuaI0Pzl7ya4_K5Jqwh-gjjlatQZF250XfPH1ir6fIDxZvz1GvCs9u44U1IoFgnXQi0tPPTQWPeP7yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روبرتو کارلوس به طور رسمی اعلام کرد که به پیروان دین اسلام پیوسته و مسلمون شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82331" target="_blank">📅 20:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82330">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sdx5StmUGhAi_p81B8n7fFkiigWrt9bR6-DlBx1LXmXIj3ReVQGEbnbn77SmKcB2AYx0lEVVraheVhtnRrQxL1Ib3Y4NFDl9Xk5OlGoXRvYgoM2KU0D_67-njlA62DxoG03VI8Kps_IAwqTd4jNi_LIlrqEBYcDctG47CYT1A401X1lNh0E-K_O_NvtWhemmBphy6nf0rIPjiQGARuVP94K7cB8u3Z3ZSWdyqk02pxb4HdZVeKf2NzhR_qweXYP2E2KOojt7RnZnPs_LofaMXEHyZG9Xvih36U82X_UWC1jKP6k_iVfqjFb5NSp-fbNEBhB3b99VO52d_GHFhq1mNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم بازا کجان؟! همه این پاسورا فقط 250 تومن
‼️
هرپاسوری که فکرشو بکنید رو ما داریم (بیش از ۲۰۰ مدل)
👀
تکی میخرید اما به قیمت عمده پرداخت میکنید چون مستقیم از وارد کننده میخرید
🛍
•
https://t.me/+5t_pd5JM8E0yZDA0
🔗
💬
مشاوره و ثبت سفارش
@Ad_Parsi</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82330" target="_blank">📅 19:56 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82328">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9efb4780b5.mp4?token=gAbB7wrGw1gozurqZ3gJwDLzNE0OwTiXUEv4xf9HBGEFyVM22uhw2xqpxzhzxW2-reAhk7oM6fT0jc2r4g0AVWNUKkuPoHOZ7YLSxZgTMSzBL0OF0JClSYMxa8FM57IqdfaiNBgNRdkeH_JcskszHXkyGGrRy5AD-HbkTnNrSYDJEkRxb4GKQsDnx0UqY4lv32qLIAF2tFGru5-M1Nm78mJDThA480W9LNsogzk3QuPyrTKT_uNAEoF9vLZMn8-pNAsbDm90hGvAU1SEsdVOw94SonsfrG87PmTUK3Tfhr7inxjtuJhNpfBNxxaHy9h__CIFzSIlFmh4VPTruarQ9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9efb4780b5.mp4?token=gAbB7wrGw1gozurqZ3gJwDLzNE0OwTiXUEv4xf9HBGEFyVM22uhw2xqpxzhzxW2-reAhk7oM6fT0jc2r4g0AVWNUKkuPoHOZ7YLSxZgTMSzBL0OF0JClSYMxa8FM57IqdfaiNBgNRdkeH_JcskszHXkyGGrRy5AD-HbkTnNrSYDJEkRxb4GKQsDnx0UqY4lv32qLIAF2tFGru5-M1Nm78mJDThA480W9LNsogzk3QuPyrTKT_uNAEoF9vLZMn8-pNAsbDm90hGvAU1SEsdVOw94SonsfrG87PmTUK3Tfhr7inxjtuJhNpfBNxxaHy9h__CIFzSIlFmh4VPTruarQ9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقا بابکو که یادتون نرفته؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82328" target="_blank">📅 19:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82327">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKpKGTWIiveT6bGfTayKPajopHIuh_S2RrekqKr3eVWsNCmdzYOgS5yerzY56baq_lKyDVSRi6uUfWwKhgwySlUhF0QGZqD034YrmF9BRjHZ0pgkAe1bAbGaFUyvPg4xfYU8_9P0ZjG4sRNnAWQkBxp4AMlPhAEo1_6xFN2J_u-pjhmVAeuoovosBCJ6Vwse43nuPBfXtXjC_HFJSXt93gDSRJ1BdGXmQuumocOtjalSDwkM-j6afE97kgR-dVezDpJMkHWtPMsQJ7_xcsw62oTlDyQ7rcWsUIGMFjpsqXtdkn90FGu0hjMWodoBHw4FFhhxLYxvkqMY9y2_zzAEUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای خدا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/82327" target="_blank">📅 18:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82326">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9336e75d1.mp4?token=KPEskAQxAVqgLXBUs2JwzVMiZwfy_XV0IuYqf7ZMpcglwa_25LDwM1urJhG7-eC7qnBDj914iWH_0oy21GAHwflYnqG_Y6LVNo-BjxvSAZ9UVVFJ8w7cfpyMnv6KMbGNRvT9OvYgou7TCG87uzAXljOusSKxEzYRPXjcfEW9FqS1rNR5S71yFanwn-21-YLfYhR1AT3cAO-iT3JF8AB2WEjMEZ20pY84B-ttkxbgNSQ51m8HLDXftdHpA1smVGDgPOBm3HVcNRCnjI7CF99C67VBrH0lEoLQoEc705i4Q195Ki6hoZATW3C5MMCoyj64PTxGVCCW0vTvBV5FQFqA-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9336e75d1.mp4?token=KPEskAQxAVqgLXBUs2JwzVMiZwfy_XV0IuYqf7ZMpcglwa_25LDwM1urJhG7-eC7qnBDj914iWH_0oy21GAHwflYnqG_Y6LVNo-BjxvSAZ9UVVFJ8w7cfpyMnv6KMbGNRvT9OvYgou7TCG87uzAXljOusSKxEzYRPXjcfEW9FqS1rNR5S71yFanwn-21-YLfYhR1AT3cAO-iT3JF8AB2WEjMEZ20pY84B-ttkxbgNSQ51m8HLDXftdHpA1smVGDgPOBm3HVcNRCnjI7CF99C67VBrH0lEoLQoEc705i4Q195Ki6hoZATW3C5MMCoyj64PTxGVCCW0vTvBV5FQFqA-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قشنگ معلومه سگه پشماااااش ریخته
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82326" target="_blank">📅 17:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82324">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tP_YZx5h5x1BCcmJD3AZiWafuGGHSWeULQ1YLHX1l0wysmLGke7OM_8tfMp7g5gpy1N3epN1T2dBFgAvMP-Hkf0ID1zYHys-eVzBrIPKJIySej88x5n9MKZmDevoFcInqeq9yr8r5pyfrHsIephAWVPXPvZloCw1xxgxKFHwBbIdc7-llOaRjKpBmn4jKPIPP-vbg9UCkY6qqZ3LyxlihVpXHX3nkCPpunU4wWJlXwyEMrnRSeUdVyKzt6CSUGOQkJVonekwVS80wqDrKW2RlkDFlRGR6-wtYRojd_vcLQ2S8oUuFftQz660ZQPpmKm-gbqHAn1T3fdrkFRButTATQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NQu0-bvoq8H1_q0rsOSpAivHee-PSs1klLLKuxTLEV6wvZDDcAKahqT3IVdKxHaKWJJAYHgnJERZEShBARgAV9Qnb_xmbIjq62bUZZV9jPSO1jz4RZfZHl_Olr06rJ2GMwqbTd6rERiiID9V5bShh6U17pa6RwvD1KcrRuTy0N8tqj6-SX_D6jqNcttrbj4fbVLAIox0j5S-8iZcs8rHZjAWl6tHT22t2iFSZi2ZyCEHyY3QRUa2WZqrlspl6hLHF-auGSynPYYh6wjRBcxF-a2LhfZpOi_wlGqDhWCf-XwcTBKzDFG_O8ZiXPDX2C63vTPcUVgXlLX8SBR2LC63kQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جام‌جهانی با ما چه کرد.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82324" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82323">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOBzwQOlUSe32jqUUC34nKE0d8ols-PZ03p5pNbIM7jMGHucEG3UDrP3XAebs4XEstPmSZQHL1ZhhshZ9ZEq6SpnbZ1pLfETE2wGkFZBuLms1_uFnKsPoEMwMqeMI7yzE4TcI_92Q3IgFvxebB0Lbi39k06TGdIE9MuXHnloJJlLOwwt7SDXLfsUajY-XV4P2RXgECpXmTAyVA0OgaPdlky1tRltiqFYSRYDQ3xNZhXKWJouwEy9gkA0cFxhye5fXT0bXwjUkOZIudAgrTfCSm8sWYU8VOnwVp_WyF0JpSKU3lnVp897mQ1Yj9GhtwMwdgeyh3B7Dw7xSF69UkIhGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس افزایشی بلک‌جک زنده
🃏
⏩
در روزهای دوشنبه تا جمعه با حداقل ۵ میلیون ریال شارژ حساب کاربری و ثبت پیش‌بینی در میزهای بلک‌جک زنده، در صورتی که در همان روز حداقل یک میلیون ریال پیش‌بینی ناموفق داشته باشید، بت‌فوروارد با توجه به تکمیل مراحل از ۱۰ تا ۲۰ درصد مبلغ پیش‌بینی ناموفق را به عنوان بونوس به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/BJR20
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r27
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82323" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82322">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شورای شهر تهران: به زودی اسم فرودگاه «مهرآباد» تهران رو به فرودگاه «شهید خامنه‌ای» تغییر میدیم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82322" target="_blank">📅 15:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82321">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">طبق تحقیقات جدید محققین، افراد باهوش هرگز ادمین فان هیپ هاپ نمیشوند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82321" target="_blank">📅 14:33 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82320">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fk3yQvzvXoREpLf4B6AGkVoLgkDkDQggF-1qst1OYHjjr-kiinEH2Fmo1JlCcqrv_SLTDb4eYOePesfuqG6Y4F8hqytRpAhlGxDRwDNmuO0HJBOzLnYvdcs6KYj0S9-t2aKSVsX9sm6Kgownat7X5QGqjZ83m0vyh5HnnoSpLc98l-5vWc-Q45a6NfXWN61ZXM37O4U9eufEsVjbAo-gBwvGL1D2P3wVQstQ4K6w-pahtFGgnASO9utXBhzCc84YQO03OvN7CHXf2v0VA2TQK8Nu8Wr5FRsB0M2a0z_2s8XfdN1oQoZFPQmFriqKljEKVXREXrd2d4ipag8i9xWFrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز روز جهانی کاپل هاست.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82320" target="_blank">📅 13:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82319">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uI0jY9UDUocLSOYiZZmoVLh8oKduEerwvW7xYx-okWVImCxeZc58TIhaV6ZQYEZAFr-alQnuMFNkWCTzAP0xewjlaqeHGyuYJBiODIfn2dULGCil4sJQ0oKu2PB5kd9luLyedT6EGgk3P5tG57PTNXdc1_2OSAovUY8k_O0ecty1luL92MRbO0V_pXbmAiaWoZ9e3ULuf-Ecqx0p8xarbVIr274DC6Bu3NClqMC_83k-BpqDIWjiVOpmEtV09wkvSGVW-cVmaiFs6V4jAu11JngYIOT7ooN8cANyGLyedeCNalfH8_k6gtUKF0rU3IalOwohWtfu9RDtSGq5csiihA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید. ۸  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82319" target="_blank">📅 13:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82318">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frombRoKe( Leandro Trossard)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSgNqn76UVh41w3nVmyV-nYNyWOdLmHYQTNBDFeCAQPOPSG57onX6hARZtYyGLugLy2lTaJd29_fQNWG4ZEhCxxcZeKSNOy3iuMGIcS8VdLd27QzMQ_eaJyBpQxJS4TG_LIib9mSOAoWZKXX8vB1YomtixsSsSswYBZxdh_6evBV0C3QERkbr2UkYdWpoQbRjDNW5i5xX081fDL-0_UJI3GFvTNubqYKxYFjVi6YZguTzAjdq85ntTegHDjeWMGzvf4QSHQNPRg-fkfS_UvDWWDhfPQ1aI9i-571WtvtQZmsEdjPQdn1SKBhJbSxua9I4i6QnN2G0S5y3ijPyPD1Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت خرید کلمه (رونالدو) رو هم تایپ کنی نمیتونه بگیرتش
😂</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82318" target="_blank">📅 11:42 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82317">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsejCvXE7CWzFuGAbuaYnAO_oK75K2O6xkgKpYXpwHxEtRwjbZ3s4RJ8Q44XZYbqmkKUuUIvEhmMUVGDOEj_WRJYCmWb856GTkcEGekCN6rkQWHWPYdnpsSJpZamDijXSgUlBoJLo9d7dsnQax-elZjMmMCbKcVDriyohd5wOzFrzuOEnWgLzJDCE2RZGt_mm9dP-MXgaW8UJem2y1QYaLeQ1sL0KnHGzw3m-l8YNTh2d5D74mDgCunhg7ivLdNTmHdnX5rlIVrSb4KCkkIoIB4pKTpam4m2nmMdBRhLBufsHiehwZStrElAuUBksSCLus-6_3eJgm2nziMxPpleGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت خرید کلمه «مادرید» رو کامنت کنید
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82317" target="_blank">📅 11:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82316">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RC58STWIwmnqMs6Q3enUq9r9wvMUR2xeL9rcAYPb0SqVkraSpiu_YHiyKBT94vwSP0MMuOhsvLuCXxOYQZpFbcVd8b5FPRezCSInC-BreyRio4UJmoM9fJ3m19o1gsViDUit2GzUBPnDKI86dyKaZRjhzmJJJsHVHSEbv0V205XyM-ZqN17cgZHJ0yKzcxMEe4fzBNwWQV48YNwGsI5UTZyTaV58ArCbY4ahHGrEezzN3Uc-vE1cOLwCRG-CYh5-95CeJDA7p1558uc0_4Gkd_EDPduCU5PoKPgXNuzdIo-xq1er2at0Kk2jfy4npptfNpObaUK2PUrcpcafSVl2Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس افزایشی بلک‌جک زنده
🃏
⏩
در روزهای دوشنبه تا جمعه با حداقل ۵ میلیون ریال شارژ حساب کاربری و ثبت پیش‌بینی در میزهای بلک‌جک زنده، در صورتی که در همان روز حداقل یک میلیون ریال پیش‌بینی ناموفق داشته باشید، بت‌فوروارد با توجه به تکمیل مراحل از ۱۰ تا ۲۰ درصد مبلغ پیش‌بینی ناموفق را به عنوان بونوس به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/BJR20
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r27
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82316" target="_blank">📅 11:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82315">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترکوندی شیر
👇
🫵
🔥
🔥
ماشاالله شیر
👏
👏
👏
👏
و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82315" target="_blank">📅 10:11 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82314">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">حالتون چطوره؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82314" target="_blank">📅 02:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82313">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0ee8dd4d7.mp4?token=SgKSnkjhw12FMzHZhBe75inuTKfK7GmnUCjPUYebYR4NqMxMR6Jc-rLFmJFVftkNFtvTehfRlRk-wCsgJH43MjPvxJxQxLe-iHu-v4Iqw5-g2u9tBVk3IO-3Djd_2dOuSVfCkaeWx-Iv8tCcRcaht9YVkrbLx7w9mh_p9ThYHCz0vERxRTGQUAToP-443NQuWCMoHO7oyLZekPVC7wzooJdjB0L-jxMvWLg-bl2Q864ew4fUJOMQpIeqeqkP7VKz-_3v4E7D7V27O8D-54N99_gOkUHXE3WHA_4ndAr9-_GCRYStFWHCAXAjHwxX_rd8-R70vDayjpYC5MwZkoMbaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0ee8dd4d7.mp4?token=SgKSnkjhw12FMzHZhBe75inuTKfK7GmnUCjPUYebYR4NqMxMR6Jc-rLFmJFVftkNFtvTehfRlRk-wCsgJH43MjPvxJxQxLe-iHu-v4Iqw5-g2u9tBVk3IO-3Djd_2dOuSVfCkaeWx-Iv8tCcRcaht9YVkrbLx7w9mh_p9ThYHCz0vERxRTGQUAToP-443NQuWCMoHO7oyLZekPVC7wzooJdjB0L-jxMvWLg-bl2Q864ew4fUJOMQpIeqeqkP7VKz-_3v4E7D7V27O8D-54N99_gOkUHXE3WHA_4ndAr9-_GCRYStFWHCAXAjHwxX_rd8-R70vDayjpYC5MwZkoMbaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری صداوسیما: ۸۱ میلیون تومن جمع شده برای کشتن ترامپ
ترامپ بفهمه براش ۴۳۳ دلار و ۴۰ سنت میخوان هزینه کنن برا کشتنش خودکشی میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/82313" target="_blank">📅 00:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82312">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJ1gUNKo1vuYI-o-DRX5PC6lSuutVPQoIq-7dyQtrFPj3Ru6IWyalD7Ml2wXt6mpP0DKvlA6D8fEJj4YmfQBHbz8Zge_CY0d6G6L30L1dBTTjYZg57kVjdvsLG2X0QWGwZ4FETFx3GkA3Ch2_3cnw78D42luQ8p4G2q0hnbwD1yX857ySGHOvJfmXnDQ-FdEmmYU4q--MftvdiLnYmL7J8Pqz51QivAN3CeAWnb4vjKHLpP-cEdz0GH4oIlGFkKaF5n87YhNRxhuHRKdP-kuPWDaAqm04jpVPLSeNVQjy4hllbkRjDhAQnqNXvGgxtwq9qQU5cC1hbkUluD3C-83yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم جلوش شلوارک بپوشی بی احترامی برداشت میکنه میزاره میره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/82312" target="_blank">📅 23:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82311">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">رودری تو این جامعه ای که زندگی همه وابسته به فضای مجازیه هیچ پیج و اکانتی تو فضای مجازی نداره و هیچ فعالیتی نمیکنه توش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82311" target="_blank">📅 22:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82310">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_24Dr0AH8uDRkagyoQhBd5EjyprQX2vbrp8uwmOaoEP8SPE2yCN3ZJAGPwY3qI7fG2Jk0ommXCd9uNTT5OqQRvirdEqAKG7HI5Xk_P8pZ0swD60KSzE2t15vWPEzwhmKF-WtBrtJoApnt7ghP5HvICYw_Y7wpIaxx7JSEdSCk_4n8Jbm4CMXr1I_LeY7LHOSMHNxaqYHkDBQXXxM7DsYkG1hKSE7CEzYbA6u9iC8g49HX9RslVGgS7W3H1U5ORT8rnJqMaHsKtlxZi8nCvoeNQToo4NVjNclkioh2qwaplhITWBRSEUaIZrvmdctlnGktA5YjdQwmZI8y3k2humHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایرانی همه جا مالباخته هست
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/82310" target="_blank">📅 22:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82308">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZD8y9oltL_epS6sbHFLKq_odLO0OJxRyDgYHwijM0si8z3XlD5ckhh2W8XS8e8zAbVmHIVj6xCuPPBmSL_6Wkobt-b92CbeUlo0CDzFB20sq6zbbssQF3GUAgTYPUxSpBU7cVI5oCO7Cs46_LM2WMhcvrGbadbeRGA4IHUgmtYQsW-WrZmQX5uAdmLobfPxLDhoqfwpBDGJmx83zLs3BYZDsLPmJZd667nujUiWpHYwsYaX3xCedlk5vRhgJ7H-YnSeSmDPXU-Nd2SCJv-x6SdQjmjt0nU5ErtS91DRgmElTLg2Fm764s4Hz4CkgCOk8P-a9wGS9nB6qWL461c9bYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YCKdEmV39EH_UrVDyqFGn2oTlBUBRksEoqaU3KFyqB5KJa3KwkkVprROklPaiXa8FDR_O_wUNUpcsbq4NsZUeBr0YjjciL9H8vCBe6x-GqfzFcx48nq5npeP3P_njW-8oTUI3BX1g7MHSYAVeVbAVkd97mLnFkPkRuwFY1k8cGYjN13nZjPlBxQUj0mepfmkeLiNMxvdmyO5hVxqwxyEXVoGIReWytSRQdGnZ8AfsYEqOY7vBylfbHbw6iqSsHjnW-whU4ZX0kKTfM_rHRzvxXd21F98wq8j5Xu0_UAUVDt1SAt7qRl-jG7deZFxu1tvTHtDGtC9EZ5kvL6OKjjEJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونفر تو عروسیشون خودشونو شبیه شرک و فیونا کردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82308" target="_blank">📅 21:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82307">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اسرائیل مثل همیشه جنوب لبنان رو زد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82307" target="_blank">📅 20:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82306">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">این چه دیس کصشریه کچی به خلسه داده  Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/82306" target="_blank">📅 19:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82305">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">این چه دیس کصشریه کچی به خلسه داده
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/82305" target="_blank">📅 18:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82304">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQ9BmZ_xJBIUu1aMWFzdj3R6vlIYNX_za0DQXR3Q49n9KlCSHxP0d1ed1IfeiHTAz9HDh15-uEro-8hkFNH-fWfH8HhG1oQwKF1HE_FD1VKA9vaTlTuy21vJY2iUjWXdeH2Hk9QlIXGiHVZl9r_X0PuiuXXCjSaRVWjuPzMjDyXCSw5WNmgjcpZDt4pYL6f277XfCPUmOFlgWiUkAgu8d1q-yJCdqSbFWB4n_ki1CloUUeCRDXIt2K6LyZdWsp4lAr2AToZRuu2tq0WTU-D8QM7WdqApHWNextWFlaoTZOVueP8eWUXtcJumREEdwsBt5LlNjE4RHfGHiGg9wRsU0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لرا پرچم بالا
🔥
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/82304" target="_blank">📅 17:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82303">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U43yUw2lZrO049h75ILRynebMf-0_YTSJefbET1TTPJ6ddkzk93WiiAV0a-T8rs6emEsGqBm9_9vd_yp_0vTR3SFFPjQIIncolR3ATASIoB3B3kmdmXpF9pgReS0LFQzL8tPFlMynbVhyXO2iozrgzoZb_zVwfHss_zJOydD3a-q6oI8f9YkupcxusO3iMM1TSfnX3vFrKm360VsmN_CUs-fgJW-AzXfJEZwEc97_4PVrcofbiRu3XlnFJl4qjGj1qOFEMUl9NgrJB8H4kZBCK7x89h40nY5vkov9Xmf6m3-ADxHNJiI7Th8-IgSVpbStlii22ct7iJxj4-DHwyJaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت تجهیزات و پوتین کماندو هایی که قراره جلوی مجهزترین و قویترین ارتش دنیا رو بگیرن:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/82303" target="_blank">📅 16:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82301">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/485f8430bb.mp4?token=alJAgQKMHHCOiBXqtd9GaAlK5FVI79O1MmVrh7epJph0ycdjfCgJIEG4IEFuXc2YCQ3D-F60D4nnR_Joi2_soB2RDmB3MrM5TyT2y7WKQU1Qw0cpU3Pz1LgfsrQkqhOuV6njQMZOteinHFckrzsRCB_dZiHM1icgZJK6lMCrZV-Nw0AbSWgn8MK5BN6g2ZibsVnNqw8aWYR2XB1MHjKDbB6wPFlYPBAScyBYSVG0oKJ5PkNkOhXgomB4rIJullfq0WulQLVBi7DgiwvRdDRzpGqabl2G6-o4NS7OopMT7YJywxfG6vlBE_LnUNUDtGz9kCihvgFcOsxbl6vR3jsACQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/485f8430bb.mp4?token=alJAgQKMHHCOiBXqtd9GaAlK5FVI79O1MmVrh7epJph0ycdjfCgJIEG4IEFuXc2YCQ3D-F60D4nnR_Joi2_soB2RDmB3MrM5TyT2y7WKQU1Qw0cpU3Pz1LgfsrQkqhOuV6njQMZOteinHFckrzsRCB_dZiHM1icgZJK6lMCrZV-Nw0AbSWgn8MK5BN6g2ZibsVnNqw8aWYR2XB1MHjKDbB6wPFlYPBAScyBYSVG0oKJ5PkNkOhXgomB4rIJullfq0WulQLVBi7DgiwvRdDRzpGqabl2G6-o4NS7OopMT7YJywxfG6vlBE_LnUNUDtGz9kCihvgFcOsxbl6vR3jsACQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صداوسیما یه برنامه جدید به اسم «با عرض معذرت» ساخته که توش ترامپ و اعضای کابینه دولتش رو مسخره میکنن :
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82301" target="_blank">📅 16:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82300">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSr1d6IgSn_QRZ3V9AoWhy2FEocnLwtPSRTilkfFR7aj3aQ370953sBwFMxoGb0FlgrdLShsrHXIhK68J0xa2enaF7HoTz5i09Mnk3yHzMn8ew_4MbBmhNHEvSbnhSlpC0JEFyJe3CDr8yyz-ECWKNAvpjOxVxgTN5k0QrnS9uy7f1ICGDgygZirEE0YJxi4MUCeX6gIamr2d2tUvOBtqKDhpJ2NSAIN5o_syqP74bNftrUwjs7EBzJVTX9QSGHtuO0aebgXD13RdXNtLoxL7cQluN_0gvsIyot9lG2Y-fWKRt9_9eah3up9YQfueaEl0ArUqFLPWm1EdHedP-18fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس افزایشی بازی‌های رولت زنده
🔘
⏩
در روزهای دوشنبه تا جمعه با حداقل ۵ میلیون ریال شارژ حساب کاربری و ثبت پیش‌بینی در میزهای رولت زنده، در صورتی که در همان روز حداقل یک میلیون ریال پیش‌بینی ناموفق داشته باشید، بت‌فوروارد با توجه به تکمیل مراحل از ۱۰ تا ۲۰ درصد مبلغ پیش‌بینی ناموفق را به عنوان بونوس به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/ROUL20
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r26
💻
@BetForward</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82300" target="_blank">📅 16:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82299">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">شایع این پست نوید محمدزاده رو لایک کرده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82299" target="_blank">📅 15:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82298">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXCj9DdfAFa74AYGIxjNood2kvPCccnCBB8LBKh3-kWnTZcBgzPP2fTwpM8CEcNTpKK8KIMXTutJUYifJR6J3uxpOOwoBeJ2S6L6UUFsiFz8l895bOPcfg02fl7ecxkPwp-eXyZZyKVCe_j8SSG7psZAiUFWKZZ1fBBMTcATpeFsIoDGKMXQxK_5zixYHbBZ1cwPUyu0die73EvZpzs94Adi5WnksbPNVdtmPxNxakq2TmGNWY-Vch2OLXY3wlmfQt2hiLrXwfSy1T2fs5tInnttK7uGC0wPwUWfxSy7n4JkFwY4dZkVTIEb4z4iPNTiIo-8G8ihmpKsguDfOka7sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوید محمد زاده: قبلا از فلسطین حمایت کردم،الان میکنم در آینده هم خواهم کرد چون با اسرائیل حال نمیکنم،تمام اسطوره های زندگیم از مارادونا تا کریس رونالدو طرفدار فلسطین بودن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82298" target="_blank">📅 15:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82297">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کار کنید حال کنید حال کنید کار کنید و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82297" target="_blank">📅 14:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82296">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDnqP2XY30H7RKzqn_Enxn87BGsXhKdmBfvGt1QCxmm0odpsZ8jLZCjXnSROtUK3MNICMihEKUS0EIovytFghx4gtsPjoEp9UDazThBYyHE_688H8dYZG-Cypt0H3R0bavPAjdBvauKnQrYUOHVmyyzlo9Z8HzjQDJct6dy91Tjcy0Ypg01bSIdAhqHzPFcr5CRK1ZMy5MxrzCKmLbXwapLrlQxkf98g9x880BUXWkz_wYlxVk4xtQG7hp9eEWDpV17M3J69qKSfIcVARD1rL5yt5bZm4diOvYQX9UjA2wp0cVmWUMy5WjUlEx0eD87JCG5cTteFTk_PkZH_IAg_ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرداری الیگودرز لرستان، کف رودخونه رو آسفالت کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/82296" target="_blank">📅 13:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82295">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qd9MUBPLeUM7LOY0Ytf-2p2IzCyw3JwDPIAckMGIVwXDVrC-CHHTKW8lG8gpUnb4Xx3NIuxYe9l2udHZaHRx7J8ZRbrlgYuhWTYB2heYCMmHEp663AcPz3fnd4SNojqO5J0Ak6zvXBfzUrIsb27tLYdEwS9FK2VPpbQHYe4AaDvrN70cjE1fmBoGvHt4BwMXzx15v4zdoU1JZF8vWyCOuvcjnzSpDYC4xcVrae5gESwkp3hi26F876yuvlv6nquDFE7m0Fce5MkPmRWnF2Cd0eAT8vUuP6TeePvnF6Dgn4aCwzrhOEcQ53QBFQe8gVjxlbzYLg_PbpIqNEiIow7nCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک میلیون نفر نوید محمدزاده رو انفالو کردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82295" target="_blank">📅 12:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82294">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjLUeOiFXednAV04XL2g_IEI2zmLiXpmkVxdQMEq1yYcAX6kN9P0iwfs_b5MVQdxGDCCzx1EDVrXrCi-vTW1KMcK_bsVasQbITjb7cg3bqY2LWDs_uijkJuuA9KPGVKXIR8Vq4wzxk71-dbgDGsdS-yHTZbbIZQZXMmeSc-i6PaFFiyPFR_Th0_99SCFOa8Ndc1uchlj_cV3rpZ5rYHY8RFdLEeKVhVB5DNiJkUCR5OfuuFjM6eeW_I5ZL4Djlk3hcWypbE3rb8gG7qXJ6ybPoRUf879DlSiuEaeRDuSv-hG7lHJTTDBPkt4x2j1YTVzzVwWiYh_g6pas9kkBHhAbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/82294" target="_blank">📅 10:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82293">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNqyoRW9dqm-7Wp4uHjbJs-t31sH1JzEgCITzRksLxF8KRbg3c4IMy7_-vlCX10eSx5cx-jqyYH93kXGwkhLF_m0K2bjItLKvEsdtaksojmK7HuxT58XUyXBPZ0uu0dIKhWxhG-Xo3r9H_CetL-YPPlbiXlSaUt1P3N0saFoyH0iJ1zPF_naunBZmJfonJ6VAQMzl__89VjxEoWr8hvpbR18QfmUU_zXn-aFRwvBQECRQy1OuIpF644Xk4EuB7szLgYGE0M6_rIbnzbW83XMJdXdToo7N4KHXS0K8svc0bruul-wrpTplUdLTMaArPW-qc4ZpxrZ8O_vW9KpVUNgiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریستیانو رونالدو : احتمالاً این آخرین سال فوتبالی من خواهد بود و می‌خواهم میراثی فوق‌العاده از خودم به جا بگذارم.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82293" target="_blank">📅 10:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82292">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGxgF38NjdMZOplmv-BeXFoeFujIOY_QPThygshQKcZjTNVYO9DoSEEhJn2ob1QYrmMZQdmLb6_zcNoXOTd7IajF43k-KxqkMQnydNGlCOtGYZG_56xVNv6tl8G8pp0pt3zHHQIYGzkBOtrqifhYi5p74kGsKunIEW350TjN-ZlDuc2J2uD3vf6jh6PHIkjL5zB2-Ch21lqoQFvaSh7T5MaXBnHJCDn9kVP3rOcWG9037a2vz8ntHFKIWPrhPlR-PO_ZafP27-t18FjY2eN2TvR6X-0dxWqV7cTWCrINlARe91yd0bCa5T-iebU8BvAMzIL7LOnqMRvdlQJWy6bX6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس افزایشی بازی‌های رولت زنده
🔘
⏩
در روزهای دوشنبه تا جمعه با حداقل ۵ میلیون ریال شارژ حساب کاربری و ثبت پیش‌بینی در میزهای رولت زنده، در صورتی که در همان روز حداقل یک میلیون ریال پیش‌بینی ناموفق داشته باشید، بت‌فوروارد با توجه به تکمیل مراحل از ۱۰ تا ۲۰ درصد مبلغ پیش‌بینی ناموفق را به عنوان بونوس به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/ROUL20
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r26
💻
@BetForward</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/82292" target="_blank">📅 10:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82291">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نوید محمد زاده: قبلا از فلسطین حمایت کردم،الان میکنم در آینده هم خواهم کرد چون با اسرائیل حال نمیکنم،تمام اسطوره های زندگیم از مارادونا تا کریس رونالدو طرفدار فلسطین بودن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/82291" target="_blank">📅 02:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82290">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نوید محمد زاده: قبلا از فلسطین حمایت کردم،الان میکنم در آینده هم خواهم کرد چون با اسرائیل حال نمیکنم،تمام اسطوره های زندگیم از مارادونا تا کریس رونالدو طرفدار فلسطین بودن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/82290" target="_blank">📅 02:07 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82289">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoLDXVOCdR17i79aY-ObAwnGCFiWuiGvVEG7Cm8KaCKzhOwsFIGvBqyI3z-lTgS-8uhiJPkgjZOPJAi1Ja7lVv6sSpTUq4c38-v8itaCxcNpjJRb5InC2KSKSbv8VmRqERorQPVR6GuGmyPdwkqrKC6V2fNRm5yQwO2UlboQ9-Fe7qDjlVH_29WaxRVrIOsTZzTMmmErrLPkXs5UJRb84wHeDiIIyIMR49qqbYb5NKWEg6OBSv2g_OptPFy45zDccJF3ojLneGhn_UhWps0lMTH9Qg0GpLvQ1M0Sd-iJ5Afmc9CE_lcFzapGbnYciHGeaabMJz8vCHZdYmWj24KxpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اثرات تمرین با فران تورس
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/82289" target="_blank">📅 00:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82288">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">5 ساعت و 45 دقیقه دیگه آتش بس تموم میشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/82288" target="_blank">📅 23:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82287">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIo8yz_dkgopRNp9CS7qqyezFO_mfiUyymZxYb06xr0bYqJE4gRQ4077JXe6gyh85c_RL4ULI_YAm00p-s-rNPRHtFEq_l4RcA_H-ajaZ8vmxskHTJqo07HMtHuM6qcX_WNbSmfjMJ-_DDnxUqZLXYUbLwQ7NTg6zX1zFQexsw2AbEPNdjg42UlQDOfK0cfW1gfMJr3l2h66vdMWf1JtG5aZS2-3jSeOCBYXLMjLi-5XSPJ42R95By-Txdp-bJMsq0uADVjaDhyQu6cr5gP7vrWv8J5L8iLSjGpGFVOCTxrgEHvlJv2GQ7AsqWAD2TKzuPUkHK9xb0_tElyfD8-ahw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیمی رو معرفی کنید که توانایی مقابله با این خط هافبک رو داشته باشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/82287" target="_blank">📅 22:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82286">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X74lyNUn-eZkZdYITupX0izS8YjMYYKojRckuaoIToHIbTkn7bZ0ZdQV2NQ7mXtFynY4MiA7aVN5pnXESDLKjDh6dVGXBjrRH0obbPWOzHVtOG0np4e3SEG19Iu9YyIlrtKwy9PriC4qBPA2n5Ns0W58f2RG2pgLyzIKWr-uGdPca5PYH1lUQ9c1BkDpfPNGrCiIpSJS8Q1GfMqYXCtobn4aDKb5verykREFTByocPFT_O7prPHDvcfhX-Amuk0OY_vG6UjQxrxRXzK--kpNWRtrklhS-11qa_GJwzjLPVJ484_-lHihkyanHAhOvBcoUsjPRWcSkBkQXRwNW3nMFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیر وی گووو
🔥
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/82286" target="_blank">📅 22:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82285">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDFQa4pMZ_Lhi1tQ2DWU54L5EnPcHUOGsKB3b0LidpvPDw1756wFwtEM5AmnTo0JtK6faLMBCiMMd7TK3458e80Tg8ThamErvpi-j2_c33JES7Q7avFymqhVHNAEnQWMfRiQtH4sGZyiHYHpILnO_Qt07VkQAS7tKGU645IUF4jPHs7fKg9Z2JVaghEAEdxYU24nOVuyuQx9EuHTKDFWde9RSWuSs_G1HTIpq9ENtBpB_niC2vPDeAceOGwc1haq6fpP8XEFPNZSNKgOGBa73q1MOx5qsndBtSCXHQHMPsNaMeu5LWvfv63b0tJgjod7N6L3DYDEu_vHnfZqmH6b9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخرین تلاش های مردم برای حفط آبرو
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82285" target="_blank">📅 21:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82284">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd9bdf52c.mp4?token=URAjy4UBKB6e9LJLAs-Vt14o_y424EMwCH2ABZoNtO8rJ0HsljLlpsta794pteprWQCS5ZIe8XGRrXMFhacMtSeZ3OTbqXq4CUsI1TMF-zp0Actrb7tz62aXFxQvXQnLI0Ju7jw60Uz7pCfmQmA9kI1d2xFZFaUhvNigNEgjVYW4BHjcI8DIap5lXaoGNzOCdE63jc6I3mQe7E1wnmWwRd3INjlFa4jmCLBZ1uWtqFOWY_6xqehmZRXHSHlsoSzKUYFJvVxJuZW0GLXw1Ki6KNCvkHokd5sqTenY7zPnO2CyLN4jXBkw17rgCONQiC1N9kFq6nnQY1fR-2NhEC6LP5vEmWvieIzMXOv16HR8O6A-UtboZHcBDzJme1ujLRy4gHprgmP58wZJtLSX76TvUJSI7BG0fW_vMcbZMtgJmxgir5ptpRBNZrgsxNoSxRFq3SofX-HLQvuc7CHnQPj5CPbg6RmF3urriB2TT7Bh-5uXDI61yFt_3vMPgdVDKpc2gkihHQRBu5jvRVtm-cPCB6sAVogx1MW9UPzgaV85oBm_whrvKdnf7a3zhWiSu4rmhnfYsAmC_jKnMYGsmCE_8jDpbPcqZGM19w8vZU3NOr4m5T0uoWfboI--7Szpd56Kh0WxRFz-JBZ1WPInoWpMS0rLz9fFY00XcmSCzcg32yk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd9bdf52c.mp4?token=URAjy4UBKB6e9LJLAs-Vt14o_y424EMwCH2ABZoNtO8rJ0HsljLlpsta794pteprWQCS5ZIe8XGRrXMFhacMtSeZ3OTbqXq4CUsI1TMF-zp0Actrb7tz62aXFxQvXQnLI0Ju7jw60Uz7pCfmQmA9kI1d2xFZFaUhvNigNEgjVYW4BHjcI8DIap5lXaoGNzOCdE63jc6I3mQe7E1wnmWwRd3INjlFa4jmCLBZ1uWtqFOWY_6xqehmZRXHSHlsoSzKUYFJvVxJuZW0GLXw1Ki6KNCvkHokd5sqTenY7zPnO2CyLN4jXBkw17rgCONQiC1N9kFq6nnQY1fR-2NhEC6LP5vEmWvieIzMXOv16HR8O6A-UtboZHcBDzJme1ujLRy4gHprgmP58wZJtLSX76TvUJSI7BG0fW_vMcbZMtgJmxgir5ptpRBNZrgsxNoSxRFq3SofX-HLQvuc7CHnQPj5CPbg6RmF3urriB2TT7Bh-5uXDI61yFt_3vMPgdVDKpc2gkihHQRBu5jvRVtm-cPCB6sAVogx1MW9UPzgaV85oBm_whrvKdnf7a3zhWiSu4rmhnfYsAmC_jKnMYGsmCE_8jDpbPcqZGM19w8vZU3NOr4m5T0uoWfboI--7Szpd56Kh0WxRFz-JBZ1WPInoWpMS0rLz9fFY00XcmSCzcg32yk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنها دو هفته پس از هجوم قبلی، دوباره هزاران مهاجر از مراکش سعی کردند وارد سئوتای اسپانیا شوند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82284" target="_blank">📅 21:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82282">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tA5gbuLw4LbhDeuyb6U-nHsqCAqZ7DAz8zWYTYK-dVLklOWwiSUBpaf01DxcWzsxVh5F7qMK-nmQ_8tGsgziuOf1pV8sQyhg3G1yzoSVHEmQx3CzOxFrnEiuEWeWJ89KgrTv3t_8Pc7dP_kj7TRfpjhReNjXiGHHqP2n4ReQUv5AO2b6JsxAWbsgZLh_U_pTbO5Ic6HIZpZ7FVAAl5cdJlo8nQVhtmBC3qEIi5eD7ufsSq5asukv1-JXBjnMzI_Un21toV5kuMm5uH_c5CALeczzCmGUQsp1rS63xymJgWlxKqUNePbu-du3_EXtLawHZT9Ipc6X5OOGjqz8w5sjbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید چرسی تو چنلش  تا این لحظه تنها کسی از بین اون ۱۴.۱۵ نفر که قبول کرد اشتباه کرده و معذرت خواهی کرد چرسی بوده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82282" target="_blank">📅 18:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82281">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پست جدید چرسی تو چنلش  تا این لحظه تنها کسی از بین اون ۱۴.۱۵ نفر که قبول کرد اشتباه کرده و معذرت خواهی کرد چرسی بوده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82281" target="_blank">📅 18:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82278">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UTFur3YkL7pSPsb8UU0kxuD_HV8-JzpiyidRFNpX3EQwBFY9FGfG5CK5l1rHAEW7h8zpLPwszKMAfcsnEAOtt_Z90ePsJwXPgWlgG9t5Tg0VHGkaRFZU1DKA3Yh_vzAqLX5kItIYN3uWCdmLFf3w1zmupV6eYxYVDZPkcwJFqA0OLv66NzOB2k62trOm7iA-j-urOoSEoi2ilUTCUrjpepQtn6_cpEvFHJJNeqJ9Fz1LpYjhb-mtOj3VlLz4EX2ki-dzbqDD96wTvCvZRGJHLiS1nqO4EGnxTXlyEA9kwGH4sbAPZfQ1pPqxlhd5Ml22CTHPZRBpDdqoPv6wm_uluQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/krB7vC2mhjBe6yZ7PBtEFVGnUHTLxF-tgZTLoq7Qcqyrhj7c-LaRZltOmF4m1Rw-_J5I4JIHBD9T0MADOus7uZ_oZ3RZ1H4nKeqpzFyB3cWi_e_hh5kT_m2GoY5E1j36PUlrb_uEUzObL4DQSSVNtpIncMR4q-kxF8ZmJciJ0Q3p-ERbNtORBtBr6OK_MX-aHJNTcLLjsZ_96oNLFZ0DMPpIcZRQ7YeQ1-xo7ORXNk0i2cO9RKowXZxav4L4w_yBf61XTIAN55vzg-wrv2U37mcezajC4eMxHapfdrCHKLF0Qk5PvDCnePHB543623FnGxIVgP1_kjV4U6gDCDMo3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست جدید چرسی تو چنلش
تا این لحظه تنها کسی از بین اون ۱۴.۱۵ نفر که قبول کرد اشتباه کرده و معذرت خواهی کرد چرسی بوده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82278" target="_blank">📅 18:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82277">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSN-vvd3-UuIKTvRrqisho6ObJyaVUphjPbdgDoPW5bZdjQOCf6RBu1hfIYSIGkVmNhGhvqYNIcZz3yHUNBKMMuVwhh-Og9SkCWNPkQGEtDH4roUBKG7Y3XEp9ziaE8dXiqclXJK0nrvDHHZSuwVCTY2pLEAuHtY3Xt6QaUAsUJeg5m9JMZDgpcyLaxUqf8O6qZtCroK1aMEjPMB0gEskK6VkIxyr1IO0fuzegWea5Ryu76hbvaHg6-ryQAlnw73i2YsqAl7bhRYdTWZfalum0honxQdPQj9MyPynI8SnqcRESdWd5R7VgRaAuGBM6fIYzc7qzVkDL90cFWzBds9lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامیار این کارو نکن.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82277" target="_blank">📅 18:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82275">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">عربستان جملات ضد اسرائیلی رو از توی کتابای درسیش حذف کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82275" target="_blank">📅 17:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82274">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWq5DXfLH_YRs6mMIcjbF88ALe9_PksnqSmLRAsrMP09_rKXg2hRqZAAlJ2WDu5C1_wq1lNgPrm2lBSQNMwhsFG6jfcFZnQhUFDEeogD7L88Oxguy_pty7Etdp4wX2x1OHs9XeOlgU8o-aRFWnwh4R_YIgQ9Qvw20N881oxxkOI0Y0VWsIrrT2KZAQb5ox09LQOosREr0KftjiiHaPkH-XwaY_M7tzSwFw8oDBdYZt1bDEm3cMGLrZXXfpDAviXbObJuZFIg52zEdJUAFh6_vDuAPKchdtby7D9PuUofe8sF07EBhVOqI6GD6SBq67BcDzSKRki4mwXarNahqMaDuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامین رضاییان رفته تو دایرکت یک بازیگر دو رگه ایرانی - آمریکایی به اسم جول فرشاد (بازیگر سریال ایفوریا) و ازش عکس نود خواسته و ازش خواسته که وارد رابطه بشن. نه تنها چند خبرگزاری خبرش رو کار کردن بلکه این خانم‌ هم این موضوع رو علنی کرده و گفته بزودی تو یک مصاحبه…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82274" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82273">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C035vNPr41kTS6K7Tid51h30CMxUzJ347DM1NXaLb7dBDAs8Cax8ch6mwLzXIM6kD9oad_Hj3Fvw197UhHBOs5mCv3BuygxgMYNQep0vHzUWbGxGz0C7m0T-c4NybCgZAWDD9P3dB8DNwe7rjLzsy6URxEwl9OLDV-AuLhcaAUudEhJtLhp6GAqZediwqZFpgjSSTpzQa0Orq992WLo5hdQdS2LTiuPTcXTIYOTnARZj0nTISnTvPLSFIx7xRZL75tIqX5EU_1xLlvuRYYLEjTQSZYSrk6ZanLrK98SmVdlc5p396AMkQybptG78ZcXsHzH2_mOnkG57xCWnaLPOfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید متین فتاحی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82273" target="_blank">📅 15:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82272">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYvnStHiPnoA8Lyktymf_ROztUNFDhhW7TkJVkNpfU5YRLMzRdF5SHjZEGWiKg3-Ua1_ef2fTkRPDNxg9xY4ALdyF-CzOqdei4oxVWL_z5q-c6xuhP856DGuYDc10FzVikYRE0gbl_Ky4TCyiXNIIag61wR6UBsyuUqBM1g2uMCpytbJCq8nt0_d2cxs-qWW-kIj-mCSBFbR4mNaV0nc95v40J2JARYxITPN4UK29ePpgvn9t2WrYUgvvs9BGq9f8HL3_-MWlj5edHU-FDN2lV6VXUBNRM-a6h1R9GqduUvCX5PajG1JwblABGeALrlzKt6MwoQsRcCCqQq9OAGgBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرامو از مراکشیا یاد بگیرید، اسپانیا چون عاشق اسلام بود بهش تزریق کردن که احساس کمبود نکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82272" target="_blank">📅 15:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82271">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNw9avSHmfJir4W6WYSzt6ChjERie28ifQwMXq9l2sD-nqy01M-bPohTVTcrIJfGw8k5H41tTZNahrLHJ5N9YprXlPu3_eZDYJFA7Q8cbDfwqKnRJmnzykcI29X9DC66QaiTSBg__HcNsjbapWEibidmGr-m0G5ZYpX7rB9QPqNOGurds6U7pqeqkXtPXsYx1nBG4sJtBJ5-VnC2BytiVtGOSluhdLDoRUgxhM6Z2ViODEfoXiOYMcqvXth6NpaDIclfyjHwhclC62duVrY-yWE6pTkMJEa1n-iGPokm3EDPVhkbJaDlpnX5Vdj0ghEkmQ8ltp0xOdsAT2HNi7nURg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سطح اطلاعات و نگرش آرتیستی که خودشو یک شخص با سوادِ سیاسی و تاریخی میدونه:
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82271" target="_blank">📅 14:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82270">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فرمانده کل ارتش:
هر ایرانی بتونه یه سرباز آمریکایی رو اسیر کنه یا بکشه 30000 دلار میدیم بهش.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82270" target="_blank">📅 13:54 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82269">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1569dd1b49.mp4?token=JwMA542lMIp4J9eW_heXlSH3xx9X37rtl1uPFPs9alVKY0HcCIZAhi_y-7RBzqSVeyGciYIhC0_uzhvpReMLqd48VAsAltcR1ta8I4E_3Cze36NWK7uHBNhpPyWMVCcvxvey_cf9yQHiWtfJiBs2M-CylqBgNLIpl0cM0zaOx2_3ER3w7IePVxegkgvvqVPIYvIeezn8THK1IYot1rWKXhhkMtK41RRb6J4jZNK6h-qfpKIE3SnC15QEtxFrlj7a7eiWEDoIvG7OcA1K9u4Gch4rCZd0gtbX2LSE4SqKsB-Zjsv_xvRMvkA9681gpDe-EqGntah8lNHo0l6vK9UQsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1569dd1b49.mp4?token=JwMA542lMIp4J9eW_heXlSH3xx9X37rtl1uPFPs9alVKY0HcCIZAhi_y-7RBzqSVeyGciYIhC0_uzhvpReMLqd48VAsAltcR1ta8I4E_3Cze36NWK7uHBNhpPyWMVCcvxvey_cf9yQHiWtfJiBs2M-CylqBgNLIpl0cM0zaOx2_3ER3w7IePVxegkgvvqVPIYvIeezn8THK1IYot1rWKXhhkMtK41RRb6J4jZNK6h-qfpKIE3SnC15QEtxFrlj7a7eiWEDoIvG7OcA1K9u4Gch4rCZd0gtbX2LSE4SqKsB-Zjsv_xvRMvkA9681gpDe-EqGntah8lNHo0l6vK9UQsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تهی دیشب با زنش رفتن کنسرت د ویکند.
یه i love you هم تو استوریش نوشته که من متوجه نشدم با د ویکنده یا با زنشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82269" target="_blank">📅 12:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82268">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fwk2FyjHbd-AhMw1YOg2e1wU1MrjyoWDTreMAN3IwEeptNKotQI8Fk1yfKZuKtMWASUeFkDGuA1Y3VWr9vaEDo9NXQgdlHV7f4sbxiT1cK9TAHCsZ2OxSTil327AdszEiLEpcr5bLZzv6wR3tHgk1P4VreltSuBXGD6ZsTUNFDHQc4T6MT6NkR6DffhdI63q3Lw8UM5bnOdHM9to4hUCy1AspbWVIdzWzlHBVyDr-ef6OJtuCP3EHjOCRho-nCQrAlHlG1UkcMdjTJvYYVuag6siEvXGpT0MQ9_pDZNOQ06t9TTGtQCw738YJozxIWeLMkKBWe9aJ_g3-2BUjlUy8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب دیگه کم کم بریم سراغ ایونت  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82268" target="_blank">📅 11:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82266">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3TiH3buTmNGhCkbnWw8rbyleOm_lgnxv4k4-1F0SDnLtcmpEuRlj6d2ol8MFl7O53_sg1Z6EC4vN9GICfJVR0xZU9jp1kGyt0Lc8FRxrPmrSpPR8XNjPQ-STiY9nDqrnbJYvI8v0FGtLld7TS7FT33EI1knk9agtEi4Emme3a8L5Oh5wOnvwsxAoPVtItaxqE4__2TJdXjOa9abx5wUXf_PVTMJ28iw6H0eg3-ywmmwp2AAEjlZLdTSEdmSXz4ReXiyNca7vpwRUY1XhejLTCMK72UlI3TBNSJwXlJg6ys7Q5h8ec5G0HSuOYR9JglT0AqFStWi4LnfFkUnReJy4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرام صادقی یکی از معترضان در اعتراضات 18 و 19 دی در کرج اعدام شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82266" target="_blank">📅 10:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82265">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Npk0pY2qES7c3g8m45zK55Srr2-F8PDJbgDQZ86T3huSF45J6PQ6slkvBybqNJ8T2UfHj8IAnlY9Yb45QkorLlhjgVwa4TUutowaWyhNU905t8vOSKQCevnBPv_7YVQMXE1eoPgCddzFJH7M4afeX44iB0XtxAEMP6UiY-6UGpKzoyiJ3kS0XfC9KZrKluLL6uk0Y56UuRmG7sAuHiFuOuIPOGzpo3MhdZwZ6I0sJgor3KQ63sViRpEQ5NGaRTjZoiOdfe1coFnemv1ZgABXWwzL3y2o2PeppLVFi-eEL8uKN9D44cuY9XzHWBYYWzqB9C5p_hfxmwFOJGA4eigJwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راستی پیشرو سیک سینابو زده و سیناب برگشته ایران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/82265" target="_blank">📅 08:09 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82263">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CL-GLqidjObPWNjL-l2tMzHR1S2ujmazV2tXNCbFW7eeE1VIaoVAvreGDkv3BJ60g2OoEZJQbKx4VR94vKh_uIvsv9yylKnePyBKaWBX7FkRPPVjt3d772wgUGEAprW7zH7M6v_FpnaIcPm5Vn_KRh8affJiflofL9Fa7NW3Iv5nvVfNqYb-ysHLE11MI1rBPkmI1LeQ96ggufUI0vg7ai9osHsKVCWXgjlwvR3jpZ1ttd5otb1e8glNQcmEonGCF5jaXIJmwqgGZeCbJUUrmMEy0jjOU7WSCslr3laFuYGLeUkJXpbCc4F6rD0U5UIuqEdL5aLfq128VVBM16-hzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب دیگه کم کم بریم سراغ ایونت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/82263" target="_blank">📅 03:29 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82262">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">توروخدا به ملتفت دیس بده یکم بخندیم  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/82262" target="_blank">📅 02:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82261">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نمیدونم براتون مهمه یا نه ولی دلو فردا ترک میده، اگه دوست خودتونم بود باز بکیرتون بود؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/82261" target="_blank">📅 00:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82260">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAcM4TCefGq-pi4w4DRmMvRoU9hoPfC4DiTiuYAcS48ET-6Phf4A6dNQFfVVko9HCg5HGojW8-ENeaHQbABVxoXo0j-1SvIYSkN3wdUhn8V_RnsZBdO9FUNpPwz921eWNcNkusfSldJ6zpDktM2ripUz7-NGE_-Q7f5QzoSQ8daEdfSqAK1KCJjr_-kRy-shy1yxh_3iBVy0tAvTBIcTOGTl4I307Pv0O1mYjRr3YnHVuHhX8D2Pbq3e0DRXYYuF7NZ-JEzufgdVtRMVUdTqSGFq0lG8UKBdia-teAcXjIVdkd9xlqHfreaVBr_CLwAgDj86ecEr9TjiB_GSyGbFOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظرم انتخاب خیلی بدی کرده و رو چیز اشتباهی نشسته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/82260" target="_blank">📅 00:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82258">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/atPR3pe0wtOml7Yi32iEI9B3oVHUPPXjuWQtjCicL1ykRzP3teKkRsURLdx1NrqtcfWGe6K75w77pIfNlrerizrA35tVbpt6_RwhHWXBtJbiZzR-TlOJ_M8hFPg-PvTW6YbME6nm_9kj6bGVMmS7gvgIFvU3ucp9XLhWxZnUlsVvXx-cCliFk7ZMF95xxj7R4mrIuNDxenpZvQkbxF58GOa1foDDdED3Id07K8h6m7qyGXoKChVKqxrmfc4nZ9m7sZD6AqJRmS2vIKounKomj50p23w3lvxcnBWWmP_TBK976HVJmKBF_Cc-qv1KnHK9Q_lg3HjD7SNag0QlwvKQxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F6rYnKVAuKvI_9WtcnNJutl6Keqnct8TojAYRnYn2-J5g_2XQSQKhmMBTqQ5VFI7YbUZx5O5sxjrS4QttfUivWEC5Oz602cJS2EJUhf9vxQ9iSlaBiFg_3gcDo0DdLSEIq2m4QOkYsjbcQXa5e8pFhnROH0-yYV0ZZj3KzmIPALjCrY4YBBXFzwyrUV-Kd0HW21UMB3oMZWF3MzZrZZVMbv6mcky8RByuoK8f9gnquzwGy3U1dYPjHVvOi4E4Mqt92M1_eGVYGxad--7dF2sN5fJR72BiJjf-vDXrbImy2xc-KM07rwYI9PsJ2mTjoDTcxqvGH8oyPKkWsCps4kpCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این اوبی میرفته دایرکت ملت میگفته عکس با کارت ملی بدید عضو گارد جاویدانتون کنم و اسلحه بدم بهتون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/82258" target="_blank">📅 00:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82257">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
احتمالا همتون داستان جدید رامین رضاییان با کیس جدیدش (گوهر فرشاد) که چت‌هاش رو پخش کرده رو شنیدین یا دیدین؛ + حالا به همین مناسبت یادی کنیم از زمانی که دوست دختر سابقش طی یه حرکت منطقی عکس و فیلم شومبولِ رامین خوشگله رو پخش کرد :)))
📥
مشاهده عکس و فیلم‌ها…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/82257" target="_blank">📅 00:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82254">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ihcPqGszJAq4RXU3BDfrRnq4fY2KoQG32O5l9wlKnO1136u02dbGOhVoD15G7duSJ4WTEfP53lbX9puU4pgK2NVdyQHq0topv5jy-4U-mzcSOqplXEV1oFqPMdLuEwmISXJS61hbWLgpUq50LpPCTVZn-sSafx0Siy-TrbLWuoDcKleW4Y_AwEgfKhpKq-oNKJ2AoFqGDq8LNsnHhXRmbMdyNvzKKLPdLRoeWVOmOI7NT5eFJXNp5_1b3JqFQ6x0R4_aoy5hwfVp1tRiqqc0WXzVZ6M6PGhOE6OhQAI-eyETqk5oQnYlocVlvGtWacoJEgxxi0duBN5MZVR7U4xGOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bElrkN9932l_dzwYsD5nQPFh_fBnr-trhWOxhxiUamMpVlDzWMrqNE3URH3lG6u9nGpsom2HmMiI7rwG-7rrtICuG37h27MehHPYcTSdB6E_Un3Dl6yapYYrB49-SM03Akv7QfDrhoMiPwZZ5KQ9xvsTOeE1J-9gMheGJj4_CBLx6Y6EIHyyApAymPXc5LFshbv8aa8B-QMSrO6OCMjrsp0a-mneUZnPlMpb1dTmm3EGDI_dqYQmqq3V4qim8Ta-AoPqF49MkvTNLwJNQ3-6JqcH3D4yUVHrVWYrIlQx2pUgHjftAT66mFFB7k7WVRbTDWv3Qg9noV8YTymxXRh-2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WHKq6RUvZthxqpLziWLVkCn9xC74RWhsGBzlLmG-dJMsEowH134pC3VH_GC8M3L8ebRmxHnUUxLoqyRdxr5QmdrFcXdXPv58sNmGUmQWJ5m8Mp6kXozfp8G5yojVTSLQliEtLIkk157ORomLyOXdQ6swvXOakU68ztUFL1CQjo0RCK6zT4t0i8WcVgUn2i3LcNlK2kjLVVetBtNSREt2eiNi_iNLZzjeYy_5F8BbLJy74GGQiFxxuxFCczm7pTu5FhDUrGFaDOuYCVvFScokG2oxIaXYn1-ed6ZEw-nvHlO-mXVhK_iDcipDNJf19oVmAhc02HK_qg_MsPqJEEFmUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
احتمالا همتون داستان جدید رامین رضاییان با کیس جدیدش (گوهر فرشاد) که چت‌هاش رو پخش کرده رو شنیدین یا دیدین؛
+ حالا به همین مناسبت یادی کنیم از زمانی که دوست دختر سابقش طی یه حرکت منطقی عکس و فیلم شومبولِ رامین خوشگله رو پخش کرد :)))
📥
مشاهده عکس و فیلم‌ها
@TopTel</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/82254" target="_blank">📅 23:50 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82253">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">روسیه بصورت فوری تا زمستان ۲۰۲۷ صادرات بنزین و دیزل خودش رو ممنوع کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/82253" target="_blank">📅 23:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82252">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d727b7c564.mp4?token=o7ydPB1yKOtZg2_x6vpPlyH55pYz1G_uDDcCTr9TMVlxhaWBxDB0lnGhu-rNIw2hhzwOQhvi3Cx0HFCiO3RU2HWruujfK9vhf7J98s0WJaQiL3cjrbVW-Cn9-cTIzPnkU4dSxOxYvextLJfnesYFBKgUc4D54wfDnef2t_pbTbbCPLxTwNK82-Ht6fOOaQoKvBOD-rCnjjuz4Hm8GjdSmwvRHl2t8yxpidq-a1bUn3Vy1rpx9zyQY54ABkjt6H7SVqq1vFF7YT826TsJwDT1nCCrqiE1wrxfhjjZByi9rVJywBWafiJQSjfeLW2eXv1pCmB1L5oyyZyxXkvZpNQYYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d727b7c564.mp4?token=o7ydPB1yKOtZg2_x6vpPlyH55pYz1G_uDDcCTr9TMVlxhaWBxDB0lnGhu-rNIw2hhzwOQhvi3Cx0HFCiO3RU2HWruujfK9vhf7J98s0WJaQiL3cjrbVW-Cn9-cTIzPnkU4dSxOxYvextLJfnesYFBKgUc4D54wfDnef2t_pbTbbCPLxTwNK82-Ht6fOOaQoKvBOD-rCnjjuz4Hm8GjdSmwvRHl2t8yxpidq-a1bUn3Vy1rpx9zyQY54ABkjt6H7SVqq1vFF7YT826TsJwDT1nCCrqiE1wrxfhjjZByi9rVJywBWafiJQSjfeLW2eXv1pCmB1L5oyyZyxXkvZpNQYYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کصکش فقط یک دقیقه‌ کیر گوزیدی، چطوری تو راند اول ناک اوت شدی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/82252" target="_blank">📅 22:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82251">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">راستی این یارو امیر علی اکبری تو راند 1 ناک اوت شد اونم با ضربه جب
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82251" target="_blank">📅 22:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82250">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سلام فریب جان سیریک  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82250" target="_blank">📅 22:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82249">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سلام فریب جان سیریک
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/82249" target="_blank">📅 22:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82248">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5QcdfHhFNS2bRIfSmzZYTpZLUXF_qCDnn311WHqBzkqMJ8pk9bj3OCrMfVa2tkhVgFB_In-KvOp-Nk4ki-a3KC-9doh2gUwzemD6Jpzokmpz1HcVC7iLUhDSshdxsRgMB1B13YGmapBWztDHPa1Zn8BQ2MHFiY8hrPD1Zvf_Og4bOsbQaYEo7pMoo3fT39yhl-app5vO9kbpgrydHbbdDYQxUEkXOWnRWTyFdQQtOuZWbbBDZ_qMEoE1Syt28IcHMop1vFoXM91UkydZStRo7Yn189nMuWJAFVEyJQPSIr5_xVDFIFJjY7XDcs0YWwql-7s9Fz0-2WYCikIvcxmAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامین رضاییان رفته تو دایرکت یک بازیگر دو رگه ایرانی - آمریکایی به اسم جول فرشاد (بازیگر سریال ایفوریا) و ازش عکس نود خواسته و ازش خواسته که وارد رابطه بشن. نه تنها چند خبرگزاری خبرش رو کار کردن بلکه این خانم‌ هم این موضوع رو علنی کرده و گفته بزودی تو یک مصاحبه…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/82248" target="_blank">📅 21:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82244">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eK39H-ptZftHAMM5Ml1ZJQhRLFHgZIRMjUWY-V8abV7l1vY8NR96go8V0hoiWPlm-2EOEyObKY5f-ktUGjdXq5gaH7G5DV8wuucA0c8SUOjBZxvEjMzDb-YgxfeHdNvIoO4eC2aIkfBrz-f46T3zWbBm7S36E_6qRQQ5aNyBd9MSTelo4aZQ7pGQqeBY1mm0R0t9g3VSHr68QAbTE1cHrO07kS-cur8PeYIzdEPAi-z6SEgtaRqCGW0AGbNLcys7C026graXUkJYKgGRVUaXc30FtdOZddcVL4jctNZeAxpOR7-MY8gcYCLAALgwSCkQoQtfA8ThPu2syZSh9_KhQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل نصف حیوون آزاری های جامعه این بازیه، فک کن وقتی بچه بودی اینو بدن دستت بگن کتکش بزن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82244" target="_blank">📅 21:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82240">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یارو بهترین کص ها ایران اشاره کنه زیرشن بعد بره دایرکت یکی نود بگیره جق بزنه روش؟
میفهمی حالا سطح تفکر من و شما و دلیل اینکه میگم نادون و احمقید؟</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82240" target="_blank">📅 21:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82239">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7ITcRuXcLG3_mC6NKAvHImaKxpFbqN0apP_m_G2_MuCqoIcM07OX3hDWeNCmXq4olmm2MDXzSMEfNQ48rkVjMWvswZ_LYOIa3BKyDgoNVAMddiNA1Bo39sTyJ0B2iGBFb-YAODV6gYR4VdYuy1YFx6RXxjeGRsp-hkGHzVFjtiJ90sT5M8k07JYRyNUmPldV7UfROO1L56zfgXKuxUQA1ROC28wPZhvuu9uwkStAS_i9lViCfH3iGry-Ze5-0FxN7tWiEuYatY6_wpGrlJjlawjNFAJ76AxbVcATrQxUvOQcEfhOnz2WrolXSBEF6pG0MphaDU4AXQ44Hh4J-i86g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامین رضاییان رفته تو دایرکت یک بازیگر دو رگه ایرانی - آمریکایی به اسم جول فرشاد (بازیگر سریال ایفوریا) و ازش عکس نود خواسته و ازش خواسته که وارد رابطه بشن. نه تنها چند خبرگزاری خبرش رو کار کردن بلکه این خانم‌ هم این موضوع رو علنی کرده و گفته بزودی تو یک مصاحبه همه‌چیز رو میگه و آبروشو میبره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/82239" target="_blank">📅 20:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82238">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پرسپولیس تارتار بوی سه گانه میده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82238" target="_blank">📅 19:38 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82235">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aJimePeCvQsjzMlXU2vbHXUGcQG5fRxjgKrNt4dgtggZB5JcmiUhgoq8EREyxRTMD0ihj2bXr9x9WMm1w_pVFEQFW3degQ8gW63csGzjVtRjzc8uIKJhjjaYCVzq8T3E0kcAj5GH9MhrMaALC9Ik2g_uM7yQSoVDQGp1NOFeR-KX8H7s1uCyHhPJB7bnt_rjYg8aINexxQD3liUuZACeieUKvsx2fgQF9AA9HL1amnHmGIwDaNpBbrs6-zu7A4YyphR2ay65x_u-PS72PbrH5W4JwEumpTtD5xEsjZi7-pGJpMLPMiutsUzb2J2ItlmC2ZfaeaMtJkwFLRAsWanOEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aCKovXiEYgZj5H7PUfFeGWk7G92II1BsqH5XNONvin3ya0DEh4sGALjEntsrq5NvMwtpve4se2NxY_zOpwmZ4ixcDqOM0yRTmqIz4lWI5GgsuDABWfy0bfehjPwoPxv-NIpvYL12g9Biw3H64RVWNozmbbTOpX6FKvrpDDbHNeRNKBiy9NuGoMsBjTDAY4yWckNzi8oVA10y1YIkwDsqYUZq6l_JNEZHX9NXSZbIYQnmCEdOmA2-3wHU3m-nGOn7Erl763qxJXumqZ_Q4l-Q9MOPj9nvyihdyMuA92C0cSx5HntyaduQbLX9V-2D0fWQ5rYaXmhCptjiu8gNHSC7jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aqLYww-7JOzSTGS_xeiXWvxkutJhMgqejdulP4z0_VpTl1Td-uBd_g2jmI-2Gnf1p39FfE10TNG7jxD--slNKptmX6n9M4DxdfoHAv-_deURk-BXs0SZiMa303csYL0H8r-JJjpUWwbqmgI3I2tRrQQHOJtrvBN9XFDp2GUYdexvoTPn2-CDBewHTOECz_9o6bVxFGedJhsZ0KooJz4qjlN9H1tJmi-0SDjbYObZEbTH_mMuDj4nca7fkR7c-oVYQZqT03y7ksr2zTnliW--9MI_-vluAKvBNoJKU-q0qW1j5Sywko7SU_UB9hQO42IXupHaifPT7WfmU1stw2k03A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">افغانستان
🤝
فلسطین
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/82235" target="_blank">📅 19:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82234">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soeHMFiavHGGkPbz7byCnYESfa0_PSYngg8VOrIIDzh2pMw1PpUl1I4djc9pYYjgdpVlQxhwQaQfTXtEjY8p1IX1D2Wn4-oglalDH_rLN8VGyQ1emsKM9LsRBd97iF6ft9UdNzXxRHNpHCjnEDSWNrM74DCVtfdB5bsDXey2Wlet5C7ZqdjLOtDTLjl7dUC2T-CgFX8N0kIGSjoy1nj105EMG_KY_KIfYfpUnX6Ux6GFb4-IHN9T58oyg4YKWHjSIFQvZu2L9FcyYC2USU7GEkphvTxMMnfUlArdnb6B6LWw0qTt1S2M7pK5i-F14poUFhQBJeJZRIsVHbmvB_Rd3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسه دیگه محمود خستمون کردی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/82234" target="_blank">📅 18:25 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

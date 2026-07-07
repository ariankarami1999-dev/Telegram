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
<img src="https://cdn4.telesco.pe/file/djxZJL032Xjs2Lwb5RTCxPXPPL9rgtkBICFLTe8nQTjXAN0fsk6XzLiJTv_vtJ66LGnY_ea-F5X4WnygEeZ1pjUhuNBCsu7v72T98y4-pot-s3HbCuY00GEQHW4ZgIJBoqHchyUP5lyu8ie7vVrai4dH996zWAp5scvna0PpVMSCsq_ebPmgbgXvAo9nn08P-ta8lJyOxLi6yofK0zxGSMrZ3-s5YVqPsYfNCFVqm0LyqX_3TFcKgtJwgzuY3uXHhNPcjRPAzjIlVkO6P_xg_05sfco92W4OYKMt5W4PizUfX9MppfT0eQLrBZPhVqkH1_QWxVtWB1q60gQRfH3FBw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 19:49:56</div>
<hr>

<div class="tg-post" id="msg-447960">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c2759e33f.mp4?token=BnD4b9TknoDZ7oGAT40498y2IA11Fboy4c2pl08uRtPyeUAGtQeOHhYkjGmgSvfGUOMT5Vy_hmhLqx1EbIN_2COezUiZ4i-lRA0Bn1WWdqGVaxjdPdBjn7FzO1uILUNw_S54U-bOX6Tzu_tnzPM6AJyImwJT1CXKVe6d0P5xWtykmDqHBraGQePzgzBOT0axMzFcUBegQLe3RhnGijPYDDzWmtQKDn8LZgsBmzoPsV2fLv7a9LSUOyS8OcaYAT8MQ6EI6BSyL_VT2K5ykgItsoFi1XltaDqDMVBEt1rzZ6d4ue4ILCN5TnSJ6gBrpGoUmFZJdQ0n24GIOT8r-I3W-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c2759e33f.mp4?token=BnD4b9TknoDZ7oGAT40498y2IA11Fboy4c2pl08uRtPyeUAGtQeOHhYkjGmgSvfGUOMT5Vy_hmhLqx1EbIN_2COezUiZ4i-lRA0Bn1WWdqGVaxjdPdBjn7FzO1uILUNw_S54U-bOX6Tzu_tnzPM6AJyImwJT1CXKVe6d0P5xWtykmDqHBraGQePzgzBOT0axMzFcUBegQLe3RhnGijPYDDzWmtQKDn8LZgsBmzoPsV2fLv7a9LSUOyS8OcaYAT8MQ6EI6BSyL_VT2K5ykgItsoFi1XltaDqDMVBEt1rzZ6d4ue4ILCN5TnSJ6gBrpGoUmFZJdQ0n24GIOT8r-I3W-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول مصر به آرژانتین در دقیقۀ ۱۴
⚽️
آرژانتین ۰ - ۱ مصر
@Farsna</div>
<div class="tg-footer">👁️ 700 · <a href="https://t.me/farsna/447960" target="_blank">📅 19:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447959">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c7988fbbe.mp4?token=co6UMCIrcQxE0QYQt3ONCLYTkPuETLl73ySWCvxwqmUsGxmCOiXpvRl_ypM5yMugiw9NWbUr__w0EafIO5M8cf0tAYYtMwnHTYPSwN_F1jqw3DcvVL4mo2zqJlvSqau0yRDkZdDA7b3PCCu1xyjdZJr4CyHH-IqfhHmTs-UZ1iL4GQIwKgMuZjzVFhKXc42ZSCa08t2-2HGSbAHxRj1aSZQvrkipLywhYz0xJ1iu26NG987o37RGjndoNMhYzoG2a3jFh-47d2Tw3xb_8KJv3PlBQ8yrlWcq5upiPMMxfrV1hh_COFfrpQqyjsQWRk1MLwPu-a1SE3VIm-7JEy4bYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c7988fbbe.mp4?token=co6UMCIrcQxE0QYQt3ONCLYTkPuETLl73ySWCvxwqmUsGxmCOiXpvRl_ypM5yMugiw9NWbUr__w0EafIO5M8cf0tAYYtMwnHTYPSwN_F1jqw3DcvVL4mo2zqJlvSqau0yRDkZdDA7b3PCCu1xyjdZJr4CyHH-IqfhHmTs-UZ1iL4GQIwKgMuZjzVFhKXc42ZSCa08t2-2HGSbAHxRj1aSZQvrkipLywhYz0xJ1iu26NG987o37RGjndoNMhYzoG2a3jFh-47d2Tw3xb_8KJv3PlBQ8yrlWcq5upiPMMxfrV1hh_COFfrpQqyjsQWRk1MLwPu-a1SE3VIm-7JEy4bYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استاندار خراسان‌رضوی: درهای حرم امام رضا(ع) در مدت برگزاری مراسم تشییع و تدفین رهبر شهید باز خواهد بود
🔹
البته رواق‌ها و بخش مرکزی حرم برای مراسم طواف و تدفین بسته خواهد بود. @Farsna</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/farsna/447959" target="_blank">📅 19:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447958">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f0274261a.mp4?token=E3OXtBPZEhHWVF1LBLsgLjbOJ1WPqV1i0w11lLhJbAotrHhlEP5T4T8dAlT2L9eX2ziMoRVCp6_DAJvGhQuheuJVVgPjZq-nbdxs29_gINH6Wnw0rUHrrBuAv961BBbJuIMMW9h2D6GXfvkPQ_n3e0PlX8OyR5-Fix-WW2jTErY78AxqRUvq9VMo4ypNGojsn0CHtHugNQL8wBSf5ZTHxwRaoCMXh1gcY71NXUQl3ScmOecWEEFFnBpwjriGxiWcIvkhIedaQYCa0P08QV2Z85qo81BQP1QF1H-70fg8dxOLzAtqpuKJ9kVU9e3dsjVp7Soew4I9tnxnuGJauDNWgw0CRZe5PqD2p55cL6JnSV4L9R9EtH3Zo53rBl_gPt_r-r7-lejZtffHJb9cAY698iW1XVI8vsr-iQWvQuM2gK0g0sBEh1t5ldKTQMt46ENO16Z1tD0HMTLdtVPzcyuvRzhN7IxVPaFEDxoBwCCrF44THkLcrjFAH8fkt7Qj9YJz450vfO3vwU4sV1AVuuSofEKGnxxcnnFSWvsxFEx5Z6Z9PmpDqm6BQImdzFHncqiJ0jPA74N_J2yKpzJ3PqfRzzn4RIN5t0dl9_r6BEfLkdisrnxqUpbi-A9raLxz0YTpA_Ld-0uGdxn3NTsgnIGkLG0vaiD582H5qmNZpZ5V9Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f0274261a.mp4?token=E3OXtBPZEhHWVF1LBLsgLjbOJ1WPqV1i0w11lLhJbAotrHhlEP5T4T8dAlT2L9eX2ziMoRVCp6_DAJvGhQuheuJVVgPjZq-nbdxs29_gINH6Wnw0rUHrrBuAv961BBbJuIMMW9h2D6GXfvkPQ_n3e0PlX8OyR5-Fix-WW2jTErY78AxqRUvq9VMo4ypNGojsn0CHtHugNQL8wBSf5ZTHxwRaoCMXh1gcY71NXUQl3ScmOecWEEFFnBpwjriGxiWcIvkhIedaQYCa0P08QV2Z85qo81BQP1QF1H-70fg8dxOLzAtqpuKJ9kVU9e3dsjVp7Soew4I9tnxnuGJauDNWgw0CRZe5PqD2p55cL6JnSV4L9R9EtH3Zo53rBl_gPt_r-r7-lejZtffHJb9cAY698iW1XVI8vsr-iQWvQuM2gK0g0sBEh1t5ldKTQMt46ENO16Z1tD0HMTLdtVPzcyuvRzhN7IxVPaFEDxoBwCCrF44THkLcrjFAH8fkt7Qj9YJz450vfO3vwU4sV1AVuuSofEKGnxxcnnFSWvsxFEx5Z6Z9PmpDqm6BQImdzFHncqiJ0jPA74N_J2yKpzJ3PqfRzzn4RIN5t0dl9_r6BEfLkdisrnxqUpbi-A9raLxz0YTpA_Ld-0uGdxn3NTsgnIGkLG0vaiD582H5qmNZpZ5V9Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم عراق در تدارک مراسمی باشکوه
🔹
آماده‌سازی‌ها برای استقبال از پیکر رهبر شهید امت اسلام ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/farsna/447958" target="_blank">📅 19:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447957">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0736ea3351.mp4?token=MpH9V8m6fh6-A3O1U07OIy4oleUCGqJx3b4cS79dCATCgBqvWYlkDAYY-FbfZ9BJCFAuWszzDIjHuQzqM2P0KHfxUKfoYK6Mf_WU8oBQAewrs1quneqHfvMxj0qys_U5fxV55MWXoiRQ_Al3g7pGZz30yixdFFuLUdlAx2eoy4S4fWCM9qdzSka9JbE3fw2gX6nRg-Ivy7ldnq4UYSkXlcORPAw0E_6Cu37RRoYvrGjzp7gU450Po3dLMHvpify_4ytnJ2OcstPUs6km6-lVf5XuX5l_koIiI7nFYW-yKutq-HUeD13J9Gi6QVr5fJMRaauvXZCg1paGkseQS6pQmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0736ea3351.mp4?token=MpH9V8m6fh6-A3O1U07OIy4oleUCGqJx3b4cS79dCATCgBqvWYlkDAYY-FbfZ9BJCFAuWszzDIjHuQzqM2P0KHfxUKfoYK6Mf_WU8oBQAewrs1quneqHfvMxj0qys_U5fxV55MWXoiRQ_Al3g7pGZz30yixdFFuLUdlAx2eoy4S4fWCM9qdzSka9JbE3fw2gX6nRg-Ivy7ldnq4UYSkXlcORPAw0E_6Cu37RRoYvrGjzp7gU450Po3dLMHvpify_4ytnJ2OcstPUs6km6-lVf5XuX5l_koIiI7nFYW-yKutq-HUeD13J9Gi6QVr5fJMRaauvXZCg1paGkseQS6pQmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استاندار خراسان‌رضوی: حوالی ساعت ۶ صبح پنجشنبه مراسم تشییع رهبر شهید در خیابان امام رضای مشهد آغاز می‌شود
🔹
پیش‌بینی شده که تشییع ۵ تا ۶ ساعت طول بکشد و غروب پنجشنبه هم مراسم تدفین انجام می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/farsna/447957" target="_blank">📅 19:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447956">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63f377383.mp4?token=KXX28f0GAVa-hCXZxSwQCDJJt5XsPC9EFicAyyLfBZGIX-pRiA8twYGa7747taEvo440Yexp4higPmZywSbBgpN7ec5I7Nn6Avpmlcw3mqenN1q9uh4wmn0gkWWLcwezpPJOoOYdkGleldWbuxInFiN5rcmQBQQ7b3E-Bdw0XPK7y6fqAo-ba5Aoy8EjtGMEnHZDUTC-W8-HV8JjH-RBxT9qOEaQ0vDSqDoQEJ-8B_YA4zKyJjTfiqTSXdrEk-Pp4DInlF9ZtfNNVEKTFXatfwiXJhKIUmcqARPBbONehXQT2rnYEaK_FGFQo93BZlVeUx-B5edyBg5cSH9w3miILQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63f377383.mp4?token=KXX28f0GAVa-hCXZxSwQCDJJt5XsPC9EFicAyyLfBZGIX-pRiA8twYGa7747taEvo440Yexp4higPmZywSbBgpN7ec5I7Nn6Avpmlcw3mqenN1q9uh4wmn0gkWWLcwezpPJOoOYdkGleldWbuxInFiN5rcmQBQQ7b3E-Bdw0XPK7y6fqAo-ba5Aoy8EjtGMEnHZDUTC-W8-HV8JjH-RBxT9qOEaQ0vDSqDoQEJ-8B_YA4zKyJjTfiqTSXdrEk-Pp4DInlF9ZtfNNVEKTFXatfwiXJhKIUmcqARPBbONehXQT2rnYEaK_FGFQo93BZlVeUx-B5edyBg5cSH9w3miILQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استاندار خراسان‌رضوی: حوالی ساعت ۶ صبح پنجشنبه مراسم تشییع رهبر شهید در خیابان امام رضای مشهد آغاز می‌شود
🔹
پیش‌بینی شده که تشییع ۵ تا ۶ ساعت طول بکشد و غروب پنجشنبه هم مراسم تدفین انجام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/farsna/447956" target="_blank">📅 19:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447953">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JYpGxySQJqlvhfazLSqELmY9xuIxYSa_Ghi_nguhYgRZHnZ0HvX3IEVMcXx7OSILaDFdzO9MOgZt2mnuutrEjJNU9PC80hUM9g-x7CnSbUzMC4sxGmi21uC-2oP9TpIlsMarUSYSRBIN-0XVW_ZyLOMBvOby0kC8uqNOblRqMmbxJy3Cu8KzsdqznLP1YdCm2be_VAej4X5uxUt8pIhjg3bBq2yNX-VNvBkXkzCt4IpPQQGpBCeQzLkZu0T5MNfm3xX7SqVWyuZYEmnWk87oDYTi1jWyn8tP34AQWdA7HiQWLyi1cHEh1SpEaswFIU9bYzjvODIZ3B3tqVcXL113ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F3uNI1aEKaEMMmd4A3qi-21wUcDQ6qCcaRKV4b8qvF6Iy1UPl4OvXMwBytgvboMxtMvXYKKlVjgCedg_ZcG4iDEApObQOyXXUIyALTwNBLvLJ4rxBJzZQ05Ig8PVrM-T-wEme0hKWv1HtNx_BYcWwQjXtN-8S-JEBKMc94WlDFMd7cFuq5uRD1DCZnG5EROYZx5Olcd5qv_3EnyeH_9ja9ruLhiEKgsjwm1YdXre0HIgAKVoAe6NsfXgeGaD-QZHG6YgkAdzTnY2Ip2eZk4DjY6rPR4B96gK4R7lwmOHPIrpqKEoARSmIiivGVGkeUDNb7Aba2LppoHlYzO3Qde49A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QUhD21dTS54CpSqgxemD8eNAvOVieoUiblQqbDpYMs6cZPilX_y_6ngRafmU5Ep9rsgniUtWRXBUUBD1M1aCejmoRQtDbUYq0FwDPycyUCFn3ZZ2kwUs4TBqnWQlfcklt6l-tfhbrjHDCjlrjtwNZDZI3oeyxWPKj8ceaErQ3veITuyPJcD9H8E8rA60JBzIV7AFyS5AyowDwydkYLI0tcz4OTIbA62xMma-eq_kHuuIlHVfZc1BlV6AqgTkHJIYukaD7_9DBv2xV_V2tkBJwzV5cVGs1ZJsv4UAQlM8dCu6GkDqKVKIgEgFDwGLVTZ4Y5RtwV0Z3SThVmA0u-_ZCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استقرار نیروهای الحشد الشعبی در مسیر فرودگاه نجف اشرف
@FarsNewsInt</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/farsna/447953" target="_blank">📅 19:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447952">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پزشکیان راهی نجف شد
🔹
رئیس‌جمهور، به‌منظور شرکت در مراسم استقبال از پیکر مطهر رهبر شهید انقلاب، دقایقی پیش تهران را به مقصد نجف اشرف ترک کرد.
@Farsna</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/farsna/447952" target="_blank">📅 19:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447951">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/199cb5464d.mp4?token=RdxOl80Z7B8XBsw5oan_KswUyUPmxDg9axV7W6bFj-63vriyorq8dC7VPAwqakSHsxzJLzn8DithDKgz-kNf6vsBPn3lfitgc-68QQreWyM6tv7AcIx8AMuT1HPMUkMlmYkfffVTCcVRpn4p7CwuncpFR4VGlhACydnyauuuxHoCSX_mXPMuae5YLbGhq_9SBdnzunjnP9OC6QwYgCZrmc1ACP41wZz3QuUQKvbnMY_cHYf1ICPyPOceZtPRVIl-bfxK-TGJHgrIXBbzyJ7FuGEksIxq1YwyJ1X6_iJyEcbWKaIKHHhJXgrD0-vj0Zop8MVWReda-IQL3d_Eprn10GY93DO_rLHY7_uA9UURZhdx6ifBl6DhnQVrGtUgjXat6XUivnFpO4Z2JPxXUXjgVP0i8XtKXYskAnPhm2TL_YR5KshGMyud01MOSOvWb1ClT3rw3c-xuKVcQLANtWZ4a5pidysmTnlg5RW1mhLnffFYtY7FzviEgPGnvvA-KLuUNbPE-L6H-p1wDEKlCFOri3lukGb20Q2cYq3-Ir_S-Ew-rNp0idbRrtjCOQHR3usxOAEekJWgJLwG3YkFOtgRIK1YV2ytM_47sbYHYxKT8rXe-g0W-3sYH6MqM-ajMHZboTczBBjddTXWSQ7rciW_KwP2Djhj8R1jNPJYnvIkGzY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/199cb5464d.mp4?token=RdxOl80Z7B8XBsw5oan_KswUyUPmxDg9axV7W6bFj-63vriyorq8dC7VPAwqakSHsxzJLzn8DithDKgz-kNf6vsBPn3lfitgc-68QQreWyM6tv7AcIx8AMuT1HPMUkMlmYkfffVTCcVRpn4p7CwuncpFR4VGlhACydnyauuuxHoCSX_mXPMuae5YLbGhq_9SBdnzunjnP9OC6QwYgCZrmc1ACP41wZz3QuUQKvbnMY_cHYf1ICPyPOceZtPRVIl-bfxK-TGJHgrIXBbzyJ7FuGEksIxq1YwyJ1X6_iJyEcbWKaIKHHhJXgrD0-vj0Zop8MVWReda-IQL3d_Eprn10GY93DO_rLHY7_uA9UURZhdx6ifBl6DhnQVrGtUgjXat6XUivnFpO4Z2JPxXUXjgVP0i8XtKXYskAnPhm2TL_YR5KshGMyud01MOSOvWb1ClT3rw3c-xuKVcQLANtWZ4a5pidysmTnlg5RW1mhLnffFYtY7FzviEgPGnvvA-KLuUNbPE-L6H-p1wDEKlCFOri3lukGb20Q2cYq3-Ir_S-Ew-rNp0idbRrtjCOQHR3usxOAEekJWgJLwG3YkFOtgRIK1YV2ytM_47sbYHYxKT8rXe-g0W-3sYH6MqM-ajMHZboTczBBjddTXWSQ7rciW_KwP2Djhj8R1jNPJYnvIkGzY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون اجرایی رئیس‌جمهور: رهبر شهید، جمهوری اسلامی را به گونه‌ای ساخت که در برابر تمام قدرت‌های جهان ایستاد.
@Farsna</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/farsna/447951" target="_blank">📅 19:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447950">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🎥
جزئیات مراسم تشییع رهبر شهید در نجف از زبان سرکنسول ایران در کربلا
@Farsna</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/farsna/447950" target="_blank">📅 18:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447949">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">هواشناسی با صدور هشدار نارنجی، از احتمال وقوع طوفان و گردوخاک شدید تا پنجشنبه در استان تهران خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/farsna/447949" target="_blank">📅 18:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447948">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/588ed1bb1e.mp4?token=Rro29_c0NbWfrW-1q5DYdlx1y87JFT6uUiTQSqOaUJVWSXb1d9QQFoYCCNbEDqvuNNtGV0s4Wr-iZMVZBlsX_v4teLbaZ7P5Xs9p74f7PZSiKdAkb8M-aR_k0RgElsz26_cg9XXMa0HC68dV0qzyQJDTMWtc8XDZoZw3NhWbYaWhN6Z3JUqzq1fQGjtMZVnbcN0cxUvA25FS2G_-OkCkW7nIz4MMCpOTV_ZU6qMogRV1vD1n9XD459NLJpzR6s7egjKEr-UOu342P95kdkFLCnqlrDcSZaka3n9gG_O4H9ZMnIGA18Brpq84oMVXFGEw3sAzdwoPUT2AuPzO7vMMdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/588ed1bb1e.mp4?token=Rro29_c0NbWfrW-1q5DYdlx1y87JFT6uUiTQSqOaUJVWSXb1d9QQFoYCCNbEDqvuNNtGV0s4Wr-iZMVZBlsX_v4teLbaZ7P5Xs9p74f7PZSiKdAkb8M-aR_k0RgElsz26_cg9XXMa0HC68dV0qzyQJDTMWtc8XDZoZw3NhWbYaWhN6Z3JUqzq1fQGjtMZVnbcN0cxUvA25FS2G_-OkCkW7nIz4MMCpOTV_ZU6qMogRV1vD1n9XD459NLJpzR6s7egjKEr-UOu342P95kdkFLCnqlrDcSZaka3n9gG_O4H9ZMnIGA18Brpq84oMVXFGEw3sAzdwoPUT2AuPzO7vMMdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کهنسال عراقی: با شهادت سید علی خامنه‌ای من ۳ شبانه‌روز نه سحری خوردم و نه افطار.
@Farsna</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/farsna/447948" target="_blank">📅 18:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447947">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">حرم رضوی مهیای میزبانی از زائران و عزاداران تشییع و تدفین رهبر شهید
🔹
قائم‌مقام تولیت آستان قدس رضوی: محدودسازی تردد صرفاً در صحن‌های مرکزی حرم رضوی از ظهر روز قبل از مراسم آغاز می‌شود و تا پایان مراسم تدفین ادامه خواهد داشت.
🔹
تردد در صحن‌های پیرامونی تا زمانی که شرایط ایمنی و مدیریت جمعیت اجازه دهد، برقرار خواهد بود.
🔹
در تلاش هستیم که شرایطی فراهم شود تا حتی زائرانی که امکان حضور در صحن انقلاب را ندارند، بتوانند در نماز مشارکت داشته باشند.
@Farsna</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/447947" target="_blank">📅 18:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447946">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d824fcad1c.mp4?token=apZR_N_xlkQdCD6kPcDNxTaSsDhfacFRndh5wmrOKvcX8n8VVZRBwHY7g_jMHh-V-Lb2XnUTf7QGPnM8GeLfTlWB-8B_Dt_yXt8P3J3URJvHv_emNIuOJcP2ZCouBhnjgz1ULeCHg1IQ2V0t4BoQriryrcz_CGEUMO-Ixcb_u3SgbnI93LjcE_C2hXYPQcgykBddZ6CmSIbBD5j0jY0qxpoXuLLvSeWbs5_uTcCCUmGYEL_N3P3S73KATNi34V86Jsn3Qj-INo7n_gUgz_0BkjGknHdcdpaenmz5A0zfyLaMTpOn70J9-uozYX4z5Qji8mIsCFhs_eEjIv20jDO2pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d824fcad1c.mp4?token=apZR_N_xlkQdCD6kPcDNxTaSsDhfacFRndh5wmrOKvcX8n8VVZRBwHY7g_jMHh-V-Lb2XnUTf7QGPnM8GeLfTlWB-8B_Dt_yXt8P3J3URJvHv_emNIuOJcP2ZCouBhnjgz1ULeCHg1IQ2V0t4BoQriryrcz_CGEUMO-Ixcb_u3SgbnI93LjcE_C2hXYPQcgykBddZ6CmSIbBD5j0jY0qxpoXuLLvSeWbs5_uTcCCUmGYEL_N3P3S73KATNi34V86Jsn3Qj-INo7n_gUgz_0BkjGknHdcdpaenmz5A0zfyLaMTpOn70J9-uozYX4z5Qji8mIsCFhs_eEjIv20jDO2pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عهد و پیمان اهالی عراق با آقای شهید
@Farsna</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/farsna/447946" target="_blank">📅 18:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447945">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxInX5H4YsqSRd1Kt1FCz2tRgYXq1eoX_IyjPzmlPbHDup-c6HjCD5d0sPkuOIWXhaoUXC0onfZ5OwkI79DL6fEUmtSVRYkmaymBbzG8Nsw9oYw4Bz6boLWU-ck8jZ0vIHqIVByGj01xKXrMdO90TtkqBDablH31vKgVSIiXtx9KQTRVzJDnoCcpjDJviuwYSLou23lzIXmLOMgwCpDxDPIeSXNwBtQ0ofsKOPSTwqizh71SvwuCAX4bWcI65jO547kBVeDn6FeHHY3bjZeXJxuKEO5Iam-vHJZ3BMoRPZcsWrX6PlCD6IcdxsUqpb4x7qbCj65u50p5w8WUHPC2aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت دفاع: ایران در برابر هر تجاوزی پاسخ قاطع و متناسب خواهد داد
🔹
سردار طلایی‌نیک: دشمن تصور می‌کرد با ترور رهبر انقلاب، فرماندهان نظامی، دانشمندان و حمله به مراکز مسکونی، می‌تواند نظام جمهوری اسلامی را دچار فروپاشی کند، اما نتیجه کاملاً برعکس شد و انسجام ملی، حمایت مردمی و اقتدار نظام بیش از گذشته تقویت شد.
🔹
جمهوری اسلامی ایران مسیر دیپلماسی را با اقتدار دنبال می‌کند، اما در برابر هرگونه تجاوز یا عبور از خطوط قرمز، پاسخ قاطع، مؤثر و متناسب خواهد داد و تجربه‌های گذشته نیز این واقعیت را برای دشمنان اثبات کرده است.
🔹
امروز جمهوری اسلامی ایران با اتکا به مردم، توان داخلی، تجربه‌های ارزشمند دفاعی و هدایت‌های رهبر معظم انقلاب اسلامی، حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای، مسیر تقویت قدرت ملی، توسعه بازدارندگی و حفظ امنیت پایدار را با قدرت ادامه خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/447945" target="_blank">📅 18:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447944">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22dd375f85.mp4?token=CkS_T_0CnYQwOwISVZltpNV_kWRBz3wSTrInOrq7OsVpAmskFTirf-DvEI4Wr4TWhPwYFPq2MHlin_SpHjVweOZmfoMgLM0gs2DIOy--s4GEg4CdI8kc6aBdHcFVThgTCaRyJQ0hOFLsr59ZyW5SI2H-9caTjGmjwgdkYLYwXp3jqhn0wNRfzwwUQ2fs78GY5TAHnDx6kfpKYw1YH89MEGVWLd8toLfa9Ea84CDook_nZPtTGK5oAm8zvQeOR-qP1ZqeDH55jZvOpROjdmVIO-O1L3kaJUlkCSL8ajAKBkMhMZpMcQapZKQwaPk4wvdVSS1twdIL4ny8c35dDJA74g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22dd375f85.mp4?token=CkS_T_0CnYQwOwISVZltpNV_kWRBz3wSTrInOrq7OsVpAmskFTirf-DvEI4Wr4TWhPwYFPq2MHlin_SpHjVweOZmfoMgLM0gs2DIOy--s4GEg4CdI8kc6aBdHcFVThgTCaRyJQ0hOFLsr59ZyW5SI2H-9caTjGmjwgdkYLYwXp3jqhn0wNRfzwwUQ2fs78GY5TAHnDx6kfpKYw1YH89MEGVWLd8toLfa9Ea84CDook_nZPtTGK5oAm8zvQeOR-qP1ZqeDH55jZvOpROjdmVIO-O1L3kaJUlkCSL8ajAKBkMhMZpMcQapZKQwaPk4wvdVSS1twdIL4ny8c35dDJA74g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خودنمایی پرچم ایران و عراق در خیابان‌های عراق در استقبال از تشییع رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/farsna/447944" target="_blank">📅 18:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447943">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f7789ff06.mp4?token=S-0xAAnWaBJ3iFtDeeTob6IrtpI4WJkL5OumqPSiCkn97wNVXrfnUGBUn09NZD78DtTYImNdPxLl3hPsTMMRGqZLOKhp4x23JQlQGipTzdjU4B18Bjg85oKr-RfjZAIYJxZti6MlO_w6bEPzMMLEzYWSZaycRW-3gyt9cxi1yeB8pGoao3rwAXl-RZwWFov_hGdUjYkLNmyYuLtDhiW4Ti00Ozu5WSSVRzFDyhnQanqgZJKVgzMrIC5NWU5t08zD5lDBFygf0jLscHE4RzuRhTJi9a54JQf8lu8s04RxrA5HIZa1h8fM2v2WdtNJtXWs7LjLyRrKy6erVlzJ87rROA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f7789ff06.mp4?token=S-0xAAnWaBJ3iFtDeeTob6IrtpI4WJkL5OumqPSiCkn97wNVXrfnUGBUn09NZD78DtTYImNdPxLl3hPsTMMRGqZLOKhp4x23JQlQGipTzdjU4B18Bjg85oKr-RfjZAIYJxZti6MlO_w6bEPzMMLEzYWSZaycRW-3gyt9cxi1yeB8pGoao3rwAXl-RZwWFov_hGdUjYkLNmyYuLtDhiW4Ti00Ozu5WSSVRzFDyhnQanqgZJKVgzMrIC5NWU5t08zD5lDBFygf0jLscHE4RzuRhTJi9a54JQf8lu8s04RxrA5HIZa1h8fM2v2WdtNJtXWs7LjLyRrKy6erVlzJ87rROA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرزندی که مهمان‌ خانهٔ پدر شد
🔸
روایتی از پیوند عاطفی عمیق مردم عراق با قائد شهید امت
@Farsna</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farsna/447943" target="_blank">📅 18:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447942">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/476d11a9c0.mp4?token=fJjUKuthmEVQSknqJXEE1-D2MzLqtgIaj_derbHbnk_HhcbDk9JGl_9UxENM0FLlKAEXVHFmaHkNpWYj2l_TN6kUcwyRaDokF1DPp-nHTFqRaTSFtTh_IJ1usGiatEPUa2dF8k9Y7afKLUiQUWk_K9rKZoNr2WMTOp3zOZDXwN5DKPYxrxfsjL65FGtaxLxzHbg2fubqtjaFDh_S2imw0k_xBvT_LcOWy7wDiC-O-P76BJK4Te4SuzX5ECnT5OZtIpuD0uQrGNntm9Pg4Ghs-wd4c0pLnpF48W5l8G8Ys7fXbqV17knOS0geNdv_ckpmwC9YRdDEkipPopJtYX_66Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/476d11a9c0.mp4?token=fJjUKuthmEVQSknqJXEE1-D2MzLqtgIaj_derbHbnk_HhcbDk9JGl_9UxENM0FLlKAEXVHFmaHkNpWYj2l_TN6kUcwyRaDokF1DPp-nHTFqRaTSFtTh_IJ1usGiatEPUa2dF8k9Y7afKLUiQUWk_K9rKZoNr2WMTOp3zOZDXwN5DKPYxrxfsjL65FGtaxLxzHbg2fubqtjaFDh_S2imw0k_xBvT_LcOWy7wDiC-O-P76BJK4Te4SuzX5ECnT5OZtIpuD0uQrGNntm9Pg4Ghs-wd4c0pLnpF48W5l8G8Ys7fXbqV17knOS0geNdv_ckpmwC9YRdDEkipPopJtYX_66Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
نشست رسانه‌ای مهمانان خارجی تشییع رهبر شهید  عکس: زینب حمزه‌لویی @Farsna</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/farsna/447942" target="_blank">📅 18:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447941">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305328c444.mp4?token=CmiRN1_BoUmi-JoNvzMMfHK9eZqYgelqdMkMay00wRvDfxk3qtnkboRgpUW_M_kAHHKqDcj05eY0ZIPzF5H5nceevZVWP2XPB5uBoU8bHx0TQ6r2Coko_nznTKbo7QtPNHyKDmUKCJad_DbsU4PYNQDxsZkQbKcxCRQkusHk41vYx9IGZ7m9dtal01fs2wlJHLgEi4Ba2Ad6IlZjCFY9juyi--3UEKJIv886eRQxfVArrg_8j1oLzCapBvunjBTr8LdSkVGnIPuVBej1maeF0w1Rkos05ivZPcqgSqEzJMs8hUT9RjqDcHTQ6IqYT60cWP5K9S_HqE_qSQOwPiwnzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305328c444.mp4?token=CmiRN1_BoUmi-JoNvzMMfHK9eZqYgelqdMkMay00wRvDfxk3qtnkboRgpUW_M_kAHHKqDcj05eY0ZIPzF5H5nceevZVWP2XPB5uBoU8bHx0TQ6r2Coko_nznTKbo7QtPNHyKDmUKCJad_DbsU4PYNQDxsZkQbKcxCRQkusHk41vYx9IGZ7m9dtal01fs2wlJHLgEi4Ba2Ad6IlZjCFY9juyi--3UEKJIv886eRQxfVArrg_8j1oLzCapBvunjBTr8LdSkVGnIPuVBej1maeF0w1Rkos05ivZPcqgSqEzJMs8hUT9RjqDcHTQ6IqYT60cWP5K9S_HqE_qSQOwPiwnzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصویری دیده‌نشده از رهبر شهید؛ آخرین هدیهٔ مردم تهران، به آقای شهید…
🔸
در آستانهٔ تشییع رهبر شهید، مردم آخرین هدیه‌شان را با دست‌های خود ساختند. هر کس بومی را رنگ کرد و از پیوند آن‌ها روی دیوار شهر، تصویری خاص و دیده‌نشده از رهبر شهید خلق شد؛ یادگاریِ ماندگاری که تار و پودش از عشق و مشارکت مردم بود.
@Farsna</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/farsna/447941" target="_blank">📅 18:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447940">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f49b6b30c1.mp4?token=OvaRxV6lCVyCDgnZMa4ZZq0HYoMT9StaNt1OQ6FXGgOR-dIjvFffpJgloFb7lk5AdMAYt1_ppBGBvsrIFU8cNxeRK72QhCs5U2gouF1bWUz3Px3FVzS86d8pNVHGhrjLlpBlDyXGuGHRoKihWah3pLbQrXwykqTvLvrnRUigNnWJ1PHlnOMtM1D9nsibW-LVgMfX9PL685iPnmqpZFNaSSd2u21VGmdFyUFfkMz462P88794UVLBmc1KFlwaEnU_KQnw-rwYTVc6-6LT6ue9nDO4-atU-stHE5rg9y00ymj8jPUz5i4dxbB5GPiyRZ6fFSLX4q_top5bo1FsIfMoug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f49b6b30c1.mp4?token=OvaRxV6lCVyCDgnZMa4ZZq0HYoMT9StaNt1OQ6FXGgOR-dIjvFffpJgloFb7lk5AdMAYt1_ppBGBvsrIFU8cNxeRK72QhCs5U2gouF1bWUz3Px3FVzS86d8pNVHGhrjLlpBlDyXGuGHRoKihWah3pLbQrXwykqTvLvrnRUigNnWJ1PHlnOMtM1D9nsibW-LVgMfX9PL685iPnmqpZFNaSSd2u21VGmdFyUFfkMz462P88794UVLBmc1KFlwaEnU_KQnw-rwYTVc6-6LT6ue9nDO4-atU-stHE5rg9y00ymj8jPUz5i4dxbB5GPiyRZ6fFSLX4q_top5bo1FsIfMoug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: من از ناتو خیلی ناامید شده‌ام، ناتو [در رابطه با ایران] با ما رفتار خوبی نداشت
🔹
اگر نشست ناتو در ترکیه برگزار نمی‌شد احتمال داشت که اصلاً در آن شرکت نکنم.
🔹
قبل از اینکه اصلاً از ناتو درخواستی کنم، آن‌ها گفتند که برای مقابله با ایران پشت ما نخواهند…</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/447940" target="_blank">📅 18:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447939">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abc858c595.mp4?token=PcfEtSOTYNHuArRae_7eOfn65hvcIMr-8BczCUf20q1H3wP47xir0p5lSheZChbKEs_RLdmQ1BB_9JOSdECK0VUkBsLB7B4tyGjcZpbm2o_9jf5E211I7_hPXTwSNhcVXngYlDIC0u-hUSYt7GT5oMJajZbSZ3O7bWdTsbBpOLA4RPHkNpxO02eSxVhE0xrGm7l8Yih0baxwOZEXl4x9bi_7CPcMUmJC2WyPm7AmJVM0kMfHzlgQ6w-56wqVGTyNcaXb21n2Cw7qYpnTygy4NGu9hb3b7h1syEATGd-VAxyuz41eom4vYxgSMhA0HzquL0jdLlHjuC0taNn3UzVJMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abc858c595.mp4?token=PcfEtSOTYNHuArRae_7eOfn65hvcIMr-8BczCUf20q1H3wP47xir0p5lSheZChbKEs_RLdmQ1BB_9JOSdECK0VUkBsLB7B4tyGjcZpbm2o_9jf5E211I7_hPXTwSNhcVXngYlDIC0u-hUSYt7GT5oMJajZbSZ3O7bWdTsbBpOLA4RPHkNpxO02eSxVhE0xrGm7l8Yih0baxwOZEXl4x9bi_7CPcMUmJC2WyPm7AmJVM0kMfHzlgQ6w-56wqVGTyNcaXb21n2Cw7qYpnTygy4NGu9hb3b7h1syEATGd-VAxyuz41eom4vYxgSMhA0HzquL0jdLlHjuC0taNn3UzVJMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چشم عراق روشن؛ گفت‌وگوی بی‌پرده با مردم عراق که چشم‌انتظار بزرگ‌ترین رویداد تاریخ عراق هستند
🔸
به زودی مراسم تشییع پیکر رهبر شهید انقلاب در عراق برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/farsna/447939" target="_blank">📅 18:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447938">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/667eab7dcb.mp4?token=DBv4TDjYNRIHJB0Uvw08AukFjB73zo9k0AwPn0F2RfyBAfN54pEhoqTSoT67CF-c3-gYnAy4HBEVuakVqP4EFZwiWNU9whNVDx0RBHwp0wCl-4ftjWu84VCQ14nOGtFR2GZ8I7bsEedpUNMaTfLMsYxO6NPFy-dFGoLsC9ok_5Kv44zs6hJ3tt1AP1zlcSAMDF5yhgULq_lgjozUcC1VTSDJ0vpp1jGQV2cBwPWotP83tuyDrDUmcR5NK26LMz2ZbGJSBmjDOYhbtDg9w4Gs5igejCEEu215tldRfoF3IwAE9yu42pGHv5J4BTqvVwYhAjBfMiat8d08JHvByQHaiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/667eab7dcb.mp4?token=DBv4TDjYNRIHJB0Uvw08AukFjB73zo9k0AwPn0F2RfyBAfN54pEhoqTSoT67CF-c3-gYnAy4HBEVuakVqP4EFZwiWNU9whNVDx0RBHwp0wCl-4ftjWu84VCQ14nOGtFR2GZ8I7bsEedpUNMaTfLMsYxO6NPFy-dFGoLsC9ok_5Kv44zs6hJ3tt1AP1zlcSAMDF5yhgULq_lgjozUcC1VTSDJ0vpp1jGQV2cBwPWotP83tuyDrDUmcR5NK26LMz2ZbGJSBmjDOYhbtDg9w4Gs5igejCEEu215tldRfoF3IwAE9yu42pGHv5J4BTqvVwYhAjBfMiat8d08JHvByQHaiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لقب حضرت آقا تا همیشه همین می‌ماند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/farsna/447938" target="_blank">📅 18:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447937">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCndxyiB_J3PeioNON0w5oTOOBy6Gda7G9PjqgJf3acDci1xfl5DGbTjVyHKVq6qGFpXf8DL2QHO5t04bpIztBqXztfsf1dCFmGoFHasGpuIWmdeLV_MXja1TyezvFoz19lIrcE20UeOzK_q7Cg8b8ntZDQIfKDT7ZXrreFxULc15ZfINIg8cucgvTIpMdpwgjjt6N10FK-anMI6IOGd9Owjb9mnVf1JTslUXv3NxxUg_IGwDGH1ma9T8Y-V2JF8TP8VAQ1UGfyKLS_pJ3SrLuiSJl35cGnMlhwgzoZXliP9SUSoFuZEaPhDs4alFd4J2cOemVUVaomaFYgrkoR5Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کسی گفته حساب بازاری‌ها از رهبر و انقلاب جداست؟
🔹
کرکره آن‌قدر بالا نیست که بشود راحت چشم انداخت و داخل مغازه را دید، اما در میانهٔ در و کمی پایین‌تر از انتهای کرکره، دو چشم تیله‌ای زل‌زده به آدم‌های بیرون؛ لباس سیاه تن کرده و در دستش پرچمی دارد دوبرابر قد خودش.
🔹
دنبال پدر از این‌ور به آن‌ور می‌رود. پدری که عحیب متعهد  است. «حتی در روزهای جنگ که همه بستند و رفتند؛ ما در قلب شهر ماندیم و هیچ‌وقت خیابان را خالی نکردیم. اصلاً چه کسی گفته...»
🔗
دو کلام حرف‌ حساب کاسبی از کاسب‌های شهر را
اینجا
را بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/447937" target="_blank">📅 17:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447936">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4413e158b8.mp4?token=nh2ANI9AvFQojGUO7QwRbee9ttBmfEjTMgtTVUUbCzMt4CaRu9YCuCJe9ys-GWwjEUExBJ0LqT1DI8PZriQB5iCoal4YAPNdiZh60daGCi7nBQctx2iTtWXdBiND8WKnhmsW6ZgA1dvpKW7smiPlYHpqS7VIt0HqTwduLHdVR9Qt3YJ3ELK7kaJE5pm5XjA2vZxVwsCxBk1RDLUyjWoWIIBKuigEzh08I2SJd7N0GN-ORyFIcdp-JIM8jhtmfDePZ-0Bg6UA7y1AJcYAZo8UmMsHVuGHxQhg738j6_J4rwCfqTvsVshaoX-1ogyXdBW9J3UDDpsCOV9aFAEN3pmoYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4413e158b8.mp4?token=nh2ANI9AvFQojGUO7QwRbee9ttBmfEjTMgtTVUUbCzMt4CaRu9YCuCJe9ys-GWwjEUExBJ0LqT1DI8PZriQB5iCoal4YAPNdiZh60daGCi7nBQctx2iTtWXdBiND8WKnhmsW6ZgA1dvpKW7smiPlYHpqS7VIt0HqTwduLHdVR9Qt3YJ3ELK7kaJE5pm5XjA2vZxVwsCxBk1RDLUyjWoWIIBKuigEzh08I2SJd7N0GN-ORyFIcdp-JIM8jhtmfDePZ-0Bg6UA7y1AJcYAZo8UmMsHVuGHxQhg738j6_J4rwCfqTvsVshaoX-1ogyXdBW9J3UDDpsCOV9aFAEN3pmoYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از دلتنگی ایرانیان ساکن عراق برای آقای شهید ایران
🔸
آن‌ها در انتظار تشییع پیکر رهبر شهید در عراق هستند
@Farsna</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/farsna/447936" target="_blank">📅 17:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447935">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ایلام چهارشنبه تعطیل شد
🔹
استانداری ایلام: تمام دستگاه‌های اجرایی، بانک‌ها، دانشگاه‌ها، مراکز آموزشی و سایر ادارات دولتی استان روز چهارشنبه ۱۷ تیرماه تعطیل است.
🔹
این تصمیم با هدف تسهیل حضور مردم در آیین وداع با پیکر مطهر رهبر شهید انقلاب در کربلا و با توجه به افزایش تردد در جاده‌های ایلام گرفته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/farsna/447935" target="_blank">📅 17:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447934">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b353fba9ba.mp4?token=pKImUad7etThdhRylVeVzrT7kUrr9pBDd9pHqkTXMCZ_eGzfvuQIiqPbOmuJBwI1VEmD5rjmlKvesbfIM9sbacgYE2OLA0hRoW45J-nhF3qFaf0k6G42SmjrTODH5CQO7RFhN7conYYEqdE8Cx6cYZxbPQFTcRqgKGo5WMceH8kfHjJeJ_-bnYluRmeK29SETxdwvmDXBi5EC7lmKrV-o9oGbeZhr-c6a1aKfzpiNCBcIzU493W6gvtEJmzRzBAaP0-LbGieMPyBFWv5DIFQ2GOfy1ReW_QK-PU0T8Ce5SkkB7gYdkWhy9NF3LDQjLU7ymRCjbKemEVDd3ApMRldfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b353fba9ba.mp4?token=pKImUad7etThdhRylVeVzrT7kUrr9pBDd9pHqkTXMCZ_eGzfvuQIiqPbOmuJBwI1VEmD5rjmlKvesbfIM9sbacgYE2OLA0hRoW45J-nhF3qFaf0k6G42SmjrTODH5CQO7RFhN7conYYEqdE8Cx6cYZxbPQFTcRqgKGo5WMceH8kfHjJeJ_-bnYluRmeK29SETxdwvmDXBi5EC7lmKrV-o9oGbeZhr-c6a1aKfzpiNCBcIzU493W6gvtEJmzRzBAaP0-LbGieMPyBFWv5DIFQ2GOfy1ReW_QK-PU0T8Ce5SkkB7gYdkWhy9NF3LDQjLU7ymRCjbKemEVDd3ApMRldfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تنبیه متقلب‌ها در مستطیل سبز!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/447934" target="_blank">📅 17:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447933">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WO7llEq4hjx4Ma2JhUps6GXPTF40CcpCjs6daxu8fhnxgy-UpCfRxkXaj7rahoFZdTC1dw8edDOOcLrXF6fU-wxxl5H8X0scX6fXptF-v-06TjxG2TrwqihMxFknD_LvtEoqa-PJU34Klmd5m0VsyQIsO2do3yPc1vD4ugLmfayaR6U-8TvEc5578zhEnTTfbhLFdFO63SyXUc-WvE8OgJs6ql_qVBDTVfVoJmJzwqTkoFke6OFb2xgkYmuW2JHqDEuh2IaRoRZ0NM78SFC9ZLZnbUp4we3hhGLrOqNxTTlZdVBTeOJiJEnWiYg-C74JSRzRTkCbfTrA0RuS_M7Rhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرزویی که دختر عکاس را از بندرعباس به قم کشاند
🔹
در میان همهمهٔ خانهٔ میزبان، گوشه‌ای نشسته و دوربینش را محکم در آغوش گرفته؛ هنوز سؤال اول را نپرسیده‌، اشک روی گونه‌هایش سرازیر می‌شود.
🔹
آرزویی دارد که به‌خاطر آن دست خانواده‌اش را گرفته و از بندرعباس راهی قم شده؛ سفری طولانی فقط برای اینکه شاید بتواند.‌‌..
🔗
ماجرای سفر این دختر عکاس برای برآورده‌شدن آرزویش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/farsna/447933" target="_blank">📅 17:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447932">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df726c7c93.mp4?token=U29vokrpj80h_JB8v05hDNzdCltyGXQLtHOb174MdaOEskmcHx0qh50ZJkwkXXeYBHCYOxBUoJy6Wr8x1aTv2-U__v1yub7ynJfYDzUAFyUXf9xlt3JfaeZNgnBh1HE0_gKERPBCT1bM7kXiJkHIthITQJTYfUSTmU2j5B5qAhtTl2Ms6wYbo-Q1_W2zldhoBXwQXkwTbzXFnvRu2-6V2ed-4yfGbrjptQbnFP0-Z0TPkJxGREvIZv7n9p_J9C3shbuUSv68mzYaudDYvTNZcGrry1C9ef3JH_3NZvV6NO8wSIbl4jARsC4_vJQ4w2bqUE7f2ZX1vd8hYqJQ4WVOgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df726c7c93.mp4?token=U29vokrpj80h_JB8v05hDNzdCltyGXQLtHOb174MdaOEskmcHx0qh50ZJkwkXXeYBHCYOxBUoJy6Wr8x1aTv2-U__v1yub7ynJfYDzUAFyUXf9xlt3JfaeZNgnBh1HE0_gKERPBCT1bM7kXiJkHIthITQJTYfUSTmU2j5B5qAhtTl2Ms6wYbo-Q1_W2zldhoBXwQXkwTbzXFnvRu2-6V2ed-4yfGbrjptQbnFP0-Z0TPkJxGREvIZv7n9p_J9C3shbuUSv68mzYaudDYvTNZcGrry1C9ef3JH_3NZvV6NO8wSIbl4jARsC4_vJQ4w2bqUE7f2ZX1vd8hYqJQ4WVOgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلاش بی‌وقفهٔ جوانان عشایر عراقی در دل شب برای استقبال هرچه باشکوه‌تر از رهبر شهید امت
@Farsna</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/447932" target="_blank">📅 17:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447931">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba9e6e1784.mp4?token=KQvd5S-ap9xlLeLKQcSzLTcrgMqdHDvruPQ68A78L-8KxcmH1kzqR2YZKEuLxhELoAvjn3LqbnCtaXVjtMOrzSLqFSLDrJp4o7060FBtn-MR5aV4aI7fBc5DMA-pyQWcEBwphpvXwLpEtLRJb8kgO-3oEhFZ_ZAri5Wh6hANhTBgrlbzQ8DMFuYF1orL3kRppqded-0oW_wYeyjOJeULGyKdS6Hf1wUmYbG-W-uQSSAVULRD3dItrofkgq7UrKXNjcdNi07rbMFsIOnCQtyC4464iZPllFfuNst4jydpIzgRM4aQYzd9H11TjiSEB62CTR_RYlHxwJLFE4QcRN-bKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba9e6e1784.mp4?token=KQvd5S-ap9xlLeLKQcSzLTcrgMqdHDvruPQ68A78L-8KxcmH1kzqR2YZKEuLxhELoAvjn3LqbnCtaXVjtMOrzSLqFSLDrJp4o7060FBtn-MR5aV4aI7fBc5DMA-pyQWcEBwphpvXwLpEtLRJb8kgO-3oEhFZ_ZAri5Wh6hANhTBgrlbzQ8DMFuYF1orL3kRppqded-0oW_wYeyjOJeULGyKdS6Hf1wUmYbG-W-uQSSAVULRD3dItrofkgq7UrKXNjcdNi07rbMFsIOnCQtyC4464iZPllFfuNst4jydpIzgRM4aQYzd9H11TjiSEB62CTR_RYlHxwJLFE4QcRN-bKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آماده‌سازی ورودی حرم امام حسین(ع) برای تشییع پیکر رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/447931" target="_blank">📅 17:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447930">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8c696d52.mp4?token=PG3mfnXUzpusrE4cg3PayepEqtIhLTMIoOTQ5xTrv_8mObOVZtgcKeDTUwZozaDEdXJT9BkaqapAoXGzVo50Bch2WuJs-o03h1lnik-TcLv4s57JopHtQ8QtTT8RPDNAdQ4sx5K790E9n_ql0xs9kiqKdYepasg98ffxVWkc5V-Rra7UgO-Y756xdcc58OGywXpVEjMGWFUVRZiNThT_2DsdOl84_l3S15wVQFPPSF5v9ZJWtECRUHgWj2k5I9U8rDHuvzSit6SVFtUjBlqS1DXm1_Mr3uZEisfyohDcbrbQzL4c_0Rj4lQ91DLV0kpUfWE6uClMIlhkCGpOlU-Z2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8c696d52.mp4?token=PG3mfnXUzpusrE4cg3PayepEqtIhLTMIoOTQ5xTrv_8mObOVZtgcKeDTUwZozaDEdXJT9BkaqapAoXGzVo50Bch2WuJs-o03h1lnik-TcLv4s57JopHtQ8QtTT8RPDNAdQ4sx5K790E9n_ql0xs9kiqKdYepasg98ffxVWkc5V-Rra7UgO-Y756xdcc58OGywXpVEjMGWFUVRZiNThT_2DsdOl84_l3S15wVQFPPSF5v9ZJWtECRUHgWj2k5I9U8rDHuvzSit6SVFtUjBlqS1DXm1_Mr3uZEisfyohDcbrbQzL4c_0Rj4lQ91DLV0kpUfWE6uClMIlhkCGpOlU-Z2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
به عراق خوش آمدید آقای شهید...
🔸
چند قاب از اشتیاق مردم عراق برای ملاقات با قائد شهید امت
@Farsna</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/447930" target="_blank">📅 17:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447924">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YSbHnEqNCeJfnmyXrYmckdjyLG4_dkfgN1S0nlua1iQaXk60C1GoFUm5HM-SqMuJbx3SeGQf9jEWzWBpOtbkW2f3_lFFdtWEjTiNNia8-yl0f6vPFGV6dsxHwpdDlWA4ybXciZ18wWnYOIdHvD4CW_XKO2j1qz0WpgpgNNv1GgQc30Pz4NRKVVXLPhWwr6jnOr2kIelQDAisXOn8TOADNl7jtbPRA4k_wVgEJU6_srY2_2lRrgQmnZYzncnpRgC1GbRjXl7RJwkikFm7H7Nyu9x0eVFg3qWZ4t1U9NXQ9rRdPlP0yy4nNAvCjGChA2EXhpsTuUTn1lKinAz7BI4pfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MwbkgxwQ_uOnfxdmtLSJLcMPSJ45Qukd40QvKTz2p-su-a5eI7vKVN-e5V-XoqQSI5NO2Q1jA6snttrt5-dVDcnJBShKkRNPU73C-CdIl7yGhCCgeo2KVmyusTMZW25f5e0ms3ZNiIFCegyaP3mK18qNk4-F49mFYOtZY5CM3e15387bBnrLqAFwSGDEjsSHViyva2we1NX8T0remFinVwE1CrhbMbO5uHV-CgdXczDohB53GrkYPx7PnBAlJE-VdWUSOOaxlnohhqL2NeuB27cSpx2MwxK8AwBvE-xKF-K10rjFERgVWhBAgIb91PO2ZL4lJv0Oy6aySB5RLmKt2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y7hXRNyHIBvGzKIpG7t80Y4Te6L8UTIoClRaHZ4-ItOvoPLgCxmgpJ5Lrh-nUw5ZaM2l67wfdDaBrgq_I6bt3czIgXw3irpm-hssxORFKFWsp2ybagWlXdcpcASOGOrCIuakr1n8iVPRU9BdGvJNCvWgyDeHqntHN94qIXQtYGkC-VYnCjeP6tm0YXOZiMDUf702KAMvd9Yi8EkuNj1zITeY5LWenqJOCHPJhN3qD60glvXYdY-94MRtF84Y-37EMtVkJTUUMoidjpS3IB8Z4h9fcjd0B7P5h8Dd7d6mRVSHH3P1LhH0TvQgeRwQtKIhpM7iqcuE5GN66HzaWE7BFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nQWf41h_5Cf9c2eRmvzht5WIRxOi_2i9bI88QxMOiHar2_pdh2JfjJR9tg5AOI5GXifqlzi9CkZoKbZTHfViq2JXZByHlGgFp7VbecOZXb2oa8S0vo9oKJcO6NMssZYt2DhPAGh1zeaTmGMBbwzJWmPPjDspPcRMTm-WvEmr5Xi4jYXUOqnZ5L_mCDLgHzC2kZDu_1Z-E-UzbXQZkie_dUL7phSimSDlSwSheh4gAcNJzmlQMlE4GeOjTC5mbQoguyfRR6i_T5l362VjplKrdZIsL-sEl5bzgnHi_rbo2c0kfnl9FjNxihz0RpD3qCa4yYz-U_uercOTcz0j4HceaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u-L8Ks9RSnUuSI1lxNyYNPjjv1VzU4U2fHFODDLa5f9ti5lJs6XpOyslCkDvy4SowbCqn7ZsHThK4h9V4C6GpU4Oz0rfS-8f72u6qOmeSC-5kEDeHBf7HoJihfvqkwjmAA0LQuQ-08WUiICBzpkYqG65tHf8O8R43EIf5ybVCO7CpQTVvNG1QAI3Im5mhjsEk_Er2OWsVX7KeCqrCODnDVxjZEgSZmn1LHMO2nyqZ1-o1JziuZRKbWXkpXMCJin38CHEHOuclKJrEf7hMF9GyrE1Z72EB3ecCFruyDqjbTzXmlELYI14y6h7D8OUsGrppZW8gxwVCMWI4UKKWbekew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
⚽️
آدیداس از توپ مراحل نیمه‌نهایی و فینال جام‌جهانی ۲۰۲۶ رونمایی کرد
@Sportfars</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/447924" target="_blank">📅 17:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447923">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">حادثه برای یک نفتکش در سواحل عمان
🔹
سازمان تجارت دریایی انگلیس اعلام کرد یک نفتکش هنگام عبور از تنگۀ هرمز، در سواحل عمان، هدف پرتابه‌های ناشناس قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/447923" target="_blank">📅 17:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447922">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vp4g5zaLLFmA6Zs5nJ1b2vCpIhAMoLLrATUhCRQd0YvvZMf0Q04h8wk2iRGuzuTVbuwjGiRNBldr9Pr8Pu_9uCp8lOpFR9J1IlJp8cqKYuMKTwK5rQ2LNYar9vkoNXfUbm45a8ABDRDzErCQ2NgFRWiuwA3r7iI7XbwJbJovJ1Cs7KMQ7JXCbFL75O6W7YXhRFO_9NojErP8XSdb8Ut2YyXbf8SZy7ci3yXyM1qrH6e8W4ti0aN1wXfgS61wjlxNDP4xoxyxrMCw6mD_S96iG4TKILXvDqcdRXBCua8BSNMrOw4uE5VyhtCQIo1Gp-bsfMnT4MmgS1QM90xKEbSyug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
آسمان قم میزبان طواف پیکر پاک رهبر شهید انقلاب، بر گرد مضجع شریف حضرت معصومه(س)
@Farsna</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/447922" target="_blank">📅 16:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447921">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4c8b46e0f.mp4?token=CdQZYBgAmbzRpb_RORHP26w5ZGhiJZ09akliPkfc2po6K21SNM6Q7s20P0C8DO5QasU6Y0A_gavcvusT7iKCnErJsuFnLOC14fgIJDNkUhPEfU76Bds5KIDatNLEZZRLHL7_OY5LDRB_vOCDS5OMG1q66jgOQuM2FutNBIv116W0SYur-8HfnmYlh1hmRsUG8RG8u7FJydepVf4kKkyOmNWMqO3gu2tWMthTblPqCVB3uQlGkwtQiqi9caCLfzjdrBKgDR38IiQ6Pt-ZCjWJwx-UDXubw3XfxJGfz9vINem1Pp4zl8AVYDxx1KM3MUlZMfPqhBQF6X2LX_VGtkgrHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4c8b46e0f.mp4?token=CdQZYBgAmbzRpb_RORHP26w5ZGhiJZ09akliPkfc2po6K21SNM6Q7s20P0C8DO5QasU6Y0A_gavcvusT7iKCnErJsuFnLOC14fgIJDNkUhPEfU76Bds5KIDatNLEZZRLHL7_OY5LDRB_vOCDS5OMG1q66jgOQuM2FutNBIv116W0SYur-8HfnmYlh1hmRsUG8RG8u7FJydepVf4kKkyOmNWMqO3gu2tWMthTblPqCVB3uQlGkwtQiqi9caCLfzjdrBKgDR38IiQ6Pt-ZCjWJwx-UDXubw3XfxJGfz9vINem1Pp4zl8AVYDxx1KM3MUlZMfPqhBQF6X2LX_VGtkgrHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: به فروش اف-۳۵ به ترکیه فکر می‌کنیم
🔹
رابطهٔ ما با ترکیه بهتر شده و ترکیه از خیلی جهات، بسیار وفادارتر از کشورهای دیگری بوده که فکر می‌کردیم به ما وفادار بمانند. @Farsna</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/447921" target="_blank">📅 16:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447920">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3b8ae83e9.mp4?token=cR1LYyNflSRBdon7aKhBDmu4EGGwlhpr7LGSz36_mUYiVvlu6VddN0pK0ow8DPtSSgPJ-LFG7_MLZgYsUNQ8SmnUdOK7S65z99pMjaFWNHg-PyR9_LIFKn7ykq5WBK3jZ7oS0RSHWA00tj20AaWwvZzmcikrJ6SbcyPkyl182kgj9_Du-iYEt5J423Uy-7eaLhjhYBZiExDu0oMr-bt-gxxDprrfUWmWmOQkumMdA61g_E03fGioEsYqkn7s5sZ8Mvwa6iVoJh4pSzHO5WRVwTyu9XChPntgJmA1ce7vYhk4f2XIEjN7mguKe3BCsB0jan0Fzu4MgHCYrXtTvfA9cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3b8ae83e9.mp4?token=cR1LYyNflSRBdon7aKhBDmu4EGGwlhpr7LGSz36_mUYiVvlu6VddN0pK0ow8DPtSSgPJ-LFG7_MLZgYsUNQ8SmnUdOK7S65z99pMjaFWNHg-PyR9_LIFKn7ykq5WBK3jZ7oS0RSHWA00tj20AaWwvZzmcikrJ6SbcyPkyl182kgj9_Du-iYEt5J423Uy-7eaLhjhYBZiExDu0oMr-bt-gxxDprrfUWmWmOQkumMdA61g_E03fGioEsYqkn7s5sZ8Mvwa6iVoJh4pSzHO5WRVwTyu9XChPntgJmA1ce7vYhk4f2XIEjN7mguKe3BCsB0jan0Fzu4MgHCYrXtTvfA9cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درخواست نتانیاهو از ترامپ: ترکیه نباید به اف-۳۵ دست پیدا کند
🔹
نتانیاهو در گفت‌وگو با شبکهٔ فاکس نیوز، ترکیه را «رژیمی آلوده به اخوان‌المسلمین» خواند و گفت به‌نظر من نباید اف‑۳۵ یا موتور برای جنگنده‌هایشان در اختیار آن‌ها گذاشت.
🔹
ترامپ ماه پیش تلویحا موافقت…</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/447920" target="_blank">📅 16:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447914">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jDCmyxAW34lwEqVWuD4jJ4Aix3TcETbDh35hqTjh8gTWtOESkws6lLLtGz6Fi28lpbrRRY3YhPAzpoOwPYMLxcwZXtLjZ5Jjd4fNREG3oW2d-oObxzzYOs_UOPJl9qT1IlGM3fsGbSEHUs1Npsn8K9s3Kdru_R37135CS2BitZXlogKPeyIVj7eFHmSOFOkmGCR6fCS3J69SdOLWipj-hyOJZws-sDxTZ9rGzdFupBuZRo-4iEBhfB8jFYM-9h4XLrRW9kGbVgqTPVEjw3N-h7vDd3m3dBd2Wq0K3hKYxWljHgKw0rSlzuYgf-R2YCco_6_GfXhXnWk5AHNFX5847g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ax9iXKOJVkDOZ0nkGhIvi7X2iSb7QB0P4vfkHc4fHc74MOalXCyooGW0DSP0HOYVKL4rOPcU1-S0ktE15Gog-hKJZ5bVqG4_K22jTfxrqlE-bjn4v9sTr1xLxDZk3FGPfUHwShlckUYqCxkn-fGhjqWf37c1vRqid-VwAeuI38VYpL70HiLxzbewMjkKxspcO025TlC7hJ6TfwJQbEGWLEWSloQz2AQlYTIarxGoFuV5lkvxDtWtaS-oUiw0-4ajLE7xbhkNDop0piwvXkua9aHFkqNeniX47SIqpyYvTPBEZ4_Gpr1XmuGtqo3jeRMfihMDPKWzIgwjgNy994-a1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cTo0uh6XeaQwSFQvse2Xz85g_wvxO02E1O1g84kLOtBBiJvKXyoQMuwRWhnydkXqLdq418kLhzcuEpoxesy_jwGxxnYrhUEhXDv0xj5tyhzMfxIYyvMKlxyXX_nYkXYsTjB6JGNeIj3gZ4kxrvJPL1th5hHjcjMJmOagnf7W6hzwi9PBnVrlDsj2MDNyonj-jcW9ehPDS5OKhAQir65dGMJL-i04wVxiVtvJ5lKjW0JMpwiQUO40tzp44amNMGwjk4ZJupLzTyyz_B0t7_Em0Hv8m-qEP6fVk9P2Zk4uWXDsCWyF7eCQSJylsq52lo6U6dqBslnukTGIIF5wQyXRtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jU8UDqUzSg6_-xXoGo6WJp9LMq3lZSifMdo4zEyPRq6sE5PVablPXYaGbMhWhewwKdPHaIYmRu7e3UlWGW_CywKtteHVKr28UiznAqa9xKJGq3vqTJTIV4ua7DQbs_Q__-l92G95ysp4iLIEKD5soW1gSftsNXrONfN8vium83ohXK6npL0BqRcWe9vVb_1FY3sgnQG_4nT3qwqKiXQAmtFy-fPUwqkxRqbEme7pks-2le9eoYw_pk5NvZgj2Ld5cTtQTwi1yvMBwgrOx-4R2Ahm9qFZd4WyCpYqkt7GFI9sR8FS6QrWa2qBYaz2oAQ1b9N56FhN1trr1zKrwBG68A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FOTGzsefftBvXn6xZEZvj5yMWypTXsfIq-EFVQRyC26UMKCW_WiYG_wMV-DY1ZPa9Ro-RO-5kVZLtUd_ZxThuDt3f_iK5N1639dhfZxOh0hVhTf5wzeVL_r38SFUfVBm75f9HClP-mjstG86NS-kPMOZl7rGa3rZPCAIS_7moXIWaWWcvk1B45kKLqQm4c3JtjMlM3i-Fh5wdDOWBzkNLRde7izavsYrOfVRaKlT63rMy-jx0OiQ6hAL6RihSMy5z69nnKpNyzsbMVKlRC12mXZxr37MTiSslXo9dPEU2FE2Hg-Jgf4CP5KyZg2zDGx9Wh_9hM5MS01KjLd_OumbPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hQFFKfHk53uOqN1nXZFWb1AoAvYe9KrtGwTSODYZMkK3fsPDkeN3ZeIGNnbL38ohFfc5kpS-j8baYdZPkz3_wdAbCyZ_sp7hcf7ABZW4XelHzh0W2dxgcC4Wf4ik2kwG4sY5w7ffZdNOymr_wVxRuHX4cX6w85OLI9uNdWl6oRCJP4Q_aQj0jdhhEqrRUA8_6AhxGvNwe9YV1zquYVlvxHmQ2mXHn_l6YgJnVqiIbefH9SPFXOjxcVvpoGEaEjiB3gPFEn7Q3UTI-D-lMyHV7t2-0cWOfCZprFFCEpCULzFI7j88LfBb04g0909_mxmHpWH__NAeellqAmZS3adrpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اقامهٔ نماز بر پیکر مطهر رهبر شهید انقلاب اسلامی در جمکران
عکاس:
عادل عزیزی
@Farsna</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/447914" target="_blank">📅 16:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447913">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🔴
چهارشنبه در عراق، تعطیلی رسمی اعلام شد
🔹
علی فالح الزیدی نخست وزیر عراق دستور داد به خاطر برگزاری مراسم تشییع رهبر شهید انقلاب، روز چهارشنبه تعطیلی رسمی اعلام شود.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/447913" target="_blank">📅 16:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447912">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201cd87687.mp4?token=V46rB2oaIZORByP2XmhINaZ2dawLVWk4NxsnNlwYifjDhQfhkw-8150kbmXkXMxmS1LcrcXVKiRcheEBLfP85yEPwBgbOiviU9l_tYwgTq-DZ1N1qczggj4wE30UVaMR4tNaMc7Vr4zYQYpwTGLQMytRvBf7MGGdxtVJe1VOteP2YIXiN4HZ3UEl6VV6OfE5obVNTi0NU8bCAxGFpuW8p1UBxraNjxkhd6Ewf7hCuth4s_cdXHcLYSLNURoNKoG4Qd0f_tVqAwua38uHYF9IoiNKBbGHgqA9v1wvRCi0Sk6--YC6OeWuCRJEge5DOJz5-8g5UYbF557_AsgmrLXSrIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201cd87687.mp4?token=V46rB2oaIZORByP2XmhINaZ2dawLVWk4NxsnNlwYifjDhQfhkw-8150kbmXkXMxmS1LcrcXVKiRcheEBLfP85yEPwBgbOiviU9l_tYwgTq-DZ1N1qczggj4wE30UVaMR4tNaMc7Vr4zYQYpwTGLQMytRvBf7MGGdxtVJe1VOteP2YIXiN4HZ3UEl6VV6OfE5obVNTi0NU8bCAxGFpuW8p1UBxraNjxkhd6Ewf7hCuth4s_cdXHcLYSLNURoNKoG4Qd0f_tVqAwua38uHYF9IoiNKBbGHgqA9v1wvRCi0Sk6--YC6OeWuCRJEge5DOJz5-8g5UYbF557_AsgmrLXSrIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه نفر رو مثل آقای خامنه‌ای پیدا نمی‌کنید...
🎥
یه نفر رو مثل آقای خامنه‌ای پیدا نمی‌کنید...
🎥
امام خمینی(ره) بهمن ۱۳۶۱: اگر گمان بکنید که در تمام دنیا، رئیس جمهورها و سلاطین و امثال اینها، یک نفر را مثل آقای خامنه‌ای پیدا بکنید که متعهد به اسلام باشد و خدمتگزار، و بنای قلبی‌اش بر این باشد که به این ملت خدمت کند، پیدا نمی‌کنید. یک نعمت خدا به ما، این است که داده./کانال سلام آخر
@Farsna</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/447912" target="_blank">📅 16:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447911">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک ملی ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diq5-jv-NGm1xLA6FzHXK7OUeVOSzLPmLHdmytdNf14LouioAWdnnxvYcUI3xiiLgg3jd3F_S7Qb0c3VolIhatDVOvNVHZEfeINBhKoZl2kppLuiF02mcAuy-rozZGfg5EY7iX1_ICh7K8cDmHen_6K-_ZTH9__N78HeXtuMNX-QzM7NpnEHYgunktz_nbmuYq4r5r_pLk3rTd9PLrUbQTMUUcy38x66ahkjfnTHc3NhQUmg4FYsb15hpNZh01Th6vairFOKCxAs4XI4VowutwXTXHvHSbQR5IlE2DqF4nFcNO2g4e6nOQJKrgZJ7LsD3L3OOEu0Hs-EGQ34DOLAww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اینفوگرافیک:
🔝
برای اطلاع از روش‌های فعلی انتقال وجه، این اینفوگرافیک را ببینید.
جزئیات هر خدمت به‌صورت خلاصه در تصویر آمده است.
@bankmelli_ir
| بانک‌ ملی ‌ایران
🌟</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/farsna/447911" target="_blank">📅 16:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447910">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/447910" target="_blank">📅 16:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447909">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f489625ab0.mp4?token=g0EFew3XnYkwcq5TsgcQCBEWcFpgAsl9sDMxC-Sq0gdI4zMkGJ1qUuDDF7u3Jl4jooo0hY0tMs_AKYYhYfc8x5V0oWx_tscKAC43kBYqntsaF_GCG7r956ofyMeslNLF28ekuOTTVhEE0FC2hfA-s1au6vY3fTqJ9B13gYbzggm8suUx3pNX0_AlOJyZJ8tIqCQHpx76_w3CLLB2wANp1Z1K4dQQ41g6QmyGWZ3PvY2klmY0ulcy2lx-fuZLZ386ON41nIOVe4t2hxZRAEO1QUwO9SCGYpswJt6ShUCVtDaW32kz2Zs6JkW8xpSaJaBjT_8lhpE_9KhD6kYAJY0eTgEEYyWBJasyzvzEc5VjOZFgTOcgjU1fBuQ3ZeGsgg0WPkHpW-QT-Rt1RzbSO5CFRr9G8Aix2DQotEpHg0B0zTV51noJSdVdlkTQZLh2xANE4qaqkH-0H9_K8L8OcjFjnB6Q499upLFugHpA1ycrFDAQH21ZU3HTbN7VfXe6G4HMNnTakBXS3Wpmu2d9wQGwdo2quscAkMVRmJeoO5eWgqzfUPVCa6Q30vM--AW7P0Shs0xtoXMSd1qjVom161Dl-gX9NCtJPfkcI4S6CzY7mAqHgJyMSLbNvL_u8B-dDAc3YZTRT25cwFQuUQ6_0KBxiLp9eHCOm2Uka1DRRlMuRsk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f489625ab0.mp4?token=g0EFew3XnYkwcq5TsgcQCBEWcFpgAsl9sDMxC-Sq0gdI4zMkGJ1qUuDDF7u3Jl4jooo0hY0tMs_AKYYhYfc8x5V0oWx_tscKAC43kBYqntsaF_GCG7r956ofyMeslNLF28ekuOTTVhEE0FC2hfA-s1au6vY3fTqJ9B13gYbzggm8suUx3pNX0_AlOJyZJ8tIqCQHpx76_w3CLLB2wANp1Z1K4dQQ41g6QmyGWZ3PvY2klmY0ulcy2lx-fuZLZ386ON41nIOVe4t2hxZRAEO1QUwO9SCGYpswJt6ShUCVtDaW32kz2Zs6JkW8xpSaJaBjT_8lhpE_9KhD6kYAJY0eTgEEYyWBJasyzvzEc5VjOZFgTOcgjU1fBuQ3ZeGsgg0WPkHpW-QT-Rt1RzbSO5CFRr9G8Aix2DQotEpHg0B0zTV51noJSdVdlkTQZLh2xANE4qaqkH-0H9_K8L8OcjFjnB6Q499upLFugHpA1ycrFDAQH21ZU3HTbN7VfXe6G4HMNnTakBXS3Wpmu2d9wQGwdo2quscAkMVRmJeoO5eWgqzfUPVCa6Q30vM--AW7P0Shs0xtoXMSd1qjVom161Dl-gX9NCtJPfkcI4S6CzY7mAqHgJyMSLbNvL_u8B-dDAc3YZTRT25cwFQuUQ6_0KBxiLp9eHCOm2Uka1DRRlMuRsk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار لبیک یاحسین (ع) مردم عزادار قم در کنار خودروی حامل پیکر مطهر رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/447909" target="_blank">📅 16:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447908">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b16b182af5.mp4?token=cD1o3iuhcgWodVHSiI7gqFFzf2Dp0Ou5Y4s7ewLzJJzVfpi_mK2RWShAwWl2cbYVPOq1bcLIURwxGux2ar_TV7TX-TMmdk710V6Z6RUeVDvSYJsnxBuOu8Iw9YumGV6SYSvBBBtk0e71GK89LxJTROw1uXHYL2KZcqaojWRg-eKn8DLbalOBhsHioEJVdoNbx5rp0vMhO32rH53Z3tL40Il4NDCw0nbUG8bxcIPFHd2-CBHch0IhF-dpOtvwYqtpywXRUcVJPE-yayOBNsfcNG4Mx4_pcvaQ4LP9u8hhJMsDG0L32BXxHg12lJ6OISq_5_vjLfglACI4V5U_JSLv7jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b16b182af5.mp4?token=cD1o3iuhcgWodVHSiI7gqFFzf2Dp0Ou5Y4s7ewLzJJzVfpi_mK2RWShAwWl2cbYVPOq1bcLIURwxGux2ar_TV7TX-TMmdk710V6Z6RUeVDvSYJsnxBuOu8Iw9YumGV6SYSvBBBtk0e71GK89LxJTROw1uXHYL2KZcqaojWRg-eKn8DLbalOBhsHioEJVdoNbx5rp0vMhO32rH53Z3tL40Il4NDCw0nbUG8bxcIPFHd2-CBHch0IhF-dpOtvwYqtpywXRUcVJPE-yayOBNsfcNG4Mx4_pcvaQ4LP9u8hhJMsDG0L32BXxHg12lJ6OISq_5_vjLfglACI4V5U_JSLv7jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سفری که در حافظهٔ ایلام ماندگار شد
@Farsna</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/farsna/447908" target="_blank">📅 16:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447907">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d5a8cdbd6.mp4?token=Bv6XX1EKyQx64LGdAc_FErnF5044Chv6j6rpsq6GNJUuzZZ_v5Bj6_pic_WiVeScaoW9kM-1ZiB_Z6O7xW9Sy-DH8Va0u76zq8NOdAbENjFFIlfysqSgmURY8m1gdhLwJRbf9pVstMQvw31M2q71icSOKozbC6ZRUojs7apGHiA63dyEMk8w8cjIKsyY_AUzGV_XyJMVtW7ZIBRbOaogUNmjt_A33WP8La1EUMS-Iyrk4ferkKQl4QOhCh1rzFmkgXtwud0XVV6abmFZInLNXS_yLryP4F_pOqHNlSABFS6gRRgFicMSGGWuZy8Ee3H7U-xst3UoIilLKKFqyR9gUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d5a8cdbd6.mp4?token=Bv6XX1EKyQx64LGdAc_FErnF5044Chv6j6rpsq6GNJUuzZZ_v5Bj6_pic_WiVeScaoW9kM-1ZiB_Z6O7xW9Sy-DH8Va0u76zq8NOdAbENjFFIlfysqSgmURY8m1gdhLwJRbf9pVstMQvw31M2q71icSOKozbC6ZRUojs7apGHiA63dyEMk8w8cjIKsyY_AUzGV_XyJMVtW7ZIBRbOaogUNmjt_A33WP8La1EUMS-Iyrk4ferkKQl4QOhCh1rzFmkgXtwud0XVV6abmFZInLNXS_yLryP4F_pOqHNlSABFS6gRRgFicMSGGWuZy8Ee3H7U-xst3UoIilLKKFqyR9gUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی اینترنشنال کلاس احکام می‌گذارد!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/447907" target="_blank">📅 16:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447906">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tf1Euv4yV2-mD1Hzf6NgZq5jSkcPdRqJtXg2XLgp9Lneuks5wcR6nQ2lotvEmNKBoWBNWOu2E6pFrQMH5dV-gMUhDxBz23Ms9k9-786ARmwcpRoHt8kwO6xeLg2qrrISYMswTP4Br4q4gT59iwQDkQuaQD2kgOJY_zbuv5p7Q2EPq0w4AdKWI_xBHlSUVW9vTdpxMAbR2L2SMCko9I0LY3akrtYKV_ywUkRwwlyain2Qj-oyzWj4z2f0GbVrEKBvXRMszeMCHf7kRpVpq--qu_J-3LVRnh13pKC67aJfF_WffA6TCjmk2w-Zdm5LXEKk7uqpSd0lcTzpeQH87LMPGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آستان قدس حسینی: شیخ عبدالمهدی کربلایی، نمایندهٔ آیت‌الله سیستانی و متولی شرعی حرم حسینی، فردا در حرم امام حسین(ع) بر پیکر رهبر شهید انقلاب نماز می‌خواند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/447906" target="_blank">📅 16:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447905">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30bd08b26e.mp4?token=oE6LXTLoFbt8OCLr8a5EutjOn9EjYd9iM6f-NtisgYzdO-k5ZH20Ex8qOnrh0L5mEU1g0CgReBMKue6iDHl5vmI-jgnqJcE2CWThpL4vWB8IoxYVGmnAfbnRkvmvCT5LxgMOBvH-6U5octk1QT6y0rILJOfGb3I5NFCcmcenrLMd6mVfEFc2b1B-lcZFsVGgcwLuQzf6AbARQxOZTqPi54ZDp-rYRwc3ck6oYOsBoaISvCB_L_Gnm9ldeRRpm7g9nYyoTgp7_oEjlj3gLacIOnMjkdtFNIdmWfD7tJWS3ZpoCVY8z9Bo0XhFVT6osZqhHkHpYAM_8T6eJ_oX_SsMTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30bd08b26e.mp4?token=oE6LXTLoFbt8OCLr8a5EutjOn9EjYd9iM6f-NtisgYzdO-k5ZH20Ex8qOnrh0L5mEU1g0CgReBMKue6iDHl5vmI-jgnqJcE2CWThpL4vWB8IoxYVGmnAfbnRkvmvCT5LxgMOBvH-6U5octk1QT6y0rILJOfGb3I5NFCcmcenrLMd6mVfEFc2b1B-lcZFsVGgcwLuQzf6AbARQxOZTqPi54ZDp-rYRwc3ck6oYOsBoaISvCB_L_Gnm9ldeRRpm7g9nYyoTgp7_oEjlj3gLacIOnMjkdtFNIdmWfD7tJWS3ZpoCVY8z9Bo0XhFVT6osZqhHkHpYAM_8T6eJ_oX_SsMTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مراسم تشییع رهبر شهید، نماد اقتدار و عزت ایران است
🔹
هم‌زمان که همهٔ ما سوگواریم، با تمام وجود به روش و منش رهبرمان افتخار می‌کنیم.
🔹
ایران امروز مقتدرتر و سربلندتر از هر زمان دیگری ایستاده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/447905" target="_blank">📅 15:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447897">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MTo_UDiCOBcNWfhZO1ktKN0e8BC0cwWMZxMKHQwqSq2IDzYr_aUaukiniA_8CAKkzUS2I6UZNtFiJJdF2gqVMi2Mc5fXEHW5U9GZ-9coYmCz10QxcKr9OqSf35wzqT3p4elBcMkh3_bUvJxdQtbIEB4A3riKHCsAJ5JVtSLUeZnnO2xLuisBNvYnB473Bx1BRiZEvSh5U2Y9q04oGrEEfg-EP-kqenqbEjk16jFz558hssuuQyDC_hasJRncsJqB4Xx6FWhP_i5LlVt2guS2gl9bYV0MGYLO0Ae08r7aGUYavMpG83Lki8pzGyoALTOILh4icP9BDmVoVQpopJnVWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eAY4XDsoElcIY-OJOF6-Dzqx-cBI7uhpI8aGEW3AfptnPxQpcrzueGOqlOfoVrWCyGimDTv-axa_JlYrJXE1-ldNdz22MzWaKJxe4IkisSN0Pky-Zmo18Tk6jIweL17mWVj_j1Azf-NmwOgNP_uumhGpnzeEqZpf9vty__v9bFivQr2yRGfiOZw1p1vbDi1dMw8CA1X0VFrC0LU0XpBjmwA4Ggy2vkNfX4nOQhFAqGkOpXk8XaTahnBP0o9eXwzxNBArKOF_HCy5UGdW_6te6XW2pn-NkcNZuRwP-Biw7hbH_LPjAlMfdauvJTB2ZzUGOUuPh5u1KLy6h3OeS1XJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CFLtJW6J_HuSLpWUwlcO7DnHDYRBvXCDqWbiSFeQno_r441j9ReT_BLJ6PmEG3DnM_AD6x3RpOkp-_t1rJXF_yv5IYIndtMZL2QLApC-SOc5jtwxGGvn7dItF5AyORdfNM_FIcBERJNzxIfVWfGJCZvlTD3GF4K5whYUcOfiCwh0Vovw3KzZr7ozM5Avp5wUkQ7Iv7eP5Rf4QmGSQEP0IZg8idnqoSZzl_E3xOnu7FYWvJBqP2VUcs3zDSZS1wo-qC392vpdN3U1XVpxm-AhD1UXzCj2g5fM4GeFPDwVDfM3FtiCKJdWmFqeJh-KSo_JBDwxXSESxWgJC0AGVQa2Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ddJnK1DFtpOyQckwwETv5HOyXaGomj6W7uK_yW7ApJPSWfvTHNmZWGC3hYTM8SGDCWGyiqx9xrLGBaho1XnRh0FE28QY7nBRVhRpGYjk99sRwOgGsThYG-gv94FiTfT10yaZzOHjTMmb5uFFaK7YAVKs0iU6zw7epKYtrzmHi5L2m7JtNWiYZok5PpWqBa0YrlvKaLsHcx72AdBxF4jYP0VhAXOGHHjKBWsHHgRvTh6hbGz8XxpX_LsaBTSJ8jzKFRvAiikR1_VnX3x5svKFm-aNc_Bl1yRojhusxb_ysWhXvZvkfyr6pTvTTzVcI0IUGKD5K8pHEk4pXuj6tNrR0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RnY0DuJHDa6S2RDQwfnK9u2zpHthGaQeyWt6jNyvTL_WN5tstI269wsZsctGTMkIG5q1bmbRZIL34yiswY6g02jz0ZcY65ddxjcaoBhVq1ALqh_p40HTEBLcqmUa5801okmmW0ozpzRQnHH3wahrIb44ZRWfslqZnoC6EToGv3-YgJaa_JGOGMZWuBeKtkqupGuYRD7iRDPXAY7yMEuYX4NWjgvYneGhQ4fWXCZ3JVoEOG9K6yj8jlozlXxY6sTFjdw3CHAjPlVw7jaO5_4Z0VwoynYqvFG7VdeAPizSw14IRCkqmWrs_pwBF4W4FrO0PHP_HW0J2crUbqfkNe0sZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RLSGAlB9BdnVfRMEJtYFe8fFfTsymmQlkDVVu4iX4kGKeXkc4EMSPKXmM10IaSKqVMLGVpEWQMs-Q3TUTeyurcLHyItsQ8wwgcC1tM3zHYgDkTH1Q4sjX4KjXpmORNRoNXw1kLAvVZygCciPtGiXvhq9Mo_2ieyEYFi1a8WIrX7Bkh1Q5pQ0fz1MQDWzsobBJhmGQIZxD5kvymmBYobbjhAoNGKI1VXUmuI4w1BCXdixWwJxMRyzTLzfAXCxAqJg6GeQrP7di4LqySln2_H8I5c_ggyQySjK-GjKRYjYajAt79ax6h6P6zh6fXJDs5lwG5G-tw7fz5FGKlg7vO8fng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ClYcVcNOjsHL-0EEsRUMY_6VnwR-WIDuGXyLf4w0bELpBOiytWYtj7Cm_Q04UuMht_zgcuLvjnbphidtPrDTuMBaE--HFSONJlm06ldgjh8aE1n4mbCWIAZ3XFUa4GWnlOftJ_dYugAVbC6wPBndZEZrDOccTET-7ejnGb1c851XxrPY2fjrMF3xa48PYmjE-7ms3OSI9dZdJVlCJ9TMeeuoqdb0HkE-k6IJBx5mN9tVXPE2L1ggtE1UEaoUAkOz5nInCVOmITxCXTugPr4Rf8tO_7PGIHJYE74G7wZ6Mr5QRYhdfs5GmXToFUrBclJXhPKsM4KPPvsMdvU99E50FA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تشییع پیکر مطهر رهبر شهید ایران در قم
عکس:
احمدرضا مداح
@Farsna</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/447897" target="_blank">📅 15:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447896">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebukTTdiS1mGGvhk92CBJe1mEmsbmt2tuD2Q1sdvqLZ62NDLZ3SG1-zT3jjJvajsZds6uXfxLuB95eOW6IsVxKsr13fhO6FYf6rZq8C1ovP-2Kbt0M32ney5hrGhMRI5X4-HVXRHxK3Z8j7pj_pvuDPf0CMdrkxSY7lZLsVaZoMJHBgPGpjvTxiwfr2s_29mIFOIH2HADM2gVCB77RGrH3J6iD_aTvfAwW3fO0uCfQftZzbo_BoOR7i-8UNCgckJL8_uPfenxxre7ekraC8oWPsFFS_TjTeR2LgMnzFS55U4vRirtXMY5Dl1FIf1zIv1xs6UiVyFD90lUKbQIFUKHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جابه‌جایی ۲۴ میلیون مسافر با حمل‌ونقل عمومی در ایام وداع و تشییع رهبر شهید
🔹
معاونت حمل‌ونقل شهرداری تهران: ناوگان حمل‌ونقل عمومی پایتخت در سه روز برگزاری مراسم وداع و تشییع رهبر شهید انقلاب، ۲۴ میلیون مسافر را جابه‌جا کرد و رکورد جدیدی در جابه‌جایی مسافر به ثبت رسید.
در این مدت:
🔸
۱۴ میلیون و ۸۰۰ هزار نفر با مترو
🔸
۸ میلیون و ۶۰۰ هزار نفر با اتوبوس
🔸
۶۰۰ هزار نفر با تاکسی
تردد کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/447896" target="_blank">📅 15:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447890">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nZlnTvuQGPjvZiSM6mer6srJkFGm8wOWTzZ-J7Q6dZ1aG4YisQxbSmqw4eMdnBBDZqM9o3NxVSrYmPI7m06TevNGxQzk-rSe3HxQETbUTNT08DtgtcD6Qym03BFLhbBBe5XipQSc2KirCurRY7bLoumgVmPYnJMgrQ6KI-VgoRKijYIAEyeaMWaZ7GDXv62M2d4_d2b2mcsPJzgscSLYo3uXOw3885AYo8ApcvC4lGcsCpFtgxwMD9L4LPd2bbsOH5b17AU8Kq9Q9_IFPm-rCLmqFazK8OXNyCPloUF3_AxZiCbuVp-bLGlCamtc_PMjwZtFyKGKqfTsQ0j4LUg9hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u8CzO9VnY3z4L5SoKAP9q9Vbyhzl2yyPwHU8YHbWyZEEyY6W7BNd5FKtV8MaFe-HGrDiPVJ0cLyqOUXxjaEM6cc9UcOY5Cr7mmry624MasXDv5PVVTb-RO8SJS2I4xd2Bv421XcIYST5Jogi64fxIaQqv_Otec7K19WymA14QnvpKCwFTNXp-rW7HXTXI924kTFCtmlTZqCeB9CfwdHthw0OClnyemWv6NRa75FqIojFtlNO0BAEVtSVXDg21LXZ0D8PdXTkI06GfGmzNfXH1ovoQs1dmV2TC-EQLWJvOJ7HSAnEO-CB9tH__CDDzVglLRu_nCeMarosYn5h6-fNnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fE04QwvoPikCYo5KeqQ4A6CaFFIbY2ttOrQ4wrRaRUL7fJB22ggc7F_VKi_KUZ_I461jXOuoZiTalPVbk2OT691xXtUoZ7DVMV1c969Iw6YXmjFbtHGUC-SVVw41jJkHMtwafmnTEG42NW-B757fi704p7DcPvXH6_kofFeRFqjRcP4g5I5twhaC7tWuYhCBbDmU7eRObEiV1Xz28cfRHhMFu6hSP51stIq0mewZX2Lb77zU-0fIS6aOvhVMmf1xSj2goiWPWa3TFn2Yst8Weaw3C6gt0ldI4mSQ5htyofASM8NNLRqOQjje1Cv-1tlFTUFlb4ZaNl8OEsuKYqLrbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VNwLKRM80LyFs9cRfJE2WtESQ-tW9Q4KTRMHtBPiWGpWsrL9e8XUqeew7y291XXjX__JhkwChtb6rgwrK-DBT8Y8AzTpLB9j86xulsQ_xfG5rti4iSuLXU0FkeiuNZ_quPzizIR5R16zwekslyJJIdlh6_E61cq6GvIse3qw9pS8A9rByFaWqNPGulTCwmpdRna91PAmB53cvu7VAlMLssJqWqO6w11d4uspacqzal_kSfW4tNKVQXOYBy-3VfFlHsmPZwpm1C6V_Szf1gWSQs2UALyNc5gcuAS54ARl_XHZwLrTeliO-hAy6kuHsfNwxkIQlET0bR9XejHLUDlRIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ac2--cd2lUj5qHxcXTDgr2v1-L54EAYVA_NehOTKrgQKPMK5hIepSOketgL-VvxrNPxsjyElmzInf1BqfoVSdgmdYJgE6YN9YngfOlVBoPhTz1zR5Cr8zZF5Wbe0Td4PvqjtwnYvou4y0_t59Ibcn0_dBia3qfZEax2vEVRLF-_zxdgiXjSTCKiY5CBHHA3BPqbmV6fvFMEm_8oEgQKv2IyJq_nO3MLTRjXcxsY7kEV8wFamhvsPSm5QWsX8GApNfuqf2MEowDiIW1HofTofBbgK_DD689gpkSyX-Hb-DTMS07LnOoHWxToK3D2GGeul4QnNPf0S3Im8LhebXvLldA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MckTovpj3JgWYdpGCHYK2Ikbf7bnZXJWh5MbN2yUX1UGqNj3CGp71X6d89-kc_tJ2pksm9CBdsBhpdHW9Myf1SDL2vP0YEVB1yN_dx-8kIsLDP7x3WmhwleYOwBqC_a5jmFioBxSlZKoncxB8sITBGae3IE2yKPua8U6yimL4CzMdgUsmnzqdv3XaKDoNpAzkQF_76Q3m3TT-O7w2sGWoVUnXi6DWxy6s2JcgBPky4PVFii-LJ4PSeiefvzro5VsYtgzZVmxVXgmXKKusyqBiHI3Ko9_nlw4aILm8bwvAIC77Ra46Qxi2bQuhvp-d6fsYyn_vOYlqdRphMX9JHqR3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عراقی‌ها، آماده برای بدرقۀ امام مجاهد شهید
@Farsna</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/447890" target="_blank">📅 15:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447889">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d6a4568ee.mp4?token=VB-44vaoXYTD90SSqP0SbWyGnPlsPjAJSEbQaEfYtYevfPUxgy8NyrToqmlyR7cZXEkWlCFOU3gXDmOiWy-CfcD6bBZeNY1wIhwZTOVc5sbrkVbYoc1QiDfcIGIl_YE4FN138YkcNUc9eZsQat_j6Q7V4F_W5UmP3CARRg1IyBTCqB60YhxyvODTpmmvw4zooiImwUDlZ7r5Kazl_8rk97IuSpiUryIgoi-MyvjHJUJRHirMaNhTdzQZ4oJCDoWegkhHEYYRwgN8PKTwyU8jTWk38jf0N_5Omux7LvBA2pv6oDlfWM8Dx6dK1fJXDe-uwhWrGOzoa2R_KNdJ_9shrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d6a4568ee.mp4?token=VB-44vaoXYTD90SSqP0SbWyGnPlsPjAJSEbQaEfYtYevfPUxgy8NyrToqmlyR7cZXEkWlCFOU3gXDmOiWy-CfcD6bBZeNY1wIhwZTOVc5sbrkVbYoc1QiDfcIGIl_YE4FN138YkcNUc9eZsQat_j6Q7V4F_W5UmP3CARRg1IyBTCqB60YhxyvODTpmmvw4zooiImwUDlZ7r5Kazl_8rk97IuSpiUryIgoi-MyvjHJUJRHirMaNhTdzQZ4oJCDoWegkhHEYYRwgN8PKTwyU8jTWk38jf0N_5Omux7LvBA2pv6oDlfWM8Dx6dK1fJXDe-uwhWrGOzoa2R_KNdJ_9shrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ برای شرکت در نشست ناتو وارد ترکیه شد  @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/447889" target="_blank">📅 15:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447888">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05958b3d00.mp4?token=gLwEB5GfrtZWndpp15WkfR1-sOaL5IYlrLrhXXJyGl9SRJf7iI1oVr5kmABsrueE7F6EqGdRq6cvPgtbzizTuYZIw_TgjSa8zePiKcJi-QJZCWqNEIstVmA7IeCzQ6YO2OoKU1lX2lL2x6Oq1vaiuAVbKuNav_81L-86R4-AJ-B8lmx2nX8abRgH0hBIDYOH1OtpnxvVV8rHP6IDAV8oJP4OSJCURNdYGFFyotSxEmqb4Fzm-ZaHt8Iueu_vwPLOvX9RLshBkT-nUEqL2Fc80syUqciTBAnXmewkojABnLmQ00VrHtpzezsUpzu1vxgiF8y3KoFgnPYz84crA2UDag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05958b3d00.mp4?token=gLwEB5GfrtZWndpp15WkfR1-sOaL5IYlrLrhXXJyGl9SRJf7iI1oVr5kmABsrueE7F6EqGdRq6cvPgtbzizTuYZIw_TgjSa8zePiKcJi-QJZCWqNEIstVmA7IeCzQ6YO2OoKU1lX2lL2x6Oq1vaiuAVbKuNav_81L-86R4-AJ-B8lmx2nX8abRgH0hBIDYOH1OtpnxvVV8rHP6IDAV8oJP4OSJCURNdYGFFyotSxEmqb4Fzm-ZaHt8Iueu_vwPLOvX9RLshBkT-nUEqL2Fc80syUqciTBAnXmewkojABnLmQ00VrHtpzezsUpzu1vxgiF8y3KoFgnPYz84crA2UDag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر مطهر رهبر شهید با بغض و اشک مردم ایران بدرقه شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/447888" target="_blank">📅 15:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447887">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a71d2baf61.mp4?token=MDxkYZ9PoFYkya5Yb_cxhq9BIzwusOyHvn2TeqYXJcU5GBXCLxrRK2A_wrLUMRSth5zsY5Yot7C9WAh0uybqO5uF2Lz3HnENw_bzEU4aPvXSJvCM_JkXyzo29-YjCzvfdRXCQ_2c3EigUsBLog495Zav54bU3rEPVWmoM0uNXg2vxCCgX_dXYRKkO90ms0I2g4Mm1PrBy1MEI-sCAFoAWVQ6VGwKqsFHSmDtoMsGSz1oT8T1evLvO3ufIZwRjFUlrbPfVXUURkRjYs9tWfsNyTHkn8o43YAsfad1jm-vnPul-c2J2M8upCg9TnqOM0ttvq5tPqZE4UVA03SB6sarNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a71d2baf61.mp4?token=MDxkYZ9PoFYkya5Yb_cxhq9BIzwusOyHvn2TeqYXJcU5GBXCLxrRK2A_wrLUMRSth5zsY5Yot7C9WAh0uybqO5uF2Lz3HnENw_bzEU4aPvXSJvCM_JkXyzo29-YjCzvfdRXCQ_2c3EigUsBLog495Zav54bU3rEPVWmoM0uNXg2vxCCgX_dXYRKkO90ms0I2g4Mm1PrBy1MEI-sCAFoAWVQ6VGwKqsFHSmDtoMsGSz1oT8T1evLvO3ufIZwRjFUlrbPfVXUURkRjYs9tWfsNyTHkn8o43YAsfad1jm-vnPul-c2J2M8upCg9TnqOM0ttvq5tPqZE4UVA03SB6sarNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نایب‌رئیس مجلس اعلای شیعیان لبنان در سفر به تهران با عراقچی دیدار و گفت‌وگو کرد
@Farsna</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/447887" target="_blank">📅 15:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447880">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cbH0fx7syI_mcoSEWBX0F5pXlnd02lfI6jqKI2I7nOYpMCu2zmSJu5dy3RVyy0k-pEaQNX2wlKF5Pf5lgUWu1pGXuVpAe9smi6v-nqBeH_PTr14PdKCI9EWmvDDfetaP6g8Z56jti8H985x4PT0ggtn2tD_3ZVbIQb3seboObO-0n5Nwc6huC2g_2GvurRDEH_nZn8QfBjt29cTZAdcD0mbGyHEh40LTRssBRS6tYB8Iwp3YwVLp433sR5a-F0BfVCeyRq7lK_9ftJyRSsYvycbko5gEUc7ehkLB33v75PZNZZ9Bv3wAPWEUZtDoLILwleqzheHQkzc3-oIWDfzFLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mlJp0zIYalWBnwUbcB2eS70xBo1T9FNRszhZN12Jq8l29QTnUZlBuxdR7aDAm8NWTX80OA19IeaWp_Z4PaxV0Mcyf9qoNUIbS5RHOFZJEAa_ZdQr5QUyWUUpS7C5_KITfIZC0dNTDgXtNerb7xUwP6ggAP1TePhy_aILlC_vbGyKz6G38Klxsu04lWKZwnYHVcbyLflYZslG0O6rr9zun_7ksyQQdf2r-0GyQbDK9-8m1dv8OC02cdAwxXbIDwYpL34Txt1_s1OczmfXJqP4RHXQaG4o35YWTKKSnS56JB89UVM_f_SbPgyUHZJIPjlGZsMLFwwUxK-TuJNobge8pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mHijAYNl1YRD_tujN0jyapAe5Hq1j2IzWSbLh17tqlz4wpzyxH_Jj8Fjzg0Hnd4H4COtbC0KyggtUrioQt_407ejGsaT6eSBO9AaZRmHtdBhXT5v4DEv5Yl175HoUeGe7D5SrXcXAVQfR_ADk19IRBJWVJ9Fe-8IooMuaeMCAUEGQny1x7bhTjd39_HDPUwQxFqN1cgCdBJDEw8_N1-jml_7-rpeFDfayl6Pad0_0pnfXOz-4_9-6R7ftW0e1emOUqHBfiaJRZ_FW2mzqyHOVFBK8_t3D83KsSRMprRpIq330ZhjTaj1vgYqsyQlZXyY16LDhs8J95FSB0uge5vqaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yd3SvF2QadUwBCeAo_Iph66_qBzOEBD6G1qZdCmJziRkqxNNyzrzEjuM4JVg5rSkuMW2lBKOZpdzXmYxInM4s61ou4TMRa8wH8h54tONuMbsKi-gmP0qQqXSsYpsKxR0IXfSi1mF0zIRnhE4u3rSfUKkW3UwtLE6BZ2OfL-MK5BhRdRNJoGbEDufhkT4MZSnrWJfYgB94Z71nMOVi_1Ui8bbSXvO0MLXZoBpnqGbncBcpKztp8Z_f5eDQ6RClIYl1YhC01FhMq5PGsfWqk5y3EtFFf_PEJI9Rv2DBfFF9tefNPtCy_NpxrTU4_TJLmpzA2eokC5AGNPGpgANtkLeUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MHotbM_kIqP6gZZeUx7Thpptzsxw6wcNVERssO2z2M4_6PvvI3CfetmriM4KtA_wc-mlQ_EWedhkrlWpiPpAf4JTLCWgRunUTfg_jzZrY4I6sx9QLv0y5v7pcVWqpMMWu3tuWw7_ikjRPkYFP3UoXRuNmnojeoETq3MzJsil3keYw3f7XsaKzhkpVP9PQXI1f5HXJjzbl5gDztE4WSanGnC_Dw2iGn7BiwivFEWGlPXxC8EP4NzCz6Xv5o48jPXaRc8oBi0Co0A09aApB9SYqGZ4aFj73dr-K_hxq1jQ4QW8mpmUtEF8ogcrVk4PftjQrN-nrBQ-0ggzOdpzMWJqNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3cSgF54t-bIm98IadSjceP04pXIGmNsvlVQqL26gCETatrpZrBEgNdn6tBoUhNYq2R90L-JdIFiDduSCqkkh2vFUstfxWGn_pEZE44dRKbvPFhoTEp-fSDIMMTJCSOujDhlFIRBu_s7keoSPsPUaNFmxLey1p6yt8v7SsDMD3fK09FARl_l68ziVVS4qNBnrqiA-4XTOGcBYe1ycS3GIKqT4nZWbOE3wavls9lF9m3MRsXshE2yGlF7vycFsubop0XpptMn8SyIGRN9s5XjS0WizxSKBiw400nhpKul8k8ipbazot0lE7kHpax8MiQ64zkS2M877Qsq2Gkl2ZvV3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J_iAj2Q6v_2MJup9OEc_9SsFyloeU0L8k6JUrxZspO_HBsPrzBEJDU6740SlkLS8DpYila2FJ5e8NKoiLMdTaMmzo7LbAXxxwf1Dqn4oCKOFwCsXQdbSzJ2a0ED6LAPjpC83LxhWI00OdBquoxjNuGhfHGHyZCaSokLmCXRbWsmgG9rAP1vch8WPd4aaPAWFFrYbkWmSle0J-qdt7B7nQuWL3R0JPjvsrcowTp9w-Ub78a6ck7hUDcRfSi-Huo8jlLy489nTB3wtK-0GZcQx57N7MzFEbWc3sTDVKGPrHb-QFHF5-5FjYyq-tPXx_Qzgqm-jPvBnKWqLGRx1I_Fuhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نشست رسانه‌ای مهمانان خارجی تشییع
رهبر شهید
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/447880" target="_blank">📅 15:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447879">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbbb7123ed.mp4?token=gOpoA2lvJwwP8U9pa-utnwPiKuJjqcxYpzWx_DjZlIZ64HVrJUpmTYBJYLoD4x5ZDzypBF5r41SlOoOL9UOL6_PM0KqIKnPiIwhVg-0PE4XIZaEE3eHsdLz8JyKMZeX64n7PV9yjchL47Bbk6u5OwYemYOPoSmfVCIwhieu3dHFOxGdwPR_3Dj5PnwlwN0Jdc_Vj_trO_1tZuST9sggjh6T9emSDNcy4ZLQNv5-nzONzF2hVqIdYlcnzYg0tUvcTtAUBO43KbaUshnCmwCG1j9019A2PoMe_O-bkcp5txhi9W_hUOASvnsIGYVPqat7HA-_tFOn5s2DP0Ule4kXQm0Dk1ILOlBllpAjldi2cWgHCizp2JZIDim-Pu6Jv5C5z3UZlOQLIOD8J8Ve5b-xTwbIWeUaPq-qDOOuAAvkUw9xEccSv17Eff_4rv58BUQQHy2SyLVyxxKSJrw0kziwSOmTuAS6GvCzokGOxlt82AE1BoweEzr6U_kxkAu87FRv4D3GQstBu_lw6zwKtGcZU9b04FEt2TLeXC30O_nYZNnko6QWG_PJs8kLPY4UDCGbYxXioPhsTjGZPrcRWgMIXipraElMjaWiTeXqC7QiHzHU2dlzAZsgyFweUQ1LigCVzVr0-oi4fWlBlDGdZVIb-mY21ZWKmWzkQeldlVqmAn00" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbbb7123ed.mp4?token=gOpoA2lvJwwP8U9pa-utnwPiKuJjqcxYpzWx_DjZlIZ64HVrJUpmTYBJYLoD4x5ZDzypBF5r41SlOoOL9UOL6_PM0KqIKnPiIwhVg-0PE4XIZaEE3eHsdLz8JyKMZeX64n7PV9yjchL47Bbk6u5OwYemYOPoSmfVCIwhieu3dHFOxGdwPR_3Dj5PnwlwN0Jdc_Vj_trO_1tZuST9sggjh6T9emSDNcy4ZLQNv5-nzONzF2hVqIdYlcnzYg0tUvcTtAUBO43KbaUshnCmwCG1j9019A2PoMe_O-bkcp5txhi9W_hUOASvnsIGYVPqat7HA-_tFOn5s2DP0Ule4kXQm0Dk1ILOlBllpAjldi2cWgHCizp2JZIDim-Pu6Jv5C5z3UZlOQLIOD8J8Ve5b-xTwbIWeUaPq-qDOOuAAvkUw9xEccSv17Eff_4rv58BUQQHy2SyLVyxxKSJrw0kziwSOmTuAS6GvCzokGOxlt82AE1BoweEzr6U_kxkAu87FRv4D3GQstBu_lw6zwKtGcZU9b04FEt2TLeXC30O_nYZNnko6QWG_PJs8kLPY4UDCGbYxXioPhsTjGZPrcRWgMIXipraElMjaWiTeXqC7QiHzHU2dlzAZsgyFweUQ1LigCVzVr0-oi4fWlBlDGdZVIb-mY21ZWKmWzkQeldlVqmAn00" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📽
خدمت رسانی بیمارستان سیار برکت در چهلسرا به زوار آقای شهید
ایران
@Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/447879" target="_blank">📅 15:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447878">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدرگاه فرهنگ</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b651a243a.mp4?token=sDeaMYeFkeOJr9ZJgakFx_xpzhTh2jnrTzG2aQI4Ln1TsmAsHal7CAJOqLRpVi6V7dBXqpIgyjbmkes3qcyy_yrc9rrXvZPiUFqX08aGMpKndxdQTX60oPsSEnY9nC1k5Z4QolvUGoBQIsZbJEGzjKRYKQu7QsVP8M2ZzW9FoIrjxkvcxx9bXZW_gNx5_XRt3MxAaA6F7u4eXXAHJQ5XLbr0CiyZZ45RNAWWl8YnQKfwnRoh6exXnstsiOc2IkBTDeUdafHH4idmWhXQhMO_TZWAVP_2zVJI0sT5iWX0drJnTWkGj1mFbMI1ZWJx8KxN8tW-vdkroQvSwWuCtoyFvAhaFEOKdQSbK8kFIJstIqzuxxugXwJ5iIAag8AoC2k-8bMycMEny80iLPeUVui7vy_GoIDVGu_W65hHj9s1beqxb8kNGuC6-TZqa0PUqH6TTGyCZ44vYr6E_2CY0yQgpd78oonJcgzOXt72RFzvhgSrHYREP8_V1YHu8SDRyFU6PFGpMMry1gqNRKo1GXzgXdWuOkUFaYSRfVyPlGrF_WuTNOaa46rrHqwCjpc9xphFm-auBSVjnzNQ2x1Lx8U7lgGPltz6kY-aUQcIOOEJTdTK5ZG8Tp6li48WE-ye_33zrYiRrXH-VQl-Zw9w75yYzVnZHZZiTwI_Yzeh5VwCMyo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b651a243a.mp4?token=sDeaMYeFkeOJr9ZJgakFx_xpzhTh2jnrTzG2aQI4Ln1TsmAsHal7CAJOqLRpVi6V7dBXqpIgyjbmkes3qcyy_yrc9rrXvZPiUFqX08aGMpKndxdQTX60oPsSEnY9nC1k5Z4QolvUGoBQIsZbJEGzjKRYKQu7QsVP8M2ZzW9FoIrjxkvcxx9bXZW_gNx5_XRt3MxAaA6F7u4eXXAHJQ5XLbr0CiyZZ45RNAWWl8YnQKfwnRoh6exXnstsiOc2IkBTDeUdafHH4idmWhXQhMO_TZWAVP_2zVJI0sT5iWX0drJnTWkGj1mFbMI1ZWJx8KxN8tW-vdkroQvSwWuCtoyFvAhaFEOKdQSbK8kFIJstIqzuxxugXwJ5iIAag8AoC2k-8bMycMEny80iLPeUVui7vy_GoIDVGu_W65hHj9s1beqxb8kNGuC6-TZqa0PUqH6TTGyCZ44vYr6E_2CY0yQgpd78oonJcgzOXt72RFzvhgSrHYREP8_V1YHu8SDRyFU6PFGpMMry1gqNRKo1GXzgXdWuOkUFaYSRfVyPlGrF_WuTNOaa46rrHqwCjpc9xphFm-auBSVjnzNQ2x1Lx8U7lgGPltz6kY-aUQcIOOEJTdTK5ZG8Tp6li48WE-ye_33zrYiRrXH-VQl-Zw9w75yYzVnZHZZiTwI_Yzeh5VwCMyo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طنین اذان در لحظه ورود؛ گویی آسمان هم به استقبال رهبر شهید آمده بود
🏴
آخرین ورود به میدان آزادی
#باید_برخاست
#یالثارات_الحسین
@dargah_farhang</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/447878" target="_blank">📅 14:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447877">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/447877" target="_blank">📅 14:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447876">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مازندران فردا تعطیل شد
🔹
استاندار مازندران:‌ در راستای تسهیل تردد زائران برای حضور گسترده در تشییع رهبر شهید، کلیهٔ ادارات، دستگاه‌های اجرایی، مراکز آموزشی و دانشگاه‌های استان به استثنای شعب بانک‌ها و دستگاه‌های خدمات‌رسان فردا تعطیل است. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/447876" target="_blank">📅 14:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447874">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5fZDTANAZ1pBoe-4f7B6t9XxYH0O62TRGcNI6XCKx324PHKhL_m08QrG6StqsKzhlvu_7HMrqCHt3kjp7q5v8RL2XZBx0lkqmc_yjfqD3O0A0nuRKl1LB9ZBmIr88lFAyfkrfDmurUTh2vUP0TaLlV9WM5gWFQRJxY-jSp_2tfVk9qSc3FnqE9IFK201pOpVrU7jSPvf2jmjUoQdp2bZ9UjWHOxT6Y3szMDX7MlT460lgt_rjHBOFdnC7FB8FmkBz6zznqL0VCM7W8XAVpqxcFbpWkYZ35pQ5GdlIr6wpA16BZoFTuvl4nULNQSo_edWTi75x4xzMZtC20KaKQxTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عمامهٔ مشکی‌ات ماندگار شد ای آقای شهید ایران...
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/447874" target="_blank">📅 14:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447873">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/326861d6c8.mp4?token=LICzIv5OWNmVLRf9HM3maA331QKp2Sh_EX1pz84TwhmsOE7d68BSxubfHj5-1NCsyA0Bg8rpRRcWXVqcjUEbglk7hzrTo0Uw3alBS5cLoVuAg_sXMwVd4Xuhc3PxtDEYgCTGLhjTSS-zd29XCtX_MGIHeELi-TxdTMZMXauxQJUIULAD_PBd4ZLDVmVmK-r4_GvOR7K8xBZpSZ0gz8fYv4CHZVh9Z33JXRJB57Z4Z8qhUDzw0xWHAk3lU0giQay9yZhKqaSTGCXmFjXeUNx4-zT_-ahg5Yu48ivrex55dT25hnHWV-EzfvEbZ-GSQZqBM9MFf6CLGz55EY-2W7tQJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/326861d6c8.mp4?token=LICzIv5OWNmVLRf9HM3maA331QKp2Sh_EX1pz84TwhmsOE7d68BSxubfHj5-1NCsyA0Bg8rpRRcWXVqcjUEbglk7hzrTo0Uw3alBS5cLoVuAg_sXMwVd4Xuhc3PxtDEYgCTGLhjTSS-zd29XCtX_MGIHeELi-TxdTMZMXauxQJUIULAD_PBd4ZLDVmVmK-r4_GvOR7K8xBZpSZ0gz8fYv4CHZVh9Z33JXRJB57Z4Z8qhUDzw0xWHAk3lU0giQay9yZhKqaSTGCXmFjXeUNx4-zT_-ahg5Yu48ivrex55dT25hnHWV-EzfvEbZ-GSQZqBM9MFf6CLGz55EY-2W7tQJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از موج جمعیت در تشییع رهبر شهید در قم
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/447873" target="_blank">📅 14:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447872">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc22eef9fd.mp4?token=D5WSUTYLlPFcQw5N9AvRYsIMVo4AGMH1aFdVaNxKubDRaQAnhgYtqejMNWXNmQkBT5mrKqNQ0NB3CVLjNARnUo_kzhLZePRb9VZbVkA32k9J8Xsmm5NRcLgQczaK4XSIaK-OXXvRE6Z4nNTbXkykxlNB6dJZYuORhEXstKbpTwdOPGlCW07ejM6obYnLmKNLAbjWD4XP_LZRNNrb0NNyZzDC6SZsdC9ozCygJCYE0J5paBu7OxF3mL8sp-2fuq8_mmyCtAlO9PFYLOn8RT9M2CxiTfFJc9IKDm4Vccje59RAmzi4v15S_o1ad2wCzwVC8NiaQPutUSUgm-3P0kRwAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc22eef9fd.mp4?token=D5WSUTYLlPFcQw5N9AvRYsIMVo4AGMH1aFdVaNxKubDRaQAnhgYtqejMNWXNmQkBT5mrKqNQ0NB3CVLjNARnUo_kzhLZePRb9VZbVkA32k9J8Xsmm5NRcLgQczaK4XSIaK-OXXvRE6Z4nNTbXkykxlNB6dJZYuORhEXstKbpTwdOPGlCW07ejM6obYnLmKNLAbjWD4XP_LZRNNrb0NNyZzDC6SZsdC9ozCygJCYE0J5paBu7OxF3mL8sp-2fuq8_mmyCtAlO9PFYLOn8RT9M2CxiTfFJc9IKDm4Vccje59RAmzi4v15S_o1ad2wCzwVC8NiaQPutUSUgm-3P0kRwAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ برای شرکت در نشست ناتو وارد ترکیه شد
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/447872" target="_blank">📅 14:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447870">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff6481e194.mp4?token=FLZVXlA7Gi0NW3HCARSryjNOnYykskUO8RRORMw8-KhlCNxJhIxF7Z5oxffcaodJGfQhMJb-DeHV838DbhzN7S2LkcPaqtnp_ZpFHwTw388siMtzqWSpajJxUVnr1RagzAYa_grKORkR4mjCJK6zir79QZ6fCkEoR16hmOVe7wKLlxvaFb6K38_J8TYqQcr50olwfM3StQ0dYW3tMELYdSrUoiUhl36-h7VrGNn96L0UUfHC5uImYIRHYcSmDjYxnjBOrgsrFrv0P4_YaL0OA8x7iFtxbbhRoTerwU_05EgJUHiPeauvXwiLiMpGPpZsO-4YKC-C8Nssqnx7pd2yfF2nXFsqf_o5vlaw0bEn_UPL66Q-zlTAbV8zufT5s8dL-xlwG13SybPwKJU9DyzxYSmpuZELVVajlV4nUIuTR_87dIBp4A2np590jBwAt8UM-BLCZtUoCAW1zXaCsrDKgVAyLMkee7LJv_9yWh_iPUNLmHPeNeXP8lHVzRCyh7W8127HjXzFdevIwxhMU5Ay4AIIAwucFjIX3FT7Va_v4UfQ5c1zC1dbAWBZpklrDaYARvKDQ0vOw4uFiB-3tdl6QHkv_niY-sN0vFrz70KU5naq-PvRN7Wove9tpp9KmRT4fi8GS8rlgrU7M6f-c8qdg35KwtiYgQUrvqitudSpETA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff6481e194.mp4?token=FLZVXlA7Gi0NW3HCARSryjNOnYykskUO8RRORMw8-KhlCNxJhIxF7Z5oxffcaodJGfQhMJb-DeHV838DbhzN7S2LkcPaqtnp_ZpFHwTw388siMtzqWSpajJxUVnr1RagzAYa_grKORkR4mjCJK6zir79QZ6fCkEoR16hmOVe7wKLlxvaFb6K38_J8TYqQcr50olwfM3StQ0dYW3tMELYdSrUoiUhl36-h7VrGNn96L0UUfHC5uImYIRHYcSmDjYxnjBOrgsrFrv0P4_YaL0OA8x7iFtxbbhRoTerwU_05EgJUHiPeauvXwiLiMpGPpZsO-4YKC-C8Nssqnx7pd2yfF2nXFsqf_o5vlaw0bEn_UPL66Q-zlTAbV8zufT5s8dL-xlwG13SybPwKJU9DyzxYSmpuZELVVajlV4nUIuTR_87dIBp4A2np590jBwAt8UM-BLCZtUoCAW1zXaCsrDKgVAyLMkee7LJv_9yWh_iPUNLmHPeNeXP8lHVzRCyh7W8127HjXzFdevIwxhMU5Ay4AIIAwucFjIX3FT7Va_v4UfQ5c1zC1dbAWBZpklrDaYARvKDQ0vOw4uFiB-3tdl6QHkv_niY-sN0vFrz70KU5naq-PvRN7Wove9tpp9KmRT4fi8GS8rlgrU7M6f-c8qdg35KwtiYgQUrvqitudSpETA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک محله در مشهد برای تشییع رهبر شهید پای‌کار اسکان زائران آمد
🔹
در آستانۀ مراسم تشییع رهبر شهید در مشهد، اهالی شهرک شهید رجایی با راه‌اندازی پویشی خودجوش، برای میزبانی از زائران پای‌کار آمدند.
🔹
ساکنان این محله تاکنون بیش از ۳۰۰ پتو و دیگر اقلام مورد نیاز را برای تجهیز محل‌های اسکان زائران جمع‌آوری کرده‌اند تا سهمی در میزبانی شایسته از شرکت‌کنندگان در این مراسم بزرگ داشته باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/447870" target="_blank">📅 14:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447869">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فرودگاه بوشهر از شنبه بازگشایی می‌شود
🔹
مدیرکل فرودگاه‌های بوشهر: نخستین پرواز فرودگاه بوشهر پس از وقفهٔ ۴ ماهه روز شنبه توسط شرکت هواپیمایی ساها انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/447869" target="_blank">📅 14:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447868">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مازندران فردا تعطیل شد
🔹
استاندار مازندران:‌ در راستای تسهیل تردد زائران برای حضور گسترده در تشییع رهبر شهید، کلیهٔ ادارات، دستگاه‌های اجرایی، مراکز آموزشی و دانشگاه‌های استان به استثنای شعب بانک‌ها و دستگاه‌های خدمات‌رسان فردا تعطیل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/447868" target="_blank">📅 13:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447867">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مسیر نهایی تشییع رهبر شهید در مشهد اعلام شد
🔹
استاندار خراسان‌رضوی: مسیر نهایی تشییع رهبر شهید در مشهد از خیابان امام رضا به‌سمت حرم مطهر است؛ نماز در حرم مطهر برگزار می‌شود و خیابان‌های شمالی هم محدودهٔ نماز هستند. @Farsna - Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/447867" target="_blank">📅 13:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447866">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab6b053ed6.mp4?token=TPiH2RCk0C4lRqrhPV688aolRQyb8twCUUcY7FhkW9RU9hksKuVWWOqm21G0l_fax2Pp2jH7CGFZT9Dzs46QmYOElimd_d3LbAQ3LqwMKNJg1SlqWWxAG_UpyReKeF7TQb-z3fMCfXngSQ9-ZcUeOUzRbcCey7sieaZnO63EPhqmqwKtSMALKwmcW9gx7P8XWvlHrWD0n_qL-pEJz--wi7hXctU4kwUnTPCQVAJ2oc_XwCg4eACcPxNn1evYvPuO4h7EQ2snfRNhoOsigYTllP4_P46_lZcuqhKyyO0F_xSl_0BXt3O5u8xo2DhHunsJCE25HDmBUAI6MTKAC6JKhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab6b053ed6.mp4?token=TPiH2RCk0C4lRqrhPV688aolRQyb8twCUUcY7FhkW9RU9hksKuVWWOqm21G0l_fax2Pp2jH7CGFZT9Dzs46QmYOElimd_d3LbAQ3LqwMKNJg1SlqWWxAG_UpyReKeF7TQb-z3fMCfXngSQ9-ZcUeOUzRbcCey7sieaZnO63EPhqmqwKtSMALKwmcW9gx7P8XWvlHrWD0n_qL-pEJz--wi7hXctU4kwUnTPCQVAJ2oc_XwCg4eACcPxNn1evYvPuO4h7EQ2snfRNhoOsigYTllP4_P46_lZcuqhKyyO0F_xSl_0BXt3O5u8xo2DhHunsJCE25HDmBUAI6MTKAC6JKhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از مصلای امام خمینی تا حرم امیرالمؤمنین(ع)  @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/447866" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447865">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مسیر نهایی تشییع رهبر شهید در مشهد اعلام شد
🔹
استاندار خراسان‌رضوی: مسیر نهایی تشییع رهبر شهید در مشهد از خیابان امام رضا به‌سمت حرم مطهر است؛ نماز در حرم مطهر برگزار می‌شود و خیابان‌های شمالی هم محدودهٔ نماز هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/447865" target="_blank">📅 13:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447864">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00d8f2f20f.mp4?token=YC7zUisd8cauekuwSE3JN7GpwZNYxzD_ZQ19la4l4vbgU9F5EHzzqjSTmMfVuBj3AmqSKSex2HESA0_DTj08P3BLSLiyEBNOraZ7RxfBALW3uLiUe73e9UA30uH5fKRvG2ZNf-abtLb_yKqUJt6IoIaSHTPFiEOlMekfxEwAkxxPysJWuVG6dI9MYS4lF8qTKQDliN85HmAb7pTI13Otgg8QAFiZvC9hmAK8Bd7LsKqmJ1hXXfQZOlb7_Oy5iPSc-fNi32Xk28pUmPH36rWNBTHWzIg31P-hc0xckYurKf9aQkBl2EWQ096uCHEfHhkBEn3Qx9CMCtLgG6YzbDr5eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00d8f2f20f.mp4?token=YC7zUisd8cauekuwSE3JN7GpwZNYxzD_ZQ19la4l4vbgU9F5EHzzqjSTmMfVuBj3AmqSKSex2HESA0_DTj08P3BLSLiyEBNOraZ7RxfBALW3uLiUe73e9UA30uH5fKRvG2ZNf-abtLb_yKqUJt6IoIaSHTPFiEOlMekfxEwAkxxPysJWuVG6dI9MYS4lF8qTKQDliN85HmAb7pTI13Otgg8QAFiZvC9hmAK8Bd7LsKqmJ1hXXfQZOlb7_Oy5iPSc-fNi32Xk28pUmPH36rWNBTHWzIg31P-hc0xckYurKf9aQkBl2EWQ096uCHEfHhkBEn3Qx9CMCtLgG6YzbDr5eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از مصلای امام خمینی تا حرم امیرالمؤمنین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/447864" target="_blank">📅 13:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447863">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5VlnQ-RAEAMWh8dghEYU5WK3bwzZ-eIOdMSOk297dvIcPH1w7Y7aCujpRyL8p_W_S80uP2UzNankx3GuhiRFtBymjq0zsjqCpzsH9GVVl2X-uSktVShWvaX7iMK8BYOFailRY4uOnVE-FVxG5rqP2Djzgqa-9se6y5qwH05z0rZeNHD7JvYrckak-pz2XY78Xw4hqL3ptKxDX57Mq98Akg30oMzn6Sj9_VlAwGrAhJ81sjleJ5vUjrmhPNYULjRlttA-LKNRGzyRvCje_wTWuavmxGY6-eFehPGOj0FHRR25OOObyAclV7gcCWKQjWuawvWHnuhFLisEQlsQFEnqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار قاآنی: تشییع بی‌نظیر پیکر مطهر امام شهیدمان در عراق خط سرخ خون‌خواهی را پررنگ‌تر خواهد ساخت
🔹
فرمانده نیروی قدس سپاه: مطالبه تشییع رهبر شهید انقلاب اسلامی و برنامه‌ریزی گسترده برای این واقعه تاریخی توسط دولت و ملت عراق، عمق پیوند معنوی دو ملت بزرگ عراق و ایران را به همه جهانیان نشان می‌دهد.
🔹
حمایت مقام معظم رهبری شهید از مردم بزرگ عراق و به میدان آمدن مرجعیت عزیز باعث نبرد شهید سلیمانی در کنار جوانان فداکار عراق با داعش و آمریکای متجاوز شد تا اینکه ترامپ جنایتکار قهرمان دو ملت را به همراه فرمانده عالی مقام حشد الشعبی  ابومهدی المهندس به شهادت رساند.
🔹
تشییع بی‌نظیر پیکر مطهر امام شهیدمان در عراق به مانند تشییع با عظمت شهیدان سلیمانی و ابومهدی، مشت های در هم گره شده دو ملت دربرابر فتنه های آمریکایی را محکم‌تر و خط سرخ خونخواهی را پررنگ‌تر خواهد ساخت.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/447863" target="_blank">📅 13:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447862">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ادارات گلستان فردا تعطیل شد
🔹
استانداری گلستان: در راستای تسهیل شرایط حضور اقشار مختلف مردم در تشییع پیکر رهبر شهید انقلاب در مشهد، فعالیت دستگاه‌های اجرایی و ادارات استان فردا تعطیل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/447862" target="_blank">📅 13:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447861">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f7a5dc84.mp4?token=h-Cf1P5cqjiDwj-yBWRxdBIQ2IqDM5CBt4Q9A-S4axdElSpPN6TWxDtUdSHDXD7_Ksr21M9UrzuX9Hi1OrNzCo0sDCNiZESZEVdEA7AJq1sY11GWcxcSW7fMDVk7DwIjceExo6e8MVLGedV0SQnbFvJVTUWa5_NQkeokjDPDkiqT-1ksmCj81n_2tnGTopUi-0Utp0WfPkOfNdUXSsQIGeNRDwEdxLG-BbFuy9ezqNUVYekES_VaX6O-ci27pIudGY6yprR032MXfxhMJcYfhhI3aTe4dw0r8slfqGhEnmau9rWfquemPn9XhA6zi1y1dX5_T3PLUMhkxAr9kQHiZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f7a5dc84.mp4?token=h-Cf1P5cqjiDwj-yBWRxdBIQ2IqDM5CBt4Q9A-S4axdElSpPN6TWxDtUdSHDXD7_Ksr21M9UrzuX9Hi1OrNzCo0sDCNiZESZEVdEA7AJq1sY11GWcxcSW7fMDVk7DwIjceExo6e8MVLGedV0SQnbFvJVTUWa5_NQkeokjDPDkiqT-1ksmCj81n_2tnGTopUi-0Utp0WfPkOfNdUXSsQIGeNRDwEdxLG-BbFuy9ezqNUVYekES_VaX6O-ci27pIudGY6yprR032MXfxhMJcYfhhI3aTe4dw0r8slfqGhEnmau9rWfquemPn9XhA6zi1y1dX5_T3PLUMhkxAr9kQHiZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چند قاب از آماده‌شدن نجف برای استقبال از قائد شهید امت
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/447861" target="_blank">📅 12:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447860">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPXnYlZEQju--aC4FCbQAVxn_w0fPhjxs4Q9_mP_kj7ZhrM0EdUmTGPaazahFJIHEjLqVkcTxsjI4fqrc2be9Lxy2DjVXxivyvxsQxWcUy4rExolI-pNVgyXi6GkCEH730dvhe3aj9bndzwgz0XFONhNEntT24JUMCy4hK7VdKLiNnrDdApVF0YeWz0Q_T5Lr3DqW7T7EfFZxkSr3yaPVsbqxD2X5PfAA4j4TtA9WQ7yQDrkFtlQ1l8ZbT4yLzSNODvAyXYgwR5tLsAwSIrz2_m3Ex7EWUBN-j1Y4HjIoNmW6RxMQrvxZk1jVQOf9W49IlmvSUfKIEnF6ITOhkMcmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهش تاریخی بورس پس‌از بازگشایی بازار
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۲۴ هزار واحدی به ۵ میلیون و ۳۱۲ هزار واحد رسید و رکورد تاریخی جدیدی را ثبت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/447860" target="_blank">📅 12:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447859">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bc49333c2.mp4?token=vEQz2xKfsmouFZlu-aVBjpxMTOfzD29HllfhvC-eLe-4Kx_qTW5avFEZi1Rh2mHwHGGSMYIqevPWaHS7shuqwPTtQs_XcRJjsYrb6czDyJqmg7Ry5APyPtSvpKgSZp_bTnfr3xCY5ln9L5A7WL4C66Sjt_A71TmB2-QKygcRDylELk43Q5BUzYWZBl348Z6SUyUvVuEhKjN0P3HquKVxMXzKzcLDMYgo0fndz3JJ7XCGNW3svnF9x4xaN91yyjxwji118bXMjagSRsjl2YJEdEkCbQArIwhCfApCgrPfiqgXtgYj_9AFOzMp7zxG8Tr4INu3QiaR_Fd57QK7qbUFzkLEFVkYl-oPIJSPXA6w8DRH4SPi4UwTxuKTXI0-aPR3iAKUiTCAEwq4ib8Um3QJpALIdI_kZNRFUjQho5flgypH0PR4P_GdhGBsmzznooIaLLs0zYbNcu2FC1CbPueUjPTP6j5aDFONUCVYFAsfUIJ_QrVEp9ld-9pN3T4A3xtpQH2Z3fptwyA9Dx4ordZDld-JXaBc1JAbmO6AmS-OTb6Gtea-3Cmk-VV46fRfJ4iCw6yj_wWMxc867Iibl0mLQm0Neefknd5wDL_TjfGtHRv_i5GlltOtPprVE3iy-SJma2XWLrNQpHgzQMut87ep9qbW8Cv2OOUC7nH3qnf5Eeo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bc49333c2.mp4?token=vEQz2xKfsmouFZlu-aVBjpxMTOfzD29HllfhvC-eLe-4Kx_qTW5avFEZi1Rh2mHwHGGSMYIqevPWaHS7shuqwPTtQs_XcRJjsYrb6czDyJqmg7Ry5APyPtSvpKgSZp_bTnfr3xCY5ln9L5A7WL4C66Sjt_A71TmB2-QKygcRDylELk43Q5BUzYWZBl348Z6SUyUvVuEhKjN0P3HquKVxMXzKzcLDMYgo0fndz3JJ7XCGNW3svnF9x4xaN91yyjxwji118bXMjagSRsjl2YJEdEkCbQArIwhCfApCgrPfiqgXtgYj_9AFOzMp7zxG8Tr4INu3QiaR_Fd57QK7qbUFzkLEFVkYl-oPIJSPXA6w8DRH4SPi4UwTxuKTXI0-aPR3iAKUiTCAEwq4ib8Um3QJpALIdI_kZNRFUjQho5flgypH0PR4P_GdhGBsmzznooIaLLs0zYbNcu2FC1CbPueUjPTP6j5aDFONUCVYFAsfUIJ_QrVEp9ld-9pN3T4A3xtpQH2Z3fptwyA9Dx4ordZDld-JXaBc1JAbmO6AmS-OTb6Gtea-3Cmk-VV46fRfJ4iCw6yj_wWMxc867Iibl0mLQm0Neefknd5wDL_TjfGtHRv_i5GlltOtPprVE3iy-SJma2XWLrNQpHgzQMut87ep9qbW8Cv2OOUC7nH3qnf5Eeo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با خروج خودروی حامل پیکرهای مطهر از بزرگراه پیامبر اعظم، قم برای همیشه با شهید خامنه‌ای وداع کرد
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/447859" target="_blank">📅 12:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447852">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XpYlX8dVhGGu8oXRCk6P0QWWIEpSpgtkPaf2WqMs-sVGfOCb5Xzxmq0sZtZYZBssYWp7XcNyVMPbEzvnzOwGBkKWStQWXWkS2ZjN9Y2ptf5g7bI3gz0QL2WKuUuUNmhsg3ymD4C8F2pGdxbk833PQG672rsV3IBdQPlNxQsGCG5NuWPQSF7Zxn9wx53fy6pRQ2ppJjP6h0FfbyeMOLagQDSl0WcuKyThUoSb31BhSyStsaq43_DomAtMMoFmlmkNSCBAvORUvCs8Sj9OPbDXyrcKtMRVUWLXcN57u4scP19f1rEAZMrE2NzpKSNBlAoC9OLpHk1ayeyXzuN4QmOnYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rNvvDJIOGzwlQsERgZ00DgTqw5xZQUNO4M_H8A9m48cyZmT9ybZPLxwbUfDG04M50MOKlNSxG0rCOoYrdG7nD-h_iuyoeaB8PbuEyUi6PLeGR7mQQrO_2_XPaUqeWAt2-2Wv1SKemR4WangVcxbz0Pd-C1sTK3ngpnCYSNTLQbcYRsaybzZitzRU8HZsYahrpU_4K2aWSvbBF8tnpVng1cHdyfLXhUGPGPq3TT5A21cAQk4tJsvsL8JNKTcficZuI2C07_-DAGEv15BMXfW2O9adSYSDANia8c2p-me3a1OtAln3AYk8BMtajiAqKr3hEipdZe1yyAq39pxBiFCKKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RdawiFAi_nFLoRclCsofdjimQDvd5XKaMfRh0HocVW2E3YVoYiAQzhSZvVCF-3D0yMxwg8NGkSvnn2fFmAOYAqmZyMN3qtVk38Gy3b-oL60--7ZMNbeCJ6vx5_WL_zKFqL2ZOIOLbF41prhoVA2e3parOzn3vrn-3s09Z8uRf1nFRke0shzlhRRDfkhvT_798TBtSaKpv4jdSrRCeeFQAyKDFF8UwxF_MgIpy1aYeC9EMLM9-34_-Ab-Ng_PyCDyHj71qgBv6Vuj5L9kLJftc63-Miwd1oOUgZhZU6fML6UnXM1cXV9m9--kOGMFAFxhG1gwUeAZ-nMvhWyfiXt9cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rbwzMDTLLR0vT3hdRFccr0-zhh3qMx2bxc0GD9kmURWBrhxWbOGJBGUA-6MuiI4Th8saym6byYKiRiIv_UPOZcJW4rlo4OExW7rZehJNJl2nbVyuho3KqyPXE3Q0A5ilyosEW_aIjTCsMUkEhI8v0J37xyTF1W8rZ5FBJMJSRWSbpFhIRHXNajbk6N11jmGFxbXo9gfAVnMwFMz0JjNTT08uuPetc4LEh8gByJ8wAMR5TLhYfUiL2GEEYRQQh6XNj4i_WT3iDgkOGpc6z_4VAWLkl8sx21XYmXap64-8Tz7rQ5JguQvhhlg6b9KDe7qLdE7jBcgeh_xzQSH2uUU9pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hYk_doX0K7ct1TREax65e1DDmijLoXBkd70-GDlecOMe5E4kNQ5pHm5SQKw9Wdp52v8EnlJzpiSNkgi9eQ-FS_0e7QzLSgHqO29cPmJQp57rRw3K5xMtf0FYJUqnYMceeYDKbEJiEMZhJFaMeuYQVq_2jz-3R7dWlPJDLyyX4mjyEb9_hqHZxf3HKyIGzuv-lzhj735jQtWGlBDfCFs9-dE2F_c8clpaYUEV7xpV1yH_wMPYxlA-poJXYnelcFGIMOh0SBHkhe1Jjogsc3CQu1hHlHFiEHVjgHoQCrO9qPKJB30gmFEKqbY8PYGE_T0rOv0kYy6TtX2lhmQqC7lFuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/na4n_R1P3bkAE_-5rxMs50fsTXNDj4Yo7j6baoErDeZ5fYKFSdf_-tQ16EaDkOAaunjmJOkdAt_-oUQsSE96TKndAQKiqwgztZYyySOSd-AFnKeMWRrDyVh6vqmQAG0LuD5VNC2ZkzBildw271k71K-KbKk2qLhI8zdpFznYcvweCDFE48MBxW0-4EaflE_ljnxGQjFoyOig-N5cWyzv9ESNHtKYLFHwbyXH-CEzAk-6YVbFBD7U7k0UtUSHAMsrz6mtBpJ7dwGU1dwlJsceFqc1EgfyrW07Y-2z8eV4YseZyv6dyW1WqW3lr4XCBgGvJqDx6lqvgjfEwccbtQAlwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZU5l36AEtsRnmFrcO27QnMrP9xFTksiSb0M-U8j_VZqfJ0rCsPDCe-ta45ImStagB6WamDJfBI_fFtMl09I6HPqjUoeduw5bgesQ68GKnhlXFe8BMEQbqW620MzDVQSdEJT3sqiIaVSEecZnPUi6JmDVOPtAP9_5szJRFPUx2nj1KvplRiVpDL-KAK_Y903skRJoRCOJ3CoWOZmEGJxuA3eg_P8xxbdPmBzRD7qw__eaSXyw1pa8QrFtGjP_3VpL8jIy_st7LgErP7bkHagb5K50uoGDjZc_zVx8CEenxbgSv_enIZx0X3eAZBXNtEc93pvdPMtxN8db5E3rb5Tguw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تشییع پرشکوه پیکر پاک رهبر شهید در قم
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/447852" target="_blank">📅 12:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447850">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53eddbf811.mp4?token=Y2zP3vINBip3FlkVDhpvtW6JXsFgZBlTV-ZWvmCImBE7BCBgkVvDJaewEMTQW1Lv9fBfkbgm7vvOiOrdkzBp2iuChAV0-3iufD7ZWtJDukdgbnVpSxW312b9JOl9LLoIgn1n5yKpNO0QwQi9uKQe_tupoEPcGn_gRgOpn6Eni4d6vkeQyPUgkzQ6NTPUcaCJ8IH22XI-tt-nn2YmK13rniQTFf2u5YBvlFS9Mz_Cjge8qiYlc7HX-ECJWSksID9QSUfnn3v5IStdUe1hvGHrayO-eTFOJUjUT9xSNbzfzVRN43MVoeF4iKxsWfxYb1eosA8ePsf2Iapd6JvWgqYq9SbfCqhdWzll9GgUiRVEBSJi01TmLlXGLZDdEytrUR7d35UElEYHXsYI953uL3TTSHkbl03nqJInGSw6DXBYHIEf-eGW7-flV0oBOt_sberC4OqQDGZv6fQa0cIFh-aOMXUg_YEfGN_2zP78BO8N4DHlgWwwtXoVbVZZBveqGxywtFAlp6mR1Dr6kp3cq7JBkNsFw5FUPMKC2XqYP6cFkMzawG8RtGHeb9urP1zFac9zgY44J2hCCHEYap19UDeuhfVd4VLH9LkF_Mwh08CEi7RQNgf5OrCUUVvDoVMyi3p2xYLwSYAZW1fRIRmi4qTRes1OFaT9b5iGl8O4mFbda_E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53eddbf811.mp4?token=Y2zP3vINBip3FlkVDhpvtW6JXsFgZBlTV-ZWvmCImBE7BCBgkVvDJaewEMTQW1Lv9fBfkbgm7vvOiOrdkzBp2iuChAV0-3iufD7ZWtJDukdgbnVpSxW312b9JOl9LLoIgn1n5yKpNO0QwQi9uKQe_tupoEPcGn_gRgOpn6Eni4d6vkeQyPUgkzQ6NTPUcaCJ8IH22XI-tt-nn2YmK13rniQTFf2u5YBvlFS9Mz_Cjge8qiYlc7HX-ECJWSksID9QSUfnn3v5IStdUe1hvGHrayO-eTFOJUjUT9xSNbzfzVRN43MVoeF4iKxsWfxYb1eosA8ePsf2Iapd6JvWgqYq9SbfCqhdWzll9GgUiRVEBSJi01TmLlXGLZDdEytrUR7d35UElEYHXsYI953uL3TTSHkbl03nqJInGSw6DXBYHIEf-eGW7-flV0oBOt_sberC4OqQDGZv6fQa0cIFh-aOMXUg_YEfGN_2zP78BO8N4DHlgWwwtXoVbVZZBveqGxywtFAlp6mR1Dr6kp3cq7JBkNsFw5FUPMKC2XqYP6cFkMzawG8RtGHeb9urP1zFac9zgY44J2hCCHEYap19UDeuhfVd4VLH9LkF_Mwh08CEi7RQNgf5OrCUUVvDoVMyi3p2xYLwSYAZW1fRIRmi4qTRes1OFaT9b5iGl8O4mFbda_E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای زائران قم در بدرقهٔ آقای شهید ایران
🔸
از مسجد مقدس جمکران تا حرم حضرت معصومه(س) ۱۰۰ عمود وجود دارد که تاکنون پس‌از ساعت‌ها حدودا دوسوم مسیر طی شده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/447850" target="_blank">📅 12:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447843">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qT4sKYi5NmU2mblSIu4_lCMYS_vIAqnNNz_BfA1-Ki4-S0255u2_pDdICtJM6Rj9eGt3oKEaPk6jqV4IKruoptuwSKfXIFYBcAz-ZE2vEdsUETvChCFjEvTvX25v5jeDgUZEv9nNh2f8xAbfBSm7TMe-vS_C76zJB0mT-5rcw8ECsLcI4LOgELkBovxN8Sd7R3tuDND-irhXyaHV0vomnqBvkxxGVsVyi12m1OoTtdbXm1K6NBLmPAuYc27yROXNZOLamo50iuBu3V1p9QAH2B7T0y-tjoAdZaZTmE2Bl07nllqAEsI6eZSf2Mw0Z0m6CmSq8llA7lrcwBCbWCS74w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YXb78PU7FIdPch-QiTMmrJLTgqUzCBKoZSHKRRYlzjRecPpqlEhrWW_dWeRvhdLSqVTwYzWWbyJ3u2Xxp3GCrLtIb20NnF-CNs3zNVGK2UU9bhMC-PtGpVajKBRtV68iFdE5mdj1YbiXHagh5AoJUtLi33OZ0kVM78cWRZ4xK5UEDL0PvN4d_WZGVOiDvISI__zTNdoJdyZwra2s1rOEDuKlYjN75OW126GFheIyVwbO5uLcNcNyCOE7KWjFnOPXqsM4tSIWasGJNcUifaFZK3aPJ1XvJEWmTw8TZT_WxgDKELxMcowxxsdK7zsIxr4rO-ZIp0x6Z9pUBgz4TRVj0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PZGqGo2GMTSEzlfpfYgpuXH9Fsa9TUZLxUx_8pUTUx1pjLaINgbtR20Yk7j8brNcDRhTDnpr9jEt3LyHPqkL7TmM-OQRZz9G92HdTgFvi-tQeYzKLidfdBL1uCyXdv2DlA_qFuyv6fk3Fbnklw49bzO9StoU-9qDiYDyiRSTcLyjtRILJR77W9KMzyoQE2eNwjgcXOIG1rnPBft6cY6sqCsehfXyPlSnjsAKfzDBPSK3YyNVpgbh8-8_LbVLQ3P-BqAvSRgrYuPH8UiUhT7i2Uo7wdFpa75eNuEGnW6xnOE6ol5ccw5u4OovkyQRDR4fVR7_qMJS-IYSnAp8k6NvsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R4Cxa_CeYGUtIX1eEmV7nbCtdu7zPtSMzVx5qhnJnogxGwqdMkYCgNSMMjI-zYbxJ1v2z9Kd_yZ8-GxdUoHArlVaJQ38GNpXvnt2ZbcZX4b3kzEfRwr6uHj516byKGlwneaFpsjfkqKT7GQ9s8w0pLu4pXMOoCqgR9pWH7eT3p8KYed_rrHI-eRNrkmO8-iboduXYr2G1TbviTig3qSsj7dbw_PkpTG0cm9V1ZHz4LE-enP7oKoP62acFiM3BVhGJMrzXmFWiP3vVC5xmjgt_AdepnBU-oP5jc-sYY7J3xbihKTnhPNSkrb9ZdGm5td976IHVGNLVmlthupald9-vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hDnDExoxgY8V5LIk_YPCBe6NId0qDeUnoob9wvTsV9oul8ZdcnhY1SiacqNj7g-AzZ-XNoTfQmhZyEh0FwPPYrtqsXzbIltAqsJnIre3dSn5s29602M7J3trj252GdwsEK0ecSebPzcsc4or-QVlTusnRNxcBsrOTgKEW4MmMDnJ4FtOlqtqaDrvxMItaR9jzIZR3PC3JIPEehYaLv9X97YEKsm0uLH1o-JpkDESI3xpyO4cPViozdudB1pgq6RAQOwrhx5natOW6ulkeTgWhSjfLKHwrGnYk2FQ0RvZ54wmyCl81zzMoEEH8r65SBVaQ_aUYVB4lWj3aqbzYoS8-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h4um2z2-XU2HRMvC07q5iddeeHJKEeM075jplHtOdLIKD9JfH-KIFZ0xeg7HmEk9SJ0fUo1m4nEN_xlRb23vrE0H5oOIXgybnHe7SzL7lBrPse_8a0tYkwjhY4QCbh9qFW_Nvmc5a1w-W8Orq11pTh7_wxPqTMKpY-hmEvTs49EtB1mz9mGYKDqbKjt-UL8Yv81cZVUMJFK0TmTo6QBKYQRE1A6Bd7ArXwy6g8dsxi2-dG2DsBHNLDbJqO4idic8CxYX43P1Kg31tEpZUmhMa5gSCrjFaLL6fXx53bA5BUeJmp1Uwq16t9aUbm1peWL_mjNXgJWYjpFnsM-DWBq5xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pbvLfTRZl7TKuYdeB7pgaQ9ymJUSM3croaIhex9x8FcovYCf282V2FOGbp_X4tXx7QPFtsm5JQcRLVbV9G5gZ8BMT-kx_eZzPEvREaRx8LEd9sypUgjTaqtzXP6Ddk8WGGTW85z5tPo1qDWi2Pf5Q7nZ8HEepTnhw2jqRMCeLljPhSO64VqQ6yXhPl87P0hUO-qaEeic0aoPOXrcXOoD1VLhFoYd_ZRtbeeaTbYkuaG34gpQr-FqPixrxIlaVwE9I8X-L8yXTXLXLD6V4id7VAnZNT4h40Bmu917FjiKnELiP_SZvYibAmAHuU5VPLReUz5C_WOIlBHiDK8n9Zqkdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
نجف آمادۀ میزبانی از رهبر شهید انقلاب  @Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/447843" target="_blank">📅 11:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447842">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16a691fdee.mp4?token=Rq98JysMlEhTttCxuRHTvHK5zjGztZ2RrPWoL_ubT7RTKsukcrkVqOAx7ZlFKZq7DcvEbJJcxuZ6Pq-slLsBlx5AI_oNkld_1RRidowjSDX9Mfqn_sXcuURt42GtFpmI4jQdfX0MaPWmWKd8ThqogLAISkOEvXxtt8TwS4Pez9AaklcqBiqWqn3SKYu_tpwAfaQyIXObCm7JH4mIpBebCgb9JdA9BWlfciLh8JfA1FS07oLnRPw6BVcSqjWeIZ-hF5_NMAQkuWVbp1Nn98ZsYeJ0oeP7gZ-cvrFdzdgd-G9QG7TsDcHd9vp9ClUBYo10tUtxFvyry_8cP0GJefyeoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16a691fdee.mp4?token=Rq98JysMlEhTttCxuRHTvHK5zjGztZ2RrPWoL_ubT7RTKsukcrkVqOAx7ZlFKZq7DcvEbJJcxuZ6Pq-slLsBlx5AI_oNkld_1RRidowjSDX9Mfqn_sXcuURt42GtFpmI4jQdfX0MaPWmWKd8ThqogLAISkOEvXxtt8TwS4Pez9AaklcqBiqWqn3SKYu_tpwAfaQyIXObCm7JH4mIpBebCgb9JdA9BWlfciLh8JfA1FS07oLnRPw6BVcSqjWeIZ-hF5_NMAQkuWVbp1Nn98ZsYeJ0oeP7gZ-cvrFdzdgd-G9QG7TsDcHd9vp9ClUBYo10tUtxFvyry_8cP0GJefyeoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت ارامنه از کمک‌های رهبر شهید به کشورشان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/447842" target="_blank">📅 11:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447841">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dee4630bf4.mp4?token=DJ7zdaJvBnrSF3Tf-qNtNhqICLMf-r0dUBobIK0ijYAlTOJp3GZMsNOCBvNtCsIVBoncs1MhcP6eV4lOK-2ORU21hr_30nmAOTgibs652Amd5HKiZ5kPH7iUQwkNvAMEhBUJpQhIn_OOerlqQSzfDMvdaLuYdwa_DkVT5bhS9Z_Ak88jqYCpaaCn1RRS0kBFZKg7f8N7uUDWRXA5PuvbVaFcWlRGH3DlCzc0rHYpN2ajA3C7-iRMCzd_forgOoQ40mLXP68BqsocBXXjhOCtgoN-BQ1L7E0ofaoAffTKQVfe_3dud_WQoIDiC5wHzWTZTUKS_M4JWwBZ3z81gqpDZ7lYJRHqx6UQvXonRu8jC8gb7TtHSnTgLak-OS1zLs74d4IfgtrlUmnMG4IK0eBdQFe1RVfTNwmcOJUb7LlYpDX83xSDTAjXl9qo0VRxG8xGrpkq5BTVA1s8y4t9BsjWuXCc9pEycY3eMQX9KrAfRxrk5lixNUp2Da5449Yf0pI3jdJ1Nmlr_9mwv2y1A2S9jXEFqQkM6uQM3mRCMZdXclcXF5yrtC6Wzfk8Ff0TroIAIoRUVvKNuIukdpPb_gmc6Ey_si2n1m4k_1w9tq9Z0oeyIBEwmXie7VogUK4lmEhwPhqeU4XUwORX-XU9KWwaJ1PvKrs0vjhPOA7ZO_2to0M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dee4630bf4.mp4?token=DJ7zdaJvBnrSF3Tf-qNtNhqICLMf-r0dUBobIK0ijYAlTOJp3GZMsNOCBvNtCsIVBoncs1MhcP6eV4lOK-2ORU21hr_30nmAOTgibs652Amd5HKiZ5kPH7iUQwkNvAMEhBUJpQhIn_OOerlqQSzfDMvdaLuYdwa_DkVT5bhS9Z_Ak88jqYCpaaCn1RRS0kBFZKg7f8N7uUDWRXA5PuvbVaFcWlRGH3DlCzc0rHYpN2ajA3C7-iRMCzd_forgOoQ40mLXP68BqsocBXXjhOCtgoN-BQ1L7E0ofaoAffTKQVfe_3dud_WQoIDiC5wHzWTZTUKS_M4JWwBZ3z81gqpDZ7lYJRHqx6UQvXonRu8jC8gb7TtHSnTgLak-OS1zLs74d4IfgtrlUmnMG4IK0eBdQFe1RVfTNwmcOJUb7LlYpDX83xSDTAjXl9qo0VRxG8xGrpkq5BTVA1s8y4t9BsjWuXCc9pEycY3eMQX9KrAfRxrk5lixNUp2Da5449Yf0pI3jdJ1Nmlr_9mwv2y1A2S9jXEFqQkM6uQM3mRCMZdXclcXF5yrtC6Wzfk8Ff0TroIAIoRUVvKNuIukdpPb_gmc6Ey_si2n1m4k_1w9tq9Z0oeyIBEwmXie7VogUK4lmEhwPhqeU4XUwORX-XU9KWwaJ1PvKrs0vjhPOA7ZO_2to0M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی از اقامهٔ نماز آیت‌الله جوادی آملی بر پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/447841" target="_blank">📅 11:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447840">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🎥
پیکر آقای شهید در میان عاشقان بدرقه می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/447840" target="_blank">📅 11:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447839">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d28ec779a.mp4?token=HKpzPFvHJWBduuoHSi8yoxdOSBxjup8naOWJgsPIIDkjpmOf3c-DQxqaMo-WcG9gW_7e-U_C5FNKxow3RLporsqWB412JVR7H2sqmgwZLZwrUCVepRuKEjxO0VNuUOAyZ2wJBrHzCH_3IP5uH5PyFvuZCLuhFLuraKf1svuxOJ6Oq1uXWGGGXxDbZUZFksN2cDnabGMx4IG7nsUGJy_RZBHk_RAOHc6kgMIdfTeNSleROmAgJ0LJKBk9R60YlNjg-mXdzq057Q2pnPSgBpaq5xWJ_kTwamWj8ilHUtAPeDZJsrzYO7w82bFesBC7Us9SQkA_Vpy4oSAUDGZ7OJEvIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d28ec779a.mp4?token=HKpzPFvHJWBduuoHSi8yoxdOSBxjup8naOWJgsPIIDkjpmOf3c-DQxqaMo-WcG9gW_7e-U_C5FNKxow3RLporsqWB412JVR7H2sqmgwZLZwrUCVepRuKEjxO0VNuUOAyZ2wJBrHzCH_3IP5uH5PyFvuZCLuhFLuraKf1svuxOJ6Oq1uXWGGGXxDbZUZFksN2cDnabGMx4IG7nsUGJy_RZBHk_RAOHc6kgMIdfTeNSleROmAgJ0LJKBk9R60YlNjg-mXdzq057Q2pnPSgBpaq5xWJ_kTwamWj8ilHUtAPeDZJsrzYO7w82bFesBC7Us9SQkA_Vpy4oSAUDGZ7OJEvIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
رسانه‌های سوریه: صدای انفجار در نزدیکی هتل محل اقامت ماکرون در دمشق شنیده شد
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/447839" target="_blank">📅 11:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447838">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcl6vEAaEdHiKiuyl3zw1weSTVi5ONix5rruceZ9XcgoCzssIw3tAtuh6H_XWWe4TXtSa9kAchJS1VzQSqVRYXZtFr4Pk61ExDdrNW00ZW3HJ0mzG_kHrzr-rD2vyex6ib7ddsgOypgocHOYxRLszmeV9CvWImJ1W8QQRRsGTRPhFcwfY796xOpRVNmtPMDZNSsRKUBPuZMTv4iwDhnSDjeGVwn-0SQO1lbFvGI_p0-UBdYEIkOrcGd_aihHkG-30HThsi74VQM3tAsBIMmJCL8CRN6BowoullIQpJdN6cnzijxqVVSQ_s91rSatWkAA5FYXr1hq8z9q583ZMs5ycw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه اژه‌ای به رهبر معظم انقلاب در پاسخ به تمدید دوره ریاست خود بر دستگاه قضا
🔹
با عرض تسلیت مجدد شهادت حضرت اباعبدالله‌الحسین علیه‌السلام و یاران با وفای‌شان و همچنین شهادت امام شهیدمان و فرزندان و سایر بازماندگان آن عزیز سفر کرده به پیشگاه حضرت بقیةالله‌الاعظم روحی و ارواح العالمین له الفداء و به شما رهبر معظم انقلاب (حفظه‌الله‌تعالی) از حُسن اعتماد حضرت مستطابعالی و انتصاب مجدد اینجانب برای تصدی ریاست قوه قضائیه تشکر می‌کنم.
🔹
از خدای عزّ و جلّ و سرورمان حضرت صاحب‌الامر علیه‌السلام استمداد می‌طلبم و توفیق انجام این مسئولیت سنگین را خواهانم.
🔹
بـحول و قـوّه الهی تمام همّ و سعی خود را به کار خواهم برد تا به نـحـوه احسن مأموریت‌های محوله را به سرانجام برسانم و هدایت‌ها و توصیه‌ها و مطالبات امام شهیدمان و مطالب و نکات ارزشمند مناسبتی هفته قوه قضاییه سال جاری جنابعالی همواره سرلوحه کار خود و همکارانم خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/447838" target="_blank">📅 11:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447837">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55e320d8a2.mp4?token=ErmUg3fY6kXTI3CyniRJQVpGZDTvEP9VHlQUVHwupmr3koeXYNmIrYYOW3LZX-b8TAhtl8WyFFhs4MtY-4IeFDOAwurCpIQXdOBlGBETZ7SRRyCy-Gyzyg2KNfj3vP_r1NC1hnjtSjE2KmDeINXDVxGt-HsxTzFzJSz06npJpUNeV6E2NYKK2D8AZgxFLafW-mwCrkRgrlNfI6uQUsZd1ltiuvWAd-O3epm9UvaeaRHn8tkOkLIjL_Wp_Knza7y7FEnYHMMJK2XBPSkpCbft3qsqw1MdHehxBb2UnExlVf62vwZYYci3YHsH4TzCLvxq2dE0UYHvKCVAe02xTOzC2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55e320d8a2.mp4?token=ErmUg3fY6kXTI3CyniRJQVpGZDTvEP9VHlQUVHwupmr3koeXYNmIrYYOW3LZX-b8TAhtl8WyFFhs4MtY-4IeFDOAwurCpIQXdOBlGBETZ7SRRyCy-Gyzyg2KNfj3vP_r1NC1hnjtSjE2KmDeINXDVxGt-HsxTzFzJSz06npJpUNeV6E2NYKK2D8AZgxFLafW-mwCrkRgrlNfI6uQUsZd1ltiuvWAd-O3epm9UvaeaRHn8tkOkLIjL_Wp_Knza7y7FEnYHMMJK2XBPSkpCbft3qsqw1MdHehxBb2UnExlVf62vwZYYci3YHsH4TzCLvxq2dE0UYHvKCVAe02xTOzC2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کربلا آمادهٔ میزبانی از قائد شهید امت می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/447837" target="_blank">📅 11:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447836">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67aa8dde97.mp4?token=jEZqSVx6yOnqr-YaSzfYg7A6kNHpAbmPzSig5stwHoxvJg9cW754QgOkoG5s_a-zu22qPYDra4zaq-AkoSU3xGrQkcDHylzWQQVxabGbUDn3LF1Bt2xqrLPWRJ7rIMFvAYgDaJvNBBt-HxzYqej10ArJS3TZjOXzlrXis6cnYSiFupIK_j-aUQsnQn1VmzDwx5u80vVVBgCp6B580WG1pwsZeDkX8A4lbLKf4eX7q6G9xz88MhW-GhX9lUrGy88DrW8dB7xx8vlDimr3-yk-DpVPNYLJe0nAjbPsQII89BGC-jcajFOYh85Kutb7U2MvD22FE49LVgPXofCejH3VcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67aa8dde97.mp4?token=jEZqSVx6yOnqr-YaSzfYg7A6kNHpAbmPzSig5stwHoxvJg9cW754QgOkoG5s_a-zu22qPYDra4zaq-AkoSU3xGrQkcDHylzWQQVxabGbUDn3LF1Bt2xqrLPWRJ7rIMFvAYgDaJvNBBt-HxzYqej10ArJS3TZjOXzlrXis6cnYSiFupIK_j-aUQsnQn1VmzDwx5u80vVVBgCp6B580WG1pwsZeDkX8A4lbLKf4eX7q6G9xz88MhW-GhX9lUrGy88DrW8dB7xx8vlDimr3-yk-DpVPNYLJe0nAjbPsQII89BGC-jcajFOYh85Kutb7U2MvD22FE49LVgPXofCejH3VcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروش وصف‌ناپذیر مردم قم در آخرین وداع با امام شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/447836" target="_blank">📅 10:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447835">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">شرکت راه‌آهن: فروش بلیت قطارهای فوق‌العاده برای تشییع پیکر رهبر شهید انقلاب در مسیر تهران-مشهد و بالعکس از ساعت ۱۷ امروز آغاز می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/447835" target="_blank">📅 10:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447834">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43325970c0.mp4?token=f0DVVfPVJm-Zh1U2_W1yp1dp9DDAz-2XyuQHZz2ILQPtCsh_gRwEkDETnUQJoLdyhSQA0NW1-aPcIXlNxGF9e0OrBNDSQjTS14-53F4zq-PLKn4EfWPRWPNUnZ6aT2fwskn1UW-kxUgvvqApNPw1-N35R7brEnuti8yVbmSgwhNFWFymuBqG88ANGWl9f3aG9PAl5ouh56Px8KPCyBdxs7r7v-5dejePIOIe9VyGXDTumVnYSlX6_9RWrQTmijmH4aqlXKbrPxcHlllzuhufSxkOEgQ_e38KiE34Dx6soSRNlXDKtJTdxXhHXY9Oqwq9fDEUA1vXenGKYcXLxSiHUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43325970c0.mp4?token=f0DVVfPVJm-Zh1U2_W1yp1dp9DDAz-2XyuQHZz2ILQPtCsh_gRwEkDETnUQJoLdyhSQA0NW1-aPcIXlNxGF9e0OrBNDSQjTS14-53F4zq-PLKn4EfWPRWPNUnZ6aT2fwskn1UW-kxUgvvqApNPw1-N35R7brEnuti8yVbmSgwhNFWFymuBqG88ANGWl9f3aG9PAl5ouh56Px8KPCyBdxs7r7v-5dejePIOIe9VyGXDTumVnYSlX6_9RWrQTmijmH4aqlXKbrPxcHlllzuhufSxkOEgQ_e38KiE34Dx6soSRNlXDKtJTdxXhHXY9Oqwq9fDEUA1vXenGKYcXLxSiHUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نجف آمادۀ میزبانی از رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/447834" target="_blank">📅 10:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447833">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86162004cb.mp4?token=Or_dQa_PjYqXwG2FOQa70nWSL8TzQ1nM8fHuSy0L4M-f4PscAFnlRc6isFqxo9Y2kZpa56HSCu0VfTEVk5oIN9wR4LkvxRpPVi3N_JLVUahSoBo5pqk0CgNDQc6ZMGNvxsBrCmNS59JeXjYF3roN4dNgxxluBNBxL8Ofppzrnzs6NU8q7E8QFz-knUJGKLERD0bV0Amy9O2bNt0IExa0XFOwyiQ-R8ktzKJS71Q1TOLHkOM7zRWsVPDgGigSwlS7E9viGwNXh-i3ctCK43lDu8iaxF8cvGlAbcO-CnVdq_jxnnfGz5x0a20nsJHAb-NeOYv4QwbtINxuKNAjWPcyZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86162004cb.mp4?token=Or_dQa_PjYqXwG2FOQa70nWSL8TzQ1nM8fHuSy0L4M-f4PscAFnlRc6isFqxo9Y2kZpa56HSCu0VfTEVk5oIN9wR4LkvxRpPVi3N_JLVUahSoBo5pqk0CgNDQc6ZMGNvxsBrCmNS59JeXjYF3roN4dNgxxluBNBxL8Ofppzrnzs6NU8q7E8QFz-knUJGKLERD0bV0Amy9O2bNt0IExa0XFOwyiQ-R8ktzKJS71Q1TOLHkOM7zRWsVPDgGigSwlS7E9viGwNXh-i3ctCK43lDu8iaxF8cvGlAbcO-CnVdq_jxnnfGz5x0a20nsJHAb-NeOYv4QwbtINxuKNAjWPcyZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری مردم قم در آخرین حضور امام شهید انقلاب در شهرشان
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/447833" target="_blank">📅 09:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447832">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🎥
پیکر مطهر امام شهید انقلاب در آغوش جمعیت گستردۀ عزاداران در قم
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/447832" target="_blank">📅 09:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447830">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dfbb44f7b.mp4?token=AEXjYFUv7CNy8rwcwM5DDk_qrn-KyRxQpJbayo5JLaqIWkK75EVKrUMhTWUSLdRX9utG8p2ZIWnneL_4uWYcOafo_JMnWhTBln9E4WVhtlSY5LZ8VpfSJqGJNgYP2lUA1Vtci6wCeUki9dz0hK3Cos9Ztd4E0irSva1joTXiQnWsxNK1hAtG2r6HZ1LXlPFgrnQ_4LE_2GV323bSiidbcKCFZn1nbpigNMLcRNEahrxbhJxv5WA_0bqKF1KpzAFtURTzCWoPamHEcAbrUFNpzymlujuFY-phJ7YgpAe4KnB0wfF9iHjnEtH0HCOAmqMtExz9vVv_13F3eb0WgKXAbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dfbb44f7b.mp4?token=AEXjYFUv7CNy8rwcwM5DDk_qrn-KyRxQpJbayo5JLaqIWkK75EVKrUMhTWUSLdRX9utG8p2ZIWnneL_4uWYcOafo_JMnWhTBln9E4WVhtlSY5LZ8VpfSJqGJNgYP2lUA1Vtci6wCeUki9dz0hK3Cos9Ztd4E0irSva1joTXiQnWsxNK1hAtG2r6HZ1LXlPFgrnQ_4LE_2GV323bSiidbcKCFZn1nbpigNMLcRNEahrxbhJxv5WA_0bqKF1KpzAFtURTzCWoPamHEcAbrUFNpzymlujuFY-phJ7YgpAe4KnB0wfF9iHjnEtH0HCOAmqMtExz9vVv_13F3eb0WgKXAbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فاطمیون افغانستان با شعارهای بیعت با رهبرانقلاب برای بدرقۀ رهبر شهید آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/447830" target="_blank">📅 09:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447829">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b72f9513c.mp4?token=vN10R5mNHTYAPU8UA8jvinyudY8NGBdK2qakAr3KCfnAPRFPenlkOQSSA77HN4PWtKPt45s0xY5ZuTF70_Gv2oWHqBA2k-j0nbNYUwR-iLiGkm0xtQS_PVVaBQDIjOPvek9vIkpi-be7-kfg6CLzRM8kb6tposMmsbbtKAT8vJvVVvHbm7sIoTJsSkBZ-x38jzIvcODaoNzw73fR4Oz8GU0gewOuG1KPiHcPOuUBHo7Dk5hsSIm6-AeVmQTJSYkeqt8lnSNPVQejmzFu7mg30j3CcLv9YigIV5BthZ1MZSNl3LqD3Y5JZRL6kKwe995LMO8Jcge6TuYyzD5Y3u00NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b72f9513c.mp4?token=vN10R5mNHTYAPU8UA8jvinyudY8NGBdK2qakAr3KCfnAPRFPenlkOQSSA77HN4PWtKPt45s0xY5ZuTF70_Gv2oWHqBA2k-j0nbNYUwR-iLiGkm0xtQS_PVVaBQDIjOPvek9vIkpi-be7-kfg6CLzRM8kb6tposMmsbbtKAT8vJvVVvHbm7sIoTJsSkBZ-x38jzIvcODaoNzw73fR4Oz8GU0gewOuG1KPiHcPOuUBHo7Dk5hsSIm6-AeVmQTJSYkeqt8lnSNPVQejmzFu7mg30j3CcLv9YigIV5BthZ1MZSNl3LqD3Y5JZRL6kKwe995LMO8Jcge6TuYyzD5Y3u00NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کریستوفر هلالی، روزنامه‌نگار ساکن آمریکا در برنامه پرچمدار: رهبر شهید انقلاب به مانند امام حسین بدون ترس شهید شدند و غربی‌ها چنین چیزی را نمی‌فهمند.
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/447829" target="_blank">📅 08:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447828">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c94196c376.mp4?token=ViSrZQLh-YB4v8Oo2OkPNC8tvAt3ClodRVZyoJWbr7-5CwhhTumpVl_a1LrBVwmPDUSM5p3oJ2upwOUU3ckm2SdovjF0e_7fpfyr7eS3omqOChMlvVMY0-bam1xR8oS9U6shxQHWKPfJfz0wcP1Rtnyr4iEvXIk-IrsO2WcjJmJ5E50QqEj78FLi6-DSHxt8aPsFPVV5xeuqVcU1rh5Od8xwxFwsI0gavxTaI12MEnbQGD99K5XOnhjJ3aU91NgDSwHsN6bI5EdduiiPIMPUW0Ia_FRff687CXz5I525WuZojlWk4VbXq_Pp2nvv2Mktd86TUzoO1MMR5r0D3aV4S6tqlshxyxNwokOtWFOt-MnBq5jaI9zBoAt5gBE0QZZZc-FVroV-8ANyvwbSCsYolRb18Uc0nf5uK7foIJWDmTMr1ZLFGP63PNQVItDoeKb2wsOhKjJEjIVNpJIfh6DPNw7tz6U6_tut1Y1ozqybcJz2mi6uwJ_a1gmuV59wxZHFFmeZSnchKLdJoi1g1OgyeAKd1jR1IVjJ0Djq8gOSd92GsojHU5bL05_Jz0fcGWQud1IYr1RBVQYxlesXPgvXMwcCa8vYxieOYUG6CFvo8qyXh-ChK7Dz7vixvvIn2IQkukYuO3Xn00Az5UAAe3CFItn7hoRNQJQ4lWI-HYi0_gM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c94196c376.mp4?token=ViSrZQLh-YB4v8Oo2OkPNC8tvAt3ClodRVZyoJWbr7-5CwhhTumpVl_a1LrBVwmPDUSM5p3oJ2upwOUU3ckm2SdovjF0e_7fpfyr7eS3omqOChMlvVMY0-bam1xR8oS9U6shxQHWKPfJfz0wcP1Rtnyr4iEvXIk-IrsO2WcjJmJ5E50QqEj78FLi6-DSHxt8aPsFPVV5xeuqVcU1rh5Od8xwxFwsI0gavxTaI12MEnbQGD99K5XOnhjJ3aU91NgDSwHsN6bI5EdduiiPIMPUW0Ia_FRff687CXz5I525WuZojlWk4VbXq_Pp2nvv2Mktd86TUzoO1MMR5r0D3aV4S6tqlshxyxNwokOtWFOt-MnBq5jaI9zBoAt5gBE0QZZZc-FVroV-8ANyvwbSCsYolRb18Uc0nf5uK7foIJWDmTMr1ZLFGP63PNQVItDoeKb2wsOhKjJEjIVNpJIfh6DPNw7tz6U6_tut1Y1ozqybcJz2mi6uwJ_a1gmuV59wxZHFFmeZSnchKLdJoi1g1OgyeAKd1jR1IVjJ0Djq8gOSd92GsojHU5bL05_Jz0fcGWQud1IYr1RBVQYxlesXPgvXMwcCa8vYxieOYUG6CFvo8qyXh-ChK7Dz7vixvvIn2IQkukYuO3Xn00Az5UAAe3CFItn7hoRNQJQ4lWI-HYi0_gM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از سیل خروشان جمعیت نمازگزاران بر پیکر رهبر شهید انقلاب در مسجد جمکران
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/447828" target="_blank">📅 08:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447820">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BI8knv06OwwW-_lvT1wl2T9hWpt6WLz1eekHSoW72aHVpqjxbTnm4EC7vmgr5JDCsns5dX2JpM-H94GnVtrH3TW_cxzgRoffbS4-RGb3YppxehzZuBDpvz26pLG2f07vYS7B9aKWH13eGdTXmHDUppGNDJBc-d4rE7LHTaBm0ktpZVKRoBxnM9qNIcDRcUD6Mnbb7sT1ETeQrHRZZZNDk6R9UvL2rMQEmGLjByqN6CIt0VVjEMNI0MboKaISeg5QHTULX0yuOrtkfFd_hRAUcWYIc1_c54LpOCSmsZhQy2PQY_E1ufsF2sWKb_TOzxJ3uhmqMchvZfUdvVq0zf7Haw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dL9bo-Z4b9dlTqlitGpk01S0nZPWYrzAQWLmFgPi2Yez3TqDIzhIdSCNSPmzifmiY9qopbftoLCH36D3rr3hL_1CyN6-GMmovujNsMQ3pkbP-Xq4023GP3xNJc544vtYiBPVwWllSlQiM2FWw3VfQyYyhFVQhoISg0Z9_zq--bIq3X1PUtbKuEl9kjZCHG6vJOGf7GdnK-EcmHokixQjbIL84LE_ireNI8hxfNZQqadPKBGOZb2nEPzk0lmwlmw8K8kHuNFz0CJ0n5x1Ar9Q1Rnxpgmd1yE2UmD0DcHFm1b923KW6b97h0a8PE-Eziv9lO5Myd9ztYtKTz-v31jHyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/adB2u0eHQNitoM8-cGQbwHxQXvnGTbz_X6oGtrNBravNYwZMWzkJAO7iA-ZGt6ysPQTl5xfI-UTtfgXrClcOaIYOcCuTl-sIMIjoWl6_1AeSoxq1Qj7WEbJgFjiQD0VhmU38qd6FQzU7yxqk4y6eLzaulKNUe-SfTQI-4CVgLyMDpRJqU0bytBr21UTBo_o7EvjzzkldnhY6U194cUQmqz8VKdOT_eWu-cPUR6djFLfoKdemUUELANJt3yprPcEg-7kw4OP-Ouzv8TkcITtp-2D0epDQ-j_50sQrszSak4ucq6GrGqTTdOw471u3SHB9AKDxJf8Cdo2gFzs2dvtxFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mPApEG3XmlwaShABq3hEqHuklQFd2GaS2xtlVpChO_cGgYcsMlD4Sd_lho-NxU9RgMeAXUtiJk4s0LvhQ5mzHfO6zlj-XpLGzLW5N3nzzts741fUPjFc47y6CSmPwmIWLWbv5bWuhNRgCFc1_ge3TqicynW5b7l641wtNDp-WCWmJQEuv3yNSXbz5ytI4KVSWmUfdN4MX_BU2B5OFKw8-sM033q7PG74IhPm3t_vhPxxuY8rh6D_bG7E5U0TNf6UPQwI-hDvZQNPCpHlRxtRPXF2P_bNgNbiTlVd0gfdBez6HuwKpiOf16ZV6kdASb2DUitMl98Z-anspzw0S4gS6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B2koy7K7wzWvL-Qz6TpCVaCemYmke7usYc2zcxPABhsj5HSgeL5mn06QeLwxtY_yz6q0-IwjSN8xPrCowiIhQpBsgGCdeI3IxNJ5YToUvdW3ETex8_FewOX24BuG87ZmZUSB0UWJe_IiYrV3vtCbe4aY_fSMvMyAwSDib2L-ltKlVODlr6QoctCENXXUajxkEX5OVopPoBihH9Kk1VGByaR35LBmfpCOAEl_9mlONWSh-nERv-CZKp9Fjisl9RRtkz4NykuJ-JRDbg0ZXLpk1I4jgJm5_t4MWRjT0mmatVhS35DZ2NQpbND7cKjl6z3b3CMRm4Gu0J5LtWEpbkHYHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RwJU43YGmafVg86ci-JWRmK7jWADD30rGrFiDhwSxIebDR44o28i_TgVyI9ReIa9yAjDofKcAkjw4ew3jvt9j8fEokjOwdm3yA_LP_t29V9RE3SvrpJhRxDk6OD9J5jIgIG65OvJqbs9zal9oo1ZwN1h2RL8TdBZ32blreBEupUUfzE8_kCVSsfi-VyYDkBQTEJxTiCIuo0G72n8z2FFaYJIx6fwzYUERxouy2_g0DMxDtpEHsFlUAmsgCJB-xKCZuCazGbp4PnZnt21wT4m75zsbu8w0CzbWm7T4wp1X-unmB4o5GUuYg2e19Xopv6DBlTDvTQ2BPMipSGriqENRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VqS8Bhx0IGQK8ktQfP9q1Tz0FLTCRWetg8Z5gBEDz97eV-MjPwVeR0LTSC5qgH06UyTze_ihy0iMtDegPHOhUyqWhgfzZSmrZ8pMcNRz7WWeLnfEuHmtmR6am32rXFdL6D-Bn_BPSZrATFhDTRX4l75hDx2e6lX0xFbT4apCFv6jvoVetV9L7O14g5Msj8DmXs-NdzgziuSeC3766q7SwZrsQGjcfS9qFqcw9eGpneWBBNTix6rimoo6aOV9qQoO-1RY8cQ_wxZ8ZYHC_s1rhQjf1TpCxBPvW4oWMFSL9hkL7T-CzHPAh7mgO63-yxJaRt75p-y8oyzXGr9km5IQuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DL_XT9kpXq_ztUQ3JR63bzGlokO1krXt6s-9I9oTpQeplDzZfVdgEvqMT5MSyOmH90JF40EBjvZMLhZIJrIwea6-dZq6Yit4E5sR5OCObGrzMxHi3fiOyrrcoplfOYokd_efLgHwCs5nQlJlOgNz2sflBmGMadpa4_lJVOjk_4l6P3_zAQ1I-RDACZIeKSsqdLx3ZydlDG2adB5WK63owG74K_aArl-nOlVtA6cxpxbPzMw_W76i0qAACdMAKHgzBlA6bkt8ZIktbmVnslIkw5um2hYVBYXGDoTOZOkBZJp3Y0gR-dL_SqJb57va8M6YdZPfBS4t1EP6RzWUa6L6bQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب‌های هوایی از بدرقۀ امام شهید انقلاب در خیل عظیم جمعیت مردم قم
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/447820" target="_blank">📅 08:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447819">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e7e992159.mp4?token=l76dbfhjUL5cCeNvWWlxVryZzfNY4CZXOghFXt1iOyFQQy9nqp00xrY7HHBHrkpDn47UQ4oPEicRnXcUD6pEqDVigGTO6WCM39HR-9HJOjXv8dvR51tHQrb_GAy5SW7rudpJZyI4GZJgitxpeHypTQAEnL7I9E6WSipDQhwSEV5k7asRrdLpm7AwkjphBrQyYX0LOuM40sTY6POweJdsb_k3g9LyiE7vEIitKGFFIB_thxqn3wN0zsyXUdqigfZc8X_ttk7DndAY9MDhbeaDWHJinFIyzA-jOXce1U0R5BjhmWeaL15F5sGOCgkt9kPGLkecxJ_lG9NMjJLzLD_WBnlerx0gLHIiNa8Usga4w0B4GSvlWuNmGwIHe-mPFCD24d92cYrXhBWNwd5KiC03k0vr9XdnYkWU9u3ldGe1UiHiSpxs52w-zTnqbpCB1kYhaiyG-ZpzlGDCu12CNID5RNjAYG1kiTLKo6kr_6s4TABz4SVcX8B6jOxtLuncwDQTyo883jVSS8q3EBEbAJYJzWAdtVWTfdA2tuRelslwh0uvx8V5cxwO6FmdWySSrRvTM8gPwPXU08G0-03PHm0R6ZIzf0GnPAwuQR-0vrZN0nsxmQr6vhrqduiz7DJlJIF6lQ6rchq0B4OWuP2_VXasfqVxfr7M9f-JkqXT48IzYx4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e7e992159.mp4?token=l76dbfhjUL5cCeNvWWlxVryZzfNY4CZXOghFXt1iOyFQQy9nqp00xrY7HHBHrkpDn47UQ4oPEicRnXcUD6pEqDVigGTO6WCM39HR-9HJOjXv8dvR51tHQrb_GAy5SW7rudpJZyI4GZJgitxpeHypTQAEnL7I9E6WSipDQhwSEV5k7asRrdLpm7AwkjphBrQyYX0LOuM40sTY6POweJdsb_k3g9LyiE7vEIitKGFFIB_thxqn3wN0zsyXUdqigfZc8X_ttk7DndAY9MDhbeaDWHJinFIyzA-jOXce1U0R5BjhmWeaL15F5sGOCgkt9kPGLkecxJ_lG9NMjJLzLD_WBnlerx0gLHIiNa8Usga4w0B4GSvlWuNmGwIHe-mPFCD24d92cYrXhBWNwd5KiC03k0vr9XdnYkWU9u3ldGe1UiHiSpxs52w-zTnqbpCB1kYhaiyG-ZpzlGDCu12CNID5RNjAYG1kiTLKo6kr_6s4TABz4SVcX8B6jOxtLuncwDQTyo883jVSS8q3EBEbAJYJzWAdtVWTfdA2tuRelslwh0uvx8V5cxwO6FmdWySSrRvTM8gPwPXU08G0-03PHm0R6ZIzf0GnPAwuQR-0vrZN0nsxmQr6vhrqduiz7DJlJIF6lQ6rchq0B4OWuP2_VXasfqVxfr7M9f-JkqXT48IzYx4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای مردم در مسجد جمکران و وداع با رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/447819" target="_blank">📅 08:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447818">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🎥
حضور جمعیت بی‌پایان عاشقان رهبر شهید انقلاب در خیابان‌های اطراف مسجد مقدس جمکران
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/447818" target="_blank">📅 07:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447812">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bHrlKU6IZBZrPZiQyWmFwqMYha1ZF_ilS7UhtqNFlrm6J6KojX4kKYXbq9YfCPx4XKUkJ0VNKqiZ2TgUS50Ol2rcA4bvf9HN390tKLtEeDUlQEq4FBy4hBHhydeNkHl68eTx4jSV-WMqbdufhgAM4byiteiWwrPxusyF-Y9NZqTwJKRFjI9WUS9aWyesuiIEInxa7mDwfavO5-TtN-v7xLeaCCOEF85nWKHuk0Gnrb21msITlmR9oUM2YMU6ATiBzmmiA7QtbmvZFeszZRnFEGE3j8gi-Cae77wn82RLB04VeGCb53ohTp6wTnHLYWpEincrnGlVihX3U75osE2YTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bgfT7CZivwVKHa91bM0x69G2jb_96X-0llXhynvP66apFnSDSyEaJtCCVBPilOK_Sr6Frvh3O2lIUKUqGGOmjfE3hIUArPeByYR2xBA6ECsTIPSsqwIDLZZg4yYy4bJxR4f58Pymbt16BW-dBB_n5pvzGXIOlvm0Z28hDuW4LKxdFMfEEnCsdfK9y61s0tn0vDX8MJ8EF7cqSJ4RbtkYav13gFn6V3f8y103ypDhEY8XesY120WiU89moevZxTq-CewFyO7m5AnEKXWYbQjDKRnZ2k_Kfq_auGLjGYa6DFOyC3gAiiIKmlubOKYKFNuCiPCC6jmGhVcelODWN0JYcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I7cWfaM48W0sNmSfNpTN4pbZlgsZaCzx1cqtfMXAJnz342mAK2o5RQI-QgOQ5WYG6zWomdD8nV7ZtdUygEMTYzAXrEff-ndB5YDrLW_gav-g55wTKuHSR9O_sJFK_0ZYu_UWrjlKZ11hqB6v6k0h9pDgwQuu25g6RsAhG0TAdgumAH7oYnOGVOazjKSpd68EBPoa27-Qb6gg_JxPU82r2vAozlA37hL8XvFMrnPP5k7zINjj3QyHEXL0FyXPRUxGamgzHUfiV4xwy-HUXNauQbYvw2XyAdrVxOtQo1ydn5i4RC3wltJmVmNqTfoB4s6Z476y98-jzqNeQmgwrt1Ewg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uZdB8E7D5-gs35Y_rDz1555SninCW7tho8gyxiVdC0kxeqSpfZTLl4E0Cp8hCM4egB9Eo-8P1IJ6_5lOKUxzuyuS_FsZYxhIkw8FSGsZdUj5a8uH3mBgY07DyPDfPPEpmysBaEvNEGScL0uy4ih79D2o_MazCJMy2eyKII9Jls9GRGam8hqYwG4EirJ0X6uGu24NWe_r2LjpOR2HppKL_04sNOGbBARwBT0lBF9gsv2mCrTtl4VK0aKltuYrDz1-m80nzYcMuCrROewk7vVZZMfFdb_kvchOyxCqp5-zIUllNc3FwdIs4ZDEWEPKrY97tvd3MrPabaaEqwkH8zxnzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ANUigSwW_mkfzvI1xaAwzpQMHDeV2u1PC3IH9jgNBBYK3Jyw7RLELsmZA6zT7bT5UunHqJ8AidF_fjI-SYqQrN4ejIjMP0TjfumJHXN-2yVmuitRiMQHUkjOZEm9xFycoHA0nso9g5xF8dXgv3fV6HkWLJl8Tr9sHqwB_TMSYZNaBRq-T_VdwqCAVJgwOrXrAid3ggH8HtR75eDh6Rylm4cslbpHf3yXA9VjFcFzzoFmofFmDV-_fb-hy-NQUIljoEwlTeEgD16P4sb9X5aj8bIcJTkxlDgcP_iK-PdSXmuMLn-XcWJ5NAmzYT-UHc5k7BAcJvcU5e9AlCUOFBDEWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T7eVhWVGEh8kvykGQXrClkkhQizy58MsPM5TZuorm7xGcS0Joa88ylsN19uMD_yYZGBofUDJMQb62xR0r4MIF__RH8ugELiNy7uoACdg0KfZZuq9X0X13lGjGcm772a5TMM9dStooKgNoQL4H8Mt_DV-mmpzlgcqepREPD6bokpejxxHjo1F7q_LzZH-Lm7QFztE4NnslTNXOoEPZdyDN6luDrZn550gsNNEXVe0UuoTHHKZFcFYenVPNAi0YaFVqBQ6bo-mHbwTGfF8dNAEaY_2F4Y75qCtpD7Im7DB9rXXIsC-kR5MjCBUL6th5-2FQD4MtIbJQPSRZES3X7KMdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نماز آخرین زیارت
عکس:
حسین شاه بداغی
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/447812" target="_blank">📅 07:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447811">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8-eSqXSBtmq82Fgyxro3nN7l_qoNPv3WWirXmcgeR_zTu8qJ7CyHiVwXzdOwHilSWA9l5lZp1fjoWNI_Px2C0Jw1bb6ot0g9Xn67DZsYKgWghNRtKy_DYzsk46wwNrQ3MmAyZHVMWfUCFc-T9YcPoypAGarh6Vva-HLIsNviynzZurosfOBQZ7BUs15HWCPrFx49rQKLn5Tqcr2ULChEpLaVkQCgxYLTNABF2wxudOOW-la9TYU_Uyl1e8QRKVwTmlOzGvJwnsiXfNsY9tu3RXCFSXP6-F7N9UaUjFQGHTCihxxY4An9dP6x8sMDzoFsrB00_FmCYt-VmE6IXcyig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قاب ماندگار از حضور خیل عظیم مردم عزادار در مسجد جمکران، برای اقامۀ نماز بر پیکر مطهر رهبر شهید انقلاب و شهدای خانواده ایشان
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/447811" target="_blank">📅 07:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447810">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e19f3357f2.mp4?token=j3zABBIuBrMPjIrJlixIrltvSbnpEVmDQmq5wXzpV3tjlUnCKjPzehT30wfI6X3dMCMa01vGOOrQkkbSKfdl_PXYxyUNosDkCkxxbNZ5zEyCbU25Rlk1tStLHwgWy4UWVV454ax_FfGNV3D6YEfDDWM4csXe2r5nadz9-hFDbkbhacuFYOJ8fEUyAUW_zSbilGTh-dmHgdnN4Fx6LPJ7XZk_iMenn6fgmYGPGUW85w_jhR_URtx3hmryU466wTQm6WyRF1iExt6L4wdt-39u8rpZN4dmYaMtGI9iUNf2Jmyneh4ad8sNWlfa1iNMrJMzFA2IrYiWx7tokTskS-Zpnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e19f3357f2.mp4?token=j3zABBIuBrMPjIrJlixIrltvSbnpEVmDQmq5wXzpV3tjlUnCKjPzehT30wfI6X3dMCMa01vGOOrQkkbSKfdl_PXYxyUNosDkCkxxbNZ5zEyCbU25Rlk1tStLHwgWy4UWVV454ax_FfGNV3D6YEfDDWM4csXe2r5nadz9-hFDbkbhacuFYOJ8fEUyAUW_zSbilGTh-dmHgdnN4Fx6LPJ7XZk_iMenn6fgmYGPGUW85w_jhR_URtx3hmryU466wTQm6WyRF1iExt6L4wdt-39u8rpZN4dmYaMtGI9iUNf2Jmyneh4ad8sNWlfa1iNMrJMzFA2IrYiWx7tokTskS-Zpnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروش بی‌پایان مردم برای وداع با رهبر شهیدشان در قم
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/447810" target="_blank">📅 07:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447809">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6340788de5.mp4?token=hmLUYe5RUV0k25tyYk6-50CHXyZ1wYxvl5F3Y5clHmmnDdGUKIPLWZ_lbj6h7n0s9ZjGwaEzkbAYmwlzKLUhy_Z1F-MIPL8M8pgg0Tt26IXCjVbvZ_ZVyckbxoLeY5VPRLQgNT3TdPOwlamXZnN4USUeOSowt8Jej6aOqfjMF7lVrAw_QE4Ij1u7F8sR1WPBhYDeCW5AISRcDEIprOfkHC6qwvHR9NJFqSEIlUbL3ZXnJp6CtPWJR0npHs_Kf1NcuuWgUOlCSM0ndvo9mYLybrTt_a3Q5LF26vhGVh9lQ1V2TxkQ1rVhRFv1Tc_coI5ejuCumNcYkgjd5dtk5wU8jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6340788de5.mp4?token=hmLUYe5RUV0k25tyYk6-50CHXyZ1wYxvl5F3Y5clHmmnDdGUKIPLWZ_lbj6h7n0s9ZjGwaEzkbAYmwlzKLUhy_Z1F-MIPL8M8pgg0Tt26IXCjVbvZ_ZVyckbxoLeY5VPRLQgNT3TdPOwlamXZnN4USUeOSowt8Jej6aOqfjMF7lVrAw_QE4Ij1u7F8sR1WPBhYDeCW5AISRcDEIprOfkHC6qwvHR9NJFqSEIlUbL3ZXnJp6CtPWJR0npHs_Kf1NcuuWgUOlCSM0ndvo9mYLybrTt_a3Q5LF26vhGVh9lQ1V2TxkQ1rVhRFv1Tc_coI5ejuCumNcYkgjd5dtk5wU8jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز مراسم تشییع رهبر شهید انقلاب از بلوار پیامبر اعظم(ص) قم به‌سمت حرم حضرت معصومه(س)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/447809" target="_blank">📅 07:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447799">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SykI8EZPoTn-74wjN5n5VvzuUQzFVSotXdkqAUWc5sDrqz_y459oHXol-geT7N_x1Dw4y0Y_HE9VwlLD01ionoNzc772zA9FKkTxgpt4zwo0du_hJYgL3p-iFwgkHSOhGDztJ8Xg1PqkuqjWiZOnnNpmXB5_7T83EJSqQz389yhw8zEP-QI7masXWEQh8XtVVIcwHaZusxHNtPxWoTqHSm_v-gOhrecYoBkjcRVRbpHH62fJeAEo14RYSSl7Oknqn9WWG4L_Jtrs8LWae7lWRHMTiQ663zioS8x85NxQRTseUxVzEeZvB794cfApsW76vHqwwHnw1bn7JihG1gSU6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qvh-ttZAoxUmkez3Z2SXVDKsgTSXwBOV2FPS97fOir_koKO8Pz45pbsTaOHs9PMQ_bUk70myXJwtvJO4ODbL2EuL9fTtsb3wEnvxfa27chdqkOuXNbAMZbyyal3flt3aM8fda7gKDEvQssCzlslBSylThIVMTahyolqDgBsHBNlA289-WP1U0Y4L_d72izHaJyZWJpM5RqQ7OpPnGyoP-9nPl_K2VKKcgdOdSpFgTQ5Zjl9zhfpx0f5PYxk79_a8c9t8WVnkcWFBv6R__gPeOTKNvCQu3rKi0waEnG9llLDruYl0Z6cEM1xEAyE5xhvFgfJSkdrm5BJxiWHORAxYVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HSpNBjLYSPoGYqfjsKSf9pl3sf8sf9nWgKmC-TM8bfHP_jYULDe59ATgt_YdXPPbxtg5qI1nbl8bMBwCmIGU-wK9RHzvUFDGTiywFvmj9RQ6gwgf6Ys3iSzyaZeu1nlUl63FsOtaajJIts2b4OBwWKnzlTvhG0MhI3eScAq1ewHqS5unse4snLssgZfgayU7nRyHqRL2UVyORI-0maL4wynr_Q661EsdhOSnX2cmEEvqIEZxHdoXjGCwW-Z0oDH45sH9gkySZJSllxiqCa3QhvQSuyf55QRYMNLgFEg0NFRhg3Y98tO5h_9p9rIBIcTS1BhderZkB7plBOwwCie8yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B7gc2XQ4mm-vbaZs5p9Z1yAa29IFDyPEujak0FSRV3nI0Vve0ImPiIrVNE0zRUH2z7TxWXZgVLgXi9HFOV_cNDgoSUFqfVQ2vl98vZcirRJ9J_3f2gACRuLVAraSBu7HuIGKuHKreA8rWzcU3CGuAevR75igBn827QKBp3TM-h7ymKDnECPTRuBoh1wnsHbjlplrRjJX3nKPdGS8DPQIKEAKhBCZdg0_pC7d5S1qRP-BM3J1PFg4UB5XRz3S2e8-8VUA5cZsNQKJBtkR8SwOkHZQcNSx8-KzNbpT_qLd7koq4Yz8gvCHFu3Y7QdHLoFcfBI6UkO9LzD5oCQWwQwX4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P50nrgkVVGKVPqjPw-bvXnJBid4eaZukePlQPaEcVV5tRuO03ddauz8nfCNzHT1xODH3_RnOq3B64ZdOwbDuIwGfkdWTSId6DdLFnTbZKPp6TL-NanmpbQzP4zmiVztZ_TU1K0zU3VCo9cxPTMzhvi4C8ZRvJoG9mSzc4cjEAd2CflU9VzC3pRDhKW65qDgxei5oCq5TQmOfZXUaCzfPI5wsRlKCM8y_KaQA3e0h0ShFVLlwLQ6XJ95ngQCf9BOTehvVa6EK_ckURXMpkVRLAi9VvjskiZo7HcXi907QzYnJA1nwMbsv2JwokwHYdswWYN3T6WmDJnvSxzHTTPggVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BiT8f4Q0Ewk1ihCFB0nAunWGkpBGJvnDY1wot0ypqgArS_MXbm68_ixtGPtPZPweLVBmwlK7trD1-Bz6MiSdwDI35Pw0LILkFNMxhojPGMvP72o0kPzJXUwPMUS6M2SyoOH75bDOvqOI1HrAA4xVd3_ytgHVIS8yB3IiZ1asf5kXyMa8GUb1LvCGU7D4saxP7vsPIXhoTVjiLZSAo0Ad3DkYGcOH-eR2bK7Xghcv5V092zGHEhpBe_btkUUik9QXxknBovVibJdSN3npZCk7hOGEM1I3-iGHoa1LkGWmj4alOKMuND-nVX8Ed415LU4CVwOcukXTTsOpJ0aKeEmTig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QtFxuQVaiZpuey_gwEo0A5M0ap7DgCiWVwJdXWEapJERttkHJKRoMjsyPxusk2KmeX0J0XNwiUwKqEXSQJaXICsl9WbjwyujdZNc1b-4kH8-22dxXaUZR4UVnjTNkVWNPZwqNWv94o1JlLmZNxNlds2R0lvIwS8xOTiUgbGjGdUDQXeUhZgjonwYr5IP3ATWdN68lNmdafzGUJJK3TAIjCsa-pw2hM6E7AIYzpsIWGsLaK3gXXef9M6RRpiJzpgrZluradDlwjrMvmOZxG7FdiAvskXkU9XrW00lFFfg8_M_5j6SuaFy8GaXBoz18vFafQo8YNqebyDui8VAT_ewaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/focqv9SIWwUYDjaQgAnCiWXRdiZNKvUvtw0A6jO7Tl6DrCnRaWlXlDQ29G2PI9QFkQY7dY67dS0tKPAK2N7i-uODnq3CVFinnSEV_-TYjL2S6S8gEvDcxjZshOJZrp0JjiJJliMxHTuJJLIewaerRwYdf_sx0fsChrEMrHhHFptK9ZCidV1bA5YAjgW0WIvBI3hsldSsFdtiQJJDWkTWVKnQn-fitTCYxIPIXIwMxaa5YgvOwfX1xLVRkhNtuTpwjy5pVUjPyzp8NuPIa1w4rFm5MEvsLLPvluLe_KpdcpYtrdU1jwIvv2WHEX5hbrpE90hx1eyXEKJv3VSGFYkBug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gFgl1-H3AN4htTW2xCQ-Orwc7vrOlLgcMx2Hdg6zDKhwl8i35hAE9MDW_Xl37NejV37hXNQrjpFP8BvAd9i4BarHqDiHC0i81IXah3GkeSobwrLtgf_SnOlHpu3nVbPFEfq0HeOQF3Yfw-ac5zqARNASPsMaXeyJdySAuTTnAVwi9hiTOCwr3RieiMDRwOH8cKZr9ihVv4FETOW0dbuH8hU-mTKwxKdYoHXVppT5Ygs8NPjLNDLaTRxQp3pZGLyDmyDLOS4YQj88_GiMsUmTqv_Nw5y-VHYJoSeQWX13fENogqY61dRpV9Poi3bgbp_fXFGFrM3Zs4H0bRl5EXnGAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MCn73dKVqD5RoT41VxorqvnGe5QxacvrSSQJcBOue7HXoj0zdR3sa1LsH88xomTU5h6iAGJ5xdqkrw52_zucv3uWzahRDHUfOL6KMNnDlWZG4wguwKd2VRAxqJ-rOkUv3fa28QdKo8nke-WnvyWxrGPzT2GQL7MKt-jG-zXReBf0jT5930XcewWr9N6swOaVNNCkGdf3i7Feh5KhBk16J3dOzUye_JQhmF0B-zFbP7tZBJ642FD0F42jE3jqcXO4ldNAuFjclE7U6spY9NLBdPL9emO_aXURkjjUXh-0fAw1Et6r_GSadswzwBd6NRReTBrNHdRy4F2hjqZbUXrmXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خیل جمعیت عزادار امام شهید در بزرگراه پیامبر اعظم(ص) قم
عکس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/447799" target="_blank">📅 06:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447798">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/983268db8b.mp4?token=JYf9YQuz4BPck8issbdP8NZaIYfcvocLzfMKEMOq0hE-3EkG6_JA-CvvtuYuh6UUaqWutc-0rBIiLIY_8cAxegaL5P1iO0ERaB8WZ_Nm2fpli51M7iH-8feKLCOobFcsrMh6NikmppV4c7NJx06NELQT5fE-YCu9ldO6d6tF1ovJWOVCdaw3YFGrULXpnZj7XgA_uqOVcqln52cdhrF-YL3qq3lsqDH46BXWEkhK-QyYCNmdJ9LHRj0IqB6lmv0IzlOTZahzphLkCxokH9Iv456mecdhrl8rmqhYAS0xYHSdo5Kd5rbh00MB2mUu9nYznMmt5f9zG1X_d67-KR3QGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/983268db8b.mp4?token=JYf9YQuz4BPck8issbdP8NZaIYfcvocLzfMKEMOq0hE-3EkG6_JA-CvvtuYuh6UUaqWutc-0rBIiLIY_8cAxegaL5P1iO0ERaB8WZ_Nm2fpli51M7iH-8feKLCOobFcsrMh6NikmppV4c7NJx06NELQT5fE-YCu9ldO6d6tF1ovJWOVCdaw3YFGrULXpnZj7XgA_uqOVcqln52cdhrF-YL3qq3lsqDH46BXWEkhK-QyYCNmdJ9LHRj0IqB6lmv0IzlOTZahzphLkCxokH9Iv456mecdhrl8rmqhYAS0xYHSdo5Kd5rbh00MB2mUu9nYznMmt5f9zG1X_d67-KR3QGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از شکوه و عظمت حضور مردم در تشییع پیکر رهبر شهید انقلاب در قم  @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/447798" target="_blank">📅 06:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447797">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cef9405f6.mp4?token=LHQjg2tgAWzLAzyZdBj9iqaJlxzvHURDRThGC1K44TgZvypzV8k4fQTV5fxORkIXoQYpIczfivm6sK5eDAZVVsvw-t2NjbdFutXWEM9IFbBzR5E7Dd72eH7iID6ald8wWxI_9IyzugtYFiPouIOdH0NIv8n-ovkwS2Oha9YZaiNTttiy8jYkzvfcZ0lnYDVDkdCxTJ6Yyr619yAmrGjJYN6BQT0JUBNMgf8ehF8PpBaf15n36RXfIV-uoLdqvKi3Nf8mqzjh8zth_QLpGowalMyatV-GKIo5fkOgC5bv4woQ4vJfKLiWnGloKOjPJucDZE8onWUaX-Wn1J3H40lMVSYD8kE8ehkRkccc4-4MDzxqVAif80KOkOcLAlCzieLldrosBbZRVZ1g6883XkrrmOkiWC6N80RB9vfa9uZ4vmW-erKyU4X0NJBLp21NA2_ZtSImLcgR12yMcFcYeu9njutvjJ0VZDRK89QaboI8C6guKIpjmfEPXxmX9QpsFxJVUjaB3cFRHJU5WPZixz37Go7uFoiXdrQ4VdETrKbNZliP4GunHEbed9UaR9HzuTkA0Bgr0k3BzfFjeQ-eKsTQqp7t8RMuFomQJmljtB7fkGoz4_esUXOknP5ZEjfFqzjkc-TyWCis2oCMMRAeUt_L4Q5MkfohAOl80f64iOVUKp4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cef9405f6.mp4?token=LHQjg2tgAWzLAzyZdBj9iqaJlxzvHURDRThGC1K44TgZvypzV8k4fQTV5fxORkIXoQYpIczfivm6sK5eDAZVVsvw-t2NjbdFutXWEM9IFbBzR5E7Dd72eH7iID6ald8wWxI_9IyzugtYFiPouIOdH0NIv8n-ovkwS2Oha9YZaiNTttiy8jYkzvfcZ0lnYDVDkdCxTJ6Yyr619yAmrGjJYN6BQT0JUBNMgf8ehF8PpBaf15n36RXfIV-uoLdqvKi3Nf8mqzjh8zth_QLpGowalMyatV-GKIo5fkOgC5bv4woQ4vJfKLiWnGloKOjPJucDZE8onWUaX-Wn1J3H40lMVSYD8kE8ehkRkccc4-4MDzxqVAif80KOkOcLAlCzieLldrosBbZRVZ1g6883XkrrmOkiWC6N80RB9vfa9uZ4vmW-erKyU4X0NJBLp21NA2_ZtSImLcgR12yMcFcYeu9njutvjJ0VZDRK89QaboI8C6guKIpjmfEPXxmX9QpsFxJVUjaB3cFRHJU5WPZixz37Go7uFoiXdrQ4VdETrKbNZliP4GunHEbed9UaR9HzuTkA0Bgr0k3BzfFjeQ-eKsTQqp7t8RMuFomQJmljtB7fkGoz4_esUXOknP5ZEjfFqzjkc-TyWCis2oCMMRAeUt_L4Q5MkfohAOl80f64iOVUKp4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از شکوه و عظمت حضور مردم در تشییع پیکر رهبر شهید انقلاب در قم
@Farsna</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/447797" target="_blank">📅 06:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447796">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59d9c0fdb.mp4?token=uEHLOKBj8SOYKYfZ_BPWaxIEMiuW2fANLL6hqvChKKaEKRf9BBiU33rUa4qX5KfnUyav3gfpY9uGBi6NPutgPpV-HJZsi2KHPi6Pxo2R9jaeOwbNlAOreqw0jSj8Hqkc2blb1ndYqMHuW10NtsBKnGNMjNPj41HTYnm7gwtKHVFEX8C127jn6-lln1CTOZZQQDpL_W3eoUjX79SOpaB6PFpTyZPbhqOWo24x3DXrXAZq3AIxwdGPr6mibrsSqBOeEAHsW2kRMJlzRiFMDOxFviG7bXwi_UAUzA65ieg3nq3V4teBaet0xHWpN_1SMlVjlzVervMmi3MfbCwaTnhFMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59d9c0fdb.mp4?token=uEHLOKBj8SOYKYfZ_BPWaxIEMiuW2fANLL6hqvChKKaEKRf9BBiU33rUa4qX5KfnUyav3gfpY9uGBi6NPutgPpV-HJZsi2KHPi6Pxo2R9jaeOwbNlAOreqw0jSj8Hqkc2blb1ndYqMHuW10NtsBKnGNMjNPj41HTYnm7gwtKHVFEX8C127jn6-lln1CTOZZQQDpL_W3eoUjX79SOpaB6PFpTyZPbhqOWo24x3DXrXAZq3AIxwdGPr6mibrsSqBOeEAHsW2kRMJlzRiFMDOxFviG7bXwi_UAUzA65ieg3nq3V4teBaet0xHWpN_1SMlVjlzVervMmi3MfbCwaTnhFMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر مطهر رهبر شهید انقلاب اسلامی در جایگاه وداع با مردم در مسجد مقدس جمکران قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/447796" target="_blank">📅 06:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447794">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c43be92ab9.mp4?token=Eb5uxTWCeWO4J29hEBEUTup06weFaO5x4Fqm9FwmVuEVxv-wyuvfpX9FRg2a3Hm0Ni0eWdaHrgY8MSxs03gkLTlmkmpjZF4D1XBBedE9Iqo_o6xkZS2klGr8R3uPuxvO2JEAiWGgULSwKF3DoMvs87EK-nwIflTNMJ_cKNGsJS0qt7_VNvdw1sAAVMXC6iNOPrtwVDIfxXpiNolJaYB7wcvGBy9syqNmgKy5-3xOyP9Idq88m12MEvqNQE1VZhLEIssLphzJJvHTpMssG91m1tWZntaE2ZPwu5LZTTiWSxmlc-kcwrcWqjFPIqELsvZ1xUYy5L1jM8IVoX5BJWTBYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c43be92ab9.mp4?token=Eb5uxTWCeWO4J29hEBEUTup06weFaO5x4Fqm9FwmVuEVxv-wyuvfpX9FRg2a3Hm0Ni0eWdaHrgY8MSxs03gkLTlmkmpjZF4D1XBBedE9Iqo_o6xkZS2klGr8R3uPuxvO2JEAiWGgULSwKF3DoMvs87EK-nwIflTNMJ_cKNGsJS0qt7_VNvdw1sAAVMXC6iNOPrtwVDIfxXpiNolJaYB7wcvGBy9syqNmgKy5-3xOyP9Idq88m12MEvqNQE1VZhLEIssLphzJJvHTpMssG91m1tWZntaE2ZPwu5LZTTiWSxmlc-kcwrcWqjFPIqELsvZ1xUYy5L1jM8IVoX5BJWTBYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بانگ الله‌اکبر زنان شهیدپرور در بدرقۀ آقای شهید ایران در جمکران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/447794" target="_blank">📅 06:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447793">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b585c6d4ad.mp4?token=b3BLAKFjxulIzSgGmIrPk-GH238kBH7itdCVeLjnBqAPYNTBYV47dxKFEUZGVzRKNbNc1d1C3z_mnoXaV7lr6tIJMyha-EusTLHDEiKbDwaxZJ9JCYxo1UWwUwSFgs5PyhcPtJEjH_HdcyOMMt00pcx4IAU4CBvOzoOuwma2Q48yMUOGLH0WxbiJLOGroa5gYlTdpB3p4Qgc4SJKAtMHTi1Mc4N7w952RrxVSf8fLZ8cpnlmutWCsLYpYkoJlJCI5JQIjtNbdxPOF0aM4ITc4zO3dxRBDflRw8KtlTThUfpLy-iAxH5c1hfpXXCV-SxRR5c0Ze3jjAsGJZHd7jzzuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b585c6d4ad.mp4?token=b3BLAKFjxulIzSgGmIrPk-GH238kBH7itdCVeLjnBqAPYNTBYV47dxKFEUZGVzRKNbNc1d1C3z_mnoXaV7lr6tIJMyha-EusTLHDEiKbDwaxZJ9JCYxo1UWwUwSFgs5PyhcPtJEjH_HdcyOMMt00pcx4IAU4CBvOzoOuwma2Q48yMUOGLH0WxbiJLOGroa5gYlTdpB3p4Qgc4SJKAtMHTi1Mc4N7w952RrxVSf8fLZ8cpnlmutWCsLYpYkoJlJCI5JQIjtNbdxPOF0aM4ITc4zO3dxRBDflRw8KtlTThUfpLy-iAxH5c1hfpXXCV-SxRR5c0Ze3jjAsGJZHd7jzzuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع پیکر مطهر رهبر شهید انقلاب و شهدای خانواده ایشان بر روی دستان مردم عزادار در مسجد مقدس جمکران
@Farana</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/447793" target="_blank">📅 06:39 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

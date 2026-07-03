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
<img src="https://cdn4.telesco.pe/file/RphuTCfrxuxxe6lK-0EJ-_tqfcS_xT4QZ6cnUajj8RB4WSj2cLqX2mlmeFTMYkzS2Qisd8bmt1_IeHlbcGrLxjigrfNEvuaYQpdGvP3TNpwK7Gpbit6vnQjQNmMqNOwmblgTt3e7RqnTtgBovIbDkjXjdnSVaZ3G1-ND6_d5_jz-bIwtEOwwgVKjFPsXQLRrM-D5M-S6kLOInxOhWSXRblQEHu8ipkd_xzLRv0p-Vg5wv3cbHD2Ar6yJ60yjKUqLKAmkoF-G8exAyIZdl1UqZr-VEJzq6K9zk3npqgsY-zuXhlFMZ03ud4ywOwXnvUzpbYvrUPe0nWmMgqXpXqCaLw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.85M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 15:31:33</div>
<hr>

<div class="tg-post" id="msg-446279">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaef1c1112.mp4?token=uOCi7sjx7PYi9kWahkNQYlPg2jFhaiFbvhzjoNLEsr8_gh5uQXUdAh2-EmGfTpwusVXhaxtLqzzvkLa76eauhwmTK5rmooPCJGUhC08ID1nMuzdtt2fHnRwlILpel-uAsws58spJmGAhQZhKjjV4PvkM6kJgbFWRHNUdXefM5JwDNcTE5cG9_9Buxn64vpQEUnue4q1_qkAKPTOMsA-fdl-ME1Xy6gl3n_b7gGZLudOkjL2ir4PFpujaqO6gTqvqMc2odvraez18EG14G6vk4j0AuHanxVx_7f2IIK64VFFrXTbY4v5pr3pCBLWCwNVwkVl1WskP-kt5P8m-iowrSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaef1c1112.mp4?token=uOCi7sjx7PYi9kWahkNQYlPg2jFhaiFbvhzjoNLEsr8_gh5uQXUdAh2-EmGfTpwusVXhaxtLqzzvkLa76eauhwmTK5rmooPCJGUhC08ID1nMuzdtt2fHnRwlILpel-uAsws58spJmGAhQZhKjjV4PvkM6kJgbFWRHNUdXefM5JwDNcTE5cG9_9Buxn64vpQEUnue4q1_qkAKPTOMsA-fdl-ME1Xy6gl3n_b7gGZLudOkjL2ir4PFpujaqO6gTqvqMc2odvraez18EG14G6vk4j0AuHanxVx_7f2IIK64VFFrXTbY4v5pr3pCBLWCwNVwkVl1WskP-kt5P8m-iowrSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ستاد تشییع و وداع با رهبر شهید انقلاب: درهای مصلای تهران فردا از ساعت ۶ صبح به روی مردم باز خواهد شد
🔹
در صورت فراهم‌شدن امکان بازگشایی درهای مصلی از امشب، اطلاع‌رسانی لازم در این مورد انجام خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/farsna/446279" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446278">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda9a50f81.mp4?token=t1zXnpQd8PoSc_UIEnTsIxm22djQmGHAPoQrNrTADll5PwAs48z4blMHTeF-sdQ11_7m_Dr7ULiVMSLZU-0yartsXd-4LXITWRpe_h7AUmQM5RZeDUVtucta94bHSLvq_6ARDr1SgHwgcqlYi-54Rt4U3HufjgKCnKZrjuNNa9sSHs9-YMHsWggqaTmJiTkTnOFYHNw6qR6kyJgWg35CUGs6P2pFIe40h0Sq-qNRCtRDajeGWtCWCkBE9ZAnO3Hiqve-iAmhahaMxarVJweBsgT3JpgY5ISXAx6Mjb1e6lCp0gYTfh3xXu-GH5IoyY6_IhzIk6cjNE9fhWpduCVhEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda9a50f81.mp4?token=t1zXnpQd8PoSc_UIEnTsIxm22djQmGHAPoQrNrTADll5PwAs48z4blMHTeF-sdQ11_7m_Dr7ULiVMSLZU-0yartsXd-4LXITWRpe_h7AUmQM5RZeDUVtucta94bHSLvq_6ARDr1SgHwgcqlYi-54Rt4U3HufjgKCnKZrjuNNa9sSHs9-YMHsWggqaTmJiTkTnOFYHNw6qR6kyJgWg35CUGs6P2pFIe40h0Sq-qNRCtRDajeGWtCWCkBE9ZAnO3Hiqve-iAmhahaMxarVJweBsgT3JpgY5ISXAx6Mjb1e6lCp0gYTfh3xXu-GH5IoyY6_IhzIk6cjNE9fhWpduCVhEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راهنمای اسکان و پارکینگ مراسم تشییع رهبر شهید در تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/farsna/446278" target="_blank">📅 15:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446277">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1UZqD2Jq_dxbkC7j3YuiQLw1rxq6FoJ09tvnM2DAJk4gVJQ6yz1egNHJrybiIbjGZ4Ho9kt8VdGTsNL5mUkXM3e2YIu-65MbnvYlGU30Z6angCt7SlPcxu6k8YMeZD99PsgrhBQVlXTKypDc-7dR8rcLuIaQTsujoP_y1qLI-llJD25-nesrMq79ckroICqpmQFXZjpTRwGfaxj98oz29AJ4XqxKYin1Zjt0QWjEiIwoT-urhJG_2Z0t7_h4aXYifruvjGItUIfNDrPcj6bNIWgfpgSYQWr-B7UD5WfE-UE0hAOd-KmId5TMxRO2psTYeERIJ1K7DfSlqXmMqJQaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعطیلی ۴ روزهٔ اتحادیه‌های صنفی تهران
🔹
رئیس اتاق اصناف تهران: با توجه به ابلاغیهٔ رسمی دولت برای برگزاری مراسم وداع و تشییع پیکر مطهر رهبر شهید انقلاب، اتاق اصناف تهران و کلیهٔ اتحادیه‌های صنفی پایتخت از روز شنبه تا سه‌شنبه تعطیل خواهند بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/farsna/446277" target="_blank">📅 15:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446276">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7de078a47.mp4?token=Y6Zbl6AmcVwF8CMd8vdQJE72EE4oYOkv-dVj1Brxi1BAXFtmkRIfxcR4xqrbeMVbxd6wExJvWVmak04MhXJ7xLabWX29Xzu8AD_Kt8uijkD3Yh3FLFaLfJ5Fie66KVxSHmJuq9eKJM0ynhqcHBw9jLevk1baZweOnrqfdfBAV8uxY9PjYC8qTr4kZGAHQ8RYRITkgGlpMrIU1TD0Tt5-TO3_SWbLFOUHXf-xGnAbhi7HHZRgZ5hUqg-VN8T4rfdne7MetS9r89JgLwj9lny9kHzQtUO0LHSrVSsUeyt8TY6jiMNMAgEU05YMVmiuaDcgPrQIGtYIzfXc5kdDHmj34g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7de078a47.mp4?token=Y6Zbl6AmcVwF8CMd8vdQJE72EE4oYOkv-dVj1Brxi1BAXFtmkRIfxcR4xqrbeMVbxd6wExJvWVmak04MhXJ7xLabWX29Xzu8AD_Kt8uijkD3Yh3FLFaLfJ5Fie66KVxSHmJuq9eKJM0ynhqcHBw9jLevk1baZweOnrqfdfBAV8uxY9PjYC8qTr4kZGAHQ8RYRITkgGlpMrIU1TD0Tt5-TO3_SWbLFOUHXf-xGnAbhi7HHZRgZ5hUqg-VN8T4rfdne7MetS9r89JgLwj9lny9kHzQtUO0LHSrVSsUeyt8TY6jiMNMAgEU05YMVmiuaDcgPrQIGtYIzfXc5kdDHmj34g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام رئیس مجلس قرقیزستان به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/farsna/446276" target="_blank">📅 15:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446275">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5933555f6f.mp4?token=HqmUj8CnXgAkaoD06-Uj3DwEzGvhul13i_wWPFvoUwBrGZ4F7af4OKhTWvXv2Y5BuDhpK70Xc6fTug0qC30b88hadPwPehLIyeu1o66Mdvo6qy4-WzuaUPdSO2mq5YVOnSoivPR7ODxBD0n1g_Ig9blS9GDRYn3ApbYDoxnXLj6td3atmtalo-iEBy4KZd2Y2B7Tm-MMMsiheUAim1ci4Fuh2wg4uZPZmM3uc_sK8lThUFy79SuBMQDevou3cUjoW1yckV84d1jTIkKll1_gek4_RSD6UHamww6Z7RJWfxdWmxVu9begBbxpd1PoWsQpVgsMWJrf4ho0LEZjpYlRIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5933555f6f.mp4?token=HqmUj8CnXgAkaoD06-Uj3DwEzGvhul13i_wWPFvoUwBrGZ4F7af4OKhTWvXv2Y5BuDhpK70Xc6fTug0qC30b88hadPwPehLIyeu1o66Mdvo6qy4-WzuaUPdSO2mq5YVOnSoivPR7ODxBD0n1g_Ig9blS9GDRYn3ApbYDoxnXLj6td3atmtalo-iEBy4KZd2Y2B7Tm-MMMsiheUAim1ci4Fuh2wg4uZPZmM3uc_sK8lThUFy79SuBMQDevou3cUjoW1yckV84d1jTIkKll1_gek4_RSD6UHamww6Z7RJWfxdWmxVu9begBbxpd1PoWsQpVgsMWJrf4ho0LEZjpYlRIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام رئیس مجلس ازبکستان به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/farsna/446275" target="_blank">📅 15:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446274">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbcf4154ba.mp4?token=r4fHj2JL5TrcSYmR57hanqeQykmx2iGIRRqPKN3QZ8fCpeSZGnCYhdmplXDUxnhFjWrjJSif9EAO6zfJ1pMmwQsQCULEAnLVDr1pJWplbILr2w1OdzI6VfrfQkdLFoGrWG854CBj_gTgPo8rKVY1pPoVW7cLHQOczD5ujbn_tNxe8BCUl8gG41OhzpcuTLajsPPBROmvkKFPXLuxneFDM1wE-mwpZztkmCqjX8315yQB8NOnjuj4puTg_r_zjaWgpX7N6lK1rArsUfFQv_mLSzH9NUnfIUzNX8WnOR7NnLUK0-7XIxPKihP6V1GGwfky09mjxGPxJTvJZzbr9tD6gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbcf4154ba.mp4?token=r4fHj2JL5TrcSYmR57hanqeQykmx2iGIRRqPKN3QZ8fCpeSZGnCYhdmplXDUxnhFjWrjJSif9EAO6zfJ1pMmwQsQCULEAnLVDr1pJWplbILr2w1OdzI6VfrfQkdLFoGrWG854CBj_gTgPo8rKVY1pPoVW7cLHQOczD5ujbn_tNxe8BCUl8gG41OhzpcuTLajsPPBROmvkKFPXLuxneFDM1wE-mwpZztkmCqjX8315yQB8NOnjuj4puTg_r_zjaWgpX7N6lK1rArsUfFQv_mLSzH9NUnfIUzNX8WnOR7NnLUK0-7XIxPKihP6V1GGwfky09mjxGPxJTvJZzbr9tD6gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام رئیس منطقۀ کردستان عراق به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/farsna/446274" target="_blank">📅 15:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446272">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14db9faf02.mp4?token=P-LcBC1lV7Fmi6nbNm1IMJS8ys6QXzaUT_VXjn3IX0ObRL2Sm2GuhNx4T6khzc9Jpz8OxJQoETq7CDe69zNGJ0PPMHuWr-s8aCWUs6FOIjo7oifc6RHQv-CojihmsaN556tg6LBV1jhkyO5wSB-upy13OHx6PuYiNqcTz8KAoq-XPzzzLOkeywD4qWXOJPdZVitZuiTT3KJ1zNLxkAll9MTqlkwUqB0WcQnDm6P18eQtGp81FoZ1zHW5-70kNr1Xo-iZTPWDaIbB-BTUZ1a7yjoBpNqN3qVE-0877Av0t-S4znNYXgY2GnqPImLeXQfln7uTVIgZBMqGHk5p8Z-6hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14db9faf02.mp4?token=P-LcBC1lV7Fmi6nbNm1IMJS8ys6QXzaUT_VXjn3IX0ObRL2Sm2GuhNx4T6khzc9Jpz8OxJQoETq7CDe69zNGJ0PPMHuWr-s8aCWUs6FOIjo7oifc6RHQv-CojihmsaN556tg6LBV1jhkyO5wSB-upy13OHx6PuYiNqcTz8KAoq-XPzzzLOkeywD4qWXOJPdZVitZuiTT3KJ1zNLxkAll9MTqlkwUqB0WcQnDm6P18eQtGp81FoZ1zHW5-70kNr1Xo-iZTPWDaIbB-BTUZ1a7yjoBpNqN3qVE-0877Av0t-S4znNYXgY2GnqPImLeXQfln7uTVIgZBMqGHk5p8Z-6hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیدهادی خامنه‌ای برادر رهبر شهید انقلاب: شهادت مناسب‌ترین دستمزد ایشان بود
.
@Farsna</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/farsna/446272" target="_blank">📅 15:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446271">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7585a8203f.mp4?token=WzdGoFDZxnY67f9KAQ-c9SD2kFfpmHFoQT7uA797CiKkbXNcXG9FVZ9at1F4Y3vmDC04Mj8sChKfMKPs073ikmKkvcrZmfhWXJiSk-UF5mVbJoEzvKXBh65VOP1TxE_m7qzlwTzXvMcOcHCKNjXxh26xeHwvER6Z21XQeSAmZk2MQoSsoI9sMXy4AF6TImdhEt79b3neadXwLkfoY0PKb-lVGC9SkI2XcOBRISCeh1G0rTDqNzTtX8YyOZaVFsW1-bSEZNH_iM8yiogxWZrCwEGff7q-of1bSsW365qGdPnr-9ymamCcpv7XqPc7yvGccsjwpEYcl4YUDrfUfzL5cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7585a8203f.mp4?token=WzdGoFDZxnY67f9KAQ-c9SD2kFfpmHFoQT7uA797CiKkbXNcXG9FVZ9at1F4Y3vmDC04Mj8sChKfMKPs073ikmKkvcrZmfhWXJiSk-UF5mVbJoEzvKXBh65VOP1TxE_m7qzlwTzXvMcOcHCKNjXxh26xeHwvER6Z21XQeSAmZk2MQoSsoI9sMXy4AF6TImdhEt79b3neadXwLkfoY0PKb-lVGC9SkI2XcOBRISCeh1G0rTDqNzTtX8YyOZaVFsW1-bSEZNH_iM8yiogxWZrCwEGff7q-of1bSsW365qGdPnr-9ymamCcpv7XqPc7yvGccsjwpEYcl4YUDrfUfzL5cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام نخست‌وزیر و فرمانده ارتش پاکستان به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/farsna/446271" target="_blank">📅 15:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446270">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c32121a1ae.mp4?token=IV_z132mLv0LxtS67EaXBaudFiWP33JqHOt51RCXVJL9WrYaYIY5Ktf31OvLOTDlY0_Z8XCH2Z9n5tkrWBuBviw2ktpUUwqWheJBxb3ZO2tmhP8nEu3yDNfmxw5k7uU9RGbpxtzrdapPKPQcW2wX23_TKL0HYrd5PpWLNDSzg6o0yQd1SOTsOvSDlmX0An0fT0gof7RezEkqDfJ_FKkypfCVrjMnjOYf9yG3GPfBcEKadV-d0tFuqmMs0QXBgIp29KihnDOZKD2E1IbunpcZNl6ANzVYIUhShzYNzk050a25tSHq-GgTLIMJei3ugVReaIFPFzwOf85YoKfiswZrMYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c32121a1ae.mp4?token=IV_z132mLv0LxtS67EaXBaudFiWP33JqHOt51RCXVJL9WrYaYIY5Ktf31OvLOTDlY0_Z8XCH2Z9n5tkrWBuBviw2ktpUUwqWheJBxb3ZO2tmhP8nEu3yDNfmxw5k7uU9RGbpxtzrdapPKPQcW2wX23_TKL0HYrd5PpWLNDSzg6o0yQd1SOTsOvSDlmX0An0fT0gof7RezEkqDfJ_FKkypfCVrjMnjOYf9yG3GPfBcEKadV-d0tFuqmMs0QXBgIp29KihnDOZKD2E1IbunpcZNl6ANzVYIUhShzYNzk050a25tSHq-GgTLIMJei3ugVReaIFPFzwOf85YoKfiswZrMYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کدام هیئت‌های خارجی تا ظهر امروز برای وداع با رهبر شهید وارد تهران شدند؟
@Farsna</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/farsna/446270" target="_blank">📅 15:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446269">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca3e80ab3.mp4?token=sdiTEreg0dAzmO_cGyHARoAg-e11MJKwLNWTkpRmzn1xqpNhRKxpX3cbLswjR5gXDlAQWH74uxxrL7o3Ws0EVXkUqKlupUIvUV1aVO2PRy7OTPyHMQ7fSgWDLv_wlgDjpjQdfwfwopvmifPh0JQ6G3erBrdI0R0fy7ZOvQ4GlJK2NuW4fNACuVHmLDZ2AE1soxKOXJ05BBBT99jXvV-AasK2uLBQSv9OnsNv_FQx5U50v__yEDAHF-N0YhjAhEP2vqV85ZBgHASPzQeIRAil2pH5mAIOQXyiE0JvUxe8EgHIKYOW-gaEqSQaSKwvVbPqXm1kbCYrDRCrsDFBmjZYow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca3e80ab3.mp4?token=sdiTEreg0dAzmO_cGyHARoAg-e11MJKwLNWTkpRmzn1xqpNhRKxpX3cbLswjR5gXDlAQWH74uxxrL7o3Ws0EVXkUqKlupUIvUV1aVO2PRy7OTPyHMQ7fSgWDLv_wlgDjpjQdfwfwopvmifPh0JQ6G3erBrdI0R0fy7ZOvQ4GlJK2NuW4fNACuVHmLDZ2AE1soxKOXJ05BBBT99jXvV-AasK2uLBQSv9OnsNv_FQx5U50v__yEDAHF-N0YhjAhEP2vqV85ZBgHASPzQeIRAil2pH5mAIOQXyiE0JvUxe8EgHIKYOW-gaEqSQaSKwvVbPqXm1kbCYrDRCrsDFBmjZYow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا گریه می‌کنی؟
@Farsna</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/farsna/446269" target="_blank">📅 15:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446267">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M2XUPrewS2Fu9JOAsNh-ncO_UT-fo8fxpm9lEIt75XYWEKMOfjvwLS5J3__fMiTjtlOvlfcMW7_qVP3wQEIQlo2voJpUB42BP4017jL4d6SIXTUE0TjNBNOfF8361EP2Did5p_qBvc2Ty6rH3O7P8fUx1AX5V0ajKYZwmr21MGvKnTifE0GvDfylog-BnpAgOg-Mbvy_RSAxgt7YO9uMRQPniOQoI2ZLRGaRbuUNK1UMde2Q4PL55o-faQ80tjD8xtNDP2L2zvSv6OMmXnuNdwoXdoXcjA00b2uRDkPBJJrjdTorSdufYi0VzgAUa3X4v6IdtY9hcYLQD-9A--VXyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ixj19rfk0pT1z1fe1RqvT3m6elmMUC36LAQ3-szIzinSvNQG4n5CMfh1hMZc2M4061WHQ9ZYPDl2yJ5WjqN-C1utw9QbkiRQofxFTETzxJZmnZleYExXrtIltN489KhmnCgt9tDYW15rRyWVGqhyrnCUWjWy9gzF39yHHJ7y-gcheFLPaf3qfjozZltj0gC17u7GBaEfmLjBRrWck8pbhNdeQWPn6ycTrciHcLHMQ8GPqQqa9vLQ_z15x4yZpezIPYvZIh1KDr-VcIAkJzvBbritO4-4ZZL0i32VnIZhOCGkmCf4Lr1LJwHkCVegdypU8J90NGQyxgTJ7l2tRxud8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور علمای اهل سنت برای مراسم وداع با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/farsna/446267" target="_blank">📅 15:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446266">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2af14934df.mp4?token=Ald5H5Zco9A1A_sX7lDTNV8wG824eduAbCARaxyRvy4AbYZk-jXHwg6d9Te_y6FVNkSgtcJPnzOpeAjGkeXIdqxVcJPJ6Dzp9Q_Ou5aMak84sYmvJREU5S_p_oVfOe357zA7uEy4r8Uud6EemxH_uYUZmOmMV_EKh7hsLKyUwE_CuCfbXntliYEuM6TqQ-9YLnvvulF6L9C9YryrHeWEqvJOCSXUF5jyOHJMJYNPYfO6QrPcctK4hHUQrgNZs03qKCKcPbt0KRj6IHqZo1jK-Y1fBTq9royu9am51G5xjtg02owvSLCbBuco2NkJiM0FwrMi8UkpPgegyJNDdC8NEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2af14934df.mp4?token=Ald5H5Zco9A1A_sX7lDTNV8wG824eduAbCARaxyRvy4AbYZk-jXHwg6d9Te_y6FVNkSgtcJPnzOpeAjGkeXIdqxVcJPJ6Dzp9Q_Ou5aMak84sYmvJREU5S_p_oVfOe357zA7uEy4r8Uud6EemxH_uYUZmOmMV_EKh7hsLKyUwE_CuCfbXntliYEuM6TqQ-9YLnvvulF6L9C9YryrHeWEqvJOCSXUF5jyOHJMJYNPYfO6QrPcctK4hHUQrgNZs03qKCKcPbt0KRj6IHqZo1jK-Y1fBTq9royu9am51G5xjtg02owvSLCbBuco2NkJiM0FwrMi8UkpPgegyJNDdC8NEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قابی که اشک فیلم‌بردار حسینیهٔ امام خمینی(ره) را درآورد
@Farsna</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/farsna/446266" target="_blank">📅 15:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446265">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514a7a3b42.mp4?token=WUL8RyUFWMVv18SlL3Xu2K9p2Ea_gCpRXfsuC3_fmOL91MhLnnThqCCtMGQqf9QGe2Lbuolsui0ao_Qz3i837_H7P15SvukwfGt4PdPVMWcxKWwp7i6xyjtA-MTNjeeAUuuCp-FrY6WpEBO9mBp9D-JNHYU1CquxXj_boWcUl1_suIeKYVh2WjJ7_v4c8PfS6J9im3KOaXeV49B_0uAdvTwJ23cVGAdpRSbk4hOkceQ99kJLPp17mxdzO47A0xLhxMKQcxa4x0RntznVDnoZuj_EZXbtTLk_IHILTLh9tRoW3yi3tuXcLAJOI8rkIuphXXCaDHWhFbNDyhc0-H-MqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514a7a3b42.mp4?token=WUL8RyUFWMVv18SlL3Xu2K9p2Ea_gCpRXfsuC3_fmOL91MhLnnThqCCtMGQqf9QGe2Lbuolsui0ao_Qz3i837_H7P15SvukwfGt4PdPVMWcxKWwp7i6xyjtA-MTNjeeAUuuCp-FrY6WpEBO9mBp9D-JNHYU1CquxXj_boWcUl1_suIeKYVh2WjJ7_v4c8PfS6J9im3KOaXeV49B_0uAdvTwJ23cVGAdpRSbk4hOkceQ99kJLPp17mxdzO47A0xLhxMKQcxa4x0RntznVDnoZuj_EZXbtTLk_IHILTLh9tRoW3yi3tuXcLAJOI8rkIuphXXCaDHWhFbNDyhc0-H-MqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام رئیس‌جمهور تاجیکستان به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/farsna/446265" target="_blank">📅 14:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446258">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m-wV5vkg5_YM50MS8KzqexEE5xUQt9WcokkBbMAEJnkTmKdr8ga_EBdUJKxXdjkRcvJqiJ6Pesk6tP51TU-UtjYoOr4QaU4RIeHJyI9Rw9AUYn5pYSNm-FXYnz0tEfhoMQsIQg_BkRektOUmEz0sxPrj8wzqI40qr8n9cEGk5N-gWVeB_d3NiENaBKrsaDA7WW_xwG7YQbKpuByKOYx6vMwVO0rayHfzXqRQP0hoThLpMafbSrZBbfyU_tgBM-7gbP_Qc5r7VX2p0ZT5TEBifAlnEYkXWSNs6Efor5c9UEPVD0v8o81N_MYa5T31HAoh8WkgJKRSSzwvOuTuWnKRxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E9lgN8OPu8Kx_Mg4syZJT4EiYFUyh5Kl0HUinu3myiIOyA4RUhITrKmVGOpJ2NWYgRjoVISOGghzmz1_A43P2uP705pmJt1-NIRDPWIpuPIF7kax_cMJ7kvKEi4yfyqKZ39St6pyH6JHIaVzLXTDzRRxN-WO39si6mTwbUqK5btEA2gTGmDXU5mutlxTgcVUBoQHSGjEg2yXAWv65gyUIGV7UipqW3ew264sl6Ed_91wsCyju9g4nAiRlskSiXuF2s8edDpuEdXnx7svuk148zYHmcVakudbnkhapgX-uclMopJtjushElpFnBXwLbpDPPd82EAb4eAmtKXrcS5NmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WxQaTUoR9zrCw59CAdDgXki4m4dgmIlWIfbEmUO4x6Y5WgItKLXBiqRAqYBdcF4d8g3j1RXoGQoDIaIqdbH4noTgmt40HBZWNWkh1hVcJ2Zi5yEy8Jm-JX9Ha1W6SPjn6nJnscoeEP5hURyJpGLhzzq7AKfWVR0vTBbIELksXGT0rbo06n4wI9vQvFFN1emPoWohx1IY56wGm0p1z2HyUG4x2UYfI8Q5oJjz4tkN8IEpBICfIgqmJ4RP9daUiiMtLI6OWz43oRAc_l5vFm99OT_CcbqW_0ajBW1LAbVdkecYuSCJZxnfoe0TOATuXjD9Zy0ZfP53zslZaVNj2MivuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ev_ka1XTESuGq4L0rQvKpNnHBjRuo1lceq86u13QzbQwkUTOFagfAthQK-3crKvf-SpOzecbneaofF3P0hfzyTBInWKPh7CjHWTu_3In-K-pgVBX4XkzbA_c7UAYHGqpBiAa86Y9F_pRhm878LrNl1ZieDC1U13mfz669QVSxn9Owbxc2dUHEJAzzFC0vnW57n9rWC27dVyvVofghx-8iIY3Up0weo9pJaIYstKXEl4YYMBqQSjLDofqbmJ9Vhf9OPiAmkRB-J_z20PbtXAh6VJGch0gucfbHPhuuqafZ6inxLZYGM2kUElESIxWOulfICY30rN5C-6z8F11ct6kCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXqs-1UQWjncq3O9uXhDRLAG6fPjwTms5luRv28336zbFKg8y0bJ7TB10yUb9SZHO39NISGUtTDMhVIBBtVBy6NkhkczV3sMgwnpiqZXCleJ2n4DqnZ8kqEYX4m_HsCIeuJ7ly-ZvdwbvyFRRx9Pd7RDy2w2qHTuTgFlkTerpBisU91vMbOJqu5Yc4OJoKYzfg42C4JohOgAl1lx9RbjTUutb1fn7cW52DC7BmpE6cprJY0brIRGMU4bGo8RuOMZZJgE5vpFZ2WGEgfSGkIvWEPIQk0c2UhmsJuwQfdWv2spp0YE8FErchff4KXnDm42VkvJ4loibClLrCVkLTRRig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oKpQbrODmbymLJaKH4WT891Z29JE_jjc0spGcjOKj9m0iIZFbi5z-DGiuPTU83Jip3CQkCoqDiVrF6fUtTZeJaaUCMoamqMLfI4h9iLoCP4PmCgqt8ffQ2F-kcsKWr9fC94Ob2fBaCQIgIys2NPk9rmk9izcrQmGGFW9SErqCrTbRldW-W7iMbKdLdY5jplQQ0Xgx5Gia_-kPuhhv02vXsI6XPM2KvvwSXpHDcscxGERMcAf8Cz5BU3vIKSSRNZSxrlaKOP5WpJIleXpXz8k1dItAvH0_E3J6ANvn33BQPK-5zwvNzjS2-Nmt7xDCaQ1Lo3AeR7YwI3Qi30fpMOIRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i2n8It_GGEHE5IPtdemAOysee8_2DAuSg1KvXmPr9EySWvaY9zzCwpPArOp3hpbRis9c6-1w-J2iz6rYe0hsFQUB7a1s0OKX3QaADg-v8e4xdSP63gI1lboPU2l5i-uKvCI666ff9ijC1DYnaPZ_bDseKt2jEcvreHyc61hjNblKipIZ08JKpfT-JLDgR1jN2vlQ51CMOtrKVeH_F5igmP8qUOcGZREW27SGq7x4rBc4-20vjEipOmRg-IGjUPsc5JRE63Ieedbn_SKdYd63s-UUiXnvxR-uxxlCg9n51lO5h5i5M1zQhzvySOuZ7k_prc0_p5k76ZQhFg-zINYTDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ادای احترام سران قوا و مسئولان ارشد کشور به پیکر مطهر امام شهید
عکس:
زینب حمزه لویی
@farsna</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/farsna/446258" target="_blank">📅 14:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446257">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtM9LjmOmww6v_ShYtbNwQhk1iUUZ00pckIGBZwtlruuaE3IGOf0q5ubRG7PhmUYcLJX3yQ7hvBaSAeowfq8NBis17JPrMFm2COOz8FTmUub-OxlIwRJFJIFLp8qlZbUlfy_uAOK_1h-OLZL0EcgyBeDRh4bFd4J5UzCwaBqut7qXGBiwHggAH0F-9J9U8OYHWv64ySR5VEmOx0NQz3Px598yHXUhTL8XUl5MBEyZe_ZWZMzzx_TXxaA-KsKFgr9S7xYWFihfFvNSDvm-CFEngkAKb1cXKvrXF6OWptpf3eGX7P1-TDc43GrxnThqoSRD819RuUUG0lA-JSNwHjxkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دست‌نوشته‌ شهید مصباح‌الهدی باقری برای آقای شهید ایران
🔹
یا سیدنا القائد؛ به وجود پر از مهر و صفایت می‌نازم...
🔸
شهید مصباح‌الهدی باقری‌کنی، داماد رهبر شهید انقلاب، اسلامی در آغاز جنگ تحمیلی اخیر، همراه رهبر شهید بر اثر حمله جنایت‌کارانه‌ی آمریکا و اسرائیل…</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/farsna/446257" target="_blank">📅 14:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446255">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utyb80hlIv6o21Szy8Bu2GHRNPT56VClQAzVCn3tCNwxocmJbfZ_I2K112-PFTqDu2ksLblt7UwlvwLqvjfsGopYMiNL0q3KaLplHDRB961Lusdh_1y8e5eT5f_olCctr45ay2DpxzKgLCckdUBjpzpFTLCqoXsKgy12XrLE1-dJQkC3OUonvaVHcU_xR8jQbNftzpziSTMEp2Nuu0YHU12hMSToCo17aiVWS2BY4T95M7RfD24GzvYbDIpmggwqG3VATqlcJb6DWzX3TFAhHR62gXplx6KEJVbja-bpuJZSqocu-NbySN-qPV_RWckzmN9guE4Cpwbgw-QUMyxhmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
یادبود بچه‌های مظلوم میناب در ورودی سالن ادای احترام مقامات کشورهای خارجی به پیکر مطهر رهبر شهید انقلاب در مصلای تهران
@Farsna</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/farsna/446255" target="_blank">📅 14:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446254">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e695d4c345.mp4?token=TkwZjksx5r7hPzOe2alAPYbwAmB3o67hfMciAUNBgwSMA11P0GMsP7ATJf3NEK8uDdCYj5rkLyDcTBRucmUg0eXK12uarPPTU2IC1I3bSoz9MHzJGFHRWMPpKr6OV6EgdszeK8IqCnD0gy7ZOKG_k-aLSzkSwRAa5Lfs-jtlPmu0-58RGqK4yIT-XYgcFbJjg0JIoHtOEEKEXiM7HOOa3p-p4-wC5Z74QspLBplx-ZTg_jP6FFfF0rFg4ba3cW8XBGSWNyETaOROjPWi7Y60qTXvlRiRDxSt7qOqs2oNZZ6SU7nevv4T2uaIdV79BuLAwO2SAYDifgOZhP6jz6Ex8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e695d4c345.mp4?token=TkwZjksx5r7hPzOe2alAPYbwAmB3o67hfMciAUNBgwSMA11P0GMsP7ATJf3NEK8uDdCYj5rkLyDcTBRucmUg0eXK12uarPPTU2IC1I3bSoz9MHzJGFHRWMPpKr6OV6EgdszeK8IqCnD0gy7ZOKG_k-aLSzkSwRAa5Lfs-jtlPmu0-58RGqK4yIT-XYgcFbJjg0JIoHtOEEKEXiM7HOOa3p-p4-wC5Z74QspLBplx-ZTg_jP6FFfF0rFg4ba3cW8XBGSWNyETaOROjPWi7Y60qTXvlRiRDxSt7qOqs2oNZZ6SU7nevv4T2uaIdV79BuLAwO2SAYDifgOZhP6jz6Ex8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجسمه مشت گره‌کرده رهبر شهید در میدان انقلاب نصب شد
@Fars_plus</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/446254" target="_blank">📅 14:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446253">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fa6057f04.mp4?token=I3kYSK88Mrtsk4Con9u51n64iP3NdJFVlaJQ8pe7jlgg8L9M_QFsdkedeIXKRDOdmsMTBqWkSOL-CZOLXsQrWSsUvuxqdHvDAczoe4rqfp-wEYnJL53f-vzLke-cl2GjFOh1YrSR_YnZOXgi3ZgK9_oJMAA1RCtpG7pkJY-WHkOvoKutX7uMhJZox49EDfHTNhJFZEBnLDhe5inRrZow34IuJNE1OOpBKIUusAYELlIEjQu7Bmvj8X0Jysbr4ClLcqoeDGjAewKiuk3RV7CCtMdJOoyJlBAYwLDx0PTLKZt6IRr1WmodPZyoLTfBFuj1gsoqHI1SPZeoJuRH_SX3gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fa6057f04.mp4?token=I3kYSK88Mrtsk4Con9u51n64iP3NdJFVlaJQ8pe7jlgg8L9M_QFsdkedeIXKRDOdmsMTBqWkSOL-CZOLXsQrWSsUvuxqdHvDAczoe4rqfp-wEYnJL53f-vzLke-cl2GjFOh1YrSR_YnZOXgi3ZgK9_oJMAA1RCtpG7pkJY-WHkOvoKutX7uMhJZox49EDfHTNhJFZEBnLDhe5inRrZow34IuJNE1OOpBKIUusAYELlIEjQu7Bmvj8X0Jysbr4ClLcqoeDGjAewKiuk3RV7CCtMdJOoyJlBAYwLDx0PTLKZt6IRr1WmodPZyoLTfBFuj1gsoqHI1SPZeoJuRH_SX3gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام رئیس مجلس بلاروس به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/446253" target="_blank">📅 14:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446252">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caae8012d4.mp4?token=Qy2dyY6NVeggtj7Lcnb6KZ66UT5LVnbJ0PqVirwtVAYNETVXzRLcjyTFtQTMNqycrCSR_c8PHtVQR9qnj9NAR7kAk1BhoI3jc3M3f9fTcyfUyTV_hgVthjT0QXQZXvrYo0pqF6IqcwIij-9DboFfnLDFsBjtr0N_oQAPmlIdOHfIXnom5jBakxG5JabiQkfJrlCMf5DM2Qt498G4AvbmNdU1GEANJY7QKZF7Dl0LD1YwgIZ3nNUlhkGgcizlUWCQUY-n09xnlHkD7hQlZy8TgAURQWJr8X1QRroGOw_T-0pd54rcqwes28sXiUz_035ulmRp5cIwWx8f1zMGSYT8nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caae8012d4.mp4?token=Qy2dyY6NVeggtj7Lcnb6KZ66UT5LVnbJ0PqVirwtVAYNETVXzRLcjyTFtQTMNqycrCSR_c8PHtVQR9qnj9NAR7kAk1BhoI3jc3M3f9fTcyfUyTV_hgVthjT0QXQZXvrYo0pqF6IqcwIij-9DboFfnLDFsBjtr0N_oQAPmlIdOHfIXnom5jBakxG5JabiQkfJrlCMf5DM2Qt498G4AvbmNdU1GEANJY7QKZF7Dl0LD1YwgIZ3nNUlhkGgcizlUWCQUY-n09xnlHkD7hQlZy8TgAURQWJr8X1QRroGOw_T-0pd54rcqwes28sXiUz_035ulmRp5cIwWx8f1zMGSYT8nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام نخست‌وزیر ارمنستان به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/446252" target="_blank">📅 14:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446251">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08e418570b.mp4?token=fmOCpKbEMvCOryCNPqiSUs_vBDagDwWKyg9lb-RJp1jWi6L22qDY745KD4TzZCIv2b0Agx5jKwE6lcg1VB9HpD158-0r7gSh_sBRs113UaWsI87Dc61HtLJvmchXm0xCa-eLaiFB8CjcQzGaYNBQBhvbQ2XlRJIqoh0WRm5A3iIPH-A8DkVpcDJ3jdCdddxZr98imQVlkUxmdWu3x0qRaq-7HTi2tQTFR45OMeVwc6ywjFPO9tHcrz-DITQQ5wcWdHB_ksn5Zs6AOoebsF7bFC3vgBlfNDt2Q4a2uC67Zc_mMqSDfORJPXk1zBJwxF0hTB--NkIg1lFB8wCElfy9-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08e418570b.mp4?token=fmOCpKbEMvCOryCNPqiSUs_vBDagDwWKyg9lb-RJp1jWi6L22qDY745KD4TzZCIv2b0Agx5jKwE6lcg1VB9HpD158-0r7gSh_sBRs113UaWsI87Dc61HtLJvmchXm0xCa-eLaiFB8CjcQzGaYNBQBhvbQ2XlRJIqoh0WRm5A3iIPH-A8DkVpcDJ3jdCdddxZr98imQVlkUxmdWu3x0qRaq-7HTi2tQTFR45OMeVwc6ywjFPO9tHcrz-DITQQ5wcWdHB_ksn5Zs6AOoebsF7bFC3vgBlfNDt2Q4a2uC67Zc_mMqSDfORJPXk1zBJwxF0hTB--NkIg1lFB8wCElfy9-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام رئیس مجلس جمهوری آذربایجان به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/446251" target="_blank">📅 14:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446250">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41090b7f32.mp4?token=dSTnzA-R0uVzgH-AOdtzcE8gMFWXDvSCPI5sjAk17PVyzx81hpE_fGuj5d-ikDZpYS8S-aPunvTd7mgPgs1gDSZ7DRTrrIDgEKuw8G2_T8iuDWHQ3gPyb6YgQ7OA0N1T2l18RwBXL48FMimx-xPON6t6WYtYEglDdLYVps6IRx0pitAm1A5ffbh5SjctVWgyiqYT3_BLRIlpwedF5yp-qVpyJnEqKFubTp41r-_d07CxXzU_wmdfJFkEkekY9EyuemnZmgoY9o1Z4tgL9E3-wYBx1LHwmYFe_Cr6DqZLyeQXk2CnfWX2yBARJokclz0c6FWuzqL07td_hQkvlFA7tRB8jcIt8yaUB16MEt1q1X7on_KHksKb6BdvjPIqkUk2Fmz9Dlr5Hab-BLQfErsue8Hpy2Qo7Ac3VGLysfTUtMFLwNO-D4vt5DjVRkMIFuSNzgA9JUmqSDEsz50Dhkk7GzpF4wekO80C1ilhwblHZj-f4-ej1DowlwEeTumFUEJW9lDIDtxLECR399MsSx4rROy1cHV2uPW3A4um5Etstg0ICheUblOPj5RiRPO9g0ec49XiS-ghnQ8ONfvxeY-hjjbk2WVGI6i4Yv2UP51MXjFyPguUO_1A2V9IXwrqr_spx2RY-g-K0K8tp7-Qk3-JgIA4vDfx1quih9R5K8_FceU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41090b7f32.mp4?token=dSTnzA-R0uVzgH-AOdtzcE8gMFWXDvSCPI5sjAk17PVyzx81hpE_fGuj5d-ikDZpYS8S-aPunvTd7mgPgs1gDSZ7DRTrrIDgEKuw8G2_T8iuDWHQ3gPyb6YgQ7OA0N1T2l18RwBXL48FMimx-xPON6t6WYtYEglDdLYVps6IRx0pitAm1A5ffbh5SjctVWgyiqYT3_BLRIlpwedF5yp-qVpyJnEqKFubTp41r-_d07CxXzU_wmdfJFkEkekY9EyuemnZmgoY9o1Z4tgL9E3-wYBx1LHwmYFe_Cr6DqZLyeQXk2CnfWX2yBARJokclz0c6FWuzqL07td_hQkvlFA7tRB8jcIt8yaUB16MEt1q1X7on_KHksKb6BdvjPIqkUk2Fmz9Dlr5Hab-BLQfErsue8Hpy2Qo7Ac3VGLysfTUtMFLwNO-D4vt5DjVRkMIFuSNzgA9JUmqSDEsz50Dhkk7GzpF4wekO80C1ilhwblHZj-f4-ej1DowlwEeTumFUEJW9lDIDtxLECR399MsSx4rROy1cHV2uPW3A4um5Etstg0ICheUblOPj5RiRPO9g0ec49XiS-ghnQ8ONfvxeY-hjjbk2WVGI6i4Yv2UP51MXjFyPguUO_1A2V9IXwrqr_spx2RY-g-K0K8tp7-Qk3-JgIA4vDfx1quih9R5K8_FceU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">KHAMENEI.IR – باید برخاست</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/farsna/446250" target="_blank">📅 14:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446249">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18ab5e31a5.mp4?token=p6aNiolC_mQxdSvok5Ir41B67lFxnKqXkdUdvyc2jbO2oKTxCVhIMMRG4WLDCG73P8bsO7jtoA5A-fZARHbh686_GwPdaKUc_bGaPFkAYGbRa97kJTyAGFnv59GAZOPNzVOLzjPGiSKB1iX0cydix1IaNCBLylCRtST_m6gW8qjV7CqYANWu4xHNKUTXeueb5NOZjl88ZEMxiEXHnULiRnTTSwL03br78sVIRyg18X8fkNb0t4M4bnE5Vco77RVF1bfuE7zppndQGLQ770MOsS90o496z3QOhA4GHp5Z-5NVcehDbx0Zvpv1D8wZdyhFP2ZVjH9SzYjut9jTFi2_Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18ab5e31a5.mp4?token=p6aNiolC_mQxdSvok5Ir41B67lFxnKqXkdUdvyc2jbO2oKTxCVhIMMRG4WLDCG73P8bsO7jtoA5A-fZARHbh686_GwPdaKUc_bGaPFkAYGbRa97kJTyAGFnv59GAZOPNzVOLzjPGiSKB1iX0cydix1IaNCBLylCRtST_m6gW8qjV7CqYANWu4xHNKUTXeueb5NOZjl88ZEMxiEXHnULiRnTTSwL03br78sVIRyg18X8fkNb0t4M4bnE5Vco77RVF1bfuE7zppndQGLQ770MOsS90o496z3QOhA4GHp5Z-5NVcehDbx0Zvpv1D8wZdyhFP2ZVjH9SzYjut9jTFi2_Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیابان‌های تهران آمادۀ میزبانی از مراسم وداع با آقای شهید ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/farsna/446249" target="_blank">📅 14:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446248">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b6b839c64.mp4?token=KWcB9nKgQPIPS4UcrIpx2jqGVKY7XeaplhZoVUZReLlOqj4sA21UEsBryf6kIg-3O7Ep6AiUQHU1aR1sGl0L0fGjBf1Z2V-YTdp4lSdyPc1sv5dtLG3BUj-r93Kt-RWMgXDOAGwfwq-NikBm_T_zwoH59lnKdctoyczi1WDCS9M6NFuM2xRC23BLsu_iKC8aT8MulOzKoQ3ADMeC_QYYKYH5rxmoCQYtbdlJVi4VKsS1UtUJs-vJLXFAQyCMG00D5NY2uTKAHzDZLzH0QF5govfFu08PV2ugYx94wJ9PMaK0Nv2G1qs733ZlWDamHa5kXFo0A-9dKJjoWH7CEpK0Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b6b839c64.mp4?token=KWcB9nKgQPIPS4UcrIpx2jqGVKY7XeaplhZoVUZReLlOqj4sA21UEsBryf6kIg-3O7Ep6AiUQHU1aR1sGl0L0fGjBf1Z2V-YTdp4lSdyPc1sv5dtLG3BUj-r93Kt-RWMgXDOAGwfwq-NikBm_T_zwoH59lnKdctoyczi1WDCS9M6NFuM2xRC23BLsu_iKC8aT8MulOzKoQ3ADMeC_QYYKYH5rxmoCQYtbdlJVi4VKsS1UtUJs-vJLXFAQyCMG00D5NY2uTKAHzDZLzH0QF5govfFu08PV2ugYx94wJ9PMaK0Nv2G1qs733ZlWDamHa5kXFo0A-9dKJjoWH7CEpK0Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ستاد تشییع و وداع با رهبر شهید انقلاب: درهای مصلای تهران فردا از ساعت ۶ صبح به روی مردم باز خواهد شد
🔹
در صورت فراهم‌شدن امکان بازگشایی درهای مصلی از امشب، اطلاع‌رسانی لازم در این مورد انجام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/446248" target="_blank">📅 14:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446247">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5024157923.mp4?token=aoU2Y9EE7vPlJltiqeGEJbUc5lypJQaaJbZE1tgbYsSr6rjZ4iUIFQCKZYA0wGJcGsS39TCwx2eJfOQ-sIoS8d9uREDnpCcNsIE34FFmO8L21Mr6_cXj08xpNC6Rk_VIkkxt3lUq13Zbb_woesCOwu564p6wuIjT3yeY8Lh71JlHeQUQkWwRNfXEWG4xcKKIsh9eN6967Kb-m8tYc8KKlLfR9Kzq53jabocGny9PmRsKX20I_D59Kq1LEtvB8ktnuwaPifd9ylEoP-Z2nk3FgOZZB2JjtywU8sr-ObxvibsuNedXr50Xorm1SKUOaNlYGSHr4gsFSF3UtQAkcMQ1dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5024157923.mp4?token=aoU2Y9EE7vPlJltiqeGEJbUc5lypJQaaJbZE1tgbYsSr6rjZ4iUIFQCKZYA0wGJcGsS39TCwx2eJfOQ-sIoS8d9uREDnpCcNsIE34FFmO8L21Mr6_cXj08xpNC6Rk_VIkkxt3lUq13Zbb_woesCOwu564p6wuIjT3yeY8Lh71JlHeQUQkWwRNfXEWG4xcKKIsh9eN6967Kb-m8tYc8KKlLfR9Kzq53jabocGny9PmRsKX20I_D59Kq1LEtvB8ktnuwaPifd9ylEoP-Z2nk3FgOZZB2JjtywU8sr-ObxvibsuNedXr50Xorm1SKUOaNlYGSHr4gsFSF3UtQAkcMQ1dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام رئیس مجلس عراق به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/446247" target="_blank">📅 14:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446246">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">باید برخاست</div>
  <div class="tg-doc-extra">KHAMENEI.IR</div>
</div>
<a href="https://t.me/farsna/446246" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
قطعه موسیقی «باید برخاست»
موسیقی ویژۀ آئین بدرقۀ رهبر شهید انقلاب.
@Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/446246" target="_blank">📅 14:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446245">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2066c8005a.mp4?token=f_F-xVMdnCaZp7iyii6_NaggLoLM9HyTwWLimOTDNxUmHFM61Xy65yx3hi3IJivgqei5e0xJS7pqviqodhp4ml73WFv06OQIeNNs4M5_FQ690t2bRDb4A08a5jomqap6_fllUHx3TsCzSgnIhOYgmU9vTboDM3E1WVI7jLagZBAWeMFxeF_RuL0yxdGw7qNt2-KYpj3q3d_op_ttTyDt13i1hjKtjyqazocOVb44_4s_lPJbVoEU6xe7eL9bYEKm15Mwjl95f8SA3xmQd8T8NICIvpPWUWXD---3wDQMU6_Vak31asoITohDdT0dGi0he7QQvMoiRSV7q2iA0OA1MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2066c8005a.mp4?token=f_F-xVMdnCaZp7iyii6_NaggLoLM9HyTwWLimOTDNxUmHFM61Xy65yx3hi3IJivgqei5e0xJS7pqviqodhp4ml73WFv06OQIeNNs4M5_FQ690t2bRDb4A08a5jomqap6_fllUHx3TsCzSgnIhOYgmU9vTboDM3E1WVI7jLagZBAWeMFxeF_RuL0yxdGw7qNt2-KYpj3q3d_op_ttTyDt13i1hjKtjyqazocOVb44_4s_lPJbVoEU6xe7eL9bYEKm15Mwjl95f8SA3xmQd8T8NICIvpPWUWXD---3wDQMU6_Vak31asoITohDdT0dGi0he7QQvMoiRSV7q2iA0OA1MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار وحیدی: دشمن آرزوی تسلیم‌شدن ایران را به گور می‌برد.
@Farsna</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/446245" target="_blank">📅 14:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446244">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23286d3e5e.mp4?token=r4zb9Kpuo8r6qob2B60ns5Hs6d8rYj2Pr9AbKFRGuL02P1dwpVypNJhhG2epv_vKXRdwPGt7WArSS92GbGTMIjY74X02wzNbIL6FYQj3YeVfrJ5ZdP1-1cAaShtxC-c_YOEtbzROgvi3JIohYXUvBmCRosh-CXB7y-mtb3D8Y7XR0KHrrvj3vXyeF-MpkbEPfZLgM1LA3bvmyoEF5PacMogq3PZX1smHUedn3bVDpBVoEoOxGfqI-eZDqqy8XA4v6-qaebrY_YOzgNeFb-UGKsU22dBNwAkEx1mqJJHA-9EpTppTxuC3xjY-DEkdL6ck4pPXxiEnPhGKPG9zGCV53g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23286d3e5e.mp4?token=r4zb9Kpuo8r6qob2B60ns5Hs6d8rYj2Pr9AbKFRGuL02P1dwpVypNJhhG2epv_vKXRdwPGt7WArSS92GbGTMIjY74X02wzNbIL6FYQj3YeVfrJ5ZdP1-1cAaShtxC-c_YOEtbzROgvi3JIohYXUvBmCRosh-CXB7y-mtb3D8Y7XR0KHrrvj3vXyeF-MpkbEPfZLgM1LA3bvmyoEF5PacMogq3PZX1smHUedn3bVDpBVoEoOxGfqI-eZDqqy8XA4v6-qaebrY_YOzgNeFb-UGKsU22dBNwAkEx1mqJJHA-9EpTppTxuC3xjY-DEkdL6ck4pPXxiEnPhGKPG9zGCV53g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام رهبر ملی ترکمنستان به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/446244" target="_blank">📅 14:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446242">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc36adf0d3.mp4?token=psax5Cl52s00zRAOPozbS5bKf1Con-XJS0latU-xM2IBh_vg66LBSab3nEGIRijmh83GxQEBu4OUHui9Q_6tcTlsMwK8h6KulJBjUX_fVQo0MBZg11ot-foTn0e4BugAHSaYBeV83aSl1FkwiKyTAAOfPFTx0OrsdVABPBcTDyHNEGGFqqz24txn-OJ0bVO1g5iWPTIfM5bfJElwN2q1oQrKl7QwebSO8454HelJ5nMpF3D6BjAhtimxN9t7Ndu0zBYBvLE5DjjJ7mdiJU8xG8syNtL4GzpD92hxxtE_5tecP3LEmE83Lz8BscvEtUoNephOFLXt3MP6i46NA5Vs_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc36adf0d3.mp4?token=psax5Cl52s00zRAOPozbS5bKf1Con-XJS0latU-xM2IBh_vg66LBSab3nEGIRijmh83GxQEBu4OUHui9Q_6tcTlsMwK8h6KulJBjUX_fVQo0MBZg11ot-foTn0e4BugAHSaYBeV83aSl1FkwiKyTAAOfPFTx0OrsdVABPBcTDyHNEGGFqqz24txn-OJ0bVO1g5iWPTIfM5bfJElwN2q1oQrKl7QwebSO8454HelJ5nMpF3D6BjAhtimxN9t7Ndu0zBYBvLE5DjjJ7mdiJU8xG8syNtL4GzpD92hxxtE_5tecP3LEmE83Lz8BscvEtUoNephOFLXt3MP6i46NA5Vs_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نخست‌وزیر پاکستان وارد تهران شد
@Farsna</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/446242" target="_blank">📅 14:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446241">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6906509da4.mp4?token=t_i94m5YLk53ROZOaOhC1Axm6685l-eYjQDkaR2J2IHn-JKxMT4r844GCGP2IgWlxOhSPqxQbABMeBtuZiUYcK5uyEOFOPm6Nj1ijGCHf62PjgNZXbuYsT8XIAzytJAjb2aYgDLjPgQmpydtrGDKUOEdZvMkBHSQhaNxJ_PcjzXTbOQUFPU-ARChtiP6d3EkwwvgKl778bceeU7AntYZw_9EG5bpi9yRWdt6jlUQEJmskACeh6sHjWTQ9VNRamG83YlY1j18jrE7pMT5pjCHl4LDaTcU--nbR-AXEQSBnRJ1_s1XYSPkKthIAD_SvP2RRZl_Kfgl33e97cL0JqSmTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6906509da4.mp4?token=t_i94m5YLk53ROZOaOhC1Axm6685l-eYjQDkaR2J2IHn-JKxMT4r844GCGP2IgWlxOhSPqxQbABMeBtuZiUYcK5uyEOFOPm6Nj1ijGCHf62PjgNZXbuYsT8XIAzytJAjb2aYgDLjPgQmpydtrGDKUOEdZvMkBHSQhaNxJ_PcjzXTbOQUFPU-ARChtiP6d3EkwwvgKl778bceeU7AntYZw_9EG5bpi9yRWdt6jlUQEJmskACeh6sHjWTQ9VNRamG83YlY1j18jrE7pMT5pjCHl4LDaTcU--nbR-AXEQSBnRJ1_s1XYSPkKthIAD_SvP2RRZl_Kfgl33e97cL0JqSmTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام حداد عادل به پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/446241" target="_blank">📅 13:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446240">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51ebf3683c.mp4?token=DhFWCsnJxohC5N_rwVCsq20bEosjgKqBZabwpAv6fIgG9uLzjN0iXiEyRRsRubRiZTa9krNhOLpkXlTV8gnj76oRN7BUY6v2GtpBK2IjtrnrxzE7pvISpi9iPDWV1Af7BPBIHT7riMUjVnL6qbEzFwQwNV2G38p9p1optqZvoewP-CY9hGKL9mfmX4hh0ntPYkIw391AtCMifQf0mhD-1BenPd2XsH8lpWb1X8dMxf8-uDakIUJq49npC0Qmhp5pw1YBpU1vzG8Rx49spNLhWI0A6ZxamOvDLZ20aE1CxZHSi0LJV-A159qtQ5sd9mmugdm5o4H8ZPevVv4DGYYLUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51ebf3683c.mp4?token=DhFWCsnJxohC5N_rwVCsq20bEosjgKqBZabwpAv6fIgG9uLzjN0iXiEyRRsRubRiZTa9krNhOLpkXlTV8gnj76oRN7BUY6v2GtpBK2IjtrnrxzE7pvISpi9iPDWV1Af7BPBIHT7riMUjVnL6qbEzFwQwNV2G38p9p1optqZvoewP-CY9hGKL9mfmX4hh0ntPYkIw391AtCMifQf0mhD-1BenPd2XsH8lpWb1X8dMxf8-uDakIUJq49npC0Qmhp5pw1YBpU1vzG8Rx49spNLhWI0A6ZxamOvDLZ20aE1CxZHSi0LJV-A159qtQ5sd9mmugdm5o4H8ZPevVv4DGYYLUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام سید حسن، سید یاسر و سید علی خمینی به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/446240" target="_blank">📅 13:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446239">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df1a50e982.mp4?token=sl4wmhJJDnPMsKpbrnmP6wsUh981LPVZ-RqlttT24UHQ1Eap7kCJnhKBzc-O_OLgI_aWFEbrAjH3XOezlXT0zpJguRz4RRO4Hm99YOGLX6mn71Xv7oTDOewMHJI5uYuL69v-dW2-9Js90u_pKL-kPO0i_NS3Qu3dKxEZysufAkKBqLehAs97uxV2gLdPyffx8MD8_3ww8gDYeO1DTjb8bafyGuzV1pEsgpXQmWDbcdL4KC-PFkKrWKumhvowGa5l_gjsazKbhCAfGDo9lZZTMQNXGD1wnXrRHpPK8zJF-Gjrw-sVq-WmdhM1F8oRqH9djLJ6yd4e0pK70AOrMeCP1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df1a50e982.mp4?token=sl4wmhJJDnPMsKpbrnmP6wsUh981LPVZ-RqlttT24UHQ1Eap7kCJnhKBzc-O_OLgI_aWFEbrAjH3XOezlXT0zpJguRz4RRO4Hm99YOGLX6mn71Xv7oTDOewMHJI5uYuL69v-dW2-9Js90u_pKL-kPO0i_NS3Qu3dKxEZysufAkKBqLehAs97uxV2gLdPyffx8MD8_3ww8gDYeO1DTjb8bafyGuzV1pEsgpXQmWDbcdL4KC-PFkKrWKumhvowGa5l_gjsazKbhCAfGDo9lZZTMQNXGD1wnXrRHpPK8zJF-Gjrw-sVq-WmdhM1F8oRqH9djLJ6yd4e0pK70AOrMeCP1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اشک‌های پزشکیان و سرلشکر رضایی در مراسم وداع با رهبر شهید  @Farsna</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/446239" target="_blank">📅 13:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446238">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/284edbc04f.mp4?token=itkVa7tYWvtvkcUiT7PhuuzQgF31ezOrzkdav6lNEYBEaLfnLU5em08arjC8okdGYIdhZUW3zvxl0oLRfqTkQeNYmhaAhriQujHyTxKMYSAnNTfPumDuJPd-Ki7_9c7trR8kLmduLLFUOOV_ocrBtzFNWsuLwSrGYJJzXF_yQ3tpLBH3JaOThKBBFzL-xjMNUrLjG4-s40-K2egXYSxkrB34g2UAdLnTNVWfA0MBMmRo4kOa9UQpNtZRrlIau2fz0eHmq5_4qUdPtYSJLrEBBNzdiLwhq64zRCzjNzzV1t6silxjzj6z3zV2WbBc3Qf1tFZRXc2xSoGvwR7eLpbKmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/284edbc04f.mp4?token=itkVa7tYWvtvkcUiT7PhuuzQgF31ezOrzkdav6lNEYBEaLfnLU5em08arjC8okdGYIdhZUW3zvxl0oLRfqTkQeNYmhaAhriQujHyTxKMYSAnNTfPumDuJPd-Ki7_9c7trR8kLmduLLFUOOV_ocrBtzFNWsuLwSrGYJJzXF_yQ3tpLBH3JaOThKBBFzL-xjMNUrLjG4-s40-K2egXYSxkrB34g2UAdLnTNVWfA0MBMmRo4kOa9UQpNtZRrlIau2fz0eHmq5_4qUdPtYSJLrEBBNzdiLwhq64zRCzjNzzV1t6silxjzj6z3zV2WbBc3Qf1tFZRXc2xSoGvwR7eLpbKmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام روسای قوا و رئیس مجمع تشخیص مصلحت نظام به رهبر شهید انقلاب    @Farsna</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/446238" target="_blank">📅 13:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446236">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b05979c5d8.mp4?token=eXhn6ZvLkrNuqW4qieWfqytc_he431eEuDvXrY4ORhMpiMESd2PYUU8JFfG4iWeZbNWPml7iLs1lFGWS2W0-6hdjCbctvxHCYr19AUx0G5etWkjpOA80Du5GhhuB3yQQvRfK4cA2zebFjrKGm5uFkdGUrwvnOGHNrvItIQ941Crq6b9tlCh91ds88cC0ZVqWgaDbmVeVw3H4S31LP-p0K2uou087lTEA1HfG5kW04a8I4A43GZF12WfcZyL9iVTHrAwpg01gEjhEwKQRM6ViDC5CsJ32gOiEzNLRxnBAHMrrBQwvVIA3-fkONn7ed-cqgZB6gg_zedazYkjMblCNZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b05979c5d8.mp4?token=eXhn6ZvLkrNuqW4qieWfqytc_he431eEuDvXrY4ORhMpiMESd2PYUU8JFfG4iWeZbNWPml7iLs1lFGWS2W0-6hdjCbctvxHCYr19AUx0G5etWkjpOA80Du5GhhuB3yQQvRfK4cA2zebFjrKGm5uFkdGUrwvnOGHNrvItIQ941Crq6b9tlCh91ds88cC0ZVqWgaDbmVeVw3H4S31LP-p0K2uou087lTEA1HfG5kW04a8I4A43GZF12WfcZyL9iVTHrAwpg01gEjhEwKQRM6ViDC5CsJ32gOiEzNLRxnBAHMrrBQwvVIA3-fkONn7ed-cqgZB6gg_zedazYkjMblCNZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام روسای قوا و رئیس مجمع تشخیص مصلحت نظام به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/446236" target="_blank">📅 13:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446235">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ef3133b31.mp4?token=Nvy0n3GERbUVa527U2ukq-jiYQ_NN4BHNANL0WUbGyMcorh8yO7M22R_snpjKURsr2aUtLgAF0w_mt4Z9mfTmNUv2jv7Hlm-asgHmXmrVSYoDZv74namrggztB7DtIl5FBVrGUDTNds7APyKhywNUGTQv75swu0vtcjEWZ-lZlzIvC2GQUrQIu0s5ZBNnRGGZRX9jHlZkY2mWAdBYlW5ztXy3shkr3xigWFi1LAt_PeZPdOdItwW45rtjC6cFRLQUGI_40LMvBpPrbhdM9m-Ehb-7_DlcCeFDqGi0d_dog0NQt68nru99yeAhZBYkA3293y02XiF52aimy-LF9mt9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ef3133b31.mp4?token=Nvy0n3GERbUVa527U2ukq-jiYQ_NN4BHNANL0WUbGyMcorh8yO7M22R_snpjKURsr2aUtLgAF0w_mt4Z9mfTmNUv2jv7Hlm-asgHmXmrVSYoDZv74namrggztB7DtIl5FBVrGUDTNds7APyKhywNUGTQv75swu0vtcjEWZ-lZlzIvC2GQUrQIu0s5ZBNnRGGZRX9jHlZkY2mWAdBYlW5ztXy3shkr3xigWFi1LAt_PeZPdOdItwW45rtjC6cFRLQUGI_40LMvBpPrbhdM9m-Ehb-7_DlcCeFDqGi0d_dog0NQt68nru99yeAhZBYkA3293y02XiF52aimy-LF9mt9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس مجلس جمهوری آذربایجان برای شرکت در مراسم وداع با رهبر شهید، وارد تهران شد
@Farsna</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/446235" target="_blank">📅 13:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446234">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d511dc52a.mp4?token=qGNd4G5bpGQajbrf12GDNUIhf5PU1hhuNwjjzV0r5_2XuaFnUo93yMYQBbw315GIQ9mS82oZwEKs29FOHgymLcyghM76H6Lf1ouQDgp7FQiI2mMiLdxaFakVY8IBI_xZZGZ24H5GcbspKB6u8PChERV9sVSORNmrRDiSciftn9ydvpWgTYpeEbBZh_M3ApWfL6DnUE0LIsJ5baeavrP9eU-TQ7yWRk3ppGTBj_bX6Z2-RntLmOPne6KNDs7lN4wfOTLhBBbVw97HSZJFAU5gaQ-TAWyi7S-Mplow2nO7AQXwHayy1i8mmtJ2P8tHteOMSDW9ZseXTGZ_io3eFknJ-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d511dc52a.mp4?token=qGNd4G5bpGQajbrf12GDNUIhf5PU1hhuNwjjzV0r5_2XuaFnUo93yMYQBbw315GIQ9mS82oZwEKs29FOHgymLcyghM76H6Lf1ouQDgp7FQiI2mMiLdxaFakVY8IBI_xZZGZ24H5GcbspKB6u8PChERV9sVSORNmrRDiSciftn9ydvpWgTYpeEbBZh_M3ApWfL6DnUE0LIsJ5baeavrP9eU-TQ7yWRk3ppGTBj_bX6Z2-RntLmOPne6KNDs7lN4wfOTLhBBbVw97HSZJFAU5gaQ-TAWyi7S-Mplow2nO7AQXwHayy1i8mmtJ2P8tHteOMSDW9ZseXTGZ_io3eFknJ-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور رئیس مجلس قطر برای شرکت در مراسم وداع با رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/446234" target="_blank">📅 13:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446232">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8ce3c8a43.mp4?token=kqRix97qK-yzy8fCzZmssGBkUoL1Zf4t_5YKtj7yJoj28SdnS8z71HXYF93Z7LapYIbeN1tlyrZhFksyAgct4GOzgWETvpEXvIP97qKPLh0D1horaDh-W5H6I-e_PMg5rQjhTjTnwtu0UqtdzML7sJ2cUig7yaln-_RN_FlKySu4QIYgNMhw_Q2M9HZt_gK3CTRCmcbWehXtMzwX9z31wW7POtW2DslVNXRdfs3FmproUuoStkGwOSUEOxKUU51WNjXNSmdIqIRFV8OdJ2cJl751PMI2Cp-EDK1XewzzyZihqAlGjieELmzsBHgAIWpby4zr20ZtF2XDYfo3EqEmMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8ce3c8a43.mp4?token=kqRix97qK-yzy8fCzZmssGBkUoL1Zf4t_5YKtj7yJoj28SdnS8z71HXYF93Z7LapYIbeN1tlyrZhFksyAgct4GOzgWETvpEXvIP97qKPLh0D1horaDh-W5H6I-e_PMg5rQjhTjTnwtu0UqtdzML7sJ2cUig7yaln-_RN_FlKySu4QIYgNMhw_Q2M9HZt_gK3CTRCmcbWehXtMzwX9z31wW7POtW2DslVNXRdfs3FmproUuoStkGwOSUEOxKUU51WNjXNSmdIqIRFV8OdJ2cJl751PMI2Cp-EDK1XewzzyZihqAlGjieELmzsBHgAIWpby4zr20ZtF2XDYfo3EqEmMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای حرم حضرت معصومه(س) در آستانهٔ تشییع پدر امت
@Farsna</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/446232" target="_blank">📅 13:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446226">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RntCAtp30mgoiuomb9E64CldiRDxgNecd57msWXXuO6oMoOWjiPNcE8Ow4tffYY6s6D53bwpR4NVPeeNs8oZkM_jHEF6x4VVYWHLIQE0zxszAbs9OenjbWyBRwaYEjTmo4_OQ2XzieI8eRPOmqudSzls9NRtsi2QVL3BSFv5Vz1DKWJ5UM3x-EdMV9BIS5MkM08kpyFjrrAoZRQDfXSSvDl1GkVK0YbdStfEDwn-wAt_tAVPlQYg0vQhQ2M7DR6JHhrBMCkyp4GYwX9pY3RQp2Udy_v0o9DXvOLciKla_4OO5p0B6tlKNZceQsdRom2joJwmZ1ilFL0xr6mleM9wqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ShWCb8yoXOtJVwT5UPOX0d_1Pp1achRsqJ5ulw6lslxed9gap5mN7NGopqyqEQ44xBEIXJzkKLCOyisMumEX-wt13HMHda953I1K6GmtW8VMqdGwFl_tMw8eddlP5j9tIvesUTZdW0Gln6MdFcNlUFvLR87vA3NpTq3HN2tKBGjmWu2mA3BqeGf0rzqK-IAFAHytxu-meKu9Yiwhsw9o24mu3Vt-2FIRvpsIdyPWr7fhiQVpoNt2-8X6hrWtqTAkjIm4SW8jsByiJy6Vh7y6LrAxoMxHkrEIeBQDpM0JGodAoaB6EvU6pWV_db7TXx9tGAelbI5IpMgeK7x45NNTSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Bn2K3p9J7a-B2dFQx95YzidPap737nAvSZAcp_b8aCUEp97FaA7NoSjFRwxbyJx_oyFt6i1I-wez1hsZ80_-rBfFQOT66AfwIYzBzBuGKpzYt7BN82oXwrKURNKgxWR7qcOoycXOUgezv_x1Ye1Xr6O58QqTAK0vnfJcwKiy3RJ1WeMO8bXh1boYtJCNlCZyHRhv2m2Ioeelgza-uHgfVf7Li1mIaax_EmhMkdzj14h_ndKQ4eOIR7dnI9yHN6vWNOUqhR2Qz1QEyfUICp7LDdBYZvI7JF4r0MwWPOH1yK40wGeFm9dK8HkwF4pDyqtqHr52e0Ni3qWSLKyUVxy0HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TwrJAb9Clq2lO0LvKi2P366PSEJTqzpCX2nizheYRxPbACBneiNtv9RBkM07wJEtxIBPcnIGykNxwkSTtaYos1hMcSRxLravP3uBaR1iVagp2PxMfIHU_MVaMpg_7Ns8Bu3yR_3Vy7J8ZHGdfXTtDSTN9OjEl51Wn9C3uhgbuiqwUENelsUKwEPhsBTlLnTKLCf5soJV5EC_hdCoAe16j2Sis4vIt1Emt4Usgp_-BqmneC3am3yz0DEa9WZArjIsOmHYh_9Iuh5XJwnois4wPtpms62gB_u2Hga8xPmvxNi2HJcs71T7zsPEOg66-Y53DBhONML5vmFUKfX45nyI1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AZbxsuJcrXZIn1ByAhxt92HPtnVovFZwbkFKX5kLgScpl8igyNVnHpiCo_cQ0fSRYwnEA38e72mNqdrH6YR881ztB8CfJRBIDiAM_iDhoRrvPSajL1MTmTCAuMelz8ZQmixnaZAnIAN5aZKVeYD8naNwe5V0a-9pP6rigtpkqO75hRIAf_WDp0qnP0iK-nH_6f5uctnA19_eZuqPTr57yKHRDKSfLetK92-0VUB1XmgGtqFWfHKlVP9fNrSZ2lQlvahdW_0rK3DA5trj-8PNLjcAOHSgrHS-QnFIE37RDO55USAgNYsl7Nr81yjbsH97nhkg5t0xx54E-rvhcyAgZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/g8mah3wmASQ5iyD0VBdY7LPA2dqhDq7seVX0SOv8s30OlAWtNRpRBfy2QQF7ywmm_4AeJZl9O2cs_ozLmobRvI0-iQbiEFjKPgDa7pARnkJKj0hUBP3MdJ1VT704T3oQP0HcyF9ITEMoeLFSobJebaqCqXt2_3diyTXB45_Zza1QkJa-jBT0UqvbVv9rQX_Uo3Q47MSeUtIgmygKn0D9HX8BO6RDOgnQFO46j0MD0bw87KzGMQ7KJv0qY3pCD0ru0Iyw_KLHJr-89BJABXUsU4eTJSpriH1OXpsYs7wyVR7RS3LG8hQz-LLePxuNhjbFbb3y-5L4jPHOXrcIhYC-fA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همراهی فرید دهقانی با وزیر صمت در بازدید از موکب چادرملو در آستانه مراسم تشییع رهبر شهید انقلاب
🔹
وزیر صنعت، معدن و تجارت و هیات همراه و مدیرعامل شرکت معدنی و صنعتی چادرملو  با حضور در موکب این شرکت در میدان ولیعصر(عج) تهران از روند آماده‌سازی و تدارکات پیش‌بینی‌شده برای خدمت‌رسانی به زائران مراسم تشییع رهبر شهید بازدید کرد.
🔹
به گزارش روابط عمومی چادرملو، فرید دهقانی در این بازدید ضمن تشریح آخرین اقدامات انجام‌شده برای تجهیز و آماده‌سازی موکب برای وزیر صمت و هیأت همراه، روند اجرایی و تمهیدات پیش‌بینی‌شده برای ارائه خدمات به زائران را تشریح کرد.
🔹
مدیرعامل چادرملو همچنین با قدردانی از تلاش عوامل اجرایی و دست‌اندرکاران برپایی موکب، از زحمات آنان تقدیر کرد و با آرزوی توفیق برای همه خدمت‌گزاران به آنان خداقوت گفت.
🔹
لازم به ذکر است، موکب شرکت معدنی و صنعتی چادرملو در میدان ولیعصر(عج) تهران برپا شده و آماده پذیرایی و خدمت‌رسانی به زائران و شرکت‌کنندگان در مراسم تشییع رهبر شهید است.</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/446226" target="_blank">📅 13:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446225">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqMiCTbx34wVUWYYaMAX1hGztQb_ym95rzB35pBARiH2kMFvD6UEsnrLA6Xkvdl9xGw9y56sud11X0xo9OYYxG8RXtQnVlxAz6PTCYd2qzd4CfOB3VxaH_jZTJt3YpiGIw00oQRJXuZptrLZxh0w8eJq8m4xSLtmzCnbUTsfbvwq0-6QIopOgQWIObJKj8uPPRlqkLFqgGFaPtVBF1P8AQE_blKPo-MWDTu2nvyKYGnGXgDK1gceHZeFx5Nl4VzP7PBeOUXZ1I425yKZPuVtrJ9NnPalBetYYtSn8eBwnqWSApb7X8uODYE3U_A5GTq-Bu9f0Qase8lm2ELt9feGSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/446225" target="_blank">📅 13:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446224">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/446224" target="_blank">📅 13:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446222">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b447433567.mp4?token=rae5nq44bgVvEDkIWqDMk3lIsVX8FZpzJz7LRxvidPsNeuSV3i6zQCDE8nLAn4b4M1sSgB38P081Pc3lj6I7fxNx8spUurUROwoH_1DqRvKXBA-zwuGf_jm0Ry_60yriln12h82yh2vgWmq_98dP-YZYZNsrrh46uFgCDH-zCH0Yc8X5Uq9jXcjfWSyBASL1exe8fL3agTKYoR9hb0V8Q6Fw_Iwo5uzZfxYhnSXftMu1lGS4Opz8yHzBpIMOlg3PZJ0ltkkJeLBR5cY68jGxQJXGoo9N0TRy-6zGTdLoaibs9kP137EredeMD4MnPAfc04ZwNo1y598CDKANFOR_ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b447433567.mp4?token=rae5nq44bgVvEDkIWqDMk3lIsVX8FZpzJz7LRxvidPsNeuSV3i6zQCDE8nLAn4b4M1sSgB38P081Pc3lj6I7fxNx8spUurUROwoH_1DqRvKXBA-zwuGf_jm0Ry_60yriln12h82yh2vgWmq_98dP-YZYZNsrrh46uFgCDH-zCH0Yc8X5Uq9jXcjfWSyBASL1exe8fL3agTKYoR9hb0V8Q6Fw_Iwo5uzZfxYhnSXftMu1lGS4Opz8yHzBpIMOlg3PZJ0ltkkJeLBR5cY68jGxQJXGoo9N0TRy-6zGTdLoaibs9kP137EredeMD4MnPAfc04ZwNo1y598CDKANFOR_ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع فرماندهان ارشد نیروهای مسلح با فرماندهٔ شهید کل قوا  @Farsna</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/446222" target="_blank">📅 13:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446220">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd6ea0f1b9.mp4?token=CcFW4s_RNdsys_u2DqVPDwJwALcjUxuSK1FydzNc3b_Zr6O-i7R2o3zy6tK3dpgL8uW6_DnGc-rt47m7612d9XATmO6_NuO_fLzs6d53XQu9vSpFm6zb7rLN4fdMUOSCEvUnuDiYpFti0t7WNmIFy91bNmjeELT0p3KaY8TT5tfZdlMzCZLVVVx__ecmCXU5_F_M2n0l4-iEMinR1MfIGZ3IFnnmAJ0RZ6Jnc-8zOVWfMT5QCjxIdpSuIvraZOF-_HteNC2UZiDMlhbrNN_1Lg0NbfYAa51rPomsRa0qMRhRlnCtdLVZWpalMLMR-_ZdLuB9OTDdI7UlSxZj6OKHkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd6ea0f1b9.mp4?token=CcFW4s_RNdsys_u2DqVPDwJwALcjUxuSK1FydzNc3b_Zr6O-i7R2o3zy6tK3dpgL8uW6_DnGc-rt47m7612d9XATmO6_NuO_fLzs6d53XQu9vSpFm6zb7rLN4fdMUOSCEvUnuDiYpFti0t7WNmIFy91bNmjeELT0p3KaY8TT5tfZdlMzCZLVVVx__ecmCXU5_F_M2n0l4-iEMinR1MfIGZ3IFnnmAJ0RZ6Jnc-8zOVWfMT5QCjxIdpSuIvraZOF-_HteNC2UZiDMlhbrNN_1Lg0NbfYAa51rPomsRa0qMRhRlnCtdLVZWpalMLMR-_ZdLuB9OTDdI7UlSxZj6OKHkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار هیئت‌های ویژهٔ افغانستان، چین و نامیبیا با پزشکیان
@Farsna</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/446220" target="_blank">📅 13:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446219">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65b69877cc.mp4?token=VtIvJ9u4f3srw3bhLTC73CMDhlYyTjOhHr-ygM-S_6f27f-l5tBxp6Jqcic1hm_AqjEtZ5fazF42nmDW1fjxsEb1Esz-29Y4Ji80Smig14aO0LSZoKK4Ehx1hcJ0c0vbJDMqBgnAEKxKJKvO4SlR-bsEXEBnFzhHuHKfk-NYzzdhKGx9YMKUVZ4kH9uujKCtJa_W6yZtJwnoQ3iis24p29r0MD-RcZ81DSgeGsEgpEfdK0hvXYpoLHiQofDpNOq9Rrp2Fc5cGR89pttlYk1BF17oarFw9oXjvJbG80m-ylxIZIrH5pBdUD_r8-EnetMumbQJswZENl4rGdltDILt3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65b69877cc.mp4?token=VtIvJ9u4f3srw3bhLTC73CMDhlYyTjOhHr-ygM-S_6f27f-l5tBxp6Jqcic1hm_AqjEtZ5fazF42nmDW1fjxsEb1Esz-29Y4Ji80Smig14aO0LSZoKK4Ehx1hcJ0c0vbJDMqBgnAEKxKJKvO4SlR-bsEXEBnFzhHuHKfk-NYzzdhKGx9YMKUVZ4kH9uujKCtJa_W6yZtJwnoQ3iis24p29r0MD-RcZ81DSgeGsEgpEfdK0hvXYpoLHiQofDpNOq9Rrp2Fc5cGR89pttlYk1BF17oarFw9oXjvJbG80m-ylxIZIrH5pBdUD_r8-EnetMumbQJswZENl4rGdltDILt3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرماندهٔ ارتش پاکستان وارد تهران شد
@Farsna</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/446219" target="_blank">📅 13:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446218">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKzlveDqp0fuXtDN26MYGMlPktt-cpi7yz_kZiaAfAy2GM9KokykKYiWQaMttWZk1VH5WqkzMfa24KoUJ-LytINVrrad_HEv9c-ntMd_sfHpmnddx7N8tCJjqqSDpym7XmaNwD5UF_chuIxF00cJNYu4NtS1-O4C7VkCKmdjrHJbU4EzjREWQXE5qRlecHpKMk4kSvnjHaOif3rk_g0qXpKIdgOY_S5b25rVywkJxwmVBCtzSXL8iB7wWJSmBW5qqmsRXatcqQRv3uVye3RimFMn49SqssIWlsEfO-sVvCsyLcsYj9e2e5LKCwoX2SyQyYiMt8pGFrmcYimNJNMkoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دست‌نوشته‌ شهید مصباح‌الهدی باقری برای آقای شهید ایران
🔹
یا سیدنا القائد؛ به وجود پر از مهر و صفایت می‌نازم...
🔸
شهید مصباح‌الهدی باقری‌کنی، داماد رهبر شهید انقلاب، اسلامی در آغاز جنگ تحمیلی اخیر، همراه رهبر شهید بر اثر حمله جنایت‌کارانه‌ی آمریکا و اسرائیل به بیت رهبری، به درجه رفیع شهادت نائل شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/446218" target="_blank">📅 13:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446217">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e65c733269.mp4?token=tre5X-QGRtFOJgfDcKoi6aEywWvWKaUG5Rdf7p9bN-6YbNUF2BreM3cxnAjkZIJSVaUXzm3ty4T7zkpAQhpW54atySs7j_vt0ki5mSGM6ZjBfbZje_pP3GqnOVcqVZx0KWQs0Y5gSlhzfILvKWJ6tzxSCh0Fc7k_Ycax3EONtS-NTtD0Jm6i1U8FUh8N7BBLdVYi_D8hSkaiqU___6yjQxKPZ424cssmTO7NtatQhBQt03jVnWkqYUoNmTpPubbsXfjc8a6EErv5jWJNNwc7HntTSEshTOJ80Uknpw8zWeqyyCYHFuJTJsgU1dtHaRwhHUA_YuPmcrNq5iWrdCreHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e65c733269.mp4?token=tre5X-QGRtFOJgfDcKoi6aEywWvWKaUG5Rdf7p9bN-6YbNUF2BreM3cxnAjkZIJSVaUXzm3ty4T7zkpAQhpW54atySs7j_vt0ki5mSGM6ZjBfbZje_pP3GqnOVcqVZx0KWQs0Y5gSlhzfILvKWJ6tzxSCh0Fc7k_Ycax3EONtS-NTtD0Jm6i1U8FUh8N7BBLdVYi_D8hSkaiqU___6yjQxKPZ424cssmTO7NtatQhBQt03jVnWkqYUoNmTpPubbsXfjc8a6EErv5jWJNNwc7HntTSEshTOJ80Uknpw8zWeqyyCYHFuJTJsgU1dtHaRwhHUA_YuPmcrNq5iWrdCreHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار رادان: قدرت نیروهای مسلح به رخ دنیا کشیده شد
🔹
اگر امروز نیروهای مسلح پرقدرت مقابل قوی‌ترین ارتش های دنیا ایستادند بخاطر تلاش‌های قائد شهید امت بود.
@Farsna</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/446217" target="_blank">📅 13:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446216">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b54d67a638.mp4?token=YThVKcyKtzxFaCJD0IYOqoc1zhKh15bB-lNxVMDnBm8yAIoKbFqlblBfdEWTH4CtKS6zkY__6C7ZvOSUWzqfzQcAUMeinv9yghnyOzdakqUI-6OMHfwQKiAYLU713cC-fizcWBAiH6LGpRKuHlYAMv7ZHdpdBsBNOg3h191Xo4DDtQZfFJt2WiyUz_uEvv36QHJSS29lppruyoaKzRc4eJ-PBw8aTooYwIHecqkW9cyAxIi0EAZXvANiRWqGm0ATyXCv14rk8MRqM3cMKLnqF4qsMvYkIIm7GHMpmsI172oYOAyE-mv0N0W53GT68isxty2-vvRk77bjvOkHhWMAdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b54d67a638.mp4?token=YThVKcyKtzxFaCJD0IYOqoc1zhKh15bB-lNxVMDnBm8yAIoKbFqlblBfdEWTH4CtKS6zkY__6C7ZvOSUWzqfzQcAUMeinv9yghnyOzdakqUI-6OMHfwQKiAYLU713cC-fizcWBAiH6LGpRKuHlYAMv7ZHdpdBsBNOg3h191Xo4DDtQZfFJt2WiyUz_uEvv36QHJSS29lppruyoaKzRc4eJ-PBw8aTooYwIHecqkW9cyAxIi0EAZXvANiRWqGm0ATyXCv14rk8MRqM3cMKLnqF4qsMvYkIIm7GHMpmsI172oYOAyE-mv0N0W53GT68isxty2-vvRk77bjvOkHhWMAdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود هیئت پاکستانی به تهران برای ادای احترام به پیکر رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/446216" target="_blank">📅 13:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446215">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f6ba4e64c.mp4?token=bMmzkvUlannghmWkegzZgNpU80X2UmidSiyz_Oj0nYLzI6hkUbXVL0r794j7Kq7RQQIPm4DGENdX7Lt5XOo5eT38tJnvXNGQbGxFkjKz4rCKZKjiSkopJXyCsfJayddX-eQDopkv5upCUHj0HcO_C3stDR9DY5Xmq_Ubehz1g1ExgzjNpaV9eQ-3g0pv9Q7MmRDYGLuSROHm0-Ok3Ojdk80NafKPAt2hOwFXOZdj-spNmGrzMj08O3_ovIXECpsdtnjKEgMTzSOAUe7pKG8hzfdp4oWyZtbTk1Ii2gqpHGSJEgCHot2-ulGTeBa75yu1csS_51LR_lrADsIK5sVOXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f6ba4e64c.mp4?token=bMmzkvUlannghmWkegzZgNpU80X2UmidSiyz_Oj0nYLzI6hkUbXVL0r794j7Kq7RQQIPm4DGENdX7Lt5XOo5eT38tJnvXNGQbGxFkjKz4rCKZKjiSkopJXyCsfJayddX-eQDopkv5upCUHj0HcO_C3stDR9DY5Xmq_Ubehz1g1ExgzjNpaV9eQ-3g0pv9Q7MmRDYGLuSROHm0-Ok3Ojdk80NafKPAt2hOwFXOZdj-spNmGrzMj08O3_ovIXECpsdtnjKEgMTzSOAUe7pKG8hzfdp4oWyZtbTk1Ii2gqpHGSJEgCHot2-ulGTeBa75yu1csS_51LR_lrADsIK5sVOXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع فرماندهان ارشد نیروهای مسلح با فرماندهٔ شهید کل قوا  @Farsna</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/446215" target="_blank">📅 12:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446214">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d18ea965.mp4?token=YwbDLdy3Pr759V97IliWQb__ODFCsZjXHXZbaRFapU_Kg2FYTYeihXnPuUXKVZGJIrWRDTqfu5m1xs8lFe24TtvGbWLX7sTM-DwPIFq9ZRLenWurWd9GfOTgcGuAz7US8nNIHVu-eUAxmz529sGftmBPPuscRgJpUTI7e2PLMqHhXC_zlCf55udOqdBTczvUZXeCeIlKzXlBogyLCS6G-FSF_AyZVtoPJxWScGO9wt-yRKePOcux-j0S5tsJa3RMCkyJs_yD4YI1yhFFfun_BkCg-GzJ0R-K6AtTFh_E6x4PXf-A-m5HaP-uVBotYRnHkw8k2VQMv7-g2EVNxhN2hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d18ea965.mp4?token=YwbDLdy3Pr759V97IliWQb__ODFCsZjXHXZbaRFapU_Kg2FYTYeihXnPuUXKVZGJIrWRDTqfu5m1xs8lFe24TtvGbWLX7sTM-DwPIFq9ZRLenWurWd9GfOTgcGuAz7US8nNIHVu-eUAxmz529sGftmBPPuscRgJpUTI7e2PLMqHhXC_zlCf55udOqdBTczvUZXeCeIlKzXlBogyLCS6G-FSF_AyZVtoPJxWScGO9wt-yRKePOcux-j0S5tsJa3RMCkyJs_yD4YI1yhFFfun_BkCg-GzJ0R-K6AtTFh_E6x4PXf-A-m5HaP-uVBotYRnHkw8k2VQMv7-g2EVNxhN2hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود رئیس‌جمهور گرجستان به تهران برای مراسم وداع با رهبر شهید  @Farsna</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/446214" target="_blank">📅 12:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446213">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ec925b47e.mp4?token=Zgoxj__ctjQfaUomxpu98m7dsWPYGsVlpNyXV-x1Mq1nTlIbYli93Wegq_xRhJlFDE_F3UP-ZkKbgug33vjBU1Ac-wQdB5ta88wYdJ3wqNysrgTv7NCB_eS0TlTmHu8JnYW-JmYlm5CFVV9tFDTg2Z7mcB2r7-Tn0uX9iC7_x8oUHB0moSPWGLFdbT9wAZP9eohqzpJy7RAcrLc9EGv466t-ZIN9QgnnuKomc9QW2t3sA0Eehrtm8ZHrhkfc0YkdG3ZcqPS2HGbTLH7Baom-TZ0-ojmt0JgmrxjBwnYrdvXAmIqm6jjllUQmpG6ge6volGH9F6vGDamZ-1vHq4tTgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ec925b47e.mp4?token=Zgoxj__ctjQfaUomxpu98m7dsWPYGsVlpNyXV-x1Mq1nTlIbYli93Wegq_xRhJlFDE_F3UP-ZkKbgug33vjBU1Ac-wQdB5ta88wYdJ3wqNysrgTv7NCB_eS0TlTmHu8JnYW-JmYlm5CFVV9tFDTg2Z7mcB2r7-Tn0uX9iC7_x8oUHB0moSPWGLFdbT9wAZP9eohqzpJy7RAcrLc9EGv466t-ZIN9QgnnuKomc9QW2t3sA0Eehrtm8ZHrhkfc0YkdG3ZcqPS2HGbTLH7Baom-TZ0-ojmt0JgmrxjBwnYrdvXAmIqm6jjllUQmpG6ge6volGH9F6vGDamZ-1vHq4tTgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع فرماندهان ارشد نیروهای مسلح با فرماندهٔ شهید کل قوا  @Farsna</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/446213" target="_blank">📅 12:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446212">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97aeab7b7b.mp4?token=gXoIKi524VD4VEX_Sh-ylYY8t_bjPOrSbDlTX7BZhN8jLHudLjlSbLeI4M4S7bEGE_OJpZvMlHf1ilyAo2X5sp4QwiF42ISsUkCDEH7Tk2MBAIE-rFNZruNWcSnWCfchsUH7IWyRQc2Sax6ICIswta8KoguiQPEc23St8kInp-ovcA-FEhFdtkA0qZqDnNelty1Uj1CvAc0IQ3MUlkxRgHVDU8sYjW1mKd8DrDVbsT9x7LsgmZHxXoJT6afOkluIxCRnk445Qa4o82Z_t68wO-mXUnmP61rcWGs9PKfFebKveZWrOIYAaSUQZc7o3j6Fx-WkYvZAKCPRAAdJAGQrVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97aeab7b7b.mp4?token=gXoIKi524VD4VEX_Sh-ylYY8t_bjPOrSbDlTX7BZhN8jLHudLjlSbLeI4M4S7bEGE_OJpZvMlHf1ilyAo2X5sp4QwiF42ISsUkCDEH7Tk2MBAIE-rFNZruNWcSnWCfchsUH7IWyRQc2Sax6ICIswta8KoguiQPEc23St8kInp-ovcA-FEhFdtkA0qZqDnNelty1Uj1CvAc0IQ3MUlkxRgHVDU8sYjW1mKd8DrDVbsT9x7LsgmZHxXoJT6afOkluIxCRnk445Qa4o82Z_t68wO-mXUnmP61rcWGs9PKfFebKveZWrOIYAaSUQZc7o3j6Fx-WkYvZAKCPRAAdJAGQrVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع فرماندهان ارشد نیروهای مسلح با فرماندهٔ شهید کل قوا
@Farsna</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/446212" target="_blank">📅 12:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446210">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8e6eaa98.mp4?token=Q_t8o3rrvMoKINpRUNhlV6xYrB4OwOz1cTuUs80_kg9vEfyKuBf2b0jp9tGdotlbm1C-7tCcyLd3Jft6VXHtfYyhGv0Tzm9qLwr9WIqaE0DWDWwyM3II6K_jLvu7PeAdGK7r_puzjh5EqO_E5hsxh2hyqknvK-RD0ltwcTuImsje0tKgrzaGduqrxV3CcmbsKQDB59v7Az7QjzBzl1NJqLT7rOB-IgSrWmdv_KoRbtVDcboVLko4kVc4ErHgKDYnLqeqMs2gh9HP3uL7PdTJIa4V21HRR7j6cSZJxiDfAqIujbqw3ePDEDX5Y3aG8CRyWGbVUS8ZD-O4Yffyi61BCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8e6eaa98.mp4?token=Q_t8o3rrvMoKINpRUNhlV6xYrB4OwOz1cTuUs80_kg9vEfyKuBf2b0jp9tGdotlbm1C-7tCcyLd3Jft6VXHtfYyhGv0Tzm9qLwr9WIqaE0DWDWwyM3II6K_jLvu7PeAdGK7r_puzjh5EqO_E5hsxh2hyqknvK-RD0ltwcTuImsje0tKgrzaGduqrxV3CcmbsKQDB59v7Az7QjzBzl1NJqLT7rOB-IgSrWmdv_KoRbtVDcboVLko4kVc4ErHgKDYnLqeqMs2gh9HP3uL7PdTJIa4V21HRR7j6cSZJxiDfAqIujbqw3ePDEDX5Y3aG8CRyWGbVUS8ZD-O4Yffyi61BCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون رئیس‌جمهور ترکیه برای شرکت در مراسم وداع با رهبر شهید وارد تهران شد  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/446210" target="_blank">📅 12:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446208">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b9579cbe8.mp4?token=t1hliKlzVjpqgSnAhYf7b6nO-RbwTBJ_IGTR9_okamFFwGZ3ceJlBC2i3nIjI5L5tlSDO2nfMbt1opd2eSXbFa2Qcru-AnGQuBPe1mvGC0bN6ydCsarDH37YPvjTzfyIMEuPDGKIXxX779ZHLYffVEWDkKR_Yx-p8CIF7g-yJzKzDeqpHVlcc1JZc2_tOR0Cd-pRZSGQS8b5oJltbguI0FcirA1PbrtAphRPa29H4k7_Nv6bxxTbzWU7eDyGARu_XhSitoubxhIG_1Wgnoegirhp_wJntmilJ2_MI-qTxBxkgq1_9M4rxkLAYKbSapNfL6w0V2SpfZBilxuk_TAE0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b9579cbe8.mp4?token=t1hliKlzVjpqgSnAhYf7b6nO-RbwTBJ_IGTR9_okamFFwGZ3ceJlBC2i3nIjI5L5tlSDO2nfMbt1opd2eSXbFa2Qcru-AnGQuBPe1mvGC0bN6ydCsarDH37YPvjTzfyIMEuPDGKIXxX779ZHLYffVEWDkKR_Yx-p8CIF7g-yJzKzDeqpHVlcc1JZc2_tOR0Cd-pRZSGQS8b5oJltbguI0FcirA1PbrtAphRPa29H4k7_Nv6bxxTbzWU7eDyGARu_XhSitoubxhIG_1Wgnoegirhp_wJntmilJ2_MI-qTxBxkgq1_9M4rxkLAYKbSapNfL6w0V2SpfZBilxuk_TAE0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود هیئت عمانی به تهران برای شرکت در مراسم وداع با رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/446208" target="_blank">📅 12:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446207">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2919107021.mp4?token=vaz7cUUA_tJ1YIMxfawbiAEwRhsMS9QbXPaY5K5vrPufS_m6gVPBV-b8Tjl-ufvBS68ijjH3ScGNYB9nFxAVWTq9sj_P7Nh0xFyHhzRaGG1xV753FW8pmin5UBf8pFyo3j2myb_z5m6Txg2encxS7O6-6zeVtFw1Bp47jpYMQDlSUFMv3zqLbw-5F-4KQwueb4W0jXB419tnaxL-dKjDu3ZkY97Cbx7XceOMxBDKnnNthNzAxSXU2WXy_MRh5Y2kJKr1wp5ksxoQpqUdJkD0em7wPkXf9xAwqPdRgF5H5EDAYGIAcqKpgQvW2_ltHFIcDt4P4_Z9Dwd7pkrqgCvs-jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2919107021.mp4?token=vaz7cUUA_tJ1YIMxfawbiAEwRhsMS9QbXPaY5K5vrPufS_m6gVPBV-b8Tjl-ufvBS68ijjH3ScGNYB9nFxAVWTq9sj_P7Nh0xFyHhzRaGG1xV753FW8pmin5UBf8pFyo3j2myb_z5m6Txg2encxS7O6-6zeVtFw1Bp47jpYMQDlSUFMv3zqLbw-5F-4KQwueb4W0jXB419tnaxL-dKjDu3ZkY97Cbx7XceOMxBDKnnNthNzAxSXU2WXy_MRh5Y2kJKr1wp5ksxoQpqUdJkD0em7wPkXf9xAwqPdRgF5H5EDAYGIAcqKpgQvW2_ltHFIcDt4P4_Z9Dwd7pkrqgCvs-jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس‌جمهور عراق برای شرکت در مراسم ادای احترام به پیکر رهبر شهید انقلاب وارد تهران شد.  @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/446207" target="_blank">📅 12:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446206">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eb3f4182e.mp4?token=PrcUau-OZgnuk8URTMqOVd1KKaRbztGMtkFFULF3JJJmm0Z4Ca8w-_2Ux4ItYyVfFykhKVhPVsJmRiwfKwkzV8HCNvgu8A0HtN6ctRtBzEJQF_TBcF5teAgARoK2spM0q3qCTA93H7v23aLCDxrKjQ92DRXkH5_c3QkboPjQuIQiY5y0doveqqn2JB0xLrLCp_aTBCWakTvmVM9lV8XlMCa7DJ3EAcXmtzJpa6RHWyu_GCTsFOrLcA4rSkjJpcHTFSAS0Lj925YjH8vWlNVBMAVtBHR_ycj_clqvbCmrm_OGVX6z06xjco9IE5DmxDJcwZAc7xG3p2h98xU-K2DWUDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eb3f4182e.mp4?token=PrcUau-OZgnuk8URTMqOVd1KKaRbztGMtkFFULF3JJJmm0Z4Ca8w-_2Ux4ItYyVfFykhKVhPVsJmRiwfKwkzV8HCNvgu8A0HtN6ctRtBzEJQF_TBcF5teAgARoK2spM0q3qCTA93H7v23aLCDxrKjQ92DRXkH5_c3QkboPjQuIQiY5y0doveqqn2JB0xLrLCp_aTBCWakTvmVM9lV8XlMCa7DJ3EAcXmtzJpa6RHWyu_GCTsFOrLcA4rSkjJpcHTFSAS0Lj925YjH8vWlNVBMAVtBHR_ycj_clqvbCmrm_OGVX6z06xjco9IE5DmxDJcwZAc7xG3p2h98xU-K2DWUDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۰ نکتهٔ مهم برای حضور در تشییع رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/446206" target="_blank">📅 12:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446205">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38064a6885.mp4?token=Dly3LsT5ZtMW7Kc0gPl-RiH8aEU292TX3EqwKtjwX4O9_PCCKv-mWQMJmOoyhDxCh4mgrwz0mj1cJctnX8dx5eJr02BPA2svoMdI5BLB82t0C96vuFKWBjjt-hOtdvtK-P6Ndwv7wZabqFf9z1X9Qjp1RJ-Qwj1j-J0px9Dr1yUaiGCk2UguOt7i1gYvZG_Fl8HhFYL7YkEYHbyDGzyox4Q725oF5a3HeqJ92txrvZM-1F43zDptK4kd_BhXLsXTsZ2BQ4ync0trOly2JVS0XkcNIsNy40iTnvOOjqq-b5Ij6PIlVoM_d7TNc6ADu26q2xKQ12-4ipZcwFjyc4sVlF8iYoUVpNi8m_zMhIRrGkz1ylWSYRlBjYFYefToP91RitX9NWPRbvA7NGSUERz6-FvAJqiiQRlXJ0FCHbrtXjhdvJTzLH9wOXp4VgpFmmQqUEi41XyqL15flp5UFHQ7BPXoD9h4rGZybASf6U12kfDHifyYAFwoE-OT-noNYOeRQmwVWfKS_wkG6ZwBPzE8laB9z2YuvvSFKgv4K-XHQtyf-RPdwbf2YrmVHdv9950n2AThrgT6a-KKEdUxLHvjPkM8y3dD82qz_GV3utFWoqluNjzGQbHyIdSEjarJ6lU1OTUBZmR5kQ62vHY-LM2XebvHnWAf4tHJKfWjUZCFdpI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38064a6885.mp4?token=Dly3LsT5ZtMW7Kc0gPl-RiH8aEU292TX3EqwKtjwX4O9_PCCKv-mWQMJmOoyhDxCh4mgrwz0mj1cJctnX8dx5eJr02BPA2svoMdI5BLB82t0C96vuFKWBjjt-hOtdvtK-P6Ndwv7wZabqFf9z1X9Qjp1RJ-Qwj1j-J0px9Dr1yUaiGCk2UguOt7i1gYvZG_Fl8HhFYL7YkEYHbyDGzyox4Q725oF5a3HeqJ92txrvZM-1F43zDptK4kd_BhXLsXTsZ2BQ4ync0trOly2JVS0XkcNIsNy40iTnvOOjqq-b5Ij6PIlVoM_d7TNc6ADu26q2xKQ12-4ipZcwFjyc4sVlF8iYoUVpNi8m_zMhIRrGkz1ylWSYRlBjYFYefToP91RitX9NWPRbvA7NGSUERz6-FvAJqiiQRlXJ0FCHbrtXjhdvJTzLH9wOXp4VgpFmmQqUEi41XyqL15flp5UFHQ7BPXoD9h4rGZybASf6U12kfDHifyYAFwoE-OT-noNYOeRQmwVWfKS_wkG6ZwBPzE8laB9z2YuvvSFKgv4K-XHQtyf-RPdwbf2YrmVHdv9950n2AThrgT6a-KKEdUxLHvjPkM8y3dD82qz_GV3utFWoqluNjzGQbHyIdSEjarJ6lU1OTUBZmR5kQ62vHY-LM2XebvHnWAf4tHJKfWjUZCFdpI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود رئیس‌جمهور تاجیکستان به تهران برای وداع با رهبر شهید  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/446205" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446204">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اطلاعیه شماره ۲ آستان قدس رضوی ویژهٔ مراسم تشییع و تدفین رهبر شهید انقلاب
🔹
آستان قدس رضوی با اولویت قطعی تداوم جریان زیارت و خدمت‌رسانی شایسته و ایمن به زائران عزیز، تمهیدات لازم را برای برگزاری شایسته مراسم تشییع و تدفین رهبر شهید انقلاب اسلامی و دیگر شهدای گران‌قدر از خانواده معظم ایشان پیش‌بینی کرده است.
🔹
در همین چارچوب و به‌منظور فراهم‌سازی مقدمات این مراسم باشکوه و معنوی، تمهیدات و تغییراتی در فرایند تشرف به زیارت بارگاه منور رضوی مدنظر قرار گرفته است.
🔹
بر این اساس، جریان زیارت و تردد زائران در صحن‌های پیرامونی حرم مطهر به‌صورت مستمر و بدون وقفه تداوم می‌یابد و محدودیت‌های تشرف و تردد، صرفاً در صحن‌ها و رواق‌های مرکزی حرم مطهر رضوی، از ظهر چهارشنبه ۱۷ تیرماه ۱۴۰۵ به‌صورت تدریجی اعمال می‌شود و تا پایان مراسم تدفین ادامه خواهد داشت.
🔹
از زائران حضرت شمس‌الشّموس(ع) خواهشمندیم این مهم را در برنامه‌ریزی سفر به مشهد مقدس مد نظر قرار دهند و با خادمان خود در اجرای هرچه شایسته‌تر این مراسم همکاری نمایند. یقین داریم همراهی و صبر شما، همچون همیشه، پشتوانه برگزاری آیینی در شأن حرم مطهر رضوی و رهبر شهید انقلاب اسلامی خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/446204" target="_blank">📅 11:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446203">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56e495a0e0.mp4?token=XMUKsmvT4idA4yh8A9ikHChduRPew7ffl6Gq3W7KzKRsn7GB68KEmnEw2IORwb5Ep9KBUadfYzdevspn-aTvGHWEfzdlaKexQoYmOLS8x4tR_5KYMDCvYu6Doa7Z-83SSF4q2x7cINSmxOVSfcOu4GhGUoTDbIoKfixcGhK9jUAQ2sHis2bTntmROqBK5LIqY2iO8DOSIAfLgu1Qel5KX75afAPZ5Rc1amfgL4L0SUTOwM3343qF6hUDg_CPLWIOmUTCy4bejBWIlP3Kn4JQYtOXbaD2zv57f_HAPXUlNZqUL5X6habPWbpk-OBttmBPLovn5ECYt6j5MRxylDEgejzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56e495a0e0.mp4?token=XMUKsmvT4idA4yh8A9ikHChduRPew7ffl6Gq3W7KzKRsn7GB68KEmnEw2IORwb5Ep9KBUadfYzdevspn-aTvGHWEfzdlaKexQoYmOLS8x4tR_5KYMDCvYu6Doa7Z-83SSF4q2x7cINSmxOVSfcOu4GhGUoTDbIoKfixcGhK9jUAQ2sHis2bTntmROqBK5LIqY2iO8DOSIAfLgu1Qel5KX75afAPZ5Rc1amfgL4L0SUTOwM3343qF6hUDg_CPLWIOmUTCy4bejBWIlP3Kn4JQYtOXbaD2zv57f_HAPXUlNZqUL5X6habPWbpk-OBttmBPLovn5ECYt6j5MRxylDEgejzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار رئیس اقلیم کردستان عراق با پزشکیان
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/446203" target="_blank">📅 11:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446202">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSSJQ7uPGcb7r0flV-C8dMgfm-FF65spOUAyOqY3ZVp1BYppY-YVYY2pAvb4aI6mJr8wgLCgpqWD_tarVeiWSXxj_gML4XprDZYLqUjbVLA45l4nqu9MLWk7Iv6MEJFZFaOGQVK1etbgTqTKJv4ooZ5N7Ou_NB3vwVYYcGoHYUd2gywz7B3ioalR_yBcTs9AXjqri7AWfL3dxyj3lWlqiX6QJ2CePzte-7T5LFePQF2lZGhYKEVPq_XmsWLtzt4JawKHGofBHLCH9IFZ1M1HaWYHtc3EMcSVJq73-TF8LM8uy4sbc8nn9Q14oxlJ2_mvSO1JE13GwRr28JSjRiE-Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازداشت یک جوان اسرائیلی به اتهام جاسوسی برای ایران
🔹
روزنامه یدیعوت آحارونوت گزارش داد دادستانی منطقه قدس اشغالی علیه یک جوان ۲۱ ساله به نام الی لیوون (Eli Levon) به اتهام جاسوسی برای ایران در دادگاه منطقه‌ای قدس کیفرخواست صادر کرده است.
🔹
بر اساس این گزارش، متهم در اواخر سال ۲۰۲۵ و اوایل سال ۲۰۲۶ با دو فرد که خود را «سینا» و «الکساندر» معرفی کرده و به ادعای دادستانی برای نهادهای اطلاعاتی ایران فعالیت می‌کردند، ارتباط برقرار کرده است.
🔹
به نوشته یدیعوت، این جوان مأموریت‌هایی از جمله عکاسی از اماکنی در قدس و ثبت تصاویر ساختمانی در محله بخاری را انجام داده و در ازای اجرای این مأموریت‌ها، مبالغی پول دریافت کرده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/446202" target="_blank">📅 11:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446201">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/765d628c1d.mp4?token=oEY8yboX2ue4vrKuT4KPvIoupXGoW5KlHdN_0R7soRhaTtAANUft4jusXxWYJkOoYihaMNgMy68EZltu59E5vg8QrLnh9Muuf_TRuSeEuyVjr5bT52xH8b4e3r773bboY1t7rmhJkqdAotcKh1CQu2KiifjHFFqcOe3DnoLjwElTzJVuO4YYzI6BffgPlSCG1pWH1XGJfXvSvzSpfJHdIAzTEKAUgYwYTpTkpu-OaORsGk1m8ZF6tuvE3OTLwA02NLkiuBADBnPoYPhxsX41bcloCpjUqctfoujaQIuqNLVEenq7c7n3Jawldwv04nLo9Iwwe4NKN2z7FKtMA-jwxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/765d628c1d.mp4?token=oEY8yboX2ue4vrKuT4KPvIoupXGoW5KlHdN_0R7soRhaTtAANUft4jusXxWYJkOoYihaMNgMy68EZltu59E5vg8QrLnh9Muuf_TRuSeEuyVjr5bT52xH8b4e3r773bboY1t7rmhJkqdAotcKh1CQu2KiifjHFFqcOe3DnoLjwElTzJVuO4YYzI6BffgPlSCG1pWH1XGJfXvSvzSpfJHdIAzTEKAUgYwYTpTkpu-OaORsGk1m8ZF6tuvE3OTLwA02NLkiuBADBnPoYPhxsX41bcloCpjUqctfoujaQIuqNLVEenq7c7n3Jawldwv04nLo9Iwwe4NKN2z7FKtMA-jwxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی و وزیر خارجۀ قزاقستان دیدار کردند
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/446201" target="_blank">📅 11:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446199">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df2fd6009a.mp4?token=iGvQWzmPCSVtCl4L7I1qmaP6QlNAIjlp_S9nBuFlj1grigvR7Sx53ozL-_Lmqw6onsG0j9DCIuIDlDdvVjs3MWQt1SqMHkzagso7tVvDQgOzWfYxUcZkbq9PuPH1ELhdpKcb4Of2QZ9cKegWp438_WWFIgabO1hTYJngqcVA6tsMDAlnBPoo3WEmWz_zQR1kS5Mfjw1u_PPFyT_dzhIKyiQnVG9WhNdfStajDg1HcOE0GqQvljyaRp_u70C75pIPgVCx4QIgNosnDzSkq1oEz9ckPnMehvwDtwPEGdKyZyjfgiDMgnevWSay2muHR5m1_TBKlWNsK2S1k1xqFXaOkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df2fd6009a.mp4?token=iGvQWzmPCSVtCl4L7I1qmaP6QlNAIjlp_S9nBuFlj1grigvR7Sx53ozL-_Lmqw6onsG0j9DCIuIDlDdvVjs3MWQt1SqMHkzagso7tVvDQgOzWfYxUcZkbq9PuPH1ELhdpKcb4Of2QZ9cKegWp438_WWFIgabO1hTYJngqcVA6tsMDAlnBPoo3WEmWz_zQR1kS5Mfjw1u_PPFyT_dzhIKyiQnVG9WhNdfStajDg1HcOE0GqQvljyaRp_u70C75pIPgVCx4QIgNosnDzSkq1oEz9ckPnMehvwDtwPEGdKyZyjfgiDMgnevWSay2muHR5m1_TBKlWNsK2S1k1xqFXaOkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود رئیس‌جمهور گرجستان به تهران برای مراسم وداع با رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/446199" target="_blank">📅 11:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446198">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">حزب‌الله برای رهبر شهید، مراسم یادبود برگزار می‌کند
🔹
جنبش حزب الله از مردم لبنان خواست در مراسم یادبودی که به خاطر رهبر شهید انقلاب برگزار خواهد شد، شرکت کنند.
🔹
این مراسم قرار است شامگاه چهارشنبه آینده در ضاحیه بیروت برگزار شود.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/446198" target="_blank">📅 11:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446197">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/705ec49c6b.mp4?token=Bw0KaHfiYktopJpnzZK4Ne9J0KzYoiXU_t4zMi_EeVLXah-U4tIJPG6AXsuywFPy8ZAOB_tiY32IinYQLXtxvP-jLQmn5fSiVbF2q0E3Btx1im5PlOec3zjylSYflZue8Pri6sIjwFzGAys8uJ9SlpMN1c1DJ5m1iLtyajiEA6vfTpW9Wbx34_oZAGhuwwbUjFz9qM58HAFbdVSMIETq0e-QNeNEHiY3k5Vp_hBywsJK7U2lupP-k80uhxBpAE62ztg-9iaEPrPrJa94j_vVZknZyVKNDQbsanKKnPVq1Mev8u3yuyrZ5l5mWhRADpBQOQDce9NnrfE5w-uOBy5RoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/705ec49c6b.mp4?token=Bw0KaHfiYktopJpnzZK4Ne9J0KzYoiXU_t4zMi_EeVLXah-U4tIJPG6AXsuywFPy8ZAOB_tiY32IinYQLXtxvP-jLQmn5fSiVbF2q0E3Btx1im5PlOec3zjylSYflZue8Pri6sIjwFzGAys8uJ9SlpMN1c1DJ5m1iLtyajiEA6vfTpW9Wbx34_oZAGhuwwbUjFz9qM58HAFbdVSMIETq0e-QNeNEHiY3k5Vp_hBywsJK7U2lupP-k80uhxBpAE62ztg-9iaEPrPrJa94j_vVZknZyVKNDQbsanKKnPVq1Mev8u3yuyrZ5l5mWhRADpBQOQDce9NnrfE5w-uOBy5RoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون رئیس‌جمهور ترکیه برای شرکت در مراسم وداع با رهبر شهید وارد تهران شد
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/446197" target="_blank">📅 11:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446194">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a01edc6a9.mp4?token=tM_WeBOzAw1mmisT3xEx-SqL_Z7OQ9l945briaFXRHweVt8umtXQ7VOCScPUEu4JJWrxdfj1940PdzHcgN0wv6_J0D2M9_OYOKKDz5IaJEgqWl1zYDLVakEdFkx3TUT4Sk-KLod8AMQRHgaPA0ni0DcucE4EhEavv8TGln_X5XpVtKdvo6_vKDp5QWmZ5dSDZdt9ZwUSIzC7Qq7ecKLGQ9vYHbMixYCoJ9k8v9g6C87Y6c0_WZaC9bQEhiNr_1yd5-7RPDN50Wi9ROqotb_ZyK0LedUJPHztLSDEFNFbB81UVilEq6fDz8pZpEh2Z-dpDarY0KqWC8ZK17jiq8EUhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a01edc6a9.mp4?token=tM_WeBOzAw1mmisT3xEx-SqL_Z7OQ9l945briaFXRHweVt8umtXQ7VOCScPUEu4JJWrxdfj1940PdzHcgN0wv6_J0D2M9_OYOKKDz5IaJEgqWl1zYDLVakEdFkx3TUT4Sk-KLod8AMQRHgaPA0ni0DcucE4EhEavv8TGln_X5XpVtKdvo6_vKDp5QWmZ5dSDZdt9ZwUSIzC7Qq7ecKLGQ9vYHbMixYCoJ9k8v9g6C87Y6c0_WZaC9bQEhiNr_1yd5-7RPDN50Wi9ROqotb_ZyK0LedUJPHztLSDEFNFbB81UVilEq6fDz8pZpEh2Z-dpDarY0KqWC8ZK17jiq8EUhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تظاهرات ضداسرائیلی در فرانسه در هزارمین روز جنگ غزه
🔹
همزمان با فرارسیدن هزارمین روز جنگ غزه، هزاران نفر در پاریس، پایتخت فرانسه، با برگزاری راهپیمایی سکوت، یاد قربانیان این جنگ را گرامی داشتند و خواستار پایان حملات اسرائیل به نوار غزه شدند.
🔹
شرکت‌کنندگان در این مراسم با همراهی صدای طبل و در سکوت در خیابان‌های پاریس حرکت کردند تا به گفته برگزارکنندگان، نسبت به تداوم کشتار غیرنظامیان فلسطینی اعتراض کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/446194" target="_blank">📅 11:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446193">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bB9Cxz-9Bs5KHMVGHmRoiqYJ--KfJeCr-ltEnAoe2zQ2FZltitSDJZQhQ81hVJ8vmJIJgqCHlBU4sO9wHqR_-kPnukh8Q_wpJQktt8HF8AphwLGQP7TSKl1bHgaUeavUxlH4VAafRGzpLaNYL_OksNfVMJ-91B9bFg_BxjMeZM8QhhHiX6vEPmyGNfp2FEkOiZVBP0hOPUy5-2CMGRhjXEMeOjIpnbV9KeacsiNg6hElldyYpUqhE0rOKUGwc1J5wEEiZaDU5JiY5EiL_n7WxMLctlTj_7J5CtBbOVLFBxnSmHIRV_NtgVfBQjB6mz1_QRvq6H6MEYerGAV-raZTuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ورود نخست‌وزیر ارمنستان به تهران برای شرکت در مراسم وداع با رهبر شهید انقلاب @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/446193" target="_blank">📅 11:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446192">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6a3c0ca20.mp4?token=E7x6sb1tpB7j3JX47-vZUP00k7uBmLN8p0ZzLu5nxpJsQ92Nhjan75C9kut6ZwJCZj3q-4bYWeo1azbu8NYnUT1ELnhyNnoz9WtScqAJdwjxXXnfb58BJdcHeOwRy6NCO01Cpky34nCSoCg_Iwno882dBm4KJRN7ggAFzJ2Qt-9MyBTq-5kK5pgg0u6bgYVgtzDf3ivlg2W_A4DydwCa06GTihg8WXMhXOPQcKYFdoljQ7uTt9a7KcBjKtFw41d6l9tPaoafwrzmmzRBWkssqAHPaGuitI_jtUzCWvy5ugScEfuQN19BK80BuVvsYlCvRkoe0gUGDLQLLVVVgxytGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6a3c0ca20.mp4?token=E7x6sb1tpB7j3JX47-vZUP00k7uBmLN8p0ZzLu5nxpJsQ92Nhjan75C9kut6ZwJCZj3q-4bYWeo1azbu8NYnUT1ELnhyNnoz9WtScqAJdwjxXXnfb58BJdcHeOwRy6NCO01Cpky34nCSoCg_Iwno882dBm4KJRN7ggAFzJ2Qt-9MyBTq-5kK5pgg0u6bgYVgtzDf3ivlg2W_A4DydwCa06GTihg8WXMhXOPQcKYFdoljQ7uTt9a7KcBjKtFw41d6l9tPaoafwrzmmzRBWkssqAHPaGuitI_jtUzCWvy5ugScEfuQN19BK80BuVvsYlCvRkoe0gUGDLQLLVVVgxytGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام جمعی از فرماندهان مقاومت اسلامی به پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/446192" target="_blank">📅 11:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446189">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A6wpycsqhcZX56E00SmI1qesGYcAEv_rVKLYsLnZ44YdYf5KpnZXo_ooBoSLjs5YKWaF76yk2yUm9OwwA3YNUk60Z1bmFDe6VrtDwdqkXLEP2kZ18yfYl1cAkfRGzMo2xXLTIeIcdAVCAPLMAxZwOTvRpVDS5hASoL0Vny7YiVFe0JhmyPrTcCDvQ9scYkk0zHRpTjvYBhxaBiUlz1QKhujHKB2VIlBOhKgX_CXE8sCOpxwVBR38GR_iUIiO3m2UD0lJjcipuaa-xSOf67ktbDws8FaVlpTkSUZSk1JEhvDU4TlWT62d4NOZcGEMy1z8U06FDEopDkTlVErmIMS1KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bianYvflU5xg7bsBzLwNAU0vLlMEwJ5SLlFix9RrI4qaTo87PhfCDSJ3_SnWks91-n6ZZvYPI9pLPdtO7L_0PzbeJtb4bpEJ3GOcmzLK1S0dAI_vcP8dIFh1wCUaQ-wQinkXXuZo-RqrIm432V21YGVviGncGD1DBlwJJnVC7l1MoOlUtByMwx-C7-mzecwKN0ambe4ZqM7KumejZfS8P13xsjLYl6O403gMoLalyMEC-GkKG025_8s0S5ZMozrjpEZB2wCHsOh_-p8EnVvvFpSsB6Biw-bbmwsuiO1LSBuKYQNqaCFdqJpEr6jgq1NgA32oYx4s3HzM7pwtEEmovQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tvy-mSPMlNsSLoQkNtvQ3sTrFuqKAEw-w-9lTqXpP2WJOfPifDGacLVemLzAODfqoYetSRkfpe0zrTi12c8l6wTx6EKvhg4TFRrE7_U7NePTlSfSie71rVN_6qAIn32jAtUmmus6BEj1HPjsQaF4c6zbiVC0BanQs6XYWKh6FZ1KLSu8tJGJ0RNdutkNN6kmAkYN30P4qCIuu71Y7vZHBTrKvDcXvvQp4xcxqxhWJkxqJL75JvO7no9QRl3KWdaeLhahJDxfXXTzuvid0kvkJIbwdYWDDWbJgIUK2Mi87o7wGw_EATXljJ_4WqyLsEyEEaT0rwgBT9GlMhqPMmemDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار رهبر ملی ترکمنستان با پزشکیان
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/446189" target="_blank">📅 11:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446188">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da991e29b8.mp4?token=l4T5I6ekMuSiGN-zY1KrFOVDdcMjsvUZylBsP5k_hLSrxUOK8dbvE1peva0YBe3jUDi0mNkx39Ul2CG7I8EH0XZUGo8Jl10QQIkkrK9oo4hR74njKllHqJ3xFm-H0gc3UWoHfDHmq1GsL1cKMDkByMC_byml7xwPejduMyh0mC1JCLVb-XPA8EOL48dwWnfPp9h2aRjZ4bAxWVh3R9AaNFDPffnqKNrJHAKtn8ewi4zvZOCN-ivZd0XA7iWfh1PXvjRoF3XRiFh7sGiTUjjELos3lB4h2Mtd0DuN2WDch8pLum-LsStiLy65VzVtbueH2fAgG88vjozVw3ZEK2PMRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da991e29b8.mp4?token=l4T5I6ekMuSiGN-zY1KrFOVDdcMjsvUZylBsP5k_hLSrxUOK8dbvE1peva0YBe3jUDi0mNkx39Ul2CG7I8EH0XZUGo8Jl10QQIkkrK9oo4hR74njKllHqJ3xFm-H0gc3UWoHfDHmq1GsL1cKMDkByMC_byml7xwPejduMyh0mC1JCLVb-XPA8EOL48dwWnfPp9h2aRjZ4bAxWVh3R9AaNFDPffnqKNrJHAKtn8ewi4zvZOCN-ivZd0XA7iWfh1PXvjRoF3XRiFh7sGiTUjjELos3lB4h2Mtd0DuN2WDch8pLum-LsStiLy65VzVtbueH2fAgG88vjozVw3ZEK2PMRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام حدادعادل و جمعی از مقامات کشوری به پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/446188" target="_blank">📅 11:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446187">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01d988089.mp4?token=SWly007gxZzmupDAbckmJNVD3wVMnwcd9UqqrACU51AMXvezEFKFY96ADjpXx5i0Ch7zeJq9kptVWJuKE0dFW7279a9wMqDd_T0QOewYPeiDFXvWcaXi2de6BD6T77EOGHrjn9SLU9UkCt1R-PFPUbzpS-KOVkKhhuTe9rd4VY8N6TGIVa2tY15aCXwCKjZu5K6xuFhPQvJjSBlNWO0eisf1uDIoVDvhsrFXyRUPqB9yzkWTXD9BrMqPpn9WOFb2Gzl3pyJeg_kWxelRJx5dX6YY_y5LPYOCPZInIa42mExYJ-zY86wucIIVM3XwBtrb-mXGU1iG87gz4ClTSX_oPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01d988089.mp4?token=SWly007gxZzmupDAbckmJNVD3wVMnwcd9UqqrACU51AMXvezEFKFY96ADjpXx5i0Ch7zeJq9kptVWJuKE0dFW7279a9wMqDd_T0QOewYPeiDFXvWcaXi2de6BD6T77EOGHrjn9SLU9UkCt1R-PFPUbzpS-KOVkKhhuTe9rd4VY8N6TGIVa2tY15aCXwCKjZu5K6xuFhPQvJjSBlNWO0eisf1uDIoVDvhsrFXyRUPqB9yzkWTXD9BrMqPpn9WOFb2Gzl3pyJeg_kWxelRJx5dX6YY_y5LPYOCPZInIa42mExYJ-zY86wucIIVM3XwBtrb-mXGU1iG87gz4ClTSX_oPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام هیئتی از بانوان ‌طلاب و  فعالان عرصهٔ بین‌الملل به پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/446187" target="_blank">📅 10:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446186">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/652fcc680d.mp4?token=Gei8qOXTcA_DbcVtveAy5626d81zth4nMhBzvL9zehXrEYF-6T3aFHhg--aQrHEo_LhsWmBzOFp9hjm8R1rEO-LOGtgAQjXNJekjWIPlCIM5WsfcCT3H1RYWnTcQXJ4-Hbjs4RwNyDfCD6XKranHJyoEMvTSryOAhInOAvbFw3POb8FrbshwXvQdBiqeCadWLK9KeoRHWTVdvCQZ8-g-iwqFhZ47Ssoyc4JRwQqaWEq9y-Dfag095LW7IQ9hbhdU_jX-6Rt1z4-yOrzlfoypJ-ke7mm2u0LeBLTAjlixAP3lAyM9lPrHQvR6PFiPGu0xF93QTQ3lagzkQxD1Npe7jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/652fcc680d.mp4?token=Gei8qOXTcA_DbcVtveAy5626d81zth4nMhBzvL9zehXrEYF-6T3aFHhg--aQrHEo_LhsWmBzOFp9hjm8R1rEO-LOGtgAQjXNJekjWIPlCIM5WsfcCT3H1RYWnTcQXJ4-Hbjs4RwNyDfCD6XKranHJyoEMvTSryOAhInOAvbFw3POb8FrbshwXvQdBiqeCadWLK9KeoRHWTVdvCQZ8-g-iwqFhZ47Ssoyc4JRwQqaWEq9y-Dfag095LW7IQ9hbhdU_jX-6Rt1z4-yOrzlfoypJ-ke7mm2u0LeBLTAjlixAP3lAyM9lPrHQvR6PFiPGu0xF93QTQ3lagzkQxD1Npe7jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام هیئتی از جمعیت اسلامی کشور بنگلادش به پیکر رهبر شهید انقلاب اسلامی
.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/446186" target="_blank">📅 10:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446185">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aa82a200d.mp4?token=Vh9_8v1FoewSna9LLyYelstVWeIsm8Mfr4qOrO14TTZ5RRo-abF3JfC_12Rv0u_n5hNk4cjS-MQQCInP20ozQDMvJL3iiFt7UmNTqhAg8nKebpKZwLHWy9ZlCOTm3UYLwdrvlSwF6YA17TSspsuxNdxjiFCiCOjPwvqvxbf3EdiHdDBWpn8P2n7WvPOr-V02Kz-t_UpTMFmaC3NqUsdm8sQToxTefw9BKJvOl1mbbGgSoNubUOFyG5sFnnxi_j2tEUB8ulPNjTwmhYjf72nd9g7N03ds0x7HCS-Ut36zDBIWFyak-bFLbqJicynuPd9hZNXyd8arfzQkE9CdG_S0gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aa82a200d.mp4?token=Vh9_8v1FoewSna9LLyYelstVWeIsm8Mfr4qOrO14TTZ5RRo-abF3JfC_12Rv0u_n5hNk4cjS-MQQCInP20ozQDMvJL3iiFt7UmNTqhAg8nKebpKZwLHWy9ZlCOTm3UYLwdrvlSwF6YA17TSspsuxNdxjiFCiCOjPwvqvxbf3EdiHdDBWpn8P2n7WvPOr-V02Kz-t_UpTMFmaC3NqUsdm8sQToxTefw9BKJvOl1mbbGgSoNubUOFyG5sFnnxi_j2tEUB8ulPNjTwmhYjf72nd9g7N03ds0x7HCS-Ut36zDBIWFyak-bFLbqJicynuPd9hZNXyd8arfzQkE9CdG_S0gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام هیئتی از ارمنستان به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/446185" target="_blank">📅 10:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446183">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90978d21ad.mp4?token=MJFF7sFFPNgay9sm-vHwZGbhJ6KPPNXazfPcVWRE44XSi718Mw2iYDeDyX6X_AsRabpEUiRq1pwBQ-_2xeQROzZ-WLBptWWcO9jOqnpl7NnSZMT96kVxCTtdw-gyif-Z4oKI3LmHLMmRrAjEXgiq_7cC0pj3XZ1NR6L0fIpvy_tDbqV6sbaDH29_x6X_XaqiZ60sDhMCJs3_ZmP9TlrZjH0FUoZKI-I1y-EiZl4CZtZnpaF3taFn_7kSlQNyikB6VKir2UBgzud38Qwt-mcGsAbIIgSh3idE_sf_2hUMtUplORlqZTy3R3R-62Vhc0ZNAwuyQma80zPmHMbMT7n1kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90978d21ad.mp4?token=MJFF7sFFPNgay9sm-vHwZGbhJ6KPPNXazfPcVWRE44XSi718Mw2iYDeDyX6X_AsRabpEUiRq1pwBQ-_2xeQROzZ-WLBptWWcO9jOqnpl7NnSZMT96kVxCTtdw-gyif-Z4oKI3LmHLMmRrAjEXgiq_7cC0pj3XZ1NR6L0fIpvy_tDbqV6sbaDH29_x6X_XaqiZ60sDhMCJs3_ZmP9TlrZjH0FUoZKI-I1y-EiZl4CZtZnpaF3taFn_7kSlQNyikB6VKir2UBgzud38Qwt-mcGsAbIIgSh3idE_sf_2hUMtUplORlqZTy3R3R-62Vhc0ZNAwuyQma80zPmHMbMT7n1kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام جمعی از نمایندگان پارلمان عراق، شیوخ، عشایر، احزاب اسلامی و احزاب منطقهٔ کردستان عراق به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/446183" target="_blank">📅 10:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446182">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e789c04085.mp4?token=m59aXZX70nC-NrFx7mWmF4orCY03EL1Yt4Q6jxJd98JW72OiSaTSJq-YdQb2Dgw-3J3RnYFCPwYX8LXsrOueEyRVxuTGsojwW2q8dJ4NLHirjoGw7CdqdWzZbF6UISJC2YiNZJltQN_4cdLNEl8aup-AMCY74ptl1fxh102rEKYvPGPB6g2uFQjgKxvnq_KA7y1Bez7E1iTgcOOC9GmaGEjNyZqIx78MrM4StIi2WfE9eAGU7LGm81RpveHP1h8EUtpToqdIhEZBkev7u8nmEtXH3kcMAAlATl2Ckd2obiSyaRL959nvmtSHzaR5bARam0n-SdwwdYmwF1yNRQWEjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e789c04085.mp4?token=m59aXZX70nC-NrFx7mWmF4orCY03EL1Yt4Q6jxJd98JW72OiSaTSJq-YdQb2Dgw-3J3RnYFCPwYX8LXsrOueEyRVxuTGsojwW2q8dJ4NLHirjoGw7CdqdWzZbF6UISJC2YiNZJltQN_4cdLNEl8aup-AMCY74ptl1fxh102rEKYvPGPB6g2uFQjgKxvnq_KA7y1Bez7E1iTgcOOC9GmaGEjNyZqIx78MrM4StIi2WfE9eAGU7LGm81RpveHP1h8EUtpToqdIhEZBkev7u8nmEtXH3kcMAAlATl2Ckd2obiSyaRL959nvmtSHzaR5bARam0n-SdwwdYmwF1yNRQWEjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام نمایندگان احزاب ملی سیاسی لبنان به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/446182" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446181">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df2cab2b78.mp4?token=FETHt_cB5d8rNff4uTaydRj2h4xHuVupgZ4HAqIf9hnYR5bvnKm2I-vJk-DM8rhIus8wXcyXPFQ_HEA9pmI-BpGQgIMy_QhqjXj44NGNjU3At4B4nMsa2-xbLxULaiIccBuPtNX14uqH6-tb69wmu_aG3ixJTWbnDSardNGDduyj8cOrMl-HnBQanXPGe1RXIAe-GnETft7cuGnXfc9J6eC_GFqtMMZbb0Gp0ohDUoN-0i_muhqgbJ4JXNWnsQYllWWTJolDsXg86jFUUP4W2SlV5-iUGisbxDXV8CsJnfWOZb4adD2owfeA7xzcCarBoTC84T9_aPO4oGiQxBnorA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df2cab2b78.mp4?token=FETHt_cB5d8rNff4uTaydRj2h4xHuVupgZ4HAqIf9hnYR5bvnKm2I-vJk-DM8rhIus8wXcyXPFQ_HEA9pmI-BpGQgIMy_QhqjXj44NGNjU3At4B4nMsa2-xbLxULaiIccBuPtNX14uqH6-tb69wmu_aG3ixJTWbnDSardNGDduyj8cOrMl-HnBQanXPGe1RXIAe-GnETft7cuGnXfc9J6eC_GFqtMMZbb0Gp0ohDUoN-0i_muhqgbJ4JXNWnsQYllWWTJolDsXg86jFUUP4W2SlV5-iUGisbxDXV8CsJnfWOZb4adD2owfeA7xzcCarBoTC84T9_aPO4oGiQxBnorA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع جمعی از اعضای حزب‌الله لبنان و خانوادهٔ سید حسن نصرالله و عماد مغنیه و فرماندهان شهید حزب‌الله با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/446181" target="_blank">📅 10:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446180">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2d477d6c.mp4?token=RBJCfEw5Hx1_7l95ODy6PSffPWTZxXm9uclEeey3A_irCFXCRjKtKB3Y7hrhdEjeRmELlQvOdfFWtPC0WWmkBl7c9zChv6_HoxZcbER0qQy8a4DjZmdHH_zE3G3mb7H42EKPCW5Qiw__KmyrrCqTvGUgADq50cFL3x_B6DvBxZFesbXKok2X7XJck8tvq6QUCstUPWf6YsYyS3m09i-k40JNXILKPKNddh6-0mUjvndM-vYxXg44Zi_KoEazMv-vQqORp8TZ-osWb0dUTLivJz2W3BwTwl1BzlpilZFixq7x-YSYc3CH4rJGlnBjE4Tjw2rky2YNlWCOmQKJ8A_oOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2d477d6c.mp4?token=RBJCfEw5Hx1_7l95ODy6PSffPWTZxXm9uclEeey3A_irCFXCRjKtKB3Y7hrhdEjeRmELlQvOdfFWtPC0WWmkBl7c9zChv6_HoxZcbER0qQy8a4DjZmdHH_zE3G3mb7H42EKPCW5Qiw__KmyrrCqTvGUgADq50cFL3x_B6DvBxZFesbXKok2X7XJck8tvq6QUCstUPWf6YsYyS3m09i-k40JNXILKPKNddh6-0mUjvndM-vYxXg44Zi_KoEazMv-vQqORp8TZ-osWb0dUTLivJz2W3BwTwl1BzlpilZFixq7x-YSYc3CH4rJGlnBjE4Tjw2rky2YNlWCOmQKJ8A_oOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع جمعی از اصحاب رسانهٔ لبنان، عراق و افغانستان با پیکر مطهر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/446180" target="_blank">📅 10:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446179">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/931974eef8.mp4?token=d0FaRZV-9jime-p8ppyf1Y_Y_k7Vwuw7HMZLyVSF-CuTMHQLgoDvVM5p0352m9kdB5BRKIblMkjlguAtQtjhZwnENFKOqj3UbW65yjh2txycEGpeGoTpNGYAAJkrifdqYXXhWy0Gsn3bHw2HriIwBf4UcCSQsCJ3h0itgPVL2rEM0gyFmCLNa9KUCC_ODGGwdBNngKRgiOszfVj_DfkeYHLtNvBOVuZIrXOzcf37COS7G2Ul7alpocRetCN50oLIwZ94WQRAoHT0VFOqJm8Gfr2eZijwn6EAONnGMvp_269qRrH-ks8shCKFQXato5aNOZiMeYk-dKg0bCshoa27fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/931974eef8.mp4?token=d0FaRZV-9jime-p8ppyf1Y_Y_k7Vwuw7HMZLyVSF-CuTMHQLgoDvVM5p0352m9kdB5BRKIblMkjlguAtQtjhZwnENFKOqj3UbW65yjh2txycEGpeGoTpNGYAAJkrifdqYXXhWy0Gsn3bHw2HriIwBf4UcCSQsCJ3h0itgPVL2rEM0gyFmCLNa9KUCC_ODGGwdBNngKRgiOszfVj_DfkeYHLtNvBOVuZIrXOzcf37COS7G2Ul7alpocRetCN50oLIwZ94WQRAoHT0VFOqJm8Gfr2eZijwn6EAONnGMvp_269qRrH-ks8shCKFQXato5aNOZiMeYk-dKg0bCshoa27fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام هیئت شعبیهٔ فلسطین به پیکر رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/446179" target="_blank">📅 10:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446178">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2a90374e8.mp4?token=UU3nlRCKzsQPz6nStvjLh1BAtodOWgedCS1MgzhKto7rgTn3Oh-xpCGTISpaVq-0Jtox5bG-FoM0zMke7iS7AthMkR6OtscibbZAFwN3FyAcg8eJg0CNLWok9LDRVXLvO2jv_KpmMNs0LH7DeWDBHGjv6G1bZXmfyjK0xxlm7CsQHOYvYhiA45HWEyRGjKIMZZQVImtNuShC7-y6L3XWua24rnleN3pnn-n--RUlv5RXjRYbNzETbZ4OBUGBPxaFY6pSdBCH-DHtGV0GPTnzZAKtUV0c-CQgfjbPTaBjNMJlq0xqc7SolfvD1qDU5pSnqP2kcD6TbRZmwrt_HfCwZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2a90374e8.mp4?token=UU3nlRCKzsQPz6nStvjLh1BAtodOWgedCS1MgzhKto7rgTn3Oh-xpCGTISpaVq-0Jtox5bG-FoM0zMke7iS7AthMkR6OtscibbZAFwN3FyAcg8eJg0CNLWok9LDRVXLvO2jv_KpmMNs0LH7DeWDBHGjv6G1bZXmfyjK0xxlm7CsQHOYvYhiA45HWEyRGjKIMZZQVImtNuShC7-y6L3XWua24rnleN3pnn-n--RUlv5RXjRYbNzETbZ4OBUGBPxaFY6pSdBCH-DHtGV0GPTnzZAKtUV0c-CQgfjbPTaBjNMJlq0xqc7SolfvD1qDU5pSnqP2kcD6TbRZmwrt_HfCwZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام هیئتی از علمای فلسطین
به پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/446178" target="_blank">📅 10:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446177">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3baf406e7.mp4?token=ByJdQmpDF_tku9dlfeqRluBy2Om319w3kYfO76dvlppAUNKAcRTZi_43pyIhLFokAi_G438HUkRzdFh49e4khabotwG3FQH_pNXGMyd8C_0vWzqi2GSQc8Ock7ScyYpSPI5KYpleIDI_Df6FJOHiSVAsnDS57Rly1zsyICaNji2q3DFMFoC_7eXYm6cCq13g3fHdKr-eN5sX5nFJPr6yknk7evrj7qIpzMAv5pi0HVHE2z4XkqH_I3mz96ucsYD0Do9vjGLmfkZx5qWRg1wMxi5UyF1osyRwBZc_Rtd73GlMLDU0R-JTBRaREIfdNmzBYk2zyii88G7Vq6KKzSbEOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3baf406e7.mp4?token=ByJdQmpDF_tku9dlfeqRluBy2Om319w3kYfO76dvlppAUNKAcRTZi_43pyIhLFokAi_G438HUkRzdFh49e4khabotwG3FQH_pNXGMyd8C_0vWzqi2GSQc8Ock7ScyYpSPI5KYpleIDI_Df6FJOHiSVAsnDS57Rly1zsyICaNji2q3DFMFoC_7eXYm6cCq13g3fHdKr-eN5sX5nFJPr6yknk7evrj7qIpzMAv5pi0HVHE2z4XkqH_I3mz96ucsYD0Do9vjGLmfkZx5qWRg1wMxi5UyF1osyRwBZc_Rtd73GlMLDU0R-JTBRaREIfdNmzBYk2zyii88G7Vq6KKzSbEOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس‌جمهور عراق برای شرکت در مراسم ادای احترام به پیکر رهبر شهید انقلاب وارد تهران شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/446177" target="_blank">📅 10:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446176">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت باب القبله طهران</strong></div>
<div class="tg-text">نماهنگ«‌مسافر کرببلا»
قـرار بـود ما فـداشـیـم
سیـدعـلی فدای‌ما شـد
بـالاخره‌بـعـد یـه عـمـری
مـسـافـر کرببلا شـد
شعر و صدای:سیـدجواد پرئی
گروه‌سرود: بنات الحیدر
تنظیم : یوسف جهانی
کارگردان: اسماعیل بهرامی
تهیه کننده : رسانه «هیأت‌باب‌القبله‌طهران»
‌    ━━━◈❖✿❖◈━━━
اینستاگرام
|
تلگرام
|
واتساپ
|
بـله
|
روبیکا
╭━━⊰•═
🍃
═•⊱━━╮
@babolghebleh_ir
╰━━⊰•═
🍃
═•⊱━━╯</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/446176" target="_blank">📅 10:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446175">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/446175" target="_blank">📅 10:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446174">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cb65272d.mp4?token=j-aL2uPqSGltx_v73W9Cr5aE11gLL-ARZ9IV6bUhd5YJIrp34yx-DsnDpI-O8Pq8PZZ-BCrRtnxRuh_NY8FBaRRk60ZrMWjWGIzq73YPAEwJQeP5lsOb4JRtNz-rF1_Faa6DySXlsoVx0y7PO-jBsTpAUBqCLbe6Wsi9keCc-TsuLB4pb-wnVgSbONtlv489N44xgD70HHrIgMszJYn8eUzeY_qh3dSYSKDmquLSwfMhPAon12HwAOThXzl-WIh8kwDxOjtd-lcamoMFbuGWBxXmZFXnJ3IXGawxDZbO0_mALFl8g-GHCPhcwffvtdiF-zDg08_cKA_2mCX8r4nMSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cb65272d.mp4?token=j-aL2uPqSGltx_v73W9Cr5aE11gLL-ARZ9IV6bUhd5YJIrp34yx-DsnDpI-O8Pq8PZZ-BCrRtnxRuh_NY8FBaRRk60ZrMWjWGIzq73YPAEwJQeP5lsOb4JRtNz-rF1_Faa6DySXlsoVx0y7PO-jBsTpAUBqCLbe6Wsi9keCc-TsuLB4pb-wnVgSbONtlv489N44xgD70HHrIgMszJYn8eUzeY_qh3dSYSKDmquLSwfMhPAon12HwAOThXzl-WIh8kwDxOjtd-lcamoMFbuGWBxXmZFXnJ3IXGawxDZbO0_mALFl8g-GHCPhcwffvtdiF-zDg08_cKA_2mCX8r4nMSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جمعی از رهبران هندو، شیعیان تایلند و شیعیان آلمان به رهبر شهید انقلاب ادای احترام کردند
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/446174" target="_blank">📅 10:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446173">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e981b69479.mp4?token=ZlOk5N3ok99i27b27NSOtTTxw0CTtXfkgASXMwJQRQIHN6jjuk_9SvA6klF6CZzoBJaW7yROU3-tDa8pDq1MZpSgEICIDrmfU6wHHmQYPro_1bmjSvyguHbXQHJKHZVepHViw19MrlDKEC6CNZ91UnWRDASor-USuzpoooK1MHiIZjnej4dXmTSHP1DG6yEp3i3ZYrZHIhZGHu4ZQk4FPpJfXxVsagNtyw5ThKfn3hv3VApMv8ERQpEsJXnIOYBzy6_d4YeYHo6Z2fC6sXhPhdCe3uUBSn1JcVuqqK2nhRfGE4d7ABvANgTxuu413-c4iiuMb99L7wzZeI981cIOPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e981b69479.mp4?token=ZlOk5N3ok99i27b27NSOtTTxw0CTtXfkgASXMwJQRQIHN6jjuk_9SvA6klF6CZzoBJaW7yROU3-tDa8pDq1MZpSgEICIDrmfU6wHHmQYPro_1bmjSvyguHbXQHJKHZVepHViw19MrlDKEC6CNZ91UnWRDASor-USuzpoooK1MHiIZjnej4dXmTSHP1DG6yEp3i3ZYrZHIhZGHu4ZQk4FPpJfXxVsagNtyw5ThKfn3hv3VApMv8ERQpEsJXnIOYBzy6_d4YeYHo6Z2fC6sXhPhdCe3uUBSn1JcVuqqK2nhRfGE4d7ABvANgTxuu413-c4iiuMb99L7wzZeI981cIOPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام نمایندگان پارلمان و عضو حزب احیای جمهوری بلغارستان به پیکر رهبر شهید انقلاب اسلامی
.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/446173" target="_blank">📅 10:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446172">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/351721101b.mp4?token=bfXhEUMoYPxdZ1eKt4-H-5pUKJ4y_CE0jQ9Pk4eZkPYR9lgDX8igHLmBA8peJa-IYItm_6LSju9mbNTbrCRTz1P4h_Dm4kfPkgrgYhpbP7HqhdXNjNGDc165ZC3TGdPsaggQHquxK422HFwhpYI9bl7qU98KzeNPv2X8mwmJeTFu9Rgo3vNLMR9_nTEqVH0rwOunhxNi66NDH0pWdP9oU_R55b0Pk5u_-rw8ks0Ol9BBcuMuPq9tjskjqZQ2v5v6XUzUAhLLwzuZuYeAd86aVVkFzCXGBnnyoCk78BcNvuEPHNJixqap6LL2-TqbLqPhMxyyROE17h0NOFbjY7MN5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/351721101b.mp4?token=bfXhEUMoYPxdZ1eKt4-H-5pUKJ4y_CE0jQ9Pk4eZkPYR9lgDX8igHLmBA8peJa-IYItm_6LSju9mbNTbrCRTz1P4h_Dm4kfPkgrgYhpbP7HqhdXNjNGDc165ZC3TGdPsaggQHquxK422HFwhpYI9bl7qU98KzeNPv2X8mwmJeTFu9Rgo3vNLMR9_nTEqVH0rwOunhxNi66NDH0pWdP9oU_R55b0Pk5u_-rw8ks0Ol9BBcuMuPq9tjskjqZQ2v5v6XUzUAhLLwzuZuYeAd86aVVkFzCXGBnnyoCk78BcNvuEPHNJixqap6LL2-TqbLqPhMxyyROE17h0NOFbjY7MN5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام هیئت علمای روسیه به پیکر مطهر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/446172" target="_blank">📅 10:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446171">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/905841b04a.mp4?token=gR5X67WySvBqDgt5X4NwzC-bs7c9vmXji2uk2pnyiljs5FLuBqDlrEzr4D6i0mNo86TWJNw0h62P594yv8yg75BzymE1mSJf-0TlKrIB5Gp-WBcYrfCNBRV4d1B4DhEdI8RbWZnvJX-OqozpZ_qC228fKvTSQmN4TPR_OhKcEJmzGlrILD01530pDme6QixtiDn1lvs-mEFb12WlqOllXbKfMIGqiSI4J8wIxpht0UZ1Co9E3ZLIXi8FGHjdt7aKhNZ4qUePnVu_BgXHjDV3dXnTInPy6HnGIWT8mgdNvWR5o3axlFuO-u9SizDmn4sUSKuJB3RUT46IJUixdz5-fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/905841b04a.mp4?token=gR5X67WySvBqDgt5X4NwzC-bs7c9vmXji2uk2pnyiljs5FLuBqDlrEzr4D6i0mNo86TWJNw0h62P594yv8yg75BzymE1mSJf-0TlKrIB5Gp-WBcYrfCNBRV4d1B4DhEdI8RbWZnvJX-OqozpZ_qC228fKvTSQmN4TPR_OhKcEJmzGlrILD01530pDme6QixtiDn1lvs-mEFb12WlqOllXbKfMIGqiSI4J8wIxpht0UZ1Co9E3ZLIXi8FGHjdt7aKhNZ4qUePnVu_BgXHjDV3dXnTInPy6HnGIWT8mgdNvWR5o3axlFuO-u9SizDmn4sUSKuJB3RUT46IJUixdz5-fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام هیئت احزاب ترکیه به پیکر رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/446171" target="_blank">📅 10:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446170">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/116bdea616.mp4?token=UGW5WUs_1Kbz630Wcp_ywIjyaGs_aKzWbzcbZsb3lmYGPUFOgbbMgUUUh0uaNkYAHMmmdKDUnXh7sfCFvJlEHy7URDpt3tatuV4AhC4cj37NojaIuV2tJ2j-WNgTS3T9RO73Lz8xnmUpkcIGm5I0SHdQ0pHAc6xAOa0et3hUGKrqp8plFdF9EoHX-JfrKzrV9aGpY5HKMXaQpRNMfwMQR04cTTOKc_nvgWnRw3fY6GICgduqhm7QJ-XJmIRBL4_ah098WQp9nyt5hVLQRXdAARYnnmNsYoUE1Aj__Vav1zT4zQ3XgyjZpZBRZyyi6rmSmiBpsP7g8DBQgJWi-5YbOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/116bdea616.mp4?token=UGW5WUs_1Kbz630Wcp_ywIjyaGs_aKzWbzcbZsb3lmYGPUFOgbbMgUUUh0uaNkYAHMmmdKDUnXh7sfCFvJlEHy7URDpt3tatuV4AhC4cj37NojaIuV2tJ2j-WNgTS3T9RO73Lz8xnmUpkcIGm5I0SHdQ0pHAc6xAOa0et3hUGKrqp8plFdF9EoHX-JfrKzrV9aGpY5HKMXaQpRNMfwMQR04cTTOKc_nvgWnRw3fY6GICgduqhm7QJ-XJmIRBL4_ah098WQp9nyt5hVLQRXdAARYnnmNsYoUE1Aj__Vav1zT4zQ3XgyjZpZBRZyyi6rmSmiBpsP7g8DBQgJWi-5YbOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع هیئت فاطمیون افغانستان با پیکر مطهر رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/446170" target="_blank">📅 10:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446169">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65551a3320.mp4?token=Sdd0DbRowV-m643PSOpLriD11C3sceNmApioao2D226C7OQWsjaV672NM_HKbFPHECRv3oACYRBklBtpmqA_uEMbdzDMTXlbBga5ALUG0sqNS3nGvBNItE-waRtBD_IGteDJbJAVZFXjxf73h26HokzsBGz2FmOKUPzB0InRRqDrUXH5LGTPM32Vv98wlgDnJtvdQWjnhOFcB2Dyt5N38IbrWvnyYZFyOQQA7fSfQlPjtrRJ2ic0Rl01PUL4zPSSz4vnRviXiKW9CeBfkfb8E0rr-3gMdYV__mn9YquleWHwtPHx4y_87WYSXq7gbYAiCJDH9h5gIR6hkCGwMpeN8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65551a3320.mp4?token=Sdd0DbRowV-m643PSOpLriD11C3sceNmApioao2D226C7OQWsjaV672NM_HKbFPHECRv3oACYRBklBtpmqA_uEMbdzDMTXlbBga5ALUG0sqNS3nGvBNItE-waRtBD_IGteDJbJAVZFXjxf73h26HokzsBGz2FmOKUPzB0InRRqDrUXH5LGTPM32Vv98wlgDnJtvdQWjnhOFcB2Dyt5N38IbrWvnyYZFyOQQA7fSfQlPjtrRJ2ic0Rl01PUL4zPSSz4vnRviXiKW9CeBfkfb8E0rr-3gMdYV__mn9YquleWHwtPHx4y_87WYSXq7gbYAiCJDH9h5gIR6hkCGwMpeN8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام هیئت اداره عالی مسلمانان گرجستان به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/446169" target="_blank">📅 10:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446168">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ab6c6104e.mp4?token=fpNfrWmD4Y1OFQjwdrophWVudXXjJOI542Ue0z4-okyCPeGoEsYdu4yIJ-hU8562BJp7-1mbMwAquoAOKqJEhi5TLtksrS9v44XSzvTk0rzoWyrhRD7ofGNqRbAyCIdWIwznF3ZsTq427xw3Onqu_afmQ9Oey8tu1zOZwfEZw-qlF_gdM72VyRAgT1MDvuXl2MKoH_WbWark1klPuKj3vVka87ePHQTPlIAvN5ZvCefh00O6l8oMuMphHESXfkp-JcuAZrpY9Eqvry3xaHVrK__sAZyM25wePaxrg1o2kCo6NV3AqOFTG_zY0evWnP1n9gVD06l_kK_XjLtEB75x_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ab6c6104e.mp4?token=fpNfrWmD4Y1OFQjwdrophWVudXXjJOI542Ue0z4-okyCPeGoEsYdu4yIJ-hU8562BJp7-1mbMwAquoAOKqJEhi5TLtksrS9v44XSzvTk0rzoWyrhRD7ofGNqRbAyCIdWIwznF3ZsTq427xw3Onqu_afmQ9Oey8tu1zOZwfEZw-qlF_gdM72VyRAgT1MDvuXl2MKoH_WbWark1klPuKj3vVka87ePHQTPlIAvN5ZvCefh00O6l8oMuMphHESXfkp-JcuAZrpY9Eqvry3xaHVrK__sAZyM25wePaxrg1o2kCo6NV3AqOFTG_zY0evWnP1n9gVD06l_kK_XjLtEB75x_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور
هیئتی از رهبران شیعهٔ پاکستان در آیین وداع با رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/446168" target="_blank">📅 10:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446167">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J81Gg1nT2NQXbMHZAxpl9tQkhVXGEIdmRoMlyVD4upif7Jbn-7vUcSfhvqbyBmSZUvtANdZrA9133TlXkxPXSkrIdGG06OXwPCKuVsR_DFAOBu0b1nTaPrnDJPV9tBq1hjS1rHN6LQGZY373aGK6mhDAB2hERA1ABqiwPaeIwH0fukYbu07ePhWV__HxxVNl9cXeHpR3XN8DTlNfImX_GQW-9Q57e6CI5EuqU5Z4bwSX0w7_un8nS6yG9zkbDieNVUXHSsrfE4_frtWgbZzzeyrcOZTaSRgzoO3DDDml0nbXqDDMuPaXEknFY3sZJBGkNTQPkoCi9GQrsMQvR4kEfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش سی‌ان‌ان از بدرقه آقای شهید ایران؛ نمایش قدرت و انسجام
🔹
شبکه خبری سی‌ان‌ان در گزارشی، مراسم تشییع رهبر شهید انقلاب را حامل پیامی از اقتدار و انسجام ایران به آمریکا و جهان خواند.
🔹
سی‌ان‌ان افزود، هدف از این مراسم، ارسال این پیام به جهان و دشمنان جمهوری اسلامی ایران عنوان شده که نظام نه‌تنها از جنگی موجودیتی جان سالم به در برده، بلکه رهبر شهید خود را به نمادی از مقاومت و پایداری تبدیل خواهد کرد.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/446167" target="_blank">📅 10:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446166">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77724b4de0.mp4?token=UY8BEO3WmpQoDbZAXvzo4kAQXMgm-9bhgBVw1Qg7U0iny-bdbdg8kf2wKTJY_PhPdnYviFqukbX8liwiA6RAAkQBgP6GqJ1l2u7_RAXClmiXIfFeuCo4jKm6PE5TGrLxXZe88r-BWrb-mkdwGLwHt9_YuQxjPvJPHI-fc2fnkcHdI9lyKMdYjuiomnRpaPNrehCbBe0pPy3D8sFB2LdWUlk5vfLfuuR7dHEzNGz_9jTT2QmpjTqBoPmikZBfxaD8ynjBeR1-BahoWUVTA08gGiLsgKzUdBUlaH-4nmSm3N5rR_JzhfpPrva-d4VL8yhg7YXHwVb6A4ssm_SY9i2y1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77724b4de0.mp4?token=UY8BEO3WmpQoDbZAXvzo4kAQXMgm-9bhgBVw1Qg7U0iny-bdbdg8kf2wKTJY_PhPdnYviFqukbX8liwiA6RAAkQBgP6GqJ1l2u7_RAXClmiXIfFeuCo4jKm6PE5TGrLxXZe88r-BWrb-mkdwGLwHt9_YuQxjPvJPHI-fc2fnkcHdI9lyKMdYjuiomnRpaPNrehCbBe0pPy3D8sFB2LdWUlk5vfLfuuR7dHEzNGz_9jTT2QmpjTqBoPmikZBfxaD8ynjBeR1-BahoWUVTA08gGiLsgKzUdBUlaH-4nmSm3N5rR_JzhfpPrva-d4VL8yhg7YXHwVb6A4ssm_SY9i2y1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود رئیس‌جمهور تاجیکستان به تهران برای وداع با رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/446166" target="_blank">📅 10:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446165">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9563db8921.mp4?token=l-hbTnv2RgJMvn6yIlp5xK7Pp5kJBfLeJztKDm3F2dF_RiPcJf08jrcBhvkHC5J1-FZn-NZsKoppxmUqNb0-sOBzuBUpIp0-z1EDlJ3oUDpR7jmfyyYLrMeZtGbNyYYTjugaDV7dPmaEvdL2skaAqp1JiiNmVf1SiMfmOXEINRDxeLuzunwXOHyIR_AfahN--9zFZNTsaEfSy5KK_t8BA8AorCWFrE7jsFAzb6IP09ppVUYmlphogiWOK1g3mJ0RBloLrrhALAmeJ2Q2TgvQnZrMxOz_UrW4uUG2wU8o9E2BHKI4InmzkrLKKETGEotI1ZBbxSoXoiVKYncK5SCDOQDqklcWtZZGulIw3r8LYdxOx7V-VSOrYjL5f1wqcqzROuuePEI0iSz_ROFGrxGs9f_HWo8rcwJnNycfKTMzXdKrNonqivgtFMWkmgUGMHPaXYPmnfJzwVuu318Fhii0-q-1h3gnYUDJyEBVEEc_WGHfSnqcpSsvly5_PV-K_1ND58eLbvEOAJ92c_hXXZeAcdZYCA44z0_Ta5LmE9OY7sqdwaDvgtO4x1rCzSQJjtxMOP44dz_JZeAkMzTmz11oP0tMR89bsBUN42xGUhoPdn6qoBkNJmr0KIitFjeEewrVz-a_79XiI_oo0uw2P6pqMNzPfvr2yFSbhyypnz2ntj8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9563db8921.mp4?token=l-hbTnv2RgJMvn6yIlp5xK7Pp5kJBfLeJztKDm3F2dF_RiPcJf08jrcBhvkHC5J1-FZn-NZsKoppxmUqNb0-sOBzuBUpIp0-z1EDlJ3oUDpR7jmfyyYLrMeZtGbNyYYTjugaDV7dPmaEvdL2skaAqp1JiiNmVf1SiMfmOXEINRDxeLuzunwXOHyIR_AfahN--9zFZNTsaEfSy5KK_t8BA8AorCWFrE7jsFAzb6IP09ppVUYmlphogiWOK1g3mJ0RBloLrrhALAmeJ2Q2TgvQnZrMxOz_UrW4uUG2wU8o9E2BHKI4InmzkrLKKETGEotI1ZBbxSoXoiVKYncK5SCDOQDqklcWtZZGulIw3r8LYdxOx7V-VSOrYjL5f1wqcqzROuuePEI0iSz_ROFGrxGs9f_HWo8rcwJnNycfKTMzXdKrNonqivgtFMWkmgUGMHPaXYPmnfJzwVuu318Fhii0-q-1h3gnYUDJyEBVEEc_WGHfSnqcpSsvly5_PV-K_1ND58eLbvEOAJ92c_hXXZeAcdZYCA44z0_Ta5LmE9OY7sqdwaDvgtO4x1rCzSQJjtxMOP44dz_JZeAkMzTmz11oP0tMR89bsBUN42xGUhoPdn6qoBkNJmr0KIitFjeEewrVz-a_79XiI_oo0uw2P6pqMNzPfvr2yFSbhyypnz2ntj8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شیعیان کشورهای حوزهٔ خلیج فارس به قائد امت ادای احترام کردند
@Farsna</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/446165" target="_blank">📅 10:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446164">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCJYRvmWjtfFzypkT7FRKzhZPaXh5QM4bJaXt9To2gGvO0iyNwuXnTvHPY2ak-r4HhN4DnhuZby5QaSaLDPrxbN1YC9LjpMDAJ-ZQZQXn-Hwkwoba9hjQzso4uIUiP9vAlaRCSPnAAPJtGbrmfnQDDTkPQXuDrwp5TKWs6BrAXEGZrgNNjIDaCtmgajl7ApTNTy4jYUNmRnSy0ox4nkjfZGg79FGgDq71s3vgicjvIFyP1TyIjJdgvX3i4Ab4P-Uq340kwD4ElAGlusH6kZg4Zjw5DilME8a07Dig6zXTjaaKYqoJ0MQoqzaSm72KVvCnK0AE8POyHPxADU1vQyf3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محدودیت‌های کارت سوخت حذف شد
🔹
شرکت پخش فرآورده‌های نفتی: محدودیت‌های سوخت‌گیری با کارت هوشمند سوخت در ایام تشییع رهبر شهید انقلاب برداشته شد.
🔹
صدور کارت المثنی سوخت نیز یک‌روزه انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/446164" target="_blank">📅 10:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446163">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc1efa7b7.mp4?token=p-cDbPXUa7TPFFKlLwU0cnqzY4NVLB39cEGfgun7hwJIWaJzyRkrgPNz_rbCWJ9jCazzwZkzRZgbQtVXmk9CxZf3zK3hJOLftoqoUVa6ZkIai0FkX_GgeJH9Uf_vzwWm2a9sXIBYZTE5AxL6IzlEf_6yN0oilByd03yUJn6RyXnhmTfi1GEcFa0FUYMvG9J0wYgSv-edqU86bxxaDGJjO0m1HEV2ia6GSV11LGFtiACzau8XFxyaVSlpu_TuZrDbHhx6WdqyLBPmFnhDUxNP_1CMEC_4qh4hRykV-ugFSyeB4cgOmjxtRtsS6unOavwNBFUMVU7Vc97zx3YnoLTDWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc1efa7b7.mp4?token=p-cDbPXUa7TPFFKlLwU0cnqzY4NVLB39cEGfgun7hwJIWaJzyRkrgPNz_rbCWJ9jCazzwZkzRZgbQtVXmk9CxZf3zK3hJOLftoqoUVa6ZkIai0FkX_GgeJH9Uf_vzwWm2a9sXIBYZTE5AxL6IzlEf_6yN0oilByd03yUJn6RyXnhmTfi1GEcFa0FUYMvG9J0wYgSv-edqU86bxxaDGJjO0m1HEV2ia6GSV11LGFtiACzau8XFxyaVSlpu_TuZrDbHhx6WdqyLBPmFnhDUxNP_1CMEC_4qh4hRykV-ugFSyeB4cgOmjxtRtsS6unOavwNBFUMVU7Vc97zx3YnoLTDWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور احمد مسعود و هیئتی از افغانستان برای ادای احترام به قائد شهید امت
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/446163" target="_blank">📅 09:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446162">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ae670d40b.mp4?token=ZYG83jtyXg6LmrOkjohqvE4rHmSpSsTUxILDYLtHz0nA5SXTROB_vDIoWerQPey600537O9rdPGfrFjrTU74cQVfyZeGIZiduIBr8XvVD4ab1Xr637nRUSmpcm-NT73bGmGQ9Gf0472iUvKRiVrmhadu0Fiq5_I71np_3S7MZ07THlX2wl6sPfxu0npZOrTwuO47QKsC-qZ3pBEsoJgmQYK2hmIef_Rro9SQnfbQUsmwlqg5Of_w59ka72DjL7F1GFNBokVg-UUxJMGSL7A9CTbba7pm2bgbQ3hgEvnPJyNKuQhFFSaA-fUFTz02vQ4pwrB3PbzbCoS2D1gIlAIemw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ae670d40b.mp4?token=ZYG83jtyXg6LmrOkjohqvE4rHmSpSsTUxILDYLtHz0nA5SXTROB_vDIoWerQPey600537O9rdPGfrFjrTU74cQVfyZeGIZiduIBr8XvVD4ab1Xr637nRUSmpcm-NT73bGmGQ9Gf0472iUvKRiVrmhadu0Fiq5_I71np_3S7MZ07THlX2wl6sPfxu0npZOrTwuO47QKsC-qZ3pBEsoJgmQYK2hmIef_Rro9SQnfbQUsmwlqg5Of_w59ka72DjL7F1GFNBokVg-UUxJMGSL7A9CTbba7pm2bgbQ3hgEvnPJyNKuQhFFSaA-fUFTz02vQ4pwrB3PbzbCoS2D1gIlAIemw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود رئیس مجلس ازبکستان به تهران برای ادای احترام به رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/446162" target="_blank">📅 09:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446161">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3CA1cmgyUhlFNxcbjAZBCoSmH_UTXck2AxgQ3CeCugJurijH-gR58PEvZ0tMlTmt_KkziUj-aVN8fCVLmyloWquok1KNo2WwYcXYaAb0wUuR4xO9gsU0Izr-U-rgwB1hOB8p0ON2UEqO3FEi-s_Y-8Y93KzHNfXKD-yd9Zke7o7pogQy3660-yKCYai-EM8dnYWkT1yusjJ7G3DUXkOv25bTmCLJDWp6dS0F4Exj_s2m-BUToSEarxMAtyRoW8eNr2RKEES9jZ7D7cJXvtmF3dUyYeBdRxqLVjZeJJL_6-I4h5SttQdKDo030SKGygGojf8wIcYoRLj_omb8zEblw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رئیس جمهور عراق عازم تهران شد
🔹
شبکه خبری العهد گزارش داد «نزار امیدی» رئیس جمهور عراق برای شرکت در مراسم تشییع رهبر شهید، عازم تهران شده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/446161" target="_blank">📅 09:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446160">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a23fccfdd1.mp4?token=NP-mq0uCj8ABqZ6YeN7tke26D5DQiIp8rjN_4EZiqQS2IequqvPDWCXTOFTphLSZHbFnW-C4paFQYAeJWUESPdJq64HpV0TU6bG-leY6Rn-AWIho40he7UbizE2zHNeG0J5yJ61dwkp6oESVknaQ2xVrqEEhsTqrNOPnH5gltYyigM_U8peQpPppxiRv82IAAC7uFuCwi20kTs3JFTT8jqlD_XYp59ALMW1OlMXstNLwsjmmopG353njGqYEC01SZZ-xQOzD7BqbqmhJV-uZNVZbkSe_3sAfCd4MzorE9ntL0n6gLbCZnqq2X-Lp6z22mKuCXv26IOZZ_oRYbva5ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a23fccfdd1.mp4?token=NP-mq0uCj8ABqZ6YeN7tke26D5DQiIp8rjN_4EZiqQS2IequqvPDWCXTOFTphLSZHbFnW-C4paFQYAeJWUESPdJq64HpV0TU6bG-leY6Rn-AWIho40he7UbizE2zHNeG0J5yJ61dwkp6oESVknaQ2xVrqEEhsTqrNOPnH5gltYyigM_U8peQpPppxiRv82IAAC7uFuCwi20kTs3JFTT8jqlD_XYp59ALMW1OlMXstNLwsjmmopG353njGqYEC01SZZ-xQOzD7BqbqmhJV-uZNVZbkSe_3sAfCd4MzorE9ntL0n6gLbCZnqq2X-Lp6z22mKuCXv26IOZZ_oRYbva5ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام جمعی از اعضای جنبش اَمل لبنان به پیکر قائد امت
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/446160" target="_blank">📅 09:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446159">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bbc863f81.mp4?token=UWDuIHf0jCKHUkKY0NUdE8_z7rktosC7sD97e4rcHHHycisCT9OzngLRJPH66fDaKdN-QyLABo0mGVq-0jwONSIe7LdVG0-0AP0_M-uNVcY1fBoBKDLONU9WCcY7-JBNQGRM2Tb-cxniB0lMHTvpE-VPYicwJKb7ugeZc3ykI5WCDi6pa4B0Yo7ocncWCzqDSxJx9DOU13su7S9pJtATqo5m1_YfD-HYmaWE1CvgEqGdafOc38VjwdMA-F1T0j_pZ7TI0jw6ka4PIWedXjErd4cxcQOtVQ5zWMbg-dfa8AIK1Z9I2qwSTf9HXR4L3erHZFTSE25M-z8GorxeVhGEZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bbc863f81.mp4?token=UWDuIHf0jCKHUkKY0NUdE8_z7rktosC7sD97e4rcHHHycisCT9OzngLRJPH66fDaKdN-QyLABo0mGVq-0jwONSIe7LdVG0-0AP0_M-uNVcY1fBoBKDLONU9WCcY7-JBNQGRM2Tb-cxniB0lMHTvpE-VPYicwJKb7ugeZc3ykI5WCDi6pa4B0Yo7ocncWCzqDSxJx9DOU13su7S9pJtATqo5m1_YfD-HYmaWE1CvgEqGdafOc38VjwdMA-F1T0j_pZ7TI0jw6ka4PIWedXjErd4cxcQOtVQ5zWMbg-dfa8AIK1Z9I2qwSTf9HXR4L3erHZFTSE25M-z8GorxeVhGEZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور استانداران نجف و کربلا و شخصیت‌های مجاهد عراق در مراسم وداع با رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/446159" target="_blank">📅 09:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446158">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb955c9ba1.mp4?token=nKy0LpSMy3Wok20HoEXeyFp_4nHujuZyBejHEF0zcEV0EE2O0YhBf0BMbfagGE85tUU-tKYvk0dXUhJHPIr2Yp315Iou8AVrB_WqA7xkc6DZtjF1D9F5DTPFoG3sZE2hroT-5mYPdZYuAdXO0d7_8elxWLYa1IgcaPEvSK4TJ-QVbyBZXtoxviCyUQxoXs8RqBaNFPUT9Vr6KbPUHoHKQOIDAHY2CWwzIsS5NizY9gNFc-YErOB21LBvfSvSMgLBm0-z0qf8KGd4oUaSDE0dsXihhoPgChpSOeDQvOfbXjKzoojG3RQLaE-dCJ8RvH_3tE2cvfZ8jb8MG_vzsXBS4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb955c9ba1.mp4?token=nKy0LpSMy3Wok20HoEXeyFp_4nHujuZyBejHEF0zcEV0EE2O0YhBf0BMbfagGE85tUU-tKYvk0dXUhJHPIr2Yp315Iou8AVrB_WqA7xkc6DZtjF1D9F5DTPFoG3sZE2hroT-5mYPdZYuAdXO0d7_8elxWLYa1IgcaPEvSK4TJ-QVbyBZXtoxviCyUQxoXs8RqBaNFPUT9Vr6KbPUHoHKQOIDAHY2CWwzIsS5NizY9gNFc-YErOB21LBvfSvSMgLBm0-z0qf8KGd4oUaSDE0dsXihhoPgChpSOeDQvOfbXjKzoojG3RQLaE-dCJ8RvH_3tE2cvfZ8jb8MG_vzsXBS4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام جمعی از شخصیت‌های حشدالشعبی عراق به پیکر مطهر رهبر شهید  @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/446158" target="_blank">📅 09:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446157">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f418014f0.mp4?token=A10pbiKD-RWh4XxXdsPZ5CXbfRTnRZSj0-qPzRZ7eO4J9MvmexUkuJjo_A5KBcpHQbyxCBBBPgvzV6c3NW-zacLNZu2iYj3l1I0i9RnuYGtiUIEd-WQx6tfzQL00RGl6EQYy0gDGBenu6lpPcqPElhH6j-6xTnE-Ghhy8g6R-GEdeKsQa5WIPHF0fXgZqKo9ag-oCMuirg8WnfPeVZqqd-50m2I-nfFSm1o-cofCZvTZRZPPizDJFPAd4ybry3iuY-SeEFMB13g7YtQB8YD_RB1EKNUpZ9_qFfQHJAtbZjmsFQCD5f26a83WUoCrZoU6TDO5ffUN-fn6y8n6p5PTbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f418014f0.mp4?token=A10pbiKD-RWh4XxXdsPZ5CXbfRTnRZSj0-qPzRZ7eO4J9MvmexUkuJjo_A5KBcpHQbyxCBBBPgvzV6c3NW-zacLNZu2iYj3l1I0i9RnuYGtiUIEd-WQx6tfzQL00RGl6EQYy0gDGBenu6lpPcqPElhH6j-6xTnE-Ghhy8g6R-GEdeKsQa5WIPHF0fXgZqKo9ag-oCMuirg8WnfPeVZqqd-50m2I-nfFSm1o-cofCZvTZRZPPizDJFPAd4ybry3iuY-SeEFMB13g7YtQB8YD_RB1EKNUpZ9_qFfQHJAtbZjmsFQCD5f26a83WUoCrZoU6TDO5ffUN-fn6y8n6p5PTbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام جمعی از شخصیت‌های حشدالشعبی عراق به پیکر مطهر رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/446157" target="_blank">📅 09:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446156">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ba0a3539.mp4?token=Q95d3qOKbGZQLMYAGqzlZW5OqBVKjKhO9ub5hCalkYFDq8GyWWneZh61AqVZ6PfqJuWrFOWDdpY1ow6f_UjN9r5qldsyH5SV3eofuhpTjZml_KAHK3zV4fmxtP7x0-TI3LvtJy5mpKNT0zpDNq4J8kh9seI1o6QCSEQZ8MC6KLreBHmwXwlfn38lWgRnZZgFHNJEtM3G2wKAHwk-WrbGYzwQgXApPQUu_8nLic2VBrwywM7Rga6j75y488uDyQU2bhxsR_TvLFvxvrIUhTXLGEkMuTpxpGxnb0-MpH35K4DjUBYz1IomYYAVZCf5iqAvJO_WLYZqcRybKWyylvdNTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ba0a3539.mp4?token=Q95d3qOKbGZQLMYAGqzlZW5OqBVKjKhO9ub5hCalkYFDq8GyWWneZh61AqVZ6PfqJuWrFOWDdpY1ow6f_UjN9r5qldsyH5SV3eofuhpTjZml_KAHK3zV4fmxtP7x0-TI3LvtJy5mpKNT0zpDNq4J8kh9seI1o6QCSEQZ8MC6KLreBHmwXwlfn38lWgRnZZgFHNJEtM3G2wKAHwk-WrbGYzwQgXApPQUu_8nLic2VBrwywM7Rga6j75y488uDyQU2bhxsR_TvLFvxvrIUhTXLGEkMuTpxpGxnb0-MpH35K4DjUBYz1IomYYAVZCf5iqAvJO_WLYZqcRybKWyylvdNTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع جمعی از شخصیت‌های جبههٔ مقاومت عراق با قائد امت
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/446156" target="_blank">📅 09:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446155">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1fc62f1ca.mp4?token=NdV0C8kXdugNuxUdTr1iZY0NuDEnq7Tg7AzFpR0ABY3a9BBXuh5ZmJECRBAFBkcpGfPfRqJRLVilWC9Cs766pOBbmAzusukzepvebVVIvweZvvSuL-JeY2YqAPkrRTavm9N-sKp2PoDe1Eo8nv3sP88cxdtLXptca6FfIQxnzs8AKJdimBdij9VIakvTNYbrYrAEG-FevREt5feYh2EdnGKDCK49TG6iESkm0To4I-xrpnXk_eXHtrKsI7e94BWnj4YUgwa7snHBqkIfeIFh7J_YsT2HHdtCJGXC4HOqNBXrq61PeafcP0uuEtHBfITzOBZ606E-U68VPn5OnEE2xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1fc62f1ca.mp4?token=NdV0C8kXdugNuxUdTr1iZY0NuDEnq7Tg7AzFpR0ABY3a9BBXuh5ZmJECRBAFBkcpGfPfRqJRLVilWC9Cs766pOBbmAzusukzepvebVVIvweZvvSuL-JeY2YqAPkrRTavm9N-sKp2PoDe1Eo8nv3sP88cxdtLXptca6FfIQxnzs8AKJdimBdij9VIakvTNYbrYrAEG-FevREt5feYh2EdnGKDCK49TG6iESkm0To4I-xrpnXk_eXHtrKsI7e94BWnj4YUgwa7snHBqkIfeIFh7J_YsT2HHdtCJGXC4HOqNBXrq61PeafcP0uuEtHBfITzOBZ606E-U68VPn5OnEE2xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سال‌ها آرزوی شهادت؛ سرانجام اجابت شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/446155" target="_blank">📅 09:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446154">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54672fa8d3.mp4?token=CNgkCG63wz1igVkl0SWQP5lr1noVkvyOPuOfmEn7btrNcUOsLss4GI4JwyNQb_Wlc0VuMJi7Y1ljAMh_yXwsbhUhtCRrOT58eHN3YZAVFb8HV1eiK62IGjk6Ce0BLY4Tp2PkGcw5r9qXuvh-mgjeqT1pnXChJPor_BiqL9b2cB9QS-ai0WxSYy1ZAXHZXCzKDE5PZ3ZM-kdlEWXhO1P2nLmB5VbAKxYi6KJLNLkAA4PVvA4k55rIX01oq8mfgnB3Ac5RFQ1nq4IQXqhvZSe07IQwzKSvo8aM8T9WG3VHN553roal_S4N1NkOPoCujr7BhvXEdEZLLe2NIocXKcMrqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54672fa8d3.mp4?token=CNgkCG63wz1igVkl0SWQP5lr1noVkvyOPuOfmEn7btrNcUOsLss4GI4JwyNQb_Wlc0VuMJi7Y1ljAMh_yXwsbhUhtCRrOT58eHN3YZAVFb8HV1eiK62IGjk6Ce0BLY4Tp2PkGcw5r9qXuvh-mgjeqT1pnXChJPor_BiqL9b2cB9QS-ai0WxSYy1ZAXHZXCzKDE5PZ3ZM-kdlEWXhO1P2nLmB5VbAKxYi6KJLNLkAA4PVvA4k55rIX01oq8mfgnB3Ac5RFQ1nq4IQXqhvZSe07IQwzKSvo8aM8T9WG3VHN553roal_S4N1NkOPoCujr7BhvXEdEZLLe2NIocXKcMrqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود رئیس اقلیم کردستان عراق به ایران برای شرکت در مراسم تشییع و وداع رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/446154" target="_blank">📅 08:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446153">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61ef459c66.mp4?token=PwXsXCuyx3XsgekkIhIXjCIl8muCQ8pvygMp6pnsymeOK94FnshJb5EzcgmXsf6IXhAEFqtSjLKyv079sO67SzLFIQxH2hZX6tfgEs5-4zEy0hF5W4KWCK___5kPi-OnIWlKx8UFvbJqWTbWGhiaysJ3aEsHT1ZYUrR6fHW__8gIbB7NVijJTbwhC9WclaCQ85dgQew8J973yZw-77YMPuZVOvuuymYOjlIgtfYy7KafKPI52AJl-r2W8tIIhXtS7CvwjjWtIUmUcjW-yBuXBvitVBtDiFHEtv-XuNJEeifnCuI3BV7wYugOSji9jihud5163YA1GQN6EdiyrpMdjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61ef459c66.mp4?token=PwXsXCuyx3XsgekkIhIXjCIl8muCQ8pvygMp6pnsymeOK94FnshJb5EzcgmXsf6IXhAEFqtSjLKyv079sO67SzLFIQxH2hZX6tfgEs5-4zEy0hF5W4KWCK___5kPi-OnIWlKx8UFvbJqWTbWGhiaysJ3aEsHT1ZYUrR6fHW__8gIbB7NVijJTbwhC9WclaCQ85dgQew8J973yZw-77YMPuZVOvuuymYOjlIgtfYy7KafKPI52AJl-r2W8tIIhXtS7CvwjjWtIUmUcjW-yBuXBvitVBtDiFHEtv-XuNJEeifnCuI3BV7wYugOSji9jihud5163YA1GQN6EdiyrpMdjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود نخست‌وزیر ارمنستان به تهران برای شرکت در مراسم وداع با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/446153" target="_blank">📅 08:54 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

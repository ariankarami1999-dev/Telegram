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
<img src="https://cdn4.telesco.pe/file/YN5dSGrgn0AFOgOhTqYhjotqu1Shrj9vDoyrF1FbTrIcMiygQk4FA9R-Gz5_oxmnXD_QJjvuKK9q3NjqcLTKw836_PETiz7awpsvsYv2jRjPBezkZFiuKcKcvycZzJt43y2wvwKSdm4V8tV84-PUpuu5FS9RwtNAMVYAppBd6Nsb6mUWXtXMT2c6ihzS4AAOlOYkB1pWW94gYOFhjz1y4yqpHsX7e6QNdEr6lmRfWkd8vZFZzq297_lxVkkwsy5rVpyarQ7gTTXHATa2KJ-7qebidp5hpYBLYfK6SdR7TlsEkJH9OwFlIDOieE1oLQdOffQ-qrH8a1mI5OlhhEYs3w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.41M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-23 16:14:42</div>
<hr>

<div class="tg-post" id="msg-670996">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIAk2n1vxixcxLDKhujqQajA7tRN58dtAABrXMolcNiULzzT80T-UgN0vXLZNADxZYUUJj75JiTSwKcWVqn15xAIMnuqBM1LXVeJQZIoZnfV4knnHtWQEO_Bg7umplf0Y-EVWxSRJyKOspfTCWzz1i6NU1egSgJpIn9JM7v9ib7NKKVhA7rqw7T3AGd3RkfhMsV88F8kd8VfRriRQfC3U2MO7vIZ4t9lTT1pf8JjWLjmxtnDflPsy86I6zs-_K5tSE6PZre7d7ZnbJVuDewa8CeQBikOXlQ_FnOU0RCWBab02PQpxbOzWYNfFtOOluNI1x5xX1gFCX0-q5Ox2wmxTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کوه کلنگ که ترامپ تهدید به حمله به آن کرد، کجاست؟ / تاسیسات مرموز ایران در قلب زاگرس
🔹
رئیس جمهور آمریکا در صحبت های اخیر خود به حمله به کوه کلنگ اشاره کرده است. اما این کوه کجاست و اهمیت آن در چیست؟
دراین‌باره بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3230219</div>
<div class="tg-footer">👁️ 14 · <a href="https://telegram.me/akhbarefori/670996" target="_blank">📅 16:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670991">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SiM_sIKuXubF0UGOIuzDqdHsDxvfrI51UxyNT7JeZKNi1RftUf7Lg9V0QmbUgM9Pj1dqNEuMcTch6dg3UYiR4XfeOvHsnLjW55Z_G5bzFJKHPh5dV3vbMBVwMbeulnjsbtvPn1A26OeMvysk4-cQdWt25s6fsBwOvgHycSlSqFieutiUffgmSIZ_l9ciR8AfBN24ePumUA-NSmli37il8mZialnn_DUFAtXn2GovhAvnXVEBMLBFFMmfVA17QTrt8HpBejrMHruwp_kvytu8Ke7s8AmJYWWeC6iA-4aSm_rBUu0iShPjGFcEcVXwKQrl0ixG5vYdkEj0nUJrVPFlbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qRCJPi1WtAt_G4VauOROIZM7X8xdR2hAzRnhTxA-ZSziNyLPsQwoAmmlwAlzdyUawpKClsdygVFJWBP7-sLV4aJ-GH4VKV82HEy4LoIP7qvEwEewO4oRAB2qwfdwvJcjY_a3qAdd1GylIWhLeZUSoXfukTvqMTZCx0UNG6P22XBjn5J1TS5xccnY-m7uG6iyZhDzRX_U4YdOy6RkwJD1_wo26HWEy0WrgYy51SXHObB4hMk19G2qg2N1EfsS8MZgWZ-Y0eo5VJBKV-TgIN029x6AaweWAjEwkwA9UYoRrbxjeg5vwq_C_KMj98MwQ7Xph_yg50NvJv9bo3pvyoSUWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ks3Qv8IjX7BOikmBY2mJ4cD2dWBYevzW1zqRThTAPgfQWSHhI4ETOmAXS_pwxU-Bf7jJIj_BGQRgYyEC2hiA-3QB6x9skLHeBVsENGD67GrtYfQfwAenUu9tmZCEYuxedDqnpki7Ffl0jOqt7EfAAn9JYNJeva9n4Bi2ON7blPREkaHREIGHJeVHCruMBfLbaBcbce0uVoG_Xxo3dBXSH5z8saoQyquEWXBZXHPnXI1wJKY8-7Xa9590TAhXwxg5dnnapBVZq1hStPEhseNIoD_tiNqxwk51abTGqR7h8U4R1poYKfkqDIvf5n3p71naKx2ij10g8ghH9Fl0iLPfvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kwApLXuYZDSgWTQq1Q51w3yV5quvhdiB0pUAiS8OfNK1aKMgk7fZiejzsyiWFOICwwHC8ep1oQU9abOknszoN45d3qTnm85o600hUYM0aU73EJzF3lARmM9nOgEIAYMMpQtpVNEsxSGmmS21TeJ6qe-jgKqplWarl7mmd-qOEYSi-5-lXwrc4RigKLnsP7nISXXKdAlQgZSHzBLqicnGsNP68MiyP1ulBBF8N0qOhUlcviYlS-qy2dP2Bli3PJ9b4I-5QdPXMWqqqQo7yGV7YNLUn4u7-N11nhRJ3VxIfrmADiiw9z62QRnlB6ArUht5b1t9psFOsrN9aXMcGIOX-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RHmHMXXyQ5AYr6v060CeoF24-gpNh-3vVVNnSV6XyOA59d9609DfOdx5tFZxdGsCgOdH0zOJd_kYzbyqFb8Me8_QkaAAuEkAMIJd3txpoN1M8BWys6bPSCJjFGNCrL96yUMlOiNYqzyKr9ZGZQr0-CVbCIdDR4pv-lduyF1javcVvuAVW15vPWmzp04DDIp47Fd0hRXTiBrVSixw4PvrCVgBPQLUU9u0ttG-WFOQCO5QkJIxtA8h-jWqprTT7vX21UcJmkujPuE25D65m38p-ZU4cMOt9mh_0xsxbKfCNCwgkV5pKZOTnxgz0_Wl5YANf5QkbwWjbtDY1RG0xlhrrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چند اصل کلیدی پس‌انداز رو یاد بگیر تا پولت رو‌ هوشمندانه  ذخیره کنی
#دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://telegram.me/akhbarefori/670991" target="_blank">📅 16:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670990">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
نقض آتش بس در جنوب لبنان
🔹
منابع لبنانی از حمله پهپادی رژیم صهیونیستی به شهرک النبطیه الفوقا در جنوب لبنان خبر دادن.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://telegram.me/akhbarefori/670990" target="_blank">📅 16:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670989">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7da3b4274.mp4?token=FI1bJlUWsw08j8UeOyx5YuhFozVJ9HaztwRZPH0XXzF5h5gxh9byQuvTrSsWgM1wEL2wRP0Dn-4NhqySXqDnRq1fbUMjVs2NfwKdFR4aGQw7tYGY-iwWEHkTYK2lThxhQt1Sq_ObS_IZR2HtCTbJuWme0qFQ2h_vF61yFgHgzy6k2cK0terLkCLX_J6s0pOqZwyeObmRvy5iUp_nEmYst3EK9XgFfw4zx88P4h1vye-uhKriByTT1sbf9KoskYPC8t97bl4c6kSk8vcaKiYfxd5YeA47Zzwu5BjxRPrY-LpOa_Pp5r9x4gNnwdefl5kSrtyXUSM6wNujG8b2MKUBxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7da3b4274.mp4?token=FI1bJlUWsw08j8UeOyx5YuhFozVJ9HaztwRZPH0XXzF5h5gxh9byQuvTrSsWgM1wEL2wRP0Dn-4NhqySXqDnRq1fbUMjVs2NfwKdFR4aGQw7tYGY-iwWEHkTYK2lThxhQt1Sq_ObS_IZR2HtCTbJuWme0qFQ2h_vF61yFgHgzy6k2cK0terLkCLX_J6s0pOqZwyeObmRvy5iUp_nEmYst3EK9XgFfw4zx88P4h1vye-uhKriByTT1sbf9KoskYPC8t97bl4c6kSk8vcaKiYfxd5YeA47Zzwu5BjxRPrY-LpOa_Pp5r9x4gNnwdefl5kSrtyXUSM6wNujG8b2MKUBxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی در فرودگاه بین‌المللی بصره
🔹
منابع خبری از وقوع آتش‌سوزی در محوطه فرودگاه بین‌المللی بصره در جنوب عراق خبر دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://telegram.me/akhbarefori/670989" target="_blank">📅 16:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670988">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک ملی ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_kkVK15tWZuSin8vWYd2VLUz6ZpSXNHD1m2lwvQ0h1dBWuihOSwUZwhMEvzB4Iu8-f7R_a-6KmfS4bf803S88eif9IFUgbeBG3-eK6T8Pk5uW17QtGrv2GjrCvYAMNFkHodBinhXtjqVhtGHvFcGolYdO-MleosuPdUw2C_nrJDLCRqejuz0u5v5918tQBsFENyz8HVmpDUkhuA7g8B10eR_iQ1pnXV-SLlKAre2aVfKyNHYgANIMG8L8T-6Xr0nsSdGBnFPquL9D8reSennG7eLRZtjPSHUSMbW0vfqpAxdjxpR_IoVP6WQzTxaoS32CBU_-pCHuOd_YUPljbSxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
آخرین وضعیت ارائه خدمات بانک ملی ایران؛ از واریز سود سپرده‌ها تا وصول چک
🔹
با ادامه روند بازگشت خدمات بانک ملی ایران، بخش عمده‌ای از خدمات بانکی از جمله واریز سود سپرده، خدمات چک، پرداخت اقساط تسهیلات، انتقال وجه، خدمات کارت و مدیریت پرداخت‌ها به پایداری رسیده است. متخصصان بانک نیز همزمان در حال تثبیت پایداری سامانه‌ها و تکمیل بازگشت سایر خدمات هستند.
🔗
مشروح خبر...
@bankmelli_ir
| بانک‌ ملی ‌ایران
🌟</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://telegram.me/akhbarefori/670988" target="_blank">📅 16:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670987">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
چهار نقطه شهر بوشهر مورد اصابت پرتابه دشمن قرار گرفت  استانداری بوشهر:
🔹
در ادامه نقض آتش بس و تفاهم از سوی دشمن امریکایی ظهر امروز چهار نقطه شهر بوشهر مورد اصابت پرتابه های دشمن قرار گرفت./ ایرنا  #اخبار_بوشهر در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://telegram.me/akhbarefori/670987" target="_blank">📅 16:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670986">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jT9IvYVht11xRYq0guZFgI-xeEXVXiC-4QF_RqkOnQx4Rc_YzusnJ8MiXSaVar_4YV5VJ_37ea4YfwfY68sHOHwOkXO8icHwFpJqC_XkmpcTtchMDxoNLNtTEiK1hWwW4Ben2H3EjFsKZRyl39TFZLeZd1sszc5WAmcFViOG30GGqzGaKRCyu4KUik7FTEq68yy-F_sWADCwGFyS1pPfBP6jHsIu4ZuUlp2ow-6pc-M9tWO-7BnpBAvb3E06TPDXxlPJCN_hxV3h1AuZBAkWhRHgYdXHwaiNkw6tfiR_sV1vqC-kIHzS8oMcsSUZMn5cRyZldEoYYJD-ZOrUH5utKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نهاد مدیریت آبراه خلیج فارس: تا قبل از تنش‌آفرینی آمریکا در تنگهٔ هرمز، ۲۰۰ شناور غیرایرانی به‌طور هماهنگ‌شده از این تنگه عبور کردند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://telegram.me/akhbarefori/670986" target="_blank">📅 16:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670985">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
تاجگردون رئیس کمیسیون برنامه و بودجه باقی ماند.
🔹
آژانس ایمنی اروپا خواستار پرهیز از حریم هوایی حوزه خلیج فارس به دلیل تنش‌های ایران و آمریکا شد.
🔹
شهریاری مجددا رئیس کمیسیون بهداشت و درمان شد.
🔹
رضائی کوچی رئیس کمیسیون عمران باقی ماند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://telegram.me/akhbarefori/670985" target="_blank">📅 16:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670984">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
داریوش فرضیایی به سوگ مادر نشست
🔹
«داریوش فرضیایی» مجری و برنامه‌ساز شناخته‌شده تلویزیون که سال‌ها با نام «عمو پورنگ» در میان مخاطبان شناخته می‌شود، در غم از دست دادن مادر خود عزادار شد./تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://telegram.me/akhbarefori/670984" target="_blank">📅 15:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670983">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJSoSgTcWXnExsh8iDi6PkSoqqh1o44AYyZuN0FKkB94H6iFSFitTcfXkY_axrXnZVupWWRuXKekeGCm7OV6yrJw8CLWaD7zQKiPGlMEboMUnPx3iyGk242Shk9LwCGr4RxDDMGjEuarLRs52IdEe601bp-Md3VVnl_9qGkX-iz7YrOwk43F0D1mG-IX0Bp63PUid0eMNeZOGvBnmTXe6HG38HZPL6uFXRkgePPX5A6chLWrBXQ8Mm0dyXqM5HA4RXestSucWNize2qXhGqM9uqeJvyAEYX8JCHBJxnhB1R5lER7vxLfmuNc1k7_BqOrUvxnrqwRSUYzlqYD35385A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کمپین بزرگ اسنپ‌مارکت با جایزه ۵ میلیاردی
🔹
اسنپ‌مارکت کمپین تابستانی خود را با جایزه نقدی ۵ میلیارد تومان برای یک نفر آغاز کرده و به ازای هر خرید، یک شانس در قرعه‌کشی نهایی به کاربران می‌دهد.
🔹
این کمپین با هدف قدردانی از همراهی کاربران طراحی شده تا خریدهای روزمره را به تجربه‌ای هیجان‌انگیزتر تبدیل کند؛ یعنی هرچه خرید بیشتر، شانس برنده شدن هم بیشتر.
🔹
به گفته اسنپ‌مارکت، فرآیند انتخاب برنده نهایی با رعایت ضوابط و در چارچوبی شفاف، طی مراسمی با پوشش سراسری برگزار و نتیجه آن به‌صورت رسمی اعلام خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://telegram.me/akhbarefori/670983" target="_blank">📅 15:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670981">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74cac75825.mp4?token=BuV4wUC7fm_iTKIedlLvB-nnizJGdiQFxgUs0RrogeCKOYtLX9oxbAmdVYRnOuVz6OZfkqW0uIF7I5JN0_ssS7dqIlPB3pBaNDQpAvUd0m9tQCJ2llrgs5cyrwVqeMDNt5qvhA8wPUnFIghmj-OVmSmx56FvjFjUNsBJdo4PH552siimnY0X1V-S6x8ZagXTpUXsG4wmgh_E2VmUsVUmzq1L-rHc-1N2wecbHSv_332jFtCCSPMP84EA67BF_TgvmWF4irzNOdxIl4VWfH366H6N2lR4zG4d5pvHB8dQo7LM_140gQTo7MzfkDSe974rqzzQnUyPrs2k9PgxKJ_O_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74cac75825.mp4?token=BuV4wUC7fm_iTKIedlLvB-nnizJGdiQFxgUs0RrogeCKOYtLX9oxbAmdVYRnOuVz6OZfkqW0uIF7I5JN0_ssS7dqIlPB3pBaNDQpAvUd0m9tQCJ2llrgs5cyrwVqeMDNt5qvhA8wPUnFIghmj-OVmSmx56FvjFjUNsBJdo4PH552siimnY0X1V-S6x8ZagXTpUXsG4wmgh_E2VmUsVUmzq1L-rHc-1N2wecbHSv_332jFtCCSPMP84EA67BF_TgvmWF4irzNOdxIl4VWfH366H6N2lR4zG4d5pvHB8dQo7LM_140gQTo7MzfkDSe974rqzzQnUyPrs2k9PgxKJ_O_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات روسیه به پایتخت اوکراین در شب گذشته
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://telegram.me/akhbarefori/670981" target="_blank">📅 15:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670980">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
آزادی ۵۵ صیاد ایرانی از بازداشتگاه‌های امارات
سفارت ایران در ابوظبی:
🔹
۵۵ صیاد اهل سیستان و بلوچستان و هرمزگان که به دلیل اختلال در سامانه‌های ردیابی توسط گارد ساحلی امارات بازداشت شده بودند، پس از حدود دو ماه آزاد شدند و در حال بازگشت به کشور هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://telegram.me/akhbarefori/670980" target="_blank">📅 15:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670977">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EzzYJMjm-6jKFEK6xThVQvjKvZ2jmzVMVZ9TAzXnBMFyH83CnMa7Oy8kqd16OyqDL7TITxUTOukplI3e0lh4i7TBCpYNamB_nw5vWULdYx-4oQbZXxV_XPQFAfeWC4eWQBqej6-paOfFXPeqwtRcs522pPZKl7Gfh5hJ-OD3ekStIvW1zAbsLYsFf1B3Y1nY_cLg7uaYZC1oW3WityME9snLzFoE9oDF_jf19svwAcRkLcmdd1En7BdLwIkeVKWU7d1hGOGOBaVTNW4iDwynqf-lSh_UpcyUnpMLQGz_cNIcyPpzs0nX-5ljontyFFgSxHcpS9GjGBSmN6QxTgSprw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J7oaha0Sk3G6zvbMvo04LIQ2rJnbeqI1WLzCFvw_SyMXyMqBJP4qUj4lPn_fYTZ7zr9QdPHROnf_syv-GCCwHgXWd_oEG8jmeRxcvnBACkzCHjrdYX63HnW57WPE7jACN5ngZp_lugTwk5CB-YKoIsvp4Bf-30k9ba_fCxva_KWSzslw6WSjMkSXUX2lOWc_pbUMaf_lIkG-gBNAb49F2k9wvYhrNXoFNmierKMTwCID0kcuagdCGmuLTN9zHT8Xy_9sczeoHBDBjwb5l4NpxRt6C3NYCQOAOLbX6dwVAjIRN0m42IISgLQynNNjxSDtgd65-F_n3gcS4een5Rnghw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iytoFO1O7vWk4i3j74K9ExrIQCIz8cydNVyrnNHaV7X_KJsF5ubEz-gTytIRLXsyOjZjt6Kl9XMTbSwuljFWu5AbkVTwmukr78tdY7A2qNoF8kbDkiTvr-8JRfb9dATMDSNNvJEEZg2v-HJsotk_uTtfSnQEn2Gxw-4PjDUdL_tdcFsT_E3SBVPIrP2qS80HOu_rj0nwO0jD6RTV4g5hGO8_pNWV3GKe54_qg6i9VcpNM4pyNud0mQIXMGBMzRLvDzIc8kM5X4t49T5J9esvIeRIudK-WCB4AXUcfZLSAp0HjXUnDsPDGCVfN3vuAkvid7bvxNymc_zVLyJhFFWl7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ظهور نقص فنی در نمایشگر گلکسی S26 اولترا
🔹
سامسونگ در پی گزارش‌های کاربران مبنی بر مشاهده هاله قرمز در مرکز نمایشگر گلکسی S26 اولترا، تحقیقات گسترده‌ای را آغاز کرده است.
🔹
کارشناسان احتمال می‌دهند این مشکل ناشی از نقص سخت‌افزاری در فناوری جدید «نمایشگر حریم خصوصی» باشد که با تنظیمات نرم‌افزاری قابل رفع نیست و می‌تواند منجر به تعویض قطعات شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://telegram.me/akhbarefori/670977" target="_blank">📅 15:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670976">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
برگزاری مجدد انتخابات ریاست کمیسیون امنیت ملی مجلس تکذیب شد/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://telegram.me/akhbarefori/670976" target="_blank">📅 15:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670975">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
افسر ارتش صدام: روزی نبود که خبر ترور کسی را در خانه‎اش نشنویم؛ ایران بعد از جنگ هیچ‌کدام از فرماندهان و خلبانان بعثی زمان جنگ را رها نکرد و همه را حذف کرد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://telegram.me/akhbarefori/670975" target="_blank">📅 15:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670974">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/244879ec69.mp4?token=CB5FCPybQwY6Gm3axw9e2GDnd0N6Tja-pBU7Bt7b3Pmha_yvIbx3aA2cNVAO2nFiCXdUn_oA0Tdi0N6TXRrGo1xlu3TBmivj4K4dhWqsVpnD0f1T4HgjRzwMOGeUX5XiSutr0LRqEOMvnp6xYaiso0xVWyJT4U42GxRgHOA1eMCXXL5P-MD0TBYQ2ByqCK4gL3v8_MEF91HshCFIkGbWJ-u5Wq1qHtndJm1Rzna4GEnxbtPlo-qjpC1jcXo2BNwemyRjKbTYwA_KyXlmoXx1ptXQfFzchuDebn1hz2lBGBRlje5vCxatsJNgDBFtN2uJyCn4NbmlDc0q2btW6wPTURV6WYpZENDnm6Arz4DMaJ4ShgpGFeGITNm9eQdRF_SgNPNGGF7yEgt2n6LFyIlGZBt-VObySzo-eKlHkltU6pwMgrvMuhQg1T-5xO0RA1hHRvNFI8zbVt8ofa3QrXsxFqosiEuxveIxYwYx6y2E1Z7CObXIhMuAIhbcAbJrDKfxmBPzNrEOZNZnJ_5QztkfxsCEXxwXb0MsN26D0QZWqmKtfozskgvdmCarf2EnHpBsAngKDjZh4sSXwwqeAS3op7IaFERVYEvfgjHk_9U2oJRKBx3gAI18hkj8xjORQ5_ean6G2G1q0FjbZF4VYd8ijnCKVmfT3Y7TZoGbyLvRth0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/244879ec69.mp4?token=CB5FCPybQwY6Gm3axw9e2GDnd0N6Tja-pBU7Bt7b3Pmha_yvIbx3aA2cNVAO2nFiCXdUn_oA0Tdi0N6TXRrGo1xlu3TBmivj4K4dhWqsVpnD0f1T4HgjRzwMOGeUX5XiSutr0LRqEOMvnp6xYaiso0xVWyJT4U42GxRgHOA1eMCXXL5P-MD0TBYQ2ByqCK4gL3v8_MEF91HshCFIkGbWJ-u5Wq1qHtndJm1Rzna4GEnxbtPlo-qjpC1jcXo2BNwemyRjKbTYwA_KyXlmoXx1ptXQfFzchuDebn1hz2lBGBRlje5vCxatsJNgDBFtN2uJyCn4NbmlDc0q2btW6wPTURV6WYpZENDnm6Arz4DMaJ4ShgpGFeGITNm9eQdRF_SgNPNGGF7yEgt2n6LFyIlGZBt-VObySzo-eKlHkltU6pwMgrvMuhQg1T-5xO0RA1hHRvNFI8zbVt8ofa3QrXsxFqosiEuxveIxYwYx6y2E1Z7CObXIhMuAIhbcAbJrDKfxmBPzNrEOZNZnJ_5QztkfxsCEXxwXb0MsN26D0QZWqmKtfozskgvdmCarf2EnHpBsAngKDjZh4sSXwwqeAS3op7IaFERVYEvfgjHk_9U2oJRKBx3gAI18hkj8xjORQ5_ean6G2G1q0FjbZF4VYd8ijnCKVmfT3Y7TZoGbyLvRth0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر خارجهٔ روسیه: حملات آمریکا به ایران نقض یادداشت تفاهم
است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://telegram.me/akhbarefori/670974" target="_blank">📅 15:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670973">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
جنایات رژیم صهیونسیتی در کرانه باختری ادامه دارد
یکی از فلسطینی‌های ساکن الخلیل که خانه‌اش توسط نظامیان صهیونیست ویران شده است:
🔹
من خانه‌ام را در ۱۰ سال ساخته بودم اما آنها خانه‌ام را در پنج دقیقه بدون هشدار قبلی تخریب کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://telegram.me/akhbarefori/670973" target="_blank">📅 15:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670972">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZF1WbLeTI1OR2QfhiX9uU-_jaDgOkXJAN4-vijbjjsqJ__pucTujDpXACCx-iLOXfVCCLd9ZVgMEao-0DZ_v-eyszk0o6jE7g9NSVVl3V7Ixj66c5JKAB4eEFL3CUk1h75gIszVbRjpPfvsG_dQkzZebKyNRjntpZxUl0mghizGBOq8KleHsKTR_VP6JeS-2QlEexZbXHOouT4u_cFbb3VjQPBe5rznhpwxmXOJ6m6U4VKfN4oMk0M1Yf5KPwrHAh1W9BAZGXDPgDMuJ-xbKHUk0XDZ0wJPF454nqyt7kRvfzZXL2-ACqIcfWk7IqCR9NFs6EfHa0cVAiN8qP9lcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
احمدی‌نژاد با دوستان و همکارانش دیدار کرد
🔹
این اقدام پس‌از شایعه نیویورک‌تایمز مبنی بر حصر خانگی محمود احمدی‌نژاد صورت گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://telegram.me/akhbarefori/670972" target="_blank">📅 15:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670971">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزارت صمت: قیمت‌گذاری فعلی خودرو مناسب نیست؛ دستورالعمل جدیدی تدوین خواهد شد.
🔹
هند سفیر ایران را احضار کرد.
🔹
پاکستان حملات یمن به عربستان را محکوم کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://telegram.me/akhbarefori/670971" target="_blank">📅 15:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670969">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
روایت سرلشکر صفوی از بینش رهبر شهید انقلاب به مسائل منطقه‌ای و نظامی
سرلشکر پاسدار رحیم صفوی:
🔹
در سال ۷۶، ما ۲هزار موشک داشتیم، حضرت آقا در آن زمان فرمودند ۲هزار موشک کم است و باید به چند ۱۰ هزار موشک برای چندین ماه جنگ برسد.
🔹
۱۵ سال قبل حضرت آقا به بستن تنگه هرمز به عنوان یک ابزار نگاه می‌کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://telegram.me/akhbarefori/670969" target="_blank">📅 14:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670968">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
حکم پرونده‌ای با ۱۴۸۱ شاکی در مهاباد صادر شد
دادگستری آذربایجان‌غربی:
🔹
حکم بدوی پروندهٔ یک شرکت هرمی با ۱۴۸۱ شاکی صادر و ۶ نفر از متهمان این پرونده به حبس‌های طولانی، جزای نقدی، انحلال شرکت و مصادره اموال محکوم شدند.
🔹
بخشی از اموال توقیف‌شده به مال‌باختگان بازگردانده شده و بازپرداخت مابقی نیز طبق قانون ادامه خواهد داشت.
#اخبار_اذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://telegram.me/akhbarefori/670968" target="_blank">📅 14:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670967">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1XUmTm5ak3YVpWAXl6gQHqk7S-bjMBlpGZfqnxQ1ORgw-nBhEHRw9cPpFuwXdJdrRxVv_H96KkAA3RaYmA0CmTzdFG20-oQs99VwnzSURR8LG9Af3XTV4csFEPhM6SYmC-3md0Z52FZ-yCcnSRYkONgZECVorY3XZVhNnmOAiUIoUGssSBCr6Y7Ntqfi5Cg_f3TOo7ewloCbqgf0bou7aAGPbtXcH6I-8vNKodjSjj5OCK1GMZJzVNyUMUv1FrqayvK9LZs4Vgk1Lnve-UPS8kUMZBCq8sMhQVgjXB936evll06zqqYFEZRfD7bzzmfq5zwB1aPzxgBbrhxjVRyyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرار بیمه‌ای؛ چالش بزرگ تأمین اجتماعی
🔸
برآوردها نشان می‌دهد سالانه حدود ۴۳۰ هزار میلیارد تومان فرار بیمه‌ای در کشور رخ می‌دهد.
🔸
بازگشت بخشی از منابع ناشی از فرار بیمه‌ای می‌تواند به تقویت منابع سازمان تأمین اجتماعی و بهبود مستمری بازنشستگان کمک کند.
@amarfact</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://telegram.me/akhbarefori/670967" target="_blank">📅 14:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670966">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
اسامی ۱۴ بازیکن تیم ملی والیبال ایران برای دیدار مقابل اوکراین
🔹
پاسورها: عرشیا به‌نژاد و ایلشن داوودی‌پور
🔹
قطرپاسورها: علی حاجی‌پور و محسن دلاوری
🔹
دریافت‌کننده‌های قدرتی: مرتضی شریفی، پوریا حسین‌خانزاده، مبین نصری و علی حق‌پرست
🔹
مدافعان میانی: محمد ولی‌زاده، سید عیسی ناصری، یوسف کاظمی و نیما باطنی
🔹
لیبروها: محمدرضا حضرت‌پور و حسین حاجی‌کلاته
🔹
تیم ملی والیبال ایران از ساعت ۱۸ روز چهارشنبه ۲۴ تیرماه در نخستین دیدار خود در هفته سوم مرحله مقدماتی لیگ ملت‌های ۲۰۲۶ به مصاف اوکراین می‌رود.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://telegram.me/akhbarefori/670966" target="_blank">📅 14:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670965">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
فایننشال تایمز به نقل از یک فرد‌آگاه: مقام‌های کشورهای حاشیه خلیج فارس مظنون هستند ایران یا گروه‌های هم‌پیمان آن از توافق‌های رومینگ میان اپراتورهای تلفن همراه منطقه برای ردیابی نیروهای آمریکایی سوءاستفاده کرده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://telegram.me/akhbarefori/670965" target="_blank">📅 14:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670964">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
اصابت چند پرتابه دشمن به غرب بندرعباس تأیید شد
🔹
استانداری هرمزگان برخورد این پرتابه‌ها را در حدود ساعت ۱۳ امروز تایید و اعلام کرد که اخبار تکمیلی در این خصوص به زودی اطلاع‌رسانی می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://telegram.me/akhbarefori/670964" target="_blank">📅 14:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670963">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c662d108c6.mp4?token=ZmggD7SCf8hZeos6MNR1etkf72_gc6GMQ631WsfZFPbE6paQNPwVl_oPOj_VEB1Yg9LKgwoAN7JlVAkHe0JLqAFY9Y1Se0EgZsUIYKhvCploCgf_kk9rihOIy2uP9D6x5ieOHCSdE73oizCfaUeZktSQ5l_O2_rVMR881ncTH5_FpAqPxZie4KPMYxdBEcye3gDdopaaOTsETrvP7fs-HjzOh4xsrHibkAZKIsFdyjv3uB-v3dm3x6Lg9TJmjScocnuAjSsNeds308gHyQAhVfXZ3Bg9avPU173i2LEzqeQzSf4FdInZE_0UMBhooOs_z_fWjWOTzsXz0ZK_KZcQ4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c662d108c6.mp4?token=ZmggD7SCf8hZeos6MNR1etkf72_gc6GMQ631WsfZFPbE6paQNPwVl_oPOj_VEB1Yg9LKgwoAN7JlVAkHe0JLqAFY9Y1Se0EgZsUIYKhvCploCgf_kk9rihOIy2uP9D6x5ieOHCSdE73oizCfaUeZktSQ5l_O2_rVMR881ncTH5_FpAqPxZie4KPMYxdBEcye3gDdopaaOTsETrvP7fs-HjzOh4xsrHibkAZKIsFdyjv3uB-v3dm3x6Lg9TJmjScocnuAjSsNeds308gHyQAhVfXZ3Bg9avPU173i2LEzqeQzSf4FdInZE_0UMBhooOs_z_fWjWOTzsXz0ZK_KZcQ4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار ویدئوی قتل مهاجر کلمبیایی به دست مأموران اداره مهاجرت آمریکا
🔹
تصاویر دوربین مداربسته، لحظات منتهی به تیراندازی مرگبار مأموران اداره مهاجرت و گمرک آمریکا (ICE) به یک مرد ۲۶ ساله کلمبیایی را در شهر «بیدفورد» ایالت مین به ثبت کرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://telegram.me/akhbarefori/670963" target="_blank">📅 14:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670962">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0b2b196d.mp4?token=Q3S8-OKgHpQ6kQjjZCY3pn-XsMlWGYP9b1untAJ6QGVUNtWgLWAWSq_CtEdB_Xk6HNPy7zF1JkEYpHZ6WTByMrZa6nqIXP34JrSi6rtCyTHrxm9RlT8E9vK6D5YcnLbQHEKw9xJbmScW5KzfKDjJIr2fttEgm-Gtn84BriBafCxf6xb1f9E1XfQY2J722bQJC-8RRk0PpjXR1pGUcn3G7grdxSbK_x3mkI0oRjGk23ur4B98-N9ONVjAluQ7QCTHRB_Y0gDBjqH69NvZtsH51ag_SPndmZ9NytNVDkk3Q9Xgj9vmNqfxL5Mu-kZhdv_1yU6cfMC9561LtMfDldGvDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0b2b196d.mp4?token=Q3S8-OKgHpQ6kQjjZCY3pn-XsMlWGYP9b1untAJ6QGVUNtWgLWAWSq_CtEdB_Xk6HNPy7zF1JkEYpHZ6WTByMrZa6nqIXP34JrSi6rtCyTHrxm9RlT8E9vK6D5YcnLbQHEKw9xJbmScW5KzfKDjJIr2fttEgm-Gtn84BriBafCxf6xb1f9E1XfQY2J722bQJC-8RRk0PpjXR1pGUcn3G7grdxSbK_x3mkI0oRjGk23ur4B98-N9ONVjAluQ7QCTHRB_Y0gDBjqH69NvZtsH51ag_SPndmZ9NytNVDkk3Q9Xgj9vmNqfxL5Mu-kZhdv_1yU6cfMC9561LtMfDldGvDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با بسته‌ماندن تنگۀ هرمز کشتی‌ها همچنان در خلیج همیشه فارس لنگر انداخته‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://telegram.me/akhbarefori/670962" target="_blank">📅 14:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670961">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8e2326267.mp4?token=vfJhOjHOaLqYIsmPXlE9XFXD3Kkzjw2kstVm37AyUdpsvczitwxeS2-7_K6Le8EeWkdAbKDVMUW05yvl0Lhw_4H_F6lMLSGXhUkNNMzh3nUpNHPUedllukrW-j49--KdwyrJZtUMNEEJaptAmqJFVanbp9I5jr_kF6t5mg_nL-zZjBfLW2shF4oKxp4mFYSx5awdd7psshrkTO-bao3EIZhGZE7J1ge8jkzvUdPEi3mDw0IeTtj5qJYZd8kTntnhcnKOQ2zk00xfXpr9jQU7oyMbbOXeqB-qubGIKg8u8iKHRhHC6Ii696CTfx7xGowv5Kz9q67Y1pCMIJtvty9xzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8e2326267.mp4?token=vfJhOjHOaLqYIsmPXlE9XFXD3Kkzjw2kstVm37AyUdpsvczitwxeS2-7_K6Le8EeWkdAbKDVMUW05yvl0Lhw_4H_F6lMLSGXhUkNNMzh3nUpNHPUedllukrW-j49--KdwyrJZtUMNEEJaptAmqJFVanbp9I5jr_kF6t5mg_nL-zZjBfLW2shF4oKxp4mFYSx5awdd7psshrkTO-bao3EIZhGZE7J1ge8jkzvUdPEi3mDw0IeTtj5qJYZd8kTntnhcnKOQ2zk00xfXpr9jQU7oyMbbOXeqB-qubGIKg8u8iKHRhHC6Ii696CTfx7xGowv5Kz9q67Y1pCMIJtvty9xzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین تصویر از آمبولانسی که در حمله به لار مورد اصابت قرار گرفت
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://telegram.me/akhbarefori/670961" target="_blank">📅 14:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670960">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
هشدار درباره کاهش ذخایر تسلیحاتی آمریکا در صورت تداوم درگیری با ایران
سی‌ان‌ان به نقل از کارشناسان نظامی:
🔹
ذخایر مهم تسلیحاتی ایالات متحده به‌طور قابل‌توجهی کاهش یافته است.
🔹
در صورت تداوم حملات به ایران با شدت کنونی، این ذخایر با فشار مضاعفی مواجه شده و روند تخلیه آن‌ها تسریع خواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://telegram.me/akhbarefori/670960" target="_blank">📅 14:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670959">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_9GFSslilqQnLBTu1sUrBzVa17VvTlGlypYEhttqR-_i_JH9pc2y1fiI8lCQdnL7rH1qr43cG5LrDD0O0oNKJDIQq34Ebnw2RItFH3gsksBDJvXLZyqnmTRVR0XOXDBX1-inqQvKhX6jjciLfEeu3r7jW_G5pRS8_xOLOf9JMRcDtLn_hjet6QE4v-qFWTDXQxPGNMq-ZF3KVdHwOp5U7KYgip6qHwD8WLr8XHl79eKiozjZBsYQ9QkyWkX_CvFIYpQejB4LQ937YORIc3XfJALVaeKC0TSQPJ0_QWHDCaWd5VvpLBtKYuchET_yWAWq8FPekMzF_lGPsNiD5Uyiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۳ تیر ۱۴۰۵؛ ساعت ۱۲:۳۰
🔹
دلار امروز با ادامه روند صعودی به حدود ۱۸۳ هزار تومان رسید و نسبت به روز گذشته افزایش قیمت را ثبت کرد.
🔹
در بازار طلا و سکه هم سکه بهار آزادی با رشد روزانه، به حدود ۱۷۵ میلیون تومان صعود کرد.
🔹
روند امروز بازار ارز و طلا نشان می‌دهد که فشار افزایشی همچنان بر معاملات این دو بازار سایه انداخته است./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://telegram.me/akhbarefori/670959" target="_blank">📅 14:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670958">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
اصابت پرتابه به آبادان و حوالی ماهشهر
معاون امنیتی و انتظامی استانداری خوزستان:
🔹
امروز سه‌شنبه ۲۳ تیرماه، در ساعت ۱۳:۲۵ نقطه‌ای در شهرستان آبادان و در ساعت ۱۳:۳۰ نیز نقطه‌ای در حوالی ماهشهر هدف اصابت پرتابه قرار گرفت.
🔹
حادثه دوم به دو انفجار شدید منجر شده و جزئیات تکمیلی پس از ارزیابی‌های اولیه اعلام خواهد شد.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://telegram.me/akhbarefori/670958" target="_blank">📅 14:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670957">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_cS6QaVO0b4lqK4EEBWUL70RQiQ7qRuF4VtEi39walfY_TlNO2QJ3aIpRRT4l7trLxFYZqNexQGbmFI9p9ojImmgBQVTepU0F0RhRRcTLO_D0pNJhUkCMFwBz85g0H8-Htyt7cNJmLdB3Zy55kFkMSyOMI3W0BLsA1Yhk-hiiDTqkPlDH1H5vOyfhURwrbSo6kJqZu4pKeC7_JT_VTCf9jnA8y-RZHnvBlZNMuazYMbLX1CS70AkKazG87E8VraU667ln9gs7fsWvwWTekDOV8PG7jFTCEgxQ0ALTXkxhLQmQUqWiKMP5nVYls4ZqLaSA2ATuapIuoZ4WM4ziLbXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت همچنان صعودی است؛ ۸۷.۲۳ دلار به ازای هر بشکه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://telegram.me/akhbarefori/670957" target="_blank">📅 14:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670956">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
تیزر قسمت اول از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای سعید اعمی که به دلیل پیدایش غده‌ای در بدن و عمل جراحی برای رفع آن، روح از جسم ایشان جدا شده و در عالم برزخ، عذاب و ثوابی که با مرور تمام امور زندگی از جمله اذیت فروشنده پیر در ۵ سالگی تا کمک به جوان در راه مانده در بزرگسالی را درک می‌کند؛ نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: سعید اعمی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://telegram.me/akhbarefori/670956" target="_blank">📅 14:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670950">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XJLlvolTGoEFYCoHiI-wHocNhcX3PHv8QjKkBgo4G6S22Aj2Hgit_LMAZMaZrJjcK_AQTvwjQNRv6ONyZutrGqSKXc4OTQOnIDI6Q-DvblORoW4Osb4m6WQJhmywKs6eIFDTzOsHtlVZmNzipuX-CspyGlBc84-4vwtgKGZFrpmeX0f0m-x4bkk6I-U-68nlYnxRJje5ZMPrN0KMjlf4usMEd-ET7KShy5d0eHkFwQzt-IWfg3xv9JYEGTaDc9bQGP9swaFzEb0EhBQG9xGGDlgY533uZvA3HYI5c5tT1yBKTGCkWjm6xrfUNjr1ZNZ2OT5cC1dK5K0mxO8GaSC1Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZdJxXQ8BE3dI5MFyVvrSjGDDRpix526If7AqysUwR8Zel1FUOHNj-E9ruCCRjp2EQt1ohZHOs6FgTF2fnbhGRW1sOGcN_9NicTnc5ZLLC0ug8tche5iszqu52EGTa80lODDdokADzgO1OMKBuvpsL02R8RamRt6TTBs4jim0jZVsrY9PxVMycDQOltEfK7nqINeDb3Nk6oULGmZCWNyWVh1QTKslLo25YeaORoMCnfAr9GUlmW0UqjCce7zKguy_XCP9bO1RseQ0HQO92qoouk21rJPcTAilgQD-54NsL6r_A9gP3WMPvny9Y4Q53mmE_lC9wz8XDCh9QnsWshcbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fm_i6fEcupuFa4elB9VI_1ZUKN2itEKnITlECNaJpk88rnfO_jE6KHICrOpRzBF9NtEKM-X-yFyhHOQbCk5Y-8Kb0r7-rTcO9_XUVg08AHkMqjBVNuNYbmQ_L53MIIWx7cmSS_-F5fmkgAT88EYmClqu8W56cyUlm25GavT_Q94raGoR_NRopjyl_v_thC3256fyP4EaF03XGEnycxTmSjlphCfEHqI0nL5_94nygJvilToodISV9gd3k1aCzk3bIMZXicM8bVhU5IsX1r-GvjMt3bWg6-66rlA3g7ne6e17v-BOnSE-RXieJvwaTivOuNdW7OKD1zhpSQ4oulpzHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qEKQ3tSasZ_3YxmvUgGs7bGzARoAHXNOaQSQ-hmnaC4OnxnG5NR-i33l8JJiLSLmf0CYK4S4rsUgrnROIPtjMKWpuLSZRX1vJRvup70qUYk4rkQtFrEAa66eRGGJmTW6YIfmxHcHmsQB6grpraK2vWZOcsS8XJZeEGbOl3brywRLs7rY5LmwjHNwH9IHxCNObVaw-HXrKTakg4btrUe9OlO-sR97QmmG8vZRc7YYY6xWITflMlOs5eV87kn4SIgDL76MeOCcPF1ACuP2JdZXkkidkheu9rOZnSTqUnPQpHD8Sbuko3HFRRnfaApjuBkQaugoZ0diqm4mHgnW4iIvwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e7Xn9vc1NTwTeW2aTsIaRw3ft0FRgz_Cu-qj5DrDVDDLrIggJS6OlaGRRbDFKrqJD5b4O-1bVixcx8OseoV6CLdYeJ5tuftqaokdlPaxRkNg_IZSCJ1mbl7BokZrVv0e8Z2YKVB0ZNgT7DkLKJDTR32jQyP_uxiSAe7JUpLck7u0sSbVi8HalJYZuVRjVIWP3sr_Ym5-DDNl22ARV89j5hOaI-F1mXKZAcN5V1CEFY4THzrJhLmFe1wyUsAv2tvdZBCA40L3PzFJbgnsn-g3ArS8_wfWSKfbve1IEbbUtz3oU_jIzC7YJ5bTK4fUWAEALGCtd9hUwn3JlkYLz3biaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KUe887w_E-JCl0vgDlxIKM9lFFqcIw8ZhoXbhqYCQK0KbtIJ6-7MWfZ2DUrEPbMVmqHFezZHZzJyyZ-_iBKc4L3uihv43zZdUew3fjFxKC38-eGrpK8gREeQfmNl9p0OpAb7hHmL6fZpBekJC8GIWXX_7npNoLHqNuSZq0Ipm6Y5p1Ha5U-D7i2u5sRvaUHO27KjyP9ASlsPV6rPrCaXMhk89XfZgJMF0LOLDBuFMl3AdVQQk-BSfhk5EGqLLl8FumFCFCCYDaHuYUHgtYnJ9vCy7iFCvbJZ49ZQgltMMrC1MSv3Z7uKCFs54InoUfpCxhB3rNinlr2MSQAiay5hbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شال مناسب هر رنگ لباس؛ این ترکیب‌ها استایل‌تان را چند برابر جذاب می‌کند
😍
#فوری_استایل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://telegram.me/akhbarefori/670950" target="_blank">📅 14:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670949">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6bd01cff0.mp4?token=lit6Nn3yjGh2TSs_qBKGnPUr96DNEA7U6kvQrCm3DgtK_nDyauTHddiJop2ZVaaU-_94GBkTMNDQqoxvqx79zzV2cyCBSDmP8DVcJCWLcWAEKhhEIrt_J-QNOks-ClFKqINzjUy4cDRPhLUEAJCBWT1SyxZx-Sm3y9VikO7qQrzGM7A7DsODLu-R6FcsX1wavzOcIfeBIbv22aWWcAth6OF8ta5euplBYVqz5B5L0yFJZUzoxUDiSn-Wvb7FQdzEbPNkxpaLoAWUSz8UG-5rBSB9uJ60kmALWdgsYKoC0aEIIItywAiXpI805JAj8y2ydVKOc17PowzMnkySMRtjiAf7rh7L7jZdLJsEqLcxTxY8jukaK7IQ1guQFV4YMf6JCFZi6x4iSvhCaQIf2ZCpeexG_m1hBzMwhkIaxQANwwq0nJjqa97Qe2kpI5vU50IkkaF-Gfs81SXeIXKVV7WD2bmdSruHjLVdRj7F5YABMsFG9M7mdfsjRsGfJgLzvuTrXC0-0d-nrmlKnFNPTT4CXkJTkhdAgRScgTgpL4DFq-SC0FwFeJ-vK0tXYzMj8QR1liHjghATMMedXCG-_4oMeTqqBHJm6OWwztolVnBdYz71L5JdUUKuHO9ExBnujrD3rrOkhy8IuoKUZT8DjFz5fbs7UsIdSxG-iyeuDcZURe0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6bd01cff0.mp4?token=lit6Nn3yjGh2TSs_qBKGnPUr96DNEA7U6kvQrCm3DgtK_nDyauTHddiJop2ZVaaU-_94GBkTMNDQqoxvqx79zzV2cyCBSDmP8DVcJCWLcWAEKhhEIrt_J-QNOks-ClFKqINzjUy4cDRPhLUEAJCBWT1SyxZx-Sm3y9VikO7qQrzGM7A7DsODLu-R6FcsX1wavzOcIfeBIbv22aWWcAth6OF8ta5euplBYVqz5B5L0yFJZUzoxUDiSn-Wvb7FQdzEbPNkxpaLoAWUSz8UG-5rBSB9uJ60kmALWdgsYKoC0aEIIItywAiXpI805JAj8y2ydVKOc17PowzMnkySMRtjiAf7rh7L7jZdLJsEqLcxTxY8jukaK7IQ1guQFV4YMf6JCFZi6x4iSvhCaQIf2ZCpeexG_m1hBzMwhkIaxQANwwq0nJjqa97Qe2kpI5vU50IkkaF-Gfs81SXeIXKVV7WD2bmdSruHjLVdRj7F5YABMsFG9M7mdfsjRsGfJgLzvuTrXC0-0d-nrmlKnFNPTT4CXkJTkhdAgRScgTgpL4DFq-SC0FwFeJ-vK0tXYzMj8QR1liHjghATMMedXCG-_4oMeTqqBHJm6OWwztolVnBdYz71L5JdUUKuHO9ExBnujrD3rrOkhy8IuoKUZT8DjFz5fbs7UsIdSxG-iyeuDcZURe0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری شبکه عربی: کسی به ایران خرده نگیرد که ایران حق همسایگی را رعایت نمی‌کند، کدام حق همسایگی..!؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://telegram.me/akhbarefori/670949" target="_blank">📅 13:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670948">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
دستگیری عامل ارسال مختصات نقاط حساس کشور به دشمن
🔹
مرکز اطلاع‌رسانی پلیس تهران از دستگیری فردی خبر داد که با سوءاستفاده از پوشش یک پروژه تحقیقاتی، اقدام به جمع‌آوری تصاویر و مختصات جغرافیایی نقاط حساس کشور و ارسال آن برای افراد و گروه‌های مشخصی در خارج از کشور کرده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://telegram.me/akhbarefori/670948" target="_blank">📅 13:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670947">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLxixDbOlNE2pH_GTwV9xDetX5vhspo0yIO_fZIKIF9QgMnB6PlP0Pc0RXaVeAitgI4ZLmqwFHUpuVRdJtudoo7x7LDX3YHs5a6iCN7Tr9dK-miect-t4WVxbxoMNMX7it6SusiHyoa53KWVlKirtJ4j1s_N_2JGgHna8leEV1Lfk42E4f1O8GSfyG8SbNdyrGyo43PbqP_fAJFTHvQNW__K6dlKEey-XhvVQjTOkDl-kuu-41AUumid-pzOEwq64WVOawSfiFdQTN4zQ_CcErPN6fhLamg18OFt-iFnbBq8pfkNF6YgoAoluJyZlphU39GrZAbE0yaTKbsQTuQaIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◾️
تنها ۲ روز تا پایان مهلت ارسال آثار به سوگواره رسانه‌ای «بدرقه یار» باقی مانده است.
▪️
سوگواره «بدرقه یار» فرصتی برای ثبت و ماندگار کردن روایت‌های مردمی و آثار رسانه‌ای مرتبط با تشییع رهبر شهید انقلاب است. از تمامی هنرمندان، عکاسان، خبرنگاران، فعالان رسانه و تولیدکنندگان محتوا دعوت می‌شود آثار خود را به دبیرخانه این سوگواره ارسال کنند.
📌
بخش‌های سوگواره:
• گزارش ویدئویی
• عکس
• نماهنگ
• لوگوتایپ
• پوستر
• نقاشی دیجیتال
• داستان کوتاه
• تیتر، خبر، مصاحبه
• آثار هوش مصنوعی (پوستر و انیمیشن)
📌
هر شرکت‌کننده می‌تواند حداکثر ۳ اثر در هر بخش به دبیرخانه سوگواره ارسال کند.
🏆
به برگزیدگان هر بخش، جوایز ارزنده و یادبود
#بدرقه_یار
اهدا خواهد شد.
📅
مهلت نهایی ارسال آثار:
۲۵ تیرماه ۱۴۰۵
📩
لینک ثبت آثار:
https://survey.porsline.ir/s/aU5VZuaW
📨
همچنین می‌توانید آثار خود را از طریق شناسه زیر در تمامی پیام‌رسان‌ها ارسال کنید:
@Badraghe_yar
برای اطلاع از آخرین اخبار و جزئیات سوگواره، کانال رسمی «بدرقه یار» را دنبال کنید
👇
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://telegram.me/akhbarefori/670947" target="_blank">📅 13:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670946">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
رویترز: ۸۰ درصد آمریکایی‌ها جنگ با ایران را طولانی می‌دانند
🔹
طبق نظرسنجی رویترز/ایپسوس از هر پنج آمریکایی، چهار نفر انتظار دارند جنگ آمریکا با ایران برای مدت طولانی ادامه یابد.
🔹
این نظرسنجی نشان داد که ۷۹ درصد از پاسخ‌دهندگان فکر می‌کنند دخالت نظامی آمریکا در ایران «برای مدت طولانی ادامه خواهد یافت»، که نسبت به ۶۵ درصد در اواخر ماه مارس افزایش یافته است.
🔹
تنها ۱۸ درصد از پاسخ‌دهندگان گفتند که فکر می‌کنند جنگ «خیلی سریع و ظرف چند هفته پایان می‌یابد.»/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://telegram.me/akhbarefori/670946" target="_blank">📅 13:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670945">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
اصابت چند پرتابه دشمن به غرب بندرعباس تأیید شد
🔹
استانداری هرمزگان برخورد این پرتابه‌ها را در حدود ساعت ۱۳ امروز تایید و اعلام کرد که اخبار تکمیلی در این خصوص به زودی اطلاع‌رسانی می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://telegram.me/akhbarefori/670945" target="_blank">📅 13:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670944">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
راهور: جاده هراز به دلیل انجام عملیات عمرانی در روزهای دوشنبه و سه‌شنبه ۲۹ و ۳۰ تیرماه از ساعت ۸:۰۰ صبح تا ۱۷:۰۰ به‌ صورت کامل در هر ۲ مسیر رفت و برگشت مسدود خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://telegram.me/akhbarefori/670944" target="_blank">📅 13:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670943">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
چهار نقطه شهر بوشهر مورد اصابت پرتابه دشمن قرار گرفت
استانداری بوشهر:
🔹
در ادامه نقض آتش بس و تفاهم از سوی دشمن امریکایی ظهر امروز چهار نقطه شهر بوشهر مورد اصابت پرتابه های دشمن قرار گرفت./ ایرنا
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://telegram.me/akhbarefori/670943" target="_blank">📅 13:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670942">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a21c16fb8d.mp4?token=evx-7OhzBx1vHrAo21LHnOvCSo_VLHzF2_rziTMh7RQD6lZoyvvD1iso2-YbHqgMVNc90xTkj-Bw3N19RxFEofC4eSy008UxAWQaOrqyLCImeFbRpxXLKtcee7ljF6J-GaBKpO5RaFI6fAQ8IGo-ZDMnWwiMY9J6LMvyCpD1S0e7p9pEP7jjwlxy9XbWPk3ZVrIBzPUDOXygGAXeolyu7eIa_XJiQ1jFbhRRJ7utxGmIsSMntWLfl4mRBE67ptqzbyc7sxPvI6Uk41DyetWIuOsJj8_jJFbwajiQKKUuo51KlH0NcwQO-jp9ruaDMUiVuOVep0s00Hh0kW7_G367SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a21c16fb8d.mp4?token=evx-7OhzBx1vHrAo21LHnOvCSo_VLHzF2_rziTMh7RQD6lZoyvvD1iso2-YbHqgMVNc90xTkj-Bw3N19RxFEofC4eSy008UxAWQaOrqyLCImeFbRpxXLKtcee7ljF6J-GaBKpO5RaFI6fAQ8IGo-ZDMnWwiMY9J6LMvyCpD1S0e7p9pEP7jjwlxy9XbWPk3ZVrIBzPUDOXygGAXeolyu7eIa_XJiQ1jFbhRRJ7utxGmIsSMntWLfl4mRBE67ptqzbyc7sxPvI6Uk41DyetWIuOsJj8_jJFbwajiQKKUuo51KlH0NcwQO-jp9ruaDMUiVuOVep0s00Hh0kW7_G367SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله هوایی آمریکا به ساختمان سازمان تنظیم مقررات و ارتباطات رادیویی در بندرعباس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://telegram.me/akhbarefori/670942" target="_blank">📅 13:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670941">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
ادعای دادستانی بحرین: سه نفر به اتهام جاسوسی برای سپاه پاسداران انقلاب اسلامی به حبس ابد محکوم شدند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://telegram.me/akhbarefori/670941" target="_blank">📅 13:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670940">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
ساعت کاری ادارات قم از ۶ تا ۱۲ شد
استانداری قم:
🔹
ساعت کاری دستگاه‌های اجرایی استان قم با هدف مدیریت مصرف انرژی و حفظ پایداری شبکه برق، از ۲۴ تیرماه تا اطلاع ثانوی به ۶ صبح تا ۱۲ تغییر کرد./تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://telegram.me/akhbarefori/670940" target="_blank">📅 13:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670939">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JAchlLvfjand9vxvgwZYkPWuwp_sLKEuoeUKXTyyX8qi0IH-_xQSEaF9whIFmnTwMv8dLx22hijjG0M1U_o3N2mWW45Hidb2rjzFI-Bq9_0R4UL3cZ0jh69cpijbCB5cIEqkx4Nl572McynoUy5igA4ofY1RkSQMmED_54LwO2m5btxr2hq7A1PZ5SSNLzVnrwLoJ9u0-TecBeoDCBwaJyQMNVaTH5ld9z8nkz1I38TmTvESNrh7CBNsoWfbZURqaqXJQmqcgkQUjahIMTPuWoTXzFP7jwg5mFulzADbrZr7EQ_Z8QFj_6zSQ1gGD6zImsYNL1D0dLRoVk2CgaSltA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام رهبر انقلاب به کشورهای عربی بر روی موشک خیبرشکن آماده پرتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://telegram.me/akhbarefori/670939" target="_blank">📅 13:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670938">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a5fde6ff9.mp4?token=kyx9KeDExrmxY-2Z4f43TglS-xZcL763sKLsQNy98UYBecb5BAsFLed818gJALBhysGWqNz0Ufqtd0sbR02xy1kKqjbxM2bWDbF2hG3r_KxBEBu8V1umAED61MhZrObt2YtwpD-mm5oEZv5RxugTSRW_1A4RJFh7FwxO3EhUjzWk8Z0zTAQSz0T2ehPSq2ef1yksn876FqrU9puiBxIxnZHfJSTu-U9_kGkud8Q39Xyc1Uj5httSEfdJsK65PBQU84FolI7YWPcB8c_2K_svw7lBFQ8zfJqv7AXPK4BbjrpDUsMvyKdK8ITH5HsI3S33Ma-UQEHItRknENzG3K1iVohlzyFDi2_f-Ur7spnTOsiGZjGC6lcoc67qx2zAh57k-7Q-HGiAsiWj6lTtQeHsmh5vBWfsWQhlJmikEVEnpcvKn2kLKxBlsSQccCE7GH8C5yGQpFbwcl6_Yiw6R-zi29lj95e6mmWgUHO4-N5m8cjzALYN-0FsD_FUNQv5uGHxc7zPqEE5J9C-YDDLNaqUOKWwE7Om57qF0Czn1xQlyWL0eIUxTESuviQXpqf7jxJs7eur30n1PaA8mPabqy_1FCK6sv9DrMr-7i29ygrJJlcF9qH5NLdRLudyc6EOMmqCd3qzbUfh7gvZHEMD-wXThgVeZartsVuTf0-z7XuhfD0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a5fde6ff9.mp4?token=kyx9KeDExrmxY-2Z4f43TglS-xZcL763sKLsQNy98UYBecb5BAsFLed818gJALBhysGWqNz0Ufqtd0sbR02xy1kKqjbxM2bWDbF2hG3r_KxBEBu8V1umAED61MhZrObt2YtwpD-mm5oEZv5RxugTSRW_1A4RJFh7FwxO3EhUjzWk8Z0zTAQSz0T2ehPSq2ef1yksn876FqrU9puiBxIxnZHfJSTu-U9_kGkud8Q39Xyc1Uj5httSEfdJsK65PBQU84FolI7YWPcB8c_2K_svw7lBFQ8zfJqv7AXPK4BbjrpDUsMvyKdK8ITH5HsI3S33Ma-UQEHItRknENzG3K1iVohlzyFDi2_f-Ur7spnTOsiGZjGC6lcoc67qx2zAh57k-7Q-HGiAsiWj6lTtQeHsmh5vBWfsWQhlJmikEVEnpcvKn2kLKxBlsSQccCE7GH8C5yGQpFbwcl6_Yiw6R-zi29lj95e6mmWgUHO4-N5m8cjzALYN-0FsD_FUNQv5uGHxc7zPqEE5J9C-YDDLNaqUOKWwE7Om57qF0Czn1xQlyWL0eIUxTESuviQXpqf7jxJs7eur30n1PaA8mPabqy_1FCK6sv9DrMr-7i29ygrJJlcF9qH5NLdRLudyc6EOMmqCd3qzbUfh7gvZHEMD-wXThgVeZartsVuTf0-z7XuhfD0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وضعیت پرونده «امیرتتلو» از زبان‌ یکی‌ از وکلایش
🔹
توبه موکلم از سوی دادگاه احراز شده و این موضوع می‌تواند در بررسی درخواست‌های مطرح‌شده مورد توجه قرار گیرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://telegram.me/akhbarefori/670938" target="_blank">📅 13:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670937">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
هشدار سازمان مالیاتی به بانک‌ها: املاک را نفروشید، سال بعد مالیاتش را می‌دهید
رئیس سازمان امور مالیاتی:
🔹
اگر تا پایان امسال املاک، مستغلات و سهام مازاد را واگذار نکنند باید سال آینده، مالیات عایدی املاک مازاد همه سال‌های گذشته را یکجا پرداخت کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://telegram.me/akhbarefori/670937" target="_blank">📅 13:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670933">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qB6_sxk6yrK39ZL-aVvnc9GGsXajyCXXwWfbXeh8gT6JCDMfW8Hc3W1q-YbxMkDI1ENFKrxcLiOOPOLZdm9KQaZR66jF6iTTCng3mNmIcJZqwfRRBfE__qfu4OPi-ps87uzUfN0_SpY-CbgEdRhw86h-d2wE_R72vD8SkMzQafUOjwq_1dwSv1DYzqM7LOUB_Wg7LQwbbZnNaMFqIj4GAsLlcjDKRQ84FsjRR7Tk2kRcSXLQcGSjJtQnKhp3F9TK-mfC3nyXtRnnHppJOBs86jn0wY4xafeqcu0vPWKBqFg48IKmEPBp19ZZTeQBgcDOVWPhn3YJtVOlia_774aPxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QGRsps6dJMcDx61TNVwPVTQBciZzhF0dg-1n6zDZq6PMK_qvbETCICDUc7ww6E-fYnungVrLDr5GrWysywCABvw74vUYVk97zda0Sv_--iOiOBboUm-foLhVyoUd-m-NipTONj7nuG7JoH95VrWOMA7oG76xWSTulW0H212Axr9wRYMBbjP2ZM59VCPv6t1uEo-7DnuSBqnCqcu-vJpEok_HVz7jmNfZhFaEmXESfp24IQy8PiX2GNjWAxiOrfMIvXwTcaVtR2Uv-jrWSkR5YpC_J4FodPeatUxNHRnkqRxWGyNUgXwfnvP-g2Zauc-uW4Tc-WEB_Qsz24VoQwlI2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BmkJSiAJGzD16xMsRbde072YuUEdudMalOQ1yxXiJcSsRWPQJM4Y5seJvnma5jkuttQNjdEXHEhv35giJaOh4fzp0C9Qg7ktIgA5eLPjzQ_atwa_zStb58LkwYWaPkO8p15gF_wfljpiyK4d2HPRnrJJS_lhtuszwy-2tt3Ojr9reEI720qI2FGrcCaGykXIip-aqUz3G6MgZshg8NjjTiGouS-GrtwkAAjpGrL-WxFUNxLT5s5Tb_3st6c7dBJpwwlaYiWcnDkOeIrqjvVWj9qiYC2Gfx_0xvD4qPenMygPgWt8QVpp91GdVoDEI_0p5dblJMh-sj9z5qmsyQ5XiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YksAwWrKESU_mY-TJAzmJSy8XLxvJGBiZaBKZ9yb3kkq0in4E1yEm9UaWU7YIRTt5sYlwdb47iGZjBgDvlHaKUabBk6JG1UUW7vktXlumu-dTRr4WytuIJjLx5OE9ge_gTo7ckYyB7u_sHna36526TTM58olJ2_XRAJrnfm5W5gjUZVc5hLpFAg5hhsPPUQ6EEiNK4OzcU8it0dWG1LgwEoLE0ug4bgJ16unkXh1TXscWQwqOtwoTdhKSJN_q71QkwGUUYfap15zaK5e47JV4JJxjJsppw2JDYzSe0TUZ9Ai2KX2HdPMPkBmA-FAlzJ7Ky2vqTrxwT6zp2V7YHrf6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
راهنمای تغذیه ۹ ماه بارداری
🔹
در هر ماه از دوره بارداری باید تغذیه به چه شکلی باشد؛ در این اسلایدها ببینید
@Tv_Fori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://telegram.me/akhbarefori/670933" target="_blank">📅 13:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670932">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HwKC0uNIZOBZJGHEiG-eKELlxliJBF6yInjauS0rVt0brNCS2eBcHvvkO9sHOWhCqGu2eg7lSICXTJsmIBSDsvA92X2K-lMirIUYuDkznTFuLOGIbNEwm66Yvb48xHN_sffohHOrSuuBWp4x8P1j9ktOQ3Bs8YsUqtfdL4ud4r1CWk7n9I4ql5hqj_dk0jUdA13B7_FNe3sTGJc-TVvQKdHNoGvIBnMVSBBkWCVh4RniuyBDcd8dd-wC4KgL1Pt1sxzzMKQ_jQWyZWRibzze1Sa1YqzHXGMuJT1NlmSN8wKfvloJoZXRLF4_ftqrcvoVb7sjNoWIPv9fuk7nLlE16Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تماشای «فراموشخانه» در تالار حافظ
🔹
اگر اهل تجربه‌های متفاوت در تئاتر هستید، «فراموشخانه» روی صحنه است. این نمایش، فرصتی است برای دیدن یک اثرِ دغدغه‌مند و زنده در تالار حافظ.
🔹
با استفاده از کد تخفیف sahab15 می‌توانید بلیت خود را با ۱۵٪ تخفیف تهیه کنید و به تماشای این نمایش بنشینید.
🔹
همراهی شما، انرژی اصلی گروه برای ادامه این مسیر است.
📍
مکان: تالار حافظ
🎫
تهیه بلیت از سایت تیوال
https://www.tiwall.com/p/faramooshkhaneh2</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://telegram.me/akhbarefori/670932" target="_blank">📅 13:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670930">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
بغض تماشاگران خردسال برنامه محفل ستاره‌ها با مداحی احساسی برای رهبر شهید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://telegram.me/akhbarefori/670930" target="_blank">📅 12:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670925">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
محاکمه مهندس ایرانی در آمریکا
رویترز:
🔹
یک مهندس ایرانی‌تبار به اتهام صادرات غیرقانونی فناوری با کاربرد بالقوه در پهپادهای نظامی به شرکتی در ایران که یکی از مشتریانش سپاه بوده، مجرم شناخته شد.
🔹
دادستان‌ها مهدی صادقی را به همراه یک تاجر ایرانی متهم کردند که سیستم ناوبری مورد استفاده در پهپادهای نظامی ایران را ساخته‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://telegram.me/akhbarefori/670925" target="_blank">📅 12:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670915">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lKyPzEMA8XAWZPJpxErIzqIcKFQCWeYt2wSfLj3_AWhs11WdVAwH5kOd2x2B3KporC9UsmyyYLMwH00JEaXN9nNrgveAPUuAeG71XdrD7Bm5W-5pvjOH2LdlV4hMqhE2vy4xfcFuATrZYr_zCzbDPGO-gWFZ_fKyPf49YO81L7PLFw94RySvxF_hVHRZQ0qJgO-yyaekz5syJGffdPer7U_vGnNa3OwVHq56iKGT4VXt16C-2Z_PkAhM5R8LpxAbqwgD2fCnzeDN3uYAyw5vVT_otZaeE3QTm7IJG9OieKfK8WsstKjpDjSqsvkWpleaIHqtWcmLfo0tvQFRR6IaJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sWHiTI0by8i4FvV6itajlGL0vvALVRxbfXtW24apoJUDboo1bc34qyPw-XorIeK8hW8R3xVzG72wCOIBuc4V5tc6rSsd4FyFzhShgN9_Cmauj_zm6ZrhGzpdYHS7rc4C-OH1wbFVLof72_H2UrcvynL9RnnC6V55V7GhS8WqLzO17gXEf8-5Xb8jhvgue0vb5gZsZaFymHpdquA9Cmvv9X9WQTTOyguR75xmdRvZtfw5gwtWzDNn0mTXa9v0xUKl1Mla9w1SdWoaBTnYLml4j9pkMez_S5BKRqIEiwBRp9WMT9mZZcCYv5D1rr9axieShQ03GChBOVvq0wq5-d-PtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z0HXspN8FwExu5H_FhjsNpyl1tPjk2TQi374MgQBsnSDmAMqv20t4MIjUHZn4-y-4KwZc-wQ55e8USj9FS6D38MxmF25jxNyqk2zSYL7cbV9PIljyssagyKDZ-quZc7F4RVlJQZySo-cGOO3tXklGzB9gmEWrKEBwG1jQzsNtFZiGZlOKSYtOF8WwXliTU8yZLB91NWsK_rFX5QPg9tgjnXNXmozRYk3d2LCRTzIXGVRGPguxGiWZSAABsxycVYLi59TG2_IRkeNh05bZd0qMdmCn6IMJLEIfLf97shOI-415gmKzkuHe5cR0cUi4ueNH0Xv95dO9KcNlyfs0Lm6dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tkMil8wRfB15YSCZo7hGT9DjYbcJ6_94J_u4zvoX1BlD6mW1SPav6Tff6S4qKzmRW7sgtcxAgGQQUF0ec6L5fCX4g-1N0p3YpxWptpD1_YqGQhehg3mahUGdtTw6kDIZuoP-eX8zsMYEMFG4fqx2aazyYX7AR9Fp1IqQgtD5iCoFzSxQmLgTp0BJSvwlWOAB0fajTJ--x4H2It3vlKqDInl2dggF8W51Lzxi2hTBC8vXJZRZZekPzeetsFz7EJ_RXsz6DG4yYEGSjXJsKgK600R7HX2GD4aMnFlwtfgvWaCfPa5FYeSvrlqmC-BRqEXwtb0PGs2sNBHw5YP04HbxDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l-ZeOhUQJu0HtEVZsJZvdYzTdCQWDKOHHJepwejB3AmkDDkcUiKD94Tt_AT2XVuvOboiXIjVZNJv-hINqqrz4Y3jLHGShU2l5oWwgkacWJahGH41jsuGvutfLeFwvgZx0SuyajkMH_qKPcB_6svfCfwN-TzkvQqB8FXXZjtCKhtLaG7C6WCXLuguFghh1eSn5nqyA-bgkAGKzruDIgOGK5ud35v_DyB7A1U5VnkRUV87vhER_VpehrCTsbZnFu43aNlciRYGFFWzVhz2l3OLC23IB8n1NGOdRWV4RPKxFxXclgauqVeHYvYtn8dpT19axXtQx_wjTlZXV6q0UVMvog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZGCgP3_ASl10ZHo7lX-A5Ve3EHMiVnz2lpqWPW9LAyLtPnLZlpUGzUV0QkWht6sywjxBi1bJKKi_ns5DxX2HT9UWZumxg7DvknBxGh6YEOibrRNMBwegSyM1KsTX0mrCB3vzJAMPzBKudAhk9tnVs902NXAGDEl0vtebjXM3TQQfK3Y6VffOmuO4NYGHBPm8vxiacVt82AP2qvAjvbxvavfdokbSDfrZJ3fGyQGDO3QWPkXvUqV7O5SEKCasIpkZ9VAoJTY_0deZkb1G_JBvSJfAq5hnBcoBsk87Ra0uEPDdEHeC_bgcvNTXr-kuvHxb7ZkmNc2bpVO_YY6COes8Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OVZPyfnXAFua5eu2B8qK_4gfVuciYFbZ1icc8n7-R5StA39-Iy8YSrG9plNgkC4On5JP6qc9wZcBDWZgiQFjcQLQCr-YltLPWAlAlZnDwNZ2yFrp02savz7zSQsp_fQr8rl313CGZnr-AKuH3LtN9DmILV-oVnFwcPYN989OgxAG36tjROnvZFEJ1Y_RcwFEpoBiWHZNhaZJVJMvBfoApIk1cNEbgVGUSR_tFiZPRszIjUf3cAypD9RMGccXNU1zKv48IFFb1l7La-eSy7tsg8ab9dnuts2fJuA1mjXoTqsbfcUaD6kzE2_97sdQ-n3u6SUsOr-i_SW4u3vbRQv4fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WeRCfyZAW-eBFSCVP0I4RMCPyXRhkS_iyT-Fo_MA7XBxkQn1Iim-naEvSgW-YJHNFLFiQWaXMbRblBa5-EeL8IT2gXa8ZORRTqsv7oyQtuXbrzet6xglm-xKS0__kpvoVgafZyYiwhPqKY8WGGmp8Cs1yD90F4hwqe8T8e7Ujs9foOwVE0JXqXH-AeueZjFIGMdcPIrqnAp0Bc2JaVexht0LxiobwJvbUEO3vYvu8JMRv5viPFp_7qCELOQIyLQSXnCCNTpJLFtiSuXKMldLxjrrDr4rdojy_1BPFyYc5rmGfpLEHI2KuWNhi1JQaQfg0v9CYPX20TB07BBFOpoMRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bp5W9KeRYTwhPur2fi7w4es61TCRTHwuyk8ek2FYHAmGV-dfpjzcogE7QLppNNUhXkjKZFMenzcav9E2rVgcXcXRNRk0e9l4pQW5X9ALmx8nyyHuDKDavmbUDMupVJB-bxC05mlnoe-Hgx4A98V7g_GDE3PBYHvjOeHa3DXrac9nRciHGkTdjJtM7mdIW_EQpckmDQJiVoBPgIBwoyy1RbBlP9O1YpLiHsctDCjCZcG3E6mzOnw57im4i4pkrB8kD-dPWTV9toXrQwwXDg21_2qohNU7G-ccacaRJFs4S423A5xuT035660428q5czI-t9Cvz_oA4zc1xPOeDAaIyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xjb97J5xRyLfeHPhtA8AeWD-9quh1JQiHzqB2qzgU2FAeedCqdhIgCpxbxtG22ophnFRByR9EvwLHjVaHT9QzGhFwJtZbRlAG2f2qCC0uHa6ytsI-2alxzDoqZ6KqWbzqIBpM2-Y-y-PNM21lzzd2fGDqrudzX08SnL88Pe1dwUQSuJhL75XQgKtbPDZNzLBXX048zcGs4oaTLYJS3MhlN3V6hyE9yaD3rnE6qh02H6USqFND0N4WLHsEnySbFEV6tU7rQkScJSrx-OnFhi2ylEaqp1PHwz0OwS0tTWfsbyo-Cbcl0kDn-L_4XdhfLt-ty0m9jM8zSbd7aJ5Di4DNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از فاکس‌نیوز تا نیویورک‌‌پست و تایمز اسرائیل
‌
🔹
غوغای رسانه ای اَبَر پرده‌های تهیه و نصب شده توسط کارگروه فضا آرايی معاونت فرهنگی و اجتماعی شهرداری مشهد، در آئین بدرقه آقای شهید ایران، در رسانه های بین‌المللی دنیا/ایران رسانه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://telegram.me/akhbarefori/670915" target="_blank">📅 12:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670892">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCAzlArCtKkcO2o-7dlq-t3h4OT-mIjD4fIb1JQHWHW96pW7BKpErfVkxRqjU7dbytYwEAua7wuhkUoLnbNrXcVrPIG8k8eMBXEh3ZLd8Pg5__AmSq8hjTYBUZc3G4kHop6V_3g0mnnRWq-28Pui9TQ1pTb9V2715-Sjl2DvGPGEauFNWk1UZT0E3_cPq2H4QMTXozONg8Dy0y7bVw3dX3ozwdpYIXS0flE0j1sPmIrN8ueyU88zXuJKnpb8INz83GxSPk-a8sSUl5Zx9t7B8_XTJD2Z1aTx64TEMPr5Atfor-EqsX0JG5gars4_8_0bKE5uiw0UTIQCDn-DpuFT6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زندگی ما به تصمیم‌های خرد هم گره خورده است
🔹
نیاز به کار عجیبی نیست، قوی‌تر کردن دست اقتصادمان از همین تغییرات ساده شروع می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://telegram.me/akhbarefori/670892" target="_blank">📅 12:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670890">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d2ae27004.mp4?token=Q3XTaiXtG-2cVy4m9JLbdGc9k-49r9OisFgVrVJMYep6nnBWJxRMbo1nf6WPcIYjy0MVqI7P7iEyUmzmJygPDZcRqe8cMqg40wGxz0L7bmr7YBOON5Nyf5UCdPROuiO5x_5jNDM8ljh9aDrXmYVOQJJL0ds4Mi_NzgH_ueFY5xBdEbhL96_b4NJREQXhqWt63C78deRXmXLSNgzfqCU5Azd_shfGGk14VGpo3LRK90u3O6oYsMS8x0DQX_8Fmzj5BV1ZPAKi1TbJwHs9GB7ny5HMU4xu9Ka3CORQOM9TiSz_4-sC2r7jDXvEyOJhbjWaNuq48UvfwrSFCQyyLxfQWyKn-kxDWBjNx0tBlTH7nH2FGRY7MxKk_vjXDumrH3zjRXEvhaFLxw8KkoeXIbXmbeJWDubBx2EvjzaVILu2MsKDEEDFivUxR_ZGUg3jGhSaZxYXKGAvEvMfEvmbn7b8Jug85Fri_1oEFwXr_ulBU7ZfGuelWOC6tDRQQBjbiLff9l5sf6PkipubPbO0-yaZB1Cbod9wlWfXOcuDA6IbFPO03jXoxqUqjdbl3zwL3xO8ZDKh4kcmbgVKXMp8o8Iz7BnMeisLylz-YSYVRqAdZ4lf5MEFLhY0xhDZBboYNslz4jCJZeofQG_sDlIfL2NlmOkcwb59qZpl3QMtCktwbRY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d2ae27004.mp4?token=Q3XTaiXtG-2cVy4m9JLbdGc9k-49r9OisFgVrVJMYep6nnBWJxRMbo1nf6WPcIYjy0MVqI7P7iEyUmzmJygPDZcRqe8cMqg40wGxz0L7bmr7YBOON5Nyf5UCdPROuiO5x_5jNDM8ljh9aDrXmYVOQJJL0ds4Mi_NzgH_ueFY5xBdEbhL96_b4NJREQXhqWt63C78deRXmXLSNgzfqCU5Azd_shfGGk14VGpo3LRK90u3O6oYsMS8x0DQX_8Fmzj5BV1ZPAKi1TbJwHs9GB7ny5HMU4xu9Ka3CORQOM9TiSz_4-sC2r7jDXvEyOJhbjWaNuq48UvfwrSFCQyyLxfQWyKn-kxDWBjNx0tBlTH7nH2FGRY7MxKk_vjXDumrH3zjRXEvhaFLxw8KkoeXIbXmbeJWDubBx2EvjzaVILu2MsKDEEDFivUxR_ZGUg3jGhSaZxYXKGAvEvMfEvmbn7b8Jug85Fri_1oEFwXr_ulBU7ZfGuelWOC6tDRQQBjbiLff9l5sf6PkipubPbO0-yaZB1Cbod9wlWfXOcuDA6IbFPO03jXoxqUqjdbl3zwL3xO8ZDKh4kcmbgVKXMp8o8Iz7BnMeisLylz-YSYVRqAdZ4lf5MEFLhY0xhDZBboYNslz4jCJZeofQG_sDlIfL2NlmOkcwb59qZpl3QMtCktwbRY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تجربه تاریخ؛ با تورم موجود کجا سرمایه‌گذاری کنیم؟
@Tv_Fori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://telegram.me/akhbarefori/670890" target="_blank">📅 12:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670888">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqQZJXu9kq2sMmEuIgbxR9N4giIbg89tf6XUq8aWyuUBRY3ePPpHo3FLiar_KZ6q0rUD-o-D_Fle0p5yLA6orbjyD1wqwIitH9cziaunedOTgyVVSOVyp3FBkfu7G2Pw5fZSrtLNea9xtC0QtRvsWDK816H_SS94JcJdtmve-KspGjJLArKNbeRlLYpFAK6WrJLnd3mlzqc7moNGFzNoiH490rUihs3Z3XUF0OiGNtgywWN36A8G0SWBmQ1Yqwt9Hu4Vcuu8szWXzPvV4kG58Q3cpUdYGcVcfDL_tSKB4Je-3M3E3uYEiTcALhmPLfQLzxKlu1Zf109-w8OocXTxyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
داریوش فرضیایی به سوگ مادر نشست
🔹
«داریوش فرضیایی» مجری و برنامه‌ساز شناخته‌شده تلویزیون که سال‌ها با نام «عمو پورنگ» در میان مخاطبان شناخته می‌شود، در غم از دست دادن مادر خود عزادار شد./تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://telegram.me/akhbarefori/670888" target="_blank">📅 12:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670886">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUyXeOeJFZeQYr3s-B5Ku2uUkvXnZ1hkHDlAEmgEWIAVqrbZEmqxi_FoDaUNKFIHj02WtwAx8MykYmwLh7WY-Kp06h_Ggf86K04NMHJbzbZEIjPnphkYyx470284AR0uTFSUap5wyWeH1cVLT7nJzvQQgzEpPPD4Pqk57OBBwLBhX3OIOfw3qPObILqJM-gRnqr9Zo5FA1OINX0IcTbnh6klJrRAIOYe7kBeKKFhp2ob_X4fANZy1XpYj1ABeojHUDrDUZtEfn1SyWXM4y4bzTNafZIbOX7SCd-qW-Jd0-NGESKg_nHkyZi2y0hQR2r_q1c6npbxVDQSEwwE9xVIhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نشانه‌های تروما‌های حل نشده چیه؟
#سلامت_روان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://telegram.me/akhbarefori/670886" target="_blank">📅 12:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670885">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0R9Gl1BRXenMDy4kFBkTa2bhJYhDdoawMm5_R1XvQfhrC_xXE5iWCbkRkOGyLMOlGopQwOUKWqz9J9gPFir_RbIaxtynmLKBgcWgK4tKWCLciePFJ3h5OaBr1YseSqQRaaW4Dgb-VTtgQivvnQ1YlQm-SwUjv8Z-js7RVSdEV6y0IUc6XSkkxErH6_AXRw9MqfD7mRU9gFM59qoUaT-c-0XAmsEYSUzi8UDFFhr3mERu-2XZcpGFh-nRAciP02Lrv0Dn1geLGFSGA5mPlLapfomlsSCKV1Gwj3QT1xuSdqRsoXpj0zsGwDnagcqLqrqj7yHv0olg-IsaR2qAtJkiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خواهر لیندسی گراهام با حمایت رئیس جمهور فاسد آمریکا به عضویت سنای آمریکا درآمد
🔹
به دنبال حمایت رئیس جمهور فاسد آمریکا، فرماندار کارولینای جنوبی خواهر لیندسی گراهام را برای تصدی کرسی سنای آمریکا که پیش‌تر در اختیار برادر او بود، منصوب کرد./ایسنا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://telegram.me/akhbarefori/670885" target="_blank">📅 11:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670884">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
قسمت اول آموزش سلاح جنگی کلاشینکف
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://telegram.me/akhbarefori/670884" target="_blank">📅 11:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670878">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
گرانی دینار در بازار آزاد؛ اثر نرخ دولتی ارز اربعین
🔹
به‌دنبال تعیین نرخ رسمی ارز اربعین (هر هزار دینار حدود ۱۲۹ هزار تومان)، قیمت دینار در بازار آزاد با ۱۰ درصد افزایش به ۱۲۰ هزار تومان رسید.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://telegram.me/akhbarefori/670878" target="_blank">📅 11:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670874">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
امارات: دو اوکراینی در حمله ایران زخمی شدند
ایندیپندنت کیف:
🔹
وزارت دفاع امارات مدعی شد که موشک‌های کروز ایران که به دو نفتکش اماراتی در تنگه هرمز حمله کردند منجر به کشته شدن یک خدمه و زخمی شدن هشت نفر، از جمله دو اوکراینی شد./ خبر فوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://telegram.me/akhbarefori/670874" target="_blank">📅 11:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670872">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
رئیس‌جمهور برزیل: اگر آمریکا بر کشتی‌های عبوری از تنگه هرمز مالیات وضع کند، مانند «دزدان دریایی» رفتار کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://telegram.me/akhbarefori/670872" target="_blank">📅 11:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670871">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 نگاه شما به پلتفرم‌های جدید خرید اقساطی چیست؟</h4>
<ul>
<li>✓ راهکاری عالی برای مدیریت هزینه‌ها و خرید کالاهای ضروری است</li>
<li>✓ به دلیل سود پنهان یا کارمزدها، اقتصادی نیست و ترجیح نمی‌دهم</li>
<li>✓ باعث ایجاد بدهی‌های غیرضروری و مصرف‌گرایی می‌شود</li>
<li>✓ کارآمد است اما سقف اعتباری آن‌ها برای خریدهای مهم کم است</li>
</ul>
</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://telegram.me/akhbarefori/670871" target="_blank">📅 11:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670868">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb05813815.mp4?token=KMvkd76jyn1mjLuvqn5Rgo0pdYaGlKjMTUrt27XVhYZjfU4jVKW9cZKDGKdPJy0eSLrR17QTxUpuikoNd3sitsbVEirP1BUqVU0ksfopOLLlUd_dxTfrzoPu8Q3SivJ3KttEePNWDOYeWIkmiAhQ2Kirh2B_Tifv-I3EcMegf4Nu1VYAuMYTO1xL7q09443vdMuf-K2CHjg09xX3u82VchR-WxX1fK4fk1Ujc4K4hLKbGERdgGiRJtSqsze8-YDO8wecXOYme8iNHis-cBAN0gv6tyArKhCL7EejvbtDSFN_BD0UDV5f2G53izdCX2saMuIaDoz-D4qo-xviKaLAVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb05813815.mp4?token=KMvkd76jyn1mjLuvqn5Rgo0pdYaGlKjMTUrt27XVhYZjfU4jVKW9cZKDGKdPJy0eSLrR17QTxUpuikoNd3sitsbVEirP1BUqVU0ksfopOLLlUd_dxTfrzoPu8Q3SivJ3KttEePNWDOYeWIkmiAhQ2Kirh2B_Tifv-I3EcMegf4Nu1VYAuMYTO1xL7q09443vdMuf-K2CHjg09xX3u82VchR-WxX1fK4fk1Ujc4K4hLKbGERdgGiRJtSqsze8-YDO8wecXOYme8iNHis-cBAN0gv6tyArKhCL7EejvbtDSFN_BD0UDV5f2G53izdCX2saMuIaDoz-D4qo-xviKaLAVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سنک اویگور، فعال سیاسی آمریکایی: امیدوارم که هیچ‌کس هرگز ویدئوهایی را که از غزه، لبنان یا ایران منتشر می‌شود، نبیند
🔹
اگر مردم آنها را ببینند، خواهند فهمید که همه افراد در رسانه‌های ما گروهی دروغگو هستند که برای اسرائیل کار می‌کنند. این امید بزرگ آنهاست. اما این امید اکنون در حال از بین رفتن است، زیرا دیوارها فرو ریخته‌اند. افراد از جناح‌های چپ، راست و میانه سیاسی می‌گویند: «من چشم دارم. من آن مراسم تشییع را دیدم. می‌دانم مردم ایران در کدام سمت ایستاده‌اند. شما گروهی دروغگو هستید.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://telegram.me/akhbarefori/670868" target="_blank">📅 10:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670863">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6d1aa412e.mp4?token=v6C9xLNugMS_NHEocbobJMgwDymnJ6LJB6SvJCwmWC1WwU-FFsshBXbv3cXw0xQNzmKBW9OjEUwnKskUuf7YXCrKAefJJR5pL0_sTbZwEFTVzI3A1HefxCTp553Qa8C662DWfGSsCYxIFEWduoIbAxxdEfnfsHghRJtHeteFjpL3XjUzvBHE5rUmEG2cv3fmgbZYxPEegM_40rzECoymAP52IGsPtg0MBWHZmj7MYOlN8Pye2BV-lR7ye2EKUB_6c4-wWB4elQDiEfOdY05k6IdvoGOx48M1QZDpR1y3tNyXbxX6pYDMG6qIaZ6c9xvUUDmOd4uLlN826jNWZDC0bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6d1aa412e.mp4?token=v6C9xLNugMS_NHEocbobJMgwDymnJ6LJB6SvJCwmWC1WwU-FFsshBXbv3cXw0xQNzmKBW9OjEUwnKskUuf7YXCrKAefJJR5pL0_sTbZwEFTVzI3A1HefxCTp553Qa8C662DWfGSsCYxIFEWduoIbAxxdEfnfsHghRJtHeteFjpL3XjUzvBHE5rUmEG2cv3fmgbZYxPEegM_40rzECoymAP52IGsPtg0MBWHZmj7MYOlN8Pye2BV-lR7ye2EKUB_6c4-wWB4elQDiEfOdY05k6IdvoGOx48M1QZDpR1y3tNyXbxX6pYDMG6qIaZ6c9xvUUDmOd4uLlN826jNWZDC0bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی ساده‌ترین چیزها بهترین خاطرات را می‌ساختند؛ از والپیپر ماهی تا CS کلاسیک
🥹
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://telegram.me/akhbarefori/670863" target="_blank">📅 10:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670862">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dw6J6f24KWyEeB50eCGm7gbOn-_f38Pm7XeXK6b8UV09F8NRHOpFrNinpPcsKQFOJz1ZBOKbJIOowMb_FXlFAA-eYtS5AIY2V0MrzakLQCxQM_oW7i91QU_47TEIuhi8GW5Op17jKnXbEd1nReKqnEkaIyZ8IfRydqVZpjeEPhpArL5Ta6Zko4w7VzdQYMKzJd27qRFD3j7oFMyz1tDNIve-JxJex4ChgLgBAeYdNRD9N4zlllCDJrTQ45F-z4yJELpPouseeOjDd0PfJYpeKv-9GQoeK1OhslriPi1Y09S83lpzToAkyM2RShXygsyKSE4IBg0WFI3q7Ta8mBG7vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۸ شهر از ۱۰ شهر گرم جهان در ایران؛ دهلران با ۵۲.۱ درجه سانتی‌گراد در صدر ایستاد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://telegram.me/akhbarefori/670862" target="_blank">📅 10:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670860">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae914f0128.mp4?token=rr8GEXKxnkKwNDpyS2RX38WF5i6e83qObfwtip_m59IhsLmdmU9tDFdBNBirRchxMiTpT_LVkAsRigPXwe4HyjKX9ZcB8yRJkHi6vf27vgL_j61mh8PZFDkPdBCehWek6BHBAH4qGn-qbHpoQ-evhIv92_19DKTH1lCdDFtF4qSfMbhexCfnFKs5zVn3CUH3WiRr5oV-Z1qMmMtB5J5nk7AIlEgB4jYznoe_0LIf6089bEodzs5hpJKJrySe3Pcdxy85EP1RnOZA3JeajqWMIkqaHdwnXxWLUbrHJM5hq42leyvoaavda2H7ttUKRjX6jmz_O3Am-9L6KfJncnOkZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae914f0128.mp4?token=rr8GEXKxnkKwNDpyS2RX38WF5i6e83qObfwtip_m59IhsLmdmU9tDFdBNBirRchxMiTpT_LVkAsRigPXwe4HyjKX9ZcB8yRJkHi6vf27vgL_j61mh8PZFDkPdBCehWek6BHBAH4qGn-qbHpoQ-evhIv92_19DKTH1lCdDFtF4qSfMbhexCfnFKs5zVn3CUH3WiRr5oV-Z1qMmMtB5J5nk7AIlEgB4jYznoe_0LIf6089bEodzs5hpJKJrySe3Pcdxy85EP1RnOZA3JeajqWMIkqaHdwnXxWLUbrHJM5hq42leyvoaavda2H7ttUKRjX6jmz_O3Am-9L6KfJncnOkZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش یامال به تصویر نوزادی‌اش در آغوش مسی: فکر می‌کنم کمی بزرگ شدم! لئو هم همینطور، امیدوارم در فینال جام‌جهانی با مسی روبرو شوم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://telegram.me/akhbarefori/670860" target="_blank">📅 10:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670856">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGmy3-bxUs37GU-Rn0XhYOwdsds_rGWtT9u8vV7xLNwwTAQjtSrxuiGjxTM7RC6vPjXJxhW4HO0ZqiDuB4MJGbXKSKzxO8zWJRA6s--QJv4Z-Uj27PVcE9Tj-DOaAxUWl6w2NbzLza6DaQ-aoF0M09qFnWa9F9_9AThrRBsdu7Cp_3oRii-8odzIVfxioUgT2y_1TkmaExa2uS8bKwAitcYJa-MoOBe80TUTvMtxj0QmKUIurbE2eMHRtCaWMq25MG5Emih0Bb1i_vvH2sm0RxqyeqFsffbaVY7U7FghnUEDxwcZIt_OB-JbfU6rIneg0wDhbwLLa70VpJKd1AX20w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۰ نیمه‌نهایی اخیر جام جهانی در یک قاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://telegram.me/akhbarefori/670856" target="_blank">📅 10:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670852">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kYi4qXD3QXX29JhYBAMl4Dq4gDFstr45i-QKnBXm9yKfsZNy1aXxN614H7cRskYd0Y_iWmyOJMJ7tv_ntTlErZ-_9aDVBy8t4FNvA8hKQQUxJvco76S1GGcwHWiIdGMEir6VuruYZKyAbmWJUA1ZlNA2dcG2iHiFs20CTDMDt1n34-l2cn1P23Mehzm13_ZWQYT1lZEqWp_MO5adu9OAWwQue8BHHYlWA89Qo7qEoiK5cEW1bcG0QCvJSJKDcMW3x8DX2uZdKkYAvUcwJch6kgqKmkY_-K0Iwa-PLVl6YoDuRDoEzO0rK3FE_TXEJh7xGLoqgb85TySygnBjTA8BEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3CcW0_pqvrLxL6HK1frGib0EAo2xmdl1Fk9cm2eOd_5XxlsrooXRCYFDW81HlqvjA927n9ckhVgbhUFBapbK5nd2CzYRv6PK_EkfgxsPLgPdWOLt5FeAvtpVcWlVUhHZYdHNLpNAS6yAoThE3LhgH5lOOmXxgv4V3hQxJXbUKbRcrPHMtwRqXIklLSuideZbwHsP_26N9tqdoeRHxduCpEXbozcvIQjUeQwpq1WJYwmYBeqxC7a3ok7JAvtMPrb45GP2gFzhobLiTy6q-J8nGPrRi6aqx9s5ZeJawPhFvhyrIuB11aykwiVJtZBnL0Idqb1PbvsWkc3yXkODPQmuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LzfxjZyXlpvXWusLS_HURPk_Me4xbZFDFHiC5ns8TFngsWuGeBvBTAdov8Fc31Us796cnl6c8KcFwo-TurYsCNi7-Hw0aMDaFYGx_zC90SaWvQr4PDFkxRQDS_CkCqIOulzlVlxZaUfZqLD70FmubFz54YpKJ4UF2B9EeZ8tbIaxKHzO6GH7_c6As7m7k5mmSDe3e81jqtsBqhr3h3mdIjkennKjwwObAPF-ef11zw6F_jeaIg1g15oPy9AQBwNYrtIolpF0H0xu9Stt3k-ElYnKXVt6lORrIYKo1q709adi19SVMwvj3yxurrSAgqKsSDIzFK5Ot2LCBGBXym98tQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مرغ رو به این روش درست کن
😁
مواد لازم:
🔹
ران مرغ: ۴عدد
🔹
رب گوجه: ۲قاشق غذاخوری
🔹
فلفل دلمه ای: ۱عدد
🔹
پیاز: ۱ عدد #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://telegram.me/akhbarefori/670852" target="_blank">📅 10:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670851">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDNdQMHefcEX4P5wss5rXyAPEWbzIdpsvIC27GZ-1glmNAwW_3MC5coatZoHy_Fzpcz65P9KoV1vaonjUGsdigWNN7TDnjyeOvoAmKU7W7XgsXrb1OYBKITWbxL6L13CCPd6HWNP1HBGZVQRBge7BkdEg1Cr6VgKj-htbYCm1_QimlTDI8VUDUFdD-Quk4HXDqOjy_hXBUHoWghF_ZezM5ETUPiGXefWwrm4iBpPbRT5sor1OoK4ifART8di3irabh8rMNXrM4l5Bw2kJ-l9SKWEMADNBxO0cWziT6IH21QBtwSv0Jua9Qn8UGkOCp2-fycIM4j9YJc2Z7qMxvuNew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چطور باید به توییت‌ها و اظهارات تند ترامپ پاسخ داد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://telegram.me/akhbarefori/670851" target="_blank">📅 09:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670850">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‌
♦️
جزئیات حملهٔ دیشب آمریکا به بوشهر و چغادک
فرماندار بوشهر:
🔹
در ادامهٔ نقض تفاهم از سوی دشمن آمریکایی، دیشب در ۳ نوبت، ۲ نقطه در این شهرستان هدف حمله قرار گرفت؛ براساس ارزیابی‌های اولیه، این حوادث تاکنون هیچ‌گونه آسیب جانی یا مجروحی نداشته است.
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://telegram.me/akhbarefori/670850" target="_blank">📅 09:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670849">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/habPmGo8xTK_WR5xhBWYCZ5gIl_JnWl59WcZpeiRMkOhoHKHWvDKpysThTwh_DsQ3FMKPuLyUaYKcm1U7Y3c-9_PiMEFvYrvJOg1F12P6pjuteUZsSPbMZxGu17h1EDWVdRDNXR5GQLamwoVUn57q8kqakPjv41vnePWeTJanJorO--TqPn_BXwni8z5r9IM9fiJlwcZh1DW6iYslHrgPazS03EsDHq5tyS8FqsPMAJMVeOW6BEv9Q4YXmbj73eibW3bDaGteLTFYq6PM1YPhM5sptnr_yierhMJxOpQCWCj0M32WWa2baOKbslN0asILFy_c2j9I1J22c--71ODyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدیرعامل سایپا: مجوز افزایش قیمت نگرفته‌ایم
🔹
در صورت صدور مجوز افزایش قیمت، موضوع از طریق سامانه کدال به اطلاع خواهد رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://telegram.me/akhbarefori/670849" target="_blank">📅 09:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670842">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d31aa2ae1.mp4?token=lg3KirunHL3ZHIs03MA4dOs0qvy19xW1O8i5awO3f1D2UCVwW5suOn3i1XbRN9KsequHhc1ytger2SaW4agpkJvwKZuxRf_D_HZ3fQVFA8TOO5PG1_8EVBdcjfHDy-bP39xRKE3-ZbZS1hHpwKh7gc_TuCdy__C8DStD_yvLRkT6KAypHHwFLrP02wrArPsRx0De9Naz_su9e1MCkkno_90EfMNLsD7IbORKScVrAPn7cUXLU_ARJ7MGSuIOpYps_sg5ir5iQ-_mCxPS8c_LuwEvAFZFOPLJFIbSO0HpETmhqL1eY41IZcRVtqOuNlPwmTJgZ6_aNF90RRQzp8ePxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d31aa2ae1.mp4?token=lg3KirunHL3ZHIs03MA4dOs0qvy19xW1O8i5awO3f1D2UCVwW5suOn3i1XbRN9KsequHhc1ytger2SaW4agpkJvwKZuxRf_D_HZ3fQVFA8TOO5PG1_8EVBdcjfHDy-bP39xRKE3-ZbZS1hHpwKh7gc_TuCdy__C8DStD_yvLRkT6KAypHHwFLrP02wrArPsRx0De9Naz_su9e1MCkkno_90EfMNLsD7IbORKScVrAPn7cUXLU_ARJ7MGSuIOpYps_sg5ir5iQ-_mCxPS8c_LuwEvAFZFOPLJFIbSO0HpETmhqL1eY41IZcRVtqOuNlPwmTJgZ6_aNF90RRQzp8ePxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کنایه تند محمدعلی ابطحی به مدیران عالی کشور!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://telegram.me/akhbarefori/670842" target="_blank">📅 09:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670841">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1XT9U7DMIZlq5Apk6ItVXrUS8fxqAaXu8p_UWv4_7GEfVJPnHnAGCmIS_0GyU8MLZfqvcFDaSs87wjQsDbA-_v-uGQBHP7NVHLobB7fKEU1hUFf4gFXRfnbEQTo4seH3F6yXktqbW4emfH-d2wIDWOSe0_FSyVLlQzzxW30XZxl62lIOFFcJNcPEUsNLrVEm25s7GUIgbY2NyI81R4C3rH7ykKYLCv4qBiqF1wn1NI5mWUzUfhOZOf8e9tKJAbEEGP4NH5fxfwuuS9WMQpV27LsQ-jgIKJ2MTU2AYGcl9rCMZDtKe3mNyz-Z1O2L66cfpr6lAuwPIjxjh4sHNm8SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاتز: تماشای ویرانی غزه، حس خوبی دارد
🔹
وزیر جنگ رژیم صهیونیستی در جریان بازدید از شمال نوار غزه، با افتخار درباره ویرانی‌های به بار آمده با جنایات این رژیم صحبت کرد و آن را «نتیجه سیاستی حساب‌شده» خواند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://telegram.me/akhbarefori/670841" target="_blank">📅 09:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670839">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efb736c682.mp4?token=WW7m8A1bA6IBHKB2BHjC63ClJRK9r0i8lbIfm7VgzenV4AArhrHZvF2sw9wTaBTfVNHxif0a5GY-cJHEF-15XED9sz02m_U1Wk2zxkUFsYCsinJffDaBgqkKfsZFXp9HHY4DHequY0MFFCW5Lwp31uwZGKtXZHpiiFdYjcsIECWv-J76KBUy2CH0FzLXFyzeA_QDZYuSq88zRa78WRqduroD2OYhuGTwKUTvu3rKWcK7CPlymHnv-wMFVse59j5gyoafs6dGdkTnVNgd75r0XVLLLXht2Z9dzb6HL7AeQhNx8ge_WS_U8mBhSQ0r3IuhKlCCbZ_P3tDT4xfsLGw3fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efb736c682.mp4?token=WW7m8A1bA6IBHKB2BHjC63ClJRK9r0i8lbIfm7VgzenV4AArhrHZvF2sw9wTaBTfVNHxif0a5GY-cJHEF-15XED9sz02m_U1Wk2zxkUFsYCsinJffDaBgqkKfsZFXp9HHY4DHequY0MFFCW5Lwp31uwZGKtXZHpiiFdYjcsIECWv-J76KBUy2CH0FzLXFyzeA_QDZYuSq88zRa78WRqduroD2OYhuGTwKUTvu3rKWcK7CPlymHnv-wMFVse59j5gyoafs6dGdkTnVNgd75r0XVLLLXht2Z9dzb6HL7AeQhNx8ge_WS_U8mBhSQ0r3IuhKlCCbZ_P3tDT4xfsLGw3fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سختی یافتن آب در غزه؛ سفری خطرناک میان آوار
🔹
در غزه، دسترسی به آب آشامیدنی به سفری دشوار و خطرناک در میان آوارهای ناشی از بمباران تبدیل شده است. مردم مجبورند برای یافتن منابع آب، مسیرهای پرخطر را طی کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://telegram.me/akhbarefori/670839" target="_blank">📅 08:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670838">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgVghSZR1ISxC5krJqWB3-6IxSdOuYsNlDpE8ZKTCIHYPNeiMRsSInthJ1e1bd8UltJAWCRBa4sjbJsIR_LQPXv4LaRCTRZGSx3Ck87_mWmcd7wyl1e_UFW5CKRJkJ-7TQz8vBH4w2IC021w_tkV_NXZaD_1c7IOiKmUo8I5x_-314JRtcuEzbQoyQGizf2Z2UCX0uwmhb4E6edkMPJEgh2qw0vA7V6cbOEm-P01XcNYZePhTyk9PnL-eTviR0M3hgqjmZrXpea3IG2N6Nw_xA_za7uQ869sUOLd4ipV8ELQ4E_gdiOlRtF1yDKaFdA7JOTE6APS9J72wDuxnzVSiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فوری|نشست علنی مجلس شامگاه دوشنبه ۲۲ تیر ماه با حضور ۲۵۹ نفر از نمایندگان در بهارستان برگزار شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://telegram.me/akhbarefori/670838" target="_blank">📅 08:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670835">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOgvWzaa39qumhgKKKcLZEw7W0Czd8Vw3AIt4eSDHx_-AB5que1hwwq8XeiLCYPUdq0A6q_BmDsD01ikcGNMqAEgvaOjN4-UeJfBQPp4Tctxv1tbMuS_hnSqT2a3fy4zbujiToV62viUQs_1HONPMOTBL27adVZ5eXfEF1ZV8EixC3TDxFNHcU6k8z5xSMlwbmn8-jvqLFfFQ2CfWcU57Eer0oQNiH8DtIDRZUwfXQJqrljOLlqMkFZOKteGu97dppk0YWgEJzvaRAYjR78tdCh792sYSS-CIcaPYbZk8KLaq5Swt6MTMvQlpMtTYvq9-XBdg8kP2wRuztVhwiD1tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدال تیم‌های ملی فرانسه و اسپانیا؛ ساعت ۲۲:۳۰ امشب
🔹
در مرحله نیمه‌نهایی فوتبال جام جهانی ۲۰۲۶ تیم‌های ملی فرانسه و اسپانیا از ساعت ۲۲:۳۰ امشب به مصاف هم خواهند رفت.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://telegram.me/akhbarefori/670835" target="_blank">📅 08:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670834">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
جزییات حمله دشمن آمریکایی به امیدیه
معاون امنیتی استانداری خوزستان:
🔹
در ساعت ۲ و ۱۰ دقیقه بامداد امروز سه شنبه ۲۳ تیرماه نقاطی در شهرستان امیدیه مورد تهاجم و اصابت پرتابه‌های دشمن آمریکایی قرار گرفت.
🔹
تاکنون ۴ نفر مجروح شده‌اند. / ایسنا
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://telegram.me/akhbarefori/670834" target="_blank">📅 08:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670832">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
پیام مهم سپاه به مردم اردن/ تاسیسات مهم و محل استقرار دشمن آمریکایی در یک پایگاه هوایی در اردن هدف موشک های بالستیک قرار گرفت
روابط عمومی سپاه:
🔹
ملت شریف و مسلمان اردن؛
سحرگاه امروز رزمندگان اسلام در مرحله سوم موج دوم عملیات نصر۲ بارمز یالثارات الحسین (ع)، تاسیسات مهم و محل استقرار دشمن آمریکایی در یک پایگاه هوایی تحت اشغال ارتش کودک کش آمریکا در خاک شما را که از آن برای حمله به ما استفاده شده بود، هدف موشک های بالستیک قرار دادند و جنایتکاران آمریکایی را به سزای عملشان رساندند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://telegram.me/akhbarefori/670832" target="_blank">📅 08:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670831">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50698e670a.mp4?token=NgNzLsR74n5x2O-hvQ3k2Js0XJV6fRCF85lZCTGvUiODTuGxix2tB56pTTMdWzZSjMIv-vG6IzbQtfQricoLUBJjLoEuwLb5fSA9lHmJbhXUA-jaNaomeS7sXPvASH7vY4fv2o4UHK2lF_BNqFrSwL9GHUtOoLv5j7RLYrvHrkanT2Yh9KXXTCJfbMUL8JS45ULa_9sLWlzkUx-EwxgOMehPjtmbFq6pEi5RvNCvOa9spvpbU-eHUFKoJ_ziXGDclXzr5SovdmSZNik1DDXIm2hAHBIG7NXKsVcEe6ZJfelWYr8Wka5UvrCCaTBJISybojrfpeFY26A21psDuzWLRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50698e670a.mp4?token=NgNzLsR74n5x2O-hvQ3k2Js0XJV6fRCF85lZCTGvUiODTuGxix2tB56pTTMdWzZSjMIv-vG6IzbQtfQricoLUBJjLoEuwLb5fSA9lHmJbhXUA-jaNaomeS7sXPvASH7vY4fv2o4UHK2lF_BNqFrSwL9GHUtOoLv5j7RLYrvHrkanT2Yh9KXXTCJfbMUL8JS45ULa_9sLWlzkUx-EwxgOMehPjtmbFq6pEi5RvNCvOa9spvpbU-eHUFKoJ_ziXGDclXzr5SovdmSZNik1DDXIm2hAHBIG7NXKsVcEe6ZJfelWYr8Wka5UvrCCaTBJISybojrfpeFY26A21psDuzWLRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این ۶ تمرین، هم فرم بدنت بهتر میشه، هم احساس سبکی بیشتری می‌کنی
💪
#ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://telegram.me/akhbarefori/670831" target="_blank">📅 08:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670828">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کم‌کاری وزارت نیرو در خصوص کیفیت پایین و کمبود آب شرب در جنوب کشور
هاشم خنفری، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
کمبود و کیفیت پایین آب شرب در جنوب کشور، به‌ویژه خوزستان، به بحرانی جدی تبدیل شده و دستگاه‌های مسئول کم‌کاری کرده‌اند.
🔹
با وجود ظرفیت خلیج فارس، از تصفیه و استفاده از آب دریا برای تأمین آب شرب به‌صورت گسترده استفاده نشده است.
🔹
وزارت نیرو و آبفا باید برای بهبود کیفیت و تأمین پایدار آب شرب، اقدامات جدی انجام دهند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://telegram.me/akhbarefori/670828" target="_blank">📅 07:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670826">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIzEeiyb5GnLlT1aOOy-_bbl7d4dje3feSKkqa6NEp6a5diBchpCuT21ATO8pNfOaNirk3FVu7whOaBQ2NgOETqCvRlbBSDBA296BHooXISA3hniNe9kBlibkzONtQHaYoo5HyBdmHDvGrZHk-_j4y0bNJpNnjAW5tbG3I_Mv_icmSAmHE369vdVUSX0Ym__5KeMikHqBZwCigFUEvLIs1yo9P5-y4d6LHhy3H0v0a88mPog6OqWsFCCormE3k8dCsbZB3rWYkw5v1_BLSEfQ3cWpFecS8hIjXHKFRHX8nJ0dqJf8ZvQeaUK4jPs0d3gy_g96TKRbRSvMeOzVrJ3-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز سه‌شنبه
۲۳ تیر ماه
۲۹ محرم ‌۱۴۴۸
۱۴ جولای ۲۰۲۶
سه‌شنبه‌ها
#دعای_توسل
بخوانیم
⬅️
متن و صوت دعای توسل
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://telegram.me/akhbarefori/670826" target="_blank">📅 07:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670825">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
رادار پاتریوت، رادار کنترل هوایی ناوگان پنجم دریایی ارتش آمریکا و یک سامانه راداری اخطار اولیه c-ram منهدم شدند
روابط عمومی سپاه پاسداران:
🔹
ملت مجاهد و بیدار ایران اسلامی؛
رزمندگان غیرتمند نیروهای دریایی و هوافضای سپاه در مرحله دوم موج دوم عملیات نصر۲، با رمز یا لثارات الحسین علیه‌السلام، در پاسخ به شرارت های ارتش کودک کش آمریکا با حمله موشکی و پهپادی به ناوگان پنجم دریایی شیطان بزرگ در بحرین، مخازن سوخت آن ناوگان را به آتش کشیدند و رادار پاتریوت، رادار کنترل هوایی ناوگان و همچنین یک سامانه راداری اخطار اولیه c-ram را مورد اصابت قرار داده و منهدم نمودند.
🔹
در این مرحله مرکز کنترل و مانیتورینگ قایق‌های هدایت‌پذیر بدون سرنشین نیز به طور کامل نابود شد.
🔹
عملیات مقابله به مثل ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://telegram.me/akhbarefori/670825" target="_blank">📅 07:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670823">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee20b9c964.mp4?token=M0SPNwkQmRINzW1QLGfZA1WSYI1NOo8zgEPdclGSivgNSQfjv0ZACr0BdpPE4UG3HDKtbID-UeDFjsJjxr-fImioIS1AwBp8VNE9th-nB165hz4oNUWs5pijA_akDH8nGYL9HTXVL0a82VkNBr1rcLqjYK6V3x4y49qiaTK5E6kqMP9RVoDnpFRpM9Bplmja73y5tOv6HhtaZgHn7BeuxkM7uVT4OQRG0wvMYmGwAn3B7e4qWMEMXIbFXxI0c6UUaiFv_E5tLPjtcgoxVFiyPh6JELf1b2ybknbpRxDFeusmM5avml-QTqkK7o5i1OlsZ7sPLBgeLVMR_6_inEX2Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee20b9c964.mp4?token=M0SPNwkQmRINzW1QLGfZA1WSYI1NOo8zgEPdclGSivgNSQfjv0ZACr0BdpPE4UG3HDKtbID-UeDFjsJjxr-fImioIS1AwBp8VNE9th-nB165hz4oNUWs5pijA_akDH8nGYL9HTXVL0a82VkNBr1rcLqjYK6V3x4y49qiaTK5E6kqMP9RVoDnpFRpM9Bplmja73y5tOv6HhtaZgHn7BeuxkM7uVT4OQRG0wvMYmGwAn3B7e4qWMEMXIbFXxI0c6UUaiFv_E5tLPjtcgoxVFiyPh6JELf1b2ybknbpRxDFeusmM5avml-QTqkK7o5i1OlsZ7sPLBgeLVMR_6_inEX2Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرواز گسترده هواپیماها و بالگردها بر فراز بیروت، پایتخت لبنان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://telegram.me/akhbarefori/670823" target="_blank">📅 06:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670822">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
انفجار این بار در کویت
🔹
منابع خبری از شنیده شدن صدای انفجار در پایگاه اشغالگران آریک در کویت گزارش می دهند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 63K · <a href="https://telegram.me/akhbarefori/670822" target="_blank">📅 06:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670821">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
سنتکام مدعی پایان موجی از تجاوزات به ایران شد
ارتش آمریکا در بیانیه‌ای ادعا کرد:
🔹
«در طول این ماموریت پنج ساعته، نیروهای آمریکایی به اهداف نظامی در سراسر ایران از جمله بوشهر، چابهار، جاسک، کنارک، ابوموسی و بندرعباس حمله کردند تا توانایی ایران در حمله به کشتی‌های تجاری را بیش از پیش تضعیف کنند».
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62K · <a href="https://telegram.me/akhbarefori/670821" target="_blank">📅 06:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670820">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
انفجار این بار در کویت
🔹
منابع خبری از شنیده شدن صدای انفجار در پایگاه اشغالگران آریک در کویت گزارش می دهند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62K · <a href="https://telegram.me/akhbarefori/670820" target="_blank">📅 05:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670819">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
وزارت کشور بحرین: آژیر خطر برای دومین بار در سراسر کشور به صدا درآمد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60K · <a href="https://telegram.me/akhbarefori/670819" target="_blank">📅 05:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670818">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGtTiUPkmDxcRAxlhHSQATYprogO2vYF0GX1sAgerTAoEMVEMyYeWhFG0qL4xZ3LQ0Py9JaIMAXoC8wzgXI3Z5uMYLQk_RyXVawMIFH0rdmk1vZttcgflCkEe7pW06t1pN2Jq_AAG1vSAhm_SKCXvsjZ8MiO7NY7VEuEjvwoT6eN0HeP5tgXPRmIyX9VRGMV7cRVHD9NjUMpqjxtl6lcJ6xY9xqZXhdbZlt-GN1x4oHzCs0IX_si2WcFB3KIR9oOQ6B35h_cv3yblKAh0p6_Y9CUjejAu7WqVpCFqk8LCrA8y0WfVMg1_ZIV1h5hTXuvafSzj-ozBQZfW7vSueT2cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پوستر فیفا به بهانه شروع مرحله نیمه‌نهایی جام جهانی ۲۰۲۶ از امشب
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://telegram.me/akhbarefori/670818" target="_blank">📅 05:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670817">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
رسانه‌های عربی: در پی اصابت موج دیگری از موشک‌های ایرانی به پایگاه‌های آمریکا در بحرین، صداهای انفجار مهیبی به گوش می‌رسد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://telegram.me/akhbarefori/670817" target="_blank">📅 05:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670816">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
روابط عمومی سپاه پاسداران انقلاب اسلامی: دو فروند سوپر نفت کش متخلف فریب خورده، مورد اصابت واقع شدند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://telegram.me/akhbarefori/670816" target="_blank">📅 05:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670815">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
نماینده مجلس: انتقام رهبر شهید، ضرورتی انکار ناپذیر است
حبیب قاسمی، نماینده مجلس:
🔹
رژیم صهیونیستی با همدستی آمریکا سه جنگ را طی یک سال بر ایران تحمیل کرد که منجر به شهادت سرمایه‌های بزرگی مانند فرماندهان، دانشمندان هسته‌ای و مردم بی‌گناه شد و این خسارت‌ها نباید بدون پاسخ باقی بمانند.
🔹
ارزش خون رهبر شهید به‌قدری والاست که اگر تمام دارایی دشمنان را در یک کفه ترازو و خاک پای ایشان را در کفه دیگر بگذاریم، کفه خاک پای رهبر سنگین‌تر خواهد بود، اما انتقام یک درس مکتبی و ضرورتی انکارناپذیر است.
🔹
فرمایش امروز رهبر معظم انقلاب مبنی بر خونخواهی رهبر شهید پیامی قاطع به دشمنان بود که هزینه شهادت این رهبر عظیم‌الشأن با هیچ معیاری قابل جبران نیست و جبهه مقاومت با اتحاد بیشتر پاسخ خواهد داد.
🔹
دشمن امروز از درون احساس لرزه و ناامنی می‌کند، ترسی که فراتر از دوران حیات رهبر شهید است و تا جایی پیش خواهد رفت که حتی قدرت تصمیم‌گیری درست را از آن‌ها خواهد گرفت، چرا که وجدان‌های بیدار جهان نیز در صف خونخواهان قرار گرفته‌اند.
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://telegram.me/akhbarefori/670815" target="_blank">📅 05:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670814">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در ابوظبی امارات
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://telegram.me/akhbarefori/670814" target="_blank">📅 05:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670813">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
آرزوی خوک نجس: آمریکا تنگه هرمز را کنترل می‌کند
رئیس جمهور آمریکا بامداد سه‌شنبه در مصاحبه با شبکه «نیوزمکس» مدعی شد:
🔹
«ایران ممکن است دردسر ایجاد کند و کارهای نامناسبی انجام دهد، اما ما اوضاع را تحت کنترل داریم».
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://telegram.me/akhbarefori/670813" target="_blank">📅 04:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670811">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
روابط عمومی سپاه پاسداران انقلاب اسلامی: دو فروند سوپر نفت کش متخلف فریب خورده، مورد اصابت واقع شدند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://telegram.me/akhbarefori/670811" target="_blank">📅 04:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670810">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
گزارش‌ها از حمله موشکی به پایگاه اشغالگران آمریکا در اردن
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://telegram.me/akhbarefori/670810" target="_blank">📅 04:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670809">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
گزارش‌ها از حمله موشکی به پایگاه اشغالگران آمریکا در اردن
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59K · <a href="https://telegram.me/akhbarefori/670809" target="_blank">📅 04:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670808">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBdGjEha3yfNtoFGLWFkxlCEgdHGz0xd8LVAstSXSRtzKvEsINYRzDQe_k4KtepQtZ1uMep75xMDhK22Pz_IPg4r2vVMYHeL3B93mCE_iCvIQWyDAEIItly3-tHgk-Bg7TZK_mN-36DqOPmlJuyYnp4GSzFaBU3sq99KjPGxpviqOmmbw_sruEUkQLysTZc49Gn8mLvisH87AMdrQnF4ByZZbrQulMis1TxllxPA15eSS_1Qcp1VFHTqFN-fTShWtmdbtS-agGAnivQcvfyPvWlMAJN5N2dOkxl_R5XOu1iEUrgi1uvhvpuRyIOOmiEL396uJdBAeGWOIBAy_eaAYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت از ۸۳ دلار عبور می‌کند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://telegram.me/akhbarefori/670808" target="_blank">📅 04:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670807">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a74326eb78.mp4?token=j14hGT3jAVI9EceTgRFQs3uGUdf3Nctz1YuD9k4n7sVneQ63dKEpDSXu_sH5AzDoRW9KZMLEnYi7eQ7GGsHUA1mMT3upps1N8BSZVudTs7715J71G72o6oIuT8kUDUC0WFKmKTu9g_Z10-QtELth8LFqY9XjqSvFRzp3SzWZnHmCYRu4zgIfZrpen96aJhCu0LwyRHdnYTYlQW3WscyBvaHteDULGzrLpe286wHyZf4uv3MjxCqESZAQzNrmlyyIxha7M0NgyER36bR2Ou0AKkDOCQnQ4LYpt1Sa2oDaKLgzOvJUkLXXLbiOlcrbmWPwwjIbk254sGgFPS9X_DEhEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a74326eb78.mp4?token=j14hGT3jAVI9EceTgRFQs3uGUdf3Nctz1YuD9k4n7sVneQ63dKEpDSXu_sH5AzDoRW9KZMLEnYi7eQ7GGsHUA1mMT3upps1N8BSZVudTs7715J71G72o6oIuT8kUDUC0WFKmKTu9g_Z10-QtELth8LFqY9XjqSvFRzp3SzWZnHmCYRu4zgIfZrpen96aJhCu0LwyRHdnYTYlQW3WscyBvaHteDULGzrLpe286wHyZf4uv3MjxCqESZAQzNrmlyyIxha7M0NgyER36bR2Ou0AKkDOCQnQ4LYpt1Sa2oDaKLgzOvJUkLXXLbiOlcrbmWPwwjIbk254sGgFPS9X_DEhEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخی منابع از به صدا در آمدن آژير هشدار در سفارت آمریکا در بغداد خبر می دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://telegram.me/akhbarefori/670807" target="_blank">📅 04:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670806">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
آمریکا خدمات کنسولی خود را در امارات به حالت تعلیق درآورد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://telegram.me/akhbarefori/670806" target="_blank">📅 03:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670805">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
گزارش‌ها از وقوع انفجارهای جدید در بحرین
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://telegram.me/akhbarefori/670805" target="_blank">📅 03:56 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn5.telesco.pe/file/lPPj3Uz1NJAeVo7XfA9_dQ324LgY4skblKOo0iZHnkptENAGm9d90488XHip2pe6ZYtTSYVwO3IDZ4V_DwuR8NqrokR_Aug7WD-9lItvseMj42ahsSfhmQDEFnu7n8YIpxBJ-U7_GQj66FmBXMsrEgBPGqLQyuv1V3JxzmGZA6WHuGDYh3AcJW6gRnzzdToXnx0XOh3xk0EvDqOWlpgqDoTSG3SlTyLCn6GK32w53xBxdUzG42aPmEjIdIdD2TeALBOcRYKzBIN_tnS92CQirfuThXcZy9QZ2xULJjaZx-ILIkpY2jNMz0VK1HJ-Ff980GBezI7WabqgB0TXm-tJEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 531K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 15:26:42</div>
<hr>

<div class="tg-post" id="msg-101887">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ji2279qBP-I9MZkztx1KUyx7K4KEnYMZBFbAZkm6s6LNLF3R25qvWRnEux3RL3ucWTMpUHgePkn9GOj302aEwKJwzUtG9aEtnDIMciGWlPzNcdidpEt4Cr8r0h5u4dGwDLpL-cWCSVcpxuboQoIHunKxJM8AXOEE2Jx_Ukah9U6I3nZa3SX9kVWqmFlPYjdEzkpYvXtEJmnjmADy50_rudIQQTlC2KU9hvX88tDwgakU4giBXALiLI_KYCicFlibxazbVigx1HWLn0gGam9XBzJxn_PQObkQG6sJ3mVtGpzCRw1Ap4CtK88goeKXXZWf9HxGdUZh0bmQuomHMnk-Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
هزینه تیم‌های پرمیرلیگ تا اینجای نقل‌وانتقالات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/Futball180TV/101887" target="_blank">📅 15:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101886">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPlRT1kvLqa-pPtHy__ReRnyyZXeAXy9ZVYZrY1GIBA0XLQeFXp8nizYGui3VHfAL1AJqEdAuK3pab0Gc7QCYUt3JWuECPaKFJJ3LWPEHABggHcMhE8nszk6ca_W3Xlx7i9uZIyPcuFuqT2BDU9r0UqjJXmvBbb8SEmVyjnKRowRxDDDOovdTyZR1KwCcRMk016I_tez_YSN6am5hLUYUDQZk2ey8XsgwUvvfyrNkWBDu2egQnEiyYD9btaSn_KRpM2v-FHfWESnPh8WO87hNRo5_zVetE5g-YsgV3DFiPXuduSeFxj4qi1h-jB33_cjEYOEPphS9DOHRqcpZDp-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رودرا: اصلا بعید نیست که اندریک این تابستون رئال رو ترک کنه، این احتمال حالا جدیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/Futball180TV/101886" target="_blank">📅 15:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101885">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0iH2bFSPX28-XxwOrHFngUyKhDQPsLj0aoDUoF6srJvMw2q7wsdudpouy4cPUy99WqGP0r8frTp9C47Y3CigOEz8QAAuSMdXXvMFmpikpjWh-ruYtI4bky0OXHC3_sWU-CyFV_jcob4JzaziJHzpL_qprwf8k2dfT4G3U7TS8LQXzXVRsP5LJ_5dksNRg6TzeBg47OZCjABd5mLA9XYObcNU89r9uYxYKwcSDKikSTFQ3_SvhJt9PVsbWAdcy2hDQ-0l6gHCemW7PXTrwMzzm_lxc27_Vyw5-vy1AtO-diSq_CnvgsgxmpwGT2M0PKwGHjKdIOeBpKhBndZWoqlFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
سانتی اونا: رئال مادرید از شایعات مربوط به انتقال مایکل اولیسه در رسانه‌ها استفاده کرد، در حالی که به طور مخفیانه در حال مذاکره برای جذب یان دیومانده بود. حتی آن‌ها به طور پنهانی به مقر باشگاه لایپزیگ سفر کردند تا این انتقال را نهایی کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/Futball180TV/101885" target="_blank">📅 15:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101884">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f29886b9b.mp4?token=SmWbuP02jwa9yhTFtchL7YM0WvGFOKNgNCNVqhL_HCvis1frqi3ckZSdxR4d-NUCLt7GVAbZptr3b8zz1X4Uzcq6pPBCAxlJRtzOq-L0IGtjqtUQXBcMnqo1EGdXDL_s6ITiAsObbJNN02j8ePvVBJul2NCYpC2z4wonfTxQiKVBad-b5aZl7n3qExvhxLDe4J7eXMESWxiqjmwA_yZgwCtJEpGr4eLQWt3OP7LFziXm4xlz2z-rqi0hFAiy_oKHH566mUyVbitKGzK66d_3aAnIQrgXkKMjbnJ8k4EVW6gbitLZMapwhm-Gl-dj6O0aJEaMxISPoYaoY4ULVRCyxLs_IvXp9aOjnOz-VpHBiAw1j5kfE0fVr2ocoGE1c5khuKA50Kc0xFCUmhJ57yMpC4MMgpxkzEOgL7KcICMHrRTA4zejo7Qcl-P5YMTnyCFWq7xizObShVn8GAzn9cPPOkBZwnK7Oz7cfoP1XuWO6bgHN88hWdrg-08oJth_gMb35_5ex67WYh346CfdHEhoerrEABI7S2iV0JSitdhnt2Kj2O-nSfFA9Fl7EdzMY69PQOq21zcGPTaUWL2_DCiKF2JhXcHnkkFkRH7YQod1_VYfWYr6uGA1QjhbxarS1RZiDZ5Sza9BQ1leFrm2ui2tUESM7wyud5m9hv0I3UpDMX8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f29886b9b.mp4?token=SmWbuP02jwa9yhTFtchL7YM0WvGFOKNgNCNVqhL_HCvis1frqi3ckZSdxR4d-NUCLt7GVAbZptr3b8zz1X4Uzcq6pPBCAxlJRtzOq-L0IGtjqtUQXBcMnqo1EGdXDL_s6ITiAsObbJNN02j8ePvVBJul2NCYpC2z4wonfTxQiKVBad-b5aZl7n3qExvhxLDe4J7eXMESWxiqjmwA_yZgwCtJEpGr4eLQWt3OP7LFziXm4xlz2z-rqi0hFAiy_oKHH566mUyVbitKGzK66d_3aAnIQrgXkKMjbnJ8k4EVW6gbitLZMapwhm-Gl-dj6O0aJEaMxISPoYaoY4ULVRCyxLs_IvXp9aOjnOz-VpHBiAw1j5kfE0fVr2ocoGE1c5khuKA50Kc0xFCUmhJ57yMpC4MMgpxkzEOgL7KcICMHrRTA4zejo7Qcl-P5YMTnyCFWq7xizObShVn8GAzn9cPPOkBZwnK7Oz7cfoP1XuWO6bgHN88hWdrg-08oJth_gMb35_5ex67WYh346CfdHEhoerrEABI7S2iV0JSitdhnt2Kj2O-nSfFA9Fl7EdzMY69PQOq21zcGPTaUWL2_DCiKF2JhXcHnkkFkRH7YQod1_VYfWYr6uGA1QjhbxarS1RZiDZ5Sza9BQ1leFrm2ui2tUESM7wyud5m9hv0I3UpDMX8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
امروز تولد هالکه و به همین مناسبت یادی کنیم از یکی از ضربات سنگین و پشم ریزونش.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/Futball180TV/101884" target="_blank">📅 14:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101882">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRi1gNqt7fZKNfpP4_J9sgJz5PI7wb9LQfNjOK2IzLSEo71YeKa3yHk7jGRx_QU027vJ2Y3eHGUFt2x2vb-1scQttoMCDneK_EBMzYZ9VGn-VdMbjQJimBu7bAO-NQDlIAgG37X-IeJrurgqEsseE9p4CVgZB_TEwWNYwSqv2Q1N6wvXzoU2U0fcG44iHxZkxfWHWNZGl8N3JUJCeLUw8lDOEjDsdQm7utWTblmCeD9PPNEbNYPl_SWvt4FuZZqg11Ykxi1IChucb7p-Ss2klFM6lq4ZG7PiG6PlVsMVNpDPiRDFkynrjDGMgJIHfLJ1fHxOSQbOvG3bX7Sn3YVghA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6342fd750.mp4?token=M-ZA5WEOu22uaFlokNH0xZAnn6S0tOZvFKOzEV9LLL7XEw8K8QoqkBLpHcBAhfIyIU9XtQVRfKwXLyBm_cgwiDRCgFkUcK_EM5aE5wnST0la3BaXPaTEkW-bGF28heH_dCfrZsBAyUkaTkzGsHKyG5xUwiyqmax0qN-b2LeKTEL-1uRjkgUA9x6cHyuj77P7e7PXW7dmsvTGFLLdLqMcrBYskm12ylO3FCNt1zUNMHMH9YCo8SKqrj5s7wQiRq_N6Z9VjbDE6AE6204aj8IAB9mE9nK43K_LQw1EYF3WPHe5H0wP_r7VDRAmb41ALZ7mcCaXgE8_7kU-UJIgFQz42A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6342fd750.mp4?token=M-ZA5WEOu22uaFlokNH0xZAnn6S0tOZvFKOzEV9LLL7XEw8K8QoqkBLpHcBAhfIyIU9XtQVRfKwXLyBm_cgwiDRCgFkUcK_EM5aE5wnST0la3BaXPaTEkW-bGF28heH_dCfrZsBAyUkaTkzGsHKyG5xUwiyqmax0qN-b2LeKTEL-1uRjkgUA9x6cHyuj77P7e7PXW7dmsvTGFLLdLqMcrBYskm12ylO3FCNt1zUNMHMH9YCo8SKqrj5s7wQiRq_N6Z9VjbDE6AE6204aj8IAB9mE9nK43K_LQw1EYF3WPHe5H0wP_r7VDRAmb41ALZ7mcCaXgE8_7kU-UJIgFQz42A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
هِیبا ابوک همسر سابق شرف حکیمی:
وقتی سال ۲۰۲۰ با اشرف ازدواج کردم، عاشقش بودم اما او انگار به من شک داشت و فکر میکرد دارم به او خیانت میکنم. وقتی دیدم نمیشه رابطه رو نجات داد درخواست طلاق دادم اما اشرف اصلا ناراحت به نظر نمی‌رسید! بعدا فهمیدم چرا؛ او تمام دارایی‌هاش رو به نام مادرش کرده بود و چیزی به نام خودش نداشت. این یه حرکت حساب شده بود و واقعا شوکه شدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/Futball180TV/101882" target="_blank">📅 14:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101881">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/356f27159c.mp4?token=PZpOjPAK7SSQl0ZntKnVyKbf5aKxUwsxD6bMAuUaOdeupwrVy4ZQJx6JFX4ioaOg0qGPMBhkTWADFWt0CryEkjoJ571-3x_OVjUxYYNeBmi-KbfvIAIWnC_SdOZ4TabjBG5pVaaYAk0meZ8ZQc7PZvqoPEMGHvjeD0ot5z7q3jGhdJp85ZXeKB_IPosN2M71NZJp3cyDwB21h4ZkBrUtnX47Mdl1vTd5syeQX4-yD2R9sucRsqCLEq-dPm1nLg4QtNs_4cFJVZ4EgJal-u_qhMaEJuITDzVTWxf6ioudA6miRK2da35ifwqchoYhlcUbBfaDFbWuY-rRDbMtwCoSQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/356f27159c.mp4?token=PZpOjPAK7SSQl0ZntKnVyKbf5aKxUwsxD6bMAuUaOdeupwrVy4ZQJx6JFX4ioaOg0qGPMBhkTWADFWt0CryEkjoJ571-3x_OVjUxYYNeBmi-KbfvIAIWnC_SdOZ4TabjBG5pVaaYAk0meZ8ZQc7PZvqoPEMGHvjeD0ot5z7q3jGhdJp85ZXeKB_IPosN2M71NZJp3cyDwB21h4ZkBrUtnX47Mdl1vTd5syeQX4-yD2R9sucRsqCLEq-dPm1nLg4QtNs_4cFJVZ4EgJal-u_qhMaEJuITDzVTWxf6ioudA6miRK2da35ifwqchoYhlcUbBfaDFbWuY-rRDbMtwCoSQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هالند لاشی تو مراسم عروسی دوناروما هم نتونست جلوی خودشو بگیره و مهمان‌ها رو وادار کرد «حرکت پاروی وایکینگی» رو انجام بدن.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/Futball180TV/101881" target="_blank">📅 14:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101880">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBNe8E5lPk_VZ3dWsi05q45E2sp5n8ea_HthLr9vmWZfEQd1WtsY14Acan0axWvJGcfVJFWvG61Pc2GmPgE-f-XpgS3ta-uX5CkbodjNsf7zYMg4zIdil2Vh7f6ww6uWGGq4C-8bUcBOS-kAPtrxiOjc6Bg7Nfnfdhtl8FS63vWfD_2MJ5lNIQDK33BkRkZSLdpRbrQ0yPzvHslyWVPmjKTKEwZ6vUbFS4qxTcLmyu7Fsq05hR1NeeVhIVFJiOkTK2q8OlGFAEZ4ScTcQCmpf9VK212e1239oLe5zQc6bx113FW-l6Q8CQa1RKLCxIDTo_s5efmFjOqtRnoCY4AWBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خط‌حمله نیست که ماشالا فلیک رفته تیم دوومیدانی برا خط‌حمله ش جمع کرده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/101880" target="_blank">📅 14:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101879">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ff0c27865.mp4?token=vbJwYCxzGGfGsueE__bZ1Y6WPbRo0qdwXiICv6h0Vl1tD6AqQUOaK1egT5-MVf4JgW3hjOj2NiKOH3ieMbmS-CRBqCW2EfCj3ObJ_ZruY3zWLN8RZyfx_O4GPIVPqiWxGaYxpzZLpJb615GwfjC4D06bw_TwoABmw9Nl4ZzCKgMpr0qs55Ht5orfV51Ev7Qj9lSn-P2oFKcJ6Yk2rZHBRP7d5jffbbBAtXv4j6Gt9uhTmF2AQgty88XTMtCQ_6Aji4iM_JxVKILqt1eKPgXTIhSrqE-2M-PHY6UUSn4aCW6oZ35BXhIJD9ybY_zB747ejyaQ-tsR3T5_9tV80naqSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ff0c27865.mp4?token=vbJwYCxzGGfGsueE__bZ1Y6WPbRo0qdwXiICv6h0Vl1tD6AqQUOaK1egT5-MVf4JgW3hjOj2NiKOH3ieMbmS-CRBqCW2EfCj3ObJ_ZruY3zWLN8RZyfx_O4GPIVPqiWxGaYxpzZLpJb615GwfjC4D06bw_TwoABmw9Nl4ZzCKgMpr0qs55Ht5orfV51Ev7Qj9lSn-P2oFKcJ6Yk2rZHBRP7d5jffbbBAtXv4j6Gt9uhTmF2AQgty88XTMtCQ_6Aji4iM_JxVKILqt1eKPgXTIhSrqE-2M-PHY6UUSn4aCW6oZ35BXhIJD9ybY_zB747ejyaQ-tsR3T5_9tV80naqSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
صدایی که این چند روز تو ذهنمون پلی میشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/101879" target="_blank">📅 13:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101878">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qm_P9ZEBOMs9wKsN1vFbwxjRrLffWfgnbY_d-1sBmuBGYXJG00gneeHJmK99Qzx6pTm0b0rufodh8IDVzhfpv9aL5hiVhgggyn6OKEQ0lzpVG2L8kVayagwSdlR2bDyklojavxME0hQvz3MzuvIsm6Fv8ZqL8la_EbZtCAaeGhTbDx_VApuGJDXr3a-wWsCjiRIs1Ai3devRIezxuuLtn_ytdO0CKwy3WiHATF-09mqznW08ruPAiZbCDIjTWFEpJZIo8H4Lfkp_cVUCuXUCJvnGfUdjhWwHj8I3zbpLZivTJ71rCJM9oaCShZ7et0boA8ipN0wYmmQ2BsncXR38xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🇪🇸
ترکیب‌احتمالی فصل‌آینده بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/101878" target="_blank">📅 13:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101877">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc2d82d4a6.mp4?token=EjBmTNFbvbrhub_X_2qk-GkWOwSnQDyOM-yp-eiDfpRnAUCt2LIRpsV9SLi3n7zq0P3H4uf2GhC3P8KsM9mHS5g458FtC7T0_8W-q_60f3YX0ZcM8PeXXGbdInLB1eK2NG6lZvVl3sFwKvAzq0A9BDBQM9RGjHjPQaGrz2L-FVY4bmhdge_E9YUGDXQ6sTDqJMc-cb_h0PphguUJ5E85TuAtgX-T3gyWsWLqH72GX0itrIK5gvhXgD9zG6m6dTGEO2jYG-YRewTDujymH-CslXmjz6VbV9Y1xeFgs8ITwaLUBC5hxfRBYnCV0UNogXEMqb8RGxvO0LLZaisOLABcmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc2d82d4a6.mp4?token=EjBmTNFbvbrhub_X_2qk-GkWOwSnQDyOM-yp-eiDfpRnAUCt2LIRpsV9SLi3n7zq0P3H4uf2GhC3P8KsM9mHS5g458FtC7T0_8W-q_60f3YX0ZcM8PeXXGbdInLB1eK2NG6lZvVl3sFwKvAzq0A9BDBQM9RGjHjPQaGrz2L-FVY4bmhdge_E9YUGDXQ6sTDqJMc-cb_h0PphguUJ5E85TuAtgX-T3gyWsWLqH72GX0itrIK5gvhXgD9zG6m6dTGEO2jYG-YRewTDujymH-CslXmjz6VbV9Y1xeFgs8ITwaLUBC5hxfRBYnCV0UNogXEMqb8RGxvO0LLZaisOLABcmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
مرور دودهه تاریخی برای فوتبال اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/101877" target="_blank">📅 13:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101876">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/705177dcef.mp4?token=Qg00_XwKwtUZ0pGuuw_1uM5q5zreHyt62k-6KIHUdR3lup5mQMz6rp5cSyIjKLnGYO8STlF2ulXi0kw4lX3_a2_1ThauxOtNQpIzh7W9h_sp6SdU_2svz5y_i5gCOQeX9QoRVkTZap9V67V6rAqda7b5SWV0dqNgRTuLj-X56V6LeTm9TjQrMyj-27mc_ZdS6aD3AVDrfbrvJbvAHr6e7mOco-p_Q5HneNsIsAavfY4uj8NHzUw4CtxR-9bomlw_wEEii4gbrCuXRIWDjZsXReMBfOawvI14VKKGwWcYojUp_P93sKyOW5t-6uO2RZOiVtupJQaf5FzetApo8OgpBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/705177dcef.mp4?token=Qg00_XwKwtUZ0pGuuw_1uM5q5zreHyt62k-6KIHUdR3lup5mQMz6rp5cSyIjKLnGYO8STlF2ulXi0kw4lX3_a2_1ThauxOtNQpIzh7W9h_sp6SdU_2svz5y_i5gCOQeX9QoRVkTZap9V67V6rAqda7b5SWV0dqNgRTuLj-X56V6LeTm9TjQrMyj-27mc_ZdS6aD3AVDrfbrvJbvAHr6e7mOco-p_Q5HneNsIsAavfY4uj8NHzUw4CtxR-9bomlw_wEEii4gbrCuXRIWDjZsXReMBfOawvI14VKKGwWcYojUp_P93sKyOW5t-6uO2RZOiVtupJQaf5FzetApo8OgpBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
عشوه‌های مجری صداوسیما روی آنتن زنده که در فضای مجازی حسابی وایرال شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/101876" target="_blank">📅 12:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101875">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umyzVG54i-5LNigzlP--Mi0JkBegA_rSl_05mi-9AEeoVTkHA8HDX9KwhVpHEkkyvO2DvE-qtzb84WRt55E5jIYHRrspYw9EkIyDGjvimaforiciKdjyavPKe5TNinkRqRJLEO2dhO72nNmGbwxNoY8iHzVlelsKOGB98rpsPLpmajfKPZUzZVUwc0Iew2GuHJxfhDDT50ud3pW8i21gWsnpzuHeOG5ebvNUeq7dCQS5x5RsslgBSIHu79nBQPgkyEr5o9z0KDIhCDghGspgRMCKgR824WxFDAUIKXjWYR_yDdDX1IiBfUE4zUOenrP8MfdRxIpwasUU2WIKYbUeQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
متئو مورتو:
رئال مادرید و رودری به توافق رسیدن
حالا رودری فقط منتظر توافق رئال مادرید با سیتیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/101875" target="_blank">📅 12:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101874">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d9c9fae5.mp4?token=eDAEZENAJoI-m_4ZH6_m-oE7O3_svBZ3jUAwK2Gmuc-RL91u5lbOn2Ks_XRrg4GsouoHQMpz47h6OrbjkF0LhSw1egjMgCtYJgseMYlxfIXtMQVA3f6GjLuAPOyxNJZ4T17JRheLQ9-3KAfQ2NXCT0JLT136j9C9yrpgHwkvsdid4ly2lIx3U0WXgszOjhjNyqhU24Lbcuo132NE8pM0hdxJfyRxYMo-rHijSZJ6EB5peGqDAzjz_79KOYZUe6_xEIuUHFvhwp-EyGB0ig9vIUwqcxuk5As5GI4dLrl1UgjrtLo2GyFyw9ZpoWCJbUW2OftN28s7gysQKvlqjdsYHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d9c9fae5.mp4?token=eDAEZENAJoI-m_4ZH6_m-oE7O3_svBZ3jUAwK2Gmuc-RL91u5lbOn2Ks_XRrg4GsouoHQMpz47h6OrbjkF0LhSw1egjMgCtYJgseMYlxfIXtMQVA3f6GjLuAPOyxNJZ4T17JRheLQ9-3KAfQ2NXCT0JLT136j9C9yrpgHwkvsdid4ly2lIx3U0WXgszOjhjNyqhU24Lbcuo132NE8pM0hdxJfyRxYMo-rHijSZJ6EB5peGqDAzjz_79KOYZUe6_xEIuUHFvhwp-EyGB0ig9vIUwqcxuk5As5GI4dLrl1UgjrtLo2GyFyw9ZpoWCJbUW2OftN28s7gysQKvlqjdsYHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
🇪🇸
وضعیت رختکن فصل‌آینده رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/101874" target="_blank">📅 12:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101873">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd5ea884d.mp4?token=WZr0xp8SmadnlVuVYduf-xJuIO_0xqCOzhzbR1NUPBRXw63826Lj5N5gBDouwB-9h2Zh0z0V6f4KiYBsMdzTlI8t9V6GHWhCYtbLwC4ctrhG3ccVfw8AH-_b-yEz5DVyNihMgHxvar1U3aReTGnWErEJ_Mo2qa8qMEuvVxfJOrCs7GBJo92PKpn9e9Yx7OBwva_sEx3vDSMQzRAN-WUAitMe37_OUHNk2OVLZK09bAmj9jnKlsaK3z8k9uZOqpX4g5o7QQhMbROMG8pFl_u1TbyTnQFcUuLKhxkXQCYPngWwZ_tg3UYScHa5oyB-NGM1HahenkKeS26HJCU2j46dMCufqPqH3AQYRimFZQn2uxETfH5Mbg7fEUZunBb0evpRS7i_5At2FYgod65eEIe3hSy_sFe0ahz-OggAZwM9wjHncp7vdJyUyvfRs3kL4dRZyzFXBV_J-mgSFc0ObAK9PYjSqv-a5B84KbeK61xGJgi3Xn2VO2bi9kWwb3qSfsTomRicLTOQeYjOyjuIhgDbx2BFz368aDL5di3wNp516JM-KCbADiBrVawpucJrRDLiVMDdX5AvVCNwrXXcEzvKUZrFL3_u4jTeuR4iXXvR87cQOMTH59d0-4KoWox1_cHK4qpIVec91wvDzRAb91txl6zB_XBMQrZnRJyVPW-4KF0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd5ea884d.mp4?token=WZr0xp8SmadnlVuVYduf-xJuIO_0xqCOzhzbR1NUPBRXw63826Lj5N5gBDouwB-9h2Zh0z0V6f4KiYBsMdzTlI8t9V6GHWhCYtbLwC4ctrhG3ccVfw8AH-_b-yEz5DVyNihMgHxvar1U3aReTGnWErEJ_Mo2qa8qMEuvVxfJOrCs7GBJo92PKpn9e9Yx7OBwva_sEx3vDSMQzRAN-WUAitMe37_OUHNk2OVLZK09bAmj9jnKlsaK3z8k9uZOqpX4g5o7QQhMbROMG8pFl_u1TbyTnQFcUuLKhxkXQCYPngWwZ_tg3UYScHa5oyB-NGM1HahenkKeS26HJCU2j46dMCufqPqH3AQYRimFZQn2uxETfH5Mbg7fEUZunBb0evpRS7i_5At2FYgod65eEIe3hSy_sFe0ahz-OggAZwM9wjHncp7vdJyUyvfRs3kL4dRZyzFXBV_J-mgSFc0ObAK9PYjSqv-a5B84KbeK61xGJgi3Xn2VO2bi9kWwb3qSfsTomRicLTOQeYjOyjuIhgDbx2BFz368aDL5di3wNp516JM-KCbADiBrVawpucJrRDLiVMDdX5AvVCNwrXXcEzvKUZrFL3_u4jTeuR4iXXvR87cQOMTH59d0-4KoWox1_cHK4qpIVec91wvDzRAb91txl6zB_XBMQrZnRJyVPW-4KF0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
اتمام حجت یورگن کلوپ با هواداران و مردم آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101873" target="_blank">📅 12:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101872">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05d40892a3.mp4?token=an5uMYE6srWdSSmw6hXVxvltlwxuUi7L5RSz3Ig1PTKfz6hoNqCDCOezmm75nGRKlbKc5_dZ7PIQOtzIpQiP-Oop9QIuFWlYvU_sRd0yRZBLP7bN7YAwyOuZbdzrN0ecSPdOwlhpoEAvmw-j257fhicO1zLRR9FVw0FuleXkqMGihZXkGdek2e2J4NINYTOA-fVfVdTql-eViuqyyKEVse60-_nTPfiMbhZr302XknT3fvbum3WZ5F9Wjwf-La_AYhMVyPztgxSsOqlXO9x69xDWcBDf6LsGgQO5LIbUtokY0pnNP6KcNv9L6gVUTBtotyK0l3i5xEyLXc9-cyj9ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05d40892a3.mp4?token=an5uMYE6srWdSSmw6hXVxvltlwxuUi7L5RSz3Ig1PTKfz6hoNqCDCOezmm75nGRKlbKc5_dZ7PIQOtzIpQiP-Oop9QIuFWlYvU_sRd0yRZBLP7bN7YAwyOuZbdzrN0ecSPdOwlhpoEAvmw-j257fhicO1zLRR9FVw0FuleXkqMGihZXkGdek2e2J4NINYTOA-fVfVdTql-eViuqyyKEVse60-_nTPfiMbhZr302XknT3fvbum3WZ5F9Wjwf-La_AYhMVyPztgxSsOqlXO9x69xDWcBDf6LsGgQO5LIbUtokY0pnNP6KcNv9L6gVUTBtotyK0l3i5xEyLXc9-cyj9ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇩🇪
خاطره جالب مولر از بازی مقابل آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/101872" target="_blank">📅 11:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101871">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Af5xj_OlUq-VRosgAvjlXLCt762bo0BHB-tlQJJkc-m8S0bULU6jtef7p_C-zyFQa0rfGf0GLcU2VYUBVYjbKG_ZyvDxucHlqmZpZX8w18mWk8RP_iL-IYHsRTugsNtvv7M0p1FuUoVzKqF-l9Kc67KZzziWps7eqoTzWikyHW-HwEx3vvvAf-k-X-vqGCoLzqHr7DO_DchD1bkyvIXM9VpR3lKFbddgop1XONGyWmdHb2CY2Ge7YjuCBSeW_--5RWauYqR19xpi-Fao3cT9JBeKMe1IMuPBnndu8tqOgKH0AEX7bpCuypYSALzzIh-VpO9VWietQK0OgyrL0aMa8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لی کانگ این رسما با قراردادی به ارزش 40 میلیون یورو از پاری سن ژرمن به اتلتیکو مادرید پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/101871" target="_blank">📅 11:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101870">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kiD-eUyVOekC-xXFf10UdCV5gIz3-l_Fx1Z9lXamR-g1FgjMXHMSd9Dx_clxbNFhLi1F0nGXOI1goXjGSFC2urHac_oaLuESpRkp_TyD9ywf-mQ145gi7_wYiwFLm6sLITe2gFMvmr7K0oJk2-5h1Y-mHIQKA9CbiUAJ43rE7uNcBUEAY3irPIAve7rqRYo7pOPexsZOmp_JcIkPJMZ4rizMbYs6RHC_MW7mrw2zEssP8TSeq4QQA65jdcLWh1JoSMPfk682XFEWT0BTRHs8EaFBToPvYT0AEmay6xXqU3U5MCVS5-cLuL1cNSVRSlz9eJ0tZWC4XtC5HkBL5GsHGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
تحقیقات سه‌ساله فیورنتسو سانتینی، تاریخ‌دان ایتالیایی، نشان می‌دهد که لیونل مسی ریشه‌های برزیلی دارد!
بر اساس این گزارش، جدِ پدربزرگِ مادری مسی در سال ۱۸۹۹ از ایتالیا به برزیل مهاجرت کرده و پس از مدتی خانواده به روساریوِ آرژانتین نقل‌مکان کرده‌اند. همچنین در دوران اقامت در برزیل، نام خانوادگی و برخی از نام‌های کوچک اعضای خانواده تغییر کرده است. این گزارش تأکید می‌کند که پس از مهاجرت خانواده به آرژانتین، دیگر هیچ سندی از حضور آن‌ها در برزیل وجود ندارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/101870" target="_blank">📅 11:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101869">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/917b2cd572.mp4?token=ZaZEYzh_-MUzWfUUw1K4-058GTbofNdKCT1D4pMTnuXmGBhHxGP9D6owyVTE5h2tSRvpNS3r7ECHLuNbJ6JUwKPbNyHVUaDNyiZ0qmWJpy7BJsVX8JhU8Krd7O0wUC7hiPkYwWkw5k_rDWNU5yg23wQNL0n1q_WcZXnsx-G7PyYz9qoFOOCXg_MvUlV6ba_NL9N7aZ7WHF_HyogWm2_y_4UEahV0I_WBDMTG-CmCE3TuV5B-KxRe5ompOkQLx_BikQ_OtG-bAprPfDCV7WB1fO1zs2jQdpRnPUGyh2BhqAgmP89WtrgiV_4rWdyi-PZPW0oh8GYkIJqISORGBc-xo1MdO3MWLo9_Fd1lsRM3ZUXAozHXmXeWipvFx-sEvhLMvOk0osut46P6DK_A8-zy77hr6QnKJwILKl4hNrjcmPLv1G0qgGCX6zzhjRoQf7RCiyS11PiBX_nAGhtCVRvazfSK1zLttRJRwVb3XFMaS4lbvkPUmv-O9WXTt0Jf45GTT7yoOn2zyytU6uSHsaTfMC4oKD34GUlrDFDQJpzHX2aGOjHd6LBGblAT5XzpyBCEYZ5vr2wG2Z0ZQgYPtOmQGE4eAxdqMqgFh62jKFtY9I0SkpKSIuFNeJpNQ1SsabtU1qg8YemRI7YKvsu9Y1rutbkpQBPfgJgs84hxrn3u_xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/917b2cd572.mp4?token=ZaZEYzh_-MUzWfUUw1K4-058GTbofNdKCT1D4pMTnuXmGBhHxGP9D6owyVTE5h2tSRvpNS3r7ECHLuNbJ6JUwKPbNyHVUaDNyiZ0qmWJpy7BJsVX8JhU8Krd7O0wUC7hiPkYwWkw5k_rDWNU5yg23wQNL0n1q_WcZXnsx-G7PyYz9qoFOOCXg_MvUlV6ba_NL9N7aZ7WHF_HyogWm2_y_4UEahV0I_WBDMTG-CmCE3TuV5B-KxRe5ompOkQLx_BikQ_OtG-bAprPfDCV7WB1fO1zs2jQdpRnPUGyh2BhqAgmP89WtrgiV_4rWdyi-PZPW0oh8GYkIJqISORGBc-xo1MdO3MWLo9_Fd1lsRM3ZUXAozHXmXeWipvFx-sEvhLMvOk0osut46P6DK_A8-zy77hr6QnKJwILKl4hNrjcmPLv1G0qgGCX6zzhjRoQf7RCiyS11PiBX_nAGhtCVRvazfSK1zLttRJRwVb3XFMaS4lbvkPUmv-O9WXTt0Jf45GTT7yoOn2zyytU6uSHsaTfMC4oKD34GUlrDFDQJpzHX2aGOjHd6LBGblAT5XzpyBCEYZ5vr2wG2Z0ZQgYPtOmQGE4eAxdqMqgFh62jKFtY9I0SkpKSIuFNeJpNQ1SsabtU1qg8YemRI7YKvsu9Y1rutbkpQBPfgJgs84hxrn3u_xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
درگیری خونین و فوق‌العاده شدید در لیگ امیدهای فوتبال کرج؛ مملکت بی‌صاحب همینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101869" target="_blank">📅 11:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101868">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClkTkrriDr2LNiXkVc2-acuHd3NVQuC7PXKOwNw1efC_Ahgmb20jJglxfN-57QIQzJCvqAyYejmbq4kbz85hDEcyCima_gl9E5wMpZIfaapN77o6Lp8i-hn7jOShvTmCuCs_euExkSWtc6Xp35yQMyx7xWtjcZ2oB3sCeNsPUCc490iW7BIKQkBZjmE7ESJjP4Mm3EmTiwWovYZZj0jlv96rzPHUB8Hpy1PwFDQzeuOhNd-HykSFMgK9q8zehGnK60vFERmBs4F6crZf9zrgHCkV0Tz2Y84LtoIDFJ72CMjWGUSyLgni2iqkMFL13F26ZCQggvGFMHEzzM0Y2k_apg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
👀
شاهکار سرمربیان اسپانیایی در فصل‌گذشته
🇪🇸
🏆
دلافوئنته قهرمان جام‌جهانی
🇫🇷
🏆
لوئیز انریکه قهرمان لیگ‌قهرمانان
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
میکل آرتتا قهرمان پریمیرلیگ انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏆
اونای امری قهرمان مسابقات لیگ‌اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/101868" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101867">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f4c9480c3.mp4?token=b2PxyLBpzdRPMtPK1GKkH7LAtPkDog-Vy0LLYt0trrweeZ4lSRg8fjOHg3gw2oRGBDtEJ0RAKVe4-WCgT3edPvifwsagUu4YIsRMRdX_zkWjhmOE753xe2gol2pJxYHfuWRTnhUorYqX4NJEprE3jLW9RYlMix7JQE5QA0rLas0MuZ3i-MgHz2vIF46BRmOwAMwE0M3bVNwLN2PHNJ6dtF-ddrdMpjW8RLm74nFyPQhWnkZhvmGuECXLd6de_OQak52MwutHLL4wSJQLht3ai_zL6I8lztbBk-iTv26NAnxiUNSYSezGWwLUn28JDx2p2_vXNMwDLDyyc4a6hTc4iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f4c9480c3.mp4?token=b2PxyLBpzdRPMtPK1GKkH7LAtPkDog-Vy0LLYt0trrweeZ4lSRg8fjOHg3gw2oRGBDtEJ0RAKVe4-WCgT3edPvifwsagUu4YIsRMRdX_zkWjhmOE753xe2gol2pJxYHfuWRTnhUorYqX4NJEprE3jLW9RYlMix7JQE5QA0rLas0MuZ3i-MgHz2vIF46BRmOwAMwE0M3bVNwLN2PHNJ6dtF-ddrdMpjW8RLm74nFyPQhWnkZhvmGuECXLd6de_OQak52MwutHLL4wSJQLht3ai_zL6I8lztbBk-iTv26NAnxiUNSYSezGWwLUn28JDx2p2_vXNMwDLDyyc4a6hTc4iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
🏆
رقابت‌نفس‌گیر توپ‌طلا ۲۰۲۶ در یک‌نگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/101867" target="_blank">📅 10:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101862">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KZf7ji4P2elSKJ1k122n-MKoatVIuxprC9Q4ZtHeTx6YwbrEYjav_OKwxzAYsBVm0tqtAFr-UaVoYI5K_nYwCMFH9mOZiisAnbOwu3LOLpzBYDaJi3eHuTWQLDd9CICPySm8KuX2IJhOrzSXFsiWLN8kl7FFJE87R-Lvr9yR-eFBdNi0LQwPCxEWoshRwE8xb2pD8JjcbwfL-97t9sdmqoB7s6x_BM-2h6bVaLSCwsIzsFrT4FwoL-ZJEB5nJ1l3p0O8qf4gUxbPvrb88mnoCUPh3lV2bxrOzr0TPSWguwiLDmOCgXNe0kBfaA2E_mlnY9LrjAfT8vmVmr8QwEeZGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TMi0dRIBdto8lbnFO1uS1i1XM-53CMrTjlFftfYI01OeOiR9-i3_OTE6YxObH1ta6twoAm6WTwdltksBIrxtuvh0ehV7IPDGFNxqqZIlkQD69F8RIeK3Ksi6Vok4jzSa3S5ku0gXoSmIA4ClJpD2_Tad5OVvrotloKMo0Y-eISLpDsCvW5_9jtkoHkB5r_fOI_Y9vZ9NHEifZtrWkNMysxhV9x3G2H5CBQnUoCjMnt-1H8j9E3OgV75wg8YWO6sp9aw6yL9xyy4pzyfEg8OoqcFcvkWp8yuLmCtoSZ1idul54jIs1cNW6mmvAVicY-JDnnBhfZTYKJ9YSBNn88Z3rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZNyOoveo_Ju7CFdcYUN6Lb_trva6yFar8WRg3V_hdnWHXegThlw4N1ohoRkkoSams-V9mGDQj-gJgwGi_yArEeWAIH25KQ0qEKJ1Xicx78heHpiAgsBDDMc0cfYLyUYFcLiMEnIXnMD9_Y8ep3uY4MxFsmSB7AfpyWG6a1r3SNTyAooAHq6qB5JE-Bhn_scr6_uK5LOO9qTlfuWevpSsk_mwS_f7oWfVZIBiuKDvQOWk69qsw6lf7BYVzRc7bG3b1tKn59dFdn2lVP_Rj1Mf_d6oXvrJGvO4vlqzC4ev_LfcUxfqIgZt4uhGs1Loz2mcahbc11GLf-QwxX582CYEsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TS2eWv3ucHYmQKyjUxMGzdv7FknQG5NujEhUIhg5dnncwR3WRcaIwtuDu-wKkSp1u9ulslk-RqNRp1Rc_zbIHfZjv3H9V3hfHZrHfFG0SlqOltuELSla5VfUgl3n49oDaacZHIQw4ov07NdfClcBf9CTnck1Fx8HM3B6ZxuuQXX9C599NHYHoEHL0aFoOSCMploCHCXd6pzuhqr6aW41apisZgnzKUvkEcJsq8_j0Kzh_wRR5OVBynxTzcJyNfYf0YguQ7DrTTZdlgd5b9AG8F0-qgf-29osBvSv5BwqYS-8VIUcsAcgSd6KgGaV3Lpps3yy5uy48lfpuiUSvn0Jmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GcWzRMG2s3sr0-zQE9dxEcv544LE4h0AjqX3Nxo7CyMRoMFTM_LrVQLR528MPRV19JWy9fKGK0hGvccugGjnuf7qpGLFHuCH--xVKVe8V8ReJjT1lSXpjz4UvJs7T8wQXKmAYl5RYnj80yOv3ETVFaE4Rj8F8qtXumgVqW_uykUNlJoRawRK5Vc1RhSTLuPew8UR-gjCOUzMjhdRJjCqIne4mLCmC83PFv1H0WdY-ZSN2o0jVQsIlyT_jqNwPvVZJ-mMyGbAW-HOpzzePKZ-FHJAekNiv11g7kSbJ57KwjN6F23Z-aUtyJXXMtgUAHkMomddCcyOnJxuOr_NtONfqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">+ قدرت تورم :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101862" target="_blank">📅 10:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101861">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5d7ccd208.mp4?token=ih9kN0VwiJtXQ-NCNyv9C1aBPSckVmMHhuK875Mps01WWzKwp2u4ql_5CQKF1nLmikp5XID63ga9PeIkIGAAhvvc4H5oH50Rpb5SVoJduW6ISEZzIt7oVGI7eklzjCeRJ5zSHjG0HfkegH89twjEsu5XNp48tmXEeBEoZV4mjl8rL3rS0Am1i9V6Z8mfSxy0DGcLWGKZpYIZZJzpRm15QHoEYdKXX41tPWlzBun9XZ7pM5KlIa1iNbT6NVJK195O_85OyJceaLLgDQITVU7YrAD9MEmjlu1LYwdUnllVVvl9DBrLQ1v57Gr4J3Xmnn2peRBkf7YlP7X6LN8Bc2xZtg--ZedjP3D0FijTDUS8J3cV5sztOx7vv6GvGbK394PI_GD9oOkbEMMpF6iIfKN2jUgMdjahA3-pkP48UmvmYtYpvua3nqXxMe-biOm_4aKLvndKLKjSpkTh_vS7pQEkGAD2AMbnWW8huOik4uTf3aXHzSg9nix1GDWB0Bc2TkWaaBoYaq5nDAnIra4LqnFhbGK78IpfilLgVgY0NKq0UZnU3raVwRNH_vB5IuDSKhOllAqG_iCXgyKvGYM1NDrI9fzAjhyr5mldcls01i67MxVdVx5jBi8AuhJronyKMVS90J_Cd1FYglvRKMqY_kekgCaUVS0J4UcSyNK0rXifIIM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5d7ccd208.mp4?token=ih9kN0VwiJtXQ-NCNyv9C1aBPSckVmMHhuK875Mps01WWzKwp2u4ql_5CQKF1nLmikp5XID63ga9PeIkIGAAhvvc4H5oH50Rpb5SVoJduW6ISEZzIt7oVGI7eklzjCeRJ5zSHjG0HfkegH89twjEsu5XNp48tmXEeBEoZV4mjl8rL3rS0Am1i9V6Z8mfSxy0DGcLWGKZpYIZZJzpRm15QHoEYdKXX41tPWlzBun9XZ7pM5KlIa1iNbT6NVJK195O_85OyJceaLLgDQITVU7YrAD9MEmjlu1LYwdUnllVVvl9DBrLQ1v57Gr4J3Xmnn2peRBkf7YlP7X6LN8Bc2xZtg--ZedjP3D0FijTDUS8J3cV5sztOx7vv6GvGbK394PI_GD9oOkbEMMpF6iIfKN2jUgMdjahA3-pkP48UmvmYtYpvua3nqXxMe-biOm_4aKLvndKLKjSpkTh_vS7pQEkGAD2AMbnWW8huOik4uTf3aXHzSg9nix1GDWB0Bc2TkWaaBoYaq5nDAnIra4LqnFhbGK78IpfilLgVgY0NKq0UZnU3raVwRNH_vB5IuDSKhOllAqG_iCXgyKvGYM1NDrI9fzAjhyr5mldcls01i67MxVdVx5jBi8AuhJronyKMVS90J_Cd1FYglvRKMqY_kekgCaUVS0J4UcSyNK0rXifIIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
روتین تمرینی لوئیس دلافوئنته‌ی ۶۵ ساله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/101861" target="_blank">📅 10:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101860">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/025979a7c1.mp4?token=rGSzJa3v03gi9yQNVeWV0mR1KSkYHY-ygg1drETNWPjhYWs2vszd_Lutc7NGP-21Wf8FPm7WTNMcqpDKwv5Cuhzq_ogTr3GB-vvC65HxByIJuLsDotg--I_smFw81mnsmQJzw5vp_bhhHpxk_47h53KCkddiBDzuN3W2hKp4RjnfiEl3E3e8H9hmt3QyyPA36MKG68eUSFE66E0m-MVBZtIdVMf63t85tf2Th444yLktWrJO2zXfNjzHD4cXfAjL57AGDFVnamlZ-_2meh7KPo-DAi5ZEqUKOhq1Ce9n214LY6u39mqxy3rltUoL-thJs7CYLm-Hsf7qOewcuPzJ3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/025979a7c1.mp4?token=rGSzJa3v03gi9yQNVeWV0mR1KSkYHY-ygg1drETNWPjhYWs2vszd_Lutc7NGP-21Wf8FPm7WTNMcqpDKwv5Cuhzq_ogTr3GB-vvC65HxByIJuLsDotg--I_smFw81mnsmQJzw5vp_bhhHpxk_47h53KCkddiBDzuN3W2hKp4RjnfiEl3E3e8H9hmt3QyyPA36MKG68eUSFE66E0m-MVBZtIdVMf63t85tf2Th444yLktWrJO2zXfNjzHD4cXfAjL57AGDFVnamlZ-_2meh7KPo-DAi5ZEqUKOhq1Ce9n214LY6u39mqxy3rltUoL-thJs7CYLm-Hsf7qOewcuPzJ3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
دلبری‌های لامین‌یامال و‌ زیدش بعد جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101860" target="_blank">📅 10:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101859">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/552820f16b.mp4?token=g-WFp1-UEIZJPowMEvkRjoUf5U4Ao0zuIoPIoRiPnEGUqxgPZiScZHstsXAAdzcWCFJZH2mpUDIAz3dWvHVgW55EtCBG5RVE0JEgtIfJjW0-Yjdld4_h5gui2kWOOZr4sMeEDo6Vm4ukYhlNonyrzeWovUAucAgED7mbLvBVivYCvHue0zzHo90EPNiK0wZUfEu-3fsHvzvdo0DBMObXnh4dA41M57sKxE0M2UjK6TKjtnXMGcpNq446FKsBTfvML6u27ID_Xs-L6S1MW7gBfeU50BPqjy6-xmBIY4Rp5Gnw7d_EOe-2PX6OnN2eSDrCK_yrd9m4VVcEqWlHi2xNOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/552820f16b.mp4?token=g-WFp1-UEIZJPowMEvkRjoUf5U4Ao0zuIoPIoRiPnEGUqxgPZiScZHstsXAAdzcWCFJZH2mpUDIAz3dWvHVgW55EtCBG5RVE0JEgtIfJjW0-Yjdld4_h5gui2kWOOZr4sMeEDo6Vm4ukYhlNonyrzeWovUAucAgED7mbLvBVivYCvHue0zzHo90EPNiK0wZUfEu-3fsHvzvdo0DBMObXnh4dA41M57sKxE0M2UjK6TKjtnXMGcpNq446FKsBTfvML6u27ID_Xs-L6S1MW7gBfeU50BPqjy6-xmBIY4Rp5Gnw7d_EOe-2PX6OnN2eSDrCK_yrd9m4VVcEqWlHi2xNOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
⚠️
بی‌توجهی یامال به دختر پادشاه اسپانیا که در فضای مجازی حسابی وایرال شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/101859" target="_blank">📅 09:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101858">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5533cc045.mp4?token=c0dLlbfsqPlPe_O4M_XRAo7VV-MryIJfKhiDbBT6EQip_arE_k2cLY1e-KVpfstchsuLrgNJs82SnEBnRlc3Rd4vaAqKGWHPPYY33sQhUPgiLziiUhKkKxnwNBXHVNNYt2WMfozdshEp0wf-nYAau5I63gzYsvLmnPNx-e4fYim1AuA3yteCu3dpFFfxcdeAwDLGBYTir5C-n0elZX23Pm6t4j6lFl2-TsllseEEtceH2XE7_8kYFiDOD1_NfnUU7TFDh6VnL3zYH6_3ekrrtQ90gMIykFW-__YPnsO1kZPXfghGm_IgpWdClsGbcC9rscBNcbmRnij441ugDWBVdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5533cc045.mp4?token=c0dLlbfsqPlPe_O4M_XRAo7VV-MryIJfKhiDbBT6EQip_arE_k2cLY1e-KVpfstchsuLrgNJs82SnEBnRlc3Rd4vaAqKGWHPPYY33sQhUPgiLziiUhKkKxnwNBXHVNNYt2WMfozdshEp0wf-nYAau5I63gzYsvLmnPNx-e4fYim1AuA3yteCu3dpFFfxcdeAwDLGBYTir5C-n0elZX23Pm6t4j6lFl2-TsllseEEtceH2XE7_8kYFiDOD1_NfnUU7TFDh6VnL3zYH6_3ekrrtQ90gMIykFW-__YPnsO1kZPXfghGm_IgpWdClsGbcC9rscBNcbmRnij441ugDWBVdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😔
امباپه‌هم دیروز اکسپوزیتو رو برده یه جواهر فروشی معروف کف پاریس و براش هدیه گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/101858" target="_blank">📅 09:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101857">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiLXc6rUIUimaBPiSQNYThVloEpIdBbZKt2YZFKCkXjW1jnvLiEcleh4ABCJ0fZz7Al3uzkTkxe-OQlUfYs4gNrlG0lyKckUwbpjSGM4WE3Q58jvkRA2EQ_S2js19ZZCp-Bfl-mHHpwInaLo1FH4D-cRIzHL2MEZAJOe1a2lcL9PLIGCT7gKV5r96oIPVjPCA8zZRpezsGvtJUk9q0jbV-VVuBzkjjpWfmjghMR0mfiABmOtnKefXpbL-g4S8f0VDKlzH6JsolxsL16CZyrU_rm79GDaEJ3pvf9PJT5IXQPNDxtWm17KKKpPzyAexzbp0wDd-N4piACFizUDEBnDRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
✔️
تمامی کاورهای بازی FC در یک‌نگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/101857" target="_blank">📅 09:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101856">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحامیان_جبهه_پایداری</strong></div>
<div class="tg-text">این یکی واقعا معرکس و حسابی زده توخال!
#من_نمیتونم
@hamiyanpaydari</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/101856" target="_blank">📅 09:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101855">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
▶️
کلیپ‌فوق‌العاده دیدنی از پایان برخی از اساطیر معروف تاریخ فوتبال در جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101855" target="_blank">📅 09:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101854">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2e5fe7985.mp4?token=NqtLqXHrpP0QYXGZRoIUqUW24T2fWt63uu4h6BCeK5UA3qPDjXd3X4sboqFyqAjTHip_Dhr-qgDedkHmPiFlHxBZq7KTlUhyVENcxqehuT0T4PDMlcx15kiVCwv4STnYqp489jPiyiMURuTELCNl_Jbx1WNb-tOCvzUzUgDI5ZSrJTk3PSwII2WXMuMonbKD3Nz4Sd9bCEmUTf-c_jfHf3zsYJ7ZumeX-AhaGVQ1WctlA9dYg6urjFj1Af0MSRqTQUkedqXbocfj8nD36xJYsAJfQeA2t2BEVQTPZ5PNP2MXsNF2coaCPe5xuEEgdhuRmU-L4oqCL92YbyyQGVb0vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2e5fe7985.mp4?token=NqtLqXHrpP0QYXGZRoIUqUW24T2fWt63uu4h6BCeK5UA3qPDjXd3X4sboqFyqAjTHip_Dhr-qgDedkHmPiFlHxBZq7KTlUhyVENcxqehuT0T4PDMlcx15kiVCwv4STnYqp489jPiyiMURuTELCNl_Jbx1WNb-tOCvzUzUgDI5ZSrJTk3PSwII2WXMuMonbKD3Nz4Sd9bCEmUTf-c_jfHf3zsYJ7ZumeX-AhaGVQ1WctlA9dYg6urjFj1Af0MSRqTQUkedqXbocfj8nD36xJYsAJfQeA2t2BEVQTPZ5PNP2MXsNF2coaCPe5xuEEgdhuRmU-L4oqCL92YbyyQGVb0vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
✅
علیرضا فغانی: هميشه خود را كنار مردم ايران مي دانم و از حقوقشان دفاع مي كنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101854" target="_blank">📅 09:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101853">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBGnU8aI1UzQNWMJdCutdv1PMI3AvHph5xn9tpD6EcaTJ7gB3ORsun1h4b2ApnFLhz0HcvVwBc0fszMbAK9vpyYDFvj7Z7rFnLm8vgv3Ar4YXvXWG3kGJtKpNz5UffOFNAFitBTJiRVMRLrHQTEwyWpzU7hHwetmp85slhYdj2y7mBr4X7tnTcRCeYJbgJxSdFf9bJB3elQgwLlrG6rQoEaJXh3XtPJw-ugqdCWds3ai9gvPITUZo6sfqd6gqM4Ik5cy6grZLbGEbAYCU0j05s_wtktnnb8EdcD27fNC8ZIK7W1ROVqL9A2Czz4lp6JeRmNSjCjYZnSkYcr27chnhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رسانه ESPN: رئال‌مادرید تصمیم گرفته که به سبک بارسلونا، شاکله اصلی تیمش رو حول محور بازیکنان اسپانیایی بنا کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/101853" target="_blank">📅 02:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101852">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7211acfa.mp4?token=gha5Gup9AWk28a96mlAumZ2LinbP02xa_qVmhvlteLn14RoL9o2Lbb-w1CbNHB1k6O5-9CbjSWnZhXZ2ZGFAeJFSthNrSfZYHAkFek6xHySfjoganF4K7j2uDR4GxxvElvWEECYXxc8S2wXw8k6tYYnQJf7eT9CKXpE1EA65jcF0v6tcT-QawyxAte_zpVYV46IEMZcbXSetp8g6eFpOo79Nt8-1XaN13Rc9PVaCMKvmV1iOgm0eD5fvh4gjaXuWfT-Z-9egOxV256vuI-O_om4acX9sSbt92KCDgymAnWnNSzRxCTXTgGTFNSn576x9E5910p2i83b9h8oRRUca5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7211acfa.mp4?token=gha5Gup9AWk28a96mlAumZ2LinbP02xa_qVmhvlteLn14RoL9o2Lbb-w1CbNHB1k6O5-9CbjSWnZhXZ2ZGFAeJFSthNrSfZYHAkFek6xHySfjoganF4K7j2uDR4GxxvElvWEECYXxc8S2wXw8k6tYYnQJf7eT9CKXpE1EA65jcF0v6tcT-QawyxAte_zpVYV46IEMZcbXSetp8g6eFpOo79Nt8-1XaN13Rc9PVaCMKvmV1iOgm0eD5fvh4gjaXuWfT-Z-9egOxV256vuI-O_om4acX9sSbt92KCDgymAnWnNSzRxCTXTgGTFNSn576x9E5910p2i83b9h8oRRUca5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
‼️
🇪🇸
شروع‌قدرتمند آردا گولر در ترکیب رئال‌مادرید برای فصل‌جدید با خراب کردن‌پنالتی امروزش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/101852" target="_blank">📅 02:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101851">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqBfL5eXffk83RIOptdjjsekAKpKqqa_WKRHvwWvf21h_CHcAU6DFE8-IwT5_8QHh-H2rdRrbu8SIAKmMM21aRwRVm9Dk3XGKPyGlXbfJdOH3e8hMdIhtcmjjJ5whEE4i2bwiYTZGif5ZDIsJut2vbhKTM1HIVwOLOEW48_iFeRHOWfSNfGNTLtvOd2nPeU36w3KAqP0ma89nAGs7D9Ll_wiJx4qoU6H3E4B8qgj2jz3Cyp7xRe6p0XPUgidcFdxZ5C0psFTu416pMftcnmI2C_oO2eXe0CQ-VSvUEqYC4YSavV3AEG_I7eugiaea4gLPIPAL78FzzRlbzgl3lf4YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇻
بر اساس شایعات منتشر شده از منابع خبری آمریکای جنوبی، ووزینیا گلر شگفتی‌ساز کیپ‌ورد فصل‌آینده به لیگ‌شیلی خواهد رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/101851" target="_blank">📅 02:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101850">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c-dxPaReRuS_mY1ZdYhm7r1tGjq6MWqQcB7KFQY49ipWzZ35Bvw89p1JgxaN4oyCR2sJqcsE9yUhclbHfL0-4mtwfXntsCJDYGPwsFiH0b4L0Z8XswqlsYxqsZcxM1hgxr3TELR9IlnHZAtUwhHbnUVEKK-baVhIUXNJ1ZGAn3DZdkKHOixN7yJZFpBuIsE6deUiYsVgVmZ-9n-9nORboljarC3jbv3vBFbURaqWNW5XZheKDnXu0XPBnv-gVvGaxQX9bao6EUmV7kBiNxnsp9f5AJ9V0tFpRBSUWUZHyFirtZbJklowJWh0zrliGICWh98OgPTa_dZ5V9n1IYC1jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/101850" target="_blank">📅 01:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101849">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pO_irJUtT2rhxfqpKf7PyD-gSlt8-7YlalRilBltYgkKs-leVbRM6aHH2lj9GZxO9mnE-wkgw81NDwORIXC6U_V5pZbDpe9-tI-deedBf3dXzjy5A4XjxWeh5aCKQ-gKg2nFDHwxihohDNE6KlLikVXgEirRKakIWUmyQxeVpC9uJOLtTOp2SG7qnhQrDnFYZImr-lEXd22iy1xLQjY4wzC5pIEyP7osclBnKCqXQMRDyqrBJS3xjLKbbNksV_ayhaArZEXhDI61CAgLMRkjdE7Ofts70NtIzEZE2mjfHHT_athypEJ9DCXeB-64Pcy_nEmYQ6GZVSjFrRZ-Fi_zWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
🔥
🔥
🔥
مارکا: دیومانده تایید نهایی برای حضور در مادرید رو داده. این بازیکن به پیشنهاد نجومی پاری‌سن‌ژرمن دست رد زده و گفته که فقط به مادرید میره. مذاکرات فشرده برای توافق نهایی با لایپزیگ درحال انجامه و بزودی خبر رسمی میاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101849" target="_blank">📅 01:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101848">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eiy0tLkafz6e5NlgE8OZSAEMIPYxqD3yByegkuWZSDo8mrUrf8iDW4CGXfHaBbj-cauNwaN9W-zLc0OSHIXtnQMp3rWYH6J0fmiNKXZF1YV4PyA5F3yuQP4O-XAWDFfU8nyHW7TQu-ncso0vkTT2avCyTdygfRuLxA7e8GU1m9G4oyInNQJYgcjbEnH6TFijjtw4-SArep7PATKU7ys8_NYS-34GI8mEge94dy3bnVS6mmcdRUb4k-UON7AGJMvDygYK-07hML9nT78MErKUswbpDrfXzI8dK8EadpM4hmXONJTNezO12LUf3FOv7DPKu_fzOfffJhZfuLFvA7bepA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
په‌په‌آلوارز: رئال‌مادرید و ژوزه‌مورینیو دیوانه‌وار عاشق دیوماند شده‌اند. این تلاش پس از ناامیدی از جذب اولیسه صورت گرفته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/101848" target="_blank">📅 01:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101845">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EAI7ucwi1x_gDmhKAbBnyUzCpOS5JSH7SoJ-79ghUx2VQ8idGPdg1r_erIIsXszmr9JMPRTHXdJbpb0H9k9EMPiNCucEvuCo3ZJAxDCJiw9HIKqnqEsTcNIDBFnKULWDCP1Zg0NumoVt2ZpFEywflFpw6EqCZMDtCve0rrSdxRjKokg8ZWbUn-PXCkDqlgUhDis10n91XTbKjiMQJ6ftbwacTgZot9teSupp6IDb4luOe-3maPdqJMBHavVqrNoUg2XKYSznaNZ1nWjEfiCgIv5J9RfGlDs0Deuue_Yjk-prr0gWSlyWhpKhTxQDanTD1quWmJczWytCzpb2IBzDNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oCTN1H3XHJjlyofiJBerARkC7Nb5pr1xfINQZaiqLJRMGFghJhSs3TE59yYVyHUhoJZFo9YdcKhKZnLJFQw30wbLplUyHDgsqyCCrwVz6t_HM6PD46JbczzaaRbjKZx9e1KC2VKNadM-tuos0kSHYZhJAL6y_jNg2XJ0RafKY5YUGoSZkJV6wm2IlTx7DdQdgG3FY06xOvZpzd3smo3-cFhbqwT3g4hcVZR1RrY8-rSO7WHKdJBrxurxY6c8qeJ69vexJcYTzJaJoCyeya3zab1dPLOB_S70smHkWld3YJ0zpltLyQyETmwLtEsEXSrDryn6Iw4yqq-U9IdDxWdC0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
په‌په‌آلوارز: رئال‌مادرید و ژوزه‌مورینیو دیوانه‌وار عاشق دیوماند شده‌اند. این تلاش پس از ناامیدی از جذب اولیسه صورت گرفته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101845" target="_blank">📅 01:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101844">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5gTgF5oyyDJsMyZThRgDfnaqfkIfDBlqYIJgKAFAAYrbAxCXf3uGyUpQzDTPeD81bIUtFOW1JWfSOBt2m4N-y2G7LmYfHU__15m7lQtuAjlP6yqXiJqk6VvjZQbx8GaBdA_OkIrj19JHIL-RWqvA3sjO6mavlCy_4v2tsTeOCCW-QCOR2zuOMfghscB9cNwzENEa3fLJp7hwA8XUX9LNw8FDqn2ohS58THu06K2dURxulI6DjZIcuLzUosLQ8EnUv_RPFMLEqL5Eh4S2tFi5XS5dRjh5o9AkpSd5Triv57Mj1wMuG57PPEUoG8c4SdQZ1FAqjcP716sktDXonMVUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇪🇸
په‌په‌آلوارز خبرنگار مطرح مادریدی: در رئال‌مادرید برای یک‌فروش دردناک و غیرمنتظره آماده میشن. بزودی نام این بازیکن فاش میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101844" target="_blank">📅 01:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101843">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jynl55_sMJU1p6lW3WKPUFBRXa-l8U6TN_tX9M4DblkDNI__9BByvKI1HIG-GmlzYJ4WqnFh4zaRfVgsnwa175Ap0RPIfpLdZB4EQbq-dIpM-0bXFDC_cI8R5Vk588R3CHknjHk15pdPhD5MpbbhrwV3v056aNyTrMaZNBeEQal1o80OomSce3VT1QWkfpiH9cALPJUvVt7ajkXd5LQ5BBxU9jFitEM8nzxNN7ybHneH2MwMwkNybRFcrP3nobUEbDTFgmy2xi9RLyDIXm6dEm58V-EGwLgcf034Bwe6fRGNQ3OM6sjfw2EyT4lPe2vhGbViHWoE0XMTVO0fxSgjcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇪🇸
په‌په‌آلوارز خبرنگار مطرح مادریدی: در رئال‌مادرید برای یک‌فروش دردناک و غیرمنتظره آماده میشن. بزودی نام این بازیکن فاش میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101843" target="_blank">📅 01:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101842">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
⚪️
رومانو: رئال مادرید پیشنهاد اولیه ای را برای جذب دیوماند به لایپزیگ ارسال کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101842" target="_blank">📅 01:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101841">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dkl-bjDqFmLy0NWGgzqKJ8KSOr5KrpZUENoUv7uG4BgPHz47CIdCSeFDJ49Axlfguvg0dxUUUfcN23RQ3G_OuNubAaBBchgut_48afv6iKwfBq-ITQ5QW9eT65RtyrLTF0auxu4vrHkFu8cGrOoE03bodAcSynig0QBXOpQEk9wYxaEBWr2GyXNJ-riQB8OJQ3rOGS2GHzinSPpsDP5-zs2EBQ1Xb4VL04mNaIhBcyhDtTFqsKSDzMeRN50xVe2ANP2r4cvDRwB3z_E_3Fk2PeClSfzs8qB45QGHFOyN6m1tzUmSsOmg6jrtW_wnYDzKZgCt2Fsk4Axmzm-U8is5qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیژن مرتضوی و بانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101841" target="_blank">📅 01:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101840">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOgmW3Zndc8PHocJU0jk_b1guPew-Wwz8_LlI1CnLdVAWqIa124lLWQjsm-aS9_pVAz46D9I77DDhpHLLp5PeMzt4w5G46p9pAtF3Xq6YDGwJKwXLjKHWwHjJQ-sp0Kn78kdeAbnZLEw3yhA38bu7lHyIjgpof94M9ACV86pg2PTOWbNcDtv37Wr33zbqmRiJPt3PWSqgGrxz_EBkP0dPY7kq7-cQ-fxilb3gLOj3uwpJHcUSrOAqbYdxEwXQVLheg1yogr7LusfKwSEhDRucI-J-vsyn2A-s99Ahu5E2TidbcKfUymxBNHTVWtqhkQXiXxsXYtEVuy5ObG2lRWxxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🤯
رقابت دو اسطوره برای رسیدن به ۱۰۰۰ گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101840" target="_blank">📅 01:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101839">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8hS5nyq9ZDtekpSKWSLar57xy8jXakgHmZVnxvPscClK-T_aAEP1qQuCn9gMM1NHn-s3T9q0IYgy9Mx5i4meZBuAyggVbBD0gpzJ0vAs62eTSpxUnyF7wSytTAicgQ7hXIByx44okJRDiqk6ZiqTm-gGIEIw4iwa1sslgKla2uv2tvBaxYgKr8sn1S5xHTj3rtMJrmo4C2FS6Z6O42mLGBmmPGPlxJfxI2NPiTSiT1S1825OJ_YvR76BFy4UqaQNYsOagBshacayxw77MR4z9OorZkrMVngQBpF3FN5ID2-3Ar6pp9o5cRAp6EqKHaekr9DEuPODbsy8XR8Dl5uhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رومانو:
رئال مادرید پیشنهاد اولیه ای را برای جذب دیوماند به لایپزیگ ارسال کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101839" target="_blank">📅 00:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101838">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofUNm_gw89WLJrT4rFKLFGfEVFLlsVxXBL0i_6M4PdJPxqNLJfXi7EkVYo8GF5SY6gxbXw9c5mPEvCfMPUL3GoqQ_J3Bh6_7zyiRhe2CA6VZMupjMz5bgtBshffK3YC-LX4x7QI50GKQqk9QkHGNgI-4bvPVZJJUKLso1EmsO21cadLy3fPbxY25y_9EhzYhHZMh5_2yrInTdbQ4fcEOlQNsezolxgL1dmgSp4n5Ui55hrkWM_HBuQLPQQ7xBpxGycOL1WFOMTtaPM3x4KQjQNjpFXxILpGTUl3DEbT_3LJY5sJmGO5M2688w7JUdPn_FIxaI8OrRlBVhGN5W8W_fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
بهترین بازیکن جام جهانی ۲۰۲۶ از نگاه فیفا و برخی رسانه های فوتبالی جهان.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/101838" target="_blank">📅 00:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101836">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnGK86CA3BOjPRpZ3F4dFfF1WGC58WNLxJFjnBPAH523dm7EqH_xkYNwu3G2wXfFPirHQQNXpBv1kSLG8ulLQELyVF8IRbGZ6JhXqPrwZTqbFin8ASLdnjyT7zHtSbSDOPcuJLvnwalsB0KyRkAY0tqOhFp_CV51KfyPwZfI_f5gX5W0yEaiL4O4xIewCp15rvwxouFbNQdWsuL78FcEk80AiarulIEYuMZEigIcJuMAU--PJTufBd4baruJC_Oj4W9_Cwqs56Y_YioKrtAZl6CVdYKmg0NlwCYB6rkF70q0a2ctGUtwff1cDvBBGbkmsUhv6GLyKOODU60EvlA7ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
تیم ملی آرژانتین اعلام کرد که لیونل اسکالونی به عنوان سرمربی این تیم به کار خود ادامه خواهد داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101836" target="_blank">📅 23:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101835">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQssKl4K0sbjOY-93pUKzjemIUDfr7dn-UnhSh1sl8PWoy-2OiS_yQBf3DNpiE-7IJ6q-Aut227cidbgGswHI2s_hw3YPrpk9eH8aEeVkIzaV4eznWE9wdOsCGz6DYlqH69oBY-bG61CmYBA5swII8Zs27mQm4jOlFKgm-yWf2AtMGglfyu1aAOm8yU0RWsTolta3mZ8O_MrVzXbQAXHXvYkQi2mmwHodmx-rr8fvUFYl62Mdkm8JsXRyzG7hoNiSVkRvJKUU_I861VswUOb6-g7QApIk1qFDdYmzDBH9Vrxow_UKjnDRFAvkb7FTjg5lg6gcC-YPzpcbMc-Ju4bwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
فهرست بازیکنان سانتوس برای بازی بعدیشون مشخص شد و نیمار به لیست برگشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101835" target="_blank">📅 23:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101834">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-CEXRC4nNi_EY7zJWzkogVfcK6QZHqZZCxpE0fkwU805e26DOxvZajlGWoMBkOenZQcPJk4-Jom-7E0Tu84RY13yPzKbA8KYlVXlCfN6CNZKFF94uVS3QCA5LylEu8rZFwnKHBJRhmCW67y2c2DtSzKixRgMRRKZHg_3ugwqzBmL-QQKo5WBlxz6a7CzIpOoNFV33YpVhHJH-hA8XvNV-MtoBvhRlydZVZ80MBPJmWlPaa4W-vzt73BkotjSUZ3iJQQQ43kOAAbDQixT47d7gB0ypWOU4DYiosn073lLg86ujESHPeen1IWmhTGHz0LC81LTZ5UMBndc3NvO_HyAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لبرون جیمز ۴۱ ساله با فیلادلفیا سونی‌سیکسرز، یکی از مدعیان قهرمانی NBA در فصل آینده، قرارداد امضا کرده. این انتقال مثل این میمونه که لیونل مسی ۳۹ ساله برای فصل آینده با آرسنال قرارداد امضا کنه.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101834" target="_blank">📅 23:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101833">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
🇺🇸
دونالد ترامپ: با وجود اینکه درحال گفتگو با ایران هستیم اما باید بگویم که مهمات ما برای یک حمله وحشتناک به ایران تکمیل شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101833" target="_blank">📅 23:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101831">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A_ymFyJ6-gxy-gCCQDS7P3GiFINVUVl9ZCUeLmtUhb1WblcjmPLDVW4xRZl9oIjHDz0x_uL25lcRlxTOb_edkvV-BO5wSs9TFYFV6UamfBhUIOYQlXHNjAiKPub69f8872-90-pTXpLVvHJ6lYe_oQUWVSOU60Dlqovy5txXJSwW5L_UXdgc10P9EM639PrzrYTV44DNfv_L3hKkv4KbWVyFWqB7xm5QT7u6RZVA_SFAT_s8Sr3jpa9Yi-Pb4PL7DbI4lEryQXFt6zA3Q0c0r_B3RG4bfQWRlUWHhk4xZzqhBTKHwtwwPIkOdVjWNjLm4yvBPvWuRR1REvMe_R7uFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IqoAFHX2EPkesrU_kwLM3IR4LCx6ONh6X4sfimZPcxq1qBkjM-Nt6XQbU3T7RnkdeZwbl5bfgIWo-jeLII641TjhjiJBKIIojZPfTGGrg7GzymMvq_bF3bxJIzg8o9jkQu4zvQopjh1O6QgV3qAT6cxBPLy94FjqJsm0HBG0I7-jj6icX7lxkb1UQXzeHT0jIn0cT0hETbBME_gVOEPFv7bN-uBOLJzww4WWuY2Drd6UgNw0iCEndp13l17sMQ3SFv3pTsDNoqyVvRpnEvCcOnT6aiXuF-HOymusKg5QhvTnIJGS9iUUWDDLloXAOlZb5P3Vz03Wtzp6ShhTkKRXlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
👀
نیکی نیکول گفته دلیل جداییش از لامین یامال، دخالت‌های زیاد مادر یامال بوده؛ از تماس‌های روزانه گرفته تا کنجکاوی درباره جزئیات رابطه و کلا مادر یامال علاقه خاصی داشته بدونه یامال تو رابطه با دوست دخترش چیکار میکنه! او مدعی شده این دخالت‌ها باعث خراب شدن رابطه شده و همین رفتارو در رابطه فعلی یامال با اینس گارسیا هم میبینه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101831" target="_blank">📅 23:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101829">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sB3NzRlGsKpU1dovk2-hnN30hYj55ZAa3A-kD_sTWWLH2_a6nR7PwsIfhMvhIh9pYNw6NnPJkBpsgIIqUi4BUAwdXiyK0C84ayLqZ7TmFxpcM9FSXKW1cJR2kPwHYY1nTYreZ6zhvSr_a0xR4eNeejz4m_yf7wYFFS2k9V9Cgw9N_Ado0deEUs4lUOZz73lEvcDtImmq0piKVdQGrOKyv1dnbB2nj1f5D4C0By3ZH3QlaLLFCje6ODaNEn5X8tU0cKFYbwfvR-EbuabR3d8QezEJnHhDN42wpZwbkn8mneyWW7w3k-Z1ijC-nr9eahcNBkTij3wiTs0yZGiWhgIWJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d8O0GqOodaOiWnhEOV1nzkWseWzu97Pdjto_15bySSk6hlCUiHhaSlz5v7PwqnMED22HiFMD5N42WPbr5nttu4-PHu-L3YxX-C3blbsJ_BDrzG1NWaqZGdssJoGk21kGq9rcg3Yo65jNOdjzsREbQoN0Mo8e2OZXjLtjZMsSBIOnxGQpE95z58Tc7pb1lQUK4w58QHb6vtS26ZqTcc7FIpBbt0tYR0qYFLNPg8E3bQicw9NGfQIztt1YXUwvWMcGWhBpLk3lK3BMUYFrDoK04vtN3bexn25JL_U68GQbRCYxMkjzMJTEoXFM8y7GEFikAVaYm6arQOx894cwB45RYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔴
زمانی که رافائل لیائو تو میلان بود دوست‌دختر سابقش با استفاده از مدارک جعلی تلاش کرد ۲ میلیون دلار از حساب‌هاش منتقل کنه، اما ایجنت لیائو این اقدام رو کشف کرد. تحقیقات پلیس میلان جعل اسناد رو تأیید کرد و در نهایت دادگاه این دختره تیغ زن رو به پرداخت ۵ میلیون دلار غرامت محکوم کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101829" target="_blank">📅 22:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101828">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mn9EhdtZQd1F3179u90tlBnejif9Ih8qdX1mE_nqlQNGoVPy2FRaPoTCSxfMyx8cOmZr3PchFLlULVTTDe7pjsf4fSgDbifsMBiVK_YkN50fih0x8Hv6eSMNhWUeDk3eAno-llaqMYehmiGQU22b8AEdoPx4HP0KSYPy7zsZ2zEGt10-IB8PGETzrcQvMiCMLS_Oqw5P1_qLTGo21SI9em14DIA7rfyE6nFKezKu7LxkVRYIr_byBSd8DbxlrMTH0QWi3Bf-RwW7KP22cEyWyTkCitIYkfO5NAMVqHLJtnQh6hcJMETHSJ1lDq3Pazl7OBn7Xn8nyVK0fw5gIvO1NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
توماس مولر در مورد ادعاهایی مبنی بر اینکه داوران به لیونل مسی در زمین امتیاز می‌دهند:
🔺
"در مرحله یک‌چهارم نهایی جام جهانی 2010، ما مقابل آرژانتین پیش بودیم و مسی دقیقاً کنار من ایستاده بود.
🔺
توپ به سمت بالا پرتاب شد و به دست من برخورد کرد. داور بلافاصله…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101828" target="_blank">📅 22:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101827">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mg5moLrcG_pGMqN7iZMuKAA06rdzXvViyGgBEqvLUGzJeWZ_qOoXOikjYRS9eq394YgvCEBOHOa2G2gYMGms_euEVzPL-wc7uY74kwQ0F-UGkUNoH42aFneCHvedKDKa13qu8zzuD9w0wW5PY2MD0B-vVRoJGKtTzCZJlmSLAX-I5SBPsJBz7Q3Mz2pSstyYOKD1D9Q6enhpbC1h3LfFv1mr9kDZuNF1egvApYz5BiqgGyVanpMv55a9o8PMjRO7txk_es3_cOgVSjsPg_bTEZfIai4rkE6CBh9FvRn3oti0MfnNbca0UjvVfIdB-Y6khRdscuwkqd4GO2TPNs_rYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🇸🇦
•
الهلال رسماً سامرویل رو با مبلغ 70 میلیون یورو از وستهام جذب کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/101827" target="_blank">📅 22:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101826">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7qzUnz3Q-mBZAOwHAfgahFVfYzHLWAcfU99sNZd7XNcIe129-6tEW-DvyUsdSeZ-iKcFMlhDmrYuyMErBhfLyeRPI0lP_cP3wYOMm4DU64PMg0wkO94ViEQRFbkCfnexWEKjlGEahbb-JdPMj62QI3TUkGzWQ00_4pJjLsIpN1nZEnVYl_-V7PQTiI2j1WUjjsxv5w2h8EqIXWyBf8T6P9xiFbow0PGdIbvncTVjGiznMKtKv_FaOxl_Q37JctiDy6t9mK7knifkTmSywS-b4foDB3BNrf1am3w8Bk6iauBFcq6GYL0WQEBGXJAsK7zPg5Hj9hkOInaI7B-79pCfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
دیوید اورنشتین: رئال مادرید قصد داره که رودری رو حتما این تابستون به خدمت بگیره.عملکرد رودری در جام جهانی یکی از عواملی بود که باعث شد باشگاه رئال مادرید تصمیم به تلاش برای جذب او بگیرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101826" target="_blank">📅 22:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101823">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSaTNt_u_jk8PRSwIJY0UZNUxAqQ0Umh1Pg9MXvQ58AF74mp7cElPH3J_mXENVJgxZ17PF3ObiJE9gjCV9NgLhdo2a-gxUrwz39Mpu8NyzbuRhccLE4xAkzvfcrsjxcDcBbLKvmikpP9brQsGNkU5loJceh2QczhZ4_cdAT9J68VCoegisIYpU4zrZNNSeEcVbIIl0ZTAXrw98fBYEP3nO7Glfy9OTR3AzSQ5wp5K61N0a9cOf2CGyxy1WdUU3J5ftQI-AxjCYHoiZubuEV96qwKX8o0S1v7EoF3CjF9nqCTy4DKxXpicuqqG79z1wL5hZys3t55x1MmDZaGZVt2wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
🎙
ووزينيا درباره شایعات پیوستن به اینتر میامی و بازی کنار لیونل مسی:
من عاشق فوتبال هستم. اینکه در ۴۰ سالگی هنوز اینجا هستم، به خاطر علاقه واقعی‌ام به این ورزش است. میخواهم حداقل یک یا دو سال دیگر بازی کنم. امیدوارم باشگاهی را پیدا کنم که واقعا من را به‌عنوان یک فوتبالیست بخواهد، نه فقط برای اهداف تبلیغاتی.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101823" target="_blank">📅 22:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101822">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YM5ObBQdA3YrjfOxTa3wRRqSfo72V-M6FNSJ5ek_238pTL0QN0hEkh_fAVhWZ34K4cDrwZuU97Vjd5YsJu6bSarj5X1M9I2hdhPY3ax2aKgXOCEj0Z9dK_TYvcSQJGTyOdTmjLfLn7kGVLCE2Go42jdzqzhMkbra2jID0xplxD-m69nCQmxosbhqYDbZIwrnAnMAfiUMl1HuLrzA5CNTXkuSn9XwWMSyC6JjbL6gXaqhOrBsJkSHAWPgYF4lRMbq7Flna-X9Pi5tkaLSnfYmdSZcDCz9y0GcMgP10h3SsYJbkVS6b8FWm7j3EcLjm1cSVeXiiC_je_01wo_1kl03Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
دیوید اورنشتین:
رئال مادرید قصد داره که رودری رو حتما این تابستون به خدمت بگیره.عملکرد رودری در جام جهانی یکی از عواملی بود که باعث شد باشگاه رئال مادرید تصمیم به تلاش برای جذب او بگیرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101822" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101821">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxEY79kFN7egV6ywka-SNRqs7EbUq8HZXZSqy4SR5K7tXEZXdpd4VQ1PVvChrFj5jcn4h8rNlPxlNQ9v-_cvr-XQ4dkiy_zW6uGvxTozhlDunTyK52x3JHeKAS6OTtSXhCmSyyudcZf4hpTpOZWSFhPn7mCNy3N0WHlsHpVX7ODmVBLRkII5V0g1LRy2vrnl_YvNHCfjMzGZUgmVYma-nFFFL6QuVoYIgzw5Ro8EXnuquerlSFbKBWiLQf3k4ok2g3MWAqdY2Adffj-oT3051ujhcpCpkZecNj29uTQ7K_56sEgJTs6sNLxephgJ8yZHFMzRDTuzTdgZf7yYTJ6uhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
رده بندی ۱۰ بازیکن برتر جام جهانی از نگاه اسکای اسپورت:
🥇
🇦🇷
لیونل مسی
🥈
🇫🇷
کیلیان امباپه
🥉
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگام
4️⃣
🇫🇷
عثمان دمبله
5️⃣
🇪🇸
اونای سیمون
6️⃣
🇳🇴
ارلینگ هالند
7️⃣
🇪🇸
پدرو پورو
8️⃣
🇪🇸
میکل اویارزابال
9️⃣
🇪🇸
آیمریک لاپورته
🔟
🇪🇸
پائو کوبارسی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101821" target="_blank">📅 22:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101816">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oiQfy_5z1IFMFApp8t5GOs25mKu6AAowIC2USSRMKQ9XSGLzYGjma8iT-vHsrrUqvoNNW7mmXqCXpDhrelswMB0-lwyxIUHOumtbNIoqKQC_jqdYm88p5YWVP1EXrh_V4VqOMOQOOKEqjs5ATnjl8HRc_hiahqyU32HoDOvPv97Iid6mq-TFtV4kbTO9j7Q2lIW8EEis8Y7Ys4YbhnvmRD1ytcNpqnpi_RJ192P3NeafBJKLGj7kQB6u5K-kZB_wlExLhSfT-8Tf25IbeueoWW1xoou7r7Gf1Wv-D1b0NJ2eUC9sC01sbGMY3SLTd-sc0-89nl6bLwsBhVuXrmoX4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uIAHhY6XCD1gxtXi7lCJ8EcRFwHrVCNziziq8joaSmQk2WdSg30qjnUiWSQgYmw5hkE1eQSriUESzL3DApM8LRYcup-biZiLHbOkwmQkoNiH1T2zQtMhpbHBqbwQfehSk19jRx53KtaUOFWeCTOk0JKnnFA4NohbcrYobjrYPsbRsEg7nH0Mc8syQ3-qnQ_AncXx6qDknWtzCZPWwylz6rjl6QKn0dR0iIcCwAQdO5TaszmQ_WKSs0aq2reG2j71UQxsXTPoya7_UkqQusMMwiTMVBnv02H9miDGgZN3yz5Uu01p14nb4f-eSR_xzgug-Mq0NnZwAxaugN5XmtlhUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UNxyCxXYyYKv6doIhAKNmlrpnyRjHBW56xFQfQbT05blqs0xBRZJI6TMk-6Xk3XZr-r1E8UXG-qOolSv62nwAkLuYIafA6o2HpGG24yYf-kjaAGuoSeOLPatMegmH5jj4zzInrOU5VGzC0iUgrOVj1c5aPqYvJ85tgWurs_K_PGd4FDQiBUeDBadJj0_-txpWs50s4Np4Y85SCQVYwqrLuXAFUmgnx91zIAN2iwu0tdArTC3xztaxr68nbjELA5rGLYoz8VFY7t4ALsCNN4NT9Kk_SzZ0zSAOnEunDcHhg_uO5NTYpfelUYB4GvhDeKfxqeSVJR2eAzxHIQBGjgmig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lpGGf89ht5sQf_CVIo6CCIDxQGzmZ34PjkpNoT0Xv9-3TC-z5icFR4osITzxwvDaJKIjav7iv9uDb9paa30oQpCsWE-4vJlxhTF0gHDVhmerwmLusbJfpB6u5HNXHpK-J18BYyDvgyVsdqfxmmJQiACQ9If5uVqzbroD2Bp2wM6QqE9rp8K8sTOG9EynvYdIMsaSZDMO8juuaCexgOyABhA2cAB0_5NczJyKaeMsSKQL5KGvRFs96lY8sXZELMmNfXtjjDz5PHscuYAHfShEC-k6Y9xQbvgIKF139EMfCoLdf0DFzvZMmiVGZVz87063yQ1RDlgQNr5pH7SufVi8-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CbB11MHzFHRe5GP4HO_J7Ad4aBfc5iDgkIYpLeQwClML7044uYc1tObn31hcr4E2E-E74-xOHxY-4799f1tJuKGMHHOj-5Qze3w82mfdDRN_WSAe99lPq2li4jnMf6Mj1Hx2m52_efbDeBUeKMrLqgX0FTXvCOgGiMVltICIzmze2J5w6wcSV-MzPYcUiOUoQJayvEWDmcnNFW2GGuvG_ZIBAkgY7jgQW0TiHivKSYhvKoS3Wi5yS8kQIrDH-R15gNfrJiO6JbEaaCGH6X63vQpj8hMqfVg99BzWLO9H1B-Vg6pb2ki5DtCyzRo-1uxYRMVKtzXpl4JQ0jXJRaEP5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🌈
🏳️‍🌈
فران تورس با مارکوس یورنته رفته تعطیلات
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101816" target="_blank">📅 21:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101815">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1tpzNSLmoeHXYg97U-zGPNAIFBWAw7_nWK6vnVsk_lWq1XtOiYTzJRT9gK7Ly7L9njdc0AykuqEnVN1Xysm4-LA0myT4aYoUHuGp2ULLiXbMihauZaAt-BiHfzSs0Lvj1xEfGCwCurtsdXImldv4JcMEIatxheW1friKke9kvazg3qCVYn8zICJtAS3NNXTuGcl_1BSYrKIzumddqazR_z90hVkVE0ur5BEN_XuvJpNmaHyb06IrjbqDzQ6AswnJ_GsXsi2g4EyA063kQDDJAIbnXYu3OZtcYyceszYLZuIQEMbOBqTrfNJEGK41S3M22o89qHmVTiKq_lA5PtlSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
کریستیانو رونالدو برای چهارمین سال متوالی پردرآمدترین ورزشکار سال ۲۰۲۶ معرفی شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101815" target="_blank">📅 21:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101814">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2I75EUoursg-3emAB8-1b4f2I-jBSeDZiDenDSkHW228-oRb6XCZVEzQGXraw3fMg_2t4vQj-r0-bu2Nm6rewATDUH68j6sSp0bDhnPqaTB4aw_SCL-tyWkLfHk_kv0iYAN8vzBNFvlonEVtBjZ9yvfWDtBjECdkodB6RpiYLC8FfAFPRoZzZSPfqoBcslyKHUGPgUsjgqErX-o1mAtynHSeVaujJDLoK7wNFsWT3n_4WyXe0cTm7fvU1fJRaZ3mM4hVwil3AelM-F6YmafgxIBrwIx-KeXDxSV0_hx8EtPHKcUJMIP1CKii1GDsvDBl0-5jtnLUSvwAQ7sq8EUgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب امشب بارسلونا در بازی دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101814" target="_blank">📅 21:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101813">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxMsyOBVHnEHERy5NB7m0EScBEn7QM-gVmZfBjlu09HMMaWSzLJt2BRN7G7HvXgQL_5G1Gz2l6-RFHYveH2MdPe1RUUREKykh-QUufL-pjy4G6DfR1TkpMVWedEdqPMNYDcuRnEz0vhHPIlJaILuI2Ygj3eELlu30YwvzFkQtDAh19UmWZyWhgYJlL-IP_3tOVd-oF8txbRavbJjnj2n5HPhwBoSPosSLlzkamYWf8nR37bHO09jiJ_DrTE53oxKqjUMaUGQMUIVBinSVpuRfCW8KA7IwBuB-swl3kVy5OOfhmPP8RLgId4WO3T0G_CaiGtETUstHrqjQ7g2ApVjOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
کریستین فالک:
‼️
بایرن مونیخ تابستون امسال مایکل اولیسه رو نمی‌فروشه و بررسی احتمال جدایی او به تابستون سال آینده موکول شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101813" target="_blank">📅 21:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101811">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jLrP_RcV0JgrE05G_qWUu0i3dszmL2Tn_SdKVK9ZXMBoZ1eaeHU_K5Hp6fDeT69sHEcSVkPI3sVaN19zR3JfMizx_oPyzerunWpSzIzPZiBtid-OkQCbfYgnnxy_xkoDyfGWxxlNENALbLwPn3x5oLKjetvdspmlwLaoXDXypqoJLbm_DMtDAvXU4ByCreYyG0A94FoJs3H4KDWjXzTQ8GLp8Ym6D5Jxryw-_zBryWXJkFmlzLFmWnte_cBVL8BhWaIypcGXiuNKcORAQZJ0aq4SBqSPcF_F4h4H2ohY-iCxYwuXMxP_sgoE4qpERIX6Fi0yt9f57Cs9yzEfJwzCBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h25mwP0gAmmNoleuTmy3KMlMpPEpLzj7rQdqlCB79oUWJAdXp3SHGYdAeoHTVbtkQn97nE0BGcQphVrdgFIetTWDcmixrmTMhJrSKZwOMZEuUqK0OoKTL2cNjwRaH1ZMbJZZJOrnLFrAvzW09Nrk1UQStSW74AP4FC6n3ipl3u5Q88s-ovO2ga3AcC1D76k_QFO-hK-ueE_CmGaVm0ajrqtCmcPnuPwd8bjf2P5Gi3WpDqpHFW9sG4HBNcPQfPX7wI4Os669NvetB05KtzqcfbnibQhEyELMRs2c4Ew5dBFscH_tnQ1OQFpYHTuAqEoXyxIP-ZeMEDPmTAVRPGY66A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
💎
۹۱۵ روز پیش، پائو کوبارسی اولین بازی خود را برای بارسلونا انجام داد؛ در حالی که تنها ۱۶ سال داشت. حالا او قهرمان جهان است و ۵ جام با بارسلونا کسب کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101811" target="_blank">📅 21:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101810">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a142d4e6b9.mp4?token=LHKENAtqohsm2pgvAj3PH5LgxCETigkhh_aaoLzIy3SF_xS8U1wM9ylTXsijtqJfdp-dNEJmn9eWWnpj9sCmID-AF3CDKRXjTU5yT_W1-3aRsaG77Lc46AUp1Rw0vCRUOMDquf5-7jzUoh1zhQbIGeZVLd-y_b13laivYUgA6YNUjvux85TI1EP9khr--F36PeSSzjkk3HDHa2oSKXqmNzXodT8Igc9vRR8GkTJYmOIbyIQbCiq8lB-KJwm2O0HYLsda3N42bHN_cT_pP93KtDfX-Qknd2w6yM7GK9CfwJl3p82sCG-xxS-jBq_b-TdbE4Sg-pAsEiJfQMEEz9Y33g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a142d4e6b9.mp4?token=LHKENAtqohsm2pgvAj3PH5LgxCETigkhh_aaoLzIy3SF_xS8U1wM9ylTXsijtqJfdp-dNEJmn9eWWnpj9sCmID-AF3CDKRXjTU5yT_W1-3aRsaG77Lc46AUp1Rw0vCRUOMDquf5-7jzUoh1zhQbIGeZVLd-y_b13laivYUgA6YNUjvux85TI1EP9khr--F36PeSSzjkk3HDHa2oSKXqmNzXodT8Igc9vRR8GkTJYmOIbyIQbCiq8lB-KJwm2O0HYLsda3N42bHN_cT_pP93KtDfX-Qknd2w6yM7GK9CfwJl3p82sCG-xxS-jBq_b-TdbE4Sg-pAsEiJfQMEEz9Y33g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پیرس مورگان:
چرا نمیخوای ازدواج کنی؟
❌
🔻
زلاتان ابراهیموویچ:
چون دوست ندارم 50 درصد از ثروتم رو از دست بدم.
💀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101810" target="_blank">📅 21:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101809">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkLjAod6O8SewaTSWRTP6qfh0NQDwjJNoJd4S1-vy0ZPA3hw6KS8lplgT0PzH3XHXz8YDzTcpdO9b4msmM9VVvSBvudXew1HFPS8kP3aMM71xqw6Y5UxutWHiBBu98-i3s0nDboUazzBIu_9iWEONhFqvr8KcJ3GlXqCXZdoCQRMM5HdXoGtM3msXhAPNbgljOzWG1EQ1P2Hk81h-wA2Hpy_30DxV-fOS-iZFkDh-VBwrqKdpRDw1dGW7w2KEX_KhCBd6boreT-ekcCjX4H6DH8Mawal8wCyZir0o0uhte6v9QNaeFyuaSamtqaJhbPwQiQFHYvxVXRND_ad1kolPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
🚨
فوووووری اکبر عبدی بازیگر سال‌های متمادی ایران به دلیل بیماری قلبی در سال ۶۶ سالگی درگذشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101809" target="_blank">📅 21:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101808">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAWBL5uhZwUXb6YK5suE3FV-_9mOXziQ3opArO-1v-2OUhB8JYLjpXMib1DGOjUd6Ns6T9Vf3QMOw2-FpXgyclrbC6_ViGf2uzdWflg6rRa_4DVF5TPm4kqhUsCTKG7KcGO4jze-_DgNirFrBsgYvGoMkJTuhZm2oRKoZya_AbZa5aBJlbOHR32A2sxDZyU3HQOzc_x-nEa1uXRR6OGOX6P-vbp2Fj5amP0sSsQLYPyxTW1cUnZt7iWCxuBwdUc0JtYuZVqZSghvHR2vhS7pw4jpdDoj7xzle3y2ozS5wbfCjlpQiV8R9zGmjoLDWyJTNzht7_Rb7IXTDN5EYVejsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
کریستیانو رونالدو تنها بازیکن تاریخ فوتبال است که در ۴ سال تقویمی مختلف، میانگین بیش از ۱ گل در هر بازی را ثبت کرده است.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101808" target="_blank">📅 21:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101806">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmNETFck4aVesciB7V7KjPFM_HPs09Xc7tTxMe6hBVBDkEuvgdqyqzaRpknINxoJLXbRVwGOJtc4AzApb2BATEfZMcGEbZoWv6jRTQpnbmq7B4dUFAok1G0uDkdHfFAbX1B_owtiaj0eM-GR6GqvOAHodPuhBwikde-sBzHua7nhZV56mPJkWSNSQ-XzAKykYFOkrZl0Ymp9ZsV1XPinpB2Xi2ez0Dy9uhp-RRYfBFkp8jgNZk9q9HenCF-xuHK2cIybHp-MYLptY3c6w228OWNFqMzXeQyls35tm892Z_73J2pxeDeexe8X4-gs9tGUoXAhXjK559Bi93kkqa2ZWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a81621b4.mp4?token=MPywpIXcEFaVWOAkDqxyqsywa5bnuhEHUuiSbqq6gQQLsFd1HTkJtfmJVHXWO3b2ibMaPZsKMpLWRks7roWTydB7jUv4O16kuTT9xhQ0l075Kugnlehtb_rU6aO1k0t50OOJbt-GYlO7ldh4B8ZdAIjlFNSq-g9QaQKBuCGhTNeSmzx01PAPkGd9eCz7aO2gWjXh9egFlsgtaZ_RXfHe67vLxoKDFq5BGWfvHuOfPndpCMejuWHL8DnpVI8RtkLS5GwinxjdQ1S-uJZtVpYRjDzIevCP1Fh0QCqxh1BZEtvpgyXo9FWUdY4VQH07LF194Z0AhJrIVVRtGHccqTcHUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a81621b4.mp4?token=MPywpIXcEFaVWOAkDqxyqsywa5bnuhEHUuiSbqq6gQQLsFd1HTkJtfmJVHXWO3b2ibMaPZsKMpLWRks7roWTydB7jUv4O16kuTT9xhQ0l075Kugnlehtb_rU6aO1k0t50OOJbt-GYlO7ldh4B8ZdAIjlFNSq-g9QaQKBuCGhTNeSmzx01PAPkGd9eCz7aO2gWjXh9egFlsgtaZ_RXfHe67vLxoKDFq5BGWfvHuOfPndpCMejuWHL8DnpVI8RtkLS5GwinxjdQ1S-uJZtVpYRjDzIevCP1Fh0QCqxh1BZEtvpgyXo9FWUdY4VQH07LF194Z0AhJrIVVRtGHccqTcHUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تونی کروس، هافبک سابق رئال مادرید، بالاخره درباره توییت «فوتبال برنده شد» که پس از قهرمانی اسپانیا مقابل آرژانتین در فینال جام جهانی منتشر کرده بود، توضیح داد
.
🔺
دیدم که خیلی‌ها از آن توییت خوششان نیامد، اما همچنان پای حرفم هستم. به نظر من، یک تیم واقعی فوتبال روز یکشنبه برنده شد. همچنین معتقدم هر کسی جام جهانی را تماشا کرده باشد، دیده که اسپانیا بهترین تیم تورنمنت بود و آرژانتین نه‌تنها شایسته قهرمانی، بلکه حتی شایسته رسیدن به فینال هم نبود.
🔺
به‌خصوص مقابل انگلیس، بازی خوبی ارائه ندادند. آن‌ها بیشتر مسابقاتشان را به‌خاطر قضاوت‌های جانبدارانه داوران و فوتبالی که مدام با خطا روی حریف همراه بود، بردند. به همین دلیل از قهرمانی اسپانیا در فینال خوشحال شدم و همان باعث شد آن توییت را منتشر کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101806" target="_blank">📅 20:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101805">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9frj4ao7asbKl0VxzafPVseCqgdP86vZlpMjVC5UPHeuuiirV8boMUzl7pX7e1ZqV-hF1BKzRuZN2qDyfp7t86H-rBvqVpDx_Wo0e7DHEfUKUM6KvwLzXbKliOes5ywFiyweACeNktxN1ZRxg2TRIXvuFCEupntiZa8vchBS7vQ5yzAxeUJwfelD1rLLlJa7IY7GLqUtxlCJ8A21cRYMeLG3-uz441BciedwFHwpHxS6suiAoEuvoOwmXWlS9fRU_3TxPoGSJfxmV63QtDjiAiVENAtbBBQG2Fmq4TEFPvm0jcVt4lCsS2NQ24dMjO3uE2YqmKW57_1hz11xHNTLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لیساندرو مارتینز درباره کسایی که از شکست آرژانتین خوشحال شدن:
سقوط بزرگان همیشه باعث خوشحالی افراد معمولی بوده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101805" target="_blank">📅 20:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101804">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/et9TG-xLlIW506KDyozYxPl9xt39QEMIdaGZNwrY5-X9LICazUlSkTEhm1wgaZzLLYaLmwK9fsag_5OgBy0xmIsnWvVjdWq2vlU0Hj5lmkaGZuinMt-XOEImaB3aI1bEkbbe99_kw2DrK8eAp-bCIhV6Jx7769RFDtd83AaXqZW6oBLl7vJhGPf2BZdc2FAvmFHSVUA6MyxttiE0tkeOyKUXQ18kB6pUnTEGkH9H8ustV1BDj58wSU1q6PVt8B3k7qowxb0s9iSHEneO93dJEr5uUvbVODdEO2XiF-NE6z3Q1Fp6A3HsuyKWOkOoheZAAOpHlKoxBK_DNdy0OvRGHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
اسپورت:
فِران تورس از شرایطش در بارسلونا ناراضی است و تردیدها درباره آینده‌اش، احتمال جدایی او را بیشتر کرده. او احساس میکند هیچ‌وقت گزینه اول تیم نبوده و باشگاه ارزش واقعی‌اش را ندانسته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101804" target="_blank">📅 20:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101802">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HaUJT_mSXkMYIz8gftW_cMJ2lHs4v1z9q342Ykct803RtYsnn5_3geKohcBr6DMkYxmI-8euo_0CoBDR-OKdsLsrMWFvHPLFJEhcc2tVhvcn7GCdw3wEZJrv3c_q7EefPMwEK1R_zzkUvo6-g-WcwPA6papWQu6_x5mc8zHRSDSUmIuroKZVIdVktD6mJcgxdBQPfXestKNHSt4M3k3-rxv1PhRxJbRgaVuGHp53Wc89Fq0uFg3MEoMZCSD7JlrKHfsmPthw6wxhMz36SLBCELDbJouDZIJ8fl0PyqYMyTEBjgaG8j2REgN0l4dk34s-ZJ_asgXiq1OGU5aaki7HEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g9bXA2_zveLnie1-Z6BlKB3x7pXIKnu5DfS84ZgJilAeLh-nCFLN6wQZKZFf6AsvduncmfaX1XOfvDMq1YcCQUz5lv5b-tF_Mp8UQkpzBn2mAgZObPGUnP2KX66EuTzOOyTjV5b4LDjO0wZj8-t_Yrr6WHRIK55UlZQsSnyxFuaOfVvNIbrvHbidIuPOww1Y0eJLvAhk5ldVdbbkFs5hd_y11xC0h4oyCDTxGcz3pvgzYNrSKQ9em6SkQBdkILJ-ir49zypOqEQ4JPnaTd_Fz-thxxPj3JLCoLJ-153qBnhXeOTpic7F3_aruJxfDqdfXjmqjJIMUHrHpGs2YoY6UQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بدن سکسی‌ای که فرناندو تورس ساخته.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101802" target="_blank">📅 20:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101801">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8sfmMQ8pa8ZhkPiRLfniPg5CGoH1vmqHW82EyBvpbZVlzg6V1LgXp90JrUDh8HW7LPJ5uUtpdvvdtqPT_PKsyBOs9TENiOXg5wZT8cwn3LOEsb-2OgiNTlRnA7kTxTHjSIeaCO0oBBDqK6WoT253znxRHQmt3_3fk6bneVxHIQvBm8wfq24EBlnXFVqztY_eeOroaJ8sKy87gPz29HIcuIyVqgyh2zaeQ-0ifRN7580XqEe9srqsmtqcNHb8fClYZnvERq3FvKylJo4vmEiuSMpIuU6IYL9K4-ORQk7C69sVRwOCGCqOkkV44E-MtcfYEJrcej6FeroIFsvKpyL9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
لیونل مسی در چندین بخش آماری بهترین بازیکن جام جهانی بود:
⚔️
بیشترین دوئل موفق: 60
🎯
بیشترین دریبل موفق: 28
🅰️
بیشترین موقعیت‌سازی: 25
🎯
بیشترین سانتر دقیق: 20
🥵
بیشترین خطای گرفته‌شده: 20
🚀
بیشترین شوت از خارج محوطه: 18
همه این آمارها در ۳۹ سالگی!
🐐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101801" target="_blank">📅 20:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101800">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgyZUcdIdo-559GLC6bnVPkGBRCEE5VKJZP8S13QjR8vT7S-C-HBdRzwzTK4hath3-oVsYanwIXU5qgg9r26Eheys9Yy6P-5NSgzXWKSPJnBY0s0rnO1nA_LmuU3gCy5JEF_mmQJKBPnQJbCfjI4Yz2D9Mx8O2A1E8Clu8WPgrFAaQjYqTBRV2K64Z1ZD6Bn4G9PhxBsyobbj6A1xF-5lJo347X80UGr_LpJ7G59IiC5_pSIuTUAaYzDtAxbZ-bCLyrRSthKWYRO5qoa4WgSG5rRsayUgJAJhsx6KjQjwZb0T2UjfbJlB85Ek_ELBBn6qT1yH1U-xqT6g7o89i5VPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
✅
الاهلی مصر اعلام کرد که روز ۱۹ آگوست در جام خوان‌گمپر به مصاف بارسلونا میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101800" target="_blank">📅 19:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101799">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQLl4sKUHMFL2cGqc6zO86nq1-_JMJ5J3yAER2PzmMg7sB3VYhCtzm1yrc_4jME5wu1w2uNaXKzlsQH89WqVK5gk3Q22qBslnRQXMZeyIWaSowdTO1upq-IozuIkH3zFH6FyoV9yH-oPVLbsHuOdLfyit7TbGCRDIw42GPuuAQkqIMZUAFljDGaqOQDhGXFvQyRjmTbUr52HgJCgfjcJInNjuT8nxpmMzmaxRmoQY6HvA71AnrsAOBZJXW42DcoRoRtNrlBTCNij7J2FZQG6SgjAwx7ApSLqcunV0baJ44rMcpkVLjgtZrhZ2Odswv-B9YQBfuqIzXkNnAdHxpUsCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
لئاندرو پاردس فقط ۵ روز بعد از بازی در فینال جام جهانی، با بازوبند کاپیتانی بوکا جونیورز در کوپا سودآمریکانا به میدان رفت! هافبک آرژانتینی از ابتدا بازی کرد، ۹۰ دقیقه کامل در زمین بود و حتی پاس گل پیروزی‌بخش تیمش را هم ثبت کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/101799" target="_blank">📅 19:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101798">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a03QsOQil3s5SWL-Jy5mhqUoU-xz8W09bvh1bdY0kr7tweI-r3xNscl_A852xDlA9383hdMRhpEeAWOZrfRce6F84-Vq-hkXbOiclo8R0iP7xm1E3xGjPcxbZlI0FZ-SrObzgp9Gr41MD0j5kaif80RvdalrE7MNBr3jZzWCTk-RfjN_WeVUf2hKxmWDU82v1dlZG_2K38x8rvUVRZgw410PkPOT9XRJyYe5lCOB0qa3wFLLZyEtajARaPywoLuThse7kj6rKQjlKO60CZjtFpQfk6gV5TZ2tvcoeaS0A77xrMyyb6Lsw1atUSqxFRZ5bJHrwg0fD6srACFWVpzkpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
فابريزيو رومانو: پیرلو به تیم ملی ایتالیا 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101798" target="_blank">📅 19:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101797">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L377ZtVukJOQNzJBvCG2ajxyAKIRtLynwDsuD2W4pDeP8he545PxxCVlqv-90VAdMbgpaoFDMIez8ujaYHDKGIAgZfAEh3aszPshY7cDGUfWIMx7Y6ydzK-Tv7oWX5QECBvQHncktVhYEH1sf2eEVGlynIMFIykWGR0CSJnxF2PXB5-3e1-awS7kYcPm3_lnXOZ--fTRuXpBi1reAfVqmAdsTR7-NAqz7J29lJpG5Aom-3bro0HSVi0NweuIk0AHyJu1fU3f6qvT1fKa_Abt83BZq37NlQxPiZNZtnDNEOFByZgTLTfgaJnKIyvzxv3An0NwjPylzG3BYiU9jahBlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بالاترین امتیاز ثبت‌شده توسط بازیکنان لالیگا در هر فصل از ۲۰۰۹/۱۰ تا امروز (با حداقل ۳۰ بازی):
2025/26
🇪🇸
لامین یامال — 8.23
2024/25
🇪🇸
لامین یامال — 8.01
2023/24
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگام — 7.81
2022/23
🇫🇷
آنتوان گریزمان — 7.69
2021/22
🇫🇷
کریم بنزما — 7.69
2020/21
🇦🇷
لیونل مسی — 8.52
2019/20
🇦🇷
لیونل مسی — 8.71
2018/19
🇦🇷
لیونل مسی — 8.48
2017/18
🇦🇷
لیونل مسی — 8.68
2016/17
🇧🇷
نیمار — 8.52
2015/16
🇦🇷
لیونل مسی — 8.46
2014/15
🇦🇷
لیونل مسی — 8.84
2013/14
🇦🇷
لیونل مسی — 8.34
2012/13
🇦🇷
لیونل مسی — 8.83
2011/12
🇦🇷
لیونل مسی — 8.88
2010/11
🇦🇷
لیونل مسی — 8.76
2009/10
🇦🇷
لیونل مسی — 8.65
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101797" target="_blank">📅 19:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101796">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqh7PV0YJTbZCz9QFLsJxpjY3ob1XWDiDT4XFBL_GGlLDiIOoGkt7wyNWKhSBmsZ0iMR2Rm5_iNmU5mojyvn9G8yt3JoIb-Du5Ee6FkBdaA6W6kxNTXeCb7whfEBmn0qY17u9dg-i4_CEyomi3Qe84MwW4cLri-itCoURi6k0LeJA7rMOR4sHSHiBXv76sA9RDGjhrCZNO1tmYdYALYpi9CObEJxqTiqPJIjKI9sSYgwWY-gDuj3_Uv01_jAo1TWAGiItzezS-oZevDgwnLb8864I4ZgOI3SVf2iWBtEYRfqM7mLFYpEfjCetrMqZwftma-aJRn_4Nq9VDuOpagtyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💀
مثلث‌خط حمله فصل بعد بارسلونا: GAY
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101796" target="_blank">📅 19:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101795">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xeu6kcLSCu7k_FpqISalUGrhFkVZMve1erSdY1pC9SdmSeTS8myT1dgGc9JkG-dJfsk1tcUHB8wBmedJWs8p15IX8cjz1v6hLuzW5NvqRKWE_H_CvHODuz1MoOJF6wSAZikIZ8BgSivPcqYeqT0wzRt4-AOCLJphhfeK3NComZZDUENB0SSJ6p3qPbRi0FNcT2BEKvNYyTH5bTJeoewhnDZjrcLZWX4z7uq9VDm6sRAzzYUKoOYUfntPsyLUoiReH-iM9SwYlMx16omAsWmqJYqpUfVcdgK2-EbaNAAyCwvMtiO_F9qCPVydt81KVupuGS8vbhuDRL2l7FzSvM5MuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
⚽️
بیشترین دستمزد هفتگی در سیتیزن‌ها.
💰
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101795" target="_blank">📅 18:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101794">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1da4d2bb8.mp4?token=KL06BCIMKu4IL3oP9i8AYEz6OofgHCQljYduq--Ojl-GsLrNZRYIg7PSpV3b_CgJtLIQsmFRmzq6dwZ2D9rJW7a6EQpmr5JI-rbjCJAZMI1ayBbIKcJcUROkrxc0-Nmmd42f5hOroRYuBEBYjIVt5VIVFAzs0rY0g7Y3vOSUQIjnMP2fmYVOFQLoemublpCxU2cYc8V4Pk9-2AL1wu7ODhyUDOUQPer6uD8JzX9zbebWK4nQfYZspR5RpTBx09Amb2asCg6m7wAXC_ka4vYi3N20W4tVkmtlV8-M3IEbJ_gOz4-OYyZKNzMnJMKQIUfl_XOBqqwBwknrXV9TMBl_pT9ThxxO29FDAvdItCdVovNAnbO1L0D5TCdZHV5pYy4SkvEpaL8jA5JDzijTDNKzW1WA41x60l8PR8quC3nzrubPpjecf4z_a1jWzgS1_9pqO-4vc6vyym37-vj-ht7RkUITFWvXU_wqUzJynRJlT6EYYCZsbbhRL5JOUs-Ye750_7kz6A54gONsy7g3NgqCc5GzUqs7CvC3eixYAb2xEW6FK9o8OnhibWF4B1kIMTLu3VGWaSpFizvVC3bP4YKWhPC9xvJJYzxoyWpwcwVw_-hpncopEF7qQgKCZbJyn8ZHkqpzxmBNGcQU8xbL2FyjYGjl7Ql96RzIRJcv6BGa3js" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1da4d2bb8.mp4?token=KL06BCIMKu4IL3oP9i8AYEz6OofgHCQljYduq--Ojl-GsLrNZRYIg7PSpV3b_CgJtLIQsmFRmzq6dwZ2D9rJW7a6EQpmr5JI-rbjCJAZMI1ayBbIKcJcUROkrxc0-Nmmd42f5hOroRYuBEBYjIVt5VIVFAzs0rY0g7Y3vOSUQIjnMP2fmYVOFQLoemublpCxU2cYc8V4Pk9-2AL1wu7ODhyUDOUQPer6uD8JzX9zbebWK4nQfYZspR5RpTBx09Amb2asCg6m7wAXC_ka4vYi3N20W4tVkmtlV8-M3IEbJ_gOz4-OYyZKNzMnJMKQIUfl_XOBqqwBwknrXV9TMBl_pT9ThxxO29FDAvdItCdVovNAnbO1L0D5TCdZHV5pYy4SkvEpaL8jA5JDzijTDNKzW1WA41x60l8PR8quC3nzrubPpjecf4z_a1jWzgS1_9pqO-4vc6vyym37-vj-ht7RkUITFWvXU_wqUzJynRJlT6EYYCZsbbhRL5JOUs-Ye750_7kz6A54gONsy7g3NgqCc5GzUqs7CvC3eixYAb2xEW6FK9o8OnhibWF4B1kIMTLu3VGWaSpFizvVC3bP4YKWhPC9xvJJYzxoyWpwcwVw_-hpncopEF7qQgKCZbJyn8ZHkqpzxmBNGcQU8xbL2FyjYGjl7Ql96RzIRJcv6BGa3js" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
▶️
اشرف‌حکیمی و امباپه در کنسرت بد‌بانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101794" target="_blank">📅 18:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101793">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b632e2b27.mp4?token=Zwyl4v3t-lRc8a2az1LfcHjajAvGCooOBYw5cOqXvJ4_TsG7vZMzLL3bN64M18j0kQHzK_pxTY8SgeUuuZbELcEHJwQ_Av0hBogP7CvwxSoYi2oDkl78CGTuMurzClxcLQebfliPDUVKRVn4j-rgw2LDEa4lb8JaGRq1zbVd-omusbsFL_hjRtPQy6kuD_E8sMU2rbUFz4vXdHpXYpZbmaZeATpI1YIckQiWW3wOy4B4gNuWr4mAtEni79vuAvMCOgKgudHAeeuruWEbRBZTimkYw9N_R_oOzXykUXyi5yDxW1E8srVlzPCSQkJwAU8byZMxP0leOd2VrtYQ4Yl_ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b632e2b27.mp4?token=Zwyl4v3t-lRc8a2az1LfcHjajAvGCooOBYw5cOqXvJ4_TsG7vZMzLL3bN64M18j0kQHzK_pxTY8SgeUuuZbELcEHJwQ_Av0hBogP7CvwxSoYi2oDkl78CGTuMurzClxcLQebfliPDUVKRVn4j-rgw2LDEa4lb8JaGRq1zbVd-omusbsFL_hjRtPQy6kuD_E8sMU2rbUFz4vXdHpXYpZbmaZeATpI1YIckQiWW3wOy4B4gNuWr4mAtEni79vuAvMCOgKgudHAeeuruWEbRBZTimkYw9N_R_oOzXykUXyi5yDxW1E8srVlzPCSQkJwAU8byZMxP0leOd2VrtYQ4Yl_ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسی همه چیش بهترینه، حتی میم‌ شدنش.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101793" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101792">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e74ccace70.mp4?token=AmoriVTeMDIS6XGx8_b4ki9mc5DMLqcnFOW49Vj2zOhsmzDcbEcBPLrVnsCLneVYtTatDIhcOr9s3ov_DwbpDA9OT-L9lA1Gvr9U9CQq4p2MfrIb7Uowf2To6rMH9lH7dtopIQjeYM2QeonPeZA4X9H8WMb2otmRl8iNx1OwW_GpOs52IY2K6jmrR0YiW0ZST0nN9rHcuH9p3bDq0ZQE4KkGqGTYXt4J0ZiYL1DgHh8TGpnR6KyJyOZFU5iRtVSQfCsXtCbjWFxS8uJg50nwaxsbP5egsdfTrIPDx-IslaFvkCihfdi-CEKMbypETdg82a6qy5yWeyoxFBQbe668cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e74ccace70.mp4?token=AmoriVTeMDIS6XGx8_b4ki9mc5DMLqcnFOW49Vj2zOhsmzDcbEcBPLrVnsCLneVYtTatDIhcOr9s3ov_DwbpDA9OT-L9lA1Gvr9U9CQq4p2MfrIb7Uowf2To6rMH9lH7dtopIQjeYM2QeonPeZA4X9H8WMb2otmRl8iNx1OwW_GpOs52IY2K6jmrR0YiW0ZST0nN9rHcuH9p3bDq0ZQE4KkGqGTYXt4J0ZiYL1DgHh8TGpnR6KyJyOZFU5iRtVSQfCsXtCbjWFxS8uJg50nwaxsbP5egsdfTrIPDx-IslaFvkCihfdi-CEKMbypETdg82a6qy5yWeyoxFBQbe668cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🇮🇷
عباس‌عراقچی وزیر خارجه پزشکیان: توافق با آمریکا بهترین توافق ممکن بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101792" target="_blank">📅 18:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101791">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWjd3Y8_H1GUzD5PDr89C0L-toPkiM04j_Wo7V3oU6PUrPMVQPjN0a7MaSU-ixQkLPBg0zP4TijX-lMGJEkTWOGwTk_gjLcCLwcbQ-6XYG1LM6vXS44CWQbsMYW5w2eyV9Y0SM0JgBZtdioPYOwx25UN88rERb2klPz-UwbFd-bkVVol3lQqLOtUVJEbq0BbuhHbJynwrHOlZnGxG7w6yFId7uNP32HQIoCj61w6os0En6TmiQVIFvJN2nfTgEZxEqwH5UMhmLAYiPIx5o6VR3oZdt_p6v9_96xRaLkV8XjDQpRUbclJDPsxOvZTZzwY_sOfQA6WZQKvl6N3iW7T1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
💣
💣
💣
💣
💣
🇪🇸
خبر فوری: فلوریان پلتنبرگ: رودری اکنون به طور رسمی یکی از مهم‌ترین اهداف فلورنتینو پِرز در بازار نقل و انتقالات است. مذاکرات با نمایندگان این بازیکن آغاز شده و پِرز با این انتقال موافقت کرده است.
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101791" target="_blank">📅 17:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101790">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👀
یک استعداد دیگه در کارخانه لاماسیا درحال ساخته شدنه؛ سال‌ها بعد اسمشو قراره زیاد بشنوید..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101790" target="_blank">📅 17:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101789">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXpn0J8GN9y_CF1Aq4af1UZuxu6xFdBh85vHAhR4hhvrT5dRsEwjbhmk7l9XoNrqhcFBhwdlFflQ6ahOywzxgINv_FqzCSx77mZ07odQCJgx7GjI1DNNwN9m_Fv8Nph0oKnQKLA_48Zc4eW0yqaAvEC8Bfu1lL80vwV5RRXAUMJUr4MJD0VAQDrfiDO1hPyV_3ex1Nr5uAsWZ94D2ougODDhu8LOMHZDdjSPy9XhaWBFXSpAS9E6A7kch-Bn-jHfLcJ3hZLUg51Eukn_pp1PcoVpB_t6BA4Iws6slpHrQFVg7MYQ90JJu5dp6Te-2tUScytMjhpMINSs5mMdUc-nqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
✅
رئال‌مادرید به رودری اعلام کرده که مشکلی با عمل جراحی مربوط به مصدومیت غضروفی این بازیکن و غیبت برای چند هفته ندارد و تصمیم نهایی برای عقد قرارداد به این بازیکن واگذار شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101789" target="_blank">📅 17:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101787">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NiYvkGpb1ETDIzb3xXA42Kw_pgkZXI9ThOxa5DfzYa5g4HAr1hA5Nxt1Mak2OCEF-ARCuDRrC1tGqsfEnq65LCRXxMWcnaYlbdKm2lAhgNcgU6NDIzkOc-S7FTN2BXx_1Z6csQUaiqqGwHOiHMjNC8t6RZSlm8FXLF35xgWeqP4foykxNDlANYCYmjJMPIA9tUFVAf8si6ABKHwsDIkxVco_8qr8aiLwKtg1QrqkDrGF_D-oBkrBot65KstZnlZH8SKKFaBcnB3oibOi9YsmlKxNnTycM5bqQlEOGnopIu1tEjUu8tAHldDVPusHXNTt6VLdJTje1_r0Ps8lw6YDhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/elXFfHMJqghg_1vvrTAlXV8IOic2-CunNSJPGzKVQxXnPbuYT5rcf8j_wTE4XguBxQKvk34UyzV6FNy2ZCQH9NsUpyqX3_dl9J8dFTq60a2oZobGYxz0vFadcZde2uyE8iTmNwCW0poORVPJgkWPTdBpyhM5_-tkuGKBt9-1bLPB7R7qewTpHGTZyt0YUhu906wK5CHIv0JxQC1yECKh6HUjsNgL4jkQ5uot8RYuv4LECPnGXyBp5zZPKrZR3tE_hScxOhdPA7jSlt0mmuwQuWGINT5l3qVA1m4eTgtXZq6uGnA5LQVsGKJSeR68HN8JJFhdupCBj7uwWSBPe3gRUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
مشکوک به نظر میرسی هالندعلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101787" target="_blank">📅 17:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101786">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpRJw6B4M0EBkUjCD9IqjPeVqfZqFjI16HvvYdPVuSWTdpOT9KJWhwZyZHN2n9rUSvrwVJtckt2XxMn2kW6PyUgQlSkvCuz54X5fdePQS-VhinjRejRbRixUIZHizq53fHLQgjEhCXLqueKWwEr5bIPCMoQ52BWrz-NzFZATd50Ei7bSbpTBfQLQ_VOGozyv_t-JTxK5LpODhswjZl1sa_Rnnq-2Yc2ruL_iLirKx-YgYmaG7c4RBWoIlegq4KkAtfCv46IwpbdLfIrv_VTPPkgNiel3z5P8XBdfhGDeH9Qvn314uautBv60L7OyKOyp1U1corwlo-fv2zZI_60Pog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اسپورت: منچسترسیتی با توجه به شایعات جدایی رودری، مارک‌برنال ستاره جوان بارسلونا رو زیر نظر گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101786" target="_blank">📅 17:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101785">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
⭕️
🔵
براساس شایعات منتشر شده، قرار است یاسر‌آسانی تا فردا به تهران برگردد و در تمرینات استقلال حاضر شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101785" target="_blank">📅 17:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101784">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJOmmBqCLpJ710TVZqsMzpcB3Nyin_vcSWDCsPNWNsNeIqKtrrAfGkHm3MGgQqt4q5jWa1kgwz-Ci7KsNHc3Sroiy4rRzFJGBzZz3T-8GW1D04h7oKGg5op8IJ8j8lngp8lwx_VDiZ9FKhpVoZiWW3uROuB3OMZ4xsNCB5I0FFfwXS8ljpaXiQVVxk2332y-2FfQwHeAEIZBro0ZMisfWtKJb1nhk-UF_gHrg8ahGj22mNsW6jn0GzGQ97aRDP718mVIX7GFFYKdOgkxP9VKw8P82vMV3M3O3cq901HwG7WDdUQflWV_ejX6aoQfepryVEtsjBYWVlido_LEiyTc7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇹
✔️
به نقل از گاتزتا دلواسپورت، آندره‌آ پیرلو سرمربی جدید تیم ملی ایتالیا خواهد بود و این قرارداد به زودی نهایی می‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101784" target="_blank">📅 17:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101783">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e1ed1b860.mp4?token=rGqyxTSNAUuaIyrYNAQnzeSfZLVarSO80hseR36tNTCBNzfGoqaRlk6Pa64jAT7xGndiDGVy3z7x-Eb-_BpWZyrr3MT58iEc5LHa495i5pWaAVXLnTz0O1PLUiLt_btCrCtJCwyt3V7yv5v2ZiD4aFRawgWVC3dGNX6zQOlK9rPtKR1DxxiWjdVStHoYj3U2gMLB8NXl9XAZOyfUUXHhmMOVq9ZzN1sd89oxw0KPUjf_5LJtShGfxRqjnIIRSU90nGkGy5Mg7cpieBsGImgiqj8ged0kxviKfcI_4QP9D3LzJmcOGMpjC_nkfxFQQJFsP31_SLWeQ36m-aKrPNF5SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e1ed1b860.mp4?token=rGqyxTSNAUuaIyrYNAQnzeSfZLVarSO80hseR36tNTCBNzfGoqaRlk6Pa64jAT7xGndiDGVy3z7x-Eb-_BpWZyrr3MT58iEc5LHa495i5pWaAVXLnTz0O1PLUiLt_btCrCtJCwyt3V7yv5v2ZiD4aFRawgWVC3dGNX6zQOlK9rPtKR1DxxiWjdVStHoYj3U2gMLB8NXl9XAZOyfUUXHhmMOVq9ZzN1sd89oxw0KPUjf_5LJtShGfxRqjnIIRSU90nGkGy5Mg7cpieBsGImgiqj8ged0kxviKfcI_4QP9D3LzJmcOGMpjC_nkfxFQQJFsP31_SLWeQ36m-aKrPNF5SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
مهدی‌قایدی ستاره تیم‌ملی ایران: اگر میخواید عاقبت بخیر بشید، بچه‌دار بشید
😔
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101783" target="_blank">📅 16:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101781">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kgXcS4pIVeAvkyENBzXHzBr6sNgEgyI5qNgTfW4H16hoAkZoQa5uH3X5LWhn4NhtRCmSi6aOwgi1g5RcuQZqhxFRnPeSB_M6lXL91B9hNARQpvq1_8F13V5Iwm9AUw-_4E1y5WRudT4bfJMxaVDtEwkgQAeGmFDF1p2euwtL0IdnnSPyb82jECKz8PIuB-GtZve1Xon9eRdCPvKnrsMm_LiJ02V4CZ7QKIQNU3Tl7gVAupOAAllObPkX9T1PrG4o2GwRDpDwjfZA4rpBFt7mHP0CB8LLAHdbla5SodeLfu9GeGNxAuYvQ7MyJ76zFE4202rT84lSpVRBp03BMpOKQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sW_z9hkKUqwrnJ-MGOU9tvFrEU_6uLD4ZkWg_BTEqaN2venw2MIufyjDZEvBxmGGtaktJDrfEJO4E8sILqT90zyvG-xvatFgvoF0ghIag2oBUM5kHVy30S4waQ-9NAm_1YdsOMCHMZVvRBxKzRTMc78D7QUysoyjLh4dGBoOTx4OTh23ML2Ky46FlYKOILqGb56OMJwhMHWsJtbbiY4sxvUtiMY2mlxef6sZhrxX6qIM1jo2A9zNj4EWOgzX0DxYkYTzwYLLTepKMYG2L3Qeyj6vanAK93jZwAoaw5DyUjoH7ooiOJK_IXFtAVIoAKPSDa41_rQ-XE_Nd0oEXCyjwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
⚪️
امروز، ۲۶ سال از جنجالی‌ترین انتقال تاریخ فوتبال می‌گذرد؛ لوئیس فیگو، کاپیتان و ستاره بارسلونا، با فعال شدن بند فسخ ۶۲ میلیون یورویی‌اش توسط فلورنتینو پرز راهی رئال مادرید شد. این انتقال رکورد جهان را شکست و بازگشت او به نیوکمپ با استقبال شدید هواداران بارسا، از جمله پرتاب سرِ خوک به سمتش، همراه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101781" target="_blank">📅 16:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101780">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPKUNsBj_5NIPX_aJc_cjA_WMhdGS3j7XCOMHNaPurqOTCdD1hcYx96fBkh4gptxOJAfIK02SdI8gcCxJBYBGKxSg5j3BdRF9zWsAl5Wl9fzlzsNjJtS-HLmsNeSswm3AKhxKYSqNLVshVhVjhoaQ-ikv9dff1HRz5LAcg6EBb9bU7EXV9iyidSP8U7brq1aJ2JU-768VCUWD6G3CTXI6jvTWELizXEDPGLDdoYMkw7TBFvT4WbY_1EnxjNINiK8vQ8sYZd5T6sObEsQab5KKewQ-gjltgRY-uk2AMwULnKBEdCdNt6mBIQTStsOJ2Z_VNXQflFUiq7lpBHgQEJ2Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینتر دید کسی حواسش نیست رفت به یه تیم از دسته 5 آلمان 16 تا گل زد. دوستانه نیست این دشمنانه‌ست بیشتر.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101780" target="_blank">📅 16:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101779">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56f574b376.mp4?token=IZ-zDZh-anZ7pSchKjcpzGE5hDvKEO-6PQ17shjx6jTWyribkiEH03C-b4hln4SqGxtMPkwjXVS76m-qECZZVwT27athFD3E8ReAePeJBMHW6Xtb69rUCNpIf8XIxrY4bZ3S5M19uNBJXnOaQBjupzmK_EHVyuR_fhar6bJ8hkpD5HbhXLvs1ZaaTZVj5Bt0lJGAxo2Bo5U0pdGOfjU3URpcEe9JGUkH-Hj087_9b98OB_zduPmP1c_AaCGs1oUXvVirUYRbdlotx38sNq1_PvhMOk-lna8Xl__VA66TmT7Jqi8tAF1lAzDXucu8zu3s3SazrqEqTBUMI7XcRvz5tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56f574b376.mp4?token=IZ-zDZh-anZ7pSchKjcpzGE5hDvKEO-6PQ17shjx6jTWyribkiEH03C-b4hln4SqGxtMPkwjXVS76m-qECZZVwT27athFD3E8ReAePeJBMHW6Xtb69rUCNpIf8XIxrY4bZ3S5M19uNBJXnOaQBjupzmK_EHVyuR_fhar6bJ8hkpD5HbhXLvs1ZaaTZVj5Bt0lJGAxo2Bo5U0pdGOfjU3URpcEe9JGUkH-Hj087_9b98OB_zduPmP1c_AaCGs1oUXvVirUYRbdlotx38sNq1_PvhMOk-lna8Xl__VA66TmT7Jqi8tAF1lAzDXucu8zu3s3SazrqEqTBUMI7XcRvz5tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
برخی از سوپرگل‌های لوئیز سوارز در بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101779" target="_blank">📅 16:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101778">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3068c762cc.mp4?token=FvYzH_qi9khafNgQcqx286F6_lV5gdY7jE_AqVw22rQPGK9d6cW4wOt-uo1I0g6h6l7Q8jIdBMJqh9_1ko8gIZkwEjynniRt5aAMcdZuz6J8oYjQTwQtt7UjCo9EKC17HE_rR1tsdPAPOKHSKWeeki4wzi5ZSXgVBfEMckeQUcopqzf7ySXbZLHj1VUT1O9NZQ-UoLb2dfqqtGtK0mSJdkvZi87EVVa8w__PV4pXA1Yt2K90p-2ZVZXCkkMQPG9VZ1tyfUrN_pYhaVkokG1LYDPAZU6RpIe1zEJo30zsIqj9RIffMzy-OIFV9tDC8gQQqtMyIABZA7fEZHbWvZwSBAwAWLHUJKRA8RTMjRFQoNmWM_6f8nqSk-eS6JZktgAYAkzWNY61HNM8-E58r7c54a4Xa5qel-zsIVs3absYZotyqiZnMaKfZyzoz-gsTqRbKtgJb8xUD8ulBDTbPYojjyL_AmO6XaM39qIyRtPhA7Ync3CRadmY_mPdGKgihM3KfOwfKMC6rKiZbDZwf3v9JIi8-4mT5lwHafB8Mp5N800nQOj2ytoU1UAKV5d3jM-cVrLEzy9Wm3CwpCB0CcqS3Rg1X1ynChaonDtGPrADttk6TgOdpWaViMfdytnWoQ2HpV-T_2RCn93Yud_QX5N4mCmI2j3W9AQTL_xq0k1blE4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3068c762cc.mp4?token=FvYzH_qi9khafNgQcqx286F6_lV5gdY7jE_AqVw22rQPGK9d6cW4wOt-uo1I0g6h6l7Q8jIdBMJqh9_1ko8gIZkwEjynniRt5aAMcdZuz6J8oYjQTwQtt7UjCo9EKC17HE_rR1tsdPAPOKHSKWeeki4wzi5ZSXgVBfEMckeQUcopqzf7ySXbZLHj1VUT1O9NZQ-UoLb2dfqqtGtK0mSJdkvZi87EVVa8w__PV4pXA1Yt2K90p-2ZVZXCkkMQPG9VZ1tyfUrN_pYhaVkokG1LYDPAZU6RpIe1zEJo30zsIqj9RIffMzy-OIFV9tDC8gQQqtMyIABZA7fEZHbWvZwSBAwAWLHUJKRA8RTMjRFQoNmWM_6f8nqSk-eS6JZktgAYAkzWNY61HNM8-E58r7c54a4Xa5qel-zsIVs3absYZotyqiZnMaKfZyzoz-gsTqRbKtgJb8xUD8ulBDTbPYojjyL_AmO6XaM39qIyRtPhA7Ync3CRadmY_mPdGKgihM3KfOwfKMC6rKiZbDZwf3v9JIi8-4mT5lwHafB8Mp5N800nQOj2ytoU1UAKV5d3jM-cVrLEzy9Wm3CwpCB0CcqS3Rg1X1ynChaonDtGPrADttk6TgOdpWaViMfdytnWoQ2HpV-T_2RCn93Yud_QX5N4mCmI2j3W9AQTL_xq0k1blE4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چطور در لاماسیا، مسی و اینیستا می‌سازند؟  اینیستا و تشریح سازوکار خاص‌ترین آکادمی فوتبال جهان؛ استعدادیابی در سرتاسر دنیا، مطابق با استانداردهای بارسا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101778" target="_blank">📅 15:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101777">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">▶️
👤
به بهانه تولد 49 سالگی مهدی مهدوی‌کیا ستاره سابق پرسپولیس؛ تمام گلهایی که در در تیم ملی به ثمر رسانده را در این ویدیو می‌توانید ببینید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101777" target="_blank">📅 15:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101776">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKEFs3h6UA47HDJYhPAU_0qvHlwYbK35MxPawUub04-t_PgOCNswSMMj8PYbPnQ4F6blVIThv4yBHH35H3PkLLXlup0I2Ix8usaG8BSjaRcJAwNjDUEH0Ii3NxPEZXv2aaB92Nz_uQc2mfI7gCzeaI79IcHeje53lBx5b26fQIodQwtP6efSdWAIl-l-ALgYLpEWkMKTAD76RfQOX-mKQXO97IYfh7WryCPo0ZZIHL8z2WdKGI4RviXgYM-Osr_H2FasMAH4slZxfgckk6i3p7vo-tz_ZwmTUS_aTjbMz_8zWKeBQUPSwGxwp9pcjTfnCfTeqiAu-r2WI1QfXnIYAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇩🇪
یورگن کلوپ:
با چیزی که خیلی مخالفم فحش به خانوادست! اگر به خانواده‌ام توهین کنید، من می‌روم. اگر روزی فکر کردید من مربی بدی هستم، مستقیم به خودم بگویید؛ همان لحظه بدون اینکه حتی غرامتی بخواهم، کنار می‌روم. من این کار را برای خودم انجام نمی‌دهم، برای شما انجام می‌دهم. با وجود اینکه دیدم با ناگلزمان و توخل چه رفتاری شد، این مسئولیت را پذیرفتم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101776" target="_blank">📅 15:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101775">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcNTrspHIHUHCq1KivZrucfuzLXnjNnM8Yv4pUz4cK77PBrCKR8IvcjBjerLVJJDuvXm4NmD9WTAelt4E5d54Ee1PMv7p5WpxBDh75SaPijRqD0bRPN059J3Ws2029OHP0YU6XT-7L_eb2VdESE5u5_c2RJXj5WBqvx8RmZ0Ip5yyhNFEfUgJVTUjQm3E7WqZUYgdr-8JsVCWrdqGbTR33o-kucQZYsG-YtYTpwZpNSvX3J-k6qkxXHHwISdS81i9hPX50J2VGG6Ra0AYtdN4Awqbzh1aLAUfTmFv-fMaeSS1sRh3FcZIFh_sBt7T6CyAvWdL3eHbigbh29e2EK38g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
دنیله دروسی:
عشق من فوتبال و رمه! اگه بازیکن رم نبودم، حاضر بودم همیشه 10 ساعت با ماشینم سفر کنم تا برم استادیوم و تشویقشون کنم. هیچکسی هیچوقت نمیتونه رم رو بیشتر از من دوست داشته باشه.
تولدت مبارک آخرین گلادیاتور رم
🎉
🎊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101775" target="_blank">📅 15:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101774">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjwuBkYktC0Khr21wyZnY1AmXPbS29pnGr9rF16dqT3J2Po7e8xdptNk55pLYm8q523yRa8Q8QocEk6ODdBXopuugKeYEgGdsTM8QmU8MPA_OMi8XtNHM1DQYnncVylUmc-8Ta3hqNOf2trM2s_ZGe-nsPdgxgyntuh0by7rxrwC0kF9XpWAcEC658OmY4v3_nXJ-zAafAta11YykqNUwnNwXB6tQWK_aHc5eEa6BBulkChR0eR3TKzn6gx8mf5Gk3jxie3tnsAlcMF5Bf9m_I1Ha_bJhCInB9kAlVUroXlirIOFLrTjP1XBZKz4_ok06fXbfQ7tSYfrMlLiE-4bVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
قرعه کشی مرحله گروهی لیگ قهرمانان اروپا 27 مرداد ماه برگزار میشود.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101774" target="_blank">📅 15:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101773">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlsXWRddwjkaenGNNbS280kpC_xNBwYjgqD-oCtkAea5sv_ycfKfd_PUBRGepdfFZWCrAns2356Tn7YRR5tJ7MxkE-z_LZOXjW-GddRcm4wYCtGbcJenxAVuE33XemllSgfFlssMkqw2OVW9XXLSwwDudBw8EWt56UYHWHqIa7ZeRViUFOHaxHrKDgsbk6cjHElUFE_bEPHlVFxvX3BRvKhYdBKZtzjqSdV4kKIaGuzJCcmiQGAiFMKAyoeqM_A3-XqAziVjtjsRXAtXVfPqQhGTdD5-B6kzOjfZbRdQYOfP9i9YbKP8dJFrSOYC02kjEhXa1ox8N9iHx9oyEmwNrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
📊
مقایسه عملکرد نیمار‌‌ و امباپه برای پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101773" target="_blank">📅 15:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101772">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0RQp4NG2rgAK6WtlVPEdVrl89amn5d8xux4kQGdeW23whFrJnQGJ4ctCCt-qhC0o76RNJOBGE4RwAbTde6sl___jt4Hc3UnYxGutVeeI813e8UstBJPU3oBIWoYwFx-SgjPeqJ_1mAfXXJlj0b963JMH236-BeiBJ2qNMh1E8HCdo7d8PHDCWgx7kjqYLJlCGRk-bkidMdhPpeLhDqhD2lPWUv7I-Ak5z69TXIZgM1F7awcZn2CNcWShUJ3U7MS-OsG4wdGdjRwZsDjFONZjln4IijZ58VOnbStnHKqR9JY5hgVVEToFe-oB-OhKzgs3scSIS1ySFb-EVE2oUjdYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوریییییی از فابريزيو رومانو
🚨
🚨
🇮🇹
🔺
پپ گواردیولا پیشنهاد سرمربیگری تیم‌ملی ایتالیا رو رد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101772" target="_blank">📅 15:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101771">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qjfu0YOK6VijTV1ZbHk-ng_YVJ8o0FJ6-GbI0aCaNUPhTvM4HnjizePMPadVMTd8bmTGJLNk8FbdD2loQR7tP3lXDNeyhtMGl8d5n4-fHUY_KWMj6qZxxjhWXX9hLbNF6ZcjOaMU5cFykzHl056MwiFZQhgb8R77EjyldaRQm-J0y5oXaluUDMqjVOz_c-KGVJV_HEsPdYLQEMY8pFoYFO35V5gLgMrAIkxeCURxV1iRtsSJfFZwOioV973vb35B-hMiGc8jdffFh4VKuhRd6Kg8gXhRFt1abEBHqx4QG6tu6LXewLaVO5QWB9CiQAoQqwk_4kUUTibfRMt0xv2_Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
اندریک و خانومش و بچه‌ای که خانومش بارداره به اسم کندریک!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101771" target="_blank">📅 14:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101770">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyh1Zzs3Iyq0k9NrzM9rQE2UulVVu7fcU9u__Y89JjXDrbwjSs4pYvNitH8l_veM0tfdAYVpmt6JI2DPRi4pS5i0uVzxhCDJ6q_ecrh4ZET_4wc6475-4J-QCgg29C9EIjrlROOpos48MOeu6HS1LXnRTLWmIoNiPXLgvuGXeWTrVJewt0NSEawLcaLYMZ-HQV3c49YoPATYW7dbh1fYw1HBYieJTl44A1BaCHluAAZ6LkZITDsAs5Aeu0H1EdmP1afy7pBhGMh305ktbyUvJPRU5FIiaJT1Jn8FyQVlBlWs4b1Hjn6T-zZ-i0CcdDKEY9GBbkfO38daLz5YFr4mgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚑
🔴
از زمان پیوستن به بارسلونا، فرنکی دی‌یونگ 416 روز رو به علت مصدومیت از دست داده که با این مصدومیت جدیدش احتمالا به 566 روز هم برسه
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101770" target="_blank">📅 14:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101769">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/accd9e1667.mp4?token=dUZ25r_8dIgnQwg2avPPDZ-y4425h7jC3ynOgcpDy0nrh7y4eLhfAOf6g80dRB8cGfBzTSpqI3YJEsFKkA8gPYMZhupiDyaXN8FMfvYyqrJKQZCtet9KFg57BYMPr2Y1hrg0x7F-2d-EvStT91MdFA45DGIFF9v7ZVr1MTy-Ay4wV6nMfuE-Cv-w5xn8q2jX5Vn70NOF8tCiFk-hNKFxF4MOa_wrDsKBZxyXUAxHZN-DyMJpfjIG2747dW8Z3ZDbdzta_Oa6RygMEG5rWMjsEXoo8FoqUqOa9RVjrwrz9-2QN8ABiNkrgyPEkSxXtcSwBONgoPQdYpZtPWEveaoKXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/accd9e1667.mp4?token=dUZ25r_8dIgnQwg2avPPDZ-y4425h7jC3ynOgcpDy0nrh7y4eLhfAOf6g80dRB8cGfBzTSpqI3YJEsFKkA8gPYMZhupiDyaXN8FMfvYyqrJKQZCtet9KFg57BYMPr2Y1hrg0x7F-2d-EvStT91MdFA45DGIFF9v7ZVr1MTy-Ay4wV6nMfuE-Cv-w5xn8q2jX5Vn70NOF8tCiFk-hNKFxF4MOa_wrDsKBZxyXUAxHZN-DyMJpfjIG2747dW8Z3ZDbdzta_Oa6RygMEG5rWMjsEXoo8FoqUqOa9RVjrwrz9-2QN8ABiNkrgyPEkSxXtcSwBONgoPQdYpZtPWEveaoKXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
در چنین روزی، ۱۶ سال پیش، ماریو بالوتلی در جریان یکی از بازی‌های دوستانه پیش‌فصل منچسترسیتی این حرکت عجیب را انجام داد. روبرتو مانچینی آن‌قدر از این اتفاق عصبانی شد که بلافاصله بالوتلی را تعویض کرد..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101769" target="_blank">📅 14:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101768">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33b6580c49.mp4?token=ZqhOhXbwxyE4T1BAEqtdrRjs-3Q6tCbREr63Ac3rsioAfOPIvZ-hZWp9y9bjhOeqY5h0CFAy6UUHkAPK-1Tla6dpg3eyKXeLiTdznr3phqsE6HJow7BWit4_fQmoXjrCLS9UEjWim6FtQulxWcydTxlhFL0MFEgQV3epH4HZwwnBon8JCV9gDLDfjSnj-tOzWel3AfZtR2CogjqB7CLO2GZsUKeFZppAoa7WpzH-xezkgaIX9ySJsde9ciIi6JXrHM8U8URl0UCs2MSGNQk5ocupqm2S1bA_hHoopCIT7w0lwFdHIpb0p3AZfTqaZcjQKdtkBD7SDzP4gcguBdSxyzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33b6580c49.mp4?token=ZqhOhXbwxyE4T1BAEqtdrRjs-3Q6tCbREr63Ac3rsioAfOPIvZ-hZWp9y9bjhOeqY5h0CFAy6UUHkAPK-1Tla6dpg3eyKXeLiTdznr3phqsE6HJow7BWit4_fQmoXjrCLS9UEjWim6FtQulxWcydTxlhFL0MFEgQV3epH4HZwwnBon8JCV9gDLDfjSnj-tOzWel3AfZtR2CogjqB7CLO2GZsUKeFZppAoa7WpzH-xezkgaIX9ySJsde9ciIi6JXrHM8U8URl0UCs2MSGNQk5ocupqm2S1bA_hHoopCIT7w0lwFdHIpb0p3AZfTqaZcjQKdtkBD7SDzP4gcguBdSxyzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
کدگذاری به سبک قلعه‌نویی؛ واکنش قائدی به حرکات عجیب قلعه‌نویی کنار زمین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101768" target="_blank">📅 14:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101767">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTonYUjjOva7vR_O9S3FIJMm6ezEhil3VumRJcsIEDnpZ94UHLyFv0VJJpza845g_xmjxMa0Z0mzI1L_wTRDj634pXAJKc-VhUaORTXzhkQUQynfSfsnbVL45JTYuxoYwQwH3qYt5vVNslUytc9zQdqb0EFpwLtY88VW6Nr4HISOoj6A0w0euuzQSpPQUwJNwBDLlc59hzmTsVhS9GVZKhIfHDK46hSz-P-EEKoJ4tw39EwhVrX2HrAGIYImUsNyrNTC69CQnR3snBoiznZ_sf-D4v3MShFElZE2ASmUsbwU30M_wcd367qQZRmI_BENbxu4mvPOJn7bVP5emky9QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نفرات چلسی برای اردوی استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101767" target="_blank">📅 14:08 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

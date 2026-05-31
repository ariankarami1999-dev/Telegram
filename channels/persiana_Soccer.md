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
<img src="https://cdn4.telesco.pe/file/Y-xPyG9rqL-hC0ltMCK3SbjmOcov35wdwwLIGE56FNxTCMFRxit_kNmZQ9-u5Ht2NEIys3Sk1mSUf-vDwkJJjxky031IVgP-h2lI2kcgvdbuYRAmWrCa1JohOOlyhaRBRo6iZtoMkwCuKhzItLGA0qVho-mbSgbUNnfJrlw9_rCIx70YVBAl-JJGIrOIdvDEVdLi-COfKHMxYCaFsRAtCzKscN3RG5LL8p_0OgsCIkU5LUQOrMQ0JcX5ECnbu5bLzrjV7tuieXqg5vY84JkXGGpGcfKLWq5aGKYIsu6ZwftNiXjEmU9NpzjsKS2MBuq3nMJJHPpIRhKGeYqXmtSNrA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 178K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 13:13:25</div>
<hr>

<div class="tg-post" id="msg-22530">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPm6i7XpbuLruXA9KLV6XcDJXgvAwzzIFNkPgHBQF08fYni6aT3fKF2T6JXBNEI7ghE1rFRcR1i4xkKf2gQ9UoZ1bCLL4kqG9PqdjVdWrrRJ6cgNTIn_hvoTyUT9tRwIA2ZW63oWtR8Lv4I5s1c10xxMLpOGp158zNxlyX5StVkSD1kY57t_xA-0en4gWqWeBY9P9A5e5k-dtcK1jBwxBtJfMbKnVoggnWmBG0w0m2lryylajVv-cPgWfFV7pooF5irSYDYDFqMdU-_DenZHnzNGSWOeGcBqwYeZU38uZxF7n1QQPKH1ZbQfPa21doJ9N4OBER2cj7IbxFySzZYIMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇵🇹
#نقل‌وانتقالات|رافائل لیائو به شکل رسمی اعلام‌کرد که‌دراین‌تابستون‌رسما از میلان جدا خواهد شد. مقصد بعدی ستاره تیم ملی پرتغالی یکی از تیم های لیگ برتر انگلیسه. منچستریونایتد اولویت اوله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/persiana_Soccer/22530" target="_blank">📅 13:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22529">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dt4fS0aNTu4n9t1FaBcZnhHDzUi9t6wt1mXIxQzbjZIqukN0jN7tGyXE8ZzFfVNdc3DMkRekdQaZz4RQ44Du2K6Vqm2xeY6QcI5xh9-oUNY6EBLgJ699IZY44QS5Okk6sZnVd3qUL44TNE43r2aIkqlzugXYtd9ZysI3Rc-DCvKxjK7JN9kezxoxOKFg3AaKqtn-e5tQwbKUbiu936nnBLKQ9zG_V9A0nW_CNuiX0HAk_QdftA31JA4px_L-hSLB96gP3xAeqL_exC6lCbjBm0Zcg3Fv-tBZdtd6RegPR6S8xIlQDOaQ8x_kmwXnni-OlQFyH3xWCTlvaDfuG3TeEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو آموزشی‌نحوه‌واردکردن‌فرکانس جدید بصورت دستی در رسیورماهواریاهست؛ شبکه‌های یاهست که بالا معرفی کردیم همشون تاپ ترین هستن که بازیارو باگزارش‌فارسی، کیفیت فوق العاده، بدون سانسور و تبلیغات‌آزاد دهنده و جلوترازصداوسیماپخش میکنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/persiana_Soccer/22529" target="_blank">📅 12:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22528">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaXKoPz53ZbF4WlmVF9O9Fnt23b6JBA-q5BUAm9Rdw0B2DY0MUrapH2UWbBqFJaCZmODwXWNbt8pLHagnBbXr8F9iQzshIEbyxX3bFlq2xt51URNyKETeFbjLOVqbp4arys1WLOrHzBvijVEOgwH1fRky-SFAkVVe7p9QzcxRUgVYG5QIwrZz_e3ifmWVR5HQ7MTj4fQKBy_vBXzuOEFNaWwidQ74fsjeXZ_bmYns8HH0SfCvRQPvPDhK6Ei511FchIE81QHZ2uq9lY8tYeWNOHX17Pcc9-1o8Z4XgQwP0JcR40SCfUpw4UKz57bpTPKfNlKY-H9lKnxbxWzU_J1Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخرین‌اخبار منتشر شده؛ باشگاه بارسا طی ساعات آینده پیشنهاد برگ ریزون 135 میلیون یورو برای جذب خولیان آلوارز به اتلتیکو ارائه خواهد کرد و این بار این باشگاه با این آفر موافقت خواهد کرد و این انتقال رسما انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/persiana_Soccer/22528" target="_blank">📅 12:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22527">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/460d6cadb7.mp4?token=TF3Fn7zwAh2YeFM0ZS0r1R-jcxAjxO576r3sFotzfqZz6LACz8d86G2e3FSndp1BkIZ2xih64JF49g4bS4D2qg9jyBZvq1GpUNeDNrwIJZEdJAiD55-a0K-inUgS7riugHOcdIaHua-0il7XZcMjbXM9rgWUAirdKzBhOZwz-ZKCbolyS9_sKKJnNeNAbn3gYGdOIPVbBGcoVm9lfvT3xFHLoP7FRlFEOdp586mVQnT6dXgCORzWjdnVh7fg8jX5D_b_4jR6imTRTcfgKQ3ZtZDTTHsEiX5r3v0t9k3ex4EvjvpWwSCL8_5wC0arTbGWRX4qywvBIWfaZP6LDjJPNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/460d6cadb7.mp4?token=TF3Fn7zwAh2YeFM0ZS0r1R-jcxAjxO576r3sFotzfqZz6LACz8d86G2e3FSndp1BkIZ2xih64JF49g4bS4D2qg9jyBZvq1GpUNeDNrwIJZEdJAiD55-a0K-inUgS7riugHOcdIaHua-0il7XZcMjbXM9rgWUAirdKzBhOZwz-ZKCbolyS9_sKKJnNeNAbn3gYGdOIPVbBGcoVm9lfvT3xFHLoP7FRlFEOdp586mVQnT6dXgCORzWjdnVh7fg8jX5D_b_4jR6imTRTcfgKQ3ZtZDTTHsEiX5r3v0t9k3ex4EvjvpWwSCL8_5wC0arTbGWRX4qywvBIWfaZP6LDjJPNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی بااعتماد به نفس کامل به کراشت گفتی بیاد ورزشگاه بازیتو ببینه که تحت تاثیر قرارش بدی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22527" target="_blank">📅 12:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22526">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twXSBUkLwHEerxnqFilwM3ItsZEEu1PE5GgrOl-4FAU8SeAaxbfL2so2RdHHUYGsGy5zMeSlra9vQOGOoVx-g8UpqoRcaSQ1LQMIY2MVb-b3SmHs0Ysbxrsrh9-MMc6aJf-iYf2Y7wa_ihlq05osTi9c5ry3iurjf_a1jLqFBF6l08lB72J_GBXIGmSq-WoBh3TQBWaF-wzyZng7bXmNjmxmmkcRxIwZXwLXtr9TyWK0r-iszb9P2Dhd6w9o5OGazpGup-EhKsrnU16pbXSAeud7O-mD8XTL13hwKEdVv--rzUoNADcliRSO0MVlgyJ0OzG5niq63M44ddalU76a7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ به احتمال فراوان فصل اینده رقابت‌های لیگ برتر 18 تیمی خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22526" target="_blank">📅 12:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22525">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55166b2d48.mp4?token=eAnf6VgxqYKer5nnoAuPulp97gRj5j9HFnj0fMruWxLcNRFVWinr5i5B4qx9wKk-vVIltvld_eGqXYw-H8lbjk8I_5Xr-PfML5IBFDc9rKxuK1cG9LklEZuNlqJlPvea71UXRNogbvE2YE__BH9Zhz2qnCZAxN7eU-xBs8kcqGYPER1ZC2QojKB-dXbF5TXVt9swDlH3xF4D-DQfHCxoer3V2V7lBZPqjh9JPfjgXaYYLdGLATxDD5o4aUqLAu70GHtEOr865ITTAWQZQJG-kg7W1ojRkb7wnmDAJTLLE1LHjhSc1Ga1VKLm7HcoSPmTxJPSUVYMWGhsQIb2iwRM8whRYRBdnQ1KzhgztgfM0uGHYA13EuTNVG7ze7uzlheq7kD-tb62kEStb5yTh_NDEhyRcL60GEko_n-kn0k9XOpQ6d3fBczgkcxH-8I6EeoWoIteIAE3D26P-VUmOVqF8lmEgmckyy3ysmgOpb6-0zJQTc7rw2PEU1-Bk1-vrNPzPut3jR8SaBpCc-SUXv6tLV7D3hkRz36l2RKRLtUF7eYiwKvfFWTuRIpdmF9e10Z91JxaUwTcCoj9gCrd7NIcS8Ho1XCGBzUraWl1E6UodSr5Kzc90F_ov5xXVlt3OqhH7cMaPoHD_p5zPcUET_VPboxusY8P2E_BORfcgMhYydI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55166b2d48.mp4?token=eAnf6VgxqYKer5nnoAuPulp97gRj5j9HFnj0fMruWxLcNRFVWinr5i5B4qx9wKk-vVIltvld_eGqXYw-H8lbjk8I_5Xr-PfML5IBFDc9rKxuK1cG9LklEZuNlqJlPvea71UXRNogbvE2YE__BH9Zhz2qnCZAxN7eU-xBs8kcqGYPER1ZC2QojKB-dXbF5TXVt9swDlH3xF4D-DQfHCxoer3V2V7lBZPqjh9JPfjgXaYYLdGLATxDD5o4aUqLAu70GHtEOr865ITTAWQZQJG-kg7W1ojRkb7wnmDAJTLLE1LHjhSc1Ga1VKLm7HcoSPmTxJPSUVYMWGhsQIb2iwRM8whRYRBdnQ1KzhgztgfM0uGHYA13EuTNVG7ze7uzlheq7kD-tb62kEStb5yTh_NDEhyRcL60GEko_n-kn0k9XOpQ6d3fBczgkcxH-8I6EeoWoIteIAE3D26P-VUmOVqF8lmEgmckyy3ysmgOpb6-0zJQTc7rw2PEU1-Bk1-vrNPzPut3jR8SaBpCc-SUXv6tLV7D3hkRz36l2RKRLtUF7eYiwKvfFWTuRIpdmF9e10Z91JxaUwTcCoj9gCrd7NIcS8Ho1XCGBzUraWl1E6UodSr5Kzc90F_ov5xXVlt3OqhH7cMaPoHD_p5zPcUET_VPboxusY8P2E_BORfcgMhYydI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لحظه پنالتی آخر آرسنال و قهرمانی پاری سن ژرمن در فینال لیگ قهرمانان با گزارش جذاب فرشاد محمدی مرام که یکی‌از آرسنالی‌های دو آتیشه هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22525" target="_blank">📅 11:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22524">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91b2ba8656.mp4?token=ZiV8r8Zvx-D9mO-BnW1ROUU7vTSXDJsuKN6M_IxxNqg0FbC92VZVEbF8MhwAuhTH3Ihc7wZODruDqxQyeTpCQfhEVdKoIyz1ICHWnKpErsCkCcwRWub_ni4VIIpec0QU02W2ZAh7RfgRQLLnc9i3cARw1207qAhsqZSTXkxknpdSQSSHJ63k2BGTrSg4sbn6nlSD6lc_Oi-Sr0JhYcuScBxkrTXkHrDKj-tdMqQ_rs0uiHlNhQ1V3aSlqug5VNAPJCMCWd1k-Nnogdxx6yMu71d9fSzDvgHHjOpVOTxNuMz7zl7YrQeAcfLL-cQeISKLi802-B-np_4psRnZYidQzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91b2ba8656.mp4?token=ZiV8r8Zvx-D9mO-BnW1ROUU7vTSXDJsuKN6M_IxxNqg0FbC92VZVEbF8MhwAuhTH3Ihc7wZODruDqxQyeTpCQfhEVdKoIyz1ICHWnKpErsCkCcwRWub_ni4VIIpec0QU02W2ZAh7RfgRQLLnc9i3cARw1207qAhsqZSTXkxknpdSQSSHJ63k2BGTrSg4sbn6nlSD6lc_Oi-Sr0JhYcuScBxkrTXkHrDKj-tdMqQ_rs0uiHlNhQ1V3aSlqug5VNAPJCMCWd1k-Nnogdxx6yMu71d9fSzDvgHHjOpVOTxNuMz7zl7YrQeAcfLL-cQeISKLi802-B-np_4psRnZYidQzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
واکنش عجیب ایوان تونی بازیکن تیم الاهلی به قیچی برگردون کریس رونالدو ستاره النصر
😳
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/22524" target="_blank">📅 11:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22523">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlR-izVaYPfLOz03BZFNOMdGXgQMVYM2MlcIpkM2wjSWT6NHtqBqd6ioLZaAjy7B7h5TEPC18QUKTMiRBP2MHuNbLmt_QxDXQoDIn9elChQ-npEpkLCLWIts_bD7-A03x5vVmKQmX3Dj13UzwMMcJ8ABTEJAfUjb7MTdXsfHVZH2rzbwAfl3oyNj08AHce0vXlZ0opkxrEaks2QWskAb_eZvzNnj0zXzhp5LoIi5MbwQkFGNs0MTXz49Mp6OnwIjnkN7zH-oAZJonBO5-GrVpY9yCcbp6qhUHAqABIU6XbxJTCB_F-RDwDAY91izJ19_HgtU59bd4e6c_1ZgVydeXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ مدیر برنامه های الهیار صیادمنش مهاجم24ساله سابق تیم فنرباغچه و هال‌سیتی درگفتگویی‌کوتاه بارسانه پرشیانا اعلام کرد اولویت این بازیکن برای فصل آینده حضور در فوتبال اروپاست اما اگر تصمیم‌به‌بازگشت به لیگ برتر داشته باشد اولویت او باشگاه…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/persiana_Soccer/22523" target="_blank">📅 10:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22522">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1346d9dda7.mp4?token=fMhGrIc12t8cGl9I76IbF822rhnpeSwjR4iS1yAs3Gu2WYVGX5zD55_KMmdeIhFK0T8CCNF9JfuWvgk2kaA5G7aGtkv5CHiayqKhFNN7CaMG-Jyq3sOerNxR71LuVwhkLzJCDsgc6F0Lpo2BghlsCE_OjIvc-h5F5CbbPHvBzMXw9yfJPrGPSiioezMoiqvXiicAtsAQoVLmDxwDs4jVz5y7mvz0E1XZR4iGcmrMaX1Mal1-JkrviHAwpIzRw8M_nuGuwyUZbNN3u5SJRp9Rol5vYs_Kqxe-GwEIhxqpZx7xh3MtJBDzeIWJu74YehuTdOnM93SWSWVtEFPUy_FCNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1346d9dda7.mp4?token=fMhGrIc12t8cGl9I76IbF822rhnpeSwjR4iS1yAs3Gu2WYVGX5zD55_KMmdeIhFK0T8CCNF9JfuWvgk2kaA5G7aGtkv5CHiayqKhFNN7CaMG-Jyq3sOerNxR71LuVwhkLzJCDsgc6F0Lpo2BghlsCE_OjIvc-h5F5CbbPHvBzMXw9yfJPrGPSiioezMoiqvXiicAtsAQoVLmDxwDs4jVz5y7mvz0E1XZR4iGcmrMaX1Mal1-JkrviHAwpIzRw8M_nuGuwyUZbNN3u5SJRp9Rol5vYs_Kqxe-GwEIhxqpZx7xh3MtJBDzeIWJu74YehuTdOnM93SWSWVtEFPUy_FCNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ژوزه مورینیو سرمربی‌ سابق چلسی:
ابراموویچ مالک چلسی به من‌گفت‌که برای مهاجم کی رو در نظر داری؟ منم بهش گفتم دیدیه دروگبا؛ گفت اون کیه؟ کجاست؟ گفتم شما فقط پول بده و حرف نزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/22522" target="_blank">📅 10:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22521">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c743e5df08.mp4?token=qLctV_nQN5iOde_2fpasSzmwPCuVQrTcqcTZIDKySIXi680NsiKGZsagPwQpicEbmlscGOjWR4zovUfG84Jhssqm6M1f3JHk9AndU4b49zagq9EdYdJkd0AP4m7MAXols3kxCtWUXr-Hmu2U5MDCq4Wr8rKQjT3PlSKSSknetkbdYp-Y_z02Zc6A7ArxWunff1BdEfX6-bgECvkz4kylM6vjXSzs1oELLQHQQEQpuZfG85gU1YqlhhHQJW1XDHbWVnH-nsexbPVgqgSQ3Rv_jkCNI9rznb-vQ1aWPkl3FXgoURPcEMtN3dwgkdgIFUQwoYtbduxiQAFEFqYVVyyoKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c743e5df08.mp4?token=qLctV_nQN5iOde_2fpasSzmwPCuVQrTcqcTZIDKySIXi680NsiKGZsagPwQpicEbmlscGOjWR4zovUfG84Jhssqm6M1f3JHk9AndU4b49zagq9EdYdJkd0AP4m7MAXols3kxCtWUXr-Hmu2U5MDCq4Wr8rKQjT3PlSKSSknetkbdYp-Y_z02Zc6A7ArxWunff1BdEfX6-bgECvkz4kylM6vjXSzs1oELLQHQQEQpuZfG85gU1YqlhhHQJW1XDHbWVnH-nsexbPVgqgSQ3Rv_jkCNI9rznb-vQ1aWPkl3FXgoURPcEMtN3dwgkdgIFUQwoYtbduxiQAFEFqYVVyyoKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یجوری هم متعجب شد از اخراج شدنش که فکر کردم یه خطای ساده انجام داده!!! دِ اخه مرد حسابی زمین فوتبال رو با رینگ بوکس اشتباه گرفتی
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/22521" target="_blank">📅 10:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22520">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b417aa36e.mp4?token=qorvY22czpWThaLJuvmllWxFK9h-5NGwmTkJkpurThh0CPd-7FK95q3Ba7cCGUWNRTrQweu1bwRW4U42uLyKe869kGqGuVf3pJgGUdsosrYZY6op5Rq2UXbnuSXx6z7FGtNQnKnSV2rRpmaLC5mO-dOpL5EJsJvmOKQyWsmdYD-3ylJ0PQMrm9dWisZ_XXqXmRruTuzT_3fpS3QNIa1IkMXs6yEtRYQfUyoA_ESSS2ySB-ZHfImOE2TD9bEB_BYjcMoBHDIEWQ92P1P7HIGHVj8bjTT69QQnDCvVftOCFwZVXiTcsUZdvE5zd5tHKklohBbmnyHSR4xQJwLuk7uzXE3wEePplCz9GbRdmiKTXXG2t3h-zFVwF6dnXxuV-ZJg47o4TglgUUT2xsAVXmpWta8f0Zyb_9LxP-H8IysRvt4k-dOr5O9HgGuKDW_pns7YSay5jHPofb6X0fTZ7ktAZMhmz6XMeqGTo1EycB3epVgfSMaOEwvZw4TuM1HQ-usO7hHLzzm4M3fmK8UHYTIIyjA80zp-o3PSMkzntGDpcQ9-kBtXck9a0bWrmIYZoRz7Z3pKQeugvbqGS6Og2CaUdYNMo704rfrtiuDF0OGQYJc9LXq_hxGrswkfG_lw2wO2AcAwpEqg6LCrS9WYSxuW2WLmqTfDTF-EKp3JGgoLIro" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b417aa36e.mp4?token=qorvY22czpWThaLJuvmllWxFK9h-5NGwmTkJkpurThh0CPd-7FK95q3Ba7cCGUWNRTrQweu1bwRW4U42uLyKe869kGqGuVf3pJgGUdsosrYZY6op5Rq2UXbnuSXx6z7FGtNQnKnSV2rRpmaLC5mO-dOpL5EJsJvmOKQyWsmdYD-3ylJ0PQMrm9dWisZ_XXqXmRruTuzT_3fpS3QNIa1IkMXs6yEtRYQfUyoA_ESSS2ySB-ZHfImOE2TD9bEB_BYjcMoBHDIEWQ92P1P7HIGHVj8bjTT69QQnDCvVftOCFwZVXiTcsUZdvE5zd5tHKklohBbmnyHSR4xQJwLuk7uzXE3wEePplCz9GbRdmiKTXXG2t3h-zFVwF6dnXxuV-ZJg47o4TglgUUT2xsAVXmpWta8f0Zyb_9LxP-H8IysRvt4k-dOr5O9HgGuKDW_pns7YSay5jHPofb6X0fTZ7ktAZMhmz6XMeqGTo1EycB3epVgfSMaOEwvZw4TuM1HQ-usO7hHLzzm4M3fmK8UHYTIIyjA80zp-o3PSMkzntGDpcQ9-kBtXck9a0bWrmIYZoRz7Z3pKQeugvbqGS6Og2CaUdYNMo704rfrtiuDF0OGQYJc9LXq_hxGrswkfG_lw2wO2AcAwpEqg6LCrS9WYSxuW2WLmqTfDTF-EKp3JGgoLIro" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
کدبیس سه‌شبکه‌جذاب ماهواره‌ یاهست که بعد بالااومدن نیاز به‌واردکردن‌کدبیس دارند. اولش دکمه F1 میزنید بعدپشت‌بندش‌سه تا 3 بعدش یه صفحه میاد که باید کدبیس رو وارد کنی:  کدبیس شبکه جام جهانی HD:  BISS:2585AB552585CD77  کدبیس شبکه ورزش تاجیک HD: BISS:03A01BBE20C16D4E…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/22520" target="_blank">📅 10:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22519">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baebe6400d.mp4?token=KyRlNC9MlB7n1P1g3gVOu713wsYXAKdFg4fEUCV8JK4gWy_rPE8LfOKR_5VqIRpCamNqcmnfrCaQpcDNf-CiAuJVBrJNi7COimhkiJw8cDLpxLQfZ3lidecwg_S7JkxSRh52sHw0lgROeW3Z7pzsXdbykEXnnoQFeA2WGRoDGgHMWEXz8z8CcNw4o489zXQ_QO5FlygBoyFGtOuoI-gPj7DJBsy4tujSYdVshJp7XM4WOWBZAw7zuQQQq-JmqTREvRZYKfVVyZRZ-VG7I-fKvLWDkpeGYyrYfXMpEFKQBlpK4IdyFcwAMK0JjGgfqvUbvc0omGs9OOdqaT1b3GgCyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baebe6400d.mp4?token=KyRlNC9MlB7n1P1g3gVOu713wsYXAKdFg4fEUCV8JK4gWy_rPE8LfOKR_5VqIRpCamNqcmnfrCaQpcDNf-CiAuJVBrJNi7COimhkiJw8cDLpxLQfZ3lidecwg_S7JkxSRh52sHw0lgROeW3Z7pzsXdbykEXnnoQFeA2WGRoDGgHMWEXz8z8CcNw4o489zXQ_QO5FlygBoyFGtOuoI-gPj7DJBsy4tujSYdVshJp7XM4WOWBZAw7zuQQQq-JmqTREvRZYKfVVyZRZ-VG7I-fKvLWDkpeGYyrYfXMpEFKQBlpK4IdyFcwAMK0JjGgfqvUbvc0omGs9OOdqaT1b3GgCyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ویتینیا: اونا تا میتونستن وقت تلفی کردن، اما در همچین بازی‌هایی بایدصبورباشی؛
ویتینیا علاوه برکسب‌جایزه بهترین بازیکن فینال یه‌آمار فوق‌العاده هم ثبت کرد؛ هافبک پرتغالی، در فینال لیگ قهرمانان اروپا مقابل آرسنال باثبت ۱۴۱ پاس صحیح، با رکورد تاریخی ژاوی درسال ۲۰۱۱ مقابل‌منچستریونایتد برای بیشترین تعداد پاس‌صحیح دریک‌بازی فینال از زمان شروع ثبت‌دقیق‌داده‌ها درفصل ۲۰۰۳/۰۴ برابری کرد؛ او همچنین باثبت مجموع ۱,۵۸۹ پاس صحیح در این فصل‌از رقابت‌ها و تعداد پاس‌های‌بالای ۱۰۰ در ۹ بازی مختلف، به‌تنها بازیکنی در کنار ژاوی تبدیل شد که به چنین دستاورد بی‌نظیری دست یافته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/22519" target="_blank">📅 10:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22518">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOJv9pBZD9sn5KPGjoB8XxocNU6fhGHDePicUkeWhCy5-BAmTpc2l3vmVeP9gl3gDVOCK1nNgZfrbX43bp5pDzjswMfcdZAEf6U3HONdVQSQHhNNvRoPMqNjKQyhIQGsGUg4TWw8kDbfuTKopLY3axyAcE6Q6PMD5cSMrkxOqiluhZYPNXG2PBnKMr9aa3OndnvOXxPF3wOgh6M6U5JF5GFVeaZHU3wT7qu_0sQ_M4nXv19aUGN5MA8TJfp_j3V9orRTXbNJHcvlA2xXwYmND0bj_iJF5uMRJyRPnWejq5urwPxoCsXPkHvBsMHBmsmSbGLLSPA66DpsTyqR5TuO_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
🎉
کافی‌فقط‌عضوبشی‌تا
#وینروبهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r10
📱
@winro_io</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/persiana_Soccer/22518" target="_blank">📅 10:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22517">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSr3i4a88R3odeglq7J6gaDvHX64MeK8nmNhbmXZY-nUI-OaVCNM84sHK4rnPgnex8uC10kNI30i89T3ehQbOTvA1jYEgq0C1DPjLoPE92ZUn1kmwqc1v-9Za8asDSlQk9GUactM-PosXd2aIKQVpTD4a93KnWmFiI-b4K4JBGjjyUo8yUH5ZJ9lZtycUiBkyrxNz20bZPacgfFXpXucpnqPsA7Zj-txRxx01ip9fD-PrHDtK2zlVdDwtDX-l_7aeQSjZ7IgMOTjfVtncZbAbMoGa36tYxbzMrfLZbxPcQnY_6wnExVAI28E9KQq3EfkKshvHvDcYylCqW8czr9wRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با بازگشت نیمار جونیور به تیم ملی برزیل برای جام جهانی؛ وینیسیوس جونیور شماره 10 این تیم رو به نیمار برگردوند و خودش شماره 7 پوشید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/22517" target="_blank">📅 09:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22516">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRGtYcYX-xgxwUSkQzt0fUhQYexxA14oAYzBzPX4rZ2q665QVLeqfJxAADY0xkvlnHboXagmqMAfan7YjPefXQ9IQhptxq69PC6oyTX2ZFIOQJAlzNW0gkSqWggjy2aiO20KSmK1ehJzru2nT25MsSWkHGoa2WReu_nh51Zvp2sG-QBKvBVYvPfheH5AJx__7S9i25qGGFe9bOGgm5ZG9gXVH27iq-UTUrohH4IVH_RfGmghItZTqy53RIbW5KPI9EHHwpJPnwMhHpII21yDjSZaCVW6uUOkhqwl9XClNuCwjjTZeJVskaEQWLlOJ0JiMA70D4PqMS7_KhrWp55e9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|گاتزتا:سران‌باشگاه منچستر یونایتد مذاکرات‌رسمی‌خود رابرای جذب رافائل لیائو ستاره پرتغالی‌آث‌میلان‌آغاز کرده‌اند و قصد دارند این بازیکن روبعداز جام جهانی 2026 به خدمت بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/22516" target="_blank">📅 09:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22515">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNMgVMRIBOuuv2oonpJR_rI7ibJgXSvto7ZWH_TO15xYV-KPkC_iSkCOCOOobo1av0tG0Tvl_btwp1_5ok4mrpj_XnUqfYCVLiWYQI3P5twTxTdHxbAtS5YEmL6PbgZ_bL0Vd1b3HZYXGcB2PEKy39KI-VLiGoQnqAJsVyH9OsHXju8no0K3CEdAFzOTJWamhu8K63I6cUhl2WZ0iqQvdV9jq1TBDM-VtiCv5yv4dhLRd_dtj5TTvgJr11G99BUadBDItcH1KYwbi-mZrrGyF3tLo77HJL5xHeHzJCD-glamtCop8nJHeaJxwsRQLv5p-UFCZhR7tII6djM1EQ5Qjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛ برناردو سیلوا ستاره سابق باشگاه منچسترسیتی؛علاوه‌بر بارسا از اتلتیکومادرید نیز آفر دریافت کرده که اعلام کرده اولویتش عقد قرارداد و پیوستن به‌باشگاه بارسلونا است. این انتقال بزودی و به شکل رسمی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/22515" target="_blank">📅 09:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22514">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aulmGRz6tDQ-5vyd2wUfdbsGu2GzdAmH2GrleuMJFABplvHyZmdnuDdLEdl8oFGjHBURyZyi_NsyYEOzQu69bfhiQU9TnHGo9zaoTZrwXUyWJ1iOlbT_1OH2V-Nc-nmJmf4JOmJbTKoX08eKfO034ucf6VS3kN0I43wv4wCa6odyfvpUzsj23K0jx7rXzfPRz5YwTvGA_ph1lGmEMAVzEoEMGMx3Lv11I3QUDl3chCECzNc07V05qsw_dKIaX6yCwGvXDmqeeLdgCc3Qn9ESxrF0-x2nVoPitSVFyQnqXac_af3oTnhU-p6YgSjHmwlAKLUT1lwrHHZW5oOOJKdjKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👤
مدیربرنامه‌‌های دراگان اسکوچیچ سرمربی سابق‌تراکتور: به‌باشگاه‌تراکتور قول دادیم که امسال اسکوچیچ راهی تیمی از ایران نشود اما اسکوچیچ از ابتدای فصل آینده با یکی از سه باشگاه سپاهان، پرسپولیس یا استقلال قرارداد امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22514" target="_blank">📅 00:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22512">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3mErtgvfzMSL0PqA49tmjNhD72oHRuMLV1hg08yJ2LZGlbDNL-JCtWCFgjCHRs9a2ZjKz04utYkH0r-f2rmZAVLnNbXC2dsBcFim58mevpAHWGSi1HEDobrcqoH2ZOFC3UmGIgogoKj1PF8vrh85MCRxVH4nPpLI5vUDHBqbE6RUfOtarBlQc4z8vNLOdiN3QrB1ixFP2fR5C8BdnAgRJsYiJpTwZw7qlZ0MiIuCBkajbsoG9_NCDMxSnHrQBd_CHNkGABh98jT8EFyFfUIU0KNCcVFk26AdoGYE7g2alTnHdYEWVzO3g9Fxbyu4-tOCWeRZG7ydzEgnXdk9JlSxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌بازی‌های‌مهم‌‌امروز؛
آغاز مسابقات دوستانه ملی پیش از آغاز رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/22512" target="_blank">📅 00:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22511">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJm-cTZYycEcTIbfp90RapBSPaFRbD9NGu_ZIanE7yUKgsMRFzgIZfdMBoah4o5xNOtsstOAi-qkK-F8tY3HiYgp1vEqTKg9ru1lov6-_bZEQ0Q7c-E9vkwfd19aXqShBY9VF12ytR__fVHm9FbzMho4aT_5jakeP-H9lh-3PSp2UMXbOlLMqiPdcwOB_2vU5PSfQDw-2wPTcHY8s331qAByZKBX9qyQoz1BgEL2nagwyzaYORzhXstaJAFzoUstPOs8UcY3tB4H9GdCb32w5AQGXN1d4JYjUjVG1hmDVevVvJdqtklr7RC5TJpRhtPnzgpEVjqqa7PLFDRy-UZxwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنهادیدارمهم‌دیروز؛
دومین قهرمانی پیاپی شاگردان انریکه در UCL با شکست توپچی‌های لندن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/22511" target="_blank">📅 00:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22510">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opNzkJm_reRBq03VhD4Z_sftbTtdCdetrSNz7jGhIrW62xi0DlqYDiKO0kqcvZ-hIm5crqzvq5K6VB6M_ytKnLVjOzbP410dV3IpBKj7TzF3NcZEeeyZFZ72aWihq3Yc8tMDV95NQ6-ID-0g9_sre2PLZGoUOt91cMiaKG5ZdVZLqceOXLqdCWnG3tFzkAWFqq3W6bP7JJo50iLboG9K5Wdj_Hv8dJd5HodgaWYuqCHWDzgzKD98uTjfYwNg3wuTKIEtwdKuRDScf99KA2MHeThDSvuGSdZmZwhdafJYu8RbbJ11iqrIqivYw27p5boiZjdly3Ikdyc3e-0Wp4p_rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
کافیه‌فقط‌عضو‌بشی‌تا
#وینرو
بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست. پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
a9
📱
@winro_io</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22510" target="_blank">📅 00:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22509">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tt1bSjJ8RUaie_NuoeqVKUEQmll713ITtsljaSMaLBpu7QgpDv5DZgnNVLT8SFC3DcxQpD9kGuwd7pjoWNDFLIaZP4ISUQfr5jKAmOHyKlStud7RkFSjy7PpQG8RYz5mnUwED8a9ifB-PTC2uxtwpQS0BRizjjT19TkOnrHlno7HbGy6-_TSwYFZZes_rbTxdM6RBMEt8ak5Aue2yrwIUNNubtvN5nrNg2IsKOuwaIQwy58ev1Bv37gFerHumK5tmrOjG8MmNb14sH5zrj4WzvNjMhXxewE9XzLSvekvH274PwY60GhG0uAtPeFow6vtp9D87pFyvSDD8Eo9Yi7mtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های دوران سرمربیگری هانسی فلیک‌ و ژوزه مورینیو سرمربیان فصل‌آینده بارسلونا
🆚
رئال
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/22509" target="_blank">📅 00:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22508">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXCd4xbvjB2xJGzXjwnBLaBn__r1B2fL1ZMYJ-lsB-kN7dZNcJxMGEvF2KeYEDA7i90zPpM9g4Vrg4Tmu4RFa6JPgQztNknBb6SaopPqSKJ1kgJ7sAJ81LKmEomimcpvF1UEwaqD5DNOy1l84_R1TPcCvrNwBI__pM2fs2B20N1mI_4Rn0PaIe1nJsG-YevLy-thNwrMulTQNXig7f11SLepIfKxjZCOeMOUr6b5VBtc9fdtz7QEFP96yXDqHsWZH3L9DWRzKD7c9wOmvlbOqCgJPkqZ_dOX3zvDBhqGORBGKKS41WoYgDU6XjszmBwHJ2n6gn2bdkJ36TI3Ny1pMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس به دلیل سفر افشین پیروانی به آمریکا باسرپرست چندین ساله خود قطع همکاری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/22508" target="_blank">📅 00:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22507">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmRF4nlbfora49GtzCSlaOfxNVI1aJz4_SSVNWWrK5yR5ZKfC8N2JMJHTYkdDv6DyuoQpkP4cxl51pzS_Un46-dqCxC5ooh-2h2vRvDtmeWe1ENtgMAh2XVKiJjpZvILaCKIQihvv8KtwkigzoGaDCIyLlE16VlLZEw2khLJq79m9G1MPvn94OOKTxYHX7NM1bZve3DKTL31rUYBTpQi-NhcYEdf1PUcwFxUsVP2_J0h67Fzw8L7Y02xDXfmz_XYNAYfP-G-cTdcbMmsTXSja6NxTLDhzWitBV-jgGzQ6dKhnzusF9xV-Fa6mYV_AyanOsVp2eKs5rKWyIGOXq3Jug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
تمامی قهرمانان ادوار مختلف رقابت های لیگ قهرمانان اروپا؛ رئالی‌ها همچنان‌بااختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/22507" target="_blank">📅 23:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22506">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMhH7AKb4YvsTp-gDxFVmjm6d2-7qW934cz032BpOu45fepeQur4bysZF7NwqK5lkvhofHyMenbgMkDdSWI2KyJ1PU7JrDiKcMYsE4B3zlXJqn1DKArQ6Xm-09GLMhhbZtbnTxbxg6E-DMiL-3-8l8Th9XgrSs4UEtogbhcBxESgsA2eMLTXIgEUbDaahj7LpHu94aZ_kjrKKcQYvbUYpBqj175tqX1Dd0bZ9xI5Vc5Brj0l2caM69gU7G6E3TkKybOur9YqwsW68887Je3TY7pVmvtAltYsbWiExbupF_gSZ7fjDnk-Scn-Fy88RPgHjTyUOq-IeN054pV-3vOtdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیوکامل‌ضربات‌پنالتی دیدار حساس امشب دو تیم آرسنال
🆚
پاری‌سن ژرمن در فینال چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/22506" target="_blank">📅 23:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22505">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78d5a3b7a3.mp4?token=ZHdDdsFPzFIJ6uL-Udg5ZdzMwzjcgl-cK2VAgn8ez61gjWAXi3br3eguMHUvA5nuLfTmWt8GJSL5i9Ha-NhOtLTu4LAmxlMPUpSHMPkLGBal1OVw_u563CinAecVRa3S807nnSDncNzgeu9JJAirKMGVrldwKGL2o2pcjToVujxubUXPe6x4x4KAV_GudcsJeq2TBfjRvehTpRlOriN7aeIYCDlikwDQL9PWLLKPJ9AFjQob0MXfJ7a-74aRtOEKvrJ-FjIsta00Ws0aaX4wdvpLky0mbFmUHWTYmGzhXbnhpe666In9LxGui_RbstBsLZcJAcaIJf-knjmLwE1L4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78d5a3b7a3.mp4?token=ZHdDdsFPzFIJ6uL-Udg5ZdzMwzjcgl-cK2VAgn8ez61gjWAXi3br3eguMHUvA5nuLfTmWt8GJSL5i9Ha-NhOtLTu4LAmxlMPUpSHMPkLGBal1OVw_u563CinAecVRa3S807nnSDncNzgeu9JJAirKMGVrldwKGL2o2pcjToVujxubUXPe6x4x4KAV_GudcsJeq2TBfjRvehTpRlOriN7aeIYCDlikwDQL9PWLLKPJ9AFjQob0MXfJ7a-74aRtOEKvrJ-FjIsta00Ws0aaX4wdvpLky0mbFmUHWTYmGzhXbnhpe666In9LxGui_RbstBsLZcJAcaIJf-knjmLwE1L4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اینم‌نسخه‌اصلی صحبت‌های امشب عادل فردوسی پور برای دوستانی که قصد استوری کردنش رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22505" target="_blank">📅 23:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22504">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52a1e84d8c.mp4?token=H17sHIaekiYDQYZJYnwyJw0XGhiVEu90eJbDOpVvP16ET5qV42qkz4F8ueAPY38ERVJH20JeQgJvABnmsfHSoRGEPFGhgtMXxJ4S8FgPytezGudnrNAgx-2fwGQFARBm68cCbGcSFp72Y1pBPlC5sqj1OHqmbCQJn4K8SX-143VHMUFmq-vUpr1Id8fJ3c2-KP02xg8qXzdCYYWKv9fpa7n-5gmImPG5TAQmj8uZHKCEar0alp93qciwWHC4IBtakO_FaPKZgmgIP_AF74eEDqvwaIwK6Xr1OQJZNjeZtaa9a4FE7mpT1yP8ejTulnPQ2cLmrAeilSoeObPDGlwgPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52a1e84d8c.mp4?token=H17sHIaekiYDQYZJYnwyJw0XGhiVEu90eJbDOpVvP16ET5qV42qkz4F8ueAPY38ERVJH20JeQgJvABnmsfHSoRGEPFGhgtMXxJ4S8FgPytezGudnrNAgx-2fwGQFARBm68cCbGcSFp72Y1pBPlC5sqj1OHqmbCQJn4K8SX-143VHMUFmq-vUpr1Id8fJ3c2-KP02xg8qXzdCYYWKv9fpa7n-5gmImPG5TAQmj8uZHKCEar0alp93qciwWHC4IBtakO_FaPKZgmgIP_AF74eEDqvwaIwK6Xr1OQJZNjeZtaa9a4FE7mpT1yP8ejTulnPQ2cLmrAeilSoeObPDGlwgPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👤
صحبت‌‌های فوق العاده ارزشمند و گران‌ بهای عادل خان فردوسی‌پور درشروع‌مسابقه امشب فینال چمپیونزلیگ و تسلیت به خانواده‌های داغدار دی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22504" target="_blank">📅 23:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22503">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVqUl8-pm1K0ZmfQEVRFM9HTiAwRj-K1kiUMIZWF7Prw7ketzkEJXWdXvXN-k-rnEwFnPZxdSqVSNpmoNZ9xGxm6GhTEtcaCsdR-2H670xMoX5QzLn7C9Xt50zBMGpKQ9CToCF-2ugmvNsSLN9k1XcEMKpSw-j753ue8456GBpKkJWplT2O1hE7gr14xHst8WjYR_IZnA9O56WsSRuu_OXfVP34pVer3SPnhvNPp1Q0PkL6wPk48FKZ7IyOxasXH_5OA0DMNRulT3yFsOEgdq4YmlyVZZc610BfFOhMtPoYY-illU_AkF8OiqDLKhR9QpENuRdP7Mw4f_KzPWQ0Xsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لحظه حک شدن نام باشگاه پاری‌ سن‌ ژرمن روی جام قهرمانی فصل 26-2025 لیگ قهرمانان اروپا؛ این دومین قهرمانی UCL در تاریخ PSG بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22503" target="_blank">📅 22:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22502">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d915ebc4d.mp4?token=O_h3BIez4CzGzhX_XdSdBU_Bu7ET9hJ4AfwIhn6KKAPuJTcKwi2mDtGkA_evsf0AGA7Z2yF9cLCN1f8jZSVoZA3ywIy6OwIoCrBRK6h5AyZ20dgWbkKtU1PE85cqtpmyDqyUcWXhXOrke-7vQjKK9iJH54x1oZakaOSNNf6UjNjhnVW7y-lUmFqDMVJh-FiRj7pzl_VNEPqknwRgRHwMX4GDSJe6S5bROOWaaDH1PCegHmUnxZ76OfcQzH4qGceAObMXwCtE0I5up5O_QPrZmtNA4y-fDE4rUSfP8cyRDhSVrX5BlpORX4gLhQce0Ynzc-ksrA6Gf9ABR8dujBG7JWue82sMGdFxVniEmcy3wId7tiGbSDWVhikpQ3V6nET68lUpT9xFTvYBKxPmVhD3ncYdHH_a3tGtz4qtu1xxyYAmyJydXmKLgX_Nx1KbO3GEmCb4PRa-6fxnalAkQmN11GGs-aTjOQ6qcdELKArfXGNroig_4zv22pYriyPJhUyXm7-l8toIIxaKJg9DQZGeQ6bhbBuQA252rEWj_UCiNigmri1jeq2VFl5tpKLv42Jy_3Z7pjaSJ6Oxmg3NK7cE3aBbGvLPyraTSddfCDMgMXajgRaD7D45yCAl5QjnwVTFkkWz8C84peW5GFznyI2WGkEAlcfi1HZqIlbiWKY8Yvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d915ebc4d.mp4?token=O_h3BIez4CzGzhX_XdSdBU_Bu7ET9hJ4AfwIhn6KKAPuJTcKwi2mDtGkA_evsf0AGA7Z2yF9cLCN1f8jZSVoZA3ywIy6OwIoCrBRK6h5AyZ20dgWbkKtU1PE85cqtpmyDqyUcWXhXOrke-7vQjKK9iJH54x1oZakaOSNNf6UjNjhnVW7y-lUmFqDMVJh-FiRj7pzl_VNEPqknwRgRHwMX4GDSJe6S5bROOWaaDH1PCegHmUnxZ76OfcQzH4qGceAObMXwCtE0I5up5O_QPrZmtNA4y-fDE4rUSfP8cyRDhSVrX5BlpORX4gLhQce0Ynzc-ksrA6Gf9ABR8dujBG7JWue82sMGdFxVniEmcy3wId7tiGbSDWVhikpQ3V6nET68lUpT9xFTvYBKxPmVhD3ncYdHH_a3tGtz4qtu1xxyYAmyJydXmKLgX_Nx1KbO3GEmCb4PRa-6fxnalAkQmN11GGs-aTjOQ6qcdELKArfXGNroig_4zv22pYriyPJhUyXm7-l8toIIxaKJg9DQZGeQ6bhbBuQA252rEWj_UCiNigmri1jeq2VFl5tpKLv42Jy_3Z7pjaSJ6Oxmg3NK7cE3aBbGvLPyraTSddfCDMgMXajgRaD7D45yCAl5QjnwVTFkkWz8C84peW5GFznyI2WGkEAlcfi1HZqIlbiWKY8Yvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیوکامل‌ضربات‌پنالتی دیدار حساس امشب دو تیم آرسنال
🆚
پاری‌سن ژرمن در فینال چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22502" target="_blank">📅 22:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22501">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50097d1448.mp4?token=lGNM6E1X3NJLmwAOAcyC6TU-uuDcfX7FvX6UZjwJEd0VzqDsr3N56aBzkuruZZg7yND7L-ZEkTaYtlCFYC8riLXPXbLJfMKj-mKcnTIV6HFeOLZk_W_9RYi5645tM3ZMN6iPZj-FDXMjMAUapvvXJkHQVZD76PfH-MK305rjSCVnC9gFSIA3zqzsj528RMjw7JF1F3AKITTkxTspQByq3wpTxMAU6RkE7cyLwb8vJLHgjuOjly_4mxX5w8EyLcGWZj7Kb_tstH0NmQ1V9vJ65IJiGiw2f5O4xNFvOreiwzSyZTiaMyinzzrSZhc0AKlt7-Fnd_FOHee_aYXIWYrtgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50097d1448.mp4?token=lGNM6E1X3NJLmwAOAcyC6TU-uuDcfX7FvX6UZjwJEd0VzqDsr3N56aBzkuruZZg7yND7L-ZEkTaYtlCFYC8riLXPXbLJfMKj-mKcnTIV6HFeOLZk_W_9RYi5645tM3ZMN6iPZj-FDXMjMAUapvvXJkHQVZD76PfH-MK305rjSCVnC9gFSIA3zqzsj528RMjw7JF1F3AKITTkxTspQByq3wpTxMAU6RkE7cyLwb8vJLHgjuOjly_4mxX5w8EyLcGWZj7Kb_tstH0NmQ1V9vJ65IJiGiw2f5O4xNFvOreiwzSyZTiaMyinzzrSZhc0AKlt7-Fnd_FOHee_aYXIWYrtgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
لحظه حک شدن نام باشگاه پاری‌ سن‌ ژرمن روی جام قهرمانی فصل 26-2025 لیگ قهرمانان اروپا؛ این دومین قهرمانی UCL در تاریخ PSG بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22501" target="_blank">📅 22:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22500">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhQeOU9pq0yJXgU9_FJeqx-2ZvbjHb9xeKLSpOHdoPg7n9ymgL0pPbNvfE3CLootEWJ7bXGR6VtGzgKXKNKaGmvWEzSChQZj4Qz6c4smrufkULGHBTkZlobRUvtx81Q3DzxTXXyhzf7ImGRxGTHfCBYP6mu9-IxKk6G7m0x71VxiaCru3fUNi6vOiRe3hd-CfqtuR3TJZFmKqepY_iPtKdQs44HglIBVyaykDF5kGSrFqaETNV6x-tch3OI7WPIwv6Jn51QNnhXDyhL_zO6qJIrT6q7J4wPVdeuYE1VHyG2JBc4dmhdN-CVQjVm_CcZ4ocpgwu0llFyyYM8N6vIoWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیدار فینال‌لیگ‌قهرمانان‌اروپا مابین تیم‌های پاری‌ سن‌ ژرمن و آرسنال پس از تساوی یک-یک در اوقات قانونی و اضافه، به ضربات پنالتی کشیده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/22500" target="_blank">📅 22:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22498">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c46R93KJ1KuIHx0rHROguWv4Nm5TVO2od1hT5Sc-L8I-DydwTNUrUSsz2AGlvTkgdTx2Bj4KIgGu8w1M-lt8XqBliwmUoTavfOP9jJLe2NHzNKcFLoXLEuxO49pHnp9pdBDcQDI_lHyZm7uLTW_frUtfUbTGw3gJiWUv6301f5pY-yx1ED5wqdwhKY_w10hqd8OJnbdVg5C3jQuzb3a52lW6OIf-AXWN9WLF0ZoHw0tJtEHWXwxZ5_FtEw8IPzEcanQdyNu01f098lbl1uOOOY8Xbrb60aKKW2jSqdHrLS54DM8x77wJeNI_1phCpzvW_-no0AhmK2QV-6eikojppQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازی مهیج و دیدنی امشب دوتیم ارسنال
🆚
پاری سن ژرمن بوقت‌های اضافی کشیده شد. آمارو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/22498" target="_blank">📅 22:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22497">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgqxalB68Es8dsVEO7AvKFtzxoa6wkRtZz0-cJxir3b8RmUlHoFTrNtm4dnlBCyeiYCGEE6uoPrtDWx9Co2QlkrpV3oJ8Xg6PNPHGW47vB5pJeNDgZ4pZzoXz4UuvVt3OBBVYAK9Lw10T3lSZlFlJ2vrYsnJArP34UFzyTPPLSmdT3JS5GkarJHJhpQIGKKtSzPEmLtCDajWzjKlDPE31b6k5p1WfEtYNQYwasXGQyNV94USd8DxjezumxZKJ5xFxdgvg6hxCpFgV2KIyZ3KFr4r9YE_aK3urSE2pO1cJ86L_04v8ZpP3SB3ZPu9_Dw8XtOPlcMT_RlEMICzKrEBoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|سران باشگاه منچستریونایتد به درخواست مایکل کریک سرمربی جوان خود با ارائه پیشنهادی 100 میلیون یورویی بدنبال جذب فرمین لوپز ستاره اسپانیایی باشگاه بارسلوناست.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22497" target="_blank">📅 22:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22496">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKuZT08MogQ5Jo_e57mTqNirLQXOlFmut-3QbrH-LC-tYrVUi2IpLyrjSxEIFfLe1xqp7rlM2vZMOYo1enOuZ722qf-7nfPnrK02mKKadJZwXgy3VlLftVv2yDH5ZQ4sqtAe5cAy-mh9nSawDx5y8noZnSsijeaxMuiuEkSgcrnHmbC9Gd8YKYpKPtqADEUJvKNzCNCXdmy1J3wPWR0i08rThDv3sTf_mKnkNF6T3sblWZokvSySLJK3CmzYcXflMRt96fa6UjLCj64kh4vjpBVK5culkmcyGVWX0fGRo4vPA6G3FhQaY6toaf6dva9hiGGeiXYCtf_oLW7jUiX4Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/22496" target="_blank">📅 21:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22495">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O96aoxv3S9af4fkRxQ0boK1gm1pA-t9gCTL18oiVnB22MbMYvPaYW8ZpuLge80kvsmNfWo1NG5D6fA2xWkSGKrtDEsrfvtNo_fzCbZrCopjRKZUMF4P5PivPEbv8RSDqtEUzZifjLsCD7T7k8zUi6KgZRTuIq20wp4mU0kP46dE2fef4WPF67pbW0P8Sibo9vElgrywAJTC_fRqiqUJz2j6ew5NtqBPWpuyslmuUgxXL5P0-s5PRkJvUCS0B_ameA011_UwBKcDFnP0k5XVkROEReD8hf3hBmjPabkyG-mVq3okO4jJTd30_dA7xumsGIEPIJGt0XaiXaPmvfu-TqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تنها 45 دقیقه تا قهرمانی تاریخی آرسنال میکل آرتتا درلیگ‌قهرمانان‌اروپا و کسب دومین جام ارزش مند و شیرین فصل؛ جای عارف خیلی خالیه.
💔
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/22495" target="_blank">📅 21:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22494">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEx-2LLmFFd_btN2nkiwPEX375rOZy6yb-pAiuHVV1Bopm2X4nLrhwW-Z2I7QqJNcQlUOHI1qxt_osQ0GXF9fIgAD7zRaP-bqSaqHFQWKRUl0EHteEgh8RzK0nIF95Onlays6PrnXG2GRPzmWAPLUm8LhIEZAdZ0p-mIS61tF73glc_FA2rqNcHieE9V2I1wZiXGOW18sm7cvuFArEINNxM1yu_4ezNfYQo3XKs-vz-uFybfQdrqfVc8CDbgN9GV0HGlmIUfuR6rHXSNLZpGUZUYov2fULj_fHlvCjnsZprxabdzTXDPimbNiPNlWIE-W_-ZkbEpJCxcSTvZ1beb_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باشگاه پرسپولیس پیشنهاد مالی بسیار بالایی رو بمدت‌سه‌فصل به آریا یوسفی داده و احتمال قبول‌کردن‌این‌آفر فوق العاده از سوی این بازیکن ملی‌پوش‌بسیارزیاد است. سالانه 80 میلیارد تومان پایه دستمزد + 20 میلیارد تومان آپشن.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/22494" target="_blank">📅 20:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22493">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYeq9LV6gEt_rNP8D93kora1aSvIgsPp6EfeyL32TQ7zNb1pzMQXGkVUHseOzoFKZBJrGxaBCko35tzBvKnJH9DVZA60ZViS0e3pPAxakh1COzs9hskCka_tYHn99st1GMCVR3YfONgIE-SSMWbdSgSGVf2_KQvSntNzDT2ZYwexY4FKBN_QZHHVA44i84Yc8PO_FLL2wAQ-LQlqNUm1pXVk1vEzJoJ3pKBPLWN8pc4OPXeIHDsWNBLNZX_StT0h7nMmDPtgA-ICpENGH9LwbhtKKyEpgCVjS5Y1OmZAYDVXlgkHwUK3G1f7mhKsr8BX-MnKggR3W9lTK81TX2mypQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
علاوه بر دریک؛ این‌مدل‌انگلیسی طرفدار آرسنال اعلام کرد روی قهرمانی‌این‌تیم درلیگ قهرمانان اروپا دربازی امشب با PSG پنج میلیون دلار شرط بسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22493" target="_blank">📅 20:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22492">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a443979ea7.mp4?token=KnQr5CC39p6o6UlEu3-SHg2ofO5tlPwBVwDWUUZUblME5qa6ikG7ABZs4fWPAsfG_6O_47XOE8MdaY1Sydiz6FvnLOilQ9mamij2EK-INV0hq3iqz20ihRT-ztCbjXOuTkclwAgAlZpE5f62EMAZ4AHv1ay9lYYw4yeEOQHXMavI558n-m6mlofvWlyfmEIvhzuT7I3F1SvXPLDJhz5PmN2J83R3y3uMtN7BMZUXRXXdGjUOJtQ0ghuGumKrbIzfXxlNI8DyToTT-wtCG6TelvICl4_SYJg9ybn-cKEf50gyvly8CJ-LLv3zz3JEbo5537VMrNWeiVBFSG07EDiAfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a443979ea7.mp4?token=KnQr5CC39p6o6UlEu3-SHg2ofO5tlPwBVwDWUUZUblME5qa6ikG7ABZs4fWPAsfG_6O_47XOE8MdaY1Sydiz6FvnLOilQ9mamij2EK-INV0hq3iqz20ihRT-ztCbjXOuTkclwAgAlZpE5f62EMAZ4AHv1ay9lYYw4yeEOQHXMavI558n-m6mlofvWlyfmEIvhzuT7I3F1SvXPLDJhz5PmN2J83R3y3uMtN7BMZUXRXXdGjUOJtQ0ghuGumKrbIzfXxlNI8DyToTT-wtCG6TelvICl4_SYJg9ybn-cKEf50gyvly8CJ-LLv3zz3JEbo5537VMrNWeiVBFSG07EDiAfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دریک رپر معروف کانادایی یک میلیون دلار روی قهرمانی آرسنال تو چمپیونزلیگ شرط‌بندی کرده.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22492" target="_blank">📅 19:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22491">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHt6_Yt6meqrOf4-vGuq-zqiL32jUMI9hhom030SnZOJPEBnjRlGnzkXE5_pzlC6Ijv1F1_fwpo9e6VTjOdMKtRr-pU-AbEqKfr6x6rES4Rms7xWXbt3azwgQgzAMypi9LaRwDFjYKfthox0fxGso7LQkoi0DRNVPnHX4aRZiQ-srVk7YVjzQ45egIJFr5Js8kmUG2shNDmV4vbltGp9D9okffBU2EiHN6gksSo6eqEsiuJHAlufh_YX-9MhLXL6kUHDEKNEuy7K0gjhhdl0PuXcqZpusXgng7Br_0QJPVbwdMjfFkaGdklv1PaY9VMwESLTT6o8M8QX3c9_vAUmLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور در روزهای گذشته نیز خبر دادیم؛ آریا یوسفی و محمدامین حزباوی دوستاره جوان تیم سپاهان مدنظر اوسمار ویرا برزیلی قرار گرفته است. آریا یوسفی علاوه بر باشگاه پرسپولیس از یک باشگاه اماراتی اماراتی نیز آفر رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/22491" target="_blank">📅 19:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22490">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyGrXfNkUvyEg_rMLXIvMo7Ss4F7lshzepUYiz7WevBr3lQpxAl5hnQ-_3LS0gwKQ0BXD3q2vsasXyD7GL4JCjn1j4o6pKJoUohs4zP599VfYqvFyhMYOwS4JordIa0NuePIqRDC4NqmwiHXY489UE0Hpfm2fIm_FpYMJMH2Nvr9G4rAO-tCFvfqbwmCZyAHA79A45CCWuHXovlXs9wvejOT154Es2A2lGRj0f0wm2ao1QhIVUoSpma7P5vdwghGuo0SM2N10xaaz82_QS9-8iTnaXESjGGG14tdpLx_q5GzENEp1zdyeH-03LK-6WzUD38q60tko9HezqTh6s67SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزبه چشمی هافبک ملی پوش استقلال نیز در تمرین روزگذشته‌شاگردان‌قلعه‌نویی دچار مصدومیت شدید شده و ممکن‌است به دلیل پارگی رباط صلیبی رقابت های جام جهانی 2026 رو از دست بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/22490" target="_blank">📅 19:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22488">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGFb-chnJSv9yld4v8Kfe_zB30RzPslrRSt9i5xfGUmojeml-qHQvFHKb6dReC_tgm1yF7wLMVxH0cbKMqh-7kmFD7LiQwLRByRBAFvMPdQimkXMwqExYQuVdgkz97LUtMPGhpztZENXfpENsHF688jkb5zEjL0MniC9UfWerKzw9d11tdEpS8RHwPD_MO_2R268x8oXYkofVmKd5YknsAXUXLHea5iHJEzXA342qH6XUtD2qWqQY_TE34-TnWIObFQFrRes5VABCVPDZOmV1vqFoj_kYsu7h1z7u2P_LoTAbMS9sl5Ge5bHM9-soz27zrYBkSxaFGTL8mkHjHDRFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور در روزهای گذشته نیز خبر دادیم؛ آریا یوسفی و محمدامین حزباوی دوستاره جوان تیم سپاهان مدنظر اوسمار ویرا برزیلی قرار گرفته است. آریا یوسفی علاوه بر باشگاه پرسپولیس از یک باشگاه اماراتی اماراتی نیز آفر رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/22488" target="_blank">📅 18:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22486">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jh_G3P5tCxtTnnAxbgbAoLI_yNTu65ryFvhy6-64rUaKpHZFYRdYkHWM3HOxZHmF5BbhRSBrjSa-td7IsCKZJc-DzzKVIgWY_uB4Q_AVEwitfRXhBZ8wlgrGwerd8vhvx5YtxIXk8kHJ5UWMDYYjPqlWtqoek2hxaWWxnmD7Bt0m1HP2h9EYugHeJyNVqDwvgOP1r_2KaV-f-uwHbg3d9qsHv3HKWhh9h6LZuiHlfnnfvyhNZ5X9nlG-CFveNqz7abc8gqR5FXK6vONl3UwuAV5ykkn68OKFkGFetiHNBIhlZ3lFf6Wrl06JuI_jvxvh_1znQGxVuyqd2HGFla5ELA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SoxC0d5ktucUyN7nU89A5vK18vYkgZbORvhSEodWxhV5ZZlLV5nbf-wJoQTZUmpZdpUHLrUQcoBBTo81ex6cOiW-DWfq2mnp5_NEszaSGXN9Y2MIfkcq_t8jjng54CmgkJ6NLdCFgW8-wwXDB8Rubi4KigSHDvGir6awZBLAOF8VcMULkiTqb7Pt0ED_okdbgiLG-_fEDL20_yZTF3xgHhM-ZwDB3s34xztwOGcmOJ57WxvSd0Y1vAsdqKbFR8CziZN4-eKrDzD_jtBPZBJgh0oO3x3gcVUOnflrQ3G6GC2AHs5ZHGxddeDfworC-aea_T2r-OREI6Abgb1TJVUBiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
شماتیک‌‌ترکیب‌دوتیم‌پاریسن‌ژرمن و آرسنال؛ ساعت ۱۹:۳۰ با گزارش عادل‌فردوسی‌پور ببینید‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/22486" target="_blank">📅 18:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22485">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDntENtaWr7zieUu7vq8mq9tYm86hZ1KCLFKIFACz-PGFCmbg_9V7HM-hxeZcjM3dNEvTB2KNTO9ZrIseBUxIEmZju3puruxRZWpYmI_DzXY6SlMw9574guzAvnDnF_s9596LUIM-GL2Z-x8-4YS3egJZ_LZizM8Zm39U-H4FRSJa1SaHiM7kHiB4IR1Y05r-o5ymUWfoW3PMfMFMzre7lwz9NXJi6Y-zCmvfkaryAhf3gg5OP6v8Qz_P8a6_RvN_5Bpg7TXJpUCUOljjt90cKO5u60YMJp26__fvA1r3YFP7xFieFCLNCVUDiCD9KWhaKnW3csetBy1ScZ3L2gx4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکردفوق‌العاده‌داوید رایا ستاره آرسنال در این‌فصل لیگ‌قهرمانان‌اروپا؛ رایا درصورت کلین‌شیت در بازی امشب، رکورددار در تاریخ اروپا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22485" target="_blank">📅 17:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22483">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6GgJGt--H982H2SB2Xpjh-Z3zwBpa5oM9NHYLhZSmupwDPuix5lMPG814AN9d09BAYO82KWzABYCt3R3r1bMG3ay4cRkTYAUgchQGBHNhjbsVy6oBSvJPo3ybURtU-o86v3fmci64mANXSkZOXGSMnC0mYa9dWZYJvPSsF6fV832GMpyQ5cY-QYKYG3BfpRajoY9y8g4NEEQySfUtAM3UH3J0jmiCv70xKRPgN5tg_umvT3I29xfI46vgO2W326SDuJ9qEAkjhps1Em1M-h49SAu9to0LLfgyUyyfXRe_DnbWHJ76IdP7Z0wMPsybPvETi6nboePbj21PNieOb4Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22483" target="_blank">📅 17:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22482">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATWwUcNBah5L6F9Ui5qiLrdhFbmFiFEaQlJl0_eYiuZUvLEcqXPC-q56amIBneYIkhoydTBrAfd_2mzrge-6Rw4owUyZS_x6z3dZU1Y19IdhxD7JOxujUFP55lJK71UOGlpWhhnjSr9JhJBfhOyOjohP_4QPyNSs7SFsMUUfJPxOIWmEEsb-b5xylkLeGjEvTvc3gKNRpafho3WsPh_fODfFd5QnK2VxvnKGuX9Wuoy1KCwoML0RSFt3EDLo0onz7M5CeqFL3KhJbQ2hXsszXbK4U2PlIGvD1g0brqlwCVqDUjqpmFLxXFEJWi3N6TDFp_fpIK2PvKZLNcSaQBI5DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22482" target="_blank">📅 17:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22481">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aparat Sport [3.6.2].apk</div>
  <div class="tg-doc-extra">8.2 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/22481" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
#مهم
؛ رفقای گل این اپ آپارات اسپرته که تموم بازی های مهم روجلوتراز صداوسیما و با کیفیت فوق العاده و با گزارش فارسی پخش میکنههه. یه قسمتی هم داره میزنی رو صفحه میتونی هم زمان هم بازی رو ببینی هم تو تلگرام و اینستا آنلاین باشی. خودمم ساعت 8 نوبت دندون پزشکی دارم از طریق همین برنامه نگاه میکنم. عادل خان‌هم گزارشگر بازیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22481" target="_blank">📅 17:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22480">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSvGjygDAp4449rJEQW5fI8nqGJvMzSu6Zwa3okYa7VPaqFaNnUxOoFZCs1VwHlxAQiY2uaikTV_j4swllpbkKemU8ceFMVEZLNnxKfBCHjn1ruXzFbyLshXNISdnX2X-dOFRvMP_NjOlyFjcKj51cWGQGHuNbPeiJXzFP-HUXvKwd2jBR-sgzQu8U0D_CSoISnOPTPE9UxL0N8vN333woyxK7qcmx3UDgtlfb_peg_VkZe96KDJPeiIUNnNV1yGaGsicn4a7ZXCURx_HR7UmhGOH_GbA27Cla8nMWoktJeTMf9kcUzgFV4ZKID5Y4KQdILjNLoSNJTX2eJAsnbK-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22480" target="_blank">📅 17:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22479">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caf37364cd.mp4?token=QF2OP5zrrGgdnIgTKbRIoU9shZ2ltzAYf1E-A0G7zFBXPIEzENoxEEMii67ZpZjks6p0wYFY7rWYdIXJnXeolEe-2NcAjTOeANb4Cwwpa4ss5fjbAqlttuyIKlP7duIfTnnCgKKKNtl1zBp3Y2XXl78IR39TgX_LzJfwNCFaNnMDyjiwoFl02R_xs3N44coTGlJKcM7db2VhaiZVKVaQ-irliy8cBG73SqTCwcovS_YcOgxqYldEOh4gwSZO_1pnHO1MavDjEoRynstC9UyJ551U3XtjLNULlcnQD-yTbHdHKrQ_xaYG76WamYmkhdFIKgUEDvYpW-Nrnvia-jW_LI7KobcLYF8X3pEnfzMp4Hbi5yed4HZ_azDOwhhN-ZspYYmrpy02DKgvo7MDqyvXKKGEfBwkRwgbXUsOkUVC8kggbmK1uf86EZEBHjTkqWWXVncHn1Loox3pnzPe5PWdnqoV0b75JldJ7tq_OaqoPGAoxgaYX_9vFM8ACoONkZ9WIdqjLZmEXBHqhlIz6qisQQ6dL0gF6-vEDO_-Dcw1rLr3-hV0Pn8pbO6Z7BtV2be8gOsRZ2KQVmE6DdkV2jx-79YarAhiy1bzIrGsK2Q0XzbOGXxDvoeJzrNir3Pdijw09pueonm4KFnPsDpolEYipsH1qHocadZQCWE8nV9ujo0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caf37364cd.mp4?token=QF2OP5zrrGgdnIgTKbRIoU9shZ2ltzAYf1E-A0G7zFBXPIEzENoxEEMii67ZpZjks6p0wYFY7rWYdIXJnXeolEe-2NcAjTOeANb4Cwwpa4ss5fjbAqlttuyIKlP7duIfTnnCgKKKNtl1zBp3Y2XXl78IR39TgX_LzJfwNCFaNnMDyjiwoFl02R_xs3N44coTGlJKcM7db2VhaiZVKVaQ-irliy8cBG73SqTCwcovS_YcOgxqYldEOh4gwSZO_1pnHO1MavDjEoRynstC9UyJ551U3XtjLNULlcnQD-yTbHdHKrQ_xaYG76WamYmkhdFIKgUEDvYpW-Nrnvia-jW_LI7KobcLYF8X3pEnfzMp4Hbi5yed4HZ_azDOwhhN-ZspYYmrpy02DKgvo7MDqyvXKKGEfBwkRwgbXUsOkUVC8kggbmK1uf86EZEBHjTkqWWXVncHn1Loox3pnzPe5PWdnqoV0b75JldJ7tq_OaqoPGAoxgaYX_9vFM8ACoONkZ9WIdqjLZmEXBHqhlIz6qisQQ6dL0gF6-vEDO_-Dcw1rLr3-hV0Pn8pbO6Z7BtV2be8gOsRZ2KQVmE6DdkV2jx-79YarAhiy1bzIrGsK2Q0XzbOGXxDvoeJzrNir3Pdijw09pueonm4KFnPsDpolEYipsH1qHocadZQCWE8nV9ujo0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این میم دیکتاتور داره هر روز سمی تر و سمی تر میشه؛ تاثیر کیلیان امباپه روی هم تیمی‌هاش
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/22479" target="_blank">📅 16:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22477">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YDXDNySxefPQf5ya4bJWPWltq_6fBrG1dz9ugCEux-9Llr7ZGNHgROD3xGc5uuNNcc-ufoeJC1R66ntajX_efL7RVqsGyVVhNxePWwLgjS8KnQ6CR112ogI8mYwI1hY9MeoD6bUu8p2_hzYwN-14Z-JzKhIpux1DbWcq7P6gqYNsnWZMIH9F_obRJ78piv62LlOSqA-ZQmiTdpJZl1Qa-MMdEFKft7IAqPpie-YmgZ60pIxiPnI8T_2xeRZT_oCSQ7NapfEDo7h27pIQlgLHKNg3DbavtTcM0zKkJqM_MfxT1-pNsIAZREsDn4daEal_3GBi_B2Y1VzwvUVyB33m4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/on5_QwTBeMdFjJLVghAbBgH6rfJKhlGIiYdfHPooSAD5V7OHXwtYruJeiwyVcGVrgiZskwrO8F2gq-wgia-ODPuuk8GlZzSsP-cl0xEPK3AWJLYXTgym6dQI47J3uA2VEFcEixbIJ5ftqLBjgzaci9H4uWfwkViPjKwkWUY3lir14BhF2xIQTa16rr1GfhJ6vO5SaT6nsIumrCLOK3qC65dQJLlftPdzdzvG9Rgk99TKFO2X37uOBmwVqdjEqcPG2xQp0SEPpa6BSWbCCxeIW7aOeKaN4zSHodoUZhvpKl3oPWhscmIfGxeYSBySDEdGaDOaU5cczQkjK-HzDQYE2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇺
مجری‌ و خبرنگار بازی حساس امشب دوتیم آرسنال
🆚
پاری‌سن ژرمن در فینال چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/22477" target="_blank">📅 16:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22476">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lB1GL1bl6aTTvmc7BEG26eXbIzCpTaNFPtcPCQ68xoagwqLKAxBe99056NT1ADC1H5WNAMZXDhOszq7KXKnwThxR5EiGxOF4Z9klYR6QZma_9sTFiVl7I4oMb2-nrE2cxHwF0-Ntk4TNI5ZlsBdGi2UMeWF_yDN5oDaM1FtbrKtpY8gtjPJNYVAh87H-hfzn05aSSI7PaYqpoQObgkMfNAYZ4NnGAVIO3TurtoQ0hKyAnlOlc0Geg4zFvfZ7qOpn_o5Xa3uRpeQGU_w1JaJ14ab2bNIySn4YGxdy6A-kmAKVfrH1oUGIcB4_t0ydp6lk7ToaufFU836X-ctNDJm_hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/22476" target="_blank">📅 16:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22475">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d18fefc27.mp4?token=XXMy7TV0IpXroGT7Q3tmxvGJ_6FK77UgSy0aPk7XN3StNyKUDmHrEqn-wx5EUXzxbPK45oQKWknDnIH7ybSSD5LGeaxI6goxEtKlnVZBBvJ4t2qsvsn1RqSCzOJ4FE6qs-r_nbPWORFMEknbDsVkMcDxgmsuqM2O7LpO5710F8loUvYNDvAIQCCyZTOI-wuA4FV33M-4bQwqwZyW-mplgPbsK-pIzt_0qWywHsMhyV2XLz_XVsQnKJUSDrsujf05FSeY1WbgHEqaX7as4V8YvOnys8WCwr8Ewc-w5R8SVgGF06qV9CRx8Ua0pYO1GTRk4-JCU0M53NNtbDt7iy4SKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d18fefc27.mp4?token=XXMy7TV0IpXroGT7Q3tmxvGJ_6FK77UgSy0aPk7XN3StNyKUDmHrEqn-wx5EUXzxbPK45oQKWknDnIH7ybSSD5LGeaxI6goxEtKlnVZBBvJ4t2qsvsn1RqSCzOJ4FE6qs-r_nbPWORFMEknbDsVkMcDxgmsuqM2O7LpO5710F8loUvYNDvAIQCCyZTOI-wuA4FV33M-4bQwqwZyW-mplgPbsK-pIzt_0qWywHsMhyV2XLz_XVsQnKJUSDrsujf05FSeY1WbgHEqaX7as4V8YvOnys8WCwr8Ewc-w5R8SVgGF06qV9CRx8Ua0pYO1GTRk4-JCU0M53NNtbDt7iy4SKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مورینیو در اولین بازیش روی نیمکت رئال مادرید وقتی دفاع کردن ترنت الکساندر آرنولد رو میبینه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/22475" target="_blank">📅 16:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22474">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEmC_Wt56hdUezatNN1eGLRrkq2elu9R2Zyj1v0bnfHaPUW1VkRFAAgbdItroMmuwuwigsixMTiATJz5u5bCxwWyEhIR5wv-8Wkw9_SwJBq_kVeKapU4kyEFLzn8zh8_EI5sC0s18AwJs5jP_RZ0o0cO5xCXttz2SLk4ciIa5--vZuQIt8lfPJt4VSp9dnuyo3PXeAlHR68J-hJuNvarmxE69HsdYCTx1elNRNLgh5TFaZ_E1gNhztcEClgqXN_qHW41coTMJWabkPe5Cpq5FjIxf6y0yofbvG-67w8CnX3eqeWDuiLs7RX-DnWFiuYGg36HnMPW7pCGMltsGRyx6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|ژابی‌آلونسو سرمربی جدید تیم‌چلسی خواستارجذب آردا گولر شده است هرچند رئال‌مادرید این بازیکن راغیرقابل فروش اعلام کرده مگر اینکه رقمی بسیار نجومی پرداخت شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22474" target="_blank">📅 16:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22473">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvzQxe5BEwUDwSZuhgjqCwKNl8DpMKj6N4Er33mgQqOCBSc3KpjCzdR87KsOlmPVn3_UjSudZ9LDtYoPr0_ljj-06NRQczYvVV_-5Svpjn2Tk5WUlknhW4jdsw13UcUTEQP8Ms8RhpEDNiExKT1nBu9RmGowZqrIr6COhsCNQG2cwTR3et_SUN1WANJ0ZyQLTpiXuXjtf2H9xwP1k8PeYJ5ECjmj--GR-KkTU1WYjGssYhiXJd_0w_gnI6ZLZyCyt4-vd_O-XvFzpiz6gSEND9KMxs8qsz2oljVKXRZ00st6QhZOXsJvXz2lAsV2RWgzvyE8htkkpqQa1vQ2E9Xa2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکردفوق‌العاده‌داوید رایا ستاره آرسنال در این‌فصل لیگ‌قهرمانان‌اروپا؛ رایا درصورت کلین‌شیت در بازی امشب، رکورددار در تاریخ اروپا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/22473" target="_blank">📅 15:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22472">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHpdoQd5Prh1e781cpp2Xr_8jKG0AGVXyNAYY3hpRel1nfyaO9lVUAV7ZYZ0y1eVY0d3U8Gc3KfFhqAy-144NwEt8RpOd4tg2G4pMIsAScHQbh_H8Tn0MWEzT_TiFdEBx_zwlFVE9jFErrSx84NC6qVJkZRZyDdFYhK_uS-g18zpzQNEqhmRhp5cXFDumyS1i0Nei188eF4Wj_bcTgBdgvCjpxnu0NCRcBsCTDWNhNoE3VGScredINGvh4uZ0EZRXJRuQmgErRw3ZaQ5YPnDkHefYO0MRbkEq3eLDfWtX3J5Su3Uq9gYGiZ9Z9AUXfHpDlHKzsSyt2Js3cAnTOF63A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه بعدی اتلتیکو: هیر وی گو؛ برای پیشنهاد دوم به مشکل برخوردیم، بلیط کنسرت فردا تمام شده، بنابراین پیشنهاد قبلی را با ۶ بلیط برای کنسرت یکشنبه بهبود می‌دهیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/22472" target="_blank">📅 15:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22471">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrccDkt0QtKcEnEa5HHww7-icNDGoWpnhbXizVjnfXSFdniEpiSWjdNHa5B79KShBGCg1eRIy6nCG2JwWZLxbFIGtg3JUz6tH0FnfkSdeqaZgyr_pQLjD58r2_PUUmddIGRIx_YU6yksrpb5F_okd6Fg2EJqsfUMQiOJsy8_WPdOGGdLxCKu0EaovgQnBjCufTDRSmzW1rBBKW23nPb49vKFGto-Drcbb9-E88BCcnVlfnEyIZSDyRAPtf5gEv7TxT6L9yxhozgfK9z5Gwmo71QRSalQp-W9mhzYgae6pqMRQMT1iironhSNCxVX2p4BlaYgudCVQkVizqvVImRZ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سیدمهدی رحمتی سرمربی خیبر خرم آباد بعد از اختلاف با مالک این باشگاه از هدایت این تیم استعفا داد و به احتمال فراوان فراز کمالوند یکی از بهترین مربیان ایرانی‌هدایت‌خیبر رو برعهده خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22471" target="_blank">📅 15:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22470">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLfV2-VsGSQtyU_28pMDlcHhMCK6EQCPwEGTKj-8NWGyaUy29v1MjBCsqGcmd96TYyFB_bICoTyiga76fPLzUWTTQsvqPNVC57NFyu4FoCpO09iI4Ef5FOmAbEdlSi1OBTj0FlIDtSzPMt19SR5af3ADSDbZODS2Iexdl_4aNbtBHbtY_X68yuIbo-I8B0D0IVq7Pf_Loj8GrPrVanBN5ge5u1QESSL8ZbxhoY_3B4VW07zTk2P5Uvlo2wuyQBiZrkX8X-_FXDviDdfqfAWpI_mpeE37evQRu--018rMyhnThtqG7mqnWYFNHEyjhERTCvZMo2py1w2NJYZsJ-nd3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/22470" target="_blank">📅 14:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22469">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6gCPsvvJEnKquGzeQFiyxJhkzUrtEJQEWO0zADTFzWOCgTAdB5V4Sbvwy2vKQU9V2o3ltf32OnSIMwKu9Vhww1hZHCmXbTUjrKeDZswJiwB4CfCUZOhKhygG5zpxC0lsqP7baSKsVFJqV_p8H_ZqnJJFluB64bYlnDTVPd2PyY16MCDOCCP-vCtd4KcoPGQNBSINkBjO1GAKkA70zF1kDCa6TrD6YMjDwHEN4O2Bvzubk__XxJxzOtC4h9IsHAlaMedFpbcp--pn3naKNgdz9ueFAN0on9LfRKQv0ac7oG38Re57sDRL4-Sqggwsq_h4j4pO-2qxEqWsVNOys4cMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
#فکت
؛ کریم‌ بنزما یکی از بهترین مهاجمان یک دهه‌اخیر درکل دوران فوتبالی‌اش تنها یک دوره درجام‌ جهانی برای فرانسوی‌ها حضور داشته است!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/22469" target="_blank">📅 14:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22468">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwxZxncMLyIqqQwLtQguNNGqye-H8uc9IQ0RzsP3u2KynNq9ZbdG-xm3SljMWAwht58c9bfyPKDNigtgYUhaN2_nbCV0km3uGIJgE25QrJZ8ckNXlBPGwFTv0pWjICnwWbGZYe1eKAOqjy0umoEnEqIWVYEKIA9VKh_loF_aUNudR0EAcx57b1qYzWzjgetJyavJOByvL0rfcUFyBXVyNTs30Bu0F5PTIkC0tOELV4JjV7KYjmwnp4jW3lVKpspsA3QO11ble14glKm1RfTLCoNzNGaHYyCeIsj7KdHLADlMVZvzq5xtKmQHefbHm25QiixU-EWVhqDCnRxCj30luQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇪🇸
پیش‌بینی ژاوی سرمربی‌سابق بارسا از نتیجه فینال امشب: PSG بانتیجه 3 بر 1 آرسنال رو میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/22468" target="_blank">📅 14:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22467">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPrFesDiRifCaML5Jna_Vp1wNemFbWE2NM6tvKQy3nCMkdkAQ8WjallCIYDzTMBqZU7-7whEoDNuHND9udA1Dq_d-WjjfQf_NAhZO0O6KCemuRxk_YVQyAwQtNTHHpqyNp3vJTBSHUQxgOgieX4tUW1zwPoCfFeNf7Hy6Xazrb73-XSEz2J9gUm8a8OrELnTc8bn9UiRlzCp8kCAz0uaKtnK6CnRcBpQmcGb3ewNOxBfXTll3VSi2ASh5ZSGqpxkkxItgE8Z6hflPsa8eVIobtKlAwkd74nlHQ-_wNkogJ0i6l50yre19BquUEBrN-s20QLDXX3xpflJCFPv_9fwwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باتوجه‌به‌‌مصدومیت‌های‌پیاپی در فصل قبل؛
احتمال‌اینکه امید عالیشاه درلیست مازاد اوسمار ویرا قرار بگیره و ازجمع سرخپوشان جداشه خیلی زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/22467" target="_blank">📅 14:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22466">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d381ZrjknsY_ZfUpOVJPiX4SLHZgsvnGp703pNcICFTT7jDQCn02GE3LDEVSfh5xrIfpQ-sJLR4yOs7nVfsxqwAgDwv7banNJt_MNC3YiIeD6YDlfOWppeWCeAMKr7ApRL_BZNSb7OHW_miHt7X7mh4qs49kkAH-y4dm9eL5TW34dXj9eYxqZsdWE-1Tgs-L9pssoox_MAN7USlfIkrIQ-zX5XX2bYa1jSs1U0Vhyhqi1PbvbAaUTfrkw9fSB1hi1C4sxV8Tj8z220T1-QFUCbqe6M-medAqu8UMHleT8TXlVX5riXYSEfr-e-7B3RohHf5gN2lLqo5Wd8cKUtj0oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
ژول‌کونده مدافع میانی تیم بارسا با پلی استیشن یکش رفته اردوی تیم ملی فرانسه برای جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/22466" target="_blank">📅 14:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22465">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-61iPI3JMTtZUIEIKuDu6JaTgPh3AhKg9HVNPVg5uNRxPdv_LHwAr7gWM7L0LN6yQbxU64x1MwT7gn5IqAM2FdCBqzrFaS2M4S4l81tgU_LfrmdhcfqD-nKVn9LMsKZfHKGSGjfvhV1weDjtrFPBijvS4VYQNZgbrDTvs2t6rz6o027NQbgdrCL8hrP-DXB1p4-w0ip9d1bK5BnSbYlGbpSKe8KwK9uKghDV_i4rr91dJa7pgh-wtP6q30ADOWG7Z1Pp3NKY3zXq6Vn94UKalveCqQMgJxxQjVxEpeRIrjY1Axmwqt4_NypV0LHcZWu5BejNgM_gbLQxhPBk_1Rkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ علی رغم تلاش علی تاجرنیا برای گرفتن مجوز رسمی فعالیت فرهاد مجیدی در لیگ برتر؛ اسطوره باشگاه استقلال به مدیریت این تیم‌اعلام‌کرده علاقه ای به بازگشت به ایران ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22465" target="_blank">📅 13:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22464">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIq10VnZZ-lXiTZywjyQzcAShEYOb1JRADWVdaY6Sl5WFvL5tHE3nrOvKMiKDP2KQnxpUcnD_n_UAxS0l5Y5nudWHzu2V-fWL-1WuHLrY7FqFym0W_kgQfJXH1UHB0GNAdSqhxZky-ecTNjMhLDHFNc6CLG-FTGn1z47wY9YC10Q97S6JxT0NnFOcl3P_0_xngcJgRjl9-4JYPomKdCNNoktr-ar7obs-LrRwgrLy27xC6cRNf3ui60lmNud1WOfPV43WCr3fF2_nA4oMkmorWHbxBdyBxviQNcI2k-a10wqtyx8z1DQZPVpJ3fhrgesmm57f_tW2DCRxFTxK4yTkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ استن کرونکه مالک آرسنال در صورت قهرمانی این تیم تو چمپیونز لیگ قول داده به هر بازیکن آرسنال یه رولز-رویس فانتوم هدیه بده.
💰
این‌جایزه بین 530 تا 580 هزار دلار ارزش داره.
💵
ناصر خلافم قول داده درصورت قهرمانی پاریس به هر بازیکن این تیم یک میلیون پوند…</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22464" target="_blank">📅 13:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22463">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcgjBAraskTv6Vf1vmRDb7D-QHMns_8AXRNkQiZWVziSEBgAEcQDY7u7XWX-qclNwYmIWTHKVn6TQqtAY8toVleNeAYrMKWhStEFmfy9w8JUEC87fLyFt5yJaxVkYrZK7G-nqrTVuqBgjXOtIYEOeIKkDUuUPUt5pH3i8Tgh7Q0ci58W-pxy5adAAICmXeAIBWcipAf7kfFN5viCCroRtZbKcRBTwXuF2uRbyGQtJ1_pMywZxutss_deYcEaPcTJCwGdlFXeJwEL7rcgUsTjJjt3hbyooJMAedOivfpodNoKBzprI5yURMl_aDAgkaIMV-HDPZcZYwWmpUlcZGKisQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ علی علیپور مهاجم 30 ساله پرسپولیس بزودی با حضور در ساختمان این باشگاه قرار داد خود را به مدت دو فصل تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22463" target="_blank">📅 13:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22462">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vT-kWEjS3B6Ytc6X_-p3X8BCijBV4S4Hn9ZQnELkBPNI3ASShnilLdr5_uewyzv3oYd0kqC8-mOviCHf-DFjAjX6dYF6OWG0HFttJ8ZOiM4expi8I9Q_4lixbjzuRFbXDdExrrlghZKjQqaXTlMBs_PNdYdJ9oFfKK31PNafapEkyQspwqC-RyWsMooCmgBo-XXg5n1Y-ZjgC2xzL1NExCofm-a1o9qhhkfN8PGKVBT86Evenuy0vFr2jcOKAxLJ34HOn4WflxQZWBPM-VoqPipqUBSpElOvEF4Nj0SKe4xtAB9el84BQnM1HH3CubyzA0nmSBN4haR3XoG66EXxxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22462" target="_blank">📅 12:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22461">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9rpUt15IoWR-vct3sNOcDQVjetwYZMtNKB5XF7eqm6QZ1BcIH6ts-gjbLRgupiHIYFlvJSl307rIunGzw9EYLWwrx504E_QswTBlT-HPZwIkPW3DoIqVPlKi2ozNwq2t78NdDmFBFPTjQBvF4HRO9BYpgPMHHBA9vtJBiXnPup3aLXZ4nGMIR3_o999qmddObr6K3e0t9A_nmnTIKcomN6bqU1tVhPBRHziZDcI0VC_SipYRexvNccn_zZz84mggAaXxQ81EN1lN6XBEpVB6xHPQcmMs5A8zVNIohzwyCqQ6VY0Bh-s4p-32OElmaIGb1lU1RuEXonTpreWvVNCiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ رسانه‌‌های‌اماراتی: علی‌رغم علاقه شدید فرهادمجیدی‌به‌استقلال و هواداران این باشگاه اما اسطوره آبی‌ها به دلیل حکومت جمهوری اسلامی قید بازگشت‌به‌تیم‌رو زد. مجیدی زمانی به این تیم باز خواهدگشت که دیگراین‌حکومت وجود نداشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22461" target="_blank">📅 12:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22460">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEMnFXNerM5ttZGK5BEu2slQz9Ij_EGBssFCx9ctoqgsLtqll6XaFLQnJ64G1SeEmomLqrlX7b0llenF2ncebaYx4Fp1LeWLghz9Ze3TmUSrnkdOQ-NYbBiaozE0qF3LzaxRdvoz_wl4Yt1JWToPKb6uc8HuPD57VWmcaOi5zCYsjXMg25UOCl868aKK6ODT9ERyOuYzC7w9do3DYaT6XmVWksCzq7D8-Jc1T5_2SX-ncSzMEwuKoSO4h3a4SH6THcQ7_XumX9cjibLazV1gyKrhBD8b4CBMOpxT_SoreM0UYTOpgXgavoaYg2m1eOXaDckElDZRjgJu1uPgX_GILQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب کهکشانی و پرستاره بارسلونا هانسی فلیک در فصل‌اینده رقابت‌ها برای‌فتح UCL؛ به این ترکیب به احتمال فراوان برناردو سیلوا و کوکوریا مدافع چپ اسپانیایی باشگاه چلسی رو نیز اضافه کنید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22460" target="_blank">📅 12:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22459">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5359012d10.mp4?token=Ngql_8P_4djZWPY-QnVtvceyzS6GtpRKi0aH_8489yLq_fAwZHSbkm4EexjOswl-LJl-esMER7aO8NmWifpSyO2NBEd5k3WjL3kHdwlgxHzrIbotVIH5JvIPYj5FRV1YcHKWyUYE0xkucipUMx_lPvtY4Q0KaRdgUI5TTdFCj2B1FUXYO20-dKHCrvpTm85EyLTu3GnknGLFMrHMnm6kIXVRLV9EZ-0RgXoJ5AkTYbufJJpe5RjNss_IDTKnLBNHeDY6Qm9vQOEIRnY-5w08NaD0mhNr3CKDH2difPD03HMDpClpQFFzDC49Xm-DMxCzILTNzxZ1aXM2EZeyb7v-Vm8dD1uBL8GIGxBJzS1e_gevlSMhg09SqR0SE4wpRsMdY7BV6FcdkKBdGIwXBiDbnNpp42JVGg5L29E4u54LWjK0ZxyeKi9L6dTQ79Jd-LDLI0-o2qObOB4qph2W3u77mEgw3HiEDQ5EDoI8hdpxWOmZTur2KFodY0nPzMzL86MDn9wiRSPPwujOPEfqbg8MIdUf3zMU6XmowweVLPmowdJ-fqtYJnsq5LzZuOdTwvx5cWjjqwS5BS4PjKW4ABaQWngxy0jsPfKcjJ4JpthxFCQ0bctRps5xxCfoS0Mw_U5HHLKeJ7ay1z-b905K2Ch4TrHo84CJKuEzDGdVJQ0jhdc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5359012d10.mp4?token=Ngql_8P_4djZWPY-QnVtvceyzS6GtpRKi0aH_8489yLq_fAwZHSbkm4EexjOswl-LJl-esMER7aO8NmWifpSyO2NBEd5k3WjL3kHdwlgxHzrIbotVIH5JvIPYj5FRV1YcHKWyUYE0xkucipUMx_lPvtY4Q0KaRdgUI5TTdFCj2B1FUXYO20-dKHCrvpTm85EyLTu3GnknGLFMrHMnm6kIXVRLV9EZ-0RgXoJ5AkTYbufJJpe5RjNss_IDTKnLBNHeDY6Qm9vQOEIRnY-5w08NaD0mhNr3CKDH2difPD03HMDpClpQFFzDC49Xm-DMxCzILTNzxZ1aXM2EZeyb7v-Vm8dD1uBL8GIGxBJzS1e_gevlSMhg09SqR0SE4wpRsMdY7BV6FcdkKBdGIwXBiDbnNpp42JVGg5L29E4u54LWjK0ZxyeKi9L6dTQ79Jd-LDLI0-o2qObOB4qph2W3u77mEgw3HiEDQ5EDoI8hdpxWOmZTur2KFodY0nPzMzL86MDn9wiRSPPwujOPEfqbg8MIdUf3zMU6XmowweVLPmowdJ-fqtYJnsq5LzZuOdTwvx5cWjjqwS5BS4PjKW4ABaQWngxy0jsPfKcjJ4JpthxFCQ0bctRps5xxCfoS0Mw_U5HHLKeJ7ay1z-b905K2Ch4TrHo84CJKuEzDGdVJQ0jhdc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
پنج‌ موزیک رسمی‌جام‌جهانی دوره‌‌های اخیر؛ تنها دوازده روز تا شروع داغ رقابت های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/22459" target="_blank">📅 11:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22458">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCG55xN5ORhdQgShejoywRnFZ_HheX4-MPzl3lh-S-IQ6l_S9Cn4f6aguSX74SizPNkirnpiW63r9TOMR47bREI9bp4wqDj2r8B79TlDPbRYcnYUC-CGs1HGvyIyRngOVnxu9ZCv8kB0r_hIpcYWR66F1sWefDIGJNnhRM4YQ0zsnzsgRHFJw0lWP7zWQOjKZKtJB8ry1kVEzyDMnBFaoVEFJHf3kg8CaitMQ_XbIeZuNyQCjYrtfM2P45UFCpVGEBfxRpa13lXgm4uUrLii-34KBPTYtZJ0vAkWLKyCPUhErN9yHqvSbnE-smaD4NTCxPRg5HQg4g-luduROGF7OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
مدیر برنامه‌های نیکو پاز: ما با باشگاه رئال مادرید بر سر تمام بندها به توافق کامل رسیده‌ایم و نیکو درپایان فصل‌جاری به این تیم بازخواهد گشت. منچسترسیتی، چلسی، اینترمیلان به دنبال جذب او بودند اما نیکو علاقه داشت به رئال مادرید برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22458" target="_blank">📅 10:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22457">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMods73e9Plh32S8LoufxLNIO_eYyJOR5P86FjN9GBG-bjUOQVUeYKd_vmq36V3wFHMmF7onW4E8PHgHT2KPxGXC9BS3dqORQJe1K4OZsoUFIZYVC_vuWZykZ2zpZMAZZB_ZI1FVSWpLO-hl_rn44APVnBB05zBpOpdoXzu7bHHjrY0gxndOUj7UppzkaPaVl-NYSLI9vDUFn10PXVDtQlTnT2FVFCrcyW8QnBwP0wjrgSytnmdKdDSywX_Xt4jjMdJSd6348aeMVuaLoZRZxnN4os1iZ9KZhRPSvDAqPntuIqFk6bGBIYbvYR8zlRN8Esz56ieVRgko9xq2V8lStg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
به‌مناسبت فینال امشب و حساس، مروری بر فهرست پرافتخارترین سرمربیان تاریخ لیگ‌قهرمانان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22457" target="_blank">📅 10:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22456">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUHVCkMDjF33xeNlqxh9IXlRbT41FGbYjl-TGjjHc6eQ_KNPqa3L72wRhZ0AwrGred-nG41oo0T8qfHOH712xvQkj4u26jJGDMsB9XwMsMRiIzsPGg0T2d_-4ppJHsUljEg1sipwUDhriN-e9AOjhVBJ08c5k9YnB9advwoAMTkVpGSLaq3yqoIaSh8VWigIxPSrEQd7SOItJjOg6iPx6sq3MsixYMkUZBlTKukTl2LE1daCHJpNFhr0elwoVZFaEgQudvRYSAHfy0Kqbtycc30G5a_etUNJDJDn_tyXUCvh6E8jNdJle-diISQ74FqBwh5iFz--vHkOgHEyzrPZqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لوئیز انریکه‌سرمربی‌تیم PSG: میکل آرتتا گفته قطعا آرسنال قهرمان چمپیونزلیگ میشه؟ اینا همش حرفای هیجانیه امشب‌میبینیم کی قهرمان میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22456" target="_blank">📅 10:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22454">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d629612bbf.mp4?token=HoTwDfutDvfoH68pP32cfm_A-VQR1wKfMwW5sRXqRgTUU5Zqb5alviLzfLtxfmvAjtwcd9-mYUJuvpZOlJI-lAuwLmtIqHAvZD7ymiPNf0o6Rri8MuzeiJegOmHN0dwUfTexM_36tO59k8l4gvnKQXuoWd-13Lq5W1YxqFBsDTKea1WzUdJ3Ovh9Ngo8sSWW-r0jJCw-QoWpCtak-kcr8v4SD8D2yaIyBosqMWVPU1ijxHLlIYZ9bBYn7F0DNp4agpr9HieIwq5NYCTyigwtwEnljDGqM4CwJxiIllyE0fYrxu2uw_l0lfc3SAtz3ZSiJrJX4Xz9Wrcr2I1pyyNQPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d629612bbf.mp4?token=HoTwDfutDvfoH68pP32cfm_A-VQR1wKfMwW5sRXqRgTUU5Zqb5alviLzfLtxfmvAjtwcd9-mYUJuvpZOlJI-lAuwLmtIqHAvZD7ymiPNf0o6Rri8MuzeiJegOmHN0dwUfTexM_36tO59k8l4gvnKQXuoWd-13Lq5W1YxqFBsDTKea1WzUdJ3Ovh9Ngo8sSWW-r0jJCw-QoWpCtak-kcr8v4SD8D2yaIyBosqMWVPU1ijxHLlIYZ9bBYn7F0DNp4agpr9HieIwq5NYCTyigwtwEnljDGqM4CwJxiIllyE0fYrxu2uw_l0lfc3SAtz3ZSiJrJX4Xz9Wrcr2I1pyyNQPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
پدری به‌همراه فران تورس و دوست‌دخترش رفتن شهربازی، اونوقت پدری نشسته کنار فران؛ فقط قیافه پدری که متوجه‌شد شب‌قراره تو پارک بخوابه
😂
😂
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/22454" target="_blank">📅 09:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22453">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c867b80a08.mp4?token=R7zKmr3QKS4tMhzjhzMCkQK5BAb-9O0FiznKzlaS1v44F3dex97_TjbjiJIVPF4rZr9rNC_UnUksY16TFfaYGMaU5hXCrm-9L5yaAs4TraDJ_sjrVyTYzeBX2I8qk3vlMxedDYwsoDbawTXXrbI7WYisMvQafYNxWJ0KLvh8ipn0ld0PkfI33CkG1FMl5Ln5eikEOuoCFYdglGzDx8z-2gZCjUBvy1akTVxh6Bw5WHjLQbTDLv4tTXdOUpWwfG4FjcsQGLfm6u5cCSILLkRHtIGiTnGofd4Cne991Or07lCPZL2iP8b-Y0eaT1SmgBnG0WIdE3ikt7QytZHSqmKbeXHQWvz-ii-Y4OmC8j3QxhMIVvM5j6eTMXRXe8lcWMBGdgmRWbY2oGgsdxgqK_wwy0oUdNW-Mx6IrWn1mQrnhWFmE2qRy4XZ5RJpYn09UQegjJtFski4FtNTorQBZgQxWZdaQbc9uLgatR3fqoBNeT55OgcB9HP60duBWAOFLG4BaDnykTMCfbkq7Vg8Xf02eTlwuf2STV2en0zDI8S0biNRhq0t2nCeNgFDFmOfauyLcPyCFsnRsIp984sOU1QtEcq5Z8aEQjmEgpyKGdhbtWFBi_rapylTVr4or2U1uRdYY4aQ37-mBwLgqa2kUcx4zVP6NMfJhtKDg3Wa3cK9ZcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c867b80a08.mp4?token=R7zKmr3QKS4tMhzjhzMCkQK5BAb-9O0FiznKzlaS1v44F3dex97_TjbjiJIVPF4rZr9rNC_UnUksY16TFfaYGMaU5hXCrm-9L5yaAs4TraDJ_sjrVyTYzeBX2I8qk3vlMxedDYwsoDbawTXXrbI7WYisMvQafYNxWJ0KLvh8ipn0ld0PkfI33CkG1FMl5Ln5eikEOuoCFYdglGzDx8z-2gZCjUBvy1akTVxh6Bw5WHjLQbTDLv4tTXdOUpWwfG4FjcsQGLfm6u5cCSILLkRHtIGiTnGofd4Cne991Or07lCPZL2iP8b-Y0eaT1SmgBnG0WIdE3ikt7QytZHSqmKbeXHQWvz-ii-Y4OmC8j3QxhMIVvM5j6eTMXRXe8lcWMBGdgmRWbY2oGgsdxgqK_wwy0oUdNW-Mx6IrWn1mQrnhWFmE2qRy4XZ5RJpYn09UQegjJtFski4FtNTorQBZgQxWZdaQbc9uLgatR3fqoBNeT55OgcB9HP60duBWAOFLG4BaDnykTMCfbkq7Vg8Xf02eTlwuf2STV2en0zDI8S0biNRhq0t2nCeNgFDFmOfauyLcPyCFsnRsIp984sOU1QtEcq5Z8aEQjmEgpyKGdhbtWFBi_rapylTVr4or2U1uRdYY4aQ37-mBwLgqa2kUcx4zVP6NMfJhtKDg3Wa3cK9ZcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
موشک‌های‌گرانیت‌ژاکا بازیکن ۳۳ ساله سوئیسی سابق باشگاه‌های بایر لورکوزن و توپچی‌های لندن.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22453" target="_blank">📅 09:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22452">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/928b5d2877.mp4?token=EFv1V0hZFkHlvBwrJq3gJfoI5gSXr2_cio_7jW0ju1lWpRkWlP2DVW9OpRVkK5rxQDOSi1UraWiX8j25EeKxUrLQiCTLHpAj0RUkfq_08e7ph2B_odJZHst949LEBpuDoFc5D0DxxPWhArnJAPN6zBH5-Q7oiH1Q519i9yj7LOXK6B8DALnLfaKZ0UAF1k5kfIbadHQf5MpisCdB0BVJWoujeOtwrt2HfRK5yWBiFqnrtbRKoitWHRB9XsLobOgHtXmEThIXnSx1O_3H1ToprJjYXgmfAFGzHHdxMNqt8dRj3kwBFjhamMxx8eHFssZycHJP6u9baFn-rRK3wcgDYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/928b5d2877.mp4?token=EFv1V0hZFkHlvBwrJq3gJfoI5gSXr2_cio_7jW0ju1lWpRkWlP2DVW9OpRVkK5rxQDOSi1UraWiX8j25EeKxUrLQiCTLHpAj0RUkfq_08e7ph2B_odJZHst949LEBpuDoFc5D0DxxPWhArnJAPN6zBH5-Q7oiH1Q519i9yj7LOXK6B8DALnLfaKZ0UAF1k5kfIbadHQf5MpisCdB0BVJWoujeOtwrt2HfRK5yWBiFqnrtbRKoitWHRB9XsLobOgHtXmEThIXnSx1O_3H1ToprJjYXgmfAFGzHHdxMNqt8dRj3kwBFjhamMxx8eHFssZycHJP6u9baFn-rRK3wcgDYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لوئیز انریکه‌سرمربی‌تیم PSG
: میکل آرتتا گفته قطعا آرسنال قهرمان چمپیونزلیگ میشه؟ اینا همش حرفای هیجانیه امشب‌میبینیم کی قهرمان میشه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22452" target="_blank">📅 09:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22451">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb17964484.mp4?token=eKhJkJesjQRXc4G_vp8_z55wHxbEFnYoJdWXOSE0mNhpaMOgLlNRjZbk0kt1vNHhY9OwyMnKFUoB48CrlWvxHUiUEKr6ufUoqjmtw2i3yQL0jJZHTGXo5kwhvi1vU3ZlJ0seOdE4u0EpV6RDtjDcQj7NZjn1QeyWeSgpcA0i6XeCTGpdcfb0ys_xSWNsK1GqJdotrFHkzhztRPLfD5tg4X2ddgxDNxTssAOx_J_xagr2f7jyoLIwKiZWyIdZcNYHX7jj3StcNR_gjd3l4ly6n1cjCXEnApSnICCTlOlQcA21QAJQfgLr1HQJDejnhRw3DuSb50HB5Ohz7UsqAsLpcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb17964484.mp4?token=eKhJkJesjQRXc4G_vp8_z55wHxbEFnYoJdWXOSE0mNhpaMOgLlNRjZbk0kt1vNHhY9OwyMnKFUoB48CrlWvxHUiUEKr6ufUoqjmtw2i3yQL0jJZHTGXo5kwhvi1vU3ZlJ0seOdE4u0EpV6RDtjDcQj7NZjn1QeyWeSgpcA0i6XeCTGpdcfb0ys_xSWNsK1GqJdotrFHkzhztRPLfD5tg4X2ddgxDNxTssAOx_J_xagr2f7jyoLIwKiZWyIdZcNYHX7jj3StcNR_gjd3l4ly6n1cjCXEnApSnICCTlOlQcA21QAJQfgLr1HQJDejnhRw3DuSb50HB5Ohz7UsqAsLpcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
وضعیت خوان لاپورتا مدیرعامل باشگاه بارسلونا در روزهای اخیر بعد از پیدا کردن نفت زیر نیوکمپ
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22451" target="_blank">📅 09:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22450">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoJqHfwBoQWPOHmslOZdnsioWyFulQDt32vU_4A2KOX832rwjUpTBESZgH8tQeoeTwGl1A5qM8ltDcMptv7mHwyLM34Vk4_-etnJQx5x1Y5t3mBXxPczIg6wkYkp__jwqORyo60FupI8oAYHFA9UtaBm4PWngwpWBMaLOwAkhnDqiHV_x-4_d0dh2VDip675IvSuBJJhDiNV2x_xH7dsfxKIRjN7oatkBlUwal4ARR5gZAy7inBanl67_12Fih98ilv5QFH3cIH-6IfAEkw3o-qKsGa_1QrQiGpp3c1gaGPX3ZokJJhvJiP-OXOuyCz3aIT4MFjjio7zSFyEl89NDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22450" target="_blank">📅 01:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22448">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctRLP2cwWLsFbofWdkR1geYbaNYAn_wPiKDYSkRRg8e7Ea9vPy-fXgX4oTlPkgSo06sb8dp6x3z7efUQitxkul2rkMfgfeZkcLcfAFNFhKTbPqzdIOyrtZmD9Y2sOtcOtqjeq5OLWOeuomnAsMVJu2aYE97j_QIGfAR-y_MZWmSsA5nDfnRaUoykfYUPbc3ItTShlqTZZ85Uao1PiOl6-vja9oAd0q5_TIRsSJI_7X5fDonKC_m79A-u0EwbL5jbvxbfLwvqejdr703tX6DqWGiarf6-83rUxlPlTmmI_ZcuBCgUVedp0nL_Kb8q8XxgTjpXZ6T_d9x1VeioAjp7IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه تنها بازی مهم امروز؛
پایان فصل باشگاهی 2025/26 با فینال حساس لیگ قهرمانان اروپا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22448" target="_blank">📅 01:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22447">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqoDJtReHqpiKFTM7qW8o7suDA2yoh7-9CX0F9GHXeUVOoiVLo_cIqdeipK6GNfIG-4EZ5I8wSmlx3El0l0_ID288WPMrJ68Uzuc9S3EQFgba-EPngCrwrbcue7Wvtig7uPG2kqBSdjiVAVi82u0vM4xs9G-WLyqxl7u0HSz0HCwCwO1m1iKj4I0SdJubcG5S4jNU5ZsA8yr0MZa9-Smn53p9iSLaXfQeGBCofGOFPMbf-C1iBL87qf5AlouKrWVTz0Bc3e_s2rLMu6s1S6FQ2BnMklPmEZiseJawbXgwMiuxlYCSyU6GcJ2NKyInImQW7erVjWq3I_1BdiAbiiNww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل دیدارهای دیروز؛
برد تیم‌های آسیایی در فاصله کمتر از دو هفته مانده به جام جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22447" target="_blank">📅 01:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22446">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ah9K9VG9Ku-gTjNMUgwYffE_QSlTwR-kyVMU2FNVfOzxfqNXO-wFjZc_qjmPjR4vLR7F_nnTk9OIN7nHmzBAAzpj6tT-YeyCfqfFFl_OERPLLA-4g_-1B5D0cEEcZ5Lf2cRDVqA8TIa7RGR9GYEyobVQh1w-tgTITHD3MCbfA7ZR7eH8fdZPr9pa7jxxjHetm1Qkl3H-Uqx1rePUmvyuG0cAdQGOThqDRKkeYz-WTjNNRYrNl1YGPIlwCI5bBsW2kLbFslLYh_oMe5Vhs_C1jY_9ksFwMaSGd-TBD6zhr92hfYKEOp46wTjHMSU3VUTyivHdxrQ9ZUot64EgcFF3EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فواید پیاده روی رو ببینید؛
گشاد بازی رو کنار بزارید؛ فقط یه‌ساعت پیاده روی عادی میتونه بیشتر ازاون چیزیکه فکرش رو میکنی بدنت رو تغییر بده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22446" target="_blank">📅 01:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22445">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fam_kPUJYnE50y4RJdBARMlM1rNJktrUnKdIJtsSGDW7FLwPMFpaA0PSGF8u5q5lDAU2Q3KHI5onx7jrSGztpRO3XTzhXfg9FqebLHICGUDprprw7ftn6g7CmcPGNMEeIFnE_7hsHSfMwnXXQZnMDFqWnsCx3lgCVn6pzFf09oqMCcRK8bzUyYvaW3BKQHQYsLatEFWP96wQsquX7tfA19-H2-_Kr0HybWS1vIJYeZe8g66j_RDUE7p5XtPd_dSej--EBxBh7IS4LUjTYOYyd9VNCy9wvlJ358Fw60VynQTSzStApxl_MDeruUVpMbofza6U39HFurkL-ujtrQUszA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بازی‌فوق‌العاده‌حساس‌وتماشایی فرداشب آرسنال - پاری‌سن ژرمن رو در آپارات اسپرت ببینید. عادل خان هم بازی رو گزارش میکنه. از صداوسیما هم یکی دو دیقه جلو تره. کلا سعی کنید هیچی از این سازمان مزخرف نبینید. لینکشو فرداشب براتون میزارم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22445" target="_blank">📅 01:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22443">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_u_8M9QaZudINvie7v830SQ2EMNkzeh_Wm1weZNLEDe3mdYBZE2Lpw2pQUnR9vtab3pMpEQRnf05h9vKLBZR4lMYsdCrQJbyHwRq8U34UYW1iUCv80wSjuMjWoJ0qkFvpm_m1vnp_ZVUZ1nAW9TQDECOHvysiY8Xqu7bP5sY6aLUmyJ47dWOoiCvOXo5DFB_F_SML18PB7wcmc3W5PTzl5rrP4LHtz0STIDB-xPdLtSb5X1xIGlsgF7X5J7_FxoBgGinfQIuqLhSbhWGgtUsPcmtxo2FS3GaYZPoiPS-IHE2SgW9DM9ht3R-fJNbM42sYe52KgT3ufDZq28kexhrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو: آنتونیو رودیگر مدافع میانی رئال مادرید قرار داد خود را یک‌فصل دیگر با این تیم تمدید کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22443" target="_blank">📅 00:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22441">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SVyjBvqZES_qdP4fIy23UtFcBW5eSrNqnagm6MiJDLlaBM26j2DAdCB5EveSAkCxVGtCixLEwiACas2EYfJb78oyXQ112YLaYwWwj6kuelMf4bYuNZ3bZlhh1aBsfZPc9EY3sGYWsk4x2ft2GI-B1bvW2ZBnI9XyyRMFvKUq7n5TLiWDFNfJd7D3rS1Zh9ecYSkFvWFYVXUT9bQvSdwOWUSYVDhXpIMrWNDD46o4u879chXH5ouBavr18APEH7smTDwXlSTlzloujxAeMjWPgw8SLmoI4vj9N2WcqDkEEpKegaes21MGbmEA9EPFgmaBZevaSYxof6SKbcardSWoUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UfINc_fgbU_gEs9Om-KDNpy4n546kW3yjF40BxiiYOdG0Sw2vcjN5r6UmycvZZmm5wGO662Bgwi3-3Xsr65H6nX8NXoY3WCRayo9Aybhr8SrjvV4FWBZea2Xd_XKDVuK_uxVMWiE9C8QWr6rEJfFCL0oclZIK_TZqqZoRDXu9RblwVe_kBxiErwgk38KXZ1AtTmTyShoNivcJBYqKMaiSnAKt3DH0gNE5_5AjPJAB0UUb-Nvt3n5ygvJnhPq2FmOZ5XZyZFascwNaLQ5UXnME75ctbiWrPcuk87aApfkHtnyGHWmDNV12RO5oZqAgcyrIEc_vjDAqq2DFdU62DXG7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▶️
هایلایتی‌از عملکرداستثنایی آنتونی گوردون فوق ستاره جدید بارسلونا در فصل گذشته رقابت ها.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22441" target="_blank">📅 00:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22440">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VE7eWwRWjkJrTT1k7JzSSiROPxPj0cGFU9TXFeZ0ZVy7bWuqS7smtSR4bPclCa89OednXoiWq4oV8gh7CFV75d4vQN_OVP9K6vtPaR145LLTlwwC1KVaJyaamvXmVcPyOphnkp5gEkt-VsXMRQZE0Mgdq914eqn6anxeGib1IBS55Pps9ZpwAEhQ5sjmjOLczbjhqnJLeOOamAxOoARqS72H9n0SfYUwcMT_yUdSs-kKXOym0WQ4Rk8m_vkCHaB12NFj8Cit9FUq0zGiMgt8n7RQ8YEtqg-AqTvHORN809PMwRNK9G-fLz8xaT8VnmVtxJdhs7ZyaLwZNbbpt2FvcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ریکاردو ساپینتو سرمربی‌سابق‌استقلال‌که در روز های اخیر با عقد قراردادی به پافوس قبرس پیوست با این باشگاه قهرمان‌جام‌حدفی شد. از معروف ترین بازیکنان این تیم میتوان به داوید لوئیز مدافع سابق چلسی و آرسنال با اون موهای خوشکلش یاد کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22440" target="_blank">📅 00:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22439">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o91SS-cF-RllwaRDez6oE24jPXALX9yYr9QB5o-PJwSiCM-OPF5JHzD0lM2fopamTiMCZQgWujPrSCiMFLoOEADSULIb3TJcIciEtSf9WzkiO04rlzcceHLWWl7KJSl5CvgVZYH81M9WKXzV_XdPsweERQsPd7Tu5pqkrfSSx6BYNjDElqVjDbtp5fhe-zL9WIr_Cmn-1LwLkk1NjEFTIXrj2HgcGybs4lQX-Ped5iLE6MxZ7gAeZKg5q5VtCf6LyJaFE5cdNNbStwd0-NM0BuhmDXU4JwfL1iDk6bpcDiYUDOgppLZDKM5ht90SAvHBZzXWw7jksB5kRlRjcgTguQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کدبیس سه‌شبکه‌جذاب ماهواره‌ یاهست که بعد بالااومدن نیاز به‌واردکردن‌کدبیس دارند. اولش دکمه F1 میزنید بعدپشت‌بندش‌سه تا 3 بعدش یه صفحه میاد که باید کدبیس رو وارد کنی:  کدبیس شبکه جام جهانی HD:  BISS:2585AB552585CD77  کدبیس شبکه ورزش تاجیک HD: BISS:03A01BBE20C16D4E…</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22439" target="_blank">📅 21:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22438">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsdcIho_QbcSVVQuWBI0cwPQmY_ZvfalfLv4hk0i26bZwOmbzzbNUastRC0sexzw_FOhuSzKL64Kgf1Fh4KpTpQuClySTBNAyYS_LKhpAWLWE8r6ZMzo7-n57axrv0CmfKFORXGlOq8xwugk0EXsisCZ6hkkXAJYK9IW5JJR1qJg5aS7Y5L0xFcf--7S0US7JZPVQE-eRum8JeNlDt5C2mF3AlWex0z1C5Bdhtzs3rBLXIVFFF-oxA22_grU1Tp2MURjd41qQb4q7eGlopiLKLNRUAzHLoE5pUbz_6Jz_5yGA6PjV7dtuw7QiApJG-hE1PuZJSeq1w3bE5M-dsRZFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛ ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22438" target="_blank">📅 21:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22437">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✅
تیم‌امیرقلعه‌نویی مقابل تیم دوم و ناقص گامبیا که در رتبه 116 ام جهان قرار داره سه - یک بازی رو برد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22437" target="_blank">📅 20:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22436">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwOdjlcXSxR54aHp8ny0QfLmIGkk4-x9OrrPss7sPxKCL0Fkr_hGkuFe3nh5bwe5kWYzQ7E3tDqtQtwNUYh380BeEAeW8YGCIhUhvhCWZPh6znXG3axq68c5jAhFaCrxn40bMCDVzC2ktA56dB2Ng-_SLTewLql606lgJs1L4f-kEKsn5eqNcpo5hiWltqV4itDTzh812vqtA3EIkY1Ze-Ra9yOLStAJgZIRqWf1BC74J091mxk_jymUNsPjj5W7jMAFOH_O51eKU19J7p0Xps5NsDMBiNxTNGWfYvh8wMB3T0K4LJtEPcrs2aOl1yk848QXxKu2lKiL5O-8ZadOIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|سران باشگاه منچستریونایتد به درخواست مایکل کریک سرمربی جوان خود با ارائه پیشنهادی 100 میلیون یورویی بدنبال جذب فرمین لوپز ستاره اسپانیایی باشگاه بارسلوناست.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22436" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22435">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🏆
کار گرافیکی تماشایی از قهرمانان جام‌ جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22435" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22432">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrrA0vkdEnARuuIUBOLcQY8U2jN4EdFxme31lCQ32C5LACLhyTB8yQqKgKODqGB-ssUTCgIRIEw7qXTEA1ny9ZzZAtPWkrzC1E6ldGqQdOnW9H5QhqNrvlWPwsne_JCixLi2ui6P_MTkEnkh0hRhMZNQ85bTkeq1QW9UkXVWwZOm-aBPV_yHx40xSJc61Z3j1tXFvX5eWiAaAWg4c8AalAT0f35W3YzXplpeGy86n6-Vm0rIiXJpY2uCBP5DKtaDRCke9eFxxNjwj8iX1GZw6IcLvJgzNGzm782oDv1S6RHZF5UY2CitnKEcI_n1HqVUeygA8IXOO0S87r_QxVYrVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
بیانیه عجیب اتلتیکو علیه بارسا: «هیر وی گو! ما یک فکس به همراه پیشنهاد خود به بارسلونا ارسال کرده‌ایم: ۴ بلیط برای کنسرت فردای گروه «بد بانی»، اشتراک سالانه ABC و یک کیسه تخمه آفتابگردان. مشتاقانه منتظر پاسخ هستیم تا «اعلامیه رسمی» را آماده کنیم.
⚪️
…</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22432" target="_blank">📅 19:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22431">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVqu1aOWdAbhTEL_hQjzVwoJNib_ipSKpt5E_LkK_FExV9OEW_RvIgWJK_cH-nDhZIQCOmx-wQ8tFSPkpuAj-ldFoqb5VA9T3_KrkXQ-vIJiAWyNF4M3OpxAZcpluTkG5s4Dl517DCbHpfWtdTI3awR-85N0wOzW_0Y9mTG8RT1GRHVqAtr7BYTlloy0vaOPHQq6jH7zlVlzIs9Ly3NSYqxmdASJRtYNA4tXZcmjUQ5QU-mPJh_bMQZWJOOoU11TRByvFzKeey2Ozpdlmtro3pR6GzAeCu1Ij0uJFQfUxCpqRkWFsjgNpgps6uNMRicW_wtHgzosFFFCQssR6dJ82A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
بیانیه عجیب اتلتیکو علیه بارسا:
«هیر وی گو! ما یک فکس به همراه پیشنهاد خود به بارسلونا ارسال کرده‌ایم: ۴ بلیط برای کنسرت فردای گروه «بد بانی»، اشتراک سالانه ABC و یک کیسه تخمه آفتابگردان. مشتاقانه منتظر پاسخ هستیم تا «اعلامیه رسمی» را آماده کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22431" target="_blank">📅 19:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22430">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFs4dcomyRogRvGuXp4UZSJ5PRhdObsIZJAEABYBlzX2PJC8ftQeYGdRQ_FfPQlcYSu7oz2OXuSkzr1xb9afooz6sTPS9-oecmh2zxu4tNYckvJMu9WaMFkhIm_wpSGq8PCr-c541u0H9JVJ1-Az-c-rJTvL5c2r8PqSF8ZFmEhlbwAJfxl0jIKc37LI3J6p8VSe6OK40DibCEOJX1IKCE_01VdBWqnziif8HAUz8qF3qNSVwA8lq-5xmZRRAT52pUywZrcucOxehighVjlpFhRTDAI11DNh24zypjucyC4ZKnRowlNMVnLtgXPUABEaIXGSXPGdYeK5v4uAEj10FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخرین‌اخبار منتشر شده؛ باشگاه بارسا طی ساعات آینده پیشنهاد برگ ریزون 135 میلیون یورو برای جذب خولیان آلوارز به اتلتیکو ارائه خواهد کرد و این بار این باشگاه با این آفر موافقت خواهد کرد و این انتقال رسما انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22430" target="_blank">📅 19:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22429">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9v3kp8d0ovMtqYksLNEL95iwOrd7xamTUvE6TYTNcU3eEFEqHAypZYOiR7Qynd0rm6HR9GzMzTfoOOu1BA1V0GRsXZEiKs78dOU1xoum3c1TgciseooDUIksz5gjdCBS0S-GTy3gsIYAIDTFcs1y4MRv6a8FTv0krVHKwvlr3r4n7lbb0SNHMmTQ3pPcnaYgIPOcHGJXHruXQFJMB9iQaiH6BbAs__Vur6pZaWid2CVL98lGuxaDSFepoIy-pnBBVT1AY_jr7LM4ivTg2-yd4xW4z2uDqQqkhsbSLuRaFBKR8db5YsR6gCXH5gk_QKrKvc3KvLUk4xYG5_Qp8a2Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام ایجنت رامین رضاییان؛ ستاره ملی پوش استقلال که نیم‌فصل دوم به فولاد پیوسته بود برای فصل اینده به جمع آبی‌ها باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22429" target="_blank">📅 17:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22428">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e99804290.mp4?token=PAsokE1cvFApecszk6-r359kArCAZc5VpsHkieULHMhBrQjIIm5v8VTpjZ-GcWO6usPWgCMpiZI2d70kxcygeJE-QA8mqKkVSV_Cp1VaXtcMi-8QSb_AkFH152uNX0b_rYhPQ7ygOHtR_yBkDA4NLTAEePIKO7AtgZ3fP2NJ3tJIaEC9yn58RxR0pgpkcjf7MLnPdKZQcQ4i7snK8RDttB8nVOeGWPtolCyg2XGVteNd7g7MtUQI59Lw4ay_57bxp8CIQFOSDMW4uR9y6clN8d46_d5uw3ixbhvhk5bam1YC28PdXZRL3cIG7mJKUbp4oawjDu3UlTcDK7erATlGHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e99804290.mp4?token=PAsokE1cvFApecszk6-r359kArCAZc5VpsHkieULHMhBrQjIIm5v8VTpjZ-GcWO6usPWgCMpiZI2d70kxcygeJE-QA8mqKkVSV_Cp1VaXtcMi-8QSb_AkFH152uNX0b_rYhPQ7ygOHtR_yBkDA4NLTAEePIKO7AtgZ3fP2NJ3tJIaEC9yn58RxR0pgpkcjf7MLnPdKZQcQ4i7snK8RDttB8nVOeGWPtolCyg2XGVteNd7g7MtUQI59Lw4ay_57bxp8CIQFOSDMW4uR9y6clN8d46_d5uw3ixbhvhk5bam1YC28PdXZRL3cIG7mJKUbp4oawjDu3UlTcDK7erATlGHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گل‌تماشایی هریسون رید بازیکن‌فولام به لیورپول به‌ عنوان بهترین گل فصل لیگ جزیره انتخاب شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22428" target="_blank">📅 16:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22427">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fs9ar-SkKcTuvdDJOCuBTKS0-GfX13pLMIQ1SbUctN7AsqB5E5k1QKbxc7uTyE_N2HqaQRwUZ57Q_ZU6feShKYnQ7dSXoEreA0P-6ShzD8W4X1SAlRDV-PYqHzbSfYZ2_LcupN-rI0xp5rOoVOaGsP5KPkmbKQ0RMuH6ADRGO4DTiw9LFwZ8tmlXqnhCrzJBDGqJCALphpzC8SeCjlQhTpa1RS1EfWIhgSVqYlugL7pogstNop0ux2M4LEdKyUNMMJwT1VFSrr63MdF702nb89ASdFqAoKijFJ5e5WNAN7jjsse_aDSvVcjnfUcPk2m97W5f1kobUwbvn5Uch6i6ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22427" target="_blank">📅 16:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22426">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwSa46su4X4rE6RXwf_Y4ZE4PtNlbfn42r3_9vchlLEBLDCswutYc5FoF3n5dwsldcmcYz-yx7zoKxa-xLHG6OQtfq7TNEqfnkymURsolf5efAP7NAt3-GvXNbTYi0v4vQIHBfSYz8kuGAx9Ycgb4xEXzBGLph7kQ_v-Qy4ya4eIITe2w76j6XWJbMw6Jo3wLx9rytj-cQ-9NTEakavsp1TUxITGR5iyTlKKj73qLX2sVWAqt5AyrPVjcBRQjBLbQPqzv5b6NkhtFTiCtF_Yq8rKtEiMINCE7xZYLvMpcdk706Z5ZDK3qDzYK_bSoJaXJYJtPEz8M5U6S0jtx98Wsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسانه پرتغالی آبولا هم مدعی شده که باشگاه بارسا در حال نهایی کردن عقد قرارداد دو ساله با برنارد سیلوا با دستمزد سالانه 8 میلیون یوروعه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22426" target="_blank">📅 16:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22425">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ccdf1c58d.mp4?token=Ko8wW2d0yLVQHvcUiO0C214VWqCSR8pEzhMZKP-h_CSJbu0XZiJh-W3Y1t1CnKm4FWmbszS27hJgyP6wT8zCMZyjCZ78aIfa503fIBg6wWMMsQkInSaNeugMx9lLpXcGkofC_mI7yJylXCvnwP3zd4yzF6mcwHeiAuCi1I_Arq2JQaZlIj0kHBs3tqeAADaI60B2TyJtzZ2koA_LCMg5X4DISMUAcj5BLa8hla6KgsQvwtEa7nIxQ_7YUcVUlm7f6hJB3wdsY0ifA_oJzVDnOZKR17LLuuCWSCRS3nfHLyFju-T8Ne1hfG1iFuv-g7FIgtQzlaANOA8mw32QChQ1w4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ccdf1c58d.mp4?token=Ko8wW2d0yLVQHvcUiO0C214VWqCSR8pEzhMZKP-h_CSJbu0XZiJh-W3Y1t1CnKm4FWmbszS27hJgyP6wT8zCMZyjCZ78aIfa503fIBg6wWMMsQkInSaNeugMx9lLpXcGkofC_mI7yJylXCvnwP3zd4yzF6mcwHeiAuCi1I_Arq2JQaZlIj0kHBs3tqeAADaI60B2TyJtzZ2koA_LCMg5X4DISMUAcj5BLa8hla6KgsQvwtEa7nIxQ_7YUcVUlm7f6hJB3wdsY0ifA_oJzVDnOZKR17LLuuCWSCRS3nfHLyFju-T8Ne1hfG1iFuv-g7FIgtQzlaANOA8mw32QChQ1w4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌که‌باشگاه ماخاچ قلعه روسیه از عملکرد درخشان محمد جواد حسین نژاد ستاره ایرانی خود منتشر کرد. حسین نژاد تنها یک فصل از قراردادش با این باشگاه روسی باقی مانده. درصورت باز شدن پنجره آبی‌ها مدیران این باشگاه تهرانی برای جذب قطعی این‌فوق ستاره 23 ساله اقدام خواهندکرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22425" target="_blank">📅 15:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22424">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjoe0rF5qhxfirdrd3209pA5T6ICOxnQDKY1gnafXBaKpfUHHbNeWVmjLHpJSZP_yzSzr1ACgfvFG-N_OmvdRMpeXaewgEUsX3iRAaywSk5hUqeN3OL8gu-Fn8KKMvjPbsIFsuMopYI2voUEkwviR4exK8RKEHuphIvLvDKhVrNv_z7wzj0MBMBH2czUzd5soM0bxaESk06UYNVslxqvyi3IwuWe7MhkF5D1yymY3Hy0-f1EE1WBQzhA6LIsraVMZeZ1HIEvEdl2xO-u2NNLl9JYLUcNMQg9eRiSW3UznZEeedUjOdpd2l3JDBMZl0GRGihQdDf1X3i6LNGAgFu1PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات؛ رسانه مارکا: رودری ستاره اسپانیایی منچسترسیتی میخواد از جمع سیتیزن ها جدا شه و باقراردادی 4 ساله راهی رئال مادرید شه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22424" target="_blank">📅 14:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22423">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LomIiJl50PVkVWJYiaLR2T-D8KPWPC8JHfpFeHVqY_qTxgtGNopRTiu3xH1xmk4ojV6U6UdxlENov1mebUZ1tZT__3AcUk9-aiQRJaTX-alju7QhK87FNrc77zgRIwlHcHshMgK3wMkFdOZ6WSPVUKia4wzMFf6N-xjyTz4-a68omjS6m0s_UvCJvJoIsbKJ6t6dlSLnzLqxIkDHxhKcMnVq6YFqGjVWLqLB_W5tgW-S4ZeLCyX9TIngddaW1wpzvHlMAGa0uO22DM50aqChvfEH6B2aVunhnBff2y84Z9f6CLEa6jwA32-9uX-2LTpMgho_-bS3eDMuKWgT2FppyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جرارد رومرو: یوشکو گواردیول مدافع سیتی نیز همچون خولیان آلوارز در خواست جدایی از منچستر سیتی کرده. فلیک عملا با تماس هاش داره راه انتقال ستاره‌های مدنظر خود به نیوکمپ رو هموار میکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22423" target="_blank">📅 14:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22422">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XeiJVCaArUWKdLetVYhbTrI2442clknW-Gl5pU1q9v6bo5NwYTCuIgZiwmAcQ9zqAkX30fw9PLZuPaDeX9f6zcWa_RUHba53esjhM46ecr1rnpKfq05bdQYSycij2kn3S2DbPlq82WccSv7qaiKZ8lPm0zCnRgTnGXGO2eQv_uSHrk3E7UiTaTUO3SCJ5uxt8mihd-yBKXTcV92qEimNleVgpRLM_ACk2gBzTXdSQYY2oR18nEGyyME-G_lLqqr1S3oHmJWi4ZiOauIzTxRidhEsRy5-ZnLjlhNVNqaL90oZIoJUZKJNPDQFvIzPcbaCFdeO6KmnlcgCyPEb-GHyNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌انتقالات|ادعای‌رسانه‌های‌انگلیسی: یوشکو گواردیول مدافع 24 ساله منچستر سیتی هدف بعدی سران بارسا بعدِ نهایی کردن قرارداد خولیات آلوارزه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22422" target="_blank">📅 13:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22421">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNbHW865iiDSr8W5hOjZ3QaMDUJm10gB395xg8SYipoLylOw8_KaT2QsnLMvHg1ueHjyeVXD5oy55-gkGicp9XCtNqkpOizmnBGNyUv0Say-UHqRjwpe3DgTZtpz-tJE6Gc20hbcZkAGLspGHEOoKc0yVTEaPbk-w-D0MZv4n5H1O8HF4NcUTlvD1GCKXrDJmso97cknk8DqaVPM8FbbI0fAnXCMvIkd3qgzLA9eNY2VaK1vMqD7ZGeahEtwyHtadgayZoyee2_4OJwffh3dAg1XduWMscKWO5coVn0fqrEHzUep-rmDA_YFvWQMlvMvtMTayorg7mrdzEewpUmF3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات؛ رسانه مارکا: رودری ستاره اسپانیایی منچسترسیتی میخواد از جمع سیتیزن ها جدا شه و باقراردادی 4 ساله راهی رئال مادرید شه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22421" target="_blank">📅 13:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22420">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqMXZILaLA4vtSJ7ItwnKja27j0yIolua-uhykFrcQDQkGUM8dXiTitjX6CQg9Vo24m4ko2dYeeEkRMD1srEPhtPYQPQxuNkQRe3Qdi9YZm2CVBxIZ4DLvoUVNec_VK-h0FNmgXlcs5Mt5qKjrIdHglc7HaG7rkpau9S44IbA5fUrJ-TzEw-aMm_0c_ikJ_SCVjaVSBYfxAEC4wI6oALYIvSqqiQiK1qSXNpD9J20reCiNOIE2h-AgXkdCtZFTeHhoXZd1IgIzktc3ThK_-PVCX1N9_KNuKrZK-v3HKBRoQKfzapGL46y-QbzcgFBWAFYSCj1kVe_9L8EirD9ZBjLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... یاسر آسانی ستاره آلبانیایی استقلال امروز در تماس با علی تاجرنیا اعلام کرده که فصل آینده رقابت ها نیز در تیم استقلال خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22420" target="_blank">📅 12:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22419">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQNbqdi5Jm5Zg4ms-cU6vJTo6cNShYI60lIyQgFyWTbNfT3gzy-vrmmatgooMeIqDZmEgmpH8ZAg4avLYLifHnAIuw0xCj1w6csvhyPUfqq64MRowIsm5l0ebtRvGRelAMHN_7t2lMFwlhxFFD-kCA8hJojHxqq8lZa39quBIErXFTxAkLSyU206l9Go0oXGSIbgFda3Erez_qJUTZhA7TXFwpKcArrCIUCzyPEmwFDg3UcntWPdjsnd016IAx9fcLaU1KvxvdugkW75Q7TSXB2H0y2DnDPSTpK6LFiOzGyEt3W48aCxGUGDaK7y1ZLOTHkx3bU4pcFr5ZspDHh6bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22419" target="_blank">📅 12:26 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

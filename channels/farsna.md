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
<img src="https://cdn4.telesco.pe/file/s8k8TQdC7E1PGSvXDGszNjLKZulW6a2xpR0ZuMASembELxw1Wj6VXDNQXEguzdXDgGIQwZ1oG_AS-dkCnLsE4LSdP-Wvo3nz6s-LpYYlv2aIi7lljvK9S9vwsBFPe8ezsNxZlWNAHQTRa9DLhG-usJ6ukAtOxcIL5B0pTsvceC2VTgENuTFJUZ7ZaHhkZCJOAXw30UljmZ4A_iILcxLclvRa0_9-niUam54TF_an2Vpoj53UitWcR7CVU2HObrIQuAcpw3A2qmNDwmb-ApAp6S1xI5r4wNTHZZJ_DoGuezBwPDB5qarONtCb7P5PD_8JEUQcqJan6lkL_qpG1TOjIg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 20:42:00</div>
<hr>

<div class="tg-post" id="msg-466305">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/liQZxDVeVMEk0UPC8VoR_hIdWg2N-RXviTx9ISMdOVTlC3Sig6e1P495dZNFuHJ1sIlckXc0SsSwB83gZhIASFQI_7WnP4_1vmAR76cw05ecfA9T5ysa4cqptZLQfviKqSIACtvF86lynkNxXfx4HnOYMs27SwfsjYBiWJZDZ3Cbvj6yscBbkT3N9eYyFn2nW8G6O69Fy8OVE0FJKIHegdRyQOJCXtOuUHgDHGbQqrJ_ktHeJiQ83bHe1VnlGAnK9h5qMH2F5h617g3lnNgUbGbwo9PNU-WW4TctXndXkp1b-F42m6r1_gnkDIdVV65McfIzrAcPjGg7Vypw4cuePA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر نفت استعفا کرد
🔹
معاون اطلاع‌رسانی دفتر رئیس‌جمهور: با پذیرش استعفای محسن پاک‌نژاد، طی حکمی از سوی رئیس‌جمهور، حمید بورد به‌عنوان سرپرست وزارت نفت منصوب شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/farsna/466305" target="_blank">📅 20:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466304">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/farsna/466304" target="_blank">📅 20:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466303">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f2372ddac.mp4?token=suGd1cDAKLaCmTrvKo20flPnfiBt8JBNROx0GwBf-OcTo8HvBHQvanlKGxb9W2rft_J9OOcicuZuz2XDpwDQPo3HQU6SEZA9LDaxdL0cDl_QHIRpAzbjBmfsFhJauXD5VVbaCY66OtBx5WujqtNtpGEUEvojW-L1nw6KxLNuZel9DimgK84fCLOF9Q3wp16xZj7wGxENjHc0C5OiClYOBoX-OFhSGxXYopGcAAS29huRZSQZ-h-MTTkiKDqGb-MZpxjV968SVBmZm9YKYG6LJDeYox-ukVlEZtouEYZE7-OavF38F3RUvDxDtSTwf4QPX7DG5FmXO-DhgnmCQAmR0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f2372ddac.mp4?token=suGd1cDAKLaCmTrvKo20flPnfiBt8JBNROx0GwBf-OcTo8HvBHQvanlKGxb9W2rft_J9OOcicuZuz2XDpwDQPo3HQU6SEZA9LDaxdL0cDl_QHIRpAzbjBmfsFhJauXD5VVbaCY66OtBx5WujqtNtpGEUEvojW-L1nw6KxLNuZel9DimgK84fCLOF9Q3wp16xZj7wGxENjHc0C5OiClYOBoX-OFhSGxXYopGcAAS29huRZSQZ-h-MTTkiKDqGb-MZpxjV968SVBmZm9YKYG6LJDeYox-ukVlEZtouEYZE7-OavF38F3RUvDxDtSTwf4QPX7DG5FmXO-DhgnmCQAmR0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی: طرح تثبیت قیمت ۱۲ کالا در سراسر کشور اجرا می‌شود
🔹
طرح «تثبیت ۶ ماهۀ قیمت ۱۲ قلم کالای اساسی در تهران»  مورد توجه دولت قرار گرفته و قرار است این طرح در سراسر کشور اجرا شود.
🔹
قرار شده کمیته‌ای ۶-۷ نفره تشکیل شود تا تجربیات و زیرساخت‌های ایجادشده را…</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/farsna/466303" target="_blank">📅 20:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466302">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIxYe0AiOs7LF5YCNFNxbOZi9jCdMQs8X7d7PShkyJXhC0K4-KKGgvvf8QDkv6ClzjRjlfF3mBwgZa_Xj7o3tR6fvg63S1ze3i7GyMBXr1fZjX4hIDrX32S4hmu6w74N2DmJ67dD2nMbBcYQHFHGlMuT_Cy19rIyF9uKLqhcQohNCGTiXRifRCjI0OivA-XKPmZBh24eiqX5BJq653sFzomlnOojWK6PvA_ON_LeMBH9M3o0up5Qu3mhFhu-JB_pTaL43M8z6g6-DL-dUK_M3cAy1ClJxhO512WyZZ7H2Vo4BSF4ONe6WGmf9CS6qQ9TXo9khtjI9B4DIvE0hAAcpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی: طرح تثبیت قیمت ۱۲ کالا در سراسر کشور اجرا می‌شود
🔹
طرح «تثبیت ۶ ماهۀ قیمت ۱۲ قلم کالای اساسی در تهران»  مورد توجه دولت قرار گرفته و قرار است این طرح در سراسر کشور اجرا شود.
🔹
قرار شده کمیته‌ای ۶-۷ نفره تشکیل شود تا تجربیات و زیرساخت‌های ایجادشده را بررسی و به کل کشور منتقل کند تا با همکاری دولت و شهرداری‌ها، این مدل در سایر شهرها نیز قابل اجرا باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/farsna/466302" target="_blank">📅 20:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466301">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwIcNLUW3aBL1DQbj56pOXN63_VW-e20MREbKp12OZvVkdzyfmFTsSDUj2kvZKpdPVHn9gZ1odMHrR2CcrhOA101vU7j0fc5h0FvzCFjErbJA7LaZjK8HuXUx5TlidvAHEv6RqrixFx-yku0T0KnK10d1Bv9SKPzXXWbmhXDlgCuNnK-sLWtSL6DLBckEsYHMeXYV2cBqqfZl985djtUJQE5TkefWKmudKhoi6wKlkc7fnq9lKCKC1GDYSjNrmEc4DPhwZW6tndTWlFzHAUoJH4AD2uQS4LGZ9W3OnHicc2qu3KdwmZPQIuVVORZvXpxPNyIea6WcoNSud1qIk9G7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
محل‌های استفاده از طرح «تورم صفر» شهرداری تهران را بشناسید  @Farsna</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/466301" target="_blank">📅 19:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466296">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">دفترچۀ زبان.pdf</div>
  <div class="tg-doc-extra">17.7 MB</div>
</div>
<a href="https://t.me/farsna/466296" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">‌
‌
🖼
دفترچۀ انتخاب رشتۀ کنکور ۱۴۰۵ منتشر شد
@Farsna</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/farsna/466296" target="_blank">📅 19:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466295">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70fcd4c336.mp4?token=UWepxLzA_coLq5LGXCZhC-SnoKNdmqKo4LtHYp7RzD7A52Qt6Jf0x_luW0vE4S8Vq8p6V1zgQ5Pl4ewlRiL3rJ1krymy_rDsYe1ICr400JPPyCkWm4lZ_KfGK8bODLA0zV8A28vQ0SdXh6GnUDXaFhEoFUaKRUArB14j2FlQPesVjFl18bvgNAYE_dO9eRbfhmhsU3U_W5PGdFr7QttM0Jm1UlFWJiBGi1kk56iaoSsVJ1XktnJXtiQ-zOkAglGJ0Dr7Kp9lM5FbKz2JUce2BguRkKECVQqcycZpkXtxM9qpciO_643OsDwqJJQGhWcjnji83_szRMapBUgKJ5yJPIOYJdhjQ-ODgyLZkJw2_VqGb5vUkquacqcE89GWQir0oeM-XbZ76dXeHCbNnUUl0SD3mBwCtCwt5Ruh7aC5TgmGWTMORdt8-TPxUqbZA2kBxEWdR3AmkvIaq1mGL6SS4CtFh83pgvYbzXdOzJEcFrZUyFRU3lTbgwQDwWAjCouk9th_0-hc8YBDlgmHDlIdmb0hIA1zGozQVUAQKxTQy6eu0N9bJHrs9c7qmeRH_MjJHJZw3xYqOaEBco6BLTRBQAFLLVRywZM8D1MXQ00RZHYuc-zGPd8G4c7uy_MI9xsDVB7crn9iGiUh-DoldRX8MXTAhfJXOmhsIs2xM52tcYs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70fcd4c336.mp4?token=UWepxLzA_coLq5LGXCZhC-SnoKNdmqKo4LtHYp7RzD7A52Qt6Jf0x_luW0vE4S8Vq8p6V1zgQ5Pl4ewlRiL3rJ1krymy_rDsYe1ICr400JPPyCkWm4lZ_KfGK8bODLA0zV8A28vQ0SdXh6GnUDXaFhEoFUaKRUArB14j2FlQPesVjFl18bvgNAYE_dO9eRbfhmhsU3U_W5PGdFr7QttM0Jm1UlFWJiBGi1kk56iaoSsVJ1XktnJXtiQ-zOkAglGJ0Dr7Kp9lM5FbKz2JUce2BguRkKECVQqcycZpkXtxM9qpciO_643OsDwqJJQGhWcjnji83_szRMapBUgKJ5yJPIOYJdhjQ-ODgyLZkJw2_VqGb5vUkquacqcE89GWQir0oeM-XbZ76dXeHCbNnUUl0SD3mBwCtCwt5Ruh7aC5TgmGWTMORdt8-TPxUqbZA2kBxEWdR3AmkvIaq1mGL6SS4CtFh83pgvYbzXdOzJEcFrZUyFRU3lTbgwQDwWAjCouk9th_0-hc8YBDlgmHDlIdmb0hIA1zGozQVUAQKxTQy6eu0N9bJHrs9c7qmeRH_MjJHJZw3xYqOaEBco6BLTRBQAFLLVRywZM8D1MXQ00RZHYuc-zGPd8G4c7uy_MI9xsDVB7crn9iGiUh-DoldRX8MXTAhfJXOmhsIs2xM52tcYs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رهبر انقلاب شبیه‌ترین فرد به امام شهید است
صادق محصولی:
بنده توفیق داشتم چندین جلسه خدمت رهبر انقلاب قبل از دفاع مقدس سوم، باشم؛ جلسات دونفره و در موضوعاتی که مورد بحث بود، خدمتشان باشم و از نظراتشان استفاده کنم. به‌طور کلی، برداشت من این است که اگر بخواهیم در یک جمله بگوییم، شاید ایشان شبیه‌ترین فرد به امام شهید، باشند.
🔹
یک بار خدمت اخوی بزرگ‌تر ایشان، حضرت آیت‌الله مصطفی بودیم. بحث رهبر انقلاب پیش آمد. آقا مصطفی، علاوه بر توانایی‌های علمی ایشان، در مورد زهد و تقوای ایشان مطالبی گفت که برای من خیلی جالب بود. ایشان با عبارات والا و شایسته، در مورد ایشان تعریف ‌کردند که الحمدلله به لحاظ تهجد، زهد و تقوا، درجات عالی دارند.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/466295" target="_blank">📅 19:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466294">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbewat2DgO3hMiRwKPhKRuliDtMTyDw2LqL9XplAENIoPbQ9P7TeF2gs4rB6itibgMLyCG1OnYj_tud7KeBYJtjGcL1OIaRTS9AHLYWP_VZFnSoRGxh4XUEGgN0Q1Tf5Bi1LzSX365TkbhWeGpSX15T36EU-ioxLvPwYhkiEYBQm96jwI03sFLlWVqFkerApYbXe3b2fW1sccGkIXcXX-qYZnUt8A907NUZmfJ0XKXqSwlV1rUQCkeehMUYaqVMK024zGod3q5AHVy9aIYdP0GfOnQm8QBWzGSwQR2VaSA0SApnLFi6hegrk8CY9JhCfkPXHkOBROMUXh9p32H6eaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ فرار نیروهای سعودی از چند منطقه در تعز
🔹
خبرگزاری سبأ یمن: نیروهای وابسته به سعودی از منطقه التُربه و ۲ منطقۀ الشمایتین و سامع در استان تعز بیرون رانده شدند. @Farsna</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/farsna/466294" target="_blank">📅 19:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466293">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGMGQNlGW2ePYEzTzDFL9vfpqRWoarL8LSNo5NrVB9LqD3ZixvaNQC8rcxb7whGrc5xipd1CPKqTvRrUhA7f41cnDdSHnBKqBV-F63Mw0RRUmRdi_tNkJ9UTii-44XJ4iMeMRFu6HccEClISyl19S-mTJ5gpdCKSnJRgZ7rE1l5_RPnXJsiGlMRiy4r7U2IT5BgWGivLpuKQZv28x1US803CjzDP01C-HCFH_TQPNENrrNjXLClxfHpsnkzPz4nD1x5lMuJjXmvJF_MWfipRV2tMueJn8h6vsWrGtp4v53DFtk6EQ0HH_Wg0q3xa-M0OHi2qQZGoVBsW-PJdDWxvIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
قیمت هر قلم کالا و نحوۀ ثبت‌نام در طرح «تورم صفر» چگونه است؟  @Farsna</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/farsna/466293" target="_blank">📅 19:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466292">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjS-HAnchPELQU5ai33ahMxqxzLbvGcvfxcKK7fD1fDQcIunuB1zlRUGfKo9Xl4jn3MjnH-0u0YpW1Nl5Bg9WjbrWR4l4QHil1eAx5vRJ6dIumYXEiEN_wAbaugUSetLZrVPVXJ4Qj0MUXmtcq-xdNu4i4IL90fQIqTLplb_p9eTvB53JYPJJI379HKmVZ1STzko3Zp0sHhm0RYXOo-Fm4G9mBf4Aj0eRjslExAi1Q8um4P8ggCd76mUs_l51O5YdrNahcC0qi3sBxIdGrwNWUiwJ5YLjski6wJ41TCITU7snMUfiOHSYPmIlV1c1jZYoYEaxnkuBi9-90Fk_Nr4EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین برف پاییزی بر دماوند نشست
🔹
با ورود سامانه بارشی و افت محسوس دما قله دماوند برای نخستین‌بار در پاییز امسال چهره‌ای زمستانی به خود گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/farsna/466292" target="_blank">📅 19:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466282">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c31larpnYS91ESl9QYNAWTofjGPRqDVy8YFc5uGc7vjTleBNK95Mk1Mbs06OqISffeXfg5EfREFmMxnUi5ptbAXCawBbtaQaqQnFNKG7o7yiPta437KkLgwkh9_gQFNWF6lXEY9LqPYGyl-giAMS6RuM8cfIUVTA2lG5Du0qetyUyNL1R-0YCcyeXT9ZYv28GYuZl7FzW3X5jaaTe3I9r1jC-dExF85JO-SN4TxtLf6mrgW8hgl1dsvuRKNa5J0YEk2nnp0Sparxfl-Ntlah-cNxCtURonk_zNxuC7Nz0WlRXZSD6U4rh8IKHpmRqYau6PBgtEsU6BBUeCLYhKUK0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a5rJ-cGYsw7FJYKizACLHk1L5nUuAY020ZTzlfjxm-BUoxgJWICTBFOTS9hktxJ73KKJtgcaLK40gekGettoaHH2IU2eZMKGaPZdEoaeqPUuIJEF-DBngMWxBTQfSIyUTSgD7_0yopV-FJrzVH_vuMYIO-pWAEy79juYLw1ad7yldBh2OR85saByJUF5PMjdimRz5hO1usQQ0ffDsOCxLu6e4XSE65TtS6XikKRPynOhCAqi9XdOdvHetvaJ4Hr9S6JCX09XAeGGPuPn9PHyV7YmYMaAdhGwRgyqo1jqRfo3dvu8OT70rKt4L-GMgL400OFldr_sP2HPnLt-Xz4G3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CaAunHJhaVv2fofzha5GkG0oKTvxMOD1Hjv1ESCiS5HiLD1tyQrP54AXWbqW7Wf98cRCpVdkl6CnP-Bwfm5cU-L_FMuMaOfIutrVEF4WWSuCOdQQKEwmLoVeL3ci1W4IFAFVDPyr5-U2r2qAnvGUn1fvXApzLB2kN2zDaFlytS7EaDqCA7T4MOfevvopTODIOErBYrTcCqAqHv4XIliOCPu4ydurNsA01DBMph27ChQDLVY3dVfodcc107LdMuwtsMjdupGxxeM60ECqRMBc4TXilhb7vf3fh4iQMJkSf0mNwkbkMkx8jYg9cph3HtrdzPIPwjFfbjFKkRyqLyudRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I2bzZYTNuUlLq8tf1RrrSZ0DE1vqq31Bsb0mcSGc7YxODcr2pp28LvRUuYE1rsNqGsVsIg1VOdqamBszx-VmPo6iDRzw0kA0UIco6gZOcN3JhmogE4rWK0AnkcIdoRN_Pl5dzVtMUFztcHa5zEQqwM-e7IUfGuneDIAKO4nUp1narlGUjWcjGH7Aw3eQBTMA5wWbEidmjdE8D5kkg40U3OCXwnj_NDfwllHIC9jUVxEcHXqymn2ZnfqCum9My73XMYii8JoIoYxraNk04KvEK3WL3WX0dwWUXkZmvKwb6v8kIYpSPZ0FRhEjz6NDw3rQMGHm8jzHHg43aNNw-GW_Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H29RxrYnhVsrxUvvs7Fhjruc2KY2pzIFIMYrHyTC6ahuabV-1p0vAdPPwHm3zBm9AOV8kEwexuf68uAICi3zrKJdx6ILne3txH9hLL17AerkNqppg8zPqFORZ4lt-42TJEcsX3m8j4G-vw9O2_HpMWwpSCJ17sMC-kCfEFoCtwhhnsjrxWEJH1OMNTe9jtThStwJqg2utP-hr8XdrKjhG83MOXRtn4szk5FQGTBJDcO5_Psi7FTuCjwiUf1RnCWzwpY3Qi4bQa9C7gadLxykZgLrOHCvVoVixcsuw-eiq4HCWN89-yS-WPq77l-Jq9KzOaHuDDa0OmZwutwEj-ZPbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rq6Gk4IEk32tgcWiqorOESdq6615OWYwG1mCnwA9J7hx0Q_4lr507qAtgc0N3rFrAndDzcYf9AW48Euu-Ge-oJoQ-ek0PxfoSykpuoYI8e4o0ecvWtFPiFncdP-tSCXx5OVKleBcygxYo13lWDt8vm4du-FqxV6VIpLZqByftLNOCF8HTQKDouUb79BmSnBrMsuFnDSec3MHS47jqs5cePEYmUEY0jTaEecIubWFi_7bEloyN-UiOs8Pom4hGo_I-HQ6cFFiiTbIKcu0zbJd00elDkidVh6Z1tPJXM4-aL0D3fyvZKxno5nN_CSyFVxjZ_vyj-vmBGv5mwemiFQmHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ly9IsHOXdRhMraaV76Ww1Jb5FBs9QqEVHSDL8WuVYIBgQb7kpD9oWX9CC73JT7gndWxDE81WL8vOvkly2GE1S9st9FUeoSN_QLtoHx64X44-qPKlvIeVDj1lZx5-qQSz1l9zC5VFHttJ0hdRnmslOHuuQTewp2u4P9yTfF76j0s5-R5HqTntskX-RdQ3LaqPEK0KbNbI0-7vLQDZTIgkhOkDm9tnB2z-r6WF9I6AEpW5PggT85rGAlXSKjStss5S15RXzv_PRk1oy-8BHA9UQfZU4W1spVJ-9lSzIcob2MrtQgvQpPVEqIq44kkyCBrOXPG-sPuab4-v5hNBW6wucg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PHhV6qWa7fXNEX4yNXU9i37K2AuIoXoXMnXYt0dI8qfNaR30_rRuIxXqWqMmP-FnQMzLGTIJ07EAyZ1iOC03Jecopmc6ZNFg69DiM9gYslC9WqZSFiCX4KdEOlfuXrIuQGKEu35vSyX2nnaNNkcEuVdjM4E-5gFSds2QPmJMc7Lkwgr-ttkyTrNnsjHq07fhuUJz31WoZOoxqHB0zmZFgJvsxfx33nDsj6vafAxle2XVW02wnvx3uM4VdGjnFW0EaXatWTHS472qY8IwEOMc8EgsRb7ICrn7OXI53_M1gCwjkuF_NbrZmZveY5046QH1FwJv7Ou50VZqtX8sJUa2QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pVGa9ZXi-R3nTXWSru8BFySn5gws1VnytLUZ8O4YfLnbCwh5AwTejyRp87zLN68kbPWn7WLtB1nP0OhUcgVOVg181JBLmykRIL8Fueps9xFTSQjgnUPJtSe77i_gpXUwQqZQ2-eI_Wdw7aCF0XBhnNGqYWTLiWo_5RrKkO-uQeJVF1MJlWOg71aHzQpjIRJl7hPeALuoIBDRgAWnwO4kZgB7xtepksniMRW1two64K-FPETj5Cc-arKCvVEfCk8pUeXTt6d_FG39AMpJ6vMNMNz6YCowmpV4KD1srV4OZgcqnqa74nRYQ-egtQG3FE0qv-DFgUFlfRFC3zFwN7oOVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iGulOsEZUDTI8NQGyTXW1rQfJ54Qr6UDZ1zGYgUFTTz8IiavsGKQXzfALQ6C0Yjobu5b0rTaLvJvWPewjrbzOCt6aAB4I8GmKJwbcFDqpJfWQycl0RTtXu8NpnEDDxG6o8xWntA-f56PdRGL4xAD5BC7I4iOSWgtwHyUkNwKoGaqjO3bK9WKA73xzRVSm_wrEqj2QgXa19KgTVMobB2wyAk07KuzmR06FXWuwccHsB_5P7yjaOH5tEuRZudL5tD-FUPN4ZR87djr_1BnpAAvsr2doHlYlAv8rfF_kIVe4Oh2FtvR5KAzARPbv9cSdwQIxJYmRFthVbkpLC9OUv26Fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏋‍♀
استقبال بانک صادرات ایران از قهرمانان وزنه‌برداری
🔹
قهرمانان تیم ملی وزنه‌برداری در بازگشت از مسابقات آسیایی ناگویا ژاپن، مورد استقبال مدیران ارشد بانک صادرات ایران قرار گرفتند.
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#وزنه_برداری
#بانک_صادرات
#بانک_صادرات_ایران</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/466282" target="_blank">📅 19:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466281">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAy5B7Ot68AgVrkgEiCIEf-f6kv7zQ48tMk84nCTyhc9XSpm7XM2HTSJf-kjLrIlZQopcG-PU0V3AStIP3XIk6apYbJr8FuJ3HhBpshWjN_0JClIakvXIe45VeLHHvf0VJcUWLN5Tukb63TwseL01ye8Tm7fhd8prrn6upUhRo6KkkPjSaIJKsM_11jJlCgZBvTwE-8hGTAz1sl9U41XHJ1Shec_B3e6L1aBiJ7jiV0VVEv0-GTeL815_2mlz-kblySSj3JMKOiCh71ctOS5W8h48Bc2LUK08bPySd5AQumsQNuxcZOj2TY9ZmI-wFqn_yAh1R8knVhIM2xFw1dkPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طلای بازی‌های آسیایی ۲۰۲۶ ناگویا در دستان همکار
#بيمه_البرز
علیرضا عبدولی، فرنگی‌کار شایسته کشورمان و همکار
#بيمه_البرز
، در جریان رقابت‌های کشتی فرنگی بازی‌های آسیایی ۲۰۲۶ ناگویا  به مدال ارزشمند طلا دست یافت.
مشروح خبر:
https://www.alborzinsurance.ir/PublicBlogDetail/5106</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/farsna/466281" target="_blank">📅 19:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466280">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/farsna/466280" target="_blank">📅 19:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466279">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2014acdb2c.mp4?token=kG-dLnXYnrljLqMMB4vZAF1VYZuW-sOPv0FLqBvBhGd83JsU5YR-qo12KQqO7TtW7zORcdu6O_grm-uIwSN6DdsuDaPBHmzTebqyY0e57dBxOOyJSIxfs8PHcgKaeC6N2tZKdcHnORn92b7ej4owO1FxscdahWFBM1NVBxAL3C2pVhZf5-XIlv8yhy3D54tZ-77UbJTs0cE09r70JiNw1wR4HarzmO8D9u69gEEY2kyA_VNzw1wonyR4rCi9xhnvrhqffTctq9FPZOiewgMqxW2pMIMW3M-5JOzeQ1KVspR5QeP-YTfAExlME4q6AXMxRmGF3wQTebg7veuH1nnDTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2014acdb2c.mp4?token=kG-dLnXYnrljLqMMB4vZAF1VYZuW-sOPv0FLqBvBhGd83JsU5YR-qo12KQqO7TtW7zORcdu6O_grm-uIwSN6DdsuDaPBHmzTebqyY0e57dBxOOyJSIxfs8PHcgKaeC6N2tZKdcHnORn92b7ej4owO1FxscdahWFBM1NVBxAL3C2pVhZf5-XIlv8yhy3D54tZ-77UbJTs0cE09r70JiNw1wR4HarzmO8D9u69gEEY2kyA_VNzw1wonyR4rCi9xhnvrhqffTctq9FPZOiewgMqxW2pMIMW3M-5JOzeQ1KVspR5QeP-YTfAExlME4q6AXMxRmGF3wQTebg7veuH1nnDTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رتوش چهره تروریست‌ها در ۵ دقیقه!
❌
رسانه‌های ضدایرانی سیاوش جمشیدی را با دستکاری و حذف سلاح از عکسش با فتوشاپ «معترض» جا زدند.
✅
اما سرقت، کلاهبرداری، حمل و نگهداری سلاح غیرمجاز جنگی، مشارکت در آدم‌ربایی، تهدید با سلاح گرم، شلیک با سلاح کمری و اجتماع و تبانی…</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farsna/466279" target="_blank">📅 18:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466278">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJXPsy0YB6nksIZMa_fXOpcz_qIxnGJ-SSE_PGS-u138aXIwA5mM63J-2zu6iak38c6jYQMLX74hniPtMbwmlGBzht07Zl_7d9wen6e9sZPVRPdrphA_T4y0OChTh-IC5yg3KP35_V3eV5A0wyLxRuCugjjVKcdLHSurh958RlOqkmsUzTPyR_kcaK4gGbB0o8b73XmP_a2F5WsfrGisg-oLxFW0PpfTQXM-1adxdp75x0HD-lhDmwn5ZUi_YHb07Msqp6K8I7gYhbh4-XngePV7bivcpPFgZ5jaeT8Ti8p9ZNQvSW90l1xPPL1Fc8PgoMI2Pg8wYOJTbf5kw0ZJ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت: عمر نیمی از بیمارستان‌ها بیش از ۳۰ سال است
🔹
مدیرکل دفتر فنی وزارت بهداشت: بخشی از زیرساخت‌های بیمارستانی فرسوده است و برای افزایش آمادگی در بحران، تأمین اعتبار و تدوین استاندارد ملی ایمنی مراکز درمانی ضروری است.
🔹
درحال حاضر بیش از نیمی از بیمارستان‌های کشور بیشتر از ۳۰ سال قدمت دارند و ۴۱ درصد بیمارستان‌ها از نظر ایمنی سازه‌ای باید در اولویت رسیدگی و مقاوم سازی قرار گیرند.
🔹
۴۰ هزار تخت بیمارستانی در دست ساخت است و برای ارتقاء ایمنی اطفای حریق، آسانسورها و اجزای غیر سازه ای بیمارستانها حدود ۲۵۰ همت مورد نیاز است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/farsna/466278" target="_blank">📅 18:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466277">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تداوم پیشروی‌های ارتش یمن؛ تعز در آستانۀ آزادسازی
🔹
به‌گفتۀ مدیر دفتر المیادین در یمن، نیروهای مسلح یمن در آستانۀ به‌دست‌گرفتن کنترل منطقۀ راهبردی تربه در استان تعز قرار دارند.
🔹
کنترل تربه می‌تواند برتری آتش نیروهای یمنی و امکان محاصرۀ بخش‌های باقی‌ماندۀ…</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/farsna/466277" target="_blank">📅 18:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466276">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBrkdz1poOvlcfMOJoVESyB3b9Ad2LudcIIcY_adHFEze_4BIOZrookb_TPEOFLdT2DomSk2e5i9pP5COJMrXyalUHk5Y8-LWjH4ulYIpImtlOpDvl2IvbuRLv7oWMOpQsGjFFuA7aITZ9TLclvo4K463fqBdeZwUYmVerw3Hzv7IM9vBe7dWn8X5Nh5UNr1619d0srZbXZ4WCiEBCv3jBIdk6uGYH98QbgMnafscOJnlw2vv6gzmONhsFd05mll1-AxAZEKoytuy7hDzry2SPbU2qQj8yR5084KH1ZXw8_IrBd5V9ucy6diZqFfnkEI_4gq4ZivwQxAmy4LpfJQ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه ماندن خودروهای گذر موقت در کشور هموار شد
🔹
براساس ابلاغ گمرک، مدیران گمرک در مرزها و استان‌ها اجازه پیدا کرده‌اند بدون نامه‌نگاری با پایتخت، مهلت پلاک گذر موقت خودروها را به مدت ۲ ماه تمدید کنند.
🔹
این اقدام هم شامل مسافرانی می‌شود که دفترچهٔ بین‌المللی تردد دارند و هم سرمایه‌گذاران خارجی را در بر می‌گیرد.
🔸
پیش از این تصمیم، رانندگان پس از پایان مهلت اولیهٔ خودروهایشان گرفتار یک بروکراسی طولانی می‌شدند؛ پرونده‌ها باید حتماً به تهران فرستاده می‌شد و پاسخ آن هفته‌ها طول می‌کشید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/466276" target="_blank">📅 18:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466275">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qqvm3Vji9ndERgNaK4RR24F6A0z_OfIeQlbypJGSiGTe45ExHZ42up0blORAV6fKstKJq-M5wgeXPos42M0D0wPJ8QK-8880mKnemuX9E1lw2RovmnOqneuFjwwPKdA-EngqELqG8Q3Dc7oRqML8bCRbPWNjjN1-OvGSmREzLgqX6Dry131B_PHaLW-eua65LgXfQ7DbKwFit27C7fceIpgZMMmKdsBXJCcWocA5esBOTDAkRI2i5P9eDpyOh5pidKUVOmoo6ahRqgx6rZHMC3fZFNgjl_KNnusIpb-zH5LQgczGKGMbaN6U2h6H768RExJGvLiLagYYvOE4QdznRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر رسیدن آسیایی‌ها به جام‌جهانی فوتبال تغییر می‌کند
⚽️
کنفدراسیون فوتبال آسیا درحال بررسی راه‌اندازی لیگ ملت‌های آسیا از سال ۲۰۳۰ است. این رقابت دوسالانه قرار است با انتخابی جام‌جهانی و جام ملت‌های آسیا ادغام شود.
⚽️
در طرح پیشنهادی، تیم‌های آسیایی در ۳ سطح قرار می‌گیرند. در دوره‌های هم‌زمان با انتخابی جام‌جهانی، ۶ تیم برتر سطح اول مستقیما به جام‌جهانی صعود می‌کنند و تیم‌های هفتم تا دهم برای ۳ سهمیۀ دیگر به پلی‌آف می‌روند.
🔸
لیگ ملت‌های آسیا علاوه بر مسیر انتخابی، قهرمان هم خواهد داشت و ۸ تیم برتر سطح اول وارد مرحلۀ حذفی می‌شوند.
🔹
این طرح همچنین شامل سیستم صعود و سقوط میان سه سطح و حذف تقسیم‌بندی منطقه‌ای تیم‌هاست.
🔹
ای‌اف‌سی برگزاری یک دورۀ آزمایشی در سال‌های ۲۰۲۸ و ۲۰۲۹ را پیشنهاد کرده و قرار است نخستین دورۀ رسمی لیگ ملت‌های آسیا از ۲۰۳۰ آغاز شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/466275" target="_blank">📅 18:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466274">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۴۲.pdf</div>
  <div class="tg-doc-extra">2.8 MB</div>
</div>
<a href="https://t.me/farsna/466274" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۴۱.pdf</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/466274" target="_blank">📅 18:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466270">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفالس نیوز</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pHoO6cLiIheZk7HBTE7PoBWgxAd-HjUWQ9PfFARj4_MRwkprIiR2wDFSzUWlr3eiq0BoDiQsAOUvjkQh3cjoeqNu8WJWENA38_v4lG7uK4H6IGUu0DoVWfT9YSEott0JTJlVxWjqfnJYmjHgWoik5SphyNZJE3jQ8yWthC5TuonfrgzyD7PUOWdxC_WLqp4U4zACLUZYOSCQh1b39AWQySwJNc0VihHpIIPQOwax9e9bpI5bJAWDIHFGMPtp6Slh-fkMfts8nLjblxlECzZftpSg9sltw4_p33RumXNxADD9X5_vM5Ybh8qNF8leSWk-GTXOT513Pk9DsrZH8SG4tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hcihaVWjfiNWkd7qICzJfmtwNT0vrRzgY0yd_20Y9OK8QlgInB4eKQSOSEYk-6wc9REdfXegsm9g8ZtahSiTUSTFGtJ_gOR0EmUwmC9HgGeSu9sH5ctec7wAvhk0LgSsscmNBe6fjtE3XUp_ubsscF_TOT6y-slEGIKDfeMkf__8EJTzOMlz-LO-PchSyFH-wG7K1NRYENlrc5-QoTm5AYbsrSTdZlN-q333Dl_ikyiBgTo_qB_rAECW8EG7lkuBNLCb4I75W0ccoxnuJ33Cet7d46TmJZKbua-l77SZeVnlGKaU_0GbtdlJlDQ9cvyffzOntwA9zEk5Q-61nasU6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ifg7XdEqGe-kNv_Bu-SoLe7Yw8glDok1XhpIZPu4vfBuHT39hoQsw4Ty5hEC_8MKQ8Z-FfjJJsyNfMfIMuptPMar0G-PsEinbR3KEDD7-d9ZWjG0hj2WTfihnn-OwBeyoKff1TRaiebU8TQPijqZg6O-a-Q1WSjvgs3rdQHv3ufgtLEpWZDGMDH9koU_hVacf9fJANjJxLeDGAviZTdrXH6BkBauIwWw58CBVXKyiDptgBZKl4SPEP3qTTce_Em5M2MFZFnLwvmZ91KeZziCK9QGZZL0lXedOXQPbTd2pd3WRnfersj0rljhtgBTkWCc9LxjeRNdO5PEmgZ38XdV5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yea1T4ERDZ6p3kfL6Xkgsa1hXR9lJh_9mcvHmml1BGirccqqli4zhksJGB5jQ21rzeFod1sVWd0Wog1jmHf7oqSETkGYhKY80C67Rj_MPAJyf1xZiFvrFRhf6hP6nlID-W8Ngu58zS0rbM_jX6A0BzprZwXWxyYcZl0VpoZlXeieYjsTyqLVpD8_7ZgzBSEs5tyU1-kLRiwq1ylyn38RgSL6Cylvjud7psH7zUzFV06d6Sq_r7hrUatAmLN3evOYBFiyLCMZ6OPzZ1-yAdF-yfqIc-vqFzWKq01RBfcgADL1DQqYt8gXEndJrDctwOBZ2JqAV23EFVuxJ_DN6DLa8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رتوش چهره تروریست‌ها در ۵ دقیقه!
❌
رسانه‌های ضدایرانی سیاوش جمشیدی را با دستکاری و حذف سلاح از عکسش با فتوشاپ «معترض» جا زدند.
✅
اما سرقت، کلاهبرداری، حمل و نگهداری سلاح غیرمجاز جنگی، مشارکت در آدم‌ربایی، تهدید با سلاح گرم، شلیک با سلاح کمری و اجتماع و تبانی علیه امنیت کشور؛ بخشی از کارنامه سیاوش جمشیدی که روز گذشته به سزای اعمالش رسید.
🔎
این اولین بار نیست که رسانه‌هایی مثل اینترنشنال، BBC فارسی و منوتو با انتخاب گزینشی یا دستکاری تصاویر تلاش می‌کنند تصویری متفاوت از اشرار و اقدامات مجرمانه ارائه دهند. زینب جلالیان، پخشان عزیزی، وریشه مرادی، رامین حسین‌پناهی، شتاو ساعدپناه، نوید افکاری و... نمونه‌هایی از تبدیل «تروریست» به «معترض» با فتوشاپ هستند.
⚠️
اما رسانه‌های ضدایرانی در این کار سابقۀ طولانی دارند.
نمونه‌های پیشین را
اینجا
ببینید.
@Fals_News</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/466270" target="_blank">📅 17:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466265">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nt_amRuiTk3GpIaSkkTFJC0bJeRSt_QwtUnegV07v1CofEyF9dW8sDtphHI2Ib-_HbFt7PHl1HcF_nPNs3FxP6_T45fQN8QmRlrR4Em-_eboxJS7i68u0-3WzfBi5rQF1Vwo3AXiSecdSYioZM4yhW087tMArp8nsJF1vbz5HhQoNIH8Wf_KwsEX1RzgtugiMV24SSJyn_FfWabWE1mvSb6AsAsecZ0U4S5ASRVr0IlQ8rvxsdBhGJbNfh1Nww8lmVN_wPWoC8RG6AU4o9aGCvd_Ll5NacKz9WgMA78ZLu1x0zxZeynbL89k8nGNZuvnlezD993whRVETrGp0pMd8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tn8R67gKNCe1Ts_9271w1PL-Aryde-2yT7Lv7FI5tAs_6GQ-Bg9vEhxLN0I8jGF4oY4jZ8LoguNE4sM9aGPKK1-yOCkNvlNPEbw25o3L_irXzTzXMvnQsYQ-INExlw42yF7tR2SvhIroMNIkgRWFeGQlYnopJC-GT9E28ARubbI1LEAbQGdM4Pk12CyOgZPGUUBhB0hYA2tRYGYuAgK_OzLDOhTMf9NQxWYlVhXsrXIQg6eyEZiA03Cw9cTOCf6dPpZ3GLVX3mYK7opfQ47ybhSUbZqtEUYq34YfXLTFloA63LkWFtqF8Mdhf2BM62Poris_Z0PguvzYai007X9HDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cHF3M7mC-8y1WSCihe2OEzo2CtfGBhbIMvU0zI2uj89im5VUEVYTVkYbXzhJ1ofg5EmYDxEzwUEEQkvb8erb8TSHoeeXha7JxPT8glBvCpzF7C5OznO3rTjKfVna5fCurYxpfX0_jTWyThYB98I3U9BJW_p9aKNw3ip2zHuo2frRIxDvpEKKvGW8CWg1gZZUCl49AGUpIITUS3HCskNQq0rKgqsu-R5gVmSlfmOH5RBRNN76WdwppCOIEAEbA8pt7qT9owOTYqZExt4r2ter7-G7ThwfpOj8xXuyTa17yyZpCJYvdNPOtT5ABl7U5CdTVo-1JWDZhBmJagKl1by89w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OsSgxaiKswnY_xlODJQ8zRl2Amu7HLmeZZ0GkpQVL9uQwIFHW7gAq3HkpB9L7gnIQIB4KXyHCzfiF43dTzXnfJrHYiHySjMDUDk0DBo8rL3XrUCPs707ICMIr-e2oyzlMzeRnMEauj87I5hOndyX6EliQzaJpnwqq7wySzVuBiKPBPcitQyCIJFPZtbVQxwxY_duNQ-bPXDWPaa__wmk7M21zUBh2mlncnPTim85Kmq8mIj0_QVziGEa8eQfrJprHMJ91Kk9G_atY_qBtOgoQHEtcqOFVjufSCupLO37e4EV4sG2iiqATvh9v4hQ7OrBa2hlQD2LnFfqvCwXku10sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e2cI-QK9-5OUJZduL6Q0Ihqix2O8-kqkLHbgHDeP8CwqI6tWdv9pjaVERecw0NK27hrl2UeSkf4qSXeF6lHZa2Tj6177qCv80fEcXpGjvLp6vKT_2fQF0qBhp92aIGJyUqQEUUqlsVtE9Y68AO9wGG2qFR79gKh24LHgyYatEcSy1l6p41RbK3QUkhfz-OjoCaja782sp35rmffSW6a8ssJh2psP_WGLYISaYLU2SGuMtc_orpCdS6Qlv3Qz0tdWwtDylBKloXtApgWZmJ-YpASF1F8ZN5eLd2J6pgTSt3zbjuF3r4lSZa6NUNxyfm0kkq2WbUqTrr4A3TTGWTQ5gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
افتتاحیهٔ هفتهٔ جهانی فضا
عکس:
میثم نهاوندی
@Farsna</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/farsna/466265" target="_blank">📅 17:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466263">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K37NL6M8B_2pDYUy6Mi-8HZyywo-oQFpnKU7OMOU_Q8pJEAy8z7PaXDAwvU3o6RInq8eK0bMAr0wvugj_ncrsGfKFoOgXq4d7x7h6tvpFEiFhNHv6o_EuCEOF4h2lFGka2dMUe4HtXNDkT18REeIl_bbnXVzb3qGniq3qD8IORb12u3_-Njo0JEf4LDcJvb0pZ7N34fVBtfIMuJcdSfwc1EIn6h2SKUfFVEn7pAtvKFrlRWN2LR7ncnTOrYmoONFIf8MV0xs1rMK7emHq4H-u7asHvPBbWeBLBfhV4-8GiLLsyl8Z01x6-Z28qtOp5cnL3jqHddG0c9q1ufn3o04vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پایان کار کاروان ایران در بازی‌های آسیایی با رتبۀ ۶
🔹
کاروان ورزشی کشورمان با کسب ۱۹ مدال طلا، ۱۸ نقره و ۱۵ برنز در جایگاه ششم جدول توزیع مدال‌های بازی ‌های آسیایی ایستاد و به کار خود پایان داد.
🔸
در دورۀ  قبلی بازی‌های آسیایی یعنی ۲۰۲۲ هانگژو، کاروان ایران…</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/466263" target="_blank">📅 17:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466262">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ol9G8QEAZmUJtgWRAYjk9UCEKi3qqxeX_mZmk_Fw5Cz1tTGYTarYcajHbJXAyaQ-pS026GiXoOErqajrYl3UA7Rqpf7-HD54lBH5BWAvAxSJR5WG0I_nHxfPp_-J6rs-XQeQCCxyngSm6ut8VQQFobuLZyvSvPZi6h3sIyAsQD5mvcQFpYmrtpc3KHpKQUDgCEod3_YxrYEvR6whW7qkjbfQOIXneMNyC9PdJBIv70Wh3NdvnI3msjHNHdXEbuyTEMnfPP-oZNfVndTLRR2qHLggLX89_IMcmIFuC9bK2PrwJ3qQs5tM0vl1KlksQoS3abmsTOyR4G7GZkaFZci_jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار روسیه به آمریکا دربارۀ «جنگ تمام‌عیار در فضا»
🔹
مدودف، معاون شورای امنیت روسیه، در واکنش به درخواست اوکراین برای اعمال فشار علیه منظومۀ ماهواره‌ای «راسوت» روسیه گفت: «هرگونه تلاش برای از کار انداختن این منظومه می‌تواند به «جنگ تمام‌عیار در فضا» منجر شود.
🔹
در صورت نابودی «راسوت»، ماهواره‌های آمریکایی از جمله استارلینک نیز ممکن است هدف قرار بگیرند و آمریکا باید پیامدهای چنین اقدامی را در نظر بگیرد.»
🔸
«راسوت» یک منظومۀ ارتباطی ماهواره‌ای روسیه در مدار پایین زمین است که مسکو می‌خواهد آن را رقیبی برای استارلینک کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/farsna/466262" target="_blank">📅 17:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466261">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رسمی هلدینگ تاپیکو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cC01Yv4Y4ep4PD8CBBesn2j_3YsNASYFW6UMkJWeh9H8UUCOOrHEB88FwecjuRLHqOUxUKJL0i8doWJJ8YKPeM8geIMVbtQbOYmuWy2awdPT-gkOV2hTPo2u6UtpZxM80ZQw9Fr3xHC6BbEftTi4SiywzTZmrbaMqZgdjDx8NYQN-GIWhHef0L-8FZJlaavwHddISWYrtodXDlJBsRIQRYb8Ru_uwuQ2NdxURibUIa3taAAW-Yi2xk9SLJc98xVS9awr5MtzV2TraUkZ9WAzNb-j-_KmiyDVTanH9nUfrv9v-YvRXIMm2IAtkH8WgehHwHtb0CsLx39clz5QwRAQgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرپرست شرکت نفت ایرانول اعلام کرد:
✅
برنامه ایرانول برای فعال‌سازی ظرفیت‌های تولید و توسعه محصولات پیشرفته
🔶
سرپرست شرکت نفت ایرانول، توسعه ظرفیت‌های تولید، افزایش بهره‌وری، گسترش بازار محصولات صنعتی و حرکت به سمت محصولات با ارزش افزوده بالاتر را از محورهای اصلی برنامه‌های این شرکت عنوان کرد و گفت: فعال‌سازی ظرفیت‌های سایت آبادان، تقویت تولید محصولات مبتنی بر روغن‌های پایه گروه ۲ و ۳ و توسعه همکاری‌های درون‌گروهی، از محورهای توسعه آتی ایرانول خواهد بود.
🔶
به گزارش مدیریت روابط عمومی، برند و مسئولیت اجتماعی تاپیکو، اکبر میرزاپور سرپرست شرکت نفت ایرانول، در حاشیه بازدید از پالایشگاه تهران در گفتگو با خبرنگار ایلنا اظهار کرد: ایرانول از ظرفیت‌های تولیدی، فنی و انسانی قابل توجهی برخوردار است و تمرکز ما بر این است که با برنامه‌ریزی و سرمایه‌گذاری هدفمند، از این ظرفیت‌ها برای توسعه تولید و بازار استفاده کنیم.
🔶
وی افزود: در کنار تقویت فعالیت‌های جاری، شناسایی ظرفیت‌هایی که امکان بهره‌برداری بیشتری از آنها وجود دارد نیز در دستور کار قرار گرفته و سایت آبادان یکی از مهم‌ترین این ظرفیت‌هاست.</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/farsna/466261" target="_blank">📅 17:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466257">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس‌ پرس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C2JPEP44DZq0TywxVfZ6j4e09ldTMXKTgd0zALK2j0MLTTYg2R_rXyAHZMOPBVR85tQYMmZ4b7YvW8OzdofBkdxK1ZVv-ayXQEYXrL1b0mTQ5QBDs4OeemSTlD-9Q-U4MUSlnb_F3d-vAghIkDhehM3HQmFjEXjbxRy2aKSZnD1p5sY_kW_G456qK1ftkmFHQcx2j-0_uMmtBdbdZCCuHpI9eglTEpqdrWLxLr2hrVseXUWO-sUbU6mxri7idF0shNn7hJDokjk3Oby3O1zORFaQHy8_4Xrbars67ACmdor7pygKqwVBJy9Q0R4qe26hrH9eLtGFlg8k5oeAxbiaEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xr-UrnfTrMialemdLISYnxHio40NE04bkJhov_Sh8e7SKoYUqcadhrkY98-tZTYj2BZYDEa5k67ty9jpDULtfwPF9MEwRwj4EN9DORadkYTQzLllyJ9r0fAvi4t8dyesSZ-JnCWjoDWh_cIMu-fGqTsyK8u5sEACfuviU2jf5gz3vpgUFPHfEjGudjQeDzcHZTi6D2f0D5_E6E_dHnHVpCAu6zr-3z4AEMlsZHXEhoMZVDGGa18_Vv_0pJ60U5YhT9YGo0pzKO5eN87JnoQ9zSOUg4aTkT5Q0i6oJLJEAEiYsP0jB0zXoIjGuRv0m2qogE-u1T1vEkqlu6HtCcusmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WOWRihWWxPImW9buYGKKvaFyJJYcHvIMBWoIwimJr-FfwSGFg-Tp3ROd1-zad6-6k2iLq4RyQP1lwNJWzsoteqqw9ptWq3gw1HYLiTkOQkuolXuw6odTgCkrYyRdXVDS3wvbSdv2_zFnjvVq7U9kc9YIJal6it2zMKH01fMW5GQRwd96uu-yXtG1Bl2QbhOHvC54ASFmcTkXLHRQHZdi8RA05Xcg5SX5_XXHTd7cLkBczwZNMFad63lTkvaRVcHNiOTd17jcEPluOiTp75LWt4-1rptYtB1gchx5s5SK4iNUuRTwAvOXAjStZ1rGrLdiW4jSvc7_KSGcXYZ59-2uag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ptEWBDs2BLpcCwRPcni3BFy0dNQhjC2qWZGm-4UkjeSUNVXACJOzJttkjetfKl1xnAqmCg5IMb7swB2VwACwKJZUBVKAJcW8BCWtGittvcji_91UkCxfQdk8eJsckP8Nw4SwsIFFWFhnMrkVjKHpsxK8gzedoHnCBOVUqMeK1N9QlqQFo2vYGkkrXWVFBxfELt8zdN4ck1kjA6vR9anYbfmKZeHt-TEnH_s7eQKVYYSxsM6NswPokJ8VhHzYUMgaX6c6stH3QYgZDcj0Cjz5M1OolmP-zWoNliwOe-XCI1ABhmhbkouiSNHD9X2jgRyPN_TyFuLJFRnTDGz-5lAhTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔰
بازدید مدیرعامل شرکت ملی مس از کارخانه تغلیظ مجتمع مس سرچشمه
🔻
مدیرعامل شرکت ملی صنایع مس ایران، شنبه ۱۱ مهرماه، با حضور در مجتمع مس سرچشمه، از کارخانه تغلیظ بازدید و آخرین وضعیت تولید و فعالیت این واحد را بررسی کرد.
🔹
دکتر سیدمصطفی فیض در این بازدید که با همراهی محمود خدادادی، مدیر مجتمع مس سرچشمه انجام شد، ضمن حضور در بخش‌های مختلف کارخانه تغلیظ، با مدیران، مهندسان و کارشناسان این مجموعه گفت‌وگو کرد و در جریان شرایط تولید و مهم‌ترین مسائل عملیاتی کارخانه قرار گرفت.
🔹
مدیرعامل شرکت ملی مس در جریان این بازدید، حفظ پایداری تولید را ضروری برشمرد و آمادگی تجهیزات را از الزامات اصلی فعالیت در مجتمع دانست.
🔹
وی همچنین بر هماهنگی میان بخش‌های عملیاتی و فنی و پایش مستمر فرآیند تولید تأکید کرد.
لینک خبر در مس‌پرس:
https://mespress.ir/x6TP
@mespress_ir</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/farsna/466257" target="_blank">📅 17:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466256">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/farsna/466256" target="_blank">📅 17:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466255">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IaO3VpCM6oKt6wclNIkigEoi9xKWf9MZeZIMzU2RR1jvZv6Khgft-8VUrx0qkJeKQauvvg34QBXUpjFI7amOH3J6Y5LO2UfrC9g82BcR8cFWtiss6eQoinVgWfL73G2Zs4qalMaRrl8jQGPByeXBgXUv-BRCmjjgJ6404hbEXPqblrPo7aIKiwPvfsuyrKQzd5GLYXjDM9NHdj8LZS8LA7yo4VYJHVaXikHTWRbOVT6rkpqdwiCvqVosbpS2LhfAHzZMBWUSbdU4uFQQXAeXLoJxZVR_ro0Ion7Z-EouKp7fV8YFJQB6GPEGktaaxvaheR-WlrcCaAf_K6YQsVSnrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی کودکان پیش‌دبستانی هم متوجه شده‌اند که ماجرای پایگاه هوایی «فیرفورد» یا پرواز فلای‌دبی خیلی ناشیانه برای اتهام‌زنی به ایران طراحی شده است.</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/466255" target="_blank">📅 16:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466254">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pc1j-X_FfdPNopOEBbnLD1jaHo0TXNSa_CkhjDsT7x0KGCwy-w74gH_W6PbAT5i7oIdxd7o723zjbCuxvXdpYoLaD_obGdXaDgHM3VFEdd9LP2hlZuioaveeNjzXIPcL4KhbBIapVmQovuIz0yqzrr1rqX2d5_2_xFfyJ793ww8asFkgeLXT1Yhcazl0ntUDX12njdj8Omeh71dER5AwT0ViT2sl2xYHTvxMDLGLA7Q94WJERjcf_DPSoeyIZJzaett2JQWrw3y_SwttJWYhhnStit9mjMX8C5YuUFXA3f6QmX4HDH9asVJMa-hVxDIg9Bx_vuyw4PiRwwAdV7r9Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرامکو زیر حملات موشکی یمن رفت
🔹
سخنگوی نیروهای مسلح یمن: ۲ شرکت آرامکو در ریاض و خریص عربستان هدف حملات موشکی و پهپهادی قرار گرفتند.
@Farsna</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/466254" target="_blank">📅 16:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466253">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXBcDp227dKPnHCrpwi_3m9_9sQ_Ty0_mk4pkBjFQnoYWE-fT2FX5N0esX78zf2ky0AGsU5-b90D8C5ve-N8GJ8lTc-7fDr1laihPS33qCtegV57sGUIJ5U7HDHyWk-wdJLGyOQYx33B6AoVQzoqJaRqXXvChVpCx4_b4g8XEj1ohJJMH26tmFftrVSGAkDGl3j2Hm1eOY6N5X6WD0hpdCIeXniWGLPVm-0aRt0_GhSLTmsiiJAySg8y79TXL3evMi86-9b5xd4dioju-4aNViZI8TNK95ggELn11_lmmZ2_bTiLJNO8-WesUffEWt7MLc-a-UUV7CWo_qZr_gNh2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی دولت: آیین‌نامۀ حمایت از بازگشت نخبگان خارج از کشور با ۳ محور در هیئت دولت تصویب شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/466253" target="_blank">📅 16:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466252">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0Qa9tzchjrcvakqwhh6U03q9b2f8laH7mGMEy6MpwjtjEZ7dKjFK8wkSeWaLWZLtotxqyE6lmcAbgfxdmePqG-H3i49UNHwL_U34RcKKaZm6PkAPONnMPpRnqvYanQM5EU-4SNPkjYmJsT5cKoH6hNI6TkBk6Mu-Ik-WTEwRREhoXN_s1SNmizguP4QCEDx7EZHVt_ZPBrlbdD9Yqir5XRBbAEkPyFMu11HOytFjrIen1C3talbyHM_-thPobxXaO2ZeUo-KEYgdIpuAWGbep6Neo35abCMVCLgxSNQXhw2vca1f0sWgzUId-WCZ9KIjkuulfTRdhH0s2CqE8cNbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نبرد ایران و آمریکا در میدان نفت و دلار
🔹
جنگ ایران و آمریکا فقط در میدان نظامی و تحریم‌ها دنبال نمی‌شود؛ قیمت نفت در آمریکا و نرخ دلار در ایران به ۲ شاخص برای سنجش اثرگذاری سیاست‌های دو طرف تبدیل شده‌اند.
🔹
دولت ترامپ با آزادسازی ذخایر راهبردی و افزایش عرضه تلاش می‌کند قیمت انرژی را کنترل کند؛ در مقابل، واشنگتن نوسانات ریال را نیز به‌عنوان نشانهٔ اثرگذاری فشارهای اقتصادی خود برجسته می‌کند.
🔹
در ایران، دلار به یکی از ملموس‌ترین شاخص‌های وضعیت اقتصادی تبدیل شده و افزایش آن می‌تواند به تابلوی نمایش موفقیت فشارهای آمریکا تبدیل شود.
🔹
بنابراین ثبات بازار ارز بخشی از مدیریت جنگ اقتصادی و روانی است و تقویت عرضهٔ ارز، کاهش نااطمینانی و هماهنگی سیاست‌های اقتصادی می‌تواند به تعدیل انتظارات و ثبات بازار کمک کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/466252" target="_blank">📅 16:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466251">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cebc383706.mp4?token=rxTTxDIuuMlF0WhWOCb1FH0fDcKqlOHiNFUlDTUaFpVUH01Z-RTjolY9kV3eHPaaloqH1VkjJrDh7MG2lpziFZGIF5xaX5ncZ8DFEPDxSLyyQb-jrKj_gOXFBYPrXEagZ2uZsMmVnwbqSV8lAsnrPwAXTjuVGSd4PYnJxmPbMwwpisfxj2gyWiHTUOJ2W8pJLOfpWh66fI027JepRJVUnecDlnmjERtstCRc3qwi_WYqy3DEIS_nSxLpnr1ElYeBhgU1JYU7k9UgsO4q1YtXAADyDpU7u42R-o5P9nHClICvoSycaKOCLwnxe0FngfVXtvHRDNmaqJbphYEwonlfNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cebc383706.mp4?token=rxTTxDIuuMlF0WhWOCb1FH0fDcKqlOHiNFUlDTUaFpVUH01Z-RTjolY9kV3eHPaaloqH1VkjJrDh7MG2lpziFZGIF5xaX5ncZ8DFEPDxSLyyQb-jrKj_gOXFBYPrXEagZ2uZsMmVnwbqSV8lAsnrPwAXTjuVGSd4PYnJxmPbMwwpisfxj2gyWiHTUOJ2W8pJLOfpWh66fI027JepRJVUnecDlnmjERtstCRc3qwi_WYqy3DEIS_nSxLpnr1ElYeBhgU1JYU7k9UgsO4q1YtXAADyDpU7u42R-o5P9nHClICvoSycaKOCLwnxe0FngfVXtvHRDNmaqJbphYEwonlfNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خطری که سازمان ملی هوش مصنوعی را تهدید می‌کند
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/466251" target="_blank">📅 16:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466250">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdKKBZnWe807XnqttjXYujstYip1l8qbSfga4gB4wsFsZnUwehl54CDHqMyvuGrKluyuSRTRQ5dM5t_5A0w0lX8e1djWqcCRVe3ePrSOp-xvpOz5nvEfZM6zMtza9IzFzasrxWJwjqLEG8ZsQWkd0hWnLhJ8D5vQ7ziMn6_pac6q6p0ZLQ37YKB1atCTjaGAs5NeS9hM_ODn3t-0aaOxD5P_9tiz_NerQPM5cBFmf96cwu_LCZChSvTpEpTmhPf4Lk1ak8GDzWFsM5kOnbqVE-I1FtV4Iw9keG353vqyGzkzIo0lpOVHLlOEMAkq6MuTN3m6bb3zG1rLE4aMN-UQzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنگین‌ترین ماهوارهٔ ایرانی ۶ هزار کیلومتر تصویربرداری کرد
🔹
رئیس گروه فضایی صاایران: پس از تزریق ماهوارهٔ پایا یا طلوع ۳ به مدار، تیم متخصصان به‌صورت شبانه‌روزی روی تثبیت آن کار کردند و پس از ۱۰ روز، همزمان با روز ۱۳ رجب و ولادت حضرت امیرالمؤمنین(ع)، ماهواره تثبیت شد و توانست به سمت زمین نشانه‌روی کند.
🔹
پس از تثبیت ماهواره، اولین تصاویر توسط پایا دریافت شد؛ این درحالی بود که حتی مطمئن نبودیم دوربین ماهواره پس از اتفاقات رخ‌داده بتواند به‌درستی کار کند.
🔹
اکنون حدود ۱۰ ماه از این مأموریت گذشته و ماهواره پایا تاکنون حدود ۶ هزار کیلومتر مربع تصویربرداری کرده است.
🔹
گام بعدی ما برای دستیابی به فاز صنعتی، «منظومه‌سازی ماهواره‌ای» در سال‌های آینده خواهد بود و امیدوارم به‌زودی شاهد فرود ماه‌نورد ایرانی بر سطح ماه باشیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/farsna/466250" target="_blank">📅 16:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466249">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">فردا زمان برگزاری انتخابات شوراها مشخص می‌شود؟
🔹
جوکار، رئیس هیئت مرکزی نظارت بر انتخابات شوراها: زمان برگزاری انتخابات هنوز نهایی نشده و فردا در جلسه مشترک با ستاد انتخابات کشور دربارهٔ آن تصمیم‌گیری خواهد شد.
🔹
احتمال دارد انتخابات در برخی شهرها به تعویق…</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/farsna/466249" target="_blank">📅 16:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466248">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ad175c275.mp4?token=ql8vR8qQlGbnrMeNAUYuuBeZZws-OA0X5hg8wpKVAzB4XM1RwnZUc48rYD1VkjNpUC7Hxc0giZrnaTKNLmDLO_F1alhym2r9uNm6780hwFE60Q033VczT4VjBnihT1BZxH0EQyBSX_SLuMw7gO4PRnUFMvSBztxuSEg0e-yUa5WyuSzLIHgBQRnBvFO3L71_pHT-ZD6spo-9iJlfiKNqmT7OMtSeNxQxvl_PD2NJe7AlfMZzjclOLulmSeHvpEvhdsGCBI-5x1jSy7Px60OMX5fAQ3E7qwtfK0tvDXbVDtd2yLnngUTq_cJmMYHAdO8geTFHVm07yazSjkUtxbPzUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ad175c275.mp4?token=ql8vR8qQlGbnrMeNAUYuuBeZZws-OA0X5hg8wpKVAzB4XM1RwnZUc48rYD1VkjNpUC7Hxc0giZrnaTKNLmDLO_F1alhym2r9uNm6780hwFE60Q033VczT4VjBnihT1BZxH0EQyBSX_SLuMw7gO4PRnUFMvSBztxuSEg0e-yUa5WyuSzLIHgBQRnBvFO3L71_pHT-ZD6spo-9iJlfiKNqmT7OMtSeNxQxvl_PD2NJe7AlfMZzjclOLulmSeHvpEvhdsGCBI-5x1jSy7Px60OMX5fAQ3E7qwtfK0tvDXbVDtd2yLnngUTq_cJmMYHAdO8geTFHVm07yazSjkUtxbPzUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دارندۀ مدال برنز المپیاد اقتصاد: اصلاً نمی‌دانستم المپیاد یعنی چه!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/466248" target="_blank">📅 16:11 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466247">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">حملات موشکی یمن به تجمع نیروهای مزدور سعودی
🔹
سخنگوی نیروهای مسلح یمن: تجمع نیروهای سعودی در شرق استان الجوف پس‌از ناکامی آن‌ها در پیشروی به‌سمت مواضع نیروهای یمنی هدف قرار گرفتند؛ این تجمعات با چندین فروند موشک بالستیک و پهپاد هدف قرار گرفته‌ شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/466247" target="_blank">📅 15:56 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466246">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIT0C4MzG6_5odRUHKysdB64X3hbTxsxNqOCdqbhux3tzNLE9GwGyStMeuW1PGQj_l7soWubx8vHQA-gI4nXWJj2x_MmriUO3ZiEWLP7NmJumrE03Az2DJ_yYLOU_zN6NbPKSL1hvVXEF9Bcm6xoyA1vSxnByZhCq5C0DuMaBvSF8uPL6SiM29y3i_63CwA0lnWhtHmdj-MII5nsSRoDFDRl1N4T3dpo1qynegFqx1b9Fw7Dzp_namqdcdsmu6Tvm7egeaNpp53jX4eJ292NzW9p2WRlp7JpqE7SA-wp2wtq1uww9fKw0VGKkQldC1xOE5sS71ALE860ASMG-VzNfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه جایگزینی تراستی‌ها آزمایش شد
🔹
بانک مرکزی تاکنون بیش‌از ۱.۵ میلیارد دلار از منابع ارزی خود را از طریق شبکهٔ بانکی روسیه منتقل کرده است؛ مسیری که طبق اطلاعات فارس ظرفیت جابه‌جایی میلیاردها دلار دیگر از منابع ایران را نیز دارد.
🔹
بیش‌از ۳ میلیارد دلار از منابع ارزی بانک مرکزی در بانک‌های روسی نگهداری می‌شود و این بانک‌ها بابت آن ۱۶ درصد سود پرداخت می‌کنند.
🔹
این ظرفیت درحالی وجود دارد که حدود ۸ میلیارد دلار ارز صادراتی در حساب‌های تراستی ۱۸ بانک باقی مانده و به‌گفتهٔ دیوان محاسبات، موجب تأخیر در ۸۵ درصد معاملات مرکز مبادله شده است.
🔹
شبکهٔ بانکی روسیه می‌تواند علاوه‌بر چین، برای تسویهٔ تجارت ایران با هند، برزیل و کشورهای آسه‌آن نیز مورد استفاده قرار گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/466246" target="_blank">📅 15:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466245">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی بانک قرض الحسنه مهر ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHZ67gAjLoXXxayRAmki1yQs4rWDL08W9hMU-M9QD9tC6HTmEe9MkRBxuyPv1Ognu0I9YOGNywKB5G8oWC1fsfzU9G-4YpkfThdjQ3YT1kA1W2B53veAxSpI0-54vy7z5jf2c5ZSzQ-c2huzdxWLM_vTDnKf21lFl4OZ-omMuyp4xfQ7ydgk7M-fM9Jt89r7UOav-R-YqL_jwzAC7O2QH6e2sVSYGggNcDn5AFAOS-k05KhtSH9olBCIWhJBAqCCZos7O32Q6o9lSST2I64JgrOiwjp01d63b4oc4dRNSSoIw8BzninShBTbAD3xxGpozUzFAOPHUwhCV0DQhrfrLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
🔹
🔸
🔹
🔸
در میانه سال دوم اجرای برنامه جامع راهبردی و فراتر از اهداف تعیین شده
🔰
منابع بانک مهر ایران از ۱۰۰۰ همت عبور کرد...
🔸
بانک مهر ایران به‌عنوان اصلی‌ترین متولی بانکداری قرض‌الحسنه در کشور، موفق شد با گذشت تقریباً نیمی از سال، رشد قابل توجه بیش از ۴۲ درصد را در شاخص مانده منابع تجربه کند و در باشگاه بانک‌هایی با بیش از ۱۰۰۰ همت قرار گیرد.
🔸
بانک مهر ایران به‌عنوان نخستین و بزرگ‌ترین بانک قرض‌الحسنه کشور، در دومین سال اجرای برنامه جامع راهبردی و به‌رغم ریسک‌های متعددی مانند بروز دو جنگ تحمیلی به کشور که شرایط کلان اقتصادی و فعالیت شبکه بانکی از آن متأثر شده، توانست منابع خود را به یک میلیون میلیارد تومان ارتقا دهد.
🔸
بر اساس برنامه جامع راهبردی، خطوط کسب‌وکار بانک تعیین شده و به تبع آن سبد محصولات متنوعی در اختیار مشتریان هر یک از گروه‌های خرد و اجتماعی، اصناف و کسب‌وکارها و همچنین سازمان‌ها و شرکت‌ها قرار گرفته است.
🔸
این موضوع در کنار تأمین مالی ارزان‌قیمت، سرعت بالا و فرآیند آسان پرداخت تسهیلات، ارائه خدمات متنوع بانکی و مالی به مشتریان و پایداری سامانه‌ها موجب افزایش تعداد مشتریان این بانک به بیش از ۲۴ میلیون نفر و به تبع آن رسیدن منابع به عدد ۱۰۰۰ همت شده است.
جزئیات خبر...
🔸
🔹
🔸
🔹
🔸
🆔
@mehreiran_bank</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/466245" target="_blank">📅 15:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466244">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_2TtTq-3OmSJFmfrMixrR_OUsO9oGA53SmIfy7dP-QzZjv3Ho6yWBzOx3Vo-NlPvQ_G0iD4PBztaxZEJ9PGqC4yg_n4pKhfeePasAlvBaGz8ODhC1nnEcQ_FDk2jDWbVnBBjueF9A2SayaC6lozPq3mpbHtOPATtOLeGs9ASS7HFlEY_EXBu-kWoK2o0M6U8yorG_wqAOUdQXcVQdTK8RSla6-YD6YPoYhFGSktjP5EKePCMPyQ6ttjazxxC3lS2rYDtn6BzIDfTiLjnkvvFbEd0Y8YZOaXHGq4IAd83GLO1g1uVFB4B-T28KOZE7ZYqKUPvuHRFyxRvBOkP7F_BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یار دبستانی اُپارک شروع شد!
🎒
💦
شروع مدرسه رو با یه خاطره هیجان‌انگیز برای کوچولوها همراه کنید!
🥳
اُپارک به نوآموزان متولد سال‌های ۱۳۹۸، ۱۳۹۹ و ۱۴۰۰ یک بلیت هدیه می‌ده.
🎁
📅
۴ تا ۳۰ مهر
🎟️
کافیه هنگام مراجعه، کارت شناسایی معتبر کودک رو همراه داشته باشید تا بلیت هدیه‌تون رو دریافت کنید.
👇
برای مشاهده شرایط کامل و اطلاعات بیشتر، همین حالا وارد لینک زیر شوید:
🔗
لینک</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/466244" target="_blank">📅 15:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466243">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farsna/466243" target="_blank">📅 15:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466242">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqiR1C8GcxOV3087YGv88Ek-bRPrTSS0bCbCGFU0mP11SG1D0pSpHWF7605ANBIovWDf6YUiPq-yeia6FqlseY7UdNB-QGFdy4B9Nr5RNJyMsX39vfrl-VU2zPNRFe0m0ta1QazD1p7Mj52tL4tmxjilmqQPod6K8wpICKlQrp6qApTDS25lKf11q-iX0KlJO-x3hz452R_6njtorF8CJnIuhKeNIrPxE8xgAU09RHIN-oXx7TtO1qE6F4F23M1nn6c4yv8hXfP2L2dFseIFkwxaEpeTJfzP-WnrBEDaML7uNKGL-fq5Hxm20vkcjMJJaU407bmHYqMrKla-px4mpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از سرگیری پروازهای نجف از فرودگاه مشهد
🔹
مدیر روابط‌عمومی فرودگاه شهیدهاشمی‌نژاد: اولین پرواز در مسیر مشهد - نجف پس از اعمال محدودیت‌های دولت عراق، امروز ساعت ۱۸:۴۰ انجام می‌شود.
🔹
دومین پرواز نیز یک ساعت بعد از آن به انجام خواهد رسید و تعیین قیمت بلیت در اختیار سازمان هواپیمایی کشوری است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/466242" target="_blank">📅 15:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466241">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzuXRlfCF_RPGOhcy1FyW_b44B-RKDWAWWcolO2IcrBT7sBQTlkOfjKt3HQy-mS69ogWMXRjlR_sIH-pdz2NyAiPnkL8UyRCj_8J2G5Z9oymb8IV1kbuR3tJUb4QfQ4zjAyvuvgWrIehTgtfzmv09nAIE45ItnQrrlq99rW-yGrSKD9jFZtcW8RUH6Y8_glL4ka4sxwD6qmrS2uhY8gd5Pmuei2gl_sqYfq8lanbal97QEu7ni2qgUC5kIaeXCks00RXn1_UUj-0tdeez88KTYH5ivo4aE6rL8n-1re-0suvxpn1khmIToc8s81uAclxZLMcomXcW0lEg3nZM7hQgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال صهیونیست: شاید اسرائیل چند سال آینده دیگر وجود نداشته باشد
🔹
ژنرال بازنشسته ارتش اشغالگر با هشدار درباره آینده این رژیم گفت اگر مجموعه‌ای از بحران‌های داخلی، اقتصادی، امنیتی و بین‌المللی حل نشود، ممکن است اسرائیل چند سال آینده دیگر وجود نداشته باشد.
🔹
اسحاق بریک در مقاله‌ای در روزنامه «معاریو» تأکید کرد نخستین گام، خروج جامعه اسرائیل از وضعیت «انکار و سرکوب» و پذیرش واقعیت‌های موجود است. او جامعه اسرائیل را دچار شکاف‌های عمیق میان راست و چپ، مذهبی و سکولار و عرب و یهودی دانست و گفت غلبه منافع گروهی بر منافع داخلی، توان جامعه برای مقابله با چالش‌های مشترک در حوزه‌های امنیت، اقتصاد، آموزش و زیرساخت را تضعیف کرده است.
🔹
وی همچنین درباره انزوای بین‌المللی و تضعیف روابط خارجی رژیم صهیونیستی هشدار داد و گفت این رژیم طی سه سال جنگ بخش مهمی از روابط خود با جهان را از دست داده است. به گفته بریک، اسرائیل در حال از دست دادن حمایت آمریکا و کشورهای اروپایی است و ادامه این روند می‌تواند توانایی آن برای ادامه حیات را با مشکل مواجه کند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/466241" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466240">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کشوری که ۱۵۰۰ برابر ایران هزینه کرد اما چهاردهم شد
🔹
قطر با صرف میلیاردها دلار برای ورزش و جذب ورزشکاران خارجی، ویترینی پرزرق‌وبرق از قدرت ورزشی ساخت، اما نگاهی به نتایج این کشور نشان می‌دهد پول، به‌تنهایی اصالت و قهرمان‌سازی نمی‌خرد.
🔹
این در شرایطی است که کمک مستقیم به تمام فدراسیون‌های ایران در سال ۱۴۰۴، فقط حدود ۱.۲ میلیون دلار برآورد شده بود.
🔹
ایران در بازی‌های آسیایی ناگویا ۲۰۲۶، ۵۲ مدال گرفت و رتبه ششم آسیا را به دست آورد؛ در مقابل، قطر با هزینهٔ ۱.۸ میلیارد دلاری برای ورزش در سال ۱۴۰۴، تنها ۱۶ مدال گرفت و چهاردهم آسیا شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/farsna/466240" target="_blank">📅 15:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466239">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXuqCAKvD25F6kCIouvbi01-O3INloNGpF3xUERGhdzRErnEiGXOJdemW5v9SS1wWeTJfVwzRqvAZE9fjbBDff0eA3kXBsYEAigB_YLhaglpSV7rHsSslpgxOKtzQ6lcTlr1Y9EFEeunDS7d9MB1vs6e3CTRnJ-irVct384vPrnOzfWnJKNmGbyLWpGfGl35nPgaxc15LgAHal8-ZjsWEA46Ajn54nzsGK4eD-PKE5Gid6v6vK86RL4Ih7iypJeZFlx1IXVeVW6rJzZ_FdWxCWnTvWQTvxiAbm_7W1OJvwBqCnKsFDIIvMvf-c2CwNZFs3laBoiSgKtse6C7xIYWRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل دسترسی کاربران رایگان جمنای را محدود کرد
🔹
از ۹ اکتبر (۱۷ مهر) کاربران رایگان جمنای فقط به مدل Flash-Lite دسترسی خواهند داشت و مدل‌های Flash و Pro برای آن‌‎ها حذف می‌شوند.
🔹
مدل فلش‌لایت برای پاسخ‌های سریع، کارهای روزمره و گفت‌وگوهای معمول طراحی شده، درحالی‌که مدل‌های فلش و پرو برای وظایف پیچیده‌تر و استدلال عمیق‌تر کاربرد دارند.
🔹
مشترکان AI Plus نیز دیگر به مدل Pro دسترسی نخواهند داشت اما کاربران AI Pro و Ultra همچنان به هر سه مدل دسترسی دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/466239" target="_blank">📅 15:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466238">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgyQd3I4PS_N5tKwON_V5gBakmn-9128A_fUyUVHdpgBipdamLYJgzReI7Te2nWg8Y8gQ1WTYgx2k05bM1RB0m4kh8VqTlAlEIUz1eH7h4MancF-dyfk0WEiALcgMsrsZ4nDpLM9QOo4yaGFdyKtBkr3BNhwLSaSd24_mUDiaAFP1ich3w9vOmYlf9G-t8MEL11hUEl-i1nqw6icwwTE43xDJF0xn7HvivorGniy8vhBWZZIc46BchyHodOtegDx3bCE0hxQZcjI5qLKnQYCLtUoLYiqKB3buft-9drN1Rgxr4cCjRuvyPVOele6x3rhNuhIe2Imz63d4BPjRxB9tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
رئیس سازمان حج و زیارت: اگر کسی از حج امسال انصراف دهد عین پولش برگشت داده می‌شود و سال آینده می‌تواند ثبت‌نام کند و اعزام شود.  @Farsna</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/466238" target="_blank">📅 15:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466237">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2f2cb823.mp4?token=Dx6AqoNgqTbEw3iOQ9IN1Ptz6ILVi1pU2qEAb1qtlB1T5aJvxR_OieEUFBpBw0eH7N1CbCzEUnG34R9wOWXPQDEE7A1ItiqHFu9skGKLlwhv-9vmQSZZHgP1bD6ZSHQ3jWD1OZewaK4f76BeFpxExBPMOfF7AriBUh3yfQxyz6050sd6rPNrCKvWUss8pLqTCrb29ylgv46YARccnpp-8b-5mYMZB_yafZiqU1tUtH5sjQ-PYnFaRGSdQR0CKHt5IDA4M_TQRFO4WRqMlTIQhRebb6Z2HcAuhACzef31BfieCGIePcPiDqAWBmUthxpuf3oQ-i-bxjnFGnnUlxBj0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2f2cb823.mp4?token=Dx6AqoNgqTbEw3iOQ9IN1Ptz6ILVi1pU2qEAb1qtlB1T5aJvxR_OieEUFBpBw0eH7N1CbCzEUnG34R9wOWXPQDEE7A1ItiqHFu9skGKLlwhv-9vmQSZZHgP1bD6ZSHQ3jWD1OZewaK4f76BeFpxExBPMOfF7AriBUh3yfQxyz6050sd6rPNrCKvWUss8pLqTCrb29ylgv46YARccnpp-8b-5mYMZB_yafZiqU1tUtH5sjQ-PYnFaRGSdQR0CKHt5IDA4M_TQRFO4WRqMlTIQhRebb6Z2HcAuhACzef31BfieCGIePcPiDqAWBmUthxpuf3oQ-i-bxjnFGnnUlxBj0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کشف کارگاهی که بسته‌بندی برندهای معتبر را جعل می‌کرد
@Farsna</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/466237" target="_blank">📅 14:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466236">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14f6940786.mp4?token=YbujUF9V6DNDbV_eggZhmYdKAd3FraaJO8q_DQRXx9mQHmnD8gkWN5VhJVOtM7d0k7VOLZAGuonx5_5rsy0Tw_D5OStJAVApOx9AOPYyBCEZ0SKgPy0GyaIoFJCkYGBgM-0_xvSiaOJLS1dr4L-fTKItNMHEX-CXLIUIcgtzitNpjgZs6ByEniM31Rzf6I0yDpTs6TpfHwUcMGnhBmLcgTGMcyVF8DJftGbOCQMiV2t1uvpHyQANN2IZsJcilxNztAZIIiyhsamJ5A1ar9zYUTL5zagC9VpqBKgD04YnWwG-S326by5laaNIRDSDILydSZgM2KR7FtnFR9FULby4Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14f6940786.mp4?token=YbujUF9V6DNDbV_eggZhmYdKAd3FraaJO8q_DQRXx9mQHmnD8gkWN5VhJVOtM7d0k7VOLZAGuonx5_5rsy0Tw_D5OStJAVApOx9AOPYyBCEZ0SKgPy0GyaIoFJCkYGBgM-0_xvSiaOJLS1dr4L-fTKItNMHEX-CXLIUIcgtzitNpjgZs6ByEniM31Rzf6I0yDpTs6TpfHwUcMGnhBmLcgTGMcyVF8DJftGbOCQMiV2t1uvpHyQANN2IZsJcilxNztAZIIiyhsamJ5A1ar9zYUTL5zagC9VpqBKgD04YnWwG-S326by5laaNIRDSDILydSZgM2KR7FtnFR9FULby4Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: استان‌های شمالی و برخی استان‌های شمال‌غرب، غرب و جنوب امروز هم شاهد بارش خواهند بود.
🔹
همچنین فردا در بخش‌هایی از استان‌های گیلان، مازندران، کرمانشاه، ایلام، اصفهان، استان مرکزی و لرستان باران می‌بارد؛ موج جدیدی از بارش‌ها پس‌فردا وارد کشور می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/466236" target="_blank">📅 14:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466235">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b3aa391a2.mp4?token=ETEkFy04liWeKFRbHFEssDPNvppwSi31TLFaWjBDqiseRo_S8ObREHKjTcNRyGizgy5T5uHzIE2M_CdHGat7Rk7FF1ThyRWxpGObY_fqZh-XcG9hZzb-9XabxSXzGiHegwSsrCunTI5oOiCrL9WCZPZtcLKcfLHwxhX1ATYI-5JPHkbicmEyJxvyIbe2eVmpn0oarCWBUMosN6fIKwI5WkCRRnj61MoTp8U7ldmTLUbI7-87Jeu67QB3HVYfHFUD9GsqoBKcmDCg6CQOOG9t9F6_I7DBloTTZQ0ce-WEiRI_0dy-4rsIbR_pGI5xjxPiTp010iqnKHdOeO1bXuOw11qjgEO6LjuAXo_ktn9IkiXRhAd5h47RQdtwmdrvxlCiwbw0xWTgvo6PjrioALILz1pV_QZThS_D2MslZFvxlXTmZBxAD_RE0mLdopCa5hMteFsQ4f7Qpr4lU3zrOMepp851swvtaNCAFMywWztGibtggBO-Fv3SiguvMP3eA9ho8uxMQa0iv_4WZL9CNqykD1w94f1OFRnvsz08JlTq-yEoy6DM5oLSfouObqEh2ySAROMtxTdyhxbe7HaXRMWxWmwmZkT9-u83nm9Ds-HLnU2svFiQ-STtjGoSGz_LBRYFNJ0ZPggCEyFzwdtZZi62bEuWZHvfPxltZHVGcnhyRpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b3aa391a2.mp4?token=ETEkFy04liWeKFRbHFEssDPNvppwSi31TLFaWjBDqiseRo_S8ObREHKjTcNRyGizgy5T5uHzIE2M_CdHGat7Rk7FF1ThyRWxpGObY_fqZh-XcG9hZzb-9XabxSXzGiHegwSsrCunTI5oOiCrL9WCZPZtcLKcfLHwxhX1ATYI-5JPHkbicmEyJxvyIbe2eVmpn0oarCWBUMosN6fIKwI5WkCRRnj61MoTp8U7ldmTLUbI7-87Jeu67QB3HVYfHFUD9GsqoBKcmDCg6CQOOG9t9F6_I7DBloTTZQ0ce-WEiRI_0dy-4rsIbR_pGI5xjxPiTp010iqnKHdOeO1bXuOw11qjgEO6LjuAXo_ktn9IkiXRhAd5h47RQdtwmdrvxlCiwbw0xWTgvo6PjrioALILz1pV_QZThS_D2MslZFvxlXTmZBxAD_RE0mLdopCa5hMteFsQ4f7Qpr4lU3zrOMepp851swvtaNCAFMywWztGibtggBO-Fv3SiguvMP3eA9ho8uxMQa0iv_4WZL9CNqykD1w94f1OFRnvsz08JlTq-yEoy6DM5oLSfouObqEh2ySAROMtxTdyhxbe7HaXRMWxWmwmZkT9-u83nm9Ds-HLnU2svFiQ-STtjGoSGz_LBRYFNJ0ZPggCEyFzwdtZZi62bEuWZHvfPxltZHVGcnhyRpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درخشش ایران در المپیاد جهانی نجوم
🔹
تیم ملی المپیاد نجوم و اخترفیزیک ایران در نوزدهمین المپیاد جهانی این رشته در ویتنام، با کسب ۵ مدال طلا در میان بیش از ۶۶ کشور و ۳۲۰ دانش‌آموز درخشید.
اسامی مدال‌آوران ایران
:
🔸
سارینا علم‌پور
🔸
محمدحسین حسینی
🔸
هیربد فودازی
🔸
حسین معصومی
🔸
ارشیا میرشمسی کاخکی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/466235" target="_blank">📅 14:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466234">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">صدای شنیده‌شده در بندرخمیر مربوط به فعالیت شرکت گچ بود
🔹
فرمانداری بندرخمیر هرمزگان: صدای انفجاری که در محدودۀ شهر بندرخمیر شنیده شد، مربوط به عملیات معمول و قانونی شرکت گچ خمیر بوده و حادثه یا شرایط غیرعادی گزارش نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/466234" target="_blank">📅 14:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466233">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5756415753.mp4?token=NsmDmx_UUY75MoVk6mhhx-bC-bFLgiW7fpPDGfReJ3wDv1lbdgC4BSvKI-O8JMh3PLKiTStXz_MEmLzNLEfdjkzmrrClNMmZNPKS1bMKkLso-Uc1x_MA7j4cl_xZ4CI35BDOgRnnwqHeOetGXrtMPBp1Wzd-tqCikpfiaLsJuPVzblUO5bZAJGQ-Z44xopYUu-gU5btYJ42PqFrKSTFlRB9wBKZhJC6pYMD6IjL1lt7NRAeSvo4cmxzvFsgcrOY3iTqGFQjgE8u0rqB7OMOcxFe8zs9pAUXMcoe66iq_YOAUv4_AiHKtBY_z454NTJ3i9xH1NgRlyrgcEu7IGJFVAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5756415753.mp4?token=NsmDmx_UUY75MoVk6mhhx-bC-bFLgiW7fpPDGfReJ3wDv1lbdgC4BSvKI-O8JMh3PLKiTStXz_MEmLzNLEfdjkzmrrClNMmZNPKS1bMKkLso-Uc1x_MA7j4cl_xZ4CI35BDOgRnnwqHeOetGXrtMPBp1Wzd-tqCikpfiaLsJuPVzblUO5bZAJGQ-Z44xopYUu-gU5btYJ42PqFrKSTFlRB9wBKZhJC6pYMD6IjL1lt7NRAeSvo4cmxzvFsgcrOY3iTqGFQjgE8u0rqB7OMOcxFe8zs9pAUXMcoe66iq_YOAUv4_AiHKtBY_z454NTJ3i9xH1NgRlyrgcEu7IGJFVAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ کابوس جمهوری‌خواهان شد
🔹
وزیر خزانه‌داری آمریکا: مردم آمریکا زیر چرخ‌های کامیون تورم له می‌شوند.
@Farsna</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/466233" target="_blank">📅 14:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466232">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38fd43416c.mp4?token=Q3gTJomXlNBjmekyXf8bLnhpN7628tbwX0eaUb1CXGRiXLLmSIi-2Tx5imD3ZzUg1MVYidMvsbw5EpR-9BN6iy6hXU58DmVgnOXFtHng3BvMfdspDofhqb-jXG_r-tN0hvQKXCmyat9lg_i9anxP7jWK4O5CVgff6G0tvWSCK-W8_UiTm-cgG5R8AsqvoUz2M6lSNleyrgqSoDS0ZrrfUecAvbKUciqU7yxO4w_49dk9XjeH59GDrIOVNNaieZql7c9PiPVcS0hYW-VD_BWS0W6C_jIndIhKd3cfaHrtsDKop_MrgHM3Nh-oLGnqwl7ivb2kYCuL6goS__1yQ-wnfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38fd43416c.mp4?token=Q3gTJomXlNBjmekyXf8bLnhpN7628tbwX0eaUb1CXGRiXLLmSIi-2Tx5imD3ZzUg1MVYidMvsbw5EpR-9BN6iy6hXU58DmVgnOXFtHng3BvMfdspDofhqb-jXG_r-tN0hvQKXCmyat9lg_i9anxP7jWK4O5CVgff6G0tvWSCK-W8_UiTm-cgG5R8AsqvoUz2M6lSNleyrgqSoDS0ZrrfUecAvbKUciqU7yxO4w_49dk9XjeH59GDrIOVNNaieZql7c9PiPVcS0hYW-VD_BWS0W6C_jIndIhKd3cfaHrtsDKop_MrgHM3Nh-oLGnqwl7ivb2kYCuL6goS__1yQ-wnfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برجک زندان رجایی‌شهر فروریخت
🔹
در ادامۀ تخریب دیوارهای زندان رجایی‌شهر البرز، برجک این زندان نیز تخریب شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/466232" target="_blank">📅 14:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466231">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88addec6bc.mp4?token=h7bpzjzEke6qT6kjrGMQJuHaYNGKkoIglnCvQ6oSve-uUQjwISHScWZPPHoYPtu6iS54sAYznS4zMYNXTRptUk0jT1s2-KFAj7haC4J86j-rXrL-Y3TXjBKHXrkO5u5kaliBQVys3nD4vbYBfIAAf-fSziUQmHe9tYSrsbode_KGmQAoU_W_QtW8qSB_nBdA64rc4RCT3bYR9RBK7YOSSnZs7c4ObfcVp6M6A8O5JdLsmJEwaBJKO7h0HMxeMCSduQdbtdjWcaopfFB7TPo9y_9VNE4g_iu5f7q74EcS1CSupcUWKsJ38rseAiMt9PBr9Fg-MYEa4deHdocc3wDb2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88addec6bc.mp4?token=h7bpzjzEke6qT6kjrGMQJuHaYNGKkoIglnCvQ6oSve-uUQjwISHScWZPPHoYPtu6iS54sAYznS4zMYNXTRptUk0jT1s2-KFAj7haC4J86j-rXrL-Y3TXjBKHXrkO5u5kaliBQVys3nD4vbYBfIAAf-fSziUQmHe9tYSrsbode_KGmQAoU_W_QtW8qSB_nBdA64rc4RCT3bYR9RBK7YOSSnZs7c4ObfcVp6M6A8O5JdLsmJEwaBJKO7h0HMxeMCSduQdbtdjWcaopfFB7TPo9y_9VNE4g_iu5f7q74EcS1CSupcUWKsJ38rseAiMt9PBr9Fg-MYEa4deHdocc3wDb2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
۱. آرش محمدی</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/466231" target="_blank">📅 14:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466230">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86022fba13.mp4?token=kF1BbXQ8_Pd6g_qwYKoS64LMlOvovt5SILAGo8FAviw-uLcIb36DbdSZO9uQ4EGUOYAiVfST9Zxg5djqO0gtVcJm3VvHaZrvAikGh1FWlFMEoutSkAogltKp4hKH91_YlES0_RS_6X1DjJo-rg3Dvvw2Ouncc7djsceCXzoPH85baPkq53yDnzX-By-qFYXbND7z4lGBKWG-pvoq6U__UWxZ9tpCuXttC8yN2WEZYQOdoKVE-fDr7VV6c5Oni8ZOUe1AD9-rdYZieR0Z1BH1NV1LAuIXcCNnFBajXW2y9rE5SxkIVb6soAeNVjZ-DDDKLf8vknLJgLGBSVwWslzOZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86022fba13.mp4?token=kF1BbXQ8_Pd6g_qwYKoS64LMlOvovt5SILAGo8FAviw-uLcIb36DbdSZO9uQ4EGUOYAiVfST9Zxg5djqO0gtVcJm3VvHaZrvAikGh1FWlFMEoutSkAogltKp4hKH91_YlES0_RS_6X1DjJo-rg3Dvvw2Ouncc7djsceCXzoPH85baPkq53yDnzX-By-qFYXbND7z4lGBKWG-pvoq6U__UWxZ9tpCuXttC8yN2WEZYQOdoKVE-fDr7VV6c5Oni8ZOUe1AD9-rdYZieR0Z1BH1NV1LAuIXcCNnFBajXW2y9rE5SxkIVb6soAeNVjZ-DDDKLf8vknLJgLGBSVwWslzOZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر ارتباطات: ۳ ماهوارهٔ جدید از منظومهٔ شهید سلیمانی در دههٔ فجر رونمایی می‌شود
.
@Farsna</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/466230" target="_blank">📅 14:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466229">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGlZpm1ZTH0HM-i8b4VTTLSljO4cKa3CDvqvenSVCJylX946vTO1ySkZVZWXa-5V4Nli97DpJdsEv5uKIBChZXu5Ys8kuwEm2Ju9SGoL4qZ8_wPB0RlLrCTrzfbe3NYoVqnr2f5YhEwOuAdKwgoOmNBeqkAuijdrdreQIDGcmRtsbfFzFtaTN2b-h7jlJ0nOn-tCqz--uKE3c0H294yrS3sW8GXd-ckgvQ3SJybzhQru6SuHWUuEgWzY2CGwAH-TiyoG3H_uAKwKP0-sgUIoLCTvo6h3tu1R81Tsu3BGWpiknCg3xk3FSv1ik0CpXKnFauSM14vU4rLimMf-2Sr_hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک نفتکش در تنگهٔ هرمز هدف قرار گرفت
🔹
به‌گزارش سازمات تجارت دریایی انگلیس، یک نفتکش در تنگهٔ هرمز هدف اصابت یک پرتابهٔ ناشناس قرار گرفته است.
🔹
ناخدای این کشتی می‌گوید که بر اثر این اصابت به موتورخانه این نفتکش آسیب وارد شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/466229" target="_blank">📅 14:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466228">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b68653419.mp4?token=OL3eib1OUheByO0p57fr6G0mHVCfEvQq_iVlk7uRsdC-374324i0j3Rmg911eb6zb-FPZKX7pkWxebEz2KKc8MbKgvDi0roc0IHsIa_vBK70MyZ5OI8RvyDONxabQ0zuHrWO6w8Yut_MUiMTwy7JglzabmAlHfBw_wGfOcxNNXwvt9vEQUQQZ8eSpA_JdisrJGVgMRHhEtv1FO_D6lkRBbpf-G9saXapqWHzSJVvzsbgyOJeQJFRuXyyQIp_E-nsaCzWHfKO9A5nMqL_bwlBp6xsQtpR7s1IIOYGfnos5lHMPh2avoZPpP-ynCO7ELUI8bmGPk9a_8SNqtXfkYUfz4OvE7hdt3WZY4OPrKm8-QiWYXs76K4x7et4biNKq8GiJa00LUUMjRWN9uJ7HitQ0NugYk_ynT2FQBuCbZzZfRZUH3cbPEhLr3hyEbpIYzXi9AGkoTwGQR7ay6Jlo0PnaKDVLJnvPhts1a-PWHKa2sgZTc9nWqXzQPWWVoGwk1Yr1mrtrJczG8INwg56JCeF10XqRae3NiOE_dUV-OxUcMv4zbwr-fy3zJfqeoMK985ArdzjsAUn4K2bkJaC3wTOr8pURJ2XSPg73KYiV7Ms79gEFkgQuHX-VW2Tw5jp7C04vMiwvVOMwWk0OcM5vgkHx1og6i_s5HIYKEJ3Sy-6Gto" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b68653419.mp4?token=OL3eib1OUheByO0p57fr6G0mHVCfEvQq_iVlk7uRsdC-374324i0j3Rmg911eb6zb-FPZKX7pkWxebEz2KKc8MbKgvDi0roc0IHsIa_vBK70MyZ5OI8RvyDONxabQ0zuHrWO6w8Yut_MUiMTwy7JglzabmAlHfBw_wGfOcxNNXwvt9vEQUQQZ8eSpA_JdisrJGVgMRHhEtv1FO_D6lkRBbpf-G9saXapqWHzSJVvzsbgyOJeQJFRuXyyQIp_E-nsaCzWHfKO9A5nMqL_bwlBp6xsQtpR7s1IIOYGfnos5lHMPh2avoZPpP-ynCO7ELUI8bmGPk9a_8SNqtXfkYUfz4OvE7hdt3WZY4OPrKm8-QiWYXs76K4x7et4biNKq8GiJa00LUUMjRWN9uJ7HitQ0NugYk_ynT2FQBuCbZzZfRZUH3cbPEhLr3hyEbpIYzXi9AGkoTwGQR7ay6Jlo0PnaKDVLJnvPhts1a-PWHKa2sgZTc9nWqXzQPWWVoGwk1Yr1mrtrJczG8INwg56JCeF10XqRae3NiOE_dUV-OxUcMv4zbwr-fy3zJfqeoMK985ArdzjsAUn4K2bkJaC3wTOr8pURJ2XSPg73KYiV7Ms79gEFkgQuHX-VW2Tw5jp7C04vMiwvVOMwWk0OcM5vgkHx1og6i_s5HIYKEJ3Sy-6Gto" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بلاتکلیفی ۲۳ سالهٔ زمین ۴۲ هکتاریِ قزوین که قرار بود گلخانه شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/466228" target="_blank">📅 14:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466227">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6db14e940f.mp4?token=VuHEmxpjoMr7Pgd604xGDx58ZyF4i87DMmaMYVEYStFhkO7Y1ij2jgocGRhYv7SslZ6NlZd03eN2NhmNhiSYrgFXEnvk4Xx0TPZTXP4S8xFTnlHIWpZJL5lC_rRTk67QCGjhzW-EGGIeUAh8H--E1IEAzWshNttxvkLbPR8mmGVmn7Ao_S4h_PRyPLqvpLFv6NXeCOWzRJJ2l7li9l2ARP-8dxSLIZjKPIO0mwpNCHg6j1158HcItEgmeAFeLdWb7XRfxU7fyYaZoP92IxGmb9flODOAnTdXyAb_znswpfBuXijLGQsGPkIgZwL23AZSHcNeA-NngCbcnKmeYeaZYbrpCPXI-vPS5WjWATRdLma_ifzXVdyWHQNqJT7xKL-e0MeB17OhgtlJy2whDjKx7_fKUeDZsOfEBfh5Oa_G1pFDGnucWGjksaiw54yXHb1LKdr-vUUybSjhnZZpuqhKln84MawdbRhleSvQUbUmdx42BHzfS6nLc62Dcff99oTJrtRnLiGyxNIvW7Edj5Lj40CTBdqSDa4L--KHoSFoZhH3Rek2jsJ7dBYEccvSXKpzZuMXjbD3YQS4cunrIm2l2Tm0HqS4sUo_bF8618ZFKs-tifcQkdj6AdmuuqP7da5t_hnIVxC95LWD2kW_sRHhRYlm-vZInCn_xYMqx8jRCiY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6db14e940f.mp4?token=VuHEmxpjoMr7Pgd604xGDx58ZyF4i87DMmaMYVEYStFhkO7Y1ij2jgocGRhYv7SslZ6NlZd03eN2NhmNhiSYrgFXEnvk4Xx0TPZTXP4S8xFTnlHIWpZJL5lC_rRTk67QCGjhzW-EGGIeUAh8H--E1IEAzWshNttxvkLbPR8mmGVmn7Ao_S4h_PRyPLqvpLFv6NXeCOWzRJJ2l7li9l2ARP-8dxSLIZjKPIO0mwpNCHg6j1158HcItEgmeAFeLdWb7XRfxU7fyYaZoP92IxGmb9flODOAnTdXyAb_znswpfBuXijLGQsGPkIgZwL23AZSHcNeA-NngCbcnKmeYeaZYbrpCPXI-vPS5WjWATRdLma_ifzXVdyWHQNqJT7xKL-e0MeB17OhgtlJy2whDjKx7_fKUeDZsOfEBfh5Oa_G1pFDGnucWGjksaiw54yXHb1LKdr-vUUybSjhnZZpuqhKln84MawdbRhleSvQUbUmdx42BHzfS6nLc62Dcff99oTJrtRnLiGyxNIvW7Edj5Lj40CTBdqSDa4L--KHoSFoZhH3Rek2jsJ7dBYEccvSXKpzZuMXjbD3YQS4cunrIm2l2Tm0HqS4sUo_bF8618ZFKs-tifcQkdj6AdmuuqP7da5t_hnIVxC95LWD2kW_sRHhRYlm-vZInCn_xYMqx8jRCiY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارتش: در این جنگ به این نتیجه رسیدیم که حتما باید برد موشک‌هایمان‌ را ارتقا دهیم و الان به این سمت رفته‌ایم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/466227" target="_blank">📅 13:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466226">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r50GDXim11TiI3OxnPOT3deHopxueCznwpnMDDNfh2ES_sKKIIh7sYBT7iSkDHB2btg4Erq1CmcU-Vck6SVZReEYH_i68dXqdzzXiy2Ejr80G1VT_BfEwco_LioCOktSFDrYCdIa0nAnsO0wjWTVGYujRNpDxF3BSGqXn-n4hTq0dHKMhxIWbWhgfqHfZX4pclgVmfAkXKkjl3PWi0T7EY429G3yZlliX-8nQa6Qm93SJWgF580dy2vlRoh7KBc3vDBFmiXVt0j_gqKhQatUZrpihRxlYWfepMdKIxa7pnspLyo6DRJWBqbE3-AaP1dmj7U-zYt4u-JkioTglWg_xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس کمی ریزش کرد
🔹
شاخص کل بورس در پایان معاملات امروز با کاهش ۵ هزار واحدی به ۷ میلیون ۷۸۳ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/466226" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466225">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3g9tUHf8yNpqpvjNtf-tVQ1iWIfE899PVKekGDmPbi2uvPOtkiL2nJQUDFjLVz5P-jAR9n0EuZ4k6fKW44417TIFAd87tlu9yi8qCrQjHqIs1MJYOzxp-ih1IbI2npTlEHq-LMzt3Ue3UP7UAmbfn0A6-ZRZOrmA1ki_mnzNQPhrbfbe6NB51rEz2Oizvs0pzAM_0RjtK7ijE6gtKA87nz3erT8C6359WAt4Fm3VZ9FEZz_ekf9YREwU3zzynxjf1m5JnKAbW64jGC4afeQxWasOnxZNGzocDAGm5eNvTk4__uKCaCG_rtxzST92zGWs3dJ6i0MHMv7ZoD2dV30dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی هکرها به اطلاعات ۵۰۰ افسر اطلاعاتی عربستان
🔹
گروه «دفاع سایبری انصارالله» و گروه هکری «اویس قرنی»: به اطلاعات مرتبط با حدود ۵۰۰ نفر از کارکنان و افسران سرویس اطلاعاتی عربستان سعودی دسترسی پیدا کردیم.
🔹
برخی از این افسران طی ماه‌های گذشته با سرویس اطلاعاتی اسرائیل (موساد) و طرف‌های اماراتی همکاری داشته‌اند و رفت‌وآمدهای آنان با برخی فعالیت‌های محرمانه در منطقه مرتبط بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/466225" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466224">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3ca67e9ee.mp4?token=M8DzgSHMyQFVlVa7YxKKfnsje8bGga-Svrvc3pxPTwa_2bPATOnCwC2hFWYbQfa1gGxebrhSxtr93pyTbtQ9aOlG5eq195F6taNXketClgir7--p-bcy5GDCY1bSicO7Tom0noUuPqOU17gHPd7HYPTrTaGQO2kS1UP0kj0Fyt4taK8El5BF9f3RhIEHTEpcIufaWW3-d1H1QiDToI1zPvhEUVxjbE_7YZIWHn_vnZGFoT76HH5y-z4bV2MT6TyCyU_Ua84ecsIXdXjlBxwy5PxzWnrRmpUU2k6w6b9HsJl93-pTFJpe3Cj9JKIQLVCNBgFBGTi0YDatvZ_Fl-C45w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3ca67e9ee.mp4?token=M8DzgSHMyQFVlVa7YxKKfnsje8bGga-Svrvc3pxPTwa_2bPATOnCwC2hFWYbQfa1gGxebrhSxtr93pyTbtQ9aOlG5eq195F6taNXketClgir7--p-bcy5GDCY1bSicO7Tom0noUuPqOU17gHPd7HYPTrTaGQO2kS1UP0kj0Fyt4taK8El5BF9f3RhIEHTEpcIufaWW3-d1H1QiDToI1zPvhEUVxjbE_7YZIWHn_vnZGFoT76HH5y-z4bV2MT6TyCyU_Ua84ecsIXdXjlBxwy5PxzWnrRmpUU2k6w6b9HsJl93-pTFJpe3Cj9JKIQLVCNBgFBGTi0YDatvZ_Fl-C45w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس بسیج اساتید: شرط التزام به ولایت فقیه را از آیین‌نامۀ جذب اساتید حذف کرده‌اند
🔹
پیشوایی: شرط التزام به ولایت فقیه، شرط مربوط به حضور در اغتشاشات و ملاحظات اخلاقی درباره اشتغال افراد دارای فساد، از آیین‌نامه جدید حذف شده است.
🔹
آیین‌نامۀ جدید هنوز به…</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/466224" target="_blank">📅 12:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466223">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
رئیس بسیج اساتید: شرط التزام به ولایت فقیه را از آیین‌نامۀ جذب اساتید حذف کرده‌اند
🔹
پیشوایی: شرط التزام به ولایت فقیه، شرط مربوط به حضور در اغتشاشات و ملاحظات اخلاقی درباره اشتغال افراد دارای فساد، از آیین‌نامه جدید حذف شده است.
🔹
آیین‌نامۀ جدید هنوز به تأیید شورای‌عالی انقلاب فرهنگی نرسیده؛ یک ویرایش در مجموعۀ وزارت علوم تهیه شده که اشکالات متعددی دارد و با بسیاری از قوانین بالادستی در تضاد است.
🔹
ما نسبت به این موضوع انتقاد داریم و معتقدیم این کار با بی‌تدبیری انجام شده و باید در اسرع وقت اصلاح شود.
@Farspolitics_
link</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/466223" target="_blank">📅 12:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466222">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfc678926d.mp4?token=B2ry7V37kW5YteZlGSHFK8-Fa86bVQGkgkuNG-XoGx3SdI2kY8zO7TmjB2dup5RA4D13_NTT6e2pYUq9FRVGwvpa6WX6QjITtsIOVssbw28QC1KAmHcA5pzzVo5bpdXiIwns5n70_nOfYTI3lST6Nij9KHn_b1rT7KKi--VT2tLtyIql4SPOGKsXDTk-gll4bKJcFJfJ4NKFcizmBirYaaL5sRXmcNtcZSXCMce_FHDFk468OGYiHnAy0Q35wbRwxhX3-5GMvmJWDu9bPnliQqJk3yBArKKTrqnDq633_0eMPaEXgnH44x42Md2gHRPJrmalZMn__CAk_5ySg3Yf2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfc678926d.mp4?token=B2ry7V37kW5YteZlGSHFK8-Fa86bVQGkgkuNG-XoGx3SdI2kY8zO7TmjB2dup5RA4D13_NTT6e2pYUq9FRVGwvpa6WX6QjITtsIOVssbw28QC1KAmHcA5pzzVo5bpdXiIwns5n70_nOfYTI3lST6Nij9KHn_b1rT7KKi--VT2tLtyIql4SPOGKsXDTk-gll4bKJcFJfJ4NKFcizmBirYaaL5sRXmcNtcZSXCMce_FHDFk468OGYiHnAy0Q35wbRwxhX3-5GMvmJWDu9bPnliQqJk3yBArKKTrqnDq633_0eMPaEXgnH44x42Md2gHRPJrmalZMn__CAk_5ySg3Yf2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: امیدوارم خبر اعزام ۴۰ هزار نیرو از سوی پاکستان به عربستان برای جنگ با مردم یمن شایعه باشد.
🔹
زیرا هم ما و هم کشورهای منطقه می‌دانیم که هر مداخله جدیدی در تحولات مرتبط با یمن، صرفا باعث پیچیده‌تر شدن اوضاع می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/466222" target="_blank">📅 12:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466221">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc651cc526.mp4?token=gbrjVOzW_cUVIS5JtPTa-JKnd59pgXxSdfzuETOr_M8yQkDTtrO0LSLiZI7EIqq4BN1PY65hZya_nZIvBXilkIcxsZHb2z2SA32lNzeG3Q57grn05cnORZF088TFpsolxgvVgdZIJM8rZWM2CdDY9lyMye5Fhvj0kC4Y_yN2zC7RvsS6HmghKtG3kUaRPzeNyLxR_Piuh_8coDMsHx8hblVsj7oog8vz-snl2u0Xznj5hqB9-eP45fmEv0hDiwKc9p0hqtDwM6ACmjGosEmAIYx5Wl0SHV6vnTDoE7oQO5XSqRGfYyeEd3WevayXECWi9RAXN1zp6u_tqTq4v5RTnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc651cc526.mp4?token=gbrjVOzW_cUVIS5JtPTa-JKnd59pgXxSdfzuETOr_M8yQkDTtrO0LSLiZI7EIqq4BN1PY65hZya_nZIvBXilkIcxsZHb2z2SA32lNzeG3Q57grn05cnORZF088TFpsolxgvVgdZIJM8rZWM2CdDY9lyMye5Fhvj0kC4Y_yN2zC7RvsS6HmghKtG3kUaRPzeNyLxR_Piuh_8coDMsHx8hblVsj7oog8vz-snl2u0Xznj5hqB9-eP45fmEv0hDiwKc9p0hqtDwM6ACmjGosEmAIYx5Wl0SHV6vnTDoE7oQO5XSqRGfYyeEd3WevayXECWi9RAXN1zp6u_tqTq4v5RTnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: توقف بمباران و رفع محاصره تنها راهکار حل بحران یمن است.
🔹
موضع ایران دربارهٔ بحران یمن کاملاً شفاف و استوار است؛ تداوم بمباران‌ها و تشدید محاصره اقتصادی ظالمانه علیه ملت مظلوم یمن هرگز راه به جایی نخواهد برد.  @Farsna</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/466221" target="_blank">📅 12:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466220">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3503b34580.mp4?token=ep_ndicV65Oa28xskwiQCgY-HetrFqZfRLwm1VLDI2sZbXJd77zVdqzkLRGTUg1mpc78zgwuE2Ljs3AyslUtpBMWxctEcCgIy5XcNh2dIE5g7efXX7JmCwxjByVtMV1WWu6CwznI8tc9Le1LnCzOiyohUygsWFk0_aQS4g5HnVXOd_pjRiKBJaRaI2VoNHcGBN1ZdDP9rU6fZcapGjR07rNmVSUoPooofgE384gQkjJiIgPqBgKZGdgnwMpK4vI9jJdveUQYLStsRK53qy0JPEJo-ON_RMFfrYOxpGSIENiE_r300ZCGVaYYIHl66THqeR87II8yOGcRwkBxy0-PLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3503b34580.mp4?token=ep_ndicV65Oa28xskwiQCgY-HetrFqZfRLwm1VLDI2sZbXJd77zVdqzkLRGTUg1mpc78zgwuE2Ljs3AyslUtpBMWxctEcCgIy5XcNh2dIE5g7efXX7JmCwxjByVtMV1WWu6CwznI8tc9Le1LnCzOiyohUygsWFk0_aQS4g5HnVXOd_pjRiKBJaRaI2VoNHcGBN1ZdDP9rU6fZcapGjR07rNmVSUoPooofgE384gQkjJiIgPqBgKZGdgnwMpK4vI9jJdveUQYLStsRK53qy0JPEJo-ON_RMFfrYOxpGSIENiE_r300ZCGVaYYIHl66THqeR87II8yOGcRwkBxy0-PLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: ازسرگیری پروازهای عراق ناکامی سیاست انزواسازی ایران را اثبات کرد.
🔹
اقدام غیرقانونی آمریکا در تسری بین‌المللی قوانین داخلی خود، نقض آشکار مقررات حقوق بین‌الملل و اخلال در اصل حسن همجواری و روابط دوستانه منطقه‌ای است.
🔹
دستگاه دیپلماسی…</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/466220" target="_blank">📅 12:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466219">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/743ca75329.mp4?token=YNhxHoZ79q2YDBfgLR-2BwOTtD-iu5vqa7jxJfO3JQIweLCSSji4Man9LYux5PkNTOvPbMFnzWkiRg59f85-ZIXgM-y6JzGhM0Lg9FZEQJfSU-sLJhSmVoL7UervMA2bduS9yF25vHQITweO9wkKwJq93zj6V-UeYDvTKyxLQtJDZxIgZBzWqO7mHRPCsyf-B5BeCP1FT1_b0tpO2sj_I4aOtJsSqqjmZChpIG0hnUXCG-WWcejoc6eLrQYBiFLKKUYgsmRd0ZPaYrwUPe_rFPTQ4AFipjf9I770HEn-yPjoc9hOEpiUMU_TK3J6FOQAfuvTF5PVZtoKJ8-RzXxG9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/743ca75329.mp4?token=YNhxHoZ79q2YDBfgLR-2BwOTtD-iu5vqa7jxJfO3JQIweLCSSji4Man9LYux5PkNTOvPbMFnzWkiRg59f85-ZIXgM-y6JzGhM0Lg9FZEQJfSU-sLJhSmVoL7UervMA2bduS9yF25vHQITweO9wkKwJq93zj6V-UeYDvTKyxLQtJDZxIgZBzWqO7mHRPCsyf-B5BeCP1FT1_b0tpO2sj_I4aOtJsSqqjmZChpIG0hnUXCG-WWcejoc6eLrQYBiFLKKUYgsmRd0ZPaYrwUPe_rFPTQ4AFipjf9I770HEn-yPjoc9hOEpiUMU_TK3J6FOQAfuvTF5PVZtoKJ8-RzXxG9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: پاسخ آینده ایران به هرگونه تعرض از مبدأ منطقه کاملاً متفاوت خواهد بود.
🔹
ایران با صدور هشدار قاطع به برخی کشورهای منطقه، خواستار تجدیدنظر فوری در گذاردن امکانات و قلمرو خود در اختیار جبههٔ آمریکایی-صهیونیستی برای تعرض به خاک ایران شده…</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/466219" target="_blank">📅 12:23 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466218">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91dd73c84d.mp4?token=gZiDL4mMttj5vhoOaAbGZk9ofmTTitk1FG8kHio0MRFEqqIPUFJXRfBOxMfhsKGZwXa2sGw6IixRxiqzNPSnpsCWUWcGCc47y69pcZkwexWHOdEzj2qcCea6mH0BCJEWl_os8J_x_LS0BDDcgVJCfmF3Vjlq-Nfi-qy428wQap30nc-LBFuGXYhzFs3bpHYavPKc65wbbLXTbMmBEK3a_GuWJzjkjDgEQLixSZeUpwPgg1HV6-ju285I82m-6IfdgsVCpZ3HmnDFCwrRVmzqTKaDsLxSSzH9aLKEH2lYwaoVUKnGIoiSopnGMWGgay_l-WqADFowwPqy7wOuuk06jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91dd73c84d.mp4?token=gZiDL4mMttj5vhoOaAbGZk9ofmTTitk1FG8kHio0MRFEqqIPUFJXRfBOxMfhsKGZwXa2sGw6IixRxiqzNPSnpsCWUWcGCc47y69pcZkwexWHOdEzj2qcCea6mH0BCJEWl_os8J_x_LS0BDDcgVJCfmF3Vjlq-Nfi-qy428wQap30nc-LBFuGXYhzFs3bpHYavPKc65wbbLXTbMmBEK3a_GuWJzjkjDgEQLixSZeUpwPgg1HV6-ju285I82m-6IfdgsVCpZ3HmnDFCwrRVmzqTKaDsLxSSzH9aLKEH2lYwaoVUKnGIoiSopnGMWGgay_l-WqADFowwPqy7wOuuk06jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: ایران از حقوق هسته‌ای و اقتدار ملی عقب‌نشینی نمی‌کند.
🔹
تداوم عضویت ایران در NPT از سال ۱۹۷۰ و پایبندی کامل به تعهدات بین‌المللی، متأسفانه با بدعهدی، تعرضات نظامی جبهه استکبار، ترور دانشمندان و حمله به تأسیسات صلح‌آمیز هسته‌ای مواجه شده…</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/466218" target="_blank">📅 12:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466217">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3178e27c.mp4?token=cCJ9awHZ_hwOVYuNuSt130R82oYvHcJSPqttwUyaljX0HPDQaRzkcn7RGkQY-ItkUKxGXLgOmFxO_mNTdxYgKxW15zGdmrwThfOnP-crDjCSJEGZEwQWng_LCtd6cNj5E-znkSOi4HXGq8ru-VP4mp4Uz-W87auM5oYkkvLWAJdjASh4KDWnjgLOTUbxFqP5Xic4beSY6MLnxVBmJ8TQEJ-u0kqCNCe_Tog5S9IJd7pUUsTRY7eCkxyPqQ2cgEVQe2oTBaPzi4gva9JpdxVPExS-zKEuBcph1NajuAZ_Ish0S1cmw_acKPIZnZXibXD128I295xdOTjVuzl3UpyHLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3178e27c.mp4?token=cCJ9awHZ_hwOVYuNuSt130R82oYvHcJSPqttwUyaljX0HPDQaRzkcn7RGkQY-ItkUKxGXLgOmFxO_mNTdxYgKxW15zGdmrwThfOnP-crDjCSJEGZEwQWng_LCtd6cNj5E-znkSOi4HXGq8ru-VP4mp4Uz-W87auM5oYkkvLWAJdjASh4KDWnjgLOTUbxFqP5Xic4beSY6MLnxVBmJ8TQEJ-u0kqCNCe_Tog5S9IJd7pUUsTRY7eCkxyPqQ2cgEVQe2oTBaPzi4gva9JpdxVPExS-zKEuBcph1NajuAZ_Ish0S1cmw_acKPIZnZXibXD128I295xdOTjVuzl3UpyHLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: خروج متجاوزان، شکست ۲۳ سالهٔ اشغالگری آمریکا در عراق را رقم می‌زند.
🔹
پایان اشغالگری آمریکا در عراق و گام‌های عملی در جهت خروج کامل متجاوزان، رویدادی مبارک در راستای تحکیم سیادت، حاکمیت ملی و استقلال این کشور و اثبات دیگری بر شکست تاریخی…</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/466217" target="_blank">📅 12:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466216">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60d534aef2.mp4?token=P4Ys4jgZZYLKubx3R8AwrZwGetvFhkvka6gT_5eYc5jY_Li0NDrY4RS09QitdYrdNQz0MauYXE_QH6syyBDrLmgHt2dz6yQhVGzOdYcT-Y0hcTrY4g3LbUhL_eNrUn9GOZFmtTWSteWj-ABDR-Rtx9yF3ekRKMygPWJQgCQf07hJ_Rog-LgVzAsVBfQb5Quv5Q6D4LyDEw5fTBHMVB6j7FSPEyCI9KLvGJrIa8XdVYTXNkZPZjYVw2iDxku4BXDrtYEJsGRstdlhZtnMBrfl3DDH2GwXBfsF_Zeva7BNMQZuW9agQhTHAibWdeRf3K2KqteN2yuUY-tApkT2ABAsJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60d534aef2.mp4?token=P4Ys4jgZZYLKubx3R8AwrZwGetvFhkvka6gT_5eYc5jY_Li0NDrY4RS09QitdYrdNQz0MauYXE_QH6syyBDrLmgHt2dz6yQhVGzOdYcT-Y0hcTrY4g3LbUhL_eNrUn9GOZFmtTWSteWj-ABDR-Rtx9yF3ekRKMygPWJQgCQf07hJ_Rog-LgVzAsVBfQb5Quv5Q6D4LyDEw5fTBHMVB6j7FSPEyCI9KLvGJrIa8XdVYTXNkZPZjYVw2iDxku4BXDrtYEJsGRstdlhZtnMBrfl3DDH2GwXBfsF_Zeva7BNMQZuW9agQhTHAibWdeRf3K2KqteN2yuUY-tApkT2ABAsJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کتیبۀ جدید تصویر رهبر شهید در ایوان ساعت حرم امام رضا(ع) نصب شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/466216" target="_blank">📅 12:11 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466215">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08444f99d1.mp4?token=hl4RixdFqFh9fiUSoC2DIRkVNk54jsptPieraEueHwJIJpa7ENelwNjHVKcvtXMEA_m3gdqdx--X5m4C-1HgjXBR0r7xa9mdjINoxvsbiMA-zhqmmkzFsDZSWvE2yNDt0CzpLBByA_Awt6HmLOXe_zD2z5ouP_H7oBWEWNOfzKvs4t1hryw-S2O0VYZMaPSvp56D0W2FSn_1KAmBaCdb5Fo-xxFNZ3NTpmyeYi3Kh-ViXcPo7AyfPZXppgofoSCThH2xmK5EEQHYmniTFbQM7R2CkiCyRtLR5RA1KSevGWft00yxj8-JwovrIWDe-PA6Vr1I-1Lx3uSeRi2axJB65g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08444f99d1.mp4?token=hl4RixdFqFh9fiUSoC2DIRkVNk54jsptPieraEueHwJIJpa7ENelwNjHVKcvtXMEA_m3gdqdx--X5m4C-1HgjXBR0r7xa9mdjINoxvsbiMA-zhqmmkzFsDZSWvE2yNDt0CzpLBByA_Awt6HmLOXe_zD2z5ouP_H7oBWEWNOfzKvs4t1hryw-S2O0VYZMaPSvp56D0W2FSn_1KAmBaCdb5Fo-xxFNZ3NTpmyeYi3Kh-ViXcPo7AyfPZXppgofoSCThH2xmK5EEQHYmniTFbQM7R2CkiCyRtLR5RA1KSevGWft00yxj8-JwovrIWDe-PA6Vr1I-1Lx3uSeRi2axJB65g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: حضور رئیس‌جمهور در ترکمنستان دیپلماسی منطقه‌ای ایران را فعال‌تر می‌سازد.
🔹
حضور رئیس‌جمهور ایران در شهر «آوازه» ترکمنستان جهت شرکت در دو رویداد راهبردی، جلوه دیگری از پویایی مستمر دیپلماسی منطقه‌ای و تعامل مقتدرانه با همسایگان است.  …</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/466215" target="_blank">📅 12:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466214">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fec971ed20.mp4?token=JmsdnmawGFPYVX9T7yutaFGVsdj9ZfxeiKNaqnWV68ihYvXPiiyD3OB_oo1r4MlnvqxFEwJd5lvfw21zPdbHE5popAzA_fmsled0Cz2CguUOGuB6bCOZYpmpIusc9j-xA6lHgD4GV3HI_EXUnjXbtaBMMgu0dC_8prF42pneAJU1mP41_KaXq6BRIl6rf5K3RzGxsn6Vw722g4pXqVdsrs_q1SKBcUwF6waQpKIlu6RpXNQ6DXBNRkFtAEs2NbPdhFLogcs-cj0O94aFNHJmR1pPLYtI_0mcv20x2V67i3rSme-XI1kV1V3xHhurSznC8EUUQxh02UQAYlP0L_sG1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fec971ed20.mp4?token=JmsdnmawGFPYVX9T7yutaFGVsdj9ZfxeiKNaqnWV68ihYvXPiiyD3OB_oo1r4MlnvqxFEwJd5lvfw21zPdbHE5popAzA_fmsled0Cz2CguUOGuB6bCOZYpmpIusc9j-xA6lHgD4GV3HI_EXUnjXbtaBMMgu0dC_8prF42pneAJU1mP41_KaXq6BRIl6rf5K3RzGxsn6Vw722g4pXqVdsrs_q1SKBcUwF6waQpKIlu6RpXNQ6DXBNRkFtAEs2NbPdhFLogcs-cj0O94aFNHJmR1pPLYtI_0mcv20x2V67i3rSme-XI1kV1V3xHhurSznC8EUUQxh02UQAYlP0L_sG1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار بلالی: متناسب با نیاز عملیاتی در ساخت موشک نوآوری می‌کنیم
🔹
مشاور فرمانده نیروی هوافضای سپاه: خودمان سازنده و تولیدکنندة موشک هستیم و نیازهای عملیاتی را درک می‌کنیم؛ به همین دلیل به‌دنبال نوآوری می‌رویم و محصولات مورد نیاز عملیات را تولید می‌کنیم.…</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/farsna/466214" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466213">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a8523050e.mp4?token=ihaibbdJouXO9wqEfOjzpmK9sI0xuPt3K68oXeT1Y4ODkCd2ProXI0MKp8t0aZsXfQWEFy9zbBp1sK6BI3KhIrIVeB3tPStc1KOBdJbXf5EcpBorBnZ96B_wmYHI436mobYYFpd0zDLVQNrQER13R13UFmFGUHiYLeFJQIF0vC9m39VO6FLwa9LLrsCIfSXo3xnXRRP4LoGsGRxS6soJHs0IM8XNDqvFR2Hctg3rK2oGndhd-En-kb-qpI5Dqrxc4LWanvL0pACdGsuzY9z5YFaB9BXD-sFXaOBEpbtYFqG4Gb9v_ybciSnPpQ0Ty70l-NgFcRohZMvhhNIQozmKlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a8523050e.mp4?token=ihaibbdJouXO9wqEfOjzpmK9sI0xuPt3K68oXeT1Y4ODkCd2ProXI0MKp8t0aZsXfQWEFy9zbBp1sK6BI3KhIrIVeB3tPStc1KOBdJbXf5EcpBorBnZ96B_wmYHI436mobYYFpd0zDLVQNrQER13R13UFmFGUHiYLeFJQIF0vC9m39VO6FLwa9LLrsCIfSXo3xnXRRP4LoGsGRxS6soJHs0IM8XNDqvFR2Hctg3rK2oGndhd-En-kb-qpI5Dqrxc4LWanvL0pACdGsuzY9z5YFaB9BXD-sFXaOBEpbtYFqG4Gb9v_ybciSnPpQ0Ty70l-NgFcRohZMvhhNIQozmKlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: همدستی انگلیس با در اختیار گذاشتن پایگاه نظامی جرم آشکار بین‌المللی است.
🔹
بقائی در پاسخ به خبرنگار فارس: احضار سفیر انگلیس و ابلاغ اعتراض رسمی ایران، پاسخ صریحی به فرار روبه جلوی لندن از مسئولیت بین‌المللی خویش در مشارکت با تجاوز نظامی…</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farsna/466213" target="_blank">📅 12:07 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466212">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشکده خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZHJz9GVS4Rvai0i_bP0fz6v9Idyjy0N9-G0Of9gC0c4TdIrsHwQiYAtnbm3mrXA_ozbnKEAiT4QpPvpBfxT7Wpntzw3J40bZGIG0mnVgfmOtCx3jImF4f5u-tAnhOGPDlG_FF_eNHtAMZcZSZqiM64TAuwxVQ7u3oC0OBamS3cxcNS_Qm2HdUmrasDJzmLbCplXi14nx_NxLGdx5F3qkP_NJlDeL0FSoO8VRRVzgKDPqNGVlDcVA3iPf9l_-l0mUPsaPjG8mZyFiTnVjHKgdv16NfQwgcXlp7fCw-H734-l4irCDWQDggwuOh0phvjtnMXPkfv_pig5CuwtN9IZ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔰
مهلت ثبت‌نام و انتخاب رشته در پذیرش دوره های کاردانی و کارشناسی ناپیوسته دانشکده خبرگزاری فارس مهرماه سال ۱۴۰۵ تمدید شد.
🏷
براساس اعلام سازمان سنجش آموزش کشور، مهلت ثبت‌نام و انتخاب رشته در پذیرش دوره کاردانی و کارشناسی ناپیوسته دانشگاه جامع علمی کاربردی
از امروز تا ۱۳ مهرماه تمدید شد.
📚
رشته‌های تحصیلی:
🎙
خبرنگاری
📸
عکاسی خبری
🎞
سینما‑تدوین فیلم
🤝
روابط‌عمومی
🎤
گویندگی و دوبله
ارسال  عدد ۱۴ را به شماره ۵۰۰۰۱۰۱۴
🌐
لینک سایت ثبت‌نام
🔗
futurix.ir/go/rxDxXO
☄️
☄️
این فرصت رو از دست ندهید
🎓
مرکز آموزش علمی کاربردی خبرگزاری فارس
🎓</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/farsna/466212" target="_blank">📅 12:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466211">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e0f900518.mp4?token=QsJMWC10vDVPlgy7Avn5BT8Xic39WhiD4URdbzIkvGExGQVIc087efTTxvCvMBAR5EedeR_cp-_eIby6teTNs6qUInIp4X99B5biItqueDC153H-90uFMjSPaZkDIZAUkmfHTfDRe4Gf3xiYCF2vl9DRCYTJDxdy-tRyZPDOJlo7eLYNXm2P-58cvQl7UVrTfzrUSwuyybfXty8WEnxrsJSQiQYkdv65RDMthpp2LmxxBKX1Lf68wPSui-PF8XkXzu1bPF8Iq1X-uJ2XpZy9SBSNC05kO2N6ncHIwG6srvpS8v98M87exHdTdrRM5faHby8h7eo6zH__q8m6QGnblA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e0f900518.mp4?token=QsJMWC10vDVPlgy7Avn5BT8Xic39WhiD4URdbzIkvGExGQVIc087efTTxvCvMBAR5EedeR_cp-_eIby6teTNs6qUInIp4X99B5biItqueDC153H-90uFMjSPaZkDIZAUkmfHTfDRe4Gf3xiYCF2vl9DRCYTJDxdy-tRyZPDOJlo7eLYNXm2P-58cvQl7UVrTfzrUSwuyybfXty8WEnxrsJSQiQYkdv65RDMthpp2LmxxBKX1Lf68wPSui-PF8XkXzu1bPF8Iq1X-uJ2XpZy9SBSNC05kO2N6ncHIwG6srvpS8v98M87exHdTdrRM5faHby8h7eo6zH__q8m6QGnblA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: ارتقای امنیت تنگه هرمز مستلزم لغو کامل تحریم‌های آمریکا است.
🔹
ارسال پاسخ‌های صریح و مقتدرانهٔ ایران به پیشنهادهای طرف آمریکایی از طریق میانجی قطری در دوحه، ناکامی واشنگتن در انحراف مسیر گفتگوها به سمت مباحث هسته‌ای را آشکار ساخت.
🔹
موضع…</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/466211" target="_blank">📅 12:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466210">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5992e0e99c.mp4?token=M-w0D4bT2ehUyJMd6CrdrAvwGD5H4mU9yXrcH_-vOR9zVLj9jpf16Hv7dU2b-LoHpOQJDmdTj4PeKQDhh_0tcNoyIwWCfJDO52zs8q7iWUwIZCkJmRm_VhRwfofP_zDfGb1uPbnz2q2OVzxhRCc0vOhJucBG2VuJJshovMBirxsDG58utc5SXqKvXVQH87jCdgonYwwthurcl1Nno_-A8FCr79ApR-5NrUSxqoi0jVB2WVgg8HsNec8cwXotnUamjjVM_h0rocDhKdQNJkwIKeobCIc8JHl0dAKUCtBnMkRkbFm_JaDco_RRlrMJeJgP4gwzDAL7GbJgwKdpc4MZgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5992e0e99c.mp4?token=M-w0D4bT2ehUyJMd6CrdrAvwGD5H4mU9yXrcH_-vOR9zVLj9jpf16Hv7dU2b-LoHpOQJDmdTj4PeKQDhh_0tcNoyIwWCfJDO52zs8q7iWUwIZCkJmRm_VhRwfofP_zDfGb1uPbnz2q2OVzxhRCc0vOhJucBG2VuJJshovMBirxsDG58utc5SXqKvXVQH87jCdgonYwwthurcl1Nno_-A8FCr79ApR-5NrUSxqoi0jVB2WVgg8HsNec8cwXotnUamjjVM_h0rocDhKdQNJkwIKeobCIc8JHl0dAKUCtBnMkRkbFm_JaDco_RRlrMJeJgP4gwzDAL7GbJgwKdpc4MZgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: ایران سوءتفاهم‌های دیپلماتیک با بیروت را از طریق گفت‌وگو رفع می‌کند.
🔹
علی‌رغم برخی فضاسازی‌های بیرونی، سفیر ایران پیش‌تر موافقت رسمی (آگرمان) خود را از دولت لبنان دریافت کرده و هیچ‌گونه اجماع‌‌نظری علیه روابط دیپلماتیک دو کشور در داخل…</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farsna/466210" target="_blank">📅 11:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466209">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdb119fa8a.mp4?token=NGgfJG_rTEkwvMkzuG1DW02N99NmuzpYi0SVpY8GR5AHCtXXl3BQQPVwhESFHlEfBKVrdTKvZT_ND2JxbL02GA0EkKTvhbCA3eWJBXi8I_1ZmV6AELm2t3vW0hd5AUW6Lml_9-PvbAd_ynHTXZxM5Hx8qwsBFyArIIRPCW1-tF9aAQtJgWFlH9O4zfTPzJcniry19uzCQWjGzKcHoOsc7FZ6mbkEHxxm4aWMCcsfOFXm_4jqOfhoooVvY5offYKpQQhTf-eHBsxcttXWRg074Z2rewZqul-C-JkwtHBAsos72hi4oCjq46plNgeJrK_7dX_hlnUjNeCzvNhmcWexIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdb119fa8a.mp4?token=NGgfJG_rTEkwvMkzuG1DW02N99NmuzpYi0SVpY8GR5AHCtXXl3BQQPVwhESFHlEfBKVrdTKvZT_ND2JxbL02GA0EkKTvhbCA3eWJBXi8I_1ZmV6AELm2t3vW0hd5AUW6Lml_9-PvbAd_ynHTXZxM5Hx8qwsBFyArIIRPCW1-tF9aAQtJgWFlH9O4zfTPzJcniry19uzCQWjGzKcHoOsc7FZ6mbkEHxxm4aWMCcsfOFXm_4jqOfhoooVvY5offYKpQQhTf-eHBsxcttXWRg074Z2rewZqul-C-JkwtHBAsos72hi4oCjq46plNgeJrK_7dX_hlnUjNeCzvNhmcWexIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: کمیتهٔ ۶ نفره شورای‌عالی امنیت ملی پرونده مذاکرات را هدایت می‌کند.
🔹
حضور وزیر خارجه در این کمیته عالی که مسئولیت بررسی دقیق و همه‌جانبهٔ موضوعات مرتبط را بر عهده دارد، گواهی بر هماهنگی کامل دستگاه دیپلماسی با تدابیر کلان امنیت ملی است.…</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/466209" target="_blank">📅 11:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466208">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fe5ac6185.mp4?token=i4wOH4DF6rhxI41JR3IwnbfOZSKYRmpIZuPuJl1sXRVRZBJapiyqjy_TVYPLrFqR0wxQBRsS1xCFI080oJwlMqATvrVlLKhqtOwJ7q-Ju9XYen3HctIAFAYcUVFmRRYwUYh_yCzr6L0HZyUFWrh67ILr9iJAmddtMTz-myZNh8thWhBSh6MSgmQG8_kN6nHY2BVB7vxTAMwpWk1hxzEtAn1xj39hFoZI-_bf8thphxLeyJnYH7czSg1rOkC4CNAG5e3hKrkoLFM6aHiJTGx9aRs5-CzAIP7k1sbXSWfctYdzAIQuODwmRQceWc9l5PSs7Fz9rb_UpLdk49wlBN0NuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fe5ac6185.mp4?token=i4wOH4DF6rhxI41JR3IwnbfOZSKYRmpIZuPuJl1sXRVRZBJapiyqjy_TVYPLrFqR0wxQBRsS1xCFI080oJwlMqATvrVlLKhqtOwJ7q-Ju9XYen3HctIAFAYcUVFmRRYwUYh_yCzr6L0HZyUFWrh67ILr9iJAmddtMTz-myZNh8thWhBSh6MSgmQG8_kN6nHY2BVB7vxTAMwpWk1hxzEtAn1xj39hFoZI-_bf8thphxLeyJnYH7czSg1rOkC4CNAG5e3hKrkoLFM6aHiJTGx9aRs5-CzAIP7k1sbXSWfctYdzAIQuODwmRQceWc9l5PSs7Fz9rb_UpLdk49wlBN0NuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برجک زندان رجایی‌شهر فروریخت
🔹
در ادامۀ تخریب دیوارهای زندان رجایی‌شهر البرز، برجک این زندان نیز تخریب شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/farsna/466208" target="_blank">📅 11:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466207">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wt8UiM8MrJ0oVXTZJsG94VDwVjJUWvMwAikgk99ec-89Ahmo8WC_QzOfTa1ttsAowt0f9-oGNTROpiLW_3d8kgNtAHDLqgQLNY0uKtLMKgF2T94cOcSTECeKRkaW_wiObKqwBoOAmjow3citAhS_KMN6lJISyYrb2sG3Mdjz56wwEr4DEWyDir-Uwi96mLGcYjLWYaswIKy7-PY50S3oyoCG7lHeemRJt1fbjD3eidIjZS3zOEI7lEKJk-Fjc0uUsunn7RYyTmVipano8IqG0ew4eZtAoY8AYnjdlEX9ksPhjwM6o9_kwYtG4jyqAMkOuaaHz6DVvcL4CpAlMGsttw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله: اخراج آمریکا از عراق، آغازی بر پایان حضور نظامی واشنگتن در منطقه است
🔹
حزب‌الله لبنان با انتشار بیانیه‌ای، اخراج نیروهای اشغالگر آمریکایی از خاک عراق را یک دستاورد تاریخی و پیروزی بزرگ خواند و آن را به دولت، ملت و مرجعیت این کشور تبریک گفت.
🔹
حزب‌الله…</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/farsna/466207" target="_blank">📅 11:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466206">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28abbaba6b.mp4?token=AUJM_FSTdcoK6gJeg9Acs-0NVWIHffifTgSjxGcE-ogHwyRCzhbkk9yn3frwgb42xZTwFUAgKAWsWJUmC-jd22cuX2aC0UdVcCEOOk_Las3JpEhqJRwd1LLECsRc6IxuyXQ62ewuQMplOaSA6d5kQOtHhk2CWdlxJANeH_UI1_evK94hflQ7_8dotDmWCwN2WNPvrjzINRJExr4WAjGpbxGLaVJn3Ss64EkjajXZBYmLI4vvs3rZJB7eqsDqTXu2_VafNhNdp31C-HuHDyrsY_Md-eBa4yCXD7vqonT7z1GZBegz4Swak5VUOkbtdLsLdTCMsJhgOv2sW714SlQjlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28abbaba6b.mp4?token=AUJM_FSTdcoK6gJeg9Acs-0NVWIHffifTgSjxGcE-ogHwyRCzhbkk9yn3frwgb42xZTwFUAgKAWsWJUmC-jd22cuX2aC0UdVcCEOOk_Las3JpEhqJRwd1LLECsRc6IxuyXQ62ewuQMplOaSA6d5kQOtHhk2CWdlxJANeH_UI1_evK94hflQ7_8dotDmWCwN2WNPvrjzINRJExr4WAjGpbxGLaVJn3Ss64EkjajXZBYmLI4vvs3rZJB7eqsDqTXu2_VafNhNdp31C-HuHDyrsY_Md-eBa4yCXD7vqonT7z1GZBegz4Swak5VUOkbtdLsLdTCMsJhgOv2sW714SlQjlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه در واکنش به ادعای اخراجی هیئت ایران از آمریکا: دشمن با دروغ به‌دنبال دستاوردسازی است؛ این ادعا کاملا دروغ است.
🔹
ورود و خروج ما از ابتدا اطلاع رسانی‌شده و مشخص بود؛ یکی از دیپلمات‌های ما قرار بود چند روز دیگر برای انجام وظایف در نییورک…</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/farsna/466206" target="_blank">📅 11:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466205">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81e66396ea.mp4?token=JXscxRWFiq1UTPn7cs-WeMwkZJKj1QDqNRaYVT0SyMAapKF04pPABhA-145GIDMibx7CSYD3BPU4sV8VZ2DQXPxqAF9g1Pb49-XlmTmhJK5J_6QOMQgQhhRgkgMZfLalXTFHlK784NnZCH9sxw1IrGUSyWJ0YoTM_8ov4TnPUJOLfbfRxSPumhOU3yVLyk6evjVbciaBvV7bFYxQPdAe48O70wXTi2j0XZzsaEL8aOQrwKKCTEiWZZSW_UxiQ6O16Dqqy1Y8zJC2idP5g5JYR1zV9NESJ7gWXJMOkIGO6xaakz0YrExVlvVykbOOxz8pMvZGQ9on2uJUOpi477e1HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81e66396ea.mp4?token=JXscxRWFiq1UTPn7cs-WeMwkZJKj1QDqNRaYVT0SyMAapKF04pPABhA-145GIDMibx7CSYD3BPU4sV8VZ2DQXPxqAF9g1Pb49-XlmTmhJK5J_6QOMQgQhhRgkgMZfLalXTFHlK784NnZCH9sxw1IrGUSyWJ0YoTM_8ov4TnPUJOLfbfRxSPumhOU3yVLyk6evjVbciaBvV7bFYxQPdAe48O70wXTi2j0XZzsaEL8aOQrwKKCTEiWZZSW_UxiQ6O16Dqqy1Y8zJC2idP5g5JYR1zV9NESJ7gWXJMOkIGO6xaakz0YrExVlvVykbOOxz8pMvZGQ9on2uJUOpi477e1HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: کشورهای منطقه باید مانع سوءاستفاده از قلمرو خود برای تعرض علیه ایران شوند.
🔹
در حاشیهٔ مجموع عمومی سازمان ملل با کشورهای جنوبی خلیج فارس صحبت کردیم؛ رایزنی‌های دیپلماتیک ایران در نیویورک، آزادی هم‌وطنان بازداشت‌شده در امارات را محقق…</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farsna/466205" target="_blank">📅 11:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466204">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29297c7fcf.mp4?token=CuXmDhoqf944a_T_9y-CnNwuBKpExYQWDhF8EIvjK4m4_xKGxt99P3UFPK17Fa89Ix2TaPJouw6J5W0M9NskDiD88KQQDNuQEuczt8NboQQRKW2L04E0hfvVYs3jzr0w7nZ5LKbPt8dXwdkziLixE4xVU-1wuzQqeN65k9oOkrwUJOOBku99vWIr52ulk47QR3d2qFnGkvo5az7KGmY9tEZe66igHYbMJBTEeoTMOwyaTYtxzN0aRGEooxHhRepC1MrfGfL7e5yxcQsKRxqEqle-nyb9XrWA6gUMM0rcxvNTiQv04NUhh_5NQOPmn3CPOPlV8RP7FkVrRYru0K25Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29297c7fcf.mp4?token=CuXmDhoqf944a_T_9y-CnNwuBKpExYQWDhF8EIvjK4m4_xKGxt99P3UFPK17Fa89Ix2TaPJouw6J5W0M9NskDiD88KQQDNuQEuczt8NboQQRKW2L04E0hfvVYs3jzr0w7nZ5LKbPt8dXwdkziLixE4xVU-1wuzQqeN65k9oOkrwUJOOBku99vWIr52ulk47QR3d2qFnGkvo5az7KGmY9tEZe66igHYbMJBTEeoTMOwyaTYtxzN0aRGEooxHhRepC1MrfGfL7e5yxcQsKRxqEqle-nyb9XrWA6gUMM0rcxvNTiQv04NUhh_5NQOPmn3CPOPlV8RP7FkVrRYru0K25Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مجمع عمومی سازمان ملل فرصت مهمی برای رساندن صدای منطق، اقتدار و مظلومیت ایران به دنیا بود.
🔹
یکی از موفق‌ترین حضورهای ایران در مجامع بین‌المللی را در هفتهٔ گذشته تجربه کردیم. @Farsna</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/466204" target="_blank">📅 11:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466203">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yonk55ma3BDIEaY1RXm3w3UOzMosvfrVFoEysFCfNnMu2I40tX7Y_daSwlcJSfYPH8hjEhptEFJPLk08dSdV1FM1AcK8tvUPyJMxi18cJT1IDIaowYZ3uYxN7Xf70m_uTtvn-ZUdJplG0SUZ0t41BPtWFRtVVGkhxiXv76-mGe1-Z4-nnY0DpHVrcQYGKSlNeEiH45FrjwqqiUj_th_MoAc3nlSipNWQTVWeovkCkJq50dAQTR1E3lc8x58lqzC7ihhtG92yMPX5wKavXaYByaX_cWQWt17UiG1LGukBLJMS_xJh6GW5ZmNOSczV7NquFICX22HYDUkvTgxAZw9w0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: درخصوص استیضاح وزیر کار تصمیم‌گیری می‌شود
🔹
بیگدلی، عضو کمیسیون اجتماعی مجلس خطاب به قالیباف: پس‌از اینکه استیضاح احمد میدری در کمیسیون بررسی شد، باید در نخستین جلسۀ علنی مطرح شود. از شما درخواست دارم دربارۀ ارجاع استیضاح وزیر کار تعیین‌تکلیف شود.…</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/466203" target="_blank">📅 11:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466202">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16f66a5c2d.mp4?token=om4Qd2QP6m_IX2gxQIHIPLrvZLt3cttaF6Bbdeyr04SXv7uqwtJNFRJv0n6VSXPFvVvQKfvageJ7infZyJH8f8PIjGwHN20n60yykQBqg6YJ2Nli4ZdzKRtnHAostx02eKtNrHsW1OqWsu58EE_KpGf-dciGKO4NgMo9qKdfS8V1sWZ-B6upCJbyNlcQdD6HBrwkWx7nsuSSp6yn7N6-GQTOZugp5kCRJSxHSDPbpZD_s65UXi58F52cnFLU3-UNeO9IUlSRZSImOt8XKGAHV33RC58ojd8ignhm9Nw3XV6i2ozLIVXddmn5U_LqvI3nIzuGn0zbrclpKus5jS1PFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16f66a5c2d.mp4?token=om4Qd2QP6m_IX2gxQIHIPLrvZLt3cttaF6Bbdeyr04SXv7uqwtJNFRJv0n6VSXPFvVvQKfvageJ7infZyJH8f8PIjGwHN20n60yykQBqg6YJ2Nli4ZdzKRtnHAostx02eKtNrHsW1OqWsu58EE_KpGf-dciGKO4NgMo9qKdfS8V1sWZ-B6upCJbyNlcQdD6HBrwkWx7nsuSSp6yn7N6-GQTOZugp5kCRJSxHSDPbpZD_s65UXi58F52cnFLU3-UNeO9IUlSRZSImOt8XKGAHV33RC58ojd8ignhm9Nw3XV6i2ozLIVXddmn5U_LqvI3nIzuGn0zbrclpKus5jS1PFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مجمع عمومی سازمان ملل فرصت مهمی برای رساندن صدای منطق، اقتدار و مظلومیت ایران به دنیا بود.
🔹
یکی از موفق‌ترین حضورهای ایران در مجامع بین‌المللی را در هفتهٔ گذشته تجربه کردیم.
@Farsna</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/farsna/466202" target="_blank">📅 11:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466201">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cd1rdiGoyK75U0Ct4ka9lumUm3LXfCdMZ2DGNvd7w6Mf7lw_FYC6MFqD25pgZ7HV0gO4RAJO3ybdIMVzqJQrHRCjr8IFLsODnjMmWuTu3sxntTMILYZdSsZgs-iE0Qo_ixM-u0C6u4fKRNdjM08A04SmffQZXzzpyJd-EYz9KYN1KzaZiHgWrUaqPuW0Na2jRe4UJwgMLy3t9NcdzzWxvLZlJXRiQ9Bbquq4_Fl2pglM0Yq-GNMnXRkPx95iufBs_1lJS81ywxcjSE_JImtOKDXMvSXyIiIQCtEOY3gGC_c8NEtdrYw5FYQVRZX4WEaCTVgkx8XkzQ6Jmdanf59o2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسات مجلس از هفتۀ آینده در محل دائمی صحن برگزار می‌شود
🔹
سخنگوی هیئت‌رئیسه مجلس: طبق مصوبۀ شعام از هفتۀ آینده جلسات صحن علنی با سازوکار دیگری تشکیل خواهد شد.
🔹
براساس تصمیم جدید هیئت‌رئیسه، جلسات صحن هم در محل دائمی صحن و مکمل آن به‌صورت وبینار برگزار خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/466201" target="_blank">📅 11:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466200">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01bdd591de.mp4?token=vkVXZjbrjJ-GKY6maQQRnoK50sFlWOBpmRHPYD5a3FS6iflZUqTZuqtL3PjP-Gg9wrkq3-s2v814nkPwMGp6G1O9nnpRUbZeJGrTv094ZL28dUZHYg6hzn3q2ZqpBnf7NMDHm2SF48Z_pF6-1Y2jeoZh8elV4VM_TPLm43vpJEe2Sfsk2el5mtyvKLupX8WMmSweSIlEH37FQ4jhDXTPuU-n7jpB_HJQiBSrftiffqix7EY6YrWmDMYgvPcbu3fxgnTutw7fhLu2uaegZmQqNl_xkqqJQDh4Z5S5tc-3Di8tnuOiS7fEmJIQLTDmdRvcagos_Loa2oDrwyvtiMC8JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01bdd591de.mp4?token=vkVXZjbrjJ-GKY6maQQRnoK50sFlWOBpmRHPYD5a3FS6iflZUqTZuqtL3PjP-Gg9wrkq3-s2v814nkPwMGp6G1O9nnpRUbZeJGrTv094ZL28dUZHYg6hzn3q2ZqpBnf7NMDHm2SF48Z_pF6-1Y2jeoZh8elV4VM_TPLm43vpJEe2Sfsk2el5mtyvKLupX8WMmSweSIlEH37FQ4jhDXTPuU-n7jpB_HJQiBSrftiffqix7EY6YrWmDMYgvPcbu3fxgnTutw7fhLu2uaegZmQqNl_xkqqJQDh4Z5S5tc-3Di8tnuOiS7fEmJIQLTDmdRvcagos_Loa2oDrwyvtiMC8JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیابان‌های پاریس علیه ماکرون به‌صدا درآمد
🔹
صدها نفر از معترضان فرانسوی در مرکز پاریس تجمع کردند و با سردادن شعارهایی علیه رئیس‌جمهور فرانسه، خواستار خروج کشورشان از اتحادیهٔ اروپا و ناتو و توقف حمایت نظامی از اوکراین شدند.
🔹
فیلیپو، رهبر حزب «میهن‌پرستان» فرانسه، در این تجمع گفت: «منابعی که دولت فرانسه برای اوکراین هزینه می‌کند، باید برای کاهش مالیات سوخت در داخل کشور اختصاص یابد و به مشکلات اقتصادی مردم رسیدگی شود.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farsna/466200" target="_blank">📅 11:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466199">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">۴ معبر تهران به‌نام شهیدان تنگسیری، شمخانی، موسوی و خرازی نام‌گذاری شدند
🔹
بزرگراه جدید‌الاحداث(دوگاز): به‌نام شهید عبدالرحیم موسوی
🔹
میدان نوبنیاد: به‌نام شهید شمخانی
🔹
بلوار دریا: به‌نام شهید تنگسیری
🔹
خیابان رام(پاسداران): به‌نام شهید کمال خرازی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/466199" target="_blank">📅 11:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466198">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4tXckXLwiNQHXZdiAKzY-i4sEts9UdUNNa9RrsVz1ycJxQOCxmpnUhwRGwu2uGLfQgCwkGBarBYmd2vfqcbZxmmTU-fLfQzikUJzdbLKjOYHE9xRfgOZRRjXeqHJ_GwPkXf6ueNQ1zXLSVqoS_psJoscOUUPhW_n_2vOVqSJaQ61OOR9Bs0X1tmqEk3HHcnQ1Xt-usGrVsywUgMVCROdZil6AZY6MlpcgoBICrCQWSat-BB3t5j2-xR80qdcqgUoRv9yqculgrHRYqOk8-F5cCZht6mxiMGQZAGNLvC-vKwTXfvhLktDEt84HJZUB5LZWEaPkJ-fOh-1HaFK7Z6dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی: حملات به پالایشگاه‌های روسیه را افزایش می‌دهیم
🔹
رئیس‌جمهور اوکراین: کی‌یف در واکنش به تشدید حملات روسیه به زیرساخت‌های انرژی و شهری اوکراین، حملات خود به پالایشگاه‌های نفت روسیه را افزایش خواهد داد.
🔹
سرویس‌های اطلاعاتی اوکراین اسنادی به‌دست آورده‌اند که نشان می‌دهد رئیس‌جمهور روسیه «دکترین جدیدی» برای حملات نظامی تدوین کرده است.
🔹
این سیاست جدید طیف گسترده‌تری از اهداف غیرنظامی از جمله زیرساخت‌ها، مراکز لجستیکی، جاده‌ها، مدارس و بیمارستان‌ها را دربرمی‌گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/466198" target="_blank">📅 10:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466197">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گروهی از زندانیان ایرانی در امارات آزاد شدند
🔹
گزارش‌های رسیده حاکی است در پی رایزنی‌های مستمر هیئت‌های دیپلماتیک و امنیتی ایران، گروهی از زندانیان ایرانی که سال‌ها در زندان‌های امارات به‌سر می‌بردند، آزاد شدند.
🔹
این هموطنان که تا ساعاتی دیگر از طریق مرزهای هوایی به آغوش وطن بازخواهند گشت، شامل تعدادی از بانوان ایرانی نیز هستند. پیگیری‌های حقوقی و دیپلماتیک برای استیفای حقوق این هموطنان، به‌صورت جدی دنبال می‌شود.
🔹
بنابر اعلام این هیئت دیپلماتیک و امنیتی کشورمان، رایزنی‌ها برای آزادی سایر زندانیان باقی‌مانده در امارات و بازگشت کامل آنان به کشور، با جدیت در دستور کار دستگاه‌های مسئول قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/466197" target="_blank">📅 10:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466196">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37a02c8515.mp4?token=NuVAAEucPHh64mZY-Vw7Y5B5T71cSROgmoZ1beLhCHitJwUihiB3YLfT5eUTFZL4IfFn9UvxdU3nOIMJx6Zs1_kf0QjFeVKyrS8VcnfTEHXcTHFlpFu2afk_2Qx7TI5wrqwBR7Rzc-akfG0zSHxsD412kcBaQeiNzrGA_8TsBkgCO_O5DXFGW5gbajQGwKGNTpNMOREmYjLJeKXKbXEo1SvC-cfvOR4xwv28keWmNyJ7ZHHyQSSNG4uswi60oC3jpC4hoGXJ89OOKKr0P5gJsWBK43g2mpk0JXOjom4AZEW4Z7nNhLJKeSFYIBeb2hGSbKkfnZUgUSLzFz5EPcz_9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37a02c8515.mp4?token=NuVAAEucPHh64mZY-Vw7Y5B5T71cSROgmoZ1beLhCHitJwUihiB3YLfT5eUTFZL4IfFn9UvxdU3nOIMJx6Zs1_kf0QjFeVKyrS8VcnfTEHXcTHFlpFu2afk_2Qx7TI5wrqwBR7Rzc-akfG0zSHxsD412kcBaQeiNzrGA_8TsBkgCO_O5DXFGW5gbajQGwKGNTpNMOREmYjLJeKXKbXEo1SvC-cfvOR4xwv28keWmNyJ7ZHHyQSSNG4uswi60oC3jpC4hoGXJ89OOKKr0P5gJsWBK43g2mpk0JXOjom4AZEW4Z7nNhLJKeSFYIBeb2hGSbKkfnZUgUSLzFz5EPcz_9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی در واکنش به ادعای مقامات آمریکایی مبنی‌بر اخراج هیئت ایرانی، با رد این موضوع گفت: هیئت ایرانی طبق برنامهٔ از پیش تعیین‌شدهٔ خود به آمریکا سفر کرده و بازگشته است.  @Farsna</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/466196" target="_blank">📅 10:49 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466195">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNli9aOtGKTAXTy5sxDU6V-s9AARTfO7Ar1BoAJovQ06889sHt3gcyRTR3pdaHO4AKBSogNtJu_HuiYyjilYZcJ1REQpoO1586Dd1LixZyNf5LlTzUYJz1cCFAE2a1z7At9dY4-F6I4ffOc7QiQKo2_ulhVS8rmbdijX-ZJbt0h3dM_yMdG7ZimAy9Y729PzU96W96N_TQ1wqtIQI7uXAMS6oPR05K_QHcWY1EI1UcQAIL7Wg-SXcceizPUG5hhrb4rP8FhdQxHZup6dgZxxqK7ht37OBLc7H7hWuK3mfZb7DkZNawMKDyvM4shUAdr1oY0B9gM_oVMRuHvGPcPBBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
رئیس‌دفتر رئیس‌جمهور: شایعۀ موافقت دولت با استیضاح میدری تکذیب می‌شود
🔹
در فضای مجلس شایع شده که دولت با استیضاح وزیر کار موافق است و خود دولت این را گفته.
🔹
شأن دولت قطعا این نیست. رئیس‌جمهور از همۀ وزرا با تمام وجود حمایت می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farsna/466195" target="_blank">📅 10:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466194">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6aNlvLBUTBE6eugqmO5wmIC0T_FYm3OVGSRgjJscw_5VQgcaHCBouVv6crBd8LaGQ55SJAS306uwwIYK6qI6uTCE1AVEFPmk_b77CjyUdlg9zc0pSYI3owUp6sCpmmRvCtgz9-OJ9m4Tk3KcfQlpL0jtLpo6xhhmUa4ytyMhjmXiA3A4Q6s6TV8qAlNuouR_JvIZbLCCInlFfdwERO1s952ZnroBZDaf1pkZq7Md3F0o5pa00c7uybRqLrjTKzvWz8WtzKG2gwOalQL2t6PsTSPJEzf6e17kM5bHb_OE0GgLnF9NZV2Z075iOPtWxo8mMxHQrzXNqO9rFHWy-RM_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت هواپیمایی عراق: پروازها به ایران از ماه اکتبر (۹ مهر) با مبدا نجف آغاز می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/466194" target="_blank">📅 10:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466193">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">انهدام کنترل‌شدهٔ مهمات در پاکدشت
🔹
سپاه استان تهران: تا ساعت ۱۶ امروز عملیات انهدام مهمات عمل‌نکردهٔ دشمن در پاکدشت انجام می‌شود؛ احتمال شنیدن صدای انفجار ناشی از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/466193" target="_blank">📅 10:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466192">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0194d01ade.mp4?token=dagGSQQ7DBflFzICGjEzoj0G11AKhy1t8-l3xLs65sEVXOiBtIICdDCRgGur8ZAY7qmYE1ez4UXQTqAOBUpVrDcPjq9EixTyt7_7rnBYnraP145MTVJcWwDg8U5Dn-u33H_Xgl-mdBT0m-7ISApSla8pftVrgAoDZJw_9CHKZOQVfP-LoXjVjys4SlsG_TCzm02KBFjdHM8V_mIOTLk9FBh2-XPSC40GK4hiy0BxMTQ2xOI0N6RLCjdshf5uaCpJ5M77z8iWQ1nEt585QIaF_nM96tzbLBccOIGpap34SBYRcOQlrmrTXeAWPivgTcoVGTRWLr1mwD_LjN03RfLQXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0194d01ade.mp4?token=dagGSQQ7DBflFzICGjEzoj0G11AKhy1t8-l3xLs65sEVXOiBtIICdDCRgGur8ZAY7qmYE1ez4UXQTqAOBUpVrDcPjq9EixTyt7_7rnBYnraP145MTVJcWwDg8U5Dn-u33H_Xgl-mdBT0m-7ISApSla8pftVrgAoDZJw_9CHKZOQVfP-LoXjVjys4SlsG_TCzm02KBFjdHM8V_mIOTLk9FBh2-XPSC40GK4hiy0BxMTQ2xOI0N6RLCjdshf5uaCpJ5M77z8iWQ1nEt585QIaF_nM96tzbLBccOIGpap34SBYRcOQlrmrTXeAWPivgTcoVGTRWLr1mwD_LjN03RfLQXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی: دشمنان اگر برخورد نظامی را در پیش بگیرند پاسخی محکم می‌گیرند
🔹
وزیر خارجه در نشستی با سفرا و رؤسای نمایندگی‌های خارجی مقیم تهران: ایران در راستای دیپلماسی و پیدا کردن راه‌حل دیپلماتیک جدی است؛ همانطور که در دفاع از خود جدی است.
🔹
شرط‌های خود را برای…</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/466192" target="_blank">📅 10:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466191">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0wo30Ad4qltLQKDQUIR2y45yo5yFIb0aScCrhQ2Ewvw2eWb5wxgE6ldvYG8jr6eDnUvAlrZNUG-3ST3dBPsd9O4mbqccPTpHvRFIlXVo5a84D_OtdA2i9b8uwqKdxQtgDmF_Xs5XyJn8pYPjIIHYZKIsZapzNMglgN9lOCNdk1fZeC-ErDPPgEPyJeOHTg8CBwoh_FQh4NXHmMamenHm7I7C26ZA_dVZv1cUfy4jELOzCnuhEEGQTFYz2BdM0U36jTwpvsUNYm7WsI2lKj5gLDllQy5NgunPQTkqLSf_62UPfm9ArdujRGPfqbMHcb5TDmVgSQSPkhnUp2GMwpr0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: دشمنان اگر برخورد نظامی را در پیش بگیرند پاسخی محکم می‌گیرند
🔹
وزیر خارجه در نشستی با سفرا و رؤسای نمایندگی‌های خارجی مقیم تهران: ایران در راستای دیپلماسی و پیدا کردن راه‌حل دیپلماتیک جدی است؛ همانطور که در دفاع از خود جدی است.
🔹
شرط‌های خود را برای بازگشایی تنگهٔ هرمز به وضوح برای همه توضیح دادیم؛ همهٔ این شروط منطبق با تعهداتی است که آمریکا باید بپذیرد.
🔹
اگر طرح ۷ روزه که به آمریکا ارائه شده است مورد پذیرش واقع شود، تنگهٔ هرمز مجددا بازگشایی خواهد شد.
🔹
اگر دشمنان ما مسیر برخورد نظامی را بخواهند مجددا در پیش بگیرند پاسخی محکم‌تر از گذشته خواهند گرفت و قوی‌تر از گذشته از خود دفاع خواهیم کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/466191" target="_blank">📅 10:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466190">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHWga-2nMTdq10eFwis7_w2L9Xm0QfDwHosJ1UXtlMZ1BGZwT59NgXohLK2pVDXXgltFX1Qw3H9LAf6MzJYkQkFgkGnQ2p4DzfutSL1mxtk-CSL33-Jas3ANzwckiUOKfTFp2LOZAbztzZYeCUWF6YXdatKd07HcN6XQF4hPqpxknFMw0eq_tlafeIVX6hGIpTumdOcr5QqHFHM5j90ZH12zgmLTHMDNZftBJyjd6Qz54E98v6fQSqtHu0r7Sz9-quHgjFk6kmIrFxZDXw6oL_qJhTyo_SJTxK6pzHOQQqaIvZHK72SGkvJFZmsSHyzOQ74ppMKkPEufLDEHxFgejg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی شهرداری تهران: اقلام دیگری مثل مرغ، رب و پنیر به طرح «تورم صفر» اضافه خواهد شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/466190" target="_blank">📅 10:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466189">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترک فعل بانک‌مرکزی به دادسرا ارجاع شد
🔹
دیوان محاسبات کشور: طبق آخرین ماندۀ اعلامی، معادل ۷.۹ میلیارد دلار از عواید ارزی حاصل از صادرات در حساب‌های کارگزاری، تراستی و پوششی مرتبط با ۱۸ بانک عامل در داخل کشور بوده است.
🔹
تأخیر در دسترسی به این وجوه باعث شده حدود ۸۵ درصد حجم معاملات مرکز مبادله، از ابتدای تأسیس تا مرداد امسال، با تأخیر زمانی بین بانک‌ها کارسازی مالی شود.
🔹
یافته‌های دیوان محاسبات حاکی از ضعف در سازوکارهای رهگیری و نظارت بانک مرکزی بر جریان منابع ارزی است. ترک فعل بانک مرکزی در این خصوص به دادسرا ارسال شده.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/466189" target="_blank">📅 10:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466188">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کشف ۹۲ تن برنج احتکارشده در جنوب تهران
🔹
رئیس پلیس امنیت اقتصادی تهران: ۹۲ تن برنج احتکارشده در شهرری کشف شد. در ۴ ماه اخیر ۵۹۶۵ تن انواع کالای اساسی از جمله برنج و روغن و قندوشکر و حبوبات کشف شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/466188" target="_blank">📅 10:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466187">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGRZ19uez7FQ_8oPJZA99AmCclrS_V165RA3gkC_uCWwMG9pSo91driTRAsDQSSWCMKfpfBmCIdq6px3D-0Ct5DK3cQ_R5m6GUMjic-IPP69CbFcImM1CT6m45n_upUu2IyeEAsXdMUFf_fJpZzOwPvzXl9BV7BSum5_eOwuDjUaCeOB536hOF5ld84hLh_UJ7T-n_y8A9IP0JXrZWTQH7LD5QaD40CP_EII1DngsaCBOHQmeG3ZdhvuipTJQRpX3OLwH8AiYtnsOoItiMvIaR6oGR86Tx2UC7cPY7r1vRR2xBhxTQQJpm1RlN4c7BUtvEZq_YN_ZqztJxJ7mMbtFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ‌های جدید ارز در مرکز مبادله اعلام شد
🔹
دلار: ۱۷۵٬۷۵۴ تومان
🔹
یورو: ۱۹۷٬۸۱۳ تومان
🔹
درهم: ۴۷٬۸۵۶ تومان
🔹
یوآن: ۲۶٬۲۱۰ تومان
🔹
روبل: ۲٬۱۰۵ تومان
@Farsna</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/466187" target="_blank">📅 10:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466186">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5fdf314.mp4?token=tryrZrKaOp28fCz5KQMXuU0pQUPsmpVeMufJ2mqwVR_jQid3bfStbEAI52BC93ni1jk1_xE6ymA-1vJZ71fk-5hg8WmMGfDP34D5mQ4YBEnxsrbuSxh1IG9Ki24BV7Xv69B1prU1jy54VjkdsJNM6mBkRGL-LP2T5yrT1PPDO6QNwsrQFzKIJi31MwnY5j3BoUYxEUV9J8gzAFGe4kjLeco-eyxVqfkDTUTGlgB8o2sy9z_RruUqtFlvSeGu8muwSGYpJsW_tTNncuG_Fy8BI48M3ZLqbdYu9UXt0meLWA0HsFs4pytbVNG2ifuFqs9Z4YhB5zY68ZPmCqoplCZxZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5fdf314.mp4?token=tryrZrKaOp28fCz5KQMXuU0pQUPsmpVeMufJ2mqwVR_jQid3bfStbEAI52BC93ni1jk1_xE6ymA-1vJZ71fk-5hg8WmMGfDP34D5mQ4YBEnxsrbuSxh1IG9Ki24BV7Xv69B1prU1jy54VjkdsJNM6mBkRGL-LP2T5yrT1PPDO6QNwsrQFzKIJi31MwnY5j3BoUYxEUV9J8gzAFGe4kjLeco-eyxVqfkDTUTGlgB8o2sy9z_RruUqtFlvSeGu8muwSGYpJsW_tTNncuG_Fy8BI48M3ZLqbdYu9UXt0meLWA0HsFs4pytbVNG2ifuFqs9Z4YhB5zY68ZPmCqoplCZxZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: اصلاح اساسی وضعیت معیشت پرسنل شریف فراجا یک اولویت قطعی است
🔹
مجلس تقویت همه‌جانبۀ‌ بنیه‌ انتظامی، از جمله تجهیز پلیس به فناوری‌های روز و اصلاح اساسی وضعیت معیشت پرسنل شریف فراجا و دیگر نیروهای مسلح را یک اولویت قطعی می‌داند.  @Farsna</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/466186" target="_blank">📅 09:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466185">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImZw_tZvM-k_dp9lzra59iuZYYiCvdLNPByYq266h36SW5D5J9nbaKh-DwvP1JrudOy5sWVUmK9RSjAd8iaNzwNkFMZcdjxjxzycUm7_yKiDbehYBuhybQzLyXf9wHC0su6z76lwd6nWO2EK85ODqrUflz2jCPX_v7otcqNS3rMykUzFDWNauuif0B42i_VCgUlt_FTIgwPa35FO_LCtOfjz2QGx21KZCUlYN0ufI2W_s6-4vzHmf1CfD_5IrqwIz1mZDFukUFkItqIjwx7rpn2pTRQQZE9u8UguyRHC1Zrm-SdfrqR9aB-98n0NbFdIg0ad1IrkTbqQpOv45pmkqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجری آمریکایی: ادعای تروریستی‌بودن حادثه فلای‌دبی بی‌مدرک است
🔹
مجری شبکه آمریکایی «پی‌بی‌اس» با زیر سؤال بردن اظهارات دونالد ترامپ و بنیامین نتانیاهو درباره انگیزه حادثه فلای‌دبی، تأکید کرد که هیچ مدرکی برای اثبات انگیزه تروریستی ارائه نشده است.
🔹
«جف بنت»، مجری برنامه «PBS NewsHour»، پنجشنبه‌ شب در گفت‌وگو با «ژولیت کایم»، مقام پیشین دولت‌های کلینتون و اوباما، به اظهارات امارات متحده عربی درباره بررسی احتمال «فعالیت تروریستی یا برنامه‌ریزی قبلی» اشاره کرد و از کایم پرسید در شرایط فعلی درباره انگیزه این اقدام چه چیزی را می‌توان با مسئولیت‌پذیری بیان کرد.
🔹
کایم نیز در پاسخ گفت پس از هر بحران، حادثه تروریستی یا فاجعه، معمولاً خیلی زود روایتی شکل می‌گیرد که اغلب به دلایل سیاسی مطرح و تقویت می‌شود.
🔹
او گفت: «فکر می‌کنم فعلاً باید این مسائل را کنار بگذاریم، چون چنین اتفاقی معمولاً رخ می‌دهد. انتخابات در پیش است.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/466185" target="_blank">📅 09:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466183">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7f35df4ad.mp4?token=INbylFIpZnGFHiQRHKQ5Zh8n8wHBEqEYRgLs1d3Xagmbj626q_DAVLBumqNaq362SgbOocNVjH-KQggJn0GlNCGdjQBCL7YX6qsjJezCni2bwgcwICt7BliGBK0ylIXdmqaO93N1B1v7Ut96wngDAM2X7cr0zr8ddgEnOyp5ToZQGkOKocaVuvpg_bKRhknXlO5h2_Ehv_rd2tZwGOtL3ij0BmIkJ4VqPguyoGyFcBUfsW816mmq68kX3Bo5sRF9J0JVeyuo4fXaDNJnGeXiCXJbxLSf7Hn4PwabiuLv5IfOBIuMXbx-fhemB6KYvIpnd1iN9viLSHXFq0NbiYj5rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7f35df4ad.mp4?token=INbylFIpZnGFHiQRHKQ5Zh8n8wHBEqEYRgLs1d3Xagmbj626q_DAVLBumqNaq362SgbOocNVjH-KQggJn0GlNCGdjQBCL7YX6qsjJezCni2bwgcwICt7BliGBK0ylIXdmqaO93N1B1v7Ut96wngDAM2X7cr0zr8ddgEnOyp5ToZQGkOKocaVuvpg_bKRhknXlO5h2_Ehv_rd2tZwGOtL3ij0BmIkJ4VqPguyoGyFcBUfsW816mmq68kX3Bo5sRF9J0JVeyuo4fXaDNJnGeXiCXJbxLSf7Hn4PwabiuLv5IfOBIuMXbx-fhemB6KYvIpnd1iN9viLSHXFq0NbiYj5rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
قالیباف: ۷ شرط ایران محقق نشود تنگۀ‌ هرمز باز نخواهد شد
🔹
این فقط صهیونیست ها نیستند که‌ در استیصال و درماندگی‌ گرفتار شده‌اند، آمریکایی ها نیز در مقابل ایستادگی و مقاومت ملت ایران مستاصل گشته‌اند.
🔹
آمریکایی ها که در رسانه‌ها حرف دیگری می زنند، اخیراً…</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/466183" target="_blank">📅 09:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466182">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b76509c10a.mp4?token=UEEz0at0DlR6qR-rEsBgz8ek3uv75PfDFEOyaf0yQOElG7onpFw-WqO_D6HAB-3DekCiZfC3Dk0eW6Y-D-_PX9lCwBgLEhAsafecQLtfN9R7SnE7QxyPxWRlYH1VXYE9GpViBStN_AyxYPUhl5AxYzVE8MAQUwP5TpId_Ef1xzV5vSYhcwJO0aqDasM7eS-jh0xJVs0h_-EyAKq9qFbn5tYQeu63AraK1gv099t-zN5PGd0sCZLOblFwAb1FCFEBGQFAGUpvBe4hdUu1Mu6kPlYeKFglQlX6DlAKc4hTokqfeFwqKigpO51aB278uqj74m6Mpvy6NGBK5wjtIAO_Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b76509c10a.mp4?token=UEEz0at0DlR6qR-rEsBgz8ek3uv75PfDFEOyaf0yQOElG7onpFw-WqO_D6HAB-3DekCiZfC3Dk0eW6Y-D-_PX9lCwBgLEhAsafecQLtfN9R7SnE7QxyPxWRlYH1VXYE9GpViBStN_AyxYPUhl5AxYzVE8MAQUwP5TpId_Ef1xzV5vSYhcwJO0aqDasM7eS-jh0xJVs0h_-EyAKq9qFbn5tYQeu63AraK1gv099t-zN5PGd0sCZLOblFwAb1FCFEBGQFAGUpvBe4hdUu1Mu6kPlYeKFglQlX6DlAKc4hTokqfeFwqKigpO51aB278uqj74m6Mpvy6NGBK5wjtIAO_Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: ایران سیاست کلان و امنیت ملی‌خود را با توییت‌ها یا مصاحبه‌های روزانۀ مقامات آمریکایی تنظیم نمی‌کند
🔹
آنها این صراحت و قاطعیت ما را به خوبی می شناسند و با گوشت و پوست و استخوان درک کرده اند اما برای آن که افکار عمومی داخلی خود و مردم دنیا را فریب…</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/466182" target="_blank">📅 09:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466181">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fcde6921f.mp4?token=O_NB6ZR9sq9ZVlTNx1lDYE6EVGlhT67IeRoUOl4Wvxg8_-ilsKlWV5xbR93bglANnYr38nznMyz6PFU42AVEsc8gleZgoyAmrokQawOclbjlcrte2BXvHYIM4PUkmTUL0HN4ojCHn96orYUWgCvWZRaTDoGTawwexm2mr54uooo0WZ7B8nOyYjB7_Mgk1ecLSrMam_kMghsLjh4hBqScGsT_vDqXMKloLpwbukNi5PdfRg7wMaGHogr7f7zER3sc_y0JXDw4gt-yAuXemWapxox_mmQtVX73RTWliD8CglFzId61lRGVtbARxJJ6GYgU0Hzq7Q9UN0EAYbG1vLAj9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fcde6921f.mp4?token=O_NB6ZR9sq9ZVlTNx1lDYE6EVGlhT67IeRoUOl4Wvxg8_-ilsKlWV5xbR93bglANnYr38nznMyz6PFU42AVEsc8gleZgoyAmrokQawOclbjlcrte2BXvHYIM4PUkmTUL0HN4ojCHn96orYUWgCvWZRaTDoGTawwexm2mr54uooo0WZ7B8nOyYjB7_Mgk1ecLSrMam_kMghsLjh4hBqScGsT_vDqXMKloLpwbukNi5PdfRg7wMaGHogr7f7zER3sc_y0JXDw4gt-yAuXemWapxox_mmQtVX73RTWliD8CglFzId61lRGVtbARxJJ6GYgU0Hzq7Q9UN0EAYbG1vLAj9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: براساس راهبرد اقتدار و عقلانیت، نه هیجان‌زده می‌شویم، و نه مرعوب
🔹
آمریکایی‌ها که در رسانه‌ها حرف دیگری می‌زنند، اخیراً از طریق میانجی، پیشنهادهایی مطرح کرده‌اند. اما باید متوجه باشند که دوران فرسایش زمان و دیکته‌ کردن مطالبات یک‌طرفه گذشته است…</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/466181" target="_blank">📅 09:41 · 12 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

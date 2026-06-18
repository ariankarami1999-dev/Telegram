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
<img src="https://cdn5.telesco.pe/file/l9Ok3GDC1DKY2enHntFJFNcOH_b8T7gktxg69k9FgjctNIlr6-kkfK_MUQREOZU1RMSxLi6V9BcBdldG3vKrxMc0PSSYSWPwTlC79eRM46_6xLhZGzmhYA5CCFJVdIxV00uV5-SF2lFKKTgfsbxpYQnslJZfXWZS_xWtQesJVM3iQATWgOH1QujRmMQu3Nllil-c-CLD3426uVDwN5kEfwRA7oDNJv-Po8PxJNn4ZVNwry4KbwWpZ45B2Ta1DPk0GI16Ti47j5JnbhfsvFwJANQNqbJS7m86DDwZldqLt3nhXgyObQ3CqpUGaH7VCAIFDRrA3EOb0JaXYEFUKr8I2Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 662K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 14:37:40</div>
<hr>

<div class="tg-post" id="msg-94182">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtXBiJSo4BcB7O-B-unKMgbrDcnzdgo7i01JJoqbTpbKpi5hCWTlBZf-P2DIhg-Cip7Qq2QVPAwOESV0kWabjBE1AE5aKrFf4NgKyoecBnWYHcuoVAy2LRFKXRp0EmHhRVSJ_wtPd_7yhIHgYHeWgMSW9VGs2dd0QtQydJ0bH-3xfepVV0QYvWh8R5zJaeH2uldqtQlrXYxehJk7FhMC27qZDkE__iynlph-S_wLYb8YwrtNamgTy7RNlx-kBIBA4Zkop2i00Zcc7sH4hYnQeUvj8un673zoSCl7AK7B83BSCoaA8-4kSqgX5rndoX2xPThQdB2mwcTOOdCibeyj4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوووووری نیکولو شیرا:
رئال مادرید آماده‌ست یک پیشنهاد بزرگ به چلسی ارائه کنه. بازیکن هم علاقه‌منده چلسی رو ترک کنه و به رئال مادرید بپیونده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/Futball180TV/94182" target="_blank">📅 14:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94181">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQa-Z3s5ECzom-5qtIDfEC-1PmNl1UHzru7KoMN4EaXxF7jiTppPBCYWQsC-MudfDcIxSg4JgvJOr7yBlXNx1_REGgzUA_L0fP9FCqQu7IAoec0mlAkOQk-fv4TwkclnlaB_eggAoIqFIYw_fNwcpJIsTIj-Ljuq8kmXgXD2OFwiy4KJHHGIwwbimkJiWJrbWaGeiHgre4on89OO7EwzP3YjyGVcXZLkzmcpsPPYyJ0efoHI1IlGvWv-T9efNgT3ZZn5q7XyrmviSj58RK_x70-7V6S6re84FfNtQlIV0Kx4nbb2zu2R_iV5lwYQ5p7PYfz4IGMO5_VJ54mdJQfeRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🇳🇴
📊
عملکرد ارلینگ‌هالند در کریر فوتبالی خودش بعد درخشش در اولین‌بازی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/Futball180TV/94181" target="_blank">📅 14:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94180">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9087c58782.mp4?token=INUR9gCYa3m2ro3EHadeoaj18ywf_48FCUzFTy0uraogD5TtS5E9HRLvsTi0yUE-S0tDbG0bB1YSk5SqG7o5vZAeyTTzuKldbARLVcLy-THldWwcvhObQVcy4mtjpCTxMmqVLj7IriMGHxSuAdJ5vd9xSg1Jf8UUOmUaN95RgZ3l2mMm_3E4be-xhH4gmNOFFAEVFH-_6UT0T0sfCWQrdeBm0qo5oBUhTaaGJO7oodq730169U2BLNC6Rz6JKhx_tf0sMT-pgxY5vPge6si1TdJxGMkOK8GFOmNeWZxxu5SEseBRN_5grUkRJHZ2dWSNu3K5ewGt38_BmcLzFw3RwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9087c58782.mp4?token=INUR9gCYa3m2ro3EHadeoaj18ywf_48FCUzFTy0uraogD5TtS5E9HRLvsTi0yUE-S0tDbG0bB1YSk5SqG7o5vZAeyTTzuKldbARLVcLy-THldWwcvhObQVcy4mtjpCTxMmqVLj7IriMGHxSuAdJ5vd9xSg1Jf8UUOmUaN95RgZ3l2mMm_3E4be-xhH4gmNOFFAEVFH-_6UT0T0sfCWQrdeBm0qo5oBUhTaaGJO7oodq730169U2BLNC6Rz6JKhx_tf0sMT-pgxY5vPge6si1TdJxGMkOK8GFOmNeWZxxu5SEseBRN_5grUkRJHZ2dWSNu3K5ewGt38_BmcLzFw3RwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های زیبای دکتر انوشه: فوتبال و زندگی مثل هم هستن و شاید دلیلش همین باشه که ما اینقدر فوتبال رو دوست داریم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/Futball180TV/94180" target="_blank">📅 14:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94179">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oayXOoN7gb6xAzWp2F_fC9dGntvcBgkxGC7dDLVdvzimlCVVgq7jtYUGvK0mHLpYhxgAwUizZUnwAZs1CBA3Z58epH6KLcSvDKaguQN1-GUlz5TSSohRlDcIrXTEDDFPKR-PCKkQp4Kw6GECQ54WovhzSyzsDzbsgfLGbQbhLhBzXURMuBXHKHryuo9nW-fTHgmZOB5aar6D0pA4w9MH6YCri0E_8e8KrEcOGkoNDVmXE3TLctUDAzPconp7WiU7wYeN7MRp7bm8ztFRr5AbqDqPKiS3SJpy82yGhDeFswTYMhxkfNiHi_75tNEI2BXbNg3jnjKvaazMj8kQ4ykATw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پستی که رونالدو تو اینستاگرام لایک کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/94179" target="_blank">📅 14:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94178">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39843c046d.mp4?token=TQQilmVndwmBQEcUnBcojWZLv6KRoW-F-TTGDoh0QcIoNF1SwsFyc-p5cE_Fc7cHQj-Nu_4Z2ajnAZwTNtZFJ7NzgvvVKNTL_u0pqvKegrCzQCzRXRKAPhUqebf8Pwzbs2C78qXaAA6iu_iCKxmgaXcVN9CgyLn3DTPgKS548E7VkCyfYIq0KWSqEHDhHlnX3mH8ktbcVuf7hBlEYOUSy7wU0EiTwf9ay-VKb-zJCu0k9ZrGDMJMdag0IUYeL1mi7BnNc1nWLP_rWz9jtLw8s2BWYhfKfAU4c_xeKeN9ZEGp9YERRS37S5wWlG9jfC80jWZgYD-VnG2wXqU6Y9uPpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39843c046d.mp4?token=TQQilmVndwmBQEcUnBcojWZLv6KRoW-F-TTGDoh0QcIoNF1SwsFyc-p5cE_Fc7cHQj-Nu_4Z2ajnAZwTNtZFJ7NzgvvVKNTL_u0pqvKegrCzQCzRXRKAPhUqebf8Pwzbs2C78qXaAA6iu_iCKxmgaXcVN9CgyLn3DTPgKS548E7VkCyfYIq0KWSqEHDhHlnX3mH8ktbcVuf7hBlEYOUSy7wU0EiTwf9ay-VKb-zJCu0k9ZrGDMJMdag0IUYeL1mi7BnNc1nWLP_rWz9jtLw8s2BWYhfKfAU4c_xeKeN9ZEGp9YERRS37S5wWlG9jfC80jWZgYD-VnG2wXqU6Y9uPpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇨🇻
خیابونای کیپ‌ورد بعد درخشش گلرشون جلو اسپانیا یه نقاشی غول‌پیکر ازش ساختن و فوق‌العاده شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/94178" target="_blank">📅 14:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94177">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">امضای پزشکیان از نزدیک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/94177" target="_blank">📅 13:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94176">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnfP0laITKTpVjDO_3Dve7OkJ3g4df20eXs3wklvQXDsThri7hByY9ZpKEk47oM-pQkW5UaOEvjTUfmtRWyXFntrgF3FIfPhzn1ebBn-E1StVDwr7-BcCO5RaI_7iCKc-DcttQUwDyAzcpEPPSyhLo42pGeF6uDoBQ9VpqhfB4KV6VaQ9fwL7tzVfL4NotNjzFmbknMs3g3_QENThGKamKJd_JsK9NjtRxzif6V6hPxrmsAQtsEfyx7HBxUyalSWLwJC86e08IA2H2kU91-gJ7ErAX7NAMTFuYQk-UBwspfeZwJK5GknD2bC69s5WutqZXG5Q5dh0JCE_trV6Q_-IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
سه‌گانه ترسناک بایرن‌مونیخ:
🔺
‏اولیسه: پاس گل
➕
بهترین بازیکن زمین
🔺
‏هری کین: 2 گل
➕
بهترین بازیکن زمین
🔺
لوئیز دیاز: گل و پاس گل
➕
بهترین بازیکن زمین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/94176" target="_blank">📅 13:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94175">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6df6576c1.mp4?token=F6sZE5urFQM62tnpXeI6H6lZjFdZ4FC4eAGlNR5PSEkbncnVYJR_tO4oXOwfqEPaFiDMoIXl4v-yAKodhaRKoH9jyTq1rGEgr7F3CQoERsPH8XByYZgoVGKIo02GPbFwjWXRiHD9QtwSljlC7esIJx7SkRjcpWdeXqJmN3v9E9B1Le4SuWsG00WoT9vBHxTzFxEN4npqfR9LDkFzL3Q5GvHKuPlvvVnl-Dx-rMr5DUqVn6jY0Dm1oNAnRYSUD3OABRb2H0vgtjmvfwjVfBR28o9cBJfRu5C4qDYrt3AzAUZWLUmusFovfkzcalbg_7CCgVCazLVWtGRA2c5sj8Z1gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6df6576c1.mp4?token=F6sZE5urFQM62tnpXeI6H6lZjFdZ4FC4eAGlNR5PSEkbncnVYJR_tO4oXOwfqEPaFiDMoIXl4v-yAKodhaRKoH9jyTq1rGEgr7F3CQoERsPH8XByYZgoVGKIo02GPbFwjWXRiHD9QtwSljlC7esIJx7SkRjcpWdeXqJmN3v9E9B1Le4SuWsG00WoT9vBHxTzFxEN4npqfR9LDkFzL3Q5GvHKuPlvvVnl-Dx-rMr5DUqVn6jY0Dm1oNAnRYSUD3OABRb2H0vgtjmvfwjVfBR28o9cBJfRu5C4qDYrt3AzAUZWLUmusFovfkzcalbg_7CCgVCazLVWtGRA2c5sj8Z1gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سباستین ورون، اسطوره فوتبال آرژانتین: اگر مسی مصدوم شود، آرژانتین با چالش‌های زیادی برای ادامه جام جهانی مواجه می‌شود/ در ۲۰ سال گذشته مسی نماد آرژانتین بوده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/94175" target="_blank">📅 13:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94173">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33819b4cf6.mp4?token=My8eORNCwS4hBL0TmibUmTo82CATIfAbX-dv9Cjr_iC1QbMC-E3-vTmJtE-3xO5O4p0t0ejRBRLGtt3XbFc5WH6KcAyD9eru-BmkmHqph00BiaMGnF_Ah_aSLobYgB1qlk8NrGSM-OzKpkYTvfDl-aQvifrW69XbZHWPME-9VDhaI15n0OYyd5kQ8qbzyk3DQQY_E4SgFKfokLZfLrtIwB53G48hIw3LDbfWcOUc_ju4dEmETpD31fAd7Rp6UoTE1rArH7uxScHrlgF9QfvbRql9TDhSoWp6LCHBtH6Tvfmah0a0XKZeEm9Zra7m2YE86lNX_peC0G3ShmTkiWbmVol1sdWj8kuhIWvmBpdAN0yol_3z4V-1bJ7v7iUOq4x0idjjkDdJLCq66Mo24p1EIpxB-Yzurkwz18-17i4nyN0fLOCZ8Ptyo8Mh084yfK-fzxfSCl7m1do5Ey2-ZzrgvUHS1ob-WvTGvYzYy0HTAssCBWe09PKWrSIFVO4aUakFEVud5tOPwUDKl-vA__iCbrLp7dua87VJIg45C2UetvARIhT8PshCtBal-rF71uFMlVqqr6ikC-LfwN8BZUOsmYOnA8w5QCjZzZ6VzUUx85puGQOJXvrDjIMr8vTRg-IvAkRUZYZ-urPuOjthQGBFqhVp2tDme8AZ8n6DBEIS-Ak" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33819b4cf6.mp4?token=My8eORNCwS4hBL0TmibUmTo82CATIfAbX-dv9Cjr_iC1QbMC-E3-vTmJtE-3xO5O4p0t0ejRBRLGtt3XbFc5WH6KcAyD9eru-BmkmHqph00BiaMGnF_Ah_aSLobYgB1qlk8NrGSM-OzKpkYTvfDl-aQvifrW69XbZHWPME-9VDhaI15n0OYyd5kQ8qbzyk3DQQY_E4SgFKfokLZfLrtIwB53G48hIw3LDbfWcOUc_ju4dEmETpD31fAd7Rp6UoTE1rArH7uxScHrlgF9QfvbRql9TDhSoWp6LCHBtH6Tvfmah0a0XKZeEm9Zra7m2YE86lNX_peC0G3ShmTkiWbmVol1sdWj8kuhIWvmBpdAN0yol_3z4V-1bJ7v7iUOq4x0idjjkDdJLCq66Mo24p1EIpxB-Yzurkwz18-17i4nyN0fLOCZ8Ptyo8Mh084yfK-fzxfSCl7m1do5Ey2-ZzrgvUHS1ob-WvTGvYzYy0HTAssCBWe09PKWrSIFVO4aUakFEVud5tOPwUDKl-vA__iCbrLp7dua87VJIg45C2UetvARIhT8PshCtBal-rF71uFMlVqqr6ikC-LfwN8BZUOsmYOnA8w5QCjZzZ6VzUUx85puGQOJXvrDjIMr8vTRg-IvAkRUZYZ-urPuOjthQGBFqhVp2tDme8AZ8n6DBEIS-Ak" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
▶️
انتقادات تند پیروز قربانی به امیر قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/94173" target="_blank">📅 13:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94172">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EX-VUAPysH_Wv-E4VrgBSj9IivQxFv-iIjmsRS_j-F8ofR57_uxxyW1w89OOyv99kL_we5Gp098Y3GC6RvwI5iEIqJbuu_cEZq8_zyPUoy3CrFfhVyzY37RiEHPIiivvJHIyAkywwuEuIFJelOJzp_3zd_6MN_bzqWj12HfrSHqu49lRUmDXtSCNBeaIOsql6a-nu6qyy-R6LYIDJeNYmNqz6v_8fgF_LACQjG1si-hZAfTI_MqmS87qucK4EcstV7TyIvZr6bPgwHOTbDW-5E1XYnMuWAvdfUmnH8srCZwrArd6-wv9ssNJ5olMLKkfKyYE_INyTDfMJjpaDE9ASQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
خانواده لیونل‌مسی WC2022
🆚
WC 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/94172" target="_blank">📅 13:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94171">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb6168a2a.mp4?token=NvtaSGzyhTx14hNrxs2LgUyfnDhgtbLAZpUSnvnm4IyhulnvAAEdQwSh9-Lzn7OGFMkmPv_sdI5xwyeZoOgEy3KqJBXvKkihqRm8AUqPhIt2gTPeC-3L9Lc0cf2bAyg79H5uCnZSKubQpFO-_qepLwb-YoiEZrwKXquamuEv6oODr5e15u9aMxSn9wZXXJCr3RBzaD4RC2fBc3Axyh-xBzGDUMWUnjsR9ljrz3PdNsrWnDlPthVTDvX-Ws2MDwVvEPFNICF1ymhhK3hCHoXfflyd4Y755oMmK7y3vz1pBJZ2e98RHd0WpDLqynsHPgF3NHN2e8KaD0KUhQByJ-G8zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb6168a2a.mp4?token=NvtaSGzyhTx14hNrxs2LgUyfnDhgtbLAZpUSnvnm4IyhulnvAAEdQwSh9-Lzn7OGFMkmPv_sdI5xwyeZoOgEy3KqJBXvKkihqRm8AUqPhIt2gTPeC-3L9Lc0cf2bAyg79H5uCnZSKubQpFO-_qepLwb-YoiEZrwKXquamuEv6oODr5e15u9aMxSn9wZXXJCr3RBzaD4RC2fBc3Axyh-xBzGDUMWUnjsR9ljrz3PdNsrWnDlPthVTDvX-Ws2MDwVvEPFNICF1ymhhK3hCHoXfflyd4Y755oMmK7y3vz1pBJZ2e98RHd0WpDLqynsHPgF3NHN2e8KaD0KUhQByJ-G8zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇦🇷
🇵🇹
صحبت‌های محرم‌نویدکیا درباره تفاوت حضور لیونل‌مسی و‌ رونالدو در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/94171" target="_blank">📅 13:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94170">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3720508738.mp4?token=gvRLwlN5jjP9bqmhqXYs1chIh090AiI6WppfoZsGrnPcSm_5WxxrmMUYNEinTjGjU7g7rxIKWUuuolB-nUW5-5mC6nqJBeBfBRZ1nlhyCFCha7TvYKHR1F8raDPwyU7viGhH8h4E77uHK9nRlnMJ7XNunaMdEDNaHGw82YcNozfwV--VpQCDWvYssW60M___IsM9Q-Q66leyJioeqcsZv_P9OKyhPzgRnF7Ds3WcRAgzkHCEqsUQpnLw8Vi-_FUO3hM7IAxIx4k2VaAQ_yoOE73Br--CSK1zs4onmY3DKxi67oy0ut4s4tDnA5GgvWEDrcvf359bqv4BORT5_tvQrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3720508738.mp4?token=gvRLwlN5jjP9bqmhqXYs1chIh090AiI6WppfoZsGrnPcSm_5WxxrmMUYNEinTjGjU7g7rxIKWUuuolB-nUW5-5mC6nqJBeBfBRZ1nlhyCFCha7TvYKHR1F8raDPwyU7viGhH8h4E77uHK9nRlnMJ7XNunaMdEDNaHGw82YcNozfwV--VpQCDWvYssW60M___IsM9Q-Q66leyJioeqcsZv_P9OKyhPzgRnF7Ds3WcRAgzkHCEqsUQpnLw8Vi-_FUO3hM7IAxIx4k2VaAQ_yoOE73Br--CSK1zs4onmY3DKxi67oy0ut4s4tDnA5GgvWEDrcvf359bqv4BORT5_tvQrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهار نظر جنجالی سباستین ورون, اسطوره فوتبال آرژانتین: مارادونا از لیونل مسی بازیکن بهتری بود/ او در زمانه‌ای فوتبال بازی می‌کرد که حتی زمین‌ها صاف نبودند ولی او رویایی بازی می‌کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/94170" target="_blank">📅 13:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94169">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSx2XRF5Xe5LfCSWkTpu2oMOn6dXl94nLZfkkLuXbDIBp7ErUM2cNUkJZfxjVsv0zNqunfGKe_MtxumdXw31mjK96vK6nttmVlnUJ3zTMYXdmQKoWeTbec7pQNwtMiqfL_EVGxeUCRCZfvlkO_YReCiLusMzzjDleI41n8W-g4jOjCW8ePoBuGdZsLi21d9qh2nF44BvJ3l0U2K5CoJQhKbLuI3IiBySeQZDszhhMUDTJ4nkYgaN8LhrOiKPmbsaqrBDurCE0tjoT0TU4yblKnm0-tq2gbYAOgUWTdfkiKJlq63fb0zyldOGQixS0oK24ZsTy2nUZQnGf6hxfygaJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
بیشترین پاس‌گل تا پایان هفته‌اول مرحله گروهی جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/94169" target="_blank">📅 12:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94168">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8bc47b42.mp4?token=ifcB9PStvS0ERjq2t0_UTEtv2z-LfIgp8LdLejyHLixUYxN-4x9grlpnQkd-nqCiVKuCcoZOFsXefLhPiaJ8eWzhsLGHTUNq9gMwAuriPTnGyROhTW44MGJFBXoi0m7qXDapHSfy1zler_XZ6qHFyvgce4B6voKoxV-hORkRmjcL9d9ajKDpeJVmXNSyYMqwKfBE5oOyGc8HZYqyCk07eXUXxhZktC6AjulTemv0CmlLnd6ocNBCW9dnkQ1b3ZbopQcOICw6s1dO_ONx6JGqsxjndY4ywT_ImxOhRjUd0KeEbZ4UlgqeUZ4Oxc-c-1-ooDTyOHiE307FP6tyxZM9Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8bc47b42.mp4?token=ifcB9PStvS0ERjq2t0_UTEtv2z-LfIgp8LdLejyHLixUYxN-4x9grlpnQkd-nqCiVKuCcoZOFsXefLhPiaJ8eWzhsLGHTUNq9gMwAuriPTnGyROhTW44MGJFBXoi0m7qXDapHSfy1zler_XZ6qHFyvgce4B6voKoxV-hORkRmjcL9d9ajKDpeJVmXNSyYMqwKfBE5oOyGc8HZYqyCk07eXUXxhZktC6AjulTemv0CmlLnd6ocNBCW9dnkQ1b3ZbopQcOICw6s1dO_ONx6JGqsxjndY4ywT_ImxOhRjUd0KeEbZ4UlgqeUZ4Oxc-c-1-ooDTyOHiE307FP6tyxZM9Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراتر از سم
😂
؛
🤣
چالش بازخوانی نام بازیکنان تیم ملی ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/94168" target="_blank">📅 12:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94167">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb354f20c.mp4?token=mEVwG_OBp_WT8kqJFNU6DWkV77PIlt1Z3li-nKOkej2QZ9FrSrCwo6XIYGHNRpn-GvQ8-yodl6NRqpOJLg1v-O3sa1x3feOjT8Zpm-X60UvmQcx7XRD8ZTqlmR_mvKHwGEiZx_pAxy3CKFqHE0q7dMEGTA3r8tiEttIJJTNauscb_KeoL439eCobrTp7EkKrAgvauyxZt5ypqmKXJCiZI1S8uPvGaazaZ0rRX2VB5I9pukEYS7ZuVOa2r__jH_uuOxZJRWEoeHTB_1q7BA9U0Vi6PGw02rR75l6PVQlB4nMRKiC_XwL4VD67Kjbx7Gxqdwkls5iqSACWr10cprIbhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb354f20c.mp4?token=mEVwG_OBp_WT8kqJFNU6DWkV77PIlt1Z3li-nKOkej2QZ9FrSrCwo6XIYGHNRpn-GvQ8-yodl6NRqpOJLg1v-O3sa1x3feOjT8Zpm-X60UvmQcx7XRD8ZTqlmR_mvKHwGEiZx_pAxy3CKFqHE0q7dMEGTA3r8tiEttIJJTNauscb_KeoL439eCobrTp7EkKrAgvauyxZt5ypqmKXJCiZI1S8uPvGaazaZ0rRX2VB5I9pukEYS7ZuVOa2r__jH_uuOxZJRWEoeHTB_1q7BA9U0Vi6PGw02rR75l6PVQlB4nMRKiC_XwL4VD67Kjbx7Gxqdwkls5iqSACWr10cprIbhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهار نظر جنجالی سباستین ورون, اسطوره فوتبال آرژانتین: مارادونا از لیونل مسی بازیکن بهتری بود/ او در زمانه‌ای فوتبال بازی می‌کرد که حتی زمین‌ها صاف نبودند ولی او رویایی بازی می‌کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/94167" target="_blank">📅 12:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94165">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTk2UeFJA05G3oD7EW-aaxYFz8tr_RlDeF-c2uoCeb57XTx0jaUvkQvkvzyQWZn0DlYpHG0VuIbwYau2et-G0R2JNus34bat_Vpw3T5OZJKpV9JTUUAMggc541XeYwO0u9qjkaMTl2vM5owgyb_Y7jFl9SS6RbbqX7aF7dQdJyV9getWzQHvNzeDRSB7LCZ8rKVFG1a0Ja1wApH5pZu68Hij0uOKs2XqrAclnrG2TsWnDb7Gy7rE4ZfJgcCRmjzpkcFTnOX2HMYWJwb5hbDtTBWf7f-xmejAW5lEBaJd27Q2z97PjOaejIaaVy2yai7x-VwGvHzotRmNigZGvZRCkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🤣
تو ورزشگاه‌های مکزیک یه پیرمرد فوت‌فتیش بجای تماشای بازی درحال عکس گرفتن از پاهای خانوما بوده که توسط تیم امنیتی و اخلاقی فیفا از حضور در مابقی مسابقات محروم شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/94165" target="_blank">📅 12:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94164">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFVcfWZCoprSfrjOdjwNENoVQ7_F-U8234m24-TikXsIBNo1K8HW8WAlZb7X0FG5nbk5Y46gd6o5WGygPTehiuvtoO-OyOdjHHCt-EiPKc2d15nKfFYabacInojVStg00AXR_VB9iJrK0KVaQcunwRYTB3gJOrkxA-9cK2ugh5eG4orlCeBUYMtdtTOJycgztxNrIKmkBohjjUcCJcTbbhcmtfH7zgwrd2lRagFkWFttFp7PU_6OTIcwHZVONIWCq6Z_VjLtTFrBfEK2QSW8xxcRZ0IcD29V4R1kV1643Sn5G33ZedFQEA3ImvEb48JwfNlIoGSs-dWUpEpDkoXDrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فوووووری و رسمی ابراهیما کوناته با قراردادی تا سال 2030 به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/94164" target="_blank">📅 12:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94162">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtnjcqDe1FKFY-6L1xvz9o5ER17YHM8TAq99Kglj4D3QXTABuJBO3qzuteuAk_mD2WwNRawpFtnoE518LYwuu8EvlWvhLepq_nwzGoDyh3e7-CPynGb63SQ7AYRHSoBz2LlUm4j3rq1W1j_sEyvE4MO651tXUasn8zr51r0wFq7IrNVhM3kbWnDQovMDGl7D2Kq6d765jj83A5OqNlpWZH7avW4WhOY64tZ_1vcwNe9Ykwqw8Rhe2xZfNhnLKqEAg6hg-M_VV1E5QX1bHgnCqPoupPTjnX6iCN3KSWHwlioiWI9PJVtb-iAXikPMaBAsXFd_NaMHYzADfgKdUSKzwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🎙
مارک کوکوریا:
رئال مادرید یه ابهت خاصی داره، واقعا سخته توضیحش بدی. هیچ‌وقت نمیدونی چی قراره اتفاق بیفته. خیلی کم پیش میاد کسی بتونه درک کنه چطور رئال درست وقتی همه فکر میکنن کارش تموم شده، برمیگرده و بازی رو میبره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/94162" target="_blank">📅 12:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94161">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5767fe2278.mp4?token=O-zjIgqdxkSP5QzFHMOuE4NyVTrQe3GDc5_ujvHc04f1fQeSeJRcttxcXWEX7DNdP_V0_3HzAp5UklP-arg7poQKbjwKlh_iDkPfcD20t8kskeDejFDNnNzM1UefMisdOrmIMx2BtJWQvFgQB0QBMbvgxm2ncildER9II6LPJXz_maIOjbcOW-ObE80VNh2L3po2s6Zu0w3XYwlKEEmcrGRDptV6dnv_CEdIYVrH2SFhapRlio-xzTYNBqCcF37_EcRlVOHXZS1ue3Je-7DEYHwsP3-peq2boWWJDTv-YuK_EnjuJ14oFdQz-6IY_ApKDUrSf5lKeeYabQmc3spwPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5767fe2278.mp4?token=O-zjIgqdxkSP5QzFHMOuE4NyVTrQe3GDc5_ujvHc04f1fQeSeJRcttxcXWEX7DNdP_V0_3HzAp5UklP-arg7poQKbjwKlh_iDkPfcD20t8kskeDejFDNnNzM1UefMisdOrmIMx2BtJWQvFgQB0QBMbvgxm2ncildER9II6LPJXz_maIOjbcOW-ObE80VNh2L3po2s6Zu0w3XYwlKEEmcrGRDptV6dnv_CEdIYVrH2SFhapRlio-xzTYNBqCcF37_EcRlVOHXZS1ue3Je-7DEYHwsP3-peq2boWWJDTv-YuK_EnjuJ14oFdQz-6IY_ApKDUrSf5lKeeYabQmc3spwPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🏆
🇬🇭
رسانه‌های خارجی با انتشار این ویدیو نوشتن که غنا دیشب به کمک سحر و جادو هواداراش تونسته دقیقه آخر پاناما رو ببره
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/94161" target="_blank">📅 12:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94160">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5190506dcf.mp4?token=cxi5BowFrFaWk0ExdXfyaVim_KzXjThuJyWJLFIpor2nkXFjCgzZHnrmDc4DtOhBLh-0FkVpBhiWqNsjK1uFYPCJrzByDvna3_u9VfWbfhKAlWgGsTa1ZoZtIb5SMC8xR2JVBMdCaTbZYCGDw4GdsJNpLHX-JfaQ2sIuZz5Vy_KAhp5CsTfcgp8XfRxmDPJY5owN7G9oomwwE9WEuuUVhD4NTCeemRb8XXhbgfC_UQ7rsWIzlprSNb5EUgOr_zGO_MwUvLsqlBFa0SSQDjV9LicaiDmWgoJiBSxS2kcc0M45g8eRcfLYIMBIpDvT2gPGqAbaMaDSa2CePUJF1-2i2jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5190506dcf.mp4?token=cxi5BowFrFaWk0ExdXfyaVim_KzXjThuJyWJLFIpor2nkXFjCgzZHnrmDc4DtOhBLh-0FkVpBhiWqNsjK1uFYPCJrzByDvna3_u9VfWbfhKAlWgGsTa1ZoZtIb5SMC8xR2JVBMdCaTbZYCGDw4GdsJNpLHX-JfaQ2sIuZz5Vy_KAhp5CsTfcgp8XfRxmDPJY5owN7G9oomwwE9WEuuUVhD4NTCeemRb8XXhbgfC_UQ7rsWIzlprSNb5EUgOr_zGO_MwUvLsqlBFa0SSQDjV9LicaiDmWgoJiBSxS2kcc0M45g8eRcfLYIMBIpDvT2gPGqAbaMaDSa2CePUJF1-2i2jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔺
حمله نویدکیا به قلعه نویی: وقتی حسین‌نژاد رو دعوت نمیکنی حتما باید از لحاظ ذهنی به خودت سر بزنی
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/94160" target="_blank">📅 12:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94159">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Au6FKKJNcPSaqZaJGpBOowKC11-FdXM_vwFU5tDpXhejWJWLcy-d7yL9sBkF-URXG-XGGFr1KvAufhjRCzdEUt41Jkd-4rLQ-HAzeF4sO_48cJmQWnaXFAv8MRX4BhcWzD7R9nr-hOJQURGA3W4n889JNjvPG2CeRmwqtX6jdEJXy5Js_s6qBlH0GC8ZjNClQFh2bEy7Gk57spraUyfJ5d2Ijo-9bju_uL5qt1zNOT9x8WCgph5ggllIq1tsL10Rc7_S4lOZ_k5mx6KPsGsXnxofkEPe81m0auidVQLDe54pXPBrFj33BOAz4yxEfh0xm2PNH5zjWgfUlp9LMaW56g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جام جهانی ۲۰۲۶ در پایان هفته اول به میانگین ۳.۱۳ گل در هر بازی رسیده؛ آماری که از شروعی پرگل و جذاب در این تورنمنت خبر میده.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/94159" target="_blank">📅 12:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94158">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/CFOX1opPYo0C76DaDPDQxhYH2D9qrllYSAd8lFJt2qb64rEdINjuWqv6gj0p95-n9xBcfI5K-eL70UCf2PXOf9ncpBxGdDuXyPdwZLNa0MIHmd6pkYOuJLer6mMAzEr7fSyhfSYj5kmp3UYDtl8k6JJXrQsRHbFIvlmpK66xS0Bb32f-oVmkMaj5FDOX_wPdMfWU_F4mlIU3veNj3VeH4jSbB_ITZBUVdQnSCDonV1tOAW2gTgU7fwq3q6IM5IR6FjDsjZIvoTz5zf32URHY49KgXNRMEzI202C0F0lAFv1u0S-T8CyqRLZtYSKIqtCcHgZO9n5i38BU55n1tactwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نابغه خودتی پسر بقیه اداتو درمیارن
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/94158" target="_blank">📅 12:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94157">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWDW6dEZsvyTi28IcczcnwLAr9TtIoCEPy7jq6aQAWHly4LHjcnleljq21o2TsfrZvEfU1ysyak3ti3SiR3XxTXc2VTRR3Trncp2L1_cjpweYLDbkvFyv3tZ3ikk_Zp8LS9o_THnVRf-43b6utPd5BrRVt1L_SkDzn1snqyH4dLeDdEZPeUmRlnLy_xhLqonAhN1CsrPc_cNwNwwVDw5y6Oj2Gb86hQivg9DYpL5soWwQ5q9uL0KSTzao34pHzDsE66s2X6zqFmRlZki9MKua0nDdEmub7m40hmzRnHhLdi11zqLK2ZUHIWIrG8NN7C6yD5pO0xCU6xeK1e8wksIVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
رامین‌رضاییان در تیم‌منتخب هفته‌اول مرحله گروهی جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/94157" target="_blank">📅 12:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94156">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDOCw-Z4qhziLopgr-p5UADrbyGb1CoUWEQcNqjginpF0jEetpdJwF8cQ3lXK2bUKEg8EBE4zI58C2lnCXQpM8TdIJbEUwjg3Nhg37dsnYh_gby-qCc3T-Ic0WJV-D5cln5rJtePklgFgKC2_3ExYUMuaucZS7DA4_c0yyUxNGthzPaduDCvNRuGFwI4shVgTwFgXLoLAx1AfUXY08WtJAPoUz2JXR8LFBD2I1U2WNjJTJsEUlyS5NNOemTeZ8mdFvQjVcdIb3dZH94CFcCyOrrQlaHthdor4yBmAa2tbRPKZzbsRyDTED2sqMsePdO6wn_7jk2LWTOiit1fKpbKMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود‌بلینگهام ستاره تیم‌ملی انگلیس بعد درخشش دیشب مقابل کرواسی با دوس‌دخترش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/94156" target="_blank">📅 12:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94155">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7db6ffd41.mp4?token=bIfn4S-6J4ekjthxAbRx7d_n4rW-sVspxTTG1aV_jsrargd-8BXKXv9wV4bcvWbbsO4eX3RNZNJyf0g0WgwjrZKrpVRE_Byjaz37vGBCO4ZI4dcMHZZA4bEz2kVd6n9CJXDGK2FKHaLiGNTOnx_T90EjtdIWaMdN_ZieBufJz6W9KEDjrQt-yVBdXPzBT1mvdmI2wJciVWod8TO5NgpjgCsJc-SAebtTTubKQn3uPHSuMAOBTqgoxzyjz95weRU_7bdRB2xT8-1ECnavoK-ynHe0aNNAQhxx3ZSofRXdSAqLtMv8LhDZkhFVDGf1vVFTlswGjaV5DS7h-1SO_DeqiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7db6ffd41.mp4?token=bIfn4S-6J4ekjthxAbRx7d_n4rW-sVspxTTG1aV_jsrargd-8BXKXv9wV4bcvWbbsO4eX3RNZNJyf0g0WgwjrZKrpVRE_Byjaz37vGBCO4ZI4dcMHZZA4bEz2kVd6n9CJXDGK2FKHaLiGNTOnx_T90EjtdIWaMdN_ZieBufJz6W9KEDjrQt-yVBdXPzBT1mvdmI2wJciVWod8TO5NgpjgCsJc-SAebtTTubKQn3uPHSuMAOBTqgoxzyjz95weRU_7bdRB2xT8-1ECnavoK-ynHe0aNNAQhxx3ZSofRXdSAqLtMv8LhDZkhFVDGf1vVFTlswGjaV5DS7h-1SO_DeqiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
بدل لوئیز سوارز یه جمله گفت که باید رو تمام درهای توالت‌عمومی و کوچه و خیابون بنویسیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/94155" target="_blank">📅 12:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94154">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5pPEulUBCx2FLc3v-z6CzcD0NE4FTq1VSB3DAnYMLWzqTf5DUH_HJ1Pz3olHO8uNMnP9i8nGFiqebgz4NCGy3DM3OxCGs41a1_3YQrujtVChJzXH2JwWBPldlXGgz29ovGGQblweVFhaU4zJhyJDv7iTky4Dg3kJXMAqCO4QGPHSPe-E0e9mSyHX5WIfXLKZpxh08kMb5ApnoJR4_Zj2k84M0YWxYVXCSB95JeuoDrrM9y2dVHO8-cVAhT8IpJCzBO9hMZkPyzQ5IoXsiYkCAByrG32e5z4QTyHaVA9j6hn8yU6tM_6bBywINBUjSAGpRgfwV959QnZdsjYUK4HtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🏆
میزان حضور تماشاگران در ۲۴ بازی ابتدایی جام‌جهانی؛ تقریبا همه بازی‌ها ظرفیت استادیوم تکمیل شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/94154" target="_blank">📅 11:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94153">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2491447567.mp4?token=O8prS52Z91PCpDvYOzVY7UyDAfGxvdjKmIBXcy9G0SON8rWeH3kX-hsDts9nZyaUMWE1eXRU4QOZUwT4_7vxmTEv_n6bnoSKTwTsajn_VttVIOBAmdYvJDxpZB5S9KjK0F5NSiZUdBJOJevpJnsYRiQ9cJBcRUtbNm_XKw3rVmo6r3CQHwnECN55QqxdG0kbaFr2lPwb2w91XB8i3bmxmUD0fFwuI7EepNso0oqA-6IAKxVF_7UqWQnh3FlNrICzcWhs50L-W1G1wyhNpRps7A34eu06RzMe4Gzlt08InACOsR6yh_fl91CRjfzdXHU7vdVdpjvHvZKllupVttZezpaXxZb1etVcegJCbX5QCL743ROwkEsZu9R0_ZxmVqQZ0FSZX2uoWhSa-NT88gAI0SIh9FDNE0Om7u6i6_FmbhDMCapDL4r6L6yQXZHpmdX7HLsiccYvYL8m5brgajFEj_6FrgYrl66OivRdRs5XSGSwagwxeYLZg_2zRBD1WhicONKCmjE7BWvd3cRev8_jn_SQgSnC_8fUYbyaACTEtuYieDaCY82GjXSEOKz4JkagJYh0u8yzBRXNJ2kI5vXileDCDfoMAeTW2WO6IUa4DTTPeTi6fVGcZKR_pYOi8RoJhpu-LepyTFCLMV5j7Asas9N4NAHqBDmdY1aXTW4qXXI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2491447567.mp4?token=O8prS52Z91PCpDvYOzVY7UyDAfGxvdjKmIBXcy9G0SON8rWeH3kX-hsDts9nZyaUMWE1eXRU4QOZUwT4_7vxmTEv_n6bnoSKTwTsajn_VttVIOBAmdYvJDxpZB5S9KjK0F5NSiZUdBJOJevpJnsYRiQ9cJBcRUtbNm_XKw3rVmo6r3CQHwnECN55QqxdG0kbaFr2lPwb2w91XB8i3bmxmUD0fFwuI7EepNso0oqA-6IAKxVF_7UqWQnh3FlNrICzcWhs50L-W1G1wyhNpRps7A34eu06RzMe4Gzlt08InACOsR6yh_fl91CRjfzdXHU7vdVdpjvHvZKllupVttZezpaXxZb1etVcegJCbX5QCL743ROwkEsZu9R0_ZxmVqQZ0FSZX2uoWhSa-NT88gAI0SIh9FDNE0Om7u6i6_FmbhDMCapDL4r6L6yQXZHpmdX7HLsiccYvYL8m5brgajFEj_6FrgYrl66OivRdRs5XSGSwagwxeYLZg_2zRBD1WhicONKCmjE7BWvd3cRev8_jn_SQgSnC_8fUYbyaACTEtuYieDaCY82GjXSEOKz4JkagJYh0u8yzBRXNJ2kI5vXileDCDfoMAeTW2WO6IUa4DTTPeTi6fVGcZKR_pYOi8RoJhpu-LepyTFCLMV5j7Asas9N4NAHqBDmdY1aXTW4qXXI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
💎
🏆
تعریف و تمجید فوق‌العاده محرم‌نویدکیا از قضاوت علیرضا فغانی در بازی فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/94153" target="_blank">📅 11:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94152">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LS55hvQi7lr2qGuaFUXN8QWZLa4w8PACBdl04ldJh9ssmNF5Dc4cWHNBZghmjBCkg45kVe8jYOEhhDTViR-aHW3ejF9QEOqZdJXFuQEOQ4aGvwgXK2Ya8NyipgO8lQfVQ5mJV5FopunLLLLLQJXPvlzgtqotCF-aXc_Vj9k8xTWMJkhjZUbmRlEKxjEVnRJR2DqCjV5IZIFVc2EjgLsjJW4Sq-m40a6dGWT7GpOzpc8Iw5Vt9p7oI9dtN3LZGGMtCUzC9jLL2pRXkiNZ4nA9IJEp9gMdtH2ghY5DlgEAGYc6KkXiuEkyg7EAOvYlmm1P1UiXDwp8XfZjNQyBc3XMmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
زرگر سرویس سپرده‌گذاری طلای ملّی‌گلده.
شما طلای خودتون رو برای یک دوره مشخص سپرده‌گذاری می‌کنین و در پایان دوره، سودتون رو هم از جنس طلا دریافت می‌کنین.
یعنی بدون اینکه طلایی بفروشی یا از داراییت خارج بشی، طلات می‌تونه برای خودش طلا بسازه.
✅
۱ ماهه: ۰.۵٪ افزایش وزن طلا
✅
۳ ماهه: ۱.۷۵٪ افزایش وزن طلا
✅
۶ ماهه: ۴.۵٪ افزایش وزن طلا
✅
۹ ماهه: ۷.۵٪ افزایش وزن طلا
✅
۱۲ ماهه: ۱۲٪ افزایش وزن طلا
طلا برای خیلی‌ها فقط یک داراییه.
برای کاربران زرگر، یک داراییِ در حال رشد.
🏆
و یادت نره؛ تا پایان خرداد هر هفته به قید قرعه یک شمش طلای ۵ گرمی هم به یکی از کاربران زرگر هدیه می‌دیم.
🔗
زرگر؛ به طلات وزن می‌ده.
🟢
ملّی‌گلد؛ پلتفرم امن خرید و فروش آنلاین طلا</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/94152" target="_blank">📅 11:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94150">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c14ca557dd.mp4?token=uwlcxgZ8o2sm1NmN6WjkIARFQ74ap45pgUa7HtAtcRPl7lPqeQRUVYGfIJxXDN74oDbiHPTkneDjaIM31zq1tnCwsFgBv35J1cCAtGEVoukLPVa2939FA8KFaVcSt-F2uCpe2K6a4dwO-XK-kNh-EsAco_XfjB3-zw5JHb88UNwEui2XvyemV9NmTcWdxTzaUd1g-c-YVe4peybjkUmm5KqDYIVBx0jc3RTH9AqBe_mPR4U5DJOLa9mEEpxr-UwylNwmgm1ZJrY4ENQnGrySL_2rySMX9KJYfsUBWHZpGUoiF0aGuox_sL--YQ30IZq8-XcGYp4hQqJ5ck18kqsCpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c14ca557dd.mp4?token=uwlcxgZ8o2sm1NmN6WjkIARFQ74ap45pgUa7HtAtcRPl7lPqeQRUVYGfIJxXDN74oDbiHPTkneDjaIM31zq1tnCwsFgBv35J1cCAtGEVoukLPVa2939FA8KFaVcSt-F2uCpe2K6a4dwO-XK-kNh-EsAco_XfjB3-zw5JHb88UNwEui2XvyemV9NmTcWdxTzaUd1g-c-YVe4peybjkUmm5KqDYIVBx0jc3RTH9AqBe_mPR4U5DJOLa9mEEpxr-UwylNwmgm1ZJrY4ENQnGrySL_2rySMX9KJYfsUBWHZpGUoiF0aGuox_sL--YQ30IZq8-XcGYp4hQqJ5ck18kqsCpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⁉️
تفاوت هواداران فوتبال اروپا و آمریکا از زبون زلاتان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/94150" target="_blank">📅 11:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94149">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab0ef7f628.mp4?token=Xvqq-QWuKkoI86GWE19LYHTrUm41l6uGaQR33tUd3a4pgpg211nkBTl7fN6Rn3qO7MRKqWJNzrn1lBIZHov7Sdj5WvkLkF5nAmARf4ouG8nZznegINdl8Y-sg51QxLuhAHJ400mj6Bv3m2OUl_Yjlkd37lU0KRVqrUF1cYlOzP0h4IYjE5svBlol0ayvt-kgW2fWjYkey7bBk3AnJ9fjSkswKQAyZCAac2HS6vpwr_TzyShB8jiA7lB7Sasayi7yyrPUl1hLryOx4Utnt7cJ5_e0rh7vG5DnEu3pVceKKs8eJzBwrfl0_A6FRMvABmBFb1YYeQR1xtODXIOVL5xAlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab0ef7f628.mp4?token=Xvqq-QWuKkoI86GWE19LYHTrUm41l6uGaQR33tUd3a4pgpg211nkBTl7fN6Rn3qO7MRKqWJNzrn1lBIZHov7Sdj5WvkLkF5nAmARf4ouG8nZznegINdl8Y-sg51QxLuhAHJ400mj6Bv3m2OUl_Yjlkd37lU0KRVqrUF1cYlOzP0h4IYjE5svBlol0ayvt-kgW2fWjYkey7bBk3AnJ9fjSkswKQAyZCAac2HS6vpwr_TzyShB8jiA7lB7Sasayi7yyrPUl1hLryOx4Utnt7cJ5_e0rh7vG5DnEu3pVceKKs8eJzBwrfl0_A6FRMvABmBFb1YYeQR1xtODXIOVL5xAlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔥
دیس پیروز قربانی به میثاقی: با تتلو اون جای خالی رو پر میکنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/94149" target="_blank">📅 11:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94144">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BzaYY6JZMxfHsmuOwfqoJBs6y3B2NhHvSzWYBsGc_9plhW7MJ90Mw5Bjff6Ks283qVRKV359EklipYT3D2NWDxa9VStMqaFRVnQvmlE66ZQUkDGabDTnpKenYQdXwo44r0n1YfCzHrT63IZhqdWfjbSsJW4Hq5bRK94AgnhSxv0J20Li6s8PUgyf06-0zKLya1U-LDQ3GlhQ3bIYKP_zEhl8h0Dvw-t4r2_4rNSC3rqedorwmu2KQgynjFwrxQC11FNlTWJOcZpzfKXvbn1GwIE80xgvGRp4unGCcMzd9kIA2oxxTywiCZ3-P7hRLluUBJwNH2B0ZOO94hSdG7W6zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u0_f4RdAH-5uocpB_UOAgW_8YuWuaak9oy3GdQxCTmJsEK8NjzLONetAtCb0XQzQ31RLm_kgH6GjOPXc0M675op0d7cw2OZWuovW4njmqPlwA5zK5tABtNSdV4vVHPao8BqhH_PsnPvxFpZHVZUOg4CqeB9fAwpyZIng7fQgvxV-41kFwT4_LI_otqjagIYSPAdTEcip4SzZvyYjdZnW0Ksh6zAvqjlNSBJ_U1wtSYYFuvDsdTLpNBvuT_FZsbi-6F-zrd1MyG7O7mvoRYTLvReRbHH5se5YHHHMz3h9lC5OM-cCAT4Gm4_BlP-Df4jRSyS3VW5ceFTbK1XvRisTEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uP3etKc7gL012xgilDa7Juv2DAv5sLZNpjijWgT5f91dLMhhG88EhivNKW8W4LNUD-uNjpeU3hIeXoWYnduS0kJfNCGywTujJFG9g2zfxlPQTFHDkR6X0EugWHUMKoV4SjJcy1p48SWVnT9HGP-ceJpJkK6PB-8l6gUzOO2Vl2nUF4errd7Xr3scEyFpttxgWR3kzOQzOGnlRH8cvzfRFW6yZLTh8F35RWsjLiJoJ21lv5tnJXXsVQLbr0rjI443WoliksOS3rrGZHo2j_sArFbxW9Amlh9THEKmLNc0MOT0OSlu_jz-8Q3-A3Siaue25eiXFj6oKXCmNSlUajQM7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/irw_e_3WD0WLlD_v6ZBCkGfx6RRzoljdFXPlP8-B_nb1ycZDVp4k3cVJNGNYhuvKYACgI7FNbU4NF_RzRGF7s2lYZYYwHDi-HNi_qhEiq_pD_X6e4ji9m_2gvSd5BfGa0Oczhb5O1xx7yMwjJhsX5TyUI2SqI_8bTOYaBPjinfMUF11fjzX4KpFw86gKdJfKEI5ee1CkNF0em9T9QhWE5Cppe8smvGnSM9SbowPSOUX9WJ6YxzLH3jLsHiP1fpW0V3tzhZCd2EnYqtXBVMJPVM682Gpbs3LhQanGrhH-PT8OqWr_qnsDkXHByMDpJbuH1krs3whv2zbaAjt2-aP4_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CGAskMmYLMqZjYJJhvUM_Vw-o90DajdqSt9O3vDyEWLNHfj0k8taPCtDaWrduDyICcZNg0yowPANIC4mZVMe6MLgrqkeFBRxpAAVLnZbCi_sQZQdEPz3SpKCHYMoQuZ6h7WP4v9RU-YpPMFJPJ65GfUs1wYqvLjmR3BJKDRWw0RgjurYLP8RZSXRtdUISAGl6UNMJ0S00v37rUP6HBjwq0fbJK_ImQRoul_gYB1cOuklsptnlKxpdc3xFkDx2Yax4sg5tmK_v4jziueUS4a_7X2536N-wdIsoEmsjnQRd3Rbx-KXlnrdLJYGS3Uw4L6JlLR_Tbmf-UNyWTF6GwTbRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🔥
بازیکنای کلمبیا و زیدیاشون هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/94144" target="_blank">📅 10:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94143">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8MbORB3k0b0q1yqzJUjsOfAcBZZAUOkyliAfCdLFY2gVBIg1_9VkX_CfovK5FUDertbGh7fSnK0WP5H-6PW9JRKZHAe3kMjn9YbXUNYJVin2oRB9xRIVmUmHnvDvoqAgtjnymqfsUHLidSWe3HEqrYzNjTECF1y6edCo3vY_PazM8eSl3MKCOtE1VW5KI2LEc_JukcEnkaNDsq8LWdZIvTgOsk3PIlJiVhT8RP-oe_FUWG4VJLAySIy6JupS5CtchZw8syOOzVDBhhpEyT7NOOdguS3sGbUy4emO7sLbDe5Upcysii6a0GE5X8ANmnYs7MVf5fsLLSGE5VDX1kH9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
رفتن دیدن رنگ صورتی به بازیکنا اعتماد به نفس می‌ده و بابت خاص بودن رنگش، تلاش‌شون بیشتر می‌شه.(روانشناسی)
🔻
از طرفی هیچ تیمی صورتی نمی‌پوشه و این رنگ به دلیل تفاوت با رنگ لباس‌ها بیشتر تو چشمه. (اقتصادی)
🔺
اینجوری شد که امسال یه بخش زیادی از بازیکنای جام جهانی استوک صورتی شدن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/94143" target="_blank">📅 10:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94138">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JTUmRBZs2h4J8eGLVGqqAbxyvgwnrfER4SGwjMbxmZ9eMhvlQMHDEr6cvkQGS469hjp_oqLTPw_lIBU3yIUBFMLwfeIrMbgs93zKggxch2_xae6zbulmFQ4j6cQeGD9Tvc8qN72okJNREAuvnSOEp5oU-MvbsPJ288nbwJZDWX0Rf7b11SBfkwqLOMFsq7GGAecnOGDvIG-R6W9PolsA_jS-R2HAqg7cVtceYqyiIwTZheFuiNXsPYOOAI20X1oBILt2mei3Yr5dgabl26pWAE6vOZFoE1_89TLbiyFHE-Ji8Z6_iOthQb3F-BUfkFKTCZiwgf9Ov26Jikzuq1_Icg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CETkSD-JGNA23QspEkr0R4Vh3Gt1d7N-sJ6owRCrfNfE32h_iynRDXaJMADAfztZZNdasQAGlyCt4lbfLjezZfY9qo1R8nlzTxflBvjvWE-C7ztEHi869E_D-V5sKUGFEnfjPmeG-Uav8p9WY_6FIsaDBXg4DEFfLmDtiEwLuEYhkZ0PmT7pzauQKzi2luO_39aMkbS0_swuZ2aOlqmCFU1tho1RwXp6RfRbTRS2myf3S8ZgFv8kEJ8txgvEGLeCeZUn5--CbMgBq-2Kl2SOWFazao4n-VDHXRqoi-Ga7_i-B86gp-VfU8v_7h-1qs6E_cpsNSPdoSqdmsyxZEMX0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/twHOJs6J0rjBV1O0YTT6m2zI0q7qkmDCteaQI6xcnaxqjunY1dNDOSYeHIlCcMcYpEZfW2hB9H6boiZSUjMZa5f5LhSbenT-bYrs36WbzzNctZ7s2Y6OL8G4JX7Tp9k1ikM5uBamhCnxyWUQSaZ14G7KDvIybX2Nj3w83ISmh3ZsIW7WDi0FwS2aIyPMabEG3U7anCQfRTKrsq274iZ_jz_ypjDJZqDiNioHHtLy1xxEpVbk3vPx-QeOQRWjb5VjqME6CPYQ9-cyIj3k71_YAYU4N7exQ7LJ9gEleCI_w_v0FYDkvW2GkMh2rxL0y3V30iiscwB6eueyDdM-mNbvxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pBZFs6rZKbXjrutDHphYhzW96OqibnvDcNAXhf8O8j00th6bSlv0xGPbUEdDXk-smvI6bSa6XeVBhul7g0V3TAMA8nUIT94B4mjntYP3SBZeTSbruTQDcGhGHgo1T0QBxwmI0XAMBA4kME0VDANVMKfLpCvwgBjBsB1zyb6YckQWCDQi6CAVD4yTSolP2suz4AULOg_MljmbaIajhnMtILdJsY9I8OVyzdmJF4uZXKQWRfVaLZYB2eT8fYq2r_9zHrMjXttuUShGi9wZuXd9Na4nLvCmFwKfmzf-G9kch2-j9gl5qbhPQTvRmLKxAubzs1KWFzzTtElGsAk3BAwTVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
حق برزیل واقعا قهرمانی جام جهانیه
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/94138" target="_blank">📅 10:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94137">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a99ba4fd6f.mp4?token=S3x-DKRFkVcUCgri6bVJ-DBasNzucgFvA7FufD-8lHZhpoQco_o_LY255leKJOZ6Yg7bDL_MWFFlaFM0O7gmFUKiOpiDhDwqrylh_kr3bpMwXo6znFc78i9c_FM07uLKceKCnz6tPrmwLYS1bSHu1Wn23jAAys3ZL_wFNnTtkbKyDaQkghCQ6RpX4TZuTArOijZL-WfW8BUkICD3nrIVKApvjWQqJVX0wGiTQwiMBhLyrRpUFFeS26gXbl_Y-c5ODJlZ_ZNJsfZ-g_jxGe0-Vir3MZL-CSnNjGC0MoZnqj72KeCVgakk-FgxTRz0EAqBAIq3S4sKdfAn-iqfvTXxRmQZeT_9NBVZrvlqQajJGXNE1thNpSVSR-sF6CfSfN3MsNOYJbGXXBMqvelef_2w4UXN1Ckz2kUqAkjmhkM3pv3osoXF9FE-Lxdwi_4zru2omp8HkwnpfrLAGvClOP-YploONNbtK-yEH-nlSwLhIVET1TpZzm6_sUUwF20U3fVZ-6FmDyM7n_mxI1IKRCD2xCKwsgAcG72oeXbKCPdqdp_neA-MzEBmVndmqngnQNbD1gITu5N0t8m4fr6wLUyaoUstY7y9M6kdu6qJ__DWMN78MPOs5gQpcZjJcVJ_RgKNs8WZEjTaNiucj8JgyzzNpTgeWLKRyQkHqxejNbE3A7s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a99ba4fd6f.mp4?token=S3x-DKRFkVcUCgri6bVJ-DBasNzucgFvA7FufD-8lHZhpoQco_o_LY255leKJOZ6Yg7bDL_MWFFlaFM0O7gmFUKiOpiDhDwqrylh_kr3bpMwXo6znFc78i9c_FM07uLKceKCnz6tPrmwLYS1bSHu1Wn23jAAys3ZL_wFNnTtkbKyDaQkghCQ6RpX4TZuTArOijZL-WfW8BUkICD3nrIVKApvjWQqJVX0wGiTQwiMBhLyrRpUFFeS26gXbl_Y-c5ODJlZ_ZNJsfZ-g_jxGe0-Vir3MZL-CSnNjGC0MoZnqj72KeCVgakk-FgxTRz0EAqBAIq3S4sKdfAn-iqfvTXxRmQZeT_9NBVZrvlqQajJGXNE1thNpSVSR-sF6CfSfN3MsNOYJbGXXBMqvelef_2w4UXN1Ckz2kUqAkjmhkM3pv3osoXF9FE-Lxdwi_4zru2omp8HkwnpfrLAGvClOP-YploONNbtK-yEH-nlSwLhIVET1TpZzm6_sUUwF20U3fVZ-6FmDyM7n_mxI1IKRCD2xCKwsgAcG72oeXbKCPdqdp_neA-MzEBmVndmqngnQNbD1gITu5N0t8m4fr6wLUyaoUstY7y9M6kdu6qJ__DWMN78MPOs5gQpcZjJcVJ_RgKNs8WZEjTaNiucj8JgyzzNpTgeWLKRyQkHqxejNbE3A7s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
💥
وایکینگ‌های دیوانه درحال دلبری تو جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/94137" target="_blank">📅 09:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94136">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1df67b89f.mp4?token=RsP6Jd8M1DAPfktiHJOJqpdzhsBzEW92LfLucJClZiHw0Sa0MxqxKDU3-RsR8k5v7sRPsAkmJnvTZL0s8aagbZ4LbcMrC0iWJLORj1ih6Ryx9o_8grn9YT3Um61l8frJfGSVe6cBQvxc1-A6hanssqiMSAh7AjRLKolmUMOEBd8vs8DuaUvxprCDZTbHsCIAPod-AB1o2rxe2Pa803WEEb0twaJ2OwP2xJpwjYpKzKVDuLeE5T885QZf8ZNJPk10Mpfui1nH6uBXQ5ngX7QqKmAzeMoyghHr_SaDgPuJMZ8hy1a5xJV5_Jf9cAtegk9zQ0BW_Dqy_j-jBRLxB636sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1df67b89f.mp4?token=RsP6Jd8M1DAPfktiHJOJqpdzhsBzEW92LfLucJClZiHw0Sa0MxqxKDU3-RsR8k5v7sRPsAkmJnvTZL0s8aagbZ4LbcMrC0iWJLORj1ih6Ryx9o_8grn9YT3Um61l8frJfGSVe6cBQvxc1-A6hanssqiMSAh7AjRLKolmUMOEBd8vs8DuaUvxprCDZTbHsCIAPod-AB1o2rxe2Pa803WEEb0twaJ2OwP2xJpwjYpKzKVDuLeE5T885QZf8ZNJPk10Mpfui1nH6uBXQ5ngX7QqKmAzeMoyghHr_SaDgPuJMZ8hy1a5xJV5_Jf9cAtegk9zQ0BW_Dqy_j-jBRLxB636sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🙂
دیشب وسط برنامه زنده عادل فردوسی‌پور پاش گرفت و اینجوری داشت بگا میرفت هرچند طبیعی جلوه داد
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/94136" target="_blank">📅 09:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94135">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d434481e09.mp4?token=DX_4KabBVDfb4GykVcqbmEPfTUoXnrw8-hdxGVqDKfrizjqMVDIzrZOA1995OhBH2zRQ8fh9jCrABMzVG4i9A1M96R78ciA8Fl_qnd-e4MsUB3EX-nSgjLjm8Jk5gtlrioiK_HJQ_2OMprprmUyjmP7sVvHBiyBLoPY-nc3aimyRVYUOUk0rbjJBNow-4vsS4o1-_3NGXPVzLGKRLKUMGdAvZFnGTmzLjfGR7Va4tSAekXZHrDe2LjISAMEpjv4cKqiwfUH8ZCGFNClInPn4THj7SdiDhPsRAJFvsCRJDvCjR6NU237imlTYVDifctiZkBy1mit2Tu3zoUoX178OeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d434481e09.mp4?token=DX_4KabBVDfb4GykVcqbmEPfTUoXnrw8-hdxGVqDKfrizjqMVDIzrZOA1995OhBH2zRQ8fh9jCrABMzVG4i9A1M96R78ciA8Fl_qnd-e4MsUB3EX-nSgjLjm8Jk5gtlrioiK_HJQ_2OMprprmUyjmP7sVvHBiyBLoPY-nc3aimyRVYUOUk0rbjJBNow-4vsS4o1-_3NGXPVzLGKRLKUMGdAvZFnGTmzLjfGR7Va4tSAekXZHrDe2LjISAMEpjv4cKqiwfUH8ZCGFNClInPn4THj7SdiDhPsRAJFvsCRJDvCjR6NU237imlTYVDifctiZkBy1mit2Tu3zoUoX178OeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🙂
👀
منتخب ایران باید این‌شکلی باشه تازه مورد قبول مردم قرار میگیره :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/94135" target="_blank">📅 09:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94134">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBIhvS6zeN1ewifCEfTRgdWyA2aqnX2biB8pboGMJHpJB138JEyl_eu_yfeVhU5K1gKwpZAzUTyQ5ISv4kfszZ2gaSr2fkxV831I3n1DE7-eGwtcphceoJS2jJqL3Pz3j-8rpFh-me6jOQt5VgMjyVJ5DQKPxf4ozwGW-8PiPXPoD_i-THaNj4mrLsKE6mQeh9Dmkaj0TIpzpo9RoEd_H6o_xmDSUjpSpJpOOrfYLHUd1CuDOUGfSn-CBBc6YzXG7W1092YUgnXh32ktEKvba8FBb8YN65yVoAgX7w6FAYyt4-JvVmY2BCTsxvqiqywPFgN5RyaF_-8pz1o10CSY9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
نتایج دور اول جام جهانی:
‏
🔥
۲۴ بازی
⚽️
۷۵ گل
⚽️
یک هت‌تریک
⚽️
۷ دبل
⚽️
۳ گل به خودی
🟥
۳ کارت قرمز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/94134" target="_blank">📅 08:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94133">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmqeqc7_dMEDhE3GbcENIZFfMg7loRSYvKGvoi9OjhPMCQleFisBG9EHyf6X-asNj15bC8cHr1bUv_2GNVNoUt6eO4ApO5XxZFVO0rCryPHWbkAY0JyzhXZ5DBzF3kcKEdSHHWL9eg191szpSZZzmnIl2nBIgcthcsoHIeRaEQfRdBJJcm6Ob1ppvGAwj02kd89UWiCglATOKD0OJ5TPisYpM2eppatdCn2E3QUSulJpetoTMoQj6DRTu0CpQNREKPr2biwiOtcGs91OmPdi1X4UpZp-vCl_n76JiP7B2rijb6Mme28a2g7dotaKAndBcCoo5yS4MmmYNheY652UjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🏆
🇩🇪
مثلث خط‌حمله بایرن‌مونیخ تو دور اول مرحله گروهی بهترین بازیکن زمین شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/94133" target="_blank">📅 08:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94132">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgiItb9ImENglqsvcTZV0OHNx8yKfS6cO-Z24Xs12ntCaC9K6DXGyY4vN965zl8ndFWY4Gwsr2PFdEjfeS2P9_YUPJIZqXjsItB4YZe4AfEjQ1KC9dTT8qa3gqtS3kUOn7slddJ-YfjMK56ElS6io2elBQ2m29wfTWaNXLzilzLmadA6qAGqCLD5fSQNQAy0o2a3EElNBNCmjrAnZml5kjztvZFDegBFSpDPDpUvQi2-5IKf9B7zdh3RemOI3e8Hov1OmJB4eKNXvezYAPNzVBDZjclJqDp150asmrRRRqYh_DZtSVzg8hRxyRd9lFLKCgz2G64eiPS1h8xV5to_AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
رده‌بندی بهترین‌گلزنان هفته‌اول‌ مرحله‌ گروهی‌ جام‌جهانی با صدرنشینی مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/94132" target="_blank">📅 07:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94131">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdzQzNL4c2tQLsAWXLjWYDo--MOTD9iu0H0auaUufUFLGA4XYJlh1mefTSf1WcikAW32-O-6T2UihWNFHdnyozCKTFKZ_IyG8dMCuNN--Lgpaq2ULQGTXCCDjEwKlrHOjM6P0vZcqRfO39HL5jpcZKiFN-La7spmqBbmRKvn9SHly1eXtx1TTAAiOC5iBgG5j0Ce26gMR6vyrmyA5-OvmcuPsO0TbRtht8q-nacbphXwrqWmgegG0x40mCVEEKZ7J90xIsyPEKnZ7J-bxdSN0a1heJJR1esLR_Qq1nE5_rL8MVprspA7fwt0Z0IzQ5xhkI_-K_LPBizVK3mnkExycA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
رده‌بندی برترین تیم‌های سوم جام‌جهانی تا پایان هفته‌اول؛ هشت تیم از دوازده تیم سوم مرحله گروهی، به مرحله حذفی صعود خواهند کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/94131" target="_blank">📅 07:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94130">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYauzoyjOMlbT8YB-646RWiryDveqkmYg9gQB0-VGwxbctTtgwa9TlubmYao-R0koyHJgruM1RKKmnPYtvc-BSanX07LM3LR1O1KE0m4ROjcMufValkjkAxR3_sMEt7kVOOJp3m7aivOAaUwyX13uUuQmc5QSDE3pvDEllnGL8prZ5kd-jeC31PgV3lrRD4rz-gZI8ZxP9bz4KR_AtzFfnJRLpDF7d5LgOmDwWpvJKSLUhR351l2pECeJLYq4DkpihT-6KkIaS0AREsbeMEyH7DsRw7881XQ57xLVs7NsFg6eT7GWC-cYBPGS5h1zhO3SKjzNUq74gDqx3Jw8kT_iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
جدول‌نهایی ۱۲ گروه‌ جام‌جهانی پس از پایان هفته‌اول مرحله‌گروهی مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/94130" target="_blank">📅 07:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94129">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEwmI84sz5fPop9o9zmHo1uDMbkBXE0xtqV4Oxg3JgANVCh0SNvlGjCkZNW8Igija8fUeiYLrryVYjW-h_DrAu3J5fK2HfKrBRmh-5yYgf5mvK-JH6ImMYCqW496LV8HlTiEi2xtTtR1_spqlX60sPo6JI8N_CP_QfCkLATf6l_b1v4YOmf0YovL19qBbahKPFyTRVgMzL3fSt_wEOOsEFkjc2b96uOK-KigWNz1U6OUm5b-sFzy9Y3cGOkFLuqeU2rbwy2YPFQHyz0CJJ8Sh6UBwDFd0z6qZYGu3j2QVHU2f6sNwGWjI3RiaAvf8-iDcGiZT2wKuWBJYvSsjtu5jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
لوئیز دیاز بهترین بازیکن دیدار کلمبیا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/94129" target="_blank">📅 07:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94128">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MP0eIVqf15GDpzxv-iy3MiCze4wu6Ccs-QejgB33TQPrXKwqecyRR5Ze4qiM7EtBgRrRl6EAPMoittM7QW9FLAhOvy-iIyndxN5sEETpJrxQEq75-JSVGrGeheEx0cG9YSBLHBOKvqhc_grhSZrmSo5vWULNLJ_2azj9DAEHqXZI6niI8p0ZRSM_Xb25cETgZ9mpiPjdy4FrvAwdg6F3hsefoB9tiMTNHC8-_kZPcaGWTPOXtpzCnpa1flUCf3qPJ93n-tdQTUYp89O1PTPbvFouUa5niXisxC_MX1zosgTdybMSLnUS5owj6NkV_7HA0_riKmgyPYehgP48jXIJcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
جدول گروه K جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/94128" target="_blank">📅 07:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94127">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🏆
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی رسما به پایان رسید و بازی‌ها در هفته‌دوم از امشب آغاز خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/94127" target="_blank">📅 07:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94126">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🏆
پایان‌بازی|کلمبیا
😆
😃
ازبکستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/94126" target="_blank">📅 07:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94125">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uva9HhSIhjhR-9iFyiDKQK4XHnZXnuX-5NCdPHRpV_kUsR8yBFP8Rg1O4f3qcdV1cnf-Umz2hs938Enr47FpPabHMt6s2fPxJA9TwXV5ADWqQN_m-u3Rq62CeMKWpaMHKHG3KJS5g5ilxncEVCMsdJ33ZQkJwieUJ23M4_RMgRp9S9A0_rlJS9IyCqRfhF9Gw-HY5vrDuWKelevbDXKvK5ESulPQ-3SDZg5SHFKt_WH8GyRRYCq1qgFfRpmhY993_-kMh3IPiTlJxL1Lz0j8ScOQrgAq52X9eXcrCwjxq9aRbVyIBJNDhjeDUiP_sbMhBdVA8yX44rNlzHkoScAJ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🏆
۸۰۸۲۴ نفر بازی امروز کلمبیا و ازبکستان رو در استادیوم آزتکا از نزدیک میبینن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/94125" target="_blank">📅 07:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94124">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAWbTfyUXx7Od8ITHOrHAHdkWHKc0X9o3KAadinCLg3OgU0lIIF3kQ05hmk1wfP-Jvk9F3ANY7-6JfjEWyRPZGuLRYAdXuToCy_e0rAELYef1JFnjmDnCyY9MZ38-YBMfFZ5hDg43nUx-hhEQMWLWVt9Gat1ieId_Gk657YcPg4rYDERQVtROmnJzb7OOonatDwLxgt75V9W_vF9iWfC10EQeZfvwILKo6u8xKr_00p1V8GsoT0gcSVswwb3i_KiYqdIeumM33JfMZBDmEo_lO4sb8zDuFo1521qh0gMQzPlrxy2QXs-oEA62SQcKys8UAG6pr-21lbR9-bRKp6Tkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
تصویری تاریخی از امضای تفاهم‌نامه میان جمهوری اسلامی و آمریکا با امضای رسمی مسعود پزشکیان و دونالد ترامپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/94124" target="_blank">📅 07:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94123">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0618ddcda6.mp4?token=F9Oe0Kjkpx5EQfnM0U2U3ZfRzt2aRHGhZSvSjJA0vTT5DyEEkPHMg-_SlxrTNovb7TLMNs52MnKO2XDAuvab-rOStZOv5ir4jR9mKtNXW5O5TDSZIeG-NRhEPDK0pHfgGnBatS1d14CrmQr1_QCGYuQuq-jf2BWokSfsWwBZq2qtbKovyEXWDaMRalxRPl4-2iFeQxDh64FJF7-YSPRbfcWYXlO4RPGm-Rnh34e8Yuwm3NpaA_kfvVxQySQdJ3cPboPs9hMalFzdqKBbfhl5rB3oeHL5gEa8IZrp5-SEbIKQV7iLBzlwOJCIbL5fS3pCPIy9w5BWW29keXxJPc0QnjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0618ddcda6.mp4?token=F9Oe0Kjkpx5EQfnM0U2U3ZfRzt2aRHGhZSvSjJA0vTT5DyEEkPHMg-_SlxrTNovb7TLMNs52MnKO2XDAuvab-rOStZOv5ir4jR9mKtNXW5O5TDSZIeG-NRhEPDK0pHfgGnBatS1d14CrmQr1_QCGYuQuq-jf2BWokSfsWwBZq2qtbKovyEXWDaMRalxRPl4-2iFeQxDh64FJF7-YSPRbfcWYXlO4RPGm-Rnh34e8Yuwm3NpaA_kfvVxQySQdJ3cPboPs9hMalFzdqKBbfhl5rB3oeHL5gEa8IZrp5-SEbIKQV7iLBzlwOJCIbL5fS3pCPIy9w5BWW29keXxJPc0QnjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
گل‌دوم کلمبیا به ازبکستان توسط دیاز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/94123" target="_blank">📅 07:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94122">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82ffe050c7.mp4?token=m15PrSWO8qfI_1BlK5YhXM_4wDurBo5dUspwrU3znl9AikIc9jNp3q2O8JpOgAYjuQ2JcKLU4jllb0LnmWZrk1ZMdcNgOlRzGgDqM8KBj-jw_wthcshn1tPWV3O6dMmq5MiCVt4F3a4-nbnl6rPfrOQQmy86ik21MZXffeerme7S6dg5vuYRJYD3N44-P7zuMzl2YAdTGfU9q_zjLHC1De8Tml6RurRdw2DVAoCqzj7OR-97Q5nxgPRGPa1ew9UFaOXOQFS5HLSbisiLTLSZYNCsGqteKb1tRwBkwBnrRm5bZr8zOu5GpJzrEZX34YrdoBMjChDC8th30yd3blfpQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82ffe050c7.mp4?token=m15PrSWO8qfI_1BlK5YhXM_4wDurBo5dUspwrU3znl9AikIc9jNp3q2O8JpOgAYjuQ2JcKLU4jllb0LnmWZrk1ZMdcNgOlRzGgDqM8KBj-jw_wthcshn1tPWV3O6dMmq5MiCVt4F3a4-nbnl6rPfrOQQmy86ik21MZXffeerme7S6dg5vuYRJYD3N44-P7zuMzl2YAdTGfU9q_zjLHC1De8Tml6RurRdw2DVAoCqzj7OR-97Q5nxgPRGPa1ew9UFaOXOQFS5HLSbisiLTLSZYNCsGqteKb1tRwBkwBnrRm5bZr8zOu5GpJzrEZX34YrdoBMjChDC8th30yd3blfpQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇿
لحظه اولین گل ازبک‌ها در تاریخ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/94122" target="_blank">📅 06:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94121">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">لوییززززززززز دیاااااااز</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/94121" target="_blank">📅 06:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94120">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کلمبیااااااااا زددددددد</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/94120" target="_blank">📅 06:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94119">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دوممممممممم</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/94119" target="_blank">📅 06:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94118">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گلگلگلگگلگلگل</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/94118" target="_blank">📅 06:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94117">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">فیض الله‌ افففففففف</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/94117" target="_blank">📅 06:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94116">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اولین گل تاریخ ازبک‌ها در جام‌جهانی</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/94116" target="_blank">📅 06:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94115">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ازبکستان مساویووووو زددددد</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/94115" target="_blank">📅 06:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94114">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گلگلگگلگلل</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/94114" target="_blank">📅 06:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94113">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔥
🏆
🇺🇿
جو پرشور ازبکستانی‌ها در استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/94113" target="_blank">📅 06:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94112">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c320d9c471.mp4?token=GGaLX4XWvLas0C70uZWKDsOj7uKN3PMGpVgIU7QfNBsU6oRuTn19pIpnN2Ne-5vyEkXLkEMSyY1wfODrns4wRYEmPcrbxpp17bru7tW1X8YB_lGrl5G2a-MaN6dMhFue8QToTIvtBusR_Ncfs7CTsVSr-NXMonLnXyRY2bBM9_EysEWV5bxCVW3R9tJ3jrLL4Rubb0b5ZGVjRRK_xuBhx_9UV1VeqXi23Mda6Cs0LtNHdVNiIWXQrxtG5GCyTWEhwCCpmt7JxTVZsGmb-22B6lTozB6LOEha9GHnhPdpS9Lvf2GOwU_FuYyAvfR-fX5XLeaOhdiE9NNJuIJ6HiTckQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c320d9c471.mp4?token=GGaLX4XWvLas0C70uZWKDsOj7uKN3PMGpVgIU7QfNBsU6oRuTn19pIpnN2Ne-5vyEkXLkEMSyY1wfODrns4wRYEmPcrbxpp17bru7tW1X8YB_lGrl5G2a-MaN6dMhFue8QToTIvtBusR_Ncfs7CTsVSr-NXMonLnXyRY2bBM9_EysEWV5bxCVW3R9tJ3jrLL4Rubb0b5ZGVjRRK_xuBhx_9UV1VeqXi23Mda6Cs0LtNHdVNiIWXQrxtG5GCyTWEhwCCpmt7JxTVZsGmb-22B6lTozB6LOEha9GHnhPdpS9Lvf2GOwU_FuYyAvfR-fX5XLeaOhdiE9NNJuIJ6HiTckQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
گل‌اول کلمبیا به ازبکستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/94112" target="_blank">📅 06:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94111">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کلمبیا زد
🔥
🔥</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/94111" target="_blank">📅 06:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94110">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گللللللللللللللل</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/94110" target="_blank">📅 06:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94109">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWvqtE4-FsxXc41zJr-ZeKY6-XmtYFS_FIYGfLuZdru-hRIfjL4egQDP-LSG1s5d1XVa_14GwZtQK_pVtvk0fTuFR5-OIdEtUvURWgPxxsuzQIZfnPEJYAA5xxgpyFXcACCo0QWtqi4-yAmSGll7lobXG5o28KcYbaUFaw37sXURk3pW7pXlSzsXpHIlfT8TUGddfP91vpJISlMS9M74RC8qKfPfAOgMvc5j_u2CaPfpKKXRBxwJhNZR4j_TSSWsNVMe-NYO9ZH91LUa2WydQqIYbROc1AKIky9Iisyr6lz612WBfPUIVyJEZTZ8DgJPJwhJeSW_hMGfjYGJ8yqCoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی از حق نگذریم تنها برنده بازی دیشب ایشون بود که زندگیو برده..
💗
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/94109" target="_blank">📅 06:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94108">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">شروع بازی کلمبیا
🆚
ازبکستان</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/94108" target="_blank">📅 05:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94107">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DsOEZeIdnpfvAGbxoJD5Uj42Hd9cXLFji3jw9AMNUwxpiSk0hYAi5yR2Z2TvRMNXObNXGEfkmCx71dx5JgAqdfZaBq9ZRqeBSiGPwbDh5tijW3aFqZN7ylJGWjkYXq5dR2GpbptFay74nutwyKh5w_k24E2wzSTb8tO2GGiEjJsTP4XMxuy2EjiZlHvlIXmfV5miJ2fnnzdTl3v8gJjqSmeIx_JYSIQBenuAY8yDHGDkHTaVrVowcUhAQvWK6elUGwyIQVV0A_WEjEFGmo1Ic1HqPxraBcZ-ncd_GmzlwUiXKSumnOg7jGLs5Xdkz-p8gxGcPF1Nl_dpbIksuTSd_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویر جنجالی رسانه‌های اسپانیایی از کص‌ خنده‌های یامال و زیدش بعد ریدمان جلو کیپ‌ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/94107" target="_blank">📅 05:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94105">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xd1YHz9VefHPKg4bU-L8R3INPmoBMB0NDV1k3W4rGe3k1T8iHVWhHaEyIlgUGOc5Z1pT2AW8TsJxyraQMmWNmCj3lv4iELFd917GIaHjVU6qCKQiN8OhPQtuL4zowILQL0lODjhCnxb_ptTlGmn7L7CATe7q1mrRt2XIFnTitE_YkVp8Zb-oITgcZXK5Um68ATtt8x1GdymIajiwfW3EmQlDJ5cIU0DGgDXnWOUiVTUz7H9IrvuKY_nnShG7de1pTAzvMpuyv8LKz9icm7EW0otZBG9pKh_9h8s57Oga1yaSeVh8-tLfUgUDm61OLAl5pBvMJVNl5XwZbHH-V6eYcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nxXHZiFa1AirF6PaYEISpEvDIEVKY5oRm8yWMrdt2ve_7c9ri_-AMXZ-Tr_SusZudjxToWR9d9JoNLGzmoUtM4mrHE-wrstZnYx4RQlfaVS_mhmL24DmnZQd8ONeuT78SoXse1wVYjG_0F0xC81uctcC4K0JYpiLrgTw3wMgoVY2ZDG9W6uieWw6K3rfEWAn-01YhXNo9LzM1SvIIjZSswbo88VUP_9VIvpi74iZh45rB6Mvmndn3_ij2Z3gw3-VgVc0ppDARdvMmjw3wXKe0CRA5BIeAyGbT8Nf8ul-OJwvtKpLYmQt3Rrql0pBTL4PUxgrRT54OTl-lDDnpt2gQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">2014
✅
2018
✅
2026
⏳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/94105" target="_blank">📅 04:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94104">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4VEiUL5uGnWIVbIIA3U3GxO7QiFHVUdCBtwokRjIIRv2YVKVtyauCFkEm0H4ldqf9zXyXik8mm_QGfjxCBu4NxK-78Q08NrQoXJtxeSh45Sz_rVbm0uCv1GPAj3at4NEIe84I2HsZ3YGW_IL9-m09_fe4hT369BrGUHliyXaIFr6payZYIfDNNuxXYmz7olScFuLDDsIDNslEU_kagxIjUxWImNyYhR_byvQHviO2_bfL5UKXVn8VnYVJiqPIsbWHF-u8Eg8cniiLBxS20DVYdvIHdNZs4mmrTkaZE3AxN9JqFjQTdTVxirsaiM38X3ze5RMAK7c0cuO-JPN68umQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🎙
مصاحبه روبرتو مارتینز پس از تساوی ۱-۱ مقابل کنگو:
🔻
نتیجه خوبی نگرفتیم اما ‏در جام جهانی هر اتفاقی ممکن است بیفتد؛ آرژانتین در ۲۰۲۲ مقابل عربستان شکست خورد اما سپس قهرمان جام جهانی شد و اسپانیا در سال ۲۰۱۰ مقابل سوئیس شکست خورد اما سپس قهرمان شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/94104" target="_blank">📅 04:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94103">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPBgTyfKGe1I4oQcaYS5lClFbKJDG1rzQ7XjPm5iHgYrk7DXgEfLdYU3VDIwY4C-MUbdaIX3FmZHGZOehXlPGdbBZVutBgHT3QJ4xYNanDFHof7xNb4it5Dg7OJTRRbaqdYgYe-EF4DwGWwJS0fRdfXw-zHYv1Tm6mtXrWq6hqVjbojx5C3CZFyK-M3LDDdxlE_YF3lZz9cpajiIsCSVy6OzK3q5UOzcTkbDwFPpxXD_i0B2RFVMBegIVQJAZ0CSbzXgwO70J1ppz2LkVs5x7VtE5ilVgtzfBY0BDfQ7oGtm3izrOuaYyyIvfMlKczk55-DPJcEfQqV_a42tmaAP_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇺🇿
ترکیب رسمی کلمبیا
⚽️
ازبکستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/94103" target="_blank">📅 04:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94102">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTTuo7I0twDdOvuzXCnYTcUu4oiK_busTD84PmjAeAy6JCgt0HFN0lKIxQ6c8gWWJP7SkyzcoiYz79zmHyGzpdelVIpfUD2V0e_4JdF4AbfB4PO4v10jTQHJN7soRbULkLAB3e-yEoJWYKPtPs8lPYvRDjqtMR2AF0hZtsOfGTd7nOADuP7ejXHejjbWx07D49pjPlhFQcEXOA0KYrEkPEYyK8kykMJEag0PI3vNrRt6J382YyHZ3dw-BM8VsOSseLN-P7-cNa7IJabx78MvKjvZWiaOpO6FsXWtL5GoFzzUVvjYj83Sx2No2d5PVEeegWbMbtSo1lb1CZNh2VnLlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه L جام‌جهانی پس از پایان هفته اول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/94102" target="_blank">📅 04:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94101">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nicd-cpmh3ss4CTuAGa5Ch8GMzxxmkG_DFhzAQlmVe2vsMbvCPBnsbV_1mRpR0YSRjcDV0Ao5iXMYDFk2EwgJp5DKKNHiz5c65PuRvGGITsPUEEaPLZyxv2AUva1HbTMEwRb-F9peIpzYMo4gkp8ky6MCWQyXwzmX8_QQoyp_xD5DGiLwX30-oV82wa2SJrtQY_simp2i_Wk9wrtu6ndy8fMqoV9dOWDf9GdLmSU5WsiPsFLHVkyjFENbTTh8p3eEKPhyg06oyKhwUoGbZO4aQvUpEMquCzNgu6cSzN32Qk1rXngav9cGLmMB0p_J5MZos4_wCkr6a4ifp68Nu5A2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | اتوبوس همیشگی کیروش با گل دقیقه 95 به مقصد رسید.
🇬🇭
غنا 1 -
🇵🇦
پاناما 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/94101" target="_blank">📅 04:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94100">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1bb7784089.mp4?token=pV53Srx69Jd5gREB4jWF-Q-pQQrWYxva4OetINPCAE1qTlJyLQWRmDnWbCaNcBxleqGUnmUg-Ht3R1HDlKqzzbcrN8KSFr9P1_9GbeqHCdTfz1KBDYCEGM_hbRAUsaXe2DHh4h5v0U_sD7RlyoiB1unu8GeK2kowuZZHaTPrVWIjhdrvTqp7NulrK4YEOQrxKn3d5_q-UJV007e5y8z3cZgsxSqpAG7YhDNPfRHqC-G0HA-P463hLzxAhQkoYjJtCHFDVMKqxhl2oyK9pUggJIAPC9jgJ-w2shvqmMFR-qSMrV-d3ZuyJ94g8tUPCvjGggD8thn0H2glit9jbKpb21rG56a0nX4l3e_H7Qc93BqP8E8uZWtQw4F--itQqZW0wGfQYwrfJl46_6jY4qGygF8sV7iyDF8AtAgIMj-7Ew4oi0sRTqg3qTsn2MNipkMFaPhZa3bTd1fF8f5tok2COyE-criLSthA9qjttWs8QOqivrHNAEjiI-Tq0uEMiv192amqcX-qnJt7zdz_Bt5TFcI-xQpTJeyZ53E_cIICcpLHxRhsbDwzTUteDBjECULKBC7YcIQT_-7S_TavQ2sOXVAtc0pZTqlf2BwiyoS3y2s4T8uIuDGSof-qodxazd5h-4O3nE5w-FS3o2O7Ec3tg5N_ECEu2KvYqSJCFdX51Do" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1bb7784089.mp4?token=pV53Srx69Jd5gREB4jWF-Q-pQQrWYxva4OetINPCAE1qTlJyLQWRmDnWbCaNcBxleqGUnmUg-Ht3R1HDlKqzzbcrN8KSFr9P1_9GbeqHCdTfz1KBDYCEGM_hbRAUsaXe2DHh4h5v0U_sD7RlyoiB1unu8GeK2kowuZZHaTPrVWIjhdrvTqp7NulrK4YEOQrxKn3d5_q-UJV007e5y8z3cZgsxSqpAG7YhDNPfRHqC-G0HA-P463hLzxAhQkoYjJtCHFDVMKqxhl2oyK9pUggJIAPC9jgJ-w2shvqmMFR-qSMrV-d3ZuyJ94g8tUPCvjGggD8thn0H2glit9jbKpb21rG56a0nX4l3e_H7Qc93BqP8E8uZWtQw4F--itQqZW0wGfQYwrfJl46_6jY4qGygF8sV7iyDF8AtAgIMj-7Ew4oi0sRTqg3qTsn2MNipkMFaPhZa3bTd1fF8f5tok2COyE-criLSthA9qjttWs8QOqivrHNAEjiI-Tq0uEMiv192amqcX-qnJt7zdz_Bt5TFcI-xQpTJeyZ53E_cIICcpLHxRhsbDwzTUteDBjECULKBC7YcIQT_-7S_TavQ2sOXVAtc0pZTqlf2BwiyoS3y2s4T8uIuDGSof-qodxazd5h-4O3nE5w-FS3o2O7Ec3tg5N_ECEu2KvYqSJCFdX51Do" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل اول غنا به پاناما در دقیقه 95
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/94100" target="_blank">📅 04:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94099">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حرامبال واقعی</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/94099" target="_blank">📅 04:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94098">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اتوبوس کیروش آخرشم کار خودشو کرد
🤣
🤣</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94098" target="_blank">📅 04:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94097">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">غنا زدددددددد</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/94097" target="_blank">📅 04:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94096">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">یک دقیقه سکوت برای اون دسته پسرایی که بیدارن و بازی غنا و پاناما رو تماشا کردن.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/94096" target="_blank">📅 04:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94094">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ct7z8q2iZ3Y1SfT_OWON3NyZDupxtZ_HK_TxMdJIg-cCmmhZj2SZmiU6WWbLRyrJpp6Mlmy5l7lLzZnnNGy2MtMxTgpT2peo_jfejY42Zm-pRuF4CEhmSH9lyJkGNVq8wWn0drOr00x6HNvVtrRTrMwX2uINyZT9et0QFG1QthRs-vMu9Vu8ZrhZeIEmV1ykxAUTK696YAZdCmFPkvdC8nfzk9AtzTECAY0Cu-eaz6dXrVx0ztxqx5rSQr8nbEixD5fH07kZG4zVaKhCjj_qyDhLZqthcIMfSDN82twcz0U_hRhaklkmLXbNWISycNgKUxQ6l-8vt4ujGGr7yWUthg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CFDQscHDxQUs46RbFYu_BMLc0I1X9CoyzKeG1yIsnC_8GDOTr0FfMnfioJLrZcLvUEWm53DPRnGOPRRAZTiLCTsX1mrZnaQ0wb4eCZcUhEEzx9ROVSxzl-PBiF91n0EdMCDPDIPzd9bs_xEZovFtTxBVbS-SA7xHNKqEBVHj-AIcCIDW66V0s5jEjn4KZulcFhUEDEcMO601VNJcvsN8OO845cajcExeNpK3b-JfTOIGLogY6Nl1B7fBRmPjeg9Tx2vIicQNFiBaTvNWNuIdqXtQUTfW60m8l-HoYijlZYKN-eUuKdSuVhvAm_Hb2HM3-kGpa6sgJL7CmIbKUs4lzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇨🇴
🇺🇿
ترکیب رسمی کلمبیا
⚽️
ازبکستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/94094" target="_blank">📅 04:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94093">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb68696e35.mp4?token=Nosb8PVyXrmM10Zqo0ZtKNlDXLCo3PyRVDrxV-GfwiIsrAqxf6fWAK1GtO5gDjuCGg65y7R6N5x9i9SUcaozRElq1Qcn_JF76wLI0b9sg4Ob0XQh6xRKsMNUEl2vq2gNH-_ysEU00K9iNGpZYOdv3p2BYHJ8ehm48IEqgIm--1FZxvOJFArjixWiZ7pPFJq4FVU3qFIdt7J200kkqNGWZTlBdf1u7_icNnifvm54nuDogueyzv5C7WjTTKZcC-rQbWoIQRxfez8avFUvv41CS4ZOM0BKdiWV4zZd6-7mxwOkkP51cMGi5jsa_KNZzfQsIqvkGvoCpLceUkutLtNgjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb68696e35.mp4?token=Nosb8PVyXrmM10Zqo0ZtKNlDXLCo3PyRVDrxV-GfwiIsrAqxf6fWAK1GtO5gDjuCGg65y7R6N5x9i9SUcaozRElq1Qcn_JF76wLI0b9sg4Ob0XQh6xRKsMNUEl2vq2gNH-_ysEU00K9iNGpZYOdv3p2BYHJ8ehm48IEqgIm--1FZxvOJFArjixWiZ7pPFJq4FVU3qFIdt7J200kkqNGWZTlBdf1u7_icNnifvm54nuDogueyzv5C7WjTTKZcC-rQbWoIQRxfez8avFUvv41CS4ZOM0BKdiWV4zZd6-7mxwOkkP51cMGi5jsa_KNZzfQsIqvkGvoCpLceUkutLtNgjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
❗️
شعار مسی مسی هوادارای کنگو مقابل رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/94093" target="_blank">📅 03:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94092">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a621f46e4a.mp4?token=ij1ujeKxoDqsnhQE079U8-b_pNhangljC8lU0lVI3PCv1xFLj1_xULgYEiaWtymNZa9ia-YBoePKDYo0HAWsxB0huGlzLi373QtPDyGTC6O9Sd-M73wzRP2zn0AGUoL8b2BGNccJqP5LM8Yq9nEqCDakcV50kzrSnlPz4o6_VYEloU9GRhjFVOCAWar3WiOdYD3_QtqaNhHk0iY0USJY7-gsb-rl5bKXGweXG4mqUjtslYsROMYkMcBApawgxCO5hV2C7MQrpvXTWIJEqVavSbXzOe8oTNqfUKcI5ZSrAnr1ynoPEongedK-0BpAWLfhe87ADlILb-4aWcgY4XHkPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a621f46e4a.mp4?token=ij1ujeKxoDqsnhQE079U8-b_pNhangljC8lU0lVI3PCv1xFLj1_xULgYEiaWtymNZa9ia-YBoePKDYo0HAWsxB0huGlzLi373QtPDyGTC6O9Sd-M73wzRP2zn0AGUoL8b2BGNccJqP5LM8Yq9nEqCDakcV50kzrSnlPz4o6_VYEloU9GRhjFVOCAWar3WiOdYD3_QtqaNhHk0iY0USJY7-gsb-rl5bKXGweXG4mqUjtslYsROMYkMcBApawgxCO5hV2C7MQrpvXTWIJEqVavSbXzOe8oTNqfUKcI5ZSrAnr1ynoPEongedK-0BpAWLfhe87ADlILb-4aWcgY4XHkPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: آیا برنامه خاصی برای مهار رونالدو داشتی؟
🔺
آپل موکائو بازیکن کنگو: راستش نه، واقعا نه؛ ما میدونیم که رونالدو مثل قبل نیست و مسن‌تر شده..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/94092" target="_blank">📅 03:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94091">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aF5yXEBCYAFVBdW8QZA5XCKSwqxlYBDqQgj9muxR_S0HMKb3wgXI5tWXF-rxjcbU_Mhmfdm_npPbbAEKXBrZsw3KxDEC2IMOMNb007_qs42B-maId_quw4S2NUS2m24R9nBXY_RykseUu4ck2GcMcAr3mFTyvaZjfMh5bvzMV_DRfbogGM5Xm_N65kQfUU4rVHErc4UtsVxHp904D31dVY7mFRzgm0V8GOCRfikfRhf5BB88zBwNVyqBcsTBHvZRXCJoJqNItXjb1uk5RDw_TxjN-XvDn1tUfd4PTP9g8eOwggWS_Ys4pZwGOgXOTXo1nidgbYrYbX1O8uJZpBeH0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع نیمه دوم بازی فوق حساس و جذاب غنا - پاناما
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/94091" target="_blank">📅 03:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94090">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">شروع نیمه دوم بازی فوق حساس و جذاب غنا - پاناما
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/94090" target="_blank">📅 03:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94089">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0SPD0o21UGM78xnlR58XYwO_FH2QECZcGSUIUUh9W60T0LBSU2OrWx5Lw59F6M-E6vGj0_43oz86vkFM7OZlqIIw94o98X8RkN9QiucFPYvYgvlrBN7q-syc57E9ZCfUZnKa3piyHg-b2LZT6euUjOy27htegTnpe0x-czuDCnedjhUWKf6vhWTLP45IQwoq5qjuGpkl2ARtVcrZqQpGV9eH3lLUw6ceOs0jUbE-NIBBjSahdRiU3wznF5PKTUbR5gWFlusYVyjGd_T6hxLXBnyrHL01aKEoUMZjEaXP25FyoLXYJ7MNk5jA53QUbK9N-_9giYq33xvPzi64L6bVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📰
#فوریییییییی
از رومانو:
⚪️
رئال مادرید رسما و شرعا مذاکراتش رو با چلسی برای جذب انزو فرناندز استارت زده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/94089" target="_blank">📅 03:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94088">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a6b42281.mp4?token=jqtJlXUEMCsgAi3jJlBnoud5eqvg7Us00UOP_C-4RRf9HyzbIwXvn5ZiqNC9R_yA_H-XQXupde49WtFTPbtnbNPvAWreFkZ1awUJtU9js5PzTSR-SYzgSGELFpy_9Y-k7nGHK5AGCBHpbid9WTo0oykyenfJGQWwVravKuGCXcimd4QF8EyrH6N-_5ydpV-tjYrY65tRJ_W18eNoSINE0QhBil4Cqb4TPpx5XL_9TYdKb6GGTQ6tFmqwi43r4KCdIlaZj3SNozijt_S4MYtNi5wm2mG7zM_8ilUDlwEExMLij8oaQ7wrSQYOyQt3beXtPW-RsqtZIXZxr_tDbOw59Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a6b42281.mp4?token=jqtJlXUEMCsgAi3jJlBnoud5eqvg7Us00UOP_C-4RRf9HyzbIwXvn5ZiqNC9R_yA_H-XQXupde49WtFTPbtnbNPvAWreFkZ1awUJtU9js5PzTSR-SYzgSGELFpy_9Y-k7nGHK5AGCBHpbid9WTo0oykyenfJGQWwVravKuGCXcimd4QF8EyrH6N-_5ydpV-tjYrY65tRJ_W18eNoSINE0QhBil4Cqb4TPpx5XL_9TYdKb6GGTQ6tFmqwi43r4KCdIlaZj3SNozijt_S4MYtNi5wm2mG7zM_8ilUDlwEExMLij8oaQ7wrSQYOyQt3beXtPW-RsqtZIXZxr_tDbOw59Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
توخل حسابی از دریبل تر و تمیز بلینگهام تو بازی با کرواسی پشماش ریخت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/94088" target="_blank">📅 03:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94087">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پایان نیمه اول
🇬🇭
غنا 0 -
🇵🇦
پاناما 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/94087" target="_blank">📅 03:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94086">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کیروش این جام جهانیم اتوبوس چیده باز.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/94086" target="_blank">📅 03:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94085">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzhFZ2KvQtvpMlx2SZZwirCD-Q4F8tGtT8tr1KGdLpa7_qS-1LJtH2T05fe6gh27MDGXSnmXszGRNo5wZIDmxPRJW2c5yHYfQfxeCGpwPMVvh7UpAlscEGWjOBqTYffycEYVwKMA4TQvLyOI4UAdoFbVqd3CjUXE7a7MXrXvJbl68djV3_3OdzVzaj-IYNZYfqlo2udMqoBak2-PkHYswRzVfViZ9U5yiqS1dJdfagTBslG7ATbZomQ-4R7e3fs5oh76XxDXmHoh7guB3tFsFv0bPi8tf7j44ts-FjiadZIS6TXVT9hRebC4xVVVgVYMsfb4sBArUIfVA9NoaRpMjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
طرف حدود 800 هزار دلار روی عدم برد غنا تو بازی امشب بت زده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/94085" target="_blank">📅 02:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94084">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بریم برا بازی تیم کیروش و رفقا</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/94084" target="_blank">📅 02:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94083">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f241bddbcf.mp4?token=Rq6ijluDOXVmbT-seCxNPR8EffIzt8Aw5n5v3Ewr8E1I_gebqwpFNSz5hCT2ld2iWYrqTMCL-sFoIWxQTsaNW6G6ORqLoHQhO8iDNbkU_EhsGTq6ww_Xk8-yDJrYgp0YXD6SK2xKCVH-IR0EBzkTXDexrSFo3qrE5qqVZIB-Aswzkm4ywI3_00k3xGRwsnNLqstnrjhPsPZVCdenfD0NIvUkshz-Orf09QSt3yPocUpzx3ZWOs1nQxwmVN_hGSu7jJ9FLpIlY5gyp0N4GkOilBtLbVEESjX3_EFpqQSYc4XXCQhiS3zrg0S0NekayzXxCEHDMXBLxKaeIQSBSJ3zSXbKYI5e8yxlgB8GeNWJtneuoNK0cDYqlcr28O9AW45uBnCqckjUpuAneE-Beu6YCjeNOfpuNt4aPQpYSDAsWXWtQNP1Ujy-rPMxGSyMjTyBwwNZnS69egD_qzpb7h-X2o8jV0h4yCcf7NAqo8PEd78Nq2pkfwyUPHyCKvv7oglrePWsRH5ha2_LQLcE7-M-gsXCHVqK4V9wPnC38UNNj1GqIj2facQ-2eY8ADQKqas6F42BBgECQlUnoSijECEsZkgodwSTA9Yg5lMikD27dGMUkjnefdrEhu5NrXKpRCUsB2VYAAYLCtZalVTwdjx2xbn-bp4x-PA7ytKVTz_cDjE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f241bddbcf.mp4?token=Rq6ijluDOXVmbT-seCxNPR8EffIzt8Aw5n5v3Ewr8E1I_gebqwpFNSz5hCT2ld2iWYrqTMCL-sFoIWxQTsaNW6G6ORqLoHQhO8iDNbkU_EhsGTq6ww_Xk8-yDJrYgp0YXD6SK2xKCVH-IR0EBzkTXDexrSFo3qrE5qqVZIB-Aswzkm4ywI3_00k3xGRwsnNLqstnrjhPsPZVCdenfD0NIvUkshz-Orf09QSt3yPocUpzx3ZWOs1nQxwmVN_hGSu7jJ9FLpIlY5gyp0N4GkOilBtLbVEESjX3_EFpqQSYc4XXCQhiS3zrg0S0NekayzXxCEHDMXBLxKaeIQSBSJ3zSXbKYI5e8yxlgB8GeNWJtneuoNK0cDYqlcr28O9AW45uBnCqckjUpuAneE-Beu6YCjeNOfpuNt4aPQpYSDAsWXWtQNP1Ujy-rPMxGSyMjTyBwwNZnS69egD_qzpb7h-X2o8jV0h4yCcf7NAqo8PEd78Nq2pkfwyUPHyCKvv7oglrePWsRH5ha2_LQLcE7-M-gsXCHVqK4V9wPnC38UNNj1GqIj2facQ-2eY8ADQKqas6F42BBgECQlUnoSijECEsZkgodwSTA9Yg5lMikD27dGMUkjnefdrEhu5NrXKpRCUsB2VYAAYLCtZalVTwdjx2xbn-bp4x-PA7ytKVTz_cDjE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
▶️
اینوووو اگه نبینید امشبتون به فنا میره. خیابانی یه کسشری گفت که مغز خداداد به گوه خوردن افتاد
😂
😂
😂
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/94083" target="_blank">📅 02:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94082">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc078c31b9.mp4?token=oXrrrS3VYNrKwQr7urCTFTN4403GJNR7bMkBcRfjy9VuK6M-TDOKfbSoDJl8VXZ1qNa8fWcNgo4wqoJ-hQt6JLKsvwxdx-tqND8ms4luq0lxXlWNrwAQCIZz4T1HQo-J3B4XkeVjHLaC6-xPB8br_h7nsOxxBhGCE-0baiau4UbOSe_-pW-NJuQ4ENEYQ8j2o4pIWjZ0AsIzWDyvcuz0jwuz3y6lnDqShhapB0N4IKlch5UP_JllNxL2FMWQJNtCgLkho8ArQBRvHyxQrxOASz4tPcKkau-8z2IIPJy6RC0F8sYiOK1_MPppforuyrFa5YiQgbmYNUjec2acNFZC2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc078c31b9.mp4?token=oXrrrS3VYNrKwQr7urCTFTN4403GJNR7bMkBcRfjy9VuK6M-TDOKfbSoDJl8VXZ1qNa8fWcNgo4wqoJ-hQt6JLKsvwxdx-tqND8ms4luq0lxXlWNrwAQCIZz4T1HQo-J3B4XkeVjHLaC6-xPB8br_h7nsOxxBhGCE-0baiau4UbOSe_-pW-NJuQ4ENEYQ8j2o4pIWjZ0AsIzWDyvcuz0jwuz3y6lnDqShhapB0N4IKlch5UP_JllNxL2FMWQJNtCgLkho8ArQBRvHyxQrxOASz4tPcKkau-8z2IIPJy6RC0F8sYiOK1_MPppforuyrFa5YiQgbmYNUjec2acNFZC2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🎙
فیروز کریمی خطاب به بیرانوند: این چیزی که ما دیدیم خیلی هم تنگ نبود
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/94082" target="_blank">📅 02:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94080">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hdR9XZrE1LK7gAjWGR3T10fOzJTVKwOlSYP4gn4WkwabDw_VPqGTq1BQxInkolxwocJ9bU4Aezi4ZUyyKHSZ83eRYWw5gx4Px1ZkUITSrryqYC9a7jWohk9TFkbdVwzrhM5U5kZo7vM5LcdVpenIsYOK-Q_5WAJDtpgpwCMDVeVD0V8Ga1K9SRGw59qrH6VRYdB0a3bmo0Z3kDUzed_hN-WuPEuBviAoEk77u7FZ4Or1POhhU5rPE4IlAhG0an6ppyKIYXXjhAS5m5xOw10az63AZVwxvKumUZnNfRGRm5X1rIygzO6LSd9_pYTH1mehvpnRbyzJ6rbgcF29u9RHxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NwZ8RTUV30hUGQgQQU3_dPPPp9Qf1VErbEcNcQn2Us85K99oxSTHCXqn1dmvT_GHzRVgG9e31TkG0gKbGzGkUD7WYbl2annxeN5zyf-T4giYkreFDnUOUDLK5VamxtTA4WINJcqrg7NoDYr1xrxOh9esU39XI0EvHV-UN9AWa2uVjZuB7GGMgf0ZN2lTSj1pS6zgAtnILXMv_8FAAmHkCKWb6h3RRmxOVw0wayyE01AUCJfZ3XuUgzIpILO0PNPeROk_iQXCL-nm4IXPTMLOPyiKltS5lMTa0g-3xNxkqTAOdq9EtwFkdH7NL0AHXtmy3a34-LWN2zygunkZoH5izg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونالدو با ریدمان امشبش قشنگ خوراک میم یه عده رو جور کرد
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/94080" target="_blank">📅 02:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94079">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IP7aSWWwif9WE59vhTpraQY3-cEraT0m3cGtRCQ6zXfZiErJi865JZcKO90ZJpIgk5b7WX8iyrH6OWYWUXRTwr192t4nE_E40y2fuAf_G9u1_6NaWAO6XjylnWmCF_ABKVbZlHoBa-_77oMdqLyApkM4HkBW-FUjoSdziM-qCDeRU1jQ1GrVFWGLqt_Ru-5WXiHO1FUvGCvn-0q0tNfbv0yl55awGbt544MeCDh0jSAAEGBcLFVA8VCSbSoIb8JDyA3oUv82VHzb1WFtQOGChtwlz8USHEFsC2-KOre76p44H5_ldVjdN2mTNzjQjtVu1kMU014-2KT-BpSWfBNh-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فوریییییییی از رومانو؛ ویکتور مونیوز به لیورپول پیوست.
⚪️
20 میلیون یورو از این انتقال به رئال مادرید میرسه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/94079" target="_blank">📅 02:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94078">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3VHgC_wpAXIZDmUbiMscCIm1x7UWB8yxFrnNw_65fWE6hxnPW8r4J8zO8QTr9Eqo3bmwvpblPagKnMUO76jmT_hKNUSXRV3_wP96h45qPf5l8Rg2oYzPtOA5cK74zEkWmlr57g0Y1mEa7ezbHPAAu7oLDqqkehmGTjKLHSHhPJG1IUymMhHDtFvYwqfvOt8sUPagFjYFFkev11uhVZJSXwJmxXp7iQPixeP2-G9R-sdGPyEJ4IlQDYP9j7hg5Xfbklu2XLU6k9QYp5zeQn5-fP1YyX2u4FMLyW5lzRE1fN4_93mfxM9rsCol32SwRnoxXZD4jAELrANpuQZn7YE8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
دقیقه 94 و درحالیکه انگلیس 4-2 مقابل کرواسی پیروز شده بود هری‌کین به این شکل خودشو جلوی شوت گواردیول پرتاب کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/94078" target="_blank">📅 02:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94077">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WojZ5jXWPJPe4Y0hKr7w603mDR-tZA8TGrcGVAK6UJ6MwWcyYi4dlLJHqkQuWsqFrcGKwBp0-T6j1RsYvXtqLUmOqTo5qgXx7YKfrzHcaZQjR4rtN6N9TcOkgIqsTUXSwZyuI7jMfxQLqJyPIpmX2veopEwnA1VAXQyfASEQ-l8QBIPABCFgpiuz4DHe612ECAvf2w6ZLI_kWuHYEkXLdP-NOGIp2C6RMAfhrNoQRJXMhXPuKKcUfXesg37sPwnpqBqjVIBgk6zogzWg02aCV5OmQWOmjvGBSPftkaJN2u8fNYEHDQuqDzU63Lzb_EEHBZWJ4ffJeEyptKtI24g8DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏆
انگلیس برای اولین‌بار در تاریخ در سه جام‌جهانی مختلف بازی افتتاحیه برنده شد
🇹🇳
2-1 تونس (2018)
🇮🇷
6-2 إيران (2022)
🇭🇷
4-2 کرواسی (2026)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/94077" target="_blank">📅 01:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94076">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfvfqByXRglEK5IJ0z6QDRdemRucmWceTjZUzM58TWTdax5Q_7trhfGCJiERciu-PkjSLvqPg-pMrNFBByqB-hpomkRO5XxG8jtgQQRPtPg67ebL24Ec3vqJA4iYI32piG-oFCAz9JAs8l9IOMSNZgvUmwWHREWidQUxH7on-jCYN9D3WG6m1zC4p0Ns6hezpsxp4DBOhZY_lKHX059QN0YBKZNI9CQqKjUffuflxd_LRjHkWiEyktqNtscvQDZ2nXdnalfPCJIp7yLOS6LmYAxvLJkJqgivlkREUuzj1v25wbkaUMR7guMs4kV9ZKU280OjQTCcEHTyLNNEOSo0mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه یه وقت فکر کردی کصخلی به این فکر کن که بارسلونا بند 30 میلیون یورویی رشفورد رو فعال نکرد و به جاش 80 میلیون یورو برای گوردون خرج کرد
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/94076" target="_blank">📅 01:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94074">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fd5R9rJzLRK4PJoEZqviFSD2NC_t4YE8CYaZpHSMPyM_-_74o4K0dnkndTMp-GmTqj-wMgbKiNR8uqdnIOkWRuKVF-jqMxCbRCgS42lC8lJKMuGRxLIiRh1MrVOvFRRLpryaw9uir5Yy7C8lWUvgQfzDu8Xo_Fl7DnRPX-dlYjndfP1p4NWZgW4lXlezYWeggVWPZwdoflLNG9OnlsJzgGiZfoM4Wu4HYV8peYond2SzMyMvTWANLAhM9URvUn8EBCvJG3SMepiG4lW2fJ3f7-X1CdSEjR39bEDYZzgGRvxebxe_yrDHxeEyS1vfkvPDa_dXM1Al4Dy7dKc281SyLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/elYaOu4sqb4FyN2YUFeX453AyowOQiSc8iijhLFYC9qV_EbmJr6pUQWy4L6w2veypIIjKFidGODjD6uz3NNonT97N6TqqLxbaXx313c5a9hgtUHhN-ypoqs7QpvkkD0hyk1ARWDP3O0VMJDMXZ571H99RjlS-VdPgDF54m0OWQM3vLUeVSRyFjIFHp-sexJ5LtRKj6WJNwZXupO0iXXopcGkKdnMy_L07HSgMs_Ge7oECTMW1LJWqeTXkm0mvhB4TwmU-wJqDjCUR-elAJuN-n1uQaVK5b9XAZ_Kdgjku0XpkCD7T-DHcQ0H7b_mIuMd9lo1AIr03FPdy5iogPh3WA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">داور VAR بازی انگلیس - کرواسی هستن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/94074" target="_blank">📅 01:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94073">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q70DFNdi8WW6DLlolVevkFgZf-S1BWU03_Lo_6h4mxm-laX_EUg5h01NNrHkCbJmR7Zha0JIFDI9XW-6s3Ic9eh5GnCaDbUEZ81wzb5RHxnuRYz0qSPqP3WazoISRx1Z7fC-cVFhTrVh6n0FrYfAOxZnfYsw-b87NLdIyn7lCGv_YXK63BksolILERo78edl6TVfnN78Ia7oeQU334C8Vfqky4oiYvvFafOMFjyuErgigvdrN95kcT0XOj6wj7WcVhqhG9KsJBfsfbRMB-9xIG2lNr9PSizC2JsvqnnNPdpkj_DtlWYJFnZctQTnD9qf2ov7tdLuRSPDsEuaud4OFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚠️
دارایی‌های مسدود شده ایران که طبق گفته منابع مختلف قراره آزاد بشه:
🇨🇳
چین: ۲۰-۵۰ میلیارد دلار
🇶🇦
قطر: ۲۰-۵۰ میلیارد (شامل ۶ میلیارد بشردوستانه)
🇮🇶
عراق: ۱۵ میلیارد (برق و گاز)
🇮🇳
🇰🇷
هند و کره جنوبی: هرکدام ۷ میلیارد
🇯🇵
ژاپن: ~۳ میلیارد
🇺🇸
آمریکا: ۲ میلیارد
🇱🇺
🇴🇲
لوکزامبورگ و عمان: مبالغ کمتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/94073" target="_blank">📅 01:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94072">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4wrcXkvbSlJ1ouRPRKVU9JVYr36e5lcXtVIFGNPZnrCf_vN_AYRvDuXSAmsvO6rRs06Utv8ZkqBxaqJgFhLzDeOsx12irNYhbf_WcbS-DD4QOwFWPaij10XnEFKnnLC2FOHAAUdL1kYA2_EYeijcA_-W7rJaGYDQ18KAkTz9itY2im4cGbzOPNrVhdPRrupg99pbyU_a189navA6bXHujVYUiWuwMfz_bJE7Yd345a_SmhA_YZWZxx5lpnax7sUVLmo5NWmPY9D9_Tv3BZCJddypHI85hHt2Udoq3mkDn3ty-zB408MF5A7BWDPJ0KFgCCtzfhIUsvrksRFirIOPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیونل مسی در کنار دختر ریاض محرز
😊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/94072" target="_blank">📅 01:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94071">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/suyKSoKH916eL0eTRk5_Q0sKCgh-ulYJeQyMLI67y4ob5FQZdcG_XleqLMYpPJt-RdtbhMlKqvwofveGn6m13v5cvVzvEkByNQXDTJOXVEfoQrrsfMZUUCG-bRuEuP6NAlmokV3WvCbhDssvSlj3opTgp63LO2ugtaPz3jOXAb1xwuAGwpmQDL-FrRP5wrG09nY6Rg3uWy2lYCqo1RlSveNUCDkekrVL0Vk7HbisyiCcPfbhRyy_YiPlZe3Vk6vHVAkRmfZiO5YdH2ovA90ePXvPVD-ZfCmiwF2KUT9vcIFBZ5d8a4E6T6-dg3lKdUr_vW1j8R8eixoyf4QmQaqwdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین گلزنان جام جهانی تا اینجای کار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/94071" target="_blank">📅 01:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94070">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/94070" target="_blank">📅 01:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94069">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WoLTkj0p5NYQOhUyzQZJEp9-KQt_GmH-WkN5tSv92B4nImF_j8GFMZtzMASC9LjxVBVo2lvKvk_CJ4PvB7vyH5L7haGjniUh83CgHsQH6Ar618iaE2V-uUUCGtbhCv5IP-bJyy0caEcWzPm5SF_Zp0t9WeCMnD5wxiU4YkEQYQkGe8aVbf1Z3jrVDbrACrG4YsNHH4KU0qnxny3g-I-_y2KhK2ub5hUv4g1H2cpZFEsUAye3nnZt-8aIxFaJt7ck4FTlkSV8oPMSqOdxXdRZuvYTK3E_KXkylFr1sg-2Jr1tZMFDrCY4si3Nm3eIA-R52pruXegpeprnt7SFEu2Jnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/94069" target="_blank">📅 01:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94068">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/F_X5Y68lfPaDcjzk_r1mlIXzNScvn0rv10mN2ZiNUCvtXbit4UZYydpJ2yIQeuV3IeWWQCEiAgbY-YuU5ZvA7ysguo16EYJu5xGPx7iucUGMhhIdLxAJaQ7LlHeJ4YpqXXy7z5FgrSTgYc0urcssiaCW9ETDKFWDM3U_pujqjzCmFcWAeIhvMjyjMIyaV8JJejN8XpM4PpI4_xleFp73FyS6S8w8_HBMDeITdm2bBiqhUTyvjx7U9-nHEBNNVNXtTtUrB6Nmi7Rp9Tf_P57oYVjq6cE1QxM0BD5njHs0lRadHyffhjx7u-KPPFtaY_dUKQ1f8FaFVw-v3khENkJCIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/94068" target="_blank">📅 01:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94067">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQp1URRudgbs6m8NTKWlAsoPdM4qWtaN9Jn6Lz-cnT3HI3i_PwxwXhz9FdHyRcnQVhdIIFaorfjv1nkouDsQBvrk_I6o9UTvOFM0tTJ-J0UvxIwIrQkuY4YAVWzdUyX5NulsQfYQDW1bhnjgIz8bLJo-N3qEbcOtSriBpV5yX9m2QfAroUV8AmXXsPEfAO0AR4b0Ys8r-mDLxBHO1T92EB5CSLI2z8xt4A1XXqAs2p_zuCZfqKVcexkOcyKh1VWNkcw83QlKkK6OozK6yL4OZPuFOeqGsXwCk-gEuHLEBi03HGgj4OoH3aC-ORWwHxlgpdFPnBwX82rqwMskCOdl1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جود بلینگهام جوانترین بازیکن اروپایی تاریخ شد که در چهار تورنمنت مختلف شرکت کرده است:
• جام ملت های اروپا 2020
• جام جهانی 2022
• جام ملت های اروپا 2024
• جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/94067" target="_blank">📅 01:45 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
